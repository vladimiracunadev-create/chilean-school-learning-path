"""Student material for 2.º medio Música, OA 04 (interpretar repertorio diverso a una y más voces con conciencia estilística, aplicando medios de registro y transmisión en la gestión y difusión del quehacer musical).

Las piezas de los ejercicios son descripciones inventadas («de ejemplo»); no hay letras ni partituras con derechos.
El canto, la práctica instrumental y la grabación de audio real quedan para el docente; el cuaderno prepara la reflexión escrita.
"""
from __future__ import annotations

from student_content_mu_m2_a import L
from student_lessons import arith, ex

OA4 = "MU2M OA 04"

# ---------------------------------------------------------------- OA 04 · clase 1 (una y más voces)
L(
    OA4, 1,
    "Lápiz y papel. Las melodías y las entradas están descritas con compases en los ejercicios (son de ejemplo). Cantar a varias voces lo dirige tu docente.",
    "Aprenderé a distinguir cómo suenan una voz y varias voces (unísono, ostinato, canon y voces con líneas distintas) y a contar sus entradas. Sirve para preparar una interpretación a más de una voz sin perderse.",
    ["Reconozco melodía, acompañamiento y pulso.", "Sé qué es el unísono.", "Cuido el balance en un grupo."],
    [
        "Un repertorio se puede interpretar a una voz o a varias. A una voz hay una sola línea melódica, con o sin acompañamiento. A más voces hay varias líneas a la vez. Cuando todas cantan lo mismo suena el unísono. Un ostinato es un patrón corto que se repite muchas veces, por ejemplo un ritmo de bombo, y sirve de base a otras voces.",
        "En el canon, todas las voces cantan la misma melodía, pero cada una entra en un momento distinto. Si la melodía dura 8 compases y la segunda voz entra después de 2 compases, ambas voces se superponen. Para calcular cuántos compases dura todo, se suman a la duración de la melodía los compases que separan la entrada de la primera voz de la entrada de la última. Con tres voces que entran cada 2 compases, la tercera entra 4 compases después de la primera.",
        "También hay piezas a voces con líneas distintas: una lleva la melodía y otra canta una línea diferente que va por debajo. En ese caso lo importante es escuchar a las demás voces, entrar a tiempo con una cuenta común y cuidar el balance. Si te pierdes, no corrijas gritando: sigue el pulso y vuelve a entrar en la siguiente frase.",
    ],
    [("canon", "las voces cantan la misma melodía entrando en momentos distintos"), ("ostinato", "patrón corto que se repite muchas veces"), ("entrada", "momento en que una voz comienza a cantar"), ("compás", "grupo de pulsos que se repite; aquí se usa para contar la duración"), ("unísono", "todas las voces cantan lo mismo a la vez"), ("línea", "voz o parte independiente dentro de la pieza")],
    [
        ("Calcular el final de un canon", "Un canon de ejemplo a dos voces tiene una melodía de 6 compases. La segunda voz entra 2 compases después de la primera. ¿En qué compás termina la segunda voz, contando desde el compás 1 de la primera?", ["La segunda voz empieza dos compases después, en el compás 3.", "Su melodía dura 6 compases: desde el 3 hasta el 8."], "En el compás 8"),
        ("Reconocer un ostinato", "En una pieza de ejemplo, un cajón repite siempre el mismo patrón de cuatro golpes mientras las voces cantan estrofas distintas. ¿Qué es el patrón del cajón?", ["Es un patrón corto que se repite sin cambiar.", "Las voces cambian sobre él."], "Un ostinato"),
    ],
    [
        ("Pensar que un canon es que las voces canten cosas distintas.", "En el canon todas cantan la misma melodía, pero entran en momentos diferentes.", "Revisa que la melodía sea la misma y solo cambie la entrada."),
        ("Entrar cuando suena la voz vecina en vez de contar los compases.", "Se pierde la entrada propia y la pieza se desordena.", "Cuenta los compases y usa la cuenta común del grupo."),
    ],
    [
        ex("¿Qué es un ostinato? A) Un patrón corto que se repite muchas veces. B) Un cambio de tempo.", "A", "Es una base repetida."),
        ex("¿Cómo se llama cuando todas las voces cantan lo mismo a la vez? A) Unísono. B) Canon.", "A", "Es el unísono."),
        ex("En un canon, ¿qué diferencia a las voces? A) El momento en que entran. B) La melodía que cantan.", "A", "Cantan la misma melodía en tiempos distintos."),
    ],
    [
        ex("Una melodía de ejemplo de 8 compases se canta en canon a dos voces; la segunda entra 2 compases después. ¿En qué compás termina la segunda voz? A) 10. B) 8.", "A", "Empieza en el compás 3 y dura 8 compases: termina en el 10."),
        ex("¿Qué debe hacer una voz que se pierde? A) Seguir el pulso y volver a entrar en la siguiente frase. B) Cantar más fuerte para recuperar.", "A", "Volver con calma evita desordenar al grupo."),
        ex("¿Qué se necesita para entrar a tiempo a varias voces? A) Una cuenta común y escuchar a las otras voces. B) Mirar solo la propia parte.", "A", "La entrada exige coordinación."),
    ],
    [
        arith("Un canon de ejemplo tiene una melodía de 8 compases y tres voces que entran cada 2 compases. ¿Cuántos compases dura el canon completo, desde que empieza la primera voz hasta que termina la tercera?", "8+2*2", "La tercera entra 4 compases después de la primera y su melodía dura 8.", " compases"),
        ex("Una pieza de ejemplo tiene un ostinato de bombo y una voz que cambia de frase. ¿Qué voz se mantiene siempre igual? A) El bombo. B) La voz.", "A", "El ostinato no cambia."),
        ex("Dos voces cantan la misma frase y, al mismo tiempo, una tercera canta otra línea más grave. ¿Qué se oye? A) Dos voces en unísono y una línea distinta. B) Un canon de tres voces.", "A", "No hay entradas desfasadas de la misma melodía."),
    ],
    [
        ex("Un grupo canta un canon, pero la segunda voz empieza cuando la primera ya va en el compás 4 en lugar del 3 acordado. ¿Qué efecto tiene? A) La segunda voz termina un compás más tarde de lo acordado. B) La segunda voz termina antes.", "A", "Entrar un compás más tarde corre todo su final un compás."),
        ex("Una estudiante dice: «En el canon, si no escucho a las otras voces me da igual.» ¿Qué responde un compañero? A) Escuchar ayuda a mantener el pulso y a entrar a tiempo. B) Tiene razón, solo cuenta la propia voz.", "A", "La coordinación depende de escuchar."),
    ],
    [
        ex("Un coro de ejemplo tiene tres secciones y quiere cantar un canon con una entrada cada 4 compases. ¿Qué compás señala la entrada de la tercera sección? A) 9. B) 5.", "A", "La primera entra en el 1, la segunda en el 5 y la tercera en el 9."),
        ex("Una persona canta un ostinato muy fuerte y tapa la melodía principal. ¿Qué corrección conviene? A) Bajar el volumen del ostinato. B) Cantar el ostinato más rápido.", "A", "El ostinato sostiene, no tapa."),
    ],
    [ex("En un taller escolar quieren cantar a dos voces con un grupo mixto, pero algunas personas no se sienten seguras. ¿Qué opción mantiene la participación? A) Ofrecer roles equivalentes, como ostinato corporal o unísono. B) Obligar a quienes dudan a cantar en solitario.", "A", "Se respeta la comodidad sin perder el objetivo.")],
    [
        ex("¿Verdadero o falso? En un canon todas las voces cantan la misma melodía.", "Verdadero", "Solo cambia el momento de entrada."),
        ex("Una melodía de 4 compases se canta en canon a dos voces con entrada 1 compás después. ¿Cuántos compases dura todo? A) 5. B) 4.", "A", "La segunda termina un compás después de la primera."),
        ex("¿Qué es una línea? A) Una voz o parte independiente. B) Un tipo de instrumento.", "A", "Es una parte de la pieza."),
    ],
    (
        "Pieza de ejemplo: un canon a tres voces con una melodía de 6 compases en el que cada voz entra 2 compases después de la anterior. Escribe: a) el compás de entrada de cada voz (la primera entra en el compás 1), b) el compás en que termina la tercera voz, c) una indicación para no perderse.",
        "a) Voz 1: compás 1; voz 2: compás 3; voz 3: compás 5. b) La tercera entra en el 5 y dura 6 compases: termina en el compás 10. c) Contar los compases y volver a entrar en la frase siguiente si me pierdo.",
        ["entradas correctas en 1, 3 y 5", "final correcto con el cálculo", "indicación de escucha y cuenta"],
        ["respuestas a), b) y c) con el cálculo"],
        ["contar mal el compás de término", "no usar una cuenta común"],
        "Reconoce el canon y pide revisar el compás final contando uno a uno.",
    ),
    "Canta con una persona de tu casa una canción que ambas conozcan, una en unísono y otra marcando un ritmo repetido, y anota qué diferencia se oye.",
    "Inventa una melodía de 4 compases (descríbela con palabras) y calcula cuántos compases dura un canon a tres voces con entrada cada compás.",
)

# ---------------------------------------------------------------- OA 04 · clase 2 (conciencia estilística)
L(
    OA4, 2,
    "Lápiz y papel. Las piezas y sus estilos están descritos en los ejercicios (son de ejemplo). La escucha de modelos reales la selecciona tu docente.",
    "Aprenderé a identificar los rasgos de estilo de una pieza y a decidir cómo interpretarla con conciencia estilística. Sirve para cantar o tocar una pieza de modo coherente con su carácter y no solo copiarla.",
    ["Describo tempo, dinámica y articulación.", "Reconozco tradición oral, escrita y popular.", "Interpreto a una y más voces."],
    [
        "Tener conciencia estilística es saber qué rasgos dan carácter a una pieza y hacerlos sonar al interpretarla. Entre los rasgos están: el tempo, la dinámica, la articulación, los adornos (notas rápidas que decoran la melodía), el timbre de la voz o del instrumento, el modo de acentuar las sílabas y el grado de libertad con que se varía una frase.",
        "Cada estilo trae sus costumbres. Una canción de cuna de tradición oral se canta suave, con pocos adornos y tempo lento. Una pieza de baile popular marca los pulsos y usa timbres brillantes. Una pieza escrita para coro suele pedir afinación cuidada y dinámicas indicadas en la partitura. Estas son tendencias, no reglas fijas: dentro de cada estilo hay variantes.",
        "Interpretar con conciencia estilística no es imitar a un cantante o a un grupo en particular. Primero se escucha, se anotan los rasgos de estilo y se decide cuáles hacer sonar con la propia voz y los propios recursos. Luego se prueban dos versiones y se compara cuál se acerca más al carácter buscado.",
    ],
    [("estilo", "conjunto de rasgos que dan carácter a una pieza"), ("adorno", "notas rápidas que decoran una melodía"), ("conciencia estilística", "saber qué rasgos dan carácter a una pieza y hacerlos sonar"), ("acentuar", "dar más fuerza a ciertas sílabas o notas"), ("variante", "versión distinta de una misma pieza"), ("timbre", "color propio del sonido de una voz o instrumento")],
    [
        ("Elegir rasgos según el estilo", "Una pieza de ejemplo es una canción de cuna de tradición oral. ¿Qué tempo y qué dinámica son más adecuados?", ["La canción busca calmar.", "El tempo lento y la dinámica suave calman."], "Tempo lento y dinámica suave"),
        ("Comparar dos versiones", "Versión 1 de ejemplo: marca los pulsos con fuerza y usa un timbre brillante. Versión 2 de ejemplo: canta suave, sin acentuar los pulsos. Una pieza de baile popular, ¿con cuál versión se acerca más a su estilo?", ["El baile necesita pulso marcado.", "La versión 1 marca los pulsos."], "La versión 1"),
    ],
    [
        ("Interpretar todas las piezas con el mismo tempo y la misma voz.", "Se pierde el carácter propio de cada estilo.", "Antes de cantar, anota los rasgos del estilo y decide cuáles usar."),
        ("Pensar que interpretar con estilo es copiar a un artista exacto.", "La copia ignora la voz y los recursos propios.", "Toma los rasgos y adáptalos."),
    ],
    [
        ex("¿Qué es conciencia estilística? A) Saber qué rasgos dan carácter a una pieza y hacerlos sonar. B) Cantar siempre fuerte.", "A", "Es el conocimiento y uso de los rasgos."),
        ex("¿Qué es un adorno? A) Notas rápidas que decoran la melodía. B) Un silencio largo.", "A", "Decora sin cambiar la melodía base."),
        ex("Una pieza de ejemplo es una canción de cuna. ¿Qué dinámica es adecuada? A) Suave. B) Muy fuerte.", "A", "La canción de cuna debe calmar."),
    ],
    [
        ex("¿Qué se hace antes de interpretar con estilo? A) Escuchar y anotar los rasgos. B) Memorizar la letra solamente.", "A", "El análisis guía la decisión."),
        ex("Una pieza de baile popular de ejemplo se canta con tempo muy lento y sin marcar pulsos. ¿Qué pasa? A) Pierde su carácter de baile. B) Gana carácter de baile.", "A", "El baile necesita pulso claro."),
        ex("¿Por qué los estilos son tendencias y no reglas fijas? A) Porque dentro de cada estilo hay variantes. B) Porque cada persona inventa el estilo que quiere.", "A", "Hay versiones distintas."),
    ],
    [
        ex("Una intérprete quiere cantar una pieza coral con una voz muy brillante como la de un cantante famoso. ¿Qué decisión es consciente del estilo? A) Mantener la afinación cuidada que pide la pieza y adaptar el timbre de su voz. B) Imitar el timbre del cantante aunque dañe la voz.", "A", "Cuida el estilo y la voz."),
        ex("¿Qué conviene hacer al comparar dos versiones propias de una pieza? A) Escuchar ambas y elegir cuál se acerca más al carácter buscado. B) Escoger la más rápida.", "A", "La elección sigue el carácter."),
        ex("Dos versiones de una pieza de ejemplo: una con muchos adornos y otra sin adornos. La pieza pide sencillez. ¿Cuál se acerca más? A) La sin adornos. B) La con muchos adornos.", "A", "La sencillez pide pocos adornos."),
    ],
    [
        ex("Un compañero dice: «Cantaré esa canción igual que mi artista favorito.» Otro dice: «Anotaré sus rasgos y usaré los que mi voz pueda hacer.» ¿Qué postura muestra conciencia estilística? A) La del segundo. B) La del primero.", "A", "El segundo analiza y adapta."),
        ex("Una canción de ejemplo se canta con humor. ¿Qué rasgo de estilo ayuda a mostrarlo? A) Acentuar con juego las sílabas y variar la dinámica. B) Mantener siempre el mismo volumen.", "A", "La expresividad exige variación."),
    ],
    [
        ex("En un ensayo se acuerdan tres rasgos de estilo: tempo medio, dinámica suave y pocos adornos. Una intérprete agrega muchos adornos. ¿Qué observación es correcta? A) Contradice el estilo acordado. B) Mejora el estilo siempre.", "A", "Se aparta de lo acordado."),
        ex("¿Qué pasa si se interpreta un canto de trabajo en el campo con un timbre de estudio muy pulido? A) Puede perder el carácter directo del estilo. B) Nunca cambia su carácter.", "A", "El carácter depende del contexto."),
    ],
    [ex("Para un acto escolar quieres cantar una canción de cuna de ejemplo sin que suene como una marcha. ¿Qué haces? A) Bajar el tempo, cantar suave y evitar acentos fuertes. B) Subir el volumen para que se oiga.", "A", "Ajustas los rasgos al carácter.")],
    [
        ex("¿Verdadero o falso? Cada estilo tiene rasgos que se pueden escuchar y describir.", "Verdadero", "Los rasgos son audibles."),
        ex("¿Qué es una variante? A) Una versión distinta de una misma pieza. B) Un error al cantar.", "A", "Hay variantes dentro de un estilo."),
        ex("¿Qué es el timbre? A) El color propio del sonido. B) La rapidez del pulso.", "A", "Se refiere al color del sonido."),
    ],
    (
        "Elige una pieza de ejemplo de una tradición (cuna, baile, trabajo, coral o canción de homenaje) y escribe: a) tres rasgos de estilo que la caracterizan (tempo, dinámica, articulación, adornos o timbre), b) cómo los harías sonar con tu voz, c) una decisión de adaptación a tus recursos.",
        "Pieza: canción de cuna. a) Tempo lento, dinámica suave, pocos adornos. b) Cantaría bajito, alargando las frases y sin acentos fuertes. c) Bajaría una nota si la más aguda me resulta difícil.",
        ["tres rasgos coherentes con la pieza", "cómo interpretarlos con los propios recursos", "una adaptación que cuide la voz"],
        ["respuestas a), b) y c) escritas"],
        ["copiar a un artista sin adaptar", "elegir rasgos que contradicen el carácter"],
        "Reconoce los rasgos y pide justificar con una frase cómo la voz propia los puede hacer sonar.",
    ),
    "Escucha dos canciones de estilos distintos y anota dos rasgos de cada una.",
    "Prueba cantar una frase de dos formas (suave y marcada) y explica cuál cuadra mejor con un estilo que elijas.",
)

# ---------------------------------------------------------------- OA 04 · clase 3 (medios de registro)
L(
    OA4, 3,
    "Lápiz y papel. Los medios de registro están descritos en los ejercicios. Grabaciones y partituras reales las aporta tu docente; el audio no se incluye en este cuaderno.",
    "Aprenderé qué medios sirven para registrar una música (partitura, tablatura, notación gráfica, grabación de audio y video) y qué conserva cada uno. Sirve para elegir cómo dejar constancia de mi quehacer musical.",
    ["Sé qué es una partitura.", "Interpreto a una y más voces.", "Describo rasgos de estilo."],
    [
        "Registrar una música es dejarla guardada para volver a ella. Hay varios medios. La partitura registra las alturas y las duraciones de las notas con signos convencionales. La tablatura indica en qué cuerda y traste de la guitarra se toca. La notación gráfica usa dibujos o símbolos acordados por el grupo. El texto con acordes anota la letra con las cifras de acordes sobre las palabras. La grabación de audio conserva el sonido real, y el video suma gestos y escenario.",
        "Cada medio conserva algo y pierde algo. La partitura permite recrear la pieza, pero no conserva el timbre exacto ni los adornos que dependían de la intérprete. La grabación conserva ese timbre y esa interpretación, pero no muestra cómo se escribió ni facilita cambiarla. La notación gráfica es flexible, pero requiere un acuerdo previo para leerse igual. Por eso muchas veces se combinan: una partitura sencilla más una grabación de referencia.",
        "Elegir el medio depende del propósito: si se quiere que otro grupo toque la pieza, sirve la partitura o la tablatura; si se quiere conservar una interpretación, la grabación; si se quiere explicar una idea, el video. También hay que cuidar la calidad: una grabación con ruido ambiente o saturada pierde valor como registro.",
    ],
    [("registro", "forma de dejar guardada una música"), ("partitura", "escritura musical con signos convencionales para alturas y duraciones"), ("tablatura", "escritura que indica cuerda y traste en la guitarra"), ("notación gráfica", "dibujos o símbolos acordados para anotar una música"), ("grabación", "registro del sonido real"), ("medio", "soporte o vía para registrar o transmitir")],
    [
        ("Elegir el medio según el propósito", "Un grupo de ejemplo quiere que otro curso toque su pieza en una flauta dulce, sin necesidad de oírlos. ¿Qué medio conviene?", ["Se necesita saber las notas y duraciones.", "La partitura las registra."], "La partitura"),
        ("Qué conserva cada medio", "Una cantante de ejemplo quiere dejar constancia de cómo suena su voz en una versión. ¿Qué medio es mejor?", ["Quiere conservar el sonido real.", "La grabación de audio lo conserva."], "La grabación de audio"),
    ],
    [
        ("Creer que la partitura conserva todo lo que se oye en una interpretación.", "No conserva el timbre exacto ni los adornos propios de la intérprete.", "Complementa con una grabación o una nota escrita sobre el estilo."),
        ("Pensar que cualquier grabación sirve como registro.", "Una grabación con ruido o muy fuerte pierde detalle.", "Cuida el lugar, el volumen y la distancia al grabar."),
    ],
    [
        ex("¿Qué registra una partitura? A) Alturas y duraciones con signos convencionales. B) El timbre exacto de una voz.", "A", "Eso es lo que conserva la partitura."),
        ex("¿Qué medio indica cuerda y traste en la guitarra? A) La tablatura. B) La notación gráfica.", "A", "Es la función de la tablatura."),
        ex("¿Qué medio conserva el sonido real de una interpretación? A) La grabación de audio. B) El texto con acordes.", "A", "La grabación conserva el sonido."),
    ],
    [
        ex("Un grupo quiere registrar una idea que aún no tiene notas fijas, solo gestos y sonidos acordados. ¿Qué medio conviene? A) Notación gráfica. B) Partitura convencional.", "A", "La notación gráfica es flexible."),
        ex("¿Qué pierde una partitura frente a una grabación? A) El timbre y los adornos de una intérprete concreta. B) Las notas de la melodía.", "A", "La partitura no fija el timbre."),
        ex("¿Por qué se combinan medios? A) Porque cada uno conserva cosas distintas. B) Porque todos conservan lo mismo.", "A", "La combinación completa el registro."),
    ],
    [
        ex("Una persona quiere compartir cómo se baila una pieza de ejemplo y cómo suena. ¿Qué medio es más completo? A) Video con sonido. B) Solo texto con acordes.", "A", "El video suma gestos y sonido."),
        ex("Una grabación de ejemplo se hizo junto a una calle muy ruidosa. ¿Qué problema tiene como registro? A) Pierde detalle por el ruido ambiente. B) Cambia el tempo de la pieza.", "A", "El ruido tapa el sonido."),
        ex("Otro curso quiere tocar una pieza escrita con guitarra y no sabe leer partitura, pero sí tablatura. ¿Qué registro necesita? A) Una tablatura. B) Una notación gráfica nueva.", "A", "Es el sistema que conoce."),
    ],
    [
        ex("Una estudiante dice: «Con la partitura ya tengo la interpretación exacta.» ¿Qué corrección es correcta? A) La partitura guía, pero el timbre y los adornos dependen de quien interpreta. B) La partitura incluye cada detalle del sonido.", "A", "La partitura no fija todo."),
        ex("Un grupo graba una interpretación y pierde el papel donde anotó la letra con acordes. ¿Qué podría hacer para volver a tocar la pieza? A) Escuchar la grabación y volver a anotar el texto con acordes. B) Pedir a otro grupo que invente la pieza de nuevo.", "A", "La grabación sirve de apoyo."),
    ],
    [
        ex("Para dejar registrada una canción de tradición oral de tu comunidad, con permiso de quienes la cantan, ¿qué combinación es más útil? A) Una grabación de referencia y una anotación escrita del texto o de la melodía. B) Solo una foto del lugar.", "A", "Combina sonido y escritura."),
        ex("Un grupo quiere registrar su pieza de 3 minutos en tomas de 3 minutos y hace 4 tomas. ¿Cuántos minutos de grabación tendrá en total? A) 12. B) 7.", "A", "4 tomas × 3 minutos son 12 minutos."),
    ],
    [ex("Tu curso hace un archivo de música escolar. ¿Qué decisión es mejor? A) Guardar la partitura sencilla y una grabación de referencia de cada pieza. B) Guardar solo el título de cada pieza.", "A", "Así se conserva escritura y sonido.")],
    [
        ex("¿Verdadero o falso? Cada medio de registro conserva cosas distintas.", "Verdadero", "Ninguno conserva todo."),
        ex("¿Qué es la notación gráfica? A) Dibujos o símbolos acordados para anotar una música. B) Una grabación en video.", "A", "Es un medio flexible."),
        ex("¿Qué se cuida para que una grabación sirva como registro? A) Lugar silencioso y volumen sin saturar. B) Que sea muy corta.", "A", "Evita ruido y distorsión."),
    ],
    (
        "Tu grupo debe registrar una canción de ejemplo de tres estrofas para otro curso que no la conoce. Escribe: a) dos medios que usarías y qué conserva cada uno, b) qué se perdería si usaras solo uno, c) una medida para cuidar la calidad del registro.",
        "a) Texto con acordes (conserva letra y armonía) y grabación de audio (conserva el sonido y el estilo). b) Solo el texto no muestra el estilo, y solo la grabación no permite leer los acordes. c) Grabar en un lugar silencioso y sin saturar el volumen.",
        ["dos medios con lo que conserva cada uno", "una pérdida explicada si se usa solo uno", "una medida de calidad concreta"],
        ["respuestas a), b) y c) escritas"],
        ["afirmar que un medio conserva todo", "no relacionar el medio con el propósito"],
        "Reconoce los medios y pide explicar qué se pierde con uno solo.",
    ),
    "Anota qué medios de registro hay en tu casa o en tu curso para música y qué conserva cada uno.",
    "Elige una canción de tu zona y escribe qué medio usarías para que otra persona pueda aprenderla y por qué.",
)

# ---------------------------------------------------------------- OA 04 · clase 4 (grabar una toma con método)
L(
    OA4, 4,
    "Lápiz y papel. El registro real de audio o video lo hace el grupo con ayuda de tu docente; aquí se practica la planificación y los cálculos.",
    "Aprenderé a preparar y registrar una interpretación con método: lugar, volumen, cuenta de entrada, varias tomas y nombre de archivo. Sirve para dejar un registro claro de mi quehacer musical.",
    ["Conozco medios de registro.", "Interpreto a una y más voces.", "Dirijo entradas con cuenta previa."],
    [
        "Para registrar una interpretación se prepara el espacio y el equipo. Se elige un lugar con poco ruido, se coloca el micrófono o el celular a una distancia que capte bien todas las voces, y se prueba el volumen para que el sonido no se sature (no suene distorsionado). A volumen seguro se protege el oído de todo el grupo.",
        "Antes de grabar se acuerdan la cuenta de entrada (por ejemplo cuatro pulsos), el orden de las secciones y la señal de corte. Se hacen varias tomas, cada una desde el comienzo, y se escuchan para elegir la mejor. En una toma se evita parar a mitad: si hay un error pequeño, se sigue, porque una toma completa muestra mejor la fluidez. Cada archivo se nombra con claridad: título de la pieza y número de toma, por ejemplo «cancion_toma2» (se puede sumar la fecha).",
        "Para calcular el tiempo de una sesión se suma la preparación, la duración de cada toma y el tiempo para escuchar. También se revisa el espacio en el dispositivo y la batería. Si en la grabación aparecen voces de personas ajenas al grupo, se pide permiso antes de guardarla o compartirla.",
    ],
    [("toma", "una grabación completa de la pieza"), ("saturar", "subir tanto el volumen que el sonido se distorsiona"), ("cuenta de entrada", "pulsos que se marcan antes de empezar"), ("sesión", "periodo de trabajo de grabación"), ("archivo", "registro guardado con un nombre"), ("distorsión", "sonido deformado por exceso de volumen")],
    [
        ("Calcular una sesión", "Una sesión de ejemplo incluye 10 minutos de preparación, 3 tomas de 4 minutos cada una y 8 minutos para escucharlas. ¿Cuántos minutos dura la sesión?", ["Las tomas suman 3 × 4 = 12 minutos.", "Se suman preparación, tomas y escucha: 10 + 12 + 8."], "30 minutos"),
        ("Nombrar un archivo", "Un grupo graba la cuarta toma de una pieza llamada «canon». ¿Qué nombre de archivo es claro?", ["Debe incluir la pieza y el número de toma.", "Un nombre sin datos no se encuentra después."], "canon_toma4"),
    ],
    [
        ("Subir el volumen al máximo para que la grabación «se oiga».", "El sonido se satura y se distorsiona; además daña el oído.", "Ajusta el volumen para que el sonido sea nítido y sin distorsión."),
        ("Detener la toma y empezar de nuevo en cada error pequeño.", "Se pierde la continuidad y no se ve la fluidez de la pieza.", "Sigue hasta el final y elige la mejor toma después."),
    ],
    [
        ex("¿Qué significa saturar? A) Subir tanto el volumen que el sonido se distorsiona. B) Bajar el volumen a cero.", "A", "Saturar es exceder el volumen."),
        ex("¿Para qué sirve la cuenta de entrada? A) Para empezar juntos al mismo tempo. B) Para terminar la pieza.", "A", "Marca el tempo de comienzo."),
        ex("¿Qué es una toma? A) Una grabación completa de la pieza. B) El micrófono que se usa.", "A", "Es una grabación completa."),
    ],
    [
        ex("¿Por qué hacer varias tomas? A) Para elegir la mejor al escucharlas. B) Para que cada toma dure más.", "A", "Permite comparar y elegir."),
        ex("¿Qué lugar es mejor para grabar? A) Uno con poco ruido. B) Un patio con mucho tránsito.", "A", "El ruido tapa el sonido."),
        ex("¿Por qué conviene nombrar los archivos con claridad? A) Para encontrarlos después. B) Para que suenen más fuerte.", "A", "El nombre permite ubicarlos."),
    ],
    [
        arith("Una sesión de ejemplo incluye 5 minutos de preparación, 4 tomas de 3 minutos y 7 minutos para escucharlas. ¿Cuántos minutos dura?", "5+4*3+7", "Se suman preparación, tomas y escucha.", " minutos"),
        ex("Una toma de ejemplo tiene un pequeño error de entrada en un compás, pero sigue hasta el final con buen pulso. ¿Qué conviene hacer? A) Guardarla y compararla con otras tomas. B) Borrarla de inmediato sin escucharla.", "A", "Una toma completa tiene valor de comparación."),
        ex("Nombra el archivo de la segunda toma de una pieza de ejemplo llamada «homenaje». A) homenaje_toma2. B) toma.", "A", "Incluye pieza y número de toma."),
    ],
    [
        ex("En la sesión, el volumen de la guitarra satura el micrófono. ¿Qué se corrige? A) Alejar el micrófono o bajar el volumen de la guitarra. B) Subir más el volumen.", "A", "Evita la distorsión."),
        ex("Una toma tiene el sonido de otras personas que hablan cerca. ¿Qué paso corresponde antes de compartirla? A) Pedir permiso o volver a grabar sin esas voces. B) Compartirla igual.", "A", "Se cuida el consentimiento."),
    ],
    [
        ex("Una sesión de 20 minutos usa 6 en la preparación, 10 para dos tomas de igual duración y el resto para escuchar. ¿Cuánto dura cada toma y cuánto queda para escuchar? A) 5 minutos por toma y 4 para escuchar. B) 10 minutos por toma y 4 para escuchar.", "A", "10 minutos entre dos tomas dan 5 cada una; 20 − 6 − 10 = 4."),
        ex("El celular del grupo tiene poca batería. ¿Qué decisión es adecuada antes de grabar? A) Cargarlo o usar otro dispositivo. B) Esperar que alcance.", "A", "Evita perder la toma."),
    ],
    [ex("Tu curso quiere grabar una canción para una feria. ¿Qué plan es más completo? A) Lugar silencioso, cuenta de entrada acordada, tres tomas y archivos con nombre claro. B) Una sola toma sin probar volumen.", "A", "Contiene los pasos clave.")],
    [
        ex("¿Verdadero o falso? Una toma con un error pequeño debe detenerse siempre.", "Falso", "Conviene seguir y comparar."),
        ex("¿Qué se revisa antes de grabar? A) Espacio y batería del dispositivo. B) El color del micrófono.", "A", "Así se evitan cortes en la toma."),
        ex("¿Qué se acuerda antes de grabar? A) Cuenta de entrada, orden y señal de corte. B) Solo el título.", "A", "Es la organización mínima."),
    ],
    (
        "Planifica una sesión de ejemplo para registrar una canción a dos voces: escribe a) los pasos que seguirás desde el lugar hasta guardar el archivo, b) cuánto dura la sesión si hay 7 minutos de preparación, 3 tomas de 5 minutos y 6 minutos de escucha, c) el nombre de archivo de la mejor toma si fue la segunda de la canción «viento».",
        "a) Elegir lugar silencioso, probar volumen, acordar cuenta de entrada y corte, hacer las tomas, escucharlas y nombrar el archivo. b) 7 + 3 × 5 + 6 = 28 minutos. c) viento_toma2.",
        ["pasos ordenados de la preparación al archivo", "cálculo correcto de la sesión", "nombre de archivo claro"],
        ["respuestas a), b) y c) escritas"],
        ["olvidar probar el volumen", "sumar mal las tomas"],
        "Reconoce el plan y pide revisar el cálculo de la sesión.",
    ),
    "Revisa en tu casa o en el colegio un lugar silencioso y anota qué ruidos oyes durante un minuto.",
    "Escribe una lista de revisión de cinco puntos para antes de grabar a tu grupo.",
)

# ---------------------------------------------------------------- OA 04 · clase 5 (registrar, contrastar versiones y difundir)
L(
    OA4, 5,
    "Lápiz y papel. Las versiones y los medios de difusión están descritos en los ejercicios. La audición real de las tomas y la publicación la gestiona tu docente.",
    "Aprenderé a contrastar dos versiones de una interpretación y a decidir cómo difundirla con respeto a la autoría y con cuidado de las personas. Sirve para gestionar mi quehacer musical de forma responsable.",
    ["Conozco medios de registro.", "Planifico una toma.", "Interpreto con conciencia estilística."],
    [
        "Contrastar dos versiones es compararlas con los mismos criterios. Se escucha cada una y se anota, para cada criterio, lo que se oye: pulso estable, entradas a tiempo, balance entre voces, afinación, fluidez y carácter de estilo. Después se decide cuál comunica mejor el propósito. La decisión se apoya en lo que se escuchó y no en cuál es más fuerte o más rápida.",
        "Difundir es hacer conocida una música. Antes hay que elegir el medio según la audiencia y el propósito: una muestra presencial en el colegio, una grabación para el archivo del curso o un video en un espacio en línea acordado con la persona docente. La difusión exige cuidar a las personas: se pide permiso a quienes aparecen o suenan, no se publican datos personales y, si alguien recibe comentarios hostiles, se avisa a una persona adulta de confianza en lugar de responder solo o discutir.",
        "También se cuida la autoría. Si la pieza es de otra persona, se indica su nombre y se pide autorización para difundir versiones cuando corresponde. Si la pieza es de tradición oral de una comunidad, se consulta a quienes la cantan y se acuerda cómo presentarla. Una buena gestión incluye un programa claro con el orden de las piezas y su duración total.",
    ],
    [("contrastar", "comparar dos cosas para ver sus diferencias"), ("criterio", "pauta que se usa para comparar o juzgar"), ("difundir", "hacer conocida una música"), ("audiencia", "personas a quienes se dirige una música"), ("autoría", "reconocimiento de quien creó una pieza"), ("programa", "lista ordenada de piezas con su duración")],
    [
        ("Contrastar con criterios", "Versión A de ejemplo: pulso estable y voces equilibradas, pero con una entrada tarde en el estribillo. Versión B de ejemplo: pulso que se acelera y voces desequilibradas. Para un acto de bienvenida, ¿cuál conviene difundir?", ["A tiene dos criterios logrados y un error corregible.", "B falla en pulso y balance."], "La versión A"),
        ("Armar un programa", "Programa de ejemplo con tres piezas: una de 3 minutos, otra de 4 y otra de 5, con pausas de 1 minuto entre ellas. ¿Cuánto dura el programa completo?", ["Las piezas suman 3 + 4 + 5 = 12.", "Hay dos pausas entre tres piezas: 2 minutos."], "14 minutos"),
    ],
    [
        ("Elegir la versión que suena más fuerte o más rápida.", "La fuerza y la velocidad no miden la calidad.", "Compara con criterios audibles y propósito."),
        ("Publicar una grabación sin preguntar a quienes participaron.", "Se vulnera su derecho a decidir si su voz o su imagen se difunden.", "Pide permiso y acuerda el medio con el grupo y la persona docente."),
    ],
    [
        ex("¿Qué es difundir una música? A) Hacerla conocida. B) Guardarla sin mostrarla a nadie.", "A", "Difundir es dar a conocer."),
        ex("¿Qué se hace antes de publicar una grabación grupal? A) Pedir permiso a quienes suenan o aparecen. B) Cambiar los nombres de los archivos.", "A", "Se respeta a las personas."),
        ex("¿Qué es una audiencia? A) Las personas a quienes se dirige una música. B) El lugar donde se ensaya.", "A", "Es el público."),
    ],
    [
        ex("Al contrastar dos versiones, ¿qué se usa? A) Los mismos criterios en ambas. B) Un criterio distinto para cada una.", "A", "Para comparar hace falta un criterio común."),
        ex("Una pieza es de otra persona. ¿Qué se hace al difundir tu versión? A) Indicar su autoría y pedir autorización cuando corresponde. B) Presentarla como propia.", "A", "Se cuida la autoría."),
        ex("Una canción de tradición oral de una comunidad se quiere difundir. ¿Qué paso corresponde? A) Consultar a quienes la cantan y acordar cómo presentarla. B) Presentarla como creación del curso.", "A", "Se respeta a la comunidad."),
    ],
    [
        arith("Un programa de ejemplo tiene cuatro piezas de 2, 3, 3 y 4 minutos, sin pausas. ¿Cuántos minutos dura?", "2+3+3+4", "Se suman las duraciones de las piezas.", " minutos"),
        ex("Versión 1 de ejemplo: muy rápida y con todas las entradas desordenadas. Versión 2: tempo medio y todas las entradas a tiempo. Para una muestra, ¿cuál conviene? A) La versión 2. B) La versión 1, porque es más rápida.", "A", "La rapidez no mide calidad."),
        ex("Un grupo duda entre publicar su grabación en un espacio abierto o solo mostrarla en el curso. ¿Qué pregunta ayuda a decidir? A) ¿Quiénes aparecen y están de acuerdo con la audiencia? B) ¿Cuántos «me gusta» tendrá?", "A", "El consentimiento guía la difusión."),
    ],
    [
        ex("Tras publicar un video escolar, una estudiante recibe comentarios que la humillan. ¿Qué es lo más adecuado? A) Avisar a una persona adulta de confianza y no responder sola. B) Responder uno por uno para defenderse.", "A", "Se pide ayuda y se evita la escalada."),
        ex("Un compañero dice: «Mi versión es mejor porque suena más alto.» ¿Qué responde bien otra persona? A) Compararlas por pulso, entradas y balance. B) Aceptar el volumen como único criterio.", "A", "El volumen no es criterio de calidad."),
    ],
    [
        ex("El programa de ejemplo de un acto debe durar a lo más 15 minutos e incluye piezas de 5, 4 y 4 minutos. ¿Cabe? A) Sí, dura 13 minutos. B) No, dura 17 minutos.", "A", "5 + 4 + 4 = 13, menos de 15."),
        ex("Si te sientes muy nervioso o con angustia ante mostrar tu música, ¿qué conviene? A) Conversarlo con tu docente o con una persona adulta de confianza y elegir un rol con menos exposición. B) Callarlo y obligarte.", "A", "Se busca apoyo y alternativas."),
    ],
    [ex("Tu curso grabó una pieza en dos versiones y debe elegir para el archivo escolar. ¿Qué proceso es mejor? A) Escuchar ambas con la misma pauta, registrar lo que se oye y elegir según el propósito. B) Elegir al azar.", "A", "Combina criterio, evidencia y propósito.")],
    [
        ex("¿Verdadero o falso? Se debe pedir permiso a las personas que aparecen en una grabación antes de difundirla.", "Verdadero", "Se respeta su decisión."),
        ex("¿Qué incluye un buen programa? A) El orden de las piezas y la duración total. B) Solo los nombres de los integrantes.", "A", "Facilita la organización."),
        ex("¿Qué NO conviene publicar junto con un video escolar? A) Datos personales como direcciones. B) El título de la pieza.", "A", "Los datos personales no deben publicarse."),
    ],
    (
        "Versión A de ejemplo (3 minutos): pulso parejo, balance bueno, estribillo con dinámica suave. Versión B de ejemplo (4 minutos): pulso que se acelera y voces que se tapan. Escribe: a) una tabla de dos filas con los criterios pulso, balance y carácter para cada versión, b) cuál elegirías para difundir y por qué, c) dos cuidados que tendrías antes de publicar.",
        "a) A: pulso parejo, balance bueno, carácter suave logrado. B: pulso acelerado, voces tapadas, carácter poco claro. b) Elegiría A porque cumple los criterios y el propósito de calmar. c) Pedir permiso a las personas que suenan y no publicar datos personales.",
        ["compara con los mismos criterios", "elige según criterios y propósito", "dos cuidados concretos de difusión"],
        ["tabla o lista con criterios", "decisión justificada y dos cuidados"],
        ["elegir por volumen o rapidez", "olvidar el permiso de las personas"],
        "Reconoce la comparación y pide agregar un cuidado más sobre autoría o privacidad.",
    ),
    "Escucha dos versiones de una canción que conozcas y anota una diferencia en pulso, otra en balance y otra en carácter.",
    "Redacta una breve nota para pedir permiso a las personas de tu grupo antes de compartir una grabación.",
)
