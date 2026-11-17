"""Hotelería TP 3.º y 4.º medio: OAE-05 (centro de negocios con amabilidad, discreción e inglés básico) y OAE-06 (cierre de cuenta, monedas, documentación comercial y normativa de consumo). Todo en papel: tarifas, folios, tipos de cambio y cajas inventados y rotulados «de ejemplo»; sin cifras tributarias."""
from __future__ import annotations

from tp_seho_common import build

O5 = "TP-SEHO-3y4-OAE-05"
O6 = "TP-SEHO-3y4-OAE-06"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: no reemplaza la práctica con un instructor ni la norma vigente."

# ============================================================ OAE-05, clase 1
F = ("Ficha 20 (centro de negocios de ejemplo, inventado). «Hotel Marea de Ejemplo»: centro de negocios abierto de 08:00 a 20:00. Servicios y tarifas de ejemplo: impresión o fotocopia blanco y negro, $100 por hoja; a color, $300 por hoja; escaneo, $200 por documento; "
     "sala de reuniones para hasta 8 personas, $15.000 por hora; internet en los equipos del centro, sin costo para huéspedes. Reglas: los documentos de los huéspedes son confidenciales; no se leen ni se comentan, no se guardan copias y, al terminar, se cierra la sesión y se borran los archivos del huésped del equipo, según el protocolo.")
build(
    O5, 1, F,
    use="Aprenderé qué ofrece un centro de negocios, cómo se atiende con amabilidad y discreción, y qué reglas de confidencialidad y ergonomía se aplican.",
    prior=["Sé calcular precios por unidad.", "Conozco la confidencialidad de datos de huéspedes.", "Sé leer una ficha de tarifas."],
    explain=[
        "Un centro de negocios es un espacio del hotel con servicios de oficina para los huéspedes: impresión, fotocopias, escaneo, internet y salas de reuniones. Quien lo atiende ayuda con amabilidad, explica las tarifas antes de cobrar y se asegura de que el huésped sepa cómo usar el servicio.",
        "La discreción es no leer, comentar ni conservar la información que el huésped trae. Un documento puede tener datos personales o de su empresa. Por eso se sigue el protocolo: se entrega lo impreso solo al huésped, no se guardan copias y, al terminar, se cierra la sesión y se borran los archivos del equipo. Nunca se deja un documento a la vista de otras personas.",
        "El precio de un servicio se calcula multiplicando la tarifa unitaria por la cantidad. Quien pasa horas frente a una pantalla cuida su postura, hace pausas breves y regulares y ajusta la pantalla a la altura de los ojos." + LIM,
    ],
    vocab=[("centro de negocios", "espacio del hotel con servicios de oficina para los huéspedes"), ("discreción", "no leer, comentar ni conservar la información que trae el huésped"), ("confidencial", "que no debe conocer ni difundir nadie sin autorización"), ("protocolo", "conjunto de pasos acordados para realizar un servicio"), ("cerrar sesión", "terminar el uso del equipo para que otra persona no acceda a la información")],
    worked=[
        ("Calcular una impresión", "Una hoja en blanco y negro cuesta $80 en un centro de ejemplo y un huésped imprime 15 hojas. ¿Cuánto paga?", ["Total = tarifa × cantidad.", "80 × 15 = 1.200."], "$1.200"),
        ("Aplicar la discreción", "Un huésped de ejemplo deja olvidadas en la impresora dos hojas con su contrato. ¿Qué haces?", ["No las lees ni las comentas.", "Las entregas solo al huésped, o las guardas en un sobre cerrado en recepción."], "Entregarlas solo al huésped, sin leerlas"),
    ],
    mistakes=[("Leer en voz alta el título de un documento que un huésped está imprimiendo, para «ayudarlo» a ordenarlo.", "Se invade su confidencialidad y otras personas pueden escucharlo.", "Atiende sin leer el contenido y pregunta solo lo necesario, en voz baja."),
              ("Dejar los archivos de un huésped en el computador compartido «por si vuelve».", "Otra persona podría ver o llevarse información confidencial.", "Cierra la sesión y borra los archivos al terminar, según el protocolo.")],
    T=[
        ("abc", "En Hotelería: ¿qué es el centro de negocios?", "Un espacio del hotel con servicios de oficina para los huéspedes", "La bodega de insumos del hotel", "El lugar donde duermen los huéspedes", "El centro de negocios ofrece impresión, escaneo, internet y salas de reuniones."),
        ("abc", "{F} ¿Hasta qué hora atiende el centro de negocios?", "Hasta las 20:00", "Hasta las 18:00", "Hasta las 22:00", "La ficha fija el horario de 08:00 a 20:00."),
        ("abc", "{F} ¿Cuánto cuesta una hoja impresa a color?", "$300", "$100", "$200", "La ficha fija $300 por hoja a color; $100 es blanco y negro y $200 el escaneo."),
        ("=", "{F} Un huésped imprime 25 hojas en blanco y negro. ¿Cuánto paga?", "100*25", "Se multiplica la tarifa por hoja por la cantidad de hojas.", " pesos"),
        ("=", "{F} Un huésped imprime 10 hojas a color. ¿Cuánto paga?", "300*10", "Se multiplica la tarifa por hoja a color por la cantidad.", " pesos"),
        ("abc", "{F} Un huésped imprime un contrato. ¿Qué haces con su contenido?", "No lo leo ni lo comento, y lo entrego solo a él", "Lo leo para ayudarlo a ordenarlo", "Lo comento con mi compañero", "La ficha manda confidencialidad: los documentos no se leen ni se comentan."),
        ("abc", "{F} Un huésped termina de usar el computador del centro y se va. ¿Qué corresponde hacer?", "Cerrar su sesión y borrar sus archivos del equipo según el protocolo", "Dejar sus archivos para el siguiente huésped", "Guardar una copia por seguridad", "Los archivos del huésped no se conservan; se borran al terminar."),
        ("=", "{F} Una empresa de ejemplo usa la sala de reuniones 3 horas. ¿Cuánto paga?", "15000*3", "Se multiplica el valor por hora por las horas de uso.", " pesos"),
        ("abc", "{F} Alguien que no es huésped pide usar la sala de reuniones. ¿Qué haces?", "Consultar a la jefatura si el hotel atiende a visitantes y qué tarifa corresponde", "Cobrar un precio inventado", "Dejarlo entrar sin preguntar", "Lo que no está en la ficha se consulta; no se inventan precios."),
        ("abc", "{F} Un huésped fotocopió su documento de identidad y se fue dejando el original sobre la máquina. ¿Qué haces?", "Guardarlo en un sobre cerrado en recepción, sin sacar otra copia, y entregárselo solo a él", "Dejarlo sobre la mesa a la vista, para que lo encuentre al volver", "Sacar una copia extra por si la necesita después", "Un documento de identidad es un dato personal: no se copia ni se deja a la vista."),
        ("abc", "Quien atiende el centro lleva 3 horas sentado frente al computador. ¿Qué cuidado corresponde?", "Hacer una pausa breve y ajustar la postura y la altura de la pantalla", "Seguir sin pausas para no atrasarse", "Cruzar las piernas y acercarse a la pantalla", "La ergonomía pide pausas regulares y una buena postura."),
        ("abc", "Un huésped se muestra molesto porque la impresora tarda. ¿Qué respuesta es adecuada?", "Pedir disculpas con calma y explicar cuánto demorará", "Decirle que tenga paciencia y mirar otra cosa", "Culpar a otro compañero", "Un trato amable y claro baja la tensión y muestra respeto."),
        ("=", "{F} Una sala se reserva de 09:00 a 12:00 y de 14:00 a 16:00. ¿Cuánto cuesta en total?", "15000*((12-9)+(16-14))", "Se suman las horas de ambos bloques y se multiplican por el valor por hora.", " pesos"),
    ],
    ctx=("abc", "{F} A las 19:50 llega un huésped que necesita imprimir 20 hojas en blanco y negro y el centro cierra a las 20:00. ¿Qué haces?", "Atenderlo con amabilidad, informar el costo antes y, si no alcanza el tiempo, ofrecer una alternativa como atenderlo a primera hora", "Decirle que ya cerraron", "Imprimir sin decir cuánto cuesta", "Se atiende con amabilidad, se informa el costo y se ofrece una alternativa clara."),
    sc=[
        ("En Hotelería: ¿qué es la discreción en el centro de negocios?", "No leer ni comentar lo que trae el huésped", "Los documentos del huésped son confidenciales."),
        ("¿Cómo se calcula el cobro de varias hojas?", "Tarifa por hoja multiplicada por la cantidad", "El total depende de la cantidad de hojas."),
        ("¿Qué haces con los archivos del huésped al terminar?", "Cierro la sesión y los borro", "Así otra persona no puede acceder a ellos."),
    ],
    op=("Centro de negocios de ejemplo: impresión blanco y negro $90 por hoja, color $250, escaneo $150 por documento, sala de reuniones $12.000 por hora. Un huésped pide: 30 hojas en blanco y negro, 6 hojas a color, 4 escaneos y la sala por 2 horas. "
        "Calcula cuánto debe pagar, y escribe tres frases de lo que dirías y harías para atenderlo con amabilidad y discreción.",
        "Blanco y negro: 30 × 90 = 2.700. Color: 6 × 250 = 1.500. Escaneos: 4 × 150 = 600. Sala: 2 × 12.000 = 24.000. Total: 28.800 pesos. Frases: «Buenas tardes, ¿en qué puedo ayudarle?»; «Son $28.800 en total, ¿le parece bien?»; no leo sus documentos y al terminar cierro la sesión y borro sus archivos del equipo.",
        ["calcula bien cada servicio y el total", "informa el costo antes de cobrar", "incluye discreción y cierre de sesión"],
        ["hoja con los cálculos y tres frases"],
        ["sumar mal los servicios", "no informar el total", "olvidar la confidencialidad"],
        "Pregunta: «¿qué haces con los archivos al terminar?». Si no menciona borrarlos y cerrar sesión, repasa el protocolo."),
    reinforce="Escribe cinco reglas de discreción para quien atiende un centro de negocios.",
    extend="Explica por qué un huésped confía más en un hotel que cuida sus documentos.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 21 (documentos y frases de ejemplo). Hoja de solicitud de servicio: fecha, nombre o habitación del huésped, servicio pedido, cantidad, tarifa, total y firma de quien atiende. Registro de uso de la sala: hora de inicio, hora de término y encargado. "
     "Frases en inglés: Copy / Print / Scan = Copiar / Imprimir / Escanear. How many copies? = ¿Cuántas copias? Black and white or color? = ¿Blanco y negro o a color? The meeting room is available = La sala de reuniones está disponible. It costs fifteen thousand pesos per hour = Cuesta quince mil pesos por hora. Please wait a moment = Espere un momento, por favor.")
build(
    O5, 2, F,
    use="Aprenderé los documentos del centro de negocios y las frases básicas en inglés para atender, informar tarifas y pedir datos con cortesía.",
    prior=["Conozco la discreción y las tarifas.", "Sé multiplicar.", "Sé leer frases cortas en inglés."],
    explain=[
        "El centro de negocios usa dos documentos principales. La hoja de solicitud de servicio registra qué pidió el huésped, la cantidad, la tarifa y el total, y la firma de quien atendió. El registro de uso de la sala anota quién la ocupó y entre qué horas, para evitar dobles reservas y calcular el cobro.",
        "Con un huésped extranjero se usan frases cortas y claras en inglés básico. Copy, print y scan son los servicios de copiar, imprimir y escanear. «How many copies?» pregunta la cantidad y «Black and white or color?» pregunta el tipo de impresión. Se habla despacio, con una sonrisa, y se confirma lo entendido.",
        "Siempre se informa el precio antes de cobrar. Si no entiendes algo, usas «Please wait a moment» y consultas. No se inventan traducciones: si falta una palabra, se muestra un papel con el precio escrito en números." + LIM,
    ],
    vocab=[("hoja de solicitud de servicio", "documento que registra qué servicio pidió el huésped, la cantidad y el total"), ("registro de uso de la sala", "anotación de quién ocupó la sala y en qué horario"), ("copy", "copiar, en inglés"), ("print", "imprimir, en inglés"), ("scan", "escanear, en inglés"), ("How many copies?", "¿Cuántas copias?")],
    worked=[
        ("Traducir una pregunta", "¿Cómo preguntas «¿Cuántas copias?» a un huésped extranjero?", ["Se busca la frase en la ficha.", "La pregunta de cantidad es «How many copies?»."], "«How many copies?»"),
        ("Completar una solicitud", "Un huésped de ejemplo pide 20 hojas a $100 cada una. ¿Qué total se anota en la hoja de solicitud?", ["Total = tarifa × cantidad.", "100 × 20 = 2.000."], "$2.000"),
    ],
    mistakes=[("No anotar en el registro de la sala la hora de término de una reunión.", "No se sabe cuánto cobrar ni cuándo queda libre para otro huésped.", "Anota hora de inicio y de término en cada uso."),
              ("Responder en español muy rápido a un huésped que no lo entiende.", "No logra comunicarse y puede sentirse excluido.", "Habla despacio, usa frases simples en inglés y apoya con un papel escrito.")],
    T=[
        ("abc", "En Hotelería: ¿para qué sirve el registro de uso de la sala?", "Para anotar quién la ocupó y en qué horario", "Para guardar los documentos del huésped", "Para fijar las tarifas del hotel", "El registro evita dobles reservas y permite calcular el cobro."),
        ("abc", "{F} ¿Qué significa «Scan»?", "Escanear", "Imprimir", "Copiar", "La ficha asocia scan con escanear; print es imprimir y copy es copiar."),
        ("abc", "{F} ¿Cómo se dice «¿Cuántas copias?» en inglés?", "How many copies?", "Black and white or color?", "Please wait a moment", "La ficha indica esa frase para preguntar la cantidad."),
        ("abc", "{F} ¿Qué significa «Black and white or color?»", "¿Blanco y negro o a color?", "¿Cuántas copias?", "La sala está disponible", "Es la pregunta para elegir el tipo de impresión."),
        ("=", "{F} Un huésped pide 12 copias en blanco y negro a $100 cada una. ¿Cuál es el total que se anota en la hoja de solicitud?", "100*12", "Se multiplica la tarifa por la cantidad solicitada.", " pesos"),
        ("abc", "{F} ¿Qué dato lleva la hoja de solicitud además del servicio pedido y la cantidad?", "La tarifa, el total y la firma de quien atiende", "El número de teléfono de la familia", "La contraseña del huésped", "La ficha lista tarifa, total y firma; la contraseña nunca se registra."),
        ("abc", "{F} Una huésped extranjera pregunta por la sala de reuniones. ¿Qué frase usas para decirle que está libre?", "The meeting room is available", "Please wait a moment", "Scan", "Esa frase informa la disponibilidad de la sala."),
        ("=", "{F} Una sala se usó de 15:00 a 17:00. ¿Cuánto se cobra con la tarifa de ejemplo de $15.000 por hora que dice la ficha?", "15000*(17-15)", "Se multiplican las horas de uso por el valor por hora.", " pesos"),
        ("abc", "{F} Un huésped extranjero pregunta algo que no entiendes. ¿Qué dices?", "Please wait a moment, y consulto", "Nada, y sigo trabajando", "Que no hablas inglés y que vuelva otro día", "La frase es cortés y permite buscar ayuda."),
        ("abc", "{F} Quieres informar el precio a un huésped que no entiende español. ¿Qué haces?", "Mostrarle un papel con el precio escrito en números y decir la frase en inglés", "Gritar el precio en español", "No decirle el precio", "Un papel con números ayuda a comunicar sin errores."),
        ("=", "{F} En un día se registraron 7 solicitudes de servicio y 3 son escaneos. ¿Cuántas no son escaneos?", "7-3", "Al total de solicitudes se le restan los escaneos.", " solicitudes"),
        ("abc", "Un huésped pide que le des su contraseña de acceso a un equipo para probarlo después de que él se va. ¿Qué respondes?", "Que las claves personales no se guardan ni se entregan", "Que sí, para ayudarlo", "Que mejor la anotes en la hoja de solicitud", "Las claves son datos privados que nunca se registran."),
        ("abc", "{F} Dos huéspedes quieren la sala a las 10:00. En el registro, la sala figura ocupada por el primero. ¿Qué haces?", "Informar al segundo que no está disponible y ofrecerle otro horario", "Dársela a los dos a la vez", "Cobrar solo al segundo", "El registro evita doble uso; se ofrece una alternativa."),
    ],
    ctx=("abc", "{F} Una huésped extranjera dice: «I need to print twenty pages, black and white». La tarifa de ejemplo es $100 por hoja en blanco y negro. ¿Cuál es la respuesta adecuada?", "«Sure. Twenty pages in black and white. It costs two thousand pesos. Please wait a moment.»", "«No hablo inglés», y se va a otro lugar", "Imprimir sin confirmar nada", "Se confirma la cantidad y el tipo, se informa el costo y se pide un momento con cortesía."),
    sc=[
        ("En Hotelería: ¿cómo se dice «imprimir» en inglés?", "Print", "Es la palabra del servicio de impresión."),
        ("¿Qué documento registra qué pidió el huésped y cuánto cuesta?", "La hoja de solicitud de servicio", "Allí se anotan servicio, cantidad, tarifa y total."),
        ("¿Qué se informa siempre antes de cobrar?", "El precio", "El huésped debe saber cuánto pagará."),
    ],
    op=("Un huésped extranjero llega al centro de negocios de ejemplo y quiere escanear 3 documentos, a $200 cada uno, e imprimir 10 hojas a color, a $300 cada una. "
        "Escribe: tres frases en inglés de la ficha (de tu elección) para atenderlo, el total que anotarías en la hoja de solicitud y qué otros datos llevaría esa hoja.",
        "Frases: «Scan», «How many copies?» y «Please wait a moment». Total: 3 × 200 = 600 y 10 × 300 = 3.000; total 3.600 pesos. La hoja llevaría fecha, nombre o habitación, servicio, cantidad, tarifa y firma de quien atiende.",
        ["usa tres frases correctas de la ficha", "calcula el total", "nombra los datos de la hoja de solicitud"],
        ["hoja con las tres frases, el total y los datos de la hoja"],
        ["inventar frases en inglés que no están en la ficha", "olvidar uno de los servicios en el total", "olvidar la firma"],
        "Pregunta: «¿cómo dices ¿cuántas copias? en inglés?». Si no responde 'How many copies?', repasa la ficha."),
    reinforce="Escribe en una tabla las seis frases en inglés de la ficha con su significado en español.",
    extend="Explica por qué mostrar el precio escrito en números ayuda cuando hay una barrera de idioma.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 22 (caso de ejemplo, inventado). Son las 19:30 y el centro de negocios cierra a las 20:00. Llega un huésped que necesita imprimir 40 hojas en blanco y negro y 10 a color desde un pendrive (una memoria portátil) que trae también fotos personales y otros archivos de su empresa. "
     "Tarifas de ejemplo: blanco y negro $100 por hoja, color $300. La impresora de ejemplo imprime 10 hojas por minuto. El huésped es extranjero y habla inglés básico. Una de las hojas tiene datos de una cuenta bancaria.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de atención en el centro de negocios: tiempo disponible, costo, discreción con documentos sensibles y comunicación en inglés básico.",
    prior=["Conozco las tarifas y la discreción.", "Conozco frases en inglés básico.", "Sé calcular tiempos y costos."],
    explain=[
        "Para analizar un caso se leen los datos, se calcula el tiempo y el costo, y se revisan los riesgos. El tiempo de impresión se calcula dividiendo las hojas por las hojas que imprime la máquina por minuto. El costo es la suma de cada tipo de hoja por su tarifa. Si el tiempo disponible alcanza, se atiende; si no, se informa con honestidad y se ofrece una alternativa.",
        "Un pendrive puede traer archivos que no tienen relación con lo que el huésped quiere imprimir. Quien atiende no los abre ni los mira: pide al huésped que elija su archivo y lo ayuda a seleccionarlo. Si una hoja contiene datos sensibles, como los de una cuenta bancaria, no se lee ni se comenta, y se entrega solo al huésped.",
        "Con un huésped extranjero se usan frases cortas en inglés y se confirma lo entendido. Siempre se informa el total antes de imprimir." + LIM,
    ],
    vocab=[("pendrive", "memoria portátil que guarda archivos"), ("dato sensible", "dato muy privado cuyo mal uso puede causar daño, como los de una cuenta bancaria"), ("ritmo de impresión", "hojas que la impresora imprime por minuto"), ("tiempo disponible", "minutos que quedan antes del cierre"), ("alternativa", "otra opción cuando no se puede cumplir lo pedido")],
    worked=[
        ("Calcular el tiempo de impresión", "Una impresora de ejemplo imprime 8 hojas por minuto y hay que imprimir 40 hojas. ¿Cuántos minutos demora?", ["Tiempo = hojas ÷ hojas por minuto.", "40 ÷ 8 = 5."], "5 minutos"),
        ("Mirar archivos ajenos", "Un huésped de ejemplo entrega un pendrive con muchas fotos y pide imprimir un solo documento. ¿Qué haces?", ["No abres las fotos.", "Le pides que elija su documento."], "Pedirle que elija su documento sin mirar sus fotos"),
    ],
    mistakes=[("Abrir las fotos del pendrive «para encontrar el archivo más rápido».", "Se invade su privacidad sin necesidad.", "Pide al huésped que indique el archivo o que lo seleccione él."),
              ("Comentar con el compañero los datos bancarios que aparecieron en una hoja.", "Son datos sensibles y confidenciales; comentarlos puede perjudicar al huésped.", "No los comentes ni los copies, y entrega la hoja solo al huésped.")],
    T=[
        ("abc", "En Hotelería: ¿qué es un dato sensible?", "Un dato muy privado cuyo mal uso puede causar daño", "Un dato que está escrito con letra pequeña", "El precio de una impresión", "Los datos bancarios son sensibles; un precio no lo es."),
        ("=", "{F} ¿Cuántas hojas en total debe imprimir el huésped?", "40+10", "Se suman las hojas en blanco y negro y las de color.", " hojas"),
        ("=", "{F} ¿Cuántos minutos demora la impresión de todas las hojas?", "(40+10)//10", "Se dividen las hojas por las que imprime la máquina por minuto.", " minutos"),
        ("=", "{F} Son las 19:30. ¿Cuántos minutos faltan para el cierre?", "20*60-(19*60+30)", "Se restan a la hora de cierre, en minutos, los minutos transcurridos hasta las 19:30.", " minutos"),
        ("abc", "{F} ¿Alcanza el tiempo para imprimir todo antes del cierre?", "Sí: la impresión demora 5 minutos y quedan 30", "No: la impresión demora más de 30 minutos", "No se puede saber", "Con 5 minutos de impresión y 30 disponibles, el tiempo alcanza."),
        ("=", "{F} ¿Cuánto debe pagar el huésped por las hojas en blanco y negro y a color?", "40*100+10*300", "Se calcula cada tipo de hoja por su tarifa y se suman.", " pesos"),
        ("abc", "{F} El pendrive trae fotos personales. ¿Qué haces?", "No abrirlas y pedirle que elija el archivo", "Abrirlas para encontrar el archivo", "Copiarlas por si las necesita", "Las fotos son privadas y no se miran sin necesidad."),
        ("abc", "{F} Una hoja impresa muestra los datos de una cuenta bancaria del huésped. ¿Qué haces?", "No leerla ni comentarla, y entregarla solo a él", "Fotografiarla por seguridad", "Dejarla en la bandeja para que él la retire", "Los datos sensibles se manejan con máxima discreción."),
        ("abc", "{F} ¿Qué frase en inglés usas para preguntar el tipo de impresión?", "Black and white or color?", "How are you?", "Where is the bus?", "Esa frase pregunta si imprimirá en blanco y negro o a color."),
        ("abc", "{F} Si la impresión tardara 40 minutos, con 30 disponibles, ¿qué se haría?", "Informar con honestidad y ofrecer terminar a primera hora o imprimir una parte", "Prometer que alcanzará", "Imprimir todo sin decir nada", "Se informa la limitación y se ofrece una alternativa."),
        ("abc", "{F} Un compañero propone guardar en el computador una copia del archivo del huésped para atenderlo más rápido la próxima vez. ¿Qué respondes?", "Que no, porque no se conservan archivos de los huéspedes", "Que sí, si la carpeta tiene su nombre", "Que sí, mientras sea un archivo pequeño", "Guardar archivos de huéspedes contradice el protocolo de confidencialidad."),
        ("=", "{F} Después de pagar con un billete de $20.000, ¿cuánto vuelto recibe el huésped? (el total se calcula con las tarifas de la ficha)", "20000-(40*100+10*300)", "Al billete se le resta el total de las hojas en blanco y negro y a color.", " pesos"),
        ("abc", "{F} Antes de imprimir, ¿qué corresponde informar al huésped?", "El total que pagará", "El precio de su habitación", "Cuántos huéspedes hay en el hotel", "Se informa el costo para que decida con datos completos."),
    ],
    ctx=("abc", "{F} Terminada la impresión, el huésped se va con prisa y olvida su pendrive en el computador. ¿Qué haces?", "Guardarlo en un sobre cerrado en recepción, anotar la novedad y entregarlo solo a él", "Mirar su contenido para saber de quién es", "Conservarlo en el escritorio sin registro", "Se resguarda sin abrirlo y se registra para devolverlo al dueño."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el tiempo de impresión?", "Dividiendo las hojas por las que imprime la máquina por minuto", "Así se compara con el tiempo disponible."),
        ("¿Qué haces con las fotos de un pendrive ajeno?", "No las abro", "Son privadas y no se necesitan para atender."),
        ("¿Qué haces si no alcanza el tiempo?", "Informo y ofrezco una alternativa", "Se actúa con honestidad y se ofrece una solución."),
    ],
    op=("Caso de ejemplo. Son las 19:45 y el centro cierra a las 20:00. Un huésped pide imprimir 90 hojas en blanco y negro (a $100 cada una) con una impresora de 10 hojas por minuto. El archivo viene en un pendrive que además contiene fotos de su familia. "
        "Calcula el tiempo y el costo, decide si alcanza, y escribe tres frases de lo que dirías y harías con respeto y discreción.",
        "Tiempo: 90 ÷ 10 = 9 minutos; quedan 15 minutos, así que alcanza. Costo: 90 × 100 = 9.000. Frases: «Son $9.000, ¿le parece bien?»; «Por favor elija su archivo, yo no miraré lo demás»; al terminar cierro la sesión y borro el archivo del equipo.",
        ["calcula tiempo y costo", "decide con los datos", "protege la privacidad de las fotos"],
        ["hoja con los cálculos, la decisión y tres frases"],
        ["abrir las fotos", "olvidar informar el costo", "no cerrar sesión"],
        "Pregunta: «¿cómo encuentras el archivo sin ver las fotos?». Debe decir que el huésped lo elige."),
    reinforce="Inventa un caso de un huésped con un pendrive y escribe qué haces y qué no haces con sus archivos.",
    extend="Explica por qué avisar con anticipación que no alcanza el tiempo es mejor que prometer algo imposible.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 23 (solicitudes del día en el centro de negocios, de ejemplo). A: 30 hojas blanco y negro. B: 12 hojas a color. C: sala de reuniones por 2 horas. D: 6 escaneos. E: 20 hojas blanco y negro y 5 a color. "
     "Tarifas de ejemplo: blanco y negro $100 por hoja; color $300; escaneo $200; sala $15.000 por hora. En la caja del centro hay $41.300 al cierre.")
build(
    O5, 4, F,
    use="Aprenderé a calcular el cobro de cada solicitud, sumar el día y comprobar que la caja cuadra con el registro, con orden y honestidad.",
    prior=["Conozco las tarifas.", "Sé multiplicar y sumar.", "Conozco la hoja de solicitud."],
    explain=[
        "Al terminar el día se revisa que lo registrado coincida con el dinero recibido. Para cada solicitud se calcula el total multiplicando la tarifa por la cantidad. Después se suman los totales de todas las solicitudes y se compara con el dinero que hay en la caja. A esta comprobación se le llama cuadre de caja.",
        "Si el dinero coincide con el registro, la caja cuadra. Si hay diferencia, se revisa primero el cálculo y los registros, y luego se informa a la jefatura, sin ocultarla ni tapar la diferencia con dinero personal. El centro registra también las novedades, como un servicio no cobrado por una falla del equipo.",
        "Todo cobro se explica con claridad al huésped, y los datos de las solicitudes no se comparten fuera del hotel." + LIM,
    ],
    vocab=[("cuadre de caja", "comparación entre lo registrado y el dinero recibido"), ("diferencia", "dinero de más o de menos respecto del registro"), ("sobrante", "dinero de más en la caja"), ("faltante", "dinero de menos en la caja"), ("novedad", "hecho que debe quedar anotado, como una falla de un equipo")],
    worked=[
        ("Sumar los cobros del día", "En un centro de ejemplo se cobraron $2.000, $3.500 y $1.500 en tres solicitudes. ¿Cuánto debe haber en caja por esas solicitudes?", ["Se suman los tres totales.", "2.000 + 3.500 + 1.500 = 7.000."], "$7.000"),
        ("Detectar un faltante", "El registro de ejemplo suma $9.000 y en la caja hay $8.500. ¿Qué diferencia hay?", ["Se compara el registro con la caja.", "9.000 − 8.500 = 500."], "Faltan $500"),
    ],
    mistakes=[("Poner dinero propio en la caja para que «cuadre» una diferencia.", "Oculta el problema y no permite descubrir su causa.", "Informa la diferencia a la jefatura y revisa los registros."),
              ("Cerrar el día sin revisar cada solicitud porque «siempre cuadra».", "Los errores pequeños se repiten y pasan inadvertidos.", "Calcula cada solicitud y compara con la caja todos los días.")],
    T=[
        ("abc", "En Hotelería: ¿qué es el cuadre de caja?", "La comparación entre lo registrado y el dinero recibido", "El conteo de huéspedes del hotel", "El cambio de turno del personal", "El cuadre compara los registros con el dinero real."),
        ("=", "{F} ¿Cuánto se cobró en la solicitud A?", "30*100", "Se multiplica la tarifa por hoja por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuánto se cobró en la solicitud B?", "12*300", "Se multiplica la tarifa a color por las hojas.", " pesos"),
        ("=", "{F} ¿Cuánto se cobró en la solicitud C?", "2*15000", "Se multiplican las horas de la sala por el valor por hora.", " pesos"),
        ("=", "{F} ¿Cuánto se cobró en la solicitud D?", "6*200", "Se multiplican los escaneos por su tarifa.", " pesos"),
        ("=", "{F} ¿Cuánto se cobró en la solicitud E?", "20*100+5*300", "Se calcula cada tipo de hoja por su tarifa y se suman.", " pesos"),
        ("=", "{F} ¿Cuál es el total que debe haber en caja según las cinco solicitudes?", "30*100+12*300+2*15000+6*200+20*100+5*300", "Se suman los cobros de las cinco solicitudes.", " pesos"),
        ("abc", "{F} Si la caja tiene $41.300 y el registro suma $41.300, ¿cómo queda el cuadre?", "Cuadra: no hay diferencia", "Sobra dinero", "Falta dinero", "El registro y la caja coinciden, así que no hay diferencia."),
        ("=", "{F} Si al contar la caja se encuentran $40.800, ¿cuánto falta respecto del registro?", "41300-40800", "Al total registrado se le resta el dinero contado.", " pesos"),
        ("abc", "{F} Hay un faltante de $500. ¿Qué haces primero?", "Revisar los cálculos y los registros, y luego informar a la jefatura", "Poner $500 propios en la caja", "Borrar un registro para que cuadre", "Se investiga la causa y se informa; no se oculta."),
        ("abc", "{F} Un compañero dice: «Si sobran $200, me los guardo». ¿Qué respondes?", "Que un sobrante también se registra e informa", "Que está bien, porque son pocos pesos", "Que se reparta entre todos", "Un sobrante es una diferencia y debe informarse."),
        ("abc", "{F} La impresora falló durante la solicitud A y no se imprimieron 5 hojas. ¿Qué debe hacer quien atiende?", "Cobrar solo las hojas impresas y anotar la novedad", "Cobrar las 30 hojas igual", "No anotar nada", "Se cobra lo realmente entregado y se registra la falla."),
        ("=", "{F} Con el cobro de A corregido a 25 hojas, ¿cuánto debería sumar el registro del día?", "25*100+12*300+2*15000+6*200+20*100+5*300", "Se reemplaza el cobro de A por las 25 hojas realmente impresas.", " pesos"),
    ],
    ctx=("abc", "{F} Al cerrar, la caja tiene $1.000 de más y la persona que atendió dice que no sabe por qué. ¿Qué corresponde?", "Revisar los registros, anotar la diferencia e informar a la jefatura", "Guardarse el dinero", "Dejarlo en la caja sin anotar", "Una diferencia en cualquier sentido se investiga y se informa."),
    sc=[
        ("En Hotelería: ¿qué es un faltante?", "Dinero de menos en la caja", "Es una diferencia negativa frente al registro."),
        ("¿Qué haces si hay una diferencia?", "Reviso, anoto e informo a la jefatura", "No se oculta ni se tapa con dinero propio."),
        ("¿Qué se cobra si la impresora falla?", "Solo lo realmente entregado", "Se cobra lo que el huésped recibió."),
    ],
    op=("Solicitudes de ejemplo de un día: P, 40 hojas blanco y negro a $100; Q, 8 hojas a color a $300; R, sala por 3 horas a $15.000; S, 10 escaneos a $200. En la caja hay $53.000. "
        "Calcula el total del registro, di si la caja cuadra, cuánto sobra o falta, y qué harías.",
        "P: 4.000. Q: 2.400. R: 45.000. S: 2.000. Total: 53.400. En la caja hay 53.000, así que faltan $400. Revisaría los cálculos y los registros, anotaría la diferencia e informaría a la jefatura sin poner dinero propio.",
        ["calcula cada solicitud y el total", "compara con la caja", "decide con honestidad"],
        ["hoja con los cálculos y la decisión"],
        ["sumar mal", "restar al revés", "ocultar la diferencia"],
        "Pregunta: «¿qué haces si falta dinero?». Si responde 'lo pongo yo', repasa por qué se informa."),
    reinforce="Inventa tres solicitudes con tarifas y calcula el total del registro.",
    extend="Explica por qué revisar la caja todos los días ayuda a encontrar errores pequeños a tiempo.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 24 (folio de ejemplo, inventado). Huésped de la habitación 205, estadía de 3 noches. Cargos: alojamiento, 3 noches × $48.000; restaurante, $18.500; lavandería, 6 prendas × $1.500; estacionamiento, 3 noches × $6.000. Abono: anticipo de $20.000. "
     "Check-out a las 11:00; el folio debe quedar listo a las 10:30. Medios de pago: efectivo, tarjeta o transferencia. Al pagar se entrega el documento tributario que corresponda según la norma vigente.")
build(
    O6, 1, F,
    use="Aprenderé qué es el cierre de cuenta, qué reúne un folio, qué cobros se notifican y qué reglas de claridad, consumo y documentos se cumplen en el pago.",
    prior=["Sé calcular totales de servicios.", "Conozco la reserva y el anticipo.", "Sé leer una cuenta con varios cargos."],
    explain=[
        "El cierre de cuenta es el proceso de revisar, notificar y cobrar todo lo que un huésped consumió durante su estadía. El folio es la cuenta que reúne los cargos (cobros por servicios, como el alojamiento o la lavandería) y los abonos (pagos, como el anticipo). El total a pagar es la suma de los cargos menos los abonos.",
        "El cierre se prepara con tiempo, antes de que el huésped baje, para revisar errores y evitar esperas. Se notifica al huésped cada cobro con su detalle, según la protección al consumidor: debe poder revisar y preguntar antes de pagar. Al pagar se entrega el documento tributario que corresponda según la norma vigente, sin inventar reglas.",
        "Si el huésped quiere pagar en otra moneda, se informa el tipo de cambio que el hotel usa ese día. Los datos de la cuenta son confidenciales: se cobra en voz baja y no se muestran folios de otros huéspedes." + LIM,
    ],
    vocab=[("cierre de cuenta", "proceso de revisar, notificar y cobrar todo lo que el huésped consumió"), ("folio", "cuenta que reúne los cargos y abonos de una estadía"), ("cargo", "cobro por un servicio o consumo"), ("abono", "pago que se descuenta de la cuenta, como un anticipo"), ("documento tributario", "documento que respalda un pago ante la autoridad, según la norma vigente"), ("tipo de cambio", "valor en pesos de una moneda extranjera en un día")],
    worked=[
        ("Calcular el total a pagar", "Un folio de ejemplo suma cargos por $85.000 y tiene un abono de $15.000. ¿Cuánto debe pagar el huésped?", ["Total a pagar = cargos − abonos.", "85.000 − 15.000 = 70.000."], "$70.000"),
        ("Distinguir cargo y abono", "En un folio de ejemplo aparece «anticipo $10.000». ¿Es cargo o abono?", ["Un anticipo es un pago del huésped.", "Se descuenta de la cuenta."], "Un abono"),
    ],
    mistakes=[("Entregar al huésped solo el total sin mostrar el detalle de los cargos.", "No puede revisar ni reclamar un cobro erróneo; se afecta su derecho a información clara.", "Muestra el detalle de cada cargo y responde sus preguntas."),
              ("Mostrar en el mostrador el folio de un huésped mientras otros esperan cerca.", "Se difunden datos personales y de consumo.", "Atiende en voz baja y no muestres folios ajenos.")],
    T=[
        ("abc", "En Hotelería: ¿qué es el folio de un huésped?", "La cuenta que reúne los cargos y abonos de su estadía", "La lista de habitaciones libres", "El reglamento interno del hotel", "El folio es la cuenta de la estadía; la lista de habitaciones o el reglamento son otros documentos."),
        ("abc", "{F} En el folio, ¿qué es el anticipo de $20.000?", "Un abono", "Un cargo", "Un descuento sorpresa", "El anticipo es un pago del huésped que se descuenta."),
        ("=", "{F} ¿Cuánto es el cargo de alojamiento?", "48000*3", "Se multiplica la tarifa por noche por las noches.", " pesos"),
        ("=", "{F} ¿Cuánto es el cargo de lavandería?", "1500*6", "Se multiplica el precio por prenda por la cantidad de prendas.", " pesos"),
        ("=", "{F} ¿Cuál es el total de los cargos del folio?", "48000*3+18500+1500*6+6000*3", "Se suman los cuatro cargos de la cuenta.", " pesos"),
        ("=", "{F} ¿Cuánto debe pagar el huésped después de descontar el anticipo?", "48000*3+18500+1500*6+6000*3-20000", "Al total de cargos se le resta el abono.", " pesos"),
        ("abc", "{F} ¿A qué hora debe estar listo el folio?", "A las 10:30", "A las 11:00", "A las 12:00", "La ficha fija las 10:30, antes del check-out de las 11:00."),
        ("abc", "¿Qué derecho del huésped se cumple al mostrarle el detalle de los cargos?", "Recibir información clara para revisar y preguntar antes de pagar", "Pagar menos de lo consumido", "No recibir ningún documento", "La protección al consumidor incluye información clara sobre lo que se cobra."),
        ("abc", "{F} Al pagar, ¿qué documento corresponde entregar?", "El documento tributario que corresponda según la norma vigente", "Un papel interno sin valor", "Ninguno, si paga en efectivo", "Siempre se entrega el documento tributario que corresponde según la norma."),
        ("abc", "{F} Un huésped no reconoce el cargo de restaurante. ¿Qué haces?", "Revisar el comprobante del consumo, mostrárselo y corregir si hay un error", "Decirle que pague y reclame después", "Borrar el cargo sin revisar", "Se verifica con el comprobante y se corrige solo si corresponde."),
        ("abc", "{F} Un huésped quiere pagar en otra moneda. ¿Qué debes informar antes de cobrar?", "El tipo de cambio que usa el hotel ese día", "Nada, porque se calcula solo", "El precio de otra cuenta", "El tipo de cambio debe ser claro antes de cobrar."),
        ("=", "{F} Un huésped paga solo el restaurante, de $18.500, con un billete de $20.000. ¿Cuánto vuelto recibe?", "20000-18500", "Al billete se le resta el valor del consumo.", " pesos"),
        ("abc", "Otro huésped, en la fila, te pide ver el folio de la persona que está adelante. ¿Qué respondes?", "Que no puedes mostrar cuentas de otros huéspedes", "Que sí, si es rápido", "Que sí, si es su amigo", "Los datos de consumo son confidenciales."),
    ],
    ctx=("abc", "{F} A las 10:20 notas que el folio no muestra el abono del anticipo. ¿Qué haces?", "Corregirlo con el comprobante del anticipo y avisar a la jefatura", "Esperar a que el huésped lo note", "Cobrar la cuenta sin descontarlo", "Se corrige antes de cobrar para no cobrar de más."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el total a pagar de un folio?", "Cargos menos abonos", "El abono reduce lo que falta pagar."),
        ("¿Qué se entrega al pagar?", "El documento tributario que corresponda", "Respalda el pago según la norma vigente."),
        ("¿Qué se muestra al huésped antes de cobrar?", "El detalle de cada cargo", "Debe poder revisar y preguntar antes de pagar."),
    ],
    op=("Folio de ejemplo: alojamiento, 2 noches × $55.000; desayuno extra, $6.000; lavandería, 4 prendas × $1.500; anticipo, $30.000. Check-out a las 11:00. "
        "Calcula el total de cargos y lo que debe pagar el huésped, y escribe dos acciones que harías antes de cobrar para cumplir con informar con claridad y cuidar sus datos.",
        "Cargos: 110.000 + 6.000 + 6.000 = 122.000. Abono: 30.000. A pagar: 92.000. Acciones: mostrar el detalle de cada cargo y responder preguntas; cobrar en voz baja sin mostrar folios de otros huéspedes y entregar el documento tributario que corresponde.",
        ["calcula cargos y saldo", "nombra una acción de información clara", "nombra una acción de privacidad"],
        ["hoja con cálculos y dos acciones"],
        ["no descontar el anticipo", "olvidar el detalle de los cargos", "no mencionar privacidad"],
        "Pregunta: «¿por qué se resta el anticipo?». Si no responde que ya fue pagado, repasa abono y cargo."),
    reinforce="Inventa un folio con cuatro cargos y un abono y calcula lo que debe pagar el huésped.",
    extend="Explica por qué preparar el folio antes del check-out evita esperas y errores.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 25 (documentos de cobro, de ejemplo). Folio: cuenta del huésped con cargos y abonos. Boleta: documento tributario para un consumidor final. Factura: documento tributario a nombre de una empresa; requiere sus datos tributarios (razón social, identificador tributario, giro y dirección) y se pide antes de emitirla. "
     "Voucher: comprobante de un pago con tarjeta. Nota de crédito: documento que corrige o anula un cobro ya emitido. Tipo de cambio del día (de ejemplo): 1 dólar de ejemplo = 900 pesos. Folio de ejemplo: total a pagar $81.000.")
build(
    O6, 2, F,
    use="Aprenderé los documentos del cierre de cuenta (folio, boleta, factura, voucher, nota de crédito) y a convertir monedas con un tipo de cambio de ejemplo.",
    prior=["Conozco el folio y sus cargos.", "Sé multiplicar y dividir.", "Conozco el pago con tarjeta."],
    explain=[
        "El folio reúne los cargos y abonos. Al pagar se emite un documento tributario: la boleta para un consumidor final y la factura cuando la compra es a nombre de una empresa, para lo cual se piden antes sus datos tributarios. El voucher es el comprobante de un pago con tarjeta. La nota de crédito corrige o anula un cobro ya emitido, por ejemplo uno duplicado. Qué documento corresponde en cada caso lo determina la norma vigente.",
        "El tipo de cambio es el valor en pesos de una moneda extranjera. Para pasar dólares a pesos se multiplican los dólares por el tipo de cambio; para pasar pesos a dólares se dividen los pesos por el tipo de cambio. El hotel informa el tipo de cambio antes de cobrar y lo registra.",
        "Si un documento ya emitido tiene un error, no se cambia a mano: se consulta a la jefatura o a contabilidad cómo corregirlo según la norma vigente. Los documentos de pago se entregan solo al huésped." + LIM,
    ],
    vocab=[("boleta", "documento tributario para un consumidor final"), ("factura", "documento tributario a nombre de una empresa"), ("voucher", "comprobante de un pago con tarjeta"), ("nota de crédito", "documento que corrige o anula un cobro ya emitido"), ("datos tributarios", "datos de la empresa que se piden para emitir una factura"), ("tipo de cambio", "valor en pesos de una moneda extranjera")],
    worked=[
        ("Convertir dólares a pesos", "Con un tipo de cambio de ejemplo de 1 dólar = 800 pesos, un huésped paga 50 dólares. ¿Cuántos pesos son?", ["Pesos = dólares × tipo de cambio.", "50 × 800 = 40.000."], "40.000 pesos"),
        ("Elegir el documento", "Un huésped de ejemplo viaja por su cuenta y paga su cuenta. ¿Qué documento tributario corresponde?", ["Es un consumidor final.", "Se emite una boleta."], "Una boleta"),
    ],
    mistakes=[("Corregir a mano con lápiz una boleta ya emitida que tiene un error.", "Un documento tributario no se altera; hacerlo puede traer problemas al hotel.", "Consulta a la jefatura o contabilidad cómo corregirlo según la norma vigente."),
              ("Cobrar en dólares sin decir el tipo de cambio que se usa.", "El huésped no puede comprobar si el cobro es justo.", "Informa el tipo de cambio antes de cobrar.")],
    T=[
        ("abc", "En Hotelería: ¿para qué sirve una nota de crédito?", "Para corregir o anular un cobro ya emitido", "Para cobrar una noche extra", "Para reservar una habitación", "La nota de crédito corrige un documento ya emitido."),
        ("abc", "{F} ¿Qué documento se emite a nombre de una empresa?", "La factura", "La boleta", "El voucher", "La factura se emite a nombre de una empresa; la boleta es para un consumidor final."),
        ("abc", "{F} ¿Qué comprobante respalda un pago con tarjeta?", "El voucher", "La nota de crédito", "El folio vacío", "El voucher es el comprobante del pago con tarjeta."),
        ("abc", "{F} ¿Qué datos se piden antes de emitir una factura?", "Los datos tributarios de la empresa", "La clave de la tarjeta", "El nombre de la mascota del huésped", "La factura exige razón social, identificador, giro y dirección."),
        ("=", "{F} Un huésped paga 120 dólares de ejemplo. ¿Cuántos pesos son?", "120*900", "Se multiplican los dólares por el tipo de cambio.", " pesos"),
        ("=", "{F} El total a pagar de $81.000, ¿cuántos dólares de ejemplo son?", "81000//900", "Se dividen los pesos por el tipo de cambio.", " dólares"),
        ("=", "{F} Una empresa de ejemplo paga 250 dólares. ¿Cuántos pesos son?", "250*900", "Se multiplican los dólares por el tipo de cambio.", " pesos"),
        ("abc", "{F} Se cobró dos veces el mismo consumo y el documento ya fue emitido. ¿Qué corresponde?", "Consultar cómo corregirlo con una nota de crédito según la norma vigente", "Cambiar el valor a mano en el documento", "Dejar el cobro doble", "Un cobro ya emitido se corrige con el documento adecuado, no a mano."),
        ("abc", "{F} Un huésped pide una factura para su empresa después de haber recibido una boleta. ¿Qué haces?", "Consultar a la jefatura o contabilidad cómo corregirlo según la norma vigente", "Entregar una factura sin anular nada", "Cambiar la fecha de la boleta", "Un cambio de documento se resuelve con quien conoce la norma."),
        ("abc", "{F} El voucher dice $81.000 y el folio dice $83.000. ¿Qué haces antes de cerrar?", "Verificar cuál es correcto y corregir el registro", "Dejarlo así", "Anotar el valor que más conviene", "Una diferencia entre documentos se verifica antes de cerrar la cuenta."),
        ("=", "{F} Del total de $81.000, el huésped paga $40.000 en efectivo y el resto con tarjeta. ¿Cuál es el monto del voucher?", "81000-40000", "Al total se le resta lo pagado en efectivo.", " pesos"),
        ("abc", "Dejas el voucher y la boleta de un huésped sobre el mostrador, a la vista. ¿Qué observación corresponde?", "Deben entregarse al huésped y no quedar a la vista de otros", "Está bien si el huésped no está", "Está bien si son pocos", "Los documentos de pago contienen datos personales."),
        ("abc", "Un huésped paga en dólares y quiere el vuelto en pesos. ¿Qué debes tener claro?", "El tipo de cambio informado y registrado de ese día", "Un tipo de cambio cualquiera", "El tipo de cambio del mes pasado", "El tipo de cambio debe ser el vigente y estar informado."),
    ],
    ctx=("abc", "{F} Una turista extranjera dice: «Quiero pagar los $81.000 en dólares». ¿Qué haces?", "Informar el tipo de cambio de ejemplo (900 pesos por dólar), el monto en dólares y registrarlo", "Pedirle que traiga pesos", "Cobrar un monto en dólares sin explicar cómo se calculó", "Se informa el tipo de cambio y el monto antes de cobrar."),
    sc=[
        ("En Hotelería: ¿cómo se pasan dólares a pesos?", "Multiplicando por el tipo de cambio", "El tipo de cambio es el valor en pesos de un dólar."),
        ("¿Qué documento se emite a nombre de una empresa?", "La factura", "Lleva los datos tributarios de la empresa."),
        ("¿Se corrige a mano un documento ya emitido?", "No", "Se corrige con el documento que corresponda según la norma."),
    ],
    op=("Datos de ejemplo. Tipo de cambio del día: 1 euro de ejemplo = 1.000 pesos. Un huésped debe pagar $64.000. Quiere pagar con tarjeta una parte y el resto en euros: paga $24.000 con tarjeta. "
        "Calcula el monto del voucher y cuántos euros paga el resto, y escribe qué documento tributario entregarías si el pago es personal y cuál si lo paga una empresa.",
        "Voucher: $24.000. Resto: 64.000 − 24.000 = 40.000 pesos, que son 40.000 ÷ 1.000 = 40 euros. Pago personal: boleta; pago de una empresa: factura, con sus datos tributarios, según la norma vigente.",
        ["calcula voucher y conversión", "distingue boleta y factura", "menciona la norma vigente"],
        ["hoja con cálculos y documentos"],
        ["multiplicar en lugar de dividir", "confundir boleta con factura", "no informar el tipo de cambio"],
        "Pregunta: «¿por qué dividir los pesos para obtener euros?». Si no lo explica, repasa la conversión."),
    reinforce="Haz una tabla con los cinco documentos de la ficha y cuándo se usa cada uno.",
    extend="Explica por qué una nota de crédito deja trazabilidad de una corrección.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 26 (folio con errores, de ejemplo, inventado). Huésped de la habitación 308: llegó el día 10 y sale el día 12 (tarifa de $52.000 por noche). Anticipo: $25.000. "
     "El folio muestra: alojamiento, 3 noches × $52.000 = $156.000; restaurante, $14.800; restaurante, $14.800 (el mismo consumo anotado dos veces, con el mismo comprobante); estacionamiento, 2 noches × $6.000 = $12.000. El anticipo no aparece como abono. Total mostrado: $197.600.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un folio con errores, corregirlos con respaldo y explicar el cobro correcto con claridad al huésped.",
    prior=["Conozco el folio, cargos y abonos.", "Sé contar noches.", "Conozco la nota de crédito."],
    explain=[
        "Antes de cerrar una cuenta se revisa el folio punto por punto. Los errores más comunes son un cargo duplicado, una noche contada de más, un abono que no se descontó o un precio mal anotado. Se compara cada cargo con su comprobante o con la reserva: las noches se cuentan desde la llegada hasta la salida.",
        "Para corregir un error se busca el respaldo (comprobante, ficha de reserva), se corrige el folio antes de emitir el documento y se registra qué se cambió y por qué. Si el documento ya se emitió, se consulta a la jefatura cómo corregirlo, por ejemplo con una nota de crédito.",
        "Al explicar el cobro al huésped, se reconoce el error con respeto, se muestra el detalle corregido y se pide disculpas por la molestia, sin culpar a nadie." + LIM,
    ],
    vocab=[("cargo duplicado", "el mismo consumo anotado dos veces"), ("respaldo", "documento que prueba un cobro, como un comprobante o la reserva"), ("corrección", "cambio hecho para eliminar un error"), ("comprobante", "papel que prueba un consumo o un pago"), ("trazabilidad", "posibilidad de seguir qué se hizo, cuándo y por qué")],
    worked=[
        ("Detectar un cargo duplicado", "En un folio de ejemplo aparece dos veces «$9.000 restaurante» con el mismo comprobante. ¿Qué error hay?", ["Es el mismo comprobante registrado dos veces.", "Es un cargo duplicado."], "Un cargo duplicado"),
        ("Contar noches", "Un huésped de ejemplo llegó el día 3 y sale el día 7. ¿Cuántas noches debe cobrarse?", ["Noches = día de salida − día de llegada.", "7 − 3 = 4."], "4 noches"),
    ],
    mistakes=[("Corregir un cargo del folio sin revisar el comprobante.", "Se puede eliminar un cobro correcto o mantener uno erróneo.", "Revisa el comprobante antes de cambiar el folio."),
              ("Culpar al compañero del turno anterior frente al huésped.", "No resuelve el problema y daña la imagen del hotel.", "Reconoce el error con respeto y explica la corrección.")],
    T=[
        ("abc", "En Hotelería: ¿qué es un cargo duplicado?", "El mismo consumo anotado dos veces", "Un descuento aplicado dos veces", "Un servicio gratuito", "Duplicado significa repetido; es el mismo cobro registrado más de una vez."),
        ("=", "{F} Según las fechas de llegada y salida, ¿cuántas noches debe cobrarse el alojamiento?", "12-10", "Se resta el día de llegada al día de salida.", " noches"),
        ("abc", "{F} ¿Qué error hay en el cargo de alojamiento?", "Se cobraron 3 noches y corresponden 2", "Se cobraron 2 noches y corresponden 3", "No hay ningún error", "Las fechas indican 2 noches; el folio muestra 3."),
        ("=", "{F} ¿Cuánto debe costar el alojamiento correcto?", "52000*2", "Se multiplica la tarifa por las 2 noches correctas.", " pesos"),
        ("abc", "{F} ¿Qué error hay en el restaurante?", "El mismo consumo, con el mismo comprobante, aparece dos veces", "El consumo no tiene precio", "El consumo es de otra habitación", "La ficha dice que es el mismo consumo anotado dos veces."),
        ("abc", "{F} ¿Qué error hay con el anticipo de $25.000?", "No aparece descontado como abono", "Está descontado dos veces", "Es mayor que el total", "La ficha dice que no aparece como abono."),
        ("=", "{F} ¿Cuál es el total correcto de cargos?", "52000*2+14800+6000*2", "Se suman el alojamiento correcto, un solo cargo de restaurante y el estacionamiento.", " pesos"),
        ("=", "{F} ¿Cuánto debe pagar el huésped después de descontar el anticipo?", "52000*2+14800+6000*2-25000", "Al total correcto de cargos se le resta el abono.", " pesos"),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre el total mostrado y el total correcto de cargos?", "197600-(52000*2+14800+6000*2)", "Al total mostrado se le resta el total correcto.", " pesos"),
        ("abc", "{F} ¿Cómo se explica el error al huésped?", "Reconociendo el error con respeto, mostrando el detalle corregido y pidiendo disculpas", "Diciéndole que el sistema nunca falla", "Culpando a otro compañero", "Se informa con claridad y respeto lo corregido."),
        ("abc", "{F} Se detecta el error después de haber emitido la boleta. ¿Qué haces?", "Consultar a la jefatura cómo corregirlo, por ejemplo con una nota de crédito", "Borrar el valor de la boleta con corrector", "No decir nada al huésped", "Un documento emitido se corrige con el procedimiento que indica la norma."),
        ("abc", "{F} El huésped dice que sabe leer y prefiere calcular él mismo el total. ¿Qué haces?", "Mostrarle el detalle y dejarlo revisar con calma", "Decirle que no tiene tiempo", "Negarse a mostrarle el folio", "Tiene derecho a revisar el detalle antes de pagar."),
        ("abc", "{F} Un compañero propone no corregir los $14.800 repetidos para «que el huésped no se dé cuenta». ¿Qué respondes?", "Que no: cobrar de más es un error que se debe corregir", "Que está bien si el huésped no lo nota", "Que se corrige solo si reclama", "Cobrar un consumo dos veces perjudica al consumidor."),
    ],
    ctx=("abc", "{F} Al explicar los errores, el huésped se muestra molesto y dice que no volverá. ¿Qué respuesta es adecuada?", "Pedir disculpas, mostrar la corrección y ofrecer registrar su comentario para mejorar", "Decirle que no se moleste", "Cobrarle sin responder", "Reconocer y corregir con respeto es la mejor forma de atender un reclamo."),
    sc=[
        ("En Hotelería: ¿qué haces antes de corregir un cargo?", "Reviso su comprobante o respaldo", "El respaldo prueba si el cargo es correcto."),
        ("¿Cómo se cuentan las noches?", "Restando el día de llegada al de salida", "El día de salida no es una noche."),
        ("¿Qué haces si el documento ya se emitió?", "Consulto cómo corregirlo", "No se altera un documento emitido."),
    ],
    op=("Folio de ejemplo: llegada el día 4, salida el día 7, tarifa $40.000 por noche. Muestra: alojamiento 4 noches × 40.000 = 160.000; restaurante $9.500; restaurante $9.500 (mismo comprobante); abono de $20.000 no descontado. "
        "Encuentra los errores, calcula el total correcto y lo que debe pagar, y escribe una frase para explicarlo al huésped.",
        "Errores: 4 noches cobradas y son 3; restaurante duplicado; abono no descontado. Alojamiento correcto: 3 × 40.000 = 120.000. Cargos correctos: 120.000 + 9.500 = 129.500. A pagar: 129.500 − 20.000 = 109.500. Frase: «Encontramos tres errores en su cuenta, ya los corregimos y le pedimos disculpas; este es el detalle correcto».",
        ["encuentra los tres errores", "calcula bien total y saldo", "explica con respeto"],
        ["hoja con errores, cálculos y frase"],
        ["no detectar la noche de más", "dejar el cargo duplicado", "no descontar el abono"],
        "Pregunta: «¿cuántas noches son entre el día 4 y el 7?». Si responde 4, repasa el conteo de noches."),
    reinforce="Inventa un folio con un error y escribe cómo lo corregirías.",
    extend="Explica por qué guardar el motivo de cada corrección ayuda a mejorar el trabajo del equipo.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 27 (cuenta compartida de ejemplo, inventada). Una empresa de ejemplo paga el alojamiento de su trabajador: 4 noches × $55.000, con desayuno incluido. El trabajador paga sus consumos propios: restaurante $24.000 y lavandería $12.000. "
     "Tipo de cambio de ejemplo del día: 1 dólar de ejemplo = 900 pesos. El trabajador paga sus consumos con un billete de 50 dólares de ejemplo; el hotel entrega el vuelto en pesos.")
build(
    O6, 4, F,
    use="Aprenderé a dividir una cuenta entre quien paga la empresa y quien paga el huésped, convertir monedas y calcular el vuelto con orden.",
    prior=["Conozco el folio y el tipo de cambio.", "Sé multiplicar y restar.", "Sé calcular vueltos."],
    explain=[
        "En una cuenta compartida, una parte la paga un tercero, como una empresa, y otra el huésped. Cada parte debe tener su propia cuenta y su documento tributario correcto: el alojamiento se factura a la empresa, y los consumos propios se cobran al huésped. Así se evita mezclar lo que paga cada uno.",
        "Si el huésped paga en una moneda extranjera, se convierte el monto: pesos ÷ tipo de cambio para saber cuántas unidades de la otra moneda equivalen, o unidades × tipo de cambio para pasar a pesos. Si se entrega un billete mayor que el monto, el vuelto es la diferencia, calculada en pesos con el tipo de cambio informado.",
        "Antes de cobrar, se muestra a cada pagador su parte con detalle y se registra. Los datos de la empresa y del huésped se tratan con confidencialidad." + LIM,
    ],
    vocab=[("cuenta compartida", "cuenta en que una parte la paga un tercero y otra el huésped"), ("pagador", "persona o empresa que paga una parte de la cuenta"), ("conversión de moneda", "cálculo del valor de una moneda en otra"), ("vuelto", "dinero que se devuelve cuando el pago es mayor que el monto"), ("consumo propio", "gasto que paga el huésped")],
    worked=[
        ("Separar lo que paga la empresa", "Un convenio de ejemplo cubre 3 noches a $40.000, y el huésped paga un restaurante de $15.000. ¿Cuánto paga la empresa y cuánto el huésped?", ["Empresa: 3 × 40.000 = 120.000.", "Huésped: 15.000."], "Empresa $120.000; huésped $15.000"),
        ("Calcular el vuelto", "Un huésped de ejemplo paga con un billete de $20.000 un consumo de $13.500. ¿Cuánto vuelto recibe?", ["Vuelto = billete − consumo.", "20.000 − 13.500 = 6.500."], "$6.500"),
    ],
    mistakes=[("Poner en el mismo documento el alojamiento de la empresa y los consumos propios del trabajador.", "Se mezclan los pagadores y se dificulta cobrar y justificar cada parte.", "Separa la cuenta de la empresa y la del huésped."),
              ("Dar el vuelto sin haber informado el tipo de cambio usado.", "El huésped no puede comprobar si el cálculo es justo.", "Informa el tipo de cambio y muestra el cálculo.")],
    T=[
        ("abc", "En Hotelería: ¿qué es una cuenta compartida?", "Una cuenta en que una parte la paga un tercero y otra el huésped", "Una cuenta que se paga con tarjeta de dos personas", "Una cuenta sin cargos", "En la cuenta compartida hay más de un pagador."),
        ("=", "{F} ¿Cuánto debe pagar la empresa por el alojamiento?", "55000*4", "Se multiplica la tarifa por las 4 noches.", " pesos"),
        ("=", "{F} ¿Cuánto suman los consumos propios del trabajador?", "24000+12000", "Se suman el restaurante y la lavandería.", " pesos"),
        ("abc", "{F} ¿Quién debe recibir el documento tributario por el alojamiento?", "La empresa", "El trabajador", "Nadie", "El alojamiento lo paga la empresa; los consumos propios, el huésped."),
        ("=", "{F} Los consumos propios en pesos, ¿cuántos dólares de ejemplo son?", "(24000+12000)//900", "Se dividen los pesos por el tipo de cambio.", " dólares"),
        ("=", "{F} El billete de 50 dólares de ejemplo, ¿cuántos pesos vale?", "50*900", "Se multiplican los dólares por el tipo de cambio.", " pesos"),
        ("=", "{F} ¿Cuánto vuelto en pesos recibe el trabajador?", "50*900-(24000+12000)", "Al valor del billete en pesos se le resta lo que debe.", " pesos"),
        ("abc", "{F} El trabajador pide que se pase la lavandería a la factura de la empresa. ¿Qué haces?", "Consultar si el convenio de la empresa lo permite, y si no, cobrarla al trabajador", "Pasarla sin consultar", "Perdonarla", "La empresa solo paga lo acordado; lo demás se consulta o se cobra al huésped."),
        ("abc", "{F} Antes de cobrar los consumos propios, ¿qué debe hacerse?", "Mostrar el detalle al trabajador y informar el tipo de cambio", "Cobrar directamente en dólares", "Entregar solo el total", "Se informa el detalle y la conversión antes de cobrar."),
        ("abc", "{F} Un compañero propone usar el tipo de cambio de la semana pasada «porque es más fácil». ¿Qué respondes?", "Que se usa el tipo de cambio informado del día", "Que sí, porque es más rápido", "Que se use el que prefiera el huésped", "El tipo de cambio debe ser el vigente y estar informado."),
        ("=", "{F} Si el trabajador solo tuviera un billete de 100 dólares de ejemplo, ¿cuánto vuelto en pesos recibiría por sus consumos?", "100*900-(24000+12000)", "Al valor del billete en pesos se le resta lo que debe.", " pesos"),
        ("abc", "{F} El trabajador pregunta cuánto paga la empresa por su estadía. ¿Qué haces?", "Informarle solo si el hotel y la empresa lo permiten, y consultar a la jefatura", "Mostrarle la factura de la empresa completa", "Decirle un valor cualquiera", "La cuenta de la empresa es confidencial; se consulta qué puede informarse."),
        ("abc", "{F} Después de entregar el vuelto, ¿qué registras?", "El monto cobrado, el tipo de cambio, el pago en dólares y el vuelto entregado", "Solo el nombre del huésped", "Nada, porque ya pagó", "El registro permite verificar el cobro más tarde."),
    ],
    ctx=("abc", "{F} Al contar el vuelto notas que entregaste $1.000 de menos al trabajador. ¿Qué haces?", "Reconocerlo, devolver la diferencia y anotarlo", "Callar y esperar que no lo note", "Pedirle que lo devuelva", "Corregir un error propio con honestidad protege al cliente y a la confianza."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el vuelto?", "Billete menos consumo", "El vuelto es la diferencia entre lo entregado y lo debido."),
        ("¿Quién recibe el documento por lo que paga la empresa?", "La empresa", "Cada pagador recibe el documento de su parte."),
        ("¿Qué tipo de cambio se usa?", "El informado del día", "Debe ser vigente y conocido por el cliente."),
    ],
    op=("Cuenta compartida de ejemplo. La empresa paga 3 noches a $60.000. El huésped paga sus consumos: $28.000. Tipo de cambio: 1 dólar de ejemplo = 900 pesos. El huésped entrega 40 dólares de ejemplo. "
        "Calcula lo que paga la empresa, el valor de los 40 dólares en pesos, el vuelto, y di qué documentos entregarías a cada pagador.",
        "Empresa: 3 × 60.000 = 180.000. Dólares: 40 × 900 = 36.000. Vuelto: 36.000 − 28.000 = 8.000 pesos. Documentos: factura a la empresa y boleta al huésped por sus consumos, según la norma vigente, cada una con su detalle.",
        ["calcula la parte de la empresa", "convierte la moneda y calcula el vuelto", "separa los documentos por pagador"],
        ["hoja con cálculos y documentos"],
        ["sumar la parte de la empresa a la del huésped", "dividir en vez de multiplicar", "emitir un solo documento"],
        "Pregunta: «¿cuánto paga cada uno?». Si no separa los montos, repasa la cuenta compartida."),
    reinforce="Inventa una cuenta compartida con tres cargos y decide quién paga cada uno.",
    extend="Explica por qué separar las cuentas ayuda a la empresa y al huésped a justificar sus gastos.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 28 (cierre de turno de recepción, de ejemplo). Fondo inicial de la caja: $50.000. Cobros del turno: efectivo, $142.000; tarjeta, tres vouchers de $80.000, $70.000 y $60.000; transferencia, $95.000. "
     "En el arqueo (conteo del dinero) hay en caja $190.000 en efectivo. Presentación de cuenta A: solo el total. Presentación de cuenta B: detalle de cada cargo, total, forma de pago y documento tributario. "
     "Lista de calidad del cierre (de ejemplo): detalle de cargos, total correcto, forma de pago registrada, documento entregado, datos protegidos.")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos formas de presentar la cuenta y a verificar el cierre del turno con un cuadre de caja y una lista de calidad.",
    prior=["Conozco folio, cargos y abonos.", "Sé sumar y restar dinero.", "Conozco el cuadre de caja."],
    explain=[
        "Comparar alternativas de cierre es elegir la que mejor protege al cliente y deja un registro verificable. Una cuenta con detalle de cada cargo, total, forma de pago y documento permite al huésped revisar y al hotel comprobar; una cuenta con solo el total no cumple con informar con claridad.",
        "Para verificar el cierre del turno se hace el arqueo: se cuenta el efectivo en caja y se compara con lo esperado, que es el fondo inicial más los cobros en efectivo. Las tarjetas y transferencias se verifican con sus vouchers o comprobantes. La diferencia es el contado menos el esperado: si es negativa, hay un faltante.",
        "Si hay una diferencia, se recuentan el dinero y los registros, se anota en el informe y se avisa a la jefatura. Nunca se tapa con dinero propio ni se modifica un registro para que cuadre." + LIM,
    ],
    vocab=[("arqueo", "conteo del dinero en caja para compararlo con lo esperado"), ("fondo inicial", "dinero con que comienza la caja al inicio del turno"), ("efectivo esperado", "fondo inicial más los cobros en efectivo"), ("lista de calidad", "lista de puntos que se comprueban al cerrar una cuenta"), ("trazabilidad", "posibilidad de seguir qué se cobró, cuándo y por qué")],
    worked=[
        ("Calcular el efectivo esperado", "Una caja de ejemplo comenzó con $30.000 y recibió $70.000 en efectivo. ¿Cuánto efectivo debe haber?", ["Esperado = fondo inicial + cobros en efectivo.", "30.000 + 70.000 = 100.000."], "$100.000"),
        ("Calcular una diferencia", "En un arqueo de ejemplo hay $98.000 y lo esperado es $100.000. ¿Qué diferencia hay?", ["Diferencia = contado − esperado.", "98.000 − 100.000 = −2.000."], "Faltan $2.000"),
    ],
    mistakes=[("Elegir la presentación de cuenta que solo muestra el total «porque es más rápida».", "El cliente no puede revisar los cargos y se pierde la información clara.", "Elige la que muestra detalle, total, forma de pago y documento."),
              ("Modificar un voucher para que la tarjeta cuadre con el registro.", "Se altera una prueba de pago y se oculta el error.", "Verifica la diferencia y consulta a la jefatura.")],
    T=[
        ("abc", "En Hotelería: ¿qué es el arqueo de caja?", "El conteo del dinero en caja para compararlo con lo esperado", "El pago de la propina del personal", "El conteo de las llaves de las habitaciones", "El arqueo cuenta el dinero y lo compara con los registros."),
        ("=", "{F} ¿Cuánto efectivo debería haber en caja?", "50000+142000", "Se suma el fondo inicial a los cobros en efectivo.", " pesos"),
        ("=", "{F} ¿Cuánto suman los tres vouchers de tarjeta?", "80000+70000+60000", "Se suman los tres montos de los comprobantes.", " pesos"),
        ("=", "{F} ¿Cuánto suman en total los cobros por efectivo, tarjeta y transferencia?", "142000+80000+70000+60000+95000", "Se suman los cobros de los tres medios de pago.", " pesos"),
        ("abc", "{F} El arqueo muestra $190.000 en efectivo. ¿Cómo queda el cuadre del efectivo?", "Hay un faltante de $2.000", "Hay un sobrante de $2.000", "Cuadra exactamente", "El esperado es 192.000 y el contado es 190.000."),
        ("=", "{F} ¿Cuántos pesos faltan en el efectivo?", "50000+142000-190000", "Al efectivo esperado se le resta el efectivo contado.", " pesos"),
        ("abc", "{F} Con el faltante, ¿qué haces primero?", "Recontar y revisar los registros, y luego informar a la jefatura", "Poner $2.000 propios para que cuadre", "Cambiar un registro para ocultarlo", "Se investiga la causa y se informa; no se oculta."),
        ("abc", "{F} ¿Qué presentación de cuenta cumple mejor con informar con claridad?", "La B, con detalle de cargos, total, forma de pago y documento", "La A, solo con el total", "Ambas por igual", "La B permite al cliente revisar cada cargo."),
        ("abc", "{F} ¿Qué punto de la lista de calidad incumple la presentación A?", "El detalle de cargos", "El total correcto", "La protección de datos", "A muestra solo el total y no el detalle."),
        ("=", "{F} Una presentación cumple 4 de los 5 puntos de la lista de calidad. ¿Qué porcentaje cumple?", "4*100//5", "Se multiplican los puntos cumplidos por 100 y se dividen por el total.", " %"),
        ("abc", "{F} Un compañero dice: «Cerremos con la presentación A porque hay fila». ¿Qué respondes?", "Que la B sigue siendo la mejor y se puede preparar con anticipación", "Que la A es mejor siempre", "Que se cobre sin mostrar nada", "El apuro no justifica ocultar el detalle; se prepara con tiempo."),
        ("abc", "{F} Al verificar, encuentras que un voucher de $70.000 no figura en el registro. ¿Qué haces?", "Anotar la diferencia, buscar el cobro asociado y avisar a la jefatura", "Ignorar el voucher", "Romper el voucher", "Un comprobante sin registro puede ser un cobro no anotado y se investiga."),
        ("abc", "{F} Terminas el turno y dejas los folios y vouchers sobre el mostrador. ¿Qué observación corresponde?", "Deben guardarse en un lugar seguro, porque contienen datos de los huéspedes", "Está bien si el hotel está vacío", "Está bien si son pocos", "Los documentos de pago contienen datos personales y se resguardan."),
    ],
    ctx=("abc", "{F} Una huésped pide revisar con calma el detalle de su cuenta y hay fila de espera. ¿Qué haces?", "Atenderla con paciencia, mostrarle el detalle y pedir disculpas a quienes esperan", "Apurarla para no atrasar a los demás", "Decirle que lo revise en su casa", "Informar con claridad es un derecho del cliente, y la espera se explica con amabilidad."),
    sc=[
        ("En Hotelería: ¿cómo se calcula el efectivo esperado?", "Fondo inicial más cobros en efectivo", "Es lo que debe haber en la caja."),
        ("¿Qué haces con un faltante?", "Recuento, registro y aviso a la jefatura", "No se oculta ni se cubre con dinero propio."),
        ("¿Qué presentación de cuenta es mejor?", "La que muestra detalle, total y forma de pago", "Permite al cliente revisar lo cobrado."),
    ],
    op=("Cierre de ejemplo. Fondo inicial $40.000. Cobros del turno: efectivo $85.000; tarjeta $60.000 (dos vouchers de $35.000 y $25.000); transferencia $45.000. El arqueo muestra $128.000 en efectivo. Dos presentaciones de cuenta: A solo con el total, B con detalle. "
        "Calcula el efectivo esperado, la diferencia, qué harías, y cuál presentación elegirías y por qué.",
        "Esperado: 40.000 + 85.000 = 125.000. Contado: 128.000. Sobran $3.000. Haría un recuento, revisaría los registros, anotaría el sobrante e informaría a la jefatura. Elegiría la B porque muestra el detalle y permite al cliente revisar cada cargo.",
        ["calcula el esperado y la diferencia", "decide con honestidad", "elige la presentación con razón"],
        ["hoja con cálculos, decisión y razón"],
        ["restar al revés y llamarlo faltante", "guardarse el sobrante", "elegir la presentación sin razón"],
        "Pregunta: «¿qué haces con un sobrante?». Si responde 'nada', repasa que también se informa."),
    reinforce="Haz una lista de verificación de 5 puntos para el cierre de una cuenta y evalúa un caso inventado.",
    extend="Explica por qué la trazabilidad de los cobros ayuda a resolver reclamos.",
)
