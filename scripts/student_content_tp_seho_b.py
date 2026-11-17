"""Hotelería TP 3.º y 4.º medio: OAE-03 (reservas, check-in y check-out con protocolos y protección al consumidor) y OAE-04 (supervisar el servicio de habitaciones e informes diarios). Todo en papel: planillas, tarifas y estados de habitaciones inventados y rotulados «de ejemplo»; la limpieza y los productos químicos solo como reglas generales."""
from __future__ import annotations

from tp_seho_common import build

O3 = "TP-SEHO-3y4-OAE-03"
O4 = "TP-SEHO-3y4-OAE-04"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: no reemplaza la práctica con un instructor ni la norma vigente."
QUI = " Esto es aprendizaje conceptual en papel: la limpieza con productos químicos y el uso de equipos exigen instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-03, clase 1
F = ("Ficha 11 (condiciones de ejemplo, inventadas). «Hotel Marea de Ejemplo»: habitación doble, $48.000 por noche, con impuestos y desayuno incluidos (tarifa final de ejemplo); una habitación doble aloja a 2 personas. "
     "Garantía de la reserva: anticipo de $20.000. Cancelación sin costo hasta 48 horas antes de la llegada; después se cobra la primera noche. Si la persona no llega y no avisa (no presentación), también se cobra la primera noche. "
     "Check-in desde las 15:00 y check-out hasta las 12:00. Medios de pago: efectivo, tarjeta o transferencia. Datos para reservar: nombre completo, documento de identidad, teléfono o correo, fechas y cantidad de personas.")
build(
    O3, 1, F,
    use="Aprenderé qué es una reserva, qué condiciones se informan antes de confirmarla, cómo se cuidan los datos del cliente y qué reglas generales protegen al consumidor.",
    prior=["Sé multiplicar y restar dinero.", "Conozco los servicios de un hotel.", "Sé leer una ficha de condiciones."],
    explain=[
        "Una reserva es el compromiso entre el hotel y el cliente: el hotel mantiene una habitación para unas fechas y el cliente acepta las condiciones. Para asegurarla se puede pedir una garantía, como un anticipo, que es un pago parcial adelantado. El check-in es la entrada del huésped a su habitación y el check-out es su salida. Hoy los hoteles usan un sistema de administración hotelera (un programa que registra reservas, ocupación y cuentas); en este cuaderno el mismo trabajo se hace en papel.",
        "Antes de confirmar, se informa con claridad el precio total, qué incluye, las condiciones de pago, la política de cancelación (cuándo se puede cancelar sin costo) y qué pasa si el cliente no llega. Informar con claridad es parte de la protección al consumidor: el cliente decide con datos completos y sin sorpresas, según la norma vigente.",
        "Los datos del cliente, como su documento y su teléfono, son personales y confidenciales: se piden solo los necesarios y no se comparten. Nunca se pide por teléfono o correo la clave secreta de una tarjeta." + LIM,
    ],
    vocab=[("reserva", "compromiso de mantener una habitación para unas fechas bajo ciertas condiciones"), ("anticipo", "pago parcial adelantado que garantiza la reserva"), ("política de cancelación", "reglas sobre cuándo se puede cancelar sin costo"), ("no presentación (no-show)", "cuando el cliente no llega y no avisa"), ("protección al consumidor", "reglas que aseguran información clara y trato justo al cliente"), ("sistema de administración hotelera", "programa que registra reservas, ocupación y cuentas del hotel")],
    worked=[
        ("Calcular el saldo", "Una reserva de ejemplo cuesta $90.000 en total y el cliente dejó $30.000 de anticipo. ¿Cuánto le falta pagar?", ["Saldo = total − anticipo.", "90.000 − 30.000 = 60.000."], "$60.000"),
        ("Aplicar una política de cancelación", "Un hotel de ejemplo permite cancelar sin costo hasta 24 horas antes de la llegada. Un cliente cancela 3 días antes. ¿Tiene costo?", ["3 días son 72 horas, más que 24.", "Cancela dentro del plazo."], "No tiene costo"),
    ],
    mistakes=[("Confirmar una reserva diciendo solo el precio por noche, sin explicar la política de cancelación.", "El cliente no conoce las condiciones y puede reclamar un cobro que no esperaba.", "Informa el precio total, qué incluye, las condiciones de pago y de cancelación antes de confirmar."),
              ("Pedir por teléfono la clave secreta de la tarjeta para «asegurar» la reserva.", "La clave es un dato privado que nunca se entrega; pedirla pone en riesgo al cliente.", "Pide solo los datos de la ficha y usa un medio de pago seguro.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una reserva?", "El compromiso de mantener una habitación para unas fechas bajo ciertas condiciones", "El pago final de la estadía", "El registro de salida del huésped", "La reserva se hace antes de la llegada; el pago final y la salida son otras etapas."),
        ("abc", "{F} ¿Cuánto es el anticipo que garantiza la reserva?", "$20.000", "$48.000", "$12.000", "La ficha fija un anticipo de $20.000; $48.000 es el precio de una noche."),
        ("abc", "{F} ¿Hasta cuándo se puede cancelar sin costo?", "Hasta 48 horas antes de la llegada", "Hasta 24 horas antes de la llegada", "Hasta el día de la llegada", "La ficha fija 48 horas antes; después se cobra la primera noche."),
        ("=", "{F} Un cliente reserva 3 noches en habitación doble. ¿Cuánto es el total de la estadía?", "48000*3", "Se multiplica la tarifa por noche por el número de noches.", " pesos"),
        ("=", "{F} Con el total de 3 noches y el anticipo de la ficha, ¿cuánto falta pagar?", "48000*3-20000", "Al total de la estadía se le resta el anticipo.", " pesos"),
        ("abc", "{F} Un cliente cancela con 24 horas de anticipación. ¿Qué corresponde cobrar?", "La primera noche, porque canceló fuera del plazo de 48 horas", "Nada, porque canceló antes de llegar", "Todas las noches reservadas", "El plazo sin costo es de 48 horas; con 24 horas se cobra la primera noche."),
        ("abc", "¿Qué debe informarse antes de confirmar una reserva?", "El precio total, qué incluye, las condiciones de pago y de cancelación", "Solo el precio por noche", "Solo el nombre de quien atiende", "La protección al consumidor exige informar con claridad todas las condiciones."),
        ("abc", "¿Qué dato no corresponde pedir nunca por teléfono o correo al reservar?", "La clave secreta de la tarjeta", "El nombre completo", "Las fechas de llegada y salida", "La clave es privada; el nombre y las fechas son datos propios de la reserva."),
        ("=", "El hotel tiene 30 habitaciones dobles y para una noche hay 21 reservadas. ¿Cuántas quedan disponibles?", "30-21", "Al total de habitaciones se le restan las reservadas.", " habitaciones"),
        ("abc", "{F} Una persona reservó, no llegó y no avisó. ¿Qué corresponde según la ficha?", "Cobrar la primera noche por no presentación", "No cobrar nada", "Cobrar toda la estadía y además una multa", "La ficha establece que la no presentación se cobra con la primera noche."),
        ("abc", "{F} Un cliente quiere reservar una habitación doble para 5 personas. ¿Qué corresponde?", "Informar que la doble aloja a 2 personas y ofrecer otras habitaciones disponibles", "Confirmar la reserva sin decir nada", "Decirle que no puede alojarse en ningún hotel", "La capacidad se informa con claridad y se ofrece una alternativa."),
        ("abc", "Alguien llama y pregunta si una persona conocida tiene una reserva en el hotel. ¿Qué respondes?", "Que no puedes confirmar datos de los clientes, y ofrecer tomar un mensaje", "Que sí, y a qué fecha llega", "Que sí, pero sin decir la fecha", "Confirmar que alguien es cliente ya revela un dato personal."),
        ("abc", "{F} Un cliente reclama que le cobraron más de lo que se le informó. ¿Qué corresponde primero?", "Revisar la reserva y las condiciones informadas, y corregir el cobro si hubo un error", "Decirle que el sistema nunca se equivoca", "Pedirle que pague y reclame después", "Se verifica con los datos de la reserva y se corrige si corresponde."),
    ],
    ctx=("abc", "{F} Un cliente llama y dice: «Quiero reservar dos noches, ¿cuánto sale?». ¿Qué respuesta cumple con informar con claridad?", "«Son $96.000 con desayuno e impuestos; con $20.000 de anticipo se garantiza; se cancela sin costo hasta 48 horas antes»", "«Son $48.000, después vemos el resto»", "«Mándeme su tarjeta con la clave»", "Dar el total, lo que incluye, la garantía y la cancelación evita sorpresas."),
    sc=[
        ("En Hotelería: ¿qué es un anticipo?", "Un pago parcial adelantado que garantiza la reserva", "Se paga antes de la llegada y se descuenta del total."),
        ("¿Qué se informa antes de confirmar una reserva?", "Precio total y condiciones de pago y cancelación", "El cliente debe decidir con datos completos."),
        ("¿Se puede pedir la clave de la tarjeta por teléfono?", "No", "La clave es un dato privado que nunca se entrega."),
    ],
    op=("Condiciones de ejemplo de otro hotel: habitación triple a $60.000 por noche, desayuno incluido; anticipo de $25.000; cancelación sin costo hasta 72 horas antes de la llegada; si no llega, se cobra la primera noche. "
        "Un cliente quiere reservar 4 noches para 3 personas y pregunta por teléfono. Escribe: lo que le informarías antes de confirmar (al menos cuatro datos), el total, el saldo después del anticipo, y una regla de privacidad que aplicarías.",
        "Informaría: tarifa de $60.000 por noche con desayuno, capacidad para 3 personas, anticipo de $25.000, cancelación sin costo hasta 72 horas antes, no presentación con cobro de la primera noche. Total: 60.000 × 4 = 240.000. Saldo: 240.000 − 25.000 = 215.000. Privacidad: pediría solo los datos necesarios y no la clave de la tarjeta, y no comentaría sus datos con terceros.",
        ["informa precio, inclusiones, anticipo y cancelación", "calcula bien total y saldo", "nombra una regla de privacidad"],
        ["hoja con la información, los dos cálculos y la regla"],
        ["no mencionar la cancelación", "restar el anticipo antes de multiplicar", "pedir datos innecesarios"],
        "Pregunta: «¿qué pasa si el cliente cancela con 48 horas de aviso?». Si no responde que no tiene costo, repasa el plazo de 72 horas de este hotel."),
    reinforce="Escribe tres condiciones de reserva de un hotel inventado y redacta una frase para informarlas a un cliente por teléfono.",
    extend="Explica por qué informar la política de cancelación antes de confirmar protege tanto al cliente como al hotel.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 12 (habitaciones y tarifas de ejemplo, inventadas; todas con desayuno e impuestos incluidos). «Hotel Marea de Ejemplo» tiene 24 habitaciones: 6 simples (1 persona, 1 cama), $35.000 por noche; 8 dobles (2 personas; matrimonial con 1 cama grande o twin con 2 camas), $48.000; "
     "6 triples (3 personas), $60.000; y 4 suites (hasta 4 personas, con sala de estar), $90.000. Ficha de reserva: nombre completo, documento, fecha de llegada y de salida, tipo de habitación, cantidad de personas, tarifa, anticipo y observaciones.")
build(
    O3, 2, F,
    use="Aprenderé los documentos y conceptos de una reserva: tipos de habitación, tarifa, noches, disponibilidad, ocupación y ficha de registro del huésped.",
    prior=["Conozco la reserva y sus condiciones.", "Sé calcular porcentajes simples.", "Sé leer una tabla."],
    explain=[
        "Las habitaciones se clasifican por capacidad y camas: simple (1 persona), doble (2 personas), triple (3) y suite (más espacio y sala de estar). En una doble matrimonial hay una cama grande y en una doble twin hay dos camas separadas. La tarifa es el precio por noche de cada tipo; el plan indica qué incluye, como el desayuno.",
        "Las noches se cuentan desde la llegada hasta la salida: si llega el día 10 y sale el día 13, son 3 noches. El total de alojamiento es la tarifa por noche por el número de noches. La disponibilidad es cuántas habitaciones hay libres para vender en una fecha. La ocupación es el porcentaje de habitaciones ocupadas: ocupadas × 100 ÷ total.",
        "La ficha de reserva es el documento que respalda el acuerdo: lleva los datos del cliente, las fechas, el tipo de habitación y las condiciones. Una ficha incompleta genera errores. Los datos de la ficha son confidenciales y solo los usa el personal autorizado." + LIM,
    ],
    vocab=[("tarifa", "precio por noche de un tipo de habitación"), ("disponibilidad", "habitaciones libres que se pueden vender en una fecha"), ("ocupación", "porcentaje de habitaciones ocupadas respecto del total"), ("doble matrimonial", "habitación para 2 personas con una cama grande"), ("doble twin", "habitación para 2 personas con dos camas separadas"), ("ficha de reserva", "documento con los datos y condiciones de una reserva")],
    worked=[
        ("Contar noches", "Un cliente de ejemplo llega el día 5 y sale el día 9. ¿Cuántas noches se aloja?", ["Noches = día de salida − día de llegada.", "9 − 5 = 4."], "4 noches"),
        ("Calcular la ocupación", "Un hotel de ejemplo tiene 20 habitaciones y 12 están ocupadas. ¿Cuál es la ocupación?", ["Ocupación = ocupadas × 100 ÷ total.", "12 × 100 ÷ 20 = 60."], "60 %"),
    ],
    mistakes=[("Contar las noches sumando también el día de salida.", "El día de salida no es una noche de alojamiento; se cuentan solo las noches dormidas.", "Resta el día de llegada al día de salida."),
              ("Dejar en blanco la fecha de salida de la ficha «porque el cliente todavía no sabe».", "Sin esa fecha no se sabe cuántas noches cobrar ni cuándo liberar la habitación.", "Registra una fecha provisoria y anótala como tal en observaciones.")],
    T=[
        ("abc", "En Hotelería: ¿qué es la disponibilidad?", "Las habitaciones libres que se pueden vender en una fecha", "El precio de la tarifa de una habitación", "La cantidad de huéspedes que se han ido", "La disponibilidad es lo que queda libre para vender, no el precio ni las salidas."),
        ("abc", "{F} ¿Cuántas personas aloja una habitación triple?", "3 personas", "2 personas", "4 personas", "La ficha indica que la triple es para 3 personas; la doble es para 2 y la suite hasta 4."),
        ("abc", "{F} ¿Qué tipo de habitación doble tiene dos camas separadas?", "La doble twin", "La doble matrimonial", "La simple", "La twin tiene dos camas; la matrimonial tiene una cama grande."),
        ("=", "Un huésped llega el día 12 y sale el día 15. ¿Cuántas noches se aloja?", "15-12", "Se resta el día de llegada al día de salida.", " noches"),
        ("=", "{F} Una pareja se aloja 4 noches en una suite. ¿Cuánto es el total de alojamiento?", "90000*4", "Se multiplica la tarifa de la suite por el número de noches.", " pesos"),
        ("=", "{F} Hoy hay 18 de las 24 habitaciones ocupadas. ¿Qué porcentaje de ocupación tiene el hotel?", "18*100//24", "Se multiplican las ocupadas por 100 y se dividen por el total de habitaciones.", " %"),
        ("abc", "{F} Una familia de 4 personas quiere alojarse en una sola habitación. ¿Qué tipo se les ofrece?", "Una suite", "Una triple", "Una doble", "Solo la suite aloja hasta 4 personas según la ficha."),
        ("=", "{F} ¿Cuántas habitaciones del hotel pueden alojar a 3 personas o más?", "6+4", "Se suman las triples y las suites.", " habitaciones"),
        ("abc", "{F} Una persona reservó una habitación doble y llega con dos acompañantes. ¿Qué corresponde?", "Verificar si hay una triple libre e informar la diferencia de tarifa antes de cambiar", "Aceptar a los tres en la doble sin avisar", "Decirle que no puede alojarse nunca", "Se informa la capacidad y la diferencia de tarifa para que el cliente decida."),
        ("abc", "Una ficha de reserva queda sin fecha de salida. ¿Qué riesgo tiene?", "No se sabe cuántas noches cobrar ni cuándo liberar la habitación", "Ninguno, porque se adivina al final", "Que el cliente cambie de nombre", "Sin la fecha de salida no se calcula el total ni se planifica la disponibilidad."),
        ("=", "{F} Dos noches en una habitación triple frente a dos noches en una doble. ¿Cuántos pesos más cuesta la triple?", "(60000-48000)*2", "Se calcula la diferencia de tarifa por noche y se multiplica por las noches.", " pesos"),
        ("abc", "Una compañera quiere sacar fotos de las fichas de reserva con su celular para estudiarlas en su casa. ¿Qué respondes?", "Que no, porque contienen datos personales y deben usarse solo en el lugar autorizado", "Que sí, mientras no las comparta con nadie", "Que sí, si borra las fotos después de un mes", "Los datos de los huéspedes son confidenciales y no salen del lugar de trabajo."),
        ("abc", "{F} Un cliente pide una habitación simple para 2 personas porque «es más barata». ¿Qué corresponde?", "Explicar que la simple es para 1 persona y ofrecer la doble", "Aceptar, porque entre dos pueden dormir en una cama", "Cobrar la tarifa de la simple y alojar a ambos", "La capacidad se respeta; no se vende una habitación para más personas de las que aloja."),
    ],
    ctx=("abc", "{F} Una pareja con una persona en silla de ruedas pide una doble. La ficha no indica cuál es accesible. ¿Qué haces?", "Consultar cuál habitación doble es accesible antes de confirmar y registrarlo en observaciones", "Asignar la primera doble libre", "Decirles que no hay habitaciones accesibles sin revisar", "Se verifica la accesibilidad antes de comprometer la habitación."),
    sc=[
        ("En Hotelería: ¿cómo se cuentan las noches de una estadía?", "Restando el día de llegada al de salida", "El día de salida no es una noche de alojamiento."),
        ("En un hotel, ¿cómo se calcula el porcentaje de ocupación de una noche?", "Ocupadas por 100, dividido por el total", "Es el porcentaje de habitaciones ocupadas."),
        ("¿Qué documento respalda los datos y condiciones de una reserva?", "La ficha de reserva", "Reúne los datos del cliente y las condiciones acordadas."),
    ],
    op=("Ficha de ejemplo de otro hotel: simple $30.000, doble $42.000, suite $80.000, por noche, con desayuno incluido; el hotel tiene 20 habitaciones y hoy hay 13 ocupadas. "
        "Llega una pareja el día 8 y sale el día 12, y pide una doble. Calcula: las noches, el total de alojamiento, la ocupación del hotel hoy, y escribe los datos que anotarías en la ficha de reserva.",
        "Noches: 12 − 8 = 4. Total: 42.000 × 4 = 168.000. Ocupación: 13 × 100 ÷ 20 = 65 %. Ficha: nombres completos, documentos, llegada el día 8, salida el día 12, tipo doble, 2 personas, tarifa $42.000, anticipo si corresponde y observaciones.",
        ["calcula noches y total", "calcula la ocupación", "lista los datos de la ficha"],
        ["hoja con tres cálculos y la lista de datos"],
        ["contar 5 noches", "dividir al revés la ocupación", "olvidar el tipo de habitación o la tarifa en la ficha"],
        "Pregunta: «¿por qué el día de salida no cuenta como noche?». Si no responde que no se duerme esa noche, repasa el conteo."),
    reinforce="Haz una tabla con los cuatro tipos de habitación de la ficha, su capacidad y su tarifa.",
    extend="Explica por qué conviene registrar las observaciones, como una necesidad de accesibilidad, en la ficha de reserva.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 13 (planilla de reservas de ejemplo, inventada). Noches: lunes (L), martes (M), miércoles (X) y jueves (J). Reservado: 101 (doble): L y M. 102 (doble): M y X. 103 (doble): libre las 4 noches. 104 (triple): X y J. 105 (suite): solo L. "
     "Tarifas: doble $48.000 por noche, triple $60.000. Solicitud: un cliente llama y pide 2 habitaciones dobles, entrando el lunes y saliendo el miércoles.")
build(
    O3, 3, F,
    use="Aprenderé a analizar una planilla de reservas frente a una solicitud, detectar conflictos y ofrecer alternativas sin vender dos veces la misma habitación.",
    prior=["Conozco disponibilidad y ocupación.", "Sé contar noches.", "Sé leer una planilla."],
    explain=[
        "Una planilla de reservas muestra, por habitación y por noche, si está reservada o libre. Para atender una solicitud, primero se calcula qué noches pide el cliente y después se busca qué habitaciones del tipo pedido están libres en todas esas noches. Una habitación libre solo una de las dos noches no sirve para una estadía de dos noches seguidas.",
        "La sobreventa (overbooking) es vender más habitaciones de las que existen para una fecha. Provoca que un huésped llegue y no tenga habitación, y por eso se evita: cada reserva o cambio se anota de inmediato en la planilla. Si no hay disponibilidad del tipo pedido, se ofrece una alternativa, como otro tipo de habitación con su diferencia de tarifa, y el cliente decide.",
        "Se registra la decisión del cliente y se confirma por escrito. Los datos de la planilla son confidenciales: no se informa quién ocupa cada habitación." + LIM,
    ],
    vocab=[("planilla de reservas", "tabla que muestra qué habitaciones están reservadas o libres cada noche"), ("conflicto", "cuando dos reservas piden la misma habitación en la misma noche"), ("sobreventa (overbooking)", "vender más habitaciones de las que existen para una fecha"), ("alternativa", "otra opción que se ofrece cuando no hay lo pedido"), ("confirmar por escrito", "enviar al cliente el detalle acordado para que lo verifique")],
    worked=[
        ("Buscar una habitación libre dos noches", "En una planilla de ejemplo, la habitación A está ocupada la noche 1 y la B está ocupada la noche 2. El cliente pide 2 noches seguidas desde la noche 1. ¿Sirve alguna?", ["A no sirve porque la noche 1 está ocupada.", "B no sirve porque la noche 2 está ocupada."], "Ninguna sirve para las dos noches"),
        ("Contar noches pedidas", "Un cliente de ejemplo entra el viernes y sale el domingo. ¿Qué noches necesita?", ["Duerme el viernes y el sábado.", "El domingo se va."], "Viernes y sábado, 2 noches"),
    ],
    mistakes=[("Confirmar dos habitaciones dobles «porque seguro alguien cancela».", "Es sobreventa: si nadie cancela, un huésped llega sin habitación.", "Confirma solo lo que hay disponible y ofrece alternativas por escrito."),
              ("No anotar de inmediato un cambio de fechas en la planilla.", "Otra persona puede vender esa habitación sin saber que ya está comprometida.", "Registra cada cambio al momento de acordarlo.")],
    T=[
        ("abc", "En Hotelería: ¿qué es la sobreventa (overbooking)?", "Vender más habitaciones de las que existen para una fecha", "Vender habitaciones muy baratas", "Cobrar una noche más de lo reservado", "La sobreventa supera la capacidad real; las otras opciones son cobros o descuentos."),
        ("=", "{F} El cliente entra el lunes y sale el miércoles. ¿Cuántas noches pide?", "3-1", "Se resta el día de llegada (lunes, día 1) al de salida (miércoles, día 3).", " noches"),
        ("abc", "{F} ¿Cuántas habitaciones dobles están libres la noche del martes?", "1 (la 103)", "2 (la 102 y la 103)", "3 (las tres)", "El martes la 101 y la 102 están reservadas; solo la 103 está libre."),
        ("abc", "{F} ¿Cuántas dobles están libres las dos noches (lunes y martes)?", "1, la 103", "2, la 102 y la 103", "Ninguna", "La 102 está libre el lunes pero reservada el martes; solo la 103 sirve las dos noches."),
        ("abc", "{F} ¿Qué habitación de otro tipo está libre el lunes y el martes?", "La 104, triple", "La 105, suite", "Ninguna", "La 105 está reservada el lunes; la 104 solo está ocupada miércoles y jueves."),
        ("=", "{F} Si se asignan la 103 y la 104 por las dos noches, ¿cuál es el costo total?", "48000*2+60000*2", "Se calcula cada habitación por sus dos noches y se suman.", " pesos"),
        ("abc", "{F} ¿Qué corresponde ofrecer al cliente?", "La 103 doble y la 104 triple, informando la diferencia de tarifa, para que decida", "Confirmar dos dobles igual", "Rechazar la solicitud sin ofrecer nada", "Hay una alternativa verificada en la planilla y el cliente decide con información."),
        ("abc", "{F} Un compañero dice: «Confirmemos las dos dobles, algo se arreglará». ¿Qué observación corresponde?", "Es sobreventa: solo hay una doble libre las dos noches", "Es buena idea, porque siempre hay cancelaciones", "No pasa nada, porque la 102 se desocupa el lunes", "Confirmar sin disponibilidad real puede dejar a un huésped sin habitación."),
        ("=", "{F} La planilla muestra 5 habitaciones durante 4 noches. ¿Cuántas noches-habitación están reservadas en total?", "2+2+0+2+1", "Se suman las noches reservadas de cada habitación.", " noches-habitación"),
        ("=", "{F} Si en la planilla hay 7 noches-habitación reservadas de un total de 20, ¿qué porcentaje está ocupado?", "7*100//20", "Se multiplican las reservadas por 100 y se dividen por el total de 20.", " %"),
        ("abc", "{F} El cliente que reservó la 105 el lunes pide quedarse también el martes. ¿Se puede?", "Sí, porque la 105 no está reservada el martes", "No, porque la suite siempre se ocupa", "No, porque ya salió de la habitación el lunes y no puede volver a ocuparla", "La planilla muestra la 105 reservada solo el lunes; el martes está libre."),
        ("abc", "{F} El cliente de la 103 pregunta qué otra persona ocupa la 102. ¿Qué respondes?", "Que no puedes entregar datos de otros huéspedes", "Que se lo dices porque es solo un nombre", "Que se lo dices si promete no contarlo", "Los datos de los huéspedes son confidenciales."),
        ("abc", "Un cambio de fechas acordado por teléfono no se anotó en la planilla. ¿Qué riesgo produce?", "Que la misma habitación se venda dos veces", "Que el cliente no pueda cancelar", "Que suban las tarifas", "Sin registro, otro recepcionista ve la habitación libre y la ofrece."),
    ],
    ctx=("abc", "{F} El cliente dice: «Si no hay dos dobles, cancelo todo». Hay una doble y una triple libres. ¿Qué haces?", "Explicar la alternativa con su costo, respetar su decisión y registrar lo que acuerde", "Insistir en que la acepte", "Confirmar dos dobles para que no se vaya", "Se informa y se respeta la decisión; no se vende lo que no existe."),
    sc=[
        ("En Hotelería: ¿qué es un conflicto de reservas?", "Dos reservas para la misma habitación y noche", "Ocurre cuando una habitación se compromete dos veces."),
        ("¿Qué se hace si no hay el tipo de habitación pedido?", "Se ofrece una alternativa", "El cliente decide con datos completos."),
        ("¿Cuándo se anota un cambio de fechas?", "De inmediato", "Así se evita vender dos veces la misma habitación."),
    ],
    op=("Planilla de ejemplo: noches L, M, X. Habitación 201 (doble): reservada L. 202 (doble): reservada X. 203 (doble): reservada L, M y X. 204 (triple): libre. Tarifas: doble $45.000, triple $58.000. "
        "Un cliente pide una doble para L y M (sale el miércoles). Revisa la planilla y escribe: qué habitaciones dobles sirven, qué opción le ofrecerías, el costo de dos noches, y qué anotarías.",
        "Dobles: la 201 está ocupada el lunes, la 202 está libre lunes y martes, la 203 está ocupada. Sirve la 202. Costo: 45.000 × 2 = 90.000. Anotaría la reserva de la 202 para L y M con los datos del cliente, el costo y las condiciones.",
        ["revisa las dobles noche por noche", "elige la habitación correcta y calcula", "indica qué se anota"],
        ["hoja con el análisis, la elección y el registro"],
        ["elegir la 201 sin mirar el lunes", "no calcular el costo", "no registrar la reserva"],
        "Pregunta: «¿por qué no sirve la 201?». Si no responde que está reservada el lunes, repasa la lectura de la planilla."),
    reinforce="Dibuja una planilla de 4 habitaciones y 3 noches con algunas reservas y busca una habitación libre para 2 noches seguidas.",
    extend="Explica por qué la sobreventa perjudica a los huéspedes y a la reputación del hotel.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 14 (datos de ejemplo, inventados). Tarifas por noche, con impuestos y desayuno incluidos: doble $48.000, triple $60.000. Convenio con una empresa de ejemplo: 10 % de descuento sobre la tarifa, para sus trabajadores acreditados. "
     "Anticipo: $20.000. El hotel tiene 20 habitaciones y hoy hay 15 ocupadas. Objetivo de ocupación del hotel (de ejemplo): 80 %.")
build(
    O3, 4, F,
    use="Aprenderé a calcular una estadía con descuento por convenio, anticipo y saldo, y a medir la ocupación frente a un objetivo.",
    prior=["Sé calcular noches y totales.", "Sé calcular un porcentaje exacto.", "Conozco la ficha de reserva."],
    explain=[
        "Un convenio es un acuerdo entre el hotel y una empresa o grupo para ofrecer una tarifa especial a sus integrantes. Para aplicar un descuento porcentual, se calcula el porcentaje de la tarifa (tarifa × porcentaje ÷ 100) y se resta de la tarifa. Por ejemplo, el 10 % de $20.000 es $2.000, y la tarifa con descuento es $18.000. El descuento se aplica solo si el cliente acredita que pertenece al convenio.",
        "Para obtener el total de una estadía se multiplica la tarifa por noche (ya con descuento) por el número de noches. El saldo es el total menos el anticipo. Todo debe quedar en la ficha de reserva, y el cliente debe conocer el total antes de confirmar.",
        "La ocupación se mide con ocupadas × 100 ÷ total y se compara con el objetivo del hotel: si está bajo el objetivo, faltan habitaciones por ocupar. Un cálculo bien hecho se revisa dos veces antes de informarlo." + LIM,
    ],
    vocab=[("convenio", "acuerdo con una empresa o grupo para ofrecer una tarifa especial"), ("descuento porcentual", "rebaja calculada como porcentaje de la tarifa"), ("acreditar", "demostrar con un documento que se pertenece al convenio"), ("saldo", "monto que falta pagar después del anticipo"), ("objetivo de ocupación", "porcentaje de ocupación que el hotel quiere alcanzar")],
    worked=[
        ("Calcular una tarifa con descuento", "Una tarifa de ejemplo es $30.000 y el convenio da 20 % de descuento. ¿Cuál es la tarifa final?", ["20 % de 30.000 es 30.000 × 20 ÷ 100 = 6.000.", "30.000 − 6.000 = 24.000."], "$24.000"),
        ("Calcular una noche faltante", "Para llegar a un objetivo, un hotel de ejemplo de 10 habitaciones quiere 70 % de ocupación y tiene 6 ocupadas. ¿Cuántas más necesita?", ["70 % de 10 habitaciones son 7.", "7 − 6 = 1."], "1 habitación más"),
    ],
    mistakes=[("Aplicar el descuento del convenio sin pedir el documento que acredita al cliente.", "Cualquier persona podría pedir la rebaja y el hotel perdería ingresos sin respaldo.", "Pide y registra el documento que acredita el convenio."),
              ("Restar el anticipo de la tarifa de una noche en vez del total de la estadía.", "El anticipo se descuenta del total, no de una sola noche.", "Calcula primero el total de la estadía y luego resta el anticipo.")],
    T=[
        ("abc", "En Hotelería: ¿qué es un convenio con una empresa?", "Un acuerdo para ofrecer una tarifa especial a sus integrantes", "Un permiso para no pagar el alojamiento", "Un cambio de habitación sin costo", "El convenio fija una tarifa especial acordada, no libera del pago."),
        ("=", "{F} ¿Cuántos pesos de descuento por noche recibe un trabajador acreditado en una habitación doble?", "48000*10//100", "El descuento es el 10 % de la tarifa de la doble.", " pesos"),
        ("=", "{F} ¿Cuál es la tarifa final por noche de la doble con el convenio?", "48000-48000*10//100", "A la tarifa se le resta el descuento del 10 %.", " pesos"),
        ("=", "{F} Un trabajador acreditado se aloja 3 noches en una doble. ¿Cuánto es el total de la estadía?", "(48000-48000*10//100)*3", "Se multiplica la tarifa con descuento por las noches.", " pesos"),
        ("=", "{F} Con el total de la pregunta anterior y el anticipo de la ficha, ¿cuánto falta pagar?", "(48000-48000*10//100)*3-20000", "Al total de la estadía se le resta el anticipo.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de ocupación tiene el hotel hoy?", "15*100//20", "Se multiplican las ocupadas por 100 y se dividen por el total.", " %"),
        ("abc", "{F} ¿Alcanza hoy el hotel su objetivo de ocupación?", "No: tiene 75 % y el objetivo es 80 %", "Sí: tiene 85 %", "Sí: tiene 75 %, que supera el 80 %", "75 % es menor que el objetivo de 80 %, así que no lo alcanza."),
        ("=", "{F} ¿Cuántas habitaciones ocupadas equivalen al objetivo del 80 %?", "20*80//100", "Se calcula el 80 % del total de habitaciones.", " habitaciones"),
        ("=", "{F} ¿Cuántas habitaciones más deben ocuparse para llegar al objetivo?", "20*80//100-15", "A las habitaciones del objetivo se les restan las ya ocupadas.", " habitaciones"),
        ("=", "{F} Un trabajador acreditado se aloja 4 noches en una triple. ¿Cuánto es el total con el descuento?", "(60000-60000*10//100)*4", "Se aplica el 10 % de descuento a la tarifa y se multiplica por las noches.", " pesos"),
        ("abc", "{F} Una recepcionista calculó el total de un trabajador acreditado en 3 noches dobles como 48.000 × 3 − 20.000. ¿Qué error cometió?", "No aplicó el descuento del convenio", "Restó mal el anticipo", "Contó mal las noches", "Faltó el 10 % de descuento sobre la tarifa antes de multiplicar."),
        ("abc", "{F} Una persona que no es trabajadora de la empresa pide el descuento «porque conoce a alguien allí». ¿Qué corresponde?", "Explicar que el descuento exige acreditar la pertenencia al convenio, y ofrecer la tarifa normal", "Aplicar el descuento para evitar un reclamo", "Pedirle que traiga a la persona conocida", "El convenio se aplica solo con acreditación documentada."),
        ("=", "Una estadía comienza el día 28 y termina el día 2 del mes siguiente. El mes tiene 30 días. ¿Cuántas noches son?", "(30-28)+2", "Se cuentan las noches hasta el fin del mes y las del mes siguiente.", " noches"),
    ],
    ctx=("abc", "{F} Una trabajadora acreditada llama para reservar 2 noches en una doble y pregunta cuánto saldrá en total. ¿Qué respuesta es correcta?", "$86.400 en total, con el descuento del 10 % ya aplicado, y $66.400 después del anticipo", "$96.000 en total, sin descuento", "$76.400 en total", "Se aplica el descuento a la tarifa, se multiplica por las noches y después se resta el anticipo."),
    sc=[
        ("En Hotelería: ¿cómo se calcula un descuento porcentual?", "Tarifa por porcentaje, dividido por 100", "Así se obtiene la parte de la tarifa que se rebaja."),
        ("¿Qué se resta del total para obtener el saldo?", "El anticipo", "El saldo es lo que falta pagar."),
        ("¿Qué se pide para aplicar un convenio?", "Un documento que acredite al cliente", "Sin acreditación no se aplica el descuento."),
    ],
    op=("Datos de ejemplo de otro hotel: doble $40.000 por noche; convenio con 15 % de descuento para los integrantes acreditados de un club; anticipo $15.000. Hotel de 40 habitaciones con 28 ocupadas; objetivo 75 %. "
        "Una integrante acreditada se aloja 3 noches en una doble. Calcula: la tarifa con descuento, el total, el saldo después del anticipo, y la ocupación del hotel frente al objetivo.",
        "Descuento: 40.000 × 15 ÷ 100 = 6.000; tarifa final 34.000. Total: 34.000 × 3 = 102.000. Saldo: 102.000 − 15.000 = 87.000. Ocupación: 28 × 100 ÷ 40 = 70 %, menor que el objetivo de 75 %; para el objetivo harían falta 30 habitaciones ocupadas, es decir 2 más.",
        ["calcula bien el descuento", "calcula total y saldo", "compara la ocupación con el objetivo"],
        ["hoja con los cuatro cálculos y la comparación"],
        ["restar 15 en vez de 15 %", "restar el anticipo de una noche", "olvidar el objetivo"],
        "Pregunta: «¿cuánto vale el 15 % de 40.000?». Si no responde 6.000, repasa el cálculo del porcentaje."),
    reinforce="Inventa una tarifa y un descuento porcentual, y calcula la tarifa final para 3 noches.",
    extend="Explica por qué conviene conservar el documento que acredita al cliente de un convenio.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 15 (opciones de tarifa de ejemplo, inventadas). Un cliente quiere 2 noches en una habitación doble. Tarifa flexible: $52.000 por noche, cancelación sin costo hasta 48 horas antes. "
     "Tarifa no reembolsable: $44.000 por noche, se paga todo al reservar y no se devuelve si cancela. El cliente no está seguro de poder viajar. "
     "Lista de verificación del check-in (de ejemplo): 1) documento de identidad revisado; 2) datos completos; 3) tarifa y total informados; 4) forma de pago registrada; 5) horarios de desayuno y de salida informados. "
     "Check-out: revisar la cuenta con el huésped, recibir la tarjeta de acceso a la habitación y preguntar por objetos olvidados.")
build(
    O3, 5, F,
    use="Aprenderé a comparar tarifas con distinta política de cancelación y a verificar que el check-in y el check-out se hicieron completos y con calidad.",
    prior=["Sé calcular totales y diferencias.", "Conozco la política de cancelación.", "Conozco la ficha de reserva."],
    explain=[
        "Dos tarifas pueden tener precios distintos porque ofrecen condiciones distintas. La tarifa flexible permite cancelar sin costo hasta un plazo; la tarifa no reembolsable es más barata, pero si el cliente cancela no recupera lo pagado. Comparar es calcular el costo de cada una en cada escenario (si el cliente viaja y si cancela) y explicarlo con claridad. La decisión es del cliente.",
        "El check-in tiene pasos: revisar el documento, completar los datos, informar tarifa y total, registrar la forma de pago e informar horarios. Una lista de verificación es una lista de puntos que se marcan uno por uno para comprobar que no falta nada. El check-out revisa la cuenta con el huésped, recibe la tarjeta de acceso y pregunta por objetos olvidados.",
        "Verificar la calidad es comprobar que todos los puntos estén hechos y que los datos estén bien registrados. Si falta algo, se corrige y se registra qué faltó. En todo momento se cuidan los datos del cliente y se explica con respeto." + LIM,
    ],
    vocab=[("tarifa flexible", "tarifa que permite cancelar sin costo hasta un plazo"), ("tarifa no reembolsable", "tarifa más barata que no se devuelve si el cliente cancela"), ("escenario", "situación posible, como que el cliente viaje o cancele"), ("lista de verificación", "lista de puntos que se marcan uno por uno"), ("tarjeta de acceso", "tarjeta que abre la puerta de la habitación")],
    worked=[
        ("Comparar costos en un escenario", "Una tarifa de ejemplo cuesta $30.000 por noche y otra, no reembolsable, $25.000. El cliente viaja 2 noches. ¿Cuál cuesta menos?", ["Flexible: 30.000 × 2 = 60.000.", "No reembolsable: 25.000 × 2 = 50.000."], "La no reembolsable, con $10.000 menos"),
        ("Revisar una lista de verificación", "Un check-in de ejemplo tiene cuatro puntos y el recepcionista hizo tres. ¿Se puede dar por completo?", ["Se comparan los puntos hechos con la lista.", "Falta un punto."], "No: falta uno"),
    ],
    mistakes=[("Recomendar la tarifa no reembolsable sin preguntar si el cliente está seguro de viajar.", "Si cancela, pierde todo el pago y el hotel parecerá haber ocultado el riesgo.", "Explica ambos escenarios y deja que decida."),
              ("Marcar la lista de verificación como completa sin haber hecho todos los puntos.", "El registro engaña y los errores quedan sin corregir.", "Marca solo lo que realmente se hizo y anota lo pendiente.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una tarifa no reembolsable?", "Una tarifa más barata que no se devuelve si el cliente cancela", "Una tarifa que permite cancelar sin costo", "Una tarifa solo para niños", "Es más barata a cambio de no devolver el pago."),
        ("=", "{F} Si el cliente viaja, ¿cuánto paga con la tarifa flexible por las 2 noches?", "52000*2", "Se multiplica la tarifa flexible por las noches.", " pesos"),
        ("=", "{F} Si el cliente viaja, ¿cuánto paga con la tarifa no reembolsable por las 2 noches?", "44000*2", "Se multiplica la tarifa no reembolsable por las noches.", " pesos"),
        ("=", "{F} ¿Cuánto ahorra si viaja y elige la no reembolsable?", "52000*2-44000*2", "Se resta el costo no reembolsable al flexible.", " pesos"),
        ("abc", "{F} Si el cliente cancela con 5 días de aviso y eligió la tarifa flexible, ¿cuánto pierde?", "Nada, porque cancela dentro del plazo", "Una noche", "Todo lo pagado", "La flexible permite cancelar sin costo hasta 48 horas antes."),
        ("abc", "{F} Si cancela con 5 días de aviso y eligió la no reembolsable, ¿cuánto pierde?", "Todo lo pagado, $88.000", "Nada", "Solo una noche", "La no reembolsable no devuelve el pago aunque cancele con anticipación."),
        ("abc", "{F} El cliente dice que no está seguro de viajar. ¿Qué tarifa conviene ofrecerle y cómo?", "La flexible, explicando que cuesta más pero permite cancelar, y dejando que decida", "La no reembolsable, porque es más barata", "Ninguna, hasta que esté seguro", "Si hay incertidumbre, la tarifa flexible reduce el riesgo; la decisión es del cliente."),
        ("abc", "{F} Un recepcionista hace el check-in sin informar el total ni la forma de pago. ¿Cuántos puntos de la lista se cumplieron como máximo?", "3 de 5", "4 de 5", "5 de 5", "Se omitieron los puntos 3 y 4, así que como máximo se cumplieron los otros tres."),
        ("=", "{F} La lista tiene 5 puntos y se hicieron 3. ¿Qué porcentaje de la lista se cumplió?", "3*100//5", "Se multiplican los puntos hechos por 100 y se dividen por el total.", " %"),
        ("abc", "{F} Un compañero marca los 5 puntos «para ir más rápido» sin haberlos hecho. ¿Qué observación corresponde?", "Es falsear el registro; debe hacer los puntos y marcar solo lo realizado", "Está bien si el huésped es de confianza", "Está bien si hay muchos huéspedes esperando", "Un registro falso impide detectar y corregir errores."),
        ("abc", "{F} En el check-out, el huésped no entrega la tarjeta de acceso. ¿Qué corresponde?", "Pedirla con amabilidad, registrar que no la devolvió y avisar según el protocolo", "Dejarlo ir sin decir nada", "Retenerlo hasta que la entregue", "Se solicita con respeto y se registra; retener a la persona no corresponde."),
        ("abc", "{F} En el check-out, el huésped pregunta por un cobro que no reconoce. ¿Qué haces?", "Revisar la cuenta con él, mostrar el detalle y consultar si hay un error", "Decirle que pague y reclame después", "Ignorar la pregunta", "Revisar con el huésped es parte del check-out y protege al consumidor."),
        ("abc", "Un huésped, al salir, comenta que olvidó un cargador en la habitación. ¿Qué haces?", "Anotar su nombre y habitación y avisar a pisos para buscar y registrar el objeto", "Decirle que no hay nada que hacer", "Dar su teléfono a un desconocido", "Se registra el reclamo y se coordina la búsqueda sin entregar datos a terceros."),
    ],
    ctx=("abc", "{F} Un cliente que eligió la tarifa no reembolsable cancela con 10 días de aviso porque se enfermó y pide que le devuelvan el dinero. ¿Qué haces?", "Explicar con respeto las condiciones que aceptó y consultar a la jefatura si existe una excepción", "Devolver todo para evitar un reclamo", "Decirle que no hay nada que hablar", "Se explica la condición y se deriva la excepción a quien corresponde, sin dar consejos de salud."),
    sc=[
        ("En Hotelería: ¿qué ventaja tiene la tarifa flexible?", "Permite cancelar sin costo hasta un plazo", "Reduce el riesgo si el cliente no está seguro."),
        ("¿Cómo se comparan dos tarifas?", "Calculando el costo en cada escenario", "Así se ve lo que pasa si viaja y si cancela."),
        ("¿Qué se marca en una lista de verificación?", "Solo lo que realmente se hizo", "Marcar lo no hecho falsea el registro."),
    ],
    op=("Tarifas de ejemplo para 3 noches en una doble: flexible $50.000 por noche, cancelación sin costo hasta 48 horas antes; no reembolsable $42.000 por noche. Un cliente dice que tiene un 50 % de probabilidad de poder viajar. "
        "Calcula el costo de cada tarifa si viaja y lo que pierde con la no reembolsable si cancela, y escribe cómo se lo explicarías con respeto antes de que decida. Luego anota cuántos puntos de la lista de check-in (5 puntos) se cumplirían si olvidas informar los horarios.",
        "Flexible, si viaja: 50.000 × 3 = 150.000. No reembolsable, si viaja: 42.000 × 3 = 126.000. Si cancela con la no reembolsable pierde 126.000; con la flexible, no pierde nada si cancela a tiempo. Explicación: «La no reembolsable es más barata si viaja, pero si cancela no se devuelve; la flexible cuesta más pero permite cancelar; usted decide». Check-in: se cumplirían 4 de 5 puntos.",
        ["calcula los dos costos", "explica ambos escenarios con claridad y respeto", "cuenta los puntos cumplidos"],
        ["hoja con cálculos, explicación y conteo de puntos"],
        ["recomendar una tarifa sin explicar el riesgo", "confundir cuánto pierde en cada caso", "marcar los 5 puntos"],
        "Pregunta: «¿qué pierde si cancela con cada tarifa?». Si no distingue ambas, repasa la política de cancelación."),
    reinforce="Escribe una lista de verificación de 5 puntos para el check-out de un hotel y marca los que se cumplieron en un caso inventado.",
    extend="Explica por qué el cliente debe conocer los dos escenarios antes de elegir su tarifa.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 16 (estado de habitaciones de ejemplo, inventado). Hotel de 20 habitaciones. Códigos: LI = limpia e inspeccionada (lista para vender); SU = sucia (pendiente de limpieza); OC = ocupada; NM = ocupada con el letrero «no molestar»; FS = fuera de servicio por mantención (no se vende). "
     "Estado a las 11:00: OC 7, NM 1, SU 6, LI 4, FS 2. Reglas generales del personal de pisos: usar solo los productos que el hotel entrega, leer su etiqueta, no mezclarlos por iniciativa propia, pedir ayuda para mover cosas pesadas y avisar de inmediato ante un accidente.")
build(
    O4, 1, F,
    use="Aprenderé qué significa supervisar el servicio de habitaciones, los estados de una habitación y las reglas generales de privacidad, seguridad y ergonomía del personal de pisos.",
    prior=["Conozco la reserva y el check-in.", "Sé sumar y calcular porcentajes simples.", "Sé leer una tabla de estados."],
    explain=[
        "El servicio de habitaciones, o pisos, es el área que deja las habitaciones limpias, ordenadas y listas para el huésped. Supervisar es comprobar que ese trabajo se haga según los procedimientos y estándares del hotel y registrar el resultado. Cada habitación tiene un estado (limpia e inspeccionada, sucia, ocupada, fuera de servicio), y el informe diario de estado de habitaciones los reúne para que recepción sepa cuáles puede vender.",
        "Hay reglas generales de seguridad y respeto: el personal usa solo los productos que el hotel entrega, lee sus etiquetas, no los mezcla por iniciativa propia y pide capacitación; si hay un accidente o un malestar, avisa de inmediato a personal capacitado. Se respeta el letrero «no molestar», no se revisan las pertenencias del huésped y los objetos olvidados se registran y se entregan, no se guardan.",
        "También se cuida la ergonomía: pedir ayuda para mover cosas pesadas, alternar tareas y hacer pausas. Esto es aprendizaje en papel: el trabajo real con productos químicos o equipos exige capacitación con un instructor autorizado." + QUI,
    ],
    vocab=[("servicio de habitaciones (pisos)", "área que deja las habitaciones limpias y listas para el huésped"), ("supervisar", "comprobar que el trabajo cumpla los procedimientos y estándares y registrarlo"), ("estado de habitación", "situación de una habitación, como limpia, sucia, ocupada o fuera de servicio"), ("fuera de servicio", "habitación que no se vende por una falla pendiente de mantención"), ("objeto olvidado", "pertenencia que un huésped dejó en la habitación"), ("ergonomía", "cuidado de la postura y del esfuerzo al trabajar")],
    worked=[
        ("Contar habitaciones listas", "En un hotel de ejemplo hay 5 habitaciones LI, 3 SU y 2 OC. ¿Cuántas están listas para vender?", ["Solo las LI están limpias e inspeccionadas.", "Hay 5."], "5 habitaciones"),
        ("Respetar «no molestar»", "Un huésped de ejemplo dejó el letrero «no molestar» a las 10:00. ¿Qué hace el personal de pisos?", ["No entra a la habitación.", "Informa a recepción según el protocolo."], "No entra e informa según el protocolo"),
    ],
    mistakes=[("Entrar a una habitación con el letrero «no molestar» para terminar antes.", "Se invade la privacidad del huésped y se desobedece su petición.", "Respeta el letrero y coordina con recepción el horario."),
              ("Quedarse con un objeto olvidado porque «nadie lo va a reclamar».", "Es un objeto ajeno y su dueño puede reclamarlo.", "Regístralo con fecha y habitación y entrégalo según el protocolo.")],
    T=[
        ("abc", "En Hotelería: ¿qué es supervisar el servicio de habitaciones?", "Comprobar que el trabajo cumpla los estándares y registrarlo", "Hacer solo la limpieza de todas las habitaciones", "Decidir los precios de las habitaciones", "Supervisar es verificar y registrar; no es limpiar todo ni fijar precios."),
        ("abc", "{F} ¿Qué significa el código LI?", "Limpia e inspeccionada, lista para vender", "Libre sin inspección", "Limpieza inmediata", "LI indica que la habitación ya fue limpiada y revisada."),
        ("abc", "{F} ¿Cuántas habitaciones están listas para vender a las 11:00?", "4", "6", "7", "La ficha indica 4 habitaciones LI; las sucias aún no se pueden vender."),
        ("=", "{F} ¿Cuántas habitaciones están sucias o fuera de servicio en conjunto?", "6+2", "Se suman las habitaciones SU y las FS.", " habitaciones"),
        ("abc", "{F} Una habitación aparece NM. ¿Qué corresponde hacer con ella?", "No entrar y coordinar con recepción según el protocolo", "Entrar de todos modos a limpiar", "Tocar la puerta insistentemente hasta que abra", "Se respeta el pedido del huésped y se coordina con recepción."),
        ("=", "{F} ¿Qué porcentaje de las 20 habitaciones está ocupado (OC más NM)?", "(7+1)*100//20", "Se suman las ocupadas, se multiplican por 100 y se dividen por 20.", " %"),
        ("abc", "{F} ¿Por qué las 2 habitaciones FS no se venden?", "Porque tienen una falla pendiente de mantención", "Porque están reservadas", "Porque están sucias", "FS significa fuera de servicio por mantención."),
        ("abc", "{F} Una persona de pisos encuentra una billetera en la habitación de un huésped que ya salió. ¿Qué hace?", "La registra con fecha y habitación y la entrega a recepción sin abrirla", "Se la guarda para cuidarla", "La deja sobre la mesa", "Los objetos olvidados se registran y se entregan para que el dueño pueda reclamarlos."),
        ("abc", "{F} Dos productos que el hotel entrega tienen etiquetas distintas. Una persona de pisos quiere mezclarlos «para que limpien más». ¿Qué regla corresponde?", "No mezclarlos por iniciativa propia y consultar a la jefatura", "Mezclarlos si el olor es agradable", "Mezclarlos si no hay nadie cerca", "La regla general es no mezclar por iniciativa propia; la capacitación la da un instructor autorizado."),
        ("abc", "{F} Una persona de pisos se lastima la espalda moviendo algo pesado. ¿Qué corresponde?", "Avisar de inmediato a su jefatura y a personal capacitado", "Seguir trabajando para no atrasar la limpieza", "Ocultarlo hasta el fin del turno", "Ante un accidente se avisa de inmediato; ocultarlo puede agravarlo."),
        ("abc", "{F} Una persona de pisos nota documentos de un huésped sobre la mesa. ¿Qué hace?", "No los revisa ni los comenta y mantiene la privacidad", "Los lee para saber quién es", "Los fotografía por si acaso", "Las pertenencias del huésped son privadas y no se revisan."),
        ("abc", "{F} El informe diario anota una habitación como LI, pero la persona supervisora comprueba que está sucia. ¿Qué corresponde?", "Corregir el informe y avisar a recepción antes de venderla", "Dejarla como LI para que coincida", "Venderla igual y limpiarla después", "El informe debe reflejar el estado real para no vender una habitación sin limpiar."),
        ("abc", "{F} Una persona de pisos debe mover un colchón pesado sola. ¿Qué regla de ergonomía corresponde?", "Pedir ayuda para mover cosas pesadas", "Moverlo rápido para terminar pronto", "Moverlo tirando con la espalda", "La ficha manda pedir ayuda ante cargas pesadas."),
    ],
    ctx=("abc", "{F} A las 11:00, recepción pregunta cuántas habitaciones puede vender ahora y cuántas pronto. ¿Qué información entrega la supervisión?", "4 listas ahora (LI), 6 sucias que pueden estar listas tras limpiarse y 2 fuera de servicio que no se venden", "Las 20 habitaciones, porque todas son del hotel", "Solo las 7 ocupadas", "Se informa el estado real de cada grupo, con lo vendible hoy y lo pendiente."),
    sc=[
        ("En Hotelería: ¿qué significa el estado fuera de servicio?", "No se vende por una falla pendiente", "La habitación no puede usarse hasta que se repare."),
        ("¿Qué haces con un objeto olvidado?", "Lo registro y lo entrego", "El dueño debe poder reclamarlo después."),
        ("¿Qué haces ante un accidente en el trabajo?", "Aviso de inmediato a personal capacitado", "No se oculta ni se resuelve solo."),
    ],
    op=("Hotel de ejemplo con 12 habitaciones. A las 10:00, el estado es: LI 3, SU 4, OC 3, FS 1, NM 1. Una persona de pisos encontró un abrigo en una habitación sucia y otra dice que no puede entrar a la habitación NM. "
        "Escribe: cuántas habitaciones se pueden vender ahora, qué haces con el abrigo, qué haces con la habitación NM, y una regla de seguridad o de ergonomía que le recordarías al equipo.",
        "Se pueden vender 3 habitaciones (LI). El abrigo se registra con fecha y habitación y se entrega a recepción. La habitación NM no se entra y se coordina con recepción. Regla: pedir ayuda para mover cosas pesadas, o no mezclar productos por iniciativa propia.",
        ["identifica las habitaciones vendibles", "aplica las reglas de objetos olvidados y privacidad", "nombra una regla de seguridad o ergonomía"],
        ["hoja con las tres respuestas y la regla"],
        ["contar las sucias como vendibles", "guardar el abrigo", "entrar a la habitación NM"],
        "Pregunta: «¿por qué las habitaciones SU no se cuentan como listas?». Si no responde que no están limpias e inspeccionadas, repasa los códigos."),
    reinforce="Haz una tabla con los cinco estados de habitación de la ficha y escribe qué significa cada uno.",
    extend="Explica por qué respetar el letrero «no molestar» es parte del buen trato al huésped.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 17 (documentos de pisos, de ejemplo, inventados). Hoja de asignación de un turno: 24 habitaciones para limpiar. Persona A: 9 habitaciones. Persona B: 8. Persona C: 7. Carga máxima por persona en el turno (de ejemplo): 8 habitaciones. "
     "Lencería (sábanas y toallas): el hotel mantiene 3 juegos por cama (uno en la cama, uno en lavandería y uno en bodega). Camas del hotel: 20. Inventario actual: 52 juegos. "
     "Lista de verificación de inspección (de ejemplo): cama hecha, baño en orden y sin fallas visibles, artículos de cortesía repuestos (amenities: jabón, por ejemplo), luces y televisor funcionan, sin objetos ajenos.")
build(
    O4, 2, F,
    use="Aprenderé los documentos del servicio de habitaciones: informe diario, hoja de asignación, lista de verificación, inventario de lencería, registro de objetos olvidados y solicitud de mantención.",
    prior=["Conozco los estados de habitación.", "Sé multiplicar y restar.", "Sé leer una hoja de asignación."],
    explain=[
        "En pisos se trabaja con documentos. La hoja de asignación reparte las habitaciones entre las personas del turno, sin superar la carga máxima. La lista de verificación (checklist) de inspección sirve para comprobar punto por punto que la habitación cumple el estándar. El informe diario de estado de habitaciones reúne el estado de cada una, con hora y firma de quien lo verificó.",
        "El inventario de lencería registra las sábanas y toallas del hotel. El par de lencería es la cantidad de juegos que se mantiene por cama para que siempre haya reposición: aquí, 3 juegos por cama, así que el total necesario es camas × 3. Los artículos de cortesía, o amenities, también se reponen y se anotan.",
        "El registro de objetos olvidados anota fecha, habitación y descripción; la solicitud de mantención avisa de una falla, como una gotera, para que la repare el personal autorizado. Quien supervisa no repara ni modifica instalaciones por cuenta propia." + QUI,
    ],
    vocab=[("hoja de asignación", "documento que reparte las habitaciones entre las personas del turno"), ("lista de verificación (checklist)", "lista de puntos que se comprueban uno por uno"), ("par de lencería", "juegos de sábanas y toallas que se mantienen por cada cama"), ("amenities", "artículos de cortesía, como jabón, que se reponen en la habitación"), ("solicitud de mantención", "aviso escrito de una falla para que la repare personal autorizado"), ("registro de objetos olvidados", "anotación de fecha, habitación y descripción de lo que un huésped dejó")],
    worked=[
        ("Calcular lencería necesaria", "Un hotel de ejemplo tiene 10 camas y mantiene 4 juegos por cama. ¿Cuántos juegos necesita en total?", ["Total = camas × juegos por cama.", "10 × 4 = 40."], "40 juegos"),
        ("Revisar una asignación", "En un turno de ejemplo la carga máxima es 6 habitaciones y a una persona se le asignaron 7. ¿Cumple?", ["Se compara lo asignado con el máximo.", "7 es mayor que 6."], "No cumple: excede en 1"),
    ],
    mistakes=[("Marcar «cumple» en todos los puntos de la lista sin mirar la habitación para terminar antes.", "Es un registro falso y los errores llegan al huésped.", "Marca solo lo que verificaste y anota lo que falta."),
              ("Intentar arreglar por cuenta propia una gotera que descubres al supervisar.", "La reparación la hace personal autorizado; hacerla sin capacitación puede ser peligroso.", "Registra una solicitud de mantención y avisa.")],
    T=[
        ("abc", "En Hotelería: ¿para qué sirve la lista de verificación de inspección?", "Para comprobar punto por punto que la habitación cumple el estándar", "Para fijar el precio de la habitación", "Para decidir quién se aloja", "La lista ordena la revisión y deja evidencia de qué se comprobó."),
        ("abc", "{F} ¿A quién se le asignaron más habitaciones que el máximo?", "A la persona A, con 9", "A la persona B, con 8", "A la persona C, con 7", "El máximo es 8 y solo A lo supera."),
        ("=", "{F} ¿Cuántas habitaciones suman las asignaciones de A, B y C?", "9+8+7", "Se suman las habitaciones de las tres personas.", " habitaciones"),
        ("=", "{F} ¿Cuántos juegos de lencería necesita el hotel en total?", "20*3", "Se multiplican las camas por los juegos de cada cama.", " juegos"),
        ("=", "{F} ¿Cuántos juegos faltan respecto del inventario actual?", "20*3-52", "Al total necesario se le resta el inventario actual.", " juegos"),
        ("abc", "{F} ¿Qué corresponde hacer con la sobrecarga de la persona A?", "Pasar una habitación a quien tenga menos de 8, como la persona C", "Dejar que A trabaje más rápido", "Ignorar el máximo para terminar antes", "Redistribuir cumple el máximo; C tiene 7 y puede recibir una."),
        ("=", "{F} Cada juego faltante cuesta $9.000 (precio de ejemplo). ¿Cuánto cuesta reponer los que faltan?", "(20*3-52)*9000", "Se multiplican los juegos faltantes por el precio de cada uno.", " pesos"),
        ("abc", "¿Qué documento se usa cuando se descubre una gotera en un baño?", "La solicitud de mantención", "El registro de objetos olvidados", "La hoja de asignación", "La solicitud de mantención avisa la falla para que la repare personal autorizado."),
        ("abc", "¿Qué documento registra que se encontró un abrigo dejado por un huésped?", "El registro de objetos olvidados", "La solicitud de mantención", "El inventario de lencería", "Ese registro anota fecha, habitación y descripción del objeto."),
        ("abc", "{F} En una inspección, la lista dice «luces y televisor funcionan» y el televisor no enciende. ¿Qué se marca?", "No cumple, y se registra la falla", "Cumple, porque las luces funcionan", "Cumple, para no atrasar al equipo", "Un punto con falla se marca no cumple y se registra."),
        ("abc", "¿Qué debe llevar cada línea del informe diario de estado de habitaciones?", "Número de habitación, estado, observaciones, hora y firma de quien verificó", "Solo el nombre del huésped", "Solo el precio de la tarifa", "El informe reúne el estado verificable de cada habitación."),
        ("=", "{F} Si se pasa una habitación de la persona A a la persona C, ¿cuántas habitaciones tendrá C?", "7+1", "A las habitaciones que ya tiene C se le suma la que recibe.", " habitaciones"),
        ("=", "{F} Con 24 habitaciones y un máximo de 8 por persona, ¿cuál es el número mínimo de personas necesarias?", "24//8", "Se divide el total de habitaciones por el máximo por persona.", " personas"),
    ],
    ctx=("abc", "{F} Al supervisar, encuentras que faltan los artículos de cortesía en 3 habitaciones. ¿Qué haces?", "Anotar cuáles faltan, hacerlos reponer y registrar la reposición", "No decir nada, porque son artículos pequeños", "Quitarlos de otras habitaciones sin anotarlo", "Se registra y se repone para mantener el estándar con evidencia."),
    sc=[
        ("En Hotelería: ¿qué es el par de lencería?", "Los juegos que se mantienen por cada cama", "Garantiza que siempre haya lencería de reposición."),
        ("¿Qué documento reparte las habitaciones del turno?", "La hoja de asignación", "Muestra quién limpia cuáles habitaciones del turno."),
        ("¿Quién repara una falla que descubres?", "Personal autorizado de mantención", "Se solicita por escrito y no se repara por cuenta propia."),
    ],
    op=("Datos de ejemplo. Hotel con 16 camas y 3 juegos de lencería por cama; inventario actual: 44 juegos. Hoja de asignación: 18 habitaciones; carga máxima 6 por persona; personas: X con 7, Y con 6 y Z con 5. "
        "Calcula: los juegos necesarios y los que faltan; quién excede la carga máxima y qué harías; y escribe qué documento usarías para avisar una ampolleta quemada en un baño.",
        "Necesarios: 16 × 3 = 48; faltan 48 − 44 = 4. X excede la carga máxima con 7: pasaría una habitación a Z, que tiene 5. Documento: solicitud de mantención.",
        ["calcula juegos y faltantes", "detecta la sobrecarga y propone redistribuir", "nombra el documento correcto"],
        ["hoja con los cálculos, la decisión y el documento"],
        ["multiplicar por 4 en lugar de 3", "no detectar a X", "usar el registro de objetos olvidados para una falla"],
        "Pregunta: «¿por qué Z puede recibir una habitación?». Si no responde que tiene menos del máximo, repasa la carga máxima."),
    reinforce="Escribe una lista de verificación de 5 puntos para inspeccionar una habitación, con casillas de cumple y no cumple.",
    extend="Explica por qué firmar el informe diario con la hora ayuda a encontrar a quien verificó cada habitación.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 18 (informe diario de ejemplo, a las 10:00, inventado). Según recepción: 101 vacante y lista para vender; 102 lista; 103 ocupada; 104 fuera de servicio; 105 ocupada; 106 vacante y lista. "
     "Según pisos: 101 sucia (el huésped salió a las 9:30, se limpiará a las 11:00); 102 limpia e inspeccionada; 103 ocupada con el letrero «no molestar»; 104 fuera de servicio por una gotera en el baño (mantención fue avisada ayer); 105 ocupada; 106 sucia, y en ella se encontró una billetera con documentos que aún no se ha registrado. "
     "Dos huéspedes llegan a las 11:00.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un informe diario con información distinta de recepción y de pisos, detectar inconsistencias y decidir con un registro verificado.",
    prior=["Conozco los estados de habitación.", "Conozco los documentos de pisos.", "Sé comparar dos listas."],
    explain=[
        "Un informe diario es útil solo si es verdadero. Cuando recepción y pisos dicen cosas distintas de una habitación, hay una inconsistencia: se verifica el estado real mirando la habitación y se corrige el registro. Una habitación no se vende hasta que pisos la deje limpia e inspeccionada.",
        "Las novedades del informe, como una falla o un objeto olvidado, tienen un trámite: la falla va a mantención con una solicitud escrita y el objeto se registra en el registro de objetos olvidados y se entrega a recepción. Cada dato debe tener responsable, hora y firma, para saber a quién consultar.",
        "Cuando no alcanza el tiempo, se prioriza: primero las habitaciones que se necesitan antes y se avisa a recepción cuándo estarán listas, ofreciendo alternativas al huésped, como guardar su equipaje. Nunca se cambia el informe para que «cuadre» sin verificar." + QUI,
    ],
    vocab=[("inconsistencia", "dato que no coincide entre dos fuentes del mismo informe"), ("verificar", "comprobar un dato mirando la situación real"), ("novedad", "hecho que debe quedar anotado, como una falla o un objeto olvidado"), ("prioridad", "lo que se atiende primero porque se necesita antes"), ("responsable", "persona que responde por un dato o una tarea")],
    worked=[
        ("Detectar una inconsistencia", "Recepción dice que una habitación está lista y pisos la tiene sucia. ¿Hay inconsistencia?", ["Los dos datos son distintos para la misma habitación.", "Debe verificarse."], "Sí, y se verifica mirando la habitación"),
        ("Priorizar", "Llegan dos huéspedes a las 11:00 y hay dos habitaciones sucias. Una de ellas ya tiene un huésped esperando. ¿Cuál se prioriza?", ["Se necesita primero la que tiene un huésped esperando.", "La otra se limpia después."], "La que tiene un huésped esperando"),
    ],
    mistakes=[("Cambiar el informe de pisos para que coincida con recepción sin ir a ver la habitación.", "Se registra un dato falso y se puede vender una habitación sucia.", "Verifica el estado real y corrige el registro con tu firma."),
              ("Dejar la billetera encontrada en la habitación hasta el fin del turno.", "Puede perderse y el huésped no podría recuperarla.", "Regístrala y entrégala a recepción de inmediato, sin abrirla.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una inconsistencia en un informe diario?", "Un dato que no coincide entre dos fuentes del mismo informe", "Un dato que está escrito con letra pequeña", "Un dato que todos conocen", "La inconsistencia es la diferencia entre dos fuentes sobre lo mismo."),
        ("abc", "{F} ¿En qué habitaciones hay desacuerdo entre recepción y pisos?", "En la 101 y la 106", "En la 102 y la 103", "En la 104 y la 105", "Recepción las da por listas y pisos las tiene sucias."),
        ("abc", "{F} ¿Cuál es el estado real de la 101?", "Sucia, con limpieza prevista a las 11:00", "Lista para vender", "Fuera de servicio", "Pisos informa que el huésped salió a las 9:30 y se limpiará a las 11:00."),
        ("=", "{F} El informe lista 6 habitaciones. Según pisos, ¿cuántas están listas para vender ahora?", "1", "Solo la 102 está limpia e inspeccionada.", " habitación"),
        ("abc", "{F} ¿Qué corresponde con la billetera encontrada en la 106?", "Registrarla en el registro de objetos olvidados y entregarla a recepción sin abrirla", "Dejarla en la 106 hasta el fin del turno", "Guardarla en un casillero personal", "Un objeto olvidado se registra y se entrega para que el dueño lo recupere."),
        ("abc", "{F} ¿Por qué no se puede vender la 104?", "Está fuera de servicio por una gotera en el baño", "Está ocupada", "Está sucia", "Pisos la tiene fuera de servicio hasta que mantención la repare."),
        ("abc", "{F} ¿Puede entrar la persona de pisos a la 103?", "No: tiene el letrero «no molestar» y se coordina con recepción", "Sí, para limpiar rápido", "Sí, si toca primero", "Se respeta el letrero y se coordina el horario."),
        ("=", "{F} Si limpiar una habitación sucia toma 30 minutos (tiempo de ejemplo) y una sola persona debe limpiar la 101 y la 106, ¿cuántos minutos necesita?", "30*2", "Se multiplican los minutos de cada limpieza por las dos habitaciones.", " minutos"),
        ("abc", "{F} Llegan dos huéspedes a las 11:00 y solo hay una habitación lista. ¿Qué hace recepción?", "Asignar la 102 a uno, informar al otro la hora estimada de su habitación y ofrecerle guardar su equipaje", "Asignar la 101 sucia para no esperar", "Decirles que vuelvan mañana", "Se usa la habitación lista y se informa y atiende con amabilidad al otro huésped."),
        ("abc", "{F} Un compañero propone cambiar el informe de pisos para que diga que la 101 está lista, «así cuadra con recepción». ¿Qué corresponde?", "No hacerlo: se verifica el estado real y se corrige el informe de recepción", "Hacerlo, porque recepción nunca se equivoca", "Hacerlo si los huéspedes ya llegaron", "El informe debe reflejar el estado real; falsearlo puede llevar a vender una habitación sucia."),
        ("abc", "{F} ¿Qué mejora tendría el informe para que se sepa quién verificó cada dato?", "Anotar la hora y la firma de quien verificó cada habitación", "Borrar los datos viejos", "Agregar el nombre de los huéspedes", "Con hora y firma se sabe a quién consultar."),
        ("abc", "{F} ¿Qué habitación del informe tiene una falla que ya debe estar en una solicitud de mantención?", "La 104, por la gotera del baño", "La 101, por estar sucia", "La 102, por estar lista", "Una falla se registra en una solicitud de mantención; estar sucia o lista no es una falla."),
        ("=", "{F} De las 6 habitaciones del informe, según pisos, ¿cuántas no están ocupadas?", "6-2", "Solo la 103 y la 105 están ocupadas, así que se restan del total.", " habitaciones"),
    ],
    ctx=("abc", "{F} Eres supervisor o supervisora. A las 10:20 verificas la 101 y confirmas que está sucia. ¿Qué haces?", "Corregir el informe, avisar a recepción que no está lista y comunicar la hora estimada de limpieza", "No hacer nada, porque recepción lo corregirá", "Pedir a recepción que venda la 101 igual", "Avisar y corregir con evidencia evita que se venda una habitación sucia."),
    sc=[
        ("En Hotelería: ¿qué haces cuando recepción y pisos informan estados distintos?", "Verifico el estado real y corrijo el registro", "El informe debe reflejar la situación verdadera."),
        ("¿A quién se entrega un objeto olvidado?", "A recepción, con registro", "Allí el dueño puede ir a reclamarlo."),
        ("¿Se vende una habitación sucia si hay apuro?", "No", "Una habitación se vende solo limpia e inspeccionada."),
    ],
    op=("Informe de ejemplo a las 9:00. Recepción dice: 201 lista, 202 ocupada, 203 lista. Pisos dice: 201 limpia e inspeccionada, 202 ocupada con «no molestar», 203 sucia (se encontró un anillo sobre el velador, sin registrar). Una persona llega a las 9:30 y pide una habitación. "
        "Escribe: qué inconsistencia hay y cómo la resolverías, qué harías con el anillo, qué habitación asignarías y qué harías con la 202.",
        "Inconsistencia: la 203 figura lista en recepción y sucia en pisos; se verifica mirando la habitación y se corrige el informe. El anillo se registra en el registro de objetos olvidados y se entrega a recepción. Asignaría la 201, que está limpia e inspeccionada. La 202 no se entra y se coordina con recepción.",
        ["detecta la inconsistencia y la verifica", "aplica el trámite del objeto olvidado", "asigna la habitación correcta y respeta el letrero"],
        ["hoja con las cuatro decisiones"],
        ["asignar la 203", "quedarse con el anillo", "entrar a la 202"],
        "Pregunta: «¿por qué no asignas la 203?». Si no responde que está sucia, repasa la regla de vender solo habitaciones listas."),
    reinforce="Inventa un informe con una inconsistencia entre dos fuentes y escribe cómo la resolverías.",
    extend="Explica por qué un informe con datos falsos puede perjudicar a los huéspedes y al hotel.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 19 (carga de trabajo de ejemplo, inventada). Hotel de 30 habitaciones. Hoy salen 20 huéspedes (limpieza completa, 30 minutos por habitación en promedio de ejemplo) y 10 huéspedes continúan (repaso diario, 15 minutos por habitación). "
     "Inspección de cada habitación de salida: 5 minutos. Tres personas de pisos trabajan 4 horas, de 11:00 a 15:00, y a las 15:00 comienza el check-in. Reposición de toallas: 2 por persona alojada (26 personas hoy). "
     "Informe de fin de turno: habitaciones terminadas, pendientes, solicitudes de mantención, objetos olvidados y faltantes de lencería.")
build(
    O4, 4, F,
    use="Aprenderé a calcular la carga de trabajo del servicio de habitaciones, comprobar si el equipo alcanza para el plazo y decidir sin bajar el estándar.",
    prior=["Conozco los documentos de pisos.", "Sé pasar horas a minutos.", "Sé multiplicar y comparar."],
    explain=[
        "La carga de trabajo es el tiempo total que requieren las tareas asignadas. Se calcula multiplicando la cantidad de habitaciones por el tiempo de cada tipo y sumando. La capacidad del equipo es personas × horas × 60 minutos. Si la carga es mayor que la capacidad, no alcanza para el plazo.",
        "Cuando no alcanza, quien supervisa decide sin bajar el estándar: pide apoyo adicional, prioriza las habitaciones que se necesitan antes y avisa a recepción de la hora estimada. No se saltan puntos de la lista de verificación para ganar tiempo, porque la calidad es parte del servicio.",
        "También se calcula la reposición, como las toallas, con cantidad por persona × personas alojadas. El informe de fin de turno deja constancia de lo terminado y lo pendiente para el siguiente turno. Los tiempos de este cuaderno son de ejemplo y no son estándares reales." + QUI,
    ],
    vocab=[("carga de trabajo", "tiempo total que requieren las tareas asignadas"), ("capacidad del equipo", "tiempo que el equipo puede trabajar: personas × horas × 60 minutos"), ("repaso diario", "arreglo de una habitación cuyo huésped continúa"), ("apoyo adicional", "persona extra que ayuda cuando el equipo no alcanza"), ("informe de fin de turno", "registro de lo terminado y lo pendiente al terminar el turno")],
    worked=[
        ("Calcular una carga", "En un hotel de ejemplo hay 6 limpiezas de 20 minutos y 4 repasos de 10 minutos. ¿Cuántos minutos requiere el trabajo?", ["6 × 20 = 120 y 4 × 10 = 40.", "120 + 40 = 160."], "160 minutos"),
        ("Comparar con la capacidad", "Un equipo de ejemplo de 2 personas trabaja 2 horas. ¿Cuántos minutos de capacidad tiene?", ["Capacidad = personas × horas × 60.", "2 × 2 × 60 = 240."], "240 minutos"),
    ],
    mistakes=[("Saltarse puntos de la lista de verificación para llegar a tiempo al check-in.", "Se baja el estándar y el huésped recibe una habitación incompleta.", "Pide apoyo, prioriza y avisa a recepción la hora estimada."),
              ("Calcular la capacidad con las horas pero sin pasarlas a minutos.", "Se compara 12 con 750, que son unidades distintas.", "Pasa las horas a minutos multiplicando por 60.")],
    T=[
        ("abc", "En Hotelería: ¿qué es la carga de trabajo?", "El tiempo total que requieren las tareas asignadas", "La cantidad de habitaciones que tiene el hotel", "El sueldo de las personas de pisos", "La carga mide el tiempo requerido, no la cantidad de habitaciones ni el sueldo."),
        ("=", "{F} ¿Cuántos minutos requieren las limpiezas completas de las 20 habitaciones de salida?", "20*30", "Se multiplican las habitaciones por los minutos de cada limpieza.", " minutos"),
        ("=", "{F} ¿Cuántos minutos requieren los repasos diarios de las 10 habitaciones que continúan?", "10*15", "Se multiplican las habitaciones por los minutos de cada repaso.", " minutos"),
        ("=", "{F} ¿Cuántos minutos requiere en total el trabajo de limpieza y repaso?", "20*30+10*15", "Se suman los minutos de limpiezas y de repasos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos de capacidad tiene el equipo de 3 personas entre 11:00 y 15:00?", "3*4*60", "Se multiplican personas por horas por 60 minutos.", " minutos"),
        ("=", "{F} Contando solo la limpieza y el repaso (sin la inspección), ¿cuántos minutos de trabajo no alcanzan a hacerse con el equipo actual?", "20*30+10*15-3*4*60", "A la carga total se le resta la capacidad del equipo.", " minutos"),
        ("abc", "{F} ¿Qué decisión mantiene el estándar de calidad?", "Pedir apoyo adicional, priorizar y avisar a recepción la hora estimada", "Saltarse puntos de la lista de verificación", "Dejar sin limpiar las habitaciones de las llegadas", "El estándar no se baja; se busca apoyo y se informa."),
        ("=", "{F} ¿Cuántos minutos de inspección requieren las 20 habitaciones de salida?", "20*5", "Se multiplican las habitaciones por los minutos de inspección.", " minutos"),
        ("abc", "{F} ¿Qué habitaciones conviene limpiar primero?", "Las de llegadas más tempranas del día", "Las que están más lejos", "Las que se pueden hacer más rápido sin importar la llegada", "La prioridad es lo que se necesita antes; las llegadas esperan su habitación."),
        ("abc", "{F} Un compañero propone saltarse la revisión de luces y televisor en cada habitación «porque nunca fallan». ¿Qué respondes?", "Que la lista se cumple completa, porque una falla no revisada llega al huésped", "Que tiene razón, para ganar tiempo", "Que se revise solo la mitad", "Un estándar no se omite por costumbre; el control evita reclamos."),
        ("=", "{F} Hoy hay 26 personas alojadas. ¿Cuántas toallas hay que reponer?", "26*2", "Se multiplican las personas alojadas por las toallas de cada una.", " toallas"),
        ("=", "{F} Si se suma una cuarta persona de 11:00 a 15:00, ¿cuántos minutos de capacidad sobran después del trabajo de limpieza y repaso (sin contar la inspección)?", "4*4*60-(20*30+10*15)", "A la nueva capacidad se le resta la carga de limpieza y repaso.", " minutos"),
        ("abc", "{F} ¿Qué debe incluir el informe de fin de turno?", "Habitaciones terminadas y pendientes, mantenciones solicitadas, objetos olvidados y faltantes de lencería", "Solo los nombres de los huéspedes", "Solo el sueldo del equipo", "El informe deja constancia de todo lo que el turno siguiente necesita saber."),
    ],
    ctx=("abc", "{F} A las 14:00 aún quedan 5 habitaciones de salida por terminar y llega un huésped a las 14:30. ¿Qué haces?", "Priorizar su habitación, avisar a recepción la hora estimada y ofrecerle guardar su equipaje", "Entregarle una habitación sucia para cumplir", "Decirle que espere sin informar nada", "Se prioriza, se informa y se atiende con amabilidad sin bajar el estándar."),
    sc=[
        ("En Hotelería: ¿cómo se calcula la capacidad del equipo?", "Personas por horas por 60 minutos", "Así se obtienen los minutos disponibles."),
        ("¿Qué haces si la carga supera la capacidad?", "Pido apoyo, priorizo y aviso a recepción", "Se mantiene el estándar y se informa."),
        ("¿Se puede saltar un punto de la lista de verificación?", "No", "El estándar se cumple completo siempre."),
    ],
    op=("Datos de ejemplo. Hotel con 24 habitaciones: hoy salen 14 (25 minutos cada una) y 10 continúan (10 minutos cada una). Dos personas de pisos trabajan de 10:00 a 14:00; el check-in comienza a las 14:00. "
        "Calcula: la carga total en minutos, la capacidad del equipo, si alcanza, y escribe qué decidirías sin bajar el estándar.",
        "Carga: 14 × 25 = 350 y 10 × 10 = 100; total 450 minutos. Capacidad: 2 × 4 × 60 = 480 minutos. Alcanza, con 30 minutos de margen. Decisión: priorizar las habitaciones de las llegadas tempranas, usar el margen para el control de calidad y avisar a recepción las horas estimadas.",
        ["calcula la carga con ambas tareas", "calcula la capacidad en minutos", "decide sin bajar el estándar"],
        ["hoja con cálculos, comparación y decisión"],
        ["olvidar los repasos", "no pasar horas a minutos", "proponer saltarse puntos del control"],
        "Pregunta: «¿qué haces si el margen se acaba?». Debe decir que pide apoyo y avisa a recepción."),
    reinforce="Inventa un hotel con cuántas habitaciones salen y continúan, y calcula la carga de trabajo.",
    extend="Explica por qué un margen de tiempo ayuda a mantener la calidad en horas de mucha llegada.",
)
