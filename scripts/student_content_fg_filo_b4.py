"""Filosofía 4.º medio FG: OA 01 (alcances, límites y fines de la filosofía). Casos y textos de ejemplo inventados."""
from __future__ import annotations

from fg_filo_common import build

O1 = "FG-FILO-4M-OAC-01"

# ============================================================ OA 01, clase 1
F = ("Ficha 1 (tres opiniones de ejemplo en un liceo): "
     "Inés: «La filosofía no sirve: no produce nada que se pueda vender». "
     "Pablo: «Sirve para decidir mejor, por ejemplo para acordar con qué criterio repartir el fondo del curso». "
     "Rosa: «Sirve, pero hay preguntas que ni ella ni las ciencias pueden cerrar del todo».")
build(
    O1, 1, F,
    use="Aprenderé a transformar la pregunta «¿para qué sirve la filosofía?» en problemas más precisos sobre sus alcances, sus límites y sus fines.",
    prior=["Sé qué es una pregunta ontológica, epistemológica y ética.", "Sé distinguir un argumento de una opinión suelta.", "Sé que una pregunta debe aclararse antes de responderla."],
    explain=[
        "«¿Para qué sirve la filosofía?» es una pregunta que mezcla tres problemas. El alcance es hasta dónde llega la filosofía: qué tipos de preguntas puede tratar. El límite es lo que no puede lograr o dejar resuelto. El fin es el propósito por el cual vale la pena hacerla. Separar los tres permite discutir con razones y no solo con gustos.",
        "También conviene distinguir dos sentidos de «servir». Algo tiene valor instrumental cuando sirve para conseguir otra cosa, como una herramienta que ayuda a construir. Algo tiene valor propio cuando vale por sí mismo, como entender mejor el mundo. La opinión de Inés mide la filosofía solo por su valor instrumental en el comercio; Pablo mira cómo ayuda a decidir; Rosa habla de un límite.",
        "Problematizar la situación es hallar qué se afirma, qué se supone y qué pregunta queda abierta. Inés supone que solo vale lo que se vende; Pablo supone que decidir con criterio es valioso; Rosa supone que algunas preguntas no se cierran. Ninguna de las tres puede darse por probada sin razones.",
    ],
    vocab=[("alcance", "hasta dónde llega una disciplina: qué preguntas puede tratar"), ("límite", "aquello que una disciplina no puede lograr o dejar resuelto"), ("fin", "propósito por el cual vale la pena hacer algo"), ("valor instrumental", "valor de lo que sirve para conseguir otra cosa"), ("valor propio", "valor de lo que vale por sí mismo")],
    worked=[
        ("Clasificar una afirmación", "Una compañera de ejemplo dice: «La filosofía no puede decirnos cuánto mide el río». ¿Habla de alcance, límite o fin?", ["Dice algo que la filosofía no puede lograr.", "Eso es un límite."], "Límite"),
        ("Tipo de valor", "Un amigo de ejemplo dice: «Estudio matemática porque me sirve para entrar a una carrera». ¿Qué tipo de valor da a la matemática?", ["La usa para conseguir otra cosa.", "Es un valor instrumental."], "Instrumental"),
    ],
    mistakes=[("Responder «sirve» o «no sirve» sin decir para qué.", "La pregunta tiene varios sentidos de «servir».", "Pregunta si hablas de alcance, de límite o de fin."),
              ("Creer que si algo no se vende no tiene valor.", "Se confunde valor instrumental con valor propio.", "Distingue lo que sirve para otra cosa de lo que vale por sí mismo.")],
    T=[
        ('abc', '¿Qué es el alcance de una disciplina?', 'Hasta dónde llega: qué tipos de preguntas puede tratar', 'Lo que no puede lograr ni dejar resuelto', 'El propósito por el cual vale la pena practicarla', 'El alcance se refiere al campo de preguntas; el límite y el fin son otras cosas.'),
        ('abc', '{F} ¿Qué mide Inés al juzgar la filosofía?', 'Solo si produce algo que se pueda vender', 'Si ayuda a decidir con razones sobre cuestiones comunes', 'Si responde preguntas que las ciencias no resuelven', 'Inés usa el comercio como criterio único; las otras dos opiniones usan otros.'),
        ('abc', '{F} ¿Qué afirma Rosa sobre la filosofía?', 'Que sirve, pero tiene preguntas que no se pueden cerrar del todo', 'Que no sirve porque no entrega datos precisos y medibles', 'Que sirve para vender mejor sus ideas en el comercio', 'Rosa reconoce un valor y un límite al mismo tiempo.'),
        ('abc', '{F} ¿Qué ejemplo da Pablo de un uso de la filosofía?', 'Acordar con qué criterio repartir el fondo del curso', 'Medir cuánto dinero tiene el curso y cuánto falta para la gira', 'Saber cuántas personas hay en el liceo', 'Pablo habla de decidir con criterio, algo que requiere razones y no solo datos.'),
        ('abc', '{F} ¿Qué supone Inés?', 'Que solo vale lo que se puede vender', 'Que la filosofía siempre da la respuesta correcta', 'Que las ciencias no tienen límites', 'Su juicio depende de ese supuesto, que se puede discutir.'),
        ('abc', 'Alguien dice: «Aprendo a tocar guitarra solo porque me gusta». ¿Qué valor le da a la guitarra?', 'Valor propio', 'Valor instrumental', 'Valor comercial', 'Lo hace por sí mismo y no para conseguir otra cosa.'),
        ('abc', '¿Qué significa decir que algo tiene valor instrumental?', 'Que sirve para conseguir otra cosa', 'Que vale por sí mismo, sin importar sus usos', 'Que es un instrumento musical o una herramienta', 'Instrumental se refiere a ser un medio para otro fin, no a ser un objeto.'),
        ('abc', '{F} ¿Por qué la pregunta «¿sirve la filosofía?» necesita ser aclarada antes de responder?', 'Porque «servir» puede significar cosas distintas: valor instrumental, valor propio, alcance o límite', 'Porque todo el mundo sabe la respuesta y no hace falta discutir', 'Porque la filosofía no se puede discutir con razones', 'Las tres personas usan «servir» con sentidos diferentes.'),
        ('abc', 'Texto de ejemplo: «La filosofía no puede decirnos cuánto llovió ayer». ¿De qué habla?', 'Del límite de la filosofía', 'Del fin de la filosofía', 'Del alcance de las ciencias', 'Dice lo que la filosofía no puede responder: es un límite.'),
        ('abc', 'Texto de ejemplo: «La filosofía puede ayudarnos a examinar qué entendemos por justicia». ¿De qué habla?', 'Del alcance de la filosofía', 'Del límite de la filosofía', 'De un dato medible', 'Dice qué tipo de preguntas puede tratar, que es su alcance.'),
        ('{F} Escribe una pregunta que ayude a Inés y Pablo a ponerse de acuerdo antes de discutir.', '¿Qué entendemos por «servir»?', 'Define el término clave que ambos usan con sentidos distintos.'),
        ('abc', '{F} Si Rosa tiene razón en que la filosofía tiene preguntas que no se cierran, ¿qué se sigue?', 'Que su valor no depende de cerrar todas las preguntas', 'Que no vale la pena hacer filosofía', 'Que las ciencias deben reemplazarla en todas las preguntas que ella trata', 'Un límite no elimina el valor: puede seguir ayudando a pensar y decidir mejor.'),
        ('abc', '{F} ¿Cuál es una buena conclusión provisoria?', 'Habrá que precisar alcances, límites y fines antes de decir si sirve', 'La opinión de Inés es correcta, porque es la más sencilla', 'La de Pablo es correcta, porque da un ejemplo', 'Con una sola frase no basta: hay que precisar qué se pregunta y con qué criterios.'),
    ],
    ctx=('abc', 'Un grupo de ejemplo discute si conviene que el liceo ofrezca un taller de filosofía. Uno dice: «Solo vale la pena si sube las notas en otras materias». ¿Qué tipo de valor usa como criterio?', 'Instrumental, porque se mide por otro resultado', 'Propio, porque vale en sí mismo', 'Ninguno, porque no hay criterio', 'Solo lo valora si sirve para conseguir mejores notas.'),
    sc=[
        ('En Filosofía: ¿qué es el límite de una disciplina?', 'Lo que no puede lograr o dejar resuelto', 'Es aquello a lo que no llega.'),
        ('abc', '¿Qué es el fin de una actividad?', 'El propósito por el cual vale la pena hacerla', 'El momento en que termina', 'Hasta dónde llegan las preguntas que puede tratar esa actividad', 'Fin es propósito; hasta dónde llega es el alcance.'),
        ('¿Qué es un valor propio?', 'El de lo que vale por sí mismo', 'No depende de que sirva para otra cosa.'),
    ],
    op=("Usa la {F} Escribe una tabla de tres filas con Inés, Pablo y Rosa: qué supone cada una, si habla de alcance, límite o fin, y una pregunta que le harías. Cierra con una frase que no defienda a nadie y diga qué hay que aclarar.",
        "Inés: supone que solo vale lo vendible; valor instrumental; ¿qué cosas valen aunque no se vendan? Pablo: supone que decidir con criterio es valioso; alcance y fin; ¿qué pasa cuando no hay acuerdo? Rosa: supone que algunas preguntas no se cierran; límite; ¿cuáles? Cierre: hay que aclarar qué significa «servir».",
        ["identifica supuestos", "clasifica en alcance, límite o fin", "formula preguntas"], ["tabla de tres filas", "frase final"], ["tomar partido sin razones", "no distinguir alcance y fin"],
        "Pide que explique cuál de las tres preguntas haría avanzar más el diálogo."),
    reinforce="Escribe una pregunta sobre el alcance, otra sobre el límite y otra sobre el fin de la filosofía.",
    extend="Pregunta a una persona de tu entorno para qué le sirve pensar con calma una decisión y anota su respuesta.",
)

# ============================================================ OA 01, clase 2
F = ("Ficha 2 (cuatro preguntas de ejemplo): (1) ¿A qué temperatura se derrite un trozo de hielo en una sala? (se puede medir). "
     "(2) ¿Qué significa que una decisión sea justa? (3) ¿Cuántos estudiantes del liceo llegan en bicicleta? (se puede contar). "
     "(4) ¿Es mejor una vida tranquila o una vida con desafíos?")
build(
    O1, 2, F,
    use="Aprenderé a definir pregunta empírica, conceptual y valorativa, y a decir qué tipos de preguntas trata la filosofía y cuáles dependen de otras disciplinas.",
    prior=["Sé qué son alcance, límite y fin.", "Sé distinguir hechos de valoraciones.", "Sé qué es un concepto."],
    explain=[
        "Una pregunta empírica se responde con observación, medición o recolección de datos: cuántos estudiantes llegan en bicicleta o a qué temperatura se derrite el hielo. Una pregunta conceptual se responde analizando qué significan las palabras y qué razones se dan: qué significa que una decisión sea justa. Una pregunta valorativa se pregunta qué es bueno, mejor o debido, y exige razones sobre lo que importa.",
        "Las ciencias se ocupan sobre todo de las preguntas empíricas. La filosofía trabaja con las conceptuales y las valorativas, y además examina los supuestos de las empíricas: qué quiere decir «medir» o cuándo un dato basta. No hay una frontera rígida: muchas preguntas mezclan las tres. Por ejemplo, para decidir si una norma escolar es justa se necesitan datos, el significado de «justa» y razones sobre lo que importa.",
        "Otras formas de saber, como el arte, la técnica o los saberes tradicionales de una comunidad, también aportan: el arte expresa experiencias, la técnica produce cosas y los saberes tradicionales transmiten conocimientos de la vida en común. No se jerarquizan por ser más o menos «serias»; cada una tiene sus fines y métodos. Cuando se tratan saberes de pueblos originarios, conviene que los explique quien los porta o un educador o educadora tradicional.",
    ],
    vocab=[("pregunta empírica", "la que se responde con observación, medición o datos"), ("pregunta conceptual", "la que se responde analizando el significado de los conceptos y las razones"), ("pregunta valorativa", "la que pregunta qué es bueno, mejor o debido y exige razones sobre lo que importa"), ("supuesto", "idea que se da por cierta sin haberla mostrado"), ("forma de saber", "manera de conocer y transmitir conocimientos, como la ciencia, el arte o la técnica")],
    worked=[
        ("Clasificar una pregunta", "Una amiga de ejemplo pregunta: «¿Qué entendemos por amistad verdadera?». ¿Qué tipo de pregunta es?", ["No se responde midiendo ni contando.", "Pide aclarar el significado de un concepto."], "Conceptual"),
        ("Separar partes de una pregunta mixta", "Pregunta de ejemplo: «¿Es justo cobrar más a quien tiene más ingresos?». ¿Qué partes tiene?", ["Hay datos sobre ingresos (empírico).", "Hay que definir «justo» (conceptual) y valorar qué importa (valorativo)."], "Mezcla las tres"),
    ],
    mistakes=[("Creer que si una pregunta no se puede medir, no tiene respuesta.", "Se confunde responder con medir.", "Hay respuestas razonadas para preguntas conceptuales y valorativas."),
              ("Creer que la filosofía reemplaza a las ciencias.", "Cada una responde preguntas distintas y se complementan.", "Reconoce qué parte de una pregunta es empírica y consulta la disciplina que corresponde.")],
    T=[
        ('abc', '{F} ¿Qué tipo de pregunta es la 1?', 'Empírica', 'Conceptual', 'Valorativa', 'Se responde midiendo la temperatura con un instrumento.'),
        ('abc', '{F} ¿Qué tipo de pregunta es la 2?', 'Conceptual', 'Empírica', 'Valorativa', 'Pide aclarar el significado del concepto «justa» y no se responde con una medida.'),
        ('abc', '{F} ¿Qué tipo de pregunta es la 3?', 'Empírica, porque se responde contando', 'Conceptual, porque se refiere a una palabra', 'Valorativa, porque afecta a los estudiantes', 'Cuántos llegan en bicicleta es un dato que se puede contar.'),
        ('abc', '{F} ¿Qué tipo de pregunta es la 4?', 'Valorativa, porque pregunta qué es mejor', 'Empírica, porque se puede medir cada vida', 'Conceptual, porque se refiere a una definición', 'Pregunta qué es mejor y requiere razones sobre lo que importa.'),
        ('abc', '¿Qué disciplinas se ocupan sobre todo de preguntas empíricas?', 'Las ciencias', 'Solo la filosofía', 'Solo las artes', 'Las ciencias observan, miden y recogen datos.'),
        ('abc', '¿Qué agrega la filosofía a una pregunta empírica?', 'Examina sus supuestos, por ejemplo qué significa «medir»', 'Reemplaza la medición por la opinión', 'Prohíbe usar datos', 'Revisa qué se supone y cuándo un dato basta, sin sustituir la medición.'),
        ('abc', '{F} Un compañero dice: «Como la pregunta 2 no se puede medir, no tiene respuesta». ¿Qué error comete?', 'Confunde responder con medir', 'Afirma que la pregunta es empírica', 'Mezcla valorativa con conceptual', 'Se puede responder analizando el concepto y dando razones, aunque no se mida.'),
        ('abc', 'Pregunta de ejemplo: «¿Es justo que se reparta el fondo del curso en partes iguales?». ¿Qué incluye?', 'Datos, el significado de «justo» y razones sobre lo que importa', 'Solo datos sobre el monto del fondo', 'Solo una definición de «partes iguales»', 'Mezcla las tres clases de pregunta.'),
        ('abc', '¿Cuál es una pregunta conceptual?', '¿Qué significa «libertad» en una decisión colectiva?', '¿Cuántas personas votaron en la elección del curso?', '¿Es mejor ayudar a un amigo o decir siempre la verdad?', 'Pide aclarar un concepto; las otras son empírica y valorativa.'),
        ('abc', '¿Por qué no se dice que el arte o la técnica son menos serias que la ciencia?', 'Porque cada una tiene sus propios fines y métodos', 'Porque todas las formas de saber son iguales en todo', 'Porque ninguna sirve para tomar decisiones', 'Tienen propósitos distintos y no se miden con el mismo criterio.'),
        ('abc', 'Si se quiere conocer saberes tradicionales de un pueblo originario, ¿qué corresponde?', 'Acudir a un educador o educadora tradicional o a quien los porta', 'Escribir una versión propia sin consultar', 'Deducirlos a partir de lo que dice una publicación en redes', 'Esos saberes los explica quien los porta, no se inventan ni se deducen.'),
        ('{F} Reformula la pregunta 4 como una pregunta conceptual.', '¿Qué entendemos por una vida buena?', 'Pide aclarar el concepto de «vida buena» antes de comparar.'),
        ('abc', '{F} ¿Cuál de las cuatro preguntas podría responderse con una encuesta o un conteo?', 'La 3', 'La 2', 'La 4', 'Solo la 3 pide un dato que se cuenta; la 2 y la 4 piden razones sobre conceptos o valores.'),
    ],
    ctx=('abc', 'Un grupo de ejemplo quiere decidir si conviene cambiar el horario de entrada del liceo. ¿Qué parte de la pregunta es empírica?', 'Cuántos estudiantes llegan tarde con el horario actual', 'Qué significa que un horario sea justo', 'Qué importa más, el sueño o la puntualidad', 'Contar cuántos llegan tarde es un dato; lo demás se discute con razones.'),
    sc=[
        ('En Filosofía: ¿qué es una pregunta conceptual?', 'La que se responde analizando el significado de los conceptos y las razones', 'No se mide; se analiza qué significan las palabras.'),
        ('abc', '¿Cuál es una pregunta valorativa?', '¿Qué es más importante: la libertad o la seguridad?', '¿Cuántos estudiantes hay en cada curso?', '¿Qué temperatura tiene el agua que hierve?', 'Pregunta qué importa más; las otras son empíricas.'),
        ('¿Qué parte de una pregunta mixta se responde con datos?', 'La empírica', 'Las otras partes se razonan; la empírica se mide o se cuenta.'),
    ],
    op=("Usa la {F} Para cada pregunta escribe su tipo y una frase que diga qué disciplina o forma de saber ayudaría más a responderla. Luego escribe una pregunta propia mixta y separa sus partes.",
        "1 empírica: ciencias. 2 conceptual: filosofía. 3 empírica: estadística o ciencias sociales. 4 valorativa: filosofía y reflexión personal. Pregunta mixta: «¿Es justo que todos estudien lo mismo?»: datos sobre el currículo, significado de justo y razones sobre lo que importa.",
        ["clasifica cada pregunta", "asigna una disciplina razonable", "separa partes de una pregunta mixta"], ["cuatro clasificaciones", "una pregunta propia"], ["decir que la filosofía reemplaza a las ciencias", "no separar partes"],
        "Pide que explique por qué su pregunta no se responde solo con datos."),
    reinforce="Escribe una pregunta empírica, una conceptual y una valorativa sobre tu liceo.",
    extend="Anota una decisión de tu vida diaria que mezcle datos, conceptos y valores.",
)

# ============================================================ OA 01, clase 3
F = ("Ficha 3 (tres perspectivas de ejemplo sobre cómo se relaciona la filosofía con otros saberes): "
     "Perspectiva 1: «Las ciencias entregan datos y la filosofía examina qué supuestos tienen y qué usos son justos; se complementan». "
     "Perspectiva 2: «El arte y los saberes tradicionales comunican experiencias y sentidos que no se reducen a un argumento; la filosofía puede dialogar con ellos, pero no sustituirlos». "
     "Perspectiva 3: «Solo la ciencia da conocimiento firme; lo demás son opiniones».")
build(
    O1, 3, F,
    use="Aprenderé a reconstruir perspectivas sobre cómo se relaciona la filosofía con la ciencia, el arte y otras formas de saber, y a señalar sus límites sin tomar partido por una de ellas.",
    prior=["Sé distinguir preguntas empíricas, conceptuales y valorativas.", "Sé reconstruir una perspectiva con tesis, razones y límite.", "Sé qué es un supuesto."],
    explain=[
        "Reconstruir una perspectiva es exponer su tesis, sus razones y su límite con fidelidad. La perspectiva 1 sostiene que ciencia y filosofía se complementan: las ciencias aportan datos y la filosofía examina supuestos y usos. La perspectiva 2 sostiene que el arte y los saberes tradicionales aportan experiencias y sentidos que un argumento no agota. La perspectiva 3 afirma que solo la ciencia entrega conocimiento firme.",
        "Cada una tiene un límite. A la perspectiva 1 se le puede preguntar si hay preguntas valorativas que ninguna disciplina resuelve del todo. A la 2, cómo se decide cuando dos saberes proponen cosas distintas. A la 3, que su propia tesis, «solo la ciencia da conocimiento firme», no es un resultado de ninguna medición: es una afirmación sobre el conocimiento y se discute con razones, es decir, con filosofía.",
        "Esto no significa que la filosofía «gane». Contrastar perspectivas muestra qué evidencia sostiene cada una y qué queda sin responder. Un punto de acuerdo posible es que ninguna forma de saber puede responder sola todas las preguntas de la vida común.",
    ],
    vocab=[("complementarse", "aportar cada una algo distinto, de modo que juntas completan la comprensión"), ("sustituir", "ocupar el lugar de otra cosa"), ("reducirse a", "poder explicarse por completo con otra cosa más simple"), ("conocimiento firme", "conocimiento muy bien respaldado por razones y evidencia"), ("sentido", "significado que algo tiene para quienes lo viven")],
    worked=[
        ("Reconstruir con fidelidad", "Una compañera de ejemplo resume la perspectiva 1 así: «Dice que la filosofía vale más que la ciencia». ¿Es fiel?", ["La perspectiva 1 dice que se complementan.", "No dice que una valga más que la otra."], "No es fiel"),
        ("Hallar el límite de la perspectiva 3", "La perspectiva 3 afirma: «Solo la ciencia da conocimiento firme». ¿Qué pregunta le plantea un límite?", ["Esa afirmación es sobre el conocimiento.", "No se prueba midiendo, sino con razones."], "¿Cómo se prueba esa afirmación con un método científico?"),
    ],
    mistakes=[("Elegir una perspectiva antes de reconstruir las otras.", "Se juzga sin haber entendido.", "Expón tesis, razones y límite de cada una primero."),
              ("Creer que contrastar significa que la filosofía gana siempre.", "Se parte con una conclusión en vez de evidencia.", "Anota qué aporta cada una y qué queda abierto.")],
    T=[
        ('abc', '{F} ¿Cuál es la tesis de la perspectiva 1?', 'Ciencia y filosofía se complementan', 'La filosofía reemplaza a la ciencia', 'La ciencia no necesita examinar sus supuestos', 'Se afirma que las ciencias dan datos y la filosofía examina supuestos y usos.'),
        ('abc', '{F} ¿Qué razón da la perspectiva 2?', 'Que hay experiencias y sentidos que un argumento no agota', 'Que el arte es más importante que cualquier ciencia', 'Que los saberes tradicionales no pueden dialogar con nadie', 'Se apoya en que las experiencias no se reducen a un argumento.'),
        ('abc', '{F} ¿Qué sostiene la perspectiva 3?', 'Que solo la ciencia da conocimiento firme', 'Que la ciencia y el arte son equivalentes', 'Que todo conocimiento es una opinión', 'Es una tesis sobre cuál forma de saber es válida.'),
        ('abc', '{F} ¿Qué límite se le puede plantear a la perspectiva 3?', 'Que su tesis no se puede probar con un método científico y requiere razones', 'Que la ciencia nunca se equivoca y por eso no debe discutirse', 'Que no usa ningún ejemplo concreto de ciencia', 'La tesis es una afirmación sobre el conocimiento: se discute con razones filosóficas.'),
        ('abc', '{F} ¿Qué límite se le puede plantear a la perspectiva 1?', 'Que quizá hay preguntas valorativas que ninguna disciplina resuelve sola', 'Que usa datos de las ciencias', 'Que reconoce un aporte de la filosofía', 'Plantea si la complementación alcanza para cerrar todas las preguntas.'),
        ('abc', '{F} Un compañero dice: «Según la perspectiva 2, la filosofía no sirve». ¿Es fiel?', 'No: dice que la filosofía puede dialogar con otros saberes, pero no sustituirlos', 'Sí: dice que la filosofía debe quedar fuera del diálogo', 'Sí: dice que el arte es mejor que la filosofía', 'No niega a la filosofía; dice que no debe ocupar el lugar de otros saberes.'),
        ('abc', '{F} ¿En qué podrían coincidir las perspectivas 1 y 2?', 'En que ninguna forma de saber responde sola todas las preguntas', 'En que la ciencia no aporta nada a la vida diaria', 'En que la filosofía debe quedar fuera de la discusión', 'Ambas reconocen aportes distintos y no excluyen a otras.'),
        ('abc', '{F} ¿Qué aporta la ciencia, según la perspectiva 1?', 'Datos', 'Supuestos sin examinar', 'Preguntas valorativas ya resueltas', 'La perspectiva 1 le asigna datos; examinar supuestos es lo que atribuye a la filosofía.'),
        ('abc', 'Si se discute qué saberes tradicionales tiene una comunidad, ¿qué conviene hacer?', 'Consultar a quien los porta o a un educador o educadora tradicional', 'Suponer qué dirían a partir de otros pueblos', 'Resumirlos con las propias palabras sin preguntar', 'Esos saberes los explica quien los porta; no se inventan ni se generalizan.'),
        ('abc', '¿Qué conviene hacer antes de criticar una perspectiva?', 'Reconstruirla con su tesis, razones y límite', 'Buscar su error más grande y quedarse con eso', 'Preguntar cuántas personas la comparten', 'Primero se la entiende con fidelidad; contar apoyos no la evalúa.'),
        ('{F} Escribe una pregunta que la perspectiva 2 podría hacer a la perspectiva 3.', '¿Cómo mide la ciencia el sentido que una experiencia tiene para quien la vive?', 'Señala algo que la ciencia por sí sola no recoge del mismo modo: el sentido que algo tiene para quien lo vive.'),
        ('abc', '{F} Si una comunidad, por su saber tradicional, propone cuidar un río, y una científica propone medir la contaminación, ¿qué es lo más razonable según la perspectiva 1 y 2 juntas?', 'Que ambos saberes dialoguen y se complementen', 'Que se elija solo uno y se descarte el otro', 'Que no se haga nada hasta que uno cambie de idea', 'Ambas perspectivas admiten el aporte de saberes distintos sin sustituirlos.'),
        ('abc', '{F} ¿Qué se pierde si se acepta la perspectiva 3 sin revisarla?', 'La posibilidad de preguntar qué razones sostienen la propia perspectiva 3', 'La posibilidad de usar datos de las ciencias', 'La posibilidad de dialogar con el arte', 'Aceptarla sin examen deja sin revisión su tesis, que es una afirmación sobre el conocimiento.'),
    ],
    ctx=('abc', 'En un taller de ejemplo, un estudiante dice: «El arte y la filosofía se complementan: el arte muestra una experiencia y la filosofía pregunta por su sentido». ¿Con cuál perspectiva se parece más?', 'Con la 1 o la 2, por reconocer aportes distintos que se complementan', 'Con la 3, porque separa lo firme de lo opinable', 'Con ninguna, porque no menciona a la ciencia', 'Reconoce que cada saber aporta algo distinto sin sustituirse.'),
    sc=[
        ('En Filosofía: ¿qué significa que dos saberes se complementen?', 'Que cada uno aporta algo distinto y juntos completan la comprensión', 'Aportan cosas distintas que se suman.'),
        ('abc', '¿Qué hay que hacer al reconstruir una perspectiva?', 'Exponer tesis, razones y límite con fidelidad', 'Resumirla de forma que sea fácil de refutar', 'Reemplazarla por otra que nos convenza más', 'Reconstruir es exponer con fidelidad, sin deformar lo que dice.'),
        ('¿Qué tipo de afirmación es «solo la ciencia da conocimiento firme»?', 'Una afirmación sobre el conocimiento', 'No es un dato medido: es una tesis sobre qué cuenta como conocimiento.'),
    ],
    op=("Usa la {F} Escribe una tabla con las tres perspectivas: tesis, una razón, un límite y una pregunta. Cierra con un punto de acuerdo posible entre dos de ellas, sin decir cuál es mejor.",
        "P1: tesis, se complementan; razón, datos más examen de supuestos; límite, preguntas valorativas abiertas; pregunta, ¿qué pasa si los datos no alcanzan? P2: tesis, el arte y los saberes aportan sentidos; razón, la experiencia no se agota en un argumento; límite, cómo decidir entre saberes. P3: tesis, solo la ciencia da conocimiento firme; límite, su tesis no es científica. Acuerdo: ninguna responde sola todas las preguntas.",
        ["reconstruye con fidelidad", "señala límites", "propone un acuerdo"], ["tabla de tres columnas", "una frase de acuerdo"], ["decidir que una gana", "deformar una postura"],
        "Pide que indique cuál límite le parece el más fuerte y por qué."),
    reinforce="Explica con tus palabras cómo se complementan la ciencia y la filosofía en un tema que elijas.",
    extend="Anota un saber de tu entorno, como una receta familiar o un oficio, y qué aporta que un argumento no agota.",
)

# ============================================================ OA 01, clase 4
F = ("Ficha 4 (argumento de ejemplo): «Premisa 1: las decisiones comunes de un grupo requieren acordar qué se considera justo. "
     "Premisa 2: acordar qué es justo exige examinar conceptos y razones. Premisa 3: la filosofía entrena en examinar conceptos y razones. "
     "Conclusión: la filosofía aporta a las decisiones comunes de un grupo». "
     "Objeción de ejemplo: «Otras disciplinas también entrenan en examinar razones; entonces la filosofía no es necesaria».")
build(
    O1, 4, F,
    use="Aprenderé a formular una tesis sobre el aporte de la filosofía al conocimiento y a la acción, a evaluar su argumento y a responder una objeción con precisión.",
    prior=["Sé reconstruir perspectivas sobre la relación entre la filosofía y otros saberes.", "Sé distinguir válido, sólido, relevante y suficiente.", "Sé qué es una objeción y una réplica."],
    explain=[
        "Un argumento sobre los aportes de la filosofía tiene una tesis (lo que se sostiene), premisas (razones) y una conclusión. Aportar al conocimiento es ayudar a entender mejor los conceptos, las razones y los supuestos. Aportar a la acción es ayudar a decidir y actuar con criterio. En la ficha, la conclusión dice que la filosofía aporta a las decisiones comunes: es una tesis de aporte, no de exclusividad.",
        "Es importante ajustar la conclusión a lo que las premisas permiten. Las premisas muestran que la filosofía entrena en examinar razones y que eso sirve para acordar qué es justo. No muestran que sea la única disciplina que lo hace ni que sea necesaria: decir «aporta» es distinto de decir «es la única» o «es indispensable». Una conclusión demasiado fuerte para sus razones es una exageración.",
        "La objeción de ejemplo dice que otras disciplinas también entrenan en examinar razones. Una buena respuesta la reconoce y precisa: puede ser cierto, pero la tesis es que la filosofía aporta, no que sea la única. Además puede agregar una razón: la filosofía trabaja de forma explícita sobre los conceptos, como «justo», que otras disciplinas suelen dar por supuestos.",
    ],
    vocab=[("aporte", "contribución que ayuda a lograr algo, sin ser la única"), ("exclusividad", "condición de ser la única que hace algo"), ("indispensable", "que no puede faltar para que algo ocurra"), ("exageración", "conclusión más fuerte de lo que sus razones permiten"), ("precisar", "ajustar una afirmación para que diga exactamente lo que se quiere sostener")],
    worked=[
        ("Ajustar la conclusión", "Argumento de ejemplo: «Los deportes enseñan a trabajar en equipo; por lo tanto, solo los deportes enseñan a trabajar en equipo». ¿Qué falla?", ["Las premisas muestran un aporte.", "La conclusión afirma exclusividad, que no se sigue."], "La conclusión es más fuerte que las razones"),
        ("Responder una objeción", "Objeción de ejemplo: «Otras materias también ayudan a argumentar». ¿Cuál es una respuesta precisa?", ["Reconoce lo cierto.", "Aclara que la tesis es de aporte y no de exclusividad."], "Es cierto, y la tesis es que aporta, no que sea la única"),
    ],
    mistakes=[("Defender una conclusión de exclusividad con razones de aporte.", "Se pasa de «aporta» a «es la única» sin base.", "Ajusta la conclusión a lo que las razones permiten."),
              ("Responder una objeción negando algo que sí es cierto.", "Se pierde credibilidad y no se avanza.", "Reconoce lo cierto y precisa tu tesis.")],
    T=[
        ('abc', '{F} ¿Cuál es la tesis del argumento?', 'La filosofía aporta a las decisiones comunes de un grupo', 'La filosofía es la única disciplina que examina razones', 'Todas las decisiones comunes dependen de la filosofía', 'La conclusión afirma un aporte, no una exclusividad ni una dependencia total.'),
        ('abc', '{F} ¿Qué dice la premisa 2?', 'Que acordar qué es justo exige examinar conceptos y razones', 'Que la filosofía es la única que examina razones', 'Que las decisiones comunes son siempre justas', 'La premisa 2 une «acordar qué es justo» con «examinar conceptos y razones».'),
        ('abc', '{F} ¿Qué objeción plantea el ejemplo?', 'Que otras disciplinas también entrenan en examinar razones', 'Que la filosofía nunca examina razones', 'Que las decisiones comunes no necesitan razones', 'Cuestiona que la filosofía sea necesaria, porque otros también pueden hacerlo.'),
        ('abc', '{F} ¿Qué respuesta a la objeción es más precisa?', 'Es cierto; pero la tesis es que la filosofía aporta, no que sea la única', 'Es falso: ninguna otra disciplina examina razones', 'La objeción no importa: la filosofía es superior a las demás', 'Reconoce lo cierto y ajusta el alcance de la tesis.'),
        ('abc', '{F} ¿Cuál es una exageración de la conclusión?', 'La filosofía es indispensable para cualquier decisión de un grupo', 'La filosofía aporta a decisiones de un grupo', 'La filosofía puede ayudar a examinar qué es justo', 'Indispensable dice más de lo que las premisas muestran.'),
        ('abc', '¿Qué diferencia hay entre «aporta» y «es la única que aporta»?', 'La segunda afirma una exclusividad que la primera no afirma', 'No hay diferencia: ambas dicen lo mismo con otras palabras', 'La primera es falsa y la segunda es verdadera', 'Aportar admite que otros también aporten; ser única lo excluye.'),
        ('abc', '{F} Si se quiere fortalecer la premisa 3, ¿qué dato ayudaría más?', 'Un ejemplo de una discusión de curso en que se aclaró qué significa «justo»', 'La cantidad de estudiantes que dicen que les gusta la filosofía', 'La opinión de una persona famosa a favor de la filosofía', 'Un ejemplo muestra cómo se entrena en examinar conceptos; popularidad y fama no.'),
        ('abc', '{F} ¿Qué razón puede agregarse para responder la objeción?', 'Que la filosofía examina de forma explícita conceptos como «justo», que otros suelen dar por supuestos', 'Que las otras disciplinas no tienen conceptos', 'Que la filosofía siempre llega a respuestas finales', 'Es una razón que aclara qué aporta de particular, sin negar a las demás.'),
        ('abc', 'Alguien concluye: «La filosofía ayudó a aclarar un concepto en un debate; por lo tanto, la filosofía resuelve todos los conflictos». ¿Qué falla?', 'La conclusión es mucho más fuerte que el caso en que se apoya', 'El caso es falso y no ocurrió', 'La conclusión es válida pero no es sólida', 'Un caso muestra un aporte, no una solución universal.'),
        ('abc', '¿Qué es un aporte al conocimiento?', 'Ayudar a entender mejor conceptos, razones y supuestos', 'Entregar la respuesta final a todas las preguntas de un debate', 'Reemplazar los datos por opiniones', 'Aportar es ayudar a comprender, no cerrar toda discusión.'),
        ('{F} Reescribe la conclusión para que diga solo lo que las premisas permiten.', 'La filosofía ayuda a las decisiones comunes porque entrena en examinar conceptos y razones.', 'Mantiene «ayuda» o «aporta» y la razón, sin afirmar exclusividad ni necesidad.'),
        ('abc', '{F} Si alguien muestra que un grupo logró acordar qué es justo sin entrenamiento filosófico, ¿qué demuestra?', 'Que la filosofía no es indispensable, pero no que no aporte', 'Que la filosofía no aporta nada a las decisiones de un grupo', 'Que las premisas del argumento son verdaderas', 'Un contraejemplo a «indispensable» no refuta un aporte.'),
        ('abc', '¿Qué hace más honesta una posición sobre el valor de la filosofía?', 'Decir qué sostengo, qué razones tengo, qué límite reconozco y qué me haría cambiar', 'Decir que quien piense distinto no entiende la filosofía', 'No decir nada para no equivocarse', 'Una posición revisable reconoce límites y abre la posibilidad de cambiar.'),
    ],
    ctx=('abc', 'Un estudiante de ejemplo escribe: «Mi tesis es que la filosofía aporta a la acción porque entrena a pedir razones antes de actuar». Un compañero objeta: «A veces hay que actuar sin tiempo para pedir razones». ¿Cuál es una respuesta precisa?', 'Es cierto en urgencias; la tesis es que entrena un hábito útil en otras situaciones', 'Eso nunca ocurre, así que la objeción no vale', 'Tienes razón: la filosofía no sirve cuando hay que actuar rápido', 'Reconoce la parte cierta y precisa el alcance de la tesis.'),
    sc=[
        ('En Filosofía: ¿qué significa precisar una tesis?', 'Ajustarla para que diga exactamente lo que se quiere sostener', 'Es acotar su alcance a lo que las razones permiten.'),
        ('abc', '¿Qué es una exageración en un argumento?', 'Una conclusión más fuerte de lo que sus razones permiten', 'Una premisa con muchos detalles', 'Una objeción sin respuesta que obliga a abandonar la tesis', 'La exageración es pasar más allá de lo que las razones muestran.'),
        ('¿Qué conviene hacer ante una objeción cierta?', 'Reconocerla y precisar o ajustar la tesis', 'Se acepta lo cierto y se aclara hasta dónde llega lo que se sostiene.'),
    ],
    op=("Usa la {F} Escribe cinco líneas: la tesis; una premisa que te parezca más débil y por qué; una conclusión exagerada posible; la respuesta a la objeción de ejemplo; y qué dato te haría cambiar de posición.",
        "Tesis: la filosofía aporta a las decisiones comunes. Premisa débil: la 3, falta un ejemplo concreto. Exageración: «es indispensable». Respuesta: otras disciplinas también lo hacen, pero la tesis es de aporte; además la filosofía trabaja el concepto de justo. Dato: un grupo que decide mejor sin examinar conceptos de ninguna forma.",
        ["tesis ajustada", "evalúa una premisa", "responde la objeción con precisión"], ["cinco líneas"], ["afirmar exclusividad", "ignorar la objeción"],
        "Pregunta qué otra disciplina podría reclamar el mismo aporte y qué respondería."),
    reinforce="Escribe una tesis sobre un aporte de la filosofía y una razón que la apoye.",
    extend="Piensa en una discusión reciente en tu entorno y anota qué concepto convenía aclarar antes de decidir.",
)
