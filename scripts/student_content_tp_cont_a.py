"""Contabilidad TP 3.º y 4.º medio: OAE-01 (leer y utilizar información contable) y OAE-02 (procesar información contable). Empresas, cuentas e importes inventados; sin software."""
from __future__ import annotations

from tp_cont_common import build

O1 = "TP-CONT-3y4-OAE-01"
O2 = "TP-CONT-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (empresa de ejemplo, inventada). «Ferretería Los Aromos Ltda.» tiene a fin de mes: Caja $200.000; Banco $800.000; Mercaderías $1.500.000; "
     "Deudas con proveedores $600.000; Capital $1.900.000. Quienes piden información: la dueña (decide las compras), el banco (evalúa un préstamo) "
     "y el Servicio de Impuestos Internos (revisa el cumplimiento tributario).")
build(
    O1, 1, F,
    use="Aprenderé para qué sirve la información contable, quién la usa y qué riesgos hay al leerla o compartirla.",
    prior=["Sé sumar y restar cifras en pesos.", "Sé leer una tabla simple.", "Sé que una empresa vende, compra y paga."],
    explain=[
        "La contabilidad es el sistema que registra, ordena y resume los hechos económicos de una empresa para producir información útil. «Sobre la marcha de la empresa» quiere decir información periódica (por ejemplo, mensual) que muestra cuánto tiene, cuánto debe y si gana o pierde, para decidir a tiempo.",
        "Esa información la usan personas internas (la dueña, las jefaturas) y externas (el banco, los proveedores, el Servicio de Impuestos Internos). Para ser útil debe ser oportuna (llega a tiempo), comprensible, respaldada por documentos y confidencial (solo la ve quien corresponde). Se prepara según las normas internacionales de información financiera que apliquen a la empresa y la legislación tributaria vigente: el contador confirma cuáles corresponden.",
        "Todo se ordena con la ecuación patrimonial: activo = pasivo + patrimonio. El activo es lo que la empresa tiene y le sirve; el pasivo es lo que debe a otros; el patrimonio es lo que pertenece a los dueños. Caja y banco son el dinero disponible. Los riesgos más comunes son registrar sin documento de respaldo, mezclar gastos personales con los de la empresa y compartir datos con quien no debe verlos.",
    ],
    vocab=[("contabilidad", "sistema que registra y resume los hechos económicos de una empresa"), ("activo", "bien o derecho que la empresa tiene y le sirve"), ("pasivo", "deuda u obligación con otros"), ("patrimonio", "parte del activo que pertenece a los dueños"), ("usuario", "persona o institución que usa la información contable"), ("respaldo", "documento que prueba un hecho registrado"), ("confidencialidad", "reservar la información para quien corresponde")],
    worked=[
        ("Calcular el patrimonio", "Una empresa de ejemplo tiene activos por $900.000 y pasivos por $350.000. ¿Cuál es su patrimonio?", ["Se parte de activo = pasivo + patrimonio.", "Se despeja: patrimonio = activo − pasivo = 900.000 − 350.000."], "$550.000"),
        ("Identificar al usuario", "Una proveedora de ejemplo quiere saber si la empresa podrá pagarle una factura dentro de 30 días. ¿Qué tipo de usuario es y qué parte de la información le sirve?", ["La proveedora no trabaja en la empresa, es una usuaria externa.", "Le sirve saber cuánto dinero disponible (caja y banco) hay frente a lo que se debe a proveedores."], "Usuaria externa; mira dinero disponible y deudas con proveedores"),
    ],
    mistakes=[("Contar el capital como un pasivo porque «la empresa se lo debe a los dueños».", "El capital es patrimonio: lo que pertenece a los dueños, no una deuda con terceros que haya que pagar en una fecha.", "Clasifica: lo que se debe a otros es pasivo; lo aportado y acumulado por los dueños es patrimonio."),
              ("Entregar toda la información a cualquier persona que la pida por teléfono.", "La información de una empresa es confidencial y solo debe recibirla quien corresponde.", "Confirma con la jefatura quién puede recibirla y qué datos entregar.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es un activo?", "Un bien o derecho que la empresa tiene y que le sirve para operar", "Una deuda que la empresa debe pagar a otros", "Lo que pertenece a los dueños de la empresa", "El activo es lo que la empresa posee; la deuda es pasivo y lo de los dueños es patrimonio."),
        ("abc", "¿Cuál es un usuario externo de la información contable?", "Un banco que evalúa entregar un préstamo", "El encargado de bodega de la propia empresa", "El equipo de ventas de la propia empresa", "El banco no trabaja en la empresa, por eso es externo; bodega y ventas son usuarios internos."),
        ("ab", "¿Cuál es la ecuación patrimonial?", "Activo = pasivo + patrimonio", "Activo = pasivo − patrimonio", "La ecuación patrimonial suma lo que se debe y lo que es de los dueños para igualar el activo."),
        ("=", "{F} ¿Cuántos pesos suman los activos (caja, banco y mercaderías)?", "200000+800000+1500000", "Se suman las tres cuentas que son bienes de la empresa.", " pesos"),
        ("abc", "{F} ¿Qué cuenta de la ficha es un pasivo?", "Deudas con proveedores", "Mercaderías", "Capital", "Lo que se debe a proveedores es una obligación con otros; mercaderías es activo y capital es patrimonio."),
        ("abc", "{F} ¿Por qué el banco pide información contable?", "Para evaluar si la empresa podrá devolver un préstamo", "Para decidir los horarios de atención al público", "Para elegir los productos de las vitrinas", "El banco usa la información para medir la capacidad de pago antes de prestar."),
        ("=", "{F} Comprueba la ecuación: ¿cuántos pesos suman el pasivo (deudas con proveedores) y el patrimonio (capital)?", "600000+1900000", "El resultado debe coincidir con el total del activo.", " pesos"),
        ("=", "Una empresa de ejemplo tiene activos por $700.000 y pasivos por $250.000. ¿Cuál es su patrimonio?", "700000-250000", "El patrimonio es el activo menos el pasivo.", " pesos"),
        ("abc", "{F} ¿Qué dato compara la dueña con las deudas con proveedores para saber cuánto dinero disponible tiene ahora?", "Caja y banco", "Mercaderías", "Capital", "Solo caja y banco son dinero disponible; las mercaderías primero deben venderse."),
        ("abc", "Un empleado de la empresa le cuenta a un amigo, dueño de otra ferretería, cuánto debe su empresa a sus proveedores. ¿Qué característica de la información se rompe?", "La confidencialidad", "La oportunidad", "El respaldo documental", "Se entregó información reservada a alguien que no corresponde, es decir, se rompió la confidencialidad."),
        ("abc", "Una asistente anota la compra de un computador de uso personal de su jefe como gasto de la empresa. ¿Cuál es el riesgo?", "Mezclar gastos personales con los de la empresa y distorsionar la información", "Ninguno, porque el jefe es dueño de todo", "Que el banco no pueda ver la compra", "La empresa y su dueño son distintos para la contabilidad; mezclarlos deja cifras que no reflejan la realidad."),
        ("=", "{F} Si la dueña pagara con dinero disponible (caja y banco) toda la deuda con proveedores, ¿cuántos pesos quedarían en caja y banco juntos?", "200000+800000-600000", "Se suma el dinero disponible y se resta la deuda pagada.", " pesos"),
        ("ab", "{F} ¿Cumple la ficha la ecuación patrimonial?", "Sí: 2.500.000 de activo es igual a 600.000 de pasivo más 1.900.000 de patrimonio", "No: el activo es mayor que el capital", "El activo suma 2.500.000 y pasivo más patrimonio también suma 2.500.000, por lo tanto cuadra."),
    ],
    ctx=("abc", "La dueña pide a la asistente un informe para el banco. La asistente quiere agregar la lista de sueldos de cada trabajador con su nombre. ¿Qué corresponde?", "Entregar solo lo que el banco necesita y consultar a la dueña antes de compartir datos personales de trabajadores", "Entregarlo todo por si acaso al banco le sirve", "Decidir sola qué mandar y no avisar a nadie", "Los datos personales y la información reservada se comparten solo con autorización y con un fin claro."),
    sc=[
        ("En Contabilidad: ¿qué dice la ecuación patrimonial?", "Activo = pasivo + patrimonio", "Es la igualdad básica que sirve para comprobar que la información cuadra."),
        ("Nombra dos usuarios externos de la información contable.", "Por ejemplo, el banco y el Servicio de Impuestos Internos (también los proveedores)", "Son externos porque no trabajan dentro de la empresa que informa."),
        ("¿Qué haces antes de compartir información de la empresa con alguien?", "Confirmo con la jefatura quién puede recibirla y qué datos corresponde entregar", "La información contable es reservada y solo la recibe quien corresponde."),
    ],
    op=("Una panadería de ejemplo tiene al cierre del mes: Caja $150.000; Banco $450.000; Existencias $300.000; Deuda a proveedores $200.000; Capital $700.000. Calcula el total del activo, el pasivo y el patrimonio, comprueba la ecuación y escribe tres líneas para la dueña: qué usuario podría pedir esta información y qué datos no compartirías sin autorización.",
        "Activo: 150.000 + 450.000 + 300.000 = 900.000. Pasivo: 200.000. Patrimonio: 700.000. Comprobación: 200.000 + 700.000 = 900.000, cuadra. Nota: el banco podría pedirla para evaluar un préstamo; no compartiría la lista de sueldos ni datos personales sin autorización de la dueña.",
        ["calcula bien activo, pasivo y patrimonio", "comprueba la ecuación patrimonial", "nombra un usuario y un dato reservado"],
        ["hoja con los cálculos y la nota de tres líneas"],
        ["clasificar el capital como pasivo", "no comprobar que los totales cuadran", "compartir datos personales"],
        "Pregunta: «¿cómo sabes que tus cifras cuadran y a quién entregarías el informe?». Si no puede responder, pídele que repita la comprobación."),
    reinforce="Escribe tres cuentas de una tienda de tu barrio (inventadas) y clasifícalas en activo, pasivo o patrimonio.",
    extend="Explica con un ejemplo inventado por qué dos usuarios distintos pueden necesitar datos distintos de la misma empresa.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (hechos del mes de ejemplo, inventados). «Librería El Pehuén SpA»: (1) compra de cuadernos a un proveedor, con factura; "
     "(2) venta a una clienta que paga con boleta; (3) pago del arriendo del local; (4) entrega de cuadernos a un colegio, con guía de despacho. "
     "Roles: la dueña decide; el contador prepara y revisa los registros; la auxiliar contable registra y archiva documentos; el bodeguero recibe y entrega mercaderías.")
build(
    O1, 2, F,
    use="Aprenderé los conceptos básicos (hecho económico, ingreso, gasto), los documentos que los respaldan y los roles de quienes trabajan con ellos.",
    prior=["Sé la ecuación patrimonial.", "Sé qué es una factura de compra o de venta.", "Sé que cada persona de una empresa cumple un rol."],
    explain=[
        "Un hecho económico es un suceso que se puede medir en dinero y cambia los activos, los pasivos o el patrimonio de la empresa: una compra, una venta, un pago. Un ingreso es lo que la empresa gana por vender; un gasto es un consumo necesario para operar, como el arriendo o la luz. Las mercaderías compradas para vender se registran como activo hasta que se venden.",
        "Cada hecho se respalda con un documento. La factura respalda una venta entre empresas y detalla el producto, el monto neto y el impuesto. La boleta respalda la venta a una persona consumidora final. La guía de despacho respalda el traslado de mercaderías. La nota de crédito corrige o anula total o parcialmente un documento anterior, por ejemplo por una devolución. Los requisitos exactos de cada documento los fija la norma vigente.",
        "Los roles dividen el trabajo: la dueña decide, el contador prepara y revisa los registros y responde por su calidad, la auxiliar contable registra y archiva, y bodega controla lo físico. Si lo que llega a bodega no coincide con el documento, se avisa antes de registrar; nadie corrige un documento por su cuenta.",
    ],
    vocab=[("hecho económico", "suceso medible en dinero que cambia activos, pasivos o patrimonio"), ("ingreso", "lo que la empresa gana por sus ventas"), ("gasto", "consumo necesario para operar"), ("factura", "documento de venta entre empresas con detalle e impuesto"), ("boleta", "documento de venta a la persona consumidora final"), ("guía de despacho", "documento que respalda el traslado de mercaderías"), ("nota de crédito", "documento que corrige o anula parte de otro")],
    worked=[
        ("Clasificar un hecho", "Una empresa de ejemplo paga la cuenta de luz de su oficina. ¿Es ingreso o gasto?", ["La luz es un consumo necesario para operar.", "No es una venta ni un bien para vender: es un gasto."], "Gasto"),
        ("Elegir el documento", "Una empresa de ejemplo envía mercaderías a su otra sucursal sin venderlas. ¿Qué documento respalda el traslado?", ["Hay traslado de mercaderías, pero no hay venta.", "El documento que respalda el traslado es la guía de despacho."], "Guía de despacho"),
    ],
    mistakes=[("Registrar como gasto la compra de mercaderías que se van a vender.", "Las mercaderías para vender son un activo hasta que se venden; el gasto es el consumo para operar.", "Pregunta si se consume para operar (gasto) o se guarda para vender (activo)."),
              ("Corregir a mano el monto de una factura recibida.", "Un documento no se altera: solo quien lo emitió puede corregirlo con otro documento, como una nota de crédito.", "Avisa al contador y pide la corrección formal al emisor.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es un hecho económico?", "Un suceso medible en dinero que cambia activos, pasivos o patrimonio", "Cualquier cosa que ocurra en la oficina durante el día", "Un documento que se guarda en una carpeta", "Para ser hecho económico debe poder medirse en dinero y cambiar la situación de la empresa."),
        ("abc", "¿Qué documento respalda la venta a una persona consumidora final?", "La boleta", "La guía de despacho", "La nota de crédito", "La boleta se emite al consumidor final; la guía respalda traslados y la nota corrige otro documento."),
        ("abc", "¿Quién registra y archiva los documentos en el área contable?", "La auxiliar contable", "El bodeguero", "El cliente", "La auxiliar contable tiene a cargo el registro y el archivo; el bodeguero controla lo físico."),
        ("abc", "{F} ¿Qué documento respalda el hecho (4), la entrega de cuadernos al colegio?", "La guía de despacho", "La boleta", "La nota de crédito", "La entrega física se respalda con guía de despacho; la boleta es venta a consumidor final."),
        ("abc", "{F} ¿Cómo se clasifica el hecho (3), el pago del arriendo del local?", "Gasto", "Ingreso", "Activo", "El arriendo es un consumo para operar, por lo tanto es un gasto."),
        ("abc", "¿Qué diferencia hay entre ingreso y gasto?", "El ingreso es lo que se gana por vender; el gasto es un consumo para operar", "El ingreso es lo que se paga; el gasto es lo que se cobra", "Ambos son lo mismo y solo cambia el nombre", "Ingreso y gasto tienen sentido opuesto: uno viene de vender y el otro de consumir para operar."),
        ("abc", "Un colegio de ejemplo devuelve 10 cuadernos que se facturaron por error. ¿Qué documento anula parte de la factura?", "La nota de crédito", "La guía de despacho", "La boleta", "Se corrige un documento ya emitido con una nota de crédito."),
        ("abc", "{F} ¿Quién prepara y revisa los registros y responde por su calidad?", "El contador", "El bodeguero", "El colegio cliente", "El contador es quien prepara y revisa; bodega solo controla lo físico."),
        ("=", "La librería de ejemplo vende 40 cuadernos a $1.500 cada uno. ¿Cuántos pesos son los ingresos por esta venta (sin considerar impuestos)?", "40*1500", "El ingreso se calcula con cantidad por precio.", " pesos"),
        ("abc", "Un bodeguero de ejemplo recibe 50 cajas, pero la factura dice 55. ¿Qué corresponde?", "Avisar a la jefatura o al contador la diferencia antes de registrar", "Registrar 55 porque la factura siempre manda", "Registrar 50 y no avisar a nadie", "Si lo físico no coincide con el documento se avisa; no se registra como si estuviera bien."),
        ("abc", "Un compañero dice: «comprar mercaderías para vender es un gasto, igual que el arriendo». ¿Qué respondes?", "Las mercaderías para vender son un activo hasta que se venden; el arriendo es un gasto", "Tiene razón: toda compra es un gasto", "Ambas son ingresos porque mueven dinero", "Las mercaderías se guardan para vender, por eso son activo; el arriendo se consume al operar."),
        ("=", "La librería compra 6 cajas de lápices a $8.000 cada una y vende 4 de ellas. ¿Cuántos pesos, a precio de compra, quedan en mercaderías por las cajas no vendidas?", "(6-4)*8000", "Quedan las cajas no vendidas valoradas a su precio de compra.", " pesos"),
        ("ab", "{F} ¿Cuál de estos hechos genera un ingreso para la librería?", "El hecho (2), la venta a la clienta con boleta", "El hecho (1), la compra de cuadernos al proveedor", "La venta es lo que produce ingresos; la compra al proveedor es una salida de dinero."),
    ],
    ctx=("abc", "La auxiliar contable de una empresa de ejemplo recibe una factura sin fecha y con un importe tapado con corrector. ¿Qué hace?", "No la registra todavía, avisa al contador y pide una copia correcta al proveedor", "La registra con la fecha de hoy y el importe que le parezca", "La rompe y no dice nada", "Un documento incompleto o alterado no sirve de respaldo; se resuelve con el emisor."),
    sc=[
        ("En Contabilidad: ¿para qué sirve una nota de crédito?", "Para corregir o anular total o parcialmente un documento anterior", "Se usa, por ejemplo, ante una devolución de mercaderías ya facturadas."),
        ("¿La compra de mercaderías para vender es gasto o activo?", "Activo, hasta que se vendan", "Las mercaderías se guardan para vender y no se consumen al operar."),
        ("¿Qué haces si lo recibido no coincide con el documento?", "Aviso a la jefatura o al contador antes de registrar", "No se debe registrar algo que no se ha revisado ni respaldado."),
    ],
    op=("Una papelería de ejemplo tuvo estos hechos: (a) compró resmas de papel con factura; (b) vendió lápices a una persona con boleta; (c) pagó la cuenta del agua; (d) envió cajas a otra sucursal con guía de despacho. Para cada uno escribe si es ingreso, gasto, compra de mercaderías o traslado, y qué documento lo respalda; luego nombra quién del equipo lo registraría.",
        "(a) compra de mercaderías (activo), respaldada por la factura; (b) ingreso, respaldado por la boleta; (c) gasto, respaldado por el documento de la empresa que presta el servicio; (d) traslado, respaldado por la guía de despacho. Los cuatro los registra la auxiliar contable y los revisa el contador.",
        ["clasifica correctamente los cuatro hechos", "asocia cada hecho con su documento", "nombra a quien registra y a quien revisa"],
        ["tabla de cuatro filas con hecho, clasificación y documento"],
        ["llamar gasto a la compra de mercaderías", "usar boleta para un traslado", "no nombrar el rol que revisa"],
        "Pregunta: «¿por qué el hecho (d) no es una venta?». Si no distingue traslado de venta, repasa la guía de despacho."),
    reinforce="Revisa una boleta real de tu casa (sin copiar datos personales) y anota qué hecho económico respalda.",
    extend="Explica con un ejemplo inventado por qué una nota de crédito no se reemplaza escribiendo encima de la factura.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (informe al 31 de marzo de ejemplo, inventado) de «Distribuidora Costa Sur Ltda.». Activos corrientes (se convierten en dinero en menos de un año): "
     "Caja y banco $900.000; Clientes por cobrar $1.100.000; Mercaderías $2.000.000. Pasivos corrientes (se pagan en menos de un año): Proveedores $1.500.000; Impuestos por pagar $500.000. "
     "Activo no corriente: Camioneta $6.000.000.")
build(
    O1, 3, F,
    use="Aprenderé a leer un informe de situación simple y a sacar conclusiones sobre el dinero disponible y las deudas de corto plazo.",
    prior=["Sé la ecuación patrimonial.", "Sé qué son activos y pasivos.", "Sé sumar y dividir cifras exactas."],
    explain=[
        "Un informe de situación ordena las cuentas en corrientes y no corrientes. Los activos corrientes son los que se convertirán en dinero en menos de un año (caja, banco, clientes por cobrar, mercaderías). Los pasivos corrientes son las deudas que se pagan en menos de un año. Lo que dura más de un año es no corriente, como una camioneta o una deuda a cinco años.",
        "Dos lecturas sencillas ayudan a decidir. El capital de trabajo es activos corrientes menos pasivos corrientes y dice cuánto sobra de lo que se cobra y se vende después de pagar lo de corto plazo. La razón corriente es activos corrientes dividido por pasivos corrientes: si es mayor que 1, los activos corrientes cubren las deudas de corto plazo; si es menor que 1, no alcanzan.",
        "Al leer, se siguen cuatro pasos: identificar cada cuenta, sumar por grupo, calcular la medida y concluir con sus límites. El informe muestra una sola fecha y no dice si la empresa ganó o perdió en el mes, y las mercaderías primero deben venderse. Por eso la conclusión se redacta con cuidado y se respalda con los documentos.",
    ],
    vocab=[("activo corriente", "activo que se convierte en dinero en menos de un año"), ("pasivo corriente", "deuda que se paga en menos de un año"), ("no corriente", "que dura más de un año"), ("capital de trabajo", "activos corrientes menos pasivos corrientes"), ("razón corriente", "activos corrientes dividido por pasivos corrientes"), ("liquidez", "facilidad para pagar deudas con dinero disponible")],
    worked=[
        ("Calcular la razón corriente", "Una empresa de ejemplo tiene activos corrientes por $900.000 y pasivos corrientes por $300.000. ¿Cuál es su razón corriente y qué significa?", ["Razón corriente = 900.000 ÷ 300.000 = 3.", "Es mayor que 1: por cada $1 de deuda de corto plazo hay $3 de activos corrientes."], "3; cubre con holgura sus deudas de corto plazo"),
        ("Clasificar cuentas", "En una empresa de ejemplo: un terreno y una deuda que se pagará en 5 años. ¿Son corrientes o no corrientes?", ["El terreno no se convertirá en dinero en menos de un año.", "La deuda se paga en más de un año."], "Ambos son no corrientes"),
    ],
    mistakes=[("Incluir la camioneta entre los activos corrientes porque «vale mucho».", "La camioneta se usa para operar y no se convertirá en dinero en menos de un año: es no corriente.", "Clasifica por el plazo en que la cuenta se convierte en dinero o se paga."),
              ("Concluir que una empresa «ganó» porque su informe de situación tiene un patrimonio alto.", "El informe de situación muestra una fecha; lo ganado en el período se ve en el resultado.", "Usa cada informe solo para lo que muestra y declara sus límites.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es un activo corriente?", "Un activo que se convertirá en dinero en menos de un año", "Un activo que dura más de cinco años", "Una deuda que se paga pronto", "El criterio es el plazo de conversión en dinero: menos de un año."),
        ("abc", "En Contabilidad: ¿qué es un pasivo corriente?", "Una deuda que se paga en menos de un año", "Un bien que se vende en menos de un año", "Una deuda que se paga en diez años", "El pasivo es deuda y es corriente cuando su pago es de corto plazo."),
        ("ab", "¿Cómo se calcula la razón corriente?", "Activos corrientes ÷ pasivos corrientes", "Pasivos corrientes ÷ activos corrientes", "La razón corriente compara lo que se convierte en dinero con lo que se debe pagar pronto."),
        ("=", "{F} ¿Cuántos pesos suman los activos corrientes?", "900000+1100000+2000000", "Se suman solo las cuentas que se convierten en dinero en menos de un año.", " pesos"),
        ("abc", "{F} ¿Qué cuentas forman los pasivos corrientes?", "Proveedores e impuestos por pagar", "Clientes e impuestos por pagar", "Proveedores y camioneta", "Los pasivos corrientes son deudas de corto plazo; clientes y camioneta son activos."),
        ("abc", "{F} ¿Cuál cuenta es un activo no corriente?", "La camioneta", "Clientes por cobrar", "Caja y banco", "La camioneta se usa para operar durante años y no se convierte pronto en dinero."),
        ("=", "{F} ¿Cuál es el capital de trabajo (activos corrientes menos pasivos corrientes)?", "(900000+1100000+2000000)-(1500000+500000)", "Se restan las deudas de corto plazo a los activos de corto plazo.", " pesos"),
        ("=", "{F} ¿Cuántas veces cubren los activos corrientes a los pasivos corrientes (razón corriente)?", "(900000+1100000+2000000)//(1500000+500000)", "Se divide el total de activos corrientes por el de pasivos corrientes.", " veces"),
        ("=", "{F} Con todos los activos y todos los pasivos de la ficha, ¿cuál es el patrimonio?", "(900000+1100000+2000000+6000000)-(1500000+500000)", "El patrimonio es el total del activo menos el total del pasivo.", " pesos"),
        ("abc", "{F} Una persona concluye: «la empresa ganó $8.000.000 en marzo porque su patrimonio es $8.000.000». ¿Qué error comete?", "Confunde el patrimonio de una fecha con el resultado ganado en el período", "Suma mal los activos corrientes", "Olvida contar la camioneta como activo", "El patrimonio no mide lo ganado en el mes; eso se ve en el resultado del período."),
        ("abc", "Otra empresa de ejemplo tiene activos corrientes por $600.000 y pasivos corrientes por $1.200.000. ¿Qué se puede concluir de su liquidez?", "Sus activos corrientes cubren solo la mitad de sus deudas de corto plazo", "Cubre sus deudas con holgura", "No se puede decir nada porque no se conoce el capital", "600.000 ÷ 1.200.000 es menor que 1: no alcanzan a cubrir las deudas de corto plazo."),
        ("abc", "{F} La dueña quiere pagar al contado mercaderías por $3.000.000 solo con dinero disponible. ¿Qué muestra la ficha?", "Caja y banco suman $900.000 y no alcanzan para pagar $3.000.000", "Alcanza, porque la camioneta vale $6.000.000", "Alcanza, porque la razón corriente es 2", "Solo caja y banco son dinero disponible inmediato; la camioneta y las mercaderías no son dinero."),
        ("=", "{F} Si la empresa cobra todos sus clientes y paga todos los proveedores y los impuestos, ¿cuántos pesos quedarían en caja y banco?", "900000+1100000-1500000-500000", "Se suma lo cobrado al dinero disponible y se resta lo pagado.", " pesos"),
    ],
    ctx=("abc", "El dueño de una empresa de ejemplo pide una conclusión rápida del informe: «¿vamos bien?». ¿Cuál respuesta es más responsable?", "«La razón corriente es 2: cubrimos lo de corto plazo; este informe no dice si ganamos en el mes»", "«Vamos perfecto, no hay nada más que revisar»", "«Vamos mal porque tenemos deudas»", "Una conclusión responsable usa la medida calculada y declara qué no muestra el informe."),
    sc=[
        ("En Contabilidad: ¿cuándo es mayor que 1 la razón corriente?", "Cuando los activos corrientes son mayores que los pasivos corrientes", "Eso significa que cubren las deudas de corto plazo con holgura."),
        ("¿Cómo se calcula el capital de trabajo?", "Activos corrientes menos pasivos corrientes", "Muestra lo que sobra de corto plazo después de pagar las deudas."),
        ("¿Qué no puede decir un informe de una sola fecha?", "Si la empresa ganó o perdió durante el período", "Para saber eso se necesita el resultado del período, no una sola fecha."),
    ],
    op=("Una empresa de ejemplo muestra: Caja y banco $400.000; Clientes $800.000; Mercaderías $1.200.000; Proveedores $1.000.000; Impuestos por pagar $400.000; Maquinaria (no corriente) $3.000.000. Calcula sus activos corrientes, sus pasivos corrientes, su capital de trabajo y su razón corriente, y escribe tres líneas de conclusión con un límite del informe.",
        "Activos corrientes: 400.000 + 800.000 + 1.200.000 = 2.400.000. Pasivos corrientes: 1.000.000 + 400.000 = 1.400.000. Capital de trabajo: 1.000.000. Razón corriente: 2.400.000 ÷ 1.400.000 es mayor que 1 (cubre sus deudas de corto plazo). Límite: el informe no dice si ganó en el período y las mercaderías aún deben venderse.",
        ["clasifica bien corrientes y no corrientes", "calcula capital de trabajo y razón corriente", "concluye con cuidado y declara un límite"],
        ["hoja con la tabla de cálculos y la conclusión"],
        ["incluir la maquinaria en los corrientes", "dividir al revés", "afirmar que la empresa ganó"],
        "Pregunta: «¿qué te dice la razón corriente y qué no te dice?». Si responde solo con la cifra, pídele una frase de conclusión."),
    reinforce="Inventa tres cuentas corrientes y dos no corrientes para una tienda y calcula su capital de trabajo.",
    extend="Explica por qué una empresa puede tener una buena razón corriente y aun así tener problemas para pagar mañana.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (comparación de dos meses de ejemplo, inventada) de «Distribuidora Costa Sur Ltda.». Enero: ventas $4.000.000; gastos $3.000.000. "
     "Febrero: ventas $4.800.000; gastos $3.900.000. Resultado del mes = ventas − gastos. Variación porcentual = (valor nuevo − valor anterior) × 100 ÷ valor anterior.")
build(
    O1, 4, F,
    use="Aprenderé a comparar información de dos períodos, calcular variaciones y tomar una decisión con criterio y límites.",
    prior=["Sé calcular el resultado de un período.", "Sé leer razones y capital de trabajo.", "Sé calcular un porcentaje con cifras exactas."],
    explain=[
        "Comparar dos períodos es la forma más simple de leer la marcha de la empresa. Se calcula el resultado de cada mes (ventas menos gastos) y la variación, que es el valor nuevo menos el valor anterior. La variación porcentual dice cuánto cambió respecto del valor inicial: (valor nuevo − valor anterior) × 100 ÷ valor anterior.",
        "Un criterio técnico no mira una sola cifra. Si las ventas suben pero los gastos suben más rápido, el resultado puede bajar aunque se venda más. Por eso se comparan las variaciones de ventas y de gastos y se busca el origen en los documentos y registros antes de decidir.",
        "Dos meses no forman una tendencia y la comparación no explica las causas: puede haber una compra grande o una venta fuera de lo normal. La decisión se escribe con la evidencia usada y con el límite de lo que se sabe, por ejemplo: «los gastos crecieron más que las ventas; revisar el detalle antes de recortar».",
    ],
    vocab=[("período", "tramo de tiempo que se informa, por ejemplo un mes"), ("resultado", "ventas menos gastos del período"), ("variación", "diferencia entre el valor nuevo y el anterior"), ("variación porcentual", "variación expresada como porcentaje del valor anterior"), ("tendencia", "dirección que siguen los datos en varios períodos")],
    worked=[
        ("Variación porcentual de ventas", "Una tienda de ejemplo vendió $500.000 en un mes y $600.000 al siguiente. ¿Cuál es la variación porcentual?", ["Variación = 600.000 − 500.000 = 100.000.", "100.000 × 100 ÷ 500.000 = 20."], "20 % de aumento"),
        ("Decidir con criterio", "Una tienda de ejemplo vendió más, pero su resultado bajó. Sus ventas subieron 10 % y sus gastos 25 %. ¿Qué conviene hacer?", ["Los gastos crecen más rápido que las ventas, por eso el resultado baja.", "Antes de recortar, se revisan en los documentos qué gastos aumentaron."], "Revisar el detalle de los gastos que más subieron"),
    ],
    mistakes=[("Celebrar solo porque las ventas subieron.", "Si los gastos suben más, el resultado puede bajar.", "Compara siempre ventas, gastos y resultado."),
              ("Calcular el porcentaje dividiendo por el valor nuevo.", "La variación porcentual se mide sobre el valor anterior.", "Divide la variación por el valor del período anterior.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es la variación?", "La diferencia entre el valor nuevo y el valor anterior", "La suma de dos meses", "El promedio de ventas y gastos", "La variación compara el valor nuevo con el anterior restando."),
        ("abc", "¿Cómo se calcula el resultado de un mes?", "Ventas menos gastos", "Ventas más gastos", "Gastos menos activos", "El resultado mide cuánto quedó después de restar los gastos a las ventas."),
        ("ab", "¿Sobre qué valor se calcula la variación porcentual?", "Sobre el valor anterior", "Sobre el valor nuevo", "La variación porcentual dice cuánto cambió respecto de donde se partió."),
        ("=", "{F} ¿Cuántos pesos fue el resultado de enero?", "4000000-3000000", "El resultado es ventas menos gastos.", " pesos"),
        ("=", "{F} ¿Cuántos pesos fue el resultado de febrero?", "4800000-3900000", "El resultado es ventas menos gastos del mes de febrero.", " pesos"),
        ("=", "{F} ¿Cuántos pesos subieron las ventas de enero a febrero?", "4800000-4000000", "La variación es el valor nuevo menos el anterior.", " pesos"),
        ("=", "{F} ¿En qué porcentaje subieron las ventas de enero a febrero?", "(4800000-4000000)*100//4000000", "Se divide la variación por el valor anterior y se multiplica por 100.", " %"),
        ("=", "{F} ¿En qué porcentaje subieron los gastos de enero a febrero?", "(3900000-3000000)*100//3000000", "Se divide la variación de gastos por los gastos de enero.", " %"),
        ("abc", "{F} ¿Qué lectura describe mejor los datos?", "Las ventas subieron 20 % y los gastos 30 %: los gastos crecieron más y el resultado bajó", "Las ventas subieron más que los gastos y el resultado mejoró", "Todo subió igual, así que no cambió nada", "Con los porcentajes calculados, los gastos crecieron más, por eso el resultado bajó de 1.000.000 a 900.000."),
        ("abc", "{F} El dueño propone despedir a una persona del equipo de ventas «para bajar los gastos». ¿Qué respondes con criterio técnico?", "Antes se revisa en los documentos qué gastos subieron; dos meses no bastan para decidir", "Hacerlo ya, porque los gastos subieron", "No revisar nada porque las ventas subieron", "Una decisión con consecuencias se apoya en el detalle de los gastos y no en dos cifras."),
        ("abc", "{F} Otro estudiante dice: «las ventas subieron $800.000 y el resultado también subió $800.000». ¿Qué error comete?", "Olvida que los gastos también subieron y el resultado cambió distinto", "Suma mal las ventas", "Confunde enero con marzo", "El resultado pasó de 1.000.000 a 900.000; no subió, porque los gastos aumentaron más que las ventas."),
        ("=", "{F} Si en marzo los gastos subieran $300.000 respecto de febrero y las ventas se mantuvieran, ¿cuánto sería el resultado de marzo?", "4800000-(3900000+300000)", "Los gastos de marzo serían los de febrero más 300.000.", " pesos"),
        ("abc", "{F} ¿Qué límite debe declarar quien presenta esta comparación?", "Solo hay dos meses y no se conocen las causas del aumento de gastos", "Ninguno, porque las cifras son exactas", "Que enero fue un mes peor", "Una comparación de dos meses no prueba una tendencia ni explica por qué cambiaron los gastos."),
    ],
    ctx=("abc", "La contadora de una empresa de ejemplo presenta a la dueña: ventas +20 %, gastos +30 %. La dueña pregunta si hay que preocuparse. ¿Qué respuesta es más responsable?", "«Los gastos crecen más rápido; revisemos el detalle en los documentos antes de decidir»", "«No hay nada que revisar»", "«Hay que cerrar la empresa»", "La respuesta usa el dato, propone verificar y evita conclusiones apresuradas."),
    sc=[
        ("En Contabilidad: ¿cómo se calcula una variación porcentual?", "(valor nuevo − valor anterior) × 100 ÷ valor anterior", "Mide el cambio respecto del valor inicial, expresado como porcentaje."),
        ("¿Por qué no basta mirar solo las ventas?", "Porque los gastos pueden subir más y bajar el resultado", "El resultado depende de las ventas y también de los gastos del período."),
        ("¿Qué límite tiene comparar dos meses?", "No muestra una tendencia ni explica las causas", "Se necesitan más períodos y revisar los documentos que respaldan las cifras."),
    ],
    op=("Una tienda de ejemplo tuvo en abril ventas por $2.000.000 y gastos por $1.500.000, y en mayo ventas por $2.400.000 y gastos por $2.100.000. Calcula el resultado de cada mes y la variación porcentual de ventas y de gastos, y escribe una recomendación de tres líneas con un límite.",
        "Resultado de abril: 500.000; de mayo: 300.000. Ventas: 400.000 × 100 ÷ 2.000.000 = 20 %. Gastos: 600.000 × 100 ÷ 1.500.000 = 40 %. Recomendación: los gastos crecieron más que las ventas; revisar en los documentos cuáles subieron antes de recortar. Límite: solo hay dos meses.",
        ["calcula resultados y variaciones", "interpreta que los gastos subieron más", "propone verificar y declara un límite"],
        ["hoja con los cálculos y la recomendación"],
        ["dividir por el valor nuevo", "decidir sin revisar documentos", "no declarar límites"],
        "Pregunta: «¿qué revisarías antes de recortar?». Si no nombra los documentos o registros, pídele que lo agregue."),
    reinforce="Inventa las ventas de dos meses de un negocio y calcula la variación porcentual si ambas cifras son múltiplos de 100.000.",
    extend="Explica por qué una variación porcentual alta en una cifra muy pequeña puede no ser importante.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (ciclo contable de ejemplo, inventado). Pasos: 1) revisar el documento de respaldo; 2) hacer el asiento en el libro diario; 3) traspasar al libro mayor; "
     "4) preparar el balance de comprobación; 5) preparar los estados financieros. Caso de «Taller Rayén» (empresa de ejemplo): factura N.º 101 (número de ejemplo) por $60.000, "
     "emitida el 28 de mayo por compra de insumos a crédito, que se pagará el 10 de junio.")
build(
    O2, 1, F,
    use="Aprenderé el ciclo que convierte un documento en información contable y los riesgos de cada paso.",
    prior=["Sé qué hechos económicos tiene una empresa.", "Sé qué es una factura.", "Sé la ecuación patrimonial."],
    explain=[
        "Procesar información contable es transformar documentos en información ordenada. El ciclo tiene cinco pasos: revisar el documento de respaldo, hacer el asiento en el libro diario (anotación por fecha de cada hecho), traspasar al libro mayor (que agrupa los movimientos por cuenta), preparar el balance de comprobación (que verifica que todo cuadra) y preparar los estados financieros.",
        "Un hecho se registra en el período en que ocurre, aunque se pague después. Una compra a crédito hecha el 28 de mayo pertenece a mayo aunque se pague en junio. El registro siempre parte de un documento: sin respaldo, el hecho no se puede probar ante la jefatura ni ante la autoridad tributaria.",
        "Los riesgos del ciclo son registrar sin documento, registrar dos veces el mismo documento, anotar una fecha o una cuenta equivocadas y mezclar períodos. Se previenen revisando el número del documento, su fecha y su monto antes de registrar, y guardando el respaldo ordenado.",
    ],
    vocab=[("ciclo contable", "serie de pasos que convierte documentos en estados financieros"), ("libro diario", "libro donde se anotan los asientos en orden de fecha"), ("libro mayor", "libro que agrupa los movimientos de cada cuenta"), ("asiento", "anotación de un hecho económico en debe y haber"), ("balance de comprobación", "lista de saldos que verifica que el debe y el haber cuadran"), ("período", "tramo de tiempo informado, por ejemplo un mes")],
    worked=[
        ("Ordenar el ciclo", "Ordena estos pasos: (a) preparar el balance de comprobación; (b) revisar el documento; (c) hacer el asiento en el diario; (d) traspasar al mayor.", ["El ciclo parte siempre por el documento: (b).", "Sigue el diario (c), luego el mayor (d) y recién después el balance (a)."], "b, c, d, a"),
        ("Elegir el período", "Una empresa de ejemplo vende el 30 de abril y le pagan el 5 de mayo. ¿En qué mes se registra la venta?", ["El hecho (la venta) ocurrió el 30 de abril.", "Se registra en el período en que ocurre, aunque se cobre después."], "En abril"),
    ],
    mistakes=[("Esperar a que se pague una factura para registrarla.", "El hecho ocurrió antes y el período queda con cifras incompletas.", "Registra en el período en que ocurrió el hecho, con su documento."),
              ("Registrar con un papel anotado a mano, sin documento.", "Sin respaldo no se puede probar ni revisar el hecho.", "Pide el documento y no registres hasta tenerlo.")],
    T=[
        ("abc", "¿Cuál es el primer paso del ciclo contable?", "Revisar el documento de respaldo", "Preparar el balance de comprobación", "Traspasar al libro mayor", "El ciclo parte del documento; sin él no hay nada que registrar."),
        ("abc", "¿En qué libro se anotan los asientos en orden de fecha?", "En el libro diario", "En el libro mayor", "En el balance de comprobación", "El diario es cronológico; el mayor ordena por cuenta."),
        ("ab", "¿Qué libro agrupa los movimientos por cuenta?", "El libro mayor", "El libro diario", "El mayor reúne todos los movimientos de cada cuenta para saber su saldo."),
        ("abc", "{F} ¿En qué mes se registra la compra de la factura N.º 101?", "En mayo, porque el hecho ocurrió el 28 de mayo", "En junio, porque se paga el 10 de junio", "En el mes en que se archive la factura", "Se registra en el período en que ocurre el hecho, aunque se pague después."),
        ("=", "{F} ¿Cuántos días pasan entre la emisión (28 de mayo) y el pago (10 de junio)? Mayo tiene 31 días.", "(31-28)+10", "Se cuentan los días que faltan para terminar mayo y los 10 de junio.", " días"),
        ("abc", "{F} Una auxiliar espera hasta el 10 de junio para registrar la factura. ¿Qué problema produce?", "Las cifras de mayo quedan incompletas, porque el hecho ocurrió en mayo", "Ninguno, porque lo que importa es cuándo se paga", "Se duplican las cifras de junio", "Registrar tarde deja el período en que ocurrió el hecho con información incompleta."),
        ("abc", "Una compañera propone registrar una compra con un papel anotado a mano, sin factura ni boleta. ¿Qué corresponde?", "Pedir el documento de respaldo antes de registrar", "Registrarla igual y buscar el documento en un año", "Registrarla por un monto aproximado", "El registro debe estar respaldado por un documento revisable."),
        ("=", "{F} Si el taller tiene $200.000 en caja y paga la factura completa el 10 de junio, ¿cuántos pesos le quedan en caja?", "200000-60000", "Se resta de la caja el monto pagado de la factura.", " pesos"),
        ("abc", "{F} ¿Qué dato de la ficha sirve para comprobar que la misma factura no se registró dos veces?", "El número de la factura", "El día de pago", "El nombre del taller", "El número identifica un documento; el día o el nombre pueden repetirse."),
        ("abc", "¿Por qué el ciclo contable parte siempre por un documento?", "Porque sin respaldo el hecho no se puede probar ni revisar", "Porque es más rápido de archivar que de anotar", "Porque el libro diario no admite otro dato", "El documento prueba el hecho; sin él la información contable pierde valor."),
        ("abc", "Dos auxiliares registran por error la misma factura. ¿Qué efecto tiene?", "El gasto o la deuda quedan inflados", "No pasa nada porque el total es el mismo", "La deuda baja a la mitad", "Registrar dos veces el mismo documento duplica la cifra y distorsiona la información."),
        ("=", "{F} Si la factura se registrara dos veces por error, ¿cuántos pesos de deuda quedarían registrados de más?", "60000*2-60000", "Se compara lo registrado dos veces con lo que realmente se debe.", " pesos"),
        ("abc", "{F} Al cierre de mayo, el jefe pide dejar la factura sin registrar «para que el mes se vea mejor». ¿Qué corresponde?", "Registrarla en mayo y avisar al contador de la petición", "Dejarla sin registrar para evitar problemas", "Registrarla en junio sin avisar a nadie", "Las cifras deben reflejar los hechos del período; no se ocultan para mejorar un resultado."),
    ],
    ctx=("abc", "Faltan dos días para el cierre y llega una factura con fecha de la semana próxima. ¿Qué haces?", "No la registro en este cierre y consulto al contador por la fecha del documento", "La registro con la fecha de hoy para ordenar el mes", "La rompo para no tener problemas", "Se registran los hechos que ya ocurrieron; una fecha futura se consulta antes."),
    sc=[
        ("En Contabilidad: ¿qué libro agrupa los movimientos por cuenta?", "El libro mayor", "El mayor reúne los movimientos de cada cuenta."),
        ("¿En qué período se registra un hecho que se paga después?", "En el período en que ocurre el hecho", "El pago posterior no cambia el período del hecho."),
        ("Nombra un riesgo al registrar documentos.", "Registrar sin documento o registrar dos veces el mismo documento", "Ambos errores distorsionan las cifras de la empresa."),
    ],
    op=("Ordena el ciclo para este caso de ejemplo: una librería recibe la factura N.º 305 (número de ejemplo) por $90.000 el 29 de junio y la paga el 8 de julio. Escribe los cinco pasos del ciclo con una frase sobre qué harías en cada uno, en qué mes se registra y dos controles para no registrarla dos veces.",
        "1) Reviso que la factura tenga fecha, número y monto. 2) Hago el asiento en el diario. 3) Lo traspaso al mayor. 4) Preparo el balance de comprobación. 5) Preparo los estados. Se registra en junio. Controles: revisar el número 305 contra las facturas ya registradas y archivar la factura marcada como registrada.",
        ["ordena los cinco pasos", "indica el mes correcto", "propone dos controles contra duplicados"],
        ["hoja con los cinco pasos, el mes y los controles"],
        ["registrar en julio", "omitir el balance de comprobación", "no revisar el número del documento"],
        "Pregunta: «¿cómo sabes que no la registraste antes?». Si no nombra un control concreto, pídele que lo escriba."),
    reinforce="Ordena en tu cuaderno los cinco pasos del ciclo con tus propias palabras.",
    extend="Explica con un ejemplo inventado qué problema produce mezclar hechos de dos meses en un solo período.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (plan de cuentas de ejemplo, inventado). Activo: Caja, Banco, Clientes, Mercaderías, IVA Crédito Fiscal. Pasivo: Proveedores, IVA Débito Fiscal. Patrimonio: Capital. "
     "Ingreso: Ventas. Gasto: Arriendo, Luz. Reglas: el debe aumenta activos y gastos; el haber aumenta pasivos, patrimonio e ingresos. En todo asiento, total debe = total haber.")
build(
    O2, 2, F,
    use="Aprenderé qué es una cuenta, cómo se usan el debe y el haber y cómo se escribe un asiento sencillo.",
    prior=["Sé la ecuación patrimonial.", "Sé qué es ingreso y gasto.", "Sé sumar y comparar totales."],
    explain=[
        "Una cuenta es un registro con un nombre (Caja, Ventas, Proveedores) donde se anotan los aumentos y las disminuciones de un tipo de hecho. Todas las cuentas de una empresa forman su plan de cuentas. Cada cuenta tiene dos lados: el debe (izquierda) y el haber (derecha). Anotar en el debe o en el haber no significa «bueno» o «malo»: es un lado de la cuenta.",
        "La partida doble dice que todo hecho afecta al menos a dos cuentas y que el total anotado al debe es igual al anotado al haber. Las reglas son: el debe aumenta activos y gastos; el haber aumenta pasivos, patrimonio e ingresos; lo contrario los disminuye. Cuando el debe de una cuenta es mayor que su haber, su saldo es deudor; en el caso contrario, es acreedor.",
        "Un asiento se escribe con la fecha, las cuentas con sus montos en debe y haber y una glosa (frase corta que explica el hecho). Por ejemplo, una compra de mercaderías al contado carga Mercaderías al debe y abona Caja al haber. Si el debe y el haber no coinciden, el asiento tiene un error y no se acepta. Las cuentas IVA Crédito Fiscal (activo: IVA pagado en compras) e IVA Débito Fiscal (pasivo: IVA cobrado en ventas) aparecen en el plan de cuentas y se estudian en la clase siguiente.",
    ],
    vocab=[("cuenta", "registro con nombre donde se anotan aumentos y disminuciones"), ("debe", "lado izquierdo de la cuenta"), ("haber", "lado derecho de la cuenta"), ("partida doble", "todo hecho afecta dos cuentas y debe = haber"), ("saldo", "diferencia entre el debe y el haber de una cuenta"), ("glosa", "frase corta que explica un asiento"), ("plan de cuentas", "lista ordenada de las cuentas de la empresa")],
    worked=[
        ("Pago de arriendo por transferencia", "Una empresa de ejemplo paga $100.000 de arriendo desde su cuenta bancaria. ¿Cuál es el asiento?", ["El arriendo es un gasto: aumenta por el debe.", "El banco es activo y disminuye: va al haber."], "Debe Arriendo 100.000; Haber Banco 100.000"),
        ("Compra a crédito sin IVA", "Una empresa de ejemplo compra mercaderías a crédito por $40.000 (sin considerar IVA). ¿Cuál es el asiento?", ["Mercaderías es un activo que aumenta: va al debe.", "La deuda con el proveedor es un pasivo que aumenta: va al haber."], "Debe Mercaderías 40.000; Haber Proveedores 40.000"),
    ],
    mistakes=[("Anotar un aumento de caja en el haber porque «sale plata».", "Caja es activo y el activo aumenta por el debe; el haber la disminuye.", "Pregunta qué cuenta sube o baja y recuerda la regla de su grupo."),
              ("Aceptar un asiento con debe y haber distintos.", "La partida doble exige que ambos totales coincidan.", "Suma ambos lados antes de dar por terminado el asiento.")],
    T=[
        ("abc", "En Contabilidad: ¿en qué lado de la cuenta se anota el aumento de un activo?", "En el debe", "En el haber", "En el saldo", "Los activos aumentan por el debe y disminuyen por el haber."),
        ("abc", "¿En qué lado se anota el aumento de un ingreso?", "En el haber", "En el debe", "En el saldo", "Los ingresos, los pasivos y el patrimonio aumentan por el haber."),
        ("ab", "¿Qué dice la partida doble?", "Todo hecho afecta al menos dos cuentas y el debe es igual al haber", "Cada hecho se anota en una sola cuenta", "La partida doble exige igualdad entre el total del debe y el del haber."),
        ("abc", "{F} ¿A qué grupo pertenece la cuenta Proveedores?", "Pasivo", "Activo", "Gasto", "Proveedores es una deuda con otros, por lo tanto es pasivo."),
        ("abc", "{F} La cuenta Arriendo aumenta cuando se anota en...", "El debe, porque es un gasto", "El haber, porque es un pasivo", "El haber, porque es un ingreso", "Los gastos aumentan por el debe."),
        ("abc", "{F} La cuenta Capital aumenta cuando se anota en...", "El haber, porque es patrimonio", "El debe, porque es un activo", "El debe, porque es un gasto", "El patrimonio aumenta por el haber."),
        ("abc", "{F} Una empresa de ejemplo compra mercaderías al contado por $50.000 (sin IVA). ¿Cuál es el asiento?", "Debe Mercaderías 50.000; Haber Caja 50.000", "Debe Caja 50.000; Haber Mercaderías 50.000", "Debe Mercaderías 50.000; Haber Ventas 50.000", "Las mercaderías (activo) aumentan por el debe y la caja (activo) disminuye por el haber."),
        ("abc", "{F} Se paga la cuenta de luz en efectivo, por $30.000. ¿Cuál es el asiento?", "Debe Luz 30.000; Haber Caja 30.000", "Debe Caja 30.000; Haber Luz 30.000", "Debe Luz 30.000; Haber Ventas 30.000", "El gasto de luz aumenta por el debe y la caja disminuye por el haber."),
        ("=", "{F} En un asiento se carga al debe Mercaderías $150.000 e IVA Crédito Fiscal $15.000. ¿Cuántos pesos deben anotarse al haber en Caja para que el asiento cuadre?", "150000+15000", "El haber debe ser igual al total del debe.", " pesos"),
        ("abc", "Un asiento de ejemplo tiene $400.000 al debe y $380.000 al haber. ¿Qué indica?", "Que tiene un error y no se acepta hasta corregirlo", "Que está bien porque la diferencia es pequeña", "Que falta un documento en el banco", "La partida doble exige igualdad exacta; una diferencia, por pequeña que sea, es un error."),
        ("abc", "{F} Una venta a crédito sin IVA por $80.000 se registra con Clientes al debe. ¿Por qué no se anota Ventas al debe?", "Porque Clientes es un activo que aumenta y Ventas es un ingreso que aumenta por el haber", "Porque Ventas es un gasto", "Porque las ventas nunca se anotan en una cuenta", "El derecho de cobro (activo) sube por el debe y el ingreso sube por el haber."),
        ("=", "{F} Asiento de una venta sin IVA: Debe Banco $120.000 y Debe Clientes $80.000. ¿Cuántos pesos deben anotarse al haber en Ventas?", "120000+80000", "El haber de Ventas debe igualar la suma de los montos del debe.", " pesos"),
        ("abc", "{F} El dueño aporta $500.000 en efectivo a la empresa. ¿Cuál es el asiento?", "Debe Caja 500.000; Haber Capital 500.000", "Debe Capital 500.000; Haber Caja 500.000", "Debe Caja 500.000; Haber Ventas 500.000", "Entra dinero (caja sube por el debe) y aumenta el patrimonio (capital sube por el haber); no es una venta."),
    ],
    ctx=("abc", "Una auxiliar de ejemplo registra el pago de $60.000 de arriendo con Debe Caja y Haber Arriendo. El contador revisa. ¿Qué corrección corresponde?", "Invertir: Debe Arriendo 60.000 y Haber Caja 60.000", "Dejarlo porque el total cuadra", "Anotar el arriendo en Ventas", "El asiento cuadra, pero con las cuentas invertidas: el gasto va al debe y la caja disminuye por el haber."),
    sc=[
        ("En Contabilidad: ¿qué cuentas aumentan por el debe?", "Las de activos y gastos", "Esa es la regla del lado del debe."),
        ("¿Qué cuentas aumentan por el haber?", "Las de pasivos, patrimonio e ingresos", "Esa es la regla del lado del haber."),
        ("¿Cuándo un asiento no se acepta?", "Cuando el total del debe es distinto del total del haber", "La partida doble exige que ambos totales sean iguales."),
    ],
    op=("Escribe el asiento (cuentas, debe y haber) de estos tres hechos de una empresa de ejemplo, sin considerar IVA: (a) compra de mercaderías a crédito por $70.000; (b) venta al contado por $120.000; (c) pago del arriendo por $60.000 desde el banco. Comprueba que cada asiento cuadra y escribe una glosa.",
        "(a) Debe Mercaderías 70.000; Haber Proveedores 70.000. Glosa: compra a crédito. (b) Debe Caja 120.000; Haber Ventas 120.000. Glosa: venta al contado. (c) Debe Arriendo 60.000; Haber Banco 60.000. Glosa: pago de arriendo. Los tres cuadran porque debe = haber.",
        ["usa las cuentas correctas", "ubica cada una en debe o haber", "comprueba que debe = haber y escribe la glosa"],
        ["hoja con tres asientos y su comprobación"],
        ["invertir debe y haber", "no sumar los lados", "confundir compra con venta"],
        "Pregunta: «¿por qué esta cuenta va al debe?». Si no cita la regla de su grupo, repasa activos y gastos."),
    reinforce="Elige tres hechos de una tienda de barrio (inventados) y escribe su asiento con una calculadora para comprobar que cuadran.",
    extend="Explica con un ejemplo inventado por qué un asiento puede cuadrar y aun así estar mal hecho.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (operaciones de ejemplo de «Taller Rayén»; tasa de IVA de ejemplo: 10 %; la tasa real es la que fija la norma vigente). "
     "Op. 1: compra de mercaderías al contado, neto $150.000. Op. 2: venta a crédito, neto $400.000. Op. 3: pago de arriendo en efectivo, $90.000 (sin IVA, de ejemplo). "
     "Reglas: el IVA de las compras va en IVA Crédito Fiscal (debe); el IVA de las ventas va en IVA Débito Fiscal (haber); total con IVA = neto + IVA.")
build(
    O2, 3, F,
    use="Aprenderé a registrar en asientos una compra, una venta y un gasto con IVA de ejemplo.",
    prior=["Sé las reglas del debe y del haber.", "Sé calcular un porcentaje exacto.", "Sé qué es una factura."],
    explain=[
        "Cuando una empresa compra o vende, la factura incluye el monto neto (el valor del bien) y el IVA (impuesto al valor agregado). En este cuaderno se usa una tasa de ejemplo de 10 % para calcular; la tasa real y sus reglas las fija la norma vigente. El total de la factura es neto más IVA.",
        "El IVA se registra aparte. En una compra, el IVA se anota en la cuenta IVA Crédito Fiscal, que es un activo y por eso va al debe. En una venta, el IVA se anota en IVA Débito Fiscal, que es un pasivo y por eso va al haber. Al comparar ambos en el período se ve cuánto IVA corresponde declarar, siguiendo siempre la norma vigente.",
        "Un asiento de compra al contado carga Mercaderías (neto) e IVA Crédito Fiscal al debe y abona Caja (total) al haber. Una venta a crédito carga Clientes (total) al debe y abona Ventas (neto) e IVA Débito Fiscal al haber. Si se mezcla el IVA con el neto, los impuestos quedan mal calculados.",
    ],
    vocab=[("neto", "valor del bien sin impuesto"), ("IVA", "impuesto al valor agregado que se suma a compras y ventas"), ("IVA Crédito Fiscal", "cuenta del IVA pagado en compras (debe)"), ("IVA Débito Fiscal", "cuenta del IVA cobrado en ventas (haber)"), ("total con IVA", "neto más IVA"), ("al contado", "pagado o cobrado en el momento"), ("a crédito", "pagado o cobrado más adelante")],
    worked=[
        ("Compra con IVA", "Una empresa de ejemplo compra mercaderías al contado, neto $80.000, con IVA de ejemplo de 10 %. ¿Cuál es el asiento?", ["IVA = 80.000 × 10 ÷ 100 = 8.000; total = 88.000.", "Debe Mercaderías 80.000 e IVA Crédito Fiscal 8.000; Haber Caja 88.000."], "Debe Mercaderías 80.000 e IVA Crédito Fiscal 8.000; Haber Caja 88.000"),
        ("Venta con IVA", "Una empresa de ejemplo vende al contado, neto $200.000, con IVA de ejemplo de 10 %. ¿Cuál es el asiento?", ["IVA = 20.000; total = 220.000.", "Debe Caja 220.000; Haber Ventas 200.000 e IVA Débito Fiscal 20.000."], "Debe Caja 220.000; Haber Ventas 200.000 e IVA Débito Fiscal 20.000"),
    ],
    mistakes=[("Anotar el total con IVA en Mercaderías.", "El IVA no es parte del valor de la mercadería: se anota en su propia cuenta.", "Separa neto e IVA antes de hacer el asiento."),
              ("Anotar el IVA de una venta en IVA Crédito Fiscal.", "El IVA cobrado en una venta es una obligación: va en IVA Débito Fiscal, al haber.", "Compra, IVA crédito al debe; venta, IVA débito al haber.")],
    T=[
        ("abc", "El IVA de una compra se registra en...", "IVA Crédito Fiscal, al debe", "IVA Débito Fiscal, al haber", "Ventas, al haber", "El IVA pagado en compras es IVA Crédito Fiscal y, siendo un activo, va al debe."),
        ("abc", "El IVA de una venta se registra en...", "IVA Débito Fiscal, al haber", "IVA Crédito Fiscal, al debe", "Mercaderías, al debe", "El IVA cobrado en ventas es una obligación y va al haber."),
        ("ab", "El total de una factura con IVA es...", "Neto más IVA", "Neto menos IVA", "El total es el valor del bien más el impuesto."),
        ("=", "{F} Con la tasa de ejemplo, ¿cuántos pesos de IVA tiene la Op. 1?", "150000*10//100", "El IVA se calcula como neto por 10 y dividido por 100.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se pagan en total en la Op. 1 (neto más IVA)?", "150000+15000", "El total es el neto más el IVA calculado.", " pesos"),
        ("=", "{F} Con la tasa de ejemplo, ¿cuántos pesos de IVA tiene la Op. 2?", "400000*10//100", "El IVA de la venta se calcula con la misma tasa de ejemplo.", " pesos"),
        ("abc", "{F} ¿Cuál es el asiento de la Op. 1?", "Debe Mercaderías 150.000 e IVA Crédito Fiscal 15.000; Haber Caja 165.000", "Debe Mercaderías 165.000; Haber Caja 165.000", "Debe Caja 165.000; Haber Mercaderías 150.000 e IVA Crédito Fiscal 15.000", "Se separa el IVA en su propia cuenta y la caja baja por el total pagado."),
        ("abc", "{F} ¿Cuál es el asiento de la Op. 2?", "Debe Clientes 440.000; Haber Ventas 400.000 e IVA Débito Fiscal 40.000", "Debe Caja 440.000; Haber Ventas 440.000", "Debe Clientes 400.000; Haber Ventas 400.000", "Como es a crédito, se carga Clientes; ventas e IVA débito van al haber."),
        ("abc", "{F} ¿Cuál es el asiento de la Op. 3?", "Debe Arriendo 90.000; Haber Caja 90.000", "Debe Caja 90.000; Haber Arriendo 90.000", "Debe Arriendo 90.000; Haber Ventas 90.000", "El gasto de arriendo aumenta por el debe y la caja baja por el haber."),
        ("abc", "¿Por qué el IVA Crédito Fiscal va al debe?", "Porque es un activo (un derecho a favor de la empresa) y los activos aumentan por el debe", "Porque todas las compras van al debe", "Porque es un gasto de la empresa", "Su naturaleza de activo explica el lado del debe; no depende de que sea una compra."),
        ("=", "{F} ¿Cuánto suma el haber del asiento de la Op. 2 (ventas más IVA débito)?", "400000+40000", "El haber debe ser igual al total del debe.", " pesos"),
        ("abc", "{F} Una asistente registra la Op. 2 por $400.000 sin separar el IVA. ¿Qué ocurre?", "El IVA Débito Fiscal queda sin registrar y se calcula un impuesto menor al que corresponde", "El IVA queda duplicado", "No cambia nada porque el total es parecido", "Si el IVA no se separa, el impuesto de las ventas queda subestimado."),
        ("=", "{F} Con las Op. 1 y 2, ¿cuántos pesos de diferencia hay entre el IVA Débito Fiscal y el IVA Crédito Fiscal? (se compara según la norma vigente)", "40000-15000", "Se resta el IVA de las compras al IVA de las ventas.", " pesos"),
    ],
    ctx=("abc", "Una auxiliar de ejemplo recibe una factura de compra con neto $60.000 y total $66.000, y duda cómo registrarla. ¿Qué haces?", "Registrar Mercaderías 60.000 e IVA Crédito Fiscal 6.000 al debe, y el total de 66.000 al haber según cómo se pague", "Registrar los 66.000 completos en Mercaderías", "Registrar solo 6.000 y olvidar el neto", "El neto y el IVA se separan; el total pagado o adeudado va al haber."),
    sc=[
        ("En Contabilidad: ¿qué es el neto de una factura?", "El valor del bien sin impuesto", "El IVA se suma al neto para obtener el total."),
        ("¿Qué cuenta recibe el IVA de una venta?", "IVA Débito Fiscal, al haber", "Es una obligación con el fisco, por eso va al haber."),
        ("¿Quién fija la tasa real del IVA?", "La norma vigente", "En este cuaderno se usa solo una tasa de ejemplo."),
    ],
    op=("Con la tasa de ejemplo de 10 %, escribe el asiento de estas dos operaciones del «Taller Rayén»: (a) compra de mercaderías al contado, neto $300.000; (b) venta al contado, neto $500.000. Calcula el IVA y el total de cada una y comprueba que debe = haber.",
        "(a) IVA 30.000; total 330.000. Debe Mercaderías 300.000 e IVA Crédito Fiscal 30.000; Haber Caja 330.000. (b) IVA 50.000; total 550.000. Debe Caja 550.000; Haber Ventas 500.000 e IVA Débito Fiscal 50.000. En ambos casos debe = haber.",
        ["calcula IVA y total con la tasa de ejemplo", "usa IVA crédito en la compra e IVA débito en la venta", "comprueba que debe = haber"],
        ["hoja con cálculos y dos asientos"],
        ["registrar el IVA dentro de Mercaderías", "usar IVA crédito en la venta", "no comprobar el cuadre"],
        "Pregunta: «¿por qué el IVA de la venta va al haber?». Si no menciona que es una obligación, repasa la naturaleza de la cuenta."),
    reinforce="Calcula el IVA de ejemplo y el total de una compra con neto $90.000 y escribe su asiento.",
    extend="Explica qué pasaría con las cifras de una empresa si todas las ventas se registraran sin separar el IVA.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (asientos de ejemplo de «Taller Rayén»; IVA de ejemplo: 10 %). A1: aporte del dueño en efectivo: Debe Caja 1.000.000; Haber Capital 1.000.000. "
     "A2: compra al contado: Debe Mercaderías 200.000 e IVA Crédito Fiscal 20.000; Haber Caja 220.000. A3: venta a crédito: Debe Clientes 330.000; Haber Ventas 300.000 e IVA Débito Fiscal 30.000. "
     "A4: cobro al cliente: Debe Caja 330.000; Haber Clientes 330.000.")
build(
    O2, 4, F,
    use="Aprenderé a pasar asientos al libro mayor, calcular saldos y preparar un balance de comprobación.",
    prior=["Sé hacer asientos con debe y haber.", "Sé sumar y restar importes.", "Sé qué es una cuenta."],
    explain=[
        "El libro mayor tiene una cuenta por hoja o por tabla. Cada asiento del diario se traspasa: el monto del debe se anota en el debe de esa cuenta y el del haber en el haber. Al final se calcula el saldo de cada cuenta restando el lado menor al lado mayor. Si el debe es mayor, el saldo es deudor; si el haber es mayor, es acreedor.",
        "El balance de comprobación lista todos los saldos. Se suman por separado los saldos deudores y los acreedores. Si el trabajo está bien traspasado, ambas sumas son iguales. Es una comprobación de que se respetó la partida doble.",
        "Que el balance cuadre no prueba que no haya errores: se puede haber usado la cuenta equivocada, haber anotado el mismo monto mal en ambos lados u olvidado un asiento completo, y aun así cuadrar. Por eso también se revisan los documentos y las cuentas utilizadas.",
    ],
    vocab=[("traspaso", "paso de un asiento del diario al mayor"), ("saldo deudor", "cuenta con debe mayor que haber"), ("saldo acreedor", "cuenta con haber mayor que debe"), ("balance de comprobación", "lista de saldos cuyas sumas deben coincidir"), ("sumas iguales", "total de saldos deudores igual al de acreedores")],
    worked=[
        ("Saldo de una cuenta", "En el mayor de Caja de otra empresa de ejemplo, el debe suma $500.000 y el haber $120.000. ¿Cuál es su saldo?", ["Se resta el lado menor al mayor: 500.000 − 120.000.", "Como el debe es mayor, el saldo es deudor."], "Saldo deudor de $380.000"),
        ("Tipo de saldo", "Una cuenta Ventas de ejemplo tiene haber $900.000 y debe $0. ¿Qué tipo de saldo tiene?", ["El lado mayor es el haber.", "Cuando el haber es mayor, el saldo es acreedor."], "Acreedor por $900.000"),
    ],
    mistakes=[("Sumar juntos los saldos deudores y acreedores en una sola columna.", "Se comparan por separado: la comprobación es que ambas sumas sean iguales.", "Haz dos sumas distintas y compáralas."),
              ("Creer que si el balance cuadra no hay errores.", "Pueden existir errores que no alteran la igualdad.", "Revisa también los documentos, las cuentas y los períodos.")],
    T=[
        ("abc", "En Contabilidad: ¿qué es el libro mayor?", "El libro donde se agrupan los movimientos de cada cuenta", "El libro donde los hechos se anotan solo por fecha", "El informe final que se entrega al banco", "El mayor reúne los movimientos por cuenta; el diario los ordena por fecha."),
        ("abc", "¿Cuándo una cuenta tiene saldo deudor?", "Cuando su debe es mayor que su haber", "Cuando tiene deudas con el banco", "Cuando su haber es mayor que su debe", "El saldo se llama deudor por el lado que predomina en la cuenta, no por la existencia de deudas."),
        ("ab", "¿Para qué sirve el balance de comprobación?", "Para comprobar que la suma de saldos deudores es igual a la de acreedores", "Para calcular los impuestos de la empresa", "Es una verificación de que se respetó la partida doble."),
        ("=", "{F} ¿Cuántos pesos suma el debe de la cuenta Caja (A1 y A4)?", "1000000+330000", "Se suman los montos anotados al debe de Caja.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el saldo deudor de Caja después de A1, A2 y A4?", "1000000+330000-220000", "Se suma el debe y se resta el haber de Caja.", " pesos"),
        ("=", "{F} ¿Qué saldo tiene Clientes después de A3 y A4?", "330000-330000", "Se compara lo cargado en A3 con lo abonado en A4.", " pesos"),
        ("abc", "{F} ¿Qué tipo de saldo tiene Ventas?", "Acreedor", "Deudor", "Ninguno, porque es un ingreso", "Ventas solo tiene monto en el haber, por lo tanto su saldo es acreedor."),
        ("=", "{F} Con Caja en 1.110.000, ¿cuántos pesos suman los saldos deudores (Caja, Mercaderías e IVA Crédito Fiscal)?", "1110000+200000+20000", "Se suman los saldos que quedaron con el debe mayor.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suman los saldos acreedores (Capital, Ventas e IVA Débito Fiscal)?", "1000000+300000+30000", "Se suman los saldos que quedaron con el haber mayor.", " pesos"),
        ("abc", "{F} Con las sumas calculadas (1.330.000 en deudores y 1.330.000 en acreedores), ¿cuadra el balance de comprobación?", "Sí, porque ambas sumas son iguales", "No, porque hay más cuentas deudoras que acreedoras", "No se puede saber sin ver el balance anual", "Si ambas sumas son iguales, el balance cuadra; la cantidad de cuentas no importa."),
        ("abc", "{F} La auxiliar olvida pasar el cobro A4 al haber de Clientes (pero sí lo pasa a Caja). ¿Qué saldo queda en Clientes?", "Deudor por $330.000 y el balance deja de cuadrar", "Cero y el balance cuadra", "Acreedor por $330.000", "Sin el haber, Clientes conserva el debe de A3; el balance se descuadra porque faltó un lado."),
        ("=", "{F} En ese caso (sin el haber de Clientes), ¿cuántos pesos sumarían los saldos deudores?", "1330000+330000", "Cuando falta un lado, la suma de un grupo de saldos queda mayor.", " pesos"),
        ("abc", "Un balance de comprobación cuadra, pero se anotó una compra de mercaderías en la cuenta Luz. ¿Qué se concluye?", "Cuadrar no basta: hay un error de cuenta que el balance no detecta", "Que el trabajo está perfecto", "Que Luz debe pasar al grupo de pasivos", "El balance solo comprueba igualdad de sumas, no que la cuenta sea la correcta."),
    ],
    ctx=("abc", "Una auxiliar de ejemplo termina el balance de comprobación y cuadra. Su jefa pide entregarlo mañana. ¿Qué conviene hacer antes?", "Revisar una muestra de asientos contra sus documentos y cuentas", "Entregarlo sin más porque cuadra", "Borrar los asientos que no recuerda", "Cuadrar es necesario pero no suficiente; se verifican documentos y cuentas."),
    sc=[
        ("En Contabilidad: ¿qué saldo tiene una cuenta con haber mayor que debe?", "Acreedor", "El saldo toma el nombre del lado mayor de la cuenta."),
        ("¿Qué se compara en el balance de comprobación?", "La suma de saldos deudores con la de saldos acreedores", "Deben ser iguales si se respetó la partida doble."),
        ("¿Prueba el cuadre que no hay errores?", "No, pueden existir errores de cuenta o de documento", "El cuadre solo comprueba igualdad de sumas."),
    ],
    op=("En el mayor de una empresa de ejemplo, Caja tiene debe $900.000 y haber $350.000; Clientes tiene debe $400.000 y haber $150.000; Proveedores tiene debe $100.000 y haber $500.000; Capital tiene haber $300.000. Calcula el saldo de cada cuenta, indica si es deudor o acreedor, suma ambos grupos y di si el balance cuadra.",
        "Caja: 550.000 deudor. Clientes: 250.000 deudor. Proveedores: 400.000 acreedor. Capital: 300.000 acreedor. Deudores: 550.000 + 250.000 = 800.000. Acreedores: 400.000 + 300.000 = 700.000. No cuadra (diferencia de 100.000): hay que buscar el error en los asientos.",
        ["calcula los cuatro saldos", "clasifica correctamente deudor y acreedor", "suma los grupos y concluye que no cuadra"],
        ["hoja con la tabla de saldos y la conclusión"],
        ["sumar deudores y acreedores juntos", "no indicar la diferencia", "afirmar que cuadra"],
        "Pregunta: «¿qué haces ahora que no cuadra?». Si responde «lo ajusto», recuerda que se busca el error con los documentos."),
    reinforce="Inventa dos cuentas con su debe y su haber y calcula su saldo deudor o acreedor.",
    extend="Explica con un ejemplo inventado un error que no se detecta con el balance de comprobación.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 9 (balance de comprobación de ejemplo, con un error). Saldos deudores: Caja $500.000; Clientes $300.000; Mercaderías $400.000. "
     "Saldos acreedores: Proveedores $250.000; Capital $800.000; Ventas $300.000. Libro diario de ese mes: el día 12 se pagó arriendo en efectivo, $150.000 "
     "(Debe Arriendo 150.000; Haber Caja 150.000), pero la cuenta Arriendo no se traspasó al mayor.")
build(
    O2, 5, F,
    use="Aprenderé a buscar y corregir errores cuando un balance no cuadra y a comparar alternativas de corrección con criterios de calidad.",
    prior=["Sé armar un balance de comprobación.", "Sé la partida doble.", "Sé restar totales."],
    explain=[
        "Cuando un balance no cuadra hay un error que se busca con orden, nunca forzando cifras. Primero se repiten las sumas. Luego se calcula la diferencia entre los totales y se prueba con tres pistas: si es igual a un monto de un asiento, quizá ese monto se anotó solo en un lado; si es el doble de un monto, quizá un saldo está en el lado equivocado; si es múltiplo de 9, quizá dos cifras se anotaron cambiadas de lugar (por ejemplo, 450 por 540).",
        "Para comparar alternativas de corrección se usan criterios de calidad: que la corrección tenga respaldo en un documento, que use la cuenta correcta, que respete el período y que no cree un nuevo desajuste. Corregir sumando una cifra a una cuenta «que acepte cualquier cosa» solo esconde el error.",
        "Una buena práctica es dejar constancia: qué se encontró, qué se corrigió y quién lo revisó. Esto da trazabilidad, es decir, que cualquiera pueda seguir el rastro del cambio hasta el documento. El contador aprueba las correcciones.",
    ],
    vocab=[("diferencia", "resultado de restar los dos totales del balance"), ("transposición", "cambio de lugar de dos cifras al anotar"), ("trazabilidad", "posibilidad de seguir el rastro de un registro hasta su documento"), ("corrección", "arreglo del error con respaldo"), ("calidad", "información correcta, respaldada y revisable")],
    worked=[
        ("Diferencia igual a un monto", "Un balance de ejemplo tiene saldos deudores por $890.000 y acreedores por $930.000. En el diario hay un pago de $40.000 que no aparece en el mayor. ¿Qué error se sospecha?", ["La diferencia es 930.000 − 890.000 = 40.000.", "Coincide con el pago que no aparece: probablemente falta el traspaso de ese monto."], "Falta traspasar el pago de $40.000"),
        ("Saldo en el lado equivocado", "En otro balance de ejemplo la diferencia es $140.000 y hay un saldo de $70.000 que figura en el lado opuesto al que le corresponde. ¿Por qué es sospechoso?", ["El doble de 70.000 es 140.000.", "Un saldo en el lado equivocado cambia la diferencia en el doble de su monto."], "Probable saldo anotado en el lado equivocado"),
    ],
    mistakes=[("Sumar la diferencia a Capital «para que cuadre».", "Se esconde el error y se deja una cifra falsa.", "Busca el error con los documentos y corrige donde ocurrió."),
              ("Corregir tachando y escribiendo encima, sin dejar constancia.", "Se pierde la trazabilidad y nadie sabe qué cambió ni por qué.", "Corrige con un asiento de ajuste respaldado y avisa al contador.")],
    T=[
        ("abc", "¿Qué indica un balance de comprobación con totales distintos?", "Que hay al menos un error que debe buscarse", "Que la empresa tiene pérdidas", "Que faltan dueños en la empresa", "El desajuste señala un error de registro, no un resultado de la empresa."),
        ("abc", "¿Cuál es el primer paso para buscar la diferencia?", "Repetir las sumas de las columnas", "Cambiar cifras hasta que cuadre", "Ajustar la cuenta Capital", "Muchos desajustes vienen de sumas mal hechas; se revisan primero."),
        ("ab", "Una diferencia igual a un monto del diario suele indicar...", "Que ese monto se anotó solo en un lado", "Que el balance está correcto", "Si falta un lado de un asiento, la diferencia coincide con su monto."),
        ("=", "{F} ¿Cuántos pesos suman los saldos deudores?", "500000+300000+400000", "Se suman solo los saldos del grupo deudor.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suman los saldos acreedores?", "250000+800000+300000", "Se suman solo los saldos del grupo acreedor.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre acreedores y deudores?", "1350000-1200000", "La diferencia es el total mayor menos el menor.", " pesos"),
        ("abc", "{F} ¿Qué hecho del diario coincide con la diferencia?", "El pago de arriendo de $150.000 sin traspaso al mayor", "El saldo de Capital de $800.000", "El saldo de Clientes de $300.000", "La diferencia es $150.000, igual al arriendo cuyo traspaso quedó pendiente."),
        ("abc", "{F} ¿Cuál es la corrección con respaldo?", "Traspasar al mayor el asiento del arriendo, agregando la cuenta Arriendo con saldo deudor de $150.000", "Restar $150.000 a Ventas para igualar", "Sumar $150.000 a Capital para igualar", "Corrige el traspaso omitido; las otras dos alternativas fuerzan el cuadre sin respaldo."),
        ("=", "{F} Después de corregir, ¿cuántos pesos suman los saldos deudores?", "500000+300000+400000+150000", "Se agrega el saldo deudor de la cuenta Arriendo a los deudores.", " pesos"),
        ("abc", "{F} Un compañero propone sumar $150.000 a Capital «para que cuadre rápido». ¿Qué respondes?", "No: se oculta el error, deja cifras falsas y se corrige donde está con respaldo", "Sí: lo importante es que cuadre antes de la hora de salida", "Sí, pero solo si el dueño no se entera", "Forzar una cuenta no corrige el error y vuelve poco confiable la información."),
        ("abc", "Un balance tiene una diferencia de $90.000 y ningún asiento del diario tiene un monto de $90.000 ni de $45.000. ¿Qué error se sospecha?", "Dos cifras anotadas cambiadas de lugar, porque 90.000 es múltiplo de 9", "Un monto anotado solo en un lado del asiento", "Un saldo anotado en el lado equivocado", "Como no hay un monto igual a la diferencia ni a su mitad, quedan descartados el lado omitido y el saldo en el lado opuesto; el múltiplo de 9 apunta a cifras transpuestas."),
        ("=", "Una cifra de 730.000 se anotó como 370.000. ¿Cuántos pesos de diferencia produce?", "730000-370000", "La diferencia entre la cifra correcta y la anotada es múltiplo de 9.", " pesos"),
        ("abc", "{F} ¿Cuál de estas acciones NO corresponde en una revisión de calidad?", "Cambiar cifras hasta que el balance cuadre más rápido", "Comparar el asiento con su documento", "Verificar que la cuenta usada sea la correcta", "Revisar es comprobar con respaldo; manipular cifras destruye la calidad."),
    ],
    ctx=("abc", "Es viernes por la tarde y el balance de una empresa de ejemplo no cuadra por $48.000. La jefa dice que lo arregles sin dejar nada anotado. ¿Qué haces?", "Busco el error con los documentos, registro la corrección con respaldo y aviso al contador", "Sumo $48.000 a Capital y me voy", "Dejo el balance sin cuadrar y no digo nada", "Se corrige donde ocurrió el error, dejando constancia para que sea revisable."),
    sc=[
        ("En Contabilidad: ¿qué pista da una diferencia múltiplo de 9?", "Que dos cifras pueden haberse anotado cambiadas de lugar", "Es un patrón típico de las transposiciones de cifras."),
        ("¿Qué pista da una diferencia igual al monto de un asiento?", "Que ese monto se anotó solo en un lado", "Falta una parte de la partida doble."),
        ("¿Qué es la trazabilidad de una corrección?", "Poder seguir su rastro hasta el documento que la respalda", "Permite revisar quién cambió qué y por qué."),
    ],
    op=("Un balance de comprobación de ejemplo suma $1.640.000 en saldos deudores y $1.700.000 en saldos acreedores. En el diario hay un cobro de $60.000 (Debe Caja; Haber Clientes) que se pasó al haber de Clientes pero no al debe de Caja. Calcula la diferencia, explica qué error sospechas, propone una corrección con respaldo y escribe qué dejarías por escrito para el contador.",
        "Diferencia: 1.700.000 − 1.640.000 = 60.000, igual al monto del cobro. Sospecho que el debe de Caja por 60.000 no se traspasó (con ese lado faltante, los deudores quedan menores). Corrección: traspasar ese lado del asiento al mayor con el comprobante de cobro. Constancia: qué se encontró, el monto, el documento y quién lo corrigió.",
        ["calcula la diferencia", "relaciona la diferencia con el cobro omitido", "propone una corrección con respaldo y constancia"],
        ["hoja con la diferencia, la hipótesis y la corrección"],
        ["sumar la diferencia a Capital", "no dejar constancia", "no relacionar con el diario"],
        "Pregunta: «¿en qué documento apoyas la corrección?». Si no nombra uno, pídele que busque el comprobante de cobro."),
    reinforce="Escribe una lista de cinco controles que revisarías si un balance no cuadra.",
    extend="Explica por qué una diferencia múltiplo de 9 no prueba por sí sola una transposición.",
)
