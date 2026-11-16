"""Teatro 3.º y 4.º medio FG: OAC-02 (creación de ejercicios dramáticos individuales y colectivos), clases 4 a 6. Escenas inventadas; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O2 = "FG-TEAT-3y4-OAC-02"

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (equipo de ejemplo, inventado). Equipo de 4 personas: Ana (dirección), Beto (dramaturgia: escribe el texto y las acotaciones), Carla y Darío (actuación). "
     "Propósito: mostrar a estudiantes de primero medio cómo se siente esperar sin información. Tienen 3 ensayos de 20 minutos y una función de 6 minutos.")
build(
    O2, 4, F,
    use="Aprenderé a trabajar en equipo para crear un ejercicio colectivo: definir el propósito y el público, repartir roles (dirección, dramaturgia, actuación y apoyo), tomar acuerdos y decidir probando ideas.",
    prior=["Sé armar inicio, conflicto y cierre.", "Sé que la puesta en escena reúne espacio, objetos, luz y sonido.", "Sé respetar turnos y opiniones distintas."],
    explain=[
        "Un ejercicio colectivo funciona cuando el equipo comparte un propósito: lo que quiere comunicar y a quién. Con el propósito claro, cada decisión de cuerpo, voz, espacio y objetos se evalúa según si ayuda a comunicarlo. El público también importa: no es lo mismo mostrar un ejercicio a estudiantes de primero medio que a niños pequeños, porque cambian el lenguaje, el ritmo y los temas adecuados.",
        "Los roles ordenan el trabajo. La dirección coordina las decisiones y cuida el propósito y el tiempo. La dramaturgia escribe el texto y las acotaciones (indicaciones de acción y de espacio). La actuación interpreta a los personajes. El apoyo técnico se ocupa de objetos, orden del espacio y señales de inicio y fin. Todos los roles son importantes y una misma persona puede cambiar de rol si lo prefiere.",
        "Para decidir en equipo se acuerdan normas simples: hablar de a uno, escuchar hasta el final, proponer en vez de descalificar y probar las ideas antes de descartarlas. Cuando hay dos ideas opuestas, se prueban ambas y se elige la que sirve mejor al propósito. Si alguien se siente presionado o incómodo, el equipo se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("dirección", "rol que coordina decisiones, propósito y tiempo"), ("dramaturgia", "rol que escribe el texto y las acotaciones"), ("acotación", "indicación escrita sobre acciones, gestos o espacio"), ("apoyo técnico", "rol que cuida objetos, orden del espacio y señales"), ("público específico", "grupo concreto de personas al que va dirigida la escena"), ("consenso", "acuerdo al que llega el equipo tras escuchar y probar")],
    worked=[
        ("Repartir roles", "Un equipo de cinco debe presentar un ejercicio de 6 minutos con dos personajes. ¿Cómo reparte los roles?", ["Dos personas actúan, una dirige, una escribe el texto y una cuida objetos y señales.", "Cada rol tiene una tarea clara y todos opinan en las decisiones comunes."], "Dos en actuación, una en dirección, una en dramaturgia y una en apoyo técnico"),
        ("Decidir entre dos ideas", "Dos integrantes proponen finales distintos. ¿Qué procedimiento usa el equipo?", ["Prueba cada final una vez y observa cuál comunica mejor el propósito.", "Decide con el criterio del propósito, no por quién propuso."], "Probar ambos y elegir según el propósito"),
    ],
    mistakes=[("Decidir solo con la idea de quien tiene la voz más fuerte.", "Se pierden ideas que podrían servir mejor y alguien queda excluido.", "Prueba las ideas y decide según el propósito."),
              ("Repartir roles sin escuchar lo que cada integrante quiere o puede hacer.", "Si alguien no se siente cómodo, no aporta y el equipo se tensiona.", "Pregunta qué rol prefiere cada uno y respeta su decisión.")],
    T=[
        ('abc', '¿Qué hace la persona que cumple el rol de dirección?', 'Coordina las decisiones y cuida el propósito del ejercicio', 'Actúa todos los personajes mientras los demás observan', 'Escribe el texto completo y lo reparte sin conversar con nadie', 'La dirección organiza las decisiones del equipo; no reemplaza a los demás roles.'),
        ('abc', '{F} ¿Qué rol cumple Beto?', 'Dramaturgia: escribe el texto y las acotaciones', 'Dirección: coordina los ensayos del grupo y decide quién actúa', 'Actuación: interpreta al personaje principal frente al público', 'Beto escribe el texto, tarea que corresponde a la dramaturgia.'),
        ('abc', '¿Cuál es un acuerdo de equipo útil para decidir?', 'Hablar de a uno, escuchar hasta el final y probar las ideas antes de descartarlas', 'Aceptar siempre la primera idea que se diga, sin probar otras', 'Que decida la persona que habla con la voz más fuerte', 'Escuchar y probar hace que las decisiones se basen en evidencia y no en el volumen de voz.'),
        ('abc', '¿Para qué sirve definir el propósito antes de ensayar?', 'Para evaluar cada decisión de cuerpo, voz y espacio según lo que se quiere comunicar', 'Para no modificar nada durante los ensayos de la semana siguiente', 'Para que el público no necesite pensar al ver la escena', 'El propósito es el criterio común del equipo para decidir.'),
        ('abc', '{F} El propósito es mostrar cómo se siente esperar sin información. ¿Qué decisión se alinea con él?', 'Que los personajes esperen sin que nadie les explique cuánto falta', 'Que al final un personaje anuncie la hora exacta del turno de cada persona de la fila', 'Que todos conversen alegres sobre otro tema mientras esperan', 'La falta de explicación es lo que se quiere mostrar; las otras ideas la eliminan.'),
        ('abc', 'Dos integrantes proponen finales opuestos. ¿Qué procedimiento ayuda?', 'Probar ambas versiones y elegir la que mejor sirva al propósito', 'Votar sin probar y no volver a discutir nunca el tema', 'Dejar que decida quien llegó primero al grupo', 'Probar da evidencia; las otras formas no consideran el propósito.'),
        ('=', '{F} ¿Cuántos minutos suman los tres ensayos y la función?', '3*20+6', 'Se multiplican los ensayos por sus minutos y se suma la función.', ' minutos'),
        ('abc', 'Carla quiere cambiar su personaje antes de la función. ¿Qué acuerdo corresponde?', 'Plantearlo al equipo y probarlo en un ensayo', 'Cambiarlo directo en la función para sorprender al resto', 'No decir nada y esperar que nadie lo note', 'Un cambio afecta a los demás, por eso se conversa y se prueba antes.'),
        ('abc', 'Falta decidir el cierre del ejercicio. ¿Quién debe decidirlo?', 'El equipo completo, con la dirección coordinando la decisión', 'Solo la dirección, porque dirige y no necesita consultar al resto', 'Solo la dramaturgia, porque escribe el texto', 'La dirección coordina, pero las decisiones comunes se toman escuchando al equipo.'),
        ('abc', 'Darío dice que no quiere actuar, pero sí ayudar. ¿Qué respuesta respeta el trabajo en equipo?', 'Asignarle otro rol, como apoyo técnico o dramaturgia, y respetar su decisión', 'Insistir hasta que acepte actuar porque nadie más puede', 'Dejarlo fuera del grupo', 'Respetar su decisión y ofrecer otro rol mantiene al integrante dentro del equipo sin presión.'),
        ('abc', 'Un equipo pasa los tres ensayos discutiendo quién tiene la razón. ¿Qué falló?', 'No acordaron un procedimiento para decidir y probar las ideas', 'Tuvieron demasiadas ideas y debieron descartar la mayoría antes de empezar a ensayar', 'No eligieron un líder permanente', 'Sin un procedimiento para decidir, la discusión reemplaza al ensayo.'),
        ('=', 'La función dura 6 minutos y se reparte en 3 escenas iguales, con 2 cambios de 30 segundos entre ellas. ¿Cuántos segundos dura cada escena?', '(6*60-2*30)//3', 'Se pasan los minutos a segundos, se restan los cambios y se reparte en tres.', ' segundos'),
        ('abc', 'El equipo mantiene el propósito, pero ahora presentará a niños de 5.º básico. ¿Qué debe revisar?', 'Si el lenguaje, el ritmo y los gestos se entienden para esa edad', 'Nada, porque si el propósito es el mismo el ejercicio funciona igual con cualquier público', 'Cambiar el propósito por uno más difícil', 'El público cambia lo que se entiende; el propósito se conserva, pero los recursos se ajustan.'),
    ],
    ctx=('ab', 'Una integrante no está de acuerdo con una decisión del equipo. ¿Qué conviene hacer?', 'Decirlo con respeto y proponer una prueba para comparar', 'Callarse y dejar de ir a los ensayos', 'Expresar el desacuerdo y proponer una prueba aporta al equipo; irse lo deja sin esa integrante.'),
    sc=[
        ("En Teatro: ¿qué es una acotación?", "Una indicación escrita sobre acciones, gestos o espacio", "La escribe la dramaturgia para orientar la puesta en escena."),
        ("¿Qué es el público específico de un ejercicio?", "El grupo concreto de personas al que va dirigido", "Conocerlo ayuda a ajustar lenguaje, ritmo y temas."),
        ("Si alguien del equipo se siente presionado o incómodo, ¿qué se hace?", "Se detiene el trabajo y se avisa a una persona adulta", "El bienestar de las personas va primero."),
    ],
    op=("Escoge un propósito de ejemplo: mostrar cómo se siente esperar sin información, mostrar lo difícil de ponerse de acuerdo o mostrar lo útil de pedir ayuda. Escribe: el público, los roles de un equipo de cuatro (quién hace qué), dos acuerdos de equipo y cómo decidirían entre dos finales.",
        "Propósito: lo útil de pedir ayuda; público: primero medio; Ana dirige, Beto escribe, Carla y Darío actúan; acuerdos: hablar de a uno y probar antes de descartar; deciden probando los dos finales y eligiendo el que mejor muestra el propósito.",
        ["propósito y público claros", "reparte los cuatro roles", "dos acuerdos concretos", "decide probando según el propósito"],
        ["ficha del equipo con roles y acuerdos"],
        ["decidir por quién propone la idea", "no considerar al público"],
        "Pregunta: «¿cómo sabrían cuál final sirve mejor al propósito?». Debe responder probando y comparando."),
    reinforce="Con tu grupo o con una persona de tu casa, escriban dos acuerdos para decidir en equipo y pruébenlos al elegir una actividad.",
    extend="Explica por qué cambiar el público obliga a ajustar los recursos sin cambiar necesariamente el propósito.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (pauta y evaluación de ejemplo, inventadas). Criterios, con puntaje de 1 a 3: conflicto claro, cuerpo y voz, espacio y objetos, trabajo en equipo, seguridad y respeto. "
     "Ejercicio evaluado, «La fila»: conflicto claro 3, cuerpo y voz 2, espacio y objetos 3, trabajo en equipo 3, seguridad y respeto 3. "
     "Comentario de un compañero: «Cuando la persona de atrás suspiró y miró el reloj, entendí que tenía prisa; la voz se perdió al final de las frases.»")
build(
    O2, 5, F,
    use="Aprenderé a revisar un ejercicio dramático con una pauta de criterios, a dar retroalimentación descriptiva (observo, efecto, sugerencia) y a decidir qué cambiar en la siguiente versión.",
    prior=["Sé armar un ejercicio con inicio, conflicto y cierre.", "Sé que los recursos de cuerpo, voz y espacio comunican.", "Sé separar hechos de interpretaciones."],
    explain=[
        "Revisar es mirar el ejercicio con criterios, que son aspectos concretos que se observan para valorarlo: por ejemplo, si el conflicto se entiende, si el cuerpo y la voz sirven al propósito, si el espacio y los objetos ayudan, si el equipo trabajó en conjunto y si se cuidó la seguridad y el respeto. Una pauta de criterios con una escala de 1 a 3 permite ordenar lo que se vio y sumar los puntos de cada criterio.",
        "La retroalimentación descriptiva dice qué se observó, qué efecto produjo y qué se sugiere: «Cuando bajaste la voz al final, no alcancé a escuchar la última frase; prueba frases más cortas y respira antes de la última palabra». Evita frases vagas como «estuvo mal» o «me encantó», porque no ayudan a decidir qué cambiar. Siempre se habla de la escena y no de la persona.",
        "Revisar el proceso es tan importante como puntuar el resultado: los ensayos, los cambios y las decisiones muestran cuánto avanzó el equipo. Después de recibir comentarios, el equipo elige cuáles aplicar según su propósito, cambia una cosa por vez y vuelve a probar. Si un comentario es ofensivo o hiere, se detiene la revisión y se avisa a una persona adulta.",
    ],
    vocab=[("criterio", "aspecto concreto que se observa para valorar una escena"), ("pauta", "lista de criterios con una escala para valorarlos"), ("retroalimentación descriptiva", "comentario que dice qué se observó, qué efecto tuvo y qué se sugiere"), ("proceso", "camino de ensayos, cambios y decisiones hasta el resultado"), ("sugerencia", "propuesta concreta para mejorar")],
    worked=[
        ("Escribir una retroalimentación", "Viste que un actor quedó de espaldas al público durante todo el diálogo. Escribe un comentario descriptivo.", ["Observación: durante el diálogo quedaste de espaldas al público.", "Efecto y sugerencia: no se escuchó tu voz; prueba girar el cuerpo en diagonal para que se vea tu rostro."], "Observación, efecto y sugerencia concretos"),
        ("Sumar una pauta", "Un ejercicio sacó 3, 2, 3, 3 y 2 en cinco criterios de máximo 3. ¿Cuántos puntos suma y cuál es el máximo?", ["Suma: 3 + 2 + 3 + 3 + 2 = 13 puntos.", "Máximo posible: 5 × 3 = 15 puntos."], "13 de 15 puntos"),
    ],
    mistakes=[("Comentar «estuvo malo» o «me gustó mucho» sin decir por qué.", "No dice qué se vio ni qué cambiar.", "Describe lo observado, el efecto y una sugerencia."),
              ("Criticar a la persona («eres muy torpe») en lugar de la escena.", "Hiere y no ayuda a mejorar el ejercicio.", "Habla de lo que se vio en la escena.")],
    T=[
        ('abc', '¿Qué es un criterio de evaluación en una pauta?', 'Un aspecto concreto de la escena que se observa para valorarla', 'La nota final que obtiene el equipo cuando termina la presentación completa', 'La opinión personal de quien evalúa', 'El criterio es lo que se mira; la nota o la opinión no lo son.'),
        ('=', '{F} ¿Cuántos puntos suma el ejercicio «La fila»?', '3+2+3+3+3', 'Se suman los puntajes de los cinco criterios.', ' puntos'),
        ('abc', '¿Cuál es una retroalimentación descriptiva?', 'Cuando bajaste la voz al final, no alcancé a escuchar la última frase', 'Estuvo mal y no me gustó nada de lo que hicieron', 'Tú actúas mejor que el resto de las personas de tu equipo', 'Dice qué se observó y qué efecto tuvo; las otras no describen la escena.'),
        ('abc', '{F} ¿Qué criterio de la pauta apoya el comentario sobre la voz?', 'Cuerpo y voz', 'Seguridad y respeto', 'Espacio y objetos', 'La voz que se pierde pertenece al uso expresivo de cuerpo y voz.'),
        ('abc', 'Una buena sugerencia de mejora es', 'probar frases más cortas y respirar antes de la última palabra', 'hablar mejor la próxima vez, con más cuidado y sin cometer los mismos errores', 'actuar con más ganas aunque no sepas cómo', 'Es concreta y se puede ensayar; las otras no indican qué hacer.'),
        ('abc', '¿Por qué se revisa también el proceso y no solo el resultado?', 'Porque los ensayos y cambios muestran cómo el equipo tomó decisiones', 'Porque el resultado final no se puede evaluar sin conocer los ensayos de todos', 'Porque así se evita dar puntajes', 'El proceso aporta evidencia del aprendizaje además de la versión final.'),
        ('=', 'Un ejercicio sumó 12 puntos de 15 posibles. ¿Qué porcentaje del máximo logró?', '12*100//15', 'Se divide el puntaje obtenido entre el máximo y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿En qué criterio conviene trabajar para mejorar la siguiente versión?', 'Cuerpo y voz, que tuvo el puntaje más bajo', 'Conflicto claro, porque es lo más importante', 'Seguridad y respeto, porque siempre tiene 3', 'Es el único criterio con menos de 3 puntos, así que ahí hay más por mejorar.'),
        ('abc', 'Quieres comentar que el personaje se movió igual en toda la escena. ¿Cuál redacción es descriptiva?', 'Tu personaje mantuvo el mismo paso en toda la escena y no vi cambio al recibir la noticia', 'Tu personaje es aburrido, plano y se parece a todos los demás', 'Tú no sabes moverte en escena y deberías practicar más', 'La primera dice qué se vio y cuándo; las otras juzgan a la persona o al personaje sin ejemplos.'),
        ('abc', 'Un revisor elogia todo y otro critica todo, ambos sin ejemplos. ¿Qué falta en los dos?', 'Observaciones concretas con ejemplos de la escena', 'Más puntajes en la pauta, para poder sumar los criterios de otra manera', 'Una nota final distinta', 'Sin ejemplos, ninguno de los comentarios ayuda a decidir qué cambiar.'),
        ('abc', 'El equipo recibe cuatro sugerencias distintas. ¿Cómo decide cuáles aplicar?', 'Revisa cuáles se relacionan con su propósito y prueba las elegidas', 'Aplica todas a la vez para no ofender a nadie', 'Aplica solo la primera que escuchó', 'El propósito ordena la elección y probar una cosa por vez permite ver el efecto.'),
        ('=', 'Cada criterio puede tener 1, 2 o 3 puntos y hay 5 criterios. Un ejercicio tiene 3 en tres criterios y 2 en otro. ¿Cuántos puntos necesita en el último criterio para llegar a 14?', '14-(3*3+2)', 'Se suman los puntos ya obtenidos y se resta del total buscado.', ' puntos'),
        ('abc', 'Dos ejercicios suman el mismo puntaje, pero uno ensayó tres veces con cambios y el otro no ensayó. ¿Qué información agrega revisar el proceso?', 'Muestra cuánto cambió y aprendió el equipo antes de presentar', 'Indica que el que no ensayó es mejor, porque improvisar siempre demuestra más talento', 'No agrega nada, porque el puntaje ya lo dice todo', 'El proceso revela decisiones y aprendizajes que el puntaje final no muestra.'),
    ],
    ctx=('ab', 'Vas a dar un comentario a un compañero. ¿Qué orden conviene?', 'Primero algo que funcionó con un ejemplo y luego una sugerencia concreta', 'Primero todo lo que falló y al final nada más', 'Empezar por lo que funcionó con un ejemplo ayuda a conservarlo y a recibir mejor la sugerencia.'),
    sc=[
        ("En Teatro: ¿qué es la retroalimentación descriptiva?", "Un comentario que dice qué se observó, qué efecto tuvo y qué se sugiere", "Se centra en la escena y se puede aplicar."),
        ("¿Se critica a la persona o a la escena?", "A la escena, nunca a la persona", "El comentario debe ayudar a mejorar, no herir."),
        ("Si un comentario es ofensivo, ¿qué se hace?", "Se detiene la revisión y se avisa a una persona adulta", "Las faltas de respeto no se resuelven confrontando."),
    ],
    op=("Escoge un ejercicio de ejemplo: «La fila», «El paradero» o «La sala de espera». Imagina que lo viste y escribe una retroalimentación para tu compañero con: una observación concreta, su efecto, una sugerencia y el criterio de la pauta al que pertenece (conflicto claro, cuerpo y voz, espacio y objetos, trabajo en equipo o seguridad y respeto).",
        "«El paradero»: cuando el personaje miró varias veces hacia la calle sin hablar, entendí que esperaba a alguien (cuerpo y voz). Sugiero mantener esa mirada y subir un poco el volumen al decir la última frase para que llegue al fondo.",
        ["incluye observación concreta", "dice el efecto", "da una sugerencia aplicable", "nombra el criterio", "habla de la escena y no de la persona"],
        ["comentario escrito de tres o cuatro oraciones"],
        ["comentar solo si gustó", "criticar a la persona"],
        "Pregunta: «¿quien te lee podría saber qué cambiar mañana?». Si no, agrega la sugerencia."),
    reinforce="Escribe una retroalimentación descriptiva sobre un ejercicio inventado de seis líneas (observo, efecto, sugiero).",
    extend="Explica por qué revisar el proceso permite aprender más que mirar solo el puntaje del resultado.",
)

# ============================================================ OAC-02, clase 6
F = ("Ficha 6 (caso de ejemplo, inventado). Un grupo de 5 personas prepara un ejercicio de 6 minutos. Elena no quiere actuar, pero acepta ayudar con la utilería. "
     "Un compañero propone grabar la función con su teléfono y subir el video a una red social abierta. El docente indica que el ejercicio solo puede mostrarse al curso.")
build(
    O2, 6, F,
    use="Aprenderé a presentar un ejercicio respetando el consentimiento: nadie es obligado a actuar, nadie es grabado ni difundido sin permiso y cada decisión de presentación cuida a las personas y a la audiencia.",
    prior=["Sé armar y revisar un ejercicio colectivo.", "Sé dar retroalimentación descriptiva.", "Sé que las personas tienen derecho a su imagen."],
    explain=[
        "Presentar es compartir el ejercicio con una audiencia. Antes de hacerlo, se conversa el orden, el tiempo, las señales de inicio y fin y quién cuida qué. Al presentar, el grupo espera el silencio, comienza con una señal acordada, mantiene la concentración, termina con un cierre claro y agradece. La audiencia, por su parte, mira con atención y respeta sin interrumpir.",
        "El consentimiento es la autorización libre de una persona. Participar es voluntario: quien no quiere actuar puede ayudar de otra forma (dirección, utilería, apoyo técnico) y no se le presiona. Grabar, fotografiar o difundir un ejercicio también necesita el permiso de todas las personas que aparecen. Si alguna es menor de edad, se necesita además la autorización de su persona adulta responsable, y el lugar donde se mostrará debe respetar lo acordado, por ejemplo solo el curso.",
        "Subir imágenes a una red abierta puede exponer a las personas sin que puedan retirarlas después. Por eso no se difunde nada sin permiso y se muestra solo donde se acordó. Si alguien presiona a otra persona para actuar, grabar o difundir, o si algo en una presentación genera riesgo o incomodidad, se detiene la actividad y se avisa a una persona adulta de confianza, sin confrontar ni guardar el secreto.",
    ],
    vocab=[("consentimiento", "autorización libre de una persona para participar o ser registrada"), ("audiencia", "personas que presencian una presentación"), ("difundir", "hacer llegar un registro a otras personas o lugares"), ("autorización", "permiso expreso, que puede incluir a una persona adulta responsable"), ("señal de inicio", "indicación acordada para comenzar la presentación")],
    worked=[
        ("Respetar el consentimiento de participar", "Una compañera dice que no quiere actuar en la presentación. ¿Qué hace el grupo?", ["Respeta su decisión sin insistir ni burlarse.", "Le ofrece otro rol, como utilería o apoyo técnico, si ella quiere."], "Se respeta su decisión y se le ofrece otro rol voluntario"),
        ("Decidir si se graba", "Un integrante quiere grabar la función para compartirla en línea. ¿Qué necesita antes?", ["Preguntar a cada persona que aparece si acepta ser grabada y compartida.", "Obtener la autorización de la persona adulta responsable si alguien es menor de edad, y respetar dónde se acordó mostrarlo."], "Permiso de todas las personas y respeto al lugar acordado"),
    ],
    mistakes=[("Grabar y subir el video porque «todos sabían que se estaba presentando».", "Estar presente no es lo mismo que aceptar ser grabado o difundido.", "Pide permiso por separado para grabar y para difundir."),
              ("Presionar a un compañero para que actúe «porque faltaba alguien».", "El consentimiento debe ser libre, sin presión.", "Reorganiza el ejercicio o ofrece otro rol voluntario.")],
    T=[
        ('abc', '¿Qué es el consentimiento?', 'La autorización libre de una persona para participar o ser registrada', 'La obligación de aceptar lo que el grupo pida, para no perjudicar al equipo completo', 'Un permiso que vale para siempre y para cualquier uso', 'El consentimiento es libre y específico; no se impone ni se da una vez para todo.'),
        ('abc', '{F} ¿Qué respuesta del grupo respeta el consentimiento de Elena?', 'Aceptar que ayude con la utilería y no presionarla para actuar', 'Insistirle con amabilidad hasta que acepte actuar, porque faltan personas en el elenco', 'Cambiarle el rol en secreto para que no se dé cuenta', 'Se respeta su decisión y se mantiene la tarea que ella aceptó.'),
        ('abc', '{F} ¿Qué falta antes de grabar la función?', 'El permiso de cada persona que aparece, y de su persona adulta responsable si es menor de edad', 'Que el teléfono tenga buena cámara y memoria suficiente para registrar toda la función', 'Que la mayoría del grupo lo apruebe en una votación', 'Cada persona decide sobre su propia imagen, y una votación no reemplaza su autorización.'),
        ('abc', '{F} ¿Qué se debe respetar sobre dónde se muestra el ejercicio?', 'Lo indicado por el docente: solo al curso', 'Lo que prefiera quien tiene el teléfono, porque es quien graba y administra el video', 'La red social con más público', 'La indicación del docente fija el lugar de la presentación y no se cambia sin autorización.'),
        ('abc', 'Subir un video a una red abierta puede ser un riesgo porque', 'las personas no controlan después quién lo ve ni dónde se copia', 'los videos de teatro suelen verse con mala calidad y no se entiende lo que ocurre', 'solo se puede ver una vez', 'Lo publicado en abierto se puede copiar y compartir, y no se puede retirar del todo.'),
        ('abc', 'Para comenzar una presentación, el grupo debe', 'esperar el silencio y partir con una señal acordada', 'empezar apenas llega el grupo, aunque el curso todavía no esté en silencio', 'pedir al público que se ría', 'Una señal acordada ordena el inicio y centra la atención de la audiencia.'),
        ('=', 'La función total dura 36 minutos con 6 grupos que presentan 5 minutos cada uno. El resto es para cambios y comentarios. ¿Cuántos minutos quedan para eso?', '36-6*5', 'Se resta del total el tiempo de las presentaciones.', ' minutos'),
        ('abc', 'Un integrante quiere grabar el ensayo para verlo después en el grupo. ¿Qué es lo adecuado?', 'Pedir el permiso de todos para grabarlo y usarlo solo para revisión del grupo', 'Grabar sin avisar y mostrárselo al curso', 'Grabar y dejar el video disponible para quien lo quiera', 'La grabación y su uso necesitan permiso, y el uso queda limitado a lo acordado.'),
        ('abc', 'Quien presenta olvida una parte. ¿Qué respuesta de la audiencia respeta a todos?', 'Esperar con respeto a que continúe, sin burlas', 'Corregirle en voz alta desde la fila para que retome pronto la escena', 'Aplaudir para que termine antes', 'Una audiencia respetuosa permite continuar sin exponer a la persona.'),
        ('abc', 'Una compañera cambia de opinión y ya no quiere aparecer en el video que habían acordado. ¿Qué corresponde?', 'Respetar su cambio y no usar las imágenes donde aparece', 'Mantener el video porque ya lo habían acordado antes', 'Mostrarlo solo si ella no se entera', 'El consentimiento puede retirarse, y el grupo debe respetarlo.'),
        ('abc', 'Alguien presiona al grupo para que suba el video aunque dos personas dudan. ¿Qué hace un integrante que se siente incómodo?', 'Detiene la actividad y avisa a una persona adulta de confianza', 'Confronta al compañero frente a todos para que se arrepienta de insistir', 'Guarda el secreto para evitar problemas con quienes quieren subir el video', 'Ante presión o incomodidad se avisa a una persona adulta, sin confrontar ni callar.'),
        ('=', 'Un grupo de 5 integrantes pide una autorización a cada persona que aparecerá en el video; 2 de ellas son menores de edad y necesitan además la autorización de su persona adulta responsable. ¿Cuántas autorizaciones reúne el grupo en total?', '5+2', 'Se suma una autorización por integrante y otra por cada menor de edad.', ' autorizaciones'),
        ('abc', 'El grupo quiere compartir una foto del ejercicio en el diario mural del colegio. ¿Qué debe revisar?', 'Que todas las personas que aparecen o sus personas adultas responsables lo hayan autorizado', 'Que la foto quede nítida y bien encuadrada antes de colgarla en el lugar', 'Que el diario mural sea visible para todo el colegio y reciba muchas visitas', 'Aunque sea un lugar del colegio, la imagen es de las personas y requiere su permiso.'),
    ],
    ctx=('ab', 'Dos integrantes quieren grabar y otra duda. ¿Qué conviene hacer?', 'No grabar hasta tener el permiso de quien duda y respetar su decisión', 'Grabar de todas formas, porque la mayoría quiere', 'Si alguien duda, no se graba hasta que la persona decida libremente.'),
    sc=[
        ("En Teatro: ¿qué es el consentimiento?", "La autorización libre de una persona para participar o ser registrada", "No se impone ni se presume."),
        ("¿Quién decide si se usa la imagen de una persona en un video?", "Ella misma, y su persona adulta responsable si es menor de edad", "La imagen es de cada persona."),
        ("Si alguien te presiona para grabar o difundir algo, ¿qué haces?", "Me detengo y aviso a una persona adulta de confianza", "No se confronta ni se guarda el secreto."),
    ],
    op=("Escoge un caso de ejemplo: (1) quieren grabar la función y compartirla en una red; (2) una persona del grupo no quiere actuar; (3) una persona quiere retirar su permiso. Escribe qué decisión toma el grupo, a quién consulta, dónde se muestra el ejercicio y qué hace si alguien se siente presionado.",
        "Caso 2: el grupo consulta a la propia persona y respeta que no quiera actuar, le ofrece apoyo técnico, muestra el ejercicio solo al curso y, si alguien la presiona, ella o alguien del grupo avisa a una persona adulta de confianza.",
        ["respeta el consentimiento", "indica a quién consulta", "dice dónde se muestra", "incluye avisar a una persona adulta ante presión"],
        ["hoja con la decisión del grupo"],
        ["presionar a la persona", "difundir sin permiso"],
        "Pregunta: «¿quién decide sobre su propia imagen o participación?». La respuesta es la propia persona."),
    reinforce="Escribe cuatro frases que un grupo puede decir para pedir permiso antes de grabar o fotografiar un ejercicio.",
    extend="Explica por qué mostrar un ejercicio «solo al curso» protege a las personas más que subirlo a una red abierta.",
)
