"""Student material for 4.º básico Música, OA 03 (escucha abundante de músicas de diversos contextos) y OA 04 (canto e interpretación instrumental coordinada).

Todas las músicas de los ejercicios son descripciones originales ficticias; las audiciones reales las selecciona el docente.
"""
from __future__ import annotations

from student_content_mu4_a import L
from student_lessons import arith, ex

OA3, OA4 = "MU04 OA 03", "MU04 OA 04"

# ---------------------------------------------------------------- OA 03 · clase 1
FICHAS1 = (
    "Pieza 1, «Amanecer en el lago»: escrita en partitura por una compositora para un cuarteto de cuerdas; con sonidos que suben poco a poco imita la salida del sol. "
    "Pieza 2, «Marcha de los aprendices»: escrita en partitura para una banda; marca un pulso firme para desfilar. "
    "Pieza 3, «Paseo entre cuadros»: escrita en partitura para orquesta; cada una de sus 5 partes describe un cuadro distinto."
)

L(
    OA3, 1,
    f"Lápiz y papel. Las piezas están descritas por escrito (son ejemplos inventados para esta clase), así que no necesitas audio. Fichas de trabajo: {FICHAS1}",
    "Aprenderé a escuchar música de tradición escrita (docta) y a ubicarla en su contexto: quién la creó, para qué agrupación y qué quiere mostrar. Sirve para escuchar con más atención y más respeto.",
    ["Sé escuchar en silencio y por turnos.", "Sé nombrar cualidades del sonido.", "Sé qué es un instrumento musical."],
    [
        "La tradición escrita, también llamada música docta, es la música que una persona compone y escribe en una partitura. Gracias a la partitura, otras personas pueden tocarla de nuevo igual, aunque pasen muchos años. Quien la crea se llama compositor o compositora. Se escribe para distintas agrupaciones: un dúo son 2 intérpretes, un trío son 3, un cuarteto son 4 y un quinteto son 5.",
        "Una orquesta es una agrupación grande, con instrumentos de cuatro familias: cuerdas, maderas, bronces y percusión. Una banda usa sobre todo instrumentos de viento y percusión. La música descriptiva es la que usa sonidos, sin palabras, para describir algo: un amanecer, un tren o unos cuadros. La obra «Cuadros de una exposición», del compositor M. Mussorgsky, es un ejemplo conocido de música descriptiva.",
        "Para escuchar con contexto, hazte tres preguntas. ¿Quién la compuso y para qué agrupación? ¿Qué cuenta o describe? ¿Qué cualidades del sonido oigo que lo muestran? Anotar las respuestas en una ficha te ayuda a recordar cada pieza. Escuchar con respeto significa no burlarse y no hablar mientras suena la música.",
    ],
    [("tradición escrita (docta)", "música compuesta y escrita en partitura"), ("partitura", "hoja donde se escribe la música para que otros la toquen"), ("compositor", "persona que crea y escribe una música"), ("agrupación", "conjunto de intérpretes: dúo, trío, cuarteto, orquesta, banda"), ("música descriptiva", "música sin palabras que describe algo con sonidos")],
    [
        ("Leer una ficha", f"{FICHAS1} ¿Qué agrupación toca la Pieza 1 y cuántos intérpretes tiene?", ["La ficha dice cuarteto de cuerdas.", "Un cuarteto tiene 4 intérpretes."], "Un cuarteto de cuerdas, con 4 intérpretes"),
        ("Calcular una duración", "Cada una de las 5 partes de «Paseo entre cuadros» dura 2 minutos. ¿Cuánto dura la pieza?", ["Son 5 partes.", "Cada una dura 2 minutos: 5 × 2."], "10 minutos"),
    ],
    [
        ("Pensar que una música es docta solo si conozco a su compositor.", "Lo que la hace de tradición escrita es que está en partitura.", "Pregunta si está escrita en partitura, no si la conozco."),
        ("Creer que la música descriptiva siempre lleva letra.", "La música descriptiva describe con sonidos, sin palabras.", "Busca qué sonidos imitan o muestran la idea."),
    ],
    [
        ex("¿Qué hoja permite que otras personas toquen una música igual que como la escribió el compositor?", "La partitura", "En la partitura queda escrita la música."),
        ex(f"{FICHAS1} ¿Para qué agrupación está escrita la Pieza 2?", "Para una banda", "La ficha dice que la Pieza 2 es para banda."),
        ex("¿Cuántos intérpretes tiene un trío?", "3", "Trío significa tres intérpretes."),
    ],
    [
        ex(f"{FICHAS1} ¿Cuáles de las tres piezas describen algo con sus sonidos? Escribe sus números.", "1 y 3", "La Pieza 1 imita un amanecer y la Pieza 3 describe cuadros."),
        ex("¿Cuáles son las cuatro familias de instrumentos de una orquesta?", "Cuerdas, maderas, bronces y percusión", "Son las cuatro familias que forman una orquesta."),
        ex(f"{FICHAS1} En la Pieza 1, los sonidos suben poco a poco. ¿Qué imagen sonora produce eso?", "La salida del sol", "Subir poco a poco imita cómo sale el sol, según la ficha."),
    ],
    [
        arith("Un festival tiene un cuarteto, un trío y un dúo, y cada agrupación toca una vez. ¿Cuántos intérpretes suben al escenario en total?", "4+3+2", "Se suman los intérpretes de las tres agrupaciones.", " intérpretes"),
        ex("Un niño dice que una pieza escrita en partitura por un compositor desconocido no es de tradición escrita. ¿Tiene razón?", "No", "Lo que importa es que esté compuesta y escrita en partitura."),
    ],
    [
        ex("Mateo dice: «la música descriptiva tiene que tener letra para contar algo». ¿Qué le responderías?", "Que describe con sonidos, sin palabras", "La música descriptiva usa solo sonidos."),
        ex("Un cuarteto de cuerdas se transforma en quinteto cuando llega un intérprete más. ¿Cuántos intérpretes hay ahora?", "5", "Cuatro intérpretes más uno son cinco."),
    ],
    [
        arith("Un concierto de orquesta tiene 3 obras de 6 minutos cada una y una pausa de 10 minutos. ¿Cuánto dura en total?", "3*6+10", "Se multiplican las obras por su duración y se suma la pausa.", " minutos"),
        arith("Un concierto tiene un trío, un cuarteto y un quinteto. ¿Cuántos intérpretes más tiene el quinteto que el trío?", "5-3", "Se restan los intérpretes del trío a los del quinteto.", " intérpretes más"),
    ],
    [ex("En un concierto de colegio, un cuarteto toca una pieza que imita una lluvia con sonidos cortos y agudos. ¿Qué tipo de música es y cuántos intérpretes hay?", "Descriptiva; 4 intérpretes", "Imita algo sin palabras y un cuarteto son cuatro personas.")],
    [ex("¿Cómo se llama a la persona que compone una música?", "Compositor o compositora", "Es quien la crea y la escribe."), ex("¿Cuántos intérpretes tiene un dúo?", "2", "Dúo significa dos."), ex("¿Qué escribe un compositor para que otros toquen su música?", "Una partitura", "La partitura guarda la música escrita.")],
    (
        "Una persona de tu casa te lee esta pieza inventada: «Pieza 4, «La tormenta»: escrita en partitura para orquesta; empieza con sonidos suaves y agudos que van subiendo en intensidad hasta unos golpes fuertes de percusión, y termina de nuevo suave». Completa una ficha de escucha con: nombre, agrupación, qué describe, dos cualidades del sonido que lo muestran y cómo te hace sentir (con «por eso»).",
        "Nombre: La tormenta. Agrupación: orquesta. Describe: una tormenta. Cualidades: sonidos que suben de suave a fuerte y golpes fuertes de percusión. Sensación: escuché sonidos que suben hasta golpes fuertes, por eso sentí tensión.",
        ["completa los cinco campos de la ficha", "usa dos cualidades del sonido como evidencia", "escribe una sensación con «por eso»"],
        ["ficha escrita"],
        ["no dar evidencia sonora", "confundir la agrupación con el nombre de la pieza"],
        "Reconoce la ficha completa y pregunta qué cualidad del sonido muestra la tormenta; no corrige la sensación si tiene evidencia.",
    ),
    "Pregunta a una persona de tu casa si recuerda haber escuchado música de orquesta y qué instrumento le gustó.",
    "Dibuja una orquesta con sus cuatro familias de instrumentos, ordenadas en cuatro grupos.",
)

# ---------------------------------------------------------------- OA 03 · clase 2
FICHAS2 = (
    "Pieza 4, «La cosecha»: canción campesina que cantan abuelas y abuelos; se aprende de oído y no se conoce a su autor. "
    "Pieza 5, «Fantasía sobre una ronda»: un compositor escribe en partitura, para orquesta, la melodía de una ronda tradicional. "
    "Pieza 6, «Baile con pañuelo»: danza de pareja que se baila en las fiestas y se toca con guitarra y pandero; las personas mayores la enseñan a las más jóvenes, sin partitura."
)

L(
    OA3, 2,
    f"Lápiz y papel. Las piezas son ejemplos inventados, descritos por escrito. Fichas de trabajo: {FICHAS2} Los saberes y la forma de tocar las músicas de pueblos originarios los enseña el educador o educadora tradicional, no este cuaderno.",
    "Aprenderé a distinguir la música de tradición oral (folclor y pueblos originarios) de la música inspirada en raíces folclóricas. Sirve para valorar de dónde viene cada música.",
    ["Sé qué es una música de tradición escrita.", "Sé usar la ficha de escucha.", "Sé escuchar con respeto."],
    [
        "La tradición oral es la música que se aprende de oído y se pasa de generación en generación, sin partitura. Al folclor pertenecen canciones y danzas que cuentan la vida de una comunidad: el trabajo, la fiesta, la naturaleza. Muchas veces no se conoce a su autor. En Chile, por ejemplo, la cueca es una danza de pareja que se baila con pañuelo, y la tonada es una canción campesina.",
        "Los pueblos originarios también tienen músicas propias, con instrumentos propios. Por ejemplo, el kultrún es un tambor de la cultura mapuche. Cada comunidad tiene sus formas y sus momentos para tocarlos, así que lo correcto es aprenderlos de las personas de la comunidad y escucharlos con mucho respeto.",
        "La música inspirada en raíces folclóricas es distinta. Un compositor toma una melodía, un ritmo o un tema tradicional y lo escribe en partitura, por ejemplo para orquesta. La música sigue siendo de tradición escrita, pero su inspiración viene del folclor. Para distinguir pregunta: ¿cómo se transmite?, ¿se conoce el autor? y ¿está escrita en partitura?",
    ],
    [("tradición oral", "música que se aprende de oído y se transmite de generación en generación"), ("folclor", "músicas y danzas tradicionales de un pueblo"), ("inspirada en raíces folclóricas", "música escrita que usa melodías o ritmos tradicionales"), ("transmitir", "pasar algo de una persona a otra"), ("educador tradicional", "persona de la comunidad que enseña los saberes de su pueblo")],
    [
        ("Clasificar con las preguntas", f"{FICHAS2} ¿La Pieza 4 es de tradición oral o de tradición escrita? Explica con las preguntas de la clase.", ["Se aprende de oído: no hay partitura.", "No se conoce a su autor.", "Eso es tradición oral."], "De tradición oral"),
        ("Distinguir inspiración y folclor", f"{FICHAS2} ¿Por qué la Pieza 5 no es una pieza de tradición oral aunque use una ronda tradicional?", ["El compositor la escribe en partitura.", "Está escrita para orquesta."], "Porque está escrita en partitura; solo se inspira en el folclor"),
    ],
    [
        ("Pensar que toda música que usa una melodía tradicional es de tradición oral.", "Si se escribe en partitura para otra agrupación, es de tradición escrita inspirada en el folclor.", "Revisa cómo se transmite: de oído o con partitura."),
        ("Inventar cómo se toca un instrumento de un pueblo originario.", "Cada comunidad tiene sus formas y es mejor aprenderlas de su educador tradicional.", "Pregunta al educador tradicional o a la comunidad."),
    ],
    [
        ex("¿Cómo se aprende la música de tradición oral: de oído o con partitura?", "De oído", "La tradición oral se pasa de boca a oído, sin partitura."),
        ex(f"{FICHAS2} ¿Se conoce al autor de la Pieza 4?", "No", "La ficha dice que no se conoce a su autor."),
        ex("¿La cueca es una danza de pareja o una canción de cuna?", "Una danza de pareja", "La cueca es una danza que se baila en pareja con pañuelo."),
    ],
    [
        ex(f"{FICHAS2} ¿Cuáles de las tres piezas son de tradición oral? Escribe los números.", "4 y 6", "La Pieza 4 se aprende de oído y la Pieza 6 es una danza tradicional que se toca en las fiestas."),
        ex(f"{FICHAS2} ¿Qué pieza usa una melodía tradicional escrita en partitura?", "La Pieza 5", "Es la ronda escrita para orquesta."),
        ex("¿Qué es el kultrún?", "Un tambor de la cultura mapuche", "El kultrún es un instrumento de percusión mapuche."),
    ],
    [
        arith("Una ronda tradicional tiene una melodía de 8 pulsos que se repite 3 veces. ¿Cuántos pulsos suenan?", "8*3", "Se multiplica la duración de la melodía por las repeticiones.", " pulsos"),
        ex("Un niño dice: «la Pieza 5 es folclor porque usa una ronda». ¿Qué falta para que sea tradición oral?", "Que se aprenda de oído, sin partitura", "Sigue siendo escrita porque se compuso en partitura."),
        ex("Una persona quiere aprender a tocar un instrumento de un pueblo originario. ¿A quién conviene pedir ayuda?", "Al educador o educadora tradicional de la comunidad", "La comunidad conoce sus formas y sus momentos de tocar."),
    ],
    [
        ex("Ana dice que una canción sin autor conocido «no vale» porque nadie la compuso. ¿Qué le responderías?", "Que muchas canciones del folclor tienen autor desconocido y valen igual", "Lo anónimo es una característica de la tradición oral, no un defecto."),
        ex("¿Qué tienen en común la Pieza 4 y la Pieza 5, y qué las diferencia?", "Usan música tradicional; la 4 se aprende de oído y la 5 se escribe en partitura", "Comparten el origen folclórico, pero se transmiten de modo distinto."),
    ],
    [
        arith("Una comunidad canta 4 canciones tradicionales en una fiesta, de 3 minutos cada una. ¿Cuánto dura la parte cantada?", "4*3", "Se multiplica el número de canciones por su duración.", " minutos"),
        ex("Completa con «oral» o «escrita»: una orquesta lee una partitura que reúne tres melodías tradicionales. Es música de tradición…", "Escrita", "Se compuso y se lee en partitura."),
    ],
    [ex("En una fiesta del campo, los abuelos cantan una tonada que aprendieron de oído y todos aplauden el pulso. ¿Es de tradición oral o escrita y qué lo muestra?", "Oral; se aprendió de oído", "No hay partitura y se pasó de generación en generación.")],
    [ex("¿Qué tipo de música se pasa de generación en generación sin partitura?", "La de tradición oral", "Se transmite de oído."), ex("¿Una obra para orquesta con melodía folclórica es oral o escrita?", "Escrita", "Está compuesta en partitura."), ex("¿Quién enseña la forma tradicional de tocar un instrumento de un pueblo originario?", "El educador o educadora tradicional", "Es quien conoce y transmite esos saberes.")],
    (
        "Pregunta a una persona de tu casa por una canción o un baile que haya aprendido de oído (de la familia o de un lugar), sin pedir datos personales. Si no recuerda ninguna, usa «La cosecha» de la clase. Escribe: nombre o descripción, cómo se aprendió, si se conoce al autor y en qué ocasión se canta o baila. Concluye si es de tradición oral o escrita.",
        "Una ronda que una persona aprendió de niña, jugando; no hay partitura ni autor conocido; se canta en el patio. Es de tradición oral.",
        ["escribe los cuatro datos", "usa las preguntas de la clase para concluir", "respeta lo que la persona quiera contar"],
        ["ficha escrita", "conversación"],
        ["inventar datos que no sabe", "concluir sin explicar por qué"],
        "Reconoce la conclusión argumentada; si no hay claridad, pide revisar cómo se transmitió y si hay partitura.",
    ),
    "Escribe en una frase la diferencia entre tradición oral y tradición escrita.",
    "Pide a una persona de tu casa que te cante una canción que aprendió de oído y anota cómo la aprendió.",
)

# ---------------------------------------------------------------- OA 03 · clase 3
FICHAS3 = (
    "Pieza 7, «Noche de ciudad»: la toca un quinteto de jazz; cada solista inventa su parte en el momento, sin partitura fija. "
    "Pieza 8, «Rock del patio»: la tocan voz, dos guitarras eléctricas, bajo y batería; se escucha en la radio y en plataformas digitales. "
    "Pieza 9, «Tema del héroe»: música de una película, tocada por una orquesta, que acompaña las escenas de aventura. "
    "Pieza 10, «El gran baile»: un musical de teatro, donde los personajes actúan, cantan y bailan."
)

L(
    OA3, 3,
    f"Lápiz y papel. Las piezas son ejemplos inventados, descritos por escrito. Fichas de trabajo: {FICHAS3}",
    "Aprenderé a escuchar música popular (jazz, rock, fusión, música de películas y musicales) y a reconocer su contexto. Sirve para entender cómo la música popular está presente en la vida de mucha gente.",
    ["Sé qué es una agrupación musical.", "Sé usar la ficha de escucha.", "Sé distinguir tradición oral y escrita."],
    [
        "La música popular es la que escucha mucha gente y se difunde por la radio, los discos, el cine, el teatro y las plataformas digitales. Incluye muchos estilos. El jazz usa la improvisación: cada solista inventa su parte en el momento. El rock suele usar voz, guitarras eléctricas, bajo y batería. La fusión mezcla estilos distintos, por ejemplo el rock con ritmos tradicionales.",
        "También son música popular las canciones, la música de películas y los musicales. La música de una película acompaña las imágenes: puede ser tensa en una escena de peligro y alegre en una de fiesta. Un musical es una obra de teatro con canciones y bailes en que los personajes cuentan la historia cantando.",
        "Para escuchar la música popular con contexto pregunta: ¿quién la toca?, ¿cuántos intérpretes son?, ¿dónde se escucha? y ¿para qué sirve: bailar, acompañar una escena o contar una historia? Escuchar con respeto también vale para los estilos que a ti no te gustan tanto.",
    ],
    [("música popular", "música que escucha mucha gente y se difunde por medios masivos"), ("jazz", "estilo con mucha improvisación"), ("rock", "estilo con guitarras eléctricas, bajo y batería"), ("fusión", "mezcla de estilos distintos"), ("musical", "obra de teatro con canciones y bailes")],
    [
        ("Reconocer el estilo", f"{FICHAS3} ¿Qué pieza usa improvisación y cuántos intérpretes la tocan?", ["La improvisación es propia del jazz.", "El jazz de la ficha es de un quinteto: 5 intérpretes."], "La Pieza 7, con 5 intérpretes"),
        ("Contar intérpretes", f"{FICHAS3} La Pieza 8 la tocan voz, dos guitarras eléctricas, bajo y batería. ¿Cuántos instrumentos hay sin contar la voz?", ["Guitarras eléctricas: 2.", "Bajo: 1 y batería: 1.", "2 + 1 + 1 = 4."], "4 instrumentos"),
    ],
    [
        ("Pensar que la música popular es de mala calidad.", "Los estilos son distintos y no se ordenan de mejor a peor.", "Describe sus características en vez de juzgarla."),
        ("Creer que improvisar es tocar cualquier cosa.", "Quien improvisa sigue la música y el pulso, e inventa dentro de ella.", "Escucha cómo el solista respeta el pulso."),
    ],
    [
        ex(f"{FICHAS3} ¿Qué pieza acompaña las escenas de una película?", "La Pieza 9", "La ficha dice que acompaña escenas de aventura."),
        ex("¿Qué se inventa en el momento en el jazz?", "La parte del solista", "Eso es improvisar."),
        ex("¿Cuántos intérpretes tiene un quinteto de jazz?", "5", "Quinteto significa cinco intérpretes."),
    ],
    [
        ex(f"{FICHAS3} ¿Qué pieza es un musical y qué hacen sus personajes?", "La Pieza 10; actúan, cantan y bailan", "La ficha describe el musical con esas tres acciones."),
        ex("Un grupo mezcla ritmos de rock con ritmos tradicionales. ¿Cómo se llama esa mezcla de estilos?", "Fusión", "Fusión es mezclar estilos distintos."),
        ex(f"{FICHAS3} ¿Cuál de las piezas se difunde por la radio y las plataformas digitales?", "La Pieza 8", "La ficha lo dice de «Rock del patio»."),
    ],
    [
        arith("Una banda de rock tiene voz, 2 guitarras eléctricas, bajo y batería. ¿Cuántos integrantes tiene si la voz y cada instrumento los toca una persona distinta?", "1+2+1+1", "Se suman la voz y los instrumentos.", " integrantes"),
        ex("Una película muestra una escena de peligro. ¿La música debería ser tensa o alegre?", "Tensa", "La música acompaña lo que muestran las imágenes."),
        ex("¿Dónde se presenta un musical: en un teatro con personajes en vivo o solo en la radio?", "En un teatro", "Un musical es una obra de teatro con canciones y bailes."),
    ],
    [
        ex("Pablo dice: «el rock es mejor que el jazz porque tiene guitarras». ¿Qué error comete?", "Juzga en vez de describir", "Los estilos son distintos, no mejores ni peores."),
        ex("Una solista de jazz toca una frase que no está escrita y siempre mantiene el pulso. ¿Está improvisando bien o tocando cualquier cosa?", "Improvisando bien", "Inventa dentro del pulso y de la música."),
    ],
    [
        arith("Un musical tiene 12 canciones y un ensayo repasa 3 canciones por día. ¿Cuántos días se necesitan?", "12//3", "Se divide el total de canciones por las que se ensayan cada día.", " días"),
        arith("Una orquesta de cine graba 3 temas de 4 minutos y 2 temas de 3 minutos. ¿Cuántos minutos de música graba?", "3*4+2*3", "Se suman los minutos de los temas de cada duración.", " minutos"),
    ],
    [ex("Una familia ve una película de aventuras y la música cambia de rápida y fuerte a lenta y suave cuando termina la persecución. ¿Qué hace la música con las imágenes?", "Las acompaña y muestra su ambiente", "Cambia con la escena para reforzar lo que se ve.")],
    [ex("¿Qué estilo se caracteriza por la improvisación?", "El jazz", "Los solistas inventan en el momento."), ex("¿Qué es una fusión?", "Una mezcla de estilos", "Une estilos distintos."), ex("¿Qué es un musical?", "Una obra de teatro con canciones y bailes", "Los personajes cuentan la historia cantando.")],
    (
        "Elige una música popular que te rodee (la radio de una persona de tu casa, la música de una película o de un programa), a volumen bajo. Escucha un trozo corto y completa la ficha: nombre o descripción, cuántos intérpretes oyes, qué instrumentos reconoces, dónde y para qué se usa y una cualidad del sonido como evidencia. Evita dar datos personales.",
        "Descripción: música de una película de dibujos. Intérpretes: orquesta. Instrumentos: violines y trompetas. Uso: acompaña las escenas. Evidencia: suena rápida y fuerte en las escenas de persecución.",
        ["completa los cinco campos", "usa una cualidad del sonido como evidencia", "describe sin juzgar si es mejor o peor"],
        ["ficha escrita"],
        ["escribir «me gusta» como único argumento", "no indicar para qué se usa"],
        "Reconoce la ficha completa y pide mostrar cuál cualidad del sonido ayuda a decir para qué se usa.",
    ),
    "Nombra tres estilos de música popular y di qué los caracteriza.",
    "Pide a una persona de tu casa que te cuente qué músicas populares le gustaba escuchar de niña o niño.",
)

# ---------------------------------------------------------------- OA 03 · clase 4
TABLA = (
    "Pieza A: cuarteto de cuerdas, escrita en partitura, se toca en conciertos. "
    "Pieza B: voz, guitarra y pandero, aprendida de oído, se canta en fiestas del campo. "
    "Pieza C: banda de rock, se difunde en la radio, se usa para escuchar y bailar."
)

L(
    OA3, 4,
    f"Lápiz y papel. Las piezas son ejemplos inventados. Tabla de trabajo: {TABLA}",
    "Aprenderé a comparar estilos de música con los mismos criterios, sin decir cuál es mejor. Sirve para valorar la diversidad de la música.",
    ["Sé distinguir tradición oral y escrita.", "Sé qué es música popular.", "Sé describir una pieza con una ficha."],
    [
        "Comparar es mirar dos o más cosas con el mismo criterio para ver en qué se parecen y en qué se diferencian. Para comparar músicas podemos usar cuatro criterios: la agrupación (quién la toca), cómo se transmite (partitura u oído), el contexto (dónde se escucha) y la función (para qué sirve). Si usas los mismos criterios con todas las piezas, la comparación es justa.",
        "Jerarquizar es poner una cosa por encima de otra, como decir «mejor» o «peor». Una música no es mejor que otra por ser antigua, moderna, popular o docta: cada una tiene su lugar y su función. Si dices «esta es mejor», no estás comparando; estás opinando sin criterio. En cambio, «la pieza A se escribe en partitura y la B se aprende de oído» es una comparación.",
        "Cuando prefieras una música, puedes decirlo con respeto: «a mí me gusta más la pieza C porque tiene un pulso que me hace bailar». Así separas tu gusto, que es personal, de la descripción, que se puede comprobar. Respetar la música de otras personas es parte de escuchar bien.",
    ],
    [("comparar", "ver en qué se parecen y se diferencian dos cosas con el mismo criterio"), ("criterio", "la pregunta que usas para comparar"), ("jerarquizar", "decir que una cosa es mejor o peor que otra"), ("diversidad", "variedad de cosas distintas"), ("gusto personal", "lo que a una persona le agrada")],
    [
        ("Comparar con un criterio", f"{TABLA} Compara la Pieza A y la Pieza B según cómo se transmiten.", ["Pieza A: se escribe en partitura.", "Pieza B: se aprende de oído."], "La A se transmite con partitura y la B de oído"),
        ("Separar comparar de jerarquizar", "Una niña dice «la pieza C es la mejor porque es más moderna». ¿Es una comparación o una jerarquía?", ["«La mejor» pone una por encima de otras.", "No usa un criterio descriptivo."], "Una jerarquía"),
    ],
    [
        ("Decir que la música docta es mejor porque es más antigua o más difícil.", "La antigüedad o la dificultad no la hacen mejor que otra.", "Describe con criterios y deja el gusto como opinión personal."),
        ("Comparar usando un criterio distinto para cada pieza.", "La comparación no es justa.", "Usa los mismos criterios en todas las piezas."),
    ],
    [
        ex(f"{TABLA} ¿Qué pieza se aprende de oído?", "La Pieza B", "La ficha dice que se aprende de oído."),
        ex(f"{TABLA} ¿Quién toca la Pieza A?", "Un cuarteto de cuerdas", "Así lo dice la tabla."),
        ex("¿«La Pieza A es peor que la C» es una comparación o una jerarquía?", "Una jerarquía", "«Peor» pone una pieza por debajo de otra."),
    ],
    [
        ex(f"{TABLA} Compara las tres piezas según el contexto: escribe dónde se escucha cada una.", "A: en conciertos; B: en fiestas del campo; C: en la radio", "Cada contexto se lee en la tabla."),
        ex(f"{TABLA} ¿Qué pieza se usa para escuchar y bailar?", "La Pieza C", "Así lo dice la tabla."),
        ex("Elige la frase que compara con respeto: (a) «La música del campo es de mal gusto», (b) «La música del campo se transmite de oído y la docta con partitura».", "(b)", "La (b) describe con un criterio; la (a) juzga."),
    ],
    [
        arith("Un colegio escucha 3 músicas de estilos distintos y las comparan con 4 criterios cada una. ¿Cuántas respuestas escriben en total?", "3*4", "Cada música lleva una respuesta por criterio.", " respuestas"),
        ex("Dos niños escuchan la misma pieza. A uno le gusta mucho y al otro no. ¿Alguno se equivoca?", "Ninguno", "El gusto es personal; lo que se puede comprobar es la descripción."),
        ex("Para comparar músicas de forma justa, ¿qué debes hacer con los criterios?", "Usar los mismos en todas las piezas", "Así las piezas se miran del mismo modo."),
    ],
    [
        ex("Tomás dice: «la música de los pueblos originarios es menos importante porque no tiene partitura». ¿Qué error comete?", "Jerarquiza por un criterio que no la define", "Que no use partitura es una característica de la tradición oral, no una falta."),
        ex("Una persona dice «me gustan más los tambores porque me dan ganas de moverme». ¿Es un gusto personal con argumento o una jerarquía?", "Un gusto personal con argumento", "Habla de su sensación y da una razón, sin decir que otra música sea peor."),
    ],
    [
        ex(f"{TABLA} ¿Qué frase compara por agrupación sin jerarquizar: (a) «La A es más fina que la C» o (b) «La A la toca un cuarteto de cuerdas y la C una banda de rock»?", "(b)", "La (b) describe cada agrupación; la (a) juzga."),
        arith("Una tabla compara 4 piezas con 3 criterios y ya tiene 7 casillas llenas. ¿Cuántas faltan por llenar?", "4*3-7", "Se calcula el total de casillas y se resta lo ya llenado.", " casillas"),
    ],
    [ex("En una clase se escucha una pieza de orquesta y una de rock. Un compañero dice «la de orquesta es de gente culta». ¿Cómo lo dirías de manera que describa y no juzgue?", "La de orquesta se escribe en partitura y la de rock la toca una banda", "Se cambia el juicio por una descripción verificable.")],
    [ex("¿Qué significa jerarquizar músicas?", "Decir que una es mejor o peor que otra", "Es poner una música por encima de otra."), ex("¿Qué se usa para comparar de forma justa?", "Los mismos criterios", "Los criterios iguales hacen justa la comparación."), ex("¿El gusto personal puede cambiar la descripción de una pieza?", "No", "La descripción se comprueba; el gusto es personal.")],
    (
        "Escucha o recuerda dos músicas muy distintas (una puede ser de la radio y otra la que elijas) y compáralas en una tabla con los cuatro criterios de la clase: agrupación, transmisión, contexto y función. Termina con una frase de gusto personal con «porque», sin decir que una música sea mejor que la otra.",
        "Música 1: banda de rock, se difunde por radio, para bailar. Música 2: voz y guitarra, se aprende de oído, para cantar en reuniones. Frase: «Me gusta más la 1 porque su batería marca un pulso que me hace mover».",
        ["usa los cuatro criterios para las dos músicas", "no usa «mejor» ni «peor» para describir", "justifica su gusto con una cualidad del sonido"],
        ["tabla de comparación", "frase de gusto personal"],
        ["usar criterios distintos para cada música", "juzgar en vez de describir"],
        "Reconoce el uso de criterios iguales y pide cambiar los juicios por descripciones comprobables.",
    ),
    "Escribe una comparación entre dos músicas con un solo criterio, sin decir cuál es mejor.",
    "Explica a una persona de tu casa la diferencia entre comparar y jerarquizar con un ejemplo.",
)

# ---------------------------------------------------------------- OA 03 · clase 5
BIT = [
    (1, "Marcha del puerto", "escrita", "banda", 2),
    (2, "Canción de la siembra", "oral", "voz y guitarra", 3),
    (3, "Rock del patio", "popular", "banda de rock", 3),
    (4, "Danza del sur", "escrita", "cuarteto", 4),
    (5, "Ronda del valle", "oral", "voz y percusión", 2),
    (6, "Jazz de la lluvia", "popular", "quinteto de jazz", 4),
    (7, "Aire del campo", "escrita", "orquesta", 5),
    (8, "Tema de aventura", "popular", "orquesta", 3),
]
BIT_TXT = " ".join(f"{n}) «{t}», tradición {tr}, {ag}, {d} min." for n, t, tr, ag, d in BIT)
BIT_ESC = sum(1 for b in BIT if b[2] == "escrita")
BIT_ORAL = sum(1 for b in BIT if b[2] == "oral")
BIT_POP = sum(1 for b in BIT if b[2] == "popular")
BIT_MIN = sum(b[4] for b in BIT)

L(
    OA3, 5,
    f"Lápiz y papel. La bitácora de ejemplo es inventada. Bitácora de trabajo (8 entradas): {BIT_TXT} La meta anual de escucha son al menos 20 músicas variadas y cortas; las audiciones reales las elige el docente.",
    "Aprenderé a llevar una bitácora de escucha diversa: un registro ordenado de las músicas que escucho, con su tradición, su agrupación y mi evidencia. Sirve para comprobar que estoy escuchando música variada.",
    ["Sé usar la ficha de escucha.", "Sé distinguir tradición oral, escrita y popular.", "Sé comparar sin jerarquizar."],
    [
        "Una bitácora es un cuaderno donde anotas lo que haces, en orden. En una bitácora de escucha cada entrada tiene: un número, el nombre o descripción de la música, su tradición (escrita, oral o popular), la agrupación que la toca, la duración y una evidencia sonora: una cualidad del sonido que oíste. Así puedes volver a revisarla y compartirla con otras personas.",
        "Una bitácora sirve para ver la diversidad. Si todas tus entradas son de la misma tradición, quiere decir que escuchaste siempre lo mismo. Para llegar a una escucha abundante, la meta es reunir al menos 20 músicas variadas y cortas, de distintas tradiciones y con distintas agrupaciones. Contar cuántas entradas tienes de cada tradición te muestra qué te falta escuchar.",
        "Anota solo lo que escuchaste y escribe con tus palabras. No copies letras de canciones ni textos completos. Si no sabes el nombre de una música, descríbela: «canción de una película, con orquesta». Al final, revisa tu bitácora y escribe qué te llamó la atención, sin decir qué estilo es mejor.",
    ],
    [("bitácora", "registro ordenado de lo que haces o escuchas"), ("entrada", "una anotación de la bitácora"), ("evidencia sonora", "cualidad del sonido que oíste y que respalda lo que dices"), ("diversa", "con variedad de tradiciones y agrupaciones"), ("meta", "lo que quieres lograr")],
    [
        ("Contar por tradición", f"{BIT_TXT} ¿Cuántas músicas hay de tradición escrita, oral y popular?", ["Escritas: entradas 1, 4 y 7.", "Orales: entradas 2 y 5.", "Populares: entradas 3, 6 y 8."], f"{BIT_ESC} escritas, {BIT_ORAL} orales y {BIT_POP} populares"),
        ("Calcular lo que falta", f"La bitácora de ejemplo tiene {len(BIT)} entradas y la meta son 20 músicas. ¿Cuántas faltan?", ["Meta: 20 músicas.", "Hay 8.", "20 − 8 = 12."], "12 músicas"),
    ],
    [
        ("Anotar «me gustó» como única evidencia.", "No dice qué se oyó.", "Escribe una cualidad del sonido: suave, rápida, aguda, un instrumento."),
        ("Anotar solo músicas de un mismo estilo y creer que la bitácora es diversa.", "La diversidad pide distintas tradiciones y agrupaciones.", "Cuenta por tradición y busca la que falta."),
    ],
    [
        ex(f"{BIT_TXT} ¿Qué agrupación toca «Rock del patio»?", "Una banda de rock", "La entrada 3 anota banda de rock."),
        ex(f"{BIT_TXT} ¿De qué tradición es «Ronda del valle»?", "Oral", "La entrada 5 dice tradición oral."),
        ex("¿Qué campo de la bitácora guarda una cualidad del sonido oída?", "La evidencia sonora", "La evidencia sonora respalda lo que dices."),
    ],
    [
        arith(f"{BIT_TXT} ¿Cuántos minutos suman las entradas de tradición popular (3, 6 y 8)?", "3+4+3", "Se suman las duraciones de las entradas 3, 6 y 8.", " minutos"),
        ex(f"{BIT_TXT} ¿Cuál es la agrupación de la entrada 7?", "Orquesta", "La entrada 7 anota orquesta."),
        ex(f"{BIT_TXT} Escribe los números de las entradas que duran más de 3 minutos.", "4, 6 y 7", "Duran 4, 4 y 5 minutos."),
    ],
    [
        arith(f"{BIT_TXT} ¿Cuántos minutos suma toda la bitácora de ejemplo?", "+".join(str(b[4]) for b in BIT), "Se suman las duraciones de las 8 entradas.", " minutos"),
        ex(f"{BIT_TXT} Una persona dice que la bitácora de ejemplo no es diversa porque solo tiene música de orquesta. ¿Tiene razón?", "No", "Tiene banda, voz y guitarra, cuarteto, quinteto de jazz, voz y percusión y orquesta."),
    ],
    [
        ex("Una bitácora tiene 6 músicas de tradición oral y 4 de tradición escrita, y ninguna popular. ¿Qué tradición conviene escuchar para ampliarla?", "La popular", "Falta esa tradición para que sea diversa."),
        ex(f"{BIT_TXT} Un niño dice que como hay 3 populares y 2 orales, la música popular es mejor. ¿Qué error comete?", "Confunde cantidad con calidad", "La cantidad de entradas solo muestra lo que se escuchó, no qué es mejor."),
    ],
    [
        arith(f"Si cada día se escucha 1 música nueva y hay {len(BIT)} registradas, ¿cuántos días faltan para llegar a la meta de 20?", f"20-{len(BIT)}", "Se resta lo registrado de la meta, a una música por día.", " días"),
        ex("Una entrada dice: «9) Canción del río, tradición oral, voz y guitarra, 2 min, evidencia: me gustó». ¿Qué campo está mal escrito?", "La evidencia sonora", "«Me gustó» no es una cualidad del sonido que se pueda comprobar."),
    ],
    [ex("En una semana una niña registra 3 músicas: una de orquesta, una de rock y una de su casa aprendida de oído. ¿Qué tradiciones reunió?", "Escrita, popular y oral", "Orquesta es escrita, rock es popular y lo aprendido de oído es oral.")],
    [ex("¿Qué es una bitácora de escucha?", "Un registro ordenado de las músicas que escuchaste", "Guarda las entradas en orden."), ex("¿Cuántas músicas variadas y cortas es la meta de escucha?", "20", "La meta es escuchar al menos 20."), ex("¿Cuál de estos datos es la evidencia sonora: «me gustó» o «suena rápida»?", "«Suena rápida»", "Es una cualidad del sonido que se comprueba.")],
    (
        "Empieza tu propia bitácora con 4 entradas de músicas distintas que escuches esta semana (la radio, una película, una música de tu casa o una que elija el docente), a volumen bajo. Cada entrada lleva: número, nombre o descripción, tradición, agrupación, duración aproximada y evidencia sonora. Al final cuenta cuántas entradas tienes de cada tradición y qué te falta para llegar a 20.",
        "1) Música de una película, popular, orquesta, 3 min, evidencia: rápida y fuerte. 2) Canción cantada en casa, oral, voz, 2 min, evidencia: suave y lenta. 3) Música para banda, escrita, banda, 3 min, evidencia: pulso firme. 4) Rock de la radio, popular, banda de rock, 3 min, evidencia: guitarras fuertes. Tradiciones: 2 populares, 1 oral, 1 escrita. Faltan 16.",
        ["completa seis campos en cada entrada", "reúne al menos dos tradiciones distintas", "cuenta por tradición y calcula lo que falta"],
        ["bitácora escrita", "conteo por tradición"],
        ["no anotar la evidencia sonora", "no revisar la diversidad"],
        "Reconoce el orden de la bitácora y pide revisar cuál tradición falta; no corrige los gustos.",
    ),
    "Anota una música que escuches hoy con su tradición y una cualidad del sonido.",
    "Pide a una persona de tu casa que sugiera una música de otra tradición y regístrala en tu bitácora.",
)

# ---------------------------------------------------------------- OA 04 · clase 1
CANTO1 = "Sube la luna / baja el sol / canta el río / llega el día"

L(
    OA4, 1,
    f"Lápiz y tu voz, en un lugar tranquilo, sentado o de pie con la espalda recta, y un vaso de agua a mano. Canción de ejemplo inventada (cuatro frases de 4 pulsos cada una): «{CANTO1}». Canta siempre a un volumen cómodo y sin gritar.",
    "Aprenderé a cantar al unísono cuidando la respiración y escuchando a los demás para igualar la altura. Sirve para que un grupo suene como una sola voz.",
    ["Sé mantener el pulso con las palmas.", "Sé que agudo y grave son alturas.", "Sé cuidar mi voz sin gritar."],
    [
        "Cantar al unísono es cantar todos la misma melodía, con las mismas palabras y al mismo tiempo. Para que suene bien, cada persona escucha a las demás e iguala su altura, es decir, canta ni más agudo ni más grave que el grupo. Afinar es ajustar la voz para que coincida con la altura que se escucha.",
        "La respiración ayuda a cantar. Antes de empezar, inhala por la nariz de forma tranquila, como si olieras una flor, y suelta el aire despacio mientras cantas. Respira en las pausas entre frases, sin cortar una palabra. Cada frase del ejemplo dura 4 pulsos, así que tomas aire en el pulso que sigue a cada frase.",
        "Cuida tu voz y tu cuerpo. No grites ni fuerces los sonidos; si tu voz se cansa, descansa y toma agua. Mantén los hombros sueltos y la espalda recta. Un buen unísono no es el más fuerte, sino el que suena parejo, con la misma entrada, el mismo pulso y la misma intensidad.",
    ],
    [("unísono", "todos cantan la misma melodía al mismo tiempo"), ("afinar", "ajustar la voz para coincidir con la altura que se escucha"), ("frase", "grupo de palabras y sonidos que se canta de un tirón"), ("respiración", "tomar aire por la nariz para sostener la frase"), ("entrada", "momento en que empieza a cantar")],
    [
        ("Planear la respiración", f"La canción «{CANTO1}» tiene 4 frases de 4 pulsos. ¿Cuántas veces respiras si lo haces después de cada frase, incluida la última?", ["Hay 4 frases.", "Respiras una vez después de cada una."], "4 veces"),
        ("Cuidar el volumen", "Un coro canta al unísono, pero una niña grita para sonar más. ¿Qué logra en el unísono?", ["El unísono necesita sonar parejo.", "Gritar rompe esa igualdad y fuerza la voz."], "Rompe el unísono y fuerza su voz"),
    ],
    [
        ("Creer que cantar más fuerte es cantar mejor.", "Gritar fuerza la voz y desafina el grupo.", "Canta cómodo y escucha a los demás."),
        ("Respirar en medio de una palabra.", "Corta la frase y se pierde el pulso.", "Respira en las pausas entre frases."),
    ],
    [
        ex("¿Cantar al unísono es cantar la misma melodía o melodías distintas?", "La misma melodía", "Unísono significa todos lo mismo y a la vez."),
        ex("¿Por dónde conviene tomar aire para cantar: por la nariz o por la boca bien abierta?", "Por la nariz", "La inhalación por la nariz es tranquila y silenciosa."),
        ex("¿Qué debes hacer si tu voz se cansa?", "Descansar y tomar agua", "Cuidar la voz evita dañarla."),
    ],
    [
        ex(f"En «{CANTO1}», cada frase dura 4 pulsos. ¿En qué momento respiras: dentro de una palabra o entre frases?", "Entre frases", "Respirar en las pausas mantiene unidas las palabras."),
        ex("Un grupo canta y una persona se oye más aguda que las demás. ¿Qué debe hacer para afinar: seguir igual o escuchar y bajar su altura?", "Escuchar y ajustar su altura", "Afinar es igualar la altura del grupo."),
        ex("¿Cuál es una buena postura para cantar: espalda recta y hombros sueltos, o encorvada?", "Espalda recta y hombros sueltos", "Esa postura deja espacio para respirar."),
    ],
    [
        arith(f"La canción «{CANTO1}» tiene 4 frases de 4 pulsos. ¿Cuántos pulsos dura cantada una vez?", "4*4", "Se multiplican las frases por los pulsos de cada una.", " pulsos"),
        arith("Un coro canta la canción de 16 pulsos 3 veces seguidas, con 2 pulsos de pausa entre vueltas. ¿Cuántos pulsos dura todo, contando solo las 2 pausas entre las 3 vueltas?", "16*3+2*2", "Se suman las 3 vueltas y las 2 pausas intermedias.", " pulsos"),
    ],
    [
        ex("Un coro suena bien pero una niña canta más fuerte que todos. Un compañero dice «canta tan bien que nos tapa». ¿Qué debe cuidar ella para que sea unísono?", "Su intensidad, para sonar parejo", "Un unísono pide igualar la intensidad."),
        ex("Dos personas cantan la misma melodía, una empieza en el pulso 1 y otra en el pulso 3. ¿Están cantando al unísono?", "No", "No cantan al mismo tiempo."),
    ],
    [
        ex("Escribe el orden correcto para cantar: (a) cantar la frase, (b) tomar aire por la nariz, (c) escuchar la altura del grupo.", "c, b, a", "Primero se escucha, luego se respira y al final se canta."),
        arith("Una frase dura 4 pulsos y tomas aire en un pulso extra después de cada frase. Con 4 frases, ¿cuántos pulsos hay en total?", "4*(4+1)", "Cada frase sumada a su pulso de respiración.", " pulsos"),
    ],
    [ex("En la fila del colegio, un grupo canta una canción corta. Una niña nota que sus compañeros van más lento que ella. ¿Qué debe hacer para estar en unísono?", "Escuchar al grupo y ajustar su pulso", "En unísono se canta con el mismo pulso.")],
    [ex("¿Cómo se llama ajustar la voz a la altura del grupo?", "Afinar", "Es igualar la altura."), ex("¿Cantar al unísono es todos a la vez o por turnos?", "Todos a la vez", "El unísono es simultáneo."), ex("¿Se respira en medio de una palabra?", "No", "Se respira en las pausas.")],
    (
        f"Con una persona de tu casa como compañera de escucha, canta la canción «{CANTO1}» (inventa la melodía con sonidos cómodos para tu voz, sin gritar). Haz tres cosas: respira tranquilo después de cada frase, mantén el mismo pulso que tu compañera y escucha si tu altura coincide con la suya. Escribe en qué frase respiraste y qué hiciste para afinar.",
        "Respiré después de cada frase (4 veces) y bajé un poco mi altura cuando noté que mi compañera estaba más grave. Mantuvimos el mismo pulso con palmas suaves.",
        ["respira en las pausas entre frases", "mantiene el pulso del grupo", "describe cómo ajustó su altura"],
        ["interpretación", "registro escrito breve"],
        ["gritar para destacar", "respirar dentro de una palabra"],
        "Reconoce la escucha y el cuidado de la voz; si cantó más fuerte que su compañera, pide repetir buscando igualar la intensidad.",
    ),
    "Cuenta 4 pulsos con tus palmas y canta una frase corta en cada uno, respirando en la pausa.",
    "Canta con una persona de tu casa y túrnense para decidir quién escucha y quién guía el pulso.",
)

# ---------------------------------------------------------------- OA 04 · clase 2
L(
    OA4, 2,
    f"Lápiz, tu voz y dos o más personas de tu casa (o los compañeros en clase). Canción de ejemplo inventada de 4 frases de 4 pulsos: «{CANTO1}». Si cantas solo, puedes practicar con tus palmas y tu voz alternando. Cuida el volumen.",
    "Aprenderé a cantar un canon simple de dos voces, sosteniendo mi propia parte sin dejarme llevar por la otra. Sirve para cantar juntos una misma melodía en distintos momentos.",
    ["Sé cantar al unísono.", "Sé mantener el pulso.", "Sé contar las frases de una canción."],
    [
        "Un canon es una música en que todas las voces cantan la misma melodía, pero cada una empieza en un momento distinto. La primera voz parte sola. Después de un tiempo acordado, entra la segunda voz con la melodía desde el comienzo. Por eso se oyen frases distintas al mismo tiempo, y sin embargo suena bien porque la melodía está hecha para ello.",
        f"Veámoslo con la canción «{CANTO1}», de 4 frases de 4 pulsos. La voz 1 canta la frase 1 en los pulsos 1 a 4, la frase 2 en los pulsos 5 a 8, y así. Si la voz 2 entra después de 4 pulsos, canta la frase 1 en los pulsos 5 a 8. En ese momento la voz 1 canta la frase 2. Esa diferencia entre las dos voces es la distancia de entrada.",
        "Lo más difícil de un canon es sostener tu propia parte. Para lograrlo, escucha tu voz sin dejarte llevar por la otra, marca el pulso con un pie o con un dedo y sigue tu frase aunque la otra suene distinta. Si te pierdes, no te detengas bruscamente: deja pasar una frase y vuelve a entrar en el comienzo de la siguiente.",
    ],
    [("canon", "misma melodía que entra en momentos distintos"), ("voz 1 y voz 2", "las partes que entran una después de la otra"), ("distancia de entrada", "cuántos pulsos separan la entrada de las voces"), ("sostener tu parte", "seguir tu propia frase aunque suene otra"), ("simultáneo", "al mismo tiempo")],
    [
        ("Ubicar las voces", f"En «{CANTO1}», cada frase dura 4 pulsos y la voz 2 entra en el pulso 5. ¿Qué frase canta la voz 2 en el pulso 9?", ["La voz 2 canta la frase 1 en 5-8.", "En 9-12 canta la frase 2."], "La frase 2"),
        ("Calcular la duración", "La voz 1 canta 4 frases de 4 pulsos. La voz 2 entra 4 pulsos después. ¿En qué pulso termina la voz 2?", ["La voz 1 termina en el pulso 16.", "La voz 2 va 4 pulsos más atrás: 16 + 4."], "En el pulso 20"),
    ],
    [
        ("Cantar fuerte para escucharse y no perder la parte.", "Pierdes la escucha de las demás voces.", "Canta cómodo y marca el pulso para sostener tu parte."),
        ("Detener todo el canon al perderte.", "Los demás se confunden.", "Deja pasar una frase y vuelve a entrar al comienzo de la siguiente."),
    ],
    [
        ex("¿Qué tienen igual todas las voces de un canon?", "La melodía", "Todas cantan la misma melodía."),
        ex("¿La segunda voz entra al mismo tiempo que la primera o después?", "Después", "Entra con un retraso acordado."),
        ex("Si te pierdes en un canon, ¿vuelves a entrar al comienzo de la siguiente frase o paras todo?", "Al comienzo de la siguiente frase", "Así no detienes a las demás voces."),
    ],
    [
        ex(f"En «{CANTO1}» (4 frases de 4 pulsos), la voz 2 entra en el pulso 5. ¿Qué frase canta la voz 1 en el pulso 5?", "La frase 2", "En 5-8 la voz 1 canta la segunda frase."),
        ex(f"En el mismo canon, ¿qué frase canta la voz 2 en el pulso 13?", "La frase 3", "La voz 2 canta la frase 3 en los pulsos 13 a 16."),
        ex("En un canon de dos voces con entrada a los 4 pulsos, ¿en qué pulso empieza a cantar la voz 2?", "En el pulso 5", "Entra después de que la voz 1 cantó los pulsos 1 a 4."),
    ],
    [
        arith("Cada frase dura 4 pulsos y hay 4 frases. La voz 2 entra 4 pulsos después. ¿Cuántos pulsos dura todo el canon, hasta que termina la voz 2?", "4*4+4", "La voz 1 dura 16 pulsos y la voz 2 termina 4 pulsos después.", " pulsos"),
        arith("Un canon de dos voces se canta 2 veces seguidas de 20 pulsos cada vez. ¿Cuántos pulsos son en total?", "20*2", "Se multiplican las vueltas por su duración.", " pulsos"),
        ex(f"En «{CANTO1}» (4 frases de 4 pulsos), la voz 2 entra en el pulso 5. En el pulso 9, ¿qué frase canta cada voz?", "La voz 1 la frase 3 y la voz 2 la frase 2", "En 9-12 la voz 1 va en su tercera frase y la voz 2, que partió 4 pulsos después, en su segunda."),
    ],
    [
        ex("Una niña dice: «si la otra voz suena distinto, me confundo y canto lo que ella canta». ¿Qué debe hacer para sostener su parte?", "Escuchar su propia voz y marcar el pulso", "Así sigue su propia frase sin dejarse llevar."),
        ex("Dos voces cantan el canon, pero la segunda entra en el mismo pulso que la primera. ¿Es un canon o un unísono?", "Un unísono", "Si entran a la vez, cantan lo mismo al mismo tiempo."),
    ],
    [
        ex("Un canon tiene 3 voces y cada una entra 4 pulsos después de la anterior. ¿En qué pulso entra la voz 3?", "En el pulso 9", "La voz 2 entra en el 5 y la voz 3 en el 9."),
        arith("La voz 1 de un canon de 16 pulsos entra en el pulso 1. La voz 2 entra 8 pulsos después. ¿En qué pulso termina la voz 2?", "16+8", "La voz 2 termina 8 pulsos después del término de la voz 1.", ""),
    ],
    [ex("En una ronda de patio, un grupo canta una melodía y otro empieza cuando el primero termina la primera frase. ¿Qué forma musical están haciendo?", "Un canon", "La misma melodía entra en un momento distinto.")],
    [ex("¿Qué es un canon?", "La misma melodía que entra en momentos distintos", "Cada voz parte en un momento diferente."), ex("¿Qué hace la voz 1 antes de que entre la voz 2?", "Canta sola", "La voz 2 entra después."), ex("¿Qué ayuda a sostener tu parte en un canon?", "Marcar el pulso", "El pulso es la guía para seguir tu frase.")],
    (
        f"Con una o dos personas de tu casa (o con compañeros), canta «{CANTO1}» (inventa una melodía fácil y cómoda). Haz primero un unísono. Después haz un canon de dos voces: la voz 1 parte, y la voz 2 entra cuando la voz 1 termina la primera frase (4 pulsos). Marca el pulso con un pie. Escribe en qué pulso entró la voz 2, qué frase cantaba la voz 1 en ese momento y qué hiciste para sostener tu parte.",
        "La voz 2 entró en el pulso 5, cuando la voz 1 cantaba la frase 2. Para sostener mi parte marqué el pulso con el pie y escuché mi propia voz.",
        ["entra en el momento acordado", "mantiene su melodía sin copiar a la otra voz", "explica cómo sostuvo su parte"],
        ["interpretación", "registro escrito breve"],
        ["entrar antes de tiempo", "cantar lo mismo que la otra voz en cada momento"],
        "Reconoce la entrada puntual y pide marcar el pulso si la parte se desordena; si hay pérdida, vuelve a empezar la frase.",
    ),
    "Canta una frase al unísono con alguien y luego, en canon, entra cuando la primera persona termine esa frase.",
    "Crea un canon de tres voces con la misma frase y entradas cada 4 pulsos.",
)

# ---------------------------------------------------------------- OA 04 · clase 3
CLAVES = "X x x x X x x x"
TAMBOR = "X – x – X – x –"

L(
    OA4, 3,
    f"Lápiz, tus palmas y, si tienes, objetos seguros para golpear (dos cucharas de madera, una caja o un tambor pequeño), a volumen bajo. Código: X = golpe fuerte (acento), x = golpe suave, – = silencio. Partes de ejemplo de 8 pulsos: claves «{CLAVES}»; tambor «{TAMBOR}».",
    "Aprenderé a tocar instrumentos de percusión coordinados con un pulso y con acentos. Sirve para tocar juntos sin tapar ni apurar a los demás.",
    ["Sé mantener un pulso parejo.", "Sé que el acento es un golpe más fuerte.", "Sé leer una línea de golpes."],
    [
        "Los instrumentos de percusión se tocan golpeándolos, raspándolos o sacudiéndolos: el tambor, las claves, las maracas, el pandero y el triángulo son ejemplos. Para tocar juntos hay que coordinarse. Una persona o un instrumento marca el pulso parejo, y otro puede tocar un patrón sobre él. El acento es el golpe más fuerte y cae al comienzo de cada grupo de pulsos.",
        f"Leamos las partes de ejemplo, de 8 pulsos. Claves: {CLAVES}. Suenan en los 8 pulsos y tienen un acento cada 4 pulsos, en el 1 y en el 5. Tambor: {TAMBOR}. Suena solo en los pulsos 1, 3, 5 y 7 y deja silencio en los otros. Los dos coinciden en los acentos 1 y 5. Así las dos partes se encajan.",
        "Para coordinar bien, toca con cuidado y escucha las otras partes. Mantén el pulso incluso en los silencios. Si tu instrumento es el más fuerte, baja la intensidad para que se oigan los demás. Si te desordenas, vuelve al pulso 1 del siguiente grupo. Usa solo instrumentos que no se rompan y mantén un volumen bajo.",
    ],
    [("percusión", "instrumentos que se golpean, raspan o sacuden"), ("pulso", "latido parejo de la música"), ("acento", "golpe más fuerte al inicio de un grupo de pulsos"), ("silencio", "pulso en que no suena nada"), ("coordinarse", "tocar juntos, encajando las partes")],
    [
        ("Leer una parte", f"Parte del tambor: {TAMBOR}. ¿En qué pulsos suena el tambor?", ["Cuento los 8 símbolos.", "Suena en los pulsos 1, 3, 5 y 7.", "En los pulsos 2, 4, 6 y 8 hay silencio."], "En los pulsos 1, 3, 5 y 7"),
        ("Contar golpes juntos", f"Claves: {CLAVES}; tambor: {TAMBOR}. ¿En cuántos pulsos suenan las dos partes a la vez?", ["Las claves suenan en los 8 pulsos.", "El tambor suena en 4 pulsos.", "Coinciden en esos 4."], "En 4 pulsos"),
    ],
    [
        ("Apurarse en los pulsos que son de silencio.", "El silencio ocupa tiempo y desordena la parte.", "Cuenta el pulso mentalmente durante el silencio."),
        ("Tocar muy fuerte para destacar.", "Tapa a los demás y no se escucha el conjunto.", "Ajusta tu intensidad para que se oigan todas las partes."),
    ],
    [
        ex(f"Parte de las claves: {CLAVES}. ¿En qué pulsos van los acentos (X)?", "En los pulsos 1 y 5", "Las X aparecen en las posiciones 1 y 5."),
        ex("¿Qué instrumento de percusión se sacude: las maracas o el tambor?", "Las maracas", "Las maracas se sacuden."),
        ex(f"Parte del tambor: {TAMBOR}. ¿Cuántos silencios tiene?", "4", "Hay cuatro símbolos «–»."),
    ],
    [
        ex(f"Parte del tambor: {TAMBOR}. ¿Cuántos golpes fuertes (X) toca?", "2", "Hay una X en el pulso 1 y otra en el 5."),
        ex(f"Claves: {CLAVES}. ¿Cuántos golpes suaves (x) tocan?", "6", "Son 8 golpes y 2 son acentos: quedan 6 suaves."),
        ex("Si el acento va cada 4 pulsos en 8 pulsos, ¿en qué pulsos cae?", "En el 1 y en el 5", "Cada grupo de 4 empieza con acento."),
    ],
    [
        arith(f"Claves: {CLAVES}. Se tocan 3 vueltas. ¿Cuántos golpes suenan en total?", "8*3", "Cada vuelta tiene 8 golpes y hay 3 vueltas.", " golpes"),
        arith(f"Tambor: {TAMBOR}. Se tocan 4 vueltas. ¿Cuántos golpes suenan en total, sin contar silencios?", "4*4", "Cada vuelta tiene 4 golpes y hay 4 vueltas.", " golpes"),
        ex(f"Claves: {CLAVES}. Tambor: {TAMBOR}. ¿En cuántos pulsos suenan las claves pero el tambor está en silencio?", "4", "Las claves suenan en 8 y el tambor en 4; en los otros 4 el tambor calla."),
    ],
    [
        ex("Luis toca el tambor tan fuerte que no se oyen las claves. ¿Qué debe cambiar?", "Su intensidad", "Debe tocar más suave para que se oigan todas las partes."),
        ex("Una niña toca las claves y marca los acentos en los pulsos 1, 3, 5 y 7, no en el 1 y el 5. ¿Qué error comete?", "Pone acentos en pulsos que no los llevan", "Los acentos van solo al inicio de cada grupo."),
    ],
    [
        arith("Un grupo toca 3 partes de percusión de 8 pulsos cada una, una tras otra. ¿Cuántos pulsos dura la secuencia completa?", "3*8", "Se multiplican las partes por su duración.", " pulsos"),
        ex("Escribe una parte de 8 pulsos con acentos (X) en los pulsos 1 y 5, silencio (–) en los pulsos 4 y 8 y golpes suaves (x) en los demás.", "X x x – X x x –", "Los acentos van en 1 y 5, y los silencios en 4 y 8."),
    ],
    [ex("En un grupo, una niña marca siempre el pulso con unas claves, un niño toca un patrón con un tambor y otro agita unas maracas con suavidad. ¿Quién marca el pulso?", "La niña de las claves", "Ella toca el pulso parejo.")],
    [ex("¿Qué simboliza la X en las partes de percusión?", "Un golpe fuerte", "La X marca el acento."), ex("¿Qué simboliza «–»?", "Un silencio", "Es un pulso sin sonido."), ex("¿Qué debes hacer con tu intensidad si tu instrumento tapa a los demás?", "Bajarla", "Así se oyen todas las partes.")],
    (
        f"Toca con las palmas y con objetos seguros de tu casa (por ejemplo dos cucharas de madera sobre una caja) las partes de claves «{CLAVES}» y de tambor «{TAMBOR}»: primero cada una sola, después las dos con otra persona, a volumen bajo. Mantén el pulso incluso en los silencios. Escribe cuántos golpes toca cada parte en 3 vueltas y qué hiciste para no tapar a la otra persona.",
        "Claves: 8 golpes × 3 vueltas = 24. Tambor: 4 golpes × 3 vueltas = 12. Para no taparla toqué más suave en los golpes sin acento.",
        ["mantiene el pulso incluso en el silencio", "marca los acentos en los pulsos 1 y 5", "ajusta la intensidad para escucharse con la otra persona"],
        ["interpretación", "cálculo escrito"],
        ["acelerar en los silencios", "tocar muy fuerte"],
        "Reconoce el pulso estable; si se acelera en los silencios, pide contar mentalmente 1-2-3-4 con los pies.",
    ),
    "Camina con paso parejo y aplaude fuerte solo en los pasos 1 y 5 de cada grupo de 8.",
    "Escribe una nueva parte de 8 pulsos con X, x y – y tócala con otra persona sobre el pulso.",
)

# ---------------------------------------------------------------- OA 04 · clase 4
INSTR = [("tambor", "percusión"), ("pandero", "percusión"), ("metalófono", "melódico"), ("flauta dulce", "melódico"), ("guitarra", "armónico"), ("teclado", "armónico")]
INSTR_TXT = "; ".join(f"{n}: {t}" for n, t in INSTR)

L(
    OA4, 4,
    f"Lápiz, tu voz y, si tienes, un instrumento seguro de la casa (palmas, una caja, un metalófono, una flauta dulce propia). Cuida el volumen y no compartas la boquilla de una flauta. Clasificación de instrumentos de la clase: {INSTR_TXT}. Canción de ejemplo: «{CANTO1}».",
    "Aprenderé a integrar mi voz con un instrumento en una interpretación, repartiendo roles y cuidando el equilibrio. Sirve para presentar una música completa con varias partes.",
    ["Sé cantar al unísono.", "Sé mantener un pulso con percusión.", "Sé sostener mi parte en un canon."],
    [
        "Los instrumentos se agrupan por lo que hacen en la música. Los de percusión marcan el pulso y los acentos: el tambor y el pandero. Los melódicos tocan la melodía, es decir, los sonidos en orden como una canción: el metalófono y la flauta dulce. Los armónicos acompañan con varios sonidos a la vez, llamados acordes: la guitarra y el teclado.",
        f"Una interpretación integrada reparte roles. Por ejemplo, para «{CANTO1}»: la voz canta la melodía, un instrumento melódico la dobla suavemente, un instrumento armónico acompaña con acordes y la percusión marca el pulso. Se acuerda quién empieza (la introducción), cuántas veces se canta la canción y cómo se termina.",
        "El equilibrio es que se oiga cada parte. Si el instrumento tapa la voz, baja su intensidad. Las señales ayudan a entrar juntos: una cuenta de 4 pulsos, un movimiento de cabeza o un gesto de la mano. Antes de presentar, ensaya la entrada y el final. Cuida tu voz y tu instrumento y no toques tan fuerte que molestes a otras personas.",
    ],
    [("percusión", "marca pulso y acentos"), ("melódico", "toca la melodía"), ("armónico", "acompaña con acordes"), ("rol", "la tarea de cada integrante en la interpretación"), ("equilibrio", "que se oiga cada parte y ninguna tape a las otras")],
    [
        ("Clasificar un instrumento", f"Clasificación: {INSTR_TXT}. ¿Qué tipo de instrumento es la flauta dulce y qué hace en la música?", ["La lista dice melódico.", "Los melódicos tocan la melodía."], "Melódico; toca la melodía"),
        ("Planear la duración", "Una interpretación tiene una introducción de 4 pulsos, 3 vueltas de la canción de 16 pulsos y un final de 2 pulsos. ¿Cuántos pulsos dura?", ["Introducción: 4.", "Vueltas: 3 × 16 = 48.", "Final: 2.", "4 + 48 + 2 = 54."], "54 pulsos"),
    ],
    [
        ("Tocar el instrumento más fuerte que la voz.", "El instrumento tapa la melodía cantada.", "Baja la intensidad del instrumento para que se oiga la voz."),
        ("Entrar cada uno cuando quiere.", "No hay señal compartida y se desordena.", "Acuerden una señal: cuenta de 4 pulsos o gesto."),
    ],
    [
        ex(f"Clasificación: {INSTR_TXT}. ¿Qué tipo de instrumento es la guitarra?", "Armónico", "La lista dice que la guitarra es un instrumento armónico."),
        ex("¿Qué instrumento acompaña con acordes: el tambor o el teclado?", "El teclado", "El teclado es armónico."),
        ex("¿Qué señal ayuda a que todos entren juntos: una cuenta de 4 pulsos o cada uno por su cuenta?", "Una cuenta de 4 pulsos", "La cuenta marca el momento común de entrada."),
    ],
    [
        ex(f"Clasificación: {INSTR_TXT}. ¿Cuántos instrumentos de la lista son melódicos?", "2", "El metalófono y la flauta dulce son los melódicos."),
        ex("Un instrumento tapa la voz. ¿Qué debe cambiar el instrumentista?", "Su intensidad", "Debe tocar más suave para lograr equilibrio."),
        ex("¿Qué rol cumple la percusión en una interpretación: marcar el pulso o tocar acordes?", "Marcar el pulso", "La percusión marca el pulso y los acentos."),
    ],
    [
        arith("Una interpretación tiene 4 pulsos de introducción, 2 vueltas de la canción de 16 pulsos y 2 pulsos de final. ¿Cuántos pulsos dura?", "4+2*16+2", "Se suman la introducción, las dos vueltas y el final.", " pulsos"),
        arith("El grupo ensaya la canción de 16 pulsos 5 veces. ¿Cuántos pulsos ensaya en total?", "16*5", "Se multiplican los pulsos de la canción por los ensayos.", " pulsos"),
        arith("El grupo ensaya 3 veces seguidas la introducción de 4 pulsos y la canción de 16 pulsos. ¿Cuántos pulsos ensaya?", "3*(4+16)", "Cada ensayo suma la introducción y la canción.", " pulsos"),
    ],
    [
        ex("Un grupo tiene dos tambores y ninguna voz que lleve la melodía. ¿Falta qué rol?", "El de la melodía", "Los tambores marcan el pulso, pero nadie toca ni canta la melodía."),
        ex("Ana toca la flauta dulce y la voz canta la misma melodía. Dice que «no hace falta decidir quién entra primero». ¿Tiene razón?", "No", "Sin acuerdo sobre la entrada se desordenan."),
    ],
    [
        ex("Para cantar con tambor, metalófono y guitarra, ¿cuál de los tres instrumentos acompaña con acordes?", "La guitarra", "La guitarra es un instrumento armónico."),
        arith("Una presentación dura 54 pulsos y el pulso va a 2 pulsos por segundo. ¿Cuántos segundos dura?", "54//2", "Se divide el total de pulsos por los pulsos de cada segundo.", " segundos"),
    ],
    [ex("Un grupo canta con guitarra, tambor y metalófono. Cuando la guitarra se oye más fuerte que la voz, nadie entiende las palabras. ¿Qué ajuste de equilibrio es el correcto?", "Bajar la intensidad de la guitarra", "Así se oye la voz con claridad.")],
    [ex("¿Qué hace un instrumento melódico?", "Toca la melodía", "Toca los sonidos en orden como una canción."), ex("¿Qué hace un instrumento armónico?", "Acompaña con acordes", "Tiene varios sonidos a la vez."), ex("¿Qué es el equilibrio?", "Que se oiga cada parte", "Ninguna parte tapa a las otras.")],
    (
        f"Planifica con una o dos personas de tu casa una interpretación de «{CANTO1}» con voz y al menos un instrumento seguro de los que tengas (palmas, caja, metalófono, flauta dulce propia). Reparte roles (voz, melodía, acordes, percusión), acuerda la introducción y el final, ensaya la entrada con una cuenta de 4 pulsos y cuida el equilibrio. Escribe tu plan, cuántos pulsos dura tu interpretación y qué ajuste hiciste para que se oyera la voz.",
        "Roles: yo canto, otra persona marca el pulso con una caja. Introducción de 4 pulsos, 2 vueltas de 16 pulsos y final de 2: 4 + 32 + 2 = 38 pulsos. Bajé la intensidad de la caja para que se oyera la voz.",
        ["reparte los roles", "acuerda la entrada y el final", "calcula la duración", "ajusta el equilibrio"],
        ["plan escrito", "interpretación"],
        ["que un instrumento tape la voz", "no acordar la entrada"],
        "Reconoce el plan claro y pregunta cómo supieron cuándo entrar; si un instrumento tapa la voz, pide repetir con menos intensidad.",
    ),
    "Elige un instrumento de los de la clase y escribe qué tipo es (percusión, melódico o armónico).",
    "Practica una cuenta de 4 pulsos con un gesto para que tu grupo entre junto y anótala en tu plan.",
)
