"""Administración 3.º medio TP: OAE-01 (información contable básica) y OAE-02 (programa de actividades operativas). Empresas, personas y cifras inventadas; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, documentos, planillas y casos están escritos en cada ejercicio: las empresas y las personas son inventadas y las cifras son «de ejemplo», "
             "así que no necesitas programas, internet ni datos de empresas reales. No uses datos personales ni documentos reales de tu familia o de tu empresa de práctica. "
             "Este cuaderno enseña conceptos y cálculos básicos en papel; los impuestos, plazos y requisitos legales se consultan siempre en la norma vigente y con tu docente de la especialidad. "
             "Trabaja sentado con la espalda apoyada y haz una pausa corta cada 45 minutos.")

build = make_build(MATERIALS)

O1 = "TP-ADMI-3-OAE-01"
O2 = "TP-ADMI-3-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Empresa ficticia «Comercial Los Aromos Ltda.», que vende artículos de ferretería. Datos de ejemplo del mes: ventas $6.000.000; compras de mercaderías $3.500.000; "
     "sueldos $900.000; arriendo $400.000; deudas con proveedores $1.500.000. La dueña, Marcela, quiere saber cómo va el negocio.")
build(
    O1, 1, F,
    use="Aprenderé para qué sirve la información contable, quiénes la usan, qué normas la ordenan y qué cuidados éticos exige.",
    prior=["Sé sumar y restar cifras en pesos.", "Sé leer una tabla simple.", "Conozco la diferencia entre ganar y vender."],
    explain=[
        "La información contable es el conjunto de datos ordenados sobre lo que una empresa vende, lo que gasta, lo que tiene y lo que debe. Sirve para conocer la marcha de la empresa: si gana o pierde, si puede pagar sus deudas y si conviene crecer. La usan personas de adentro (dueños y jefaturas, usuarios internos) y de afuera (bancos y el Servicio de Impuestos Internos, usuarios externos).",
        "Esa información se ordena con normas. Las NIC y las NIIF son las normas internacionales de contabilidad y de información financiera: reglas comunes para reconocer y presentar las cifras. La legislación tributaria dice qué impuestos se pagan y qué documentos se deben guardar como respaldo. Si la empresa importa o exporta mercaderías, además interviene el Servicio Nacional de Aduanas. Las reglas cambian, así que siempre se revisa la norma vigente.",
        "Los riesgos de este trabajo son técnicos y éticos. Un error de digitación cambia el resultado; alterar un registro para que la empresa se vea mejor es una falta grave; comentar fuera de la empresa cifras que son reservadas rompe la confidencialidad. Por eso cada cifra debe tener un documento de respaldo, y la información financiera se comparte solo con quienes corresponde.",
    ],
    vocab=[("información contable", "datos ordenados sobre ventas, gastos, bienes y deudas de una empresa"), ("ingreso", "dinero que entra por vender"), ("costos y gastos", "lo que la empresa paga o consume para funcionar"), ("respaldo", "documento que prueba una cifra registrada"), ("confidencialidad", "deber de no difundir información reservada"), ("norma vigente", "regla que está en uso hoy y no ha sido reemplazada")],
    worked=[
        ("Ganar o perder", "La tienda ficticia «Librería Caracol» vendió $2.000.000 en un mes y tuvo costos y gastos por $1.500.000. ¿Ganó o perdió?", ["Se compara lo que entró con lo que salió.", "2.000.000 − 1.500.000 = 500.000; entró más de lo que salió."], "Ganó $500.000"),
        ("Clasificar un dato", "En la librería, el arriendo del local es de $350.000 al mes. ¿Es un ingreso o un gasto?", ["El arriendo es dinero que la empresa paga para poder funcionar.", "Todo lo que se paga para funcionar es un gasto."], "Es un gasto"),
    ],
    mistakes=[("«Vendimos mucho, entonces ganamos.»", "Vender es solo la entrada de dinero; para saber si se ganó hay que restar los costos y gastos.", "Calcula ventas menos costos y gastos antes de concluir."),
              ("Anotar una venta sin guardar la boleta o la factura.", "Sin respaldo no se puede probar la cifra ante la jefatura ni ante el Servicio de Impuestos Internos.", "Registra cada cifra con su documento y archívalo.")],
    T=[
        ("abc", "En Administración: ¿qué es la información contable?", "Datos ordenados sobre ventas, gastos, bienes y deudas de una empresa", "Una lista de clientes con sus teléfonos y direcciones", "El horario de atención y las promociones del local", "La información contable ordena cifras de la empresa; las otras opciones son datos comerciales."),
        ("abc", "{F} ¿Cuál dato de la ficha es un ingreso?", "Ventas por $6.000.000", "Arriendo por $400.000", "Sueldos por $900.000", "El ingreso es dinero que entra por vender; arriendo y sueldos son pagos que salen."),
        ("abc", "En Chile, ¿qué institución se ocupa de los impuestos internos?", "El Servicio de Impuestos Internos", "El Servicio Nacional de Aduanas, que solo ve el comercio con el exterior", "La Dirección del Trabajo, que solo ve las relaciones laborales", "Los impuestos internos los administra el Servicio de Impuestos Internos; las otras instituciones tienen otras tareas."),
        ("abc", "{F} ¿Para qué le sirve la información contable a Marcela?", "Para saber si el negocio gana o pierde y si puede pagar sus deudas", "Para elegir el color del uniforme del personal", "Para decidir qué música se toca en el local", "La información contable informa la marcha del negocio; el uniforme y la música no dependen de ella."),
        ("abc", "Un banco pide los estados de una empresa para evaluar un crédito. ¿Qué tipo de usuario de la información es el banco?", "Externo, porque está fuera de la empresa", "Interno, porque presta dinero a la empresa", "Ninguno, porque los bancos no usan información contable", "Los usuarios externos están fuera de la empresa y usan sus cifras, como bancos o el Servicio de Impuestos Internos."),
        ("abc", "¿Qué son las NIC y las NIIF?", "Normas internacionales para reconocer y presentar la información contable", "Impuestos que se pagan por importar productos", "Documentos que se entregan a los clientes al vender", "Las NIC y las NIIF son reglas contables comunes; no son impuestos ni documentos de venta."),
        ("=", "{F} ¿Cuántos pesos suman los costos y gastos del mes (compras, sueldos y arriendo)?", "3500000+900000+400000", "Se suman las tres salidas de dinero que aparecen en la ficha.", " pesos"),
        ("=", "{F} ¿Cuántos pesos ganó la empresa en el mes (ventas menos compras, sueldos y arriendo)?", "6000000-3500000-900000-400000", "El resultado es lo que entró menos todas las salidas del mes.", " pesos"),
        ("abc", "Ana anota una venta de la tienda sin guardar boleta ni factura «para no perder tiempo». ¿Qué falta en ese registro?", "El respaldo: sin documento no se puede probar la cifra", "Una calculadora más grande para sumar", "Un segundo registro idéntico en otro cuaderno", "Una cifra sin documento queda sin prueba; copiarla dos veces no la respalda."),
        ("abc", "Un compañero propone bajar la cifra del arriendo en el registro para que la empresa «se vea mejor» ante el banco. ¿Qué corresponde?", "Rechazarlo y registrar el valor real con su respaldo", "Aceptarlo si la diferencia es pequeña", "Aceptarlo si nadie del banco lo revisa", "Alterar un registro es una falta ética sin importar su tamaño ni quién lo revise."),
        ("abc", "Una asistente ve el balance en el computador de su jefatura y lo comenta con amigos en una red social. ¿Qué principio rompe?", "La confidencialidad de la información de la empresa", "La regla de ordenar los archivos por fecha", "La norma de usar siempre calculadora", "Comentar cifras reservadas con terceros rompe la confidencialidad."),
        ("=", "{F} Si las ventas del mes hubieran sido $4.500.000 y los costos y gastos los mismos de la ficha, ¿cuántos pesos habría perdido la empresa?", "3500000+900000+400000-4500000", "La pérdida es la diferencia entre lo que salió y lo que entró cuando salió más.", " pesos"),
        ("abc", "{F} Marcela dice: «Vendimos $6.000.000, así que ganamos $6.000.000». ¿Qué le responderías?", "Que hay que restar costos y gastos: lo ganado es menos que lo vendido", "Que tiene razón, porque las ventas son la ganancia", "Que debe sumar también las deudas con proveedores a las ventas", "La ganancia sale de restar costos y gastos a las ventas; las deudas no se suman a lo vendido."),
    ],
    ctx=("abc", "La contadora externa avisa que una regla tributaria cambió este año. ¿Qué haces al registrar las ventas del mes?", "Revisar la norma vigente y aplicar la regla actual", "Seguir usando la regla del año pasado por costumbre", "Preguntar a un amigo que trabaja en otra empresa", "Las reglas tributarias cambian; se aplica la norma vigente y no la costumbre ni una opinión informal."),
    sc=[
        ("En Administración: ¿qué diferencia hay entre vender y ganar?", "Vender es lo que entra; ganar es lo que queda después de restar costos y gastos", "Para saber si se ganó hay que comparar ingresos con costos y gastos."),
        ("¿Por qué cada cifra necesita un respaldo?", "Porque el documento prueba que la cifra es real y permite revisarla", "El respaldo permite comprobar cada cifra ante jefaturas o el Servicio de Impuestos Internos."),
        ("¿Qué haces si te piden alterar un registro para mejorar la imagen de la empresa?", "Me niego y aviso a mi jefatura directa", "Alterar registros es una falta ética; se informa a la jefatura."),
    ],
    op=("Con los datos de la Ficha 1, escribe un mensaje de cinco líneas para Marcela. Debe decir (1) cuánto vendió, (2) cuánto sumaron los costos y gastos, (3) cuánto ganó o perdió, (4) qué documento respalda cada cifra y (5) a quién le pediría revisar la norma vigente antes de declarar impuestos.\n{F}",
        "Marcela: en el mes se vendieron $6.000.000. Los costos y gastos sumaron $4.800.000 (compras, sueldos y arriendo). El resultado fue una ganancia de $1.200.000. Cada cifra se respalda con facturas, boletas y el contrato de arriendo. Antes de declarar impuestos pediré a la contadora que revise la norma vigente.",
        ["usa las cifras correctas de la ficha", "distingue vender de ganar", "nombra documentos de respaldo", "indica a quién consultar la norma vigente"],
        ["mensaje de cinco líneas con cifras y respaldos"],
        ["decir que ganó $6.000.000", "no mencionar respaldos", "inventar tasas o plazos legales"],
        "Revisa que el mensaje reste los costos y gastos y que ninguna cifra se invente. Si falta el respaldo de una cifra, pide que lo agregue."),
    reinforce="Escribe en tu cuaderno cinco ejemplos de ingreso y cinco de gasto de un kiosco ficticio y suma cada grupo con cifras de ejemplo.",
    extend="Explica con un ejemplo inventado por qué una empresa puede vender mucho y aun así perder dinero.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados) de «Comercial Los Aromos Ltda.». Documento 1: factura de venta por $595.000 a otra empresa. Documento 2: boleta por $8.000 a un cliente final. "
     "Documento 3: nota de crédito por $50.000 que rebaja la factura del Documento 1 por una devolución. Documento 4: guía de despacho que acompaña la mercadería que sale de la bodega. "
     "Cargos: Carla, asistente contable (registra y archiva); Pedro, contador externo (revisa y prepara los estados financieros); Marcela, gerenta (decide con esa información).")
build(
    O1, 2, F,
    use="Aprenderé los conceptos de activo, pasivo y patrimonio, los documentos de respaldo más usados y los roles de quienes trabajan con la información contable.",
    prior=["Sé qué es ingreso y qué es gasto.", "Sé que cada cifra necesita respaldo.", "Sé sumar y restar en pesos."],
    explain=[
        "El activo son los bienes y derechos de la empresa: dinero en caja, mercaderías en bodega y lo que los clientes le deben. El pasivo son sus deudas y obligaciones, por ejemplo lo que debe a proveedores o a un banco. El patrimonio es lo que queda para los dueños: aportes más resultados acumulados. Los tres se relacionan con una ecuación: activo = pasivo + patrimonio.",
        "Los documentos respaldan las operaciones. La factura respalda una venta entre empresas; la boleta, una venta a un cliente final; la nota de crédito rebaja una factura, por ejemplo por una devolución; la guía de despacho acompaña mercadería que se traslada. En importaciones y exportaciones se suma la documentación presentada ante el Servicio Nacional de Aduanas. Los estados financieros son los informes que resumen todo esto, como el balance.",
        "En el oficio cada persona tiene un rol. La asistente contable registra y archiva los documentos; el contador revisa, ajusta y prepara los estados financieros; la jefatura usa esa información para decidir. Quien registra no decide por su cuenta cambiar una cifra: si un documento tiene un dato dudoso, lo consulta con quien corresponde.",
    ],
    vocab=[("activo", "bienes y derechos de la empresa"), ("pasivo", "deudas y obligaciones de la empresa"), ("patrimonio", "lo que queda para los dueños: activo menos pasivo"), ("factura", "documento que respalda una venta entre empresas"), ("nota de crédito", "documento que rebaja el valor de una factura"), ("guía de despacho", "documento que acompaña mercadería trasladada")],
    worked=[
        ("Clasificar", "Una tienda ficticia tiene $300.000 en caja y debe $200.000 a un banco. ¿Qué es cada dato?", ["El dinero en caja es un bien de la empresa.", "La deuda con el banco es una obligación."], "Caja: activo; deuda con el banco: pasivo"),
        ("Ecuación", "Una empresa de ejemplo tiene activo de $900.000 y pasivo de $350.000. ¿Cuánto es su patrimonio?", ["Patrimonio = activo − pasivo.", "900.000 − 350.000 = 550.000."], "$550.000"),
    ],
    mistakes=[("Registrar la nota de crédito como una venta nueva.", "La nota de crédito rebaja una factura anterior; no suma ventas.", "Resta su valor del documento que corrige."),
              ("Contar la deuda con un proveedor como parte del activo.", "Lo que se debe es pasivo, no un bien de la empresa.", "Clasifica las deudas siempre en el pasivo.")],
    T=[
        ("abc", "En Administración: ¿qué es un activo?", "Un bien o derecho de la empresa, como el dinero en caja", "Una deuda con un proveedor", "El sueldo que se paga a un trabajador", "Los activos son lo que la empresa posee o puede cobrar; las deudas son pasivo y el sueldo es un gasto."),
        ("abc", "{F} ¿Qué documento de la ficha respalda una venta a un cliente final?", "La boleta del Documento 2", "La factura del Documento 1", "La guía de despacho del Documento 4", "La boleta respalda ventas a clientes finales; la factura es entre empresas."),
        ("abc", "¿Cuál de estos datos es un pasivo?", "Una deuda con un proveedor", "Las mercaderías en bodega", "El dinero en caja", "Lo que se debe es pasivo; mercaderías y caja son activos."),
        ("abc", "{F} ¿Qué rol revisa y prepara los estados financieros?", "Pedro, el contador externo", "Carla, la asistente contable", "Marcela, la gerenta", "Según la ficha, Pedro revisa y prepara los estados; Carla registra y Marcela decide."),
        ("abc", "{F} ¿Para qué sirve la nota de crédito del Documento 3?", "Rebajar el valor de la factura por una devolución", "Cobrar un monto adicional al cliente", "Acompañar la mercadería durante el traslado", "La nota de crédito rebaja una factura; la guía de despacho es la que acompaña el traslado."),
        ("abc", "Según la ecuación contable, ¿qué es igual al activo?", "Pasivo más patrimonio", "Pasivo menos patrimonio", "Patrimonio menos ingresos", "La ecuación es activo = pasivo + patrimonio."),
        ("=", "Una empresa de ejemplo tiene pasivo de $1.800.000 y patrimonio de $2.700.000. ¿Cuántos pesos suma su activo?", "1800000+2700000", "Activo = pasivo + patrimonio.", " pesos"),
        ("=", "Otra empresa de ejemplo tiene activo de $6.200.000 y pasivo de $2.450.000. ¿Cuántos pesos es su patrimonio?", "6200000-2450000", "Patrimonio = activo − pasivo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos queda valiendo la factura del Documento 1 después de aplicar la nota de crédito?", "595000-50000", "La nota de crédito se resta del valor de la factura que corrige.", " pesos"),
        ("abc", "Carla recibe una factura de un proveedor con el monto ilegible. ¿Qué corresponde?", "Consultar al proveedor o a Pedro y no registrar una cifra supuesta", "Registrar el monto que le parezca más probable", "Archivar la factura sin registrarla para no equivocarse", "Un dato dudoso se consulta; inventar la cifra o esconder el documento son errores."),
        ("abc", "La empresa compra mercaderías a crédito por un valor de ejemplo. ¿Qué cambia en la ecuación contable?", "Sube el activo (más mercaderías) y sube el pasivo (más deuda) por el mismo valor", "Sube el activo y baja el patrimonio", "Baja el pasivo porque la compra reduce las deudas", "Comprar a crédito agrega un bien y una deuda iguales, y la ecuación se mantiene."),
        ("abc", "La empresa paga con dinero de caja una deuda con un proveedor. ¿Qué ocurre con el activo y con el pasivo?", "Ambos bajan por el mismo valor", "El activo sube y el pasivo baja", "Solo baja el patrimonio", "Se usa caja (activo baja) para cancelar una deuda (pasivo baja) y el patrimonio no cambia."),
        ("abc", "{F} Marcela quiere decidir si pide un préstamo. ¿Qué documento resume la situación de la empresa para decidir?", "Los estados financieros preparados por Pedro", "Una boleta de venta aislada", "La guía de despacho de un solo envío", "Los estados financieros resumen activo, pasivo y patrimonio; un documento aislado no basta."),
    ],
    ctx=("abc", "Una empresa importa herramientas y la asistente recibe el documento de aduana de la mercadería. ¿Qué hace con él?", "Archivarlo junto con la factura y registrarlo como respaldo de la compra", "Botarlo, porque solo importan las boletas", "Entregárselo a un cliente como comprobante de venta", "Los documentos de aduana respaldan la importación y se archivan con la compra."),
    sc=[
        ("En Administración: ¿qué es el patrimonio?", "Lo que queda para los dueños: activo menos pasivo", "Es la diferencia entre lo que la empresa tiene y lo que debe."),
        ("¿Qué documento rebaja el valor de una factura?", "La nota de crédito", "La nota de crédito corrige una factura anterior."),
        ("¿Quién prepara los estados financieros: la asistente o el contador?", "El contador", "El contador revisa y prepara los estados; la asistente registra y archiva."),
    ],
    op=("Con la Ficha 2, arma un cuadro de tres columnas: Documento, Para qué sirve y Quién lo registra o revisa (usa los cargos de la ficha). Incluye los cuatro documentos y agrega una frase que explique qué haría Carla si un documento llega con un dato dudoso.\n{F}",
        "Documento 1, factura: respalda una venta a otra empresa; la registra Carla y la revisa Pedro. Documento 2, boleta: respalda una venta a un cliente final; la registra Carla. Documento 3, nota de crédito: rebaja la factura; la revisa Pedro. Documento 4, guía de despacho: acompaña mercadería trasladada; la archiva Carla. Si un dato es dudoso, Carla lo consulta con Pedro antes de registrar.",
        ["incluye los cuatro documentos de la ficha", "explica correctamente para qué sirve cada uno", "asigna roles según la ficha", "propone consultar y no inventar el dato dudoso"],
        ["cuadro de tres columnas y una frase final"],
        ["confundir factura con boleta", "decir que la nota de crédito suma ventas", "inventar un cargo que la ficha no trae"],
        "Compara cada fila con la ficha. Si el estudiante inventó un dato de un documento, pide que lo corrija con la información de la ficha."),
    reinforce="Escribe cinco bienes y cinco deudas de un negocio ficticio y clasifícalos en activo o pasivo.",
    extend="Explica con un ejemplo inventado qué cambia en la ecuación contable cuando una empresa vende a crédito una mercadería.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (estados de ejemplo, inventados) de «Importadora Cordillera Ltda.» al cierre del mes. ACTIVO: caja $1.500.000; cuentas por cobrar (lo que deben los clientes) $2.500.000; mercaderías $4.000.000. "
     "PASIVO: proveedores $2.000.000; préstamo bancario $1.500.000. PATRIMONIO: $4.500.000. RESULTADO DEL MES: ventas $5.000.000; costo de ventas (lo que costó lo vendido) $3.000.000; gastos de administración $1.200.000.")
build(
    O1, 3, F,
    use="Aprenderé a leer un balance y un resultado del mes, a comprobar que cuadran y a sacar conclusiones simples sobre la marcha de la empresa.",
    prior=["Sé qué son activo, pasivo y patrimonio.", "Sé la diferencia entre vender y ganar.", "Sé sumar y restar cifras grandes."],
    explain=[
        "El balance es un informe que muestra, en un momento dado, el activo, el pasivo y el patrimonio de la empresa. Se comprueba que cuadre: el total del activo debe ser igual al pasivo más el patrimonio. Si no cuadra, hay un error de registro o de suma y se corrige con los documentos de respaldo antes de usar el informe.",
        "El estado de resultados muestra lo ocurrido en un período. Se calcula así: ventas menos costo de ventas da la utilidad bruta; a esa utilidad se le restan los gastos de administración y queda el resultado del período, que puede ser ganancia o pérdida. El costo de ventas es lo que costó adquirir las mercaderías que se vendieron.",
        "Leer es comparar. Para saber si la empresa puede pagar lo que debe, se mira cuánto tiene disponible (caja) y cuánto tiene por cobrar frente a lo que debe a proveedores y al banco. Una cifra sola dice poco: se interpreta con otras cifras de la misma ficha y se anota la conclusión con sus límites, por ejemplo «con estos datos de un mes no se puede asegurar el resto del año».",
    ],
    vocab=[("balance", "informe del activo, pasivo y patrimonio en un momento"), ("estado de resultados", "informe de lo ganado o perdido en un período"), ("costo de ventas", "lo que costó adquirir lo que se vendió"), ("utilidad bruta", "ventas menos costo de ventas"), ("cuentas por cobrar", "dinero que los clientes deben a la empresa"), ("cuadrar", "que el activo sea igual a pasivo más patrimonio")],
    worked=[
        ("Comprobar el cuadre", "Un balance de ejemplo muestra activo $700.000, pasivo $300.000 y patrimonio $400.000. ¿Cuadra?", ["Se suma pasivo más patrimonio: 300.000 + 400.000 = 700.000.", "Ese total es igual al activo."], "Sí, cuadra"),
        ("Resultado del período", "Una librería de ejemplo vendió $900.000, su costo de ventas fue $500.000 y sus gastos de administración $150.000. ¿Cuál fue el resultado?", ["Utilidad bruta = 900.000 − 500.000 = 400.000.", "Resultado = 400.000 − 150.000 = 250.000."], "Ganancia de $250.000"),
    ],
    mistakes=[("Restar los gastos de administración a las ventas antes de calcular la utilidad bruta.", "Se altera el orden: primero se resta el costo de ventas y después los gastos.", "Calcula utilidad bruta y luego resta los gastos de administración."),
              ("Concluir que la empresa puede pagar sus deudas solo porque vendió mucho.", "Para pagar se necesita dinero disponible o cobrable, no solo ventas.", "Compara caja y cuentas por cobrar con lo que se debe.")],
    T=[
        ("abc", "En Administración: ¿qué muestra un balance?", "El activo, el pasivo y el patrimonio en un momento dado", "Solo las ventas de un día", "La lista de personas que trabajan en la empresa", "El balance resume lo que la empresa tiene y debe en un momento; no es un registro de ventas diarias."),
        ("abc", "¿Cómo se comprueba que un balance cuadra?", "El activo es igual al pasivo más el patrimonio", "El pasivo es mayor que el activo", "El patrimonio es igual a las ventas", "Cuadrar significa que se cumple activo = pasivo + patrimonio."),
        ("abc", "¿Qué es la utilidad bruta?", "Las ventas menos el costo de ventas", "Las ventas más los gastos de administración", "El patrimonio menos el pasivo", "La utilidad bruta es lo que queda de las ventas tras restar el costo de lo vendido."),
        ("=", "{F} ¿Cuántos pesos suma el activo de la ficha?", "1500000+2500000+4000000", "Se suman caja, cuentas por cobrar y mercaderías.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suma el pasivo de la ficha?", "2000000+1500000", "Se suman la deuda con proveedores y el préstamo bancario.", " pesos"),
        ("abc", "{F} ¿El balance de la ficha cuadra?", "Sí, porque el activo de $8.000.000 es igual a pasivo más patrimonio", "No, porque el activo es mayor que el patrimonio", "No, porque falta sumar el resultado del mes al activo", "El pasivo de $3.500.000 más el patrimonio de $4.500.000 da $8.000.000, igual al activo."),
        ("=", "{F} ¿Cuántos pesos es la utilidad bruta del mes?", "5000000-3000000", "Utilidad bruta = ventas − costo de ventas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos es el resultado del mes después de los gastos de administración?", "5000000-3000000-1200000", "Resultado = utilidad bruta − gastos de administración.", " pesos"),
        ("abc", "{F} ¿Puede la empresa pagar a sus proveedores solo con el dinero en caja?", "No: la caja de $1.500.000 es menor que los $2.000.000 que debe", "Sí, porque tiene mercaderías por $4.000.000", "Sí, porque el patrimonio es de $4.500.000", "El pago exige dinero disponible; la caja no alcanza, aunque otros activos sumen más."),
        ("abc", "{F} Si los clientes pagan todo lo que deben, ¿alcanzaría el dinero para pagar a los proveedores?", "Sí: caja más cuentas por cobrar suman $4.000.000, más que los $2.000.000 debidos", "No, porque las cuentas por cobrar no son dinero", "No, porque los clientes nunca pagan", "Con lo cobrado se tendrían $4.000.000, que cubren la deuda con proveedores."),
        ("abc", "Un analista dice: «Este mes hubo ganancia, entonces el año completo también será ganancia». ¿Qué observación corresponde?", "Un solo mes no basta para asegurar el resto del año", "Está bien, porque un mes siempre representa al año", "Está bien, porque las ganancias no cambian", "Un período corto limita las conclusiones; se anota esa restricción."),
        ("=", "{F} Si el costo de ventas hubiera sido $4.200.000 con las mismas ventas, ¿cuántos pesos habría sido la utilidad bruta?", "5000000-4200000", "Se resta el nuevo costo de ventas a las ventas.", " pesos"),
        ("abc", "{F} Un colega suma el préstamo bancario al patrimonio «porque es plata que entró». ¿Qué error comete?", "Una deuda es pasivo; sumarla al patrimonio hace que el balance no cuadre", "Ninguno, porque el dinero prestado es de los dueños", "Resta una deuda que debía sumar al activo", "El préstamo es una obligación; clasificarla como patrimonio rompe la ecuación contable."),
    ],
    ctx=("abc", "La gerencia de la ficha dice: «Ganamos este mes, así que repartamos todo». Antes, ¿qué cifra conviene revisar?", "Si caja y cuentas por cobrar alcanzan para las deudas con proveedores y el banco", "El color del informe impreso", "El número de páginas del balance", "Antes de repartir se verifica que la empresa pueda pagar lo que debe."),
    sc=[
        ("En Administración: ¿cómo se calcula la utilidad bruta?", "Ventas menos costo de ventas", "La utilidad bruta aparece antes de descontar gastos de administración."),
        ("¿Qué haces si el balance no cuadra?", "Reviso los documentos de respaldo y las sumas antes de usarlo", "Un balance que no cuadra tiene un error que debe corregirse."),
        ("¿Qué límite anotas al concluir con datos de un solo mes?", "Que no se puede asegurar el resto del año", "Un mes aislado no predice todo el año."),
    ],
    op=("Con la Ficha 3 escribe un informe de seis líneas para la gerencia: (1) total del activo, (2) total del pasivo, (3) si el balance cuadra, (4) resultado del mes, (5) si la caja alcanza para pagar a proveedores y (6) un límite de tu conclusión.\n{F}",
        "Activo total: $8.000.000. Pasivo total: $3.500.000. El balance cuadra con el patrimonio de $4.500.000. El resultado del mes fue una ganancia de $800.000. La caja de $1.500.000 no alcanza para pagar $2.000.000 a proveedores; con lo que deben los clientes sí. Límite: los datos son de un solo mes de ejemplo.",
        ["calcula bien activo, pasivo y resultado", "verifica el cuadre", "interpreta caja frente a deudas", "declara un límite"],
        ["informe de seis líneas con cifras de la ficha"],
        ["no restar los gastos de administración", "concluir sin comparar caja con deudas", "no declarar límites"],
        "Compara las cifras con la ficha. Si el estudiante concluye sin límite, pregunta qué otros datos faltarían."),
    reinforce="Inventa un balance de seis cuentas para un negocio ficticio y comprueba que cuadre.",
    extend="Explica con un ejemplo inventado por qué una empresa con ganancia puede tener problemas para pagar sus deudas.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Importadora Cordillera Ltda. compra un lote de herramientas a un proveedor extranjero ficticio por 2.000 dólares. Tipo de cambio de ejemplo: 1 dólar = 900 pesos. "
     "Flete y seguro de ejemplo: $150.000. Derechos de aduana de ejemplo: $90.000. Luego vende el lote en Chile por $2.800.000 sin IVA. Tasa de IVA de ejemplo: 19 % (la tasa real y las reglas se verifican en la norma vigente).")
build(
    O1, 4, F,
    use="Aprenderé a calcular el costo de una mercadería importada y a usar el IVA débito y el IVA crédito con tasas de ejemplo.",
    prior=["Sé leer un balance y un resultado.", "Sé multiplicar y restar cifras grandes.", "Sé que las normas tributarias se revisan en la norma vigente."],
    explain=[
        "Cuando una empresa importa, el precio viene en una moneda extranjera. Para registrarlo se convierte a pesos con el tipo de cambio: valor en pesos = precio en dólares × tipo de cambio. El costo total de la mercadería importada es ese valor más los gastos necesarios para tenerla en bodega, como el flete (transporte), el seguro y los derechos de aduana.",
        "El IVA es un impuesto que se agrega al precio de las ventas. Cuando la empresa vende cobra IVA y ese monto es su IVA débito; cuando compra con IVA ese monto es su IVA crédito. El IVA a pagar del período es el débito menos el crédito, si el débito es mayor. Las tasas que se usan en este cuaderno son de ejemplo: en la práctica se aplica la tasa de la norma vigente y se respalda con facturas.",
        "Las exportaciones y las importaciones tienen tratamientos tributarios y aduaneros propios, por eso se consulta la norma vigente y al contador antes de decidir. Para comprobar un cálculo se rehace en orden: primero convertir a pesos, luego sumar costos adicionales, después comparar con el precio de venta.",
    ],
    vocab=[("tipo de cambio", "cuántos pesos vale una unidad de moneda extranjera"), ("flete", "costo de transportar la mercadería"), ("derechos de aduana", "pagos asociados a la entrada de mercadería al país"), ("IVA débito", "IVA cobrado en las ventas"), ("IVA crédito", "IVA pagado en las compras"), ("margen", "venta menos costo total")],
    worked=[
        ("Convertir y sumar", "Un taller ficticio compra piezas por 500 dólares con tipo de cambio de ejemplo 800 pesos y paga $40.000 de flete. ¿Cuál es el costo en pesos?", ["Valor en pesos = 500 × 800 = 400.000.", "Costo total = 400.000 + 40.000 = 440.000."], "$440.000"),
        ("IVA a pagar", "En un mes de ejemplo, una tienda tiene IVA débito de $190.000 e IVA crédito de $120.000. ¿Cuánto IVA queda por pagar?", ["IVA a pagar = débito − crédito.", "190.000 − 120.000 = 70.000."], "$70.000"),
    ],
    mistakes=[("Olvidar el flete y los derechos y registrar solo el precio del proveedor.", "El costo de la mercadería en bodega incluye esos gastos necesarios; si se omiten, el margen se ve mayor al real.", "Suma precio en pesos, flete, seguro y derechos."),
              ("Restar el IVA débito del IVA crédito.", "El orden correcto es débito menos crédito; al revés se obtiene un signo erróneo.", "Calcula débito − crédito y revisa si resulta positivo.")],
    T=[
        ("abc", "En Administración: ¿qué es el tipo de cambio?", "Cuántos pesos vale una unidad de moneda extranjera", "El porcentaje de IVA que se cobra", "El costo de transportar la mercadería", "El tipo de cambio convierte monedas; el IVA y el flete son otras cosas."),
        ("abc", "¿Qué es el IVA débito?", "El IVA que la empresa cobra en sus ventas", "El IVA que la empresa pagó en sus compras", "El costo del transporte de la mercadería", "El débito proviene de las ventas; el crédito, de las compras."),
        ("abc", "¿Cuál de estos gastos forma parte del costo de una mercadería importada?", "El flete para traerla a la bodega", "El sueldo de la gerenta por todo el año", "La publicidad de otra línea de productos", "El flete es un gasto necesario para tener la mercadería lista."),
        ("=", "{F} ¿Cuántos pesos vale el lote comprado en dólares, antes de otros costos?", "2000*900", "Valor en pesos = dólares × tipo de cambio de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el lote en total, sumando flete, seguro y derechos?", "2000*900+150000+90000", "Se suma el valor en pesos al flete y a los derechos de la ficha.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de margen deja el lote (venta sin IVA menos costo total)?", "2800000-(2000*900+150000+90000)", "Margen = venta sin IVA − costo total del lote.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de IVA débito genera la venta de $2.800.000 con la tasa de ejemplo?", "2800000*19//100", "IVA débito = venta sin IVA × tasa de ejemplo.", " pesos"),
        ("=", "Una tienda de ejemplo tuvo IVA débito de $532.000 e IVA crédito de $380.000. ¿Cuántos pesos de IVA queda por pagar?", "532000-380000", "IVA a pagar = débito − crédito.", " pesos"),
        ("abc", "Un asistente registra el lote de la ficha solo por el precio del proveedor convertido. ¿Qué efecto tiene?", "El costo queda subestimado y el margen parece mayor al real", "El margen queda subestimado porque se cobra de más", "No cambia nada, porque el flete no importa", "Omitir flete y derechos baja el costo registrado y exagera el margen."),
        ("abc", "{F} Si el tipo de cambio de ejemplo subiera a 950 pesos por dólar, ¿qué pasaría con el costo del lote?", "Subiría, porque cada dólar valdría más pesos", "Bajaría, porque se necesitan menos pesos", "No cambiaría, porque el precio está en dólares", "Un dólar más caro en pesos encarece una compra pactada en dólares."),
        ("abc", "Un proveedor del exterior pide depositarle un pago en una cuenta personal distinta a la de la empresa. ¿Qué corresponde?", "Consultar a la jefatura y al contador antes de pagar, y dejar respaldo", "Pagar de inmediato para no atrasarse", "Pagar y no avisar a nadie para no preocupar", "Un pedido inusual de pago se verifica con la jefatura; evita fraudes y errores."),
        ("=", "{F} Si la venta se hiciera a $2.500.000 sin IVA, ¿cuántos pesos de margen quedarían?", "2500000-(2000*900+150000+90000)", "Se resta el costo total de la ficha al nuevo precio de venta.", " pesos"),
        ("abc", "{F} Para exportar un producto, un compañero afirma: «Se aplica el IVA de ejemplo de la ficha, y no hay que revisar nada más». ¿Qué respondes?", "Que las exportaciones tienen reglas propias y se consulta la norma vigente", "Que tiene razón, porque el IVA es igual en toda operación", "Que no se debe registrar ninguna exportación", "El tratamiento de una exportación se confirma en la norma vigente; la tasa de ejemplo no se generaliza."),
    ],
    ctx=("abc", "Una empresa ficticia compra 300 dólares de repuestos con tipo de cambio de ejemplo de 910 pesos y paga $20.000 de flete. ¿Cuántos pesos cuesta el lote?", "$293.000", "$273.000", "$20.300", "300 × 910 = 273.000; con el flete de 20.000 el costo es 293.000."),
    sc=[
        ("En Administración: ¿cómo se convierte un precio en dólares a pesos?", "Se multiplica por el tipo de cambio", "El valor en pesos es precio en dólares por tipo de cambio."),
        ("¿Qué IVA va primero en la resta para el IVA a pagar?", "El IVA débito", "El IVA a pagar es débito menos crédito."),
        ("¿Qué haces con las tasas de ejemplo en un caso real?", "Las reemplazo por las de la norma vigente", "Las tasas del cuaderno son de ejemplo y no sirven para declarar."),
    ],
    op=("Con la Ficha 4 escribe una hoja de costeo con estas filas: precio en dólares, valor en pesos, flete y seguro, derechos, costo total, precio de venta sin IVA y margen. Agrega una línea que diga qué revisarías en la norma vigente antes de usar estas cifras en una declaración.\n{F}",
        "Precio: 2.000 dólares. Valor en pesos: $1.800.000. Flete y seguro: $150.000. Derechos: $90.000. Costo total: $2.040.000. Venta sin IVA: $2.800.000. Margen: $760.000. Revisaría en la norma vigente la tasa de IVA, el tratamiento de los derechos y el tipo de cambio que corresponde usar.",
        ["convierte correctamente a pesos", "suma todos los costos de la ficha", "calcula el margen", "indica qué verificar en la norma vigente"],
        ["hoja de costeo con siete filas y una línea final"],
        ["omitir flete o derechos", "mezclar dólares con pesos", "dar como definitivas las tasas de ejemplo"],
        "Revisa fila por fila contra la ficha. Si el margen no coincide, pide rehacer el costo total y comparar."),
    reinforce="Convierte tres precios de ejemplo en dólares a pesos con un tipo de cambio que inventes y suma un flete también inventado.",
    extend="Explica con un ejemplo inventado cómo cambia el margen de un lote si el tipo de cambio sube pero el precio de venta se mantiene.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (datos de ejemplo, inventados). Dos ofertas para el mismo lote de herramientas de Importadora Cordillera Ltda. Oferta Alfa (proveedor ficticio): 1.800 dólares, flete y seguro $120.000, derechos $80.000. "
     "Oferta Beta (proveedor ficticio): 1.700 dólares, flete y seguro $230.000, derechos $80.000. Tipo de cambio de ejemplo: 1 dólar = 900 pesos. "
     "Además, el balance de cierre del contador muestra activo $7.900.000, pasivo $3.500.000 y patrimonio $4.500.000.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas con el costo total y a verificar la calidad de una información contable con una lista de control.",
    prior=["Sé calcular el costo de una mercadería importada.", "Sé comprobar si un balance cuadra.", "Sé que la norma vigente se consulta."],
    explain=[
        "Comparar alternativas de compra no es mirar solo el precio del proveedor: se compara el costo total, que suma el valor en pesos, el flete, el seguro y los derechos. Una oferta con precio menor puede resultar más cara si trae un flete mucho mayor. Se calcula cada alternativa con el mismo tipo de cambio y se compara con el mismo criterio.",
        "Verificar la calidad de la información contable significa revisar que sea confiable antes de usarla. La lista de control incluye: cada cifra tiene documento de respaldo; el balance cuadra; las sumas se rehicieron; las cifras de un informe coinciden con las de otro; y los datos están en la moneda y el período correctos. Si algo falla, se corrige con el documento y no se ajusta una cifra al azar.",
        "Cuando hay una diferencia entre dos totales, se calcula su valor y se busca su causa en los registros. La decisión final se anota con el criterio usado y con lo que queda pendiente, por ejemplo consultar con el contador. La información contable se maneja con reserva y solo se comparte con quien corresponde.",
    ],
    vocab=[("costo total", "valor en pesos más flete, seguro y derechos"), ("alternativa", "una de las opciones que se comparan"), ("lista de control", "pauta de revisión de la calidad de un informe"), ("diferencia", "resta entre dos totales que debían ser iguales"), ("criterio", "regla con que se decide entre alternativas"), ("coincidir", "que dos informes muestren la misma cifra")],
    worked=[
        ("Comparar dos ofertas", "Oferta X: 1.000 dólares con flete $60.000; oferta Y: 950 dólares con flete $130.000. Tipo de cambio de ejemplo: 800 pesos. ¿Cuál cuesta menos en total?", ["X: 1.000 × 800 + 60.000 = 860.000.", "Y: 950 × 800 + 130.000 = 890.000; X cuesta menos."], "La oferta X"),
        ("Hallar una diferencia", "Un balance de ejemplo tiene activo $500.000 y pasivo más patrimonio $520.000. ¿Cuál es la diferencia?", ["Se restan los dos totales.", "520.000 − 500.000 = 20.000."], "$20.000"),
    ],
    mistakes=[("Elegir la oferta de menor precio sin sumar fletes y derechos.", "El costo total puede ser mayor aunque el precio inicial sea menor.", "Compara siempre el costo total de cada alternativa."),
              ("Ajustar una cifra del balance para que cuadre sin buscar el documento.", "Se tapa el error y el informe deja de ser confiable.", "Busca la causa de la diferencia en los respaldos y corrígela.")],
    T=[
        ("abc", "En Administración: ¿qué incluye el costo total de una compra importada?", "Valor en pesos, flete, seguro y derechos", "Solo el precio en dólares", "El margen que se espera ganar", "El costo total reúne todo lo necesario para tener la mercadería en bodega."),
        ("abc", "¿Para qué sirve una lista de control de calidad de un informe contable?", "Para revisar que la información sea confiable antes de usarla", "Para decorar el informe", "Para reemplazar los documentos de respaldo", "La lista de control ordena la revisión; no sustituye los respaldos."),
        ("abc", "¿Qué se hace cuando dos totales que debían ser iguales difieren?", "Calcular la diferencia y buscar su causa en los registros", "Cambiar uno de los totales para igualarlos", "Ignorarla si es pequeña", "Se busca la causa con los respaldos; forzar el total oculta el error."),
        ("=", "{F} ¿Cuántos pesos cuesta en total la oferta Alfa?", "1800*900+120000+80000", "Costo total = dólares × tipo de cambio + flete y seguro + derechos.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta en total la oferta Beta?", "1700*900+230000+80000", "Se aplica el mismo cálculo a la oferta Beta.", " pesos"),
        ("abc", "{F} ¿Qué oferta conviene por menor costo total?", "Alfa, porque cuesta menos en total", "Beta, porque su precio en dólares es menor", "Ninguna, porque cuestan exactamente lo mismo", "Alfa suma $1.820.000 y Beta $1.840.000; el precio menor de Beta se pierde por el flete."),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre los costos totales de las dos ofertas?", "(1700*900+230000+80000)-(1800*900+120000+80000)", "Se resta el costo menor al mayor.", " pesos"),
        ("abc", "{F} El balance de cierre del contador muestra activo $7.900.000. ¿Cuadra con pasivo más patrimonio?", "No: pasivo más patrimonio suman $8.000.000", "Sí, porque ambos totales son iguales", "Sí, porque el patrimonio es mayor que el pasivo", "3.500.000 + 4.500.000 = 8.000.000, que difiere de los 7.900.000 del activo."),
        ("=", "{F} ¿Cuántos pesos es la diferencia entre el activo y el pasivo más patrimonio del balance de cierre?", "3500000+4500000-7900000", "Se resta el activo al total de pasivo más patrimonio.", " pesos"),
        ("abc", "{F} Un colega propone subir en $100.000 la caja del balance para que cuadre. ¿Qué corresponde?", "No hacerlo sin documento; revisar las sumas y los respaldos para encontrar el error", "Hacerlo, porque la diferencia coincide con ese valor", "Hacerlo y avisar después a nadie", "Que coincida el monto no prueba la causa; sin documento no se ajusta ninguna cuenta."),
        ("abc", "Un compañero compara dos cotizaciones en monedas distintas sin convertirlas. ¿Qué falla?", "Se mezclan monedas: hay que convertir ambas a pesos con el mismo tipo de cambio", "Nada, porque el valor de las monedas es igual", "Falta sumar el IVA débito de la venta", "Para comparar, ambas cifras deben estar en la misma moneda y con el mismo tipo de cambio."),
        ("abc", "{F} Si el flete de la oferta Beta bajara a $100.000, ¿cuál sería la oferta más barata?", "Beta, porque su costo total sería menor", "Alfa, porque su precio en dólares es menor", "Serían iguales", "Beta costaría 1.700×900+100.000+80.000 = 1.710.000, menos que Alfa."),
        ("abc", "El contador entrega un informe cuyo total no coincide con el del informe anterior de la misma fecha. ¿Qué haces antes de usarlo?", "Aviso al contador y pido verificar el cambio con los documentos", "Uso el que tenga la cifra más alta", "Uso el que tenga la cifra más baja", "Los informes de la misma fecha deben coincidir; se pide verificar antes de decidir."),
    ],
    ctx=("abc", "Antes de entregar un informe a la gerencia, una asistente repasa cuatro puntos: respaldos, cuadre del balance, sumas rehechas y moneda correcta. ¿Qué está aplicando?", "Una lista de control de calidad", "Un nuevo tipo de impuesto", "Un cambio de moneda", "Revisar respaldos, cuadre y sumas es una lista de control antes de entregar."),
    sc=[
        ("En Administración: ¿qué se compara para elegir entre dos proveedores?", "El costo total de cada oferta", "El costo total incluye flete, seguro y derechos."),
        ("¿Qué haces si el balance no cuadra?", "Busco la causa en los documentos", "No se fuerza un total: se encuentra el error."),
        ("¿Por qué se usa el mismo tipo de cambio al comparar?", "Para que la comparación sea justa", "Con tipos distintos las ofertas no serían comparables."),
    ],
    op=("Con la Ficha 5 escribe una recomendación de cinco líneas: cuánto cuesta cada oferta en total, cuál recomiendas, qué diferencia hay y qué puntos de la lista de control aplicarías antes de comprar. Agrega qué harías con la diferencia del balance de cierre.\n{F}",
        "Alfa cuesta $1.820.000 y Beta $1.840.000. Recomiendo Alfa, que es $20.000 más barata en total. Revisaría respaldos, tipo de cambio y sumas antes de comprar. El balance de cierre tiene una diferencia de $100.000: pediría al contador revisar los registros con sus documentos.",
        ["calcula ambos costos totales", "elige con un criterio explícito", "usa la lista de control", "no ajusta cifras sin respaldo"],
        ["recomendación de cinco líneas con cifras"],
        ["comparar solo precios en dólares", "forzar el cuadre del balance", "mezclar monedas"],
        "Comprueba los costos totales de la ficha. Si el estudiante recomienda sin criterio, pide que nombre cuál usó."),
    reinforce="Compara en papel dos cotizaciones de ejemplo que inventes, sumando todos los costos, y elige una con un criterio escrito.",
    extend="Explica con un ejemplo inventado por qué una diferencia pequeña en un balance igual debe investigarse.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (caso de ejemplo, inventado). Empresa ficticia «Distribuidora Pampa Verde Ltda.». Plan estratégico del año (resumen de ejemplo): aumentar en un 10 % las ventas a pequeños comercios. "
     "La jefa del área de ventas, Valeria, debe elaborar el programa operativo del trimestre con un equipo de 4 personas (2 vendedores, 1 asistente y 1 encargado de bodega). "
     "Riesgos que Valeria anotó: tareas sin responsable, personas con demasiadas horas seguidas, atrasos por falta de insumos.")
build(
    O2, 1, F,
    use="Aprenderé qué es un programa de actividades operativas, cómo se relaciona con el plan estratégico y con las orientaciones de la jefatura, y qué riesgos conviene prever.",
    prior=["Sé sumar horas y calcular en días.", "Sé la diferencia entre meta y actividad.", "Conozco los cargos de una empresa."],
    explain=[
        "El plan estratégico de gestión dice hacia dónde quiere ir la empresa en un período largo. El programa operativo baja ese rumbo a un departamento o área: qué actividades se harán, quién las hará, con qué recursos y en qué fechas. Se elabora siguiendo las orientaciones de la jefatura, que fijan la meta, el plazo y los límites del área.",
        "Un programa operativo considera cinco elementos: recursos humanos (las personas y sus horas), insumos (lo que se consume, como papel o mercaderías), equipamiento (computadores, vehículos u otros equipos), distribución temporal (cuándo se hace cada actividad) y proyección de resultados (qué se espera lograr y cómo se medirá). Faltar en uno de ellos deja el programa incompleto.",
        "Elaborar el programa tiene riesgos que se previenen desde el diseño: tareas sin responsable, jornadas sobrecargadas que dañan la salud y la calidad, atrasos por falta de insumos y metas que no se pueden medir. El programa es un documento de trabajo que la jefatura revisa y aprueba; quien lo elabora no cambia por su cuenta las metas fijadas.",
    ],
    vocab=[("plan estratégico", "rumbo de la empresa para un período largo"), ("programa operativo", "plan de actividades concretas de un área"), ("recursos humanos", "personas que trabajan y sus horas"), ("insumo", "material que se consume al trabajar"), ("equipamiento", "equipos y herramientas que se usan"), ("proyección de resultados", "lo que se espera lograr y cómo se medirá")],
    worked=[
        ("De plan a programa", "El plan de una librería ficticia dice «mejorar la atención al cliente». ¿Qué actividad operativa puede derivarse?", ["Una actividad operativa es concreta, con responsable y fecha.", "Por ejemplo, «responder las consultas en menos de 24 horas, a cargo de la asistente»."], "Responder consultas en menos de 24 horas, con responsable"),
        ("Clasificar un recurso", "En el programa de la librería aparece «un computador para el registro». ¿Es insumo o equipamiento?", ["Un computador no se consume al usarlo.", "Los equipos que se usan repetidamente son equipamiento."], "Equipamiento"),
    ],
    mistakes=[("Escribir actividades sin responsable ni fecha.", "No se puede controlar lo que no tiene persona a cargo ni plazo.", "Asigna a cada actividad un responsable y un período."),
              ("Programar a una persona con más horas de las que tiene disponibles.", "Genera atrasos, errores y cansancio.", "Calcula las horas disponibles antes de repartir tareas.")],
    T=[
        ("abc", "En Administración: ¿qué es un programa operativo?", "Un plan de actividades concretas de un área, con responsables, recursos y fechas", "El rumbo general de la empresa para muchos años", "Una lista de precios de los productos", "El programa operativo concreta las actividades de un área; el rumbo general es el plan estratégico."),
        ("abc", "{F} ¿Qué meta del plan estratégico debe apoyar el programa de Valeria?", "Aumentar un 10 % las ventas a pequeños comercios", "Contratar a diez personas más", "Cambiar el nombre de la empresa", "La ficha indica que la meta del plan es aumentar las ventas a pequeños comercios."),
        ("abc", "¿Cuál de estos es un insumo?", "El papel que se consume al imprimir", "El computador del escritorio", "La camioneta de reparto", "El insumo se consume al trabajar; el computador y la camioneta son equipamiento."),
        ("abc", "{F} ¿Cuántas personas forman el equipo de Valeria?", "Cuatro", "Tres", "Cinco", "La ficha indica 2 vendedores, 1 asistente y 1 encargado de bodega: cuatro personas."),
        ("abc", "¿Qué elemento del programa responde a «cuándo se hace cada actividad»?", "La distribución temporal", "La proyección de resultados", "El equipamiento", "La distribución temporal ordena las actividades en el tiempo."),
        ("abc", "¿Qué elemento responde a «qué se espera lograr»?", "La proyección de resultados", "Los insumos", "Los recursos humanos", "La proyección dice qué se espera y cómo se medirá."),
        ("=", "{F} El trimestre tiene 12 semanas y el equipo trabaja 4 personas. ¿Cuántas semanas-persona hay disponibles, sin considerar permisos?", "12*4", "Semanas-persona = semanas × personas.", " semanas-persona"),
        ("=", "Un vendedor de ejemplo tiene 40 horas semanales disponibles y le asignan 12 horas de visitas, 8 de reuniones y 10 de informes. ¿Cuántas horas le quedan libres?", "40-12-8-10", "Horas libres = disponibles menos asignadas.", " horas"),
        ("abc", "{F} Valeria anota «bodega: preparar pedidos» sin nombrar a nadie. ¿Qué riesgo de su lista aparece?", "Una tarea sin responsable", "Una jornada sobrecargada", "Una falta de insumos", "Si no hay nombre, nadie responde por la tarea."),
        ("abc", "Un jefe pide un programa para el trimestre y la elaboradora decide por su cuenta cambiar la meta a una más fácil. ¿Qué corresponde?", "Mantener la meta fijada y plantear sus dudas a la jefatura", "Cambiarla porque conoce mejor el trabajo", "Eliminar la meta del documento", "La meta la fija la jefatura; se conversa y no se cambia por cuenta propia."),
        ("abc", "Un programa asigna 55 horas semanales a una persona con 40 disponibles. ¿Cuál es el problema principal?", "Sobrecarga: afecta la salud y la calidad del trabajo", "El programa está demasiado ordenado", "Faltan colores en la tabla", "Pasar de las horas disponibles genera cansancio, errores y atrasos."),
        ("abc", "Se programan visitas a clientes con 20 carpetas de catálogos, pero solo hay 8. ¿Qué se debe corregir?", "Los insumos: faltan catálogos para las visitas", "El equipamiento: sobran vehículos", "La proyección de resultados: es demasiado alta", "Con menos catálogos que visitas faltan insumos."),
        ("abc", "Un compañero dice que el programa solo lo lee quien lo escribe. ¿Qué respondes?", "Lo revisa y aprueba la jefatura y lo usa el equipo", "Es cierto, es privado del autor", "Se debe esconder para que no lo critiquen", "El programa es un documento de trabajo compartido con la jefatura y el equipo."),
    ],
    ctx=("abc", "Valeria necesita decidir si incluye una capacitación de ventas de dos días en el trimestre. ¿Qué debe revisar primero?", "Si hay horas disponibles del equipo y si la jefatura la autoriza", "Si la capacitación tiene un nombre atractivo", "Si otras empresas del rubro hacen lo mismo", "Se revisan las horas del equipo y la autorización de la jefatura antes de programar."),
    sc=[
        ("En Administración: ¿cuáles son los cinco elementos de un programa operativo?", "Recursos humanos, insumos, equipamiento, distribución temporal y proyección de resultados", "El programa los incluye todos para estar completo."),
        ("¿Quién fija la meta del programa?", "La jefatura, según el plan estratégico", "El programa baja la meta de la jefatura, no la inventa."),
        ("¿Qué riesgo trae asignar más horas de las disponibles?", "Sobrecarga, errores y atrasos", "El cansancio baja la calidad y retrasa las entregas."),
    ],
    op=("Con la Ficha 6, escribe la primera hoja del programa del trimestre: la meta que apoya, los cinco elementos (nombra al menos un ejemplo de cada uno usando solo los cargos de la ficha) y dos riesgos con una medida preventiva para cada uno.\n{F}",
        "Meta: aumentar las ventas a pequeños comercios. Recursos humanos: 2 vendedores, 1 asistente y 1 encargado de bodega. Insumos: catálogos impresos. Equipamiento: computador y camioneta. Distribución: visitas semanales. Resultados: 10 % más de ventas. Riesgo: tareas sin responsable; medida: nombrar a una persona por tarea. Riesgo: sobrecarga; medida: sumar las horas antes de asignarlas.",
        ["relaciona el programa con la meta", "nombra los cinco elementos", "usa los cargos de la ficha", "propone medidas preventivas"],
        ["hoja con meta, cinco elementos y dos riesgos con medida"],
        ["omitir un elemento", "inventar personas que la ficha no trae", "decir riesgos sin medida"],
        "Marca los cinco elementos en la hoja. Si falta uno, pide que lo agregue con un ejemplo de la ficha."),
    reinforce="Escribe tres actividades operativas de un quiosco ficticio, cada una con responsable y fecha.",
    extend="Explica con un ejemplo inventado cómo cambiaría el programa si el plan estratégico pidiera reducir costos en lugar de aumentar ventas.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (formatos de ejemplo, inventados) de «Distribuidora Pampa Verde Ltda.». Formato 1, cuadro de actividades: columnas Actividad, Responsable, Inicio, Término, Horas. "
     "Formato 2, carta Gantt: calendario en que cada actividad es una barra que va de su fecha de inicio a la de término. Formato 3, cuadro de recursos: lista de personas, insumos y equipos de cada actividad. "
     "Formato 4, ficha de indicadores: meta, indicador (cómo se mide), valor de partida y valor esperado. Ejemplo de indicador: «visitas a comercios por semana».")
build(
    O2, 2, F,
    use="Aprenderé los documentos del programa operativo (cuadro de actividades, carta Gantt, cuadro de recursos e indicadores) y qué rol cumple cada persona al elaborarlo.",
    prior=["Sé qué es un programa operativo.", "Sé calcular horas y semanas.", "Sé leer un calendario."],
    explain=[
        "El programa operativo se escribe en documentos con una función clara. El cuadro de actividades lista qué se hará, quién responde, cuándo empieza y termina y cuántas horas toma. La carta Gantt dibuja cada actividad como una barra en un calendario y deja ver qué actividades se superponen. El cuadro de recursos detalla las personas, insumos y equipos que necesita cada actividad. La ficha de indicadores dice qué meta se busca y cómo se medirá.",
        "Un indicador es una medida que permite saber si se avanza hacia la meta, por ejemplo «visitas a comercios por semana». Un buen indicador es claro, medible con un dato que se puede registrar y tiene un valor de partida y un valor esperado. La distribución temporal usa fechas y duraciones: la duración es el tiempo que toma una actividad, y la holgura es un margen que se deja para imprevistos.",
        "Los roles son parte del programa. La jefatura fija metas y aprueba; quien elabora el programa organiza la información y consulta lo que falte; los responsables de cada actividad entregan datos reales de sus horas. Si un dato no existe, se anota como supuesto y se informa; no se inventa para completar el cuadro.",
    ],
    vocab=[("carta Gantt", "calendario que muestra cada actividad como una barra"), ("indicador", "medida que muestra el avance hacia la meta"), ("responsable", "persona que responde por una actividad"), ("duración", "tiempo que toma una actividad"), ("holgura", "margen para imprevistos"), ("supuesto", "dato no confirmado que se declara como tal")],
    worked=[
        ("Elegir el documento", "Quieres ver si dos actividades de una oficina ficticia se superponen en el calendario. ¿Qué formato sirve?", ["Se necesita ver barras en un calendario.", "Eso lo muestra la carta Gantt."], "La carta Gantt"),
        ("Duración", "Una actividad de ejemplo empieza el lunes 3 y termina el viernes 7 del mismo mes. ¿Cuántos días hábiles dura?", ["Se cuentan lunes, martes, miércoles, jueves y viernes.", "Son 5 días."], "5 días hábiles"),
    ],
    mistakes=[("Usar como indicador «mejorar el servicio».", "No se puede medir con un dato claro.", "Define un indicador medible, como «reclamos por mes», con valor de partida y valor esperado."),
              ("Inventar las horas de una actividad para completar el cuadro.", "Una cifra inventada engaña a la jefatura.", "Pregunta al responsable o anota el dato como supuesto.")],
    T=[
        ("abc", "En Administración: ¿qué muestra una carta Gantt?", "Cada actividad como una barra en un calendario", "Solo la lista de personas del equipo", "La deuda de la empresa", "La carta Gantt ordena las actividades en el tiempo."),
        ("abc", "{F} ¿Qué formato indica cuántas horas toma cada actividad y quién responde?", "El cuadro de actividades (Formato 1)", "La ficha de indicadores (Formato 4)", "El cuadro de recursos (Formato 3)", "El Formato 1 trae columnas de Responsable y Horas."),
        ("abc", "¿Qué es un indicador?", "Una medida que permite saber si se avanza hacia la meta", "Un permiso firmado por la jefatura", "El nombre del área de la empresa", "Los indicadores miden avance; no son permisos ni nombres."),
        ("abc", "{F} ¿Cuál de estos es un indicador bien definido?", "Visitas a comercios por semana", "Mejorar el servicio", "Ser una buena empresa", "El primero se puede contar; los otros dos son deseos sin medida."),
        ("abc", "¿Qué es la holgura en un programa?", "Un margen de tiempo para imprevistos", "El sueldo adicional de un trabajador", "Una actividad sin responsable", "La holgura es tiempo de reserva para imprevistos."),
        ("abc", "{F} ¿Qué formato detalla qué personas, insumos y equipos necesita cada actividad?", "El cuadro de recursos (Formato 3)", "La carta Gantt (Formato 2)", "El cuadro de actividades (Formato 1)", "El Formato 3 lista los recursos de cada actividad."),
        ("=", "Una actividad de ejemplo tiene 3 personas que dedican 6 horas cada una. ¿Cuántas horas-persona suma?", "3*6", "Horas-persona = personas × horas por persona.", " horas-persona"),
        ("=", "Un indicador de ejemplo parte en 15 visitas por semana y la meta es llegar a 24. ¿Cuántas visitas más por semana se esperan?", "24-15", "Aumento esperado = valor esperado − valor de partida.", " visitas"),
        ("=", "Una actividad de ejemplo empieza el día 6 y termina el día 17 del mismo mes, contando ambos días. ¿Cuántos días corridos dura?", "17-6+1", "Se cuenta también el día de inicio.", " días"),
        ("abc", "Un responsable no sabe cuántas horas tomará una actividad nueva. ¿Qué corresponde en el cuadro?", "Anotar un supuesto declarado y confirmarlo después", "Escribir una cifra al azar sin avisar", "Dejar la actividad fuera del programa para siempre", "Un dato dudoso se declara como supuesto; así la jefatura sabe qué confirmar."),
        ("abc", "Dos actividades de la carta Gantt usan a la misma persona en la misma semana y suman 55 horas, y la persona tiene 40 disponibles. ¿Qué debe hacerse?", "Reprogramar o repartir tareas para no pasar de las horas disponibles", "Dejarlo así, porque la carta se ve ordenada", "Quitar la carta Gantt", "Superponer más horas que las disponibles genera sobrecarga."),
        ("abc", "{F} Valeria elige como indicador «visitas a comercios por semana». ¿Qué le falta para completar su ficha?", "Un valor de partida y un valor esperado", "Un dibujo del logo", "El nombre de todos los clientes", "La ficha pide valor de partida y valor esperado para medir el avance."),
        ("abc", "Un compañero dice que la jefatura solo firma el programa sin revisarlo. ¿Qué respondes?", "La jefatura fija metas y aprueba, por eso lo revisa", "Tiene razón, no lo lee", "La jefatura debe elaborarlo todo sola", "Aprobar supone revisar que el programa cumpla metas y recursos."),
    ],
    ctx=("abc", "Una asistente quiere avisar al equipo cuándo cae cada actividad del trimestre. ¿Qué documento imprimiría para pegarlo en la pared?", "La carta Gantt", "La ficha de indicadores", "El cuadro de recursos", "La carta Gantt muestra las fechas de todas las actividades de un vistazo."),
    sc=[
        ("En Administración: ¿qué indica la duración de una actividad?", "El tiempo que toma", "La duración se usa para ubicar la actividad en el calendario."),
        ("¿Qué formato mide el avance hacia la meta?", "La ficha de indicadores", "Allí se anotan la meta, el indicador y los valores."),
        ("¿Qué haces si un dato no existe?", "Lo declaro como supuesto y lo confirmo", "No se inventan datos; se declaran los supuestos."),
    ],
    op=("Con la Ficha 7, completa un cuadro de actividades con tres filas para el área de ventas de «Distribuidora Pampa Verde» (por ejemplo: visitas a comercios, registro de pedidos y control de bodega). Usa las columnas del Formato 1 y agrega un indicador con valor de partida y valor esperado.\n{F}",
        "Actividad 1: visitas a comercios; responsable: vendedor 1; inicio día 3; término día 28; 80 horas. Actividad 2: registro de pedidos; responsable: asistente; inicio día 3; término día 28; 60 horas. Actividad 3: control de bodega; responsable: encargado de bodega; inicio día 5; término día 26; 40 horas. Indicador: visitas por semana; partida 15; esperado 24. Supuesto: horas confirmadas por cada responsable.",
        ["usa las columnas del formato", "pone responsable y fechas", "define un indicador medible", "declara supuestos si los hay"],
        ["cuadro de tres filas y un indicador"],
        ["omitir responsables", "indicadores sin medida", "horas inventadas sin declarar"],
        "Revisa que las tres filas tengan todas las columnas. Si un dato es un supuesto y no está declarado, pide que lo marque."),
    reinforce="Dibuja en papel una carta Gantt simple de tres actividades en cuatro semanas, con barras.",
    extend="Explica con un ejemplo inventado por qué una actividad sin indicador es difícil de evaluar.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (caso de ejemplo, inventado) del área de ventas de «Distribuidora Pampa Verde Ltda.». Programa borrador del trimestre (12 semanas). Actividad A, visitas a comercios: vendedor 1 y vendedor 2, 24 horas semanales en total, semanas 1 a 12. "
     "Actividad B, registro de pedidos: asistente, 15 horas semanales, semanas 1 a 12. Actividad C, preparación de pedidos: encargado de bodega, 30 horas semanales, semanas 1 a 12. "
     "Actividad D, capacitación de ventas: cada persona del equipo, 16 horas en la semana 6. Horas semanales disponibles por persona: 40. El único camión de reparto está reservado para el área de compras en las semanas 5 y 6. Meta: 10 % más de ventas.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un programa borrador en papel: encontrar sobrecargas, conflictos de recursos y vacíos antes de proponerlo a la jefatura.",
    prior=["Sé qué elementos tiene un programa operativo.", "Sé calcular horas y capacidad.", "Sé leer una tabla de actividades."],
    explain=[
        "Analizar un programa borrador es revisarlo con preguntas fijas. Primero la carga: se suman las horas asignadas a cada persona por semana y se comparan con sus horas disponibles. Segundo los recursos: se verifica que cada insumo y equipo exista cuando se necesita y que no esté reservado para otra actividad. Tercero el tiempo: se revisan las superposiciones y la holgura. Cuarto los resultados: se comprueba que haya indicadores para la meta.",
        "La capacidad es la cantidad de trabajo que una persona o un equipo puede hacer en un período. Hay sobrecarga cuando las horas asignadas superan las disponibles. Hay un conflicto de recursos cuando dos actividades necesitan el mismo equipo al mismo tiempo. Una dependencia ocurre cuando una actividad no puede empezar hasta que otra termine.",
        "El resultado del análisis es una lista de hallazgos con una propuesta para cada uno, siempre sujeta a la aprobación de la jefatura. No se corrige el programa escondiendo el problema ni quitando actividades que la jefatura pidió; se propone un ajuste y se informa su efecto.",
    ],
    vocab=[("capacidad", "trabajo que se puede hacer en un período"), ("sobrecarga", "horas asignadas mayores a las disponibles"), ("conflicto de recursos", "dos actividades piden el mismo equipo a la vez"), ("dependencia", "una actividad espera a que termine otra"), ("hallazgo", "problema encontrado al revisar"), ("ajuste", "cambio propuesto para resolver un hallazgo")],
    worked=[
        ("Revisar la carga", "Una persona de ejemplo tiene 40 horas semanales y le asignan 18 horas de atención, 14 de reuniones y 12 de informes. ¿Está sobrecargada?", ["Se suman 18 + 14 + 12 = 44.", "44 es mayor que 40."], "Sí, por 4 horas"),
        ("Detectar un conflicto", "Dos actividades de una oficina ficticia necesitan la única sala de reuniones el martes de 10 a 12. ¿Qué ocurre?", ["Ambas piden el mismo recurso a la misma hora.", "Eso es un conflicto de recursos."], "Conflicto de recursos"),
    ],
    mistakes=[("Resolver la sobrecarga reduciendo horas de una actividad sin avisar.", "La actividad puede dejar de cumplir la meta y la jefatura no lo sabe.", "Propón un ajuste y su efecto, y espera la aprobación."),
              ("Mirar solo el total del equipo y no la carga de cada persona.", "El equipo puede tener horas libres mientras una persona está sobrecargada.", "Calcula las horas por persona.")],
    T=[
        ("abc", "En Administración: ¿qué es una sobrecarga?", "Horas asignadas mayores a las que la persona tiene disponibles", "Un exceso de insumos en la bodega", "Un error de ortografía en el programa", "La sobrecarga compara horas asignadas con horas disponibles."),
        ("abc", "¿Qué es un conflicto de recursos?", "Dos actividades que necesitan el mismo equipo al mismo tiempo", "Una discusión entre dos personas del equipo", "Una actividad sin indicador", "El conflicto de recursos ocurre cuando un mismo recurso es pedido a la vez."),
        ("abc", "{F} ¿Cuántas horas semanales dispone cada persona del área?", "40", "35", "45", "La ficha indica 40 horas semanales disponibles por persona."),
        ("abc", "{F} ¿En qué semanas no se puede contar con el único camión de reparto?", "En las semanas 5 y 6", "En las semanas 1 y 2", "En las semanas 11 y 12", "La ficha dice que el camión está reservado para otra área en las semanas 5 y 6."),
        ("=", "{F} ¿Cuántas horas semanales suman las actividades A, B y C?", "24+15+30", "Se suman las horas semanales de las tres actividades permanentes.", " horas"),
        ("=", "{F} ¿Cuántas horas semanales dispone el equipo completo de 4 personas?", "4*40", "Capacidad semanal = personas × horas disponibles por persona.", " horas"),
        ("=", "{F} ¿Cuántas horas semanales libres le quedan al equipo en las semanas sin capacitación?", "4*40-(24+15+30)", "Libres = capacidad del equipo menos horas asignadas.", " horas"),
        ("=", "{F} En la semana 6 se suma la capacitación de 16 horas por persona. ¿Cuántas horas libres quedan esa semana en el equipo?", "4*40-(24+15+30)-4*16", "Se resta también la capacitación de las cuatro personas a la capacidad.", " horas"),
        ("abc", "{F} ¿Cuántas horas tiene asignadas el encargado de bodega en la semana 6 y está sobrecargado?", "46 horas (30 de la actividad C y 16 de capacitación): sí, supera las 40 disponibles", "30 horas: no, porque la capacitación no se suma a sus tareas", "46 horas: no, porque la capacitación es obligatoria y no cuenta", "30 + 16 = 46, que supera las 40 horas disponibles; que sea obligatoria no elimina la sobrecarga."),
        ("abc", "{F} Valeria propone eliminar la capacitación porque no hay horas. ¿Qué es lo más adecuado?", "Proponer a la jefatura un ajuste, como mover tareas de esa semana, y esperar su respuesta", "Eliminarla sin avisar", "Pedir a la gente que trabaje más de 40 horas sin registrarlo", "Los ajustes se proponen y la jefatura decide; esconder horas extras es un riesgo."),
        ("abc", "Una actividad de ejemplo no puede empezar hasta que termine otra. ¿Cómo se llama esa relación?", "Dependencia", "Holgura", "Sobrecarga", "Una actividad que espera a otra tiene dependencia con ella."),
        ("abc", "{F} Falta un dato en el borrador: ¿qué parte revisarías para saber si el programa busca la meta?", "Los indicadores: no hay ninguno que mida el aumento de ventas", "El color de la portada", "El nombre de la camioneta", "La ficha trae una meta pero ningún indicador para medirla."),
        ("abc", "El analista encuentra tres hallazgos y los resuelve borrándolos del documento sin avisar. ¿Qué falla?", "No informa a la jefatura ni deja registro de los cambios", "Nada, porque el programa queda más corto", "Debió agregar más actividades", "Un hallazgo se informa con una propuesta; borrarlo oculta el problema."),
    ],
    ctx=("abc", "Una asistente nota que la semana 6 tiene la capacitación y que un vendedor tiene visitas programadas el mismo día. ¿Qué hallazgo anota?", "Superposición de actividades de una misma persona", "Falta de insumos", "Error de digitación en el nombre de la empresa", "Dos actividades de la misma persona en el mismo horario son una superposición."),
    sc=[
        ("En Administración: ¿cómo se detecta una sobrecarga?", "Comparando horas asignadas con horas disponibles de cada persona", "Se calcula la carga de cada persona por separado."),
        ("¿Qué es un hallazgo?", "Un problema encontrado al revisar el programa", "Cada hallazgo lleva una propuesta de ajuste."),
        ("¿Quién aprueba los ajustes?", "La jefatura", "El analista propone; la jefatura decide."),
    ],
    op=("Con la Ficha 8, escribe un informe de análisis de cinco líneas: (1) capacidad del equipo, (2) horas asignadas por semana, (3) horas libres, (4) un hallazgo con su propuesta de ajuste y (5) qué indicador falta para medir la meta.\n{F}",
        "Capacidad semanal del equipo: 160 horas. Horas asignadas: 69 semanales, y 133 en la semana 6 con la capacitación. Horas libres: 91, y 27 en la semana 6. Hallazgo: el encargado de bodega llega a 46 horas esa semana; propuesta: repartir parte de sus tareas, sujeto a aprobación. Falta un indicador de ventas a pequeños comercios.",
        ["calcula capacidad, asignación y libres", "detecta un hallazgo real de la ficha", "propone un ajuste sin decidir por la jefatura", "nota el indicador faltante"],
        ["informe de cinco líneas con cifras"],
        ["sumar horas por persona incorrectamente", "no proponer ajuste", "ocultar un hallazgo"],
        "Comprueba las cifras con la ficha. Si el estudiante corrige el programa por su cuenta, pide que lo convierta en propuesta."),
    reinforce="Revisa en papel el horario semanal de una persona ficticia y marca si hay sobrecarga o superposición.",
    extend="Explica con un ejemplo inventado cómo cambia un hallazgo si se agrega una persona al equipo.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (datos de ejemplo, inventados). Programa de apoyo administrativo de «Servicios Maitén Ltda.» para 8 semanas. Equipo: 3 personas, 40 horas semanales cada una; costo de ejemplo de una hora de trabajo: $5.000. "
     "Actividades: orden del archivo, 90 horas; atención de consultas, 120 horas; digitación de facturas, 150 horas. Insumos de ejemplo: 4 cajas de carpetas a $12.000 cada una y 6 resmas de papel a $4.500 cada una. "
     "Equipamiento: 2 computadores ya existentes (sin costo adicional). Meta: dejar al día el archivo y las facturas en 8 semanas.")
build(
    O2, 4, F,
    use="Aprenderé a calcular horas, costos de insumos y fechas de un programa con datos de ejemplo, y a decidir si el programa cabe en el tiempo y el presupuesto.",
    prior=["Sé qué es una carta Gantt.", "Sé calcular capacidad semanal.", "Sé multiplicar y dividir cifras simples."],
    explain=[
        "Para saber si un programa es posible se compara la demanda de trabajo con la capacidad. La demanda es la suma de horas que necesitan las actividades; la capacidad es horas por persona × personas × semanas. Si la demanda es menor o igual a la capacidad, el programa cabe; si la supera, hay que agregar tiempo, personas o reducir actividades con aprobación de la jefatura.",
        "El costo de recursos humanos de una actividad es horas × costo por hora. El costo de insumos es cantidad × precio unitario. El presupuesto del programa es la suma de ambos, más los equipos nuevos si los hay. Todas las cifras de este cuaderno son de ejemplo; en un caso real vienen de documentos de la empresa.",
        "La distribución temporal se calcula con la duración: semanas necesarias = horas de la actividad ÷ horas semanales que se le dedican. Siempre se agrega holgura para imprevistos como licencias o fallas, y se anota cómo se medirá el resultado, por ejemplo «porcentaje de facturas digitadas».",
    ],
    vocab=[("demanda de trabajo", "horas que necesitan las actividades"), ("capacidad", "horas que puede entregar el equipo"), ("costo por hora", "valor de ejemplo de una hora de trabajo"), ("presupuesto", "suma de costos del programa"), ("holgura", "margen para imprevistos"), ("porcentaje de avance", "parte del trabajo ya hecha, sobre 100")],
    worked=[
        ("Demanda y capacidad", "Un equipo de ejemplo de 2 personas con 40 horas semanales, durante 4 semanas, debe hacer 280 horas de trabajo. ¿Alcanza?", ["Capacidad = 2 × 40 × 4 = 320 horas.", "La demanda de 280 es menor que 320."], "Sí, sobran 40 horas"),
        ("Costo de un insumo", "Una oficina ficticia compra 5 cajas de archivo a $3.000 cada una. ¿Cuánto cuestan?", ["Costo = cantidad × precio.", "5 × 3.000 = 15.000."], "$15.000"),
    ],
    mistakes=[("Comparar horas semanales con horas totales sin convertir.", "Se mezclan unidades distintas y el resultado engaña.", "Convierte todo a horas totales del programa."),
              ("No dejar holgura y programar al 100 % de la capacidad.", "Cualquier licencia o falla atrasa el programa.", "Reserva un margen para imprevistos.")],
    T=[
        ("abc", "En Administración: ¿qué es la capacidad de un equipo en un programa?", "Las horas que puede entregar en el período", "Las horas que piden las actividades", "El precio de los insumos", "La capacidad es oferta de horas; lo que piden las actividades es la demanda."),
        ("abc", "¿Cómo se calcula el costo de personas de una actividad?", "Horas multiplicadas por el costo por hora", "Horas divididas por el número de semanas", "Insumos más equipos", "El costo de personal es horas por costo de la hora."),
        ("abc", "¿Para qué se deja holgura en un programa?", "Para absorber imprevistos como licencias o fallas", "Para pagar menos sueldos", "Para evitar medir los resultados", "La holgura protege los plazos frente a imprevistos."),
        ("=", "{F} ¿Cuántas horas suma la demanda de trabajo de las tres actividades?", "90+120+150", "La demanda es la suma de horas de las actividades.", " horas"),
        ("=", "{F} ¿Cuántas horas de capacidad tiene el equipo durante las 8 semanas?", "3*40*8", "Capacidad = personas × horas semanales × semanas.", " horas"),
        ("abc", "{F} ¿Alcanza la capacidad para la demanda del programa?", "Sí, porque 960 horas de capacidad superan las 360 horas de demanda", "No, porque la demanda supera la capacidad", "No se puede saber sin conocer el sueldo", "La capacidad es 960 horas y la demanda 360; el programa cabe y queda holgura."),
        ("=", "{F} ¿Cuántos pesos cuesta en personal la actividad «digitación de facturas»?", "150*5000", "Costo de personal = horas × costo por hora de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan las 4 cajas de carpetas y las 6 resmas de papel en total?", "4*12000+6*4500", "Se suma cada insumo, calculado como cantidad por precio.", " pesos"),
        ("=", "{F} ¿Cuántos pesos suma el presupuesto del programa (personal de las tres actividades más insumos)?", "(90+120+150)*5000+4*12000+6*4500", "Presupuesto = costo de personal + costo de insumos.", " pesos"),
        ("=", "{F} Si el equipo dedica a «orden del archivo» 15 horas semanales en total, ¿cuántas semanas necesita para las 90 horas?", "90//15", "Semanas = horas de la actividad ÷ horas semanales dedicadas.", " semanas"),
        ("abc", "{F} Un compañero propone programar las 8 semanas completas al 100 % de capacidad. ¿Qué riesgo tiene?", "Sin holgura, cualquier imprevisto atrasa el programa", "Ninguno, porque la capacidad nunca falla", "Se pagan menos horas", "Sin margen para licencias o fallas, los atrasos se vuelven inevitables."),
        ("=", "{F} Si el equipo bajara a 2 personas, ¿cuántas horas de capacidad tendría en las 8 semanas?", "2*40*8", "Se rehace el cálculo con 2 personas.", " horas"),
        ("abc", "{F} Con 2 personas, ¿alcanza la capacidad para las 360 horas de demanda?", "Sí, porque 640 horas son más que 360", "No, porque con 2 personas la demanda sube a 640 horas", "No se puede calcular con 2 personas", "640 horas de capacidad cubren las 360 de demanda."),
    ],
    ctx=("abc", "La jefatura pide agregar 700 horas de otra tarea al programa de la ficha. ¿Qué conviene responder?", "Con 960 horas de capacidad y 360 de demanda, la suma de 1.060 horas no cabe; propongo ajustar plazo, personas o alcance", "Que sí cabe, porque 700 es menor que 960", "Que no se puede hacer nunca", "La demanda total sería 1.060 horas, mayor que la capacidad; se propone un ajuste."),
    sc=[
        ("En Administración: ¿qué es la demanda de trabajo?", "Las horas que piden las actividades", "La demanda se compara con la capacidad del equipo."),
        ("¿Cómo se calcula el costo de insumos?", "Cantidad por precio unitario", "Cada insumo se multiplica por su precio."),
        ("¿Qué haces si la demanda supera la capacidad?", "Propongo a la jefatura más tiempo, más personas o menos alcance", "Los ajustes se proponen y aprueba la jefatura."),
    ],
    op=("Con la Ficha 9, escribe una hoja de cálculo en papel: demanda total, capacidad, horas de holgura, costo de personal, costo de insumos y presupuesto. Agrega una frase con una recomendación para la jefatura y un indicador de avance con su valor esperado.\n{F}",
        "Demanda: 360 horas. Capacidad: 960 horas. Holgura: 600 horas. Personal: 360 horas × $5.000 = $1.800.000. Insumos: $75.000. Presupuesto: $1.875.000. Recomendación: el programa cabe con holgura; se puede cumplir en menos semanas. Indicador: facturas digitadas sobre las recibidas; esperado 100 %.",
        ["calcula bien demanda y capacidad", "calcula costos de personal e insumos", "presenta una recomendación", "define un indicador con valor esperado"],
        ["hoja con seis cálculos, una recomendación y un indicador"],
        ["mezclar horas semanales con totales", "olvidar los insumos", "indicador sin valor esperado"],
        "Verifica los seis cálculos. Si el estudiante olvidó los insumos, pide que los sume al presupuesto."),
    reinforce="Calcula en papel la capacidad de un equipo ficticio de 5 personas con 38 horas semanales durante 6 semanas.",
    extend="Explica con un ejemplo inventado por qué el costo por hora de ejemplo debe reemplazarse por datos reales en un caso verdadero.",
)

# ============================================================ OAE-02, clase 5
F = ("Ficha 10 (alternativas de ejemplo, inventadas) para «Servicios Maitén Ltda.». Meta: digitar 600 facturas en 6 semanas. Alternativa 1: 2 personas, 40 horas semanales cada una; rendimiento de ejemplo de 5 facturas por hora de cada persona; costo de ejemplo de $5.000 por hora. "
     "Alternativa 2: 3 personas, 20 horas semanales cada una; mismo rendimiento y mismo costo por hora. Criterios de la jefatura: cumplir la meta, costo máximo de $2.000.000 y no superar las horas disponibles de nadie.")
build(
    O2, 5, F,
    use="Aprenderé a comparar dos alternativas de programa con criterios de la jefatura y a verificar su calidad con una lista de control.",
    prior=["Sé calcular capacidad, demanda y costo.", "Sé qué es un indicador.", "Sé declarar supuestos."],
    explain=[
        "Comparar alternativas de programa significa evaluarlas con los mismos criterios fijados por la jefatura: por ejemplo cumplir la meta, no pasar de un costo máximo y respetar las horas disponibles de cada persona. Para cada alternativa se calcula el resultado esperado (rendimiento × horas), el costo (horas × costo por hora) y se verifica cada criterio con un sí o un no. Una alternativa que no cumple un criterio obligatorio se descarta.",
        "Si más de una alternativa cumple, se elige con un segundo criterio, por ejemplo el menor costo o la mayor holgura, y se escribe por qué. La decisión final es de la jefatura: quien elabora el programa presenta la comparación con los cálculos a la vista y los supuestos.",
        "Verificar la calidad del programa es revisar una lista de control: la meta está definida; cada actividad tiene responsable, fecha y horas; las cifras se rehicieron; los recursos existen; hay un indicador con valor de partida y esperado; y los supuestos están declarados. Se corrige lo que falle antes de entregar.",
    ],
    vocab=[("alternativa", "una de las opciones que se comparan"), ("rendimiento", "trabajo hecho por hora"), ("criterio obligatorio", "condición que toda alternativa debe cumplir"), ("costo máximo", "tope de gasto fijado por la jefatura"), ("lista de control", "pauta para revisar la calidad"), ("supuesto", "dato no confirmado, declarado")],
    worked=[
        ("Verificar la meta", "Dos personas de ejemplo trabajan 30 horas semanales cada una, durante 4 semanas, con rendimiento de 4 piezas por hora. ¿Cuántas piezas producen?", ["Horas = 2 × 30 × 4 = 240.", "Piezas = 240 × 4 = 960."], "960 piezas"),
        ("Descartar", "Una alternativa de ejemplo cumple la meta pero cuesta $2.400.000 y el máximo es $2.000.000. ¿Se descarta?", ["Un costo sobre el máximo incumple un criterio obligatorio.", "Se descarta aunque cumpla la meta."], "Sí, se descarta"),
    ],
    mistakes=[("Elegir la alternativa más barata aunque no cumpla la meta.", "Incumple un criterio obligatorio; no es válida.", "Descarta primero lo que no cumple y compara el costo entre las que sí cumplen."),
              ("Entregar el programa sin rehacer los cálculos.", "Un error pequeño puede cambiar la decisión.", "Rehaz las cifras con la lista de control.")],
    T=[
        ("abc", "En Administración: ¿qué es un criterio obligatorio al comparar alternativas?", "Una condición que toda alternativa debe cumplir", "Una opinión sobre la alternativa que más gusta", "Un color del informe", "El criterio obligatorio filtra las alternativas que no sirven."),
        ("abc", "¿Quién toma la decisión final entre las alternativas?", "La jefatura", "El analista que hizo los cálculos", "La alternativa que produce más facturas", "La jefatura decide con la información que se le presenta."),
        ("abc", "¿Qué hace quien elabora el programa con los supuestos?", "Los declara en el documento", "Los esconde para que el programa se vea completo", "Los reemplaza por datos inventados", "Declarar supuestos permite que la jefatura los confirme."),
        ("=", "{F} ¿Cuántas horas totales trabaja la alternativa 1 en las 6 semanas?", "2*40*6", "Horas = personas × horas semanales × semanas.", " horas"),
        ("=", "{F} ¿Cuántas facturas digita la alternativa 1 en las 6 semanas?", "2*40*6*5", "Facturas = horas totales × rendimiento por hora.", " facturas"),
        ("=", "{F} ¿Cuántas horas totales trabaja la alternativa 2 en las 6 semanas?", "3*20*6", "Horas = personas × horas semanales × semanas.", " horas"),
        ("=", "{F} ¿Cuántas facturas digita la alternativa 2 en las 6 semanas?", "3*20*6*5", "Facturas = horas totales × rendimiento por hora.", " facturas"),
        ("abc", "{F} ¿Cuál de las alternativas cumple la meta de 600 facturas?", "Ambas, porque producen 2.400 y 1.800 facturas", "Solo la alternativa 2", "Ninguna de las dos", "Las dos superan las 600 facturas; por eso la meta no decide y se usan los otros criterios."),
        ("=", "{F} ¿Cuántos pesos cuesta la alternativa 1 (horas totales × costo por hora)?", "2*40*6*5000", "Costo = horas totales × costo por hora de ejemplo.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la alternativa 2?", "3*20*6*5000", "Costo = horas totales × costo por hora de ejemplo.", " pesos"),
        ("abc", "{F} Con el máximo de $2.000.000, ¿cuál es la alternativa que cumple todos los criterios y cuesta menos?", "La alternativa 2, que cuesta $1.800.000", "La alternativa 1, que cuesta $2.400.000", "Ninguna cumple", "La alternativa 1 supera el máximo; la 2 cumple meta, costo y horas y cuesta menos."),
        ("abc", "{F} Con un máximo de $2.500.000 ambas alternativas cumplen todo. ¿Cuál escogerías si la jefatura prioriza ahorrar dinero?", "La alternativa 2, porque cuesta menos", "La alternativa 1, porque sus personas trabajan más horas", "La alternativa 1, porque rinde más facturas aunque cueste más", "Si se prioriza ahorrar, se elige la que cuesta menos entre las que cumplen: la alternativa 2."),
        ("abc", "El programa entregado a la jefatura tiene responsables y fechas, pero ningún indicador. ¿Qué punto de la lista de control falla?", "Falta el indicador con valor de partida y esperado", "Falta el nombre de la empresa", "Sobran las fechas", "La lista exige indicadores para saber si se cumple la meta."),
    ],
    ctx=("abc", "Una asistente va a entregar su comparación. Antes de enviarla, vuelve a calcular el costo de cada alternativa con la calculadora. ¿Qué paso de la lista de control cumple?", "Rehacer las cifras", "Declarar supuestos", "Fijar la meta", "Repetir los cálculos corresponde a rehacer las cifras."),
    sc=[
        ("En Administración: ¿qué se hace con una alternativa que no cumple un criterio obligatorio?", "Se descarta", "Un criterio obligatorio no se negocia."),
        ("¿Cómo se calcula el costo de una alternativa?", "Horas totales por costo por hora", "Se multiplican las horas totales por el costo de ejemplo."),
        ("¿Qué incluye la lista de control del programa?", "Meta, responsables, fechas, horas, cifras, recursos, indicador y supuestos", "Cada punto verifica una parte del programa."),
    ],
    op=("Con la Ficha 10, escribe una comparación de cuatro líneas: horas y costo de cada alternativa, cuál cumple los tres criterios de la jefatura, qué alternativa propones y qué puntos de la lista de control revisaste. Agrega un supuesto que declarar.\n{F}",
        "Alternativa 1: 480 horas, $2.400.000, supera el máximo. Alternativa 2: 360 horas, $1.800.000, cumple meta, costo y horas. Propongo la alternativa 2. Revisé meta, cifras rehechas y horas por persona. Supuesto: el rendimiento de 5 facturas por hora se mantiene durante las 6 semanas.",
        ["calcula horas y costos de ambas", "aplica los tres criterios", "propone con un criterio explícito", "declara un supuesto"],
        ["comparación de cuatro líneas con cálculos"],
        ["decidir solo por costo sin ver la meta", "no rehacer cálculos", "no declarar el supuesto"],
        "Comprueba que los costos coincidan con la ficha. Si el estudiante no declara supuestos, pide que lo agregue."),
    reinforce="Compara en papel dos horarios de trabajo de un equipo ficticio con los mismos criterios de costo y horas.",
    extend="Explica con un ejemplo inventado cómo cambiaría la decisión si el rendimiento por hora bajara a la mitad.",
)
