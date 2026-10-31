"""Cuaderno del estudiante de 7.º básico Artes Visuales: AR07 OA 05 (interpretar relaciones entre el propósito expresivo del trabajo personal y de pares, y el uso del lenguaje visual)."""
from __future__ import annotations

from student_content_ar7_a import lesson, m, task, w
from student_lessons import arith, ex

OA5 = "AR07 OA 05"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Una hoja, lápiz y lápices de colores. Los trabajos de estudiantes que se analizan son de ejemplo y están descritos en esta clase.",
    "Aprenderé a reconocer el propósito expresivo que declara quien crea y a distinguirlo de lo que yo supongo al mirar. Sirve para interpretar los trabajos de mis compañeros y los míos con respeto.",
    ["Sé describir lo que veo antes de interpretar.", "Sé que una intención dice qué, cómo y por qué."],
    [
        "El propósito expresivo es lo que quien crea quiere comunicar con su trabajo: una emoción, una idea, un recuerdo, una crítica. Cuando la autora o el autor lo declara, por ejemplo en una ficha o en una conversación, es la primera fuente para interpretar su obra. No puedo adivinarlo solo mirando: puedo suponer, pero debo comprobar con quien creó. Mi lectura es una interpretación; el propósito declarado es lo que la persona dijo.",
        "Declarar el propósito se hace con una frase corta: «Quise mostrar la prisa de la mañana con líneas diagonales y colores fuertes». Una declaración clara tiene qué se quiere comunicar y alguna pista del cómo. Después puedo comparar lo que se ve con lo que se declaró: ¿coinciden?, ¿qué decisión visual sostiene el propósito?, ¿qué parte no se entiende todavía? Que no coincida no significa que el trabajo esté mal: puede significar que falta ajustar una decisión.",
        "Al hablar de trabajos de pares uso tres pasos: pregunto el propósito, describo lo que veo y relaciono ambas cosas. Si la autora no está, uso la ficha o lo anoto como pregunta. Nunca digo «lo que quiso hacer fue…» como si lo supiera. Digo «tal vez quería…, ¿es así?». Así respeto su voz y practico interpretar con evidencia.",
    ],
    [("propósito expresivo", "lo que quien crea quiere comunicar con su trabajo"), ("declarar", "decir con claridad el propósito"), ("interpretación", "lectura propia de lo que se ve"), ("coincidir", "estar de acuerdo lo que se ve con lo que se dijo"), ("par", "compañero o compañera que también crea")],
    [
        w("Comparar propósito y lectura", "Camila declara: «Quise mostrar la soledad de una plaza vacía». Su dibujo tiene una banca pequeña y mucho espacio blanco. ¿Coinciden?", ["La banca pequeña muestra pocos elementos.", "El espacio blanco enfatiza el vacío.", "Ambos apoyan la soledad."], "Sí, coinciden: el espacio blanco y la banca pequeña sostienen la soledad"),
        w("Distinguir suposición y declaración", "Miras la obra de un compañero y piensas «quería hacer reír». Él no ha dicho nada. ¿Qué haces?", ["Es una suposición.", "Pregunto antes de afirmar.", "Uso «tal vez quería… ¿es así?»."], "Preguntarle, usando «tal vez quería hacer reír, ¿es así?»"),
    ],
    [
        m("Afirmar el propósito de un compañero sin preguntarle.", "Se confunde la suposición propia con lo que él quiso hacer.", "Pregunta y usa «tal vez quería…»."),
        m("Pensar que si lo que veo no coincide con lo declarado, el trabajo está mal.", "Puede faltar ajustar una decisión visual.", "Señala qué decisión podría acercar el trabajo al propósito."),
    ],
    [
        ex("El propósito expresivo es: A. lo que quien crea quiere comunicar B. el material que usó.", "A", "El propósito es la idea o emoción que se quiere transmitir."),
        ex("Si una autora declara su propósito en la ficha, ¿es la primera fuente para interpretar su obra? ¿Sí o no?", "Sí", "Dice lo que ella quería comunicar."),
        ex("«Tal vez quería mostrar prisa, ¿es así?» ¿Es una afirmación o una pregunta respetuosa?", "Una pregunta respetuosa", "Propone una lectura y pide comprobarla."),
    ],
    [
        ex("Tomás declara: «Quise mostrar el calor del verano». Su trabajo usa amarillos y naranjas con círculos grandes. ¿Coinciden lo declarado y lo visto?", "Sí", "Los tonos cálidos y los círculos grandes sostienen el calor."),
        ex("Valentina declara: «Quise mostrar el silencio de la noche». Su trabajo usa un fondo oscuro, rojos fuertes y líneas quebradas. ¿Qué decisión visual no coincide con el propósito? A. Las líneas quebradas con rojo fuerte, que dan tensión B. El fondo oscuro, que da sensación de noche", "A", "Las líneas quebradas y el rojo fuerte no sugieren silencio."),
        ex("¿Cuál es una declaración de propósito más completa? A. «Quise mostrar el cansancio con figuras inclinadas y grises» B. «Quise hacer un dibujo de personas»", "A", "Dice qué comunicar y pistas del cómo para comparar con lo visto."),
    ],
    [
        ex("Ignacio escribe: «Quiero mostrar la fuerza del mar con líneas largas y azules oscuros». Una compañera describe: «Veo líneas largas curvas y azul oscuro». ¿Qué palabra de su declaración confirma que coincide: «líneas largas» o «mar»?", "Líneas largas", "Es un dato visible que ambas descripciones comparten."),
        arith("Un curso tiene 30 estudiantes y 12 ya declararon su propósito. ¿Cuántos faltan?", "30-12", "Se resta lo declarado del total."),
        ex("Un estudiante declara «Quise mostrar alegría» pero su trabajo es todo gris y con líneas verticales muy rígidas. ¿Qué cambio lo acerca más a su propósito? A. Reemplazar el gris por amarillos y naranjas B. Hacer las líneas todavía más rígidas", "A", "Los colores vivos acercan la lectura a la alegría."),
    ],
    [
        ex("Dos estudiantes quieren mostrar tranquilidad. La primera usa curvas suaves y azules claros; el segundo usa diagonales rojas. ¿Cuál tiene más coherencia entre propósito y lenguaje visual?", "La primera", "Las curvas y azules claros sostienen tranquilidad."),
        ex("Alguien dice «el trabajo de Sofía es sobre su familia» sin haberle preguntado. ¿Qué falta?", "Preguntarle a Sofía o leer su ficha", "Es una suposición, no un propósito declarado."),
    ],
    [
        ex("Hugo declara: «Quise mostrar la espera, con una silla vacía pequeña en el centro». Un compañero afirma que el dibujo muestra «un mueble». ¿Cuál lectura se acerca más al propósito declarado: «espera» o «mueble»?", "Espera", "Coincide con lo que el autor declaró."),
        ex("Una declaración dice: «Quise hacer algo bonito». ¿Es una buena declaración de propósito? A. No, porque no dice qué quiere comunicar ni cómo B. Sí, porque es breve.", "A", "«Bonito» no dice qué comunicar."),
    ],
    ex("Trabajo de ejemplo: un autorretrato hecho con formas geométricas sin rostro, en tonos azules. La autora declara: «Quise mostrar que a veces no sé cómo me siento». ¿Qué decisión visual sostiene mejor su propósito? A. Un rostro sin rasgos ni expresión B. Un rostro sonriendo con ojos grandes.", "A", "La falta de rasgos refleja no saber cómo se siente."),
    [
        ex("En Artes Visuales, ¿qué es el propósito expresivo?", "Lo que quien crea quiere comunicar", "Puede ser una emoción, idea o crítica."),
        ex("Verdadero o falso: puedo afirmar el propósito de un compañero sin preguntarle.", "Falso", "Debo preguntar o leer su ficha."),
        ex("¿Qué frase respetuosa uso para proponer una lectura?", "«Tal vez quería…, ¿es así?»", "Reconoce que es una suposición."),
    ],
    task(
        "Elige UN trabajo de ejemplo. A) Un dibujo con una banca pequeña y mucho espacio blanco; la autora declara «soledad de una plaza vacía». B) Una pintura de círculos grandes amarillos y naranjas; el autor declara «calor del verano». C) Un trabajo con rojos fuertes y líneas quebradas; la autora declara «silencio de la noche». Escribe qué ves, si coincide con lo declarado y qué decisión cambiarías o mantendrías.",
        "Elegí la C. Veo: rojos fuertes y líneas quebradas. Declarado: silencio. No coincide: los rojos y las líneas quebradas dan tensión. Cambiaría las líneas por curvas suaves y el rojo por azul oscuro. Mantendría el espacio vacío abajo, porque ayuda al silencio.",
        ["describe lo que ve", "compara con el propósito declarado", "propone una decisión que cambiaría o mantendría", "usa un tono respetuoso"],
        ["comparación escrita", "decisión propuesta"],
        ["afirmar el propósito sin declararlo", "criticar sin dar una alternativa"],
        "Destaca la decisión mejor relacionada con el propósito y pregunta cómo lo diría a la autora.",
    ),
    "Escribe en una frase el propósito de uno de tus trabajos y cuéntaselo a una persona de tu casa para ver si lo entiende igual.",
    "Escribe dos declaraciones de propósito para el mismo dibujo y di cuál se entiende mejor por el lenguaje visual.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Una hoja, lápiz, lápices de colores y retazos de papel de colores. Los trabajos de ejemplo están descritos en esta clase.",
    "Aprenderé a relacionar el color, la forma, la composición y el material con el propósito de un trabajo. Sirve para decidir qué recurso usar y para explicar por qué lo elegí.",
    ["Sé reconocer el propósito expresivo.", "Sé que el efecto de un recurso depende del contexto."],
    [
        "El color puede dar sensaciones: los cálidos (rojo, naranja, amarillo) suelen sentirse activos y los fríos (azul, verde) más tranquilos. La saturación marca intensidad: colores muy fuertes llaman la atención y los apagados se sienten sutiles. La forma también comunica: las geométricas (cuadrados, triángulos) dan orden y las orgánicas (curvas libres) dan naturalidad. El efecto nunca es fijo; depende de la composición y del propósito.",
        "La composición es cómo se ordena todo. Un elemento grande y centrado destaca; uno pequeño en una esquina se siente lejano. El espacio vacío puede dar calma o soledad; el espacio lleno, energía o agobio. El material también habla: el papel arrugado da aspereza, la acuarela diluida da suavidad, el cartón da firmeza. Todo se elige según el propósito.",
        "Para relacionar uso la fórmula «propósito, recurso y efecto»: «Mi propósito es mostrar calma, uso azul claro y curvas suaves, el efecto es de tranquilidad». Si un recurso no apoya el propósito, lo cambio. Pruebo una variable a la vez y compruebo con otra persona si la idea se entiende. Así cada decisión tiene una razón y no solo un gusto.",
    ],
    [("color cálido", "rojo, naranja y amarillo, que suelen sentirse activos"), ("color frío", "azul y verde, que suelen sentirse tranquilos"), ("forma orgánica", "forma curva y libre, como las de la naturaleza"), ("forma geométrica", "forma regular, como cuadrado o triángulo"), ("recurso", "decisión del lenguaje visual como color, forma, composición o material")],
    [
        w("Propósito, recurso y efecto", "Quieres mostrar la prisa de una mañana. ¿Qué recursos eliges y qué efecto buscas?", ["Color: rojos y naranjas fuertes, que se sienten activos.", "Forma y composición: diagonales repetidas que dan movimiento.", "Efecto: sensación de apuro."], "Rojos y naranjas fuertes con diagonales repetidas para dar sensación de apuro"),
        w("Detectar el recurso que contradice", "Tu propósito es calma y tu dibujo tiene líneas quebradas negras muy juntas. ¿Qué cambias?", ["Las líneas quebradas dan tensión.", "Cambio a curvas suaves y espacio libre.", "Pruebo con azul claro."], "Cambiar las líneas quebradas por curvas suaves con más espacio libre"),
    ],
    [
        m("Pensar que cada color siempre produce la misma emoción.", "El efecto cambia con el contexto y la composición.", "Explica el efecto en tu trabajo, apoyado en lo que rodea al color."),
        m("Elegir un recurso porque «se ve lindo» sin relacionarlo con el propósito.", "No se sabe qué aporta.", "Usa «propósito, recurso y efecto» para decidir."),
    ],
    [
        ex("Un color cálido es: A. rojo B. azul.", "A", "El rojo es cálido; el azul es frío."),
        ex("Las curvas libres de una hoja pertenecen a formas: ¿geométricas u orgánicas?", "Orgánicas", "Son formas libres como las de la naturaleza."),
        ex("Un elemento pequeño en una esquina de un espacio grande se siente: A. lejano B. protagonista.", "A", "El tamaño y la posición lo alejan."),
    ],
    [
        ex("Quieres mostrar alegría de fiesta. ¿Qué paleta elegirías: amarillo, naranja y rojo vivos o gris y azul oscuro?", "Amarillo, naranja y rojo vivos", "Los cálidos y saturados dan energía festiva."),
        ex("Para dar sensación de orden usas formas: A. geométricas repetidas B. manchas libres sin forma.", "A", "Las formas regulares repetidas se ven ordenadas."),
        ex("Un trabajo tiene mucho espacio vacío y una figura pequeña. ¿Qué sensación puede dar: soledad o fiesta?", "Soledad", "El vacío alrededor aísla a la figura."),
    ],
    [
        arith("Una paleta tiene 3 colores cálidos y 2 fríos. ¿Cuántos colores tiene?", "3+2", "Se suman cálidos y fríos."),
        ex("Propósito: mostrar el peso de una piedra. ¿Qué material ayuda más: cartón grueso y oscuro o papel de seda blanco?", "Cartón grueso y oscuro", "Se siente firme y pesado."),
        ex("Propósito: mostrar movimiento del viento. ¿Qué elige: líneas largas diagonales o cuadrados quietos?", "Líneas largas diagonales", "Las diagonales largas sugieren movimiento."),
    ],
    [
        ex("Dos trabajos con el propósito de calma. El primero usa azul pálido y curvas; el segundo usa rojo fuerte y diagonales. ¿Cuál tiene recursos más coherentes con la calma?", "El primero", "Azul pálido y curvas se sienten tranquilos."),
        ex("Una estudiante dice: «Usé rojo porque el rojo siempre es amor». Su dibujo es una señal de alto. ¿Es sólida su razón?", "No", "El rojo cambia de efecto según el contexto."),
    ],
    [
        ex("Tu propósito es mostrar un recuerdo lejano. ¿Qué decisión de color ayuda más? A. Tonos apagados y poco saturados B. Colores neón muy intensos.", "A", "Lo apagado se siente lejano."),
        ex("Tienes un dibujo con un elemento grande al centro y quieres que se sienta que ese elemento es muy importante. ¿Qué mantienes?", "El tamaño grande y la posición central", "Ambos destacan lo importante."),
    ],
    ex("Propósito: mostrar el desorden de una pieza muy revuelta. Tres opciones. A. Composición con muchos objetos superpuestos en distintas direcciones B. Composición perfectamente simétrica. C. Una sola figura al centro. ¿Cuál lo muestra mejor?", "A", "Las superposiciones y direcciones distintas dan desorden."),
    [
        ex("En Artes Visuales, ¿qué es un color frío?", "Azul y verde", "Suelen sentirse tranquilos."),
        ex("Verdadero o falso: un color siempre significa lo mismo.", "Falso", "Depende del contexto."),
        ex("¿Qué fórmula usas para relacionar recursos?", "Propósito, recurso y efecto", "Une la idea con las decisiones."),
    ],
    task(
        "Elige UN propósito. A) Mostrar la prisa de una mañana. B) Mostrar la calma de un lago. C) Mostrar el desorden de una pieza. Haz un boceto con un color, una forma y una composición que apoyen ese propósito, y escribe la fórmula «propósito, recurso y efecto» para cada uno. Cambia un recurso y anota si el efecto cambió.",
        "Elegí B. Color: azul pálido, efecto de frescura. Forma: curvas largas y suaves, efecto de calma. Composición: horizonte bajo y mucho espacio vacío, efecto de amplitud. Cambié el azul por rojo y el efecto pasó de calma a calor.",
        ["elige color, forma y composición", "escribe propósito, recurso y efecto", "cambia un recurso y compara", "relaciona cada recurso con el propósito"],
        ["boceto", "tabla de propósito, recurso y efecto"],
        ["elegir recursos por gusto", "no comprobar el cambio"],
        "Destaca la relación mejor explicada y pregunta qué otro recurso cambiaría.",
    ),
    "Mira un afiche de tu casa y di qué color, forma y composición usa y qué sensación da.",
    "Elige tres propósitos y para cada uno escribe un recurso de color, uno de forma y uno de composición.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Una hoja y lápiz. Los dos trabajos de estudiantes que se comparan son de ejemplo y están descritos en esta clase.",
    "Aprenderé a comparar las decisiones de dos trabajos con el mismo propósito, observando qué recursos usa cada uno y qué efecto producen. Sirve para aprender de otros sin copiar.",
    ["Sé relacionar propósito, recurso y efecto.", "Sé que dos trabajos pueden decir lo mismo de maneras distintas."],
    [
        "Comparar es mirar dos trabajos juntos para ver en qué se parecen y en qué se diferencian. Dos estudiantes pueden tener el mismo propósito, por ejemplo mostrar la soledad, y tomar decisiones distintas: una usa una figura pequeña y mucho espacio vacío; el otro usa una multitud donde una persona está de espaldas. Ambas pueden funcionar, pero con efectos diferentes.",
        "Para comparar uso una tabla con cuatro filas: propósito, color y forma, composición y material, y efecto. Anoto lo que veo en cada trabajo y marco semejanzas y diferencias. Luego respondo: ¿qué decisión de cada uno apoya mejor el propósito?, ¿qué podría aprender del otro sin copiarlo? Aprender significa tomar una idea, como el uso del espacio vacío, y adaptarla a mi propia obra.",
        "Comparar no es decidir quién es mejor. Es entender cómo cada decisión cambia el efecto. Uso un tono respetuoso: «El trabajo de A usa…, el de B usa…; en A se siente…, en B se siente…». Siempre cito los datos que veo. Si hay una decisión que me llamó la atención, anoto cómo podría probarla yo con mi propio estilo.",
    ],
    [("comparar", "mirar dos cosas juntas para ver semejanzas y diferencias"), ("semejanza", "algo que dos trabajos tienen en común"), ("diferencia", "algo en que dos trabajos no coinciden"), ("adaptar", "tomar una idea y cambiarla para hacerla propia"), ("estilo", "manera personal de hacer las cosas")],
    [
        w("Tabla de comparación", "Trabajo A: una figura pequeña en el extremo de una hoja blanca. Trabajo B: una multitud gris con una persona de espaldas. Ambos quieren mostrar soledad. Compara.", ["Semejanza: ambos usan la soledad como propósito.", "Diferencia en composición: A usa vacío y B usa multitud.", "Efecto: A se siente aislado; B se siente solo entre gente."], "Mismo propósito; A lo logra con el vacío y B con una persona de espaldas entre la multitud"),
        w("Aprender sin copiar", "Te gustó el espacio vacío del trabajo A. ¿Cómo lo adaptas a tu dibujo de una niña que espera el bus?", ["No copio la figura pequeña en la esquina.", "Dejo un espacio grande a un lado de la niña.", "Mantengo mi propia figura y mis colores."], "Dejar un gran espacio vacío junto a mi figura, con mis propios colores"),
    ],
    [
        m("Comparar para decir cuál trabajo es el mejor.", "La comparación sirve para entender las decisiones, no para ordenar a las personas.", "Describe cómo cada decisión cambia el efecto."),
        m("Copiar la decisión del otro trabajo sin adaptarla.", "Se pierde la voz propia.", "Toma la idea y cámbiala con tus recursos."),
    ],
    [
        ex("Comparar es: A. mirar dos trabajos para ver semejanzas y diferencias B. elegir quién gana.", "A", "La comparación explica decisiones."),
        ex("Dos trabajos usan azul. Eso es una: A. semejanza B. diferencia.", "A", "Es algo que tienen en común."),
        ex("¿Cuál es una fila de la tabla de comparación? A. Efecto B. Precio de los materiales.", "A", "Las filas son propósito, color y forma, composición y material, y efecto."),
    ],
    [
        ex("Trabajo A: círculos rojos grandes juntos. Trabajo B: círculos rojos pequeños y separados. Ambos usan círculos rojos. ¿En qué difieren? A. En el tamaño y la separación B. En el color.", "A", "El color es el mismo; cambian el tamaño y la separación."),
        ex("Trabajo A usa una sola figura grande al centro. Trabajo B usa muchas figuras pequeñas en los bordes. ¿Cuál se centra más en un solo protagonista?", "A", "Una figura grande al centro destaca como protagonista."),
        ex("Para mostrar movimiento, A usa líneas diagonales y B usa curvas en espiral. Ambos logran movimiento. ¿Es posible?", "Sí", "Diferentes recursos pueden lograr el mismo propósito."),
    ],
    [
        ex("Trabajo A: paisaje en tonos fríos y vacío. Trabajo B: paisaje en tonos cálidos y lleno de detalles. Ambos quieren mostrar un lugar. ¿Cuál se siente más tranquilo?", "A", "Fríos y vacío transmiten calma."),
        ex("Te gustó cómo el trabajo B usa papel arrugado para mostrar aspereza. ¿Cómo lo adaptas a tu dibujo de una montaña?", "Usando papel arrugado en tu propia montaña", "Tomas la idea del material y la usas en tu obra."),
        arith("En la tabla de comparación anotas 2 semejanzas y 3 diferencias. ¿Cuántos puntos anotaste?", "2+3", "Se suman semejanzas y diferencias."),
    ],
    [
        ex("Dos estudiantes comparan trabajos. Uno dice «el mío es mejor porque usa más colores». La otra dice «el mío usa dos colores y el otro cinco; mi propósito necesita calma». ¿Quién compara mejor?", "La segunda", "Explica el efecto de la decisión y no ordena por cantidad."),
        ex("Un estudiante copia exactamente la composición de un compañero y cambia solo los colores. ¿Aprendió de él o copió?", "Copió", "No adaptó la idea ni la hizo propia."),
    ],
    [
        ex("Trabajo A usa 3 colores y trabajo B usa 5. El propósito de ambos es calma. ¿Cuál puede mostrarlo mejor? A. Cualquiera, depende de cómo usen los colores B. El que tiene más colores.", "A", "La cantidad de colores no determina el efecto."),
        ex("Dos trabajos tienen el mismo propósito, alegría. Uno usa curvas y amarillos; el otro, diagonales y naranjas. ¿Se pueden preferir ambos?", "Sí", "Ambos pueden funcionar con efectos distintos."),
    ],
    ex("Trabajo A: una casa pequeña lejos, en una hoja casi vacía. Trabajo B: una casa grande que ocupa la hoja. Propósito de ambos: mostrar la sensación de hogar. ¿Cuál enfatiza la cercanía?", "B", "La casa grande ocupa la hoja y se siente cercana."),
    [
        ex("¿Para qué sirve comparar trabajos?", "Para entender cómo cada decisión cambia el efecto", "No es para decidir quién gana."),
        ex("Verdadero o falso: aprender de otro trabajo es copiarlo.", "Falso", "Se adapta la idea a la propia obra."),
        ex("¿Qué se cita al comparar?", "Los datos que se ven en cada trabajo", "Así la comparación se puede comprobar."),
    ],
    task(
        "Elige UNA pareja de trabajos de ejemplo. A) Una figura pequeña en el extremo de una hoja blanca frente a una multitud gris con una persona de espaldas; propósito: soledad. B) Un paisaje en tonos fríos y vacío frente a un paisaje cálido y lleno de detalles; propósito: mostrar un lugar. C) Una casa pequeña y lejana en una hoja casi vacía frente a una casa grande que ocupa la hoja; propósito: hogar. Haz la tabla de cuatro filas, escribe una semejanza y una diferencia, y qué idea adaptarías a tu propio dibujo sin copiar.",
        "Elegí la B. Semejanza: ambos muestran un lugar. Diferencia: uno usa tonos fríos y vacío, otro cálidos y mucho detalle. Efecto: el primero se siente tranquilo, el segundo, animado. Adaptaría el vacío del primero en mi dibujo de una playa, con mis propios colores.",
        ["completa la tabla de cuatro filas", "escribe una semejanza y una diferencia", "explica el efecto de cada decisión", "adapta una idea sin copiarla"],
        ["tabla de comparación", "idea adaptada"],
        ["decidir quién es mejor", "copiar sin adaptar"],
        "Destaca la diferencia mejor descrita y pregunta cómo cambiaría su dibujo con esa idea.",
    ),
    "Compara dos objetos de tu casa del mismo tipo (por ejemplo, dos tazas) y di una semejanza y una diferencia visual.",
    "Escribe qué decisión de otro trabajo te llamó la atención y cómo la harías a tu manera.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Una hoja y lápiz. Los trabajos y comentarios de ejemplo están escritos en esta clase.",
    "Aprenderé a ofrecer retroalimentación a un compañero según criterios, con respeto y con datos. Sirve para ayudar a mejorar un trabajo sin imponer mi gusto.",
    ["Sé comparar decisiones entre trabajos.", "Sé relacionar propósito y lenguaje visual."],
    [
        "La retroalimentación es un comentario que ayuda a mejorar un trabajo. Para que sea útil se basa en un criterio, es decir, una pregunta clara sobre el trabajo, como «¿se nota el propósito?» o «¿el color apoya la idea?». No se trata de decir «me gusta» o «no me gusta», sino de explicar qué se ve y cómo se relaciona con el criterio. Un comentario útil es específico, respetuoso y propone una posibilidad.",
        "Una fórmula sencilla tiene tres partes: lo que veo, el criterio y una pregunta o sugerencia. Por ejemplo: «Veo que usas líneas curvas y azul claro (lo que veo). Tu propósito es calma y esas decisiones lo apoyan (criterio). ¿Qué pasaría si dejas más espacio vacío al lado de la figura?» (sugerencia en forma de pregunta). Siempre empiezo por lo que funciona y después sugiero cambios.",
        "Quien recibe el comentario decide si lo usa. Yo no puedo exigirlo ni burlarme. Evito frases como «está feo» o «hazlo como yo». Cuido que el comentario hable del trabajo y no de la persona. Si recibo un comentario, escucho completo, pido un ejemplo si no entiendo y agradezco. Después anoto cuál usaré y por qué.",
    ],
    [("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("criterio", "pregunta clara con que se mira un trabajo"), ("específico", "que dice algo concreto y no general"), ("sugerencia", "idea para probar un cambio"), ("respetuoso", "que cuida a la persona y habla del trabajo")],
    [
        w("Comentar con la fórmula", "Trabajo de ejemplo: una pintura con muchos triángulos rojos y negros quebrados. Propósito declarado: mostrar el ruido de la ciudad. Escribe un comentario.", ["Lo que veo: triángulos rojos y negros quebrados.", "Criterio: ¿se nota el ruido?", "Sugerencia en forma de pregunta."], "«Veo triángulos rojos y negros quebrados que dan sensación de ruido. ¿Qué pasaría si repites algunos más pequeños para sentir más movimiento?»"),
        w("Reconocer un comentario poco útil", "Alguien dice: «No me gusta tu dibujo». ¿Qué le falta?", ["No dice qué se ve.", "No usa un criterio.", "No propone nada."], "Le falta lo que ve, un criterio y una sugerencia"),
    ],
    [
        m("Comentar solo «me gusta» o «está feo».", "No ayuda a mejorar ni dice qué se ve.", "Usa lo que veo, el criterio y una sugerencia."),
        m("Insistir en que el compañero haga mi sugerencia.", "El autor decide qué usar.", "Ofrece la idea y respeta su decisión."),
    ],
    [
        ex("¿Cuál de estos es un criterio? A. «¿Se nota el propósito?» B. «¿Me cae bien la autora?».", "A", "Un criterio es una pregunta sobre el trabajo."),
        ex("¿Un comentario respetuoso habla del trabajo o de la persona?", "Del trabajo", "Así no se juzga a quien lo hizo."),
        ex("¿Cuál es la primera parte de la fórmula de retroalimentación: lo que veo o la sugerencia?", "Lo que veo", "Se parte de un dato."),
    ],
    [
        ex("Elige el comentario más útil: A. «Los azules claros y las curvas dan calma. ¿Qué pasaría si dejas un espacio vacío al lado?» B. «Está bonito».", "A", "La A dice qué se ve, el efecto y una sugerencia."),
        ex("Un amigo dice: «Hazlo como yo lo haría». ¿Es una sugerencia respetuosa?", "No", "Impone en vez de proponer."),
        ex("¿En qué forma conviene ofrecer una sugerencia: pregunta o mandato?", "Pregunta", "«¿Qué pasaría si…?» deja la decisión a quien crea."),
    ],
    [
        ex("Trabajo de ejemplo: un dibujo de una plaza con una figura pequeña y mucho vacío. Propósito: soledad. Criterio: ¿el espacio apoya el propósito? Un comentario adecuado es: A. «El espacio vacío y la figura pequeña apoyan la soledad» B. «Me gusta la plaza».", "A", "Aplica el criterio con datos."),
        ex("Tu compañero recibe tres comentarios y quiere usar solo uno. ¿Está bien? A. Sí, porque decide qué usa B. No, debe usar los tres.", "A", "La decisión es de quien crea."),
        arith("Revisas 4 trabajos y escribes 3 comentarios por trabajo. ¿Cuántos comentarios escribes?", "4*3", "Se multiplican trabajos por comentarios."),
    ],
    [
        ex("Una estudiante comenta: «Tus colores son feos». Reescribe en forma útil. A. «Veo colores muy intensos; tu propósito es calma, ¿qué pasaría si usas tonos más suaves?» B. «Cambia los colores».", "A", "La A usa el criterio y una pregunta."),
        ex("Un compañero comenta y se burla del dibujo. ¿Qué principio se rompió?", "El respeto", "La retroalimentación debe cuidar a la persona."),
    ],
    [
        ex("Recibes el comentario: «No se entiende el centro de la imagen». ¿Qué haces primero? A. Pedir un ejemplo de qué parte no se entiende B. Enojarte.", "A", "Pedir un ejemplo ayuda a entender el comentario."),
        ex("Tu compañera te dice un comentario con datos y una sugerencia. ¿Qué haces para cerrar? A. Agradecer y anotar qué usarás B. Ignorarla.", "A", "Agradecer y anotar muestra que escuchaste."),
    ],
    ex("Trabajo de ejemplo: una escultura de cartón con la forma de un puente. Propósito: unión. Hay una grieta grande en el medio. Escribe el criterio: A. «¿La estructura apoya la idea de unión?» B. «¿Es el cartón más barato?».", "A", "El criterio se relaciona con el propósito."),
    [
        ex("¿Qué tres partes tiene la fórmula de retroalimentación?", "Lo que veo, el criterio y una sugerencia", "Dan un comentario completo."),
        ex("Verdadero o falso: puedo burlarme si el trabajo no me gusta.", "Falso", "Se cuida a la persona."),
        ex("¿Quién decide si usa la sugerencia?", "Quien crea", "La autoría es suya."),
    ],
    task(
        "Elige UN trabajo de ejemplo. A) Una pintura de triángulos rojos y negros quebrados; propósito: ruido de la ciudad. B) Un dibujo de una plaza con una figura pequeña y mucho vacío; propósito: soledad. C) Una escultura de cartón con forma de puente con una grieta en el medio; propósito: unión. Escribe un comentario con las tres partes (lo que veo, criterio, sugerencia en pregunta) y un comentario recibido que no usarías, con la razón.",
        "Elegí la C. Veo: un puente de cartón con una grieta en el medio. Criterio: ¿la estructura apoya la unión? La grieta separa las dos mitades. Sugerencia: ¿Qué pasaría si unes la grieta con una tira de papel? Comentario que no usaría: «Hazlo más alto», porque no aporta a la unión.",
        ["escribe lo que ve", "usa un criterio", "sugiere en forma de pregunta", "justifica un comentario que no usaría"],
        ["comentario de tres partes", "razón sobre un comentario no usado"],
        ["decir «me gusta» o «está feo»", "imponer una sugerencia"],
        "Destaca el comentario más claro y pregunta cómo lo diría si estuviera frente a la autora.",
    ),
    "Practica con una persona de tu casa: dile un comentario con lo que ves, un criterio y una pregunta sobre un objeto decorativo.",
    "Escribe dos criterios nuevos que usarías para comentar un trabajo de un compañero.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA5, 5,
    "Una hoja, lápiz y un trabajo propio o el ejemplo escrito en esta clase.",
    "Aprenderé a revisar mi trabajo con los comentarios que recibí, decidiendo qué cambiar y qué mantener para conservar mi voz propia. Sirve para mejorar sin perder mi idea.",
    ["Sé dar y recibir retroalimentación según un criterio.", "Sé relacionar propósito y recursos."],
    [
        "Revisar es volver a mirar mi trabajo con ojos nuevos. Parto de mi propósito y de los comentarios que recibí. Para cada comentario hago tres preguntas: ¿se refiere a mi propósito?, ¿lo veo en mi trabajo?, ¿un cambio lo mejoraría sin alterar mi idea? Si respondo que sí, lo uso; si no, lo dejo y anoto la razón. Mi voz propia es lo que hace mi trabajo distinto de los demás, y debo protegerla. Si un comentario dice «poco contraste», habla de la diferencia entre zonas claras y oscuras.",
        "Los cambios se planifican y se prueban de a uno. Si cambio el color, no cambio también la composición. Hago una pequeña prueba, la comparo con la versión anterior y anoto el efecto. Si mejora, la conservo; si pierde la idea, vuelvo atrás. Una revisión también puede decidir no cambiar nada si el trabajo ya cumple el propósito.",
        "Al final escribo una nota de revisión: qué comentarios usé, cuáles no y por qué, qué cambié y qué mantuve, y qué efecto tuvo. Esa nota muestra que decidí con razones. También me sirve para la próxima obra: aprendo qué recursos funcionan para mi propósito y cuáles quiero seguir probando.",
    ],
    [("revisar", "volver a mirar el trabajo para decidir qué cambiar"), ("voz propia", "manera personal de comunicar que hace único el trabajo"), ("versión", "estado del trabajo en un momento"), ("nota de revisión", "texto corto con los cambios y las razones"), ("mantener", "decidir no cambiar algo porque ya cumple el propósito")],
    [
        w("Filtrar un comentario", "Tu propósito es calma. Un compañero comenta: «Pon un rojo fuerte para llamar la atención». ¿Lo usas?", ["¿Se refiere a mi propósito? No, apunta a llamar la atención.", "Un rojo fuerte rompería la calma.", "Lo dejo y anoto la razón."], "No lo uso, porque rompería la calma que quiero mostrar"),
        w("Probar un cambio", "Un comentario dice: «Falta espacio vacío junto a la figura». ¿Cómo lo pruebas?", ["Hago una versión nueva con más espacio.", "Comparo con la anterior.", "Anoto el efecto."], "Hacer una versión con más espacio vacío, compararla y anotar el efecto"),
    ],
    [
        m("Cambiar todo según todos los comentarios.", "Se pierde el propósito y la voz propia.", "Filtra con las tres preguntas."),
        m("No cambiar nada y no anotar por qué.", "No muestra que se revisó con razones.", "Anota lo que mantuviste y por qué."),
    ],
    [
        ex("¿Cuál es la primera pregunta para filtrar un comentario: si se refiere a mi propósito o si me gusta?", "Si se refiere a mi propósito", "El propósito guía la revisión."),
        ex("La voz propia es lo que hace al trabajo: A. distinto de los demás B. igual a los demás.", "A", "Es la manera personal de comunicar."),
        ex("Si un cambio pierde mi idea, ¿vuelvo atrás o lo dejo? ¿Qué haces?", "Vuelvo atrás", "Se conserva la idea original."),
    ],
    [
        ex("Cambias a la vez el color y la composición. ¿Puedes saber qué mejoró?", "No", "Al cambiar dos variables juntas no se sabe cuál produjo el efecto."),
        ex("Un comentario dice «Agrega más detalle» pero tu propósito es mostrar vacío. ¿Qué haces? A. No lo uso y anoto la razón B. Lo uso sin pensar.", "A", "Contradice el propósito."),
        ex("En tu nota de revisión, ¿qué debes anotar de un comentario que no usaste? A. La razón por la que no lo usaste B. El nombre de quien lo dijo.", "A", "La nota muestra que decidiste con razones."),
    ],
    [
        ex("Tu propósito es el movimiento. Un comentario dice «las líneas parecen quietas». ¿Qué pruebas: líneas diagonales más largas o más cuadrados?", "Líneas diagonales más largas", "Las diagonales largas dan movimiento."),
        arith("Recibiste 6 comentarios y usaste 2. ¿Cuántos no usaste?", "6-2", "Se restan los usados del total."),
        ex("Tras una prueba, la nueva versión pierde el espacio vacío que era tu idea. ¿Qué haces?", "Vuelves a la versión anterior", "La nueva versión no conserva el propósito."),
    ],
    [
        ex("Dos estudiantes reciben el comentario «poco contraste». Una agrega negro en todo; el otro oscurece solo el fondo y deja su figura clara. ¿Quién conserva su voz?", "El segundo", "Mantiene su figura clara y el protagonismo."),
        ex("Una estudiante revisó, no cambió nada y escribió: «No cambié porque el propósito ya se ve en el vacío». ¿Es una revisión válida?", "Sí", "Decidió con una razón."),
    ],
    [
        ex("Tu nota de revisión dice solo «Cambié cosas». ¿Qué falta? A. Qué cambió, por qué y qué efecto tuvo B. Un título nuevo.", "A", "Una nota necesita razones y efectos."),
        ex("Después de la revisión, comparas dos versiones. La segunda muestra mejor tu propósito. ¿Cuál conservas?", "La segunda", "Cumple mejor con el propósito."),
    ],
    ex("Recibiste tres comentarios: 1) «Aclara el centro». 2) «Pon un color neón». 3) «Agranda la figura». Tu propósito es calma con una figura pequeña. ¿Cuáles usas probablemente? A. Solo el 1 B. Los tres.", "A", "El 2 y el 3 contradicen la calma y la figura pequeña."),
    [
        ex("En Artes Visuales, ¿qué es la voz propia?", "La manera personal de comunicar", "Hace único el trabajo."),
        ex("Verdadero o falso: debo usar todos los comentarios.", "Falso", "Filtro con mi propósito."),
        ex("¿Cuántos cambios pruebo a la vez?", "Uno", "Así veo qué efecto tuvo."),
    ],
    task(
        "Elige UN caso de ejemplo. A) Propósito: calma. Comentarios: «aclara el centro», «pon un color neón», «agranda la figura». B) Propósito: movimiento. Comentarios: «las líneas parecen quietas», «agrega más cuadrados», «usa un tono más oscuro». C) Propósito: soledad. Comentarios: «agrega más gente», «deja más espacio vacío», «usa letras grandes». Filtra cada comentario con las tres preguntas, elige uno para probar y anota qué mantendrías. Escribe tu nota de revisión.",
        "Elegí la C. Uso «deja más espacio vacío», porque apoya la soledad. No uso «agrega más gente», porque contradice la soledad, ni «letras grandes», porque no se refieren al propósito. Mantengo la figura pequeña. Efecto de la prueba: con más vacío la figura se ve más sola.",
        ["filtra cada comentario con razones", "elige un cambio para probar", "anota lo que mantiene", "escribe la nota de revisión con efecto"],
        ["tabla de filtro de comentarios", "nota de revisión"],
        ["usar todos los comentarios", "cambiar varias cosas a la vez"],
        "Destaca el comentario mejor filtrado y pregunta cómo protegió su voz propia.",
    ),
    "Cuenta a una persona de tu casa qué cambiarías en una obra tuya y qué no, con una razón para cada decisión.",
    "Escribe una segunda nota de revisión para el mismo trabajo pero con otro propósito.",
)
