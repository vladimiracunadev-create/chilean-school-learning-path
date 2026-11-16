"""Música 3.º y 4.º medio FG: OAC-06 (evaluación crítica de procesos y resultados musicales). Rúbricas, bitácoras y comentarios de ejemplo, inventados; sin audio real."""
from __future__ import annotations

from fg_musi_common import build

O6 = "FG-MUSI-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (rúbrica de ejemplo para evaluar un trabajo musical grupal; cada criterio se puntúa de 1 a 4). Criterios de resultado: coherencia con el propósito, dominio técnico, claridad de la forma. "
     "Criterios de proceso: planificación del ensayo, registro de versiones, colaboración en el grupo. Un grupo de ejemplo obtiene: coherencia 3, dominio técnico 2, forma 4, planificación 2, registro 3, colaboración 4.")
build(
    O6, 1, F,
    use="Aprenderé a distinguir los criterios para evaluar el resultado de una obra y los del proceso de trabajo, y a usar una rúbrica con evidencia para evaluar críticamente.",
    prior=["Juzgo con criterios estéticos y evidencia.", "Registro versiones en una bitácora.", "Sé que una opinión necesita razones."],
    explain=[
        "Evaluar críticamente es valorar un trabajo con criterios claros, evidencia y una postura fundada. En música conviene evaluar dos cosas. El resultado es la obra o interpretación final: su coherencia con el propósito, su dominio técnico, la claridad de su forma, su expresividad. El proceso es el camino para llegar a ella: cómo se planificó, cuánto se ensayó, si se registraron versiones y cómo colaboró el grupo. Un buen resultado puede venir de un proceso débil, y al revés.",
        "Una rúbrica es una tabla de criterios con niveles que describen qué se observa en cada uno. Sirve para evaluar con más justicia, porque todos usan los mismos criterios. Cada puntaje debe apoyarse en una evidencia: un compás, una versión, una anotación. Una rúbrica no reemplaza la escucha ni el diálogo: orienta la mirada y deja claro qué se espera.",
        "Evaluar no es calificar a la persona sino describir el trabajo. Se dice qué se logró, qué falta y por qué, con respeto.",
    ],
    vocab=[("evaluación crítica", "valoración con criterios, evidencia y postura fundada"), ("resultado", "obra o interpretación final"), ("proceso", "camino de trabajo para llegar al resultado"), ("rúbrica", "tabla de criterios con niveles de logro"), ("evidencia de proceso", "registro que muestra cómo se trabajó")],
    worked=[
        ("Clasificar criterios", "¿Es «registro de versiones» un criterio de resultado o de proceso?", ["Se refiere a cómo se trabajó.", "Es parte del camino, no de la obra final."], "De proceso"),
        ("Sumar la rúbrica", "Un grupo obtiene 4, 3, 2 en tres criterios de resultado. ¿Cuántos puntos suma de un máximo de 12?", ["4 + 3 + 2 = 9.", "Máximo: 3 × 4 = 12."], "9 de 12"),
    ],
    mistakes=[("Evaluar solo el resultado.", "Se ignora cómo trabajó el grupo y qué aprendió.", "Agrega criterios de proceso con evidencia."),
              ("Poner un puntaje sin evidencia.", "Nadie puede comprobar por qué se asignó.", "Anota el compás, la versión o la anotación que lo respalda.")],
    T=[
        ('=', '{F} ¿Cuántos puntos de resultado suma el grupo (coherencia, dominio técnico y forma)?', '3+2+4', 'Se suman los tres puntajes de los criterios de resultado.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos de proceso suma el grupo?', '2+3+4', 'Se suman planificación, registro y colaboración.', ' puntos'),
        ('abc', '{F} ¿Qué criterio de resultado tiene el puntaje más alto?', 'Claridad de la forma, con el máximo de 4 puntos', 'Coherencia con el propósito', 'Dominio técnico', 'La forma tiene 4, el máximo posible.'),
        ('abc', '{F} ¿Qué criterio de proceso necesita más trabajo?', 'La planificación del ensayo, con 2', 'La colaboración, con 4', 'El registro de versiones, con 3', 'Tiene el puntaje más bajo de los tres criterios de proceso.'),
        ('abc', '¿Qué es una rúbrica?', 'Una tabla de criterios con niveles de logro', 'Un instrumento de percusión', 'Una opinión escrita', 'Describe qué se observa en cada nivel.'),
        ('abc', 'Un grupo obtuvo buen resultado, pero no registró versiones ni planificó. ¿Qué conclusión es válida?', 'El resultado fue bueno, pero el proceso tiene aspectos por mejorar', 'El grupo debe repetir todo', 'El proceso no importa si el resultado es bueno', 'Resultado y proceso se evalúan por separado.'),
        ('abc', '{F} ¿Cuál es una evidencia adecuada para el puntaje de registro 3?', 'Una bitácora con tres versiones y su efecto', 'La simpatía del grupo', 'El nombre de la obra', 'La evidencia de un puntaje debe poder comprobarse por otras personas.'),
        ('abc', '{F} Una compañera dice que el grupo debe tener 4 en todo para estar bien. ¿Qué respuesta es mejor?', 'Evaluar es describir qué se logró y qué falta, no exigir perfección', 'Tiene razón, todo debe ser 4', 'Los puntajes no importan', 'La evaluación sirve para orientar la mejora, no para exigir perfección.'),
        ('abc', '¿Cuál de estos es un criterio de proceso?', 'Colaboración en el grupo, que describe cómo se trabajó', 'Afinación de la voz, que describe la ejecución final', 'Claridad de la forma, que describe cómo suena la obra', 'Describe cómo se trabajó, no la obra final.'),
        ('abc', '{F} El grupo tiene dominio técnico 2. ¿Qué evidencia podría explicar ese puntaje?', 'Varias entradas fuera de pulso en un pasaje', 'Que la forma esté clara', 'Que trabajaron todos juntos', 'Se vincula al control de la ejecución.'),
        ('abc', 'Un grupo obtiene 11 de 12 en resultado y 3 de 12 en proceso. ¿Qué conviene hacer?', 'Planificar mejor el próximo trabajo, sin desvalorar el resultado', 'Descartar el resultado', 'Considerar el proceso irrelevante', 'Hay que mejorar el proceso sin negar lo logrado.'),
        ('=', '{F} ¿Cuántos puntos tiene como máximo la rúbrica completa, con sus 6 criterios de hasta 4 puntos?', '6*4', 'Son 6 criterios y cada uno vale como máximo 4 puntos.', ' puntos'),
        ('abc', 'Evaluar críticamente un trabajo es', 'describir lo logrado y lo que falta con criterios y evidencia', 'decir si el grupo cae bien', 'compararse con otros sin criterios', 'Incluye una postura fundada y respetuosa, con evidencia citada.'),
    ],
    ctx=('abc', 'En una clase, un grupo recibe «buen trabajo» sin más explicación. ¿Qué evaluación sería más útil para su aprendizaje?', 'Una con criterios, puntajes y evidencia de resultado y proceso', 'Una con un puntaje único sin explicación', 'Una que solo diga cuál grupo ganó', 'Los criterios y la evidencia permiten mejorar.'),
    sc=[
        ('¿Qué diferencia hay entre resultado y proceso?', 'El resultado es la obra final y el proceso es el camino para llegar a ella', 'Resultado y proceso se evalúan por separado con sus criterios.'),
        ('¿Cuántos puntos suman 4, 4 y 2?', '10', 'Al sumar 4 + 4 + 2 resulta 10.'),
        ('abc', 'Cada puntaje de una rúbrica debe', 'apoyarse en una evidencia que otra persona pueda comprobar', 'decidirse por simpatía', 'ser el mismo para todos', 'Sin evidencia no se puede comprobar.'),
    ],
    op=("Con la {F} como modelo, evalúa un trabajo tuyo o de ejemplo con tres criterios de resultado y tres de proceso (puntajes de 1 a 4), cita una evidencia para cada puntaje y escribe una frase de conclusión respetuosa.",
        "Resultado: coherencia 3 (el crescendo apoya la idea), forma 4 (partes claras), dominio técnico 2 (dos entradas fuera de pulso). Proceso: planificación 3, registro 2, colaboración 4. Conclusión: buen resultado, mejorar el registro de versiones.",
        ["seis criterios", "evidencia para cada puntaje", "conclusión respetuosa"], ["rúbrica completa"], ["puntajes sin evidencia", "evaluar a la persona"],
        "Reconoce la rúbrica y pide completar la evidencia de los puntajes bajos."),
    reinforce="Escribe tres criterios de proceso que usarías para evaluar un ensayo.",
    extend="Compara los criterios de esta rúbrica con los de otra actividad del colegio y señala dos diferencias.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (registro de ensayo de ejemplo de una interpretación de 8 compases en 4/4, escuchada por una compañera con una pauta). Compases con pulso estable: 1, 2, 3, 5, 6 y 8. Compases donde se apura el pulso: 4 y 7. "
     "Afinación: la voz desafina en el compás 6 en la nota larga. Balance: en los compases 3 y 4 la guitarra tapa la voz. Dicción: las palabras se entienden en todos los compases excepto el 7. Todo se grabó a volumen moderado.")
build(
    O6, 2, F,
    use="Aprenderé a evaluar aspectos técnicos de una interpretación (pulso, afinación, balance y claridad) con evidencia por compás, separando lo que se oye de lo que se supone.",
    prior=["Uso una rúbrica con evidencia.", "Entiendo qué es pulso estable y afinación.", "Sé qué es equilibrar los volúmenes."],
    explain=[
        "Los aspectos técnicos son los que se pueden observar en la ejecución y la producción. El pulso estable significa que el tempo se mantiene parejo, sin apurarse ni frenarse. La afinación es que las notas suenen en la altura correcta. El balance es que cada voz o instrumento tenga el volumen adecuado, de modo que la melodía se oiga y nadie quede tapado. La claridad, en canto, es que la letra se entienda; en un instrumento, que cada nota se distinga.",
        "Evaluar lo técnico con evidencia exige localizar el momento exacto: «en el compás 4 el pulso se apura» es una observación útil; «el pulso está mal» no lo es. Conviene anotar cuántos compases cumplen el criterio y cuáles no. Así se puede decidir qué trabajar primero y comprobar si hay mejora más adelante.",
        "Los aspectos técnicos se evalúan en relación con el propósito: una pequeña imperfección puede importar menos que un problema que impide oír la idea de la obra.",
    ],
    vocab=[("pulso estable", "tempo que se mantiene parejo, sin apurarse ni frenarse"), ("afinación", "que las notas suenen en la altura correcta"), ("balance", "volumen adecuado de cada voz o instrumento"), ("claridad", "que se entienda la letra o se distingan las notas"), ("evidencia por compás", "dato que indica en qué compás se observa algo")],
    worked=[
        ("Contar compases con problema", "En una interpretación de 8 compases, el pulso es estable en 5. ¿En cuántos no lo es?", ["Total de compases: 8.", "Con pulso estable: 5.", "Sin pulso estable: 8 − 5 = 3."], "3 compases"),
        ("Hacer una observación útil", "Reescribe «el balance está mal» para que sea una evidencia.", ["Hay que indicar qué compases y quién tapa a quién.", "Ejemplo: «En los compases 5 y 6 el bajo tapa la voz»."], "En los compases 5 y 6 el bajo tapa la voz"),
    ],
    mistakes=[("Decir «está desafinado» sin indicar dónde.", "No se sabe qué corregir.", "Señala el compás y la nota."),
              ("Evaluar la técnica sin considerar el propósito.", "Se puede priorizar un detalle menor y descuidar lo central.", "Pregunta qué problema impide que se escuche la idea de la obra.")],
    T=[
        ('=', '{F} ¿Cuántos compases tienen pulso estable?', '6', 'Los compases 1, 2, 3, 5, 6 y 8 son seis.', ' compases'),
        ('abc', '{F} ¿En qué compases se apura el pulso?', '4 y 7', '3 y 4', '6 y 7', 'La ficha los señala como 4 y 7.'),
        ('abc', '{F} ¿Dónde se escucha la desafinación?', 'En la nota larga del compás 6', 'En el compás 3', 'En todos los compases', 'La ficha la ubica en el compás 6.'),
        ('abc', '{F} ¿Qué problema de balance hay?', 'La guitarra tapa la voz en los compases 3 y 4', 'La voz tapa la guitarra en todo el trabajo', 'La percusión está desafinada', 'Se indica quién tapa a quién y dónde.'),
        ('abc', '{F} ¿En qué compás no se entiende la letra?', 'El 7', 'El 6', 'El 3', 'La ficha dice que en todos se entiende excepto en el 7.'),
        ('abc', '{F} ¿Qué compás tiene dos problemas: pulso apurado y letra poco clara?', 'El compás 7, donde el pulso se apura y además no se entiende la letra', 'El compás 4, donde la guitarra tapa la voz', 'El compás 6, donde la voz desafina', 'El 7 reúne el pulso apurado y la letra poco clara; el 4 tiene el pulso apurado, pero su letra sí se entiende.'),
        ('abc', 'Una evaluadora escribe «hay problemas de técnica». ¿Qué le falta?', 'Indicar el aspecto y el compás donde se observa', 'Subir la nota para compensar el comentario', 'Cambiar de tema para no discutir la técnica', 'Una evidencia debe ser localizable en un compás concreto.'),
        ('abc', '{F} ¿Qué ajuste podría resolver el balance de los compases 3 y 4?', 'Bajar el volumen de la guitarra', 'Subir el volumen de todo', 'Quitar la voz', 'Se equilibra sin subir el volumen general.'),
        ('abc', '{F} Si el propósito es que se entienda el mensaje de la letra, ¿qué problema es prioritario?', 'El balance en los compases 3 y 4 y la dicción del 7', 'La nota larga desafinada del compás 6', 'El pulso estable del compás 1', 'Ambos problemas impiden oír el texto de la canción.'),
        ('=', '{F} Si cada compás dura 3 segundos, ¿cuántos segundos dura la interpretación de 8 compases?', '8*3', 'Se multiplican los compases por los segundos de cada uno.', ' segundos'),
        ('abc', '¿Qué significa pulso estable?', 'El tempo se mantiene parejo, sin apurarse ni frenarse', 'Todos tocan lo más fuerte posible', 'La melodía no cambia', 'No se apura ni se frena.'),
        ('=', '{F} ¿En cuántos de los 8 compases se entiende la letra?', '8-1', 'Se entiende en todos los compases excepto el 7, así que se resta 1 del total.', ' compases'),
        ('abc', 'Evaluar la técnica de una grabación a volumen alto puede ser un problema porque', 'cansa el oído y puede ocultar detalles', 'siempre mejora la afinación', 'hace que el pulso sea estable', 'El volumen moderado cuida la audición.'),
    ],
    ctx=('abc', 'Una estudiante evalúa a un compañero y dice: «Estuvo bien, pero el pulso se apuró». El compañero pregunta dónde. ¿Qué respuesta es más útil?', 'En los compases 4 y 7, donde el pulso se apura', 'En todas partes, creo', 'No me acuerdo, pero se sentía', 'La evidencia localizada permite saber exactamente qué corregir.'),
    sc=[
        ('¿Qué es el balance?', 'El volumen adecuado de cada voz o instrumento', 'Que la melodía se oiga y nadie quede tapado.'),
        ('Si 6 de 8 compases tienen pulso estable, ¿cuántos no lo tienen?', '2', 'Al restar 6 de 8 quedan 2 compases.'),
        ('abc', 'Una evidencia técnica útil es', 'la que indica el compás donde ocurre', 'la que dice «está mal»', 'la que compara con otro grupo', 'Una evidencia útil debe poder localizarse en la interpretación.'),
    ],
    op=("Con la {F} como modelo, escribe una evaluación técnica de una interpretación de 8 compases (real o de ejemplo) con cuatro aspectos: pulso, afinación, balance y claridad. Cita el compás de cada observación y prioriza uno según el propósito.",
        "Pulso estable en 5 de 8 compases (se apura en 4 y 7). Afinación: se desafina en el compás 6. Balance: la guitarra tapa la voz en 3 y 4. Claridad: la letra no se entiende en el 7. Prioridad: el balance, porque el propósito es contar una historia.",
        ["cuatro aspectos", "compás citado", "prioridad justificada"], ["evaluación técnica"], ["observaciones sin compás", "no priorizar"],
        "Reconoce la evaluación y pide ubicar cada observación en un compás."),
    reinforce="Escucha una grabación tuya y anota en qué compás se apura o se frena el pulso.",
    extend="Propón un ejercicio de dos minutos para mejorar el pulso estable en los compases problemáticos.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (cuatro comentarios de ejemplo sobre la interpretación de una compañera que canta una canción propia en 6 compases). "
     "Comentario 1: «Lo hiciste pésimo, se nota que no practicaste.» Comentario 2: «Me gustó la parte del estribillo.» "
     "Comentario 3: «En los compases 3 y 4 el volumen de la guitarra tapó tu voz; probaría bajarla un poco para que se entienda la letra, porque tu propósito era contar una historia.» "
     "Comentario 4: «Todo estuvo perfecto, nada que cambiar.»")
build(
    O6, 3, F,
    use="Aprenderé a dar retroalimentación a pares que sea específica, fundada en criterios y respetuosa, y a sostener una postura personal sin descalificar a la persona.",
    prior=["Evalúo con rúbrica y evidencia.", "Reconozco aspectos técnicos.", "Separo evaluar el trabajo de juzgar a la persona."],
    explain=[
        "La retroalimentación entre pares es el comentario que se da a un compañero o compañera para ayudar a mejorar su trabajo. Para que sirva debe ser específica (señala qué y dónde), fundada (se apoya en un criterio y una evidencia), respetuosa (habla del trabajo, no de la persona) y útil (propone un camino posible). Una estructura que ayuda: lo que funciona y por qué, lo que podría mejorar con evidencia y una sugerencia.",
        "Una postura personal fundada y respetuosa implica decir lo que piensas con razones, sin ofender y aceptando que la otra persona puede ver otras cosas. «Lo hiciste pésimo» descalifica; «Todo estuvo perfecto» no ayuda; «Me gustó» agrada, pero no orienta. En cambio, un comentario con compás, criterio, sugerencia y propósito sí permite mejorar.",
        "Recibir retroalimentación también se practica: se escucha completa, se pregunta si algo no queda claro y se decide qué cambiar. No hay que cambiarlo todo; se prioriza.",
    ],
    vocab=[("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("específica", "que indica qué y dónde"), ("fundada", "apoyada en criterio y evidencia"), ("respetuosa", "que habla del trabajo y no ofende a la persona"), ("sugerencia", "propuesta concreta para mejorar")],
    worked=[
        ("Evaluar un comentario", "¿Por qué el comentario 3 de la ficha es útil?", ["Señala dónde: compases 3 y 4.", "Se apoya en un criterio: el balance.", "Propone una sugerencia: bajar la guitarra."], "Es específico, fundado y propone una sugerencia"),
        ("Contar compases afectados", "La guitarra tapó la voz en los compases 3 y 4. ¿Cuántos compases son de los 6?", ["Compases 3 y 4: 2.", "Fracción: 2 de 6."], "2 de 6 compases"),
    ],
    mistakes=[("Confundir sinceridad con descalificar.", "Un comentario ofensivo no entrega información y puede bloquear a la persona.", "Habla del trabajo y ofrece una sugerencia."),
              ("Decir solo «me gustó».", "Agrada pero no orienta.", "Agrega qué funcionó y por qué.")],
    T=[
        ('abc', '{F} ¿Cuál comentario es más útil para mejorar?', 'El comentario 3, que indica compás, criterio y sugerencia', 'El comentario 1, porque es el más sincero', 'El comentario 4, porque es muy positivo', 'Es específico, fundado y propone una sugerencia.'),
        ('abc', '{F} ¿Por qué el comentario 1 no sirve?', 'Descalifica y no dice qué ni dónde', 'Es demasiado largo', 'Menciona compases', 'Ataca a la persona sin dar evidencia.'),
        ('abc', '{F} ¿Qué le falta al comentario 2 para orientar?', 'Decir por qué funcionó esa parte y en qué instante se nota', 'Un elogio más largo y entusiasta', 'Un tono más severo', 'Un elogio sin razones no guía.'),
        ('abc', '{F} ¿Qué problema tiene el comentario 4?', 'No identifica nada concreto ni ayuda a mejorar', 'Es demasiado crítico', 'Menciona demasiados compases', 'Decir que todo es perfecto no aporta información.'),
        ('abc', '{F} ¿Qué criterio usa el comentario 3?', 'Balance entre voz y guitarra', 'Dominio técnico del pulso', 'Originalidad', 'Habla de que la guitarra tapa la voz.'),
        ('abc', '{F} ¿Qué propósito de la autora menciona el comentario 3?', 'Contar una historia', 'Hacer bailar', 'Calmar', 'La ficha lo dice de manera explícita en el comentario.'),
        ('abc', 'Para ser respetuosa, una retroalimentación debe hablar de', 'el trabajo, no de la persona', 'la persona que lo hizo', 'quién ganó el año pasado', 'El foco está en el trabajo.'),
        ('=', '{F} La guitarra tapó la voz en 2 de los 6 compases. ¿Cuántos compases se oyeron con buen balance?', '6-2', 'Se restan los compases con problema del total.', ' compases'),
        ('abc', 'Un estudiante dice: «Soy sincero, por eso puedo decir lo que quiera». ¿Qué respuesta es mejor?', 'Se puede ser sincero y respetuoso a la vez, hablando del trabajo con evidencia', 'Es cierto, sinceridad no tiene límites', 'Mejor no decir nunca nada', 'Sinceridad y respeto no se oponen.'),
        ('abc', '{F} Si la autora recibe los cuatro comentarios, ¿qué conviene hacer?', 'Priorizar el 3 y probar la sugerencia', 'Cambiar todo el trabajo', 'Ignorar todos', 'Se elige lo que aporta información útil.'),
        ('abc', 'Una buena estructura para retroalimentar es', 'lo que funciona y por qué, lo que puede mejorar con evidencia, y una sugerencia', 'solo los defectos, ordenados de mayor a menor gravedad', 'solo elogios generales para que nadie se sienta mal', 'Esa estructura combina reconocimiento y mejora.'),
        ('abc', '{F} Un comentario dice «tu voz no suena bien». ¿Cómo hacerlo más específico?', 'Indicar el compás y qué nota desafina', 'Decir que suena aún peor', 'Agregar un chiste', 'Hay que localizar el problema para que se pueda corregir.'),
        ('abc', 'Al recibir un comentario poco claro, conviene', 'preguntar a qué compás o criterio se refiere para obtener la evidencia', 'aceptarlo sin preguntar', 'ignorarlo, porque no sirve', 'Preguntar ayuda a obtener la evidencia que falta.'),
    ],
    ctx=('abc', 'Una estudiante debe dar su opinión sobre la presentación de un compañero. Piensa que el volumen de la percusión tapó la letra en el estribillo. ¿Qué comentario escribe?', 'En el estribillo la percusión tapó la letra; propongo bajarla, porque el mensaje importa', 'La percusión estuvo horrible, no se entendió nada', 'Estuvo bien, no se me ocurre nada que cambiar', 'Es específico, fundado y propone una sugerencia respetuosa.'),
    sc=[
        ('En Música: ¿Qué hace específico a un comentario?', 'Indica qué observó y dónde', 'Ubica la observación para poder mejorarla.'),
        ('¿Cuántos compases bien balanceados hay si 3 de 8 tienen problemas?', '5', 'Al restar 3 de 8 quedan 5 compases.'),
        ('abc', 'Una postura fundada y respetuosa', 'da razones y no ofende', 'solo elogia', 'solo critica', 'Combina criterio, evidencia y respeto por la otra persona.'),
    ],
    op=("Con la {F} como modelo, escribe un comentario de retroalimentación para una interpretación (real o de ejemplo) con tres partes: lo que funciona y por qué, lo que podría mejorar con evidencia (compás o instante) y una sugerencia concreta.",
        "Funciona: la voz suave del primer compás crea cercanía. Mejorar: en los compases 5 y 6 se apura el pulso. Sugerencia: contar en voz baja «1, 2, 3, 4» y practicar a tempo lento.",
        ["tres partes", "evidencia localizada", "sugerencia concreta"], ["comentario escrito"], ["comentario ofensivo", "sin evidencia"],
        "Reconoce el comentario y pide agregar el criterio al que se refiere."),
    reinforce="Reescribe el comentario «Lo hiciste mal» para que sea específico y respetuoso.",
    extend="Practica pedir retroalimentación: escribe dos preguntas concretas para hacer a quien evalúa tu trabajo.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (bitácora de proceso de ejemplo de un estudiante que prepara una interpretación de 8 compases durante 4 sesiones). "
     "Sesión 1: 15 minutos; tocó la pieza completa sin parar; anotó «salió bien». Sesión 2: 20 minutos; aisló los compases 5 y 6; pulso estable en 1 de 3 intentos. "
     "Sesión 3: 20 minutos; trabajó 5 y 6 a tempo lento; pulso estable en 3 de 3 intentos. Sesión 4: 25 minutos; pieza completa; el compás 6 salió estable y el 8 se apuró. "
     "Autoevaluación escrita: «Mi proceso fue excelente; no tengo nada que cambiar.»")
build(
    O6, 4, F,
    use="Aprenderé a evaluar críticamente mi propio proceso y resultado con la ayuda de la bitácora, evitando tanto la autocomplacencia como la dureza excesiva, y reconociendo evidencias de mejora.",
    prior=["Uso una rúbrica de proceso y resultado.", "Doy retroalimentación fundada.", "Registro versiones y cambios."],
    explain=[
        "Autoevaluar es evaluar tu propio trabajo con los mismos criterios con que evaluarías el de otra persona. La bitácora aporta la evidencia de proceso: cuánto tiempo practicaste, qué trabajaste, qué resultados tuviste y qué cambios hiciste. Con esas evidencias puedes ver si tu proceso fue eficaz, por ejemplo si aislar los compases difíciles produjo mejora.",
        "Dos sesgos son comunes. La autocomplacencia es decir «todo está perfecto» sin evidencia; la dureza excesiva es decir «soy un desastre» sin evidencia. Ambos impiden mejorar. Una autoevaluación equilibrada reconoce logros con datos, identifica lo que falta con datos y propone un cambio concreto. Se dice «en la sesión 3 el pulso estuvo estable 3 de 3 veces al trabajar a tempo lento» y no «soy bueno» o «soy malo».",
        "Evaluar también el resultado: en la sesión 4, ¿qué compases cumplen el criterio y cuáles no? Así se decide el siguiente paso.",
    ],
    vocab=[("autoevaluación", "evaluación del propio trabajo con criterios y evidencia"), ("autocomplacencia", "creer que todo está bien sin evidencia"), ("dureza excesiva", "criticarse más de lo que muestra la evidencia"), ("evidencia de proceso", "dato de la bitácora sobre cómo se trabajó"), ("eficaz", "que produce el resultado esperado")],
    worked=[
        ("Medir una mejora", "En la sesión 2 el estudiante logró el pulso estable en 1 de 3 intentos y en la sesión 3, en 3 de 3. ¿Cuántos intentos estables más logró?", ["Sesión 3: 3.", "Sesión 2: 1.", "3 − 1 = 2 intentos estables más."], "2 intentos más"),
        ("Detectar un sesgo", "El estudiante escribe «Mi proceso fue excelente; no tengo nada que cambiar». ¿Qué sesgo muestra?", ["Afirma que todo es perfecto.", "No cita evidencia y ignora que el compás 8 se apuró."], "Autocomplacencia"),
    ],
    mistakes=[("Escribir «salió bien» como única evidencia.", "No dice qué compases ni con qué calidad.", "Anota cuántos intentos fueron estables y en qué compás."),
              ("Pensar que reconocer un error es un fracaso.", "Es información para decidir el siguiente paso.", "Escribe el error con datos y una acción para corregirlo.")],
    T=[
        ('=', '{F} ¿Cuántos minutos practicó el estudiante en total en las cuatro sesiones?', '15+20+20+25', 'Se suman los minutos de las cuatro sesiones.', ' minutos'),
        ('abc', '{F} ¿Qué estrategia produjo mejora entre las sesiones 2 y 3?', 'Trabajar los compases 5 y 6 a tempo lento', 'Tocar la pieza completa sin parar', 'Practicar menos tiempo', 'La mejora coincide con el trabajo a tempo lento.'),
        ('abc', '{F} ¿Por qué la autoevaluación escrita es autocomplaciente?', 'Dice que no hay nada que cambiar aunque el compás 8 se apuró', 'Cita datos de la bitácora', 'Menciona los compases', 'Ignora la evidencia del compás 8.'),
        ('abc', '{F} ¿Qué evidencia de la sesión 4 muestra un aspecto por mejorar?', 'El compás 8 se apuró al tocar la pieza completa', 'El compás 6 salió estable', 'La sesión duró 25 min', 'Es el único problema señalado para esa sesión.'),
        ('abc', '{F} ¿Qué autoevaluación es más equilibrada?', '«El pulso mejoró de 1 a 3 intentos estables en los compases 5 y 6; falta el compás 8»', '«Soy pésimo, no sirvo para esto y me equivoco siempre»', '«Todo salió perfecto, no hay nada que mejorar»', 'Reconoce logros y límites con datos.'),
        ('abc', 'La dureza excesiva consiste en', 'criticarse más de lo que muestra la evidencia', 'reconocer un error con datos', 'felicitarse con razones', 'Va más allá de lo que se comprueba.'),
        ('abc', '{F} En la sesión 1 el estudiante anotó «salió bien». ¿Qué falta en esa anotación?', 'Compases, intentos y calidad observable', 'Un adjetivo más positivo', 'La opinión de otra persona', 'Debe haber datos que la respalden.'),
        ('abc', '{F} La sesión 4 se dedicó a la pieza completa. ¿Qué decisión es razonable para una sesión 5?', 'Trabajar el compás 8 a tempo lento', 'Dejar de practicar', 'Repetir la pieza completa rápido', 'Se aplica la estrategia que ya funcionó al nuevo problema.'),
        ('abc', 'Un estudiante dice: «Mis errores demuestran que no tengo talento». ¿Qué respuesta es más adecuada?', 'Los errores son información para ajustar el proceso', 'Tiene razón, debe abandonar', 'Los errores no existen', 'El error indica qué conviene trabajar en adelante.'),
        ('=', '{F} ¿Cuántos minutos más practicó en la sesión 4 que en la sesión 1?', '25-15', 'Se resta la duración de la sesión 1 de la duración de la sesión 4.', ' minutos'),
        ('abc', '{F} ¿Qué dato muestra la eficacia de aislar los compases 5 y 6?', 'Pasó de 1 a 3 intentos estables de 3 al trabajar esos compases', 'Dedicó 25 minutos a la sesión 4', 'Dijo que su proceso fue excelente', 'Compara dos sesiones usando datos de la bitácora.'),
        ('abc', 'La autoevaluación se apoya en', 'la bitácora, que muestra cómo se trabajó, y los criterios', 'la opinión de quien no vio el trabajo', 'el humor del día', 'La bitácora aporta la evidencia de cómo se trabajó.'),
        ('abc', '{F} ¿Cuántos compases se mencionan con problemas en la sesión 4?', '1', '2', '3', 'Solo el compás 8 se apuró.'),
    ],
    ctx=('abc', 'Una estudiante revisa su bitácora y ve que, aunque practicó 30 minutos diarios, el compás 3 se mantiene desafinado. ¿Qué conclusión sobre su proceso es la más razonable?', 'Debe cambiar la estrategia de práctica, por ejemplo aislar ese compás', 'Debe practicar lo mismo por más tiempo', 'No hay nada que cambiar', 'El tiempo por sí solo no garantiza mejora; hay que ajustar el método.'),
    sc=[
        ('¿Qué es la autocomplacencia?', 'Creer que todo está bien sin evidencia', 'Impide detectar lo que falta mejorar.'),
        ('¿Cuántos minutos suman sesiones de 10, 15 y 20 minutos?', '45', 'Al sumar 10 + 15 + 20 resulta 45.'),
        ('abc', 'Una autoevaluación equilibrada', 'reconoce logros y límites con datos', 'solo muestra logros', 'solo muestra errores', 'Combina ambas miradas apoyándose siempre en evidencia.'),
    ],
    op=("Con la {F} como modelo, escribe tu propia autoevaluación de un proceso de práctica de tres sesiones (pueden ser de ejemplo): datos de cada sesión, un logro con evidencia, un límite con evidencia y una acción para la próxima sesión.",
        "Sesión 1: 10 min, pieza completa. Sesión 2: 15 min, aislé el compás 4. Sesión 3: 20 min, compases 3 y 4 a tempo lento. Logro: el pulso del compás 4 pasó de 1 a 3 intentos estables. Límite: el compás 5 sigue apurado. Acción: trabajar el 5 a tempo lento.",
        ["datos por sesión", "logro y límite con evidencia", "acción concreta"], ["autoevaluación escrita"], ["autocomplacencia", "dureza excesiva"],
        "Reconoce la autoevaluación y pide agregar un dato numérico al límite."),
    reinforce="Anota en una bitácora cuánto practicaste hoy, qué trabajaste y un resultado observable.",
    extend="Compara dos bitácoras (la tuya y una de ejemplo) y señala qué estrategia parece más eficaz.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (diagnóstico de ejemplo de un grupo después de su presentación). Fortalezas con evidencia: forma clara (3 partes bien diferenciadas) y buena colaboración (todas las personas tocaron en al menos dos partes). "
     "Debilidades con evidencia: balance (la percusión tapó la voz en 4 de los 10 compases) y pulso (se apuró en 3 de los 10 compases). Propósito: transmitir alegría. Tiempo disponible: 3 ensayos de 20 minutos antes de la próxima presentación.")
build(
    O6, 5, F,
    use="Aprenderé a registrar una evaluación crítica y a convertirla en un plan de mejora con prioridades, metas medibles y seguimiento, apoyándome en la evidencia y en el propósito expresivo.",
    prior=["Evalúo resultado y proceso con evidencia.", "Doy retroalimentación fundada.", "Hago una autoevaluación equilibrada."],
    explain=[
        "Una evaluación crítica tiene sentido si lleva a mejorar. El paso final es un plan de mejora: se listan las fortalezas (para conservarlas), se priorizan las debilidades según su efecto en el propósito expresivo y se fijan metas medibles. Una meta medible dice qué, cuánto y cómo se comprobará: «lograr que la percusión no tape la voz en ningún compás en la próxima grabación».",
        "Para priorizar se pregunta cuál debilidad impide más que se cumpla el propósito. Si el propósito es transmitir alegría y la percusión tapa la voz en 4 de 10 compases, el balance afecta más directamente que un pulso apurado en 3 de 10. También se organiza el tiempo: si hay 3 ensayos de 20 minutos, hay 60 minutos en total, que se reparten entre las tareas.",
        "El seguimiento consiste en volver a evaluar con los mismos criterios para comprobar si la meta se cumplió. Si no se cumplió, se ajusta el plan; no se abandona.",
    ],
    vocab=[("plan de mejora", "lista de acciones, prioridades y metas para corregir debilidades"), ("fortaleza", "aspecto logrado que conviene conservar"), ("debilidad", "aspecto por mejorar"), ("meta medible", "objetivo que dice qué, cuánto y cómo se comprobará"), ("seguimiento", "nueva evaluación con los mismos criterios para ver si hubo mejora")],
    worked=[
        ("Calcular el tiempo disponible", "Un grupo tiene 4 ensayos de 15 minutos. ¿Cuántos minutos tiene en total?", ["4 ensayos.", "4 × 15 = 60 minutos."], "60 minutos"),
        ("Redactar una meta medible", "Convierte «mejorar el pulso» en una meta medible para un pasaje de 8 compases.", ["Hay que decir qué, cuánto y cómo se comprueba.", "Ejemplo: tocar los 8 compases con pulso estable en 3 de 3 intentos."], "Tocar los 8 compases con pulso estable en 3 de 3 intentos"),
    ],
    mistakes=[("Fijar metas como «tocar mejor».", "No se puede comprobar si se cumplió.", "Dice qué, cuánto y cómo se comprobará."),
              ("Trabajar todas las debilidades al mismo tiempo.", "El tiempo se dispersa y no se nota avance.", "Prioriza según el propósito y reparte el tiempo.")],
    T=[
        ('=', '{F} ¿Cuántos minutos de ensayo tiene el grupo en total?', '3*20', 'Se multiplican los ensayos por los minutos de cada uno.', ' minutos'),
        ('=', '{F} ¿En cuántos compases la percusión no tapó la voz?', '10-4', 'Se resta del total los compases con problema.', ' compases'),
        ('abc', '{F} ¿Qué debilidad conviene priorizar para el propósito de alegría?', 'El balance, porque la percusión tapa la voz', 'El pulso, porque se apuró más veces', 'Ninguna, porque son fortalezas', 'Si no se oye la voz, el mensaje de alegría se pierde; además el balance falló en más compases.'),
        ('abc', '{F} ¿Cuál es una fortaleza con evidencia?', 'La forma clara en tres partes diferenciadas', 'Que la percusión tape la voz', 'Que el pulso se apure', 'Es lo que el grupo logró con claridad.'),
        ('abc', '{F} ¿Cuál es la mejor meta medible para el balance?', 'Que la percusión no tape la voz en ningún compás de la próxima grabación', 'Equilibrar mejor el sonido en la próxima presentación', 'Que la canción suene más linda para todo el público', 'Dice qué, cuánto y cómo se comprueba.'),
        ('abc', '{F} Si dedican 30 minutos al balance y el resto al pulso, ¿cuántos minutos quedan para el pulso?', '30', '20', '40', '60 minutos totales menos 30 dejan 30 minutos.'),
        ('abc', 'El seguimiento de un plan de mejora consiste en', 'volver a evaluar con los mismos criterios', 'cambiar de criterios cada vez', 'esperar sin revisar', 'Permite comprobar si la meta se cumplió.'),
        ('abc', '{F} El pulso se apuró en 3 de los 10 compases. ¿Qué meta es medible?', 'Tocar los 10 compases con pulso estable en 2 de 2 intentos', 'Tocar con más cuidado y concentración', 'No apurarse nunca más en ninguna presentación', 'Indica cuánto y cómo se comprueba.'),
        ('abc', 'Un grupo cumple su meta, pero no registra la nueva evaluación. ¿Qué falta?', 'La evidencia que muestra que se cumplió', 'Una meta más corta', 'Una opinión de otro grupo', 'Sin registro de la nueva evaluación no hay seguimiento real.'),
        ('abc', '{F} ¿Por qué conviene conservar las fortalezas en el plan?', 'Para no perderlas mientras se trabajan las debilidades', 'Porque no necesitan práctica jamás', 'Porque así se evita evaluar', 'Lo logrado también debe mantenerse mientras se mejora el resto.'),
        ('abc', '{F} Si el grupo logra la meta de balance en el primer ensayo, ¿qué decisión es razonable?', 'Pasar a la siguiente prioridad y comprobar el balance al final', 'Dejar de ensayar porque la meta ya se cumplió', 'Cambiar el propósito para que no haya más metas', 'Se avanza y se confirma que la mejora se mantiene.'),
        ('abc', 'Un plan de mejora no debería', 'ignorar el propósito expresivo', 'incluir fortalezas', 'incluir metas medibles', 'La prioridad se decide según el propósito.'),
        ('abc', '{F} El balance fue deficiente en 4 de los 10 compases. ¿Qué afirmación es correcta?', 'Es menos de la mitad de los compases, pero una proporción importante', 'Es más de la mitad de los compases', 'Es casi la totalidad de los compases', '4 de 10 es menos de la mitad, aunque no es poco.'),
    ],
    ctx=('abc', 'Un grupo recibe tres comentarios: mejorar el pulso, mejorar el balance y mejorar la afinación. Tiene dos ensayos de 20 minutos. ¿Qué es lo más razonable?', 'Priorizar una o dos debilidades según el propósito y fijar una meta medible', 'Intentar mejorarlo todo sin prioridades', 'Esperar a que se arreglen solas', 'Con poco tiempo hay que priorizar.'),
    sc=[
        ('¿Qué dice una meta medible?', 'Qué, cuánto y cómo se comprobará', 'Permite saber con claridad si la meta se cumplió.'),
        ('¿Cuántos minutos son 2 ensayos de 25 minutos?', '50', 'Se multiplican 2 por 25 minutos.'),
        ('abc', 'Para priorizar una debilidad se mira', 'cuánto afecta el propósito expresivo', 'cuál es la más fácil de nombrar', 'cuál comentó otro grupo', 'El propósito expresivo orienta cuál debilidad es la prioridad.'),
    ],
    op=("Con la {F} como modelo, escribe un plan de mejora para un trabajo tuyo o de ejemplo: una fortaleza a conservar, dos debilidades con evidencia, la prioridad justificada por el propósito, una meta medible y cómo harás el seguimiento.",
        "Fortaleza: forma clara. Debilidades: la voz se pierde en 3 de 8 compases; el final se apura. Prioridad: la voz, porque el propósito es contar una historia. Meta: que la voz se entienda en los 8 compases en 2 de 2 grabaciones. Seguimiento: grabar al final del último ensayo y revisar la pauta.",
        ["fortaleza", "prioridad justificada", "meta medible y seguimiento"], ["plan de mejora"], ["metas vagas", "no priorizar"],
        "Reconoce el plan y pide agregar cómo comprobará la meta."),
    reinforce="Escribe una meta medible para mejorar la afinación de una frase de una canción.",
    extend="Después de aplicar tu plan, evalúa de nuevo con los mismos criterios y compara los resultados.",
)
