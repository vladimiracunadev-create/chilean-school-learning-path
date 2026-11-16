"""Teatro 3.º y 4.º medio FG: OAC-06 (gestión y difusión de proyectos teatrales), clases 1 a 3. Proyectos, cronogramas y afiches de ejemplo, inventados; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O6 = "FG-TEAT-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (proyecto de difusión de ejemplo, inventado). Un grupo presentará «Los paraguas» el viernes a las 12:00 en el gimnasio del colegio, con entrada gratuita. "
     "Aforo: 80 personas. Público objetivo: estudiantes de 1.º y 2.º medio. Medios disponibles: el diario mural, la radio del colegio (30 segundos al aire), la lista de mensajes del curso y un afiche digital.")
build(
    O6, 1, F,
    use="Aprenderé a diseñar un proyecto de difusión de una obra: definir objetivo, público y mensaje, y elegir medios (impresos, radiales y digitales) que sirvan a ese público de forma veraz y segura.",
    prior=["Sé que cada obra tiene un propósito y un público específico.", "Sé que las imágenes y datos de las personas requieren consentimiento.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Difundir una obra es hacer que su público se entere y quiera asistir. Un proyecto de difusión tiene cuatro decisiones básicas. El objetivo dice qué se quiere lograr, por ejemplo que asistan 60 de las 80 personas que caben. El público objetivo es el grupo al que se quiere llegar. El mensaje contiene los datos clave: qué se presenta, cuándo, dónde, cuánto cuesta o si es gratis, y quién puede asistir. Los medios son los canales con los que se comunica el mensaje.",
        "Los medios pueden ser impresos (afiche, programa de mano, diario mural), sonoros (radio escolar) o digitales (afiche digital, lista de mensajes del curso, página del colegio), que son las TIC, es decir, las tecnologías de la información y la comunicación. Cada medio tiene ventajas y límites: el diario mural lo ve quien pasa por el pasillo, la radio llega a todo el colegio pero solo dura unos segundos, y la lista del curso llega a quienes están en ella. Se elige según dónde está el público.",
        "La difusión es veraz: no promete lo que la obra no ofrece, no engaña con datos falsos y respeta el contenido apropiado a la edad. También cuida a las personas: se publican solo los datos necesarios, sin teléfonos ni direcciones personales, y las imágenes de personas necesitan su consentimiento.",
    ],
    vocab=[("difusión", "acción de dar a conocer una obra para que su público se entere"), ("público objetivo", "grupo de personas al que se dirige la difusión"), ("mensaje", "datos clave que se comunican: qué, cuándo, dónde y para quién"), ("medio", "canal con el que se comunica el mensaje"), ("TIC", "tecnologías de la información y la comunicación"), ("aforo", "cantidad máxima de personas que caben en un lugar")],
    worked=[
        ("Definir un objetivo", "Un grupo quiere llenar el 50 % de un aforo de 120 personas. ¿Cuántas personas son?", ["Calculo 120 × 50 ÷ 100.", "El resultado es 60."], "60 personas"),
        ("Elegir un medio", "El público objetivo son estudiantes que pasan por el pasillo central. ¿Qué medio es útil?", ["Un afiche en el diario mural llega a quienes pasan por allí.", "La lista de mensajes de otro curso no llegaría a este público."], "El diario mural"),
    ],
    mistakes=[("Hacer un afiche sin la hora o el lugar.", "Sin esos datos el público no puede asistir.", "Incluye qué, cuándo, dónde y para quién."),
              ("Difundir solo por el medio que más le gusta al grupo.", "El público puede no usar ese medio.", "Elige los medios según dónde está el público.")],
    T=[
        ('abc', '¿Qué es el público objetivo de una difusión?', 'El grupo de personas al que se quiere llegar con el mensaje', 'Todas las personas del país que tengan un teléfono y puedan ver la publicación en línea', 'El grupo de amigos de quienes actúan en la obra', 'Es el grupo concreto al que se dirige la difusión.'),
        ('abc', '{F} ¿Cuál es el público objetivo de este proyecto?', 'Estudiantes de 1.º y 2.º medio', 'Todo el barrio del colegio', 'Familias de estudiantes de básica', 'La ficha lo indica: estudiantes de 1.º y 2.º medio.'),
        ('abc', '{F} ¿Qué es el aforo de este proyecto?', 'La cantidad máxima de personas que caben en el gimnasio: 80', 'El número de intérpretes: cuatro', 'El tiempo que dura la función: ocho minutos', 'El aforo es el máximo de personas que cabe en el gimnasio.'),
        ('abc', '¿Qué datos mínimos debe tener el mensaje de difusión?', 'Qué se presenta, cuándo, dónde, si es gratis y quién puede asistir', 'El nombre completo y el teléfono personal de cada integrante del grupo, para que puedan contactarlos', 'Solo el título de la obra y una imagen atractiva', 'Esos datos permiten asistir; los datos personales no son necesarios.'),
        ('abc', '{F} La radio del colegio da 30 segundos al aire. ¿Qué conviene decir?', 'Título, día, hora, lugar y que la entrada es gratuita', 'La historia completa de la obra con todos sus detalles', 'Una lista con todos los nombres de los integrantes', 'En poco tiempo se entregan los datos clave que permiten asistir.'),
        ('abc', '¿Qué significa difundir de forma veraz?', 'No prometer lo que la obra no ofrece ni dar datos falsos', 'Exagerar un poco para atraer a más gente', 'Ocultar detalles importantes, como la hora, para generar curiosidad en el público', 'La veracidad mantiene la confianza del público.'),
        ('=', '{F} El grupo quiere que asista el 75 % del aforo. ¿Cuántas personas son?', '80*75//100', 'Se calcula el 75 % de 80.', ' personas'),
        ('abc', '{F} ¿Qué limitación tiene la radio escolar como medio?', 'Solo dura unos pocos segundos y no deja un dato escrito', 'No llega a ningún estudiante del colegio porque solo la escuchan los docentes', 'Solo puede usarse para dar noticias deportivas', 'El mensaje es breve y desaparece, por lo que conviene complementarlo.'),
        ('abc', 'Un grupo quiere poner en el afiche el teléfono personal de una integrante para que consulten. ¿Qué conviene?', 'No incluirlo y usar un contacto del curso o del colegio autorizado', 'Incluirlo, porque así el público se contacta rápido y puede resolver todas sus dudas', 'Incluirlo solo en la versión digital del afiche', 'El teléfono personal de una integrante la expone sin necesidad.'),
        ('abc', 'Quieres llegar a estudiantes que casi no usan redes. ¿Qué combinación de medios sirve más?', 'Diario mural, radio escolar y comentarios en las salas', 'Una publicación en un perfil nuevo creado para la función', 'Un correo masivo a personas que nunca han ido al colegio', 'Se eligen los medios que el público realmente usa.'),
        ('abc', 'Un grupo difunde que la entrada es gratuita, pero el día de la función cobra una cuota. ¿Qué falló?', 'La difusión no fue veraz y engañó al público', 'El aforo estaba mal calculado', 'La radio habló muy rápido', 'Prometer algo que luego no se cumple pierde la confianza del público.'),
        ('=', 'La función tiene aforo de 80 personas. Se repartirán invitaciones al 60 % del aforo. ¿Cuántas invitaciones son?', '80*60//100', 'Se calcula el 60 % del aforo.', ' invitaciones'),
        ('abc', 'Se difunde el mismo mensaje por tres medios y el 90 % de los asistentes dice que lo vio en la lista de mensajes. ¿Qué conviene hacer en la próxima difusión?', 'Reforzar ese medio y mantener los otros como apoyo', 'Eliminar la lista de mensajes porque ya funcionó', 'Dejar de difundir porque ya hay público suficiente', 'El dato muestra qué medio funciona más, sin descartar los complementarios.'),
    ],
    ctx=('ab', 'El grupo no sabe si el gimnasio está disponible a esa hora. ¿Qué hace antes de difundir?', 'Confirmar el lugar y la hora con quien lo administra', 'Difundir primero y ver después si se puede', 'Difundir un dato sin confirmar puede obligar a cancelar y confundir al público.'),
    sc=[
        ("En Teatro: ¿qué es el aforo?", "La cantidad máxima de personas que caben en un lugar", "Se usa para calcular a cuántas personas invitar."),
        ("¿Qué datos mínimos lleva el mensaje de una difusión?", "Qué se presenta, cuándo, dónde, si es gratis y quién puede asistir", "Son los datos que permiten asistir."),
        ("¿Se puede publicar el teléfono personal de una integrante en el afiche?", "No, se usa un contacto autorizado del colegio o del curso", "Los datos personales de las integrantes se protegen siempre."),
    ],
    op=("Imagina que presentarás una escena de ejemplo en tu colegio. Escribe: el objetivo de difusión con una cifra, tu público objetivo, el mensaje con los cinco datos clave y dos medios que elegirías con una razón para cada uno. No incluyas datos personales.",
        "Objetivo: que asistan 45 de las 60 sillas. Público: estudiantes de 3.º y 4.º medio. Mensaje: «Los paraguas», jueves 12:00, gimnasio, entrada gratuita, para estudiantes de enseñanza media. Medios: radio escolar, porque llega a todos; diario mural, porque lo ven en el pasillo.",
        ["objetivo con cifra", "público objetivo claro", "mensaje con los cinco datos", "dos medios con razón", "sin datos personales"],
        ["hoja con la planificación de difusión"],
        ["olvidar la hora o el lugar", "incluir datos personales"],
        "Pregunta: «¿una persona que lee esto sabe cuándo y dónde ir?». Debe responder que sí."),
    reinforce="Escribe un mensaje de 20 palabras para anunciar una actividad de tu colegio, con qué, cuándo, dónde y para quién.",
    extend="Explica por qué usar varios medios coordinados suele llegar mejor que usar solo uno.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (cronograma de ejemplo, inventado). Función el viernes. Tareas y duración: redactar el mensaje, 1 día; pedir autorización del gimnasio, 1 día (se hace a la vez que el mensaje); "
     "diseñar el afiche digital, 2 días (empieza cuando el mensaje está listo); imprimir los afiches, 1 día (empieza cuando el afiche está listo); pegar los afiches y avisar en la radio, 1 día. "
     "Equipo de 5: coordinación, contenido, diseño, medios y logística.")
build(
    O6, 2, F,
    use="Aprenderé a gestionar un proyecto de difusión en equipo: repartir roles, ordenar tareas con un cronograma, respetar dependencias y usar herramientas colaborativas cuidando la privacidad.",
    prior=["Sé qué es un objetivo, un público y un mensaje.", "Sé trabajar en equipo con acuerdos.", "Sé sumar y contar días."],
    explain=[
        "Gestionar un proyecto es organizar quién hace qué y cuándo para lograr el objetivo. En un equipo de difusión suelen existir roles como coordinación (cuida los plazos y el propósito), contenido (redacta el mensaje), diseño (crea el afiche), medios (publica y avisa por los canales) y logística (pide permisos, imprime y reserva el lugar). Todos opinan en las decisiones comunes y cada tarea tiene una persona responsable.",
        "El cronograma ordena las tareas en el tiempo. Algunas tareas dependen de otras: el afiche no puede imprimirse si aún no está diseñado. Otras pueden hacerse a la vez, como redactar el mensaje y pedir un permiso. El camino más largo de tareas que dependen unas de otras define cuánto tarda el proyecto. Conviene dejar un margen para imprevistos.",
        "Para trabajar de forma colaborativa se pueden usar herramientas como un documento compartido o un calendario del curso, supervisadas por el docente. Se cuida la privacidad: acceso solo para el equipo, sin datos personales innecesarios y sin compartir cuentas ni claves. Si hay un desacuerdo que no se resuelve o alguien se siente presionado, se avisa a una persona adulta.",
    ],
    vocab=[("rol", "conjunto de tareas que asume una persona en el equipo"), ("cronograma", "orden de las tareas en el tiempo, con sus plazos"), ("dependencia", "relación entre tareas en que una no puede empezar si no termina otra"), ("responsable", "persona a cargo de que una tarea se cumpla"), ("herramienta colaborativa", "documento, calendario u otro medio que el equipo usa en conjunto")],
    worked=[
        ("Reconocer una dependencia", "El afiche debe diseñarse antes de imprimirse. ¿Cómo se relacionan esas tareas?", ["La impresión depende del diseño: no puede empezar antes.", "Se anotan en el cronograma una después de la otra."], "La impresión depende del diseño"),
        ("Calcular el camino más largo", "Mensaje 1 día, luego diseño 2 días, luego impresión 1 día. ¿Cuántos días toma esa cadena?", ["Se suman los días de las tareas que van una tras otra.", "1 + 2 + 1 = 4."], "4 días"),
    ],
    mistakes=[("Poner todas las tareas en el mismo día sin mirar dependencias.", "Algunas no pueden empezar hasta que otra termine.", "Ordena las tareas que dependen unas de otras."),
              ("Compartir una clave de cuenta del colegio por mensajes del curso.", "Cualquiera podría usarla y se pierde el control.", "Usa herramientas autorizadas y accesos individuales.")],
    T=[
        ('abc', '¿Qué es una dependencia entre tareas?', 'Una relación en que una tarea no puede empezar hasta que termine otra', 'Un acuerdo entre dos personas para repartirse el trabajo y no ayudarse después', 'Una tarea que se hace siempre el último día', 'Una dependencia fija el orden entre tareas.'),
        ('abc', '{F} ¿Qué tarea depende del diseño del afiche?', 'Imprimir los afiches', 'Redactar el mensaje', 'Pedir autorización del gimnasio', 'La ficha indica que imprimir empieza cuando el afiche está listo.'),
        ('abc', '{F} ¿Qué dos tareas se pueden hacer a la vez?', 'Redactar el mensaje y pedir la autorización del gimnasio', 'Diseñar el afiche digital e imprimir los afiches', 'Imprimir los afiches y pegarlos en el diario mural', 'La ficha dice que el permiso se hace a la vez que el mensaje; las otras parejas dependen una de otra.'),
        ('abc', '¿Qué hace la persona en el rol de coordinación?', 'Cuida plazos y propósito, y mantiene al equipo informado', 'Diseña todos los materiales de difusión sin consultar', 'Redacta el mensaje y decide solo qué medios usar', 'La coordinación organiza sin reemplazar los otros roles.'),
        ('abc', '¿Por qué conviene dejar un margen en el cronograma?', 'Para absorber imprevistos sin atrasar la función', 'Para que el equipo tenga menos tareas', 'Para no tener que definir responsables', 'Los imprevistos ocurren, y el margen evita que afecten la fecha.'),
        ('abc', '¿Cuál es una herramienta colaborativa adecuada para el equipo?', 'Un documento compartido con acceso solo para el equipo y el docente', 'Una cuenta personal de una integrante con su clave compartida', 'Una publicación abierta en una red con todos los datos del grupo', 'El acceso controlado cuida la privacidad y permite colaborar.'),
        ('=', '{F} Mensaje 1 día, diseño 2 días, impresión 1 día y pegado y radio 1 día, una tarea tras otra. ¿Cuántos días toma esa cadena?', '1+2+1+1', 'Se suman los días de las tareas que van una después de la otra.', ' días'),
        ('abc', '{F} Si el permiso del gimnasio se demora 2 días en lugar de 1 y se hacía a la vez que el mensaje, ¿cambia el plazo total de la cadena principal?', 'No, porque sigue siendo más corto que la cadena de mensaje, diseño, impresión y pegado', 'Sí, porque todas las tareas del cronograma deben terminar el mismo día, sin importar cuánto duren', 'Sí, porque el permiso se hace antes que el mensaje', 'El permiso corre en paralelo; mientras no supere la cadena principal, el plazo no cambia.'),
        ('abc', 'Dos integrantes quieren hacer la misma tarea y ninguna cede. ¿Qué conviene?', 'Acordar criterios, repartir tareas por turnos y, si no se resuelve, pedir ayuda a una persona adulta', 'Que cada una la haga por separado y elegir la mejor sin explicar el motivo ni escuchar a la otra persona', 'Que decida quien tiene más seguidores en redes', 'Los acuerdos claros evitan conflictos y la ayuda adulta apoya si no se resuelve.'),
        ('abc', 'Un integrante propone crear un grupo de mensajería con personas ajenas al colegio para organizar el trabajo. ¿Qué conviene?', 'Usar solo los canales autorizados por el docente y limitar el grupo al equipo', 'Crearlo para tener ayuda de muchos y avisar después al docente', 'Incluir a cualquiera que quiera colaborar, sin revisar quiénes son', 'Los datos del equipo se protegen limitando el acceso a quienes corresponde.'),
        ('abc', 'El diseñador entrega el afiche un día más tarde de lo previsto. ¿Qué puede hacer el equipo?', 'Ajustar el cronograma, revisar qué tareas se atrasan y usar el margen', 'Ignorar el atraso y mantener las fechas originales, porque el cronograma ya está decidido', 'Cancelar la función para evitar problemas', 'El cronograma se ajusta con base en las dependencias y el margen.'),
        ('=', 'Un equipo de 5 personas tiene 15 tareas repartidas en partes iguales. ¿Cuántas tareas tiene cada integrante?', '15//5', 'Se divide el total de tareas entre las integrantes.', ' tareas'),
        ('abc', 'El equipo quiere cuidar la privacidad en su calendario compartido. ¿Qué mejor decisión toma?', 'Escribir las tareas y los responsables sin datos personales innecesarios', 'Anotar el domicilio de cada integrante para saber dónde se reúnen', 'Compartir el calendario con todos los cursos del colegio sin revisar el contenido', 'El calendario debe incluir solo lo necesario para organizar el trabajo.'),
    ],
    ctx=('ab', 'Alguien del equipo no cumplió su tarea a tiempo. ¿Qué hace el equipo?', 'Conversa con respeto, revisa qué pasó y reorganiza la tarea', 'Lo excluye del proyecto sin escucharlo', 'Escuchar y reorganizar mantiene el proyecto y el respeto entre integrantes.'),
    sc=[
        ("En Teatro: ¿qué es un cronograma?", "El orden de las tareas en el tiempo, con sus plazos", "Permite saber qué se hace primero y cuánto tarda."),
        ("¿Qué es una dependencia entre tareas?", "Una tarea que no puede empezar hasta que termine otra", "Define el orden en que deben hacerse las tareas."),
        ("¿Qué se evita al usar herramientas colaborativas?", "Compartir claves o datos personales innecesarios", "Así la privacidad del equipo queda bien cuidada."),
    ],
    op=("Imagina un equipo de cuatro personas que debe difundir una función en dos semanas. Escribe: los roles (quién hace qué), una lista de cinco tareas con su duración en días, una dependencia entre dos tareas y cuántos días tarda la cadena más larga. Indica una herramienta colaborativa y cómo cuidas la privacidad.",
        "Roles: coordinación, contenido, diseño y logística. Tareas: mensaje 1 día, permiso 1 día (a la vez), afiche 2 días, impresión 1 día, pegado 1 día. Dependencia: la impresión depende del afiche. Cadena más larga: 1+2+1+1=5 días. Documento compartido solo para el equipo y el docente, sin datos personales.",
        ["reparte los roles", "cinco tareas con duración", "una dependencia correcta", "calcula la cadena más larga", "cuida la privacidad"],
        ["hoja con roles, tareas, dependencia y días"],
        ["no respetar dependencias", "compartir datos personales"],
        "Pregunta: «¿qué tarea no puede empezar antes de que termine otra?». Debe nombrarla."),
    reinforce="Haz un cronograma de cuatro tareas para organizar una actividad de tu casa o curso y marca cuáles dependen de otras.",
    extend="Explica por qué el camino más largo de tareas dependientes determina cuánto dura el proyecto.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (borrador de afiche de ejemplo, inventado). Elementos: título «Los paraguas»; fecha, hora y lugar; una foto de un ensayo con 4 integrantes (uno aún no dio su permiso); "
     "una imagen de un cartel de otra obra copiada de internet; el teléfono personal de una integrante; letras claras sobre fondo oscuro.")
build(
    O6, 3, F,
    use="Aprenderé a usar medios y TIC para difundir una obra (afiche, programa, radio, mensajes del curso) y a decidir con responsabilidad sobre imágenes, derechos de autor, consentimiento, privacidad y accesibilidad.",
    prior=["Sé qué datos lleva un mensaje de difusión.", "Sé que las imágenes de personas necesitan su permiso.", "Sé que la música y las imágenes de otros tienen autoría."],
    explain=[
        "Un material de difusión comunica mejor si es claro: un título visible, los datos clave ordenados y letras legibles con buen contraste con el fondo. También ayuda que sea accesible: texto suficientemente grande, imágenes con una descripción escrita para quien no las puede ver y un mensaje que se entienda sin necesidad de explicación adicional.",
        "Las TIC ofrecen muchos recursos, pero se usan con responsabilidad. Las imágenes y la música tienen autoría y derechos de autor: se usan las propias o las que cuenten con permiso o licencia, y se indica quién las creó. Copiar un cartel de otra obra sin permiso no es válido. Las fotos de personas necesitan su consentimiento, y si son menores de edad, también el de su persona adulta responsable. No se publican teléfonos, direcciones ni otros datos personales.",
        "Los canales también se eligen con cuidado. El diario mural, la radio escolar y las listas del curso supervisadas por el docente son más seguros que las redes abiertas. Si alguien recibe mensajes ofensivos o hostiles por la difusión, no responde con insultos, guarda captura, bloquea y avisa a una persona adulta de confianza.",
    ],
    vocab=[("contraste", "diferencia de luz o color que permite leer un texto"), ("accesibilidad", "condiciones para que todas las personas puedan acceder al mensaje"), ("derecho de autor", "derecho de quien creó una obra a decidir cómo se usa"), ("licencia", "permiso que indica en qué condiciones se puede usar una obra"), ("consentimiento", "autorización libre de una persona para usar su imagen")],
    worked=[
        ("Revisar un afiche", "Un afiche tiene letras amarillas muy claras sobre fondo blanco. ¿Qué problema tiene?", ["Hay poco contraste y el texto cuesta leerse.", "Conviene cambiar el color de las letras o del fondo."], "Poco contraste; se cambian colores"),
        ("Decidir sobre una imagen", "Un grupo quiere usar una foto de un cartel de otra obra que encontró en internet. ¿Qué corresponde?", ["La imagen tiene autoría y derechos; no se puede usar sin permiso.", "Se crea una imagen propia o se usa una con licencia que lo permita."], "Crear una imagen propia o usar una con permiso"),
    ],
    mistakes=[("Usar cualquier imagen de internet porque «está a la vista de todos».", "Que se pueda ver no significa que se pueda usar.", "Usa imágenes propias o con permiso y cita al autor."),
              ("Subir una foto del ensayo sin preguntar a todas las personas que aparecen.", "Cada persona decide sobre su imagen.", "Pide el consentimiento antes y publica solo si todos aceptan.")],
    T=[
        ('abc', '{F} ¿Qué elemento del afiche necesita corregirse por la privacidad de una persona?', 'El teléfono personal de una integrante', 'El título «Los paraguas» en letras grandes', 'La fecha, la hora y el lugar de la función', 'Un teléfono personal expone a la integrante; la fecha, la hora y el lugar son datos necesarios.'),
        ('abc', '{F} ¿Qué problema tiene la foto del ensayo con 4 integrantes?', 'Uno de ellos aún no dio su permiso para aparecer', 'Es una foto muy pequeña para el afiche', 'No tiene el nombre de la obra escrito sobre ella', 'La imagen de una persona requiere su consentimiento.'),
        ('abc', '{F} ¿Qué problema tiene la imagen copiada de internet?', 'Es de otra obra y tiene autoría, por lo que no se puede usar sin permiso', 'Es de un tamaño distinto al del afiche y por eso se vería deformada al imprimirla', 'Está en blanco y negro', 'La autoría y los derechos exigen permiso o una imagen propia.'),
        ('abc', '{F} ¿Qué decisión del borrador favorece la lectura?', 'Las letras claras sobre fondo oscuro, que dan buen contraste', 'La imagen copiada de otra obra', 'La foto de un ensayo con personas', 'El contraste entre letras y fondo ayuda a leer.'),
        ('abc', '¿Qué es una licencia que permite usar una imagen?', 'Un permiso que indica en qué condiciones se puede usar la obra', 'Un número que identifica la imagen en internet y permite buscarla en otros sitios', 'La opinión de quien la encontró primero', 'La licencia dice qué usos están permitidos y con qué condiciones.'),
        ('abc', 'Para que un afiche sea accesible, ¿qué conviene?', 'Texto suficientemente grande, buen contraste y descripción escrita de las imágenes', 'Letras pequeñas y decorativas, de colores claros, para que el afiche se vea elegante', 'Solo imágenes para que se entienda sin leer', 'Un mensaje claro y descrito llega a más personas.'),
        ('=', 'Un grupo reúne 5 imágenes para el afiche: 2 propias, 1 con licencia que permite usarla citando a su autor y 2 copiadas sin permiso. ¿Cuántas imágenes puede usar el grupo?', '2+1', 'Se cuentan las propias y la que tiene licencia; las copiadas sin permiso no se pueden usar.', ' imágenes'),
        ('abc', 'Un grupo quiere usar una música conocida en un video de difusión. ¿Qué conviene?', 'Crear una música propia o pedir permiso de uso antes', 'Usarla porque es solo para el colegio', 'Usarla y avisar después si alguien reclama', 'La música tiene autoría y se usa con permiso.'),
        ('abc', 'Alguien comenta en la lista del curso: «esos actores son unos inútiles». ¿Cómo responde el grupo?', 'No responde con insultos, guarda captura y avisa a una persona adulta si el mensaje se repite', 'Responde con otro insulto para defenderse delante de todo el curso', 'Borra la lista para que nadie lo vea', 'Se evita escalar el conflicto y se deja evidencia para pedir ayuda.'),
        ('abc', 'Un afiche pide a la gente que envíe su nombre completo, curso y teléfono para reservar un lugar gratuito. ¿Qué conviene cambiar?', 'Pedir solo los datos necesarios, o no pedir reserva si la entrada es libre', 'Pedir además la dirección de cada persona', 'Dejar los datos como están, porque nadie los va a usar para nada más que reservar el lugar', 'Se piden solo los datos mínimos, y si no son necesarios, no se piden.'),
        ('abc', 'Para publicar una foto del ensayo con 4 integrantes, uno de ellos dice que no quiere aparecer. ¿Qué decisión respeta el consentimiento?', 'No usar esa foto o recortar para que no aparezca, si él lo acepta', 'Publicarla igual porque la mayoría quiere y el desacuerdo de una persona no cuenta', 'Publicarla y borrarla si alguien reclama más tarde', 'Cada persona decide sobre su imagen y una mayoría no la reemplaza.'),
        ('=', 'Se imprimirán 50 afiches. Cada afiche usa 2 hojas. ¿Cuántas hojas se necesitan?', '50*2', 'Se multiplican los afiches por las hojas de cada uno.', ' hojas'),
        ('abc', 'Un grupo quiere asegurarse de que el mensaje de difusión sea veraz y respetuoso antes de publicarlo. ¿Qué hace?', 'Hace que una persona ajena al equipo lo lea y el docente lo revise', 'Lo publica rápido para no perder tiempo y corrige después si alguien detecta un error', 'Pregunta a las redes qué les parece antes de decidir', 'Una revisión previa detecta errores de datos y de tono antes de publicar.'),
    ],
    ctx=('ab', 'Una integrante pide que se saque su foto del afiche después de verlo. ¿Qué hace el grupo?', 'La saca de inmediato y agradece que lo haya dicho', 'Mantiene la foto porque ya se imprimió', 'El consentimiento puede retirarse y el grupo debe respetarlo.'),
    sc=[
        ("En Teatro: ¿qué es la accesibilidad en un material de difusión?", "Condiciones para que todas las personas puedan entender el mensaje", "Incluye contraste, tamaño del texto y descripciones."),
        ("¿Se puede usar una imagen copiada de internet sin permiso?", "No, tiene autoría y derechos de autor", "Que se pueda ver no significa que se pueda usar."),
        ("¿Qué se hace ante mensajes ofensivos en línea sobre la difusión?", "No responder con insultos, guardar captura, bloquear y avisar a una persona adulta", "Es el protocolo seguro para cuidarse y pedir ayuda."),
    ],
    op=("Diseña, escribiendo, un afiche de ejemplo para una función de tu colegio: indica el título, los cinco datos clave, qué imagen usarías (propia o con permiso), cómo asegurarías el contraste y la accesibilidad, y qué datos no incluirías por privacidad.",
        "Título «Los paraguas»; jueves 12:00, gimnasio, entrada gratuita, para estudiantes de enseñanza media. Imagen: dibujo hecho por el grupo. Letras blancas grandes sobre fondo azul oscuro y descripción escrita de la imagen. No incluyo teléfonos personales ni nombres sin permiso.",
        ["título y cinco datos", "imagen propia o con permiso", "contraste y accesibilidad", "no incluye datos personales"],
        ["descripción del afiche"],
        ["copiar imágenes sin permiso", "poner teléfonos personales"],
        "Pregunta: «¿quién creó esta imagen y tienes permiso?». Debe responder."),
    reinforce="Dibuja o describe un afiche para una actividad inventada con letras de buen contraste y una imagen creada por ti.",
    extend="Explica por qué «cualquier imagen que está en internet» no puede usarse en un afiche sin pensar en su autoría.",
)
