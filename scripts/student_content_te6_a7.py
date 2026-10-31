"""Cuaderno del estudiante, 6.º básico Tecnología: OA 07 (internet y comunicación en línea), clases 1 a 4.

Clase 1 seguridad de la fuente, 2 compartir información de distinto carácter, 3 privacidad, 4 normas de uso y publicación responsable.
Seguridad: no se pide abrir ningún sitio ni crear cuentas; todos los casos son ficticios y están escritos en el cuaderno, sin enlaces ni marcas.
Las decisiones de publicar o registrarse se toman siempre con una persona adulta de la casa o de la escuela.
Simplificación declarada: no se verifica el manejo de una plataforma real; se enseñan criterios y decisiones. Las normas legales (edad mínima de una plataforma,
derechos de autor y licencias) se dan en términos generales y deben ser confirmadas por el docente según la plataforma y la normativa vigente.
"""
from __future__ import annotations

from student_content_te6_a import reg
from student_lessons import arith

OA7 = "TE06 OA 07"

# ------------------------------------------------------------------ OA 07, clase 1
reg(
    OA7, 1,
    materials="Hoja y lápiz. Todos los casos están escritos en este cuaderno; no necesitas abrir ningún sitio.",
    use="Aprenderé a decidir si una fuente de internet es segura y confiable antes de usar o compartir su información. Sirve para no difundir errores ni caer en engaños.",
    prior=["Sé que una fuente es el origen de una información.", "Sé que en internet hay información verdadera y falsa.", "Sé pedir ayuda a una persona adulta."],
    explain=[
        "Una fuente es el lugar de donde viene una información. En internet hay fuentes confiables y otras que no lo son. Antes de usar o compartir información, se comprueba la fuente con cinco preguntas: ¿quién la escribió?, ¿cuándo?, ¿qué organización la respalda?, ¿da pruebas o datos? y ¿otras fuentes confiables dicen lo mismo?",
        "Una fuente segura suele tener autor o institución conocida, fecha, datos que se pueden comprobar y un lenguaje sereno. Señales de alerta: no tiene autor ni fecha, usa palabras como «increíble» o «compártelo ya», pide contraseñas o datos personales, ofrece premios, o tiene una dirección parecida a otra conocida pero con letras cambiadas.",
        "Una fuente puede ser confiable para un tema y no para otro. Un museo explica bien su colección, pero no es la mejor fuente sobre medicina. Siempre se contrastan al menos dos fuentes independientes. Si una página pide datos o algo parece sospechoso, no se hace clic y se avisa a una persona adulta.",
    ],
    vocab=[("fuente", "origen de una información"), ("confiable", "que se puede creer porque da pruebas"), ("contrastar", "comparar lo que dicen distintas fuentes"), ("engaño", "información falsa hecha para confundir"), ("autor", "persona o institución que creó la información")],
    worked=[
        ("Revisar una fuente con las cinco preguntas", "Un mensaje dice: «Increíble: se descubrió que los gatos hablan, compártelo ya». No tiene autor ni fecha. ¿Es confiable?", ["No tiene autor, fecha ni datos.", "Usa palabras como «increíble» y pide compartirlo."], "No es confiable"),
        ("Contrastar fuentes", "Un museo de ciencias y un informe de una universidad coinciden en que el agua hierve a 100 grados Celsius al nivel del mar. ¿Qué indica?", ["Dos fuentes independientes dicen lo mismo.", "El dato es más seguro."], "El dato es más confiable"),
    ],
    mistakes=[
        ("Creer una información porque está muy compartida.", "Muchas personas pueden compartir un engaño.", "Comprueba la fuente con las cinco preguntas."),
        ("Hacer clic en un mensaje que ofrece un premio.", "Puede ser un engaño para robar datos.", "No hagas clic y avisa a una persona adulta."),
    ],
    R=[
        ("¿Una fuente sin autor ni fecha es una señal de alerta o de confianza?", "De alerta", "No se puede saber quién lo escribió ni cuándo."),
        ("Si un mensaje ofrece un premio y pide datos, ¿haces clic?", "No", "Puede ser un engaño."),
        ("¿Qué es contrastar fuentes?", "Comparar lo que dicen distintas fuentes", "Así se comprueba un dato."),
    ],
    C=[
        ("¿Por qué una información muy compartida puede ser falsa?", "Porque cualquier persona puede compartir un engaño", "Compartir no prueba que sea verdad."),
        ("¿Cuál es una pregunta para comprobar una fuente? A ¿Quién la escribió?, B ¿Cuántos «me gusta» tiene?", "A", "Los «me gusta» no prueban que sea cierta."),
        ("¿Una fuente confiable en un tema lo es siempre en otros?", "No", "Cada fuente tiene un tema de especialidad."),
    ],
    A=[
        ("Un sitio dice: «Beba este jugo y cure cualquier enfermedad». Sin autor, sin fecha y sin pruebas. ¿Confiable o no?", "No confiable", "Promete algo sin pruebas y no tiene autor."),
        ("Una página de una biblioteca nacional da el autor, la fecha y las fuentes de un artículo sobre aves. ¿Confiable o no?", "Confiable", "Tiene autor, fecha y fuentes."),
        arith("Revisas una información con 5 preguntas y una fuente responde bien 3. ¿Cuántas preguntas no cumple?", "5-3", "Se resta lo que cumple del total.", " preguntas"),
    ],
    Z=[
        ("Dos fuentes dicen cosas distintas sobre la altura de una montaña. ¿Qué haces?", "Buscar una tercera fuente confiable", "Contrastar permite decidir con más evidencia."),
        ("Rosa dice: «Si lo dice un sitio con muchos colores y animaciones, es confiable». ¿Es correcto?", "No", "La apariencia no prueba que sea confiable."),
    ],
    D=[
        arith("Un grupo revisa 12 mensajes: 4 son engaños y el resto son confiables. ¿Cuántos son confiables?", "12-4", "Se resta lo engañoso del total.", " mensajes"),
        ("Una dirección parece igual a la de un banco, pero con una letra cambiada, y pide la contraseña. ¿Qué hay que hacer?", "No hacer clic y avisar a una persona adulta", "Puede ser un engaño que roba datos."),
    ],
    ctx=("Para un trabajo sobre el cuidado del agua, encuentras tres fuentes: A un artículo de una universidad con autor, fecha y datos; B un mensaje que dice «El agua pronto se acabará, compártelo ya» sin autor; C una nota de una organización conocida con fecha reciente. Elige las dos fuentes que usarías y explica por qué.", "Usaría A y C porque tienen autor o institución, fecha y datos. B no tiene autor ni pruebas y pide compartirlo", "Se eligen las fuentes con las señales de confianza."),
    sc=[
        ("¿Qué preguntas ayudan a comprobar una fuente?", "Quién, cuándo, qué organización, qué pruebas y si otras fuentes coinciden", "Son las cinco preguntas de la clase."),
        ("¿Qué haces si algo parece sospechoso?", "No hago clic y aviso a una persona adulta", "Evita un posible engaño."),
        ("¿Cuántas fuentes se contrastan como mínimo?", "Dos", "Así se comprueba un dato."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un mensaje dice «Tu curso ganó un viaje, haz clic y escribe la contraseña de tu cuenta» y no tiene autor. Caso 2: un artículo de una institución de ciencias, con autor, fecha y datos, dice que las plantas producen oxígeno. Aplica las cinco preguntas, escribe si es confiable y qué harías. No abras ningún sitio: usa solo lo escrito aquí.",
        "Caso 1: sin autor, sin organización, sin datos y pide la contraseña. No es confiable. No hago clic y aviso a una persona adulta",
        ["aplica las cinco preguntas", "decide si es confiable", "dice qué haría", "usa solo los datos del caso"],
        ["ficha con las cinco preguntas y la decisión"],
        ["creer por el diseño", "no avisar a una persona adulta"],
        "Pregunta: «¿qué señal te hace confiar o desconfiar?». Si no nombra una, pídele volver a las preguntas.",
    ),
    reinforce="Cuéntale a una persona de tu casa las cinco preguntas para comprobar una fuente.",
    extend="Explica por qué contrastar con una segunda fuente protege de difundir un engaño.",
)

# ------------------------------------------------------------------ OA 07, clase 2
reg(
    OA7, 2,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a elegir cómo compartir información de distinto carácter (texto, imagen, audio, video y archivos) con otras personas. Sirve para comunicar bien y seguro.",
    prior=["Sé qué es un correo electrónico.", "Sé que hay información que se puede compartir y otra que no.", "Sé pedir ayuda a una persona adulta."],
    explain=[
        "Compartir información es enviarla o ponerla a disposición de otras personas. Puede ser de distinto carácter: un texto, una imagen, un audio, un video o un archivo con una tabla. Cada tipo ocupa distinto espacio. Un texto es liviano, una imagen es más pesada y un video es lo más pesado. El peso se mide en megabytes, que se abrevian MB.",
        "Hay medios para compartir con una persona o con un grupo. El correo electrónico sirve para mensajes formales y archivos adjuntos. Un chat o mensajería sirve para conversar rápido con un grupo. Una plataforma de la escuela o un sitio del curso permite publicar para todo el grupo bajo reglas de la escuela. Un foro permite conversar sobre un tema. Se elige según a quién quieres llegar y cuánto tiempo debe estar disponible.",
        "Para compartir bien: el mensaje debe tener un asunto claro, un saludo, el contenido y una despedida. Si adjuntas un archivo, revisa que sea el correcto y que no sea muy pesado; si pesa mucho, se puede comprimir. Antes de enviar, relee y confirma a quién va. Un mensaje enviado no siempre se puede recuperar.",
    ],
    vocab=[("adjunto", "archivo que se envía junto con un mensaje"), ("megabyte (MB)", "unidad que mide el peso de un archivo"), ("asunto", "título corto de un correo"), ("plataforma", "sitio o aplicación para compartir y trabajar en línea"), ("foro", "espacio en línea para conversar sobre un tema")],
    worked=[
        ("Elegir el medio", "Quieres que todo tu curso vea las fotos de una exposición durante un mes, con la autorización de las familias. ¿Eliges un chat o una plataforma de la escuela?", ["Debe estar disponible por un mes para todo el curso.", "La plataforma de la escuela tiene reglas de uso."], "La plataforma de la escuela"),
        ("Calcular el peso de los adjuntos", "Adjuntas 3 imágenes de 2 MB cada una. El correo permite hasta 10 MB. ¿Cuánto pesan y cabe?", ["3 × 2 = 6 MB.", "6 MB es menos que 10 MB."], "Pesan 6 MB y sí cabe"),
    ],
    mistakes=[
        ("Enviar un correo sin asunto.", "No se sabe de qué trata.", "Escribe un asunto claro y breve."),
        ("Adjuntar un archivo sin revisarlo.", "Puede ser el equivocado o muy pesado.", "Revisa el archivo y su peso antes de enviar."),
    ],
    R=[
        ("¿Qué pesa más: un texto o un video?", "Un video", "Un video tiene muchas imágenes y sonido."),
        ("¿Qué unidad mide el peso de un archivo?", "El megabyte (MB)", "Es una unidad de tamaño de archivos."),
        ("¿Qué es un adjunto?", "Un archivo que se envía junto con un mensaje", "Va con el mensaje."),
    ],
    C=[
        ("¿Para qué sirve el asunto de un correo?", "Para decir de qué trata", "Ayuda a entender el mensaje."),
        ("¿Qué medio eliges para conversar rápido con un grupo pequeño? A un chat, B un correo formal.", "A", "El chat es rápido."),
        ("¿Por qué se relee un mensaje antes de enviarlo?", "Porque no siempre se puede recuperar", "Evita enviar algo equivocado."),
    ],
    A=[
        arith("Adjuntas 4 documentos de 1 MB y una imagen de 3 MB. ¿Cuántos MB pesan en total?", "4*1+3", "Se suman los documentos y la imagen.", " MB"),
        arith("El correo permite hasta 20 MB. Ya adjuntaste 13 MB. ¿Cuántos MB más puedes adjuntar?", "20-13", "Se resta lo adjuntado del máximo.", " MB"),
        ("Quieres enviar una tabla de datos y un texto formal a la profesora. ¿Qué medio eliges? A correo electrónico, B conversación oral sin registro.", "A", "El correo permite adjuntar y deja registro."),
    ],
    Z=[
        ("Un video de 80 MB no cabe en un correo de máximo 25 MB. ¿Qué opción es mejor? A comprimirlo o compartirlo en la plataforma del curso con ayuda de una persona adulta, B enviarlo igual.", "A", "Enviarlo igual falla."),
        ("Mateo envía a todo el curso un mensaje que solo era para su amigo. ¿Qué error cometió?", "No revisó a quién lo enviaba", "Debía confirmar el destinatario."),
    ],
    D=[
        arith("Un envío tiene una presentación de 9 MB, 6 fotos de 2 MB cada una y un audio de 5 MB. ¿Cuántos MB pesa en total?", "9+6*2+5", "Se calcula el total de cada grupo y se suman.", " MB"),
        arith("Un correo permite 25 MB. Si cada foto pesa 5 MB, ¿cuántas fotos como máximo caben?", "25//5", "Se divide el máximo entre el peso de cada foto.", " fotos"),
    ],
    ctx=("Debes enviar a tu profesora un informe de 2 MB, una foto de 3 MB y un audio de 4 MB. El correo permite 10 MB. Calcula si cabe y escribe un asunto y las partes del mensaje.", "2 + 3 + 4 = 9 MB; sí cabe. Asunto: «Informe, foto y audio de mi trabajo de Tecnología». Saludo, contenido y despedida", "El total es menor que 10 MB y el mensaje tiene sus partes."),
    sc=[
        ("¿Qué tipos de información se pueden compartir?", "Texto, imagen, audio, video y archivos", "Son los tipos de la clase."),
        ("¿Qué se revisa antes de enviar?", "Destinatario, archivo y peso", "Así se evitan errores de envío."),
        ("¿Qué medio permite adjuntar archivos y dejar registro?", "El correo electrónico", "Es formal y guarda el mensaje."),
    ],
    open_task=(
        "Escoge una situación. Situación 1: debes enviar al curso las instrucciones de una actividad (texto de 1 MB) y dos fotos de 4 MB cada una por un medio que admite 10 MB. Situación 2: quieres compartir con tu profesora un audio de 6 MB y un informe de 3 MB por un correo que admite 8 MB. Calcula el peso, decide el medio, escribe el asunto, un mensaje de tres líneas y qué harías si no cabe. No envíes nada real.",
        "Situación 2: 6 + 3 = 9 MB, no cabe en 8 MB. Comprimo el audio con ayuda de una persona adulta o uso la plataforma de la escuela. Asunto: «Audio e informe de Tecnología»",
        ["calcula el peso", "decide el medio", "asunto y mensaje con partes", "alternativa si no cabe"],
        ["mensaje escrito con cálculo y plan"],
        ["no calcular el peso", "enviar sin revisar el destinatario"],
        "Pregunta: «¿cuántos MB pesa todo y cuántos permite el medio?». Revisa el cálculo.",
    ),
    reinforce="Escribe en papel un mensaje de tres líneas con asunto para invitar a un familiar a ver tu trabajo.",
    extend="Explica por qué conviene usar la plataforma de la escuela y no un chat personal para compartir un trabajo con todo el curso.",
)

# ------------------------------------------------------------------ OA 07, clase 3
reg(
    OA7, 3,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a proteger mi privacidad y la de otras personas al usar internet: qué datos no se comparten, cómo usar contraseñas y cómo configurar quién ve mi información. Sirve para cuidarme y cuidar a las demás personas.",
    prior=["Sé qué es un dato personal.", "Sé que algunas cosas se comparten solo con personas de confianza.", "Sé pedir ayuda a una persona adulta."],
    explain=[
        "La privacidad es el derecho a decidir quién conoce tu información. Los datos personales son los que identifican a una persona: nombre completo, dirección, teléfono, fotos, colegio, rutas habituales y contraseñas. En internet no se comparten con desconocidos. Lo que publicas puede quedar guardado mucho tiempo y ser copiado; eso se llama huella digital.",
        "Una contraseña protege una cuenta. Una buena contraseña es larga, mezcla letras, números y símbolos, no usa tu nombre ni tu fecha de nacimiento, y es distinta en cada cuenta. No se comparte con amigos; solo se puede compartir con una persona adulta de confianza, de tu familia o de la escuela. Si crees que alguien la conoce, avisa a una persona adulta para cambiarla.",
        "Las plataformas tienen configuración de privacidad: puedes elegir que lo que publicas lo vea solo tu grupo, solo personas conocidas o todo el mundo. Para menores, lo mejor es lo más privado, siempre con una persona adulta. Antes de publicar una foto o un video de otra persona, pides permiso. Si algo te incomoda o te asusta, no respondas, guárdalo como prueba y cuéntaselo a una persona adulta.",
    ],
    vocab=[("privacidad", "derecho a decidir quién conoce tu información"), ("dato personal", "dato que identifica a una persona"), ("huella digital", "rastro que dejan tus actividades en internet"), ("contraseña", "clave secreta que protege una cuenta"), ("configuración de privacidad", "opciones para decidir quién ve lo que publicas")],
    worked=[
        ("Clasificar datos", "¿Cuáles son datos personales que no se comparten con desconocidos: tu dirección, el color favorito, el nombre de tu colegio?", ["La dirección identifica dónde vives.", "El nombre del colegio dice dónde estás cada día."], "Tu dirección y el nombre del colegio"),
        ("Evaluar una contraseña", "¿Qué contraseña es mejor: A «Rocio2014» (nombre y año de nacimiento), B «cT7#mel_92po»?", ["A usa un nombre y un año fáciles de adivinar.", "B es larga y mezcla letras, números y símbolos."], "B"),
    ],
    mistakes=[
        ("Compartir la contraseña con un amigo para jugar.", "Otra persona puede usar tu cuenta sin permiso.", "Solo se comparte con una persona adulta de confianza, de tu familia o de la escuela."),
        ("Publicar una foto de un compañero sin preguntarle.", "No se respeta su privacidad.", "Pide permiso antes de publicar."),
    ],
    R=[
        ("¿Se comparte la dirección de tu casa con desconocidos?", "No", "Es un dato personal."),
        ("¿Una contraseña buena es corta o larga?", "Larga", "Es más difícil de adivinar."),
        ("¿Con quién se puede compartir una contraseña?", "Con una persona adulta de confianza, de tu familia o de la escuela", "Es quien puede ayudarte."),
    ],
    C=[
        ("¿Qué es la huella digital?", "El rastro que dejan tus actividades en internet", "Lo que publicas puede quedar guardado."),
        ("¿Para qué sirve la configuración de privacidad?", "Para decidir quién ve lo que publicas", "Protege la información."),
        ("Si algo en línea te incomoda, ¿qué haces?", "No respondo, guardo la prueba y aviso a una persona adulta", "Es la forma segura de actuar."),
    ],
    A=[
        arith("Una contraseña de 4 dígitos tiene 10 posibilidades por cada lugar. ¿Cuántas combinaciones hay en total?", "10*10*10*10", "Se multiplican las posibilidades de cada lugar.", " combinaciones"),
        ("Elige la contraseña más segura. A «123456», B «lu7#Tr_9pa».", "B", "B es más larga y mezcla caracteres."),
        ("Un juego pide tu nombre completo, tu curso y tu dirección para jugar. ¿Qué haces?", "No lo escribo y consulto a una persona adulta", "Son datos personales."),
    ],
    Z=[
        ("Sofía dice: «Si mi perfil es privado, puedo publicar mi dirección». ¿Está en lo correcto?", "No", "Aun así la información puede copiarse o filtrarse."),
        ("Un compañero publicó una foto tuya sin preguntarte. ¿Qué haces?", "Le pido que la retire y aviso a una persona adulta", "Tienes derecho a decidir sobre tu imagen."),
    ],
    D=[
        arith("Una clave de 2 dígitos tiene 100 combinaciones y una de 4 dígitos tiene 10.000. ¿Cuántas veces más combinaciones tiene la de 4 dígitos?", "10000//100", "Se divide el total de 4 dígitos entre el de 2 dígitos.", " veces"),
        ("En un chat, un desconocido te pide una foto y tu dirección. ¿Qué haces?", "No respondo y aviso a una persona adulta", "Es una situación de riesgo."),
    ],
    ctx=("Vas a crear con ayuda de una persona adulta una cuenta de la plataforma del curso. Escribe qué datos no pondrías, cómo sería tu contraseña (sin escribir la real) y qué configuración de privacidad elegirías.", "No pondría dirección ni teléfono. Contraseña larga con letras, números y símbolos, sin mi nombre. Perfil privado, visible solo para mi curso", "Se protegen los datos y se elige la configuración más privada."),
    sc=[
        ("¿Qué es un dato personal?", "Un dato que identifica a una persona", "Por ejemplo, la dirección."),
        ("¿Cómo debe ser una buena contraseña?", "Larga y distinta en cada cuenta", "Es más difícil de adivinar."),
        ("¿Qué haces antes de publicar la foto de otra persona?", "Pedirle permiso", "Se respeta su privacidad."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: una página de juegos pide tu nombre completo, tu dirección y tu teléfono para dar un premio. Caso 2: quieres publicar en la plataforma del curso una foto del grupo con 5 compañeros. Escribe qué harías, qué datos no entregarías, a quién pedirías permiso y qué configuración de privacidad usarías. No escribas datos reales.",
        "Caso 2: pido permiso a los 5 compañeros y a una persona adulta responsable; publico en la plataforma del curso con privacidad solo para el curso",
        ["dice qué datos no entrega", "pide permiso a quien corresponde", "elige configuración privada", "consulta a una persona adulta"],
        ["plan escrito de protección"],
        ["entregar datos personales", "publicar sin permiso"],
        "Pregunta: «¿quién podría ver esto y quién dio permiso?». Revisa que haya autorización.",
    ),
    reinforce="Escribe tres datos que no compartirías en internet y por qué.",
    extend="Explica por qué lo que se publica puede dejar una huella digital aunque se borre después.",
)

# ------------------------------------------------------------------ OA 07, clase 4
reg(
    OA7, 4,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé las normas de uso para publicar y comunicarme en línea: respeto, derechos de autor y reglas de la plataforma. Sirve para convivir bien y publicar con responsabilidad.",
    prior=["Sé comprobar una fuente.", "Sé proteger datos personales.", "Sé qué es un derecho de autor."],
    explain=[
        "Las normas de uso son reglas para convivir en línea. La primera es el respeto: se escribe como se habla frente a frente. El ciberacoso es molestar, insultar o excluir a alguien por medios digitales y es una conducta grave. Si lo ves o lo sufres, no respondas, guarda la prueba y avisa a una persona adulta o a la escuela.",
        "Otra norma es respetar los derechos de autor: las fotos, textos, música y videos tienen un autor. Para usar una obra ajena se necesita permiso o que tenga una licencia de uso libre, y siempre se cita la fuente. Copiar un trabajo y decir que es tuyo se llama plagio. También se respetan las reglas de cada plataforma, como la edad mínima para tener una cuenta.",
        "Antes de publicar usa una lista: ¿es verdadero y la fuente es confiable?, ¿protege datos personales?, ¿tengo permiso de las personas que aparecen?, ¿respeta derechos de autor?, ¿es respetuoso?, ¿lo revisó una persona adulta? Si una respuesta es no, no se publica. Publicar con responsabilidad significa pensar en cómo afectará a otras personas.",
    ],
    vocab=[("norma de uso", "regla para convivir en línea"), ("ciberacoso", "acoso por medios digitales"), ("plagio", "copiar un trabajo ajeno diciendo que es propio"), ("licencia de uso libre", "permiso del autor para usar su obra bajo ciertas condiciones"), ("responsabilidad", "pensar en las consecuencias de lo que haces")],
    worked=[
        ("Revisar antes de publicar", "Quieres publicar una foto del curso en que sale un compañero que no te dio permiso y se ve una hoja con su dirección. ¿Qué pasos de la lista no cumples?", ["No tienes permiso del compañero.", "La dirección es un dato personal."], "Permiso y protección de datos personales"),
        ("Identificar el plagio", "Una estudiante copia un párrafo de un sitio y dice que lo escribió ella. ¿Qué es?", ["Copió un trabajo ajeno.", "Dijo que era suyo."], "Plagio"),
    ],
    mistakes=[
        ("Decir «era una broma» para molestar a alguien en línea.", "El daño sigue siendo real.", "Escribe como si lo dijeras frente a frente."),
        ("Copiar y pegar sin citar la fuente.", "Es plagio.", "Usa tus palabras y anota la fuente."),
    ],
    R=[
        ("Copiar un trabajo ajeno y decir que es tuyo, ¿cómo se llama?", "Plagio", "No se reconoce al autor."),
        ("¿Qué haces si ves ciberacoso?", "No respondo, guardo la prueba y aviso a una persona adulta", "Es la forma segura de actuar."),
        ("¿Qué se cita al usar una obra ajena?", "La fuente", "Se reconoce al autor."),
    ],
    C=[
        ("¿Por qué se escribe en línea como si fuera frente a frente?", "Porque el daño a la otra persona es real", "El respeto es igual."),
        ("¿Qué es una licencia de uso libre?", "Un permiso del autor para usar su obra bajo ciertas condiciones", "Indica qué se puede hacer."),
        ("¿Por qué existe una edad mínima en una plataforma?", "Porque está pensada para personas de cierta edad", "Es una norma de la plataforma."),
    ],
    A=[
        ("Una estudiante quiere subir una canción famosa como fondo de su video del curso. ¿Qué necesita?", "Permiso o una licencia de uso", "La canción tiene derechos de autor."),
        arith("La lista de revisión para publicar tiene 6 preguntas y tu publicación responde que sí a 5. ¿Cuántas preguntas faltan?", "6-5", "Se resta lo cumplido del total.", " pregunta"),
        ("Un compañero escribe en el chat del curso: «Eres un tonto y nadie te quiere». ¿Qué es?", "Ciberacoso", "Es insultar por medios digitales."),
    ],
    Z=[
        ("Ana dice: «Si borro la publicación, ya no importa». ¿Es correcto?", "No", "Pudo ser vista o copiada."),
        ("Un grupo publica un afiche con la fotografía de un artista que bajaron de internet sin avisar. ¿Qué debieron hacer?", "Usar fotos propias o con permiso y citar la fuente", "Respetan los derechos de autor."),
    ],
    D=[
        arith("Un curso tiene 28 estudiantes. Uno toma la foto de grupo y los demás salen en ella. ¿De cuántos estudiantes se necesita permiso para publicarla?", "28-1", "Se descuenta a quien toma la foto.", " permisos"),
        ("Antes de publicar, una estudiante cumple 5 de 6 preguntas de la lista; no tiene permiso de una persona que aparece. ¿Publica?", "No", "Si una respuesta es no, no se publica."),
    ],
    ctx=("Tu curso quiere publicar en la plataforma de la escuela un video de una exposición con música. Usa una canción de un grupo famoso y muestra a 6 estudiantes. Revisa con la lista: derechos de autor, permisos, datos personales y respeto, y decide qué cambiar.", "Debo reemplazar la canción por música propia o con licencia libre, pedir permiso a los 6 estudiantes y a sus familias, y evitar nombres completos. Con una persona adulta revisamos el respeto", "Se revisan los puntos de la lista y se corrige."),
    sc=[
        ("En Tecnología: ¿Qué es el plagio?", "Copiar un trabajo ajeno diciendo que es propio", "Falta de respeto al autor."),
        ("¿Qué haces si una respuesta de la lista es no?", "No publico", "Se corrige antes de publicar."),
        ("¿Quién revisa lo que se publica?", "Una persona adulta", "Ayuda a decidir con responsabilidad."),
    ],
    open_task=(
        "Escoge una publicación. Publicación 1: un afiche del curso con una foto de un deportista famoso copiada de internet y los nombres completos de 4 estudiantes. Publicación 2: un video del curso con música de un grupo conocido y un comentario burlón sobre una compañera. Revisa con la lista de 6 preguntas, marca las que no se cumplen y escribe cómo corregir cada una antes de publicar.",
        "Publicación 1: no cumple derechos de autor ni datos personales. Cambio la foto por una propia o con licencia y uso solo nombres de pila",
        ["revisa la lista completa", "marca lo que no se cumple", "propone una corrección para cada punto", "consulta a una persona adulta"],
        ["lista de revisión con correcciones"],
        ["publicar sin revisar", "justificar una burla"],
        "Pregunta: «¿qué respuesta de la lista es no?». Revisa que se corrija antes de publicar.",
    ),
    reinforce="Escribe tres normas que seguirías en un chat del curso.",
    extend="Explica por qué citar la fuente y pedir permiso son formas de respeto, con un ejemplo.",
)
