"""Objetivos genéricos TP 3.º y 4.º medio, módulo A: OAG-01 (comunicarse oralmente y por escrito), OAG-02 (leer textos del trabajo) y OAG-03 (tareas prolijas, plazos y calidad).
Todo en papel: empresas, personas, documentos, horarios y cifras inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_gene_common import build

G1 = "TP-GENE-3y4-OAG-01"
G2 = "TP-GENE-3y4-OAG-02"
G3 = "TP-GENE-3y4-OAG-03"
LIM = " Este cuaderno trabaja en papel, con casos de ejemplo: no reemplaza a tu profesor, a tu jefatura ni a la norma vigente."

# ============================================================ OAG-01, clase 1
F = ("Ficha 1 (tres mensajes de ejemplo sobre un mismo atraso en una tienda de ropa). Mensaje A, a un compañero de turno: «Oye, llego como 20 min tarde, tapa la caja po». "
     "Mensaje B, a la jefa de tienda: «Estimada Sra. Paula: le informo que llegaré 20 minutos después de mi hora de entrada por un problema de transporte. Le avisaré apenas esté en el local. Saludos cordiales, Matías». "
     "Mensaje C, a un cliente que espera: «Disculpe la demora; en cuanto llegue mi colega lo atenderá con gusto».")
build(
    G1, 1, F,
    use="Aprenderé a elegir el registro de habla y de escritura según la situación laboral y la persona con quien me comunico.",
    prior=["Sé redactar frases completas.", "Sé calcular diferencias de horas.", "Sé que no se habla igual con un amigo que con un cliente."],
    explain=[
        "En el trabajo, el registro es la forma de hablar o escribir que eliges según la situación y la persona que recibe el mensaje. El registro formal usa trato respetuoso, frases completas y sin jerga; se usa con jefaturas, clientes y documentos. El registro informal es cercano y se usa con personas de confianza, en situaciones sin consecuencias escritas. El registro técnico usa el vocabulario propio del oficio y solo se entiende bien entre quienes lo conocen.",
        "Un mensaje claro entrega lo necesario: quién, qué, cuándo y, si corresponde, por qué. Si hablas con alguien que no conoce tu oficio, cambias las siglas y los términos técnicos por palabras simples o los explicas. Un mensaje escrito, aunque sea de mensajería, queda como registro y puede leerlo más gente de la que pensabas.",
        "Elegir bien el registro es una forma de respeto: muestra que valoras a la otra persona y cuida la imagen de la empresa. Cuando dudes, es más seguro usar un registro formal y claro." + LIM,
    ],
    vocab=[("registro", "forma de hablar o escribir que se elige según la situación y el interlocutor"), ("registro formal", "trato respetuoso, frases completas y sin jerga"), ("registro informal", "forma cercana de hablar, propia de la confianza"), ("registro técnico", "vocabulario propio de un oficio, claro entre quienes lo conocen"), ("interlocutor", "persona con quien se conversa o a quien se escribe"), ("jerga", "palabras o expresiones propias de un grupo, que otros pueden no entender")],
    worked=[
        ("Elegir el registro", "Una asistente administrativa de ejemplo escribe el primer correo a una empresa proveedora que no conoce. ¿Qué registro usa?", ["Es la primera comunicación con alguien externo y sin confianza.", "Corresponde trato respetuoso, frases completas y sin jerga."], "Registro formal"),
        ("Reescribir un mensaje", "Mensaje: «Mañana no voy, tengo un trámite». Se envía al jefe de una oficina. ¿Cómo se reescribe?", ["Se agrega el trato respetuoso y se precisa el motivo y la fecha.", "Se ofrece una solución para la tarea pendiente."], "«Sr. Rojas: le informo que mañana no podré asistir por un trámite personal. Dejaré mis pendientes ordenados para el turno. Saludos cordiales, Ana»."),
    ],
    mistakes=[("Escribir a un cliente «no te preocupes, ya te lo mando po».", "La jerga y el tuteo apresurado restan seriedad y pueden sonar poco respetuosos con quien no conoce al trabajador.", "Usa trato de usted y una frase completa: «No se preocupe, se lo enviaremos hoy»."),
              ("Usar una sigla del oficio con una clienta sin explicarla.", "Quien no conoce el oficio no la entiende y se queda sin la información que necesita.", "Reemplaza la sigla por palabras simples o explícala la primera vez.")],
    T=[
        ("abc", "En comunicación laboral: ¿qué caracteriza al registro formal?", "Trato respetuoso, frases completas y sin jerga", "Vocabulario del oficio sin explicarlo a nadie", "Frases breves y cercanas, como entre amigos", "Lo formal se define por el respeto y la claridad; lo cercano es registro informal y el vocabulario del oficio es técnico."),
        ("abc", "{F} ¿A quién se dirige el mensaje A?", "A un compañero de turno con quien hay confianza", "A la jefa de la tienda", "A un cliente que espera", "El mensaje A habla de «tapar la caja», algo que se pide a un colega; la jefa y el cliente reciben los otros mensajes."),
        ("abc", "{F} ¿Qué palabra del mensaje A pertenece al registro informal?", "«po»", "«Saludos»", "«local»", "«po» es una muletilla coloquial; las otras palabras aparecen también en un mensaje cortés."),
        ("abc", "Una técnica en enfermería de ejemplo explica a una usuaria que no conoce el tema por qué debe volver a control. ¿Qué forma de hablar conviene?", "Palabras simples, sin siglas, y confirmar que entendió", "Siglas clínicas para ahorrar tiempo", "Un tono de broma para que no se asuste", "Quien no conoce el oficio necesita palabras simples; las siglas y las bromas pueden dejarla sin información clara."),
        ("abc", "{F} ¿Por qué el mensaje B es más adecuado para la jefa que el mensaje A?", "Usa trato respetuoso, entrega el motivo y compromete un aviso", "Es más largo y por eso siempre es mejor", "Usa palabras técnicas del comercio que la jefa exige", "Lo útil para la jefa son el respeto, el motivo y el aviso, no el largo ni los términos técnicos."),
        ("abc", "Un aprendiz envía un mensaje a un grupo de mensajería donde está su jefa. ¿Qué debe cuidar?", "Que sea claro y respetuoso, porque queda escrito y lo lee todo el grupo", "Que lleve muchos emojis para que suene relajado", "Que no incluya datos, para no comprometerse", "Un mensaje escrito deja registro y lo ven varias personas, por eso la claridad y el respeto son clave."),
        ("=", "En una tienda de ejemplo, la entrada de Matías es a las 08:30, el atraso informado es de 20 minutos y la tienda abre al público a las 09:15. ¿Cuántos minutos antes de abrir llega?", "(9*60+15)-(8*60+30+20)", "Se compara la hora de apertura con la hora a la que llega, ambas en minutos.", " minutos"),
        ("abc", "El encargado de una bodega de ejemplo avisa a su jefe que faltan cartones. ¿Qué mensaje es el adecuado?", "«Sr. Rojas: quedan 12 cajas de cartón y se agotarían mañana. ¿Autoriza el pedido?»", "«Jefe, se acaba el cartón»", "«¡¡Urgente!! Nadie pidió el cartón, qué desorden»", "El mensaje adecuado es respetuoso, entrega cantidad y plazo y plantea una acción concreta."),
        ("abc", "Una recepcionista de ejemplo debe avisar por escrito a una visita de un cambio de sala. ¿Qué texto escribe?", "«Sr. Díaz: su reunión de las 10:00 se traslada a la sala 2, segundo piso. Disculpe la molestia»", "«Cambiamos la sala, suba nomás»", "«Sala 2, ahí nos vemos»", "El texto correcto trae trato cortés, hora y lugar; los otros dejan dudas o suenan descuidados."),
        ("abc", "Camila trabaja con su jefa desde hace años y se tratan con mucha confianza. Para un informe firmado que irá a un cliente, ¿qué registro usa Camila?", "Formal, aunque con su jefa converse de forma cercana", "Informal, porque con su jefa hay confianza", "Técnico y sin explicaciones, para ahorrar tiempo", "El registro depende de quién leerá el documento, no solo de la confianza entre quienes lo escriben."),
        ("abc", "Un cocinero de ejemplo escribe en el pizarrón de turno una sigla del oficio que los auxiliares nuevos aún no conocen. ¿Qué falla de comunicación hay?", "Usa una sigla técnica sin explicarla a quienes no la conocen", "Usa un registro demasiado formal", "Escribe un mensaje demasiado largo", "El problema es que el vocabulario técnico no se enseñó a todo el equipo."),
        ("abc", "{F} Un compañero propone enviar el mensaje A a la jefa «porque es más rápido». Matías duda. ¿Qué argumento es más sólido?", "Le faltan el trato respetuoso y el motivo, y la jefa los necesita para organizar la caja", "Es mejor enviar A porque la jefa también se ríe con la jerga", "Da lo mismo cuál se envíe si el atraso es el mismo", "El mensaje A no entrega el motivo ni muestra respeto, y la jefa necesita esos datos para decidir."),
        ("=", "Un equipo de ejemplo envía 9 avisos por día; 3 llegan con jerga y deben reescribirse. En una semana de 5 días, ¿cuántos avisos se envían bien a la primera?", "(9-3)*5", "Se restan los mal escritos de cada día y se multiplica por los días.", " avisos"),
    ],
    ctx=("abc", "{F} Hoy Matías debe escribir además a un proveedor que no conoce, para avisar que su pedido llegará un día tarde por el mismo problema de transporte. ¿Cómo escribe?", "En registro formal: saludo, motivo, nueva fecha y despedida cortés", "Con el mensaje A, porque ya lo escribió una vez", "Con una frase sola, «se atrasa un día», para no molestar", "Al proveedor se le escribe en registro formal con los datos que necesita para reorganizarse."),
    sc=[
        ("En comunicación laboral: ¿qué registro usas con un cliente que no conoces?", "El formal", "Con quien no hay confianza se usa trato respetuoso y claro."),
        ("¿Qué haces con una sigla del oficio si hablas con alguien que no la conoce?", "La explico o uso palabras simples", "Así la persona entiende la información que necesita."),
        ("¿Por qué conviene cuidar un mensaje de mensajería con tu jefa?", "Porque queda escrito y puede leerse después", "Los mensajes escritos dejan un registro de lo dicho."),
    ],
    op=("Caso de ejemplo. Eres auxiliar en un centro de salud ficticio. Debes dar tres mensajes: (1) avisar por mensaje a un compañero de turno que dejaste una carpeta sobre el mesón; (2) avisar por escrito a la jefa del centro que mañana llegarás 30 minutos más tarde por un trámite; (3) explicar de palabra a un usuario que no conoce el centro dónde queda el módulo de admisión. "
        "Escribe los tres mensajes, indica el registro de cada uno y una razón para tu elección.",
        "(1) «Dejé la carpeta azul sobre el mesón, por si la necesitas» — informal. (2) «Estimada Sra. Marta: le informo que mañana llegaré 30 minutos más tarde por un trámite personal. Dejaré mis tareas organizadas. Saludos cordiales» — formal. (3) «Con gusto: siga por el pasillo hasta el fondo; admisión queda a la derecha» — formal y con palabras simples.",
        ["elige un registro adecuado para cada interlocutor", "incluye los datos necesarios en cada mensaje", "explica la razón de cada elección"],
        ["hoja con los tres mensajes, el registro de cada uno y una razón"],
        ["usar jerga con la jefa", "no dar el motivo o la hora en el mensaje 2", "usar términos técnicos con el usuario"],
        "Pregunta: «¿cambiarías el mensaje 1 si la carpeta tuviera datos de pacientes?». La respuesta debe mencionar cuidar la confidencialidad y no dejarla a la vista."),
    reinforce="Escribe una misma noticia de tres formas: para un amigo, para tu jefa y para un cliente. Subraya qué palabras cambiaste.",
    extend="Explica con un ejemplo por qué un registro técnico puede ser correcto con un colega y equivocado con un cliente.",
)

# ============================================================ OAG-01, clase 2
F = ("Ficha 2 (correo de ejemplo). Para: Sr. Fuentes, jefe de bodega de «Distribuidora Costanera de Ejemplo». Asunto: «Solicitud». "
     "Texto: «Hola, necesito que me manden las cajas que faltan. Es urgente. Daniela». "
     "Datos del pedido de Daniela, encargada de una cafetería de ejemplo: se pidieron 120 cajas de vasos; llegaron 85; la cafetería necesita las restantes antes del viernes.")
build(
    G1, 2, F,
    use="Aprenderé a escribir correos y notas formales de trabajo con asunto, saludo, mensaje claro, cierre y firma.",
    prior=["Distingo el registro formal del informal.", "Sé restar.", "Sé qué es un correo electrónico."],
    explain=[
        "Un correo o una nota formal de trabajo tiene partes ordenadas. El asunto dice en pocas palabras de qué se trata (por ejemplo, «Faltante de 35 cajas de vasos»). El saludo usa el nombre y el cargo de la persona. El cuerpo entrega lo que pasó, lo que se pide y para cuándo. El cierre agradece y se despide con cortesía, y la firma incluye nombre, cargo y empresa.",
        "Para que el mensaje se entienda, usa frases cortas y una idea por párrafo. Incluye los datos que permiten actuar sin preguntar de nuevo: cantidades, fechas, lugares y números de pedido. Si adjuntas un archivo, nómbralo en el texto. Antes de enviar, relee: revisa la ortografía, los nombres y las cifras, porque un correo mal escrito puede retrasar el trabajo o dañar la imagen de la empresa.",
        "Cuida la privacidad: no pongas datos personales de clientes, pacientes o compañeros si no son necesarios, y verifica los destinatarios antes de enviar. Un correo de trabajo es un documento que queda guardado." + LIM,
    ],
    vocab=[("asunto", "línea que resume de qué trata el correo"), ("cuerpo", "parte del mensaje donde se explica lo que pasa y lo que se pide"), ("firma", "nombre, cargo y empresa de quien escribe"), ("adjunto", "archivo que se envía junto con el correo"), ("destinatario", "persona a quien va dirigido el mensaje"), ("faltante", "cantidad que no llegó o no está")],
    worked=[
        ("Escribir un asunto", "Una secretaria de ejemplo avisa que la reunión de planificación se cambia del martes al jueves. ¿Qué asunto es mejor: «Aviso» o «Cambio de la reunión de planificación al jueves»?", ["El asunto debe decir de qué se trata sin abrir el correo.", "El segundo trae el tema y el cambio."], "«Cambio de la reunión de planificación al jueves»"),
        ("Calcular un faltante", "Un taller de ejemplo pidió 60 rollos de papel y recibió 42. ¿Cuántos faltan?", ["Faltante = pedido − recibido.", "60 − 42 = 18."], "18 rollos"),
    ],
    mistakes=[("Escribir en el asunto «Hola» o dejarlo vacío.", "La persona no sabe de qué trata el correo ni cuánta prioridad darle, y puede perderse entre otros.", "Escribe un asunto breve y específico, con el tema y la acción."),
              ("Escribir «Es urgente» sin decir para cuándo.", "«Urgente» no es una fecha; cada persona lo entiende distinto y no sabe cuándo actuar.", "Indica una fecha u hora concreta: «lo necesitamos antes del viernes a las 12:00».")],
    T=[
        ("abc", "En correos de trabajo: ¿qué cumple el asunto?", "Resumir en pocas palabras de qué trata el correo", "Reemplazar el saludo al destinatario", "Contar todos los detalles del pedido", "El asunto da el tema para que el lector sepa de qué se trata; los detalles van en el cuerpo."),
        ("abc", "{F} ¿Qué parte del correo de Daniela es el asunto?", "«Solicitud»", "«Hola»", "«Es urgente»", "El asunto es la línea que se escribe aparte, antes del texto; las otras expresiones están dentro del cuerpo."),
        ("abc", "{F} ¿Qué dato del pedido Daniela no incluyó en su correo y era necesario?", "La cantidad de cajas que faltan y la fecha límite", "Un saludo al comienzo del mensaje", "La firma con su nombre al final", "El correo de Daniela ya tiene saludo y firma, pero no dice cuántas cajas faltan ni para cuándo; esos datos permiten actuar."),
        ("=", "{F} ¿Cuántas cajas de vasos faltan por llegar?", "120-85", "Al total pedido se le restan las cajas ya recibidas.", " cajas"),
        ("abc", "{F} ¿Qué asunto es el mejor para un correo corregido de Daniela?", "«Faltante de 35 cajas de vasos, pedido a entregar antes del viernes»", "«Hola, urgente»", "«Pedido»", "El mejor asunto indica el problema, la cantidad y el plazo; los otros no permiten priorizar."),
        ("abc", "Una asistente de oficina de ejemplo va a escribir al jefe de recursos humanos y no sabe su cargo exacto. ¿Qué hace antes de enviar?", "Verifica el nombre y el cargo en la lista de personal de la empresa", "Lo escribe como cree recordarlo", "Omite el saludo para no equivocarse", "Revisar nombre y cargo evita errores que dañan la imagen de la empresa."),
        ("abc", "Se debe escribir el cierre de un correo a un proveedor. ¿Cuál es adecuado?", "«Agradezco su respuesta. Saludos cordiales, Luis Peña, encargado de compras»", "«Chao, avísame no más»", "«Gracias» sin nombre ni cargo", "Un cierre cortés y con firma completa permite al proveedor saber quién escribe."),
        ("=", "Una oficina de ejemplo envía 14 correos por la mañana y 11 por la tarde. De ellos, 5 tenían el asunto vacío y debieron reenviarse con el asunto completo. ¿Cuántos correos salieron bien a la primera?", "14+11-5", "Se suman todos los correos enviados y se restan los que tuvieron que reenviarse.", " correos"),
        ("abc", "El encargado de una obra de ejemplo adjunta una planilla de materiales a un correo. ¿Qué debe incluir en el texto?", "Mencionar que adjunta la planilla y qué contiene", "Nada, porque el adjunto se explica solo", "Copiar toda la planilla dentro del correo", "Nombrar el adjunto evita que el lector lo pase por alto."),
        ("abc", "Un técnico de laboratorio clínico de ejemplo debe escribir a su jefa sobre una muestra mal rotulada. ¿Qué texto cuida la privacidad?", "Indicar el número de muestra y el problema, sin escribir el nombre del paciente", "Escribir el nombre completo y el diagnóstico del paciente", "Copiar a todo el personal del centro para que se enteren", "Los datos del paciente son confidenciales; con el número de muestra basta para identificarla."),
        ("abc", "Antes de presionar «enviar», Lorena relee su correo. ¿Qué revisa primero para evitar errores de fondo?", "Que los nombres, las cifras y las fechas sean correctos", "Que el correo sea lo más largo posible", "Que el color de la letra sea llamativo", "Los errores en cifras y fechas pueden causar pérdidas y retrasos."),
        ("abc", "{F} Un compañero sugiere corregir el correo de Daniela solo cambiando «Hola» por «Estimado Sr. Fuentes». ¿Qué observación es correcta?", "Mejora el saludo, pero siguen faltando el asunto específico, la cantidad y la fecha", "Con ese cambio el correo queda completo", "El saludo no es importante, solo importa la firma", "El saludo es solo una de las partes; el correo debe indicar qué falta y para cuándo."),
        ("=", "El pedido de otra cafetería de ejemplo fue de 200 cajas de servilletas. En dos entregas llegaron 75 y 90 cajas. ¿Cuántas cajas debe pedir por correo como faltante?", "200-75-90", "Al pedido total se le restan las dos entregas recibidas.", " cajas"),
    ],
    ctx=("abc", "{F} Daniela quiere reescribir el correo. Tiene dos borradores. Borrador 1: asunto «Faltante de 35 cajas de vasos», saludo «Estimado Sr. Fuentes», pedido de las cajas antes del viernes y firma con cargo. Borrador 2: asunto «Hola», saludo «Sr.», y «mándenme lo que falte, gracias». ¿Cuál envía?", "El borrador 1, porque tiene asunto específico, cantidad, plazo y firma", "El borrador 2, porque es más corto", "Ninguno: conviene llamar por teléfono sin dejar nada escrito", "El borrador 1 reúne las partes y datos que permiten actuar sin preguntar de nuevo."),
    sc=[
        ("En correos laborales: ¿qué debe decir el asunto?", "De qué trata el correo", "Ayuda a priorizar y a encontrar el mensaje después."),
        ("¿Qué dato evita escribir solo «es urgente»?", "Una fecha u hora concreta", "Cada persona entiende «urgente» de un modo distinto."),
        ("¿Qué haces antes de enviar un correo?", "Reviso destinatarios, cifras y ortografía", "Un error puede retrasar el trabajo o exponer datos."),
    ],
    op=("Caso de ejemplo. Eres encargado de una ferretería ficticia y un cliente (la constructora «Obras del Sur de Ejemplo») pidió 40 sacos de cemento (cantidad de ejemplo). Hoy llegaron solo 28 y el cliente los necesita el lunes a las 09:00. "
        "Escribe el correo formal al cliente: con asunto, saludo, cuerpo (qué pasó, cuántos faltan, qué propones), cierre y firma con nombre y cargo inventados.",
        "Asunto: «Entrega parcial de 28 sacos; faltan 12 para el lunes». Saludo: «Estimada Sra. Valdés:». Cuerpo: «Le informo que hoy llegaron 28 de los 40 sacos de cemento pedidos; faltan 12. Gestionaré que lleguen antes del lunes a las 09:00 y le confirmaré por correo mañana a las 12:00». Cierre: «Agradezco su comprensión. Saludos cordiales, Rodrigo Núñez, encargado de bodega».",
        ["incluye asunto específico", "indica correctamente cuántos sacos faltan", "propone un plazo concreto", "usa registro formal y firma"],
        ["correo escrito con las cinco partes"],
        ["calcular mal el faltante", "asunto vacío", "plazo sin hora o fecha", "tono informal"],
        "Pregunta: «¿qué harías si no puedes cumplir el plazo que prometiste?». Debe responder que avisa a tiempo, con una nueva fecha y una disculpa."),
    reinforce="Escribe tres asuntos específicos para tres situaciones distintas de tu especialidad y compáralos con «Aviso».",
    extend="Explica por qué un correo de trabajo se considera un documento y qué cuidado de privacidad implica.",
)

# ============================================================ OAG-01, clase 3
F = ("Ficha 3 (caso de ejemplo en una obra de edificación). El jefe de turno, Sr. Parra, dice a Tomás en medio de ruido de máquinas: «Lleva eso arriba antes de que llegue el camión». "
     "Tomás sube 6 sacos de yeso al segundo piso. El Sr. Parra se refería a las 4 cajas de rollos de cinta que estaban junto a la entrada y debían ir al tercer piso. El camión llegó a las 11:00; Tomás terminó de subir los sacos a las 10:50.")
build(
    G1, 3, F,
    use="Aprenderé a dar y recibir instrucciones orales con claridad: escuchar con atención, repetir para confirmar y preguntar cuando hay dudas.",
    prior=["Conozco los registros formal e informal.", "Sé restar horas.", "Sé que el ruido y el apuro dificultan entender."],
    explain=[
        "Una instrucción oral clara responde cuatro preguntas: qué hay que hacer, dónde, para cuándo y quién lo hace. Decir «eso» o «arriba» sin precisar deja espacio al error. Quien da la instrucción se asegura de que fue entendida; quien la recibe practica la escucha activa: mira a quien habla, no interrumpe, toma nota si es necesario y pregunta lo que no entiende.",
        "Una técnica útil es repetir con tus palabras lo que entendiste y pedir confirmación: «Entonces subo las cajas de cinta al tercer piso antes de las 11:00, ¿correcto?». Esto se llama parafraseo y confirma la instrucción. También hay barreras que dificultan la comunicación: el ruido, el apuro, la jerga, el cansancio y los prejuicios sobre quien habla. Se reducen buscando un lugar más tranquilo, hablando más despacio, usando palabras simples o escribiendo lo importante.",
        "En un trabajo con riesgos, una instrucción mal entendida puede causar un accidente; por eso, ante la duda, se pregunta antes de actuar. Preguntar no es mostrar debilidad, es cuidar el trabajo y a las personas." + LIM,
    ],
    vocab=[("instrucción", "indicación de qué hacer, dónde, para cuándo y quién lo hace"), ("escucha activa", "atender sin interrumpir y mostrar que se entiende"), ("parafraseo", "repetir con tus palabras lo entendido para confirmarlo"), ("barrera de comunicación", "algo que dificulta entender, como el ruido, el apuro o la jerga"), ("confirmar", "comprobar que ambas personas entendieron lo mismo")],
    worked=[
        ("Completar una instrucción", "Un jefe de cocina de ejemplo dice: «Pon eso en la cámara». ¿Qué datos faltan para que sea una instrucción clara?", ["Falta precisar qué es «eso» y para cuándo.", "También conviene decir quién lo hace si hay más personas."], "Qué producto, cuándo y quién"),
        ("Parafrasear", "Una supervisora de ejemplo dice a un ayudante: «Deja las carpetas azules en el estante 3 antes de las 15:00». ¿Cómo las parafrasea el ayudante?", ["Repite lo entendido con sus palabras.", "Termina pidiendo confirmación."], "«Dejo las carpetas azules en el estante 3 antes de las 15:00, ¿correcto?»"),
    ],
    mistakes=[("Asentir con la cabeza «para no quedar mal» sin haber entendido la instrucción.", "Si la entendió mal, el trabajo se hará mal y habrá retrabajo o riesgo.", "Pregunta lo que no entendiste o repite lo que entendiste para confirmarlo."),
              ("Dar una instrucción importante a gritos y sin repetirla, en medio del ruido.", "El ruido impide oír bien, y gritar no asegura que el mensaje se entienda.", "Acércate, usa palabras simples y confirma que la persona lo entendió.")],
    T=[
        ("abc", "En comunicación oral laboral: ¿qué es el parafraseo?", "Repetir con tus palabras lo entendido para confirmarlo", "Hablar más fuerte para que te oigan", "Anotar la instrucción en un cuaderno personal", "El parafraseo confirma la comprensión repitiendo con palabras propias; anotar o gritar no lo reemplazan."),
        ("abc", "{F} ¿Qué barrera de comunicación aparece en el caso?", "El ruido de las máquinas y una instrucción con palabras vagas", "Que Tomás no quería obedecer", "Que el Sr. Parra habló en un registro muy formal", "El caso dice que hay ruido y que el jefe usó «eso» y «arriba» sin precisar."),
        ("abc", "{F} ¿Qué palabras de la instrucción del Sr. Parra eran imprecisas?", "«eso» y «arriba»", "«camión» y «antes»", "«llegue» y «lleva»", "Ni «eso» ni «arriba» dicen qué objeto ni a qué piso; las otras palabras sí tienen un sentido concreto."),
        ("=", "{F} El camión llegó a las 11:00 y Tomás terminó de subir los sacos a las 10:50. ¿Cuántos minutos antes del camión terminó?", "(11*60)-(10*60+50)", "Se resta la hora en que terminó a la hora de llegada del camión, en minutos.", " minutos"),
        ("abc", "Una auxiliar de bodega de ejemplo recibe una instrucción larga con tres tareas. ¿Qué técnica la ayuda más a no olvidar ninguna?", "Anotar las tres tareas y confirmarlas con quien las dio", "Memorizarlas sin escribir nada", "Hacer solo la primera y preguntar por las otras después", "Anotar y confirmar reduce el olvido y los malentendidos."),
        ("abc", "{F} Si Tomás hubiera dicho «¿Qué cosa y a qué piso?», ¿qué habría logrado?", "Aclarar la instrucción antes de actuar", "Retrasar al jefe y molestarlo", "Demostrar que no sirve para el trabajo", "Preguntar a tiempo permite corregir la ambigüedad, que es el origen del error."),
        ("abc", "Una recepcionista de ejemplo escucha por teléfono el nombre «Pizarro», pero la línea está con ruido y duda si es «Pizarro» o «Pizarra». ¿Qué hace?", "Pide que lo deletree o lo repite para confirmar", "Anota el que le parece más probable", "Cuelga porque no se entiende", "Pedir que repita o deletree confirma el dato antes de anotarlo."),
        ("abc", "{F} El Sr. Parra quiere que el mensaje no se malentienda otra vez. ¿Qué instrucción es mejor?", "«Tomás, sube las 4 cajas de rollos de cinta de la entrada al tercer piso antes de las 11:00»", "«Tomás, sube lo que está abajo cuando puedas»", "«Tomás, lleva eso arriba, ya sabes cuál»", "La mejor instrucción precisa qué, dónde, para cuándo y quién; las otras repiten la ambigüedad."),
        ("=", "{F} Tomás subió 6 sacos de yeso. Si cada subida, en un carro de ejemplo, lleva 2 sacos, ¿cuántas subidas hizo?", "6//2", "Se divide el total de sacos entre los que lleva cada subida.", " subidas"),
        ("abc", "Un cocinero de ejemplo debe avisar de una novedad en medio del ruido de la cocina. ¿Qué hace?", "Se acerca, llama la atención de la persona y dice el mensaje con claridad", "Grita el mensaje desde la otra punta", "Deja el mensaje para el final del turno", "Acercarse reduce la barrera del ruido y asegura que el mensaje llegue."),
        ("abc", "Sofía repite al supervisor: «Entonces devuelvo la llave al encargado hoy a las 17:00». El supervisor había dicho «mañana a las 17:00». ¿Qué ocurrió gracias al parafraseo?", "Se detectó el error antes de actuar", "Se retrasó el trabajo sin razón", "Nada, porque el parafraseo no sirve", "Al repetir lo entendido apareció la diferencia, y se corrigió a tiempo."),
        ("abc", "{F} Un compañero dice: «Tomás tuvo la culpa por no entender». ¿Qué respuesta es más justa?", "Hubo responsabilidad compartida: la instrucción fue imprecisa y Tomás no confirmó", "La culpa es solo del Sr. Parra porque es el jefe", "La culpa es solo de Tomás porque debió adivinar", "El error nace de dos fallas: una instrucción vaga y la falta de confirmación."),
        ("=", "Un turno de ejemplo recibe 5 instrucciones orales por hora durante 6 horas, y se confirman con parafraseo solo 2 de cada 5. ¿Cuántas instrucciones no se confirman en el turno?", "5*6-2*6", "Se calcula el total de instrucciones y se restan las confirmadas.", " instrucciones"),
    ],
    ctx=("abc", "Una estudiante en práctica en un centro de salud de ejemplo recibe de la técnica en enfermería la indicación: «Llévale eso a la señora de la camilla». Hay tres personas en camilla y tres bandejas. ¿Qué hace?", "Pregunta qué bandeja y a quién, y repite lo entendido antes de moverse", "Elige la bandeja más cercana", "Espera sin hacer nada hasta que la técnica la corrija", "Ante una instrucción ambigua en un centro de salud, preguntar y confirmar evita errores con las personas."),
    sc=[
        ("En una obra o un taller de ejemplo: ¿qué cuatro datos tiene una instrucción clara?", "Qué, dónde, para cuándo y quién", "Con esos datos se puede actuar sin adivinar."),
        ("En el mundo del trabajo: ¿qué haces si no entiendes una instrucción?", "Pregunto antes de actuar", "Preguntar a tiempo evita errores, retrabajo y riesgos."),
        ("¿Cómo confirmas que entendiste?", "Repito con mis palabras y pido confirmación", "Así se verifica que ambos entendieron lo mismo."),
    ],
    op=("Caso de ejemplo en un taller de confección ficticio. La supervisora, Sra. Rojas, dice a una aprendiz: «Pasa esas telas a la mesa grande antes de la hora de almuerzo». Hay dos rollos de tela azul en una mesa, tres de tela blanca en otra, y hay dos mesas grandes. "
        "Escribe: (1) qué datos faltan en la instrucción, (2) tres preguntas que haría la aprendiz, (3) cómo parafrasearía, (4) cómo la supervisora habría dado la instrucción completa.",
        "(1) Faltan qué telas, a qué mesa y a qué hora. (2) «¿Cuáles telas, las azules o las blancas?», «¿A cuál de las dos mesas grandes?», «¿A qué hora es el almuerzo?». (3) «Entonces paso los dos rollos azules a la mesa grande 1 antes de las 13:00, ¿correcto?». (4) «Lucía, pasa los dos rollos azules a la mesa grande 1 antes de las 13:00».",
        ["detecta los datos que faltan", "formula preguntas útiles", "parafrasea con precisión", "reescribe la instrucción completa"],
        ["hoja con las cuatro respuestas"],
        ["no preguntar y suponer", "parafraseo sin confirmación", "instrucción sin hora o sin lugar"],
        "Pregunta: «¿qué harías si la supervisora está apurada y no responde?». Debe buscar otra forma de confirmar, como pedir que lo escriba, y no actuar a ciegas."),
    reinforce="Escribe tres instrucciones vagas de tu especialidad y reescríbelas indicando qué, dónde, para cuándo y quién.",
    extend="Explica con un ejemplo por qué escuchar activamente es parte de la seguridad en el trabajo.",
)

# ============================================================ OAG-01, clase 4
F = ("Ficha 4 (hojas de novedad de una bodega de alimentos de ejemplo). Versión 1: «Turno malo. El nuevo dejó todo botado y la cámara es un desastre, nadie ayuda». "
     "Versión 2: «Turno de tarde, día de ejemplo. A las 16:20 se encontró una caja de yogures abierta y 6 potes caídos en el pasillo 2. A las 16:35 se retiraron los potes y se limpió el piso. Avisó: Lucía Soto, bodeguera. No hubo personas lesionadas. Se pidió revisar el embalaje del proveedor». "
     "Un hecho es algo que se puede comprobar; una opinión es lo que alguien piensa o siente.")
build(
    G1, 4, F,
    use="Aprenderé a comunicar por escrito una novedad o incidente con hechos ordenados, datos precisos y sin acusaciones.",
    prior=["Escribo correos formales.", "Sé calcular duraciones de tiempo.", "Distingo registros formal e informal."],
    explain=[
        "Informar una novedad o un incidente por escrito es dejar un registro claro para que otras personas puedan decidir y actuar. Un buen informe breve responde: qué ocurrió, cuándo, dónde, quién lo detectó o participó, cómo se actuó y qué se pide o propone. Se ordena en el tiempo, de lo primero a lo último, con horas y cantidades concretas.",
        "Es importante separar los hechos de las opiniones. Un hecho se puede comprobar («6 potes caídos en el pasillo 2»); una opinión es lo que alguien piensa o siente («un desastre», «la culpa es del nuevo»). En un informe se escriben hechos, con un tono neutro y respetuoso, sin culpar a personas ni usar insultos. Si hay una causa probable, se escribe como hipótesis («podría deberse a...»).",
        "Si en el incidente hay personas lesionadas o en riesgo, lo primero es avisar de inmediato a quien corresponde. Los informes no deben incluir datos personales innecesarios, como diagnósticos de personas." + LIM,
    ],
    vocab=[("incidente", "hecho inesperado que altera el trabajo, con o sin daños"), ("hecho", "algo que se puede comprobar"), ("opinión", "lo que alguien piensa o siente sobre algo"), ("orden cronológico", "orden según el tiempo, de lo primero a lo último"), ("hipótesis", "explicación posible que aún no está comprobada"), ("informe breve", "texto corto que registra qué pasó, cuándo, dónde, quién, cómo se actuó y qué se pide")],
    worked=[
        ("Hecho u opinión", "Un cocinero de ejemplo escribe: «La fritura estaba mala». Otro escribe: «El aceite de la freidora tenía 9 días de uso». ¿Cuál es un hecho comprobable?", ["Un hecho se puede verificar con un dato.", "«Mala» es una apreciación; «9 días» es una cifra."], "El segundo: «El aceite tenía 9 días de uso»"),
        ("Duración de un incidente", "Una nota de ejemplo dice que una impresora falló a las 09:10 y se reparó a las 10:05. ¿Cuántos minutos estuvo fuera de servicio?", ["Se pasa todo a minutos o se cuenta de 09:10 a 10:05.", "De 09:10 a 10:00 son 50 minutos y de 10:00 a 10:05, 5 más."], "55 minutos"),
    ],
    mistakes=[("Escribir en el informe «el nuevo es un flojo y por su culpa pasó».", "Acusa sin pruebas, incluye una opinión ofensiva y no sirve para decidir qué corregir.", "Escribe los hechos con horas y cantidades, y propone revisar la causa."),
              ("Omitir la hora y el lugar del incidente.", "Sin ellos, nadie puede comprobar ni ubicar lo ocurrido.", "Siempre incluye cuándo y dónde, con la mayor precisión posible.")],
    T=[
        ("abc", "En registros de trabajo: ¿qué es un hecho?", "Algo que se puede comprobar con un dato o una observación", "Lo que alguien siente respecto de un compañero", "Una explicación que aún nadie ha revisado", "Un hecho es verificable; los sentimientos son opiniones y la explicación sin comprobar es una hipótesis."),
        ("abc", "{F} ¿Cuál de las dos versiones de la hoja de novedad es la más útil?", "La versión 2, porque entrega horas, cantidades y acciones", "La versión 1, porque es más corta", "Ambas, porque las dos avisan que hubo problemas", "La versión 2 permite saber qué pasó y cómo se actuó; la 1 solo expresa molestia."),
        ("abc", "{F} ¿Qué expresión de la versión 1 es una opinión?", "«un desastre»", "«cámara»", "«turno»", "«Un desastre» es una apreciación; «cámara» y «turno» solo nombran lugares o momentos."),
        ("=", "{F} Se encontró la caja a las 16:20 y se retiraron los potes a las 16:35. ¿Cuántos minutos pasaron entre ambos hechos?", "(16*60+35)-(16*60+20)", "Se restan las dos horas expresadas en minutos.", " minutos"),
        ("abc", "{F} ¿Qué dato permite ubicar el lugar del incidente de la versión 2?", "«pasillo 2»", "«turno de tarde»", "«Lucía Soto, bodeguera»", "El lugar es «pasillo 2»; el turno y la persona responden otras preguntas."),
        ("abc", "Una técnica en laboratorio de ejemplo debe registrar que se rompió un tubo de ensayo vacío. ¿Qué anotación es adecuada?", "«A las 11:40 se quebró un tubo vacío al caer de la gradilla; se avisó a la jefatura; sin personas lesionadas»", "«Me lo hicieron caer, qué descuidados»", "«Se rompió algo»", "La anotación adecuada tiene hora, hecho, aviso y estado de las personas, sin culpar."),
        ("abc", "{F} Una compañera propone agregar a la versión 2: «el proveedor siempre embala mal». ¿Qué es correcto?", "Escribir que podría deberse al embalaje y pedir revisarlo, porque no está comprobado", "Escribirlo como un hecho porque ya pasó otras veces", "No escribir nada sobre el embalaje", "Sin pruebas es una hipótesis; se redacta como posible causa y se pide revisar."),
        ("abc", "Una guardia de seguridad de ejemplo ve a un visitante caer por un resbalón en un pasillo húmedo. ¿Qué hace primero?", "Avisar de inmediato a quien corresponde para que atienda a la persona y luego registrar", "Terminar de escribir el informe antes de avisar", "Esperar a ver si la persona se levanta sola", "Si hay una persona en riesgo, se avisa primero; el informe se redacta después."),
        ("=", "Una oficina de ejemplo registró 18 incidentes en un trimestre; 7 tenían hora y lugar completos. ¿Cuántos informes quedaron incompletos?", "18-7", "Al total de informes se le restan los completos.", " informes"),
        ("abc", "Un informe de ejemplo dice: «A las 08:00 Pedro dejó la puerta abierta y como siempre es descuidado se perdió una caja». ¿Cómo se corrige?", "«A las 08:00 la puerta quedó abierta y faltó una caja; se solicita revisar el registro de entradas»", "«Pedro es descuidado, hay que sancionarlo»", "«Se perdió una caja por culpa de alguien»", "El informe corregido deja solo hechos y propone una revisión, sin acusar."),
        ("abc", "Un informe incluye el diagnóstico médico de una persona accidentada, que no era necesario. ¿Qué problema tiene?", "Expone datos personales sensibles sin necesidad", "Es demasiado corto", "Está escrito en orden cronológico", "Los datos de salud son sensibles y solo deben incluirse si es imprescindible."),
        ("abc", "{F} Si se quisiera completar la versión 2, ¿qué dato agregarías?", "La hora en que se avisó a la jefatura", "Una descripción de lo que sintió Lucía", "Una crítica al turno de la mañana", "La versión 2 no dice cuándo se avisó; ese dato sirve para seguir los hechos, mientras los sentimientos y las críticas no aportan."),
        ("=", "En una bodega de ejemplo se registraron 9 novedades por semana durante 4 semanas, y cada novedad bien redactada ahorra 15 minutos de consultas posteriores. Si todas estaban bien redactadas, ¿cuántos minutos se ahorraron?", "9*4*15", "Se multiplican las novedades por semana, las semanas y los minutos ahorrados.", " minutos"),
    ],
    ctx=("abc", "En un centro de salud de ejemplo, una auxiliar encuentra a las 09:05 una silla de ruedas con un freno que no funciona, en el pasillo 1. Aún nadie la ha usado. ¿Qué informe escribe?", "«A las 09:05 se encontró en el pasillo 1 una silla con un freno que no funciona; se la retiró de uso y se avisó a mantención»", "«La silla es un desastre y nadie la revisa nunca»", "«Hay algo malo en el pasillo»", "El informe correcto tiene hora, lugar, hecho, acción y aviso, sin opiniones."),
    sc=[
        ("En un informe de novedad: ¿qué se escribe, hechos u opiniones?", "Hechos", "Los hechos se pueden comprobar; las opiniones no ayudan a decidir."),
        ("¿Qué datos mínimos incluye un informe breve de un incidente?", "Qué, cuándo, dónde, quién, cómo se actuó y qué se pide", "Con eso otra persona puede decidir sin preguntar."),
        ("¿Qué haces primero si hay una persona en riesgo?", "Aviso de inmediato a quien corresponde", "Primero se protege a las personas y luego se escribe."),
    ],
    op=("Caso de ejemplo. En una cocina de un casino de ejemplo, a las 12:10 la ayudante Karen ve que una caja de verduras llegó con la tapa mojada y 3 bolsas rotas; se dejaron aparte y se avisó al jefe de cocina, Sr. Vera, a las 12:15. No hubo lesionados. "
        "Escribe un informe breve con: qué, cuándo, dónde, quién, qué se hizo y qué propones; mantén un tono neutro. Luego marca en tu informe un hecho y una opinión que habrías evitado.",
        "«Casino de ejemplo, cocina. A las 12:10 Karen, ayudante, detectó que una caja de verduras tenía la tapa mojada y 3 bolsas rotas. Se apartó la caja y a las 12:15 se avisó al jefe de cocina, Sr. Vera. No hubo lesionados. Se propone revisar el transporte con el proveedor». Hecho: «3 bolsas rotas». Opinión evitada: «el proveedor es un irresponsable».",
        ["incluye qué, cuándo, dónde, quién y acciones", "usa hechos y tono neutro", "propone una acción concreta", "distingue un hecho de una opinión"],
        ["hoja con informe de entre 4 y 6 líneas y la marca de hecho y opinión"],
        ["escribir opiniones o acusaciones", "omitir horas", "no proponer nada"],
        "Pregunta: «¿qué pasaría si el informe dijera que Karen fue descuidada?». Debe explicar que no hay pruebas y que el informe busca corregir el proceso."),
    reinforce="Escribe dos hechos y dos opiniones sobre una misma situación de tu especialidad y explica la diferencia.",
    extend="Explica por qué un informe sin acusaciones ayuda más a mejorar el trabajo del equipo.",
)

# ============================================================ OAG-02, clase 1
F = ("Ficha 5 (cinco documentos de ejemplo de una distribuidora ficticia). Documento 1: «Orden de trabajo OT-114. Tarea: ordenar el estante 4 de la bodega. Plazo: viernes 12:00. Responsable: Pía». "
     "Documento 2: «Instructivo de recepción de mercadería, versión 3, vigente desde marzo de ejemplo». Documento 3: «Ficha técnica de un carro de bodega de ejemplo: carga máxima 300 kg». "
     "Documento 4: «Memorándum interno: la bodega cerrará una hora antes el jueves por inventario». Documento 5: «Etiqueta de caja: 12 unidades. Mantener en lugar seco. No apilar más de 4 cajas».")
build(
    G2, 1, F,
    use="Aprenderé a reconocer los tipos de textos que se leen en el trabajo (orden de trabajo, instructivo, ficha técnica, memorándum, etiqueta) y para qué sirve cada uno.",
    prior=["Sé leer con atención.", "Sé usar fechas y horas.", "Sé que no todo texto sirve para lo mismo."],
    explain=[
        "En el trabajo se leen textos con propósitos distintos. La orden de trabajo encarga una tarea y fija responsable y plazo. El instructivo describe los pasos de una tarea; el manual explica cómo funciona o cómo se usa un equipo. La ficha técnica entrega datos de un producto o equipo, como su capacidad o sus medidas. El memorándum o la circular informa algo a las personas de la empresa. La etiqueta identifica un producto y da avisos de uso y almacenamiento.",
        "Antes de usar un documento, revisa cuatro datos: su título, quién lo emite, para quién es y si está vigente (versión y fecha). Un documento antiguo puede contener indicaciones que ya cambiaron. Lee el texto completo antes de actuar, porque las advertencias pueden estar al final. Si falta un dato, como un plazo, pregunta a quien emitió el documento.",
        "Leer un documento no te autoriza a hacer cualquier tarea. Si el texto habla de equipos o trabajos con riesgo, solo puede hacerlo personal capacitado y autorizado." + LIM,
    ],
    vocab=[("orden de trabajo", "documento que encarga una tarea y fija responsable y plazo"), ("instructivo", "documento que describe los pasos de una tarea"), ("ficha técnica", "documento con datos de un producto o equipo"), ("memorándum", "comunicación escrita interna para informar algo al personal"), ("etiqueta", "texto sobre un producto que lo identifica y da avisos de uso y almacenamiento"), ("vigente", "que está en uso y no ha sido reemplazado")],
    worked=[
        ("Reconocer el documento", "Un texto de ejemplo dice: «Tarea: etiquetar los 3 pasillos nuevos. Plazo: jueves 16:00. Responsable: Sofía». ¿Qué tipo de documento es?", ["Encarga una tarea y nombra responsable y plazo.", "Eso corresponde a una orden de trabajo."], "Una orden de trabajo"),
        ("Comprobar vigencia", "Un instructivo de ejemplo dice «versión 2, marzo» y en la carpeta hay otro «versión 4, septiembre». ¿Cuál se usa?", ["Se elige el más reciente y vigente.", "La versión 4 reemplaza a la 2."], "El de la versión 4"),
    ],
    mistakes=[("Leer solo el primer párrafo de un instructivo y comenzar la tarea.", "Las advertencias o los pasos clave pueden estar más abajo y se pasan por alto.", "Lee el documento completo antes de actuar."),
              ("Usar un instructivo antiguo porque «ya me lo sé».", "Puede haber cambiado un paso o una norma, y el trabajo quedaría mal hecho.", "Revisa que la versión sea la vigente.")],
    T=[
        ("abc", "En lectura de documentos del trabajo: ¿para qué sirve una orden de trabajo?", "Para encargar una tarea con responsable y plazo", "Para explicar cómo funciona un equipo", "Para informar un cambio a todo el personal", "La orden fija quién hace qué y para cuándo; explicar equipos es tarea del manual y avisar cambios es del memorándum."),
        ("abc", "{F} ¿Qué documento informa del cierre anticipado de la bodega?", "El memorándum interno (documento 4)", "La orden de trabajo (documento 1)", "La etiqueta de caja (documento 5)", "El memorándum comunica un aviso a todo el personal; la orden y la etiqueta cumplen otros fines."),
        ("abc", "{F} ¿Quién es la responsable de la tarea de la orden OT-114?", "Pía", "El jefe de bodega", "Quien recibe la mercadería", "La orden nombra a Pía como responsable; los otros cargos no aparecen en el documento."),
        ("abc", "{F} ¿Qué dato del documento 2 sirve para saber si el instructivo es el actual?", "La versión 3 y la fecha desde la que rige", "La palabra «recepción» del título", "El nombre de la bodega", "La versión y la fecha de vigencia muestran si el documento es el actual."),
        ("abc", "{F} ¿Qué información aporta la ficha técnica del carro de bodega?", "Un dato del equipo: su carga máxima", "Una tarea con plazo y responsable", "El horario de cierre de la bodega", "La ficha técnica entrega datos del equipo, como la carga máxima."),
        ("abc", "Un instructivo de ejemplo comienza con la frase «Antes de comenzar, lea todo el documento». ¿Qué conviene hacer?", "Leerlo completo antes de actuar, porque las advertencias pueden estar al final", "Leer solo el primer paso y seguir", "Leer únicamente las partes que ya conoce", "Las advertencias importantes pueden aparecer al final; saltarse partes expone a errores."),
        ("=", "{F} Hay 27 cajas iguales por guardar y la etiqueta permite apilar como máximo 4 cajas. ¿Cuántas pilas se necesitan, como mínimo?", "(27+3)//4", "Se divide entre 4 y la caja que sobra necesita otra pila.", " pilas"),
        ("abc", "{F} Hoy es lunes. ¿Qué plazo tiene Pía para la orden OT-114?", "Hasta el viernes a las 12:00", "Hasta el jueves, antes del inventario", "Hasta que cambie la versión del instructivo", "El plazo está escrito en la orden; el jueves corresponde al aviso de cierre anticipado."),
        ("abc", "Una orden de trabajo de ejemplo dice «Revisar las etiquetas del pasillo 2» y no indica plazo. ¿Qué corresponde?", "Preguntar a quien la emitió cuál es el plazo antes de comenzar", "Hacerlo cuando haya tiempo libre", "Dejarla para fin de mes", "Una orden sin plazo no se puede priorizar; se consulta al emisor."),
        ("abc", "{F} Un compañero dice: «El documento 4 no me importa, yo solo hago órdenes de trabajo». ¿Qué respuesta es correcta?", "El cierre anticipado puede cambiar los plazos de sus órdenes", "Tiene razón: cada documento afecta a una sola persona", "Solo importa si lo firmó el jefe en persona", "Un aviso general puede afectar el cumplimiento de cualquier tarea."),
        ("abc", "En la pared hay un instructivo de ejemplo versión 2 y en la carpeta uno nuevo, versión 3, con cambios. ¿Qué corresponde?", "Usar el vigente, versión 3, y avisar para retirar el antiguo", "Usar el de la pared porque está a la vista", "Combinar pasos de ambos según el gusto", "Solo el documento vigente refleja las reglas actuales."),
        ("abc", "El manual de un equipo de ejemplo dice «Uso solo por personal capacitado». Un compañero afirma: «Leí todo el manual, ya puedo usarlo». ¿Qué observación corresponde?", "Leer el manual no basta: se necesita capacitación y autorización", "Si lo leyó completo queda habilitado", "El manual es solo una guía y no exige nada", "El manual declara un requisito aparte de la lectura: capacitación del personal."),
        ("=", "Una empresa de ejemplo emitió en un mes 36 órdenes de trabajo, 5 instructivos, 12 fichas técnicas y 9 memorándums. ¿Cuántos documentos no fueron órdenes de trabajo?", "5+12+9", "Se suman todos los documentos que no son órdenes de trabajo.", " documentos"),
    ],
    ctx=("abc", "{F} Pía va a cumplir la OT-114 y ve en el estante 4 cinco cajas apiladas con la etiqueta del documento 5. ¿Qué debe hacer?", "Reordenar según la etiqueta (máximo 4 cajas) y dejar constancia de lo que cambió", "Dejar las cinco cajas, pues la orden solo dice ordenar", "Quitar la etiqueta para que no genere dudas", "La orden pide ordenar y la etiqueta fija un límite; ambas deben cumplirse."),
    sc=[
        ("En una bodega de ejemplo: ¿qué documento fija responsable y plazo de una tarea?", "La orden de trabajo", "Esos datos son la función de la orden de trabajo."),
        ("¿Qué revisas para saber si un instructivo está vigente?", "La versión y la fecha", "Una versión más antigua puede haber sido reemplazada."),
        ("¿Qué haces si falta un dato importante en un documento?", "Pregunto a quien lo emitió", "Suponer el dato puede llevar a un error."),
    ],
    op=("Caso de ejemplo. En una empresa ficticia de aseo y mantención llegan tres textos. A: «Circular: desde el lunes la entrega de uniformes será los miércoles, de 10:00 a 12:00». "
        "B: «Orden de trabajo OT-220. Tarea: inventariar 5 estantes. Plazo: martes 17:00. Responsable: Ignacio». C: «Etiqueta de caja: 24 unidades. Vence 08/2027. No exponer al sol». "
        "Para cada texto escribe qué tipo de documento es, para qué sirve y un dato que lo comprueba; luego escribe una pregunta que harías a la jefatura sobre la orden B.",
        "A: circular o memorándum; informa un cambio a todo el personal; dato: «desde el lunes... los miércoles». B: orden de trabajo; encarga una tarea; dato: responsable y plazo. C: etiqueta; identifica el producto y da avisos; dato: vencimiento y condición de almacenamiento. Pregunta: «¿Los estantes se inventarían todos el mismo día o hay un orden de prioridad?».",
        ["clasifica correctamente los tres textos", "justifica con un dato del texto", "formula una pregunta pertinente"],
        ["hoja con tres clasificaciones, tres justificaciones y una pregunta"],
        ["clasificar la etiqueta como orden", "no justificar con un dato", "preguntar algo que el texto ya dice"],
        "Pregunta: «¿qué texto cambia primero tu rutina de la semana?». Debe mencionar la circular de los uniformes o la orden con su plazo, y justificar."),
    reinforce="Escribe una lista de cinco documentos que se usan en tu especialidad y marca para qué sirve cada uno.",
    extend="Explica por qué dos documentos distintos pueden afectar la misma tarea y cómo decidir cuál manda si se contradicen.",
)

# ============================================================ OAG-02, clase 2
F = ("Ficha 6 (etiqueta de un aceite vegetal de ejemplo). Contenido neto: 900 mL por envase. Caja con 10 envases; peso de la caja completa: 11 kg. Vencimiento: 06/2027 (mes y año). "
     "Almacenar en lugar fresco y seco, lejos de fuentes de calor. Equivalencias de ejemplo: 1 kg = 1.000 g; 1 L = 1.000 mL; 1 m = 100 cm.")
build(
    G2, 2, F,
    use="Aprenderé a leer etiquetas, fichas técnicas y tablas con sus unidades, equivalencias y advertencias.",
    prior=["Sé multiplicar y dividir números enteros.", "Conozco gramos, kilos, litros y metros.", "Sé leer una tabla de doble entrada."],
    explain=[
        "Una etiqueta o ficha técnica entrega datos que hay que leer con cuidado. El contenido neto es la cantidad de producto sin contar el envase. La fecha de vencimiento indica hasta cuándo se puede usar; las condiciones de almacenamiento dicen cómo guardarlo; las advertencias y los símbolos informan de cuidados. Si un símbolo no lo conoces, no lo ignoras: preguntas a tu jefatura o a tu instructor y lees la hoja de seguridad del producto.",
        "Cada cifra va con su unidad, y no se pueden mezclar unidades distintas sin convertirlas. Para convertir, se usan equivalencias: 1 kg son 1.000 g, 1 L son 1.000 mL y 1 m son 100 cm. Para pasar de una unidad mayor a una menor se multiplica; de una menor a una mayor, se divide. Una masa (kg, g) mide cuánta materia hay; un volumen (L, mL) mide cuánto espacio ocupa.",
        "En una tabla de doble entrada, cada dato está en el cruce de una fila y una columna. Para leerlo, ubica primero la fila, luego la columna y lee la celda donde se cruzan." + LIM,
    ],
    vocab=[("contenido neto", "cantidad de producto sin contar el envase"), ("fecha de vencimiento", "fecha hasta la que se puede usar el producto"), ("unidad de medida", "patrón con el que se expresa una cantidad, como kg, L o m"), ("equivalencia", "relación entre dos unidades, como 1 kg = 1.000 g"), ("masa", "cantidad de materia, que se mide en g o kg"), ("volumen", "espacio que ocupa algo, que se mide en mL o L")],
    worked=[
        ("Convertir unidades", "Un envase de ejemplo contiene 3 kg de harina. ¿Cuántos gramos son?", ["Se pasa de una unidad mayor a una menor: se multiplica.", "3 × 1.000 = 3.000."], "3.000 g"),
        ("Leer una tabla", "Tabla de ejemplo (unidades por sucursal). Fila Este: lunes 14, martes 6. Fila Oeste: lunes 11, martes 9. ¿Cuántas unidades recibió Oeste el lunes?", ["Se ubica la fila Oeste y la columna lunes.", "En el cruce está el 11."], "11 unidades"),
    ],
    mistakes=[("Sumar 900 mL y 2 L directamente como «902».", "Son unidades distintas y no se pueden sumar sin convertir antes.", "Convierte 2 L a 2.000 mL y luego suma: 2.900 mL."),
              ("Leer la fecha 06/2027 como «seis de enero de 2027».", "En una etiqueta, ese formato indica mes y año, no día y mes.", "Interprétala como junio de 2027, según el formato de la etiqueta.")],
    T=[
        ("abc", "En etiquetas de producto: ¿qué indica el contenido neto?", "La cantidad de producto sin contar el envase", "El peso del envase vacío", "La fecha hasta la que sirve", "El contenido neto es solo el producto; el envase y la fecha son otros datos."),
        ("abc", "{F} ¿Hasta cuándo se puede usar el producto, según la etiqueta?", "Hasta junio de 2027", "Desde junio de 2027", "Hasta que se abra el envase", "La fecha de vencimiento marca el límite superior, no el comienzo del uso."),
        ("abc", "{F} ¿Cómo debe almacenarse el producto?", "En lugar fresco y seco, lejos de fuentes de calor", "En lugar seco, aunque quede junto a una fuente de calor", "En lugar fresco, aunque tenga humedad", "La etiqueta pide las dos condiciones a la vez, fresco y seco, y lejos del calor."),
        ("=", "{F} ¿Cuántos mililitros de aceite hay en 6 envases?", "900*6", "Se multiplica el contenido de un envase por el número de envases.", " mL"),
        ("=", "{F} ¿Cuántos litros de aceite hay en una caja completa?", "(10*900)//1000", "Se calculan los mL de la caja y se pasan a litros dividiendo por 1.000.", " L"),
        ("=", "Una etiqueta de ejemplo dice «Contenido: 2 kg». Una receta usa porciones de 500 g. ¿Cuántas porciones salen de un envase?", "(2*1000)//500", "Se convierten los kilos a gramos y se divide entre el tamaño de la porción.", " porciones"),
        ("abc", "Tabla de ejemplo (unidades recibidas): sucursal Norte, lunes 12 y martes 8; sucursal Sur, lunes 9 y martes 15. ¿Cuántas unidades recibió la sucursal Sur el martes?", "15", "8", "9", "Se cruza la fila Sur con la columna martes; 8 y 9 son otras celdas de la tabla."),
        ("=", "Un rollo de cinta de embalaje de ejemplo mide 4 m y se corta en tramos de 40 cm. ¿Cuántos tramos salen?", "(4*100)//40", "Se pasan los metros a centímetros y se divide entre el largo de cada tramo.", " tramos"),
        ("abc", "{F} Un bodeguero ve «11 kg» en la caja y «900 mL» en la etiqueta del envase. ¿Qué mide cada dato?", "11 kg es la masa de la caja completa y 900 mL el volumen de un envase", "Los dos miden lo mismo con unidades distintas", "11 kg es el volumen de la caja y 900 mL su masa", "Los kilogramos miden masa y los mililitros miden volumen."),
        ("abc", "En una ficha de producto de ejemplo aparece un símbolo de advertencia que el auxiliar no conoce. ¿Qué hace antes de manipular el producto?", "Pregunta a su jefatura o instructor y revisa la hoja de seguridad", "Lo ignora porque no está explicado", "Supone el significado por el dibujo", "Una advertencia que no se conoce se consulta, no se supone ni se ignora."),
        ("abc", "Dos fichas de ejemplo muestran una cantidad: una dice «1 L» y la otra «1.000 mL». ¿Qué conclusión es correcta?", "Es la misma cantidad expresada en unidades distintas", "Son cantidades distintas porque las cifras son diferentes", "No se pueden comparar nunca", "Como 1 L equivale a 1.000 mL, las dos fichas indican la misma cantidad."),
        ("abc", "{F} Un compañero lee la etiqueta en marzo de 2027 y dice: «Está vencido, porque el año 2027 ya comenzó». ¿Qué respuesta es correcta?", "No está vencido: vence en junio de 2027, que aún no llega", "Sí, porque 2027 ya empezó", "Sí, porque marzo es un mes anterior", "El vencimiento está en el mes indicado, no en el año completo."),
        ("=", "{F} Un pedido de ejemplo requiere 45 litros de aceite. ¿Cuántas cajas completas se necesitan?", "(45*1000)//(10*900)", "Se divide el volumen pedido en mL entre el volumen de una caja en mL.", " cajas"),
    ],
    ctx=("abc", "{F} Un nuevo bodeguero recibe 8 cajas del aceite y las deja junto a una estufa de la bodega porque «ahí hay espacio». ¿Qué corresponde?", "Moverlas a un lugar fresco y seco, según la etiqueta, y avisar a su jefatura", "Dejarlas, porque el aceite no se echa a perder", "Cubrirlas con cartón para protegerlas del calor", "La etiqueta pide almacenar lejos del calor; el espacio disponible no justifica incumplirlo."),
    sc=[
        ("En una etiqueta de ejemplo: ¿qué indica el contenido neto?", "La cantidad de producto sin el envase", "Es el dato que se usa para calcular cuánto producto hay."),
        ("¿Cómo pasas de kilogramos a gramos?", "Multiplicando por 1.000", "Un kilogramo equivale a mil gramos."),
        ("¿Qué haces con un símbolo de advertencia que no conoces?", "Pregunto a mi jefatura o instructor", "Un símbolo desconocido no se supone, se consulta."),
    ],
    op=("Caso de ejemplo. Una cocina de un casino de ejemplo recibe esta etiqueta: «Arroz de ejemplo. Contenido neto: 5 kg. Caja con 4 sacos. Vence 11/2027. Almacenar en lugar seco, cerrado y lejos de la humedad». "
        "Escribe: (1) cuántos gramos tiene un saco, (2) cuántos kilos tiene la caja, (3) hasta cuándo puede usarse, (4) dos condiciones de almacenamiento, (5) una pregunta que harías si ves un símbolo que no conoces.",
        "(1) 5.000 g. (2) 4 × 5 = 20 kg. (3) Hasta noviembre de 2027. (4) Lugar seco y cerrado, lejos de la humedad. (5) «¿Qué significa este símbolo y dónde veo la hoja de seguridad del producto?».",
        ["convierte bien las unidades", "interpreta la fecha mes/año", "extrae las condiciones de almacenamiento", "formula una pregunta pertinente"],
        ["hoja con las cinco respuestas y sus cálculos"],
        ["leer 11/2027 como día y mes", "multiplicar mal los sacos", "ignorar el símbolo desconocido"],
        "Pregunta: «¿qué pasa si el saco se moja?». Debe relacionar la humedad con la condición de almacenamiento y avisar a la jefatura, sin improvisar."),
    reinforce="Busca en tu casa la etiqueta de un alimento y escribe contenido neto, vencimiento y una condición de almacenamiento; no abras ni pruebes el producto.",
    extend="Explica con un ejemplo por qué mezclar unidades sin convertir puede llevar a un pedido equivocado.",
)

# ============================================================ OAG-02, clase 3
F = ("Ficha 7 (circular de ejemplo N.º 7). De: Jefatura de Administración. Para: todo el personal de «Comercial Andes del Sur de Ejemplo». Asunto: cambio de horario de almuerzo. "
     "A partir del lunes 4, el almuerzo será en dos turnos rotativos: el turno A, de 13:00 a 13:45, y el turno B, de 13:45 a 14:30. Cada área informará a la jefatura, hasta el miércoles 30, qué personas irán en cada turno. "
     "Las consultas se envían al correo de Administración. El horario será vigente por tres meses y luego se evaluará.")
build(
    G2, 3, F,
    use="Aprenderé estrategias para leer textos del trabajo: identificar propósito y destinatario, ideas principales, datos clave y significado de palabras nuevas.",
    prior=["Reconozco tipos de documentos laborales.", "Sé calcular duraciones de tiempo.", "Sé subrayar y resumir."],
    explain=[
        "Leer un texto del trabajo con eficacia sigue tres momentos. Antes de leer, mira el título, el asunto, quién escribe y a quién va dirigido para anticipar el propósito. Durante la lectura, subraya fechas, cantidades, nombres y plazos, y marca lo que no entiendes. Después de leer, resume con tus palabras la idea principal y anota qué debes hacer tú y para cuándo.",
        "La idea principal es lo más importante que dice el texto; los detalles la completan, como horas o ejemplos. Para entender una palabra nueva, usa el contexto: las palabras que la rodean dan pistas. Por ejemplo, si el texto dice que un turno es «rotativo» y que los grupos se van turnando, deduces que cambia entre grupos. Si el contexto no alcanza, busca el significado en un glosario o pregunta.",
        "Cuando dos partes de un documento se contradicen o falta información, no adivines: consulta a quien lo emitió. Una buena lectura permite actuar con seguridad y evita errores costosos." + LIM,
    ],
    vocab=[("propósito", "razón por la que se escribió el texto"), ("destinatario", "persona o grupo a quien va dirigido el texto"), ("idea principal", "lo más importante que dice un texto"), ("detalle", "dato que completa la idea principal"), ("contexto", "palabras y situación que rodean una palabra y ayudan a entenderla"), ("rotativo", "que cambia o se turna entre personas o grupos")],
    worked=[
        ("Idea principal y detalle", "Un aviso de ejemplo dice: «El jueves se hará el inventario; por eso la bodega cerrará a las 17:00». ¿Cuál es la idea principal?", ["La idea principal es el hecho central.", "La hora de cierre es un detalle que lo completa."], "Se hará un inventario el jueves"),
        ("Significado por contexto", "Un texto de ejemplo dice: «El pago será mensual, es decir, una vez al mes». ¿Qué significa «mensual»?", ["La frase que sigue lo explica.", "Se deduce a partir del contexto."], "Que ocurre una vez al mes"),
    ],
    mistakes=[("Subrayar casi todo el texto para «no perder nada».", "Al marcar todo, no se distingue lo importante y el resumen se vuelve imposible.", "Subraya solo fechas, cantidades, nombres y la idea principal."),
              ("Leer solo el título de una circular y actuar según lo que se imagina.", "El detalle puede cambiar lo que realmente se debe hacer o para cuándo.", "Lee el texto completo y confirma la tarea con tus propias palabras.")],
    T=[
        ("abc", "En lectura de textos laborales: ¿qué conviene identificar antes de leer el detalle?", "El propósito, el destinatario y el asunto", "El número de palabras del texto", "La última línea del documento", "El propósito y el destinatario orientan la lectura; contar palabras no ayuda a entender."),
        ("abc", "{F} ¿Cuál es el asunto de la circular?", "Cambio de horario de almuerzo", "Evaluación del personal", "Consultas por correo", "El asunto está escrito de forma explícita en el encabezado de la circular."),
        ("abc", "{F} ¿A quién va dirigida la circular?", "A todo el personal de la empresa", "Solo a la Jefatura de Administración", "Únicamente a los jefes de área", "El encabezado dice «Para: todo el personal»; la jefatura de Administración es quien escribe."),
        ("abc", "{F} Según el contexto, ¿qué significa que los turnos sean «rotativos»?", "Que cambian o se turnan entre grupos", "Que son obligatorios para todos al mismo tiempo", "Que duran tres meses", "La circular reparte al personal en dos turnos, lo que indica que se alternan."),
        ("abc", "{F} ¿Cuál es la idea principal de la circular?", "El almuerzo pasa a dos turnos y cada área debe informar quién irá en cada uno", "El turno B dura 45 minutos", "El horario será evaluado en tres meses", "Los otros enunciados son detalles que completan el cambio principal."),
        ("=", "{F} ¿Cuántos minutos dura el turno B de almuerzo?", "(14*60+30)-(13*60+45)", "Se restan la hora de inicio a la de término, ambas en minutos.", " minutos"),
        ("abc", "Para no olvidar fechas y responsables de una circular, ¿qué técnica conviene?", "Subrayar o anotar fechas y responsables en un resumen aparte", "Memorizarlos sin anotarlos", "Pedir a otro compañero que los recuerde por ti", "Anotar lo esencial deja un registro confiable y permite revisarlo."),
        ("abc", "{F} ¿Hasta cuándo debe informar cada área quiénes irán en cada turno?", "Hasta el miércoles 30", "Hasta el lunes 4", "Hasta que pasen los tres meses", "El lunes 4 es cuando parte el horario; el plazo para informar es el miércoles 30."),
        ("=", "{F} Un área de 24 personas reparte 5 de cada 8 en el turno A. ¿Cuántas personas van en el turno B?", "24-24*5//8", "Se calcula el grupo del turno A y se resta del total del área.", " personas"),
        ("abc", "{F} Un compañero resume: «Habrá un solo turno de almuerzo, de 13:00 a 14:30». ¿Qué error tiene su resumen?", "Ignora que son dos turnos rotativos de 45 minutos cada uno", "Cambió el asunto de la circular", "No menciona el correo de consultas", "La circular crea dos turnos; un solo bloque de 90 minutos cambia el sentido del cambio."),
        ("abc", "Un documento de ejemplo dice en un párrafo «la capacitación será el martes» y en otro «la capacitación será el jueves». ¿Qué haces?", "Consulto a quien lo emitió antes de actuar", "Elijo la fecha que me acomoda", "Asumo que vale la más antigua", "Si el texto se contradice no se adivina: se confirma con quien lo emitió."),
        ("abc", "{F} El texto dice que el horario «será vigente por tres meses y luego se evaluará». ¿Qué se infiere?", "Que después de ese tiempo podría mantenerse o cambiar según la evaluación", "Que durará para siempre", "Que ya no rige desde el lunes 4", "«Evaluará» indica que se revisará al final del plazo, sin asegurar su continuidad."),
        ("=", "{F} Antes del cambio el almuerzo duraba 60 minutos al día. Con el turno B, ¿cuántos minutos menos de almuerzo tiene una persona en una semana de 5 días?", "(60-45)*5", "Se calcula la diferencia diaria y se multiplica por los cinco días.", " minutos"),
    ],
    ctx=("abc", "{F} Marta es jefa de un área de 12 personas y entiende que solo debe informar quién irá en el turno A. ¿Cuál es la lectura correcta?", "Debe informar el turno de cada persona, A o B, hasta el miércoles 30", "Solo debe informar el turno A, porque el B es automático", "Debe esperar a que Administración asigne los turnos", "La circular pide informar quién irá en cada turno, no solo en el A."),
    sc=[
        ("En lectura de textos laborales: ¿qué es la idea principal?", "Lo más importante que dice el texto", "Los detalles la completan, pero no la reemplazan."),
        ("¿Cómo deduces una palabra nueva?", "Con las pistas del contexto", "Las palabras cercanas suelen explicar el significado."),
        ("¿Qué haces si dos partes del texto se contradicen?", "Consulto a quien lo emitió", "Elegir sin confirmar puede llevar a un error."),
    ],
    op=("Caso de ejemplo. Lee esta nota de una clínica veterinaria ficticia: «Nota N.º 3. Para: asistentes. Asunto: nuevo sistema de turnos de aseo. Desde el viernes 8, el aseo del salón de espera será por turnos semanales rotativos entre las cuatro asistentes: Ana, Bea, Carla y Dora, en ese orden, partiendo por Ana. Quien termina su semana entrega al cuarto día hábil un breve registro firmado a la encargada. Dudas, con la encargada». "
        "Escribe: el propósito, el destinatario, la idea principal, dos detalles, el significado de «rotativos» por contexto y una pregunta que harías.",
        "Propósito: informar el nuevo sistema de turnos. Destinatarios: las asistentes. Idea principal: el aseo del salón se reparte en turnos semanales rotativos. Detalles: orden Ana, Bea, Carla, Dora, y registro firmado a la encargada. «Rotativos»: que se turnan. Pregunta: «¿Qué pasa si una asistente se ausenta en su semana?».",
        ["identifica propósito y destinatario", "distingue idea principal y detalles", "deduce el significado por contexto", "formula una pregunta pertinente"],
        ["hoja con los seis elementos"],
        ["confundir idea principal con detalle", "copiar el texto sin resumir", "inventar datos"],
        "Pregunta: «¿qué semana le toca a Dora?». Debe responder la cuarta semana, contando el orden del texto."),
    reinforce="Elige un aviso real de tu liceo, subraya fechas y responsables y escribe la idea principal en una línea.",
    extend="Explica con un ejemplo por qué subrayar todo el texto es lo mismo que no subrayar nada.",
)

# ============================================================ OAG-02, clase 4
F = ("Ficha 8 (planilla de entrega de turno de una bodega de ejemplo). Producto / stock registrado / stock contado / estado. "
     "Cajas de guantes de ejemplo / 40 / 40 / OK. Rollos de cinta / 25 / 22 / Diferencia. Bolsas de basura / 60 / 63 / Diferencia. Cartón corrugado / 18 / 18 / OK. "
     "Regla de la planilla: toda diferencia se anota con la hora y se informa a la jefatura antes de cerrar el turno. Cierre del turno: 18:00.")
build(
    G2, 4, F,
    use="Aprenderé a usar la información de planillas y documentos para decidir qué hacer, calcular diferencias y detectar datos que faltan o se contradicen.",
    prior=["Leo tablas de doble entrada.", "Sé restar y sumar cantidades.", "Sé reconocer tipos de documentos laborales."],
    explain=[
        "Una planilla organiza datos en filas y columnas para compararlos. En una planilla de inventario, el stock registrado es lo que el sistema o el papel dice que hay, y el stock contado es lo que se cuenta realmente. La diferencia entre ambos se calcula restando; si el contado es menor, hay faltante; si es mayor, hay sobrante. Cada planilla trae reglas, como anotar la hora de cada diferencia e informar a la jefatura.",
        "Para usar un documento en una decisión, sigue tres pasos: lee el dato, compáralo con la regla o la meta, y decide qué acción corresponde. Anota lo que observas tal como es, no lo que esperabas. Si una celda está vacía, si dos documentos se contradicen o si no sabes qué hacer, consulta a la jefatura y deja constancia por escrito.",
        "Una planilla bien llenada es evidencia de lo que pasó. Alterar un registro para que «cuadre» es una falta grave de honestidad." + LIM,
    ],
    vocab=[("planilla", "documento que organiza datos en filas y columnas"), ("stock", "cantidad de un producto que hay en bodega"), ("stock registrado", "cantidad que dice el registro"), ("stock contado", "cantidad que se cuenta realmente"), ("faltante", "cuando lo contado es menor que lo registrado"), ("sobrante", "cuando lo contado es mayor que lo registrado")],
    worked=[
        ("Calcular una diferencia", "En una planilla de ejemplo, el registro dice 50 resmas y se contaron 47. ¿Hay faltante o sobrante y de cuánto?", ["Se resta lo contado a lo registrado.", "50 − 47 = 3 y lo contado es menor."], "Faltante de 3 resmas"),
        ("Aplicar una regla", "La regla de otra planilla dice: «Anotar la hora de toda diferencia». Se halla una diferencia a las 16:30. ¿Qué se anota?", ["Se anota la diferencia y la hora observada.", "La hora es 16:30."], "La diferencia con la hora 16:30"),
    ],
    mistakes=[("Anotar en «stock contado» el mismo número del registro para «no complicarse».", "Falsea la información y oculta un problema real.", "Anota siempre el conteo real, aunque no coincida."),
              ("Dejar una celda vacía y suponer que es cero.", "Puede ser un dato que falta; suponerlo cambia el resultado.", "Pregunta a quien llenó la planilla y completa el dato.")],
    T=[
        ("abc", "En planillas de inventario: ¿qué indica la columna «estado»?", "Si lo contado coincide con lo registrado o hay diferencia", "Quién contó el producto", "A qué hora se contó el producto", "La columna estado resume si hay coincidencia o diferencia entre registro y conteo."),
        ("abc", "{F} ¿Cuántos rollos de cinta se contaron?", "22", "25", "3", "El conteo es la tercera columna; 25 es lo registrado y 3 es la diferencia."),
        ("abc", "{F} ¿Qué productos presentan diferencia?", "Rollos de cinta y bolsas de basura", "Cajas de guantes y cartón corrugado", "Solo los rollos de cinta", "La columna estado marca diferencia en cinta y bolsas; guantes y cartón coinciden."),
        ("=", "{F} ¿Cuántas unidades se contaron en total entre los cuatro productos?", "40+22+63+18", "Se suman los cuatro valores de la columna de stock contado.", " unidades"),
        ("abc", "{F} Según la regla de la planilla, ¿qué debe hacerse con las diferencias?", "Anotarlas con la hora e informarlas a la jefatura antes de cerrar", "Corregir el registro sin avisar", "Esperar al próximo inventario para informarlas", "La planilla exige anotar la hora e informar antes del cierre del turno."),
        ("abc", "Una celda de una planilla de ejemplo aparece con un guion en lugar de un número. ¿Qué haces?", "Pregunto a quien la llenó y completo el dato", "Supongo que es cero", "Borro la fila completa", "Una celda sin dato no vale cero: se pregunta a quien la llenó."),
        ("=", "Una bodega de ejemplo cuenta 5 cajas de 24 unidades cada una más 7 unidades sueltas. El registro dice 130 unidades. ¿Cuántas unidades faltan?", "130-(5*24+7)", "Se calcula lo contado y se resta del registro, porque el contado es menor.", " unidades"),
        ("abc", "{F} Hay que informar a la jefa la diferencia de las cintas. ¿Qué anotación cumple con la regla?", "«17:40, rollos de cinta: faltan 3 (registrado 25, contado 22)»", "«Rollos de cinta: hay diferencia»", "«Faltan cosas en la bodega»", "La anotación completa trae hora, producto, cantidad y los dos valores comparados."),
        ("abc", "Dos documentos de ejemplo se contradicen: la planilla manda contar cada 2 horas y el instructivo cada 3 horas. ¿Qué haces?", "Consulto a la jefatura cuál rige y lo dejo por escrito", "Hago siempre el más fácil", "Cuento cada 2 y cada 3 horas a la vez", "Ante una contradicción entre documentos, se consulta quién define cuál manda."),
        ("abc", "{F} Un compañero propone anotar 25 en «stock contado» de las cintas para no complicarse con el informe. ¿Qué corresponde?", "Anotar el conteo real, 22, y avisar la diferencia", "Anotar 25 porque coincide con el registro", "Dejar la celda vacía", "La planilla debe reflejar lo observado, aunque genere trabajo adicional."),
        ("abc", "{F} ¿Qué NO permite saber la planilla?", "Por qué faltan 3 rollos de cinta", "Cuántas cajas de guantes se contaron", "Qué productos coinciden con el registro", "La planilla muestra el dato, pero no la causa de la diferencia."),
        ("=", "{F} Cada rollo de cinta cuesta $1.200 (precio de ejemplo). ¿Cuál es el valor del faltante de rollos?", "(25-22)*1200", "Se calcula el faltante y se multiplica por el precio de cada rollo.", " pesos"),
        ("abc", "{F} A las 17:50, faltando 10 minutos para el cierre, un compañero sugiere dejar el informe de diferencias para mañana. ¿Qué corresponde?", "Informar hoy, porque la regla exige hacerlo antes de cerrar el turno", "Dejarlo para mañana porque queda poco tiempo", "Corregir la planilla para que no haya diferencia", "La regla establece plazo hasta el cierre del turno, sin excepciones por falta de tiempo."),
    ],
    ctx=("abc", "{F} Faltan 3 rollos de cinta. Al revisar, la jefa pregunta: «¿Dónde pueden estar?». ¿Qué respuesta es correcta?", "«La planilla no lo dice; propongo revisar los despachos de hoy y avisarle»", "«Seguro se los llevó alguien del turno anterior»", "«No importa, son pocos»", "Sin evidencia no se acusa; se propone revisar registros."),
    sc=[
        ("En una bodega de ejemplo: ¿cómo se calcula una diferencia de inventario?", "Restando el stock contado al registrado", "La resta muestra si hay faltante o sobrante."),
        ("¿Qué anotas en la planilla: lo que esperabas o lo que contaste?", "Lo que conté", "La planilla es evidencia de lo que realmente ocurrió."),
        ("¿Qué haces si dos documentos se contradicen?", "Consulto a la jefatura", "Ella decide cuál de los documentos rige."),
    ],
    op=("Caso de ejemplo. En la planilla de entrega de turno de una farmacia ficticia (solo datos de ejemplo), un auxiliar anota: Cajas de mascarillas, registradas 30, contadas 28; Termómetros, registrados 12, contados 12; Alcohol gel en frascos, registrados 20, contados 23. Regla: toda diferencia se anota con hora y se informa a la encargada. Hora actual: 17:35. "
        "Escribe: (1) qué productos tienen faltante y cuáles sobrante, (2) las diferencias, (3) el texto que anotarías, (4) una pregunta a la encargada.",
        "(1) Faltante: mascarillas; sobrante: alcohol gel; coincide: termómetros. (2) Mascarillas: faltan 2; alcohol gel: sobran 3. (3) «17:35, mascarillas: faltan 2 (registradas 30, contadas 28); alcohol gel: sobran 3 (registrados 20, contados 23)». (4) «¿Hubo ventas o ingresos recientes sin registrar?».",
        ["calcula bien cada diferencia", "clasifica faltante y sobrante", "aplica la regla con la hora", "formula una pregunta pertinente"],
        ["hoja con cuatro respuestas y cálculos"],
        ["invertir faltante y sobrante", "no anotar la hora", "acusar a una persona"],
        "Pregunta: «¿qué harías si al volver a contar el alcohol gel fueran 20?». Debe corregir el conteo y dejar constancia del reconteo."),
    reinforce="Inventa una planilla de ejemplo con tres productos, calcula las diferencias y escribe la anotación que cumpliría la regla.",
    extend="Explica por qué falsear un registro es más grave que informar una diferencia.",
)

# ============================================================ OAG-03, clase 1
F = ("Ficha 9 (lista de verificación de entrega de un taller de costura de ejemplo, «Taller Aguja de Ejemplo»). Criterios: 1) costuras rectas y sin hilos sueltos; 2) largo dentro de la tolerancia de la orden (± 2 cm, valor de ejemplo); "
     "3) etiqueta cosida con la talla correcta; 4) prenda doblada y en bolsa; 5) prenda limpia, sin manchas. Orden OT-31: 20 pantalones talla M, largo 100 cm.")
build(
    G3, 1, F,
    use="Aprenderé a realizar tareas de forma prolija: ordenada, completa y según el estándar de calidad que pide la empresa o el cliente.",
    prior=["Sé leer una orden de trabajo.", "Sé restar y multiplicar enteros.", "Sé qué es una medida y una unidad."],
    explain=[
        "Trabajar de forma prolija es hacer una tarea completa, ordenada y sin errores evitables, cuidando también la presentación. Para saber si una tarea está bien hecha se usa un estándar de calidad: el nivel que la empresa, el cliente o la norma exigen. Ese estándar suele bajarse a criterios concretos, que se revisan con una lista de verificación, es decir, una lista de puntos que se marcan uno a uno.",
        "Una medida casi nunca puede ser exacta, por eso se fija una tolerancia: el margen permitido por encima o por debajo de la medida pedida. Si un largo pedido es 100 cm con tolerancia de ± 2 cm, se acepta entre 98 y 102 cm. Trabajar prolijo incluye mantener el puesto ordenado y limpio, usar los materiales con cuidado y dejar un registro de lo hecho.",
        "Cumplir el plazo no reemplaza la calidad: ambas forman parte de lo que se entrega. Si no puedes cumplir un criterio, lo informas a tiempo en lugar de ocultarlo." + LIM,
    ],
    vocab=[("estándar de calidad", "nivel o criterio que debe cumplir un producto o servicio"), ("criterio", "punto concreto que se revisa para saber si algo está bien hecho"), ("lista de verificación", "lista de criterios que se marcan al revisar un trabajo"), ("tolerancia", "margen permitido por encima o por debajo de una medida"), ("registro", "anotación escrita de lo que se hizo o se revisó"), ("prolijo", "ordenado, completo y cuidadoso")],
    worked=[
        ("Calcular un rango de tolerancia", "Un tablero de ejemplo debe medir 50 cm con tolerancia de ± 1 cm. ¿Entre qué medidas se acepta?", ["El mínimo es 50 − 1 y el máximo es 50 + 1.", "49 y 51."], "Entre 49 cm y 51 cm"),
        ("Usar una lista de verificación", "Un auxiliar de ejemplo marca 4 de los 5 criterios de una lista y deja uno sin marcar. ¿Puede entregar el trabajo como terminado?", ["La lista está completa solo si se cumplen todos los criterios.", "Falta revisar o corregir el criterio sin marcar."], "No, hasta cumplir y marcar el criterio que falta"),
    ],
    mistakes=[("Entregar una tarea a tiempo pero con la mesa de trabajo sucia y los materiales desordenados «porque otro la limpia».", "Deja trabajo extra a otra persona y puede afectar la calidad del siguiente turno.", "Deja tu puesto ordenado y limpio antes de irte."),
              ("Marcar todos los criterios de la lista sin haberlos revisado.", "La lista pierde su valor como evidencia y los errores llegan al cliente.", "Revisa cada criterio antes de marcarlo.")],
    T=[
        ("abc", "En producción y servicios: ¿qué es un estándar de calidad?", "El nivel que un producto o servicio debe cumplir", "El horario de entrega de un producto", "La opinión del compañero de turno", "El estándar fija lo que se espera del trabajo; el horario y las opiniones son otros datos."),
        ("abc", "{F} ¿Qué revisa el criterio 2?", "Que el largo esté dentro de la tolerancia de la orden", "Que las costuras sean rectas", "Que la etiqueta tenga la talla correcta", "El criterio 2 habla del largo y la tolerancia; los otros revisan costuras y etiqueta."),
        ("abc", "{F} Una prenda llega al embalaje arrugada y suelta. ¿Qué criterio incumple?", "El criterio 4", "El criterio 1", "El criterio 5", "El criterio 4 pide la prenda doblada y en bolsa; el 5 solo exige que esté limpia."),
        ("abc", "{F} Tres pantalones miden: A, 99 cm; B, 102 cm; C, 97 cm. ¿Cuáles cumplen el criterio 2?", "A y B", "B y C", "Solo A", "El rango aceptado va de 98 a 102 cm; 97 cm queda fuera."),
        ("=", "{F} De los 20 pantalones, 3 tienen hilos sueltos y 2 tienen la talla de la etiqueta equivocada (ninguno tiene ambos defectos). ¿Cuántos cumplen estos dos criterios?", "20-3-2", "Se restan del total los que fallan en cada criterio, sin repetir ninguno.", " pantalones"),
        ("abc", "Una cocinera de ejemplo termina su turno y deja la mesa con restos y utensilios sin lavar «porque otro turno la limpia». ¿Qué falla hay en su trabajo?", "No deja su puesto ordenado y limpio al terminar", "Cocinó más de lo necesario", "Llegó tarde a su turno", "Dejar el puesto sucio traslada trabajo a otros y afecta la calidad del siguiente turno."),
        ("abc", "Un asistente administrativo de ejemplo entrega un informe con cifras correctas, pero con hojas desordenadas y sin numerar. ¿Qué estándar incumple?", "El de orden y presentación del documento", "El de exactitud de las cifras", "Ninguno, porque las cifras están bien", "La exactitud está bien, pero la presentación también forma parte de la calidad."),
        ("abc", "{F} Marcela revisa una prenda y ve que la etiqueta dice talla L, pero la orden pide talla M. ¿Qué corresponde?", "Corregir la etiqueta antes de entregar", "Entregarla y avisar después", "Quitar la etiqueta para que no se note", "Se corrige antes de entregar para cumplir lo pedido; ocultar el error no lo resuelve."),
        ("=", "Una imprenta de ejemplo entrega 250 afiches y detecta que 1 de cada 10 tiene manchas. ¿Cuántos afiches no tienen manchas?", "250-250//10", "Se calcula la décima parte con manchas y se resta del total.", " afiches"),
        ("abc", "Un jefe de ejemplo dice: «Mientras llegue a tiempo, no importa cómo quede». ¿Qué respuesta es correcta?", "El plazo es necesario, pero la calidad también es parte de lo que se entrega", "Tiene razón: el plazo es lo único que importa", "La calidad importa y el plazo no", "Un trabajo entregado a tiempo pero mal hecho no cumple el compromiso con el cliente."),
        ("abc", "Rodrigo revisó los 20 pantalones, pero no anotó nada en la lista de verificación. ¿Qué problema tiene?", "No queda evidencia de que la revisión se hizo", "Ninguno, mientras él sepa que lo hizo", "Solo falta ordenar la mesa", "Sin registro, nadie más puede comprobar que se revisó."),
        ("abc", "{F} Una compañera dice que el criterio de las manchas «es cosa de gusto». ¿Qué argumento es correcto?", "Está escrito en la lista, así que se cumple siempre y no depende del gusto", "Tiene razón: cada persona decide qué es una mancha", "Solo importa si el cliente lo reclama", "Un criterio escrito en la lista es un estándar de la empresa, no una opinión."),
        ("=", "En un día de ejemplo se confeccionaron 14 pantalones por hora durante 6 horas y en el control salieron 12 con defectos. ¿Cuántos pantalones quedaron sin defectos?", "14*6-12", "Se calcula el total confeccionado y se restan los defectuosos.", " pantalones"),
    ],
    ctx=("abc", "{F} Faltan 15 minutos para el despacho y Marcela encuentra 4 pantalones con hilos sueltos. ¿Qué hace?", "Corregirlos y volver a revisarlos, e informar si el atraso afecta la entrega", "Despacharlos igual para cumplir la hora", "Separarlos sin decir nada a nadie", "Se corrige el defecto y se informa a tiempo; despachar con defectos o callar no cumple el estándar."),
    sc=[
        ("En un taller de ejemplo: ¿qué es la tolerancia de una medida?", "El margen permitido sobre o bajo la medida pedida", "Permite aceptar medidas que no son exactas pero sirven."),
        ("En el mundo del trabajo: ¿para qué sirve una lista de verificación?", "Para revisar uno a uno los criterios de calidad", "Ayuda a no olvidar criterios y deja evidencia."),
        ("¿Cómo dejas tu puesto al terminar la tarea?", "Ordenado y limpio", "El puesto ordenado forma parte del trabajo prolijo."),
    ],
    op=("Caso de ejemplo. En la cocina de un jardín infantil ficticio, la encargada pide dejar lista una bandeja de 12 vasos con agua para la hora de colación. Criterios de ejemplo: 1) vasos limpios; 2) cada vaso con la misma cantidad; 3) bandeja ordenada y limpia; 4) entrega a las 10:30. "
        "Escribe: (1) una lista de verificación con esos criterios, (2) qué harías si encuentras un vaso con una marca de suciedad, (3) cómo dejarías el puesto al terminar, (4) a quién avisarías si no alcanzas a las 10:30.",
        "(1) Lista: vasos limpios; misma cantidad en cada vaso; bandeja ordenada y limpia; entrega a las 10:30. (2) Cambio ese vaso por uno limpio y vuelvo a revisar. (3) Dejo la mesa limpia y los utensilios guardados. (4) Aviso a la encargada apenas veo que no llego, con una hora nueva.",
        ["lista con los cuatro criterios", "acción correcta ante un defecto", "orden del puesto", "aviso oportuno"],
        ["hoja con la lista y tres respuestas breves"],
        ["marcar criterios sin revisar", "ocultar el defecto", "avisar tarde"],
        "Pregunta: «¿qué pasa si todos los vasos tienen un poco más o un poco menos?». Debe hablar de tolerancia o de nivelar y volver a revisar."),
    reinforce="Escribe una lista de verificación de cinco criterios para una tarea de tu especialidad.",
    extend="Explica con un ejemplo por qué una tarea a tiempo pero con baja calidad puede salir más cara.",
)

# ============================================================ OAG-03, clase 2
F = ("Ficha 10 (plan de trabajo de ejemplo para ordenar y rotular una bodega pequeña). Tareas: A) contar y registrar existencias, 3 horas; B) rotular estantes, 2 horas (solo puede comenzar cuando A termina); "
     "C) reubicar cajas, 4 horas (solo puede comenzar cuando B termina); D) limpiar pasillos, 1 hora (puede hacerse en cualquier momento). Trabaja una sola persona, de 09:00 a 18:00, con una hora de almuerzo de 13:00 a 14:00. Entrega: mañana a las 12:00.")
build(
    G3, 2, F,
    use="Aprenderé a planificar una tarea: dividirla en pasos, ordenarlos, estimar su duración, priorizar y avisar con tiempo si hay riesgo de atraso.",
    prior=["Sé calcular horas y duraciones.", "Sé sumar y restar enteros.", "Sé leer una orden de trabajo con plazo."],
    explain=[
        "Planificar es decidir qué se hará, en qué orden, quién lo hará y cuánto tardará. Primero se divide el trabajo en tareas. Luego se ve cuáles tienen dependencia, es decir, cuáles no pueden comenzar hasta que otra termine, y cuáles son independientes y pueden hacerse en cualquier momento. Después se estima la duración de cada una y se suman las horas necesarias.",
        "Para saber si se llega al plazo, se calcula el tiempo disponible, descontando almuerzo y pausas, y se compara con el tiempo necesario. La diferencia es la holgura: el tiempo que sobra como reserva. Si no hay holgura, cualquier atraso afecta la entrega. Para elegir qué hacer primero se prioriza según urgencia (qué vence pronto) e importancia (qué tiene mayor efecto).",
        "Si detectas que no llegarás al plazo, avisa de inmediato y propone una nueva fecha. Ocultar un atraso solo lo hace más difícil de resolver." + LIM,
    ],
    vocab=[("dependencia", "relación en que una tarea no puede comenzar hasta que otra termine"), ("tarea independiente", "tarea que puede hacerse en cualquier momento"), ("duración", "tiempo que tarda una tarea"), ("holgura", "tiempo de reserva que sobra al comparar lo disponible con lo necesario"), ("plazo", "fecha u hora límite para entregar"), ("prioridad", "orden de importancia con que se hacen las tareas")],
    worked=[
        ("Sumar las duraciones", "Un trabajo de ejemplo tiene tres tareas: 2 h, 3 h y 1 h. ¿Cuántas horas necesita en total?", ["Se suman las duraciones.", "2 + 3 + 1 = 6."], "6 horas"),
        ("Calcular la holgura", "Una persona tiene 9 horas disponibles y necesita 7 horas para el trabajo. ¿Cuál es la holgura?", ["Holgura = disponible − necesario.", "9 − 7 = 2."], "2 horas"),
    ],
    mistakes=[("Estimar la duración de una tarea sin contar el tiempo de almuerzo ni las pausas.", "El plan parece posible en papel, pero en la práctica falta tiempo.", "Calcula el tiempo disponible descontando almuerzo y pausas."),
              ("Avisar el atraso el mismo día de la entrega.", "Quien espera el trabajo ya no puede reorganizarse.", "Avisa en cuanto detectes el riesgo y propón una nueva fecha.")],
    T=[
        ("abc", "En planificación del trabajo: ¿qué es una dependencia entre tareas?", "Cuando una tarea no puede comenzar hasta que otra termine", "Cuando dos personas hacen la misma tarea", "Cuando una tarea dura más que otra", "La dependencia habla del orden obligatorio, no de quién la hace ni de cuánto dura."),
        ("abc", "{F} ¿Qué tarea solo puede comenzar cuando termina la tarea A?", "La tarea B", "La tarea C", "La tarea D", "La ficha dice que B espera a A; C espera a B y D es independiente."),
        ("abc", "{F} ¿Qué tarea puede hacerse en cualquier momento?", "La tarea D", "La tarea A", "La tarea C", "Solo D no depende de otra, por eso puede ubicarse donde convenga."),
        ("=", "{F} ¿Cuántas horas de trabajo suman las cuatro tareas?", "3+2+4+1", "Se suman las duraciones de las cuatro tareas.", " horas"),
        ("=", "{F} ¿Cuántas horas efectivas de trabajo hay en un día, descontando el almuerzo?", "(18-9)-1", "Se calculan las horas entre la entrada y la salida y se resta la hora de almuerzo.", " horas"),
        ("=", "{F} ¿Cuántas horas de trabajo hay disponibles entre las 09:00 de hoy y las 12:00 de mañana?", "(18-9-1)+(12-9)", "Se suman las horas efectivas de hoy y las de mañana hasta la hora de entrega.", " horas"),
        ("=", "{F} ¿Cuántas horas de holgura quedan al comparar el tiempo disponible con el necesario?", "(18-9-1)+(12-9)-(3+2+4+1)", "La holgura es el tiempo disponible menos el tiempo que exige el trabajo.", " hora"),
        ("abc", "{F} Si A comienza hoy a las 09:00, ¿a qué hora termina?", "A las 12:00", "A las 13:00", "A las 11:00", "Con una duración de 3 horas desde las 09:00 termina a las 12:00, antes del almuerzo."),
        ("abc", "{F} ¿Cuál es el orden obligatorio de las tareas dependientes?", "A, luego B y luego C", "C, luego B y luego A", "B, luego A y luego C", "Cada tarea espera a la anterior, y por eso el orden es A, B, C."),
        ("abc", "Una oficinista de ejemplo debe elegir qué hace primero: (1) responder a un cliente cuyo plazo vence hoy, (2) ordenar el estante de papelería que no tiene plazo, (3) revisar un correo informativo sin fecha. ¿Qué prioriza?", "Responder al cliente cuyo plazo vence hoy", "Ordenar el estante porque es más fácil", "Revisar el correo informativo porque ya lo abrió", "Lo urgente y con efecto en un cliente va primero que lo que no tiene plazo."),
        ("abc", "{F} Un compañero propone empezar por C «porque es la tarea más larga». ¿Qué respuesta es correcta?", "No se puede: C depende de B y B depende de A", "Sí, las tareas largas siempre van primero", "Sí, porque D es corta y puede esperar", "La dependencia obliga a respetar el orden aunque la tarea sea larga."),
        ("abc", "Un encargado de ejemplo ve que su trabajo se atrasará dos días por una falla ajena. ¿Cuándo debe avisar al cliente?", "En cuanto lo detecta, con una nueva fecha propuesta", "El día de la entrega", "Solo si el cliente pregunta", "Avisar a tiempo permite que el cliente se reorganice."),
        ("abc", "{F} Si la tarea A tarda 1 hora más de lo planificado, ¿qué ocurre con la entrega de mañana a las 12:00?", "Aún se cumple, pero sin holgura: se terminaría justo a las 12:00", "Se pasa del plazo por una hora", "No cambia nada, porque D es independiente", "La hora extra consume la holgura que había, de modo que el trabajo terminaría justo en el plazo."),
    ],
    ctx=("abc", "{F} Hoy a las 12:00, al terminar A, descubres que los rótulos para B llegarán recién mañana a las 09:00. ¿Qué haces?", "Aviso hoy a la jefatura que la entrega de las 12:00 de mañana no se podrá cumplir, hago D mientras tanto y propongo una nueva hora", "Espero sin hacer nada hasta mañana", "Rotulo con papeles cualquiera sin avisar", "Con B retrasada se pierde la holgura; se avisa de inmediato, se aprovecha el tiempo con la tarea independiente y se propone una nueva hora."),
    sc=[
        ("En una bodega de ejemplo: ¿qué es una tarea independiente?", "La que puede hacerse en cualquier momento", "No depende de que otra tarea termine antes."),
        ("En el mundo del trabajo: ¿cómo se calcula la holgura?", "Tiempo disponible menos tiempo necesario", "Muestra cuánto tiempo sobra como reserva."),
        ("¿Cuándo avisas de un atraso?", "En cuanto lo detecto", "Avisar pronto permite reorganizar el trabajo."),
    ],
    op=("Caso de ejemplo. Debes preparar el salón de una escuela de capacitación ficticia para un curso que comienza mañana a las 09:00. Tareas: A) retirar y guardar los materiales anteriores, 1 hora; B) limpiar el piso y las mesas, 2 horas (después de A); C) disponer 30 sillas y 15 mesas, 2 horas (después de B); D) preparar las carpetas de los participantes, 1 hora (en cualquier momento). Jornada: hoy de 14:00 a 18:00, sin almuerzo. "
        "Calcula las horas necesarias, indica el orden, decide si alcanzas hoy y, si no, qué avisarías y a quién.",
        "Horas necesarias: 1 + 2 + 2 + 1 = 6. Hoy hay 4 horas (14:00 a 18:00). Orden: A, B, C y D en cualquier momento. Hoy se avanza A (14–15), B (15–17) y D (17–18); C queda para mañana temprano, pero el curso empieza a las 09:00. Aviso a la encargada que C requiere 2 horas y propongo llegar a las 07:00 mañana o pedir ayuda.",
        ["suma correctamente las horas", "respeta las dependencias", "detecta que no alcanza", "propone un aviso y una solución"],
        ["hoja con cálculo, orden, conclusión y aviso"],
        ["ignorar las dependencias", "no avisar", "no calcular el tiempo disponible"],
        "Pregunta: «¿qué cambiaría si llega una segunda persona?». Debe explicar qué tareas se podrían hacer a la vez sin romper las dependencias."),
    reinforce="Divide una tarea de tu especialidad en cuatro pasos, marca cuál depende de cuál y estima la duración de cada uno.",
    extend="Explica con un ejemplo por qué una planificación sin holgura es riesgosa.",
)

# ============================================================ OAG-03, clase 3
F = ("Ficha 11 (control de un lote en una imprenta de ejemplo, «Gráfica Norte de Ejemplo»). Lote de 200 tarjetas de presentación. Criterios: colores correctos, texto sin errores, corte recto y cantidad exacta. "
     "Muestra revisada: 20 tarjetas; 1 con error en el teléfono; 2 con corte torcido; 17 sin defectos. Regla de ejemplo: si la muestra tiene 3 o más tarjetas con defectos, se detiene el lote y se revisa completo.")
build(
    G3, 3, F,
    use="Aprenderé a controlar la calidad de mi trabajo: revisar una muestra, detectar no conformidades, informar errores y buscar su causa.",
    prior=["Sé qué es un estándar de calidad.", "Sé calcular partes de un total.", "Sé que ocultar un error empeora el problema."],
    explain=[
        "El control de calidad es revisar que un producto o servicio cumpla los criterios acordados. Cuando es imposible revisar todo, se revisa una muestra, es decir, una parte del lote. Un producto o servicio que no cumple un criterio es una no conformidad. Se decide qué hacer según la regla de la empresa: corregir (retrabajo), apartar, descartar o detener el lote. Retrabajo es volver a hacer o corregir algo para que cumpla.",
        "Cada trabajador practica el autocontrol: revisa su propio trabajo antes de pasarlo al siguiente. Cuando aparece un error, no basta corregirlo: hay que buscar la causa raíz, que es la razón de fondo que lo originó, preguntando «¿por qué?» varias veces. Si la causa está en la plantilla, la máquina o el proceso, se corrige ahí para que no se repita. Los errores se informan y se registran, sin culpar a personas.",
        "Una forma simple de medir defectos es la proporción por cada 100 piezas: defectuosas multiplicadas por 100 y divididas entre el total revisado." + LIM,
    ],
    vocab=[("control de calidad", "revisión de que algo cumple los criterios acordados"), ("muestra", "parte del lote que se revisa"), ("no conformidad", "producto o servicio que no cumple un criterio"), ("retrabajo", "volver a hacer o corregir algo para que cumpla"), ("causa raíz", "razón de fondo que originó un error"), ("autocontrol", "revisión que cada trabajador hace de su propio trabajo")],
    worked=[
        ("Calcular defectos por cada 100", "En un lote de ejemplo se revisan 50 piezas y 4 tienen defectos. ¿Cuántas defectuosas hay por cada 100 revisadas?", ["Se multiplica por 100 y se divide entre las revisadas.", "4 × 100 ÷ 50 = 8."], "8 por cada 100"),
        ("Aplicar la regla de un lote", "Regla de ejemplo: si en la muestra hay 5 o más piezas con defectos, se detiene el lote. En una muestra aparecen 4. ¿Qué se hace?", ["Se compara 4 con el límite de 5.", "4 es menor que 5, así que no se detiene el lote."], "No se detiene el lote, pero se corrigen las 4 piezas"),
    ],
    mistakes=[("Mezclar una pieza defectuosa con las buenas para que no se note.", "El defecto llega al cliente y la empresa pierde confianza y dinero.", "Aparta la pieza, regístrala y avisa a quien corresponde."),
              ("Corregir cada pieza una por una sin preguntarse por qué se repite el error.", "El error seguirá apareciendo mientras la causa no se corrija.", "Busca la causa raíz y corrígela en el origen.")],
    T=[
        ("abc", "En control de calidad: ¿qué es una no conformidad?", "Un producto o servicio que no cumple un criterio", "Un reclamo del cliente sin fundamento", "Una instrucción que el trabajador no entiende", "Es el incumplimiento de un criterio establecido, sea de producto o de servicio."),
        ("abc", "{F} ¿Qué es la muestra en este control?", "Las 20 tarjetas que se revisaron", "Las 200 tarjetas del lote", "Las 3 tarjetas con defectos", "La muestra es la parte del lote que se revisa, no el lote ni solo los defectos."),
        ("=", "{F} ¿Cuántas tarjetas de la muestra tienen algún defecto?", "1+2", "Se suman la tarjeta con error de texto y las dos con corte torcido.", " tarjetas"),
        ("abc", "{F} Según la regla de ejemplo, ¿qué debe hacerse con el lote?", "Detenerlo y revisarlo completo", "Entregarlo y corregir las 3 tarjetas", "Descartar solo las 20 tarjetas de la muestra", "La regla pide detener y revisar todo cuando hay 3 o más defectuosas."),
        ("=", "{F} ¿Cuántas tarjetas defectuosas hay por cada 100 revisadas en la muestra?", "3*100//20", "Se multiplican las defectuosas por 100 y se divide entre las revisadas.", " por cada 100"),
        ("abc", "Un cocinero de ejemplo advierte que una salsa quedó distinta al estándar de la receta de la empresa. ¿Qué corresponde?", "Apartarla, avisar al responsable y registrar la no conformidad", "Mezclarla con otra salsa para que no se note", "Servirla igual y esperar si hay reclamos", "Apartar, avisar y registrar evita que el producto llegue al cliente."),
        ("abc", "En una lavandería de ejemplo, una camisa sale con una mancha que debía quedar limpia. Volver a lavarla es un caso de…", "Retrabajo", "Muestra", "Tolerancia", "El retrabajo es repetir o corregir lo que no cumplió el criterio."),
        ("=", "En una imprenta de ejemplo, corregir una tarjeta con corte torcido toma 5 minutos. Si hay 14 tarjetas así, ¿cuántos minutos de retrabajo se necesitan?", "14*5", "Se multiplica el tiempo de corrección por el número de tarjetas.", " minutos"),
        ("abc", "Un operario revisa el archivo de impresión y ve que el teléfono está mal escrito en el diseño original, por lo que se repetirá en todas las tarjetas. ¿Cuál es la mejor acción?", "Detener, corregir el diseño original y avisar al responsable", "Corregir a mano tarjeta por tarjeta sin tocar el diseño", "Imprimir todo y esperar a ver si alguien reclama", "El error nace en el archivo original, y corregirlo allí evita repetirlo."),
        ("abc", "Dos trabajadoras descubren el mismo error: una lo oculta para evitar un reto y la otra lo informa. ¿Qué diferencia tiene para la empresa?", "Informarlo permite corregir la causa antes de que el error llegue al cliente", "Ocultarlo ahorra trabajo a todos", "No hay diferencia si el error es pequeño", "Un error informado se puede corregir; uno oculto puede repetirse y llegar al cliente."),
        ("abc", "Una bodega de ejemplo tuvo 3 despachos con producto equivocado. Preguntando «¿por qué?»: se confundieron las etiquetas, porque se imprimieron iguales, porque la plantilla no distingue los productos. ¿Cuál es la causa raíz?", "La plantilla de etiquetas no distingue entre productos", "El despachador se confundió", "Las etiquetas se imprimieron iguales", "La causa raíz es la última razón de la cadena de «¿por qué?»; confundirse y que las etiquetas salgan iguales son consecuencias de ella."),
        ("abc", "{F} La jefa dice: «Con 17 buenas de 20 estamos bien; entreguemos». ¿Qué observación corresponde?", "La regla de ejemplo exige detener y revisar el lote cuando hay 3 o más defectuosas, y aquí hay 3", "Tiene razón: 17 de 20 es suficiente", "Debe entregarse solo si el cliente no mira", "La regla fija un límite de 3 defectuosas y la muestra lo alcanza, así que no se entrega sin revisar."),
        ("=", "Un lote de ejemplo de 400 piezas se revisa completo: aparecen 28 con defectos y se logran reparar 12. ¿Cuántas piezas quedan que no cumplen el estándar?", "28-12", "A las defectuosas se les restan las que se pudieron reparar.", " piezas"),
    ],
    ctx=("abc", "En un centro de salud de ejemplo, una auxiliar rotula 30 tubos de muestra y al revisar su propio trabajo nota que 2 tienen el rótulo ilegible. ¿Qué hace?", "Rehace los rótulos, anota lo ocurrido y revisa por qué se emborronaron", "Los entrega esperando que se entiendan", "Los esconde al fondo de la caja", "El autocontrol detecta el error antes de que cause confusión con las muestras."),
    sc=[
        ("En una imprenta de ejemplo: ¿qué es la muestra?", "Una parte del lote que se revisa", "Permite evaluar un lote sin revisar todas las piezas."),
        ("¿Qué es el retrabajo?", "Corregir o rehacer para que cumpla", "Busca que el producto final cumpla el criterio."),
        ("¿Qué haces con un error que descubres?", "Lo informo y busco su causa", "Informarlo permite corregirlo en el origen."),
    ],
    op=("Caso de ejemplo. Una panadería ficticia produjo 120 panes de molde para un pedido. En la revisión de una muestra de 20 panes, 3 están más pequeños que el estándar (peso de ejemplo) y 1 tiene la bolsa rota. Regla de ejemplo: si la muestra tiene 3 o más panes defectuosos, se revisa todo el pedido. "
        "Escribe: (1) cuántos panes defectuosos hay en la muestra, (2) qué dice la regla, (3) por cada 100 panes revisados, cuántos son defectuosos, (4) una posible causa raíz del pan pequeño y cómo la buscarías, (5) qué informarías por escrito.",
        "(1) 3 + 1 = 4. (2) 4 es mayor que 3, así que se revisa todo el pedido. (3) 4 × 100 ÷ 20 = 20 por cada 100. (4) Posible causa: cantidad de masa por pan; se busca preguntando por qué se pesó distinto y revisando la porción. (5) «Hora, cantidad de panes, defectos, acción: se detuvo el pedido y se propone revisar la porción».",
        ["cuenta bien los defectuosos", "aplica la regla", "propone causa raíz", "redacta un informe sin culpar"],
        ["hoja con cinco respuestas"],
        ["no sumar la bolsa rota", "ignorar la regla", "culpar a una persona"],
        "Pregunta: «¿qué harías si la balanza pesó mal?». Debe proponer revisar el instrumento y volver a medir antes de descartar panes."),
    reinforce="Describe un error común de tu especialidad y escribe tres «¿por qué?» seguidos hasta llegar a una posible causa raíz.",
    extend="Explica por qué informar un error ayuda más que ocultarlo, incluso si causa molestia.",
)

# ============================================================ OAG-03, clase 4
F = ("Ficha 12 (registro semanal de un equipo de digitación de ejemplo). Meta diaria: 50 documentos, con un máximo de 5 errores por cada 100 documentos (regla de ejemplo). "
     "Lunes: 60 documentos, 3 errores. Martes: 50 documentos, 2 errores. Miércoles: 100 documentos, 10 errores. Jueves: 40 documentos, 0 errores.")
build(
    G3, 4, F,
    use="Aprenderé a medir el cumplimiento de metas de plazo, cantidad y calidad con datos, y a decidir qué mejorar sin alterar los registros.",
    prior=["Sé calcular una proporción por cada 100.", "Sé restar y multiplicar.", "Sé leer un registro semanal."],
    explain=[
        "Un indicador es un dato calculado que muestra cómo va el trabajo. La meta es el valor que se espera alcanzar. El cumplimiento se obtiene comparando lo realizado con la meta. Hay indicadores de cantidad (cuántos documentos se hicieron), de calidad (cuántos errores hubo) y de plazo (si se entregó a tiempo). Un trabajo bien hecho cumple los tres.",
        "Para comparar errores entre días con distinto volumen, se usa la proporción por cada 100 documentos: errores multiplicados por 100 y divididos entre los documentos del día. Si una persona hace más documentos pero con más errores proporcionales, no necesariamente trabajó mejor. Los datos se usan para detectar qué mejorar, no para culpar.",
        "Los registros deben ser verdaderos. Cambiar o borrar un dato para «llegar a la meta» es falsear la información y puede esconder problemas que después son mucho más graves." + LIM,
    ],
    vocab=[("indicador", "dato calculado que muestra cómo va el trabajo"), ("meta", "valor que se espera alcanzar"), ("cumplimiento", "comparación entre lo realizado y la meta"), ("proporción por cada 100", "errores multiplicados por 100 y divididos entre el total"), ("calidad", "grado en que el trabajo cumple los criterios"), ("falsear", "cambiar un dato para que parezca otra cosa")],
    worked=[
        ("Medir cumplimiento de cantidad", "Un equipo de ejemplo tiene una meta de 30 piezas por día y hizo 24. ¿Cuántas piezas faltaron?", ["Faltante = meta − realizado.", "30 − 24 = 6."], "Faltaron 6 piezas"),
        ("Errores por cada 100", "Un día de ejemplo hubo 6 errores en 200 documentos. ¿Cuántos errores hubo por cada 100?", ["Se multiplica por 100 y se divide entre 200.", "6 × 100 ÷ 200 = 3."], "3 errores por cada 100"),
    ],
    mistakes=[("Decir que el día con más producción fue el mejor sin mirar la calidad.", "Más cantidad con muchos errores puede significar más retrabajo.", "Compara cantidad y calidad con las metas de ambas."),
              ("Borrar errores del registro para que el equipo «cumpla».", "Falsea los datos y oculta un problema que seguirá repitiéndose.", "Registra la verdad, corrige los errores y analiza la causa.")],
    T=[
        ("abc", "En el control del trabajo de un equipo: ¿qué es una meta diaria?", "El valor que se espera alcanzar cada día", "El horario de entrada al trabajo", "El sueldo que recibe el equipo", "La meta fija el resultado esperado; el horario y el sueldo son condiciones del trabajo."),
        ("abc", "{F} ¿Qué día no se cumplió la meta de cantidad?", "El jueves", "El lunes", "El martes", "El jueves se digitaron 40 documentos, menos que los 50 de la meta."),
        ("=", "{F} ¿Cuántos documentos se digitaron en total entre el lunes y el jueves?", "60+50+100+40", "Se suman los documentos de los cuatro días.", " documentos"),
        ("=", "{F} ¿Cuántos errores hubo en total entre el lunes y el jueves?", "3+2+10+0", "Se suman los errores de los cuatro días.", " errores"),
        ("=", "{F} ¿Cuántos errores por cada 100 documentos hubo el lunes?", "3*100//60", "Se multiplican los errores por 100 y se divide entre los documentos del día.", " por cada 100"),
        ("abc", "{F} ¿Qué día cumplió la cantidad pero no la regla de errores?", "El miércoles", "El lunes", "El jueves", "El miércoles hizo 100 documentos con 10 errores, el doble del máximo permitido por cada 100."),
        ("=", "{F} ¿Cuántos documentos le faltaron al jueves para llegar a la meta de cantidad?", "50-40", "A la meta se le resta lo realizado ese día.", " documentos"),
        ("abc", "¿Cómo se calculan los errores por cada 100 documentos?", "Multiplicando los errores por 100 y dividiendo entre los documentos", "Restando los errores a los documentos", "Dividiendo los documentos entre los errores", "La proporción compara los errores con el total y la expresa sobre 100."),
        ("=", "Un taller de ejemplo planifica 7 ensamblajes por día durante 5 días y el equipo completó 29. ¿Cuántos ensamblajes faltaron?", "(7*5)-29", "Se calcula la meta de los cinco días y se resta lo completado.", " ensamblajes"),
        ("abc", "{F} El jefe dice: «El miércoles fue el mejor día porque se digitaron más documentos». ¿Qué falta considerar?", "La calidad: el miércoles superó el máximo de errores", "El sueldo del equipo ese día", "Si el equipo llegó a la hora", "Un buen día cumple cantidad y calidad; el miércoles falló en calidad."),
        ("abc", "Para que el equipo «cumpla», un compañero propone borrar del registro los errores del miércoles. ¿Qué corresponde?", "No alterar el registro: corregir los errores y buscar su causa", "Borrarlos si nadie se entera", "Pasarlos al registro del día siguiente", "El registro debe reflejar la verdad, y la mejora surge de analizar el error."),
        ("=", "{F} Si el miércoles se hubiera querido cumplir la regla con los 100 documentos, ¿cuántos errores se podían tener como máximo?", "100*5//100", "Se aplica el máximo permitido por cada 100 documentos a los 100 del día.", " errores"),
        ("abc", "{F} Según los datos, ¿qué conclusión es la más adecuada?", "El lunes y el martes cumplen las dos metas; hay que revisar los errores del miércoles y la baja cantidad del jueves", "Todos los días cumplen porque el total semanal supera la meta", "Solo importa el miércoles porque hizo más documentos", "Cada día se evalúa contra sus propias metas; solo lunes y martes cumplieron cantidad y calidad."),
    ],
    ctx=("=", "{F} El viernes a las 14:00 el equipo lleva 26 documentos, la jornada termina a las 17:00 y la meta diaria es la de la ficha. ¿Cuántos documentos por hora necesita digitar en lo que queda del día?", "(50-26)//(17-14)", "Se calcula lo que falta para la meta y se reparte entre las horas que quedan.", " documentos por hora"),
    sc=[
        ("En un equipo de ejemplo: ¿qué es una meta?", "El valor que se espera alcanzar", "Sirve para comparar lo realizado con lo esperado."),
        ("¿Por qué se calculan los errores por cada 100 documentos?", "Para comparar días con distinta cantidad de documentos", "La proporción permite una comparación justa."),
        ("¿Se pueden borrar errores del registro para llegar a la meta?", "No, porque falsea la información", "Un registro falso oculta problemas que luego crecen."),
    ],
    op=("Caso de ejemplo. Una bodega ficticia registra sus despachos: Lunes, 40 despachos y 2 con error; Martes, 50 despachos y 1 con error; Miércoles, 25 despachos y 5 con error. Meta de ejemplo: 40 despachos diarios y no más de 5 errores por cada 100 despachos. "
        "Escribe: (1) qué días cumplen cantidad, (2) cuántos errores por cada 100 hubo cada día, (3) qué días cumplen la regla de errores, (4) una conclusión y una acción de mejora, sin culpar a personas.",
        "(1) Lunes y martes (40 y 50). (2) Lunes: 2 × 100 ÷ 40 = 5; martes: 1 × 100 ÷ 50 = 2; miércoles: 5 × 100 ÷ 25 = 20. (3) Lunes y martes (5 y 2, máximo 5); el miércoles no. (4) Lunes y martes cumplen ambas metas; el miércoles no cumple ni cantidad ni calidad: se revisa qué cambió ese día (por ejemplo, el volumen de pedidos o la capacitación) y se refuerza el control.",
        ["calcula la proporción por cada 100", "compara con las metas", "concluye con los datos", "propone una mejora sin culpar"],
        ["hoja con cálculos y una conclusión de dos líneas"],
        ["comparar solo cantidad", "no calcular por cada 100", "culpar a una persona"],
        "Pregunta: «¿qué pasaría con la meta si el miércoles se agregara una persona más?». Debe plantear que se reevalúa la cantidad y se vigila que no suban los errores."),
    reinforce="Inventa una meta de cantidad y una de calidad para una tarea de tu especialidad y calcula si un día de datos de ejemplo las cumple.",
    extend="Explica con un ejemplo por qué un indicador de cantidad sin uno de calidad puede engañar.",
)
