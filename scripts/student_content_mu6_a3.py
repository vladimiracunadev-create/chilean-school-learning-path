"""Student material for 6.º básico Música, OA 03 (escucha abundante de músicas de diversos contextos y culturas: tradición escrita, tradición oral y popular, con música chilena y del mundo).

Todas las músicas de los ejercicios son descripciones originales inventadas; las audiciones reales (por ejemplo, las obras y artistas que nombra el OA) las selecciona y pone el docente.
Todo lo que se afirma de tradiciones es general; los significados y usos de la música de pueblos originarios los enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_content_mu6_a import L
from student_lessons import arith, ex

OA3 = "MU06 OA 03"
TIPOS = ("tradición escrita (docta): se escribe en partitura y suele tener un compositor conocido; tradición oral (folclor y música de pueblos originarios): se aprende escuchando y repitiendo, "
         "y pasa de una generación a otra; música popular (jazz, rock, fusión): se difunde por grabaciones, radio, conciertos y plataformas, y llega a un público amplio")

# ---------------------------------------------------------------- OA 03 · clase 1 (tradición escrita)
L(
    OA3, 1,
    f"Lápiz y papel. Tipos de música de la clase: {TIPOS}. Todas las músicas están descritas en los ejercicios. La profesora o el profesor puede poner obras reales (por ejemplo, de compositores chilenos y del mundo); en casa basta con las descripciones.",
    "Aprenderé a reconocer la música de tradición escrita (docta): cómo se escribe, quién la crea y con qué instrumentos suena. Sirve para escuchar con atención obras de compositores chilenos y del mundo y describir lo que se oye.",
    ["Sé que una melodía se puede escribir con símbolos o números.", "Sé nombrar instrumentos de cuerda, viento y percusión.", "Sé describir tempo y dinámica."],
    [
        "La música de tradición escrita, también llamada docta o académica, se anota en una partitura: un papel con los símbolos que indican las notas, su duración, el tempo y la dinámica. Gracias a la partitura, una obra puede tocarse con las mismas notas en otros lugares y muchos años después. Quien crea la obra es un compositor o una compositora.",
        "Estas obras se interpretan con instrumentos agrupados: una orquesta tiene familias de cuerdas (como violín y chelo), de viento (como flauta y trompeta) y de percusión (como timbal). Hay obras para un grupo pequeño, como un cuarteto de cuerdas (cuatro músicos), y obras para una orquesta completa. Una fanfarria es una pieza breve, con trompetas y percusión, hecha para anunciar algo importante.",
        "Para escuchar de manera apreciativa se presta atención sin hacer otra cosa y se describe lo que se oye: qué instrumentos tocan, si el tempo es lento o rápido, cómo cambia la dinámica y qué propósito parece tener. Chile tiene compositores de tradición escrita, igual que otros países; sus obras se escuchan junto a las del mundo. No se trata de decir «me gusta» o «no me gusta», sino de explicar qué se escucha.",
    ],
    [("partitura", "papel con los símbolos de una obra: notas, duraciones, tempo y dinámica"), ("compositor", "persona que crea una obra musical"), ("orquesta", "gran grupo con cuerdas, vientos y percusión"), ("fanfarria", "pieza breve de trompetas y percusión para anunciar algo"), ("escucha apreciativa", "escuchar con atención y describir lo que se oye")],
    [
        ("Clasificar la música", "Una obra de 10 minutos para orquesta, escrita por un compositor y leída de una partitura por 50 músicos. ¿Es de tradición escrita, oral o popular?", ["Está en una partitura y tiene compositor.", "Eso es propio de la tradición escrita."], "De tradición escrita"),
        ("Describir con atención", "Una fanfarria comienza en p con un solo timbal y, en 8 compases, llega a ff con trompetas. ¿Qué propósito expresivo tiene probablemente?", ["El crescendo y las trompetas dan solemnidad.", "Las fanfarrias se usan para anunciar algo importante."], "Anunciar algo importante con solemnidad"),
    ],
    [
        ("Creer que toda música con violines es docta.", "Los violines también tocan folclor y música popular; lo que define la tradición es cómo se crea y se transmite.", "Pregunta si está escrita en partitura y tiene compositor conocido."),
        ("Decir que una obra «es aburrida» sin describirla.", "Una escucha apreciativa explica lo que se oye, no solo el gusto.", "Nombra instrumentos, tempo, dinámica y propósito."),
    ],
    [
        ex("¿Dónde queda escrita una obra docta para que otras personas la lean?", "En la partitura", "La partitura reúne los símbolos de la obra."),
        ex("¿Quién crea una obra de tradición escrita: el compositor o el público?", "El compositor", "El compositor o la compositora escribe la obra."),
        ex("Una pieza breve de trompetas y percusión para anunciar un acto importante, ¿cómo se llama?", "Fanfarria", "Esa es la definición de fanfarria."),
    ],
    [
        ex("¿Cuál de estos instrumentos pertenece a la familia de las cuerdas: violín, flauta o trompeta?", "Violín", "La flauta y la trompeta son de viento."),
        ex("Una obra se escribe para 4 instrumentos de cuerda. ¿Es un cuarteto o una orquesta completa?", "Un cuarteto", "Cuarteto significa un grupo de cuatro."),
        ex("Una fanfarria suele sonar con trompetas y percusión. ¿Qué es más típico en ella: una guitarra eléctrica o un timbal?", "Un timbal", "El timbal es percusión de orquesta."),
    ],
    [
        arith("Una orquesta escolar tiene 20 instrumentos de cuerda, 10 de viento y 4 de percusión. ¿Cuántos instrumentos tiene en total?", "20+10+4", "Se suman las tres familias.", " instrumentos"),
        ex("Cuenta cuántas de estas músicas son de tradición escrita: (1) sinfonía leída de una partitura, (2) rock con guitarra eléctrica, (3) cuarteto de cuerdas con compositora conocida, (4) canto de cuna aprendido de oído.", "2", "Son la (1) y la (3); la (2) es popular y la (4) es de tradición oral."),
        arith("Una fanfarria tiene 8 compases de 4 pulsos y va a 96 pulsos por minuto. ¿Cuántos segundos dura?", "8*4*60//96", "Son 32 pulsos y cada pulso dura 0,625 segundos.", " segundos"),
    ],
    [
        ex("Camila dice que toda música con violines es docta. ¿Tiene razón?", "No: los violines también tocan folclor y música popular", "Lo que define la tradición es cómo se crea y se transmite, no un instrumento."),
        ex("La misma obra se interpreta en dos países con dos orquestas distintas. ¿Qué se mantiene igual: las notas escritas o el sonido exacto de cada orquesta?", "Las notas escritas", "La partitura fija las notas; el sonido cambia con los músicos."),
    ],
    [
        arith("Un cuarteto de cuerdas tiene 4 músicos. ¿Cuántos cuartetos completos se arman con 60 músicos de cuerdas?", "60//4", "Se reparten los músicos de a 4.", " cuartetos"),
        ex("Una obra empieza con una flauta sola en p, luego entran las cuerdas y termina en ff con todos los instrumentos. ¿Qué dos recursos usa para crecer: tempo y rango o textura y dinámica?", "Textura y dinámica", "Entran más instrumentos (textura) y sube el volumen (dinámica)."),
    ],
    [ex("Tu curso quiere que otro curso toque exactamente las mismas notas y duraciones de una melodía que inventaron. ¿Qué deben entregar: una partitura o un relato de cómo suena?", "Una partitura", "La partitura fija notas y duraciones para que otros las lean.")],
    [ex("¿Cómo se llama el gran grupo con cuerdas, vientos y percusión?", "Orquesta", "Esa es la definición de orquesta."), ex("¿Qué es una escucha apreciativa?", "Escuchar con atención y describir lo que se oye", "No se limita al gusto."), ex("¿Qué familia de la orquesta incluye el timbal?", "Percusión", "El timbal se golpea.")],
    (
        "Lee esta descripción y completa una ficha de escucha: «Obra para orquesta de 5 minutos, escrita por un compositor y leída de una partitura. Empieza lenta y suave con cuerdas. A mitad entran trompetas y timbales y el volumen crece hasta ff. Termina rápido y con todos los instrumentos.» En tu ficha escribe: tradición, tres rasgos del lenguaje musical (tempo, dinámica, textura) y el propósito expresivo que crees que tiene.",
        "Tradición escrita (orquesta, partitura). Rasgos: tempo que pasa de lento a rápido, dinámica con crescendo de p a ff y textura que crece al entrar más instrumentos. Propósito: construir una llegada importante o un final lleno de energía.",
        ["identifica la tradición", "nombra tres rasgos con evidencia", "explica un propósito"],
        ["ficha escrita"],
        ["decir solo «me gusta»", "mezclar dinámica con tempo"],
        "Reconoce la ficha y pide señalar en la descripción la frase que justifica cada rasgo.",
    ),
    "Cuenta los instrumentos de la orquesta escolar de los ejercicios y agrúpalos por familia.",
    "Escribe la descripción de una fanfarria de 8 compases para anunciar un cumpleaños: tempo, dinámica e instrumentos.",
)

# ---------------------------------------------------------------- OA 03 · clase 2 (tradición oral: folclor y pueblos originarios)
L(
    OA3, 2,
    f"Lápiz y papel. Tipos de música de la clase: {TIPOS}. Todas las músicas están descritas en los ejercicios. Para música de pueblos originarios, quien enseña la forma tradicional es el educador/a tradicional o la comunidad; aquí solo se describe en general.",
    "Aprenderé a reconocer la música de tradición oral (folclor y música de pueblos originarios): cómo se aprende, cómo cambia y para qué sirve en una comunidad. Sirve para escuchar con respeto músicas que no están escritas.",
    ["Sé que la tradición escrita usa partituras.", "Sé que una canción puede cantarse en familia.", "Sé comparar dos listas de números."],
    [
        "La música de tradición oral se aprende escuchando y repitiendo, sin necesidad de partitura, y pasa de una generación a otra. El folclor es la música tradicional de un pueblo: canciones, bailes y juegos que una comunidad cantó durante muchos años. Muchas veces no se conoce quién fue su autor, porque pertenece a la comunidad.",
        "Como se aprende de oído, una misma canción puede tener versiones: cada persona o lugar la canta con pequeños cambios en la letra, la melodía o el ritmo. Eso no la hace «equivocada»: forma parte de la tradición. Los usos pueden ser fiestas, trabajos, juegos, canciones de cuna o ceremonias. En Chile hay folclor como la cueca y la tonada.",
        "Los pueblos originarios, como el mapuche y el aymara, tienen músicas con instrumentos propios, por ejemplo el kultrún, que es un tambor mapuche, y la trutruka y la pifilka, que son instrumentos de viento mapuche. Sus significados y usos los enseña el educador/a tradicional o la comunidad; en esta clase solo reconocemos que son músicas de tradición oral y las escuchamos con respeto y sin burla.",
    ],
    [("tradición oral", "forma de aprender música escuchando y repitiendo, de generación en generación"), ("folclor", "música tradicional de un pueblo, que cantan y bailan sus comunidades"), ("versión", "forma en que una persona o lugar canta una misma canción, con pequeños cambios"), ("kultrún", "tambor del pueblo mapuche"), ("educador/a tradicional", "persona de la comunidad que enseña los saberes de su pueblo")],
    [
        ("Reconocer la transmisión", "Una canción de cuna la aprendió Rosa escuchándola a su abuela y la canta a su hermana pequeña, sin papel. ¿De qué tradición es?", ["No hay partitura.", "Se aprendió escuchando y se pasa a otra generación."], "De tradición oral"),
        ("Comparar versiones", "Versión del norte: 1-2-3-1. Versión del sur: 1-2-3-3. ¿Cuántas notas cambian entre las dos?", ["Comparo nota por nota: 1=1, 2=2, 3=3, pero 1≠3.", "Cambia solo la última."], "1 nota"),
    ],
    [
        ("Pensar que una canción de tradición oral está mal si dos personas la cantan distinto.", "Las versiones forman parte de la tradición oral.", "Describe qué cambia entre versiones sin decir cuál es la única correcta."),
        ("Inventar el significado de una música de un pueblo originario.", "Los significados los enseña el educador/a tradicional o la comunidad; no se inventan.", "Describe lo que se oye y pregunta a quien corresponda."),
    ],
    [
        ex("¿Cómo se aprende la música de tradición oral: leyendo partitura o escuchando y repitiendo?", "Escuchando y repitiendo", "No necesita partitura."),
        ex("El kultrún, ¿es un tambor o un instrumento de viento?", "Un tambor del pueblo mapuche", "Es un instrumento de percusión mapuche."),
        ex("¿Quién enseña el significado de una música de un pueblo originario: el educador/a tradicional o una persona que lo inventa?", "El educador/a tradicional o la comunidad", "Ellos conocen y transmiten el saber."),
    ],
    [
        ex("Dos niñas cantan la misma ronda con una palabra distinta. ¿Qué tienen: dos versiones o dos canciones totalmente distintas?", "Dos versiones", "Es la misma canción con un pequeño cambio."),
        ex("La cueca y la tonada, ¿son ejemplos de folclor chileno o de rock?", "De folclor chileno", "Son música tradicional de Chile."),
        ex("La trutruka y la pifilka, ¿son instrumentos de percusión o de viento?", "De viento", "Se soplan para producir sonido."),
    ],
    [
        arith("Una canción tradicional se la enseñó una abuela a 3 nietos y cada nieto se la enseñó a 4 amigos. ¿Cuántos amigos aprendieron la canción?", "3*4", "Cada uno de los 3 nietos enseñó a 4.", " amigos"),
        ex("Cuenta cuántas de estas músicas son de tradición oral: (1) canto de cuna aprendido de oído, (2) sinfonía leída de partitura, (3) ronda infantil heredada, (4) rock con guitarra eléctrica.", "2", "Son la (1) y la (3)."),
        ex("Versión A: 5-4-3-2-1. Versión B: 5-4-3-3-1. ¿Cuántas notas cambian?", "1", "Solo la cuarta pasa de 2 a 3."),
    ],
    [
        ex("Julia dice que una canción folclórica sin partitura es «menos música». ¿Tiene razón?", "No: es otra tradición, que se aprende de oído", "La tradición oral es música completa, con su propia forma de transmitirse."),
        ex("En una comunidad, una canción se canta en la fiesta de cada año con pequeños cambios por quien la dirige. ¿Qué lo explica: la tradición oral con versiones o un error del cantante?", "La tradición oral con versiones", "Las versiones son normales cuando se transmite de oído."),
    ],
    [
        arith("Una ronda tiene 4 estrofas de 8 compases de 2 pulsos. ¿Cuántos pulsos tiene entera?", "4*8*2", "Se multiplican estrofas, compases y pulsos.", " pulsos"),
        ex("Un investigador anota en un cuaderno cada versión de una misma canción: 3 de la costa, 4 de la montaña y 2 del valle. ¿Cuántas versiones anotó?", "9", "3 + 4 + 2 = 9."),
    ],
    [ex("Una cantora de tu comunidad canta una tonada que aprendió escuchando a una persona mayor, y la canta con una estrofa distinta a la que canta otro vecino. ¿De qué tradición es y por qué las estrofas pueden ser distintas?", "De tradición oral; porque se aprende de oído y cada persona la canta con pequeñas diferencias", "En la tradición oral aparecen versiones.")],
    [ex("¿Cómo se llama la música tradicional que cantan y bailan las comunidades de un pueblo?", "Folclor", "Se canta y se baila en las comunidades."), ex("En Música: ¿Qué es una versión?", "La forma en que una persona o lugar canta una misma canción", "Tiene pequeños cambios."), ex("¿Qué debemos hacer con una música que no conocemos de otro pueblo?", "Escucharla con respeto", "No burlarse ni inventar su significado.")],
    (
        "Lee estas dos versiones de una canción de cuna inventada para esta actividad. Versión de la casa A: «Duérmete, luna blanca» con melodía 3-2-1-1 y tempo lento. Versión de la casa B: «Duérmete, luna clara» con melodía 3-2-1-3 y el mismo tempo. Escribe qué cambió, qué se mantiene y por qué ambas son válidas. Si puedes, pregunta a una persona de tu casa si conoce una canción de cuna y escribe una frase sobre cómo la aprendió.",
        "Cambió una palabra (blanca/clara) y la última nota (de 1 a 3). Se mantiene el tempo lento, el diseño de las tres primeras notas y la idea de arrullar. Ambas son válidas porque en la tradición oral cada lugar canta su versión.",
        ["señala lo que cambia", "señala lo que se mantiene", "explica por qué las versiones son válidas"],
        ["texto escrito"],
        ["decir que una versión está equivocada", "no mencionar lo que se mantiene"],
        "Reconoce el análisis y pide señalar, nota por nota, dónde cambia y dónde coincide.",
    ),
    "Comparte con alguien de tu casa una canción de cuna que ya conozcas y anota si la cantan igual.",
    "Escribe una tercera versión de la canción de cuna de los ejercicios cambiando solo una nota.",
)

# ---------------------------------------------------------------- OA 03 · clase 3 (música popular: jazz, rock, fusión)
L(
    OA3, 3,
    f"Lápiz y papel. Tipos de música de la clase: {TIPOS}. Todas las músicas están descritas en los ejercicios. Si escuchas música popular, hazlo a volumen bajo.",
    "Aprenderé a reconocer la música popular (jazz, rock y fusión): cómo se hace, con qué instrumentos suena y por qué llega a tanta gente. Sirve para describir lo que escucho a diario con las mismas palabras que usamos para otras músicas.",
    ["Sé que la música puede ser de tradición escrita u oral.", "Sé nombrar instrumentos como guitarra, bajo y batería.", "Sé calcular duraciones con el tempo."],
    [
        "La música popular se difunde por grabaciones, radio, conciertos y plataformas, y la escucha un público muy amplio. Sus canciones suelen tener autores conocidos y una forma clara, por ejemplo estrofas y un estribillo que se repite. Incluye muchos estilos; en esta clase conocemos tres: jazz, rock y fusión.",
        "El jazz nació en Estados Unidos y se caracteriza por la improvisación: una persona inventa una melodía en el momento sobre un acompañamiento. El rock suele usar guitarra eléctrica, bajo eléctrico y batería, con pulso marcado y volumen fuerte. La fusión mezcla estilos de distintas músicas, por ejemplo rock con ritmos folclóricos o jazz con instrumentos de otros países.",
        "Al escuchar música popular se describen los mismos elementos que en otras músicas: pulso, tempo, dinámica, forma y textura. Por ejemplo: «es una canción en forma estrofa-estribillo, con tempo moderado, y en el estribillo entran todos los instrumentos». También se pregunta qué la hace parecida o distinta a la tradición oral y a la escrita: en la popular casi siempre hay una grabación que la fija, pero cada concierto puede variar.",
    ],
    [("música popular", "música que se difunde mucho por grabaciones y medios y llega a un público amplio"), ("improvisación", "inventar música en el momento sobre un acompañamiento"), ("rock", "estilo con guitarra eléctrica, bajo y batería, de pulso marcado"), ("fusión", "mezcla de estilos de distintas músicas"), ("estribillo", "parte de una canción que se repite igual")],
    [
        ("Reconocer el estilo", "Un grupo toca guitarra eléctrica, bajo y batería con pulso marcado y volumen fuerte. ¿Qué estilo es más probable: rock o folclor de cuna?", ["Guitarra eléctrica, bajo y batería son típicos del rock.", "El folclor de cuna es suave."], "Rock"),
        ("Contar secciones", "Una canción tiene 3 estrofas de 8 compases y 2 estribillos de 4 compases. ¿Cuántos compases dura?", ["Estrofas: 3 × 8 = 24 compases.", "Estribillos: 2 × 4 = 8 compases.", "24 + 8 = 32."], "32 compases"),
    ],
    [
        ("Creer que popular significa «de poca calidad».", "Popular quiere decir que llega a mucha gente; hay música popular muy compleja.", "Descríbela con los mismos elementos que otras músicas."),
        ("Pensar que todo lo que usa guitarra es rock.", "La guitarra aparece en folclor, en jazz y en otros estilos.", "Mira el conjunto: instrumentos, ritmo y volumen."),
    ],
    [
        ex("¿Qué estilo se caracteriza por la improvisación: el jazz o la fanfarria?", "El jazz", "En el jazz una persona inventa una melodía en el momento."),
        ex("¿Qué instrumentos usa el rock con más frecuencia: guitarra eléctrica, bajo y batería o violines y flautas?", "Guitarra eléctrica, bajo y batería", "Esa es la formación típica del rock."),
        ex("¿Cómo se llama la parte de una canción que se repite igual?", "Estribillo", "El estribillo vuelve igual después de cada estrofa."),
    ],
    [
        ex("Una canción mezcla un ritmo folclórico con guitarra eléctrica y batería. ¿Qué es: jazz, fusión o fanfarria?", "Fusión", "Mezcla dos estilos."),
        ex("Una solista inventa una melodía en el momento sobre un bajo y una batería. ¿Qué hace?", "Improvisar", "Inventa música en el momento."),
        ex("Una canción tiene estrofa, estribillo, estrofa, estribillo. ¿Cuántas veces suena el estribillo?", "2", "Aparece después de cada estrofa y son 2 estrofas."),
    ],
    [
        arith("Una canción va a 120 pulsos por minuto y tiene 64 pulsos. ¿Cuántos segundos dura?", "64*60//120", "Cada pulso dura medio segundo.", " segundos"),
        ex("Cuenta cuántas de estas músicas son populares: (1) rock con batería, (2) canto de cuna de la abuela, (3) jazz con solista que improvisa, (4) fanfarria leída de partitura.", "2", "Son la (1) y la (3)."),
        arith("Una banda toca 4 canciones de 3 minutos y 2 canciones de 5 minutos. ¿Cuántos minutos suena en total?", "4*3+2*5", "Se calcula cada grupo y se suman.", " minutos"),
    ],
    [
        ex("Mateo dice que una grabación es lo mismo que una partitura. ¿Cuál es la diferencia principal?", "La grabación guarda el sonido; la partitura guarda los símbolos para interpretarla", "Una se escucha y la otra se lee."),
        ex("En un concierto de jazz la misma canción dura 4 minutos en la grabación y 7 minutos en vivo, porque cada solista improvisa. ¿Qué explica la diferencia: la improvisación o un error?", "La improvisación", "En el jazz cada vez se improvisa algo distinto."),
    ],
    [
        ex("Una canción va estrofa, estribillo, estrofa, estribillo, y las dos estrofas tienen la misma música. Si A es la estrofa y B el estribillo, ¿qué forma tiene escrita con letras?", "ABAB", "Alternan la estrofa A y el estribillo B dos veces."),
        arith("Un grupo de rock ensaya 3 canciones de 4 minutos cada una, dos veces cada una. ¿Cuántos minutos ensaya?", "3*4*2", "Cada canción dura 4 min y se toca 2 veces.", " minutos"),
    ],
    [ex("En una fiesta del curso se mezcla una cueca con guitarra eléctrica y batería. ¿Cómo describirías esa música: fusión o música de tradición escrita?", "Fusión", "Mezcla folclor y rock.")],
    [ex("¿Qué es el jazz?", "Un estilo popular que se basa en la improvisación", "Nació en Estados Unidos."), ex("¿Qué significa fusión?", "Mezcla de estilos", "Une elementos de distintas músicas."), ex("¿Cómo llega la música popular a mucha gente?", "Por grabaciones, radio, conciertos y plataformas", "Eso la difunde.")],
    (
        "Escribe una ficha de escucha para esta canción inventada: «Rock fusión de 3 minutos a 100 pulsos por minuto. Empieza con guitarra eléctrica y batería, el volumen crece en el estribillo. A la mitad hay un solo improvisado de flauta. Termina con un ritardando.» Anota estilo, tempo (según los rangos de la clase), dos rasgos de dinámica o forma y el propósito expresivo.",
        "Estilo: rock con fusión (guitarra eléctrica y flauta). Tempo moderado (100 por minuto). Rasgos: crescendo en el estribillo y un solo improvisado en el medio. Propósito: dar energía en el estribillo y mostrar creatividad en el solo; el ritardando cierra con calma.",
        ["nombra el estilo", "clasifica el tempo con el rango", "da evidencia del propósito"],
        ["ficha escrita"],
        ["usar solo «me gusta»", "no usar los rangos de tempo"],
        "Reconoce el análisis y pide ubicar cada rasgo en la descripción.",
    ),
    "Cuenta cuántas veces se repite el estribillo en una canción que conoces.",
    "Escribe la descripción de una fusión entre cueca y jazz: instrumentos, tempo e improvisación.",
)

# ---------------------------------------------------------------- OA 03 · clase 4 (música chilena y sus orígenes e influencias)
L(
    OA3, 4,
    f"Lápiz y papel. Tipos de música de la clase: {TIPOS}. Todas las músicas están descritas en los ejercicios. Los significados de la música de pueblos originarios los enseña el educador/a tradicional o la comunidad.",
    "Aprenderé a reconocer los orígenes e influencias de la música chilena: aportes de pueblos originarios, de la música traída de Europa y de estilos populares como el rock. Sirve para entender por qué la música de Chile suena como suena.",
    ["Sé reconocer música de tradición escrita, oral y popular.", "Sé que hay pueblos originarios en Chile, como el mapuche y el aymara.", "Sé que la fusión mezcla estilos."],
    [
        "La música chilena tiene varios orígenes. Los pueblos originarios aportaron músicas e instrumentos propios, como el kultrún y la trutruka mapuches. Con los españoles llegaron instrumentos como la guitarra y la música de tradición escrita europea. Con el tiempo, estas influencias se mezclaron y dieron origen al folclor chileno, como la cueca y la tonada.",
        "En el siglo veinte, cantautores y grupos folclóricos llevaron esas músicas a nuevos públicos, y algunos compositores de tradición escrita se inspiraron en la música de los pueblos originarios y del campo. Más tarde, el rock, el jazz y otros estilos populares también influyeron: hay bandas de rock chileno y grupos que tocan la cueca con un sonido urbano.",
        "Al escuchar música chilena se puede preguntar: ¿qué instrumentos usa?, ¿suena a folclor, a música de pueblos originarios, a tradición escrita o a popular?, ¿hay una mezcla? Para responder, mira los rasgos: el instrumento, el ritmo, la forma y el propósito. Algunas obras reúnen varias influencias a la vez, y eso se llama fusión. Los repertorios concretos los elige el docente.",
    ],
    [("origen", "de dónde viene una música o un instrumento"), ("influencia", "aporte de otra música o cultura que cambia una música"), ("cantautor", "persona que escribe y canta sus propias canciones"), ("folclor chileno", "música tradicional de Chile, como la cueca y la tonada"), ("fusión", "mezcla de varias influencias en una misma obra")],
    [
        ("Identificar influencias", "Una obra usa trutruka, guitarra y batería con una melodía de tonada. ¿Qué influencias reúne?", ["La trutruka viene de la música mapuche.", "La guitarra llegó con los españoles y suena en la tonada, que es folclor chileno.", "La batería viene de estilos modernos como el rock."], "Mapuche, folclor (con guitarra de origen europeo) y estilos populares modernos"),
        ("Contar influencias", "Una obra usa kultrún (pueblo mapuche), violín (tradición escrita) y guitarra eléctrica (rock). ¿Cuántas influencias distintas tiene?", ["Kultrún: mapuche.", "Violín: tradición escrita.", "Guitarra eléctrica: rock.", "Cada uno es de un origen distinto: 3."], "3 influencias"),
    ],
    [
        ("Creer que la música chilena tiene un solo origen.", "Tiene varios: pueblos originarios, música traída de Europa y estilos populares modernos.", "Busca qué instrumentos y ritmos señalan cada influencia."),
        ("Explicar el significado de una música de un pueblo originario sin conocerlo.", "Su significado lo enseña el educador/a tradicional o la comunidad.", "Describe solo lo que se oye."),
    ],
    [
        ex("¿Qué instrumento mapuche es un tambor?", "El kultrún", "El kultrún es un tambor del pueblo mapuche."),
        ex("¿Qué instrumento llegó con los españoles: la guitarra o el kultrún?", "La guitarra", "El kultrún es mapuche."),
        ex("La cueca y la tonada, ¿son folclor o música de tradición escrita?", "Folclor", "Son música tradicional chilena."),
    ],
    [
        ex("Un grupo toca una cueca con guitarra eléctrica y batería. ¿Qué influencias reúne: folclor y rock o solo fanfarria?", "Folclor y rock", "La cueca es folclor y la guitarra eléctrica con batería es rock."),
        ex("Un compositor de tradición escrita usa en una obra para orquesta una melodía inspirada en música del campo. ¿Qué tradición es la obra?", "De tradición escrita, con influencia del folclor", "Está escrita para orquesta e inspirada en el campo."),
        ex("Una cantautora escribe y canta sus propias canciones con guitarra. ¿Qué hace una cantautora: crea e interpreta o solo interpreta?", "Crea e interpreta", "Cantautor significa que escribe y canta."),
    ],
    [
        ex("Cuenta cuántas influencias hay en una obra con trutruka, una melodía de tonada y batería de rock.", "3", "Mapuche, folclor y rock."),
        arith("Una antología tiene 15 músicas: 6 de tradición escrita, 5 de folclor y el resto de música popular. ¿Cuántas son populares?", "15-6-5", "Se restan las dos cantidades conocidas del total.", " músicas"),
        arith("Una audición dura 3 minutos de música mapuche, 4 de cueca y 5 de rock chileno. ¿Cuántos minutos suena en total?", "3+4+5", "Se suman los tres tiempos.", " minutos"),
    ],
    [
        ex("Luis dice que una cueca con batería ya no es folclor. ¿Qué es más preciso decir: que es una fusión o que está mal?", "Que es una fusión", "Mezcla folclor con un instrumento de rock."),
        ex("Una obra mezcla melodía de tonada, kultrún y orquesta. ¿Qué dos tradiciones de las tres de la clase reúne?", "La oral (folclor y pueblos originarios) y la escrita", "La tonada y el kultrún son de tradición oral y la orquesta es de tradición escrita."),
    ],
    [
        ex("Una obra: 8 compases de kultrún solo, luego 8 compases con guitarra que se suma, luego 8 compases con orquesta. ¿Qué textura crece: más capas de sonido o menos?", "Más capas de sonido", "Se van sumando instrumentos."),
        arith("En un festival suenan 3 grupos de folclor de 12 minutos, 2 de rock de 15 minutos y 1 de orquesta de 20 minutos. ¿Cuántos minutos dura todo?", "3*12+2*15+20", "Se calcula cada grupo y se suman.", " minutos"),
    ],
    [ex("En una fiesta de aniversario de tu escuela tocan una cueca, un rock y una obra de orquesta. ¿Cuántas tradiciones distintas de las tres de la clase aparecen?", "3", "Folclor (oral), rock (popular) y orquesta (escrita).")],
    [ex("¿Cuáles son tres orígenes de la música chilena?", "Pueblos originarios, música traída de Europa y estilos populares modernos", "Esas son las influencias de la clase."), ex("Una música que mezcla varias influencias, ¿cómo se llama?", "Fusión", "Reúne rasgos de distintas músicas."), ex("¿Quién enseña los significados de la música de un pueblo originario?", "El educador/a tradicional o la comunidad", "Ellos transmiten el saber.")],
    (
        "Lee esta ficha inventada. «Obra chilena de 4 minutos: empieza con kultrún y trutruka a tempo lento. Entra una guitarra con una melodía de tonada. Al final se suman batería y bajo eléctrico y el volumen sube a f.» Escribe qué influencias reúne cada instrumento, la tradición de cada parte (oral, escrita o popular) y qué propósito expresivo puede tener el crecimiento del final.",
        "Kultrún y trutruka: pueblos originarios (tradición oral). Guitarra y melodía de tonada: folclor (tradición oral). Batería y bajo eléctrico: estilos populares (rock). El crecimiento final da energía y fuerza, como una fiesta que se va sumando.",
        ["asocia cada instrumento con su origen", "clasifica la tradición", "da un propósito con evidencia"],
        ["ficha escrita"],
        ["inventar significados de la música de un pueblo originario", "no nombrar las influencias"],
        "Reconoce el análisis y recuerda que el significado tradicional lo enseña la comunidad.",
    ),
    "Anota dos instrumentos que conoces e indica si vienen de pueblos originarios, de Europa o de estilos modernos.",
    "Describe una obra fusión de tu invención con tres influencias y explica qué instrumento aporta cada una.",
)

# ---------------------------------------------------------------- OA 03 · clase 5 (escucha abundante y registro)
L(
    OA3, 5,
    f"Lápiz y papel. Tipos de música de la clase: {TIPOS}. Las fichas están escritas en los ejercicios. La profesora o el profesor selecciona las músicas reales; en casa puedes usar la lista de pasos. Cuida el volumen.",
    "Aprenderé a organizar una escucha abundante de al menos 15 músicas variadas, cortas y medianas, y a registrarla con una ficha. Sirve para comparar tradiciones, estilos y propósitos con datos.",
    ["Sé reconocer tradición escrita, oral y popular.", "Sé describir tempo, dinámica y forma.", "Sé sumar y restar para llevar una cuenta."],
    [
        "Escuchar de manera abundante significa escuchar muchas músicas variadas, no solo una vez la misma. La meta de este OA es escuchar apreciativamente al menos 15 músicas de corta y mediana duración. En esta clase llamamos corta a una música de hasta 5 minutos y mediana a una de más de 5 y hasta 15 minutos (rangos de referencia).",
        "Para que la escucha sea variada conviene repartir las 15 músicas entre las tres tradiciones y entre músicas chilenas y del mundo. Cada escucha se registra en una ficha con: título o descripción, tradición, duración, dos rasgos del lenguaje musical y el propósito expresivo. Al juntar las fichas se pueden contar y comparar: cuántas de cada tradición, cuántas cortas y cuántas medianas.",
        "La escucha apreciativa tiene reglas: se escucha completa, sin hacer otra cosa, a volumen seguro y con respeto por todas las músicas, aunque no las conozcas o no sean tus favoritas. Puedes decir que algo te gusta más o menos, siempre que lo expliques con lo que se oye. Después de varias fichas, compara: ¿qué cambia de una tradición a otra? ¿qué se parece?",
    ],
    [("escucha abundante", "escuchar muchas músicas variadas, repartidas entre tradiciones"), ("ficha de escucha", "registro de título, tradición, duración, rasgos y propósito"), ("música corta y mediana", "hasta 5 minutos y más de 5 hasta 15 minutos (referencia de la clase)"), ("variedad", "mezcla de tradiciones, épocas y lugares"), ("comparar", "decir qué se parece y qué cambia entre dos músicas")],
    [
        ("Repartir la escucha", "Para 15 músicas quieres 5 de cada tradición (escrita, oral y popular). ¿Cuántas músicas de cada tradición necesitas si repartes parejo?", ["15 músicas entre 3 tradiciones.", "15 ÷ 3 = 5."], "5 de cada una"),
        ("Clasificar la duración", "Una música dura 7 minutos. ¿Es corta o mediana según los rangos de la clase?", ["Corta: hasta 5 minutos.", "Mediana: más de 5 y hasta 15.", "7 está entre 5 y 15."], "Mediana"),
    ],
    [
        ("Escuchar solo música que ya te gusta.", "La escucha abundante busca variedad, no solo gustos propios.", "Reparte las escuchas entre tradiciones."),
        ("Llenar la ficha con «linda» y «bonita».", "La ficha necesita rasgos audibles y propósito.", "Escribe tempo, dinámica, forma o textura."),
    ],
    [
        ex("¿Cuántas músicas, como mínimo, pide escuchar el OA?", "15", "El OA dice al menos 15 músicas variadas."),
        ex("Una música dura 3 minutos. ¿Es corta o mediana?", "Corta", "Dura hasta 5 minutos."),
        ex("¿Qué datos pide la ficha de la clase además del título o descripción?", "La tradición, la duración, dos rasgos y el propósito", "La ficha de la clase pide esos datos."),
    ],
    [
        ex("Una música dura 14 minutos. ¿Corta o mediana?", "Mediana", "Es más de 5 y hasta 15."),
        ex("Una ficha dice: «Música: canción de cuna. Tradición: oral. Duración: 4 minutos. Rasgos: tempo lento y voz sola. Propósito: arrullar». ¿Está completa?", "Sí", "Tiene descripción, tradición, duración, dos rasgos y propósito."),
        ex("Una ficha dice: «Tradición: popular. Me gustó mucho». ¿Qué le falta?", "El título o descripción, la duración, dos rasgos del lenguaje musical y el propósito", "Una ficha necesita evidencia audible."),
    ],
    [
        arith("Ya escuchaste 9 músicas de las 15 que se piden. ¿Cuántas te faltan?", "15-9", "Se restan las escuchadas del total.", " músicas"),
        arith("Escuchaste 4 músicas de 3 minutos y 3 de 6 minutos. ¿Cuántos minutos escuchaste?", "4*3+3*6", "Se calcula cada grupo y se suman.", " minutos"),
        ex("Tus fichas dicen: 6 escritas, 4 orales y 5 populares. ¿Cuál tradición tiene más escuchas?", "La escrita", "6 es mayor que 4 y que 5."),
    ],
    [
        ex("Un curso escuchó 15 músicas: 7 chilenas y el resto del mundo. ¿Cuántas fueron del mundo?", str(15 - 7), "15 − 7 = 8."),
        ex("Un estudiante escuchó 15 músicas y todas eran populares. ¿Qué le falta a su escucha para ser variada?", "Músicas de tradición escrita y de tradición oral", "La variedad pide repartir entre las tres tradiciones."),
    ],
    [
        arith("Un plan de escucha tiene 15 músicas: 5 minutos de cada una en promedio. ¿Cuántos minutos son en total?", "15*5", "Se multiplica el número de músicas por su duración promedio.", " minutos"),
        arith("Si escuchas 3 músicas por semana, ¿cuántas semanas necesitas para llegar a 15?", "15//3", "15 músicas repartidas de a 3.", " semanas"),
    ],
    [ex("Planificas tu semana: lunes, miércoles y viernes escucharás 2 músicas cada día. ¿Cuántas escuchas harás esa semana?", "6", "3 días × 2 músicas = 6.")],
    [ex("¿Qué se escribe en la ficha de escucha?", "Título o descripción, tradición, duración, dos rasgos y propósito", "Esos son los campos de la clase."), ex("¿Por qué conviene escuchar músicas de distintas tradiciones?", "Para comparar y conocer más variedad", "La escucha abundante busca variedad."), ex("¿Hasta cuántos minutos dura una música corta?", "5", "Es el rango de referencia de la clase.")],
    (
        "Completa tres fichas de escucha con estas descripciones inventadas. Música 1: «Canción de cuna cantada por una voz sola, lenta y suave, 2 minutos.» Música 2: «Sinfonía de 12 minutos para orquesta, comienza en p y termina en ff.» Música 3: «Rock de 4 minutos con estribillo que se repite tres veces.» En cada ficha escribe tradición, si es corta o mediana, dos rasgos y un propósito. Después escribe cuántas músicas de las 15 que pide el OA te faltarían si solo hubieras escuchado estas 3.",
        "Música 1: tradición oral, corta, tempo lento y dinámica suave, propósito arrullar. Música 2: tradición escrita, mediana, orquesta y crescendo de p a ff, propósito construir una llegada fuerte. Música 3: popular, corta, estribillo repetido y guitarra eléctrica y batería, propósito dar energía. Faltarían 12 músicas.",
        ["clasifica bien tradición y duración", "da dos rasgos y un propósito por ficha", "calcula bien las músicas que faltan"],
        ["tres fichas escritas"],
        ["llenar con «linda»", "no calcular las músicas que faltan"],
        "Reconoce las fichas y pide señalar en la descripción dónde se ve cada rasgo.",
    ),
    "Anota cuántas músicas has escuchado esta semana y de qué tradición.",
    "Diseña un plan de escucha de 15 músicas repartidas entre tradiciones, con duraciones cortas y medianas.",
)
