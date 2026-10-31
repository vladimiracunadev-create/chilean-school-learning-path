"""Student material for 7.º básico Música, OA 07 (reconocer el rol de la música en la sociedad, las experiencias musicales propias, los contextos en que surge y las personas que la cultivan).

Todas las situaciones, encuestas y entrevistas de los ejercicios son inventadas para esta clase. Las experiencias musicales personales son privadas: cada persona decide qué comparte. Los saberes y repertorios de los pueblos originarios los enseñan las y los educadores tradicionales y las comunidades; este cuaderno no los describe.
"""
from __future__ import annotations

from student_content_mu7_a import L
from student_lessons import arith, ex

OA7 = "MU07 OA 07"
FUN = "bailar, celebrar, calmar, acompañar una actividad (marchar, trabajar, estudiar) y expresar identidad (como un himno)"

# ---------------------------------------------------------------- OA 07 · clase 1 (las funciones de la música)
L(
    OA7, 1,
    f"Lápiz y papel. Funciones de la clase: {FUN}. Todas las situaciones están escritas en los ejercicios. Tu registro de música personal es privado: tú decides si lo compartes.",
    "Aprenderé a reconocer para qué sirve la música en la vida de las personas (sus funciones) y a relacionarlo con mis propias experiencias. Sirve para entender por qué la música está presente en tantos momentos de la sociedad.",
    ["Sé que la música se escucha, se interpreta y se crea.", "Sé que hay músicas para distintos momentos.", "Sé contar y comparar números pequeños."],
    [
        f"La música cumple funciones en la sociedad, es decir, sirve para algo. En esta clase trabajamos cinco: {FUN}. Una canción de cuna sirve para calmar y hacer dormir. La cueca, la danza nacional de Chile, sirve para bailar y celebrar en fiestas como las de septiembre. Una marcha acompaña el paso de una banda en un desfile. Un himno, como el Himno Nacional de Chile que se canta en actos cívicos, expresa la identidad de un grupo.",
        "Una misma música puede cumplir más de una función. Una cueca puede ser para bailar y para celebrar a la vez. También cambia según el momento: una canción tranquila calma al llegar a casa, y la misma canción puede acompañar un estudio. Para reconocer la función se pregunta «¿para qué se usa esta música en esta situación?». La respuesta depende de la situación, no solo de la música.",
        "Las experiencias personales también cuentan. Cada persona usa la música de maneras distintas: para relajarse, para darse ánimo, para recordar a alguien o para compartir con amigos. Hacer un registro de cuánto tiempo y para qué escuchamos música ayuda a descubrirlo. Ese registro es privado, y comparar no significa juzgar: las funciones que cumple la música para cada persona son válidas. Lo que importa es entender el rol que tiene en la vida.",
    ],
    [("función", "para qué sirve la música en una situación"), ("celebrar", "festejar un acontecimiento con otras personas"), ("identidad", "lo que une y caracteriza a un grupo de personas"), ("himno", "canción que representa a un país o a un grupo"), ("registro personal", "lista privada de cuándo y para qué escucho música")],
    [
        ("Reconocer la función", "En un desfile escolar, una banda toca una marcha para que el curso avance al mismo paso. ¿Qué función cumple la música?", ["Se usa durante una actividad: marchar.", "Marca el paso de las personas."], "Acompañar una actividad"),
        ("Sumar el registro", "Un registro semanal dice: 40 minutos para calmarme, 25 para bailar y 55 para acompañar el estudio. ¿Cuántos minutos de música son en total?", ["Se suman los tres tiempos.", "40 + 25 + 55 = 120."], "120 minutos"),
    ],
    [
        ("Pensar que la música solo sirve para entretener.", "También calma, acompaña tareas, celebra y expresa identidad.", "Pregunta «¿para qué se usa aquí?»."),
        ("Creer que una canción tiene una sola función para siempre.", "La función depende de la situación y puede cambiar.", "Revisa en qué momento y con quién se usa."),
    ],
    [
        ex("Una canción de cuna se canta para que un bebé se duerma. ¿Qué función cumple?", "Calmar", "Busca que el bebé se tranquilice y duerma."),
        ex("Una pareja baila cueca en una fiesta. ¿Qué función cumple la música?", "Bailar", "La música acompaña el baile."),
        ex("Un himno que se canta en un acto cívico, ¿qué función cumple: expresar identidad o calmar?", "Expresar identidad", "Representa a un país o grupo."),
    ],
    [
        ex("Un grupo de personas canta para remar al mismo ritmo. ¿Qué función cumple la música: acompañar una actividad o bailar?", "Acompañar una actividad", "Ayuda a coordinar el trabajo."),
        ex("¿Puede una misma música cumplir dos funciones? Responde sí o no.", "Sí", "Una cueca puede servir para bailar y para celebrar."),
        ex("Una persona escucha música suave mientras estudia para concentrarse. ¿Qué función cumple: acompañar una actividad o expresar identidad?", "Acompañar una actividad", "La música acompaña la tarea de estudiar."),
    ],
    [
        ex("Situaciones: 1) cueca en una fiesta, 2) canción de cuna, 3) Himno Nacional en un acto, 4) cumbia en un matrimonio, 5) marcha en un desfile. ¿Cuántas son para bailar?", "2", "La 1 y la 4 se usan para bailar."),
        ex("Un registro semanal dice: calmarme 35 minutos, bailar 20, acompañar el estudio 50 y cantar el himno del equipo 25. ¿Para qué función se usó más tiempo la música?", "Acompañar una actividad (el estudio)", "50 es el tiempo mayor."),
        arith("Una persona escucha música 20 minutos en la mañana, 45 en la tarde y 30 en la noche. ¿Cuántos minutos son en el día?", "20+45+30", "Se suman los tres tiempos.", " minutos"),
    ],
    [
        ex("Pedro dice que la música solo sirve para entretener. ¿Qué función de la clase muestra que sirve para algo más: calmar a un bebé con una canción de cuna o pasar el rato?", "Calmar a un bebé con una canción de cuna", "Sirve para calmar, no solo para entretener."),
        ex("Una canción tranquila calma a una persona al llegar a casa y acompaña el estudio de otra. ¿La función depende solo de la música? Responde sí o no.", "No", "Depende también de la situación en que se usa."),
    ],
    [
        ex("Un equipo de barrio canta su propia canción antes de cada partido, y todos se sienten parte del mismo grupo. ¿Qué función cumple principalmente esa canción?", "Expresar identidad", "Representa y une al grupo."),
        arith("Un curso de 24 estudiantes se reparte en 4 grupos iguales para armar un registro de funciones. ¿Cuántos estudiantes hay por grupo?", "24//4", "Se reparten en partes iguales.", " estudiantes"),
    ],
    [ex("En una feria de barrio un domingo, una familia baila cumbia y se ríe. ¿Qué dos funciones cumple la música: bailar y celebrar o calmar y marchar?", "Bailar y celebrar", "Acompaña el baile y la fiesta.")],
    [ex("Entre las cinco funciones de la clase, ¿cuál cumple una canción de cuna?", "Calmar", "Ayuda a dormir."), ex("¿Qué se pregunta para reconocer una función?", "¿Para qué se usa la música en esta situación?", "Es la pregunta de la clase."), ex("¿El registro de mi música es privado o público?", "Privado", "Cada persona decide si lo comparte.")],
    (
        "Completa una tabla con estas seis situaciones inventadas: a) una canción de cuna, b) una cueca en una fiesta, c) una marcha de banda, d) un himno en un acto, e) música suave mientras estudio, f) una cumbia en un matrimonio. Para cada una escribe la función (de las cinco de la clase) y, si quieres, escribe también una situación de tu vida y para qué usas tú la música en ella (esta parte es privada).",
        "a) calmar; b) bailar y celebrar; c) acompañar una actividad; d) expresar identidad; e) acompañar una actividad; f) bailar y celebrar. Mi situación: escucho música tranquila al llegar a casa para relajarme, función de calmar.",
        ["asigna una función a cada situación", "justifica con «para qué»", "reconoce que una música puede tener más de una función"],
        ["tabla de seis situaciones", "frase de situación propia opcional"],
        ["pensar que solo hay una función por canción", "no relacionar la función con la situación"],
        "Reconoce la tabla y pide explicar, en una frase, por qué eligió esa función para cada situación.",
    ),
    "Escribe tres situaciones en que hayas escuchado música esta semana y para qué.",
    "Haz un registro de un día de tu música y clasifica los minutos por función.",
)

# ---------------------------------------------------------------- OA 07 · clase 2 (los contextos en que surge la música)
L(
    OA7, 2,
    "Lápiz y papel. Todas las tarjetas de contexto están escritas en los ejercicios. Cuatro preguntas para describir un contexto: ¿quién la hace?, ¿dónde?, ¿cuándo? y ¿para qué?",
    "Aprenderé a describir el contexto de una música con cuatro preguntas (quién, dónde, cuándo y para qué). Sirve para entender por qué una música suena como suena y cómo cambia según el lugar y la ocasión.",
    ["Sé que la música cumple funciones.", "Sé distinguir lugares públicos y privados.", "Sé sumar y multiplicar números pequeños."],
    [
        "El contexto de una música es el conjunto de circunstancias en que surge y se usa. Se describe con cuatro preguntas. ¿Quién la hace? Una banda escolar, un coro, una familia, una persona sola. ¿Dónde? En un dormitorio, una plaza, una sala de concierto, una radio. ¿Cuándo? En un cumpleaños, en las fiestas de septiembre, un domingo de feria. ¿Para qué? Para bailar, calmar, celebrar, acompañar o expresar identidad.",
        "El contexto influye en cómo es la música. En una sala de concierto, el público suele escuchar en silencio. En una fiesta, el público baila y canta. La música de una canción de cuna se canta bajito en un lugar privado. Un desfile ocurre en un espacio público y la música suena fuerte para que se oiga. Un mismo tipo de música puede cambiar de carácter según el contexto en que se use.",
        "En Chile hay muchos contextos y muchas músicas: fiestas familiares, escuelas, plazas, radios, teatros y comunidades. Los pueblos originarios tienen músicas propias, que se cuidan y se enseñan en sus comunidades, por lo que su forma tradicional la enseñan las y los educadores tradicionales. Describir un contexto con las cuatro preguntas nos ayuda a respetar y entender cada música en su propio lugar, sin compararla con otras como si una fuera mejor.",
    ],
    [("contexto", "circunstancias en que surge y se usa una música"), ("espacio público", "lugar abierto a todas las personas, como una plaza"), ("espacio privado", "lugar reservado, como una casa"), ("ocasión", "momento o fecha en que se usa la música"), ("las cuatro preguntas", "quién, dónde, cuándo y para qué")],
    [
        ("Describir con las cuatro preguntas", "Tarjeta: «Una banda escolar toca una marcha en el desfile de las fiestas de septiembre, en la calle del colegio, para que el curso avance al mismo paso.» ¿Quién la hace?", ["Se busca quién toca.", "Es una banda escolar."], "Una banda escolar"),
        ("Contar tiempo de música", "En una feria hay 5 grupos que tocan 20 minutos cada uno. ¿Cuántos minutos de música hay?", ["Son 5 grupos de 20 minutos.", "5 × 20 = 100."], "100 minutos"),
    ],
    [
        ("Describir una música solo por su nombre.", "Sin el contexto no se entiende por qué existe ni cómo se usa.", "Responde quién, dónde, cuándo y para qué."),
        ("Pensar que una música es mejor que otra por el lugar donde suena.", "Cada música cumple su función en su contexto; no se comparan como si hubiera una mejor.", "Descríbela en su propio contexto."),
    ],
    [
        ex("¿Cuáles son las cuatro preguntas para describir un contexto?", "Quién, dónde, cuándo y para qué", "Son las cuatro de la clase."),
        ex("En una sala de concierto, ¿el público suele escuchar en silencio o bailar?", "Escuchar en silencio", "Es una costumbre de ese contexto."),
        ex("Una canción de cuna que se canta en la casa, ¿está en un espacio público o privado?", "Privado", "Una casa es un espacio reservado."),
    ],
    [
        ex("Tarjeta: «Un grupo toca en la plaza del barrio un domingo de feria para que las personas bailen.» ¿Cuándo ocurre?", "Un domingo de feria", "Es el momento que indica la tarjeta."),
        ex("En esa misma tarjeta (plaza del barrio, domingo de feria, para bailar), ¿es un espacio público o privado?", "Público", "Una plaza está abierta a todas las personas."),
        ex("Una misma canción se toca en una sala de concierto y en una fiesta. ¿Qué cambia: el contexto o la canción?", "El contexto", "Cambian el lugar, la ocasión y el comportamiento del público."),
    ],
    [
        arith("Una radio escolar emite 3 canciones por programa y 4 programas por semana. ¿Cuántas canciones emite en la semana?", "3*4", "Se multiplican las canciones por los programas.", " canciones"),
        ex("A) Concierto en un teatro; B) fiesta en una plaza. ¿En cuál contexto es más probable que el público baile?", "B", "Una fiesta en una plaza invita a bailar."),
        ex("Una música para dormir a un bebé, ¿se toca mejor suave o fuerte?", "Suave", "Su función es calmar."),
    ],
    [
        ex("Marta dice que una música siempre suena igual, sin importar el contexto. ¿Tiene razón? Responde sí o no.", "No", "El contexto cambia cómo se toca y cómo se recibe."),
        ex("Se toca una canción de cuna muy fuerte en una fiesta de 100 personas. ¿Calza con su contexto de origen? Responde sí o no.", "No", "Una canción de cuna es suave y privada, no festiva."),
    ],
    [
        ex("Seis contextos: 1) canción de cuna en un dormitorio, 2) desfile en la calle, 3) concierto en un teatro, 4) programa de radio que escucha todo el barrio, 5) ensayo en la casa, 6) coro que canta en la plaza del pueblo. ¿Cuántos son espacios públicos?", "4", "Son el 2, el 3, el 4 y el 6; el 1 y el 5 son privados."),
        arith("Un festival escolar tiene 6 grupos que tocan 15 minutos cada uno y pausas de 5 minutos entre grupo y grupo (hay 5 pausas). ¿Cuántos minutos dura el festival?", "6*15+5*5", "Se suman los minutos de música y los de pausas.", " minutos"),
    ],
    [ex("En un cumpleaños, una familia canta una canción para festejar. Usando las cuatro preguntas, ¿qué responde la pregunta «para qué»: celebrar o marchar?", "Celebrar", "Se canta para festejar al cumpleañero.")],
    [ex("¿Qué pregunta de contexto averigua el lugar?", "¿Dónde?", "Describe el espacio donde suena la música."), ex("¿Una plaza es un espacio público o privado?", "Público", "Está abierta a todas las personas."), ex("¿Quién enseña la forma tradicional de las músicas de los pueblos originarios?", "Las y los educadores tradicionales y las comunidades", "Esos saberes se cuidan en sus comunidades.")],
    (
        "Describe el contexto de una de estas tarjetas inventadas con las cuatro preguntas: A) un coro canta en la plaza del pueblo, en una fiesta de aniversario, para recibir a los visitantes; B) una familia canta cumpleaños feliz en casa; C) una radio de barrio pone música alegre en la mañana. Escribe quién, dónde, cuándo y para qué, y si es un espacio público o privado. Después, si quieres, describe un contexto musical de tu vida, de forma breve y sin nombres de personas.",
        "A) Quién: un coro; dónde: la plaza del pueblo; cuándo: una fiesta de aniversario; para qué: dar la bienvenida y celebrar; espacio público. B) Quién: una familia; dónde: en la casa; cuándo: un cumpleaños; para qué: celebrar; espacio privado. C) Quién: una radio de barrio; dónde: en el aire y en las casas; cuándo: la mañana; para qué: acompañar el día; público.",
        ["responde las cuatro preguntas", "distingue espacio público y privado", "no compara una música como mejor que otra"],
        ["descripción de una tarjeta", "contexto propio opcional"],
        ["describir solo el nombre de la música", "dejar sin responder alguna de las cuatro preguntas"],
        "Reconoce la descripción y pide completar la pregunta que quedó sin responder.",
    ),
    "Describe con las cuatro preguntas una música que escuchaste esta semana.",
    "Compara dos contextos distintos de una misma canción y explica qué cambia.",
)

# ---------------------------------------------------------------- OA 07 · clase 3 (las personas que cultivan la música)
L(
    OA7, 3,
    "Lápiz y papel. Los roles y los casos están escritos en los ejercicios. La entrevista de la actividad es opcional y solo con una persona adulta de confianza que quiera participar; no se escriben datos personales.",
    "Aprenderé a reconocer las personas y los oficios que cultivan la música (compositores, intérpretes, directores, lutieres, docentes, ingenieras de sonido y otros) y lo que aporta cada una. Sirve para valorar que la música es un trabajo de muchas personas.",
    ["Sé que la música surge en contextos.", "Sé que hay funciones de la música.", "Sé sumar y dividir números pequeños."],
    [
        "Cultivar la música es cuidarla, crearla y compartirla. Muchas personas lo hacen, cada una con un rol. La compositora o el compositor crea música nueva. La intérprete o el intérprete la canta o la toca. La directora o el director guía a un coro o a una orquesta. La lutier o el lutier fabrica y repara instrumentos. La docente o el docente enseña música. La ingeniera o el ingeniero de sonido cuida los micrófonos y el volumen. La gestora o el gestor cultural organiza conciertos y festivales.",
        "Una misma persona puede cumplir más de un rol. Violeta Parra, por ejemplo, fue una cantautora chilena: compuso canciones y las interpretó, y además recopiló canciones tradicionales. Claudio Arrau fue un pianista chileno reconocido en el mundo: su rol principal fue el de intérprete. Beethoven fue un compositor alemán. También existen cantoras y cantores populares, músicos de barrio, integrantes de coros y bandas escolares, que cultivan la música sin ser famosos.",
        "Todas estas personas hacen posible que la música llegue a la sociedad. Algunas trabajan en la música y otras la cultivan por gusto o por tradición familiar o comunitaria. Reconocer sus roles ayuda a valorar su trabajo y a descubrir cómo podemos participar nosotros: cantando en un coro, ayudando a organizar un acto o aprendiendo de una persona mayor que sabe canciones de su comunidad. Entrevistar a alguien que cultive la música, con su permiso, es una buena forma de aprender.",
    ],
    [("compositor/a", "persona que crea música nueva"), ("intérprete", "persona que canta o toca música"), ("director/a", "persona que guía a un coro o una orquesta"), ("lutier", "persona que fabrica y repara instrumentos"), ("gestor/a cultural", "persona que organiza conciertos y actividades culturales")],
    [
        ("Reconocer el rol", "Una persona regula los micrófonos y el volumen en un concierto. ¿Qué rol cumple?", ["Cuida el sonido de los equipos.", "Es la ingeniera o el ingeniero de sonido."], "Ingeniero o ingeniera de sonido"),
        ("Contar personas", "Un festival necesita 1 gestora, 2 ingenieros de sonido y 8 intérpretes. ¿Cuántas personas son?", ["Se suman los tres grupos.", "1 + 2 + 8 = 11."], "11 personas"),
    ],
    [
        ("Pensar que solo las personas famosas cultivan la música.", "También lo hacen cantoras de barrio, coros, docentes y bandas escolares.", "Busca a quienes hacen música en tu comunidad."),
        ("Creer que cada persona puede tener un solo rol.", "Una cantautora compone y también interpreta.", "Reconoce los roles según lo que la persona hace."),
    ],
    [
        ex("La persona que crea música nueva, ¿se llama compositor o intérprete?", "Compositor o compositora", "Compone obras nuevas."),
        ex("La persona que fabrica y repara instrumentos, ¿se llama lutier o director?", "Lutier", "Es su oficio."),
        ex("La persona que guía a un coro, ¿es director/a o gestor/a cultural?", "Director o directora", "Guía a las voces del coro."),
    ],
    [
        ex("Una persona organiza los permisos y el calendario de un festival de música. ¿Qué rol cumple?", "Gestor o gestora cultural", "Organiza actividades culturales."),
        ex("Una profesora enseña a cantar a un curso. ¿Qué rol cumple: docente de música o lutier?", "Docente de música", "Su trabajo es enseñar música a otras personas."),
        ex("Una estudiante canta en un acto escolar una canción que compuso otra persona. ¿Qué rol cumple al cantarla: compositora o intérprete?", "Intérprete", "Canta una música que creó otra persona."),
    ],
    [
        ex("En una banda de 5 personas, 2 componen y cantan, 1 solo toca, 1 solo compone y 1 solo produce el sonido. ¿Cuántas personas son intérpretes?", "3", "Las 2 que cantan y la que toca."),
        ex("En esa misma banda (2 componen y cantan, 1 solo toca, 1 solo compone, 1 solo produce el sonido), ¿cuántas personas son compositoras?", "3", "Las 2 que componen y cantan más la que solo compone."),
        arith("Cada ingeniero de sonido cuida 4 micrófonos. Un festival tiene 8 micrófonos. ¿Cuántos ingenieros hacen falta?", "8//4", "Se reparten los micrófonos en grupos de 4.", " ingenieros"),
    ],
    [
        ex("Violeta Parra compuso canciones, las interpretó y recopiló canciones tradicionales. ¿Cuántos roles de la clase cumplió: 1 o más de uno?", "Más de uno", "Fue compositora e intérprete, y recopiladora."),
        ex("Luis dice que solo las personas famosas cultivan la música. ¿Tiene razón? Responde sí o no.", "No", "También lo hacen coros, docentes y músicos de barrio."),
    ],
    [
        arith("Una orquesta escolar tiene 24 estudiantes divididos en 4 grupos iguales por familia de instrumentos y 1 directora para todas. ¿Cuántas personas hay en total, contando a la directora?", "24+1", "Se suman las y los estudiantes y la directora.", " personas"),
        ex("En la orquesta anterior hay 24 estudiantes en 4 grupos iguales. ¿Cuántos estudiantes tiene cada grupo?", "6", "24 ÷ 4 = 6.", "24//4"),
    ],
    [ex("Una vecina dirige el coro de la junta de vecinos y ensaya los jueves. ¿Qué rol cumple?", "Directora de coro", "Guía las voces del coro.")],
    [ex("¿Quién crea música nueva?", "El compositor o la compositora", "Es su rol."), ex("¿Qué hace un lutier?", "Fabrica y repara instrumentos", "Es su oficio."), ex("¿Se necesita permiso para entrevistar a una persona que cultiva la música?", "Sí", "Siempre se pide permiso y se respeta lo que quiere compartir.")],
    (
        "Lee esta entrevista inventada a don Mario, lutier de guitarras: «¿Qué hace? Fabrico y reparo guitarras. ¿Por qué lo hace? Me gusta que las personas puedan tocar instrumentos que suenen bien. ¿Quiénes usan sus guitarras? Cantoras, un coro escolar y una banda de barrio.» Responde: qué rol cumple don Mario, a qué personas ayuda y por qué su trabajo es importante para la música. Si quieres, prepara 3 preguntas para una persona adulta de confianza que cultive la música (sin pedir datos personales).",
        "Don Mario es lutier: fabrica y repara instrumentos. Ayuda a cantoras, a un coro escolar y a una banda de barrio. Su trabajo es importante porque sin instrumentos que suenen bien, esas personas no podrían tocar. Preguntas: ¿Cómo empezó a tocar? ¿Qué música le gusta compartir? ¿Qué le gustaría que otras personas aprendieran?",
        ["identifica el rol correctamente", "nombra a las personas que se benefician", "explica la importancia del trabajo"],
        ["respuesta escrita", "tres preguntas opcionales"],
        ["pensar que solo hay un rol por persona", "pedir datos personales en la entrevista"],
        "Reconoce el rol y pide explicar qué pasaría con el coro si no hubiera quien repare las guitarras.",
    ),
    "Nombra a tres personas de tu comunidad que cultiven la música y qué rol cumplen, sin dar datos personales.",
    "Prepara cinco preguntas para entrevistar, con permiso, a una persona que haga música en su comunidad.",
)

# ---------------------------------------------------------------- OA 07 · clase 4 (mi experiencia musical y su lugar en la sociedad)
L(
    OA7, 4,
    "Lápiz y papel. La encuesta del curso y los casos están escritos en los ejercicios; son inventados. Tu mapa musical es privado y puedes elegir qué parte compartir.",
    "Aprenderé a presentar mi experiencia musical con tres partes (qué música, en qué contexto y para qué, y qué personas la cultivan) y a leer datos de una encuesta con cuidado. Sirve para explicar el rol de la música en mi vida y respetar las distintas experiencias de otras personas.",
    ["Sé reconocer funciones, contextos y roles de la música.", "Sé sumar y comparar números.", "Sé escuchar a otras personas con respeto."],
    [
        "Para explicar el rol de la música en nuestra vida podemos armar un mapa musical con tres partes. La primera es la música: qué escucho o qué hago. La segunda es el contexto y la función: en qué lugar y momento, y para qué la uso. La tercera son las personas: quiénes la cultivan, como un cantante, una docente, una banda o alguien de mi familia o comunidad. Con esas tres partes se comunica una experiencia de manera clara y respetuosa.",
        "Las experiencias de las personas son distintas, y esa diversidad es valiosa. Si una compañera prefiere otra música, se le pregunta por qué le gusta y se escucha su respuesta, sin decir que está equivocada. Una encuesta permite ver cómo se reparten las respuestas en un grupo. Por ejemplo, si de 30 estudiantes 12 escuchan música para bailar, 10 para relajarse y 8 para acompañar tareas, bailar es lo más frecuente, pero no es la mayoría, porque la mayoría necesita más de 15.",
        "Al presentar conclusiones hay que cuidar lo que se afirma con los datos. «La mayoría» significa más de la mitad. «La más frecuente» significa la que tiene el número mayor, aunque no llegue a la mitad. También hay que pedir permiso antes de usar las respuestas de otras personas y no mostrar datos personales. Compartir nuestro mapa musical es voluntario, y cada persona decide qué parte quiere mostrar.",
    ],
    [("mapa musical", "descripción de mi música con tres partes: música, contexto y función, y personas"), ("encuesta", "preguntas hechas a un grupo para ver cómo se reparten las respuestas"), ("más frecuente", "la respuesta con el número mayor"), ("mayoría", "más de la mitad del total"), ("diversidad", "que las personas tengan experiencias distintas")],
    [
        ("Leer una encuesta", "En un curso de 20 estudiantes, 9 escuchan música para bailar, 7 para relajarse y 4 para acompañar tareas. ¿Qué función es la más frecuente?", ["Comparo los tres números.", "El mayor es 9, de bailar."], "Bailar"),
        ("Distinguir mayoría", "En esa encuesta de 20 estudiantes, ¿es correcto decir que la mayoría escucha música para bailar?", ["La mayoría es más de la mitad de 20, o sea más de 10.", "9 no supera 10."], "No, 9 de 20 no es más de la mitad"),
    ],
    [
        ("Decir «la mayoría» cuando solo es el grupo más grande.", "La mayoría exige más de la mitad del total.", "Compara el número con la mitad del total."),
        ("Decir a un compañero que su música está equivocada.", "Las experiencias son distintas y todas son válidas.", "Pregunta por qué le gusta y escucha su respuesta."),
    ],
    [
        ex("¿Cuántas partes tiene el mapa musical de la clase?", "3", "Son la música, el contexto con su función y las personas."),
        ex("Un compañero prefiere otra música que tú. ¿Qué haces: preguntarle por qué la elige o decirle que está mal?", "Preguntarle por qué la elige", "Así se valora la diversidad."),
        ex("¿Todas las personas escuchan la misma música? Responde sí o no.", "No", "Las experiencias musicales son distintas."),
    ],
    [
        arith("Una encuesta tuvo 12 respuestas para bailar, 10 para relajarse y 8 para acompañar tareas. ¿Cuántos estudiantes respondieron en total?", "12+10+8", "Se suman las respuestas de cada función.", " estudiantes"),
        arith("En una encuesta de 30 estudiantes, 12 eligieron bailar y 10 eligieron relajarse. ¿Cuántos estudiantes más eligieron bailar que relajarse?", "12-10", "Se resta el menor al mayor.", " estudiantes"),
        ex("¿Qué falta en la frase «Escucho cumbia en las fiestas»: la música, el contexto o las personas que la cultivan?", "Las personas que la cultivan", "Tiene la música (cumbia) y el contexto (las fiestas)."),
    ],
    [
        arith("En otra encuesta, 8 estudiantes eligen acompañar tareas y 6 más cambian de opinión y eligen lo mismo. ¿Cuántos eligen acompañar tareas ahora?", "8+6", "Se suman las personas que cambian de opinión.", " estudiantes"),
        ex("Con esos 14 que eligen acompañar tareas (y 12 que eligen bailar y 4 que eligen relajarse), ¿qué función pasa a ser la más frecuente?", "Acompañar tareas", "14 es el número mayor de los tres."),
        ex("En el curso A, 12 de 30 estudiantes bailan; en el curso B, 10 de 20. ¿En qué curso bailar es una parte mayor del grupo?", "En el curso B", "10 de 20 es la mitad, y 12 de 30 es menos de la mitad (15)."),
    ],
    [
        ex("Pedro afirma que «la mayoría escucha para bailar» porque 12 es el número más alto de una encuesta de 30. ¿Qué error cometió?", "Confundió «más frecuente» con «mayoría»", "La mayoría requiere más de 15 y 12 no lo supera."),
        ex("Quieres usar en tu presentación la respuesta de una compañera de la encuesta. ¿Qué haces primero: pedirle permiso o usarla sin avisar?", "Pedirle permiso", "Cada persona decide qué comparte."),
    ],
    [
        ex("En un curso de 30 estudiantes, ¿cuál es la menor cantidad de estudiantes para que bailar sea la mayoría?", "16", "La mitad es 15 y la mayoría es más de la mitad."),
        arith("En la encuesta (12 para bailar, 10 para relajarse y 8 para acompañar tareas), 2 de quienes eligieron bailar cambian de opinión y pasan a relajarse. ¿Cuántos eligen ahora relajarse?", "10+2", "Se suman los que cambiaron.", " estudiantes"),
    ],
    [ex("Mi mapa musical dice: «Música: cumbia. Contexto y función: fiestas de familia, para bailar y celebrar. Personas: un grupo de barrio que la toca.» ¿Cuántas partes tiene completas?", "3", "Tiene la música, el contexto con su función y las personas.")],
    [ex("¿Qué significa «la mayoría»?", "Más de la mitad", "Es más de la mitad del total."), ex("¿Qué se pide antes de usar la respuesta de otra persona?", "Permiso", "Compartir es voluntario."), ex("¿Qué función tiene mi música si la uso para relajarme al llegar a casa?", "Calmar", "Esa función ayuda a tranquilizarse.")],
    (
        "Arma tu mapa musical con tres partes: 1) una música que escuchas o haces; 2) el contexto (quién, dónde, cuándo) y la función (para qué la usas); 3) las personas o grupos que la cultivan. Escribe tres o cuatro oraciones en total. Si prefieres no compartirlo, guárdalo para ti. Para practicar puedes usar el ejemplo inventado: «cumbia, que se escucha en las fiestas de familia para bailar y celebrar, y que un grupo de barrio toca».",
        "Música: cumbia. Contexto: en las fiestas de familia, de noche, con personas que bailan; función: bailar y celebrar. Personas: un grupo de barrio que la toca y quienes organizan la fiesta. Esta música me importa porque reúne a la familia.",
        ["incluye las tres partes", "describe contexto y función con precisión", "respeta la diversidad y la privacidad"],
        ["mapa musical escrito", "frase de cierre"],
        ["describir solo el nombre de la música", "decir que una música es mejor que otra"],
        "Reconoce el mapa y pide agregar la parte que falta, si no están las tres.",
    ),
    "Escribe una frase que describa, con las tres partes, una música de tu vida.",
    "Inventa una encuesta de 5 preguntas sobre música para tu curso, pidiendo permiso y sin datos personales.",
)
