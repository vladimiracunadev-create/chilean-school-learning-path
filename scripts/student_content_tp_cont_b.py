"""Contabilidad TP 3.º y 4.º medio: OAE-03 (llenado, tramitación y registro de documentación) y OAE-04 (hechos económicos de comercio nacional e internacional). Documentos, empresas e importes inventados."""
from __future__ import annotations

from tp_cont_common import build

O3 = "TP-CONT-3y4-OAE-03"
O4 = "TP-CONT-3y4-OAE-04"

# ============================================================ OAE-03, clase 1
F = ("Ficha 10 (oficina de ejemplo, inventada). «Papelería Los Aromos SpA» maneja estos documentos: factura de compra, boleta de venta, comprobante de egreso (constancia interna de un pago), "
     "comprobante de ingreso (constancia interna de un cobro) y recibo. Riesgos frecuentes: documento ilegible, con enmiendas o datos incompletos, extraviado, o con datos personales de clientes a la vista. "
     "Se tramita así: revisar, aprobar, pagar y archivar.")
build(
    O3, 1, F,
    use="Aprenderé por qué se documentan los hechos, qué riesgos tiene el llenado y la tramitación y cómo cuidar los datos personales.",
    prior=["Sé qué es una factura y una boleta.", "Sé que cada hecho económico necesita respaldo.", "Sé qué es el RUT."],
    explain=[
        "Documentar es dejar una prueba escrita y revisable de un hecho económico. Hay documentos tributarios (como la factura y la boleta), que se emiten según la norma vigente y ante el Servicio de Impuestos Internos, y documentos internos (como el comprobante de ingreso o de egreso), que la empresa usa para dejar constancia de cobros y pagos.",
        "Realizar el llenado de un documento es completarlo con todos sus datos, de forma legible y sin enmiendas. Tramitarlo es hacerlo pasar por sus etapas: revisar, aprobar, pagar y archivar, en ese orden. Registrarlo es anotarlo en los libros y guardarlo con su respaldo; los plazos de conservación son los que fija la norma vigente.",
        "Los documentos suelen incluir datos personales, como el RUT (número que identifica a una persona o empresa ante el Servicio de Impuestos Internos) o la dirección. Esos datos se usan solo para el fin del documento, se guardan con acceso restringido y no se muestran a quien no los necesita. Un documento enmendado, incompleto o extraviado pierde valor como prueba.",
    ],
    vocab=[("documentar", "dejar una prueba escrita y revisable de un hecho"), ("tramitar", "hacer pasar un documento por sus etapas"), ("comprobante de egreso", "constancia interna de un pago"), ("comprobante de ingreso", "constancia interna de un cobro"), ("RUT", "número que identifica a una persona o empresa ante el Servicio de Impuestos Internos"), ("enmienda", "cambio hecho sobre un dato ya escrito"), ("dato personal", "información que identifica a una persona")],
    worked=[
        ("Detectar un documento incompleto", "A una empresa de ejemplo llega un comprobante de ingreso sin fecha y sin firma. ¿Puede tramitarse?", ["Le faltan datos que lo hacen revisable.", "Se devuelve a quien lo preparó para completarlo antes de tramitarlo."], "No; se completa antes de tramitar"),
        ("Ordenar la tramitación", "Ordena: archivar, pagar, revisar, aprobar.", ["Primero se revisa que el documento esté correcto.", "Luego se aprueba, se paga y por último se archiva."], "Revisar, aprobar, pagar, archivar"),
    ],
    mistakes=[("Corregir un monto con corrector sin avisar.", "No se sabe quién cambió el dato ni por qué, y el documento pierde valor como prueba.", "Pide al emisor un documento corregido y deja constancia."),
              ("Dejar a la vista una lista con RUT y direcciones de clientes.", "Se exponen datos personales a quien no los necesita.", "Guarda esos documentos con acceso restringido y usa los datos solo para su fin.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es documentar un hecho económico?", "Dejar una prueba escrita y revisable del hecho", "Contárselo de palabra a la jefatura", "Anotarlo en un papel sin fecha ni firma", "Documentar exige una prueba escrita que otra persona pueda revisar."),
        ("abc", "¿Cuál de estos es un documento interno de la empresa, no tributario?", "El comprobante de egreso", "La factura", "La boleta", "El comprobante de egreso es una constancia interna de un pago; factura y boleta son tributarios."),
        ("ab", "¿Qué significa llenar bien un documento?", "Completar todos los campos de forma legible y sin enmiendas", "Dejar en blanco los datos que no se recuerdan", "Un documento bien llenado puede ser revisado por otra persona sin dudas."),
        ("abc", "{F} Una factura recibida tiene el monto tapado con corrector. ¿Qué riesgo de la ficha presenta?", "Una enmienda", "Un extravío", "Un dato personal expuesto", "El corrector cambia un dato ya escrito: eso es una enmienda."),
        ("abc", "{F} ¿Qué orden de tramitación indica la ficha?", "Revisar, aprobar, pagar y archivar", "Pagar, revisar, aprobar y archivar", "Archivar, pagar, revisar y aprobar", "La revisión va primero y el pago solo después de aprobar."),
        ("abc", "En Contabilidad: ¿qué es el RUT?", "El número que identifica a una persona o empresa ante el Servicio de Impuestos Internos", "El valor total de una factura", "El número correlativo de una boleta", "El RUT identifica a una persona o empresa; no es un monto ni un correlativo."),
        ("=", "{F} Cada semana se archivan 45 documentos de la papelería. ¿Cuántos se archivan en 4 semanas?", "45*4", "Se multiplican los documentos semanales por las semanas.", " documentos"),
        ("abc", "Se imprime una lista de clientes con RUT y dirección y se deja sobre el mostrador. ¿Qué principio se rompe?", "La protección de datos personales", "La oportunidad de la información", "El respaldo documental", "Los datos personales deben resguardarse y mostrarse solo a quien los necesita."),
        ("abc", "{F} Se pierde la factura original de una compra ya registrada. ¿Qué corresponde?", "Avisar a la jefatura, pedir una copia al proveedor y dejar constancia", "Hacer otra factura igual con los mismos datos", "No hacer nada porque la compra ya está registrada", "El respaldo debe conseguirse con el emisor; inventar un documento es falsificar."),
        ("abc", "¿Por qué un documento enmendado con corrector es riesgoso?", "Porque no se sabe quién cambió el dato ni por qué y pierde valor como prueba", "Porque el monto enmendado siempre queda mal calculado", "Porque solo el contador puede usar corrector en los documentos", "La enmienda sin respaldo quita confianza en el dato."),
        ("abc", "Un asistente llena una factura de ejemplo y deja en blanco el RUT del cliente «para completarlo después». ¿Qué corresponde?", "No entregarla hasta completar el dato y consultar a la jefatura si falta información", "Entregarla y completar el dato otro día", "Escribir un RUT cualquiera para no dejar el espacio vacío", "Un documento incompleto no se entrega; inventar un dato es falsear el documento."),
        ("=", "En un mes de ejemplo se emitieron 120 documentos y 9 tenían errores de llenado. ¿Cuántos estaban bien llenados?", "120-9", "Se restan los documentos con error del total emitido.", " documentos"),
        ("abc", "{F} ¿Quién puede acceder a los documentos que contienen datos personales de clientes?", "Solo quienes los necesitan para su función", "Todo el personal, para que estén disponibles", "Cualquier persona que visite la oficina", "El acceso se limita a quien necesita el dato para su trabajo."),
    ],
    ctx=("abc", "Una compañera te pide una copia del comprobante de egreso de un proveedor persona natural, con su RUT y cuenta bancaria, «para mandárselo a una amiga». ¿Qué respondes?", "Que no puedo entregarlo sin autorización de la jefatura y que esos datos solo se usan para el pago", "Que sí, porque son datos de la empresa", "Que se lo mande ella por su cuenta sin avisar", "Los datos personales no se comparten con fines ajenos al documento."),
    sc=[
        ("En Contabilidad: ¿qué orden sigue la tramitación de un pago?", "Revisar, aprobar, pagar y archivar", "La aprobación debe ir antes del pago, nunca después."),
        ("¿Qué haces si falta un dato en un documento?", "Lo devuelvo para completarlo antes de tramitar", "Un documento incompleto no sirve de respaldo."),
        ("¿Cómo se resguardan los datos personales de un documento?", "Con acceso restringido y usándolos solo para su fin", "Así se evita exponerlos a quien no los necesita."),
    ],
    op=("Revisa esta bandeja de ejemplo de una oficina: un comprobante de ingreso sin fecha; una factura con el monto enmendado con corrector; una lista de clientes con RUT dejada sobre el mostrador. Escribe, para cada caso, el riesgo y qué harías, y cierra con el orden de tramitación de un pago.",
        "Comprobante sin fecha: riesgo de dato incompleto; lo devuelvo a quien lo preparó. Factura enmendada: riesgo de enmienda; pido un documento corregido al emisor y aviso al contador. Lista con RUT: riesgo de exponer datos personales; la guardo con acceso restringido. Tramitación: revisar, aprobar, pagar y archivar.",
        ["identifica el riesgo de cada caso", "propone una acción responsable", "nombra el orden de tramitación"],
        ["hoja con tres casos, tres acciones y el orden"],
        ["corregir el documento por cuenta propia", "dejar a la vista datos personales", "pagar antes de aprobar"],
        "Pregunta: «¿por qué no corriges tú el monto?». Si no menciona la enmienda y el respaldo, repasa el valor de prueba."),
    reinforce="Anota en tu cuaderno tres datos personales que puede tener un documento de una empresa (inventados) y cómo los resguardarías.",
    extend="Explica con un ejemplo inventado por qué una empresa debe conservar sus documentos ordenados.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 11 (documento de ejemplo, inventado). Factura de ejemplo N.º 0001: Emisor «Distribuidora Costa Sur Ltda.» (RUT de ejemplo 00.000.000-0); "
     "receptor «Papelería Los Aromos SpA»; fecha 10 de marzo; detalle: 20 resmas de papel a $4.000 cada una; neto $80.000; IVA (tasa de ejemplo 10 %) $8.000; total $88.000.")
build(
    O3, 2, F,
    use="Aprenderé a reconocer los documentos de la operación de compra y venta y los campos de una factura.",
    prior=["Sé qué es una factura, una boleta y una guía de despacho.", "Sé calcular el IVA con una tasa de ejemplo.", "Sé multiplicar cantidad por precio."],
    explain=[
        "Una compra o una venta pasa por varios documentos. La cotización es la lista de precios que ofrece un proveedor antes de vender. La orden de compra es el pedido que hace el comprador. La guía de despacho respalda el traslado de la mercadería y la factura respalda la venta y su cobro. La nota de crédito corrige o anula parte de una factura, por ejemplo por una devolución.",
        "Una factura tiene campos: emisor (quien vende), receptor (quien compra), fecha, detalle con cantidad, descripción y precio unitario, neto, IVA y total. La cantidad por el precio unitario da el subtotal de cada línea; la suma de las líneas es el neto; el IVA se calcula sobre el neto y el total es neto más IVA. Los requisitos exactos los fija la norma vigente.",
        "Antes de pagar, se comparan tres documentos: orden de compra (lo pedido), guía de despacho (lo recibido) y factura (lo cobrado). Si no coinciden, se avisa al contador y se pide al emisor la corrección formal; nadie cambia a mano los datos de un documento.",
    ],
    vocab=[("cotización", "oferta de precios antes de la compra"), ("orden de compra", "pedido que hace el comprador al proveedor"), ("emisor", "quien emite el documento y vende"), ("receptor", "quien recibe el documento y compra"), ("subtotal", "cantidad por precio unitario de una línea"), ("detalle", "líneas con lo comprado o vendido")],
    worked=[
        ("Subtotal de una línea", "Una factura de ejemplo detalla 15 cajas de lápices a $3.000 cada una. ¿Cuál es el subtotal de esa línea?", ["Se multiplica cantidad por precio unitario.", "15 × 3.000 = 45.000."], "$45.000"),
        ("Reconocer al emisor", "En una factura de ejemplo, «Librería Aurora Ltda.» vende a «Colegio Los Pinos». ¿Quién es el emisor?", ["El emisor es quien vende y emite el documento.", "«Librería Aurora Ltda.» vende."], "Librería Aurora Ltda."),
    ],
    mistakes=[("Pagar una factura sin comparar con la orden de compra y la guía.", "Se puede pagar lo que no se pidió o no se recibió.", "Compara las tres: lo pedido, lo recibido y lo cobrado."),
              ("Cambiar a mano el total de una factura recibida.", "Solo el emisor puede corregirla formalmente.", "Pide la corrección al emisor y avisa al contador.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es una orden de compra?", "El pedido que hace el comprador al proveedor", "El documento que cobra el impuesto", "El documento que respalda el traslado de mercaderías", "La orden de compra es el pedido previo a la entrega y al cobro."),
        ("abc", "¿Qué es una cotización?", "Una lista de precios que ofrece el proveedor antes de la compra", "Un documento que prueba que ya se pagó", "Un documento que anula una factura", "La cotización es una oferta anterior a la compra."),
        ("ab", "¿Para qué sirve un comprobante de egreso?", "Para dejar constancia interna de un pago hecho por la empresa", "Para cobrarle una venta a un cliente", "El comprobante de egreso es la constancia interna de un pago."),
        ("abc", "{F} ¿Quién es el emisor de la factura?", "Distribuidora Costa Sur Ltda.", "Papelería Los Aromos SpA", "El Servicio de Impuestos Internos", "El emisor es quien vende; aquí la distribuidora."),
        ("abc", "{F} ¿Qué campo de la factura indica cuántas unidades se compraron?", "La cantidad del detalle", "El neto", "La fecha", "La cantidad está en el detalle; el neto es un monto."),
        ("=", "{F} Comprueba el neto: ¿cuántos pesos da 20 resmas por $4.000 cada una?", "20*4000", "El subtotal es cantidad por precio unitario.", " pesos"),
        ("=", "{F} Comprueba el IVA de ejemplo: ¿cuántos pesos es el 10 % de $80.000?", "80000*10//100", "El IVA se calcula sobre el neto.", " pesos"),
        ("abc", "{F} La papelería devuelve 5 resmas. ¿Qué documento emite el proveedor para corregir la factura?", "Una nota de crédito", "Una orden de compra", "Una cotización", "La nota de crédito corrige o anula parte de una factura."),
        ("=", "{F} ¿Cuántos pesos netos tiene la devolución de 5 resmas al precio de la factura?", "5*4000", "Se multiplican las resmas devueltas por su precio unitario.", " pesos"),
        ("abc", "{F} La papelería encuentra que el total de la factura dice $80.000 en vez de $88.000. ¿Qué corresponde?", "Avisar al contador y pedir al emisor la corrección formal", "Corregir el total a mano", "Registrar $80.000 y no avisar", "Un documento recibido no se corrige a mano; se pide la corrección al emisor."),
        ("abc", "¿Qué diferencia hay entre una orden de compra y una factura?", "La orden es el pedido previo; la factura respalda la venta y su cobro", "Son el mismo documento con otro nombre", "La orden incluye el IVA y la factura no", "La orden es el pedido; la factura es el cobro de lo vendido."),
        ("=", "Una orden de compra pide 30 resmas y el proveedor entrega 25. ¿Cuántas resmas faltan por entregar?", "30-25", "Se restan las unidades recibidas a las pedidas.", " resmas"),
        ("abc", "¿Qué documentos conviene tener juntos antes de pagar una compra?", "La orden de compra, la guía de despacho y la factura", "Solo la factura", "La factura y la cotización de otro proveedor", "Comparar lo pedido, lo recibido y lo cobrado evita pagar de más."),
    ],
    ctx=("abc", "Llega una factura por 40 resmas, pero la guía de despacho firmada por bodega dice 35. ¿Qué haces antes de pagar?", "Aviso al contador de la diferencia y pido al proveedor aclarar o corregir el documento", "Pago las 40 porque la factura manda", "Pago las 35 por mi cuenta y no digo nada", "Cuando lo recibido no coincide con lo cobrado se avisa y se pide corrección formal."),
    sc=[
        ("En Contabilidad: ¿quién es el emisor de una factura?", "Quien vende y emite el documento", "El receptor es quien compra y recibe el documento."),
        ("¿Cómo se calcula el subtotal de una línea?", "Cantidad por precio unitario", "Así se obtiene el valor de cada línea del detalle."),
        ("¿Qué tres documentos se comparan antes de pagar?", "La orden de compra, la guía de despacho y la factura", "Lo pedido, lo recibido y lo cobrado deben coincidir."),
    ],
    op=("Una factura de ejemplo detalla: 12 cajas de lápices a $3.000 cada una y 8 resmas de papel a $4.000 cada una. Calcula el subtotal de cada línea, el neto, el IVA con la tasa de ejemplo de 10 % y el total, y nombra qué dos documentos compararías con ella antes de pagar.",
        "Lápices: 12 × 3.000 = 36.000. Resmas: 8 × 4.000 = 32.000. Neto: 68.000. IVA: 6.800. Total: 74.800. Comparo con la orden de compra y con la guía de despacho.",
        ["calcula los subtotales y el neto", "calcula el IVA de ejemplo y el total", "nombra los documentos de comparación"],
        ["hoja con la tabla de la factura y los cálculos"],
        ["calcular el IVA sobre un subtotal", "olvidar sumar el IVA al total", "no comparar con otros documentos"],
        "Pregunta: «¿qué haces si la guía dice menos resmas?». Si no avisa al contador, repasa el procedimiento ante diferencias."),
    reinforce="Escribe en tu cuaderno qué datos tiene una factura y marca cuáles son cantidades, precios y totales.",
    extend="Explica con un ejemplo inventado por qué una orden de compra ayuda a evitar pagar de más.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 12 (venta de ejemplo). «Papelería Los Aromos SpA» (emisor, RUT de ejemplo 00.000.000-0) vende a «Colegio Los Alerces» (receptor, nombre de ejemplo): "
     "30 cuadernos a $1.200 cada uno y 10 cajas de lápices a $3.000 cada una. Ambos productos son afectos a IVA (de ejemplo); tasa de ejemplo 10 %. Pago a crédito a 30 días; fecha de emisión: 5 de abril.")
build(
    O3, 3, F,
    use="Aprenderé a llenar una factura con datos de ejemplo, a calcular sus montos y a detectar errores de llenado.",
    prior=["Sé los campos de una factura.", "Sé calcular el IVA con una tasa de ejemplo.", "Sé qué es el neto y el total."],
    explain=[
        "Para llenar una factura se parte por los datos de las partes: emisor y receptor con su nombre y RUT. Luego se escribe el detalle, con cantidad, descripción y precio unitario de cada línea. El subtotal de cada línea es cantidad por precio; la suma de los subtotales es el neto; el IVA de ejemplo es el 10 % del neto y el total es neto más IVA.",
        "También se anota la forma de pago. En una venta a crédito a 30 días, el vencimiento es la fecha de emisión más 30 días. Antes de entregar el documento se hace una revisión final: comparar cantidades y precios con el pedido, repetir los cálculos y confirmar que los datos del receptor estén completos.",
        "Un error de llenado se corrige emitiendo un documento nuevo, como una nota de crédito, según la norma vigente; no se enmienda. El documento se emite a nombre de quien realmente compra: cambiar el receptor por conveniencia personal es una falta de ética y puede traer consecuencias legales.",
    ],
    vocab=[("vencimiento", "fecha límite de pago de una venta a crédito"), ("subtotal", "cantidad por precio unitario de una línea"), ("neto", "suma de los subtotales sin impuesto"), ("afecto a IVA", "producto que lleva IVA"), ("forma de pago", "si es al contado o a crédito y su plazo"), ("revisión final", "control antes de entregar el documento")],
    worked=[
        ("Llenar los montos", "Una factura de ejemplo vende 25 cajas de clips a $2.000 cada una, con IVA de ejemplo de 10 %. ¿Cuál es el neto, el IVA y el total?", ["Neto = 25 × 2.000 = 50.000.", "IVA = 5.000; total = 55.000."], "Neto $50.000; IVA $5.000; total $55.000"),
        ("Calcular el vencimiento", "Una factura de ejemplo se emite el 10 de junio con crédito a 30 días. ¿Cuándo vence? (Junio tiene 30 días.)", ["Se suman 30 días a la fecha: 10 de junio más 30 días.", "Pasados los 30 días de junio, se llega al 10 de julio."], "El 10 de julio"),
    ],
    mistakes=[("Calcular el IVA sobre cada línea y luego olvidar sumarlo al total.", "El total debe ser neto más IVA y quedaría subestimado.", "Calcula el neto, luego el IVA y suma ambos."),
              ("Cambiar el nombre del receptor para que la compra figure a nombre de otra persona.", "El documento debe reflejar quién compra realmente.", "Emite el documento a nombre de quien compra y consulta a la jefatura.")],
    T=[
        ("abc", "{F} ¿Qué documento corresponde emitir en esta venta entre empresas?", "Una factura", "Un comprobante de egreso", "Una cotización", "Una venta entre empresas se respalda con factura; el egreso es una constancia interna de pago."),
        ("=", "{F} ¿Cuántos pesos es el subtotal de los cuadernos?", "30*1200", "Se multiplica la cantidad por el precio unitario.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el subtotal de las cajas de lápices?", "10*3000", "Se multiplica la cantidad por el precio unitario.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el neto de la factura?", "30*1200+10*3000", "El neto es la suma de los subtotales de las dos líneas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el IVA de ejemplo sobre el neto?", "66000*10//100", "Se calcula el 10 % del neto.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el total de la factura?", "66000+6600", "El total es el neto más el IVA.", " pesos"),
        ("abc", "{F} ¿Qué datos de la ficha permiten saber cuándo vence el pago?", "La forma de pago (crédito a 30 días) y la fecha de emisión", "El RUT del emisor", "El nombre del colegio", "El vencimiento se calcula con la fecha y el plazo acordado."),
        ("abc", "{F} Si la factura se emite el 5 de abril con crédito a 30 días, ¿cuándo vence? (Abril tiene 30 días.)", "El 5 de mayo", "El 30 de abril", "El 30 de mayo", "Treinta días después del 5 de abril es el 5 de mayo."),
        ("=", "{F} La asistente escribe el total como $72.000 en vez del correcto. ¿Cuántos pesos de diferencia hay?", "72600-72000", "Se resta el total escrito al total correcto.", " pesos"),
        ("abc", "{F} Alguien sugiere calcular el IVA solo sobre los cuadernos. ¿Qué respondes?", "Como ambos productos son afectos, el IVA se calcula sobre el neto total", "Tiene razón: los lápices nunca llevan IVA", "El IVA se calcula sobre el total ya con IVA", "La ficha dice que ambos productos son afectos; el IVA se aplica al neto de todo lo afecto."),
        ("abc", "Antes de entregar la factura al colegio, ¿qué revisión final es la adecuada?", "Comparar cantidades, precios, cálculos y datos del receptor con el pedido", "Pedirle al colegio que revise los cálculos", "Revisar solo la ortografía del detalle", "La revisión es responsabilidad de quien emite y cubre cantidades, precios, cálculos y datos."),
        ("abc", "{F} El colegio pide que la factura salga a nombre de un apoderado, para beneficio personal de esa persona. ¿Qué corresponde?", "Emitirla a nombre de quien realmente compra y consultar a la jefatura", "Cambiar el nombre para tener contento al cliente", "Emitir dos facturas, una por cada nombre", "El documento debe reflejar a quien realmente compra; cambiarlo por conveniencia es faltar a la ética."),
        ("=", "{F} Si el colegio devuelve 6 cuadernos, ¿cuántos pesos netos debe tener la nota de crédito?", "6*1200", "Se multiplican los cuadernos devueltos por su precio unitario.", " pesos"),
    ],
    ctx=("abc", "Después de emitir una factura, el asistente nota que escribió 300 cuadernos en vez de 30. ¿Qué hace?", "Avisa al contador y se corrige con un documento formal, sin enmendar el original", "Tacha el cero con un lápiz y lo entrega", "Lo entrega así y espera que nadie lo note", "Los errores se corrigen con documentos formales y sin enmiendas."),
    sc=[
        ("En Contabilidad: ¿cómo se calcula el neto de una factura?", "Se suman los subtotales de todas las líneas", "El IVA se calcula después sobre ese neto."),
        ("¿Cuál es el vencimiento de una venta a crédito de 30 días?", "La fecha de emisión más 30 días", "El plazo comienza a contar desde la emisión."),
        ("¿Cómo se corrige un error de llenado en un documento emitido?", "Con un documento nuevo según la norma vigente, sin enmendar", "La enmienda quita valor al documento como prueba."),
    ],
    op=("Llena en tu cuaderno una factura de ejemplo para esta venta: «Papelería Los Aromos SpA» vende a «Liceo Los Coigües» (nombre de ejemplo) 40 cuadernos a $1.500 cada uno y 5 cajas de tijeras de punta roma a $6.000 cada una; productos afectos a IVA; tasa de ejemplo 10 %; crédito a 30 días; emisión el 12 de junio (junio tiene 30 días). Calcula subtotales, neto, IVA, total y vencimiento, y haz la revisión final.",
        "Cuadernos: 40 × 1.500 = 60.000. Tijeras: 5 × 6.000 = 30.000. Neto: 90.000. IVA: 9.000. Total: 99.000. Vencimiento: 12 de julio. Revisión final: cantidades y precios comparados con el pedido, cálculos repetidos y datos del receptor completos.",
        ["calcula todos los montos", "indica el vencimiento correcto", "hace una revisión final de datos y cálculos"],
        ["factura llenada en el cuaderno con sus cálculos"],
        ["olvidar el IVA en el total", "calcular mal el vencimiento", "no repasar los datos del receptor"],
        "Pregunta: «¿cómo comprobaste los cálculos?». Si no los repitió, pídele que los haga otra vez en la calculadora."),
    reinforce="Inventa una venta de tres productos y calcula el neto, el IVA de ejemplo y el total.",
    extend="Explica con un ejemplo inventado qué problema puede traer emitir un documento a nombre de quien no compró.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 13 (bandeja de documentos de ejemplo del día). D1: factura de compra N.º 210 por $88.000, con guía de despacho y orden de compra que coinciden. "
     "D2: factura de compra N.º 211 por $55.000, sin guía de despacho. D3: comprobante de egreso N.º 45 por el pago de D1, $88.000, sin firma de aprobación. "
     "D4: boleta de venta N.º 3001 por $12.000, que aparece archivada dos veces. Etapas: revisar, aprobar, pagar y archivar.")
build(
    O3, 4, F,
    use="Aprenderé a tramitar y registrar documentos aplicando criterios de control: coincidencia, aprobación, correlativos y resguardo de datos.",
    prior=["Sé las etapas de tramitación.", "Sé comparar orden de compra, guía y factura.", "Sé qué es una nota de crédito."],
    explain=[
        "Un criterio técnico de tramitación es no avanzar una etapa si falta algo. Una factura se aprueba solo si coincide con la orden de compra y la guía de despacho; un pago se registra con un comprobante de egreso firmado por quien aprueba; un documento duplicado se deja una sola vez en el archivo y se anota la duplicación.",
        "Los documentos se archivan por número correlativo, es decir, en orden numérico. Así, si falta un número en la serie (por ejemplo, 45, 46 y 48), se nota que falta el 47 y se busca, o se informa a la jefatura y se deja constancia. Una nota de crédito por devolución reduce lo que se debe pagar al proveedor.",
        "Quien aprueba y quien paga conviene que sean personas distintas: es un control cruzado que reduce errores y fraudes. Los documentos con datos personales se guardan con acceso restringido y solo se usan para su fin. Si algo no coincide, se avisa; nunca se ajusta un documento para que calce.",
    ],
    vocab=[("correlativo", "número que sigue un orden sin saltos"), ("duplicado", "documento repetido por error"), ("control cruzado", "revisión por una persona distinta de quien ejecuta"), ("constancia", "anotación que deja registro de lo ocurrido"), ("aprobación", "visto bueno de quien corresponde")],
    worked=[
        ("Decidir si se paga", "Llega una factura de ejemplo que coincide con su orden de compra y su guía de despacho. ¿Puede pasar a aprobación?", ["Coincide con lo pedido y lo recibido.", "Cumple el criterio para pasar a la etapa de aprobación."], "Sí, pasa a aprobación"),
        ("Detectar un número que falta", "En el archivo de comprobantes de ejemplo hay los números 20, 21, 23. ¿Qué se hace?", ["Falta el número 22 en la serie.", "Se busca el 22 y, si no aparece, se informa a la jefatura y se deja constancia."], "Buscar el 22 e informar si no aparece"),
    ],
    mistakes=[("Pagar una factura porque «ya viene firmada por el proveedor».", "Debe coincidir con lo pedido y lo recibido antes de pagar.", "Compara con la orden y la guía; si falta algo, avisa."),
              ("Archivar los dos ejemplares de un documento duplicado y registrar la venta dos veces.", "Se infla la venta registrada.", "Deja un solo ejemplar y anota la duplicación.")],
    T=[
        ("abc", "{F} ¿Cuál documento está listo para pasar a la etapa de aprobación?", "D1, porque coincide con la guía y la orden de compra", "D2, porque tiene un monto menor", "D3, porque ya es un comprobante de pago", "D1 es el único que cumple el criterio de coincidencia."),
        ("abc", "{F} ¿Qué le falta a D2 antes de poder aprobarse?", "La guía de despacho que compruebe lo recibido", "El pago del comprobante de egreso", "Un número de boleta", "Sin guía no se puede comprobar que se recibió lo facturado."),
        ("ab", "{F} ¿Qué le falta al comprobante D3 para tramitarse correctamente?", "La firma de aprobación", "Una nueva factura", "Un pago es válido para el control interno solo con su aprobación."),
        ("=", "{F} Si D1 y D2 se pagaran, ¿cuántos pesos sería el total?", "88000+55000", "Se suman los montos de las dos facturas.", " pesos"),
        ("abc", "{F} ¿Qué se hace con D4, la boleta archivada dos veces?", "Dejar un solo ejemplar y anotar la duplicación", "Archivar ambas y registrar dos ventas", "Eliminar una sin dejar constancia", "Un duplicado no se registra dos veces y se deja constancia."),
        ("abc", "¿En qué orden se tramita un documento de pago?", "Revisar, aprobar, pagar y archivar", "Pagar, archivar, revisar y aprobar", "Aprobar, archivar, pagar y revisar", "El pago se hace después de revisar y aprobar."),
        ("=", "{F} Si D4 se registrara dos veces, ¿cuántos pesos de venta quedarían registrados de más?", "12000*2-12000", "Se compara lo registrado dos veces con la venta real.", " pesos"),
        ("abc", "{F} ¿Por qué no se paga D2 hasta tener la guía?", "Porque no se puede comprobar que lo facturado fue recibido", "Porque la guía reemplaza a la factura al momento de pagar", "Porque la guía fija el descuento por pronto pago", "Se paga lo recibido; la guía es la prueba de la entrega."),
        ("=", "El proveedor emite una nota de crédito por $11.000 por una devolución de D1 ($88.000). ¿Cuántos pesos quedan por pagar?", "88000-11000", "La nota de crédito reduce el monto de la factura.", " pesos"),
        ("abc", "¿Qué ventaja tiene archivar por número correlativo?", "Permite notar si falta algún documento cuando hay un salto en la numeración", "Ahorra papel en la oficina", "Evita tener que pagar impuestos", "El salto en la serie delata el documento faltante."),
        ("abc", "En el archivo de comprobantes hay los números 72, 73 y 75. ¿Qué corresponde?", "Buscar el 74 y, si no aparece, informar a la jefatura y dejar constancia", "Crear un 74 sin respaldo para completar la serie", "Renumerar los demás comprobantes", "Un número faltante se busca y se informa; no se inventa."),
        ("abc", "¿Por qué conviene que quien aprueba y quien paga sean personas distintas?", "Es un control cruzado que reduce errores y fraudes", "Así se paga más rápido", "Porque cada persona cobra sueldo distinto", "Que dos personas revisen disminuye el riesgo de errores o fraudes."),
        ("abc", "{F} Un comprobante de egreso tiene el RUT y la cuenta bancaria de una persona proveedora. ¿Cómo se resguarda?", "Con acceso restringido y usándolo solo para el pago", "Dejándolo en una carpeta abierta para todo el personal", "Sacando copias para quien las pida", "Los datos personales se protegen limitando quién accede a ellos."),
    ],
    ctx=("abc", "Tu jefa te pide aprobar y pagar una factura que no coincide con la guía, porque «el proveedor es de confianza». ¿Qué haces?", "Explico la diferencia, pido la corrección formal y dejo constancia", "Pago igual para no discutir", "Cambio la guía para que coincida", "El control se cumple igual con proveedores conocidos y sin ajustar documentos."),
    sc=[
        ("En Contabilidad: ¿cuándo pasa una factura a aprobación?", "Cuando coincide con la orden de compra y la guía de despacho", "La coincidencia es el criterio previo a aprobar."),
        ("¿Qué indica un salto en la numeración correlativa?", "Que puede faltar un documento", "El número faltante debe buscarse o informarse."),
        ("¿Por qué separar quien aprueba de quien paga?", "Para tener un control cruzado", "La revisión de otra persona reduce errores y fraudes."),
    ],
    op=("Una bandeja de ejemplo tiene: factura N.º 310 por $60.000 con guía y orden que coinciden; factura N.º 311 por $45.000 sin orden de compra; comprobante de egreso N.º 12 sin firma; y comprobantes N.º 12, 13 y 15 en el archivo. Para cada caso escribe qué harías y por qué, y cierra con la regla de separar aprobación y pago.",
        "N.º 310: pasa a aprobación porque coincide. N.º 311: no se paga hasta tener la orden de compra; aviso al contador. Comprobante sin firma: se devuelve para la aprobación. Archivo: falta el 14; lo busco y, si no aparece, informo y dejo constancia. Aprobar y pagar los hacen personas distintas para tener control cruzado.",
        ["decide correctamente cada caso", "justifica con el criterio de control", "explica la separación de funciones"],
        ["hoja con una decisión y una razón por caso"],
        ["pagar sin orden de compra", "inventar el comprobante faltante", "no justificar la decisión"],
        "Pregunta: «¿qué documento te falta en cada caso?». Si no lo identifica, repasa los tres documentos de comparación."),
    reinforce="Escribe una lista de tres controles que aplicarías antes de pagar una factura.",
    extend="Explica con un ejemplo inventado cómo un control cruzado puede evitar un error costoso.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 14 (operaciones de ejemplo de «Comercial Pewen Ltda.»). (a) Compra de insumos a un proveedor de la misma ciudad. (b) Venta a un cliente de otra región de Chile. "
     "(c) Compra de mercaderías a una empresa de otro país. (d) Venta de mercaderías a una empresa de otro país. La empresa lleva sus registros en pesos chilenos; "
     "en el exterior se usa moneda extranjera, por ejemplo dólares. Tipo de cambio de ejemplo: $900 por cada dólar.")
build(
    O4, 1, F,
    use="Aprenderé la diferencia entre comercio nacional e internacional, qué cambia al registrar una operación con otro país y qué cuidados hay que tener.",
    prior=["Sé registrar una compra y una venta.", "Sé qué es una factura.", "Sé multiplicar cantidades por un valor."],
    explain=[
        "El comercio nacional ocurre entre personas y empresas de Chile. El comercio internacional ocurre con otro país: importar es comprar mercaderías a otro país y traerlas; exportar es venderlas a otro país. En las operaciones internacionales intervienen el transporte internacional, otra moneda y el control del Servicio Nacional de Aduanas, institución chilena que fiscaliza la entrada y salida de mercaderías.",
        "Cuando una operación se pacta en moneda extranjera, hay que convertirla a pesos para registrarla. Se usa el tipo de cambio, que es la cantidad de pesos que cuesta una unidad de moneda extranjera. El valor en pesos es la cantidad de moneda extranjera por el tipo de cambio del día del hecho. En este cuaderno los registros se llevan en pesos y el tipo de cambio es de ejemplo.",
        "Cada operación debe tener su respaldo: la factura del proveedor o cliente, los documentos de transporte y los documentos de aduana que correspondan según la norma vigente. Las reglas de cada trámite las explica un especialista, como un agente de aduanas; el registro contable solo parte cuando se tiene el respaldo.",
    ],
    vocab=[("comercio nacional", "compras y ventas dentro de Chile"), ("importar", "comprar mercaderías a otro país y traerlas"), ("exportar", "vender mercaderías a otro país"), ("moneda extranjera", "moneda de otro país, como el dólar"), ("tipo de cambio", "pesos que cuesta una unidad de moneda extranjera"), ("aduana", "servicio que controla la entrada y salida de mercaderías")],
    worked=[
        ("Clasificar una operación", "Una empresa de ejemplo compra telas a un proveedor de otro país. ¿Es importación o exportación?", ["La empresa compra y trae las mercaderías al país.", "Comprar a otro país es importar."], "Importación"),
        ("Convertir a pesos", "Una factura de ejemplo es por 80 dólares y el tipo de cambio de ejemplo es $850. ¿Cuántos pesos es?", ["Valor en pesos = dólares × tipo de cambio.", "80 × 850 = 68.000."], "$68.000"),
    ],
    mistakes=[("Registrar 300 dólares como 300 pesos.", "Se registra una cifra miles de veces menor a la real.", "Convierte la moneda extranjera a pesos con el tipo de cambio antes de registrar."),
              ("Aceptar un trámite aduanero «sin papeles» porque es más barato.", "Sin respaldo la operación no se puede registrar ni defender.", "Consulta a la jefatura y a un agente de aduanas; no se aceptan atajos.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es importar?", "Comprar mercaderías a otro país y traerlas", "Vender mercaderías a otro país", "Comprar mercaderías a una empresa de otra región de Chile", "Importar es comprar al extranjero; vender al extranjero es exportar."),
        ("abc", "En Contabilidad: ¿qué es exportar?", "Vender mercaderías a otro país", "Comprar mercaderías a otro país", "Vender mercaderías en otra región de Chile", "Exportar es vender mercaderías fuera del país."),
        ("ab", "¿Cuál de estas ventas es comercio nacional?", "Vender a un cliente de otra región de Chile", "Vender a una empresa de otro país", "Cuando el cliente está en Chile, la venta es nacional aunque sea en otra región."),
        ("abc", "{F} ¿Cuál operación es una importación?", "(c), la compra de mercaderías a una empresa de otro país", "(a), la compra de insumos en la misma ciudad", "(d), la venta a una empresa de otro país", "Importar es comprar a otro país."),
        ("abc", "{F} ¿Cuál operación es una exportación?", "(d), la venta de mercaderías a una empresa de otro país", "(b), la venta a otra región de Chile", "(c), la compra a una empresa de otro país", "Exportar es vender fuera del país."),
        ("=", "{F} Una compra de 100 dólares, ¿cuántos pesos es con el tipo de cambio de ejemplo?", "100*900", "Los pesos se obtienen multiplicando dólares por el tipo de cambio.", " pesos"),
        ("abc", "¿Qué institución chilena fiscaliza la entrada y salida de mercaderías del país?", "El Servicio Nacional de Aduanas", "La Dirección del Trabajo", "El banco de la empresa", "Aduanas controla el ingreso y la salida de mercaderías."),
        ("abc", "{F} ¿Por qué las operaciones internacionales requieren más documentos?", "Porque intervienen otro país, transporte internacional y control aduanero", "Porque siempre se pagan en efectivo", "Porque no necesitan factura", "Los documentos extra respaldan el transporte y el paso por aduana."),
        ("=", "{F} Una factura es por 250 dólares. ¿Cuántos pesos es con el tipo de cambio de ejemplo?", "250*900", "Se multiplica el monto en dólares por el tipo de cambio.", " pesos"),
        ("abc", "Un auxiliar de una empresa que lleva registros en pesos anota una compra de 450 dólares como 450 pesos. ¿Qué error comete?", "No convirtió la moneda extranjera a pesos con el tipo de cambio", "Olvidó que la compra es nacional", "Sumó dos veces la compra", "La cifra debe expresarse en pesos usando el tipo de cambio del día."),
        ("abc", "Una factura de exportación de ejemplo no indica en qué moneda está expresada. ¿Qué falta?", "La moneda, para poder convertirla a pesos con el tipo de cambio", "Solo la dirección del cliente", "Nada, porque se asume pesos", "Sin la moneda no se sabe cuánto vale el documento en pesos."),
        ("=", "{F} Se compran 60 unidades a 5 dólares cada una. ¿Cuántos pesos es el total con el tipo de cambio de ejemplo?", "60*5*900", "Primero se obtiene el total en dólares y luego se convierte a pesos.", " pesos"),
        ("abc", "Un conocido ofrece hacer un trámite aduanero «sin papeles» y más barato. ¿Qué corresponde?", "Rechazarlo y consultar a la jefatura y a un agente de aduanas", "Aceptarlo porque ahorra dinero", "Aceptarlo si el conocido promete que no habrá problemas", "Una operación sin respaldo no puede registrarse ni defenderse ante la autoridad."),
    ],
    ctx=("abc", "Una empresa de ejemplo recibe una factura en dólares y el auxiliar no sabe qué tipo de cambio usar. ¿Qué hace?", "Consulta al contador cuál tipo de cambio corresponde y anota su fuente", "Usa el que recuerde de la semana pasada", "No registra nunca la operación", "El tipo de cambio debe tener una fuente identificada, no una memoria."),
    sc=[
        ("En Contabilidad: ¿qué es el tipo de cambio?", "Los pesos que cuesta una unidad de moneda extranjera", "Sirve para convertir moneda extranjera a pesos."),
        ("¿Cómo se convierte una cifra en dólares a pesos?", "Se multiplica por el tipo de cambio", "Los pesos son dólares por el valor de cada dólar."),
        ("¿Qué institución controla la entrada y salida de mercaderías?", "El Servicio Nacional de Aduanas", "Es la institución aduanera de Chile."),
    ],
    op=("Una tienda de ejemplo realizó cuatro operaciones: compró cajas de cartón en su ciudad; vendió productos a una tienda de otra región del país; compró repuestos a una empresa de otro país por 120 dólares; vendió productos a una empresa de otro país por 90 dólares. Con un tipo de cambio de ejemplo de $900, clasifica cada operación (nacional, importación o exportación) y convierte a pesos las dos internacionales.",
        "1) Nacional. 2) Nacional. 3) Importación: 120 × 900 = 108.000 pesos. 4) Exportación: 90 × 900 = 81.000 pesos. Se archivan factura y documentos de transporte y aduana de las operaciones 3 y 4.",
        ["clasifica correctamente las cuatro operaciones", "convierte a pesos con el tipo de cambio", "nombra el respaldo de las internacionales"],
        ["tabla con operación, clasificación y valor en pesos"],
        ["registrar los dólares como pesos", "confundir importar con exportar", "no nombrar el respaldo"],
        "Pregunta: «¿cuál es el tipo de cambio y de dónde lo sacaste?». Si no lo puede indicar, repasa que debe tener fuente."),
    reinforce="Escribe tres ejemplos de productos que un negocio chileno podría importar y dos que podría exportar, sin nombres de marcas.",
    extend="Explica con un ejemplo inventado por qué una venta a otro país tiene más documentos que una venta en tu ciudad.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 15 (importación de ejemplo de «Comercial Pewen Ltda.»). Mercaderías por 2.000 dólares valor FOB; flete y seguro internacional: 300 dólares; "
     "tipo de cambio de ejemplo: $900 por dólar. Gastos de internación pagados en Chile (valor de ejemplo): $150.000. "
     "FOB (simplificado): precio de la mercadería puesta a bordo, sin flete ni seguro internacional. CIF (simplificado): costo de la mercadería más seguro y flete hasta el puerto de destino.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos básicos de una importación (FOB, CIF, flete, seguro, gastos de internación) y cómo se forma el costo de las mercaderías en pesos.",
    prior=["Sé qué es importar.", "Sé convertir dólares a pesos.", "Sé sumar los componentes de un costo."],
    explain=[
        "Al comprar a otro país, el precio puede incluir distintos tramos del viaje. El valor FOB es el precio de la mercadería puesta a bordo en el país de origen, sin flete ni seguro internacional. El valor CIF suma el costo de la mercadería, el seguro y el flete hasta el puerto de destino. Estas son definiciones simplificadas: las reglas completas las enseña un especialista en comercio exterior.",
        "El flete es el pago por transportar las mercaderías y el seguro cubre posibles daños o pérdidas durante el viaje. Al llegar al país se pagan gastos de internación: derechos de aduana y otros costos para ingresar las mercaderías. Sus valores y reglas los fija la norma vigente; aquí se usan valores de ejemplo.",
        "El costo de las mercaderías importadas, en pesos, es el valor CIF convertido con el tipo de cambio más los gastos de internación. Ese costo total es el que se registra como activo en Mercaderías. Si se registra solo el valor FOB, el costo queda subestimado y el resultado futuro se calcula mal.",
    ],
    vocab=[("FOB", "valor de la mercadería puesta a bordo, sin flete ni seguro"), ("CIF", "costo de la mercadería más seguro y flete"), ("flete", "pago por transportar las mercaderías"), ("seguro", "cobertura de daños o pérdidas durante el viaje"), ("gastos de internación", "costos para ingresar las mercaderías al país"), ("costo total", "valor CIF en pesos más gastos de internación")],
    worked=[
        ("Valor FOB en pesos", "Una empresa de ejemplo compra mercaderías por 500 dólares FOB con un tipo de cambio de ejemplo de $800. ¿Cuánto es el FOB en pesos?", ["Valor en pesos = dólares × tipo de cambio.", "500 × 800 = 400.000."], "$400.000"),
        ("Valor CIF en pesos", "Con 500 dólares FOB, 50 dólares de flete y seguro y un tipo de cambio de ejemplo de $800, ¿cuánto es el valor CIF en pesos?", ["CIF en dólares = 500 + 50 = 550.", "550 × 800 = 440.000."], "$440.000"),
    ],
    mistakes=[("Registrar solo el valor FOB como costo de las mercaderías.", "Se omiten flete, seguro y gastos de internación que también forman parte del costo.", "Suma CIF en pesos y gastos de internación para obtener el costo total."),
              ("Convertir el flete con otro tipo de cambio cualquiera.", "El valor en pesos cambia y no se puede verificar.", "Usa el tipo de cambio indicado por la fuente definida para el hecho.")],
    T=[
        ("abc", "En Comercio internacional: ¿qué es el tipo de cambio?", "La cantidad de pesos que cuesta una unidad de moneda extranjera", "El impuesto que se paga en la aduana", "El precio de transporte de las mercaderías", "El tipo de cambio convierte monedas; no es un impuesto ni un transporte."),
        ("abc", "¿Qué es el valor FOB (de forma simplificada)?", "El precio de la mercadería puesta a bordo, sin flete ni seguro internacional", "El precio de la mercadería con flete y seguro hasta el destino", "El valor de los derechos pagados en Chile", "FOB deja afuera flete y seguro internacionales."),
        ("ab", "¿Qué incluye el valor CIF (de forma simplificada)?", "El costo de la mercadería más el seguro y el flete", "Solo el costo de la mercadería", "CIF suma los tres componentes: mercadería, seguro y flete."),
        ("=", "{F} ¿Cuántos pesos es el valor FOB?", "2000*900", "Se multiplica el valor FOB en dólares por el tipo de cambio.", " pesos"),
        ("=", "{F} ¿Cuántos pesos son el flete y el seguro?", "300*900", "Se convierten a pesos los dólares de flete y seguro.", " pesos"),
        ("=", "{F} ¿Cuántos dólares es el valor CIF?", "2000+300", "El CIF suma la mercadería, el flete y el seguro.", " dólares"),
        ("=", "{F} ¿Cuántos pesos es el valor CIF?", "(2000+300)*900", "Se convierte a pesos el total CIF en dólares.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el costo total de las mercaderías (CIF en pesos más gastos de internación)?", "(2000+300)*900+150000", "El costo total suma el CIF en pesos y los gastos de internación.", " pesos"),
        ("abc", "{F} ¿Qué cuenta aumenta al registrar la importación y por qué monto?", "Mercaderías, por el costo total", "Gasto, por el valor FOB", "Ventas, por el valor CIF", "Las mercaderías importadas son un activo y se registran por su costo total."),
        ("abc", "{F} Un auxiliar registra Mercaderías solo por el FOB en pesos. ¿Qué omite?", "Flete, seguro y gastos de internación, que forman parte del costo", "Nada, porque el FOB es el costo completo", "El IVA de la venta", "El costo total incluye todo lo necesario para dejar las mercaderías en la empresa."),
        ("abc", "{F} Si el tipo de cambio de ejemplo del día fuera $950 en lugar de $900, ¿qué pasaría con el FOB en pesos?", "Subiría, porque cada dólar vale más pesos", "Bajaría, porque cada dólar vale menos pesos", "Quedaría igual, porque el FOB está en dólares", "Con más pesos por dólar, el mismo valor en dólares equivale a más pesos."),
        ("=", "{F} ¿Cuántos pesos más sería el FOB si el tipo de cambio fuera $950 en lugar de $900?", "2000*950-2000*900", "Se compara el FOB con cada tipo de cambio y se resta.", " pesos"),
        ("abc", "¿Qué documentos conviene archivar juntos para respaldar el costo de una importación?", "La factura del proveedor extranjero y los documentos de transporte y de aduana", "Solo la factura del proveedor", "Solo el documento de transporte", "El costo total se respalda con todos los documentos del viaje."),
    ],
    ctx=("abc", "Una empresa de ejemplo ve dos ofertas por las mismas mercaderías: una a 1.000 dólares FOB y otra a 1.050 dólares CIF. Un estudiante dice que la FOB «siempre es más barata». ¿Qué respondes?", "No se pueden comparar así: hay que sumar flete y seguro a la oferta FOB antes de comparar", "Tiene razón, porque 1.000 es menor que 1.050", "La CIF es siempre más barata", "FOB y CIF miden tramos distintos; se comparan sumando lo que falta."),
    sc=[
        ("En Comercio internacional: ¿qué incluye el valor CIF de forma simplificada?", "El costo de la mercadería más el seguro y el flete", "CIF suma el viaje hasta el puerto de destino."),
        ("¿Cómo se obtiene el costo total de una importación?", "Valor CIF en pesos más gastos de internación", "Ese monto es el que se registra en mercaderías."),
        ("¿Quién fija los gastos de internación reales?", "La norma vigente", "Aquí solo se usan valores de ejemplo."),
    ],
    op=("Una importación de ejemplo tiene mercaderías por 1.500 dólares FOB, flete y seguro por 150 dólares, tipo de cambio de ejemplo de $880 y gastos de internación de ejemplo por $100.000. Calcula el valor CIF en dólares y en pesos, y el costo total en pesos; luego escribe qué documentos archivarías.",
        "CIF en dólares: 1.500 + 150 = 1.650. CIF en pesos: 1.650 × 880 = 1.452.000. Costo total: 1.452.000 + 100.000 = 1.552.000. Archivo: factura del proveedor extranjero, documentos de transporte y de aduana.",
        ["calcula el CIF en dólares y en pesos", "suma los gastos de internación", "nombra los documentos de respaldo"],
        ["hoja con los cálculos y la lista de documentos"],
        ["registrar solo el FOB", "no convertir a pesos", "no nombrar documentos de respaldo"],
        "Pregunta: «¿qué incluye el costo total?». Si omite los gastos de internación, repasa la definición."),
    reinforce="Inventa una importación con valores FOB y de flete en dólares, y calcula el CIF en pesos con un tipo de cambio de ejemplo.",
    extend="Explica por qué un cambio en el tipo de cambio altera el costo en pesos de una importación aunque el precio en dólares sea el mismo.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 16 (hechos de ejemplo de «Comercial Pewen Ltda.»; registros en pesos; IVA de ejemplo 10 %). "
     "Hecho 1 (3 de junio): importa mercaderías por un valor CIF de 1.000 dólares, a crédito con el proveedor extranjero; tipo de cambio de ejemplo: $900 (sin otros impuestos de importación, para simplificar). "
     "Hecho 2 (10 de junio): vende en Chile al contado, neto $400.000, más IVA. "
     "Hecho 3 (15 de junio): exporta a crédito mercaderías por 500 dólares; tipo de cambio de ejemplo: $880; en este caso de ejemplo no se agrega IVA.")
build(
    O4, 3, F,
    use="Aprenderé a registrar en asientos una importación, una venta nacional y una exportación con datos de ejemplo.",
    prior=["Sé hacer asientos con debe y haber.", "Sé calcular IVA con tasa de ejemplo.", "Sé convertir moneda extranjera."],
    explain=[
        "Para registrar una operación internacional se sigue un orden: revisar los documentos, tomar el tipo de cambio de la fecha del hecho con su fuente, convertir a pesos y escribir el asiento. Una importación a crédito carga Mercaderías (activo, al debe) y abona una cuenta de deuda con el proveedor del exterior (pasivo, al haber).",
        "Una exportación a crédito carga una cuenta de cobro, como Clientes del exterior (activo, al debe), y abona Ventas de exportación (ingreso, al haber). El tratamiento tributario de las exportaciones y de las importaciones lo define la norma vigente; en este cuaderno se simplifica y se indica en cada caso. Una venta nacional con IVA se registra igual que en OAE-02: Caja o Clientes al debe; Ventas e IVA Débito Fiscal al haber.",
        "Se usa el tipo de cambio de la fecha del hecho porque es el valor de ese día. Si el documento no trae el tipo de cambio, se consulta al contador y se anota su fuente. El asiento siempre se comprueba: el total del debe es igual al total del haber.",
    ],
    vocab=[("proveedor del exterior", "empresa de otro país a la que se compra"), ("cliente del exterior", "empresa de otro país a la que se vende"), ("venta de exportación", "ingreso por vender a otro país"), ("tipo de cambio del día", "valor de la moneda extranjera en la fecha del hecho"), ("fuente", "origen del dato, que debe poder verificarse")],
    worked=[
        ("Importación a crédito", "Una empresa de ejemplo importa mercaderías por 300 dólares CIF a crédito con tipo de cambio de ejemplo de $850. ¿Cuál es el asiento (sin otros impuestos)?", ["300 × 850 = 255.000.", "Mercaderías aumenta (debe) y la deuda con el proveedor del exterior también (haber)."], "Debe Mercaderías 255.000; Haber Proveedores del exterior 255.000"),
        ("Venta nacional al contado", "Una empresa de ejemplo vende al contado en Chile, neto $100.000, con IVA de ejemplo de 10 %. ¿Cuál es el asiento?", ["IVA = 10.000; total = 110.000.", "Entra dinero a Caja; se registran Ventas e IVA Débito Fiscal."], "Debe Caja 110.000; Haber Ventas 100.000 e IVA Débito Fiscal 10.000"),
    ],
    mistakes=[("Registrar la exportación con el tipo de cambio de otro día.", "El valor en pesos del hecho queda mal.", "Usa el tipo de cambio de la fecha del hecho y anota su fuente."),
              ("Registrar una exportación a crédito con Debe Caja.", "El dinero aún no entra; se cobra después.", "Carga Clientes del exterior; Caja se usa cuando se cobre.")],
    T=[
        ("=", "{F} Hecho 1: ¿cuántos pesos vale la importación?", "1000*900", "Se multiplican los dólares por el tipo de cambio de ejemplo.", " pesos"),
        ("abc", "{F} ¿Cuál es el asiento del Hecho 1?", "Debe Mercaderías 900.000; Haber Proveedores del exterior 900.000", "Debe Proveedores del exterior 900.000; Haber Mercaderías 900.000", "Debe Mercaderías 900.000; Haber Caja 900.000", "Es una compra a crédito: aumentan las mercaderías y la deuda, no sale dinero de Caja."),
        ("abc", "{F} En el Hecho 1, la cuenta de deuda con el proveedor del exterior es un...", "Pasivo", "Activo", "Ingreso", "Es una obligación con otros, es decir, un pasivo."),
        ("=", "{F} Hecho 2: ¿cuántos pesos es el IVA de ejemplo?", "400000*10//100", "El IVA es el 10 % del neto.", " pesos"),
        ("abc", "{F} ¿Cuál es el asiento del Hecho 2?", "Debe Caja 440.000; Haber Ventas 400.000 e IVA Débito Fiscal 40.000", "Debe Ventas 440.000; Haber Caja 440.000", "Debe Caja 400.000; Haber Ventas 400.000", "Entra dinero a Caja por el total, y se registran la venta y el IVA débito al haber."),
        ("=", "{F} Hecho 3: ¿cuántos pesos vale la exportación?", "500*880", "Se multiplican los dólares por el tipo de cambio de ejemplo de ese día.", " pesos"),
        ("abc", "{F} ¿Cuál es el asiento del Hecho 3?", "Debe Clientes del exterior 440.000; Haber Ventas de exportación 440.000", "Debe Caja 440.000; Haber Ventas de exportación 440.000", "Debe Ventas de exportación 440.000; Haber Clientes del exterior 440.000", "Es a crédito: se registra un derecho de cobro (debe) y el ingreso (haber)."),
        ("abc", "¿Por qué se usa el tipo de cambio de la fecha del hecho?", "Porque es el valor de la moneda en el momento en que ocurrió la operación", "Porque siempre es el más bajo del mes", "Porque lo decide el cliente o el proveedor", "El valor en pesos del hecho se mide con el tipo de cambio de ese día."),
        ("=", "{F} Considerando los Hechos 2 y 3, ¿cuántos pesos suman las ventas registradas (sin IVA)?", "400000+440000", "Se suman los ingresos de ambas ventas.", " pesos"),
        ("abc", "{F} Un auxiliar registra el Hecho 3 como 500 pesos. ¿Qué consecuencia tiene?", "Las ventas quedan registradas muy por debajo de su valor real", "Las ventas quedan registradas de más", "No hay consecuencia, porque son las mismas unidades", "Registrar la cifra en dólares como pesos subestima el ingreso."),
        ("=", "{F} ¿Cuántos pesos de ventas se dejaron de registrar si el Hecho 3 se anotó como 500 pesos?", "440000-500", "Se resta lo anotado al valor correcto.", " pesos"),
        ("abc", "Un documento de exportación de ejemplo no trae el tipo de cambio. ¿Qué haces?", "Consulto al contador qué tipo de cambio corresponde y anoto su fuente", "Uso el que me parezca razonable", "Dejo la operación sin registrar para siempre", "El dato debe tener una fuente verificable."),
        ("abc", "{F} ¿Qué documentos archivarías para respaldar el Hecho 1?", "La factura del proveedor extranjero y los documentos de transporte y aduana", "Solo un correo de aviso", "Solo la boleta de una venta nacional", "Una importación se respalda con la factura y los documentos del viaje."),
    ],
    ctx=("abc", "Una auxiliar de ejemplo registra la exportación a crédito del Hecho 3 con Debe Caja. El contador la revisa. ¿Qué corrección corresponde?", "Cambiar Caja por Clientes del exterior, porque el dinero aún no se cobra", "Dejarlo porque igual cuadra", "Anotar la venta en una cuenta de gastos", "Un cobro pendiente es un derecho de cobro, no dinero en caja."),
    sc=[
        ("En Comercio internacional: ¿qué cuenta se carga en una importación a crédito?", "Mercaderías", "Aumenta el activo que se recibe."),
        ("¿Qué tipo de cambio se usa para registrar un hecho?", "El de la fecha del hecho, con su fuente", "El valor depende del día en que ocurrió."),
        ("¿Se carga Caja en una exportación a crédito?", "No, se carga Clientes del exterior", "El dinero se cobra después, por eso no entra a Caja todavía."),
    ],
    op=("Escribe los asientos de ejemplo de estos dos hechos de una empresa que lleva registros en pesos: (a) importa a crédito mercaderías por 400 dólares CIF, con tipo de cambio de ejemplo de $870, sin otros impuestos; (b) exporta a crédito mercaderías por 200 dólares, con tipo de cambio de ejemplo de $860, sin IVA en este caso de ejemplo. Calcula los pesos y comprueba que debe = haber.",
        "(a) 400 × 870 = 348.000: Debe Mercaderías 348.000; Haber Proveedores del exterior 348.000. (b) 200 × 860 = 172.000: Debe Clientes del exterior 172.000; Haber Ventas de exportación 172.000. Ambos asientos cuadran.",
        ["convierte bien los dólares a pesos", "usa las cuentas correctas", "comprueba que debe = haber"],
        ["hoja con los cálculos y los dos asientos"],
        ["usar Caja en operaciones a crédito", "mezclar tipos de cambio", "no comprobar el cuadre"],
        "Pregunta: «¿por qué no usaste Caja?». Si no menciona que es a crédito, repasa el concepto."),
    reinforce="Convierte a pesos tres cifras en dólares con un tipo de cambio de ejemplo y escribe el asiento de una de ellas.",
    extend="Explica por qué dos operaciones iguales en dólares pueden valer distinto en pesos si ocurren en días distintos.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 17 (diferencia de cambio, ejemplo inventado). Una empresa compró a crédito mercaderías importadas por 1.000 dólares cuando el tipo de cambio de ejemplo era $900: deuda registrada $900.000. "
     "Se paga 30 días después. Caso A: ese día el tipo de cambio de ejemplo es $920. Caso B: ese día es $880. Regla para una deuda en dólares: si se pagan más pesos que los registrados, hay una pérdida por diferencia de cambio; "
     "si se pagan menos, hay una ganancia.")
build(
    O4, 4, F,
    use="Aprenderé a calcular y registrar la diferencia de cambio al pagar o cobrar una operación en moneda extranjera.",
    prior=["Sé convertir moneda extranjera a pesos.", "Sé registrar asientos con debe y haber.", "Sé qué es una pérdida y una ganancia."],
    explain=[
        "Cuando una operación se pacta en dólares y se paga después, el tipo de cambio puede haber cambiado. La diferencia de cambio es la diferencia entre los pesos que se pagan o cobran hoy y los pesos que se registraron el día del hecho. Se calcula como pesos del pago menos pesos registrados.",
        "Para una deuda en dólares: si el dólar sube, se pagan más pesos y hay una pérdida por diferencia de cambio; si el dólar baja, se pagan menos pesos y hay una ganancia. Para un cobro en dólares ocurre lo contrario: si el dólar sube, se reciben más pesos y hay una ganancia. La regla simple es mirar si se pagan o reciben más pesos que los registrados y si se es deudor o acreedor.",
        "El asiento del pago de una deuda con pérdida carga Proveedores (por lo registrado) y Pérdida por diferencia de cambio, y abona Banco por lo pagado. Con ganancia, abona Banco por lo pagado y Ganancia por diferencia de cambio. El tipo de cambio de cada día tiene su fuente y se anota. El tratamiento tributario lo define la norma vigente.",
    ],
    vocab=[("diferencia de cambio", "diferencia entre los pesos pagados o cobrados y los registrados"), ("pérdida por diferencia de cambio", "pesos pagados de más en una deuda"), ("ganancia por diferencia de cambio", "pesos pagados de menos en una deuda"), ("deudor", "quien debe pagar"), ("acreedor", "quien debe cobrar")],
    worked=[
        ("Pago con pérdida", "Una deuda de ejemplo de 500 dólares se registró a $900 (450.000 pesos). Se paga cuando el tipo de cambio de ejemplo es $910. ¿Cuál es la diferencia de cambio?", ["Se pagan 500 × 910 = 455.000.", "455.000 − 450.000 = 5.000 pesos de más: pérdida."], "Pérdida de $5.000"),
        ("Cobro con pérdida", "Una empresa de ejemplo cobra 200 dólares registrados a $900 (180.000 pesos). Cobra con un tipo de cambio de ejemplo de $890. ¿Qué ocurre?", ["Recibe 200 × 890 = 178.000.", "Recibe 2.000 pesos menos de los registrados: pérdida."], "Pérdida de $2.000"),
    ],
    mistakes=[("Decir que si el dólar sube siempre gana la empresa.", "Depende de si debe o cobra dólares.", "Revisa si la empresa paga o recibe y compara los pesos con los registrados."),
              ("Ajustar el costo de las mercaderías por la diferencia de cambio.", "La diferencia aparece al pagar y se registra aparte, en su propia cuenta.", "Registra la pérdida o ganancia en la cuenta de diferencia de cambio.")],
    T=[
        ("abc", "En Comercio internacional: ¿qué es la diferencia de cambio?", "La diferencia entre los pesos pagados o cobrados y los pesos registrados", "El impuesto que se paga en la aduana", "El flete de una importación", "Se produce por el cambio del tipo de cambio entre el hecho y el pago."),
        ("abc", "Si se debe en dólares y el dólar sube antes del pago, ¿se pagan más o menos pesos?", "Más pesos", "Menos pesos", "Los mismos pesos", "Con un dólar más caro, la misma deuda en dólares cuesta más pesos."),
        ("ab", "Una pérdida por diferencia de cambio en una deuda en dólares significa que...", "Se pagan más pesos de los registrados", "Se pagan menos pesos de los registrados", "Pagar de más es una pérdida; pagar de menos es una ganancia."),
        ("=", "{F} Caso A: ¿cuántos pesos se pagan?", "1000*920", "Se multiplican los dólares por el tipo de cambio del día del pago.", " pesos"),
        ("=", "{F} Caso A: ¿cuántos pesos es la pérdida por diferencia de cambio?", "1000*920-900000", "Se resta lo registrado a lo pagado.", " pesos"),
        ("=", "{F} Caso B: ¿cuántos pesos se pagan?", "1000*880", "Se multiplican los dólares por el tipo de cambio de ese día.", " pesos"),
        ("=", "{F} Caso B: ¿cuántos pesos es la ganancia por diferencia de cambio?", "900000-1000*880", "Se resta lo pagado a lo registrado.", " pesos"),
        ("abc", "{F} ¿Cuál es el asiento del Caso A?", "Debe Proveedores 900.000 y Pérdida por diferencia de cambio 20.000; Haber Banco 920.000", "Debe Proveedores 920.000; Haber Banco 900.000 y Ganancia por diferencia de cambio 20.000", "Debe Banco 920.000; Haber Proveedores 920.000", "Se cancela la deuda registrada, se reconoce la pérdida y sale dinero del banco por lo pagado."),
        ("abc", "{F} ¿Cuál es el asiento del Caso B?", "Debe Proveedores 900.000; Haber Banco 880.000 y Ganancia por diferencia de cambio 20.000", "Debe Proveedores 880.000 y Pérdida por diferencia de cambio 20.000; Haber Banco 900.000", "Debe Banco 880.000; Haber Proveedores 880.000", "Se cancela la deuda registrada, sale menos dinero del banco y la diferencia es una ganancia."),
        ("abc", "Un estudiante dice: «si el dólar sube, la empresa siempre gana». ¿Qué respondes?", "Depende: si debe dólares pierde; si cobra dólares gana", "Tiene razón, siempre gana", "Nunca gana porque el dólar solo sirve para importar", "Quien debe dólares paga más pesos al subir; quien cobra dólares recibe más."),
        ("abc", "Una deuda en dólares de ejemplo se pagó con una pérdida. Un auxiliar suma esa pérdida al costo de las mercaderías. ¿Qué error comete?", "Mezcla un efecto del pago con el costo de la mercadería, que debe registrarse aparte", "Ninguno, porque es lo mismo", "No convirtió dólares a pesos", "La diferencia de cambio se registra en su cuenta específica."),
        ("=", "Un cliente del exterior debe 600 dólares registrados a $900 (540.000 pesos). Paga cuando el tipo de cambio de ejemplo es $930. ¿Cuántos pesos de ganancia por diferencia de cambio hay?", "600*930-540000", "La empresa recibe más pesos de los registrados.", " pesos"),
        ("abc", "Un cliente del exterior debe 400 dólares registrados a $900 y paga con el dólar a $870. ¿Es ganancia o pérdida para quien cobra?", "Pérdida, porque recibe menos pesos que los registrados", "Ganancia, porque el dólar bajó", "No hay diferencia, porque la deuda es la misma en dólares", "Al cobrar dólares, un dólar más barato da menos pesos que los registrados."),
    ],
    ctx=("abc", "Una auxiliar de ejemplo debe registrar un pago en dólares, pero no tiene el tipo de cambio del día. ¿Qué hace?", "Pide el dato al contador, que indica la fuente, y lo anota en el registro", "Usa el tipo de cambio de la deuda original para que no haya diferencia", "No registra el pago hasta fin de año", "Si se usa un dato inventado para evitar diferencias se distorsiona la información."),
    sc=[
        ("En Comercio internacional: ¿cómo se calcula la diferencia de cambio?", "Pesos pagados o cobrados menos pesos registrados", "Esa resta muestra si hay más o menos pesos."),
        ("¿Qué pasa con una deuda en dólares si el dólar baja antes del pago?", "Se pagan menos pesos y hay una ganancia", "La misma deuda en dólares equivale a menos pesos."),
        ("¿Dónde se registra la diferencia de cambio?", "En su propia cuenta de pérdida o ganancia", "No se mezcla con el costo de las mercaderías."),
    ],
    op=("Una empresa de ejemplo debe 800 dólares registrados a $900 (720.000 pesos) y los paga cuando el tipo de cambio de ejemplo es $915. Calcula los pesos pagados y la diferencia de cambio, indica si es pérdida o ganancia, escribe el asiento y anota qué fuente indicarías para el tipo de cambio.",
        "Pesos pagados: 800 × 915 = 732.000. Diferencia: 732.000 − 720.000 = 12.000, pérdida. Asiento: Debe Proveedores 720.000 y Pérdida por diferencia de cambio 12.000; Haber Banco 732.000. Fuente: la indicada por el contador para el día del pago, anotada en el registro.",
        ["calcula los pesos pagados y la diferencia", "clasifica correctamente la pérdida o ganancia", "escribe el asiento y menciona la fuente"],
        ["hoja con cálculos, asiento y nota de fuente"],
        ["confundir pérdida con ganancia", "sumar la pérdida al costo", "no anotar la fuente"],
        "Pregunta: «¿pagaste más o menos pesos que los registrados?». Si no responde, repasa la regla."),
    reinforce="Inventa una deuda en dólares y calcula la diferencia de cambio con dos tipos de cambio distintos.",
    extend="Explica por qué una empresa que cobra mucho en dólares y paga en pesos puede verse afectada por el tipo de cambio.",
)
