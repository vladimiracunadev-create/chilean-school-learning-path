"""Química Industrial TP 3.º medio: OAE-01 (ordenar y disponer materias primas), OAE-02 (medir y registrar variables) y OAE-03 (informes), clases 1 a 3. Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_quin_common import AVISO, EMER, build, em

O1 = "TP-QUIN-3-OAE-01"
O2 = "TP-QUIN-3-OAE-02"
O3 = "TP-QUIN-3-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La empresa ficticia «Química Demo Valle Claro» tiene una bodega de materias primas con tres sectores: recepción, almacenamiento general y un sector de productos inflamables con acceso restringido. "
     "Hay 120 bultos de ejemplo en recepción, 300 en almacenamiento general y 80 en el sector restringido, cuya capacidad es de 100 bultos. Peligros anotados: bultos mal apilados, piso resbaladizo y envase sin rótulo. "
     "Regla de la matriz de ejemplo: puntaje de riesgo = probabilidad (de 1 a 5) × gravedad (de 1 a 5). Bultos mal apilados: probabilidad 3 y gravedad 4. Envase sin rótulo: probabilidad 4 y gravedad 4. Piso resbaladizo: probabilidad 4 y gravedad 2. "
     "En almacenamiento general, cada nivel de estante admite 25 bultos.")
build(
    O1, 1, F,
    use="Aprenderé qué es ordenar y disponer materias primas en una planta química, qué peligros y riesgos tiene una bodega, para qué sirven el rótulo y la hoja de datos de seguridad, y por qué leer documentos no me habilita para manejar sustancias.",
    prior=["Sé leer una tabla sencilla.", "Sé multiplicar, dividir y sumar números enteros.", "Sé que una empresa se rige por reglas escritas."],
    explain=[
        "En Química Industrial, una materia prima es el material que entra a la planta para transformarse en un producto, y un insumo es lo que se usa en el proceso sin quedar necesariamente en el producto final. Ordenar y disponer significa decidir dónde y cómo se guardan, con un layout, que es el plano de disposición de sectores, pasillos y estantes. Cada envase debe llevar un rótulo, que es la etiqueta con el nombre, el lote y el pictograma de peligro, y cada producto tiene una hoja de datos de seguridad, un documento del fabricante que informa sus peligros y precauciones generales: en este cuaderno solo se lee.",
        "Un peligro es una fuente que puede causar daño y el riesgo es la posibilidad de que ese daño ocurra. En la matriz de ejemplo el puntaje se calcula como probabilidad por gravedad y se atiende primero el puntaje mayor. La autoridad sanitaria fiscaliza que el almacenamiento cumpla la norma vigente, y la empresa debe mantener rótulos, pasillos y accesos al día.",
        f"Trasladar y guardar sustancias exige formación, autorización y elementos de protección: leer un documento no habilita a nadie para hacerlo. {EMER} {AVISO}",
    ],
    vocab=[("materia prima", "material que entra a la planta para transformarse en producto"), ("insumo", "material que se usa en el proceso sin quedar necesariamente en el producto"), ("layout", "plano de disposición de sectores, pasillos y estantes"), ("rótulo", "etiqueta con nombre, lote y pictograma de peligro"), ("hoja de datos de seguridad", "documento del fabricante con peligros y precauciones generales, que solo se lee"), ("peligro", "fuente que puede causar daño"), ("riesgo", "posibilidad de que un peligro cause daño"), ("puntaje de riesgo", "probabilidad multiplicada por gravedad, según la matriz")],
    worked=[
        ("Peligro y riesgo", "En una bodega de envases vacíos de ejemplo, una escalera plegable queda abierta en medio del pasillo. ¿Cuál es el peligro y cuál el riesgo?", ["El peligro es la escalera abierta en el pasillo, porque puede causar daño.", "El riesgo es que alguien tropiece con ella y se lesione."], "Peligro: la escalera abierta; riesgo: que alguien tropiece y se lesione"),
        ("Puntaje de riesgo", "En otra bodega de ejemplo, el tránsito de una grúa horquilla en el pasillo tiene probabilidad 2 y gravedad 5. ¿Qué puntaje resulta?", ["Se multiplica la probabilidad por la gravedad.", "2 por 5 son 10."], "10 puntos"),
    ],
    mistakes=[("Creer que quien leyó el layout y la hoja de datos de seguridad ya puede trasladar productos.", "Trasladar sustancias exige formación, autorización y elementos de protección; leer no basta.", "Usa los documentos para saber qué se debe respetar y pide autorización para trabajar."),
              ("Llamar riesgo a la fuente del daño, como el piso resbaladizo.", "La fuente del daño es el peligro; el riesgo es la posibilidad de que alguien resbale.", "Pregúntate: ¿esto es la fuente o es la posibilidad de daño?")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una materia prima?", "El material que entra a la planta para transformarse en un producto", "El producto terminado que se entrega al cliente", "El envase vacío donde se guarda el producto", "La materia prima es lo que se transforma; el producto terminado es el resultado."),
        ("abc", "En Química Industrial: ¿qué es una hoja de datos de seguridad?", "Un documento del fabricante con los peligros del producto y las precauciones generales", "Una receta que enseña cómo combinar el producto con otros", "Una factura con el precio y la cantidad comprada", "La hoja informa peligros y precauciones; no es una receta ni un documento de compra."),
        ("abc", "En Química Industrial: ¿para qué sirve el layout de una bodega?", "Para decidir y mostrar dónde van los sectores, los pasillos y cada tipo de producto", "Para calcular el precio de venta de cada producto", "Para reemplazar los rótulos de los envases", "El layout organiza el espacio; no calcula precios ni reemplaza rótulos."),
        ("=", "{F} ¿Cuántos bultos hay en total en la bodega de la ficha?", "120+300+80", "Se suman los bultos de recepción, de almacenamiento general y del sector restringido.", " bultos"),
        ("abc", "{F} ¿Por qué el sector de productos inflamables tiene acceso restringido?", "Porque su riesgo exige que entre solo personal autorizado", "Porque allí se guardan los bultos más baratos", "Porque es el sector más grande de la bodega", "El acceso restringido limita la entrada justamente por el riesgo del sector."),
        ("abc", "{F} Con la matriz de la ficha, ¿cuál de los peligros debe atenderse primero?", "El envase sin rótulo, con 16 puntos", "Los bultos mal apilados, con 12 puntos", "El piso resbaladizo, porque tiene probabilidad 4", "Se prioriza el mayor puntaje, que combina probabilidad y gravedad."),
        ("=", "{F} ¿Qué puntaje de riesgo tienen los bultos mal apilados?", "3*4", "Se multiplica la probabilidad por la gravedad anotadas en la ficha.", " puntos"),
        ("abc", "{F} Llega a recepción un envase con el rótulo borrado. ¿Qué corresponde?", "No guardarlo ni usarlo y avisar al responsable de bodega para que lo identifique con la documentación", "Guardarlo en almacenamiento general y rotularlo según lo que parezca", "Abrirlo para ver qué contiene y así rotularlo", "Un envase sin rótulo no se guarda ni se abre: se identifica con documentos y con el responsable."),
        ("=", "{F} Mañana llegan 35 bultos que corresponden al sector restringido. ¿Cuántos bultos quedarían sin lugar en ese sector?", "80+35-100", "Se suman los bultos actuales y los que llegan, y se resta la capacidad del sector.", " bultos"),
        ("abc", "{F} Una jefatura de ejemplo propone guardar los envases sin rótulo en almacenamiento general «mientras se identifican». ¿Es correcto?", "No: un envase sin rótulo es un riesgo y no se guarda hasta identificarlo con documentos y autorización del responsable", "Sí, si almacenamiento general tiene espacio libre", "Sí, si se anota en un papel que está «sin rótulo»", "Un papel aparte no reemplaza al rótulo: sin identificación no se sabe qué peligros tiene."),
        ("abc", "Dos compañeros discuten: A dice que el riesgo es «el piso mojado» y B dice que el riesgo es «que alguien se caiga por el piso mojado». ¿Quién tiene razón?", "B: el piso mojado es el peligro y la caída posible es el riesgo", "A: el riesgo es lo que está a la vista", "Ambos, porque peligro y riesgo significan lo mismo", "El peligro es la fuente y el riesgo es la posibilidad del daño."),
        ("=", "{F} ¿Cuántos niveles de estante se necesitan para guardar los 300 bultos de almacenamiento general?", "300//25", "Se divide el total de bultos entre los que admite cada nivel.", " niveles"),
        em("Mientras lees los documentos de una bodega de ejemplo, una persona te cuenta que huele un olor fuerte y extraño en recepción y que un bulto gotea.", 0),
    ],
    ctx=("abc", "En una práctica de ejemplo, un encargado te dice: «Ve a reordenar rápido los bidones del fondo de la bodega, ya viste el layout». No hay instructor presente. ¿Qué respondes?", "Que no, porque trabajar en una bodega química exige formación, autorización y norma vigente, y que consultarás a un adulto responsable", "Que sí, si usas guantes", "Que sí, pero solo los bidones que parezcan livianos", "Leer el layout no habilita para trasladar sustancias; sin instructor ni autorización no se hace."),
    sc=[
        ("En Química Industrial: ¿qué es un peligro?", "Una fuente que puede causar daño, como un envase sin rótulo", "El peligro es la fuente; el riesgo es la posibilidad de daño."),
        ("En Química Industrial: ¿qué datos lleva un rótulo?", "Nombre del producto, lote y pictograma de peligro", "El rótulo identifica el contenido y avisa del peligro."),
        ("En Química Industrial: ¿cómo se calcula el puntaje de riesgo de la matriz de ejemplo?", "Probabilidad multiplicada por gravedad", "El puntaje combina cuán probable y cuán grave es el daño."),
    ],
    op=("Bodega ficticia «Química Demo Costa Norte»: tiene recepción, un sector restringido junto a la salida de emergencia y pasillos con cajas en el suelo. Escribe (a) un peligro y su riesgo asociado en esa bodega, (b) por qué el sector restringido debe estar señalizado y quién debe autorizar la entrada, (c) qué información útil para una emergencia debería mostrar el layout, (d) por qué leer el layout no te habilita para trabajar ahí.",
        "(a) Peligro: cajas en el suelo del pasillo; riesgo: que alguien tropiece y se lesione. (b) Porque su riesgo limita el acceso; lo autoriza el responsable de la bodega. (c) Dónde está la salida de emergencia, cuál es la ruta para llegar y dónde está el punto de reunión. (d) Porque trabajar ahí exige formación, autorización, norma vigente y elementos de protección.",
        ["distingue peligro y riesgo", "justifica la señalización y nombra quién autoriza", "indica información útil para una emergencia", "aclara que leer no habilita"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo a la fuente del daño", "creer que el layout autoriza el ingreso", "no nombrar quién autoriza"],
        "Pregunta: «¿quién puede autorizarte a entrar y qué necesitas tú?». Si no responde, pídele que relea el último párrafo de la explicación."),
    reinforce="Inventa dos peligros de una bodega con probabilidad y gravedad, calcula sus puntajes y di cuál se atiende primero.",
    extend="Explica con un ejemplo por qué un layout desactualizado puede ser peligroso en una emergencia.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Guía de recepción de la empresa ficticia «Química Demo Valle Claro». Proveedor: Proveedora Demo S.A. Producto: «Material A de ejemplo» (materia prima). Lote: L-4821. Bultos declarados en la guía: 45. Bultos recibidos y contados: 40. "
     "Rótulos: 32 completos y 8 ilegibles. Vida útil indicada: 12 meses desde la elaboración. Hoja de datos de seguridad: adjunta. Recibió y registró: bodeguero. Verificó y autorizó el ingreso: jefe de bodega. Cada paleta (plataforma de apoyo) admite 8 bultos. "
     "Roles de ejemplo: el bodeguero recibe y registra; el jefe de bodega verifica y autoriza; el prevencionista de riesgos revisa que el almacenamiento cumpla la norma; el proveedor entrega la hoja de datos de seguridad.")
build(
    O1, 2, F,
    use="Aprenderé los documentos y roles de la recepción de materias primas: guía, lote, rótulo, hoja de datos de seguridad e inventario, y quién hace cada tarea.",
    prior=["Sé qué es un rótulo y una materia prima.", "Sé sumar, restar y dividir números enteros.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "En Química Industrial, una guía de recepción es el documento que registra qué llegó, cuánto y en qué estado. El lote es el grupo de producto fabricado en una misma tanda y se identifica con un código: si un lote tiene un problema, el código permite saber qué otros bultos están afectados, y a eso se llama trazabilidad. El inventario es el registro de las existencias de la bodega. La guía se completa contando lo que realmente llegó, no copiando lo que dice el proveedor.",
        "Si hay diferencias entre lo declarado y lo recibido, o rótulos ilegibles, no se corrige la guía en silencio: se anota la diferencia, se informa al responsable y se deja constancia. La hoja de datos de seguridad la entrega el proveedor y la bodega la archiva sin modificarla. Cada rol tiene una función distinta: registrar, verificar, prevenir y entregar información.",
        f"Esta clase trabaja con documentos en papel; recibir y mover sustancias exige formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("guía de recepción", "documento que registra qué llegó, cuánto y en qué estado"), ("lote", "grupo de producto fabricado en una misma tanda, con un código"), ("trazabilidad", "posibilidad de seguir un producto desde su origen hasta su destino mediante registros"), ("inventario", "registro de las existencias de la bodega"), ("paleta", "plataforma de apoyo sobre la que se agrupan los bultos"), ("prevencionista de riesgos", "profesional que revisa que el trabajo cumpla las normas de seguridad")],
    worked=[
        ("Diferencia de recepción", "La guía de un producto de ejemplo declara 60 bultos y el bodeguero cuenta 57. ¿Cuántos faltan y qué se hace con el dato?", ["Se resta lo recibido a lo declarado: 60 menos 57 son 3.", "Se anota la diferencia en la guía y se informa al jefe de bodega; no se escribe 60 para que cuadre."], "Faltan 3 bultos; se anota y se informa"),
        ("Porcentaje de rótulos completos", "En otra recepción de ejemplo, 18 de 24 bultos traen el rótulo completo. ¿Qué porcentaje es?", ["Se divide 18 entre 24 y se multiplica por 100.", "18 por 100 son 1.800, y 1.800 entre 24 son 75."], "75 %"),
    ],
    mistakes=[("Anotar como «recibidos» la cantidad que dice la guía del proveedor sin contar.", "La guía de recepción registra lo que realmente llegó; si no se cuenta, se oculta una diferencia.", "Cuenta los bultos y anota lo contado, con la diferencia si existe."),
              ("Corregir o reescribir la hoja de datos de seguridad cuando parece incompleta.", "El documento es del fabricante; la bodega no lo modifica, lo archiva y consulta al proveedor.", "Informa al responsable y pide la hoja correcta al proveedor.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un lote?", "Un grupo de producto fabricado en una misma tanda, identificado con un código", "Una caja con los documentos del proveedor", "El número de bultos que caben en una paleta", "El lote agrupa producto de una misma tanda y permite seguirlo si hay un problema."),
        ("abc", "En Química Industrial: ¿qué es la trazabilidad?", "La posibilidad de seguir un producto desde su origen hasta su destino mediante registros", "La velocidad con que se descarga un camión", "El orden alfabético de los productos en el estante", "La trazabilidad se apoya en registros como el lote y la guía."),
        ("abc", "En Química Industrial: ¿qué registra una guía de recepción?", "Qué llegó, cuánto y en qué estado", "Cuánto pagó la empresa por cada kilo", "Qué productos se despacharán mañana", "La guía de recepción deja constancia de lo que realmente llegó."),
        ("=", "{F} ¿Cuántos bultos faltan respecto de lo declarado en la guía?", "45-40", "Se resta lo recibido a lo declarado en la guía del proveedor.", " bultos"),
        ("abc", "{F} ¿Quién entrega la hoja de datos de seguridad del producto?", "El proveedor", "El bodeguero, al contar los bultos", "El prevencionista, que la redacta en la bodega", "La hoja la elabora el fabricante y la entrega el proveedor."),
        ("abc", "{F} ¿Qué rol verificó y autorizó el ingreso del producto?", "El jefe de bodega", "El bodeguero", "El proveedor", "El bodeguero recibe y registra; el jefe de bodega verifica y autoriza."),
        ("=", "{F} ¿Qué porcentaje de los bultos recibidos tiene el rótulo completo?", "32*100//40", "Se divide los rótulos completos entre los bultos recibidos y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas paletas se necesitan para los bultos recibidos, si cada una admite 8 bultos?", "40//8", "Se divide el total de bultos recibidos entre los que admite cada paleta.", " paletas"),
        ("abc", "{F} Los 8 bultos con rótulo ilegible se anotaron en la guía como «completos» para no retrasar el ingreso. ¿Qué opinas?", "Está mal: se debe anotar que son ilegibles e informar al responsable", "Está bien, porque llegaron en buen estado", "Está bien, si luego se rotulan en la bodega", "El registro debe reflejar la realidad; ocultar el problema impide la trazabilidad."),
        ("abc", "{F} Si el lote L-4821 tuviera un problema de calidad, ¿para qué serviría conocer su código?", "Para identificar qué bultos del mismo lote pueden estar afectados y dónde están", "Para saber cuánto pagó el proveedor por el lote", "Para decidir en qué paleta se apilan", "El código del lote permite rastrear los bultos que comparten origen."),
        ("abc", "{F} El prevencionista de riesgos pregunta: «¿para qué la guía anota la vida útil de 12 meses?». ¿Qué respuesta es la correcta?", "Para controlar el vencimiento y usar primero lo que vence antes", "Para calcular cuántos bultos faltan", "Para decidir quién firma la guía", "La vida útil permite planificar el uso antes de que el producto venza."),
        ("=", "{F} El proveedor repone los bultos faltantes. ¿Cuántas paletas se necesitarán para todos los bultos del lote ya repuesto? Redondea hacia arriba.", "(45+7)//8", "Se suma el total de 45 bultos declarados, se divide entre 8 por paleta y se redondea hacia arriba.", " paletas"),
        em("Mientras revisas una guía de recepción de ejemplo, te avisan que de un bulto recién descargado sale humo.", 1),
    ],
    ctx=("abc", "Un proveedor de ejemplo entrega una guía sin código de lote y sin hoja de datos de seguridad. El camión espera. ¿Qué debe hacer el bodeguero?", "Informar al jefe de bodega y dejar constancia de lo que falta antes de que se autorice el ingreso", "Aceptar todo y completar el lote con un número inventado", "Aceptar todo y pedir la hoja al mes siguiente", "Sin lote no hay trazabilidad y sin hoja no se conocen los peligros: se informa antes de autorizar."),
    sc=[
        ("En Química Industrial: ¿qué es el inventario?", "El registro de las existencias de la bodega", "El inventario dice qué hay y cuánto."),
        ("¿Se debe copiar la cantidad de la guía del proveedor sin contar?", "No: se anota lo realmente contado", "La guía de recepción registra la realidad."),
        ("En Química Industrial: ¿qué hace el jefe de bodega en la recepción?", "Verifica y autoriza el ingreso", "Es quien confirma que todo está conforme."),
    ],
    op=("Recepción ficticia en «Química Demo Costa Norte»: la guía declara 32 bultos del lote K-077, se cuentan 25, hay 5 sin rótulo legible y falta la hoja de datos de seguridad. Escribe (a) qué diferencias debe anotar el bodeguero, (b) a quién debe informar, (c) por qué no se corrige la guía para que cuadre, (d) qué porcentaje de los bultos recibidos tiene rótulo legible.",
        "(a) Faltan 7 bultos, hay 5 rótulos ilegibles y falta la hoja de datos de seguridad. (b) Al jefe de bodega. (c) Porque la guía debe reflejar lo real; si se corrige, se pierde la trazabilidad. (d) Hay 20 rótulos legibles de 25 recibidos, es decir, 80 %.",
        ["detecta las diferencias", "nombra a quién informar", "justifica no alterar la guía", "calcula o expresa la proporción de rótulos legibles"],
        ["hoja con las cuatro respuestas"],
        ["ocultar la diferencia", "no informar", "olvidar la hoja de datos de seguridad"],
        "Pregunta: «¿qué pasaría con la trazabilidad si la guía dijera 32 recibidos?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe una guía de recepción de ejemplo con proveedor, lote, cantidades declarada y recibida, y estado de los rótulos.",
    extend="Explica con un ejemplo por qué el código de lote ayuda cuando un producto presenta un problema de calidad.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Plano de planta simplificado de la bodega de la empresa ficticia «Química Demo Valle Claro», escala 1:200 (1 cm del plano representa 2 m reales). Sectores: R recepción, G almacenamiento general, I sector restringido, D despacho y S salida de emergencia. "
     "Distancias medidas en el plano: R–G = 4 cm; G–D = 6 cm; R–I = 9 cm; I–S = 3 cm; G–S = 5 cm. "
     "Matriz de compatibilidad de ejemplo (en la realidad la define la hoja de datos de seguridad y la norma vigente): los productos del grupo 1 y del grupo 2 NO se guardan juntos; grupo 1 con grupo 1 sí; grupo 2 con grupo 2 sí; el grupo 3 (no peligroso, de ejemplo) puede estar con cualquiera. "
     "Productos de ejemplo: P1 es del grupo 1; P2, del grupo 2; P3, del grupo 3; P4, del grupo 1. Estantes: E1 contiene P1; E2 contiene P3; E3 contiene P2.")
build(
    O1, 3, F,
    use="Aprenderé a analizar en papel el layout de una bodega: medir distancias con la escala, separar productos incompatibles según una matriz y mantener libre la ruta de salida.",
    prior=["Sé qué es un layout y un rótulo.", "Sé usar una escala.", "Sé que la hoja de datos de seguridad se lee, no se improvisa."],
    explain=[
        "En Química Industrial, la segregación es guardar separados los productos que no deben estar juntos porque podrían reaccionar entre sí o agravar un accidente. Dos productos incompatibles no se guardan en el mismo estante ni cerca. La hoja de datos de seguridad y la norma vigente indican qué productos son incompatibles; una matriz de compatibilidad es una tabla que resume esas reglas. Los productos se ordenan en grupos y la tabla dice qué grupos pueden convivir.",
        "El layout también debe dejar libre la ruta de evacuación, que es el camino señalado que lleva a la salida de emergencia. Para medir distancias en el plano se aplica la escala: con 1:200, 1 cm del plano son 200 cm, es decir, 2 m reales. Un layout correcto cumple tres cosas a la vez: separa incompatibles, mantiene pasillos y salida libres y deja los productos de uso frecuente cerca de la recepción y el despacho.",
        f"Todo lo anterior se trabaja sobre un plano y una tabla. Mover o reubicar sustancias es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("segregación", "guardar separados los productos que no deben estar juntos"), ("incompatible", "que no debe guardarse junto a otro producto por el peligro que implica"), ("matriz de compatibilidad", "tabla que indica qué grupos de productos pueden guardarse juntos"), ("ruta de evacuación", "camino señalado que lleva a la salida de emergencia"), ("escala", "relación entre una medida del plano y la medida real"), ("grupo de compatibilidad", "conjunto de productos que se tratan igual en la matriz")],
    worked=[
        ("Escala 1:200", "En un plano de ejemplo a escala 1:200, dos estantes están separados por 7 cm. ¿Cuántos metros hay entre ellos en la realidad?", ["1 cm del plano representa 2 m.", "7 por 2 son 14 m."], "14 metros"),
        ("Leer la matriz", "En una matriz de ejemplo, un producto P5 del grupo 2 está en un estante con un producto del grupo 3. ¿Está permitido?", ["El grupo 3 puede estar con cualquiera.", "Por lo tanto, la combinación del grupo 2 con el 3 está permitida."], "Sí, está permitido"),
    ],
    mistakes=[("Poner juntos dos productos «porque se parecen en el envase» sin mirar el grupo de la matriz.", "El parecido del envase no dice si son compatibles; lo dicen la hoja de datos y la matriz.", "Mira siempre el grupo de cada producto en la matriz antes de decidir."),
              ("Tapar la salida de emergencia con estantes para ganar espacio.", "La ruta de evacuación debe estar siempre libre; el espacio extra no justifica el riesgo.", "Dibuja el layout dejando la salida y los pasillos despejados primero.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la segregación de productos en una bodega?", "Guardar separados los productos que no deben estar juntos", "Guardar todos los productos juntos para ahorrar espacio", "Dividir un producto en bultos más pequeños", "La segregación evita que productos incompatibles queden cerca."),
        ("abc", "En Química Industrial: ¿qué es una matriz de compatibilidad?", "Una tabla que indica qué grupos de productos pueden guardarse juntos", "Un listado de los precios de los productos", "Un plano con los caminos de los camiones", "La matriz resume las reglas de convivencia entre grupos."),
        ("abc", "En Química Industrial: ¿por qué la ruta de evacuación debe estar libre?", "Porque en una emergencia las personas deben poder salir sin obstáculos", "Porque así los camiones descargan más rápido", "Porque lo exige solo la jefatura de ventas", "Una ruta bloqueada puede impedir la salida cuando más se necesita."),
        ("=", "{F} ¿Cuántos metros hay en la realidad entre R y G?", "4*2", "Con escala 1:200, cada centímetro del plano vale 2 metros.", " m"),
        ("abc", "{F} Según la matriz, ¿qué producto es incompatible con P1?", "P2", "P4", "P3", "P1 es del grupo 1, que no se guarda junto con el grupo 2, al que pertenece P2."),
        ("abc", "{F} ¿En cuál de los estantes NO debe guardarse P4?", "E3, donde está P2", "E1, donde está P1", "E2, donde está P3", "P4 es del grupo 1, incompatible con el grupo 2 de P2."),
        ("=", "{F} ¿Cuántos metros mide la ruta de recepción a despacho pasando por G (R–G–D)?", "(4+6)*2", "Se suman los tramos en centímetros y se convierte con la escala.", " m"),
        ("abc", "{F} ¿Por qué P3 puede guardarse en el mismo estante que P2?", "Porque el grupo 3 puede estar con cualquier grupo según la matriz", "Porque P3 y P2 tienen el mismo número de bultos", "Porque P3 es de menor tamaño que P2", "La regla del grupo 3 permite su convivencia con todos los grupos."),
        ("=", "{F} ¿Cuántos metros hay de I a la salida S, que es la ruta de evacuación del sector restringido?", "3*2", "Se convierte con la escala el tramo I–S del plano.", " m"),
        ("abc", "{F} Se propone mover un estante para que quede delante de la salida S y ganar espacio. ¿Qué corresponde?", "Rechazar la propuesta porque la salida y su ruta deben quedar libres", "Aceptarla si el estante queda bien rotulado", "Aceptarla si la salida se usa pocas veces", "La salida de emergencia no se obstruye, aunque se use poco."),
        ("abc", "{F} Un compañero dice: «P4 y P1 son del mismo grupo, así que pueden compartir estante». ¿Es correcto?", "Sí: grupo 1 con grupo 1 está permitido en la matriz", "No: productos de un mismo grupo siempre se separan", "Solo si P4 no tiene rótulo", "La matriz permite guardar juntos los productos de un mismo grupo."),
        ("=", "{F} ¿Cuántos metros más corta es la ruta G–S que la ruta G–D?", "(6-5)*2", "Se restan las distancias en centímetros del plano y se convierte con la escala.", " m"),
        em("Estudias el plano de una bodega de ejemplo cuando oyes que alguien avisa que un estante se cayó y que un envase se rompió en el sector restringido.", 2),
    ],
    ctx=("abc", "Un encargado de ejemplo quiere guardar un producto del grupo 2 en el estante de un producto del grupo 1 «solo por esta noche». ¿Qué corresponde?", "No hacerlo: la matriz prohíbe esa combinación y cualquier excepción la decide el responsable con la norma vigente", "Hacerlo si el estante tiene espacio", "Hacerlo si se pone un letrero de aviso", "Una matriz de compatibilidad no admite excepciones por comodidad; un letrero no elimina el riesgo."),
    sc=[
        ("En Química Industrial: ¿qué indica 1:200 en un plano?", "Que 1 cm del plano representa 200 cm reales", "La escala convierte lo dibujado en distancias reales."),
        ("¿Qué grupo puede estar junto a cualquier otro en la matriz de la ficha?", "El grupo 3", "La regla de la ficha lo dice para el grupo no peligroso."),
        ("En Química Industrial: ¿qué documento define la compatibilidad real de un producto?", "La hoja de datos de seguridad junto con la norma vigente", "Son las fuentes oficiales; la matriz las resume."),
    ],
    op=("Plano ficticio de la bodega «Química Demo Costa Norte», escala 1:100 (1 cm = 1 m): recepción a 6 cm del estante X, estante X a 8 cm del despacho, salida de emergencia a 4 cm del estante X. Hay dos productos: Q1 (grupo 1) y Q2 (grupo 2), sin lugar asignado. Escribe (a) cuántos metros hay de recepción a despacho pasando por X, (b) si Q1 y Q2 pueden guardarse en el mismo estante y por qué, (c) qué regla debe respetar el layout respecto de la salida, (d) por qué este análisis no te habilita para mover productos.",
        "(a) 6 más 8 son 14 cm, es decir, 14 m. (b) No, porque son de grupos incompatibles según la matriz de ejemplo. (c) La salida y la ruta de evacuación deben quedar libres. (d) Mover sustancias exige formación, autorización y norma vigente.",
        ["aplica la escala", "usa la matriz de compatibilidad", "protege la salida de emergencia", "aclara que el análisis no habilita"],
        ["hoja con las cuatro respuestas"],
        ["sumar sin convertir la escala", "guardar juntos incompatibles", "bloquear la salida"],
        "Pregunta: «¿qué dice la matriz sobre los grupos 1 y 2?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Dibuja un plano de bodega con cuatro sectores, anota las distancias en centímetros y calcula una ruta en metros con tu escala.",
    extend="Explica con un ejemplo por qué la segregación de productos reduce el daño posible en una emergencia.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Existencias de la bodega ficticia «Química Demo Valle Claro» a fin de mes. Material A: 480 kg, consumo diario del programa de producción 60 kg. Material B: 350 kg, consumo diario 25 kg, vence en 20 días. Material C: 900 kg, consumo diario 50 kg, vence en 90 días. "
     "Stock de seguridad de ejemplo: 7 días de consumo. Lotes del Material A: lote A1 con 200 kg, que vence en 30 días; lote A2 con 280 kg, que vence en 75 días. Regla FEFO: primero vence, primero sale (se usa antes el lote que vence antes). Cada paleta admite 100 kg.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar criterios de inventario con datos de ejemplo: cobertura en días, stock de seguridad, regla FEFO y paletas necesarias, con cálculos exactos en una planilla.",
    prior=["Sé qué es un inventario y un lote.", "Sé multiplicar y dividir números enteros.", "Sé redondear hacia arriba."],
    explain=[
        "En Química Industrial, el programa de producción dice cuánto material se consumirá cada día. La cobertura es el número de días que alcanza la existencia al ritmo de consumo: se calcula dividiendo los kilos que hay entre los kilos que se consumen por día. El stock de seguridad es la reserva mínima que se mantiene para no detener la producción si hay un atraso del proveedor, y aquí se mide en días de consumo.",
        "La regla FEFO (first expired, first out) manda usar primero el lote que vence antes, para no perder producto por vencimiento. Cuando se necesita saber cuántas paletas hacen falta, se divide el total entre lo que admite cada una y, si sobra algo, se redondea hacia arriba, porque media paleta también ocupa una paleta entera. Estos cálculos se hacen en la planilla; la decisión final es del jefe de bodega y la jefatura de producción.",
        f"Mover, abrir o preparar el material es tarea de personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("programa de producción", "plan que indica cuánto material se consumirá cada día"), ("cobertura", "días que alcanza la existencia al ritmo de consumo"), ("stock de seguridad", "reserva mínima para no detener la producción"), ("FEFO", "regla que manda usar primero el lote que vence antes"), ("vencimiento", "fecha o plazo después del cual el producto ya no debe usarse"), ("redondear hacia arriba", "subir al siguiente entero cuando sobra una parte")],
    worked=[
        ("Cobertura", "En una planilla de ejemplo hay 300 kg de un material y se consumen 20 kg por día. ¿Cuántos días de cobertura hay?", ["Se divide la existencia entre el consumo diario.", "300 entre 20 son 15."], "15 días"),
        ("Regla FEFO", "Un material de ejemplo tiene el lote X que vence en 12 días y el lote Y que vence en 40 días. ¿Cuál se usa primero?", ["FEFO manda usar antes lo que vence antes.", "El lote X vence en menos días que el Y."], "El lote X"),
    ],
    mistakes=[("Usar primero el lote más nuevo porque «está en mejor estado».", "Con FEFO se usa primero el que vence antes; el más nuevo puede esperar.", "Compara los días de vencimiento y elige el menor."),
              ("Decir que 480 kg necesitan 4 paletas de 100 kg porque 480 entre 100 «da casi 5».", "Sobran 80 kg que igual ocupan una paleta, y se redondea hacia arriba.", "Divide y, si hay resto, suma una paleta.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la cobertura de un material?", "Los días que alcanza la existencia al ritmo de consumo", "La cantidad de bultos que caben en una paleta", "El precio de un kilo del material", "La cobertura relaciona lo que hay con lo que se consume cada día."),
        ("abc", "En Química Industrial: ¿qué significa FEFO?", "Se usa primero el lote que vence antes", "Se usa primero el lote que llegó último", "Se usa primero el lote más grande", "FEFO ordena el uso según el vencimiento."),
        ("abc", "En Química Industrial: ¿para qué sirve el stock de seguridad?", "Para no detener la producción si el proveedor se atrasa", "Para guardar productos vencidos", "Para aumentar el precio del material", "La reserva mínima evita quedarse sin material por un atraso."),
        ("=", "{F} ¿Cuántos días de cobertura tiene el Material A?", "480//60", "Se divide la existencia entre el consumo diario.", " días"),
        ("=", "{F} ¿Cuántos días de cobertura tiene el Material C?", "900//50", "Se divide la existencia entre el consumo diario del programa.", " días"),
        ("abc", "{F} ¿Qué lote del Material A se usa primero según FEFO?", "El lote A1, porque vence en 30 días", "El lote A2, porque tiene más kilos", "El lote A2, porque vence más tarde", "FEFO usa antes el lote que vence antes, sin importar su tamaño."),
        ("=", "{F} ¿Cuántos kilos de Material A forman el stock de seguridad de 7 días?", "60*7", "Se multiplica el consumo diario por los días de reserva.", " kg"),
        ("abc", "{F} ¿Los 480 kg de Material A superan el stock de seguridad de 7 días?", "Sí, porque 480 es mayor que 420", "No, porque 480 es menor que 420", "Sí, porque 480 es igual a 420", "El stock de seguridad de A es 60 por 7, que son 420 kg."),
        ("abc", "{F} ¿Se alcanza a consumir el Material B antes de que venza?", "Sí, porque su cobertura de 14 días es menor que los 20 días de vigencia", "No, porque la cobertura de 14 días es mayor que los 20 días de vigencia", "No se puede saber sin conocer el precio", "Si el material se consume en 14 días y vence en 20, se usa antes del vencimiento."),
        ("=", "{F} ¿Cuántas paletas se necesitan para los 480 kg de Material A? Redondea hacia arriba.", "(480+99)//100", "Se divide entre 100 kg por paleta y se redondea hacia arriba, porque 80 kg también ocupan una paleta.", " paletas"),
        ("=", "{F} Producción pide cubrir 12 días de consumo del Material A. ¿Cuántos kilos hay que comprar además de la existencia?", "60*12-480", "Se calcula el consumo de 12 días y se resta lo que ya hay.", " kg"),
        ("abc", "{F} ¿Qué material tiene la menor cobertura?", "El Material A, con 8 días", "El Material B, con 14 días", "El Material C, con 18 días", "Al comparar 8, 14 y 18 días, el menor es el de A."),
        em("Mientras calculas la cobertura en una planilla de ejemplo, te avisan que un camión de reparto acaba de golpear un estante y que gotea líquido de un bulto.", 3),
    ],
    ctx=("abc", "Producción de ejemplo pide usar el lote nuevo porque «se ve más limpio», aunque el lote antiguo vence en 10 días y el nuevo en 60. ¿Qué dice la regla FEFO?", "Usar primero el lote antiguo, porque vence antes", "Usar primero el lote nuevo, porque está más limpio", "Usar ambos lotes al mismo tiempo", "FEFO decide por el vencimiento y no por la presentación."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula la cobertura?", "Se divide la existencia entre el consumo diario", "La cobertura son los días que alcanza lo que hay."),
        ("¿Qué hay que hacer si al dividir para calcular paletas sobra una parte?", "Redondear hacia arriba", "La parte sobrante también ocupa una paleta."),
        ("En Química Industrial: ¿qué lote se usa antes con FEFO?", "El que vence antes", "FEFO significa primero vence, primero sale."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte»: Material K con 270 kg y consumo de 30 kg diarios; lote K1 con 90 kg que vence en 8 días y lote K2 con 180 kg que vence en 45 días. Stock de seguridad de 5 días. Escribe (a) la cobertura de K, (b) el stock de seguridad en kilos, (c) qué lote se usa primero y por qué, (d) cuántos kilos habría que comprar para cubrir 15 días de consumo.",
        "(a) 270 entre 30 son 9 días. (b) 30 por 5 son 150 kg. (c) El lote K1, porque vence antes (FEFO). (d) 30 por 15 son 450 kg y menos 270 de existencia son 180 kg.",
        ["calcula la cobertura", "calcula el stock de seguridad", "aplica FEFO", "calcula la compra necesaria"],
        ["hoja con los cuatro cálculos"],
        ["dividir al revés", "usar primero el lote nuevo", "no restar la existencia"],
        "Pregunta: «¿cuántos kilos necesitas en total y cuántos tienes?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa tres materiales con existencia y consumo diario y ordénalos de menor a mayor cobertura.",
    extend="Explica con un ejemplo por qué un stock de seguridad muy alto también puede ser un problema.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Dos alternativas de layout para el almacenamiento general de la empresa ficticia «Química Demo Valle Claro» (escala 1:200, 1 cm = 2 m). "
     "Alternativa A: estantes pegados a la pared, pasillo central de 3 m, distancia de recepción a los estantes más usados 5 cm, costo de reordenar $400.000 (de ejemplo), salida de emergencia completamente libre. "
     "Alternativa B: estantes en islas, pasillos de 2 m, distancia a los estantes más usados 3 cm, costo $250.000 (de ejemplo), una isla deja la salida de emergencia parcialmente tapada. "
     "Se hacen 40 viajes de ida por día entre recepción y los estantes más usados. Revisión de rótulos de la bodega: 25 envases revisados con 5 puntos de control cada uno (nombre, lote, pictograma, fecha de recepción y responsable); 20 envases cumplen los 5 puntos, 3 no tienen lote y 2 no tienen fecha de recepción.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas de layout con distancias, costos y seguridad, y a verificar la calidad de los rótulos con una lista de control, sin sacrificar la salida de emergencia.",
    prior=["Sé usar una escala.", "Sé qué es un layout y un rótulo.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "En Química Industrial, comparar alternativas es mirar varios criterios a la vez: la distancia que se recorre, el costo y la seguridad. Un criterio de seguridad, como mantener libre la salida de emergencia, es una condición obligatoria: una alternativa que no lo cumple se descarta aunque sea más barata o más corta. Entre las alternativas que sí lo cumplen, se compara el costo y el ahorro de recorrido.",
        "Verificar la calidad es comprobar con una lista de control que cada envase tenga los datos exigidos. Una lista de control (o de verificación) es una tabla de puntos que se revisan uno a uno y se marcan como cumple o no cumple. El porcentaje de cumplimiento se calcula dividiendo los envases que cumplen todo entre los revisados y multiplicando por 100. Lo que no cumple se informa al responsable para que se corrija.",
        f"Comparar y calcular es trabajo de planilla; reordenar la bodega o rotular envases lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("alternativa", "una de las opciones que se comparan para resolver un problema"), ("criterio", "aspecto que se usa para comparar opciones, como costo o seguridad"), ("condición obligatoria", "requisito que una opción debe cumplir para poder ser elegida"), ("lista de control", "tabla de puntos que se revisan y se marcan como cumple o no cumple"), ("porcentaje de cumplimiento", "envases que cumplen todo, divididos entre los revisados y multiplicados por 100"), ("no conformidad", "punto que no cumple lo exigido")],
    worked=[
        ("Descartar por una condición obligatoria", "Una alternativa de ejemplo cuesta menos, pero bloquea una puerta de emergencia; otra cuesta más y deja la puerta libre. ¿Cuál se descarta?", ["La puerta de emergencia libre es una condición obligatoria.", "Se descarta la que la bloquea, aunque cueste menos."], "Se descarta la alternativa que bloquea la puerta"),
        ("Porcentaje de cumplimiento", "En una revisión de ejemplo, 36 de 40 etiquetas cumplen todos los puntos. ¿Qué porcentaje de cumplimiento hay?", ["Se divide 36 entre 40 y se multiplica por 100.", "36 por 100 son 3.600, y 3.600 entre 40 son 90."], "90 %"),
    ],
    mistakes=[("Elegir la alternativa más barata sin mirar la seguridad.", "La seguridad de la salida es una condición obligatoria, no un criterio opcional.", "Descarta primero lo que incumple una condición obligatoria y luego compara el costo."),
              ("Contar como «cumple» un envase al que le falta un punto de la lista.", "Para cumplir se necesitan todos los puntos; un punto faltante es una no conformidad.", "Marca «no cumple» si falta cualquiera de los puntos y registra cuál.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una condición obligatoria al comparar alternativas?", "Un requisito que la opción debe cumplir para poder ser elegida", "Un criterio que solo se mira si sobra tiempo", "El precio más bajo entre las alternativas", "Si una opción no cumple la condición obligatoria, se descarta sin importar lo demás."),
        ("abc", "En Química Industrial: ¿qué es una lista de control?", "Una tabla de puntos que se revisan y se marcan como cumple o no cumple", "Una lista de precios de los productos", "Un plano con las rutas de los camiones", "La lista de control sirve para verificar punto por punto."),
        ("abc", "En Química Industrial: ¿qué es una no conformidad?", "Un punto que no cumple lo exigido", "Un producto que se vende con descuento", "Una opinión distinta de la jefatura", "La no conformidad es un incumplimiento que se registra e informa."),
        ("=", "{F} ¿Cuántos metros hay de recepción a los estantes más usados en la alternativa A?", "5*2", "Con escala 1:200, cada centímetro del plano vale 2 metros.", " m"),
        ("=", "{F} ¿Cuántos metros hay de recepción a los estantes más usados en la alternativa B?", "3*2", "Se convierte con la escala la distancia de la alternativa B.", " m"),
        ("abc", "{F} ¿Cuál es el problema de seguridad de la alternativa B?", "Una isla tapa parcialmente la salida de emergencia", "Su costo es mayor que el de la alternativa A", "Su distancia de recorrido es menor", "La salida de emergencia tapada incumple una condición obligatoria."),
        ("=", "{F} ¿Cuántos metros se ahorran por día en viajes de ida con la alternativa B respecto de la A?", "(5-3)*2*40", "Se resta la distancia de B a la de A, se convierte a metros y se multiplica por los viajes.", " m"),
        ("=", "{F} ¿Cuántos pesos más cuesta la alternativa A que la B?", "400000-250000", "Se resta el costo de B al costo de A.", " pesos"),
        ("abc", "{F} ¿Qué alternativa conviene elegir y por qué?", "La A, porque la B incumple la condición obligatoria de la salida libre aunque cueste menos", "La B, porque es más barata y recorre menos metros", "La B, porque la salida parcialmente tapada se puede despejar después", "La seguridad de la salida es obligatoria: descarta a la B."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tiene la revisión de rótulos?", "20*100//25", "Se dividen los envases que cumplen entre los revisados y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué se informa al responsable respecto de los 5 envases que no cumplen?", "Que 3 no tienen lote y 2 no tienen fecha de recepción", "Que los 5 envases no tienen ningún dato", "Que los 5 envases se deben tirar", "Cada no conformidad se registra con el punto específico que falta."),
        ("=", "{F} Los 5 envases con faltantes se corrigen y se revisan de nuevo; ¿cuántos envases cumplirían entonces los 5 puntos?", "20+5", "Se suman los que cumplían y los que se corrigieron.", " envases"),
        em("Estás comparando dos layouts de ejemplo cuando alguien avisa que se rompió un bidón y que hay un olor fuerte junto a la salida de la bodega.", 4),
    ],
    ctx=("abc", "Un jefe de ejemplo te dice: «Anota que los 25 envases cumplen, para no retrasar la auditoría; los 5 con datos faltantes los arreglo mañana». ¿Qué respondes?", "Que el registro debe reflejar lo real: se anotan las 5 no conformidades y se informa al responsable", "Que está bien si los arreglas esa misma semana", "Que está bien si la auditoría no es importante", "Un registro falso impide corregir y pierde la trazabilidad."),
    sc=[
        ("En Química Industrial: ¿qué se hace con una alternativa que incumple una condición obligatoria?", "Se descarta", "La condición obligatoria no se negocia."),
        ("En Química Industrial: ¿cómo se calcula el porcentaje de cumplimiento de una revisión?", "Envases que cumplen entre revisados, por 100", "Es una proporción expresada en porcentaje."),
        ("En Química Industrial: ¿qué se anota al detectar una no conformidad?", "El punto que falta y se informa al responsable", "La anotación permite corregir y seguir el caso."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: layout X cuesta $300.000 (de ejemplo), ahorra 10 metros por viaje y deja una puerta de emergencia libre; layout Y cuesta $150.000, ahorra 14 metros por viaje y obliga a dejar cajas delante de esa puerta. Hay 30 viajes por día. Escribe (a) qué layout se descarta y por qué, (b) cuántos metros por día ahorra el layout elegido, (c) una lista de control de cinco puntos para revisar rótulos, (d) qué harías si una revisión encuentra envases sin lote.",
        "(a) Se descarta Y: bloquea la puerta de emergencia, una condición obligatoria. (b) 10 por 30 son 300 metros por día. (c) Nombre, lote, pictograma, fecha de recepción y responsable. (d) Anotar la no conformidad, informar al responsable y no usar el envase hasta identificarlo.",
        ["descarta por la condición obligatoria", "calcula el ahorro", "propone una lista de control completa", "registra e informa la no conformidad"],
        ["hoja con las cuatro respuestas"],
        ["elegir por costo sin mirar seguridad", "olvidar un punto de la lista", "no informar"],
        "Pregunta: «¿qué layout cumple todas las condiciones obligatorias?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Compara dos layouts inventados con una tabla de distancia, costo y seguridad, y decide cuál elegir.",
    extend="Explica con un ejemplo por qué una lista de control mejora la calidad de la revisión.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (registro de ejemplo, inventado). Planilla de control del tanque T1 de la planta ficticia «Química Demo Valle Claro». Límites de ejemplo: temperatura de 20 a 60 °C; presión de 100 a 150 kPa; pH de 6 a 8; caudal de 20 a 40 L/min. "
     "Lecturas de las 08:00: temperatura 45 °C, presión 120 kPa, pH 7 y caudal 30 L/min. En el turno se hicieron 20 lecturas de temperatura y 18 estuvieron dentro del límite. Instrumentos de la planta: termómetro, manómetro, pHmetro, flujómetro y balanza.")
build(
    O2, 1, F,
    use="Aprenderé qué variables se miden en una planta química, con qué instrumento y en qué unidad, qué es un límite y un indicador, y por qué solo personal autorizado mide en planta.",
    prior=["Sé leer una tabla sencilla.", "Sé calcular un porcentaje sencillo.", "Sé que una medida lleva un número y una unidad."],
    explain=[
        "En Química Industrial, una variable es una magnitud que cambia en un proceso y se puede medir, como la temperatura, la presión, el pH, el caudal o la masa. Cada variable se mide con un instrumento: el termómetro mide la temperatura, el manómetro mide la presión, el pHmetro mide el pH, el flujómetro mide el caudal, el higrómetro mide la humedad y la balanza mide la masa. Toda medida lleva su unidad, como °C, kPa, L/min o kg; sin unidad, el número no dice nada.",
        "Un límite es el valor mínimo o máximo aceptable de una variable; aquí son números de ejemplo, porque los reales los fija la empresa según la norma vigente. Un indicador es un dato calculado con varias mediciones, como el porcentaje de lecturas dentro del límite. El pH indica si una solución es ácida, neutra o básica: 7 es neutro, menos de 7 es ácido y más de 7 es básico. Todo se anota en un registro con fecha, hora, unidad y firma.",
        f"Medir en una planta exige autorización, porque implica estar cerca de tanques, tuberías y equipos. Leer un registro en papel no tiene ese riesgo. {EMER} {AVISO}",
    ],
    vocab=[("variable", "magnitud que cambia en un proceso y se puede medir"), ("instrumento", "aparato con que se mide una variable"), ("unidad", "patrón con que se expresa una medida, como °C o kg"), ("límite", "valor mínimo o máximo aceptable de una variable"), ("indicador", "dato calculado con varias mediciones que resume cómo va el proceso"), ("pH", "medida de acidez: 7 neutro, menor ácido, mayor básico"), ("registro", "anotación escrita con fecha, hora, unidad y firma")],
    worked=[
        ("Lectura dentro del límite", "En una sala de ejemplo, el higrómetro marca 55 % de humedad y el límite va de 40 a 70 %. ¿La lectura está dentro del límite?", ["Se compara el valor con el mínimo y el máximo.", "55 está entre 40 y 70."], "Sí, está dentro del límite"),
        ("Un indicador", "En un turno de ejemplo se hicieron 28 lecturas de caudal y 21 estuvieron dentro del límite. ¿Qué porcentaje es?", ["Se divide 21 entre 28 y se multiplica por 100.", "21 por 100 son 2.100, y 2.100 entre 28 son 75."], "75 %"),
    ],
    mistakes=[("Anotar una medida sin unidad, por ejemplo «120».", "Sin unidad no se sabe qué se midió ni en qué escala; el registro queda incompleto.", "Escribe siempre número y unidad, junto con fecha, hora y firma."),
              ("Creer que quien sabe leer un instrumento puede acercarse a medir en la planta.", "Medir en planta exige autorización y formación por el riesgo del lugar.", "Lee registros en papel y consulta a un adulto responsable antes de acercarte a un equipo.")],
    T=[
        ("abc", "En Química Industrial: ¿qué mide un manómetro?", "La presión", "La temperatura", "El caudal", "El manómetro es el instrumento de la presión; no mide temperatura ni caudal."),
        ("abc", "En Química Industrial: ¿qué es un indicador?", "Un dato calculado con varias mediciones que resume cómo va el proceso", "El instrumento con que se mide una variable", "El límite máximo de una variable", "El indicador resume mediciones, como el porcentaje de lecturas dentro del límite."),
        ("abc", "En Química Industrial: ¿por qué toda medida debe llevar su unidad?", "Porque sin unidad el número no dice qué se midió ni cuánto es", "Porque la unidad corrige el error del instrumento", "Porque solo la pide el proveedor del instrumento", "El número solo tiene sentido con su unidad."),
        ("abc", "{F} ¿Qué instrumento mide el caudal de 30 L/min?", "El flujómetro", "El manómetro", "El higrómetro", "El caudal se mide con un flujómetro."),
        ("=", "{F} ¿Cuántos °C faltan para que la temperatura de las 08:00 llegue al límite máximo?", "60-45", "Se resta la temperatura de la lectura al límite máximo.", " °C"),
        ("abc", "{F} ¿Qué indica el pH 7 de la lectura de las 08:00?", "Que es neutro, justo en el centro de la escala", "Que es muy ácido", "Que es muy básico", "En la escala de pH, 7 es neutro."),
        ("abc", "{F} ¿La presión de las 08:00 está dentro del límite?", "Sí, porque 120 está entre 100 y 150", "No, porque 120 es mayor que 100", "No, porque 120 es menor que 150", "Para estar dentro del límite debe estar entre el mínimo y el máximo a la vez."),
        ("=", "{F} ¿Qué porcentaje de las lecturas de temperatura del turno estuvo dentro del límite?", "18*100//20", "Se dividen las lecturas dentro del límite entre el total y se multiplica por 100.", " %"),
        ("=", "{F} Si el caudal se mantiene en 30 L/min, ¿cuántos litros pasan en 60 minutos?", "30*60", "Se multiplica el caudal por los minutos.", " L"),
        ("abc", "{F} Un compañero anota «presión 120» sin unidad. ¿Qué problema tiene el registro?", "Falta la unidad, y sin ella no se sabe si son kPa u otra", "Ninguno, porque la unidad se supone", "Falta el límite de la variable en cada lectura", "El registro debe llevar número y unidad."),
        ("abc", "Una estudiante en práctica de ejemplo ve un manómetro en una tubería de la planta y quiere acercarse a tomar la lectura. ¿Qué corresponde?", "Leer solo si está autorizada e instruida; si no, consultar a un adulto responsable", "Acercarse con cuidado, porque solo es leer", "Tomar la lectura desde lejos con el celular sin pedir permiso", "Estar cerca de tuberías exige autorización por el riesgo del lugar."),
        ("=", "{F} En otra planilla del mismo tipo hay 25 lecturas de presión y 20 están dentro del límite. ¿Qué porcentaje es?", "20*100//25", "Se dividen las lecturas dentro del límite entre el total y se multiplica por 100.", " %"),
        em("Mientras lees una planilla de ejemplo, una persona te avisa que un manómetro de la sala marca de forma anormal y que sale vapor de una tubería.", 0),
    ],
    ctx=("abc", "Un operario de ejemplo anota en la planilla «temperatura alta» sin número ni hora. ¿Qué debe corregirse?", "Anotar el valor numérico con su unidad, la fecha y la hora", "Nada, porque «alta» es suficiente", "Solo la firma, porque lo demás se entiende", "Una descripción sin número no permite comparar con el límite ni seguir la tendencia."),
    sc=[
        ("En Química Industrial: ¿qué es una variable?", "Una magnitud que cambia en un proceso y se puede medir", "Se puede medir y cambia, como la temperatura."),
        ("En Química Industrial: ¿qué es un límite?", "El valor mínimo o máximo aceptable de una variable", "El límite dice hasta dónde es aceptable la medida."),
        ("¿Qué indica un pH menor que 7?", "Que es ácido", "En la escala de pH, menos de 7 es ácido."),
    ],
    op=("Planilla ficticia del tanque T9 de «Química Demo Costa Norte»: temperatura 30 °C (límite de ejemplo de 10 a 50 °C), presión 90 kPa (límite de 100 a 140 kPa), caudal 25 L/min (límite de 20 a 30 L/min). Escribe (a) qué instrumento mide cada variable, (b) cuál de las tres lecturas está fuera del límite, (c) qué indicador resumiría si en 10 lecturas 8 estuvieron dentro del límite, (d) por qué leer esta planilla no te habilita para medir en la planta.",
        "(a) Termómetro, manómetro y flujómetro. (b) La presión, porque 90 es menor que 100. (c) 8 por 100 entre 10: 80 % de lecturas dentro del límite. (d) Porque medir en planta exige formación, autorización y norma vigente.",
        ["asocia variable e instrumento", "compara con el límite", "calcula el indicador", "aclara que leer no habilita"],
        ["hoja con las cuatro respuestas"],
        ["confundir instrumento y variable", "no comparar con el mínimo", "creer que leer autoriza a medir"],
        "Pregunta: «¿entre qué valores debería estar la presión?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe una planilla de ejemplo con cuatro variables, su unidad, su límite y una lectura, y marca cuáles están dentro del límite.",
    extend="Explica con un ejemplo por qué un número sin unidad puede llevar a una mala decisión.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Certificado de verificación de la balanza B-3 de la planta ficticia «Química Demo Valle Claro». Rango: de 0 a 600 kg. Resolución: 1 kg. Masa patrón de verificación: 100 kg; lectura de la balanza con el patrón: 102 kg. Tolerancia de ejemplo: ±3 kg. "
     "Vigencia de la calibración: 180 días; han pasado 150 días desde la última calibración. Roles de ejemplo: el operador mide y registra; el técnico de instrumentación calibra; el supervisor revisa el registro; el profesional especialista aprueba los informes. "
     "Otra balanza de la planta pesó tres veces la misma masa patrón de 100 kg y marcó 96, 96 y 96 kg.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos de rango, resolución, exactitud, precisión, error, tolerancia y calibración, y quién hace cada tarea al medir y registrar en una planta química.",
    prior=["Sé qué son una variable, una unidad y un límite.", "Sé restar números enteros.", "Sé que los registros llevan fecha y firma."],
    explain=[
        "En Química Industrial, el rango de un instrumento es el conjunto de valores que puede medir, y la resolución es el cambio más pequeño que puede mostrar. Una medida nunca es perfecta: el error es la diferencia entre lo que marca el instrumento y el valor de referencia, que se obtiene con un patrón, es decir, una masa o una referencia de valor conocido. La tolerancia es el error máximo aceptable; si el error es menor o igual a la tolerancia, el instrumento sirve.",
        "La exactitud es qué tan cerca está la medida del valor verdadero, y la precisión es qué tan parecidas son las medidas repetidas entre sí. Un instrumento puede ser preciso y a la vez no exacto, si marca siempre lo mismo pero lejos del valor verdadero. La calibración es la comparación del instrumento con un patrón para comprobar o corregir su error; tiene una vigencia, que es el plazo en que el certificado es válido. Calibrar lo hace un técnico autorizado; el operador solo mide y registra.",
        f"En este cuaderno solo se leen y calculan certificados en papel: manipular instrumentos y patrones en una planta exige formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("rango", "valores que un instrumento puede medir"), ("resolución", "cambio más pequeño que el instrumento puede mostrar"), ("patrón", "referencia de valor conocido con que se compara un instrumento"), ("error", "diferencia entre la lectura y el valor de referencia"), ("tolerancia", "error máximo aceptable"), ("exactitud", "cercanía de la medida al valor verdadero"), ("precisión", "parecido entre medidas repetidas"), ("calibración", "comparación del instrumento con un patrón para comprobar o corregir su error")],
    worked=[
        ("Error y tolerancia", "Un manómetro de ejemplo marca 148 kPa frente a un patrón de 150 kPa, y su tolerancia es ±4 kPa. ¿Sirve?", ["El error es la diferencia entre 150 y 148: 2 kPa.", "2 es menor que 4, así que está dentro de la tolerancia."], "Sí, el error de 2 kPa está dentro de ±4 kPa"),
        ("Vigencia", "Un termómetro de ejemplo tiene una calibración con vigencia de 120 días y han pasado 100 días. ¿Cuántos días quedan?", ["Se resta lo transcurrido a la vigencia.", "120 menos 100 son 20."], "Quedan 20 días"),
    ],
    mistakes=[("Decir que un instrumento es exacto porque repite siempre la misma lectura.", "Repetir la misma lectura muestra precisión, pero puede estar lejos del valor verdadero.", "Compara la lectura con un patrón antes de hablar de exactitud."),
              ("Que el operador «corrija» el instrumento cuando ve un error.", "Calibrar o ajustar lo hace un técnico autorizado; el operador mide, registra e informa.", "Si sospechas un error, avisa al supervisor y no uses el instrumento hasta que lo revisen.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la resolución de un instrumento?", "El cambio más pequeño que puede mostrar", "El rango completo de valores que puede medir", "El error máximo aceptable", "La resolución es el escalón mínimo de la lectura."),
        ("abc", "En Química Industrial: ¿qué es la tolerancia?", "El error máximo aceptable", "La fecha en que se calibró el instrumento", "La cantidad de lecturas del turno", "La tolerancia fija hasta qué error el instrumento sirve."),
        ("abc", "En Química Industrial: ¿qué es la calibración?", "La comparación del instrumento con un patrón para comprobar o corregir su error", "La anotación del resultado en la planilla", "La compra de un instrumento nuevo", "La calibración verifica el instrumento frente a una referencia."),
        ("=", "{F} ¿Cuál es el error de la balanza B-3 con el patrón de 100 kg?", "102-100", "Se resta el valor del patrón a la lectura de la balanza.", " kg"),
        ("abc", "{F} ¿El error de la balanza B-3 está dentro de la tolerancia de ±3 kg?", "Sí, porque 2 kg es menor que 3 kg", "No, porque 2 kg es mayor que 1 kg", "No, porque la balanza marca más que el patrón", "Mientras el error no supere la tolerancia, el instrumento sirve."),
        ("=", "{F} ¿Cuántos días de vigencia le quedan a la calibración de la balanza B-3?", "180-150", "Se resta lo transcurrido a la vigencia total.", " días"),
        ("abc", "{F} ¿Podría la balanza B-3 pesar una masa de 650 kg?", "No, porque 650 kg está fuera de su rango de 0 a 600 kg", "Sí, porque su resolución es de 1 kg", "Sí, si se calibra antes", "Un instrumento solo mide dentro de su rango."),
        ("abc", "{F} La otra balanza marcó 96, 96 y 96 kg con el patrón de 100 kg. ¿Qué se puede decir?", "Es precisa, porque repite el valor, pero no es exacta, porque está lejos de 100 kg", "Es exacta, porque marca siempre lo mismo", "Es exacta y precisa, porque no cambia", "Repetir la misma lectura da precisión; la cercanía al patrón da exactitud."),
        ("=", "{F} ¿Cuántos kilos se aleja de 100 kg la lectura repetida de la otra balanza?", "100-96", "Se resta la lectura al valor del patrón.", " kg"),
        ("abc", "{F} Si la otra balanza tuviera una tolerancia de ±3 kg, ¿qué debería hacerse?", "No usarla y avisar al supervisor para que la revise un técnico autorizado", "Seguir usándola porque es precisa", "Restar 4 kg a cada pesada por cuenta propia", "Con error mayor que la tolerancia, el instrumento queda fuera de uso hasta su revisión."),
        ("abc", "{F} ¿Quién debe calibrar la balanza?", "El técnico de instrumentación", "El operador que la usa", "El profesional que aprueba el informe", "Según los roles de la ficha, calibrar es tarea del técnico."),
        ("=", "{F} Un patrón de 100 kg se pesa en la balanza B-3 dos veces y marca 102 y 101 kg. ¿Cuántos kg suman los dos errores?", "(102-100)+(101-100)", "Se calcula el error de cada lectura y se suman.", " kg"),
        em("Estás leyendo el certificado de una balanza de ejemplo cuando oyes que en la sala de la balanza hay un olor extraño y que alguien se siente mal.", 5),
    ],
    ctx=("abc", "Un técnico de ejemplo te muestra un termómetro cuya calibración venció hace 10 días y te pide usarlo «solo hoy». ¿Qué corresponde?", "No usarlo hasta que se renueve la calibración y avisar al supervisor", "Usarlo si la lectura parece razonable", "Usarlo y anotar que está vencido", "Una calibración vencida deja sin respaldo la medida: se informa antes de usarlo."),
    sc=[
        ("En Química Industrial: ¿qué es el rango de un instrumento?", "El conjunto de valores que puede medir", "Fuera de su rango el instrumento no sirve."),
        ("¿Cómo se obtiene el error de un instrumento?", "Restando el valor del patrón a la lectura", "El error es la diferencia entre lectura y patrón."),
        ("En Química Industrial: ¿qué diferencia hay entre exactitud y precisión?", "La exactitud es cercanía al valor verdadero; la precisión, parecido entre lecturas repetidas", "Son conceptos distintos que no deben confundirse al evaluar."),
    ],
    op=("Certificado ficticio de un termómetro de «Química Demo Costa Norte»: rango de 0 a 100 °C, resolución 1 °C, patrón de 50 °C, lectura 54 °C, tolerancia ±2 °C, vigencia 90 días y han pasado 60. Escribe (a) el error del termómetro, (b) si sirve o no y por qué, (c) cuántos días de vigencia quedan, (d) quién debe actuar si sirve o no.",
        "(a) 54 menos 50 son 4 °C. (b) No sirve, porque 4 es mayor que la tolerancia de 2 °C. (c) Quedan 30 días. (d) Un técnico autorizado debe revisarlo y calibrarlo; el operador avisa al supervisor y no lo usa.",
        ["calcula el error", "compara con la tolerancia", "calcula la vigencia restante", "asigna el rol correcto"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "usar un instrumento fuera de tolerancia", "dejar que el operador corrija el instrumento"],
        "Pregunta: «¿el error es mayor o menor que la tolerancia?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa el certificado de un manómetro con rango, resolución, patrón, lectura y tolerancia, y decide si sirve.",
    extend="Explica con un ejemplo por qué un instrumento muy preciso puede igual dar resultados incorrectos.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (registro de ejemplo, inventado). Planilla de temperatura del tanque T2 de la planta ficticia «Química Demo Valle Claro»; límite de ejemplo de 20 a 60 °C; una lectura cada 2 horas, en °C. "
     "08:00 = 42; 10:00 = 45; 12:00 = 48; 14:00 = 84; 16:00 = 45; 18:00 = 48. Observación del supervisor: a las 14:00 el termómetro marcaba 48 y el operador invirtió los dígitos al escribir. "
     "En la misma hoja, la presión de las 12:00 aparece como «120» sin unidad y la lectura de las 16:00 fue borrada con corrector y reescrita sin firma.")
build(
    O2, 3, F,
    use="Aprenderé a leer una planilla de mediciones, detectar valores atípicos y errores de anotación, y corregir un registro sin ocultar el error original.",
    prior=["Sé qué es un límite y un indicador.", "Sé calcular un promedio sencillo.", "Sé que un registro lleva unidad y firma."],
    explain=[
        "En Química Industrial, un dato atípico es una lectura muy distinta de las demás. Puede ser un cambio real del proceso o un error de anotación. No se decide por intuición: se compara con el límite, con las lecturas vecinas y con lo que informe el supervisor. Un error de transcripción ocurre al copiar el número, por ejemplo al invertir dos dígitos, como escribir 84 en lugar de 48.",
        "Un registro se corrige sin borrar ni usar corrector: se tacha con una línea para que el valor original siga legible, se escribe el valor correcto al lado y se anotan la fecha y la firma de quien corrige. Así el cambio queda a la vista y se puede revisar. El promedio de una serie se calcula sumando las lecturas y dividiendo entre su número; un dato erróneo puede cambiarlo mucho.",
        f"Todo el análisis es de planilla: tocar un instrumento o un tanque exige formación y autorización. {EMER} {AVISO}",
    ],
    vocab=[("dato atípico", "lectura muy distinta de las demás"), ("error de transcripción", "error al copiar un número, como invertir dos dígitos"), ("corrección de un registro", "valor tachado con una línea, valor correcto al lado, fecha y firma"), ("promedio", "suma de las lecturas dividida entre el número de lecturas"), ("lecturas vecinas", "las lecturas anterior y posterior a la que se analiza")],
    worked=[
        ("Detectar un dato atípico", "En una planilla de ejemplo, las lecturas de pH son 7, 7, 17, 7. ¿Cuál es atípica y qué error se sospecha?", ["La lectura 17 se aleja de las demás, que valen 7.", "Probablemente se agregó un dígito al anotar."], "17; probable error de anotación"),
        ("Promedio", "Cuatro lecturas de ejemplo valen 20, 24, 28 y 32 °C. ¿Cuál es el promedio?", ["Se suman: 20 más 24 más 28 más 32 son 104.", "Se divide entre 4: 26."], "26 °C"),
    ],
    mistakes=[("Borrar con corrector una lectura equivocada para que la planilla se vea limpia.", "El registro pierde el valor original y no se puede revisar quién cambió qué.", "Tacha con una línea, escribe el valor correcto, fecha y firma."),
              ("Aceptar una lectura muy distinta de las demás como real sin preguntar.", "Podría ser un error de transcripción o un problema del instrumento.", "Compara con las lecturas vecinas y consulta al supervisor.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un dato atípico?", "Una lectura muy distinta de las demás", "La primera lectura del turno", "La lectura que está justo en el límite", "Un dato atípico se aparta de la serie y debe revisarse."),
        ("abc", "En Química Industrial: ¿qué es un error de transcripción?", "Un error al copiar un número, como invertir dos dígitos", "Un error del instrumento por falta de calibración", "Un error del cálculo del promedio", "Se produce al pasar la lectura a la planilla."),
        ("abc", "En Química Industrial: ¿cómo se corrige un registro?", "Tachando con una línea el valor errado y anotando el correcto con fecha y firma", "Borrando el valor y escribiendo el correcto encima", "Dejando el valor errado y avisando de palabra", "La corrección debe dejar visible el valor original y quién corrigió."),
        ("abc", "{F} ¿Qué lectura de la planilla de temperatura es un dato atípico?", "La de las 14:00, que dice 84", "La de las 08:00, que dice 42", "La de las 18:00, que dice 48", "El 84 se aleja de las demás y supera el límite de 60."),
        ("abc", "{F} ¿Qué explicación da el supervisor para el 84?", "Los dígitos se invirtieron: el termómetro marcaba 48", "El termómetro estaba descalibrado", "La temperatura realmente subió a 84 °C", "La observación dice que se invirtieron los dígitos al escribir."),
        ("=", "{F} ¿Cuántos °C hay de diferencia entre la lectura anotada a las 14:00 y la que marcaba el termómetro?", "84-48", "Se resta el valor correcto al valor anotado por error.", " °C"),
        ("=", "{F} Con el valor corregido de las 14:00, ¿cuál es el promedio de las seis lecturas?", "(42+45+48+48+45+48)//6", "Se suman las seis lecturas con el 48 corregido y se divide entre 6.", " °C"),
        ("=", "{F} ¿Cuál sería el promedio si se dejara el 84 sin corregir? Las seis lecturas suman 312.", "312//6", "Se divide la suma con el 84 entre las seis lecturas.", " °C"),
        ("abc", "{F} ¿Cómo debe corregirse la lectura de las 14:00 en la planilla?", "Tachar el 84 con una línea, escribir 48 al lado, anotar fecha y firma", "Borrar el 84 con corrector y escribir 48", "Dejar el 84 y anotar el promedio corregido", "La corrección conserva visible el dato original y deja responsable."),
        ("abc", "{F} ¿Qué falla tiene la presión «120» de las 12:00?", "Falta la unidad", "Falta la hora", "El número es demasiado grande", "Sin unidad no se sabe qué escala se usó."),
        ("abc", "{F} La lectura de las 16:00 fue borrada con corrector y reescrita sin firma. ¿Qué corresponde?", "Informar al supervisor, porque se perdió el valor original y falta responsable", "Aceptarla porque se ve más ordenada", "Borrar también las demás con corrector para igualar", "Una corrección sin traza no cumple las reglas de un registro."),
        ("=", "{F} ¿Cuántos °C subió la temperatura entre las 08:00 y las 12:00?", "48-42", "Se resta la lectura inicial a la lectura de las 12:00.", " °C"),
        em("Corriges una planilla de ejemplo cuando oyes una alarma y que alguien avisa que se está filtrando un líquido desde el tanque de la sala.", 1),
    ],
    ctx=("abc", "Una supervisora de ejemplo te muestra una planilla con una lectura de 9 entre lecturas de 90, 91 y 92. ¿Qué es lo más adecuado?", "Preguntar si es un error de anotación y, si lo es, corregirlo tachando con fecha y firma", "Dejar el 9 porque podría ser real y no preguntar", "Borrarlo para que la serie se vea pareja", "Un valor muy distinto de sus vecinos debe revisarse y corregirse con traza."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula el promedio de una serie?", "Sumando las lecturas y dividiendo entre su número", "El promedio resume la serie en un valor."),
        ("¿Se puede borrar con corrector una lectura equivocada?", "No: se tacha con una línea, se escribe el valor correcto, fecha y firma", "El registro debe conservar la traza."),
        ("En Química Industrial: ¿qué se hace con una lectura muy distinta de sus vecinas?", "Se revisa y se consulta al supervisor", "Puede ser error de anotación o un cambio real."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte», temperatura de un tanque cada hora, en °C, con límite de ejemplo de 10 a 50 °C: 30, 32, 38, 63. Sabes que el valor de la cuarta hora se anotó mal (el termómetro marcaba 36). Escribe (a) cuál es el dato atípico y qué error se sospecha, (b) cómo corregirías el registro, (c) el promedio con el valor corregido, (d) a quién avisarías.",
        "(a) El 63, probablemente se invirtieron los dígitos de 36. (b) Tachar con una línea, escribir 36 al lado, fecha y firma. (c) 30 más 32 más 38 más 36 son 136; 136 entre 4 son 34 °C. (d) Al supervisor.",
        ["identifica el dato atípico", "describe la corrección correcta", "calcula o expresa el promedio", "nombra a quién avisar"],
        ["hoja con las cuatro respuestas"],
        ["borrar con corrector", "no avisar al supervisor", "no identificar el error de anotación"],
        "Pregunta: «¿cómo queda a la vista el valor original después de tu corrección?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una planilla de seis lecturas con un dato atípico, explica la causa posible y corrígela con traza.",
    extend="Explica con un ejemplo por qué una corrección con fecha y firma protege tanto a quien registra como a quien revisa.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada). Control de masa de 5 sacos de un lote de ejemplo de la planta ficticia «Química Demo Valle Claro»: masa nominal 25 kg por saco; tolerancia de ejemplo ±1 kg (se aceptan sacos de 24 a 26 kg). Masas pesadas: 25; 24; 26; 27; 23 kg. "
     "Otros datos de la planilla: un líquido de ejemplo ocupa 450 L y tiene una masa de 900 kg; el caudal de llenado es 30 L/min; la temperatura al inicio de un ensayo de ejemplo fue de 40 °C y al final, de 46 °C. Equivalencias: 1 kg = 1.000 g y 1 L = 1.000 mL.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo: comprobar tolerancias, calcular promedios, convertir unidades, estimar una densidad y expresar un cambio como porcentaje.",
    prior=["Sé calcular un promedio.", "Sé qué es una tolerancia.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "En Química Industrial, una masa nominal es la masa que debería tener un envase según su rotulado, y la tolerancia dice cuánto se puede desviar. Un saco cumple si su masa está entre el mínimo y el máximo permitidos. Para comparar medidas hay que usar la misma unidad: 1 kg son 1.000 g y 1 L son 1.000 mL, así que para pasar de kg a g se multiplica por 1.000.",
        "La densidad de un líquido es su masa dividida entre su volumen, por ejemplo en kg por L; aquí los valores son de ejemplo. El caudal permite calcular un volumen: litros que pasan = caudal en L/min por los minutos. La variación porcentual compara el cambio con el valor inicial: se divide el cambio entre el valor inicial y se multiplica por 100. Todos los cálculos de esta clase son de planilla y se hacen con números enteros exactos.",
        f"Los cálculos orientan decisiones que toma el supervisor; pesar, llenar o manipular envases lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("masa nominal", "masa que debería tener un envase según su rotulado"), ("tolerancia", "desviación máxima permitida"), ("conversión de unidades", "cambio de una unidad a otra equivalente"), ("densidad", "masa de un material dividida entre su volumen"), ("caudal", "volumen que pasa por unidad de tiempo"), ("variación porcentual", "cambio dividido entre el valor inicial, multiplicado por 100")],
    worked=[
        ("Tolerancia", "Un envase de ejemplo tiene masa nominal de 10 kg y tolerancia ±2 kg. Pesa 13 kg. ¿Cumple?", ["El rango aceptable va de 8 a 12 kg.", "13 está fuera de ese rango."], "No cumple"),
        ("Variación porcentual", "Una temperatura de ejemplo pasa de 50 °C a 60 °C. ¿Cuál es la variación porcentual?", ["El cambio es 10 °C.", "10 entre 50, por 100, es 20."], "Subió 20 %"),
    ],
    mistakes=[("Comparar 25 kg con 24.500 g sin convertir.", "Las unidades distintas no se pueden comparar directamente.", "Convierte todo a la misma unidad antes de comparar."),
              ("Dividir el cambio entre el valor final en la variación porcentual.", "El porcentaje se calcula respecto del valor inicial.", "Divide siempre entre el valor de partida.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es la masa nominal de un saco?", "La masa que debería tener según su rotulado", "La masa del saco vacío", "La masa máxima que soporta el estante", "La masa nominal es la masa declarada del envase."),
        ("abc", "En Química Industrial: ¿qué es la densidad de un líquido?", "Su masa dividida entre su volumen", "Su volumen dividido entre su masa", "Su temperatura dividida entre su caudal", "La densidad relaciona masa y volumen."),
        ("abc", "En Química Industrial: ¿para pasar de kg a g qué se hace?", "Se multiplica por 1.000", "Se divide entre 1.000", "Se suma 1.000", "Un kilogramo equivale a 1.000 gramos."),
        ("abc", "{F} ¿Qué rango de masa acepta la tolerancia de los sacos?", "De 24 a 26 kg", "De 25 a 27 kg", "De 23 a 25 kg", "La tolerancia de ±1 kg se suma y se resta a 25 kg."),
        ("=", "{F} ¿Cuántos sacos de los 5 pesados están dentro de la tolerancia?", "3", "Cumplen los sacos de 25, 24 y 26 kg; los de 27 y 23 kg quedan fuera.", " sacos"),
        ("=", "{F} ¿Cuál es la masa promedio de los 5 sacos?", "(25+24+26+27+23)//5", "Se suman las cinco masas y se divide entre 5.", " kg"),
        ("=", "{F} ¿Cuántos gramos tiene el saco de 24 kg?", "24*1000", "Se multiplica por 1.000 para pasar de kg a g.", " g"),
        ("=", "{F} ¿Cuántos kg por litro tiene la densidad del líquido de ejemplo?", "900//450", "Se divide la masa entre el volumen.", " kg/L"),
        ("=", "{F} Con el caudal de llenado de la ficha, ¿cuántos litros pasan en 15 minutos?", "30*15", "Se multiplica el caudal por los minutos.", " L"),
        ("=", "{F} ¿Cuál fue la variación porcentual de la temperatura del ensayo?", "(46-40)*100//40", "Se divide el cambio entre el valor inicial y se multiplica por 100.", " %"),
        ("abc", "{F} Un compañero dice: «los 5 sacos cumplen porque el promedio es 25 kg». ¿Es correcto?", "No: el promedio es 25, pero los sacos de 27 y 23 kg individualmente están fuera de tolerancia", "Sí, porque el promedio es igual a la masa nominal", "Sí, porque 27 y 23 se compensan", "La tolerancia se aplica a cada saco, no al promedio."),
        ("=", "{F} El llenado de un tanque con el caudal de la ficha dura 45 minutos. ¿Cuántos litros se llenan?", "30*45", "Se multiplica el caudal por los minutos de llenado.", " L"),
        em("Estás haciendo cálculos de una planilla de ejemplo cuando alguien avisa que se rompió un saco y que se levanta polvo con olor irritante.", 2),
    ],
    ctx=("abc", "Una supervisora de ejemplo recibe un reporte con «masa 24,5» sin decir si es kg o g. ¿Qué debe pedir?", "Que se anote la unidad antes de comparar con la tolerancia", "Nada, porque 24,5 es parecido a 25", "Que se multiplique por 1.000 siempre", "Sin unidad no se puede comparar con la tolerancia de kg."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula la densidad?", "Masa dividida entre volumen", "La densidad relaciona cuánta masa hay en cada litro."),
        ("¿Cuántos gramos son 3 kg?", "3.000 g", "Un kilogramo equivale a mil gramos, por eso se multiplica."),
        ("En Química Industrial: ¿respecto de qué valor se calcula la variación porcentual?", "Del valor inicial", "El cambio se compara con el punto de partida."),
    ],
    op=("Planilla ficticia de «Química Demo Costa Norte»: 5 envases con masa nominal de 20 kg y tolerancia ±2 kg pesan 20; 22; 19; 23; 21 kg. Un líquido de ejemplo ocupa 300 L y tiene una masa de 600 kg. Escribe (a) cuántos envases cumplen la tolerancia, (b) la masa promedio, (c) la densidad del líquido, (d) por qué la tolerancia se revisa envase por envase.",
        "(a) Cumplen 20, 22, 19 y 21; no cumple el de 23 (rango de 18 a 22 kg): 4 envases. (b) 105 entre 5 son 21 kg. (c) 600 entre 300 son 2 kg/L. (d) Porque cada envase debe cumplir; un promedio puede ocultar uno fuera de rango.",
        ["aplica el rango de tolerancia", "calcula el promedio", "calcula la densidad", "justifica la revisión individual"],
        ["hoja con las cuatro respuestas"],
        ["aceptar por el promedio", "confundir masa y volumen", "olvidar el rango inferior"],
        "Pregunta: «¿entre qué valores debe estar cada envase?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa cinco masas de envases con su tolerancia, decide cuántos cumplen y calcula el promedio.",
    extend="Explica con un ejemplo por qué comparar medidas en unidades distintas puede llevar a una decisión equivocada.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Se deben controlar sacos de 25 kg con tolerancia de ±2 kg en la planta ficticia «Química Demo Valle Claro». Regla de ejemplo: la resolución del instrumento debe ser menor que la tolerancia. "
     "Balanza X: rango de 0 a 100 kg, resolución 1 kg, certificado vigente por 40 días más, arriendo mensual $90.000 (de ejemplo). Balanza Y: rango de 0 a 500 kg, resolución 5 kg, certificado vencido hace 10 días, arriendo mensual $50.000 (de ejemplo). "
     "Registro de 10 pesadas del turno: 8 completas (valor, unidad, fecha, hora y firma), 1 sin unidad y 1 sobrescrita sin firma.")
build(
    O2, 5, F,
    use="Aprenderé a comparar instrumentos según rango, resolución, vigencia y costo, y a verificar la calidad de un registro de mediciones con una lista de control.",
    prior=["Sé qué son rango, resolución y tolerancia.", "Sé calcular porcentajes sencillos.", "Sé corregir un registro con traza."],
    explain=[
        "En Química Industrial, elegir un instrumento es compararlo con lo que se necesita medir. Primero se revisan las condiciones obligatorias: el valor que se mide debe estar dentro del rango, la resolución debe ser menor que la tolerancia (si no, el instrumento no distingue lo que hay que controlar) y el certificado de calibración debe estar vigente. Solo entre los instrumentos que cumplen todo eso se compara el costo.",
        "Verificar la calidad de un registro es revisar, con una lista de control, que cada anotación tenga valor, unidad, fecha, hora y firma y que no esté borrada ni sobrescrita sin traza. El porcentaje de registros completos es un indicador de la calidad del trabajo. Las anotaciones incompletas se informan al supervisor para corregirlas con la traza correcta.",
        f"Todo es análisis en papel: instalar, calibrar o usar los instrumentos corresponde a personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("condición obligatoria", "requisito que una opción debe cumplir para poder elegirse"), ("certificado vigente", "certificado de calibración cuyo plazo aún no vence"), ("registro completo", "anotación con valor, unidad, fecha, hora y firma"), ("sobrescrita", "anotación escrita encima de otra, sin dejar visible la original"), ("lista de control", "tabla de puntos que se revisan uno a uno")],
    worked=[
        ("Elegir con condiciones obligatorias", "Una tolerancia de ejemplo es ±3 kg. El instrumento P tiene resolución de 5 kg y el instrumento Q, resolución de 1 kg. ¿Cuál cumple la regla?", ["La regla exige que la resolución sea menor que la tolerancia.", "5 no es menor que 3, pero 1 sí lo es."], "El instrumento Q"),
        ("Porcentaje de registros completos", "En una revisión de ejemplo, 9 de 12 registros están completos. ¿Qué porcentaje es?", ["Se divide 9 entre 12 y se multiplica por 100.", "9 por 100 son 900, y 900 entre 12 son 75."], "75 %"),
    ],
    mistakes=[("Elegir el instrumento más barato aunque su resolución sea mayor que la tolerancia.", "No distingue las diferencias que hay que controlar; el ahorro no sirve.", "Revisa primero rango, resolución y vigencia y compara el costo al final."),
              ("Aprobar un registro al que le falta la unidad porque «se entiende».", "Sin unidad el dato queda incompleto y no se puede comparar con el límite.", "Marca «no cumple», anota qué falta e informa al supervisor.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es una condición obligatoria al elegir un instrumento?", "Un requisito que debe cumplir para poder elegirse", "Un criterio que se mira solo si sobra tiempo", "El precio más bajo entre las opciones", "Quien no cumple una condición obligatoria se descarta."),
        ("abc", "En Química Industrial: ¿cuándo un registro está completo?", "Cuando tiene valor, unidad, fecha, hora y firma", "Cuando solo tiene el valor y la firma", "Cuando el valor está dentro del límite", "El registro completo incluye todos esos datos."),
        ("abc", "En Química Industrial: ¿qué significa que un certificado esté vigente?", "Que su plazo de validez aún no ha vencido", "Que el instrumento nunca falla", "Que el certificado fue impreso este año", "La vigencia es el plazo en que el certificado respalda la medida."),
        ("abc", "{F} ¿Cuál es la tolerancia del control de los sacos?", "±2 kg", "±1 kg", "±5 kg", "La ficha fija ±2 kg para sacos de 25 kg."),
        ("abc", "{F} ¿La balanza X cumple la regla de resolución?", "Sí, porque su resolución de 1 kg es menor que la tolerancia de 2 kg", "No, porque su rango es de solo 100 kg", "No, porque su resolución es mayor que su tolerancia", "La regla compara resolución con tolerancia."),
        ("abc", "{F} ¿Por qué la balanza Y no sirve para este control?", "Su resolución de 5 kg es mayor que la tolerancia de 2 kg y su certificado está vencido", "Su rango de 500 kg es demasiado pequeño", "Porque su arriendo es más caro", "Incumple dos condiciones obligatorias: resolución y vigencia."),
        ("=", "{F} ¿Cuánto cuesta al año el arriendo de la balanza X?", "90000*12", "Se multiplica el costo mensual por 12 meses.", " pesos"),
        ("=", "{F} ¿Cuántos pesos al año se ahorrarían con la balanza Y respecto de la X?", "(90000-50000)*12", "Se resta el costo mensual de Y al de X y se multiplica por 12.", " pesos"),
        ("abc", "{F} Sabiendo todo lo anterior, ¿qué balanza conviene elegir?", "La X, porque cumple rango, resolución y vigencia aunque cueste más", "La Y, porque es más barata", "La Y, porque tiene mayor rango", "Entre las que cumplen las condiciones obligatorias, solo queda la X."),
        ("=", "{F} ¿Qué porcentaje de las 10 pesadas del registro está completo?", "8*100//10", "Se dividen las completas entre las revisadas y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué corresponde hacer con la pesada anotada sin unidad?", "Marcarla como no cumple, anotar qué falta e informar al supervisor", "Aceptarla porque el valor está dentro de la tolerancia", "Escribir la unidad que parezca más probable", "Una anotación incompleta se informa; no se adivina la unidad."),
        ("=", "{F} Si el supervisor corrige las 2 anotaciones con problemas con la traza correcta, ¿cuántas de las 10 pesadas quedarán completas?", "8+2", "Se suman las completas y las corregidas.", " pesadas"),
        em("Mientras comparas instrumentos en un cuaderno de ejemplo, una persona te avisa que se rompió el vidrio de un equipo de la sala y que hay un olor fuerte.", 3),
    ],
    ctx=("abc", "Una jefatura de ejemplo propone usar la balanza Y «solo esta semana» por ahorro, pese a su certificado vencido. ¿Qué respondes?", "Que no corresponde, porque falta la condición obligatoria de vigencia y debe informarse al supervisor", "Que sí, si se anotan las pesadas con cuidado", "Que sí, si se le suma 5 kg a cada pesada", "Con certificado vencido las medidas no tienen respaldo."),
    sc=[
        ("En Química Industrial: ¿qué regla relaciona la resolución con la tolerancia?", "La resolución debe ser menor que la tolerancia", "Así el instrumento distingue lo que se controla."),
        ("¿Cómo se calcula el porcentaje de registros completos?", "Completos entre revisados, por 100", "Es un indicador que resume la calidad de los registros."),
        ("En Química Industrial: ¿qué se hace con un registro al que le falta la unidad?", "Se marca como no cumple y se informa", "La corrección la hace el responsable con traza."),
    ],
    op=("Caso ficticio de «Química Demo Costa Norte»: se necesita pesar envases de 10 kg con tolerancia de ±2 kg. Balanza M: resolución 1 kg, certificado vigente, arriendo $30.000 al mes. Balanza N: resolución 1 kg, certificado vencido, arriendo $20.000 al mes. Un registro de 5 pesadas tiene 4 completas y una sin firma. Escribe (a) qué balanza se descarta y por qué, (b) si la resolución de la balanza elegida cumple la regla y por qué, (c) el costo anual de la balanza elegida, (d) qué porcentaje del registro está completo.",
        "(a) Se descarta la N, porque su certificado está vencido. (b) Sí, porque la resolución de 1 kg es menor que la tolerancia de 2 kg. (c) 30.000 por 12 son 360.000 pesos. (d) 4 de 5 es 80 %.",
        ["descarta por vencimiento", "aplica la regla de resolución", "calcula el costo anual", "calcula el porcentaje de registro completo"],
        ["hoja con las cuatro respuestas"],
        ["elegir por precio", "no aplicar la regla de resolución", "no informar el registro incompleto"],
        "Pregunta: «¿cuál es la condición que descarta la N?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Compara dos instrumentos inventados con una tabla de rango, resolución, vigencia y costo, y decide cuál elegir.",
    extend="Explica con un ejemplo por qué la resolución de un instrumento debe relacionarse con la tolerancia.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Informe de turno de la planta ficticia «Química Demo Valle Claro» sobre el tanque T3: temperatura medida cada hora, en °C: 30; 32; 34; 36; 38; 40 (seis lecturas, cinco intervalos de una hora). Límite de ejemplo: de 20 a 60 °C. "
     "Formato de informe de ejemplo: título, fecha, responsable, objetivo, datos, tendencia, observaciones, firma del responsable y espacio para la aprobación del profesional especialista. La empresa usa planillas manuales en papel y planillas digitales; aquí solo se trabaja en papel.")
build(
    O3, 1, F,
    use="Aprenderé para qué sirve un informe de mediciones, qué es una tendencia, por qué se usan formatos establecidos y por qué quien informa describe datos y el profesional especialista decide.",
    prior=["Sé qué es una variable, una lectura y un límite.", "Sé calcular un promedio sencillo.", "Sé que un registro lleva fecha y firma."],
    explain=[
        "En Química Industrial, un informe de mediciones es un documento que presenta los datos medidos de una variable, describe cómo se comportaron y se entrega a un profesional especialista para su revisión y aprobación. Se escribe en un formato establecido, es decir, una plantilla fija con los mismos campos para todos, que puede ser una planilla manual en papel o una digital. Así los informes se pueden comparar y revisar.",
        "La tendencia es la dirección en que van los datos: pueden subir, bajar, mantenerse estables u oscilar. Una proyección es una estimación de lo que ocurriría si la tendencia siguiera igual; sirve para avisar, pero no es una certeza. En el informe se separan los datos y las observaciones, que son hechos medidos, de las opiniones y de las decisiones: quien informa describe, y el profesional especialista interpreta, aprueba y decide.",
        f"Escribir un informe no te habilita para intervenir en un tanque ni en un equipo. {EMER} {AVISO}",
    ],
    vocab=[("informe de mediciones", "documento que presenta datos medidos y su comportamiento"), ("formato establecido", "plantilla fija con los mismos campos para todos"), ("tendencia", "dirección en que van los datos: sube, baja, estable u oscila"), ("proyección", "estimación de lo que pasaría si la tendencia siguiera igual"), ("observación", "hecho medido o visto, sin opinión"), ("profesional especialista", "persona que revisa, aprueba y decide a partir del informe")],
    worked=[
        ("Describir una tendencia", "Una presión de ejemplo se mide cuatro veces: 50, 48, 46 y 44 kPa. ¿Qué tendencia hay?", ["Cada lectura es 2 menor que la anterior.", "Los datos bajan de forma pareja."], "Baja 2 kPa por lectura"),
        ("Observación y opinión", "Un operario escribe «el tanque es un desastre». ¿Cómo se convierte en una observación?", ["Una observación se apoya en un dato medido.", "Por ejemplo: «la temperatura subió de 30 a 33 °C en 2 horas»."], "Con un dato medido, como la subida de 30 a 33 °C en 2 horas"),
    ],
    mistakes=[("Escribir en el informe una opinión o una orden en lugar de describir los datos.", "El informe presenta hechos medidos; la decisión es del profesional especialista.", "Anota datos y tendencia, y deja la interpretación y la decisión al especialista."),
              ("Completar lecturas que aún no se han medido porque «siempre dan lo mismo».", "Un informe solo registra lo realmente medido; inventar datos lo vuelve falso.", "Anota solo lecturas reales y deja constancia de las que faltan.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es un informe de mediciones?", "Un documento que presenta datos medidos y su comportamiento para que lo revise un especialista", "Una orden de trabajo para operar un equipo", "Una factura con el costo de los instrumentos", "El informe describe datos; no ordena trabajos ni cobra."),
        ("abc", "En Química Industrial: ¿qué es una tendencia?", "La dirección en que van los datos: sube, baja, se mantiene o oscila", "El valor máximo que alcanzó una variable", "El instrumento con que se mide", "La tendencia describe cómo cambian los datos en el tiempo."),
        ("abc", "En Química Industrial: ¿por qué se usan formatos establecidos?", "Para que todos informen los mismos datos y los informes se puedan comparar y revisar", "Para que cada persona escriba como prefiera", "Para reemplazar la firma del responsable", "Un formato común ordena la información y facilita la revisión."),
        ("=", "{F} ¿Cuántos °C subió la temperatura entre la primera y la última lectura?", "40-30", "Se resta la primera lectura a la última.", " °C"),
        ("abc", "{F} ¿Qué tendencia muestran las lecturas de temperatura?", "Suben de forma pareja", "Se mantienen estables", "Bajan de forma pareja", "Cada lectura es mayor que la anterior en la misma cantidad."),
        ("=", "{F} ¿Cuántos °C subió la temperatura por hora?", "(40-30)//5", "Se divide la subida total entre los cinco intervalos de una hora.", " °C"),
        ("=", "{F} ¿Cuántos °C faltan para que la última lectura llegue al límite máximo?", "60-40", "Se resta la última lectura al límite máximo.", " °C"),
        ("=", "{F} ¿Cuál es la temperatura promedio de las seis lecturas?", "(30+32+34+36+38+40)//6", "Se suman las seis lecturas y se divide entre 6.", " °C"),
        ("abc", "{F} ¿Quién aprueba el informe de la ficha?", "El profesional especialista", "El operador que mide", "El proveedor de los instrumentos", "El formato reserva un espacio para la aprobación del especialista."),
        ("=", "{F} Si la subida siguiera igual, ¿en cuántas horas más llegaría la temperatura al máximo desde la última lectura? Es una proyección, no una certeza.", "(60-40)//2", "Se divide lo que falta para el máximo entre lo que sube cada hora.", " horas"),
        ("abc", "{F} ¿Cuál de estas frases es una observación y no una opinión?", "La temperatura subió de 30 a 40 °C en cinco horas", "El tanque se está portando mal", "El turno anterior trabajó peor", "Una observación se apoya en datos medidos."),
        ("abc", "{F} Un operador escribe en el informe «hay que apagar todo ahora». ¿Qué corresponde?", "Anotar los datos y la tendencia, y dejar la decisión al profesional especialista", "Mantener la frase, porque el operador decide", "Borrar la tendencia para no alarmar", "El informe describe; la decisión es del especialista."),
        em("Escribes un informe de ejemplo en una oficina de la planta cuando oyes una alarma y alguien grita que un tanque de la sala vecina está botando humo.", 4),
    ],
    ctx=("abc", "Un supervisor de ejemplo te pide anotar ya las lecturas de las 15:00 y las 16:00, que aún no se miden, «porque siempre dan lo mismo». ¿Qué respondes?", "Que no: el informe solo registra lecturas realmente medidas", "Que sí, si coinciden con el promedio", "Que sí, si las firma otra persona", "Un informe con datos inventados deja de ser confiable."),
    sc=[
        ("En Química Industrial: ¿quién decide a partir del informe?", "El profesional especialista", "Quien informa describe y el especialista decide."),
        ("En Química Industrial: ¿qué es una proyección?", "Una estimación de lo que pasaría si la tendencia siguiera igual", "No es una certeza, solo una estimación para avisar."),
        ("¿Qué se hace si falta una lectura del turno?", "Se deja constancia de que falta; no se inventa", "El informe solo contiene lo realmente medido."),
    ],
    op=("Informe ficticio de «Química Demo Costa Norte»: temperatura de un tanque cada hora, en °C: 25, 25, 26, 25, 26. Límite de ejemplo de 10 a 40 °C. Escribe (a) qué tendencia describe la serie, (b) una observación apoyada en datos, (c) una frase que NO debería ir en el informe porque es una opinión, (d) quién debe aprobar el informe.",
        "(a) Se mantiene estable, con pequeñas variaciones de 1 °C. (b) La temperatura se mantuvo entre 25 y 26 °C en cinco horas, dentro del límite. (c) «El operador de este turno trabaja mal». (d) El profesional especialista.",
        ["describe la tendencia", "escribe una observación con datos", "reconoce una opinión", "nombra a quien aprueba"],
        ["hoja con las cuatro respuestas"],
        ["mezclar opinión y dato", "inventar una tendencia", "no mencionar al especialista"],
        "Pregunta: «¿qué dato apoya tu observación?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Escribe cinco lecturas de ejemplo y descríbelas con una frase de tendencia y una observación con datos.",
    extend="Explica con un ejemplo por qué un informe con una opinión puede confundir a quien lo aprueba.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (formato de ejemplo con datos inventados). Informe semanal de pH del estanque E5 de la planta ficticia «Química Demo Valle Claro». Periodo: lunes a viernes. Responsable: técnico de turno. Límite de ejemplo: de 6 a 8. "
     "Tabla de datos: lunes 7; martes 7; miércoles 7; jueves 6; viernes 8. Gráfico descrito: el eje horizontal muestra los días y el eje vertical muestra el pH; los puntos unen los valores de cada día. "
     "Observación del responsable: «el jueves el pH bajó a 6, que es el valor mínimo permitido; el viernes subió a 8, que es el valor máximo permitido».")
build(
    O3, 2, F,
    use="Aprenderé las partes de un informe de mediciones: tabla, gráfico, ejes, rango, promedio y observaciones, y cómo describir la variabilidad de los datos sin interpretar de más.",
    prior=["Sé qué es una tendencia y una observación.", "Sé calcular un promedio.", "Sé restar números enteros."],
    explain=[
        "En Química Industrial, los datos de un informe se presentan en una tabla, que ordena los valores en filas y columnas, y a menudo en un gráfico, donde el eje horizontal suele mostrar el tiempo y el eje vertical, la variable medida. El valor máximo es el mayor de la serie y el valor mínimo es el menor. El rango es la diferencia entre el máximo y el mínimo, y muestra cuánto varió la variable en el periodo.",
        "El promedio resume la serie en un solo número: se suman los datos y se divide entre cuántos son. Un promedio puede ocultar variaciones: dos series pueden tener el mismo promedio y una de ellas variar mucho más. Por eso un informe incluye también el máximo, el mínimo y el rango. La variabilidad es cuánto cambian los datos.",
        f"Un buen informe nombra el periodo, el responsable, el límite y la unidad, y describe sin exagerar. Este trabajo es de papel; no habilita a intervenir en equipos. {EMER} {AVISO}",
    ],
    vocab=[("tabla", "forma de ordenar datos en filas y columnas"), ("gráfico", "dibujo que muestra los datos con ejes"), ("eje", "línea del gráfico que muestra una magnitud, como el tiempo o el pH"), ("valor máximo y mínimo", "el mayor y el menor valor de una serie"), ("rango", "diferencia entre el valor máximo y el mínimo"), ("promedio", "suma de los datos dividida entre cuántos son"), ("variabilidad", "cuánto cambian los datos")],
    worked=[
        ("Rango", "Cuatro lecturas de ejemplo de caudal valen 22, 28, 25 y 31 L/min. ¿Cuál es el rango?", ["El máximo es 31 y el mínimo es 22.", "31 menos 22 son 9."], "9 L/min"),
        ("Promedio", "Cuatro lecturas de temperatura de ejemplo valen 10, 12, 14 y 16 °C. ¿Cuál es el promedio?", ["La suma es 10 más 12 más 14 más 16, que es 52.", "52 entre 4 son 13."], "13 °C"),
    ],
    mistakes=[("Informar solo el promedio y no el máximo y el mínimo.", "El promedio puede ocultar valores cercanos al límite.", "Incluye promedio, máximo, mínimo y rango."),
              ("Dar por estable una serie porque el promedio es redondo.", "La estabilidad se juzga mirando el rango y la tendencia, no solo el promedio.", "Describe la tendencia y la variabilidad con los datos.")],
    T=[
        ("abc", "En Química Industrial: ¿qué es el rango de una serie de datos?", "La diferencia entre el valor máximo y el mínimo", "El promedio de todos los datos", "El límite fijado por la empresa", "El rango mide cuánto varió la serie."),
        ("abc", "En Química Industrial: ¿qué suele mostrar el eje horizontal de un gráfico de mediciones?", "El tiempo, como los días o las horas", "La unidad del instrumento", "El nombre del responsable", "El eje horizontal ordena las lecturas en el tiempo."),
        ("abc", "En Química Industrial: ¿qué es la variabilidad?", "Cuánto cambian los datos", "El valor que más se repite", "La fecha del informe", "La variabilidad describe la dispersión de los datos."),
        ("=", "{F} ¿Cuál es el rango del pH semanal?", "8-6", "Se resta el valor mínimo al máximo de la tabla.", ""),
        ("=", "{F} ¿Cuál es el promedio del pH de la semana?", "(7+7+7+6+8)//5", "Se suman los cinco valores y se divide entre 5.", ""),
        ("abc", "{F} ¿Qué muestra el eje vertical del gráfico descrito?", "El pH", "Los días", "El responsable", "La ficha dice que el eje vertical muestra el pH."),
        ("abc", "{F} ¿En qué día el pH fue el valor mínimo?", "El jueves", "El miércoles", "El viernes", "El mínimo de la tabla es 6, anotado el jueves."),
        ("abc", "{F} ¿Por qué el informe debería indicar el máximo y el mínimo y no solo el promedio?", "Porque el promedio de 7 no muestra que el pH llegó a los dos extremos del límite", "Porque el promedio siempre está mal calculado", "Porque el máximo y el mínimo reemplazan a la firma", "El promedio puede ocultar valores cercanos al límite."),
        ("=", "{F} ¿Cuántos días de la semana el pH estuvo en 7?", "3", "Según la tabla, lunes, martes y miércoles marcaron 7.", " días"),
        ("abc", "{F} ¿Qué frase describe mejor la serie?", "Estable en 7 durante tres días, con una baja a 6 el jueves y una subida a 8 el viernes", "Sube de forma pareja durante toda la semana", "Baja de forma pareja durante toda la semana", "La descripción debe recoger lo que muestran los datos día a día."),
        ("abc", "{F} Un compañero escribe «el estanque se descontroló el jueves». ¿Qué corresponde?", "Reemplazarlo por «el jueves el pH fue 6, el mínimo permitido»", "Dejarlo porque es una buena síntesis", "Quitar el jueves del informe", "Se describe con el dato medido y sin juicios."),
        ("=", "{F} Otra semana de ejemplo tuvo pH 5, 7, 8, 7, 7. ¿Cuál fue su rango?", "8-5", "Se resta el mínimo al máximo.", ""),
        em("Revisas un informe de ejemplo en la oficina cuando alguien avisa que de la sala de estanques sale un olor muy fuerte y que se oye un ruido anormal.", 0),
    ],
    ctx=("abc", "Un profesional de ejemplo te dice: «Dos informes tienen el mismo promedio de pH, 7, así que son iguales». ¿Qué respondes?", "Que no necesariamente: hay que mirar el rango y la tendencia, porque pueden variar muy distinto", "Que sí, porque el promedio resume todo", "Que sí, si ambos tienen la misma firma", "Dos series pueden tener igual promedio y distinta variabilidad."),
    sc=[
        ("En Química Industrial: ¿cómo se calcula el rango?", "Máximo menos mínimo", "El rango es la distancia entre los extremos de la serie."),
        ("En Química Industrial: ¿qué se suma para calcular el promedio?", "Todos los datos de la serie", "Luego se divide entre cuántos son."),
        ("¿Por qué se incluyen máximo, mínimo y rango además del promedio?", "Porque el promedio puede ocultar variaciones", "Los extremos muestran qué tan cerca del límite se estuvo."),
    ],
    op=("Informe ficticio de «Química Demo Costa Norte» sobre la humedad de una bodega, en %: lunes 50; martes 52; miércoles 54; jueves 50; viernes 54. Límite de ejemplo de 40 a 60 %. Escribe (a) el máximo, el mínimo y el rango, (b) el promedio, (c) una frase que describa la serie sin opinar, (d) qué eje mostraría los días en un gráfico.",
        "(a) Máximo 54, mínimo 50 y rango 4 %. (b) 260 entre 5 son 52 %. (c) La humedad se mantuvo entre 50 y 54 %, dentro del límite, con variaciones de hasta 4 puntos. (d) El eje horizontal.",
        ["calcula máximo, mínimo y rango", "calcula el promedio", "describe sin opinar", "identifica el eje del tiempo"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "no dividir entre 5", "opinar en la frase"],
        "Pregunta: «¿qué dato apoya tu frase?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa seis lecturas de una variable, calcula máximo, mínimo, rango y promedio, y escribe una frase que las describa.",
    extend="Explica con un ejemplo por qué dos series con el mismo promedio pueden exigir decisiones distintas.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Registro horario del tanque T6 de la planta ficticia «Química Demo Valle Claro», de 08:00 a 15:00. Temperatura en °C (límite de ejemplo 20 a 60): 30; 31; 33; 35; 38; 42; 47; 53. "
     "Presión en kPa (límite de ejemplo 100 a 150): 110; 110; 111; 110; 110; 111; 110; 110. Caudal en L/min (límite de ejemplo 20 a 40): 40; 38; 36; 34; 32; 30; 28; 26. "
     "Las lecturas están en orden: la primera es de las 08:00, la segunda de las 09:00, y así hasta la octava, de las 15:00.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso con tres variables: describir la tendencia de cada una, detectar cuál exige aviso al especialista y escribir una observación clara y sin opiniones.",
    prior=["Sé qué es una tendencia, un rango y un límite.", "Sé restar y dividir números enteros.", "Sé separar observación de opinión."],
    explain=[
        "En Química Industrial, al analizar un caso con varias variables se describe cada una por separado y luego se comparan. Una variable puede subir, bajar, mantenerse estable u oscilar; además, puede cambiar a un ritmo parejo o cada vez más rápido. Si los aumentos crecen (1, 2, 2, 3, 4…), la variable no solo sube: acelera, y eso conviene avisarlo.",
        "Para decidir qué avisar, se compara el último dato con el límite y se mira hacia dónde va la tendencia. Una variable estable y lejos del límite no preocupa; una que se acerca al límite sí merece un aviso al profesional especialista. La observación se escribe con datos: qué variable, de cuánto a cuánto, en qué periodo y en qué unidad.",
        f"Describir tendencias no es operar el equipo: las decisiones sobre el proceso las toman el especialista y el personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("tendencia creciente", "los datos suben a lo largo del tiempo"), ("tendencia decreciente", "los datos bajan a lo largo del tiempo"), ("estable", "que se mantiene casi igual"), ("aceleración de un cambio", "cuando los aumentos o disminuciones son cada vez mayores"), ("aviso al especialista", "informe de que una variable se acerca a un límite o cambia de forma anormal")],
    worked=[
        ("Describir una variable", "Una temperatura de ejemplo va 40, 41, 41, 42 °C. ¿Cómo se describe?", ["Sube muy poco: 2 °C en total.", "Casi no cambia, es prácticamente estable."], "Prácticamente estable, con una subida de 2 °C"),
        ("Decidir un aviso", "Un caudal de ejemplo va 30, 28, 26, 24 L/min y su límite mínimo es 20. ¿Se avisa?", ["Baja 2 por lectura y ya está en 24.", "Se acerca al límite mínimo de 20, así que se avisa al especialista."], "Sí, se avisa porque se acerca al mínimo"),
    ],
    mistakes=[("Decir que una variable «sube parejo» sin mirar los aumentos entre lecturas.", "Los aumentos pueden ser cada vez mayores y eso indica aceleración.", "Calcula la diferencia entre cada lectura y la anterior."),
              ("No avisar porque la lectura todavía está dentro del límite.", "Una variable puede estar dentro del límite y acercarse rápido a él.", "Mira el valor, la tendencia y la distancia al límite.")],
    T=[
        ("abc", "En Química Industrial: ¿qué significa una tendencia decreciente?", "Los datos bajan a lo largo del tiempo", "Los datos suben a lo largo del tiempo", "Los datos se repiten sin cambio", "Decreciente significa que los valores disminuyen."),
        ("abc", "En Química Industrial: ¿cuándo se dice que un cambio se acelera?", "Cuando los aumentos o disminuciones son cada vez mayores", "Cuando las lecturas se hacen más seguido", "Cuando el instrumento cambia", "La aceleración se ve en diferencias cada vez más grandes."),
        ("abc", "En Química Industrial: ¿qué es un aviso al profesional especialista?", "Informar que una variable se acerca a un límite o cambia de forma anormal", "Cambiar el valor del límite", "Apagar el equipo por cuenta propia", "El aviso entrega información; la decisión es del especialista."),
        ("abc", "{F} ¿Qué tendencia muestra la presión?", "Estable en torno a 110 kPa", "Sube cada vez más rápido", "Baja de forma pareja", "La presión solo alterna entre 110 y 111."),
        ("=", "{F} ¿Cuántos L/min bajó el caudal entre las 08:00 y las 15:00?", "40-26", "Se resta la última lectura a la primera.", " L/min"),
        ("=", "{F} ¿Cuántos °C subió la temperatura entre las 08:00 y las 15:00?", "53-30", "Se resta la primera lectura a la última.", " °C"),
        ("abc", "{F} ¿Cómo cambia la temperatura de una hora a la siguiente?", "Los aumentos son cada vez mayores: 1, 2, 2, 3, 4, 5, 6", "Aumenta siempre 1 °C", "Disminuye cada hora", "Las diferencias entre lecturas crecen, por eso se acelera."),
        ("=", "{F} ¿Cuántos °C subió la temperatura entre las 14:00 y las 15:00?", "53-47", "Se resta la lectura de las 14:00 a la de las 15:00.", " °C"),
        ("abc", "{F} ¿A qué hora la temperatura superó por primera vez los 45 °C?", "A las 14:00, con 47 °C", "A las 13:00, con 42 °C", "A las 15:00, con 53 °C", "La primera lectura mayor que 45 es 47, de las 14:00."),
        ("=", "{F} Si el caudal sigue bajando 2 L/min por hora, ¿en cuántas horas llegaría al mínimo desde las 15:00? Es una proyección, no una certeza.", "(26-20)//2", "Se divide lo que falta para el mínimo entre lo que baja cada hora.", " horas"),
        ("abc", "{F} ¿Qué dos variables deberían avisarse al especialista?", "La temperatura, que acelera, y el caudal, que baja hacia su mínimo", "Solo la presión, porque es la más estable", "Ninguna, porque todas están dentro del límite", "Una variable dentro del límite puede acercarse a él con rapidez."),
        ("abc", "{F} ¿Cuál es la mejor observación para el informe?", "La temperatura subió de 30 a 53 °C y el caudal bajó de 40 a 26 L/min entre las 08:00 y las 15:00; la presión se mantuvo estable", "Todo anda mal en el tanque T6", "El tanque T6 no sirve", "La observación debe llevar variables, valores, periodo y unidades."),
        em("Analizas el registro de un tanque de ejemplo cuando alguien avisa que el tanque está caliente al tacto y que sale vapor por una válvula.", 5),
    ],
    ctx=("abc", "Un compañero de ejemplo dice: «Todo está dentro del límite, así que no hace falta avisar nada». ¿Qué le respondes?", "Que igual conviene avisar de la temperatura que acelera y del caudal que se acerca a su mínimo", "Que tiene razón, porque no hay valores fuera del límite", "Que solo debe avisar cuando haya una alarma", "Dentro del límite no significa sin riesgo si la tendencia se acerca."),
    sc=[
        ("En Química Industrial: ¿qué se compara para decidir un aviso?", "El último dato, el límite y la tendencia", "Con eso se ve si la variable se acerca al límite."),
        ("¿Cómo se ve que un aumento se acelera?", "Las diferencias entre lecturas son cada vez mayores", "Cada subida es mayor que la anterior."),
        ("En Química Industrial: ¿qué datos lleva una buena observación?", "Variable, valores, periodo y unidad", "Con esos datos la observación se puede verificar fácilmente."),
    ],
    op=("Registro ficticio de «Química Demo Costa Norte», de 08:00 a 12:00: temperatura en °C (límite de ejemplo 10 a 50): 20; 21; 23; 26; 30. Caudal en L/min (límite de ejemplo 15 a 40): 35; 35; 34; 35; 35. Escribe (a) qué tendencia tiene cada variable, (b) cuál debe avisarse y por qué, (c) una observación para el informe, (d) cuánto subió la temperatura en total.",
        "(a) La temperatura sube y acelera (1, 2, 3, 4 °C por hora); el caudal es estable. (b) La temperatura, porque acelera aunque está lejos del límite. (c) Entre las 08:00 y las 12:00 la temperatura subió de 20 a 30 °C y el caudal se mantuvo entre 34 y 35 L/min. (d) 10 °C.",
        ["describe las tendencias", "decide qué avisar", "redacta la observación con datos", "calcula la subida total"],
        ["hoja con las cuatro respuestas"],
        ["no ver la aceleración", "avisar solo por el límite", "redactar sin unidades"],
        "Pregunta: «¿cuánto subió la temperatura cada hora?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa dos variables con ocho lecturas cada una, descríbelas y decide cuál avisarías.",
    extend="Explica con un ejemplo por qué una variable dentro del límite puede merecer un aviso.",
)
