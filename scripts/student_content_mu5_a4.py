"""Student material for 5.º básico Música, OA 03 (escucha abundante de músicas de diversos contextos y culturas de América y el mundo).

Todas las músicas de los ejercicios son descripciones originales inventadas; las audiciones reales (por ejemplo, obras de compositores americanos y del mundo, música de tradición oral, jazz, rock, tangos o cumbias) las selecciona y pone el docente.
Todo lo que se afirma de tradiciones y regiones es general; los significados y usos de la música de pueblos originarios los enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_content_mu5_a import L
from student_lessons import arith, ex

OA3 = "MU05 OA 03"

# ---------------------------------------------------------------- OA 03 · clase 1 (tradición escrita)
FIC1 = (
    "Pieza A, «Alba en la pampa» (inventada): partitura de una compositora para un trío de violín, flauta y violonchelo. "
    "Pieza B, «Danza de los herreros» (inventada): partitura para un quinteto de bronces, con dos trompetas, un corno, un trombón y una tuba. "
    "Pieza C, «Calle de noche» (inventada): partitura para una orquesta con instrumentos de las cuatro familias."
)

L(
    OA3, 1,
    f"Lápiz y papel. Las piezas están descritas por escrito (son ejemplos inventados), así que no necesitas audio. Fichas de trabajo: {FIC1} Si un adulto de confianza puede poner música de partitura (de orquesta o de cuarteto, a volumen bajo), úsala; si no, trabaja con las fichas.",
    "Aprenderé a escuchar música de tradición escrita (docta) y a describir quién la creó, para qué grupo se escribió y qué instrumentos usa. Sirve para escuchar con atención música de compositores de América y del mundo.",
    ["Sé nombrar cualidades del sonido.", "Sé que hay instrumentos de cuerda, de viento y de percusión.", "Sé escuchar en silencio y por turnos."],
    [
        "La tradición escrita, también llamada música docta, es la música que una persona compone y escribe en una partitura. Gracias a la partitura, otras personas pueden tocarla de nuevo muchos años después. Quien la crea es un compositor o una compositora. Hay compositores de América, como Carlos Chávez (México) y Carlos Guastavino (Argentina), y de otras partes del mundo, como Erik Satie (Francia).",
        "Las obras se escriben para distintas agrupaciones: un dúo son 2 intérpretes, un trío son 3, un cuarteto son 4 y un quinteto son 5. Una orquesta es una agrupación grande con cuatro familias de instrumentos: cuerdas (violín, violonchelo), maderas (flauta, clarinete), bronces (trompeta, trombón) y percusión (timbal). Cada intérprete da su propia interpretación: dos grupos que tocan la misma partitura suenan parecidos, pero no idénticos.",
        "Para escuchar con atención, hazte tres preguntas. ¿Para qué agrupación fue escrita? ¿Qué instrumentos oigo y de qué familia son? ¿Qué cualidades del sonido destacan: altura, intensidad, timbre o duración? Anota las respuestas en una ficha. Los títulos y las obras reales las elige tu profesor o profesora; aquí practicas con descripciones inventadas.",
    ],
    [("tradición escrita (docta)", "música que se compone y se escribe en una partitura"), ("compositor o compositora", "persona que crea una música"), ("partitura", "papel en que está escrita la música"), ("trío, cuarteto, quinteto", "agrupaciones de 3, 4 y 5 intérpretes"), ("orquesta", "agrupación grande con cuerdas, maderas, bronces y percusión")],
    [
        ("Contar intérpretes", "La pieza A es para un trío y la pieza B para un quinteto. ¿Cuántos intérpretes hay entre las dos?", ["Trío: 3.", "Quinteto: 5.", "3 + 5 = 8."], "8 intérpretes"),
        ("Clasificar instrumentos", "En la pieza A suenan violín, flauta y violonchelo. ¿Cuántos son de la familia de las cuerdas?", ["El violín es de cuerdas.", "El violonchelo es de cuerdas.", "La flauta es de maderas."], "2"),
    ],
    [
        ("Pensar que una partitura hace que dos grupos suenen idénticos.", "Cada intérprete decide detalles de su interpretación.", "La partitura guía; cada interpretación suena parecida, no idéntica."),
        ("Creer que la música docta es solo europea.", "También hay compositores de América y de todo el mundo.", "Escucha obras de varios países."),
    ],
    [
        ex("En la tradición escrita, ¿dónde queda anotada la música?", "En una partitura", "La partitura es el papel que guarda la música escrita."),
        ex("¿Cómo se llama la persona que crea y escribe una música?", "Compositor o compositora", "Es quien compone la obra."),
        ex("¿Cuántos intérpretes tiene un cuarteto?", "4", "Cuarteto significa cuatro."),
    ],
    [
        ex("¿A qué familia de la orquesta pertenece la flauta?", "Maderas", "Las flautas, clarinetes y similares forman la familia de las maderas."),
        ex("Según la clase, ¿de qué país es el compositor Carlos Guastavino?", "Argentina", "La clase lo nombra entre los compositores de América."),
        ex("La pieza B, «Danza de los herreros», es para un quinteto de bronces. ¿Cuántos intérpretes toca?", "5", "Un quinteto tiene cinco intérpretes: dos trompetas, un corno, un trombón y una tuba."),
    ],
    [
        arith("Una orquesta pequeña tiene 12 intérpretes de cuerdas, 4 de maderas, 4 de bronces y 2 de percusión. ¿Cuántos intérpretes son?", "12+4+4+2", "Se suman los intérpretes de las cuatro familias.", " intérpretes"),
        ex("En la pieza B suenan trompetas, un corno, un trombón y una tuba. ¿A qué familia pertenecen todos?", "Bronces", "Estos instrumentos de viento metálico forman la familia de los bronces."),
        arith("Un curso escucha tres obras de 4, 6 y 5 minutos. ¿Cuántos minutos escucha en total?", "4+6+5", "Se suman los minutos de las tres obras.", " minutos"),
    ],
    [
        ex("Marta afirma que si dos grupos tocan la misma partitura suenan exactamente iguales. ¿Es cierto?", "No", "Cada interpretación tiene pequeñas diferencias de tempo, intensidad y timbre."),
        ex("Se escucha una pieza escrita para quinteto de bronces. ¿Cuál de estos instrumentos no debería oírse: trombón, violín o tuba?", "Violín", "El violín es de cuerdas y no está en un quinteto de bronces."),
    ],
    [
        arith("En una orquesta de 22 intérpretes hay 2 de percusión. ¿Cuántos intérpretes no son de percusión?", "22-2", "Se restan los de percusión del total.", " intérpretes"),
        ex("Un cuarteto de cuerdas tiene 2 violines, 1 viola y 1 violonchelo. ¿Cuántos instrumentos no son violines?", "2", "Se cuentan la viola y el violonchelo."),
    ],
    [ex("En una ficha de escucha anotas que la pieza usa trompetas y tubas. ¿Escribes que es una pieza para cuerdas o para bronces?", "Para bronces", "Esos instrumentos son de la familia de los bronces.")],
    [ex("¿Qué significa trío?", "Una agrupación de 3 intérpretes", "Tri significa tres."), ex("¿De qué familia es el violonchelo?", "Cuerdas", "Se toca con arco y cuerdas."), ex("¿Qué es una partitura?", "El papel en que está escrita la música", "Permite tocarla de nuevo.")],
    (
        "Haz una ficha de escucha para una pieza de tradición escrita. Puedes usar la pieza C («Calle de noche») o una música de orquesta o cuarteto que escuches con un adulto de confianza, a volumen bajo. Escribe: título, quién la compuso (si lo sabes), para qué agrupación está escrita, dos instrumentos con su familia y una cualidad del sonido que te llamó la atención.",
        "Título: «Calle de noche» (inventada). Compositor: no se sabe, es un ejemplo. Agrupación: orquesta. Instrumentos: flauta (maderas) y timbal (percusión). Cualidad: los timbales suenan graves y fuertes.",
        ["completa los cinco datos de la ficha", "ubica cada instrumento en su familia", "describe una cualidad del sonido"],
        ["ficha escrita"],
        ["poner un instrumento en la familia equivocada", "no decir la cualidad del sonido"],
        "Reconoce la ficha y pide que justifique la familia de cada instrumento; las obras reales las elige el docente.",
    ),
    "Anota el nombre de dos instrumentos de cuerdas y dos de maderas.",
    "Busca con un adulto una pieza de orquesta y haz su ficha.",
)

# ---------------------------------------------------------------- OA 03 · clase 2 (tradición oral: folclor y pueblos originarios)
CASOS2 = (
    "Caso 1: una canción de cuna que se aprende escuchándola y cantándola, sin partitura, y cada lugar le cambia un poco la letra. "
    "Caso 2: una obra para orquesta con partitura firmada por su compositora. "
    "Caso 3: una danza de fiesta de un pueblo que todos conocen, nadie sabe quién la creó y se enseña bailando junto a personas mayores. "
    "Caso 4: un cuarteto escrito en partitura hace 100 años."
)

L(
    OA3, 2,
    f"Lápiz y papel. Los casos son inventados y están escritos aquí. {CASOS2} Si un adulto de confianza sabe una canción tradicional y quiere enseñártela, puedes aprenderla; es opcional.",
    "Aprenderé a reconocer la música de tradición oral (folclor y música de pueblos originarios) y a describir cómo se transmite. Sirve para valorar y respetar música que se aprende escuchando y viviendo en comunidad.",
    ["Sé que la música docta se escribe en partitura.", "Sé escuchar con respeto.", "Sé nombrar cualidades del sonido."],
    [
        "La tradición oral es la música que se aprende escuchando, cantando y tocando junto a otras personas, sin necesitar partitura. Se transmite de memoria, de persona a persona, de generación en generación. Muchas veces no se conoce quién la creó: pertenece a una comunidad. Como pasa de boca en boca, puede cambiar un poco según el lugar.",
        "El folclor reúne canciones, danzas e instrumentos tradicionales de una región o país. En Chile, la cueca y la tonada son ejemplos de música folclórica. La música de pueblos originarios es parte de la tradición oral de cada pueblo. Por ejemplo, el pueblo mapuche usa instrumentos como el kultrún (un tambor) y la trutruka (un instrumento de viento). En los Andes se tocan la quena y la zampoña, que son instrumentos de viento.",
        "Al escuchar música de pueblos originarios hay que hacerlo con respeto. Su significado, sus usos en ceremonias y su forma tradicional de tocarla los enseñan los educadores y educadoras tradicionales y las comunidades, no se inventan ni se imitan sin permiso. En esta clase nos fijamos en lo que se puede oír: instrumentos, ritmo, si canta una persona o un grupo, y si hay pregunta y respuesta.",
    ],
    [("tradición oral", "música que se transmite de memoria, sin partitura"), ("folclor", "música, danzas e instrumentos tradicionales de una región o país"), ("comunidad", "grupo de personas que comparte una cultura"), ("kultrún y trutruka", "tambor y instrumento de viento del pueblo mapuche"), ("quena y zampoña", "instrumentos de viento de los Andes")],
    [
        ("Clasificar un caso", "Una danza de fiesta se enseña bailando junto a personas mayores, sin partitura, y nadie sabe quién la creó. ¿Es tradición oral o tradición escrita?", ["No usa partitura.", "Se transmite de persona a persona.", "No hay autor conocido."], "Tradición oral"),
        ("Explicar un cambio", "Dos pueblos cantan la misma canción, pero con una letra un poco distinta. ¿Por qué puede pasar esto en la tradición oral?", ["La canción se aprende de memoria.", "Cada lugar puede cambiar algo al transmitirla."], "Porque se transmite de memoria y cada lugar la cambia un poco"),
    ],
    [
        ("Pensar que la música oral no tiene reglas porque no está escrita.", "Tiene reglas que la comunidad enseña y mantiene.", "Se aprende con quienes la practican."),
        ("Imitar la música de un pueblo originario sin conocer su sentido.", "Cada pueblo decide cómo se toca y para qué.", "Escúchala con respeto y pregunta a un educador o educadora tradicional."),
    ],
    [
        ex("En la tradición oral, ¿cómo se aprende la música: leyendo una partitura o escuchando y repitiendo?", "Escuchando y repitiendo", "No necesita partitura."),
        ex("El kultrún es un tambor. ¿A qué tipo de instrumento pertenece: percusión o viento?", "Percusión", "Los tambores se tocan golpeándolos."),
        ex("En una canción folclórica, ¿siempre se conoce quién la creó?", "No", "Muchas veces pertenece a una comunidad y no se sabe quién la creó."),
    ],
    [
        ex(f"{CASOS2} ¿Cuántos de los cuatro casos son de tradición oral?", "2", "Son los casos 1 y 3."),
        ex("La quena y la zampoña son instrumentos de viento. ¿Se tocan soplando o golpeando?", "Soplando", "Los instrumentos de viento suenan con el aire."),
        ex("La cueca, ¿es un ejemplo de música folclórica de Chile? Responde sí o no.", "Sí", "La cueca es parte del folclor chileno."),
    ],
    [
        arith("Una canción tradicional tiene 8 versos y en un pueblo cambiaron 2 de ellos. ¿Cuántos versos quedaron iguales?", "8-2", "Se restan los versos cambiados del total.", " versos"),
        arith("En una rueda de 12 personas, 5 tocan instrumentos de percusión y las demás cantan. ¿Cuántas personas cantan?", "12-5", "Se restan las que tocan del total.", " personas"),
        ex("Un grupo escucha una pieza con un tambor, una trutruka y voces. ¿Cuántos tipos de instrumentos de viento hay?", "1", "Solo la trutruka es de viento."),
    ],
    [
        ex("Pedro dice que la música de tradición oral no sigue reglas porque no está escrita. ¿Es cierto?", "No", "Sigue reglas que la comunidad enseña y mantiene."),
        ex("¿Por qué una canción de tradición oral puede cambiar con el tiempo?", "Porque se transmite de memoria y cada persona puede cambiar algo", "No existe una partitura que fije cada detalle."),
    ],
    [
        arith("Una persona enseña una canción a 3 personas. Cada una de ellas se la enseña después a 3 personas nuevas. ¿Cuántas personas nuevas la aprenden en la segunda vuelta?", "3*3", "Las 3 personas enseñan a 3 cada una.", " personas"),
        arith("Un grupo aprende una canción en 3 sesiones de 20 minutos. ¿Cuántos minutos dedica en total?", "3*20", "Se multiplican las sesiones por los minutos de cada una.", " minutos"),
    ],
    [ex("Un niño escucha una melodía de quena tocada por una persona de su comunidad y la repite de memoria. ¿Qué tradición ilustra: oral o escrita?", "Oral", "Aprende escuchando y repitiendo, sin partitura.")],
    [ex("¿Qué significa tradición oral?", "Música que se transmite de memoria", "Se aprende sin partitura."), ex("¿Quién enseña los usos ceremoniales de la música de un pueblo originario?", "Los educadores o la comunidad", "Ellos conocen su sentido."), ex("¿La trutruka es de percusión o de viento?", "De viento", "Es un instrumento de viento.")],
    (
        "Haz una ficha de escucha de una música de tradición oral. Puedes usar el caso 1 (canción de cuna) o 3 (danza de fiesta), o una canción que otra persona quiera enseñarte (es opcional). Escribe: cómo se transmite, si canta una persona o un grupo, qué instrumentos oyes o imaginas y una cualidad del sonido (fuerte o suave, rápido o lento).",
        "Caso 3 (danza de fiesta): se transmite bailando con personas mayores; canta y baila un grupo; hay tambor; el ritmo es rápido y el sonido fuerte.",
        ["explica cómo se transmite", "indica quién canta o toca", "describe una cualidad del sonido", "trata la música con respeto"],
        ["ficha escrita"],
        ["decir que una canción oral tiene partitura", "inventar significados de música de pueblos originarios"],
        "Reconoce la ficha; si aparece música de un pueblo originario, recuerda que su significado lo enseña el educador o educadora tradicional.",
    ),
    "Nombra dos instrumentos de viento de los Andes.",
    "Pregunta, si quieres, a una persona mayor de tu confianza qué canción tradicional sabe y anota cómo la aprendió.",
)

# ---------------------------------------------------------------- OA 03 · clase 3 (música popular: jazz, rock, fusión)
POP = (
    "Música 1 (inventada): cuarteto con saxofón, contrabajo, batería y piano; en un momento, el saxofonista inventa su melodía mientras los otros mantienen el pulso. "
    "Música 2 (inventada): guitarras eléctricas fuertes, bajo y batería con un ritmo muy marcado, y una voz que canta. "
    "Música 3 (inventada): un cuarteto de jazz que suma una quena y un tambor andino."
)

L(
    OA3, 3,
    f"Lápiz y papel. Las músicas están descritas por escrito: {POP} Si puedes, escucha con un adulto de confianza, a volumen bajo, una pieza de jazz y una de rock.",
    "Aprenderé a reconocer la música popular (jazz, rock y fusión) y a describir sus instrumentos, su pulso y si hay improvisación. Sirve para escuchar música actual con más atención.",
    ["Sé reconocer instrumentos eléctricos, de cuerdas y de percusión.", "Sé identificar el pulso.", "Sé nombrar cualidades del sonido."],
    [
        "La música popular es la que se difunde mucho entre el público, por radio, grabaciones y conciertos, y suele usar instrumentos amplificados. El jazz nació en Estados Unidos, en comunidades afroamericanas, y se caracteriza por la improvisación: una persona inventa su melodía en el momento, sobre un pulso y una estructura que el grupo mantiene. El rock usa guitarras eléctricas, bajo y batería con un ritmo muy marcado.",
        "Una fusión es la mezcla de dos o más estilos, por ejemplo jazz con instrumentos o ritmos de música tradicional. Escuchar música popular es fijarse en el timbre (qué instrumentos suenan), en el pulso y el ritmo (qué tan marcado es), en la dinámica y en si hay improvisación. La improvisación no es tocar cualquier cosa: se improvisa respetando el pulso y el estilo.",
        "Hay música popular de todo el mundo y de América. Escucharla con atención significa describirla, no solo decir si te gusta. Por ejemplo: «Suena una guitarra eléctrica fuerte con un pulso muy marcado, por eso parece rock». Cuida el volumen: la música amplificada puede dañar el oído si es muy fuerte.",
    ],
    [("música popular", "música muy difundida, con instrumentos a menudo amplificados"), ("jazz", "estilo nacido en Estados Unidos, con improvisación"), ("rock", "estilo con guitarras eléctricas, bajo y batería"), ("fusión", "mezcla de estilos"), ("improvisar", "inventar música en el momento, sobre un pulso")],
    [
        ("Clasificar", f"{POP} ¿Qué estilo es la música 2?", ["Tiene guitarras eléctricas fuertes, bajo y batería.", "El ritmo es muy marcado.", "Esas son las características del rock."], "Rock"),
        ("Reconocer una fusión", f"{POP} ¿Por qué la música 3 es una fusión?", ["Tiene un cuarteto de jazz.", "Suma una quena y un tambor andino.", "Mezcla dos estilos."], "Porque mezcla jazz con instrumentos andinos"),
    ],
    [
        ("Creer que improvisar es tocar cualquier cosa.", "Se improvisa sobre un pulso y una estructura.", "Mantén el pulso y el estilo mientras inventas."),
        ("Pensar que fuerte es lo mismo que bueno.", "El volumen alto puede dañar el oído y no hace mejor la música.", "Cuida el volumen y cuida tu oído."),
    ],
    [
        ex("¿En qué país nació el jazz?", "Estados Unidos", "Nació en comunidades afroamericanas de ese país."),
        ex("¿Qué instrumentos forman la base de una banda de rock: guitarra eléctrica, bajo y batería o quena, zampoña y tambor?", "Guitarra eléctrica, bajo y batería", "Esa es la formación típica del rock."),
        ex("En una improvisación de jazz, ¿la persona solista inventa la melodía en el momento?", "Sí", "Improvisar es inventar la música sobre la marcha."),
    ],
    [
        ex(f"{POP} ¿Qué estilo es la música 1?", "Jazz", "Hay saxofón, contrabajo, batería, piano y un solista que improvisa."),
        ex("Un grupo mezcla una cueca con rock. ¿Cómo se llama esta mezcla de estilos?", "Fusión", "Una fusión mezcla dos o más estilos."),
        ex("¿La música popular se difunde por radio y grabaciones o se escucha solo en una sala de conciertos?", "Por radio y grabaciones, entre otros medios", "Llega a mucha gente por distintos medios."),
    ],
    [
        arith("Un concierto tiene 5 canciones de 4 minutos y 2 canciones de 6 minutos. ¿Cuántos minutos dura la música?", "5*4+2*6", "Se suman los minutos de los dos tipos de canción.", " minutos"),
        arith("Una canción de rock tiene 60 pulsos y va a 2 pulsos por segundo. ¿Cuántos segundos dura?", "60//2", "Se reparten los pulsos entre los que pasan en cada segundo.", " segundos"),
        ex("Una banda tiene una persona en la guitarra eléctrica, una en el bajo, una en la batería y una que canta, y cada una hace solo eso. ¿Cuántas personas tiene?", "4", "Cada persona cumple una función distinta."),
    ],
    [
        ex("Marta cree que improvisar es tocar cualquier cosa sin ninguna regla. ¿Es cierto?", "No", "Se improvisa sobre un pulso y una estructura, con estilo."),
        ex("Una banda une cumbia y jazz. ¿Qué nombre recibe: fusión o repetición?", "Fusión", "Mezcla dos estilos distintos."),
    ],
    [
        arith("Una banda toca 3 piezas de jazz de 7 minutos y 2 de rock de 4 minutos. ¿Cuántos minutos más dura el jazz que el rock?", "3*7-2*4", "El jazz dura 21 minutos y el rock 8; se restan.", " minutos más"),
        ex("Si en un cuarteto de jazz cada integrante improvisa una vez, ¿cuántas improvisaciones hay?", "4", "Un cuarteto tiene cuatro integrantes y cada uno improvisa una vez."),
    ],
    [ex("Quieres describir una música con guitarra eléctrica fuerte y ritmo muy marcado. ¿Dices «me gustó» o «suena una guitarra eléctrica fuerte con pulso marcado»?", "La segunda", "La segunda describe lo que se oye.")],
    [ex("¿Qué es una fusión?", "Una mezcla de estilos", "Une elementos de varios estilos."), ex("¿Qué caracteriza al jazz?", "La improvisación", "Una persona inventa su melodía en el momento."), ex("¿Qué debes cuidar al escuchar música amplificada?", "El volumen", "Un volumen muy alto daña el oído.")],
    (
        "Haz una ficha de escucha de una música popular. Puedes usar la música 1, 2 o 3 o una pieza de jazz o rock escuchada con un adulto de confianza, a volumen bajo. Escribe el estilo, los instrumentos que oyes, si el pulso es muy marcado y si hay improvisación. Termina con una frase que empiece con «Por eso parece…».",
        "Música 2: rock. Guitarras eléctricas, bajo, batería y voz. Pulso muy marcado. Sin improvisación. Por eso parece rock: tiene guitarras eléctricas fuertes y un ritmo muy marcado.",
        ["escribe estilo e instrumentos", "describe pulso e improvisación", "justifica con lo que se oye"],
        ["ficha escrita"],
        ["decir solo «me gustó»", "confundir el volumen alto con el estilo"],
        "Reconoce la ficha y pide justificar el estilo con un rasgo audible; recuerda cuidar el volumen.",
    ),
    "Di dos instrumentos que suenan en el rock.",
    "Busca con un adulto una pieza de jazz y cuenta cuántos solistas improvisan.",
)

# ---------------------------------------------------------------- OA 03 · clase 4 (música de América y sus orígenes)
GEN = "huayno, joropo, tango y cumbia"

L(
    OA3, 4,
    f"Lápiz y papel. Los datos están en la clase. Géneros de la clase: {GEN}. Si un adulto de confianza puede poner un ejemplo, escúchalo a volumen bajo.",
    "Aprenderé a ubicar en América de dónde vienen géneros como el huayno, el joropo, el tango y la cumbia, y a reconocer que muchos mezclan músicas de distintos orígenes, entre ellos el africano. Sirve para conocer la riqueza musical de América.",
    ["Sé que la música tiene instrumentos típicos.", "Sé que la música tradicional se transmite de memoria.", "Sé ubicar países en un mapa de América."],
    [
        "La música de América nació de la mezcla de muchas tradiciones: las de los pueblos originarios, las que llegaron desde África y las que llegaron desde Europa. Por eso hay géneros muy distintos. De la música de origen africano vienen sobre todo los tambores, los ritmos que se superponen y el canto en que una voz llama y otras responden.",
        "El huayno es música andina que se canta y se baila, con instrumentos como la quena y la zampoña. Se escucha en países andinos como Perú y Bolivia, y también en el norte de Chile. El joropo es música y baile de Venezuela y Colombia; suena con arpa, cuatro (una guitarra pequeña de cuatro cuerdas) y maracas. El tango nació en la zona del Río de la Plata, entre Argentina y Uruguay, y usa el bandoneón (un instrumento parecido a un acordeón). La cumbia nació en Colombia y hoy se escucha y baila en muchos países de América, incluido Chile.",
        "Para describir estas músicas conviene fijarse en el origen, los instrumentos y el pulso y ritmo. La música no tiene fronteras: un género nace en un lugar y se transforma en otros. Al escuchar, hazlo con respeto y curiosidad, sin burlarte de los géneros que no conoces.",
    ],
    [("huayno", "música andina que se canta y se baila"), ("joropo", "música y baile de Venezuela y Colombia"), ("tango", "música del Río de la Plata, con bandoneón"), ("cumbia", "música nacida en Colombia, hoy popular en muchos países"), ("origen africano", "tambores, ritmos que se superponen y canto de llamada y respuesta")],
    [
        ("Ubicar un género", "El tango nació en la zona del Río de la Plata. ¿Entre qué dos países está esa zona?", ["Río de la Plata es la zona entre Argentina y Uruguay.", "Ahí nació el tango."], "Argentina y Uruguay"),
        ("Ubicar un género", "El joropo suena con arpa, cuatro y maracas. ¿En qué países se canta y baila principalmente?", ["Busco en la explicación de la clase dónde se canta y baila el joropo.", "La explicación dice que es música y baile de Venezuela y Colombia."], "Venezuela y Colombia"),
    ],
    [
        ("Pensar que cada género pertenece a un solo país.", "Los géneros nacen en un lugar y se difunden por otros.", "Fíjate en dónde nacieron y dónde se escuchan hoy."),
        ("Creer que la música de América viene de un solo origen.", "Mezcla tradiciones indígenas, africanas y europeas.", "Busca los distintos orígenes de cada género."),
    ],
    [
        ex("¿Qué género usa el bandoneón?", "Tango", "El bandoneón es característico del tango."),
        ex("¿Dónde nació la cumbia?", "En Colombia", "Desde allí se difundió a otros países."),
        ex("El joropo suena con arpa, cuatro y maracas. ¿El cuatro es una guitarra pequeña de cuatro cuerdas o un tambor?", "Una guitarra pequeña de cuatro cuerdas", "Así lo define la clase."),
    ],
    [
        ex("¿Qué instrumentos andinos de viento se usan en el huayno?", "La quena y la zampoña", "Son los que menciona la clase."),
        ex("De la música de origen africano vienen sobre todo los tambores, los ritmos superpuestos y un tipo de canto. ¿Cuál?", "El canto de llamada y respuesta", "Una voz llama y otras responden."),
        ex("Según la clase, ¿la cumbia se escucha hoy solo en Colombia o en muchos países de América?", "En muchos países", "Nació en Colombia y se difundió por América."),
    ],
    [
        arith("Un curso quiere escuchar 3 músicas de cada uno de los 4 géneros de la clase. ¿Cuántas músicas escuchará en total?", "3*4", "Se multiplican las músicas por género por el número de géneros.", " músicas"),
        ex("Una música suena con arpa, cuatro y maracas. ¿Qué género es: huayno, joropo o tango?", "Joropo", "Esos son sus instrumentos típicos."),
        ex("Una música andina con quena y zampoña, que se canta y se baila, se escucha en Perú y Bolivia. ¿Qué género es?", "Huayno", "Es música andina de esos países."),
    ],
    [
        ex("Marta cree que el tango y la cumbia nacieron en el mismo lugar. ¿Dónde nació cada uno?", "El tango en el Río de la Plata y la cumbia en Colombia", "Son zonas distintas de América."),
        ex("¿Por qué decimos que la música de América es una mezcla?", "Porque reúne tradiciones indígenas, africanas y europeas", "Esas tradiciones se encontraron en América."),
    ],
    [
        arith("Un curso ha escuchado 2 músicas de cada uno de los 4 géneros de la clase y 3 de otros estilos. ¿Cuántas músicas ha escuchado?", "2*4+3", "Se multiplican por género y se suman las otras.", " músicas"),
        arith("Para llegar a 15 músicas, un grupo ya escuchó 9. ¿Cuántas le faltan?", "15-9", "Se resta lo escuchado de la meta.", " músicas"),
    ],
    [ex("Un compañero dice que la cumbia es solo de Chile. ¿Qué le corriges?", "Nació en Colombia y hoy se escucha en muchos países", "Su origen está en Colombia.")],
    [ex("¿Qué género nació en el Río de la Plata?", "Tango", "Allí se originó."), ex("¿La quena, que se usa en el huayno, es un instrumento de viento o de percusión?", "De viento", "Se toca soplando."), ex("¿Qué países comparten el joropo?", "Venezuela y Colombia", "Es música de ambos.")],
    (
        "Elige uno de los cuatro géneros de la clase y haz una ficha: nombre, de dónde viene, dos instrumentos típicos (si los conoces por la clase) y una cualidad que oirías, como pulso marcado o melodía suave. Si puedes, escúchalo con un adulto de confianza, a volumen bajo, y verifica si coinciden.",
        "Tango: viene del Río de la Plata (Argentina y Uruguay). Instrumento: bandoneón. Cualidad: pulso marcado y melodía con mucha expresión.",
        ["dice de dónde viene", "nombra instrumentos de la clase", "describe una cualidad audible"],
        ["ficha escrita"],
        ["decir que un género es de un solo país", "inventar instrumentos o datos que no sabe"],
        "Reconoce la ficha; si el estudiante no está seguro de un dato, que lo pregunte al docente en lugar de inventarlo.",
    ),
    "Escribe el nombre de un género de la clase y el país donde nació.",
    "Pregunta a una persona mayor de tu confianza qué música baila y anota si es de uno de estos géneros.",
)

# ---------------------------------------------------------------- OA 03 · clase 5 (escucha abundante y registro)
LOG = [
    (1, "Aurora de cuerdas", "escrita", 3), (2, "Marcha de la plaza", "escrita", 5), (3, "Coral de invierno", "escrita", 4),
    (4, "Canto de cosecha", "oral", 2), (5, "Ronda del pueblo", "oral", 3), (6, "Danza de la fiesta", "oral", 6), (7, "Canto con tambor", "oral", 4),
    (8, "Noche de saxo", "popular", 7), (9, "Guitarras al sol", "popular", 3), (10, "Baile eléctrico", "popular", 4), (11, "Puente andino", "popular", 5),
]
LOG_TXT = " ".join(f"{n}) «{t}», tradición {tr}, {m} minutos." for n, t, tr, m in LOG)
CUENTA = {tr: sum(1 for x in LOG if x[2] == tr) for tr in ("escrita", "oral", "popular")}
TOTAL_MIN = sum(m for *_x, m in LOG)
CORTAS = sum(1 for x in LOG if x[3] <= 3)
MEDIANAS = len(LOG) - CORTAS

L(
    OA3, 5,
    f"Lápiz y papel. Registro de escucha (títulos inventados): {LOG_TXT} Convención de la clase: una música corta dura hasta 3 minutos y una mediana, más de 3 y hasta 8 minutos.",
    "Aprenderé a llevar un registro de escucha de varias músicas, a contarlas por tradición y a ver cuántas faltan para llegar a 15. Sirve para escuchar mucha música variada de forma organizada.",
    ["Sé distinguir tradición escrita, tradición oral y música popular.", "Sé sumar y restar.", "Sé escuchar con respeto."],
    [
        "Escuchar música en forma abundante significa escuchar muchas músicas distintas, de diversos contextos y culturas. La meta del curso es escuchar al menos 15 músicas variadas, cortas y medianas. Para no perder la cuenta se lleva un registro: una lista con el título, la tradición (escrita, oral o popular) y la duración de cada música.",
        f"Con el registro puedes contar cuántas músicas hay de cada tradición y cuántos minutos escuchaste. En el registro de la clase hay {len(LOG)} músicas: {CUENTA['escrita']} de tradición escrita, {CUENTA['oral']} de oral y {CUENTA['popular']} populares, y suman {TOTAL_MIN} minutos. Para llegar a 15 faltan {15 - len(LOG)} músicas. También ayuda a revisar si todas las tradiciones están representadas.",
        "Escuchar bien no es solo oír: después de cada música anota una frase que describa lo que oíste, con una cualidad del sonido, por ejemplo «los tambores suenan graves y fuertes». Si algo te gustó, di por qué con lo que se oyó. Y si algo no te gustó, respeta que a otras personas sí les guste.",
    ],
    [("registro de escucha", "lista de las músicas escuchadas, con título, tradición y duración"), ("meta", "cantidad que quiero alcanzar"), ("música corta", "dura hasta 3 minutos"), ("música mediana", "dura más de 3 y hasta 8 minutos"), ("variada", "de tradiciones y estilos distintos")],
    [
        ("Contar por tradición", f"{LOG_TXT} ¿Cuántas músicas son de tradición oral?", ["Las orales son la 4, 5, 6 y 7.", "Son 4."], f"{CUENTA['oral']}"),
        ("Calcular lo que falta", f"Con {len(LOG)} músicas registradas y una meta de 15, ¿cuántas faltan?", ["Meta: 15.", f"Ya hay {len(LOG)}.", f"15 − {len(LOG)} = {15 - len(LOG)}."], f"{15 - len(LOG)} músicas"),
    ],
    [
        ("Anotar solo si me gustó.", "Un registro necesita datos que se puedan comprobar.", "Anota título, tradición, duración y una cualidad del sonido."),
        ("Escuchar solo un tipo de música.", "La meta pide música variada.", "Cuenta cuántas hay de cada tradición y completa las que faltan."),
    ],
    [
        ex(f"{LOG_TXT} ¿De qué tradición es «Marcha de la plaza»?", "Escrita", "El registro lo indica."),
        ex(f"{LOG_TXT} ¿Cuántos minutos dura «Noche de saxo»?", "7", "El registro anota 7 minutos."),
        ex("La meta del curso es escuchar al menos 15 músicas. Si ya tienes 11, ¿cumpliste la meta?", "No", "Todavía te faltan músicas."),
    ],
    [
        ex(f"{LOG_TXT} ¿Cuántas músicas hay de tradición escrita?", str(CUENTA["escrita"]), "Son la 1, la 2 y la 3."),
        ex(f"{LOG_TXT} ¿Cuántas músicas populares hay?", str(CUENTA["popular"]), "Son la 8, 9, 10 y 11."),
        ex(f"{LOG_TXT} ¿Cuántas músicas son cortas (hasta 3 minutos)?", str(CORTAS), "Son la 1 (3 min), la 4 (2 min), la 5 (3 min) y la 9 (3 min)."),
    ],
    [
        arith(f"{LOG_TXT} ¿Cuántos minutos suman las cuatro músicas de tradición oral?", "2+3+6+4", "Se suman las duraciones de la 4, 5, 6 y 7.", " minutos"),
        arith(f"{LOG_TXT} ¿Cuántos minutos suman todas las músicas del registro?", "+".join(str(m) for *_x, m in LOG), "Se suman las 11 duraciones.", " minutos"),
        ex(f"{LOG_TXT} ¿Cuántas músicas son medianas (más de 3 y hasta 8 minutos)?", str(MEDIANAS), "Son las que duran más de 3 minutos."),
    ],
    [
        ex("Rosa tiene 3 músicas escritas, 4 orales y 4 populares. Quiere una música más de cada tradición. ¿Cuántas músicas tendrá en total?", "14", "11 músicas más 3 nuevas suman 14."),
        ex("Rosa propone completar la meta de 15 escuchando solo música popular. ¿Qué problema tiene?", "La meta pide música variada, de tradiciones distintas", "Debe incluir también la escrita y la oral."),
    ],
    [
        arith("Un curso escucha 2 músicas por clase. ¿Cuántas clases necesita para llegar a 15, redondeando hacia arriba?", "(15+1)//2", "Con 2 por clase, 8 clases dan 16, que supera 15.", " clases"),
        arith(f"{LOG_TXT} Si se agregan 4 músicas de 5 minutos cada una, ¿cuántos minutos suma el registro?", f"{TOTAL_MIN}+4*5", "Se suma lo que ya había y lo nuevo.", " minutos"),
    ],
    [ex("Un curso quiere repartir 15 músicas en 3 tradiciones por igual. ¿Cuántas debe escuchar de cada una?", "5", "15 dividido en 3 es 5.")],
    [ex("¿Qué datos lleva un registro de escucha?", "Título, tradición, duración y una cualidad del sonido", "Así se puede revisar lo escuchado."), ex("¿Qué dura una música corta?", "Hasta 3 minutos", "Es la convención de la clase."), ex("¿Cuántas músicas se espera escuchar como mínimo?", "15", "Es la meta del curso.")],
    (
        "Crea tu propio registro de escucha de 6 músicas. Pueden ser las del registro de la clase o músicas que escuches con un adulto de confianza, a volumen bajo. Para cada una anota título, tradición, minutos y una frase con una cualidad del sonido. Al final cuenta cuántas son de cada tradición y cuántas te faltan para llegar a 15.",
        "1) «Marcha de la plaza», escrita, 5 min, trompetas fuertes. 2) «Canto de cosecha», oral, 2 min, voces al unísono. 3) «Noche de saxo», popular, 7 min, saxofón con improvisación. 4) «Aurora de cuerdas», escrita, 3 min, violines suaves. 5) «Danza de la fiesta», oral, 6 min, tambor rápido. 6) «Guitarras al sol», popular, 3 min, pulso muy marcado. Son 2 de cada tradición y faltan 15 − 6 = 9 músicas para llegar a 15.",
        ["registra seis músicas con los cuatro datos", "incluye las tres tradiciones", "calcula bien las que faltan"],
        ["registro escrito", "conteo"],
        ["anotar solo títulos", "olvidar una tradición"],
        "Reconoce el registro y pide revisar que aparezcan las tres tradiciones y que el conteo coincida con la lista.",
    ),
    "Anota el título de dos músicas que hayas escuchado esta semana y su duración aproximada.",
    "Agrega a tu registro 3 músicas más y actualiza cuántas faltan para 15.",
)
