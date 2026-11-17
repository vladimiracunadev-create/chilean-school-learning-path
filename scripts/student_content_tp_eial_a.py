"""Elaboración Industrial de Alimentos TP (3.º y 4.º medio): OAE-01 (recepcionar, pesar, clasificar, almacenar e inventariar), OAE-02 (elaborar, conservar y envasar: flujo, balance de materia, rendimiento y costo; solo conceptos) y OAE-03 (monitorear el estado de materias primas y productos con análisis básicos). Todo en papel: plantas, proveedores, lotes, cantidades y límites inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_eial_common import build

O1 = "TP-EIAL-3y4-OAE-01"
O2 = "TP-EIAL-3y4-OAE-02"
O3 = "TP-EIAL-3y4-OAE-03"
LIM = " Esto es aprendizaje conceptual en papel, con datos de ejemplo: la práctica en una planta de alimentos requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar."
LIMX = " Las máquinas, los equipos de frío, las atmósferas peligrosas y los productos químicos de limpieza solo se estudian aquí como concepto: su uso requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar. Ante un accidente o una intoxicación, avisa a un adulto responsable y a emergencias."

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (planta de conservas de ejemplo, inventada). Muelle de recepción: llegan camiones con materias primas (frutas y verduras frescas), insumos (sal, azúcar, aceite) y materiales (frascos, tapas y cajas de cartón). "
     "La recepcionista de bodega compara la guía de despacho con la orden de compra, pesa en la balanza del muelle y clasifica cada producto. El jefe de calidad decide si un lote se acepta o se rechaza; el jefe de bodega autoriza el ingreso al almacén de lo aceptado. "
     "Reglas generales: no se recibe nada sin documento; lo rechazado se separa e identifica; los productos se almacenan sobre tarimas, no en el piso, y separados de los productos de limpieza. La autoridad sanitaria fiscaliza el cumplimiento de la norma sanitaria vigente.")
build(
    O1, 1, F,
    use="Aprenderé a situar el trabajo de recepción y bodega de una planta de alimentos: qué productos llegan, qué etapas hay, qué riesgos existen y qué norma lo regula.",
    prior=["Sé sumar y restar cantidades.", "Sé leer una ficha con datos.", "Sé que los alimentos se transforman en una planta antes de llegar a las tiendas."],
    explain=[
        "En Elaboración Industrial de Alimentos, la materia prima es el alimento principal que se transforma, como frutas, verduras o leche. El insumo es un producto que se usa en la elaboración y no es la materia prima principal, como la sal, el azúcar o el aceite. Los materiales de envase y embalaje son los frascos, tapas, cajas y películas con que se contiene y protege el producto. Todo esto llega de proveedores y se registra en un inventario, que es la lista de lo que hay en bodega.",
        "En la recepción se hacen cinco tareas: recepcionar (recibir comparando con el documento), pesar, clasificar (agrupar según su naturaleza), seleccionar (separar lo apto para usar de lo que no cumple) y almacenar. Los registros pueden llevarse en un sistema informático o en un manual de inventarios en papel; lo importante es que cada entrada y cada salida quede anotada.",
        "Los riesgos principales son la contaminación cruzada (paso de microbios de un producto a otro), las plagas, el vencimiento de productos, los errores de pesaje y los accidentes al mover cargas. La autoridad sanitaria fiscaliza el cumplimiento de la norma sanitaria vigente. Mover cargas y operar equipos del muelle exige personal capacitado y autorizado." + LIM,
    ],
    vocab=[("materia prima", "alimento principal que se transforma en la planta"), ("insumo", "producto que se usa en la elaboración y no es la materia prima principal"), ("material de envase y embalaje", "frasco, tapa, caja o película que contiene y protege el producto"), ("inventario", "lista de lo que hay en bodega"), ("seleccionar", "separar lo apto para usar de lo que no cumple"), ("contaminación cruzada", "paso de microbios de un producto a otro"), ("guía de despacho", "documento con que el proveedor acompaña lo que entrega")],
    worked=[
        ("Clasificar un producto", "En una planta de ejemplo llega un bidón de aceite que se usa en la elaboración. ¿Es materia prima, insumo o material de envase?", ["El aceite se usa en la elaboración, pero no es el alimento principal que se transforma.", "Eso lo define como insumo."], "Insumo"),
        ("Ordenar tareas", "En la recepción de un camión de ejemplo, ¿qué va antes: almacenar o recepcionar comparando con el documento?", ["Almacenar solo es posible con un producto ya aceptado.", "Primero se recibe y se compara con el documento."], "Primero se recepciona"),
    ],
    mistakes=[("Guardar los sacos directamente en el piso porque «así se mueven menos».", "El piso acumula humedad y suciedad, y los sacos pueden contaminarse o dañarse.", "Almacena sobre tarimas y separado de los productos de limpieza."),
              ("Recibir un camión sin documento porque «el conductor conoce el pedido».", "Sin documento no hay respaldo de qué se recibió ni quién respondió.", "Pide la guía de despacho antes de recibir y avisa a la jefatura si falta.")],
    T=[
        ("abc", "En Elaboración Industrial de Alimentos: ¿cuál de estos productos de una planta de conservas es un insumo?", "Un saco de azúcar que se usa en la elaboración", "Las verduras frescas que son la materia prima principal", "Un frasco vacío que contendrá el producto", "El azúcar apoya la elaboración sin ser el alimento principal; el frasco es material de envase."),
        ("abc", "{F} ¿Quién decide si un lote se acepta o se rechaza?", "El jefe de calidad", "La recepcionista de bodega", "El jefe de bodega", "La ficha asigna esa decisión al jefe de calidad; la recepcionista compara y pesa, y el jefe de bodega autoriza el ingreso."),
        ("abc", "{F} Según las reglas generales de la ficha, ¿dónde se almacenan los productos?", "Sobre tarimas y separados de los productos de limpieza", "Directamente en el piso para facilitar el conteo", "Junto a los productos de limpieza para ahorrar espacio", "La ficha pide tarimas y separación de los productos de limpieza para evitar humedad y contaminación."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa clasificar en la recepción?", "Agrupar los productos según su naturaleza, como materia prima, insumo o material", "Medir cuánto pesa cada producto que llega", "Decidir cuánto se le pagará al proveedor", "Clasificar es agrupar por naturaleza; pesar es medir y pagar depende de lo recibido."),
        ("abc", "{F} ¿Qué riesgo busca evitar la regla de separar e identificar lo rechazado?", "Que un producto rechazado se mezcle con los aceptados y se use por error", "Que el proveedor cobre dos veces el mismo producto", "Que la balanza del muelle se descalibre con el uso", "Un rechazo sin separar ni identificar puede terminar usado en producción."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿por qué el pesaje en la recepción es un control y no solo un trámite?", "Porque permite comprobar que se recibió la cantidad pedida", "Porque reemplaza la revisión del documento de despacho", "Porque solo sirve para completar el inventario del mes", "El peso medido se contrasta con lo pedido y lo declarado; no sustituye los documentos."),
        ("=", "En el muelle de una planta de ejemplo se pidieron 5 cajas de tapas de 40 unidades y 8 cajas de frascos de 24 unidades. ¿Cuántas unidades de material de envase se pidieron en total?", "5*40+8*24", "Se calcula cada tipo de material y se suman los totales.", " unidades"),
        ("abc", "{F} Llega un camión con sacos de sal, pero sin guía de despacho. ¿Qué corresponde según la ficha?", "No recibir la mercadería hasta contar con el documento y avisar a la jefatura", "Recibirla y pedir el documento la próxima semana", "Recibirla si el conductor dice conocer el pedido", "La ficha establece que no se recibe nada sin documento."),
        ("abc", "En una planta de ejemplo llega un rollo de película plástica para envolver cajas en el despacho. ¿Cómo se clasifica?", "Como material de embalaje", "Como materia prima", "Como insumo de la elaboración", "La película protege y agrupa cajas, así que es un material de embalaje y no un alimento ni un insumo."),
        ("abc", "{F} El jefe quiere firmar la recepción por el total sin pesar la mitad de los sacos, «asumiendo que pesan lo mismo». ¿Qué observación es correcta?", "No debe firmarse un total que no se comprobó, porque la firma respalda los datos", "Es correcto, porque pesar todo siempre es innecesario", "Solo corresponde pesar cuando el proveedor lo pide", "La firma certifica que los datos son verdaderos; asumir pesos deja sin respaldo las diferencias."),
        ("abc", "Una planta de ejemplo registra las entradas a bodega, pero nunca las salidas hacia producción. ¿Cuál es la consecuencia más probable?", "El inventario muestra más stock del que realmente hay y se puede pedir tarde", "El inventario muestra menos stock del real y se pide de más", "No hay consecuencia, porque las entradas bastan para controlar", "Sin las salidas, lo registrado supera lo existente y falta aviso para reponer."),
        ("=", "La bodega de ejemplo tiene 450 kg de azúcar. Entran 3 sacos de 25 kg y salen 2 pedidos de la producción de 40 kg cada uno. ¿Cuántos kg de azúcar quedan?", "450+3*25-2*40", "Al stock inicial se suman las entradas y se restan las salidas.", " kg"),
        ("abc", "{F} En un día de lluvia, unos sacos de azúcar esperan en el piso del muelle mientras se libera la balanza. ¿Cuál es el riesgo principal?", "Que se humedezcan y contaminen, y el lote deba rechazarse", "Que la balanza del muelle mida de más", "Que el inventario de frascos quede desactualizado", "El azúcar en el piso mojado absorbe humedad y puede contaminarse, que es lo que protege la regla de tarimas."),
    ],
    ctx=("abc", "{F} Llegan al mismo tiempo un camión de frutas frescas y otro de frascos. El jefe dice: «recibe primero los frascos, que son más fáciles». ¿Qué criterio es adecuado?", "Atender primero lo perecible, porque se deteriora más rápido, y dejar el resto en espera", "Atender primero lo más fácil, porque ahorra tiempo", "Atender primero el camión que llegó desde más lejos", "Las frutas frescas se deterioran con el tiempo, mientras los frascos pueden esperar sin perder calidad."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cuál es la diferencia entre materia prima e insumo?", "La materia prima es el alimento principal que se transforma; el insumo apoya la elaboración", "La clasificación depende de la naturaleza del producto en el proceso."),
        ("¿Qué se hace con un camión que llega sin documento?", "No se recibe hasta contar con el documento y se avisa a la jefatura", "Sin documento no hay respaldo de lo recibido."),
        ("¿Qué institución fiscaliza la norma sanitaria vigente?", "La autoridad sanitaria", "Es la institución que controla las condiciones sanitarias de los establecimientos."),
    ],
    op=("Una planta de ejemplo recibió estos productos: 300 kg de tomates frescos, 50 kg de sal, 1.200 frascos vacíos, 20 cajas de cartón para el despacho y 100 litros de aceite. "
        "Escribe: (a) la clasificación de cada producto (materia prima, insumo o material de envase y embalaje), (b) cuál de ellos debe atenderse primero si todos esperan en el muelle y por qué, y (c) dos reglas generales de almacenamiento que apliquen a estos productos.",
        "(a) Tomates: materia prima. Sal y aceite: insumos. Frascos y cajas: materiales de envase y embalaje. (b) Los tomates frescos, porque son perecibles y se deterioran más rápido. (c) Almacenar sobre tarimas y separado de los productos de limpieza; identificar lo rechazado y mantenerlo aparte.",
        ["clasifica correctamente los cinco productos", "elige lo perecible y da la razón", "enuncia dos reglas de almacenamiento"],
        ["hoja con las tres respuestas"],
        ["clasificar la sal como materia prima", "elegir los frascos por ser más fáciles", "guardar los sacos en el piso"],
        "Pregunta: «¿qué pasa con los tomates si esperan sin ser atendidos?». Debe responder que se deterioran y pueden rechazarse."),
    reinforce="Escribe una lista de cinco productos de una planta de alimentos inventada y clasifica cada uno como materia prima, insumo o material de envase y embalaje.",
    extend="Explica con un ejemplo inventado por qué anotar cada entrada y cada salida de bodega evita errores en los pedidos.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documentos de una compra de ejemplo, inventados). Orden de compra N.º 31 de la Planta de Conservas de Ejemplo: 600 kg de manzanas, 200 kg de azúcar y 3.000 frascos. "
     "Guía de despacho N.º 412 del proveedor: 580 kg de manzanas, 200 kg de azúcar y 3.000 frascos. "
     "Pesaje del camión que trajo las manzanas: entró con 7.420 kg (peso bruto) y salió vacío con 6.840 kg (tara). El peso neto es el peso del producto sin el vehículo ni el envase. "
     "La factura (documento de cobro) llegó por 600 kg de manzanas. Roles: la recepcionista pesa y firma la recepción; el administrador revisa la factura antes de pagar.")
build(
    O1, 2, F,
    use="Aprenderé los documentos y los términos de la recepción (orden de compra, guía, factura, peso bruto, tara y peso neto) y qué rol responde por cada uno.",
    prior=["Conozco las tareas de recepción y la clasificación de productos.", "Sé sumar y restar cantidades.", "Sé leer una ficha con datos."],
    explain=[
        "La orden de compra es el documento con que la planta solicita productos al proveedor. La guía de despacho acompaña la entrega y detalla qué se entregó. La factura es el documento de cobro del proveedor. Al recibir, se compara lo pedido con lo declarado en la guía y con lo que realmente llegó, y se anotan las diferencias en el registro de recepción.",
        "Para pesar se usan tres términos: el peso bruto es el peso del producto con el vehículo o el envase; la tara es el peso del vehículo o el envase solo; y el peso neto es el peso del producto, que se obtiene restando la tara al peso bruto. También se distingue la selección, que separa lo apto para usar de lo que no cumple los criterios, de la clasificación, que agrupa por naturaleza.",
        "Cada registro tiene un responsable. La tarjeta de inventario (kárdex) anota, para cada producto, las entradas, las salidas y el stock, tanto en papel como en una planilla informática. Firmar un documento es afirmar que sus datos son verdaderos, por eso no se firma sin comprobar." + LIM,
    ],
    vocab=[("orden de compra", "documento con que la planta solicita productos al proveedor"), ("factura", "documento de cobro del proveedor"), ("peso bruto", "peso del producto con el vehículo o el envase"), ("tara", "peso del vehículo o del envase solo"), ("peso neto", "peso del producto sin vehículo ni envase"), ("tarjeta de inventario", "ficha por producto con entradas, salidas y stock"), ("stock", "cantidad de un producto que hay en bodega")],
    worked=[
        ("Calcular el peso neto", "Un camión de ejemplo con harina entra pesando 9.150 kg y, ya descargado, sale con 6.350 kg. ¿Cuál es el peso neto de la harina?", ["El peso neto es el bruto menos la tara.", "9.150 − 6.350 = 2.800."], "2.800 kg"),
        ("Distinguir documentos", "Un papel del proveedor muestra 20 cajas de tomates entregadas y viaja con el camión. ¿Qué documento es?", ["Detalla lo entregado y acompaña la mercadería.", "Eso corresponde a la guía de despacho."], "Una guía de despacho"),
    ],
    mistakes=[("Pagar la factura solo porque está emitida, sin comparar con lo recibido.", "Se puede pagar por productos que no llegaron o llegaron incompletos.", "Compara la factura con la guía de despacho y con el pesaje antes de pagar."),
              ("Restar al revés y obtener un peso neto negativo o mayor que el bruto.", "El peso bruto incluye el vehículo o el envase, así que siempre es mayor que el neto.", "Resta la tara al peso bruto: bruto menos tara.")],
    T=[
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es el peso neto?", "El peso del producto sin el vehículo ni el envase", "El peso del producto más el vehículo o el envase", "El peso del vehículo o del envase vacío", "El peso neto es solo el producto; el bruto incluye el envase y la tara es el envase solo."),
        ("abc", "{F} ¿Qué documento muestra lo que el proveedor declaró entregar?", "La guía de despacho N.º 412", "La orden de compra N.º 31", "La tarjeta de inventario de azúcar", "La guía acompaña la entrega y declara lo que el proveedor envió; la orden refleja lo pedido."),
        ("abc", "{F} En el pesaje del camión, ¿cuál es el peso bruto?", "7.420 kg, el peso del camión con la carga", "6.840 kg, el peso del camión vacío", "580 kg, el peso de las manzanas", "El peso bruto incluye vehículo y carga; el vacío es la tara y las manzanas son el peso neto."),
        ("=", "{F} Según el pesaje de la ficha, ¿cuántos kg netos de manzanas descargó el camión?", "7420-6840", "El peso neto se obtiene restando la tara al peso bruto.", " kg"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿para qué se registra la tara?", "Para restarla del peso bruto y obtener el peso neto", "Para calcular el precio por unidad del producto", "Para identificar el lote del proveedor", "Sin la tara no se puede separar el peso del producto del peso del vehículo o del envase."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa seleccionar materia prima?", "Separar lo apto para usar de lo que no cumple los criterios", "Elegir al proveedor más barato del mes", "Contar cuántas unidades hay en bodega", "Seleccionar es apartar lo que no cumple; escoger proveedores o contar es otra tarea."),
        ("=", "Un camión de ejemplo con azúcar entra pesando 5.280 kg y sale vacío con 4.915 kg. ¿Cuántos kg netos de azúcar descargó?", "5280-4915", "Al peso bruto se le resta la tara para obtener el neto.", " kg"),
        ("abc", "{F} La factura llegó por 600 kg de manzanas. ¿Qué debe comprobar el administrador antes de pagar?", "Que coincida con lo realmente recibido según la guía y el pesaje, no solo con lo pedido", "Que coincida con la orden de compra, por ser el documento más antiguo", "Solo que lleve la firma del proveedor", "La factura debe pagarse según lo recibido; la ficha muestra una entrega de 580 kg y no de 600."),
        ("=", "Las tapas de ejemplo llegan en cajas de 120 unidades. Llegan 24 cajas completas y una caja con 80 tapas. ¿Cuántas tapas llegaron?", "24*120+80", "Se multiplican las cajas completas por su contenido y se suma la caja parcial.", " tapas"),
        ("abc", "En otra entrega de ejemplo, la guía dice 580 kg, pero la balanza marcó 560 kg netos. Un compañero propone corregir la guía con lápiz. ¿Qué corresponde?", "Anotar el peso medido como diferencia en el registro y avisar a la jefatura, sin alterar la guía", "Corregir la guía, porque el peso medido es el real", "Aceptar el peso de la guía, porque es del proveedor", "Se deja constancia de lo medido, pero no se modifica un documento ajeno."),
        ("abc", "{F} La recepcionista firmó sin pesar porque «el proveedor siempre trae lo correcto». Más tarde faltan kilos y nadie puede probarlo. ¿Qué falló?", "Se firmó sin comprobar y no quedó registro del peso recibido", "El proveedor no emitió la factura a tiempo", "La tarjeta de inventario no tenía columna de tara", "La firma afirma que los datos son verdaderos; sin pesaje no hay respaldo para reclamar."),
        ("=", "La tarjeta de inventario de tapas de ejemplo muestra un stock inicial de 1.200 unidades, entradas de 480 y 360, y salidas de 900. ¿Cuántas tapas hay en stock?", "1200+480+360-900", "Al stock inicial se suman todas las entradas y se restan las salidas.", " tapas"),
        ("abc", "Una planta de ejemplo pasa a una planilla informática, pero sigue anotando a mano en el cuaderno los mismos movimientos, sin revisar que coincidan. ¿Cuál es el riesgo principal?", "Que los dos registros difieran y no se sepa cuál es el stock real", "Que se pierda la fecha de vencimiento de los productos", "Que el proveedor entregue menos mercadería", "Dos registros paralelos sin cotejo pueden contradecirse y dejan dudas sobre el stock."),
    ],
    ctx=("=", "{F} La factura llegó por 600 kg, pero se pagará según lo realmente recibido. Si el precio de ejemplo es de $420 por kg, ¿cuántos pesos corresponde pagar por las manzanas según el pesaje?", "(7420-6840)*420", "Se calcula el peso neto recibido y se multiplica por el precio por kilo.", " pesos"),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se obtiene el peso neto?", "Restando la tara al peso bruto", "El bruto incluye el vehículo o el envase, que debe descontarse."),
        ("¿Qué documento detalla lo que el proveedor entregó?", "La guía de despacho", "Acompaña la entrega y permite verificar lo recibido."),
        ("¿Qué se hace con una diferencia entre la guía y el peso medido?", "Se anota en el registro de recepción y se avisa a la jefatura", "Dejar constancia permite aclarar la diferencia con el proveedor."),
    ],
    op=("Documentos de ejemplo. Orden de compra: 400 kg de zanahorias y 150 kg de sal. Guía de despacho: 400 kg de zanahorias y 150 kg de sal. Pesaje del camión con las zanahorias: bruto 6.380 kg y tara 6.000 kg. Factura: 400 kg de zanahorias y 150 kg de sal. "
        "Escribe: (a) el peso neto de zanahorias según el pesaje, (b) qué diferencia hay respecto de la guía y de la orden, (c) qué documentos compararías antes de pagar y (d) qué anotarías en el registro de recepción.",
        "(a) 6.380 − 6.000 = 380 kg. (b) Faltan 20 kg respecto de la guía y de la orden, que dicen 400 kg. (c) La factura con la guía de despacho y con el pesaje. (d) «Zanahorias: guía 400 kg, peso neto medido 380 kg, diferencia de 20 kg; se avisa a la jefatura».",
        ["calcula el peso neto con bruto menos tara", "detecta los 20 kg de diferencia", "indica los documentos que compara y el registro"],
        ["hoja con las cuatro respuestas"],
        ["sumar la tara al bruto", "pagar por lo que dice la factura sin comparar", "no registrar la diferencia"],
        "Pregunta: «¿qué documento muestra lo que de verdad llegó?». Si responde la factura, repasa que el pesaje mide lo recibido."),
    reinforce="Haz una tabla con la orden de compra, la guía de despacho y la factura, y escribe quién emite cada una y para qué sirve.",
    extend="Explica con un ejemplo inventado por qué firmar una guía sin pesar puede traer problemas semanas después.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de recepción de ejemplo, inventado). Criterios del registro de la planta (valores de ejemplo; los reales los fijan la norma vigente y el manual de la planta): la fruta se acepta si en una muestra de 100 piezas hay como máximo 5 dañadas; "
     "los frascos se aceptan si la muestra no tiene trizaduras; los sacos deben llegar secos y sin roturas; todo envío debe traer guía de despacho. La muestra es una porción pequeña del lote que se examina para juzgar el lote completo. "
     "Llegada del día: (a) 800 kg de manzanas, y en la muestra de 100 piezas hay 8 dañadas; (b) 2.000 frascos, y la muestra no tiene trizaduras; (c) 6 sacos de azúcar de 25 kg, de los cuales 1 llegó mojado; (d) 40 cajas de cartón sin guía de despacho.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de recepción en papel: comparar cada producto con los criterios del registro y decidir si se acepta, se rechaza o se acepta en parte.",
    prior=["Conozco los documentos de la recepción.", "Sé restar cantidades.", "Sé comparar un dato con un límite."],
    explain=[
        "Al recibir se compara cada producto con criterios del registro: documento, cantidad, estado del envase y calidad de una muestra. La muestra es una porción pequeña del lote que se examina para juzgar el lote completo; se toma de distintos puntos y no solo de la superficie. Cada criterio tiene un límite que fija la norma vigente y el manual de la planta; en este cuaderno los límites son de ejemplo.",
        "Hay tres decisiones posibles: aceptar si se cumple todo, rechazar si se incumple un criterio importante y aceptar en parte si solo una porción del lote tiene problemas, como algunos sacos dañados dentro de un envío de varios. Siempre se anota la decisión, la causa, la cantidad y el proveedor en el registro de recepción.",
        "Lo rechazado no se mezcla con lo aceptado: se deja aparte e identificado hasta que el proveedor lo retire. Si hay dudas, se consulta al jefe de calidad y no se usa el producto mientras tanto. La recepción completa se hace antes de firmar, aunque el conductor tenga apuro." + LIM,
    ],
    vocab=[("muestra", "porción pequeña del lote que se examina para juzgar el lote completo"), ("aceptar", "recibir el producto porque cumple los criterios"), ("rechazar", "no recibir el producto porque incumple un criterio importante"), ("aceptar en parte", "recibir solo la porción del lote que cumple"), ("criterio de aceptación", "condición que el producto debe cumplir para recibirse"), ("registro de rechazo", "anotación de la causa, la cantidad y el proveedor")],
    worked=[
        ("Decidir con un criterio", "En un registro de ejemplo, los envases de jugo se aceptan si la muestra tiene como máximo 3 abollados de 50. Llega un lote con 2 abollados en la muestra. ¿Se acepta?", ["Se compara el dato con el máximo permitido.", "2 es menor que 3, así que se cumple el criterio."], "Se acepta"),
        ("Aceptar en parte", "Llegan 10 cajas de tapas y 2 están mojadas y deformadas. ¿Qué se hace?", ["Solo una parte del envío tiene problemas.", "Se rechazan las 2 dañadas y se aceptan las otras 8."], "Se acepta en parte: se aceptan 8 cajas"),
    ],
    mistakes=[("Revisar solo la capa superior del cajón y aceptar el lote completo.", "El estado de la superficie no representa el interior del lote.", "Toma la muestra desde distintos puntos del lote."),
              ("Aceptar sacos mojados porque «se pueden secar».", "La humedad puede haber alterado el producto y el criterio exige sacos secos.", "Rechaza el saco, sepáralo, identifícalo y registra la causa.")],
    T=[
        ("abc", "{F} ¿Qué decisión corresponde para las manzanas?", "Rechazarlas, porque la muestra superó el máximo de piezas dañadas", "Aceptarlas, porque la mayoría de las piezas está sana", "Aceptarlas y usarlas primero", "La muestra tiene 8 dañadas y el máximo es 5, por lo que no se cumple el criterio."),
        ("abc", "{F} ¿Qué decisión corresponde para los frascos?", "Aceptarlos, porque la muestra cumple el criterio", "Rechazarlos, porque no se revisaron todos uno por uno", "Aceptar solo la mitad del envío", "La muestra no tiene trizaduras y la ficha acepta el lote en ese caso."),
        ("abc", "{F} ¿Qué corresponde hacer con las 40 cajas de cartón?", "No recibirlas hasta contar con la guía de despacho", "Recibirlas porque el cartón no se echa a perder", "Recibirlas y anotar la guía la semana siguiente", "El criterio general de la ficha exige guía de despacho en todo envío."),
        ("=", "{F} Se aceptan los sacos de azúcar que llegaron secos. ¿Cuántos kg de azúcar se aceptan?", "(6-1)*25", "Se restan los sacos mojados del total y se multiplica por el peso de cada saco.", " kg"),
        ("abc", "{F} ¿Qué se hace con el saco mojado?", "Separarlo, identificarlo como rechazado y registrar la causa", "Usarlo de inmediato en la elaboración para que no se pierda", "Devolverlo al camión sin anotar nada", "Lo rechazado se aparta e identifica y se deja registro de la causa."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es una muestra en la recepción?", "Una porción pequeña del lote que se examina para juzgar el lote completo", "El lote completo revisado uno por uno", "El producto que el proveedor regala para probar", "La muestra representa al lote y permite decidir sin revisar todo."),
        ("=", "{F} ¿Cuántas piezas dañadas de más hay en la muestra de manzanas respecto del máximo permitido?", "8-5", "Se resta el máximo permitido a lo encontrado.", " piezas"),
        ("abc", "En otra entrega de ejemplo, la muestra de 100 frutas tiene 4 dañadas y el máximo es de 5. ¿Qué decisión corresponde?", "Aceptar el lote, porque 4 no supera el máximo de 5", "Rechazar el lote, porque hay frutas dañadas", "Pedir una muestra nueva hasta que no haya ninguna dañada", "El criterio fija un máximo y 4 está dentro del límite."),
        ("abc", "{F} ¿Qué datos deben quedar en el registro de rechazo de las manzanas?", "La causa (8 dañadas en la muestra de 100), la cantidad rechazada y el proveedor", "Solo la cantidad rechazada", "Solo el nombre de quien recibió", "El registro debe permitir explicar y reclamar la decisión: causa, cantidad y proveedor."),
        ("abc", "{F} Un jefe dice que no hace falta sacar la muestra de manzanas porque la capa superior del cajón se ve bien. ¿Qué respuesta es correcta?", "La muestra se toma desde distintos puntos, porque la superficie no representa el interior", "Tiene razón, porque la vista basta", "Basta con revisar un solo cajón elegido al azar", "La capa superior puede ocultar fruta dañada en el resto del lote."),
        ("abc", "Un proveedor reclama porque se rechazó su lote de manzanas. ¿Qué argumento del registro respalda la decisión de la planta?", "Que la muestra superó el máximo del criterio y la causa quedó registrada", "Que el proveedor suele entregar fruta de mala calidad", "Que el precio de la fruta estaba muy alto", "Una decisión se justifica con el criterio y el dato medido, no con opiniones."),
        ("=", "Llegan 12 cajas de frascos de 24 unidades; en 2 de las cajas todos los frascos están trizados. ¿Cuántos frascos se aceptan?", "(12-2)*24", "Se restan las cajas dañadas del total y se multiplica por el contenido de cada caja.", " frascos"),
        ("abc", "{F} Si se aplican los criterios, ¿cuántos de los cuatro envíos quedan aceptados total o parcialmente?", "2 envíos: los frascos y el azúcar", "1 envío: solo los frascos", "3 envíos: todos menos las manzanas", "Los frascos se aceptan por completo y el azúcar en parte; manzanas y cajas no se reciben."),
    ],
    ctx=("abc", "{F} El conductor del camión de manzanas dice que tiene otra entrega y pide que se firme de inmediato. ¿Qué respuesta corresponde?", "Explicar que primero se completa la verificación y se registra la decisión, y recién después se firma", "Firmar primero y verificar cuando se pueda", "Aceptar sin verificar si el conductor es conocido", "La firma respalda la decisión, por lo que la verificación va antes que la firma."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cuáles son las tres decisiones posibles en una recepción?", "Aceptar, rechazar o aceptar en parte", "Dependen de si el producto cumple todo, nada importante o solo una porción."),
        ("¿Qué se hace con un producto rechazado?", "Se separa, se identifica y se registra la causa", "Así no se mezcla con lo aceptado y queda respaldo."),
        ("¿De dónde se toma la muestra de un lote?", "De distintos puntos del lote", "La superficie no representa el interior del lote."),
    ],
    op=("Llegada de ejemplo, con los criterios de la ficha de esta clase. (a) 500 kg de zanahorias, y la muestra de 100 piezas tiene 3 dañadas. (b) 10 sacos de sal de 20 kg, de los cuales 2 llegaron rotos y derramados. (c) 1.000 tapas con guía de despacho, y la muestra no tiene deformaciones. "
        "Escribe: la decisión para cada envío con su razón, cuántos kg de sal se aceptan y qué dos datos anotarías en el registro de rechazo de los sacos rotos.",
        "(a) Aceptar: 3 dañadas no superan el máximo de 5. (b) Aceptar en parte: se aceptan 8 sacos, es decir 160 kg de sal; los 2 sacos rotos se rechazan. (c) Aceptar: tiene guía y la muestra cumple. En el registro de rechazo: «2 sacos de sal rotos, 40 kg» y el nombre del proveedor.",
        ["decide bien los tres envíos y justifica", "calcula 160 kg de sal", "anota causa o cantidad y proveedor en el rechazo"],
        ["hoja con las tres decisiones y el registro"],
        ["rechazar las zanahorias aunque cumplan", "aceptar los 10 sacos", "no anotar el proveedor"],
        "Pregunta: «¿qué pasaría con los 2 sacos rotos si no se separan?». Debe decir que podrían mezclarse con los aceptados."),
    reinforce="Escribe un registro de recepción de ejemplo con tres productos inventados y marca para cada uno si se acepta, se rechaza o se acepta en parte.",
    extend="Explica con un ejemplo inventado por qué se rechaza un lote con un criterio y no por una opinión.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (inventario de azúcar de ejemplo, inventado). Lotes en bodega: lote A, 100 kg, con 60 días de vida útil restante; lote B, 150 kg, con 90 días; lote C, 120 kg, con 120 días. "
     "FEFO significa que sale primero el lote que vence antes; PEPS significa primero en entrar, primero en salir. Consumo de producción: 80 kg por semana. El stock mínimo (de seguridad) de la planta es el consumo de dos semanas. "
     "El precio de ejemplo del azúcar es de $900 por kg.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar criterios de inventario con datos de ejemplo: rotación de lotes (FEFO y PEPS), stock mínimo, valor del inventario y cotejo entre el registro y el conteo.",
    prior=["Conozco la tarjeta de inventario.", "Sé multiplicar y restar enteros.", "Sé comparar fechas o plazos simples."],
    explain=[
        "La rotación de lotes ordena la salida de los productos. Con PEPS (primero en entrar, primero en salir) sale el lote que llegó antes. Con FEFO (primero en vencer, primero en salir) sale el lote que vence antes, aunque haya llegado después. En alimentos se prefiere FEFO cuando los lotes tienen distinta vida útil restante, para evitar que un lote venza sin usarse.",
        "El stock mínimo es la cantidad que no debe faltar para no detener la producción; cuando el stock baja de ese valor, corresponde pedir reposición. El valor del inventario se calcula multiplicando la cantidad de cada lote por su precio. Cada cierto tiempo se hace un conteo físico y se compara con el registro: si hay diferencia, se investiga y se corrige con respaldo.",
        "El inventario puede llevarse en una planilla informática o en un manual en papel, con las mismas ideas. Ordenar los lotes para que el que vence antes quede al frente es parte de un almacenamiento ordenado y seguro; mover cargas pesadas exige personal capacitado." + LIM,
    ],
    vocab=[("FEFO", "primero en vencer, primero en salir"), ("PEPS", "primero en entrar, primero en salir"), ("stock mínimo", "cantidad de seguridad que no debe faltar en bodega"), ("reposición", "nuevo pedido para recuperar el stock"), ("conteo físico", "recuento de lo que realmente hay en bodega"), ("vida útil restante", "tiempo que queda antes del vencimiento")],
    worked=[
        ("Elegir con FEFO", "Hay dos lotes de ejemplo: el lote X con 40 días de vida útil restante y el lote Y con 25 días. ¿Cuál sale primero con FEFO?", ["FEFO saca primero el que vence antes.", "25 días es menos que 40 días."], "El lote Y"),
        ("Calcular un stock mínimo", "Una planta de ejemplo consume 50 kg de sal por semana y fija su stock mínimo en dos semanas de consumo. ¿Cuánto es el mínimo?", ["Se multiplica el consumo semanal por 2.", "50 × 2 = 100."], "100 kg"),
    ],
    mistakes=[("Poner el lote nuevo delante del antiguo «porque es más fácil de alcanzar».", "El lote antiguo queda atrás y puede vencer sin usarse.", "Ordena para que salga primero el lote que vence antes."),
              ("Cambiar el conteo físico para que calce con la planilla.", "Se oculta una diferencia real y no se investiga su causa.", "Anota el conteo real, investiga la diferencia y ajusta solo con respaldo.")],
    T=[
        ("abc", "{F} Según FEFO, ¿qué lote sale primero?", "El lote A, porque le quedan 60 días", "El lote C, porque es el último en vencer", "El lote B, porque tiene más kilos que A", "FEFO saca primero el lote con menos vida útil restante, que es A."),
        ("=", "{F} ¿Cuántos kg de azúcar hay en total en la bodega?", "100+150+120", "Se suman los kilos de los tres lotes.", " kg"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa PEPS?", "Primero en entrar, primero en salir", "Primero en pagar, primero en salir", "Producto en proceso, siempre sale", "PEPS ordena la salida según el orden de llegada de los lotes."),
        ("=", "{F} ¿Cuál es el stock mínimo de azúcar, en kg?", "80*2", "El mínimo es el consumo de dos semanas.", " kg"),
        ("=", "{F} ¿Cuántos kg sobre el stock mínimo hay actualmente en bodega?", "100+150+120-80*2", "Al stock total se le resta el mínimo.", " kg"),
        ("abc", "{F} ¿Por qué FEFO puede ser mejor que PEPS cuando los lotes tienen distinta vida útil?", "Porque un lote que entró después puede vencer antes, y FEFO evita perderlo", "Porque FEFO siempre saca el lote más grande", "Porque PEPS no registra la fecha de entrada", "FEFO mira la fecha de vencimiento, que es lo que determina la pérdida."),
        ("=", "{F} ¿Cuántos pesos vale el lote B?", "150*900", "El valor se obtiene multiplicando los kilos por el precio por kilo.", " pesos"),
        ("=", "{F} Si el consumo de la semana se toma del lote que sale primero, ¿cuántos kg quedan de ese lote?", "100-80", "Al lote que sale primero se le resta el consumo semanal.", " kg"),
        ("=", "{F} Con el stock total y el consumo de 80 kg por semana, ¿para cuántas semanas completas alcanza el azúcar?", "(100+150+120)//80", "Se divide el stock total por el consumo semanal y se consideran las semanas completas.", " semanas"),
        ("abc", "Un bodeguero de ejemplo coloca un lote recién llegado delante de otro más antiguo porque es más fácil de alcanzar. ¿Qué consecuencia es la más probable?", "El lote antiguo queda atrás y puede vencer sin usarse", "El lote nuevo se vence antes que el antiguo", "No hay consecuencia, porque la planilla corrige el orden", "El producto mal ubicado queda sin usar y se pierde por vencimiento."),
        ("abc", "{F} El stock de azúcar baja a 150 kg y el jefe quiere que nunca se pase del mínimo. ¿Qué corresponde?", "Solicitar reposición, porque ya está bajo el mínimo de 160 kg", "Esperar, porque aún quedan 150 kg", "Rechazar los pedidos de producción", "El stock está bajo el mínimo y se debe pedir antes de quedarse sin producto."),
        ("=", "{F} ¿Cuántos pesos vale todo el inventario de azúcar?", "(100+150+120)*900", "Se multiplica el total de kilos por el precio por kilo.", " pesos"),
        ("abc", "En una planilla informática el stock de azúcar dice 370 kg, pero el conteo físico da 355 kg. ¿Qué corresponde?", "Investigar la diferencia de 15 kg, revisar entradas y salidas y ajustar solo con respaldo", "Cambiar el conteo físico para que calce con la planilla", "Ignorar la diferencia por ser pequeña", "La diferencia debe explicarse con los registros antes de corregir."),
    ],
    ctx=("abc", "{F} La jefa de bodega nota que el lote C está en la entrada y el lote A al fondo. ¿Qué ajuste corresponde?", "Reubicar para que el lote A, que vence antes, quede al frente y salga primero", "Dejarlo así, porque el lote C es el que más se ve", "Retirar el lote C para renovar su etiqueta", "Con FEFO debe salir primero el lote que vence antes, y el orden físico debe facilitarlo."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué significa FEFO?", "Primero en vencer, primero en salir", "Ordena la salida según la fecha de vencimiento."),
        ("¿Cómo se calcula el valor de un lote?", "Multiplicando los kilos por el precio por kilo", "Cantidad por precio da el valor del lote."),
        ("¿Qué se hace si el conteo físico no coincide con el registro?", "Se investiga la diferencia y se ajusta con respaldo", "Así se evita ocultar un problema real."),
    ],
    op=("Inventario de sal de ejemplo: lote P, 60 kg, con 30 días de vida útil restante; lote Q, 40 kg, con 80 días; lote R, 100 kg, con 50 días. Precio de ejemplo: $700 por kg. Consumo: 50 kg por semana; el stock mínimo es el consumo de una semana. "
        "Escribe: (a) el orden de salida según FEFO, (b) el stock total y si está sobre el mínimo, (c) el valor del lote R y (d) qué harías si el conteo físico da 190 kg y la planilla dice 200 kg.",
        "(a) P, luego R, luego Q (30, 50 y 80 días). (b) 60 + 40 + 100 = 200 kg, que supera el mínimo de 50 kg. (c) 100 × 700 = 70.000 pesos. (d) Investigar la diferencia de 10 kg, revisar entradas y salidas y ajustar solo con respaldo.",
        ["ordena los lotes con FEFO", "calcula stock y valor correctamente", "propone investigar la diferencia con respaldo"],
        ["hoja con las cuatro respuestas"],
        ["ordenar por kilos", "ordenar por orden alfabético de los lotes", "ajustar la planilla sin investigar"],
        "Pregunta: «¿por qué sale primero el lote P?». Debe decir que es el que vence antes."),
    reinforce="Inventa tres lotes de un insumo con sus días de vida útil y ordénalos según FEFO.",
    extend="Explica con un ejemplo inventado cuándo PEPS y FEFO dan el mismo orden y cuándo dan órdenes distintos.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (flujo general de una planta de ejemplo, inventada). Etapas en orden: recepción de materia prima, preparación, tratamiento de conservación, envasado, rotulado, almacenamiento y despacho. "
     "El jefe de producción coordina el trabajo; el jefe de calidad revisa los registros y decide si un lote se libera; los operarios trabajan bajo supervisión y solo con equipos para los que están autorizados. "
     "Peligros que se vigilan: biológicos (microbios), químicos (restos de limpieza, aditivos mal usados) y físicos (trozos de vidrio o metal). La autoridad sanitaria fiscaliza el cumplimiento de la norma sanitaria vigente.")
build(
    O2, 1, F,
    use="Aprenderé a situar el flujo de elaboración de una planta de alimentos: etapas generales, para qué se conserva un alimento, qué peligros se vigilan y qué rol responde por cada etapa.",
    prior=["Conozco las tareas de recepción de materias primas.", "Sé leer una ficha con datos.", "Sé sumar y restar cantidades."],
    explain=[
        "La elaboración industrial transforma materias primas en productos terminados siguiendo un flujo de proceso: una secuencia de etapas, como recepción, preparación, tratamiento de conservación, envasado, rotulado, almacenamiento y despacho. Cada etapa tiene un responsable y deja registros. Este cuaderno describe el flujo en general y no enseña a elaborar, porque los procedimientos y los parámetros reales los define el docente de la especialidad y la norma vigente.",
        "Conservar un alimento es alargar su vida útil evitando que se descomponga. Los métodos se agrupan por lo que hacen: conservación por frío, por calor, por retiro de agua (deshidratación), por fermentación y por aditivos. Un aditivo es una sustancia que se agrega a un alimento con una función tecnológica y que debe declararse en el rótulo. Aquí solo se estudian sus nombres y su finalidad.",
        "Los peligros se clasifican en biológicos (microbios), químicos (restos de productos de limpieza o aditivos mal usados) y físicos (trozos de vidrio o metal). Las máquinas, la esterilización y las cámaras de frío exigen personal capacitado y autorizado." + LIMX,
    ],
    vocab=[("flujo de proceso", "secuencia de etapas por las que pasa el producto"), ("conservación", "conjunto de métodos que alargan la vida útil de un alimento"), ("deshidratación", "retiro de agua para alargar la vida útil"), ("aditivo", "sustancia que se agrega a un alimento con una función tecnológica y debe declararse"), ("peligro biológico", "microbios que pueden dañar la salud"), ("peligro físico", "objeto extraño, como vidrio o metal, en el alimento")],
    worked=[
        ("Ubicar una etapa", "En el flujo de una planta de ejemplo, ¿qué va antes: envasado o tratamiento de conservación?", ["El tratamiento actúa sobre el producto antes de cerrarlo.", "Después viene el envasado."], "Primero el tratamiento de conservación"),
        ("Clasificar un peligro", "Aparece un trozo de plástico duro dentro de un producto. ¿Qué tipo de peligro es?", ["Es un objeto extraño en el alimento.", "Eso corresponde a un peligro físico."], "Peligro físico"),
    ],
    mistakes=[("Pensar que un producto sellado ya no puede descomponerse.", "El envase protege, pero un producto contaminado o un cierre dañado pueden descomponerse igual.", "Considera que cada etapa cuenta y que el cierre también se revisa."),
              ("Regular un equipo «porque ya vi cómo se hace».", "Sin autorización ni capacitación hay riesgo de accidente y de dañar el producto.", "Pide que lo haga personal autorizado y avisa a la jefatura.")],
    T=[
        ("abc", "{F} ¿Qué etapa va inmediatamente después del tratamiento de conservación?", "El envasado", "La recepción de materia prima", "El despacho", "La ficha ordena el flujo: tratamiento y luego envasado."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué busca la conservación de un alimento?", "Alargar su vida útil evitando que se descomponga", "Mejorar siempre su sabor", "Aumentar el peso del producto final", "Conservar es proteger el alimento del deterioro por más tiempo."),
        ("abc", "{F} ¿Quién decide si un lote se libera?", "El jefe de calidad", "Un operario nuevo", "El jefe de producción", "La ficha asigna esa decisión al jefe de calidad, que revisa los registros."),
        ("abc", "En Elaboración Industrial de Alimentos: la refrigeración y la congelación, ¿a qué grupo de métodos pertenecen?", "Conservación por frío", "Conservación por calor", "Conservación por deshidratación", "Ambas usan el frío para retardar el deterioro del alimento."),
        ("abc", "En Elaboración Industrial de Alimentos: el secado de frutas, ¿a qué grupo pertenece?", "Conservación por retiro de agua (deshidratación)", "Conservación por frío", "Conservación por aditivos", "El secado reduce el agua disponible, que es lo que define la deshidratación."),
        ("abc", "{F} ¿Cuál de estos hallazgos corresponde a un peligro físico?", "Un trozo de vidrio de un frasco roto en el producto", "Microbios presentes en el producto", "Restos de producto de limpieza en el alimento", "El vidrio es un objeto extraño; los microbios son biológicos y los restos de limpieza, químicos."),
        ("abc", "{F} Un operario nuevo quiere regular un equipo del tratamiento porque cree saber cómo se hace. ¿Qué corresponde?", "No intervenir y pedir que lo haga personal autorizado", "Hacerlo con cuidado y avisar después", "Hacerlo si se trata de un ajuste pequeño", "La ficha indica que solo se opera con equipos para los que se está autorizado."),
        ("=", "Un turno de ejemplo terminó 1.250 envases y se descartaron 45 por defectos. ¿Cuántos envases quedaron aprobados?", "1250-45", "A los envases terminados se les restan los descartados.", " envases"),
        ("abc", "{F} Restos de un producto de limpieza aparecen en el alimento. ¿Qué tipo de peligro es?", "Un peligro químico", "Un peligro físico", "Un peligro biológico", "Los restos de limpieza son sustancias químicas que no deben estar en el alimento."),
        ("abc", "Un compañero dice: «Si el producto está en envase sellado, ya no puede descomponerse ni contaminarse». ¿Qué observación es correcta?", "El envase protege, pero si el producto entró contaminado o el cierre falla, puede descomponerse igual", "Es correcto, porque el sellado elimina todos los riesgos", "Solo ocurre en productos congelados", "El envase es una barrera, no una garantía; el producto debe ser seguro antes de sellarlo."),
        ("abc", "{F} Si un lote sale con un defecto, ¿qué permite el registro de cada etapa?", "Ubicar en qué etapa pudo originarse y qué lotes se afectaron", "Corregir el defecto sin avisar a nadie", "Reducir la cantidad que se produce", "Los registros por etapa sirven para rastrear dónde ocurrió el problema."),
        ("=", "Un turno de ejemplo con tres líneas terminó 800, 950 y 1.100 envases, y se descartaron 60 en total. ¿Cuántos envases quedaron?", "800+950+1100-60", "Se suman los envases de las líneas y se restan los descartados.", " envases"),
        ("abc", "{F} El jefe de producción pide acelerar el envasado y dejar los registros «para después». ¿Qué respuesta es correcta?", "Los registros se hacen en cada etapa, porque después no se sabrá qué se hizo ni quién lo hizo", "Es correcto, porque la producción es lo urgente", "Basta con registrar al final de la semana", "El registro oportuno respalda el trabajo y permite rastrear problemas."),
    ],
    ctx=("abc", "{F} Una planta de ejemplo recibe una queja: un cliente encontró un trozo de metal en un frasco. ¿Qué paso corresponde?", "Conservar el reclamo, revisar los registros del lote y avisar al jefe de calidad", "Descartar la queja si el lote ya se vendió", "Retirar solo ese frasco y no revisar el lote", "Un peligro físico puede afectar a todo el lote, por lo que se investiga con los registros."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es un flujo de proceso?", "Una secuencia de etapas por las que pasa el producto", "Ordena el trabajo y permite ubicar dónde ocurre un problema."),
        ("¿Qué tipos de peligro se vigilan en la ficha?", "Biológicos, químicos y físicos", "Son las tres categorías en que se agrupan los peligros."),
        ("¿Quién opera los equipos de la planta?", "Solo personal autorizado y capacitado", "Operar sin autorización arriesga accidentes y daños al producto."),
    ],
    op=("Una planta de ejemplo recibe cuatro avisos en un turno: (1) un trozo de vidrio apareció en un envase, (2) un lote de materia prima llegó con signos de microbios, (3) se detectaron restos de producto de limpieza en una bandeja y (4) un operario nuevo intentó ajustar un equipo sin autorización. "
        "Escribe: (a) qué tipo de peligro es cada aviso, (b) quién debe ser informado en cada caso y (c) por qué se anota todo en un registro.",
        "(a) 1 es físico, 2 es biológico, 3 es químico y 4 es un riesgo de seguridad del trabajador. (b) El jefe de calidad en los tres primeros avisos y el jefe de producción o supervisor en el cuarto. (c) Porque el registro permite saber qué ocurrió, en qué etapa y qué lotes se afectaron.",
        ["clasifica los cuatro avisos", "indica a quién avisar", "explica el sentido del registro"],
        ["hoja con las tres respuestas"],
        ["decir que el vidrio es un peligro biológico", "no avisar al supervisor en el cuarto caso", "pensar que registrar es perder tiempo"],
        "Pregunta: «¿qué pasa si nadie anota el trozo de vidrio?». Debe responder que no se podrá rastrear el lote."),
    reinforce="Escribe el flujo de una planta de alimentos inventada con cinco etapas y un responsable para cada una.",
    extend="Explica con un ejemplo inventado cómo un registro por etapa ayuda a encontrar la causa de un defecto.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (balance de materia de un lote de ejemplo, inventado). Lote 7 del producto Z: entran 500 kg de materia prima; en la preparación se pierden 60 kg (descarte y recortes); en el tratamiento de conservación se pierden 15 kg; se obtienen 425 kg de producto envasado. "
     "Envase primario: el que está en contacto con el producto. Envase secundario o embalaje: el que agrupa varios envases para protegerlos y transportarlos. Funciones del envase: contener, proteger, informar y facilitar el transporte.")
build(
    O2, 2, F,
    use="Aprenderé el vocabulario de la elaboración en papel: diagrama de flujo, balance de materia, merma, rendimiento y tipos y funciones de los envases.",
    prior=["Conozco las etapas generales de una planta de alimentos.", "Sé calcular porcentajes sencillos con enteros.", "Sé leer una tabla breve."],
    explain=[
        "Un diagrama de flujo muestra con cajas y flechas las etapas por las que pasa el producto. El balance de materia compara lo que entra con lo que sale: la materia prima que entra es igual al producto obtenido más las mermas. La merma es la pérdida de materia o producto durante el proceso, como descartes, recortes o evaporación, y se registra por etapa.",
        "El rendimiento es la relación entre el producto obtenido y la materia prima usada, y se expresa en porcentaje: producto obtenido por 100, dividido por la materia prima. Si entran 100 kg y se obtienen 80 kg, el rendimiento es 80 %. Un buen balance cuadra: nada desaparece sin registrarse.",
        "El envase cumple cuatro funciones: contener, proteger, informar y facilitar el transporte. El envase primario está en contacto con el producto; el envase secundario o embalaje agrupa varios envases. Los métodos concretos de elaboración y envasado los enseña el docente de la especialidad con la norma vigente." + LIMX,
    ],
    vocab=[("diagrama de flujo", "esquema de cajas y flechas con las etapas del proceso"), ("balance de materia", "comparación entre lo que entra y lo que sale del proceso"), ("merma", "pérdida de materia o producto durante el proceso"), ("rendimiento", "relación entre el producto obtenido y la materia prima usada, en porcentaje"), ("envase primario", "el que está en contacto con el producto"), ("embalaje", "envase que agrupa y protege varios envases para el transporte")],
    worked=[
        ("Calcular un rendimiento", "En un lote de ejemplo entran 200 kg de materia prima y se obtienen 160 kg de producto envasado. ¿Cuál es el rendimiento?", ["Se divide el producto obtenido por la materia prima y se expresa en porcentaje.", "160 × 100 ÷ 200 = 80."], "80 %"),
        ("Calcular la merma", "Entran 300 kg de materia prima y se obtienen 270 kg de producto. ¿Cuánto fue la merma total?", ["La merma es lo que entra menos lo que sale como producto.", "300 − 270 = 30."], "30 kg"),
    ],
    mistakes=[("Calcular el rendimiento dividiendo la materia prima por el producto obtenido.", "Así el resultado supera el 100 % y no mide lo que se aprovechó.", "Divide el producto obtenido por la materia prima y multiplica por 100."),
              ("Dejar sin registrar una merma pequeña «porque es poco».", "El balance de materia deja de cuadrar y no se sabe en qué etapa se pierde.", "Registra cada merma con su etapa y su causa.")],
    T=[
        ("=", "{F} ¿Cuántos kg de producto envasado se obtienen según el balance, si se restan las dos mermas a la materia prima?", "500-60-15", "A lo que entra se le restan las mermas registradas.", " kg"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es la merma?", "La pérdida de materia o producto durante el proceso", "El producto que se devuelve al proveedor", "El producto que se guarda como muestra", "La merma es la parte que se pierde en las etapas del proceso."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué mide el rendimiento?", "La relación entre el producto obtenido y la materia prima usada", "El tiempo que demora el proceso", "El costo del producto por kilo", "El rendimiento compara cuánto producto se obtuvo con cuánta materia prima entró."),
        ("=", "{F} ¿Cuántos kg suman las mermas del lote 7?", "60+15", "Se suman las pérdidas de preparación y de tratamiento.", " kg"),
        ("=", "{F} ¿Cuál es el rendimiento del lote 7, en porcentaje?", "425*100//500", "Se divide el producto obtenido por la materia prima y se multiplica por 100.", " %"),
        ("abc", "{F} ¿En qué etapa del lote 7 hubo más merma?", "En la preparación, con 60 kg", "En el tratamiento, con 15 kg", "En el envasado, con 425 kg", "60 kg supera a 15 kg; los 425 kg son el producto obtenido y no una merma."),
        ("=", "En otro lote de ejemplo entran 600 kg de materia prima y se obtienen 540 kg de producto envasado. ¿Cuál es el rendimiento, en porcentaje?", "540*100//600", "Se divide el producto obtenido por la materia prima y se multiplica por 100.", " %"),
        ("abc", "En Elaboración Industrial de Alimentos: además de contener el producto, ¿qué función cumple el envase?", "Proteger el producto e informar al consumidor mediante el rótulo", "Aumentar la cantidad de producto", "Reemplazar el control de calidad", "El envase protege del deterioro y es soporte del rótulo con la información."),
        ("abc", "{F} Una caja de cartón agrupa 12 frascos para el transporte. ¿Cómo se clasifica la caja?", "Como envase secundario o embalaje", "Como envase primario", "Como materia prima", "La caja agrupa envases y no toca el producto, por lo que es embalaje."),
        ("abc", "{F} El lote 7 tuvo 85 % de rendimiento y otro lote de ejemplo tuvo 90 %. ¿Qué es lo más razonable?", "Revisar en qué etapas difieren las mermas antes de sacar conclusiones", "Concluir que el segundo lote se elaboró mejor sin revisar nada", "Descartar los registros del primer lote", "El balance por etapa muestra dónde ocurre la diferencia, que es lo que permite mejorar."),
        ("abc", "En otro balance de materia, entran 500 kg y la suma del producto y de las mermas registradas da 480 kg. ¿Qué indica?", "Faltan 20 kg por registrar o hay un error de pesaje, y debe revisarse", "Que hubo 20 kg de ganancia de producto", "Que el balance está correcto porque se acerca", "Un balance correcto cuadra; una diferencia sin explicar exige revisión."),
        ("=", "Entran 900 kg de materia prima; las mermas son 90 kg en la preparación y 45 kg en el tratamiento, y se descartan 15 kg más por control de calidad. ¿Cuántos kg de producto aprobado se obtienen?", "900-90-45-15", "A lo que entra se le restan todas las mermas y el descarte.", " kg"),
        ("abc", "Lote P: entran 400 kg y se obtienen 340 kg. Lote Q: entran 500 kg y se obtienen 410 kg. ¿Qué lote tiene mayor rendimiento?", "El lote P, con 85 %", "El lote Q, con 82 %, porque produjo más kilos", "Ambos tienen el mismo rendimiento", "El rendimiento compara con la materia prima usada: 340 sobre 400 es 85 % y 410 sobre 500 es 82 %."),
    ],
    ctx=("=", "{F} La jefa quiere obtener 850 kg de producto envasado con el mismo rendimiento del lote 7. ¿Cuántos kg de materia prima necesita?", "850*100//85", "Se divide el producto deseado por el rendimiento del lote y se multiplica por 100.", " kg"),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calcula el rendimiento?", "Producto obtenido por 100, dividido por la materia prima", "Se expresa en porcentaje de lo que se aprovechó."),
        ("¿Qué es el embalaje?", "El envase que agrupa y protege varios envases para el transporte", "No toca el producto: solo agrupa y protege varios envases."),
        ("¿Qué debe hacer un balance de materia?", "Cuadrar: lo que entra es igual al producto más las mermas", "Nada puede desaparecer sin registro: todo lo que entra debe salir como producto o merma."),
    ],
    op=("Balance de ejemplo de un lote: entran 800 kg de materia prima; en la preparación se pierden 100 kg; en el tratamiento, 40 kg; en el envasado, 20 kg. "
        "Escribe: (a) cuántos kg de producto envasado se obtienen, (b) la merma total, (c) el rendimiento en porcentaje y (d) en qué etapa se concentra la mayor merma y por qué conviene registrarla por etapa.",
        "(a) 800 − 100 − 40 − 20 = 640 kg. (b) 100 + 40 + 20 = 160 kg. (c) 640 × 100 ÷ 800 = 80 %. (d) En la preparación, con 100 kg; el registro por etapa permite ver dónde se pierde más y qué mejorar.",
        ["calcula 640 kg y 160 kg", "obtiene 80 % de rendimiento", "identifica la etapa con mayor merma y justifica el registro"],
        ["hoja con los cuatro cálculos"],
        ["dividir al revés y obtener más de 100 %", "olvidar sumar una merma", "no justificar el registro"],
        "Pregunta: «¿cómo sabrías si falta anotar una merma?». Debe responder que el balance no cuadraría."),
    reinforce="Dibuja un diagrama de flujo de cinco cajas para una planta inventada y anota una merma de ejemplo en cada etapa.",
    extend="Explica por qué dos lotes con distinto rendimiento deben compararse etapa por etapa y no solo por el resultado final.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (tabla de dos lotes del producto M, de ejemplo e inventada). Lote 21: entran 1.000 kg; mermas de 120 kg en preparación, 30 kg en tratamiento y 10 kg en envasado; se obtienen 840 kg. "
     "Lote 22: entran 1.000 kg; mermas de 80 kg en preparación, 35 kg en tratamiento y 85 kg en envasado; se obtienen 800 kg. "
     "Nota del operario del lote 22 en envasado: «frascos rotos y producto derramado». Meta de ejemplo de la planta: rendimiento de al menos 82 %.")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel el balance de materia de dos lotes: calcular rendimiento y mermas por etapa, ubicar el problema y proponer una mejora relacionada con la causa registrada.",
    prior=["Conozco el balance de materia y la merma.", "Sé calcular porcentajes con enteros.", "Sé leer una tabla breve."],
    explain=[
        "Para analizar un lote se calcula su rendimiento y se compara con la meta de la planta. Si no se cumple, se mira la merma de cada etapa para ubicar dónde se pierde más. Esa comparación es más útil que mirar solo el resultado final, porque indica qué etapa revisar. La meta de este cuaderno es un valor de ejemplo.",
        "La causa de una merma debe quedar anotada junto con el número: «frascos rotos y producto derramado» explica mucho más que un «85» solo. Con la causa se propone una acción correctiva, es decir, una medida que ataca el origen del problema, como revisar el estado de los frascos o el cierre. Aumentar la materia prima de entrada para compensar solo oculta el problema y sube los costos.",
        "Cada lote lleva su registro firmado por el responsable. Si la causa de una merma es un equipo, la revisión la hace personal autorizado de mantención, no el operario por su cuenta." + LIMX,
    ],
    vocab=[("meta de rendimiento", "valor mínimo de rendimiento que la planta espera lograr"), ("merma por etapa", "pérdida registrada en cada etapa del proceso"), ("causa", "origen de un problema o de una pérdida"), ("acción correctiva", "medida que ataca la causa de un problema"), ("desviación", "diferencia entre lo obtenido y lo esperado")],
    worked=[
        ("Comparar con la meta", "Un lote de ejemplo tiene rendimiento de 83 % y la meta es de 85 %. ¿Cumple la meta?", ["Se compara el resultado con la meta.", "83 es menor que 85."], "No cumple la meta"),
        ("Ubicar la etapa", "Un lote de ejemplo perdió 40 kg en preparación, 90 kg en tratamiento y 20 kg en envasado. ¿En qué etapa se pierde más?", ["Se comparan las tres mermas.", "90 es el mayor valor."], "En el tratamiento"),
    ],
    mistakes=[("Anotar solo el número de la merma, sin la causa.", "Sin causa no se puede decidir qué corregir.", "Anota el número, la etapa y la causa observada."),
              ("Subir la cantidad de materia prima de entrada para «compensar» una merma.", "Se tapa el síntoma, se gasta más y la causa sigue.", "Busca la causa y aplica una acción correctiva en esa etapa.")],
    T=[
        ("=", "{F} ¿Cuál es el rendimiento del lote 21, en porcentaje?", "840*100//1000", "Se divide el producto obtenido por la materia prima y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué lote cumple la meta de 82 %?", "El lote 21", "El lote 22", "Ambos lotes", "El lote 21 tiene 84 %, mientras que el lote 22 tiene 80 %, por debajo de la meta."),
        ("abc", "{F} ¿En qué etapa del lote 22 hubo más merma?", "En el envasado, con 85 kg", "En la preparación, con 80 kg", "En el tratamiento, con 35 kg", "85 kg es la mayor de las tres mermas del lote 22."),
        ("=", "{F} ¿Cuántos kg suman las mermas del lote 22?", "80+35+85", "Se suman las mermas de las tres etapas.", " kg"),
        ("abc", "{F} ¿Qué causa se registró para la merma en el envasado del lote 22?", "Frascos rotos y producto derramado", "Evaporación durante el tratamiento", "Cáscaras y recortes de la preparación", "La nota del operario describe esa causa para el envasado."),
        ("=", "{F} ¿Cuántos kg más se perdieron en la preparación del lote 21 que en la del lote 22?", "120-80", "Se resta la merma del lote 22 a la del lote 21.", " kg"),
        ("=", "{F} Para alcanzar la meta de 82 % el lote 22 debía obtener 820 kg. ¿Cuántos kg le faltaron?", "820-800", "A lo necesario para la meta se le resta lo obtenido.", " kg"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿por qué se comparan las mermas etapa por etapa y no solo el rendimiento final?", "Porque muestra dónde ocurre el problema y qué conviene corregir", "Porque el rendimiento final no se puede calcular sin ellas", "Porque cada etapa tiene su propia meta de precio", "El detalle por etapa orienta la acción correctiva."),
        ("abc", "{F} ¿Qué acción corresponde a la causa registrada en el envasado del lote 22?", "Revisar el estado de los frascos y el cierre en el envasado con el responsable", "Reducir el tamaño de las piezas en la preparación", "Aumentar la materia prima de entrada para compensar", "La acción correctiva debe atacar la causa anotada, que está en el envasado."),
        ("abc", "{F} Un jefe propone subir la entrada de materia prima a 1.100 kg para compensar las mermas del lote 22. ¿Qué observación es correcta?", "Compensa el síntoma, pero no corrige la causa y sube los costos", "Resuelve el problema por completo", "Es lo único que se puede hacer con una merma", "Entrar más materia no cambia lo que se pierde en el envasado."),
        ("abc", "El operario del lote 22 anotó «85» en el envasado sin explicar la causa. ¿Qué falta en el registro?", "La causa de la merma y la firma, para poder analizarla y corregirla", "Nada, porque basta con el número", "Cambiar el número a 35 para igualar el tratamiento", "El número sin causa no permite decidir qué mejorar."),
        ("=", "{F} Si el lote 22 hubiera perdido solo 35 kg en el envasado y lo demás igual, ¿cuántos kg habría obtenido?", "1000-80-35-35", "A la entrada se le restan las mermas ajustadas de las tres etapas.", " kg"),
        ("=", "{F} Si cada kg de materia prima perdido en el lote 21 tuvo un costo de ejemplo de $350, ¿cuántos pesos se perdieron por la merma total?", "(120+30+10)*350", "Se suma la merma total y se multiplica por el costo por kilo.", " pesos"),
    ],
    ctx=("abc", "{F} El jefe dice: «el lote 22 está bien porque salió producto». ¿Qué respuesta corresponde?", "Salió producto, pero su rendimiento quedó bajo la meta y hay una causa que revisar", "Tiene razón, porque la planta produjo", "El rendimiento no importa si hay producto", "Cumplir la meta y entender la causa de la merma es parte del control del proceso."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se ubica la etapa con más problema en un lote?", "Comparando la merma de cada etapa", "La mayor merma indica dónde mirar primero."),
        ("¿Qué debe anotarse junto al número de una merma?", "La etapa y la causa observada", "Con la causa se decide la acción correctiva."),
        ("¿Qué es una acción correctiva?", "Una medida que ataca la causa del problema", "No tapa el síntoma: corrige el origen."),
    ],
    op=("Datos de ejemplo de dos lotes del producto N, ambos con 600 kg de entrada. Lote 31: mermas de 40 kg en preparación, 15 kg en tratamiento y 5 kg en envasado. Lote 32: mermas de 45 kg en preparación, 65 kg en tratamiento y 10 kg en envasado; nota del operario en tratamiento: «equipo detenido y producto sobrante». La meta de ejemplo es 85 %. "
        "Escribe: (a) el producto obtenido y el rendimiento de cada lote, (b) qué lote cumple la meta, (c) en qué etapa se concentra el problema del lote que no cumple y (d) una acción correctiva relacionada con la causa anotada.",
        "(a) Lote 31: 600 − 60 = 540 kg, rendimiento 90 %. Lote 32: 600 − 120 = 480 kg, rendimiento 80 %. (b) Cumple el lote 31. (c) En el tratamiento del lote 32, con 65 kg. (d) Pedir que personal autorizado de mantención revise el equipo detenido y registrar la causa.",
        ["calcula los productos obtenidos", "compara con la meta", "relaciona la causa con una acción correctiva"],
        ["hoja con las cuatro respuestas"],
        ["compensar con más materia prima", "no usar la nota del operario", "sumar mal las mermas"],
        "Pregunta: «¿por qué la acción debe tocar el tratamiento?». Debe responder que ahí está la mayor merma y su causa."),
    reinforce="Inventa un lote con tres mermas por etapa y calcula su rendimiento y la etapa con más pérdida.",
    extend="Explica con un ejemplo inventado la diferencia entre compensar una merma y corregir su causa.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (orden de producción de ejemplo, inventada). Lote de 2.000 envases. Costos de ejemplo: 600 kg de materia prima a $900 por kg; insumos por $120.000; 2.000 envases a $150 cada uno; mano de obra por $380.000. "
     "Control de calidad del envasado: se revisa una muestra de 80 envases y el lote se acepta si hay como máximo 2 defectuosos en la muestra (criterio de ejemplo). En la muestra de este lote se encontraron 3 defectuosos. Precio de venta de ejemplo: $1.000 por envase.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo: calcular el costo de un lote y el costo por envase, y decidir con una muestra si un lote envasado se acepta.",
    prior=["Conozco el balance de materia y el rendimiento.", "Sé multiplicar y dividir enteros.", "Sé comparar un dato con un límite."],
    explain=[
        "El costo de producción de un lote es la suma de sus gastos: materia prima, insumos, envases y mano de obra. Se calcula multiplicando cada cantidad por su precio y sumando. El costo por unidad se obtiene dividiendo el costo total por la cantidad de unidades buenas. Con el precio de venta se calcula la diferencia por unidad, que debe cubrir también otros gastos de la empresa.",
        "El control de calidad del envasado usa una muestra: se revisan algunos envases y se cuenta cuántos son defectuosos. Si el número supera el máximo del criterio, el lote se retiene para decidir qué hacer con él según el procedimiento del jefe de calidad. Revisar todo envase de un lote grande tomaría demasiado tiempo, por eso se usa la muestra.",
        "Un envase más barato puede ahorrar dinero, pero solo sirve si sigue cumpliendo sus funciones de contener y proteger y cumple la norma. Cuando se descartan envases, el costo total se reparte entre menos unidades buenas, así que el costo por unidad sube." + LIM,
    ],
    vocab=[("costo de producción", "suma de los gastos para producir un lote"), ("costo por unidad", "costo total dividido por las unidades buenas"), ("muestra", "porción del lote que se revisa para decidir"), ("defectuoso", "envase que no cumple el criterio de calidad"), ("retener un lote", "mantenerlo apartado hasta decidir su destino")],
    worked=[
        ("Costo por unidad", "Un lote de ejemplo de 500 envases tuvo un costo total de $200.000. ¿Cuánto cuesta cada envase?", ["El costo por unidad se obtiene dividiendo el total por las unidades.", "200.000 ÷ 500 = 400."], "$400 por envase"),
        ("Decidir con una muestra", "El criterio de ejemplo de un lote es como máximo 1 defectuoso en una muestra de 50. En la muestra hay 2 defectuosos. ¿Se acepta?", ["Se compara lo encontrado con el máximo.", "2 supera a 1."], "No se acepta: se retiene el lote"),
    ],
    mistakes=[("Elegir un envase más barato sin revisar si cumple su función de proteger.", "El ahorro se pierde si el producto se daña o no cumple la norma.", "Evalúa primero que el envase proteja y cumpla la norma, y después compara precios."),
              ("Suponer que el costo por envase no cambia cuando se descartan envases.", "El mismo gasto se reparte entre menos envases buenos.", "Divide el costo total por los envases buenos.")],
    T=[
        ("=", "{F} ¿Cuántos pesos cuesta la materia prima del lote?", "600*900", "Se multiplican los kilos por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan los envases del lote?", "2000*150", "Se multiplica la cantidad de envases por el precio de cada uno.", " pesos"),
        ("abc", "{F} Según el criterio de ejemplo, ¿cuántos defectuosos se aceptan como máximo en la muestra?", "Como máximo 2", "Como máximo 3", "Ninguno", "El criterio de la ficha fija un máximo de 2 en una muestra de 80."),
        ("=", "{F} ¿Cuál es el costo total del lote, en pesos?", "600*900+120000+2000*150+380000", "Se suman materia prima, insumos, envases y mano de obra.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta cada envase si se divide el costo total por los 2.000 envases?", "(600*900+120000+2000*150+380000)//2000", "El costo por unidad es el costo total dividido por las unidades.", " pesos"),
        ("abc", "{F} ¿Qué decisión corresponde con los 3 defectuosos encontrados?", "Retener el lote para decidir su destino, porque supera el máximo de 2", "Aceptarlo, porque 3 de 80 es poco", "Despachar el lote y descartar solo los 3 envases sin registrar", "Se encontró más que el máximo del criterio, así que el lote no se acepta sin evaluación."),
        ("=", "{F} ¿Cuántos pesos queda de diferencia por envase entre el precio de venta y el costo por envase?", "1000-(600*900+120000+2000*150+380000)//2000", "Al precio de venta se le resta el costo por unidad.", " pesos"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿por qué se revisa una muestra y no todos los envases de un lote grande?", "Porque revisar todo lleva demasiado tiempo y la muestra permite decidir sobre el lote", "Porque los envases de un lote nunca se pueden revisar", "Porque la muestra reemplaza el rótulo de cada envase", "La muestra es una porción representativa que permite juzgar el lote completo."),
        ("=", "En un lote de ejemplo se retienen 60 envases defectuosos cuyo costo unitario es de $670. ¿Cuántos pesos de costo quedan comprometidos en esos envases?", "60*670", "Se multiplica la cantidad de envases por su costo unitario.", " pesos"),
        ("abc", "Un compañero propone cambiar a un envase más barato sin revisar si protege el producto. ¿Qué respuesta es correcta?", "Primero hay que evaluar que cumpla su función de proteger y la norma, y después comparar precios", "Corresponde cambiarlo siempre, porque el ahorro es lo principal", "No se debe cambiar nunca de envase", "Un envase barato que no protege termina costando más por productos dañados."),
        ("abc", "{F} Si se descartan 100 envases y el costo total no cambia, ¿qué ocurre con el costo por envase bueno?", "Sube, porque el mismo gasto se reparte entre menos envases buenos", "Baja, porque hay menos envases", "Se mantiene, porque el costo total no cambia", "Dividir el mismo costo entre menos unidades da un resultado mayor."),
        ("=", "Un nuevo lote de ejemplo de 2.500 envases buenos mantiene un costo por envase de $670. ¿Cuál es el costo total, en pesos?", "2500*670", "El costo total se obtiene multiplicando el costo por unidad por las unidades.", " pesos"),
        ("abc", "En otro lote, la muestra de 80 envases tiene 2 defectuosos y el máximo del criterio de la ficha es 2. ¿Qué decisión corresponde?", "Aceptar el lote, porque cumple el máximo del criterio", "Retener el lote, porque hay defectuosos", "Repetir la muestra hasta que no haya ninguno", "El criterio permite hasta 2 defectuosos, y 2 no lo supera."),
    ],
    ctx=("abc", "{F} Un cliente pide bajar el precio de venta a $650 por envase. ¿Qué observación corresponde?", "A $650 se vendería bajo el costo de $670 por envase y habría pérdida", "A $650 todavía habría ganancia, porque 650 es más que la mitad de 1.000", "El precio de venta no tiene relación con el costo", "El costo por envase calculado en la ficha es $670, que supera a $650."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calcula el costo por unidad?", "Dividiendo el costo total por las unidades buenas", "Así se reparte el gasto total entre lo que sí se puede vender."),
        ("¿Qué se hace con un lote cuya muestra supera el máximo de defectuosos?", "Se retiene para decidir su destino", "No se despacha mientras no se evalúe según el procedimiento."),
        ("¿Qué pasa con el costo por envase si se descartan envases?", "Sube", "El mismo costo total se divide entre menos envases buenos."),
    ],
    op=("Lote de ejemplo de 1.000 envases. Costos: 300 kg de materia prima a $800 por kg, insumos por $60.000, 1.000 envases a $120 cada uno y mano de obra por $200.000. Control de calidad: muestra de 50 envases; se acepta con un máximo de 1 defectuoso; en esta muestra hay 1 defectuoso. Precio de venta de ejemplo: $700 por envase. "
        "Escribe: (a) el costo total, (b) el costo por envase, (c) la decisión sobre el lote con su razón y (d) la diferencia por envase entre el precio de venta y el costo.",
        "(a) 240.000 + 60.000 + 120.000 + 200.000 = 620.000 pesos. (b) 620.000 ÷ 1.000 = 620 pesos por envase. (c) Se acepta, porque 1 defectuoso no supera el máximo de 1. (d) 700 − 620 = 80 pesos por envase.",
        ["calcula el costo total y por envase", "decide con el criterio de la muestra", "calcula la diferencia por envase"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo de los envases", "retener el lote aunque cumple el máximo", "dividir por 50 en lugar de 1.000"],
        "Pregunta: «¿qué pasaría con el costo por envase si 100 envases se descartan?». Debe decir que sube."),
    reinforce="Inventa un lote con cuatro costos y calcula su costo total y su costo por unidad.",
    extend="Explica con un ejemplo inventado por qué un envase más barato puede terminar saliendo más caro.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 9 (laboratorio de calidad de una planta de ejemplo, inventada). Análisis que se hacen: (1) humedad del producto, medida con un instrumento; (2) color y olor del producto, percibidos por un panel entrenado; (3) recuento de microorganismos, que se hace en el laboratorio. "
     "Roles: el analista de laboratorio toma y analiza las muestras; el jefe de calidad compara los resultados con el estándar y decide. Regla de la planta: toda muestra se identifica con producto, lote, fecha y nombre de quien la tomó. "
     "Las muestras no se prueban fuera de un análisis sensorial autorizado.")
build(
    O3, 1, F,
    use="Aprenderé a situar el control de calidad de una planta de alimentos: qué es la inocuidad, qué tipos de análisis existen (fisicoquímico, microbiológico y sensorial) y quién responde por ellos.",
    prior=["Conozco el flujo de una planta de alimentos.", "Sé leer una ficha con datos.", "Sé comparar un dato con un límite."],
    explain=[
        "El aseguramiento de calidad es el conjunto de acciones planificadas para que el producto cumpla los estándares de calidad e inocuidad. La inocuidad significa que el alimento no daña la salud de quien lo consume. Se vigila en las materias primas, en los productos intermedios (los que aún no terminan el proceso) y en los productos finales, siempre conforme a la normativa vigente.",
        "Hay tres grandes tipos de análisis básicos. El análisis fisicoquímico mide propiedades con instrumentos, como la humedad o el peso. El análisis microbiológico cuenta o detecta microorganismos y lo hace personal de laboratorio capacitado. El análisis sensorial evalúa con los sentidos el aspecto, el olor, el sabor y la textura; solo lo hace un panel entrenado y autorizado. Ninguno reemplaza a otro, porque cada uno detecta cosas distintas.",
        "Toda muestra se identifica con producto, lote, fecha y quién la tomó. Probar muestras para ver si están buenas fuera de un análisis autorizado es un riesgo para la salud. El jefe de calidad compara los resultados con el estándar y decide." + LIM,
    ],
    vocab=[("aseguramiento de calidad", "acciones planificadas para que el producto cumpla los estándares"), ("inocuidad", "que el alimento no daña la salud de quien lo consume"), ("análisis fisicoquímico", "medición de propiedades con instrumentos"), ("análisis microbiológico", "detección o recuento de microorganismos en laboratorio"), ("análisis sensorial", "evaluación con los sentidos por un panel entrenado"), ("producto intermedio", "producto que aún no termina el proceso")],
    worked=[
        ("Clasificar un análisis", "El laboratorio de una planta de ejemplo mide el peso de cada envase con una balanza. ¿Qué tipo de análisis es?", ["Se mide una propiedad con un instrumento.", "Eso corresponde a un análisis fisicoquímico."], "Fisicoquímico"),
        ("Distinguir sensorial y microbiológico", "Un panel entrenado evalúa el aspecto y el olor de un producto. ¿Qué tipo de análisis es?", ["Se usan los sentidos.", "Eso es un análisis sensorial, no uno microbiológico."], "Sensorial"),
    ],
    mistakes=[("Probar un poco de la muestra «para ver si está buena».", "El gusto no detecta los microbios peligrosos y se arriesga la salud.", "No pruebes muestras; el análisis sensorial lo hace un panel autorizado."),
              ("Pensar que si el producto se ve bien no hace falta el análisis microbiológico.", "Los microbios no siempre se ven ni se huelen.", "Cada análisis detecta algo distinto; se complementan.")],
    T=[
        ("abc", "{F} La humedad medida con un instrumento, ¿qué tipo de análisis es?", "Fisicoquímico", "Sensorial", "Microbiológico", "La humedad es una propiedad que se mide con un instrumento."),
        ("abc", "{F} El recuento de microorganismos, ¿qué tipo de análisis es?", "Microbiológico", "Fisicoquímico", "Sensorial", "Contar microorganismos corresponde a un análisis microbiológico de laboratorio."),
        ("abc", "{F} El color y el olor percibidos por un panel entrenado, ¿qué tipo de análisis son?", "Sensorial", "Fisicoquímico", "Microbiológico", "Se evalúan con los sentidos, lo que define el análisis sensorial."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa inocuidad?", "Que el alimento no daña la salud de quien lo consume", "Que el alimento tiene buen sabor", "Que el alimento dura más tiempo", "La inocuidad se refiere a la seguridad para la salud, no al sabor ni a la duración."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es el aseguramiento de calidad?", "El conjunto de acciones planificadas para que el producto cumpla los estándares", "La revisión del producto solo cuando ya está en el almacén", "La limpieza de la planta al terminar el turno", "Incluye acciones planificadas en todo el proceso, no solo al final."),
        ("abc", "{F} ¿Quién toma y analiza las muestras en el laboratorio de la ficha?", "El analista de laboratorio", "El jefe de calidad", "El jefe de bodega", "La ficha asigna al analista tomar y analizar; el jefe compara y decide."),
        ("abc", "{F} ¿Qué datos debe llevar la identificación de una muestra?", "Producto, lote, fecha y nombre de quien la tomó", "Producto y lote, pero no quién la tomó", "Solo el color observado", "La ficha pide los cuatro datos para poder rastrear la muestra."),
        ("abc", "{F} Un compañero propone probar una muestra para ver si está buena. ¿Qué respuesta es correcta?", "No se prueban muestras fuera de un análisis sensorial autorizado", "Está bien si la muestra se ve limpia", "Está bien si se prueba solo un trozo pequeño", "Probar sin autorización arriesga la salud, ya que el sabor no detecta peligros microbiológicos."),
        ("=", "El laboratorio de ejemplo toma 3 muestras de cada uno de 8 lotes, y una de las 3 muestras de cada lote va a análisis microbiológico. ¿Cuántas muestras no van a análisis microbiológico?", "8*3-8", "Se calculan todas las muestras y se restan las del análisis microbiológico.", " muestras"),
        ("abc", "Un lote se ve bien y huele normal. Un compañero dice que no hace falta el análisis microbiológico. ¿Qué respuesta es correcta?", "Los microbios no siempre se ven ni se huelen, por eso un análisis no reemplaza a otro", "Tiene razón, porque el análisis sensorial detecta todo", "El análisis microbiológico solo sirve para productos congelados", "Cada análisis detecta algo distinto y se complementan."),
        ("abc", "¿Por qué el estándar de calidad debe existir antes del análisis?", "Para tener con qué comparar el resultado y decidir si cumple", "Para que cada analista fije su propio criterio después de medir", "Para que el análisis sea más rápido", "Sin estándar un resultado no se puede interpretar como aceptable o no."),
        ("=", "En un día de ejemplo, el laboratorio hace por lote 5 análisis fisicoquímicos, 3 sensoriales y 2 microbiológicos. ¿Cuántos análisis hace en 4 lotes?", "(5+3+2)*4", "Se suman los análisis de un lote y se multiplican por la cantidad de lotes.", " análisis"),
        ("abc", "La acidez de un jugo medida con instrumento, el sabor percibido por un panel y el recuento de bacterias, ¿qué tipos de análisis son, en ese orden?", "Fisicoquímico, sensorial y microbiológico", "Sensorial, fisicoquímico y microbiológico", "Microbiológico, sensorial y fisicoquímico", "Medir con instrumento es fisicoquímico, percibir es sensorial y contar bacterias es microbiológico."),
    ],
    ctx=("abc", "{F} El jefe de calidad recibe estos resultados de un lote: humedad fuera del estándar, análisis sensorial conforme y análisis microbiológico conforme. ¿Qué corresponde?", "No liberar el lote hasta revisar la desviación, porque basta un parámetro fuera del estándar", "Liberarlo, porque dos de tres análisis cumplen", "Repetir solo el análisis sensorial", "Cada parámetro debe cumplir su estándar; uno fuera de rango obliga a revisar."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cuáles son los tres análisis básicos?", "Fisicoquímico, microbiológico y sensorial", "Miden propiedades, microorganismos y características percibidas."),
        ("¿Qué datos lleva la identificación de una muestra?", "Producto, lote, fecha y quién la tomó", "Permiten rastrear la muestra hasta su origen."),
        ("¿Quién compara los resultados con el estándar y decide?", "El jefe de calidad", "Tiene la responsabilidad de decidir según el estándar."),
    ],
    op=("El laboratorio de una planta de ejemplo recibe una muestra de un producto intermedio. Se pide: medir su humedad, evaluar su aspecto y olor, y contar microorganismos. "
        "Escribe: (a) qué tipo de análisis corresponde a cada petición, (b) qué datos llevaría la identificación de la muestra, (c) por qué no se prueba la muestra para decidir y (d) quién decide con los resultados.",
        "(a) Humedad: fisicoquímico. Aspecto y olor: sensorial. Recuento de microorganismos: microbiológico. (b) Producto, lote, fecha y quién la tomó. (c) Porque el sabor no detecta peligros microbiológicos y probar fuera de un análisis autorizado arriesga la salud. (d) El jefe de calidad, comparando con el estándar.",
        ["clasifica los tres análisis", "indica los datos de identificación", "explica por qué no se prueba y quién decide"],
        ["hoja con las cuatro respuestas"],
        ["confundir sensorial con microbiológico", "no mencionar al jefe de calidad", "decir que probar es la mejor prueba"],
        "Pregunta: «¿qué análisis detecta los microbios?». Debe responder el microbiológico y no el sensorial."),
    reinforce="Inventa cuatro mediciones de una planta de alimentos y clasifica cada una como fisicoquímica, microbiológica o sensorial.",
    extend="Explica con un ejemplo inventado por qué un análisis sensorial no reemplaza a uno microbiológico.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 10 (especificaciones e informe de ejemplo, inventados). Especificaciones del producto Q: humedad entre 10 % y 14 %; peso neto mínimo por envase de 500 g; sensorial con color uniforme y sin olores extraños; microbiológico dentro del estándar del laboratorio. "
     "Informe del lote 45: humedad 12 %; pesos de una muestra de 5 envases: 502 g, 498 g, 505 g, 500 g y 510 g; sensorial conforme; microbiológico conforme.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario de la calidad: parámetro, especificación, conformidad y no conformidad, y a leer un informe de resultados con su registro.",
    prior=["Conozco los tres tipos de análisis básicos.", "Sé calcular un promedio con enteros.", "Sé comparar un dato con un rango."],
    explain=[
        "Un parámetro es una característica medible o evaluable del producto, como la humedad, el peso o el color. La especificación es el requisito o el rango que ese parámetro debe cumplir, por ejemplo humedad entre 10 % y 14 %. Un resultado es conforme cuando cumple la especificación y es una no conformidad cuando no la cumple.",
        "Un informe de resultados lista por lote cada parámetro con su valor. Para leerlo se compara cada valor con su especificación. Un promedio puede ocultar valores individuales fuera de rango: si la especificación exige un mínimo por envase, cada envase debe cumplirlo. Los valores de este cuaderno son de ejemplo y no reemplazan los de la norma vigente.",
        "Un registro de calidad lleva producto, lote, fecha, parámetro, resultado y firma del analista. Un dato real no se cambia para que cuadre: si hay un error, se corrige con una anotación que explique el motivo y se firma. Ocultar una no conformidad pone en riesgo al consumidor." + LIM,
    ],
    vocab=[("parámetro", "característica medible o evaluable del producto"), ("especificación", "requisito o rango que un parámetro debe cumplir"), ("conforme", "resultado que cumple la especificación"), ("no conformidad", "resultado que no cumple la especificación"), ("registro de calidad", "documento con producto, lote, fecha, parámetro, resultado y firma")],
    worked=[
        ("Comparar con un rango", "La especificación de ejemplo de un producto pide humedad entre 8 % y 12 %, y el resultado es 13 %. ¿Es conforme?", ["Se compara con el rango.", "13 supera el máximo de 12."], "No conforme"),
        ("Calcular un promedio", "Tres envases de ejemplo pesan 504 g, 500 g y 508 g. ¿Cuál es el promedio?", ["Se suman los pesos: 504 + 500 + 508 = 1.512.", "1.512 ÷ 3 = 504."], "504 g"),
    ],
    mistakes=[("Cambiar un dato real para que el informe «cuadre».", "Se oculta una no conformidad y se pierde confianza en el registro.", "Anota el dato real; si hay error, corrígelo con una nota que explique el motivo."),
              ("Dar por conforme un lote porque el promedio cumple, aunque un envase esté bajo el mínimo.", "La especificación exige el mínimo en cada envase.", "Compara cada valor individual con la especificación.")],
    T=[
        ("abc", "{F} Con humedad de 12 %, ¿el lote 45 cumple la especificación de humedad?", "Sí, porque 12 está entre 10 % y 14 %", "No, porque 12 es menor que 14", "No, porque no llega a 14", "El resultado está dentro del rango de la especificación."),
        ("abc", "{F} ¿Cuántos envases de la muestra del lote 45 pesan menos que el mínimo?", "Uno, el de 498 g", "Dos, los de 498 g y 500 g", "Ninguno", "Solo 498 g está bajo 500 g; el de 500 g cumple el mínimo."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es una especificación?", "El requisito o rango que un parámetro debe cumplir", "El resultado de un análisis ya hecho", "El precio de un lote terminado", "La especificación fija lo que se espera; el resultado se compara con ella."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es un parámetro?", "Una característica medible o evaluable del producto", "Una máquina del laboratorio", "El nombre del analista", "La humedad, el peso o el color son parámetros del producto."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es una no conformidad?", "Un resultado que no cumple la especificación", "Un análisis que no se hizo por falta de tiempo", "Un lote que ya se vendió", "No conformidad significa no cumplir lo que la especificación exige."),
        ("=", "{F} ¿Cuántos gramos suman los pesos de los 5 envases de la muestra?", "502+498+505+500+510", "Se suman los pesos de los cinco envases.", " g"),
        ("=", "{F} ¿Cuál es el peso promedio de los 5 envases de la muestra?", "(502+498+505+500+510)//5", "El promedio es la suma de los pesos dividida por la cantidad de envases.", " g"),
        ("abc", "{F} El promedio de la muestra supera el mínimo, pero un envase pesa 498 g. ¿Cómo se clasifica ese envase?", "Como una no conformidad individual, porque cada envase debe cumplir el mínimo", "Como conforme, porque el promedio cumple", "Como un envase que se anula del informe", "La especificación se refiere a cada envase, no solo al promedio."),
        ("abc", "¿Qué datos debe llevar un registro de calidad?", "Producto, lote, fecha, parámetro, resultado y firma del analista", "Solo el resultado", "Solo la firma del jefe", "El registro debe permitir rastrear el resultado hasta su origen."),
        ("abc", "¿Por qué la especificación debe estar escrita antes de analizar?", "Para tener con qué comparar el resultado y decidir con un criterio objetivo", "Para que cada analista decida su propio criterio después de medir", "Para ahorrar tiempo de medición", "Sin especificación previa no hay criterio para decidir si un resultado es aceptable."),
        ("abc", "{F} El analista anota 500 g en lugar de 498 g «para que cuadre». ¿Qué falla?", "Se altera un dato real y se oculta una no conformidad", "Nada, porque la diferencia es de solo 2 g", "Se pierde el promedio de la muestra", "El registro debe reflejar el dato medido, aunque sea desfavorable."),
        ("=", "En una muestra de ejemplo de 10 envases, 7 pesan 500 g o más y el resto pesa menos. ¿Qué porcentaje de los envases no cumple el mínimo?", "(10-7)*100//10", "Se calcula la cantidad que no cumple y se expresa como porcentaje del total.", " %"),
        ("abc", "{F} Otro lote tiene humedad de 15 %. ¿Cómo se clasifica este resultado?", "Como no conformidad, porque supera el máximo de 14 %", "Como conforme, porque está cerca del rango", "Como conforme si el análisis sensorial es normal", "La especificación fija un máximo de 14 %, y 15 % lo supera."),
    ],
    ctx=("abc", "{F} El jefe de calidad ve que el informe del lote 45 contiene una no conformidad de peso en un envase. ¿Qué decisión inicial corresponde?", "Retener el lote, registrar la no conformidad y evaluarla según el procedimiento", "Liberar el lote porque el promedio cumple", "Eliminar el dato del informe", "Un resultado fuera de especificación debe registrarse y evaluarse antes de liberar."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre conforme y no conforme?", "Conforme cumple la especificación y no conforme no la cumple", "La especificación es el criterio para clasificar un resultado."),
        ("En la industria de alimentos: ¿cómo se calcula un promedio?", "Se suman los valores y se divide por la cantidad", "Es la suma total repartida en partes iguales."),
        ("¿Qué se hace si un dato registrado tiene un error?", "Se corrige con una nota que explique el motivo y se firma", "No se cambia el dato sin dejar rastro de la corrección."),
    ],
    op=("Informe de ejemplo del lote 60 del producto R. Especificaciones: humedad entre 9 % y 12 %; peso neto mínimo por envase de 250 g. Resultados: humedad 13 %; pesos de 4 envases: 251 g, 249 g, 255 g y 253 g. "
        "Escribe: (a) si la humedad es conforme, (b) cuántos envases pesan menos que el mínimo, (c) el peso promedio de los 4 envases y (d) qué harías con el lote y qué anotarías en el registro.",
        "(a) No es conforme: 13 % supera el máximo de 12 %. (b) Un envase, el de 249 g. (c) (251 + 249 + 255 + 253) ÷ 4 = 252 g. (d) Retener el lote, avisar al jefe de calidad y anotar los dos resultados fuera de especificación con su fecha, lote y firma.",
        ["clasifica la humedad como no conforme", "cuenta el envase bajo el mínimo y calcula el promedio", "propone retener y registrar"],
        ["hoja con las cuatro respuestas"],
        ["dar el lote por conforme por el promedio", "no registrar la humedad", "cambiar el peso de 249 a 250"],
        "Pregunta: «¿por qué no basta con que el promedio sea 252 g?». Debe decir que cada envase debe cumplir el mínimo."),
    reinforce="Inventa una especificación con un rango y tres resultados, y marca cuál es conforme y cuál no.",
    extend="Explica con un ejemplo inventado por qué un promedio puede ocultar un resultado fuera de especificación.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 11 (decisión sobre lotes, de ejemplo e inventada). Criterio de decisión de la planta: se libera el lote si todos los parámetros son conformes; se retiene si hay una no conformidad fisicoquímica, de peso o sensorial que puede reevaluarse; se rechaza si hay una no conformidad microbiológica o de inocuidad. "
     "Informe de tres lotes, cada uno de cajas de 12 envases. Lote 51 (40 cajas): humedad 11 %, pesos de la muestra todos sobre el mínimo, sensorial conforme, microbiológico conforme. "
     "Lote 52 (35 cajas): humedad 13 %, un envase de la muestra bajo el peso mínimo, sensorial conforme, microbiológico conforme. Lote 53 (30 cajas): humedad 12 %, pesos conformes, sensorial conforme, microbiológico fuera del estándar. La especificación de humedad es entre 10 % y 14 %.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un caso en papel: leer el informe de tres lotes y decidir si cada uno se libera, se retiene o se rechaza según un criterio.",
    prior=["Conozco parámetros, especificaciones y no conformidades.", "Sé multiplicar enteros.", "Sé leer una tabla breve."],
    explain=[
        "Con el informe de un lote, el jefe de calidad decide su destino. Liberar significa que el lote puede seguir su camino al almacén o al despacho. Retener significa mantenerlo apartado e identificado hasta evaluar una no conformidad que podría reevaluarse. Rechazar significa que el lote no puede usarse como estaba previsto, por ejemplo cuando hay una no conformidad microbiológica o de inocuidad.",
        "La gravedad no es igual para todos los parámetros. Una no conformidad microbiológica afecta la inocuidad, es decir, la seguridad para la salud, y no puede compensarse con buenos resultados en otros parámetros. Otras no conformidades, como el peso de un envase, pueden evaluarse. En todos los casos se registra la decisión, quién la tomó y por qué.",
        "Un lote retenido o rechazado se identifica y se aparta, y su destino lo decide el jefe de calidad con el procedimiento y la norma vigente. Ningún compañero puede decidir por su cuenta reprocesar o despachar ese lote." + LIM,
    ],
    vocab=[("liberar un lote", "permitir que el lote siga su camino porque cumple todo"), ("retener un lote", "mantenerlo apartado e identificado hasta evaluarlo"), ("rechazar un lote", "no usarlo como estaba previsto por una no conformidad grave"), ("inocuidad", "seguridad del alimento para la salud"), ("reevaluar", "volver a revisar con el procedimiento antes de decidir")],
    worked=[
        ("Aplicar el criterio", "Con el criterio de la ficha, un lote de ejemplo tiene todos los parámetros conformes. ¿Qué se decide?", ["El criterio libera el lote si todos los parámetros son conformes.", "No hay ninguna no conformidad."], "Se libera"),
        ("Distinguir gravedad", "Un lote de ejemplo tiene un envase bajo el peso mínimo y todo lo demás conforme. ¿Se rechaza?", ["Una no conformidad de peso puede reevaluarse.", "El rechazo se reserva a las microbiológicas o de inocuidad."], "No: se retiene para evaluar"),
    ],
    mistakes=[("Liberar un lote con un microbiológico fuera del estándar porque los otros resultados son conformes.", "La inocuidad no se compensa con otros parámetros.", "Aplica el criterio: una no conformidad microbiológica obliga a rechazar."),
              ("Despachar un lote retenido porque el cliente lo espera.", "Un lote retenido aún no está evaluado y puede tener un problema.", "Mantén el lote apartado hasta que el jefe de calidad decida.")],
    T=[
        ("abc", "{F} ¿Qué decisión corresponde para el lote 51?", "Liberarlo, porque todos los parámetros son conformes", "Retenerlo, porque la humedad es la más baja", "Retenerlo, porque ningún lote se libera sin una segunda revisión", "Todos sus parámetros cumplen, y la ficha libera el lote en ese caso."),
        ("abc", "{F} ¿Qué decisión corresponde para el lote 52?", "Retenerlo, porque un envase está bajo el peso mínimo y puede reevaluarse", "Liberarlo, porque el promedio cumple", "Rechazarlo, porque toda no conformidad obliga a rechazar", "Una no conformidad de peso se reevalúa y por eso el lote se retiene."),
        ("abc", "{F} ¿Qué decisión corresponde para el lote 53?", "Rechazarlo, por la no conformidad microbiológica", "Liberarlo, porque los demás parámetros son conformes", "Retenerlo hasta que baje la humedad", "La ficha rechaza el lote ante una no conformidad microbiológica."),
        ("=", "{F} ¿Cuántos envases tiene el lote 51 en total?", "40*12", "Se multiplican las cajas por los envases de cada caja.", " envases"),
        ("abc", "{F} ¿Qué no conformidad es más grave y por qué?", "La microbiológica del lote 53, porque afecta la inocuidad", "La de peso del lote 52, porque afecta el precio", "Ambas son igual de graves", "La inocuidad es la seguridad para la salud y el peso solo afecta el contenido."),
        ("=", "{F} ¿Cuántos envases quedan retenidos del lote 52?", "35*12", "Se multiplican las cajas por los envases de cada caja.", " envases"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué significa retener un lote?", "Mantenerlo apartado e identificado hasta evaluarlo", "Venderlo con descuento", "Eliminarlo de inmediato", "Retener es una pausa: el lote queda aparte mientras se decide su destino."),
        ("=", "{F} ¿Cuántos envases hay en total entre los tres lotes?", "(40+35+30)*12", "Se suman las cajas de los tres lotes y se multiplican por los envases de cada caja.", " envases"),
        ("=", "{F} ¿Cuántos envases no se liberan, entre el lote retenido y el rechazado?", "35*12+30*12", "Se suman los envases del lote 52 y del lote 53.", " envases"),
        ("abc", "{F} Un vendedor pide despachar el lote 52 porque «solo un envase pesa poco y el cliente espera». ¿Qué respuesta corresponde?", "No se despacha mientras esté retenido; el jefe de calidad evalúa la no conformidad", "Se despacha si se avisa al cliente por teléfono", "Se despacha quitando de la caja el envase liviano", "Un lote retenido solo se mueve cuando el jefe de calidad decide, aunque haya apuro."),
        ("abc", "{F} En el lote 53, el análisis sensorial fue conforme. ¿Por qué eso no basta para liberarlo?", "Porque los microbios no siempre se ven ni se huelen, y afectan la inocuidad", "Porque el análisis sensorial es obligatorio solo para productos nuevos", "Porque el análisis sensorial siempre debe repetirse", "El análisis microbiológico detecta lo que los sentidos no perciben."),
        ("=", "{F} Si, tras evaluarlo, el jefe de calidad libera el lote 52 descartando 6 envases con peso bajo el mínimo, ¿cuántos envases se liberan?", "35*12-6", "Al total de envases del lote se le restan los descartados.", " envases"),
        ("abc", "El lote 54 de ejemplo tiene todos sus parámetros conformes salvo la humedad, que es 15 %, con especificación entre 10 % y 14 %. ¿Qué decisión indica el criterio de la ficha?", "Retenerlo, porque es una no conformidad fisicoquímica que puede reevaluarse", "Liberarlo, porque 15 % está cerca del máximo", "Rechazarlo, porque toda no conformidad es grave", "El criterio retiene ante no conformidades fisicoquímicas y rechaza solo las microbiológicas o de inocuidad."),
    ],
    ctx=("abc", "{F} El jefe de producción propone reprocesar por su cuenta el lote 53 para no perder el producto. ¿Qué respuesta corresponde?", "El destino de un lote rechazado lo decide el jefe de calidad con el procedimiento y la norma vigente", "Corresponde reprocesarlo de inmediato para ahorrar costos", "Basta con que lo autorice cualquier operario", "Un lote rechazado por inocuidad no se reprocesa sin decisión formal."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre retener y rechazar un lote?", "Retener es apartarlo para evaluar; rechazar es no usarlo por una no conformidad grave", "La gravedad de la no conformidad distingue ambas decisiones."),
        ("¿Qué no conformidad obliga a rechazar según la ficha?", "La microbiológica o de inocuidad", "Afecta la seguridad para la salud y no se compensa."),
        ("¿Qué se registra junto a la decisión sobre un lote?", "Quién la tomó y por qué", "Así la decisión puede revisarse después."),
    ],
    op=("Criterio de la ficha de esta clase. Informe de ejemplo: lote 70 (20 cajas de 12 envases): todo conforme. Lote 71 (25 cajas de 12 envases): sensorial no conforme por olor extraño, el resto conforme. Lote 72 (15 cajas de 12 envases): microbiológico fuera del estándar. "
        "Escribe: (a) la decisión para cada lote con su razón, (b) cuántos envases se liberan y (c) por qué el jefe de producción no debe despachar el lote 71 por su cuenta.",
        "(a) Lote 70: se libera, todo es conforme. Lote 71: se retiene, la no conformidad sensorial puede reevaluarse. Lote 72: se rechaza, por la no conformidad microbiológica. (b) Se liberan 20 × 12 = 240 envases. (c) Porque el lote retenido debe ser evaluado y el destino lo decide el jefe de calidad.",
        ["decide bien los tres lotes", "calcula 240 envases liberados", "explica por qué no se despacha un lote retenido"],
        ["hoja con las tres respuestas"],
        ["rechazar el lote sensorial", "liberar el lote microbiológico", "contar los envases del lote retenido"],
        "Pregunta: «¿qué pasaría si se despacha el lote 71 sin evaluar?». Debe decir que podría llegar un problema al consumidor."),
    reinforce="Inventa tres lotes con resultados y aplica el criterio de la ficha para decidir si se liberan, se retienen o se rechazan.",
    extend="Explica con un ejemplo inventado por qué una no conformidad microbiológica no se compensa con buenos resultados en otros parámetros.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 12 (registro de humedad de ejemplo, inventado). Mediciones consecutivas de humedad (en %) de un producto, en orden, a lo largo de un turno: 11, 12, 11, 13, 13, 14, 15, 15. Especificación: humedad entre 10 % y 14 %. "
     "Regla de la planta: en la primera medición fuera de la especificación, quien mide avisa al jefe de calidad y espera su indicación. Un gráfico de control en papel anota las mediciones en orden para ver tendencias.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio con datos de ejemplo: calcular promedio y porcentaje fuera de especificación, leer una tendencia en un registro de mediciones y decidir cuándo avisar.",
    prior=["Conozco parámetros y especificaciones.", "Sé calcular promedios y porcentajes con enteros.", "Sé leer una lista ordenada de datos."],
    explain=[
        "Un registro de mediciones en el tiempo permite calcular el promedio (suma dividida por la cantidad), el rango (diferencia entre la mayor y la menor medición) y el porcentaje de mediciones fuera de especificación (cantidad fuera por 100, dividida por el total). Estos valores resumen, pero no reemplazan mirar cada medición.",
        "Un gráfico de control en papel marca las mediciones en el orden en que se hicieron, con las líneas de los límites de la especificación. Permite ver una tendencia, por ejemplo una humedad que sube turno tras turno, antes de que una medición salga del límite. Una tendencia se avisa aunque todas las mediciones sigan dentro del rango.",
        "La regla de aviso se cumple desde la primera medición fuera de especificación: se informa al jefe de calidad y se espera su indicación. El operario no ajusta equipos por su cuenta ni cambia un número para mantener el registro dentro del rango." + LIM,
    ],
    vocab=[("promedio", "suma de los valores dividida por la cantidad de valores"), ("rango", "diferencia entre la medición mayor y la menor"), ("tendencia", "dirección en que cambian las mediciones con el tiempo"), ("gráfico de control", "dibujo en papel de las mediciones en orden con sus límites"), ("fuera de especificación", "medición que no cumple el rango exigido")],
    worked=[
        ("Calcular un promedio", "Cuatro mediciones de ejemplo de humedad dieron 10, 12, 12 y 14. ¿Cuál es el promedio?", ["Se suman: 10 + 12 + 12 + 14 = 48.", "48 ÷ 4 = 12."], "12 %"),
        ("Calcular un rango", "Las mediciones de ejemplo fueron 9, 11 y 13. ¿Cuál es el rango?", ["Se identifica la mayor (13) y la menor (9).", "13 − 9 = 4."], "4 puntos de humedad"),
    ],
    mistakes=[("Decir que no hay problema porque el promedio está dentro del rango.", "El promedio oculta mediciones individuales fuera de especificación.", "Compara cada medición con la especificación, además del promedio."),
              ("Anotar 14 en lugar de 15 para dejar el registro dentro del rango.", "Se oculta un dato real y se pierde la señal de alerta.", "Anota el dato medido y avisa según la regla.")],
    T=[
        ("abc", "{F} La séptima medición es 15 %. ¿Cumple la especificación?", "No, porque supera el máximo de 14 %", "Sí, porque está cerca del rango", "Sí, porque la anterior estaba en el límite", "El máximo permitido es 14 % y 15 % lo supera."),
        ("=", "{F} ¿Cuál es la suma de las 8 mediciones?", "11+12+11+13+13+14+15+15", "Se suman todas las mediciones en orden.", " %"),
        ("=", "{F} ¿Cuál es el promedio de las 8 mediciones?", "(11+12+11+13+13+14+15+15)//8", "El promedio es la suma dividida por la cantidad de mediciones.", " %"),
        ("abc", "{F} Según la regla de la planta, ¿en qué medición debió avisarse al jefe de calidad?", "En la 7.ª, la primera con 15 %", "En la 6.ª, la primera con 14 %", "En la 8.ª, la última del turno", "La regla manda avisar en la primera medición fuera de especificación, que es la séptima."),
        ("abc", "{F} ¿Cuántas mediciones están fuera de la especificación?", "Dos", "Una", "Cuatro", "Solo las dos mediciones de 15 % superan el máximo de 14 %."),
        ("=", "{F} ¿Qué porcentaje de las 8 mediciones está fuera de la especificación?", "2*100//8", "Se divide la cantidad fuera de especificación por el total y se multiplica por 100.", " %"),
        ("abc", "En Elaboración Industrial de Alimentos: ¿para qué sirve un gráfico de control en papel?", "Para ver las mediciones en orden y detectar una tendencia antes de salirse del límite", "Para calcular el precio de venta del lote", "Para reemplazar la especificación", "Al anotar los datos en orden se ve si suben o bajan con el tiempo."),
        ("abc", "{F} ¿Qué tendencia muestran las mediciones de la ficha?", "Suben desde 11 % hasta 15 % a lo largo del turno", "Bajan desde 15 % hasta 11 %", "Se mantienen constantes en 13 %", "Las últimas mediciones son mayores que las primeras."),
        ("=", "{F} ¿Cuál es el rango de las mediciones, es decir, la diferencia entre la mayor y la menor?", "15-11", "El rango resta la medición menor a la mayor.", " puntos"),
        ("abc", "{F} Alguien dice que no hay problema porque el promedio está dentro del rango. ¿Qué respuesta es correcta?", "El promedio oculta mediciones fuera de rango; cada medición se compara con la especificación", "Tiene razón, el promedio es lo único que importa", "El promedio solo se usa cuando las mediciones son altas", "Un promedio dentro del rango puede coexistir con valores individuales fuera de especificación."),
        ("abc", "{F} Tras la séptima medición, ¿qué acción es adecuada?", "Avisar al jefe de calidad y seguir su indicación, sin ajustar el equipo por cuenta propia", "Ajustar el equipo para bajar la humedad", "Anotar 14 para mantener el registro dentro del rango", "La regla manda avisar; alterar el dato o intervenir sin autorización agrava el problema."),
        ("=", "Dos turnos de ejemplo: en el primero 5 de 40 envases quedaron fuera de peso y en el segundo 3 de 60. ¿Qué porcentaje de los 100 envases quedó fuera de peso?", "(5+3)*100//(40+60)", "Se suman los envases fuera de peso y se divide por el total de envases.", " %"),
        ("abc", "La línea 1 tuvo 5 envases no conformes de 50 (10 %) y la línea 2 tuvo 8 de 100 (8 %). ¿Qué línea tuvo menor porcentaje de no conformes?", "La línea 2, con 8 %", "La línea 1, porque tuvo menos envases no conformes", "Ambas tuvieron el mismo porcentaje", "El porcentaje relaciona los no conformes con el total, y 8 % es menor que 10 %."),
    ],
    ctx=("abc", "{F} Antes de enviar el informe a un cliente, un supervisor quiere borrar las dos mediciones de 15 % y dejar solo las conformes. ¿Qué corresponde?", "Informar todas las mediciones, incluidas las no conformes, con la acción tomada", "Borrarlas para no preocupar al cliente", "Cambiarlas por 14 para mantener el registro limpio", "Ocultar datos reales es una falta; el informe debe reflejar lo medido y lo que se hizo."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es el rango de un grupo de mediciones?", "La diferencia entre la mayor y la menor", "Muestra qué tan separadas están las mediciones."),
        ("¿Cuándo se avisa al jefe de calidad según la regla de la ficha?", "En la primera medición fuera de especificación", "Avisar desde la primera medición fuera de rango limita el problema."),
        ("¿Qué muestra un gráfico de control?", "Las mediciones en orden y su tendencia", "Permite ver el cambio con el tiempo."),
    ],
    op=("Registro de ejemplo de peso neto de envases en un turno, en gramos y en orden: 505, 503, 501, 500, 499, 498. Especificación: mínimo de 500 g por envase. Regla de aviso: en la primera medición bajo el mínimo se avisa al jefe de calidad. "
        "Escribe: (a) el promedio de las 6 mediciones, (b) cuántas mediciones incumplen la especificación, (c) en qué medición debió avisarse y (d) qué tendencia se observa y por qué conviene mirarla aunque las primeras mediciones cumplían.",
        "(a) La suma es 3.006 g y el promedio es 501 g. (b) Dos: 499 g y 498 g. (c) En la quinta medición, 499 g. (d) Los pesos bajan en el turno; la tendencia permite avisar antes de que se salgan del mínimo.",
        ["calcula el promedio con suma y división", "cuenta las dos mediciones bajo el mínimo y ubica la quinta", "describe la tendencia a la baja"],
        ["hoja con las cuatro respuestas"],
        ["decir que no hay problema por el promedio", "avisar en la sexta medición", "cambiar un dato"],
        "Pregunta: «¿qué habría pasado de ver la tendencia antes?». Debe decir que se habría avisado antes de salirse del mínimo."),
    reinforce="Inventa seis mediciones de una variable de una planta y calcula su promedio y su rango.",
    extend="Explica con un ejemplo inventado cómo una tendencia puede avisar de un problema antes de que haya una no conformidad.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 13 (comparación de proveedores de ejemplo, inventada). Por cada 100 kg comprados de una materia prima: proveedor A, precio de $900 por kg y 90 kg utilizables (conformes en recepción); proveedor B, precio de $720 por kg y 80 kg utilizables. "
     "Matriz de decisión (puntaje de 1 a 5 y peso de cada criterio, definidos antes de evaluar). Pesos: calidad 3, costo por kg utilizable 2, plazo de entrega 1. Puntajes de A: calidad 5, costo 2, plazo 4. Puntajes de B: calidad 3, costo 4, plazo 2. "
     "Exigencia mínima del jefe de calidad: al menos 85 kg utilizables de cada 100 kg.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas con criterios definidos, calcular un costo por kg utilizable, usar una matriz ponderada y verificar después si la decisión funcionó.",
    prior=["Sé multiplicar y dividir enteros.", "Conozco conformidad y no conformidad.", "Sé leer una tabla breve."],
    explain=[
        "Para comparar dos proveedores no basta mirar el precio por kg. El costo por kg utilizable divide lo que se paga por lo que realmente se puede usar: si de 100 kg solo 80 son conformes, se pagó por 100 pero se usan 80. Por eso el producto no conforme encarece la compra. Los datos de este cuaderno son de ejemplo.",
        "Una matriz de decisión ordena los criterios con un peso cada uno y un puntaje por alternativa. El puntaje ponderado se calcula multiplicando cada puntaje por su peso y sumando. Los pesos se fijan antes de evaluar, para que la decisión sea objetiva y no se acomode a un resultado deseado. Además puede haber una exigencia mínima: quien no la cumple queda fuera aunque tenga buen puntaje.",
        "Decidir no termina el trabajo: se verifica comparando, en las siguientes recepciones, el porcentaje de conformes y los reclamos con lo esperado. Si no se cumple, se revisa la decisión." + LIM,
    ],
    vocab=[("costo por kg utilizable", "lo pagado dividido por los kilos que se pueden usar"), ("matriz de decisión", "tabla que compara alternativas con criterios y pesos"), ("puntaje ponderado", "suma de cada puntaje multiplicado por el peso de su criterio"), ("exigencia mínima", "condición que una alternativa debe cumplir para ser considerada"), ("verificación", "comprobación posterior de que la decisión funcionó")],
    worked=[
        ("Costo por kg utilizable", "Un proveedor de ejemplo vende 100 kg a $500 por kg y 80 kg son utilizables. ¿Cuál es el costo por kg utilizable?", ["El gasto total es 100 × 500 = 50.000.", "50.000 ÷ 80 = 625."], "$625 por kg utilizable"),
        ("Puntaje ponderado", "Una alternativa de ejemplo tiene puntajes 4 en calidad (peso 2) y 3 en costo (peso 1). ¿Cuál es su puntaje ponderado?", ["Se multiplica cada puntaje por su peso: 4 × 2 y 3 × 1.", "8 + 3 = 11."], "11 puntos"),
    ],
    mistakes=[("Elegir al proveedor con menor precio por kg sin mirar cuánto se puede usar.", "El producto no conforme se paga y no sirve, así que el costo real es mayor.", "Compara el costo por kg utilizable."),
              ("Cambiar los pesos de la matriz después de ver los resultados.", "La decisión deja de ser objetiva y se acomoda a lo que se quiere.", "Fija los criterios y los pesos antes de evaluar.")],
    T=[
        ("=", "{F} ¿Cuántos pesos se pagan por 100 kg del proveedor A?", "100*900", "Se multiplica la cantidad de kg por el precio por kg.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por kg utilizable del proveedor A?", "100*900//90", "Se divide lo pagado por los kg utilizables.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por kg utilizable del proveedor B?", "100*720//80", "Se divide lo pagado por los kg utilizables.", " pesos"),
        ("abc", "{F} ¿Qué proveedor tiene menor costo por kg utilizable?", "El proveedor B, con $900", "El proveedor A, con $1.000", "Ninguno, porque son iguales", "B cuesta $900 por kg utilizable, que es menos que los $1.000 de A."),
        ("abc", "{F} ¿Qué proveedor tiene mayor proporción de producto utilizable?", "El proveedor A, con 90 kg de cada 100", "El proveedor B, con 80 kg de cada 100", "Los dos tienen la misma proporción", "Los 90 kg utilizables de A superan los 80 kg de B."),
        ("=", "{F} ¿Cuál es el puntaje ponderado del proveedor A?", "5*3+2*2+4*1", "Se multiplica cada puntaje por su peso y se suman.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje ponderado del proveedor B?", "3*3+4*2+2*1", "Se multiplica cada puntaje por su peso y se suman.", " puntos"),
        ("abc", "{F} Con la matriz ponderada, ¿qué proveedor tiene el mayor puntaje?", "El proveedor A", "El proveedor B", "Ambos empatan", "A suma 23 puntos y B suma 19, por lo que A gana."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿por qué conviene comparar el costo por kg utilizable y no solo el precio por kg?", "Porque el producto no conforme se paga igual y no se puede usar", "Porque el precio por kg no tiene importancia", "Porque el costo por kg utilizable siempre es menor", "El costo real incluye lo que se paga por producto no utilizable."),
        ("abc", "Un jefe cambia los pesos de la matriz después de ver los puntajes, para que gane su proveedor favorito. ¿Qué problema hay?", "Los pesos deben definirse antes de evaluar, para que la decisión sea objetiva", "Ninguno, los pesos se pueden ajustar cuando se quiera", "Los pesos no influyen en el resultado final", "Cambiar los pesos después acomoda la decisión al resultado deseado."),
        ("abc", "Ya elegido un proveedor, ¿cómo se verifica que la decisión fue buena?", "Comparando en las siguientes recepciones el porcentaje de conformes y los reclamos con lo esperado", "Esperando que no lleguen reclamos, sin registrar nada", "Preguntándole al proveedor si cumplió", "La verificación usa datos registrados en el tiempo y no impresiones."),
        ("=", "{F} Si el peso del costo por kg utilizable sube a 3 (calidad 3 y plazo 1 se mantienen), ¿cuántos puntos suma el proveedor A?", "5*3+2*3+4*1", "Se recalcula el puntaje ponderado con el nuevo peso del costo.", " puntos"),
        ("abc", "{F} ¿Qué proveedor cumple la exigencia mínima del jefe de calidad?", "Solo el proveedor A, con 90 kg utilizables", "Solo el proveedor B, por su menor costo", "Ambos proveedores", "La exigencia pide al menos 85 kg, y solo A la cumple."),
    ],
    ctx=("abc", "{F} El administrador quiere comprar al proveedor B porque su precio por kg es menor. ¿Qué respuesta es completa?", "Mostrar el costo por kg utilizable y los resultados de calidad, y decidir con la matriz y la exigencia mínima", "Comprar a B por precio, sin más análisis", "Comprar a A sin mostrar datos", "La decisión se apoya en datos comparables y en criterios fijados antes."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calcula el costo por kg utilizable?", "Dividiendo lo pagado por los kg utilizables", "Así se incluye el efecto de lo que no se puede usar."),
        ("¿Cuándo se definen los pesos de una matriz de decisión?", "Antes de evaluar las alternativas", "Así la decisión no se acomoda a un resultado deseado."),
        ("¿Qué es una exigencia mínima?", "Una condición que la alternativa debe cumplir para ser considerada", "Deja fuera lo que no la cumple aunque tenga buen puntaje."),
    ],
    op=("Datos de ejemplo. Por cada 100 kg comprados: proveedor C, $600 por kg y 75 kg utilizables; proveedor D, $630 por kg y 90 kg utilizables. Pesos de la matriz: calidad 3, costo 2, plazo 1. Puntajes de C: calidad 2, costo 3, plazo 4. Puntajes de D: calidad 5, costo 4, plazo 3. Exigencia mínima: 80 kg utilizables de cada 100. "
        "Escribe: (a) el costo por kg utilizable de cada proveedor, (b) el puntaje ponderado de cada uno, (c) cuál cumple la exigencia mínima, (d) qué proveedor eliges y (e) cómo verificarías después que la decisión fue buena.",
        "(a) C: 60.000 ÷ 75 = 800 pesos; D: 63.000 ÷ 90 = 700 pesos. (b) C: 6 + 6 + 4 = 16; D: 15 + 8 + 3 = 26. (c) Solo D cumple. (d) D, por puntaje, por menor costo por kg utilizable y por cumplir la exigencia mínima. (e) Comparar en las siguientes recepciones el porcentaje de conformes y los reclamos con lo esperado.",
        ["calcula los costos por kg utilizable", "calcula los puntajes ponderados", "elige con la exigencia mínima y propone una verificación"],
        ["hoja con las cinco respuestas"],
        ["elegir por el menor precio por kg", "ignorar la exigencia mínima", "cambiar los pesos después"],
        "Pregunta: «¿por qué C queda fuera aunque su precio sea menor?». Debe decir que no cumple la exigencia mínima de 80 kg."),
    reinforce="Inventa dos proveedores con precio y kg utilizables y calcula el costo por kg utilizable de cada uno.",
    extend="Explica con un ejemplo inventado por qué el proveedor más barato por kg puede no ser el más conveniente.",
)
