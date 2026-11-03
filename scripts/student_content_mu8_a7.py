"""Student material for 8.º básico Música, OA 07 (apreciar el rol de la música en la sociedad a partir del repertorio trabajado, respetando la diversidad y riqueza de los contextos socioculturales).

Todas las comunidades, encuestas y casos de los ejercicios son inventados («de ejemplo») para esta clase; el repertorio real y las músicas de comunidades concretas los selecciona el docente.
Sobre los pueblos originarios solo se dice lo general: sus músicas pertenecen a sus comunidades y su forma tradicional la enseñan quienes las cultivan.
"""
from __future__ import annotations

from student_content_mu8_a import L
from student_lessons import arith, ex

OA7 = "MU08 OA 07"

# ---------------------------------------------------------------- OA 07 · clase 1 (funciones de la música)
L(
    OA7, 1,
    "Lápiz y papel. Las situaciones están descritas en los ejercicios (son de ejemplo). Si quieres, piensa en las músicas que se usan en tu casa, en tu barrio o en tu colegio.",
    "Aprenderé a reconocer las funciones que cumple la música en la sociedad (acompañar el trabajo, bailar y celebrar, conmemorar, arrullar, comunicar ideas, dar identidad y enseñar) y a relacionarlas con rasgos audibles. Sirve para comprender por qué las personas hacen y usan música.",
    ["Sé relacionar un propósito con rasgos audibles.", "Sé que la música puede ser de tradición oral, escrita o popular.", "Sé sumar y restar números pequeños."],
    [
        "La música cumple funciones en la vida de las personas. Se usa para acompañar un trabajo en grupo, con un pulso parejo que ordena los movimientos. Se usa para bailar y celebrar, con un pulso claro y un tempo movido. Se usa para conmemorar o recordar, en homenajes y actos. Se usa para arrullar, con melodías lentas y suaves. Se usa para comunicar ideas, para dar identidad a un grupo, como un himno escolar, y para enseñar, como las canciones que ayudan a recordar datos.",
        "Una misma música puede cumplir varias funciones a la vez: una canción de una fiesta sirve para bailar y para celebrar. Para identificar la función se mira quién la usa, cuándo y para qué, y qué rasgos audibles la acompañan. Una música sin letra también comunica, porque sus rasgos, como el tempo, el volumen y el timbre, transmiten sensaciones e ideas.",
        "Apreciar el rol de la música en la sociedad es comprender que cada música cumple un papel en su comunidad, y valorarlo sin compararlo con el de otras. Una música para arrullar no es «menos importante» que una para un gran concierto: cumple otra función. Al describir una función conviene dar el uso, el momento y un rasgo audible que lo sostenga, como en: «sirve para bailar, porque el pulso es claro y movido».",
    ],
    [("función de la música", "papel que cumple la música en la vida de las personas"), ("conmemorar", "recordar un hecho o a una persona en un acto"), ("identidad", "sentimiento de pertenecer a un grupo"), ("arrullar", "calmar o hacer dormir con una música suave"), ("comunidad", "grupo de personas que comparten un lugar, una historia o una tradición")],
    [
        ("Reconocer la función", "Una música con pulso parejo acompaña a un grupo mientras trabaja. ¿Qué función cumple?", ["Se usa durante un trabajo.", "El pulso parejo ordena los movimientos."], "Acompañar el trabajo"),
        ("Contar tiempos", "Un acto escolar dura 90 minutos: 30 de homenaje con música y 20 de baile. ¿Cuántos minutos quedan para otras partes del acto?", ["Se restan los minutos usados.", "90 − 30 − 20 = 40."], "40 minutos"),
    ],
    [
        ("Pensar que una música solo puede cumplir una función.", "Una misma música puede servir para varias cosas a la vez.", "Pregunta quién la usa, cuándo y para qué."),
        ("Creer que una música es más importante porque se toca ante más personas.", "Cada música cumple una función propia en su comunidad.", "Describe la función sin comparar su importancia."),
    ],
    [
        ex("Una canción lenta y suave se canta para hacer dormir a un bebé. ¿Qué función cumple?", "Arrullar", "Calma con rasgos lentos y suaves."),
        ex("Un himno de un colegio que todos cantan al comenzar un acto, ¿qué función cumple?", "Dar identidad", "Une a las personas del colegio."),
        ex("Una canción con una melodía simple sirve para recordar los meses del año. ¿Qué función cumple?", "Enseñar", "Ayuda a recordar datos."),
    ],
    [
        ex("¿Qué rasgo ayuda a que una música sirva para bailar? A) Un pulso claro y constante. B) Un silencio muy largo.", "A", "El pulso claro permite moverse al compás."),
        ex("Una canción se usa en una fiesta para bailar y para celebrar un cumpleaños. ¿Cumple una función o dos?", "Dos", "Cumple las funciones de bailar y de celebrar."),
        ex("¿Una música sin letra puede comunicar ideas o sensaciones? Responde sí o no.", "Sí", "Lo hace con sus rasgos, como el tempo, el volumen y el timbre."),
    ],
    [
        arith("De 12 canciones de un repertorio de ejemplo, 5 son para bailar. ¿Cuántas no son para bailar?", "12-5", "Se resta lo que son para bailar del total.", " canciones"),
        arith("Una fiesta de ejemplo tiene 3 bloques de 25 minutos de música para bailar y 2 pausas de 10 minutos. ¿Cuántos minutos dura en total?", "3*25+2*10", "Se suman los bloques de baile y las pausas.", " minutos"),
        ex("Dos músicas: la primera es lenta, suave y se repite; la segunda es rápida, fuerte y tiene aplausos. ¿Cuál sirve para celebrar en una plaza?", "La segunda", "Rápida, fuerte y con aplausos invita a celebrar."),
    ],
    [
        ex("Un compañero dice: «Una música para arrullar es menos importante que una para un gran concierto». ¿Es correcto? Responde sí o no.", "No", "Cada música cumple una función propia."),
        ex("Un coro canta en el homenaje al fundador de un colegio con una melodía lenta y suave. ¿Qué función cumple y qué rasgo la sostiene?", "Conmemorar; el tempo lento y suave", "Recuerda a una persona y lo lento y suave acompaña el recuerdo."),
    ],
    [
        arith("En un curso de 24 estudiantes, 12 cantan en un homenaje. ¿Qué porcentaje del curso canta?", "12*100//24", "Se divide lo que cantan por el total y se multiplica por 100.", " %"),
        ex("Una canción de un acto escolar se usa para dar identidad al colegio, para recordar a un exalumno y para celebrar el aniversario. ¿Cuántas funciones tiene?", "3", "Son identidad, conmemorar y celebrar."),
    ],
    [ex("En una radio comunitaria de ejemplo, un programa dura 60 minutos y 45 minutos son música para bailar. ¿Cuántos minutos tiene el resto del programa?", "15 minutos", "Se restan los 45 minutos de baile de los 60 del programa.")],
    [ex("¿Qué función cumple una canción de cuna?", "Arrullar", "Calma a quien la escucha."), ex("¿Qué función cumple un himno escolar?", "Dar identidad", "Une a las personas del colegio."), ex("¿Se puede comparar cuál función es más importante? Responde sí o no.", "No", "Cada música cumple su propio papel.")],
    (
        "Lee estos tres casos de ejemplo. 1) Un grupo de vecinas canta con pulso parejo mientras prepara alimentos para una actividad comunitaria. 2) El coro de un colegio canta una melodía lenta y suave en un homenaje a un profesor. 3) Un conjunto toca una pieza rápida y con pulso claro en la fiesta de aniversario de un barrio. Para cada caso escribe: la función (o las funciones), un rasgo audible que la sostiene y quién usa la música.",
        "1) Acompañar el trabajo; pulso parejo; las vecinas. 2) Conmemorar; tempo lento y suave; el coro del colegio y el público del homenaje. 3) Bailar y celebrar; tempo rápido y pulso claro; el barrio.",
        ["nombra una o más funciones", "da un rasgo audible por caso", "no compara la importancia de las músicas"],
        ["tres casos con función y rasgo"],
        ["decir que una función vale más que otra", "no dar un rasgo audible"],
        "Reconoce los casos y pide explicar en uno de ellos por qué el rasgo audible sirve a esa función.",
    ),
    "Escribe una música que se use en tu casa o en tu barrio y la función que cumple.",
    "Describe una música que cumpla dos funciones a la vez y un rasgo audible para cada una.",
)

# ---------------------------------------------------------------- OA 07 · clase 2 (contextos y repertorio)
L(
    OA7, 2,
    "Lápiz y papel. Las comunidades y situaciones son inventadas («de ejemplo») y están descritas en los ejercicios. Si quieres, piensa en cómo cambia una canción según el lugar donde se canta.",
    "Aprenderé a explicar cómo el contexto (lugar, época, comunidad y medios de transmisión) influye en la música que se hace y en cómo suena. Sirve para comprender por qué existen músicas tan distintas y para valorarlas.",
    ["Sé reconocer funciones de la música.", "Sé diferenciar tradición oral, escrita y popular.", "Sé multiplicar números pequeños."],
    [
        "El contexto es el conjunto de circunstancias en que se hace la música: el lugar, la época, la comunidad y los medios con que se transmite. El contexto ayuda a explicar los rasgos de una música. En una comunidad rural, una fiesta puede tener música cantada de oído y tocada con los instrumentos que hay a mano. En un teatro de ciudad, una orquesta puede tocar una pieza escrita en partitura. Ninguna es mejor: responden a contextos distintos.",
        "Los medios de transmisión también cambian la música. De boca en boca, una canción se modifica un poco cada vez. En una partitura, se conserva casi igual. En grabaciones y plataformas, llega a mucha gente en poco tiempo y se escucha repetida. A veces las personas toman una música de un lugar y la transforman, y así nacen mezclas nuevas. Por eso el repertorio de una sociedad cambia con el tiempo.",
        "Para explicar el contexto de una música, se responde: ¿dónde y cuándo se hace?, ¿quién la hace?, ¿con qué instrumentos?, ¿cómo se transmite?, ¿para qué sirve? Después se relaciona con un rasgo audible: «se toca con instrumentos de percusión simples porque es una fiesta al aire libre». Siempre se debe respetar la información que da la propia comunidad sobre su música.",
    ],
    [("contexto", "circunstancias en que se hace la música: lugar, época, comunidad y medios"), ("medio de transmisión", "manera en que una música pasa de unas personas a otras"), ("repertorio", "conjunto de músicas que un grupo sabe tocar o cantar"), ("transformar", "cambiar una música al tomarla desde otro lugar o época"), ("comunidad", "grupo de personas que comparten un lugar, una historia o una tradición")],
    [
        ("Relacionar contexto y rasgos", "En la comunidad ficticia de Valle Claro, una fiesta al aire libre se acompaña con tambores simples y palmas, y la música se aprende de oído. ¿Cómo se transmite esa música?", ["Los datos dicen que se aprende de oído.", "No se escribe en partitura."], "De oído, de forma oral"),
        ("Calcular una transmisión oral", "Una persona le enseña una canción a 3 personas, y cada una de ellas se la enseña a otras 3 personas. ¿Cuántas personas la aprenden en esta segunda ronda?", ["Cada una de las 3 enseña a 3.", "3 × 3 = 9."], "9 personas"),
    ],
    [
        ("Pensar que la música de una ciudad es mejor que la de un pueblo.", "Cada una responde a su contexto, no se compara su valor.", "Explica el contexto en lugar de comparar."),
        ("Creer que una música se mantiene igual cuando pasa de boca en boca.", "En la tradición oral cada versión cambia un poco.", "Comprueba cómo se transmite."),
    ],
    [
        ex("¿Qué es el contexto de una música?", "Las circunstancias en que se hace: lugar, época, comunidad y medios", "Ayuda a explicar los rasgos de la música."),
        ex("Una orquesta toca una pieza leyendo partitura en un teatro. ¿Cómo se transmitió esa música: por escrito o de oído?", "Por escrito", "La partitura es un medio escrito."),
        ex("Una comunidad canta una melodía que aprende de oído en una fiesta. ¿Cambia un poco cada vez o se mantiene idéntica?", "Cambia un poco cada vez", "Así ocurre en la tradición oral."),
    ],
    [
        ex("¿El contexto puede explicar por qué una música usa ciertos instrumentos? Responde sí o no.", "Sí", "Los instrumentos dependen de la tradición y de lo que hay disponible."),
        ex("Una canción llega a mucha gente en poco tiempo gracias a grabaciones y plataformas. ¿Qué medio de transmisión es este: masivo o de boca en boca?", "Masivo", "Las grabaciones y plataformas llegan a muchas personas."),
        ex("Dos músicas suenan distinto: una de una fiesta de pueblo y otra de un teatro. ¿Cuál es mejor? A) Ninguna: responden a contextos distintos. B) La del teatro.", "A", "No se compara el valor de las músicas; se explica su contexto."),
    ],
    [
        arith("En tres comunidades de ejemplo se usan 3, 5 y 4 instrumentos distintos. ¿Cuántos instrumentos se usan en total?", "3+5+4", "Se suman los instrumentos de cada comunidad.", " instrumentos"),
        arith("Una radio de ejemplo emite 24 canciones diarias, repartidas por igual entre 4 tipos de música. ¿Cuántas canciones hay de cada tipo?", "24//4", "Se reparte el total entre los 4 tipos.", " canciones"),
        ex("En la tradición oral, una persona enseña una canción a 3 personas y cada una la enseña a otras 3. ¿Cuántas personas la saben en total en la tercera ronda, si en la ronda 1 la aprenden 3, en la ronda 2 la aprenden 9 y en la ronda 3 la aprenden 27 (sin contar a quien la creó)?", "39", "3 + 9 + 27 = 39 personas."),
    ],
    [
        ex("Una melodía se canta en una fiesta a tempo rápido y en la escuela a tempo lento para aprenderla. ¿Qué explica el cambio de tempo: el propósito de cada contexto o la cantidad de personas que la escuchan?", "El propósito de cada contexto", "En la fiesta se baila y en la escuela se aprende."),
        ex("Un joven dice que una música tradicional de otra comunidad «ya no sirve porque hay música nueva». ¿Qué le falta considerar: que cumple su función en su comunidad o que se escribe en partitura?", "Que cumple su función en su comunidad", "Cada música tiene un papel en su contexto."),
    ],
    [
        arith("Una canción de ejemplo se toca a 60 pulsos por minuto en la escuela y a 120 en una fiesta. ¿Cuántos pulsos más suenan en 3 minutos en la fiesta que en la escuela?", "120*3-60*3", "Se calculan los pulsos de cada contexto y se restan.", " pulsos"),
        arith("Un repertorio de ejemplo tiene 18 canciones: 6 de tradición oral, 7 escritas y el resto populares. ¿Cuántas son populares?", "18-6-7", "Se restan las orales y las escritas del total.", " canciones"),
    ],
    [ex("Tu curso quiere conocer la música de una fiesta de otra comunidad. ¿Qué es lo primero que conviene hacer? A) Preguntar y escuchar cómo la hace y para qué la usa. B) Cambiarla para que sea más moderna.", "A", "Se respeta la información de la propia comunidad.")],
    [ex("¿Qué cuatro cosas forman el contexto?", "Lugar, época, comunidad y medios", "Así se definió en la clase."), ex("¿Cómo cambia la música cuando pasa de boca en boca?", "Cambia un poco cada vez", "Es propio de la tradición oral."), ex("¿Se puede decir que una música es mejor que otra por su contexto? Responde sí o no.", "No", "Cada música responde a su contexto.")],
    (
        "Usa estas dos músicas de ejemplo. A) En la comunidad ficticia de Valle Claro, una melodía se canta en las fiestas, se aprende de oído de los mayores y se acompaña con palmas y un tambor. B) En una ciudad ficticia, una orquesta toca una pieza escrita en partitura en un teatro. Escribe para cada una: el lugar, cómo se transmite, un rasgo audible que se explica por el contexto, y una frase de respeto que diría al hablar de ellas.",
        "A) Lugar: fiestas de la comunidad; transmisión oral; rasgo: tambor y palmas con pulso claro porque acompañan la fiesta; frase: «Me parece valioso cómo los mayores transmiten esa melodía». B) Lugar: teatro; transmisión escrita; rasgo: instrumentos de orquesta que leen la misma partitura; frase: «Es interesante cómo se conserva igual en la partitura».",
        ["relaciona el contexto con un rasgo audible", "distingue transmisión oral y escrita", "usa una frase de respeto sin comparar"],
        ["dos descripciones", "dos frases de respeto"],
        ["decir cuál música es mejor", "no explicar la transmisión"],
        "Reconoce las descripciones y pide explicar por qué la misma frase de respeto no sirve para comparar las dos músicas.",
    ),
    "Escribe una música de tu entorno y cómo se transmite.",
    "Describe cómo cambiaría una canción que conoces si pasara de boca en boca entre cinco personas.",
)

# ---------------------------------------------------------------- OA 07 · clase 3 (diversidad y respeto)
L(
    OA7, 3,
    "Lápiz y papel. Los casos y las encuestas son inventados («de ejemplo») y están en los ejercicios. No necesitas materiales especiales. Sobre la música de pueblos originarios, la información tradicional la entregan las personas de esas comunidades o un educador o educadora tradicional.",
    "Aprenderé a respetar la diversidad de músicas y de comunidades: escuchar con curiosidad, preguntar con respeto, no ridiculizar y cuidar las músicas que pertenecen a una comunidad. Sirve para convivir y aprender de músicas distintas a las mías.",
    ["Sé explicar el contexto de una música.", "Sé reconocer funciones de la música.", "Sé calcular porcentajes sencillos."],
    [
        "En nuestro país conviven comunidades con músicas muy distintas, y cada una tiene sentido para quienes la cultivan. Respetar la diversidad significa escuchar con atención, preguntar con curiosidad y reconocer que cada música cumple una función en su comunidad. Decir «no me gusta» expresa un gusto personal. Decir «es fea» o «es rara» juzga a la comunidad que la hace, y eso no es respetuoso.",
        "Algunas músicas son parte de ceremonias o tradiciones de una comunidad. Esas músicas pertenecen a esa comunidad y su forma tradicional la enseñan las personas que la cultivan, por ejemplo un educador o educadora tradicional. Por eso no se imitan en broma, no se usan como disfraz ni se copian ritos. Si se quiere conocer una música así, se pregunta y se acepta lo que la comunidad desee compartir.",
        "Al conocer una música nueva, conviene seguir tres pasos: escuchar en silencio, anotar lo que se oye y preguntar para qué se usa. Después se puede decir qué rasgos llamaron la atención, sin comparar su valor con el de otras músicas. En el curso, respetar la diversidad también es valorar lo que cada estudiante trae de su familia o su barrio, sin obligar a nadie a mostrar lo que no quiere.",
    ],
    [("diversidad", "existencia de muchas formas distintas de hacer música"), ("respeto", "valorar y cuidar a las personas y a sus músicas sin burlarse"), ("gusto personal", "lo que a mí me gusta o no, sin juzgar a otras personas"), ("juzgar", "decir que algo es bueno o malo sin conocerlo"), ("educador o educadora tradicional", "persona que enseña los saberes de su pueblo según la tradición de su comunidad")],
    [
        ("Distinguir gusto y juicio", "¿«No me gusta esta música» expresa un gusto personal o un juicio sobre la comunidad que la hace?", ["Habla de lo que le pasa a quien lo dice.", "No dice nada malo sobre la comunidad."], "Un gusto personal"),
        ("Calcular una preferencia", "En una encuesta de ejemplo de 30 estudiantes, 12 prefieren música para bailar. ¿Cuántos prefieren otra cosa?", ["Se resta lo que prefieren bailar del total.", "30 − 12 = 18."], "18 estudiantes"),
    ],
    [
        ("Imitar en broma un canto de una ceremonia.", "Esa música pertenece a una comunidad y tiene un sentido propio.", "Pide información y acepta lo que la comunidad quiera compartir."),
        ("Decir que una música es fea porque no la entiendo.", "No conocerla no es lo mismo que ser mala.", "Anota lo que oyes y pregunta para qué se usa."),
    ],
    [
        ex("Burlarse de la música de otra comunidad, ¿es respetuoso? Responde sí o no.", "No", "Juzga a las personas que la cultivan."),
        ex("Al conocer una música nueva, ¿conviene preguntar para qué se usa? Responde sí o no.", "Sí", "Ayuda a comprender su función."),
        ex("«No me gusta esta música», ¿es un gusto personal o un juicio sobre una comunidad?", "Un gusto personal", "Habla de la propia opinión."),
    ],
    [
        ex("Al escuchar una música desconocida, ¿qué es mejor? A) Escuchar, anotar lo que se oye y preguntar para qué se usa. B) Decir cuál música es la mejor.", "A", "Así se aprende sin juzgar."),
        ex("Una música es parte de una ceremonia de una comunidad. ¿Quién enseña su forma tradicional: la comunidad o un video de una persona desconocida?", "La comunidad", "Quienes la cultivan son quienes pueden enseñarla."),
        ex("Una música se está presentando. ¿Qué es más respetuoso? A) Escuchar en silencio. B) Comentar en voz alta mientras toca para mostrar que ya la conoces.", "A", "Escuchar con atención muestra respeto."),
    ],
    [
        arith("En una encuesta de ejemplo de 30 estudiantes, 9 prefieren música tradicional. ¿Qué porcentaje es?", "9*100//30", "Se divide el número por el total y se multiplica por 100.", " %"),
        arith("Una muestra del curso presenta 5 músicas de comunidades distintas, de 4 minutos cada una. ¿Cuántos minutos dura la muestra?", "5*4", "Se multiplican las músicas por los minutos de cada una.", " minutos"),
        ex("Un compañero dice que la música de otra comunidad es «rara y fea». ¿Qué respuesta es respetuosa? A) «A mí me suena distinta; ¿para qué se usa?». B) «Tienes razón, es rara».", "A", "Muestra curiosidad y no juzga."),
    ],
    [
        ex("Un estudiante dice: «La música de mi barrio es mejor que la de otros lugares». ¿Qué conviene responder: que cada música cumple una función en su comunidad o que tiene razón?", "Que cada música cumple una función en su comunidad", "No se compara el valor de las músicas."),
        ex("Un compañero quiere poner un canto ceremonial de una comunidad como música de fondo de un video de broma. ¿Qué conviene hacer: no usarlo en la broma y pedir información a la comunidad, o usarlo igual?", "No usarlo en la broma y pedir información a la comunidad", "Esa música pertenece a la comunidad y no se usa en broma."),
    ],
    [
        arith("En una muestra del curso, 3 grupos presentan 2 minutos de explicación y 4 minutos de música cada uno. ¿Cuántos minutos dura en total?", "3*(2+4)", "Cada grupo usa 6 minutos y hay 3 grupos.", " minutos"),
        arith("De un curso de 30 estudiantes participan 24 en la muestra. ¿Qué porcentaje participa?", "24*100//30", "Se divide lo que participan por el total y se multiplica por 100.", " %"),
    ],
    [ex("Una compañera cuenta que en su comunidad un canto solo se canta en ceremonias. ¿Qué hace el curso? A) Respeta lo que ella decida compartir. B) Le pide que lo cante igual.", "A", "Nadie está obligado a mostrar lo que no desea.")],
    [ex("¿Qué se hace primero al conocer una música nueva?", "Escuchar en silencio", "Es el primer paso."), ex("¿Qué diferencia hay entre gusto personal y juicio?", "El gusto habla de mí y el juicio de la comunidad", "Solo el primero es una opinión personal."), ex("¿Quién enseña la forma tradicional de una música ceremonial?", "La comunidad o un educador tradicional", "Así lo dice la clase.")],
    (
        "Revisa este caso de ejemplo. Tu curso prepara una muestra con músicas de distintos lugares. Un compañero propone hacer una burla de un canto ceremonial «para reírse un rato». Una compañera dice que su familia cultiva una música tradicional y que prefiere no mostrarla. Otro compañero dice que la música que él escucha es «mucho mejor» que las demás. Escribe 1) qué responderías a cada uno con una frase respetuosa, 2) qué tres pasos seguirías para conocer una música nueva, 3) qué harías si quisieras aprender una música ceremonial de una comunidad.",
        "1) «No usemos ese canto en broma: pertenece a una comunidad.» «Respetamos que prefieras no mostrarla.» «Cada música tiene su función; compartamos lo que oímos de cada una.» 2) Escuchar en silencio, anotar lo que se oye y preguntar para qué se usa. 3) Preguntaría a personas de esa comunidad o a un educador tradicional y aceptaría lo que quieran compartir.",
        ["no ridiculiza ni compara", "respeta la decisión de no mostrar", "sigue los tres pasos para conocer una música"],
        ["tres respuestas respetuosas", "tres pasos", "plan para aprender con la comunidad"],
        ["usar el canto ceremonial en broma", "obligar a alguien a mostrar su música"],
        "Reconoce las respuestas y pide explicar por qué un canto ceremonial no se imita en broma.",
    ),
    "Escribe una frase respetuosa que dirías al conocer una música que no entiendes.",
    "Escribe qué harías para preparar una muestra del curso que valore las músicas de todos sin obligar a nadie a mostrarlas.",
)

# ---------------------------------------------------------------- OA 07 · clase 4 (mi experiencia y mi lugar en la sociedad)
L(
    OA7, 4,
    "Lápiz y papel. La encuesta del curso es de ejemplo y está escrita en los ejercicios. Si quieres, aplica lo aprendido haciendo preguntas parecidas a personas de tu casa, sin anotar nombres.",
    "Aprenderé a describir el lugar que ocupa la música en mi comunidad y en mi curso usando datos de una mini-encuesta, y a presentar conclusiones respetando las respuestas de todos. Sirve para apreciar el rol de la música a partir del repertorio que hemos trabajado.",
    ["Sé reconocer funciones de la música.", "Sé explicar el contexto de una música.", "Sé calcular porcentajes sencillos."],
    [
        "Una mini-encuesta ayuda a conocer qué lugar tiene la música en un grupo. Se hace una pregunta y se anotan las respuestas en una tabla, sin nombres. En una encuesta de ejemplo en un curso de 30 estudiantes, se pregunta para qué usan la música: 12 para bailar, 8 para calmarse, 6 para concentrarse y 4 para celebrar. La suma de las respuestas es 30, igual que el total de estudiantes, porque cada persona eligió una sola opción.",
        "Con la tabla se hacen conclusiones que se apoyan en datos: «bailar es la función más frecuente, con 12 de 30 estudiantes». Se calcula el porcentaje: 12 ÷ 30 × 100 = 40 %. No se debe concluir más de lo que muestran los datos. «La mayoría usa la música para bailar» sería falso, porque 12 no es más de la mitad de 30. Y cada respuesta, aunque sea minoritaria, merece respeto.",
        "Para apreciar el rol de la música en la sociedad, se relacionan los datos con el repertorio trabajado: se pueden nombrar las funciones que se conocieron y un rasgo audible de cada una. Una presentación respetuosa incluye una breve introducción, los datos, una conclusión y una frase que valore la diversidad de respuestas. Nadie está obligado a contar cosas íntimas de su familia o de su vida.",
    ],
    [("mini-encuesta", "pregunta que se hace a un grupo y cuyas respuestas se anotan en una tabla"), ("dato", "número o respuesta anotada que sirve de evidencia"), ("porcentaje", "parte de cada 100"), ("conclusión", "idea que se obtiene a partir de los datos"), ("minoritaria", "que elige una parte menor del grupo")],
    [
        ("Leer la tabla", "Encuesta de ejemplo de 30 estudiantes: bailar 12, calmarse 8, concentrarse 6, celebrar 4. ¿Cuántos usan la música para celebrar o para concentrarse?", ["Se suman las dos respuestas.", "6 + 4 = 10."], "10 estudiantes"),
        ("Calcular un porcentaje", "En esa encuesta, ¿qué porcentaje usa la música para bailar?", ["Se dividen los 12 por los 30.", "12 ÷ 30 × 100 = 40."], "40 %"),
    ],
    [
        ("Concluir «la mayoría» con menos de la mitad.", "Mayoría es más de la mitad del grupo.", "Compara el número con la mitad del total."),
        ("Obligar a alguien a contar cosas personales en la encuesta.", "Cada persona decide qué comparte, y las encuestas no llevan nombres.", "Pregunta sin anotar nombres y acepta que alguien no responda."),
    ],
    [
        ex("Encuesta de ejemplo de 30 estudiantes: bailar 12, calmarse 8, concentrarse 6, celebrar 4. ¿Cuántos estudiantes usan la música para calmarse?", "8", "Es el dato de esa fila."),
        ex("En esa misma encuesta, ¿cuál es la función más frecuente?", "Bailar", "Tiene el número mayor: 12."),
        ex("En esa misma encuesta, ¿cuántas funciones distintas aparecen?", "4", "Son bailar, calmarse, concentrarse y celebrar."),
    ],
    [
        arith("Encuesta de ejemplo: bailar 12, calmarse 8, concentrarse 6, celebrar 4. ¿Cuántos estudiantes usan la música para bailar o celebrar?", "12+4", "Se suman las dos respuestas.", " estudiantes"),
        arith("En esa encuesta, ¿cuántos estudiantes más usan la música para bailar que para concentrarse?", "12-6", "Se resta el número de la función menos frecuente del de la más frecuente.", " estudiantes más"),
        ex("¿Qué conclusión se apoya en los datos? A) Bailar es la función más frecuente, con 12 de 30 estudiantes. B) Más de la mitad del curso usa la música para bailar.", "A", "12 de 30 es menos de la mitad."),
    ],
    [
        arith("En otro curso de ejemplo respondieron 24 estudiantes y 6 eligieron calmarse. ¿Qué porcentaje es?", "6*100//24", "Se divide lo que eligieron calmarse por el total y se multiplica por 100.", " %"),
        arith("¿Cuánto suman todas las respuestas de la encuesta de ejemplo (bailar 12, calmarse 8, concentrarse 6, celebrar 4)?", "12+8+6+4", "La suma debe coincidir con el total de estudiantes, porque cada uno eligió una sola opción.", " respuestas"),
        ex("La mitad de 30 estudiantes es 15. ¿Es mayoría que 12 estudiantes usen la música para bailar? Responde sí o no.", "No", "12 es menos que 15, la mitad del curso."),
    ],
    [
        ex("Ana concluye: «A nadie le gusta la música tradicional». Su encuesta no preguntó por ella. ¿Qué falla en su conclusión?", "No se apoya en datos", "No preguntó por ese tema."),
        ex("Un estudiante responde algo distinto al resto en la encuesta. ¿Qué se hace con su respuesta: se registra y se respeta, o se corrige?", "Se registra y se respeta", "Cada respuesta es válida y se anota."),
    ],
    [
        arith("Para la presentación, el curso dedica 2 minutos a cada una de las 4 funciones y 3 minutos a la introducción. ¿Cuántos minutos dura?", "4*2+3", "Se suman los minutos de las funciones y de la introducción.", " minutos"),
        arith("En la encuesta de ejemplo, ¿cuántos estudiantes eligieron las dos funciones menos frecuentes (concentrarse y celebrar)?", "6+4", "Se suman los estudiantes de esas dos funciones.", " estudiantes"),
    ],
    [arith("Para el aniversario del colegio, 16 de 30 estudiantes prefieren música para bailar. ¿Cuántos tienen otra preferencia que el curso debe tomar en cuenta?", "30-16", "Se restan los 16 del total.", " estudiantes")],
    [ex("¿Qué se anota en una mini-encuesta: nombres o respuestas?", "Respuestas, sin nombres", "Así se cuida la privacidad."), ex("¿Qué es una mayoría?", "Más de la mitad", "Más de la mitad del grupo."), ex("¿Hay que respetar las respuestas que elige poca gente? Responde sí o no.", "Sí", "Cada respuesta merece respeto.")],
    (
        "Usa esta encuesta de ejemplo de un curso de 20 estudiantes sobre «¿para qué usas la música?»: bailar 8, calmarse 6, concentrarse 4, celebrar 2. Escribe 1) cuántos suman las respuestas, 2) cuál es la función más frecuente y qué porcentaje del curso representa, 3) una conclusión que se apoye en los datos, 4) una frase que valore las respuestas minoritarias, 5) la función que más te interesa conocer mejor y un rasgo audible que la sostenga (por ejemplo, el tempo o el volumen).",
        "1) 20. 2) Bailar, 8 de 20 = 40 %. 3) «Bailar es la función más frecuente, con 8 de 20 estudiantes.» 4) «Las respuestas de celebrar y concentrarse también son valiosas.» 5) Calmarse: el tempo lento y el volumen suave.",
        ["calcula bien la suma y el porcentaje", "la conclusión se apoya en los datos", "valora las respuestas minoritarias"],
        ["suma y porcentaje", "conclusión", "frase de respeto"],
        ["decir «la mayoría» con 40 %", "anotar nombres de personas"],
        "Reconoce los datos y pide explicar por qué 8 de 20 no es la mayoría.",
    ),
    "Pregunta a una persona de tu casa para qué usa la música y anota su respuesta, sin nombre.",
    "Haz una mini-encuesta de cinco respuestas y escribe una conclusión que se apoye en los datos.",
)
