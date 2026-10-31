"""Cuaderno del estudiante de 6.º básico Artes Visuales: AR06 OA 05 (evaluar críticamente trabajos propios y de pares según emociones y problemáticas sociales, materiales y procedimientos, lenguaje visual y propósitos expresivos)."""
from __future__ import annotations

from student_content_ar6_a import lesson, m, task, w
from student_lessons import arith, ex

OA5 = "AR06 OA 05"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA5, 1,
    "Una hoja y un lápiz. Los trabajos que se evalúan en esta clase son inventados y están descritos aquí; puedes usar después un trabajo tuyo.",
    "Aprenderé qué es evaluar críticamente un trabajo de arte y cuáles son los cuatro criterios para hacerlo: emociones y problemáticas sociales, materiales y procedimientos, lenguaje visual y propósitos expresivos. Sirve para dar y recibir opiniones claras, justas y útiles.",
    ["Sé analizar una obra con lenguaje visual, material y contexto.", "Sé que fundamentar es apoyar lo que digo con evidencias."],
    [
        "Evaluar críticamente es mirar un trabajo con criterios claros, juzgar qué logra y qué no, y dar razones con evidencia. «Crítico» no significa «negativo»: una buena crítica reconoce lo que funciona y propone mejoras. Evalúo el trabajo, no a la persona, y lo hago con respeto. Para esta unidad uso cuatro criterios. El primero es la expresión de emociones y problemáticas sociales: ¿qué emoción o problema se ve y cómo lo muestra?",
        "El segundo criterio son los materiales y procedimientos: ¿se eligieron materiales adecuados y se usaron con cuidado? El tercero es la aplicación del lenguaje visual: ¿cómo se usaron la línea, la forma, el color, la textura y el espacio? El cuarto son los propósitos expresivos: ¿la obra logra lo que su autor quería comunicar? Cada comentario debe corresponder a un criterio y llevar una evidencia que se vea. Así no mezclo gustos con razones.",
        "Una frase útil tiene cuatro partes: el criterio, la evidencia, el juicio y la sugerencia. Ejemplo: «En materiales, el papel se arrugó porque tiene demasiada cola; logra unir las piezas, pero conviene usar menos cola». Antes de evaluar, leo la intención del autor, porque no se puede juzgar si no sé qué quería lograr. También evito frases como «está feo» o «está perfecto» sin explicar por qué.",
    ],
    [("evaluar", "juzgar un trabajo con criterios y razones"), ("criterio", "aspecto que se mira para evaluar"), ("evidencia", "detalle visible que sostiene un juicio"), ("sugerencia", "propuesta concreta para mejorar"), ("problemática social", "problema que afecta a muchas personas, como la basura en una plaza")],
    [
        w("Asignar un comentario a su criterio", "Comentario: «El azul oscuro del fondo hace que las figuras amarillas se vean muy bien». ¿A qué criterio corresponde?", ["Habla de colores y de cómo se ven unas formas.", "Eso es el lenguaje visual.", "Entonces es el tercer criterio."], "Lenguaje visual"),
        w("Completar una crítica", "Trabajo: un dibujo de una plaza con un solo árbol seco, bancas vacías y colores grises; intención: mostrar la falta de áreas verdes. Escribe una frase con criterio, evidencia, juicio y sugerencia.", ["Criterio: propósito expresivo.", "Evidencia: el árbol seco y los grises muestran falta de verde.", "Juicio y sugerencia: logra mostrar la falta de áreas verdes; podría agregar un pequeño brote verde para dar esperanza si quiere."], "Propósito: el árbol seco y los grises muestran falta de verde; logra la idea y podría sumar un brote verde"),
    ],
    [
        m("Decir solo «me gustó» o «está feo» sin criterio ni evidencia.", "No ayuda al autor a entender qué mejorar.", "Nombra el criterio, muestra la evidencia, da un juicio y una sugerencia."),
        m("Criticar a la persona («no sabes dibujar») en vez del trabajo.", "Ofende y no mejora la obra.", "Habla del trabajo y de lo que se ve en él."),
    ],
    [
        ex("¿Evaluar críticamente es solo decir lo malo de un trabajo?", "No", "También reconoce lo que logra y propone mejoras."),
        ex("¿Cuál es uno de los cuatro criterios: «materiales y procedimientos» o «cuánto cuesta»?", "Materiales y procedimientos", "Es uno de los criterios de evaluación."),
        ex("En una crítica, «sugerencia» significa...", "Una propuesta concreta para mejorar", "Ayuda al autor a saber qué cambiar."),
    ],
    [
        ex("Comentario: «La cola se ve por los bordes y el cartón se despegó». ¿A qué criterio corresponde: materiales y procedimientos o propósitos expresivos?", "Materiales y procedimientos", "Habla del uso de los materiales."),
        ex("Comentario: «Se ve mucha tristeza porque la figura está sola y gris». ¿A qué criterio corresponde: expresión de emociones o lenguaje visual?", "Expresión de emociones", "Habla de la emoción que muestra la obra."),
        ex("Comentario: «La línea quebrada y los rojos fuertes hacen sentir tensión». ¿Qué criterio principal usa: lenguaje visual o materiales?", "Lenguaje visual", "Nombra línea y color, que son recursos del lenguaje visual."),
    ],
    [
        ex("Quieres evaluar un trabajo cuyo autor dice que quiso mostrar alegría. Antes de evaluar, ¿qué necesitas conocer: su intención o el precio de sus materiales?", "Su intención", "No se puede juzgar si no se sabe qué quería lograr."),
        ex("¿Cuál frase es una buena crítica? A: «Está horrible». B: «Los colores cálidos y las figuras en movimiento muestran alegría; podrías aclarar el fondo para que se vean más».", "B", "La B tiene evidencia, juicio y sugerencia."),
        ex("Una crítica dice: «El árbol seco y los grises muestran falta de verde». ¿Cuál es la evidencia?", "El árbol seco y los grises", "Es lo que se ve y sostiene el juicio."),
    ],
    [
        ex("Dos comentarios sobre el mismo dibujo. Uno: «Está feo». Otro: «Los trazos son muy débiles y el fondo se confunde con la figura; usa un color más oscuro en el fondo». ¿Cuál ayuda más?", "El segundo", "Da evidencia y una sugerencia concreta."),
        ex("Sobre un trabajo de un compañero, ¿qué conviene decir: «No sabes pintar» o «Los colores se mezclaron porque no esperaste el secado»?", "Los colores se mezclaron porque no esperaste el secado", "Se evalúa el trabajo con una razón, no a la persona."),
    ],
    [
        ex("El autor de un trabajo dijo que quiso mostrar el cuidado del agua. Otro compañero dice que la obra muestra mucha alegría. ¿Qué debe hacer quien evalúa: comparar lo que se ve con la intención del autor o ignorar la intención?", "Comparar lo que se ve con la intención del autor", "Así se juzga si logra su propósito."),
        arith("Un trabajo recibe 4 comentarios: 1 sobre emociones, 1 sobre materiales y 1 sobre lenguaje visual. ¿Cuántos comentarios corresponden al cuarto criterio, propósitos expresivos?", "4-3", "Se resta del total los tres comentarios ya asignados."),
    ],
    ex("Un compañero te muestra un collage de tapas pegadas formando un pez, y te pide tu opinión. Su intención es mostrar el reciclaje. ¿Cómo empiezas: leyendo su intención y luego nombrando un criterio con evidencia, o diciendo si te gusta?", "Leyendo su intención y luego nombrando un criterio con evidencia", "Así la crítica es justa y útil."),
    [
        ex("¿Cuántos criterios usamos para evaluar un trabajo en esta unidad?", "Cuatro", "Son emociones y problemáticas, materiales y procedimientos, lenguaje visual y propósitos expresivos."),
        ex("Verdadero o falso: una crítica útil lleva criterio, evidencia, juicio y sugerencia.", "Verdadero", "Esas partes ordenan la evaluación."),
        ex("¿Se evalúa el trabajo o a la persona?", "El trabajo", "La crítica se refiere a lo que se ve en la obra."),
    ],
    task(
        "Elige UN trabajo descrito. A) «Plaza sin árboles»: dibujo en lápiz de colores con bancas vacías, un árbol seco y colores grises; intención: mostrar la falta de áreas verdes. B) «Río de envases»: collage de tapas y papeles azules pegados con mucha cola que se arrugó; intención: mostrar la contaminación del agua. C) «Mi abuelo y yo»: dibujo con colores cálidos, dos figuras tomadas de la mano y un sol grande; intención: mostrar cariño. Escribe una frase de evaluación para cada uno de los cuatro criterios, con evidencia, juicio y sugerencia.",
        "Elegí la A. Emociones y problemática: el árbol seco muestra falta de áreas verdes; se entiende bien. Materiales: los lápices de colores están bien usados; se podría presionar más para que el color sea más intenso. Lenguaje visual: los grises dan sensación de tristeza; un brote verde podría dar contraste. Propósito: logra mostrar la falta de verde, porque casi todo el dibujo es gris.",
        ["escribe una frase por criterio", "cada frase tiene evidencia", "incluye juicio y sugerencia", "evalúa el trabajo y no a la persona"],
        ["cuatro frases de evaluación"],
        ["opiniones sin evidencia", "criticar a la persona"],
        "Pregunta qué evidencia sostiene cada juicio y qué sugerencia ayudaría más al autor.",
    ),
    "Mira un dibujo tuyo y di una cosa que logra y una que mejorarías, con una evidencia.",
    "Evalúa un mismo trabajo desde dos criterios distintos y comprueba si llegas a conclusiones diferentes.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA5, 2,
    "Una hoja y lápiz. Las obras que se evalúan se describen en la clase; son inventadas y no representan a personas reales.",
    "Aprenderé a evaluar si un trabajo expresa una emoción o una problemática social de forma clara y respetuosa. Sirve para dar opiniones útiles sobre obras que hablan de temas importantes para las personas.",
    ["Sé que evaluar críticamente usa criterios, evidencias y sugerencias.", "Sé analizar color, línea y espacio en una obra."],
    [
        "Muchos trabajos de arte expresan una emoción, como alegría, miedo, calma o tristeza, o muestran un problema social, como la basura en las calles, la falta de áreas verdes, el ruido o la falta de respeto hacia las personas mayores. Para evaluarlos, pregunto: ¿qué emoción o problema muestra? ¿Con qué recursos lo hace? ¿Se entiende sin que el autor tenga que explicarlo? Un trabajo logra su expresión cuando los recursos visuales (color, línea, tamaños, espacio) apoyan la emoción o el problema.",
        "Por ejemplo, un dibujo de una calle llena de basura con colores sucios y una figura pequeña que recoge un papel muestra una problemática social, la basura en la ciudad, y también esperanza, por la figura que ayuda. Si la figura es muy pequeña y casi no se ve, puedo sugerir agrandarla. Una sugerencia útil dice qué cambiar y por qué; por ejemplo: «agranda la figura para que se note que alguien ayuda».",
        "Cuando una obra trata un tema social, la evalúo con especial respeto. No me burlo de las personas ni del problema, y no uso nombres de personas reales. Reconozco el esfuerzo de quien se atreve a hablar de un tema difícil. También cuido que la obra no ofenda a nadie ni exponga a otra persona. Mi crítica busca ayudar a que el mensaje sea más claro, no a quitarle valor al trabajo.",
    ],
    [("emoción", "lo que siente una persona, como alegría o miedo"), ("problemática social", "problema que afecta a muchas personas de una comunidad"), ("expresar", "mostrar algo con los recursos de la obra"), ("mensaje", "idea que la obra quiere comunicar"), ("respeto", "tratar con consideración a las personas y a sus ideas")],
    [
        w("Evaluar la emoción", "Dibujo: un niño con los brazos abiertos corriendo en un campo amarillo bajo un sol grande, con líneas largas y curvas. Intención: mostrar alegría. ¿La obra expresa alegría?", ["Los colores amarillos son cálidos.", "Los brazos abiertos y las líneas curvas dan idea de libertad.", "Todo apoya la alegría."], "Sí; los colores cálidos, los brazos abiertos y las curvas apoyan la alegría"),
        w("Proponer una sugerencia", "Dibujo de una calle con basura; una figura casi invisible recoge un papel. Intención: mostrar esperanza. ¿Qué sugieres?", ["La figura que muestra esperanza casi no se ve.", "La obra no destaca ese mensaje.", "Sugiero agrandar la figura y darle un color más claro."], "Agrandar la figura y darle un color claro"),
    ],
    [
        m("Pensar que un tema social serio solo puede mostrarse con colores oscuros.", "También se pueden mostrar con esperanza o contraste.", "Mira qué quiere comunicar el autor y qué recursos usa."),
        m("Burlarse de un trabajo porque su tema es difícil.", "Falta respeto y no ayuda a mejorar.", "Evalúa el mensaje y los recursos con respeto."),
    ],
    [
        ex("¿Cuál de estos es un ejemplo de problemática social: la basura acumulada en una plaza o un lápiz rojo?", "La basura acumulada en una plaza", "Es un problema que afecta a muchas personas del barrio."),
        ex("¿La alegría es una emoción o un material?", "Una emoción", "Es algo que sentimos."),
        ex("Evaluar con respeto significa...", "Tratar con consideración a las personas y al trabajo", "Se critica el trabajo con razones, sin burlas."),
    ],
    [
        ex("Un dibujo de una plaza sin juegos, con una niña mirando una reja y colores grises quiere mostrar la falta de espacios para jugar. ¿Qué problemática social aborda?", "La falta de espacios para jugar", "La intención nombra esa problemática."),
        ex("Un trabajo usa azules oscuros, una figura encogida y mucho vacío. ¿Qué emoción expresa con más claridad: soledad o entusiasmo?", "Soledad", "El vacío, la figura encogida y los azules oscuros apoyan la soledad."),
        ex("¿Se entiende la emoción de un trabajo si el autor tiene que explicarla mucho porque no se ve en la obra?", "No", "Una obra logra expresar cuando los recursos visuales lo muestran por sí solos."),
    ],
    [
        ex("Una obra quiere mostrar miedo con una figura pequeña entre sombras. Un compañero sugiere agregar muchos colores alegres. ¿Esa sugerencia ayuda a la emoción?", "No", "Los colores alegres contradicen el miedo."),
        ex("Una obra sobre el ruido de la ciudad usa líneas quebradas rojas y amarillas. ¿Los recursos apoyan el tema?", "Sí", "Las líneas quebradas y los colores fuertes se sienten ruidosos."),
        ex("Un trabajo sobre el cuidado del agua muestra una gota enorme azul y personas que la rodean. ¿Qué emoción se entiende mejor: protección o miedo?", "Protección", "Las personas rodeando la gota sugieren cuidado."),
    ],
    [
        ex("Dos dibujos del mismo tema, la basura en una playa. Uno muestra colores sucios y una persona recogiendo; el otro, una playa limpia y sin personas. Si la intención es mostrar el problema y la acción, ¿cuál cumple mejor?", "El que muestra colores sucios y una persona recogiendo", "Muestra el problema y la acción."),
        ex("Un compañero dice que un trabajo sobre las personas mayores es «aburrido». ¿Qué crítica es más respetuosa y útil? A: «Los colores son muy apagados; puedes agregar un color cálido para mostrar cariño». B: «Qué fome, nadie lo va a mirar».", "A", "La A da evidencia y sugerencia, sin burla."),
    ],
    [
        ex("Evaluar una obra sobre la falta de áreas verdes. La obra usa un solo árbol verde pequeño en un fondo gris. ¿Qué mensaje sugiere: que hay pocas áreas verdes o que sobran?", "Que hay pocas áreas verdes", "El único árbol pequeño en un fondo gris sugiere escasez."),
        ex("Una niña dibujó a una persona real de su curso con burla para hablar de un problema. ¿Es adecuado?", "No", "No se debe exponer ni burlarse de una persona real."),
    ],
    ex("Debes evaluar un afiche sobre el respeto a las personas mayores. Muestra una niña ayudando a un señor a cruzar la calle, con colores cálidos. La intención es mostrar respeto. ¿Cuál es tu juicio: logra su intención porque hay una acción amable y colores cálidos, o no logra nada?", "Logra su intención porque hay una acción amable y colores cálidos", "La acción y el color apoyan el mensaje de respeto."),
    [
        ex("¿Qué debe hacer una obra para expresar bien una emoción?", "Usar recursos visuales que la apoyen", "El color, la línea y el espacio deben ir en la misma dirección."),
        ex("Verdadero o falso: una obra sobre un tema serio puede mostrar esperanza.", "Verdadero", "Puede incluir contraste con una acción positiva."),
        ex("¿Qué debes evitar al evaluar un trabajo sobre un tema social?", "Las burlas", "Se requiere respeto con las personas y el tema."),
    ],
    task(
        "Elige UN trabajo descrito. A) «Plaza sin juegos»: dibujo gris con una niña mirando por una reja; intención: mostrar la falta de espacios para jugar. B) «Ruido»: líneas quebradas rojas y amarillas con una figura que se tapa los oídos; intención: mostrar el ruido de la ciudad. C) «Amistad»: dos figuras de colores cálidos tomadas de la mano; intención: mostrar cariño. Evalúa: ¿expresa la emoción o el problema?, ¿con qué recursos?, ¿qué sugieres?",
        "Elegí la B. Sí expresa el ruido: las líneas quebradas y los colores fuertes se sienten ruidosos y la figura tapándose los oídos lo confirma. Sugiero agregar un poco de azul tranquilo en una esquina para mostrar contraste con el ruido.",
        ["dice qué emoción o problema muestra", "nombra los recursos que lo apoyan", "da un juicio y una sugerencia", "evalúa con respeto"],
        ["frase de evaluación con evidencia"],
        ["opinar sin evidencia", "burlarse del tema"],
        "Pregunta cómo se enteraría alguien de la emoción sin leer la intención y qué recurso es el más claro.",
    ),
    "Piensa en una emoción y di qué colores y líneas usarías para mostrarla.",
    "Rehace el dibujo de un trabajo evaluado aplicando tu sugerencia y comprueba si se entiende mejor.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA5, 3,
    "Una hoja, lápiz y, si quieres, un trabajo tuyo hecho con papel o pintura. Los trabajos que se evalúan están descritos en la clase.",
    "Aprenderé a evaluar el uso de materiales y procedimientos de un trabajo, con una escala de tres niveles. Sirve para saber si los materiales fueron los adecuados, si se usaron con cuidado y qué mejorar.",
    ["Sé evaluar con criterios y evidencias.", "Sé reconocer problemas de técnica como chorreado, arrugas por cola o estampas manchadas."],
    [
        "Para evaluar los materiales y procedimientos miro tres cosas. Primero, si los materiales eran adecuados para la idea: por ejemplo, la lana sirve para una textura blanda, y el cartón para una base firme. Segundo, si se usaron con cuidado: sin manchas, sin cola a la vista, con bordes limpios, sin arrugas por exceso de humedad. Tercero, si el procedimiento se siguió en orden: por ejemplo, esperar que la capa se seque antes de pintar encima.",
        "Una escala de tres niveles ayuda a ordenar la evaluación. Nivel 3, Logrado: los materiales son adecuados, se usan con cuidado y el procedimiento se sigue en orden. Nivel 2, En desarrollo: los materiales son adecuados, pero hay descuidos que se notan. Nivel 1, Por mejorar: los materiales no sirven a la idea o hay muchos descuidos. Siempre acompaño el nivel con una evidencia, como «hay manchas en los bordes» o «el cartón se despegó».",
        "También evalúo mi propio trabajo con la misma escala. Compruebo qué fue difícil, qué material usé bien y qué cambiaría. Un nivel bajo no es un castigo: indica qué practicar. Evaluar la técnica no significa evaluar el talento, sino el cuidado y el conocimiento de los materiales. Con práctica, cualquiera puede mejorar el uso de las herramientas y los pasos, y eso se nota en el trabajo.",
    ],
    [("material adecuado", "material que sirve a la idea de la obra"), ("procedimiento", "pasos para hacer algo, en un orden"), ("nivel", "grado de logro en una escala"), ("descuido", "falta de cuidado que se nota en el trabajo"), ("autoevaluar", "evaluar el propio trabajo")],
    [
        w("Asignar un nivel", "Un collage de papeles tiene materiales adecuados, pero hay cola visible en los bordes y dos papeles arrugados. ¿Qué nivel recibe?", ["Los materiales son adecuados.", "Hay descuidos que se notan.", "Eso es el nivel 2, En desarrollo."], "Nivel 2, En desarrollo"),
        w("Dar la evidencia", "Un trabajo de pintura en que el amarillo chorreó sobre el azul porque no esperaron el secado. ¿Qué evidencia y qué sugerencia das?", ["Evidencia: el amarillo chorreó sobre el azul.", "Causa: no se esperó el secado.", "Sugerencia: esperar que cada capa se seque antes de pintar encima."], "El amarillo chorreó sobre el azul; esperar el secado entre capas"),
    ],
    [
        m("Poner un nivel bajo por considerar que «no tiene talento».", "Se evalúa el cuidado y los pasos, no el talento.", "Describe la evidencia de la técnica."),
        m("Dar el nivel más alto sin revisar bordes, manchas o procedimiento.", "No se evaluó realmente.", "Revisa las tres cosas antes de decidir."),
    ],
    [
        ex("¿Cuántos niveles tiene la escala de esta clase?", "Tres", "Son Logrado, En desarrollo y Por mejorar."),
        ex("El nivel 3 de la escala se llama...", "Logrado", "Es el nivel con materiales adecuados, cuidado y orden."),
        ex("Un material adecuado es el que...", "Sirve a la idea de la obra", "Su textura y resistencia ayudan al mensaje."),
    ],
    [
        ex("Un cartón se despegó en las esquinas y los materiales eran adecuados. ¿Qué criterio estás evaluando: el uso de los materiales o la emoción?", "El uso de los materiales", "Habla de cómo se unieron y cuidaron."),
        ex("Una persona pintó encima antes de que se secara la capa de abajo. ¿Qué parte del procedimiento no siguió: esperar el secado o elegir el color?", "Esperar el secado", "El secado entre capas es un paso del procedimiento."),
        ex("Un trabajo tiene materiales que no sirven a la idea y muchos descuidos. ¿Qué nivel recibe: 1, 2 o 3?", "1", "Cumple con la descripción del nivel Por mejorar."),
    ],
    [
        ex("Un trabajo sobre una montaña quiere dar sensación de aspereza. Usó arena pegada con cola. ¿Es un material adecuado?", "Sí", "La arena es rugosa."),
        ex("Un trabajo de grabado salió con las letras al revés. El autor no invirtió las letras en la matriz. ¿Qué sugieres?", "Invertir las letras en la matriz", "La estampa se invierte y hay que anticiparlo."),
        arith("Evaluaste 4 trabajos: 2 quedaron en nivel 3, 1 en nivel 2 y 1 en nivel 1. ¿Cuántos trabajos no alcanzaron el nivel 3?", "4-2", "Se resta del total los que sí llegaron al nivel 3."),
    ],
    [
        ex("Una compañera dice: «Mi trabajo tiene nivel 3 porque terminé primero». ¿Es un buen argumento?", "No", "El nivel depende de materiales, cuidado y procedimiento, no de la velocidad."),
        ex("Un compañero señala que tu trabajo tiene el nivel 2 y te muestra dos manchas de pintura en los bordes. ¿Qué cualidad tiene su comentario: evidencia concreta o solo gusto personal?", "Evidencia concreta", "Muestra manchas visibles que sostienen el juicio."),
    ],
    [
        ex("Un trabajo usa cartulina fina como base de una escultura que debe sostener un peso. Se doblan las paredes. ¿La elección del material fue adecuada?", "No", "La cartulina fina no soporta peso; faltó resistencia."),
        arith("Un curso evalúa 9 trabajos: 4 quedan en nivel 3, 3 en nivel 2 y los demás en nivel 1. ¿Cuántos quedan en nivel 1?", "9-4-3", "Se resta del total los de nivel 3 y los de nivel 2."),
    ],
    ex("Quieres autoevaluar tu estampa de cartón. El material era adecuado, seguiste los pasos en orden, los bordes están limpios y no hay manchas. ¿Qué nivel eliges: 3 Logrado o 1 Por mejorar?", "3 Logrado", "Cumple las tres cosas: material adecuado, cuidado y orden."),
    [
        ex("¿Qué miras para evaluar materiales y procedimientos?", "Si fueron adecuados, si se usaron con cuidado y si se siguió el orden", "Son las tres cosas de esta clase."),
        ex("Verdadero o falso: un nivel bajo en técnica es un castigo.", "Falso", "Indica qué practicar."),
        ex("¿Qué debe acompañar a cada nivel?", "Una evidencia", "Así se justifica el nivel."),
    ],
    task(
        "Elige UN trabajo descrito. A) Collage de papeles de colores sobre cartón; los materiales son adecuados, hay cola visible y dos papeles arrugados. B) Pintura de un lago; los colores están limpios, bien secados entre capas y sin manchas. C) Escultura de cartulina fina que se dobla al ponerle una tapa encima. Asigna un nivel (1, 2 o 3) en materiales y procedimientos, escribe la evidencia y una sugerencia.",
        "Elegí la A. Nivel 2, En desarrollo. Evidencia: los materiales son adecuados, pero se ve cola en los bordes y hay dos papeles arrugados. Sugerencia: usar menos cola, extendida con un pincel, y presionar con un papel limpio encima.",
        ["asigna un nivel con razón", "muestra una evidencia", "da una sugerencia concreta", "evalúa el cuidado y no el talento"],
        ["nivel, evidencia y sugerencia escritos"],
        ["nivel sin evidencia", "evaluar el talento"],
        "Pregunta qué paso del procedimiento mejoraría más el trabajo y cómo se vería.",
    ),
    "Revisa un trabajo tuyo y di un material bien usado y un descuido.",
    "Autoevalúa dos trabajos tuyos con la misma escala y compara cuál nivel es más alto y por qué.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA5, 4,
    "Una hoja, lápiz y una regla. Los trabajos y la pauta de puntos se describen en la clase.",
    "Aprenderé a evaluar la aplicación del lenguaje visual (color, línea, composición y textura) con una pauta de puntos. Sirve para dar un juicio claro sobre cómo un trabajo usa sus recursos visuales.",
    ["Sé que el lenguaje visual incluye línea, forma, color, textura y espacio.", "Sé evaluar con una escala de niveles y evidencias."],
    [
        "Evaluar el lenguaje visual es mirar cómo se usan los recursos de una imagen y si ayudan a comunicar la idea. En esta clase uso una pauta de cuatro aspectos, cada uno con puntaje de 1 a 3. El primero es el color: ¿hay una gama clara y contrastes que ayudan a ver lo importante? El segundo es la línea: ¿su tipo (curva, recta, quebrada) apoya el mensaje? El tercero es la composición: ¿están bien ubicados los elementos y el espacio vacío o lleno? El cuarto es la textura: ¿se nota y aporta?",
        "En cada aspecto, 3 puntos significa que el recurso apoya claramente la idea; 2 puntos, que la apoya en parte; y 1 punto, que no la apoya o la confunde. Así, la suma máxima es 12 puntos. El puntaje total ayuda a resumir, pero lo más importante son las evidencias de cada aspecto. Dos trabajos con el mismo total pueden tener fortalezas distintas, por eso conviene mirar el detalle.",
        "Por ejemplo: un dibujo de una noche tranquila tiene colores azules y violetas (3 puntos en color), líneas horizontales suaves (3), una luna pequeña al centro con mucho espacio vacío (2, porque el espacio vacío podría ser más equilibrado) y casi sin textura (1). Total: 9 de 12. Al comunicar el resultado, empiezo por lo que funciona y después sugiero un cambio concreto, como agregar una textura de puntitos en el cielo.",
    ],
    [("pauta", "lista de aspectos con puntajes para evaluar"), ("puntaje", "número que muestra cuánto se logró"), ("composición", "cómo están ubicados los elementos en la obra"), ("fortaleza", "aspecto que el trabajo hace bien"), ("equilibrio", "reparto de peso visual que no se ve cargado hacia un lado")],
    [
        w("Calcular el puntaje", "Un trabajo recibe 3 en color, 2 en línea, 3 en composición y 1 en textura. ¿Cuál es el puntaje total?", ["Se suman los puntos de los cuatro aspectos.", "3 + 2 + 3 + 1.", "El total es 9 de 12."], "9 de 12 puntos"),
        w("Justificar un puntaje", "Un dibujo usa líneas quebradas en rojo para mostrar tensión. ¿Qué puntaje en línea le pondrías y por qué?", ["Las líneas quebradas apoyan la tensión.", "El rojo refuerza la idea.", "El recurso apoya claramente la idea: 3 puntos."], "3 puntos, porque las líneas quebradas apoyan la tensión"),
    ],
    [
        m("Decidir el total sin mirar el detalle de cada aspecto.", "Se pierde la información sobre qué mejorar.", "Comenta las evidencias de cada aspecto."),
        m("Dar 3 puntos a todo para ser amable.", "No ayuda al autor a mejorar.", "Sé honesto y justo, con una razón por cada puntaje."),
    ],
    [
        ex("¿Cuántos aspectos tiene la pauta de esta clase?", "Cuatro", "Son color, línea, composición y textura."),
        ex("En esta pauta, ¿3 puntos significan que el recurso apoya claramente la idea o que no la apoya?", "Que la apoya claramente", "El puntaje más alto indica el mejor logro."),
        ex("¿Qué es la composición: cómo se ubican los elementos o qué color tienen?", "Cómo se ubican los elementos", "Es la organización de lo que hay en la obra."),
    ],
    [
        arith("Un trabajo recibe 2 en color, 3 en línea, 2 en composición y 2 en textura. ¿Cuántos puntos suma?", "2+3+2+2", "Se suman los puntos de los cuatro aspectos."),
        ex("Un dibujo de una feria alegre usa mucho gris en todo. ¿Qué puntaje es más probable en color si la idea era alegría: 1 o 3?", "1", "El gris no apoya la alegría."),
        ex("¿Cuál es el puntaje máximo posible en la pauta completa?", "12", "Cuatro aspectos con 3 puntos cada uno suman 12.", calc="4*3"),
    ],
    [
        ex("Dos trabajos tienen 10 puntos. En uno todo está bien menos la textura y en el otro falla la composición. ¿Es mejor mirar solo el total o el detalle?", "El detalle", "Cada uno necesita una sugerencia distinta."),
        ex("Una figura muy pequeña queda en una esquina con casi todo el espacio vacío, pero la idea era mostrar la importancia de esa figura. ¿Qué aspecto necesita mejorar: la composición o la textura?", "La composición", "La ubicación y el tamaño no destacan lo importante."),
        ex("Una pintura de un día de lluvia tiene azules y grises, líneas verticales largas y gotas repetidas. ¿Qué puntaje le darías en línea si la idea es lluvia: 1 o 3?", "3", "Las líneas verticales largas apoyan claramente la idea de lluvia."),
    ],
    [
        ex("Un compañero recibió 7 puntos y dice: «Mi trabajo es malo». ¿Qué conviene responderle: «Tiene 7 de 12; te muestro cuáles aspectos van bien y cuál puedes mejorar» o «Sí, es malo»?", "Tiene 7 de 12; te muestro cuáles aspectos van bien y cuál puedes mejorar", "El puntaje se acompaña de fortalezas y sugerencias."),
        ex("Un trabajo recibe 3 en color, 3 en línea, 3 en composición y 1 en textura. ¿Qué sugerencia ayuda más: agregar una textura que aporte al mensaje o cambiar todos los colores?", "Agregar una textura que aporte al mensaje", "El único aspecto bajo es la textura."),
    ],
    [
        ex("Un trabajo obtuvo 6 puntos de un máximo de 12. ¿Qué parte del total es: la mitad o un cuarto?", "La mitad", "6 es la mitad de 12."),
        arith("Un grupo evalúa 5 trabajos y a cada uno le da 8 puntos. ¿Cuántos puntos hay en total entre los cinco?", "5*8", "Se multiplican los trabajos por el puntaje de cada uno."),
    ],
    ex("Debes evaluar una pintura de un amanecer con anaranjados y amarillos que se mezclan suavemente, líneas curvas, un sol bien ubicado a un tercio del borde y textura de pinceladas visibles. La idea era calidez y calma. ¿Cuál total te parece más justo: 11 o 4?", "11", "Casi todos los recursos apoyan la idea."),
    [
        ex("¿Qué debe acompañar a cada puntaje?", "Una evidencia", "Así se justifica el puntaje."),
        ex("Verdadero o falso: el puntaje total resume, pero el detalle de cada aspecto es más importante.", "Verdadero", "El detalle dice qué mejorar."),
        ex("¿Qué aspecto de la pauta se refiere a la ubicación de los elementos?", "La composición", "Es la organización de la obra."),
    ],
    task(
        "Elige UN trabajo. A) «Noche tranquila»: azules y violetas, líneas horizontales suaves, luna pequeña al centro con mucho vacío y casi sin textura. B) «Feria»: colores muy variados y fuertes, líneas diagonales, figuras en todo el cuadro y papeles de distintas texturas. C) «Tormenta»: grises y azules oscuros, líneas verticales largas, pocas figuras y textura de pintura gruesa. Asigna de 1 a 3 puntos por cada aspecto (color, línea, composición, textura), suma el total y escribe una fortaleza y una sugerencia.",
        "Elegí la A. Color 3, línea 3, composición 2, textura 1. Total: 9 de 12. Fortaleza: los azules y las líneas horizontales dan calma. Sugerencia: agregar una textura de puntitos en el cielo y equilibrar el espacio vacío.",
        ["asigna un puntaje por aspecto con razón", "calcula bien el total", "escribe una fortaleza", "da una sugerencia concreta"],
        ["tabla con cuatro puntajes", "frase de fortaleza y sugerencia"],
        ["puntaje sin evidencia", "dar siempre el máximo"],
        "Pregunta qué aspecto subió más con su sugerencia y qué puntaje esperaría después del cambio.",
    ),
    "Mira un afiche y di cuántos puntos le darías en color, de 1 a 3, y por qué.",
    "Evalúa un trabajo tuyo con la pauta y compara con la evaluación de una persona de tu casa.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA5, 5,
    "Una hoja y lápiz. Los trabajos y las críticas que se analizan están escritos en la clase.",
    "Aprenderé a evaluar si un trabajo logra su propósito expresivo y a escribir una crítica completa y fundamentada con criterio, evidencia, juicio y sugerencia. Sirve para comunicar mis juicios de manera clara, justa y respetuosa.",
    ["Sé usar los criterios de evaluación y las pautas de puntaje.", "Sé que fundamentar es apoyar con evidencias visibles."],
    [
        "El propósito expresivo es lo que el autor quiere comunicar. Evaluar si un trabajo lo logra es comparar lo que se ve con esa intención. Para hacerlo, primero leo la intención. Después miro el trabajo y busco evidencias que apoyen o contradigan esa idea. Por último decido si el propósito se logra del todo, en parte o no se logra, y explico por qué. Si la intención es mostrar calma, y el trabajo usa azules suaves y líneas horizontales, se logra; si usa rojo fuerte y líneas quebradas, no.",
        "Una crítica completa tiene cuatro partes: el criterio que evalúo, la evidencia que veo, el juicio que doy y la sugerencia que propongo. Un ejemplo: «En el propósito expresivo, el trabajo quiere mostrar la soledad y lo logra en parte: la figura pequeña y el espacio vacío la muestran, pero el amarillo vivo del fondo da alegría. Sugiero cambiar el fondo por un tono gris azulado». Observa que reconoce algo bueno y propone un cambio concreto.",
        "Una buena crítica es respetuosa y específica. Evita las palabras absolutas como «nunca» o «todo está mal». Tampoco habla de la persona, solo del trabajo. Después de escribirla, la releo y compruebo que cada afirmación tenga una evidencia. Un trabajo puede lograr su propósito aunque a mí no me guste su estilo: mi gusto no es el criterio, sino la relación entre la intención y los recursos que se ven.",
    ],
    [("propósito expresivo", "lo que el autor quiere comunicar con su obra"), ("juicio", "conclusión sobre qué tan bien se logra algo"), ("crítica", "evaluación con criterios, evidencias y sugerencias"), ("específico", "preciso, no general ni vago"), ("absoluto", "que no admite excepciones, como nunca o todo")],
    [
        w("Juzgar el propósito", "Intención: mostrar la calma de un lago. El trabajo usa azules suaves, líneas horizontales largas y mucho espacio libre. ¿Logra el propósito?", ["Los azules suaves dan calma.", "Las líneas horizontales apoyan la quietud.", "Todos los recursos coinciden con la calma."], "Sí, lo logra"),
        w("Completar una crítica", "Intención: mostrar alegría. El trabajo tiene figuras saltando, pero el fondo es gris oscuro. Escribe el juicio y la sugerencia.", ["Evidencia 1: las figuras saltando apoyan la alegría.", "Evidencia 2: el fondo gris oscuro la contradice.", "Juicio: la logra en parte. Sugerencia: aclarar el fondo con un color cálido."], "La logra en parte; sugiero aclarar el fondo con un color cálido"),
    ],
    [
        m("Juzgar según si me gusta el estilo y no según el propósito.", "El gusto personal no es el criterio.", "Compara lo que se ve con la intención del autor."),
        m("Escribir una crítica general como «todo está mal».", "No ayuda y puede ofender.", "Sé específico y reconoce lo que funciona."),
    ],
    [
        ex("¿Qué compara una evaluación del propósito expresivo: lo que se ve con la intención o el precio con el tamaño?", "Lo que se ve con la intención", "Así se sabe si la obra logra lo que quiere comunicar."),
        ex("Una crítica completa tiene criterio, evidencia, juicio y...", "Sugerencia", "Son las cuatro partes."),
        ex("¿Se evalúa según el gusto personal o según el propósito del autor?", "Según el propósito del autor", "El gusto no es un criterio."),
    ],
    [
        ex("Intención: mostrar energía. El trabajo usa rojos y naranjos con líneas diagonales. ¿Logra su propósito: sí o no?", "Sí", "Los cálidos y las diagonales apoyan la energía."),
        ex("Intención: mostrar soledad. El trabajo muestra una multitud pegada de personas sonrientes. ¿Logra su propósito?", "No", "La multitud contradice la soledad."),
        ex("Una crítica dice: «Nunca vas a mejorar». ¿Es una buena crítica?", "No", "Es absoluta y habla de la persona."),
    ],
    [
        ex("Ordena las partes de una crítica: 1) sugerencia, 2) criterio, 3) juicio, 4) evidencia. Escribe los números en el orden de esta clase.", "2, 4, 3, 1", "Criterio, evidencia, juicio y sugerencia."),
        ex("Intención: mostrar frío. El trabajo usa azules y grises, pero una gran mancha naranja está al centro. ¿Qué sugerencia ayuda más: cambiar la mancha por un azul claro o agregar más naranjo?", "Cambiar la mancha por un azul claro", "Los naranjos dan calor y contradicen el frío."),
        ex("¿Cuál juicio está mejor fundamentado? A: «Lo logra porque las líneas curvas y azules muestran agua en movimiento». B: «Lo logra porque sí».", "A", "La A incluye evidencia."),
    ],
    [
        ex("Un trabajo cuya intención era mostrar calma recibió el comentario «los colores son bonitos». ¿Responde al propósito expresivo?", "No", "Habla de gusto y no compara con la intención."),
        ex("Un compañero dice: «Tu estilo no me gusta, entonces no logra su propósito». ¿Es un buen argumento?", "No", "El gusto no demuestra que el propósito no se logre."),
    ],
    [
        ex("Dos críticas al mismo trabajo. Primera: «Es lo peor». Segunda: «Quiere mostrar tristeza y lo logra con los grises y la figura sola, pero el sol amarillo la contradice; sugiero cambiarlo por un sol pálido». ¿Cuál es más completa?", "La segunda", "Tiene criterio, evidencia, juicio y sugerencia."),
        ex("Intención: mostrar el cuidado del agua. El trabajo muestra una llave que gotea y un balde debajo que recoge las gotas. ¿Qué evidencia apoya el propósito: el balde que recoge las gotas o el color de la llave?", "El balde que recoge las gotas", "Muestra una acción de cuidado, que es lo que quiere comunicar."),
    ],
    ex("Debes hacer la crítica de un cartel cuya intención es «cuidar el agua». El cartel muestra una gota grande y azul, un grifo cerrándose y letras pequeñas. ¿Cuál sugerencia es más útil: agrandar las letras o cambiar la gota por un cuadrado negro?", "Agrandar las letras", "Mejora que el mensaje se lea sin cambiar lo que ya funciona."),
    [
        ex("¿Qué es el propósito expresivo?", "Lo que el autor quiere comunicar con su obra", "Es lo que se compara con lo que se ve."),
        ex("Verdadero o falso: una crítica puede reconocer lo que funciona y sugerir un cambio.", "Verdadero", "Esa es la forma más útil de criticar."),
        ex("¿Por qué conviene evitar «nunca» y «todo está mal»?", "Porque son absolutos y no ayudan", "No indican qué mejorar."),
    ],
    task(
        "Elige UN trabajo. A) Intención: mostrar calma. Trabajo: azules claros, líneas horizontales y una barca pequeña, con un rayo rojo en el cielo. B) Intención: mostrar alegría en el recreo. Trabajo: niños saltando, colores amarillos y naranjos, líneas curvas y fondo claro. C) Intención: mostrar la contaminación del aire. Trabajo: cielo gris pardo, una chimenea con humo oscuro y un árbol pequeño gris. Escribe una crítica de cuatro partes (criterio, evidencia, juicio, sugerencia) sobre si logra su propósito.",
        "Elegí la A. Criterio: propósito expresivo. Evidencia: los azules claros, las líneas horizontales y la barca pequeña dan calma, pero el rayo rojo da tensión. Juicio: lo logra en parte. Sugerencia: cambiar el rayo rojo por una nube clara.",
        ["compara lo que se ve con la intención", "usa las cuatro partes", "reconoce algo que funciona", "es respetuosa y específica"],
        ["crítica escrita con cuatro partes"],
        ["juzgar según el gusto", "crítica general"],
        "Pregunta qué evidencia es la más fuerte de su crítica y cómo la diría con otras palabras sin perder claridad.",
    ),
    "Elige un afiche y di su propósito y una evidencia que lo apoya.",
    "Escribe dos críticas del mismo trabajo, una breve y otra con más evidencia, y compara cuál es más útil.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA5, 6,
    "Una hoja, lápiz y un trabajo tuyo o las críticas escritas en esta clase. Para practicar con otra persona puede ayudarte alguien de tu casa.",
    "Aprenderé a recibir y dar evaluaciones entre compañeros de forma respetuosa, y a decidir qué cambios hacer en mi trabajo sin perder mi autoría. Sirve para mejorar con ayuda de otros y mantener mi propia idea.",
    ["Sé escribir una crítica con criterio, evidencia, juicio y sugerencia.", "Sé que autoría significa que las decisiones finales son mías."],
    [
        "La evaluación entre pares es cuando compañeros evalúan los trabajos de los otros. Sirve para ver cosas que uno mismo ya no nota. Para que funcione, quien evalúa usa los cuatro criterios, da evidencias y sugerencias, y trata con respeto. Quien recibe la evaluación escucha sin interrumpir, hace preguntas para entender y agradece. No es necesario aceptar todo lo que le dicen, pero sí pensar cada comentario con atención.",
        "Para decidir qué cambios hacer, comparo cada sugerencia con mi propósito expresivo. Si me ayuda a comunicar mejor mi idea, la aplico. Si cambia mi idea, la agradezco y no la aplico. Puedo usar una tabla con tres columnas: «Lo que me dijeron», «Lo que decido» y «Por qué». Por ejemplo: «Me dijeron que el fondo amarillo contradice la calma; decido cambiarlo a azul claro, porque mi propósito es la calma».",
        "La autoevaluación completa el proceso. Reviso mi trabajo con la misma pauta que usarían los demás y anoto qué creo que logra y qué no. Al final comparo mi evaluación con la de mis compañeros: si coinciden, tengo más seguridad; si no, pienso por qué. Esta revisión no busca un trabajo perfecto, sino un trabajo mejor y más claro, donde yo sigo siendo quien decide. Los cambios que sí aplico los registro.",
    ],
    [("evaluación entre pares", "evaluación que hacen compañeros del mismo nivel"), ("autoevaluación", "evaluación que hago de mi propio trabajo"), ("autoría", "que las decisiones finales de la obra son mías"), ("sugerencia", "propuesta concreta para mejorar"), ("registro", "nota de lo que me dijeron, lo que decido y por qué")],
    [
        w("Decidir con el propósito", "Tu propósito es mostrar calma. Un compañero dice: «El fondo amarillo fuerte se ve más que tu barca». Otro dice: «Pon un rayo rojo para que sea emocionante». ¿Qué haces con cada comentario?", ["El primero ayuda: el fondo fuerte contradice la calma.", "El segundo cambia tu propósito: tensión, no calma.", "Aplico el primero y no el segundo."], "Cambio el fondo amarillo; no pongo el rayo rojo"),
        w("Escribir el registro", "Un compañero te sugirió aclarar el fondo y lo aplicaste. Completa la tabla.", ["Lo que me dijeron: el fondo oscuro tapaba la figura.", "Lo que decido: aclarar el fondo con celeste.", "Por qué: así la figura se ve y se mantiene la calma."], "Me dijeron que el fondo tapaba la figura; aclaro con celeste porque mantiene la calma"),
    ],
    [
        m("Aplicar todas las sugerencias aunque cambien mi idea.", "La obra deja de ser mía.", "Compara cada sugerencia con tu propósito."),
        m("Enojarse o interrumpir mientras te evalúan.", "No permite entender el comentario.", "Escucha primero y pregunta después."),
    ],
    [
        ex("La evaluación entre pares es la que hacen... ¿docentes o compañeros?", "Compañeros", "Pares son personas del mismo nivel."),
        ex("Cuando recibes una evaluación, ¿qué haces primero: escuchar o interrumpir?", "Escuchar", "Escuchar ayuda a entender."),
        ex("La autoevaluación es la evaluación de...", "Mi propio trabajo", "La hago yo mismo sobre lo que creé."),
    ],
    [
        ex("Un compañero te dice algo que cambia tu idea de calma por la de tensión. ¿Aplicas la sugerencia?", "No", "Cambia tu propósito expresivo."),
        ex("La tabla del registro tiene tres columnas: lo que me dijeron, lo que decido y...", "Por qué", "Justifica la decisión."),
        ex("Otro compañero sugiere agrandar la figura principal para que se vea más y tu propósito es destacarla. ¿La aplicas?", "Sí", "Apoya tu propósito."),
    ],
    [
        ex("Quieres dar una evaluación a un compañero. ¿Cuál frase usas: «Tu fondo gris oscuro tapa la figura; sugiero uno más claro» o «Está mal pintado»?", "Tu fondo gris oscuro tapa la figura; sugiero uno más claro", "Da evidencia y sugerencia concreta."),
        ex("En tu autoevaluación escribes: «Mi trabajo logra el propósito porque los azules y las curvas muestran calma». Tu compañero dice lo mismo. ¿Qué conclusión sacas: tengo más seguridad de que lo logra o debo rehacerlo todo?", "Tengo más seguridad de que lo logra", "Coinciden dos miradas."),
        arith("Recibes 5 sugerencias y decides aplicar 3. ¿Cuántas no aplicas?", "5-3", "Se resta lo aplicado del total."),
    ],
    [
        ex("Un amigo se molesta cuando le dicen que mejore su fondo y no vuelve a hablar con nadie del trabajo. ¿Qué actitud sería mejor: escuchar, preguntar y decidir qué aplicar, o no volver a mostrar su trabajo?", "Escuchar, preguntar y decidir qué aplicar", "La evaluación entre pares sirve para mejorar con ayuda de otros."),
        ex("Dos compañeros dan sugerencias contradictorias: uno dice «agranda la barca» y el otro «achícala». Tu propósito es mostrar lo pequeña que se siente la barca en un mar enorme. ¿Cuál aplicas?", "La de achicarla", "Apoya tu propósito de mostrar la barca pequeña."),
    ],
    [
        ex("Tu autoevaluación y la de un compañero difieren: tú crees que el color es 3 y él cree que es 1. ¿Qué haces: pedirle la evidencia y revisar el trabajo, o ignorar su opinión?", "Pedirle la evidencia y revisar el trabajo", "La diferencia se resuelve mirando evidencias."),
        ex("Después de la revisión, quien mira tu trabajo dice qué quería comunicar y acierta. ¿Qué indica eso sobre tu autoría?", "Que mi propósito sigue claro", "La intención se mantuvo después de los cambios."),
    ],
    ex("Te dan cuatro sugerencias: 1) aclarar el fondo, 2) cambiar la figura por otro tema, 3) usar un borde más limpio, 4) poner un cielo rojo que contradice tu propósito de calma. ¿Cuáles aplicas si quieres conservar tu idea y mejorar la técnica?", "La 1 y la 3", "Mejoran la claridad y la técnica sin cambiar la idea."),
    [
        ex("¿Qué es la evaluación entre pares?", "La que hacen compañeros del mismo nivel sobre el trabajo de los otros", "Aporta otra mirada."),
        ex("Verdadero o falso: debo aplicar todas las sugerencias que me den.", "Falso", "Elijo las que ayudan a mi propósito."),
        ex("¿Qué registro uso para decidir los cambios?", "Lo que me dijeron, lo que decido y por qué", "Ordena el proceso."),
    ],
    task(
        "Elige UNA situación. A) Tu trabajo muestra la calma de un lago; recibes: «aclara el fondo», «pon un volcán en erupción» y «agranda la barca». B) Tu trabajo muestra alegría en el recreo; recibes: «pon más figuras saltando», «hazlo todo gris» y «aclara el cielo». C) Tu trabajo muestra el cuidado del agua; recibes: «agranda la gota», «cambia el tema a un auto» y «usa letras más grandes». Completa la tabla (lo que me dijeron, lo que decido y por qué) y escribe una frase de autoevaluación.",
        "Elegí la A. Me dijeron «aclara el fondo»: decido aplicarlo porque ayuda a ver la calma. Me dijeron «pon un volcán en erupción»: decido no aplicarlo porque cambia mi propósito. Me dijeron «agranda la barca»: decido no aplicarlo porque quiero mostrarla pequeña en un lago enorme. Autoevaluación: mi trabajo logra la calma porque los azules y las líneas horizontales la muestran.",
        ["completa la tabla de decisiones", "decide con base en su propósito", "rechaza sugerencias con respeto y razón", "escribe una autoevaluación con evidencia"],
        ["tabla de tres columnas", "frase de autoevaluación"],
        ["aplicar todo sin pensar", "rechazar todo"],
        "Pregunta qué sugerencia fue la más útil, por qué, y cómo cambió el trabajo.",
    ),
    "Pide a una persona de tu casa un comentario sobre un dibujo tuyo y di si lo aplicarás y por qué.",
    "Escribe una evaluación a un trabajo descrito en esta unidad y compárala con la de otra persona.",
)
