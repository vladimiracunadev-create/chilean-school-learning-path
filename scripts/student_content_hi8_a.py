"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (Humanismo y Renacimiento)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 01"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (fechas redondeadas; las épocas son convenciones de los historiadores). "
     "Edad Media: se suele ubicar entre los siglos V y XV; una fecha de cierre usada por convención es 1453, año de la caída de Constantinopla. "
     "Humanismo: movimiento intelectual que estudia los textos de Grecia y Roma y pone atención en el ser humano; su precursor es Petrarca (1304-1374). "
     "Renacimiento: movimiento cultural y artístico que nace en ciudades italianas como Florencia en los siglos XIV y XV y se extiende por Europa en el siglo XVI. "
     "Personas: Leonardo da Vinci (1452-1519), Miguel Ángel (1475-1564). "
     "Imprenta de tipos móviles de Gutenberg: hacia 1450. Primer viaje de Colón a América: 1492.")
build(
    OA, 1, F,
    use="Aprenderé a situar el Humanismo y el Renacimiento en el tiempo y en el espacio, y a plantear la pregunta que guía este tema: ¿cómo cambió la manera de mirar al ser humano?",
    prior=["Sé leer líneas de tiempo y calcular diferencias entre años.", "Sé que los siglos se cuentan en números romanos.", "Conozco la Edad Media europea como época anterior."],
    explain=[
        "El Humanismo y el Renacimiento son dos procesos que van juntos, pero no son lo mismo. El Humanismo es un movimiento de ideas: sus estudiosos leían de nuevo a autores de Grecia y Roma y defendían que el ser humano merece atención por sí mismo, por su inteligencia y su capacidad de conocer y transformar el mundo. Leonardo da Vinci estudió el cuerpo humano, diseñó máquinas y pintó; Miguel Ángel esculpió el David y pintó la bóveda de la Capilla Sixtina. El Renacimiento es el movimiento cultural y artístico en que esas ideas se ven en pinturas, edificios y libros.",
        "Para situarlos hay que usar el tiempo y el espacio. El siglo XV son los años 1401 a 1500, y el siglo XVI, los años 1501 a 1600. Ambos procesos nacen en ciudades italianas como Florencia, gracias al comercio y a familias ricas que pagaban obras, y luego se extienden a otras regiones de Europa durante el siglo XVI.",
        "Un error frecuente es pensar que todo cambió de golpe, como si Europa «despertara» en un año exacto. Las épocas son divisiones que ponen los historiadores para ordenar el pasado. Ideas humanistas ya existían en el siglo XIV, en plena Edad Media, y muchas costumbres medievales continuaron. Por eso la pregunta histórica no es «¿cuándo empezó?», sino «¿qué cambió, dónde y por qué?».",
    ],
    vocab=[("Humanismo", "movimiento de ideas que estudia a los autores clásicos y valora al ser humano"), ("Renacimiento", "movimiento cultural y artístico europeo de los siglos XIV al XVI"), ("precursor", "persona que inicia una idea antes de que se haga común"), ("siglo", "periodo de cien años; el XV va de 1401 a 1500"), ("convención", "acuerdo que se usa para ordenar, aunque no sea una fecha exacta")],
    worked=[
        ("Calcular la duración de una vida", "Según la ficha, Petrarca vivió entre 1304 y 1374. ¿Cuántos años vivió?", ["Busco los dos años: 1304 y 1374.", "Resto: 1374 − 1304 = 70."], "70 años"),
        ("Ubicar un año en su siglo", "¿A qué siglo pertenece 1453, año usado como cierre de la Edad Media?", ["Recuerdo que el siglo XV va de 1401 a 1500.", "El 1453 está entre esos años."], "Siglo XV"),
    ],
    mistakes=[("Afirmar que el Renacimiento empezó un año exacto en toda Europa.", "Se confunde una fecha de convención con un cambio que ocurrió de golpe.", "Escribe «en los siglos XIV y XV, en Italia» y explica que luego se extendió."),
              ("Usar «Humanismo» y «Renacimiento» como si fueran la misma palabra.", "No se distingue el movimiento de ideas del movimiento artístico.", "Di que el Humanismo son las ideas y el Renacimiento es su expresión cultural y artística.")],
    T=[
        ("{F} ¿En qué región actual de Europa nace el Renacimiento?", "En Italia", "La ficha menciona ciudades italianas como Florencia."),
        ("{F} ¿Cómo se llama el movimiento de ideas que estudia los textos de Grecia y Roma y valora al ser humano?", "Humanismo", "La ficha lo define con esas dos características."),
        ("=", "{F} ¿Cuántos años vivió Leonardo da Vinci?", "1519-1452", "Se resta el año de nacimiento al de muerte.", " años"),
        ("=", "{F} ¿Cuántos años antes del primer viaje de Colón nació Miguel Ángel?", "1492-1475", "Se restan el año de nacimiento y el del viaje.", " años"),
        ("{F} ¿A qué siglo pertenece el año 1492?", "Siglo XV", "El siglo XV va de 1401 a 1500."),
        ("=", "{F} Entre el nacimiento de Petrarca y el de Leonardo da Vinci, ¿cuántos años pasaron?", "1452-1304", "Se restan los dos años de nacimiento de la ficha.", " años"),
        ("{F} Ordena del más antiguo al más reciente: primer viaje de Colón, nacimiento de Petrarca, nacimiento de Miguel Ángel, caída de Constantinopla.", "Nacimiento de Petrarca, caída de Constantinopla, nacimiento de Miguel Ángel, primer viaje de Colón", "Los años son 1304, 1453, 1475 y 1492 en ese orden."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 50 años y va del año 1300 al 1500. ¿Cuántos centímetros mide?", "(1500-1300)//50", "Se divide el tramo de 200 años por lo que vale cada centímetro.", " cm"),
        ("{F} ¿Qué afirmación es correcta? A) El Renacimiento empezó de golpe en todo el continente el año 1453. B) El Renacimiento fue un proceso gradual que nació en Italia y luego se extendió.", "B) El Renacimiento fue un proceso gradual que nació en Italia y luego se extendió.", "La ficha habla de siglos y de una extensión posterior, no de un año exacto."),
        ("Un compañero dice: «Antes del Renacimiento nadie en Europa estudiaba a los autores clásicos». Corrígelo con un dato de la ficha.", "Petrarca, precursor del Humanismo, nació en 1304, en plena Edad Media, y ya estudiaba textos de Grecia y Roma", "Hay ideas humanistas dentro de la Edad Media, así que el cambio fue gradual."),
        ("¿Por qué conviene decir «hacia 1450» y no «el 1450» para la imprenta de Gutenberg?", "Porque es una fecha aproximada que los historiadores estiman", "Las fechas antiguas se redondean cuando no hay un registro exacto."),
        ("Un cuadro no tiene firma, fecha ni lugar. ¿Qué dos datos necesitas conocer para situarlo en el tiempo y el espacio?", "Cuándo se pintó y dónde se pintó", "Situar es ubicar una obra en un tiempo y en un lugar."),
        ("Leonardo da Vinci estudió el cuerpo humano, diseñó máquinas y pintó. ¿Qué idea humanista muestra su trabajo? A) El ser humano puede conocer y transformar el mundo con su inteligencia y su creatividad B) Solo Dios puede explicar la naturaleza y el ser humano no debe investigarla", "A) El ser humano puede conocer y transformar el mundo con su inteligencia y su creatividad", "La opción B es la mirada teocéntrica medieval; el Humanismo valora la capacidad humana de crear y conocer."),
    ],
    ctx=("Un museo escolar prepara un afiche con el título «El Renacimiento: un despertar repentino de Europa». ¿Qué título más preciso propondrías? A) El Renacimiento: un cambio gradual que nació en Italia B) El Renacimiento: un cambio que ocurrió en 1453 en toda Europa", "A) El Renacimiento: un cambio gradual que nació en Italia", "El título A recoge el lugar de origen y el carácter gradual que explican las ideas de la ficha."),
    sc=[("¿Qué es el Humanismo según la ficha?", "Un movimiento de ideas que estudia a los autores clásicos y valora al ser humano", "Así lo define la ficha."),
        ("¿Qué siglo va del año 1501 al 1600?", "Siglo XVI", "Cada siglo parte en el año 01 y termina en el año 00."),
        ("=", "¿Cuántos años separan el nacimiento de Petrarca (1304) de su muerte (1374)?", "1374-1304", "Se resta el año de nacimiento al de muerte.", " años")],
    op=("Dibuja una línea de tiempo con la escala 1 cm = 50 años, desde 1300 hasta 1600. Marca estos cuatro puntos con una raya y su nombre: nacimiento de Petrarca (1304), imprenta de Gutenberg (hacia 1450), primer viaje de Colón (1492) y muerte de Miguel Ángel (1564). Debajo escribe una frase que explique por qué el Renacimiento no empezó un día exacto. {F}",
        "Petrarca a 0,1 cm del inicio, Gutenberg a 3 cm, Colón a 3,8 cm y Miguel Ángel a 5,3 cm; frase: «Hubo ideas humanistas desde el siglo XIV y el cambio se extendió poco a poco».",
        ["respeta la escala", "los cuatro puntos están bien ubicados", "la frase explica el carácter gradual"], ["línea de tiempo dibujada", "frase escrita"], ["poner los puntos sin medir con la escala", "escribir que el Renacimiento empezó en 1492"],
        "Pide que cuente por qué Petrarca queda tan al comienzo y qué dice eso sobre el origen de las ideas."),
    reinforce="Di en voz alta, con tus palabras, la diferencia entre Humanismo y Renacimiento y un dato de la ficha para cada uno.",
    extend="Busca en tu casa o en tu cuaderno un objeto o texto con fecha y explica a qué siglo pertenece esa fecha.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, carta, Florencia, 1480, escrita por un maestro de escuela a un amigo: «Mis alumnos leen a Cicerón en latín. Quiero que aprendan a hablar con claridad y a servir bien a su ciudad. Algunos padres se quejan: dicen que los libros antiguos no enseñan a rezar.» "
     "Fuente B, contrato, Florencia, 1485, entre un banquero y el taller de un pintor: «El pintor hará un retablo para la capilla de la familia del banquero. Entregará la obra en doce meses y el banquero pagará doscientos florines.»")
build(
    OA, 2, F,
    use="Aprenderé a leer una fuente del Renacimiento preguntando quién la escribió, cuándo, dónde y para qué, y a separar lo que dice de lo que yo interpreto.",
    prior=["Sé situar un hecho en el siglo y en la región.", "Sé que Humanismo y Renacimiento son procesos graduales.", "Sé que una fuente es una pista del pasado."],
    explain=[
        "Una fuente histórica es cualquier huella del pasado que sirve para conocerlo: una carta, un contrato, una pintura, un edificio. Para analizarla se contextualiza, es decir, se averigua quién la hizo, cuándo, dónde y con qué propósito. Una carta personal y un contrato legal se escriben con intenciones distintas y por eso informan cosas distintas.",
        "También hay que separar la descripción de la interpretación. Describir es decir lo que la fuente muestra o dice: «la carta menciona a Cicerón». Interpretar es sacar una idea a partir de eso: «el maestro quería formar buenos ciudadanos». Una interpretación sólida se apoya en la fuente y no dice más de lo que ella permite.",
        "Cada fuente tiene límites. Una carta expresa la opinión de una persona, no la de toda una ciudad. Un contrato muestra el mecenazgo, que es el apoyo de una persona rica que paga obras a artistas, pero no cuenta lo que el artista pensaba. Por eso un buen historiador compara varias fuentes y escribe conclusiones proporcionales a la evidencia.",
    ],
    vocab=[("fuente", "huella del pasado que sirve para conocer la historia"), ("contextualizar", "averiguar autor, fecha, lugar y propósito de una fuente"), ("mecenazgo", "apoyo económico que una persona rica da a artistas o sabios"), ("interpretación", "idea que se saca a partir de lo que dice una fuente"), ("evidencia", "dato de la fuente que sostiene una conclusión")],
    worked=[
        ("Contextualizar una fuente", "Una nota de ejemplo dice: «Venecia, 1495. Un comerciante anota que compró tres libros impresos a un librero». ¿Quién, cuándo y dónde?", ["Autor: un comerciante.", "Fecha: 1495.", "Lugar: Venecia."], "Un comerciante, en 1495, en Venecia"),
        ("Separar descripción e interpretación", "De la nota anterior se afirma: (1) «El comerciante compró tres libros impresos» y (2) «Todos los comerciantes de Venecia leían». ¿Cuál es descripción?", ["La frase (1) repite lo que la nota dice.", "La frase (2) generaliza a todos y la nota habla de uno."], "La (1) describe; la (2) generaliza más de lo permitido"),
    ],
    mistakes=[("Concluir con una carta que «todos» pensaban lo mismo.", "Una carta muestra la opinión de una sola persona.", "Escribe «el autor opina que» y busca otra fuente para comparar."),
              ("Contar la fuente sin averiguar quién la escribió ni para qué.", "Sin autor ni propósito no se sabe cuánto creerle.", "Antes de usarla, anota autor, fecha, lugar y propósito.")],
    T=[
        ("{F} ¿Quién escribió la Fuente A?", "Un maestro de escuela de Florencia", "La ficha dice que la escribió un maestro de escuela."),
        ("{F} ¿En qué año se firmó el contrato de la Fuente B?", "1485", "La ficha da ese año para la Fuente B."),
        ("=", "{F} ¿Cuántos años pasaron entre la carta y el contrato?", "1485-1480", "Se resta el año de la carta al del contrato.", " años"),
        ("{F} ¿Para qué se escribió el contrato? A) Para contar un recuerdo personal B) Para fijar la obra, el plazo y el pago", "B) Para fijar la obra, el plazo y el pago", "Un contrato establece obligaciones entre dos partes."),
        ("{F} ¿Cuál de las dos fuentes muestra mejor ideas humanistas sobre la educación y por qué?", "La Fuente A, porque habla de leer a Cicerón y de formar ciudadanos", "La carta menciona textos clásicos y el servicio a la ciudad."),
        ("{F} ¿Quién es el mecenas en la Fuente B?", "El banquero", "Es quien paga la obra al pintor."),
        ("{F} Clasifica: (1) «La carta dice que algunos padres se quejan». (2) «Todos los florentinos desconfiaban del Humanismo». ¿Cuál es descripción y cuál es una generalización excesiva?", "La (1) es descripción y la (2) es una generalización excesiva", "La carta habla de «algunos padres», no de todos los florentinos."),
        ("=", "{F} Si el banquero pagara los doscientos florines en cuatro cuotas iguales, ¿cuántos florines tendría cada cuota?", "200//4", "Se divide el pago total entre las cuotas.", " florines"),
        ("{F} ¿Basta la Fuente A para saber qué pensaban todos los padres de Italia? A) Sí, porque es una carta B) No, porque es la opinión de un maestro sobre algunos padres de una ciudad", "B) No, porque es la opinión de un maestro sobre algunos padres de una ciudad", "Una sola carta no permite generalizar a toda Italia."),
        ("{F} Un compañero concluye con la Fuente A: «En 1480 toda Europa estudiaba a Cicerón». ¿Qué falla en su conclusión?", "La fuente es de un maestro de Florencia y no habla de toda Europa", "Generaliza desde un lugar y una persona a todo un continente."),
        ("{F} El contrato dice que el retablo irá a una capilla. ¿Qué continuidad con la Edad Media muestra?", "Que el arte seguía sirviendo a fines religiosos", "Una capilla es un lugar de culto, así que la fe seguía presente en el arte."),
        ("{F} ¿Qué conclusión es proporcional a la Fuente A? A) «Al menos un maestro de Florencia enseñaba en 1480 con textos de Cicerón» B) «El Humanismo triunfó en todas las escuelas italianas»", "A) «Al menos un maestro de Florencia enseñaba en 1480 con textos de Cicerón»", "La conclusión A no dice más de lo que la carta permite."),
        ("{F} La Fuente B es un documento legal y la Fuente A, una carta personal. ¿Cuál se escribió para tener valor legal entre dos partes?", "La Fuente B, el contrato", "Un contrato se hace para fijar compromisos exigibles."),
    ],
    ctx=("Un curso quiere saber por qué los artistas del Renacimiento tenían tanto trabajo en Florencia. Con la Fuente B, ¿qué factor puede señalar sin exagerar? {F}", "Que había personas ricas, como un banquero, que pagaban obras por contrato", "El contrato muestra el mecenazgo de un banquero en 1485, aunque no prueba que fuera lo único."),
    sc=[("¿Qué cuatro datos averigua quien contextualiza una fuente?", "Autor, fecha, lugar y propósito", "Son los datos que ubican la fuente."),
        ("¿Qué es el mecenazgo?", "El apoyo económico de una persona rica a artistas o sabios", "Así se definió en la explicación."),
        ("Una carta dice «los vecinos están contentos con el nuevo puente». ¿Qué falta para creerle sin dudas: A) conocer quién la escribió y si tenía interés B) comprobar que la carta coincide con lo que tú ya piensas", "A) conocer quién la escribió y si tenía interés", "El autor y su propósito influyen en la confianza en una fuente.")],
    op=("Analiza esta fuente de ejemplo: «Roma, 1510. Un joven aprendiz escribe a su madre: ya sé dibujar una mano con sus sombras, y mi maestro me deja mezclar los colores, pero todavía no firma mis dibujos». Completa una tabla con cuatro filas: autor, fecha, lugar y propósito probable. Después escribe una frase de descripción y otra de interpretación que no exagere. {F}",
        "Autor: un aprendiz; fecha: 1510; lugar: Roma; propósito: contarle a su madre sus avances. Descripción: «El aprendiz sabe dibujar una mano con sombras». Interpretación: «Los talleres enseñaban el dibujo con sombras a sus aprendices, al menos en este caso».",
        ["completa las cuatro filas", "la descripción repite lo que dice la fuente", "la interpretación es proporcional"], ["tabla escrita", "dos frases"], ["afirmar que todos los aprendices de Roma aprendían así", "mezclar lo que dice la fuente con lo que se supone"],
        "Pide que explique por qué su interpretación no habla de todos los talleres."),
    reinforce="Elige una carta o nota breve y responde en voz alta: quién la escribió, cuándo, dónde y para qué.",
    extend="Escribe una pregunta que no se pueda responder con la Fuente A y dime qué otra fuente ayudaría.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (resumen para este cuaderno). Rasgos medievales (siglos XI al XIV): el saber se centra en Dios (teocentrismo); los libros se copian a mano, sobre todo en monasterios; el arte enseña la fe con figuras planas. "
     "Rasgos del Renacimiento (siglos XV y XVI): el saber se interesa por el ser humano y la naturaleza (antropocentrismo); se estudian de nuevo textos de Grecia y Roma; la pintura usa la perspectiva y cuerpos realistas; la fe cristiana sigue muy presente. "
     "Territorio: el Renacimiento se desarrolla en Italia (Florencia, Roma, Venecia) desde 1400; llega con fuerza a los Países Bajos, Francia, Inglaterra y España desde 1500.")
build(
    OA, 3, F,
    use="Aprenderé a reconocer qué cambió y qué continuó entre la Edad Media y el Renacimiento, y a explicar cómo se extendió el movimiento por el territorio europeo.",
    prior=["Sé distinguir descripción e interpretación.", "Sé ubicar Italia y otras regiones de Europa.", "Sé calcular diferencias entre años."],
    explain=[
        "Un cambio es algo nuevo que aparece o algo que se transforma; una continuidad es algo que se mantiene. En el Renacimiento hubo cambios importantes: el ser humano y la naturaleza pasaron al centro del interés (antropocentrismo), se recuperaron los textos clásicos y los pintores usaron la perspectiva. Pero también hubo continuidades: la fe cristiana siguió siendo muy importante y muchas obras tenían temas religiosos.",
        "Para entender el proceso hay que mirar también el territorio, es decir, el lugar donde ocurre algo. El Renacimiento comenzó en ciudades italianas ricas por el comercio y se difundió a otras regiones más tarde. Por eso no todos los lugares cambiaron al mismo tiempo: un pueblo alejado podía seguir con costumbres medievales mientras Florencia ya vivía el Renacimiento.",
        "Al comparar épocas conviene evitar dos extremos. Decir que todo cambió esconde las continuidades; decir que nada cambió esconde las transformaciones. Una buena explicación nombra ambos: qué cambió, qué siguió igual, dónde y cuándo.",
    ],
    vocab=[("cambio", "algo nuevo que aparece o se transforma"), ("continuidad", "algo que se mantiene a través del tiempo"), ("antropocentrismo", "mirada que pone al ser humano en el centro del interés"), ("teocentrismo", "mirada que pone a Dios en el centro de todo"), ("perspectiva", "técnica de pintura que da sensación de profundidad")],
    worked=[
        ("Clasificar cambio y continuidad", "Una iglesia de 1520 sigue celebrando misa como en 1320, pero su pintura del altar usa la perspectiva. ¿Qué es continuidad y qué es cambio?", ["La misa se repite igual: continuidad.", "La perspectiva en la pintura es una técnica nueva: cambio."], "Continuidad: la misa; cambio: la perspectiva"),
        ("Medir la difusión en el territorio", "Un humanista llega de Italia a Inglaterra en 1510. Si el Renacimiento tomó fuerza en Italia hacia 1400, ¿cuántos años pasaron entre 1400 y la llegada de ese humanista?", ["Resto: 1510 − 1400.", "El resultado es 110."], "110 años"),
    ],
    mistakes=[("Decir que en el Renacimiento la gente dejó de ser religiosa.", "Se confunde interés por el ser humano con rechazo a la fe.", "Recuerda que la fe cristiana siguió muy presente y muchos humanistas eran creyentes."),
              ("Pensar que todos los lugares de Europa cambiaron a la vez.", "Se ignora que el movimiento partió en Italia y se difundió de a poco.", "Indica siempre el lugar y el momento en que llegó el cambio.")],
    T=[
        ("{F} ¿En qué región de Europa se desarrolla primero el Renacimiento?", "En Italia", "La ficha dice que se desarrolla en Italia desde 1400."),
        ("{F} ¿Cómo se copiaban los libros en la Edad Media según la ficha?", "A mano, sobre todo en monasterios", "La ficha lo indica entre los rasgos medievales."),
        ("{F} ¿Qué técnica de pintura es un rasgo del Renacimiento?", "La perspectiva", "La ficha la nombra junto a los cuerpos realistas."),
        ("{F} Clasifica como cambio o continuidad: a) la perspectiva en la pintura, b) la fe cristiana, c) el estudio de textos de Roma.", "a) cambio; b) continuidad; c) cambio", "La fe se mantiene; la perspectiva y el estudio de los clásicos son novedades."),
        ("=", "{F} Según la ficha, el Renacimiento llegó con fuerza a Francia desde 1500, y en Italia se desarrolla desde 1400. ¿Cuántos años después llegó a Francia?", "1500-1400", "Se restan los años de inicio en cada territorio.", " años"),
        ("{F} ¿Por qué se dice que el cambio no fue uniforme en el territorio?", "Porque llegó a cada región en momentos distintos: primero Italia y después otras regiones", "La ficha separa las fechas de Italia y del resto de Europa."),
        ("{F} Un mapa del Renacimiento hacia 1420 debería marcar con más fuerza: A) Italia B) Inglaterra", "A) Italia", "En 1420 el movimiento se desarrollaba en Italia y llegaba a Inglaterra más tarde."),
        ("{F} Una pintura de 1510 muestra a la Virgen María con perspectiva y cuerpos realistas. ¿Qué cambio y qué continuidad muestra?", "Cambio: perspectiva y cuerpos realistas; continuidad: tema religioso", "La técnica es nueva y el tema sigue siendo cristiano."),
        ("{F} ¿Qué rasgo del Renacimiento demuestra que no hubo ruptura total con la Edad Media?", "La fe cristiana sigue muy presente", "Ese rasgo se conserva de la época anterior."),
        ("{F} Un cartel dice: «En 1450 Europa dejó de ser medieval de un día para otro». ¿Qué datos de la ficha lo contradicen?", "Que otras regiones lo adoptaron en el siglo XVI y que la fe siguió presente", "La ficha muestra una difusión gradual y rasgos que continúan."),
        ("{F} En 1450 un pueblo del interior de Francia sigue copiando libros a mano. ¿Contradice eso que el Renacimiento nació en Italia hacia 1400?", "No, porque el cambio llegó más tarde a otras regiones", "La difusión por el territorio fue gradual."),
        ("{F} Un historiador dice: «Todo cambió con el Renacimiento». ¿Qué continuidad de la ficha le puedes oponer?", "Que la fe cristiana siguió muy presente", "Esa continuidad muestra que no todo cambió."),
        ("{F} ¿Qué cambio de mirada separa el saber medieval del renacentista, según la ficha? Responde con «de… a…».", "De Dios (teocentrismo) al ser humano y la naturaleza (antropocentrismo)", "La ficha opone el saber centrado en Dios al interés por el ser humano."),
    ],
    ctx=("Un guía de museo dice: «Mira esta tabla de 1520 de un pintor holandés: usa perspectiva, pero su tema es la Virgen». Explica cómo la obra combina cambio y continuidad. {F}", "Combina un cambio, la perspectiva, con una continuidad, el tema religioso", "La técnica es nueva y el contenido conserva la fe, como en la ficha."),
    sc=[("¿Qué es una continuidad histórica?", "Algo que se mantiene a través del tiempo", "Es lo contrario de un cambio."),
        ("¿Qué región recibió el Renacimiento más tarde: Italia o España?", "España", "Según la ficha, España lo recibió con fuerza desde 1500."),
        ("=", "El Renacimiento se desarrolló en Italia desde 1400. ¿Cuántos años pasaron hasta 1500, cuando llegó con fuerza a los Países Bajos?", "1500-1400", "Se resta el año de inicio en Italia al año de llegada a otro territorio.", " años")],
    op=("Haz una tabla de dos columnas, «Cambio» y «Continuidad», y escribe en ella cuatro rasgos de la ficha: perspectiva, fe cristiana, estudio de textos de Grecia y Roma y atención al ser humano. Después elige una región de la ficha y escribe cuántos años después que en Italia llegó el Renacimiento, usando 1400 como año de inicio en Italia. {F}",
        "Cambio: perspectiva, estudio de textos clásicos, atención al ser humano. Continuidad: fe cristiana. Francia: 1500 − 1400 = 100 años después.",
        ["clasifica los cuatro rasgos correctamente", "hace la resta bien", "nombra una región de la ficha"], ["tabla completa", "cálculo escrito"], ["poner la fe cristiana como cambio", "olvidar usar 1400 como punto de partida"],
        "Pide que explique por qué la fe cristiana va en la columna de continuidad."),
    reinforce="Cuenta oralmente un cambio y una continuidad del Renacimiento y di dónde y cuándo ocurrían.",
    extend="Escribe un ejemplo de tu vida de algo que cambió y algo que continuó en tu colegio en los últimos cinco años.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son testimonios reales). "
     "Voz 1, banquero de Florencia, 1470: «Pago pinturas y libros porque honran a mi familia y a mi ciudad.» "
     "Voz 2, pintor de un taller, 1470: «Gracias a mis protectores puedo experimentar con la perspectiva, pero debo pintar lo que me piden.» "
     "Voz 3, sacerdote, 1470: «El arte debe llevar a las personas a Dios; me alegra que embellezca las iglesias.» "
     "Voz 4, campesino cerca de Florencia, 1470: «Pago el arriendo de la tierra y no sé leer; esas obras no llegan a mi aldea.» "
     "Causas que mencionan los historiadores: comercio y bancos ricos en las ciudades italianas; mecenazgo de familias poderosas; sabios que llegaron a Italia con manuscritos griegos; y, desde 1450, la imprenta.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar lo que decían distintos actores del Renacimiento y a explicar por qué este movimiento tuvo varias causas y no solo una.",
    prior=["Sé contextualizar una fuente.", "Sé reconocer cambio y continuidad.", "Conozco la idea de mecenazgo."],
    explain=[
        "Un actor histórico es una persona o grupo que participa en un hecho. En el Renacimiento los actores eran muchos: banqueros que financiaban obras, artistas que las hacían, sacerdotes que las encargaban para las iglesias y campesinos que casi no tenían acceso a ellas. Cada actor tenía una perspectiva, es decir, un punto de vista según su lugar en la sociedad.",
        "Contrastar perspectivas significa compararlas y ver en qué coinciden y en qué se separan. El banquero ve honor y prestigio, el pintor ve libertad limitada, el sacerdote ve fe y el campesino ve distancia. Ninguna voz cuenta toda la historia; juntas muestran que el Renacimiento benefició sobre todo a quienes vivían en las ciudades y tenían dinero o educación.",
        "También hay que explicar las causas. Una explicación multicausal reconoce que un hecho tiene varias razones que se combinan: el dinero del comercio, el mecenazgo, la llegada de manuscritos griegos y la imprenta. Elegir una sola causa suele ser una simplificación.",
    ],
    vocab=[("actor", "persona o grupo que participa en un hecho histórico"), ("perspectiva", "punto de vista de un actor según su posición social"), ("causa", "razón que ayuda a explicar por qué ocurrió algo"), ("multicausal", "explicación que combina varias causas"), ("contrastar", "comparar para ver coincidencias y diferencias")],
    worked=[
        ("Identificar perspectivas", "En la ficha, ¿qué perspectiva tiene el campesino sobre las obras del Renacimiento?", ["Leo su voz: paga arriendo y no sabe leer.", "Dice que las obras no llegan a su aldea."], "Ve las obras como algo lejano a su vida"),
        ("Distinguir causas", "Una persona dice: «El Renacimiento se debió solo a la imprenta». ¿Por qué es una explicación incompleta?", ["La ficha menciona más causas: bancos, mecenazgo y manuscritos griegos.", "Además, la imprenta es de hacia 1450 y el movimiento empezó antes."], "Porque ignora otras causas y empezó antes de la imprenta"),
    ],
    mistakes=[("Atribuir el Renacimiento a una sola causa, como el dinero.", "Se simplifica un proceso con varias razones combinadas.", "Nombra al menos dos causas y explica cómo se relacionan."),
              ("Creer que la voz del banquero representa a toda la sociedad.", "Se olvida que cada actor mira desde su posición.", "Compara varias voces y di quién habla y quién queda sin voz.")],
    T=[
        ("{F} ¿Quién dice «pago pinturas y libros porque honran a mi familia y a mi ciudad»?", "El banquero de Florencia", "La Voz 1 es la del banquero."),
        ("{F} ¿Qué perspectiva tiene el sacerdote sobre el arte?", "Que debe llevar a las personas a Dios", "La Voz 3 lo dice."),
        ("{F} ¿Qué actor dice que no sabe leer?", "El campesino", "La Voz 4 lo señala."),
        ("{F} ¿Qué actores de la ficha se benefician claramente del mecenazgo: banquero y pintor, o campesino?", "Banquero y pintor", "Uno paga por prestigio y otro obtiene trabajo y libertad para experimentar."),
        ("{F} ¿Qué diferencia hay entre la voz del pintor y la del banquero sobre quién decide qué pintar?", "El banquero encarga; el pintor debe pintar lo que le piden", "La Voz 2 habla de límites y la Voz 1 de encargo."),
        ("{F} Clasifica cada causa como económica o cultural: a) comercio y bancos ricos, b) manuscritos griegos que llegan a Italia.", "a) económica; b) cultural", "El comercio y los bancos son dinero; los manuscritos son saber."),
        ("{F} Ordena de quien más participa en hacer la obra a quien menos accede a ella: campesino, banquero, pintor.", "Pintor, banquero, campesino", "El pintor las hace, el banquero las paga y al campesino no le llegan."),
        ("=", "{F} Petrarca nació en 1304. ¿Cuántos años antes de la imprenta (desde 1450) nació?", "1450-1304", "Se resta el año de su nacimiento al año de la imprenta.", " años"),
        ("{F} Una persona dice: «El Renacimiento se debió solo al mecenazgo». ¿Qué otra causa de la ficha puedes oponerle?", "El comercio y los bancos de las ciudades italianas o la llegada de manuscritos griegos", "La ficha ofrece varias causas, no solo el mecenazgo."),
        ("{F} ¿Por qué se dice que ninguna de las cuatro voces cuenta «toda» la historia?", "Porque cada una habla desde su posición y faltan otras voces", "Las perspectivas son parciales; por ejemplo, la ficha no incluye mujeres ni artesanos."),
        ("{F} ¿Qué conclusión sobre quiénes se beneficiaron del Renacimiento es proporcional? A) Se benefició sobre todo a quienes vivían en ciudades y tenían dinero o educación B) Se benefició por igual a toda la población", "A) Se benefició sobre todo a quienes vivían en ciudades y tenían dinero o educación", "La voz del campesino muestra que las obras no llegaban a todos."),
        ("{F} Un compañero dice: «Como el sacerdote celebra el arte, la Iglesia fue enemiga del Humanismo». ¿Qué falla?", "Generaliza desde una voz y la ficha no muestra enemistad", "Una sola voz no demuestra la postura de toda la Iglesia."),
        ("{F} Si quisieras escuchar la voz de una persona que no aparece en la ficha, como un artesano, ¿qué tipo de fuente buscarías?", "Un documento de su gremio o taller, como una cuenta o un reglamento", "Esos registros muestran el trabajo cotidiano de artesanos."),
    ],
    ctx=("Una profesora pide: «Explica con dos voces de la ficha por qué el Renacimiento no benefició por igual a todos». ¿Qué dos voces elegirías? {F}", "La del banquero, que paga y se prestigia, y la del campesino, a quien las obras no llegan", "Contrasta a quien se beneficia con quien queda al margen."),
    sc=[("¿Qué es una explicación multicausal?", "Una explicación que combina varias causas", "Así se definió en la clase."),
        ("¿Qué actor de la ficha produce las obras con sus manos?", "El pintor", "Su voz dice que debe pintar lo que le piden."),
        ("Una persona opina que el Renacimiento fue obra de «un solo genio». ¿Qué respondes con la ficha? A) Fue un proceso con muchos actores y causas B) Tenía razón, porque la ficha nombra solo a un pintor", "A) Fue un proceso con muchos actores y causas", "La ficha muestra varios actores y causas.")],
    op=("Imagina que escribes un diálogo breve de seis líneas entre el banquero y el campesino de la ficha. En tres líneas el banquero defiende el mecenazgo y en tres el campesino explica por qué las obras no llegan a su aldea. Usa al menos un dato de la ficha en cada voz y cierra con una frase tuya que resuma en qué se diferencian sus perspectivas. {F}",
        "Banquero: honra a la familia y la ciudad, pago libros y pinturas. Campesino: pago arriendo, no leo, las obras no llegan. Cierre: «El banquero ve prestigio y el campesino ve distancia».",
        ["usa un dato de la ficha en cada voz", "el diálogo respeta las dos perspectivas", "la frase de cierre las contrasta"], ["diálogo escrito", "frase de cierre"], ["poner las dos voces de acuerdo sin evidencia", "inventar datos que contradicen la ficha"],
        "Pide que explique qué voz falta en el diálogo y por qué importaría escucharla."),
    reinforce="Nombra de memoria dos actores del Renacimiento y la perspectiva de cada uno.",
    extend="Escribe una voz más, la de una mujer de una familia rica de Florencia, sin inventar hechos: solo una pregunta que le harías.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). Pregunta: ¿fue el Renacimiento una ruptura total con la Edad Media? "
     "Evidencia 1: pintores del siglo XV usan la perspectiva en tablas de tema religioso. "
     "Evidencia 2: la fe cristiana sigue presente en la vida de las ciudades italianas. "
     "Evidencia 3: humanistas como Petrarca (1304-1374) estudiaban textos clásicos ya en la Edad Media. "
     "Evidencia 4: la imprenta, hacia 1450, permite copiar libros mucho más rápido que a mano. "
     "Evidencia 5: la mayoría de los campesinos europeos del siglo XV seguía viviendo del trabajo de la tierra.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento con tesis, evidencias y un límite, para responder si el Renacimiento fue o no una ruptura total con la Edad Media.",
    prior=["Sé distinguir cambio y continuidad.", "Sé contrastar perspectivas.", "Sé que una conclusión debe ser proporcional a la evidencia."],
    explain=[
        "Un argumento histórico tiene tres partes. La tesis es la respuesta que defiendes a una pregunta. Las evidencias son los datos de las fuentes que la sostienen. El límite es una frase que reconoce lo que esas evidencias no alcanzan a probar. Sin evidencia, una tesis es solo una opinión.",
        "Para esta pregunta hay evidencias de cambio, como la perspectiva y la imprenta, y de continuidad, como la fe cristiana y la vida campesina. Una tesis equilibrada puede decir que el Renacimiento transformó mucho la cultura de las ciudades, pero conservó rasgos medievales importantes. Esa respuesta es más precisa que decir «cambió todo» o «no cambió nada».",
        "Para evaluar un argumento, mira si cada evidencia se relaciona con la tesis y si el límite es honesto. Una buena respuesta cita datos concretos, explica cómo apoyan la idea y reconoce que otra fuente podría matizarla.",
    ],
    vocab=[("tesis", "respuesta que se defiende a una pregunta"), ("evidencia", "dato de una fuente que sostiene la tesis"), ("límite", "frase que reconoce lo que la evidencia no prueba"), ("ruptura", "cambio total que corta con lo anterior"), ("matizar", "precisar una idea reconociendo excepciones")],
    worked=[
        ("Elegir evidencia para una tesis", "Tesis: «El Renacimiento conservó rasgos de la Edad Media». ¿Qué evidencia de la ficha la apoya?", ["Busco datos de continuidad.", "La evidencia 2 (fe cristiana presente) y la 5 (vida campesina) muestran continuidad."], "Evidencias 2 y 5"),
        ("Escribir un límite", "Con las evidencias 1 y 4 alguien afirma que «cambió toda la sociedad». ¿Qué límite corresponde?", ["Esas evidencias hablan de la pintura y de la imprenta.", "No dicen nada de la vida de los campesinos."], "Estas evidencias no muestran lo que pasaba en la vida campesina"),
    ],
    mistakes=[("Responder con una tesis sin citar ninguna evidencia.", "Una opinión sin datos no es un argumento histórico.", "Cita al menos dos datos de las fuentes y explica cómo apoyan tu idea."),
              ("Citar solo las evidencias que apoyan la tesis y esconder las demás.", "Se evita mirar lo que la contradice.", "Menciona también una evidencia que matiza y usa el límite.")],
    T=[
        ("{F} ¿Qué evidencia de la ficha muestra la continuidad de la fe cristiana?", "La evidencia 2", "Dice que la fe sigue presente en las ciudades italianas."),
        ("{F} ¿Qué evidencia indica que la imprenta aceleró la producción de libros?", "La evidencia 4", "Habla de copiar libros más rápido que a mano."),
        ("{F} ¿Qué es la tesis de un argumento?", "La respuesta que se defiende a una pregunta", "Es la idea central que las evidencias sostienen."),
        ("{F} ¿Cuáles de las cinco evidencias muestran únicamente continuidad con la Edad Media, sin mezclar un cambio?", "La 2, la 3 y la 5", "La fe cristiana, el estudio de clásicos desde Petrarca y la vida campesina vienen de antes."),
        ("{F} ¿Qué evidencia mezcla un cambio y una continuidad a la vez?", "La evidencia 1: perspectiva nueva en tablas de tema religioso", "La perspectiva es un cambio y el tema religioso, una continuidad."),
        ("{F} ¿Qué tesis se apoya mejor en las cinco evidencias? A) El Renacimiento cambió mucho la cultura de las ciudades pero conservó rasgos medievales B) El Renacimiento no cambió nada", "A) El Renacimiento cambió mucho la cultura de las ciudades pero conservó rasgos medievales", "Las evidencias 1 y 4 muestran cambios y las 2, 3 y 5 muestran continuidades."),
        ("{F} Una tesis dice: «El Humanismo apareció de golpe con el Renacimiento». ¿Qué evidencia de la ficha la debilita?", "La evidencia 3, porque Petrarca ya estudiaba textos clásicos en la Edad Media", "Petrarca vivió entre 1304 y 1374, antes del siglo XV."),
        ("=", "{F} ¿Cuántos años antes de la imprenta (hacia 1450) murió Petrarca en 1374?", "1450-1374", "Se resta el año de su muerte al de la imprenta.", " años"),
        ("{F} Ana escribe: «Cambió todo porque apareció la perspectiva». ¿Qué le falta a su argumento?", "Más evidencias y un límite, porque la perspectiva no prueba que cambiara toda la sociedad", "Una sola evidencia sobre pintura no basta para hablar de todo."),
        ("{F} Escribe un límite honesto para la evidencia 1.", "Solo muestra un cambio en la pintura y no dice nada de la vida cotidiana de la mayoría", "La evidencia habla de pintores, no de toda la población."),
        ("{F} ¿Qué evidencia de la ficha te sirve para matizar la tesis «el Renacimiento fue para toda la sociedad»?", "La evidencia 5, porque los campesinos siguieron viviendo del trabajo de la tierra", "Muestra que la vida de muchos no cambió con el Renacimiento."),
        ("{F} Un compañero cita solo las evidencias 1 y 4 y concluye que «hubo ruptura total». ¿Qué error comete?", "Ignora las evidencias de continuidad (2, 3 y 5)", "Seleccionó solo los datos que apoyan su idea."),
        ("{F} ¿Qué respuesta es más sólida? A) «Hubo cambios y continuidades: la perspectiva y la imprenta cambian la cultura, pero la fe y la vida campesina continúan» B) «Fue una ruptura total porque sí»", "A) «Hubo cambios y continuidades: la perspectiva y la imprenta cambian la cultura, pero la fe y la vida campesina continúan»", "Cita evidencias concretas y reconoce ambos aspectos."),
    ],
    ctx=("Un concurso escolar pregunta: «¿Fue el Renacimiento una ruptura total con la Edad Media?». Redacta en una frase una respuesta que cite dos evidencias de la ficha, una de cambio y otra de continuidad. {F}", "No fue una ruptura total: la imprenta y la perspectiva cambian la cultura, pero la fe cristiana continúa", "Combina una evidencia de cambio y una de continuidad."),
    sc=[("¿Qué partes tiene un argumento histórico?", "Tesis, evidencias y límite", "Son las tres partes de la clase."),
        ("¿Para qué sirve el límite en un argumento?", "Para reconocer lo que la evidencia no prueba", "Evita decir más de lo que muestran las fuentes."),
        ("{F} ¿Qué evidencia citarías para mostrar que la imprenta es un cambio?", "La evidencia 4", "Dice que permite copiar libros mucho más rápido que a mano.")],
    op=("Escribe un párrafo de cinco a seis líneas que responda a la pregunta de la ficha. Debe incluir tu tesis, dos evidencias numeradas de la ficha (una de cambio y una de continuidad) y un límite que diga qué no prueban esas evidencias. Puedes empezar así: «Pienso que el Renacimiento fue…». {F}",
        "Pienso que el Renacimiento fue un gran cambio cultural, pero no una ruptura total. Evidencia 4: la imprenta acelera la copia de libros. Evidencia 2: la fe cristiana sigue presente. Límite: no sé qué pasaba en las aldeas.",
        ["tiene tesis clara", "cita dos evidencias distintas", "incluye un límite honesto"], ["párrafo escrito"], ["no citar evidencias", "usar solo evidencias de un tipo"],
        "Pide que explique por qué su límite es necesario y qué otra fuente buscaría."),
    reinforce="Di en voz alta una tesis sobre el Renacimiento y las dos evidencias que la sostienen.",
    extend="Busca una opinión que escuches sobre cualquier tema y reescríbela como tesis con una evidencia y un límite.",
)
