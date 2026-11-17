"""Servicios de Turismo TP 3.º y 4.º medio: OAE-01 (tomar reservas) y OAE-02 (atender a los turistas). Todo en papel; fichas y precios de ejemplo."""
from __future__ import annotations

from tp_setu_common import build

O1 = "TP-SETU-3y4-OAE-01"
O2 = "TP-SETU-3y4-OAE-02"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (de ejemplo, inventada). La agencia «Viajes Costa Azul» recibe un correo de la señora Ana Rojas, que quiere reservar la «Cabaña Lomas del Sur» para 4 personas, con entrada el día 12 y salida el día 15 del mismo mes. "
     "La ficha de reserva de la agencia pide: nombre, fechas, cantidad de personas, medio de contacto y forma de pago. En el correo, la señora Rojas escribió además su número de cédula completo. "
     "Tarifa de ejemplo: $40.000 por noche por cabaña. Las reservas se anotan en una planilla digital protegida con clave.")
build(
    O1, 1, F,
    use="Aprenderé qué es una reserva, qué datos de un cliente se piden y se protegen, y qué riesgos hay al tomarla: errores de fecha, doble reserva y mal uso de datos personales.",
    prior=["Sé sumar, restar y multiplicar con números enteros.", "Sé leer fechas y calendarios.", "Sé que los datos de las personas son privados."],
    explain=[
        "Una reserva es el compromiso de que un servicio turístico (alojamiento, transporte, excursión) estará disponible para un cliente en fechas acordadas. El prestador es quien entrega el servicio; la agencia o el ejecutivo de reservas lo gestiona. Al tomar una reserva se confirma por escrito qué se contrata, el precio y la política de cancelación, que son las condiciones para anular o cambiar y para saber cuánto se devuelve. Un buen estándar de calidad es responder rápido, ingresar los datos sin errores y confirmar al cliente.",
        "Los datos del cliente son datos personales: permiten identificarlo o ubicarlo. Se piden solo los necesarios para la reserva, se guardan en sistemas con clave, se usan solo para ese fin y no se entregan a terceros sin autorización, según la norma vigente de protección de datos. Los riesgos más comunes al reservar son digitar mal una fecha, no revisar la disponibilidad y confirmar dos veces el mismo servicio, lo que se llama doble reserva.",
        "Quien atiende reservas trabaja muchas horas frente a una pantalla: conviene ajustar la altura de la pantalla y la silla y hacer pausas breves para estirar el cuerpo. Este cuaderno es aprendizaje en papel y no te habilita para firmar contratos ni manejar sistemas reales de una empresa.",
    ],
    vocab=[("reserva", "compromiso de que un servicio estará disponible en fechas acordadas"), ("prestador", "persona o empresa que entrega el servicio"), ("dato personal", "dato que identifica o permite ubicar a una persona"), ("política de cancelación", "condiciones para anular o cambiar y devolver dinero"), ("doble reserva", "confirmar dos veces el mismo servicio para las mismas fechas"), ("disponibilidad", "que el servicio esté libre en las fechas pedidas")],
    worked=[
        ("Contar las noches", "Un cliente de ejemplo entra el día 7 y sale el día 11 del mismo mes. ¿Cuántas noches se aloja?", ["Las noches son los días entre la entrada y la salida.", "Se resta: 11 − 7 = 4 noches."], "4 noches"),
        ("Decidir qué dato pedir", "Una agencia de ejemplo reserva una visita guiada a un museo. ¿Debe pedir la dirección de la casa del cliente?", ["Se piden solo los datos necesarios para entregar el servicio.", "Para una visita guiada basta el nombre, la cantidad de personas, la fecha y un medio de contacto."], "No: no es un dato necesario para esta reserva"),
    ],
    mistakes=[("Pedir todos los datos que se te ocurran «por si acaso».", "Pedir datos que no se necesitan aumenta el riesgo si se pierden o se filtran.", "Pide solo los datos que la ficha de reserva exige."),
              ("Confirmar una fecha sin revisar si el alojamiento está libre.", "Se puede generar una doble reserva y dejar a un cliente sin servicio.", "Revisa la disponibilidad antes de confirmar por escrito.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una reserva?", "El compromiso de que un servicio estará disponible para un cliente en fechas acordadas", "El pago final que se hace al terminar el viaje", "La lista de atractivos que ofrece una ciudad", "La reserva asegura un servicio para fechas acordadas; el pago final y la lista de atractivos son otras cosas."),
        ("abc", "¿Cuál de estos es un dato personal de un cliente?", "Su nombre junto con su teléfono", "La tarifa por noche de una cabaña", "El nombre de la agencia que lo atiende", "Un dato personal identifica o permite ubicar a una persona; la tarifa y la agencia no lo hacen."),
        ("abc", "En una reserva, ¿qué es la política de cancelación?", "Las condiciones que dicen si se puede anular y cuánto se devuelve", "La lista de servicios que incluye el desayuno", "La forma de llegar al alojamiento", "Esa política fija las reglas para anular o cambiar; no describe servicios ni rutas."),
        ("abc", "{F} ¿Qué dato recibido en el correo no pide la ficha de reserva y no es necesario para tomarla?", "El número de cédula completo", "La cantidad de personas", "Las fechas de entrada y salida", "La ficha pide fechas y personas; la cédula completa sobra y aumenta el riesgo si se filtra."),
        ("=", "{F} ¿Cuántas noches dura la estadía de la señora Rojas?", "15-12", "Las noches son la diferencia entre el día de salida y el de entrada.", " noches"),
        ("=", "{F} Con la tarifa de ejemplo, ¿cuánto cuesta en pesos la estadía completa de la cabaña?", "(15-12)*40000", "Se multiplica la tarifa por las noches de la estadía.", ""),
        ("abc", "{F} ¿Qué debe comprobar la agencia antes de confirmar a la señora Rojas?", "Que la cabaña no esté ya reservada esos días", "Que la señora Rojas haya viajado antes a la zona", "Que la tarifa sea la más barata del mercado", "Confirmar sin revisar disponibilidad puede causar doble reserva; lo demás no es requisito de la reserva."),
        ("ab", "La planilla de reservas queda abierta en un computador que usan varias personas de la agencia. ¿Qué corresponde?", "Cerrar la sesión o bloquear la pantalla al alejarse", "Dejarla abierta para que cualquiera consulte más rápido", "Los datos personales solo deben verlos quienes los necesitan para su trabajo."),
        ("abc", "{F} La señora Rojas pide cambiar la salida al día 16 después de recibir la confirmación. ¿Qué haces primero?", "Revisar la disponibilidad de ese día y la política de cambios, y luego informarle", "Cambiar la fecha en la planilla sin avisarle", "Decirle que ya no se puede cambiar nada, sin revisar", "Un cambio depende de la disponibilidad y de lo acordado; se verifica y se informa al cliente."),
        ("abc", "{F} Descubres que la misma cabaña tiene otra reserva confirmada para los días 13 y 14. ¿Qué corresponde?", "Avisar a la persona responsable y ofrecer a la señora Rojas fechas o alojamientos alternativos", "Confirmar igual y ver después quién llega primero", "Borrar la otra reserva para dejar libre la cabaña", "Confirmar dos veces engaña a un cliente, y borrar la otra reserva sin permiso perjudica a otra persona."),
        ("=", "{F} Si la señora Rojas reservara 2 cabañas iguales con las mismas fechas, ¿cuánto sería el total en pesos?", "2*(15-12)*40000", "Se multiplican cabañas, noches y tarifa por noche.", ""),
        ("abc", "Por teléfono, alguien dice ser pareja de una clienta y pide el teléfono y el correo con que ella reservó. ¿Qué haces?", "No entrego sus datos y ofrezco pasarle el mensaje a la clienta", "Se los entrego, porque dice ser su pareja", "Le entrego solo el correo, que es menos importante", "Los datos de un cliente no se entregan a terceros sin su autorización, aunque digan conocerlo."),
        ("abc", "Un cliente prefiere que lo contacten solo por correo y no quiere dar su celular. ¿Qué corresponde?", "Registrar el correo como su medio de contacto y respetar su decisión", "Insistir en que el celular es obligatorio en toda reserva", "Inventar un número para completar el campo", "El medio de contacto es el que el cliente autoriza; inventar datos deja registros falsos."),
    ],
    ctx=("abc", "Una amiga te escribe: «Trabajas en la agencia, ¿me pasas la planilla de reservas de este mes para ver quién viaja?». ¿Qué corresponde?", "Explicarle que la planilla tiene datos de clientes y no puedes compartirla", "Enviársela, porque es una amiga de confianza", "Enviarle solo las filas con teléfonos, que no importan", "Los datos de clientes son confidenciales y compartirlos sin autorización es un mal uso."),
    sc=[
        ("En Servicios de Turismo: ¿qué es una doble reserva?", "Confirmar dos veces el mismo servicio para las mismas fechas", "Se evita revisando la disponibilidad antes de confirmar."),
        ("¿Qué datos de un cliente debes pedir al reservar?", "Solo los necesarios para entregar el servicio", "Pedir de más aumenta el riesgo de filtración."),
        ("¿Qué haces si alguien ajeno pide los datos de un cliente?", "No los entrego y ofrezco pasar el mensaje al cliente", "Solo el cliente puede autorizar que se compartan sus datos."),
    ],
    op=("Esta es la ficha de reserva de una excursión de ejemplo con campos propuestos: nombre, fecha de la excursión, cantidad de personas, medio de contacto, forma de pago, color favorito, número de cédula completo y dirección de la casa. Marca los campos que pedirías y los que no, y explica con una frase por qué descartas cada uno.",
        "Pido: nombre, fecha, cantidad de personas, medio de contacto y forma de pago. No pido color favorito, cédula completa ni dirección de la casa: no son necesarios para entregar la excursión y pedirlos aumenta el riesgo si se filtran.",
        ["separa campos necesarios y no necesarios", "justifica cada descarte con una frase", "relaciona la decisión con la protección de datos"],
        ["lista de campos con su justificación"],
        ["pedir la cédula completa sin necesidad", "no justificar los descartes", "dejar la dirección «por si acaso»"],
        "Pregunta: «¿qué pasaría si se perdiera la planilla con la cédula de todos tus clientes?». Si no logra responder, repasa qué es un dato personal."),
    reinforce="Anota cinco datos que te pide un formulario de inscripción y marca cuáles son realmente necesarios.",
    extend="Explica con un ejemplo inventado qué pasaría si dos clientes reciben la misma cabaña y cómo se evita.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Reserva N.º R-0307 de la agencia «Rutas del Sur»: titular Marcos Pino; alojamiento de 2 noches en el «Hostal Los Aromos» (tarifa de ejemplo $30.000 por noche, habitación doble); "
     "excursión «Laguna Verde» de un día para 2 personas ($25.000 por persona); traslado de ida y vuelta ($20.000 en total). Estado de la reserva: pendiente de pago. "
     "Observación del cliente: una de las dos personas usa silla de ruedas y pide acceso sin escalones.")
build(
    O1, 2, F,
    use="Aprenderé los tipos de servicios turísticos, los documentos de una reserva (solicitud, confirmación y voucher), los estados de una reserva y el rol de cada persona.",
    prior=["Sé qué es una reserva y qué es un dato personal.", "Sé sumar y multiplicar con números enteros.", "Sé que un sistema digital guarda registros."],
    explain=[
        "Los servicios turísticos se agrupan en alojamiento, transporte, alimentación, actividades o excursiones, y paquete, que reúne varios servicios en uno. Al reservar se usan tres documentos: la solicitud, donde el cliente pide lo que quiere; la confirmación, donde la agencia responde por escrito qué queda reservado y a qué precio; y el voucher, el comprobante que el cliente presenta al prestador para recibir el servicio. Cada reserva tiene un código único, para no confundirla con otra.",
        "Una reserva pasa por estados: pendiente (aún falta pagar o confirmar), confirmada, cancelada o utilizada. El titular es la persona a cuyo nombre queda la reserva y quien responde por ella; solo el titular, o alguien que él autorice, puede pedir cambios. Los roles son: el cliente, el ejecutivo de reservas que ingresa los datos, y el prestador que entrega el servicio.",
        "Si el cliente informa una necesidad de accesibilidad, se registra con respeto en la reserva y se consulta por escrito a cada prestador si puede atenderla. No se supone qué puede o no hacer una persona: se le pregunta qué apoyo necesita. En el campo de observaciones se escriben datos útiles y objetivos, nunca juicios sobre la persona.",
    ],
    vocab=[("alojamiento", "servicio de hospedaje, como un hostal, una cabaña o un hotel"), ("voucher", "comprobante que el cliente presenta al prestador"), ("titular", "persona a cuyo nombre queda la reserva"), ("código de reserva", "número único que identifica una reserva"), ("estado de la reserva", "situación de la reserva: pendiente, confirmada, cancelada o utilizada"), ("paquete turístico", "varios servicios vendidos juntos")],
    worked=[
        ("Clasificar un servicio", "Una agencia de ejemplo vende la entrada a una visita guiada a un museo. ¿Qué tipo de servicio es?", ["Una visita guiada es algo que el turista hace durante su viaje.", "Eso corresponde a una actividad o excursión."], "Actividad o excursión"),
        ("Sumar los servicios", "Una reserva de ejemplo tiene 2 pasajes de bus a $8.000 cada uno y una noche de hostal a $27.000. ¿Cuál es el total?", ["Pasajes: 2 × 8.000 = 16.000.", "Total: 16.000 + 27.000 = 43.000."], "$43.000"),
    ],
    mistakes=[("Escribir en observaciones: «cliente complicado».", "Es un juicio sobre la persona, no un dato útil para el servicio.", "Anota solo datos objetivos y útiles, como el apoyo que necesita."),
              ("Dar por hecho que el hostal tiene acceso sin escalones porque «todos lo tienen».", "Sin confirmación escrita, la persona podría llegar y no poder usar el servicio.", "Pregunta por escrito al prestador y registra su respuesta.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un voucher?", "El comprobante que el cliente presenta al prestador para recibir el servicio reservado", "La tarifa más barata de la temporada", "El mapa de la ruta del paseo", "El voucher respalda la reserva ante el prestador; no es una tarifa ni un mapa."),
        ("abc", "¿Quién es el prestador de un servicio turístico?", "La empresa o persona que entrega el servicio, como un hostal o un transporte", "La persona que ingresa la reserva en el sistema", "La persona que viaja y paga", "El prestador entrega el servicio; el ejecutivo lo gestiona y el cliente lo contrata."),
        ("abc", "En Servicios de Turismo: ¿qué es el titular de una reserva?", "La persona a cuyo nombre queda la reserva y que responde por ella", "El prestador del servicio principal", "El ejecutivo que la ingresó", "El titular es la persona a cuyo nombre queda; los otros dos son roles distintos."),
        ("abc", "{F} ¿Qué tipo de servicio es la excursión «Laguna Verde»?", "Una actividad o excursión", "Un alojamiento", "Un servicio de alimentación", "Una salida de un día para recorrer un lugar es una excursión; no es hospedaje ni comida."),
        ("=", "{F} ¿Cuánto cuesta en pesos la reserva completa R-0307?", "2*30000+2*25000+20000", "Se suma el alojamiento de 2 noches, la excursión de 2 personas y el traslado.", ""),
        ("abc", "{F} ¿Qué significa que el estado de la reserva sea «pendiente de pago»?", "Que la reserva existe, pero aún falta pagar lo necesario para asegurarla", "Que el cliente la canceló", "Que el prestador ya entregó todos los servicios", "Pendiente significa que falta un paso; cancelada o utilizada serían otros estados."),
        ("=", "{F} Si el hostal subiera su tarifa a $35.000 por noche, ¿cuál sería el total de la reserva en pesos?", "2*35000+2*25000+20000", "Cambia solo el alojamiento; excursión y traslado se mantienen.", ""),
        ("abc", "{F} La observación habla de una persona en silla de ruedas. ¿Qué haces?", "Consultar por escrito a cada prestador si tiene acceso sin escalones y registrar su respuesta", "Asumir que todos los lugares son accesibles y no preguntar", "Sugerirle que no haga la excursión", "Se consulta y se registra para evitar sorpresas, sin decidir por la persona qué puede hacer."),
        ("abc", "{F} ¿Quién debe entregar la habitación y recibir el voucher del cliente?", "El Hostal Los Aromos, que es el prestador del alojamiento", "La agencia «Rutas del Sur», en la recepción del hostal", "El titular de la reserva", "El prestador entrega el servicio y recibe el comprobante; la agencia lo gestionó antes."),
        ("abc", "{F} Un amigo del titular llama y pide cambiar la reserva R-0307 sin ser el titular. ¿Qué corresponde?", "Pedir que el titular lo autorice y verificar quién es antes de modificar nada", "Cambiarla, porque conoce el código de reserva", "Cancelarla para evitar problemas", "Solo el titular o quien él autorice puede pedir cambios; conocer el código no basta."),
        ("ab", "En la planilla aparece el mismo código de reserva en dos filas con titulares distintos. ¿Cuál es el problema?", "El código debe ser único, así que hay que corregirlo antes de confirmar", "No hay problema, porque los titulares son distintos", "Un código repetido hace que dos reservas se confundan y se entregue mal el servicio."),
        ("=", "{F} El cliente cancela solo el traslado y la agencia, según su política de ejemplo, no cobra nada por esa cancelación. ¿Cuánto queda por pagar en pesos?", "2*30000+2*25000", "Se mantienen el alojamiento y la excursión, y se resta el traslado.", ""),
        ("abc", "En otra reserva, el campo de observaciones dice solo «cliente difícil». ¿Qué corresponde?", "Reemplazarlo por datos útiles y objetivos para el servicio, sin juicios", "Dejarlo, porque ayuda a otros ejecutivos a prepararse", "Agregar más calificativos para que quede claro", "Las observaciones deben servir al servicio, no etiquetar a la persona."),
    ],
    ctx=("abc", "{F} Al confirmar, el cliente pregunta qué debe llevar el día de la excursión para ser atendido. ¿Qué le indicas?", "Que presente el voucher de la excursión al prestador", "Que lleve la planilla de reservas de la agencia", "Que basta con decir «tengo reserva», sin comprobante", "El voucher es el comprobante que el prestador necesita para entregar el servicio."),
    sc=[
        ("En Servicios de Turismo: ¿para qué sirve el código de reserva?", "Para identificar una reserva sin confundirla con otra", "Cada reserva debe tener un código único."),
        ("¿Quién puede pedir cambios en una reserva?", "El titular o quien él autorice", "Así se protege al cliente de cambios no autorizados."),
        ("¿Cómo se registra una necesidad de accesibilidad?", "Con respeto, en forma objetiva, y consultando al prestador por escrito", "No se supone nada: se pregunta qué apoyo necesita la persona."),
    ],
    op=("La reserva de ejemplo R-0412 incluye: 3 noches de cabaña a $45.000 la noche, un paseo en bote para 3 personas a $18.000 por persona y un almuerzo grupal de $36.000 en total. Ordena la información en una tabla con servicio, tipo de servicio y costo, calcula el total y escribe qué documento recibe el cliente para presentar a cada prestador.",
        "Cabaña, alojamiento, 3 × 45.000 = 135.000. Paseo en bote, actividad, 3 × 18.000 = 54.000. Almuerzo, alimentación, 36.000. Total: 225.000. El cliente recibe un voucher por cada prestador, que presenta al llegar.",
        ["clasifica bien los tres servicios", "calcula el total sin errores", "nombra el voucher como comprobante para el prestador"],
        ["tabla con servicio, tipo y costo, y total"],
        ["clasificar el almuerzo como actividad", "olvidar multiplicar por las personas", "no mencionar el voucher"],
        "Pregunta: «¿qué le entregas al cliente para el almuerzo?». Si no responde, repasa los tres documentos de la reserva."),
    reinforce="Elige un viaje que hayas hecho y anota qué servicios usaste y de qué tipo era cada uno.",
    extend="Explica con un ejemplo inventado por qué una reserva necesita un código único.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (de ejemplo, inventada). Correo del señor Luis Vera a la agencia «Viajes Costa Azul»: «Quiero reservar una cabaña en febrero para mi familia: dos adultos y tres niños. Prefiero lo más barato.» "
     "Cabañas de ejemplo: A (capacidad 4 personas, $50.000 por noche), B (capacidad 6, $70.000 por noche) y C (capacidad 5, $65.000 por noche). "
     "Pasos de trabajo de la agencia: leer todo el mensaje, anotar los datos que faltan, consultarlos al cliente, revisar disponibilidad, ingresar la reserva, leer de vuelta los datos y confirmar por escrito.")
build(
    O1, 3, F,
    use="Aprenderé a analizar una solicitud incompleta, detectar los datos que faltan, elegir el servicio que corresponde y verificar lo ingresado leyéndolo de vuelta con el cliente.",
    prior=["Sé qué es una reserva y su política de cancelación.", "Sé calcular el costo de una estadía.", "Sé que los datos del cliente son privados."],
    explain=[
        "Analizar una solicitud es leerla completa y separar lo que dice de lo que falta. En una reserva de alojamiento los datos esenciales son: fechas exactas de entrada y salida, cantidad de personas, medio de contacto y forma de pago. Si falta uno, no se inventa ni se supone: se consulta al cliente antes de ingresar. Suponer una fecha puede dejar al cliente sin alojamiento el día que viaja.",
        "Para elegir el servicio se compara la necesidad con la capacidad, que es la cantidad máxima de personas que puede alojar una cabaña o una habitación. Primero se descartan las opciones donde no cabe el grupo; luego, entre las que sirven, se aplica el criterio del cliente, por ejemplo el menor precio. Si el cliente cambia un dato, como la cantidad de personas, se vuelve a analizar.",
        "Para evitar errores se hace una lectura de vuelta: se repiten al cliente la fecha, la cantidad de personas y el precio, y se corrige solo cuando él confirma el dato correcto. Después se confirma por escrito. La lectura de vuelta es parte del estándar de calidad de una agencia.",
    ],
    vocab=[("capacidad", "cantidad máxima de personas que puede alojar un servicio"), ("dato esencial", "dato sin el cual no se puede ingresar la reserva"), ("lectura de vuelta", "repetir al cliente lo ingresado para detectar errores"), ("criterio del cliente", "lo que el cliente prioriza, como el precio o la cercanía"), ("confirmación escrita", "respuesta por escrito con lo que queda reservado")],
    worked=[
        ("Revisar la capacidad", "Un grupo de ejemplo de 8 personas pide cabañas. Hay una de capacidad 4 y otra de capacidad 6. ¿Alcanza con una sola?", ["La capacidad de la más grande es 6 personas.", "6 es menor que 8, por lo tanto ninguna sola sirve: se necesitan dos cabañas."], "No: se necesitan dos cabañas"),
        ("Leer de vuelta", "Una clienta de ejemplo dice que sale el día 18, pero al leer de vuelta el sistema muestra salida el día 19. ¿Qué haces?", ["La diferencia puede ser un error de digitación.", "Preguntas a la clienta cuál es el día correcto y corriges solo después de su respuesta."], "Confirmo con la clienta y luego corrijo"),
    ],
    mistakes=[("Suponer que «febrero» significa del 1 al 7.", "Es inventar un dato que el cliente no dio; la reserva quedaría en fechas equivocadas.", "Consulta las fechas exactas antes de ingresar."),
              ("Elegir la opción más barata sin revisar la capacidad.", "Si el grupo no cabe, el servicio no sirve aunque sea barato.", "Descarta primero lo que no cabe y recién después compara precios.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un dato esencial de una reserva?", "Un dato sin el cual no se puede ingresar la reserva, como las fechas", "Un dato que decora la ficha, como el color favorito", "Un dato que solo importa después del viaje", "Sin las fechas no se puede reservar; los otros datos no condicionan la reserva."),
        ("abc", "En Servicios de Turismo: ¿qué es la lectura de vuelta?", "Repetir al cliente lo ingresado para detectar errores antes de confirmar", "Leer el correo del cliente solo una vez al recibirlo", "Volver a enviar el mismo correo", "La lectura de vuelta permite corregir errores de digitación con la confirmación del cliente."),
        ("abc", "En Servicios de Turismo: ¿qué es la capacidad de una cabaña?", "La cantidad máxima de personas que puede alojar", "La cantidad de noches que se puede reservar", "El precio más alto que puede cobrar", "La capacidad se mide en personas, no en noches ni en precio."),
        ("abc", "{F} ¿Qué dato esencial falta en el correo para revisar la disponibilidad?", "Los días exactos de entrada y salida", "El nombre de las cabañas", "La cantidad de niños", "El correo dice «febrero» pero no los días; sin ellos no se puede revisar disponibilidad."),
        ("abc", "{F} ¿Cuál es la cabaña más barata en la que cabe toda la familia?", "La C, porque cabe 5 personas y cuesta menos que la B", "La A, porque es la más barata de todas", "La B, porque es la de mayor capacidad", "La A es barata pero cabe solo 4; entre las que alcanzan, la C es la más económica."),
        ("=", "{F} Si la familia se aloja 4 noches en esa cabaña, ¿cuánto paga en total en pesos?", "4*65000", "Se multiplica la tarifa de la cabaña C por las 4 noches.", ""),
        ("=", "Otra familia de ejemplo reserva la cabaña B de la ficha por 3 noches. ¿Cuánto es el total en pesos?", "3*70000", "Se multiplica la tarifa de la cabaña B por las noches.", ""),
        ("abc", "{F} El señor Vera escribe después: «Se suma la abuela, seremos 6». ¿Qué cabaña corresponde ahora?", "La B, porque es la única con capacidad para 6 personas", "La C, porque sigue siendo la más barata", "La A, porque es la más barata de las tres", "Con 6 personas solo sirve la B; la C cabe solo 5 y la A, 4."),
        ("=", "{F} Con 6 personas y 4 noches, ¿cuántos pesos más paga el señor Vera que con 5 personas y 4 noches?", "4*70000-4*65000", "Se restan los totales de la cabaña B y de la cabaña C.", ""),
        ("abc", "El cliente escribió «febrero» y la agencia ingresa «1 de febrero» por suponerlo. ¿Qué error comete?", "Inventa un dato que el cliente no dio y puede reservar fechas equivocadas", "Ninguno, porque el primer día del mes es siempre el correcto", "Cobra de más por el mes completo", "Suponer una fecha es inventar un dato esencial; el cliente podría llegar y no tener alojamiento."),
        ("ab", "Al leer de vuelta, el cliente dice que sale el día 20, pero el sistema muestra el día 21. ¿Qué haces?", "Corrijo el sistema solo después de que el cliente confirme cuál es el día correcto", "Dejo el día 21, porque ya estaba ingresado", "La lectura de vuelta existe para detectar errores, y se corrige con la confirmación del cliente."),
        ("abc", "{F} El señor Vera responde: «No te doy mis fechas por escrito, llámame al celular». ¿Qué corresponde?", "Registrar el celular que él autoriza y llamarlo para acordar las fechas antes de reservar", "Reservar fechas supuestas y avisarle después", "Rechazar la reserva por no tener las fechas por escrito", "Se respeta el medio de contacto que el cliente elige, pero no se reserva sin fechas acordadas."),
        ("abc", "{F} El sistema indica que la cabaña C está libre del 5 al 9 de febrero, pero el señor Vera quería 5 noches. ¿Cómo se reserva correctamente?", "Informarle que esa cabaña da 4 noches y ofrecerle otras fechas u otra cabaña", "Reservarla igual hasta el 10, sin revisar", "Reservar la cabaña A sin consultarle", "Reservar fuera de lo disponible produce una doble reserva; el cliente debe decidir con información clara."),
    ],
    ctx=("abc", "Una compañera de la agencia anota las reservas en un cuaderno personal y se lo lleva a su casa. ¿Qué corresponde?", "Pasar los datos al sistema de la agencia y no sacar datos de clientes fuera del trabajo", "Dejarlo así, porque el cuaderno es suyo", "Fotografiar las páginas para guardarlas en su teléfono", "Los datos de clientes se guardan en los sistemas autorizados de la agencia y no en cuadernos personales."),
    sc=[
        ("En Servicios de Turismo: ¿qué haces si falta un dato esencial?", "Lo consulto al cliente antes de ingresar la reserva", "Suponer un dato puede dejar al cliente sin servicio."),
        ("¿Cómo eliges entre dos servicios que sirven?", "Aplico el criterio del cliente, por ejemplo el menor precio", "Primero se descarta lo que no cabe."),
        ("¿Para qué sirve la lectura de vuelta?", "Para detectar errores antes de confirmar por escrito", "El cliente confirma cada dato repetido."),
    ],
    op=("Correo de ejemplo de la señora Marta Díaz: «Necesito alojamiento para mi grupo de amigas, somos 7, cerca de la playa, el fin de semana largo.» Opciones de ejemplo: cabaña P (capacidad 6, $60.000 por noche), cabaña Q (capacidad 8, $85.000 por noche), dos cabañas R (capacidad 4 cada una, $45.000 por noche cada una). Escribe: los datos que faltan, qué opción es la más barata en que caben las 7 personas por 2 noches y la frase con que leerías de vuelta los datos.",
        "Faltan fechas exactas, medio de contacto y forma de pago. Cabaña P no sirve (cabe 6). Q cuesta 2 × 85.000 = 170.000. Dos cabañas R cuestan 2 × 2 × 45.000 = 180.000. La más barata es la Q, 170.000. Lectura de vuelta: «Entonces son 7 personas, cabaña Q, 2 noches, del día… al día…, por 170.000 pesos, ¿es correcto?».",
        ["identifica los datos que faltan", "descarta la opción donde no caben y calcula los costos", "redacta una lectura de vuelta completa"],
        ["lista de datos que faltan, cálculo y frase de lectura de vuelta"],
        ["elegir la cabaña P sin revisar la capacidad", "olvidar multiplicar por las dos cabañas R", "no incluir el precio en la lectura de vuelta"],
        "Pregunta: «¿por qué no sirve la cabaña P aunque sea más barata?». Si no responde, repasa la regla de la capacidad."),
    reinforce="Escribe una solicitud de reserva incompleta con dos datos que faltan y anota qué le preguntarías al cliente.",
    extend="Explica con un ejemplo inventado por qué leer de vuelta los datos ahorra problemas a la agencia y al cliente.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (de ejemplo, inventada). Tarifario del «Hotel Los Quillayes» (inventado): habitación doble, temporada baja $45.000 por noche y temporada alta $60.000 por noche, desayuno incluido; cama extra $10.000 por noche. "
     "Para asegurar la reserva se paga un anticipo de ejemplo del 30 % del total; el resto es el saldo, que se paga al llegar. Reserva pedida por un cliente: 3 noches en temporada alta, con 1 cama extra durante las 3 noches.")
build(
    O1, 4, F,
    use="Aprenderé a calcular el precio de una reserva con la tarifa de la temporada, los extras, el anticipo y el saldo, y a comprobar el resultado antes de confirmarlo.",
    prior=["Sé multiplicar y restar con números enteros.", "Sé qué es una tarifa por noche.", "Sé calcular un porcentaje exacto como 10 % o 30 % de una cantidad."],
    explain=[
        "El precio de una reserva se calcula en orden: primero el valor de una noche (tarifa base más extras por noche, como una cama adicional); luego se multiplica por las noches; por último se aplican descuentos o anticipos. La tarifa depende de la temporada: la temporada alta es el período con más demanda, y suele costar más que la temporada baja, con menos demanda. Los precios que se informan deben decir si incluyen impuestos, según la norma vigente.",
        "El anticipo es una parte del total que se paga antes para asegurar la reserva, y el saldo es lo que falta por pagar. Un porcentaje se calcula multiplicando el total por el porcentaje y dividiendo por 100: el 30 % de 200.000 es 200.000 × 30 ÷ 100 = 60.000. Los porcentajes de este cuaderno son de ejemplo; los reales los fija cada empresa.",
        "Antes de confirmar se verifica el cálculo: se repite con otro camino, por ejemplo calcular el total y comprobar que anticipo más saldo da el total. Se informa al cliente por escrito qué incluye el precio, como el desayuno, y qué se cobra aparte.",
    ],
    vocab=[("temporada alta", "período de mayor demanda, con tarifas generalmente más altas"), ("temporada baja", "período de menor demanda, con tarifas más bajas"), ("anticipo", "parte del total que se paga antes para asegurar la reserva"), ("saldo", "lo que falta por pagar después del anticipo"), ("extra", "servicio adicional que se cobra aparte, como una cama extra"), ("tarifa base", "precio de la noche sin extras")],
    worked=[
        ("Anticipo y saldo", "Una reserva de ejemplo suma $80.000 y exige un anticipo del 25 %. ¿Cuánto es el anticipo y cuánto el saldo?", ["Anticipo: 80.000 × 25 ÷ 100 = 20.000.", "Saldo: 80.000 − 20.000 = 60.000."], "Anticipo $20.000 y saldo $60.000"),
        ("Comparar temporadas", "Un hostal de ejemplo cobra $38.000 por noche en temporada baja y $52.000 en alta. ¿Cuánto más cuestan 2 noches en alta?", ["Diferencia por noche: 52.000 − 38.000 = 14.000.", "Para 2 noches: 14.000 × 2 = 28.000."], "$28.000 más"),
    ],
    mistakes=[("Cobrar la cama extra una sola vez cuando el cliente la usa varias noches.", "El extra está fijado por noche; cobrarlo una vez deja al cliente con un precio falso y a la agencia con pérdida.", "Suma el extra a cada noche antes de multiplicar."),
              ("Calcular el anticipo sobre una sola noche en vez de sobre el total.", "El porcentaje de ejemplo se aplica al total de la reserva.", "Calcula primero el total y luego el porcentaje.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un anticipo?", "Una parte del total que se paga antes para asegurar la reserva", "El descuento que se hace al llegar", "El impuesto que cobra el prestador", "El anticipo es un pago previo; el descuento y el impuesto son otros conceptos."),
        ("abc", "En Servicios de Turismo: ¿qué es la temporada alta?", "El período con más demanda, en que las tarifas suelen ser mayores", "El período en que el alojamiento cierra", "El horario de mayor atención al público", "La temporada alta se define por la demanda, no por el horario ni por el cierre."),
        ("abc", "En Servicios de Turismo: ¿qué es el saldo en una reserva?", "Lo que falta por pagar después del anticipo", "El dinero que se devuelve al cliente al terminar", "La suma del anticipo y de los extras", "El saldo completa el pago: total menos anticipo."),
        ("=", "{F} ¿Cuánto cuesta en pesos una noche con la cama extra en temporada alta?", "60000+10000", "Se suma la tarifa de la noche y el extra de esa noche.", ""),
        ("=", "{F} ¿Cuál es el total en pesos de las 3 noches pedidas por el cliente?", "3*(60000+10000)", "Cada noche cuesta tarifa más cama extra, y se multiplica por 3.", ""),
        ("=", "{F} ¿Cuántos pesos es el anticipo del 30 % de ejemplo?", "3*(60000+10000)*30//100", "Se calcula el total y se multiplica por 30 y se divide por 100.", ""),
        ("=", "{F} ¿Cuántos pesos es el saldo que se paga al llegar?", "3*(60000+10000)-3*(60000+10000)*30//100", "El saldo es el total menos el anticipo.", ""),
        ("=", "{F} ¿Cuántos pesos menos pagaría el cliente por las mismas 3 noches con cama extra en temporada baja?", "3*(60000+10000)-3*(45000+10000)", "Se restan el total en temporada baja del total en temporada alta.", ""),
        ("abc", "{F} Un compañero calculó el total como 3 × 60.000 + 10.000. ¿Cuál es su error?", "Cobró la cama extra una sola vez, pero el extra es por noche", "Usó la tarifa de temporada baja", "No restó el anticipo", "Su resultado es 190.000, porque sumó el extra una vez en vez de tres."),
        ("abc", "{F} El cliente pregunta si el desayuno cuesta aparte. ¿Qué respondes?", "Que según el tarifario el desayuno está incluido y no se cobra aparte", "Que se paga al llegar, porque no figura en el tarifario", "Que depende del día, aunque no haya cargo en el tarifario", "El tarifario dice «desayuno incluido»; responder otra cosa informaría un cobro inexistente."),
        ("=", "Otro hotel de ejemplo cobra $55.000 por noche y da 10 % de descuento a quien reserva 4 noches o más. ¿Cuánto paga en pesos una persona por 4 noches?", "4*55000*90//100", "Se calcula el total y se paga el 90 % de ese total.", ""),
        ("abc", "{F} Otro cliente quiere 3 noches en temporada alta sin cama extra y dispone de $190.000. ¿Le alcanza el dinero?", "Sí, porque el total es $180.000, menor que $190.000", "No, porque el total sería $210.000", "No, porque falta pagar el anticipo antes", "3 × 60.000 = 180.000; el total de 210.000 corresponde al caso con cama extra."),
        ("=", "{F} Un grupo reserva 2 habitaciones dobles en temporada baja por 2 noches, y una sola cama extra por noche en total. ¿Cuánto es el total en pesos?", "2*2*45000+2*10000", "Se multiplican habitaciones y noches por la tarifa y se suma la cama extra de las 2 noches.", ""),
    ],
    ctx=("abc", "{F} El cliente dice: «Pago el anticipo hoy, pero si cambio de fecha, ¿me devuelven el dinero?». ¿Qué corresponde?", "Revisar la política de cancelación y cambios, y responderle por escrito lo que establece", "Prometerle la devolución completa para que reserve", "Decirle que nunca se devuelve nada, sin revisar", "La devolución depende de la política acordada; no se promete ni se niega sin revisarla."),
    sc=[
        ("En Servicios de Turismo: ¿qué es el saldo?", "Lo que falta por pagar después del anticipo", "El saldo se calcula restando el anticipo al total."),
        ("¿Cómo se calcula un anticipo del 30 %?", "Multiplicando el total por 30 y dividiendo por 100", "El porcentaje se aplica al total de la reserva."),
        ("¿Por qué se verifica el cálculo antes de confirmar?", "Porque un error en el precio perjudica al cliente o a la agencia", "Se comprueba que anticipo más saldo dé el total."),
    ],
    op=("Un hostal de ejemplo cobra $40.000 por noche en temporada baja y $55.000 en alta; la cama extra cuesta $8.000 por noche; el anticipo de ejemplo es 20 %. Un cliente pide 4 noches en temporada alta con una cama extra. Calcula el total, el anticipo y el saldo, y escribe el mensaje de confirmación de dos líneas que enviarías.",
        "Noche: 55.000 + 8.000 = 63.000. Total: 4 × 63.000 = 252.000. Anticipo: 252.000 × 20 ÷ 100 = 50.400. Saldo: 201.600. Mensaje: «Confirmamos 4 noches en temporada alta con cama extra, total $252.000. Anticipo de $50.400 para asegurar y saldo de $201.600 al llegar, según la política de cancelación».",
        ["calcula noche, total, anticipo y saldo", "comprueba que anticipo más saldo da el total", "redacta una confirmación clara con montos"],
        ["hoja con cálculos y mensaje de confirmación"],
        ["cobrar la cama extra solo una vez", "calcular el anticipo sobre una noche", "no informar el saldo"],
        "Pregunta: «¿cómo compruebas que tu saldo está bien?». Si no responde, pídele que sume anticipo y saldo."),
    reinforce="Inventa un tarifario de dos temporadas y calcula tres noches en cada una.",
    extend="Explica con un ejemplo inventado por qué el cliente debe saber por escrito qué incluye el precio.",
)
