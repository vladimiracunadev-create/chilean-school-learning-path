"""Interpretación musical 3.º y 4.º medio HC: OAC-03 (diseñar y gestionar presentaciones a públicos específicos: público, medios, programa, producción, ensayo general y evaluación). Casos inventados."""
from __future__ import annotations

from hc_imus_common import CLAVE, build

O3 = "AR-IMUS-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (públicos y piezas de ejemplo, inventados). "
     "Público 1: niñas y niños de un jardín infantil; atienden unos 15 minutos; les gusta moverse y repetir. "
     "Público 2: apoderados de un acto del liceo; sentados; todo el número debe durar 8 minutos; esperan algo cuidado y breve. "
     "Público 3: personas mayores de un hogar de día; sentadas, en un ambiente tranquilo; oyen mejor con un volumen claro y palabras pausadas. "
     "Piezas del grupo: pieza A, canción tranquila de 3 minutos; pieza B, ritmo enérgico de mesa de 2 minutos; pieza C, pieza participativa de 4 minutos, con palmas del público y un estribillo que se repite.")
build(
    O3, 1, F,
    use="Aprenderé a reconocer un público específico y el propósito de una presentación (qué comunicar y para quién), y a elegir piezas y modo de presentarlas según el tiempo, la edad y el ambiente.",
    prior=["Sé planificar un ensayo con tiempos.", "Reconozco rasgos de una pieza (tempo, dinámica, carácter).", "Sé que el volumen se cuida."],
    explain=[
        "Una presentación musical es un encuentro entre quienes interpretan y quienes escuchan. Para diseñarla se parte de dos preguntas: para quién (el público específico) y para qué (el propósito). El público se describe con datos observables: edad, cantidad de tiempo de atención, si está sentado o de pie, y si el ambiente es tranquilo o ruidoso. El propósito se escribe en una frase: «animar», «calmar», «enseñar un proceso», «celebrar».",
        "Con esos datos se toman decisiones. Un público infantil con poco tiempo de atención agradece piezas cortas, participativas y repetitivas. Un público de apoderados en un acto espera una presentación breve, ordenada y cuidada. Un público de personas mayores en un ambiente tranquilo necesita un volumen claro, palabras pausadas y piezas que no abrumen. No hay un público «mejor»: hay decisiones que le sirven más o menos a cada uno.",
        "El tiempo también es una decisión. Si el espacio dura 8 minutos, hay que contar las piezas, la presentación hablada y las pausas. Una presentación que se pasa del tiempo perjudica a todos. Además se cuida a quienes tocan y cantan: se calienta la voz y las manos antes de empezar, y se evita el volumen alto. Todo se puede planificar en papel con una tabla simple de público, propósito y piezas.",
    ],
    vocab=[("público específico", "grupo concreto de personas para quienes se diseña la presentación"), ("propósito", "lo que se quiere comunicar o provocar con la presentación"),
           ("participativa", "pieza en que el público hace algo, como aplaudir o repetir un estribillo"), ("programa", "orden y duración de las piezas que se presentan"),
           ("atención", "tiempo durante el cual un público puede escuchar con interés"), ("ambiente", "condiciones del lugar, como el ruido o la tranquilidad")],
    worked=[
        ("Describir un público", "Un grupo debe tocar en una biblioteca durante una hora tranquila de lectura para jóvenes sentados. ¿Qué datos observables describen al público?",
         ["Edad: jóvenes. Postura: sentados. Ambiente: tranquilo, con lectura en curso.", "Estos datos sugieren piezas suaves y un volumen bajo, que no interrumpan la lectura."],
         "Jóvenes, sentados, en un ambiente tranquilo; piezas suaves y volumen bajo"),
        ("Cuadrar un programa con el tiempo", "Un espacio dura 10 minutos. El grupo quiere tocar una pieza de 4 minutos, otra de 3 minutos y presentar durante 1 minuto. ¿Cuánto tiempo sobra?",
         ["Se suman los tiempos usados: 4 + 3 + 1 = 8 minutos.", "Se restan al espacio: 10 − 8 = 2 minutos."],
         "Sobran 2 minutos"),
    ],
    mistakes=[("Diseñar la presentación pensando en lo que le gusta al grupo y no en el público.", "No se observan las condiciones del público.", "Parte de los datos del público y escribe el propósito antes de elegir piezas."),
              ("Olvidar contar la presentación hablada dentro del tiempo total.", "El tiempo de hablar y de pausas también ocupa minutos.", "Suma piezas, presentación y pausas antes de comparar con el tiempo disponible.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es el público específico de una presentación?', 'El grupo concreto de personas para quienes se diseña la presentación', 'Todas las personas del liceo, sin importar su edad ni su ambiente', 'La cantidad de aplausos que recibe el grupo al terminar de tocar su programa', 'El público específico es un grupo descrito con datos; no es toda la gente ni los aplausos.'),
        ('abc', '{F} ¿Cuánto tiempo de atención tiene el público 1?', 'Unos 15 minutos', 'Unos 8 minutos', 'Unos 30 minutos', 'La ficha dice que las niñas y niños atienden unos 15 minutos.'),
        ('abc', '{F} ¿Qué pieza es participativa?', 'La pieza C, con palmas del público', 'La pieza A, la canción tranquila de tres minutos', 'La pieza B, el ritmo enérgico de mesa', 'La pieza C incluye palmas del público y un estribillo que se repite.'),
        ('=', '{F} ¿Cuántos minutos suman las piezas A, B y C juntas?', '3+2+4', 'Se suman las duraciones de las tres piezas indicadas en la ficha.', ' minutos'),
        ('abc', '{F} ¿Qué pieza le conviene al público 1, que se mueve y repite?', 'La pieza C, porque es participativa y repite un estribillo', 'La pieza A, porque es tranquila y no pide mover el cuerpo', 'La pieza B, porque no dura más que unos pocos minutos', 'Un público infantil agradece una pieza participativa y repetitiva; la pieza C lo es.'),
        ('abc', '{F} El público 2 dispone de 8 minutos para el número y se quiere el programa más largo de piezas completas que quepa. ¿Cuál es?', 'Las piezas A y C, que suman 7 minutos', 'Las piezas A, B y C, que suman 9 minutos', 'Las piezas B y C, que suman 6 minutos', 'A y C suman 7 y caben; A, B y C suman 9 y no caben; B y C caben, pero son más cortas.'),
        ('abc', '{F} ¿Qué decisión de presentación sirve al público 3?', 'Hablar con palabras pausadas y usar un volumen claro, sin subirlo en exceso', 'Hablar rápido para ganar tiempo y tocar siempre en volumen fuerte, sin pausas', 'Hablar bajo para no molestar y tocar sin que se oiga casi nada de la música', 'El público 3 oye mejor con volumen claro y palabras pausadas, sin exagerar el volumen.'),
        ('=', '{F} Para el público 2 se tocan las piezas A y B y se presenta durante 1 minuto. ¿Cuántos minutos sobran de los 8 disponibles?', '8-(3+2)-1', 'Se restan de los 8 minutos las dos piezas y la presentación hablada.', ' minutos'),
        ('abc', 'Un grupo prepara una sola presentación idéntica para los tres públicos de la ficha. ¿Qué problema tiene esa decisión?', 'No considera la edad, el tiempo ni el ambiente de cada público', 'Ninguno, porque una buena presentación sirve a todos por igual', 'Que las piezas serán más largas de lo que cada público necesita', 'Los tres públicos difieren en edad, tiempo y ambiente, así que una sola versión sirve peor a todos.'),
        ('abc', 'Un grupo afirma: «conocemos al público porque todos son personas». ¿Qué falla en esa descripción?', 'No usa datos observables como edad, tiempo y ambiente', 'Usa demasiados datos para describir al público', 'Describe al público por el propósito de la presentación', 'Un público específico se describe con datos observables; «personas» no permite decidir nada.'),
        ('abc', '{F} Un integrante propone tocar la pieza B más fuerte para el público 3 «para que se oiga». ¿Qué decisión es mejor?', 'Mantener un volumen moderado y claro, y pausar las palabras', 'Subir el volumen al máximo para evitar cualquier malentendido', 'Cambiar la pieza B por una pieza más rápida y ruidosa', 'El ambiente es tranquilo; basta un volumen claro y moderado, que además cuida el oído.'),
        ('abc', '{F} El propósito es «calmar y acompañar» al público 3. ¿Qué programa lo apoya mejor?', 'La pieza A y una presentación pausada', 'La pieza B repetida varias veces seguidas', 'La pieza C con palmas del público muy fuertes', 'La pieza A es tranquila y la presentación pausada acompaña el propósito de calmar.'),
        ('=', '{F} Para el público 1, el grupo toca la pieza C dos veces y presenta 2 minutos. ¿Cuántos minutos sobran de los 15 de atención?', '15-(4*2+2)', 'Se suman las dos pasadas de la pieza C y la presentación, y se restan de 15 minutos.', ' minutos'),
    ],
    ctx=('abc', 'Tu curso te pide presentar tres minutos de música en la sala de espera de un consultorio, donde las personas esperan sentadas y en silencio. ¿Qué decisión respeta al público?', 'Elegir una pieza suave, con volumen bajo y sin interrumpir las conversaciones', 'Elegir una pieza muy enérgica para que todos se animen de inmediato y se levanten', 'Tocar sin avisar y con volumen alto para que se note bien la presentación', 'Un ambiente de espera pide música suave y respeto por el silencio del lugar.'),
    sc=[
        ("En Interpretación musical: ¿qué es el propósito de una presentación?", "Lo que se quiere comunicar o provocar con ella", "El propósito se escribe en una frase y guía las decisiones."),
        ('abc', 'Para describir a un público conviene usar:', 'Datos como edad, tiempo de atención y ambiente', 'Solo el gusto personal del grupo', 'El nombre del colegio y nada más sobre las personas que escuchan', 'Los datos observables permiten decidir las piezas y su volumen.'),
        ("¿Por qué se suman la presentación y las pausas al calcular el tiempo?", "Porque también ocupan minutos del espacio disponible", "Si no se cuentan, la presentación se pasa del tiempo."),
    ],
    op=("Con la {F}, elige uno de los tres públicos y escribe: (1) una frase con el propósito; (2) el programa que presentarías (piezas y presentación hablada) y cuántos minutos suma; (3) una decisión de volumen y de voz para ese público.",
        "Público 2 (apoderados). Propósito: mostrar un trabajo cuidado y breve. Programa: pieza A (3 min), pieza B (2 min) y presentación de 1 minuto: suma 6 minutos de los 8 disponibles. Volumen: moderado y claro, con una presentación hablada ordenada y sin apuro.",
        ["escribe un propósito claro", "arma un programa que cabe en el tiempo", "calcula los minutos con la presentación", "decide volumen y voz según el público"],
        ["hoja con el público elegido, el propósito, el programa y las decisiones"],
        ["no sumar la presentación hablada", "elegir sin relacionar con el público", "pasarse del tiempo disponible"],
        "Pregunta: «¿qué dato del público apoya esa decisión?». Si no lo cita, pídele que lo busque en la ficha."),
    reinforce="Describe un público imaginario con tres datos observables y escribe qué tipo de pieza le serviría y por qué.",
    extend="Explica por qué un mismo repertorio puede presentarse de manera distinta ante dos públicos y qué decisiones cambiarías.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (recursos para presentar, de ejemplo, inventados). Presentación de un grupo de 5 personas ante 40 personas en un gimnasio con eco, sin enchufes cerca del escenario. "
     "Recurso 1: programa impreso de una hoja, con piezas y autorías; no necesita electricidad. "
     "Recurso 2: micrófono y parlante con batería de 3 horas; sirve para la voz hablada en espacios grandes; hay que probarlo y mantener un volumen moderado. "
     "Recurso 3: proyección de una imagen con el título de cada pieza; necesita enchufe y oscurecer la sala. "
     "Recurso 4: grabación de audio con un teléfono, solo con permiso de quienes aparecen; sirve para revisar el ensayo. "
     "Recurso 5: transmisión en línea del acto; necesita buena conexión y permiso de todas las personas que aparecen.")
build(
    O3, 2, F,
    use="Aprenderé a elegir recursos tradicionales y tecnologías emergentes para una presentación (programa, amplificación, proyección, grabación y transmisión), según el espacio, el público y las condiciones, cuidando el oído y los permisos.",
    prior=["Sé describir un público y un propósito.", "Sé que el volumen se cuida.", "Sé que grabar o difundir requiere permiso."],
    explain=[
        "Un medio es la vía por la que una presentación llega al público. Los medios tradicionales son los que se usan hace mucho y no necesitan electricidad: la voz, los instrumentos acústicos, el escenario, el programa impreso y una presentación hablada. Las tecnologías emergentes son las más recientes: amplificación con micrófono, proyección de imágenes, grabación con un teléfono y transmisión en línea. Ninguna es mejor por ser nueva: se elige según lo que se necesita.",
        "Para elegir se revisan tres cosas: el espacio (tamaño, eco, enchufes), el público (cantidad, edad, si necesita oír mejor) y las condiciones del recurso (electricidad, batería, conexión, permisos). Un recurso sirve si resuelve una necesidad real y cabe en las condiciones. Por ejemplo, una voz hablada se oye bien sin micrófono ante 12 personas, pero ante 200 en un gimnasio con eco conviene amplificarla a volumen moderado.",
        "Cada recurso trae cuidados. La amplificación se prueba antes y se mantiene en un volumen que no dañe el oído. Un recurso que necesita enchufe exige un plan B si no hay electricidad. Grabar o transmitir exige permiso de cada persona que aparece y de quien tenga derechos sobre la música. Las imágenes y los textos proyectados deben ser legibles y estar atribuidos. Todo esto se anota antes del día de la presentación.",
    ],
    vocab=[("medio", "vía por la que una presentación llega al público"), ("medio tradicional", "recurso que no necesita electricidad, como la voz o el programa impreso"),
           ("tecnología emergente", "recurso reciente, como la transmisión en línea"), ("amplificar", "aumentar el volumen de un sonido con micrófono y parlante"),
           ("plan B", "alternativa que se usa si un recurso falla"), ("eco", "repetición del sonido por rebote en un espacio grande")],
    worked=[
        ("Elegir un recurso según el espacio", "Una presentación será ante 10 personas en una sala pequeña y sin eco. ¿Hace falta amplificar la voz hablada?",
         ["Con pocas personas y una sala pequeña sin eco, la voz hablada se oye bien por sí sola.", "Amplificar agregaría complejidad y riesgo de volumen alto sin necesidad."],
         "No: la voz sola alcanza y es más seguro"),
        ("Pensar un plan B", "Un grupo planea proyectar el título de cada pieza, pero no sabe si habrá enchufe. ¿Qué plan B conviene?",
         ["Se necesita un medio que no dependa de la electricidad.", "Un programa impreso o decir el título en voz alta entrega la misma información."],
         "Un programa impreso o anunciar el título en voz alta"),
    ],
    mistakes=[("Usar un recurso solo porque es novedoso.", "No se revisa si resuelve una necesidad real.", "Pregunta qué necesidad resuelve y si cabe en las condiciones del lugar."),
              ("Grabar o transmitir sin avisar porque «es solo el ensayo».", "Se olvida el permiso de cada persona.", "Pide permiso antes y respeta a quien no quiera aparecer.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un medio tradicional?', 'Un recurso que no necesita electricidad, como la voz o el programa impreso', 'Una grabación de audio que se comparte en una plataforma en línea con el público', 'Un micrófono con batería que se usa en espacios muy grandes y con eco', 'Los medios tradicionales no dependen de electricidad; la grabación y el micrófono son tecnologías.'),
        ('abc', '{F} ¿Qué recurso no necesita electricidad?', 'El programa impreso (recurso 1)', 'La proyección de una imagen (recurso 3)', 'La transmisión en línea (recurso 5)', 'Solo el programa impreso funciona sin enchufe ni conexión.'),
        ('abc', '{F} ¿Para qué sirve la grabación de audio de la ficha?', 'Para revisar el ensayo, con permiso de quienes aparecen', 'Para transmitir el acto en vivo a otras ciudades sin pedir permiso', 'Para reemplazar al grupo durante la presentación en vivo ante el público', 'La ficha dice que la grabación sirve para revisar el ensayo, con permiso.'),
        ('=', '{F} El micrófono dura 3 horas con batería. Si el acto dura 45 minutos, ¿cuántos minutos de batería sobran?', '3*60-45', 'Se pasan las 3 horas a minutos y se resta la duración del acto.', ' minutos'),
        ('abc', '{F} El gimnasio tiene eco y 40 personas. ¿Qué decisión conviene para la voz hablada?', 'Amplificarla con micrófono, a volumen moderado y probado antes', 'No amplificarla y pedir al público que se acerque mucho al escenario', 'Amplificarla al máximo para que se oiga sobre el eco del gimnasio', 'En un espacio grande con eco conviene amplificar la voz, pero a un volumen moderado y probado.'),
        ('abc', '{F} No hay enchufes cerca del escenario. ¿Qué recurso tiene un problema?', 'La proyección de una imagen, porque necesita enchufe', 'La grabación de audio, porque un teléfono nunca funciona sin enchufe', 'El micrófono, porque su batería dura 3 horas', 'La proyección necesita enchufe y oscurecer la sala; el micrófono y el teléfono funcionan con batería.'),
        ('abc', '{F} Una persona del grupo no quiere salir en la transmisión en línea. ¿Qué decisión respeta a todas las personas?', 'No transmitir con ella, o transmitir solo audio si ella acepta', 'Transmitir igual, porque la mayoría del grupo quiere hacerlo así', 'Transmitir y ocultar su cara sin avisarle ni pedirle su opinión', 'El permiso es individual: sin su consentimiento no se la incluye.'),
        ('=', '{F} Un programa impreso para 40 personas se hace con 1 hoja por cada 2 personas. ¿Cuántas hojas se necesitan?', '40//2', 'Se divide el número de personas en grupos de dos para saber las hojas.', ' hojas'),
        ('abc', 'Un grupo dice «proyectemos todo porque es lo más moderno». ¿Qué falla en esa decisión?', 'No pregunta qué necesidad resuelve ni si cabe en las condiciones', 'Proyectar nunca puede servir a un público, ni siquiera en una sala oscura', 'Proyectar es más barato que cualquier otro medio para todo tipo de espacios', 'Un recurso se elige por la necesidad que resuelve, no por ser novedoso.'),
        ('abc', '{F} El acto se transmite en línea y la conexión falla a la mitad. ¿Qué plan B es razonable?', 'Seguir el acto con el público presente y grabar solo con permiso para compartirlo después', 'Detener el acto hasta que vuelva la conexión, sin importar el tiempo', 'Repetir la presentación completa para quienes miran en línea, sin avisar al público presente', 'El público presente no debe esperar; se sigue y se comparte una grabación con permiso.'),
        ('abc', '{F} Dos personas discuten si usar un parlante a volumen alto para la música. ¿Qué argumento cuida mejor el oído y la presentación?', 'Hacer una prueba previa y fijar un volumen moderado y estable', 'Subirlo al máximo y bajarlo después, si alguien se queja del ruido', 'No hacer pruebas, porque el volumen se ajusta solo durante el acto', 'La prueba previa permite fijar un volumen moderado y evita daños al oído.'),
        ('abc', 'Una estudiante propone proyectar la letra de una canción popular conocida. ¿Qué decisión es la más adecuada?', 'Consultar a su docente sobre los derechos y usar una letra propia o permitida', 'Copiar la letra de internet y no citar nada sobre su autoría', 'Cambiar el título y proyectarla en pantalla como si fuera propia', 'Las obras con derechos se consultan con el docente; se usa material propio o permitido.'),
        ('=', '{F} Para la proyección se necesitan 8 diapositivas de 30 segundos cada una. ¿Cuántos minutos dura la proyección?', '8*30//60', 'Se multiplican las diapositivas por 30 segundos y se pasa a minutos.', ' minutos'),
    ],
    ctx=('abc', 'Tu grupo presentará en una plaza, sin enchufes y con ruido de tránsito, ante 30 personas. ¿Qué conjunto de recursos es más viable?', 'Voz hablada, programa impreso y un parlante con batería a volumen moderado', 'Proyección de imágenes y transmisión en línea en vivo desde la plaza', 'Un equipo de sonido grande conectado a la red eléctrica del colegio', 'En un espacio sin enchufes se usan recursos sin electricidad o con batería.'),
    sc=[
        ("En Interpretación musical: ¿qué es un plan B?", "Una alternativa que se usa si un recurso falla", "El plan B evita que la presentación se detenga."),
        ('abc', 'Antes de grabar a una persona se necesita:', 'Su permiso', 'El permiso de la mayoría del curso', 'Ningún permiso si es un ensayo', 'El permiso es individual y se pide antes de grabar.'),
        ("¿Por qué se prueba la amplificación antes del acto?", "Para fijar un volumen moderado, seguro para el oído", "La prueba evita fallas y volumen excesivo."),
    ],
    op=("Con la {F}, elige tres de los cinco recursos para una presentación de tu grupo, justifica cada elección con una condición del espacio o del público, y escribe un plan B para el recurso que dependa de electricidad o de conexión.",
        "Elijo recurso 1 (programa impreso): no necesita electricidad y entrega las autorías. Elijo recurso 2 (micrófono y parlante): el gimnasio tiene eco y 40 personas. Elijo recurso 4 (grabación) con permiso, para revisar el ensayo. Plan B para el micrófono: si falla, el grupo habla despacio y el público se acerca al escenario.",
        ["elige tres recursos de la ficha", "justifica con una condición del espacio o del público", "escribe un plan B concreto", "menciona permisos o volumen moderado cuando corresponde"],
        ["hoja con tres recursos, tres razones y el plan B"],
        ["elegir por novedad", "no mencionar permisos al grabar", "olvidar el plan B"],
        "Pregunta: «¿qué pasa si falla ese recurso?». Si no tiene respuesta, pídele que escriba un plan B."),
    reinforce="Escribe una lista de cuatro recursos para presentar en una sala sin enchufes y marca los que no dependen de electricidad.",
    extend="Explica un caso en que una tecnología emergente mejore una presentación y otro en que un medio tradicional sea la mejor opción.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (piezas y reglas de programa de ejemplo, inventadas). Acto de 12 minutos en total, incluida la presentación hablada de 1 minuto y una pausa de cambio de 1 minuto entre piezas. "
     "Pieza P, canción tranquila, 3 minutos, energía baja. Pieza Q, ritmo de mesa, 2 minutos, energía alta. Pieza R, canción de ensamble, 4 minutos, energía media. Pieza S, pieza final participativa con palmas, 3 minutos, energía alta. "
     "Regla de la curva de energía: empezar con energía media o baja, subir poco a poco y terminar en energía alta. "
     "Regla de seguridad: no más de dos piezas de energía alta seguidas, para descansar la voz y las manos.")
build(
    O3, 3, F,
    use="Aprenderé a ensayar el diseño de un programa: ordenar piezas con una curva de energía, calcular el tiempo con pausas y presentación, y decidir entre opciones usando las reglas.",
    prior=["Sé describir un público y un propósito.", "Sé elegir recursos para presentar.", "Sé sumar tiempos con pausas."],
    explain=[
        "Un programa es la lista ordenada de las piezas de una presentación con su duración. El orden importa porque el público no escucha cada pieza por separado: la experiencia completa tiene una forma. Una curva de energía describe cómo sube o baja la intensidad de una pieza a otra. Una curva común empieza con energía media o baja, va subiendo y termina con energía alta, que deja al público con ganas de aplaudir.",
        "Además del orden, hay que contar el tiempo. El tiempo total se calcula sumando las duraciones de las piezas, la presentación hablada y las pausas de cambio entre piezas (por ejemplo para afinar, cambiar un instrumento o acomodar las sillas). Si el total supera el espacio disponible, se acorta una pieza, se quita una o se reduce una pausa; se cambia solo un elemento y se anota la razón.",
        "Un programa también cuida a quienes tocan y cantan. Tras una pieza muy exigente conviene una pieza de menor energía o una pausa. Las reglas se escriben antes de ordenar: tiempo total, curva de energía y cuidados. Para ensayar la decisión se comparan dos o tres órdenes y se elige el que cumple las reglas; si cambia una condición, se revisa de nuevo.",
    ],
    vocab=[("programa", "lista ordenada de piezas con su duración"), ("curva de energía", "forma en que sube o baja la intensidad de una pieza a otra"),
           ("pausa de cambio", "tiempo entre piezas para afinar, acomodar o descansar"), ("energía", "grado de intensidad y movimiento de una pieza"),
           ("transición", "paso de una pieza a la siguiente"), ("regla", "condición que el programa debe cumplir")],
    worked=[
        ("Calcular el tiempo de un programa", "Un programa de ejemplo tiene tres piezas de 2, 3 y 4 minutos, una presentación de 1 minuto y 2 pausas de cambio de 1 minuto cada una. ¿Cuántos minutos dura en total?",
         ["Las piezas suman 2 + 3 + 4 = 9 minutos.", "A eso se suman la presentación (1) y las pausas (2 × 1 = 2): 9 + 1 + 2 = 12 minutos."],
         "12 minutos"),
        ("Revisar una curva de energía", "Un orden de ejemplo es: alta, alta, alta, baja. ¿Cumple una curva que termina en energía alta y no tiene más de dos piezas altas seguidas?",
         ["Termina en energía baja, no alta: no cumple la curva.", "Además tiene tres piezas altas seguidas: tampoco cumple la regla de cuidado."],
         "No cumple ninguna de las dos reglas"),
    ],
    mistakes=[("Ordenar las piezas por el gusto del grupo sin pensar en la curva.", "No se considera cómo escucha el público el conjunto.", "Escribe la energía de cada pieza y ordénalas con una curva."),
              ("No contar las pausas de cambio en el tiempo total.", "Las pausas parecen sin importancia, pero suman minutos.", "Suma piezas, presentación y pausas antes de comparar con el tiempo permitido.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una curva de energía?', 'La forma en que sube o baja la intensidad de una pieza a otra', 'La lista de instrumentos que participa en cada pieza del programa', 'La cantidad de personas que aplaude al terminar cada pieza', 'La curva de energía describe cómo cambia la intensidad a lo largo del programa.'),
        ('abc', '{F} ¿Cuántos minutos dura la pieza R?', '4 minutos', '3 minutos', '2 minutos', 'La ficha asigna 4 minutos a la pieza R, la canción de ensamble.'),
        ('abc', '{F} ¿Qué energía tiene la pieza P?', 'Baja', 'Media', 'Alta', 'La pieza P es una canción tranquila de energía baja.'),
        ('=', '{F} ¿Cuántos minutos suman las cuatro piezas P, Q, R y S?', '3+2+4+3', 'Se suman las duraciones de las cuatro piezas de la ficha.', ' minutos'),
        ('abc', '{F} ¿Qué orden cumple la regla de empezar con energía baja o media y terminar en alta?', 'P, R, Q, S', 'S, Q, R, P', 'Q, S, P, R', 'P (baja) y R (media) abren, y Q y S (altas) cierran la curva.'),
        ('abc', '{F} El orden P, Q, S, R termina en una pieza de energía media. ¿Qué regla incumple?', 'La curva de energía, porque no termina en alta', 'La regla de seguridad, porque tiene tres piezas altas seguidas', 'Ninguna, porque todas las piezas están en el programa', 'La curva pide terminar en energía alta, y R es de energía media.'),
        ('=', '{F} Con las cuatro piezas, la presentación de 1 minuto y 3 pausas de cambio de 1 minuto cada una, ¿cuántos minutos dura el acto?', '3+2+4+3+1+3*1', 'Se suman las piezas, la presentación y las tres pausas entre las cuatro piezas.', ' minutos'),
        ('abc', '{F} El acto permite 12 minutos. ¿Cuál es la situación del programa completo de cuatro piezas?', 'Dura 16 minutos y se pasa por 4 minutos', 'Dura 12 minutos y cabe justo', 'Dura 14 minutos y se pasa por 2 minutos', 'Piezas 12 más presentación 1 y tres pausas 3 suman 16 minutos, o sea 4 más de lo permitido.'),
        ('abc', '{F} Para que el acto no pase de 12 minutos, se quita una sola pieza con su pausa y se conserva la curva de energía. ¿Qué pieza se quita?', 'La pieza R, con lo que el acto dura 11 minutos', 'La pieza S, con lo que el acto dura 12 minutos', 'La pieza Q, con lo que el acto dura 13 minutos', 'Quitar S termina en energía media y quitar Q deja 13 minutos; solo quitar R cabe y conserva la curva.'),
        ('abc', '{F} Un grupo ordena Q, S, P, R. ¿Qué problema tiene el programa?', 'Dos piezas de energía alta al inicio y una curva que no sube hacia el final', 'Tres piezas altas seguidas y ninguna pieza de energía media', 'Ninguno, porque las duraciones de las piezas coinciden con el tiempo', 'Q y S son altas al inicio y la curva no cierra en alta; además no es la curva pedida.'),
        ('abc', '{F} Tras la pieza S, que es participativa y exigente, el grupo tiene que cantar otra pieza. ¿Qué decisión cuida mejor las voces?', 'Hacer una pausa breve o poner una pieza de energía baja', 'Encadenar otra pieza de energía alta sin pausa de descanso para las voces', 'Cantar más fuerte para compensar el cansancio de la pieza anterior', 'Tras una pieza exigente se descansa o se baja la energía para cuidar la voz.'),
        ('abc', '{F} El público cambia: ahora son personas mayores que prefieren programas más tranquilos. ¿Qué revisión mantiene las reglas pero adapta el programa?', 'Reemplazar la pieza Q por otra de energía media y mantener un final alto suave', 'Mantener el programa igual, porque las reglas del acto no se revisan nunca', 'Quitar toda la energía del programa y terminar sin ninguna pieza alta ni final', 'Se revisa la elección con el nuevo público: se baja la energía de una pieza y se conserva la forma.'),
        ('=', '{F} Si se saca la pieza Q y la pausa de cambio que la sigue, ¿cuántos minutos dura ahora el programa de las tres piezas restantes, con presentación de 1 minuto y 2 pausas de 1 minuto?', '3+4+3+1+2*1', 'Se suman las tres piezas que quedan, la presentación y las dos pausas.', ' minutos'),
    ],
    ctx=('abc', 'Tu grupo tiene 10 minutos en una feria del liceo y quiere presentar las piezas Q, R y S, con una presentación de 1 minuto y 2 pausas de 1 minuto. ¿Qué decisión es la correcta?', 'Recortar, porque todo dura 12 minutos y se pasa', 'Aceptar el programa, porque las piezas suman 9 minutos y caben', 'Aceptar el programa, porque las pausas no cuentan en el tiempo', 'Q, R y S suman 9 minutos, más presentación 1 y pausas 2, que dan 12; hay que recortar.'),
    sc=[
        ("En Interpretación musical: ¿qué es una pausa de cambio?", "El tiempo entre piezas para afinar, acomodar o descansar", "La pausa de cambio ocupa minutos del programa."),
        ('abc', 'Una curva de energía común termina en:', 'Energía alta', 'Silencio total', 'Energía baja siempre', 'Terminar en alta deja al público con ganas de aplaudir.'),
        ("¿Por qué se cuenta la presentación hablada en el tiempo total?", "Porque ocupa minutos del espacio disponible", "El tiempo total incluye presentación, piezas y pausas."),
    ],
    op=("Con la {F}, arma un programa con las piezas P, Q, R y S (puedes quitar una) que cumpla las reglas de curva de energía, no más de dos piezas altas seguidas y 12 minutos en total con presentación y pausas. Escribe el orden, los minutos y por qué cumple.",
        "Programa: P, Q, S. Curva: baja, alta, alta (empieza en baja, termina en alta y hay solo dos piezas altas seguidas). Piezas: 3 + 2 + 3 = 8 minutos; con presentación de 1 minuto y 2 pausas de 1 minuto: total 11 minutos, que cabe en 12.",
        ["escribe el orden de las piezas", "calcula el tiempo con presentación y pausas", "verifica la curva y las dos piezas altas seguidas", "justifica que cumple las reglas"],
        ["hoja con el orden, los cálculos y la justificación"],
        ["no contar pausas", "poner tres piezas altas seguidas", "no justificar con las reglas"],
        "Pregunta: «¿cuántos minutos suma todo con pausas y presentación?». Si no lo calcula, pídele que lo escriba paso a paso."),
    reinforce="Ordena cuatro piezas inventadas con su energía para que cumplan una curva que sube y calcula el tiempo con pausas.",
    extend="Explica cómo cambiarías la curva de energía si el público fuera un grupo de niñas y niños pequeños.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (guion y roles de producción de ejemplo, inventados) para un acto de 10 minutos. "
     "Roles: presentadora, que habla antes de cada pieza; encargado de tiempo, que usa un reloj y avisa los cambios; encargada de sonido, que prueba el micrófono y el parlante antes del acto; "
     "acomodador, que recibe al público y reparte el programa. Todas las personas del grupo tocan o cantan además de su rol. "
     "Guion: saludo e idea de la presentación, 30 segundos; presentación de la primera pieza, 20 segundos; presentación de la segunda pieza, 20 segundos; cierre y agradecimiento, 30 segundos. "
     "Piezas: la primera dura 3 minutos y la segunda 4 minutos y 20 segundos. "
     "Regla: el micrófono se prueba a volumen moderado, 10 minutos antes del acto, con dos personas en el fondo para comprobar que se oye.")
build(
    O3, 4, F,
    use="Aprenderé a gestionar una presentación: repartir roles de producción, escribir un guion breve con tiempos y preparar una lista de verificación del día, cuidando el volumen y la seguridad.",
    prior=["Sé armar un programa con tiempos.", "Sé elegir recursos para presentar.", "Sé que los permisos y el volumen se cuidan."],
    explain=[
        "Gestionar una presentación es organizar a las personas, el tiempo y los recursos para que ocurra tal como se diseñó. Además de tocar o cantar, alguien debe presentar las piezas, controlar el tiempo, probar el sonido y recibir al público. Estos son los roles de producción. En un grupo pequeño una persona puede tener dos roles, pero se anota quién hace qué para que nada se olvide.",
        "El guion es el texto breve de lo que se dice entre piezas. Un buen guion nombra la idea de la presentación, el título y autoría de cada pieza, y un dato del proceso (cómo se trabajó o por qué se eligió). Cada intervención se escribe con su duración, de modo que quepa en el tiempo. Se habla con voz clara, pausada y a volumen cómodo; una presentación hablada de 20 segundos tiene unas 40 a 50 palabras.",
        "La lista de verificación es una lista corta de cosas que se comprueban antes del acto: sonido probado, programas listos, sillas, luz, plan B, agua para la voz, calentamiento hecho. Se revisa antes de empezar y se tacha cada punto. Con ella, la presentación no depende de la memoria de nadie. Si algo falla, se aplica el plan B con calma y se sigue.",
    ],
    vocab=[("rol de producción", "tarea que organiza la presentación, como el tiempo o el sonido"), ("guion", "texto breve de lo que se dice entre piezas, con sus tiempos"),
           ("lista de verificación", "lista de comprobaciones antes del acto, que se van tachando"), ("intervención", "cada momento en que alguien habla al público"),
           ("prueba de sonido", "comprobación del micrófono y el parlante antes del acto"), ("agradecimiento", "palabras de cierre que reconocen a quienes colaboraron")],
    worked=[
        ("Sumar el guion", "Un guion de ejemplo tiene un saludo de 40 segundos, dos presentaciones de 25 segundos cada una y un cierre de 35 segundos. ¿Cuántos segundos habla la presentadora en total?",
         ["Las dos presentaciones suman 25 + 25 = 50 segundos.", "Con el saludo y el cierre: 40 + 50 + 35 = 125 segundos."],
         "125 segundos"),
        ("Asignar roles", "Un grupo de tres personas debe cubrir cuatro roles de producción y todas tocan. ¿Qué decisión es razonable?",
         ["Hay un rol más que personas: alguien debe tener dos roles.", "Se reparte para que no se sobrecargue a una sola persona y se anota quién hace qué."],
         "Una persona tiene dos roles, repartidos con cuidado y anotados"),
    ],
    mistakes=[("Dejar los roles «para ver quién lo hace el día del acto».", "Sin responsables, se olvidan tareas como probar el sonido.", "Escribe quién hace qué y revisa la lista antes de empezar."),
              ("Escribir un guion sin tiempos.", "No se sabe si cabe en el espacio.", "Anota los segundos de cada intervención y suma el total.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es una lista de verificación?', 'Una lista de comprobaciones antes del acto, que se van tachando', 'Una lista de todas las canciones que el grupo sabe tocar y ha tocado antes', 'Una lista de las personas que asistieron al acto de cierre del liceo, con su firma', 'La lista de verificación evita olvidos antes del acto; no es un repertorio ni una asistencia.'),
        ('abc', '{F} ¿Qué hace la encargada de sonido?', 'Prueba el micrófono y el parlante antes del acto', 'Usa un reloj y avisa los cambios de pieza durante el acto', 'Recibe al público en la puerta y reparte el programa', 'La ficha asigna la prueba de sonido a la encargada de sonido.'),
        ('abc', '{F} ¿Cuándo se prueba el micrófono?', '10 minutos antes del acto, a volumen moderado', 'Al comenzar la primera pieza, a todo volumen', 'El día anterior, sin repetirlo antes del acto', 'La regla de la ficha dice 10 minutos antes y a volumen moderado.'),
        ('=', '{F} ¿Cuántos segundos habla la presentadora en total según el guion?', '30+20+20+30', 'Se suman las cuatro intervenciones del guion con sus segundos.', ' s'),
        ('abc', '{F} ¿Qué rol vigila los tiempos del acto?', 'El encargado de tiempo', 'La presentadora que habla antes de cada pieza', 'El acomodador que recibe al público', 'El encargado de tiempo usa un reloj y avisa los cambios.'),
        ('=', '{F} La segunda pieza dura 4 minutos y 20 segundos. ¿Cuántos segundos son?', '4*60+20', 'Se pasan los minutos a segundos y se suman los 20 segundos.', ' s'),
        ('=', '{F} ¿Cuántos segundos dura todo el acto, sumando las dos piezas (la primera de 3 minutos) y las cuatro intervenciones del guion?', '180+260+100', 'La primera pieza dura 180 segundos, la segunda 260 y el guion 100 segundos en total.', ' s'),
        ('abc', '{F} El acto es de 10 minutos y dura 9 minutos con el guion. ¿Qué se puede decir?', 'Cabe, y sobra 1 minuto para cambios', 'Se pasa por 1 minuto y hay que recortar el guion', 'Cabe justo y no sobra nada de tiempo para los cambios', 'Nueve minutos caben en diez y dejan un minuto para cambios o imprevistos.'),
        ('abc', '{F} Una persona del grupo no puede ir el día del acto y era la encargada de sonido. ¿Qué decisión conserva el plan?', 'Reasignar el rol a otra persona y avisarle con anticipación', 'Dejar el sonido sin responsable y hacerlo al final, si hay tiempo', 'Cancelar el acto porque falta una persona del grupo de producción', 'Se reasigna el rol con tiempo y se registra, así no se olvida la prueba de sonido.'),
        ('abc', '{F} El guion tiene una intervención de 20 segundos. ¿Cuántas palabras caben aproximadamente a un ritmo pausado?', 'Entre 40 y 50 palabras', 'Más de 200 palabras, leídas con rapidez', 'Menos de 5 palabras, sin pausas', 'Según la explicación, unas 40 a 50 palabras caben en 20 segundos con ritmo pausado.'),
        ('abc', '{F} Durante la prueba de sonido, el parlante suena muy fuerte y duele el oído. ¿Qué decisión es correcta?', 'Bajar el volumen y volver a probar con las dos personas en el fondo', 'Dejarlo así, porque el público oirá mejor si el volumen es alto', 'Probarlo solo con el micrófono apagado y el parlante lejos del público', 'Un volumen que duele no es seguro; se baja y se comprueba que igual se oiga al fondo.'),
        ('abc', 'Un grupo escribe en su lista: «ver cómo sale todo». ¿Qué problema tiene ese punto?', 'No dice qué comprobar, quién lo hace ni cuándo', 'Tiene demasiadas palabras para ser un punto de una lista corta', 'Reemplaza el guion de la presentación que se dice entre piezas', 'Un punto de verificación debe ser concreto, con responsable y momento.'),
        ('=', '{F} Si se suman 40 segundos de pausas de cambio al acto de 9 minutos, ¿cuántos segundos dura todo?', '9*60+40', 'Se pasan los 9 minutos a segundos y se suman las pausas.', ' s'),
    ],
    ctx=('abc', 'Faltan 5 minutos para empezar y el micrófono hace un ruido molesto. ¿Qué decisión es la más adecuada?', 'Pasar al plan B: hablar sin micrófono si el público es pequeño y avisar al grupo', 'Insistir con el micrófono al máximo para tapar el ruido y seguir igual', 'Suspender el acto sin avisar al público ni al resto del grupo', 'Con plan B el acto sigue con calma y sin volumen excesivo.'),
    sc=[
        ("En Interpretación musical: ¿qué es un guion de presentación?", "Un texto breve de lo que se dice entre piezas, con sus tiempos", "Un guion lleva títulos, autorías y duración de cada intervención."),
        ('abc', 'Un rol de producción es:', 'Una tarea que organiza la presentación, como controlar el tiempo', 'Una pieza que se toca en el acto de cierre del liceo', 'Un permiso para grabar el acto entregado por la dirección', 'Los roles de producción se suman a tocar o cantar.'),
        ("¿Por qué se tacha cada punto de la lista de verificación?", "Para comprobar que nada se olvidó antes de empezar", "Marcar cada punto evita depender de la memoria."),
    ],
    op=("Con la {F}, escribe un guion de cuatro intervenciones para un acto de tu grupo, con la duración de cada una, y una lista de verificación de cinco puntos con responsable. Suma los segundos del guion.",
        "Guion: saludo e idea, 20 s; primera pieza «canción tranquila», 20 s; segunda pieza «ritmo de mesa», 20 s; cierre y agradecimiento, 30 s: total 90 s. Lista: sonido probado (encargada de sonido); programas listos (acomodador); reloj y tiempos (encargado de tiempo); agua y calentamiento (todo el grupo); plan B (presentadora).",
        ["escribe cuatro intervenciones con tiempos", "suma los segundos del guion", "arma cinco puntos concretos de verificación con responsable", "incluye el plan B y el cuidado de la voz"],
        ["hoja con el guion, la suma y la lista de verificación"],
        ["guion sin tiempos", "puntos de la lista sin responsable", "no sumar los segundos"],
        "Pregunta: «¿quién comprueba ese punto y cuándo?». Si no lo dice, pídele que lo agregue."),
    reinforce="Escribe tres puntos de verificación para una presentación de un trío y asigna un responsable a cada uno.",
    extend="Explica cómo cambiarían los roles de producción si el acto se hiciera en una sala tan pequeña que no necesita micrófono.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (ensayo general de ejemplo, inventado) de un grupo con un acto de 10 minutos como máximo. "
     "Tiempos previstos y reales, en segundos: saludo, previsto 30, real 45; primera pieza, previsto 180, real 190; cambio, previsto 30, real 60; segunda pieza, previsto 260, real 255; cierre, previsto 30, real 35. "
     "Observaciones: el micrófono se apagó durante el saludo; en el cambio faltó acomodar una silla; la segunda pieza sonó equilibrada; el público de prueba (dos personas al fondo) oyó bien la voz hablada. "
     "Regla del grupo: se cambia un solo elemento por ensayo y se anota la razón. Se ensaya a volumen moderado y con una pausa de silencio entre las dos pasadas.")
build(
    O3, 5, F,
    use="Aprenderé a registrar y ajustar una presentación a partir de un ensayo general: comparar tiempos previstos y reales, detectar fallos y decidir un ajuste cambiando un solo elemento.",
    prior=["Sé armar un guion con tiempos.", "Sé llevar una bitácora de ensayo.", "Sé que ensayar tiene pausas y volumen moderado."],
    explain=[
        "El ensayo general es una pasada completa de la presentación en las condiciones más parecidas posibles al día real: con guion, cambios, recursos y público de prueba. No sirve para ensayar de nuevo cada pieza, sino para comprobar cómo funciona el conjunto. Se cronometra cada tramo y se anotan las observaciones: qué falló, qué sonó bien, qué se demoró.",
        "Para registrar, se arma una tabla con el tiempo previsto y el tiempo real de cada tramo y se calcula la diferencia. Una diferencia positiva significa que el tramo se alargó; una negativa, que se acortó. El total real se compara con el máximo permitido. También se anotan los fallos no medibles, como un micrófono que se apaga o una silla que faltó.",
        "El ajuste se decide con los datos: se busca el tramo con la mayor diferencia y el fallo más importante, y se cambia un solo elemento, por ejemplo acortar el guion del saludo o ensayar el cambio con las sillas ya puestas. Se anota la razón y se comprueba en el próximo ensayo. Si el ensayo cansa a alguien, se baja el número de pasadas; descansar también es un ajuste.",
    ],
    vocab=[("ensayo general", "pasada completa de la presentación en condiciones parecidas a las reales"), ("previsto", "tiempo planificado de un tramo"), ("real", "tiempo medido en el ensayo de un tramo"),
           ("diferencia", "resta entre el tiempo real y el previsto de un tramo"), ("público de prueba", "personas que escuchan el ensayo para opinar"), ("observación", "nota de algo que falló o funcionó")],
    worked=[
        ("Calcular una diferencia", "En un ensayo de ejemplo, una intervención se previó de 20 segundos y duró 35. ¿Cuál es la diferencia y qué significa?",
         ["Se resta el tiempo previsto al real: 35 − 20 = 15 segundos.", "La diferencia es positiva: el tramo se alargó 15 segundos."],
         "+15 segundos: el tramo se alargó"),
        ("Elegir un ajuste", "Un ensayo mostró que el cambio entre piezas duró 60 segundos en vez de 30, porque había que mover sillas. ¿Qué ajuste cambia un solo elemento?",
         ["El problema es la demora del cambio por mover sillas.", "Se ensaya el cambio con las sillas ya puestas o con una persona a cargo, y no se toca nada más."],
         "Dejar las sillas listas antes del acto, sin cambiar otros elementos"),
    ],
    mistakes=[("Corregir todos los fallos del ensayo a la vez.", "No se sabe qué ajuste resolvió cada problema.", "Elige el fallo más importante y cambia un solo elemento."),
              ("Medir los tiempos con una estimación «a ojo».", "No permite comparar con lo previsto.", "Cronometra cada tramo y anota los segundos.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es un ensayo general?', 'Una pasada completa de la presentación en condiciones parecidas a las reales', 'Un ensayo en que cada integrante practica su parte sin los demás, en su casa', 'Una prueba escrita sobre la teoría de la música y sus símbolos', 'El ensayo general prueba el conjunto con tiempos y recursos, no cada parte por separado.'),
        ('abc', '{F} ¿Cuántos segundos duró realmente el cambio entre piezas?', '60 segundos', '30 segundos', '45 segundos', 'La ficha indica que el cambio duró 60 segundos, el doble de lo previsto.'),
        ('abc', '{F} ¿Qué falló durante el saludo?', 'El micrófono se apagó', 'Faltó una silla', 'La voz no se oyó al fondo', 'La observación de la ficha dice que el micrófono se apagó durante el saludo.'),
        ('=', '{F} ¿Cuál es la diferencia entre el tiempo real y el previsto del saludo?', '45-30', 'Se resta el tiempo previsto al real del saludo, según la tabla.', ' s'),
        ('=', '{F} ¿Cuántos segundos duraron realmente las dos piezas juntas?', '190+255', 'Se suman los tiempos reales de la primera y la segunda pieza.', ' s'),
        ('abc', '{F} ¿Qué tramo se acortó respecto de lo previsto?', 'La segunda pieza, que duró 255 en vez de 260 segundos', 'La primera pieza, que duró 190 en vez de 180 segundos', 'El cambio, que duró 60 en vez de 30 segundos', 'Solo la segunda pieza duró menos que lo previsto; los demás tramos se alargaron.'),
        ('=', '{F} ¿Cuántos segundos duró el ensayo completo, sumando los cinco tramos reales?', '45+190+60+255+35', 'Se suman los cinco tiempos reales de la tabla de la ficha.', ' s'),
        ('abc', '{F} El máximo del acto es de 10 minutos, o sea 600 segundos. ¿Qué se puede decir del ensayo?', 'Cabe, porque 585 segundos están dentro de los 600 permitidos', 'Se pasa, porque 585 segundos superan los 600 segundos permitidos', 'No se puede saber nada sin hacer otro ensayo mucho más largo', 'El total real de 585 segundos está por debajo de 600, así que cabe y sobran 15.'),
        ('abc', '{F} El tramo con la mayor diferencia positiva es el cambio, con 30 segundos de más. ¿Qué ajuste cambia un solo elemento?', 'Ensayar el cambio con las sillas ya acomodadas', 'Acortar las dos piezas y cambiar el guion a la vez', 'Quitar el cierre y el saludo del programa', 'El problema del cambio se ataca con un ajuste concreto y único: acomodar las sillas antes.'),
        ('abc', '{F} Un grupo decide acortar el saludo, cambiar el tempo de la primera pieza y reubicar las sillas, todo en el mismo ensayo. ¿Qué falla?', 'No se sabrá cuál ajuste resolvió cada problema', 'Los tiempos previstos dejan de tener sentido para siempre', 'Nada, porque más cambios mejoran más rápido', 'La regla del grupo es cambiar un elemento por ensayo, para atribuir los resultados.'),
        ('abc', '{F} El micrófono se apagó durante el saludo. ¿Cuál es el mejor siguiente paso?', 'Revisar la batería y probarlo de nuevo, con un plan B de voz sin micrófono', 'Aumentar el volumen del parlante para el próximo ensayo y ver si se apaga', 'Quitar el saludo del acto para evitar el problema del micrófono', 'Se revisa la causa y se define un plan B; subir el volumen no resuelve un apagón.'),
        ('abc', '{F} Dos personas dicen sentirse cansadas tras el ensayo general, que tuvo dos pasadas seguidas. ¿Qué decisión de ajuste es adecuada?', 'Hacer una sola pasada y una pausa de silencio, y revisar el cansancio', 'Hacer tres pasadas seguidas para acostumbrarse más al esfuerzo', 'Pedirles que no avisen cuando estén cansadas para no atrasar al grupo', 'Descansar y reducir pasadas es un ajuste válido y cuida a las personas.'),
        ('=', '{F} ¿Cuántos segundos más largo que lo previsto fue el ensayo completo? El total previsto es 30 + 180 + 30 + 260 + 30 = 530.', '45+190+60+255+35-530', 'Se resta el total previsto al total real para ver cuánto se alargó el ensayo.', ' s'),
    ],
    ctx=('abc', 'En el ensayo general de tu grupo una pieza duró 3 minutos y 10 segundos y estaba prevista de 3 minutos. ¿Qué anotas en el registro?', 'Previsto 180 s, real 190 s, diferencia de +10 s', 'Previsto 190 s, real 180 s, diferencia de −10 s', 'Previsto 180 s, real 190 s, diferencia de −10 s', 'La diferencia real menos previsto es 190 − 180 = +10 segundos.'),
    sc=[
        ("En Interpretación musical: ¿qué es la diferencia entre tiempo real y previsto?", "La resta entre el tiempo real y el previsto de un tramo", "Una diferencia positiva significa que el tramo se alargó."),
        ('abc', 'Después de un ensayo general, conviene:', 'Cambiar un solo elemento y anotar la razón', 'Cambiar todo el programa para empezar de cero en cada ensayo', 'No registrar nada para ahorrar tiempo en el siguiente ensayo', 'Un ajuste único permite saber qué lo resolvió.'),
        ("¿Por qué se anotan los fallos aunque no se midan en segundos?", "Porque ayudan a decidir el ajuste más importante", "Un micrófono apagado se anota aunque no tenga un tiempo."),
    ],
    op=("Con la {F}, escribe el registro del ensayo general: la diferencia de cada tramo (real menos previsto), el total real y si cabe en 600 segundos. Después elige un solo ajuste para el siguiente ensayo, con su razón y cómo comprobarás que funcionó.",
        "Diferencias: saludo +15, primera pieza +10, cambio +30, segunda pieza −5, cierre +5. Total real: 585 s; cabe en 600. Ajuste: ensayar el cambio con las sillas ya acomodadas, porque es la mayor diferencia. Comprobación: cronometrar el cambio en el próximo ensayo y ver si baja de 60 a unos 30 segundos.",
        ["calcula las cinco diferencias", "suma el total real y lo compara con 600", "elige un solo ajuste y da la razón", "dice cómo comprobar el resultado"],
        ["hoja con la tabla de diferencias, el total y el ajuste"],
        ["restar al revés", "proponer varios ajustes a la vez", "no decir cómo comprobar"],
        "Pregunta: «¿qué tramo tuvo la mayor diferencia?». Si no la encuentra, pídele que calcule cada resta."),
    reinforce="Inventa una tabla de cuatro tramos con tiempos previstos y reales, calcula las diferencias y elige un ajuste.",
    extend="Explica por qué un ensayo general con público de prueba aporta información que un ensayo sin público no entrega.",
)

# ============================================================ OAC-03, clase 6
F = ("Ficha 6 (comentarios y decisiones tras un acto de ejemplo, inventados). Un grupo presentó dos piezas ante 40 personas. "
     "Hoja de comentarios del público, con dos preguntas: «¿qué parte te gustó y por qué?» y «¿qué cambiarías?». "
     "Respuestas de ejemplo: persona 1, «me gustó la segunda pieza porque el ritmo se oía claro»; persona 2, «estuvo bueno»; persona 3, «cambiaría el saludo, fue muy largo, duró casi un minuto»; persona 4, «la voz hablada se oyó bien al fondo». "
     "Cifras de ejemplo: de 40 personas, 30 respondieron la hoja. "
     "Difusión propuesta: publicar un breve texto del proceso, con el nombre del grupo y los títulos de las piezas, sin datos personales ni imágenes de otras personas; el video se comparte solo con quienes aceptaron aparecer. "
     "Pauta de evaluación de la presentación: (1) cumple el propósito; (2) cabe en el tiempo; (3) el público oye bien; (4) el proceso se comunica con claridad.")
build(
    O3, 6, F,
    use="Aprenderé a evaluar una presentación con comentarios del público y una pauta, a comunicar el proceso con claridad y a decidir cómo difundirla con respeto por los permisos y la autoría.",
    prior=["Sé armar un programa, un guion y un ensayo general.", "Sé que grabar o difundir requiere permiso.", "Sé evaluar con una pauta y con evidencia."],
    explain=[
        "Después de presentar se evalúa. La evaluación de una presentación junta tres fuentes: los comentarios del público, los datos medidos (como el tiempo) y la mirada del propio grupo. Una hoja de comentarios con dos o tres preguntas abiertas y claras, como «¿qué parte te gustó y por qué?» y «¿qué cambiarías?», entrega información más útil que un simple «estuvo bueno». Se clasifican las respuestas: las que dan evidencia (dicen qué y por qué) valen más que las que solo opinan.",
        "Comunicar el proceso significa contarle al público y a otras personas cómo se llegó a la interpretación: qué se decidió, qué se probó, qué se ajustó y por qué. Un texto breve de proceso nombra el propósito, dos decisiones, un ajuste con su razón y un resultado. Sirve para aprender y para que otras personas comprendan el trabajo, no para presumir.",
        "Difundir es compartir con más personas, y se hace con cuidado: se pide permiso a cada persona que aparece, no se publican datos personales, se cita la autoría de las obras y se evita mostrar a quienes no participaron. Si una persona se siente incómoda con una imagen o comentario, se retira y se avisa a una persona adulta de confianza. Con lo aprendido se decide qué conservar y qué cambiar en la próxima presentación.",
    ],
    vocab=[("hoja de comentarios", "formulario breve donde el público opina con preguntas claras"), ("evidencia", "dato o razón concreta que apoya una opinión"), ("comunicar el proceso", "contar qué se decidió, probó y ajustó, y por qué"),
           ("difundir", "compartir la presentación con más personas"), ("autoría", "reconocimiento de quién creó cada obra o texto"), ("permiso", "aceptación libre de una persona para aparecer o ser grabada")],
    worked=[
        ("Clasificar comentarios", "Un público de ejemplo escribe: (a) «estuvo bueno»; (b) «el saludo fue largo: duró casi un minuto». ¿Cuál comentario da evidencia?",
         ["El comentario (a) solo opina: no dice qué parte ni por qué.", "El comentario (b) dice qué parte (el saludo) y un dato comprobable (casi un minuto): da evidencia."],
         "El comentario (b)"),
        ("Decidir una difusión", "Un grupo quiere publicar el video del acto, pero una persona no quiso salir. ¿Qué decisión respeta a todas?",
         ["El permiso es individual: sin su aceptación no se la incluye.", "Se publica solo con quienes aceptaron, o se comparte solo el audio si todos aceptan."],
         "Publicar solo con quienes aceptaron, sin incluir a quien dijo que no"),
    ],
    mistakes=[("Contar solo los comentarios que elogian.", "Se pierde información para mejorar.", "Lee todos los comentarios y clasifica los que dan evidencia, sean elogios o sugerencias."),
              ("Publicar imágenes de personas del público porque «era un lugar público».", "Cada persona tiene derecho a decidir sobre su imagen.", "Pide permiso o no muestres a quienes no participaron.")],
    T=[
        ('abc', 'En Interpretación musical: ¿qué es comunicar el proceso?', 'Contar qué se decidió, probó y ajustó en el trabajo, y por qué', 'Anunciar el título de las piezas antes de tocarlas en un acto', 'Escribir los nombres de todas las personas que asistieron', 'Comunicar el proceso es explicar decisiones y ajustes; no es solo anunciar títulos.'),
        ('abc', '{F} ¿Cuántas personas respondieron la hoja de comentarios?', '30 personas', '40 personas', '4 personas', 'La ficha dice que de 40 personas, 30 respondieron la hoja.'),
        ('abc', '{F} ¿Qué comentario da evidencia sobre una parte de la presentación?', 'El de la persona 3, que dice que el saludo duró casi un minuto', 'El de la persona 2, que dice que estuvo bueno y nada más', 'Ninguno de los cuatro comentarios, porque todos son opiniones', 'La persona 3 nombra una parte y un dato comprobable; la persona 2 solo opina.'),
        ('=', '{F} ¿Qué porcentaje de las 40 personas respondió la hoja? (30 de 40 respondieron.)', '30*100//40', 'Se divide el número de respuestas por el total de personas y se multiplica por 100.', ' %'),
        ('abc', '{F} ¿Qué comentario de la persona 4 se puede registrar como logro?', 'La voz hablada se oyó bien al fondo', 'El saludo fue demasiado largo para el acto', 'El ritmo se oyó poco claro en la segunda pieza', 'La persona 4 dice que la voz hablada se oyó bien al fondo.'),
        ('abc', '{F} ¿A qué criterio de la pauta apunta el comentario de la persona 3 sobre el saludo?', 'Al criterio 2, que el acto quepa en el tiempo', 'Al criterio 1, que cumpla el propósito', 'Al criterio 4, que el proceso se comunique con claridad', 'Un saludo largo tiene que ver con el tiempo del acto, o sea el criterio 2.'),
        ('=', '{F} Si el saludo previsto era de 30 segundos y duró casi 60, ¿cuántos segundos más duró?', '60-30', 'Se resta el tiempo previsto al tiempo real para obtener la diferencia.', ' s'),
        ('abc', '{F} El grupo quiere decidir qué cambiar. ¿Qué dato usa como evidencia?', 'El comentario de la persona 3 sobre el saludo y el tiempo del acto', 'El comentario de la persona 2, que no explica nada concreto del acto', 'La cantidad de sillas que había en la sala de la presentación', 'La persona 3 da una evidencia concreta de algo que cambiar.'),
        ('abc', '{F} ¿Qué texto comunica bien el proceso?', 'Propósito: calmar al público; decisión: bajar la fuerza al entrar la voz; ajuste: acortar el saludo; resultado: el acto cupo en el tiempo', 'Fue un acto muy bonito y todas las personas del grupo lo pasaron bien en el escenario', 'Tocamos dos piezas, nos aplaudieron mucho y nos fuimos a casa contentos', 'Un buen texto de proceso nombra propósito, decisión, ajuste y resultado.'),
        ('abc', '{F} Una persona del público dice que le incomodó verse en el video que el grupo compartió. ¿Qué decisión es correcta?', 'Retirar el video, disculparse y avisar a una persona adulta de confianza', 'Dejarlo publicado, porque ya lo vieron muchas personas y no se puede borrar', 'Pedirle que no vuelva a opinar sobre los videos del grupo en el futuro', 'Respetar el malestar de la persona y retirar su imagen es parte del permiso y del buen trato.'),
        ('abc', '{F} El grupo piensa publicar el texto del proceso con el nombre completo y la dirección de cada integrante. ¿Qué falla en esa propuesta?', 'Incluye datos personales que no son necesarios', 'No cita los títulos de las piezas ni el nombre del grupo', 'Es demasiado corto para ser un texto de proceso del grupo', 'La propuesta de la ficha excluye datos personales; publicarlos expone a las personas sin necesidad.'),
        ('abc', 'Un grupo interpreta que, como solo 30 de 40 personas respondieron, «nadie quiere opinar». ¿Qué falla en esa conclusión?', 'Que 30 de 40 es la mayoría y sí da información suficiente para decidir', 'Que 30 respuestas son demasiadas para leerlas una por una en el grupo', 'Una hoja de comentarios solo sirve si responde el 100 % del público', 'Más de la mitad respondió, así que hay información suficiente para decidir.'),
        ('=', '{F} Si la próxima vez el grupo reparte la hoja a 40 personas y espera que respondan 36, ¿cuántas respuestas más que ahora serían?', '36-30', 'Se restan las respuestas actuales a las esperadas.', ' respuestas'),
    ],
    ctx=('abc', 'Tu grupo grabó una pieza que tocó una compañera ajena al grupo, invitada solo ese día. Quieren publicarla. ¿Qué decisión es adecuada?', 'Pedirle permiso a ella y citar su nombre solo si lo acepta', 'Publicarla igual, porque la pieza era del grupo y ella la tocó para el curso', 'Publicarla sin su nombre para no pedir ningún permiso a nadie', 'El permiso es de cada persona que aparece, aunque colabore solo un día.'),
    sc=[
        ("En Interpretación musical: ¿qué es un comentario con evidencia?", "Uno que dice qué parte y por qué, con un dato o razón concreta", "Un comentario con evidencia permite decidir un cambio."),
        ('abc', 'Antes de publicar un video, el grupo:', 'Pide permiso a cada persona que aparece', 'Publica y pregunta después si alguien se molestó', 'Pide permiso solo a la persona que lo grabó', 'El permiso es individual y previo.'),
        ("¿Qué haces si una persona se siente incómoda con una imagen o un comentario publicado?", "Lo retiro y aviso a una persona adulta de confianza", "Respetar la incomodidad y pedir apoyo es lo correcto."),
    ],
    op=("Con la {F}, escribe: (1) cuál de los cuatro comentarios usarías como evidencia para mejorar y por qué; (2) un texto de proceso de cuatro frases (propósito, decisión, ajuste y resultado); (3) una decisión de difusión que respete permisos y datos personales.",
        "(1) Usaría el de la persona 3, porque dice qué parte (el saludo) y un dato (casi un minuto). (2) Propósito: calmar al público. Decisión: bajar la fuerza al entrar la voz. Ajuste: acortar el saludo a 30 segundos. Resultado: el acto cupo en el tiempo. (3) Se publica el texto con el nombre del grupo y los títulos, sin datos personales, y el video solo con quienes aceptaron aparecer.",
        ["elige un comentario con evidencia y lo justifica", "escribe un texto de proceso con cuatro partes", "decide una difusión que respeta permisos", "no incluye datos personales"],
        ["hoja con la evidencia elegida, el texto de proceso y la decisión de difusión"],
        ["elegir un comentario sin evidencia", "olvidar el resultado en el proceso", "incluir datos personales"],
        "Pregunta: «¿qué dato concreto da ese comentario?». Si no lo hay, pídele que elija otro."),
    reinforce="Escribe dos preguntas abiertas para una hoja de comentarios del público y explica por qué son más útiles que «¿te gustó?».",
    extend="Explica cómo cambiaría tu decisión de difundir si en el video apareciera una persona menor de edad que no pertenece al grupo.",
)
