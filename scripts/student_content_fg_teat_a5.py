"""Teatro 3.º y 4.º medio FG: OAC-03 (interpretación teatral para un público específico), clases 4 a 6. Escenas originales e inventadas; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O3 = "FG-TEAT-3y4-OAC-03"

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (tres públicos de ejemplo, inventados). Público 1: 25 estudiantes de 4.º básico, sentados en una alfombra, con unos 15 minutos de atención. "
     "Público 2: 40 personas adultas de una junta de vecinos, sentadas en sillas, dispuestas a escuchar unos 30 minutos. "
     "Público 3: estudiantes de 2.º medio de pie en un patio con ruido de fondo, con unos 10 minutos de atención. La escena es «La lista», sobre esperar un resultado.")
build(
    O3, 4, F,
    use="Aprenderé a considerar un público específico (edad, conocimientos, lugar y tiempo de atención) y a ajustar lenguaje, ritmo, duración, amplitud y voz sin cambiar el propósito de la escena.",
    prior=["Sé que el propósito es lo que se quiere comunicar.", "Sé ajustar amplitud del gesto y proyección al espacio.", "Sé construir un personaje con objetivo y tácticas."],
    explain=[
        "Un público específico es un grupo concreto de personas a quienes va dirigida la función. Para conocerlo se averigua su edad, qué sabe del tema, qué le interesa, dónde estará y cuánto tiempo puede atender. Esta información se obtiene conversando con su docente o con las personas responsables, sin suponer. Cada dato lleva a una decisión: el lenguaje que se usa, el ritmo, la duración, el tamaño de los gestos y la fuerza de la voz.",
        "Adaptar no es cambiar el propósito. Se ajustan los recursos para que el mismo mensaje llegue: con niños de 4.º básico conviene un lenguaje sencillo, acciones muy claras y cambios de ritmo frecuentes; con personas adultas sentadas, un ritmo más pausado y textos algo más largos; en un patio con ruido, gestos amplios, voz proyectada y una escena más breve. Tampoco es simplificar tanto que se subestime al público: se le habla con respeto.",
        "También se cuida lo que corresponde a su edad. Con niños y niñas no se presentan escenas con violencia, gritos intensos ni temas que den miedo; se busca un conflicto que puedan comprender. Si quien presenta nota que alguien del público se angustia o se siente mal, se detiene con calma y se avisa a una persona adulta responsable.",
    ],
    vocab=[("público específico", "grupo concreto de personas al que va dirigida la función"), ("adaptar", "ajustar los recursos para que el mismo propósito llegue a ese público"), ("tiempo de atención", "minutos durante los cuales un público puede seguir una escena"), ("lenguaje", "palabras y modos de decir que se usan en la escena"), ("apropiado a la edad", "contenido que corresponde a la edad y madurez del público")],
    worked=[
        ("Reconocer qué se adapta", "Una escena sobre esperar un resultado se presentará a niños de 4.º básico. El grupo mantiene el propósito. ¿Qué ajusta?", ["Usa palabras sencillas y acciones muy claras.", "Acorta la duración y varía el ritmo para sostener la atención."], "Lenguaje, duración y ritmo; el propósito se mantiene"),
        ("Averiguar sin suponer", "El grupo no sabe qué tema es adecuado para una junta de vecinos. ¿Qué hace?", ["Conversa con la persona responsable de la junta.", "Pregunta por edades, intereses, lugar y tiempo disponible."], "Consultar a la persona responsable"),
    ],
    mistakes=[("Cambiar el propósito de la escena para que sea «más fácil» para el público.", "El mensaje deja de ser el del grupo.", "Mantén el propósito y ajusta lenguaje, ritmo y duración."),
              ("Suponer lo que le gusta a un público sin averiguar.", "Se pueden usar temas o palabras que no corresponden.", "Pregunta a su docente o a las personas responsables.")],
    T=[
        ('abc', '¿Qué es un público específico?', 'Un grupo concreto de personas al que va dirigida la función', 'Cualquier persona que pase por el lugar mientras se presenta', 'El grupo de amigos de quienes actúan en la escena', 'Se define por ser un grupo concreto, con edad, lugar y expectativas conocidas.'),
        ('abc', '{F} ¿Qué público tiene menos tiempo de atención?', 'El público 3, con unos 10 minutos', 'El público 1, con unos 15 minutos', 'El público 2, con unos 30 minutos', 'Los 10 minutos del público 3 son el menor tiempo entre los tres.'),
        ('abc', 'Adaptar una escena a un público significa', 'ajustar lenguaje, ritmo y duración sin cambiar el propósito', 'cambiar el mensaje por otro que le resulte más cómodo al grupo', 'dejar la escena igual para todos los públicos y todos los lugares', 'La adaptación cuida el cómo, no el qué se quiere comunicar.'),
        ('abc', '{F} Para el público 3, en el patio con ruido, ¿qué ajuste conviene?', 'Gestos más amplios, voz proyectada y una escena más breve', 'Gestos pequeños, voz suave y una escena larga con muchos detalles', 'Mantener la misma versión que se hizo para el público 2', 'El ruido y la distancia exigen amplitud, proyección y duración corta.'),
        ('abc', '{F} Para el público 1, de 4.º básico, ¿qué ajuste es adecuado?', 'Lenguaje sencillo, acciones muy claras y cambios de ritmo frecuentes', 'Frases largas y abstractas para que aprendan palabras nuevas de golpe', 'Escenas que den miedo para que se mantengan atentos todo el tiempo', 'Un lenguaje claro y acciones visibles ayudan a niños de esa edad.'),
        ('abc', 'Al adaptar la escena a un público, ¿qué se conserva?', 'El propósito que el grupo quiere comunicar', 'Exactamente las mismas palabras y la misma duración', 'La forma de actuar frente al público anterior', 'El propósito es lo que justifica la escena; lo que cambia son los recursos.'),
        ('=', '{F} El público 2 puede atender 30 minutos. La escena dura 8 minutos y luego habrá un comentario de 10 minutos con el público. ¿Cuántos minutos de esa atención quedan?', '30-8-10', 'Se restan la escena y el comentario al tiempo de atención.', ' minutos'),
        ('abc', 'Un grupo quiere presentar a niños de 4.º básico una escena con una discusión violenta y gritos. ¿Qué conviene?', 'Cambiar el conflicto por uno que comprendan y presentarlo sin violencia ni gritos', 'Mantener la escena igual porque los niños necesitan ver cómo es la realidad y acostumbrarse a ella desde pequeños', 'Presentarla de todos modos, pero con el volumen más bajo', 'El contenido debe ser apropiado a la edad; se cambia el conflicto, no solo el volumen.'),
        ('abc', 'No sabes qué temas interesan a una junta de vecinos. ¿Qué haces?', 'Conversar con la persona responsable y preguntar edades, intereses, lugar y tiempo', 'Suponer lo que les gusta según tu propia edad y tus gustos, y probar con ellos el día de la función', 'Elegir el tema más conocido en las redes y esperar que sirva', 'Averiguar con quien conoce al público evita suponer.'),
        ('abc', 'Un grupo usa jerga de redes con vecinos adultos que no la conocen. ¿Qué ocurre?', 'Parte del público no entiende y se pierde el propósito', 'Todo el público disfruta más porque suena moderno', 'Nada cambia, porque el cuerpo comunica igual', 'Si no se comprenden las palabras, el mensaje no llega al público.'),
        ('abc', 'Un grupo simplifica tanto la escena para niños que cambia lo que quería comunicar. ¿Qué error cometió?', 'Adaptó el propósito en vez de adaptar los recursos', 'Dedicó demasiado tiempo a conocer al público', 'Usó un lenguaje sencillo y gestos claros', 'Se adaptan lenguaje, ritmo y duración; el propósito se mantiene.'),
        ('=', '{F} La escena original dura 12 minutos. Para el público 3 se deja en 4 de cada 6 minutos. ¿Cuántos minutos dura la versión nueva?', '12*4//6', 'Se toma la fracción de la duración original.', ' minutos'),
        ('abc', 'Un grupo debe presentar la misma escena a los públicos 1 y 2 en una misma mañana. ¿Cuál plan es adecuado?', 'Mantener el propósito y ajustar lenguaje, ritmo y duración a cada público', 'Presentar exactamente igual a ambos para no confundirse en la memoria', 'Presentar solo al público 1 y decir que la escena no sirve para adultos', 'Cada público necesita ajustes y ambos reciben el mismo mensaje.'),
    ],
    ctx=('ab', 'Una niña del público parece angustiada y se tapa los oídos durante una escena. ¿Qué conviene hacer?', 'Detener con calma y avisar a una persona adulta responsable del curso', 'Seguir hasta el final para no interrumpir la función', 'La seguridad y el bienestar del público están antes de terminar la escena.'),
    sc=[
        ("En Teatro: ¿qué se averigua para conocer a un público específico?", "Su edad, qué sabe del tema, qué le interesa, dónde estará y cuánto tiempo atiende", "Cada dato lleva a una decisión sobre la escena."),
        ("¿Qué se conserva cuando se adapta una escena a otro público?", "El propósito del grupo", "Solo cambian los recursos, no el mensaje."),
        ("Si alguien del público se angustia durante la función, ¿qué haces?", "Detengo con calma y aviso a una persona adulta responsable", "El bienestar del público va primero."),
    ],
    op=("Escoge un público de ejemplo: niños de 4.º básico, vecinos adultos o estudiantes de 2.º medio en un patio. Escribe qué averiguarías sobre él (tres datos) y cómo adaptarías el lenguaje, el ritmo, la duración y la voz de una escena de tu elección, sin cambiar su propósito.",
        "Público: niños de 4.º básico; averiguo edad, tiempo de atención y qué saben del tema; uso palabras sencillas, ritmo con cambios, escena de 6 minutos y voz clara; el propósito (esperar con paciencia) no cambia.",
        ["tres datos del público", "ajusta lenguaje, ritmo, duración y voz", "mantiene el propósito", "contenido apropiado a la edad"],
        ["ficha de adaptación"],
        ["cambiar el propósito", "suponer sin averiguar"],
        "Pregunta: «¿qué se quiere comunicar en las dos versiones?». Debe ser lo mismo."),
    reinforce="Elige una escena inventada y escribe cómo cambiaría su primera frase para niños pequeños y para personas adultas.",
    extend="Explica la diferencia entre adaptar una escena a un público y subestimar a ese público.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (ensayo general de ejemplo, inventado). Pauta de interpretación, con puntaje de 1 a 4: voz audible, intención clara, escucha entre intérpretes, uso del espacio y adecuación al público. "
     "Resultados de «La lista»: voz audible 3, intención clara 3, escucha entre intérpretes 4, uso del espacio 3, adecuación al público 1. "
     "Observaciones del grupo observador: «Las frases largas del comienzo no se entendieron para niños de 4.º básico. A los 6 minutos el público ejemplo empezó a moverse.»")
build(
    O3, 5, F,
    use="Aprenderé a hacer un ensayo general, a evaluarlo con una pauta de interpretación y a decidir qué ajustes hacer, uno por vez, para que la escena funcione con su público específico.",
    prior=["Sé dar retroalimentación descriptiva.", "Sé adaptar una escena a un público.", "Sé que cambiar una variable por vez permite comparar."],
    explain=[
        "El ensayo general es una versión completa de la escena, con todos los recursos y en el tiempo real, como si hubiera público. Sirve para detectar problemas que no se ven en ensayos por partes: el tiempo que dura, los cambios de objetos, la voz en el espacio real y si el lenguaje se entiende. Mientras unos interpretan, otras personas observan con una pauta y anotan hechos, no solo opiniones.",
        "Una pauta de interpretación reúne criterios con puntaje, por ejemplo voz audible, intención clara, escucha entre intérpretes, uso del espacio y adecuación al público. Con los puntajes se ve qué mejorar primero: el criterio más bajo suele ser el más urgente. Las observaciones se leen junto con los puntajes. Si el público ejemplo se mueve a los 6 minutos, la escena puede ser demasiado larga para su atención.",
        "Después se decide qué ajustes hacer. Se cambia una cosa por vez, se vuelve a ensayar y se compara. Se conserva lo que funcionó y se agradece lo que aportaron quienes observaron. Si un ensayo genera cansancio excesivo, dolor de voz o incomodidad, se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("ensayo general", "ensayo completo, con todos los recursos y en el tiempo real"), ("pauta", "lista de criterios con puntaje para valorar una escena"), ("adecuación al público", "qué tan bien se ajusta la escena a las características de su público"), ("ajuste", "cambio que se hace para mejorar un aspecto"), ("evidencia", "hecho observado que respalda una conclusión")],
    worked=[
        ("Priorizar un ajuste", "Una pauta muestra voz 4, intención 3, escucha 4, espacio 3 y adecuación 2. ¿Dónde se empieza a trabajar y por qué?", ["El puntaje más bajo es adecuación al público: 2.", "Se empieza por ahí, porque es donde hay más por mejorar."], "En la adecuación al público"),
        ("Leer una observación", "Observación: «a los 5 minutos el público bostezaba». ¿Qué ajuste puede probar el grupo?", ["La evidencia sugiere que la escena es larga para su atención.", "Prueba una versión más breve, cambiando solo la duración."], "Acortar la escena y volver a probar"),
    ],
    mistakes=[("Corregir cinco aspectos de una vez después del ensayo.", "No se sabe cuál ajuste produjo la mejora.", "Cambia uno por vez y compara."),
              ("Anotar solo «estuvo bien» o «estuvo mal» en la pauta.", "No se puede decidir qué mejorar.", "Anota hechos: qué ocurrió y cuándo.")],
    T=[
        ('abc', '¿Qué es un ensayo general?', 'Un ensayo completo, con todos los recursos y en el tiempo real', 'Un ensayo solo de la parte más difícil de la escena', 'Una función con público para recibir aplausos y comentarios', 'Reproduce la presentación completa y sirve para detectar problemas globales.'),
        ('abc', '{F} ¿Qué criterio tuvo el puntaje más bajo?', 'Adecuación al público, con 1 punto', 'Voz audible, con 3 puntos', 'Escucha entre intérpretes, con 4 puntos', 'La adecuación al público tiene 1 punto, el más bajo de la pauta.'),
        ('abc', 'Mientras se hace un ensayo general, las personas que observan deben', 'anotar hechos con la pauta, como qué ocurrió y cuándo', 'comentar en voz alta lo que piensan mientras actúan los demás', 'esperar al final para dar una nota global sin ejemplos', 'Anotar hechos permite luego decidir qué mejorar con base en evidencia.'),
        ('abc', '{F} ¿Qué dato respalda que la escena es larga para su público ejemplo?', 'A los 6 minutos el público empezó a moverse', 'La escucha entre intérpretes obtuvo 4 puntos', 'La voz audible obtuvo 3 puntos', 'El movimiento del público en el minuto 6 es evidencia de pérdida de atención.'),
        ('abc', '{F} ¿Qué ajuste se relaciona con la observación sobre las frases largas del comienzo?', 'Reescribir las frases iniciales con un lenguaje más sencillo y corto', 'Subir el volumen en todas las líneas de la escena completa', 'Quitar las acciones del comienzo para que se concentren en el texto', 'La observación apunta al lenguaje, no al volumen ni a la acción.'),
        ('abc', 'Después del ensayo general, ¿cuántos aspectos conviene cambiar a la vez?', 'Uno por vez, para saber cuál produjo el efecto', 'Todos los que se mencionaron, para ahorrar ensayos', 'Ninguno, porque lo que se ensayó siempre queda bien', 'Cambiar una cosa por vez permite comparar versiones.'),
        ('=', '{F} ¿Cuántos puntos suma la pauta de «La lista» en total?', '3+3+4+3+1', 'Se suman los puntajes de los cinco criterios.', ' puntos'),
        ('=', 'La pauta tiene un máximo de 4 puntos por criterio y 5 criterios. ¿Qué porcentaje del máximo logró una escena con 15 puntos?', '15*100//(4*5)', 'Se calcula el máximo posible y se divide el puntaje obtenido entre ese máximo.', ' %'),
        ('abc', 'Un grupo anota «estuvo mal» en la pauta. ¿Qué falta para poder decidir un ajuste?', 'Un hecho concreto: qué ocurrió, cuándo y qué efecto tuvo', 'Un puntaje más alto para el mismo comentario, de manera que el grupo se sienta mejor', 'Una opinión de quien dirige, sin ejemplos', 'Sin hechos no se sabe qué cambiar ni cómo comprobar la mejora.'),
        ('abc', 'Un grupo cambia la duración, el vestuario y las palabras de la escena para mejorar el segundo ensayo, y la escena funciona mejor. ¿Qué puede afirmar?', 'Que algo de lo que cambió ayudó, pero no cuál de los tres cambios', 'Que el vestuario fue la causa de la mejora', 'Que la duración no influyó para nada y que el cambio de palabras fue lo único que ayudó', 'Con tres cambios a la vez no se puede atribuir la mejora a uno solo.'),
        ('abc', 'Una escena obtiene 4 puntos en voz, intención, escucha y espacio, y 1 en adecuación al público. ¿Qué conclusión es razonable?', 'Está bien interpretada, pero no calza con las características de su público', 'Está mal interpretada, porque tiene un criterio con 1 punto', 'No necesita ajustes, porque la mayoría de los criterios tiene el máximo', 'La interpretación es sólida y el desajuste está en cómo se ajusta al público.'),
        ('=', 'El ensayo general dura 9 minutos y el público tiene unos 10 minutos de atención. Si se agregan 2 minutos de saludo y cierre, ¿cuántos minutos se pasa de su atención?', '9+2-10', 'Se suma la duración total y se resta el tiempo de atención.', ' minuto'),
        ('abc', 'Después de un ajuste, el segundo ensayo mejora en voz audible pero sube la duración. ¿Qué hace el grupo?', 'Conserva lo que mejoró y prueba otro ajuste para acortar sin perder la voz', 'Vuelve a la primera versión completa porque no mejoró todo', 'Declara terminada la escena porque algo mejoró', 'Se conserva lo que funciona y se sigue ajustando de a un aspecto.'),
    ],
    ctx=('ab', 'Un compañero te dice que tu escena fue «la mejor». ¿Qué le pides?', 'Que mencione un hecho concreto que le hizo pensar eso', 'Que repita lo mismo para sentir más seguridad', 'Un hecho concreto te sirve para saber qué conservar.'),
    sc=[
        ("En Teatro: ¿para qué sirve el ensayo general?", "Para probar la escena completa y detectar problemas globales", "Se ve la duración real y el funcionamiento de todos los recursos."),
        ("¿Qué es una evidencia en una pauta?", "Un hecho observado que respalda una conclusión", "Permite decidir los ajustes con un fundamento comprobable."),
        ("Si durante un ensayo hay dolor de voz o incomodidad, ¿qué se hace?", "Se detiene el ensayo y se avisa a una persona adulta", "La salud y el bienestar van primero."),
    ],
    op=("Escoge una pauta de ejemplo con cinco criterios de 1 a 4 (voz audible, intención clara, escucha entre intérpretes, uso del espacio y adecuación al público). Inventa los puntajes de un ensayo general, súmalos, señala el criterio más bajo, escribe una observación con un hecho y propone un solo ajuste para el siguiente ensayo.",
        "Puntajes: voz 3, intención 4, escucha 3, espacio 2, adecuación 3; total 15. Más bajo: uso del espacio. Observación: en el minuto 4 dos intérpretes quedaron de espaldas al público. Ajuste: reubicar las sillas en diagonal.",
        ["puntajes sumados correctamente", "identifica el criterio más bajo", "observación con hecho concreto", "propone un solo ajuste"],
        ["pauta completa con ajuste"],
        ["proponer varios ajustes a la vez", "anotar solo opiniones generales"],
        "Pregunta: «¿qué hecho respalda tu observación?». Si no hay, pídele escribirlo."),
    reinforce="Haz una pauta de cinco criterios y evalúa un ensayo inventado de seis líneas, con un hecho por cada criterio.",
    extend="Explica por qué un criterio con puntaje bajo no significa que el equipo actuó mal en todo.",
)

# ============================================================ OAC-03, clase 6
F = ("Ficha 6 (caso de ejemplo, inventado). Un grupo presentará «La lista», un texto original suyo, a 25 estudiantes de 4.º básico en la sala de ese curso. La docente del curso lo autorizó. "
     "Programa de mano propuesto: título, «texto original del grupo» y los nombres de pila de los integrantes. Una persona propone sacar fotos de la función para subirlas al blog del colegio.")
build(
    O3, 6, F,
    use="Aprenderé a presentar una interpretación ante su público con respeto: avisar y coordinar con quien corresponde, reconocer la autoría, cuidar la accesibilidad y pedir consentimiento para fotos, grabaciones y difusión.",
    prior=["Sé adaptar una escena a su público.", "Sé que grabar o difundir requiere consentimiento.", "Sé revisar una escena con una pauta."],
    explain=[
        "Presentar ante un público específico requiere coordinación previa: se acuerda con su docente o responsable el día, la hora, el lugar y la duración, y se confirma que el contenido es apropiado para su edad. El día de la función se llega con tiempo, se revisa el espacio, se recuerda quién cumple cada rol y se comienza con una señal acordada. Al terminar, se agradece y, si corresponde, se conversa con el público.",
        "La autoría se reconoce: un programa de mano puede indicar el título, quién escribió el texto y los intérpretes. Si el texto es de otra persona, se necesita su permiso para presentarlo y se menciona su nombre. Las personas del equipo aparecen en el programa solo con su consentimiento, y es mejor usar nombres de pila o lo que cada una acepte.",
        "Fotografiar, grabar o publicar la función necesita permiso de todas las personas que aparecen y, tratándose de niños y niñas del público, de sus personas adultas responsables y de la docente del curso. Sin ese permiso no se toman ni se publican imágenes. También se cuida la accesibilidad: un lugar despejado para quien necesite movilidad, un volumen que todos entiendan y asientos desde donde se vea. Si ocurre cualquier situación de riesgo, se detiene la función y se avisa a una persona adulta.",
    ],
    vocab=[("coordinación previa", "acuerdo anticipado con el público o su responsable sobre día, lugar y contenido"), ("programa de mano", "hoja que informa título, autoría e integrantes de la función"), ("autoría", "reconocimiento de quién creó el texto o la obra"), ("accesibilidad", "condiciones para que todas las personas puedan participar y ver"), ("consentimiento", "autorización libre de una persona para su participación o imagen")],
    worked=[
        ("Coordinar antes de presentar", "Un grupo quiere mostrar su escena a un 4.º básico. ¿Qué hace antes?", ["Conversa con la docente del curso para acordar día, hora, lugar y duración.", "Confirma que el contenido es apropiado para esa edad."], "Coordinar con la docente y confirmar el contenido"),
        ("Decidir sobre las fotos", "Una persona del grupo quiere sacar fotos del público para el blog. ¿Qué corresponde?", ["Las imágenes de niños y niñas necesitan permiso de sus personas adultas responsables y de la docente.", "Sin ese permiso, no se toman ni se publican."], "No fotografiar sin permiso"),
    ],
    mistakes=[("Presentar sin avisar, «de sorpresa», a un curso más pequeño.", "No se puede cuidar el contenido, el tiempo ni la seguridad del grupo.", "Coordina con la docente o responsable."),
              ("Publicar fotos porque «es un blog del colegio».", "El lugar no reemplaza el permiso de las personas que aparecen.", "Pide autorización antes de tomar o publicar imágenes.")],
    T=[
        ('abc', '¿Qué se hace antes de presentar una escena ante el curso de otra docente?', 'Coordinar con ella día, hora, lugar, duración y contenido', 'Presentar de sorpresa para que la función sea más espontánea', 'Pedir a su curso que decida lo que pueden ver sin consultarle', 'La coordinación previa evita problemas de contenido, tiempo y seguridad.'),
        ('abc', '{F} ¿Qué dice el programa de mano propuesto sobre la autoría del texto?', 'Que es un texto original del grupo', 'Que es una obra publicada de otra persona', 'Que el texto no tiene autor', 'El programa dice «texto original del grupo», lo que reconoce la autoría del propio equipo.'),
        ('abc', '{F} La persona propone sacar fotos de la función para el blog. ¿Qué falta antes?', 'El permiso de las personas adultas responsables y de la docente, por ser niños y niñas', 'Que el blog tenga muchos visitantes para que la función se conozca en todo el colegio', 'Que las fotos queden bien encuadradas y nítidas', 'Las imágenes de menores requieren autorización de sus responsables y del docente.'),
        ('abc', 'Si el texto fuera de otra persona, ¿qué haría el grupo?', 'Pedir su permiso para presentarlo y nombrarla como autora', 'Presentarlo sin mencionar nada, porque la obra es conocida', 'Cambiar algunas palabras y decir que lo escribieron ellos', 'La obra ajena se usa con permiso y con reconocimiento de su autoría.'),
        ('abc', '¿Por qué conviene llegar con tiempo a la función?', 'Para revisar el espacio, los recursos y recordar los roles antes de empezar', 'Para comenzar antes de que llegue el público y así no tener que esperar a que se ordene la sala', 'Para no tener que saludar al curso al entrar', 'La preparación del espacio y del equipo da seguridad a la presentación.'),
        ('abc', '¿Qué ayuda a la accesibilidad en una sala de clases?', 'Un pasillo despejado, asientos con buena vista y un volumen que todos entiendan', 'Colocar todos los asientos pegados a la pared para ocupar menos espacio', 'Usar una voz muy baja para no molestar a otros cursos', 'La accesibilidad permite que todas las personas participen y vean o escuchen.'),
        ('=', 'La función dura 10 minutos y el saludo y cierre otros 3. Si se prepara el espacio durante 7 minutos antes, ¿cuántos minutos suma todo?', '10+3+7', 'Se suman función, saludo y cierre, y preparación.', ' minutos'),
        ('abc', 'En el programa de mano, ¿cómo se nombra a los integrantes?', 'Como cada persona haya aceptado, por ejemplo con nombre de pila', 'Con nombre completo y curso aunque algunos no lo hayan autorizado', 'No se nombra a nadie para evitar problemas', 'Nombrar a las personas requiere su consentimiento y el programa debe respetarlo.'),
        ('abc', 'Antes de grabar la función para mostrarla a otro curso, ¿qué corresponde?', 'Obtener el permiso de las personas que aparecen y acordar dónde se mostrará', 'Grabar primero toda la función y decidir después, con calma, si se muestra o no', 'Grabar solo la parte de quienes tienen más seguridad', 'La grabación y su uso necesitan permiso y un destino acordado de antemano.'),
        ('abc', 'Dos integrantes quieren subir la grabación a una red abierta y una duda. ¿Qué corresponde?', 'No subirla y respetar la decisión de quien duda', 'Subirla si la mayoría está a favor porque es lo más democrático', 'Subirla y borrar el video si alguien reclama más tarde', 'El permiso es individual, y publicar en abierto no se puede revertir del todo.'),
        ('abc', 'Alguien del público se descompone durante la función. ¿Qué hace el grupo?', 'Detener con calma y avisar a una persona adulta responsable', 'Seguir hasta el final para no estropear la presentación', 'Pedir al público que ignore lo que pasa y mire la escena', 'Ante una situación de riesgo se detiene y se avisa; la escena puede esperar.'),
        ('=', 'Un curso tiene 25 estudiantes. Si 22 familias entregaron autorización para fotos, ¿cuántas faltan?', '25-22', 'Se resta lo entregado al total del curso.', ' autorizaciones'),
        ('abc', 'Después de la función, el curso comenta la escena. ¿Qué actitud del grupo es adecuada?', 'Agradecer, escuchar con respeto y tomar nota de lo que se repite en los comentarios', 'Defender cada decisión y explicar por qué el público se equivocó', 'No escuchar los comentarios del curso para no desanimarse ni cambiar lo que ya ensayaron', 'Escuchar sin defenderse permite aprender de la experiencia con el público.'),
    ],
    ctx=('ab', 'Faltan dos autorizaciones de familias para tomar fotos. ¿Qué conviene hacer?', 'No tomar fotos del curso y mostrar la escena sin registro', 'Tomar las fotos y pedir permiso después', 'Sin autorización no se registran imágenes; la función se puede hacer igual.'),
    sc=[
        ("En Teatro: ¿qué es la coordinación previa?", "Un acuerdo anticipado con el público o su responsable sobre día, lugar, duración y contenido", "Permite cuidar el contenido y la seguridad."),
        ("¿Qué se necesita para fotografiar a niños del público?", "El permiso de sus personas adultas responsables y de la docente", "Además se pide la autorización de sus responsables."),
        ("Si hay una situación de riesgo durante la función, ¿qué se hace?", "Se detiene la función y se avisa a una persona adulta", "La seguridad va antes que la presentación."),
    ],
    op=("Escoge un público de ejemplo (un curso menor, una junta de vecinos o un taller del colegio). Escribe: con quién coordinarías y qué acordarías, cómo sería tu programa de mano (título, autoría e integrantes con su consentimiento), una medida de accesibilidad y qué harías respecto de fotos o grabaciones.",
        "Público: un 4.º básico. Coordino con su docente día, hora y duración. Programa: «La lista», texto original del grupo, integrantes con nombre de pila. Accesibilidad: pasillo despejado. Fotos: solo con permiso de las familias y de la docente; si no, no se toman.",
        ["coordina con quien corresponde", "programa con autoría y consentimiento", "medida de accesibilidad", "respeta permisos para fotos"],
        ["hoja con la planificación de la presentación"],
        ["presentar sin avisar", "publicar fotos sin permiso"],
        "Pregunta: «¿quién autoriza esto?». Debe nombrar a las personas correspondientes."),
    reinforce="Escribe un programa de mano de ejemplo para una escena inventada de tu grupo, con título, autoría e integrantes con su consentimiento.",
    extend="Explica por qué pedir permiso para las fotos de una función es una forma de cuidar a las personas del público.",
)
