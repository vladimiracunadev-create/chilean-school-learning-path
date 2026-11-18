"""Operaciones Portuarias TP 3.º y 4.º medio: OAE-03 (consolidar y desconsolidar contenedores como cálculo y lectura de documentos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_opor_common import AVISO, EMER, build

O3 = "TP-OPOR-3y4-OAE-03"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). En «Terminal Demo» hay una zona de consolidación donde se llenan de carga contenedores vacíos de 20 y de 40 pies (uno de 20 pies cuenta como 1 TEU y uno de 40 pies como 2 TEU). "
     "Hoy hay 8 contenedores de 20 pies y 6 de 40 pies por consolidar, a cargo de 5 cuadrillas de 4 personas. Rendimiento de ejemplo: una cuadrilla consolida 1 TEU por hora. "
     "Peligros anotados: vehículos de carga que circulan junto a la zona, carga que puede desplazarse dentro del contenedor, contenedores apilados en el patio, poca ventilación en el interior del contenedor y calor en verano.")
build(
    O3, 1, F,
    use="Aprenderé qué es consolidar y desconsolidar un contenedor, qué es un TEU, qué peligros tiene esta faena y por qué exige personal autorizado y norma vigente.",
    prior=["Sé qué es un contenedor.", "Sé distinguir peligro y riesgo y ordenar la jerarquía de controles.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Consolidar un contenedor es llenarlo con carga, que puede ser de un solo embarcador o de varios; desconsolidarlo es sacar esa carga al llegar a destino. Los contenedores más usados miden 20 o 40 pies. El TEU es la unidad con que se cuentan: un contenedor de 20 pies es 1 TEU y uno de 40 pies es 2 TEU. La consolidación puede ser manual, cuando la hacen personas a mano, o mecanizada, cuando parte del movimiento lo hacen equipos que opera solo personal autorizado.",
        "La faena tiene peligros propios: vehículos de carga en movimiento, carga que se desplaza dentro del contenedor, contenedores apilados, y un interior cerrado con poca ventilación, poca visibilidad y una sola salida. De ellos nacen riesgos como el atropello, el golpe o el atrapamiento, el aplastamiento y el malestar por calor. Se previenen con la jerarquía de controles: eliminar, sustituir, barreras físicas, reglas y permisos, y al final el EPP.",
        f"Entrar a un contenedor cerrado, conducir vehículos de carga o mover contenedores exige instructor autorizado y norma vigente. Este cuaderno solo enseña conceptos y cálculos en papel. {EMER} {AVISO}",
    ],
    vocab=[("consolidar", "llenar un contenedor con carga"), ("desconsolidar", "sacar la carga de un contenedor al llegar a destino"), ("TEU", "unidad de conteo: un contenedor de 20 pies es 1 TEU y uno de 40 pies es 2 TEU"), ("consolidación manual y mecanizada", "hecha por personas a mano o con equipos operados por personal autorizado"), ("espacio cerrado", "lugar con poca ventilación y una sola salida"), ("atrapamiento", "daño por quedar sujeto o apretado entre cosas")],
    worked=[
        ("Contar TEU", "Un patio de ejemplo tiene 5 contenedores de 20 pies y 3 de 40 pies. ¿Cuántos TEU son?", ["Los de 20 pies suman 5 TEU.", "Los de 40 pies suman 3 por 2, o sea 6 TEU, y 5 más 6 son 11."], "11 TEU"),
        ("Peligro y riesgo", "La puerta de un contenedor de ejemplo queda abierta hacia un pasillo de paso. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la puerta abierta hacia el pasillo, porque puede causar daño.", "El riesgo es que una persona que pasa se golpee con ella."], "Peligro: la puerta abierta sobre el pasillo; riesgo: que alguien se golpee"),
    ],
    mistakes=[("Contar un contenedor de 40 pies como 1 TEU.", "Un contenedor de 40 pies equivale a 2 TEU.", "Multiplica por 2 los contenedores de 40 pies al calcular TEU."),
              ("Creer que entrar a un contenedor es seguro porque «solo es una caja».", "Su interior cerrado tiene poca ventilación y una sola salida.", "Entrar exige autorización, formación y norma vigente.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es consolidar un contenedor?", "Llenarlo con carga, de un solo embarcador o de varios", "Sacar la carga al llegar a destino", "Anotar su número en el manifiesto de la nave", "Consolidar es llenar; sacar la carga es desconsolidar y anotar el número es un registro."),
        ("abc", "En Operaciones Portuarias: ¿cuánto cuenta un contenedor de 40 pies en TEU?", "2 TEU", "1 TEU", "4 TEU", "Un contenedor de 20 pies es 1 TEU y uno de 40 pies es el doble."),
        ("abc", "En Operaciones Portuarias: ¿por qué el interior de un contenedor cerrado se considera un espacio de riesgo?", "Porque tiene poca ventilación y una sola salida, y no se debe entrar sin autorización", "Porque siempre contiene carga peligrosa", "Porque su piso es siempre resbaladizo", "El riesgo viene de su ventilación y de su única salida, no de que siempre tenga carga peligrosa."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la carga que puede desplazarse dentro del contenedor?", "Que la carga se mueva y golpee o atrape a una persona", "Que el contenedor pierda su número de identificación", "Que el cronograma de la faena se atrase", "El riesgo es la posibilidad de daño a una persona; el número y el cronograma no son daños."),
        ("abc", "{F} Mantener separadas con barreras fijas la zona de consolidación y la ruta de los vehículos de carga es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla escrita", "De EPP, porque protege a las personas", "Una barrera fija separa los flujos sin depender de la memoria de cada persona."),
        ("abc", "{F} ¿Con qué peligro de la ficha se relaciona el riesgo de sentir malestar o falta de aire?", "La poca ventilación en el interior del contenedor", "Los contenedores apilados en el patio", "Los vehículos de carga junto a la zona", "La ventilación escasa afecta la respiración; los apilados y los vehículos se relacionan con golpes y atropellos."),
        ("=", "{F} ¿Cuántos TEU hay por consolidar hoy?", "8+6*2", "Cada contenedor de 20 pies es 1 TEU y cada uno de 40 pies es 2 TEU.", " TEU"),
        ("=", "{F} ¿Cuántas personas hay en las 5 cuadrillas?", "5*4", "Se multiplican las cuadrillas por las personas de cada una.", " personas"),
        ("=", "Un patio de ejemplo tiene capacidad para 120 TEU y ya ocupa 86. ¿Cuántos contenedores de 40 pies caben todavía?", "(120-86)//2", "Se calculan los TEU libres y se dividen entre los 2 TEU de cada contenedor de 40 pies.", " contenedores"),
        ("abc", "Durante una visita de ejemplo, un contenedor apilado se inclina y amenaza con caer junto a una persona. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a empujar el contenedor para sostenerlo", "Pasar rápido por debajo para llegar al otro lado", "Un contenedor que cae puede aplastar; se avisa y se mantiene la distancia."),
        ("abc", "En Operaciones Portuarias: ¿por qué entrar a un contenedor cerrado exige autorización y personal formado?", "Porque su interior puede tener poca ventilación, poca visibilidad y una sola salida", "Porque dentro siempre hay carga peligrosa", "Porque el contenedor pertenece a la naviera y nadie más puede entrar", "Las condiciones del interior son el riesgo; no depende del contenido ni de quién es dueño."),
        ("=", "{F} Con el rendimiento de ejemplo y las 5 cuadrillas trabajando a la vez, ¿cuántas horas tardan en consolidar todos los contenedores de la ficha?", "(8+6*2)//5", "Se calculan los TEU totales y se dividen entre los TEU que consolidan las 5 cuadrillas por hora.", " horas"),
        ("abc", "{F} Para reducir el riesgo por poca ventilación y calor, ¿cuál medida es de nivel más efectivo en la jerarquía de controles?", "Rediseñar el trabajo para que nadie tenga que permanecer en el interior cerrado", "Poner un letrero que pida beber agua", "Entregar ropa liviana a todo el personal", "Eliminar la exposición actúa sobre el peligro; el letrero es administrativo y la ropa es EPP."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por «ayudar unas horas a llenar contenedores» en un patio, porque «solo hay que pasar cajas». ¿Qué respondes?", "Que no, porque esa faena exige instructor autorizado, norma vigente y elementos de protección, y que lo consultarás con un adulto responsable", "Que sí, si te presta guantes", "Que sí, pero solo en contenedores de 20 pies", "Los guantes o el tamaño del contenedor no reemplazan la formación ni la autorización."),
    sc=[
        ("En Operaciones Portuarias: ¿qué es desconsolidar un contenedor?", "Sacar la carga del contenedor al llegar a destino", "Desconsolidar es la operación inversa a llenar el contenedor."),
        ("¿Cuántos TEU son tres contenedores de 40 pies?", "6 TEU", "Cada contenedor de 40 pies cuenta como 2 TEU."),
        ("¿Qué riesgo tiene el interior cerrado de un contenedor?", "Poca ventilación y una sola salida", "Estas condiciones hacen que entrar exija autorización."),
    ],
    op=("Una tarea de ejemplo anota: desconsolidar un contenedor en una bodega cerrada, con calor y con vehículos de carga que circulan cerca de la puerta. Escribe (a) un peligro de la tarea y su riesgo asociado, (b) un control administrativo, (c) un control de ingeniería, (d) qué hacer si se ve que una persona queda atrapada dentro de un contenedor.",
        "(a) Peligro: la poca ventilación y el calor dentro del contenedor; riesgo: que una persona sufra un malestar grave. (b) Un permiso de ingreso y letreros que prohíban entrar sin autorización. (c) Una barrera fija que separe la puerta del contenedor de la ruta de los vehículos de carga. (d) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias. La tarea la hace personal autorizado.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "indica no intervenir y avisar"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "proponer el EPP como único control", "sugerir entrar a sacar a la persona"],
        "Pregunta: «¿qué control cambia físicamente el lugar?». Si no responde, pídele que relea el nivel de ingeniería de la jerarquía."),
    reinforce="Inventa un patio con contenedores de 20 y de 40 pies y calcula sus TEU.",
    extend="Explica con un ejemplo la diferencia entre consolidación manual y mecanizada y un riesgo de cada una.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). Contenedor ficticio de 20 pies, de carga seca, código «ABCD 123456 7» (código inventado). Placa de datos de ejemplo: tara 2.300 kg; peso bruto máximo 24.000 kg. "
     "Informe de consolidación: el contenedor lleva carga de 3 embarcadores. Embarcador 1: 120 bultos, 3.000 kg. Embarcador 2: 80 bultos, 4.400 kg. Embarcador 3: 50 bultos, 2.600 kg. Precinto N.º 0045.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario del contenedor (tara, carga útil, peso bruto, precinto), la diferencia entre carga completa y consolidada y qué documentos acompañan a la consolidación.",
    prior=["Sé qué es consolidar y desconsolidar y qué es un TEU.", "Sé sumar y restar pesos en kilogramos.", "Sé qué es un conocimiento de embarque y una lista de embalaje."],
    explain=[
        "Cada contenedor tiene una placa de datos con su identificación y sus pesos. La tara es el peso del contenedor vacío. La carga útil es el peso de la carga que lleva, y el peso bruto es la tara más la carga. El peso bruto máximo es el límite que no puede superarse, y se lee en la placa de datos. Un contenedor es FCL cuando lleva la carga completa de un solo embarcador, y LCL cuando reúne carga de varios embarcadores.",
        "El precinto es un sello numerado que se coloca en la puerta para evidenciar si el contenedor fue abierto, y su número se registra en los documentos. El informe de consolidación registra qué carga de cada embarcador entró al contenedor, con sus bultos y su peso. El contenedor refrigerado mantiene una temperatura de ejemplo y el que lleva mercancías peligrosas muestra etiquetas de peligro; ambos requieren personal capacitado y norma vigente.",
        f"Si el número del precinto, los bultos o los pesos no coinciden entre los documentos y el contenedor, se registra la diferencia y se informa; no se corrige a mano. {EMER} {AVISO}",
    ],
    vocab=[("tara", "peso del contenedor vacío"), ("carga útil", "peso de la carga que lleva el contenedor"), ("peso bruto", "tara más carga"), ("peso bruto máximo", "límite de peso que no puede superarse, indicado en la placa de datos"), ("FCL y LCL", "contenedor completo de un embarcador, y contenedor con carga de varios embarcadores"), ("precinto", "sello numerado que evidencia si el contenedor fue abierto"), ("informe de consolidación", "documento que registra qué carga entró al contenedor")],
    worked=[
        ("Peso bruto", "Un contenedor de ejemplo tiene tara 3.800 kg y lleva 18.200 kg de carga. ¿Cuál es su peso bruto?", ["El peso bruto es la tara más la carga.", "3.800 más 18.200 son 22.000."], "22.000 kg"),
        ("FCL o LCL", "Un contenedor de ejemplo lleva toda la carga de un solo embarcador. ¿Es FCL o LCL?", ["Hay un único embarcador.", "Carga completa de un solo embarcador es FCL."], "FCL"),
    ],
    mistakes=[("Confundir tara con carga útil.", "La tara es el peso del contenedor vacío y la carga útil es la carga que lleva.", "Pregunta: ¿pesa el contenedor o pesa lo que lleva?"),
              ("Comparar solo la carga con el peso bruto máximo.", "El máximo cuenta tara y carga juntas.", "Suma la tara y la carga antes de comparar.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la tara de un contenedor?", "El peso del contenedor vacío", "El peso de la carga que lleva", "El peso máximo que soporta al apilarse", "La tara es el peso del contenedor vacío; la carga se mide aparte."),
        ("abc", "En Operaciones Portuarias: ¿qué diferencia hay entre un contenedor FCL y uno LCL?", "El FCL lleva la carga completa de un embarcador y el LCL reúne carga de varios", "El FCL reúne carga de varios embarcadores y el LCL es de uno solo", "El FCL es refrigerado y el LCL es de carga seca", "FCL es carga completa de un embarcador; LCL es carga consolidada de varios."),
        ("abc", "En Operaciones Portuarias: ¿qué es el precinto de un contenedor?", "Un sello numerado que evidencia si fue abierto y cuyo número se registra en los documentos", "Una llave que cualquier persona puede usar para abrir la puerta", "Una etiqueta que indica el peso de la carga", "El precinto sirve para detectar aperturas y se anota en los documentos."),
        ("abc", "{F} ¿Qué tipo de contenedor es el de la ficha por la cantidad de embarcadores?", "LCL, porque reúne carga de 3 embarcadores", "FCL, porque está lleno", "FCL, porque tiene un precinto", "Con tres embarcadores es carga consolidada, es decir, LCL."),
        ("abc", "{F} ¿Dónde se lee el peso bruto máximo del contenedor?", "En la placa de datos", "En el precinto", "En el informe de consolidación", "La placa de datos indica la tara y el peso bruto máximo."),
        ("abc", "{F} ¿Qué documento registra qué carga de cada embarcador entró al contenedor?", "El informe de consolidación", "La placa de datos", "El manifiesto de la nave", "El informe detalla bultos y pesos por embarcador."),
        ("=", "{F} ¿Cuántos kilogramos de carga lleva el contenedor en total?", "3000+4400+2600", "Se suman los pesos de los tres embarcadores.", " kg"),
        ("=", "{F} ¿Cuál es el peso bruto del contenedor con su carga?", "2300+3000+4400+2600", "El peso bruto es la tara más la carga de los tres embarcadores.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos más de carga admite el contenedor sin pasar su peso bruto máximo?", "24000-(2300+3000+4400+2600)", "Se resta el peso bruto actual al peso bruto máximo.", " kg"),
        ("abc", "{F} Se propone agregar un cuarto embarcador con 12.000 kg. ¿Es posible?", "No, porque el peso bruto llegaría a 24.300 kg, sobre el máximo de 24.000 kg", "Sí, porque 12.000 kg es menos que 24.000 kg", "Sí, porque el máximo se mide sin contar la tara", "El máximo cuenta la tara y toda la carga, y con el cuarto embarcador se superaría."),
        ("abc", "{F} Un compañero dice: «si el número del precinto del contenedor es distinto al del documento, da lo mismo». ¿Qué respuesta es correcta?", "Es falso: la diferencia se registra e informa, porque puede indicar que se abrió o que hay un error", "Es cierto: el precinto no importa si el peso coincide", "Es cierto, si el contenedor está cerrado", "El precinto evidencia aperturas; una diferencia debe investigarse."),
        ("=", "{F} ¿Cuántos kilogramos pesa en promedio cada bulto del embarcador 2?", "4400//80", "Se divide el peso del embarcador 2 entre sus bultos.", " kg"),
        ("abc", "{F} El informe registra 250 bultos y al desconsolidar se cuentan 248. ¿Qué corresponde?", "Registrar un faltante de 2 bultos e informar a quien corresponde", "Corregir el informe a 248 bultos", "Cerrar sin avisar, porque 2 bultos son pocos", "Una diferencia se registra e informa; no se cambia el informe para que cuadre."),
    ],
    ctx=("abc", "Una persona de la bodega de ejemplo te pide anotar en el informe el número de precinto de otro contenedor «porque el verdadero se ve borroso». ¿Qué respondes?", "Que se anote lo que se lee en el contenedor y la duda se informe a quien corresponde", "Que lo anotas del otro contenedor, porque son parecidos", "Que anotas cualquier número y después se corrige", "El precinto es un control de integridad; anotar un número falso lo anula."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calcula el peso bruto?", "Sumando la tara y la carga", "El peso bruto incluye el contenedor y lo que lleva."),
        ("¿Qué es un contenedor LCL?", "Uno que reúne carga de varios embarcadores", "LCL significa carga consolidada de varios embarcadores."),
        ("¿Para qué sirve el precinto?", "Para evidenciar si el contenedor fue abierto", "Su número se registra para poder comprobarlo."),
    ],
    op=("Contenedor ficticio de 40 pies. Placa de datos de ejemplo: tara 3.900 kg; peso bruto máximo 30.000 kg. Informe de consolidación: embarcador A, 90 bultos, 5.400 kg; embarcador B, 60 bultos, 8.100 kg. Precinto N.º 0112. Escribe (a) si el contenedor es FCL o LCL, (b) el peso de la carga, (c) el peso bruto, (d) si se pueden agregar 15.000 kg más y por qué.",
        "(a) LCL, porque reúne carga de dos embarcadores. (b) 5.400 + 8.100 = 13.500 kg. (c) 3.900 + 13.500 = 17.400 kg. (d) No: el peso bruto llegaría a 17.400 + 15.000 = 32.400 kg, más que el máximo de 30.000 kg.",
        ["clasifica correctamente FCL o LCL", "suma la carga", "calcula el peso bruto con la tara", "compara con el máximo y concluye"],
        ["hoja con las cuatro respuestas"],
        ["olvidar sumar la tara", "comparar solo la carga con el máximo", "confundir FCL con LCL"],
        "Pregunta: «¿qué incluye el peso bruto?». Si no responde, pídele que relea la definición de peso bruto."),
    reinforce="Escribe con tus palabras la diferencia entre tara, carga útil y peso bruto y da un ejemplo numérico inventado.",
    extend="Explica con un ejemplo por qué una diferencia en el número de precinto debe informarse.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Contenedor de ejemplo de 20 pies, de carga seca: interior de 6 m de largo, 2 m de ancho y 2 m de alto; carga útil máxima de ejemplo, 20.000 kg. "
     "Lista de la carga: 6 cajas tipo A de 2 m de largo, 1 m de ancho y 1 m de alto, de 400 kg cada una; y 6 cajas tipo B de 1 m por 1 m por 1 m, de 250 kg cada una.")
build(
    O3, 3, F,
    use="Aprenderé a cubicar una carga, es decir, a calcular su volumen, y a compararla con el volumen interior de un contenedor para saber cuánto aprovecha.",
    prior=["Sé multiplicar números enteros.", "Sé qué es la carga útil de un contenedor.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Cubicar una carga es calcular el volumen que ocupa, en metros cúbicos (m³). Para un bulto con forma de caja el volumen es el largo por el ancho por el alto, medidos en metros. El volumen de varios bultos iguales es el volumen de uno multiplicado por la cantidad. El volumen interior del contenedor se calcula igual con sus medidas interiores.",
        "El aprovechamiento de un contenedor es el porcentaje de su volumen interior que ocupa la carga: se divide el volumen de la carga entre el volumen interior y se multiplica por 100. Para saber si una carga cabe hay que comprobar dos límites por separado: que su volumen no supere el interior y que su peso no supere la carga útil máxima. Aquí solo calculamos en planilla; cómo se coloca la carga dentro del contenedor lo enseña un instructor autorizado.",
        f"Todas las medidas y pesos de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular el volumen que ocupa una carga, en metros cúbicos"), ("volumen de una caja", "largo por ancho por alto"), ("volumen interior", "espacio disponible dentro del contenedor, en metros cúbicos"), ("aprovechamiento", "porcentaje del volumen interior que ocupa la carga"), ("carga útil máxima", "peso máximo de carga que el contenedor puede llevar")],
    worked=[
        ("Volumen de una caja", "Una caja de ejemplo mide 3 m de largo, 2 m de ancho y 1 m de alto. ¿Cuál es su volumen?", ["El volumen es largo por ancho por alto.", "3 por 2 es 6, y 6 por 1 es 6."], "6 m³"),
        ("Aprovechamiento", "Un contenedor de ejemplo tiene 30 m³ interiores y lleva una carga de 15 m³. ¿Qué porcentaje aprovecha?", ["Se divide 15 entre 30, que es la mitad.", "La mitad equivale a 50 de cada 100."], "50 %"),
    ],
    mistakes=[("Sumar largo, ancho y alto en lugar de multiplicarlos.", "La suma da una longitud, no un volumen.", "Multiplica las tres medidas para obtener metros cúbicos."),
              ("Comprobar solo el volumen y olvidar el peso.", "Puede caber por volumen y superar la carga útil máxima.", "Haz las dos comprobaciones por separado.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es cubicar una carga?", "Calcular el volumen que ocupa, en metros cúbicos", "Calcular su peso total en kilogramos", "Contar los bultos de cada tipo", "Cubicar es calcular volumen; el peso y el conteo son otros cálculos."),
        ("abc", "En Operaciones Portuarias: ¿cómo se calcula el volumen de un bulto con forma de caja?", "Multiplicando largo por ancho por alto", "Sumando largo, ancho y alto", "Multiplicando solo el largo por el ancho", "El volumen necesita las tres medidas multiplicadas."),
        ("abc", "En Operaciones Portuarias: ¿qué es el aprovechamiento de un contenedor?", "El porcentaje de su volumen interior que ocupa la carga", "El número de contenedores que se llenan en un turno", "El peso de la carga dividido entre los bultos", "El aprovechamiento compara el volumen de la carga con el interior."),
        ("=", "{F} ¿Cuántos metros cúbicos tiene el volumen interior del contenedor?", "6*2*2", "Se multiplican el largo, el ancho y el alto interiores.", " m³"),
        ("=", "{F} ¿Cuántos metros cúbicos ocupan las 6 cajas tipo A?", "6*(2*1*1)", "Se calcula el volumen de una caja tipo A y se multiplica por la cantidad.", " m³"),
        ("abc", "{F} ¿Qué datos se necesitan para saber si la carga cabe por volumen?", "El volumen total de la carga y el volumen interior del contenedor", "El peso de la carga y la tara del contenedor", "El número de precinto y el código del contenedor", "El cabimiento por volumen compara volumen con volumen."),
        ("=", "{F} ¿Cuántos metros cúbicos ocupa la carga completa?", "6*(2*1*1)+6*(1*1*1)", "Se suma el volumen de las cajas tipo A y el de las cajas tipo B.", " m³"),
        ("=", "{F} ¿Cuántos kilogramos pesa la carga completa?", "6*400+6*250", "Se multiplican las cajas de cada tipo por su peso y se suman.", " kg"),
        ("=", "{F} ¿Qué porcentaje del volumen interior aprovecha la carga?", "(6*(2*1*1)+6*(1*1*1))*100//(6*2*2)", "Se divide el volumen de la carga entre el interior y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cumple la carga la condición de peso?", "Sí, porque su peso total no supera la carga útil máxima de ejemplo", "No, porque el peso debe ser igual a la carga útil máxima", "No, porque la carga ocupa menos del 100 % del volumen", "El peso se compara con su propio límite; ocupar menos volumen no lo invalida."),
        ("abc", "{F} Un compañero propone agregar 8 cajas tipo A más «porque todavía cabe peso». ¿Qué corresponde comprobar?", "El volumen: con esas cajas la carga llegaría a 34 m³, sobre los 24 m³ interiores", "Nada: si cabe en peso, cabe en volumen", "Solo el número del precinto", "El volumen es un límite distinto del peso y aquí se superaría."),
        ("=", "{F} ¿Cuántas cajas tipo B, de 1 m³ cada una, caben todavía por volumen libre?", "(6*2*2)-(6*(2*1*1)+6*(1*1*1))", "Se resta el volumen de la carga al volumen interior y se divide entre 1 m³ por caja.", " cajas"),
        ("abc", "{F} Se quiere sumar 5 cajas tipo A a la carga actual. ¿Cabe por volumen?", "No, porque el volumen que ocupan supera el volumen libre", "Sí, porque solo se cuentan los bultos y no el volumen", "Sí, porque el peso todavía lo permite", "Cada caja tipo A ocupa 2 m³ y el espacio libre no alcanza."),
    ],
    ctx=("abc", "Un compañero de práctica calcula el volumen de una caja sumando sus tres medidas y dice «la caja cabe». ¿Qué le respondes?", "Que el volumen se calcula multiplicando las tres medidas y que debe rehacer el cálculo", "Que está bien, porque sumar es más rápido", "Que solo hay que medir el largo", "Sumar medidas da una longitud y no el volumen."),
    sc=[
        ("En Operaciones Portuarias: ¿cuál es el volumen de una caja de 2 m por 2 m por 3 m?", "12 m³", "Se multiplican las tres medidas de la caja."),
        ("¿Qué dos límites se comprueban para saber si una carga cabe?", "El volumen y el peso, por separado", "Cumplir uno no garantiza cumplir el otro."),
        ("¿Cómo se calcula el aprovechamiento?", "Volumen de la carga dividido entre el interior, por 100", "El resultado se expresa como porcentaje."),
    ],
    op=("Contenedor de ejemplo con interior de 5 m de largo, 2 m de ancho y 2 m de alto, y carga útil máxima de 15.000 kg. Carga: 4 cajas tipo P de 1 m por 1 m por 2 m, de 300 kg cada una; 8 cajas tipo Q de 1 m por 1 m por 1 m, de 150 kg cada una. Escribe (a) el volumen interior, (b) el volumen de la carga, (c) el aprovechamiento en porcentaje, (d) el peso de la carga y si cumple el límite.",
        "(a) 5 × 2 × 2 = 20 m³. (b) 4 × 2 + 8 × 1 = 16 m³. (c) 16 ÷ 20 × 100 = 80 %. (d) 4 × 300 + 8 × 150 = 2.400 kg, que no supera 15.000 kg: cumple.",
        ["calcula el volumen interior", "calcula el volumen de la carga", "calcula el porcentaje", "calcula el peso y lo compara"],
        ["hoja con las cuatro respuestas"],
        ["sumar las medidas en vez de multiplicarlas", "olvidar multiplicar por la cantidad de cajas", "revisar solo el volumen"],
        "Pregunta: «¿qué dos comprobaciones hay que hacer?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa tres cajas con sus tres medidas y calcula el volumen de cada una.",
    extend="Explica con un ejemplo por qué un contenedor puede estar lleno por volumen y aun así estar lejos de su carga útil máxima.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Un lote de 240 cajas de 1 m³ y 500 kg cada una debe consolidarse en contenedores de 40 pies de ejemplo. Cada contenedor tiene un volumen interior de 60 m³ y una carga útil máxima de 24.000 kg. "
     "Costo de ejemplo: $90.000 por contenedor.")
build(
    O3, 4, F,
    use="Aprenderé a decidir cuántas cajas caben en un contenedor según el límite que se alcanza primero, a calcular cuántos contenedores se necesitan y su costo.",
    prior=["Sé cubicar una carga y calcular su peso.", "Sé qué es la carga útil.", "Sé dividir números enteros."],
    explain=[
        "Un contenedor se llena cuando se alcanza el primer límite: el volumen interior o la carga útil máxima. Para saber cuántas cajas caben por volumen se divide el volumen interior entre el volumen de cada caja; por peso, se divide la carga útil máxima entre el peso de cada caja. Se carga la menor de las dos cantidades, porque con la mayor se superaría el otro límite. Se dice que el contenedor se llena por peso cuando el peso limita antes que el volumen, y por volumen cuando ocurre al revés.",
        "Con las cajas por contenedor se calcula cuántos contenedores se necesitan: se divide el total de cajas entre las que caben en cada uno. El costo total es el número de contenedores por el costo de cada uno. Un contenedor de 40 pies cuenta 2 TEU. Si el lote no se reparte exacto, el último contenedor lleva menos carga.",
        f"Los datos son de ejemplo para un cálculo de planilla. {EMER} {AVISO}",
    ],
    vocab=[("carga útil máxima", "peso máximo de carga que puede llevar un contenedor"), ("límite que manda", "el límite, de volumen o de peso, que se alcanza primero"), ("llenarse por peso", "alcanzar la carga útil máxima antes que el volumen interior"), ("lote", "conjunto de carga que se consolida junto"), ("costo total", "número de contenedores por el costo de cada uno")],
    worked=[
        ("Qué límite manda", "Un contenedor de ejemplo tiene 30 m³ y carga útil de 9.000 kg. Se cargan cajas de 2 m³ y 300 kg. ¿Cuántas caben?", ["Por volumen caben 30 dividido en 2, o sea 15.", "Por peso caben 9.000 dividido en 300, o sea 30. Se carga la menor cantidad."], "15 cajas; manda el volumen"),
        ("Contenedores necesarios", "Un lote de ejemplo de 90 cajas se carga con 15 cajas por contenedor. ¿Cuántos contenedores se necesitan?", ["Se divide el total de cajas entre las de cada contenedor.", "90 dividido en 15 son 6."], "6 contenedores"),
    ],
    mistakes=[("Cargar según el volumen sin revisar el peso.", "Se puede superar la carga útil máxima aunque sobre espacio.", "Calcula las cajas por volumen y por peso y toma la menor cantidad."),
              ("Tomar la mayor de las dos cantidades como la que cabe.", "Con la mayor se superaría el otro límite.", "Se carga la menor de las dos.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es la carga útil máxima de un contenedor?", "El peso máximo de carga que puede llevar, sin contar la tara", "El peso del contenedor vacío más la carga", "El volumen interior disponible", "La carga útil máxima limita el peso de la carga; el volumen es otro límite."),
        ("abc", "En Operaciones Portuarias: ¿qué dos límites se comprueban para saber cuántas cajas caben en un contenedor?", "El volumen interior y la carga útil máxima", "La tara y el número de precinto", "El puerto de destino y el orden de descarga", "Caben las cajas que respetan el volumen y el peso."),
        ("abc", "En Operaciones Portuarias: ¿cuántos TEU cuenta un contenedor de 40 pies?", "2 TEU", "1 TEU", "4 TEU", "El contenedor de 40 pies equivale a dos de 20 pies."),
        ("=", "{F} ¿Cuántas cajas caben en un contenedor por peso?", "24000//500", "Se divide la carga útil máxima entre el peso de cada caja.", " cajas"),
        ("abc", "{F} ¿Qué límite determina cuántas cajas se cargan por contenedor?", "El peso, porque por peso caben menos cajas que por volumen", "El volumen, porque es el primero que se calcula", "Ninguno, porque se carga hasta llenar el contenedor", "Por volumen caben 60 cajas y por peso 48, así que el peso se alcanza primero."),
        ("=", "{F} ¿Cuántos contenedores se necesitan para el lote?", "240//(24000//500)", "Se dividen las cajas del lote entre las que caben por contenedor.", " contenedores"),
        ("=", "{F} ¿Cuántos pesos cuesta consolidar todo el lote?", "(240//(24000//500))*90000", "Se multiplican los contenedores necesarios por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuántos TEU son los contenedores que usa el lote?", "(240//(24000//500))*2", "Cada contenedor de 40 pies cuenta como 2 TEU.", " TEU"),
        ("=", "Otro lote de ejemplo tiene 180 cajas de 2 m³ y 300 kg cada una. Cada contenedor de 20 pies tiene 30 m³ interiores y 9.000 kg de carga útil máxima. ¿Cuántos contenedores se necesitan?", "180//(30//2)", "Caben 15 cajas por volumen y 30 por peso; se usa la menor cantidad y se divide el lote entre ella.", " contenedores"),
        ("abc", "{F} Si el lote fuera de 250 cajas, ¿cuántos contenedores se necesitarían?", "6 contenedores, porque 5 llevarían 240 cajas y quedan 10 para un sexto", "5 contenedores, porque 250 dividido en 48 se redondea hacia abajo", "5 contenedores, repartiendo las 10 cajas restantes entre ellos aunque superen la carga útil", "Cinco contenedores llenan 240 cajas; las 10 restantes necesitan otro contenedor."),
        ("abc", "{F} Un cliente propone cargar 60 cajas por contenedor «porque caben por volumen». ¿Qué corresponde?", "No, porque 60 cajas pesarían 30.000 kg y superarían la carga útil de 24.000 kg", "Sí, porque el volumen es el único límite", "Sí, si se informa al cliente", "El peso también es un límite y 60 cajas lo exceden."),
        ("=", "{F} Con los contenedores llenos por peso, ¿cuántos metros cúbicos de volumen interior quedan sin usar en total?", "(240//(24000//500))*(60-24000//500)", "Se calcula el volumen libre de cada contenedor y se multiplica por la cantidad de contenedores.", " m³"),
        ("abc", "Se comparan dos opciones para el mismo lote de 240 cajas de 500 kg. Opción 1: 5 contenedores de 40 pies a $90.000 cada uno. Opción 2: 10 contenedores de 20 pies, que también alcanzan para el lote, a $50.000 cada uno. ¿Cuál es más barata?", "La opción 1, porque cuesta $450.000 frente a $500.000", "La opción 2, porque cada contenedor individual es más barato", "Cuestan lo mismo, porque llevan la misma carga", "Se compara el costo total de cada opción, no el de un solo contenedor."),
    ],
    ctx=("abc", "Una persona de la oficina de ejemplo dice: «cargamos 60 cajas por contenedor, total por volumen caben y el peso se verá después». ¿Qué respondes?", "Que el peso también debe comprobarse antes, porque puede superar la carga útil máxima", "Que está bien, porque el volumen manda siempre", "Que se carga y se revisa el peso en el destino", "Un exceso de peso es un riesgo y debe evitarse en la planificación."),
    sc=[
        ("En Operaciones Portuarias: ¿qué cantidad de cajas se carga si por volumen caben 20 y por peso 25?", "20 cajas", "Se toma la menor para no superar el límite de volumen."),
        ("¿Cómo se calculan los contenedores necesarios?", "Dividiendo las cajas del lote entre las que caben por contenedor", "Cada contenedor se llena con la cantidad que cabe."),
        ("¿Cómo se calcula el costo total?", "Multiplicando los contenedores por el costo de cada uno", "Es un cálculo directo de planilla."),
    ],
    op=("Un lote de 144 cajas de 1 m³ y 500 kg cada una se consolida en contenedores de 20 pies de ejemplo, de 30 m³ interiores y 12.000 kg de carga útil máxima, a $40.000 cada uno. Escribe (a) cuántas cajas caben por volumen, (b) cuántas caben por peso, (c) cuántos contenedores se necesitan, (d) cuánto cuesta el lote.",
        "(a) 30 ÷ 1 = 30 cajas por volumen. (b) 12.000 ÷ 500 = 24 cajas por peso. (c) Manda el peso: 144 ÷ 24 = 6 contenedores. (d) 6 × 40.000 = $240.000.",
        ["calcula las cajas por volumen", "calcula las cajas por peso", "usa el límite que manda", "calcula el costo total"],
        ["hoja con las cuatro respuestas"],
        ["usar el volumen sin revisar el peso", "dividir el lote entre la cantidad mayor", "olvidar multiplicar por el costo"],
        "Pregunta: «¿qué límite se alcanza primero?». Si no responde, pídele que compare las dos cantidades."),
    reinforce="Inventa un contenedor con volumen y carga útil, una caja con volumen y peso, y calcula cuántas caben.",
    extend="Explica con un ejemplo por qué se carga la menor de las dos cantidades y no la mayor.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Hay que consolidar 480 bultos. Alternativa manual (M): 6 personas que hacen 8 bultos por persona por hora. Alternativa mecanizada (E), con equipos que opera solo personal autorizado: "
     "3 personas y un rendimiento total de 60 bultos por hora. Costo de ejemplo: $10.000 por persona por hora; el equipo de la alternativa E cuesta $60.000 por hora. Plazo: 12 horas. "
     "Al desconsolidar en destino se cuentan 478 bultos; el informe de consolidación dice 480. Lista de verificación de cierre: número de contenedor, número de precinto, bultos y peso, marcas de manipulación.")
build(
    O3, 5, F,
    use="Aprenderé a comparar una consolidación manual con una mecanizada por plazo, costo y riesgo, y a verificar la calidad con una lista de verificación y la conciliación de bultos.",
    prior=["Sé calcular rendimiento, horas y costos.", "Sé qué es una lista de verificación y conciliar registros.", "Sé qué es un faltante."],
    explain=[
        "Para comparar dos alternativas de consolidación se calculan las horas que tarda cada una, dividiendo los bultos entre su rendimiento, y su costo total, multiplicando el costo por hora por las horas. Sirve la alternativa que cumple el plazo; entre las que cumplen, conviene la de menor costo. Si solo una cumple el plazo, esa es la que sirve aunque cueste más.",
        "También se comparan los riesgos. El manejo manual expone a sobreesfuerzos por levantar y empujar peso. La alternativa mecanizada reduce ese esfuerzo, pero suma riesgos de atropello y de cargas en movimiento, y por eso los equipos los opera solo personal autorizado, con norma vigente. Ninguna alternativa elimina la necesidad de controles.",
        f"Al cerrar se usa la lista de verificación: se revisa cada punto antes de cerrar, sin anotar de memoria, y se concilian los bultos del informe con los contados en destino; una diferencia se registra e informa. Los costos y rendimientos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las formas posibles de hacer una operación"), ("consolidación mecanizada", "consolidación en que parte del movimiento lo hacen equipos operados por personal autorizado"), ("sobreesfuerzo", "daño por levantar, empujar o sostener demasiado peso"), ("costo total", "costo por hora multiplicado por las horas de la operación"), ("lista de verificación", "lista de puntos que se revisan uno por uno antes de cerrar")],
    worked=[
        ("Horas de una alternativa", "Hay que consolidar 300 bultos con 5 personas que hacen 6 bultos por persona por hora. ¿Cuántas horas tardan?", ["El rendimiento total es 5 por 6, o sea 30 bultos por hora.", "300 dividido en 30 son 10."], "10 horas"),
        ("Elegir alternativa", "La alternativa X tarda 8 horas y cuesta $400.000; la Y tarda 6 horas y cuesta $450.000. El plazo es de 10 horas. ¿Cuál conviene?", ["Ambas cumplen el plazo de 10 horas.", "Entre las que cumplen, conviene la de menor costo: X."], "La alternativa X"),
    ],
    mistakes=[("Elegir siempre la alternativa mecanizada por ser más rápida.", "Puede costar más sin que el plazo lo exija y tiene riesgos propios.", "Compara plazo, costo y riesgo antes de decidir."),
              ("Anotar de memoria un dato de la lista de verificación.", "La lista se revisa punto por punto, mirando el dato real.", "Verifica cada punto en el contenedor y en el documento.")],
    T=[
        ("abc", "En Operaciones Portuarias: ¿qué es una consolidación mecanizada?", "Una consolidación en que parte del movimiento lo hacen equipos operados por personal autorizado", "Una consolidación sin ningún registro escrito", "Una consolidación hecha solo con las manos de la cuadrilla", "Mecanizada significa que hay equipos; los operan personas autorizadas."),
        ("abc", "En Operaciones Portuarias: ¿qué riesgo es típico del manejo manual de bultos?", "Los sobreesfuerzos por levantar o empujar peso", "El atropello por un equipo mecánico", "La caída de una carga suspendida", "El esfuerzo físico es el riesgo del manejo manual; los otros aparecen con equipos."),
        ("abc", "En Operaciones Portuarias: ¿qué es el costo total de una alternativa?", "El costo por hora multiplicado por las horas que dura la operación", "El costo de una sola hora de trabajo", "El valor de la carga que se consolida", "El costo total considera todas las horas que se usa la alternativa."),
        ("=", "{F} ¿Cuántos bultos por hora hace la alternativa manual?", "6*8", "Se multiplican las personas por los bultos de cada una por hora.", " bultos por hora"),
        ("=", "{F} ¿Cuántas horas tarda la alternativa manual en consolidar los 480 bultos?", "480//(6*8)", "Se dividen los bultos entre el rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántas horas tarda la alternativa mecanizada?", "480//60", "Se dividen los bultos entre su rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántos pesos cuesta la alternativa manual?", "6*10000*(480//(6*8))", "Se multiplican las personas por el costo por persona y por las horas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la alternativa mecanizada, contando el costo del equipo?", "(3*10000+60000)*(480//60)", "El costo por hora suma las personas y el equipo, y se multiplica por las horas.", " pesos"),
        ("abc", "{F} ¿Qué alternativa conviene con el plazo de 12 horas?", "La alternativa M, porque cumple el plazo y cuesta menos", "La alternativa E, porque termina antes", "Ninguna, porque las dos superan el plazo", "Ambas cumplen y la manual es más barata."),
        ("abc", "{F} Si el plazo fuera de 9 horas, ¿qué alternativa serviría?", "Solo la E, porque la M tardaría 10 horas", "Solo la M, porque es la más barata", "Las dos, porque ambas terminan antes de 12 horas", "La alternativa M excede las 9 horas; solo la E cumple."),
        ("abc", "{F} Al desconsolidar se cuentan 478 bultos y el informe dice 480. ¿Qué corresponde?", "Registrar un faltante de 2 bultos y avisar a quien corresponde", "Corregir el informe a 478 bultos", "Cerrar sin avisar, porque 2 bultos son pocos", "Una diferencia se registra e informa; no se altera el informe."),
        ("abc", "{F} Un compañero dice: «cerremos el contenedor aunque no revisemos el número de precinto: lo anotamos de memoria». ¿Qué respuesta es correcta?", "Es falso: cada punto de la lista se revisa y registra antes del cierre, sin anotar de memoria", "Es cierto: lo importante es el peso", "Es cierto, si la jefatura está de acuerdo", "La lista de verificación se completa mirando los datos reales."),
        ("=", "{F} ¿Cuántos pesos se ahorran con la alternativa manual respecto de la mecanizada?", "(3*10000+60000)*(480//60)-6*10000*(480//(6*8))", "Se resta el costo de la alternativa manual al de la mecanizada.", " pesos"),
    ],
    ctx=("abc", "En un turno de ejemplo, una persona propone saltarse la revisión de la lista de cierre «para ganar tiempo, porque el plazo aprieta». ¿Qué respondes?", "Que la lista se revisa completa y que, si el plazo no alcanza, se informa y se reprograma", "Que se salta, porque el plazo manda", "Que se marca como revisada y se verifica después", "Marcar sin revisar falsea el registro y deja pasar errores."),
    sc=[
        ("En Operaciones Portuarias: ¿cómo se calculan las horas de una alternativa?", "Dividiendo los bultos entre su rendimiento por hora", "El rendimiento dice cuántos bultos se mueven cada hora."),
        ("¿Qué alternativa conviene si varias cumplen el plazo?", "La de menor costo", "Entre las que cumplen el plazo, se prefiere la más barata."),
        ("¿Qué se hace si los bultos contados no coinciden con el informe?", "Se registra la diferencia y se informa", "No se cambia el informe para que cuadre."),
    ],
    op=("Hay que consolidar 360 bultos. Alternativa A (manual): 5 personas que hacen 6 bultos por persona por hora. Alternativa B (mecanizada, con equipo que opera solo personal autorizado): 2 personas y un rendimiento total de 45 bultos por hora. Costo de ejemplo: $10.000 por persona por hora; el equipo de B cuesta $45.000 por hora. Plazo: 10 horas. Escribe (a) las horas de A, (b) las horas de B, (c) qué alternativa cumple el plazo, (d) el costo de la que cumple.",
        "(a) A: 5 × 6 = 30 bultos por hora; 360 ÷ 30 = 12 horas. (b) B: 360 ÷ 45 = 8 horas. (c) Solo B cumple el plazo de 10 horas. (d) B cuesta (2 × 10.000 + 45.000) × 8 = 65.000 × 8 = $520.000.",
        ["calcula las horas de A", "calcula las horas de B", "compara con el plazo", "calcula el costo con personas y equipo"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo del equipo", "comparar el costo sin mirar el plazo", "no multiplicar el costo por las horas"],
        "Pregunta: «¿qué alternativa tarda menos de 10 horas?». Si no responde, pídele que revise sus cálculos de horas."),
    reinforce="Inventa dos alternativas de consolidación con distinto número de personas y calcula cuál cumple un plazo que elijas.",
    extend="Explica con un ejemplo un riesgo de la consolidación manual y uno de la mecanizada.",
)
