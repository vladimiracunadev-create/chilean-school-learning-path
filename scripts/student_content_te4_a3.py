"""Cuaderno del estudiante, 4.º básico Tecnología: OA 04 (probar y evaluar), clases 1 a 5, y OA 05 (software de presentación), clases 1 a 4.

Las pruebas usan objetos seguros (fichas, papel, cartón, agua en vaso plástico con adulto cerca); nada de fuego, vidrio ni herramientas con filo.
Las pantallas se describen con texto y son ejemplos ficticios; no se nombra ninguna marca. Todas las clases de presentación tienen alternativa en papel.
Simplificación declarada: el OA 05 nombra también hojas de cálculo y gráficos; el plan solo tiene cuatro clases de presentación. La clase 2 enseña
en papel qué es una hoja de cálculo (filas, columnas, celdas con nombre como B3, ordenar datos y gráfico de barras desde la tabla) y la clase 3 usa
un gráfico propio como imagen; el manejo de un programa real de hojas de cálculo (fórmulas, elegir el tipo de gráfico) NO se enseña.
"""
from __future__ import annotations

from student_content_te4_a import reg
from student_lessons import arith

OA4, OA5 = "TE04 OA 04", "TE04 OA 05"

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja y lápiz. Los casos con sus datos están escritos en este cuaderno.",
    use="Aprenderé a definir criterios de funcionamiento, técnicos, ambientales y de seguridad antes de probar un trabajo. Sirve para evaluar con justicia y no por gusto.",
    prior=["Sé escribir criterios comprobables.", "Sé construir un objeto con un plan."],
    explain=[
        "Probar es usar el objeto en una situación controlada para ver si cumple lo que se pidió. Evaluar es juzgar el resultado usando criterios. Los criterios deben definirse antes de probar, para que el resultado no cambie según lo que a cada uno le gusta. Un trabajo se puede evaluar en cuatro tipos de criterios.",
        "Los criterios de funcionamiento dicen si el objeto cumple su tarea: «sostiene 10 fichas». Los criterios técnicos miran cómo está hecho: «las uniones no se despegan», «las medidas son las del plan». Los criterios medioambientales miran el cuidado de los recursos: «usa material reutilizado». Los criterios de seguridad miran si se puede usar sin riesgo: «no tiene puntas ni bordes que corten».",
        "Cada criterio debe poder responderse con sí o no, o con un número. Evita palabras como «bonito» o «bueno». Escribe también el nivel que se espera: «sostiene al menos 10 fichas». Así, quien pruebe el objeto, sea tú, un compañero o un adulto, llegará a la misma conclusión. Probar y evaluar sirve para mejorar, no para castigar.",
    ],
    vocab=[("probar", "usar el objeto en una situación controlada para ver si funciona"), ("evaluar", "juzgar un resultado usando criterios"), ("criterio de funcionamiento", "dice si el objeto cumple su tarea"), ("criterio técnico", "revisa cómo está hecho el objeto"), ("criterio de seguridad", "revisa si se puede usar sin riesgo")],
    worked=[
        ("Clasificar un criterio", "Criterio: «Las uniones no se despegan al levantar el objeto». ¿De funcionamiento, técnico, medioambiental o de seguridad?", ["Habla de cómo está construido.", "No habla de la tarea final ni del ambiente ni de riesgos."], "Técnico"),
        ("Mejorar un criterio", "Un compañero escribió: «El soporte debe ser bueno». Escríbelo como criterio de funcionamiento comprobable.", ["«Bueno» no se puede comprobar.", "Agrego una cantidad y una prueba."], "Sostiene al menos 10 fichas sin inclinarse"),
    ],
    mistakes=[
        ("Definir los criterios después de ver el resultado.", "Se elige el criterio que el trabajo cumple y la evaluación no es justa.", "Escribe los criterios antes de probar."),
        ("Usar solo criterios de funcionamiento.", "No se revisa seguridad, técnica ni ambiente.", "Incluye al menos uno de cada tipo."),
    ],
    R=[
        ("Usar el objeto para ver si cumple lo pedido, ¿es probar o decorar?", "Probar", "Probar es usar el objeto en una situación controlada."),
        ("«No tiene bordes que corten», ¿es un criterio de seguridad o de ambiente?", "De seguridad", "Habla de riesgo al usarlo."),
        ("«Usa cartón reutilizado», ¿es un criterio medioambiental o técnico?", "Medioambiental", "Habla del cuidado de los recursos."),
    ],
    C=[
        ("¿Por qué se definen los criterios antes de probar?", "Para evaluar con justicia y no por gusto", "Así el resultado no cambia según quién prueba."),
        ("¿Por qué «bonito» no sirve como criterio?", "Porque no se puede comprobar", "Cada persona opina distinto."),
        ("«Las medidas son las del plan», ¿qué tipo de criterio es?", "Técnico", "Revisa cómo está hecho."),
    ],
    A=[
        ("Clasifica «Sostiene 10 fichas durante 1 minuto»: ¿funcionamiento o seguridad?", "Funcionamiento", "Dice si cumple su tarea."),
        ("Reescribe como criterio de seguridad comprobable: «El lapicero debe ser seguro».", "No tiene puntas ni bordes que corten", "Se puede revisar mirando y tocando con cuidado."),
        arith("Una pauta tiene 4 criterios y tu trabajo cumple 3. ¿Cuántos no cumple?", "4-3", "Se restan los cumplidos del total."),
    ],
    Z=[
        ("Tomás dice: «Mi pauta solo tiene criterios de funcionamiento, pero con eso basta». ¿Qué tipo de problema puede quedar sin evaluar?", "De seguridad o de ambiente", "Un objeto puede funcionar y aun así tener un riesgo."),
        ("Elena define el criterio después de probar y elige uno que su trabajo cumple. ¿Es una evaluación justa?", "No", "El criterio debió definirse antes."),
    ],
    D=[
        ("Escribe un criterio de funcionamiento, uno técnico, uno medioambiental y uno de seguridad para un porta-lápices.", "Guarda 6 lápices; las uniones no se despegan; usa cartón reutilizado; no tiene puntas", "Un criterio por cada tipo."),
        arith("Una pauta da 2 puntos a cada criterio cumplido. Tu trabajo cumple 3 de 4 criterios. ¿Cuántos puntos obtiene?", "3*2", "Se multiplican los criterios cumplidos por 2 puntos."),
    ],
    ctx=("Se evalúa un soporte de cartón para fichas con una pauta. Define cuatro criterios, uno de cada tipo: funcionamiento, técnico, medioambiental y de seguridad. Escríbelos con un número o una acción comprobable.", "Sostiene 10 fichas; las uniones no se despegan al levantarlo; usa cartón reutilizado; no tiene puntas ni bordes que corten", "Un criterio comprobable de cada tipo."),
    sc=[
        ("En Tecnología: ¿Qué es evaluar?", "Juzgar un resultado usando criterios", "Se hace después de probar."),
        ("¿Cuáles son los cuatro tipos de criterios?", "Funcionamiento, técnicos, medioambientales y de seguridad", "Son los cuatro de la clase."),
        ("¿Cuándo se definen los criterios?", "Antes de probar", "Así la evaluación es justa."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un porta-lápices de cartón para 6 lápices. Objeto 2: un atril de cartón para 3 hojas. Escribe una pauta con cuatro criterios comprobables, uno de cada tipo, y para cada uno escribe cómo lo probarías.",
        "Objeto 1: funcionamiento: guarda 6 lápices (pongo 6 lápices); técnico: las uniones no se despegan (levanto el objeto); medioambiental: usa cartón reutilizado (reviso el material); seguridad: no tiene puntas (reviso las esquinas).",
        ["cuatro criterios de tipos distintos", "cada uno comprobable", "dice cómo se prueba", "los define antes de probar"],
        ["pauta de cuatro criterios con su prueba"],
        ["criterios como «bonito»", "repetir el mismo tipo"],
        "Pregunta: «¿cómo lo comprobaría otra persona?». Si no puede, ayúdale a poner un número o una acción.",
    ),
    reinforce="Elige un objeto de tu casa, como una mochila, y escribe un criterio de seguridad para evaluarlo.",
    extend="Escribe un criterio de cada tipo para evaluar una lonchera.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja y lápiz. Los datos de las pruebas están escritos en el cuaderno. Si pruebas, usa fichas, papel y cartón.",
    use="Aprenderé a aplicar una prueba repetible, que se hace siempre igual. Sirve para que los resultados se puedan comparar y creer.",
    prior=["Sé definir criterios antes de probar.", "Sé medir en centímetros."],
    explain=[
        "Una prueba repetible se hace siempre de la misma manera, así que otra persona podría hacerla y obtener un resultado parecido. Para eso, lo que no quieres comparar debe quedar igual. Si pruebas cuánto aguanta un puente, usa siempre las mismas fichas, la misma distancia entre apoyos y el mismo tiempo. Lo que se mantiene igual se llama constante. Lo que sí cambia es lo que comparas, por ejemplo el material, y se llama variable.",
        "Una prueba tiene cuatro partes: qué se prueba, qué se mide, cómo se hace paso a paso y cuántas veces se repite. Repetir la prueba tres veces ayuda a descubrir si un resultado fue casualidad. Si las tres veces salen casi igual, el resultado es confiable. Si son muy distintas, hay que revisar la prueba.",
        "Además, la prueba debe ser segura. Si usas agua, hazlo con un vaso plástico y una persona adulta cerca, sobre una bandeja. Nunca pruebes con objetos que puedan lastimar. Escribe los pasos para que cualquiera pueda repetir la prueba. Una prueba mal hecha da resultados que no sirven para decidir cómo mejorar.",
    ],
    vocab=[("prueba repetible", "prueba que se hace siempre igual y se puede repetir"), ("variable", "dato que puede cambiar en una prueba"), ("constante", "dato que se mantiene igual durante la prueba"), ("repetición", "cada vez que se hace la misma prueba"), ("confiable", "que se puede creer porque se repite igual")],
    worked=[
        ("Mantener lo mismo", "Pruebas dos puentes: uno de papel y otro de cartón. Pones fichas hasta que se doble 1 cm. ¿Qué debe ser igual en las dos pruebas?", ["Lo que quiero comparar es el material.", "Todo lo demás debe ser igual: tamaño del puente, distancia entre apoyos, tipo de fichas."], "El tamaño, la distancia entre apoyos y el tipo de fichas"),
        ("Repetir tres veces", "Un puente aguantó 8, 8 y 9 fichas en tres intentos. ¿El resultado es confiable?", ["Los tres números son casi iguales.", "Una diferencia de 1 ficha es pequeña."], "Sí, es confiable"),
    ],
    mistakes=[
        ("Cambiar dos cosas a la vez entre prueba y prueba.", "No se sabe cuál causó la diferencia.", "Cambia solo lo que quieres comparar."),
        ("Probar una sola vez y decidir.", "El resultado puede ser casualidad.", "Repite la prueba al menos tres veces."),
    ],
    R=[
        ("Una prueba que se hace siempre igual, ¿es repetible o casual?", "Repetible", "Se puede repetir igual."),
        ("Lo que se mantiene igual en una prueba, ¿es la constante o la variable?", "La constante", "No cambia durante la prueba."),
        ("¿Cuántas veces conviene repetir una prueba: una o tres?", "Tres", "Así se ve si el resultado cambia por casualidad."),
    ],
    C=[
        ("¿Por qué se mantienen iguales el tamaño y las fichas al comparar materiales?", "Para saber que la diferencia viene del material", "Si cambian varias cosas, no se sabe la causa."),
        ("Tres intentos dieron 3 cm, 3 cm y 12 cm de doblez. ¿Es confiable el resultado?", "No", "Un valor es muy distinto de los otros y hay que revisar la prueba."),
        ("¿Por qué una prueba con agua se hace con un adulto cerca y sobre una bandeja?", "Por seguridad y para no mojar el suelo", "El agua se puede derramar."),
    ],
    A=[
        arith("Un puente aguantó 8, 9 y 10 fichas en tres intentos. ¿Cuántas fichas más aguantó en el mejor intento que en el peor?", "10-8", "Se resta el peor resultado del mejor."),
        ("Quieres comparar dos cintas para ver cuál pega mejor. ¿Qué debe cambiar: la cinta o el tamaño del papel?", "La cinta", "Es lo que se quiere comparar; el papel debe ser igual."),
        ("Escribe la primera parte de una prueba: qué se prueba. Caso: un soporte de cartón con 10 fichas.", "Se prueba si el soporte sostiene 10 fichas", "Dice qué se prueba."),
    ],
    Z=[
        ("Mía probó el puente de papel con fichas grandes y el de cartón con fichas pequeñas. ¿Qué error hizo?", "Cambió dos cosas a la vez", "Cambió el material y el tamaño de las fichas."),
        ("Beto probó una vez y dijo «mi soporte es el mejor». ¿Qué le falta a su prueba?", "Repetirla al menos tres veces", "Una sola vez puede ser casualidad."),
    ],
    D=[
        arith("Un soporte aguantó 8, 10 y 12 fichas en tres intentos. ¿Cuántas fichas hay de diferencia entre el mejor y el peor intento?", "12-8", "Se resta el peor resultado del mejor."),
        ("Dos pruebas del mismo soporte: la prueba A dio 8, 8 y 9 fichas; la prueba B dio 4, 9 y 12 fichas. ¿Cuál resultado es más confiable?", "La prueba A", "Sus tres resultados son casi iguales; los de B son muy distintos."),
    ],
    ctx=("Quieres probar si un soporte de cartón aguanta 10 fichas. Escribe una prueba de cuatro partes: qué se prueba, qué se mide, tres pasos y cuántas veces se repite.", "Se prueba si el soporte sostiene 10 fichas. Se mide si se inclina. Pasos: poner el soporte en la mesa; agregar las fichas de a una hasta 10; esperar 1 minuto y mirar. Se repite 3 veces", "Incluye las cuatro partes."),
    sc=[
        ("¿Qué es una prueba repetible?", "Una prueba que se hace siempre igual", "Otra persona puede repetirla."),
        ("¿Se cambia una cosa o varias al comparar?", "Una", "Así se sabe qué causó la diferencia."),
        ("En Tecnología: ¿Por qué se repite la prueba?", "Para saber si el resultado fue casualidad", "Resultados parecidos son confiables."),
    ],
    open_task=(
        "Escoge una prueba. Prueba 1: comparar cuánto aguanta un puente de papel y uno de cartón del mismo tamaño con fichas. Prueba 2: comparar cuánto aguanta una cinta y otra al sostener una pieza de cartón. Escribe la prueba con cuatro partes, indica qué se mantiene igual y qué cambia, y repítela tres veces anotando los resultados.",
        "Prueba 1: se prueba el material; se mide cuántas fichas aguanta hasta doblarse 1 cm; igual: tamaño, apoyos, fichas; cambia: papel o cartón; papel: 3, 4, 3; cartón: 9, 10, 9.",
        ["cuatro partes escritas", "indica qué cambia y qué se mantiene", "repite tres veces", "anota los resultados"],
        ["descripción de la prueba y tabla de resultados"],
        ["cambiar dos cosas a la vez", "probar una sola vez"],
        "Pregunta: «¿qué cambiaste y qué dejaste igual?». Si responde que todo cambió, pídele rehacer la prueba.",
    ),
    reinforce="Prueba tres veces cuántos clips sostiene una pinza de ropa colgada de un borde y anota los resultados.",
    extend="Explica con tus palabras por qué tres intentos son mejores que uno.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja y lápiz. Las tablas de resultados están escritas en el cuaderno.",
    use="Aprenderé a registrar resultados y fallas en una tabla clara. Sirve para ver qué pasó y decidir qué mejorar con datos.",
    prior=["Sé hacer una prueba repetible.", "Sé comparar números."],
    explain=[
        "Un registro es una tabla donde anotas los resultados de la prueba. Tiene columnas para el intento, lo que mediste y lo que observaste. Por ejemplo: intento 1, fichas que aguantó, y si se inclinó o no. Anotas los datos apenas ocurren, no después de memoria. Los números llevan su unidad: fichas, centímetros o minutos.",
        "Una falla es algo que no cumple un criterio. Se registra con una frase corta que dice qué pasó y dónde: «La esquina izquierda se despegó con 7 fichas». No se escribe «quedó mal», porque no se sabe qué ocurrió. Registrar fallas es una buena práctica: sin ellas, no se sabe qué mejorar.",
        "Con la tabla puedes calcular el total, el mayor y el menor. También puedes ver si algún intento se aparta mucho de los otros. Si tres intentos dan 9, 9 y 3, el 3 llama la atención y conviene repetir. Los resultados no se cambian para que se vean mejor; se anotan tal como ocurrieron.",
    ],
    vocab=[("registro", "tabla donde se anotan los resultados"), ("resultado", "dato obtenido en una prueba"), ("falla", "algo que no cumple un criterio"), ("mayor", "el número más grande"), ("menor", "el número más pequeño")],
    worked=[
        ("Leer una tabla", "Tabla: intento 1: 9 fichas; intento 2: 10 fichas; intento 3: 8 fichas. ¿Cuál fue el menor resultado?", ["Miro los tres números: 9, 10, 8.", "El más pequeño es 8."], "8 fichas, en el intento 3"),
        ("Escribir una falla bien", "El soporte se inclinó con 7 fichas hacia la derecha. Escribe la falla.", ["Debo decir qué pasó y dónde o cuándo.", "Incluyo el número de fichas."], "Se inclinó hacia la derecha con 7 fichas"),
    ],
    mistakes=[
        ("Anotar «quedó mal» como falla.", "No dice qué pasó ni dónde.", "Escribe qué ocurrió, dónde y con cuántas fichas."),
        ("Cambiar un resultado para que se vea mejor.", "Los datos dejan de ser verdaderos.", "Anota lo que ocurrió, aunque sea malo."),
    ],
    R=[
        ("La tabla donde se anotan los resultados, ¿es un registro o un plan?", "Un registro", "Reúne los datos de la prueba."),
        ("Algo que no cumple un criterio, ¿es una falla o un logro?", "Una falla", "No cumple lo pedido."),
        ("El número más pequeño de una lista, ¿es el mayor o el menor?", "El menor", "Menor significa el más pequeño."),
    ],
    C=[
        ("¿Por qué se anota un resultado apenas ocurre?", "Para no olvidarlo ni cambiarlo", "La memoria puede fallar."),
        ("¿Cuál es una buena falla escrita? A «quedó mal», B «la esquina izquierda se despegó con 7 fichas».", "B", "B dice qué, dónde y cuándo."),
        ("Resultados: 9, 9 y 3. ¿Qué intento llama la atención?", "El de 3", "Se aparta mucho de los otros."),
    ],
    A=[
        ("Un soporte debía sostener al menos 10 fichas. En tres intentos sostuvo 9, 10 y 8 fichas. ¿En cuántos intentos cumplió el criterio?", "En 1", "Solo el intento con 10 fichas llega a 10."),
        ("Tabla: soporte A aguantó 9, 9, 10 y soporte B aguantó 6, 7, 6. ¿Cuál tuvo el menor resultado en un intento?", "B", "El menor número, 6, está en B."),
        arith("El soporte debía sostener 10 fichas y sostuvo 7. ¿Cuántas fichas menos sostuvo de lo pedido?", "10-7", "Se resta lo logrado de lo pedido."),
    ],
    Z=[
        ("Rita borró un intento malo para que la tabla se vea mejor. ¿Qué problema tiene?", "Los datos ya no son verdaderos", "Se debe anotar lo que ocurrió."),
        ("Tres intentos dieron 6, 6 y 12. ¿Qué conviene hacer antes de concluir?", "Repetir la prueba", "El 12 se aparta mucho y puede ser un error."),
    ],
    D=[
        arith("Tres soportes aguantaron 8, 10 y 6 fichas. ¿Cuántas fichas más aguantó el mayor que el menor?", "10-6", "Se resta el menor del mayor."),
        ("Registra la falla con una frase completa: el soporte se despegó en la base cuando se pusieron 6 fichas.", "La base se despegó con 6 fichas", "Dice qué, dónde y con cuántas fichas."),
    ],
    ctx=("Probaste tres veces un soporte. Intento 1: aguantó 10 fichas. Intento 2: se inclinó con 7 fichas por la esquina derecha. Intento 3: aguantó 9 fichas. Completa un registro con una frase de falla y di cuál fue el mayor resultado.", "Falla: se inclinó por la esquina derecha con 7 fichas en el intento 2. El mayor resultado fue 10 fichas en el intento 1", "Falla bien escrita y mayor correcto."),
    sc=[
        ("En Tecnología: ¿Qué es un registro?", "Una tabla donde se anotan los resultados", "Sirve para decidir con datos."),
        ("¿Se pueden cambiar los resultados para que se vean mejor?", "No", "Los datos deben ser verdaderos."),
        ("¿Qué dice una falla bien escrita?", "Qué pasó y dónde o cuándo", "Así se sabe qué mejorar."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: tres intentos de un soporte de cartón con 10 fichas (resultados: 10, 7, 9). Registro 2: tres intentos de un atril que debe sostener 3 hojas (hojas que sostuvo: 3, 2, 3; en el intento 2 se cayó una hoja). Crea una tabla con intento, resultado y observación, escribe una falla con una frase completa y marca el mayor y el menor resultado.",
        "Registro 1: intento 1: 10; intento 2: 7; intento 3: 9. Falla: se inclinó con 7 fichas. Mayor 10, menor 7.",
        ["tabla con tres intentos", "una falla bien escrita", "mayor y menor correctos", "resultados verdaderos"],
        ["tabla y falla escrita"],
        ["falla como «quedó mal»", "cambiar datos"],
        "Pregunta: «¿qué pasó exactamente y dónde?». Si no puede decirlo, pídele describir con detalles.",
    ),
    reinforce="Anota en una tabla cuántos lápices sostiene tu estuche en tres intentos.",
    extend="Escribe tres fallas de un objeto de tu casa con una frase completa para cada una.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja y lápiz. Los diálogos y datos están escritos en el cuaderno.",
    use="Aprenderé a dialogar con respeto usando la evidencia de las pruebas. Sirve para evaluar mi trabajo y el de otros sin pelear.",
    prior=["Sé registrar resultados y fallas.", "Sé que una opinión no es lo mismo que un dato."],
    explain=[
        "Dialogar sobre un trabajo es conversar para entenderlo y mejorarlo. En el diálogo se distingue la evidencia de la opinión. La evidencia son los datos de la prueba: «sostuvo 7 de 10 fichas». La opinión es lo que cada uno piensa: «a mí me gusta». Para evaluar, se usa la evidencia; las opiniones no deciden si se cumplió un criterio.",
        "Para dialogar bien, empieza por lo que logró el trabajo y luego señala lo que se puede mejorar. Usa frases como «Tu soporte sostuvo 9 fichas; para llegar a 10 podrías ensanchar la base». Habla del trabajo, no de la persona. Escucha sin interrumpir, y si no estás de acuerdo, pide el dato que apoya lo que dicen.",
        "Evalúa tanto tus trabajos como los de otros con la misma pauta. Tu trabajo no es mejor solo por ser tuyo. Al final del diálogo, acuerden una idea de mejora concreta: qué se cambiará, por qué y cómo se comprobará. Así el diálogo termina en una decisión y no en una discusión.",
    ],
    vocab=[("evidencia", "dato de una prueba que apoya una conclusión"), ("opinión", "lo que alguien piensa o siente"), ("dialogar", "conversar para entender y mejorar"), ("idea de mejoramiento", "cambio concreto que se propone"), ("pauta", "lista de criterios para evaluar")],
    worked=[
        ("Distinguir evidencia de opinión", "Dos frases: A «Mi puente sostuvo 8 fichas», B «Mi puente es el más lindo». ¿Cuál es evidencia?", ["A tiene un dato de la prueba.", "B es un gusto."], "A"),
        ("Dar una retroalimentación útil", "El soporte de Teo sostuvo 9 de 10 fichas y se inclinó a la derecha. Escribe una frase que diga un logro y una mejora.", ["Primero el logro con el dato.", "Luego una mejora concreta."], "Tu soporte sostuvo 9 fichas; para llegar a 10 podrías ensanchar la base del lado derecho"),
    ],
    mistakes=[
        ("Decir «tu trabajo está feo».", "Habla de la persona y no entrega evidencia.", "Señala un dato de la prueba y una mejora."),
        ("Defender mi trabajo sin mirar los datos.", "Mi trabajo no es mejor por ser mío.", "Evalúa con la misma pauta que a los demás."),
    ],
    R=[
        ("«Sostuvo 7 de 10 fichas», ¿es evidencia o una opinión?", "Evidencia", "Es un dato de la prueba."),
        ("«Me gusta este color», ¿es evidencia o una opinión?", "Una opinión", "Es un gusto personal."),
        ("¿Se habla del trabajo o de la persona al evaluar?", "Del trabajo", "Así el diálogo es respetuoso."),
    ],
    C=[
        ("¿Por qué las opiniones no deciden si se cumplió un criterio?", "Porque no se pueden comprobar", "La evidencia sí se comprueba."),
        ("¿Cómo conviene empezar una retroalimentación?", "Por lo que logró el trabajo", "Luego se señala lo que se puede mejorar."),
        ("Si no estás de acuerdo con una conclusión, ¿qué pides?", "El dato que la apoya", "Así se conversa con evidencia."),
    ],
    A=[
        ("Elige la frase respetuosa y útil: A «Tu atril quedó malo», B «Tu atril sostuvo 2 hojas; para llegar a 3 podrías hacerlo más ancho».", "B", "B usa un dato y propone una mejora."),
        arith("Un soporte debía sostener 10 fichas y sostuvo 7. Para llegar a la meta, ¿cuántas fichas más debe sostener?", "10-7", "Se resta lo logrado de lo pedido."),
        ("¿Cuál es evidencia? A «el cartón es raro», B «se despegó la esquina en el intento 2».", "B", "B es un hecho observado en una prueba."),
    ],
    Z=[
        ("Marcos dice: «Mi soporte es mejor que el de Lia, porque es mío». ¿Qué le falta a su argumento?", "Evidencia de las pruebas", "Que sea suyo no es un dato."),
        ("Dos estudiantes discuten sin acordar nada. ¿Qué podría ayudar a terminar con una decisión?", "Acordar una mejora concreta y cómo comprobarla", "Un acuerdo concreto convierte la discusión en una decisión."),
    ],
    D=[
        arith("En un equipo, 3 soportes aguantaron 9, 10 y 8 fichas. ¿Cuántas fichas más aguantó el mejor que el peor?", "10-8", "Se resta el peor resultado del mejor."),
        ("Reescribe «Tu atril es malo» como retroalimentación útil, sabiendo que sostuvo 2 de las 3 hojas pedidas.", "Tu atril sostuvo 2 de 3 hojas; para llegar a 3 podrías ensanchar el apoyo", "Incluye un logro con dato y una mejora, sin juzgar a la persona."),
    ],
    ctx=("Lia probó su atril con 3 hojas. Resultado: sostuvo 2 hojas y la tercera se cayó por la derecha. Escribe una frase de retroalimentación para Lia con un logro, una evidencia y una mejora concreta.", "Tu atril sostuvo 2 hojas con firmeza; la tercera se cayó por la derecha; podrías ensanchar el apoyo de ese lado", "Logro, evidencia y mejora."),
    sc=[
        ("En Tecnología: ¿Qué es la evidencia?", "Un dato de una prueba que apoya una conclusión", "Se puede comprobar."),
        ("¿Qué conviene decir primero en una retroalimentación?", "Lo que logró el trabajo", "Después se propone una mejora."),
        ("¿Se evalúa mi trabajo con la misma pauta que el de otros?", "Sí", "Así la evaluación es justa."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: el soporte de cartón de Teo sostuvo 9 de 10 fichas y se inclinó a la derecha. Caso 2: el atril de papel de Ana sostuvo 3 hojas pero se dobló en la base. Escribe un diálogo de cuatro frases: una evidencia, un logro, una mejora y una pregunta que pida un dato.",
        "Caso 1: «Tu soporte sostuvo 9 fichas (evidencia y logro). Se inclinó a la derecha (evidencia). Podrías ensanchar la base de ese lado (mejora). ¿Cuántas veces se inclinó en los tres intentos?»",
        ["menciona un logro", "da una evidencia", "propone una mejora concreta", "hace una pregunta que pide un dato"],
        ["diálogo escrito de cuatro frases"],
        ["opiniones sin datos", "hablar de la persona"],
        "Pregunta: «¿qué dato de la prueba apoya esa frase?». Si no hay, pídele reescribirla.",
    ),
    reinforce="Cuenta a alguien de tu casa un logro y una mejora de un trabajo que hayas hecho, con un dato.",
    extend="Escribe tres frases de retroalimentación para un objeto de tu elección, cada una con un dato y una mejora.",
)

# ------------------------------------------------------------------ OA 04, clase 5
reg(
    OA4, 5,
    materials="Hoja y lápiz. Los datos de las pruebas están escritos en el cuaderno.",
    use="Aprenderé a mejorar una sola variable de mi diseño y a probar de nuevo. Sirve para saber si el cambio realmente ayudó.",
    prior=["Sé hacer pruebas repetibles y registrar resultados.", "Sé dialogar con evidencia."],
    explain=[
        "Mejorar es cambiar algo del diseño para que cumpla mejor los criterios. Si cambias muchas cosas a la vez, no sabrás cuál ayudó. Por eso se cambia una sola variable por vez, que es el dato del diseño que decides modificar, como el ancho de la base o el número de capas de cartón. Todo lo demás queda igual.",
        "El ciclo de mejora tiene cinco pasos: mirar el registro y elegir la falla más importante; pensar una variable que podría corregirla; cambiar solo esa variable; probar de nuevo, con la misma prueba y tres repeticiones; y comparar los resultados nuevos con los anteriores. Si mejoró, se conserva el cambio. Si no, se prueba otro cambio.",
        "Conviene registrar los resultados antes y después. Por ejemplo: antes, la base de 15 cm aguantó 6, 7 y 6 fichas; después, con base de 20 cm, aguantó 10, 10 y 9. Esta comparación con datos es la evidencia de que el cambio ayudó. Un diseño nunca está terminado del todo: siempre se puede mejorar, y cada mejora aprende de la prueba anterior.",
    ],
    vocab=[("mejorar", "cambiar el diseño para que cumpla mejor los criterios"), ("variable", "dato del diseño que se decide cambiar"), ("antes y después", "resultados anteriores y nuevos que se comparan"), ("ciclo de mejora", "pasos repetidos de probar, cambiar y volver a probar"), ("conservar", "mantener un cambio que funcionó")],
    worked=[
        ("Elegir una variable", "Tu soporte se inclinó con 7 fichas. La base mide 15 cm. ¿Qué variable cambias primero?", ["La falla es que se inclina.", "Una base más ancha da más estabilidad.", "Cambio solo el ancho de la base."], "El ancho de la base"),
        ("Comparar antes y después", "Antes: 6, 7 y 6 fichas. Después de ensanchar la base: 10, 10 y 9. ¿Mejoró?", ["Antes el mayor era 7.", "Después el menor es 9.", "Todos los resultados nuevos son mayores."], "Sí, mejoró"),
    ],
    mistakes=[
        ("Cambiar la base, el material y las uniones a la vez.", "No se sabe qué cambio causó la mejora.", "Cambia una sola variable y vuelve a probar."),
        ("Cambiar el diseño y no volver a probar.", "No hay evidencia de que haya mejorado.", "Prueba con la misma prueba y compara con los resultados anteriores."),
    ],
    R=[
        ("Cambiar solo el ancho de la base, ¿es cambiar una variable o varias?", "Una variable", "Solo cambia un dato del diseño."),
        ("Después de cambiar el diseño, ¿se prueba de nuevo?", "Sí", "Así se sabe si mejoró."),
        ("Comparar resultados anteriores y nuevos se llama comparar...", "Antes y después", "Muestra si el cambio ayudó."),
    ],
    C=[
        ("¿Por qué se cambia una sola variable a la vez?", "Para saber cuál cambio ayudó", "Si cambian varias, no se sabe la causa."),
        ("Después de mejorar, ¿con qué prueba se prueba: la misma o una distinta?", "La misma", "Se necesita la misma para comparar."),
        ("Si el cambio no mejoró los resultados, ¿qué se hace?", "Se prueba otro cambio", "Se sigue el ciclo de mejora."),
    ],
    A=[
        arith("Antes, un soporte aguantó 6, 7 y 6 fichas. ¿Cuántas fichas suman los tres intentos?", "6+7+6", "Se suman los tres resultados."),
        arith("Después de ensanchar la base, aguantó 10, 10 y 9 fichas. ¿Cuántas fichas suman los tres intentos?", "10+10+9", "Se suman los tres resultados nuevos."),
        ("Tu atril se cae hacia atrás. ¿Qué variable cambias primero: el ancho del apoyo trasero o el color?", "El ancho del apoyo trasero", "Esa variable puede corregir la falla; el color no."),
    ],
    Z=[
        ("Fer cambió la base y la tapa a la vez, y los resultados mejoraron. ¿Qué no sabe?", "Cuál de los dos cambios ayudó", "Cambió dos variables al mismo tiempo."),
        ("Antes: 8, 8 y 9. Después: 8, 9 y 8. ¿El cambio mejoró de forma clara?", "No", "Los resultados son casi iguales."),
    ],
    D=[
        arith("Antes, el total de fichas sostenidas en tres intentos fue 19. Después fue 29. ¿Cuántas fichas más sostuvo en total?", "29-19", "Se resta el total anterior del total nuevo."),
        ("Con ese cambio (19 antes y 29 después), ¿conservarías el cambio?", "Sí", "Los resultados mejoraron mucho."),
    ],
    ctx=("Tu soporte aguantó 6, 7 y 6 fichas, y debe aguantar 10. Se inclina por la derecha. Escribe la variable que cambiarías, cómo la cambiarías y qué comparación harías después.", "Variable: el ancho de la base. La ensancho hasta 20 cm. Compararé los resultados nuevos con 6, 7 y 6 fichas", "Una sola variable y comparación antes y después."),
    sc=[
        ("¿Cuántas variables se cambian por vez?", "Una", "Así se sabe qué ayudó."),
        ("¿Qué se hace después de cambiar el diseño?", "Se prueba de nuevo", "Con la misma prueba."),
        ("¿Cómo se sabe si el cambio mejoró?", "Comparando los resultados antes y después", "Los datos muestran la diferencia."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un soporte de cartón con base de 15 cm aguantó 6, 7 y 6 fichas, y debe aguantar 10. Caso 2: un atril de cartulina sostuvo 2, 3 y 2 hojas y debe sostener 3. Elige una variable para cambiar, escribe cómo la cambiarías, inventa resultados realistas de la prueba nueva sin cambiar nada más y compara el antes y el después con una frase.",
        "Caso 1: cambio el ancho de la base a 20 cm. Después: 10, 9 y 10. Antes el total fue 19 y después 29; mejoró y conservo el cambio.",
        ["elige una sola variable", "dice cómo la cambia", "anota los resultados antes y después", "concluye con datos"],
        ["texto de mejora y comparación"],
        ["cambiar varias variables", "no comparar con los resultados anteriores"],
        "Pregunta: «¿qué dejaste igual?». Si no sabe, pídele identificar lo que no cambió.",
    ),
    reinforce="Cambia un solo detalle de un objeto de tu casa, como la altura de una torre de bloques, y compara.",
    extend="Escribe dos mejoras posibles para un soporte y explica por qué solo harías una a la vez.",
)

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja y lápiz. Las pantallas son un ejemplo ficticio descrito con palabras; si no hay computador, se dibujan en papel.",
    use="Aprenderé a definir el propósito y la audiencia de una presentación antes de abrir el programa. Sirve para que mi mensaje llegue claro a quien lo ve.",
    prior=["Sé que un software es un programa del computador.", "Sé ordenar ideas en una lista."],
    explain=[
        "Un programa de presentación sirve para mostrar imágenes, diagramas y textos en pantallas llamadas diapositivas. En el ejemplo ficticio de esta clase, a la izquierda hay una columna con las diapositivas pequeñas, al centro la diapositiva que editas y arriba los botones para insertar texto, imágenes o formas. Cada programa real se ve distinto.",
        "Antes de abrirlo, define el propósito, que es para qué presentas: informar, explicar cómo se hace algo o convencer. También define la audiencia, que son las personas que te van a ver: su edad, qué saben del tema y cuánto tiempo tienen. Para niños de primero, usa pocas palabras y dibujos grandes. Para tu curso, puedes usar datos con números.",
        "Escribe una frase que los reúna: «Quiero (propósito) a (audiencia) sobre (tema)». Después revisa si cada idea de tu presentación ayuda a ese propósito. Si una idea no ayuda, no va. Una presentación con un propósito claro es más corta, más ordenada y se entiende mejor. Un mismo tema cambia según quién lo escucha.",
    ],
    vocab=[("diapositiva", "pantalla de una presentación"), ("propósito", "para qué presentas"), ("audiencia", "personas que ven la presentación"), ("programa de presentación", "software para mostrar imágenes, diagramas y textos en diapositivas"), ("tema", "asunto del que trata la presentación")],
    worked=[
        ("Escribir la frase", "Quieres explicar a tu curso cómo cuidar una planta. Escribe la frase de propósito y audiencia.", ["Propósito: explicar.", "Audiencia: tu curso.", "Tema: cuidar una planta."], "Quiero explicar a mi curso cómo cuidar una planta"),
        ("Adaptar a la audiencia", "Presentas a niños de primero. ¿Usas párrafos largos o dibujos grandes con pocas palabras?", ["Los más pequeños leen poco.", "Los dibujos grandes ayudan a entender."], "Dibujos grandes con pocas palabras"),
    ],
    mistakes=[
        ("Abrir el programa sin saber para qué se presenta.", "Se llena de ideas sin orden.", "Escribe primero propósito, audiencia y tema."),
        ("Usar la misma presentación para cualquier audiencia.", "Lo que sirve a un curso puede no servir a niños pequeños.", "Adapta palabras, datos e imágenes a quien ve."),
    ],
    R=[
        ("«Para qué presentas» ¿es el propósito o la audiencia?", "El propósito", "Dice la finalidad de la presentación."),
        ("«Las personas que te ven» ¿es el propósito o la audiencia?", "La audiencia", "Son quienes miran la presentación."),
        ("Cada pantalla de una presentación se llama...", "Diapositiva", "Es el nombre de cada pantalla."),
    ],
    C=[
        ("¿Por qué conviene definir propósito y audiencia antes de abrir el programa?", "Para que las ideas tengan orden y sirvan al mensaje", "Así no se llena de ideas sueltas."),
        ("Si una idea no ayuda al propósito, ¿se incluye?", "No", "Solo van ideas que sirvan al propósito."),
        ("Para niños de primero, ¿qué conviene: pocas palabras y dibujos grandes o muchos números?", "Pocas palabras y dibujos grandes", "Los más pequeños leen poco."),
    ],
    A=[
        ("Quieres convencer a tu curso de reciclar el papel. Escribe la frase «Quiero ... a ... sobre ...».", "Quiero convencer a mi curso sobre reciclar el papel", "Incluye propósito, audiencia y tema."),
        ("Presentas a adultos que tienen 3 minutos. ¿Qué cuidas: ser breve o poner muchos detalles?", "Ser breve", "Hay poco tiempo."),
        arith("Tu presentación tiene 8 ideas, pero 3 no ayudan al propósito. ¿Cuántas ideas se quedan?", "8-3", "Se quitan las ideas que no ayudan."),
    ],
    Z=[
        ("Luz dice: «Mi tema es el reciclaje, así que sirve para todos». ¿Qué cambia entre presentar a niños de primero y a su curso?", "Las palabras, los datos y las imágenes", "Cada audiencia entiende cosas distintas."),
        ("Dos frases: A «Quiero informar a mi curso sobre las abejas», B «Quiero hacer algo sobre las abejas». ¿Cuál es mejor?", "A", "A dice propósito y audiencia."),
    ],
    D=[
        arith("Tienes 12 minutos para presentar y quieres usar 3 minutos en cada diapositiva. ¿Cuántas diapositivas puedes presentar?", "12//3", "Se reparte el tiempo en partes iguales."),
        ("Escribe la frase de una presentación cuyo propósito es explicar, la audiencia son niños de primero y el tema es lavarse las manos.", "Quiero explicar a niños de primero cómo lavarse las manos", "Incluye propósito, audiencia y tema."),
    ],
    ctx=("Debes presentar a tu curso cómo cuidar una planta. Escribe propósito, audiencia, tema y una decisión sobre cómo serán las diapositivas (por ejemplo palabras o imágenes).", "Propósito: explicar. Audiencia: mi curso. Tema: cuidar una planta. Diapositivas: pocas palabras y fotos o dibujos claros", "Cuatro elementos coherentes."),
    sc=[
        ("En Tecnología: ¿Qué es el propósito?", "Para qué presentas", "Puede ser informar, explicar o convencer."),
        ("En Tecnología: ¿Qué es la audiencia?", "Las personas que ven la presentación", "Cambia cómo preparas el mensaje."),
        ("¿Qué frase reúne ambas cosas?", "Quiero (propósito) a (audiencia) sobre (tema)", "Es la frase de la clase."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: explicar a niños de primero cómo lavarse las manos. Caso 2: convencer a tu curso de ahorrar agua. Escribe la frase de propósito y audiencia, dos decisiones sobre las diapositivas (palabras, imágenes, datos) y una idea que no usarías porque no ayuda al propósito.",
        "Caso 1: Quiero explicar a niños de primero cómo lavarse las manos. Decisiones: dibujos grandes y una frase corta por diapositiva. No usaría datos con porcentajes.",
        ["la frase tiene propósito, audiencia y tema", "dos decisiones coherentes con la audiencia", "descarta una idea que no ayuda"],
        ["frase y lista de decisiones"],
        ["frase sin audiencia", "decisiones que no sirven a la audiencia"],
        "Pregunta: «¿esta decisión ayuda a que ese público entienda?». Si no, pídele cambiarla.",
    ),
    reinforce="Piensa cómo explicarías lo mismo a una persona de 5 años y a una de tu edad. ¿Qué cambia?",
    extend="Escribe dos frases de propósito y audiencia para dos temas distintos.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja y lápiz. Las diapositivas se dibujan en papel si no hay computador. Los datos de las tablas están en el cuaderno.",
    use="Aprenderé a organizar una secuencia de diapositivas con una idea en cada una, y a ordenar datos en una tabla de hoja de cálculo para hacer un gráfico simple. Sirve para que la presentación sea ordenada.",
    prior=["Sé definir propósito y audiencia.", "Sé que una diapositiva es una pantalla de la presentación."],
    explain=[
        "Una presentación se organiza en una secuencia de diapositivas con tres partes: una portada con el título y quién presenta; un desarrollo con las ideas principales; y un cierre que resume o invita a actuar. Cada diapositiva tiene una sola idea principal, con un título corto que la nombra.",
        "Para planificar la secuencia, primero escribe las ideas en un esquema en papel, una línea por diapositiva. Luego ordénalas para que cada una prepare a la siguiente. Una buena regla es no pasar de cinco líneas de texto por diapositiva. Si una idea necesita más, se divide en dos diapositivas. Así la audiencia no se cansa y puede seguirla.",
        "Los datos con números se ordenan en una tabla: filas y columnas con encabezados. Un programa de hojas de cálculo muestra una tabla hecha de celdas. Cada celda se nombra con la letra de su columna y el número de su fila: B3 es la columna B, fila 3. En las celdas escribes datos y el programa puede ordenarlos o sumarlos. Con esos datos se dibuja un gráfico de barras, donde cada barra es más alta mientras mayor sea el número, y el gráfico se puede poner en una diapositiva.",
    ],
    vocab=[("portada", "primera diapositiva con el título"), ("desarrollo", "diapositivas con las ideas principales"), ("cierre", "última diapositiva que resume o invita a actuar"), ("tabla", "datos en filas y columnas con encabezados"), ("gráfico de barras", "dibujo donde cada barra representa un número"), ("hoja de cálculo", "programa con una tabla de celdas para ordenar datos y hacer gráficos"), ("celda", "casilla de la tabla, con nombre de columna y fila, como B3")],
    worked=[
        ("Ordenar una secuencia", "Diapositivas: A «Gracias por ver», B «¿Cómo cuidar una planta?», C «Dar luz y agua». Ordénalas.", ["La portada va primero.", "El desarrollo va al medio.", "El cierre va al final."], "B, C, A"),
        ("Leer una tabla de datos", "Tabla de votos: perro 9, gato 6, conejo 3. ¿Qué mascota tiene la barra más alta en un gráfico de barras?", ["La barra más alta tiene el número mayor.", "9 es el mayor."], "Perro"),
        ("Nombrar una celda", "Hoja de cálculo: en la fila 1 están los encabezados A1 «Mascota» y B1 «Votos»; en la fila 2, A2 «perro» y B2 9; en la fila 3, A3 «gato» y B3 6. ¿Dónde está el dato 6?", ["Está en la fila del gato, que es la fila 3.", "Es el dato de votos, que está en la columna B.", "Columna B y fila 3."], "En la celda B3"),
    ],
    mistakes=[
        ("Poner varias ideas en una sola diapositiva.", "La audiencia no sabe qué es lo importante.", "Una idea principal por diapositiva."),
        ("Escribir los datos de una tabla mezclados, sin encabezados.", "No se sabe qué significa cada número.", "Pon encabezados claros en filas y columnas."),
    ],
    R=[
        ("La primera diapositiva con el título, ¿es la portada o el cierre?", "La portada", "Presenta el título y quién presenta."),
        ("¿Cuántas ideas principales lleva una diapositiva?", "Una", "Así se entiende mejor."),
        ("Datos ordenados en filas y columnas, ¿forman una tabla o un cierre?", "Una tabla", "Esa es la definición."),
    ],
    C=[
        ("¿Por qué se escribe un esquema en papel antes de abrir el programa?", "Para ordenar las ideas antes", "Así cada diapositiva tiene su lugar."),
        ("Una diapositiva tiene diez líneas de texto. ¿Qué conviene hacer?", "Dividirla en dos diapositivas", "La regla es no pasar de cinco líneas."),
        ("En Tecnología: ¿qué indica una barra más alta en un gráfico de barras?", "Un número mayor", "La altura representa la cantidad."),
    ],
    A=[
        ("Hoja de cálculo: A1 «Mascota», B1 «Votos»; A2 «perro», B2 9; A3 «gato», B3 6; A4 «conejo», B4 3. ¿Qué dato está en la celda B4?", "3", "B4 es la columna B, fila 4: los votos del conejo."),
        arith("Tabla de votos: perro 9, gato 6, conejo 3. ¿Cuántos votos hay en total?", "9+6+3", "Se suman los tres números."),
        arith("En esa tabla, ¿cuántos votos más tiene el perro que el conejo?", "9-3", "Se resta el menor del mayor."),
    ],
    Z=[
        ("Eli pone en una diapositiva tres ideas distintas. ¿Qué problema tendrá la audiencia?", "No sabrá cuál es la idea importante", "Una diapositiva debe tener una idea principal."),
        ("Una tabla dice «perro 9, gato 6, conejo 3». El gráfico dibujó la barra del gato más alta que la del perro. ¿Qué está mal?", "La barra del perro debía ser la más alta", "El perro tiene el número mayor."),
    ],
    D=[
        ("En la hoja de cálculo con A1 «Mascota», B1 «Votos», A2 «perro», B2 9, A3 «gato», B3 6, A4 «conejo», B4 3, ¿en qué celda está la palabra «gato»?", "A3", "El gato está en la columna A, fila 3."),
        arith("Presentas 6 ideas y quieres una sola idea por diapositiva, con portada y cierre. ¿Cuántas diapositivas necesitas en total?", "6+2", "Son 6 de desarrollo más portada y cierre."),
    ],
    ctx=("Presentarás a tu curso «Cómo cuidar una planta». Ideas: luz, agua, tierra. Escribe la secuencia de diapositivas con portada, una por idea y cierre. Cuenta cuántas son en total.", "Portada: «Cómo cuidar una planta»; luz; agua; tierra; cierre: «A cuidar plantas». Son 5 diapositivas", "Portada, tres ideas y cierre."),
    sc=[
        ("¿Qué tres partes tiene una presentación?", "Portada, desarrollo y cierre", "Es la secuencia de la clase."),
        ("¿Cuántas ideas principales por diapositiva?", "Una", "Facilita la comprensión."),
        ("¿Para qué sirve un gráfico de barras?", "Para comparar números de un vistazo", "La altura muestra cuál es mayor."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: cuidar una planta (ideas: luz, agua, tierra). Tema 2: cuidar los útiles (ideas: ordenar, limpiar, guardar). Dibuja en papel la secuencia de diapositivas con portada, una diapositiva por idea y cierre, con un título corto en cada una. Agrega una tabla de tres datos inventados, escribe en qué celdas de una hoja de cálculo irían (por ejemplo A2 y B2) y marca cuál tendría la barra más alta.",
        "Tema 1: portada: «Cómo cuidar una planta»; luz; agua; tierra; cierre. Tabla: A1 «Lugar», B1 «Plantas»; A2 «luz» y B2 12; A3 «sombra» y B3 8; A4 «patio» y B4 5. La barra más alta es luz (B2).",
        ["portada, desarrollo y cierre", "una idea por diapositiva", "títulos cortos", "tabla con encabezados, celdas bien nombradas y barra más alta"],
        ["dibujo de la secuencia y tabla"],
        ["varias ideas en una diapositiva", "tabla sin encabezados"],
        "Pregunta: «¿qué idea nombra el título de esta diapositiva?». Si hay dos, pídele dividirla.",
    ),
    reinforce="Escribe un esquema de cinco líneas para contar a tu familia cómo fue tu día.",
    extend="Inventa una tabla de cinco datos, por ejemplo mascotas favoritas del curso, y di cuál sería la barra más alta.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja y lápiz. Las situaciones de derechos de imágenes están descritas en el cuaderno.",
    use="Aprenderé a combinar texto con imágenes propias o autorizadas, y a anotar la fuente. Sirve para respetar el trabajo de otras personas y que la diapositiva se entienda.",
    prior=["Sé organizar una secuencia de diapositivas.", "Sé que una imagen puede tener dueño."],
    explain=[
        "Una diapositiva combina texto e imagen. El texto dice la idea en pocas palabras. La imagen la muestra: puede ser un dibujo tuyo, una foto que tú tomaste, un diagrama o un gráfico de barras hecho con tus datos. Un diagrama es un dibujo con cajas y flechas que muestra pasos o partes, como los pasos para regar una planta. La imagen debe ayudar a entender la idea, no solo decorar. Si no ayuda, se saca.",
        "Una imagen tiene autor, que es la persona que la creó. No todas las imágenes de internet se pueden copiar. Una imagen propia es la que tú dibujaste o fotografiaste. Una imagen autorizada es la que su autor permite usar, y se sabe porque lo dice la página donde está o porque te lo dijo una persona adulta que lo confirmó. Si no estás seguro de que se puede usar, no la uses.",
        "Cuando usas una imagen autorizada, anotas la autoría: quién la hizo y de dónde viene, en letra pequeña bajo la imagen o en la última diapositiva. Eso se llama citar la fuente. Nunca pongas fotos de otras personas sin su permiso ni datos personales, como direcciones o teléfonos. La privacidad también se cuida en las presentaciones.",
    ],
    vocab=[("imagen propia", "dibujo o foto que hiciste tú"), ("imagen autorizada", "imagen que su autor permite usar"), ("autor", "persona que creó una obra"), ("citar la fuente", "anotar quién hizo algo y de dónde viene"), ("privacidad", "cuidado de los datos personales")],
    worked=[
        ("Elegir la imagen", "Necesitas una imagen para la diapositiva «Dar agua a la planta». Opciones: A un dibujo que hiciste tú, B una foto de internet sin permiso. ¿Cuál usas?", ["A es propia.", "B no está autorizada.", "Uso la propia."], "A, el dibujo propio"),
        ("Citar la fuente", "Usas una imagen autorizada de una planta hecha por Camila Rojas, de un sitio educativo ficticio. Escribe la autoría.", ["Pongo el nombre del autor.", "Pongo de dónde viene la imagen."], "Imagen de Camila Rojas, sitio educativo"),
    ],
    mistakes=[
        ("Copiar cualquier imagen de internet.", "Puede tener dueño que no permite usarla.", "Usa imágenes propias o autorizadas y anota la fuente."),
        ("Poner una foto de un compañero sin avisarle.", "No se respeta su privacidad.", "Pide permiso antes de mostrar la foto de alguien."),
    ],
    R=[
        ("Un dibujo que hiciste tú, ¿es una imagen propia o una autorizada?", "Propia", "Tú eres su autor."),
        ("La persona que creó una imagen, ¿es el autor o la audiencia?", "El autor", "Es quien la creó."),
        ("Anotar quién hizo una imagen y de dónde viene se llama...", "Citar la fuente", "Así se reconoce el trabajo."),
    ],
    C=[
        ("¿Por qué no se pueden copiar todas las imágenes de internet?", "Porque tienen autor y pueden no estar autorizadas", "Se debe respetar su trabajo."),
        ("¿Qué haces si no estás seguro de que una imagen se puede usar?", "No la usas", "Es mejor no arriesgarse."),
        ("Quieres mostrar el orden de tres pasos para regar una planta: 1 poner agua en un vaso, 2 verterla despacio, 3 secar el plato. ¿Qué muestra mejor ese orden: un diagrama con cajas y flechas o una foto de la planta?", "Un diagrama con cajas y flechas", "Las flechas indican qué paso va primero."),
    ],
    A=[
        ("Una compañera sale en tu foto. ¿Qué haces antes de ponerla en la presentación?", "Pedirle permiso", "Se cuida su privacidad."),
        arith("Tu presentación tiene 6 diapositivas y 4 llevan imágenes propias. ¿Cuántas no llevan imágenes propias?", "6-4", "Se restan las que sí las llevan del total."),
        ("Tienes un gráfico de barras que hiciste con tus datos. ¿Es una imagen propia o autorizada?", "Propia", "Lo hiciste tú."),
    ],
    Z=[
        ("Saúl pone una imagen sin anotar quién la hizo. ¿Qué parte de buenas prácticas olvidó?", "Citar la fuente", "Debe reconocer al autor."),
        ("Una diapositiva tiene una imagen muy bonita que no tiene relación con la idea. ¿Qué conviene hacer?", "Sacarla o cambiarla", "La imagen debe ayudar a entender la idea."),
    ],
    D=[
        ("En una presentación hay 3 imágenes propias y 2 autorizadas. ¿Cuántas fuentes de imágenes debes citar con autor y origen?", "2", "Solo las autorizadas llevan cita de autor; las propias son tuyas."),
        ("Una foto tiene la dirección de una casa visible. ¿La usarías en una presentación a tu curso?", "No", "Los datos personales como la dirección no se muestran."),
    ],
    ctx=("En tu presentación «Cómo cuidar una planta» quieres una imagen para la diapositiva «Dar agua». Tienes un dibujo tuyo y una foto que encontraste sin saber si se puede usar. Escribe qué eliges y qué escribirías para citar la fuente si fuera autorizada.", "Elijo mi dibujo propio. Si la foto fuera autorizada, escribiría el nombre del autor y de dónde viene", "Elige la propia y conoce cómo citar."),
    sc=[
        ("¿Qué imágenes puedes usar?", "Propias o autorizadas", "Respetan el trabajo del autor."),
        ("¿Qué se anota al usar una imagen autorizada?", "El autor y de dónde viene", "Se llama citar la fuente."),
        ("¿Se pueden mostrar datos personales en una presentación?", "No", "La privacidad se cuida."),
    ],
    open_task=(
        "Escoge una diapositiva. Diapositiva 1: «Dar agua a la planta». Diapositiva 2: «Guardar los útiles en su lugar». Escribe el texto en una frase de hasta 8 palabras, describe una imagen propia que pondrías (dibujo o foto), explica cómo ayuda a entender la idea y escribe cómo citarías una imagen autorizada ficticia.",
        "Diapositiva 1: texto: «Regar con poca agua cada día». Imagen: dibujo mío de un vaso regando. Ayuda: muestra cuánta agua. Cita: «Imagen de Ana Pérez, sitio educativo».",
        ["texto breve", "imagen propia o autorizada", "explica cómo ayuda", "cita la fuente de forma correcta"],
        ["diapositiva dibujada con cita"],
        ["imagen sin permiso", "imagen que no tiene relación con la idea"],
        "Pregunta: «¿quién hizo esa imagen y puedes usarla?». Si no sabe, pídele cambiarla por una propia.",
    ),
    reinforce="Dibuja una imagen simple para ilustrar una idea de tu tarea y escribe quién es el autor.",
    extend="Escribe tres reglas para usar imágenes en una presentación.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja y lápiz. Las diapositivas ejemplo están escritas en el cuaderno. Si presentas, hazlo frente a una persona de tu casa.",
    use="Aprenderé a presentar mi trabajo y a revisar si se lee bien: tamaño de letra, contraste y cantidad de texto. Sirve para que todos puedan leer la presentación.",
    prior=["Sé organizar diapositivas y combinar texto e imagen.", "Sé citar una fuente."],
    explain=[
        "La legibilidad es qué tan fácil es leer algo. Una diapositiva legible tiene letra grande, buen contraste y poco texto. El tamaño de letra debe poder leerse desde el fondo de la sala: los títulos, de 32 o más, y el texto, de 24 o más, aunque esos números son una guía. El contraste es la diferencia entre el color de la letra y el del fondo.",
        "Hay buen contraste con letra negra sobre fondo blanco o amarillo muy claro. Hay mal contraste con letra amarilla sobre fondo blanco o letra roja sobre fondo naranja. También ayuda no usar más de dos tipos de letra y no escribir todo en mayúsculas. Revisa que el texto no esté tapado por una imagen.",
        "Al presentar, mira a tu audiencia y no a la pantalla. Habla con tus palabras sobre la idea de cada diapositiva, sin leer todo lo escrito. Habla con voz clara y en el tiempo que tienes. Al terminar, pide a quien te escuchó un logro y una mejora, y ajusta la presentación. La presentación nunca incluye datos personales de otras personas.",
    ],
    vocab=[("legibilidad", "qué tan fácil es leer algo"), ("contraste", "diferencia entre el color de la letra y el del fondo"), ("tamaño de letra", "qué tan grande se ve el texto"), ("mayúsculas", "letras grandes como A, B, C"), ("retroalimentación", "opinión con un logro y una mejora")],
    worked=[
        ("Revisar el contraste", "Diapositiva A: letra negra sobre fondo blanco. Diapositiva B: letra amarilla sobre fondo blanco. ¿Cuál se lee mejor?", ["Negro sobre blanco se distingue mucho.", "Amarillo sobre blanco se ve poco."], "A"),
        ("Revisar la cantidad de texto", "Una diapositiva tiene 9 líneas de texto en letra pequeña. ¿Qué haces?", ["Hay demasiado texto.", "La divido en dos y agrando la letra."], "Dividirla en dos y agrandar la letra"),
    ],
    mistakes=[
        ("Usar letra amarilla sobre fondo blanco.", "Se distingue muy poco y no se lee.", "Usa colores con mucho contraste, como negro sobre blanco."),
        ("Leer toda la diapositiva en voz alta sin mirar a la audiencia.", "La audiencia pierde la atención.", "Mira a la audiencia y explica con tus palabras."),
    ],
    R=[
        ("Letra negra sobre fondo blanco, ¿tiene buen o mal contraste?", "Buen contraste", "Se distingue muy bien."),
        ("Letra amarilla sobre fondo blanco, ¿tiene buen o mal contraste?", "Mal contraste", "Se distingue muy poco."),
        ("¿Se lee mejor con letra grande o pequeña?", "Grande", "Se puede leer desde lejos."),
    ],
    C=[
        ("¿Por qué conviene poco texto por diapositiva?", "Para que se pueda leer rápido y seguir lo que dices", "Mucho texto cansa."),
        ("Mientras presentas, ¿miras a la audiencia o solo a la pantalla?", "A la audiencia", "Así la conectas con lo que dices."),
        ("¿Qué revisas si una imagen tapa parte del texto?", "Mover la imagen para que no tape", "El texto debe verse completo."),
    ],
    A=[
        ("Elige el mejor par: A letra blanca sobre fondo amarillo claro, B letra negra sobre fondo azul oscuro, C letra negra sobre fondo blanco.", "C", "Es el que tiene mayor contraste."),
        arith("Una diapositiva tiene 10 líneas de texto. Si la divides en dos con la misma cantidad cada una, ¿cuántas líneas tendrá cada una?", "10//2", "Se reparte el texto en dos partes iguales."),
        ("Un título está en mayúsculas en toda la diapositiva. ¿Mejora o empeora la lectura?", "Empeora", "Muchas mayúsculas cansan la lectura."),
    ],
    Z=[
        ("Dani dice: «Pongo mucho texto para que no se me olvide qué decir». ¿Qué conviene hacer en cambio?", "Usar pocas palabras y explicar con sus propias palabras", "Mucho texto se lee en lugar de explicar."),
        ("Una diapositiva tiene letra de 12 y la presentación es para una sala grande. ¿Se lee bien?", "No", "La letra es muy pequeña."),
    ],
    D=[
        arith("Presentas 5 diapositivas y tienes 10 minutos. Si usas el mismo tiempo en cada una, ¿cuántos minutos son para cada una?", "10//5", "Se reparte el tiempo en partes iguales."),
        ("Escribe una retroalimentación de dos frases para una presentación: un logro y una mejora, ambos sobre legibilidad.", "El contraste de las diapositivas se lee muy bien; podrías agrandar la letra de la diapositiva 3", "Un logro y una mejora con datos."),
    ],
    ctx=("Revisas tu diapositiva «Dar agua»: letra amarilla sobre fondo blanco, 8 líneas de texto y una imagen que tapa dos líneas. Escribe tres cambios que harías para mejorar la legibilidad.", "Cambiar a letra negra sobre blanco; reducir o dividir el texto; mover la imagen para que no tape", "Cambia contraste, cantidad de texto y posición."),
    sc=[
        ("En Tecnología: ¿Qué es el contraste?", "La diferencia entre el color de la letra y el del fondo", "Un buen contraste se lee mejor."),
        ("¿Cuánto texto es mejor: poco o mucho?", "Poco", "Se lee rápido."),
        ("¿Qué haces al presentar: lees todo o explicas con tus palabras?", "Explicas con tus palabras", "Así la audiencia entiende mejor."),
    ],
    open_task=(
        "Escoge una diapositiva de ejemplo. Diapositiva 1: título «CÓMO REGAR» en mayúsculas, letra amarilla de tamaño 14 sobre fondo blanco, 9 líneas de texto. Diapositiva 2: título «Guardar los útiles», letra negra de tamaño 28 sobre fondo blanco, 3 líneas y una imagen que tapa una línea. Revisa la legibilidad con una lista de cuatro puntos (tamaño, contraste, cantidad de texto, imagen) y escribe una mejora para cada punto. Presenta una diapositiva a una persona de tu casa y anota una retroalimentación.",
        "Diapositiva 1: tamaño: agrandar la letra; contraste: cambiar a negro; cantidad: dividir en dos; imagen: no hay. Retroalimentación: «se entiende; podrías hablar más despacio».",
        ["revisa los cuatro puntos", "una mejora para cada uno", "presenta frente a una persona", "anota una retroalimentación"],
        ["lista de revisión y nota de retroalimentación"],
        ["no revisar el contraste", "leer toda la diapositiva"],
        "Pregunta: «¿lo podría leer alguien al fondo de la sala?». Si no, pídele cambiar tamaño o contraste.",
    ),
    reinforce="Mira un afiche o cartel de tu casa y di si su letra tiene buen contraste con el fondo.",
    extend="Prepara una presentación de un minuto con dos diapositivas y practica hablando sin leer.",
)
