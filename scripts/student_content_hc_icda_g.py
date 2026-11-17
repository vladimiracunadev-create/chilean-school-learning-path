"""Interpretación y creación en danza 3.º y 4.º medio HC: OAC-07 (evaluar críticamente procesos y resultados de obras de danza, propios y de pares), clases 1 a 5. Casos y datos inventados; sin video ni obras reales."""
from __future__ import annotations

from hc_icda_common import build

O7 = "AR-ICDA-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (caso de ejemplo «Lazo», inventado). Grupo de 4 estudiantes con el propósito «unirse sin tocarse». "
     "Bitácora del proceso. Sesión 1: lluvia de ideas, 3 propuestas escritas (A: canon, B: unísono con pausas, C: contraste). Sesión 2: se elige B y se escribe la partitura de conteos. "
     "Sesión 3: se prueban dos versiones de la entrada; se elige la segunda porque la primera tapaba a una persona (queda registrada la razón). Sesión 4: ensayo general; se acorta una pausa de 6 a 4 tiempos. "
     "Resultado: muestra de 4 minutos en el patio ante 20 personas; el público contesta una encuesta breve. "
     "Evidencias de proceso: bitácora, partitura de conteos, mapa de piso y las razones de cada decisión. "
     "Evidencias de resultado: la muestra, la encuesta y el registro de lo que se vio. "
     "Evaluar procesos y resultados: mirar el camino (decisiones, pruebas, ajustes) y el producto (lo que logró la obra).")
build(
    O7, 1, F,
    use="Aprenderé a evaluar críticamente tanto el proceso como el resultado de una obra de danza, distinguiendo evidencias de cada uno y reconociendo que un buen resultado no siempre implica un buen proceso, ni al revés.",
    prior=["Sé analizar una obra con criterios.", "Sé llevar una bitácora de ensayos.", "Sé argumentar juicios con evidencia."],
    explain=[
        "Evaluar críticamente es juzgar con criterios y evidencias, no por impresión. En una obra de danza se evalúan dos cosas distintas. El proceso es el camino de creación: las ideas, las pruebas, las decisiones, los ajustes y las razones de cada cambio. El resultado es el producto que se muestra: la obra y sus efectos en quien la ve. Una obra puede tener un resultado logrado con un proceso poco pensado, o un proceso muy cuidadoso con un resultado que aún no logra su propósito. Por eso se evalúan por separado y luego se relacionan.",
        "Cada uno se evalúa con evidencias distintas. Para el proceso: la bitácora, los borradores, la partitura de conteos, el mapa de piso y las razones escritas de las decisiones. Para el resultado: la muestra, el registro de lo que se vio y las respuestas del público. Un buen proceso deja huellas: se sabe qué se probó, qué se descartó y por qué. Un resultado se evalúa respecto del propósito: ¿logró lo que quería comunicar?",
        "La evaluación crítica es respetuosa. Se evalúan decisiones, evidencias y resultados, no cuerpos ni personas; se habla con hechos («la primera entrada tapaba a una persona») y no con etiquetas («fulano trabaja mal»). Cuando se evalúa a un par se hace con su consentimiento y con cuidado, y nadie está obligado a mostrar su trabajo. Ante cualquier incomodidad o tensión en el grupo, se avisa a una persona adulta.",
    ],
    vocab=[("proceso", "camino de creación: ideas, pruebas, decisiones y ajustes"), ("resultado", "producto que se muestra y sus efectos"), ("evidencia de proceso", "huella que muestra cómo se creó, como la bitácora"), ("evidencia de resultado", "dato que muestra lo que logró la obra"), ("propósito", "idea que se quiere comunicar"), ("evaluación crítica", "juicio con criterios y evidencias, hecho con respeto")],
    worked=[
        ("Distinguir evidencias", "«La partitura de conteos con las 4 entradas». ¿Es evidencia de proceso o de resultado?", ["La partitura se escribe antes de la muestra, mientras se compone.", "Muestra el camino de creación."], "De proceso"),
        ("Evaluar proceso y resultado por separado", "Un grupo tuvo una muestra muy aplaudida, pero no registró ninguna prueba ni ajuste. ¿Cómo se evalúa?", ["El resultado parece logrado, pero hay evidencia limitada.", "El proceso queda sin registro: se evalúa como débil en evidencias."], "Resultado logrado; proceso con poca evidencia"),
    ],
    mistakes=[("Evaluar solo el resultado y pasar por alto el camino.", "El proceso explica por qué la obra funciona o no y permite mejorar.", "Revisa también las decisiones, pruebas y ajustes."),
              ("Decir «trabajó bien» o «trabajó mal» sobre una persona.", "Es una etiqueta que no dice qué decisión o evidencia respalda el juicio.", "Describe el hecho y su efecto: «la entrada tapaba a alguien y se corrigió».")],
    T=[
        ('abc', 'En creación en danza, ¿qué es el proceso de una obra?', 'El camino de creación: ideas, pruebas, decisiones y ajustes', 'La función final que se muestra al público en el patio', 'La lista de personas que participan en la obra', 'El proceso es el camino; el resultado es lo que se muestra.'),
        ('abc', '{F} ¿Cuál es el propósito del grupo?', 'Unirse sin tocarse', 'Mostrar técnica avanzada', 'Competir con otro grupo', 'La ficha dice que el propósito es «unirse sin tocarse».'),
        ('abc', '{F} ¿Cuál es una evidencia de proceso de la ficha?', 'La bitácora con las razones de cada decisión', 'La encuesta que responde el público', 'El aplauso al final de la muestra', 'La bitácora registra el camino; la encuesta y el aplauso son del resultado.'),
        ('abc', '{F} ¿Cuál es una evidencia de resultado de la ficha?', 'La encuesta breve del público', 'La partitura de conteos', 'El mapa de piso de los ensayos', 'La encuesta muestra lo que logró la obra.'),
        ('=', '{F} ¿Cuántos tiempos se ahorraron al acortar la pausa en el ensayo general?', '6-4', 'La pausa pasó de 6 a 4 tiempos.', ' tiempos'),
        ('abc', '{F} ¿Por qué se descartó la primera versión de la entrada?', 'Porque tapaba a una persona', 'Porque era muy larga', 'Porque no tenía música', 'La razón está registrada en la bitácora de la sesión 3.'),
        ('abc', '{F} Esa decisión de la sesión 3 es un ejemplo de buena práctica porque', 'registra la razón y una prueba comparativa', 'cambia la obra completa sin avisar a nadie', 'se hizo en un ensayo sin registro', 'Hay prueba de dos versiones y razón escrita.'),
        ('abc', '{F} Una persona dice: «el grupo trabajó mal porque no hizo la propuesta C». ¿Qué corresponde responder?', 'Que descartar C es una decisión que habría que justificar', 'Que tiene razón, porque debieron probar todas las propuestas antes de elegir una', 'Que es mejor no evaluar el proceso, porque solo importa el resultado final', 'Evaluar el proceso es revisar las razones, no exigir probar todo.'),
        ('=', '{F} La muestra dura 4 minutos y 20 personas contestan la encuesta. Si 15 responden que se entendió el propósito, ¿qué porcentaje es?', '15/20*100', 'Se divide 15 por 20 y se multiplica por 100.', ' %'),
        ('abc', '{F} Un grupo tiene un resultado muy aplaudido pero ninguna evidencia de proceso. ¿Qué juicio es más justo?', 'Resultado con aplausos y proceso con poca evidencia', 'Todo es excelente, porque hubo aplausos al terminar la muestra', 'Todo es deficiente, porque falta la bitácora y no se puede saber nada más', 'Se evalúan por separado: el aplauso muestra resultado y la falta de registro limita la evaluación del proceso.'),
        ('abc', 'Dos estudiantes discuten: una dice que si el resultado es bueno el proceso no importa; el otro dice que el proceso permite entender y mejorar el resultado. ¿Quién argumenta mejor?', 'El otro, porque el proceso explica por qué funciona la obra', 'La primera, porque el público solo ve el resultado final de la obra', 'Ninguno, porque el proceso no deja ninguna evidencia que se pueda evaluar', 'El proceso aporta información para explicar y mejorar el resultado.'),
        ('abc', '{F} Una integrante pide no ser nombrada en el informe de evaluación del grupo. ¿Qué corresponde?', 'Respetarlo y describir las decisiones sin identificarla', 'Nombrarla igual para que se sepa quién trabajó y quién no', 'Pedirle que explique frente al grupo por qué no quiere ser nombrada', 'Se respeta su decisión; la evaluación se centra en decisiones, no en personas.'),
        ('abc', 'Antes de la muestra, una estudiante siente mucha ansiedad y no quiere presentar. ¿Qué corresponde?', 'Ofrecerle otro rol y avisar a una persona adulta', 'Obligarla a presentar delante de todos para que se acostumbre', 'Quitarla del grupo sin avisarle para no perder más tiempo', 'Nadie está obligado a exponerse; se ofrecen alternativas y se avisa a una persona adulta.'),
    ],
    ctx=('abc', 'Un curso entrega esta evaluación de «Lazo»: «Proceso: decisiones registradas con razones y pruebas comparativas. Resultado: 15 de 20 personas entendieron el propósito». ¿Qué le falta para ser una evaluación crítica completa?', 'Una relación entre ambos: cómo las decisiones explican el resultado', 'Más opiniones sobre las personas que bailaron y su estilo', 'Una comparación con el trabajo de otro grupo del curso', 'Falta relacionar proceso y resultado: cuáles decisiones explican la comprensión del propósito.'),
    sc=[
        ("En creación en danza: ¿qué diferencia hay entre evidencia de proceso y de resultado?", "La de proceso muestra cómo se creó; la de resultado, lo que logró la obra", "Se evalúan por separado y luego se relacionan."),
        ("¿Por qué se registran las razones de cada decisión?", "Para poder revisar y justificar el proceso", "Sin razones, el proceso queda sin evidencia."),
        ("¿Se evalúa a las personas o a las decisiones?", "A las decisiones y al resultado", "Los cuerpos y las personas no se evalúan."),
    ],
    op=("Imagina que debes evaluar el proceso y el resultado de una obra inventada de tu elección (la de la ficha o una propia). Escribe: (1) tres evidencias de proceso y tres de resultado; (2) una fortaleza y una debilidad del proceso; (3) una fortaleza y una debilidad del resultado; (4) una frase que relacione ambos. No hables de los cuerpos ni nombres a personas reales.",
        "Obra «Lazo». Evidencias de proceso: bitácora, partitura de conteos, mapa de piso. De resultado: la muestra de 4 minutos, la encuesta y el registro de lo visto. Fortaleza del proceso: se probaron dos versiones de la entrada con una razón registrada. Debilidad: faltó registro del tiempo de cada ensayo. Fortaleza del resultado: 15 de 20 personas entendieron el propósito. Debilidad: la pausa final de 4 tiempos se sintió larga. Relación: el registro de pruebas explica la claridad de la entrada.",
        ["distingue evidencias de proceso y de resultado", "justifica fortalezas y debilidades con hechos", "relaciona proceso y resultado sin evaluar personas"],
        ["hoja con evidencias, fortalezas, debilidades y relación"],
        ["evaluar solo el resultado", "evaluar a las personas", "no justificar con hechos"],
        "Pregunta: «¿qué evidencia muestra esa fortaleza?». Si responde con una opinión, pídele un dato o un registro."),
    reinforce="Escribe una bitácora breve de tres sesiones para una obra inventada, con una decisión y su razón en cada sesión.",
    extend="Explica por qué un resultado aplaudido no es suficiente para evaluar una obra de danza y qué más revisarías.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (matriz de trazabilidad de ejemplo, inventada, para la obra «Lazo»). Propósito: «unirse sin tocarse». "
     "Fila 1: decisión, unísono con pausas; efecto observado, el grupo se ve como una unidad; evaluación, coherente con el propósito. "
     "Fila 2: decisión, una entrada que tapaba a una persona; efecto observado, el público no veía a una integrante; evaluación, contradice el propósito (se corrigió). "
     "Fila 3: decisión, mirada hacia el grupo en cada pausa; efecto observado, se percibe atención mutua; evaluación, coherente con el propósito. "
     "Fila 4: decisión, vestuario de colores muy distintos; efecto observado, se ve a cada persona por separado; evaluación, debilita el propósito. "
     "Filas coherentes: las que apoyan el propósito. Regla de la matriz: toda evaluación debe citar la decisión, el efecto observado y el propósito.")
build(
    O7, 2, F,
    use="Aprenderé a relacionar el propósito expresivo, los aspectos estéticos y las decisiones de una obra con los efectos observados, usando una matriz de trazabilidad para evaluar si cada decisión apoya o debilita el propósito.",
    prior=["Sé distinguir proceso y resultado.", "Sé argumentar con criterio y evidencia.", "Sé describir efectos de decisiones de composición."],
    explain=[
        "Evaluar una obra críticamente exige seguir el hilo entre el propósito (lo que se quiere comunicar), las decisiones (lo que se eligió hacer) y los efectos (lo que realmente se observa). A ese recorrido se le llama trazabilidad. Una matriz de trazabilidad es una tabla con una fila por decisión: qué se decidió, qué efecto produjo y si apoya o debilita el propósito. Así se evita juzgar por impresión y se ve qué decisiones sostienen la idea y cuáles la contradicen.",
        "Cada fila se evalúa con una regla simple: una decisión es coherente cuando su efecto observado apoya el propósito, y es incoherente cuando lo contradice o lo debilita. En «Lazo», el propósito es «unirse sin tocarse»: el unísono con pausas y la mirada al grupo apoyan el propósito, mientras que un vestuario de colores muy distintos separa visualmente a las personas y lo debilita. Un efecto puede ser positivo o negativo, intencional o no.",
        "La matriz también ayuda a decidir qué cambiar: se mantienen las decisiones coherentes y se revisan las otras. Se evalúan las decisiones, no a quienes las tomaron, y se cuida el lenguaje: «la entrada tapaba a una integrante» es un hecho; «lo hicieron mal» es una etiqueta. Si una corrección exige algo que duele o incomoda, se busca otra solución y se avisa a una persona adulta.",
    ],
    vocab=[("trazabilidad", "relación seguida entre propósito, decisión y efecto"), ("matriz de trazabilidad", "tabla de decisiones, efectos y evaluación"), ("efecto observado", "lo que realmente se ve o se oye de una decisión"), ("coherente", "que apoya el propósito"), ("debilitar", "restar fuerza al propósito"), ("decisión", "elección de composición o puesta en escena")],
    worked=[
        ("Evaluar una fila", "Decisión: iluminar a una sola persona. Efecto: el público se fija en ella. Propósito: «destacar al grupo». ¿Es coherente?", ["El efecto separa a una persona del grupo.", "Eso contradice el propósito de destacar al grupo."], "No es coherente"),
        ("Contar filas coherentes", "En una matriz hay 5 filas: 3 apoyan el propósito y 2 lo debilitan. ¿Qué parte de las filas es coherente?", ["Cuenta las filas que apoyan: 3.", "3 de 5 filas son coherentes."], "3 de 5"),
    ],
    mistakes=[("Evaluar una decisión por si es difícil o llamativa y no por su efecto.", "Una decisión se evalúa por lo que produce respecto del propósito.", "Describe el efecto observado y compáralo con el propósito."),
              ("Mirar solo si el efecto gusta, sin relacionarlo con el propósito.", "Un efecto agradable puede contradecir lo que se quería comunicar.", "Pregunta si el efecto apoya el propósito.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es la trazabilidad en una evaluación?', 'La relación seguida entre propósito, decisiones y efectos', 'La cantidad de ensayos que se hicieron antes de mostrar', 'La lista de materiales usados en la puesta en escena', 'La trazabilidad sigue el hilo propósito, decisión y efecto.'),
        ('abc', '{F} ¿Cuál es el propósito de «Lazo»?', 'Unirse sin tocarse', 'Mostrar técnica avanzada', 'Competir por ocupar el centro', 'La ficha dice que el propósito es unirse sin tocarse.'),
        ('abc', '{F} ¿Qué decisión de la ficha debilita el propósito?', 'El vestuario de colores muy distintos', 'La mirada hacia el grupo en cada pausa', 'El unísono con pausas', 'El vestuario separa visualmente a las personas.'),
        ('=', '{F} La matriz tiene 4 filas y 2 de ellas debilitan el propósito. ¿Cuántas filas son coherentes?', '4-2', 'Se restan de las 4 filas las que debilitan el propósito.', ' filas'),
        ('abc', '{F} ¿Qué efecto observado produjo la entrada que tapaba a una persona?', 'El público no veía a una integrante', 'El grupo se vio más unido', 'Se percibió atención mutua', 'La fila 2 dice que no se veía a una integrante.'),
        ('abc', '{F} ¿Por qué la mirada hacia el grupo en cada pausa es coherente?', 'Porque produce atención mutua y apoya el propósito', 'Porque es difícil de ejecutar y exige mucha práctica', 'Porque hace que el público aplauda más al terminar', 'Se evalúa por su efecto sobre el propósito, no por dificultad ni aplausos.'),
        ('=', 'Una obra tiene 12 decisiones registradas en su matriz y 9 son coherentes con el propósito. ¿Cuántas decisiones debilitan el propósito?', '12-9', 'Se restan de las 12 decisiones las 9 coherentes.', ' decisiones'),
        ('abc', '{F} Para corregir la fila 4, ¿qué decisión conserva el propósito?', 'Usar vestuario de un mismo color o tono', 'Quitar la mirada hacia el grupo', 'Cambiar el propósito por otro', 'Un vestuario unificado refuerza la idea de unirse.'),
        ('abc', '{F} Un integrante dice que la fila 4 está bien porque «los colores se ven lindos». ¿Qué corresponde responder?', 'Que se evalúa si apoya el propósito, y los colores separan', 'Que tiene razón, porque lo lindo siempre es coherente', 'Que debe mantenerlo y cambiar el propósito de la obra', 'La belleza no equivale a coherencia con el propósito.'),
        ('abc', 'Dos estudiantes discuten: uno dice que una decisión «arriesgada» es buena aunque debilite el propósito; la otra dice que se evalúa por su efecto sobre el propósito. ¿Quién argumenta mejor?', 'La otra, porque lo que cuenta es el efecto sobre el propósito', 'El primero, porque lo arriesgado demuestra creatividad y valentía', 'Ninguno, porque las decisiones de una obra no se pueden evaluar con hechos', 'Una decisión se evalúa por su efecto sobre el propósito, no por su riesgo.'),
        ('abc', '{F} Una nueva decisión: poner una pausa larga en que todas miran hacia afuera del grupo. ¿Cómo se evalúa respecto del propósito?', 'Probablemente lo debilita, porque desvía la atención del grupo', 'Apoya el propósito, porque es una decisión diferente de las demás', 'No se puede evaluar sin conocer personalmente a las personas', 'Mirar hacia afuera debilita la atención mutua.'),
        ('abc', '{F} Para evaluar una decisión que exige un giro rápido, una integrante dice que le produce mareo. ¿Qué corresponde?', 'Cambiarla por una más segura y avisar a una persona adulta', 'Mantenerla porque produce un efecto fuerte en el público', 'Pedirle que se acostumbre al mareo con más ensayos seguidos', 'El mareo manda detenerse y avisar; la decisión se reemplaza por otra segura.'),
        ('abc', 'Al armar la matriz, una persona propone escribir en la columna de evaluación «fulana lo hizo mal». ¿Qué corresponde?', 'Reescribir citando la decisión, el efecto y el propósito', 'Mantener la frase tal cual, para ser claro con el grupo', 'Dejarla si el grupo entero está de acuerdo con ella', 'La matriz evalúa decisiones con hechos, no personas.'),
    ],
    ctx=('abc', 'Un curso escribe una fila de matriz sobre una obra con propósito «una ciudad que despierta»: decisión, «luz cálida que crece de a poco»; efecto observado, «se percibe amanecer». ¿Qué evaluación es la más completa?', 'Coherente, porque la luz que crece de a poco evoca el despertar', 'Buena, porque a todas las personas les gustó mucho la luz', 'Mala, porque la luz no se mueve por el escenario', 'La evaluación cita decisión, efecto y propósito.'),
    sc=[
        ("En creación en danza: ¿qué columnas tiene una matriz de trazabilidad?", "Decisión, efecto observado y evaluación respecto del propósito", "Así se sigue la relación entre decisión y efecto."),
        ("¿Cuándo una decisión es coherente?", "Cuando su efecto apoya el propósito", "La coherencia se mide por el efecto sobre el propósito."),
        ("¿Se evalúa a quien tomó la decisión?", "No: se evalúa la decisión", "Las personas y los cuerpos no se evalúan."),
    ],
    op=("Elige una obra inventada con un propósito claro (puede ser «Lazo»). Construye una matriz de trazabilidad con cuatro filas: decisión, efecto observado y evaluación (coherente o debilita), citando el propósito. Luego escribe una corrección para cada fila que debilita el propósito, con un solo cambio por fila. Calcula qué parte de las filas es coherente antes y después de la corrección.",
        "Propósito: «unirse sin tocarse». Fila 1: unísono con pausas; el grupo se ve como una unidad; coherente. Fila 2: mirada hacia el grupo; atención mutua; coherente. Fila 3: vestuario de colores distintos; se ve a cada persona por separado; debilita. Fila 4: una entrada que tapa a alguien; no se ve a una integrante; debilita. Corrección: vestuario de un solo tono; entrada desde otro lado. Antes: 2 de 4; después: 4 de 4.",
        ["cada fila relaciona decisión, efecto y propósito", "las correcciones cambian una sola cosa por fila", "el cálculo de filas coherentes es correcto"],
        ["matriz de cuatro filas, correcciones y cálculo"],
        ["evaluar por gusto y no por efecto", "evaluar personas", "cambiar varias cosas por fila"],
        "Pregunta: «¿cómo apoya o debilita el propósito?». Si responde «me gustó», pídele que describa el efecto observado."),
    reinforce="Escribe tres decisiones de una obra inventada y para cada una su efecto probable y si apoya o debilita un propósito que elijas.",
    extend="Explica por qué una decisión muy llamativa puede debilitar el propósito de una obra y cómo lo mostrarías en una matriz.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (comentarios de ejemplo, inventados, sobre una frase de un grupo de pares: 4 intérpretes, propósito «esperar juntos», 3 minutos). "
     "Comentario C1: «Observo que las 4 personas se detienen a la vez en el segundo 90; esto produce sensación de espera compartida; me pregunto si un cambio de nivel en la pausa la haría más clara.» "
     "Comentario C2: «Fue lo peor que vi.» "
     "Comentario C3: «Fulano se mueve raro, no sirve para esto.» "
     "Comentario C4: «Me gustó mucho, quedó perfecto.» "
     "Comentario C5: «Observo que la tercera persona entra 2 tiempos tarde; esto produce que el canon se vea desordenado; me pregunto si una señal con la mirada ayudaría.» "
     "Formato de retroalimentación descriptiva: observo (un hecho observable), esto produce (un efecto) y me pregunto si (una sugerencia en forma de pregunta). "
     "Normas: hablar de la obra y las decisiones, no de las personas ni de sus cuerpos; pedir consentimiento antes de comentar; recibir sin defenderse y luego decidir qué hacer.")
build(
    O7, 3, F,
    use="Aprenderé a dar y recibir retroalimentación crítica y respetuosa sobre el trabajo de pares, con hechos, efectos y preguntas, y a decidir con criterio qué sugerencias incorporar.",
    prior=["Sé evaluar con matrices de trazabilidad.", "Sé argumentar con evidencia.", "Sé que no se evalúan los cuerpos."],
    explain=[
        "La retroalimentación entre pares es información que se da y se recibe para mejorar un trabajo. Para que sea útil y respetuosa, se usa un formato descriptivo con tres partes: observo (un hecho observable), esto produce (el efecto de ese hecho) y me pregunto si (una sugerencia en forma de pregunta). Por ejemplo: «observo que la tercera persona entra 2 tiempos tarde; esto produce que el canon se vea desordenado; me pregunto si una señal con la mirada ayudaría». La pregunta final deja la decisión en manos de quien creó el trabajo.",
        "Un comentario crítico no es un insulto ni un elogio vacío. «Fue lo peor que vi» y «quedó perfecto» no dicen qué mejorar ni qué conservar. «Fulano se mueve raro» ataca a una persona y su cuerpo. Una crítica útil habla de decisiones y efectos, es específica y puede comprobarse. También es útil señalar lo que funciona (qué conservar), porque no todo comentario es una corrección.",
        "Recibir retroalimentación es una habilidad: se escucha sin defenderse, se pregunta para entender, se agradece y después se decide qué incorporar y qué no, con una razón. Antes de comentar el trabajo de otra persona, se pide su consentimiento; si alguien prefiere no ser comentado en voz alta, se ofrece hacerlo por escrito. Si un comentario hiere o se vuelve burla, se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("retroalimentación", "información para mejorar un trabajo"), ("observo", "hecho observable, sin opinión"), ("esto produce", "efecto del hecho observado"), ("me pregunto si", "sugerencia en forma de pregunta"), ("crítica constructiva", "crítica específica que ayuda a mejorar"), ("consentimiento", "autorización para ser comentado")],
    worked=[
        ("Reescribir un comentario", "«Tu final es lento y aburrido». Reescríbelo con el formato.", ["Busca el hecho: el final dura 40 segundos sin cambios.", "Escribe: observo que el final dura 40 segundos sin cambios; esto produce sensación de espera; me pregunto si un cambio de dirección lo aclararía."], "Observo que el final dura 40 segundos sin cambios; esto produce espera; me pregunto si un cambio de dirección lo aclararía"),
        ("Decidir qué incorporar", "Recibes dos sugerencias: acortar una pausa de 4 a 2 tiempos, y cambiar el propósito. Tu propósito es claro para ti. ¿Cómo decides?", ["La primera mejora una decisión sin cambiar el propósito.", "La segunda cambia el propósito: se agradece y se decide si hay razones para hacerlo."], "Incorporar la primera y revisar la segunda con razones"),
    ],
    mistakes=[("Decir «me gustó mucho» o «no me gustó» como retroalimentación.", "No dice qué decisión funciona ni qué mejorar.", "Usa observo, esto produce y me pregunto si."),
              ("Comentar el cuerpo o la manera de ser de alguien.", "La retroalimentación es sobre decisiones y efectos, no sobre personas.", "Habla del movimiento, el tiempo, el espacio o la puesta en escena.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es la retroalimentación descriptiva?', 'Información con hecho, efecto y sugerencia como pregunta', 'Una opinión sobre si el trabajo gustó o no gustó', 'Una calificación numérica del rendimiento de cada persona', 'La retroalimentación descriptiva usa hecho, efecto y pregunta.'),
        ('abc', '{F} ¿Cuál comentario sigue el formato observo, esto produce, me pregunto?', 'C1 y C5', 'C2 y C4', 'C3 y C4', 'C1 y C5 tienen hecho, efecto y sugerencia como pregunta.'),
        ('abc', '{F} ¿Qué falla en C2, «fue lo peor que vi»?', 'No dice qué decisión ni qué efecto produce', 'Es demasiado largo para ser útil y no se entiende', 'Habla de una persona en particular y no del trabajo', 'Es una etiqueta sin hecho ni sugerencia.'),
        ('abc', '{F} ¿Qué falla en C3, «Fulano se mueve raro»?', 'Ataca a una persona y su cuerpo, no a una decisión', 'No tiene una sugerencia en forma de pregunta al final', 'Es demasiado largo para ser un comentario útil', 'La retroalimentación no evalúa cuerpos ni personas.'),
        ('abc', '{F} ¿Qué falta en C4, «me gustó mucho, quedó perfecto»?', 'Qué se conserva y por qué', 'Una frase más larga y con más elogios', 'El nombre de quién lo dice y el curso', 'Un elogio útil dice qué funciona y por qué.'),
        ('abc', '{F} ¿Cuál es el hecho observable de C5?', 'La tercera persona entra 2 tiempos tarde', 'El canon se ve desordenado', 'Una señal con la mirada ayudaría', 'El hecho es la entrada tardía; el efecto es el desorden y la sugerencia es la mirada.'),
        ('=', '{F} Si el canon de 4 personas entra cada 4 tiempos desde el tiempo 1, ¿en qué tiempo debería entrar la tercera?', '1+2*4', 'La primera entra en 1, la segunda en 5 y la tercera en 9.', ''),
        ('abc', '{F} Para mejorar C3, ¿cuál es una reescritura adecuada?', 'Observo que el gesto cambia de dirección sin pausa; esto produce brusquedad; me pregunto si una pausa ayudaría', 'Fulano debería dejar de moverse así, porque se ve mal', 'Fulano es muy distinto a los demás y no encaja en el grupo', 'La reescritura habla del gesto, no de la persona.'),
        ('abc', '{F} Al recibir C1, el grupo siente que la sugerencia cambia su propósito. ¿Qué corresponde?', 'Agradecer, preguntar y decidir con una razón qué incorporar', 'Rechazarla de inmediato sin escuchar los argumentos del grupo', 'Aceptarla sin pensarlo para evitar conflictos con el otro grupo', 'Se recibe, se pregunta y se decide con razones.'),
        ('abc', 'Dos estudiantes discuten: una dice que la crítica dura es más honesta; el otro, que una crítica específica y respetuosa ayuda más a mejorar. ¿Quién argumenta mejor?', 'El otro, porque una crítica específica orienta el cambio', 'La primera, porque la dureza muestra la verdad', 'Ninguno, porque criticar siempre hiere a quien la recibe', 'La especificidad hace útil la crítica; la dureza no agrega información.'),
        ('abc', '{F} Una persona del grupo comentado no quiere que se comente su parte en voz alta. ¿Qué corresponde?', 'Ofrecer hacerlo por escrito o en privado', 'Comentar igual, porque es parte de la actividad', 'Pedirle que explique por qué no quiere', 'El consentimiento se respeta y se ofrecen alternativas.'),
        ('abc', '{F} Durante la retroalimentación, alguien comienza a burlarse de una integrante. ¿Qué corresponde?', 'Detener el comentario y avisar a una persona adulta', 'Reírse para no quedar fuera del grupo ni parecer aburrido', 'Ignorarlo, porque seguramente solo es una broma pasajera', 'La burla se detiene y se avisa a una persona adulta.'),
        ('abc', 'Un grupo recibe 10 sugerencias y quiere aplicarlas todas a la vez. ¿Qué es lo más prudente?', 'Elegir una o dos y comprobar su efecto por separado', 'Aplicar las 10 de una vez para cumplir con todas las personas', 'No aplicar ninguna, porque son demasiadas para el tiempo que hay', 'Un cambio por vez permite saber cuál ayudó.'),
    ],
    ctx=('abc', 'Un curso debe dar retroalimentación sobre una frase que dura 3 minutos y en la que la sección final repite el mismo gesto 8 veces. ¿Cuál es el comentario mejor armado?', 'Observo que el gesto se repite 8 veces sin cambios; esto produce monotonía; me pregunto si un cambio de tamaño ayudaría', 'Se repite mucho y se hace aburrido, así que está mal hecho y hay que cambiarlo', 'Quedó muy bien, porque se ve bonito y se nota que hubo esfuerzo', 'El primero tiene hecho, efecto y pregunta.'),
    sc=[
        ("En creación en danza: ¿cuáles son las tres partes de una retroalimentación descriptiva?", "Observo, esto produce y me pregunto si", "Dan un hecho, un efecto y una sugerencia."),
        ("¿Qué se hace antes de comentar el trabajo de alguien?", "Se pide su consentimiento", "Nadie está obligado a ser comentado."),
        ("¿Cómo se reciben los comentarios?", "Escuchando, preguntando y decidiendo después con razones", "Así se aprende y se decide con criterio."),
    ],
    op=("Elige un trabajo inventado de pares (puede ser una frase de tres líneas que describas) y escribe tres retroalimentaciones: una que diga qué conservar y dos que sugieran mejoras, todas con el formato observo, esto produce, me pregunto si. Luego elige una sugerencia que recibirías y escribe por qué la incorporarías o no. Si alguien prefiere no ser comentado, escribe cómo lo ofrecerías por escrito.",
        "Trabajo: una frase de 3 minutos con propósito «esperar juntos». Conservar: observo que las 4 personas se detienen a la vez; esto produce espera compartida; me pregunto si mantener esa pausa al final reforzaría el cierre. Mejora 1: observo que el gesto se repite 8 veces; esto produce monotonía; me pregunto si un cambio de tamaño lo variaría. Mejora 2: observo que una entrada es tardía; esto produce desorden; me pregunto si una señal de mirada ayudaría. Incorporaría la primera mejora, porque no cambia el propósito.",
        ["las tres retroalimentaciones siguen el formato descriptivo", "no hablan de personas ni de cuerpos", "justifica qué sugerencia incorporaría"],
        ["hoja con tres retroalimentaciones y una decisión"],
        ["opinar sobre personas", "no incluir el efecto", "aplicar todo a la vez"],
        "Pregunta: «¿qué hecho observas y qué efecto produce?». Si responde con una opinión, pídele que cite un momento específico."),
    reinforce="Reescribe cinco comentarios del estilo «me gustó» o «está mal» con el formato observo, esto produce, me pregunto si.",
    extend="Explica por qué recibir retroalimentación sin defenderse ayuda a mejorar un trabajo y cómo decidir qué sugerencias incorporar.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (autoevaluación y coevaluación de ejemplo, inventadas, de un grupo de 4 sobre su frase). Pauta de 1 a 4 en cuatro criterios: claridad del propósito, uso de variaciones, coordinación del grupo y puesta en escena. "
     "Autoevaluación del grupo: claridad 4, variaciones 3, coordinación 4, puesta en escena 3. "
     "Coevaluación de un grupo vecino (3 personas observadoras): claridad 3, 3 y 3; variaciones 2, 3 y 2; coordinación 3, 3 y 3; puesta en escena 4, 3 y 3. "
     "Evidencias citadas por el grupo vecino: «la pausa del minuto 2 deja claro el propósito»; «las variaciones se parecen mucho»; «la entrada es pareja»; «la luz baja ayuda». "
     "Sesgo de generosidad: tender a ponerse más puntaje del que muestran las evidencias. Sesgo de severidad: tender a ponerse menos. "
     "Los puntajes evalúan la frase y sus decisiones, no a las personas.")
build(
    O7, 4, F,
    use="Aprenderé a autoevaluar y coevaluar con una pauta, a calcular promedios y diferencias, a reconocer sesgos de generosidad y severidad y a conversar sobre las diferencias usando evidencias.",
    prior=["Sé usar una pauta de criterios.", "Sé dar retroalimentación descriptiva.", "Sé calcular promedios de números enteros."],
    explain=[
        "La autoevaluación es la valoración que un grupo o una persona hace de su propio trabajo; la coevaluación es la que hacen otras personas observadoras con la misma pauta. Comparar ambas permite ver puntos ciegos: aspectos que quien hizo el trabajo no nota o que quien lo mira no entiende. Para compararlas se usan los mismos criterios y la misma escala de puntajes, aquí de 1 (se inicia) a 4 (logrado).",
        "Para sintetizar varias coevaluaciones se calcula el promedio: se suman los puntajes y se divide por la cantidad. En «variaciones», los puntajes 2, 3 y 2 suman 7 y el promedio no es un entero, así que se puede decir «entre 2 y 3» o comparar por suma. La diferencia entre autoevaluación y coevaluación indica dónde conversar. Una gran diferencia puede deberse a sesgo de generosidad (ponerse más) o de severidad (ponerse menos) o a que hay evidencias que no se vieron.",
        "Las diferencias se discuten con evidencias, no con presión: «¿qué hecho respalda tu puntaje?». Si ambos grupos citan evidencias distintas, se revisa la obra juntos. Los puntajes evalúan la frase y sus decisiones, no a las personas, y nadie está obligado a mostrar su evaluación al curso. Si una conversación se tensa, se hace una pausa y se avisa a una persona adulta.",
    ],
    vocab=[("autoevaluación", "valoración que se hace del propio trabajo"), ("coevaluación", "valoración que hacen otras personas con la misma pauta"), ("promedio", "suma de los datos dividida por la cantidad de datos"), ("sesgo de generosidad", "tendencia a ponerse más puntaje del que muestran las evidencias"), ("sesgo de severidad", "tendencia a ponerse menos puntaje"), ("punto ciego", "aspecto que alguien no nota de su propio trabajo")],
    worked=[
        ("Calcular un promedio", "Tres personas ponen 3, 4 y 2 en un criterio. ¿Cuál es el promedio?", ["Suma los puntajes: 3 + 4 + 2 = 9.", "Divide por 3: 9 / 3 = 3."], "3"),
        ("Calcular una diferencia", "Autoevaluación: 4. Promedio de la coevaluación: 3. ¿Cuál es la diferencia?", ["Resta el promedio al puntaje de autoevaluación.", "4 - 3 = 1."], "1 punto"),
    ],
    mistakes=[("Pensar que la autoevaluación siempre debe coincidir con la coevaluación.", "Las diferencias muestran puntos ciegos y sirven para conversar.", "Usa las diferencias como punto de partida para revisar evidencias."),
              ("Subir o bajar un puntaje para no tener diferencias.", "El puntaje debe reflejar las evidencias, no evitar un conflicto.", "Defiende el puntaje con un hecho observable o ajústalo si hay una razón mejor.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es la coevaluación?', 'La valoración de otras personas con la misma pauta', 'La valoración que hace el grupo de su propio trabajo', 'La nota final que pone la persona que enseña a cada grupo', 'La coevaluación la hacen otras personas observadoras con la misma pauta.'),
        ('=', '{F} ¿Cuántos puntos suman los cuatro criterios de la autoevaluación?', '4+3+4+3', 'Se suman los puntajes de claridad, variaciones, coordinación y puesta en escena.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma el grupo vecino en el criterio de variaciones entre las 3 personas?', '2+3+2', 'Los puntajes son 2, 3 y 2.', ' puntos'),
        ('=', '{F} ¿Cuál es el promedio de coordinación del grupo vecino?', '(3+3+3)/3', 'Los tres puntajes de coordinación son 3 y su promedio es 3.', ''),
        ('abc', '{F} ¿Qué criterio tiene la menor suma de puntajes del grupo vecino?', 'Variaciones, con 7 puntos', 'Claridad, con 9 puntos', 'Puesta en escena, con 10 puntos', 'Las sumas son 9, 7, 9 y 10: la menor es la de variaciones.'),
        ('=', '{F} En claridad la autoevaluación es 4 y el grupo vecino puso 3, 3 y 3. ¿Cuántos puntos de diferencia hay entre la autoevaluación y el promedio de esa coevaluación?', '4-(3+3+3)/3', 'Se resta el promedio de la coevaluación al puntaje de la autoevaluación.', ' punto'),
        ('abc', '{F} ¿Qué sesgo parece haber en la autoevaluación de claridad y coordinación?', 'Generosidad, porque se pusieron 4 y el grupo vecino puso 3 de promedio', 'Severidad, porque se pusieron menos puntos que el grupo vecino', 'Ninguno, porque la autoevaluación siempre tiene razón', 'Ponerse más que lo que ven otras personas puede indicar generosidad, aunque habría que revisar evidencias.'),
        ('abc', '{F} Para conversar sobre claridad, ¿qué es lo más útil?', 'Preguntar qué hecho respalda cada puntaje y revisar la evidencia', 'Insistir en que el grupo se ponga 3 para igualar a los demás', 'Dejar el puntaje de 4 sin conversar con nadie del grupo vecino', 'Se conversa con evidencias, no por presión.'),
        ('abc', '{F} El grupo vecino dice que «las variaciones se parecen mucho». ¿Qué decisión de revisión es más coherente?', 'Cambiar una variación a la vez para aumentar la diferencia entre ellas', 'Cambiar todas las variaciones a la vez para no repetir ninguna', 'Mantener todo igual, porque la autoevaluación fue 3', 'Un cambio por vez permite comprobar qué mejora.'),
        ('abc', 'Dos estudiantes discuten: uno dice que si las evaluaciones no coinciden, alguien se equivocó; la otra, que las diferencias muestran puntos ciegos y sirven para conversar. ¿Quién argumenta mejor?', 'La otra, porque las diferencias dan información', 'El primero, porque la verdad es una sola y alguien falló al evaluar', 'Ninguno, porque las evaluaciones no sirven para decidir nada', 'Las diferencias permiten conversar con evidencias.'),
        ('abc', '{F} Un integrante propone cambiar su puntaje de 4 a 3 en claridad «para que nadie moleste». ¿Qué corresponde?', 'Revisar la evidencia y decidir por razones, no por evitar conflictos', 'Cambiarlo, porque es mejor llevarse bien con el grupo vecino', 'Cambiarlo a 1 para quedar seguro y que nadie reclame', 'El puntaje debe respaldar la evidencia, no la comodidad.'),
        ('abc', '{F} Alguien propone usar la coevaluación para comparar a las personas del grupo entre sí. ¿Qué corresponde?', 'Rechazarlo: los puntajes evalúan decisiones, no personas', 'Aceptarlo para ver quién aporta más al trabajo del grupo', 'Aceptarlo solo con las personas que prefieren que las comparen', 'Las personas y los cuerpos no se evalúan ni se comparan.'),
        ('abc', 'Durante la conversación entre grupos, una integrante se siente criticada y se enoja. ¿Qué corresponde?', 'Hacer una pausa, volver a los hechos y avisar a una persona adulta', 'Seguir la conversación hasta que se calme sola', 'Pedirle que se retire sin explicarle por qué es mejor así', 'Una pausa y la ayuda adulta cuidan el clima del grupo.'),
    ],
    ctx=('abc', 'Un grupo se pone 4 en claridad y tres personas observadoras ponen 4, 2 y 3. ¿Cuál es el promedio de la coevaluación y qué hace el grupo?', 'Promedio 3; conversa con evidencias sobre el 2', 'Promedio 4; no conversa porque coincide con su autoevaluación', 'Promedio 2; baja su puntaje de inmediato sin conversar', 'La suma es 9 y el promedio 3; el 2 señala un posible punto ciego que conviene conversar.'),
    sc=[
        ("En creación en danza: ¿cómo se calcula un promedio?", "Se suman los puntajes y se divide por la cantidad", "Por ejemplo, 3, 4 y 2 suman 9 y el promedio es 3."),
        ("¿Qué indica una diferencia grande entre auto y coevaluación?", "Un punto ciego o un sesgo que conviene revisar con evidencias", "No significa que alguien mienta ni que se equivoque."),
        ("¿Qué se evalúa con la pauta: personas o decisiones?", "La frase y las decisiones", "Las personas no se evalúan con la pauta."),
    ],
    op=("A partir de una frase breve de tu elección, con puntajes de ejemplo que escribirás tú, completa una tabla de autoevaluación (1 a 4) y coevaluación de tres observadores en cuatro criterios. Calcula los promedios, las diferencias y señala el criterio con mayor diferencia. Escribe una pregunta para conversar sobre ese criterio con evidencias y una decisión de mejora (un solo cambio). No evalúes personas.",
        "Criterios: claridad, variaciones, coordinación, puesta en escena. Autoevaluación: 4, 3, 4, 3. Coevaluación (3 observadores): claridad 3, 3, 3 (promedio 3); variaciones 2, 3, 2 (promedio entre 2 y 3); coordinación 3, 3, 3 (3); puesta en escena 4, 3, 3 (entre 3 y 4). Mayor diferencia: claridad y coordinación (4 frente a 3). Pregunta: «¿qué hecho respalda el 4 en claridad?». Mejora: cambiar solo una variación para diferenciarla.",
        ["los promedios y diferencias están bien calculados", "reconoce el criterio de mayor diferencia", "propone una pregunta con evidencias y un solo cambio"],
        ["tabla con puntajes, promedios, diferencias y mejora"],
        ["calcular mal el promedio", "evaluar personas", "bajar el puntaje para evitar conflictos"],
        "Pregunta: «¿qué evidencia respalda ese puntaje?». Si responde «lo siento así», pídele que cite un hecho observable."),
    reinforce="Inventa una tabla de puntajes de tres personas en un criterio y calcula el promedio y la diferencia con una autoevaluación de 4.",
    extend="Explica por qué los sesgos de generosidad y severidad no significan que la persona mienta y cómo se pueden reducir.",
)

# ============================================================ OAC-07, clase 5
F = ("Ficha 5 (posibles mejoras de ejemplo, inventadas, para la frase de un grupo). Cada mejora se puntúa de 1 a 3 en impacto (cuánto aporta al propósito) y de 1 a 3 en esfuerzo (cuánto cuesta en tiempo y energía). "
     "M1: acortar una pausa de 6 a 4 tiempos; impacto 2, esfuerzo 1. "
     "M2: cambiar la música por un sonido nuevo creado por el grupo; impacto 3, esfuerzo 3. "
     "M3: agregar una señal de mirada para entrar en el canon; impacto 3, esfuerzo 1. "
     "M4: rehacer toda la sección 2; impacto 2, esfuerzo 3. "
     "M5: cambiar el vestuario; impacto 1, esfuerzo 2. "
     "Prioridad = impacto - esfuerzo (mayor es mejor; en caso de empate, se elige la de menor esfuerzo). "
     "Meta observable de ejemplo: subir la claridad del propósito de 2 a 3 en la pauta de 1 a 4 en el siguiente ensayo. "
     "Plan: un cambio por ensayo, 3 ensayos de 30 minutos, registro después de cada uno.")
build(
    O7, 5, F,
    use="Aprenderé a convertir una evaluación crítica en un plan de mejora: priorizar cambios por impacto y esfuerzo, definir una meta observable, probar un cambio por ensayo y revisar el efecto con evidencias.",
    prior=["Sé evaluar proceso y resultado.", "Sé dar y recibir retroalimentación.", "Sé comparar puntajes de una pauta."],
    explain=[
        "Evaluar sirve para decidir qué hacer después. Un plan de mejora parte de los hallazgos de la evaluación y los convierte en cambios concretos. Como no se puede hacer todo a la vez, se priorizan. Una forma sencilla es puntuar cada mejora por impacto (cuánto aporta al propósito) y por esfuerzo (cuánto cuesta en tiempo y energía) y calcular la prioridad como impacto menos esfuerzo: mientras más alta, más conviene hacerla primero. Si dos mejoras empatan, se elige la de menor esfuerzo.",
        "Un buen plan tiene una meta observable: algo que se pueda comprobar en el siguiente ensayo, como «subir la claridad del propósito de 2 a 3». Se cambia una cosa por ensayo para saber qué la produjo, se registra el efecto después de cada ensayo y se decide si el cambio se conserva, se ajusta o se descarta. Un cambio que no mejora no es un fracaso: es información.",
        "El plan debe ser realista y seguro. Se calcula el tiempo disponible (por ejemplo, 3 ensayos de 30 minutos son 90 minutos), se cuidan el calentamiento y el descanso, y se evita cualquier cambio que exija saltos, cargas o forzar el cuerpo. Se evalúa el plan y no a las personas. Si alguien se siente sobrecargado con el plan, se ajustan las tareas y se avisa a una persona adulta si hace falta.",
    ],
    vocab=[("plan de mejora", "conjunto de cambios concretos para mejorar un trabajo"), ("impacto", "cuánto aporta un cambio al propósito"), ("esfuerzo", "cuánto cuesta un cambio en tiempo y energía"), ("prioridad", "orden en que conviene hacer los cambios"), ("meta observable", "resultado que se puede comprobar"), ("criterio de éxito", "dato que indica que el cambio funcionó")],
    worked=[
        ("Calcular la prioridad", "Una mejora tiene impacto 3 y esfuerzo 2. ¿Cuál es su prioridad?", ["Resta el esfuerzo al impacto.", "3 - 2 = 1."], "1"),
        ("Elegir entre dos mejoras", "Mejora X: prioridad 1, esfuerzo 2. Mejora Y: prioridad 1, esfuerzo 1. ¿Cuál se hace primero?", ["Empatan en prioridad.", "Se elige la de menor esfuerzo: Y."], "La mejora Y"),
    ],
    mistakes=[("Intentar aplicar todas las mejoras a la vez.", "No se sabe cuál produjo el efecto y se sobrecarga al grupo.", "Elige una o dos y pruébalas por separado."),
              ("Proponer metas vagas como «que quede mejor».", "No se puede comprobar si se cumplió.", "Define una meta con un dato observable, como subir de 2 a 3 en un criterio.")],
    T=[
        ('abc', 'En creación en danza, ¿qué es una meta observable?', 'Un resultado que se puede comprobar en el próximo ensayo', 'Una intención general de que todo salga bien en la muestra', 'Un deseo de que el público aplauda más fuerte esta vez', 'Una meta observable permite comprobar si se cumplió.'),
        ('=', '{F} ¿Cuántos puntos de prioridad más tiene M3 que M1?', '(3-1)-(2-1)', 'M3 tiene prioridad 3 menos 1 y M1 tiene 2 menos 1; se restan ambas prioridades.', ' punto'),
        ('=', '{F} Si M2 bajara su esfuerzo de 3 a 2, ¿cuál sería su nueva prioridad?', '3-2', 'La prioridad es el impacto de M2, 3, menos el nuevo esfuerzo, 2.', ''),
        ('abc', '{F} ¿Qué mejora tiene la mayor prioridad?', 'M3', 'M1', 'M2', 'M3 tiene prioridad 2 y M1 tiene 1.'),
        ('abc', '{F} ¿Cuántas mejoras tienen prioridad negativa?', 'Dos: M4 y M5', 'Una: solo M4', 'Tres: M2, M4 y M5', 'M4 tiene -1 y M5 tiene -1; M2 tiene 0, que no es negativa.'),
        ('=', '{F} Los 3 ensayos duran 30 minutos cada uno. ¿Cuántos minutos suman?', '3*30', 'Se multiplican los ensayos por su duración.', ' minutos'),
        ('abc', '{F} Si se aplican primero M3 y luego M1, cada una en un ensayo distinto, ¿qué ventaja tiene?', 'Permite saber qué efecto produjo cada cambio', 'Permite terminar antes el plan completo', 'Evita registrar lo que ocurre en cada ensayo', 'Un cambio por ensayo permite atribuir el efecto.'),
        ('abc', '{F} ¿Qué criterio de éxito es el más claro para M3?', 'Que la claridad suba de 2 a 3 en la pauta', 'Que el grupo se sienta mejor y más contento con la frase', 'Que el público aplauda de pie cuando termine la frase', 'Un dato de la pauta se puede comprobar.'),
        ('abc', '{F} Tras M3, la claridad sube de 2 a 3. ¿Qué decisión es coherente?', 'Conservar la señal y probar M1 en el siguiente ensayo', 'Quitar la señal, porque ya no hace falta en los ensayos', 'Aplicar M2, M4 y M5 en el mismo ensayo para ahorrar tiempo', 'Se conserva lo que funciona y se prueba el siguiente cambio.'),
        ('abc', 'Dos estudiantes discuten: uno dice que se deben hacer primero las mejoras de mayor impacto aunque cuesten mucho; la otra, que se priorizan por impacto menos esfuerzo. ¿Quién argumenta mejor?', 'La otra, porque considera tanto el aporte como el costo', 'El primero, porque lo que más aporta siempre debe hacerse primero', 'Ninguno, porque no se pueden priorizar cambios', 'La prioridad combina impacto y esfuerzo.'),
        ('abc', '{F} Tras un ensayo, el cambio M1 no mejora la claridad (queda en 2). ¿Qué es lo más adecuado?', 'Registrar que no funcionó y probar otro cambio', 'Considerarlo un fracaso del grupo y dejar de ensayar ese día', 'Mantenerlo y aplicar otros cuatro cambios en el mismo ensayo', 'Un cambio sin mejora es información para decidir el siguiente.'),
        ('abc', '{F} Para M4 (rehacer la sección 2) el grupo propone agregar saltos grandes y giros rápidos para dar «más impacto». ¿Qué corresponde?', 'Descartar los saltos y giros y buscar otra decisión segura', 'Aceptarlos, porque aumentan el impacto de la sección', 'Aceptarlos solo si el grupo los practica mucho antes de la muestra', 'La seguridad está antes del impacto; no hay saltos ni giros rápidos en este cuaderno.'),
        ('abc', 'Una integrante dice que el plan la sobrecarga porque tiene muchas tareas. ¿Qué corresponde?', 'Redistribuir tareas y avisar a una persona adulta si persiste', 'Pedirle que lo soporte hasta el final de los tres ensayos', 'Excluirla del plan sin consultarle para no sobrecargarla más', 'Se ajusta el plan al bienestar de las personas.'),
    ],
    ctx=('abc', 'Un grupo tiene tres mejoras: X (impacto 3, esfuerzo 1), Y (impacto 2, esfuerzo 2) y Z (impacto 3, esfuerzo 2). Tiene 3 ensayos y quiere hacer una por ensayo, en orden de prioridad. ¿Cuál es el orden?', 'X, Z, Y', 'Y, Z, X', 'Z, X, Y', 'Las prioridades son X 2, Y 0 y Z 1, por lo que el orden es X, Z, Y.'),
    sc=[
        ("En creación en danza: ¿cómo se calcula la prioridad de una mejora?", "Impacto menos esfuerzo", "Considera cuánto aporta y cuánto cuesta."),
        ("¿Cuántos cambios conviene probar por ensayo?", "Uno solo", "Así se sabe qué cambio produjo el efecto."),
        ("¿Qué se hace si un cambio no mejora el resultado?", "Se registra, se revisa por qué y se prueba otro", "Un cambio sin mejora entrega información."),
    ],
    op=("Elige una frase inventada de tu elección y plantea cinco posibles mejoras con impacto y esfuerzo (1 a 3). Calcula la prioridad de cada una, elige una para el primer ensayo y escribe: la meta observable, cómo comprobarás que funcionó, cuántos ensayos usarás y cuántos minutos suman. No incluyas cambios que obliguen a saltar, cargar o forzar el cuerpo.",
        "Frase: «esperar juntos». Mejoras: M1 acortar una pausa (impacto 2, esfuerzo 1, prioridad 1); M2 cambiar el sonido (3, 3, 0); M3 señal de mirada (3, 1, 2); M4 rehacer sección 2 (2, 3, -1); M5 cambiar vestuario (1, 2, -1). Primer ensayo: M3. Meta: subir la claridad de 2 a 3. Comprobación: pauta de 1 a 4 al final del ensayo. Plan: 3 ensayos de 30 minutos, 90 minutos en total.",
        ["las prioridades están bien calculadas", "la meta es observable y se puede comprobar", "el plan prueba un cambio por ensayo y es seguro"],
        ["tabla de mejoras con prioridades, meta y plan de ensayos"],
        ["priorizar sin calcular", "metas vagas", "cambios inseguros"],
        "Pregunta: «¿cómo sabrás que funcionó?». Si responde «se verá mejor», pídele un dato observable."),
    reinforce="Con cuatro mejoras inventadas, calcula las prioridades y escribe en qué orden las probarías en tres ensayos.",
    extend="Explica por qué priorizar por impacto menos esfuerzo es mejor que hacer primero las mejoras más fáciles o las más impactantes.",
)
