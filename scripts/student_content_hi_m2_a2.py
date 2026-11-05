"""Material del estudiante de 2.º medio, Historia, Geografía y Ciencias Sociales: OA 03 (Segunda Guerra Mundial, genocidio y población civil) y OA 04 (posguerra, descolonización, ONU y derechos humanos)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 03"

# ================================================================ OA 03, clase 1
F = ("Ficha 1 (hechos). 1919: tratado de Versalles, que cierra la Primera Guerra Mundial. 1931: Japón ocupa Manchuria, territorio de China. 1935: Italia invade Etiopía. "
     "1938: Alemania une a Austria a su territorio. 1 de septiembre de 1939: Alemania invade Polonia; el 3 de septiembre Reino Unido y Francia le declaran la guerra. "
     "Bandos: el Eje (Alemania, Italia y Japón) y los Aliados (Reino Unido, Francia y, más tarde, la URSS y Estados Unidos). "
     "Liga de las Naciones: organización creada después de la Primera Guerra para mantener la paz; no tenía ejército propio. "
     "Apaciguamiento: ceder ante las exigencias de un país agresor para evitar una guerra.")
build(
    OA, 1, F,
    use="Aprenderé a situar la Segunda Guerra Mundial en el tiempo, a reconocer por qué el orden mundial de entreguerras era frágil y a nombrar sus principales actores.",
    prior=["Sé que la Primera Guerra Mundial terminó en 1918 y que Versalles se firmó en 1919.", "Sé calcular cuántos años hay entre dos fechas.", "Sé que un hecho histórico tiene varias causas."],
    explain=[
        "La Segunda Guerra Mundial comenzó en Europa en septiembre de 1939, pero sus causas venían de antes. El orden mundial es el conjunto de reglas e instituciones con que los países intentan convivir. Tras 1919 ese orden descansaba en el tratado de Versalles y en la Liga de las Naciones, una organización que no tenía ejército propio para detener a un país agresor.",
        "Entre 1931 y 1938 hubo varias agresiones: Japón en Manchuria, Italia en Etiopía y la unión forzada de Austria con Alemania. Muchos gobiernos democráticos prefirieron el apaciguamiento, es decir, ceder para evitar la guerra. Esa política no detuvo a los regímenes que querían expandirse, y por eso se dice que el orden de entreguerras era frágil.",
        "Los actores principales fueron el Eje (Alemania, Italia y Japón) y los Aliados (Reino Unido, Francia y, más tarde, la URSS y Estados Unidos). Para situar un proceso así hay que ubicar cada hecho en su fecha, decir quién lo impulsó y evitar un error común: creer que la guerra empezó de un día para otro y sin aviso.",
    ],
    vocab=[("orden mundial", "reglas e instituciones con que los países intentan convivir"), ("Liga de las Naciones", "organización creada tras la Primera Guerra para mantener la paz, sin ejército propio"), ("Eje", "bando formado por Alemania, Italia y Japón"), ("Aliados", "bando que combatió al Eje, con Reino Unido, Francia, la URSS y Estados Unidos"), ("apaciguamiento", "ceder ante un país agresor para evitar una guerra")],
    worked=[
        ("Calcular una distancia en el tiempo", "¿Cuántos años pasaron entre la ocupación de Manchuria y la invasión alemana de Polonia?", ["Tomo el año de cada hecho en la ficha: 1931 y 1939.", "Resto: 1939 − 1931 = 8."], "8 años"),
        ("Ubicar a un actor en su bando", "Italia invadió Etiopía en 1935. ¿A qué bando pertenece según la ficha?", ["Busco a Italia en la lista de bandos.", "Aparece junto a Alemania y Japón."], "Al Eje"),
    ],
    mistakes=[("Decir que la guerra empezó solo porque Alemania invadió Polonia.", "Se mira solo el hecho final y se olvidan las agresiones anteriores.", "Nombra el hecho de 1939 como inicio y agrega las agresiones de 1931 a 1938."),
              ("Creer que la Liga de las Naciones podía obligar a cumplir las reglas con su ejército.", "Se supone un poder que no tenía.", "Recuerda que no tenía ejército propio y dependía de sus miembros.")],
    T=[
        ("{F} ¿Qué hecho ocurrido el 1 de septiembre de 1939 aparece en la ficha?", "Alemania invade Polonia", "La ficha lo registra con esa fecha."),
        ("{F} ¿Qué países forman el Eje según la ficha?", "Alemania, Italia y Japón", "La ficha los nombra como el primer bando."),
        ("{F} ¿Para qué se creó la Liga de las Naciones?", "Para mantener la paz después de la Primera Guerra Mundial", "Ese es el propósito que indica la ficha."),
        ("=", "{F} ¿Cuántos años pasaron entre la invasión italiana de Etiopía y la invasión alemana de Polonia?", "1939-1935", "Se resta el año de la invasión a Etiopía al de la invasión a Polonia.", " años"),
        ("{F} ¿Qué país ocupó Manchuria, un territorio de China, en 1931? A) Japón B) Italia", "A) Japón", "La ficha dice que Japón ocupó Manchuria; Italia invadió Etiopía en 1935."),
        ("{F} ¿Cuál de estos hechos es una agresión anterior a 1939 que muestra la debilidad de la Liga? A) Italia invade Etiopía en 1935 B) Reino Unido y Francia declaran la guerra en 1939", "A) Italia invade Etiopía en 1935", "Fue una agresión de 1935; la declaración de 1939 es una respuesta ya durante la guerra."),
        ("{F} ¿Cuál de estos hechos es posterior a la unión de Austria con Alemania? A) La ocupación de Manchuria B) La declaración de guerra de Reino Unido y Francia", "B) La declaración de guerra de Reino Unido y Francia", "Manchuria fue en 1931, antes de 1938; la declaración es de 1939."),
        ("{F} En 1938 un gobierno acepta que otro país se quede con un territorio para evitar una guerra. ¿Qué política aplica? A) Apaciguamiento B) Alianza militar", "A) Apaciguamiento", "Ceder ante un agresor para evitar la guerra es apaciguamiento, según la ficha."),
        ("{F} En 1943 Estados Unidos y la URSS combaten a Alemania. ¿A qué bando pertenecen? A) Aliados B) Eje", "A) Aliados", "La ficha incluye a la URSS y a Estados Unidos entre los Aliados."),
        ("{F} ¿Qué razón de la ficha permite decir que el orden mundial de entreguerras era frágil? A) Hubo agresiones en 1931, 1935 y 1938 antes de la guerra de 1939 B) El tratado de Versalles se firmó en 1919", "A) Hubo agresiones en 1931, 1935 y 1938 antes de la guerra de 1939", "Varias agresiones sin freno muestran la fragilidad; la fecha de Versalles por sí sola no lo prueba."),
        ("{F} Un compañero dice: «La guerra de 1939 no tuvo causas anteriores». ¿Qué corrección hace con la ficha? A) Hubo agresiones previas desde 1931 y un orden débil B) Tiene razón, porque la fecha de inicio es una sola", "A) Hubo agresiones previas desde 1931 y un orden débil", "Tener una fecha de inicio no significa que no hubiera causas anteriores."),
        ("{F} Ordena del más antiguo al más reciente: (a) unión de Austria con Alemania (b) ocupación de Manchuria (c) invasión de Etiopía (d) invasión de Polonia.", "b, c, a, d", "Los años son 1931, 1935, 1938 y 1939 en ese orden."),
        ("{F} ¿Cuál es la mejor pregunta de investigación para este tema? A) ¿Por qué el orden mundial de entreguerras no evitó una nueva guerra? B) ¿Quién fue el mejor general de la guerra?", "A) ¿Por qué el orden mundial de entreguerras no evitó una nueva guerra?", "La primera se responde con hechos y fechas; la segunda es una opinión sin criterio."),
    ],
    ctx=("Una sala de museo se titula «La guerra estalló de un día para otro en 1939». ¿Qué problema tiene el título? A) Omite las agresiones y tensiones previas desde 1931 B) Confunde el inicio de la guerra con su final", "A) Omite las agresiones y tensiones previas desde 1931", "La ficha muestra hechos de 1931, 1935 y 1938 que prepararon la guerra."),
    sc=[("¿Qué era la Liga de las Naciones?", "Una organización creada para mantener la paz, sin ejército propio", "Así se define en el vocabulario."),
        ("¿Qué es el apaciguamiento?", "Ceder ante un país agresor para evitar una guerra", "Así se define en la clase."),
        ("En Historia: ¿qué es el Eje?", "El bando formado por Alemania, Italia y Japón", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo de 1919 a 1939 con una raya y un nombre para cada hecho: Versalles, Manchuria, Etiopía, Austria e invasión de Polonia. Colorea de otro color los hechos que sean agresiones. Debajo escribe dos frases: una que explique por qué el orden de entreguerras era frágil y otra que nombre a los dos bandos de la guerra. {F}",
        "Las agresiones coloreadas son Manchuria (1931), Etiopía (1935), Austria (1938) y Polonia (1939). Frases: «El orden era frágil porque la Liga no tenía ejército y las agresiones no se detuvieron»; «Los bandos fueron el Eje y los Aliados».",
        ["ubica los cinco hechos en su año", "distingue las agresiones", "las dos frases son correctas y distintas"], ["línea de tiempo dibujada", "dos frases escritas"], ["poner todos los hechos en 1939", "olvidar que la Liga no tenía ejército"],
        "Pide que explique por qué una sola fecha de inicio no basta para entender las causas."),
    reinforce="Cuenta en voz alta, con tus palabras, tres hechos anteriores a 1939 que muestren que el orden de entreguerras era frágil.",
    extend="Piensa en una discusión que empezó por algo pequeño y di qué problemas anteriores la hicieron posible.",
)

# ================================================================ OA 03, clase 2
F = ("Ficha 2 (hechos y tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Hechos: el 23 de agosto de 1939 Alemania y la URSS firman un pacto de no agresión; el 22 de junio de 1941 Alemania invade la URSS. "
     "El régimen de Hitler (nazismo) tenía partido único, propaganda estatal y una ideología racista; el de Stalin (comunismo soviético) tenía partido único y una economía dirigida por el Estado; "
     "las democracias occidentales (Reino Unido, Francia y Estados Unidos) tenían elecciones, varios partidos y prensa con libertad. "
     "Fuente A, discurso de un funcionario del régimen alemán, 1938 (de ejemplo): «Nuestro pueblo es uno solo y los enemigos de la nación serán apartados.» "
     "Fuente B, editorial de un diario británico, 1939 (de ejemplo): «Un gobierno que prohíbe la prensa libre no habla en nombre de su pueblo.» "
     "Fuente C, informe de un funcionario soviético, 1937 (de ejemplo): «El Partido vigila a los enemigos del pueblo trabajador y guía al país hacia el futuro.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre el enfrentamiento entre los regímenes de Hitler, Stalin y las democracias: quién habla, cuándo, para qué y qué prueba realmente.",
    prior=["Sé qué es una fuente y qué es la procedencia.", "Conozco los bandos de la Segunda Guerra Mundial.", "Sé que una opinión no es lo mismo que un hecho."],
    explain=[
        "La procedencia de una fuente responde a tres preguntas: quién la produjo, cuándo y con qué propósito. Un discurso oficial no es una descripción neutral: muestra lo que un gobierno quería que se creyera. La propaganda es el uso planificado de mensajes para convencer a la población, y los regímenes de partido único la controlaban con facilidad porque no había prensa libre.",
        "Los regímenes de Hitler y de Stalin tenían rasgos parecidos, como el partido único, pero ideologías opuestas: una racista y nacionalista, la otra comunista. Las democracias occidentales se distinguían por elecciones, varios partidos y prensa libre. El pacto de 1939 entre Alemania y la URSS fue un acuerdo práctico entre rivales: se rompió en 1941 cuando Alemania invadió la URSS.",
        "Al comparar fuentes de distinta procedencia conviene no concluir más de lo que muestran. Un editorial es una opinión, un informe oficial muestra la versión del Estado y ninguno prueba por sí solo qué le ocurrió a las personas. Para acercarse a los hechos se contrastan fuentes y se pregunta qué otra fuente faltaría.",
    ],
    vocab=[("procedencia", "quién produjo una fuente, cuándo y con qué propósito"), ("propaganda", "uso planificado de mensajes para convencer a la población"), ("partido único", "régimen en que solo un partido puede gobernar"), ("pacto de no agresión", "acuerdo en que dos países prometen no atacarse"), ("editorial", "texto de un diario que expresa su opinión")],
    worked=[
        ("Identificar la procedencia", "¿Quién escribió la fuente B, cuándo y qué tipo de texto es?", ["Leo el encabezado: un diario británico, 1939.", "Es un editorial, o sea una opinión."], "Un diario británico, en 1939; es una opinión (editorial)"),
        ("Medir lo que prueba una fuente", "¿La fuente A prueba que ciertas personas fueron apartadas?", ["Es un discurso de un funcionario del régimen.", "Muestra lo que el régimen decía que haría, no lo que ocurrió."], "No; prueba la intención declarada, no los hechos"),
    ],
    mistakes=[("Tomar un discurso oficial como una descripción exacta de lo ocurrido.", "Se olvida que el régimen controlaba el mensaje para convencer.", "Pregunta quién habla y para qué, y busca otra fuente para contrastar."),
              ("Creer que el pacto de 1939 muestra que Hitler y Stalin compartían la misma ideología.", "Se confunde un acuerdo práctico con una coincidencia de ideas.", "Recuerda que sus ideologías eran opuestas y que Alemania invadió la URSS en 1941.")],
    T=[
        ("{F} ¿Cuándo firmaron Alemania y la URSS el pacto de no agresión?", "El 23 de agosto de 1939", "La ficha da esa fecha."),
        ("{F} ¿Qué tipo de fuente es la fuente B?", "Un editorial de un diario británico", "El encabezado de la fuente B lo indica."),
        ("{F} ¿Qué rasgo político comparten los regímenes de Hitler y de Stalin según la ficha?", "El partido único", "La ficha lo señala en ambos casos."),
        ("=", "{F} ¿Cuántos años pasaron entre el pacto de no agresión y la invasión alemana de la URSS?", "1941-1939", "Se resta el año del pacto al de la invasión.", " años"),
        ("{F} La fuente C es un informe de un funcionario soviético. ¿Qué clase de fuente es? A) Una fuente oficial del régimen B) El testimonio de una víctima", "A) Una fuente oficial del régimen", "Su autor es un funcionario del Estado que describe lo que el régimen quiere mostrar."),
        ("{F} ¿Qué pregunta ayuda a analizar la procedencia de la fuente A? A) ¿Quién habló, cuándo y con qué propósito? B) ¿Cuántas palabras tiene la frase?", "A) ¿Quién habló, cuándo y con qué propósito?", "La procedencia se define por autor, fecha y propósito."),
        ("{F} La fuente B critica a los gobiernos sin prensa libre. ¿Qué rasgo de las democracias defiende? A) La prensa libre B) El partido único", "A) La prensa libre", "La ficha asigna prensa libre a las democracias occidentales."),
        ("{F} ¿Qué muestra el pacto de 1939? A) Un acuerdo práctico entre rivales ideológicos B) Que ambos regímenes tenían la misma ideología", "A) Un acuerdo práctico entre rivales ideológicos", "Alemania invadió la URSS en 1941, lo que confirma la rivalidad."),
        ("{F} Tienes la fuente A (régimen) y la fuente B (diario). ¿Qué haces primero para compararlas? A) Preguntar quién escribió cada una y con qué propósito B) Quedarte con la que coincide con tu opinión", "A) Preguntar quién escribió cada una y con qué propósito", "Sin conocer la procedencia no se puede comparar el valor de las fuentes."),
        ("{F} ¿Por qué la fuente A no prueba por sí sola qué ocurrió con los «enemigos de la nación»?", "Porque es un discurso del régimen que muestra lo que quería decir, no los hechos", "Una fuente oficial expresa una intención, y los hechos requieren más evidencias."),
        ("{F} Un compañero dice: «La fuente B es neutral porque es un diario». ¿Qué corrección haces? A) Un editorial expresa una opinión y hay que ver su contexto B) Es correcto, porque un diario solo informa hechos", "A) Un editorial expresa una opinión y hay que ver su contexto", "El editorial es un texto de opinión, no una descripción neutral."),
        ("{F} ¿Qué conclusión sobre las fuentes A y C es proporcional a lo que muestran? A) Ambos regímenes presentaban a sus enemigos como una amenaza en sus discursos oficiales B) Todos los habitantes de ambos países pensaban igual", "A) Ambos regímenes presentaban a sus enemigos como una amenaza en sus discursos oficiales", "Afirmar que todos pensaban igual generaliza a toda la población, algo que las fuentes no muestran."),
        ("{F} ¿Qué fuente permitiría contrastar mejor la fuente A? A) El diario privado de una persona que vivió en esa ciudad B) Otro discurso del mismo funcionario", "A) El diario privado de una persona que vivió en esa ciudad", "Otra procedencia ofrece otra mirada; repetir al mismo autor no contrasta."),
    ],
    ctx=("Un trabajo escolar afirma: «Como lo dijo el funcionario en 1938, todos los habitantes apoyaban al régimen». ¿Qué falla tiene? A) Usa una fuente oficial para afirmar lo que pensaba toda la población B) Cita una fecha antigua", "A) Usa una fuente oficial para afirmar lo que pensaba toda la población", "Un discurso oficial no demuestra la opinión de todos."),
    sc=[("¿Qué es la propaganda?", "El uso planificado de mensajes para convencer a la población", "Así se define en la clase."),
        ("¿Qué tres preguntas forman la procedencia?", "Quién la produjo, cuándo y con qué propósito", "Así se define en la explicación."),
        ("En Historia: ¿qué es un pacto de no agresión?", "Un acuerdo en que dos países prometen no atacarse", "Así se define en el vocabulario de la clase.")],
    op=("Elige dos de las tres fuentes de la ficha. Completa una tabla con cuatro columnas: quién la produjo, cuándo, con qué propósito y qué NO prueba. Después escribe una frase que compare las dos fuentes sin concluir más de lo que muestran. {F}",
        "Fuente A: funcionario del régimen alemán, 1938, propósito de convencer; no prueba qué pasó con las personas apartadas. Fuente B: diario británico, 1939, opinión; no prueba cómo era la vida en otro país. Frase: «Ambas fuentes expresan visiones opuestas sobre la prensa y el poder».",
        ["completa las cuatro columnas para ambas fuentes", "indica un límite de cada una", "la frase no generaliza"], ["tabla de dos fuentes", "frase comparativa"], ["tomar el discurso como un hecho", "no indicar qué no prueba la fuente"],
        "Pide que diga qué fuente de otra procedencia agregaría para contrastar."),
    reinforce="Explica a alguien de tu casa por qué un discurso del gobierno no basta para saber qué pasó realmente.",
    extend="Observa un aviso o una publicidad de tu entorno y di quién lo produjo, para qué y qué no te prueba.",
)

# ================================================================ OA 03, clase 3
F = ("Ficha 3 (hechos y tres relatos de ejemplo escritos para este cuaderno). "
     "Hechos: la guerra se libró en Europa, África del Norte, Asia, el océano Pacífico y el océano Atlántico, por eso se llama mundial; entre 1940 y 1941 la aviación alemana bombardeó ciudades británicas, entre ellas Londres; "
     "una ciudad es una escala local, un país es una escala nacional y todo el planeta es una escala mundial. "
     "Relato 1, diario de una niña de una ciudad bombardeada, 1940 (de ejemplo): «Dormimos en el refugio del subterráneo; por la mañana vimos una calle sin casas.» "
     "Relato 2, comunicado de un ministerio de guerra, 1944 (de ejemplo): «Nuestras fuerzas avanzaron 20 km por día durante 5 días; las pérdidas fueron menores a lo previsto.» "
     "Relato 3, testimonio de una familia refugiada, 1945 (de ejemplo): «Salimos con una maleta cuando llegó el ejército; viajamos semanas buscando un lugar donde quedarnos.»")
build(
    OA, 3, F,
    use="Aprenderé a comparar cómo vivieron la guerra distintos actores (civiles, gobiernos, refugiados) y a mirar el mismo proceso en escala local, nacional y mundial.",
    prior=["Sé interrogar la procedencia de una fuente.", "Conozco los bandos de la guerra.", "Sé que un hecho se puede mirar desde varias escalas."],
    explain=[
        "Una perspectiva es el punto de vista desde el cual alguien cuenta un hecho. En la Segunda Guerra Mundial, un gobierno que informa de un avance, una niña que vive un bombardeo y una familia que debe dejar su casa cuentan la misma guerra de modo muy distinto. Comparar perspectivas no significa que todas valgan lo mismo como prueba, sino entender qué muestra y qué calla cada una.",
        "La escala es el tamaño del espacio que se estudia. En escala local se observa una ciudad bombardeada o una familia desplazada; en escala nacional, las decisiones de un gobierno; en escala mundial, la extensión planetaria del conflicto, que abarcó varios continentes y océanos. Un desplazamiento forzado es obligar a las personas a abandonar su lugar de vida, y los bombardeos aumentaron mucho las víctimas civiles.",
        "Cuando comparas, busca qué cambia y qué se repite entre las fuentes. Un comunicado oficial suele resaltar avances y minimizar pérdidas. Un testimonio civil muestra la experiencia concreta, pero no el conjunto del país. Un error común es tomar una sola perspectiva como si fuera la guerra completa.",
    ],
    vocab=[("perspectiva", "punto de vista desde el cual alguien cuenta un hecho"), ("escala", "tamaño del espacio que se estudia: local, nacional o mundial"), ("desplazamiento forzado", "obligar a personas a abandonar el lugar donde viven"), ("población civil", "personas que no son soldados"), ("comunicado", "mensaje oficial de una institución")],
    worked=[
        ("Reconocer la escala", "El relato 1 describe una calle sin casas tras un bombardeo. ¿En qué escala se mueve?", ["Habla de una calle y de una ciudad.", "No describe un país entero ni el planeta."], "Escala local"),
        ("Calcular un dato del relato", "El comunicado dice 20 km por día durante 5 días. ¿Cuántos kilómetros avanzaron en total?", ["Multiplico los km por día por los días.", "20 × 5 = 100."], "100 km"),
    ],
    mistakes=[("Usar un comunicado oficial como si mostrara toda la experiencia de la guerra.", "Se olvida que el gobierno resalta lo que le conviene.", "Contrasta el comunicado con el testimonio de personas civiles."),
              ("Concluir que, porque un testimonio civil habla de una ciudad, así vivió todo el país.", "Se pasa de la escala local a la nacional sin evidencia.", "Escribe «en esta ciudad» y busca fuentes de otras escalas.")],
    T=[
        ("{F} ¿Qué dos océanos nombra la ficha como escenarios de la guerra?", "El Pacífico y el Atlántico", "La ficha los menciona entre los escenarios del conflicto."),
        ("{F} ¿Quién produjo el relato 2?", "Un ministerio de guerra", "El encabezado del relato 2 lo indica."),
        ("{F} ¿Qué vivió la familia del relato 3?", "Un desplazamiento forzado: tuvo que dejar su lugar de vida", "El relato describe salir con una maleta y buscar dónde quedarse."),
        ("=", "{F} Una unidad del relato 2 avanzó 20 km por día. ¿Cuántos kilómetros avanzó en 3 días?", "20*3", "Se multiplica el avance diario por los días.", " km"),
        ("{F} ¿Qué ciudad británica nombra la ficha entre las bombardeadas por la aviación alemana? A) Londres B) Varsovia", "A) Londres", "La ficha nombra Londres, bombardeada entre 1940 y 1941."),
        ("{F} ¿Qué relato muestra la experiencia de una persona civil durante un bombardeo? A) El relato 1 B) El relato 2", "A) El relato 1", "Es el diario de una niña en una ciudad bombardeada."),
        ("{F} El relato 2 dice que las pérdidas fueron «menores a lo previsto». ¿Qué perspectiva muestra? A) La de un gobierno que informa de su avance B) La de una persona refugiada", "A) La de un gobierno que informa de su avance", "El autor es un ministerio y resalta el avance."),
        ("{F} Una investigación estudia cómo la guerra alcanzó Europa, África del Norte, Asia y los océanos. ¿Qué escala usa? A) Una escala mundial B) Una escala local", "A) Una escala regional amplia, de varios países", "Varios continentes y océanos corresponden a la escala mundial, no a una ciudad ni a una familia."),
        ("{F} Se quiere explicar por qué la guerra fue mundial. ¿Qué dato de la ficha ayuda más? A) La guerra se libró en Europa, África del Norte, Asia y los océanos B) Los bombardeos de 1940 a Londres", "A) La guerra se libró en Europa, África del Norte, Asia y los océanos", "La extensión por varios continentes y océanos explica el carácter mundial."),
        ("{F} ¿Por qué el comunicado y el diario de la niña dan imágenes distintas de la guerra?", "Porque cada uno cuenta desde su perspectiva: el gobierno resalta el avance y la niña cuenta lo que vivió", "La procedencia y el propósito de cada texto cambian lo que muestran."),
        ("{F} Un compañero dice: «El relato 1 prueba que en toda Gran Bretaña las personas dormían en refugios cada noche». ¿Qué corrección haces? A) Solo prueba lo vivido por esa niña en su ciudad B) Prueba lo que hizo todo el país", "A) Solo prueba lo vivido por esa niña en su ciudad", "Un relato individual no se puede generalizar a todo un país."),
        ("{F} ¿Qué combinación de fuentes ofrece una imagen más completa? A) El comunicado, el diario de la niña y el testimonio de la familia refugiada B) Solo el comunicado", "A) El comunicado, el diario de la niña y el testimonio de la familia refugiada", "Reúne perspectivas y escalas distintas, mientras que una sola da una visión parcial."),
        ("{F} ¿Qué afirmación se sostiene mejor? A) Los civiles sufrieron la guerra de modos distintos, como el bombardeo o el desplazamiento forzado B) La guerra solo afectó a los soldados", "A) Los civiles sufrieron la guerra de modos distintos, como el bombardeo o el desplazamiento forzado", "Los relatos 1 y 3 muestran dos experiencias civiles diferentes."),
    ],
    ctx=("Un grupo prepara un panel con el título «Así vivió la guerra todo el mundo» y solo incluye el comunicado del ministerio. ¿Qué falta? A) Perspectivas de personas civiles y otras escalas B) Un mapa más grande", "A) Perspectivas de personas civiles y otras escalas", "Un solo comunicado no representa la experiencia de todas las personas."),
    sc=[("¿Qué es una perspectiva?", "El punto de vista desde el cual alguien cuenta un hecho", "Así se define en la clase."),
        ("¿Qué es un desplazamiento forzado?", "Obligar a personas a abandonar el lugar donde viven", "Así se define en el vocabulario."),
        ("=", "En un ejemplo, una ciudad de 40.000 habitantes tiene 10.000 personas sin hogar tras un bombardeo. ¿Cuántas conservan su hogar?", "40000-10000", "Se resta la cifra de personas sin hogar al total.", " personas")],
    op=("Compara dos de los tres relatos de la ficha en una tabla: perspectiva, escala (local, nacional o mundial), qué muestra y qué no muestra. Termina con una frase que explique qué ganarías al leer los dos juntos. {F}",
        "Relato 1: perspectiva de una niña civil, escala local, muestra el bombardeo, no muestra la decisión del gobierno. Relato 2: perspectiva del ministerio, escala nacional, muestra avance, no muestra la experiencia de las personas. Frase: «Juntos muestran el avance y su costo para los civiles».",
        ["indica perspectiva y escala de cada relato", "señala qué no muestra cada uno", "la frase integra ambos"], ["tabla de dos relatos", "frase final"], ["decir que un relato local vale para todo el país", "no mencionar el límite de cada relato"],
        "Pide que nombre un relato más que haría falta para entender la escala mundial."),
    reinforce="Cuenta a alguien un mismo hecho de tu día desde dos puntos de vista distintos y explica qué cambia.",
    extend="Busca en un mapa del mundo los continentes que nombra la ficha y anota cuáles son.",
)

# ================================================================ OA 03, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; hechos). "
     "Causas de la guerra: el tratado de Versalles, 1919; la Gran Depresión, desde 1929, que dejó a millones sin trabajo; la llegada de Hitler al gobierno de Alemania en enero de 1933; "
     "las agresiones de Japón, Italia y Alemania entre 1931 y 1938; el apaciguamiento; una Liga de las Naciones sin ejército. "
     "Cambios durante la guerra: se movilizaron economías enteras (guerra total); los bombardeos alcanzaron ciudades; apareció un arma nueva, la bomba atómica, lanzada sobre Hiroshima el 6 de agosto de 1945 y sobre Nagasaki el 9 de agosto de 1945. "
     "Fin de la guerra: en Europa terminó el 8 de mayo de 1945; Japón firmó su rendición el 2 de septiembre de 1945. "
     "Continuidades: varias potencias europeas conservaban colonias; seguía la rivalidad entre el comunismo soviético y las democracias occidentales.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la Segunda Guerra Mundial con los cambios que produjo y con lo que siguió igual, y a distinguir causas de largo plazo de un detonante.",
    prior=["Sé situar los hechos de entreguerras en el tiempo.", "Sé comparar perspectivas.", "Sé que un hecho tiene más de una causa."],
    explain=[
        "Explicar una guerra con una sola causa es un error. La Segunda Guerra Mundial tuvo causas de largo plazo, como el tratado de Versalles, la Gran Depresión, el ascenso de regímenes que querían expandirse y la debilidad de la Liga de las Naciones, y un detonante: la invasión de Polonia en 1939. Una explicación multicausal combina varias causas y dice cuál pesó más.",
        "La guerra produjo cambios profundos. Fue una guerra total, porque movilizó la economía y a la población, y por eso los civiles quedaron en el centro del conflicto con bombardeos y desplazamientos. La bomba atómica, usada en Hiroshima y Nagasaki en agosto de 1945, mostró un poder de destrucción nuevo y abrió un debate que dura hasta hoy.",
        "También hubo continuidades: muchas potencias europeas mantenían colonias y la rivalidad entre el comunismo soviético y las democracias occidentales siguió después de 1945. Un cambio no borra todo lo anterior. Para relacionar causas y consecuencias conviene ordenar los hechos en el tiempo y no afirmar que algo fue causa solo porque ocurrió antes.",
    ],
    vocab=[("multicausal", "explicación que combina varias causas"), ("detonante", "hecho que desencadena algo que ya tenía causas previas"), ("guerra total", "guerra que moviliza la economía y a toda la población"), ("bomba atómica", "arma de destrucción masiva, lanzada en Hiroshima y Nagasaki en 1945"), ("continuidad", "algo que sigue igual a pesar de un cambio")],
    worked=[
        ("Distinguir causa de largo plazo y detonante", "¿La Gran Depresión fue una causa de largo plazo o un detonante de la guerra?", ["Comenzó en 1929, diez años antes de 1939.", "Preparó el contexto, pero no fue el hecho inmediato."], "Causa de largo plazo"),
        ("Medir un intervalo", "¿Cuántos días pasaron entre el bombardeo atómico de Hiroshima y el de Nagasaki?", ["Tomo las fechas: 6 y 9 de agosto.", "Resto: 9 − 6 = 3."], "3 días"),
    ],
    mistakes=[("Decir que la invasión de Polonia fue la única causa de la guerra.", "Se confunde detonante con causa total.", "Agrega las causas de largo plazo de la ficha."),
              ("Creer que si algo ocurrió antes de la guerra entonces la causó.", "Se confunde coincidencia en el tiempo con causa.", "Busca evidencia de que ese hecho influyó en las decisiones.")],
    T=[
        ("{F} ¿En qué fecha terminó la guerra en Europa según la ficha?", "El 8 de mayo de 1945", "La ficha lo indica."),
        ("{F} ¿Qué arma nueva nombra la ficha entre los cambios de la guerra?", "La bomba atómica", "Aparece en la lista de cambios."),
        ("{F} ¿Qué ciudad fue bombardeada el 9 de agosto de 1945?", "Nagasaki", "La ficha da esa ciudad para esa fecha."),
        ("=", "{F} ¿Cuántos años pasaron entre la llegada de Hitler al gobierno y la invasión de Polonia?", "1939-1933", "Se resta el año de su llegada al del inicio de la guerra.", " años"),
        ("{F} ¿Qué hecho puso fin a la guerra en Asia según la ficha? A) La firma de la rendición de Japón el 2 de septiembre de 1945 B) El fin de la guerra en Europa el 8 de mayo de 1945", "A) La firma de la rendición de Japón el 2 de septiembre de 1945", "El 8 de mayo terminó la guerra solo en Europa; Japón firmó su rendición el 2 de septiembre."),
        ("{F} ¿Cuál de estos hechos fue el detonante de la guerra en Europa? A) La invasión alemana de Polonia en 1939 B) El tratado de Versalles de 1919", "A) La invasión alemana de Polonia en 1939", "Fue el hecho que desencadenó la guerra; Versalles es una causa de largo plazo."),
        ("{F} El gobierno de un país organiza toda la economía y a toda su población para la guerra. ¿Qué cambio de la ficha ilustra? A) Guerra total B) Apaciguamiento", "A) Guerra total", "Movilizar economía y población es la guerra total."),
        ("{F} Después de 1945 varias potencias europeas siguen gobernando colonias. ¿Qué es eso? A) Una continuidad B) Un cambio causado por la bomba atómica", "A) Una continuidad", "La ficha dice que ya tenían colonias antes y las conservaban."),
        ("{F} ¿Qué relación sostiene la ficha entre la Gran Depresión y la guerra? A) Fue una de varias causas de largo plazo B) Fue la única causa de la guerra", "A) Fue una de varias causas de largo plazo", "La ficha lista varias causas, no una sola."),
        ("{F} ¿Por qué se dice que los civiles quedaron en el centro de la guerra?", "Porque los bombardeos alcanzaron ciudades y la economía y la población fueron movilizadas", "La ficha describe la guerra total y los bombardeos a ciudades."),
        ("{F} Un compañero dice: «Como Versalles fue en 1919, solo él causó la guerra». ¿Qué corrección haces? A) Fue una causa entre varias, junto con la Depresión, las agresiones y la debilidad de la Liga B) Tiene razón porque es la más antigua", "A) Fue una causa entre varias, junto con la Depresión, las agresiones y la debilidad de la Liga", "Ser más antigua no la hace la única causa."),
        ("{F} ¿Qué cambio trajo la bomba atómica a la guerra? A) Un poder de destrucción nuevo para las ciudades B) Que la guerra terminó en Europa", "A) Un poder de destrucción nuevo para las ciudades", "La ficha la describe como un arma nueva lanzada sobre dos ciudades; el fin en Europa es del 8 de mayo."),
        ("{F} ¿Cuál es la mejor síntesis? A) La guerra tuvo causas de largo plazo y un detonante, y produjo cambios como la guerra total y la bomba atómica con continuidades como las colonias B) Todo cambió el 1 de septiembre de 1939", "A) La guerra tuvo causas de largo plazo y un detonante, y produjo cambios como la guerra total y la bomba atómica con continuidades como las colonias", "Combina causas, cambios y continuidades."),
    ],
    ctx=("Una infografía dice: «Todo empezó con el bombardeo atómico de 1945». ¿Qué error tiene? A) Pone una consecuencia de la guerra como si fuera su origen B) Omite las colonias europeas", "A) Pone una consecuencia de la guerra como si fuera su origen", "La bomba atómica se usó al final de la guerra, no al comienzo."),
    sc=[("¿Qué es un detonante?", "El hecho que desencadena algo que ya tenía causas previas", "Así se define en la clase."),
        ("¿Qué es la guerra total?", "Una guerra que moviliza la economía y a toda la población", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una continuidad?", "Algo que sigue igual a pesar de un cambio", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja un esquema con la guerra al centro. A la izquierda escribe tres causas de largo plazo de la ficha, arriba el detonante, a la derecha dos cambios y abajo una continuidad. Escribe una frase con «contribuyó a» que evite decir que algo fue la única causa. {F}",
        "Causas: Versalles, Gran Depresión, agresiones y apaciguamiento. Detonante: invasión de Polonia. Cambios: guerra total, bomba atómica. Continuidad: colonias europeas. Frase: «La Gran Depresión contribuyó a la inestabilidad, pero no fue la única causa».",
        ["distingue causa de largo plazo y detonante", "incluye cambios y una continuidad", "evita la causa única"], ["esquema", "frase con «contribuyó a»"], ["poner el detonante como causa única", "mezclar cambios con causas"],
        "Pide que explique por qué ocurrir antes no prueba que algo sea causa."),
    reinforce="Explica en voz alta la diferencia entre una causa de largo plazo y un detonante con un ejemplo de la guerra.",
    extend="Piensa en una consecuencia de algo que te pasó y di qué causas previas la hicieron posible.",
)

# ================================================================ OA 03, clase 5
F = ("Ficha 5 (hechos y tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Hechos: en septiembre de 1935 Alemania aprobó las leyes de Núremberg, que quitaban derechos a las personas judías; el 9 y 10 de noviembre de 1938 hubo ataques organizados contra negocios y templos judíos (Noche de los Cristales Rotos); "
     "el 20 de enero de 1942 se realizó la conferencia de Wannsee, donde funcionarios del Estado coordinaron la persecución; el exterminio judío (Holocausto) causó la muerte de alrededor de seis millones de personas judías de Europa. "
     "También fueron perseguidos el pueblo romaní, personas con discapacidad y opositores políticos. "
     "El jurista Raphael Lemkin propuso la palabra genocidio en 1944 y la ONU aprobó una convención contra el genocidio el 9 de diciembre de 1948. "
     "Fuente A, ley de un régimen, 1935 (de ejemplo): «Se establece qué personas pueden ser ciudadanas.» "
     "Fuente B, informe de un funcionario, 1942 (de ejemplo): «Se coordinó el traslado de población entre varias oficinas del Estado.» "
     "Fuente C, testimonio de una persona sobreviviente, 1946 (de ejemplo): «Perdimos la casa, el trabajo y a nuestra familia.»")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre el genocidio y la persecución de civiles en la guerra, con una tesis, evidencia de varias fuentes y un límite reconocido.",
    prior=["Sé interrogar la procedencia de una fuente.", "Sé comparar perspectivas.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Un genocidio es un crimen que busca destruir total o parcialmente a un grupo humano por su origen, religión o identidad. El exterminio judío, o Holocausto, fue ejecutado por el Estado alemán con apoyo de funcionarios y cómplices; murieron alrededor de seis millones de personas judías de Europa. También fueron perseguidos el pueblo romaní, personas con discapacidad y opositores políticos. Es un tema grave que se estudia con respeto a las víctimas.",
        "Una interpretación documentada tiene una tesis, es decir, una idea que se defiende, y evidencias de fuentes de distinta procedencia. Por ejemplo, las leyes de 1935 muestran cómo se quitaron derechos, el informe de 1942 muestra que el Estado coordinó la persecución, y el testimonio de una persona sobreviviente muestra la experiencia de las víctimas. Cada fuente prueba algo distinto.",
        "Una buena tesis reconoce sus límites: una ley no prueba lo que pasó después, y un testimonio no cuenta todo el proceso. El mundo reaccionó creando la palabra genocidio en 1944 y una convención de la ONU en 1948. Si una persona de tu entorno sufre acoso o discriminación, lo mejor es contárselo a una persona adulta de confianza.",
    ],
    vocab=[("genocidio", "crimen que busca destruir a un grupo humano por su origen, religión o identidad"), ("Holocausto", "exterminio de personas judías de Europa por el Estado alemán"), ("tesis", "idea central que se defiende con evidencias"), ("testimonio", "relato de una persona que vivió un hecho"), ("convención", "tratado internacional que obliga a los Estados que lo firman")],
    worked=[
        ("Elegir la evidencia adecuada", "¿Qué fuente de la ficha muestra la experiencia de una víctima: A, B o C?", ["La fuente C es un testimonio de una persona sobreviviente.", "Las otras dos vienen de funcionarios."], "La fuente C"),
        ("Calcular un intervalo", "¿Cuántos años pasaron entre las leyes de Núremberg y la conferencia de Wannsee?", ["Tomo 1935 y 1942.", "Resto: 1942 − 1935 = 7."], "7 años"),
    ],
    mistakes=[("Escribir una cifra de víctimas sin fuente ni cuidado.", "Se repiten números sin saber de dónde vienen.", "Usa solo cifras de fuentes confiables y, si dudas, di «millones de personas»."),
              ("Afirmar que un testimonio prueba todo el proceso.", "Se generaliza desde un caso individual.", "Escribe qué prueba el testimonio y qué fuente falta para el resto.")],
    T=[
        ("{F} ¿Cómo se llama el exterminio de personas judías de Europa?", "Holocausto", "La ficha lo nombra así."),
        ("{F} ¿Qué propuso Raphael Lemkin en 1944?", "La palabra genocidio", "La ficha lo registra."),
        ("{F} ¿En qué fecha aprobó la ONU la convención contra el genocidio?", "El 9 de diciembre de 1948", "La ficha da esa fecha."),
        ("=", "{F} ¿Cuántos años pasaron entre la Noche de los Cristales Rotos y la convención de la ONU contra el genocidio?", "1948-1938", "Se resta el año de los ataques al de la convención.", " años"),
        ("{F} ¿Cuál de estos hechos fue un ataque organizado contra negocios y templos judíos? A) La Noche de los Cristales Rotos B) La conferencia de Wannsee", "A) La Noche de los Cristales Rotos", "La ficha la ubica el 9 y 10 de noviembre de 1938; Wannsee fue una reunión de funcionarios en 1942."),
        ("{F} ¿Qué fuente de la ficha muestra que el Estado coordinó la persecución? A) La fuente B, el informe de 1942 B) La fuente C, el testimonio de 1946", "A) La fuente B, el informe de 1942", "Es un informe de un funcionario sobre coordinación entre oficinas del Estado."),
        ("{F} Una tesis dice: «La persecución fue organizada por el Estado, no fue un hecho aislado». ¿Qué fuente la apoya mejor? A) El informe de 1942 B) El testimonio de 1946", "A) El informe de 1942", "Muestra coordinación entre oficinas del Estado."),
        ("{F} Alguien dice que el Holocausto fue la única persecución del régimen. ¿Qué dato de la ficha lo corrige? A) También fueron perseguidos el pueblo romaní, personas con discapacidad y opositores B) Fue una decisión tomada en 1942", "A) También fueron perseguidos el pueblo romaní, personas con discapacidad y opositores", "La ficha nombra otros grupos perseguidos."),
        ("{F} ¿Por qué una buena interpretación necesita fuentes de distinta procedencia?", "Porque cada fuente prueba algo distinto y juntas dan una explicación más completa", "Ley, informe y testimonio muestran aspectos diferentes."),
        ("{F} Un compañero dice: «El testimonio de 1946 prueba todo lo que ocurrió en Europa». ¿Qué corrección haces? A) Prueba la experiencia de esa persona, pero se necesitan más fuentes B) Tiene razón porque la persona estuvo ahí", "A) Prueba la experiencia de esa persona, pero se necesitan más fuentes", "Un testimonio es valioso, pero no cubre todo el proceso."),
        ("{F} ¿Cuál tesis está mejor documentada con la ficha? A) El Estado quitó derechos por ley desde 1935 y coordinó la persecución hasta 1942 B) Todos los ciudadanos apoyaron las decisiones", "A) El Estado quitó derechos por ley desde 1935 y coordinó la persecución hasta 1942", "Se apoya en las fuentes A y B, mientras que afirmar que todos apoyaron no tiene evidencia en la ficha."),
        ("{F} ¿Qué límite debe reconocer quien use solo las fuentes A y B? A) No muestran la experiencia de las víctimas B) No muestran la intención del Estado", "A) No muestran la experiencia de las víctimas", "Ambas vienen de funcionarios; falta la voz de las víctimas."),
        ("{F} ¿Qué hizo la comunidad internacional después de la guerra frente al genocidio? A) Creó la palabra genocidio y aprobó una convención en 1948 B) Aprobó una convención en 1938, antes de la guerra", "A) Creó la palabra genocidio y aprobó una convención en 1948", "La ficha registra ambos hechos, en 1944 y en 1948."),
    ],
    ctx=("Un estudiante escribe: «Hubo millones de víctimas, por eso no hace falta usar fuentes». ¿Qué falla tiene? A) Una afirmación histórica necesita evidencias, aunque el hecho sea grave B) Debería citar una cifra distinta", "A) Una afirmación histórica necesita evidencias, aunque el hecho sea grave", "La historia se construye con fuentes; la gravedad no reemplaza la evidencia."),
    sc=[("¿Qué es un genocidio?", "Un crimen que busca destruir a un grupo humano por su origen, religión o identidad", "Así se define en la explicación."),
        ("¿Qué es una tesis?", "La idea central que se defiende con evidencias", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es el Holocausto?", "El exterminio de personas judías de Europa por el Estado alemán", "Así se define en el vocabulario de la clase.")],
    op=("Escribe un párrafo de cinco a siete líneas con una tesis sobre cómo el Estado organizó la persecución. Usa dos de las tres fuentes de la ficha y di qué prueba cada una y qué límite tiene. Trátalo con respeto a las víctimas y sin describir hechos violentos. {F}",
        "Tesis: «El Estado quitó derechos por ley en 1935 y coordinó la persecución en 1942». Evidencia: la ley (A) y el informe (B). Límite: ninguna de las dos muestra la experiencia de las víctimas; falta un testimonio como la fuente C.",
        ["formula una tesis clara", "usa dos fuentes con su aporte", "reconoce un límite"], ["párrafo escrito", "dos fuentes citadas"], ["afirmar sin fuente", "usar una cifra no confirmada"],
        "Pide que explique qué fuente agregaría para cubrir el límite."),
    reinforce="Explica con tus palabras qué es una tesis y por qué necesita evidencias.",
    extend="Si alguien de tu entorno sufre acoso o discriminación, piensa a qué persona adulta de confianza se lo contarías.",
)

# ================================================================ OA 03, clase 6
F = ("Ficha 6 (hechos y dos posiciones de ejemplo escritas para este cuaderno). "
     "Hechos: en noviembre de 1945 comenzaron en Núremberg los juicios a dirigentes del régimen alemán, donde se usó la idea de «crímenes contra la humanidad»; "
     "Hiroshima fue bombardeada el 6 de agosto de 1945 y Nagasaki el 9 de agosto de 1945; Japón anunció su rendición el 15 de agosto de 1945. "
     "Posición 1 (de ejemplo): «La bomba atómica acortó la guerra y evitó una invasión, que habría causado más muertes.» "
     "Posición 2 (de ejemplo): «La bomba mató a gran cantidad de civiles y existían otras alternativas para terminar la guerra.» "
     "Criterios de un buen debate: formular un argumento, apoyarlo con evidencia, considerar un contraargumento y respetar a quien piensa distinto.")
build(
    OA, 6, F,
    use="Aprenderé a debatir sobre las consecuencias y los límites de la guerra, como la justicia después de los crímenes y el uso de la bomba atómica, con argumentos y respeto.",
    prior=["Sé construir una tesis con evidencias.", "Conozco la bomba atómica y el genocidio.", "Sé que una opinión se apoya en razones."],
    explain=[
        "Un debate histórico no busca que alguien gane, sino que cada persona exponga argumentos apoyados en evidencias y escuche los de otros. Un argumento tiene una afirmación, una razón y una evidencia. Un contraargumento es una razón que va en contra de lo que se afirma, y un buen debate lo considera en vez de ignorarlo.",
        "Los juicios de Núremberg de 1945 fueron un intento de responder a los crímenes de la guerra con justicia y leyes: se juzgó a dirigentes por crímenes contra la humanidad. Sobre la bomba atómica hay posiciones distintas: unos sostienen que acortó la guerra, otros que mató a civiles y que había alternativas. Ambas posiciones usan hechos, pero los interpretan de modo diferente.",
        "Para debatir con rigor, separa lo que está probado, como las fechas, de lo que se interpreta, como lo que habría ocurrido si no se hubiera lanzado la bomba. Un límite importante: nadie puede probar con certeza lo que no ocurrió. Reconocer esos límites hace más fuerte tu argumento.",
    ],
    vocab=[("argumento", "afirmación apoyada en una razón y en una evidencia"), ("contraargumento", "razón que va en contra de una afirmación"), ("crímenes contra la humanidad", "delitos graves contra la población civil, juzgados en Núremberg"), ("evidencia", "dato o fuente que apoya una afirmación"), ("interpretación", "explicación que se da a unos hechos")],
    worked=[
        ("Separar hecho e interpretación", "«Nagasaki fue bombardeada el 9 de agosto de 1945» y «la bomba era la única alternativa». ¿Cuál es un hecho?", ["La primera frase tiene fecha y se puede comprobar.", "La segunda es una interpretación sobre lo que pudo ocurrir."], "La primera es un hecho"),
        ("Calcular un plazo", "¿Cuántos días pasaron entre el bombardeo de Nagasaki y el anuncio de rendición de Japón?", ["Tomo 9 y 15 de agosto.", "Resto: 15 − 9 = 6."], "6 días"),
    ],
    mistakes=[("Defender una posición sin considerar el contraargumento.", "Se piensa que reconocer otra razón debilita la propia.", "Presenta la razón contraria y explica por qué tu evidencia pesa más."),
              ("Presentar una hipótesis sobre lo que no ocurrió como si fuera un hecho.", "Se confunde lo probable con lo probado.", "Escribe «es posible que…» y marca el límite de la afirmación.")],
    T=[
        ("{F} ¿Qué comenzó en Núremberg en noviembre de 1945?", "Los juicios a dirigentes del régimen alemán", "La ficha lo indica."),
        ("{F} ¿En qué fecha anunció Japón su rendición según la ficha?", "El 15 de agosto de 1945", "La ficha da esa fecha."),
        ("{F} ¿Qué dice la posición 2 sobre la bomba?", "Que mató a gran cantidad de civiles y que había otras alternativas", "Así lo resume la posición 2."),
        ("=", "{F} ¿Cuántos días pasaron entre el bombardeo de Hiroshima y el anuncio de rendición de Japón?", "15-6", "Se resta el día del bombardeo al día del anuncio, ambos de agosto.", " días"),
        ("{F} ¿Qué idea se usó en los juicios de Núremberg según la ficha? A) Crímenes contra la humanidad B) Apaciguamiento", "A) Crímenes contra la humanidad", "La ficha la nombra; el apaciguamiento fue una política anterior a la guerra."),
        ("{F} ¿Cuál de estas frases es un hecho comprobable? A) Hiroshima fue bombardeada el 6 de agosto de 1945 B) La bomba era la única forma de terminar la guerra", "A) Hiroshima fue bombardeada el 6 de agosto de 1945", "Tiene fecha y se comprueba; decir que era la única forma de terminar la guerra es una interpretación."),
        ("{F} ¿Qué elemento falta en este argumento: «La bomba fue un error»? A) Una razón y una evidencia B) Una fecha futura", "A) Una razón y una evidencia", "Un argumento tiene afirmación, razón y evidencia."),
        ("{F} La posición 1 dice que la bomba evitó una invasión. ¿Qué contraargumento le corresponde? A) Existían otras alternativas para terminar la guerra B) Nagasaki fue bombardeada el 9 de agosto", "A) Existían otras alternativas para terminar la guerra", "Es la razón que contradice la posición 1; la otra es solo un dato."),
        ("{F} Quieres defender la posición 2 con respeto. ¿Qué haces? A) Presentar tu argumento y reconocer la razón de la posición 1 B) Decir que quien piensa distinto no sabe historia", "A) Presentar tu argumento y reconocer la razón de la posición 1", "Un buen debate considera el contraargumento y respeta a las personas."),
        ("{F} ¿Por qué no se puede probar con certeza que la bomba evitó una invasión?", "Porque nadie puede comprobar lo que habría ocurrido si no se hubiera lanzado", "Es una afirmación sobre un hecho que no sucedió."),
        ("{F} Un compañero dice: «Los juicios de Núremberg prueban que todos los responsables fueron castigados». ¿Qué corrección haces? A) Fueron un intento de justicia; la ficha no prueba que se juzgara a todos B) Tiene razón porque comenzaron en 1945", "A) Fueron un intento de justicia; la ficha no prueba que se juzgara a todos", "La ficha solo dice que se juzgó a dirigentes, no a todos."),
        ("{F} ¿Qué afirmación respeta mejor los límites de la evidencia? A) Hay dos interpretaciones sobre la bomba, y cada una usa los mismos hechos de modo distinto B) Una de las posiciones es completamente falsa", "A) Hay dos interpretaciones sobre la bomba, y cada una usa los mismos hechos de modo distinto", "Las dos posiciones comparten hechos y difieren en la interpretación."),
        ("{F} ¿Cuál es la mejor pregunta para iniciar un debate respetuoso? A) ¿Qué razones y evidencias apoyan cada posición sobre la bomba? B) ¿Quién tiene razón y quién se equivoca?", "A) ¿Qué razones y evidencias apoyan cada posición sobre la bomba?", "Pedir razones y evidencias abre el debate; preguntar quién se equivoca solo busca ganar."),
    ],
    ctx=("En un debate de curso un estudiante dice «Tenía que hacerse y punto». ¿Qué le falta? A) Una razón y una evidencia que lo apoyen B) Más seguidores en la sala", "A) Una razón y una evidencia que lo apoyen", "Una opinión sin razones no es un argumento."),
    sc=[("¿Qué es un contraargumento?", "Una razón que va en contra de una afirmación", "Así se define en la clase."),
        ("¿Qué partes tiene un argumento?", "Una afirmación, una razón y una evidencia", "Así se define en el vocabulario."),
        ("En Historia: ¿cuál de estas frases es una interpretación? A) La bomba era la única alternativa B) Nagasaki fue bombardeada el 9 de agosto de 1945", "A) La bomba era la única alternativa", "No tiene fecha ni se puede comprobar: habla de lo que habría ocurrido.")],
    op=("Elige la posición 1 o la posición 2. Escribe un argumento de cuatro a seis líneas con afirmación, razón y una evidencia de la ficha, y agrega un contraargumento con su respuesta. Usa un tono respetuoso. {F}",
        "Posición 2: «La bomba afectó a civiles (afirmación), y los civiles no deben ser el objetivo (razón); la ficha dice que murió gran cantidad de civiles (evidencia). Contraargumento: acortó la guerra; respuesta: no se puede probar con certeza, y había alternativas».",
        ["incluye afirmación, razón y evidencia", "considera un contraargumento", "usa tono respetuoso"], ["argumento escrito", "contraargumento y respuesta"], ["no usar evidencia", "ignorar la otra posición"],
        "Pide que distinga en su texto un hecho y una interpretación."),
    reinforce="Explica a alguien de tu casa la diferencia entre un hecho y una interpretación con un ejemplo de esta clase.",
    extend="Anota una opinión tuya sobre un tema escolar y apóyala con una razón y una evidencia.",
)

OA = "HI2M OA 04"

# ================================================================ OA 04, clase 1
F = ("Ficha 1 (hechos). Yalta, febrero de 1945: se reúnen Roosevelt (Estados Unidos), Churchill (Reino Unido) y Stalin (URSS). "
     "Potsdam, julio y agosto de 1945: nueva reunión de los vencedores; Alemania queda dividida en cuatro zonas de ocupación (Estados Unidos, URSS, Reino Unido y Francia). "
     "ONU: su Carta se firma el 26 de junio de 1945 en San Francisco y la organización comienza a existir el 24 de octubre de 1945. "
     "Declaración Universal de Derechos Humanos: 10 de diciembre de 1948. Plan Marshall: ayuda económica de Estados Unidos para reconstruir Europa, propuesta en 1947. India se independiza del Reino Unido en 1947. "
     "Superpotencia: país con enorme poder militar, económico y de influencia mundial; tras 1945 lo fueron Estados Unidos y la URSS.")
build(
    OA, 1, F,
    use="Aprenderé a situar el mundo de la posguerra: quiénes eran los actores principales, qué se acordó en las conferencias de paz y qué nuevo marco internacional nació en 1945.",
    prior=["Conozco los bandos y el final de la Segunda Guerra Mundial.", "Sé calcular distancias entre fechas.", "Sé que un acuerdo internacional tiene actores y propósitos."],
    explain=[
        "Al terminar la Segunda Guerra Mundial, Europa quedó destruida y perdió la posición dominante que tenía desde hacía siglos. Estados Unidos y la URSS salieron como superpotencias, es decir, países con un poder militar, económico y de influencia que ningún otro igualaba. Por eso se habla de un mundo con dos grandes polos de poder.",
        "Los vencedores se reunieron en conferencias como Yalta, en febrero de 1945, y Potsdam, en julio y agosto del mismo año, para decidir el futuro de Europa. Alemania quedó dividida en cuatro zonas de ocupación. En esos años comenzó también la descolonización, el proceso por el cual las colonias se independizan; un ejemplo temprano es la independencia de India en 1947.",
        "Para evitar otra guerra, los países crearon la ONU en 1945 y aprobaron la Declaración Universal de Derechos Humanos en 1948. Para situar este proceso, ubica cada hecho en su fecha y pregunta quién lo impulsó. Un error común es creer que todo el orden de posguerra se decidió en un solo día o en una sola reunión.",
    ],
    vocab=[("superpotencia", "país con enorme poder militar, económico y de influencia mundial"), ("descolonización", "proceso por el cual las colonias se independizan"), ("zona de ocupación", "parte de un país vencido administrada por potencias vencedoras"), ("ONU", "Organización de las Naciones Unidas, creada en 1945 para mantener la paz"), ("hegemonía", "posición dominante de un país sobre otros")],
    worked=[
        ("Calcular una distancia en el tiempo", "¿Cuántos años pasaron entre la creación de la ONU y la Declaración Universal de Derechos Humanos?", ["Tomo 1945 y 1948.", "Resto: 1948 − 1945 = 3."], "3 años"),
        ("Identificar una superpotencia", "Según la ficha, ¿qué países eran superpotencias tras 1945?", ["Busco la definición de superpotencia.", "La ficha dice cuáles lo fueron."], "Estados Unidos y la URSS"),
    ],
    mistakes=[("Decir que Europa mantuvo su hegemonía mundial después de 1945.", "Se ignora la destrucción y el ascenso de Estados Unidos y la URSS.", "Recuerda que ahora hay dos superpotencias y que Europa pierde el primer lugar."),
              ("Creer que la descolonización comenzó solo después de 1960.", "Se olvidan los casos tempranos como India en 1947.", "Ubica India en 1947 como un inicio del proceso.")],
    T=[
        ("{F} ¿Quiénes se reúnen en Yalta en febrero de 1945?", "Roosevelt, Churchill y Stalin", "La ficha los nombra con sus países."),
        ("{F} ¿En cuántas zonas de ocupación queda dividida Alemania?", "En cuatro zonas", "La ficha lo indica."),
        ("{F} ¿Qué fecha lleva la Declaración Universal de Derechos Humanos?", "10 de diciembre de 1948", "La ficha da esa fecha."),
        ("{F} ¿En qué ciudad se firmó la Carta de la ONU en junio de 1945?", "San Francisco", "La ficha lo indica."),
        ("{F} ¿Cuál de estos países tuvo una zona de ocupación en Alemania según la ficha? A) Francia B) Italia", "A) Francia", "La ficha nombra a Estados Unidos, la URSS, el Reino Unido y Francia."),
        ("{F} ¿Qué país se independizó del Reino Unido en 1947? A) India B) Alemania", "A) India", "La ficha ubica la independencia de India en 1947."),
        ("{F} ¿Qué es el Plan Marshall? A) Ayuda económica de Estados Unidos para reconstruir Europa B) Un tratado que dividió Alemania en cuatro zonas", "A) Ayuda económica de Estados Unidos para reconstruir Europa", "La ficha lo define así; la división de Alemania en zonas es otro hecho."),
        ("{F} Un país tiene el mayor poder militar y económico y gran influencia en todo el mundo. ¿Cómo se llama? A) Superpotencia B) Zona de ocupación", "A) Superpotencia", "Esa es la definición de la ficha."),
        ("{F} Una colonia obtiene su independencia en 1947. ¿En qué proceso se inscribe? A) Descolonización B) Ocupación", "A) Descolonización", "La independencia de colonias es descolonización."),
        ("{F} ¿Por qué se dice que Europa perdió hegemonía tras 1945?", "Porque quedó destruida y dos superpotencias, Estados Unidos y la URSS, pasaron a dominar el escenario mundial", "La ficha indica el ascenso de otras dos potencias."),
        ("{F} Un compañero dice: «La ONU nació en Yalta». ¿Qué corrección haces? A) Yalta fue una reunión de vencedores en febrero de 1945; la Carta se firmó en San Francisco en junio B) Tiene razón porque en Yalta estaban los vencedores", "A) Yalta fue una reunión de vencedores en febrero de 1945; la Carta se firmó en San Francisco en junio", "La ficha separa la reunión de Yalta de la firma de la Carta."),
        ("{F} Ordena de más antiguo a más reciente: (a) Declaración Universal de Derechos Humanos (b) Yalta (c) inicio de la ONU (d) independencia de India.", "b, c, d, a", "Los hechos van de 1945 (Yalta, ONU) a 1947 (India) y 1948 (Declaración)."),
        ("{F} ¿Cuál es la mejor pregunta para investigar este tema? A) ¿Qué nuevo orden internacional surgió tras la Segunda Guerra Mundial y quiénes lo impulsaron? B) ¿Cuál fue la mejor conferencia de la historia?", "A) ¿Qué nuevo orden internacional surgió tras la Segunda Guerra Mundial y quiénes lo impulsaron?", "La primera se responde con hechos y actores; la segunda es una opinión."),
    ],
    ctx=("Un afiche escolar dice: «En 1945 un solo acuerdo creó todo el orden de posguerra». ¿Qué problema tiene? A) Ignora que hubo varias reuniones y procesos distintos en 1945-1948 B) Usa una fecha incorrecta", "A) Ignora que hubo varias reuniones y procesos distintos en 1945-1948", "La ficha muestra conferencias, la ONU, India y la Declaración en fechas distintas."),
    sc=[("¿Qué es una superpotencia?", "Un país con enorme poder militar, económico y de influencia mundial", "Así se define en la clase."),
        ("¿Qué es la descolonización?", "El proceso por el cual las colonias se independizan", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una zona de ocupación?", "Una parte de un país vencido administrada por potencias vencedoras", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo de 1945 a 1948 con una raya y su nombre para Yalta, Potsdam, la Carta de la ONU, el inicio de la ONU, Plan Marshall, independencia de India y la Declaración Universal. Escribe debajo dos frases: una sobre las superpotencias y otra sobre la pérdida de hegemonía de Europa. {F}",
        "Yalta y Potsdam en 1945, junio y octubre para la ONU, 1947 para India y Plan Marshall, 1948 para la Declaración. Frases: «Estados Unidos y la URSS fueron superpotencias»; «Europa quedó destruida y perdió su hegemonía».",
        ["ubica los hechos en su fecha", "nombra las superpotencias", "explica la pérdida de hegemonía"], ["línea de tiempo dibujada", "dos frases escritas"], ["poner todos los hechos en el mismo año", "confundir Yalta con la ONU"],
        "Pide que explique qué diferencia hay entre una reunión de vencedores y una organización permanente."),
    reinforce="Explica en voz alta qué es una superpotencia y nombra dos hechos de 1945 con su fecha.",
    extend="Busca en un mapa dónde están Estados Unidos y la India, y anota en qué continentes se ubican.",
)

# ================================================================ OA 04, clase 2
F = ("Ficha 2 (hechos y tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Hechos: la Declaración Universal de Derechos Humanos fue aprobada por la Asamblea General de la ONU el 10 de diciembre de 1948 en París; tiene 30 artículos; es una declaración de ideales comunes, no un tratado que obligue como una ley. "
     "Resúmenes con otras palabras: artículo 1, todas las personas nacen libres e iguales en dignidad y derechos; artículo 5, nadie debe ser sometido a tortura; artículo 19, toda persona puede opinar y expresarse; artículo 26, toda persona tiene derecho a la educación. "
     "Fuente A, discurso de un delegado de un país europeo con colonias, 1946 (de ejemplo): «Nuestras colonias aún no están preparadas para gobernarse solas.» "
     "Fuente B, carta de una dirigente independentista de una colonia, 1947 (de ejemplo): «Si todos los pueblos tienen derechos, también el nuestro.» "
     "Fuente C, titular de un diario de un país vencedor, 1945 (de ejemplo): «La nueva organización mundial evitará otra guerra.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre la posguerra, como discursos, cartas y la Declaración Universal de Derechos Humanos, preguntando quién habla y con qué propósito.",
    prior=["Sé que la procedencia es quién, cuándo y para qué.", "Conozco la ONU y la descolonización.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Las fuentes de la posguerra incluyen documentos oficiales, discursos, cartas y titulares. Cada una responde a la pregunta de quién habla, cuándo y para qué. Un delegado de un país con colonias habla desde el poder; una dirigente independentista habla desde quien reclama derechos; un diario de un país vencedor puede mostrar optimismo.",
        "La Declaración Universal de Derechos Humanos, aprobada en 1948, es una fuente especial: expresa ideales comunes de los países de la ONU, pero es una declaración, no un tratado, y por eso no obliga como una ley. Sus artículos, como el que afirma que todas las personas nacen libres e iguales en dignidad y derechos, sirvieron para medir lo que los países hacían.",
        "Al interrogar fuentes se puede notar una tensión: la fuente A defiende mantener el gobierno colonial, mientras la fuente B reclama que los derechos valgan para todos los pueblos. Una fuente de procedencia distinta no se descarta, se contrasta. Y un titular optimista no prueba que la paz esté asegurada.",
    ],
    vocab=[("declaración", "documento que expresa ideales comunes, sin obligar como una ley"), ("tratado", "acuerdo entre Estados que los obliga a cumplirlo"), ("delegado", "persona que representa a su país en una reunión internacional"), ("independentista", "persona que defiende la independencia de un territorio"), ("titular", "frase principal de una noticia")],
    worked=[
        ("Identificar procedencia", "¿Quién escribió la fuente B y qué busca?", ["Leo el encabezado: una dirigente independentista, 1947.", "Reclama derechos para su pueblo."], "Una dirigente independentista; busca que los derechos valgan para su pueblo"),
        ("Distinguir un tipo de documento", "¿La Declaración Universal de Derechos Humanos obliga como una ley? Justifica con la ficha.", ["La ficha dice que es una declaración de ideales comunes.", "Agrega que no es un tratado que obligue."], "No; es una declaración, no un tratado"),
    ],
    mistakes=[("Creer que una declaración obliga igual que un tratado.", "Se confunden los dos tipos de documento.", "Recuerda que la declaración expresa ideales y no obliga como un tratado."),
              ("Aceptar un titular optimista como prueba de que la paz está asegurada.", "Se olvida que un diario muestra una visión y un momento.", "Pregunta quién lo escribió y busca otra fuente para contrastar.")],
    T=[
        ("{F} ¿En qué ciudad se aprobó la Declaración Universal de Derechos Humanos?", "París", "La ficha lo indica."),
        ("{F} ¿Cuántos artículos tiene la Declaración Universal de Derechos Humanos?", "30 artículos", "La ficha da esa cifra."),
        ("{F} ¿Quién escribió la fuente A?", "Un delegado de un país europeo con colonias", "El encabezado de la fuente A lo indica."),
        ("{F} ¿Qué órgano de la ONU aprobó la Declaración Universal de Derechos Humanos? A) La Asamblea General B) El delegado de un país europeo", "A) La Asamblea General", "La ficha dice que la aprobó la Asamblea General de la ONU el 10 de diciembre de 1948."),
        ("{F} ¿Qué artículo de la Declaración afirma que nadie debe ser sometido a tortura? A) El artículo 5 B) El artículo 26", "A) El artículo 5", "El resumen de la ficha asigna la tortura al artículo 5; el 26 es la educación."),
        ("{F} ¿Qué tipo de fuente es la fuente B? A) Una carta de una dirigente independentista B) Un discurso oficial de un delegado", "A) Una carta de una dirigente independentista", "Su encabezado la describe como carta."),
        ("{F} La fuente A dice que las colonias no están preparadas para gobernarse solas. ¿Desde qué posición habla? A) Desde un país que mantiene colonias B) Desde una colonia que reclama independencia", "A) Desde un país que mantiene colonias", "Su autor es un delegado de un país con colonias."),
        ("{F} Un artículo de la Declaración dice que toda persona tiene derecho a educarse. ¿Cuál es? A) El artículo 26 B) El artículo 19", "A) El artículo 26", "Según la ficha el 26 trata de educación; el 19 es opinión y expresión."),
        ("{F} ¿Qué diferencia hay entre una declaración y un tratado? A) El tratado obliga a los Estados; la declaración expresa ideales comunes B) La declaración obliga más que el tratado", "A) El tratado obliga a los Estados; la declaración expresa ideales comunes", "La ficha lo establece al describir la Declaración."),
        ("{F} ¿Por qué la fuente C no prueba que la paz quedó asegurada?", "Porque es un titular de un diario que expresa optimismo, no una prueba de lo que ocurrió después", "Una fuente periodística muestra una visión del momento."),
        ("{F} Un compañero dice: «Como la Declaración se aprobó en 1948, todos los países cumplían los derechos». ¿Qué corrección haces? A) Aprobarla no prueba que se cumpliera; es una declaración de ideales B) Tiene razón porque la aprobó la ONU", "A) Aprobarla no prueba que se cumpliera; es una declaración de ideales", "Un documento de ideales no demuestra lo que se hacía en la práctica."),
        ("{F} ¿Qué relación puede verse entre las fuentes A y B? A) Una defiende mantener el gobierno colonial y la otra reclama derechos para su pueblo B) Ambas piden la independencia inmediata", "A) Una defiende mantener el gobierno colonial y la otra reclama derechos para su pueblo", "Sus propósitos son opuestos."),
        ("{F} ¿Qué fuente agregarías para contrastar la fuente A? A) El testimonio de una persona de una colonia B) Otro discurso del mismo delegado", "A) El testimonio de una persona de una colonia", "Otra procedencia ofrece otro punto de vista; repetir al mismo autor no contrasta."),
    ],
    ctx=("Un estudiante escribe: «La fuente C prueba que no hubo más guerras». ¿Qué falla tiene? A) Un titular optimista de 1945 no puede probar el futuro B) Usa un titular de 1945 en vez de uno de 1946", "A) Un titular optimista de 1945 no puede probar el futuro", "Un titular es una opinión del momento."),
    sc=[("¿Qué es un tratado?", "Un acuerdo entre Estados que los obliga a cumplirlo", "Así se define en el vocabulario."),
        ("¿Qué es una declaración?", "Un documento que expresa ideales comunes sin obligar como una ley", "Así se define en la clase."),
        ("En Historia: ¿qué es un delegado?", "Una persona que representa a su país en una reunión internacional", "Así se define en el vocabulario de la clase.")],
    op=("Elige las fuentes A y B. Completa una tabla con quién habla, cuándo, para qué y qué NO prueba. Después escribe una frase que explique cómo el artículo 1 de la Declaración (todas las personas nacen libres e iguales en dignidad y derechos) se relaciona con la fuente B. {F}",
        "Fuente A: delegado de un país con colonias, 1946, propósito de mantener el gobierno colonial; no prueba la opinión de las colonias. Fuente B: dirigente independentista, 1947, reclama derechos; no prueba lo que pensaba toda la colonia. Frase: «La dirigente usa la idea de derechos para todos los pueblos».",
        ["completa quién, cuándo, para qué y límite", "conecta el artículo 1 con la fuente B", "no generaliza"], ["tabla de dos fuentes", "frase final"], ["tomar la fuente A como opinión de todos", "olvidar el límite de cada fuente"],
        "Pide que explique por qué la Declaración no obliga como un tratado."),
    reinforce="Explica a alguien de tu casa la diferencia entre una declaración y un tratado con un ejemplo de esta clase.",
    extend="Elige un artículo de la ficha y escribe un ejemplo de tu vida escolar donde se respete ese derecho.",
)

# ================================================================ OA 04, clase 3
F = ("Ficha 3 (hechos y perspectivas de ejemplo). "
     "Hechos: Indonesia proclama su independencia en 1945; India se independiza en 1947; en 1955 se realiza la Conferencia de Bandung, que reúne a países de Asia y África; Ghana se independiza en 1957; Argelia, en 1962. "
     "Escalas: global (el mundo entero), regional (Asia, África, Europa) y local (un país o una ciudad). "
     "Perspectiva de ejemplo de Estados Unidos: promueve la democracia liberal y una economía abierta, y ayuda a reconstruir Europa. "
     "Perspectiva de ejemplo de la URSS: promueve el comunismo y busca influencia en Europa oriental. "
     "Perspectiva de ejemplo de un país europeo con colonias: necesita reconstruirse y quiere conservar su influencia. "
     "Perspectiva de ejemplo de un pueblo colonizado: reclama independencia y los mismos derechos que los demás pueblos.")
build(
    OA, 3, F,
    use="Aprenderé a comparar las perspectivas de Estados Unidos, la URSS, Europa y los pueblos colonizados en la posguerra, y a mirar el proceso en escala global, regional y local.",
    prior=["Sé situar la posguerra y la ONU.", "Sé qué es una superpotencia y qué es la descolonización.", "Sé que una perspectiva es un punto de vista."],
    explain=[
        "En la posguerra, cada actor tenía una perspectiva distinta. Estados Unidos promovía la democracia liberal y una economía abierta; la URSS, el comunismo y su influencia en Europa oriental; los países europeos con colonias querían reconstruirse y conservar su influencia; y los pueblos colonizados reclamaban independencia y los mismos derechos que los demás. Comparar perspectivas significa ver qué quiere cada actor y por qué.",
        "La escala cambia lo que se ve. En escala global se observa un mundo con dos superpotencias; en escala regional, la reunión de Bandung en 1955, donde países de Asia y África discutieron su lugar en el mundo; en escala local, la independencia de un país concreto, como Ghana en 1957 o Argelia en 1962. Cada escala responde preguntas distintas.",
        "La descolonización no ocurrió en una sola fecha: Indonesia proclamó su independencia en 1945, India se independizó en 1947 y otros países lo hicieron años después. Por eso conviene evitar frases como «todas las colonias se independizaron al terminar la guerra».",
    ],
    vocab=[("perspectiva", "punto de vista de un actor sobre un hecho"), ("escala", "tamaño del espacio que se estudia: global, regional o local"), ("independencia", "condición de un territorio que se gobierna a sí mismo"), ("Conferencia de Bandung", "reunión de países de Asia y África realizada en 1955"), ("democracia liberal", "sistema con elecciones, varios partidos y libertades individuales")],
    worked=[
        ("Reconocer la escala", "La independencia de Ghana en 1957 se estudia como un caso. ¿En qué escala está?", ["Se centra en un solo país.", "No estudia todo el mundo ni toda una región."], "Escala local"),
        ("Calcular una distancia", "¿Cuántos años pasaron entre la independencia de India y la de Argelia?", ["Tomo 1947 y 1962.", "Resto: 1962 − 1947 = 15."], "15 años"),
    ],
    mistakes=[("Decir que todas las colonias se independizaron al terminar la guerra.", "Se ignoran los años distintos de cada proceso.", "Ubica cada independencia en su fecha: 1945, 1947, 1957, 1962."),
              ("Creer que Estados Unidos y la URSS pensaban lo mismo sobre la economía y la política.", "Se confunden dos proyectos opuestos.", "Compara lo que promovía cada uno según la ficha.")],
    T=[
        ("{F} ¿En qué año se realizó la Conferencia de Bandung?", "1955", "La ficha lo indica."),
        ("{F} ¿Qué reclamaba un pueblo colonizado según la ficha?", "Independencia y los mismos derechos que los demás pueblos", "Es su perspectiva en la ficha."),
        ("{F} ¿Qué promovía la URSS según la ficha?", "El comunismo y su influencia en Europa oriental", "Así describe la ficha su perspectiva."),
        ("=", "{F} ¿Cuántos años pasaron entre la independencia de Ghana y la de Argelia?", "1962-1957", "Se resta el año de Ghana al de Argelia.", " años"),
        ("{F} ¿Qué país asiático proclamó su independencia en 1945? A) Indonesia B) Ghana", "A) Indonesia", "La ficha ubica a Indonesia en 1945; Ghana está en África y se independizó en 1957."),
        ("{F} ¿Qué perspectiva corresponde a «Necesitamos reconstruirnos, pero queremos conservar nuestra influencia en las colonias»? A) La de un país europeo con colonias B) La de un pueblo colonizado", "A) La de un país europeo con colonias", "Quien quiere conservar su influencia en las colonias es la potencia europea."),
        ("{F} Un estudio analiza qué reunió a países de Asia y África en 1955. ¿Qué escala usa? A) Regional B) Local", "A) Regional", "Abarca varios países de dos continentes, no un solo lugar."),
        ("{F} Un estudio analiza la independencia de un solo país. ¿Qué escala usa? A) Local B) Global", "A) Local", "Se centra en un solo país."),
        ("{F} ¿Qué actor ayudaba a reconstruir Europa según la ficha? A) Estados Unidos, que promovía una economía abierta B) La URSS, que promovía el comunismo", "A) Estados Unidos, que promovía una economía abierta", "La ficha asocia a Estados Unidos con la reconstrucción de Europa."),
        ("{F} ¿Por qué no se puede decir que las colonias se independizaron todas al mismo tiempo?", "Porque las fechas de la ficha van de 1945 a 1962", "La ficha muestra independencias en años distintos."),
        ("{F} Un compañero dice: «La perspectiva de Estados Unidos explica por qué los pueblos colonizados querían independencia». ¿Qué corrección haces? A) Esa perspectiva explica lo que quería Estados Unidos; la de los pueblos colonizados se explica con sus propias fuentes B) Tiene razón porque ambos hablaban de libertad", "A) Esa perspectiva explica lo que quería Estados Unidos; la de los pueblos colonizados se explica con sus propias fuentes", "Cada perspectiva se explica con su propio actor."),
        ("{F} ¿Cuál de estas combinaciones compara bien dos perspectivas? A) Estados Unidos promovía la democracia liberal y la URSS el comunismo B) Estados Unidos y la URSS promovían lo mismo", "A) Estados Unidos promovía la democracia liberal y la URSS el comunismo", "La ficha las presenta como proyectos distintos."),
        ("{F} ¿Qué afirmación respeta la evidencia de la ficha? A) La descolonización fue un proceso con fechas distintas, iniciado en la posguerra B) La descolonización terminó en 1945", "A) La descolonización fue un proceso con fechas distintas, iniciado en la posguerra", "La ficha ubica independencias entre 1945 y 1962."),
    ],
    ctx=("Un grupo prepara un panel con el título «Todos los países querían lo mismo después de la guerra». ¿Qué problema tiene? A) Omite que los actores tenían proyectos y perspectivas distintas B) Nombra a Estados Unidos y a la URSS", "A) Omite que los actores tenían proyectos y perspectivas distintas", "La ficha presenta cuatro perspectivas diferentes."),
    sc=[("¿Qué es una escala?", "El tamaño del espacio que se estudia", "Así se define en la clase."),
        ("¿Qué fue la Conferencia de Bandung?", "Una reunión de países de Asia y África realizada en 1955", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es la independencia de un territorio?", "La condición de un territorio que se gobierna a sí mismo", "Así se define en el vocabulario de la clase.")],
    op=("Haz una tabla con cuatro filas: Estados Unidos, URSS, país europeo con colonias, pueblo colonizado. En las columnas escribe qué quería cada uno y qué escala (global, regional o local) usarías para estudiarlo mejor. Termina con una frase que compare dos perspectivas. {F}",
        "Estados Unidos: democracia liberal y reconstrucción de Europa, escala global. URSS: comunismo e influencia en Europa oriental, escala global. País europeo: reconstruirse y conservar influencia, escala regional. Pueblo colonizado: independencia, escala local. Frase: «Estados Unidos y la URSS tenían proyectos opuestos».",
        ["describe lo que quería cada actor", "asigna una escala razonable", "la frase compara con la ficha"], ["tabla de cuatro filas", "frase comparativa"], ["decir que todos querían lo mismo", "mezclar la escala con el actor"],
        "Pide que explique por qué la escala local ayuda a ver detalles que la global oculta."),
    reinforce="Explica con tus palabras cuál era la perspectiva de un pueblo colonizado y cuál la de un país europeo con colonias.",
    extend="Busca en un mapa los países Indonesia, India, Ghana y Argelia y anota en qué continente está cada uno.",
)

# ================================================================ OA 04, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; hechos y datos de ejemplo). "
     "Causas de la pérdida de hegemonía de Europa: ciudades y fábricas destruidas; deudas con Estados Unidos; pérdida de prestigio de las potencias coloniales; crecimiento de movimientos independentistas. "
     "Cambios: nacen la ONU (1945) y la Declaración Universal de Derechos Humanos (1948); el mundo queda con dos superpotencias; comienza la descolonización. "
     "Continuidades: muchas colonias seguían bajo control europeo en 1945; en el Consejo de Seguridad de la ONU, cinco miembros permanentes (Estados Unidos, URSS, Reino Unido, Francia y China) tienen derecho a veto, es decir, pueden bloquear una decisión; persistía la desigualdad económica entre países ricos y pobres. "
     "Dato de ejemplo: un país europeo tenía 8 colonias en 1945 y, hasta 1960, 3 se habían independizado.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la pérdida de hegemonía de Europa con los cambios y continuidades de la posguerra, como el nuevo marco de la ONU y la descolonización.",
    prior=["Sé situar la posguerra y comparar perspectivas.", "Sé que un hecho tiene varias causas.", "Sé calcular restas sencillas."],
    explain=[
        "Europa perdió hegemonía por varias causas que se combinaron: la destrucción de ciudades y fábricas, las deudas con Estados Unidos, la pérdida de prestigio de las potencias coloniales y el crecimiento de los movimientos independentistas. Una explicación multicausal no se queda con una sola razón, sino que muestra cómo se relacionan.",
        "La posguerra trajo cambios importantes: la ONU, para mantener la paz, la Declaración Universal de Derechos Humanos, un mundo con dos superpotencias y el comienzo de la descolonización. Pero también hubo continuidades: muchas colonias seguían bajo control europeo en 1945, y en el Consejo de Seguridad de la ONU cinco miembros permanentes tienen derecho a veto, lo que limita su acción.",
        "Cambio no significa que todo se transformó. Una colonia independiente puede seguir dependiendo económicamente de otros países, y una organización nueva puede reflejar el poder de los vencedores. Para relacionar causas y consecuencias, ordena los hechos en el tiempo y no digas que algo fue causa solo porque ocurrió antes.",
    ],
    vocab=[("derecho a veto", "poder de un miembro permanente del Consejo de Seguridad de bloquear una decisión"), ("Consejo de Seguridad", "órgano de la ONU encargado de mantener la paz"), ("multicausal", "explicación que combina varias causas"), ("movimiento independentista", "organización que busca la independencia de un territorio"), ("continuidad", "algo que sigue igual a pesar de un cambio")],
    worked=[
        ("Clasificar cambio y continuidad", "Según la ficha, la creación de la ONU en 1945, ¿es un cambio o una continuidad?", ["Antes de 1945 no existía esa organización.", "Es algo nuevo."], "Un cambio"),
        ("Calcular lo que queda", "Un país europeo tenía 8 colonias y 3 se independizaron. ¿Cuántas conserva?", ["Parto de las 8 colonias.", "Resto: 8 − 3 = 5."], "5 colonias"),
    ],
    mistakes=[("Decir que la descolonización terminó en 1945 porque nació la ONU.", "Se confunde la creación de una organización con el fin del dominio colonial.", "Recuerda que muchas colonias seguían bajo control europeo."),
              ("Tomar el derecho a veto como un cambio en el poder de los pequeños.", "Se olvida que lo tienen solo cinco países.", "Recuerda que es una continuidad del poder de los vencedores.")],
    T=[
        ("{F} ¿Qué países tienen derecho a veto en el Consejo de Seguridad según la ficha?", "Estados Unidos, URSS, Reino Unido, Francia y China", "La ficha los nombra como miembros permanentes."),
        ("{F} ¿Qué es el derecho a veto?", "Poder de bloquear una decisión del Consejo de Seguridad", "La ficha lo define así."),
        ("{F} ¿Qué dos documentos o instituciones nombra la ficha como cambios de la posguerra?", "La ONU y la Declaración Universal de Derechos Humanos", "La ficha los lista entre los cambios."),
        ("{F} ¿Cuál de estos países tiene derecho a veto en el Consejo de Seguridad? A) China B) Alemania", "A) China", "La ficha nombra a China entre los cinco miembros permanentes; Alemania no aparece."),
        ("=", "{F} Si el país de ejemplo de la ficha tenía 8 colonias y hasta 1960 se independizaron 3, y luego otras 2, ¿cuántas colonias conservaba después?", "8-3-2", "Se restan las dos tandas de independencias a las 8 iniciales.", " colonias"),
        ("{F} ¿Cuál de estas es una causa de la pérdida de hegemonía de Europa? A) Las deudas con Estados Unidos y la destrucción de ciudades B) La creación de la Declaración Universal de Derechos Humanos", "A) Las deudas con Estados Unidos y la destrucción de ciudades", "La ficha las lista como causas; la Declaración es un cambio posterior."),
        ("{F} La ONU se creó en 1945. ¿Qué es eso respecto de la época anterior? A) Un cambio B) Una continuidad", "A) Un cambio", "Antes de 1945 no existía esa organización."),
        ("{F} Muchas colonias seguían bajo control europeo en 1945. ¿Qué es eso? A) Una continuidad B) Un cambio", "A) Una continuidad", "Esa situación venía de antes y seguía."),
        ("{F} ¿Qué efecto puede tener el derecho a veto en la acción de la ONU? A) Una de las cinco potencias puede bloquear una decisión B) Todas las decisiones se aprueban rápido", "A) Una de las cinco potencias puede bloquear una decisión", "El veto limita la acción cuando una potencia se opone."),
        ("{F} ¿Por qué la ONU puede considerarse a la vez un cambio y una continuidad?", "Porque es una organización nueva, pero refleja el poder de los vencedores", "La ficha muestra una institución nueva con cinco miembros permanentes."),
        ("{F} Un compañero dice: «Como los movimientos independentistas crecieron en la posguerra, causaron la creación de la ONU». ¿Qué corrección haces? A) Crecer a la vez no prueba que una cosa causara la otra B) Tiene razón porque ocurrieron en la misma época", "A) Crecer a la vez no prueba que una cosa causara la otra", "Coincidir en el tiempo no prueba una causa."),
        ("{F} ¿Qué evidencia apoya mejor que Europa perdió hegemonía? A) Ciudades destruidas, deudas con Estados Unidos y dos superpotencias B) Que Francia tenía derecho a veto", "A) Ciudades destruidas, deudas con Estados Unidos y dos superpotencias", "Muestra pérdida de poder; el veto de Francia no prueba pérdida."),
        ("{F} ¿Cuál es la mejor síntesis? A) Europa perdió hegemonía por varias causas; nacieron la ONU y la Declaración, comenzó la descolonización y siguieron las colonias y las desigualdades B) Todo cambió en 1948", "A) Europa perdió hegemonía por varias causas; nacieron la ONU y la Declaración, comenzó la descolonización y siguieron las colonias y las desigualdades", "Reúne causas, cambios y continuidades."),
    ],
    ctx=("Una infografía dice: «Con la ONU terminaron las colonias». ¿Qué error tiene? A) Ignora que muchas colonias seguían bajo control europeo B) Usa la fecha de 1945 sin citar la Carta", "A) Ignora que muchas colonias seguían bajo control europeo", "La ficha señala que muchas colonias continuaban."),
    sc=[("¿Qué es una continuidad?", "Algo que sigue igual a pesar de un cambio", "Así se define en el vocabulario."),
        ("¿Qué es el Consejo de Seguridad?", "Un órgano de la ONU encargado de mantener la paz", "Así se define en la clase."),
        ("En Historia: ¿qué es un movimiento independentista?", "Una organización que busca la independencia de un territorio", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja un esquema con «pérdida de hegemonía de Europa» en el centro. Escribe tres causas a la izquierda, dos cambios a la derecha y dos continuidades abajo. Escribe una frase con «contribuyó a» sobre el veto de las cinco potencias. {F}",
        "Causas: destrucción, deudas, pérdida de prestigio colonial. Cambios: ONU, descolonización. Continuidades: colonias y desigualdad. Frase: «El veto contribuyó a que la ONU no siempre pudiera actuar».",
        ["incluye tres causas", "distingue cambios y continuidades", "usa «contribuyó a» sin causa única"], ["esquema", "frase"], ["poner los cambios como causas", "decir que la ONU eliminó las colonias"],
        "Pide que explique por qué un cambio no borra todo lo anterior."),
    reinforce="Explica a alguien de tu casa qué es un cambio y qué es una continuidad con un ejemplo de la ONU.",
    extend="Piensa en una escuela con un reglamento nuevo y di qué cambió y qué siguió igual.",
)

# ================================================================ OA 04, clase 5
F = ("Ficha 5 (hechos y evidencias de ejemplo). "
     "Hechos: los juicios de Núremberg comenzaron en noviembre de 1945; la ONU aprobó la convención contra el genocidio el 9 de diciembre de 1948 y la Declaración Universal de Derechos Humanos el 10 de diciembre de 1948; en 1966 se adoptaron dos pactos sobre derechos, que sí son tratados obligatorios para los Estados que los firman. "
     "La Conferencia de Bandung fue en 1955; India se independizó en 1947 y Ghana en 1957. "
     "Evidencia A (de ejemplo): un informe de un funcionario, 1950: «Los derechos humanos ahora figuran en documentos internacionales.» "
     "Evidencia B (de ejemplo): una carta de un grupo de una colonia, 1952: «Hablamos de derechos mundiales, pero seguimos sin gobierno propio.» "
     "Evidencia C (de ejemplo): un titular de un diario, 1948: «Un acuerdo histórico: los pueblos del mundo declaran sus ideales comunes.»")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada que evalúe las consecuencias de la Segunda Guerra Mundial, con tesis, evidencias de varias fuentes y límites reconocidos.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé relacionar causas, cambios y continuidades.", "Sé distinguir una declaración de un tratado."],
    explain=[
        "Evaluar las consecuencias de una guerra significa juzgar su alcance con criterios y evidencias, no solo contarlas. Una interpretación documentada tiene una tesis, es decir, una idea que se defiende, y usa evidencias de fuentes de distinta procedencia. Por ejemplo, la tesis «la posguerra creó un nuevo marco internacional, pero con límites» se apoya en hechos y en fuentes.",
        "Los hechos de la ficha muestran el nuevo marco: los juicios de Núremberg, la convención contra el genocidio, la Declaración Universal de Derechos Humanos y los pactos de 1966, que sí son tratados obligatorios. La evidencia B, en cambio, muestra un límite: se hablaba de derechos mundiales mientras las colonias seguían sin gobierno propio. Cada evidencia prueba algo distinto.",
        "Una buena interpretación reconoce sus límites: un titular optimista no prueba que los derechos se cumplieran, y una carta de un grupo no representa a toda una colonia. Conviene usar expresiones como «contribuyó a» y «según esta fuente» y evitar frases como «resolvió todo». Así tu texto queda proporcional a la evidencia.",
    ],
    vocab=[("tesis", "idea central que se defiende con evidencias"), ("evidencia", "dato o fuente que apoya una afirmación"), ("pacto", "tratado entre Estados que los obliga a cumplirlo"), ("marco regulador", "conjunto de reglas e instituciones que ordena las relaciones entre países"), ("límite", "aspecto que una fuente o una explicación no alcanza a mostrar")],
    worked=[
        ("Elegir evidencia", "¿Qué evidencia de la ficha apoya mejor que hubo límites en el cumplimiento de los derechos?", ["Busco una fuente que muestre una carencia.", "La evidencia B habla de colonias sin gobierno propio."], "La evidencia B"),
        ("Calcular un plazo", "¿Cuántos años pasaron entre los juicios de Núremberg y los pactos de 1966?", ["Tomo 1945 y 1966.", "Resto: 1966 − 1945 = 21."], "21 años"),
    ],
    mistakes=[("Escribir una tesis sin ninguna evidencia.", "Se piensa que una idea clara basta.", "Apoya cada parte de la tesis con una fuente o un hecho."),
              ("Usar «resolvió todo» para describir a la ONU.", "Se ignoran los límites que muestran las fuentes.", "Escribe «contribuyó a» y agrega el límite.")],
    T=[
        ("{F} ¿Cuándo aprobó la ONU la Declaración Universal de Derechos Humanos?", "El 10 de diciembre de 1948", "La ficha da esa fecha."),
        ("{F} ¿Qué diferencia tienen los pactos de 1966 con la Declaración?", "Son tratados obligatorios para los Estados que los firman", "La ficha los describe así."),
        ("{F} ¿Qué fuente de la ficha plantea un límite del nuevo marco de derechos?", "La evidencia B, la carta de un grupo de una colonia", "Habla de derechos mundiales sin gobierno propio."),
        ("=", "{F} ¿Cuántos años pasaron entre la Declaración Universal y los pactos de 1966?", "1966-1948", "Se resta el año de la Declaración al de los pactos.", " años"),
        ("{F} ¿Qué aprobó la ONU el 9 de diciembre de 1948? A) La convención contra el genocidio B) Los pactos sobre derechos", "A) La convención contra el genocidio", "Los pactos sobre derechos se adoptaron en 1966."),
        ("{F} ¿Qué tesis está mejor apoyada por la evidencia A y la B? A) La posguerra creó un marco internacional de derechos, pero con límites en la práctica B) La posguerra resolvió todos los problemas", "A) La posguerra creó un marco internacional de derechos, pero con límites en la práctica", "Esa tesis recoge el marco y el límite; decir que todo se resolvió no tiene respaldo en las fuentes."),
        ("{F} ¿Qué prueba la evidencia C? A) Que en 1948 un diario celebró el acuerdo como un hecho importante B) Que los derechos se cumplían en todos los países", "A) Que en 1948 un diario celebró el acuerdo como un hecho importante", "Un titular muestra la visión del diario, no el cumplimiento."),
        ("{F} Quieres apoyar la idea de que se buscó justicia tras la guerra. ¿Qué hecho de la ficha usas? A) Los juicios de Núremberg de 1945 B) La Conferencia de Bandung de 1955", "A) Los juicios de Núremberg de 1945", "Los juicios son el intento de justicia; Bandung trata de descolonización."),
        ("{F} ¿Qué expresión es más proporcional a la evidencia? A) La ONU contribuyó a crear un marco para los derechos B) La ONU garantizó los derechos en todo el mundo", "A) La ONU contribuyó a crear un marco para los derechos", "La evidencia B muestra que los derechos no se cumplían en todas partes."),
        ("{F} ¿Por qué la evidencia A no basta para concluir que los derechos humanos se cumplían?", "Porque solo dice que figuran en documentos, no que se hayan cumplido", "Aparecer en documentos no es lo mismo que cumplirse."),
        ("{F} Un compañero dice: «La evidencia B prueba que ninguna colonia mejoró». ¿Qué corrección haces? A) La carta muestra la queja de un grupo, no la situación de todas las colonias B) Tiene razón porque es una carta antigua", "A) La carta muestra la queja de un grupo, no la situación de todas las colonias", "Una fuente de un grupo no basta para generalizar."),
        ("{F} ¿Qué estructura tiene una interpretación documentada? A) Tesis, evidencias de varias fuentes y límites B) Opinión, repetición y conclusión", "A) Tesis, evidencias de varias fuentes y límites", "Así se define en la explicación."),
        ("{F} ¿Qué límite debe reconocer quien use solo las evidencias A y C? A) No muestran lo que vivían las colonias B) No muestran el nuevo marco internacional", "A) No muestran lo que vivían las colonias", "Son voces de un funcionario y de un diario; falta la voz de las colonias."),
    ],
    ctx=("Un estudiante escribe: «La ONU resolvió todos los conflictos porque tenía la Declaración». ¿Qué le falta a su afirmación? A) Evidencia y el reconocimiento de límites B) Citar a más líderes", "A) Evidencia y el reconocimiento de límites", "Una afirmación así necesita pruebas y reconocer límites."),
    sc=[("¿Qué es una tesis?", "La idea central que se defiende con evidencias", "Así se define en el vocabulario."),
        ("¿Qué es un pacto según la clase?", "Un tratado entre Estados que los obliga a cumplirlo", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un marco regulador?", "Un conjunto de reglas e instituciones que ordena las relaciones entre países", "Así se define en el vocabulario de la clase.")],
    op=("Escribe un párrafo de cinco a siete líneas con una tesis sobre las consecuencias de la Segunda Guerra Mundial en el orden internacional. Usa al menos dos evidencias de la ficha, di qué prueba cada una y reconoce un límite. {F}",
        "Tesis: «La posguerra creó un marco internacional de derechos, pero con límites». Evidencias: la Declaración de 1948 (ideales comunes) y la carta de 1952 (colonias sin gobierno propio). Límite: ninguna fuente muestra la situación en todos los países.",
        ["formula una tesis clara", "usa dos evidencias con su aporte", "reconoce un límite"], ["párrafo escrito", "dos evidencias citadas"], ["no usar evidencias", "decir que todo se resolvió"],
        "Pide que explique qué fuente agregaría para cubrir el límite."),
    reinforce="Explica con tus palabras qué es una interpretación documentada y qué tres partes tiene.",
    extend="Elige un tema que conozcas y escribe una tesis de una línea con una evidencia que la apoye.",
)

# ================================================================ OA 04, clase 6
F = ("Ficha 6 (hechos y dos posiciones de ejemplo). "
     "Hechos: la ONU se fundó en 1945 para mantener la paz; no tiene un ejército propio, y sus misiones de paz dependen de soldados que aportan los países; "
     "la Declaración Universal de Derechos Humanos de 1948 es una declaración, no un tratado; en 1966 se adoptaron dos pactos que sí son tratados; en el Consejo de Seguridad cinco miembros permanentes pueden vetar decisiones. "
     "Posición 1 (de ejemplo): «La ONU y la Declaración fueron un gran avance, porque por primera vez casi todos los países aceptaron ideales comunes sobre derechos.» "
     "Posición 2 (de ejemplo): «La ONU tiene límites serios: el veto de cinco países y la falta de un ejército propio le impiden hacer cumplir los derechos.» "
     "Criterios de un buen debate: afirmar, dar razones y evidencias, considerar un contraargumento y respetar a quien piensa distinto.")
build(
    OA, 6, F,
    use="Aprenderé a debatir con argumentos y respeto sobre el alcance y los límites del nuevo marco internacional: la ONU, la Declaración Universal y la descolonización.",
    prior=["Sé construir una tesis con evidencias.", "Sé qué es la ONU y qué es el veto.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Un debate histórico no busca ganarle a alguien, sino ofrecer argumentos apoyados en evidencias y considerar los de otras personas. Un argumento tiene una afirmación, una razón y una evidencia; un contraargumento es una razón que va en contra de lo afirmado. Las dos posiciones de la ficha usan hechos distintos para sostener conclusiones opuestas.",
        "Sobre la ONU hay consenso en algunos hechos: se fundó en 1945, no tiene ejército propio y cinco miembros permanentes tienen derecho a veto. Pero se discute cuánto ha logrado: unos destacan que fijó ideales comunes de derechos, y otros que no puede hacerlos cumplir. La Declaración de 1948 es una declaración, no un tratado, aunque los pactos de 1966 sí obligan a los Estados que los firman.",
        "Para debatir con rigor, separa lo probado de lo que se interpreta y reconoce el límite de tu argumento. Si dices que sin el veto la ONU habría evitado más conflictos, estás hablando de algo que no ocurrió y no puedes probarlo. Y siempre se debate respetando a quien piensa distinto.",
    ],
    vocab=[("argumento", "afirmación apoyada en una razón y en una evidencia"), ("contraargumento", "razón que va en contra de una afirmación"), ("misión de paz", "operación de la ONU para ayudar a mantener la paz en una zona de conflicto"), ("consenso", "acuerdo de la mayoría o de todos sobre un punto"), ("límite", "aspecto que un argumento no alcanza a probar")],
    worked=[
        ("Separar hecho e interpretación", "«La ONU no tiene un ejército propio» y «la ONU fracasó». ¿Cuál es un hecho?", ["La primera frase se comprueba con la ficha.", "La segunda es una valoración."], "La primera es un hecho"),
        ("Calcular un plazo", "¿Cuántos años pasaron entre la fundación de la ONU y la adopción de los pactos de 1966?", ["Tomo 1945 y 1966.", "Resto: 1966 − 1945 = 21."], "21 años"),
    ],
    mistakes=[("Defender una posición sin considerar el contraargumento.", "Se cree que reconocer otra razón debilita la propia.", "Presenta la razón contraria y explica por qué tu evidencia pesa más."),
              ("Afirmar que la ONU nunca sirvió de nada.", "Se generaliza a partir de sus límites.", "Reconoce tanto los avances como los límites con evidencias.")],
    T=[
        ("{F} ¿Qué dice la posición 2 sobre la ONU?", "Que tiene límites serios, como el veto y la falta de un ejército propio", "Así lo resume la posición 2."),
        ("{F} ¿Cuántos miembros permanentes pueden vetar decisiones del Consejo de Seguridad?", "Cinco", "La ficha lo indica."),
        ("{F} ¿De dónde salen los soldados de las misiones de paz de la ONU?", "De los países que los aportan", "La ficha dice que dependen de soldados que aportan los países."),
        ("{F} ¿Qué son los pactos de 1966? A) Tratados obligatorios para los Estados que los firman B) Declaraciones de ideales sin fuerza obligatoria", "A) Tratados obligatorios para los Estados que los firman", "La ficha los distingue de la Declaración de 1948, que no es un tratado."),
        ("{F} ¿Qué razón da la posición 1? A) Casi todos los países aceptaron por primera vez ideales comunes sobre derechos B) El veto de cinco países limita a la ONU", "A) Casi todos los países aceptaron por primera vez ideales comunes sobre derechos", "El veto es una razón de la posición 2."),
        ("{F} ¿Cuál de estas frases es un hecho comprobable? A) La ONU se fundó en 1945 B) La ONU fracasó", "A) La ONU se fundó en 1945", "Tiene fecha y se comprueba; decir que la ONU fracasó es una valoración."),
        ("{F} ¿Qué elemento falta en este argumento: «La ONU es inútil»? A) Una razón y una evidencia B) Un dato sobre dónde se fundó", "A) Una razón y una evidencia", "Un argumento tiene afirmación, razón y evidencia."),
        ("{F} La posición 1 dice que la Declaración fue un gran avance. ¿Qué contraargumento le corresponde? A) Es una declaración y no un tratado, por lo que no obliga B) Fue aprobada en París", "A) Es una declaración y no un tratado, por lo que no obliga", "Es la razón que limita el avance; el lugar es solo un dato."),
        ("{F} Quieres defender la posición 1 con respeto. ¿Qué haces? A) Presentar tu argumento y reconocer el límite del veto B) Decir que quien critica a la ONU no entiende nada", "A) Presentar tu argumento y reconocer el límite del veto", "Un buen debate considera el contraargumento y respeta a las personas."),
        ("{F} ¿Qué evidencia de la ficha apoya mejor la posición 2? A) El veto de cinco miembros y la falta de ejército propio B) La Declaración fue de 1948", "A) El veto de cinco miembros y la falta de ejército propio", "Son los límites que cita la posición 2."),
        ("{F} ¿Por qué no se puede probar que sin el veto la ONU habría evitado más conflictos?", "Porque habla de algo que no ocurrió y no hay forma de comprobarlo", "Es una hipótesis sobre un hecho que no sucedió."),
        ("{F} Un compañero dice: «Los pactos de 1966 prueban que ya no hubo violaciones de derechos». ¿Qué corrección haces? A) Obligan a los Estados que los firman, pero adoptarlos no prueba que se cumplan B) Tiene razón porque son tratados", "A) Obligan a los Estados que los firman, pero adoptarlos no prueba que se cumplan", "Un tratado obliga, pero eso no garantiza su cumplimiento."),
        ("{F} ¿Qué afirmación respeta mejor los límites de la evidencia? A) La ONU fijó ideales comunes de derechos, pero su capacidad de hacerlos cumplir es limitada B) La ONU lo hizo todo bien", "A) La ONU fijó ideales comunes de derechos, pero su capacidad de hacerlos cumplir es limitada", "Integra los avances y los límites de ambas posiciones."),
    ],
    ctx=("En un debate, una estudiante dice «La ONU es un fracaso y punto». ¿Qué le falta? A) Una razón y una evidencia que lo apoyen B) Tener más seguidores en la sala", "A) Una razón y una evidencia que lo apoyen", "Una opinión sin razones no es un argumento."),
    sc=[("¿Qué es un contraargumento?", "Una razón que va en contra de una afirmación", "Así se define en la clase."),
        ("¿Qué es un consenso?", "Un acuerdo de la mayoría o de todos sobre un punto", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una misión de paz?", "Una operación de la ONU para ayudar a mantener la paz en una zona de conflicto", "Así se define en el vocabulario de la clase.")],
    op=("Elige la posición 1 o la posición 2. Escribe un argumento de cuatro a seis líneas con afirmación, razón y una evidencia de la ficha, y agrega un contraargumento con su respuesta. Usa un tono respetuoso. {F}",
        "Posición 2: «La ONU tiene límites (afirmación), porque cinco países pueden vetar decisiones (razón), según la ficha (evidencia). Contraargumento: fijó ideales comunes; respuesta: los ideales no obligan sin tratados».",
        ["incluye afirmación, razón y evidencia", "considera un contraargumento", "usa tono respetuoso"], ["argumento escrito", "contraargumento y respuesta"], ["no usar evidencia", "ignorar la otra posición"],
        "Pide que distinga en su texto un hecho de una interpretación."),
    reinforce="Explica a alguien de tu casa la diferencia entre un hecho y una valoración con un ejemplo sobre la ONU.",
    extend="Anota una norma de tu escuela que te parezca útil y apóyala con una razón y una evidencia.",
)
