"""Diseño y arquitectura 3.º y 4.º medio HC: OAC-03 (presentaciones a públicos específicos) y OAC-04 (análisis estético de piezas y obras). Casos, paneles y obras inventados; sin imágenes ni software reales."""
from __future__ import annotations

from hc_darq_common import build

O3 = "AR-DARQ-3y4-OAC-03"
O4 = "AR-DARQ-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 10 (situaciones de presentación de ejemplo, inventadas). El mismo proyecto, «Pérgola de lectura», se presentará en tres ocasiones. "
     "Situación 1: reunión de 15 minutos con vecinas y vecinos del barrio, algunos mayores de 70 años y sin conocimientos técnicos; objetivo: obtener su apoyo. "
     "Situación 2: comisión de tres docentes que revisan el proceso durante 10 minutos; objetivo: demostrar que las decisiones tuvieron criterios. "
     "Situación 3: feria con visitantes que pasan 2 minutos frente a un panel; objetivo: que entiendan la idea central y recuerden el proyecto.")
build(
    O3, 1, F,
    use="Aprenderé a leer el propósito y el público de una presentación de proyectos y a decidir qué comunicar, con qué lenguaje, en cuánto tiempo y con qué ajustes de accesibilidad.",
    prior=["Sé qué es un proyecto de diseño y arquitectura y cómo se revisa.", "Sé sumar y restar minutos.", "Sé que no todas las personas leen o escuchan igual."],
    explain=[
        "Presentar un proyecto de diseño o arquitectura es comunicar tres cosas a un público: el propósito (para qué se hizo y a qué necesidad responde), aspectos del proceso (qué se investigó, probó y decidió) y los resultados (qué se logró y qué limitaciones tiene). Una buena presentación no repite todo lo que se hizo: elige lo que ese público necesita para entender o decidir.",
        "El público define casi todo: el lenguaje (simple o técnico), el nivel de detalle, el tiempo, el medio y las ayudas de accesibilidad. La pregunta guía es: ¿qué debe saber, sentir o decidir este público al terminar? A partir de ella se escribe el mensaje central en una frase. Un público de vecinos sin formación técnica necesita términos simples y ejemplos; una comisión que evalúa necesita ver criterios, pruebas y decisiones; un visitante de feria necesita una idea que pueda captar en segundos.",
        "La accesibilidad se piensa desde el comienzo: letra grande, buen contraste, ritmo pausado, descripción en voz alta de lo que muestran las imágenes y una alternativa si falla la tecnología. También se actúa con honestidad: se muestran las pruebas que fallaron y lo que se aprendió, porque el proceso es parte de lo que se comunica.",
    ],
    vocab=[("propósito", "para qué se hizo el proyecto y qué necesidad atiende"), ("público", "personas a quienes se dirige la presentación"), ("mensaje central", "idea principal que el público debe recordar, en una frase"), ("proceso", "investigación, pruebas y decisiones que llevaron al resultado"), ("accesibilidad de la presentación", "ajustes para que todas las personas puedan seguirla")],
    worked=[
        ("Elegir qué comunicar", "Con la ficha, ¿qué debe priorizar la presentación de la situación 2?", ["La comisión revisa el proceso y quiere ver que hubo criterios.", "Hay que mostrar criterios, pruebas y decisiones con su evidencia."], "El proceso: criterios, pruebas y decisiones"),
        ("Repartir el tiempo", "En la situación 1 hay 15 minutos y se reservan 5 para preguntas. ¿Cuántos minutos hay para exponer?", ["Se resta el tiempo de preguntas al total.", "15 − 5 = 10."], "10 minutos"),
    ],
    mistakes=[("Usar la misma presentación para todos los públicos.", "Cada público necesita otro lenguaje, otro detalle y otro tiempo.", "Escribe el objetivo y el mensaje central de cada situación antes de preparar."),
              ("Mostrar solo lo que salió bien.", "Oculta el proceso y quita credibilidad al equipo.", "Incluye pruebas fallidas y lo que se aprendió de ellas.")],
    T=[
        ('abc', '¿Qué tres elementos de un proyecto se comunican en una presentación?', 'Propósito, aspectos del proceso y resultados', 'Nombre del curso, fecha de entrega y firma del equipo ante la comisión', 'Solo el resultado final, su precio y el nombre de quienes lo hicieron', 'Presentar un proyecto es comunicar para qué se hizo, cómo se llegó y qué se logró.'),
        ('abc', '{F} ¿Cuál es el objetivo de la situación 1?', 'Obtener el apoyo de vecinas y vecinos', 'Demostrar criterios ante docentes', 'Lograr que visitantes recuerden el proyecto', 'La ficha indica que la reunión con el barrio busca su apoyo.'),
        ('=', '{F} ¿Cuántos minutos suman las tres situaciones?', '15+10+2', 'Se suman los minutos de cada situación.', ' minutos'),
        ('abc', '{F} ¿Qué lenguaje conviene en la situación 1?', 'Simple y sin términos técnicos, explicando lo necesario', 'Técnico y con muchas siglas, para que el equipo parezca más serio y preparado', 'El mismo de la comisión de docentes, porque así se evita cambiar el texto', 'El público no tiene formación técnica, así que el lenguaje debe ser claro.'),
        ('abc', '{F} ¿Qué prioridad tiene la presentación de la situación 2?', 'Mostrar el proceso: criterios, pruebas y decisiones', 'Mostrar solo el resultado terminado y lo bonito que quedó', 'Conseguir que los docentes se emocionen con la historia del equipo', 'La comisión evalúa si las decisiones tuvieron criterios, y eso se ve en el proceso.'),
        ('abc', '{F} ¿Qué adaptación de accesibilidad conviene en la situación 1?', 'Letra grande, buen contraste, ritmo pausado y descripción hablada de las imágenes', 'Letra pequeña y mucho texto, para incluir más datos y que no falte información', 'Hablar rápido y sin pausas para que alcance el tiempo, sin describir las imágenes', 'Hay personas mayores en el público, y esas ayudas facilitan seguir la presentación.'),
        ('abc', '{F} ¿Qué mensaje central es adecuado para la feria (situación 3)?', 'Una sola frase: una pérgola que da sombra y asiento a todas las personas del patio', 'Una lista de las quince decisiones técnicas tomadas durante el proceso, con sus costos', 'El historial completo de pruebas y costos, explicado hoja por hoja al visitante', 'Con 2 minutos de atención, el mensaje debe caber en una frase.'),
        ('=', '{F} En la situación 2 tienes 10 minutos: 2 para el propósito y 5 para el proceso. ¿Cuántos minutos quedan para resultados y preguntas?', '10-2-5', 'Se restan al total los minutos ya asignados.', ' minutos'),
        ('abc', '{F} Para preparar la situación 1, ¿qué pregunta guía ayuda más?', '¿Qué necesita saber y decidir este público al terminar?', '¿Qué datos técnicos puedo mostrar para impresionar a quienes escuchan?', '¿Cuánto tiempo puedo hablar sin parar para que se note el trabajo del equipo?', 'La pregunta guía parte de lo que el público necesita, no de lo que el equipo quiere mostrar.'),
        ('abc', '{F} Un equipo usa la misma presentación de 15 minutos en las tres situaciones. ¿Qué problema principal tiene?', 'No se adapta al tiempo, al nivel de detalle ni al objetivo de cada público', 'Ninguno, porque repetir la misma presentación es más ordenado y evita errores', 'Que debería usar siempre la presentación de 2 minutos, que es la más clara para todos', 'Cada situación tiene tiempo y objetivo distintos, y la misma presentación no sirve para todas.'),
        ('abc', '{F} En la feria, un integrante dice: «pongamos todos los planos en el panel». ¿Qué respuesta es mejor?', 'Con 2 minutos de atención el panel debe mostrar la idea central y dejar los planos para quien quiera ver más', 'Sí, porque mientras más planos y datos haya en el panel, más seriedad transmite el proyecto', 'No, y conviene que el panel lleve solo texto para que los visitantes lean con calma', 'La atención es muy breve, así que se jerarquiza y se deja el detalle disponible aparte.'),
        ('abc', '{F} ¿Qué cambia entre presentar el proceso a docentes y presentarlo a vecinos?', 'Con docentes se muestran criterios y evidencias; con vecinos se cuenta en simple y se destaca su beneficio', 'Nada: el proceso debe contarse igual a todos para ser justo con cada público', 'Con vecinos se cuenta solo el resultado y con docentes solo el proceso, sin explicar el propósito', 'Cambian el lenguaje, el detalle y el énfasis, no la honestidad del contenido.'),
        ('abc', 'El equipo quiere mostrar al jurado solo las pruebas que salieron bien. ¿Qué corresponde?', 'Mostrar también las pruebas fallidas y lo que se aprendió, porque el proceso es parte de lo que se evalúa', 'Ocultarlas, porque un jurado desconfía de un equipo que muestra sus errores y se ve inseguro', 'Mostrar solo las fallidas, porque de los errores se aprende más que de los aciertos', 'Un proceso honesto incluye errores y aprendizajes, lo que da credibilidad.'),
    ],
    ctx=('abc', 'Una estudiante prepara: «Público: vecinas y vecinos. Mensaje: la pérgola da sombra y asiento. Tiempo: 15 minutos con 5 de preguntas. Lenguaje simple, letra grande, describo cada imagen en voz alta». ¿Qué hace bien?', 'Ajusta el mensaje, el tiempo, el lenguaje y la accesibilidad al público', 'Prepara una presentación técnica para impresionar', 'Ignora el tiempo disponible', 'La preparación considera el público, el mensaje y las ayudas de accesibilidad.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué se comunica en la presentación de un proyecto?", "El propósito, aspectos del proceso y los resultados", "Los tres hacen entendible y creíble el proyecto."),
        ("¿Qué pregunta guía ayuda a preparar una presentación?", "¿Qué debe saber, sentir o decidir el público al terminar?", "Parte de lo que el público necesita."),
        ("¿Qué se hace con las pruebas que fallaron?", "Se muestran junto con lo que se aprendió", "Son una parte honesta y útil del proceso."),
    ],
    op=("Elige un proyecto inventado: (a) un mesón de biblioteca accesible, (b) un paradero con techo, (c) un patio con sombra. Describe tres públicos distintos (por ejemplo, vecinos, una comisión de docentes y visitantes de una feria). Para cada uno escribe el objetivo, el tiempo, el mensaje central en una frase y una decisión de lenguaje o accesibilidad.",
        "Proyecto (b): paradero con techo. Vecinos (10 min): objetivo, lograr apoyo; mensaje: «esperar el bus sin mojarse y sentados»; lenguaje simple y letra grande. Comisión (8 min): objetivo, mostrar criterios; mensaje: «decisiones con costo por año y accesibilidad»; mostrar pruebas. Feria (2 min): objetivo, recordar; mensaje: «un techo largo para toda la fila»; panel con una imagen grande.",
        ["distingue objetivo, tiempo y mensaje de cada público", "adapta el lenguaje o la accesibilidad", "escribe mensajes centrales en una frase"],
        ["tabla con tres públicos, objetivo, tiempo, mensaje y adaptación"],
        ["usar el mismo mensaje para todos", "olvidar el tiempo", "no pensar en accesibilidad"],
        "Pregunta: «¿qué cambiaste entre un público y otro?». Si no cambió nada, pídele que ajuste lenguaje o detalle."),
    reinforce="Explica el mismo objeto cotidiano (por ejemplo, una silla) en 1 minuto a una persona de tu casa y en 20 segundos a un amigo. Anota qué sacaste en el segundo caso.",
    extend="Explica por qué mostrar un error del proceso puede dar más confianza al público que ocultarlo.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 11 (medios para presentar, datos de ejemplo inventados). "
     "Panel impreso: preparar toma 4 horas; no necesita electricidad ni internet; se lee de pie; no se puede cambiar una vez impreso. "
     "Maqueta física: preparar toma 6 horas; no necesita electricidad ni internet; permite ver y tocar el volumen. "
     "Presentación en pantalla (diapositivas): preparar toma 3 horas; necesita electricidad y un equipo; se actualiza fácilmente. "
     "Modelo digital en tres dimensiones (3D): preparar toma 8 horas y un computador; permite recorrerlo en pantalla; sin equipo, no se puede mostrar. "
     "Recorrido en realidad virtual: preparar toma 12 horas y requiere equipo especial. "
     "La sala de la presentación a veces no tiene internet.")
build(
    O3, 2, F,
    use="Aprenderé a elegir medios tradicionales y emergentes para presentar un proyecto según su propósito, público, tiempo, recursos y accesibilidad, con un plan B si falla la tecnología.",
    prior=["Sé adaptar una presentación a un público.", "Sé sumar horas de trabajo.", "Sé que los datos se rotulan como de ejemplo."],
    explain=[
        "Los medios tradicionales para presentar proyectos incluyen el dibujo a mano, el panel impreso, la maqueta física y la exposición oral. Los medios emergentes, como los modelos digitales en tres dimensiones, los recorridos de realidad virtual, el video o las plataformas colaborativas, permiten mostrar el proyecto de otras maneras. Ninguno es mejor por sí mismo: se elige según el propósito, el público, el tiempo de preparación, los recursos y la accesibilidad.",
        "Cada medio tiene ventajas y límites. Una maqueta permite tocar el volumen, pero es difícil de transportar. Una presentación en pantalla se actualiza fácilmente, pero depende de electricidad y de un equipo. Por eso se prepara siempre un plan B sin conectividad: por ejemplo, una versión impresa. La tecnología no reemplaza el mensaje: una idea confusa no mejora por mostrarse en un medio moderno.",
        "Además se cuidan la accesibilidad (alto contraste, letra grande, descripción hablada o escrita de las imágenes, subtítulos en videos) y los derechos: se usan imágenes propias, con permiso o libres de derechos, y no se publican fotografías de personas sin su permiso. Los tiempos y datos de esta clase son de ejemplo.",
    ],
    vocab=[("medio tradicional", "forma de presentar sin tecnología digital, como un panel o una maqueta"), ("medio emergente", "forma de presentar con tecnología reciente, como realidad virtual"), ("plan B", "alternativa preparada por si falla el medio principal"), ("conectividad", "disponibilidad de internet o de red"), ("descripción alternativa", "texto que dice lo que muestra una imagen")],
    worked=[
        ("Sumar horas", "¿Cuántas horas toma preparar el panel impreso y la presentación en pantalla?", ["El panel toma 4 horas y la presentación en pantalla toma 3.", "4 + 3 = 7."], "7 horas"),
        ("Elegir con restricciones", "La sala no tiene internet y hay poco tiempo. ¿Qué medio de la ficha no depende de internet y se prepara en 4 horas?", ["Se buscan medios sin internet y con menos horas.", "El panel impreso toma 4 horas y no necesita internet."], "El panel impreso"),
    ],
    mistakes=[("Elegir el medio más moderno sin revisar si hay equipo, electricidad y tiempo.", "La presentación puede fallar el día en que se necesita.", "Compara medios con recursos reales y prepara un plan B."),
              ("Usar fotografías de vecinos tomadas sin su permiso.", "Se vulnera su privacidad y sus derechos.", "Usa fotos propias con permiso, dibujos o imágenes libres de derechos.")],
    T=[
        ('abc', '¿Cuál es un medio tradicional de presentación?', 'Una maqueta física', 'Un recorrido en realidad virtual', 'Un modelo digital en tres dimensiones', 'La maqueta física es un medio sin tecnología digital; los otros dos son medios emergentes.'),
        ('abc', '¿Cuál es un medio emergente de presentación?', 'Un recorrido en realidad virtual', 'Un panel impreso con letra grande y fotografías', 'Un dibujo hecho a mano sobre papel cuadriculado', 'La realidad virtual es una tecnología reciente; el panel y el dibujo son tradicionales.'),
        ('=', '{F} ¿Cuántas horas toma preparar el panel impreso y la maqueta física?', '4+6', 'Se suman las horas de preparación de ambos medios.', ' horas'),
        ('abc', '{F} ¿Qué medio de la ficha permite ver y tocar el volumen?', 'La maqueta física', 'El panel impreso', 'La presentación en pantalla', 'La ficha dice que la maqueta permite ver y tocar el volumen.'),
        ('abc', '{F} Si falla la electricidad antes de comenzar, ¿qué plan B es razonable?', 'Llevar el panel impreso y la maqueta como respaldo', 'Llevar otra copia del archivo en el mismo computador', 'Cancelar la presentación', 'El panel y la maqueta no necesitan electricidad ni internet.'),
        ('=', '{F} Hay 20 horas disponibles y se preparan el panel (4 h), la maqueta (6 h) y la presentación en pantalla (3 h). ¿Cuántas horas sobran?', '20-4-6-3', 'Se resta del total la suma de las horas usadas.', ' horas'),
        ('abc', '{F} El público son vecinos mayores, la sala no tiene internet y hay 10 horas. ¿Qué combinación es más adecuada?', 'Panel impreso y maqueta, que suman 10 horas y no dependen de internet', 'Modelo 3D y realidad virtual, que suman 20 horas y dan una experiencia moderna', 'Presentación en pantalla y modelo 3D, que suman 11 horas y se actualizan fácilmente', 'Solo la primera cabe en 10 horas y funciona sin internet.'),
        ('abc', '{F} ¿Qué ventaja da la presentación en pantalla frente al panel impreso?', 'Se actualiza fácilmente si el proyecto cambia', 'No necesita electricidad ni un equipo para mostrarse', 'Permite tocar el volumen y ver el proyecto desde todos los lados', 'La ficha dice que la presentación en pantalla se actualiza fácilmente, mientras el panel no se puede cambiar.'),
        ('abc', 'Una persona con baja visión sigue una presentación en pantalla. ¿Qué ayuda sirve?', 'Alto contraste, letra grande y descripción hablada de cada imagen', 'Colores claros y suaves sobre fondo blanco, para no cansar la vista', 'Más animaciones y efectos de movimiento para mantener la atención de la persona', 'El contraste, el tamaño y la descripción hablada mejoran el acceso a la información.'),
        ('abc', '{F} Un equipo quiere usar realidad virtual, pero tiene solo 10 horas y un público mayor sin equipo. ¿Cuál es el mejor consejo?', 'Elegir el medio según propósito, público y recursos: mejor un panel y una maqueta bien hechos que una tecnología que no alcanza', 'Usar la realidad virtual igual, porque la tecnología más nueva siempre impresiona al público', 'Hacer la realidad virtual en las 10 horas, aunque quede a medias y el público no pueda verla', 'La elección debe ajustarse a lo que el público puede usar y al tiempo real.'),
        ('abc', 'Un estudiante quiere incluir una fotografía de vecinos tomada sin su permiso. ¿Qué corresponde?', 'No usarla; usar fotos propias con permiso, dibujos o imágenes libres de derechos', 'Usarla, porque es solo una fotografía tomada en un lugar público del barrio', 'Usarla agregando una nota al pie que indique quiénes aparecen en la foto', 'La imagen de una persona requiere su permiso, aunque se agregue una nota.'),
        ('abc', '{F} ¿Qué plan de medios es más robusto para una feria con riesgo de falla eléctrica?', 'Un panel impreso como medio principal, una maqueta y una presentación en pantalla opcional, con copia de respaldo', 'Solo el modelo digital en 3D, porque es el medio moderno y llama más la atención', 'Solo una presentación en pantalla con internet, porque se actualiza en el momento', 'El plan combina medios que no dependen de electricidad con un apoyo opcional.'),
        ('abc', 'Una compañera dice: «con tecnología emergente el proyecto vale más». ¿Qué responde mejor?', 'La tecnología es un medio; vale lo que comunica del propósito y el proceso al público', 'Tiene razón, porque la tecnología siempre mejora el proyecto y lo hace más moderno', 'No importa el medio ni el mensaje si el proyecto ya está terminado y bien hecho', 'El medio sirve al mensaje; no reemplaza la claridad de la idea.'),
    ],
    ctx=('abc', 'Un equipo escribe: «Medio principal: panel y maqueta (10 horas). Apoyo: presentación en pantalla (3 horas) solo si hay electricidad. Respaldo: láminas impresas». ¿Qué hace bien?', 'Elige medios según los recursos y deja un respaldo sin conectividad', 'Depende solo de internet', 'Elige el medio más costoso sin revisar el público', 'El plan combina medios, recursos y plan B.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un plan B de presentación?", "Una alternativa preparada por si falla el medio principal", "Evita suspender la presentación ante una falla."),
        ("¿Qué se considera para elegir un medio?", "Propósito, público, tiempo, recursos y accesibilidad", "Un medio se elige para el caso, no por moda."),
        ("¿Qué se puede hacer con las imágenes de personas?", "Usar solo las que tienen su permiso o reemplazarlas por dibujos", "La privacidad de las personas se respeta."),
    ],
    op=("Tu equipo debe presentar un proyecto de ejemplo ante familias de un barrio. Datos inventados: 12 horas de preparación, sala sin internet, una persona con baja visión y otra que usa silla de ruedas. Usa los tiempos de la ficha 11 para elegir dos medios principales, un apoyo opcional y un plan B. Calcula las horas usadas y escribe una ayuda de accesibilidad por medio.",
        "Medios: panel impreso (4 h) y maqueta (6 h) = 10 horas; apoyo opcional: presentación en pantalla (3 h) = 13 horas, que excede 12, así que se deja sin hacer. Plan B: láminas impresas. Accesibilidad: panel con letra grande y contraste alto; maqueta sobre una mesa baja y descripción oral para quien no la ve.",
        ["suma las horas y respeta el tiempo", "elige medios sin internet cuando no hay conexión", "propone ayudas de accesibilidad concretas"],
        ["hoja con medios, horas, plan B y ayudas de accesibilidad"],
        ["pasarse del tiempo disponible", "depender de internet sin plan B", "no describir las imágenes"],
        "Pregunta: «¿qué haces si falla la electricidad?». Si no hay respuesta, pídele que defina el plan B."),
    reinforce="Haz un dibujo a mano de tu pieza y descríbelo en voz alta como si alguien no pudiera verlo. Anota si tu descripción alcanzó para entenderlo.",
    extend="Explica una situación en la que un medio simple sea mejor que una tecnología reciente.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 12 (panel de ejemplo, inventado). Panel vertical de 90 cm de ancho por 120 cm de alto, dividido en una cuadrícula de 3 columnas por 4 filas; cada celda mide 30 cm por 30 cm. "
     "Zonas propuestas: título (3 celdas, una fila completa), imagen principal (4 celdas, un bloque de 2 por 2), proceso (3 celdas) y resultados (2 celdas). "
     "Reglas de ejemplo del curso: la altura de las letras debe ser al menos 1 cm por cada 2 m de distancia de lectura; cada bloque de texto tiene máximo 40 palabras; el texto oscuro va sobre fondo claro con buen contraste. "
     "Distancia de lectura del título: 6 m. Distancia de lectura del texto del proceso: 2 m.")
build(
    O3, 3, F,
    use="Aprenderé a decidir la jerarquía, la distribución y la legibilidad de un panel de proyecto usando una cuadrícula, reglas de tamaño de letra y ayudas de accesibilidad.",
    prior=["Sé distribuir zonas en una cuadrícula.", "Sé dividir números enteros.", "Sé que una imagen necesita descripción."],
    explain=[
        "La jerarquía visual es el orden de importancia que se marca con tamaño, posición y contraste: lo más importante se ve primero. En un panel de proyecto el título y la imagen principal suelen ir arriba o al centro, y los bloques de texto siguen un orden de lectura claro, de izquierda a derecha y de arriba abajo. Una cuadrícula ayuda a repartir el espacio de forma ordenada y a alinear los bloques.",
        "La legibilidad depende de la distancia, el tamaño de las letras y el contraste. En este curso se usa una regla de ejemplo: al menos 1 cm de altura de letra por cada 2 metros de distancia de lectura. También se limitan las palabras de cada bloque, para que el texto se lea rápido. El texto oscuro sobre fondo claro tiene buen contraste; los colores claros sobre fondo claro se leen mal, sobre todo con baja visión.",
        "La accesibilidad incluye una descripción alternativa de cada imagen: una frase breve que dice qué muestra y para qué sirve, por ejemplo la planta de un proyecto con sus asientos y su acceso. Una etiqueta como «imagen 1» no informa nada. Las reglas de esta clase son de ejemplo; en un trabajo real se consultan las guías de accesibilidad vigentes.",
    ],
    vocab=[("jerarquía visual", "orden de importancia marcado con tamaño, posición y contraste"), ("cuadrícula", "red de columnas y filas que ordena el espacio"), ("legibilidad", "facilidad para leer un texto a cierta distancia"), ("contraste", "diferencia entre el color del texto y el del fondo"), ("descripción alternativa", "frase que dice qué muestra una imagen")],
    worked=[
        ("Calcular el tamaño de letra", "Con la ficha, ¿cuál es la altura mínima de letra para un texto leído a 4 m?", ["Regla: 1 cm por cada 2 m de distancia.", "4 ÷ 2 = 2."], "2 cm"),
        ("Revisar un bloque", "Un bloque de proceso tiene 52 palabras. ¿Cuántas sobran respecto del máximo?", ["El máximo es 40 palabras por bloque.", "52 − 40 = 12."], "12 palabras"),
    ],
    mistakes=[("Llenar el panel de texto pequeño para que no falte información.", "Nadie lo lee desde la distancia de lectura prevista y se pierde la jerarquía.", "Reduce el texto a lo esencial y deja el detalle para una hoja aparte."),
              ("Describir una imagen con «imagen 1».", "No entrega información a quien no la ve.", "Escribe qué muestra y para qué sirve en una frase.")],
    T=[
        ('abc', '¿Qué es la jerarquía visual en un panel?', 'El orden de importancia que se marca con tamaño, posición y contraste', 'El orden alfabético en que se escriben los títulos de cada bloque', 'La cantidad de colores que se usan en el panel para destacar los bloques', 'La jerarquía hace que lo más importante se vea primero.'),
        ('=', '{F} ¿Cuántas celdas tiene la cuadrícula (3 columnas por 4 filas)?', '3*4', 'El número de celdas es columnas por filas.', ' celdas'),
        ('=', '{F} ¿Cuántas celdas suman las cuatro zonas propuestas?', '3+4+3+2', 'Se suman las celdas de título, imagen, proceso y resultados.', ' celdas'),
        ('=', '{F} ¿Cuál es la altura mínima de letra del título, leído a 6 m?', '6//2', 'Se aplica 1 cm por cada 2 m de distancia.', ' cm'),
        ('=', '{F} ¿Cuál es la altura mínima de letra del texto del proceso, leído a 2 m?', '2//2', 'Se aplica 1 cm por cada 2 m de distancia.', ' cm'),
        ('abc', '{F} ¿Qué zona recibe el mayor espacio y por qué?', 'La imagen principal, de 4 celdas, porque comunica la idea central de un vistazo', 'Los resultados, de 2 celdas, porque son lo más importante del proyecto', 'El título, porque ocupa un borde y tiene la letra más grande del panel', 'La imagen principal tiene el bloque más grande de la ficha.'),
        ('abc', '{F} Un bloque de proceso tiene 55 palabras. ¿Qué corresponde?', 'Reducirlo a 40 palabras o menos, o dividirlo en dos bloques con una idea cada uno', 'Dejarlo, porque más texto informa más y el detalle ayuda a quien lee de cerca', 'Achicar la letra hasta que quepa en el mismo bloque y mantener todo el texto', 'La regla limita los bloques a 40 palabras y achicar la letra rompe la regla de tamaño.'),
        ('abc', '{F} ¿Qué combinación respeta la regla de contraste?', 'Texto gris muy oscuro sobre fondo blanco', 'Texto amarillo claro sobre fondo blanco', 'Texto celeste sobre fondo gris claro', 'El texto oscuro sobre fondo claro da buen contraste.'),
        ('=', '{F} Cada celda mide 30 cm de ancho. ¿Cuántos centímetros de ancho ocupa el título de 3 celdas en una fila?', '3*30', 'Se multiplica el ancho de una celda por 3.', ' cm'),
        ('abc', '{F} Un compañero propone poner el título en la celda inferior derecha «para dar sorpresa». ¿Qué problema tiene?', 'Rompe el orden de lectura y el título deja de ser lo primero que se ve', 'Ninguno, porque la sorpresa siempre ayuda a recordar el proyecto', 'Solo un problema de tamaño, porque en esa celda el título quedaría más pequeño', 'El título necesita una posición alta para organizar la lectura.'),
        ('abc', '{F} La imagen principal necesita una descripción alternativa. ¿Cuál es adecuada?', 'Planta de la pérgola que muestra 24 asientos y un acceso sin escalones', 'Imagen 1 de la pérgola, ubicada en el centro del panel', 'Foto bonita de la pérgola con colores vivos y buena luz', 'Una buena descripción dice qué muestra y para qué sirve.'),
        ('abc', '{F} La distancia de lectura del título pasa de 6 m a 8 m. ¿Qué ocurre con la altura mínima de letra?', 'Sube a 4 cm, y hay que comprobar que el título cabe en las 3 celdas', 'Baja a 2 cm, porque a mayor distancia se necesita menos letra', 'No cambia, porque la regla no depende de la distancia de lectura', 'Con 8 m, la regla da 8 ÷ 2 = 4 cm.'),
        ('abc', '¿Qué decisión de panel integra mejor jerarquía, legibilidad y accesibilidad?', 'Título grande arriba, imagen principal con descripción, bloques cortos, contraste alto y orden de lectura claro', 'Mucho texto pequeño distribuido en todo el panel, para que no falte información', 'Fondo oscuro con letras de color medio y sin descripciones, para que el panel se vea más moderno', 'Combina las tres ideas de la clase en decisiones concretas.'),
    ],
    ctx=('abc', 'Un grupo registra: «Título de 3 cm de altura leído a 6 m; bloques de 35 palabras; texto negro sobre fondo blanco; imagen con descripción». ¿Qué cumple bien?', 'Cumple las reglas de tamaño de letra, longitud, contraste y descripción', 'Incumple el tamaño de letra del título', 'Supera el máximo de palabras por bloque', 'Cada dato coincide con las reglas de la ficha.'),
    sc=[
        ("En Diseño y arquitectura: ¿para qué sirve una cuadrícula en un panel?", "Para repartir el espacio de forma ordenada y alinear los bloques", "Facilita la jerarquía y el orden de lectura."),
        ("¿Cómo se calcula la altura mínima de letra con la regla de ejemplo?", "Se divide la distancia de lectura en metros por 2 y da los centímetros", "La regla es 1 cm por cada 2 m."),
        ("¿Qué debe decir una descripción alternativa?", "Qué muestra la imagen y para qué sirve", "Así sirve a quien no la ve."),
    ],
    op=("Diseña la distribución de un panel de 60 cm por 90 cm con una cuadrícula de 2 columnas por 3 filas (celdas de 30 cm). Reparte las 6 celdas entre cuatro zonas: título, imagen, proceso y resultados. Calcula la altura mínima de letra del título si se lee a 4 m. Escribe una descripción alternativa de la imagen y el límite de palabras de un bloque.",
        "Título: 2 celdas; imagen: 2 celdas; proceso: 1 celda; resultados: 1 celda (suman 6). Altura de letra del título: 4 ÷ 2 = 2 cm. Descripción: planta de un paradero con techo y un espacio libre para silla de ruedas. Cada bloque de texto: máximo 40 palabras.",
        ["reparte las celdas sin pasarse", "calcula la altura de letra con la regla", "escribe una descripción alternativa útil"],
        ["esquema del panel con zonas, cálculo y descripción"],
        ["no sumar las celdas", "usar «imagen 1» como descripción", "bloques demasiado largos"],
        "Pregunta: «¿qué se ve primero y por qué?». Si no puede decirlo, pídele que marque la jerarquía."),
    reinforce="Mira un cartel de tu barrio desde lejos y anota qué se alcanza a leer. Estima a qué distancia dejas de leer el texto pequeño.",
    extend="Explica por qué la misma regla de tamaño de letra no sirve para una presentación en pantalla y un panel impreso.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 13 (plan de presentación de ejemplo, inventado). Presentación del proyecto «Pérgola de lectura» ante vecinas y vecinos: duración total de 15 minutos, de los cuales 5 son para preguntas. "
     "Equipo de cuatro personas ficticias: Ana, Bruno, Carla y Diego. "
     "Partes y tiempos propuestos: apertura y propósito 2 minutos; necesidad y evidencia 2 minutos; proceso y decisiones 3 minutos; resultado y accesibilidad 3 minutos. "
     "Medios: panel impreso y maqueta; presentación en pantalla opcional. "
     "Ensayos disponibles: 3 ensayos de 15 minutos cada uno.")
build(
    O3, 4, F,
    use="Aprenderé a gestionar una presentación: escribir un guion con tiempos, repartir roles, ensayar, preparar un plan B y responder preguntas con honestidad.",
    prior=["Sé elegir medios para un público.", "Sé calcular tiempos.", "Sé trabajar en equipo con roles."],
    explain=[
        "Gestionar una presentación es planificarla: qué se dirá, en qué orden, en cuánto tiempo, quién habla y con qué medios. El guion es un plan escrito con apertura (saludo y propósito), desarrollo (evidencia, proceso y resultado) y cierre (mensaje central y una invitación a opinar o a actuar). Se escribe con frases clave y no para leerse palabra por palabra, porque leer todo resta contacto con el público.",
        "Los turnos se reparten de forma equitativa y clara: cada integrante sabe cuándo habla y quién apoya con el panel o la maqueta. Se ensaya con cronómetro para comprobar que todo cabe en el tiempo, y se preparan respuestas a las preguntas probables. Cuando alguien pregunta algo que el equipo no sabe, se responde con honestidad: se dice lo que sí se sabe y se compromete a averiguar el resto.",
        "También se gestiona el espacio y la seguridad: llegar antes para revisar enchufes, accesos y la ubicación de la maqueta sobre una mesa estable, sin cables en el piso ni piezas sueltas. Se prepara un plan B por si falla la electricidad. Si se graba la presentación para revisarla, se pide permiso a las personas que aparecen.",
    ],
    vocab=[("guion", "plan escrito de qué se dirá, en qué orden y en cuánto tiempo"), ("turno", "parte de la presentación a cargo de una persona"), ("ensayo", "práctica completa antes de presentar"), ("plan B", "alternativa si falla el medio principal"), ("frases clave", "ideas cortas que ayudan a recordar sin leer todo")],
    worked=[
        ("Sumar el tiempo de las partes", "Con la ficha, ¿cuántos minutos suman las cuatro partes?", ["Se suman 2, 2, 3 y 3.", "2 + 2 + 3 + 3 = 10."], "10 minutos"),
        ("Repartir turnos", "Con cuatro personas y cuatro partes, ¿cómo se reparte con equidad?", ["Cada persona se hace cargo de una parte.", "Quien no habla apoya con el panel o la maqueta en su turno."], "Una parte por persona, con apoyo en los otros turnos"),
    ],
    mistakes=[("Leer el guion palabra por palabra.", "Se pierde el contacto con el público y cualquier despiste rompe la exposición.", "Escribe frases clave y practica explicarlas con tus palabras."),
              ("Ensayar una sola vez, el día anterior.", "No hay tiempo para ajustar el guion ni los tiempos.", "Haz varios ensayos con cronómetro y corrige entre ellos.")],
    T=[
        ('abc', '¿Qué es un guion de presentación?', 'Un plan escrito de qué se dirá, en qué orden y en cuánto tiempo', 'El texto completo que se lee palabra por palabra, sin mirar al público', 'La lista de los materiales, las medidas y los costos que se usaron en la maqueta', 'El guion organiza contenido, orden y tiempos.'),
        ('=', '{F} Una persona propone alargar «proceso y decisiones» de 3 a 4 minutos sin cambiar las otras partes. ¿Cuántos minutos sumarían entonces las cuatro partes?', '2+2+4+3', 'Se suman los minutos de las cuatro partes con el cambio propuesto.', ' minutos'),
        ('=', '{F} ¿Cuántos minutos de ensayo suman los tres ensayos disponibles?', '3*15', 'Se multiplica el número de ensayos por su duración.', ' minutos'),
        ('abc', '¿Qué debería tener el cierre de una presentación?', 'El mensaje central en una frase y una invitación a opinar o a actuar', 'Una disculpa por los posibles errores y una explicación de lo que faltó', 'Una lista de todos los datos mostrados, repetidos en el mismo orden', 'El cierre refuerza la idea principal y deja una acción posible.'),
        ('abc', '{F} Con cuatro integrantes y cuatro partes, ¿qué reparto es equitativo?', 'Una parte por persona, con turnos claros y quien apoya con el panel', 'Una sola persona habla todo el tiempo y las demás observan en silencio para no interrumpir', 'Todos hablan en cada parte, sin turnos fijos, para que nadie quede fuera', 'El reparto equitativo deja un turno claro para cada integrante.'),
        ('=', '{F} Se agrega una demostración de 2 minutos sin cambiar los 15 minutos totales ni los 5 de preguntas. ¿Cuántos minutos quedan para las cuatro partes?', '15-5-2', 'Se restan al total las preguntas y la demostración.', ' minutos'),
        ('abc', '{F} Con esa demostración, ¿qué ajuste es razonable?', 'Recortar 2 minutos de las partes, por ejemplo de apertura y proceso, manteniendo el mensaje central', 'Quitar el tiempo de preguntas, porque el público ya vio todo lo importante', 'Hablar más rápido para que todo el contenido siga cabiendo en los mismos minutos', 'Las partes suman 10 minutos y deben bajar a 8; recortar contenido es mejor que acelerar o eliminar las preguntas.'),
        ('abc', '¿Para qué sirve ensayar con cronómetro?', 'Para comprobar que el guion cabe en el tiempo y ajustarlo antes', 'Para aprender el guion de memoria y recitarlo palabra por palabra el día final', 'Para evitar preparar respuestas, porque con práctica surgen solas en el momento', 'El cronómetro muestra si el tiempo alcanza y permite corregir.'),
        ('abc', '{F} Se corta la electricidad antes de comenzar. ¿Qué plan B corresponde?', 'Presentar con el panel impreso y la maqueta, y dejar la pantalla como apoyo', 'Suspender la presentación hasta que vuelva la electricidad, aunque sea otro día', 'Esperar en silencio frente al público sin explicar qué ocurre ni empezar', 'Los medios sin electricidad permiten seguir.'),
        ('abc', 'Alguien del público hace una pregunta que el equipo no sabe contestar. ¿Qué corresponde?', 'Reconocerlo con honestidad, decir lo que sí saben y comprometerse a averiguar el resto', 'Inventar una respuesta que suene segura para no perder credibilidad', 'Cambiar de tema rápidamente sin responder para no mostrar que no saben', 'La honestidad da credibilidad y evita información falsa.'),
        ('abc', '{F} Un compañero propone leer el guion palabra por palabra. ¿Qué respuesta es mejor?', 'Usar frases clave y mirar al público, porque leer todo resta contacto y flexibilidad', 'Está bien, porque leer palabra por palabra asegura que nadie se equivoque ni se olvide', 'Mejor improvisar sin guion, porque así la presentación se ve más natural y cercana', 'Un guion con frases clave da seguridad sin perder cercanía.'),
        ('abc', '{F} ¿Qué cronograma de preparación es más completo?', 'Definir el mensaje, ordenar el guion, preparar medios, hacer tres ensayos con cronómetro y probar el plan B', 'Hacer el panel y la maqueta, y esperar el día de la presentación para ver qué se dice', 'Ensayar una sola vez el día anterior y revisar el espacio al llegar', 'Cubre contenido, medios, práctica, espacio y respaldo.'),
        ('abc', '{F} ¿Qué cuidado de seguridad corresponde con la maqueta en la sala?', 'Dejarla sobre una mesa estable, sin cables en el piso ni piezas cortantes sueltas', 'Colgarla de un borde de la mesa para que el público la vea mejor', 'Ponerla en el pasillo de paso para que todas las personas la vean al entrar', 'Una mesa estable y un espacio despejado evitan caídas y cortes.'),
    ],
    ctx=('abc', 'Un equipo anota: «Partes: 2 + 2 + 3 + 3 = 10 minutos; preguntas: 5 minutos; ensayos: 3 con cronómetro; plan B: panel y maqueta». ¿Qué hace bien?', 'Suma los tiempos, reserva preguntas, ensaya y prepara un plan B', 'Deja las preguntas para si sobra tiempo', 'Planea un solo ensayo sin cronómetro', 'El plan es verificable, con tiempos, práctica y respaldo.'),
    sc=[
        ("En Diseño y arquitectura: ¿cuáles son las partes de un guion?", "Apertura, desarrollo y cierre", "Organizan el mensaje en un orden claro."),
        ("¿Qué se hace al ensayar?", "Se practica completo con cronómetro y se ajusta", "Así se comprueba que el tiempo alcanza."),
        ("¿Qué se responde ante una pregunta que no se sabe?", "Se dice lo que sí se sabe y se compromete a averiguar", "La honestidad evita informar algo falso."),
    ],
    op=("Un equipo de tres personas debe presentar un proyecto de ejemplo a una comisión durante 12 minutos, con 4 de preguntas. Elige un proyecto (a) mesón de biblioteca accesible o (b) paradero con techo. Escribe el guion con cuatro partes y sus minutos (suman 8), quién habla en cada una, el mensaje de cierre, un plan B y dos preguntas probables con una respuesta honesta cada una.",
        "Proyecto (b): paradero. Partes: apertura 1 minuto (Ana), necesidad 2 (Bruno), proceso y decisiones 3 (Carla), resultado y accesibilidad 2 (Ana): 1 + 2 + 3 + 2 = 8. Cierre: «un techo largo para toda la fila». Plan B: láminas impresas. Pregunta: ¿cuánto cuesta? Respuesta: la estimación es de ejemplo y se confirmaría con una cotización.",
        ["los minutos de las partes suman 8", "reparte turnos con claridad", "incluye plan B y respuestas honestas"],
        ["guion con tiempos, turnos, plan B y preguntas"],
        ["pasarse del tiempo", "no definir quién habla", "inventar datos al responder"],
        "Pregunta: «¿qué haces si falla la pantalla?». Si no tiene plan B, pídele que lo agregue."),
    reinforce="Explica a una persona de tu casa, en 2 minutos y con un cronómetro, cómo se arma una silla o una mesa simple. Anota en cuánto tiempo terminaste.",
    extend="Explica por qué repartir los turnos con equidad mejora la presentación y no solo la convivencia del equipo.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 14 (pauta y observaciones de ejemplo, inventadas). Pauta con cuatro criterios, cada uno puntuado de 1 a 4 (4 = logrado plenamente): C1 ajuste al público; C2 claridad del mensaje central; C3 manejo del tiempo; C4 accesibilidad de los medios. "
     "Observaciones de una presentación de ejemplo ante vecinos, planificada para 15 minutos: usó términos técnicos sin explicarlos; el mensaje central se entendía en una frase; duró 18 minutos; el panel tenía letra grande y contraste alto, pero la maqueta no tenía descripción oral. "
     "Puntajes de tres observadoras: C1: 2, 2, 3; C2: 4, 4, 3; C3: 2, 1, 2; C4: 3, 3, 4.")
build(
    O3, 5, F,
    use="Aprenderé a revisar una presentación con una pauta de criterios: registrar evidencia, sumar puntajes, dar retroalimentación respetuosa y hacer un plan de mejora priorizado.",
    prior=["Sé gestionar una presentación.", "Sé sumar puntajes.", "Sé dar un comentario descriptivo y respetuoso."],
    explain=[
        "Revisar una presentación es compararla con criterios observables y no con una impresión general. Una pauta define los criterios (por ejemplo, ajuste al público, claridad del mensaje, manejo del tiempo y accesibilidad) y una escala de puntaje con descriptores. Cada persona que observa anota la evidencia (qué se vio u oyó) y luego asigna el puntaje.",
        "Con varias observadoras se suman los puntajes de cada criterio y se comparan. Si hay diferencias grandes, no se promedian sin pensar: se vuelve a la evidencia, como el reloj que marcó el tiempo, y se acuerda el puntaje según los descriptores. El criterio con el total más bajo indica la prioridad de mejora, y los criterios con totales altos muestran lo que conviene mantener.",
        "La retroalimentación respetuosa describe lo que se observó y propone un paso siguiente, sin juzgar a la persona: «usaste cuatro términos sin definir; podrías explicarlos con un ejemplo». No dice «eres mala para explicar». Si se graba una presentación para revisarla, se pide permiso a las personas que aparecen y se usa solo para el fin acordado.",
    ],
    vocab=[("pauta", "tabla de criterios con escala de puntaje"), ("evidencia", "lo que se vio u oyó y respalda un puntaje"), ("descriptor", "texto que explica qué significa cada nivel de puntaje"), ("retroalimentación", "comentario que describe y orienta la mejora"), ("plan de mejora", "lista priorizada de cambios para la próxima vez")],
    worked=[
        ("Sumar un criterio", "Con la ficha, ¿cuánto suma C2 entre las tres observadoras?", ["Los puntajes de C2 son 4, 4 y 3.", "4 + 4 + 3 = 11."], "11 puntos"),
        ("Priorizar", "C3 suma 5 y C1 suma 7. ¿Cuál se prioriza para mejorar?", ["Se elige el criterio con el total más bajo.", "5 es menor que 7."], "C3, el manejo del tiempo"),
    ],
    mistakes=[("Promediar puntajes muy distintos sin volver a la evidencia.", "Se pierde la razón de la diferencia y el puntaje deja de ser confiable.", "Revisa la evidencia y acuerda el puntaje con los descriptores."),
              ("Comentar «eres mala para explicar».", "Juzga a la persona y no dice qué mejorar.", "Describe lo observado y propone un paso concreto.")],
    T=[
        ('abc', '¿Qué hace una buena pauta de observación de una presentación?', 'Define criterios observables y una escala para puntuar con evidencia', 'Pide una nota general al final, sin explicación de los criterios usados', 'Mide cuánto simpatiza el público con el equipo y cuánto aplaude al terminar', 'Una pauta permite revisar con criterios y no con impresiones.'),
        ('=', '{F} ¿Cuánto suma C1 entre las tres observadoras?', '2+2+3', 'Se suman los tres puntajes de C1.', ' puntos'),
        ('=', '{F} ¿Cuánto suma C3 entre las tres observadoras?', '2+1+2', 'Se suman los tres puntajes de C3.', ' puntos'),
        ('abc', '{F} ¿Qué criterio tuvo el mayor total?', 'C2, claridad del mensaje central, que suma 11 puntos', 'C4, accesibilidad de los medios, que suma 10 puntos', 'C1, ajuste al público, que suma 7 puntos', 'Los totales son C1 = 7, C2 = 11, C3 = 5 y C4 = 10.'),
        ('=', '{F} ¿Cuánto suma C4 entre las tres observadoras?', '3+3+4', 'Se suman los tres puntajes de C4.', ' puntos'),
        ('abc', '{F} ¿Qué observación respalda el puntaje bajo de C1?', 'Usó términos técnicos con vecinos sin explicarlos', 'Duró 18 minutos, tres más de los planificados', 'El panel tenía letra grande y contraste alto', 'C1 mide el ajuste al público, y los términos técnicos sin explicar lo desajustan.'),
        ('=', '{F} ¿Cuántos minutos se pasó la presentación de lo planificado (15 minutos)?', '18-15', 'Se resta lo planificado a lo que duró.', ' minutos'),
        ('abc', '{F} ¿Cuál es una retroalimentación descriptiva y útil sobre C4?', 'El panel tiene letra grande y contraste alto; falta describir la maqueta en voz alta para quienes no la ven', 'La maqueta quedó fea y desordenada, así que hay que rehacerla completa', 'Hay que mejorar la accesibilidad en general, porque faltó esfuerzo en esa parte', 'Describe lo observado y señala un paso concreto.'),
        ('abc', '{F} Dos observadoras puntuaron C3 con 2 y una con 1. ¿Qué corresponde?', 'Revisar la evidencia (el reloj marcó 18 minutos) y acordar el puntaje según los descriptores', 'Promediar los puntajes y no discutir más, para ahorrar tiempo en la revisión', 'Quedarse con el puntaje de la persona de más edad, porque tiene más experiencia', 'Las diferencias se resuelven volviendo a la evidencia y a la pauta.'),
        ('abc', '{F} Un integrante dice: «C2 tuvo 11, el más alto, así que no hay nada que mejorar». ¿Qué respuesta es mejor?', 'Un puntaje alto es un logro que se mantiene, pero C3 y C1 tuvieron los totales más bajos y se priorizan', 'Tiene razón: lo mejor se deja igual y los demás criterios ya no importan después del análisis', 'Hay que bajar el puntaje de C2 para que todos los criterios queden parejos', 'La pauta sirve para mantener lo logrado y priorizar los criterios más débiles.'),
        ('abc', '{F} ¿Cuál es un plan de mejora priorizado para la próxima presentación?', 'Primero ajustar el tiempo a 15 minutos con ensayo cronometrado; luego explicar los términos técnicos y describir la maqueta', 'Cambiar el color del panel y agrandar el título para que se vea más moderno', 'Hablar más rápido en todas las partes para recuperar los minutos que sobraron', 'Sigue el orden de los totales más bajos y propone acciones concretas.'),
        ('abc', '¿Qué comentario sobre una expositora es respetuoso y útil?', 'Al explicar el proceso usaste cuatro términos sin definir; podrías definirlos con un ejemplo', 'Eres muy mala para explicar y se nota que te falta práctica', 'Se nota que no te preparaste y que el equipo no se esforzó lo suficiente', 'Describe lo observado y propone un paso, sin juzgar a la persona.'),
        ('abc', 'La presentación se grabó para revisarla. ¿Qué corresponde?', 'Pedir permiso a quienes aparecen y usar la grabación solo para la revisión acordada', 'Publicarla en línea sin avisar, para que más personas puedan revisarla', 'Grabar en secreto para que nadie actúe distinto y la revisión sea más objetiva', 'Grabar y usar la imagen de personas requiere su permiso y un fin acordado.'),
    ],
    ctx=('abc', 'Una estudiante anota: «C3: 5 de 12, la presentación duró 18 minutos en lugar de 15. Acción: reducir la parte del proceso de 3 a 2 minutos y ensayar con cronómetro». ¿Qué hace bien?', 'Indica el puntaje, la evidencia y una acción concreta', 'Solo dice que fue demasiado larga', 'Culpa a una persona del equipo', 'La nota une puntaje, evidencia y acción.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un descriptor en una pauta?", "El texto que explica qué significa cada nivel de puntaje", "Permite puntuar con el mismo criterio."),
        ("¿Qué se hace si hay puntajes muy distintos?", "Se vuelve a la evidencia y se acuerda según los descriptores", "No se promedia sin entender la diferencia."),
        ("¿Qué criterio se prioriza para mejorar?", "El que tiene el total más bajo", "Es donde la presentación estuvo más débil."),
    ],
    op=("Observa esta presentación de ejemplo (inventada): el equipo explicó con ejemplos claros ante un público de estudiantes de primero medio, duró 9 minutos de los 10 previstos, el mensaje central fue «un mesón bajo para todas las personas», y usó un video sin subtítulos. Puntúa de 1 a 4 los criterios C1 a C4 de la ficha, escribe la evidencia de cada puntaje, redacta dos logros y una mejora respetuosa, y ordena un plan de mejora.",
        "C1: 4, usó ejemplos claros. C2: 4, el mensaje cabe en una frase. C3: 4, 9 de 10 minutos. C4: 2, el video no tenía subtítulos. Logros: ejemplos claros y mensaje central. Mejora: agregar subtítulos o una descripción escrita del video. Plan: primero subtitular el video, luego mantener el ensayo cronometrado.",
        ["puntúa cada criterio con evidencia", "redacta retroalimentación respetuosa", "ordena un plan de mejora"],
        ["pauta completa con evidencia, retroalimentación y plan"],
        ["puntuar sin evidencia", "comentar sobre la persona", "no priorizar"],
        "Pregunta: «¿qué viste u oíste que respalda este puntaje?». Si no hay evidencia, pídele que la agregue."),
    reinforce="Observa una explicación corta en un video o en tu casa y anota un logro y una mejora, usando un criterio.",
    extend="Explica por qué una pauta compartida antes de presentar mejora el trabajo del equipo.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 15 (obras de ejemplo, inventadas). "
     "Obra 1: «Casa del Río», vivienda de un pueblo ficticio de clima lluvioso, época A (de ejemplo). Muros de adobe (barro y paja) de 50 cm de espesor; techo de dos aguas muy inclinado con cubierta de paja; una puerta central de 90 cm de ancho y dos ventanas pequeñas iguales, una a cada lado de la puerta; planta rectangular de 6 m por 4 m. "
     "Obra 2: «Torre Faro», edificio de oficinas de una ciudad ficticia, época C (de ejemplo, reciente). Estructura de acero y fachada de vidrio de gran superficie; 12 pisos de 3 m de altura cada uno; planta cuadrada de 20 m por 20 m; el volumen se angosta hacia arriba; las ventanas forman franjas horizontales que se repiten en cada piso.")
build(
    O4, 1, F,
    use="Aprenderé a observar y describir con rasgos formales una pieza de diseño o una obra de arquitectura, antes de interpretarla o juzgarla.",
    prior=["Sé que describir no es opinar.", "Sé calcular áreas de rectángulos.", "Sé que cada obra nace en un contexto."],
    explain=[
        "Analizar estéticamente una pieza de diseño o una obra de arquitectura empieza por observarla con atención. La descripción formal dice qué elementos se ven y cómo están dispuestos: forma, volumen, línea, proporción, ritmo (repetición ordenada), simetría (partes iguales a ambos lados de un eje), escala (tamaño en relación con las personas), textura, color y luz. No usa opiniones como «linda» o «impresionante», porque esas palabras no se pueden comprobar mirando.",
        "El análisis sigue un orden: primero se describe lo que se ve, luego se analiza cómo se relacionan los elementos (por ejemplo, cómo el ritmo de las ventanas ordena la fachada), después se interpreta qué sensación o idea sugiere y, al final, se puede emitir un juicio. Cada paso se apoya en lo observado. Medir o calcular ayuda a describir con precisión: la altura total, la superficie de una planta o cuántas veces se repite un elemento.",
        "En este cuaderno las obras son inventadas y de épocas y procedencias de ejemplo, para aprender el método sin copiar obras reales con derechos. En un trabajo real se cita la autoría, la fecha y la fuente de cada obra, y se evita atribuir rasgos a una cultura sin una fuente confiable.",
    ],
    vocab=[("descripción formal", "relato de lo que se ve, sin opinar"), ("proporción", "relación de tamaño entre las partes de una obra"), ("ritmo", "repetición ordenada de un elemento"), ("simetría", "partes iguales a ambos lados de un eje"), ("escala", "tamaño de la obra en relación con las personas"), ("época", "período de tiempo en que se hizo la obra")],
    worked=[
        ("Describir sin opinar", "Con la ficha, ¿«La Casa del Río es acogedora» es una descripción formal? ¿Cómo se reescribe?", ["«Acogedora» es una opinión que no se comprueba mirando.", "Una descripción: «tiene dos ventanas pequeñas iguales, una a cada lado de la puerta central, y muros gruesos de adobe»."], "No es descripción; se reescribe con rasgos observables"),
        ("Medir para describir", "¿Cuántos m de alto tiene la Torre Faro?", ["Tiene 12 pisos de 3 m cada uno.", "12 × 3 = 36."], "36 m"),
    ],
    mistakes=[("Escribir «es impresionante» como descripción.", "Es una opinión, y otra persona puede no estar de acuerdo con ella.", "Describe lo que se ve: altura, material, ritmo, simetría."),
              ("Pasar directo a juzgar sin describir.", "El juicio queda sin apoyo observable.", "Sigue el orden: describir, analizar, interpretar y recién después juzgar.")],
    T=[
        ('abc', '¿Qué es una descripción formal de una obra?', 'Decir qué elementos se ven y cómo están dispuestos, sin opinar', 'Contar la vida y la formación de quien hizo la obra', 'Decir si la obra es linda o fea y por qué le gusta al equipo', 'La descripción formal nombra rasgos observables, no gustos.'),
        ('abc', '{F} ¿Cuál enunciado es una descripción y no una opinión?', 'La Casa del Río tiene dos ventanas pequeñas iguales a los lados de la puerta', 'La Casa del Río es acogedora y transmite calidez a quien la ve', 'La Torre Faro es impresionante y se impone sobre el resto de la ciudad', 'Solo el primero nombra algo que se puede comprobar mirando la obra.'),
        ('=', '{F} ¿Cuántos m² tiene la planta de la Casa del Río (6 m por 4 m)?', '6*4', 'El área de un rectángulo es largo por ancho.', ' m²'),
        ('=', '{F} ¿Cuántos metros de alto tiene la Torre Faro (12 pisos de 3 m)?', '12*3', 'Se multiplican los pisos por su altura.', ' m'),
        ('abc', '{F} ¿Qué rasgo de simetría se observa en la Casa del Río?', 'Las dos ventanas iguales, una a cada lado de la puerta central', 'La cubierta de paja y su color uniforme', 'El espesor de 50 cm de los muros de adobe', 'La simetría son partes iguales a ambos lados de un eje, aquí la puerta central.'),
        ('abc', '{F} ¿Qué elemento da ritmo en la Torre Faro?', 'Las franjas horizontales de ventanas que se repiten en cada piso', 'La estructura de acero, que sostiene los 12 pisos', 'La planta cuadrada de 20 m por 20 m', 'El ritmo es la repetición ordenada de un elemento, aquí las franjas.'),
        ('=', '{F} La planta de la Torre Faro mide 20 m por 20 m y tiene 12 pisos. ¿Cuántos m² de planta suman todos los pisos?', '20*20*12', 'Se calcula el área de un piso y se multiplica por 12.', ' m²'),
        ('abc', '{F} ¿Qué contraste de escala se observa entre las dos obras?', 'La Torre Faro es de gran escala vertical (36 m) y la Casa del Río es de escala baja, cercana a las personas', 'Las dos tienen escala baja, porque ambas se apoyan en el suelo', 'La Casa del Río es de mayor escala, porque sus muros de adobe son más gruesos', 'La torre mide 36 m y la casa es una vivienda de planta pequeña y poca altura.'),
        ('abc', '{F} ¿Qué obra muestra texturas ásperas y naturales por sus materiales?', 'La Casa del Río, por los muros de adobe y la cubierta de paja', 'La Torre Faro, por el vidrio y el acero brillantes de su fachada', 'Ninguna de las dos, porque la textura solo se aprecia al tocar las obras', 'El adobe y la paja tienen texturas rugosas; el vidrio y el acero son superficies lisas.'),
        ('abc', '{F} Alguien escribe: «La Torre Faro es fría». ¿Cómo se convierte en un análisis?', 'Relacionarlo con rasgos que se ven, como superficies lisas de vidrio y acero y repetición geométrica, que dan orden y distancia', 'Agregar más adjetivos, como «muy fría» y «lejana», para describirla mejor', 'Borrar la frase, porque cualquier sensación es una opinión y no sirve al análisis', 'El análisis conecta la sensación con rasgos que se ven en la obra.'),
        ('abc', '{F} ¿Qué comparación formal entre las obras es correcta?', 'La Casa es un volumen bajo y cerrado con pocas aberturas; la Torre es alta, con grandes superficies de vidrio', 'Ambas tienen grandes superficies de vidrio que la luz atraviesa', 'Ambas son de adobe, aunque una es mucho más alta', 'La ficha describe una casa de muros gruesos y ventanas pequeñas, y una torre de fachada de vidrio.'),
        ('abc', '{F} La Torre Faro se angosta hacia arriba. ¿Qué efecto visual puede producir?', 'Sensación de ligereza y de ascenso, porque el volumen parece afinarse hacia el cielo', 'Sensación de pesadez y de hundimiento, porque el edificio parece pesar más abajo', 'Ningún efecto, porque la forma de un edificio no cambia lo que se siente al mirarlo', 'Un volumen que se afina suele leerse como ascendente; es una interpretación apoyada en un rasgo observable.'),
        ('abc', '¿Qué orden sigue un análisis estético completo?', 'Describir, analizar relaciones, interpretar y, al final, juzgar', 'Juzgar primero para fijar una postura y luego describir lo que se ve', 'Interpretar primero lo que sugiere y después describir y analizar', 'Cada paso se apoya en lo observado en el anterior.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «La Casa del Río tiene planta de 24 m², muros de adobe de 50 cm, dos ventanas iguales a ambos lados de la puerta y un techo muy inclinado de paja». ¿Qué hace bien?', 'Describe con medidas y rasgos observables, sin opinar', 'Opina sobre lo linda que es', 'Compara con una obra que no está en la ficha', 'Usa solo datos comprobables de la ficha.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué diferencia hay entre describir y opinar?", "Describir nombra rasgos que se pueden comprobar; opinar expresa un gusto", "El análisis parte de lo comprobable."),
        ("¿Qué es el ritmo en una fachada?", "La repetición ordenada de un elemento", "Por ejemplo, las franjas de ventanas que se repiten."),
        ("¿Qué paso va después de describir?", "Analizar cómo se relacionan los elementos", "Luego vienen la interpretación y el juicio."),
    ],
    op=("Obra 3 (inventada): «Pabellón de Madera», de un parque de una ciudad ficticia, época B (de ejemplo). Estructura de madera con 8 pilares iguales en fila, techo plano, sin muros, una banca corrida de 6 m y un piso de baldosas claras. Describe la obra con cinco rasgos observables (forma, ritmo, simetría, escala, textura o material) sin usar opiniones, y relaciona al menos dos de ellos.",
        "Forma: volumen abierto con techo plano. Ritmo: ocho pilares iguales en fila. Simetría: los pilares se repiten con la misma separación. Escala: baja, cercana a las personas. Material: madera con textura fibrosa, y baldosas claras lisas en el piso.",
        ["usa cinco rasgos observables", "no incluye opiniones sin evidencia", "relaciona al menos dos elementos"],
        ["hoja con la descripción en cinco líneas"],
        ["usar adjetivos de gusto", "describir lo que no está en la ficha", "no relacionar elementos"],
        "Pregunta: «¿cómo se comprueba esto mirando la obra?». Si no se puede, pídele reescribirlo."),
    reinforce="Elige un objeto de tu casa y descríbelo con cinco rasgos observables, sin decir si te gusta.",
    extend="Explica por qué dos personas pueden describir igual una obra y juzgarla distinto.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 16 (obras de ejemplo, inventadas). "
     "Obra 4: «Mercado de la Piedra», de una región ficticia de montaña con inviernos fríos y mucha piedra, época A (de ejemplo): muros de piedra de 100 cm de espesor, pocas ventanas pequeñas, techo de losas de piedra y piso de tierra apisonada; un muro típico mide 10 m de largo y 3 m de alto. "
     "Obra 5: «Casa de Tablas», de una región ficticia de bosque con lluvias frecuentes, época B (de ejemplo): estructura de madera elevada del suelo sobre postes de 50 cm de alto, revestimiento de tablas traslapadas, techo de dos aguas con alero largo y ventanas medianas. "
     "Obra 6: «Biblioteca de Hormigón», de una ciudad ficticia, época C (de ejemplo): muros de hormigón visto (sin revestir), con las huellas de las tablas del molde, ventanas grandes con marcos de acero y techo plano.")
build(
    O4, 2, F,
    use="Aprenderé a relacionar la materialidad de una obra (materiales y modo de construir) con su clima, sus recursos, su época y lo que expresa.",
    prior=["Sé describir una obra con rasgos formales.", "Sé calcular volúmenes sencillos.", "Sé que los materiales tienen propiedades distintas."],
    explain=[
        "La materialidad de una obra es el conjunto de materiales que la forman y la manera de construir con ellos, junto con lo que expresan: textura, color, peso, temperatura al tacto y durabilidad. Un muro de piedra expresa solidez; una fachada de vidrio, ligereza y transparencia; un hormigón sin revestir muestra cómo se construyó.",
        "Los materiales se eligen en relación con el contexto. El clima influye: un muro grueso de piedra o de tierra amortigua los cambios de temperatura y ayuda a conservar el calor; las ventanas pocas y pequeñas pierden menos calor en un clima frío; un alero largo protege los muros de la lluvia; elevar una estructura de madera sobre postes la separa de la humedad del suelo. Los recursos del lugar también cuentan: una región con mucha piedra o madera construye con ella, lo que reduce el transporte y su costo ambiental. Y la época importa: las herramientas y técnicas disponibles permiten ciertos materiales y formas.",
        "Una obra no es mejor por usar un material más nuevo. Cada solución responde a su clima, sus recursos y sus técnicas. Al analizarla se evita juzgar con las ideas de hoy sin entender su contexto. Las obras de esta clase son inventadas; las explicaciones constructivas son generales y no sirven para construir sin una persona profesional.",
    ],
    vocab=[("materialidad", "materiales de una obra y manera de construir con ellos"), ("hormigón visto", "hormigón sin revestir que deja a la vista su textura"), ("alero", "parte del techo que sobresale de los muros"), ("traslapar", "poner una pieza sobre el borde de otra"), ("material local", "material que se obtiene cerca del lugar de la obra")],
    worked=[
        ("Relacionar material y clima", "¿Por qué un muro de piedra de 100 cm de espesor es coherente con inviernos fríos?", ["Un muro grueso amortigua los cambios de temperatura.", "Ayuda a conservar el calor del interior."], "Porque amortigua la temperatura y conserva el calor"),
        ("Calcular una cantidad", "Un muro típico del Mercado mide 10 m de largo, 3 m de alto y 1 m de espesor. ¿Cuántos m³ de piedra tiene?", ["Volumen = largo × alto × espesor.", "10 × 3 × 1 = 30."], "30 m³"),
    ],
    mistakes=[("Decir que una obra es mejor porque usa un material más moderno.", "Cada obra responde a su clima, sus recursos y su época; moderno no es mejor.", "Analiza qué problema resuelve cada material en su contexto."),
              ("Suponer que lo que aguantó una obra antigua sirve hoy sin revisión.", "La seguridad de una construcción real depende de su cálculo y de la norma vigente.", "Usa este análisis para comprender y deja la construcción real a una persona profesional.")],
    T=[
        ('abc', '¿Qué es la materialidad de una obra?', 'Los materiales usados y la manera de construir con ellos, junto con lo que expresan', 'El precio total de la obra y de los materiales que se compraron', 'El color de su pintura y de los muros que se ven desde afuera', 'La materialidad incluye materiales, técnica y expresión.'),
        ('abc', '{F} ¿Qué material predomina en el Mercado de la Piedra?', 'La piedra', 'La madera', 'El hormigón', 'La ficha describe muros y techo de piedra.'),
        ('abc', '{F} ¿Por qué el Mercado de la Piedra tiene pocas ventanas pequeñas?', 'Pierden menos calor del interior en los inviernos fríos de la región', 'Porque la piedra impide hacer ventanas de otro tamaño', 'Para que entre más luz natural a los puestos', 'Las ventanas pequeñas y pocas conservan el calor; la piedra sí permite ventanas más grandes y la luz no es el objetivo.'),
        ('abc', '{F} ¿Por qué la Casa de Tablas se eleva sobre postes?', 'Para separar la madera de la humedad del suelo', 'Para que se vea más alta y destaque entre las otras obras del bosque', 'Para ahorrar tablas en los muros y el piso de la casa', 'En un bosque lluvioso, separar la madera del suelo ayuda a protegerla.'),
        ('=', '{F} Como regla de ejemplo, una rampa suave sube 1 cm por cada 12 cm de largo. Para salvar la altura de 50 cm de los postes, ¿cuántos cm de largo tendría la rampa? (La pendiente real la fija la norma vigente.)', '50*12', 'Se multiplica la altura por 12, según la regla de ejemplo.', ' cm'),
        ('abc', '{F} ¿Qué función cumple el alero largo de la Casa de Tablas?', 'Protege los muros de la lluvia', 'Hace que el techo sea plano', 'Aumenta la humedad del suelo', 'El alero sobresale del muro y evita que el agua lo moje.'),
        ('abc', '{F} ¿Qué expresa el hormigón visto de la Biblioteca?', 'Muestra el proceso de construcción, con las huellas del molde', 'Imita la textura de la madera y esconde las huellas del molde', 'Oculta cómo se construyó, porque la superficie queda lisa y pulida', 'Al no revestirse, deja ver las huellas de las tablas del molde.'),
        ('=', '{F} Otro muro del Mercado mide 8 m de largo, 3 m de alto y 1 m de espesor. ¿Cuántos m³ de piedra tiene?', '8*3*1', 'El volumen es largo por alto por espesor.', ' m³'),
        ('abc', 'Una región con mucha piedra construye con ella. ¿Qué ventaja ambiental general tiene usar un material local?', 'Reduce el transporte y la energía asociada a traerlo de lejos', 'Elimina cualquier impacto ambiental, porque la piedra es un material natural', 'Hace que la obra dure para siempre, porque la piedra no se desgasta', 'El material local acorta recorridos, aunque no elimina todo impacto.'),
        ('abc', '{F} Alguien dice: «la Biblioteca de Hormigón es mejor porque es más moderna». ¿Qué respuesta es más completa?', 'Cada obra responde a su clima, recursos y técnicas; ser moderna no la hace mejor, solo usa otros materiales', 'Tiene razón: lo moderno siempre es mejor, porque incorpora los avances de la técnica', 'Tiene razón, porque el hormigón dura más que cualquier otro material de construcción', 'La calidad de una obra se evalúa en relación con su contexto y su función.'),
        ('abc', '{F} ¿Qué relación entre clima y forma se observa en la Casa de Tablas?', 'Techo de dos aguas con alero largo, útil con lluvias frecuentes', 'Muros de 100 cm de piedra, útiles para conservar el calor del frío', 'Ventanas pequeñas y pocas, para conservar el calor del interior', 'Esas decisiones corresponden a la Casa de Tablas y a su clima lluvioso.'),
        ('abc', '{F} Un equipo propone construir hoy la Casa de Tablas con hormigón «para que dure más». ¿Qué análisis es más completo?', 'Evaluar clima, costo, impacto ambiental y mantención, y si cambia la expresión; la parte estructural la revisa una persona profesional', 'Es mejor siempre, porque el hormigón es más resistente y no necesita mantención', 'Es peor siempre, porque la madera es natural y el hormigón daña cualquier paisaje', 'La decisión pesa varios criterios y la seguridad exige una persona profesional.'),
        ('abc', '¿Qué relación entre la época y la materialidad se puede afirmar sin riesgo?', 'Las técnicas y herramientas disponibles en cada época influyen en los materiales y formas posibles', 'Cada época usa solo un material y lo repite en todas las obras de su tiempo', 'La época no influye en cómo se construye, porque los materiales son siempre los mismos', 'La disponibilidad de técnicas condiciona qué se puede construir.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «El Mercado de la Piedra usa piedra del lugar en muros de 1 m de espesor, coherentes con inviernos fríos, y pocas ventanas pequeñas para conservar el calor; expresa solidez». ¿Qué hace bien?', 'Relaciona material, clima, recurso local y expresión con datos de la ficha', 'Dice que es mejor que las otras obras por ser antigua', 'Opina que le gusta la piedra', 'Une materialidad, contexto y expresión con evidencia.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un material local?", "Uno que se obtiene cerca del lugar de la obra", "Reduce el transporte y su costo ambiental."),
        ("¿Para qué sirve un alero largo?", "Para proteger los muros de la lluvia", "Sobresale del muro y desvía el agua."),
        ("¿Por qué no se dice que una obra es mejor por ser más nueva?", "Porque cada obra responde a su propio contexto, recursos y técnicas", "La calidad se evalúa en relación con su contexto."),
    ],
    op=("Obra 7 (inventada): «Casa de Barro», de una región ficticia de clima seco con grandes cambios de temperatura entre el día y la noche, época A (de ejemplo): muros de tierra y paja de 40 cm de espesor, pocas ventanas pequeñas, techo plano de tierra sobre ramas y un patio interior con un árbol. Escribe tres relaciones entre material, clima y función, una ventaja ambiental general y una razón por la que no debe construirse hoy sin una persona profesional.",
        "Relación 1: muros gruesos de tierra amortiguan los cambios de temperatura del día y la noche. Relación 2: ventanas pequeñas reducen la entrada de calor al mediodía. Relación 3: el patio interior con árbol da sombra y aire más fresco. Ventaja ambiental: la tierra es un material local. Razón: una persona profesional revisa la seguridad estructural y la norma vigente.",
        ["relaciona material, clima y función con evidencia", "nombra una ventaja ambiental general", "reconoce el límite de la construcción real"],
        ["hoja con tres relaciones, una ventaja y un límite"],
        ["juzgar por antigüedad", "inventar datos de la obra", "afirmar que se puede construir sin revisión profesional"],
        "Pregunta: «¿qué dato de la ficha apoya esta relación?». Si no hay dato, pídele que lo busque."),
    reinforce="Mira una pared exterior de tu casa o escuela y anota de qué material es, cómo se siente al tacto y qué problema del clima ayuda a resolver.",
    extend="Explica por qué una obra antigua puede ser muy sustentable en su lugar y no serlo en otro.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 17 (obras de ejemplo, inventadas). "
     "Obra 8: «Templo del Sol», de una cultura ficticia, época A (de ejemplo): planta cuadrada de 12 m por lado, orientada a los cuatro puntos cardinales; escalinata central de 9 escalones de 18 cm de alto cada uno, que sube a una plataforma; un círculo dorado grabado en el piso del centro; colores ocre y rojo. En esa cultura ficticia el círculo representa el sol y los nueve escalones representan nueve ciclos de siembra (símbolos inventados para este ejercicio). "
     "Obra 9: «Silla Onda», pieza de diseño de mobiliario, época C (de ejemplo): una sola lámina curva de madera laminada, sin patas visibles, sin ornamentos y en color natural; la curva continua sugiere movimiento. "
     "Obra 10: «Reloj Cuadrado», objeto de diseño, época B (de ejemplo): esfera cuadrada con números grandes y ornamentos florales en las esquinas.")
build(
    O4, 3, F,
    use="Aprenderé a analizar el lenguaje de una obra (línea, forma, ritmo, ornamento) y sus elementos simbólicos, interpretándolos con evidencia y sin inventar significados.",
    prior=["Sé describir una obra con rasgos formales.", "Sé relacionar materiales con contexto.", "Sé distinguir una interpretación de una descripción."],
    explain=[
        "El lenguaje de una pieza de diseño o una obra de arquitectura es la manera en que usa los elementos formales: línea recta o curva, formas geométricas u orgánicas, ritmo, simetría, color, ornamento (decoración añadida) o ausencia de él. Se habla del tratamiento del lenguaje: una obra puede ser austera, con pocos elementos, o ornamentada, con mucha decoración; puede ser geométrica o de formas fluidas.",
        "Un elemento simbólico es un elemento que representa una idea dentro de una cultura o un contexto, como un círculo que representa el sol en la cultura ficticia de este cuaderno. Los símbolos dependen del contexto: un mismo círculo o un mismo color puede significar cosas distintas en otro lugar. Por eso se interpreta solo con evidencia de la fuente y nunca se inventan ni se suponen significados. Un elemento puede tener a la vez una función práctica (la escalinata sirve para subir) y una función simbólica (sus escalones representan ciclos).",
        "Cuando se analizan obras de culturas y pueblos reales, en especial de pueblos originarios, se consultan fuentes confiables y a representantes o educadores tradicionales, y se evita inventar significados. En este cuaderno todos los símbolos son inventados para practicar el método.",
    ],
    vocab=[("lenguaje de una obra", "manera de usar línea, forma, ritmo, color y ornamento"), ("ornamento", "decoración añadida a una obra"), ("austero", "con pocos elementos y sin decoración"), ("elemento simbólico", "elemento que representa una idea dentro de un contexto"), ("interpretar", "proponer qué significa o sugiere algo, apoyándose en evidencia")],
    worked=[
        ("Leer un símbolo con la ficha", "En la cultura ficticia del Templo, ¿qué representan los nueve escalones?", ["La ficha dice que representan nueve ciclos de siembra.", "Ese significado es de esa cultura ficticia, no universal."], "Nueve ciclos de siembra, en esa cultura ficticia"),
        ("Calcular una medida", "¿Cuántos cm se sube al llegar al cuarto escalón de la escalinata, si cada escalón mide 18 cm?", ["Se multiplican los escalones subidos por su altura.", "4 × 18 = 72."], "72 cm"),
    ],
    mistakes=[("Afirmar que un color o una forma significan siempre lo mismo en todas las culturas.", "Los símbolos dependen del contexto y de la fuente.", "Interpreta solo con la evidencia de la ficha o de una fuente confiable."),
              ("Inventar un significado para una obra de un pueblo real.", "Se falsea su cultura y se la ofende.", "Consulta fuentes confiables y a representantes o educadores tradicionales.")],
    T=[
        ('abc', '¿Qué es un elemento simbólico en una obra?', 'Un elemento que representa una idea dentro de una cultura o contexto', 'Un adorno añadido a la obra, sin ningún significado dentro de su contexto', 'Cualquier elemento caro o de material poco común dentro de la obra', 'Un símbolo representa una idea, y su significado depende del contexto.'),
        ('abc', '{F} En la cultura ficticia del Templo, ¿qué representa el círculo dorado?', 'El sol', 'Nueve ciclos de siembra', 'Los cuatro puntos cardinales', 'La ficha dice que el círculo representa el sol y los escalones los ciclos.'),
        ('=', '{F} Cada escalón de la escalinata mide 18 cm de alto. ¿Cuántos centímetros sube en total?', '9*18', 'Se multiplican los 9 escalones por su altura.', ' cm'),
        ('abc', '{F} ¿Qué rasgo del lenguaje muestra la Silla Onda?', 'Una curva continua, sin ornamentos, de aspecto orgánico y austero', 'Ornamentos florales en las esquinas y líneas rectas que forman cuadrados', 'Una planta cuadrada orientada a puntos cardinales, con una escalinata central', 'La ficha describe una sola lámina curva, sin ornamentos.'),
        ('abc', '{F} ¿Cuál de las piezas de la ficha es ornamentada?', 'El Reloj Cuadrado, por los adornos florales en las esquinas', 'La Silla Onda, por su curva continua y su color natural', 'Ninguna, porque ninguna de las tres piezas tiene decoración añadida', 'El reloj es la única pieza con ornamentos añadidos.'),
        ('abc', '{F} ¿Qué ejemplo reúne función práctica y simbólica en el Templo?', 'La escalinata: sirve para subir y sus nueve escalones representan ciclos de siembra', 'El color ocre y el rojo: sirven para subir y representan ciclos de siembra', 'El círculo dorado: sirve para subir a la plataforma y representa el sol', 'La escalinata cumple las dos funciones según la ficha.'),
        ('abc', '{F} Un estudiante afirma: «el círculo significa el sol en todas las culturas». ¿Qué corrección es correcta?', 'Los símbolos dependen del contexto: aquí significa sol en una cultura ficticia, y en otras puede significar otra cosa', 'Tiene razón, porque el círculo es una forma que en todas partes representa lo mismo', 'Los símbolos no existen en arquitectura, solo en el arte de pintores y escultores', 'El significado del símbolo depende de la cultura que lo usa.'),
        ('=', '{F} La planta del Templo es cuadrada de 12 m por lado. ¿Cuántos m² tiene?', '12*12', 'El área de un cuadrado es lado por lado.', ' m²'),
        ('abc', '{F} ¿Cuál de las piezas tiene el tratamiento más austero?', 'La Silla Onda, que no tiene ornamentos ni patas visibles', 'El Reloj Cuadrado, por sus números grandes y las flores de las esquinas', 'El Templo del Sol, por su círculo dorado y los colores ocre y rojo', 'La silla se reduce a una curva continua, sin decoración.'),
        ('abc', '{F} Alguien interpreta el color rojo del Templo como «violencia». ¿Qué problema tiene esa interpretación?', 'No se apoya en evidencia de la ficha, y el significado de un color depende de la cultura', 'Ninguno, porque el rojo significa violencia en todas las culturas y épocas', 'Que el rojo no se puede interpretar jamás, ni siquiera con una fuente que lo explique', 'La ficha no da ese dato, y suponerlo es inventar un significado.'),
        ('abc', 'Quieres analizar símbolos de una obra de un pueblo originario real. ¿Qué corresponde?', 'Consultar fuentes confiables y a representantes o educadores tradicionales, y no inventar significados', 'Suponer los significados por parecido con símbolos de otras culturas ya conocidas', 'Elegir el significado más llamativo para que la presentación sea más interesante', 'Los significados de una cultura real se aprenden de quienes la conocen.'),
        ('abc', '{F} ¿Qué análisis relaciona lenguaje y símbolo del Templo con evidencia?', 'La planta cuadrada orientada a los puntos cardinales y el círculo central ordenan el espacio en torno al sol, según la cultura ficticia', 'Es lindo porque el dorado hace que se vea importante y rico', 'No tiene ningún significado, porque los símbolos solo existen en las obras antiguas', 'Une rasgos formales de la ficha con el símbolo que la ficha explica.'),
        ('abc', '¿Qué diferencia un símbolo de un simple adorno?', 'El símbolo representa una idea reconocida en un contexto; el adorno decora sin ese significado', 'El símbolo siempre es más grande y más costoso que el adorno', 'No hay diferencia: todo adorno es un símbolo mientras alguien lo mire', 'El símbolo comunica una idea compartida en una cultura; el adorno solo decora.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «El Templo tiene planta cuadrada orientada a los cuatro puntos cardinales y un círculo dorado en el centro; según la ficha, el círculo representa el sol en esa cultura ficticia». ¿Qué hace bien?', 'Interpreta con evidencia de la ficha y aclara el contexto del símbolo', 'Afirma que el círculo siempre es sol', 'Inventa un significado para el color', 'La interpretación se apoya en rasgos formales y en el dato de la ficha.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué significa que una obra sea ornamentada?", "Que tiene decoración añadida", "Lo contrario es una obra austera."),
        ("¿Por qué se interpreta un símbolo solo con evidencia?", "Porque su significado depende del contexto y no se debe inventar", "Así se respeta la cultura que lo creó."),
        ("¿Qué dos funciones puede tener un mismo elemento?", "Una práctica y una simbólica", "Por ejemplo, subir y representar ciclos."),
    ],
    op=("Obra 11 (inventada): «Puerta de la Luna», de una cultura ficticia, época A (de ejemplo): un arco de piedra de 3 m de alto con una media luna tallada arriba y tres franjas de color azul, blanco y negro. En esa cultura ficticia la media luna representa el paso de la noche al día. Escribe una descripción formal de dos líneas, el tratamiento del lenguaje (austero u ornamentado, con una razón), una interpretación del símbolo usando solo lo que dice el texto y una frase que diga qué no sabrías sin una fuente confiable.",
        "Descripción: arco de piedra de 3 m con media luna tallada y tres franjas de color. Lenguaje: moderadamente ornamentado, por la talla y las franjas. Interpretación: la media luna, que representa el paso de la noche al día, marca la entrada como un cambio de un estado a otro. No sabría qué significan las tres franjas de color, porque el texto no lo dice.",
        ["describe con rasgos observables", "interpreta solo con la evidencia dada", "reconoce lo que no se puede afirmar"],
        ["hoja con descripción, lenguaje, interpretación y límite"],
        ["inventar significados", "no describir antes de interpretar", "no declarar lo que falta saber"],
        "Pregunta: «¿en qué parte del texto está ese significado?». Si no está, pídele que lo marque como suposición."),
    reinforce="Elige un logotipo o un pictograma de tu entorno y anota qué idea representa, qué forma usa y si tiene ornamentos.",
    extend="Explica por qué dos culturas pueden usar el mismo color con significados distintos.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 18 (obras de ejemplo, inventadas). "
     "Obra 12: «Mercado Cubierto», de una ciudad ficticia con lluvias, época B (de ejemplo): nave central de 24 m de largo por 12 m de ancho; techo alto con ventilación en lo alto; pasillos de 3 m de ancho entre los puestos; ocho entradas anchas sin escalones, repartidas por igual en los dos lados largos. Contexto: se construyó cuando las ferias al aire libre se suspendían por la lluvia. "
     "Obra 13: «Taburete Apilable», objeto de diseño, época C (de ejemplo): cuatro patas, asiento de 40 cm de alto, se apila hasta 6 unidades; plástico reciclado; cada taburete que se agrega a la pila suma 8 cm a su altura. Contexto: salas de reuniones que cambian su disposición rápido. "
     "Obra 14: «Palacete Aislado», vivienda de lujo ficticia, época B (de ejemplo): salones muy decorados, un solo acceso con 14 escalones y ventanas altas. Contexto: una familia que quería mostrar prestigio.")
build(
    O4, 4, F,
    use="Aprenderé a relacionar una obra con su contexto (clima, sociedad, economía, técnica) y a evaluar su funcionalidad, incluida la accesibilidad, sin descalificar épocas ni justificar exclusiones.",
    prior=["Sé analizar materialidad y lenguaje.", "Sé calcular áreas.", "Sé que una obra sirve a ciertos usos y personas."],
    explain=[
        "El contexto de una obra son las circunstancias que ayudan a explicarla: el clima, la geografía, la cultura, la economía, la técnica disponible y las necesidades de las personas de su época. Una obra se entiende mejor al preguntar para qué se hizo, para quién, dónde y cuándo, y qué decisiones formales responden a eso.",
        "La funcionalidad es qué tan bien sirve una obra a sus usos: circulación, confort (luz, ventilación, temperatura), seguridad, accesibilidad, mantención y flexibilidad. Una obra puede tener funciones prácticas, simbólicas y sociales a la vez. Para evaluarla se pregunta: ¿para quién sirve bien, para quién no y por qué? Una obra puede ser funcional para un grupo y excluyente para otro, como una entrada con muchos escalones.",
        "Entender el contexto de una obra antigua no obliga a justificar sus exclusiones: se explica por qué se hizo así y, al mismo tiempo, se reconoce hoy que la accesibilidad universal es un criterio importante. Si una obra de valor se adapta para dar acceso, se hace de forma respetuosa y con una persona profesional. Las obras de esta clase son inventadas.",
    ],
    vocab=[("contexto", "circunstancias que explican una obra"), ("funcionalidad", "qué tan bien una obra sirve a sus usos"), ("circulación", "recorridos de las personas dentro de una obra"), ("flexibilidad", "capacidad de cambiar de uso o de disposición"), ("exclusión", "dejar a personas fuera de poder usar algo")],
    worked=[
        ("Calcular la superficie", "Con la ficha, ¿cuántos m² tiene la nave central del Mercado?", ["Mide 24 m por 12 m.", "24 × 12 = 288."], "288 m²"),
        ("Leer una función", "¿Qué aporta a la funcionalidad del Mercado su techo alto con ventilación en lo alto?", ["La ventilación forma parte del confort de un espacio.", "Renueva el aire de la nave, donde circula mucha gente."], "Mejora el confort con aire renovado"),
    ],
    mistakes=[("Decir que una obra antigua es mala porque no cumple los criterios de hoy.", "No se comprende el contexto en que se hizo.", "Explica el contexto y evalúa por separado la funcionalidad actual."),
              ("Justificar la exclusión porque «así se hacía entonces».", "Entender una época no vuelve inclusiva una obra que excluye.", "Reconoce la exclusión y propone una adaptación respetuosa.")],
    T=[
        ('abc', '¿Qué es el contexto de una obra de diseño o arquitectura?', 'Las circunstancias que ayudan a explicarla: clima, cultura, economía, técnica y necesidades', 'El nombre de quien la diseñó y el año en que se terminó', 'El material más barato que había en la época de la obra', 'El contexto explica por qué la obra se hizo de cierta manera.'),
        ('abc', '{F} ¿Qué necesidad del contexto responde el Mercado Cubierto?', 'Poder vender aunque llueva', 'Mostrar prestigio', 'Cambiar rápido la disposición de una sala', 'La ficha dice que se construyó porque las ferias al aire libre se suspendían por lluvia.'),
        ('=', '{F} Un pasillo recto de la nave mide 3 m de ancho y 24 m de largo. ¿Cuántos m² tiene?', '3*24', 'El área es largo por ancho.', ' m²'),
        ('abc', '{F} ¿Qué decisión del Mercado favorece la accesibilidad?', 'Ocho entradas anchas sin escalones', 'El techo alto con ventilación en lo alto', 'Los puestos de tamaño y decoración variados', 'Las entradas anchas y sin escalones permiten el acceso a más personas.'),
        ('=', '{F} ¿Cuántos centímetros mide una pila de 6 taburetes (el primero mide 40 cm y cada taburete extra suma 8 cm)?', '40+5*8', 'Se suma al primero la altura de los 5 taburetes agregados.', ' cm'),
        ('abc', '{F} ¿Qué función práctica tiene que el taburete sea apilable?', 'Ahorra espacio al guardarlo y permite cambiar rápido la disposición de la sala', 'Lo hace más caro, pero más estable que un taburete de patas fijas', 'Muestra el prestigio de quien lo usa frente a las demás personas', 'La ficha explica que las salas cambian su disposición con frecuencia.'),
        ('abc', '{F} ¿Por qué el Palacete tiene problemas de funcionalidad para algunas personas?', 'Su único acceso tiene 14 escalones y excluye a quienes no pueden subirlos', 'Tiene demasiados salones y su recorrido interior es muy largo', 'Está muy decorado y eso dificulta limpiar y mantener los salones', 'Un solo acceso con escalones impide el ingreso a varias personas.'),
        ('abc', '{F} ¿Qué contexto explica la decoración del Palacete?', 'Una familia que quería mostrar prestigio', 'La falta de materiales de construcción en la zona', 'Las lluvias frecuentes de la ciudad ficticia', 'La ficha asocia los salones decorados con el deseo de mostrar prestigio.'),
        ('=', '{F} Las ocho entradas del Mercado se reparten por igual en los dos lados largos. ¿Cuántas hay en cada lado?', '8//2', 'Se divide el total de entradas entre los dos lados.', ' entradas'),
        ('abc', '{F} Alguien dice: «el Palacete es un fracaso porque no es accesible». ¿Qué respuesta es mejor?', 'Explicar el contexto sin justificar la exclusión: hoy se evalúa su falta de accesibilidad y se piensa cómo adaptarla', 'No se puede criticar nada de las obras de épocas pasadas, porque se hicieron con otros valores', 'Tiene razón, porque una obra que excluye a alguien es un fracaso en cualquier época', 'Se entiende el contexto y a la vez se reconoce que la accesibilidad es hoy un criterio.'),
        ('abc', '{F} ¿Qué adaptación respetuosa conviene para dar acceso al Palacete?', 'Agregar una ruta accesible, como una rampa o un ascensor, integrada con cuidado y diseñada por una persona profesional', 'Construir una entrada trasera separada, solo para quien no puede subir los escalones', 'Dejar los escalones y ofrecer ayuda siempre que alguien la pida en la entrada', 'La adaptación debe dar autonomía y cuidar el valor de la obra.'),
        ('abc', '{F} ¿Qué comparación relaciona mejor contexto y funcionalidad de las tres obras?', 'Cada una responde a necesidades distintas y su funcionalidad se evalúa según su propósito y quién queda incluido', 'Solo la más grande es funcional, porque tiene más espacio para circular', 'Solo la más antigua es funcional, porque resistió el paso del tiempo', 'La funcionalidad se evalúa con el propósito y la inclusión, no por tamaño o edad.'),
        ('abc', '¿Qué pregunta ayuda a analizar la funcionalidad de una obra?', '¿Para quién sirve bien, para quién no y por qué?', '¿Cuántos años tiene la obra y quién la diseñó primero?', '¿Qué tan famosa es la obra y cuánto cuesta visitarla?', 'Esa pregunta pone en el centro el uso y la inclusión.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «El Mercado Cubierto responde a la lluvia con una nave techada de 288 m², ventilación alta y entradas sin escalones; es funcional para vender y accesible a más personas». ¿Qué hace bien?', 'Relaciona el contexto con decisiones y evalúa función y accesibilidad con datos', 'Opina que es el mejor mercado del mundo', 'Compara con obras que no están en la ficha', 'Usa el contexto y datos de la ficha para evaluar la función.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es la funcionalidad de una obra?", "Qué tan bien sirve a sus usos y a las personas", "Incluye circulación, confort, seguridad y accesibilidad."),
        ("¿Qué pregunta ayuda a evaluar la funcionalidad?", "¿Para quién sirve bien, para quién no y por qué?", "Muestra quién queda incluido y quién no."),
        ("¿Entender el contexto justifica una exclusión?", "No: se explica por qué se hizo así y se reconoce que excluye", "Contexto y accesibilidad se analizan por separado."),
    ],
    op=("Obra 15 (inventada): «Biblioteca de la Plaza», de una ciudad ficticia, época B (de ejemplo): sala de lectura de 20 m por 10 m con ventanas altas, mesas fijas de 90 cm de alto, dos puertas con un escalón de 20 cm y un baño en el segundo piso al que se sube solo por escalera. Contexto: se hizo cuando se valoraba el silencio y el orden. Escribe dos aciertos funcionales, dos problemas de accesibilidad, el contexto que los explica sin justificarlos y una adaptación respetuosa.",
        "Aciertos: ventanas altas que dan luz y sala amplia de 200 m². Problemas: escalón de 20 cm en las dos puertas y baño sin acceso para quien no sube escaleras. Contexto: se valoraba el silencio y el orden, pero eso no justifica la exclusión. Adaptación: una rampa en una puerta y un baño accesible en el primer piso, diseñados por una persona profesional.",
        ["relaciona contexto y decisiones", "identifica problemas de accesibilidad con evidencia", "propone una adaptación respetuosa"],
        ["hoja con aciertos, problemas, contexto y adaptación"],
        ["juzgar la época como inferior", "justificar la exclusión", "olvidar la evidencia"],
        "Pregunta: «¿quién queda fuera de poder usar esto?». Si no responde, pídele revisar los accesos."),
    reinforce="Recorre un lugar de tu barrio o escuela y anota una decisión que facilite el acceso y una que lo dificulte.",
    extend="Explica por qué una obra puede ser muy funcional para un grupo de personas y poco para otro.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 19 (análisis para revisar, inventado). Se comparan dos obras ficticias. "
     "Obra 16: «Pabellón de Bambú», de una región cálida ficticia, época A (de ejemplo): estructura de cañas atadas, techo con alero largo, paredes de esteras que se abren para ventilar, planta circular de 10 m de diámetro. "
     "Obra 17: «Edificio Prisma», de una ciudad fría ficticia, época C (de ejemplo): 6 pisos de 3 m de altura cada uno, muros de hormigón y vidrio doble, planta triangular, calefacción central, una escalera y un ascensor. "
     "Texto de una estudiante: «El Pabellón es mejor porque es más natural. El Edificio Prisma es feo porque es gris. Se ve que en la época A la gente era menos inteligente». "
     "Pauta para revisar un análisis: P1 describe con rasgos observables; P2 relaciona material, clima y función; P3 usa evidencia y no estereotipos; P4 separa descripción, interpretación y juicio.")
build(
    O4, 5, F,
    use="Aprenderé a comparar obras de épocas y procedencias distintas con criterios comunes y a revisar un análisis ajeno con una pauta, corrigiendo juicios sin evidencia y prejuicios.",
    prior=["Sé analizar materialidad, lenguaje, símbolos y función.", "Sé usar una pauta.", "Sé dar un comentario respetuoso."],
    explain=[
        "Comparar dos obras es analizarlas con los mismos criterios: materialidad, lenguaje, elementos simbólicos, contexto y funcionalidad. Una tabla con los criterios en las filas y las obras en las columnas ayuda a no comparar manzanas con peras. La comparación no busca decir cuál obra es mejor en general, sino cómo cada una responde a su clima, sus recursos, su época y sus usuarios.",
        "Para revisar un análisis, sea propio o ajeno, se usa una pauta con criterios observables. Se buscan tres defectos frecuentes: los juicios sin evidencia («es feo porque es gris»), las comparaciones injustas que valoran una obra con criterios que solo calzan con otra, y los prejuicios sobre las personas o las épocas («la gente era menos inteligente»). Un prejuicio no se corrige con otro: se reemplaza por una explicación basada en el contexto, como las técnicas disponibles y las necesidades de esa época.",
        "La revisión es respetuosa: señala qué cumple la pauta, qué punto falla con una cita del texto y propone cómo mejorarlo. Las obras de esta clase son inventadas.",
    ],
    vocab=[("tabla comparativa", "tabla con criterios en las filas y obras en las columnas"), ("criterio común", "criterio que se aplica igual a todas las obras comparadas"), ("prejuicio", "juicio previo sin evidencia sobre personas o grupos"), ("anacronismo", "juzgar el pasado con ideas o técnicas del presente sin contexto"), ("revisión", "lectura crítica de un análisis para mejorarlo")],
    worked=[
        ("Detectar un juicio sin evidencia", "¿Por qué «el Edificio Prisma es feo porque es gris» no es un análisis?", ["«Feo» es una opinión y el gris es solo un dato de color.", "No dice cómo el color se relaciona con el clima o con la función."], "Es un juicio sin evidencia ni relación con el contexto"),
        ("Calcular una medida", "Si al Edificio Prisma se le agregaran 2 pisos más de 3 m, ¿cuántos metros de alto tendría?", ["Pasaría de 6 a 8 pisos de 3 m.", "8 × 3 = 24."], "24 m"),
    ],
    mistakes=[("Corregir un prejuicio con otro, por ejemplo «la época A era mejor porque era natural».", "Se reemplaza un juicio sin evidencia por otro.", "Explica ambas obras por su contexto, sus materiales y sus funciones."),
              ("Comparar una obra con criterios que solo calzan con la otra.", "La comparación resulta injusta y no informa.", "Usa los mismos criterios para las dos obras.")],
    T=[
        ('abc', '¿Qué hace una comparación justa de dos obras?', 'Usa los mismos criterios para ambas, como materialidad, lenguaje, contexto y función', 'Usa criterios distintos para cada una, ajustados a lo que más luce en ella', 'Compara solo cuál es más grande y cuál tiene más pisos o más metros cuadrados', 'Los criterios comunes permiten ver cómo responde cada obra a su contexto.'),
        ('abc', '{F} ¿Cuál afirmación es un prejuicio sobre las personas de una época?', '«En la época A la gente era menos inteligente»', '«El Pabellón es mejor porque es más natural»', '«El Edificio Prisma es feo porque es gris»', 'Solo la primera juzga a las personas de una época sin evidencia.'),
        ('=', '{F} ¿Cuántos metros de alto tiene el Edificio Prisma (6 pisos de 3 m)?', '6*3', 'Se multiplican los pisos por su altura.', ' m'),
        ('abc', '{F} En la frase «el Edificio Prisma es feo porque es gris», ¿qué punto de la pauta cumple en parte?', 'P1: nombra un rasgo observable (el color), aunque no basta para un análisis', 'P2: relaciona el material con el clima y la función del edificio', 'P3: usa evidencia suficiente para sostener que el edificio es feo', 'El color gris es observable (P1), pero la frase no relaciona ni apoya su juicio con evidencia.'),
        ('abc', '{F} ¿Qué relación entre material, clima y función se observa en el Pabellón?', 'Las paredes de esteras que se abren y el alero largo ventilan y protegen en un clima cálido', 'La calefacción central y los muros de hormigón, propios de un clima frío', 'El vidrio doble, pensado para que no entre la lluvia a través de las ventanas', 'Esas decisiones del Pabellón corresponden a su clima cálido.'),
        ('abc', '{F} ¿Qué relación entre material, clima y función se observa en el Edificio Prisma?', 'Los muros de hormigón, el vidrio doble y la calefacción central son coherentes con un clima frío', 'Las esteras abiertas para ventilar y el alero largo que protege los muros', 'La estructura de cañas atadas, liviana y fácil de reparar en un clima cálido', 'Las decisiones del Prisma responden a un clima frío.'),
        ('abc', '{F} ¿Cómo se reescribe «el Pabellón es mejor porque es más natural» con rasgos observables?', 'El Pabellón usa cañas y esteras, materiales vegetales, y se ventila abriendo sus paredes', 'El Pabellón es lindo porque se ve cálido y tiene un aspecto natural', 'El Pabellón es mejor que todos los edificios modernos de la ciudad fría', 'Reemplaza la opinión por materiales y decisiones que se pueden comprobar.'),
        ('abc', '{F} ¿Con qué frase se reemplaza el prejuicio sobre la época A?', 'En la época A se construía con las técnicas y materiales disponibles, adecuados a su clima y necesidades', 'En la época A se construía peor, porque todavía no existían las técnicas de hoy', 'En la época A no se construía con criterio, sino por costumbre y sin pensar en el clima', 'La explicación se basa en técnicas y contexto, no en juicios sobre las personas.'),
        ('abc', '{F} ¿Qué tabla comparativa es más útil?', 'Filas: materialidad, lenguaje, símbolo, contexto y función; columnas: Pabellón y Prisma', 'Filas: cuál gusta más a cada persona; columnas: edad y curso de quien opina', 'Una sola celda con una nota general para cada obra, sin explicar los criterios', 'Los criterios comunes permiten comparar con justicia.'),
        ('abc', '{F} Alguien dice: «la comparación demuestra que las obras modernas son mejores porque tienen calefacción». ¿Qué responde mejor?', 'La calefacción responde al frío y la ventilación al calor: cada obra se adecúa a su contexto', 'Tiene razón, porque la calefacción siempre mejora el confort en cualquier clima', 'No se pueden comparar obras de épocas y climas distintos, porque son de mundos diferentes', 'Cada obra se evalúa según el clima y la función que enfrenta.'),
        ('abc', '{F} ¿Qué rasgo del Pabellón puede ser sustentable según la ficha?', 'Usa materiales vegetales y ventilación natural al abrir las paredes', 'Usa calefacción central, que mantiene el confort sin depender del clima', 'Usa vidrio doble, que permite mantener el calor sin gastar energía', 'Los materiales vegetales y la ventilación natural dependen menos de energía.'),
        ('abc', '{F} ¿Cuál es una versión corregida completa del análisis de la estudiante?', 'El Pabellón (cálido) ventila con cañas y esteras y se protege con un alero; el Prisma (frío) usa hormigón, vidrio doble y calefacción; cada uno responde a su contexto', 'El Pabellón es mejor porque es natural y de época antigua, y el Prisma es feo porque es gris y moderno, así que no hay nada que comparar', 'Las dos obras son iguales porque ambas son edificios que sirven para refugiarse y no hay que compararlas', 'Corrige juicios y prejuicios con descripción y relación con el contexto.'),
        ('abc', '¿Qué hace una revisión respetuosa del análisis de un compañero?', 'Señala qué cumple la pauta, qué punto falla con una cita del texto y sugiere cómo mejorarlo', 'Le quita puntos sin explicar por qué, para que aprenda a hacerlo mejor', 'Reescribe su texto completo sin consultarle, para ahorrarle trabajo', 'Una revisión útil describe, cita y orienta sin juzgar a la persona.'),
    ],
    ctx=('abc', 'Una estudiante reescribe: «El Pabellón (época A, clima cálido) usa cañas y esteras para ventilar; el Prisma (época C, clima frío) usa vidrio doble y calefacción central; ambos responden a su contexto». ¿Qué mejora respecto del texto original?', 'Reemplaza los juicios y el prejuicio por descripciones y relaciones con el contexto', 'Mantiene los juicios y agrega adjetivos', 'Elimina la comparación', 'La nueva versión cumple los puntos de la pauta.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un criterio común?", "Un criterio que se aplica igual a todas las obras comparadas", "Evita comparaciones injustas entre las dos obras."),
        ("¿Qué defectos se buscan al revisar un análisis?", "Juicios sin evidencia, comparaciones injustas y prejuicios", "Se corrigen con descripción y contexto."),
        ("¿Cómo se corrige un prejuicio sobre una época?", "Con una explicación basada en su contexto y sus técnicas", "No se reemplaza por otro prejuicio."),
    ],
    op=("Revisa este texto de ejemplo (inventado): «La Casa Tejada es mejor que la Casa Vidriada porque es más antigua y la gente de antes sabía construir mejor». Datos de ejemplo: la Casa Tejada (región lluviosa, época A) tiene techo de dos aguas con tejas y alero largo; la Casa Vidriada (ciudad soleada, época C) tiene una fachada de vidrio con cortinas térmicas y ventilación cruzada. Usa la pauta P1 a P4, identifica el juicio y el prejuicio, y reescribe el análisis comparando las casas con criterios comunes.",
        "Juicio sin evidencia: «es mejor porque es más antigua». Prejuicio: «la gente de antes sabía construir mejor». Reescritura: la Casa Tejada responde a la lluvia con un techo de dos aguas y un alero largo; la Casa Vidriada responde al sol con cortinas térmicas y ventilación cruzada; cada una se adapta a su clima con técnicas de su época.",
        ["identifica el juicio y el prejuicio con una cita", "usa criterios comunes para ambas casas", "reescribe con descripción y contexto"],
        ["hoja con la revisión por pauta y la versión corregida"],
        ["corregir un prejuicio con otro", "comparar con criterios distintos", "no citar el texto"],
        "Pregunta: «¿qué dato de la ficha apoya tu reescritura?». Si no hay dato, pídele que lo agregue."),
    reinforce="Compara dos objetos de tu casa del mismo tipo (por ejemplo, dos sillas) usando tres criterios iguales para ambos.",
    extend="Explica por qué comparar con criterios comunes evita decir que una época es mejor que otra.",
)
