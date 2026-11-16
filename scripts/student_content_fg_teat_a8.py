"""Teatro 3.º y 4.º medio FG: OAC-05 (evaluación crítica de procesos y obras teatrales), clases 1 a 3. Funciones y registros originales e inventados; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O5 = "FG-TEAT-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (descripción de una función de ejemplo, «Los paraguas», inventada). Cuatro intérpretes cruzan el espacio con paraguas abiertos, sin hablar. La luz es azul y baja. "
     "Cada vez que uno se detiene, los otros tres lo rodean y levantan sus paraguas hasta ocultarlo. Al final queda un paraguas solo en el suelo. La función dura 8 minutos.")
build(
    O5, 1, F,
    use="Aprenderé a evaluar una obra en tres pasos (describir, interpretar y valorar) y a distinguir una valoración fundada de un simple gusto personal.",
    prior=["Distingo hechos de interpretaciones.", "Sé inferir el propósito de una obra con evidencia.", "Sé que un criterio estético es un aspecto que se observa."],
    explain=[
        "Evaluar críticamente una obra es mucho más que decir si gustó. Se hace en tres pasos. Primero se describe: qué se ve y se oye, con hechos que otra persona pueda comprobar. Luego se interpreta: qué sugieren esos hechos y qué propósito se infiere, siempre apoyado en lo descrito. Por último se valora: se juzga qué tan bien logra la obra su propósito, usando criterios estéticos y razones.",
        "Una valoración fundada nombra un criterio, cita la evidencia y explica el efecto. Por ejemplo: «los paraguas que ocultan al intérprete funcionan, porque muestran con un solo objeto cómo el grupo borra a una persona». El gusto personal («me gustó», «me aburrió») es legítimo, pero no es una evaluación por sí solo: se puede acompañar de razones, y se rotula como opinión.",
        "También se evalúa con respeto. Se habla de la obra y de las decisiones, no de las personas, y se acepta que otras personas lean la obra de otra manera. Las funciones de esta clase son descripciones inventadas; si el grupo ve una función real, la elige con su docente y respeta las normas de la sala.",
    ],
    vocab=[("evaluar", "valorar una obra con criterios y razones"), ("describir", "decir qué se ve y se oye, con hechos comprobables"), ("interpretar", "proponer qué sugieren los hechos y qué propósito tiene la obra"), ("valorar", "juzgar qué tan bien una obra logra su propósito"), ("gusto personal", "reacción individual que no necesita razones")],
    worked=[
        ("Separar los tres pasos", "Una crítica dice: «Los intérpretes caminan con paraguas; la luz es azul; esto expresa soledad; me parece muy logrado». Ubica cada parte.", ["Describir: caminan con paraguas y la luz es azul.", "Interpretar: expresa soledad. Valorar: es muy logrado (falta decir por qué)."], "Describe, interpreta y valora, pero falta el fundamento de la valoración"),
        ("Fundamentar una valoración", "Tienes la frase «me gustó el final». Reescríbela con criterio, evidencia y efecto.", ["Criterio: uso de los objetos. Evidencia: queda un paraguas solo en el suelo.", "Efecto: sugiere ausencia, lo que apoya el propósito de mostrar a quien desaparece."], "El paraguas solo en el suelo funciona porque sugiere la ausencia de alguien"),
    ],
    mistakes=[("Decir «estuvo bien» como si fuera una evaluación.", "No indica criterio ni evidencia.", "Agrega qué criterio miraste, qué viste y qué efecto produjo."),
              ("Mezclar en una misma frase lo que se vio, lo que se interpreta y lo que se valora.", "Se pierde la evidencia y no se sabe qué sostiene el juicio.", "Escribe los tres pasos por separado.")],
    T=[
        ('abc', '¿Cuál es el orden de los tres pasos de una evaluación crítica?', 'Describir, interpretar y valorar', 'Valorar, describir e interpretar al final', 'Interpretar, valorar y después describir con calma', 'Se parte de los hechos, luego se les da sentido y al final se juzga.'),
        ('abc', '{F} ¿Cuál de estas frases es una descripción?', 'Cuatro intérpretes cruzan con paraguas abiertos y sin hablar', 'La obra muestra la soledad de las personas', 'Es la mejor función de todo el festival y la que más me emocionó', 'La primera cuenta lo que se ve y se oye; las otras interpretan o valoran.'),
        ('abc', '{F} ¿Cuál es una interpretación apoyada en lo que se ve?', 'Cuando rodean y ocultan a quien se detiene, el grupo borra a la persona', 'Cuatro intérpretes cruzan con paraguas abiertos y sin hablar', 'La función dura 8 minutos y tiene luz azul', 'La interpretación propone un sentido a partir del hecho de rodear y ocultar.'),
        ('abc', '¿Qué distingue una valoración fundada de un gusto personal?', 'Nombra un criterio, cita evidencia y explica el efecto', 'Es más larga y usa palabras más difíciles', 'Siempre coincide con lo que opina la mayoría del público', 'Una valoración fundada se sostiene con criterio y evidencia, no con la cantidad de palabras.'),
        ('abc', '{F} Una espectadora dice: «Me aburrí porque no hablaban». ¿Qué tipo de comentario es?', 'Una opinión personal que aún no explica un criterio ni cita evidencia', 'Una descripción objetiva que todos comprobarían', 'Una interpretación fundada del propósito de la obra, apoyada en un hecho comprobable', 'Expresa lo que sintió; falta nombrar el criterio y el efecto en la obra.'),
        ('abc', '{F} ¿Qué valoración está fundada?', 'El paraguas solo al final funciona porque sugiere la ausencia de alguien, apoyando el propósito', 'El paraguas solo al final me pareció lindo y me gustó mucho', 'El paraguas solo al final es mejor que cualquier otra cosa que he visto en mi vida y en todos los festivales', 'La primera da criterio, evidencia y efecto; las otras solo expresan gusto.'),
        ('=', 'La función dura 8 minutos. Los intérpretes se detienen y son ocultados 5 veces, y cada ocultamiento dura 40 segundos. ¿Cuántos segundos de la función son ocultamientos?', '5*40', 'Se multiplica el número de ocultamientos por su duración.', ' segundos'),
        ('abc', 'Al evaluar a un grupo de pares, ¿cómo se habla de los intérpretes?', 'De sus decisiones y de lo que se vio, no de cómo es cada persona', 'De cómo son las personas fuera de la escena, para comprender su trabajo', 'De quién actuó mejor y quién peor, con apodos incluidos', 'La crítica se centra en la obra y sus decisiones, no en las personas.'),
        ('abc', '{F} Alguien opina que «Los paraguas» trata de la soledad y otra, de la presión del grupo. ¿Qué corresponde?', 'Revisar la evidencia que sostiene cada lectura sin exigir una sola respuesta', 'Pedir a quien habla menos que acepte la lectura de la mayoría para terminar rápido la conversación', 'Anular las dos lecturas porque no coinciden', 'Las lecturas se comparan por evidencia, y puede haber más de una razonable.'),
        ('abc', 'Escribes: «La luz azul crea frialdad, lo que apoya el propósito». ¿Qué pasos aparecen?', 'Describir (luz azul), interpretar (frialdad) y valorar (apoya el propósito)', 'Solo describir, porque nombra la luz y no explica nada de lo que produce', 'Solo valorar, porque dice que funciona', 'Contiene los tres pasos de manera breve y ordenada.'),
        ('abc', 'Un estudiante dice: «Mi gusto es mi evaluación». ¿Qué responderías?', 'El gusto es válido, pero una evaluación necesita criterio, evidencia y razones', 'Tiene razón, porque no hay diferencia entre gusto y evaluación ni se necesitan razones ni evidencia', 'El gusto no vale y no debe expresarse', 'El gusto personal es válido como opinión; la evaluación agrega fundamento.'),
        ('=', 'Un registro de crítica tiene 15 frases: 6 describen, 4 interpretan y el resto valora. ¿Cuántas frases son valoraciones?', '15-6-4', 'Se restan las frases de descripción e interpretación al total.', ' frases'),
        ('abc', '{F} Dos críticas sobre «Los paraguas»: una dice «Me encantó» y otra «Los paraguas muestran con un solo objeto cómo se borra a una persona; el recurso es claro». ¿Cuál es más útil al grupo?', 'La segunda, porque indica qué decisión funcionó y por qué', 'La primera, porque da más ánimo al grupo', 'Las dos por igual, porque ambas son positivas', 'La segunda da información para conservar lo que funcionó.'),
    ],
    ctx=('ab', 'Tu compañero te pide tu opinión sobre su escena. ¿Cómo respondes?', 'Describo lo que vi, interpreto su efecto y valoro con una razón', 'Solo le digo si me gustó o no, sin explicarle por qué', 'Una respuesta con los tres pasos ayuda más que decir solo si gustó.'),
    sc=[
        ("En Teatro: ¿cuáles son los tres pasos de una evaluación crítica?", "Describir, interpretar y valorar", "Separan lo observado, su sentido y el juicio."),
        ("¿Qué necesita una valoración fundada?", "Un criterio, evidencia y una explicación del efecto", "Sin esos tres elementos es solo gusto."),
        ("Al evaluar a un compañero, ¿se habla de la persona o de la obra?", "De la obra y de sus decisiones", "Así la crítica ayuda sin herir."),
    ],
    op=("Imagina que viste esta función de ejemplo: «Una intérprete barre un escenario vacío durante 5 minutos, a veces más rápido, a veces más lento; al final deja la escoba apoyada en el centro». Escribe una evaluación en tres pasos: dos hechos que describes, una interpretación y una valoración con criterio, evidencia y efecto.",
        "Describo: barre durante 5 minutos y cambia de ritmo; deja la escoba al centro. Interpreto: sugiere un trabajo repetido que pierde sentido. Valoro: el cambio de ritmo funciona porque muestra cansancio, lo que apoya el propósito.",
        ["dos hechos descritos", "una interpretación apoyada", "valoración con criterio, evidencia y efecto", "lenguaje respetuoso"],
        ["hoja con la evaluación en tres pasos"],
        ["decir solo si le gustó", "mezclar los tres pasos"],
        "Pregunta: «¿qué viste exactamente que sostiene tu valoración?». Debe citar el hecho."),
    reinforce="Escribe tres frases que describan, interpreten y valoren una escena cotidiana imaginaria, una por paso.",
    extend="Explica por qué un comentario como «me gustó» puede ser sincero y aun así no alcanzar como evaluación.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (pauta y propósito de ejemplo, inventados). Propósito declarado por el grupo de «Los paraguas»: mostrar cómo la presión del grupo oculta a una persona. "
     "Pauta, con puntaje de 1 a 4: uso del cuerpo y del gesto, uso de objetos y espacio, luz y sonido, coherencia con el propósito. "
     "Evaluación de un curso: cuerpo y gesto 3, objetos y espacio 4, luz y sonido 2, coherencia con el propósito 4.")
build(
    O5, 2, F,
    use="Aprenderé a aplicar criterios estéticos (cuerpo, voz, objetos, espacio, luz, sonido y coherencia) para evaluar una obra según el propósito expresivo que declara o que se infiere.",
    prior=["Sé describir, interpretar y valorar.", "Sé inferir propósitos expresivos.", "Sé leer una pauta de criterios."],
    explain=[
        "Los criterios estéticos son aspectos de una obra que se observan para valorar cómo comunica. Algunos usuales son el uso expresivo del cuerpo, del gesto y de la voz; el uso del espacio y de los objetos; la luz y el sonido; el ritmo; la coherencia entre las decisiones; y la claridad con que se entiende la propuesta. No hay un criterio mejor que otro: se eligen los que sirven para analizar esa obra.",
        "La clave es evaluar según el propósito. Una misma decisión puede ser acertada para un propósito y equivocada para otro. Una luz muy tenue funciona si el propósito es la intimidad, pero perjudica si lo que se quiere es que el público lea un texto proyectado. Por eso se pregunta primero qué busca la obra y luego qué tan bien lo logran sus decisiones.",
        "Una pauta ordena la evaluación: cada criterio tiene un puntaje, pero el puntaje se acompaña de una razón con evidencia. La coherencia con el propósito pregunta si todas las decisiones apuntan a lo mismo. Sumar puntajes sirve para ver tendencias, no reemplaza el análisis. Los puntajes de ejemplo de esta clase son inventados.",
    ],
    vocab=[("criterio estético", "aspecto de la obra que se observa para valorar cómo comunica"), ("coherencia", "relación entre las decisiones de la obra y su propósito"), ("claridad", "facilidad con que se entiende la propuesta"), ("tendencia", "dirección general que muestran varios puntajes"), ("justificar", "dar una razón con evidencia")],
    worked=[
        ("Evaluar según el propósito", "El propósito es crear intimidad. La luz es muy tenue. ¿Cómo se valora la luz?", ["La luz tenue favorece la intimidad que se busca.", "Se valora de manera positiva, citando ese efecto."], "La luz tenue es acertada para ese propósito"),
        ("Justificar un puntaje", "Pones 2 en luz y sonido a una obra. ¿Qué escribes junto al puntaje?", ["Una razón con evidencia: en el minuto 5 el sonido tapa las voces.", "Así otra persona puede comprobar por qué el puntaje es bajo."], "Una razón con evidencia observable"),
    ],
    mistakes=[("Usar los mismos criterios con el mismo peso para toda obra sin mirar su propósito.", "Un criterio puede importar mucho en una obra y poco en otra.", "Parte siempre del propósito y elige criterios útiles."),
              ("Poner un puntaje sin razón.", "No se puede comprobar ni discutir.", "Escribe la razón con evidencia junto a cada puntaje.")],
    T=[
        ('abc', '¿Qué es la coherencia en una obra?', 'La relación entre las decisiones de la obra y su propósito', 'El número de recursos que se usan en la escena', 'El acuerdo de todo el público con la obra', 'La coherencia revisa si las decisiones apuntan a lo mismo que la obra busca expresar.'),
        ('abc', '¿Por qué se evalúa una obra según su propósito?', 'Porque una decisión puede ser acertada para un propósito y equivocada para otro', 'Porque el propósito indica cuántos puntos debe tener la obra en cada criterio de la pauta', 'Porque todas las obras tienen el mismo propósito', 'El mismo recurso funciona o no según lo que la obra quiere expresar.'),
        ('abc', '{F} ¿Qué criterio obtuvo el puntaje más bajo?', 'Luz y sonido, con 2 puntos', 'Cuerpo y gesto, con 3 puntos', 'Objetos y espacio, con 4 puntos', 'Luz y sonido tiene 2 puntos, el menor de la pauta.'),
        ('abc', '{F} ¿Qué significa el puntaje 4 en coherencia con el propósito?', 'Que las decisiones apuntan con claridad a mostrar cómo el grupo oculta a una persona', 'Que la obra tiene muchos recursos técnicos y el grupo los usó todos al mismo tiempo en cada escena', 'Que a todo el público le gustó la obra', 'Un puntaje alto en coherencia indica que las decisiones sirven al propósito declarado.'),
        ('abc', 'Una luz muy tenue es acertada cuando', 'el propósito es crear intimidad y recogimiento', 'el propósito es que el público lea un texto proyectado', 'el propósito es mostrar un lugar muy iluminado', 'La luz tenue sirve a la intimidad; en los otros casos estorba.'),
        ('abc', 'Al lado del puntaje de un criterio conviene escribir', 'una razón con evidencia observable que justifique el puntaje', 'el nombre de quien actuó mejor en la escena y de quien lo hizo peor', 'una opinión sobre el resto de la obra', 'La razón con evidencia permite discutir el puntaje con fundamento.'),
        ('=', '{F} ¿Cuántos puntos suma la pauta en total?', '3+4+2+4', 'Se suman los cuatro puntajes de los criterios.', ' puntos'),
        ('abc', '{F} Un comentario del curso dice que en el minuto 5 el sonido tapaba las voces, lo que explica el 2 en luz y sonido. ¿Cuál es una sugerencia concreta?', 'Bajar el volumen del sonido para que no tape las voces en los momentos clave', 'Subir el volumen de todo para que el efecto sea más fuerte y se note desde el fondo', 'Quitar la luz y el sonido y presentar sin recursos', 'La sugerencia atiende el problema de tapar las voces y mantiene los recursos.'),
        ('abc', 'Dos personas evalúan la misma obra con distinto propósito: una cree que busca humor y otra que busca denuncia. ¿Qué ocurre con sus valoraciones?', 'Pueden diferir, porque valoran contra propósitos distintos', 'Deben ser iguales, porque la obra es la misma', 'Ninguna vale, porque no se pusieron de acuerdo', 'La valoración depende del propósito que cada una atribuye a la obra.'),
        ('abc', 'Sumas los puntajes de una obra y obtienes un número alto. ¿Qué falta para evaluar?', 'Revisar las razones de cada puntaje y la coherencia con el propósito', 'Nada, porque el número reemplaza el análisis', 'Comparar el número con el de las obras de otros cursos sin criterios', 'El número muestra una tendencia, pero no explica por qué ni para qué.'),
        ('abc', 'Un criterio es la claridad. ¿Cuál es una evidencia de poca claridad?', 'Varias personas del público no entendieron quién era cada personaje', 'La obra duró menos de lo esperado', 'Los intérpretes se vistieron de un solo color y la luz de la sala quedó encendida', 'Que el público no pueda identificar a los personajes muestra problemas de claridad.'),
        ('=', 'Una pauta de 5 criterios con puntaje máximo 4 da un máximo posible de puntos. Una obra obtiene 15. ¿Qué porcentaje del máximo logró?', '15*100//(5*4)', 'Se calcula el puntaje máximo y se divide el obtenido entre él.', ' %'),
        ('abc', 'Un grupo valora una obra de luz y sonido muy simples y la califica «pobre». La obra busca la sencillez cotidiana. ¿Qué error cometió?', 'No evaluó según el propósito, que era precisamente la sencillez', 'Usó demasiados criterios para analizar la obra', 'Dio razones y evidencia que no correspondían', 'Una decisión simple puede ser acertada si coincide con el propósito.'),
    ],
    ctx=('ab', 'Debes evaluar una obra cuyo propósito no está declarado. ¿Qué haces primero?', 'Infiero su propósito con evidencia y luego aplico los criterios', 'Aplico una pauta sin pensar en el propósito', 'Sin un propósito no hay con qué comparar si las decisiones logran lo que buscan.'),
    sc=[
        ("En Teatro: ¿qué es un criterio estético?", "Un aspecto de la obra que se observa para valorar cómo comunica", "Sirve para ordenar y fundamentar el análisis de la obra."),
        ("¿Qué se escribe junto a cada puntaje de una pauta?", "Una razón con evidencia observable", "La razón permite discutir y comprobar."),
        ("¿Por qué se evalúa según el propósito?", "Porque lo que es acertado para un propósito puede no serlo para otro", "El propósito da el sentido de la valoración."),
    ],
    op=("Escoge un propósito de ejemplo («mostrar la alegría de un reencuentro» o «mostrar la presión de un grupo»). Elige tres criterios estéticos de la clase, inventa un puntaje de 1 a 4 para una obra imaginaria y escribe una razón con evidencia para cada puntaje. Cierra con una conclusión sobre coherencia con el propósito.",
        "Propósito: mostrar la presión de un grupo. Cuerpo y gesto 3: los intérpretes se acercan hasta rodear a uno. Luz 2: la luz azul tapa los rostros. Coherencia 4: todas las decisiones apuntan a ocultar a alguien. Conclusión: es coherente aunque la luz puede mejorar.",
        ["tres criterios distintos", "razón con evidencia por puntaje", "conclusión sobre coherencia", "evalúa según el propósito"],
        ["pauta completa y conclusión"],
        ["puntajes sin razón", "no relacionar con el propósito"],
        "Pregunta: «¿esa razón dice qué se vio?». Si no, pídele agregar la evidencia."),
    reinforce="Elige una película o serie que veas (sin escribir su nombre) y anota dos criterios estéticos que usarías para evaluarla y por qué.",
    extend="Explica por qué el mismo recurso puede ser un acierto en una obra y un error en otra.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (bitácora de proceso de ejemplo, inventada). Un grupo prepara una escena de 12 minutos. Ensayo 1: no se oía la voz al fondo; la escena duró 12 minutos. "
     "Ensayo 2: subieron la proyección y recortaron una escena repetida; duró 10 minutos. Ensayo 3: ajustaron las entradas y la escena duró 8 minutos; en el comentario final, dos compañeros del curso dijeron que ahora se entendía el conflicto.")
build(
    O5, 3, F,
    use="Aprenderé a evaluar el proceso de creación (ensayos, cambios y decisiones) y no solo el resultado, tanto en obras propias como en las de mis pares, con respeto y con una bitácora como evidencia.",
    prior=["Sé evaluar una obra con criterios y propósito.", "Sé dar retroalimentación descriptiva.", "Sé que revisar el proceso permite aprender."],
    explain=[
        "Evaluar el proceso es mirar cómo se llegó a la obra: qué se probó, qué se cambió, por qué y con qué efecto. La evidencia del proceso está en la bitácora, un registro escrito de los ensayos con fecha, qué se hizo, qué se observó y qué se decidió. Un buen proceso muestra decisiones razonadas, cambios que se comprueban y trabajo en equipo; un buen resultado sin proceso no siempre muestra aprendizaje.",
        "En el caso de una obra propia, la autoevaluación consiste en revisar la bitácora y reconocer con honestidad qué funcionó y qué no, sin culparse ni culpar a otros. En el caso de una obra de pares, se da retroalimentación con respeto: se señala qué decisiones funcionaron, qué podría mejorar y qué evidencia lo respalda. Un formato útil es nombrar dos logros con evidencia y una sugerencia concreta.",
        "Evaluar el proceso incluye también cómo trabajó el equipo: si se escucharon, si repartieron roles y si cuidaron la seguridad y el consentimiento de todas las personas. Si la evaluación hiere o hay hostigamiento entre compañeros, se detiene y se avisa a una persona adulta de confianza.",
    ],
    vocab=[("proceso", "camino de ensayos, cambios y decisiones hasta la obra final"), ("bitácora", "registro escrito de los ensayos, observaciones y decisiones"), ("autoevaluación", "revisión que una persona o un grupo hace de su propio trabajo"), ("logro", "aspecto del trabajo que funcionó y se puede demostrar"), ("sugerencia", "propuesta concreta para mejorar")],
    worked=[
        ("Leer una bitácora", "Bitácora: «Ensayo 1: la voz no llegaba al fondo. Ensayo 2: respiramos antes de hablar y se escuchó en la mitad de la sala». ¿Qué evidencia de proceso hay?", ["Hay un problema identificado, un cambio hecho y un efecto observado.", "Eso muestra decisiones razonadas."], "Problema, cambio y efecto registrados"),
        ("Dar retroalimentación a un par", "Viste que sus entradas eran claras y que el sonido tapaba el diálogo. Escribe dos logros y una sugerencia.", ["Logro 1: las entradas eran claras y marcaban cada cambio de escena.", "Logro 2 y sugerencia: el conflicto se entendía; baja el volumen del sonido en el diálogo."], "Dos logros con evidencia y una sugerencia concreta"),
    ],
    mistakes=[("Evaluar solo el resultado final y no mirar la bitácora.", "No se ve cómo aprendió ni cómo decidió el equipo.", "Revisa también los ensayos y cambios."),
              ("Autoevaluarse con «todo salió perfecto» o «todo salió mal».", "No ayuda a decidir qué conservar o cambiar.", "Nombra qué funcionó y qué no, con evidencia.")],
    T=[
        ('abc', '¿Qué es una bitácora de ensayo?', 'Un registro escrito de los ensayos, observaciones y decisiones', 'Una lista con los nombres de quienes asistirán a la función', 'Un resumen del argumento de la obra para el público', 'La bitácora guarda la evidencia del proceso para poder revisarlo.'),
        ('abc', '{F} ¿Qué problema aparece en el ensayo 1?', 'No se oía la voz al fondo', 'Se repetía una escena en medio de la función', 'Las entradas de los intérpretes eran confusas', 'La bitácora dice que la voz no se oía al fondo; la repetición y las entradas se atienden después.'),
        ('abc', '{F} ¿Qué cambio hicieron en el ensayo 2?', 'Subieron la proyección y recortaron una escena repetida', 'Cambiaron de lugar el ensayo', 'Quitaron las entradas del final', 'El ensayo 2 registra mayor proyección y un recorte de la escena repetida.'),
        ('abc', '{F} ¿Qué evidencia respalda que el proceso mejoró la claridad de la obra?', 'Dos compañeros dijeron que ahora se entendía el conflicto', 'Los intérpretes dijeron que estaban cansados', 'El ensayo 3 fue el último antes de la función', 'El comentario del público de ensayo muestra un efecto del cambio.'),
        ('abc', '¿Por qué se evalúa también el proceso?', 'Porque muestra cómo el equipo tomó decisiones y qué aprendió', 'Porque el resultado final no se puede evaluar si no se conocen los ensayos', 'Porque así se evita dar retroalimentación', 'El proceso aporta evidencia de aprendizaje que el resultado no siempre muestra.'),
        ('abc', 'En una autoevaluación, ¿qué conviene hacer?', 'Reconocer con honestidad qué funcionó y qué no, citando la bitácora', 'Decir que todo salió perfecto para no desanimar al grupo', 'Culpar a quien tuvo menos tiempo para ensayar', 'La autoevaluación se apoya en evidencia y busca mejorar, no culpar.'),
        ('=', '{F} ¿Cuántos minutos se redujo la duración de la escena entre el ensayo 1 y el ensayo 3?', '12-8', 'Se resta la duración final a la inicial.', ' minutos'),
        ('abc', 'Quieres dar retroalimentación a un par. ¿Cuál formato es más útil?', 'Dos logros con evidencia y una sugerencia concreta', 'Una nota final sin explicaciones', 'Una lista de todos los errores que se vieron durante la función completa', 'El formato señala lo que funcionó y una mejora posible con razones.'),
        ('abc', 'Un grupo dice: «Nuestro resultado fue excelente, no necesitamos mirar el proceso». ¿Qué se pierde?', 'La oportunidad de saber qué decisiones lo hicieron funcionar y repetirlas', 'La nota que da la pauta de criterios y el puntaje de cada integrante del equipo', 'La opinión del público de la función final', 'Sin revisar el proceso no se sabe qué conservar en próximas obras.'),
        ('abc', 'Al evaluar el trabajo en equipo de un par, ¿qué se observa?', 'Si se escucharon, repartieron roles y cuidaron la seguridad y el consentimiento', 'Quién habló más fuerte en los ensayos y quién propuso más ideas en cada una de las sesiones', 'Quién llegó primero a cada ensayo', 'El trabajo en equipo se evalúa por escucha, roles y cuidado de las personas.'),
        ('abc', 'Un comentario de un compañero hiere a una persona del grupo. ¿Qué corresponde?', 'Detener la revisión y avisar a una persona adulta de confianza', 'Seguir con la revisión para terminar a tiempo', 'Defender a la persona con otro comentario hiriente hacia quien la criticó primero', 'Cuando una crítica hiere se detiene y se pide ayuda a una persona adulta.'),
        ('=', 'Un grupo hizo 3 ensayos y registró 4 observaciones en cada uno. De ellas, 5 llevaron a un cambio. ¿Cuántas observaciones no llevaron a cambios?', '3*4-5', 'Se calcula el total de observaciones y se restan las que generaron cambios.', ' observaciones'),
        ('abc', 'Dos grupos presentan escenas igual de buenas, pero solo uno llevó bitácora. ¿Qué ventaja tiene ese grupo al evaluar?', 'Puede mostrar con evidencia qué decisiones tomó y qué efecto tuvieron', 'Puede asegurar que obtendrá una nota más alta', 'No tiene ventaja, porque la bitácora no sirve para evaluar y solo ocupa tiempo de ensayo', 'La bitácora es evidencia del proceso y facilita revisar y explicar.'),
    ],
    ctx=('ab', 'Debes evaluar la obra de un compañero que te cae mal. ¿Qué haces?', 'Me centro en la obra, cito evidencia y escribo con respeto', 'Aprovecho para marcar todos sus errores', 'La evaluación se basa en la obra y no en las simpatías.'),
    sc=[
        ("En Teatro: ¿para qué sirve una bitácora?", "Para registrar ensayos, observaciones y decisiones como evidencia del proceso", "Permite revisar cómo se llegó a la obra."),
        ("¿Qué formato de retroalimentación se usa para un par?", "Dos logros con evidencia y una sugerencia concreta", "Es un formato respetuoso y útil para quien lo recibe."),
        ("Si una crítica hiere a una persona, ¿qué se hace?", "Se detiene y se avisa a una persona adulta de confianza", "Evitar el daño es lo primero."),
    ],
    op=("Imagina un grupo que ensaya una escena. Inventa una bitácora de tres ensayos (qué se hizo, qué se observó, qué se decidió). Luego escribe una autoevaluación de cuatro oraciones que cite esa bitácora y una retroalimentación para otro grupo con dos logros y una sugerencia.",
        "Ensayo 1: no se entendía el inicio; decidimos acortarlo. Ensayo 2: acortamos el inicio y se entendió, pero las entradas fueron lentas; decidimos ensayarlas. Ensayo 3: ensayamos las entradas y quedaron más rápidas; decidimos mantener ese orden. Autoevaluación: funcionó acortar el inicio; falló al principio el ritmo. Para otro grupo: logros, voz clara y objetos bien usados; sugerencia, ensayar los cambios de escena.",
        ["bitácora con tres ensayos", "autoevaluación honesta con evidencia", "dos logros y una sugerencia", "lenguaje respetuoso"],
        ["bitácora, autoevaluación y retroalimentación"],
        ["solo evaluar el resultado", "comentarios generales sin evidencia"],
        "Pregunta: «¿en qué ensayo se ve eso?». Debe señalar la entrada de la bitácora."),
    reinforce="Anota en una bitácora imaginaria dos ensayos de una escena de seis líneas con lo que se hizo y se observó.",
    extend="Explica por qué dos grupos con el mismo resultado pueden haber tenido procesos muy distintos y por qué eso importa.",
)
