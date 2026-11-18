"""Agropecuaria TP 3.º medio: OAE-01 (preparar el suelo) y OAE-02 (regar y drenar), clases 1 a 5 cada una. Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agro_common import AVISO, EMER, build

O1 = "TP-AGRO-3-OAE-01"
O2 = "TP-AGRO-3-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Fundo Demo» es un predio ficticio de 60 hectáreas repartidas en 5 potreros iguales. Se planea preparar el suelo de un potrero para sembrar maíz. "
     "Peligros anotados: un tractor con implementos pesados, polvo en suspensión, un potrero con pendiente, una acequia (canal pequeño de riego) sin tapa junto al camino y el ruido constante de la maquinaria.")
build(
    O1, 1, F,
    use="Aprenderé qué es preparar el suelo, qué son la erosión y la compactación, cómo se distinguen peligro y riesgo y cómo se ordenan las medidas de prevención en un predio.",
    prior=["Sé leer una ficha escrita y una lista de datos.", "Sé sumar, restar, multiplicar y dividir números enteros.", "Sé que las plantas crecen con agua, luz y nutrientes del suelo."],
    explain=[
        "El suelo es la capa superficial de la tierra donde crecen las raíces, y es un recurso que se gasta si se maltrata. Preparar el suelo es dejarlo listo para recibir semillas o plantas: se hace con labranza (labores que remueven la tierra), con maquinaria e implementos, que son herramientas que se acoplan a un tractor, y con insumos, es decir, productos que se agregan al cultivo. La erosión es el arrastre de suelo por el viento o el agua; la compactación es el apretamiento del suelo, que deja menos espacio para el aire y el agua.",
        "Todo trabajo tiene peligros, que son fuentes de daño, y riesgos, que son la posibilidad de que ese daño ocurra. La jerarquía de controles ordena las medidas de la más a la menos efectiva: eliminar el peligro, sustituirlo por otro menor, cambiar físicamente el lugar o el equipo (control de ingeniería), dar reglas, señales y capacitación (control administrativo) y, al final, el equipo de protección personal (EPP). Un arco antivuelco de un tractor es un control de ingeniería.",
        f"Las labores con tractor las hace solo una persona capacitada, autorizada y con la norma vigente al día. Además, cuidar el suelo es parte del trabajo: se evita dejarlo sin cobertura y se consulta a un asesor técnico antes de trabajar con pendiente. {EMER} {AVISO}",
    ],
    vocab=[("suelo", "capa superficial de la tierra donde crecen las raíces"), ("labranza", "conjunto de labores que remueven el suelo para sembrar"), ("implemento", "herramienta que se acopla al tractor para trabajar el suelo"), ("insumo", "producto que se agrega al cultivo, como un abono"), ("erosión", "arrastre de suelo por el viento o el agua"), ("compactación", "apretamiento del suelo que deja menos aire y agua"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Peligro y riesgo", "En otro predio de ejemplo hay un pozo de agua sin tapa junto a la bodega. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es el pozo sin tapa, porque puede causar daño.", "El riesgo es que una persona que pasa por ahí caiga dentro y se lastime."], "Peligro: el pozo sin tapa; riesgo: que alguien caiga y se lastime"),
        ("Clasificar un control", "Un predio de ejemplo escribe la regla «no se llevan acompañantes sobre el tractor» y la pega en la bodega. ¿Qué tipo de control es?", ["La medida no cambia el tractor: ordena una conducta.", "Las reglas y señales son controles administrativos."], "Control administrativo"),
    ],
    mistakes=[("Creer que usar guantes y casco basta para trabajar seguro con el tractor.", "El EPP es la última barrera: no quita el peligro y protege solo a quien lo usa.", "Primero se controla el peligro; el EPP se suma a esas medidas."),
              ("Creer que haber visto el concepto en clases habilita para conducir un tractor.", "Las labores con maquinaria exigen autorización, instructor y norma vigente.", "Aprende aquí el concepto y deja la labor a personal autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la erosión del suelo?", "El arrastre de suelo por el viento o el agua", "El apretamiento del suelo que deja menos aire y agua", "La mezcla de abonos con la tierra antes de sembrar", "La erosión es arrastre de suelo; el apretamiento es compactación y los abonos son insumos."),
        ("abc", "En Agropecuaria: ¿qué es la compactación del suelo?", "El apretamiento del suelo, que deja menos espacio para aire y agua", "El arrastre de suelo por el viento o el agua", "La remoción de la tierra con un implemento", "La compactación aprieta el suelo; el arrastre es erosión y remover la tierra es labranza."),
        ("abc", "En Agropecuaria: ¿qué es un implemento agrícola?", "Una herramienta que se acopla al tractor para trabajar el suelo", "Un producto que se agrega al suelo para alimentar al cultivo", "La persona autorizada que conduce el tractor", "El implemento es una herramienta acoplable; el producto es un insumo y la persona es el operador."),
        ("=", "{F} Se preparan 4 hectáreas por jornada. ¿Cuántas jornadas necesita uno de los potreros de la ficha?", "60//5//4", "Se divide el predio entre los potreros y luego entre las hectáreas por jornada.", " jornadas"),
        ("abc", "{F} El arco antivuelco del tractor es un control de tipo:", "De ingeniería, porque es una estructura física del equipo", "Administrativo, porque es una regla escrita", "De EPP, porque protege a quien conduce", "El arco es una estructura física del equipo y no depende de que alguien lo recuerde."),
        ("abc", "{F} Una regla que dice «solo conduce el tractor quien tiene autorización» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el tractor", "De sustitución, porque cambia a la persona", "Una regla escrita es un control administrativo; no cambia el equipo ni elimina el peligro."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al polvo en suspensión?", "Que una persona sufra molestias o daño respiratorio al respirarlo", "El polvo mismo flotando en el aire", "Que falte tierra en el potrero", "El riesgo es la posibilidad de daño; el polvo flotando es el peligro."),
        ("abc", "{F} Un estudiante dice: «sé andar en bicicleta, así que puedo manejar el tractor del fundo». ¿Qué respuesta es correcta?", "Es falso: conducir el tractor exige formación, autorización y norma vigente", "Es cierto, si va despacio", "Es cierto, si lleva casco", "La velocidad o el casco no reemplazan la autorización ni la formación."),
        ("abc", "{F} En una visita, un tractor se inclina por la pendiente y se desliza hacia la acequia. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo y avisar a un adulto responsable y a emergencias", "Correr a sujetar el tractor para frenarlo", "Meterte a la acequia para sacar al conductor", "Intervenir sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Agropecuaria: ¿por qué un suelo sin cobertura queda más expuesto a la erosión?", "Porque el viento y la lluvia pueden arrastrar sus partículas sin nada que lo proteja", "Porque al estar compactado el viento lo levanta con más facilidad", "Porque la maquinaria nunca pasa por ese suelo", "Sin cobertura nada frena el arrastre; la compactación y la maquinaria no explican por sí solas ese efecto."),
        ("abc", "{F} Se propone solo entregar protectores auditivos contra el ruido. ¿Qué medida es más efectiva en la jerarquía de controles?", "Usar un equipo más silencioso o con cabina cerrada, que baja el ruido en su origen", "Colocar un letrero que diga «hay ruido»", "Entregar el mismo protector a más personas", "Actuar sobre el origen del ruido está más arriba que un letrero o un EPP."),
        ("=", "{F} Un tractor de ejemplo prepara 3 hectáreas por hora y trabaja 4 horas por jornada. ¿Cuántas jornadas se necesitan para preparar las 60 hectáreas completas del fundo?", "60//(3*4)", "Se calculan las hectáreas por jornada y se divide el predio entre ellas.", " jornadas"),
        ("abc", "En Agropecuaria: ¿por qué sustituir un peligro es mejor que depender solo del EPP?", "Porque la sustitución reduce el peligro en su origen y el EPP protege solo a quien lo usa", "Porque el EPP elimina el peligro, pero es más caro", "Porque la sustitución se usa solo cuando el EPP ya falló", "Los niveles altos de la jerarquía actúan sobre el peligro; el EPP no lo elimina."),
    ],
    ctx=("abc", "Un vecino te ofrece pagarte por conducir su tractor «porque ya viste cómo se hace en clases». ¿Qué respondes?", "Que no, porque esa tarea exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si el potrero es pequeño", "Que sí, pero solo en terreno plano", "Haber visto el concepto no habilita para conducir; el tamaño o la pendiente del potrero tampoco."),
    sc=[
        ("En Agropecuaria: ¿qué es un peligro?", "Una fuente que puede causar daño, como una acequia sin tapa", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En el trabajo agrícola: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no elimina el peligro."),
        ("En Agropecuaria: ¿qué es preparar el suelo?", "Dejarlo listo para recibir semillas o plantas", "Preparar el suelo es dejarlo en condiciones de siembra o plantación."),
    ],
    op=("El predio ficticio «Fundo Demo» anota una tarea de ejemplo: trasladar un tractor por un camino de tierra con baches y una zanja al costado, a media tarde y con sol fuerte. Escribe (a) cuál es el peligro de la zanja y cuál el riesgo asociado, (b) un control administrativo para el camino, (c) un control de ingeniería para el mismo camino, (d) por qué el EPP no basta.",
        "(a) Peligro: la zanja junto al camino; riesgo: que el tractor se desvíe, caiga a la zanja y se dañe la persona que lo conduce. (b) Un letrero de velocidad máxima y una regla de no circular de noche. (c) Rellenar y nivelar el camino o poner una baranda junto a la zanja, hecho por personal autorizado. (d) Porque el EPP es la última barrera: no quita el peligro y protege solo a quien lo usa. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "explica por qué el EPP no basta"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "no aclarar que la tarea la hace personal autorizado"],
        "Pregunta: «¿qué control cambia el camino y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el nivel de ingeniería."),
    reinforce="Escribe la jerarquía de controles en orden y pon junto a cada nivel un ejemplo inventado de un predio agrícola.",
    extend="Explica con un ejemplo por qué una charla de seguridad es un control administrativo y no reemplaza una medida de ingeniería.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (informe de laboratorio de ejemplo, inventado). Análisis de suelo del Potrero 3 del «Fundo Demo», cultivo planeado: maíz. Resultados de ejemplo: pH 5; materia orgánica 2 %; textura: arena 30 %, limo 25 % y arcilla el resto. "
     "Rango recomendado de ejemplo para ese cultivo: pH entre 6 y 7; materia orgánica de 3 % o más. Documentos del predio: el informe de análisis (resultados del laboratorio), la orden de trabajo (qué labor, dónde y cuándo) y el registro de labores (lo que se hizo y quién lo hizo).")
build(
    O1, 2, F,
    use="Aprenderé los conceptos de textura, pH y materia orgánica, cómo se lee un informe de análisis de suelo y qué rol cumple cada persona en la preparación del suelo.",
    prior=["Sé qué es el suelo, la erosión y la compactación.", "Sé leer una ficha con datos.", "Sé sumar y restar porcentajes enteros."],
    explain=[
        "La textura del suelo es la proporción de sus partículas según su tamaño: arena (las más gruesas, que dejan pasar el agua rápido), limo (de tamaño medio) y arcilla (las más finas, que retienen agua y se aprietan con facilidad). Las tres suman 100 %. El pH mide si el suelo es ácido (menor que 7), neutro (igual a 7) o alcalino (mayor que 7). La materia orgánica son los restos de plantas y animales descompuestos; mejora la estructura del suelo y su capacidad de retener agua.",
        "Un análisis de suelo se hace en un laboratorio a partir de una muestra, que es una porción pequeña del suelo que representa al potrero. El resultado llega en un informe con cada valor y su unidad. El asesor técnico, que es el profesional que interpreta el informe, compara los resultados con el rango recomendado para el cultivo. El jefe de campo organiza el trabajo y entrega la orden de trabajo, y el operador autorizado ejecuta las labores con maquinaria.",
        f"Los documentos dejan evidencia: el informe respalda las decisiones, la orden de trabajo dice qué se hará y el registro de labores anota lo realizado. Un registro no se cambia para que «se vea mejor». {EMER} {AVISO}",
    ],
    vocab=[("textura", "proporción de arena, limo y arcilla de un suelo"), ("arcilla", "partículas muy finas del suelo, que retienen agua"), ("pH", "medida de si el suelo es ácido, neutro o alcalino"), ("materia orgánica", "restos de plantas y animales descompuestos en el suelo"), ("muestra", "porción pequeña de suelo que representa al potrero"), ("asesor técnico", "profesional que interpreta el informe y recomienda"), ("orden de trabajo", "documento que dice qué labor se hace, dónde y cuándo"), ("registro de labores", "documento donde se anota lo que se hizo y quién lo hizo")],
    worked=[
        ("Completar la textura", "Un suelo de ejemplo tiene 40 % de arena y 35 % de limo. ¿Qué porcentaje de arcilla tiene?", ["Arena, limo y arcilla suman 100 %.", "Se suman arena y limo: 40 más 35 es 75.", "A 100 se le resta 75."], "25 % de arcilla"),
        ("Leer un valor", "Otro informe de ejemplo dice «pH 8». ¿El suelo es ácido, neutro o alcalino?", ["El pH 7 es neutro.", "Un valor mayor que 7 indica suelo alcalino."], "Alcalino"),
    ],
    mistakes=[("Creer que un pH de 5 es alcalino porque el número es bajo.", "Se confunde la escala: los valores menores que 7 son ácidos.", "Compara siempre con el 7, que es neutro."),
              ("Cambiar un resultado del informe para que cumpla el rango.", "Un dato alterado oculta un problema real y quita validez al documento.", "Se usa el valor real y se informa la diferencia al asesor técnico.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la textura de un suelo?", "La proporción de arena, limo y arcilla que contiene", "La cantidad de agua que tiene en un día", "El color que tiene al estar seco", "La textura describe el tamaño de las partículas; el agua y el color son otras características."),
        ("abc", "En Agropecuaria: ¿qué indica el pH de un suelo?", "Si es ácido, neutro o alcalino", "Cuántas raíces caben en él", "Cuántos residuos de plantas tiene", "El pH mide la acidez o alcalinidad; las raíces y los residuos son otras cosas."),
        ("abc", "En Agropecuaria: ¿qué es una muestra de suelo?", "Una porción pequeña que representa al potrero", "Un potrero completo preparado para sembrar", "Un informe con la receta de abonos", "La muestra es la porción que va al laboratorio; el informe es el resultado, no la muestra."),
        ("=", "{F} ¿Qué porcentaje de arcilla tiene el suelo de la ficha?", "100-30-25", "Las tres partículas suman 100, así que se restan arena y limo.", " %"),
        ("abc", "{F} Según la ficha, ¿el suelo del Potrero 3 es ácido, neutro o alcalino?", "Ácido, porque su pH es menor que 7", "Neutro, porque está cerca del rango recomendado", "Alcalino, porque cualquier valor distinto de 7 es alcalino", "Un pH menor que 7 es ácido; el rango recomendado no cambia esa clasificación."),
        ("abc", "{F} ¿Qué documento dice qué labor se hará, en qué potrero y cuándo?", "La orden de trabajo", "El informe de análisis", "El registro de labores", "La orden indica lo que se hará; el informe entrega resultados y el registro anota lo ya realizado."),
        ("abc", "{F} ¿El pH del informe cumple el rango recomendado de ejemplo?", "No, porque 5 está por debajo de 6", "Sí, porque 5 está entre 6 y 7", "Sí, porque cualquier valor de pH sirve", "El rango pedido es de 6 a 7 y el valor medido es 5, que queda fuera."),
        ("abc", "{F} ¿Quién interpreta el informe y lo compara con el rango del cultivo?", "El asesor técnico", "El operador que conduce el tractor", "El encargado de la bodega", "Interpretar resultados es función del asesor técnico; el operador ejecuta labores."),
        ("abc", "{F} Una estudiante dice: «con este informe ya sé qué labor y qué insumo aplicar, así que lo hago yo sola». ¿Qué respuesta es correcta?", "Es falso: la decisión la toma el asesor técnico y el trabajo lo hace personal autorizado", "Es cierto, si el informe está completo", "Es cierto, si lo aprueba un compañero de curso", "Un informe no habilita para aplicar insumos ni para usar maquinaria."),
        ("abc", "{F} El jefe de campo pide anotar en el informe pH 6 para que cumpla el rango. ¿Qué corresponde?", "No alterar el informe, usar el valor real de 5 e informar al asesor técnico", "Anotar 6, porque el rango es lo importante", "Borrar el pH y dejar el casillero vacío", "Un registro alterado o incompleto pierde validez y oculta el problema."),
        ("=", "{F} Se toman 8 submuestras de 250 gramos del potrero y se juntan en una sola muestra. ¿Cuántos gramos tiene la muestra?", "8*250", "Se multiplica el número de submuestras por el peso de cada una.", " gramos"),
        ("abc", "{F} La materia orgánica medida es de 2 % y se pide 3 % o más. ¿Qué conclusión es correcta?", "Está por debajo del mínimo pedido y se informa al asesor técnico", "Está sobre el mínimo, porque 2 es menor que 3", "Es igual al mínimo, porque ambos números son bajos", "Un 2 % es menos que el 3 % pedido, así que no cumple."),
        ("abc", "En Agropecuaria: ¿por qué un suelo con mucha arcilla se aprieta con más facilidad que uno con mucha arena?", "Porque sus partículas son más finas y quedan muy juntas", "Porque la arcilla es más gruesa y pesa más", "Porque la arena retiene más agua que la arcilla", "Las partículas finas de la arcilla se compactan; la arena es gruesa y deja pasar el agua."),
    ],
    ctx=("abc", "Una conocida te propone «preparar» el registro de labores con labores que aún no se han hecho, para tenerlo listo antes de una revisión. ¿Qué respondes?", "Que no, porque un registro solo anota lo realizado, y que cualquier duda se consulta con un adulto responsable", "Que sí, si después se hacen las labores", "Que sí, pero solo las más importantes", "Anotar lo que no ocurrió es falsear el registro, aunque luego se haga o sea poco."),
    sc=[
        ("En Agropecuaria: ¿qué es la materia orgánica del suelo?", "Restos de plantas y animales descompuestos que mejoran el suelo", "La materia orgánica mejora la estructura y la retención de agua."),
        ("En el trabajo agrícola: ¿para qué sirve el registro de labores?", "Para anotar lo que se hizo y quién lo hizo", "El registro deja evidencia de lo realizado."),
        ("En Agropecuaria: ¿qué suman la arena, el limo y la arcilla de un suelo?", "100 %", "Las tres partículas forman el total del suelo."),
    ],
    op=("Informe de ejemplo del Potrero 7 del «Fundo Demo»: pH 9; materia orgánica 4 %; textura: arena 20 %, limo 45 % y arcilla el resto. Rango recomendado de ejemplo para el cultivo: pH entre 6 y 7; materia orgánica de 3 % o más. Escribe (a) el porcentaje de arcilla, (b) si el suelo es ácido, neutro o alcalino y si cumple el rango de pH, (c) si cumple la materia orgánica, (d) a quién entregas la interpretación del informe.",
        "(a) 100 − 20 − 45 = 35 % de arcilla. (b) Es alcalino, porque 9 es mayor que 7, y no cumple el rango de 6 a 7. (c) Sí cumple, porque 4 % es mayor que 3 %. (d) Al asesor técnico, que decide qué hacer; las labores las hace personal autorizado.",
        ["calcula bien la arcilla", "clasifica el pH y lo compara con el rango", "compara la materia orgánica", "nombra al asesor técnico"],
        ["hoja con las cuatro respuestas"],
        ["no restar los dos porcentajes de 100", "decir que 9 es ácido", "decidir por cuenta propia qué insumo aplicar"],
        "Pregunta: «¿9 está arriba o abajo del 7?». Si no responde, pídele que relea la explicación sobre el pH."),
    reinforce="Escribe tres textura inventadas de suelos (arena, limo y arcilla) que sumen 100 % y marca cuál tendría más arcilla.",
    extend="Explica con un ejemplo por qué el informe de análisis y el registro de labores son documentos distintos.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). El «Fundo Demo» evalúa dos potreros antes de sembrar. Potrero Norte: pendiente fuerte, suelo desnudo sin restos de cultivo y lluvias intensas en la zona. "
     "Potrero Sur: terreno plano, con restos de cultivo del año anterior (rastrojo) que cubren 60 % del suelo, y señales de compactación en los caminos de las máquinas. "
     "Tipos de labranza (conceptos): convencional (remueve mucho el suelo), mínima (remueve poco) y cero (siembra sin remover, sobre el rastrojo).")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso escrito de preparación de suelo, a distinguir tipos de labranza y a justificar qué criterio técnico se aplica según las condiciones del terreno.",
    prior=["Sé qué es la erosión y la compactación.", "Sé leer una ficha con datos.", "Sé calcular porcentajes enteros."],
    explain=[
        "En la labranza convencional se remueve mucho el suelo, lo que lo deja suelto pero expuesto al viento y a la lluvia. En la labranza mínima se remueve solo lo necesario, y en la labranza cero se siembra sin remover, sobre el rastrojo, que son los restos de cultivos anteriores. El rastrojo protege al suelo del golpe de la lluvia, retiene humedad y reduce la erosión; por eso, cuanto más porcentaje del suelo cubre, mejor lo protege.",
        "Para analizar un caso se leen las condiciones: pendiente, cobertura, compactación y clima. Luego se relaciona cada condición con un riesgo: una pendiente fuerte con suelo desnudo y lluvias intensas aumenta el riesgo de erosión; un suelo compactado en los caminos de las máquinas tiene menos aire y agua para las raíces. La decisión se justifica con dos evidencias del caso, y la toma el asesor técnico, no quien lee un cuaderno.",
        f"Un buen análisis dice qué elige, con qué evidencia y qué cambiaría si una condición cambia. Ninguna labor se ejecuta sin autorización y sin norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("rastrojo", "restos de cultivos anteriores que quedan sobre el suelo"), ("labranza convencional", "labranza que remueve mucho el suelo"), ("labranza mínima", "labranza que remueve solo lo necesario"), ("labranza cero", "siembra sin remover el suelo, sobre el rastrojo"), ("cobertura", "porcentaje del suelo cubierto por plantas o rastrojo"), ("pendiente", "inclinación del terreno"), ("evidencia", "dato del caso que respalda una decisión")],
    worked=[
        ("Calcular lo descubierto", "Un potrero de ejemplo tiene 30 % de su suelo cubierto con rastrojo. ¿Qué porcentaje queda descubierto?", ["El total es 100 %.", "Se resta lo cubierto: 100 menos 30."], "70 % descubierto"),
        ("Relacionar condición y riesgo", "Un potrero de ejemplo es plano, tiene suelo desnudo y no llueve mucho. ¿Cuál es su riesgo de erosión por lluvia comparado con uno de pendiente fuerte?", ["La pendiente fuerte hace que el agua corra y arrastre más suelo.", "En el plano de ejemplo el agua corre menos."], "Menor, porque sin pendiente el agua arrastra menos suelo"),
    ],
    mistakes=[("Elegir siempre la labranza que remueve más el suelo porque «deja la tierra más blanda».", "Un suelo muy removido y desnudo queda expuesto a la erosión.", "Se elige según pendiente, cobertura y clima, con apoyo del asesor técnico."),
              ("Dar una conclusión sin citar evidencia del caso.", "Sin dato del caso la decisión no se puede verificar.", "Cita al menos dos evidencias, como la pendiente y la cobertura.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el rastrojo?", "Los restos de cultivos anteriores que quedan sobre el suelo", "El abono que se agrega antes de sembrar", "La tierra suelta que queda tras remover el suelo", "El rastrojo son restos de cultivos; el abono es un insumo y la tierra suelta es resultado de la labranza."),
        ("abc", "En Agropecuaria: ¿qué es la labranza cero?", "Sembrar sin remover el suelo, sobre el rastrojo", "Remover mucho el suelo antes de sembrar", "No sembrar nada en el potrero", "La labranza cero siembra sin remover; la que remueve mucho es la convencional."),
        ("abc", "En Agropecuaria: ¿qué es la cobertura del suelo?", "El porcentaje del suelo cubierto por plantas o rastrojo", "La capa de pintura que se usa para marcar potreros", "La cantidad de agua que cae en un año", "La cobertura protege al suelo; no es una pintura ni la lluvia."),
        ("=", "{F} ¿Qué porcentaje del suelo del Potrero Sur queda descubierto?", "100-60", "Se resta al total lo que cubre el rastrojo.", " %"),
        ("abc", "{F} ¿Qué condición del Potrero Norte aumenta más su riesgo de erosión?", "Pendiente fuerte con suelo desnudo y lluvias intensas", "Tener un rastrojo que cubre el suelo", "Ser un terreno plano", "El agua corre rápido por la pendiente y sin cobertura arrastra suelo."),
        ("abc", "{F} ¿Qué evidencia del Potrero Sur indica compactación?", "Señales de compactación en los caminos de las máquinas", "Que el terreno sea plano", "Que haya rastrojo cubriendo el suelo", "La ficha dice que la compactación aparece en los caminos de las máquinas."),
        ("abc", "{F} Para el Potrero Sur, ¿qué labranza aprovecha mejor el rastrojo que ya protege el suelo?", "La labranza cero o la mínima, que dejan el rastrojo sobre el suelo", "La convencional, que lo remueve y lo deja descubierto", "Ninguna, porque el rastrojo impide sembrar", "Mantener el rastrojo conserva la protección que ya existe."),
        ("abc", "{F} Una estudiante dice: «ya decidí la labranza del Potrero Norte y la haré yo con el tractor del fundo». ¿Qué respuesta es correcta?", "Es falso: la decisión la toma el asesor técnico y la ejecuta personal autorizado", "Es cierto, si usa el casco", "Es cierto, si el potrero está seco", "El análisis en papel no habilita para ejecutar labores con maquinaria."),
        ("abc", "{F} Si en el Potrero Norte el 50 % de su suelo se cubriera con rastrojo, ¿cómo cambiaría su riesgo de erosión?", "Bajaría, porque el rastrojo protege al suelo del agua que corre", "Subiría, porque el rastrojo suelta el suelo", "No cambiaría, porque la pendiente es la misma", "Aunque la pendiente no cambie, la cobertura frena el arrastre."),
        ("abc", "{F} Un operador autorizado vio en el Potrero Norte un surco profundo que arrastra suelo y quiere arreglarlo con su tractor un día de lluvia fuerte. ¿Qué corresponde?", "Detener la labor, avisar al jefe de campo y esperar condiciones seguras", "Seguir trabajando, porque la lluvia ayuda a ver el surco", "Pedir a un estudiante que lo ayude a guiar el tractor", "Con lluvia fuerte y pendiente se detiene la labor y se informa; nadie sin autorización debe intervenir."),
        ("=", "{F} Un potrero de 12 hectáreas tiene 25 % de pendiente fuerte. ¿Cuántas hectáreas son de pendiente fuerte?", "12*25//100", "Se calcula el porcentaje sobre el total de hectáreas.", " hectáreas"),
        ("abc", "{F} ¿Qué dos evidencias justifican mejor evitar la labranza convencional en el Potrero Norte?", "Pendiente fuerte y suelo desnudo con lluvias intensas", "Terreno plano y rastrojo abundante", "Compactación en caminos y potrero plano", "Esas dos condiciones aumentan el arrastre; las otras evidencias pertenecen al Potrero Sur."),
        ("abc", "En Agropecuaria: ¿por qué la labranza cero puede reducir la erosión?", "Porque deja el rastrojo sobre el suelo y no lo deja expuesto", "Porque remueve más la tierra", "Porque elimina la necesidad de sembrar", "El rastrojo protege al suelo; remover más lo expone."),
    ],
    ctx=("abc", "Un familiar te pide opinión sobre cómo labrar su potrero con pendiente y te dice que «lo decidas tú ahora». ¿Qué respondes?", "Que la decisión la toma un asesor técnico con los datos del potrero, y que tú puedes ayudarle a ordenar esos datos", "Que use siempre la labranza convencional", "Que no importa la pendiente si el suelo está seco", "La elección exige evidencia y apoyo profesional; no hay una labranza correcta para todo terreno."),
    sc=[
        ("En Agropecuaria: ¿cuál labranza remueve más el suelo?", "La convencional", "La convencional remueve mucho y deja más expuesto el suelo."),
        ("En Agropecuaria: ¿qué condición del terreno aumenta el riesgo de erosión?", "Una pendiente fuerte con el suelo desnudo", "El agua corre más rápido por la pendiente y sin cobertura arrastra suelo."),
        ("En el trabajo agrícola: ¿cuántas evidencias debe citar una decisión técnica en esta clase?", "Al menos dos", "Dos evidencias hacen reproducible la decisión."),
    ],
    op=("Caso de ejemplo del «Fundo Demo»: Potrero Este, pendiente suave, 20 % del suelo cubierto con rastrojo, lluvias moderadas, sin compactación; Potrero Oeste, terreno plano, suelo desnudo, camino de máquinas muy compactado. Escribe (a) el porcentaje descubierto del Potrero Este, (b) cuál de los dos potreros tiene más riesgo de erosión por arrastre y una evidencia, (c) qué problema del Potrero Oeste se debe informar al asesor técnico, (d) quién decide y quién ejecuta la labor.",
        "(a) 100 − 20 = 80 % descubierto. (b) El Potrero Este, porque tiene pendiente y 80 % del suelo descubierto; el Oeste es plano. (c) La compactación del camino de máquinas. (d) Decide el asesor técnico; ejecuta personal autorizado.",
        ["calcula el porcentaje descubierto", "compara los potreros con una evidencia", "identifica la compactación", "distingue quién decide y quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["no restar de 100", "elegir sin citar evidencia", "decidir la labor por cuenta propia"],
        "Pregunta: «¿qué potrero tiene pendiente y qué pasa con el agua ahí?». Si no responde, pídele que relea la segunda parte de la explicación."),
    reinforce="Escribe, para tres condiciones de terreno inventadas, el riesgo principal (erosión o compactación) y una evidencia.",
    extend="Explica con un ejemplo por qué el rastrojo es una medida de protección del suelo.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Fundo Demo» compara dos alternativas para preparar 10 hectáreas, con un costo de máquina de ejemplo de $20.000 por hora. "
     "Alternativa 1: 3 labores, cada una de 2 horas por hectárea. Alternativa 2: 1 labor de 2 horas por hectárea. "
     "El asesor anota además que el combustible de ejemplo es de 4 litros por hora de máquina y que el litro cuesta $1.000 (valores de ejemplo).")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular horas, costos y combustible de dos alternativas de preparación de suelo y compararlas.",
    prior=["Sé qué es la labranza y sus tipos.", "Sé multiplicar y dividir números enteros.", "Sé leer una ficha con datos."],
    explain=[
        "Para decidir entre dos alternativas de preparación de suelo no basta con elegir la que parece mejor: se calculan sus horas de trabajo, su costo y su consumo de combustible. Las horas totales se obtienen multiplicando las labores por las horas por hectárea y por las hectáreas. El costo de máquina se obtiene multiplicando las horas totales por el valor de la hora, y el combustible, multiplicando las horas por los litros que se consumen en una hora.",
        "El criterio económico no es el único. Menos labores significa menos pasadas de maquinaria sobre el suelo, lo que reduce el riesgo de compactación y de erosión, y también las horas en que una persona está expuesta a ruido, polvo y vibración. La decisión final considera costo, protección del suelo y seguridad, y se registra con sus cálculos para poder verificarla.",
        f"Todos los números de esta clase son de ejemplo: los valores reales los entrega el asesor técnico y dependen del predio, del equipo y de la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("hora de máquina", "una hora de trabajo del tractor con sus implementos"), ("costo de máquina", "valor de las horas de máquina trabajadas"), ("labor", "una pasada o trabajo de preparación del suelo"), ("consumo de combustible", "litros que gasta la máquina en una hora"), ("alternativa", "una de las opciones posibles para hacer un trabajo"), ("criterio", "regla o dato con que se compara y decide")],
    worked=[
        ("Horas totales", "Una alternativa de ejemplo tiene 2 labores de 3 horas por hectárea, y se preparan 5 hectáreas. ¿Cuántas horas de máquina se necesitan?", ["Horas por hectárea: 2 por 3 es 6.", "Horas totales: 6 por 5 hectáreas."], "30 horas"),
        ("Costo con hora de máquina", "Con 30 horas y una hora de máquina de ejemplo de $15.000, ¿cuánto cuesta el trabajo?", ["Se multiplican las horas por el valor de cada hora.", "30 por 15.000 es 450.000."], "$450.000"),
    ],
    mistakes=[("Calcular solo el costo y olvidar el efecto de las pasadas en el suelo.", "El costo es un criterio, pero no el único.", "Considera también compactación, erosión y exposición del personal."),
              ("Multiplicar las horas por hectárea sin multiplicar por las labores.", "Se omite una parte del trabajo de cada hectárea.", "Primero se calculan las horas por hectárea de todas las labores y luego se multiplican por las hectáreas.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es una hora de máquina?", "Una hora de trabajo del tractor con sus implementos", "La hora del día en que se prepara el suelo", "El tiempo que dura un análisis de suelo", "Hora de máquina mide el trabajo del equipo; no es el horario ni el análisis."),
        ("abc", "En Agropecuaria: ¿qué mide el consumo de combustible de una máquina?", "Los litros que gasta en una hora de trabajo", "Los kilos de suelo que mueve", "Las hectáreas que prepara cada año", "El consumo se mide en litros por hora; no en suelo ni en hectáreas anuales."),
        ("abc", "En Agropecuaria: ¿qué significa que una alternativa de preparación tenga menos labores?", "Que la maquinaria pasa menos veces sobre el suelo", "Que el suelo queda más apretado", "Que se necesitan más hectáreas", "Menos labores son menos pasadas; eso reduce compactación y horas expuestas."),
        ("=", "{F} ¿Cuántas horas de máquina necesita la Alternativa 1 para las 10 hectáreas?", "3*2*10", "Se multiplican las labores, las horas por hectárea y las hectáreas.", " horas"),
        ("=", "{F} ¿Cuántas horas de máquina necesita la Alternativa 2 para las 10 hectáreas?", "1*2*10", "Se multiplica una labor por las horas por hectárea y por las hectáreas.", " horas"),
        ("=", "{F} ¿Cuál es el costo de máquina de la Alternativa 2?", "1*2*10*20000", "Se multiplican las horas totales por el valor de la hora de máquina.", " pesos"),
        ("=", "{F} ¿Cuántos litros de combustible consume la Alternativa 1?", "3*2*10*4", "Se multiplican las horas totales por los litros que se gastan en cada hora.", " litros"),
        ("=", "{F} ¿Cuánto cuesta el combustible de la Alternativa 2?", "1*2*10*4*1000", "Se calculan los litros totales y se multiplican por el precio de cada litro.", " pesos"),
        ("abc", "{F} Una estudiante compara solo el costo y dice que la Alternativa 1 es mejor porque «hace más trabajo». ¿Qué corresponde responder?", "Que además del costo se miran la compactación, la erosión y la exposición del personal", "Que es correcto, porque más labores siempre dan mejor suelo", "Que el costo no importa en la decisión", "Más pasadas pueden compactar el suelo; el costo sí importa, pero no es el único criterio."),
        ("abc", "{F} ¿Cuál alternativa expone menos horas al personal a ruido y polvo?", "La Alternativa 2, porque trabaja menos horas de máquina", "La Alternativa 1, porque trabaja más horas", "Ambas por igual, porque las hectáreas son las mismas", "Menos horas de máquina significan menos horas de exposición."),
        ("=", "{F} ¿Cuántos pesos más cuesta la máquina de la Alternativa 1 que la de la Alternativa 2?", "(3*2*10-1*2*10)*20000", "Se calcula la diferencia de horas y se multiplica por el valor de cada hora.", " pesos"),
        ("abc", "{F} Un operador autorizado propone ahorrar tiempo acelerando el tractor al máximo para terminar antes. ¿Qué corresponde?", "Rechazarlo: la velocidad se fija con el asesor y la norma, no para ahorrar tiempo", "Aceptarlo, porque ahorrar horas reduce el costo", "Aceptarlo si el potrero es plano", "Acelerar sin criterio aumenta el riesgo; los parámetros los fijan el asesor y la norma vigente."),
        ("abc", "En Agropecuaria: ¿por qué conviene registrar los cálculos de una decisión técnica?", "Porque así otra persona puede verificar de dónde salió la decisión", "Porque los números se borran si no se anotan", "Porque el registro reemplaza al asesor técnico", "El registro permite revisar la decisión; no sustituye al asesor."),
    ],
    ctx=("abc", "Un conocido te pide que le digas, sin conocer su predio, cuántas horas de tractor necesita para preparar el suelo. ¿Qué respondes?", "Que necesitas los datos de su predio y que la decisión final la toma un asesor técnico", "Que son siempre 2 horas por hectárea", "Que basta con multiplicar por 3 todas las hectáreas", "Los valores reales dependen del predio, del equipo y del asesor; un número fijo no sirve."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el costo de máquina?", "Horas totales por el valor de la hora", "Se multiplica el tiempo de trabajo por su valor."),
        ("En el trabajo agrícola: ¿qué reduce hacer menos labores sobre el suelo?", "El riesgo de compactación", "Menos pasadas de maquinaria aprietan menos el suelo."),
        ("En Agropecuaria: ¿qué se anota junto a la decisión técnica?", "Los cálculos que la respaldan", "Los cálculos permiten a otra persona verificar la decisión."),
    ],
    op=("Caso de ejemplo del «Fundo Demo»: se comparan, para 6 hectáreas, la Alternativa A (2 labores de 3 horas por hectárea) y la Alternativa B (1 labor de 3 horas por hectárea), con una hora de máquina de ejemplo de $18.000. Escribe (a) las horas totales de cada alternativa, (b) el costo de máquina de cada una, (c) cuál prefieres si solo miras el costo y por qué, (d) otro criterio, además del costo, que debe revisar el asesor técnico.",
        "(a) A: 2 × 3 × 6 = 36 horas; B: 1 × 3 × 6 = 18 horas. (b) A: 36 × 18.000 = $648.000; B: 18 × 18.000 = $324.000. (c) La B, porque cuesta $324.000 menos. (d) La compactación o la erosión del suelo, o la exposición del personal; la decisión la toma el asesor y las labores las hace personal autorizado.",
        ["calcula las horas de cada alternativa", "calcula el costo de cada una", "compara con un criterio", "nombra otro criterio no económico"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por las labores", "olvidar otros criterios", "decidir sin asesor"],
        "Pregunta: «¿cuántas horas por hectárea suman todas las labores?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Calcula las horas de máquina de una alternativa de 2 labores de 2 horas por hectárea para 7 hectáreas, y su costo con una hora de ejemplo de $10.000.",
    extend="Explica con un ejemplo por qué la alternativa más barata no siempre es la mejor para el suelo.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (comparación y control de calidad de ejemplo, inventada). El «Fundo Demo» compara tres alternativas de preparación de suelo con un puntaje de ejemplo de 1 (bajo) a 5 (alto) en cada criterio. "
     "Costo: Alt. X 2, Alt. Y 4, Alt. Z 3. Protección del suelo: Alt. X 1, Alt. Y 4, Alt. Z 3. Seguridad del personal: Alt. X 3, Alt. Y 5, Alt. Z 4. "
     "Después de la labor, la lista de verificación del jefe de campo revisó 10 puntos de ejemplo y 8 resultaron conformes.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas con una matriz de puntajes y a verificar la calidad del trabajo con una lista de verificación, sin ejecutar ninguna labor.",
    prior=["Sé calcular horas y costos de una alternativa.", "Sé sumar números enteros y calcular porcentajes.", "Sé qué es un criterio técnico."],
    explain=[
        "Una matriz de comparación ordena los criterios en filas y las alternativas en columnas, y en cada casilla anota un puntaje. El total de cada alternativa es la suma de sus puntajes. Gana la de mayor total, pero solo si los criterios están bien elegidos y si ningún criterio de seguridad queda en un valor inaceptable. Si dos alternativas empatan, se revisa cuál tiene mejor puntaje en el criterio más importante para el predio.",
        "La verificación de calidad comprueba si el trabajo cumplió lo planeado. Se usa una lista de verificación, que es una lista de puntos que se marcan como conformes o no conformes. El porcentaje de conformidad se calcula dividiendo los puntos conformes por el total y multiplicando por 100. Un punto no conforme se registra tal cual y se informa para corregirlo; no se marca como conforme para que el resultado se vea mejor.",
        f"Estos puntajes son de ejemplo: los reales los define un asesor técnico con el predio. Comparar en papel no habilita para ejecutar ni corregir labores con maquinaria. {EMER} {AVISO}",
    ],
    vocab=[("matriz de comparación", "tabla con criterios y puntajes para comparar alternativas"), ("puntaje", "número que mide qué tan bien cumple una alternativa un criterio"), ("lista de verificación", "lista de puntos que se marcan como conformes o no conformes"), ("conforme", "que cumple lo que se pedía"), ("no conforme", "que no cumple lo que se pedía"), ("porcentaje de conformidad", "puntos conformes divididos por el total, por 100")],
    worked=[
        ("Sumar puntajes", "Una alternativa de ejemplo obtiene 3 en costo, 5 en protección del suelo y 2 en seguridad. ¿Cuál es su total?", ["Se suman los tres puntajes.", "3 más 5 más 2."], "10 puntos"),
        ("Porcentaje de conformidad", "En una lista de ejemplo de 20 puntos, 15 son conformes. ¿Cuál es el porcentaje de conformidad?", ["Se divide 15 entre 20, que da 3 cuartos.", "3 cuartos son 75 de cada 100."], "75 %"),
    ],
    mistakes=[("Elegir la alternativa con mejor costo aunque tenga un puntaje muy bajo en seguridad.", "Un criterio de seguridad no se compensa con el ahorro.", "Revisa que ninguna alternativa tenga un valor inaceptable en seguridad."),
              ("Marcar como conforme un punto dudoso para llegar a 100 %.", "Se oculta un defecto y se pierde la posibilidad de corregirlo.", "Se marca no conforme, se anota y se informa.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es una matriz de comparación?", "Una tabla con criterios y puntajes para comparar alternativas", "Un plano que muestra la ubicación de los potreros", "Un informe de laboratorio con resultados del suelo", "La matriz compara alternativas; el plano y el informe son otros documentos."),
        ("abc", "En Agropecuaria: ¿qué es una lista de verificación?", "Una lista de puntos que se marcan como conformes o no conformes", "Una lista de precios de los insumos del predio", "Una lista de personas autorizadas a conducir", "La lista de verificación comprueba la calidad; no es una lista de precios ni de personas."),
        ("abc", "En Agropecuaria: ¿qué significa que un punto de la lista sea no conforme?", "Que no cumple lo que se pedía", "Que cumple, pero con atraso", "Que no se debe anotar en el registro", "No conforme es que no cumple; debe anotarse e informarse."),
        ("=", "{F} ¿Cuál es el total de puntaje de la Alt. X?", "2+1+3", "Se suman sus puntajes de costo, protección del suelo y seguridad.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje de la Alt. Y?", "4+4+5", "Se suman sus puntajes de costo, protección del suelo y seguridad.", " puntos"),
        ("=", "{F} ¿Cuál es el total de puntaje de la Alt. Z?", "3+3+4", "Se suman sus puntajes de costo, protección del suelo y seguridad.", " puntos"),
        ("abc", "{F} Con los totales de la matriz, ¿qué alternativa obtiene el mayor puntaje?", "Alt. Y", "Alt. Z", "Alt. X", "La Alt. Y suma 13, más que Z con 10 y X con 6."),
        ("abc", "{F} ¿Cuál es el puntaje de la Alt. Y en protección del suelo?", "4", "5", "3", "La ficha anota 4 para la Alt. Y; el 5 es su puntaje en seguridad y el 3 es el de la Alt. Z."),
        ("abc", "{F} Una estudiante dice: «la Alt. X cuesta menos, así que es la mejor aunque proteja mal el suelo». ¿Qué respuesta es correcta?", "Es incompleto: se suman todos los criterios y la X tiene el total más bajo", "Es correcto, porque el costo es lo único que importa", "Es correcto, si el suelo está seco", "La comparación considera todos los criterios; la X suma el menor total."),
        ("=", "{F} ¿Qué porcentaje de conformidad obtuvo la lista de verificación?", "8*100//10", "Se divide lo conforme entre el total de puntos y se multiplica por 100.", " %"),
        ("abc", "{F} El jefe de campo marca como conforme uno de los 2 puntos no conformes para llegar a 90 %. ¿Qué corresponde?", "Rechazarlo: se registra tal cual y se informa lo no conforme para corregirlo", "Aceptarlo, porque el porcentaje es lo importante", "Aceptarlo, si nadie lo revisa", "Marcar como conforme algo que no lo es oculta el defecto."),
        ("abc", "{F} Dos alternativas de ejemplo empatan en el total. ¿Qué dato se revisa para desempatar?", "El puntaje en el criterio más importante para el predio", "El nombre de la alternativa, por orden alfabético", "El criterio que aparece primero en la tabla", "Un empate se resuelve con el criterio de mayor peso para el predio."),
        ("abc", "En Agropecuaria: ¿por qué una alternativa con muy bajo puntaje en seguridad no debe elegirse solo por su bajo costo?", "Porque el ahorro no compensa el daño que podría sufrir una persona", "Porque la seguridad siempre cuesta más dinero", "Porque el costo no se puede medir", "La seguridad de las personas no se negocia por ahorro."),
    ],
    ctx=("abc", "Un amigo te muestra una matriz parecida y te pide que le digas qué alternativa debe ejecutar en su predio esta semana. ¿Qué respondes?", "Que la matriz sirve para analizar, pero que decide un asesor técnico y ejecuta personal autorizado", "Que ejecute la de mayor puntaje, sin más consulta", "Que ejecute la más barata", "Una matriz ordena la decisión, pero no habilita a ejecutar labores ni reemplaza al asesor."),
    sc=[
        ("En Agropecuaria: ¿qué se hace con un punto no conforme de la lista?", "Se anota tal cual y se informa para corregirlo", "Ocultar el defecto impide corregirlo a tiempo y con seguridad."),
        ("En el trabajo agrícola: ¿cómo se calcula el total de una alternativa?", "Sumando sus puntajes", "El total es la suma de los puntajes de cada criterio."),
        ("En Agropecuaria: ¿qué porcentaje de conformidad tiene una lista de 4 puntos con 3 conformes?", "75 %", "Tres de cuatro puntos equivalen a 75 de cada 100."),
    ],
    op=("Caso de ejemplo del «Fundo Demo»: tres alternativas con puntajes de 1 a 5. Costo: P 5, Q 3, R 2. Protección del suelo: P 1, Q 4, R 5. Seguridad: P 2, Q 4, R 5. La lista de verificación posterior revisó 20 puntos y 17 fueron conformes. Escribe (a) el total de cada alternativa, (b) cuál tiene el mayor total, (c) el porcentaje de conformidad, (d) qué haces con los puntos no conformes.",
        "(a) P: 5 + 1 + 2 = 8; Q: 3 + 4 + 4 = 11; R: 2 + 5 + 5 = 12. (b) La R, con 12 puntos. (c) 17 × 100 ÷ 20 = 85 %. (d) Se anotan tal cual, se informan al jefe de campo y al asesor técnico y se corrigen por personal autorizado.",
        ["suma bien los tres totales", "elige la de mayor total", "calcula el porcentaje", "describe qué hacer con lo no conforme"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal los puntajes", "no multiplicar por 100", "marcar lo no conforme como conforme"],
        "Pregunta: «¿qué alternativa suma más puntos?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Crea una matriz con dos alternativas y tres criterios inventados, suma los totales y elige la mejor.",
    extend="Explica con un ejemplo por qué una lista de verificación debe registrar también lo que no cumple.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Parcela Demo» es un predio ficticio de 8 hectáreas que se riega con agua de un canal que se reparte por turnos entre vecinos, y con una bomba eléctrica que sube agua a un estanque. "
     "Peligros anotados: orillas del canal resbaladizas y con corriente, un tablero eléctrico de la bomba que se moja con el agua, un estanque sin baranda y barro en los caminos. "
     "Documento del predio: el derecho de aprovechamiento de aguas (de ejemplo), que dice cuánta agua puede usar el predio.")
build(
    O2, 1, F,
    use="Aprenderé qué es regar y drenar, qué es un derecho de agua, cuáles son los peligros de un sistema de riego y cómo se ordenan las medidas de prevención.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé dividir números enteros."],
    explain=[
        "Regar es entregar agua al cultivo cuando el suelo no alcanza a dársela; drenar es sacar del terreno el agua que sobra, para que las raíces no queden ahogadas. El agua es un recurso limitado y tiene dueños: el derecho de aprovechamiento de aguas es el permiso legal para usar una cantidad de agua de una fuente, como un canal o un pozo. Se usa «según la norma vigente» y no se saca agua sin ese derecho. En los canales el agua se reparte por turnos de riego, que son los horarios que le tocan a cada predio.",
        "El riego tiene peligros propios. Las orillas de canales y estanques pueden provocar caídas al agua, con riesgo de ahogamiento. Un tablero eléctrico mojado puede provocar una descarga eléctrica, y por eso solo lo toca personal eléctrico autorizado, bajo la norma de la entidad que fiscaliza la electricidad. La jerarquía de controles aplica igual: primero eliminar o cambiar el peligro, luego controles de ingeniería, luego reglas y, al final, el equipo de protección personal.",
        f"Una baranda en el estanque es un control de ingeniería; un letrero «no acercarse al canal» es administrativo. Los equipos de riego los opera personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("riego", "entrega de agua al cultivo cuando el suelo no alcanza a dársela"), ("drenaje", "salida del agua sobrante de un terreno"), ("derecho de aprovechamiento de aguas", "permiso legal para usar una cantidad de agua de una fuente"), ("turno de riego", "horario en que a un predio le corresponde recibir el agua del canal"), ("tablero eléctrico", "caja que reúne los controles eléctricos de un equipo"), ("peligro", "fuente con capacidad de causar daño"), ("riesgo", "posibilidad de que un peligro cause daño")],
    worked=[
        ("Distinguir riego y drenaje", "En un predio de ejemplo, un potrero queda con agua estancada durante días. ¿Se necesita más riego o drenaje?", ["Hay agua sobrante que no sale del terreno.", "Sacar el agua sobrante se llama drenar."], "Drenaje"),
        ("Clasificar un control", "En un predio de ejemplo se coloca una tapa metálica fija sobre una acequia que cruza un camino. ¿Qué tipo de control es?", ["La tapa cambia físicamente el lugar.", "Cambiar el lugar es un control de ingeniería."], "Control de ingeniería"),
    ],
    mistakes=[("Creer que un predio puede sacar agua de cualquier canal si la necesita.", "El uso del agua exige un derecho y el cumplimiento de los turnos.", "Se usa solo el agua que el derecho y el turno permiten."),
              ("Creer que se puede revisar un tablero eléctrico mojado «con cuidado».", "La electricidad exige personal autorizado y norma vigente.", "No se toca: se avisa a un adulto responsable.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el drenaje de un terreno?", "La salida del agua sobrante para que las raíces no queden ahogadas", "La entrega de agua al cultivo cuando falta humedad", "El permiso legal para usar agua de un canal", "Drenar saca el agua que sobra; entregar agua es regar y el permiso es el derecho de aguas."),
        ("abc", "En Agropecuaria: ¿qué es un derecho de aprovechamiento de aguas?", "El permiso legal para usar una cantidad de agua de una fuente", "El horario en que un predio puede regar", "La zanja por donde sale el agua sobrante", "El derecho es el permiso; el horario es el turno de riego y la zanja es de drenaje."),
        ("abc", "En Agropecuaria: ¿qué es un turno de riego?", "El horario en que a un predio le corresponde recibir agua del canal", "La cantidad de agua que cae en una lluvia", "El permiso legal para perforar un pozo", "El turno ordena el reparto del agua; la lluvia y los permisos son otras cosas."),
        ("=", "{F} Un canal entrega agua a esta parcela y a otras 5, cada una por turnos iguales de 4 horas seguidas. ¿Cuántas horas dura el ciclo completo de turnos?", "(1+5)*4", "Se suman las 6 parcelas y se multiplican por las horas de cada turno.", " horas"),
        ("abc", "{F} Una baranda alrededor del estanque es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien se acerca", "La baranda es una estructura física; no depende de que cada persona se acuerde."),
        ("abc", "{F} Un letrero «no acercarse al borde del canal» es un control de tipo:", "Administrativo, porque informa y ordena una conducta", "De ingeniería, porque cambia el canal", "De eliminación, porque quita el agua", "Un letrero solo informa; no cambia el canal ni quita el agua."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las orillas resbaladizas del canal?", "Que una persona resbale, caiga al agua y se ahogue", "Las orillas resbaladizas en sí mismas", "Que el canal tenga poca agua", "El riesgo es la posibilidad del daño; las orillas resbaladizas son el peligro."),
        ("abc", "{F} Una estudiante nota que el tablero de la bomba está mojado y dice: «lo seco con un trapo y lo reviso yo». ¿Qué respuesta es correcta?", "Es peligroso: no se toca y se avisa a un adulto responsable", "Es correcto, si usa guantes", "Es correcto, si apaga la luz de la sala", "La electricidad la trata solo personal autorizado; los guantes o apagar la luz no bastan."),
        ("abc", "{F} Durante una visita una persona resbala y cae al canal. ¿Qué corresponde según las reglas generales?", "No meterte al agua ni acercarte al borde, avisar a un adulto responsable y a emergencias", "Meterte al canal para sacarla de inmediato", "Esperar a que salga sola", "Entrar al agua puede producir otro accidente; se avisa a quienes pueden actuar."),
        ("abc", "En Agropecuaria: ¿por qué un predio no puede tomar más agua que la que indica su derecho?", "Porque el agua es un recurso limitado y otros predios también tienen derecho", "Porque el agua del canal siempre es salada", "Porque el derecho solo vale en invierno", "El derecho fija la cantidad para repartir de modo justo un recurso limitado."),
        ("abc", "{F} Se propone solo entregar botas de goma como medida contra las caídas en el barro. ¿Qué medida es más efectiva?", "Mejorar el camino con una superficie firme y con drenaje", "Pedir a cada persona que camine más despacio", "Entregar un segundo par de botas", "Cambiar el camino actúa sobre el peligro; la regla y el EPP quedan más abajo en la jerarquía."),
        ("=", "{F} El estanque tiene capacidad de ejemplo de 300 m³ y se gastan 50 m³ por día. ¿Cuántos días de riego alcanza si parte lleno?", "300//50", "Se divide el volumen del estanque entre el gasto de cada día.", " días"),
        ("abc", "En Agropecuaria: ¿por qué el EPP es la última barrera de la jerarquía de controles?", "Porque no quita el peligro y protege solo a quien lo usa", "Porque elimina el peligro, pero es muy caro", "Porque se usa solo en el invierno", "El EPP deja el peligro en su lugar; por eso se prefieren controles más arriba."),
    ],
    ctx=("abc", "Un vecino te dice que su canal está seco y te pide que desvíes un poco de agua de la acequia del vecino «sin avisarle». ¿Qué respondes?", "Que no, porque el agua tiene derechos y turnos, y que lo consultarás con un adulto responsable", "Que sí, si es solo un poco", "Que sí, si lo haces de noche", "Desviar agua sin derecho ni aviso infringe el reparto, aunque sea poco o de noche."),
    sc=[
        ("En Agropecuaria: ¿qué es regar?", "Entregar agua al cultivo cuando el suelo no alcanza a dársela", "Regar compensa la falta de humedad del suelo."),
        ("En el trabajo agrícola: ¿quién toca un tablero eléctrico mojado?", "Nadie de la clase: solo personal eléctrico autorizado", "La electricidad exige personal autorizado y norma vigente."),
        ("En Agropecuaria: ¿qué es un turno de riego?", "El horario en que al predio le toca el agua del canal", "El turno ordena el reparto del agua entre los predios."),
    ],
    op=("Caso de ejemplo del predio ficticio «Parcela Demo 2»: una acequia con orillas de barro junto a un camino por donde pasan trabajadores al amanecer, y una bomba con el cable eléctrico a ras de suelo. Escribe (a) un peligro y su riesgo en la acequia, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves el cable en el agua.",
        "(a) Peligro: orillas de barro de la acequia; riesgo: que alguien resbale, caiga y se lastime o se ahogue. (b) Un letrero y una regla de no pasar por el borde de noche. (c) Una baranda o una pasarela firme sobre la acequia, hecha por personal autorizado. (d) No me acerco, aviso a un adulto responsable y a emergencias; solo personal eléctrico autorizado interviene.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca al cable y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer tocar el cable", "no avisar a un adulto responsable"],
        "Pregunta: «¿qué control cambia físicamente el lugar?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe un peligro y un riesgo de cada uno de estos lugares inventados: un canal, un estanque y un tablero de bomba.",
    extend="Explica con un ejemplo por qué un derecho de aguas protege tanto al predio como a sus vecinos.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados). Suelo de la «Parcela Demo»: humedad a capacidad de campo 30 %, humedad en el punto de marchitez 15 %, profundidad de raíces del cultivo 400 mm. "
     "Sistemas de riego (conceptos): gravitacional por surcos (el agua corre por gravedad entre las hileras) y tecnificado por goteo (una bomba envía agua por mangueras con emisores). "
     "Documentos del predio: el programa de riego (cuándo y cuánto), el registro de riego (cuándo y cuánto se regó) y el plano del sistema (dónde están canales, mangueras y válvulas).")
build(
    O2, 2, F,
    use="Aprenderé los conceptos de capacidad de campo, punto de marchitez y agua útil, los sistemas de riego gravitacional y tecnificado, los documentos del riego y los roles de quienes lo gestionan.",
    prior=["Sé qué es regar y drenar.", "Sé leer una ficha con datos.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La capacidad de campo es la cantidad máxima de agua que el suelo retiene después de que el exceso ha drenado. El punto de marchitez es la humedad bajo la cual la planta ya no puede sacar agua del suelo y se marchita. El agua útil es la diferencia entre ambas: es el agua que la planta sí puede aprovechar. Si el suelo está a capacidad de campo no necesita riego; si se acerca al punto de marchitez, sí.",
        "El riego gravitacional lleva el agua por canales y surcos usando la pendiente del terreno; es barato de instalar, pero pierde más agua. El riego tecnificado usa bomba, mangueras y emisores, como el goteo, y entrega el agua cerca de la planta con más control. Cada sistema se documenta: el programa de riego dice cuándo y cuánto regar, el registro de riego anota lo que se hizo y el plano muestra el sistema. El técnico en riego diseña y supervisa, el jefe de riego programa y el regador ejecuta, siempre con autorización.",
        f"Un regador no cambia el programa por su cuenta: si el suelo parece seco o encharcado, lo informa. {EMER} {AVISO}",
    ],
    vocab=[("capacidad de campo", "máxima agua que retiene el suelo después de drenar el exceso"), ("punto de marchitez", "humedad bajo la cual la planta ya no puede sacar agua"), ("agua útil", "diferencia entre capacidad de campo y punto de marchitez"), ("riego gravitacional", "riego en que el agua corre por gravedad, como por surcos"), ("riego tecnificado", "riego con bomba, mangueras y emisores, como el goteo"), ("emisor", "pieza que deja salir el agua cerca de la planta"), ("programa de riego", "documento que dice cuándo y cuánto regar")],
    worked=[
        ("Calcular agua útil", "Un suelo de ejemplo tiene 28 % a capacidad de campo y 12 % en el punto de marchitez. ¿Cuánto es el agua útil?", ["Agua útil es la diferencia entre ambos valores.", "28 menos 12."], "16 %"),
        ("Elegir el documento", "Un jefe de riego de ejemplo quiere saber qué día se regó el potrero 4 y cuánta agua recibió. ¿Qué documento consulta?", ["Lo que ya se hizo se anota en un registro.", "Es el registro de riego."], "El registro de riego"),
    ],
    mistakes=[("Creer que el agua útil es todo el agua que tiene el suelo.", "Parte del agua queda retenida con tanta fuerza que la planta no la puede sacar.", "El agua útil es solo la diferencia entre capacidad de campo y punto de marchitez."),
              ("Confundir el programa de riego con el registro de riego.", "El programa es lo planeado y el registro es lo realizado.", "Consulta cada documento para lo que fue hecho.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la capacidad de campo de un suelo?", "La máxima agua que retiene después de drenar el exceso", "La humedad bajo la cual la planta se marchita", "La cantidad de agua que cae en una lluvia", "La capacidad de campo es el máximo retenido; el punto de marchitez es el mínimo aprovechable."),
        ("abc", "En Agropecuaria: ¿qué es el punto de marchitez?", "La humedad bajo la cual la planta ya no puede sacar agua del suelo", "La máxima agua que el suelo retiene tras drenar", "El momento del día en que se riega", "El punto de marchitez es el mínimo; el máximo retenido es la capacidad de campo."),
        ("abc", "En Agropecuaria: ¿qué es el riego gravitacional?", "Un riego en que el agua corre por gravedad, como por surcos", "Un riego en que una bomba envía agua por mangueras con emisores", "Un riego que usa solo la lluvia", "En el gravitacional el agua corre por el terreno; la bomba y los emisores son del riego tecnificado."),
        ("=", "{F} ¿Cuánto es el agua útil del suelo de la ficha, en puntos porcentuales?", "30-15", "El agua útil es la diferencia entre capacidad de campo y punto de marchitez.", " %"),
        ("abc", "{F} ¿Qué documento muestra dónde están los canales, mangueras y válvulas?", "El plano del sistema", "El registro de riego", "El programa de riego", "El plano muestra la ubicación del sistema; el programa y el registro hablan de tiempos y cantidades."),
        ("abc", "{F} ¿Qué sistema de la ficha usa una bomba, mangueras y emisores?", "El tecnificado por goteo", "El gravitacional por surcos", "Ninguno de los dos", "El goteo es tecnificado; el gravitacional usa la pendiente."),
        ("abc", "{F} ¿Qué rol programa cuándo y cuánto regar, sin ejecutar el riego?", "El jefe de riego", "El regador", "El vendedor que entrega las mangueras", "El jefe de riego programa; el regador ejecuta lo programado."),
        ("=", "{F} Si el agua útil se expresa en milímetros sobre la profundidad de raíces, ¿cuántos milímetros hay en total?", "(30-15)*400//100", "Se calcula el porcentaje de agua útil sobre la profundidad de raíces.", " mm"),
        ("abc", "{F} Una estudiante dice: «el suelo tiene 15 % de humedad, por lo tanto está a capacidad de campo». ¿Qué respuesta es correcta?", "Es falso: 15 % es el punto de marchitez, no la capacidad de campo", "Es cierto, porque 15 % es la humedad ideal", "Es cierto, si el suelo está oscuro", "La ficha asigna 15 % al punto de marchitez; la capacidad de campo es 30 %."),
        ("abc", "{F} El regador observa que el suelo de un surco parece muy seco, pero el programa dice «no regar hoy». ¿Qué corresponde?", "Informar al jefe de riego, sin cambiar el programa por su cuenta", "Regar igual, porque él lo ve seco", "Borrar el programa y escribir otro", "Los cambios los decide el jefe de riego con los datos; el regador informa."),
        ("abc", "{F} Dos parcelas distintas del mismo predio usan el mismo registro de riego sin fecha ni nombre. ¿Por qué es un registro débil?", "Porque sin fecha ni responsable no se puede verificar", "Porque el registro nunca debe anotar la fecha", "Porque solo vale si está en un computador", "Un registro debe tener fecha y quien lo anotó para ser verificable."),
        ("=", "{F} Un surco de 80 metros de largo se riega con 5 litros por metro. ¿Cuántos litros se usan en ese surco?", "80*5", "Se multiplican los metros del surco por los litros de cada metro.", " litros"),
        ("abc", "En Agropecuaria: ¿por qué el riego por goteo da más control que el riego por surcos?", "Porque entrega el agua cerca de la planta, con bomba y emisores", "Porque no necesita agua", "Porque el agua corre sola por todo el potrero", "El goteo lleva el agua con más precisión; los surcos dependen de la pendiente."),
    ],
    ctx=("abc", "Un conocido te pide que le «ajustes» el programa de riego de su predio sin conocer su suelo, para que gaste menos agua. ¿Qué respondes?", "Que el programa lo define un técnico en riego con datos del suelo y del cultivo", "Que riegue siempre la mitad", "Que riegue solo cuando se acuerde", "El programa depende del suelo y del cultivo; un ajuste a ciegas puede ahogar o marchitar las plantas."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el agua útil?", "Capacidad de campo menos punto de marchitez", "El agua útil es el rango entre el máximo retenido y el mínimo aprovechable."),
        ("En el trabajo agrícola: ¿qué documento anota lo que ya se regó?", "El registro de riego", "El registro guarda lo que ya se realizó en el predio."),
        ("En Agropecuaria: ¿qué sistema de riego usa bomba y emisores?", "El riego tecnificado", "El tecnificado usa equipos que llevan el agua cerca de la planta."),
    ],
    op=("Datos de ejemplo del suelo de la «Parcela Demo 3»: capacidad de campo 25 %, punto de marchitez 10 %, profundidad de raíces 300 mm. El jefe de riego te muestra el plano del sistema, el programa de riego y el registro de riego. Escribe (a) el agua útil en porcentaje, (b) los milímetros de agua útil en la profundidad de raíces, (c) qué documento mostraría lo ya regado, (d) qué rol decide el cambio del programa.",
        "(a) 25 − 10 = 15 %. (b) 15 × 300 ÷ 100 = 45 mm. (c) El registro de riego. (d) El jefe de riego, con ayuda del técnico en riego; el regador solo informa.",
        ["calcula el porcentaje de agua útil", "calcula los milímetros", "nombra el documento correcto", "nombra el rol correcto"],
        ["hoja con las cuatro respuestas"],
        ["restar mal los porcentajes", "confundir programa con registro", "decir que el regador cambia el programa"],
        "Pregunta: «¿qué se resta de qué para obtener el agua útil?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Elige tres valores inventados de capacidad de campo y de punto de marchitez y calcula el agua útil de cada uno.",
    extend="Explica con un ejemplo por qué el agua que sigue en el suelo bajo el punto de marchitez no sirve a la planta.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). La «Parcela Demo» tiene dos lotes. Lote A: suelo con mucha arcilla, el agua queda estancada hasta dos días después del riego, la napa freática (nivel del agua subterránea) está a 50 cm de profundidad y las hojas amarillean. "
     "Lote B: suelo con mucha arena, el agua se infiltra de inmediato y las plantas se marchitan entre riegos. "
     "Medidas posibles (conceptos): drenar el exceso, regar con más frecuencia y menos cantidad, o reducir el riego.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de riego y drenaje con evidencias, relacionando el tipo de suelo, la napa y los síntomas del cultivo con una medida técnica posible.",
    prior=["Sé qué es el agua útil y el punto de marchitez.", "Sé qué es la textura del suelo.", "Sé leer una ficha con datos."],
    explain=[
        "El agua se mueve distinto según el suelo. En un suelo arcilloso el agua pasa lentamente, queda estancada y puede asfixiar las raíces, que necesitan aire; a eso se le llama anegamiento. En un suelo arenoso el agua pasa muy rápido y se pierde bajo las raíces. La napa freática es el nivel del agua subterránea: si está muy cerca de la superficie, el suelo se satura y necesita drenaje.",
        "Para analizar un caso se leen los síntomas y se relacionan con una causa. Hojas amarillas y agua estancada apuntan a exceso de agua, es decir, a mal drenaje. Plantas marchitas entre riegos en un suelo arenoso apuntan a poca retención, y se corrige regando con más frecuencia y menos cantidad, para que el agua no se pierda. La decisión la toma el técnico en riego con medidas del terreno, no quien lee un cuaderno.",
        f"Abrir zanjas de drenaje puede ser peligroso: las paredes se derrumban y las personas no deben meterse en una zanja profunda. Esas obras las hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("anegamiento", "exceso de agua en el suelo que deja a las raíces sin aire"), ("napa freática", "nivel del agua subterránea"), ("infiltración", "paso del agua desde la superficie hacia dentro del suelo"), ("saturado", "con todos los espacios del suelo llenos de agua"), ("síntoma", "señal visible del cultivo que muestra un problema"), ("zanja de drenaje", "canal abierto que saca el agua sobrante del terreno")],
    worked=[
        ("Relacionar síntoma y causa", "En un lote de ejemplo las hojas amarillean y el suelo tiene agua estancada. ¿Qué problema es más probable?", ["El agua estancada deja a las raíces sin aire.", "Eso es exceso de agua, o mal drenaje."], "Exceso de agua por mal drenaje"),
        ("Cálculo de distancia", "La napa de un lote de ejemplo está a 120 cm y las raíces llegan a 40 cm. ¿Cuántos centímetros hay entre las raíces y la napa?", ["Se restan las dos profundidades.", "120 menos 40."], "80 cm"),
    ],
    mistakes=[("Creer que si las hojas amarillean siempre falta agua.", "El exceso de agua también las amarillea al dejar sin aire a las raíces.", "Se mira el suelo y el drenaje antes de decidir."),
              ("Creer que se puede entrar a una zanja profunda «solo un momento» para revisarla.", "Las paredes pueden derrumbarse sin aviso.", "No se entra: la obra la hace personal autorizado.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el anegamiento de un suelo?", "El exceso de agua que deja a las raíces sin aire", "La falta de agua que marchita la planta", "El paso lento del agua hacia el canal", "El anegamiento es exceso de agua; la falta es déficit de riego."),
        ("abc", "En Agropecuaria: ¿qué es la napa freática?", "El nivel del agua subterránea", "La capa de rastrojo sobre el suelo", "El agua que corre por un canal", "La napa es agua bajo la superficie; el canal y el rastrojo son otras cosas."),
        ("abc", "En Agropecuaria: ¿qué es la infiltración del agua?", "El paso del agua desde la superficie hacia dentro del suelo", "La evaporación del agua al aire", "El arrastre de agua por el canal", "La infiltración es entrada de agua al suelo."),
        ("abc", "{F} ¿Qué evidencia del Lote A indica un problema de drenaje?", "El agua queda estancada hasta dos días y la napa está a 50 cm", "El agua se infiltra de inmediato", "Las plantas se marchitan entre riegos", "Agua estancada y napa cerca señalan mal drenaje; las otras evidencias son del Lote B."),
        ("abc", "{F} ¿Qué evidencia del Lote B muestra poca retención de agua?", "Las plantas se marchitan entre riegos y el agua se infiltra de inmediato", "Las hojas amarillean y hay agua estancada", "La napa está a 50 cm", "El agua pasa rápido y las plantas se secan; lo demás es del Lote A."),
        ("abc", "{F} ¿Qué medida técnica corresponde analizar para el Lote A?", "Mejorar el drenaje o reducir el riego, según indique el técnico", "Regar con más agua para que las hojas se recuperen", "Dejar de revisar el lote", "Hay exceso de agua; más agua empeoraría el problema."),
        ("abc", "{F} ¿Qué medida corresponde analizar para el Lote B?", "Regar con más frecuencia y menos cantidad cada vez, según el técnico", "Instalar una zanja para sacar más agua", "Regar una sola vez y en gran cantidad", "En suelo arenoso el agua pasa rápido; riegos frecuentes y cortos evitan la pérdida."),
        ("=", "{F} ¿Cuántos centímetros separan a las raíces de la napa del Lote A si las raíces llegan a 20 cm de profundidad?", "50-20", "Se restan la profundidad de las raíces a la de la napa.", " cm"),
        ("abc", "{F} Un compañero dice: «voy a entrar a la zanja de drenaje profunda para ver si sirve». ¿Qué respuesta es correcta?", "No se entra: las paredes pueden derrumbarse y la obra la revisa personal autorizado", "Se entra, si es solo un momento", "Se entra, si se lleva casco", "El derrumbe puede ocurrir sin aviso; el casco no evita quedar atrapado."),
        ("abc", "{F} Una persona queda atrapada en una zanja derrumbada del predio. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Entrar a sacarla con las manos", "Tirar de su ropa desde el borde", "Acercarse puede provocar otro derrumbe; se avisa a quienes pueden rescatar."),
        ("=", "{F} El Lote B mide 6 hectáreas y el Lote A mide el doble. ¿Cuántas hectáreas suman ambos lotes?", "6+6*2", "Se calcula el doble de 6 y se suma con el Lote B.", " hectáreas"),
        ("abc", "{F} Un estudiante propone regar el Lote A con el mismo calendario que el Lote B «porque son del mismo predio». ¿Qué problema tiene?", "Los dos suelos retienen el agua distinto y requieren manejos distintos", "Ninguno, porque el predio es el mismo", "Que el calendario no se puede escribir", "Un mismo predio puede tener suelos distintos; cada lote necesita su análisis."),
        ("abc", "En Agropecuaria: ¿por qué una napa muy cercana a las raíces puede dañar el cultivo?", "Porque satura el suelo y deja a las raíces sin aire", "Porque deja al suelo demasiado seco", "Porque evita que el agua llegue a la superficie", "La napa cercana llena el suelo de agua y asfixia las raíces."),
    ],
    ctx=("abc", "Un amigo te cuenta que sus plantas tienen hojas amarillas y quiere regar más. ¿Qué le aconsejas?", "Revisar primero el suelo y el drenaje con un técnico, porque el exceso de agua también amarillea", "Regar el doble porque seguro falta agua", "Cortar las hojas amarillas", "Una causa distinta (exceso) puede dar el mismo síntoma; hay que diagnosticar antes de actuar."),
    sc=[
        ("En Agropecuaria: ¿qué suelo drena más lento, el arcilloso o el arenoso?", "El arcilloso", "La arcilla tiene partículas finas que dejan pasar el agua despacio."),
        ("En el trabajo agrícola: ¿qué se hace antes de decidir una medida de riego o drenaje?", "Se leen los síntomas y se relacionan con la causa", "El diagnóstico se apoya en los síntomas y las mediciones."),
        ("En Agropecuaria: ¿quién entra a una zanja de drenaje profunda?", "Nadie de la clase: lo hace personal autorizado", "Las paredes de las zanjas profundas pueden derrumbarse sin aviso."),
    ],
    op=("Caso de ejemplo de la «Parcela Demo 4»: Lote C con suelo arcilloso, charcos que duran tres días y napa a 40 cm; Lote D con suelo arenoso, hojas pálidas y marchitas a media tarde. Escribe (a) cuál lote tiene problema de drenaje y una evidencia, (b) cuál tiene poca retención y una evidencia, (c) una medida conceptual para cada lote, (d) por qué no debes entrar a una zanja profunda.",
        "(a) El Lote C: charcos de tres días y napa a 40 cm. (b) El Lote D: suelo arenoso y plantas marchitas a media tarde. (c) C: mejorar el drenaje o reducir el riego, según el técnico; D: regar con más frecuencia y menos cantidad, según el técnico. (d) Porque las paredes pueden derrumbarse; la obra la hace personal autorizado.",
        ["identifica el lote con mal drenaje y cita evidencia", "identifica el lote con poca retención y cita evidencia", "propone medidas conceptuales", "explica el riesgo de la zanja"],
        ["hoja con las cuatro respuestas"],
        ["decir que el exceso de agua se corrige regando más", "no citar evidencia", "proponer entrar a la zanja"],
        "Pregunta: «¿en qué lote el agua se queda y en cuál se pierde?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe dos síntomas inventados de exceso de agua y dos de falta de agua en un cultivo, y la causa más probable de cada uno.",
    extend="Explica con un ejemplo por qué la textura del suelo cambia la frecuencia de riego.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La «Parcela Demo» tiene 4 hectáreas. El requerimiento de agua del cultivo es de 5 mm por día (valor de ejemplo). Regla del curso: 1 mm de agua sobre 1 hectárea equivale a 10 m³. "
     "Eficiencia de ejemplo del sistema: gravitacional 50 % y goteo 80 %. La bomba de ejemplo entrega 50 m³ por hora. "
     "Volumen bruto = volumen neto × 100 ÷ eficiencia.")
build(
    O2, 4, F,
    use="Aprenderé a calcular con enteros el volumen de agua que necesita un riego, a corregirlo por la eficiencia del sistema y a calcular las horas de bomba, con datos de ejemplo.",
    prior=["Sé qué es el requerimiento de agua del cultivo.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El requerimiento de agua de un cultivo se expresa en milímetros por día. Un milímetro de agua sobre una hectárea equivale a 10 metros cúbicos (m³). Por eso el volumen neto, que es el agua que el cultivo necesita, se calcula multiplicando los milímetros por las hectáreas y por 10. Este volumen es lo que llega a la planta, pero en el camino parte del agua se pierde por filtración y evaporación.",
        "La eficiencia es el porcentaje del agua aplicada que realmente llega a la planta. Para entregar el volumen neto hay que aplicar un volumen bruto mayor: se multiplica el neto por 100 y se divide por la eficiencia. Un sistema más eficiente, como el goteo, necesita menos agua para el mismo cultivo. Las horas de bomba se calculan dividiendo el volumen bruto por lo que entrega la bomba cada hora.",
        f"Todos los valores son de ejemplo: los reales los da el técnico en riego según el cultivo, el suelo y la norma de aguas vigente. {EMER} {AVISO}",
    ],
    vocab=[("requerimiento de agua", "agua que necesita el cultivo, en milímetros por día"), ("milímetro de agua", "lámina de agua de un milímetro sobre el terreno"), ("volumen neto", "agua que el cultivo necesita recibir"), ("eficiencia", "porcentaje del agua aplicada que llega a la planta"), ("volumen bruto", "agua que hay que aplicar para entregar el volumen neto"), ("caudal de la bomba", "volumen de agua que entrega la bomba cada hora")],
    worked=[
        ("Volumen neto", "Un cultivo de ejemplo requiere 3 mm por día en 5 hectáreas. ¿Cuántos m³ netos se necesitan al día?", ["1 mm sobre 1 hectárea son 10 m³.", "3 mm por 5 hectáreas por 10 m³."], "150 m³"),
        ("Volumen bruto", "Con un volumen neto de 150 m³ y una eficiencia de ejemplo de 75 %, ¿cuántos m³ brutos hay que aplicar?", ["Se multiplica el neto por 100: 15.000.", "Se divide entre la eficiencia: 15.000 entre 75."], "200 m³"),
    ],
    mistakes=[("Usar el volumen neto como si fuera el que hay que bombear.", "Se olvida que parte del agua se pierde por la eficiencia.", "Se calcula el bruto: neto por 100 dividido por la eficiencia."),
              ("Dividir por la eficiencia sin multiplicar antes por 100.", "La eficiencia es un porcentaje, no un número directo.", "Primero se multiplica por 100 y luego se divide por el porcentaje.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es el volumen neto de agua?", "El agua que el cultivo necesita recibir", "El agua que se pierde por evaporación", "El agua total que entrega la bomba al año", "El neto es lo que llega al cultivo; la pérdida es la diferencia con el bruto."),
        ("abc", "En Agropecuaria: ¿qué es la eficiencia de un sistema de riego?", "El porcentaje del agua aplicada que llega a la planta", "La cantidad de bombas que tiene el sistema", "El número de hectáreas que riega", "La eficiencia mide cuánta agua aplicada llega a la planta."),
        ("abc", "En Agropecuaria: ¿a cuántos m³ equivale 1 mm de agua sobre 1 hectárea, según la regla de la ficha?", "10 m³", "100 m³", "1 m³", "La regla del curso dice 10 m³; los otros valores no corresponden."),
        ("=", "{F} ¿Cuántos m³ netos necesita la parcela cada día?", "5*4*10", "Se multiplican milímetros, hectáreas y 10 m³ por cada milímetro por hectárea.", " m³"),
        ("=", "{F} ¿Cuántos m³ brutos hay que aplicar al día con riego gravitacional?", "5*4*10*100//50", "Se calcula el neto y se corrige por la eficiencia del sistema.", " m³"),
        ("=", "{F} ¿Cuántos m³ brutos hay que aplicar al día con riego por goteo?", "5*4*10*100//80", "Se calcula el neto y se corrige por la eficiencia del goteo.", " m³"),
        ("=", "{F} ¿Cuántas horas de bomba se necesitan al día con goteo?", "5*4*10*100//80//50", "Se divide el volumen bruto del goteo entre lo que entrega la bomba cada hora.", " horas"),
        ("=", "{F} ¿Cuántas horas de bomba se necesitan al día con riego gravitacional?", "5*4*10*100//50//50", "Se divide el volumen bruto gravitacional entre lo que entrega la bomba cada hora.", " horas"),
        ("=", "{F} ¿Cuántos m³ al día se ahorran con goteo en vez de riego gravitacional?", "5*4*10*100//50-5*4*10*100//80", "Se resta el volumen bruto del goteo al del gravitacional.", " m³"),
        ("abc", "{F} Un compañero dice que con goteo hay que aplicar el mismo volumen bruto que con surcos «porque el cultivo es el mismo». ¿Qué respuesta es correcta?", "Es falso: el goteo es más eficiente y requiere menos volumen bruto", "Es cierto, porque el neto es igual y por eso el bruto también", "Es cierto, si la bomba es la misma", "La eficiencia cambia el bruto aunque el neto sea igual."),
        ("abc", "{F} El operador autorizado quiere dejar la bomba funcionando toda la noche sin revisar el estanque «para asegurar». ¿Qué corresponde?", "Rechazarlo: el volumen se calcula y se registra; funcionar sin control es un riesgo", "Aceptarlo, porque más agua nunca daña", "Aceptarlo, si el estanque es grande", "Más agua puede anegar el cultivo; la operación de la bomba sigue el programa y la norma."),
        ("=", "{F} Si el requerimiento subiera a 6 mm por día en la misma superficie, ¿cuántos m³ netos se necesitarían?", "6*4*10", "Se cambia el requerimiento a 6 mm y se multiplica por las hectáreas y por 10.", " m³"),
        ("abc", "En Agropecuaria: ¿por qué se calcula el volumen bruto y no solo el neto?", "Porque parte del agua se pierde antes de llegar a la planta", "Porque el neto no se puede calcular", "Porque el bruto es siempre menor que el neto", "La eficiencia menor que 100 % obliga a aplicar más que el neto."),
    ],
    ctx=("abc", "Un familiar te muestra su cuenta de energía de la bomba y te pide que cambies de goteo a surcos «para ahorrar». ¿Qué comparas primero?", "El volumen bruto y las horas de bomba de cada sistema, con datos del predio y consejo de un técnico", "Solo el precio de las mangueras", "El nombre del sistema", "El ahorro depende del volumen, de las horas de bomba y de las condiciones reales del predio."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el volumen neto diario?", "Milímetros por hectáreas por 10 m³", "El neto resulta de los milímetros por las hectáreas y por 10."),
        ("En el trabajo agrícola: ¿qué pasa con el volumen bruto si baja la eficiencia?", "Sube, porque hay que aplicar más agua", "Con menor eficiencia se pierde más agua por el camino."),
        ("En Agropecuaria: ¿cómo se calculan las horas de bomba?", "Volumen bruto dividido por lo que entrega la bomba por hora", "Las horas resultan de dividir el volumen entre el caudal horario."),
    ],
    op=("Datos de ejemplo del predio ficticio «Parcela Demo 5»: 3 hectáreas, requerimiento de 4 mm por día, eficiencia del riego de 60 %, bomba de 40 m³ por hora; regla: 1 mm sobre 1 hectárea son 10 m³. Escribe (a) el volumen neto diario, (b) el volumen bruto diario, (c) las horas de bomba al día, (d) a quién entregas los resultados para decidir.",
        "(a) 4 × 3 × 10 = 120 m³. (b) 120 × 100 ÷ 60 = 200 m³. (c) 200 ÷ 40 = 5 horas. (d) Al técnico en riego, que decide el programa de riego.",
        ["calcula el volumen neto", "calcula el volumen bruto", "calcula las horas", "nombra al técnico en riego"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la eficiencia", "no multiplicar por 10 m³", "decidir sin el técnico en riego"],
        "Pregunta: «¿cuántos m³ son 1 mm sobre 3 hectáreas?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el volumen neto diario de 2 hectáreas con un requerimiento de ejemplo de 6 mm por día, y su volumen bruto con una eficiencia de 75 %.",
    extend="Explica con un ejemplo por qué un sistema con más eficiencia puede reducir el costo de bombeo.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 5 (comparación y control de ejemplo, inventada). El «Fundo Demo» compara tres sistemas para 10 hectáreas. Surcos: eficiencia 50 %, mano de obra alta, inversión baja. Aspersión: eficiencia 70 %, mano de obra media, inversión media. Goteo: eficiencia 80 %, mano de obra baja, inversión alta. "
     "Control del goteo: se midió el caudal de 4 emisores de ejemplo: 8, 9, 8 y 3 litros por hora. Rango aceptable de ejemplo: de 7 a 9 litros por hora.")
build(
    O2, 5, F,
    use="Aprenderé a comparar sistemas de riego con varios criterios y a verificar con un control de caudales si un sistema funciona dentro de un rango, sin operar ningún equipo.",
    prior=["Sé calcular el volumen bruto con la eficiencia.", "Sé leer una tabla de datos.", "Sé calcular promedios de enteros."],
    explain=[
        "Comparar sistemas de riego exige mirar varios criterios a la vez: la eficiencia (cuánta agua llega a la planta), la mano de obra (cuánto trabajo humano pide), la inversión (cuánto cuesta instalarlo) y el riesgo para las personas. Ningún sistema es el mejor en todo: el goteo es eficiente pero caro de instalar; los surcos son baratos pero pierden más agua. La decisión depende del cultivo, del agua disponible y del presupuesto del predio.",
        "Para verificar la calidad de un sistema tecnificado se mide el caudal de varios emisores y se compara con el rango aceptable. Un emisor fuera de rango suele indicar obstrucción o falla, y se registra tal cual y se informa al técnico. El promedio es la suma de los valores dividida por la cantidad de emisores; sirve para ver el funcionamiento general, pero no oculta un emisor defectuoso.",
        f"Las mediciones en terreno y las reparaciones las hace personal autorizado; aquí solo se interpretan datos de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("mano de obra", "trabajo humano que necesita un sistema"), ("inversión", "dinero que cuesta instalar un sistema"), ("emisor", "pieza que deja salir el agua cerca de la planta"), ("caudal de un emisor", "litros por hora que entrega un emisor"), ("rango aceptable", "valores mínimo y máximo que se consideran correctos"), ("promedio", "suma de valores dividida por la cantidad de valores"), ("obstrucción", "bloqueo que impide el paso normal del agua")],
    worked=[
        ("Promedio de emisores", "Cuatro emisores de ejemplo entregan 6, 8, 8 y 10 litros por hora. ¿Cuál es el promedio?", ["Se suman: 6 más 8 más 8 más 10 es 32.", "Se divide entre 4."], "8 litros por hora"),
        ("Revisar un rango", "El rango de ejemplo es de 7 a 9 litros por hora. Un emisor entrega 10. ¿Está dentro del rango?", ["10 es mayor que el máximo de 9.", "Queda fuera del rango."], "No, está fuera del rango"),
    ],
    mistakes=[("Creer que el promedio cumple y que por eso todos los emisores están bien.", "Un promedio puede ocultar un emisor muy fuera de rango.", "Se revisa cada emisor contra el rango."),
              ("Elegir el sistema por un solo criterio, como el costo.", "Se ignoran la eficiencia, la mano de obra y el riesgo.", "Se comparan todos los criterios y se justifica la elección.")],
    T=[
        ("abc", "En Agropecuaria: ¿qué es la mano de obra de un sistema de riego?", "El trabajo humano que necesita para funcionar", "La cantidad de agua que pierde", "El precio de las mangueras", "La mano de obra es trabajo humano; la pérdida es la eficiencia y el precio es la inversión."),
        ("abc", "En Agropecuaria: ¿qué es el rango aceptable de un caudal?", "Los valores mínimo y máximo que se consideran correctos", "El caudal más bajo que existe", "El promedio de todos los emisores del predio", "El rango fija un mínimo y un máximo; el promedio es otra medida."),
        ("abc", "En Agropecuaria: ¿qué suele indicar un emisor con caudal muy bajo?", "Una posible obstrucción o falla", "Que el cultivo necesita más fertilizante", "Que el suelo es arcilloso", "Un caudal bajo apunta a obstrucción; la tarea de revisarla es de personal autorizado."),
        ("=", "{F} ¿Cuál es el promedio de caudal de los 4 emisores medidos?", "(8+9+8+3)//4", "Se suman los cuatro caudales y se divide entre 4.", " litros por hora"),
        ("abc", "{F} ¿Qué emisor de los medidos queda fuera del rango aceptable?", "El que entrega 3 litros por hora", "El que entrega 9 litros por hora", "El que entrega 8 litros por hora", "Solo 3 es menor que el mínimo de 7; 8 y 9 están dentro del rango."),
        ("abc", "{F} ¿Qué sistema de la ficha tiene la mayor eficiencia?", "Goteo", "Surcos", "Aspersión", "Goteo tiene 80 %, más que aspersión con 70 % y surcos con 50 %."),
        ("abc", "{F} ¿Qué sistema de la ficha tiene la inversión más baja?", "Surcos", "Goteo", "Aspersión", "Surcos tiene inversión baja; goteo la tiene alta y aspersión media."),
        ("abc", "{F} Si solo importa gastar lo menos posible en instalar el sistema, ¿qué sistema de la ficha convendría?", "Surcos, por su inversión baja, aunque pierde más agua", "Goteo, porque es el más eficiente", "Aspersión, porque su mano de obra es media", "El criterio es la inversión inicial y surcos es el más bajo."),
        ("abc", "{F} Una estudiante dice: «el promedio de los emisores es 7, así que todos cumplen». ¿Qué respuesta es correcta?", "Es falso: un emisor de 3 litros por hora está fuera de rango aunque el promedio parezca cercano", "Es cierto, porque el promedio está en el rango", "Es cierto, porque se debe revisar solo el promedio", "El promedio no oculta un emisor defectuoso; cada uno se compara con el rango."),
        ("abc", "{F} El jefe de campo quiere repetir la medición del emisor de 3 litros por hora cambiándolo por otro «sin avisar a nadie». ¿Qué corresponde?", "Anotar la lectura real e informar al técnico, que decide la revisión", "Borrar la lectura y anotar 8", "No anotar nada para no hacer problemas", "La lectura real se registra e informa para tomar una decisión."),
        ("=", "{F} Con el agua que aplica el sistema de surcos, 100 m³ brutos entregan al cultivo cierta cantidad neta. ¿Cuántos m³ netos llegan a la planta?", "100*50//100", "Se calcula el porcentaje de eficiencia sobre el volumen aplicado.", " m³"),
        ("=", "{F} Con 100 m³ brutos aplicados, ¿cuántos m³ netos más llegan a la planta con goteo que con surcos?", "100*80//100-100*50//100", "Se resta el volumen neto de surcos al del goteo.", " m³"),
        ("abc", "En Agropecuaria: ¿por qué no existe un sistema de riego que sea el mejor en todo?", "Porque cada uno gana en algunos criterios y pierde en otros", "Porque todos tienen la misma eficiencia", "Porque el riego no se puede comparar", "Eficiencia, inversión y mano de obra suelen compensarse entre sí."),
    ],
    ctx=("abc", "Un conocido te dice que su vecino instaló goteo y que él lo instalará «igual», sin consultar a nadie. ¿Qué le sugieres?", "Comparar con un técnico la eficiencia, la inversión y las condiciones de su predio", "Copiar el sistema del vecino sin más", "Elegir el más barato sin comparar", "Lo que sirve en un predio puede no servir en otro; la comparación debe usar los datos del suyo."),
    sc=[
        ("En Agropecuaria: ¿cómo se calcula el promedio de cuatro emisores?", "Se suman los cuatro valores y se divide entre 4", "El promedio resume el funcionamiento general."),
        ("En el trabajo agrícola: ¿qué se hace con un emisor fuera de rango?", "Se anota la lectura real y se informa al técnico", "Informar permite corregir la falla a tiempo."),
        ("{F} ¿Qué criterio del riego por goteo está en nivel alto en la ficha?", "La inversión", "El goteo cuesta más de instalar."),
    ],
    op=("Datos de ejemplo del «Fundo Demo»: riego de 5 emisores con caudales de 7, 9, 8, 3 y 8 litros por hora; rango aceptable de ejemplo de 7 a 9 litros por hora. Dos sistemas candidatos: X (eficiencia 60 %, inversión baja) y Y (eficiencia 85 %, inversión alta). Escribe (a) el promedio de los emisores, (b) cuál emisor está fuera de rango, (c) qué sistema es más eficiente y qué sistema tiene menor inversión, (d) qué haces con la lectura fuera de rango.",
        "(a) 7 + 9 + 8 + 3 + 8 = 35; 35 ÷ 5 = 7 litros por hora. (b) El de 3 litros por hora. (c) Y es más eficiente; X tiene menor inversión. (d) Se anota la lectura real y se informa al técnico; la revisión la hace personal autorizado.",
        ["calcula el promedio", "identifica el emisor fuera de rango", "compara eficiencia e inversión", "no altera la lectura y la informa"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal los caudales", "creer que el promedio basta", "cambiar la lectura"],
        "Pregunta: «¿cuál valor es menor que 7?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe cuatro caudales inventados, calcula el promedio y marca cuál queda fuera del rango de 7 a 9.",
    extend="Explica con un ejemplo por qué un solo emisor defectuoso puede perjudicar al cultivo aunque el promedio parezca normal.",
)
