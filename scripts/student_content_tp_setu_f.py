"""Servicios de Turismo TP 3.º y 4.º medio: OAE-06 (elaborar propuestas de programas turísticos básicos). Todo en papel; zona, prestadores y precios de ejemplo."""
from __future__ import annotations

from tp_setu_common import build

O6 = "TP-SETU-3y4-OAE-06"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (de ejemplo, inventada). Zona ficticia «Valle de Brisa». Atractivos: Humedal Las Totoras (natural; sendero con rampa), Museo Comunitario (cultural; dos pisos con ascensor) y Mirador del Cerro (natural; 120 escalones). "
     "Servicios: Cabañas Los Alerces (autorización vigente informada), Hostal El Canelo (no ha mostrado autorización vigente), Restaurante Mesa Chica (autorización vigente informada) y Transporte Brisa (empresa autorizada). "
     "Temporada alta de ejemplo: diciembre a febrero. Un cliente pide un programa básico de 2 días para 6 personas, entre ellas una persona mayor que prefiere evitar escalones. Viajan en enero.")
build(
    O6, 1, F,
    use="Aprenderé qué es un programa turístico básico, qué elementos lo forman, qué normas y autorizaciones debe respetar y qué riesgos hay al elaborarlo: promesas incumplibles, costos ocultos y prestadores sin autorización.",
    prior=["Sé qué es una reserva y un atractivo.", "Sé calcular costos con números enteros.", "Sé que se informa solo lo confirmado."],
    explain=[
        "Un programa turístico básico es una propuesta organizada de uno a pocos días que reúne atractivos, alojamiento, alimentación, transporte y actividades, con sus costos, accesos, horarios e información relevante. Se elabora a partir del contexto local, es decir, qué atractivos y servicios hay, en qué época y con qué disponibilidad, y de las características de los turistas, como edad, intereses, presupuesto y necesidades de accesibilidad.",
        "Todo programa debe respetar las normas y regulaciones vigentes. Una de ellas es trabajar con prestadores autorizados, es decir, que cuentan con las autorizaciones que exige la norma vigente; si no se puede confirmar, no se incluye en el programa. Las actividades de turismo aventura, de transporte, acuáticas o en altura solo se ofrecen con prestadores y guías o instructores autorizados. Los riesgos al elaborar un programa son prometer lo que no se puede cumplir, no informar todos los costos, incluir prestadores sin autorización y no considerar la accesibilidad.",
        "Este cuaderno es aprendizaje en papel: los programas reales los elabora y vende una agencia autorizada, con prestadores verificados y la norma vigente. Los precios y la zona de este cuaderno son de ejemplo.",
    ],
    vocab=[("programa turístico básico", "propuesta organizada de pocos días con servicios, costos y horarios"), ("contexto local", "atractivos, servicios, época y disponibilidad de una zona"), ("prestador autorizado", "empresa o persona que cuenta con las autorizaciones que exige la norma vigente"), ("temporada alta", "período de mayor demanda, con tarifas generalmente más altas"), ("costo oculto", "gasto que el cliente no fue informado de antemano")],
    worked=[
        ("Costo de una actividad", "Una actividad de ejemplo cuesta $3.500 por persona y viajan 4 personas. ¿Cuánto cuesta en total?", ["Se multiplica el valor por persona por la cantidad de personas.", "3.500 × 4 = 14.000."], "$14.000"),
        ("Filtrar por accesibilidad", "Un cliente de ejemplo prefiere evitar escalones. Hay un museo con ascensor y un mirador de 80 escalones. ¿Cuál corresponde incluir?", ["El museo cuenta con ascensor.", "El mirador no se ajusta a la preferencia, salvo que el cliente diga otra cosa."], "El museo"),
    ],
    mistakes=[("Incluir un hostal sin confirmar su autorización «porque es barato».", "Un prestador sin autorización puede incumplir la norma y poner en riesgo al cliente.", "Incluye solo prestadores con autorización confirmada."),
              ("Dar un precio sin aclarar qué incluye.", "El cliente puede descubrir costos extra más tarde y sentirse engañado.", "Aclara por escrito qué incluye y qué no.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un programa turístico básico?", "Una propuesta organizada de pocos días que reúne servicios, costos y horarios", "Un álbum de fotos de un viaje pasado", "El permiso para guiar en un parque", "El programa organiza la propuesta de un viaje; las fotos y el permiso son otras cosas."),
        ("abc", "En Servicios de Turismo: ¿qué es el contexto local de un programa?", "Los atractivos, servicios, época y disponibilidad de una zona", "El número de turistas del año anterior", "El precio que cobra la agencia", "El contexto describe lo que hay en la zona y cuándo."),
        ("abc", "¿Por qué se incluyen solo prestadores autorizados?", "Porque la norma vigente lo exige y protege a los clientes", "Porque son siempre los más baratos", "Porque así hay menos que comparar", "La autorización responde a la norma y resguarda al cliente."),
        ("abc", "{F} ¿Qué atractivo de la ficha no se ajusta a la preferencia de evitar escalones?", "El Mirador del Cerro, con 120 escalones", "El Museo Comunitario, con ascensor", "El Humedal Las Totoras, con sendero con rampa", "Solo el mirador tiene escalones; los otros tienen ascensor o rampa."),
        ("abc", "{F} ¿Qué prestador conviene no incluir hasta confirmar su autorización?", "Hostal El Canelo", "Cabañas Los Alerces", "Transporte Brisa", "El hostal no ha mostrado autorización; los otros prestadores la tienen informada."),
        ("=", "{F} El museo de ejemplo cuesta $4.000 por persona. ¿Cuánto cuesta en total para las 6 personas del grupo?", "6*4000", "Se multiplica el valor por persona por 6.", ""),
        ("abc", "{F} El cliente viaja en enero. ¿Qué implica para el programa?", "Que es temporada alta, así que conviene confirmar disponibilidad y precios con anticipación", "Que no habrá ningún servicio abierto", "Que los precios siempre son menores", "Enero está en la temporada alta de ejemplo, con más demanda."),
        ("abc", "{F} El cliente pide agregar una actividad de turismo aventura que no está en la ficha. ¿Qué corresponde?", "Ofrecerla solo con un prestador autorizado, con guía o instructor autorizado, y según la norma vigente", "Armarla con el equipo que haya disponible", "Prometerla sin confirmar nada", "Las actividades de aventura requieren prestadores e instructores autorizados."),
        ("=", "{F} Con una cabaña de ejemplo para 6 personas a $70.000 la noche, ¿cuánto cuestan 2 noches?", "2*70000", "Se multiplica la tarifa por las noches.", ""),
        ("abc", "El cliente pide un precio «con todo incluido», pero no dice qué es todo. ¿Qué haces?", "Aclarar por escrito qué incluye y qué no, antes de cotizar", "Prometer que todo está incluido para cerrar la venta", "Cotizar solo el alojamiento", "Sin aclarar lo incluido se generan malentendidos y costos ocultos."),
        ("abc", "{F} Para la persona que prefiere evitar escalones, ¿qué corresponde hacer al elaborar el programa?", "Preguntarle qué otras condiciones necesita y elegir atractivos con acceso adecuado confirmado", "Suponer que no puede salir y dejar su participación fuera", "Asegurar que todo es accesible sin revisar", "Se pregunta y se confirma el acceso, sin suponer."),
        ("abc", "Un compañero propone decir en el folleto que el humedal «tiene el ave más rara del continente» sin comprobarlo. ¿Qué corresponde?", "No afirmarlo e incluir solo información confirmada", "Afirmarlo, porque atrae visitantes", "Afirmarlo, pero con letra pequeña", "Una afirmación sin comprobación puede engañar al cliente."),
        ("abc", "El dueño de una cabaña pide que no se informe que su cabaña no tiene acceso sin escalones. ¿Qué corresponde?", "Informar la condición real, porque el cliente decide con información veraz", "Ocultarlo para no perder la venta", "Ocultarlo solo si el cliente no pregunta", "El cliente necesita saber las condiciones reales para elegir."),
    ],
    ctx=("abc", "{F} El cliente pregunta si pueden agregar una excursión a un lugar protegido que no figura en la ficha, sin guía, «para ahorrar». ¿Qué corresponde?", "Explicar que se ofrece solo con prestadores y guías autorizados, según la norma de cuidado del lugar", "Aceptar si el grupo se compromete a cuidarse solo", "Aceptar y no mencionarlo en el programa", "Los lugares protegidos tienen reglas y se visitan con prestadores autorizados."),
    sc=[
        ("En Servicios de Turismo: ¿qué es un prestador autorizado?", "El que cuenta con las autorizaciones que exige la norma vigente", "Si no se puede confirmar, no se incluye."),
        ("¿Qué se informa al cliente sobre los costos?", "Todo lo que incluye y lo que no incluye el precio", "Así se evitan los costos ocultos para el cliente."),
        ("¿Cómo se atiende una preferencia de accesibilidad?", "Se pregunta y se confirma el acceso de cada lugar", "No se supone lo que la persona puede o no hacer."),
    ],
    op=("Un cliente de ejemplo pide un programa básico de 2 días para 4 personas, que incluya un museo, una comida y un paseo corto. Escribe una lista de cinco elementos que debe tener tu propuesta (por ejemplo: atractivos, alojamiento) y, para cada uno, un dato que debes confirmar antes de ofrecerlo.",
        "Atractivos: horario y acceso. Alojamiento: autorización vigente y disponibilidad. Alimentación: autorización y qué incluye el menú. Transporte: empresa autorizada y horario. Costos: qué incluye y qué no, y si el precio incluye impuestos según la norma vigente.",
        ["incluye cinco elementos distintos del programa", "cada elemento tiene un dato a confirmar", "menciona autorizaciones y costos incluidos"],
        ["lista de cinco elementos con su dato a confirmar"],
        ["repetir el mismo dato a confirmar", "olvidar las autorizaciones", "no mencionar qué incluye el precio"],
        "Pregunta: «¿qué pasa si no confirmas la autorización del alojamiento?». Si no responde, repasa la regla de prestadores autorizados."),
    reinforce="Elige un lugar cercano a tu casa y anota tres servicios que formarían parte de un programa de un día.",
    extend="Explica con un ejemplo inventado por qué un precio sin detalle de lo que incluye puede generar un reclamo.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Cotización del programa «Fin de semana en Valle de Brisa» para 6 personas, 3 días y 2 noches. Alojamiento: cabaña a $90.000 por noche. "
     "Alimentación: $9.000 por persona por día (3 días). Traslado en bus privado: $60.000 en total. Actividad: museo, $4.000 por persona. Incluye: alojamiento, alimentación, museo y traslados. Excluye: bebidas alcohólicas y gastos personales. "
     "Anticipo de ejemplo: 25 % del total. Documentos del programa: cotización, itinerario por día, voucher por prestador y ficha del pasajero (datos personales, solo para el equipo). Roles: ejecutivo de programas, prestadores y cliente.")
build(
    O6, 2, F,
    use="Aprenderé los elementos y documentos de un programa (cotización, itinerario, inclusiones y exclusiones, voucher), cómo se calculan costos directos y por persona, y los roles de quienes participan.",
    prior=["Sé qué es un programa turístico básico.", "Sé multiplicar y dividir con números enteros.", "Sé qué es un voucher."],
    explain=[
        "La cotización es el documento que informa al cliente el precio y lo que incluye. El itinerario es el plan día por día, con horarios, traslados y actividades. En la cotización se separan las inclusiones, que son los servicios cubiertos por el precio, y las exclusiones, que son lo que el cliente paga aparte. El voucher es el comprobante que se entrega para cada prestador y la ficha del pasajero reúne datos personales que solo ve el equipo.",
        "El costo directo es el total de lo que cuestan los servicios del programa: alojamiento, alimentación, transporte y actividades. Para el alojamiento se multiplica la tarifa por las noches; para la alimentación, el valor por persona por la cantidad de personas y de días. El costo por persona es el costo total dividido por la cantidad de personas. El precio informado debe decir si incluye impuestos, según la norma vigente.",
        "Los roles son: el ejecutivo de programas, que elabora la propuesta; los prestadores, que entregan cada servicio; y el cliente, que decide. Los datos del cliente se piden solo en la medida necesaria y se guardan con clave.",
    ],
    vocab=[("cotización", "documento con el precio y lo que incluye el programa"), ("itinerario", "plan día por día con horarios y actividades"), ("inclusiones", "servicios cubiertos por el precio"), ("exclusiones", "lo que el cliente paga aparte"), ("costo directo", "total de lo que cuestan los servicios del programa"), ("costo por persona", "costo total dividido por la cantidad de personas")],
    worked=[
        ("Costo de alimentación", "Un programa de ejemplo tiene 5 personas, 2 días y $8.000 por persona por día. ¿Cuánto cuesta la alimentación?", ["Se multiplican personas, días y valor diario.", "5 × 2 × 8.000 = 80.000."], "$80.000"),
        ("Costo por persona", "El costo total de un programa de ejemplo es $360.000 para 6 personas. ¿Cuál es el costo por persona?", ["Se divide el total por la cantidad de personas.", "360.000 ÷ 6 = 60.000."], "$60.000 por persona"),
    ],
    mistakes=[("Olvidar la exclusión «gastos personales» en la cotización.", "El cliente puede creer que todo está pagado y reclamar después.", "Escribe las exclusiones de forma clara."),
              ("Calcular la alimentación solo por un día.", "El programa tiene 3 días y el costo se subestima.", "Multiplica por los días del programa.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una cotización?", "El documento que informa al cliente el precio y lo que incluye el programa", "El comprobante que se entrega al prestador", "El plan de horarios de cada día", "La cotización informa precio e inclusiones; el voucher y el itinerario son otros documentos."),
        ("abc", "En Servicios de Turismo: ¿qué es un itinerario?", "El plan día por día, con horarios y actividades", "La lista de precios de los prestadores", "La ficha con los datos personales del pasajero", "El itinerario ordena el programa por día y horario."),
        ("abc", "En Servicios de Turismo: ¿qué son las exclusiones de un programa?", "Lo que el cliente paga aparte", "Los servicios cubiertos por el precio", "Las actividades más caras", "Las exclusiones se informan para evitar malentendidos."),
        ("=", "{F} ¿Cuánto cuesta el alojamiento de las 2 noches?", "2*90000", "Se multiplica la tarifa por noche por las 2 noches.", ""),
        ("=", "{F} ¿Cuánto cuesta la alimentación de las 6 personas durante los 3 días?", "6*3*9000", "Se multiplican personas, días y valor diario por persona.", ""),
        ("=", "{F} ¿Cuánto cuesta el museo para las 6 personas?", "6*4000", "Se multiplica el valor por persona por 6.", ""),
        ("=", "{F} ¿Cuál es el costo directo total del programa?", "2*90000+6*3*9000+60000+6*4000", "Se suman alojamiento, alimentación, traslado y museo.", ""),
        ("=", "{F} ¿Cuál es el costo por persona?", "(2*90000+6*3*9000+60000+6*4000)//6", "Se divide el costo total por las 6 personas.", ""),
        ("=", "{F} ¿Cuánto es el anticipo del 25 % de ejemplo?", "(2*90000+6*3*9000+60000+6*4000)*25//100", "Se multiplica el total por 25 y se divide por 100.", ""),
        ("abc", "{F} El cliente pregunta si el precio cubre un vino en la cena. ¿Qué respondes?", "Que no, porque las bebidas alcohólicas están excluidas del precio", "Que sí, porque la cena está incluida", "Que depende de lo que pida el grupo, sin mirar la cotización", "La cotización excluye las bebidas alcohólicas; se informa con claridad."),
        ("abc", "{F} ¿Por qué la ficha del pasajero se guarda con clave y solo la ve el equipo?", "Porque tiene datos personales que no deben conocer otras personas", "Porque así se evita imprimirla", "Porque los pasajeros no quieren recibir información", "Los datos personales se protegen y se comparten solo lo necesario."),
        ("abc", "{F} Un prestador pide la ficha completa del pasajero con todos sus datos. ¿Qué corresponde?", "Entregarle solo los datos necesarios para entregar su servicio", "Entregarle la ficha completa", "No darle ningún dato, ni el nombre", "Se comparte solo lo necesario; el nombre suele hacer falta para el voucher."),
        ("abc", "{F} Se agrega una cena especial que cuesta $12.000 por persona para los 6. ¿Qué corresponde actualizar?", "El costo total, la cotización y el itinerario, y avisar al cliente", "Solo el itinerario", "Nada, porque el precio ya estaba informado", "Un cambio afecta costo, cotización e itinerario y el cliente debe saberlo."),
    ],
    ctx=("abc", "{F} El cliente pide una rebaja del 50 % en la cotización sin cambiar el programa. ¿Qué corresponde?", "Explicar que el precio depende de los costos de los prestadores y ofrecer revisar el programa para ajustarlo", "Aceptar la rebaja para no perder la venta", "Cambiar los precios de los prestadores sin avisarles", "El precio se ajusta modificando servicios, no inventando rebajas."),
    sc=[
        ("En Servicios de Turismo: ¿qué diferencia hay entre inclusiones y exclusiones?", "Las inclusiones están cubiertas por el precio y las exclusiones se pagan aparte", "Ambas se informan en la cotización."),
        ("¿Cómo se calcula el costo por persona?", "Se divide el costo total por la cantidad de personas", "Así se compara con el presupuesto individual."),
        ("¿Qué documento entregas para que el cliente use el servicio?", "El voucher de cada prestador", "El voucher es el comprobante ante el prestador."),
    ],
    op=("Elabora la cotización de un programa de ejemplo para 4 personas, 2 días y 1 noche: alojamiento $80.000 la noche, alimentación $10.000 por persona por día, traslado $40.000 en total y una actividad de $5.000 por persona. Escribe el costo de cada ítem, el total, el costo por persona, dos inclusiones y dos exclusiones.",
        "Alojamiento: 1 × 80.000 = 80.000. Alimentación: 4 × 2 × 10.000 = 80.000. Traslado: 40.000. Actividad: 4 × 5.000 = 20.000. Total: 220.000. Por persona: 55.000. Inclusiones: alojamiento y traslado. Exclusiones: bebidas alcohólicas y gastos personales.",
        ["calcula bien cada ítem y el total", "calcula el costo por persona", "escribe inclusiones y exclusiones claras"],
        ["cotización con ítems, total, costo por persona, inclusiones y exclusiones"],
        ["multiplicar la alimentación solo por un día", "no escribir exclusiones", "dividir por un número de personas incorrecto"],
        "Pregunta: «¿cuántos días multiplicaste en la alimentación?». Si no responde, repasa el cálculo con personas, días y valor diario."),
    reinforce="Anota cuánto gastarías en alimentación para un paseo de un día con tu familia y cuánto por persona.",
    extend="Explica con un ejemplo inventado por qué las exclusiones deben estar escritas y no solo dichas.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (de ejemplo, inventada). Pedido de una familia de 5 personas (2 adultos, 1 persona mayor que necesita acceso sin escalones y 2 niños) para 3 días y 2 noches, con un presupuesto máximo de $450.000 en total. "
     "Alojamiento: Cabaña Verde, sin escalones, $60.000 por noche para toda la familia; Hostal Centro, acceso solo por escalera, $45.000 por noche, desayuno incluido. "
     "Alimentación estimada: $12.000 por persona por día. Transporte local: $2.000 por persona por día. Actividades por persona: museo $4.000, paseo en bote $10.000 y taller de cerámica $8.000.")
build(
    O6, 3, F,
    use="Aprenderé a analizar el perfil de un cliente (necesidades, presupuesto, intereses), seleccionar los componentes de un programa y comprobar que se cumple el presupuesto y la accesibilidad.",
    prior=["Sé calcular costos de alojamiento, alimentación y actividades.", "Sé qué es una cotización.", "Sé que se pregunta a la persona qué necesita."],
    explain=[
        "El perfil del turista es el conjunto de sus características e intereses: edad, necesidades, presupuesto y gustos. Para analizar un caso se separan las necesidades, que son lo indispensable, como el acceso sin escalones, y las restricciones, como el presupuesto máximo. Primero se eligen los componentes que cumplen las necesidades; después se calcula el costo y se agregan actividades con el dinero que sobra.",
        "El orden de cálculo es: alojamiento (tarifa por noche por las noches), alimentación (valor por persona por día por personas y días), transporte (igual) y, con lo que queda del presupuesto, las actividades (valor por persona por la cantidad de personas). Si una actividad tiene una condición, como una edad mínima, se revisa con el prestador y se ofrece una alternativa. No se supone qué puede hacer una persona: se le pregunta.",
        "La opción más barata no siempre es la adecuada: si no cumple una necesidad, se descarta. Se informa al cliente con claridad por qué se recomienda cada componente.",
    ],
    vocab=[("perfil del turista", "características e intereses de un turista o grupo"), ("necesidad", "lo indispensable para que el programa sirva a una persona"), ("restricción", "límite como el presupuesto o el tiempo"), ("componente", "parte del programa, como alojamiento, alimentación o actividad"), ("saldo del presupuesto", "dinero que queda después de los componentes ya elegidos")],
    worked=[
        ("Descartar una opción", "Una familia de ejemplo necesita acceso sin escalones. El hostal A es más barato pero tiene escalera; el hostal B tiene rampa. ¿Cuál se recomienda?", ["La necesidad de acceso es indispensable.", "El hostal A no la cumple aunque sea más barato; se recomienda el B."], "El hostal B"),
        ("Saldo del presupuesto", "Un presupuesto de ejemplo de $300.000 tiene gastos de $240.000 en alojamiento y alimentación. ¿Cuánto queda para actividades?", ["Se resta el gasto al presupuesto.", "300.000 − 240.000 = 60.000."], "$60.000"),
    ],
    mistakes=[("Elegir el alojamiento más barato sin revisar la necesidad de accesibilidad.", "Si no cumple lo indispensable, el programa no sirve a esa persona.", "Revisa primero las necesidades y después compara precios."),
              ("Agregar actividades hasta agotar el presupuesto sin dejar margen.", "Cualquier gasto imprevisto deja al cliente sin dinero.", "Deja un margen y avisa si el total queda muy ajustado.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es el perfil del turista?", "El conjunto de sus características e intereses, como edad, necesidades, presupuesto y gustos", "La lista de lugares que ya visitó", "El nombre de su agencia", "El perfil describe a la persona o grupo para ajustar el programa."),
        ("abc", "En Servicios de Turismo: ¿qué es una necesidad de accesibilidad?", "Una condición indispensable para que la persona pueda usar el servicio, como evitar escalones", "Un gusto por los lugares tranquilos", "Una promoción de la temporada", "Una necesidad es indispensable; un gusto o una promoción no lo son."),
        ("abc", "En Servicios de Turismo: ¿qué es el saldo del presupuesto?", "El dinero que queda después de los componentes ya elegidos", "El dinero que la agencia gana", "El anticipo que se paga al reservar", "El saldo es lo que queda disponible para otros componentes."),
        ("abc", "{F} ¿Qué alojamiento corresponde recomendar a la familia?", "La Cabaña Verde, porque no tiene escalones y cumple la necesidad de la persona mayor", "El Hostal Centro, porque es más barato", "El Hostal Centro, porque incluye desayuno", "La necesidad de acceso sin escalones es indispensable; solo la cabaña la cumple."),
        ("=", "{F} ¿Cuánto cuestan las 2 noches en la Cabaña Verde?", "2*60000", "Se multiplica la tarifa por noche por las 2 noches.", ""),
        ("=", "{F} ¿Cuánto cuesta la alimentación de las 5 personas durante los 3 días?", "5*12000*3", "Se multiplican personas, valor diario y días.", ""),
        ("=", "{F} ¿Cuánto cuesta el transporte local de las 5 personas durante los 3 días?", "5*2000*3", "Se multiplican personas, valor diario y días.", ""),
        ("=", "{F} Después de alojamiento, alimentación y transporte, ¿cuánto queda del presupuesto?", "450000-(2*60000+5*12000*3+5*2000*3)", "Se resta la suma de los tres gastos al presupuesto.", ""),
        ("=", "{F} Si se agregan las tres actividades para las 5 personas, ¿cuánto cuestan?", "5*(4000+10000+8000)", "Se suman las tres actividades por persona y se multiplica por 5.", ""),
        ("abc", "{F} ¿Caben las tres actividades en el presupuesto?", "Sí, porque cuestan $110.000 y quedan $120.000", "No, porque el total superaría los $450.000", "No se puede saber sin cotizar el hostal", "110.000 es menor que el saldo de 120.000, por lo que caben."),
        ("abc", "{F} Uno de los niños tiene 4 años y el taller de cerámica de ejemplo exige tener 6 años o más. ¿Qué corresponde?", "Revisar la condición con el prestador y ofrecer otra actividad para ese niño, informando a la familia", "Incluirlo igual, sin avisar al prestador", "Quitar el taller para todos sin preguntar", "Las condiciones del prestador se respetan y se ofrece una alternativa."),
        ("abc", "{F} La familia pregunta si el Hostal Centro podría ser una opción más barata. ¿Qué respondes?", "Que es más barato, pero su acceso es solo por escalera y no cumple la necesidad de la persona mayor", "Que sí, porque la persona mayor puede aprender a subir", "Que no existe ninguna diferencia entre ambos", "Se informa con claridad por qué una opción más barata no cumple lo indispensable."),
        ("abc", "{F} La persona mayor dice que ella puede subir unos escalones. ¿Qué corresponde?", "Preguntarle cuántos y en qué condiciones, y confirmar con el hostal antes de cambiar de opción", "Cambiar de inmediato al hostal", "Ignorar lo que dijo", "La persona decide qué le acomoda, pero se confirma el dato antes de cambiar."),
    ],
    ctx=("abc", "{F} Al sumar todo, el programa queda en $440.000, muy cerca del presupuesto. ¿Qué corresponde?", "Informar que queda muy justo y explicar que cualquier gasto extra quedaría fuera", "Ocultar el saldo para no preocupar", "Agregar otra actividad igual", "El cliente debe saber que queda poco margen para decidir con información."),
    sc=[
        ("En Servicios de Turismo: ¿qué se resuelve primero, la necesidad o el precio?", "La necesidad, porque es indispensable", "Una opción barata que no cumple lo indispensable no sirve."),
        ("¿Cómo se calcula el saldo del presupuesto?", "Se resta lo ya elegido al presupuesto total", "El saldo indica qué se puede agregar."),
        ("¿Qué haces si una actividad tiene edad mínima?", "Reviso con el prestador y ofrezco una alternativa", "Se respetan las condiciones del prestador."),
    ],
    op=("Una familia de ejemplo de 4 personas (2 adultos y 2 jóvenes) pide un programa de 2 días y 1 noche con un presupuesto de $300.000 y una persona que necesita acceso sin escalones. Opciones: Cabaña Sol, sin escalones, $90.000 la noche; Hostal Luna, escalera, $60.000 la noche. Alimentación: $11.000 por persona por día. Actividad: paseo en bote a $12.000 por persona. Elige el alojamiento, calcula alojamiento, alimentación y actividad, el total y si cabe en el presupuesto.",
        "Alojamiento: Cabaña Sol, por el acceso sin escalones: 90.000. Alimentación: 4 × 2 × 11.000 = 88.000. Actividad: 4 × 12.000 = 48.000. Total: 226.000. Cabe: queda un saldo de 74.000.",
        ["elige el alojamiento por la necesidad y no por el precio", "calcula bien alojamiento, alimentación y actividad", "compara el total con el presupuesto"],
        ["elección, cálculos, total y saldo"],
        ["elegir el hostal por ser más barato", "multiplicar la alimentación solo por un día", "no calcular el saldo"],
        "Pregunta: «¿por qué descartaste el hostal?». Si no responde, repasa la necesidad de acceso."),
    reinforce="Anota tres necesidades que podría tener una persona al viajar y cómo las preguntarías con respeto.",
    extend="Explica con un ejemplo inventado por qué conviene dejar un margen en el presupuesto del cliente.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (de ejemplo, inventada). Programa «Fin de semana en Villa Brisa» para 8 personas, 3 días y 2 noches. Alojamiento: 2 cabañas a $50.000 por noche cada una. Alimentación: $10.000 por persona por día. "
     "Actividad: paseo en bote, $9.000 por persona. Bus privado: $120.000 en total. Margen de ejemplo de la agencia: 20 % sobre el costo total. "
     "El precio informado debe decir si incluye impuestos, según la norma vigente.")
build(
    O6, 4, F,
    use="Aprenderé a calcular el costo total, el precio de venta con un margen de ejemplo, el precio por persona y a comparar con un presupuesto, informando con claridad.",
    prior=["Sé calcular costos de alojamiento, alimentación y actividades.", "Sé calcular un porcentaje exacto.", "Sé dividir el total por la cantidad de personas."],
    explain=[
        "El costo total es la suma de todos los servicios del programa. El margen es la parte que la agencia agrega para cubrir sus gastos y obtener una ganancia; aquí se expresa como un porcentaje de ejemplo sobre el costo. El precio de venta es el costo total más el margen: si el margen es 20 %, el precio es el costo multiplicado por 120 y dividido por 100. El precio por persona se obtiene dividiendo el precio de venta por la cantidad de personas.",
        "Para ordenar el cálculo conviene hacer una tabla con alojamiento, alimentación, actividades y transporte, sumar, aplicar el margen y dividir. Al terminar se comprueba por otro camino, por ejemplo multiplicando el precio por persona por la cantidad de personas, que debe dar el precio de venta. El precio informado debe decir si incluye impuestos, según la norma vigente, y los porcentajes de este cuaderno son de ejemplo.",
        "Si el precio por persona supera el presupuesto del cliente, se ofrecen ajustes honestos, como cambiar un servicio o reducir una actividad, y no se esconden costos.",
    ],
    vocab=[("costo total", "suma de todos los servicios del programa"), ("margen", "parte del precio que la agencia agrega a los costos"), ("precio de venta", "costo total más el margen"), ("precio por persona", "precio de venta dividido por la cantidad de personas"), ("comprobación", "cálculo por otro camino para verificar un resultado")],
    worked=[
        ("Precio con margen", "Un programa de ejemplo cuesta $200.000 y la agencia aplica un margen del 10 %. ¿Cuál es el precio de venta?", ["200.000 × 110 ÷ 100 = 220.000.", "El margen suma 20.000."], "$220.000"),
        ("Precio por persona", "El precio de venta de un programa de ejemplo es $220.000 para 5 personas. ¿Cuál es el precio por persona?", ["Se divide el precio por la cantidad de personas.", "220.000 ÷ 5 = 44.000."], "$44.000"),
    ],
    mistakes=[("Aplicar el margen solo al alojamiento.", "El margen es sobre el costo total del programa; así el precio queda mal calculado.", "Suma todos los costos y recién después aplica el margen."),
              ("Dividir por las noches en vez de por las personas para obtener el precio por persona.", "El precio por persona depende de la cantidad de personas.", "Divide el precio de venta por las personas.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es el margen de una agencia?", "La parte que la agencia agrega a los costos para cubrir sus gastos y obtener ganancia", "El descuento que se da al cliente", "El impuesto de un servicio", "El margen se suma al costo; no es un descuento ni un impuesto."),
        ("abc", "En Servicios de Turismo: ¿qué es el precio de venta?", "El costo total más el margen", "Solo el costo del alojamiento", "El precio más bajo del mercado", "El precio de venta incluye todos los costos y el margen."),
        ("abc", "¿Para qué sirve una comprobación del cálculo?", "Para verificar el resultado por otro camino", "Para cambiar el resultado a gusto", "Para cobrar una comisión", "La comprobación detecta errores antes de informar el precio."),
        ("=", "{F} ¿Cuánto cuesta el alojamiento de las 2 cabañas por 2 noches?", "2*2*50000", "Se multiplican cabañas, noches y tarifa.", ""),
        ("=", "{F} ¿Cuánto cuesta la alimentación de las 8 personas durante los 3 días?", "8*3*10000", "Se multiplican personas, días y valor diario.", ""),
        ("=", "{F} ¿Cuánto cuesta el paseo en bote para las 8 personas?", "8*9000", "Se multiplica el valor por persona por 8.", ""),
        ("=", "{F} ¿Cuál es el costo total del programa?", "2*2*50000+8*3*10000+8*9000+120000", "Se suman alojamiento, alimentación, bote y bus.", ""),
        ("=", "{F} ¿Cuál es el precio de venta con el margen de ejemplo del 20 %?", "(2*2*50000+8*3*10000+8*9000+120000)*120//100", "Se multiplica el costo por 120 y se divide por 100.", ""),
        ("=", "{F} ¿Cuál es el precio por persona?", "(2*2*50000+8*3*10000+8*9000+120000)*120//100//8", "Se divide el precio de venta por 8 personas.", ""),
        ("=", "{F} Comprobación: si el precio por persona fuera $94.800, ¿cuánto suman 8 precios por persona?", "94800*8", "Multiplicar el precio por persona por 8 debe dar el precio de venta.", ""),
        ("abc", "{F} Una cliente tiene un presupuesto de $90.000 por persona. ¿Qué corresponde?", "Informar que el precio por persona es $94.800, algo mayor, y ofrecer ajustes honestos", "Decir que cuesta $90.000 y cobrar después la diferencia", "Eliminar el margen sin avisar", "El cliente debe conocer el precio real y las opciones de ajuste."),
        ("abc", "{F} Un compañero dice: «apliquemos el 20 % solo al bus». ¿Qué respondes?", "Que el margen se aplica al costo total del programa, no a un solo servicio", "Que tiene razón, porque el bus es lo más caro", "Que no se aplica margen en ningún caso", "La política de ejemplo aplica el margen sobre el costo total."),
        ("abc", "{F} El cliente pregunta si el precio incluye impuestos. ¿Qué corresponde?", "Informar con claridad si los incluye, según la norma vigente, y dejarlo por escrito", "Decir que sí, aunque no se haya revisado", "Decir que no importa", "La norma vigente exige informar con claridad; se confirma antes de responder."),
    ],
    ctx=("abc", "{F} Un cliente pide el precio final por persona, pero antes de enviarlo notas que olvidaste el bus. ¿Qué corresponde?", "Recalcular con el bus incluido, comprobar el resultado y enviar el precio correcto", "Enviar el precio sin el bus y cobrar la diferencia después", "Dividir el bus entre menos personas para que parezca barato", "Un precio incompleto engaña al cliente; se corrige antes de enviarlo."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se calcula un precio con un margen del 20 %?", "Se multiplica el costo por 120 y se divide por 100", "El margen se suma al costo total."),
        ("¿Cómo se obtiene el precio por persona?", "Se divide el precio de venta por la cantidad de personas", "Así se compara con el presupuesto del cliente."),
        ("¿Qué se informa sobre los impuestos?", "Si el precio los incluye o no, según la norma vigente", "El cliente debe conocer el precio real."),
    ],
    op=("Un programa de ejemplo para 5 personas, 2 días y 1 noche cuesta: alojamiento $70.000 la noche; alimentación $9.000 por persona por día; actividad $7.000 por persona; traslado $40.000 en total. La agencia aplica un margen de ejemplo del 20 %. Calcula el costo total, el precio de venta, el precio por persona y comprueba el resultado.",
        "Alojamiento: 70.000. Alimentación: 5 × 2 × 9.000 = 90.000. Actividad: 5 × 7.000 = 35.000. Traslado: 40.000. Costo total: 235.000. Precio de venta: 235.000 × 120 ÷ 100 = 282.000. Por persona: 282.000 ÷ 5 = 56.400. Comprobación: 56.400 × 5 = 282.000.",
        ["calcula bien el costo total", "aplica el margen sobre el costo total", "comprueba el resultado multiplicando por las personas"],
        ["cálculos, precio de venta, precio por persona y comprobación"],
        ["aplicar el margen solo a un servicio", "dividir por noches en vez de personas", "no comprobar el resultado"],
        "Pregunta: «¿cómo sabes que tu precio por persona es correcto?». Si no responde, repasa la comprobación."),
    reinforce="Inventa un programa de un día para dos personas, con tres costos, y calcula el costo por persona.",
    extend="Explica con un ejemplo inventado por qué se debe informar el precio completo desde el principio.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (de ejemplo, inventada). Dos propuestas del programa «Dos días en el valle» para 4 personas. Propuesta A: día 1, salida 8:00, traslado de 3 horas, llegada 11:00, almuerzo a las 12:00, museo a las 15:00, noche en cabaña autorizada con acceso sin escalones; "
     "día 2, paseo en bote autorizado a las 9:00, regreso. Precio $380.000 con inclusiones y exclusiones escritas. Propuesta B: día 1, salida 8:00, traslado de 3 horas, llegada a las 10:00; día 2, paseo en bote de un prestador sin autorización informada; precio $340.000 sin detalle de inclusiones; "
     "no informa el acceso de la cabaña. Lista de cotejo (1 punto cada una): horarios coherentes; prestadores autorizados; costos claros con inclusiones y exclusiones; accesibilidad informada; cuida el ambiente y el patrimonio (ambas usan senderos habilitados). "
     "Encuesta de un programa anterior a 8 pasajeros, con puntajes de 1 a 5: 5, 4, 4, 5, 3, 4, 3 y 4.")
build(
    O6, 5, F,
    use="Aprenderé a comparar propuestas de programas con una lista de cotejo, a verificar horarios, autorizaciones y costos, y a mejorar el programa con las opiniones de los pasajeros.",
    prior=["Sé calcular costos y precios por persona.", "Sé calcular promedios.", "Sé qué es un prestador autorizado."],
    explain=[
        "Comparar alternativas de programa es evaluar cada una con los mismos criterios. La lista de cotejo da un punto por criterio cumplido: horarios coherentes, prestadores autorizados, costos claros con inclusiones y exclusiones, accesibilidad informada, y cuidado del ambiente y el patrimonio. Una propuesta más barata que no cumple los criterios no es mejor: puede traer riesgos o costos ocultos.",
        "Para verificar la coherencia de los horarios se suman los tiempos: si la salida es a las 7:30 y el traslado dura 2 horas, la llegada es a las 9:30; una llegada a las 8:30 sería un error. También se verifica que los prestadores tengan autorización informada y que el precio detalle qué incluye y qué excluye.",
        "Después del programa, la encuesta de satisfacción mide la calidad. El promedio se obtiene sumando los puntajes y dividiendo por la cantidad de respuestas. Los comentarios sirven para mejorar los próximos programas, y la información de los pasajeros se usa solo con su permiso.",
    ],
    vocab=[("coherencia de horarios", "que los tiempos de salida, traslado y llegada calcen"), ("lista de cotejo", "lista de criterios que se revisan uno a uno"), ("autorización informada", "autorización vigente que el prestador muestra o informa"), ("encuesta de satisfacción", "preguntas para saber qué tan conforme quedó el pasajero"), ("promedio", "suma de puntajes dividida por la cantidad de respuestas")],
    worked=[
        ("Revisar un horario", "Un programa de ejemplo sale a las 9:00 con traslado de 2 horas y dice «llegada a las 10:30». ¿Es coherente?", ["9:00 más 2 horas son las 11:00.", "Llegar a las 10:30 no es coherente: hay un error."], "No es coherente: la llegada es a las 11:00"),
        ("Promedio de una encuesta", "Cuatro pasajeros de ejemplo dan 4, 5, 3 y 4. ¿Cuál es el promedio?", ["4 + 5 + 3 + 4 = 16.", "16 ÷ 4 = 4."], "4"),
    ],
    mistakes=[("Elegir la propuesta más barata sin revisar sus criterios.", "Puede traer prestadores sin autorización o costos ocultos.", "Aplica la lista de cotejo antes de comparar precios."),
              ("Ignorar los comentarios bajos de la encuesta.", "Pueden mostrar un problema real del programa.", "Lee los comentarios y evalúa mejoras.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es la coherencia de horarios?", "Que los tiempos de salida, traslado y llegada calcen entre sí", "Que todas las actividades empiecen a la misma hora", "Que el programa tenga muchas actividades", "La coherencia exige que los tiempos se correspondan."),
        ("abc", "En Servicios de Turismo: ¿qué es una autorización informada?", "Una autorización vigente que el prestador muestra o informa", "Una promesa verbal del prestador", "Un permiso que el cliente da a la agencia", "Informada significa que se puede confirmar, no basta con decirlo."),
        ("abc", "¿Por qué una propuesta más barata no siempre es mejor?", "Porque puede no cumplir criterios importantes y traer riesgos o costos ocultos", "Porque el precio no importa", "Porque las baratas siempre son malas", "Se evalúa con criterios antes de comparar el precio."),
        ("=", "{F} Con salida a las 8:00 y traslado de 3 horas, ¿a qué hora llega? Escribe solo la hora, sin los minutos.", "8+3", "Se suma la duración del traslado a la hora de salida.", " h"),
        ("abc", "{F} ¿Qué error de horarios tiene la propuesta B?", "Dice que llega a las 10:00 con salida a las 8:00 y traslado de 3 horas", "Dice que sale a las 8:00", "Dice que el paseo es el día 2", "El traslado de 3 horas desde las 8:00 llega a las 11:00, no a las 10:00."),
        ("abc", "{F} ¿Qué criterio incumple B respecto del paseo en bote?", "Prestadores autorizados, porque el prestador no tiene autorización informada", "Costos claros", "Horarios coherentes", "El prestador del bote no muestra autorización, que es un criterio de la lista."),
        ("=", "{F} A cumple los cinco criterios y B solo cumple el del cuidado del ambiente. ¿Cuántos puntos más tiene A que B?", "5-1", "Se resta el puntaje de B al de A.", " puntos"),
        ("=", "{F} ¿Cuántos pesos más caro es A que B?", "380000-340000", "Se resta el precio de B al de A.", ""),
        ("=", "{F} ¿Cuántos pesos por persona cuesta la propuesta A?", "380000//4", "Se divide el precio por las 4 personas.", ""),
        ("abc", "{F} ¿Qué recomiendas al cliente?", "La propuesta A, porque cumple los criterios, aunque cueste más", "La propuesta B, porque es más barata", "Ninguna, sin explicar por qué", "A cumple la lista de cotejo; B tiene errores y riesgos."),
        ("=", "{F} ¿Cuál es el promedio de la encuesta de 8 pasajeros?", "(5+4+4+5+3+4+3+4)//8", "Se suman los puntajes y se divide por 8.", ""),
        ("abc", "{F} Dos pasajeros dieron 3 y comentaron que el almuerzo fue tarde. ¿Qué corresponde?", "Revisar el horario del almuerzo y ajustarlo en los próximos programas", "Descartar esas encuestas", "Culpar al guía sin revisar", "Los comentarios muestran dónde mejorar el programa."),
        ("abc", "{F} El prestador de la propuesta B pide un anticipo ahora «para asegurar el precio». ¿Qué corresponde?", "Pedirle primero su autorización informada y el detalle por escrito antes de cualquier pago", "Pagar el anticipo para no perder el precio", "Recomendar la propuesta B al cliente", "No se paga ni se recomienda a un prestador sin autorización confirmada."),
    ],
    ctx=("abc", "{F} El cliente pide que le expliques por qué la propuesta A cuesta más. ¿Qué respondes?", "Que A incluye prestadores autorizados, horarios coherentes, inclusiones y exclusiones escritas y accesibilidad informada", "Que es más cara porque los prestadores caros son siempre mejores", "Que se puede bajar el precio quitando la autorización", "Explicar con evidencia ayuda a decidir con información."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se comprueba la coherencia de horarios?", "Sumando la duración a la hora de salida", "La hora de llegada debe coincidir con el cálculo."),
        ("¿Qué haces con un prestador sin autorización informada?", "No lo incluyo hasta confirmar su autorización", "La norma vigente exige prestadores autorizados."),
        ("¿Cómo se obtiene el promedio de una encuesta?", "Sumando los puntajes y dividiendo por la cantidad de respuestas", "Resume la satisfacción en un valor."),
    ],
    op=("Compara dos propuestas de ejemplo para 5 personas. Propuesta M: salida 9:00, traslado de 2 horas, llegada a las 11:00, prestadores autorizados, precio $300.000 con inclusiones y exclusiones, accesibilidad informada. Propuesta N: salida 9:00, traslado de 2 horas, llegada a las 10:00, un prestador sin autorización, precio $250.000 sin detalle, accesibilidad no informada. Ambas usan senderos habilitados. Aplica la lista de cotejo de la ficha, da el puntaje de cada una, calcula el precio por persona de M y recomienda.",
        "M: horarios coherentes, prestadores autorizados, costos claros, accesibilidad informada y cuidado del ambiente: 5 puntos. N: horarios incoherentes (llegada a las 11:00), prestador sin autorización, costos sin detalle y accesibilidad no informada; solo cumple el cuidado del ambiente: 1 punto. Precio por persona de M: 300.000 ÷ 5 = 60.000. Recomiendo M, porque cumple los criterios.",
        ["aplica los cinco criterios a ambas propuestas", "calcula el precio por persona de M", "recomienda con evidencia y no solo por el precio"],
        ["puntaje de cada propuesta, cálculo y recomendación"],
        ["no detectar el error de horario de N", "recomendar solo por el menor precio", "olvidar la autorización del prestador"],
        "Pregunta: «¿qué error de horario tiene N?». Si no responde, pídele que sume el traslado a la salida."),
    reinforce="Compara dos opciones de viaje que conozcas con tres criterios propios.",
    extend="Explica con un ejemplo inventado por qué una propuesta barata con prestadores no autorizados puede salir cara.",
)
