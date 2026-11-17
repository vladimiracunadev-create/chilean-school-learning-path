"""Administración, mención Logística, 4.º medio TP: OAM-01 (controlar la entrada y salida de productos) y OAM-02 (controlar el almacenamiento y manejo de existencias). Bodegas, productos y cifras inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, papel y, si quieres, una calculadora simple. Todas las fichas, documentos, registros y casos están escritos en cada ejercicio: las bodegas, los productos y las personas son inventados y las cifras son «de ejemplo», "
             "así que no necesitas bodega, programas ni internet. Esto es aprendizaje conceptual en papel. Practicar esta tarea en una bodega real exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar. "
             "Aquí no se enseña a operar maquinaria ni a mover cargas: ante cualquier duda de seguridad se pide ayuda a la persona responsable. Los documentos tributarios y de traslado se rigen por la norma vigente.")

build = make_build(MATERIALS)

O1 = "TP-ADLO-4-OAM-01"
O2 = "TP-ADLO-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 27 (caso de ejemplo, inventado). Bodega de la empresa ficticia «Distribuidora Andes del Sur». Orden de compra OC-210: 120 cajas del producto A, pedidas a un proveedor. Llega un camión con la guía de despacho N.º 88 del proveedor, que dice 120 cajas. "
     "El bodeguero cuenta 117 cajas, y 3 de ellas tienen el envase dañado. Existencias antes de la recepción: 80 cajas. Stock mínimo del producto A: 60 cajas.")
build(
    O1, 1, F,
    use="Aprenderé el recorrido de un producto en la bodega (recepción, almacenamiento y despacho), por qué cada movimiento se registra y qué cuidados éticos y de seguridad exige.",
    prior=["Sé sumar y restar cantidades.", "Sé qué es una factura y una guía.", "Sé que hay datos reservados."],
    explain=[
        "En una bodega, los productos entran (recepción), se guardan (almacenamiento) y salen (despacho). Controlar la entrada y la salida significa revisar el stock disponible, comprobar que lo que llega o sale coincide con los documentos y registrar cada movimiento en un instrumento de registro, manual o computacional. El stock es la cantidad de producto que hay en bodega en un momento dado.",
        "En la recepción se compara lo que llega con la orden de compra (lo que se pidió) y con la guía de despacho (lo que el proveedor dice que envía), se cuenta lo recibido y se revisa su estado. Si hay diferencias o daños, se anotan en el registro y se informa a la jefatura antes de firmar. En el despacho se verifica que lo que sale esté autorizado por un documento. Los documentos tributarios y de traslado se rigen por la norma vigente.",
        "Hay cuidados éticos y de seguridad. Nunca se firma sin contar. No se retira producto sin un documento que lo autorice, aunque se trate de pocas unidades. Las claves del sistema son personales. Los productos pesados se mueven con equipos autorizados y con ayuda; este cuaderno no enseña a operarlos, y si hay dudas se consulta al responsable de la bodega.",
    ],
    vocab=[("stock", "cantidad de producto disponible en bodega"), ("recepción", "etapa en que llega y se revisa la mercadería"), ("despacho", "etapa en que sale la mercadería"), ("orden de compra", "documento con lo que se pidió al proveedor"), ("guía de despacho", "documento que acompaña la mercadería trasladada"), ("instrumento de registro", "formato manual o computacional donde se anotan los movimientos")],
    worked=[
        ("Diferencia en la recepción", "Un pedido ficticio era de 50 unidades y se cuentan 48. ¿Cuál es la diferencia y qué se hace?", ["La diferencia es 50 − 48 = 2.", "Se anota en el registro y se informa a la jefatura antes de firmar."], "Faltan 2 unidades; se registra e informa"),
        ("Salida sin documento", "Un compañero pide sacar 3 unidades de una bodega ficticia sin documento «porque son pocas». ¿Qué corresponde?", ["Toda salida requiere un documento autorizado.", "No se entrega sin documento y se avisa a la jefatura."], "No entregar sin documento"),
    ],
    mistakes=[("Firmar la guía de despacho sin contar la mercadería.", "Si hay diferencias o daños después no se pueden reclamar.", "Cuenta, revisa el estado y anota las diferencias antes de firmar."),
              ("Anotar las entradas de memoria al final del día.", "Se olvidan o se mezclan cifras y el stock registrado deja de ser real.", "Registra cada movimiento cuando ocurre.")],
    T=[
        ("abc", "En Logística: ¿qué es el stock?", "La cantidad de producto disponible en bodega en un momento", "La cantidad de dinero que tiene la empresa en el banco", "La cantidad de clientes que compran", "El stock mide el producto que hay disponible en la bodega."),
        ("abc", "{F} ¿Qué documento muestra lo que se pidió al proveedor?", "La orden de compra OC-210", "La guía de despacho N.º 88", "El registro de stock mínimo", "La orden de compra detalla lo que se pidió."),
        ("abc", "{F} ¿Qué documento acompaña la mercadería durante el traslado?", "La guía de despacho N.º 88", "La orden de compra OC-210", "El registro de existencias", "La guía de despacho es el documento que acompaña lo trasladado."),
        ("=", "{F} ¿Cuántas cajas faltan respecto de lo que dice la guía de despacho?", "120-117", "Diferencia = lo que dice la guía − lo contado.", " cajas"),
        ("=", "{F} ¿Cuántas cajas llegaron en buen estado?", "117-3", "Buen estado = contadas − dañadas.", " cajas"),
        ("abc", "{F} ¿Qué corresponde hacer con las 3 cajas dañadas?", "Registrar el daño, separarlas e informar a la jefatura", "Mezclarlas con las buenas para no perder tiempo", "No anotarlas para evitar problemas con el proveedor", "Los daños se registran y se informan para poder reclamar y no entregar producto defectuoso."),
        ("=", "{F} ¿Cuántas cajas habrá en bodega sumando las cajas en buen estado a las existencias previas?", "80+117-3", "Existencias nuevas = previas + buenas recibidas.", " cajas"),
        ("abc", "{F} El chofer pide firmar la guía sin contar porque tiene apuro. ¿Qué es lo más adecuado?", "Contar y anotar las diferencias antes de firmar", "Firmar de inmediato para no atrasarlo", "Firmar y contar después sin avisar", "Firmar sin contar impide reclamar diferencias después."),
        ("abc", "{F} Con las existencias de la ficha después de la recepción, ¿el producto A está sobre el stock mínimo?", "Sí, porque 194 cajas superan las 60 del mínimo", "No, porque 194 es menor que 60", "No se puede saber", "194 es mayor que 60, de modo que cumple el stock mínimo."),
        ("abc", "Un bodeguero anota las entradas del día de memoria al terminar su turno. ¿Qué riesgo tiene?", "Olvidar o mezclar cifras, y el registro deja de ser fiel", "Ninguno, porque la memoria es exacta", "Anotarlas dos veces con certeza", "Registrar al final aumenta los errores; se debe anotar en el momento."),
        ("abc", "Un compañero propone retirar 5 cajas sin documento «para un amigo». ¿Qué corresponde?", "Rechazarlo y avisar a la jefatura: toda salida requiere un documento autorizado", "Aceptar si son pocas cajas", "Aceptar y registrarlas como dañadas", "Retirar sin documento es una falta ética y distorsiona el stock."),
        ("abc", "{F} El sistema computacional muestra 190 cajas pero el conteo físico es 194. ¿Qué corresponde?", "Revisar los documentos y los registros para encontrar la causa de la diferencia", "Cambiar el conteo físico a 190", "Cambiar el sistema a 194 sin revisar", "La diferencia se investiga con documentos; no se iguala sin causa."),
        ("abc", "{F} Las cajas son pesadas y no hay equipo a mano. ¿Qué es lo más adecuado?", "Pedir ayuda y usar el equipo autorizado que corresponde", "Cargarlas entre pocos hasta que alcancen", "Apilarlas rápido para despejar el paso", "La seguridad se resuelve con el equipo autorizado y ayuda; este cuaderno no enseña a operarlos."),
    ],
    ctx=("abc", "Una bodeguera revisa una guía que dice 100 unidades, cuenta 100 y las ve en buen estado. ¿Qué hace?", "Firma la guía y registra la entrada en el instrumento de registro", "Rechaza la mercadería", "Firma sin registrar", "Si coincide y está en buen estado, se acepta y se registra la entrada."),
    sc=[
        ("En Logística: ¿qué se compara en la recepción?", "Lo que llega contra la orden de compra y la guía", "Así se detectan diferencias antes de firmar."),
        ("¿Qué haces si hay diferencias o daños?", "Los registro y los informo a la jefatura", "Registrar el hecho permite reclamar con respaldo documental."),
        ("¿Se puede retirar producto sin documento?", "No, toda salida requiere un documento autorizado", "Sin documento el stock se distorsiona y hay falta ética."),
    ],
    op=("Con la Ficha 27, escribe un acta de recepción de cinco líneas: documentos revisados, cantidad contada, diferencia respecto de la guía, cajas dañadas y a quién informarías. Agrega la nueva existencia de buenas.\n{F}",
        "Documentos: OC-210 y guía N.º 88. Contadas: 117 cajas. Diferencia: 3 cajas menos que la guía. Dañadas: 3 cajas, separadas. Informo al jefe de bodega y al comprador. Existencias con las cajas en buen estado: 194 cajas.",
        ["revisa orden y guía", "calcula la diferencia", "separa los daños", "informa a la jefatura"],
        ["acta de recepción de cinco líneas"],
        ["firmar sin anotar diferencias", "mezclar cajas dañadas", "no informar"],
        "Compara las cifras con la ficha. Si no informa a nadie, pregunta quién debe saber."),
    reinforce="Escribe en papel el recorrido de una caja desde que llega hasta que sale, indicando qué documento se usa en cada etapa.",
    extend="Explica con un ejemplo inventado cómo una diferencia no registrada hoy puede transformarse en un problema mayor.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 28 (documentos y kárdex de ejemplo, inventados) de «Distribuidora Andes del Sur». Orden de compra: pedido al proveedor. Guía de despacho: acompaña la mercadería trasladada. Acta de recepción: anota lo que realmente llegó, con diferencias y daños. "
     "Orden de salida: autoriza a despachar. Kárdex (tarjeta de existencias): para cada producto lleva fecha, documento, entradas, salidas y saldo. Kárdex del producto B: saldo inicial 50; día 3, entrada 40 (guía 91); "
     "día 5, salida 25 (orden S-14); día 9, salida 30 (orden S-15); día 12, entrada 20 (guía 97). Roles: bodeguero(a) recibe, despacha y registra; jefe(a) de bodega autoriza y revisa; comprador(a) hace los pedidos.")
build(
    O1, 2, F,
    use="Aprenderé los documentos de entrada y salida, cómo se lleva un kárdex y qué hace cada rol en el control de existencias.",
    prior=["Conozco el recorrido recepción, almacenamiento y despacho.", "Sé sumar y restar.", "Sé qué es una diferencia."],
    explain=[
        "Los documentos de bodega dejan constancia de cada movimiento. La orden de compra dice qué se pidió; la guía de despacho acompaña lo que se traslada; el acta de recepción anota lo que realmente llegó, con diferencias y daños; la orden de salida autoriza entregar productos. Los documentos tributarios y de traslado se rigen por la norma vigente.",
        "El kárdex o tarjeta de existencias es un instrumento de registro de cada producto. Tiene columnas de fecha, documento, entradas, salidas y saldo. El saldo se calcula así: saldo anterior + entradas − salidas. Se puede llevar a mano o en un sistema computacional; en ambos casos cada fila se respalda con un documento y el saldo debe coincidir con el conteo físico.",
        "Cada rol tiene su responsabilidad. El bodeguero recibe, despacha y registra; el jefe de bodega autoriza y revisa; el comprador hace los pedidos. Nadie debe aprobar y registrar su propio movimiento sin que otra persona lo revise. Las claves del sistema son personales y no se comparten.",
    ],
    vocab=[("kárdex", "tarjeta de existencias de un producto"), ("saldo", "cantidad que queda tras entradas y salidas"), ("acta de recepción", "documento de lo realmente recibido"), ("orden de salida", "documento que autoriza un despacho"), ("entrada", "cantidad que ingresa a bodega"), ("salida", "cantidad que sale de bodega")],
    worked=[
        ("Calcular saldo", "Un producto ficticio tiene saldo 30, recibe una entrada de 20 y una salida de 15. ¿Cuál es el nuevo saldo?", ["Saldo = 30 + 20 − 15.", "30 + 20 = 50; 50 − 15 = 35."], "35"),
        ("Elegir el documento", "Se quiere autorizar la entrega de 10 unidades a un cliente ficticio. ¿Qué documento corresponde?", ["Se trata de autorizar una salida.", "Eso es una orden de salida."], "Orden de salida"),
    ],
    mistakes=[("Calcular el saldo sumando las salidas.", "Las salidas reducen el stock; sumarlas lo infla.", "Resta las salidas y suma las entradas."),
              ("Registrar un movimiento sin anotar el documento que lo respalda.", "No se puede comprobar de dónde viene la cifra.", "Anota el número del documento en cada fila.")],
    T=[
        ("abc", "En Logística: ¿qué es el kárdex?", "La tarjeta de existencias de un producto con entradas, salidas y saldo", "Un contrato con el proveedor", "Un plano de la bodega", "El kárdex es el registro del movimiento y saldo de un producto."),
        ("abc", "{F} ¿Qué documento autoriza a despachar productos?", "La orden de salida", "El acta de recepción", "La orden de compra", "La orden de salida es la que autoriza entregar."),
        ("abc", "{F} ¿Qué rol hace los pedidos al proveedor?", "El comprador o la compradora", "El bodeguero", "El chofer", "Según la ficha, el comprador hace los pedidos."),
        ("=", "{F} ¿Cuál es el saldo del producto B el día 3, después de la entrada de 40?", "50+40", "Saldo = saldo anterior + entrada.", " unidades"),
        ("=", "{F} ¿Cuál es el saldo del producto B el día 5, después de la salida de 25?", "50+40-25", "Saldo = saldo anterior − salida.", " unidades"),
        ("=", "{F} ¿Cuál es el saldo del producto B el día 9?", "50+40-25-30", "Se resta la salida de 30 al saldo anterior.", " unidades"),
        ("=", "{F} ¿Cuál es el saldo del producto B el día 12?", "50+40-25-30+20", "Se suma la entrada de 20 al saldo anterior.", " unidades"),
        ("=", "{F} ¿Cuántas unidades salieron en total del producto B en esos días?", "25+30", "Total de salidas = suma de salidas.", " unidades"),
        ("abc", "{F} Al contar físicamente el producto B el día 12 hay 55 unidades. ¿Coincide con el kárdex?", "Sí, porque el saldo del kárdex es 55", "No, porque el kárdex indica 45", "No se puede comparar", "El saldo del día 12 es 55, igual al conteo físico."),
        ("abc", "El mismo bodeguero recibe, aprueba y registra un movimiento sin revisión de otra persona. ¿Qué falla?", "Falta un control: alguien más debe revisar o autorizar", "Nada, porque es más rápido", "Debe hacerlo siempre el chofer", "Sin una segunda persona no hay control de errores o abusos."),
        ("abc", "Un bodeguero presta su clave del sistema a un compañero. ¿Qué corresponde?", "Negarse, porque la clave es personal", "Prestarla si hay confianza", "Prestarla por un día", "Compartir claves impide saber quién hizo cada registro."),
        ("abc", "{F} Se anota una salida de 30 unidades sin número de orden. ¿Qué falta?", "El documento que la respalda", "El color del producto", "La fecha de cumpleaños del cliente", "Cada fila del kárdex debe tener su documento de respaldo."),
        ("abc", "{F} ¿Qué diferencia hay entre la guía de despacho y el acta de recepción?", "La guía dice lo que se envía; el acta anota lo que realmente llegó", "Son el mismo documento", "El acta autoriza la salida", "La guía es del proveedor; el acta es de la bodega y registra diferencias."),
    ],
    ctx=("abc", "El jefe de bodega pide revisar por qué el saldo del sistema no coincide con el conteo. ¿Qué documento consulta primero?", "El kárdex y sus documentos de respaldo", "El plano del edificio", "La lista de cumpleaños del personal", "Las diferencias se investigan en el kárdex con sus documentos."),
    sc=[
        ("En Logística: ¿cómo se calcula el saldo de un kárdex?", "Saldo anterior más entradas menos salidas", "La fórmula combina todos los movimientos."),
        ("¿Qué documento autoriza un despacho?", "La orden de salida", "Sin esa orden no se entrega."),
        ("¿Por qué una segunda persona revisa los movimientos?", "Para detectar errores y evitar abusos", "El control cruzado protege el registro."),
    ],
    op=("Con la Ficha 28, arma el kárdex del producto C con estos datos inventados: saldo inicial 80; día 2 entrada 30 (guía 101); día 4 salida 45 (orden S-20); día 7 salida 25 (orden S-21). Escribe cada saldo y qué documento respalda cada fila.\n{F}",
        "Saldo inicial 80. Día 2: entrada 30, guía 101, saldo 110. Día 4: salida 45, orden S-20, saldo 65. Día 7: salida 25, orden S-21, saldo 40.",
        ["calcula cada saldo", "anota el documento de cada fila", "sigue el formato del kárdex"],
        ["tabla de cuatro filas con saldo y documento"],
        ["sumar las salidas", "omitir documentos", "saltarse un saldo"],
        "Rehace los saldos. Si falta un documento, pide agregarlo."),
    reinforce="Arma en papel un kárdex de cinco movimientos para un producto ficticio.",
    extend="Explica con un ejemplo inventado por qué un kárdex llevado a mano también necesita revisarse con el conteo físico.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 29 (caso de ejemplo, inventado) de «Distribuidora Andes del Sur». Producto C. Movimientos del mes: saldo inicial 200; entradas: 60 (guía 140) y 40 (guía 152); salidas registradas: 90 (orden S-20), 50 (orden S-21) y 40 (orden S-23). "
     "Conteo físico al cierre: 114 unidades. En la carpeta de documentos aparece una orden de salida S-22 por 6 unidades, firmada el día 14, que no está en el kárdex. Nadie recuerda quién la despachó.")
build(
    O1, 3, F,
    use="Aprenderé a analizar una diferencia entre el kárdex y el conteo físico, a buscar su causa en los documentos y a corregirla con respaldo.",
    prior=["Sé calcular el saldo de un kárdex.", "Conozco los documentos de bodega.", "Sé qué es una diferencia."],
    explain=[
        "Al terminar un período se hace un conteo físico y se compara con el saldo del kárdex. Si coinciden, el registro es fiel; si no, hay una diferencia de inventario. La diferencia se calcula restando: saldo del kárdex − conteo físico. Una diferencia positiva indica que falta producto físico respecto del registro; una negativa indica que sobra.",
        "Para hallar la causa se revisan los documentos del período: entradas sin registrar, salidas sin registrar, errores de suma, productos mal ubicados o dañados. Se corrige en el registro solo cuando hay un documento que lo respalde, y la corrección la autoriza la jefatura. No se ajusta el kárdex al conteo, ni el conteo al kárdex, sin entender la causa.",
        "Todo análisis termina en una acción preventiva: registrar el movimiento en el momento, revisar que cada documento tenga su fila, y firmar solo lo contado. Una salida sin registrar puede ser un simple olvido o una falta ética; por eso se informa a la jefatura y no se acusa a nadie sin evidencia.",
    ],
    vocab=[("conteo físico", "cuenta real de lo que hay en bodega"), ("diferencia de inventario", "saldo del kárdex menos conteo físico"), ("causa", "hecho que explica una diferencia"), ("acción correctiva", "cambio que corrige un registro"), ("acción preventiva", "cambio que evita que el error se repita"), ("respaldo", "documento que prueba un movimiento")],
    worked=[
        ("Calcular la diferencia", "Un kárdex ficticio dice 75 y el conteo da 70. ¿Cuál es la diferencia?", ["Diferencia = 75 − 70.", "Resulta 5, positiva: falta producto físico."], "5 unidades de menos"),
        ("Buscar causa", "En la carpeta aparece una orden de salida de 5 unidades que no está en el kárdex. ¿Qué explicaría la diferencia?", ["La salida se despachó pero no se registró.", "El kárdex quedó con 5 más que el físico."], "Una salida sin registrar"),
    ],
    mistakes=[("Cambiar el saldo del kárdex al valor del conteo sin buscar la causa.", "Se esconde el error y puede repetirse.", "Revisa los documentos y corrige con respaldo."),
              ("Acusar a una persona de la diferencia sin evidencia.", "Puede ser un olvido de registro y daña a la persona.", "Informa a la jefatura con los hechos documentados.")],
    T=[
        ("abc", "En Logística: ¿qué es una diferencia de inventario?", "La resta entre el saldo del kárdex y el conteo físico", "El precio de un producto", "La suma de las entradas", "La diferencia compara lo registrado con lo que realmente hay."),
        ("=", "{F} ¿Cuál es el saldo del producto C según el kárdex al cierre?", "200+60+40-90-50-40", "Saldo = inicial + entradas − salidas.", " unidades"),
        ("=", "{F} ¿Cuál es la diferencia entre el saldo del kárdex y el conteo físico?", "120-114", "Diferencia = saldo del kárdex − conteo físico.", " unidades"),
        ("abc", "{F} ¿Falta o sobra producto físico respecto del kárdex?", "Falta producto físico", "Sobra producto físico", "Coinciden", "El conteo (114) es menor que el kárdex (120), por eso falta producto físico."),
        ("abc", "{F} ¿Qué documento puede explicar la diferencia?", "La orden de salida S-22 que no está en el kárdex", "La guía 140", "La orden S-20", "La S-22 no está registrada y su cantidad es la de la diferencia."),
        ("=", "{F} Si se registra la salida S-22 de 6 unidades, ¿cuál será el nuevo saldo del kárdex?", "200+60+40-90-50-40-6", "Se resta la salida no registrada al saldo.", " unidades"),
        ("abc", "{F} Con la S-22 registrada, ¿coincide el kárdex con el conteo físico?", "Sí, porque ambos son 114", "No, porque quedaría 6 de diferencia", "No se puede saber", "El saldo corregido es 114, igual al conteo físico."),
        ("abc", "{F} Nadie recuerda quién despachó la S-22. ¿Qué corresponde?", "Informar a la jefatura con los documentos y registrar la salida con su respaldo", "Culpar a la última persona que entró a bodega", "Borrar la S-22", "Se informa con hechos y se corrige con respaldo; no se acusa sin evidencia."),
        ("abc", "{F} Un compañero propone cambiar el saldo a 114 sin buscar la causa. ¿Qué respondes?", "Que primero se busque la causa y se corrija con respaldo", "Que está bien si coincide", "Que se debe borrar el kárdex", "Igualar sin causa oculta el error."),
        ("abc", "{F} ¿Qué acción preventiva evitaría repetir el problema?", "Registrar cada salida en el momento en que ocurre", "Contar menos veces", "Guardar las órdenes en casa", "Registrar en el momento evita olvidos."),
        ("=", "{F} Con 8 unidades de diferencia en lugar de 6 y el mismo conteo, ¿qué saldo tendría el kárdex?", "114+8", "Saldo del kárdex = conteo físico + diferencia positiva.", " unidades"),
        ("abc", "El conteo físico supera al kárdex en 4 unidades. ¿Qué causa es posible?", "Una entrada no registrada", "Una salida no registrada", "Una orden de compra anulada", "Si sobra producto físico, falta registrar una entrada."),
        ("abc", "{F} ¿Qué autoriza la corrección del kárdex?", "La jefatura, con el documento que la respalda", "Cualquier bodeguero", "El proveedor", "Las correcciones las autoriza la jefatura con respaldo."),
    ],
    ctx=("abc", "Otra bodega ficticia encuentra 3 unidades de menos y una guía de salida de 3 unidades sin registrar. ¿Qué hace?", "Registra la salida con su respaldo y verifica que ahora coincidan", "Ignora la guía", "Cambia el conteo", "Registrar con respaldo corrige el error de forma trazable."),
    sc=[
        ("En Logística: ¿cómo se calcula la diferencia de inventario?", "Saldo del kárdex menos conteo físico", "Así se ve si falta o sobra producto."),
        ("¿Cuándo se corrige un kárdex?", "Cuando hay un documento que lo respalda y lo autoriza la jefatura", "No se corrige por simple conveniencia."),
        ("¿Se acusa a una persona sin evidencia?", "No, se informa con hechos documentados", "Se evita dañar a alguien sin pruebas."),
    ],
    op=("Con la Ficha 29, escribe un informe de seis líneas: saldo del kárdex, conteo físico, diferencia, causa encontrada, corrección propuesta (con quién la autoriza) y una acción preventiva.\n{F}",
        "Saldo kárdex: 120. Conteo físico: 114. Diferencia: 6 unidades de menos. Causa: la orden de salida S-22, firmada el día 14, no fue registrada. Corrección: registrar la salida con su documento, autorizada por la jefatura; saldo corregido 114. Prevención: registrar cada salida en el momento.",
        ["calcula saldo y diferencia", "identifica la causa con documento", "propone corrección autorizada", "propone prevención"],
        ["informe de seis líneas"],
        ["igualar sin causa", "acusar a alguien", "no proponer prevención"],
        "Rehace las cuentas. Si el informe no menciona la autorización, pídela."),
    reinforce="Calcula en papel la diferencia de inventario de tres productos ficticios y di si falta o sobra.",
    extend="Explica con un ejemplo inventado por qué una diferencia pequeña repetida cada mes puede indicar un problema de proceso.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 30 (datos de ejemplo, inventados) de «Distribuidora Andes del Sur». Producto D: costo unitario de ejemplo $1.500; stock mínimo 40 unidades; saldo actual 72 unidades; stock objetivo de reposición 100 unidades. "
     "Pedido de salida programado para mañana: 50 unidades. Pedido de compra anterior al proveedor: 200 unidades; llegaron 190 unidades. Guía de despacho de una salida: 18 cajas con 12 unidades cada una.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar criterios de control con datos: valorizar existencias, decidir cuándo reponer, medir la exactitud de las recepciones y verificar una salida.",
    prior=["Sé calcular el saldo y las diferencias.", "Sé multiplicar y calcular porcentajes.", "Conozco el stock mínimo."],
    explain=[
        "Con los datos del kárdex se toman decisiones. El valor de las existencias se calcula multiplicando las unidades por el costo unitario. El stock mínimo es la cantidad bajo la cual hay riesgo de quedarse sin producto; cuando el saldo proyectado queda bajo el mínimo, se debe pedir reposición. La cantidad a pedir se calcula como stock objetivo menos el saldo proyectado.",
        "La exactitud de la recepción mide cuánto de lo pedido llegó. Se calcula como unidades recibidas × 100 ÷ unidades pedidas. Sirve para evaluar el cumplimiento de un proveedor. En una salida, se verifica que las unidades totales coincidan con el pedido: cajas × unidades por caja.",
        "Estos cálculos usan datos de ejemplo. En la bodega real las cifras salen del sistema o del kárdex, y toda decisión de reposición la autoriza la jefatura con los documentos a la vista.",
    ],
    vocab=[("costo unitario", "costo de una unidad"), ("valor de existencias", "unidades × costo unitario"), ("stock objetivo", "cantidad a la que se quiere llegar al reponer"), ("saldo proyectado", "saldo esperado tras movimientos planificados"), ("exactitud de recepción", "recibido × 100 ÷ pedido"), ("reposición", "pedido para volver a tener stock")],
    worked=[
        ("Valorizar", "Una bodega ficticia tiene 30 unidades de un producto de $2.000 cada una. ¿Cuánto valen?", ["Valor = unidades × costo unitario.", "30 × 2.000 = 60.000."], "$60.000"),
        ("Decidir reposición", "Saldo 50, salida programada 35, stock mínimo 20 y objetivo 80. ¿Hay que reponer y cuánto?", ["Saldo proyectado = 50 − 35 = 15, menor que 20.", "A pedir = 80 − 15 = 65."], "Sí, 65 unidades"),
    ],
    mistakes=[("Decidir la reposición mirando solo el saldo actual y no el proyectado.", "La salida programada puede dejar el stock bajo el mínimo.", "Calcula el saldo después de las salidas programadas."),
              ("Dar por buena una salida sin multiplicar cajas por unidades por caja.", "Puede haber diferencias en lo despachado.", "Verifica el total con la multiplicación.")],
    T=[
        ("abc", "En Logística: ¿cómo se calcula el valor de las existencias?", "Unidades por costo unitario", "Unidades más costo unitario", "Costo unitario dividido por unidades", "El valor se obtiene multiplicando cantidad por costo de cada unidad."),
        ("=", "{F} ¿Cuántos pesos valen las 72 unidades actuales del producto D?", "72*1500", "Valor = unidades × costo unitario.", " pesos"),
        ("=", "{F} ¿Cuál será el saldo proyectado tras la salida programada?", "72-50", "Saldo proyectado = saldo actual − salida programada.", " unidades"),
        ("abc", "{F} ¿El saldo proyectado queda bajo el stock mínimo?", "Sí, porque 22 es menor que 40", "No, porque 22 es mayor que 40", "No se puede saber", "22 unidades es menos que el mínimo de 40."),
        ("=", "{F} ¿Cuántas unidades hay que pedir para llegar al stock objetivo desde el saldo proyectado?", "100-(72-50)", "A pedir = objetivo − saldo proyectado.", " unidades"),
        ("=", "{F} ¿Cuántos pesos costará ese pedido con el costo unitario de ejemplo?", "(100-(72-50))*1500", "Costo del pedido = unidades × costo unitario.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de lo pedido llegó en la compra anterior?", "190*100//200", "Exactitud = recibido × 100 ÷ pedido.", " %"),
        ("=", "{F} ¿Cuántas unidades faltaron en esa recepción?", "200-190", "Faltante = pedido − recibido.", " unidades"),
        ("=", "{F} ¿Cuántas unidades despacha la guía de 18 cajas de 12 unidades?", "18*12", "Total = cajas × unidades por caja.", " unidades"),
        ("abc", "{F} Si la orden de salida pide 200 unidades y la guía tiene 216, ¿qué corresponde?", "Corregir la diferencia de 16 antes de despachar", "Despachar igual", "Cambiar la orden sin avisar", "Despachar de más sin autorización genera diferencias de inventario."),
        ("abc", "{F} ¿Quién autoriza el pedido de reposición?", "La jefatura de bodega, con los documentos a la vista", "El proveedor", "El chofer", "Las decisiones de compra se autorizan con respaldo."),
        ("abc", "{F} Un proveedor entregó 190 de 200 unidades. ¿Qué corresponde registrar?", "El faltante de 10 unidades y el motivo, e informar al comprador", "Nada, porque es casi lo pedido", "Que llegaron 200", "El faltante se registra para reclamar y para evaluar al proveedor."),
        ("abc", "{F} Un compañero afirma que el pedido de reposición calculado es exacto para siempre. ¿Qué respondes?", "Es un cálculo con datos de ejemplo y cambia con las nuevas salidas", "Tiene razón", "No se puede calcular", "Los pedidos se recalculan con cada movimiento nuevo."),
    ],
    ctx=("abc", "El jefe de bodega pregunta si hay que pedir producto D para mañana. ¿Qué responde un buen análisis?", "Sí: el saldo proyectado de 22 queda bajo el mínimo de 40, y habría que pedir 78", "No, porque hoy hay 72", "Sí, 100 unidades siempre", "El análisis usa el saldo proyectado, el mínimo y el objetivo."),
    sc=[
        ("En Logística: ¿cómo se calcula la cantidad a pedir?", "Stock objetivo menos saldo proyectado", "Así se llega al nivel deseado."),
        ("¿Qué mide la exactitud de recepción?", "Cuánto de lo pedido llegó", "Se calcula como recibido por cien sobre pedido."),
        ("¿Quién autoriza una reposición?", "La jefatura", "Las compras se autorizan con documentos."),
    ],
    op=("Con la Ficha 30, escribe una hoja de decisión: valor de existencias actuales, saldo proyectado, si se repone y cuántas unidades, costo del pedido, exactitud de la recepción anterior y una frase con quién autoriza.\n{F}",
        "Valor actual: $108.000. Saldo proyectado: 22 unidades. Se repone, porque 22 es menor que 40. A pedir: 78 unidades. Costo: $117.000. Exactitud de la recepción anterior: 95 %. Autoriza el jefe de bodega.",
        ["calcula valor y saldo proyectado", "decide con el mínimo", "calcula el pedido y su costo", "indica quién autoriza"],
        ["hoja de decisión de seis líneas"],
        ["usar el saldo actual sin proyectar", "olvidar el costo", "no indicar la autorización"],
        "Rehace los cálculos. Si no usa el saldo proyectado, pide corregir."),
    reinforce="Calcula en papel el valor de tres productos ficticios con distintos costos unitarios.",
    extend="Explica con un ejemplo inventado cuándo conviene pedir más que el stock objetivo.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 31 (caso de ejemplo, inventado). Bodega de «Distribuidora Andes del Sur» con 3 zonas: zona 1, productos de alta rotación (de salida frecuente) cerca de la puerta; zona 2, rotación media; zona 3, baja rotación al fondo. "
     "Producto F (alimento envasado, lote 1 con vencimiento en marzo y lote 2 con vencimiento en junio del mismo año). Un estante tiene el rótulo «Z2-E4-N1». Observaciones: cajas apiladas sobre el borde de un estante; un pasillo parcialmente bloqueado; productos sin rótulo.")
build(
    O2, 1, F,
    use="Aprenderé para qué se almacena de forma ordenada, qué condiciones y riesgos importan y qué normas y cuidados éticos se aplican al manejo de existencias.",
    prior=["Conozco el recorrido de un producto en la bodega.", "Sé leer un kárdex.", "Sé qué es un conteo físico."],
    explain=[
        "Controlar el almacenamiento es asegurar que cada producto esté en un lugar conocido, en buen estado y fácil de recuperar. Para eso se detecta su estado cualitativo (cómo está: sano, dañado, vencido) y cuantitativo (cuánto hay: su cantidad), se asigna una ubicación con un código y se mantiene un sistema de localización inmediata, manual (una planilla o un plano) o digital (un sistema computacional).",
        "Los productos se almacenan según sus condiciones de conservación: algunos requieren lugares secos, frescos o con fechas de vencimiento controladas. Las cajas no se apilan en el borde de un estante ni se bloquean pasillos; se respetan las indicaciones de altura y de carga del fabricante y de la norma vigente. Los productos peligrosos tienen reglas propias que se ven en otra clase.",
        "La ética del almacenamiento incluye no ocultar productos vencidos o dañados, no cambiar fechas de vencimiento y avisar de inmediato cualquier riesgo. Los productos pesados se mueven con equipos autorizados y con ayuda. Este cuaderno no enseña a operar maquinaria: eso corresponde a personas con autorización e instrucción.",
    ],
    vocab=[("estado cualitativo", "cómo está el producto: sano, dañado o vencido"), ("estado cuantitativo", "cuánto hay del producto"), ("ubicación", "lugar asignado a un producto en bodega"), ("código de ubicación", "clave que indica zona, estante y nivel"), ("rotación", "frecuencia con que sale un producto"), ("fecha de vencimiento", "fecha límite para usar un producto")],
    worked=[
        ("Estado cualitativo", "En una bodega ficticia una caja de yogur tiene la fecha de vencimiento pasada. ¿Cuál es su estado cualitativo y qué se hace?", ["Vencido es un estado cualitativo.", "Se separa, se registra e informa a la jefatura."], "Vencido; separar, registrar e informar"),
        ("Código de ubicación", "El rótulo «Z1-E2-N3» significa zona 1, estante 2, nivel 3. ¿En qué zona está?", ["La primera parte del código es la zona.", "La zona es la 1."], "Zona 1"),
    ],
    mistakes=[("Guardar un producto sin anotar su ubicación.", "Después nadie sabrá dónde encontrarlo.", "Registra el código de ubicación al guardarlo."),
              ("Cambiar una fecha de vencimiento «para no botar» un producto.", "Es una falta grave que puede dañar la salud de las personas.", "Registra y retira el producto vencido según la política de la empresa.")],
    T=[
        ("abc", "En Logística: ¿qué es el estado cualitativo de un producto?", "Cómo está: sano, dañado o vencido", "Cuántas unidades hay", "Cuánto costó", "El estado cualitativo describe la condición del producto, no su cantidad."),
        ("abc", "{F} ¿Qué indica el código «Z2-E4-N1»?", "Zona 2, estante 4, nivel 1", "Zona 1, estante 2, nivel 4", "Zona 4, estante 2, nivel 1", "Cada parte del código sigue el orden zona, estante y nivel."),
        ("abc", "{F} ¿Qué productos van en la zona 1 según la ficha?", "Los de alta rotación, cerca de la puerta", "Los de baja rotación", "Los que no tienen rótulo", "La ficha ubica la alta rotación en la zona 1."),
        ("abc", "{F} ¿Qué riesgo presentan las cajas apiladas sobre el borde de un estante?", "Pueden caer y causar un accidente", "Se ven más ordenadas", "Ocupan más espacio libre", "Una caja en el borde puede caerse."),
        ("abc", "{F} ¿Qué corresponde hacer con el pasillo parcialmente bloqueado?", "Despejarlo y avisar a la jefatura si el bloqueo es permanente", "Dejarlo así si pasa una persona", "Usarlo como bodega extra", "Un pasillo despejado evita tropiezos y facilita una evacuación."),
        ("abc", "{F} ¿Qué problema generan los productos sin rótulo?", "No se sabe qué son ni dónde van", "Gastan más espacio", "Son más caros", "Sin rótulo no se identifican ni ubican."),
        ("=", "Una zona de ejemplo tiene 4 estantes con 3 niveles cada uno. ¿Cuántos puestos de nivel hay en total?", "4*3", "Puestos = estantes × niveles.", " puestos"),
        ("=", "En un estante de ejemplo de 4 niveles caben 12 cajas por nivel. ¿Cuántas cajas caben en el estante?", "4*12", "Cajas = niveles × cajas por nivel.", " cajas"),
        ("abc", "{F} Un producto venció y el bodeguero propone cambiar la fecha en la etiqueta. ¿Qué corresponde?", "Rechazarlo: se separa el producto, se registra e informa", "Aceptarlo si nadie se entera", "Aceptarlo si el producto parece sano", "Alterar la fecha es una falta grave y daña la confianza."),
        ("abc", "Un producto pesado debe moverse a un nivel alto del estante. ¿Qué es lo más adecuado?", "Pedir apoyo al responsable y usar el equipo autorizado", "Subirlo entre dos personas con cualquier objeto", "Dejarlo en el pasillo", "Se mueve con equipos autorizados; este cuaderno no enseña maniobras."),
        ("abc", "{F} ¿Qué rotación tiene un producto que sale todos los días?", "Alta rotación", "Baja rotación", "Rotación media", "Una salida muy frecuente significa alta rotación del producto."),
        ("abc", "Una persona nota una gotera sobre un estante con cajas. ¿Qué hace?", "Avisa de inmediato al responsable y protege el producto si es seguro", "Espera a que se seque sola", "Mueve el estante sin avisar", "El riesgo se informa para evitar daño a productos y personas."),
        ("abc", "{F} Un compañero dice que el código de ubicación es opcional. ¿Qué respondes?", "Sin código no se recupera el producto con rapidez", "Tiene razón, es opcional", "Solo importa en bodegas grandes", "El código permite localizar un producto en segundos."),
    ],
    ctx=("abc", "Al recibir yogures con vencimiento en marzo y en junio, una bodeguera los separa y rotula cada lote. ¿Qué logra?", "Distinguir los lotes y despachar primero el que vence antes", "Mezclar los lotes sin control", "Ocultar el vencimiento", "Rotular por lote permite aplicar el criterio de vencimiento."),
    sc=[
        ("En Logística: ¿qué es el estado cuantitativo?", "Cuánto hay del producto", "Es la cantidad, no la condición."),
        ("¿Qué indica un código de ubicación?", "Zona, estante y nivel", "Permite ubicar el producto con rapidez."),
        ("¿Qué haces con un producto vencido?", "Lo separo, registro e informo", "No se mezcla con los demás."),
    ],
    op=("Con la Ficha 31, escribe una lista de cinco observaciones sobre la bodega con una acción para cada una: cajas en el borde, pasillo bloqueado, productos sin rótulo, lotes con distinto vencimiento y un producto vencido hallado en el estante.\n{F}",
        "Cajas en el borde: reubicarlas al fondo del estante. Pasillo bloqueado: despejarlo. Sin rótulo: identificar y rotular con código. Lotes: rotularlos y anotar su vencimiento. Vencido: separarlo, registrar e informar a la jefatura.",
        ["identifica los cinco riesgos", "propone una acción adecuada", "no sugiere maniobras peligrosas"],
        ["lista de cinco observaciones con acción"],
        ["cambiar fechas", "bloquear pasillos", "no informar"],
        "Revisa que cada acción sea segura y no incluya operar maquinaria. Si falta informar, pide agregarlo."),
    reinforce="Anota en papel el estado cualitativo y cuantitativo de cinco productos ficticios.",
    extend="Explica con un ejemplo inventado cómo un buen rotulado ahorra tiempo.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 32 (métodos de ejemplo, inventados) de «Distribuidora Andes del Sur». Método PEPS: primero en entrar, primero en salir. Método FEFO: primero que vence, primero que sale. Clasificación ABC de ejemplo: A son pocos productos con mucha salida; "
     "B tienen salida media; C son muchos productos con poca salida. Inventario cíclico: conteos pequeños y frecuentes de algunos productos. Registro de ubicaciones: planilla manual o sistema digital con el código zona-estante-nivel. "
     "Roles: bodeguero(a) almacena y despacha; jefe(a) de bodega define los métodos y revisa los conteos.")
build(
    O2, 2, F,
    use="Aprenderé los métodos de almacenamiento y de salida (PEPS, FEFO y clasificación ABC), el inventario cíclico y los registros de ubicación manuales y digitales.",
    prior=["Conozco el código de ubicación.", "Sé qué es rotación.", "Sé leer una fecha de vencimiento."],
    explain=[
        "El método PEPS (primero en entrar, primero en salir) despacha primero lo que llegó antes; sirve para que ningún lote quede olvidado. El método FEFO (primero que vence, primero que sale) despacha primero lo que vence antes, aunque haya llegado después; se usa con productos que tienen fecha de vencimiento. Se aplica el que la bodega fija por su tipo de producto.",
        "La clasificación ABC ordena los productos según su salida: los A son pocos y tienen mucha salida, así que van más cerca de la puerta y a un nivel cómodo; los B tienen salida media; los C son muchos y de poca salida, y van más lejos. El inventario cíclico es una forma de verificar existencias contando pocos productos cada día, en lugar de todo una vez al año.",
        "La ubicación se registra con un código zona-estante-nivel, en una planilla manual o en un sistema digital. La planilla en papel es simple pero requiere cuidar su actualización; el sistema digital es más rápido pero depende de las claves personales y de que cada movimiento se registre. En ambos casos el registro debe coincidir con la realidad.",
    ],
    vocab=[("PEPS", "primero en entrar, primero en salir"), ("FEFO", "primero que vence, primero que sale"), ("clasificación ABC", "orden por cuánta salida tiene cada producto"), ("inventario cíclico", "conteos pequeños y frecuentes"), ("localización inmediata", "poder ubicar un producto en pocos segundos"), ("lote", "grupo de unidades producidas juntas")],
    worked=[
        ("Aplicar FEFO", "Hay dos lotes de un producto ficticio: lote 1 vence en abril y lote 2 vence en mayo. ¿Cuál se despacha primero con FEFO?", ["FEFO prioriza el vencimiento más próximo.", "Abril es antes que mayo."], "Lote 1"),
        ("Clasificar", "Un producto ficticio es el segundo más vendido de una bodega con 100 productos. ¿Es A o C?", ["Tiene mucha salida.", "Los productos de mucha salida son A."], "Producto A"),
    ],
    mistakes=[("Despachar por PEPS un producto que vence antes en un lote posterior.", "Puede vencerse un lote que llegó después.", "Con productos con vencimiento usa FEFO."),
              ("Contar todo el inventario solo una vez al año y no revisar nada antes.", "Los errores se acumulan y se detectan tarde.", "Complementa con inventario cíclico.")],
    T=[
        ("abc", "En Logística: ¿qué significa PEPS?", "Primero en entrar, primero en salir", "Primero que vence, primero que sale", "Producto especial por semana", "PEPS ordena la salida según el orden de llegada."),
        ("abc", "{F} ¿Qué significa FEFO?", "Primero que vence, primero que sale", "Primero en entrar, primero en salir", "Primero en estar, último en salir", "FEFO prioriza el vencimiento más próximo."),
        ("abc", "{F} Hay dos lotes: A vence en abril y B vence en mayo, y B llegó antes. Con FEFO, ¿cuál sale primero?", "El lote A, porque vence antes", "El lote B, porque llegó antes", "Da igual cuál", "FEFO prioriza el vencimiento sin considerar la llegada."),
        ("abc", "{F} Con los mismos lotes, ¿cuál sale primero con PEPS?", "El lote B, porque llegó antes", "El lote A, porque vence antes", "Da igual cuál", "PEPS prioriza el orden de llegada."),
        ("abc", "{F} ¿Dónde conviene ubicar un producto de clase A?", "Cerca de la puerta y a un nivel cómodo", "Al fondo de la bodega", "En un nivel alto de difícil acceso", "Los productos de mucha salida se ubican más a mano."),
        ("abc", "{F} ¿Qué es el inventario cíclico?", "Contar pocos productos de manera frecuente", "Contar todo una sola vez al año", "No contar nunca", "El inventario cíclico detecta diferencias antes."),
        ("=", "Una bodega de ejemplo tiene 100 productos y cuenta 5 por día durante 5 días a la semana. ¿Cuántos productos revisa en la semana?", "5*5", "Productos revisados = por día × días.", " productos"),
        ("=", "Con ese ritmo de 25 productos por semana, ¿cuántas semanas tarda en revisar los 100 productos?", "100//25", "Semanas = productos totales ÷ productos por semana.", " semanas"),
        ("abc", "{F} Un producto sin vencimiento se despacha cuando llega y las cajas viejas quedan al fondo sin salir. ¿Qué método previene eso?", "PEPS", "FEFO", "ABC", "PEPS asegura que lo más antiguo salga primero."),
        ("abc", "{F} Para un yogur con fecha de vencimiento, ¿qué método conviene?", "FEFO", "PEPS", "Ninguno", "Con vencimiento, FEFO protege contra productos vencidos."),
        ("abc", "{F} En un registro de ubicaciones en papel, un bodeguero no anota que movió un producto. ¿Qué pasa?", "El registro deja de coincidir con la realidad", "Nada, porque el producto aparece solo", "El producto se deteriora", "Sin actualizar, la planilla indica un lugar incorrecto."),
        ("abc", "El bodeguero comparte la clave del sistema digital con un compañero. ¿Qué falla?", "No se sabe quién hizo cada registro", "El sistema se vuelve más rápido", "Nada", "Las claves son personales para identificar responsables."),
        ("abc", "{F} ¿Quién define el método de almacenamiento y revisa los conteos?", "El jefe o la jefa de bodega", "El cliente", "El proveedor", "La ficha le asigna esa función."),
    ],
    ctx=("abc", "Una bodega de alimentos envasados recibe productos con vencimientos distintos. ¿Qué método elige la jefatura?", "FEFO, para despachar primero lo que vence antes", "PEPS, sin mirar el vencimiento", "Ninguno", "Con fechas distintas conviene el método FEFO."),
    sc=[
        ("En Logística: ¿qué diferencia hay entre PEPS y FEFO?", "PEPS mira la llegada; FEFO mira el vencimiento", "Cada método usa un criterio distinto."),
        ("¿Qué se hace con los productos A?", "Se ubican cerca y a un nivel cómodo", "Estos productos tienen mucha salida y se retiran seguido."),
        ("¿Para qué sirve el inventario cíclico?", "Para detectar diferencias con conteos pequeños y frecuentes", "Así las diferencias se detectan y se corrigen antes."),
    ],
    op=("Con la Ficha 32, escribe una pauta de cinco líneas para una bodega ficticia de alimentos: método de salida elegido y por qué, dónde ubicar los productos A, cada cuánto hacer inventario cíclico, cómo registrar las ubicaciones y quién revisa los conteos.\n{F}",
        "Salida: FEFO, porque los alimentos tienen vencimiento. Productos A: cerca de la puerta y en niveles cómodos. Inventario cíclico: 5 productos por día. Ubicaciones: código zona-estante-nivel, planilla manual o sistema. Revisa los conteos el jefe de bodega.",
        ["elige el método con razón", "ubica los productos A", "propone inventario cíclico", "define quién revisa"],
        ["pauta de cinco líneas"],
        ["usar PEPS con vencimientos", "ubicar A al fondo", "sin responsable"],
        "Revisa que cada elección tenga razón. Si usa PEPS, pregunta por los vencimientos."),
    reinforce="Ordena en papel seis productos ficticios en A, B o C según su salida mensual.",
    extend="Explica con un ejemplo inventado qué método usarías con productos sin vencimiento y por qué.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 33 (caso de ejemplo, inventado) de «Distribuidora Andes del Sur». Inventario de la zona 2: producto G, 3 lotes. Lote 1: ingresó el 5, vence el 20 del mes siguiente, 40 unidades. Lote 2: ingresó el 12, vence el 10 del mes siguiente, 30 unidades. "
     "Lote 3: ingresó el 20, vence el 28 del mes siguiente, 50 unidades. Pedido de salida del día 25: 60 unidades de G. Registro de ubicaciones: lote 1 en Z2-E1-N2; lote 2 en Z2-E3-N1; lote 3 en Z2-E1-N1. Al revisar, el lote 2 tiene 4 unidades con envase dañado.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso en papel: decidir de qué lotes sale un pedido con FEFO, hallar ubicaciones y detectar productos dañados.",
    prior=["Conozco PEPS y FEFO.", "Sé leer un código de ubicación.", "Sé separar productos en mal estado."],
    explain=[
        "Para resolver una salida con FEFO se ordenan los lotes por fecha de vencimiento, del que vence primero al que vence último. Se despacha desde el primero hasta completar el pedido y luego se pasa al siguiente. Antes se verifica el estado de las unidades: las dañadas o vencidas no se despachan y se separan.",
        "Una vez decidido, se escribe el plan de despacho: lote, ubicación, cantidad que se saca y saldo que queda. El plan se anota con los códigos de ubicación para que quien prepare el pedido sepa dónde ir. Cualquier cambio de ubicación se registra.",
        "Las unidades dañadas se registran con su causa y se informa a la jefatura. Se evita despachar producto dañado aunque sea poco: puede dañar a un cliente y la reputación de la empresa. El análisis termina con una conclusión clara y los pasos siguientes.",
    ],
    vocab=[("plan de despacho", "lista de lotes y cantidades que salen"), ("saldo del lote", "cantidad que queda en un lote"), ("unidad dañada", "unidad con envase o producto en mal estado"), ("orden de vencimiento", "orden del que vence primero al último"), ("ubicación", "código del lugar donde está el lote"), ("conclusión", "resultado del análisis, claro y breve")],
    worked=[
        ("Ordenar por vencimiento", "Lotes ficticios: X vence el 15, Y vence el 8, Z vence el 22. ¿En qué orden salen con FEFO?", ["De la fecha menor a la mayor.", "8, 15, 22."], "Y, X, Z"),
        ("Cantidad por lote", "Un pedido de 70 se despacha de un lote de 50 y luego de otro de 40. ¿Cuántas unidades salen del segundo lote?", ["Del primero salen 50.", "Faltan 70 − 50 = 20, que salen del segundo."], "20 unidades"),
    ],
    mistakes=[("Despachar primero el lote que ingresó antes sin mirar el vencimiento.", "Con FEFO el criterio es la fecha de vencimiento.", "Ordena por vencimiento antes de decidir."),
              ("Incluir en el despacho unidades con envase dañado «porque son pocas».", "Entrega producto en mal estado al cliente.", "Sepáralas y regístralas.")],
    T=[
        ("abc", "En Logística: ¿con qué criterio se ordenan los lotes para despachar con FEFO?", "Por fecha de vencimiento, del más próximo al más lejano", "Por fecha de ingreso", "Por el tamaño de las cajas", "FEFO se rige por el vencimiento."),
        ("abc", "{F} ¿Qué lote vence primero?", "El lote 2, que vence el 10", "El lote 1, que vence el 20", "El lote 3, que vence el 28", "El 10 es la fecha de vencimiento más próxima."),
        ("abc", "{F} ¿Cuál es el orden de salida con FEFO?", "Lote 2, lote 1, lote 3", "Lote 1, lote 2, lote 3", "Lote 3, lote 2, lote 1", "El orden va del vencimiento más próximo al más lejano: 10, 20, 28."),
        ("=", "{F} ¿Cuántas unidades en buen estado tiene el lote 2?", "30-4", "Buen estado = unidades del lote − dañadas.", " unidades"),
        ("=", "{F} ¿Cuántas unidades en buen estado hay en total entre los tres lotes?", "40+(30-4)+50", "Se suman los tres lotes, descontando las dañadas.", " unidades"),
        ("=", "{F} ¿Cuántas unidades faltan del pedido de 60 después de agotar el lote 2 en buen estado?", "60-(30-4)", "Faltante = pedido − unidades del lote 2 en buen estado.", " unidades"),
        ("abc", "{F} ¿De qué lote se completa el pedido luego del lote 2?", "Del lote 1, que vence el 20", "Del lote 3, que vence el 28", "De ninguno", "Según FEFO, el siguiente es el lote 1."),
        ("=", "{F} ¿Cuántas unidades se sacan del lote 1 para completar las 60?", "60-(30-4)", "Se saca lo que falta tras el lote 2.", " unidades"),
        ("=", "{F} ¿Cuál es el saldo del lote 1 tras el despacho?", "40-(60-(30-4))", "Saldo = unidades del lote − unidades sacadas.", " unidades"),
        ("abc", "{F} ¿Cuál es el código de ubicación del lote 1?", "Z2-E1-N2", "Z2-E3-N1", "Z2-E1-N1", "La ficha da Z2-E1-N2 para el lote 1."),
        ("abc", "{F} ¿Qué se hace con las 4 unidades con envase dañado del lote 2?", "Se separan, se registran con la causa y se informa a la jefatura", "Se despachan primero para sacarlas", "Se mezclan con el lote 3", "Un producto dañado nunca se despacha a un cliente."),
        ("abc", "{F} Un compañero propone despachar primero del lote 3 «porque es el más nuevo y está más a mano». ¿Qué corresponde?", "Rechazarlo: con FEFO sale primero el que vence antes", "Aceptarlo por comodidad", "Esperar al día siguiente", "Con FEFO el criterio es el vencimiento y no la comodidad."),
        ("abc", "{F} ¿Qué debe incluir el plan de despacho?", "Lote, ubicación, cantidad que sale y saldo", "El nombre del cliente y su teléfono", "Solo el nombre del producto", "El plan indica de dónde y cuánto sale, y lo que queda."),
    ],
    ctx=("abc", "Una bodeguera debe preparar un pedido de 60 unidades y revisa que el lote con vencimiento más próximo tenga 26 buenas. ¿Cómo sigue?", "Saca las 26 y completa con el siguiente lote por vencimiento", "Saca 60 del lote que está más a mano", "No despacha nada", "FEFO obliga a seguir el orden de vencimiento hasta completar el pedido."),
    sc=[
        ("En Logística: ¿cuál es el primer paso de un despacho por FEFO?", "Ordenar los lotes por vencimiento", "El orden define de dónde sale cada unidad."),
        ("¿Qué se hace con unidades dañadas?", "Se separan y se registran", "Las unidades dañadas no se despachan a clientes."),
        ("¿Qué incluye el plan de despacho?", "Lote, ubicación, cantidad y saldo", "Con eso se prepara el pedido sin errores."),
    ],
    op=("Con la Ficha 33, escribe el plan de despacho de las 60 unidades: lote, ubicación, cantidad que sale y saldo de cada lote, más el tratamiento de las unidades dañadas.\n{F}",
        "Lote 2 (Z2-E3-N1): salen 26 unidades buenas; saldo 0, más 4 dañadas separadas. Lote 1 (Z2-E1-N2): salen 34 unidades; saldo 6. Lote 3 (Z2-E1-N1): no se toca; saldo 50. Dañadas: se registran con su causa y se informa a la jefatura.",
        ["ordena por vencimiento", "calcula cantidades", "usa los códigos de ubicación", "trata las dañadas"],
        ["plan de despacho con tres lotes"],
        ["usar PEPS", "despachar dañadas", "olvidar saldos"],
        "Rehace las cantidades. Si despacha dañadas, pide corregir."),
    reinforce="Ordena en papel tres lotes con fechas que inventes y decide de cuál sale cada unidad de un pedido.",
    extend="Explica con un ejemplo inventado qué problema produciría despachar siempre el lote más nuevo.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 34 (datos de ejemplo, inventados) de «Distribuidora Andes del Sur». Inventario cíclico de una semana: se contaron 5 productos. Producto 1: sistema 120, físico 120. Producto 2: sistema 60, físico 58. Producto 3: sistema 200, físico 205. "
     "Producto 4: sistema 45, físico 45. Producto 5: sistema 90, físico 88. Ventas de ejemplo: el producto 1 salió 600 unidades en el mes con un stock promedio de 100 unidades. "
     "Sistema de localización: código zona-estante-nivel; la zona 1 tiene 6 estantes y cada estante tiene 4 niveles.")
build(
    O2, 4, F,
    use="Aprenderé a medir la exactitud de un inventario, a calcular la rotación simple de un producto y a asignar ubicaciones con código en papel.",
    prior=["Sé calcular diferencias y porcentajes.", "Conozco FEFO, PEPS y ABC.", "Sé leer un código de ubicación."],
    explain=[
        "La exactitud del inventario mide cuántos productos tienen el saldo del sistema igual al conteo físico. Se calcula así: productos sin diferencia × 100 ÷ productos contados. Un valor bajo indica que hay registros que corregir. Las diferencias se analizan con documentos antes de ajustar cualquier saldo.",
        "La rotación simple de un producto indica cuántas veces se renueva su stock: salidas del período ÷ stock promedio. Una rotación alta significa que sale rápido; una baja, que puede quedar guardado mucho tiempo. Sirve para clasificar productos como A, B o C y decidir su ubicación.",
        "Para asignar ubicaciones con código se cuenta cuántos puestos hay: estantes × niveles. Cada producto recibe un código zona-estante-nivel, sin repetirlo. La asignación y los ajustes de saldo los autoriza la jefatura con respaldo.",
    ],
    vocab=[("exactitud del inventario", "porcentaje de productos sin diferencia"), ("rotación simple", "salidas del período ÷ stock promedio"), ("stock promedio", "cantidad media que hubo en el período"), ("puesto", "lugar de un nivel de estante"), ("ajuste", "corrección de un saldo"), ("sin diferencia", "sistema igual al físico")],
    worked=[
        ("Exactitud", "En un conteo ficticio de 10 productos, 8 no tienen diferencia. ¿Cuál es la exactitud?", ["8 × 100 ÷ 10 = 80.", "Se expresa como 80 %."], "80 %"),
        ("Rotación", "Un producto ficticio tuvo 300 unidades de salida en el mes y un stock promedio de 100. ¿Cuál es su rotación?", ["Rotación = 300 ÷ 100.", "Resulta 3."], "3 veces"),
    ],
    mistakes=[("Calcular la exactitud con todos los productos de la bodega y no con los contados.", "El resultado no refleja el conteo.", "Usa solo los productos contados."),
              ("Ajustar el saldo del sistema para que coincida sin buscar la causa.", "Se esconde el error y se puede repetir.", "Analiza con documentos y corrige con autorización.")],
    T=[
        ("abc", "En Logística: ¿qué mide la exactitud del inventario?", "El porcentaje de productos cuyo sistema coincide con el físico", "El precio de los productos", "El número de estantes", "La exactitud compara los registros con la realidad."),
        ("=", "{F} Los productos 2, 3 y 5 tienen diferencia. ¿Cuántos de los 5 contados no tienen diferencia?", "5-3", "Sin diferencia = contados − con diferencia.", " productos"),
        ("=", "{F} ¿Cuál es la exactitud del conteo (sin diferencia × 100 ÷ contados)?", "2*100//5", "Exactitud = productos sin diferencia × 100 ÷ productos contados.", " %"),
        ("=", "{F} ¿Cuál es la diferencia del producto 2 (sistema − físico)?", "60-58", "Diferencia = sistema − físico.", " unidades"),
        ("=", "{F} ¿Cuál es la diferencia del producto 3 (sistema − físico)?", "200-205", "El resultado negativo indica que sobran unidades físicas.", " unidades"),
        ("abc", "{F} En el producto 3, ¿qué indica una diferencia negativa?", "Sobra producto físico respecto del sistema", "Falta producto físico", "El sistema está perfecto", "Si el físico supera al sistema, sobran unidades."),
        ("=", "{F} ¿Cuál es la rotación del producto 1 en el mes?", "600//100", "Rotación = salidas ÷ stock promedio.", " veces"),
        ("abc", "{F} ¿Qué indica una rotación de 6 veces al mes?", "Que el producto sale rápido y conviene ubicarlo a mano", "Que el producto casi no se mueve", "Que el producto está vencido", "Una rotación alta significa que hay mucha salida."),
        ("=", "{F} ¿Cuántos puestos hay en la zona 1 (6 estantes de 4 niveles)?", "6*4", "Puestos = estantes × niveles.", " puestos"),
        ("abc", "{F} ¿Cuál es el código del tercer nivel del estante 5 de la zona 1?", "Z1-E5-N3", "Z1-E3-N5", "Z5-E1-N3", "El formato es zona, estante y nivel."),
        ("abc", "{F} Un compañero ajusta el saldo del producto 2 a 58 sin investigar. ¿Qué falla?", "No se buscó la causa ni se pidió autorización", "Nada, porque coincide", "Debe ajustarse a 60", "El ajuste exige causa, documento y autorización."),
        ("abc", "{F} Dos productos reciben el mismo código de ubicación. ¿Qué problema se produce?", "No se sabe cuál es cuál al buscarlos", "Se ahorra espacio sin problemas", "Mejora la rotación", "El código debe ser único para localizar con rapidez."),
        ("abc", "{F} ¿Qué se hace con una diferencia de 2 unidades de menos en el producto 5?", "Se revisan los documentos y se informa a la jefatura antes de ajustar", "Se ajusta de inmediato", "Se ignora por ser pequeña", "Toda diferencia se analiza antes de ajustar."),
    ],
    ctx=("abc", "La jefatura pregunta si el inventario cíclico de la semana es confiable. ¿Qué responde un análisis?", "Tiene 40 % de exactitud: hay que revisar documentos y registros", "Está perfecto", "No se puede decir nada", "Con 2 de 5 productos sin diferencia, la exactitud es 40 %."),
    sc=[
        ("En Logística: ¿cómo se calcula la rotación simple?", "Salidas del período divididas por el stock promedio", "Mide cuántas veces se renueva el stock."),
        ("¿Qué indica una diferencia negativa?", "Que sobra producto físico", "El físico es mayor que el sistema."),
        ("¿Quién autoriza un ajuste de saldo?", "La jefatura, con respaldo", "No se ajusta sin causa y autorización."),
    ],
    op=("Con la Ficha 34, escribe un informe de seis líneas: exactitud del conteo, diferencias de los tres productos con diferencia, qué indica la del producto 3, rotación del producto 1 y qué harías antes de ajustar saldos.\n{F}",
        "Exactitud: 40 %. Diferencias: producto 2, 2 de menos; producto 3, 5 de más (sobra físico); producto 5, 2 de menos. El producto 3 indica una entrada no registrada posible. Rotación del producto 1: 6 veces. Antes de ajustar, revisaría los documentos y pediría autorización.",
        ["calcula exactitud y diferencias", "interpreta el signo", "calcula la rotación", "indica el proceso de ajuste"],
        ["informe de seis líneas"],
        ["ajustar sin causa", "confundir signos", "no calcular exactitud"],
        "Rehace los cálculos. Si ajusta sin causa, pide agregar la revisión."),
    reinforce="Calcula en papel la exactitud de un conteo ficticio de 8 productos con 6 sin diferencia.",
    extend="Explica con un ejemplo inventado cómo cambia la rotación si el stock promedio se duplica.",
)
