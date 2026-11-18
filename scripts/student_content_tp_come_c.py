"""Construcciones Metálicas TP 3.º y 4.º medio: OAE-07 (protección contra la corrosión), OAE-08 (residuos y desechos) y OAE-09 (cálculo y cubicación de materiales). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_come_common import AVISO, EMER, build

O7 = "TP-COME-3y4-OAE-07"
O8 = "TP-COME-3y4-OAE-08"
O9 = "TP-COME-3y4-OAE-09"

# ============================================================ OAE-07, clase 1
F = ("Ficha 27 (caso de ejemplo, inventado). La sección de pintura de «Estructuras Demo» tiene 6 personas. Productos: anticorrosivo y esmalte, ambos con solvente. "
     "Peligros anotados: vapores nocivos, inflamabilidad, contacto con la piel y los ojos, trabajo en altura al pintar estructuras grandes y residuos de pintura. "
     "Inventario: 12 envases de anticorrosivo y 8 de esmalte, de 4 litros cada uno. Capacidad máxima del almacén de pinturas de ejemplo: 30 envases.")
build(
    O7, 1, F,
    use="Aprenderé qué es la corrosión, por qué se protege el acero y qué peligros tienen las pinturas y los anticorrosivos, y cómo se leen la hoja de datos de seguridad y los rótulos.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé multiplicar, sumar y dividir.", "Sé que una tarea de riesgo exige autorización."],
    explain=[
        "La corrosión es el deterioro del acero por la acción de la humedad y el oxígeno, que forman óxido. Para proteger una construcción metálica se usan anticorrosivos, pinturas y otros recubrimientos, que se aplican según una especificación del proyecto. Este cuaderno no enseña a preparar superficies ni a pintar: enseña conceptos, documentos y reglas de seguridad.",
        "Los productos tienen peligros: muchos son inflamables, es decir, pueden encenderse con una chispa o una llama; sus vapores pueden causar mareo o daño al respirarlos; y pueden irritar la piel y los ojos. Cada producto trae una hoja de datos de seguridad (HDS), un documento del fabricante que indica sus peligros, cómo almacenarlo, qué EPP usar y qué hacer ante un accidente. El envase lleva un rótulo con el nombre y los pictogramas de peligro. Las medidas se ordenan por la jerarquía: sustituir un producto con solvente por otro de menor peligro cuando la especificación lo permita, ventilar y extraer vapores (ingeniería), reglas de almacenamiento y permisos (administrativos) y protección respiratoria, guantes y lentes (EPP).",
        f"Nunca se pasa un producto a otro envase sin rótulo ni se almacena abierto o junto a fuentes de calor. La norma vigente y la HDS mandan, y las tareas las hace personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("corrosión", "deterioro del acero por la humedad y el oxígeno"), ("anticorrosivo", "producto que protege el acero contra la corrosión"), ("HDS", "hoja de datos de seguridad del fabricante, con peligros, almacenamiento y EPP"), ("rótulo", "etiqueta del envase con el nombre y los pictogramas de peligro"), ("inflamable", "que puede encenderse con una chispa o una llama"), ("ventilación", "renovación del aire para retirar vapores")],
    worked=[
        ("Contar envases", "Una bodega de ejemplo guarda 9 envases de un producto y 6 de otro. ¿Cuántos envases son?", ["Se suman los envases de los dos productos.", "9 más 6 son 15."], "15 envases"),
        ("Clasificar un control", "Un taller de ejemplo cambia un producto con solvente por otro de base agua, que la especificación acepta. ¿Qué nivel de la jerarquía es?", ["El producto nuevo tiene menos peligro.", "Reemplazar por algo menos peligroso es sustituir."], "Sustitución"),
    ],
    mistakes=[("Pasar un producto a una botella de bebida sin rótulo «para usarlo más cómodo».", "Se pierde la información de peligro y alguien puede confundirlo con una bebida.", "Mantén el producto en su envase original rotulado."),
              ("Creer que si el producto huele poco no hace falta protección respiratoria.", "Los vapores nocivos pueden no oler; la protección la fija la HDS.", "Sigue la HDS y las instrucciones de la persona responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es la corrosión?", "El deterioro del acero por la humedad y el oxígeno, que forman óxido", "La deformación del acero por el peso", "El desgaste del acero por el roce", "La corrosión es una reacción química con humedad y oxígeno, no un efecto mecánico."),
        ("abc", "En Construcciones Metálicas: ¿qué es una hoja de datos de seguridad (HDS)?", "Un documento del fabricante con los peligros del producto, su almacenamiento y los EPP", "Un documento del taller con la lista de piezas", "Una receta para preparar el producto", "La HDS informa los peligros y las medidas; no es una receta ni una lista de piezas."),
        ("abc", "En Construcciones Metálicas: ¿qué significa que un producto sea inflamable?", "Que puede encenderse con una chispa o una llama", "Que se congela con facilidad", "Que solo daña la piel al tocarla", "Inflamable se refiere al riesgo de incendio."),
        ("=", "{F} ¿Cuántos envases de pintura hay en el inventario?", "12+8", "Se suman los envases de anticorrosivo y de esmalte.", " envases"),
        ("=", "{F} ¿Cuántos litros hay en total, con 4 litros por envase?", "(12+8)*4", "Se multiplica el total de envases por los litros de cada uno.", " litros"),
        ("=", "{F} ¿Cuántos envases más caben en el almacén antes de llegar a su capacidad?", "30-12-8", "Se resta el inventario a la capacidad máxima.", " envases"),
        ("abc", "{F} Se instala una extracción que retira los vapores desde donde se producen. ¿Qué tipo de control es?", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque ordena una conducta", "EPP, porque protege a una persona", "La extracción actúa sobre el peligro en su origen."),
        ("abc", "{F} El taller cuelga junto al almacén un cartel de «prohibido encender fuego» y exige un permiso para abrir envases. ¿Qué tipo de control es?", "Administrativo, porque ordena una conducta mediante señales y permisos", "De ingeniería, porque está en el almacén", "EPP, porque protege a las personas", "Un cartel y un permiso ordenan conductas; no cambian físicamente el lugar ni protegen a una sola persona."),
        ("abc", "{F} Un compañero quiere pasar pintura de un envase grande a una botella de bebida sin rótulo para usarla más cómodo. ¿Qué corresponde?", "No hacerlo: se pierde el rótulo y puede confundirse con una bebida", "Hacerlo si escribe el nombre a mano", "Hacerlo si es poca cantidad", "Un envase sin rótulo oficial puede causar una intoxicación por confusión."),
        ("abc", "Durante una visita de ejemplo, se derrama solvente cerca de una fuente de calor. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a secar el derrame con ropa", "Esperar a que se evapore solo", "Un derrame inflamable puede encenderse; se avisa a quienes están capacitados."),
        ("abc", "{F} ¿Por qué la HDS se consulta antes de usar un producto y no después?", "Porque indica los peligros y las medidas que hay que conocer antes de abrir el envase", "Porque después ya venció", "Porque solo se lee si hay un accidente", "La información preventiva sirve antes de exponerse al peligro."),
        ("=", "{F} Si se gastan 5 envases por semana, ¿cuántas semanas alcanzan los 20 envases del inventario?", "20//5", "Se divide el inventario entre el gasto semanal.", " semanas"),
        ("abc", "{F} Un joven en práctica dice que ya sabe pintar estructuras porque vio cómo lo hace su tío. ¿Qué corresponde?", "Ver no lo habilita: la tarea exige formación, autorización y seguir la HDS y la norma vigente", "Puede hacerlo si usa mascarilla", "Puede hacerlo si es una pieza pequeña", "Ni la observación ni el EPP reemplazan la formación y la autorización."),
    ],
    ctx=("abc", "El jefe de la sección de ejemplo te pide guardar los envases abiertos cerca del calefactor «para que no se enfríen». ¿Qué respondes?", "Que no: la HDS pide almacenarlos cerrados y lejos de fuentes de calor, y que lo consultarás con el responsable", "Que sí, si es por poco tiempo", "Que sí, si los tapas con una bolsa", "Un producto inflamable no se deja abierto cerca de una fuente de calor."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es un anticorrosivo?", "Un producto que protege el acero contra la corrosión", "Su función es retrasar el óxido."),
        ("¿Qué información trae el rótulo de un envase?", "El nombre del producto y sus pictogramas de peligro", "El rótulo identifica el contenido y avisa del peligro."),
        ("¿Dónde se consultan los peligros de un producto?", "En su hoja de datos de seguridad", "La HDS es el documento del fabricante."),
    ],
    op=("Caso de ejemplo: una bodega de otro taller guarda 14 envases de anticorrosivo y 10 de esmalte, de 5 litros cada uno, con una capacidad máxima de 30 envases. Un compañero quiere quitar el rótulo de un envase porque quedó manchado. Escribe (a) cuántos envases hay, (b) cuántos litros son, (c) cuántos envases más caben, (d) qué le respondes al compañero.",
        "(a) 14 + 10 = 24 envases. (b) 24 × 5 = 120 litros. (c) 30 − 24 = 6 envases. (d) Que el rótulo no se quita ni se cambia, porque identifica el producto y avisa su peligro, y que consulte con el responsable por uno nuevo.",
        ["suma los envases", "calcula los litros", "calcula la capacidad restante", "responde con la regla de la HDS"],
        ["hoja con las cuatro respuestas"],
        ["olvidar multiplicar por los litros", "restar mal la capacidad", "aceptar quitar el rótulo"],
        "Pregunta: «¿qué se pierde si el envase queda sin rótulo?». Si no responde, pídele que relea qué trae el rótulo."),
    reinforce="Escribe tres peligros de las pinturas con solvente y un control para cada uno, indicando su nivel de la jerarquía.",
    extend="Explica con un ejemplo por qué el rótulo de un envase no debe quitarse ni cambiarse.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 28 (especificación de ejemplo, inventada) de una baranda de acero. Sistema de tres capas, con el espesor seco de cada una en micrones (µm; 1.000 µm son 1 mm): anticorrosivo, 60 µm; intermedia, 80 µm; terminación, 40 µm. "
     "Espesor total mínimo exigido: 170 µm. Preparación: limpieza de superficie al grado «L2», convención de ejemplo que fija la especificación. Las condiciones de humedad y temperatura para aplicar constan en la hoja técnica del producto. "
     "Lectura de ejemplo del inspector en una baranda: 168 µm.")
build(
    O7, 2, F,
    use="Aprenderé el vocabulario de los sistemas de protección: preparación de superficie, capas, galvanizado, espesor seco y hoja técnica, y a verificar un espesor total en papel.",
    prior=["Sé qué es la corrosión y una HDS.", "Sé sumar números enteros.", "Sé qué es una tolerancia y un registro."],
    explain=[
        "Un sistema de protección es el conjunto de capas que protegen una superficie de acero. Antes de pintar, la superficie se limpia hasta un grado de limpieza que fija la especificación. Luego se aplican capas: la anticorrosiva, que va directamente sobre el acero; la intermedia, que aumenta el espesor y la protección; y la de terminación, que protege de la intemperie y da el acabado. Otra protección es el galvanizado, un recubrimiento de zinc sobre el acero. Aquí solo se aprende qué es cada cosa, no cómo se aplica.",
        "El espesor de película seca (EPS) es el grosor de la capa una vez seca, y se mide en micrones; 1.000 micrones son 1 milímetro. El espesor total de un sistema es la suma del espesor de cada capa, y debe alcanzar el mínimo que pide la especificación. La hoja técnica del producto indica sus condiciones de uso, como el rango de humedad y temperatura, y el rendimiento. Las lecturas del espesor se registran tal como se miden, con un instrumento calibrado.",
        f"Si el espesor medido no alcanza lo exigido, se registra como no conformidad y el responsable decide la corrección. Aplicar el sistema lo hace personal formado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("capa anticorrosiva", "capa que va directamente sobre el acero"), ("capa de terminación", "última capa, que protege de la intemperie y da el acabado"), ("galvanizado", "recubrimiento de zinc que protege el acero"), ("espesor de película seca", "grosor de la capa una vez seca, medido en micrones"), ("micrón (µm)", "milésima parte de un milímetro"), ("hoja técnica", "documento del fabricante con condiciones de uso y rendimiento")],
    worked=[
        ("Espesor total", "Un sistema de ejemplo tiene capas secas de 45 µm, 85 µm y 25 µm. ¿Cuál es el espesor total?", ["Se suman los espesores de las tres capas.", "45 más 85 más 25 son 155."], "155 µm"),
        ("Comparar con el mínimo", "El mínimo exigido es 150 µm y el sistema de ejemplo mide 155 µm. ¿Cumple?", ["Se compara el total con el mínimo.", "155 es mayor que 150."], "Sí, cumple"),
    ],
    mistakes=[("Omitir una capa porque «la de terminación cubre igual».", "Cada capa cumple una función y el sistema lo fija la especificación.", "Aplica todas las capas que pide la especificación."),
              ("Anotar el mínimo exigido en lugar del valor medido cuando este queda justo debajo.", "Se falsea el registro y se oculta una no conformidad.", "Anota el valor real e informa al responsable.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es la capa de terminación de un sistema de pintura?", "La última capa, que protege de la intemperie y da el acabado", "La primera capa, que va directamente sobre el acero", "La capa que se aplica antes de limpiar", "La terminación cierra el sistema; la anticorrosiva va primero."),
        ("abc", "En Construcciones Metálicas: ¿qué es el galvanizado?", "Un recubrimiento de zinc que protege el acero", "Una pintura de color gris", "Un tipo de unión por soldadura", "El galvanizado es zinc sobre el acero, no una pintura ni una unión."),
        ("abc", "En Construcciones Metálicas: ¿qué es el espesor de película seca?", "El grosor de la capa de pintura una vez seca, medido en micrones", "El grosor del envase de pintura", "El tiempo que tarda la pintura en secar", "El espesor mide grosor, no duración."),
        ("=", "{F} ¿Cuántos micrones suman las tres capas del sistema?", "60+80+40", "Se suman los espesores de las tres capas.", " µm"),
        ("abc", "{F} ¿Cumple el sistema de la ficha el espesor total mínimo de 170 µm?", "Sí, porque el total de 180 µm supera los 170 µm", "No, porque cada capa debe medir 170 µm", "No se puede saber sin pintar", "El mínimo se compara con el total del sistema, no con cada capa."),
        ("=", "{F} ¿Cuántos micrones sobran respecto del mínimo exigido?", "60+80+40-170", "Se resta el mínimo al espesor total del sistema.", " µm"),
        ("abc", "{F} Un compañero propone omitir la capa intermedia porque «la de terminación cubre igual». ¿Qué corresponde?", "No omitirla: el sistema lo fija la especificación y cada capa cumple una función", "Omitirla si se ve bien", "Omitirla si el cliente no mira", "La omisión de una capa puede dejar al acero sin la protección prevista."),
        ("=", "{F} Si la capa de terminación quedara en 20 µm en vez de 40, ¿cuántos micrones sumaría el sistema?", "60+80+20", "Se suman las capas con el nuevo valor.", " µm"),
        ("abc", "{F} Con ese total, que no alcanza el mínimo, ¿qué corresponde?", "Registrar la no conformidad y consultar al responsable la corrección", "Aceptarlo, porque está cerca del mínimo", "Anotar 180 en la planilla para que cuadre", "Un valor bajo el mínimo se registra y el responsable decide."),
        ("abc", "{F} ¿Por qué influye la preparación de la superficie en la duración de la pintura?", "Porque una superficie sucia u oxidada impide que el recubrimiento se adhiera bien y se desprende antes", "Porque la limpieza cambia el color de la pintura", "Porque la pintura solo se pega a superficies calientes", "La adherencia depende del estado de la superficie."),
        ("abc", "{F} ¿Dónde constan las condiciones de humedad y temperatura para aplicar un producto?", "En la hoja técnica del producto y en la especificación del proyecto", "En el rótulo de la lámina", "En la pauta de mantenimiento", "La hoja técnica del fabricante fija las condiciones de uso."),
        ("=", "{F} Una baranda de otro proyecto de ejemplo lleva dos capas, de 75 µm y 95 µm. ¿Cuántos micrones suman?", "75+95", "Se suman los espesores de las dos capas.", " µm"),
        ("abc", "{F} El inspector mide 168 µm en la baranda y el jefe pide anotar 170 porque «es casi lo mismo». ¿Qué corresponde?", "Registrar 168 µm, que no alcanza el mínimo, e informar al responsable", "Anotar 170 µm", "Anotar 169 µm para no exagerar", "El registro debe reflejar el valor medido."),
    ],
    ctx=("abc", "Una compañera ve que en el registro de ejemplo falta la lectura de espesor de una baranda ya entregada y propone «completarla» con el valor mínimo exigido. ¿Qué respondes?", "Que no se inventa una lectura: se informa la falta de registro al responsable", "Que sí, porque seguro cumple", "Que sí, si nadie lo revisa", "Un registro con datos inventados no sirve como evidencia de calidad."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el espesor total de un sistema?", "Sumando el espesor de cada capa", "Cada capa aporta su espesor al total."),
        ("¿Cuántos micrones tiene un milímetro?", "1.000 micrones", "El micrón es la milésima parte de un milímetro."),
        ("¿Qué documento del fabricante da las condiciones de uso de un producto?", "La hoja técnica", "Allí figuran los rangos de aplicación y el rendimiento."),
    ],
    op=("Especificación de ejemplo: sistema de dos capas, anticorrosivo de 70 µm y terminación de 60 µm; mínimo exigido 125 µm. Lectura del inspector: 118 µm. Escribe (a) el espesor total teórico del sistema, (b) si cumple el mínimo, (c) si la lectura cumple y qué haces, (d) por qué no se omite una capa.",
        "(a) 70 + 60 = 130 µm. (b) Cumple: 130 µm supera los 125 µm. (c) No cumple: 118 µm es menor que 125 µm; se registra como no conformidad e informa al responsable. (d) Porque cada capa cumple una función y el sistema lo fija la especificación.",
        ["suma las capas", "compara con el mínimo", "evalúa la lectura", "explica por qué no se omite una capa"],
        ["hoja con las cuatro respuestas"],
        ["sumar mal los espesores", "aceptar una lectura bajo el mínimo", "omitir una capa"],
        "Pregunta: «¿la lectura de 118 µm alcanza los 125 µm?». Si responde que sí, pídele que compare ambos números."),
    reinforce="Inventa un sistema de tres capas con sus espesores y calcula su total.",
    extend="Explica con un ejemplo por qué una pintura gruesa sobre una superficie mal preparada puede fallar.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 29 (hoja de datos de seguridad de ejemplo, inventada) del producto «Pintura Demo A». Sección 2, peligros: líquido y vapores inflamables; irritante para la piel y los ojos; los vapores pueden causar mareo. Pictogramas: llama (inflamable) y signo de exclamación (irritante). "
     "Sección 4, primeros pasos: ante contacto con los ojos o ingestión, avisar a un adulto responsable y buscar atención médica de inmediato. Sección 7, almacenamiento: lugar ventilado y fresco, lejos de fuentes de calor, con el envase cerrado. "
     "Sección 8, protección: guantes, lentes y protección respiratoria indicados por el fabricante. Sección 13, eliminación: como residuo según la norma vigente. Almacén de ejemplo: máximo 24 envases; hay 18.")
build(
    O7, 3, F,
    use="Aprenderé a leer en papel una hoja de datos de seguridad, a encontrar peligros, almacenamiento, protección y eliminación, y a decidir qué hacer ante una situación del caso.",
    prior=["Sé qué es una HDS y un rótulo.", "Sé sumar, restar y calcular porcentajes.", "Sé qué es un EPP."],
    explain=[
        "Una hoja de datos de seguridad (HDS) se divide en secciones numeradas para encontrar rápido lo que se necesita. En la HDS de ejemplo, la sección 2 informa los peligros, la 4 los primeros pasos ante un accidente, la 7 el almacenamiento, la 8 la protección que se debe usar y la 13 la eliminación. Los pictogramas son dibujos de peligro: una llama indica que el producto es inflamable y un signo de exclamación indica que irrita.",
        "Leer la HDS es la primera acción preventiva: antes de abrir un envase se sabe cómo guardarlo y qué protección corresponde. Lo que dice la HDS manda por sobre el olor, la costumbre o la opinión de un compañero. Ante un accidente, la conducta es no acercarse a la zona de riesgo si no se está capacitado, avisar a un adulto responsable y a emergencias, y no dar nada a la persona por cuenta propia.",
        f"Los restos de producto y los envases son residuos que se tratan según la norma vigente. Este cuaderno no entrega indicaciones médicas ni de manejo. {EMER} {AVISO}",
    ],
    vocab=[("sección de una HDS", "apartado numerado de la hoja con un tipo de información"), ("pictograma", "dibujo que indica un tipo de peligro"), ("almacenamiento", "forma de guardar un producto, según la HDS"), ("eliminación", "destino final de los restos, según la norma vigente")],
    worked=[
        ("Buscar una sección", "En la HDS de ejemplo de otro producto, ¿qué sección miras para saber dónde guardarlo?", ["El lugar de guardado se llama almacenamiento.", "Esa información está en la sección 7."], "La sección 7"),
        ("Capacidad restante", "Un almacén de ejemplo admite 40 envases y tiene 33. ¿Cuántos más caben?", ["Se resta lo que hay a la capacidad.", "40 menos 33 son 7."], "7 envases"),
    ],
    mistakes=[("Decidir qué protección usar por el olor del producto.", "Los vapores nocivos pueden no oler y el olor no mide el peligro.", "Sigue lo que indica la HDS en su sección de protección."),
              ("Dar algo de beber o inducir algo a una persona intoxicada por cuenta propia.", "Sin formación se puede agravar el daño.", "Avisa a un adulto responsable y a emergencias.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué sección de la HDS de ejemplo informa los peligros del producto?", "La sección 2", "La sección 7", "La sección 13", "La sección 2 informa peligros; la 7 es almacenamiento y la 13 eliminación."),
        ("abc", "En Construcciones Metálicas: ¿qué sección de la HDS de ejemplo indica cómo almacenar el producto?", "La sección 7", "La sección 4", "La sección 8", "El almacenamiento está en la sección 7; la 4 es de primeros pasos."),
        ("abc", "En Construcciones Metálicas: ¿qué indica el pictograma de una llama?", "Que el producto es inflamable", "Que el producto se congela", "Que el producto es seguro al tacto", "La llama señala riesgo de incendio."),
        ("abc", "{F} ¿Qué dice la HDS sobre el almacenamiento de «Pintura Demo A»?", "Guardarla en un lugar ventilado y fresco, lejos del calor y con el envase cerrado", "Guardarla abierta para que se airee", "Guardarla junto al calefactor", "La sección 7 pide un lugar ventilado, fresco, lejos del calor y con el envase cerrado."),
        ("abc", "{F} Un envase se deja abierto junto a un calefactor. ¿Qué incumple?", "La sección 7: debe almacenarse cerrado y lejos de fuentes de calor", "La sección 13: debe eliminarse", "Ninguna, porque no está en uso", "El producto es inflamable y su almacenamiento tiene reglas escritas."),
        ("abc", "{F} Una persona se marea tras respirar los vapores del producto. ¿Qué corresponde según las reglas generales?", "Avisar a un adulto responsable y a emergencias, sin darle nada por cuenta propia", "Darle agua con azúcar", "Dejarla sola hasta que se le pase", "Sin formación no se dan indicaciones médicas; se avisa a quienes pueden actuar."),
        ("abc", "{F} ¿Dónde se indica cómo eliminar los restos del producto?", "En la sección 13, como residuo según la norma vigente", "En la sección 2", "En el pictograma de llama", "La eliminación tiene su propia sección en la HDS."),
        ("=", "{F} ¿Cuántos envases más caben en el almacén de ejemplo?", "24-18", "Se resta lo que hay a la capacidad máxima.", " envases"),
        ("=", "{F} ¿Qué porcentaje de la capacidad del almacén está ocupado?", "18*100//24", "Se multiplica por 100 lo que hay y se divide entre la capacidad.", " %"),
        ("abc", "{F} Un compañero dice que, como el producto «huele poco», no necesita protección respiratoria. ¿Qué corresponde?", "Seguir lo que indica la HDS y no el olor: la protección la fija el documento", "Tiene razón: sin olor no hay peligro", "Usar la mascarilla solo si huele fuerte", "El olor no mide el peligro; la sección 8 fija la protección."),
        ("abc", "En Construcciones Metálicas: ¿por qué la HDS tiene secciones numeradas?", "Para encontrar rápido la información que se necesita ante una duda o un incidente", "Para que ocupe más páginas", "Para que solo la entienda el fabricante", "Una estructura fija permite hallar rápido peligros, almacenamiento o eliminación."),
        ("=", "{F} Llegan 3 cajas con 2 envases cada una. ¿Cuántos envases habrá en el almacén en total?", "18+3*2", "Se suman los envases nuevos a los que ya había.", " envases"),
        ("abc", "{F} Con el almacén lleno, llegan más envases. ¿Qué corresponde?", "No guardarlos allí sin consultar, porque se supera el máximo; se pide otro lugar al responsable", "Apilarlos en el pasillo", "Abrir algunos envases para ahorrar espacio", "Superar el máximo o bloquear pasillos crea nuevos riesgos."),
    ],
    ctx=("abc", "Alguien derramó un poco de «Pintura Demo A» cerca de una estufa de ejemplo. Un compañero propone secarla con trapos «rápido, antes de que se note». ¿Qué respondes?", "Que no se acerquen: avisar a un adulto responsable y a emergencias, porque el producto es inflamable", "Que lo seque rápido", "Que espere a que se evapore", "Un derrame inflamable cerca del calor puede encenderse; no se improvisa."),
    sc=[
        ("En Construcciones Metálicas: ¿qué sección de la HDS de ejemplo indica la protección que se debe usar?", "La sección 8", "La protección indicada por el fabricante está en esa sección."),
        ("¿Qué indica un signo de exclamación como pictograma?", "Que el producto es irritante", "El signo de exclamación avisa de irritación."),
        ("¿Qué manda por sobre el olor del producto?", "Lo que dice la HDS", "El olor no mide el peligro."),
    ],
    op=("HDS de ejemplo del producto «Esmalte Demo B»: peligros: inflamable e irritante para los ojos; almacenamiento: lugar ventilado, cerrado y lejos del calor; eliminación: como residuo según la norma vigente. El almacén admite 30 envases y tiene 24. Escribe (a) qué pictogramas esperarías, (b) cómo se almacena, (c) cuántos envases más caben y qué porcentaje está ocupado, (d) qué haces si el producto salpica los ojos de un compañero.",
        "(a) Una llama (inflamable) y un signo de exclamación (irritante). (b) En un lugar ventilado, con el envase cerrado y lejos del calor. (c) 30 − 24 = 6 envases; 24 × 100 ÷ 30 = 80 %. (d) Aviso de inmediato a un adulto responsable y a emergencias, sin tratarlo por cuenta propia.",
        ["nombra los pictogramas", "describe el almacenamiento", "calcula la capacidad", "indica la conducta ante un accidente"],
        ["hoja con las cuatro respuestas"],
        ["decir que se guarda abierto", "restar mal la capacidad", "intentar tratar al compañero por cuenta propia"],
        "Pregunta: «¿qué haces con el compañero salpicado?». Si responde tratarlo tú, pídele que relea la conducta ante un accidente."),
    reinforce="Inventa una HDS breve con tres secciones y escribe una pregunta que se responda con cada una.",
    extend="Explica con un ejemplo por qué una HDS debe estar disponible en el lugar donde se guarda el producto.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 30 (datos de ejemplo, inventados). Baranda: superficie total a pintar, 96 m². Sistema de tres capas con los rendimientos de la hoja técnica: anticorrosivo, 8 m² por litro; intermedia, 12 m² por litro; terminación, 16 m² por litro. "
     "Precios de ejemplo por litro: anticorrosivo $9.000; intermedia $10.000; terminación $12.000. Merma de ejemplo: 1 litro adicional por producto. Rendimiento = superficie que cubre un litro.")
build(
    O7, 4, F,
    use="Aprenderé a calcular en papel los litros y el costo de un sistema de pintura a partir de la superficie y los rendimientos, y a incluir la merma.",
    prior=["Sé qué es un sistema de capas.", "Sé dividir números enteros exactos.", "Sé multiplicar por precios."],
    explain=[
        "El rendimiento de un producto es la superficie que cubre un litro, según su hoja técnica. Los litros que se necesitan de cada capa son la superficie total dividida entre el rendimiento de esa capa. Como cada capa tiene su propio rendimiento, cada una necesita una cantidad distinta de litros. El costo de cada capa es los litros por el precio por litro, y el costo del sistema es la suma de las tres.",
        "La merma es la parte que se pierde o sobra por uso y por pérdidas, y se suma al cálculo para no quedarse corto: en esta clase es 1 litro adicional por producto. Comprar de menos obliga a detener el trabajo y puede dejar el espesor bajo lo exigido, y comprar de más gasta dinero y obliga a almacenar producto inflamable. Los cálculos se hacen con superficies exactas dadas en el plano y se dejan en una planilla.",
        f"Es una estimación de planilla con valores de ejemplo; los rendimientos reales los fija el fabricante y la compra la decide el responsable. Aquí no se enseña a pintar. {EMER} {AVISO}",
    ],
    vocab=[("rendimiento", "superficie que cubre un litro de producto, según la hoja técnica"), ("merma", "parte que se pierde o sobra y se suma al cálculo"), ("superficie a pintar", "área total que debe recibir el sistema, en m²"), ("costo del sistema", "suma del costo de cada capa")],
    worked=[
        ("Litros de una capa", "Una capa de ejemplo rinde 20 m² por litro y la superficie es de 80 m². ¿Cuántos litros se necesitan?", ["Se divide la superficie entre el rendimiento.", "80 entre 20 son 4."], "4 litros"),
        ("Costo de una capa", "Esos 4 litros cuestan $7.000 el litro. ¿Cuánto cuesta la capa?", ["Se multiplican los litros por el precio.", "4 por 7.000 son 28.000."], "$28.000"),
    ],
    mistakes=[("Calcular los litros de todo el sistema con el rendimiento de una sola capa.", "Cada capa tiene su propio rendimiento y su propia cantidad.", "Calcula una capa a la vez con su rendimiento."),
              ("Olvidar la merma y quedarse corto de producto.", "Faltar producto detiene el trabajo y puede dejar el espesor bajo lo exigido.", "Suma la merma que fija la planilla.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el rendimiento de una pintura?", "La superficie que cubre un litro de producto, según la hoja técnica", "El tiempo que tarda en secar", "La cantidad de capas que lleva el sistema", "El rendimiento relaciona superficie y litros."),
        ("abc", "En Construcciones Metálicas: ¿qué es la merma de un producto?", "La parte que se pierde o sobra, que se suma al cálculo", "El precio de un litro", "El color final que queda", "La merma se considera para no quedarse corto de producto."),
        ("=", "{F} ¿Cuántos litros de anticorrosivo se necesitan para la superficie?", "96//8", "Se divide la superficie entre el rendimiento de esa capa.", " litros"),
        ("=", "{F} ¿Cuántos litros de la capa intermedia se necesitan?", "96//12", "Se divide la superficie entre el rendimiento de esa capa.", " litros"),
        ("=", "{F} ¿Cuántos litros de la capa de terminación se necesitan?", "96//16", "Se divide la superficie entre el rendimiento de esa capa.", " litros"),
        ("=", "{F} ¿Cuántos litros suman las tres capas, sin merma?", "96//8+96//12+96//16", "Se suman los litros de cada capa.", " litros"),
        ("=", "{F} ¿Cuántos pesos cuesta el anticorrosivo que se necesita?", "(96//8)*9000", "Se multiplican los litros por el precio por litro.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el sistema completo, sin merma?", "(96//8)*9000+(96//12)*10000+(96//16)*12000", "Se suma el costo de cada capa.", " pesos"),
        ("=", "{F} Con la merma de 1 litro por producto, ¿cuántos litros se compran en total?", "96//8+96//12+96//16+3", "Se suman los litros y 1 litro de merma por cada uno de los tres productos.", " litros"),
        ("=", "{F} ¿Cuántos pesos cuesta el sistema completo con la merma?", "(96//8+1)*9000+(96//12+1)*10000+(96//16+1)*12000", "Se calcula cada capa con su litro de merma.", " pesos"),
        ("abc", "{F} Un compañero dice: «con 12 litros de anticorrosivo alcanza para todo el sistema». ¿Qué error cometió?", "Calculó el sistema como una sola capa; cada capa tiene su rendimiento y su cantidad", "Debió multiplicar los m² por el precio", "No cometió ningún error", "Los 12 litros solo cubren la capa anticorrosiva."),
        ("=", "{F} Si la superficie a pintar subiera a 144 m², ¿cuántos litros de anticorrosivo se necesitarían?", "144//8", "Se divide la nueva superficie entre el rendimiento.", " litros"),
        ("abc", "{F} El jefe pide reducir el costo comprando solo 10 litros de anticorrosivo «para ahorrar». ¿Qué corresponde?", "Explicar que con 10 litros no alcanza para la superficie y faltar producto obliga a detener el trabajo y deja el espesor bajo lo exigido", "Comprar 10 litros y pintar menos superficie sin avisar", "Comprar 10 litros y repartirlos igual en todo", "Comprar de menos solo traslada el problema al espesor y a los plazos."),
    ],
    ctx=("abc", "Al revisar la planilla de ejemplo de otra baranda, ves que usó el mismo rendimiento para las tres capas aunque la hoja técnica da tres valores distintos. ¿Qué haces?", "Avisar al responsable para que se rehaga el cálculo con el rendimiento de cada capa", "Dejarlo así, porque es parecido", "Cambiar solo la capa de terminación", "Un cálculo con rendimientos equivocados lleva a faltantes o excesos de producto."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calculan los litros de una capa?", "Superficie dividida entre el rendimiento de esa capa", "Cada capa tiene su propio rendimiento."),
        ("¿Cómo se calcula el costo de una capa?", "Litros por precio por litro", "El costo depende de cuánto se compra y de su precio."),
        ("¿Para qué se agrega merma?", "Para no quedarse corto de producto", "Si falta producto, el trabajo se detiene."),
    ],
    op=("Caso de ejemplo: una reja de 60 m² con dos capas: anticorrosivo (6 m² por litro, $8.000 el litro) y terminación (10 m² por litro, $11.000 el litro); merma de 1 litro adicional por producto. Escribe (a) los litros de cada capa, (b) los litros a comprar con merma, (c) el costo con merma, (d) qué haces si el rendimiento de la hoja técnica cambia.",
        "(a) Anticorrosivo: 60 ÷ 6 = 10 litros; terminación: 60 ÷ 10 = 6 litros. (b) 11 y 7 litros, es decir, 18 litros. (c) 11 × 8.000 + 7 × 11.000 = 88.000 + 77.000 = 165.000 pesos. (d) Rehago el cálculo con el rendimiento nuevo y lo informo al responsable.",
        ["calcula los litros de cada capa", "suma la merma", "calcula el costo", "indica qué hacer si cambia el rendimiento"],
        ["hoja con las cuatro respuestas"],
        ["usar un rendimiento único", "olvidar la merma", "no rehacer el cálculo"],
        "Pregunta: «¿cuántos litros de merma se agregan por producto?». Si responde 1 en total, pídele que relea la ficha."),
    reinforce="Inventa una superficie y dos rendimientos y calcula los litros de cada capa.",
    extend="Explica con un ejemplo por qué comprar de más también tiene riesgos.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 31 (caso de ejemplo, inventado). Residuos mensuales de «Estructuras Demo», en kilogramos de ejemplo: chatarra de acero, 900; viruta limpia de acero, 150; aceite usado, 60; envases con restos de pintura, 40; paños y guantes con solventes, 20; basura de oficina (papel y cartón), 30. "
     "El taller trata como residuos peligrosos el aceite usado, los envases con restos de pintura y los paños y guantes con solventes. Los demás residuos son no peligrosos y reciclables.")
build(
    O8, 1, F,
    use="Aprenderé qué es un residuo, cuáles son peligrosos, qué riesgos tienen los residuos de un taller y cómo se ordenan las opciones de manejo según la norma vigente.",
    prior=["Sé qué es un peligro, un riesgo y la jerarquía de controles.", "Sé calcular porcentajes.", "Sé que las tareas de riesgo exigen autorización."],
    explain=[
        "Un residuo es un material que se desecha. En un taller de construcciones metálicas hay chatarra, viruta, aceite usado, envases con restos de pintura, paños con solventes y basura común. Un residuo peligroso es el que tiene una propiedad peligrosa, como ser inflamable o tóxico, y exige un manejo y un destino especial según la norma vigente y las autoridades competentes. Los no peligrosos pueden reciclarse o eliminarse de forma común.",
        "Las opciones de manejo se ordenan en la jerarquía de residuos, de la preferida a la menos preferida: reducir, reutilizar, reciclar, valorizar (aprovechar el residuo como material o energía) y eliminar, que es la disposición final. La segregación consiste en separar los residuos por tipo, en contenedores rotulados; mezclar un peligroso con uno común contamina todo y encarece el manejo. Los riesgos son cortes con la chatarra, resbalones por aceite derramado, incendio de paños con solventes e intoxicación por vapores.",
        f"El taller que genera residuos es responsable de ellos hasta su destino final. Solo personal formado y autorizado maneja residuos peligrosos. {EMER} {AVISO}",
    ],
    vocab=[("residuo", "material que se desecha"), ("residuo peligroso", "residuo con una propiedad peligrosa que exige manejo y destino especial"), ("segregación", "separar los residuos por tipo en contenedores rotulados"), ("jerarquía de residuos", "orden de manejo: reducir, reutilizar, reciclar, valorizar y eliminar"), ("valorizar", "aprovechar un residuo como material o energía"), ("disposición final", "destino definitivo de un residuo que no se puede aprovechar")],
    worked=[
        ("Clasificar un residuo", "En otro taller de ejemplo, un tambor tiene restos de solvente usado. ¿Es un residuo peligroso o común?", ["El solvente es inflamable y puede ser tóxico.", "Un residuo con esas propiedades es peligroso."], "Peligroso"),
        ("Porcentaje de un residuo", "En otro taller de ejemplo, 80 kg de 400 kg son aceite usado. ¿Qué porcentaje es?", ["Se multiplican por 100 los kilogramos de aceite y se divide entre el total.", "80 por 100 son 8.000, y 8.000 entre 400 son 20."], "20 %"),
    ],
    mistakes=[("Mezclar un residuo peligroso con la basura común «para ahorrar contenedores».", "Se contamina todo y el residuo común pasa a requerir manejo especial.", "Segrega y rotula cada residuo en su contenedor."),
              ("Creer que todo lo pesado es peligroso.", "La peligrosidad depende de sus propiedades, no de su peso.", "Clasifica por la propiedad peligrosa, según la norma vigente.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es un residuo peligroso?", "Un residuo con una propiedad peligrosa, como inflamable o tóxico, que exige manejo especial", "Cualquier residuo muy pesado", "Cualquier residuo que huele mal", "La peligrosidad depende de las propiedades del residuo, no de su peso ni de su olor."),
        ("abc", "En Construcciones Metálicas: ¿qué es la segregación de residuos?", "Separarlos por tipo en contenedores rotulados", "Juntarlos todos en un solo contenedor", "Quemarlos para reducir su volumen", "Segregar es separar para manejar cada tipo según corresponde."),
        ("abc", "En Construcciones Metálicas: ¿cuál es el orden de la jerarquía de residuos, de la opción preferida a la menos preferida?", "Reducir, reutilizar, reciclar, valorizar y eliminar", "Eliminar, valorizar, reciclar, reutilizar y reducir", "Reciclar, eliminar, reducir, valorizar y reutilizar", "Lo mejor es generar menos residuos y lo último es eliminarlos."),
        ("=", "{F} ¿Cuántos kilogramos de residuos genera el taller al mes en total?", "900+150+60+40+20+30", "Se suman las masas de los seis tipos de residuo.", " kg"),
        ("abc", "{F} ¿Cuál de estos residuos de la ficha es peligroso por contener solventes?", "Los paños y guantes con solventes", "La basura de oficina", "La chatarra de acero", "Los solventes son inflamables; la chatarra y el papel no tienen esa propiedad."),
        ("abc", "{F} Una bandeja que retiene derrames bajo el contenedor de aceite usado es:", "Un control de ingeniería", "Un control administrativo", "Un EPP", "La bandeja es una barrera física que contiene el derrame sin depender de las personas."),
        ("=", "{F} ¿Qué porcentaje del total es chatarra de acero?", "900*100//1200", "Se multiplican por 100 los kilogramos de chatarra y se divide entre el total.", " %"),
        ("=", "{F} ¿Cuántos kilogramos de residuos peligrosos genera el taller al mes?", "60+40+20", "Se suman aceite usado, envases con restos de pintura y paños con solventes.", " kg"),
        ("abc", "{F} Se mezclan los paños con solventes con la basura de oficina «para ahorrar contenedores». ¿Qué corresponde?", "No hacerlo: se pierde la segregación y se contamina el residuo común", "Hacerlo si son pocos paños", "Hacerlo si se tapa el contenedor", "Mezclar un peligroso con uno común obliga a tratar todo como peligroso."),
        ("abc", "En una visita de ejemplo se derrama aceite junto a un tablero eléctrico. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a secarlo con trapos", "Esperar a que se seque solo", "Un derrame junto a electricidad es doblemente peligroso; se avisa a quienes pueden actuar."),
        ("abc", "{F} Cambiar el aceite por uno que dure más y así generar menos aceite usado corresponde a:", "Reducir, el primer nivel de la jerarquía de residuos", "Reciclar", "Eliminar", "Generar menos residuo es la opción preferida de la jerarquía."),
        ("=", "{F} Si se reciclan la chatarra, la viruta limpia y el papel y cartón de oficina, ¿qué porcentaje del total se recicla?", "(900+150+30)*100//1200", "Se suman los reciclables, se multiplican por 100 y se divide entre el total.", " %"),
        ("=", "{F} ¿Qué porcentaje del total es residuo peligroso?", "(60+40+20)*100//1200", "Se multiplican por 100 los kilogramos peligrosos y se divide entre el total.", " %"),
    ],
    ctx=("abc", "Un compañero de práctica propone botar al desagüe el aceite usado «porque son pocos litros». ¿Qué respondes?", "Que no: es un residuo peligroso que se segrega y entrega a una empresa autorizada según la norma vigente, y que avisarás al responsable", "Que sí, si lo diluye con agua", "Que sí, si lo hace de noche", "Un residuo peligroso no se descarta en el desagüe; su destino lo fija la norma."),
    sc=[
        ("En Construcciones Metálicas: ¿qué es valorizar un residuo?", "Aprovecharlo como material o energía", "Es una opción preferible a eliminarlo."),
        ("¿Qué se evita al segregar los residuos?", "Contaminar el residuo común con uno peligroso", "Cada tipo se maneja según su propiedad."),
        ("¿Quién es responsable de los residuos que genera un taller?", "El taller que los genera, hasta su destino final", "La responsabilidad no termina al sacarlos del taller."),
    ],
    op=("Caso de ejemplo: otro taller genera al mes 300 kg de chatarra, 100 kg de viruta limpia, 60 kg de aceite usado y 40 kg de paños con solventes. Escribe (a) el total en kilogramos, (b) cuántos kilogramos son peligrosos, (c) qué porcentaje del total son peligrosos, (d) por qué no se mezclan los peligrosos con la chatarra.",
        "(a) 300 + 100 + 60 + 40 = 500 kg. (b) 60 + 40 = 100 kg. (c) 100 × 100 ÷ 500 = 20 %. (d) Porque se contamina la chatarra, que se podía reciclar, y todo pasaría a requerir manejo especial.",
        ["suma el total", "identifica los peligrosos", "expresa el porcentaje", "explica la segregación"],
        ["hoja con las cuatro respuestas"],
        ["incluir la viruta limpia entre los peligrosos", "mezclar los residuos", "no explicar la contaminación"],
        "Pregunta: «¿qué pasa con la chatarra si se mezcla con aceite usado?». Si no responde, pídele que relea la segregación."),
    reinforce="Escribe una tabla con cuatro residuos de un taller y marca si cada uno es peligroso o común.",
    extend="Explica con un ejemplo por qué reducir es mejor que reciclar en la jerarquía de residuos.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 32 (rótulos y registros de ejemplo, inventados). Contenedores del taller: A (azul), metal limpio reciclable; B (rojo, con tapa y rótulo de peligro), residuos peligrosos; C (gris), residuos comunes. "
     "El acopio temporal es una zona señalizada y techada donde los residuos esperan su retiro. Retiros de residuos peligrosos del trimestre: mes 1, 40 kg; mes 2, 35 kg; mes 3, 45 kg. "
     "Cada retiro lo hace una empresa transportista autorizada y deja una guía de respaldo. Capacidad del contenedor B: 20 kg.")
build(
    O8, 2, F,
    use="Aprenderé los conceptos y documentos del manejo de residuos: rótulos, contenedores, acopio temporal, empresas autorizadas, guías y trazabilidad, y a leer un registro de retiros.",
    prior=["Sé qué es un residuo peligroso y la segregación.", "Sé sumar y dividir.", "Sé que un registro debe decir la verdad."],
    explain=[
        "El manejo de residuos usa contenedores distintos para cada tipo, con un rótulo que indica el residuo que contienen y su peligro, para evitar mezclas. Los residuos esperan su retiro en el acopio temporal, una zona señalizada y techada, con el piso en buen estado y acceso controlado. El retiro de residuos peligrosos lo hace una empresa transportista autorizada según la norma vigente, y su destino final también debe ser un lugar autorizado.",
        "La trazabilidad es poder seguir un residuo desde que se genera hasta su destino, con documentos. Cada retiro deja una guía de respaldo, que se guarda como prueba de que el residuo llegó donde correspondía. El registro de retiros anota fecha, tipo de residuo, masa, empresa y guía. Las masas se anotan tal como se pesaron: alterar un registro oculta información y falta a la norma.",
        f"Un residuo sin rótulo o desconocido no se manipula, no se huele ni se vierte: se avisa al responsable. {EMER} {AVISO}",
    ],
    vocab=[("rótulo de contenedor", "etiqueta que indica el residuo que contiene y su peligro"), ("acopio temporal", "zona señalizada donde los residuos esperan su retiro"), ("empresa transportista autorizada", "empresa habilitada por la norma vigente para retirar residuos"), ("guía de respaldo", "documento que prueba un retiro y permite seguir el residuo"), ("trazabilidad", "posibilidad de seguir un residuo desde que se genera hasta su destino")],
    worked=[
        ("Promedio mensual", "En un trimestre de ejemplo se retiraron 15, 55 y 80 kg de residuos. ¿Cuál es el promedio mensual?", ["Se suman los tres meses: 15 más 55 más 80 son 150.", "Se divide entre 3: 150 entre 3 son 50."], "50 kg"),
        ("Contenedores llenos", "Con un contenedor de 25 kg de capacidad, ¿cuántos contenedores llenos son 100 kg de ejemplo?", ["Se divide la masa entre la capacidad.", "100 entre 25 son 4."], "4 contenedores"),
    ],
    mistakes=[("Entregar residuos peligrosos a quien ofrece retirarlos «más barato» sin verificar su autorización.", "Si el destino no es autorizado, el taller sigue siendo responsable del daño.", "Contrata solo empresas autorizadas y guarda la guía."),
              ("Anotar en el registro una masa menor para que el mes «se vea mejor».", "El dato falso oculta información y falta a la norma.", "Registra la masa real pesada.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el acopio temporal de residuos?", "Una zona señalizada donde los residuos esperan su retiro", "El destino final de los residuos", "Un contenedor donde se mezclan todos los residuos", "El acopio es una espera controlada, no el destino ni una mezcla."),
        ("abc", "En Construcciones Metálicas: ¿qué es la trazabilidad de un residuo?", "Poder seguirlo desde que se genera hasta su destino, con documentos", "Pesarlo una vez al final del año", "Cambiarle el rótulo cuando se llena el contenedor", "La trazabilidad es el seguimiento documentado del residuo."),
        ("abc", "En Construcciones Metálicas: ¿para qué sirve el rótulo de un contenedor de residuos?", "Para indicar qué residuo contiene y su peligro, evitando mezclas", "Para decorar el contenedor", "Para saber quién lo compró", "El rótulo informa el contenido y el peligro."),
        ("abc", "{F} ¿En qué contenedor va la chatarra limpia?", "En el A, azul, de metal limpio reciclable", "En el B, rojo, de residuos peligrosos", "En el C, gris, de residuos comunes", "La chatarra limpia es reciclable y va al contenedor de metal limpio."),
        ("abc", "{F} ¿En qué contenedor va un paño empapado con solvente?", "En el B, rojo, de residuos peligrosos", "En el A, azul", "En el C, gris", "El solvente hace que el paño sea un residuo peligroso."),
        ("=", "{F} ¿Cuántos kilogramos de residuos peligrosos se retiraron en el trimestre?", "40+35+45", "Se suman los retiros de los tres meses.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos se retiraron en promedio por mes?", "(40+35+45)//3", "Se divide el total del trimestre entre los tres meses.", " kg"),
        ("=", "{F} ¿A cuántos contenedores B llenos equivale lo retirado en el trimestre?", "(40+35+45)//20", "Se divide el total entre la capacidad de cada contenedor.", " contenedores"),
        ("abc", "{F} ¿Qué documento deja la empresa transportista autorizada en cada retiro?", "Una guía de respaldo que permite seguir el residuo", "Un permiso de trabajo", "Una hoja de datos de seguridad", "La guía prueba el retiro; el permiso y la HDS cumplen otras funciones."),
        ("abc", "{F} Una empresa sin autorización ofrece retirar los residuos peligrosos más barato. ¿Qué corresponde?", "Rechazarla: el retiro lo hace solo una empresa autorizada y se consulta al responsable", "Aceptarla si el precio es menor", "Aceptarla si promete devolver una guía", "Un precio bajo no reemplaza la autorización exigida por la norma."),
        ("abc", "{F} ¿Por qué se guarda la guía de cada retiro?", "Porque prueba que el residuo llegó a su destino y permite demostrar el cumplimiento", "Porque la guía vence al mes", "Porque sirve para pintar el contenedor", "La guía es el respaldo documental de la trazabilidad."),
        ("=", "{F} Si en el mes 4 se retiran 35 kg más, ¿cuántos kilogramos suman los cuatro meses?", "40+35+45+35", "Se suma el nuevo retiro a los tres anteriores.", " kg"),
        ("abc", "{F} Un compañero propone anotar 30 kg en lugar de 45 kg en el mes 3 para que el mes se vea más bajo. ¿Qué corresponde?", "Registrar la masa real de 45 kg, porque alterar el registro oculta información y falta a la norma", "Anotar 30 kg si el jefe está de acuerdo", "Anotar 40 kg como promedio", "El registro debe reflejar lo pesado; no se ajusta por imagen."),
    ],
    ctx=("abc", "En el acopio encuentras un bidón sin rótulo con un líquido que nadie sabe qué es. ¿Qué haces?", "No manipularlo, avisar al responsable y esperar instrucciones", "Verterlo al desagüe", "Oler el contenido para identificarlo", "Un residuo desconocido puede ser peligroso; no se manipula ni se huele."),
    sc=[
        ("En Construcciones Metálicas: ¿qué hace una empresa transportista autorizada?", "Retira los residuos peligrosos según la norma vigente", "Solo una empresa habilitada puede hacerlo."),
        ("¿Qué anota un registro de retiros?", "Fecha, tipo, masa, empresa y guía", "Así queda la trazabilidad del residuo."),
        ("¿Qué se hace con un residuo sin rótulo?", "No se manipula y se avisa al responsable", "Podría ser peligroso y no se sabe."),
    ],
    op=("Registro de ejemplo de residuos peligrosos de otro taller: mes 1, 24 kg; mes 2, 36 kg; mes 3, 30 kg. Capacidad de cada contenedor rojo: 18 kg. Escribe (a) el total del trimestre, (b) el promedio mensual, (c) cuántos contenedores llenos equivalen al total, (d) qué datos anota cada línea del registro de retiros además de la masa.",
        "(a) 24 + 36 + 30 = 90 kg. (b) 90 ÷ 3 = 30 kg. (c) 90 ÷ 18 = 5 contenedores. (d) La fecha, el tipo de residuo, la empresa y la guía, para que quede la trazabilidad.",
        ["calcula el total", "calcula el promedio", "calcula los contenedores", "lista los datos del registro"],
        ["hoja con las cuatro respuestas"],
        ["dividir el promedio entre un número equivocado", "olvidar la guía en el registro", "alterar el registro"],
        "Pregunta: «¿qué documento prueba el retiro?». Si no responde, pídele que relea la guía de respaldo."),
    reinforce="Escribe tres columnas (fecha, residuo, masa) e inventa tres filas de un registro de retiros.",
    extend="Explica con un ejemplo por qué el taller sigue siendo responsable de un residuo que entregó a una empresa no autorizada.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 33 (datos de ejemplo, inventados). En un mes, «Estructuras Demo» vende 900 kg de chatarra limpia a una recicladora autorizada a $120 por kg y paga el retiro de 120 kg de residuos peligrosos a $1.500 por kg. "
     "Propuesta: reducir en 25 % los residuos peligrosos comprando la pintura según la cubicación y no en exceso. La recicladora paga mejor la chatarra limpia que la mezclada.")
build(
    O8, 3, F,
    use="Aprenderé a analizar en papel el balance de los residuos de un taller: ingresos por chatarra, costos de retiro, el efecto de reducir y por qué conviene segregar.",
    prior=["Sé qué es un residuo peligroso y la jerarquía de residuos.", "Sé calcular porcentajes y multiplicar por precios.", "Sé que un registro debe decir la verdad."],
    explain=[
        "Los residuos tienen costos e ingresos. La chatarra limpia se vende a una recicladora autorizada y produce un ingreso: los kilogramos por el precio por kilogramo. Los residuos peligrosos cuestan, porque su retiro por una empresa autorizada se paga: los kilogramos por el costo por kilogramo. Comparar ambos valores ayuda a decidir qué medida conviene primero, pero no reemplaza las exigencias de la norma vigente.",
        "Reducir los residuos peligrosos en su origen, por ejemplo comprando la pintura según lo calculado en la cubicación, baja el costo y también el riesgo para las personas y el ambiente. Para calcular un porcentaje de reducción se multiplica la masa por el porcentaje y se divide entre 100. Segregar bien tiene un beneficio directo: la chatarra limpia se vende mejor que la mezclada.",
        f"Los estados reales de los residuos se informan siempre: ocultar que la chatarra viene contaminada infringe la norma y puede causar riesgos. {EMER} {AVISO}",
    ],
    vocab=[("recicladora autorizada", "empresa habilitada para recibir y procesar un tipo de residuo"), ("ingreso", "dinero que se recibe, como la venta de chatarra"), ("costo de retiro", "dinero que se paga por retirar un residuo"), ("reducción en origen", "generar menos residuo desde el inicio")],
    worked=[
        ("Ingreso por chatarra", "Otro taller de ejemplo vende 300 kg de chatarra a $90 por kg. ¿Cuánto ingresa?", ["Se multiplican los kilogramos por el precio.", "300 por 90 son 27.000."], "$27.000"),
        ("Porcentaje de reducción", "Un taller de ejemplo reduce en 20 % sus 50 kg de residuos peligrosos. ¿Cuántos kilogramos menos son?", ["Se multiplica la masa por el porcentaje.", "50 por 20 son 1.000, y 1.000 entre 100 son 10."], "10 kg"),
    ],
    mistakes=[("Vender chatarra contaminada como si fuera limpia para ganar más.", "Oculta su estado real y puede causar riesgos y sanciones.", "Informa el estado real y segrega bien."),
              ("Decidir solo por el costo, sin considerar el riesgo.", "Un residuo peligroso mal manejado puede causar daño aunque ahorre dinero.", "Cumple primero la norma y luego compara costos.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es una recicladora autorizada?", "Una empresa habilitada por la norma vigente para recibir y procesar un tipo de residuo", "Cualquier persona que compre chatarra", "El área del taller donde se acopia la chatarra", "La autorización la exige la norma; no basta con comprar chatarra."),
        ("=", "{F} ¿Cuántos pesos ingresan al mes por la chatarra?", "900*120", "Se multiplican los kilogramos vendidos por el precio por kilogramo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta al mes el retiro de los residuos peligrosos?", "120*1500", "Se multiplican los kilogramos retirados por el costo por kilogramo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta el retiro de los peligrosos que lo que ingresa por la chatarra?", "120*1500-900*120", "Se resta el ingreso por chatarra al costo del retiro.", " pesos"),
        ("=", "{F} ¿Cuántos kilogramos menos de residuos peligrosos genera la propuesta de reducir en 25 %?", "120*25//100", "Se multiplica la masa por el porcentaje y se divide entre 100.", " kg"),
        ("=", "{F} ¿Cuántos pesos al mes se ahorrarían con esa reducción?", "(120*25//100)*1500", "Se multiplican los kilogramos que se dejan de retirar por el costo por kilogramo.", " pesos"),
        ("abc", "{F} ¿Qué medida reduce los residuos peligrosos en su origen?", "Comprar solo la pintura que indica la cubicación", "Mezclarlos con la chatarra", "Guardarlos más tiempo en el acopio", "Reducir en origen es generar menos residuo desde el inicio."),
        ("abc", "{F} Un compañero propone vender los paños con solventes como trapos. ¿Qué corresponde?", "No hacerlo: son residuo peligroso y su destino lo fija la norma vigente, con empresa autorizada", "Hacerlo si se lavan antes", "Hacerlo si son pocos", "Un residuo peligroso no puede entregarse a cualquier persona."),
        ("abc", "{F} ¿Por qué conviene segregar bien la chatarra?", "Porque la recicladora paga mejor la chatarra limpia que la mezclada", "Porque así pesa menos", "Porque así no hace falta registrarla", "La limpieza de la chatarra mejora su valor y evita contaminar."),
        ("=", "{F} ¿Cuántos pesos al año ahorraría la reducción propuesta?", "(120*25//100)*1500*12", "Se multiplica el ahorro mensual por los doce meses.", " pesos"),
        ("abc", "{F} El jefe dice que el ahorro mensual es poco y no vale la pena. Además del dinero, ¿qué otra ventaja tiene la propuesta?", "Menos residuo peligroso significa menos riesgo para las personas y el ambiente", "Que el taller necesita menos contenedores azules", "Que la chatarra pesa más", "La reducción baja el riesgo y no solo el costo."),
        ("=", "{F} Con la propuesta, ¿cuántos pesos costaría el retiro mensual de peligrosos?", "(120-120*25//100)*1500", "Se multiplican los kilogramos restantes por el costo por kilogramo.", " pesos"),
        ("=", "{F} Si la chatarra se vendiera a $130 por kg en lugar de $120, ¿cuántos pesos más ingresarían por la venta?", "900*(130-120)", "Se multiplica la diferencia de precio por los kilogramos.", " pesos"),
    ],
    ctx=("abc", "Un compañero propone regalar el aceite usado a un conocido que dice que lo usará, para no pagar el retiro. ¿Qué respondes?", "Que no: es un residuo peligroso cuyo destino fija la norma vigente, con empresa autorizada, y que lo consultarás con el responsable", "Que sí, porque así ahorra el costo del retiro", "Que sí, si el conocido firma un papel", "Un residuo peligroso no se entrega a cualquier persona para ahorrar; su destino lo fija la norma."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el ingreso por vender chatarra?", "Kilogramos por precio por kilogramo", "El ingreso crece con la masa y el precio."),
        ("¿Cómo se calcula un porcentaje de reducción?", "Masa por porcentaje, dividido entre 100", "El porcentaje se aplica sobre la masa inicial."),
        ("¿Qué conviene hacer con la chatarra para venderla mejor?", "Segregarla y mantenerla limpia", "La chatarra limpia tiene mejor precio."),
    ],
    op=("Caso de ejemplo: un taller vende 400 kg de chatarra a $110 por kg y paga el retiro de 80 kg de residuos peligrosos a $1.500 por kg. Propone reducir en 25 % los peligrosos. Escribe (a) el ingreso por chatarra, (b) el costo del retiro, (c) cuántos pesos se ahorrarían con la reducción, (d) qué haces si el jefe pide ocultar que la chatarra tiene aceite.",
        "(a) 400 × 110 = 44.000 pesos. (b) 80 × 1.500 = 120.000 pesos. (c) 25 % de 80 son 20 kg, y 20 × 1.500 = 30.000 pesos. (d) Respondo que debe declararse el estado real, porque ocultarlo infringe la norma y puede causar riesgos.",
        ["calcula el ingreso", "calcula el costo", "calcula el ahorro", "defiende la información veraz"],
        ["hoja con las cuatro respuestas"],
        ["no aplicar el porcentaje sobre la masa", "mezclar ingresos y costos", "aceptar ocultar el estado de la chatarra"],
        "Pregunta: «¿cuántos kilogramos son el 25 % de 80?». Si no responde, pídele que relea el cálculo del porcentaje."),
    reinforce="Inventa un taller con kilogramos y precios de chatarra y de retiro, y calcula ingreso y costo.",
    extend="Explica con un ejemplo por qué ahorrar dinero no justifica manejar mal un residuo peligroso.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 34 (reglas de ejemplo del taller, no son norma). R1: metal limpio, venta a recicladora autorizada. R2: aceite usado, envases con restos de pintura y guantes o paños con solvente, contenedor rojo rotulado y retiro por empresa autorizada. "
     "R3: papel y cartón limpios, reciclaje. R4: residuo desconocido o sin rótulo, no se manipula y se consulta al responsable. Casos con masas de ejemplo: A, recortes de perfil sin pintura, 40 kg; B, tarro con restos de esmalte, 12 kg; "
     "C, cajas de cartón limpias, 8 kg; D, bidón sin rótulo con un líquido desconocido, 10 kg; E, guantes con solvente, 10 kg. Costo de ejemplo del retiro de peligrosos: $1.500 por kg.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar reglas escritas para decidir el destino de cada residuo, a calcular masas por destino y el costo de retiro, y a actuar ante un residuo desconocido.",
    prior=["Sé qué es un residuo peligroso y la segregación.", "Sé sumar y calcular porcentajes exactos.", "Sé qué es un rótulo y un registro."],
    explain=[
        "Un criterio de manejo es una regla escrita que dice qué hacer con cada tipo de residuo. Para aplicarlo se identifica el residuo del caso, se busca la regla que corresponde y se cita. Si el residuo no calza con ninguna regla, o es desconocido, o no tiene rótulo, no se maneja: no se mezcla, no se huele y no se vierte, y se consulta al responsable. La decisión se registra con la masa real.",
        "Con las reglas se calculan masas por destino: la que se recicla, la que va al contenedor rojo y la que queda sin decidir. El costo del retiro de peligrosos es los kilogramos por el costo por kilogramo. Si un contenedor rojo está lleno, no se mezcla el siguiente residuo con otro contenedor: se avisa para gestionar otro contenedor o un retiro.",
        f"Las reglas reales son las de la norma vigente; las de esta clase son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("criterio de manejo", "regla escrita sobre qué hacer con cada tipo de residuo"), ("destino", "lugar o proceso al que va un residuo: reciclaje, retiro autorizado u otro"), ("residuo desconocido", "residuo cuyo contenido no se sabe, que no se manipula"), ("contenedor lleno", "contenedor que llegó a su capacidad máxima")],
    worked=[
        ("Aplicar una regla", "Con las reglas de la ficha, un tambor de ejemplo con aceite usado, ¿qué destino tiene?", ["El aceite usado figura entre los residuos de la regla R2.", "La regla R2 manda al contenedor rojo y retiro autorizado."], "Contenedor rojo, por R2"),
        ("Costo de retiro", "Un residuo peligroso de ejemplo de 8 kg se retira a $1.500 por kg. ¿Cuánto cuesta?", ["Se multiplican los kilogramos por el costo.", "8 por 1.500 son 12.000."], "$12.000"),
    ],
    mistakes=[("Verter un líquido desconocido para «salir del problema».", "Puede ser peligroso y contaminar; su destino lo decide el responsable.", "No lo manipules y avisa al responsable."),
              ("Aplicar una regla sin comprobar que el residuo calza con ella.", "Puede enviarse un residuo peligroso por una vía de reciclaje.", "Identifica el residuo y cita la regla.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué se hace con un residuo desconocido o sin rótulo?", "No se manipula y se consulta al responsable", "Se mezcla con los residuos comunes", "Se huele para identificarlo", "Un residuo desconocido puede ser peligroso; no se manipula."),
        ("abc", "{F} ¿Qué destino y regla corresponde al caso A, recortes de perfil sin pintura?", "Venta a recicladora autorizada, por R1", "Contenedor rojo, por R2", "No se manipula, por R4", "Es metal limpio, que se recicla."),
        ("abc", "{F} ¿Qué destino y regla corresponde al caso B, tarro con restos de esmalte?", "Contenedor rojo y retiro autorizado, por R2", "Reciclaje, por R3", "Venta a recicladora, por R1", "Los envases con restos de pintura son residuo peligroso."),
        ("abc", "{F} ¿Qué destino y regla corresponde al caso C, cajas de cartón limpias?", "Reciclaje, por R3", "Contenedor rojo, por R2", "No se manipula, por R4", "El cartón limpio es un residuo reciclable."),
        ("abc", "{F} ¿Qué regla corresponde al caso D, el bidón sin rótulo?", "R4: no se manipula y se consulta al responsable", "R1: venta a recicladora", "R3: reciclaje", "No se sabe qué contiene y no se puede aplicar otra regla."),
        ("abc", "{F} ¿Qué destino y regla corresponde al caso E, guantes con solvente?", "Contenedor rojo y retiro autorizado, por R2", "Reciclaje, por R3", "Venta a recicladora, por R1", "El solvente hace de los guantes un residuo peligroso."),
        ("=", "{F} ¿Cuántos kilogramos van al contenedor rojo, sumando los casos B y E?", "12+10", "Se suman las masas de los residuos con destino contenedor rojo.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos se reciclan, sumando los casos A y C?", "40+8", "Se suman las masas de los residuos reciclables.", " kg"),
        ("=", "{F} ¿Qué porcentaje del total de los cinco casos se recicla?", "(40+8)*100//(40+12+8+10+10)", "Se suman los reciclables, se multiplican por 100 y se divide entre el total.", " %"),
        ("abc", "{F} Un compañero huele el bidón D para identificarlo. ¿Qué corresponde?", "No hacerlo: no se manipula ni se huele; se avisa al responsable, por R4", "Está bien, si lo hace con cuidado", "Está bien, si usa mascarilla", "Los vapores desconocidos pueden hacer daño; la regla es no manipular."),
        ("abc", "{F} El contenedor rojo está lleno y llega otro tarro con esmalte. ¿Qué corresponde?", "Avisar al responsable para gestionar otro contenedor o un retiro, sin mezclarlo en otro contenedor", "Mezclarlo con la basura común", "Dejarlo abierto junto al contenedor", "Los residuos peligrosos no se mezclan con otros ni se dejan sueltos."),
        ("=", "{F} ¿Cuántos pesos cuesta retirar los residuos de los casos B y E?", "(12+10)*1500", "Se multiplican los kilogramos peligrosos por el costo por kilogramo.", " pesos"),
        ("abc", "{F} Aparece una batería en la bodega, que no figura en las reglas de la ficha. ¿Qué corresponde?", "No manipularla y consultar al responsable, porque no calza con ninguna regla", "Ponerla en el contenedor azul", "Botarla con la basura común", "Un residuo fuera de las reglas se consulta antes de decidir."),
    ],
    ctx=("abc", "Un compañero propone mezclar el esmalte restante del caso B con los recortes del caso A «para que ocupen menos espacio». ¿Qué respondes?", "Que no: se contaminaría la chatarra limpia; cada residuo va a su contenedor según su regla", "Que sí, si mezcla poco", "Que sí, si lo tapa", "Mezclar un peligroso con metal limpio hace perder el reciclaje y aumenta el riesgo."),
    sc=[
        ("En Construcciones Metálicas: ¿qué hacer con un residuo que no calza con ninguna regla?", "No manipularlo y consultar al responsable", "Una decisión sin regla puede ser peligrosa."),
        ("¿Qué se cita al decidir el destino de un residuo?", "La regla que corresponde", "Así otra persona puede revisar la decisión."),
        ("¿Qué se hace con un contenedor rojo lleno?", "Se avisa para gestionar otro contenedor o un retiro", "No se mezcla el residuo con otro contenedor."),
    ],
    op=("Reglas de la ficha. Casos de ejemplo: F, recortes de plancha sin pintura, 30 kg; G, envase con restos de anticorrosivo, 6 kg; H, cartón limpio, 4 kg; I, frasco sin rótulo, 2 kg. Costo de retiro de peligrosos: $1.500 por kg. Escribe (a) el destino y la regla de cada caso, (b) los kilogramos que se reciclan, (c) el costo de retirar el peligroso, (d) qué haces con el frasco.",
        "(a) F: venta a recicladora, R1; G: contenedor rojo y retiro autorizado, R2; H: reciclaje, R3; I: no se manipula y se consulta, R4. (b) 30 + 4 = 34 kg. (c) 6 × 1.500 = 9.000 pesos. (d) No lo manipulo ni lo huelo y aviso al responsable.",
        ["asigna destino y regla", "suma lo que se recicla", "calcula el costo", "actúa ante el residuo desconocido"],
        ["hoja con las cuatro respuestas"],
        ["mandar el envase con pintura a reciclaje", "incluir el frasco en el costo", "oler o verter el frasco"],
        "Pregunta: «¿qué regla se aplica a un frasco sin rótulo?». Si no responde, pídele que relea R4."),
    reinforce="Inventa cuatro residuos de un taller y asigna a cada uno una regla de la ficha.",
    extend="Explica con un ejemplo por qué es peor mezclar un poco de residuo peligroso con una gran cantidad de chatarra limpia.",
)

# ============================================================ OAE-09, clase 1
F = ("Ficha 35 (caso de ejemplo, inventado). «Estructuras Demo» cubica los materiales de una baranda de 24 m. Perfil de ejemplo: masa por metro de 6 kg por metro; barras comerciales de 6 m; precio de ejemplo de cada barra, $24.000. "
     "Riesgos anotados: perfiles apilados que pueden caer, barras pesadas que se cargan a mano y apuro por compras de última hora. Pedir de menos detiene la obra; pedir de más cuesta dinero y exige almacenar material.")
build(
    O9, 1, F,
    use="Aprenderé qué es cubicar materiales, qué documentos se usan, por qué un error de cubicación cuesta dinero y aumenta riesgos, y a calcular barras, masas y costos simples.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé leer planos y listas de materiales.", "Sé qué es un peligro y un riesgo."],
    explain=[
        "Cubicar es calcular las cantidades de materiales, insumos y otros elementos que necesita una obra, a partir de los planos y de las especificaciones técnicas. Se calculan longitudes en metros, superficies en metros cuadrados, masas en kilogramos y cantidades en unidades. Las barras de acero se compran en largos comerciales, por ejemplo de 6 m, así que el número de barras es la longitud total dividida entre el largo de cada barra.",
        "Un error de cubicación tiene consecuencias. Si se pide de menos, la obra se detiene hasta que llegue lo que falta, y el apuro lleva a improvisar. Si se pide de más, se gasta dinero y se debe almacenar el sobrante. Cubicar también ayuda a la seguridad: la masa de cada barra y del pedido indica cómo almacenar y mover el material. Las barras apiladas deben quedar estables, y una carga que supere lo que la norma vigente permite mover a mano exige ayuda mecánica y personal autorizado.",
        f"La cubicación se hace con el plano en su revisión vigente y se deja en una planilla revisable. {EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular las cantidades de materiales de una obra a partir de planos y especificaciones"), ("largo comercial", "largo en que se vende una barra, por ejemplo 6 m"), ("masa por metro", "masa de un metro de perfil, en kg por metro"), ("merma", "cantidad adicional que se pide por pérdidas o sobrantes"), ("planilla de cubicación", "tabla donde queda registrado el cálculo de cantidades")],
    worked=[
        ("Barras necesarias", "Una reja de ejemplo necesita 30 m de perfil y las barras son de 6 m. ¿Cuántas barras hacen falta?", ["Se divide la longitud total entre el largo de cada barra.", "30 entre 6 son 5."], "5 barras"),
        ("Masa de un pedido", "Cada barra de ejemplo pesa 20 kg y se piden 7. ¿Cuántos kilogramos son?", ["Se multiplican las barras por la masa de cada una.", "7 por 20 son 140."], "140 kg"),
    ],
    mistakes=[("Pedir material «a ojo» sin una planilla.", "No hay forma de revisar el cálculo y los errores salen caros.", "Calcula con el plano y deja la planilla."),
              ("Apilar perfiles muy alto «para ganar espacio».", "La pila puede caer sobre alguien.", "Apila de forma estable y según las reglas del taller.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es cubicar materiales?", "Calcular las cantidades de materiales de una obra a partir de los planos y las especificaciones", "Calcular el volumen de un cubo", "Pagar los materiales a los proveedores", "Cubicar es calcular cantidades, no pagar ni hallar volúmenes de cubos."),
        ("abc", "En Construcciones Metálicas: ¿qué consecuencia tiene pedir de menos material?", "La obra se detiene hasta que llegue lo que falta", "Sobra material en la bodega", "No pasa nada, porque siempre se consigue al instante", "El faltante detiene el trabajo y empuja a improvisar."),
        ("abc", "En Construcciones Metálicas: ¿qué documentos usa quien cubica una obra?", "Los planos y las especificaciones técnicas", "Solo los precios del proveedor", "Solo la opinión del jefe", "Las cantidades salen del proyecto, no de los precios ni de opiniones."),
        ("=", "{F} ¿Cuántas barras de 6 m se necesitan para 24 m de baranda?", "24//6", "Se divide la longitud total entre el largo de cada barra.", " barras"),
        ("=", "{F} ¿Cuántos kilogramos pesa una barra de 6 m con 6 kg por metro?", "6*6", "Se multiplica el largo de la barra por la masa por metro.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos pesan juntas las barras del pedido?", "(24//6)*(6*6)", "Se multiplican las barras por la masa de cada una.", " kg"),
        ("=", "{F} ¿Cuántos pesos cuestan las barras del pedido?", "(24//6)*24000", "Se multiplican las barras por el precio de cada una.", " pesos"),
        ("=", "{F} Si se pide además 1 barra de merma, ¿cuántos pesos cuesta el pedido?", "(24//6+1)*24000", "Se suma la barra de merma y se multiplica por el precio de cada una.", " pesos"),
        ("abc", "{F} Las barras llegan y se apilan casi hasta el techo «para ganar espacio». ¿Qué riesgo hay?", "Que la pila caiga sobre alguien; el apilado debe ser estable y seguir las reglas del taller", "Ninguno, porque son de acero", "Que las barras se enfríen", "Una pila alta e inestable puede caer; el acero pesado agrava el daño."),
        ("abc", "{F} Una barra supera lo que la norma vigente permite cargar a mano. ¿Qué corresponde?", "Usar ayuda mecánica o pedir apoyo de personal autorizado", "Cargarla entre dos personas sin más trámite", "Cargarla rápido para que pese menos", "El límite de carga se respeta con ayudas, no con velocidad."),
        ("abc", "{F} ¿Por qué cubicar bien reduce el riesgo además del costo?", "Porque evita compras apuradas e improvisaciones que llevan a trabajar sin plan", "Porque las barras pesan menos", "Porque elimina la necesidad de EPP", "Un pedido calculado reduce el apuro, que es fuente de accidentes."),
        ("=", "{F} Si la baranda se alarga a 36 m, ¿cuántas barras se necesitan?", "36//6", "Se divide la nueva longitud entre el largo de cada barra.", " barras"),
        ("abc", "{F} El jefe pide pedir 3 barras en vez de las calculadas «para ahorrar». ¿Qué corresponde?", "Explicar que con 3 barras faltan 6 m y la obra se detendrá", "Pedir 3 y acortar la baranda sin avisar", "Pedir 3 y completar con material de otra obra", "El ahorro aparente se transforma en detención y improvisación."),
    ],
    ctx=("abc", "Un compañero dice que no hace falta planilla porque «ya sabe cuánto se necesita a ojo». ¿Qué respondes?", "Que la planilla permite revisar el cálculo y evitar faltantes o excesos, y que se deja siempre", "Que tiene razón si tiene experiencia", "Que la haga después de comprar", "Un cálculo registrado se puede verificar; la intuición no."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el número de barras para una longitud total?", "Longitud total dividida entre el largo de cada barra", "Cada barra aporta su largo comercial."),
        ("¿Cómo se calcula la masa de una barra de perfil?", "Largo por masa por metro", "La masa crece con el largo."),
        ("¿Qué consecuencia tiene pedir de menos?", "La obra se detiene hasta que llegue lo que falta", "El faltante interrumpe el trabajo de la obra."),
    ],
    op=("Caso de ejemplo: una reja de 42 m de perfil con barras de 6 m, 5 kg por metro y barras a $20.000 cada una; se agrega 1 barra de merma. Escribe (a) cuántas barras se calculan sin merma, (b) cuántos kilogramos pesa cada barra, (c) cuántos pesos cuesta el pedido con la barra de merma, (d) qué haces si una barra supera lo que la norma permite cargar a mano.",
        "(a) 42 ÷ 6 = 7 barras. (b) 6 × 5 = 30 kg. (c) (7 + 1) × 20.000 = 160.000 pesos. (d) Uso una ayuda mecánica o pido apoyo de personal autorizado, sin cargarla a mano.",
        ["calcula las barras", "calcula la masa", "calcula el costo", "indica qué hacer con una carga excesiva"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la barra de merma", "multiplicar mal la masa", "cargar a mano un peso excesivo"],
        "Pregunta: «¿cuántas barras se compran en total con merma?». Si responde 7, pídele que sume la barra adicional."),
    reinforce="Inventa una longitud total y un largo de barra y calcula el número de barras necesarias.",
    extend="Explica con un ejemplo por qué una compra de última hora puede aumentar los riesgos de una obra.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 36 (lista de materiales de ejemplo, inventada) de una escalera metálica. PE-1: perfil de 8 kg por metro, 4 barras de 6 m. PL-1: plancha de 2 m² cada una y 40 kg por m², 2 planchas. "
     "PN-1: pernos, 6 uniones con 8 pernos cada una. Pintura: 10 L. Unidades: m para largos, m² para superficies, kg para masas, L para líquidos y und para piezas contadas. "
     "Reglas de ejemplo: masa de un perfil = largo × masa por metro; masa de una plancha = superficie × masa por m².")
build(
    O9, 2, F,
    use="Aprenderé el vocabulario de la cubicación: unidades, masa por metro, masa por m², lista de materiales y revisión del plano, y a calcular masas y cantidades de una lista.",
    prior=["Sé qué es cubicar.", "Sé multiplicar y sumar.", "Sé qué es una lista de materiales."],
    explain=[
        "Una lista de materiales (LDM) ordena cada material con su código, su unidad y su cantidad. Las unidades importan: los largos se miden en metros, las superficies en metros cuadrados, las masas en kilogramos, los líquidos en litros y las piezas contadas en unidades. Confundir unidades produce errores grandes; por eso cada dato lleva su unidad y se pasa a una misma unidad antes de calcular.",
        "La masa de un perfil se calcula multiplicando su largo total por su masa por metro, y la de una plancha multiplicando su superficie por su masa por metro cuadrado. La cantidad de pernos de una unión se calcula multiplicando las uniones por los pernos de cada una. La masa total de una lista se obtiene sumando las masas de cada material. Todo se calcula con el plano y la especificación en su revisión vigente.",
        f"Si una cantidad de la lista no coincide con el plano, se registra la diferencia y se consulta al proyectista. Cubicar no habilita para fabricar ni montar. {EMER} {AVISO}",
    ],
    vocab=[("lista de materiales (LDM)", "tabla con el código, la unidad y la cantidad de cada material"), ("masa por metro", "masa de un metro de perfil, en kg por metro"), ("masa por m²", "masa de un metro cuadrado de plancha, en kg por m²"), ("unidad", "forma de medir una cantidad: m, m², kg, L o und"), ("revisión vigente", "versión actual del plano que se usa para calcular")],
    worked=[
        ("Masa de perfil", "Un perfil de ejemplo tiene 5 kg por metro y se usan 45 m. ¿Cuántos kilogramos son?", ["Se multiplica el largo por la masa por metro.", "45 por 5 son 225."], "225 kg"),
        ("Masa de plancha", "Una plancha de ejemplo de 3 m² tiene 20 kg por m². ¿Cuánto pesa?", ["Se multiplica la superficie por la masa por metro cuadrado.", "3 por 20 son 60."], "60 kg"),
    ],
    mistakes=[("Sumar metros con kilogramos en una misma cuenta.", "Son magnitudes distintas y la suma no tiene sentido.", "Calcula cada magnitud con su unidad y suma solo las del mismo tipo."),
              ("Calcular con una revisión antigua del plano.", "Las cantidades pueden haber cambiado.", "Verifica la revisión vigente antes de cubicar.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿en qué unidad se expresa una superficie?", "En metros cuadrados (m²)", "En metros (m)", "En kilogramos (kg)", "La superficie se mide en m²; el metro mide largos y el kilogramo masas."),
        ("abc", "En Construcciones Metálicas: ¿qué es la masa por metro de un perfil?", "La masa de un metro de ese perfil, en kg por metro", "El largo de la barra", "El precio de un metro de perfil", "La masa por metro es una característica del perfil, distinta del largo o del precio."),
        ("abc", "En Construcciones Metálicas: ¿qué contiene una lista de materiales?", "El código, la unidad y la cantidad de cada material", "Solo los precios de los materiales", "Los nombres de quienes construirán la obra", "La LDM ordena materiales con sus unidades y cantidades."),
        ("=", "{F} ¿Cuántos metros de perfil PE-1 hay en total?", "4*6", "Se multiplican las barras por el largo de cada una.", " m"),
        ("=", "{F} ¿Cuántos kilogramos pesa todo el perfil PE-1?", "4*6*8", "Se multiplica el largo total por la masa por metro.", " kg"),
        ("=", "{F} ¿Cuántos metros cuadrados suman las planchas PL-1?", "2*2", "Se multiplican las planchas por la superficie de cada una.", " m²"),
        ("=", "{F} ¿Cuántos kilogramos pesan las planchas PL-1?", "2*2*40", "Se multiplica la superficie total por la masa por metro cuadrado.", " kg"),
        ("=", "{F} ¿Cuántos pernos PN-1 lleva la escalera?", "6*8", "Se multiplican las uniones por los pernos de cada una.", " pernos"),
        ("=", "{F} ¿Cuántos kilogramos suman el perfil y las planchas?", "4*6*8+2*2*40", "Se suman las masas del perfil y de las planchas.", " kg"),
        ("abc", "{F} Un compañero suma los 24 m de perfil, los 4 m² de plancha y los 48 pernos en un solo total. ¿Qué error cometió?", "Sumó magnitudes distintas, con unidades que no se pueden sumar", "Debió restar los pernos", "Debió dividir entre 3", "Metros, metros cuadrados y unidades son magnitudes distintas."),
        ("abc", "{F} El plano cambia de revisión y la lista aún muestra la anterior. ¿Qué corresponde?", "Cubicar con la revisión vigente y registrar la diferencia con la lista", "Mantener la lista antigua", "Mezclar cantidades de ambas revisiones", "Se cubica siempre con la revisión vigente."),
        ("=", "{F} Si se construyen 3 escaleras iguales, ¿cuántos pernos PN-1 se necesitan?", "3*6*8", "Se multiplican las escaleras por los pernos de cada una.", " pernos"),
        ("abc", "En la lista de otra escalera de ejemplo la pintura aparece solo como «12», sin unidad, y alguien supone que son kg. ¿Qué corresponde?", "Consultar la unidad al responsable o en el plano, y no suponerla", "Suponer kg y calcular", "Quitar la pintura de la lista", "Una unidad no se supone; se verifica en el documento."),
    ],
    ctx=("abc", "Al cubicar, notas que el plano pide 6 uniones, pero la lista de materiales calcula pernos para 5. ¿Qué haces?", "Registrar la diferencia y consultarla al responsable, usando el plano vigente como referencia", "Usar la lista, porque ya estaba hecha", "Promediar ambas cantidades", "Una discrepancia entre documentos se registra y se consulta."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula la masa de una plancha?", "Superficie por masa por metro cuadrado", "La masa crece con la superficie."),
        ("¿Qué unidad usan los líquidos como la pintura?", "Litros (L)", "Los líquidos se miden en litros."),
        ("¿Qué revisión del plano se usa para cubicar?", "La vigente", "Las revisiones antiguas pueden tener cantidades distintas."),
    ],
    op=("Lista de ejemplo de una mesa metálica: perfil de 7 kg por metro, 3 barras de 6 m; plancha de 1 m² y 30 kg por m², 2 planchas; 4 uniones con 6 pernos cada una. Escribe (a) los metros y la masa del perfil, (b) la masa de las planchas, (c) los pernos, (d) qué haces si el plano cambió de revisión.",
        "(a) 3 × 6 = 18 m; 18 × 7 = 126 kg. (b) 2 × 1 × 30 = 60 kg. (c) 4 × 6 = 24 pernos. (d) Cubico con la revisión vigente y registro la diferencia con la lista.",
        ["calcula el perfil", "calcula las planchas", "calcula los pernos", "indica qué hacer con la revisión"],
        ["hoja con las cuatro respuestas"],
        ["sumar magnitudes distintas", "olvidar multiplicar por la masa por metro", "usar la revisión antigua"],
        "Pregunta: «¿qué unidad tiene el resultado de los pernos?». Si responde kg, pídele que relea las unidades."),
    reinforce="Inventa una lista de materiales de tres líneas con su unidad y su cantidad.",
    extend="Explica con un ejemplo por qué es un error sumar metros con kilogramos.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 37 (datos de ejemplo, inventados). Barras comerciales de 6.000 mm a $24.000 cada una. Piezas pedidas: A, 40 piezas de 1.450 mm; B, 21 piezas de 2.000 mm; C, 12 piezas de 2.500 mm. "
     "Se calcula cuántas piezas enteras caben en una barra y cuántas barras se necesitan; el sobrante de cada barra es lo que queda después de las piezas. Cómo se cortan las piezas no se trata aquí.")
build(
    O9, 3, F,
    use="Aprenderé a analizar en papel una planilla de cubicación de barras: piezas por barra, barras necesarias, sobrante y costo, sin ver cómo se cortan.",
    prior=["Sé dividir tomando solo la parte entera.", "Sé multiplicar por precios.", "Sé qué es una merma."],
    explain=[
        "Cuando una obra pide piezas de un largo dado, se calcula cuántas caben enteras en una barra comercial: se divide el largo de la barra entre el largo de la pieza y se toma solo la parte entera. El sobrante de cada barra es el largo de la barra menos el largo de las piezas que caben. El número de barras es el total de piezas dividido entre las piezas por barra, y su costo es las barras por el precio de cada una.",
        "Elegir bien los largos de las piezas puede reducir el sobrante, pero eso lo decide el proyecto. El sobrante total es el sobrante de cada barra por el número de barras. Los sobrantes se registran, porque son material pagado que podría reutilizarse según las reglas del taller. Toda la cuenta se hace en la planilla de cubicación.",
        f"Esto es un cálculo de papel con datos de ejemplo; cortar las piezas lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("piezas por barra", "cantidad de piezas enteras que caben en una barra"), ("sobrante", "largo de la barra que queda después de las piezas"), ("largo comercial", "largo en que se vende una barra"), ("planilla de cubicación", "tabla donde queda registrado el cálculo")],
    worked=[
        ("Piezas por barra", "Una barra de ejemplo mide 6.000 mm y se piden piezas de 1.200 mm. ¿Cuántas caben?", ["Se divide el largo de la barra entre el de la pieza.", "6.000 entre 1.200 son 5."], "5 piezas"),
        ("Sobrante", "Con piezas de 1.700 mm en una barra de 6.000 mm caben 3. ¿Cuánto sobra por barra?", ["Las 3 piezas ocupan 3 por 1.700, es decir, 5.100 mm.", "Sobra 6.000 menos 5.100, que son 900."], "900 mm"),
    ],
    mistakes=[("Contar piezas partidas, por ejemplo 4,13 piezas por barra.", "Una pieza incompleta no sirve.", "Toma solo la parte entera de la división."),
              ("Olvidar el sobrante al calcular el costo real por pieza.", "El material del sobrante también se paga.", "Registra el sobrante y considéralo en el análisis.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿por qué en la cubicación de barras se cuentan solo piezas enteras por barra?", "Porque una pieza incompleta no sirve para el conjunto", "Porque las piezas incompletas pesan menos", "Porque la barra no se puede dividir nunca", "Solo las piezas enteras cumplen el plano."),
        ("=", "{F} ¿Cuántas piezas A de 1.450 mm caben en una barra de 6.000 mm?", "6000//1450", "Se divide el largo de la barra entre el de la pieza y se toma la parte entera.", " piezas"),
        ("=", "{F} ¿Cuántos milímetros sobran en cada barra de las piezas A?", "6000-4*1450", "Se resta el largo ocupado por las piezas al de la barra.", " mm"),
        ("=", "{F} ¿Cuántas barras se necesitan para las 40 piezas A?", "40//(6000//1450)", "Se divide el total de piezas entre las piezas por barra.", " barras"),
        ("=", "{F} ¿Cuántas piezas B de 2.000 mm caben en una barra?", "6000//2000", "Se divide el largo de la barra entre el de la pieza.", " piezas"),
        ("=", "{F} ¿Cuántas barras se necesitan para las 21 piezas B?", "21//(6000//2000)", "Se divide el total de piezas entre las piezas por barra.", " barras"),
        ("=", "{F} ¿Cuántas barras se necesitan para las 12 piezas C de 2.500 mm?", "12//(6000//2500)", "Se divide el total de piezas entre las piezas por barra.", " barras"),
        ("=", "{F} ¿Cuántos milímetros sobran en cada barra de las piezas C?", "6000-2*2500", "Se resta el largo ocupado al de la barra.", " mm"),
        ("=", "{F} ¿Cuántas barras se necesitan en total para las piezas A, B y C?", "40//(6000//1450)+21//(6000//2000)+12//(6000//2500)", "Se suman las barras de los tres tipos de pieza.", " barras"),
        ("=", "{F} ¿Cuántos pesos cuestan todas esas barras?", "(40//(6000//1450)+21//(6000//2000)+12//(6000//2500))*24000", "Se multiplica el total de barras por el precio de cada una.", " pesos"),
        ("abc", "{F} Un compañero calcula 6.000 ÷ 1.450 = 4,13 y concluye que caben 4,13 piezas A por barra. ¿Qué error cometió?", "Contó piezas partidas: solo caben 4 piezas enteras por barra", "Debió redondear a 5", "Debió restar los dos largos", "Una pieza incompleta no sirve; se toma la parte entera."),
        ("=", "{F} ¿Cuántos milímetros suman los sobrantes de todas las barras de las piezas A y C?", "(40//(6000//1450))*(6000-4*1450)+(12//(6000//2500))*(6000-2*2500)", "Se multiplica el sobrante de cada barra por el número de barras de cada tipo.", " mm"),
        ("abc", "{F} El proyectista cambia las piezas A a 1.500 mm. ¿Qué corresponde hacer?", "Rehacer el cálculo con el largo nuevo, porque cambian las piezas por barra y el sobrante", "Mantener el cálculo anterior", "Sumar 50 mm al resultado", "Un largo distinto modifica cuántas piezas enteras caben."),
    ],
    ctx=("abc", "{F} Una compañera ve que la planilla de pedido anota 9 barras para las piezas A, pero el cálculo con los datos de la ficha da 10. El jefe dice «ya se pidió, dejémoslo». ¿Qué haces?", "Registrar la diferencia y avisar al responsable para corregir el pedido antes de que llegue", "Dejar el pedido como está", "Cambiar el cálculo a escondidas para que cuadre", "Una cubicación errónea se informa a tiempo; no se oculta ni se maquilla."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calculan las piezas enteras por barra?", "Largo de la barra dividido entre el largo de la pieza, tomando la parte entera", "La parte decimal sería una pieza incompleta."),
        ("¿Qué es el sobrante de una barra?", "El largo que queda después de las piezas que caben", "Es material pagado que no entra en piezas."),
        ("¿Cómo se calcula el costo de las barras?", "Barras necesarias por precio de cada una", "El costo depende del número de barras."),
    ],
    op=("Caso de ejemplo: barras de 6.000 mm a $25.000 cada una; se piden 28 piezas de 1.500 mm y 14 piezas de 3.000 mm. Escribe (a) cuántas piezas de cada tipo caben por barra, (b) cuántas barras se necesitan en total, (c) cuántos pesos cuestan, (d) por qué se registra el sobrante de las barras.",
        "(a) 6.000 ÷ 1.500 = 4 piezas; 6.000 ÷ 3.000 = 2 piezas. (b) 28 ÷ 4 = 7 barras y 14 ÷ 2 = 7 barras, es decir, 14 barras. (c) 14 × 25.000 = 350.000 pesos. (d) Porque es material pagado que podría reutilizarse y entra en el análisis del costo real.",
        ["calcula las piezas por barra", "calcula las barras necesarias", "calcula el costo", "justifica registrar el sobrante"],
        ["hoja con las cuatro respuestas"],
        ["contar piezas partidas", "no sumar las barras de los dos tipos", "creer que el sobrante no cuesta"],
        "Pregunta: «¿cuántas barras hacen falta para 14 piezas si caben 2 por barra?». Si responde 14, pídele que relea cómo se calculan las barras."),
    reinforce="Inventa una barra de 6.000 mm y una pieza, y calcula cuántas caben y cuánto sobra.",
    extend="Explica con un ejemplo por qué cambiar el largo de una pieza puede ahorrar barras.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 38 (datos de ejemplo, inventados). Presupuesto de una baranda de 30 m: perfil, 12 barras a $24.000; planchas, 3 a $50.000; pintura, 20 L a $10.000 el litro; material de aporte, 5 kg a $8.000 el kilogramo; mano de obra, 80 horas a $6.000 la hora. "
     "Costo directo = suma de materiales y mano de obra. Gastos generales de ejemplo: 10 % del costo directo. Utilidad de ejemplo: 15 % del costo directo. Precio de venta = costo directo + gastos generales + utilidad.")
build(
    O9, 4, F,
    use="Aprenderé a armar en papel un presupuesto simple con costo directo, gastos generales y utilidad, a calcular el precio por metro y a revisar errores comunes.",
    prior=["Sé calcular porcentajes exactos.", "Sé multiplicar cantidades por precios.", "Sé qué es cubicar."],
    explain=[
        "Un presupuesto parte de la cubicación: cada material y cada tipo de trabajo se multiplica por su precio. El costo directo es la suma de los materiales y la mano de obra. Además hay costos que no se asignan a una pieza, como la administración del taller, que se llaman gastos generales y se expresan como un porcentaje del costo directo. La utilidad es la ganancia de la empresa, otro porcentaje. El precio de venta es la suma de los tres.",
        "Para calcular un porcentaje del costo directo se multiplica por el porcentaje y se divide entre 100. El precio por metro se obtiene dividiendo el precio de venta entre los metros. Los errores más frecuentes son olvidar un ítem, sumar mal una unidad, o quitar los gastos generales para ofrecer un precio más bajo, lo que hace perder dinero. Los porcentajes de esta clase son de ejemplo.",
        f"Un presupuesto honesto muestra todos los costos reales; ocultarlos o inventarlos falta a la ética del oficio. Esta cuenta no habilita para ejecutar la obra. {EMER} {AVISO}",
    ],
    vocab=[("presupuesto", "cálculo del costo y del precio de una obra"), ("costo directo", "suma de los materiales y la mano de obra"), ("gastos generales", "costos de administración, expresados como porcentaje del costo directo"), ("utilidad", "ganancia de la empresa, expresada como porcentaje del costo directo"), ("precio de venta", "costo directo más gastos generales más utilidad")],
    worked=[
        ("Costo de un ítem", "Un presupuesto de ejemplo usa 15 horas de mano de obra a $5.000 la hora. ¿Cuánto cuesta?", ["Se multiplican las horas por el precio de cada una.", "15 por 5.000 son 75.000."], "$75.000"),
        ("Porcentaje del costo directo", "Con un costo directo de ejemplo de $200.000 y gastos generales del 10 %, ¿cuánto son los gastos generales?", ["Se multiplica el costo directo por 10.", "200.000 por 10 son 2.000.000, y entre 100 son 20.000."], "$20.000"),
    ],
    mistakes=[("Quitar los gastos generales para ofrecer un precio más bajo.", "La empresa pierde dinero porque esos costos existen igual.", "Incluye todos los costos y ajusta el precio con honestidad."),
              ("Olvidar un ítem del presupuesto, como la mano de obra.", "El precio queda subestimado.", "Revisa la cubicación ítem por ítem.")],
    T=[
        ("abc", "En Construcciones Metálicas: ¿qué es el costo directo de una obra?", "La suma de los materiales y la mano de obra", "Solo el precio de los materiales", "La ganancia de la empresa", "El costo directo incluye materiales y mano de obra."),
        ("abc", "En Construcciones Metálicas: ¿qué son los gastos generales de un presupuesto?", "Costos de administración que se expresan como porcentaje del costo directo", "El precio del perfil", "El sueldo de una sola persona", "Los gastos generales cubren costos que no se asignan a una pieza."),
        ("=", "{F} ¿Cuántos pesos cuesta el perfil?", "12*24000", "Se multiplican las barras por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan las planchas?", "3*50000", "Se multiplican las planchas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la pintura?", "20*10000", "Se multiplican los litros por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la mano de obra?", "80*6000", "Se multiplican las horas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suma el costo directo?", "12*24000+3*50000+20*10000+5*8000+80*6000", "Se suman todos los materiales y la mano de obra.", " pesos"),
        ("=", "{F} ¿Cuántos pesos son los gastos generales?", "(12*24000+3*50000+20*10000+5*8000+80*6000)*10//100", "Se multiplica el costo directo por 10 y se divide entre 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es la utilidad?", "(12*24000+3*50000+20*10000+5*8000+80*6000)*15//100", "Se multiplica el costo directo por 15 y se divide entre 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el precio de venta?", "(12*24000+3*50000+20*10000+5*8000+80*6000)*125//100", "El precio de venta es el costo directo más el 10 % y el 15 %, es decir, el 125 %.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta cada metro de baranda al precio de venta?", "(12*24000+3*50000+20*10000+5*8000+80*6000)*125//100//30", "Se divide el precio de venta entre los 30 metros.", " pesos"),
        ("abc", "{F} Un cliente pide quitar los gastos generales para bajar el precio. ¿Qué corresponde?", "Explicar que esos costos existen igual y que quitarlos haría perder dinero a la empresa", "Quitarlos sin avisar", "Quitar la utilidad y los materiales", "Los gastos generales son costos reales y no desaparecen."),
        ("abc", "{F} Un compañero olvidó incluir la pintura en el presupuesto. ¿Qué efecto tiene?", "El costo directo queda más bajo que el real y la empresa pierde dinero", "Ninguno, porque la pintura es barata", "El precio de venta sube", "Olvidar un ítem subestima el precio y perjudica a la empresa."),
    ],
    ctx=("abc", "Un compañero propone usar el precio por metro de la baranda de la obra anterior para la reja nueva, sin cubicarla. ¿Qué respondes?", "Que se cubica y se calcula con los datos de esta obra, porque el precio por metro de otra obra puede no corresponder", "Que sí, porque las dos son de acero", "Que sí, si la reja nueva es más corta", "Un presupuesto se apoya en la cubicación de la obra actual, no en el precio de otra."),
    sc=[
        ("En Construcciones Metálicas: ¿cómo se calcula el precio de venta del ejemplo?", "Costo directo más gastos generales más utilidad", "Cada parte se suma al costo directo."),
        ("¿Cómo se calcula un porcentaje del costo directo?", "Costo directo por porcentaje, dividido entre 100", "El porcentaje se aplica sobre el costo directo."),
        ("¿Qué pasa si se olvida un ítem del presupuesto?", "El precio queda subestimado", "Falta un costo real en el cálculo."),
    ],
    op=("Presupuesto de ejemplo de una reja de 20 m: perfil, 8 barras a $24.000; planchas, 2 a $50.000; pintura, 10 L a $10.000; mano de obra, 50 horas a $6.000. Gastos generales de ejemplo: 10 %; utilidad de ejemplo: 15 %. Escribe (a) el costo directo, (b) los gastos generales y la utilidad, (c) el precio de venta y el precio por metro, (d) qué respondes si te piden mostrar menos horas.",
        "(a) 192.000 + 100.000 + 100.000 + 300.000 = 692.000 pesos. (b) Gastos generales: 69.200; utilidad: 103.800. (c) 692.000 + 69.200 + 103.800 = 865.000 pesos; por metro, 865.000 ÷ 20 = 43.250 pesos. (d) Que el presupuesto muestra los costos reales y no se manipula.",
        ["suma el costo directo", "calcula los porcentajes", "calcula el precio y el precio por metro", "defiende la veracidad"],
        ["hoja con las cuatro respuestas"],
        ["olvidar un ítem", "calcular el porcentaje sobre el precio de venta", "aceptar manipular las horas"],
        "Pregunta: «¿sobre qué valor se calculan los gastos generales?». Si responde el precio de venta, pídele que relea la ficha."),
    reinforce="Inventa un presupuesto de tres ítems y calcula su costo directo.",
    extend="Explica con un ejemplo por qué ofrecer un precio muy bajo sin considerar todos los costos puede ser un mal negocio.",
)
