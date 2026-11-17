"""Artes visuales, audiovisuales y multimediales 3.º y 4.º medio HC: OAC-03 (presentaciones a públicos específicos) y OAC-04 (análisis estético). Obras y fichas inventadas; sin imágenes, audio, video ni software reales."""
from __future__ import annotations

from hc_avam_common import build

O3 = "AR-AVAM-3y4-OAC-03"
O4 = "AR-AVAM-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (públicos de ejemplo, inventados). Muestra del proyecto «Afiches sobre reciclaje» de un curso ficticio. Propósito: comunicar el proyecto mostrando su proceso y su resultado. "
     "Público P1: familias que visitan el liceo, con 15 minutos disponibles y edades mixtas. "
     "Público P2: estudiantes de 1.º medio, curiosos, que quieren ver y probar. "
     "Público P3: jurado de un concurso escolar, que busca proceso, criterios y coherencia con el propósito. "
     "La muestra tiene un panel con espacio para 80 palabras.")
build(
    O3, 1, F,
    use="Aprenderé a analizar a un público específico y a adaptar el propósito, el contenido y el formato de una presentación a sus necesidades.",
    prior=["Sé definir el mensaje y el destinatario de un proyecto.", "Sé registrar el proceso.", "Sé calcular tiempos y cantidades pequeñas."],
    explain=[
        "Presentar una obra o un proyecto es comunicar su propósito, su proceso y su resultado a un público. Un público específico es un grupo concreto de personas, con edades, conocimientos, tiempo y expectativas que se pueden describir. Una presentación que sirve para todos por igual casi nunca sirve bien a nadie; por eso se analiza primero a quién va dirigida.",
        "Para analizar al público se responden cuatro preguntas: quiénes son, qué saben del tema, cuánto tiempo tienen y qué esperan o necesitan. Con las respuestas se adaptan las decisiones: el lenguaje (técnico o cotidiano), la cantidad de texto, el formato (panel, recorrido guiado, demostración) y la duración. También se piensa en la accesibilidad: letra grande y de buen contraste, espacios despejados y descripciones de las obras para quienes no las puedan ver bien.",
        "Gestionar una presentación significa organizarla: definir tareas, responsables, tiempos y recursos, y revisar al final si se logró el propósito. En sala se trabaja con papel y lápiz; ninguna actividad exige materiales peligrosos ni software real.",
    ],
    vocab=[("público específico", "grupo concreto de personas con características definidas"), ("expectativa", "lo que el público espera de la presentación"), ("formato", "forma de presentar: panel, recorrido, demostración"), ("accesibilidad", "condiciones para que más personas puedan participar"), ("gestionar", "organizar tareas, tiempos y recursos")],
    worked=[
        ("Analizar un público", "Con la ficha, describe al público P1 con las cuatro preguntas.", ["Quiénes: familias; qué saben: lo básico del liceo; tiempo: 15 minutos.", "Esperan: entender de qué trata el proyecto de forma rápida."], "Familias con poco tiempo que esperan una presentación breve y clara"),
        ("Calcular el espacio", "El panel permite 80 palabras. Si el título y la presentación del proyecto usan 25, ¿cuántas quedan?", ["Se resta lo usado al máximo.", "80 − 25 = 55."], "55 palabras"),
    ],
    mistakes=[("Hacer una sola presentación igual para todos los públicos.", "Cada público tiene un tiempo, un nivel y una necesidad distintos.", "Adapta el lenguaje, la cantidad de texto y el formato a cada público."),
              ("Llenar el panel de texto técnico para que «se vea serio».", "El público con poco tiempo no lo lee y no entiende el proyecto.", "Selecciona lo esencial y usa lenguaje claro.")],
    T=[
        ('abc', '¿Qué es un público específico?', 'Un grupo concreto de personas con características que se pueden describir', 'Cualquier persona que pase por el lugar', 'El docente que pone la nota', 'Un público específico se describe por sus características; no es cualquiera ni quien evalúa.'),
        ('abc', '{F} ¿Qué necesita el público P1?', 'Una presentación breve, con textos cortos y lenguaje claro', 'Una exposición larga con vocabulario técnico', 'Una lista de materiales y precios', 'P1 tiene 15 minutos y edades mixtas, así que necesita brevedad y claridad.'),
        ('abc', '{F} ¿Qué busca el jurado P3?', 'Proceso, criterios y coherencia con el propósito', 'Solo que haya muchos adornos', 'Que la muestra dure lo menos posible', 'La ficha indica que P3 busca proceso, criterios y coherencia.'),
        ('=', '{F} Las familias recorrerán 3 estaciones del mismo largo en los 15 minutos disponibles. ¿Cuántos minutos corresponden a cada una?', '15//3', 'Se reparte el tiempo disponible en partes iguales.', ' minutos'),
        ('abc', '¿Qué conviene hacer primero al planificar una presentación?', 'Analizar al público y definir el propósito', 'Elegir los adornos y los colores', 'Imprimir todas las obras', 'Primero se sabe a quién y para qué; el resto se decide después.'),
        ('abc', '{F} Para el público P2, que quiere ver y probar, ¿qué decisión es coherente?', 'Incluir una estación con un ejercicio breve y seguro con papel y lápiz', 'Dejar solo un cartel con mucho texto', 'Prohibirles acercarse a las obras', 'P2 quiere probar, así que una actividad breve y segura se adapta a su interés.'),
        ('abc', '{F} Un grupo usa el mismo texto técnico largo para P1, P2 y P3. ¿Cuál es el problema?', 'No se adapta: P1 no lo leerá por falta de tiempo y P3 necesita ver el proceso', 'Ninguno, porque un solo texto ahorra tiempo', 'El texto es bueno si es muy largo', 'Cada público necesita un contenido y una extensión distintos.'),
        ('abc', '{F} ¿Cuál es el propósito de la muestra de la ficha?', 'Comunicar el proyecto mostrando su proceso y su resultado', 'Vender los afiches a las familias', 'Elegir al mejor estudiante del curso', 'La ficha define el propósito como comunicar proceso y resultado.'),
        ('=', '{F} Una estación explica el proceso en 40 palabras y otra el resultado en 25. ¿Cuántas palabras libres quedan en el panel?', '80-40-25', 'Se restan las palabras usadas al máximo del panel.', ' palabras'),
        ('abc', '{F} ¿Qué material conviene agregar para el jurado P3?', 'Bocetos y registro de decisiones del proyecto', 'Solo la obra final enmarcada', 'Una lista de los compañeros ausentes', 'El jurado busca proceso y criterios, que se muestran con bocetos y registro.'),
        ('abc', 'Una persona con baja visión visitará la muestra. ¿Qué decisión ayuda?', 'Usar letras grandes con buen contraste y ofrecer una descripción de las obras', 'Usar letras pequeñas y claras en un tono pastel', 'Quitar los textos para no confundir', 'La letra grande, el contraste y la descripción amplían el acceso.'),
        ('abc', 'Un estudiante dice que al público se lo conoce adivinando. ¿Qué es mejor?', 'Preguntar a representantes del público o al docente y observar sus condiciones', 'Suponer que todos tienen el mismo interés', 'No tomar en cuenta al público', 'Se conoce al público informándose, no adivinando.'),
        ('abc', 'Una invitación para presentar ante familias no dice cuánto durará. ¿Qué hace el grupo?', 'Pregunta la duración y el espacio, y adapta el plan', 'Prepara una exposición de una hora sin consultar', 'Cancela la presentación', 'Se pregunta lo que falta para adaptar el plan.'),
    ],
    ctx=('abc', 'Un grupo debe presentar su proyecto a P1 y P3 el mismo día. ¿Qué plan es coherente?', 'Preparar un recorrido breve para P1 y una carpeta con proceso y criterios para P3', 'Hacer solo un recorrido breve y no mostrar el proceso', 'Hacer solo una carpeta técnica para ambos', 'Cada público recibe un formato que responde a sus necesidades.'),
    sc=[
        ("En Artes: ¿qué es un público específico?", "Un grupo concreto de personas con características definidas", "Se adapta la presentación a esas características."),
        ("¿Qué se analiza del público?", "Quiénes son, qué saben, cuánto tiempo tienen y qué esperan", "Esas cuatro preguntas guían las decisiones."),
        ("¿Qué mejora la accesibilidad de un texto?", "Letra grande y buen contraste", "Facilita la lectura a más personas."),
    ],
    op=("Elige un público (por ejemplo, vecinos de un barrio) y un proyecto escolar. Responde las cuatro preguntas sobre el público y escribe dos decisiones de formato y de texto que adapten la presentación.",
        "Público: vecinos adultos mayores. Quiénes: personas del barrio; saben poco de arte digital; tiempo: 20 minutos; esperan entender el mural. Decisiones: textos en letra grande y una guía que lea las cédulas en voz alta.",
        ["responde las cuatro preguntas", "adapta el formato y el texto", "considera accesibilidad"],
        ["hoja con análisis y decisiones"],
        ["presentación igual para todos", "ignorar el tiempo"],
        "Pregunta: «¿qué cambió en tu presentación por este público?». Si nada, pídele una decisión concreta."),
    reinforce="Describe en tres líneas cómo explicarías un proyecto a tu abuela o a una persona mayor y cómo a un estudiante menor.",
    extend="Explica por qué la accesibilidad es parte del diseño y no un agregado.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (materiales de una muestra, de ejemplo, inventados). Obra «Patio vacío» del grupo de 3.º B (curso ficticio): collage de papel sobre cartulina de 50 por 70 centímetros. "
     "Evidencias del proceso: 6 bocetos, 3 pruebas de color y 2 retroalimentaciones de compañeros. "
     "Texto de sala borrador (32 palabras): «El patio vacío muestra cómo se siente el liceo cuando no hay nadie. Usamos papel recortado porque el borde irregular da sensación de silencio. Quisimos que quien mira se detenga y piense». "
     "El panel de proceso tiene espacio para 4 evidencias.")
build(
    O3, 2, F,
    use="Aprenderé a seleccionar qué mostrar del propósito, del proceso y del resultado, y a escribir una cédula y un texto de sala claros.",
    prior=["Sé analizar a un público.", "Sé registrar el proceso.", "Sé escribir un mensaje en una frase."],
    explain=[
        "Una presentación comunica tres cosas: el propósito (para qué se hizo), el proceso (cómo se decidió y qué se probó) y el resultado (la obra terminada). No se muestra todo: se seleccionan las evidencias que explican las decisiones más importantes. Seis bocetos casi iguales pueden resumirse en dos que muestren un cambio claro.",
        "La cédula es la ficha corta que acompaña a una obra y lleva título, autoría, técnica y dimensiones. El texto de sala explica la obra en pocas palabras, con lenguaje claro y sin repetir lo que ya se ve. Un buen texto de sala dice qué se quiso comunicar, qué decisión visual se tomó y por qué. Se evita la jerga y se escribe en oraciones cortas.",
        "Toda presentación reconoce a quienes participaron: autoría del grupo y atribución de referentes o fuentes. Si en la obra aparecen personas o trabajos de terceros, se muestra solo lo que tenga permiso. Los textos se revisan antes de imprimirse, para corregir errores y comprobar que cabrán en el espacio.",
    ],
    vocab=[("evidencia del proceso", "boceto, prueba o comentario que muestra una decisión"), ("cédula", "ficha con título, autoría, técnica y dimensiones"), ("texto de sala", "texto breve que explica la obra al público"), ("atribución", "indicación de quién hizo o inspiró algo"), ("jerga", "vocabulario técnico difícil de entender")],
    worked=[
        ("Armar una cédula", "Con la ficha, escribe una cédula para «Patio vacío».", ["Título: Patio vacío. Autoría: grupo de 3.º B.", "Técnica: collage de papel sobre cartulina. Dimensiones: 50 × 70 cm."], "Patio vacío, grupo de 3.º B, collage de papel sobre cartulina, 50 × 70 cm"),
        ("Seleccionar evidencias", "Hay 11 evidencias del proceso (6 + 3 + 2) y el panel permite 4. ¿Cuántas quedan fuera?", ["Se suman las evidencias: 6 + 3 + 2 = 11.", "11 − 4 = 7 quedan fuera."], "7 evidencias"),
    ],
    mistakes=[("Poner todas las evidencias del proceso en el panel.", "Se pierde la idea central y el público no sabe qué mirar.", "Elige las que muestran los cambios de decisión más importantes."),
              ("Usar términos técnicos sin explicarlos en el texto de sala.", "El público general no entiende y se desinteresa.", "Escribe oraciones cortas y explica cada término nuevo.")],
    T=[
        ('abc', '¿Qué es una cédula?', 'Una ficha con título, autoría, técnica y dimensiones', 'Un permiso para fotografiar a las personas', 'El precio de venta de la obra', 'La cédula identifica la obra con datos básicos.'),
        ('abc', '{F} ¿Cuál es la técnica de «Patio vacío»?', 'Collage de papel sobre cartulina', 'Fotografía digital', 'Escultura en greda', 'La ficha indica collage de papel sobre cartulina.'),
        ('abc', '{F} ¿Cuántas retroalimentaciones de compañeros tiene la ficha?', '2', '3', '6', 'La ficha indica 2 retroalimentaciones; los 6 son bocetos y los 3 son pruebas de color.'),
        ('=', '{F} El texto de sala tiene 32 palabras y se quiere dejar en 25. ¿Cuántas palabras se deben quitar?', '32-25', 'Se resta el largo deseado al largo actual.', ' palabras'),
        ('=', '{F} ¿Cuántos centímetros cuadrados tiene la obra?', '50*70', 'Se multiplica ancho por alto.', ' cm²'),
        ('abc', '{F} ¿Qué evidencia explica mejor una decisión de color?', 'Las pruebas de color', 'Los seis bocetos en lápiz', 'La cédula de la obra', 'Las pruebas de color muestran qué opciones se compararon.'),
        ('abc', '{F} El panel tiene lugar para 4 evidencias. ¿Qué selección es coherente?', 'Dos bocetos que muestran un cambio, una prueba de color y una retroalimentación', 'Cuatro bocetos casi iguales', 'Las cuatro primeras que se encuentren', 'Las evidencias seleccionadas deben mostrar decisiones, no repetir lo mismo.'),
        ('abc', '{F} ¿Qué cualidad tiene el texto de sala del borrador?', 'Dice qué se quiso comunicar, qué decisión se tomó y por qué', 'Usa muchas palabras técnicas', 'Describe solo el precio de los materiales', 'El borrador explica mensaje y decisión con lenguaje claro.'),
        ('abc', 'Alguien escribe en el texto «se usó una composición asimétrica con tensión cromática». ¿Qué conviene hacer?', 'Explicar con oraciones simples qué significa y por qué se eligió', 'Dejarlo como está porque suena más serio', 'Quitar toda explicación', 'Un texto de sala debe entenderse sin jerga.'),
        ('=', 'Una cédula tiene 6 campos y cada uno ocupa 2 líneas. ¿Cuántas líneas ocupa en total?', '6*2', 'Se multiplica la cantidad de campos por las líneas de cada uno.', ' líneas'),
        ('abc', 'Un grupo incluye una frase de un artista real en su texto de sala. ¿Qué debe hacer?', 'Ponerla entre comillas, atribuirla y no copiar textos largos', 'Copiarla sin comillas', 'Cambiar algunas palabras y no decir nada', 'La cita breve se atribuye y se distingue del texto propio.'),
        ('abc', '{F} La obra tiene un nombre de un compañero fuera del grupo en el boceto 4. ¿Qué corresponde?', 'Pedirle permiso o cubrir el nombre antes de mostrarlo', 'Mostrarlo igual', 'Quitar toda la evidencia del proceso', 'Se muestra solo lo que tenga permiso cuando aparecen personas.'),
        ('abc', 'Antes de imprimir el texto de sala, ¿qué se hace?', 'Revisar ortografía y comprobar que cabe en el espacio', 'Imprimirlo sin leerlo', 'Cambiarle la tipografía al azar', 'Revisar evita errores y problemas de espacio.'),
    ],
    ctx=('abc', 'Un grupo quiere mostrar su proceso y tiene 3 retroalimentaciones. Una cambió una decisión importante; las otras repiten lo mismo. ¿Qué elección es coherente?', 'Mostrar la que cambió una decisión y mencionar que hubo otras similares', 'Mostrar solo las que dicen que está bien', 'Ocultar todas las retroalimentaciones', 'Se muestran las evidencias que explican cambios y no las repetidas.'),
    sc=[
        ("En Artes: ¿qué es una cédula?", "Una ficha con título, autoría, técnica y dimensiones", "Identifica la obra con datos básicos."),
        ("¿Qué dice un buen texto de sala?", "Qué se quiso comunicar, qué decisión se tomó y por qué", "Ayuda al público a entender la obra."),
        ("¿Qué se hace con una cita en un texto?", "Se pone entre comillas y se atribuye", "Distingue lo ajeno de lo propio."),
    ],
    op=("Escribe la cédula de una obra imaginaria tuya (título, autoría, técnica, dimensiones) y un texto de sala de 30 a 40 palabras con mensaje, decisión y razón. Elige 3 evidencias del proceso que mostrarías y explica una.",
        "Cédula: «Mi calle», curso de 4.º medio (ficticio), dibujo en lápiz de color, 30 × 40 cm. Texto: «Mi calle muestra el camino que hago cada día. Usé líneas largas para sugerir distancia y colores cálidos para mostrar cercanía». Evidencias: boceto 1, prueba de color, retroalimentación sobre el color.",
        ["cédula completa", "texto claro con mensaje y decisión", "evidencias seleccionadas con razón"],
        ["hoja con cédula, texto y lista de evidencias"],
        ["jerga sin explicar", "mostrar todas las evidencias"],
        "Pregunta: «¿por qué elegiste estas evidencias?». Si no sabe, pídele que busque las que muestran cambios."),
    reinforce="Escribe una cédula para un objeto de tu casa como si fuera una obra: título, autoría, técnica y dimensiones aproximadas.",
    extend="Explica por qué mostrar el proceso ayuda al público a entender mejor el resultado.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (plano de montaje de ejemplo, inventado). Una sala de un liceo ficticio tiene 4 paneles de 100 centímetros de ancho. "
     "Cada obra mide 30 centímetros de ancho. Regla de montaje del grupo: dejar 10 centímetros de separación entre obras y entre las obras y los bordes del panel. "
     "Regla de altura: el centro de cada obra queda más o menos a la altura de los ojos de una persona de pie. "
     "Regla de circulación: un pasillo despejado, sin objetos en el suelo, por donde pasen también personas en silla de ruedas. "
     "Fijación: cinta adhesiva removible puesta por personas que no necesitan subirse a escaleras.")
build(
    O3, 3, F,
    use="Aprenderé a planificar el montaje de una muestra: distribuir obras, cuidar la altura, la circulación y la seguridad, y calcular el espacio.",
    prior=["Sé analizar a un público.", "Sé seleccionar evidencias.", "Sé sumar y multiplicar medidas en centímetros."],
    explain=[
        "El montaje es la forma de ubicar las obras en un espacio para que el público las vea y las recorra bien. Se decide qué obras se muestran, en qué orden y a qué distancia. Un plano de montaje es un dibujo o esquema donde se anota dónde va cada obra con medidas. El orden puede seguir el proceso (del boceto al resultado) o el tema.",
        "Las obras se ubican con una regla de altura y de separación para que se vean cómodamente. Una regla habitual es que el centro de la obra quede a la altura de los ojos de una persona de pie, y que haya una separación pareja entre obras. Para calcular cuántas caben en un panel, se suman los anchos de las obras más los espacios, incluidos los de los bordes.",
        "El montaje debe ser seguro y accesible: se usan fijaciones removibles (como cinta adhesiva) y no se suben a escaleras ni a sillas; si algo queda alto o pesado, lo instala una persona adulta autorizada. Los pasillos se mantienen despejados para que cualquier persona circule, incluso en silla de ruedas. No se dejan cables ni objetos en el suelo.",
    ],
    vocab=[("montaje", "ubicación ordenada de las obras en un espacio"), ("plano de montaje", "esquema con la ubicación y medidas de cada obra"), ("circulación", "camino por el que se mueve el público"), ("fijación", "forma de sujetar una obra"), ("separación", "espacio entre obras")],
    worked=[
        ("Calcular cuántas obras caben", "Con la ficha, ¿caben 2 obras en un panel?", ["Dos obras de 30 cm suman 60 cm; los espacios son 3 (borde, entre obras, borde) de 10 cm: 30 cm.", "60 + 30 = 90 cm, que es menor que 100 cm, así que caben."], "Sí, ocupan 90 cm de 100 cm"),
        ("Contar obras en total", "Si cada panel tiene 2 obras, ¿cuántas obras hay en los 4 paneles?", ["Se multiplica obras por paneles.", "2 × 4 = 8."], "8 obras")
    ],
    mistakes=[("Poner las obras tan juntas que no se distingue una de otra.", "La separación ayuda a mirar cada obra por separado.", "Deja una separación pareja entre obras y bordes."),
              ("Subirse a una silla para colgar una obra alta.", "Hay riesgo de caídas.", "Pide a una persona adulta autorizada o ubica la obra a la altura de los ojos.")],
    T=[
        ('abc', '¿Qué es un plano de montaje?', 'Un esquema con la ubicación y medidas de cada obra', 'Una lista con los precios de las obras', 'La nota de cada obra', 'El plano de montaje organiza la ubicación con medidas.'),
        ('abc', '{F} ¿Qué anchura tiene cada obra?', '30 centímetros', '100 centímetros', '10 centímetros', 'La ficha indica 30 centímetros por obra.'),
        ('abc', '{F} ¿Cuál es la regla de altura?', 'El centro de cada obra queda a la altura de los ojos de una persona de pie', 'Las obras se cuelgan lo más arriba posible', 'Las obras van en el suelo', 'La regla de altura de la ficha usa la altura de los ojos.'),
        ('=', '{F} Con 1 sola obra de 30 cm y 2 separaciones de 10 cm (una a cada borde), ¿cuántos centímetros ocupa del panel?', '30+2*10', 'Se suman el ancho de la obra y los dos espacios.', ' cm'),
        ('=', '{F} ¿Cuántos centímetros del panel quedan libres con esa sola obra y sus 2 separaciones?', '100-(30+2*10)', 'Se resta lo ocupado a los 100 cm del panel.', ' cm'),
        ('abc', '{F} ¿Cabrían 3 obras en un panel con las mismas reglas?', 'No, porque 3 obras y 4 separaciones ocupan 130 cm y el panel mide 100 cm', 'Sí, porque 3 obras suman 90 cm', 'Sí, si se quitan las separaciones de los bordes', 'Con 3 obras hay 90 cm de obras más 40 cm de espacios: 130 cm, más que 100 cm.'),
        ('abc', '{F} Una obra queda muy alta en el panel. ¿Qué hace el grupo?', 'Pide ayuda a una persona adulta o la baja a la altura de los ojos', 'Sube a una silla para fijarla', 'La deja ahí, aunque nadie la vea', 'La seguridad va primero y la altura de los ojos mejora la lectura.'),
        ('abc', '{F} ¿Por qué se deja un pasillo despejado?', 'Para que todas las personas circulen, incluidas quienes usan silla de ruedas', 'Para dar más lugar a los adornos', 'Para esconder las obras', 'La circulación segura y accesible es parte del montaje.'),
        ('abc', 'Un grupo cuelga una obra con un clavo y un martillo del liceo. ¿Qué problema tiene?', 'Usa una herramienta que puede dañar el muro o herir, y debe pedir autorización y ayuda', 'Ninguno, es la forma normal de colgar', 'Usan demasiada fuerza', 'Se prefieren fijaciones removibles y la ayuda de una persona adulta autorizada.'),
        ('=', 'Una obra de 40 cm y otra de 25 cm van en un panel con 3 separaciones de 10 cm. ¿Cuántos centímetros ocupan?', '40+25+3*10', 'Se suman los anchos de las dos obras y los espacios.', ' cm'),
        ('abc', 'Al ordenar las obras por proceso, ¿cuál secuencia es coherente?', 'Boceto, prueba de color y obra final', 'Obra final, boceto y prueba de color', 'Prueba de color, obra final y boceto', 'El proceso va del boceto al resultado.'),
        ('abc', '{F} Hay una extensión eléctrica cruzando el pasillo. ¿Qué se hace?', 'Se mueve o se cubre de forma segura, para que nadie tropiece', 'Se deja, porque se nota poco', 'Se tapa con una obra para que no se vea', 'Los objetos en el suelo son un riesgo de caídas.'),
        ('abc', '¿Qué es la separación entre obras?', 'El espacio libre entre una obra y otra', 'El título que se pone en la cédula', 'El soporte donde se hacen las obras', 'La separación es el espacio libre para mirar cada obra.'),
    ],
    ctx=('abc', 'Un grupo tiene 9 obras de 30 cm y los 4 paneles de la ficha. Según las reglas, ¿qué ocurre?', 'No caben todas: solo caben 8 obras, y deben dejar una fuera o usar otro espacio', 'Caben todas si las ponen sin separación', 'Caben todas con 3 por panel', 'Cada panel admite 2 obras; 4 paneles dan 8 y la novena queda fuera.'),
    sc=[
        ("En Artes: ¿qué es el montaje?", "La ubicación ordenada de las obras en un espacio", "Facilita que el público las vea y recorra."),
        ("¿A qué altura queda el centro de una obra?", "A la altura de los ojos de una persona de pie", "Es una regla habitual de montaje."),
        ("¿Quién cuelga una obra que queda alta?", "Una persona adulta autorizada", "Subirse a sillas es un riesgo de caídas."),
    ],
    op=("Dibuja o describe el plano de montaje de 4 obras de 20 cm de ancho en un panel de 120 cm, con separación de 10 cm entre obras y bordes. Calcula si caben y qué sobra o falta.",
        "4 obras de 20 cm suman 80 cm. Con 5 separaciones de 10 cm, son 50 cm. Total: 130 cm; el panel mide 120 cm, así que no caben. Propuesta: poner 3 obras en este panel (60 + 40 = 100 cm) y la cuarta en otro.",
        ["calcula obras y separaciones", "concluye si caben", "propone una solución segura"],
        ["hoja con el plano y el cálculo"],
        ["no contar los bordes", "proponer subirse a una silla"],
        "Pregunta: «¿cuántos espacios hay con 4 obras?». Si dice 3, recuérdale los bordes."),
    reinforce="Mide en casa un espacio de pared libre y calcula cuántas hojas de cuaderno (21 cm de ancho) caben con 5 cm de separación.",
    extend="Explica por qué un buen montaje puede cambiar cómo se entiende una obra aunque la obra sea la misma.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (opciones de presentación de ejemplo, inventadas). Proyecto: serie de afiches sobre reciclaje. "
     "Opción 1 (tradicional): panel impreso en cartulina y papel, sin electricidad ni internet. "
     "Opción 2 (digital): proyección de láminas en un muro con un proyector del liceo, necesita electricidad y a una persona que controle el avance. "
     "Opción 3 (emergente): galería en línea del liceo con un código QR impreso junto a cada obra que lleva a la página de la obra; necesita internet y el permiso del liceo para publicar. "
     "Opción 4 (emergente): recorrido con realidad aumentada, que superpone información sobre la obra en la pantalla de un teléfono; necesita internet y un teléfono con el software instalado; este cuaderno no incluye ese software y solo lo describe. "
     "Restricción: el espacio de la muestra no tiene internet estable.")
build(
    O3, 4, F,
    use="Aprenderé a elegir herramientas y tecnologías tradicionales y emergentes para presentar según el público, el espacio y los recursos, cuidando accesibilidad y privacidad.",
    prior=["Sé analizar a un público.", "Sé planificar un montaje.", "Sé que no todo se publica sin permiso."],
    explain=[
        "Para presentar se pueden usar herramientas tradicionales (paneles impresos, cuadernos, cédulas, maquetas) y tecnologías digitales o emergentes (proyección, galerías en línea, códigos QR, realidad aumentada). Una tecnología emergente es una que todavía se está incorporando a un campo. Ninguna es mejor en sí misma: se elige según el público, el espacio, los recursos y la seguridad.",
        "Para elegir se comparan criterios: ¿el público puede usarla?, ¿hay electricidad e internet?, ¿cuánto cuesta?, ¿es accesible (letra grande, buen contraste, texto alternativo para imágenes, subtítulos para videos)? Un código QR es una imagen que, al escanearla con un teléfono, lleva a una página. Si falla la tecnología, se necesita una alternativa sin conexión, como un panel impreso.",
        "Publicar en línea exige cuidado: se pide permiso al liceo y a las personas que aparecen, no se publican datos personales (como direcciones o teléfonos) y se atribuyen las fuentes. Si el curso no puede usar software real, se describe la tecnología en el plan y se deja una versión impresa. Este cuaderno no usa software ni dispositivos reales.",
    ],
    vocab=[("tecnología emergente", "tecnología que se está incorporando a un campo"), ("código QR", "imagen que lleva a una página al escanearla"), ("realidad aumentada", "información digital superpuesta sobre lo que se ve"), ("texto alternativo", "descripción escrita de una imagen"), ("alternativa sin conexión", "versión que funciona sin internet")],
    worked=[
        ("Elegir con una restricción", "Con la ficha, ¿qué opciones sirven si el espacio no tiene internet estable?", ["Se descartan las que necesitan internet: la 3 (galería en línea) y la 4 (realidad aumentada).", "La 1 (panel impreso) y la 2 (proyección) no requieren internet."], "Opciones 1 y 2"),
        ("Crear una alternativa", "La opción 3 falla porque no hay internet. ¿Qué alternativa sin conexión sirve?", ["Se imprime el contenido de la página de cada obra.", "Se deja junto a cada obra una hoja con la misma información."], "Una hoja impresa con la misma información"),
    ],
    mistakes=[("Elegir la tecnología más nueva sin comprobar si el público o el espacio la admiten.", "Si falla, no se puede presentar el proyecto.", "Elige según público, espacio y recursos y deja una alternativa sin conexión."),
              ("Publicar fotos de compañeros en línea sin su permiso.", "Se invade su privacidad.", "Pide consentimiento y consulta antes de publicar.")],
    T=[
        ('abc', '¿Qué es un código QR?', 'Una imagen que lleva a una página al escanearla con un teléfono', 'Una clave secreta para entrar a un computador', 'Un tipo de papel para imprimir', 'Un código QR enlaza una imagen impresa con contenido digital.'),
        ('abc', '{F} ¿Qué necesita la opción 1?', 'Ni electricidad ni internet', 'Electricidad e internet', 'Un proyector', 'La ficha dice que el panel impreso no necesita electricidad ni internet.'),
        ('abc', '{F} ¿Qué necesita la opción 3 además de internet?', 'El permiso del liceo para publicar', 'Un proyector', 'Un software de realidad aumentada instalado', 'La ficha indica el permiso del liceo para publicar.'),
        ('=', '{F} Hay 4 opciones y 2 no necesitan internet. ¿Cuántas sí lo necesitan?', '4-2', 'Se restan las opciones sin internet al total.', ' opciones'),
        ('abc', '{F} El espacio no tiene internet estable. ¿Cuál es una opción viable?', 'El panel impreso', 'La galería en línea', 'La realidad aumentada con conexión', 'El panel no depende de internet.'),
        ('abc', '{F} ¿Por qué conviene dejar una alternativa sin conexión en la opción 3?', 'Porque si falla internet el público aún puede ver la información', 'Porque ahorra papel', 'Porque el código QR funciona sin teléfono', 'La alternativa asegura que la presentación no dependa de una sola tecnología.'),
        ('abc', 'Un estudiante quiere publicar en línea una foto de un compañero haciendo su obra. ¿Qué debe hacer?', 'Pedirle consentimiento y consultar al docente antes de publicar', 'Publicarla porque la tomó él', 'Publicarla sin su nombre', 'La imagen de una persona requiere su permiso, aunque no se escriba el nombre.'),
        ('abc', '{F} En la galería en línea, una imagen de un afiche no tiene descripción. ¿Qué se agrega?', 'Un texto alternativo que describa lo que muestra', 'Más colores a la imagen', 'Nada, la imagen se explica sola', 'El texto alternativo permite a personas con discapacidad visual entender la imagen.'),
        ('abc', '{F} La opción 4 usa realidad aumentada, pero el curso no tiene el software. ¿Qué corresponde?', 'Describirla en el plan y presentar una versión impresa', 'Fingir que la usó', 'Descargar un programa de internet sin permiso', 'Si no se dispone de la tecnología, se describe y se ofrece una alternativa viable.'),
        ('=', 'Un video de 90 segundos necesita subtítulos con 3 líneas por cada 15 segundos. ¿Cuántas líneas necesita en total?', '90//15*3', 'Se divide el video en tramos de 15 segundos y se multiplica por 3.', ' líneas'),
        ('abc', 'Al elegir una tecnología para presentar, ¿qué criterio es más importante?', 'Que el público pueda usarla y que el espacio la permita', 'Que sea la más nueva', 'Que cueste lo más posible', 'Una tecnología sirve si el público y el espacio la admiten.'),
        ('abc', '¿Qué dato personal no debe aparecer en una página pública del proyecto?', 'La dirección y el teléfono de un compañero', 'El título de la obra', 'La técnica usada', 'Los datos de contacto privados no se publican.'),
        ('abc', 'Una compañera afirma que los paneles impresos ya no sirven. ¿Qué respondes?', 'Siguen siendo útiles porque funcionan sin electricidad ni internet, y se pueden combinar con tecnologías', 'Tiene razón, solo sirve lo digital', 'Nunca se deben combinar', 'Las herramientas tradicionales y las emergentes se complementan.'),
    ],
    ctx=('abc', 'Un grupo quiere usar un código QR junto a cada obra, pero el espacio no tiene internet estable. ¿Qué plan es coherente?', 'Dejar junto al código QR un resumen impreso de la obra y probar la conexión antes', 'Usar solo el código QR sin plan B', 'Eliminar los textos impresos', 'Con una alternativa impresa el público accede aunque falle la conexión.'),
    sc=[
        ("En Artes: ¿qué es un texto alternativo?", "Una descripción escrita de una imagen", "Permite que quienes no ven la imagen la entiendan."),
        ("¿Qué se pide antes de publicar la imagen de una persona?", "Su consentimiento", "Se respeta su privacidad y su decisión."),
        ("¿Qué se prepara si una tecnología puede fallar?", "Una alternativa sin conexión", "Asegura que la presentación se pueda hacer."),
    ],
    op=("Elige dos formas de presentar un proyecto escolar (una tradicional y una digital o emergente) y compáralas en cuatro criterios: público, espacio, costo y accesibilidad. Elige una y escribe una alternativa si falla.",
        "Opciones: panel impreso y proyección. Público: vecinos mayores. Espacio: sin internet. Costo: panel bajo, proyección medio. Accesibilidad: panel con letra grande; proyección con subtítulos. Elijo el panel. Alternativa: si hay luz, agregar proyección corta.",
        ["compara dos opciones con criterios", "elige con razón", "propone una alternativa"],
        ["hoja con la comparación"],
        ["elegir solo por lo novedoso", "olvidar el permiso para publicar"],
        "Pregunta: «¿qué pasa si falla la tecnología?». Si no responde, pídele una alternativa."),
    reinforce="Anota tres cosas de tu casa o colegio que usen un código QR y para qué sirven.",
    extend="Explica una ventaja y una desventaja de presentar solo en línea.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (gestión de una muestra, de ejemplo, inventada). Muestra del curso ficticio 4.º A: 4 roles (guía, montaje, registro y recepción), 6 estudiantes y presupuesto de $6.000. "
     "Gastos: cinta adhesiva removible $1.200, 10 pliegos de papel a $350 cada uno y marcadores $1.500. "
     "Cuestionario al público (con 3 preguntas de sí o no): hubo 20 respuestas y 15 personas marcaron «sí» a «¿se entiende el propósito de la muestra?». "
     "Registro de derechos: las fotografías de personas del público se toman solo con permiso; las citas de artistas llevan atribución; no se exhibe una obra ajena sin autorización.")
build(
    O3, 5, F,
    use="Aprenderé a gestionar una presentación (roles, presupuesto, tiempos y derechos) y a evaluar con el público si se logró el propósito.",
    prior=["Sé montar una muestra.", "Sé elegir herramientas de presentación.", "Sé calcular porcentajes simples."],
    explain=[
        "Gestionar una presentación significa organizarla de principio a fin: se definen roles, se reparte el trabajo, se calcula un presupuesto y se fija un calendario. Un rol es una tarea con responsable, como guiar al público, montar las obras, registrar lo que ocurre o recibir a las personas. Todas las personas del grupo deben tener una tarea clara.",
        "La presentación se evalúa con evidencia: observaciones, comentarios y un cuestionario breve al público. Con las respuestas se calcula qué proporción comprendió el propósito. Por ejemplo, 15 de 20 equivale a 75 de cada 100, es decir, 75 %. Los resultados se usan para decidir mejoras, no para culpar a personas.",
        "También se cuidan los derechos: las obras y los textos de otras personas se usan con permiso y atribución, las fotografías de personas se toman con consentimiento y los datos del público se guardan sin información personal. Si el público deja un comentario hiriente o hay un incidente, se avisa a una persona adulta del liceo.",
    ],
    vocab=[("rol", "tarea con una persona responsable"), ("presupuesto", "máximo de dinero disponible para un proyecto"), ("cuestionario", "conjunto breve de preguntas para el público"), ("proporción", "parte de un total"), ("consentimiento", "permiso de una persona para usar su imagen o sus datos")],
    worked=[
        ("Sumar gastos", "¿Cuánto suman los gastos de la ficha?", ["Cinta $1.200; papel 10 × 350 = $3.500; marcadores $1.500.", "1.200 + 3.500 + 1.500 = 6.200."], "$6.200"),
        ("Calcular una proporción", "15 de 20 personas marcaron «sí». ¿Qué porcentaje es?", ["15 de 20 es lo mismo que 75 de 100.", "El porcentaje es 75 %."], "75 %"),
    ],
    mistakes=[("Repartir tareas diciendo «todos hacen todo».", "Se pierde tiempo y nadie responde por nada.", "Asigna roles con una persona responsable de cada tarea."),
              ("Interpretar el cuestionario sin mirar cuántas personas respondieron.", "Un porcentaje de pocas respuestas puede confundir.", "Informa el número de respuestas junto con el porcentaje.")],
    T=[
        ('abc', '¿Qué es un rol en una presentación?', 'Una tarea con una persona responsable', 'Un adorno para la sala', 'El título de la obra', 'Un rol asigna una responsabilidad concreta.'),
        ('abc', '{F} ¿Cuántos roles tiene la muestra de la ficha?', '4', '6', '3', 'La ficha nombra guía, montaje, registro y recepción.'),
        ('abc', '{F} ¿Cuál fue el presupuesto del grupo?', '$6.000', '$6.200', '$3.500', 'La ficha indica un presupuesto de $6.000.'),
        ('=', '{F} ¿Cuánto cuestan juntos la cinta adhesiva y los marcadores?', '1200+1500', 'Se suman los dos gastos.', ' pesos'),
        ('=', '{F} ¿Cuánto dinero faltó respecto del presupuesto? (gastos menos presupuesto)', '(1200+10*350+1500)-6000', 'Se restan los $6.000 de presupuesto a los $6.200 de gastos.', ' pesos'),
        ('abc', '{F} ¿Qué decisión es razonable ante el exceso de gasto?', 'Reducir la cantidad de papel o buscar materiales reutilizables', 'Ignorar la diferencia', 'Pedir a otros estudiantes que paguen sin consultarles', 'Se ajusta el gasto o se buscan alternativas sin presionar a otros.'),
        ('=', '{F} ¿Cuántas personas respondieron «no» a la pregunta del cuestionario?', '20-15', 'Se restan las respuestas «sí» al total.', ' personas'),
        ('=', '{F} Si 18 de las 20 personas hubieran marcado «sí», ¿qué porcentaje habría sido?', '18*100//20', 'Se calcula cuántas de cada 100 personas habrían marcado «sí».', ' %'),
        ('abc', '{F} Un integrante quiere fotografiar a visitantes sin avisarles. ¿Qué corresponde?', 'Pedirles permiso antes de fotografiarlos', 'Fotografiarlos de lejos', 'Fotografiarlos solo si son menores', 'La ficha dice que las fotografías de personas se toman con permiso.'),
        ('abc', 'Un grupo cuelga un afiche famoso de una artista real para decorar la muestra. ¿Qué debe hacer?', 'Verificar si necesita autorización y atribuir, o usar una obra propia', 'Colgarlo sin más', 'Cambiarle el título y mostrarlo como propio', 'Una obra ajena se exhibe con autorización y atribución.'),
        ('=', 'Un cuestionario tuvo 40 respuestas y 30 dijeron «sí». ¿Qué porcentaje es?', '30*100//40', 'Se calcula cuántas de cada 100 respuestas fueron «sí».', ' %'),
        ('abc', 'Un comentario hiriente aparece en el cuestionario del público. ¿Qué haces?', 'Se lo muestras a una persona adulta del liceo y no lo difundes', 'Lo lees en voz alta para que todos lo vean', 'Buscas quién lo escribió para confrontarlo', 'Se avisa a una persona adulta y no se confronta ni se difunde.'),
        ('abc', 'Para decidir qué mejorar de una muestra, ¿qué es más útil?', 'Revisar los comentarios y las respuestas del cuestionario con el propósito en mente', 'Ignorar todos los comentarios', 'Preguntar solo a los amigos', 'La evidencia del público orienta mejoras respecto del propósito.'),
    ],
    ctx=('abc', 'En una muestra, 12 de 16 personas marcan «sí» a «¿se entendió el propósito?». Quienes comentaron dicen que no vieron el proceso. ¿Qué mejora es coherente?', 'Agregar un panel de proceso visible y revisar de nuevo con el mismo cuestionario', 'Eliminar la pregunta del cuestionario', 'Borrar los comentarios que no gustan', '12 de 16 es 75 %, y el comentario señala que falta mostrar el proceso.'),
    sc=[
        ("En Artes: ¿qué es un presupuesto?", "El máximo de dinero disponible para un proyecto", "Los gastos se comparan con ese máximo."),
        ("¿Qué porcentaje es 10 de 20?", "50 %", "10 de 20 equivale a 50 de cada 100."),
        ("¿Qué se pide antes de fotografiar a un visitante?", "Su permiso", "Es parte del respeto a su imagen."),
    ],
    op=("Planifica una muestra pequeña de tu curso: escribe 3 roles con responsable, tres gastos con su suma y una pregunta de sí o no para el público. Después inventa 10 respuestas de ejemplo y calcula el porcentaje.",
        "Roles: guía (Ana), montaje (Luis), registro (Sol). Gastos: cinta $900, papel $1.200 y marcadores $800: $2.900. Pregunta: «¿se entendió el propósito?». 10 respuestas de ejemplo: 8 sí, 2 no: 80 %.",
        ["roles con responsable", "gastos bien sumados", "porcentaje bien calculado"],
        ["hoja con el plan y el cálculo"],
        ["roles sin responsable", "no calcular el porcentaje"],
        "Pregunta: «¿qué haces con los resultados?». Si no hay mejora, pídele una acción."),
    reinforce="Escribe tres preguntas de sí o no que le harías al público de una muestra de tu curso.",
    extend="Explica cómo cambiarías la muestra si solo 5 de 20 personas dijeran «sí».",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 6 (obra inventada, descrita por escrito). «Escalera de papel», lámina ficticia de la artista Rosa Ibarra (personaje inventado). "
     "Sobre un fondo azul oscuro liso, una escalera blanca de líneas rectas sube en diagonal hasta el borde superior, sin llegar a él. "
     "En el peldaño más alto hay una figura pequeña amarilla, de espaldas. "
     "A la izquierda queda un gran espacio vacío. La superficie parece de papel recortado y pegado, con bordes algo irregulares.")
build(
    O4, 1, F,
    use="Aprenderé a analizar estéticamente una obra: describir con precisión lo que se ve y distinguir descripción, interpretación y juicio.",
    prior=["Reconozco color, forma, línea y composición.", "Sé que una obra comunica algo.", "Sé diferenciar lo que veo de lo que pienso."],
    explain=[
        "Analizar estéticamente una obra es estudiar cómo está hecha y qué efecto produce, usando los lenguajes artísticos. En una obra visual se observan la línea (recta, curva, gruesa), el color (cálido, frío, contraste), la forma, la textura, el espacio y la composición (cómo se ordenan los elementos). Se trabaja en tres pasos: describir, interpretar y juzgar.",
        "Describir es decir solo lo que se ve, sin opinar: «hay una escalera blanca de líneas rectas sobre un fondo azul oscuro». Interpretar es proponer qué podría significar, apoyándose en lo descrito: «la escalera que no llega al borde podría sugerir una meta lejana». Juzgar es valorar la obra con argumentos. Primero se describe, después se interpreta y al final se juzga.",
        "Una buena descripción usa palabras precisas y verificables y cada término técnico se explica. Una interpretación debe poder apoyarse en un detalle de la obra; si no, es una idea inventada. Las obras de esta clase son ficticias y se describen por escrito; con una obra real se necesita la obra delante y se respetan sus derechos de autor.",
    ],
    vocab=[("análisis estético", "estudio de cómo está hecha una obra y qué efecto produce"), ("descripción", "decir lo que se ve sin opinar"), ("interpretación", "propuesta de significado apoyada en detalles"), ("juicio", "valoración argumentada"), ("composición", "orden de los elementos en la obra"), ("contraste", "diferencia marcada entre dos elementos")],
    worked=[
        ("Separar descripción e interpretación", "«La escalera sin llegar al borde parece una meta lejana». ¿Es descripción o interpretación?", ["Habla de lo que sugiere («parece una meta»), no solo de lo que se ve.", "Se apoya en un detalle: la escalera no llega al borde."], "Interpretación apoyada en un detalle"),
        ("Describir con precisión", "Describe el color y la composición de la lámina.", ["Fondo azul oscuro liso, escalera blanca en diagonal, figura amarilla pequeña en lo más alto.", "A la izquierda hay un gran espacio vacío."], "Fondo azul oscuro, escalera blanca en diagonal, figura amarilla pequeña y espacio vacío a la izquierda"),
    ],
    mistakes=[("Escribir «la obra es triste» como descripción.", "Es una interpretación o una impresión, no algo visible.", "Describe lo que ves (azul oscuro, espacio vacío) y luego interpreta."),
              ("Interpretar sin apoyarse en ningún detalle de la obra.", "Se vuelve una opinión que otra persona no puede comprobar.", "Cita el detalle visual que sostiene tu interpretación.")],
    T=[
        ('abc', '¿Qué significa describir una obra?', 'Decir lo que se ve sin opinar', 'Decir si la obra gusta', 'Decir cuánto cuesta', 'La descripción se limita a lo visible.'),
        ('abc', '{F} ¿Cuál es el color de la figura pequeña?', 'Amarillo', 'Blanco', 'Azul oscuro', 'La figura del peldaño más alto es amarilla.'),
        ('abc', '{F} ¿Cuál es una descripción y no una interpretación?', 'Una escalera blanca de líneas rectas sube en diagonal sobre un fondo azul oscuro', 'La escalera simboliza el esfuerzo de toda una vida', 'La obra es muy triste', 'La primera afirma solo lo visible; las otras proponen significado o impresión.'),
        ('abc', '{F} ¿Qué elemento de la composición ocupa el lado izquierdo?', 'Un gran espacio vacío', 'Una segunda escalera', 'Una figura roja', 'La ficha indica un gran espacio vacío a la izquierda.'),
        ('abc', '{F} ¿Qué tipo de línea predomina en la escalera?', 'Recta', 'Curva y ondulada', 'Quebrada y punteada', 'La escalera es de líneas rectas.'),
        ('abc', '{F} ¿Qué detalle sostiene la interpretación «la figura parece estar sola»?', 'Que es la única figura y hay un gran espacio vacío a la izquierda', 'Que la escalera es de líneas rectas', 'Que la escalera es blanca', 'La interpretación se apoya en que no hay otras figuras y en el espacio vacío.'),
        ('abc', '{F} La figura está de espaldas. ¿Qué es una interpretación coherente?', 'Podría sugerir que mira hacia lo que viene y no al espectador', 'Significa con certeza que la figura está triste', 'Que la figura mira de frente a quien observa la obra', 'La interpretación se apoya en la posición de la figura y deja abierta la posibilidad.'),
        ('=', '{F} La lámina tiene 4 elementos principales: fondo, escalera, figura y espacio vacío. Si se describe cada uno con 2 frases, ¿cuántas frases hay?', '4*2', 'Se multiplica la cantidad de elementos por las frases por elemento.', ' frases'),
        ('abc', '{F} ¿Qué contraste de color aparece en la obra?', 'La figura amarilla contra el fondo azul oscuro', 'El fondo azul contra el borde del papel blanco', 'Las líneas rectas contra las curvas', 'Amarillo y azul oscuro destacan entre sí por la diferencia de claridad.'),
        ('abc', 'Alguien dice: «es una buena obra porque a mí me gusta». ¿Qué le falta?', 'Argumentos con detalles de la obra', 'Más cantidad de palabras', 'Mencionar que es famosa', 'Un juicio estético se apoya en razones, no solo en gusto.'),
        ('abc', '¿Qué orden es el recomendado al analizar?', 'Describir, interpretar y juzgar', 'Juzgar, describir e interpretar', 'Interpretar y luego juzgar sin describir', 'El análisis parte de lo observable y llega al juicio.'),
        ('=', 'Un análisis tiene 3 pasos (describir, interpretar y juzgar) y cada uno ocupa un párrafo de 4 oraciones. ¿Cuántas oraciones tiene?', '3*4', 'Se multiplica la cantidad de pasos por las oraciones de cada uno.', ' oraciones'),
        ('abc', 'Una obra real que no tienes delante se describe de memoria. ¿Qué riesgo hay?', 'Se pueden inventar detalles; conviene analizarla con la obra a la vista', 'Ninguno', 'Se pierde el derecho de autor', 'Sin la obra delante se pueden agregar detalles que no existen.'),
    ],
    ctx=('abc', 'Una estudiante escribe sobre la ficha: «La escalera es blanca y diagonal; el espacio vacío a la izquierda deja la mirada en la figura. Interpreto que busca mostrar soledad, porque la figura está sola y de espaldas». ¿Qué cumple bien?', 'Separa lo visible de la interpretación y la apoya en detalles', 'Juzga sin describir', 'Inventa detalles que no están en la ficha', 'Primero describe y luego interpreta con detalles de la obra.'),
    sc=[
        ("En Artes: ¿qué es una interpretación?", "Una propuesta de significado apoyada en detalles", "Debe poder comprobarse en la obra."),
        ("¿Qué orden sigue un análisis?", "Describir, interpretar y juzgar", "El análisis parte de lo observable y recién después interpreta."),
        ("¿Qué es el contraste?", "Una diferencia marcada entre dos elementos", "Ayuda a destacar partes de la obra."),
    ],
    op=("Elige una obra inventada tuya o una escena de tu entorno y escribe tres párrafos breves: descripción (3 frases), interpretación (2 frases con un detalle) y juicio (2 frases con una razón).",
        "Obra: un cuaderno abierto sobre una mesa vacía. Descripción: hay un cuaderno de tapa roja, abierto, con una página en blanco, sobre una mesa clara. Interpretación: la página en blanco podría sugerir un comienzo, porque no tiene marcas. Juicio: la obra comunica calma por su simplicidad.",
        ["separa descripción de interpretación", "apoya la interpretación en un detalle", "juzga con razón"],
        ["hoja con los tres párrafos"],
        ["mezclar opiniones en la descripción", "interpretar sin detalle"],
        "Pregunta: «¿qué detalle apoya esa interpretación?». Si no hay, pídele otra opción."),
    reinforce="Describe en cinco frases un objeto de tu pieza como si fuera una obra, sin dar tu opinión.",
    extend="Explica por qué dos personas pueden interpretar distinto una misma obra sin que una esté equivocada.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 7 (escena audiovisual de ejemplo, inventada, descrita por escrito). Cortometraje ficticio «La carta» de 12 segundos. "
     "Plano 1: plano general de una calle vacía al amanecer, 5 segundos, cámara quieta. "
     "Plano 2: primer plano de unas manos que sostienen una carta cerrada, 3 segundos. "
     "Plano 3: plano visto desde abajo hacia arriba (contrapicado) de una puerta muy alta, 4 segundos. "
     "Sonido: solo pasos lentos y viento; no hay música. Los planos se unen con cortes directos, sin transiciones. "
     "Ejemplo multimedial (inventado): una página donde, al tocar cada foto de una vieja calle, se abre un breve recuerdo escrito (interactividad).")
build(
    O4, 2, F,
    use="Aprenderé a analizar el tratamiento de los lenguajes audiovisual y multimedial: planos, ángulos, montaje, sonido e interactividad.",
    prior=["Sé separar descripción e interpretación.", "Reconozco elementos del lenguaje visual.", "Sé calcular duraciones simples."],
    explain=[
        "El lenguaje audiovisual combina imagen en movimiento y sonido. Un plano es lo que la cámara muestra entre dos cortes. Según cuánto se ve, el plano puede ser general (muestra todo el lugar), medio (de la cintura hacia arriba), primer plano (el rostro o un objeto cercano) o plano detalle (una parte muy pequeña). El ángulo es la posición de la cámara: normal, picado (desde arriba, hace ver pequeño) y contrapicado (desde abajo, hace ver grande o imponente).",
        "El montaje es el orden y la duración de los planos y la manera de unirlos, por ejemplo con cortes directos. Cambiar la duración cambia el ritmo: planos cortos aceleran y planos largos calman. El sonido (diálogo, música, ruidos, silencio) también construye sentido. Un guion es el texto que describe qué ocurre, y un storyboard son dibujos que muestran planos en secuencia.",
        "El lenguaje multimedial combina varios medios (texto, imagen, sonido, video) en un soporte digital, y suele ser interactivo: la persona elige qué abrir y en qué orden. Este cuaderno no tiene video ni software; las obras se describen por escrito y un storyboard puede dibujarse a mano en papel.",
    ],
    vocab=[("plano", "lo que muestra la cámara entre dos cortes"), ("ángulo", "posición de la cámara respecto de lo que filma"), ("montaje", "orden y duración de los planos y su unión"), ("ritmo", "velocidad con que se suceden los planos"), ("storyboard", "dibujos en secuencia que planifican los planos"), ("interactividad", "participación de quien usa la obra eligiendo qué hacer")],
    worked=[
        ("Reconocer un plano", "En la ficha, ¿qué plano muestra manos con una carta?", ["Es un plano muy cercano de un objeto y las manos.", "Se llama primer plano."], "Primer plano"),
        ("Duración total", "¿Cuántos segundos dura la escena?", ["Los planos duran 5, 3 y 4 segundos.", "5 + 3 + 4 = 12."], "12 segundos"),
    ],
    mistakes=[("Llamar «plano general» a un primer plano de un objeto.", "El plano general muestra todo el lugar y el primer plano lo muestra cercano.", "Fíjate cuánto del espacio se ve."),
              ("Decir que el ángulo contrapicado hace ver pequeño al personaje.", "El contrapicado, desde abajo, tiende a hacer ver grande o imponente.", "Recuerda: picado, desde arriba; contrapicado, desde abajo.")],
    T=[
        ('abc', '¿Qué es un plano?', 'Lo que la cámara muestra entre dos cortes', 'El guion completo', 'El sonido de fondo', 'Un plano es un tramo de imagen continuo entre dos cortes.'),
        ('abc', '{F} ¿Qué plano muestra la calle vacía?', 'Plano general', 'Primer plano', 'Plano detalle', 'La calle completa se ve de forma amplia: plano general.'),
        ('abc', '{F} ¿Qué ángulo tiene el plano de la puerta?', 'Contrapicado', 'Picado', 'Normal', 'La ficha indica que se ve desde abajo hacia arriba.'),
        ('abc', '{F} ¿Cuál es un efecto probable del plano de la puerta alta?', 'La puerta se ve grande e imponente', 'La puerta se ve pequeña', 'La puerta se ve igual que en un plano normal', 'El contrapicado agranda lo que se mira.'),
        ('=', '{F} ¿Cuántos segundos duran juntos los planos 2 y 3?', '3+4', 'Se suman las duraciones de esos dos planos.', ' segundos'),
        ('=', '{F} Si el plano 1 pasara a 8 segundos y los demás no cambian, ¿cuántos segundos duraría la escena?', '8+3+4', 'Se suman la nueva duración del plano 1 y los otros dos.', ' segundos'),
        ('abc', '{F} ¿Qué tipo de unión usa el montaje de la ficha?', 'Cortes directos', 'Transiciones de disolvencia', 'Mezcla de música y voz', 'La ficha señala cortes directos, sin transiciones.'),
        ('abc', '{F} ¿Qué efecto tiene que no haya música?', 'Resaltan los pasos y el viento y se siente silencio y expectativa', 'El sonido se vuelve más alegre', 'Hay más información en el diálogo', 'Sin música, los sonidos ambientales ganan protagonismo.'),
        ('abc', '{F} Si se acortara el plano 1 a 2 segundos, ¿qué ocurriría con el ritmo?', 'Se aceleraría', 'Se haría más lento', 'No cambiaría', 'Planos más cortos aceleran el ritmo.'),
        ('abc', '{F} En el ejemplo multimedial, ¿qué rasgo lo distingue de un video?', 'La persona elige qué foto tocar y en qué orden', 'Tiene sonido', 'Es en blanco y negro', 'La interactividad permite que cada persona elija su propio recorrido.'),
        ('abc', '¿Qué es un storyboard?', 'Dibujos en secuencia que planifican los planos', 'Un contrato de trabajo', 'Una cámara especial', 'El storyboard dibuja los planos antes de grabar.'),
        ('abc', 'Quieres mostrar a un personaje que se siente pequeño ante un problema. ¿Qué ángulo sirve?', 'Picado, desde arriba', 'Contrapicado, desde abajo', 'Ninguno, el ángulo no importa', 'Mirar desde arriba hace ver pequeño al personaje.'),
        ('=', 'Un storyboard tiene 6 cuadros y cada cuadro representa un plano de 4 segundos. ¿Cuánto dura la secuencia?', '6*4', 'Se multiplica la cantidad de planos por la duración de cada uno.', ' segundos'),
    ],
    ctx=('abc', 'Un grupo quiere mostrar «una persona que llega a un lugar nuevo y se siente pequeña». ¿Qué decisión de lenguaje audiovisual es coherente?', 'Un plano general amplio y luego un plano picado, con sonido ambiente suave', 'Solo primeros planos muy cortos y música muy fuerte', 'Un contrapicado largo que la haga ver imponente', 'El plano general y el picado enfatizan el entorno y la pequeñez.'),
    sc=[
        ("En Artes: ¿qué es el montaje?", "El orden y la duración de los planos y su unión", "Define el ritmo y el sentido de la secuencia."),
        ("¿Qué ángulo hace ver grande lo que se mira?", "Contrapicado", "La cámara mira desde abajo y por eso agranda lo filmado."),
        ("¿Qué es la interactividad en una obra multimedial?", "Que la persona elige qué hacer y en qué orden", "Distingue la obra multimedial del video."),
    ],
    op=("Dibuja a mano un storyboard de 3 cuadros para una escena inventada y escribe para cada uno el plano, el ángulo, la duración y el sonido. Suma la duración total.",
        "Escena: un estudiante llega al liceo. Cuadro 1: plano general, ángulo normal, 4 segundos, sonido de pasos. Cuadro 2: primer plano de la mochila, normal, 3 segundos, sonido de cierre. Cuadro 3: plano contrapicado de la puerta, 3 segundos, silencio. Total: 10 segundos.",
        ["usa plano, ángulo y duración", "suma bien la duración", "justifica un sonido"],
        ["hoja con tres cuadros y su descripción"],
        ["confundir picado con contrapicado", "no describir el sonido"],
        "Pregunta: «¿por qué elegiste ese plano para ese momento?». Si no responde, pídele el efecto."),
    reinforce="Describe en tres frases cómo cambiarías una escena que conozcas si usas solo planos cortos.",
    extend="Explica cómo cambia el sentido de una escena si se reemplaza el sonido de pasos por música alegre.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 8 (obra inventada, descrita por escrito). «Puerta entreabierta», fotografía ficticia de un artista inventado, Tomás Lagos. "
     "Una puerta de madera pintada de verde, entreabierta; por la rendija sale una luz cálida; al fondo se ve un camino de tierra. "
     "En el suelo, frente a la puerta, hay un par de zapatos sencillos. El resto de la imagen está en penumbra. "
     "Ejemplo de signo: una señal de tránsito con una flecha significa «siga por aquí» según una regla que todos conocen.")
build(
    O4, 3, F,
    use="Aprenderé a reconocer elementos simbólicos en una obra, diferenciar signo y símbolo y proponer interpretaciones sostenidas en detalles y en el contexto.",
    prior=["Sé describir una obra.", "Sé separar descripción e interpretación.", "Sé que una obra puede sugerir más de una idea."],
    explain=[
        "Un signo es algo que representa otra cosa por una regla compartida, como una señal de tránsito. Un símbolo también representa otra cosa, pero su significado es más abierto y depende de la cultura, de la época y del contexto de la obra. Una puerta puede sugerir un paso, una oportunidad o un límite; el significado no es fijo, y se propone según los detalles de cada obra.",
        "Para analizar un elemento simbólico se siguen cuatro pasos: ver qué elemento destaca (una puerta entreabierta), qué detalles lo rodean (luz cálida, camino de tierra, zapatos), qué ideas puede sugerir y qué contexto lo respalda. Una interpretación gana fuerza si varios detalles la apoyan y si encaja con el contexto, y la pierde si se apoya solo en uno.",
        "Se evita la sobreinterpretación, es decir, asignar significados que la obra no sostiene, y las afirmaciones del tipo «siempre significa». Se aceptan varias interpretaciones si cada una tiene respaldo. Se cuida también no atribuir significados a símbolos de pueblos o culturas que no conocemos: se consulta a quien los conoce, como un educador tradicional o una persona experta.",
    ],
    vocab=[("signo", "algo que representa otra cosa por una regla compartida"), ("símbolo", "elemento cuyo significado es abierto y depende del contexto"), ("sobreinterpretación", "asignar significados que la obra no sostiene"), ("detalle de apoyo", "rasgo visible que respalda una interpretación"), ("contexto", "circunstancias de época, lugar y función de una obra")],
    worked=[
        ("Signo o símbolo", "La flecha de tránsito de la ficha, ¿es signo o símbolo?", ["Su significado es fijo y está en una regla que todos conocen.", "Es un signo."], "Signo"),
        ("Respaldar una interpretación", "«La puerta entreabierta sugiere una oportunidad». ¿Qué detalles de la ficha la apoyan?", ["La luz cálida que sale por la rendija sugiere algo positivo.", "El camino de tierra al fondo sugiere un recorrido por delante."], "La luz cálida y el camino al fondo"),
    ],
    mistakes=[("Afirmar «la puerta siempre significa libertad».", "El significado cambia según la obra y el contexto.", "Escribe «podría sugerir…» y cita los detalles de apoyo."),
              ("Interpretar un símbolo cultural que no se conoce.", "Se corre el riesgo de falsear su sentido.", "Reconoce el límite y consulta a una persona que conozca esa cultura.")],
    T=[
        ('abc', '¿Qué es un signo?', 'Algo que representa otra cosa por una regla compartida', 'Un símbolo de significado totalmente abierto', 'Una obra sin significado', 'Un signo tiene un significado fijado por convención.'),
        ('abc', '{F} ¿Qué elemento destaca en la fotografía?', 'Una puerta verde entreabierta', 'Un auto detenido', 'Una ventana cerrada', 'La ficha describe una puerta verde entreabierta.'),
        ('abc', '{F} ¿Qué sale por la rendija?', 'Una luz cálida', 'Una luz fría y azulada', 'Una sombra muy oscura', 'La ficha indica que por la rendija sale una luz cálida.'),
        ('abc', '{F} ¿Qué detalle sugiere un recorrido por delante?', 'El camino de tierra al fondo', 'El color verde de la puerta', 'La penumbra', 'El camino de tierra sugiere un trayecto que queda por recorrer.'),
        ('abc', '{F} ¿Qué detalle sugiere que alguien podría entrar?', 'Los zapatos frente a la puerta', 'El color verde', 'La penumbra del resto de la imagen', 'Los zapatos sencillos, quietos frente a la puerta, sugieren a alguien a punto de pasar.'),
        ('abc', '{F} ¿Cuál es una interpretación bien apoyada?', 'La puerta podría sugerir una oportunidad, porque la luz cálida y el camino invitan a pasar', 'La puerta significa muerte porque sí', 'No tiene significado alguno', 'La primera se apoya en detalles; las otras no.'),
        ('abc', '{F} Alguien afirma «la puerta siempre simboliza libertad en cualquier obra». ¿Qué problema tiene?', 'Generaliza: el significado depende de la obra y el contexto', 'Ninguno, es una regla', 'No ve la puerta', 'Los símbolos no tienen significados fijos universales.'),
        ('=', '{F} Una estudiante anota 5 detalles visibles y 2 interpretaciones, cada una con 2 detalles de apoyo. ¿Cuántos detalles de apoyo usa en total?', '2*2', 'Se multiplica el número de interpretaciones por los detalles de cada una.', ' detalles'),
        ('abc', '{F} Dos compañeros interpretan la puerta de forma distinta pero ambos citan detalles. ¿Qué es lo adecuado?', 'Aceptar ambas si cada una tiene respaldo en la obra', 'Descartar una porque no puede haber dos', 'Decidir cuál es verdadera por votación', 'Se aceptan varias interpretaciones con respaldo.'),
        ('abc', 'Aparece un símbolo de un pueblo originario que no conoces. ¿Qué haces?', 'No interpretarlo por tu cuenta y consultar a una persona que conozca esa cultura, como un educador tradicional', 'Inventar un significado para completar el análisis', 'Quitarlo del análisis sin avisar', 'Así se evita falsear el significado de símbolos de otras culturas.'),
        ('abc', '¿Qué es la sobreinterpretación?', 'Asignar significados que la obra no sostiene', 'Describir con demasiado detalle', 'Citar a un artista', 'La sobreinterpretación no tiene detalles que la respalden.'),
        ('=', 'Un análisis incluye 3 elementos simbólicos y 3 detalles de apoyo por cada uno. ¿Cuántos detalles hay?', '3*3', 'Se multiplican elementos por detalles.', ' detalles'),
        ('abc', '{F} El contexto de la obra es que se hizo para una exposición sobre mudanzas. ¿Cómo cambia la interpretación?', 'La puerta podría sugerir un cambio de lugar, y esa idea se apoya en el contexto', 'No cambia nada', 'La obra deja de tener significado', 'El contexto orienta la interpretación hacia ideas coherentes con su origen.'),
    ],
    ctx=('abc', 'Para la ficha, un grupo escribe: «Puerta entreabierta, luz cálida, camino, zapatos. Interpretación posible: invitación a un nuevo comienzo. Otra: el miedo a salir. Apoyo: la luz invita, pero la penumbra puede sugerir miedo». ¿Qué cumple bien?', 'Propone dos interpretaciones y las apoya en detalles', 'Afirma una sola verdad sin respaldo', 'No usa detalles de la obra', 'Cada interpretación se sostiene con detalles distintos.'),
    sc=[
        ("En Artes: ¿qué es un símbolo?", "Un elemento de significado abierto que depende del contexto", "Se interpreta con detalles de la obra."),
        ("¿Qué es un signo?", "Algo que representa otra cosa por una regla compartida", "Un signo tiene un significado convencional que todos conocen."),
        ("¿Qué haces con un símbolo cultural que no conoces?", "Consultar a una persona que conozca esa cultura", "Así se evita falsear su sentido con ideas inventadas."),
    ],
    op=("Elige un objeto de una obra inventada tuya (una ventana, un árbol, un reloj) y escribe una descripción de 3 frases con detalles y dos interpretaciones posibles, cada una con un detalle de apoyo.",
        "Obra: una ventana abierta con una cortina movida por el viento y un cielo gris. Descripción: la cortina se mueve hacia adentro, hay un cielo gris y la ventana está abierta. Interpretación 1: sugiere entrada de algo nuevo (cortina hacia adentro). Interpretación 2: sugiere inquietud (cielo gris).",
        ["describe con detalles", "dos interpretaciones", "cada una con detalle de apoyo"],
        ["hoja con descripción e interpretaciones"],
        ["decir «siempre significa»", "interpretar sin detalle"],
        "Pregunta: «¿qué detalle apoya esa idea?». Si no hay, pídele reformularla."),
    reinforce="Elige un logotipo conocido de tu entorno y anota si es un signo o un símbolo y por qué.",
    extend="Explica cómo el contexto puede cambiar el significado de un mismo elemento, con un ejemplo inventado.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 9 (dos obras inventadas, descritas por escrito). "
     "Obra P: cartel ficticio de una feria de una ciudad costera, hecho para pegarse en las calles; impresión con una sola tinta roja sobre papel claro; letras grandes de trazo grueso y el dibujo de un pez; su función era anunciar la fiesta y atraer público familiar. "
     "Obra Q: videoinstalación ficticia de una artista de otro país, hecha para una sala de museo; proyecta en un muro, durante 6 minutos repetidos, imágenes en blanco y negro de un patio y el sonido de voces lejanas; su función es invitar a recordar. "
     "No se dan fechas: «de épocas distintas» significa que se hicieron con medios y para usos distintos.")
build(
    O4, 4, F,
    use="Aprenderé a analizar obras de diferentes épocas y procedencias considerando su contexto: lugar, función, público y medios disponibles.",
    prior=["Sé analizar el lenguaje de una obra.", "Sé reconocer elementos simbólicos.", "Sé distinguir descripción de juicio."],
    explain=[
        "El contexto de una obra son las circunstancias en que se hizo y se muestra: el lugar de procedencia, la época, quiénes la hicieron y para quién, los medios técnicos disponibles y su función (anunciar, recordar, protestar, decorar). El mismo recurso, como usar solo una tinta, puede tener razones muy distintas: en un cartel de calle puede ser una decisión económica y práctica; en una obra de museo, una decisión expresiva.",
        "Analizar obras de épocas y procedencias distintas pide evitar dos errores: el anacronismo, que es juzgar una obra antigua con las condiciones de hoy (por ejemplo, criticar que no use color si en su época no se podía imprimir con color), y la mirada que considera mejor lo propio. Se pregunta primero: ¿para qué y para quién se hizo? ¿con qué medios? ¿qué decisiones tomó su autor?",
        "Se comparan obras por sus decisiones y su contexto, no por cuál es «más avanzada». Los datos de época y procedencia se usan solo si se conocen con seguridad; si no, se declara que no se conocen. Las obras de la ficha son inventadas y no se dan fechas exactas.",
    ],
    vocab=[("contexto", "circunstancias en que se hace y se muestra una obra"), ("procedencia", "lugar o cultura de origen de una obra"), ("función", "para qué se hizo una obra"), ("anacronismo", "juzgar una obra con condiciones de otra época"), ("medios técnicos", "herramientas y procedimientos disponibles")],
    worked=[
        ("Identificar la función", "En la ficha, ¿cuál era la función de la obra P?", ["La ficha dice que se hizo para pegarse en calles.", "Su función era anunciar la fiesta y atraer público familiar."], "Anunciar la fiesta y atraer público familiar"),
        ("Evitar el anacronismo", "Alguien dice «la obra P es mala porque usa solo una tinta». ¿Qué error comete?", ["No considera que la obra se hizo para pegarse en calles con medios sencillos.", "Juzga con una condición que no era parte de su contexto."], "Comete anacronismo: exige a un cartel de calle algo que no era parte de su contexto")
    ],
    mistakes=[("Decir que la obra Q es mejor porque usa tecnología.", "La tecnología no define la calidad; cada obra responde a su contexto.", "Compara decisiones y funciones, no si usa tecnología."),
              ("Inventar una fecha o un lugar «para completar» el análisis.", "Un dato inventado puede inducir a error.", "Anota «no se conoce» cuando no tengas el dato.")],
    T=[
        ('abc', '¿Qué es el contexto de una obra?', 'Las circunstancias en que se hizo y se muestra', 'El color del marco', 'El nombre de quien la compra', 'El contexto incluye lugar, época, función y público.'),
        ('abc', '{F} ¿Cuántas tintas usa la obra P?', 'Una, roja', 'Tres', 'Ninguna', 'La ficha indica una sola tinta roja.'),
        ('abc', '{F} ¿En qué espacio se muestra la obra Q?', 'En una sala de museo', 'En las calles de una ciudad', 'En un estadio', 'La ficha indica una sala de museo.'),
        ('abc', '{F} ¿Cuál es la función de la obra Q?', 'Invitar a recordar', 'Anunciar una fiesta', 'Vender productos', 'La ficha dice que invita a recordar.'),
        ('=', '{F} La videoinstalación Q dura 6 minutos y se repite 5 veces seguidas. ¿Cuántos minutos dura en total?', '6*5', 'Se multiplica la duración de una repetición por el número de repeticiones.', ' minutos'),
        ('abc', '{F} ¿Qué decisión de la obra P responde a su contexto de calle?', 'Letras grandes de trazo grueso para leerse a distancia', 'Un sonido de voces lejanas', 'Una proyección en un muro', 'En la calle se necesita legibilidad rápida.'),
        ('abc', '{F} ¿Qué decisión de Q responde a su contexto de museo?', 'La proyección repetida en una sala donde se puede detenerse a mirar', 'Letras grandes para leerse a distancia', 'Un dibujo de un pez', 'En museo se puede observar con calma.'),
        ('abc', '{F} Alguien critica la obra P porque «no tiene sonido». ¿Qué error comete?', 'Le exige un rasgo que no corresponde a su medio impreso y a su función', 'Ninguno', 'Que no sabe leer', 'Un cartel impreso no tiene sonido por su medio.'),
        ('abc', '¿Qué es el anacronismo?', 'Juzgar una obra con condiciones de otra época', 'Una técnica de impresión', 'Una forma de colorear', 'Es aplicar criterios de hoy a una obra de otro tiempo.'),
        ('abc', 'No sabes en qué año se hizo una obra de la ficha. ¿Qué haces?', 'Anotar que no se conoce y no inventarlo', 'Escribir un año al azar', 'Eliminar la obra del análisis', 'Un dato inventado puede inducir a error.'),
        ('=', 'Un análisis compara 2 obras en 4 aspectos: función, medio, público y decisión visual. ¿Cuántas observaciones hay si se anota una por obra y aspecto?', '2*4', 'Se multiplican obras por aspectos.', ' observaciones'),
        ('abc', 'Al comparar obras de procedencias distintas, ¿qué conviene hacer?', 'Preguntar por la función y los medios de cada una y comparar decisiones', 'Decidir cuál es más moderna', 'Asumir que la propia cultura es mejor', 'Se comparan decisiones en su contexto.'),
        ('abc', '{F} ¿Qué tienen en común las obras P y Q?', 'Ambas usan decisiones visuales según su función y su contexto', 'Ambas usan color y sonido', 'Ambas se hicieron para el mismo público', 'Las dos responden a su función y contexto con decisiones propias.'),
    ],
    ctx=('abc', 'Un estudiante dice que la obra P es «de menor valor» por ser un cartel y no estar en un museo. ¿Qué responde un análisis estético atento al contexto?', 'Que cumple bien su función en la calle y que el valor se analiza con criterios coherentes con su contexto', 'Que tiene razón, el museo da más valor', 'Que no se puede analizar', 'Se evalúa por su función y su contexto, no por el lugar donde se muestra.'),
    sc=[
        ("En Artes: ¿qué es la procedencia?", "El lugar o cultura de origen de una obra", "Conocer la procedencia ayuda a comprender su contexto de origen."),
        ("¿Qué se pregunta primero al analizar una obra de otra época?", "Para qué y para quién se hizo y con qué medios", "Así se evita juzgar con condiciones de hoy."),
        ("¿Qué haces si no conoces un dato?", "Anotar que no se conoce", "No se inventan datos que no se conocen con seguridad."),
    ],
    op=("Inventa dos obras de procedencias o funciones distintas (por ejemplo, un cartel y una fotografía de museo) y escribe una comparación en 4 frases que use función, medio, público y decisión visual. No uses fechas inventadas.",
        "Obra 1: cartel de feria; función: anunciar; medio: papel impreso; público: familias; decisión: letras grandes. Obra 2: fotografía de museo; función: invitar a mirar con calma; medio: copia impresa; público: visitantes; decisión: encuadre cerrado. Ambas adaptan sus decisiones a su función.",
        ["usa función, medio, público y decisión", "no inventa fechas", "no juzga con criterios ajenos"],
        ["hoja con la comparación"],
        ["decir que una es mejor por ser moderna", "inventar datos"],
        "Pregunta: «¿para qué se hizo cada una?». Si no distingue las funciones, pídele que lo escriba."),
    reinforce="Elige un afiche de tu entorno y anota su función, su público y una decisión visual que responda a ellos.",
    extend="Explica por qué juzgar una obra de otra época con criterios actuales puede llevar a conclusiones erradas.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 10 (obra inventada, descrita por escrito). «Hoy» es un cartel ficticio de un festival de títeres de una ciudad inventada. "
     "Sobre un fondo rojo, un títere gigante hecho de líneas gruesas negras ocupa el centro; la palabra «Hoy» aparece abajo con letras blancas. "
     "Está impreso a dos tintas (rojo y negro) sobre papel claro, para pegarse en paneles de calle. "
     "Su público era familias con niñas y niños. La función era anunciar el festival. "
     "Esquema de análisis de 5 partes: 1) descripción; 2) tratamiento de los lenguajes; 3) elementos simbólicos; 4) contexto; 5) conclusión.")
build(
    O4, 5, F,
    use="Aprenderé a escribir un análisis estético completo de una obra, integrando descripción, tratamiento de los lenguajes, símbolos y contexto, con una conclusión respaldada.",
    prior=["Sé describir una obra.", "Sé reconocer símbolos y contextos.", "Sé comparar decisiones visuales."],
    explain=[
        "Un análisis estético completo integra cuatro miradas y una conclusión. 1) Descripción: lo que se ve, con precisión. 2) Tratamiento de los lenguajes: cómo usan línea, color, composición, plano, ángulo o montaje, y qué efecto producen. 3) Elementos simbólicos: qué ideas sugieren los elementos que destacan y con qué detalles se apoya. 4) Contexto: lugar, función, público y medios. 5) Conclusión: una afirmación que une las partes.",
        "La conclusión responde a «¿qué comunica la obra y cómo lo logra?» y se apoya en al menos dos evidencias de la obra. Por ejemplo: «El cartel anuncia un festival infantil con claridad porque el títere gigante y las letras blancas se leen desde lejos y el rojo atrae la mirada». Evita frases vagas como «es una obra muy buena».",
        "Antes de entregar un análisis se revisa: ¿separé lo visible de lo interpretado?, ¿usé al menos una evidencia por afirmación?, ¿consideré el contexto?, ¿evité inventar datos?, ¿cuidé el lenguaje respetuoso con otras culturas? El análisis se escribe en párrafos breves y claros.",
    ],
    vocab=[("tratamiento del lenguaje", "manera de usar los recursos visuales o audiovisuales"), ("evidencia", "detalle de la obra que respalda una afirmación"), ("conclusión", "afirmación final que une las partes del análisis"), ("legibilidad", "facilidad para leer o reconocer algo"), ("respaldo", "evidencia que sostiene una idea")],
    worked=[
        ("Ubicar una frase en el esquema", "«Está impreso a dos tintas, rojo y negro». ¿A qué parte del esquema pertenece?", ["Habla de los medios técnicos con que se hizo el cartel.", "Los medios técnicos disponibles forman parte del contexto."], "Contexto (medios técnicos)"),
        ("Revisar una conclusión", "«El cartel es lindo». ¿Por qué es débil?", ["No responde qué comunica ni cómo lo logra.", "No cita ninguna evidencia de la obra."], "No explica qué comunica ni usa evidencia"),
    ],
    mistakes=[("Escribir una conclusión que no se relaciona con lo analizado.", "Parece una opinión desconectada del análisis.", "Usa las partes del análisis para sostener la conclusión."),
              ("Mezclar descripción e interpretación en la misma frase.", "No se distingue lo visible de lo propuesto.", "Escribe primero lo que ves y luego lo que podría significar.")],
    T=[
        ('abc', '¿Qué es una conclusión de un análisis estético?', 'Una afirmación que une las partes y se apoya en evidencias', 'Una frase de adorno al final', 'Una copia de la descripción', 'La conclusión integra lo analizado con respaldo.'),
        ('abc', '{F} ¿Qué color tiene el fondo del cartel?', 'Rojo', 'Negro', 'Blanco', 'La ficha indica un fondo rojo.'),
        ('abc', '{F} ¿A qué parte del esquema pertenece «el público eran familias con niñas y niños»?', 'Contexto', 'Descripción', 'Conclusión', 'El público forma parte del contexto.'),
        ('abc', '{F} ¿Qué parte del esquema ocupa «las líneas gruesas negras del títere se leen desde lejos»?', 'Tratamiento de los lenguajes', 'Contexto', 'Conclusión', 'Habla del uso de la línea y de su efecto.'),
        ('=', '{F} El esquema tiene 5 partes y se escriben 3 frases por parte. ¿Cuántas frases tiene el análisis?', '5*3', 'Se multiplican las partes por las frases por parte.', ' frases'),
        ('abc', '{F} ¿Cuál es una conclusión bien respaldada?', 'El cartel anuncia el festival con claridad porque el títere gigante y las letras blancas se leen desde lejos', 'El cartel es muy lindo', 'El cartel es mejor que cualquier otro', 'La primera usa evidencias de la obra.'),
        ('abc', '{F} «La palabra Hoy en letras blancas sugiere inmediatez» es', 'una interpretación apoyada en un detalle', 'una descripción pura', 'un dato del contexto', 'Sugiere un significado a partir del texto y el color.'),
        ('abc', '{F} ¿Qué decisión se explica por el contexto de calle?', 'Letras blancas sobre fondo rojo para leerse rápido', 'Un sonido de fondo', 'Una proyección en un muro', 'En calles se necesita lectura rápida.'),
        ('abc', '{F} Alguien escribe «el cartel fue hecho en 1950». ¿Qué corresponde?', 'Eliminar la fecha, porque la ficha no la entrega y no se debe inventar', 'Dejarla porque suena verosímil', 'Cambiarla por 1960', 'Los datos no entregados no se inventan.'),
        ('=', 'Un análisis tiene 2 evidencias por afirmación y 4 afirmaciones. ¿Cuántas evidencias contiene?', '2*4', 'Se multiplican las evidencias por afirmación por las afirmaciones.', ' evidencias'),
        ('abc', '¿Qué se revisa antes de entregar un análisis?', 'Que cada afirmación tenga evidencia y que se haya distinguido lo visible de lo interpretado', 'Que tenga muchos adjetivos', 'Que sea muy largo', 'La revisión verifica evidencia y distinción.'),
        ('abc', 'Un compañero copia el análisis de otra persona. ¿Qué corresponde?', 'Escribir el propio con tus evidencias y citar si usas ideas ajenas', 'Cambiar solo algunas palabras', 'Entregarlo igual', 'Se atribuyen las ideas ajenas y se escribe con evidencia propia.'),
        ('abc', '{F} Quieres comparar «Hoy» con una obra de otra procedencia. ¿Qué haces primero?', 'Revisar función, medios y público de cada una', 'Decidir cuál es mejor', 'Ignorar el contexto', 'Se compara a partir del contexto.'),
    ],
    ctx=('abc', 'Para «Hoy», una estudiante escribe: «Descripción: fondo rojo, títere negro, letras blancas. Lenguaje: líneas gruesas y alto contraste. Símbolo: el títere gigante sugiere fiesta. Contexto: cartel de calle para familias. Conclusión: comunica con claridad que hay un festival infantil». ¿Qué cumple bien?', 'Recorre las cinco partes con evidencias y una conclusión relacionada', 'Solo opina que es bonito', 'No usa el contexto', 'Cada parte aporta evidencia a la conclusión.'),
    sc=[
        ("En Artes: ¿qué es una evidencia en un análisis?", "Un detalle de la obra que respalda una afirmación", "Evita opiniones sin apoyo en lo que muestra la obra."),
        ("¿Qué responde la conclusión?", "Qué comunica la obra y cómo lo logra", "Une las partes del análisis en una afirmación final."),
        ("¿Qué se hace con los datos que no se conocen?", "Se declara que no se conocen", "No se inventan datos que no se conocen con seguridad."),
    ],
    op=("Elige una obra inventada tuya y escribe un análisis de cinco partes en 8 a 10 frases: descripción, tratamiento del lenguaje, símbolos, contexto y conclusión con dos evidencias.",
        "Obra: afiche de una función de teatro escolar. Descripción: fondo morado, máscara blanca al centro. Lenguaje: contraste alto, composición centrada. Símbolo: la máscara sugiere teatro. Contexto: pegado en el liceo para estudiantes. Conclusión: comunica con claridad el evento porque la máscara y el contraste atraen la mirada.",
        ["cinco partes", "evidencias para cada afirmación", "conclusión respaldada"],
        ["hoja con el análisis"],
        ["conclusión sin evidencia", "inventar datos"],
        "Pregunta: «¿qué evidencia respalda tu conclusión?». Si no responde, pídele que vuelva a la obra."),
    reinforce="Escribe una conclusión de dos frases sobre un afiche de tu entorno, citando dos evidencias.",
    extend="Explica por qué una buena conclusión depende de las partes anteriores del análisis.",
)
