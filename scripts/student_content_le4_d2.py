"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 25 (conversación grupal enfocada y respetuosa)."""
from __future__ import annotations

from student_content_le4_d import E, reg
from student_lessons import arith

OA25 = "LE04 OA 25"

# ================================================================ OA 25 · clase 1
reg(
    OA25, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar el tema.",
    "Aprenderé a preparar una idea u opinión con un respaldo antes de conversar en grupo. Sirve para que los demás entiendan qué pienso y por qué, y para participar con confianza.",
    ["Sé distinguir un dato de lo que alguien piensa.", "Sé usar «porque» para dar una razón."],
    [
        "En una conversación grupal cada persona puede dar una idea u opinión, que es lo que piensa sobre un tema. Para que los demás la tomen en cuenta, conviene respaldarla con un fundamento. El fundamento es una razón, un dato del texto que leímos o un ejemplo que apoya la idea. Una opinión sin fundamento queda en el aire: no sabemos por qué la persona piensa así.",
        "Podemos preparar lo que vamos a decir en tres partes: la idea («Creo que…»), la razón («porque…») y un ejemplo («por ejemplo…»). Cuando el tema viene de un texto, buscamos en él un dato que apoye nuestra idea y lo nombramos. También conviene preparar una frase corta, porque así quedan tiempo y espacio para que hablen los demás.",
        "Un dato es algo que se puede comprobar, como «las plantas se secaron en vacaciones». Una opinión es lo que alguien piensa, como «es mejor regar en vacaciones». Podemos opinar distinto, pero cada opinión debería tener una razón que los demás puedan evaluar.",
    ],
    [("opinión", "lo que alguien piensa sobre un tema"), ("fundamento", "razón, dato o ejemplo que apoya una idea"), ("dato", "información que se puede comprobar"), ("ejemplo", "caso concreto que muestra una idea"), ("tema", "asunto sobre el que se conversa")],
    [
        ("Armar una intervención", "Texto «El huerto»: En la escuela de Lina plantaron un huerto en el patio. Cada curso riega los martes y los jueves. En marzo nacieron lechugas y rabanitos. En las vacaciones de invierno nadie regó y varias plantas se secaron. Idea: «Conviene que alguien riegue en vacaciones». ¿Qué dato del texto la respalda?", ["Busco qué pasó cuando nadie regó.", "El texto dice que varias plantas se secaron.", "Ese dato apoya la idea."], "Que en las vacaciones de invierno nadie regó y varias plantas se secaron."),
        ("Distinguir dato y opinión", "¿«Es mejor que alguien riegue en vacaciones» es un dato o una opinión?", ["Pregunto si se puede comprobar.", "Es lo que alguien piensa que conviene.", "No es algo comprobable."], "Es una opinión."),
    ],
    [("Dar una opinión sin ninguna razón.", "Se cree que basta decir lo que uno piensa.", "Agrega «porque…» con un dato, una razón o un ejemplo."), ("Dar un fundamento que no tiene relación con la idea.", "Se elige un dato cualquiera para completar.", "Comprueba que el dato realmente apoya lo que dices.")],
    [
        E("Según el texto «El huerto», ¿qué días riega cada curso?", "Los martes y los jueves", "Está escrito en el texto."),
        E("¿Qué pasó con las plantas cuando nadie regó en las vacaciones?", "Varias se secaron", "Lo dice el texto."),
        E("¿Cuál es una opinión: a) «Cada curso riega dos días.» b) «Es mejor que alguien riegue en vacaciones.»?", "b", "La b dice lo que alguien piensa que conviene."),
    ],
    [
        E("¿Qué es un fundamento?", "Una razón, dato o ejemplo que apoya una idea", "Sirve para explicar por qué pensamos algo."),
        E("En «Conviene regar en vacaciones porque las plantas se secan», ¿qué palabra introduce la razón?", "Porque", "Después de «porque» viene la razón."),
        E("La idea «Creo que el huerto es lindo» ¿necesita un fundamento?", "Sí", "Falta decir por qué lo piensa."),
    ],
    [
        arith("Un curso riega dos días a la semana. ¿Cuántos riegos hace en cuatro semanas?", "2*4", "Se repite dos riegos por semana durante cuatro semanas.", " riegos"),
        E("Ordena una intervención: a) porque en vacaciones nadie regó, b) Creo que debe haber turnos de riego, c) Por ejemplo, varias plantas se secaron. Escribe las letras.", "b, a, c", "Primero la idea, luego la razón y al final el ejemplo."),
        E("Elige el dato que apoya la idea «Hay que regar en vacaciones»: a) los rabanitos son rojos b) varias plantas se secaron sin riego.", "b", "Muestra qué pasa cuando nadie riega."),
    ],
    [
        E("Pablo dice: «El huerto es lo mejor de la escuela». Ema dice: «Se debe regar en vacaciones, porque varias plantas se secaron cuando nadie regó». ¿Quién respalda su idea con un dato del texto?", "Ema", "Su razón viene del texto."),
        E("Para apoyar «hay que regar en vacaciones», ¿qué razón sirve más: a) las plantas necesitan agua para vivir b) a mí me gusta el color verde?", "a", "La a explica por qué regar."),
    ],
    [
        E("¿Cuál frase usa un dato del texto: a) «Los rabanitos nacieron en marzo» b) «Siempre llueve en invierno» c) «Los huertos son difíciles»?", "a", "Solo la a aparece en el texto."),
        E("En «Creo que hay que regar en vacaciones porque nacieron lechugas en marzo y se secaron varias plantas en invierno», ¿cuántos datos del texto se nombran?", "Dos", "Una es nacieron lechugas en marzo y la otra, se secaron plantas en invierno."),
    ],
    [E("Tema: ¿Debe haber una hora de lectura silenciosa en el recreo largo? Una compañera dice: «Sí, porque en el recreo largo hay tiempo y así quienes quieren leer pueden hacerlo tranquilos». ¿Qué parte es la razón?", "Porque en el recreo largo hay tiempo y así quienes quieren leer pueden hacerlo tranquilos", "Sigue a «porque» y explica la idea.")],
    [
        E("Una idea con respaldo, ¿incluye una razón?", "Sí", "La razón sustenta la idea."),
        E("¿Una opinión puede comprobarse como un dato?", "No", "Una opinión es lo que alguien piensa."),
        E("¿Conviene preparar una frase corta antes de hablar?", "Sí", "Así quedan tiempo y espacio para los demás."),
    ],
    ("Prepara tu intervención sobre este tema: «¿Conviene tener un huerto en el patio de la escuela?». Usa el texto «El huerto» de esta clase. Escribe o di: 1) tu idea, 2) una razón con «porque», 3) un dato del texto que la apoye. Luego di tu intervención a una persona de tu casa y pídele que diga si entendió tu idea y tu razón.",
     "Creo que conviene tener un huerto en el patio, porque los cursos aprenden a cuidar plantas. En el texto, en marzo nacieron lechugas y rabanitos.",
     ["expresa una idea clara", "da una razón con «porque»", "nombra un dato del texto", "se entiende al decirla"], ["intervención escrita u oral"], ["dar opinión sin razón", "usar un dato que no está en el texto"],
     "Si falta el respaldo, pregúntate: ¿qué dato del texto muestra que mi idea es razonable?"),
    "Lee otra vez el texto y escribe dos datos que podrían apoyar la idea contraria.",
    "Prepara dos intervenciones, una a favor y otra en contra de regar en vacaciones, cada una con su razón.",
)

# ================================================================ OA 25 · clase 2
reg(
    OA25, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer en voz alta la conversación.",
    "Aprenderé a mantener el foco de una conversación: mantenerme en el tema, notar cuándo nos desviamos y volver a él. Sirve para que el grupo se entienda y llegue a una conclusión.",
    ["Sé dar una opinión con una razón.", "Sé esperar mi turno para hablar."],
    [
        "Toda conversación grupal tiene un tema, que es de lo que se conversa. Mantener el foco significa que lo que decimos tiene relación con ese tema. Cuando alguien habla de otra cosa, la conversación se desvía y el grupo pierde tiempo. Un desvío no siempre es mala intención: a veces algo nos recuerda otra historia.",
        "Para cuidar el foco podemos anotar el tema en una hoja a la vista y preguntarnos antes de hablar: ¿lo que voy a decir aporta al tema? Si me desvié o noto que otro se desvió, puedo retomar con una frase como «Volviendo al tema…» o «Eso sirve para…, pero lo que conversábamos era…». Hacerlo con respeto evita que la persona se sienta regañada.",
        "También cuidamos la conversación respetando los turnos: hablamos uno a la vez, levantamos la mano si hace falta y escuchamos sin interrumpir. Si tenemos una idea que no es del tema, la podemos anotar y decirla después.",
    ],
    [("foco", "tema central en el que se mantiene la conversación"), ("desvío", "momento en que se habla de algo que no es el tema"), ("retomar", "volver al tema después de un desvío"), ("turno", "momento que le toca hablar a cada persona"), ("aporte", "idea que ayuda a avanzar en el tema")],
    [
        ("Notar un desvío", "Tema: cómo cuidar la biblioteca del curso. Ana: «Propongo que cada semana una persona ordene los libros». Beto: «Ayer vi un perro enorme en la calle». ¿Quién se desvió del tema?", ["Pregunto si cada frase habla de la biblioteca.", "Ana habla de ordenar libros.", "Beto habla de un perro, que no es el tema."], "Beto."),
        ("Retomar con respeto", "Carla le dice a Beto: «Volviendo a la biblioteca, ¿y si hacemos una lista de turnos?». ¿Qué hace Carla?", ["Veo qué dice al empezar.", "Usa «volviendo a la biblioteca».", "Así retoma el tema sin criticar."], "Retoma el tema con respeto."),
    ],
    [("Hablar de lo primero que se nos ocurre aunque no sea del tema.", "Una idea nos recuerda otra historia y la contamos enseguida.", "Pregunta antes de hablar: ¿esto aporta al tema? Si no, anótalo para después."), ("Decir «cállate, eso no es del tema».", "Se confunde retomar el tema con regañar.", "Usa una frase amable: «Volviendo al tema…».")],
    [
        E("Tema: cuidar la biblioteca. ¿«Ayer vi un perro enorme» aporta al tema?", "No", "No habla de la biblioteca."),
        E("¿Cuál frase sirve para retomar el tema: «Volviendo al tema…» o «Eso es tonto»?", "Volviendo al tema…", "Es amable y señala el tema."),
        E("¿Qué es el foco de una conversación?", "El tema central", "Se trata de mantenerse en él."),
    ],
    [
        E("Tema: cuidar la biblioteca. Intervenciones: Ana propone turnos para ordenar libros; Beto cuenta del perro; Carla propone una lista de turnos; Dani dice «Así todos participan». ¿Cuántas intervenciones aportan al tema?", "Tres", "Aportan Ana, Carla y Dani."),
        E("¿Por qué conviene anotar el tema en una hoja a la vista?", "Para recordar de qué se conversa", "Así se nota cuándo alguien se desvía."),
        E("Dani levanta la mano y espera a que Carla termine. ¿Qué cuida Dani?", "El turno", "Respeta que hable una persona a la vez."),
    ],
    [
        E("Tema: cómo organizar el diario mural del curso. Lola dice: «Sugiero dividir el mural en secciones por materia». ¿Esa intervención aporta al tema?", "Sí", "Habla de cómo organizar el mural."),
        E("En el mismo tema, Tomás dice: «Me gusta el fútbol». ¿Qué frase amable puede usar Lola para retomar: a) «Volviendo al mural, ¿qué secciones propones?» b) «¡Siempre te sales del tema!»?", "a", "La a retoma sin regañar."),
        E("Tema: normas del patio. Pía quiere decir algo sobre su cumpleaños. ¿Qué conviene hacer: a) anotarlo y decirlo al final b) contarlo ahora aunque interrumpa?", "a", "Así no se pierde el foco ni su idea."),
    ],
    [
        E("Dos compañeros conversan sobre cuidar el curso. Uno dice: «Podemos ordenar los útiles cada viernes». El otro: «Mi tío tiene una moto roja». ¿Quién mantiene el foco?", "El primero", "Habla de cuidar el curso."),
        E("A veces un comentario fuera del tema es útil si ayuda al tema. Tema: huerto. «Mi abuela dice que las plantas se riegan temprano». ¿Aporta o se desvía?", "Aporta", "Da una idea para el cuidado del huerto."),
    ],
    [
        E("Tema: festejar el cierre del año. Escena: Ema propone una muestra de dibujos. Luis cuenta de su perro. Rosa dice «Volvamos a la muestra: ¿dónde la hacemos?». Ordena quién habla: a) Luis b) Ema c) Rosa. Escribe las letras.", "b, a, c", "Primero propone Ema, luego Luis se desvía y Rosa retoma."),
        E("En esa escena, ¿qué hizo Rosa para volver al foco?", "Propuso volver a la muestra y preguntó dónde hacerla", "Retomó el tema con una pregunta."),
    ],
    [E("Tema: cómo mantener limpia la sala. Intervención de Mateo: «Creo que cada fila podría recoger los papeles al final del día. Además, mi hermana tiene un loro». ¿Qué parte se desvía?", "Lo del loro de su hermana", "No habla de limpiar la sala.")],
    [
        E("Para mantener el foco, ¿conviene preguntarse si lo que digo aporta al tema?", "Sí", "Así evito desvíos."),
        E("¿Retomar el tema es regañar a quien se desvió?", "No", "Se hace con respeto."),
        E("Si tengo una idea que no es del tema, ¿puedo anotarla para decirla después?", "Sí", "No se pierde y no desvía al grupo."),
    ],
    ("Conversa con una o más personas de tu casa sobre este tema: «Cómo podemos cuidar un espacio común de la casa o de la escuela». Antes de empezar, escribe el tema en una hoja a la vista. Durante la conversación, da al menos dos ideas que aporten al tema y, si alguien se desvía, usa una frase amable para retomar. Al final escribe qué frase usaste y si el grupo se mantuvo en el foco.",
     "Escribí en la hoja: cuidar el comedor. Dije: «Podemos limpiar la mesa después de cada comida» y «Cada uno lleva su plato». Cuando hablamos de una película, dije: «Volviendo al comedor, ¿quién limpia el lunes?». Sí nos mantuvimos en el foco.",
     ["escribe el tema a la vista", "da al menos dos ideas del tema", "usa una frase amable para retomar si hace falta", "revisa si se mantuvo el foco"], ["notas con el tema, las ideas y la frase usada"], ["dar ideas que no se relacionan con el tema", "regañar a quien se desvía"],
     "Si el grupo se desvió mucho, prueba una frase breve: «Volviendo a…»."),
    "Escribe tres frases amables para retomar el tema de una conversación.",
    "Anota en un papel tres temas y, para cada uno, una idea que aporta y otra que se desvía.",
)

# ================================================================ OA 25 · clase 3
reg(
    OA25, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para practicar las preguntas.",
    "Aprenderé a preguntar para aclarar dudas y para verificar que entendí lo que dijeron. Sirve para evitar malentendidos y mostrar interés por lo que otras personas dicen.",
    ["Sé mantener el foco de una conversación.", "Sé esperar mi turno y escuchar sin interrumpir."],
    [
        "Cuando alguien habla, a veces no entendemos una palabra, una idea o a qué se refiere. En esos casos conviene preguntar para aclarar. Una pregunta para aclarar busca entender mejor, no criticar. Podemos decir: «¿Qué quieres decir con…?», «¿Puedes dar un ejemplo?» o «¿A qué te refieres cuando dices…?».",
        "Otra manera de verificar que entendimos es repetir con nuestras palabras lo que escuchamos y preguntar si está bien. Eso se llama parafrasear. Por ejemplo: «¿Entendí bien que propones que cada curso cuide un rincón del patio?». Si la persona dice que sí, seguimos; si dice que no, nos corrige y evitamos un malentendido.",
        "Preguntar con interés se nota en la mirada, en el tono de voz y en esperar la respuesta. Una pregunta como «¿Cómo se te ocurre eso?», dicha con burla, no aclara nada: critica. Por eso usamos un tono amable y esperamos nuestro turno para preguntar.",
    ],
    [("aclarar", "hacer que algo se entienda mejor"), ("parafrasear", "decir con otras palabras lo que alguien dijo"), ("malentendido", "error que ocurre cuando se entiende mal algo"), ("ejemplo", "caso concreto que ayuda a entender"), ("interés", "ganas de saber y escuchar a otra persona")],
    [
        ("Elegir la pregunta que aclara", "Leo dice: «Propongo que usemos el rincón para las visitas». Ema no sabe qué rincón ni qué visitas. ¿Qué pregunta aclara mejor: a) «¿Qué rincón y qué visitas?» b) «¿Para qué dices eso?»", ["Busco la pregunta que pide información.", "La a pide detalles de lo que no se entendió.", "La b suena a reproche."], "a."),
        ("Parafrasear", "Leo dice: «Cada curso cuidará un rincón del patio». Ema responde: «¿Entendí bien que cada curso se encargará de un rincón?». ¿Qué hizo Ema?", ["Compara lo que dijo Leo con lo que dijo Ema.", "Ema lo dijo con otras palabras.", "Luego preguntó si lo entendió bien."], "Parafraseó para verificar que entendió."),
    ],
    [("Preguntar con burla, como «¿Cómo se te ocurre eso?».", "Se usa la pregunta para criticar, no para entender.", "Pregunta con tono amable: «¿Qué quieres decir con eso?»."), ("Seguir sin preguntar aunque no hayamos entendido.", "Da vergüenza o miedo interrumpir.", "Espera tu turno y pregunta; entender es parte de conversar.")],
    [
        E("¿Para qué sirve preguntar «¿Qué quieres decir con…?»?", "Para entender mejor lo que dijo la persona", "Aclara una duda."),
        E("Parafrasear es decir con otras palabras lo que escuchamos. ¿Es verdadero o falso?", "Verdadero", "Esa es la definición de parafrasear."),
        E("Elige la pregunta que aclara: a) «¿Puedes dar un ejemplo?» b) «¿Qué tonterías dices?»", "a", "La a busca entender; la b ofende."),
    ],
    [
        E("Ana dice: «Haremos el afiche más tarde». Beto no sabe cuándo es «más tarde». ¿Qué pregunta aclara: a) «¿A qué hora, más tarde?» b) «¿Siempre lo dejas para después?»", "a", "Pide el dato que falta."),
        E("¿Para qué se pregunta «¿Entendí bien que…?»", "Para verificar si entendí lo que dijeron", "Se comprueba la comprensión."),
        E("Si la persona responde «no, no es eso», ¿qué se evitó gracias a la pregunta?", "Un malentendido", "Se corrigió antes de seguir."),
    ],
    [
        E("Rosa dice: «Haremos la rifa de los útiles a fin de mes». Escribe una pregunta para verificar que entendiste el momento.", "¿Entendí bien que la rifa será a fin de mes?", "Repite el dato y pide confirmación."),
        E("Marcos dice: «Necesitamos varios cartones». ¿Qué duda queda: a) cuántos cartones b) de qué color es el cielo?", "a", "«Varios» no dice la cantidad."),
        E("Tomás dice: «El plan está listo». Lola pregunta: «¿Qué incluye el plan?». ¿Qué quiere saber Lola?", "Qué partes tiene el plan", "Pide más información sobre lo dicho."),
    ],
    [
        E("Dos preguntas para Pía, que dijo: «Voy a traer cosas para la exposición». 1: «¿Qué cosas vas a traer?». 2: «¿Y para qué sirve lo que traes, si no sabes hacer nada?». ¿Cuál es una pregunta para aclarar?", "La 1", "Pide detalles sin criticar."),
        E("Ema escucha: «Reuniremos los trabajos el miércoles». Pregunta: «¿Entendí bien que los traigo el miércoles?». Pero Luis responde: «No, los reunimos el miércoles, tráelos antes». ¿Qué corrigió la pregunta?", "Entendió mal cuándo debía traerlos", "El malentendido era sobre la fecha de entrega."),
    ],
    [
        E("Una compañera dice: «Vamos a repartir roles». Tú no sabes qué roles. ¿Qué dos preguntas aclaran: a) ¿Qué roles hay? b) ¿Quién los reparte? c) ¿Para qué hablas tanto? Escribe las letras.", "a, b", "Piden información; la c critica."),
        E("Álvaro dice: «El proyecto lleva tres cosas». Ema dice: «¿Entendí bien que son tres partes?». ¿Qué falta verificar todavía?", "Cuáles son las tres cosas", "Solo se verificó el número."),
    ],
    [E("En la conversación sobre el paseo, Nico dice: «Iremos al parque». Hay dos parques en el barrio, el chico y el grande. Hugo pregunta: «¿Entendí bien que iremos al parque grande?». ¿Qué duda quiere aclarar Hugo?", "A cuál de los dos parques irán", "Quiere asegurarse de a cuál se refiere.")],
    [
        E("¿Preguntar para aclarar muestra interés?", "Sí", "Muestra que escucho y quiero entender."),
        E("¿Una pregunta con burla aclara dudas?", "No", "Critica en vez de ayudar a entender."),
        E("Antes de preguntar, ¿conviene esperar mi turno?", "Sí", "Así respeto a quien habla."),
    ],
    ("Practica con una persona de tu casa. Pídele que te diga estas tres frases, una por una: 1) «Mañana vamos a llevar cosas». 2) «El juego tiene reglas nuevas». 3) «Lo haremos más tarde». Para cada frase, escribe una pregunta para aclarar y una para verificar con «¿Entendí bien que…?». Luego anota qué respondió la persona.",
     "Frase 1. Aclarar: ¿Qué cosas vamos a llevar? Verificar: ¿Entendí bien que mañana llevamos las cosas? La persona dijo: llevamos una bolsa y agua.",
     ["hace una pregunta para aclarar por cada frase", "parafrasea para verificar", "usa un tono amable", "registra la respuesta"], ["preguntas escritas y respuesta anotada"], ["preguntar con burla", "no verificar con nuevas palabras"],
     "Si tu pregunta suena a reproche, cámbiala: «¿Qué quieres decir con…?»."),
    "Escribe dos formas amables de pedir un ejemplo cuando no entiendes.",
    "Crea un diálogo de cuatro líneas en que una pregunta para aclarar evita un malentendido.",
)

# ================================================================ OA 25 · clase 4
reg(
    OA25, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para conversar.",
    "Aprenderé a construir sobre lo que dijo otra persona: mostrar interés, agregar una idea que se conecte con la anterior y responder con empatía. Sirve para que la conversación avance y todos se sientan escuchados.",
    ["Sé mantener el foco de una conversación.", "Sé preguntar para aclarar sin criticar."],
    [
        "Una conversación avanza cuando nos escuchamos y construimos unas ideas sobre otras. Para eso mostramos interés: miramos a quien habla, no interrumpimos y podemos decir algo que muestre que escuchamos, como «Interesante lo que dices de…». Luego conectamos nuestra idea con la anterior usando frases como «Como dijo Ana…», «Agrego que…» o «Eso se relaciona con…».",
        "Construir sobre lo dicho es distinto de repetir lo mismo o de empezar otro tema. Agregamos algo nuevo: un ejemplo, una razón más o una consecuencia. Por ejemplo, si Ana dice «Podemos reciclar papel en la sala», podemos agregar: «Y además podríamos usar el reverso de las hojas para borradores».",
        "A veces alguien cuenta algo que le preocupa o lo pone triste. Mostrar empatía es ponerse en su lugar y reconocer lo que siente, sin burlarse ni dar órdenes. Podemos decir: «Entiendo que te sientas nervioso» o «Gracias por contarlo». Empatizar no significa estar siempre de acuerdo; significa tratar con respeto lo que la otra persona siente.",
    ],
    [("construir sobre lo dicho", "agregar una idea nueva conectada con la que dijo otra persona"), ("conector", "palabra o frase que une ideas, como «además» o «como dijo Ana»"), ("empatía", "ponerse en el lugar de otra persona y reconocer lo que siente"), ("interés", "ganas de escuchar y saber más"), ("aporte", "idea nueva que ayuda a avanzar")],
    [
        ("Agregar una idea nueva", "Ana: «Podemos reciclar papel en la sala». Beto responde: «Como dijo Ana, el papel se puede reciclar; además, usemos el reverso de las hojas para borradores». ¿Qué agrega Beto?", ["Busco qué idea nueva dice después de «además».", "Dice que se use el reverso de las hojas.", "Eso es nuevo, no repite lo de Ana."], "Que se use el reverso de las hojas como borradores."),
        ("Responder con empatía", "Lola cuenta: «Me da nervios hablar frente al curso». ¿Qué respuesta muestra empatía: a) «Entiendo que te sientas nerviosa; ¿qué te ayudaría?» b) «No es para tanto»?", ["Veo qué respuesta reconoce lo que siente.", "La a nombra la emoción y ofrece escuchar.", "La b minimiza lo que siente."], "a."),
    ],
    [("Repetir lo mismo que dijo otra persona como si fuera una idea nueva.", "Se quiere participar pero no se piensa algo propio.", "Agrega algo nuevo: un ejemplo, una razón o una consecuencia."), ("Responder a una emoción con «no es para tanto».", "Se cree que así se tranquiliza a la persona.", "Reconoce lo que siente: «Entiendo que te sientas así».")],
    [
        E("Ana propone reciclar papel. ¿Qué frase conecta con ella: «Como dijo Ana…» o «Cambiemos de tema»?", "Como dijo Ana…", "Une la idea nueva con la anterior."),
        E("En Lenguaje: ¿Qué es la empatía?", "Ponerse en el lugar de otra persona y reconocer lo que siente", "Es entender sus sentimientos."),
        E("Mostrar interés: ¿ayuda mirar a quien habla?", "Sí", "Indica que estás escuchando."),
    ],
    [
        E("Marta dice: «Hay que reciclar plástico». Rubén dice: «Hay que reciclar plástico». ¿Rubén construyó sobre lo dicho o repitió?", "Repitió", "No agregó nada nuevo."),
        E("Marta dice: «Hay que reciclar plástico». Rubén agrega: «Y poner un tarro con tapa en cada sala». ¿Qué aportó Rubén?", "Poner un tarro con tapa en cada sala", "Agregó cómo hacerlo."),
        E("Camila cuenta que perdió su peluche favorito. ¿Qué respuesta muestra empatía: a) «Qué pena; si quieres, te ayudo a buscarlo» b) «Eso es solo un peluche»?", "a", "La a reconoce su pena y ofrece ayuda."),
    ],
    [
        E("Ana dice: «Hagamos un mural». ¿Qué respuesta conecta con su idea: a) «Como dijo Ana, el mural puede mostrar nuestras normas» b) «Yo quiero cantar»?", "a", "La a une la idea nueva con la de Ana."),
        E("Juan dice: «Me da miedo equivocarme en la exposición». ¿Qué respuesta muestra empatía: a) «Entiendo que te dé miedo; a mí también me pasa a veces» b) «Eso es de bebés»?", "a", "Reconoce la emoción sin burlarse."),
        E("Tema: cómo cuidar los libros. Ema dice: «Forremos los libros». ¿Cuál agrega algo nuevo: a) «Y pongamos nombre en la primera página» b) «Forremos los libros»?", "a", "La a suma una idea nueva."),
    ],
    [
        E("Pía dice: «Podemos guardar los lápices en un frasco». Tomás dice: «Podemos guardar los lápices en un frasco, como dijo Pía». ¿Qué le falta a Tomás para construir sobre lo dicho?", "Una idea nueva", "Solo repitió lo de Pía."),
        E("Un niño dice: «Hoy estoy triste porque mi amigo se fue de la escuela». Otro responde: «Cambia el tema y juguemos». ¿Qué falta en esa respuesta?", "Empatía", "No reconoce lo que siente."),
    ],
    [
        E("Observa: Luis: «Propongo una biblioteca de aula». Paz: «Como dijo Luis, la biblioteca ayuda; además, cada niño podría traer un libro». Rita: «Eso se relaciona con lo de Paz: traer libros y turnos para leer». ¿Cuántas ideas distintas hay en total?", "Tres", "La biblioteca, traer libros y turnos para leer."),
        E("En esa conversación, ¿quién aporta una idea que no habían dicho los anteriores: a) Paz con «cada niño traería un libro» b) Luis con «una biblioteca»?", "a", "Luis abrió el tema; Paz agregó cómo juntar libros."),
    ],
    [E("Gabriel cuenta que no le salió bien un dibujo y se siente mal. Elige la mejor respuesta de grupo: a) «Entiendo que te sientas así; ¿quieres que te digamos qué parte nos gustó?» b) «Cualquiera dibuja mejor»", "a", "La a reconoce su emoción y lo apoya.")],
    [
        E("Construir sobre lo dicho, ¿es agregar algo nuevo conectado con lo anterior?", "Sí", "Así avanza la conversación."),
        E("Empatizar, ¿significa estar siempre de acuerdo?", "No", "Significa reconocer lo que otro siente."),
        E("¿«Además» puede unir mi idea con la de otra persona?", "Sí", "Es un conector que agrega."),
    ],
    ("Conversa con una persona de tu casa sobre el tema «cómo hacer más amigable nuestro lugar de estudio». Escucha su idea y responde tres veces: una vez con un conector como «Como dijiste…», otra vez agregando una idea nueva y otra mostrando interés con una pregunta o un comentario de empatía. Anota las tres frases que usaste y qué idea nueva aportaste.",
     "Como dijiste, un lugar ordenado ayuda. Además, podríamos tener una lámpara cerca de la mesa. ¿Cómo te sientes cuando hay mucho desorden? Entiendo que te moleste.",
     ["usa un conector", "agrega una idea nueva", "muestra interés o empatía", "mantiene el tema"], ["tres frases escritas u orales"], ["repetir lo mismo", "burlarse o minimizar lo que siente la otra persona"],
     "Si tu idea repite la del otro, cambia: suma un ejemplo o una consecuencia."),
    "Escribe dos conectores nuevos que sirvan para sumar tu idea a la de otro.",
    "Escribe un diálogo de cinco líneas donde cada persona construye sobre lo que dijo la anterior.",
)

# ================================================================ OA 25 · clase 5
reg(
    OA25, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para ensayar un desacuerdo respetuoso.",
    "Aprenderé a expresar un desacuerdo sin descalificar a nadie: decir que pienso distinto, dar mi razón y respetar a la otra persona. Sirve para resolver diferencias sin pelear.",
    ["Sé dar una opinión con una razón.", "Sé preguntar para aclarar y mostrar empatía."],
    [
        "En una conversación grupal es normal que haya opiniones distintas. Discrepar es decir que pensamos algo diferente. Eso no es una pelea. Una forma respetuosa tiene tres partes: reconocer lo que la otra persona dijo, decir en qué no estamos de acuerdo y dar nuestra razón. Por ejemplo: «Entiendo tu idea de jugar con pelota, pero yo prefiero juegos de mesa, porque así participan más personas».",
        "Descalificar es atacar a la persona en lugar de discutir la idea: decir «eso es tonto» o «tú siempre piensas mal» no aporta razones y puede lastimar. Para discrepar bien hablamos de la idea, no de la persona, y usamos frases como «No estoy de acuerdo con esa parte porque…» o «Puede que me equivoque, pero yo veo que…».",
        "También respetamos los turnos: escuchamos hasta el final antes de responder. Después de discrepar, buscamos un punto en común o una pregunta que ayude a seguir: «¿Qué te parece si probamos una semana cada opción?». Cambiar de idea con razones no es perder, es aprender.",
    ],
    [("discrepar", "decir que pensamos algo distinto"), ("descalificar", "atacar a la persona o burlarse en lugar de discutir su idea"), ("punto en común", "algo en lo que ambas personas están de acuerdo"), ("respeto", "tratar bien a otros aunque pensemos distinto"), ("razón", "motivo que explica lo que pensamos")],
    [
        ("Discrepar con razones", "Tema: ¿recreo con pelota o con juegos de mesa? Luis dice: «Juguemos a la pelota». Ema responde: «Entiendo tu idea, pero prefiero juegos de mesa, porque así participan más personas». ¿Cuál es la razón de Ema?", ["Busco lo que va después de «porque».", "Dice que participan más personas.", "Esa es su razón."], "Que así participan más personas."),
        ("Distinguir descalificar", "Mario dice: «Tu idea es tonta». ¿Mario discute la idea o ataca?", ["Veo si da una razón.", "No da razón y usa «tonta».", "Ataca la idea con burla."], "Descalifica: no da razón y se burla."),
    ],
    [("Responder a un desacuerdo diciendo «tú siempre piensas mal».", "Se habla de la persona en vez de la idea.", "Habla de la idea: «No estoy de acuerdo con esa parte porque…»."), ("Quedarse callado para evitar el desacuerdo.", "Se cree que discrepar siempre produce peleas.", "Di lo que piensas con respeto y con una razón.")],
    [
        E("¿Qué es discrepar?", "Decir que pensamos algo distinto", "No implica pelear."),
        E("¿«Eso es tonto» discute la idea con una razón o descalifica?", "Descalifica", "No da razón y se burla."),
        E("Luis dice: «Juguemos a la pelota». Ema responde: «Entiendo tu idea, pero prefiero juegos de mesa, porque así participan más personas». ¿Qué parte de la respuesta de Ema reconoce la idea de Luis?", "Entiendo tu idea", "Es la primera parte de una discrepancia respetuosa."),
    ],
    [
        E("Una forma respetuosa de discrepar reconoce la idea, dice en qué no estamos de acuerdo y da una razón. ¿Cuántas partes tiene?", "Tres", "Son reconocer, discrepar y dar la razón."),
        E("¿Por qué descalificar no ayuda a resolver un desacuerdo?", "Porque ataca a la persona y no da razones", "No se discute la idea."),
        E("Elige la frase respetuosa: a) «No estoy de acuerdo con esa parte porque tarda mucho» b) «Qué idea más mala»", "a", "La a da razón y no ataca."),
    ],
    [
        E("Pía dice: «Hagamos la fiesta en la tarde». Tú prefieres la mañana. Elige la mejor respuesta: a) «Entiendo, pero prefiero la mañana porque hay más luz» b) «Nunca eliges bien»", "a", "Reconoce la idea y da una razón."),
        E("Escribe cómo empiezas una frase para discrepar con amabilidad: «Puede que me equivoque, pero…» o «Cállate»?", "Puede que me equivoque, pero…", "Es amable y abre diálogo."),
        E("Rubén dice: «Opino distinto, porque el patio es muy ruidoso». Luis le contesta: «Tú nunca sabes nada». ¿Qué hizo Luis: a) descalificó a Rubén b) respondió a su razón?", "a", "Atacó a la persona en vez de la razón."),
    ],
    [
        E("Dos amigos discrepan sobre el color del mural. Uno quiere azul y el otro verde. Ambos quieren que el mural sea alegre. ¿Cuál es el punto en común?", "Que el mural sea alegre", "Ambos lo quieren."),
        E("Después de discrepar, ¿qué pregunta busca un acuerdo: a) «¿Qué te parece si usamos los dos colores?» b) «¿Por qué siempre quieres ganar?»", "a", "La a propone una solución compartida."),
    ],
    [
        E("Lee: Ana: «Yo prefiero reciclar en el patio». Beto: «No, eso es una pésima idea. Tú siempre piensas mal». ¿Cuántas frases de Beto descalifican?", "Dos", "«Pésima idea» y «tú siempre piensas mal» atacan sin razones."),
        E("Reescribe a Beto con respeto: elige la mejor opción: a) «No estoy de acuerdo, porque en el patio hay viento y se vuela el papel» b) «Tú nunca piensas»", "a", "La a discrepa con una razón."),
    ],
    [E("Debate del curso: ¿recreo con pelota o con juegos de mesa? Paz dice: «Entiendo que quieras pelota, pero hoy llueve». Tomás dice: «No me importa lo que digas». ¿Quién respeta el turno y la idea de la otra persona?", "Paz", "Escucha y responde con una razón.")],
    [
        E("Discrepar, ¿es lo mismo que pelear?", "No", "Se puede pensar distinto con respeto."),
        E("¿Debo hablar de la idea o de la persona al discrepar?", "De la idea", "Así no descalifico."),
        E("Después de discrepar, ¿conviene buscar un punto en común?", "Sí", "Ayuda a llegar a acuerdos."),
    ],
    ("Practica un desacuerdo respetuoso. Lee esta situación: tu curso debe elegir entre hacer la muestra de trabajos en la sala o en el patio. Una compañera, Rosa, propone el patio. Tú prefieres la sala. Escribe lo que le dirías con estas tres partes: 1) reconocer su idea, 2) decir que no estás de acuerdo con esa parte, 3) dar una razón. Luego agrega una pregunta que busque un punto en común. Puedes practicarlo en voz alta con una persona de tu casa.",
     "Entiendo tu idea de usar el patio, porque hay más espacio. No estoy de acuerdo con esa parte porque si llueve se mojan los trabajos. ¿Qué te parece si la hacemos en la sala y dejamos el patio para el recreo?",
     ["reconoce la idea de la otra persona", "dice en qué no está de acuerdo", "da una razón", "propone un punto en común"], ["texto escrito u oral con las cuatro partes"], ["descalificar a la persona", "no dar razón"],
     "Si sonó fuerte, cambia la frase por: «Puede que me equivoque, pero yo veo que…»."),
    "Escribe dos frases que descalifican y reescríbelas como desacuerdos respetuosos.",
    "Imagina un desacuerdo entre dos personajes de un cuento y escribe cómo podrían discrepar con respeto.",
)

# ================================================================ OA 25 · clase 6
reg(
    OA25, 6,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para revisar los acuerdos.",
    "Aprenderé a cerrar una conversación con acuerdos claros y a anotar las preguntas que quedaron abiertas. Sirve para que todos sepan qué se decidió y qué falta por conversar.",
    ["Sé mantener el foco, preguntar para aclarar y discrepar con respeto.", "Sé respetar turnos."],
    [
        "Una conversación grupal termina bien cuando el grupo revisa qué se decidió y qué falta. Un acuerdo es una decisión que todos entienden y aceptan, por ejemplo: «El viernes limpiaremos la sala». Un buen acuerdo dice qué se hará, quién y cuándo. Si no se sabe quién o cuándo, el acuerdo es difícil de cumplir.",
        "Una pregunta abierta es algo que quedó sin resolver y requiere más conversación, como «¿Quién traerá los materiales?». No es un fracaso: es una forma honesta de decir que aún falta decidir. Para cerrar usamos un resumen con frases como «Acordamos que…», «Quedó pendiente…» y «Las ideas principales fueron…».",
        "Cerrar bien también es agradecer los aportes y repasar cómo conversamos: ¿mantuvimos el foco?, ¿respetamos los turnos?, ¿todos pudieron hablar? Esa revisión ayuda a mejorar la próxima conversación.",
    ],
    [("acuerdo", "decisión que todos entienden y aceptan"), ("pregunta abierta", "duda que queda por resolver"), ("resumen", "repaso breve de lo más importante"), ("pendiente", "tarea o decisión que aún falta"), ("responsable", "persona que se encarga de hacer algo")],
    [
        ("Distinguir acuerdo y pregunta abierta", "Al final de una reunión, el curso dijo: «Limpiaremos la sala el viernes; Ema traerá bolsas. Falta decidir quién llevará la basura al contenedor». ¿Cuál es la pregunta abierta?", ["Busco lo que aún no está decidido.", "Dice que falta decidir quién llevará la basura.", "Eso queda abierto."], "Quién llevará la basura al contenedor."),
        ("Evaluar un acuerdo", "Acuerdo A: «Alguien limpiará algún día». Acuerdo B: «Ema limpiará la pizarra el lunes». ¿Cuál es un buen acuerdo?", ["Busco qué, quién y cuándo.", "La B dice qué (limpiar la pizarra), quién (Ema) y cuándo (el lunes).", "La A no dice quién ni cuándo."], "El B."),
    ],
    [("Terminar la conversación sin repasar qué se decidió.", "Se cree que todos recuerdan lo mismo.", "Haz un resumen: «Acordamos que… Quedó pendiente…»."), ("Anotar un acuerdo sin responsable ni fecha.", "Se piensa que no hace falta.", "Escribe qué, quién y cuándo.")],
    [
        E("En Lenguaje: ¿Qué es un acuerdo?", "Una decisión que todos entienden y aceptan", "Por eso se anota."),
        E("¿Cuáles son los tres datos de un buen acuerdo?", "Qué, quién y cuándo", "Así se puede cumplir."),
        E("«Falta decidir quién traerá los materiales». ¿Es un acuerdo o una pregunta abierta?", "Una pregunta abierta", "Aún no se resuelve."),
    ],
    [
        E("¿Para qué sirve el resumen final?", "Para recordar lo decidido y lo pendiente", "Todos revisan lo mismo."),
        E("Elige la frase de cierre: a) «Acordamos que Ema trae las bolsas el viernes» b) «Hablamos de muchas cosas»", "a", "La a dice un acuerdo concreto."),
        E("Después de cerrar, ¿conviene agradecer los aportes?", "Sí", "Reconoce el trabajo de todos."),
    ],
    [
        E("Acuerdo: «Pablo regará el huerto el martes». ¿Quién es el responsable?", "Pablo", "Es quien se encarga."),
        E("En ese acuerdo, ¿cuándo se hará la tarea?", "El martes", "Está en la frase."),
        E("Completa: «Quedó ___ decidir dónde guardar las bolsas.» Escribe la palabra.", "pendiente", "Quedó pendiente es lo que falta."),
    ],
    [
        E("Un grupo anotó: «Acordamos hacer una muestra». Faltan quién y cuándo. ¿Qué hay que agregar?", "Quién se encarga y cuándo será", "Un acuerdo claro tiene responsable y fecha."),
        E("Después de conversar, un niño dice: «Hablé yo casi todo el rato». ¿Qué revisión de la conversación hace: a) turnos b) color de la sala?", "a", "Revisa si todos hablaron."),
    ],
    [
        E("Lee la conversación: Ana: «Hagamos un diario mural». Beto: «Yo traigo los cartones el lunes». Carla: «Yo escribo los títulos». Dani: «¿Y quién cuelga el mural?». Nadie responde. ¿Cuántos acuerdos con responsable hay?", "Dos", "Beto con cartones y Carla con títulos."),
        E("En esa conversación, ¿cuál es la pregunta abierta?", "Quién cuelga el mural", "Nadie asumió esa tarea."),
    ],
    [E("Al cierre de una reunión, Rosa lee: «Acordamos que Tomás traerá pegamento el lunes. Quedó pendiente quién traerá tijeras». ¿Cuántas cosas quedaron resueltas y cuántas pendientes?", "Una resuelta y una pendiente", "Pegamento está acordado; tijeras falta.")],
    [
        E("¿Una pregunta abierta es un fracaso?", "No", "Es algo que aún se debe conversar."),
        E("¿«Acordamos que…» puede iniciar un resumen de lo decidido?", "Sí", "Dice lo decidido."),
        E("Para cerrar bien, ¿se revisa si todos pudieron hablar?", "Sí", "Ayuda a mejorar la próxima conversación."),
    ],
    ("Cierra una conversación en grupo. Lee esta conversación sobre un paseo del curso: Ema: «Podemos ir al parque». Luis: «Yo llevo el balón». Pía: «Yo llevo agua para todos». Tomás: «¿Quién avisará a las familias?». Nadie contesta. Escribe un resumen de cierre con estas partes: 1) dos acuerdos con responsable, 2) una pregunta abierta y 3) una frase para agradecer.",
     "Acordamos ir al parque; Luis llevará el balón y Pía llevará agua. Quedó pendiente quién avisará a las familias. Gracias a todos por sus ideas.",
     ["nombra dos acuerdos con responsable", "dice una pregunta abierta", "agradece los aportes"], ["resumen escrito u oral"], ["anotar acuerdos sin responsable", "olvidar lo pendiente"],
     "Si falta algo, revisa: ¿qué se acordó?, ¿quién lo hará?, ¿qué falta decidir?"),
    "Después de una conversación en casa, anota un acuerdo con responsable y una pregunta pendiente.",
    "Escribe qué harías si el grupo no llegó a ningún acuerdo y cómo lo anotarías.",
)
