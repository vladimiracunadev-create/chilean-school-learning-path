"""Gastronomía TP 3.º medio (tronco): OAE-01 (solicitar, recepcionar, almacenar y rotular materias primas), OAE-02 (higienizar y limpiar) y OAE-03 (elaborar productos de baja complejidad). Todo en papel, solo conceptos, registros y cálculos: establecimientos, proveedores, cantidades y precios inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_gast_common import build

O1 = "TP-GAST-3-OAE-01"
O2 = "TP-GAST-3-OAE-02"
O3 = "TP-GAST-3-OAE-03"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: la práctica en cocina requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); no te habilita para trabajar."

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (cocina de un casino escolar de ejemplo, inventado). Etapas del flujo de las materias primas: solicitar, recibir, almacenar y rotular (estas dos últimas se hacen apenas llega el producto) y entregar a producción. "
     "La jefa de cocina define qué se necesita; el encargado de bodega recibe y almacena; el proveedor entrega junto con una guía de despacho. "
     "Reglas generales de la cocina: se recibe solo lo que se pidió, los alimentos crudos se guardan separados de los listos para comer y todo producto lleva rótulo. La autoridad sanitaria fiscaliza el cumplimiento de la norma sanitaria vigente.")
build(
    O1, 1, F,
    use="Aprenderé a situar el trabajo de bodega y recepción de una cocina: qué es una materia prima, cuáles son las etapas del flujo, qué riesgos hay y qué norma lo regula.",
    prior=["Sé sumar y restar cantidades.", "Sé leer una ficha con datos.", "Sé qué es una cocina de un casino o restaurante."],
    explain=[
        "En Gastronomía, las materias primas son los alimentos que se transforman para elaborar un plato, como papas, carne o harina. Los insumos son productos de apoyo que se consumen en la producción, como el aceite, la sal o los envases. Los materiales son elementos de trabajo, como bandejas o etiquetas. El stock es la cantidad de cada producto que hay en bodega.",
        "Las mercaderías siguen un flujo: se solicitan según lo que necesita la producción, se reciben comparándolas con lo pedido, se almacenan y se rotulan, y luego se entregan a la cocina. Cada etapa deja un registro escrito, que permite saber qué llegó, cuándo y quién lo manejó.",
        "Los riesgos principales son la contaminación cruzada (el paso de microbios de un alimento a otro), el vencimiento de productos y la mezcla de alimentos con sustancias de limpieza. La autoridad sanitaria fiscaliza que se cumpla la norma sanitaria vigente. Las reglas generales son recibir solo lo pedido, separar crudos de listos para comer y rotular todo." + LIM,
    ],
    vocab=[("materia prima", "alimento que se transforma para elaborar un plato"), ("insumo", "producto de apoyo que se consume en la producción, como aceite o envases"), ("material", "elemento de trabajo, como una bandeja o una etiqueta"), ("stock", "cantidad de un producto que hay en bodega"), ("guía de despacho", "documento con que el proveedor acompaña lo que entrega"), ("contaminación cruzada", "paso de microbios de un alimento a otro"), ("rótulo", "etiqueta que identifica un producto")],
    worked=[
        ("Clasificar un producto", "En una cocina de ejemplo se recibe un saco de arroz. ¿Es materia prima, insumo o material?", ["El arroz es un alimento que se transforma en un plato.", "Eso lo define como materia prima."], "Materia prima"),
        ("Ordenar dos etapas", "¿Qué etapa va primero en el flujo: solicitar o recibir?", ["Sin pedido no hay qué esperar del proveedor.", "Después de solicitar, se recibe lo que llega."], "Solicitar va primero"),
    ],
    mistakes=[("Guardar un producto sin rótulo porque «igual se sabe qué es».", "Otra persona no sabrá qué es ni cuándo vence, y el producto puede usarse mal.", "Rotula apenas recibes: nombre, fecha de recepción y fecha de vencimiento."),
              ("Recibir todo lo que llega sin compararlo con el pedido.", "Se pagan o se usan productos que nadie pidió y no queda registro de las diferencias.", "Compara siempre lo recibido con el pedido y la guía de despacho.")],
    T=[
        ("abc", "En Gastronomía: ¿cuál de estos productos es una materia prima?", "Un saco de papas que se transformará en una guarnición", "Un rollo de etiquetas adhesivas para rotular", "Una bandeja plástica para guardar alimentos", "La materia prima es el alimento que se transforma; las etiquetas y las bandejas son materiales de apoyo."),
        ("abc", "{F} ¿Quién recibe y almacena las mercaderías en esta cocina?", "El encargado de bodega", "La jefa de cocina", "El proveedor", "La ficha asigna la recepción y el almacenamiento al encargado de bodega; la jefa define lo que se necesita."),
        ("abc", "{F} ¿Cuál es el orden correcto de las tres primeras etapas del flujo?", "Solicitar, recibir y almacenar", "Recibir, solicitar y almacenar", "Almacenar, solicitar y recibir", "Primero se pide, porque sin pedido no hay qué recibir, y recién después se almacena."),
        ("abc", "{F} ¿Para qué se guardan los alimentos crudos separados de los listos para comer?", "Para evitar la contaminación cruzada entre ellos", "Para que los crudos se conserven más tiempo", "Para facilitar el conteo mensual del inventario", "La separación impide que los microbios de un alimento pasen a otro."),
        ("=", "En una solicitud semanal de ejemplo se piden 3 sacos de papas de 25 kg y 2 sacos de cebolla de 10 kg. ¿Cuántos kilos se solicitan en total?", "3*25+2*10", "Se calcula el peso de cada producto y se suman.", " kg"),
        ("abc", "En Gastronomía: ¿qué es un insumo?", "Un producto de apoyo que se consume en la producción, como el aceite", "El alimento principal que se transforma en un plato", "Un elemento reutilizable de trabajo, como una bandeja", "El insumo se consume en la producción sin ser el alimento principal ni un elemento reutilizable."),
        ("abc", "{F} Llegan 40 cajas de verdura y el pedido era de 35. ¿Qué corresponde hacer?", "Compararlas con el pedido y la guía de despacho y registrar la diferencia", "Recibirlas todas y guardarlas sin revisar, porque sobra mercadería", "Devolver todo el pedido sin dejar registro", "Se recibe lo pedido y se deja constancia de la diferencia para aclararla con el proveedor."),
        ("=", "En la bodega de ejemplo hay 12 cajas de lácteos. Entran 18 cajas y salen 7 hacia producción. ¿Cuántas cajas hay ahora en stock?", "12+18-7", "Al stock inicial se le suman las entradas y se restan las salidas.", " cajas"),
        ("abc", "Aparece en la bodega un envase abierto, sin rótulo ni fecha. ¿Qué corresponde hacer?", "Separarlo y consultar a la jefatura, sin usarlo hasta saber qué es", "Usarlo si el aspecto parece bueno", "Ponerle un rótulo con la fecha de hoy y guardarlo", "Sin identificación no se sabe qué es ni cuánto lleva abierto, así que no se usa."),
        ("abc", "Un compañero dice: «Este proveedor es de confianza, así que no hace falta revisar lo que entrega». ¿Qué respuesta es correcta?", "La revisión se hace siempre, porque deja un registro que respalda lo recibido", "Tiene razón, porque revisar retrasa la producción", "Solo se revisa cuando el proveedor es nuevo", "La confianza no reemplaza el control: el registro protege a la cocina ante cualquier diferencia."),
        ("abc", "¿Por qué cada etapa del flujo deja un registro escrito?", "Para saber qué se recibió, cuándo y quién lo manejó si surge un problema", "Para decidir el precio de venta de cada plato", "Para que el proveedor cobre antes", "El registro permite rastrear los productos, que es su función principal en la bodega."),
        ("=", "Se solicitaron 80 kg de harina. El proveedor entregó 3 sacos de 10 kg y 2 sacos de 15 kg. ¿Cuántos kilos faltan por recibir?", "80-(3*10+2*15)", "Al pedido se le resta el peso de lo entregado.", " kg"),
        ("abc", "{F} Llega un pedido en que una caja de yogur está abierta y rota, aunque el resto está en orden. ¿Qué decisión es adecuada?", "Registrar la caja dañada y no aceptarla, recibiendo el resto", "Aceptarla y usarla primero para que no se pierda", "Aceptar todo y dejar la caja rota en el estante de lácteos", "Un envase roto no garantiza la inocuidad del producto, así que se deja constancia y no se recibe."),
    ],
    ctx=("abc", "{F} Un día de mucho trabajo, el proveedor deja las cajas en la puerta de la cocina y se va sin que nadie las revise ni firme la guía. La jefa propone: «las guardamos así y vemos después». ¿Qué observación corresponde?", "La recepción se hace al momento, comparando con el pedido, porque después no se sabe si hay diferencias ni quién responde", "Es correcto, porque el proveedor ya entregó y no es responsabilidad de la cocina", "Basta con revisar solo las cajas de verdura", "Sin revisión inmediata no hay respaldo para reclamar diferencias ni garantizar lo recibido."),
    sc=[
        ("En Gastronomía: ¿cuáles son las etapas del flujo de las materias primas?", "Solicitar, recibir, almacenar y rotular, y entregar a producción", "Es el recorrido que sigue la mercadería desde el pedido hasta la cocina."),
        ("¿Qué se hace con un producto sin rótulo?", "Se separa y se consulta a la jefatura", "Sin rótulo no se sabe qué es ni cuándo vence."),
        ("¿Quién fiscaliza el cumplimiento de la norma sanitaria vigente?", "La autoridad sanitaria", "Es la institución que controla las condiciones sanitarias de los establecimientos."),
    ],
    op=("Un casino de ejemplo pidió 24 kg de arroz, 10 litros de leche y 6 cajas de huevos. El proveedor entregó 24 kg de arroz, 8 litros de leche y 6 cajas de huevos, y además un saco de azúcar que nadie pidió. "
        "Escribe: (a) qué diferencias hay con el pedido, (b) qué harías con el saco de azúcar, (c) qué documentos compararías y (d) una regla para evitar la contaminación cruzada al almacenar los huevos crudos y un postre listo para comer.",
        "(a) Faltan 2 litros de leche y sobra un saco de azúcar. (b) No recibirlo hasta consultar a la jefatura y registrar que no fue pedido. (c) La orden de compra (lo pedido) y la guía de despacho (lo entregado). (d) Guardar los huevos crudos separados y por debajo del postre listo para comer.",
        ["detecta las dos diferencias con el pedido", "indica los dos documentos que compara", "propone una regla de separación de crudos y listos para comer"],
        ["hoja con las cuatro respuestas"],
        ["decir que el azúcar extra se recibe porque «puede servir»", "olvidar registrar la diferencia de leche", "guardar el crudo sobre el alimento listo para comer"],
        "Pregunta: «¿qué pasaría si nadie registra los 2 litros que faltan?». Debe responder que se pagaría por algo no recibido."),
    reinforce="Escribe una lista de cuatro productos de una cocina inventada y clasifica cada uno como materia prima, insumo o material.",
    extend="Explica con un ejemplo inventado por qué el registro de cada etapa protege tanto a la cocina como al proveedor.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documentos de una compra de ejemplo, inventados). Orden de compra N.º 15 del Casino Escolar de Ejemplo al Proveedor Fresco de Ejemplo: 30 kg de papas, 12 kg de zanahorias, 20 litros de leche y 10 kg de arroz. "
     "Guía de despacho N.º 88: papas 30 kg, zanahorias 10 kg, leche 20 litros, arroz 10 kg. "
     "Factura (documento de cobro del proveedor) por lo pedido en la orden. Roles: la jefa de cocina firma la orden de compra; el encargado de bodega firma la recepción; el administrador revisa la factura antes de pagar.")
build(
    O1, 2, F,
    use="Aprenderé qué documentos se usan al solicitar y recibir mercaderías (orden de compra, guía de despacho, factura, tarjeta de inventario) y qué rol responde por cada uno.",
    prior=["Conozco el flujo solicitar, recibir, almacenar y rotular.", "Sé restar cantidades.", "Sé leer una tabla breve."],
    explain=[
        "La orden de compra es el documento donde la cocina solicita al proveedor qué productos necesita y en qué cantidad. La guía de despacho acompaña la entrega y detalla qué se entregó. La factura es el documento de cobro. Al recibir, se compara la orden con la guía y con lo que realmente llegó, y se anota cualquier diferencia en el registro de recepción.",
        "La tarjeta de inventario es una ficha por producto donde se anotan las entradas, las salidas y el stock. Las sumas y restas de esa ficha permiten saber cuánto hay sin contar a ojo. Una requisición interna es el formulario con que producción pide a bodega lo que necesita para elaborar.",
        "Cada documento tiene un responsable: la jefa de cocina decide qué se pide, el encargado de bodega verifica y firma la recepción, y el administrador controla el pago. Firmar un documento es asumir que los datos son verdaderos, por eso no se firma sin revisar." + LIM,
    ],
    vocab=[("orden de compra", "documento con que la cocina solicita productos al proveedor"), ("factura", "documento de cobro emitido por el proveedor"), ("registro de recepción", "ficha donde se anotan lo recibido y las diferencias"), ("tarjeta de inventario", "ficha por producto con entradas, salidas y stock"), ("requisición interna", "formulario con que producción pide productos a bodega"), ("diferencia", "cantidad que no coincide entre dos documentos")],
    worked=[
        ("Clasificar un documento", "Un transportista entrega un papel que detalla 20 cajas de tomates entregadas en la puerta. ¿Qué documento es?", ["Detalla lo que se entregó y viene con la mercadería.", "Eso corresponde a la guía de despacho."], "Una guía de despacho"),
        ("Detectar una diferencia", "La orden pide 50 kg de harina y la guía de despacho indica 45 kg. ¿Cuánto falta?", ["Se compara lo pedido con lo entregado.", "50 − 45 = 5."], "Faltan 5 kg"),
    ],
    mistakes=[("Firmar la recepción «para que el transportista se vaya» y revisar después.", "La firma indica que todo llegó conforme, y luego no se puede reclamar una diferencia.", "Revisa contra la orden antes de firmar y anota las diferencias."),
              ("Pagar la factura solo porque está emitida, sin comparar con la guía.", "Se puede pagar por productos que no llegaron o llegaron incompletos.", "Compara la factura con la orden y la guía antes de pagar.")],
    T=[
        ("abc", "En Gastronomía: ¿qué documento usa la cocina para solicitar productos al proveedor?", "La orden de compra", "La guía de despacho", "La factura", "La orden se emite antes de la entrega y expresa lo que la cocina necesita."),
        ("abc", "{F} ¿Quién firma la recepción de la mercadería?", "El encargado de bodega", "El administrador", "El proveedor", "La ficha asigna la firma de recepción al encargado de bodega, que verifica lo que llega."),
        ("abc", "{F} ¿Qué documento es la factura?", "El documento de cobro del proveedor", "El detalle de lo que se entregó", "La solicitud de productos de la cocina", "La factura es el cobro; la guía detalla la entrega y la orden es la solicitud."),
        ("=", "{F} ¿Cuántos kilos de zanahorias faltaron en la entrega respecto de la orden?", "12-10", "A la cantidad pedida se le resta la cantidad entregada.", " kg"),
        ("abc", "{F} ¿Qué documentos se comparan para detectar la diferencia de zanahorias?", "La orden de compra y la guía de despacho", "La factura y la tarjeta de inventario", "La guía de despacho y la requisición interna", "La diferencia aparece al contrastar lo pedido en la orden con lo entregado en la guía."),
        ("abc", "En Gastronomía: ¿para qué sirve la tarjeta de inventario de un producto?", "Para anotar sus entradas y salidas y saber cuánto stock hay", "Para solicitar el producto al proveedor", "Para cobrar el producto al cliente", "La tarjeta lleva el control de cuánto entra, cuánto sale y cuánto queda de cada producto."),
        ("=", "La tarjeta de inventario de aceite de ejemplo muestra stock inicial de 30 litros, una entrada de 20 litros y salidas de 8 y 6 litros. ¿Cuántos litros hay en stock?", "30+20-(8+6)", "Al stock inicial se suman las entradas y se restan todas las salidas.", " litros"),
        ("abc", "{F} El administrador recibe la factura por todos los productos pedidos. ¿Qué debe hacer antes de pagar?", "Compararla con la orden y con la guía de despacho, porque en la entrega faltaron zanahorias", "Pagarla completa, porque la factura es el documento oficial", "Pagarla solo cuando llegue el producto faltante", "La factura se cobra por lo pedido, pero la guía muestra una entrega menor; se aclara antes de pagar."),
        ("abc", "Producción necesita 5 kg de azúcar para una elaboración y debe pedirlos a bodega. ¿Qué documento corresponde?", "Una requisición interna", "Una orden de compra al proveedor", "Una factura", "La requisición es el pedido interno de producción a bodega."),
        ("abc", "{F} Un transportista pide al encargado de bodega firmar rápido la guía «porque va atrasado», sin que se revise el arroz. ¿Qué corresponde?", "Revisar lo recibido contra la orden antes de firmar, aunque tome unos minutos", "Firmar y revisar al día siguiente", "Firmar solo si el transportista conoce a la jefa", "La firma certifica que lo recibido coincide con lo pedido; sin revisión no hay respaldo."),
        ("abc", "Un practicante dice: «La guía de despacho y la factura son lo mismo, solo cambia el nombre». ¿Qué corrección es correcta?", "La guía detalla lo entregado y la factura es el documento de cobro; son distintas", "Tiene razón, ambas sirven para pagar", "La factura sirve para entregar y la guía para cobrar", "Cada documento cumple una función: acompañar la entrega o cobrarla."),
        ("=", "{F} La orden pide 20 litros de leche a $850 el litro (precio de ejemplo) y la guía confirma los 20 litros. ¿Cuánto debe cobrar la factura por la leche?", "20*850", "Se multiplica la cantidad entregada por el precio de cada litro.", " pesos"),
        ("abc", "El encargado de bodega nota que la guía dice 10 kg de arroz, pero el saco pesado marca 9 kg. ¿Qué corresponde?", "Anotar la diferencia en el registro de recepción y avisar a la jefatura", "Firmar igual, porque 1 kg es poco", "Cambiar el número de la guía con lápiz para que cuadre", "Se deja constancia de la diferencia real y no se altera el documento del proveedor."),
    ],
    ctx=("abc", "{F} El administrador pregunta quién se equivocó si las zanahorias llegaron incompletas y el pedido original no se encuentra por ninguna parte. ¿Qué enseñanza deja esta situación?", "Que la orden de compra debe quedar archivada, porque es el respaldo de lo que se pidió", "Que no hace falta archivar documentos si la entrega ya se hizo", "Que basta con guardar la factura", "Sin la orden no se puede probar qué se pidió, por lo que archivarla es parte del control."),
    sc=[
        ("En Gastronomía: ¿qué documento detalla lo que el proveedor entregó?", "La guía de despacho", "Acompaña la entrega y permite verificar lo recibido."),
        ("¿Quién firma la recepción en esta ficha?", "El encargado de bodega", "Es el responsable de verificar lo que llega a la bodega."),
        ("¿Qué se hace con una diferencia entre la orden y lo recibido?", "Se anota en el registro de recepción", "Dejar constancia permite reclamar o corregir con el proveedor."),
    ],
    op=("Documentos de ejemplo. Orden de compra: 40 kg de pollo, 15 kg de tomates y 25 litros de aceite. Guía de despacho: 40 kg de pollo, 15 kg de tomates y 20 litros de aceite. Factura: 40 kg de pollo, 15 kg de tomates y 25 litros de aceite. "
        "Escribe: qué diferencia existe y entre qué documentos, qué documento muestra lo realmente entregado, qué harías antes de que el administrador pague y qué dato anotarías en el registro de recepción.",
        "Hay una diferencia de 5 litros de aceite: la orden y la factura dicen 25 litros y la guía, que muestra lo entregado, dice 20 litros. Antes de pagar, el administrador debe aclarar con el proveedor y pagar solo lo entregado o esperar el faltante. En el registro de recepción se anota «aceite: faltan 5 litros según la guía».",
        ["detecta los 5 litros de diferencia", "identifica la guía como documento de lo entregado", "indica una acción antes del pago y el dato a registrar"],
        ["hoja con la diferencia, el documento, la acción y el registro"],
        ["decir que la factura prueba lo entregado", "no registrar la diferencia", "pagar sin aclarar"],
        "Pregunta: «¿cuál documento dice lo que realmente llegó?». Si responde la factura, repasa la función de la guía."),
    reinforce="Haz una tabla con tres documentos de la clase y escribe, para cada uno, quién lo emite y para qué sirve.",
    extend="Explica por qué firmar una guía sin revisar puede traer problemas a la cocina semanas después.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de recepción de ejemplo, inventado). Criterios del registro de la cocina (valores de ejemplo; los límites reales los fija la norma vigente): los lácteos deben llegar con al menos 10 días de vida útil restante, los productos refrigerados con una temperatura de hasta 5 °C, y los envases no pueden venir hinchados ni rotos. "
     "Llegada del proveedor: (a) 20 cajas de yogur con 3 días de vida útil restante; (b) 15 kg de pollo refrigerado que el termómetro marca en 9 °C; (c) 100 kg de papas en 4 sacos, completos y en buen estado; (d) 24 latas de tomate, de las cuales 2 están hinchadas.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de recepción: comparar cada producto con los criterios del registro y decidir si se acepta, se rechaza o se acepta en parte.",
    prior=["Conozco la orden de compra y la guía de despacho.", "Sé restar cantidades.", "Sé comparar un dato con un límite."],
    explain=[
        "Al recibir mercaderías se verifica cada producto con criterios del registro: la cantidad, la vida útil restante (el tiempo que le queda antes de su fecha de vencimiento), la temperatura en los refrigerados y el estado del envase. Cada criterio se compara con el límite que fija la cocina según la norma vigente. En este cuaderno los límites son de ejemplo.",
        "Hay tres decisiones posibles: aceptar si cumple todos los criterios, rechazar si incumple alguno importante y aceptar en parte si solo una porción del lote tiene problemas, como algunos envases dañados dentro de una caja grande. Siempre se anota la decisión y la causa en el registro de recepción.",
        "Un producto rechazado no se mezcla con los aceptados: se deja a un lado, identificado, hasta que el proveedor lo retire. Un envase hinchado o roto no se abre ni se prueba; solo se separa y se avisa a la jefatura. La cadena de frío es el mantenimiento continuo del frío en los productos refrigerados desde el proveedor hasta la cocina." + LIM,
    ],
    vocab=[("vida útil restante", "tiempo que queda antes de la fecha de vencimiento"), ("aceptar", "recibir el producto porque cumple los criterios"), ("rechazar", "no recibir el producto porque incumple un criterio importante"), ("aceptar en parte", "recibir solo la porción del lote que cumple"), ("cadena de frío", "mantención continua del frío en los refrigerados"), ("envase hinchado", "envase abultado, señal de que el producto no es seguro")],
    worked=[
        ("Decidir con un criterio", "En un registro de ejemplo, el criterio de vida útil restante de los jugos es de al menos 20 días y llega un lote con 30 días. ¿Se acepta?", ["Se compara el dato con el límite.", "30 es mayor que 20, así que cumple."], "Se acepta"),
        ("Aceptar en parte", "Llegan 12 cajas de galletas y 2 están mojadas y rotas. ¿Qué se hace?", ["Solo una parte del lote tiene problemas.", "Se rechazan las 2 dañadas y se aceptan las otras 10."], "Se acepta en parte: se aceptan 10 cajas"),
    ],
    mistakes=[("Aceptar el pollo refrigerado porque «se ve bien», aunque la temperatura supera el límite.", "El aspecto no muestra si se mantuvo la cadena de frío; el criterio manda.", "Compara la temperatura medida con el límite del registro y rechaza si lo supera."),
              ("Abrir una lata hinchada para ver si el contenido está bien.", "Un envase hinchado puede indicar un producto inseguro y abrirlo es un riesgo.", "Sepárala sin abrirla, regístrala y avisa a la jefatura.")],
    T=[
        ("abc", "{F} ¿Qué decisión corresponde para el yogur?", "Rechazarlo, porque llega con menos vida útil que el mínimo del registro", "Aceptarlo, porque todavía no vence", "Aceptarlo y usarlo primero", "Tiene 3 días de vida útil restante y el criterio exige al menos 10."),
        ("abc", "{F} ¿Qué decisión corresponde para el pollo refrigerado?", "Rechazarlo, porque la temperatura medida supera el límite", "Aceptarlo, porque el límite es una referencia y no una regla", "Aceptarlo si se cocina ese mismo día", "9 °C supera el límite de ejemplo de 5 °C y la cadena de frío se rompió."),
        ("abc", "{F} ¿Qué decisión corresponde para las papas?", "Aceptarlas, porque cumplen cantidad y estado", "Rechazarlas, porque no se midió su temperatura", "Aceptar solo dos sacos y dejar los otros para después", "Llegaron los 4 sacos en buen estado y ningún criterio se incumple."),
        ("=", "{F} Se aceptan las latas de tomate que no están hinchadas. ¿Cuántas latas se aceptan?", "24-2", "Del total de latas se restan las hinchadas.", " latas"),
        ("abc", "{F} ¿Qué se hace con las 2 latas hinchadas?", "Separarlas sin abrirlas, registrarlas y avisar a la jefatura", "Abrir una para ver si el contenido está bien", "Mezclarlas con las demás y usarlas primero", "Un envase hinchado se trata como riesgo: no se abre y se deja constancia."),
        ("abc", "En Gastronomía: ¿qué es la cadena de frío?", "El mantenimiento continuo del frío en los productos refrigerados", "El orden en que se ubican los productos en la bodega seca", "El tiempo máximo que un producto puede quedar en la puerta", "La cadena de frío exige que el producto no pierda el frío entre el proveedor y la cocina."),
        ("=", "{F} El proveedor cobra $1.200 por kilo de papas (precio de ejemplo). ¿Cuánto debe pagar la cocina por las papas aceptadas?", "100*1200", "Se multiplican los kilos aceptados por el precio de cada kilo.", " pesos"),
        ("abc", "{F} El proveedor dice: «El yogur está bien, pruébelo». ¿Qué respuesta corresponde?", "Que la decisión se basa en los criterios del registro y no en una prueba", "Que lo probará y decidirá según el sabor", "Que lo aceptará solo si le hacen un descuento", "Los criterios son objetivos y probar un producto no garantiza que sea seguro."),
        ("abc", "{F} El encargado de bodega quiere guardar el pollo rechazado en el refrigerador «mientras llega el proveedor». ¿Qué debe hacer?", "Mantenerlo separado e identificado como rechazado, sin mezclarlo con lo aceptado", "Guardarlo junto con los productos aceptados para conservar el frío", "Usarlo en los platos del día para no perderlo", "Un producto rechazado no debe confundirse con los que se aceptaron."),
        ("=", "{F} El pedido era de 20 cajas de yogur con 12 yogures cada una. Si se hubieran aceptado, ¿cuántos yogures habrían ingresado?", "20*12", "Se multiplican las cajas por los yogures de cada caja.", " yogures"),
        ("abc", "{F} Un compañero propone aceptar el yogur porque «igual se consume rápido en el casino». ¿Qué observación corresponde?", "El criterio de vida útil protege la calidad; no se acepta un producto que no cumple por conveniencia", "Tiene razón, porque el consumo rápido compensa la vida útil", "Solo se rechaza si el producto huele mal", "Un criterio importante no se salta por comodidad, y el olor no es el único indicador."),
        ("abc", "{F} Al medir la temperatura del pollo, un practicante dice que el termómetro «debe estar malo» porque el pollo llegó en caja térmica. ¿Qué corresponde?", "Repetir la medición con cuidado y, si se confirma, rechazar el producto", "Ignorar la medición y aceptar", "Aceptar si el transportista asegura que viajó frío", "La medición manda sobre las suposiciones; si se repite y supera el límite, se rechaza."),
        ("=", "{F} Si el registro de la cocina exige 10 días de vida útil y el yogur trae 3, ¿cuántos días le faltan para cumplir el mínimo?", "10-3", "Al mínimo exigido se le resta la vida útil que trae el producto.", " días"),
    ],
    ctx=("abc", "{F} Una jefa nueva dice: «Acepten todo, hoy faltan insumos y el servicio es en dos horas». ¿Qué debe responder el encargado de bodega?", "Que los criterios del registro se aplican igual, y que se informa a la jefa qué productos faltan para buscar alternativas", "Que acepta todo y deja el registro en blanco", "Que acepta solo lo que le parece bien, sin anotar nada", "La urgencia no justifica recibir lo que incumple; se registra y se buscan alternativas."),
    sc=[
        ("En Gastronomía: ¿qué decisiones posibles hay al recibir un producto?", "Aceptar, rechazar o aceptar en parte", "Dependen de cuánto cumple el lote con los criterios."),
        ("¿Se abre un envase hinchado para revisarlo?", "No, se separa y se avisa a la jefatura", "El envase hinchado es una señal de riesgo."),
        ("¿Dónde se anota la decisión y su causa?", "En el registro de recepción", "Así queda respaldo ante cualquier reclamo."),
    ],
    op=("Criterios de ejemplo de otra cocina: los lácteos exigen 8 días de vida útil restante, los refrigerados llegar a hasta 5 °C y los envases no pueden estar rotos. Llegan: 10 cajas de queso con 15 días de vida útil restante; 20 kg de pescado refrigerado que marca 7 °C; 30 kg de lentejas en sacos, uno de ellos con el envase roto (6 kg del total). "
        "Para cada producto escribe tu decisión (aceptar, rechazar o aceptar en parte), la causa y el dato que anotarías en el registro. Calcula cuántos kilos de lentejas se aceptan.",
        "Queso: se acepta, porque 15 días supera el mínimo de 8. Pescado: se rechaza, porque 7 °C supera 5 °C. Lentejas: se acepta en parte; se aceptan 24 kg (30 − 6) y se rechaza el saco roto. Se anota cada decisión y su causa en el registro de recepción.",
        ["compara cada dato con su criterio", "calcula 24 kg de lentejas aceptadas", "anota la decisión y la causa"],
        ["hoja con tres decisiones, causas y cálculo"],
        ["aceptar el pescado por su aspecto", "aceptar todas las lentejas", "no explicar la causa"],
        "Pregunta: «¿qué criterio incumple el pescado?». Si no lo identifica, vuelve a comparar el dato con el límite."),
    reinforce="Inventa tres productos con sus datos de llegada y decide aceptar, rechazar o aceptar en parte con un criterio escrito por ti.",
    extend="Explica por qué la cadena de frío se rompe aunque el producto parezca en buen estado.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (inventario de ejemplo, inventado). Tarjeta del arroz: stock inicial 40 kg; entrada de 25 kg; salidas de 18 kg, 12 kg y 9 kg. Stock mínimo (nivel bajo el cual se debe pedir): 20 kg. Stock objetivo (nivel al que se quiere volver al pedir): 60 kg. "
     "Lotes de leche en la bodega: el lote A vence en 5 días y el lote B vence en 12 días. Cada lote es un grupo de producto fabricado junto. "
     "Rótulo de ejemplo: nombre del producto, fecha de recepción, fecha de vencimiento y responsable.")
build(
    O1, 4, F,
    use="Aprenderé a llevar un inventario con una tarjeta, decidir cuándo reponer, usar primero lo que vence antes y rotular correctamente.",
    prior=["Conozco la tarjeta de inventario.", "Sé sumar y restar.", "Sé comparar dos números."],
    explain=[
        "El inventario permite saber cuánto hay de cada producto. El stock final se calcula así: stock inicial más las entradas, menos las salidas. El stock mínimo es el nivel bajo el cual se debe volver a pedir para no quedarse sin producto, y el stock objetivo es el nivel al que se quiere llegar al reponer. La cantidad a pedir es la diferencia entre el objetivo y el stock actual.",
        "Para usar los productos en el orden correcto existen dos reglas. PEPS significa primero en entrar, primero en salir: se usa antes lo que llegó antes. FEFO significa primero que vence, primero en salir: se usa antes lo que tiene la fecha de vencimiento más próxima. En alimentos perecibles se prefiere FEFO, porque lo que llegó antes puede vencer después.",
        "El rótulo identifica cada producto: nombre, fecha de recepción, fecha de vencimiento y responsable. Se coloca al recibir y debe quedar visible. Los sistemas pueden ser manuales, como una planilla en papel, o digitales; en ambos se registra cada entrada y salida para que el inventario coincida con lo que hay en bodega." + LIM,
    ],
    vocab=[("stock mínimo", "nivel bajo el cual se debe volver a pedir"), ("stock objetivo", "nivel al que se quiere llegar al reponer"), ("PEPS", "primero en entrar, primero en salir"), ("FEFO", "primero que vence, primero en salir"), ("lote", "grupo de producto fabricado junto"), ("inventario", "recuento de lo que hay de cada producto")],
    worked=[
        ("Calcular un stock final", "Una tarjeta de ejemplo de azúcar tiene stock inicial de 15 kg, una entrada de 10 kg y salidas de 4 kg y 6 kg. ¿Cuánto hay?", ["Stock final = inicial + entradas − salidas.", "15 + 10 − (4 + 6) = 15."], "15 kg"),
        ("Elegir con FEFO", "De un producto hay dos lotes: uno vence en 3 días y otro en 9 días. ¿Cuál se usa primero?", ["FEFO usa primero lo que vence antes.", "El de 3 días vence antes."], "El que vence en 3 días"),
    ],
    mistakes=[("Usar siempre el producto que llegó primero, sin mirar la fecha de vencimiento.", "Un lote más nuevo puede vencer antes y se perdería.", "En perecibles aplica FEFO: revisa el vencimiento de cada lote."),
              ("No registrar una salida pequeña «porque fue poco».", "El inventario deja de coincidir con la bodega y se pide de más o de menos.", "Registra todas las salidas, también las pequeñas.")],
    T=[
        ("abc", "En Gastronomía: ¿qué significa FEFO?", "Primero que vence, primero en salir", "Primero en entrar, primero en salir", "Primero en pedir, primero en pagar", "FEFO ordena el uso según la fecha de vencimiento más próxima."),
        ("=", "{F} ¿Cuántos kilos de arroz hay en stock después de la entrada y las tres salidas?", "40+25-(18+12+9)", "Al stock inicial se suma la entrada y se restan las salidas.", " kg"),
        ("abc", "{F} ¿Qué lote de leche se usa primero según FEFO?", "El lote A, que vence en 5 días", "El lote B, que vence en 12 días", "El que se pueda abrir más fácil", "FEFO usa primero el lote con el vencimiento más próximo."),
        ("abc", "{F} Si el stock de arroz fuera de 18 kg, ¿qué corresponde hacer?", "Pedir, porque está bajo el stock mínimo", "No pedir, porque aún queda arroz", "Esperar a que llegue a 0", "18 kg es menor que el mínimo de 20 kg, así que corresponde reponer."),
        ("=", "{F} Con el stock final del arroz (26 kg), ¿cuántos kilos hay que pedir para llegar al stock objetivo?", "60-26", "Al stock objetivo se le resta el stock actual.", " kg"),
        ("abc", "{F} ¿Qué datos lleva el rótulo de ejemplo de un producto?", "Nombre, fecha de recepción, fecha de vencimiento y responsable", "Solo el precio y el proveedor", "Solo el nombre del producto", "La ficha define esos cuatro datos para identificar el producto y su plazo."),
        ("abc", "En Gastronomía: de un lote de pan de molde, ¿por qué puede ser mejor FEFO que PEPS?", "Porque un lote que llegó después puede vencer antes", "Porque el pan más antiguo siempre vence antes", "Porque FEFO ahorra espacio en la bodega", "El orden de llegada no siempre coincide con el orden de vencimiento."),
        ("=", "La tarjeta de ejemplo de la harina muestra stock inicial de 80 kg, entradas de 50 kg y 30 kg, y salidas de 45 kg y 25 kg. ¿Cuántos kilos hay en stock?", "80+50+30-(45+25)", "Se suman todas las entradas y se restan todas las salidas.", " kg"),
        ("abc", "Una tarjeta indica 32 kg de lentejas, pero al contar en la bodega hay 29 kg. ¿Qué corresponde?", "Revisar los registros de entradas y salidas para encontrar la diferencia y anotarla", "Cambiar el número de la tarjeta a 29 sin más", "Dejar la tarjeta como está, porque 3 kg es poco", "Se busca el origen de la diferencia y se ajusta con constancia, no en silencio."),
        ("abc", "{F} Un encargado dice: «Uso primero la leche del lote B, porque llegó antes». ¿Qué corrección corresponde?", "Se usa el lote A, porque vence antes; la llegada no define el orden", "Tiene razón, porque PEPS es siempre mejor", "Da igual cuál se use", "La ficha indica que A vence en 5 días y B en 12, por lo que A debe salir antes."),
        ("abc", "Llega un lote de queso sin fecha visible en el envase. ¿Qué corresponde hacer?", "Consultar a la jefatura y no almacenarlo hasta saber su vencimiento", "Ponerle la fecha de recepción como si fuera el vencimiento", "Guardarlo sin rótulo para no perder tiempo", "Sin fecha de vencimiento no se puede aplicar FEFO ni asegurar la inocuidad."),
        ("=", "{F} Durante el mes se hicieron cuatro pedidos de arroz de 34 kg cada uno. ¿Cuántos kilos entraron por esos pedidos?", "34*4", "Se multiplica la cantidad de cada pedido por la cantidad de pedidos.", " kg"),
        ("abc", "{F} Una cocina tiene 19 kg de arroz, bajo el stock mínimo. ¿Es correcto esperar a que baje más antes de pedir?", "No: bajo el mínimo corresponde pedir, antes de quedarse sin producto", "Sí: se pide solo cuando se acaba", "Sí, porque el stock objetivo es el que manda", "El stock mínimo existe para avisar a tiempo, considerando que el proveedor demora en entregar."),
    ],
    ctx=("abc", "{F} Una cocina de ejemplo dejó el pedido de arroz para cuando llegara a 5 kg, y el proveedor demora dos días en entregar. El arroz se terminó antes de la llegada. ¿Qué se debió hacer?", "Pedir al llegar al stock mínimo, que considera el tiempo de entrega", "Pedir una cantidad menor cada vez", "No tener stock mínimo, para no almacenar de más", "El stock mínimo da margen para reponer antes de que se acabe el producto."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el stock final?", "Stock inicial más entradas, menos salidas", "Es el recuento de lo que entra y sale de la bodega."),
        ("¿Qué regla usa primero lo que vence antes?", "FEFO", "FEFO ordena según la fecha de vencimiento."),
        ("¿Qué indica el stock mínimo?", "Cuándo hay que pedir", "Es el nivel de aviso antes de quedarse sin producto."),
    ],
    op=("Tarjeta de ejemplo del aceite: stock inicial 50 litros; entrada de 30 litros; salidas de 14, 11 y 9 litros. Stock mínimo 30 litros y stock objetivo 70 litros. Hay dos lotes de salsa de tomate: el lote P vence en 20 días y el lote Q en 8 días. "
        "Calcula el stock final de aceite, di si hay que pedir y cuánto, indica qué lote de salsa usarías primero y por qué, y escribe los cuatro datos del rótulo que pegarías en un producto recién recibido.",
        "Stock final: 50 + 30 − (14 + 11 + 9) = 46 litros. No hay que pedir, porque 46 es mayor que el mínimo de 30. Se usa primero el lote Q, porque vence antes (FEFO). Rótulo: nombre, fecha de recepción, fecha de vencimiento y responsable.",
        ["calcula 46 litros", "decide pedir o no con el stock mínimo", "aplica FEFO y nombra los cuatro datos del rótulo"],
        ["hoja con cálculo, decisión, lote elegido y rótulo"],
        ["restar solo una salida", "pedir aunque supere el mínimo", "usar el lote que llegó antes sin mirar el vencimiento"],
        "Pregunta: «¿qué pasaría con el lote Q si usas primero el P?». Debe responder que podría vencer antes de usarse."),
    reinforce="Inventa una tarjeta de inventario con tres movimientos y calcula el stock final y si hay que pedir.",
    extend="Explica por qué en una cocina con muchos perecibles conviene más FEFO que PEPS.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (plan de limpieza de una cocina de ejemplo, inventado). Áreas: recepción, bodega, cocina y comedor. Cada área tiene una pauta con tareas, frecuencia (después de cada uso, diaria o semanal) y responsable. "
     "Los productos químicos de limpieza deben ser autorizados, estar en su envase original con rótulo, guardarse separados de los alimentos y nunca mezclarse entre sí. La autoridad sanitaria fiscaliza según la normativa sanitaria vigente.")
build(
    O2, 1, F,
    use="Aprenderé a situar la limpieza en una cocina: qué es limpiar y desinfectar, qué peligros existen, qué reglas generales rigen y quién fiscaliza.",
    prior=["Conozco el flujo de las materias primas.", "Sé leer una pauta con tareas.", "Sé calcular multiplicaciones simples."],
    explain=[
        "En Gastronomía, limpiar es retirar la suciedad visible de una superficie, un utensilio o un equipo; desinfectar es reducir los microorganismos (seres vivos muy pequeños que pueden enfermar) a un nivel seguro. Higienizar es limpiar y desinfectar. Las dos cosas son necesarias: una superficie puede verse limpia y aun así tener microorganismos que no se ven.",
        "Los peligros de una cocina son de tres tipos: físicos (por ejemplo, un trozo de plástico en la comida), químicos (por ejemplo, restos de un producto de limpieza en una superficie donde se apoyan alimentos) y biológicos (por ejemplo, microbios que pasan de un alimento crudo a uno listo para comer). Un plan de limpieza es el documento que ordena qué se limpia, cuándo y quién lo hace.",
        "Las reglas generales son usar solo productos químicos autorizados, mantenerlos en su envase original con rótulo, guardarlos lejos de los alimentos y no mezclarlos nunca. Se firma la pauta cuando la tarea se hace. Esta limpieza exige instructor y la norma vigente de la autoridad sanitaria." + LIM,
    ],
    vocab=[("limpiar", "retirar la suciedad visible"), ("desinfectar", "reducir los microorganismos a un nivel seguro"), ("higienizar", "limpiar y desinfectar"), ("microorganismo", "ser vivo muy pequeño que puede enfermar a las personas"), ("plan de limpieza", "documento que ordena qué se limpia, cuándo y quién"), ("peligro químico", "sustancia que puede dañar o contaminar, como un producto de limpieza mal usado")],
    worked=[
        ("Clasificar un peligro", "Un trozo pequeño de vidrio cae en una olla de ejemplo. ¿Qué tipo de peligro es?", ["El vidrio es un objeto, no un producto ni un microbio.", "Eso lo hace un peligro físico."], "Un peligro físico"),
        ("Distinguir dos acciones", "Un cocinero retira restos de comida de un mesón con un paño. ¿Está limpiando o desinfectando?", ["Retira suciedad visible.", "No se habla de reducir microorganismos."], "Está limpiando"),
    ],
    mistakes=[("Pensar que una superficie sin manchas ya está desinfectada.", "Los microorganismos no se ven; limpiar no los reduce necesariamente al nivel seguro.", "Sigue la pauta: limpiar y, cuando corresponde, desinfectar."),
              ("Pasar un producto de limpieza a una botella de bebida «por comodidad».", "Otra persona puede confundirlo con una bebida y usarlo mal.", "Mantén el producto en su envase original con rótulo.")],
    T=[
        ("abc", "En Gastronomía: ¿qué diferencia hay entre limpiar y desinfectar?", "Limpiar retira la suciedad visible; desinfectar reduce los microorganismos", "Limpiar reduce los microorganismos; desinfectar retira la suciedad visible", "Son lo mismo, solo cambia el producto", "Limpiar saca lo que se ve; desinfectar actúa sobre los microorganismos que no se ven."),
        ("abc", "{F} ¿Dónde deben guardarse los productos químicos de limpieza?", "Separados de los alimentos y en su envase original con rótulo", "Junto a los alimentos, para tenerlos a mano", "En cualquier botella vacía, para ahorrar envases", "La ficha exige separarlos de los alimentos y mantener el envase original rotulado."),
        ("abc", "{F} ¿Quién fiscaliza el cumplimiento de la normativa sanitaria vigente?", "La autoridad sanitaria", "El proveedor de alimentos", "La jefa de cocina", "La ficha atribuye la fiscalización a la autoridad sanitaria; la jefa dirige la cocina."),
        ("abc", "{F} ¿Qué dice la ficha sobre mezclar productos químicos?", "Que nunca se mezclan entre sí", "Que se pueden mezclar para limpiar mejor", "Que se mezclan solo si el personal tiene experiencia", "La regla general es no mezclar, sin excepciones por experiencia."),
        ("=", "{F} Una cocina de ejemplo tiene tareas diarias en tres áreas: 6 en cocina, 4 en comedor y 3 en bodega. Trabaja 6 días a la semana. ¿Cuántas tareas diarias se hacen en una semana?", "(6+4+3)*6", "Se suman las tareas diarias de las tres áreas y se multiplican por los días.", " tareas"),
        ("abc", "En Gastronomía: ¿cuál de estas situaciones es un peligro químico?", "Restos de producto de limpieza en una superficie donde se apoyarán alimentos", "Un trozo de plástico caído en la comida", "Microbios que pasan de una carne cruda a una ensalada", "El peligro químico es una sustancia como un producto de limpieza; las otras son física y biológica."),
        ("abc", "{F} Un ayudante tiene un producto de limpieza en su envase original, pero quiere pasarlo a otra botella porque es más cómoda. ¿Qué corresponde?", "Mantenerlo en su envase original rotulado", "Pasarlo a una botella de bebida limpia", "Pasarlo a un frasco sin rótulo si se usa solo ese día", "El envase original lleva el rótulo con las advertencias; otra botella puede causar confusiones."),
        ("abc", "{F} Una pauta indica «después de cada uso» para una tabla de trabajo. ¿Cuándo se limpia?", "Cada vez que se termina de usar, aunque se vuelva a usar más tarde", "Solo al final de la semana", "Solo cuando se ve sucia", "La frecuencia pide limpiar tras cada uso, sin esperar a que se vea sucia."),
        ("abc", "Un practicante dice: «Si una superficie se ve limpia, no hace falta desinfectarla». ¿Qué respuesta es correcta?", "Los microorganismos no se ven, por eso la pauta puede exigir también desinfectar", "Tiene razón, porque limpiar elimina todos los microbios", "Solo se desinfecta cuando hay clientes en el comedor", "Una superficie visualmente limpia puede tener microorganismos que no se ven."),
        ("abc", "Un compañero siente un malestar después de usar un producto de limpieza. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Esperar a ver si se le pasa", "Aplicarle un remedio casero que alguien recomienda", "Ante un malestar no se improvisan soluciones: se avisa a quienes pueden atenderlo."),
        ("abc", "Una compañera quiere usar un limpiador que no está autorizado porque «limpia más fuerte». ¿Qué corresponde?", "Usar solo productos autorizados, porque el plan y la norma lo exigen", "Usarlo si ya lo probó en su casa", "Usarlo solo en el comedor", "La autorización no depende de la fuerza del producto ni de la experiencia personal."),
        ("=", "Una pauta de ejemplo tiene 4 áreas con 8 tareas diarias cada una. En 6 días se firmaron 170 tareas. ¿Cuántas tareas quedaron sin firmar?", "4*8*6-170", "Se calculan las tareas previstas y se resta lo firmado.", " tareas"),
        ("abc", "{F} Un inspector pregunta cómo se demuestra que el comedor se limpió ayer. ¿Qué respuesta tiene respaldo?", "La pauta del área firmada con fecha y responsable", "El recuerdo del encargado", "Que no se ven manchas", "Un registro firmado con fecha es evidencia; la memoria o la apariencia no lo son."),
    ],
    ctx=("abc", "{F} Un día de mucho trabajo, la encargada decide no firmar la pauta de bodega porque «igual se limpió». ¿Qué problema se genera?", "No queda evidencia de que se hizo, por lo que no se puede demostrar ni detectar fallas", "Ninguno, porque el trabajo ya está hecho", "Solo molesta a la jefatura", "Sin firma no hay forma de probar que la tarea se hizo ni de revisar qué falló."),
    sc=[
        ("En Gastronomía: ¿qué es desinfectar?", "Reducir los microorganismos a un nivel seguro", "Los microbios no se ven, por eso no basta limpiar."),
        ("¿Cómo se guardan los productos químicos de limpieza?", "En su envase original rotulado y lejos de los alimentos", "Así se evitan confusiones y contaminaciones."),
        ("¿Cuándo se firma la pauta?", "Cuando la tarea ya se hizo", "Firmar antes sería un registro falso."),
    ],
    op=("Una cocina de ejemplo tiene este problema: un ayudante nuevo propone mezclar dos limpiadores «para hacerlo todo de una pasada» y guardarlos juntos en una botella de agua mineral vacía. "
        "Escribe: (a) tres reglas generales de seguridad que se están incumpliendo, (b) la diferencia entre limpiar y desinfectar con un ejemplo de una mesa de trabajo, y (c) qué harías si un compañero se siente mal después de usar un producto.",
        "(a) No se mezclan productos; deben estar en su envase original rotulado; no se guardan en botellas de bebida. (b) Limpiar es retirar la suciedad visible de la mesa; desinfectar es reducir los microorganismos que no se ven. (c) Avisar de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios.",
        ["nombra al menos tres reglas incumplidas", "distingue limpiar de desinfectar con un ejemplo", "indica avisar a un adulto responsable y a emergencias"],
        ["hoja con las tres respuestas"],
        ["dar instrucciones de cómo mezclar productos", "decir que limpiar y desinfectar son lo mismo", "proponer un remedio casero"],
        "Pregunta: «¿qué podría pasar si alguien toma esa botella creyendo que es agua?». Debe reconocer el riesgo de intoxicación y la importancia del rótulo."),
    reinforce="Haz una lista de cinco reglas de seguridad para productos de limpieza y marca cuál se refiere a guardar, cuál a rotular y cuál a no mezclar.",
    extend="Explica por qué una pauta firmada también protege a la persona que limpia.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (etiqueta y documentos de ejemplo, inventados). Etiqueta de un «Limpiador Universal de Ejemplo» (producto inventado): uso en superficies lavables; advertencias: no mezclar con otros productos, mantener fuera del alcance de niños, usar guantes; "
     "ante contacto con ojos o ingestión, avisar de inmediato a un adulto responsable y a los servicios de emergencia; guardar en su envase original. "
     "Ficha de datos de seguridad: documento del fabricante con los riesgos del producto y las medidas de seguridad. Pauta de limpieza: tarea, frecuencia, responsable y firma. "
     "Roles: la jefa de cocina asigna las tareas; el encargado de limpieza las ejecuta; el prevencionista de riesgos revisa el plan y capacita en seguridad.")
build(
    O2, 2, F,
    use="Aprenderé a leer una etiqueta, una ficha de datos de seguridad y una pauta de limpieza, y a reconocer los roles y los elementos de protección personal.",
    prior=["Distingo limpiar y desinfectar.", "Conozco los tres tipos de peligro.", "Sé multiplicar y restar."],
    explain=[
        "La etiqueta del envase informa para qué sirve el producto, sus advertencias y qué hacer ante un accidente. La ficha de datos de seguridad es un documento del fabricante con información más completa sobre sus riesgos y las medidas de seguridad. Antes de usar un producto se leen ambas; no se usa un producto que no se sabe qué es.",
        "Un elemento de protección personal (EPP) es una prenda o accesorio que protege a quien trabaja, como guantes o delantal. Se usan los que indican la etiqueta y el prevencionista de riesgos, que es el profesional que revisa las condiciones de seguridad y capacita al personal. El control de plagas, es decir, de insectos y roedores, lo hace una empresa autorizada y no el personal de cocina.",
        "La pauta de limpieza registra qué tarea se hizo, cuándo, quién la hizo y su firma. Cada rol tiene su responsabilidad: la jefa asigna, el encargado ejecuta y el prevencionista revisa. Un registro debe ser verdadero: nunca se completa antes de hacer la tarea." + LIM,
    ],
    vocab=[("etiqueta", "información impresa en el envase sobre uso y advertencias"), ("ficha de datos de seguridad", "documento del fabricante con riesgos y medidas de seguridad"), ("EPP", "elemento de protección personal, como guantes o delantal"), ("prevencionista de riesgos", "profesional que revisa la seguridad y capacita al personal"), ("control de plagas", "manejo de insectos y roedores por una empresa autorizada"), ("pauta de limpieza", "registro de tarea, frecuencia, responsable y firma")],
    worked=[
        ("Buscar un dato en la etiqueta", "Una etiqueta de ejemplo dice «guardar en su envase original». ¿Es una advertencia sobre el uso o sobre el almacenamiento?", ["La instrucción se refiere a dónde y cómo mantener el producto.", "Eso es almacenamiento."], "Sobre el almacenamiento"),
        ("Identificar un EPP", "De estos elementos, ¿cuál es un EPP: guantes o una escoba?", ["Un EPP protege a la persona que trabaja.", "Los guantes protegen las manos; la escoba es un utensilio."], "Los guantes"),
    ],
    mistakes=[("Guiarse solo por el olor para saber si un producto es «el mismo de siempre».", "El olor no identifica el producto ni sus riesgos; para eso están el rótulo y la etiqueta.", "Lee siempre la etiqueta y usa solo productos identificados."),
              ("Completar la pauta de la semana el lunes, antes de hacer las tareas.", "Es un registro falso y no permite detectar tareas pendientes.", "Firma cada tarea cuando se hace, con fecha y responsable.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es una ficha de datos de seguridad?", "Un documento del fabricante con los riesgos del producto y las medidas de seguridad", "Una lista de las tareas de limpieza de cada día", "El permiso que entrega la autoridad sanitaria al local", "La ficha de datos reúne los riesgos y medidas del producto; la pauta es otra cosa."),
        ("abc", "{F} ¿Qué advierte la etiqueta sobre su uso con otros productos?", "Que no debe mezclarse con otros productos", "Que mejora al mezclarlo con otro limpiador", "Que solo debe evitarse mezclarlo con alimentos", "La etiqueta de ejemplo prohíbe mezclarlo con otros productos, sin excepciones."),
        ("abc", "{F} ¿Quién ejecuta las tareas de limpieza?", "El encargado de limpieza", "La jefa de cocina", "El prevencionista de riesgos", "La ficha indica que el encargado ejecuta lo que la jefa asigna."),
        ("abc", "{F} ¿Para qué sirven los guantes que pide la etiqueta?", "Son un EPP que evita el contacto del producto con la piel", "Reemplazan el lavado de manos al terminar", "Sirven para saber quién limpió", "Los guantes son elementos de protección personal frente al producto."),
        ("=", "La pauta semanal de ejemplo tiene 7 tareas diarias de lunes a sábado y 3 el domingo. ¿Cuántas tareas hay en la semana?", "7*6+3", "Se multiplican las tareas diarias por seis días y se suman las del domingo.", " tareas"),
        ("abc", "En Gastronomía: ¿qué es un EPP?", "Un elemento de protección personal, como guantes o delantal", "Un equipo pesado de producción", "Un producto de limpieza autorizado", "El EPP protege a la persona, no es un equipo ni un producto."),
        ("abc", "{F} Un ayudante no recuerda qué hacer si el producto cae en los ojos. ¿Qué corresponde?", "Leer la etiqueta y avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Preguntar a un compañero cómo lo resolvió una vez", "Probar un método casero", "La etiqueta indica avisar y pedir ayuda; no se improvisan remedios."),
        ("abc", "{F} ¿Quién revisa el plan de limpieza y capacita al personal en seguridad?", "El prevencionista de riesgos", "El proveedor del producto", "El encargado de limpieza", "La ficha asigna la revisión y la capacitación al prevencionista."),
        ("=", "Una pauta de ejemplo tiene 5 áreas con 6 tareas diarias cada una. Hoy se firmaron 24 tareas. ¿Cuántas tareas faltan por firmar?", "5*6-24", "Se calculan las tareas previstas del día y se resta lo firmado.", " tareas"),
        ("abc", "{F} La jefa dice que «basta con leer la etiqueta» y no hace falta tener la ficha de datos de seguridad. ¿Qué observación corresponde?", "La ficha tiene información más completa sobre riesgos y medidas; conviene tenerla disponible", "Tiene razón, porque la etiqueta siempre contiene todo", "La ficha sirve solo para calcular el pago al proveedor", "La etiqueta resume; la ficha del fabricante detalla riesgos y medidas de seguridad."),
        ("abc", "En Gastronomía: un técnico llega a controlar plagas en el local y quiere aplicar un producto sin identificarse. ¿Qué corresponde?", "Verificar que sea una empresa autorizada y registrar su visita", "Dejarlo trabajar porque conoce su oficio", "Pedir al personal de cocina que aplique el producto", "El control de plagas lo hace una empresa autorizada y debe quedar registrado."),
        ("abc", "{F} Un compañero cree que una pauta firmada sin fecha igual sirve. ¿Qué respuesta es correcta?", "No: sin fecha no se sabe cuándo se hizo la tarea", "Sí, porque la firma basta", "Sí, si la jefa recuerda cuándo fue", "La pauta debe indicar tarea, responsable y fecha para ser evidencia."),
        ("abc", "{F} Un practicante escribe «hecho» en todas las tareas de la semana el lunes, antes de hacerlas. ¿Cuál es el problema?", "Es un registro falso: la pauta se firma cuando la tarea se hace", "Ninguno, porque ahorra tiempo", "Solo es un problema si hay fiscalización", "Un registro anticipado no refleja lo ocurrido y oculta tareas pendientes."),
    ],
    ctx=("abc", "{F} Una auxiliar nueva encuentra bajo el lavaplatos un envase de producto sin etiqueta. ¿Qué debe hacer?", "No usarlo, informar al encargado y esperar que se identifique", "Usarlo si huele a limpiador", "Guardarlo en otro lugar sin avisar", "Sin etiqueta no se conocen el contenido ni sus riesgos, por lo que no se usa."),
    sc=[
        ("En Gastronomía: ¿qué es un EPP?", "Un elemento de protección personal", "Protege a la persona que trabaja frente a un riesgo."),
        ("¿Dónde se mira cómo actuar ante un accidente con un producto?", "En la etiqueta y la ficha de datos de seguridad", "Ahí el fabricante indica los riesgos y las medidas."),
        ("¿Quién hace el control de plagas?", "Una empresa autorizada", "Requiere personal con autorización y registro."),
    ],
    op=("Etiqueta de ejemplo de un «Desengrasante de Ejemplo» (inventado): uso en superficies de cocina; usar guantes y delantal; no mezclar con otros productos; guardar en su envase original, lejos de alimentos; ante contacto con los ojos o ingestión, avisar de inmediato a un adulto responsable y a emergencias. "
        "Escribe: los dos EPP que pide, dos advertencias de almacenamiento o mezcla, qué hacer ante un accidente y a qué documento del fabricante recurrirías para más información.",
        "EPP: guantes y delantal. Advertencias: no mezclar con otros productos y guardar en su envase original, lejos de alimentos. Ante un accidente: avisar de inmediato a un adulto responsable y a emergencias. Documento: la ficha de datos de seguridad.",
        ["nombra los dos EPP de la etiqueta", "recoge dos advertencias de la etiqueta", "indica avisar a un adulto responsable y a emergencias y nombra la ficha de datos de seguridad"],
        ["hoja con cuatro respuestas"],
        ["inventar EPP que la etiqueta no pide", "dar consejos médicos", "no nombrar la ficha de datos"],
        "Pregunta: «¿dónde dice la etiqueta que debe guardarse?». Si no lo encuentra, vuelve a leer el enunciado."),
    reinforce="Inventa la etiqueta de un producto de limpieza con cuatro advertencias y márcalas como uso, almacenamiento o accidente.",
    extend="Explica por qué la ficha de datos de seguridad debe estar al alcance de todo el personal que usa el producto.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (registro de limpieza del martes en una cocina de ejemplo, inventado). La pauta tenía 10 tareas ese día y se firmaron 8. Meta de cumplimiento de ejemplo: al menos 90 % de las tareas firmadas. "
     "Observaciones del supervisor: (1) una misma esponja se usó para la mesa de carnes crudas y luego para el mesón de ensaladas; (2) un frasco de detergente sin rótulo estaba en un estante, junto a un saco de azúcar; "
     "(3) la pauta del comedor estaba sin firma ni fecha; (4) las tareas de la cocina estaban firmadas con hora y responsable.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un registro de limpieza: calcular el cumplimiento, clasificar los hallazgos y proponer acciones correctivas.",
    prior=["Distingo peligros físicos, químicos y biológicos.", "Sé calcular un porcentaje.", "Sé leer una pauta de limpieza."],
    explain=[
        "Analizar un registro de limpieza significa comparar lo hecho con lo previsto. El porcentaje de cumplimiento se calcula con las tareas firmadas multiplicadas por 100 y divididas por las tareas previstas. Se compara con la meta del establecimiento. Además se revisan los hallazgos: situaciones que el supervisor observa y que se apartan de la norma o del plan.",
        "Cada hallazgo se clasifica: contaminación cruzada si un utensilio pasa de una zona sucia a una limpia, riesgo químico si un producto de limpieza está cerca de alimentos o sin rótulo, y falla de registro si falta una firma, una fecha o un responsable. Una acción correctiva es lo que se hace para eliminar la causa de un hallazgo y evitar que se repita.",
        "Una regla general es limpiar de las zonas más limpias a las más sucias y de arriba hacia abajo, para no volver a ensuciar lo ya limpio. También se usan utensilios de limpieza separados para zonas de alimentos crudos y listos para comer." + LIM,
    ],
    vocab=[("cumplimiento", "parte de las tareas previstas que se firmó como hecha"), ("meta", "porcentaje mínimo que se espera cumplir"), ("hallazgo", "situación observada que se aparta de la norma o del plan"), ("acción correctiva", "medida para eliminar la causa de un hallazgo"), ("contaminación cruzada", "paso de microbios de una zona o alimento a otro"), ("falla de registro", "falta de firma, fecha o responsable en un documento")],
    worked=[
        ("Calcular el cumplimiento", "En otra cocina de ejemplo se firmaron 15 de 20 tareas. ¿Qué porcentaje de cumplimiento tiene?", ["Se multiplican las firmadas por 100 y se divide por las previstas.", "15 × 100 ÷ 20 = 75."], "75 %"),
        ("Clasificar un hallazgo", "Un trapo se usa para limpiar un piso sucio y luego una mesa de servicio. ¿Qué tipo de hallazgo es?", ["Un utensilio pasa de una zona sucia a una limpia.", "Eso es contaminación cruzada."], "Contaminación cruzada"),
    ],
    mistakes=[("Corregir solo el síntoma, por ejemplo limpiar de nuevo la mesa, sin cambiar la esponja compartida.", "La causa sigue ahí y el hallazgo se repetirá.", "Define una acción correctiva que elimine la causa, como utensilios separados."),
              ("Subir el cumplimiento firmando tareas que no se hicieron.", "Es un registro falso y oculta las fallas reales.", "Firma solo lo verificado y analiza por qué no se hicieron las demás.")],
    T=[
        ("abc", "{F} ¿Cuál de las observaciones es un caso de contaminación cruzada?", "La esponja usada en la mesa de carnes crudas y luego en el mesón de ensaladas", "El frasco de detergente sin rótulo", "La pauta del comedor sin firma", "La esponja lleva microbios desde un alimento crudo a una zona de alimentos listos."),
        ("abc", "{F} ¿Cuál de las observaciones es un riesgo químico?", "El frasco sin rótulo junto al saco de azúcar", "La pauta del comedor sin firma", "Las tareas de cocina firmadas con hora", "Un producto sin identificar junto a un alimento puede contaminarlo o confundirse con él."),
        ("abc", "{F} ¿Cuál de las observaciones es una falla de registro?", "La pauta del comedor sin firma ni fecha", "La esponja compartida", "El frasco sin rótulo", "Falta firma y fecha, que son datos que debe tener todo registro."),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tuvo la pauta del martes?", "8*100//10", "Se multiplican las tareas firmadas por 100 y se dividen por las previstas.", " %"),
        ("=", "{F} ¿Cuántas tareas quedaron sin firmar el martes?", "10-8", "A las tareas previstas se les restan las firmadas.", " tareas"),
        ("abc", "{F} ¿Se cumplió la meta de ejemplo el martes?", "No, porque el cumplimiento fue menor que 90 %", "Sí, porque se firmó la mayoría de las tareas", "Sí, porque la cocina firmó con hora y responsable", "La meta exige al menos 90 % y el martes llegó al 80 %."),
        ("abc", "{F} ¿Qué acción correctiva elimina la causa del hallazgo de la esponja?", "Usar utensilios de limpieza separados para zonas de crudos y de listos para comer", "Enjuagar la esponja y seguir usándola", "Cambiar la esponja cada semana", "La causa es compartir el utensilio entre zonas; separarlos evita el paso de microbios."),
        ("abc", "{F} ¿Qué corresponde hacer con el frasco sin rótulo?", "Retirarlo del estante junto al azúcar, no usarlo y consultar al encargado", "Ponerle el nombre que parezca y seguir usándolo", "Pasarlo a otro estante de la bodega", "Sin rótulo no se sabe qué es, y nunca debe quedar cerca de alimentos."),
        ("abc", "En Gastronomía: ¿en qué orden se limpia una zona, como regla general?", "De las zonas más limpias a las más sucias y de arriba hacia abajo", "De las zonas más sucias a las más limpias y de abajo hacia arriba", "En el orden que prefiera quien limpia", "Así lo ya limpio no se vuelve a ensuciar con la suciedad que cae o se arrastra."),
        ("=", "Otra pauta de ejemplo tiene 20 tareas previstas el miércoles y se firmaron 18. ¿Qué porcentaje de cumplimiento tuvo?", "18*100//20", "Se multiplican las firmadas por 100 y se dividen por las previstas.", " %"),
        ("abc", "{F} Un jefe propone firmar de memoria la pauta del comedor para llegar a la meta. ¿Qué respuesta es correcta?", "Firmar solo lo que se verificó, porque un registro falso oculta las fallas", "Firmarla, porque lo importante es cumplir la meta", "Firmarla si el encargado cree recordar que se hizo", "El registro debe reflejar lo realmente hecho; una firma sin verificar lo falsea."),
        ("abc", "{F} Si solo se pudiera corregir un hallazgo antes del servicio, ¿cuál evita directamente que una sustancia de limpieza llegue a un alimento?", "Retirar el frasco sin rótulo del estante junto al azúcar", "Firmar la pauta del comedor", "Reemplazar la esponja por una nueva", "El frasco está al lado de un alimento; retirarlo elimina ese riesgo inmediato."),
        ("=", "{F} Si 5 áreas tienen 10 tareas diarias y el cumplimiento fue de 80 % durante 6 días, ¿cuántas tareas se firmaron en total?", "5*10*6*80//100", "Se calculan las tareas previstas y se toma el 80 % de ellas.", " tareas"),
    ],
    ctx=("abc", "{F} El supervisor llega durante el servicio y encuentra el frasco sin rótulo en uso sobre el mesón de preparación. ¿Qué corresponde primero?", "Detener su uso, retirarlo del área de alimentos y avisar al encargado", "Terminar el servicio y avisar después", "Rotularlo con un nombre para que siga en uso", "Hay riesgo inmediato para los alimentos, así que se detiene su uso y se informa."),
    sc=[
        ("En Gastronomía: ¿cómo se calcula el porcentaje de cumplimiento?", "Tareas firmadas por 100, dividido por las previstas", "Expresa la parte cumplida sobre el total previsto."),
        ("En gastronomía: ¿qué es una acción correctiva?", "Una medida que elimina la causa del hallazgo", "Si solo se arregla el síntoma, el problema se repite."),
        ("¿Qué falta en una falla de registro?", "Una firma, una fecha o un responsable", "Sin esos datos el registro no sirve como evidencia."),
    ],
    op=("Registro de ejemplo del jueves en otra cocina: 12 tareas previstas, 9 firmadas, meta de ejemplo de 90 %. Observaciones: un delantal sucio colgado junto a las verduras limpias; un recipiente de limpiador guardado en el estante de las especias; la pauta de bodega sin responsable. "
        "Calcula el cumplimiento, di si cumple la meta, clasifica las tres observaciones (contaminación cruzada, riesgo químico o falla de registro) y propone una acción correctiva para una de ellas.",
        "Cumplimiento: 9 × 100 ÷ 12 = 75 %, por lo que no cumple la meta de 90 %. El delantal junto a verduras limpias es contaminación cruzada; el limpiador junto a las especias es un riesgo químico, y la pauta sin responsable es falla de registro. Acción: colgar los delantales en un lugar alejado de los alimentos.",
        ["calcula 75 % y compara con la meta", "clasifica las tres observaciones con criterio", "propone una acción que elimina la causa"],
        ["hoja con cálculo, clasificación y acción correctiva"],
        ["decir que cumple la meta con 75 %", "confundir falla de registro con riesgo químico", "proponer una acción que no cambia la causa"],
        "Pregunta: «¿esa acción evita que se repita?». Si solo limpia de nuevo, ayúdale a buscar la causa."),
    reinforce="Inventa un registro con diez tareas y tres hallazgos, calcula el cumplimiento y clasifica cada hallazgo.",
    extend="Explica la diferencia entre una acción correctiva y una simple repetición de la limpieza.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (control mensual de limpieza de ejemplo, inventado). Tareas diarias: cocina 10, bodega 4 y comedor 5. Cada área funciona 5 días a la semana y se mide un mes de 4 semanas. "
     "Tareas firmadas en el mes: cocina 180, bodega 60 y comedor 100. Meta de ejemplo: al menos 90 % por área. "
     "Un envase de 5 litros de limpiador de ejemplo rinde 20 usos (dato de ejemplo) y cuesta $9.000.")
build(
    O2, 4, F,
    use="Aprenderé a controlar el cumplimiento de la limpieza de un mes, comparar áreas con una meta y estimar el uso y costo de productos.",
    prior=["Sé calcular porcentajes.", "Conozco hallazgos y acciones correctivas.", "Sé multiplicar y dividir."],
    explain=[
        "Un control mensual compara, para cada área, las tareas previstas con las tareas firmadas. Las tareas previstas se calculan multiplicando las tareas diarias por los días de trabajo de la semana y por las semanas del mes. El cumplimiento de cada área es la razón entre las firmadas y las previstas, expresada como porcentaje.",
        "Con la meta se decide qué áreas necesitan acción. Si un área queda bajo la meta, no se baja la meta ni se firma lo que no se hizo: se busca la causa, como falta de personal, tareas poco claras o falta de materiales, y se propone una acción correctiva. También se controla el consumo de productos para pedir lo necesario.",
        "El rendimiento de un producto es cuántos usos se obtienen de un envase. El costo por uso se calcula dividiendo el precio del envase por sus usos. Todos los valores de esta ficha son de ejemplo; en la práctica se siguen el rótulo del producto y la norma vigente." + LIM,
    ],
    vocab=[("tareas previstas", "tareas que debían hacerse según el plan"), ("tareas firmadas", "tareas registradas como hechas"), ("rendimiento", "cantidad de usos que se obtienen de un envase"), ("costo por uso", "precio del envase dividido por sus usos"), ("meta", "porcentaje mínimo de cumplimiento esperado")],
    worked=[
        ("Calcular tareas previstas", "Un área de ejemplo tiene 6 tareas diarias, trabaja 4 días a la semana y se mide 3 semanas. ¿Cuántas tareas están previstas?", ["Se multiplican tareas, días y semanas.", "6 × 4 × 3 = 72."], "72 tareas"),
        ("Calcular el costo por uso", "Un envase de ejemplo cuesta $6.000 y rinde 30 usos. ¿Cuánto cuesta cada uso?", ["Se divide el precio por los usos.", "6.000 ÷ 30 = 200."], "$200"),
    ],
    mistakes=[("Bajar la meta cuando un área no la alcanza.", "La meta existe para detectar fallas; cambiarla oculta el problema.", "Busca la causa del incumplimiento y define una acción correctiva."),
              ("Calcular las tareas previstas solo con los días de un semana y olvidar las semanas del mes.", "El total previsto queda muy bajo y el porcentaje sale falso.", "Multiplica las tareas diarias por los días y por las semanas medidas.")],
    T=[
        ("abc", "En Gastronomía: ¿qué mide el porcentaje de cumplimiento de una pauta?", "Qué parte de las tareas previstas se firmó como hecha", "Cuánto producto de limpieza se gastó", "Cuántas personas trabajan en el área", "El cumplimiento compara lo firmado con lo previsto por el plan."),
        ("=", "{F} ¿Cuántas tareas están previstas en la cocina durante el mes?", "10*5*4", "Se multiplican las tareas diarias por los días a la semana y por las semanas.", " tareas"),
        ("=", "{F} ¿Cuántas tareas están previstas en la bodega durante el mes?", "4*5*4", "Se multiplican las tareas diarias, los días a la semana y las semanas.", " tareas"),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tuvo la cocina?", "180*100//200", "Se multiplican las firmadas por 100 y se dividen por las previstas.", " %"),
        ("=", "{F} ¿Qué porcentaje de cumplimiento tuvo la bodega?", "60*100//80", "Se multiplican las firmadas por 100 y se dividen por las previstas.", " %"),
        ("abc", "{F} ¿Qué áreas cumplieron la meta de ejemplo?", "La cocina y el comedor", "Solo el comedor", "La bodega y el comedor", "La cocina llegó al 90 % y el comedor al 100 %; la bodega quedó en 75 %."),
        ("=", "{F} ¿Cuánto cuesta cada uso del limpiador de ejemplo?", "9000//20", "Se divide el precio del envase por los usos que rinde.", " pesos"),
        ("abc", "{F} ¿Qué acción corresponde para la bodega?", "Analizar por qué no se firmaron 20 tareas, reforzar responsables y revisar la pauta", "Bajar la meta de la bodega al 75 %", "Firmar las tareas que faltan sin verificar", "Se busca la causa del incumplimiento; bajar la meta o falsear el registro no lo resuelve."),
        ("=", "{F} En un mes se hacen 140 usos del limpiador. ¿Cuántos envases se necesitan?", "140//20", "Se dividen los usos del mes por los usos que rinde cada envase.", " envases"),
        ("=", "{F} ¿Cuánto cuestan los envases necesarios para 140 usos?", "(140//20)*9000", "Se calcula el número de envases y se multiplica por el precio de cada uno.", " pesos"),
        ("abc", "{F} Un jefe dice: «La cocina tiene 90 %, ya no hay nada que mejorar». ¿Qué respuesta es correcta?", "Cumple la meta mínima, pero aún se pueden revisar las 20 tareas no firmadas", "No cumple la meta", "Como alcanzó la meta, ya no necesita registrar su pauta", "Alcanzar la meta mínima no impide revisar las tareas pendientes."),
        ("abc", "{F} Si la bodega hubiera firmado 72 de sus tareas previstas, ¿habría cumplido la meta de al menos 90 %?", "Sí, justo, con 90 %", "No, con 85 %", "No, con 72 %", "72 × 100 ÷ 80 = 90, que iguala la meta mínima."),
        ("=", "{F} ¿Cuántas tareas quedaron sin firmar en las tres áreas durante el mes?", "(200+80+100)-(180+60+100)", "Se restan las firmadas de las previstas en las tres áreas.", " tareas"),
    ],
    ctx=("abc", "{F} La jefa debe decidir cuántos envases comprar para el próximo mes, que tendrá 160 usos. ¿Cuántos conviene pedir, si no quiere quedarse corta?", "8 envases, porque 160 usos dividido por 20 usos por envase da 8", "7 envases, porque siempre sobran", "10 envases, para asegurarse sin calcular", "El cálculo exacto evita comprar de más o de menos: 160 ÷ 20 = 8."),
    sc=[
        ("En Gastronomía: ¿cómo se calculan las tareas previstas de un mes?", "Tareas diarias por días de la semana por semanas", "Es el total de tareas que el plan exige en ese período."),
        ("¿Cómo se calcula el costo por uso de un producto?", "Precio del envase dividido por los usos", "Muestra cuánto cuesta cada vez que se usa."),
        ("¿Qué se hace si un área no llega a la meta?", "Se busca la causa y se define una acción correctiva", "Cambiar la meta no soluciona el problema."),
    ],
    op=("Control de ejemplo de otra cocina: cocina 8 tareas diarias, comedor 6 tareas diarias; ambas funcionan 5 días a la semana durante 4 semanas. Se firmaron 144 tareas en la cocina y 96 en el comedor. Meta de ejemplo: 90 %. "
        "Un envase de 4 litros cuesta $7.200 y rinde 24 usos. Calcula las tareas previstas y el cumplimiento de cada área, di cuál cumple la meta, calcula el costo por uso del envase y propone una acción para el área que no cumple.",
        "Cocina: 8 × 5 × 4 = 160 previstas; 144 × 100 ÷ 160 = 90 %. Comedor: 6 × 5 × 4 = 120 previstas; 96 × 100 ÷ 120 = 80 %, por lo que no cumple. Costo por uso: 7.200 ÷ 24 = 300 pesos. Acción para el comedor: revisar por qué no se firmaron 24 tareas y aclarar responsables.",
        ["calcula las tareas previstas de ambas áreas", "compara los porcentajes con la meta", "calcula el costo por uso y propone una acción para el área bajo la meta"],
        ["hoja con cálculos y una acción correctiva"],
        ["olvidar las semanas del mes", "decir que 80 % cumple", "bajar la meta del comedor"],
        "Pregunta: «¿qué pasaría con el comedor si se firmaran las 24 tareas sin hacerlas?». Debe reconocer el registro falso."),
    reinforce="Inventa un área con tareas diarias, días y semanas, calcula las previstas y el cumplimiento si se firmaron las nueve décimas partes.",
    extend="Explica por qué conocer el costo por uso ayuda a planificar compras sin gastar de más.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (cocina de un casino de ejemplo, inventado). Productos de baja complejidad del casino (de ejemplo): ensalada de verduras, puré de papas, arroz con verduras y sándwich frío. Cada uno tiene ficha técnica, pocas etapas y se produce bajo la supervisión de la jefa de cocina. "
     "Equipos (aparatos y máquinas): cocina industrial, refrigerador y procesadora de alimentos. Utensilios (herramientas manuales): cuchillos, tablas, ollas y cucharones. "
     "Peligros generales: cortes, quemaduras, atrapamientos, resbalones y contaminación.")
build(
    O3, 1, F,
    use="Aprenderé a situar la elaboración de productos de baja complejidad: qué los caracteriza, qué equipos y utensilios intervienen y qué riesgos y reglas generales hay.",
    prior=["Conozco el flujo de materias primas.", "Distingo limpiar y desinfectar.", "Sé multiplicar y dividir."],
    explain=[
        "En Gastronomía, un producto de baja complejidad es el que se elabora con pocas etapas, una ficha técnica clara y supervisión, sin técnicas avanzadas. Ejemplos son una ensalada o un puré. La ficha técnica es el documento que indica qué ingredientes y cantidades lleva el producto y cuántas porciones rinde. Elaborar significa transformar las materias primas en un producto listo para servir.",
        "Se trabaja con equipos, que son aparatos o máquinas (como un refrigerador o una procesadora), y con utensilios, que son herramientas manuales (como una tabla o un cucharón). La mise en place es la organización previa: tener ingredientes, utensilios y equipos ordenados y limpios antes de comenzar. Un área despejada reduce los accidentes.",
        "Los peligros más comunes son cortes, quemaduras, atrapamientos, resbalones y contaminación de los alimentos. Las reglas generales son usar los equipos solo con instrucción y autorización, mantener el orden y la limpieza, y seguir la ficha técnica. Aquí se aprenden solo conceptos; los equipos con fuego, gas o filo se practican con instructor, no con este cuaderno." + LIM,
    ],
    vocab=[("producto de baja complejidad", "elaboración con pocas etapas, ficha clara y supervisión"), ("ficha técnica", "documento con ingredientes, cantidades y rendimiento de un producto"), ("equipo", "aparato o máquina, como un refrigerador"), ("utensilio", "herramienta manual, como una tabla o un cucharón"), ("mise en place", "organización previa de ingredientes, utensilios y equipos"), ("rendimiento", "cantidad de porciones que da una elaboración")],
    worked=[
        ("Clasificar un elemento", "En una cocina de ejemplo hay un batidor manual. ¿Es un equipo o un utensilio?", ["Es una herramienta que se maneja con la mano.", "No es un aparato ni una máquina."], "Un utensilio"),
        ("Calcular porciones", "Una cocina de ejemplo produce 3 turnos de 20 porciones cada uno. ¿Cuántas porciones son?", ["Se multiplican los turnos por las porciones.", "3 × 20 = 60."], "60 porciones"),
    ],
    mistakes=[("Empezar a producir sin ordenar el área ni revisar la ficha.", "Aumenta el riesgo de accidentes y de errores en las cantidades.", "Haz primero la mise en place: ordena el área, revisa la ficha y reúne lo necesario."),
              ("Usar un equipo «porque parece fácil» sin haber recibido instrucción.", "Un uso incorrecto puede causar atrapamientos, cortes o quemaduras.", "Usa un equipo solo con instrucción y autorización del instructor o la jefatura.")],
    T=[
        ("abc", "En Gastronomía: ¿qué caracteriza a un producto de baja complejidad?", "Tiene pocas etapas, una ficha técnica clara y se produce con supervisión", "Requiere técnicas avanzadas y equipos especiales", "Se elabora sin ficha técnica, a criterio de cada cocinero", "La baja complejidad se define por pocas etapas, una ficha clara y supervisión."),
        ("abc", "{F} ¿Cuál de estos elementos de la ficha es un equipo?", "El refrigerador", "La tabla", "El cucharón", "El refrigerador es un aparato; la tabla y el cucharón son herramientas manuales."),
        ("abc", "{F} ¿Cuál de estos elementos de la ficha es un utensilio?", "El cucharón", "La procesadora de alimentos", "La cocina industrial", "El cucharón es una herramienta manual, a diferencia de las máquinas."),
        ("abc", "En Gastronomía: ¿qué es la mise en place?", "La organización previa de ingredientes, utensilios y equipos antes de producir", "El menú escrito del día", "La limpieza final de la cocina", "Es la preparación ordenada que se hace antes de comenzar la producción."),
        ("=", "Un casino de ejemplo produce 4 productos al día, cada uno en 3 turnos de servicio y con 25 porciones por turno. ¿Cuántas porciones se producen al día?", "4*3*25", "Se multiplican los productos, los turnos y las porciones.", " porciones"),
        ("abc", "{F} ¿Cuál de estos peligros menciona la ficha?", "Atrapamientos", "Ruido excesivo", "Humedad del aire", "La ficha lista cortes, quemaduras, atrapamientos, resbalones y contaminación."),
        ("abc", "{F} Un ayudante nuevo quiere usar la procesadora de alimentos porque «se ve fácil». ¿Qué corresponde?", "No usarla hasta recibir instrucción y autorización de la jefa de cocina o del docente", "Usarla, si antes mira a otra persona una vez", "Usarla con guantes", "Los equipos se usan solo con instrucción y autorización, sin importar lo fácil que parezcan."),
        ("abc", "Antes de comenzar a producir, ¿qué práctica reduce los riesgos del área de trabajo?", "Mantener el área despejada y ordenada, con los utensilios en su lugar", "Dejar todos los utensilios a mano sobre el mesón", "Guardar los utensilios solo al final de la semana", "El orden evita tropiezos, caídas y confusión entre utensilios."),
        ("=", "La jefa asigna 3 ayudantes por turno, 2 turnos al día, durante 5 días. ¿Cuántos turnos de ayudante se asignan en total?", "3*2*5", "Se multiplican los ayudantes, los turnos y los días.", " turnos"),
        ("abc", "Un compañero dice que, como el producto es de baja complejidad, no necesita supervisión ni higiene. ¿Qué respuesta es correcta?", "Baja complejidad se refiere a pocas etapas; las reglas de higiene y seguridad se aplican igual", "Tiene razón, porque son productos sencillos", "La higiene solo se aplica si lo pide un cliente", "La complejidad no cambia el riesgo de contaminación ni de accidentes."),
        ("abc", "{F} Una alumna propone guardar los cuchillos sueltos en un cajón «para tenerlos a mano». ¿Qué principio de seguridad corresponde?", "Los utensilios cortantes se guardan en un lugar definido y protegido, y los usa quien tiene autorización", "Está bien, porque el cajón es un lugar cerrado", "Es mejor dejarlos sobre el mesón para que se vean", "Un lugar definido y protegido evita cortes al buscar o mover los utensilios."),
        ("=", "La cocina elabora 120 porciones al día. Si cada ayudante puede apoyar 40 porciones al día, ¿cuántos ayudantes se necesitan?", "120//40", "Se divide el total de porciones por las que apoya cada ayudante.", " ayudantes"),
        ("abc", "{F} Falta la ficha técnica de la ensalada y un cocinero propone hacerla «como siempre». ¿Qué corresponde?", "Pedir la ficha a la jefatura antes de producir, para asegurar el mismo resultado", "Producir y anotar la ficha después", "Preguntar las cantidades a un compañero y usarlas", "La ficha da cantidades y rendimiento comunes; sin ella el resultado cambia de un día a otro."),
    ],
    ctx=("abc", "{F} Un colegio de ejemplo pide 90 sándwiches fríos para un acto y la cocina cuenta con una cocinera y dos ayudantes. ¿Cuál es el primer paso de organización?", "Revisar la orden y la ficha técnica y ordenar el área y el personal antes de comenzar", "Empezar de inmediato para ganar tiempo", "Pedir a los ayudantes que decidan las cantidades", "La organización previa evita errores de cantidad y accidentes por apuro."),
    sc=[
        ("En Gastronomía: ¿qué es un equipo?", "Un aparato o máquina, como un refrigerador", "Se distingue del utensilio, que es una herramienta manual."),
        ("¿Qué indica la ficha técnica?", "Ingredientes, cantidades y rendimiento", "Permite repetir el mismo producto y calcular porciones."),
        ("¿Cuándo se usa un equipo?", "Solo con instrucción y autorización", "El uso incorrecto puede causar accidentes."),
    ],
    op=("Una cocina de ejemplo debe producir hoy 80 porciones de arroz con verduras. Cuenta con una cocinera, dos ayudantes, una procesadora de alimentos, ollas y tablas. "
        "Escribe: (a) cuáles de esos elementos son equipos y cuáles utensilios, (b) tres acciones de mise en place antes de comenzar, (c) dos peligros generales del trabajo y una regla general de seguridad para cada uno (sin describir técnicas de cocción o corte).",
        "(a) Equipo: la procesadora. Utensilios: las ollas y las tablas. (b) Revisar la ficha técnica, ordenar y limpiar el área, reunir ingredientes y utensilios. (c) Cortes: guardar los utensilios cortantes en un lugar definido y usarlos con autorización. Resbalones: mantener el piso seco y despejado.",
        ["clasifica equipo y utensilios sin errores", "nombra tres acciones de organización previa", "relaciona dos peligros con reglas generales de seguridad"],
        ["hoja con tres respuestas"],
        ["describir cómo cortar o cocinar", "llamar equipo a las ollas", "olvidar revisar la ficha técnica"],
        "Pregunta: «¿qué pasaría si empiezas sin revisar la ficha?». Debe mencionar errores de cantidad."),
    reinforce="Haz una tabla con ocho elementos de una cocina inventada y clasifica cada uno como equipo o utensilio.",
    extend="Explica por qué ordenar el área antes de producir también protege a las personas del equipo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo, inventada). «Ensalada de verduras de ejemplo»: rinde 10 porciones. Ingredientes: lechuga 700 g, tomate 500 g, zanahoria 200 g, aliño 100 g. "
     "Orden de producción: documento que indica qué producir, cuántas porciones y para cuándo; la emite la jefa de cocina. Requisición interna: formulario con que producción pide ingredientes a bodega. "
     "Roles: la jefa de cocina dirige; la cocinera elabora; el ayudante apoya con tareas simples bajo supervisión; el encargado de bodega entrega los ingredientes.")
build(
    O3, 2, F,
    use="Aprenderé a leer una ficha técnica y una orden de producción, y a reconocer qué hace cada integrante del equipo de cocina.",
    prior=["Conozco productos de baja complejidad, equipos y utensilios.", "Sé sumar y dividir.", "Sé leer una tabla breve."],
    explain=[
        "La ficha técnica de un producto indica sus ingredientes, las cantidades, el rendimiento (cuántas porciones da) y a veces otros datos de la elaboración. Una porción es la cantidad de producto que se sirve a una persona. Si se suman los ingredientes y se divide por las porciones, se obtiene el peso aproximado de cada porción.",
        "La orden de producción dice qué se debe producir, cuántas porciones y para cuándo. Quien produce la compara con la ficha para saber cuánto necesita de cada ingrediente. Con esa cantidad se hace una requisición interna, que es el pedido de producción a bodega.",
        "El equipo de cocina se organiza en roles: la jefa de cocina dirige y decide qué se produce, la cocinera elabora, el ayudante apoya con tareas simples bajo supervisión y el encargado de bodega entrega los ingredientes. Un cambio en la ficha lo autoriza la jefa y se registra; nadie modifica las cantidades por cuenta propia." + LIM,
    ],
    vocab=[("porción", "cantidad de producto que se sirve a una persona"), ("rendimiento", "cantidad de porciones que da una ficha"), ("orden de producción", "documento que dice qué producir, cuántas porciones y para cuándo"), ("requisición interna", "pedido de producción a bodega"), ("brigada", "equipo de personas que trabaja en la cocina con roles definidos")],
    worked=[
        ("Leer el rendimiento", "Una ficha de ejemplo indica «rinde 8 porciones» y pesa 1.200 g en total. ¿Cuánto pesa cada porción?", ["Se divide el peso total por las porciones.", "1.200 ÷ 8 = 150."], "150 g"),
        ("Identificar un rol", "Quien emite la orden de producción de un casino de ejemplo es la jefa de cocina. ¿Qué hace una orden de producción?", ["Es un documento de la jefa.", "Dice qué producir, cuántas porciones y para cuándo."], "Indica qué producir, cuántas porciones y para cuándo"),
    ],
    mistakes=[("Cambiar la cantidad de aliño de la ficha porque «así le gusta a todos».", "El producto sale distinto cada día y se pierde el control del costo y del resultado.", "Propón el cambio a la jefa; si lo autoriza, se registra en la ficha."),
              ("Pedir ingredientes a bodega sin requisición.", "No queda registro de lo que salió y el inventario no cuadra.", "Pide siempre con una requisición interna firmada.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es una ficha técnica?", "Un documento que indica ingredientes, cantidades y rendimiento de una elaboración", "Un registro de limpieza de la cocina", "Una lista del personal de turno", "La ficha reúne los datos para repetir un producto con el mismo resultado."),
        ("abc", "{F} ¿Cuántas porciones rinde la ficha técnica?", "10 porciones", "7 porciones", "20 porciones", "La ficha dice «rinde 10 porciones»; 7 y 20 no aparecen."),
        ("=", "{F} ¿Cuántos gramos suman los ingredientes de la ficha?", "700+500+200+100", "Se suman las cantidades de los cuatro ingredientes.", " g"),
        ("=", "{F} ¿Cuántos gramos tiene cada porción?", "(700+500+200+100)//10", "Se suman los ingredientes y se dividen por las porciones.", " g"),
        ("abc", "{F} ¿Quién emite la orden de producción?", "La jefa de cocina", "El encargado de bodega", "El ayudante", "La ficha asigna la emisión a la jefa de cocina, que dirige la producción."),
        ("abc", "{F} ¿Qué documento usa producción para pedir ingredientes a bodega?", "La requisición interna", "La orden de producción", "La guía de despacho", "La requisición es el pedido interno de producción a bodega."),
        ("abc", "{F} ¿Quién apoya con tareas simples bajo supervisión?", "El ayudante", "La cocinera", "El encargado de bodega", "La ficha define así el rol del ayudante."),
        ("abc", "{F} Un cocinero cambia la cantidad de aliño «porque le gusta más». ¿Qué observación corresponde?", "Los cambios deben ser autorizados por la jefa y registrados, para mantener el mismo resultado", "Es válido, porque conoce el producto", "Solo es válido si un cliente lo pide", "Un cambio sin autorización altera el producto y su costo."),
        ("=", "{F} Si cada porción de ensalada se vende a $1.800 (precio de ejemplo), ¿cuánto se obtiene por las 10 porciones de la ficha?", "1800*10", "Se multiplica el precio de una porción por las porciones que rinde la ficha.", " pesos"),
        ("abc", "La orden de producción pide 40 porciones y la ficha rinde 10. ¿Qué indica esa diferencia?", "Que hay que multiplicar las cantidades de la ficha por 4", "Que la ficha está equivocada", "Que se hace una sola vez y se reparte en porciones más pequeñas", "40 es cuatro veces 10, por lo que cada ingrediente se multiplica por 4."),
        ("abc", "Un ayudante quiere firmar la requisición de bodega en lugar de la cocinera. ¿Qué corresponde?", "Que firme la persona con la responsabilidad asignada, porque la firma respalda los datos", "Que firme cualquier persona disponible", "Que firme con el nombre de la cocinera", "La firma hace responsable de lo escrito a quien la pone, por eso no se delega ni se falsea."),
        ("=", "{F} Una requisición entrega 3.500 g de lechuga. ¿Para cuántas porciones alcanza, según la ficha?", "3500//(700//10)", "Se calcula la lechuga de una porción y se divide lo entregado por ese valor.", " porciones"),
        ("abc", "{F} ¿Por qué la ficha incluye el rendimiento?", "Para saber cuántas porciones se obtienen y poder calcular cantidades y costos", "Para decidir el color del plato", "Para saber qué persona cocina", "El rendimiento permite escalar la ficha y costear cada porción."),
    ],
    ctx=("abc", "{F} Un practicante encuentra en la cocina dos fichas distintas de la misma ensalada, con cantidades diferentes. ¿Qué debe hacer?", "Consultar a la jefa cuál es la vigente y no producir hasta saberlo", "Usar la más antigua", "Promediar las cantidades de ambas", "Solo una ficha vigente asegura el mismo producto; decidir por cuenta propia genera errores."),
    sc=[
        ("En Gastronomía: ¿qué es el rendimiento de una ficha?", "La cantidad de porciones que da", "Permite calcular cantidades y costo por porción."),
        ("¿Qué documento dice qué producir, cuántas porciones y para cuándo?", "La orden de producción", "La emite la jefa de cocina."),
        ("¿Quién autoriza un cambio en las cantidades de la ficha?", "La jefa de cocina", "Los cambios se aprueban y se registran para no alterar el producto."),
    ],
    op=("Ficha de ejemplo «Arroz con verduras de ejemplo», rinde 8 porciones: arroz 800 g, zanahoria 300 g, arvejas 200 g, aceite 100 g. La jefa emite una orden de producción para 24 porciones. "
        "Calcula cuánto pesa cada porción, por cuánto hay que multiplicar la ficha y cuántos gramos de arroz se necesitan; escribe además quién emite la orden, qué documento usa producción para pedir a bodega y qué haría si cree que la ficha lleva demasiado aceite.",
        "Peso total: 800 + 300 + 200 + 100 = 1.400 g; por porción: 1.400 ÷ 8 = 175 g. La orden de 24 porciones es 3 veces la ficha (24 ÷ 8). Arroz: 800 × 3 = 2.400 g. La jefa emite la orden; producción usa una requisición interna. Si cree que lleva demasiado aceite, lo propone a la jefa para que lo autorice y registre.",
        ["calcula 175 g por porción", "calcula el factor 3 y 2.400 g", "nombra el rol, el documento y la vía de autorización de un cambio"],
        ["hoja con cálculos y tres respuestas"],
        ["usar 24 como factor", "cambiar la cantidad de aceite sin autorización", "confundir orden de producción con requisición"],
        "Pregunta: «¿por qué número se multiplica cada ingrediente?». Si responde 24, repasa cómo se calcula el factor."),
    reinforce="Escribe una ficha técnica inventada de tres ingredientes con su rendimiento y calcula el peso de una porción.",
    extend="Explica por qué todos los turnos deben usar la misma ficha técnica para el mismo producto.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (caso de producción de ejemplo, inventado). Ficha técnica «Puré de papas de ejemplo», rinde 12 porciones: papas 2.400 g, leche 360 ml, margarina 120 g. "
     "Orden de producción del día: 60 porciones para el almuerzo de un colegio de ejemplo y 24 porciones para el personal. Existencias en bodega: papas 20.000 g, leche 2.000 ml, margarina 600 g.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso de producción en papel: escalar una ficha técnica, comparar con las existencias y decidir qué hacer si algo no alcanza.",
    prior=["Sé leer una ficha técnica y una orden de producción.", "Sé multiplicar y dividir.", "Conozco la requisición interna."],
    explain=[
        "Para producir más o menos porciones que las de la ficha se calcula el factor de escala, que es el número por el que se multiplica cada ingrediente. Se obtiene dividiendo las porciones pedidas por las porciones que rinde la ficha. Si la ficha rinde 12 y se piden 36, el factor es 3, y todos los ingredientes se multiplican por 3.",
        "Luego se comparan las cantidades necesarias con las existencias de bodega. Si algún ingrediente no alcanza, se calcula cuánto falta y se decide: pedir lo que falta, producir menos porciones o consultar a la jefa. Nunca se cambian las cantidades de la ficha para que alcance, porque se altera el producto.",
        "Un buen análisis anota los datos, hace los cálculos, compara y deja una decisión justificada. Todo se registra: la orden, la requisición y cualquier diferencia." + LIM,
    ],
    vocab=[("factor de escala", "número por el que se multiplica cada ingrediente de una ficha"), ("existencias", "cantidad de un producto que hay disponible en bodega"), ("faltante", "cantidad que falta para completar lo necesario"), ("justificar", "explicar una decisión con datos")],
    worked=[
        ("Calcular el factor", "Una ficha de ejemplo rinde 5 porciones y se piden 20. ¿Cuál es el factor de escala?", ["Se dividen las porciones pedidas por las de la ficha.", "20 ÷ 5 = 4."], "4"),
        ("Calcular un faltante", "Se necesitan 900 g de un ingrediente y hay 650 g en bodega. ¿Cuánto falta?", ["Se resta lo disponible a lo necesario.", "900 − 650 = 250."], "250 g"),
    ],
    mistakes=[("Reducir la margarina de la ficha para que alcance con las existencias.", "Cambia el producto y el resultado, y no está autorizado.", "Calcula el faltante y propone pedir más o producir menos porciones."),
              ("Usar como factor el número de porciones pedidas en vez de dividirlo por el rendimiento.", "Las cantidades salen muchas veces mayores que las necesarias.", "Divide las porciones pedidas por las porciones que rinde la ficha.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es el factor de escala?", "El número por el que se multiplica cada ingrediente de la ficha", "El precio por cada porción", "El tiempo de la elaboración", "El factor ajusta todas las cantidades a las porciones que se pidieron."),
        ("=", "{F} ¿Cuántas porciones se deben producir en total?", "60+24", "Se suman las porciones del colegio y las del personal.", " porciones"),
        ("=", "{F} ¿Cuál es el factor de escala para la producción total?", "(60+24)//12", "Se dividen las porciones totales por las que rinde la ficha.", ""),
        ("=", "{F} ¿Cuántos gramos de papas se necesitan?", "2400*7", "Se multiplican los gramos de la ficha por el factor 7.", " g"),
        ("=", "{F} ¿Cuántos mililitros de leche se necesitan?", "360*7", "Se multiplican los mililitros de la ficha por el factor 7.", " ml"),
        ("abc", "{F} Con las existencias de bodega, ¿qué ingrediente alcanza para la producción total?", "Las papas", "La leche", "La margarina", "Se necesitan 16.800 g de papas y hay 20.000 g; la leche y la margarina no alcanzan."),
        ("=", "{F} ¿Cuántos mililitros de leche faltan?", "360*7-2000", "A la leche necesaria se le restan las existencias.", " ml"),
        ("=", "{F} ¿Cuántos gramos de margarina faltan?", "120*7-600", "A la margarina necesaria se le restan las existencias.", " g"),
        ("abc", "{F} ¿Qué decisión corresponde ante los faltantes?", "Pedir los faltantes o producir menos porciones, y consultar a la jefa", "Bajar la leche y la margarina de la ficha para que alcancen", "Producir igual con lo que haya, sin avisar", "Se resuelve con más ingredientes o menos porciones, no alterando la ficha."),
        ("=", "{F} ¿Cuántas porciones se pueden producir como máximo con la margarina existente?", "600//(120//12)", "Se calcula la margarina de una porción y se divide lo disponible por ese valor.", " porciones"),
        ("abc", "{F} Un cocinero propone reducir la margarina solo en el puré del personal. ¿Qué observación corresponde?", "Cambiar cantidades de la ficha altera el producto y debe autorizarlo la jefa y registrarse", "Es válido, porque son pocas porciones", "Se puede hacer si se avisa al terminar", "La autorización previa y el registro mantienen un producto constante."),
        ("=", "{F} Si las papas cuestan $1.100 el kilo (precio de ejemplo), ¿cuánto cuestan las papas de la producción total?", "16800*1100//1000", "Se convierten los gramos a kilos al multiplicar por el precio y dividir por 1.000.", " pesos"),
        ("abc", "{F} Si el pedido fuera de 30 porciones en vez de 84, ¿el factor de escala sería un número entero?", "No: 30 no es múltiplo de 12", "Sí: sería 3", "Sí: sería 2", "30 ÷ 12 = 2,5, que no es un número entero; el factor también puede ser decimal."),
    ],
    ctx=("abc", "{F} Faltan leche y margarina y el colegio necesita sus porciones primero. ¿Qué decisión es más razonable?", "Priorizar las 60 porciones del colegio, que alcanzan con las existencias, y consultar cómo completar las del personal", "Producir primero las 24 porciones del personal", "Producir todo con menos margarina", "Con las existencias se pueden completar las 60 porciones del colegio sin alterar la ficha."),
    sc=[
        ("En el tronco común de gastronomía: ¿cómo se calcula el factor de escala?", "Porciones pedidas dividido por porciones de la ficha", "Indica cuántas veces se multiplica la ficha."),
        ("¿Qué se hace si un ingrediente no alcanza?", "Se calcula el faltante y se decide con la jefa", "No se cambian las cantidades de la ficha."),
        ("¿Cómo se calcula un faltante?", "Necesario menos existencias", "Es la diferencia entre lo necesario y lo disponible."),
    ],
    op=("Ficha de ejemplo «Ensalada de verduras», rinde 6 porciones: lechuga 360 g, tomate 240 g, zanahoria 120 g. Orden de producción: 30 porciones. Existencias en bodega: lechuga 2.000 g, tomate 1.000 g, zanahoria 800 g. "
        "Calcula el factor de escala, las cantidades necesarias de cada ingrediente, qué ingrediente no alcanza y cuánto falta, y escribe qué decisión propondrías a la jefa.",
        "Factor: 30 ÷ 6 = 5. Lechuga: 360 × 5 = 1.800 g (alcanza). Tomate: 240 × 5 = 1.200 g (hay 1.000 g, faltan 200 g). Zanahoria: 120 × 5 = 600 g (alcanza). Decisión: pedir 200 g de tomate o producir menos porciones, sin cambiar la ficha.",
        ["calcula el factor 5", "calcula los tres ingredientes y detecta el tomate", "propone una decisión sin alterar la ficha"],
        ["hoja con cálculos y decisión"],
        ["usar 30 como factor", "no detectar el faltante", "proponer reducir el tomate de la ficha"],
        "Pregunta: «¿cuántos gramos de tomate necesitas para 30 porciones?». Si no llega a 1.200, repasa el factor."),
    reinforce="Inventa una ficha de tres ingredientes para 4 porciones y calcula las cantidades para 20 porciones.",
    extend="Explica por qué es mejor producir menos porciones que cambiar la ficha para que alcance.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (rendimiento y costo de ejemplo, inventados). Zanahoria: peso bruto 10 kg (con cáscara y puntas); peso neto 8 kg (lo que queda listo para usar); precio $900 por kilo bruto; porción de 160 g. "
     "Cebolla: peso bruto 8 kg; peso neto 6 kg; precio $900 por kilo bruto; porción de 100 g. La merma es lo que se pierde al preparar el producto.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: calcular merma, rendimiento, porciones y costo por porción de un producto.",
    prior=["Sé multiplicar y dividir.", "Sé calcular un porcentaje.", "Conozco la ficha técnica y las porciones."],
    explain=[
        "Al preparar un producto se pierde una parte, como cáscaras o puntas. El peso bruto es el que se compra, el peso neto es el que queda listo para usar y la merma es la diferencia entre ambos. El porcentaje de merma es la merma multiplicada por 100 y dividida por el peso bruto. El rendimiento es el peso neto sobre el bruto, también en porcentaje.",
        "El costo de lo comprado es el peso bruto por el precio. El costo por kilo neto se obtiene dividiendo ese costo por los kilos netos; es mayor que el precio de compra, porque se pagó también por la merma. Las porciones se calculan dividiendo el peso neto, en gramos, por el peso de la porción, y el costo por porción dividiendo el costo total por las porciones.",
        "Estos cálculos permiten comparar productos, planificar compras y fijar precios. Todos los números de esta clase son de ejemplo; solo se hacen cálculos en papel, sin manipular alimentos." + LIM,
    ],
    vocab=[("peso bruto", "peso del producto tal como se compra"), ("peso neto", "peso que queda listo para usar"), ("merma", "parte que se pierde al preparar un producto"), ("rendimiento", "porcentaje del peso bruto que queda como neto"), ("costo por porción", "costo total dividido por el número de porciones")],
    worked=[
        ("Calcular merma y porcentaje", "Un producto de ejemplo tiene peso bruto de 20 kg y neto de 16 kg. ¿Cuál es la merma y su porcentaje?", ["Merma = bruto − neto = 4 kg.", "4 × 100 ÷ 20 = 20."], "4 kg, es decir, 20 %"),
        ("Calcular porciones", "Un producto de ejemplo tiene 9 kg netos y la porción es de 150 g. ¿Cuántas porciones salen?", ["9 kg son 9.000 g.", "9.000 ÷ 150 = 60."], "60 porciones"),
    ],
    mistakes=[("Calcular el costo por porción usando el peso bruto en vez del neto.", "Se ignora la merma y el costo por porción sale menor que el real.", "Usa el peso neto para calcular las porciones y divide el costo total por ellas."),
              ("Pensar que el costo de un kilo servido es igual al precio de compra.", "El precio de compra incluye también lo que se pierde como merma.", "Calcula el costo por kilo neto: costo total dividido por kilos netos.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es la merma?", "La parte del producto que se pierde al prepararlo", "La ganancia que queda después de vender", "El producto que sobra del servicio", "La merma es lo que se pierde en la preparación, como cáscaras o puntas."),
        ("=", "{F} ¿Cuántos kilos de merma tuvo la zanahoria?", "10-8", "Al peso bruto se le resta el peso neto.", " kg"),
        ("=", "{F} ¿Qué porcentaje de merma tuvo la zanahoria?", "(10-8)*100//10", "Se multiplica la merma por 100 y se divide por el peso bruto.", " %"),
        ("=", "{F} ¿Qué porcentaje de rendimiento tuvo la zanahoria?", "8*100//10", "Se multiplica el peso neto por 100 y se divide por el bruto.", " %"),
        ("=", "{F} ¿Cuánto cuesta comprar los 10 kg brutos de zanahoria?", "10*900", "Se multiplica el peso bruto por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuántas porciones de 160 g salen de la zanahoria neta?", "8000//160", "Se pasan los kilos netos a gramos y se dividen por el peso de la porción.", " porciones"),
        ("=", "{F} ¿Cuánto cuesta cada porción de zanahoria?", "9000//50", "Se divide el costo total por el número de porciones.", " pesos"),
        ("abc", "{F} ¿Qué producto tuvo mayor porcentaje de merma?", "La cebolla, con 25 %", "La zanahoria, con 25 %", "Ambas tuvieron la misma merma", "La cebolla perdió 2 de 8 kg (25 %); la zanahoria, 2 de 10 kg (20 %)."),
        ("=", "{F} ¿Cuánto cuesta un kilo neto de zanahoria, considerando todo lo que se pagó por los 10 kg brutos?", "9000//8", "El costo total se reparte entre los kilos netos que quedaron.", " pesos"),
        ("abc", "{F} Una cocinera dice: «Como el kilo de zanahoria cuesta $900, cada kilo servido cuesta $900». ¿Qué corrección corresponde?", "Cada kilo servido cuesta más, porque se pagó también por la merma", "Tiene razón, porque el precio es por kilo", "Cuesta menos, porque la merma baja el precio", "El kilo neto debe cubrir el costo de lo perdido, por eso cuesta más que el bruto."),
        ("=", "{F} ¿Cuánto cuesta cada porción de cebolla de 100 g?", "(8*900)//(6000//100)", "Se divide el costo total por las porciones que salen del peso neto.", " pesos"),
        ("abc", "{F} Un proveedor ofrece zanahoria ya preparada a $1.300 el kilo neto. Solo por precio, ¿qué opción tiene menor costo por kilo neto?", "La zanahoria bruta, con $1.125 por kilo neto", "La preparada, con $1.300 por kilo neto", "Ambas cuestan lo mismo", "9.000 ÷ 8 = 1.125, que es menor que 1.300; el trabajo de preparar es un costo aparte."),
        ("=", "{F} Si la porción de zanahoria subiera a 200 g, ¿cuántas porciones saldrían de los 8 kg netos?", "8000//200", "Se pasan los kilos netos a gramos y se dividen por la nueva porción.", " porciones"),
    ],
    ctx=("abc", "{F} Una jefa compra 10 kg de zanahoria bruta creyendo que alcanzan para 62 porciones de 160 g, porque 10.000 ÷ 160 es 62. ¿Qué error cometió?", "No consideró la merma: el peso neto es de 8 kg, que alcanza para 50 porciones", "Usó una porción demasiado pequeña", "Debió comprar zanahoria ya preparada", "La cuenta debe hacerse con el peso neto; con 8 kg salen 50 porciones, no 62."),
    sc=[
        ("En Gastronomía: ¿qué es el peso neto?", "El peso que queda listo para usar", "Es lo que sobra después de la merma."),
        ("¿Cómo se calcula el porcentaje de merma?", "Merma por 100, dividida por el peso bruto", "Mide qué parte del producto comprado se pierde."),
        ("¿Con qué peso se calculan las porciones?", "Con el peso neto", "Es el que realmente se puede servir."),
    ],
    op=("Dato de ejemplo: pimentón con peso bruto de 5 kg, peso neto de 4 kg, precio de $1.200 por kilo bruto, y porción de 80 g. "
        "Calcula la merma en kilos y en porcentaje, el costo de lo comprado, cuántas porciones salen, el costo por porción y explica con tus palabras por qué el kilo neto cuesta más que el precio de compra.",
        "Merma: 5 − 4 = 1 kg, es decir, 1 × 100 ÷ 5 = 20 %. Costo comprado: 5 × 1.200 = 6.000 pesos. Porciones: 4.000 ÷ 80 = 50. Costo por porción: 6.000 ÷ 50 = 120 pesos. El kilo neto cuesta más porque se pagó también por el kilo que se perdió como merma.",
        ["calcula la merma y su porcentaje", "calcula las porciones y el costo por porción", "explica el efecto de la merma en el costo"],
        ["hoja con cálculos y explicación"],
        ["usar el peso bruto para las porciones", "olvidar convertir kilos a gramos", "no relacionar merma con costo"],
        "Pregunta: «¿cuántos gramos netos son 4 kg?». Si no responde 4.000, repasa la conversión de unidades."),
    reinforce="Inventa un producto con peso bruto y neto, calcula merma, porciones y costo por porción.",
    extend="Explica por qué dos productos con el mismo precio por kilo pueden tener distinto costo por porción.",
)
