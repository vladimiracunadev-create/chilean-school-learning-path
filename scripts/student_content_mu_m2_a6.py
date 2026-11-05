"""Student material for 2.º medio Música, OA 06 (evaluar críticamente fortalezas y áreas de crecimiento personal en audición, interpretación, creación y reflexión, propia y de otros, y diseñar un plan de mejora).

Los casos son ficticios y de ejemplo. Nadie debe exponer su desempeño real: las autoevaluaciones se hacen en privado y se comparten solo si la persona quiere.
La audición real de grabaciones del curso y la práctica instrumental quedan para el docente.
"""
from __future__ import annotations

from student_content_mu_m2_a import L
from student_lessons import arith, ex

OA6 = "MU2M OA 06"

# ---------------------------------------------------------------- OA 06 · clase 1 (evaluar mi audición)
L(
    OA6, 1,
    "Lápiz y papel. Los extractos y las autoevaluaciones están escritos en los ejercicios (son de ejemplo). Tu docente decide qué audiciones reales usar.",
    "Aprenderé a evaluar mi audición con criterios y evidencia, y a identificar fortalezas y áreas de crecimiento. Sirve para saber qué escucho bien y qué puedo practicar para describir mejor la música.",
    ["Distingo rasgos audibles, contexto y opinión.", "Describo tempo, textura, timbre y forma.", "Fundamento una valoración con razones."],
    [
        "Evaluar mi audición es revisar qué tan bien escucho y describo la música. Se usan criterios claros: si reconozco el pulso y el tempo, si distingo las voces e instrumentos, si identifico la forma (las partes de la pieza), si separo lo que se oye de lo que opino y si uso vocabulario preciso. Para cada criterio se busca una evidencia: algo que dije o escribí que muestre el nivel alcanzado.",
        "Una fortaleza es un criterio que ya logro con consistencia. Un área de crecimiento es un criterio que aún puedo mejorar. Decir «escucho mal» no sirve: es demasiado general y es un juicio sobre la persona. Sirve decir «identifico el tempo, pero a veces confundo la textura» porque indica qué mejorar. Una escala simple ayuda: 1 aún no, 2 en desarrollo, 3 logrado y 4 profundizado.",
        "Para evaluar con justicia se compara lo que escribí con una respuesta de referencia que entrega el docente. Se marca en qué coincide y en qué no. Los errores no son fracasos, son información para decidir qué practicar. La evaluación es personal: cada persona decide si la comparte con el grupo, y nadie debe presionar a otra para mostrarla.",
    ],
    [("criterio", "pauta para evaluar un desempeño"), ("evidencia", "algo que se dijo o escribió y que muestra lo logrado"), ("fortaleza", "criterio que se logra con consistencia"), ("área de crecimiento", "criterio que se puede mejorar"), ("escala", "niveles ordenados para evaluar"), ("referencia", "respuesta modelo con la que se compara")],
    [
        ("Clasificar un resultado", "Autoevaluación de ejemplo: pulso 4, tempo 3, textura 2, forma 3, vocabulario 2. Si cada criterio en nivel 2 es un área de crecimiento, ¿cuáles son?", ["Se buscan los criterios en 2.", "Textura y vocabulario tienen 2."], "Textura y vocabulario"),
        ("Pasar de un juicio general a uno útil", "Una estudiante escribe: «Escucho mal.» ¿Cómo se reescribe de forma útil?", ["Debe decir qué criterio logra y cuál no.", "Se agrega evidencia."], "«Identifico el tempo, pero a veces confundo la textura»"),
    ],
    [
        ("Escribir «soy malo/a para escuchar» como evaluación.", "Es un juicio sobre la persona, sin criterios ni evidencia.", "Nombra el criterio, la evidencia y qué practicar."),
        ("Pensar que un error significa fracaso.", "Los errores muestran qué practicar.", "Úsalos para decidir una acción de mejora."),
    ],
    [
        ex("¿Qué es una fortaleza en la audición? A) Un criterio que logro con consistencia. B) Un error frecuente.", "A", "Se refiere a lo logrado."),
        ex("¿Qué es una evidencia? A) Algo que dije o escribí y que muestra lo logrado. B) Una opinión sin ejemplo.", "A", "La evidencia sustenta el nivel."),
        ex("¿Qué nivel de la escala de la clase es «logrado»? A) 3. B) 1.", "A", "1 aún no, 2 en desarrollo, 3 logrado, 4 profundizado."),
    ],
    [
        ex("¿Qué frase evalúa mejor? A) «Distingo las voces, pero me falta describir la forma.» B) «Soy un desastre.»", "A", "Tiene criterio y dirección de mejora."),
        ex("¿Para qué sirven los errores en la evaluación? A) Para decidir qué practicar. B) Para criticar a la persona.", "A", "Dan información útil."),
        ex("¿Con qué se compara lo escrito para evaluar con justicia? A) Con una respuesta de referencia. B) Con la opinión de un amigo.", "A", "La referencia da un punto común."),
    ],
    [
        arith("Una autoevaluación de ejemplo tiene cinco criterios con niveles 3, 4, 2, 3 y 3. ¿Cuántos puntos suma?", "3+4+2+3+3", "Se suman los niveles de los criterios.", " puntos"),
        ex("En una autoevaluación de ejemplo con cinco criterios, ¿cuántos puntos serían el máximo posible si todos estuvieran en nivel 4? A) 20. B) 15.", "A", "5 × 4 = 20."),
        ex("Un estudiante marca nivel 4 en forma pero no puede nombrar las partes de ninguna pieza. ¿Qué falta? A) Evidencia que respalde el nivel. B) Más volumen al escuchar.", "A", "El nivel debe apoyarse en evidencia."),
    ],
    [
        ex("Un compañero dice: «Saqué 3 en vocabulario porque me siento seguro.» Otro dice: «Saqué 3 porque usé correctamente seis términos en mi ficha.» ¿Quién se acerca más a una evaluación crítica? A) El segundo, porque cita evidencia. B) El primero.", "A", "La evidencia da fundamento."),
        ex("Dos criterios quedaron en nivel 2. ¿Cuál es una conclusión bien formulada? A) «Mi crecimiento está en textura y vocabulario; practicaré con tres audiciones de ejemplo.» B) «No sirvo para esto.»", "A", "Convierte la evaluación en acción."),
    ],
    [
        ex("Tu docente propone que cada estudiante muestre su autoevaluación a todo el curso. Una persona prefiere no hacerlo. ¿Qué es lo adecuado? A) Respetar su decisión y ofrecerle compartirla solo con el docente. B) Obligarla.", "A", "La evaluación personal es privada."),
        ex("Sacas nivel 2 en tres de cinco criterios y te sientes desanimado. ¿Qué conviene? A) Elegir un criterio para mejorar primero y conversarlo con tu docente. B) Dejar de practicar hasta sentirse mejor.", "A", "Un paso concreto ayuda."),
    ],
    [ex("Para un taller de escucha de tu curso se propone una pauta con tres criterios: pulso, textura y forma. ¿Qué mejora la pauta? A) Agregar un criterio sobre vocabulario y una escala de cuatro niveles. B) Quitar los niveles y dejar solo comentarios generales.", "A", "Hace más claro y verificable el nivel.")],
    [
        ex("¿Verdadero o falso? Una evaluación útil indica qué criterio mejorar.", "Verdadero", "Orienta la acción."),
        ex("¿Qué es un área de crecimiento? A) Un criterio que aún puedo mejorar. B) Un instrumento nuevo.", "A", "Es lo que falta lograr."),
        ex("¿Qué tipo de evaluación es la audición de esta clase? A) Personal y privada. B) Pública y obligatoria.", "A", "Cada persona decide si la comparte."),
    ],
    (
        "Pieza de ejemplo: una cantante con guitarra, pulso tranquilo, dos estrofas y un estribillo que se repite. Escribe una autoevaluación de ejemplo de tu audición con estos criterios (nivel 1 a 4): pulso/tempo, textura, forma, separar rasgo de opinión, vocabulario. Para dos criterios agrega evidencia y termina con una fortaleza y un área de crecimiento.",
        "Pulso/tempo: 3, dije que el pulso era tranquilo. Textura: 3, dije voz y guitarra. Forma: 2, mencioné estrofas pero no el orden. Rasgo/opinión: 3. Vocabulario: 2, usé pocas palabras técnicas. Fortaleza: pulso/tempo. Crecimiento: forma y vocabulario.",
        ["cinco criterios con nivel", "evidencia en dos criterios", "una fortaleza y un área de crecimiento"],
        ["tabla o lista con niveles y evidencia", "conclusión de fortaleza y crecimiento"],
        ["dar un nivel sin evidencia", "juicios sobre la persona"],
        "Reconoce los criterios y pide una evidencia para cada nivel alto.",
    ),
    "Escucha una canción y anota lo que describiste en tres criterios para revisarlo después con una referencia.",
    "Pide a tu docente una referencia de escucha y compara en qué coincidiste y en qué no.",
)

# ---------------------------------------------------------------- OA 06 · clase 2 (evaluar mi interpretación)
L(
    OA6, 2,
    "Lápiz y papel. Las interpretaciones y los registros están descritos en los ejercicios (son de ejemplo). La grabación real de cada estudiante la maneja tu docente con su permiso.",
    "Aprenderé a evaluar mi interpretación con criterios (pulso, entradas, fluidez, afinación, balance y expresividad) y a formular áreas de crecimiento específicas. Sirve para saber exactamente qué mejorar al cantar o tocar.",
    ["Evalúo mi audición.", "Ensayo con método.", "Registro una interpretación."],
    [
        "Para evaluar una interpretación se escucha un registro (en vivo o grabado) y se anota evidencia para cada criterio. El pulso es estable si no se acelera ni se frena sin intención. Las entradas son correctas si se empieza en el momento acordado. La fluidez es avanzar sin detenerse. La afinación es cantar o tocar las alturas esperadas. El balance es el equilibrio entre voces. La expresividad es el uso de dinámica, articulación y carácter para comunicar lo que la pieza pide.",
        "Una buena evaluación localiza el problema: no «toqué mal el estribillo», sino «en el compás 5 del estribillo entré un pulso tarde». También separa la causa del resultado: entrar tarde puede venir de no contar la entrada, y se mejora con una cuenta previa. Cada área de crecimiento se acompaña de una acción concreta, como practicar el fragmento a tempo lento con cuenta.",
        "La evaluación tiene en cuenta el proceso, no solo el resultado: cuántas veces se ensayó, qué método se usó y qué cambió entre una versión y la siguiente. Cada persona avanza a su ritmo. Compararse con otra persona no ayuda; ayuda compararse con la versión anterior de uno mismo.",
    ],
    [("pulso estable", "pulso que no se acelera ni se frena sin intención"), ("afinación", "exactitud de las alturas al cantar o tocar"), ("expresividad", "uso de dinámica, articulación y carácter para comunicar"), ("proceso", "camino de ensayos y cambios hasta el resultado"), ("localizar", "indicar con precisión dónde ocurre algo"), ("acción concreta", "paso específico que se puede realizar")],
    [
        ("Localizar un problema", "Una estudiante graba una pieza de ejemplo. Escribe: «El estribillo salió mal.» ¿Cómo se reescribe con precisión?", ["Debe indicar dónde y qué.", "Se agrega un dato de compás o pulso."], "«En el compás 5 del estribillo entré un pulso tarde»"),
        ("Unir problema y acción", "Un estudiante entra tarde en cada estribillo de una pieza de ejemplo. ¿Qué acción concreta ayuda?", ["La causa puede ser no contar la entrada.", "La cuenta previa ayuda a entrar a tiempo."], "Practicar con una cuenta previa de cuatro pulsos antes del estribillo"),
    ],
    [
        ("Evaluar solo el resultado final.", "Se pierde información sobre el proceso y las causas.", "Registra cuántos ensayos hiciste y qué método usaste."),
        ("Compararse con otra persona para saber si mejoré.", "Cada persona tiene su ritmo y sus recursos.", "Compárate con tu versión anterior."),
    ],
    [
        ex("¿Qué es un pulso estable? A) Uno que no se acelera ni se frena sin intención. B) Uno muy rápido.", "A", "La estabilidad es la clave."),
        ex("¿Qué es la afinación? A) La exactitud de las alturas. B) La rapidez del tempo.", "A", "Se refiere a las alturas."),
        ex("¿Qué es la expresividad? A) Usar dinámica, articulación y carácter para comunicar. B) Tocar más fuerte.", "A", "Es comunicación musical."),
    ],
    [
        ex("¿Qué frase localiza bien un problema? A) «En el compás 3 tardé en entrar.» B) «Todo estuvo mal.»", "A", "Indica dónde ocurre."),
        ex("¿Qué se hace con cada área de crecimiento? A) Se acompaña de una acción concreta. B) Se deja para el final del año.", "A", "La acción permite avanzar."),
        ex("¿Con quién conviene compararse para ver tu avance? A) Con tu versión anterior. B) Con la persona que toca mejor.", "A", "Cada quien avanza a su ritmo."),
    ],
    [
        ex("Una estudiante se detiene en cada pasaje difícil. ¿Qué criterio está más bajo? A) La fluidez. B) El balance.", "A", "Detenerse afecta la fluidez."),
        ex("Un grupo graba dos versiones: en la primera el tempo se acelera, en la segunda es parejo. ¿Qué criterio mejoró? A) El pulso estable. B) La afinación.", "A", "Se estabilizó el tempo."),
        arith("Una autoevaluación de ejemplo de interpretación tiene seis criterios con niveles 2, 3, 3, 2, 4 y 3. ¿Cuántos puntos suma?", "2+3+3+2+4+3", "Se suman los niveles.", " puntos"),
    ],
    [
        ex("Una intérprete evalúa su pieza: «No tengo talento.» ¿Qué corrección es útil? A) Cambiar a «Mi pulso se acelera en el estribillo; practicaré con tempo lento.» B) Mantener la frase.", "A", "Pasa de la persona a un criterio con acción."),
        ex("Una compañera dice: «Si ensayas poco, no puedes evaluarte.» ¿Qué responde alguien que valora el proceso? A) Anotar cuántos ensayos hizo ayuda a explicar el resultado. B) El proceso no importa.", "A", "El proceso explica el resultado."),
    ],
    [
        ex("En un registro de ejemplo, el pulso se acelera de 90 a 100 pulsos por minuto en el estribillo. ¿Qué diferencia hay? A) 10 pulsos por minuto más rápido. B) 10 pulsos por minuto más lento.", "A", "100 − 90 = 10."),
        ex("Antes de mostrar una grabación al grupo, ¿qué debe hacer la persona que la hizo? A) Decidir si quiere mostrarla y pedir permiso a los demás participantes. B) Subirla sin avisar.", "A", "Se respeta la decisión y los permisos."),
    ],
    [ex("Para mejorar la entrada al estribillo, un grupo de ejemplo propone practicar solo ese pasaje durante 5 minutos al inicio de cada ensayo. ¿Qué característica tiene esta acción? A) Es concreta y se puede revisar. B) Es vaga.", "A", "Tiene tarea y tiempo.")],
    [
        ex("¿Verdadero o falso? Evaluar el proceso incluye cuántas veces se ensayó.", "Verdadero", "Es parte del proceso."),
        ex("¿Qué es un criterio de interpretación? A) El pulso, las entradas, la fluidez, entre otros. B) El nombre de la pieza.", "A", "Son pautas para evaluar."),
        ex("¿Qué no ayuda a saber si mejoraste? A) Compararse con otra persona. B) Registrar el avance.", "A", "La comparación no orienta."),
    ],
    (
        "Registro de ejemplo de una pieza a dos voces: el pulso se acelera en el estribillo, las entradas son correctas, la fluidez es buena, la afinación es irregular en la nota más aguda y la expresividad es baja. Escribe una evaluación de ejemplo con nivel 1 a 4 en cada uno de cinco criterios, una fortaleza y dos áreas de crecimiento con una acción concreta cada una.",
        "Pulso 2, entradas 4, fluidez 3, afinación 2, expresividad 2. Fortaleza: entradas. Crecimiento 1: pulso, practicar el estribillo a tempo lento y subirlo de a poco. Crecimiento 2: afinación, cantar la nota aguda sola y luego en la frase.",
        ["cinco criterios con nivel coherente con el registro", "una fortaleza", "dos áreas de crecimiento con acción concreta"],
        ["evaluación con niveles y acciones"],
        ["niveles que contradicen el registro", "acciones vagas"],
        "Reconoce la evaluación y pide hacer más concreta una acción.",
    ),
    "Escribe una acción concreta de cinco minutos para mejorar un pasaje que te cueste.",
    "Compara en tres criterios dos ensayos tuyos de la misma pieza y anota qué cambió.",
)

# ---------------------------------------------------------------- OA 06 · clase 3 (retroalimentar la creación de otras personas)
L(
    OA6, 3,
    "Lápiz y papel. Las creaciones y los comentarios están escritos en los ejercicios (son de ejemplo). La retroalimentación real entre estudiantes se hace con respeto y bajo la guía del docente.",
    "Aprenderé a evaluar una creación musical (propia y de otras personas) con criterios y a dar retroalimentación respetuosa y útil. Sirve para ayudar a mejorar un trabajo sin herir a nadie.",
    ["Evalúo mi audición y mi interpretación.", "Creo secciones con proposiciones dadas.", "Separo rasgo audible, contexto y opinión."],
    [
        "Evaluar una creación es revisarla frente a la consigna y a criterios claros: si cumple las condiciones (duración, compás, notas permitidas), si el motivo se reconoce, si hay equilibrio entre repetición y novedad, si la idea es coherente con el estilo y si logra el efecto buscado. Se evalúa la creación, no a la persona que la hizo.",
        "Una retroalimentación útil sigue tres pasos: describir lo que se oye o lee («el motivo vuelve tres veces»), valorar con un criterio («eso da unidad») y sugerir un cambio concreto («prueba variar la tercera repetición»). Debe ser específica, amable y orientada a mejorar. Una frase como «está feo» no ayuda; «el final termina de golpe, ¿puedes bajar la dinámica en los últimos dos compases?» sí ayuda.",
        "Recibir retroalimentación también se aprende: se escucha completa, se pregunta si algo no se entiende y se decide qué sugerencia se prueba. No toda sugerencia se adopta, pero todas se agradecen. Si un comentario hiere o humilla, se avisa a la persona docente u otra persona adulta de confianza en lugar de responder con otro ataque.",
    ],
    [("retroalimentación", "comentario para ayudar a mejorar un trabajo"), ("consigna", "condiciones del trabajo que se debe cumplir"), ("específica", "que señala con precisión qué y dónde"), ("coherente", "que mantiene relación lógica con el estilo y la idea"), ("sugerencia", "propuesta de cambio"), ("respetuosa", "que cuida a la persona")],
    [
        ("Reescribir un comentario", "Un compañero comenta una creación de ejemplo: «Está feo.» Reescríbelo con los tres pasos.", ["Primero describe lo que se oye.", "Luego valora con un criterio y sugiere un cambio."], "«El motivo vuelve tres veces sin cambios; se siente repetitivo. ¿Puedes variar la tercera vez?»"),
        ("Comprobar el cumplimiento de la consigna", "La consigna pide 8 compases de 4 pulsos. Una creación de ejemplo tiene 6 compases de 4 pulsos y 1 compás de 3 pulsos. ¿Cuántos pulsos faltan?", ["Lo pedido: 8 × 4 = 32.", "Lo escrito: 6 × 4 + 3 = 27."], "5 pulsos"),
    ],
    [
        ("Evaluar a la persona en vez de la creación.", "Hiere y no dice qué mejorar.", "Habla del trabajo: lo que se oye, el criterio y un cambio."),
        ("Decir solo cosas amables sin ninguna sugerencia.", "No ayuda a mejorar.", "Incluye una sugerencia concreta."),
    ],
    [
        ex("¿Qué se evalúa en una creación? A) La creación frente a la consigna y a criterios. B) La personalidad de quien la hizo.", "A", "Se evalúa el trabajo."),
        ex("¿Qué es una sugerencia? A) Una propuesta de cambio. B) Una burla.", "A", "Apunta a mejorar."),
        ex("¿Qué primer paso sigue una retroalimentación útil? A) Describir lo que se oye. B) Dar un puntaje.", "A", "Se parte describiendo."),
    ],
    [
        ex("¿Qué comentario es específico? A) «El puente termina de golpe; baja la dinámica al final.» B) «No me convence.»", "A", "Indica dónde y qué cambiar."),
        ex("¿Qué haces al recibir retroalimentación? A) Escuchar completa y decidir qué probar. B) Rechazarla de inmediato.", "A", "Es parte de aprender."),
        ex("Si un comentario te humilla, ¿qué es lo adecuado? A) Avisar a la persona docente o a otra persona adulta de confianza. B) Responder con un comentario igual de hiriente frente al curso.", "A", "Se pide apoyo y no se escala."),
    ],
    [
        arith("Una creación de ejemplo debe tener 6 compases de 4 pulsos. Una estudiante entrega 5 compases de 4 pulsos. ¿Cuántos pulsos faltan?", "6*4-5*4", "Se compara lo pedido con lo entregado.", " pulsos"),
        ex("Comentario de ejemplo: «El motivo se reconoce y la variación es clara, pero el final no suena a final.» ¿Qué parte destaca lo logrado? A) «El motivo se reconoce y la variación es clara.» B) «El final no suena a final.»", "A", "Valora lo logrado; lo segundo es lo que falta."),
        ex("Una creación cumple la duración pedida y repite el motivo siete veces sin cambios. ¿Qué criterio está débil? A) El equilibrio entre repetición y novedad. B) La duración.", "A", "La repetición excesiva no innova."),
    ],
    [
        ex("Compara dos comentarios sobre una introducción. Uno: «Me gusta.» Otro: «La entrada suave prepara bien la estrofa; podrías agregar un silencio antes de entrar.» ¿Cuál ayuda más? A) El segundo. B) El primero.", "A", "Tiene criterio y sugerencia."),
        ex("Una estudiante dice: «Mi creación es perfecta, no necesito retroalimentación.» ¿Qué respuesta es más útil? A) Otra persona puede notar cosas que tú ya no escuchas. B) Tiene razón.", "A", "El oído propio se acostumbra."),
    ],
    [
        ex("Un grupo comenta la creación de una compañera sin pedirle su permiso para que la escuchen todos. ¿Qué paso falta? A) Preguntarle si quiere compartirla y cómo prefiere recibir comentarios. B) Ninguno.", "A", "Se respeta la decisión de la autora."),
        ex("Recibes tres sugerencias y no puedes aplicar las tres. ¿Qué haces? A) Elegir una, probarla y volver a escuchar. B) Cambiar todo a la vez.", "A", "Se prueba una a la vez."),
    ],
    [ex("Tu curso hará una ronda de comentarios entre compañeros. ¿Qué regla ayuda a un ambiente respetuoso? A) Comentar solo la creación, con los tres pasos, y permitir que quien la creó pida pasar. B) Obligar a todos a opinar sobre todos.", "A", "Protege y guía.")],
    [
        ex("¿Verdadero o falso? Una retroalimentación útil incluye una sugerencia concreta.", "Verdadero", "Orienta la mejora."),
        ex("¿Qué es una consigna? A) Las condiciones del trabajo. B) Un tipo de instrumento.", "A", "Es el marco del trabajo."),
        ex("¿Qué se evalúa: la creación o la persona? A) La creación. B) La persona.", "A", "El foco es el trabajo."),
    ],
    (
        "Creación de ejemplo (descrita): un puente de 4 compases de 4 pulsos con el motivo «ta ti-ti ta sh» repetido sin cambios tres veces y un último compás de silencio. Escribe una retroalimentación de tres frases: describir, valorar con un criterio y sugerir un cambio concreto. Agrega una verificación de si cumple la duración.",
        "El motivo aparece tres veces sin cambios y el último compás es silencio. Eso da unidad pero resulta repetitivo. Prueba variar la tercera repetición con «ti-ti» en lugar de «ta». Duración: 4 compases × 4 pulsos = 16 pulsos, cumple.",
        ["tres pasos: describir, valorar, sugerir", "verificación de duración correcta", "tono respetuoso"],
        ["retroalimentación de tres frases y verificación"],
        ["comentar a la persona", "sugerencia vaga"],
        "Reconoce la retroalimentación y pide concretar la sugerencia.",
    ),
    "Escribe una retroalimentación de tres frases sobre una canción que conozcas.",
    "Pide a una persona de tu casa que te diga una cosa que le gustó y una sugerencia sobre tu creación, y anota qué probarías.",
)

# ---------------------------------------------------------------- OA 06 · clase 4 (reflexionar sobre el proceso, propio y de otros)
L(
    OA6, 4,
    "Lápiz y papel. Las reflexiones están escritas en los ejercicios (son de ejemplo). El diario o portafolio real de cada estudiante es personal y se comparte solo si la persona quiere.",
    "Aprenderé a reflexionar sobre mi proceso musical y el de otras personas: qué hice, qué aprendí, qué cambiaría y qué aporta cada quien. Sirve para aprender de la experiencia y valorar los aportes del grupo.",
    ["Evalúo audición, interpretación y creación.", "Doy retroalimentación respetuosa.", "Distingo evidencia de opinión."],
    [
        "Reflexionar es pensar con calma sobre lo que se hizo para aprender de ello. Una pauta simple tiene cuatro preguntas: ¿qué hice?, ¿qué resultó bien y por qué?, ¿qué no resultó y por qué? y ¿qué cambiaré la próxima vez? Las respuestas se apoyan en evidencia, como una grabación, la bitácora o una autoevaluación, y no solo en sensaciones.",
        "También se reflexiona sobre el trabajo de otras personas: qué aportaron, cómo fue la colaboración y qué se aprendió de su manera de hacer. Reconocer los aportes ajenos es parte de una evaluación justa. Hay que separar lo que uno prefiere de lo que logra una música: no gustar de una pieza no significa que esté mal hecha, ni gustar de ella significa que esté bien hecha.",
        "Cuando tocar o cantar frente a otras personas produce mucho nervio, es normal sentir tensión. Se puede hablar con el docente para elegir un rol con menos exposición, practicar con un grupo pequeño primero o usar respiración lenta. Si el malestar es fuerte o dura, conviene conversarlo con una persona adulta de confianza; no hay que enfrentarlo en soledad.",
    ],
    [("reflexionar", "pensar con calma sobre lo hecho para aprender"), ("proceso", "camino recorrido hasta el resultado"), ("aporte", "trabajo o idea que alguien suma"), ("sesgo de gusto", "juzgar solo por lo que a uno le gusta"), ("portafolio", "carpeta con evidencias del trabajo"), ("colaboración", "trabajo conjunto para un fin común")],
    [
        ("Usar la pauta de cuatro preguntas", "Una estudiante de ejemplo preparó una canción a dos voces. Su registro muestra que el pulso se aceleraba. ¿Cuál es una respuesta a «¿qué no resultó y por qué?»", ["Debe decir qué y por qué.", "Se basa en el registro."], "«El pulso se aceleraba porque no estaba contando el tempo»"),
        ("Separar gusto de logro", "Un estudiante dice: «Esa pieza no me gusta, así que está mal hecha.» ¿Qué corrección es correcta?", ["El gusto es personal.", "La calidad se evalúa con criterios."], "No gustar de una pieza no significa que esté mal hecha"),
    ],
    [
        ("Reflexionar solo con sensaciones, sin evidencia.", "Sin evidencia no se sabe en qué se avanzó.", "Apoya cada respuesta en un registro, una bitácora o una autoevaluación."),
        ("Ignorar los aportes de otras personas en el grupo.", "La evaluación pierde justicia.", "Reconoce al menos un aporte concreto de cada integrante."),
    ],
    [
        ex("¿Qué es reflexionar? A) Pensar con calma sobre lo hecho para aprender. B) Repetir sin pensar.", "A", "Es aprender de la experiencia."),
        ex("¿Qué es un aporte? A) Trabajo o idea que alguien suma. B) Una crítica que no se puede usar.", "A", "Es lo que suma al grupo."),
        ex("¿Qué es un portafolio? A) Una carpeta con evidencias del trabajo. B) Una lista de notas finales.", "A", "Reúne las evidencias del trabajo."),
    ],
    [
        ex("¿Qué pregunta forma parte de la pauta? A) ¿Qué cambiaré la próxima vez? B) ¿Quién tuvo la culpa de los errores?", "A", "Es la cuarta pregunta de la pauta."),
        ex("¿En qué se apoya la reflexión? A) En evidencias como una grabación o una bitácora. B) Solo en sensaciones.", "A", "Evidencia da solidez."),
        ex("Si te produce mucho nervio presentar tu música, ¿qué conviene? A) Hablar con tu docente para elegir un rol con menos exposición. B) Esconderlo y obligarte.", "A", "Hay alternativas respetuosas."),
    ],
    [
        ex("Una estudiante escribe: «Aprendí a contar la entrada con cuatro pulsos y mi fluidez mejoró.» ¿Qué pregunta de la pauta responde? A) Qué resultó bien y por qué. B) Qué cambiaré.", "A", "Explica un logro con su causa."),
        ex("Un grupo reconoce: «Aldo propuso el puente y Bea ordenó los ensayos.» ¿Qué hace esa frase? A) Reconoce aportes concretos. B) Resume la nota final.", "A", "Nombra aportes concretos de otras personas."),
        arith("Un portafolio de ejemplo contiene 3 grabaciones, 4 autoevaluaciones y 2 bitácoras. ¿Cuántas evidencias tiene?", "3+4+2", "Se suman las evidencias.", " evidencias"),
    ],
    [
        ex("Un estudiante dice: «Mi compañero toca mal porque su estilo no me gusta.» ¿Qué sesgo aparece? A) Juzgar solo por gusto. B) Usar criterios.", "A", "Confunde gusto con logro."),
        ex("Una compañera cuenta que le cuesta mucho sentirse segura al tocar y que lleva días con angustia. ¿Qué conviene sugerirle? A) Conversarlo con una persona adulta de confianza y con la docente. B) Que se calle.", "A", "El malestar sostenido requiere apoyo."),
    ],
    [
        ex("Tu portafolio muestra que en octubre usabas cuenta previa y en noviembre ya no. ¿Qué reflexión es más útil? A) Preguntarse por qué dejaste de usarla y retomarla. B) Ignorar el cambio.", "A", "Reconocer el cambio permite corregir."),
        ex("Un compañero grabó su ensayo. ¿Qué haces antes de comentarlo en público? A) Preguntarle si quiere compartirlo. B) Mostrarlo igual.", "A", "Se respeta su decisión."),
    ],
    [ex("Para la reflexión final del semestre se propone completar la pauta de cuatro preguntas con una evidencia por respuesta. ¿Qué ventaja tiene? A) Une lo que se siente con lo que se puede mostrar. B) Ocupa más hojas.", "A", "La evidencia respalda lo dicho.")],
    [
        ex("¿Verdadero o falso? No gustar de una pieza prueba que está mal hecha.", "Falso", "El gusto no es criterio."),
        ex("¿Cuál es una pregunta de la pauta? A) ¿Qué no resultó y por qué? B) ¿Quién es mejor?", "A", "Es una de las cuatro."),
        ex("¿Qué se hace con el nervio escénico persistente? A) Conversarlo con una persona adulta de confianza. B) Enfrentarlo en soledad.", "A", "Pedir apoyo es adecuado."),
    ],
    (
        "Escribe una reflexión de ejemplo de cuatro frases sobre un trabajo musical en grupo, siguiendo la pauta: qué hice, qué resultó bien y por qué, qué no resultó y por qué, qué cambiaré. Incluye una evidencia y el aporte de otra persona del grupo.",
        "Hice la voz grave en una canción a dos voces. Resultó bien la entrada del estribillo porque conté cuatro pulsos (lo vi en la grabación). No resultó mi afinación en la nota aguda porque no la practiqué sola. Cambiaré: practicar esa nota antes del ensayo. Un aporte: Camila ordenó los ensayos.",
        ["cuatro frases según la pauta", "una evidencia citada", "un aporte de otra persona"],
        ["reflexión de cuatro frases con evidencia y aporte"],
        ["no mencionar evidencia", "ignorar los aportes ajenos"],
        "Reconoce la pauta y pide citar la evidencia con más precisión.",
    ),
    "Responde por escrito las cuatro preguntas de la pauta sobre algo que hayas ensayado esta semana.",
    "Conversa con una persona de tu casa sobre qué aprendiste en un trabajo musical y anota un aporte de alguien más.",
)

# ---------------------------------------------------------------- OA 06 · clase 5 (diseñar un plan de mejora)
L(
    OA6, 5,
    "Lápiz y papel. Los planes y los tiempos están escritos en los ejercicios (son de ejemplo). Tu plan real es personal y lo ajustas con tu docente.",
    "Aprenderé a diseñar y revisar un plan de mejora personal con meta, acciones, tiempos, evidencia y revisión. Sirve para convertir mis áreas de crecimiento en pasos que puedo cumplir.",
    ["Evalúo audición, interpretación y creación.", "Reflexiono sobre mi proceso.", "Doy y recibo retroalimentación."],
    [
        "Un plan de mejora convierte un área de crecimiento en acciones. Tiene seis partes: el área que se quiere mejorar, una meta específica y medible (por ejemplo «entrar a tiempo en el estribillo en tres tomas seguidas»), las acciones concretas, el tiempo disponible, la evidencia que mostrará el avance y la fecha de revisión.",
        "Una buena meta es específica (dice qué), medible (se puede comprobar) y realista (se puede lograr en el tiempo disponible). Las acciones deben caber en la semana: pocas y regulares sirven más que muchas y desordenadas. Si se practican 15 minutos al día durante 4 días, son 60 minutos por semana. Conviene dejar un día de descanso y evitar sobrecargar el oído con volumen alto.",
        "El plan se revisa en la fecha acordada: se compara la evidencia con la meta, se decide si se logró y se ajusta. Si no se logró, no es un fracaso: se revisa si la meta era realista o si las acciones eran las adecuadas. Un plan sirve también para otros ámbitos de la música: audición, interpretación, creación y reflexión. Si algo te produce malestar, puedes conversar tu plan con el docente o con una persona adulta de confianza.",
    ],
    [("plan de mejora", "conjunto de acciones para lograr una meta"), ("meta específica", "meta que dice con claridad qué se quiere lograr"), ("medible", "que se puede comprobar con un dato"), ("realista", "que se puede lograr en el tiempo disponible"), ("revisión", "momento en que se compara el avance con la meta"), ("ajustar", "cambiar el plan según lo que se observó")],
    [
        ("Reconocer una meta medible", "Meta A de ejemplo: «Tocar mejor.» Meta B de ejemplo: «Entrar a tiempo en el estribillo en tres tomas seguidas.» ¿Cuál es medible?", ["Una meta medible se puede comprobar.", "B indica cuántas veces y en qué parte."], "La meta B"),
        ("Calcular tiempo de práctica", "Un plan de ejemplo propone 10 minutos de práctica al día, 5 días a la semana. ¿Cuántos minutos son por semana?", ["Cada día son 10 minutos.", "Se multiplican por los días: 10 × 5 = 50."], "50 minutos"),
    ],
    [
        ("Escribir una meta vaga como «mejorar mucho».", "No se puede comprobar si se logró.", "Escribe qué, cuánto y en qué plazo."),
        ("Planear tantas acciones que no caben en la semana.", "Se abandona el plan y desanima.", "Elige pocas acciones que quepan en tu tiempo."),
    ],
    [
        ex("¿Qué es un plan de mejora? A) Un conjunto de acciones para lograr una meta. B) Una nota final.", "A", "Es una herramienta de acción."),
        ex("¿Qué significa «medible»? A) Que se puede comprobar con un dato. B) Que es larga.", "A", "Se puede verificar."),
        ex("¿Qué se hace en la revisión? A) Comparar la evidencia con la meta. B) Cambiar la meta sin mirar.", "A", "Es el propósito de revisar."),
    ],
    [
        ex("¿Qué meta es específica? A) «Cantar la nota más aguda afinada en cuatro de cinco intentos.» B) «Ser mejor.»", "A", "Dice qué y cuánto."),
        ex("¿Qué debe cumplir una meta realista? A) Poder lograrse en el tiempo disponible. B) Ser tan exigente que casi nadie la logra.", "A", "El tiempo importa."),
        ex("Si no se logra la meta en la revisión, ¿qué se hace? A) Se revisa si la meta o las acciones eran adecuadas. B) Se hace la meta más difícil sin cambiar nada.", "A", "Es información para ajustar."),
    ],
    [
        arith("Un plan de ejemplo propone 15 minutos de práctica al día durante 4 días. ¿Cuántos minutos son en la semana?", "15*4", "Se multiplican los minutos diarios por los días.", " minutos"),
        arith("Otro plan de ejemplo propone 20 minutos al día durante 3 días y 10 minutos otro día. ¿Cuántos minutos son en total?", "20*3+10", "Se suman los minutos de los días con 20 y el día con 10.", " minutos"),
        ex("Un plan incluye practicar 40 minutos al día con volumen alto durante toda la semana sin descanso. ¿Qué observación es correcta? A) Es poco realista y puede cansar el oído; conviene reducir y descansar. B) Es el plan ideal.", "A", "El plan debe cuidar el oído."),
    ],
    [
        ex("Una estudiante tiene como área de crecimiento la fluidez. Su plan: tempo lento, fragmentos y subir el tempo. ¿Qué evidencia mostraría el avance? A) Una grabación antes y otra después. B) Su opinión de que mejoró.", "A", "La evidencia permite comparar."),
        ex("Un estudiante marca como meta «aprender a improvisar bien». ¿Qué cambio la mejora? A) «Improvisar 4 compases de 4 pulsos sobre un pulso dado sin detenerme.» B) «Improvisar muy bien.»", "A", "La meta pasa a ser específica y medible."),
    ],
    [
        ex("Un plan de ejemplo tiene área, meta, acciones, tiempo disponible y fecha de revisión. ¿Qué parte de las seis falta? A) La evidencia que mostrará el avance. B) El área que se quiere mejorar.", "A", "Las otras cinco partes están y falta la evidencia."),
        ex("Tras la revisión, una intérprete logró 2 de 4 intentos y su meta era 3 de 4. ¿Qué conclusión es correcta? A) No la logró aún: le faltó un intento y puede ajustar el plan. B) La logró.", "A", "2 es menor que 3, así que falta un intento."),
    ],
    [ex("Tu docente te pide que compartas tu plan solo si quieres. Una compañera lo comparte y otra no. ¿Qué actitud del curso es adecuada? A) Respetar ambas decisiones. B) Presionar a quien no lo comparte.", "A", "El plan es personal.")],
    [
        ex("¿Verdadero o falso? Un plan de mejora incluye una fecha de revisión.", "Verdadero", "Sin revisión no hay ajuste."),
        ex("¿Qué acompaña a cada acción del plan? A) Un tiempo y una evidencia. B) Una calificación del docente.", "A", "Hace verificable el plan."),
        ex("¿Cuántas partes tiene el plan de la clase? A) Seis. B) Tres.", "A", "Área, meta, acciones, tiempo, evidencia y revisión."),
    ],
    (
        "Elige un área de crecimiento de ejemplo (por ejemplo: mantener el pulso en el estribillo) y diseña un plan con las seis partes: área, meta específica y medible, dos acciones concretas, tiempo semanal (con el cálculo), evidencia y fecha de revisión.",
        "Área: pulso en el estribillo. Meta: mantener el tempo parejo en 3 tomas seguidas. Acciones: practicar con tempo lento 10 minutos al día y grabar tres tomas el último día. Tiempo: 10 × 5 días = 50 minutos. Evidencia: las tres grabaciones del último día. Revisión: el viernes de la semana siguiente.",
        ["las seis partes presentes", "meta específica y medible", "cálculo del tiempo correcto"],
        ["plan con seis partes"],
        ["meta vaga", "omitir la evidencia"],
        "Reconoce el plan y pide comprobar el cálculo y la evidencia.",
    ),
    "Escribe tu plan de mejora de una semana con seis partes y revísalo con tu docente.",
    "Agrega a tu plan una acción para el oído (descansar el volumen) y calcula el total de minutos de la semana.",
)
