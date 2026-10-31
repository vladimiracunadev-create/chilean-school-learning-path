"""Cuaderno del estudiante, 5.º básico Tecnología: OA 07 (internet y comunicación en línea, seguridad de la fuente y privacidad), clases 1 a 4.

Las pantallas, direcciones y mensajes son EJEMPLOS FICTICIOS: ninguna dirección existe y no se nombra ninguna marca.
Todas las clases tienen alternativa sin conexión. No se pide ingresar datos personales reales ni contraseñas reales.
Simplificación declarada: juzgar la confiabilidad de una fuente es más complejo que las señales de este cuaderno; las edades mínimas de uso de cada servicio
y las normas legales de protección de datos no se detallan y quedan para la persona adulta o la o el docente.
"""
from __future__ import annotations

from student_content_te5_a import reg
from student_lessons import arith

OA7 = "TE05 OA 07"

# ------------------------------------------------------------------ OA 07, clase 1
reg(
    OA7, 1,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno; no necesitas conexión a internet para hacerlos.",
    use="Aprenderé a elegir el medio en línea adecuado para compartir distintos tipos de información con otras personas. Sirve para que el mensaje llegue a quien corresponde, en la forma correcta.",
    prior=["Sé que internet conecta computadores y personas.", "Sé buscar información con un buscador.", "Sé que un archivo puede ser texto, imagen o sonido."],
    explain=[
        "Compartir información en línea es enviar o mostrar algo a otras personas usando internet. La información puede ser de diferente carácter: un aviso del curso, una tarea, una foto de un trabajo, una opinión o una pregunta. Antes de compartir, piensa para qué lo haces, con quién y qué tipo de contenido es: texto, imagen, archivo, enlace, sonido o video.",
        "Hay varios medios en línea. El correo electrónico sirve para mensajes más largos y formales, con archivos adjuntos. La mensajería sirve para mensajes cortos y rápidos con un grupo conocido. La videollamada sirve para conversar en directo. Un espacio compartido, como una carpeta o un documento común, sirve para trabajar juntos en el mismo archivo. Un foro sirve para conversar con muchas personas.",
        "Elegir bien el medio es parte del mensaje. Un trabajo con imágenes pesadas se comparte mejor en un espacio compartido que en un mensaje corto. Un aviso para todo el curso va a un grupo cerrado y no a un lugar público. Si el medio es público, cualquiera puede verlo. Antes de enviar, revisa que quienes lo reciban sean las personas correctas. Los servicios en línea tienen edades mínimas y reglas propias: pregunta a una persona adulta cuáles puedes usar y úsalos con su compañía.",
    ],
    vocab=[("correo electrónico", "mensaje enviado por internet con asunto y adjuntos"), ("mensajería", "intercambio de mensajes cortos entre personas"), ("espacio compartido", "carpeta o documento donde varias personas trabajan juntas"), ("adjunto", "archivo que se envía junto con un mensaje"), ("público", "que puede ser visto por cualquier persona")],
    worked=[
        ("Elegir el medio", "Debes enviar a tu profesora un trabajo con 6 imágenes y un texto largo. ¿Qué medio conviene?", ["Es un envío formal y con archivos.", "El correo electrónico permite adjuntar archivos."], "Correo electrónico con archivos adjuntos"),
        ("Pensar en quién lo ve", "Quieres avisar que mañana el curso se junta a las 15:00. ¿Lo publicas en un lugar público o en un grupo cerrado del curso?", ["El aviso es solo para el curso.", "Un grupo cerrado limita quiénes lo ven."], "En un grupo cerrado del curso"),
    ],
    mistakes=[
        ("Enviar un aviso del curso a un lugar público.", "Cualquier persona puede verlo.", "Usa un grupo cerrado con las personas correctas."),
        ("Mandar un trabajo con muchas imágenes en un mensaje corto.", "Puede no llegar o llegar incompleto.", "Usa correo con adjuntos o un espacio compartido."),
    ],
    R=[
        ("¿Qué medio permite enviar un archivo adjunto con un mensaje formal?", "El correo electrónico", "Tiene asunto y adjuntos."),
        ("Un lugar donde cualquiera puede ver lo que publicas, ¿es público o cerrado?", "Público", "Cualquier persona puede entrar."),
        ("Una conversación en directo con imagen y sonido, ¿es videollamada o foro?", "Videollamada", "Se conversa en el mismo momento."),
    ],
    C=[
        ("¿Por qué conviene pensar en quién recibirá un mensaje antes de enviarlo?", "Porque debe llegar a las personas correctas", "Un error puede mostrarlo a quien no corresponde."),
        ("Un documento donde varias personas escriben a la vez, ¿es espacio compartido o foro?", "Espacio compartido", "Sirve para trabajar juntas en el mismo archivo."),
        ("Una foto de un trabajo, ¿es información de carácter texto o imagen?", "Imagen", "Es un contenido visual."),
    ],
    A=[
        ("Quieres preguntar a tu curso un horario y recibir respuestas rápidas. ¿Mensajería de un grupo cerrado o correo formal?", "Mensajería de un grupo cerrado", "Es una consulta corta y rápida para personas conocidas."),
        arith("Un trabajo tiene 6 imágenes de 2 megas cada una. ¿Cuántos megas pesan en total?", "6*2", "Se multiplican las imágenes por su peso."),
        ("Tu profesora pide el informe del grupo con el nombre de todos. ¿Lo envías por correo o lo publicas en un lugar público?", "Por correo", "El informe es para ella y debe tener un medio directo."),
    ],
    Z=[
        ("Dos estudiantes comparten una tarea: una por un lugar público y otra por correo a la profesora. ¿Cuál cuida mejor quién la ve y por qué?", "La del correo, porque llega a quien corresponde", "El medio público la muestra a cualquier persona."),
        ("Un grupo quiere trabajar un afiche entre cuatro personas a distancia. ¿Qué medio permite editar el mismo archivo?", "Un espacio compartido", "Todas las personas pueden trabajar sobre el mismo documento."),
    ],
    D=[
        arith("El límite de un correo para adjuntos es 20 megas. Tienes 3 archivos de 5 megas. ¿Cuántos megas puedes agregar todavía?", "20-3*5", "Se restan los 15 megas usados de los 20 permitidos."),
        ("Un aviso dice «reunión de apoderados» pero lo enviaste al grupo de otro curso. ¿Qué error hubo?", "Se envió a destinatarios equivocados", "Hay que revisar quién recibe el mensaje."),
    ],
    ctx=("Debes compartir con tu profesora un informe de 2 páginas con 3 fotos, y avisar al curso la hora de la reunión de mañana. Escribe qué medio usas para cada cosa y por qué.", "Informe: correo con adjuntos o espacio compartido, porque lleva archivos. Aviso: mensajería del grupo cerrado del curso, porque es corto y para personas conocidas", "Dos medios con razón."),
    sc=[
        ("¿Qué se piensa antes de compartir información?", "Para qué, con quién y qué tipo es", "Guía la elección del medio."),
        ("¿Un grupo cerrado limita quién ve el mensaje?", "Sí", "Solo lo ven sus integrantes."),
        ("¿Qué medio sirve para trabajar juntas en el mismo archivo?", "El espacio compartido", "Permite editar a la vez."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: debes enviar a tu profesora un trabajo de Ciencias con 4 imágenes y un texto largo. Caso 2: debes avisar a tu curso que la salida pedagógica es el jueves a las 9:00. Escribe el medio que usas, quiénes lo recibirían, el tipo de información y una razón.",
        "Caso 2: mensajería de un grupo cerrado; lo reciben las personas del curso; información de texto; es corto y solo para el curso.",
        ["elige un medio adecuado", "nombra quiénes lo reciben", "indica el tipo de información", "da una razón"],
        ["tabla con medio, destinatarios, tipo y razón"],
        ["usar un medio público para un aviso del curso", "no pensar en quién recibe"],
        "Pregunta: «¿quiénes verán este mensaje?». Si no lo sabe, repasen la diferencia entre público y cerrado.",
    ),
    reinforce="Anota tres cosas que has compartido con otras personas y por qué medio.",
    extend="Explica por qué un informe con imágenes pesadas conviene en un espacio compartido.",
)

# ------------------------------------------------------------------ OA 07, clase 2
reg(
    OA7, 2,
    materials="Hoja y lápiz. Las fuentes están escritas en este cuaderno; son ejemplos inventados y no existen.",
    use="Aprenderé a revisar si una fuente es segura antes de usarla o compartirla: quién la escribe, cuándo, para qué y si otras fuentes coinciden. Sirve para no difundir información falsa ni caer en engaños.",
    prior=["Sé buscar información en internet.", "Sé que no todo lo que aparece en internet es verdadero.", "Sé anotar la fuente de lo que uso."],
    explain=[
        "Una fuente es el lugar de donde viene una información. La seguridad de la fuente es qué tan confiable es. Para revisarla, mira cuatro señales. Autoría: ¿se sabe quién la escribió y si conoce el tema? Fecha: ¿está actualizada? Propósito: ¿quiere informar, vender o engañar? Dirección: ¿pertenece a una institución conocida o tiene letras raras?",
        "La señal más fuerte es contrastar: buscar la misma información en dos o más fuentes distintas y ver si coinciden. Si solo una fuente lo dice, no lo des por cierto. Desconfía si el mensaje te apura («¡hazlo ahora!»), promete premios, tiene muchos errores o te pide datos personales. Esas son señales de engaño. La dirección con candado indica que la conexión es privada, pero no que el contenido sea verdadero.",
        "Antes de compartir una información, verifica la fuente. Si no estás seguro, no la reenvíes y pregunta a una persona adulta o a tu docente. Cuando uses una información, escribe de dónde la sacaste: autor, nombre del sitio y fecha. Así otras personas pueden comprobarla. Compartir información falsa, aunque sea sin querer, puede confundir y dañar a otras personas.",
    ],
    vocab=[("fuente", "lugar de donde viene una información"), ("autoría", "quién escribió la información"), ("contrastar", "comparar la misma información en varias fuentes"), ("engaño", "mensaje que busca que creas algo falso o entregues datos"), ("verificar", "comprobar que algo es cierto")],
    worked=[
        ("Aplicar las señales", "Un sitio dice que una planta cura todo, no muestra autor ni fecha y pide tu correo para «recibir el premio». ¿Qué señales de alerta tiene?", ["No tiene autoría ni fecha.", "Promete que cura todo y pide datos."], "Sin autoría ni fecha, promesa exagerada y pedido de datos"),
        ("Contrastar", "Una página dice que el planeta más cercano al Sol es Mercurio. Tu libro de Ciencias y el sitio de un museo científico también lo dicen. ¿Qué concluyes?", ["Tres fuentes distintas coinciden.", "Es probable que sea cierto."], "La información es confiable porque varias fuentes coinciden"),
    ],
    mistakes=[
        ("Creer una información porque aparece en el primer resultado.", "Estar primero no la hace verdadera.", "Revisa autoría, fecha, propósito y contrasta."),
        ("Compartir un mensaje que dice «reenvía a 10 personas».", "Puede ser un engaño o una información falsa.", "Verifica y avisa a una persona adulta."),
    ],
    R=[
        ("Buscar la misma información en dos o más fuentes, ¿cómo se llama?", "Contrastar", "Es comparar fuentes distintas."),
        ("Un mensaje que dice «¡hazlo ahora o pierdes el premio!», ¿es señal de engaño?", "Sí", "Apurar y prometer premios es una señal de engaño."),
        ("¿Quién escribió la información? ¿Qué señal es esa?", "La autoría", "Se refiere al autor de la fuente."),
    ],
    C=[
        ("¿Por qué conviene revisar la fecha de una fuente?", "Porque la información puede estar desactualizada", "Algunos datos cambian con el tiempo."),
        ("El candado de la dirección, ¿asegura que el contenido es verdadero?", "No", "Solo indica una conexión privada."),
        ("Si una sola fuente dice algo y ninguna otra coincide, ¿lo das por cierto?", "No", "Todavía falta contrastar."),
    ],
    A=[
        ("¿Cuál es una señal de alerta en un mensaje? A «Publicado por un museo, con autor y fecha», B «¡Compártelo ahora o te pasará algo malo!»", "B", "Apurar y amenazar es señal de engaño; A tiene autoría y fecha."),
        arith("Revisaste 5 fuentes y 4 coinciden en un dato. ¿Cuántas no coinciden?", "5-4", "Se resta lo que coincide del total."),
        ("Quieres contar un dato sobre un animal. ¿Usas un sitio con autor, fecha y de una institución, o uno sin autor?", "El sitio con autor, fecha e institución", "Tiene señales de una fuente confiable."),
    ],
    Z=[
        ("Dos estudiantes comparten una noticia. Una la contrastó con tres fuentes y otro solo la leyó en un mensaje. ¿Cuál es más seguro compartir?", "La que contrastó", "Varias fuentes que coinciden dan más confianza."),
        ("Un mensaje te pide tu clave para entregarte un premio. ¿Qué haces?", "No responder y avisar a una persona adulta", "Pedir datos personales es una señal de engaño."),
    ],
    D=[
        arith("Una información aparece en 2 libros y 3 sitios confiables. ¿En cuántas fuentes coincide?", "2+3", "Se suman todas las fuentes que la confirman."),
        ("Un dato cambia cada semana. La fuente A es confiable pero tiene tres años; la fuente B se publicó ayer y es de una institución conocida. ¿Cuál conviene usar?", "La B", "Es reciente y confiable, y el dato cambia seguido."),
    ],
    ctx=("Para un trabajo sobre volcanes, una página sin autor dice que «todos los volcanes de Chile están por despertar mañana». Tu libro de Ciencias no dice eso. Escribe dos señales de alerta, qué harás y cómo anotarías la fuente que sí uses.", "Señales: sin autor y afirmación exagerada. Contrasto con el libro y otros sitios confiables. Fuente: autor, título del libro o sitio y fecha", "Señales, contraste y fuente."),
    sc=[
        ("¿Cuáles son las cuatro señales de la clase?", "Autoría, fecha, propósito y dirección", "Son las señales para revisar una fuente."),
        ("¿Qué se hace antes de compartir?", "Verificar la fuente", "Evita difundir información falsa."),
        ("¿Qué anotas al usar una información?", "Autor, sitio y fecha", "Así otros pueden comprobarla."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: una página sin autor dice que un jugo cura todas las enfermedades y pide tu correo para enviarte un premio. Caso 2: un museo científico, con autor y fecha de hace un año, explica que la Luna da una vuelta a la Tierra en cerca de un mes. Revisa las cuatro señales, di si la fuente es confiable y qué harías antes de compartirla.",
        "Caso 2: autoría: conocida; fecha: reciente; propósito: informar; dirección: de un museo. Confiable. Antes de compartir, contrasto con mi libro de Ciencias.",
        ["revisa las cuatro señales", "concluye con razón", "propone contrastar", "dice cómo anotaría la fuente"],
        ["ficha con las cuatro señales y decisión"],
        ["creer sin revisar", "olvidar contrastar"],
        "Pregunta: «¿quién lo escribió y dónde más lo puedes comprobar?». Si no sabe, repasen las señales.",
    ),
    reinforce="Elige un dato que hayas oído y piensa en dos fuentes donde podrías comprobarlo.",
    extend="Explica por qué un mensaje que te apura a actuar es una señal de engaño.",
)

# ------------------------------------------------------------------ OA 07, clase 3
reg(
    OA7, 3,
    materials="Hoja y lápiz. Los ejemplos son inventados; no escribas datos personales reales ni contraseñas reales en ninguna actividad.",
    use="Aprenderé qué datos personales no se comparten, cómo cuidar mis contraseñas y cómo respetar la privacidad de otras personas. Sirve para estar seguro o segura al comunicarme en línea.",
    prior=["Sé que no se comparte todo en línea.", "Sé que hay medios públicos y cerrados.", "Sé que debo avisar a una persona adulta si algo me inquieta."],
    explain=[
        "La privacidad es el derecho a decidir qué cosas tuyas conocen otras personas. Los datos personales son los que te identifican: tu nombre completo, tu dirección, tu teléfono, tu colegio, tu ubicación en este momento, tus claves y tus documentos. Estos datos no se publican ni se entregan a personas que no conoces o a páginas que no son seguras.",
        "Una contraseña protege tus cuentas. Una contraseña segura es larga, mezcla letras, números y símbolos, y no usa tu nombre, tu fecha de nacimiento ni palabras fáciles de adivinar. Una frase larga que solo tú recuerdas funciona bien. No se comparte con amistades; se comparte, si hace falta, solo con una persona adulta de tu confianza. No uses la misma en todas las cuentas. Las contraseñas de ejemplo de este cuaderno son solo para practicar: nunca las uses en una cuenta real.",
        "También debes respetar la privacidad de otras personas. Antes de publicar una foto, un nombre o una conversación de alguien, pide permiso y consulta a una persona adulta. Lo que se publica puede quedar guardado mucho tiempo y copiarse, aunque lo borres. Antes de publicar, pregúntate: ¿me gustaría que esto lo vieran mañana? Configura quién puede ver tus cosas y usa los servicios con una persona adulta cerca.",
    ],
    vocab=[("privacidad", "derecho a decidir qué cosas tuyas conocen otras personas"), ("dato personal", "dato que te identifica, como nombre completo o dirección"), ("contraseña", "clave secreta para entrar a una cuenta"), ("permiso", "acuerdo previo de una persona para usar algo suyo"), ("configurar", "elegir quién puede ver o hacer algo")],
    worked=[
        ("Clasificar datos", "Clasifica cada dato como «se puede compartir» o «no se comparte»: tu juego favorito, tu dirección, tu teléfono.", ["Un juego favorito no te identifica.", "Dirección y teléfono sí te identifican."], "Se puede compartir el juego favorito; no se comparten la dirección ni el teléfono"),
        ("Revisar una contraseña", "Compara dos contraseñas de ejemplo inventadas: A «pedro2015» y B «Mi-gato-come-12-peces!». ¿Cuál es más segura y por qué?", ["A usa un nombre y un año fáciles de adivinar.", "B es larga y mezcla palabras, números y símbolos."], "B, porque es larga y difícil de adivinar"),
    ],
    mistakes=[
        ("Compartir la contraseña con una amistad para «probar» que confías.", "Cualquiera con tu clave puede entrar a tu cuenta.", "No la compartas; si hace falta, solo con una persona adulta de confianza."),
        ("Publicar una foto de un compañero sin preguntarle.", "No respetas su privacidad.", "Pide permiso antes de publicar algo de otra persona."),
    ],
    R=[
        ("Tu dirección, ¿es un dato personal?", "Sí", "Te identifica y dice dónde vives."),
        ("¿Se comparte la contraseña con amistades?", "No", "Cualquiera podría entrar a tu cuenta."),
        ("Antes de publicar la foto de otra persona, ¿qué haces?", "Pedir permiso", "Respetas su privacidad."),
    ],
    C=[
        ("¿Por qué no se publica el colegio donde estudias junto con tu nombre completo?", "Porque permite identificar dónde encontrarte", "Son datos que te identifican."),
        ("¿Qué hace más segura a una contraseña?", "Ser larga y mezclar letras, números y símbolos", "Es más difícil de adivinar."),
        ("Algo que publicas en línea y luego borras, ¿puede haber sido copiado antes?", "Sí", "Otras personas pueden haberlo guardado."),
    ],
    A=[
        ("Elige el dato que sí puedes compartir: A tu teléfono, B tu animal favorito, C tu dirección.", "B", "Tu animal favorito no te identifica."),
        arith("Una contraseña de ejemplo tiene 8 letras, 3 números y 2 símbolos. ¿Cuántos caracteres tiene?", "8+3+2", "Se suman letras, números y símbolos."),
        ("Una página desconocida te pide tu nombre completo y tu dirección para participar en un sorteo. ¿Qué haces?", "No entregarlos y avisar a una persona adulta", "Es una posible señal de engaño."),
    ],
    Z=[
        ("Dos contraseñas de ejemplo: A «Sol123» y B «Cada-lunes-leo-9-cuentos?». ¿Cuál es más difícil de adivinar y por qué?", "B, porque es más larga y mezcla caracteres", "A es corta y fácil de adivinar."),
        ("Una compañera te pide una foto del curso para publicarla, pero algunos compañeros no quieren salir. ¿Qué debes hacer?", "No publicarla sin el permiso de todos los que salen y de una persona adulta", "Se debe respetar la privacidad de cada persona."),
    ],
    D=[
        arith("Un servicio permite elegir entre 4 niveles de privacidad. Tú descartas los 2 más abiertos. ¿Cuántos niveles te quedan por elegir?", "4-2", "Se restan los descartados."),
        ("Un mensaje de alguien que no conoces te pide que le envíes una foto tuya. ¿Qué haces?", "No enviarla, no responder y avisar a una persona adulta", "Una persona desconocida pide información personal."),
    ],
    ctx=("Quieres inscribirte en un taller en línea. Te piden tu nombre completo, tu curso, tu dirección y tu teléfono. Escribe cuáles datos no entregarías sin una persona adulta, qué harías antes y cómo sería una contraseña segura de ejemplo.", "No entregaría dirección ni teléfono sin una persona adulta. Antes preguntaría a un adulto si el sitio es seguro. Contraseña de ejemplo: Mi-perro-corre-7-veces!", "Datos protegidos, adulto y contraseña."),
    sc=[
        ("En Tecnología: ¿Qué son los datos personales?", "Datos que te identifican", "Por ejemplo, nombre completo y dirección."),
        ("¿Con quién se comparte la contraseña, si hace falta?", "Solo con una persona adulta de confianza", "Protege tu cuenta."),
        ("¿Qué se pide antes de publicar algo de otra persona?", "Permiso", "Respeta su privacidad."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un formulario en línea pide tu nombre completo, tu curso, tu dirección y tu comida favorita para un concurso. Caso 2: quieres publicar una foto de tu grupo de trabajo. Escribe qué datos o permisos son necesarios, qué no harías y qué le contarías a una persona adulta.",
        "Caso 1: la comida favorita se puede compartir; no entregaría dirección ni nombre completo; contaría a una persona adulta antes de entregar cualquier dato.",
        ["distingue datos que se pueden compartir", "nombra lo que no haría", "menciona pedir permiso o avisar a un adulto", "no escribe datos personales reales"],
        ["lista de datos y decisiones"],
        ["dar datos reales", "olvidar el permiso"],
        "Pregunta: «¿este dato dice quién eres o dónde estás?». Si sí, pídele no compartirlo.",
    ),
    reinforce="Inventa una contraseña segura de ejemplo y no la uses en ninguna cuenta real.",
    extend="Explica por qué el permiso de otras personas es parte de la privacidad.",
)

# ------------------------------------------------------------------ OA 07, clase 4
reg(
    OA7, 4,
    materials="Hoja y lápiz. Los mensajes de los ejemplos son inventados.",
    use="Aprenderé a redactar un mensaje en línea claro y respetuoso, a revisarlo antes de enviar y a actuar si recibo algo que me inquieta. Sirve para comunicarme bien y con seguridad.",
    prior=["Sé elegir un medio en línea.", "Sé verificar una fuente.", "Sé cuidar mis datos personales."],
    explain=[
        "Un mensaje en línea claro tiene destinatario, asunto, saludo, mensaje y despedida. El destinatario es quien lo recibe. El asunto dice en pocas palabras de qué trata, por ejemplo «Informe de Ciencias». El saludo y la despedida muestran respeto. El mensaje va en párrafos cortos y ordenados. Si adjuntas un archivo, dilo en el texto.",
        "La netiqueta son las normas de buen trato en línea. No escribas todo en mayúsculas, porque parece un grito. No insultes ni te burles. No reenvíes cadenas que piden mandar un mensaje a muchas personas. Si citas información de una fuente, di cuál es. Escribe como si hablaras de frente con la persona.",
        "Antes de enviar, revisa: ¿el destinatario es el correcto?, ¿el asunto es claro?, ¿el adjunto es el archivo correcto?, ¿hay datos personales que no deban ir? Si recibes un mensaje que te inquieta, te insulta o te pide datos, no respondas. Guárdalo, cuéntaselo a una persona adulta de confianza y, si el medio lo permite, bloquea a quien lo envió. No estás solo ni sola.",
    ],
    vocab=[("destinatario", "persona que recibe el mensaje"), ("asunto", "frase corta que dice de qué trata el mensaje"), ("netiqueta", "normas de buen trato en línea"), ("bloquear", "impedir que una persona te escriba"), ("cadena", "mensaje que pide reenviarlo a muchas personas")],
    worked=[
        ("Armar un correo", "Debes enviar tu informe a la profesora. Escribe un asunto adecuado y la primera línea.", ["El asunto dice el tema: Informe de Ciencias.", "Saludo y mención del adjunto: «Estimada profesora, le envío mi informe adjunto.»"], "Asunto: Informe de Ciencias. Primera línea: Estimada profesora, le envío mi informe adjunto"),
        ("Qué hacer ante un mensaje que inquieta", "Un desconocido te escribe: «Dime dónde vives y te regalo algo». ¿Qué haces?", ["No respondo ni entrego datos.", "Lo guardo, aviso a una persona adulta de confianza y bloqueo."], "No responder, guardar el mensaje, avisar a una persona adulta y bloquear"),
    ],
    mistakes=[
        ("Escribir todo el mensaje en mayúsculas.", "Parece un grito.", "Usa mayúsculas solo donde corresponde."),
        ("Responder a quien te insulta.", "Puede empeorar la situación.", "No respondas, guarda el mensaje y avisa a una persona adulta."),
    ],
    R=[
        ("La persona que recibe el mensaje, ¿cómo se llama?", "Destinatario", "Es a quien va dirigido."),
        ("Un mensaje todo en mayúsculas, ¿parece un grito?", "Sí", "En línea, las mayúsculas se leen como un grito."),
        ("Si recibes un mensaje que te inquieta, ¿qué haces primero?", "Contárselo a una persona adulta de confianza", "No debes enfrentarlo solo o sola."),
    ],
    C=[
        ("¿Para qué sirve el asunto de un correo?", "Para decir de qué trata", "Ayuda a entender el tema antes de abrirlo."),
        ("Una cadena dice «reenvía a 10 personas o tendrás mala suerte». ¿La reenvías?", "No", "Las cadenas suelen ser engaños y molestan."),
        ("¿Por qué se revisa el destinatario antes de enviar?", "Para no enviarlo a la persona equivocada", "Un error muestra información a quien no corresponde."),
    ],
    A=[
        ("Eliges el mejor asunto para un mensaje con un afiche de la feria. A «Hola», B «Afiche de la feria del curso».", "B", "B dice de qué trata el mensaje."),
        arith("Antes de enviar revisas 4 cosas: destinatario, asunto, adjunto y datos personales. Ya revisaste 3. ¿Cuántas faltan?", "4-3", "Se resta lo revisado del total."),
        ("Recibes un mensaje que te insulta. ¿Respondes con otro insulto o no respondes y avisas a una persona adulta?", "No respondo y aviso a una persona adulta", "Es la forma segura de actuar."),
    ],
    Z=[
        ("Dos estudiantes envían un trabajo. Una puso asunto y saludo; el otro mandó el archivo solo, sin texto. ¿Quién comunica mejor y por qué?", "La que puso asunto y saludo", "El mensaje es claro y respetuoso."),
        ("Un compañero propone responder a quien insultó al curso en el grupo con más insultos. ¿Qué le dices?", "Que no se responde, se guarda y se avisa a un adulto", "Responder con insultos agrava el problema."),
    ],
    D=[
        arith("Un mensaje tiene 5 partes: destinatario, asunto, saludo, mensaje y despedida. Escribiste 3. ¿Cuántas te faltan?", "5-3", "Se resta lo escrito del total."),
        ("Escribes en un mensaje «te adjunto el archivo», pero olvidas adjuntarlo. ¿Qué error es?", "Decir que hay un adjunto sin enviarlo", "Hay que revisar el adjunto antes de enviar."),
    ],
    ctx=("Debes enviar a tu profesora un informe de Ciencias como archivo adjunto. Escribe el asunto, el saludo, una línea del mensaje que mencione el adjunto y la despedida, y una cosa que revisas antes de enviar.", "Asunto: Informe de Ciencias. Saludo: Estimada profesora. Mensaje: le envío mi informe adjunto. Despedida: Atentamente. Reviso el destinatario y el adjunto", "Cuatro partes y una revisión."),
    sc=[
        ("¿Qué partes tiene un mensaje claro?", "Destinatario, asunto, saludo, mensaje y despedida", "Son las cinco partes de la clase."),
        ("¿Qué se hace con un mensaje que inquieta?", "Guardarlo y avisar a una persona adulta", "Es la forma segura de actuar."),
        ("¿Qué se revisa antes de enviar?", "Destinatario, asunto, adjunto y datos personales", "Así se evitan errores."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: envías a tu profesora un informe de Ciencias en un archivo adjunto. Caso 2: invitas a tu curso a una feria el viernes a las 15:00 por mensajería del grupo cerrado. Escribe el mensaje completo con sus partes y la revisión que harías antes de enviar.",
        "Caso 2: Para: grupo del curso. Asunto: Feria del viernes. Hola a todos: los invito a la feria del viernes a las 15:00. Saludos. Reviso que sea el grupo correcto.",
        ["destinatario y asunto", "saludo, mensaje y despedida", "tono respetuoso sin mayúsculas sostenidas", "revisión antes de enviar"],
        ["mensaje con revisión antes de enviar"],
        ["no revisar el destinatario", "tono irrespetuoso"],
        "Pregunta: «¿quién lo recibirá y qué verificaste antes de enviarlo?». Si no lo verificó, pídele revisarlo.",
    ),
    reinforce="Escribe un mensaje corto de agradecimiento con asunto, saludo y despedida, para una persona de tu casa.",
    extend="Explica por qué guardar un mensaje que te inquieta puede ayudar a que una persona adulta te apoye.",
)
