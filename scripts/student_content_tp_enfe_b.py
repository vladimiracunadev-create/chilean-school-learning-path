"""Atención de Enfermería, mención Enfermería (4.º medio TP): OAM-03 (preparar instalaciones, equipos, instrumentos e insumos con asepsia y antisepsia, seguridad y prevención de riesgos biomédicos: solo conceptos, listas de verificación y cálculos de planilla). Todo en papel: servicios, insumos y cifras inventados y rotulados «de ejemplo»; sin técnicas clínicas ni procedimientos."""
from __future__ import annotations

from tp_enfe_common import LIM, build

O3 = "TP-ENFE-4-OAM-03"

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (servicio de procedimientos de ejemplo, inventado). El servicio tiene una sala de procedimientos, una sala de materiales y una sala de residuos. En el turno trabajan 1 enfermera y 2 técnicos. El técnico prepara la sala y los insumos según la lista que escribe el profesional que hará el procedimiento. "
     "Procedimientos programados en el día: 12 curaciones, 6 tomas de muestras y 4 procedimientos menores. Cada procedimiento usa un paquete estéril, y se agregan 2 paquetes de repuesto para el día. Preparar cada procedimiento toma 5 minutos de trabajo. "
     "Regla del servicio: un paquete estéril no se usa si el envase está roto o húmedo, si no tiene indicador de esterilidad o si está vencido.")
build(
    O3, 1, F,
    use="Aprenderé qué hay que tener presente al preparar una sala, un equipo o un insumo, qué riesgos biomédicos existen y qué reglas generales se siguen siempre.",
    prior=["Conozco la prevención de infecciones y la identificación segura.", "Sé multiplicar y sumar números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería (mención Enfermería), preparar es dejar listos la sala, los equipos, los instrumentos y los insumos para que el profesional pueda realizar un procedimiento de forma segura. El técnico prepara según una lista indicada por el profesional, y no agrega ni cambia nada por su cuenta. Los instrumentos son los objetos de trabajo, como pinzas; los insumos son los materiales que se consumen, como gasas o guantes. Los principios son la asepsia (evitar la presencia de microbios), la antisepsia y la seguridad.",
        "Los riesgos biomédicos son los que vienen del trabajo con material de salud: biológico (sangre y fluidos), cortopunzante (objetos que cortan o pinchan) y químico (sustancias de limpieza o desinfección). Para prevenirlos se usan elementos de protección personal, se separan los residuos y se sigue el protocolo del servicio. Un paquete estéril con el envase roto, húmedo, sin indicador o vencido no se usa y se avisa a la enfermera.",
        "Este cuaderno no enseña a preparar ni a esterilizar nada: solo los conceptos y las reglas generales." + LIM,
    ],
    vocab=[("insumo", "material que se consume en un procedimiento, como gasas o guantes"), ("instrumento", "objeto de trabajo que se reutiliza, como una pinza"), ("material estéril", "material libre de toda forma de vida microbiana, con envase íntegro"), ("riesgo biomédico", "riesgo que viene del trabajo con material de salud: biológico, cortopunzante o químico"), ("indicador de esterilidad", "marca que cambia cuando el material pasó por el proceso de esterilización"), ("lista de preparación", "lista que escribe el profesional con lo que se necesita")],
    worked=[
        ("Decidir si se usa un paquete", "Un paquete estéril de ejemplo tiene el envase húmedo. ¿Se usa?", ["La regla dice que un envase húmedo no se usa.", "Se aparta y se avisa a la enfermera."], "No se usa: se aparta y se avisa a la enfermera"),
        ("Contar paquetes", "En otro servicio de ejemplo hay 15 procedimientos y se agregan 3 paquetes de repuesto. ¿Cuántos paquetes se preparan?", ["Se suman un paquete por procedimiento y los de repuesto.", "15 + 3 = 18."], "18 paquetes")],
    mistakes=[("Usar un paquete con el envase roto «porque el material se ve limpio».", "Un envase roto significa que perdió la esterilidad aunque se vea limpio.", "Apártalo y avisa a la enfermera."),
              ("Preparar insumos distintos de los de la lista «porque son parecidos».", "El profesional definió lo que necesita; un cambio puede afectar el procedimiento.", "Prepara solo lo que dice la lista y avisa si falta algo.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un insumo?", "Un material que se consume en un procedimiento, como gasas o guantes", "Un objeto de trabajo que se reutiliza", "Un documento del profesional", "El insumo se consume; el instrumento se reutiliza."),
        ("abc", "{F} ¿Quién escribe la lista de lo que hay que preparar?", "El profesional que hará el procedimiento", "El técnico, según su criterio", "El paciente", "La ficha dice que la lista la escribe el profesional que hará el procedimiento."),
        ("abc", "{F} ¿Qué corresponde hacer con un paquete estéril que no tiene indicador de esterilidad?", "No usarlo y avisar a la enfermera", "Usarlo, si el envase se ve limpio", "Ponerle un indicador nuevo", "La regla del servicio impide usar un paquete sin indicador de esterilidad."),
        ("=", "{F} ¿Cuántos procedimientos hay programados en el día?", "12+6+4", "Se suman las curaciones, las tomas de muestras y los procedimientos menores.", " procedimientos"),
        ("=", "{F} ¿Cuántos paquetes estériles se preparan para el día, contando el repuesto?", "12+6+4+2", "Se suma un paquete por procedimiento más los 2 de repuesto.", " paquetes"),
        ("=", "{F} ¿Cuántos minutos de trabajo suma la preparación de todos los procedimientos del día?", "(12+6+4)*5", "Se multiplican los procedimientos del día por los minutos de preparación de cada uno.", " minutos"),
        ("=", "{F} Si el trabajo de preparación se reparte por igual entre los 2 técnicos, ¿cuántos minutos le corresponden a cada uno?", "(12+6+4)*5//2", "Se divide el total de minutos entre los técnicos.", " minutos"),
        ("abc", "{F} Al preparar, el técnico ve que falta un insumo de la lista y hay otro parecido en la sala. ¿Qué hace?", "Avisa a la enfermera y no cambia el insumo por su cuenta", "Usa el parecido, porque cumple la misma función", "Prepara el procedimiento sin ese insumo", "Solo el profesional decide cambios de insumo."),
        ("abc", "{F} El técnico encuentra un contenedor de cortopunzantes con la tapa suelta y el borde lleno. ¿Qué corresponde?", "No manipularlo y avisar a la enfermera para que se reemplace según el protocolo", "Presionar los objetos para que quepan más", "Vaciarlo en la bolsa común", "Un contenedor lleno se reemplaza según el protocolo; manipularlo aumenta el riesgo de pinchazo."),
        ("abc", "{F} Un técnico se pincha accidentalmente con un objeto cortopunzante al ordenar la sala. ¿Qué hace?", "Avisa de inmediato a la enfermera o profesional responsable y a emergencias, sin actuar por cuenta propia", "Se cura y sigue trabajando sin avisar", "Espera a terminar el turno", "Un accidente con cortopunzante se avisa de inmediato para recibir la atención que corresponde."),
        ("abc", "{F} Un compañero propone «esterilizar» un instrumento con un paño y alcohol «porque no hay tiempo». ¿Qué corresponde responder?", "Que la esterilización la hace personal formado con equipos y protocolos, y que no se improvisa", "Que sí, porque el alcohol esteriliza", "Que sí, si el paciente no se entera", "La esterilización es un proceso especializado y no se improvisa."),
        ("=", "{F} Si el servicio agregara 4 procedimientos más con el mismo repuesto, ¿cuántos paquetes se prepararían?", "12+6+4+4+2", "Se suma un paquete por procedimiento y los 2 de repuesto.", " paquetes"),
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿por qué se usan elementos de protección personal?", "Para protegerse a sí mismo y a las personas de los riesgos biomédicos", "Para reemplazar la higiene de manos", "Para identificar al personal del servicio", "Los elementos de protección reducen la exposición a riesgos biológicos, cortopunzantes y químicos."),
    ],
    ctx=("abc", "{F} Al ordenar la sala, el técnico ve que un frasco de una sustancia de limpieza está sin etiqueta y con olor fuerte. ¿Qué hace?", "No lo toca, se aleja del frasco y avisa de inmediato a la enfermera para que se retire según el protocolo", "Lo huele para identificarlo", "Lo mezcla con otro producto para neutralizar el olor", "Una sustancia sin etiqueta es un riesgo químico; no se manipula ni se mezcla."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿qué haces si un paquete estéril está vencido?", "No lo uso y aviso a la enfermera", "Un paquete vencido no se usa según la regla del servicio."),
        ("¿Qué haces si falta un insumo de la lista?", "Aviso a la enfermera y no lo cambio por mi cuenta", "El cambio lo decide el profesional."),
        ("¿Qué haces si te pinchas con un cortopunzante?", "Aviso de inmediato a la enfermera o profesional responsable y a emergencias", "No actúo por cuenta propia: el aviso inmediato permite recibir la atención que corresponde."),
    ],
    op=("Caso de ejemplo: en un servicio hay 8 curaciones, 4 tomas de muestras y 3 procedimientos menores programados, y se agregan 2 paquetes estériles de repuesto. Preparar cada procedimiento toma 5 minutos y trabajan 3 técnicos. "
        "Calcula: cuántos paquetes se preparan, cuántos minutos suma la preparación y cuántos le tocan a cada técnico. Escribe qué harías si un paquete tiene el envase roto y qué harías si te pinchas con un objeto de la bandeja.",
        "Procedimientos: 8+4+3 = 15; paquetes: 15+2 = 17; minutos: 15 × 5 = 75; por técnico: 75 ÷ 3 = 25. Con el envase roto: no lo uso, lo aparto y aviso a la enfermera. Si me pincho: no actúo por mi cuenta y aviso de inmediato a la enfermera o profesional responsable y a emergencias.",
        ["calcula 17 paquetes y 25 minutos", "no usa el paquete dañado", "avisa de inmediato ante el pinchazo", "no actúa por su cuenta"],
        ["hoja con tres cálculos y dos conductas"],
        ["usar el paquete roto", "no avisar del pinchazo", "calcular mal"],
        "Pregunta: «¿qué haces con el paquete roto?». Debe responder no usarlo y avisar."),
    reinforce="Escribe tres riesgos biomédicos con un ejemplo de cada uno y qué se hace en general para prevenirlos.",
    extend="Explica con un ejemplo inventado por qué un envase roto puede ser un riesgo aunque el material se vea limpio.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (estado de paquetes estériles, de ejemplo). Paquete 1: envase íntegro y seco, indicador con cambio de color, vence dentro de 30 días. Paquete 2: envase roto. Paquete 3: envase íntegro y seco, indicador sin cambio de color. Paquete 4: envase íntegro, indicador con cambio de color, vencido hace 2 días. "
     "Paquete 5: envase íntegro y seco, indicador con cambio de color, vence dentro de 5 días. Paquete 6: envase húmedo. Reglas generales: se usan primero los que vencen antes; el área limpia (material preparado) está separada del área sucia (material usado y residuos); el personal formado esteriliza y desinfecta los equipos según el protocolo. "
     "Tipos de riesgo biomédico: biológico, cortopunzante y químico.")
build(
    O3, 2, F,
    use="Aprenderé a leer el estado de un material estéril, a distinguir área limpia y sucia, a ordenar por vencimiento y a reconocer riesgos biomédicos y los elementos de protección.",
    prior=["Conozco los insumos, los instrumentos y la regla del envase.", "Sé comparar fechas y contar días.", "Sé leer una lista."],
    explain=[
        "Un material estéril es seguro de usar solo si cumple cuatro condiciones: el envase está íntegro y seco, el indicador de esterilidad cambió de color, no está vencido y fue almacenado en el área correspondiente. Si falla una sola, no se usa y se avisa a la enfermera. La regla «primero en vencer, primero en usarse» evita que el material se venza sin usarse.",
        "El área limpia es donde está el material preparado y el área sucia es donde están el material usado y los residuos. Se mantienen separadas para evitar que los microbios pasen de un lado a otro. La limpieza, la desinfección y la esterilización de equipos las hace personal formado según el protocolo; el técnico en formación no las improvisa. Los riesgos biomédicos son el biológico, el cortopunzante y el químico, y se previenen con elementos de protección y reglas de manejo de residuos.",
        "Esta clase es solo conceptual y de lectura de documentos." + LIM,
    ],
    vocab=[("área limpia", "lugar donde está el material preparado y listo para usar"), ("área sucia", "lugar donde están el material usado y los residuos"), ("indicador de esterilidad", "marca que cambia de color si el material pasó por esterilización"), ("vencimiento", "fecha desde la cual el material no debe usarse"), ("primero en vencer, primero en usarse", "regla que ordena el uso de lo que vence antes"), ("desinfección", "reducción de microbios en superficies u objetos")],
    worked=[
        ("Revisar un paquete", "Un paquete de ejemplo tiene el envase íntegro y seco, el indicador sin cambio de color y vigente. ¿Se usa?", ["El indicador sin cambio de color indica que no pasó por esterilización.", "No se usa y se avisa a la enfermera."], "No se usa: el indicador no cambió de color"),
        ("Ordenar por vencimiento", "Dos paquetes de ejemplo vencen, el primero en 4 días y el segundo en 10. ¿Cuál se usa primero?", ["Se usa primero el que vence antes.", "El primero vence en 4 días."], "El que vence en 4 días")],
    mistakes=[("Guardar un paquete usado en el área limpia «para no perderlo».", "Mezcla material usado con material limpio y contamina el área.", "Lleva el material usado al área sucia según el protocolo."),
              ("Usar primero el paquete más nuevo «porque está más lindo».", "El más antiguo puede vencerse sin usarse.", "Usa primero el que vence antes.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es el área limpia?", "El lugar donde está el material preparado y listo para usar", "El lugar donde se guardan los residuos", "El lugar donde se lava la ropa", "El área limpia es para el material preparado."),
        ("abc", "{F} ¿Qué paquete tiene el envase roto?", "El paquete 2", "El paquete 1", "El paquete 5", "La ficha dice que el paquete 2 tiene el envase roto."),
        ("abc", "{F} ¿Qué falla tiene el paquete 3?", "El indicador no cambió de color", "El envase está húmedo", "Está vencido", "El paquete 3 tiene el indicador sin cambio de color."),
        ("abc", "{F} ¿Cuál es la falla del paquete 4?", "Está vencido hace 2 días", "Tiene el envase roto", "Tiene el envase húmedo", "El paquete 4 tiene un vencimiento ya cumplido."),
        ("abc", "{F} ¿Cuántos paquetes de la ficha se pueden usar, es decir, no tienen fallas?", "Dos: los paquetes 1 y 5", "Tres: los paquetes 1, 3 y 5", "Cuatro: los paquetes 1, 3, 4 y 5", "Solo los paquetes 1 y 5 cumplen las cuatro condiciones."),
        ("abc", "{F} Entre los paquetes que se pueden usar, ¿cuál se usa primero?", "El paquete 5, que vence antes", "El paquete 1, que vence en 30 días", "Cualquiera, da lo mismo", "Se usa primero el que vence antes: el paquete 5 vence en 5 días."),
        ("=", "{F} ¿Cuántos paquetes de los 6 hay que apartar y avisar?", "6-2", "Se restan los 2 paquetes aptos del total.", " paquetes"),
        ("=", "{F} ¿Cuántos días más tarde que el paquete 5 vence el paquete 1?", "30-5", "Se restan los días del paquete 5 de los del paquete 1.", " días"),
        ("abc", "{F} Un compañero dice: «El paquete 6 está solo húmedo, se seca y sirve». ¿Qué corresponde responder?", "Que no se usa y se avisa, porque la humedad hace perder la esterilidad", "Que sí, si se seca bien", "Que sí, si se usa de inmediato", "La humedad hace perder la barrera de esterilidad; no se improvisa."),
        ("abc", "{F} Un técnico ve que alguien dejó una bolsa de residuos en el área limpia. ¿Qué hace?", "Avisa a la enfermera o al personal de aseo para que la retiren según el protocolo, y no la deja en el área limpia", "La deja, para que se lleve al final del día", "La tapa con una sábana", "Mezclar áreas contamina el material preparado."),
        ("abc", "{F} Una técnica en formación quiere desinfectar un instrumento con un producto que encontró. ¿Qué corresponde?", "No hacerlo: la desinfección la hace personal formado según el protocolo", "Hacerlo, si el producto huele a limpio", "Hacerlo mezclando dos productos", "La desinfección sigue un protocolo; un producto no identificado es un riesgo químico."),
        ("abc", "{F} Un técnico ve una gasa con sangre sobre la mesa del área limpia. ¿Qué tipo de riesgo representa?", "Biológico", "Químico", "Cortopunzante", "La sangre es un material biológico; no corta ni es una sustancia química."),
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un riesgo cortopunzante?", "El que viene de objetos que pueden cortar o pinchar", "El que viene de sustancias de limpieza", "El que viene de la sangre", "Cortopunzante significa que corta o pincha."),
    ],
    ctx=("abc", "{F} El técnico en formación ve que el envase del paquete 1 tiene una pequeña abolladura pero está íntegro y seco. Es el único paquete apto que queda en la sala. ¿Qué hace?", "Consulta a la enfermera si se puede usar, porque una abolladura puede indicar un daño", "Lo usa, porque está íntegro", "Lo descarta sin avisar", "Una duda sobre el envase se consulta antes de usar."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿qué cuatro condiciones debe cumplir un material estéril?", "Envase íntegro y seco, indicador cambiado, vigente y bien almacenado", "Si falla una, no se usa."),
        ("¿Qué paquete se usa primero?", "El que vence antes", "Así no se vence sin usarse."),
        ("¿Dónde se guarda el material usado?", "En el área sucia", "No se mezcla con el material limpio."),
    ],
    op=("Estado de ejemplo: «Paquete A: envase íntegro y seco, indicador cambiado, vence en 12 días. Paquete B: envase roto. Paquete C: envase íntegro y seco, indicador cambiado, vence en 3 días. Paquete D: envase íntegro, indicador sin cambio, vence en 20 días. Paquete E: envase húmedo». "
        "Escribe: cuáles se pueden usar; cuál usarías primero y por qué; qué harías con los otros; y a quién avisarías.",
        "Se pueden usar A y C. Usaría primero C, que vence en 3 días. B, D y E no se usan: se apartan y se avisa a la enfermera. Aviso a la enfermera.",
        ["identifica A y C como aptos", "elige C primero con razón", "aparta B, D y E", "avisa a la enfermera"],
        ["hoja con dos paquetes aptos, una elección con razón y una conducta para los demás"],
        ["usar el paquete con indicador sin cambio", "elegir A primero", "no avisar a la enfermera"],
        "Pregunta: «¿cuál usas primero, el que vence en 12 días o en 3?». Debe responder el que vence en 3 días."),
    reinforce="Escribe las cuatro condiciones de un material estéril y una falla posible de cada una.",
    extend="Explica con un ejemplo inventado por qué el área limpia y el área sucia deben estar separadas.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (casos y pauta de preparación, de ejemplo). Pauta de seis puntos: (1) sala ordenada y superficies despejadas; (2) insumos de la lista del profesional; (3) material estéril íntegro, con indicador y vigente; (4) elementos de protección personal disponibles; (5) contenedores de residuos y de cortopunzantes en su lugar; (6) registro de lo preparado y aviso de faltantes. "
     "Caso A: el técnico cumple los seis puntos. Caso B: la sala está ordenada y los insumos corresponden, pero un paquete tiene el indicador sin cambio de color y no avisa; cumple los puntos 1, 2, 4 y 5. "
     "Caso C: faltan guantes en la sala, el contenedor de cortopunzantes está lejos y el técnico no avisa de nada; cumple solo los puntos 1, 2 y 3. Caso D: el técnico detecta que falta un insumo, avisa a la enfermera y anota el faltante; todo lo demás está en orden salvo el contenedor de cortopunzantes, que está fuera de lugar; cumple los puntos 1, 2, 3, 4 y 6.")
build(
    O3, 3, F,
    use="Aprenderé a analizar casos de preparación de una sala con una pauta, a reconocer qué falló y a decidir qué se avisa y a quién.",
    prior=["Conozco el material estéril, el área limpia y sucia y los riesgos biomédicos.", "Sé calcular porcentajes de números enteros.", "Conozco la regla de avisar los faltantes."],
    explain=[
        "Analizar un caso de preparación es compararlo con una pauta. Los seis puntos cuidan distintos aspectos: el orden evita accidentes, la lista del profesional asegura que estén los insumos correctos, el material estéril íntegro evita infecciones, los elementos de protección cuidan al personal, los contenedores en su lugar previenen pinchazos y el registro permite saber qué se preparó y qué faltó.",
        "Cuando falta algo o algo no cumple, el técnico no improvisa: avisa a la enfermera y registra el faltante. Improvisar con un insumo equivocado, un material dudoso o un contenedor lejano puede dañar al paciente o al personal. El análisis no busca culpables; busca corregir y evitar que se repita.",
        "Todo se analiza en papel y el cuaderno no enseña a preparar procedimientos." + LIM,
    ],
    vocab=[("pauta de preparación", "lista de puntos que se revisan al preparar una sala"), ("faltante", "insumo que no está y debe avisarse"), ("improvisar", "hacer algo sin seguir el protocolo ni consultar"), ("contenedor fuera de lugar", "contenedor que no está donde el protocolo indica"), ("registro de preparación", "anotación de lo que se preparó y de los faltantes")],
    worked=[
        ("Aplicar un punto", "Un técnico de ejemplo empieza a preparar sin revisar si hay elementos de protección personal disponibles. ¿Qué punto incumple?", ["Los elementos de protección deben estar disponibles antes de preparar.", "Incumple el punto 4."], "El punto 4"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 4 de los 6 puntos. ¿Cuántos puntos le faltan?", ["Se restan los puntos cumplidos del total.", "6 − 4 = 2."], "2 puntos")],
    mistakes=[("No avisar que faltan guantes «porque se puede trabajar sin ellos».", "Se expone al personal a un riesgo biológico.", "Avisa de inmediato a la enfermera y espera la reposición."),
              ("Dejar el contenedor de cortopunzantes en otro rincón «porque estorbaba».", "Un cortopunzante debe poder desecharse de inmediato, cerca del lugar de uso.", "Déjalo en el lugar que indica el protocolo.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué significa improvisar?", "Hacer algo sin seguir el protocolo ni consultar", "Preparar con anticipación", "Anotar con letra clara", "Improvisar es actuar sin el protocolo ni consulta."),
        ("abc", "{F} ¿Qué punto incumple el técnico del caso B?", "El punto 3: material estéril íntegro, con indicador y vigente", "El punto 1: sala ordenada", "El punto 4: elementos de protección", "Uno de los paquetes tiene el indicador sin cambio de color."),
        ("abc", "{F} ¿Qué punto incumple el técnico del caso D?", "El punto 5: contenedores en su lugar", "El punto 6: registro", "El punto 2: insumos", "El contenedor de cortopunzantes está fuera de lugar."),
        ("abc", "{F} ¿Qué casos cumplen los seis puntos?", "Solo el caso A", "Los casos A y D", "Los casos B y C", "Solo el caso A cumple los seis puntos."),
        ("abc", "{F} ¿Cuántos puntos cumple el técnico del caso C?", "Tres", "Cinco", "Seis", "La ficha dice que cumple solo los puntos 1, 2 y 3."),
        ("=", "{F} ¿Cuántos puntos cumplen en total los casos A, B, C y D?", "6+4+3+5", "Se suman los puntos cumplidos por cada caso.", " puntos"),
        ("=", "{F} ¿Qué porcentaje del total de puntos (4 casos de 6 puntos) se cumplió?", "(6+4+3+5)*100//(4*6)", "Se multiplica el total cumplido por 100 y se divide entre los puntos evaluados.", " %"),
        ("=", "{F} ¿Cuántos puntos incumplen en total los casos B, C y D?", "(6-4)+(6-3)+(6-5)", "Se restan los puntos cumplidos de los 6 de cada caso y se suman las fallas.", " puntos"),
        ("abc", "{F} En el caso B, ¿qué debió hacer el técnico con el paquete cuyo indicador no cambió de color?", "Apartarlo y avisar a la enfermera", "Usarlo, porque el envase está íntegro", "Cambiar el indicador por otro", "Un indicador sin cambio de color significa que no está garantizada la esterilidad."),
        ("abc", "{F} En el caso C, faltan guantes. ¿Qué corresponde?", "Avisar de inmediato a la enfermera y no iniciar la preparación sin elementos de protección", "Preparar sin guantes, con cuidado", "Pedir guantes prestados de otra sala sin avisar", "Se avisa y se espera la reposición."),
        ("abc", "{F} Un compañero dice que el caso D «está bien, porque avisó el faltante». ¿Qué corresponde responder?", "Que además debe dejar el contenedor de cortopunzantes en su lugar", "Que tiene razón, porque avisar es lo principal", "Que el contenedor no importa", "Un contenedor fuera de lugar también es un riesgo."),
        ("=", "{F} Si el técnico del caso C hubiera avisado y corregido los puntos 4, 5 y 6, ¿cuántos puntos habría cumplido?", "3+3", "Se suman los tres puntos corregidos a los tres que ya cumplía.", " puntos"),
        ("abc", "{F} Al analizar los casos, la enfermera quiere culpar al técnico del caso C. ¿Qué corresponde?", "Revisar qué falló en el proceso y corregirlo, sin buscar culpables", "Sancionar de inmediato", "Ocultar el caso", "El análisis busca mejorar el proceso de preparación."),
    ],
    ctx=("abc", "{F} Antes de un procedimiento, el técnico en formación ve que no está disponible el contenedor de cortopunzantes y que hay un objeto cortopunzante usado sobre la mesa. El profesional está por llegar. ¿Qué hace?", "No manipula el objeto, avisa a la enfermera y pide que se disponga el contenedor antes de comenzar", "Lo toma con los dedos y lo guarda en un cajón", "Lo tapa con una gasa", "Un cortopunzante expuesto es un riesgo; se avisa y no se manipula sin el contenedor."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿qué haces si falta un insumo?", "Aviso a la enfermera y registro el faltante", "No se improvisa con otro insumo."),
        ("¿Dónde debe estar el contenedor de cortopunzantes?", "En el lugar que indica el protocolo, cerca del uso", "Así se desecha de inmediato sin riesgo."),
        ("¿Cuántos puntos tiene la pauta de la ficha?", "6", "Orden, lista, estéril, protección, contenedores y registro."),
    ],
    op=("Casos de ejemplo: «A: el técnico prepara la sala con los seis puntos cumplidos. B: la sala está ordenada, hay guantes y contenedores en su lugar, pero un paquete tiene el envase roto y el técnico lo deja en la bandeja sin avisar. C: faltan dos insumos de la lista y el técnico los reemplaza con otros distintos sin consultar». "
        "Usa la pauta de la ficha. Escribe: qué puntos incumple cada caso; cuántos puntos se cumplen en total si A cumple 6, B cumple 4 y C cumple 4; y cómo corregirías B y C.",
        "A cumple todos. B incumple el punto 3 (paquete con envase roto) y el 6 (no avisa). C incumple el punto 2 (cambia insumos) y el 6 (no avisa). Total: 6+4+4 = 14 de 18. Corrección: B, apartar el paquete y avisar; C, avisar a la enfermera y esperar la reposición o la indicación del profesional.",
        ["identifica los puntos incumplidos", "calcula 14 de 18", "propone correcciones concretas", "no improvisa"],
        ["hoja con puntos incumplidos, un total y correcciones"],
        ["justificar el reemplazo de insumos", "dejar el paquete roto en la bandeja", "sumar mal"],
        "Pregunta: «¿qué hace el técnico con un insumo que falta?». Debe responder avisar y no cambiarlo."),
    reinforce="Escribe los seis puntos de la pauta con tus palabras y un ejemplo de una falla de cada uno.",
    extend="Explica con un ejemplo inventado por qué improvisar con un insumo puede ser peligroso aunque se parezca al correcto.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (control de insumos, de ejemplo). Paquetes estériles: 60 en bodega, de los cuales 15 vencen dentro de 2 días y los otros 45 vencen en 40 días; consumo diario de ejemplo, 20 paquetes. Guantes: 8 cajas de 100 unidades; consumo diario de ejemplo, 100 guantes. "
     "Regla del servicio: se avisa a la enfermera para reponer cuando el stock alcanza para menos de 3 días y se usan primero los que vencen antes. El pedido de reposición lo hace la enfermera. "
     "Meta de existencias (de ejemplo): tener siempre al menos 10 días de guantes.")
build(
    O3, 4, F,
    use="Aprenderé a calcular la duración de un stock, a ver si lo que vence se alcanza a usar y a calcular cuántos insumos faltan para una meta, con enteros.",
    prior=["Conozco el material estéril y la regla de vencimiento.", "Sé multiplicar, dividir y restar números enteros.", "Sé aplicar una regla de aviso."],
    explain=[
        "El stock de un insumo es la cantidad disponible. Los días que dura se calculan dividiendo el stock entre el consumo diario. Por ejemplo, 90 unidades con un consumo de 30 por día duran 3 días. Si una parte del stock vence antes que el resto, se compara el consumo hasta esa fecha con la cantidad que vence: si el consumo es mayor, se alcanza a usar; si es menor, parte se pierde y se informa.",
        "La regla del servicio dice cuándo avisar para reponer. Una meta de existencias es la cantidad que se quiere tener siempre, por ejemplo al menos 10 días de guantes. La cantidad que falta para la meta es la diferencia entre lo que se necesita y lo que hay. El técnico entrega los datos y la enfermera hace el pedido; nunca se compra ni se pide por cuenta propia.",
        "Los números son de ejemplo para practicar la lectura de una planilla de insumos." + LIM,
    ],
    vocab=[("stock", "cantidad disponible de un insumo"), ("consumo diario", "cantidad que se usa en un día"), ("duración del stock", "días que alcanza el stock, dividiendo entre el consumo diario"), ("meta de existencias", "cantidad que se quiere tener siempre"), ("reposición", "pedido para volver al stock necesario"), ("faltante", "cantidad que falta para llegar a la meta")],
    worked=[
        ("Duración del stock", "Una sala de ejemplo tiene 120 mascarillas y usa 30 por día. ¿Para cuántos días alcanza?", ["Se divide el stock entre el consumo diario.", "120 ÷ 30 = 4."], "4 días"),
        ("Faltante para una meta", "Una meta de ejemplo es tener 500 unidades y hay 380. ¿Cuántas faltan?", ["Se resta lo que hay de la meta.", "500 − 380 = 120."], "120 unidades")],
    mistakes=[("Calcular los días de stock sin considerar que una parte vence antes.", "Se puede creer que todo alcanza, cuando una parte se perderá.", "Compara el consumo hasta el vencimiento con la cantidad que vence."),
              ("Hacer el pedido por cuenta propia «para no esperar».", "El pedido lo hace la enfermera con los datos del servicio.", "Entrega los datos y espera su decisión.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿cómo se calculan los días que dura un stock?", "Se divide el stock entre el consumo diario", "Se multiplica el stock por el consumo diario", "Se suman el stock y el consumo", "Así se sabe cuántos días alcanza lo que hay."),
        ("=", "{F} ¿Para cuántos días alcanza el stock de paquetes estériles?", "60//20", "Se divide el stock entre el consumo diario.", " días"),
        ("abc", "{F} ¿Se cumple la regla de avisar cuando el stock alcanza para menos de 3 días?", "No: el stock de paquetes alcanza para 3 días", "Sí: alcanza para menos de 3 días", "Sí: alcanza para solo 1 día", "Con 3 días no es menos de 3; la regla se cumple cuando baja de 3."),
        ("=", "{F} ¿Cuántos paquetes se alcanzan a consumir en los 2 días que faltan para el vencimiento de los 15 paquetes?", "20*2", "Se multiplica el consumo diario por los 2 días.", " paquetes"),
        ("abc", "{F} Si se usan primero los que vencen antes, ¿se alcanzan a usar los 15 paquetes que vencen en 2 días?", "Sí: en 2 días se consumen 40 paquetes, más que 15", "No: el consumo es menor", "No se puede saber", "Con 40 paquetes consumidos en 2 días, los 15 se usan antes de vencer."),
        ("=", "{F} ¿Cuántos guantes hay en el stock?", "8*100", "Se multiplican las cajas por las unidades de cada caja.", " guantes"),
        ("=", "{F} ¿Para cuántos días alcanza el stock de guantes?", "8*100//100", "Se divide el stock entre el consumo diario.", " días"),
        ("=", "{F} ¿Cuántos guantes se necesitan para cumplir la meta de 10 días?", "10*100", "Se multiplica la meta de días por el consumo diario.", " guantes"),
        ("=", "{F} ¿Cuántos guantes faltan para cumplir la meta de existencias?", "10*100-8*100", "Se resta el stock actual de lo que se necesita para la meta.", " guantes"),
        ("=", "{F} Si cada caja tiene 100 guantes, ¿cuántas cajas faltan para cumplir la meta?", "(10*100-8*100)//100", "Se divide el faltante de guantes entre los guantes de cada caja.", " cajas"),
        ("abc", "{F} El técnico se da cuenta de que faltan cajas de guantes para la meta. ¿Qué hace?", "Informa los datos a la enfermera para que haga el pedido", "Pide las cajas por su cuenta", "Compra guantes con su dinero", "El pedido lo hace la enfermera con los datos que entrega el técnico."),
        ("abc", "{F} Un compañero dice: «No importa que 15 paquetes venzan en 2 días; con tanto stock sobra». ¿Qué corresponde responder?", "Que se usan primero los que vencen antes para no perderlos", "Que tiene razón, porque hay más paquetes", "Que se descartan los 15 ahora", "Usar primero lo que vence evita pérdidas."),
        ("=", "{F} Si el consumo de paquetes subiera a 30 por día, ¿para cuántos días alcanzarían los 60 paquetes?", "60//30", "Se divide el stock entre el nuevo consumo diario.", " días"),
    ],
    ctx=("abc", "{F} Al contar los guantes, el técnico ve que hay solo 2 cajas, no 8 como dice la planilla, y que nadie anotó retiros. ¿Qué hace?", "Informa la diferencia de inmediato a la enfermera, con lo contado, y no ajusta la planilla por su cuenta", "Anota 8 cajas para que coincida", "No dice nada, para evitar problemas", "Una diferencia entre lo contado y lo registrado se informa con datos y no se oculta."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cómo calculas los días de stock?", "Stock ÷ consumo diario", "Así se sabe cuándo avisar para reponer."),
        ("¿Quién hace el pedido de reposición?", "La enfermera", "El técnico informa los datos y la enfermera hace el pedido."),
        ("¿Qué paquetes se usan primero?", "Los que vencen antes", "Así no se vencen sin usarse."),
    ],
    op=("Datos de ejemplo: «Paquetes estériles: 96 en bodega; 18 vencen en 3 días; consumo diario, 24. Mascarillas: 6 cajas de 50; consumo diario, 60; meta: 8 días. Regla: avisar si el stock alcanza para menos de 3 días». "
        "Calcula: los días de stock de paquetes y si se alcanzan a usar los 18 que vencen en 3 días; las mascarillas del stock, los días que duran y cuántas faltan para la meta. Escribe qué avisarías a la enfermera.",
        "Paquetes: 96 ÷ 24 = 4 días; en 3 días se consumen 72 paquetes, más que 18: se alcanzan a usar. Mascarillas: 6×50 = 300; 300 ÷ 60 = 5 días; la meta es 8×60 = 480; faltan 180. Avisaría a la enfermera de los 180 faltantes.",
        ["compara el consumo con los 18 que vencen", "calcula 300, 5 días y 180", "calcula 4 días de paquetes", "avisa a la enfermera"],
        ["hoja con tres cálculos y un aviso"],
        ["no usar primero lo que vence", "calcular mal el faltante", "hacer el pedido por su cuenta"],
        "Pregunta: «¿quién hace el pedido?». Debe responder la enfermera."),
    reinforce="Con 240 unidades y un consumo de 40 por día, calcula los días del stock y cuántas unidades faltan para una meta de 10 días.",
    extend="Explica con un ejemplo inventado por qué se usan primero los insumos que vencen antes.",
)

# ============================================================ OAM-03, clase 5
F = ("Ficha 5 (comparar alternativas, de ejemplo). Dos formas de ordenar una sala de procedimientos. Alternativa A: un carro único con todo el material, limpio y usado. Alternativa B: un carro limpio con el material preparado y un carro sucio con el material usado y los residuos, separados. "
     "Puntaje de 0 a 2 por criterio: A, prevención de infecciones 0, seguridad ante cortopunzantes 1, orden 1, tiempo de preparación 2, protección del personal 1; B, prevención de infecciones 2, seguridad ante cortopunzantes 2, orden 2, tiempo de preparación 1, protección del personal 2. "
     "Tiempo por procedimiento: A, 4 minutos; B, 6 minutos; 14 procedimientos en el día. "
     "Lista de verificación al terminar (6 puntos): material usado en el área sucia; residuos en su recipiente; cortopunzantes en su contenedor; superficies despejadas; elementos de protección retirados y desechados según el protocolo; registro de lo usado y de faltantes.")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos formas de ordenar una sala con criterios, a elegir con justificación y a verificar con una lista al terminar.",
    prior=["Conozco la preparación de la sala, el estéril y el stock.", "Sé sumar puntajes y calcular tiempos.", "Sé leer una lista de verificación."],
    explain=[
        "Comparar dos formas de ordenar una sala es evaluar cada una con los mismos criterios: prevención de infecciones, seguridad ante cortopunzantes, orden, tiempo de preparación y protección del personal. Se da un puntaje de 0 a 2 a cada criterio y se suman. La forma con más puntos suele ser la mejor, pero si una tiene 0 en prevención de infecciones, no se elige aunque sea más rápida.",
        "Al terminar cada procedimiento, el técnico verifica con una lista: el material usado va al área sucia, los residuos a su recipiente, los cortopunzantes a su contenedor, las superficies quedan despejadas, los elementos de protección se retiran y desechan según el protocolo y se registra lo usado y los faltantes. La decisión de cómo ordenar la sala es de la enfermera; el técnico entrega los datos.",
        "Los puntajes y los tiempos son de ejemplo para practicar la comparación." + LIM,
    ],
    vocab=[("alternativa", "una de varias formas posibles de ordenar o hacer algo"), ("criterio", "aspecto con el que se compara una alternativa"), ("carro limpio", "carro con material preparado y listo para usar"), ("carro sucio", "carro con material usado y residuos"), ("lista de verificación", "puntos que se revisan al terminar un procedimiento"), ("decisión", "elección que hace la enfermera con los datos")],
    worked=[
        ("Sumar un puntaje", "Una alternativa de ejemplo tiene infecciones 2, cortopunzantes 1, orden 2, tiempo 1 y protección 2. ¿Cuántos puntos suma?", ["Se suman los cinco puntajes.", "2 + 1 + 2 + 1 + 2 = 8."], "8 puntos"),
        ("Calcular un tiempo", "Una alternativa de ejemplo toma 5 minutos por procedimiento y hay 10 procedimientos. ¿Cuántos minutos suma?", ["Se multiplican los minutos por los procedimientos.", "5 × 10 = 50."], "50 minutos")],
    mistakes=[("Elegir la alternativa más rápida aunque tenga 0 en prevención de infecciones.", "La prevención de infecciones es una condición, no un criterio más.", "Antes de sumar, descarta lo que tenga 0 en prevención de infecciones."),
              ("Marcar la lista sin mirar la sala.", "Una verificación sin observar no previene errores.", "Mira cada punto antes de marcar.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Enfermería): ¿qué es un criterio?", "Un aspecto con el que se compara una alternativa", "Una orden del médico", "El horario del servicio", "Los criterios permiten comparar alternativas de la misma forma."),
        ("=", "{F} ¿Cuántos puntos suma la alternativa A?", "0+1+1+2+1", "Se suman los cinco puntajes de la alternativa A.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la alternativa B?", "2+2+2+1+2", "Se suman los cinco puntajes de la alternativa B.", " puntos"),
        ("abc", "{F} ¿Cuál es la alternativa más conveniente?", "La alternativa B", "La alternativa A", "Ambas por igual", "La alternativa B suma más puntos y no tiene 0 en prevención de infecciones."),
        ("abc", "{F} ¿Por qué la alternativa A no se elige aunque es más rápida?", "Porque tiene 0 en prevención de infecciones", "Porque tiene muy pocos puntos de orden", "Porque usa un solo carro", "Un 0 en prevención de infecciones es una condición que impide elegirla."),
        ("=", "{F} ¿Cuántos minutos suma la preparación de los 14 procedimientos con la alternativa A?", "14*4", "Se multiplican los procedimientos por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma la preparación de los 14 procedimientos con la alternativa B?", "14*6", "Se multiplican los procedimientos por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántos minutos más toma la alternativa B que la A en el día?", "14*6-14*4", "Se restan los minutos de A de los de B.", " minutos"),
        ("abc", "{F} Al terminar un procedimiento, el técnico deja un objeto cortopunzante sobre la mesa limpia. ¿Qué punto de la lista incumple?", "El de cortopunzantes en su contenedor", "El de registro", "El de elementos de protección", "Un cortopunzante debe ir en su contenedor."),
        ("abc", "{F} Al verificar, el técnico nota que la bolsa de residuos está llena y no hay otra. ¿Qué hace?", "Avisa a la enfermera para que se reponga según el protocolo", "Presiona los residuos para que quepan más", "La deja en el pasillo", "Un recipiente lleno se repone; manipular el contenido aumenta el riesgo."),
        ("abc", "{F} Un compañero dice: «B toma 2 minutos más, mejor usamos A». ¿Qué corresponde responder?", "Que la prevención de infecciones es una condición y B protege mejor", "Que tiene razón, por el tiempo", "Que no importa el puntaje", "El tiempo no justifica elegir una alternativa con 0 en prevención de infecciones."),
        ("abc", "{F} La lista de verificación pide registrar los faltantes. ¿Por qué?", "Para que la enfermera pueda reponer a tiempo", "Para culpar a alguien", "Para que el paciente lo vea", "El registro permite reponer a tiempo y evitar improvisaciones."),
        ("=", "{F} Si el servicio hiciera 6 procedimientos más con la alternativa B, ¿cuántos minutos suma en total?", "(14+6)*6", "Se multiplican los procedimientos totales por los minutos de cada uno.", " minutos"),
    ],
    ctx=("abc", "{F} Al terminar el último procedimiento del turno, el técnico ve que quedan material usado y una bolsa de residuos en el carro limpio. El turno se acaba en 5 minutos. ¿Qué hace?", "Lleva lo usado al área sucia según el protocolo o avisa a la enfermera si no alcanza, y lo deja registrado", "Lo deja ahí para el turno siguiente", "Lo oculta debajo del carro", "No se mezcla lo usado con lo limpio; si no se alcanza, se avisa."),
    sc=[
        ("En Atención de Enfermería (mención Enfermería): ¿cómo se elige entre dos formas de ordenar?", "Se comparan con los mismos criterios y se suman los puntajes", "Se evita elegir solo por rapidez."),
        ("¿Qué condición impide elegir una alternativa?", "Tener 0 en prevención de infecciones", "Es una condición, no un punto más."),
        ("¿Quién decide cómo se ordena la sala?", "La enfermera", "El técnico entrega los datos y la enfermera decide."),
    ],
    op=("Alternativas de ejemplo: «A: todo en un carro, 3 minutos por procedimiento; puntaje: infecciones 0, cortopunzantes 1, orden 1, tiempo 2, protección 1. B: carro limpio y carro sucio, 5 minutos; puntaje: infecciones 2, cortopunzantes 2, orden 2, tiempo 1, protección 2». 12 procedimientos al día. "
        "Calcula: los puntos de cada alternativa; los minutos de cada una en el día y la diferencia. Escribe cuál elegirías y por qué, y tres puntos de la lista de verificación que revisarías al terminar.",
        "A: 0+1+1+2+1 = 5 puntos; B: 2+2+2+1+2 = 9 puntos. Minutos: A, 12×3 = 36; B, 12×5 = 60; diferencia: 24 minutos. Elegiría B: tiene más puntos y A tiene 0 en prevención de infecciones. Puntos de la lista: material usado en el área sucia, cortopunzantes en su contenedor y registro de faltantes.",
        ["calcula 5 y 9 puntos", "calcula 36, 60 y 24 minutos", "elige B con razón", "nombra tres puntos de verificación"],
        ["hoja con dos puntajes, tres tiempos, una elección y tres puntos"],
        ["elegir A por rapidez", "sumar mal", "olvidar el registro de faltantes"],
        "Pregunta: «¿por qué no se elige A aunque es más rápida?». Debe responder por el 0 en prevención de infecciones."),
    reinforce="Elige una forma de ordenar una sala de ejemplo, califícala de 0 a 2 en los cinco criterios y suma el puntaje.",
    extend="Explica con un ejemplo inventado por qué ahorrar tiempo no justifica descuidar la prevención de infecciones.",
)
