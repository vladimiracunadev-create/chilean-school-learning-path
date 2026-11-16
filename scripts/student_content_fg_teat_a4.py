"""Teatro 3.º y 4.º medio FG: OAC-03 (interpretación teatral para un público específico), clases 1 a 3. Escenas originales e inventadas; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O3 = "FG-TEAT-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (escena original de ejemplo, «La lista»). Personajes: MARTA y TOMÁS, ambos de 17 años, en una sala de estudio. "
     "(MARTA mira su teléfono y levanta las cejas.) MARTA: Salió la lista del taller. TOMÁS: (sin levantar la vista del cuaderno) ¿Y? MARTA: Estoy segunda. "
     "TOMÁS: (deja el lápiz) ¿De cuántas vacantes? MARTA: De dos. (Pausa larga.)")
build(
    O3, 1, F,
    use="Aprenderé a elegir una escena breve que exprese un tema de interés y a preparar su interpretación con habilidades actorales (concentración, escucha, control de la voz y del cuerpo, memoria e imaginación).",
    prior=["Sé armar una situación con objetivo y obstáculo.", "Sé usar recursos de cuerpo y voz con un propósito.", "Sé leer acotaciones."],
    explain=[
        "Interpretar una obra o una escena es darle vida con el cuerpo, la voz y la intención de un personaje. Se puede partir de un tema que importa a quienes interpretan, como esperar un resultado, ponerse de acuerdo con alguien o pedir ayuda. Para elegir una escena conviene que el tema se pueda mostrar con acciones y conflicto y que sea respetuoso con todas las personas del grupo y del público.",
        "Las habilidades actorales son capacidades que se entrenan. La concentración mantiene la atención en la escena. La escucha permite responder a lo que hace la otra persona. El control de la voz y del cuerpo permite decidir volumen, ritmo, gesto y postura. La memoria ayuda a recordar el texto, mejor si cada línea se asocia a una acción o intención. La imaginación permite creer en la situación y en el espacio de la escena.",
        "Un texto dramático se compone de diálogos y de acotaciones, que son las indicaciones entre paréntesis sobre acciones, gestos o silencios. Una pausa escrita no es un vacío: es un momento de tensión que se sostiene con el cuerpo y la mirada. Los textos de esta clase son originales y breves; si el grupo trabaja con una obra publicada, su texto completo debe conseguirlo con su docente.",
    ],
    vocab=[("interpretar", "dar vida a un personaje con cuerpo, voz e intención"), ("habilidad actoral", "capacidad que se entrena para actuar, como la concentración o la escucha"), ("diálogo", "palabras que se dicen los personajes"), ("acotación", "indicación escrita entre paréntesis sobre acciones, gestos o silencios"), ("intención", "lo que el personaje quiere lograr con lo que dice o hace")],
    worked=[
        ("Elegir una escena", "Un grupo duda entre una escena sobre esperar un resultado y otra sobre un secreto de un compañero real. ¿Cuál elige?", ["La primera puede mostrarse con acciones y no expone a nadie.", "La segunda usaría información real de una persona y puede herirla."], "La escena sobre esperar un resultado"),
        ("Leer una acotación", "En un texto aparece: «(Se sienta y mira la puerta. Silencio.)». ¿Cómo la interpretas?", ["Hago la acción de sentarme y dirijo la mirada a la puerta.", "Mantengo el silencio con intención, sin llenarlo con ruidos ni palabras."], "Acción visible y silencio sostenido"),
    ],
    mistakes=[("Llenar una pausa escrita con palabras o chistes para que «no se note».", "La pausa forma parte de la tensión que el texto busca.", "Sostén el silencio con la mirada y el cuerpo."),
              ("Aprenderse el texto de memoria pero sin intención.", "Se oye como un recitado y el público no entiende qué quiere el personaje.", "Asocia cada línea a una acción o una intención.")],
    T=[
        ('abc', '¿Qué es una habilidad actoral?', 'Una capacidad que se entrena para actuar, como la concentración o el control de la voz', 'Un talento con el que se nace y que no cambia con la práctica ni con los ensayos del grupo', 'El texto que se memoriza antes del primer ensayo del grupo', 'Las habilidades se desarrollan con práctica; no son un don fijo ni solo memoria.'),
        ('abc', '{F} ¿Qué tema de interés aborda la escena?', 'Recibir un resultado de selección y cómo reaccionan dos personas', 'Un conflicto por una nota que se considera injusta', 'Un viaje de estudio a otro país', 'El texto trata de una lista de un taller y de estar segunda entre dos vacantes.'),
        ('abc', '{F} En la acotación «(Pausa larga.)», ¿qué debe hacer quien actúa?', 'Sostener el silencio con intención y mantener la tensión del momento', 'Llenar el silencio con una frase improvisada para que no se note', 'Salir de escena hasta que la pausa termine', 'La pausa es parte del efecto y se sostiene con cuerpo y mirada.'),
        ('abc', '¿Por qué es clave la concentración para interpretar?', 'Porque mantiene la atención en la escena y en quien comparte contigo', 'Porque evita tener que aprenderse el texto del personaje y permite improvisar todo lo demás', 'Porque permite actuar sin mirar nunca al público ni a nadie', 'Sin concentración se pierde la situación y la respuesta a la otra persona.'),
        ('abc', '{F} Tomás deja el lápiz antes de preguntar «¿De cuántas vacantes?». ¿Qué comunica ese cambio?', 'Que su atención pasa del cuaderno a la noticia', 'Que ya terminó su tarea y quiere salir', 'Que se enojó con Marta y la quiere interrumpir', 'Dejar el lápiz marca un cambio de atención justo antes de preguntar.'),
        ('abc', '¿Cuál es un criterio adecuado para elegir una escena de interés?', 'Que el tema pueda mostrarse con acciones y conflicto, y sea respetuoso con todos', 'Que sea el tema más conocido en las redes del momento y el que más comentarios reciba', 'Que no tenga conflicto, para que sea fácil de ensayar', 'Una escena necesita acción y conflicto, y no debe herir a nadie.'),
        ('=', 'Una escena dura 4 minutos. Se ensaya 5 veces, con una pausa de 2 minutos entre un ensayo y el siguiente (4 pausas). ¿Cuántos minutos dura la sesión?', '5*4+4*2', 'Se suman los minutos de los ensayos y los de las pausas intermedias.', ' minutos'),
        ('abc', '¿Cuál es una forma eficaz de memorizar el texto de la escena?', 'Leer por partes en voz alta y asociar cada línea a una acción o intención', 'Repetir sin pensar hasta que suene como un recitado idéntico cada vez, sin cambiar nada del tono', 'Memorizar solo las líneas de la otra persona para poder responder', 'Asociar acción e intención ayuda a recordar y a decir con sentido.'),
        ('abc', '{F} Una lectura que se apoya en el texto sobre lo que quiere Marta es', 'Contar el resultado y buscar la reacción de Tomás', 'Pedirle a Tomás que le preste su cuaderno de estudio', 'Convencer a Tomás de que ya no estudie más por hoy', 'Solo la primera se desprende de lo que dice y hace Marta; las otras no aparecen en la escena.'),
        ('abc', 'Dos intérpretes dicen «Estoy segunda»: uno con voz alegre y otra con voz baja y tensa. ¿Qué cambia?', 'La intención que percibe el público, aunque el texto sea el mismo', 'El texto, porque al cambiar la voz ya no es la misma línea que escribió el autor', 'Nada, ya que las palabras son idénticas en ambos casos', 'La interpretación cambia el sentido de las mismas palabras.'),
        ('abc', 'Un grupo quiere cambiar el tema de la escena por una disputa real del curso. ¿Qué conviene?', 'Crear un tema ficticio parecido, sin exponer a nadie, y consultarlo con el docente', 'Usar la disputa real porque así el público se interesa más en la escena y sabe que es verdad', 'Mantenerla en secreto hasta el día de la función para sorprender', 'Exponer una disputa real puede herir; un tema ficticio permite expresar lo mismo con cuidado.'),
        ('=', 'La escena tiene 8 líneas de 15 segundos cada una y 4 pausas de 10 segundos. ¿Cuántos segundos dura?', '8*15+4*10', 'Se suman los segundos de las líneas y los de las pausas.', ' segundos'),
        ('abc', 'Una compañera afirma que para interpretar bien basta con aprenderse el texto. ¿Qué respuesta es adecuada?', 'Falta usar cuerpo, voz, escucha y concentración para darle intención al texto', 'Tiene razón, porque el texto contiene todo lo que hay que mostrar al público', 'Es lo contrario: no hay que aprender el texto y solo hay que improvisar', 'El texto es solo un punto de partida; la interpretación lo completa con acciones e intención.'),
    ],
    ctx=('ab', 'Una escena que elegiste trata un tema que te incomoda mucho. ¿Qué haces?', 'Lo converso con el docente y propongo otra escena o rol', 'La actúo igual para no quedar mal con el grupo', 'Avisar y cambiar es lo correcto; el grupo no necesita que sufras para actuar.'),
    sc=[
        ("En Teatro: ¿qué es una acotación?", "Una indicación entre paréntesis sobre acciones, gestos o silencios", "Orienta la interpretación sin ser parte de lo que se dice."),
        ("¿Qué habilidad actoral permite responder a lo que hace la otra persona?", "La escucha", "Escuchar permite reaccionar en vez de recitar."),
        ("Si una escena te incomoda o te expone demasiado, ¿qué haces?", "Aviso al docente o a una persona adulta de confianza y pido cambiarla", "El bienestar de las personas va antes que la escena."),
    ],
    op=("Escoge un tema de ejemplo: esperar un resultado, pedir ayuda o ponerse de acuerdo. Escribe una escena original de entre cuatro y seis líneas con dos personajes y dos acotaciones (una acción y un silencio). Luego anota qué habilidades actorales usarías para interpretarla y por qué el tema no expone a nadie.",
        "Tema: pedir ayuda. A: (mira un papel y frunce el ceño) No entiendo este formulario. B: (se acerca) ¿Quieres que lo veamos juntas? A: (pausa) Sí, por favor. Habilidades: escucha y concentración; el tema es general y no usa casos reales.",
        ["escena original de cuatro a seis líneas", "incluye acotación de acción y de silencio", "nombra habilidades actorales", "no expone a nadie"],
        ["escena escrita y breve explicación"],
        ["usar casos reales del curso", "llenar la escena de diálogo sin acciones"],
        "Pregunta: «¿qué hace cada personaje además de hablar?». Si nada, falta acción."),
    reinforce="Lee en voz alta una escena breve inventada y marca con lápiz una acción y una pausa que sostendrías.",
    extend="Explica por qué el mismo texto puede ser distinto cuando lo interpretan dos personas.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (escena original de ejemplo, «La tarjeta»). Personajes: LUCÍA, de 16 años, y su hermano mayor PABLO, de 19. "
     "LUCÍA: Hoy no vas a usar tu tarjeta de transporte, ¿cierto? PABLO: Depende. LUCÍA: Solo hasta las cinco. PABLO: (guarda la tarjeta en el bolsillo) Tengo que salir temprano. "
     "LUCÍA: Yo te presté mi cargador, ¿te acuerdas?")
build(
    O3, 2, F,
    use="Aprenderé a construir un personaje a partir del texto: su objetivo, su obstáculo, las tácticas que usa, su relación con el otro personaje y lo que quiere decir sin decirlo (el subtexto).",
    prior=["Sé que un personaje tiene objetivo y obstáculo.", "Sé leer acotaciones.", "Sé usar cuerpo y voz con intención."],
    explain=[
        "Construir un personaje es responder, a partir del texto, algunas preguntas: quién es, qué quiere en la escena (objetivo), qué se lo impide (obstáculo), cómo intenta conseguirlo (tácticas) y qué relación tiene con el otro personaje. Las tácticas son los modos de actuar para lograr el objetivo: pedir con suavidad, recordar un favor, insistir, bromear, ofrecer algo a cambio o dar una respuesta evasiva (ni sí ni no). Cada línea del texto suele usar una táctica distinta.",
        "El subtexto es lo que el personaje quiere decir sin decirlo. Cuando Lucía dice «yo te presté mi cargador», sus palabras hablan de un cargador, pero su intención es recordar que Pablo le debe un favor. El público entiende el subtexto por el tono, la mirada y el cuerpo. Una misma frase puede tener otro subtexto si el contexto cambia.",
        "Un personaje se construye con respeto: se inspira en observaciones y en el texto, pero no es una persona real ni la identidad de quien actúa. Quien interpreta puede salir del personaje cuando termina la escena. Si el personaje exige algo que incomoda, como contacto físico o temas dolorosos de la vida real, se conversa con el docente y se busca otra forma de mostrarlo.",
    ],
    vocab=[("objetivo", "lo que el personaje quiere conseguir en la escena"), ("obstáculo", "lo que complica que lo consiga"), ("táctica", "modo de actuar para lograr el objetivo"), ("subtexto", "lo que el personaje quiere decir sin decirlo"), ("relación", "vínculo entre dos personajes: hermanos, desconocidos, jefe y empleado")],
    worked=[
        ("Reconocer una táctica", "Un personaje dice: «Tú siempre me ayudas, no me dejes sola ahora». ¿Qué táctica usa?", ["Apela a algo que la otra persona suele hacer para influir en su decisión.", "Es una táctica de presión afectuosa, no una orden."], "Apelar a la ayuda habitual para presionar con afecto"),
        ("Hallar el subtexto", "Un personaje dice «qué lindo reloj» mientras mira insistentemente la mano de otro. ¿Cuál puede ser el subtexto?", ["Las palabras hablan del reloj, pero la mirada se detiene en la mano.", "Puede querer saber la hora o pedirlo prestado sin pedirlo; se decide según la escena."], "Querer algo del otro sin pedirlo directamente"),
    ],
    mistakes=[("Elegir una sola emoción para todo el personaje, como «enojado».", "Un personaje cambia de táctica y de estado a lo largo de la escena.", "Marca cómo cambia su táctica en cada tramo."),
              ("Decir el subtexto en voz alta en vez de actuarlo.", "Se pierde el efecto y el texto queda explicado.", "Muéstralo con mirada, tono y acción.")],
    T=[
        ('abc', '¿Qué es una táctica de un personaje?', 'Un modo de actuar para lograr su objetivo', 'La emoción que quiere provocar en el público', 'La descripción física que aparece en el programa', 'La táctica es el cómo se intenta conseguir el objetivo en la escena.'),
        ('abc', '{F} ¿Cuál es el objetivo más probable de Lucía en la escena?', 'Conseguir usar la tarjeta de transporte de Pablo hasta las cinco', 'Convencer a Pablo de que salga más temprano para que le deje la tarjeta', 'Aprender cómo se guarda una tarjeta con seguridad', 'Todas sus líneas apuntan a pedir la tarjeta; las otras opciones no se apoyan en el texto.'),
        ('abc', '{F} ¿Cuál es el obstáculo principal de Lucía?', 'Pablo no quiere prestarle la tarjeta y la guarda', 'Lucía no sabe a qué hora termina su clase', 'La tarjeta está bloqueada y no sirve', 'Pablo responde con evasivas y guarda la tarjeta, lo que complica el objetivo.'),
        ('abc', '{F} Cuando Lucía dice «Yo te presté mi cargador», ¿qué táctica usa?', 'Recordarle un favor para que sienta que le debe algo', 'Amenazar con contarle a sus padres lo que hizo', 'Ofrecerle dinero para que acepte', 'Menciona un favor pasado para presionar con afecto sin exigirlo.'),
        ('abc', 'El subtexto de un personaje es', 'lo que quiere decir sin decirlo directamente', 'una nota escrita que el actor lee al público', 'el volumen con que dice las líneas', 'Las palabras pueden decir una cosa y la intención otra distinta.'),
        ('abc', 'Dos intérpretes dicen «depende»: uno con sonrisa y otro mirando al piso. ¿Qué cambia?', 'El subtexto, porque la intención que se percibe es distinta', 'El texto, porque cambiaron las palabras que dice cada intérprete en la escena', 'Nada, porque ambos dicen la misma palabra', 'Con la misma palabra, la mirada y el gesto cambian lo que el personaje quiere comunicar.'),
        ('=', '{F} Si se ensaya cada línea de la escena (cada intervención de un personaje) con 3 tácticas distintas y se anota 1 observación por prueba, ¿cuántas observaciones se anotan?', '5*3*1', 'La ficha tiene cinco intervenciones; se multiplican por las tácticas y las observaciones por prueba.', ' observaciones'),
        ('abc', '{F} Pablo dice «Depende». ¿Qué táctica le permite no negarse todavía?', 'Responder con una evasiva que deja abierta la respuesta', 'Aceptar de inmediato para evitar discusión', 'Cambiar el tema por completo', 'La evasiva retrasa la respuesta sin decir que no.'),
        ('abc', 'Para construir un personaje, ¿cuál es un procedimiento adecuado?', 'Responder a partir del texto quién es, qué quiere, qué se lo impide y cómo lo intenta', 'Copiar los gestos de una persona real del curso para que se parezca y el público la reconozca', 'Elegir una emoción y mantenerla igual hasta el final', 'El personaje se funda en el texto y en decisiones propias, no en una persona real.'),
        ('abc', 'Una actriz dice que su personaje «es enojón» y lo actúa igual toda la escena. ¿Qué falta?', 'Cambiar de táctica según cómo responde el otro personaje', 'Enojarse con más volumen cada vez que el otro personaje se niegue a ayudarla', 'Decir al público que el personaje se enoja', 'Las tácticas cambian con la respuesta del otro; una emoción fija vuelve plana la escena.'),
        ('abc', 'El texto exige que dos personajes se empujen con fuerza. ¿Qué corresponde en el aula?', 'Mostrar el conflicto con distancia, miradas y movimientos que no impliquen contacto', 'Empujarse muy suave y con cuidado para que el conflicto se vea real ante todo el público', 'Quitar el conflicto y que no pase nada', 'Se conserva el conflicto con otros recursos y sin contacto riesgoso.'),
        ('=', 'Una escena tiene 3 tramos y en cada tramo el personaje cambia 2 veces de táctica. ¿Cuántos cambios de táctica hay en toda la escena?', '3*2', 'Se multiplican los tramos por los cambios de cada uno.', ' cambios'),
        ('abc', '{F} Si Pablo dijera «Depende» con cariño y guardara la tarjeta mirando a Lucía a los ojos, ¿qué subtexto podría comunicar?', 'Que quiere prestarla, pero quiere que ella lo pida de otra forma', 'Que está molesto con Lucía y quiere terminar la conversación', 'Que la tarjeta no es suya y por eso no puede prestarla', 'El gesto cálido y la mirada sugieren que el rechazo es parcial y juguetón.'),
    ],
    ctx=('ab', 'Debes interpretar a un personaje muy distinto a ti. ¿Qué conviene?', 'Basarte en el texto y en lo que el personaje quiere, sin imitar a nadie real', 'Imitar a una persona que conozcas para que se vea natural', 'El personaje se construye con decisiones propias y el texto, sin exponer a ninguna persona real.'),
    sc=[
        ("En Teatro: ¿qué es el subtexto?", "Lo que el personaje quiere decir sin decirlo", "El público lo entiende por tono, mirada y cuerpo."),
        ("¿Qué es una táctica?", "Un modo de actuar para lograr el objetivo", "Un personaje puede cambiar de táctica varias veces."),
        ("Si una escena te pide algo que te incomoda, como contacto físico, ¿qué haces?", "Lo converso con el docente y busco otra forma de mostrarlo", "Se puede mostrar un conflicto sin contacto."),
    ],
    op=("Escoge un personaje de «La tarjeta» (Lucía o Pablo) o crea un personaje con un objetivo claro. Escribe: su objetivo, su obstáculo, dos tácticas distintas que usa (con la línea donde aparecen), un subtexto posible y cómo lo mostrarías con la mirada o el cuerpo.",
        "Lucía: objetivo, usar la tarjeta hasta las cinco; obstáculo, Pablo guarda la tarjeta; tácticas: pedir con suavidad («Solo hasta las cinco») y recordar un favor («Yo te presté mi cargador»); subtexto, me debes algo; lo muestro con una mirada firme sin sonreír.",
        ["objetivo y obstáculo claros", "dos tácticas distintas con su línea", "un subtexto posible", "indica cómo lo muestra con el cuerpo"],
        ["ficha del personaje"],
        ["describir una sola emoción", "decir el subtexto en voz alta"],
        "Pregunta: «¿en qué línea cambia de táctica?». Si no cambia, pídele buscar otra."),
    reinforce="Elige una frase cotidiana (por ejemplo «ya es tarde») y escribe tres subtextos posibles según quién la dice y a quién.",
    extend="Explica por qué un personaje que solo tiene una emoción resulta menos creíble que uno que cambia de táctica.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (propuestas de ejemplo para montar «La lista»). El equipo estudia tres ideas: (1) usar un sonido de notificación grabado por el propio grupo; "
     "(2) proyectar en una pared una pantalla de teléfono con la lista, dibujada por el grupo; (3) poner de fondo, todo el tiempo, una canción comercial conocida. "
     "El grupo tiene un proyector del colegio y una grabadora de voz de un teléfono.")
build(
    O3, 3, F,
    use="Aprenderé a tomar decisiones de puesta en escena con medios y tecnologías actuales (sonido grabado, proyección, grabación de ensayos), cuidando la seguridad, la autoría y los derechos de uso.",
    prior=["Sé que la puesta en escena incluye espacio, objetos, luz y sonido.", "Sé probar un cambio por vez.", "Sé que las personas tienen derecho a su imagen."],
    explain=[
        "Los medios y tecnologías actuales pueden apoyar una interpretación: un sonido grabado puede anunciar un hecho, una proyección puede mostrar un lugar o un mensaje, y un teléfono puede registrar un ensayo para revisarlo. Estos recursos son útiles cuando ayudan a contar la situación y al propósito del grupo, y dejan de serlo cuando distraen o ocupan el lugar de la actuación.",
        "Cada recurso trae decisiones. El sonido grabado debe ser propio o contar con permiso de uso; las canciones y los videos comerciales tienen derechos de autor y no se usan sin autorización. Las imágenes proyectadas pueden ser creadas por el grupo. Un ensayo grabado solo se guarda y comparte con permiso de quienes aparecen, y se usa únicamente para revisar. Los equipos del colegio los maneja una persona preparada y con permiso del docente.",
        "La seguridad también cuenta: cables recogidos y fuera del paso, equipos estables y fuera del alcance del público, y volumen razonable para no dañar los oídos ni tapar la voz. Se decide con pruebas: se ensaya con y sin el recurso y se compara el efecto, cambiando una sola cosa por vez.",
    ],
    vocab=[("recurso técnico", "sonido, proyección u otra tecnología que apoya la escena"), ("derecho de autor", "derecho de quien creó una obra a decidir cómo se usa"), ("autoría", "reconocimiento de quién creó algo"), ("proyección", "imagen mostrada sobre una superficie con un proyector"), ("volumen", "intensidad del sonido")],
    worked=[
        ("Elegir un sonido", "Un grupo necesita el sonido de una notificación. ¿Qué opción es adecuada?", ["Grabar un sonido propio con el teléfono en el aula.", "Así no se usa material con derechos y el grupo conserva la autoría."], "Un sonido grabado por el propio grupo"),
        ("Revisar la seguridad de un equipo", "El proyector queda en el suelo, con el cable cruzando el pasillo. ¿Qué cambia el grupo?", ["Lo sube a una mesa estable, fuera del paso del público.", "Recoge y fija el cable para que nadie tropiece."], "Equipo estable y cable fuera del paso"),
    ],
    mistakes=[("Poner música comercial «solo de fondo» porque es corta.", "Aunque sea breve, la obra tiene derechos y puede tapar la voz.", "Usa música propia o con permiso, o trabaja con silencio."),
              ("Dejar que la tecnología reemplace la actuación.", "El público necesita ver y oír a los intérpretes.", "Usa el recurso solo si ayuda a contar la situación.")],
    T=[
        ('abc', '¿Cuándo es útil un recurso técnico en una escena?', 'Cuando ayuda a contar la situación y apoya el propósito del grupo', 'Cuando es nuevo y llama la atención del público más que la historia', 'Cuando reemplaza lo que no se logró ensayar', 'El recurso es un apoyo a la historia; no un reemplazo ni un adorno.'),
        ('abc', '{F} ¿Cuál de las tres ideas necesita revisar derechos de autor antes de usarse?', 'La idea 3, la canción comercial de fondo', 'La idea 1, el sonido grabado por el propio grupo', 'La idea 2, la pantalla dibujada por el grupo', 'La canción comercial tiene autor y condiciones de uso; las otras las crea el grupo.'),
        ('abc', '¿Qué es la autoría?', 'El reconocimiento de quién creó algo', 'El permiso para copiar cualquier obra', 'El derecho de cualquiera a modificar una obra ajena', 'La autoría indica quién creó la obra y se respeta al usarla.'),
        ('abc', '{F} La idea 2 muestra en la pared una lista dibujada. ¿Qué ventaja tiene?', 'Muestra un dato de la historia sin que los intérpretes tengan que explicarlo', 'Reemplaza el trabajo del cuerpo y la voz de quienes actúan y evita que se tengan que ensayar', 'Permite proyectar cualquier imagen sin importar su autor', 'Es un recurso propio que comunica un dato y deja la actuación para las personas.'),
        ('abc', 'Antes de grabar un ensayo con el teléfono, el grupo debe', 'pedir permiso a quienes aparecen y acordar para qué se usará', 'avisar al público el día de la función', 'subirlo a una red para recibir comentarios', 'La grabación necesita autorización de las personas que aparecen y un uso acordado.'),
        ('abc', 'El volumen de un sonido grabado en una sala de clases debe ser', 'moderado, de modo que no dañe los oídos ni tape las voces', 'el más alto posible para que llegue al fondo y se note el efecto', 'tan bajo que nadie logre oírlo en la sala', 'Un volumen razonable cuida la salud y deja entender el texto.'),
        ('=', 'El grupo prueba 3 versiones del sonido; cada prueba dura 2 minutos y comentan 1 minuto después de cada una. ¿Cuántos minutos usan?', '3*(2+1)', 'Cada versión usa prueba y comentario; se multiplica por tres.', ' minutos'),
        ('abc', 'El proyector queda en el suelo y su cable cruza el pasillo. ¿Qué corresponde?', 'Subirlo a una mesa estable y fijar el cable fuera del paso', 'Dejarlo así y avisar al público que tenga cuidado', 'Pedir que alguien lo sostenga en brazos durante la función', 'Un equipo estable y un paso despejado evitan caídas y accidentes.'),
        ('abc', '{F} El equipo duda entre ensayar con sonido o sin él. ¿Cómo decide?', 'Ensaya ambas versiones, cambia solo el sonido y compara el efecto', 'Elige la versión con más recursos porque es más moderna', 'Pregunta qué prefiere el equipo que menos ensayó', 'La prueba cambia una sola variable y compara con evidencia.'),
        ('abc', 'Una compañera propone subir a una plataforma abierta un fragmento del ensayo con todas las voces. ¿Qué conviene responder?', 'Pedir primero el permiso de todas las personas que aparecen y acordar dónde se mostrará', 'Hacerlo si el fragmento es corto y nadie va a reconocer a las personas que aparecen en él ni se enterará', 'Hacerlo si la mayoría del grupo está de acuerdo', 'Cada persona decide sobre su voz e imagen, y la difusión necesita permiso.'),
        ('abc', 'Un grupo llena la escena de proyecciones y sonidos. El público dice que no entendió lo que pasaba. ¿Qué pasó?', 'Los recursos técnicos taparon la actuación y la historia', 'El público no sabe de tecnología', 'La proyección debía ser más grande aún', 'Cuando la tecnología se impone, el público pierde la acción de los personajes.'),
        ('=', 'La sala mide 9 metros de largo y la pared de proyección está en un extremo. El proyector se ubica a 3 metros de esa pared. ¿A cuántos metros del proyector queda el fondo de la sala?', '9-3', 'Se resta la distancia entre la pared y el proyector al largo de la sala.', ' metros'),
        ('abc', 'El grupo no consigue la grabadora para el día de la función. ¿Qué alternativa conserva el efecto sin tecnología?', 'Producir el sonido en vivo con la voz o con un objeto seguro, desde fuera de escena', 'Cancelar la escena porque sin grabación no hay forma de contar la historia de manera que el público la comprenda', 'Usar una canción comercial que ya tiene el sonido buscado', 'Se puede lograr el efecto con recursos propios y sin derechos de terceros.'),
    ],
    ctx=('ab', 'Quieres usar en la escena una música muy conocida porque te gusta. ¿Qué conviene hacer?', 'Crear una música propia o pedir permiso de uso antes de usarla', 'Usarla sin avisar porque es solo un fragmento corto', 'La música ajena tiene derechos y se usa con permiso; una pieza propia evita el problema.'),
    sc=[
        ("En Teatro: ¿qué es un recurso técnico?", "Un sonido, una proyección u otra tecnología que apoya la escena", "Se usa si ayuda a contar la historia."),
        ("¿Qué se necesita para usar una canción comercial en una función?", "Permiso de uso, porque tiene derechos de autor", "Usar música ajena sin permiso no está permitido."),
        ("¿Dónde se ubican cables y equipos en una sala?", "Estables y fuera del paso del público", "Así se evitan tropiezos y accidentes."),
    ],
    op=("Escoge una escena de ejemplo (por ejemplo «La lista» o «La tarjeta»). Escribe dos recursos técnicos que usarías (sonido o proyección), de dónde saldrían (propios o con permiso), cómo cuidarías la seguridad del equipo y qué prueba harías para comprobar que ayudan.",
        "«La lista»: sonido de notificación grabado por el grupo y una imagen dibujada proyectada; ambos propios; el proyector en una mesa estable con el cable fijo; prueba con y sin proyección para ver si el público entiende la lista.",
        ["dos recursos con origen propio o permitido", "medidas de seguridad", "prueba que compara con y sin recurso", "no usa obras con derechos sin permiso"],
        ["ficha de decisiones técnicas"],
        ["usar música comercial sin permiso", "no cuidar el volumen ni los cables"],
        "Pregunta: «¿quién creó este sonido o imagen?». Si no es el grupo, debe tener permiso."),
    reinforce="Anota tres sonidos que podrías grabar tú mismo (sin música comercial) para apoyar una escena y qué contarían.",
    extend="Explica por qué un recurso técnico puede empeorar una escena y cómo lo detectarías en un ensayo.",
)
