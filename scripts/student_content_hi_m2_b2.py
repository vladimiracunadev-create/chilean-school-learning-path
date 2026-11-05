"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 10 (revolución, reforma y dictaduras en América Latina) y OA 11 (fin de la Guerra Fría, neoliberalismo y globalización)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 10"

# ================================================================ OA 10, clase 1
F = ("Ficha 1 (hechos del siglo XX; las definiciones valen para esta clase). "
     "Revolución: cambio rápido y profundo del orden político y social, que suele usar la fuerza. "
     "Reforma: cambio gradual, hecho por las leyes y las instituciones que ya existen. "
     "Golpe de Estado: toma del poder por la fuerza, fuera de lo que permite la constitución. "
     "Dictadura: gobierno sin elecciones libres y sin límites legales efectivos a su poder. "
     "Hitos: golpe contra el presidente Árbenz en Guatemala, 1954; triunfo de la Revolución cubana, 1959; Alianza para el Progreso (programa de ayuda y reformas impulsado por Estados Unidos), 1961; "
     "golpe de Estado en Brasil, 1964; golpes de Estado en Chile y en Uruguay, 1973; golpe de Estado en Argentina, 1976. "
     "Contexto: Guerra Fría, la rivalidad entre Estados Unidos y la Unión Soviética (URSS).")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo y entre sus actores la tensión entre revolución y reforma en América Latina, y a distinguir revolución, reforma, golpe de Estado y dictadura.",
    prior=["Sé qué fue la Guerra Fría y quiénes eran las dos superpotencias.", "Sé ubicar un año dentro de su siglo y calcular diferencias entre años.", "Sé qué es un derecho y qué es una constitución."],
    explain=[
        "Entre 1950 y 1980 muchos sectores de América Latina exigieron cambios: campesinos sin tierra, obreros, estudiantes y habitantes pobres de las ciudades. Hubo dos caminos. La reforma busca cambios graduales por medio de las leyes y las instituciones. La revolución busca un cambio rápido y profundo del orden político y social, y a menudo usa la fuerza. Esa tensión entre ambos caminos marcó la época.",
        "La Guerra Fría hizo más intensa esa tensión. Estados Unidos temía que gobiernos cercanos a la URSS surgieran en la región, y la Revolución cubana de 1959 aumentó ese temor. Desde 1954 hubo golpes de Estado, que son tomas del poder por la fuerza fuera de lo que permite la constitución. Varios terminaron en dictaduras, es decir, gobiernos sin elecciones libres y sin límites legales efectivos.",
        "Muchas dictaduras violaron los derechos humanos, que son los derechos que tiene toda persona por el solo hecho de serlo. Para estudiar el tema hay que preguntar qué actores participaron, en qué año y en qué país. Un golpe de Estado no es lo mismo que una revolución, aunque ambos usen la fuerza.",
    ],
    vocab=[("reforma", "cambio gradual hecho por las leyes y las instituciones que ya existen"), ("revolución", "cambio rápido y profundo del orden político y social, que suele usar la fuerza"), ("golpe de Estado", "toma del poder por la fuerza, fuera de lo que permite la constitución"), ("dictadura", "gobierno sin elecciones libres y sin límites legales efectivos a su poder"), ("derechos humanos", "derechos que tiene toda persona por el hecho de serlo")],
    worked=[
        ("Clasificar un hecho", "Un presidente propone una ley para comprar tierras a los grandes dueños y venderlas a campesinos con créditos, y el Congreso la aprueba. ¿Es reforma o revolución?", ["Se hace por una ley aprobada en el Congreso.", "El cambio sigue las instituciones existentes."], "Reforma"),
        ("Calcular una distancia en el tiempo", "¿Cuántos años pasaron entre el golpe de Estado en Brasil (1964) y el de Argentina (1976)?", ["Tomo los dos años de la ficha.", "Resto: 1976 − 1964 = 12."], "12 años"),
    ],
    mistakes=[("Escribir que golpe de Estado y revolución significan lo mismo.", "Ambos usan la fuerza, pero el golpe toma el poder fuera de la constitución y la revolución cambia el orden social en profundidad.", "Define cada uno por separado y pregunta qué cambió además del gobierno."),
              ("Poner todas las dictaduras en el mismo año.", "No se distingue cada país ni su cronología.", "Ubica cada golpe con su país y su año.")],
    T=[
        ("{F} ¿En qué año triunfó la Revolución cubana?", "1959", "La ficha lo indica entre sus hitos."),
        ("{F} ¿Cómo define la ficha un golpe de Estado?", "Una toma del poder por la fuerza, fuera de lo que permite la constitución", "La ficha da esa definición."),
        ("{F} ¿Qué dos países sufrieron golpes de Estado en 1973?", "Chile y Uruguay", "Son los dos que la ficha asigna a 1973."),
        ("=", "{F} ¿Cuántos años pasaron entre el triunfo de la Revolución cubana y el golpe de Estado en Brasil?", "1964-1959", "Se resta el año de la revolución al del golpe.", " años"),
        ("{F} ¿Qué es la Alianza para el Progreso, según la ficha?", "Un programa de ayuda y reformas impulsado por Estados Unidos, lanzado en 1961", "La ficha la define así y la ubica en 1961."),
        ("{F} Un gobierno aprueba en el Congreso una ley que reparte tierras en diez años. ¿Qué camino sigue? A) Reforma B) Revolución", "A) Reforma", "Cambia por vía legal e institucional, lo propio de una reforma."),
        ("{F} Un grupo armado toma el poder y luego cambia la propiedad de la tierra y de las empresas en pocos meses. ¿Qué se parece más? A) Revolución B) Reforma", "A) Revolución", "Es un cambio rápido y profundo del orden social por la fuerza."),
        ("{F} Un general ordena ocupar el palacio de gobierno y cerrar el Congreso, aunque la constitución no lo permite. ¿Qué es? A) Golpe de Estado B) Revolución", "A) Golpe de Estado", "Es una toma del poder fuera de la constitución; la revolución se define por un cambio profundo del orden social, no solo por quién gobierna."),
        ("{F} ¿Por qué se habla de «tensión entre revolución y reforma» en la época?", "Porque unos sectores querían cambios rápidos y profundos y otros cambios graduales por las leyes", "La ficha define ambos caminos como opciones distintas que competían."),
        ("{F} Un compañero dice: «En 1973 hubo golpes en todos los países de América Latina». ¿Qué respondes? A) La ficha solo nombra a Chile y Uruguay en 1973 B) Tiene razón porque era la Guerra Fría", "A) La ficha solo nombra a Chile y Uruguay en 1973", "El contexto no prueba que ocurriera en todos los países."),
        ("{F} Ordena de más antiguo a más reciente: a) golpe en Brasil b) Revolución cubana c) golpe en Argentina d) Alianza para el Progreso.", "b, d, a, c", "Las fechas son 1959, 1961, 1964 y 1976."),
        ("{F} ¿Por qué la Guerra Fría ayuda a explicar el interés de Estados Unidos por lo que ocurría en la región?", "Porque rivalizaba con la URSS y temía que países de la región se acercaran a ella", "La rivalidad entre superpotencias es el contexto que da la ficha."),
        ("¿Cuál es la mejor pregunta guía para este tema? A) ¿Cómo se enfrentaron proyectos de reforma y de revolución en América Latina entre 1954 y 1976 y qué consecuencias tuvo para los derechos humanos? B) ¿Qué país latinoamericano tuvo el mejor presidente?", "A) ¿Cómo se enfrentaron proyectos de reforma y de revolución en América Latina entre 1954 y 1976 y qué consecuencias tuvo para los derechos humanos?", "La pregunta A tiene tiempo, lugar y se responde con hechos; la B es una opinión."),
    ],
    ctx=("Una línea de tiempo escolar rotula «Reforma: 1973» junto al golpe de Estado en Chile. ¿Qué error tiene? A) Llama reforma a un golpe de Estado, que toma el poder por la fuerza fuera de la constitución y no es un cambio gradual por las leyes B) Debería poner 1976, el año en que ocurrió ese golpe", "A) Llama reforma a un golpe de Estado, que toma el poder por la fuerza fuera de la constitución y no es un cambio gradual por las leyes", "La ficha define reforma y golpe de Estado como procesos distintos y fecha el golpe en Chile en 1973."),
    sc=[("En Historia: ¿qué es una reforma?", "Un cambio gradual hecho por las leyes y las instituciones que ya existen", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una dictadura?", "Un gobierno sin elecciones libres y sin límites legales efectivos a su poder", "Así se define en la clase."),
        ("En Historia: ¿qué es un golpe de Estado?", "Una toma del poder por la fuerza, fuera de lo que permite la constitución", "Así se define en el vocabulario.")],
    op=("Dibuja una línea de tiempo de 1950 a 1980 con escala 1 cm = 5 años. Marca con una raya y el país: golpe en Guatemala (1954), Revolución cubana (1959), Alianza para el Progreso (1961), golpe en Brasil (1964), golpes en Chile y Uruguay (1973) y golpe en Argentina (1976). Debajo escribe dos frases: una que defina reforma y otra que defina revolución. {F}",
        "Posiciones desde 1950: 0,8 cm; 1,8 cm; 2,2 cm; 2,8 cm; 4,6 cm; 5,2 cm. Frases: «La reforma cambia de forma gradual por las leyes»; «La revolución cambia rápido y a fondo el orden social, a menudo por la fuerza».",
        ["respeta la escala", "ubica los seis hitos con su país", "las dos definiciones son distintas y correctas"], ["línea de tiempo dibujada", "dos frases escritas"], ["marcar los hitos sin medir", "definir reforma y revolución con las mismas palabras"],
        "Pide que explique por qué un golpe de Estado no es lo mismo que una revolución."),
    reinforce="Explica en voz alta la diferencia entre reforma y revolución con un ejemplo inventado por ti.",
    extend="Averigua con una persona de tu casa qué recuerda o ha oído sobre la Guerra Fría y anota una frase.",
)

# ================================================================ OA 10, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, discurso de un dirigente campesino, 1962, en la plaza de un pueblo: «La tierra de la hacienda lleva años sin cultivarse; pedimos que la ley la reparta entre quienes la trabajan.» "
     "Fuente B, informe de un diplomático extranjero a su gobierno, 1962, escrito en la capital: «El reparto de tierras podría acercar al país a gobiernos hostiles a nuestros intereses; conviene apoyar a los sectores moderados.» "
     "Fuente C, testimonio de una profesora entregado en 1985 a una comisión que recibe denuncias: «En 1975 me despidieron del colegio sin explicación ni juicio y no pude volver a trabajar en mi oficio.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre el período con las preguntas de procedencia: quién habla, cuándo, desde dónde, para qué y qué calla.",
    prior=["Sé qué es una fuente histórica.", "Sé distinguir reforma, revolución, golpe de Estado y dictadura.", "Sé calcular diferencias entre años."],
    explain=[
        "La procedencia de una fuente es su origen: quién la produjo, cuándo, dónde y con qué propósito. Una fuente no es un relato neutral. Un discurso busca convencer, un informe diplomático busca informar a un gobierno y recomendarle decisiones, y un testimonio es un recuerdo de una persona sobre lo que vivió, a veces contado años después.",
        "Cada fuente dice algo y también calla algo. El discurso del dirigente muestra qué pedían los campesinos, pero no dice qué opinaban los dueños. El informe muestra cómo veía un país extranjero el reparto de tierras, pero no escucha a los campesinos. Por eso se contrastan las fuentes: se comparan para ver en qué coinciden, en qué se oponen y qué falta.",
        "Una buena conclusión es proporcional a la evidencia. De un solo testimonio se puede afirmar lo que esa persona vivió, no lo que vivieron todas. Cuando varios testimonios coinciden y se apoyan en otros registros, la afirmación se fortalece. Para los derechos humanos, los testimonios y los documentos oficiales se usan juntos.",
    ],
    vocab=[("procedencia", "origen de una fuente: autor, fecha, lugar y propósito"), ("propósito", "lo que el autor de una fuente quiere lograr con ella"), ("contrastar", "comparar fuentes para ver coincidencias, diferencias y vacíos"), ("testimonio", "relato de una persona sobre lo que vivió o presenció"), ("silencio de una fuente", "aquello que la fuente no menciona")],
    worked=[
        ("Identificar el propósito", "Un afiche de 1968 dice: «Vota por la reforma». ¿Cuál es su propósito más probable?", ["Un afiche se pega en la calle para llegar a muchas personas.", "Pide una acción concreta: votar."], "Convencer de votar por la reforma"),
        ("Medir la distancia de un testimonio", "Una persona declara en 1991 sobre algo que vivió en 1977. ¿Cuántos años después declara?", ["Tomo ambos años.", "1991 − 1977 = 14."], "14 años"),
    ],
    mistakes=[("Tratar un discurso como si describiera lo que pensaba toda la población.", "Se olvida que el discurso es de una persona con un propósito.", "Pregunta quién habla y a quién quiere convencer."),
              ("Descartar un testimonio solo porque se contó años después.", "Se confunde distancia en el tiempo con falsedad; lo correcto es contrastarlo con otras fuentes.", "Anota la fecha del relato y busca otras fuentes que lo confirmen o corrijan.")],
    T=[
        ("{F} ¿Quién produjo la fuente A?", "Un dirigente campesino", "La ficha lo indica como su autor."),
        ("{F} ¿En qué año se escribió el informe de la fuente B?", "1962", "La ficha lo fecha en 1962."),
        ("{F} ¿Qué hecho cuenta la fuente C?", "Que la despidieron del colegio sin explicación ni juicio", "El testimonio relata ese despido."),
        ("=", "{F} ¿Cuántos años pasaron entre los hechos que cuenta la fuente C y el momento en que se entregó el testimonio?", "1985-1975", "Se resta el año de los hechos al del testimonio.", " años"),
        ("{F} ¿Cuál es el propósito más probable de la fuente B? A) Informar a su gobierno y recomendarle qué hacer B) Convencer a la población del país de apoyar la reforma", "A) Informar a su gobierno y recomendarle qué hacer", "Es un informe dirigido a su propio gobierno, no un discurso público."),
        ("{F} ¿Qué se puede afirmar con la fuente A? A) Que un dirigente campesino pedía repartir la tierra por ley B) Que todos los campesinos del continente pedían lo mismo", "A) Que un dirigente campesino pedía repartir la tierra por ley", "Una sola fuente no prueba lo que pensaba todo un grupo en todos los países."),
        ("{F} ¿Qué guarda silencio la fuente B? A) La opinión de los campesinos sobre el reparto B) La fecha del informe", "A) La opinión de los campesinos sobre el reparto", "El informe habla de intereses extranjeros y no da voz a los campesinos."),
        ("{F} La fuente A fue dicha en 1962 y la C se recogió en 1985. ¿Cuál es el motivo principal para tomar con cuidado la C? A) Es un recuerdo contado años después y debe contrastarse B) Los testimonios siempre son falsos", "A) Es un recuerdo contado años después y debe contrastarse", "La memoria y la distancia en el tiempo piden contrastar el testimonio."),
        ("{F} ¿Por qué A y B, juntas, permiten conocer mejor el conflicto por la tierra que cada una por separado?", "Porque muestran la demanda de los campesinos y la mirada de un país extranjero, dos perspectivas distintas", "Contrastar perspectivas completa los vacíos de cada fuente."),
        ("{F} Un compañero concluye: «La fuente C demuestra que a todos los profesores del país los despidieron». ¿Qué corrección haces? A) Solo prueba lo que vivió esa profesora, hacen falta más fuentes B) Está bien porque es un testimonio", "A) Solo prueba lo que vivió esa profesora, hacen falta más fuentes", "Una conclusión debe ser proporcional a la evidencia."),
        ("{F} Un compañero dice: «El informe B es verdad absoluta porque es de un diplomático». ¿Qué falla en su razonamiento?", "Que un informe tiene autor, intereses y propósito, y debe contrastarse con otras fuentes", "Ninguna fuente es neutral solo por la posición de quien la escribe."),
        ("{F} ¿Qué segunda fuente ayudaría más a comprobar lo que cuenta la fuente C? A) Un registro de la época sobre la contratación y el despido de profesores del colegio B) Un discurso de un político de otro país sobre la economía", "A) Un registro de la época sobre la contratación y el despido de profesores del colegio", "Debe tratar el mismo hecho para confirmarlo o corregirlo."),
        ("{F} ¿Cuál de estas preguntas interroga mejor la procedencia de la fuente A? A) ¿Quién habla, ante quién y qué quiere lograr con su discurso? B) ¿Qué dice el discurso sobre la tierra de la hacienda?", "A) ¿Quién habla, ante quién y qué quiere lograr con su discurso?", "La procedencia es autor, lugar, fecha y propósito."),
    ],
    ctx=("En un museo, un panel pone solo la fuente B y concluye que «la región entera rechazaba el reparto de tierras». ¿Qué falta para sostener esa conclusión? A) Fuentes de campesinos, dueños y otros actores B) Una segunda fuente diplomática del mismo país", "A) Fuentes de campesinos, dueños y otros actores", "Una sola perspectiva no representa a todos los actores."),
    sc=[("En Historia: ¿qué es la procedencia de una fuente?", "Su origen: autor, fecha, lugar y propósito", "Así se define en el vocabulario."),
        ("¿Qué significa contrastar fuentes?", "Compararlas para ver coincidencias, diferencias y vacíos", "Así se explica en la clase."),
        ("En Historia: ¿por qué debe contrastarse un testimonio entregado años después?", "Porque es un recuerdo y conviene compararlo con otras fuentes para confirmarlo o corregirlo", "La distancia en el tiempo pide contrastar, no descartar.")],
    op=("Escribe una tabla con tres columnas (autor y fecha, propósito, qué calla) para las fuentes A, B y C. Después redacta una conclusión de dos frases que use al menos dos fuentes y que no afirme más de lo que ellas permiten. {F}",
        "A: dirigente campesino, 1962; busca convencer de repartir tierra; calla la opinión de los dueños. B: diplomático, 1962; informa y recomienda a su gobierno; calla a los campesinos. C: profesora, 1985; denuncia un despido; calla otros casos. Conclusión: «En 1962 había quienes pedían repartir la tierra y quienes, desde fuera, temían sus efectos; los testimonios como el de 1985 muestran vivencias individuales que deben contrastarse».",
        ["completa autor, fecha, propósito y silencio de cada fuente", "usa al menos dos fuentes", "la conclusión es proporcional a la evidencia"], ["tabla completa", "conclusión de dos frases"], ["generalizar a partir de una sola fuente", "confundir propósito con contenido"],
        "Pide que explique qué otra fuente agregaría para dar voz a un actor que falta."),
    reinforce="Elige un mensaje que recibiste hoy y di quién lo envió, para qué y qué calla.",
    extend="Piensa en una noticia que hayas oído y pregunta: ¿qué fuente la contradiría o la completaría?",
)

# ================================================================ OA 10, clase 3
F = ("Ficha 3 (hechos y datos de ejemplo). "
     "Hechos: en 1954 un golpe de Estado derriba en Guatemala al presidente Árbenz, que había impulsado una reforma agraria; en 1959 triunfa la Revolución cubana; en 1961 Estados Unidos lanza la Alianza para el Progreso, con ayuda económica a cambio de reformas. "
     "Perspectivas de ejemplo sobre un reparto de tierras: campesino («la tierra debe ser de quien la trabaja»), dueño de hacienda («es una expropiación injusta»), gobierno reformista («hay que repartir con ley y pago»), gobierno extranjero («puede favorecer a la URSS»). "
     "Escalas: local (una hacienda), nacional (un país), continental (la región en la Guerra Fría). "
     "Dato de ejemplo: una hacienda de 2.000 hectáreas cultiva solo 500 y 40 familias trabajan en ella como inquilinas.")
build(
    OA, 3, F,
    use="Aprenderé a comparar las perspectivas de distintos actores y a mirar un mismo hecho en escala local, nacional y continental.",
    prior=["Sé distinguir reforma y revolución.", "Sé interrogar la procedencia de una fuente.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Un mismo hecho se ve distinto según quién lo mire. En un reparto de tierras, el campesino lo ve como justicia, el dueño como pérdida de su propiedad, el gobierno reformista como una solución con ley y pago, y un gobierno extranjero como un riesgo político en plena Guerra Fría. Comparar perspectivas no significa que todas valgan igual: significa entender qué argumento y qué interés tiene cada actor.",
        "También importa la escala, que es el nivel desde el que miramos. En escala local se ve una hacienda y las familias que viven en ella. En escala nacional se ven las leyes, los partidos y la economía del país. En escala continental se ve cómo la rivalidad entre Estados Unidos y la URSS influía en las decisiones de muchos gobiernos.",
        "Para comparar bien se usa una matriz: se pone cada actor, su argumento, su interés y la escala en que actúa. Así se evita quedarse con una sola voz. Después se redacta una conclusión que diga en qué coinciden y en qué se oponen las perspectivas, sin afirmar más de lo que muestran los datos.",
    ],
    vocab=[("perspectiva", "forma de mirar un hecho según la posición y los intereses de quien lo mira"), ("escala", "nivel desde el que se analiza un hecho: local, nacional o continental"), ("expropiación", "traspaso obligatorio de una propiedad al Estado, por lo general con una compensación"), ("inquilino", "campesino que vivía y trabajaba en una hacienda a cambio de un pequeño terreno"), ("interés", "lo que un actor quiere lograr o conservar")],
    worked=[
        ("Reconocer una escala", "«Las 40 familias de una hacienda esperan la decisión sobre la tierra». ¿Qué escala usa esta frase?", ["Habla de una hacienda y de sus familias.", "No habla de todo el país ni de la región."], "Escala local"),
        ("Calcular qué parte se usa", "En otra hacienda de ejemplo de 800 hectáreas se cultivan 200. ¿Qué porcentaje se cultiva?", ["Divido lo cultivado por el total: 200 ÷ 800 = 0,25.", "Lo paso a porcentaje: 25 %."], "25 %"),
    ],
    mistakes=[("Creer que comparar perspectivas es decir que todas tienen razón.", "Se confunde entender los argumentos con aceptarlos todos.", "Explica cada argumento con sus intereses y luego evalúa cuáles tienen más evidencia."),
              ("Explicar un golpe solo por lo que pasó dentro del país.", "Se ignora la escala continental de la Guerra Fría.", "Pregunta qué influencias externas había y qué evidencias las muestran.")],
    T=[
        ("{F} ¿Qué actor dice «es una expropiación injusta»?", "El dueño de hacienda", "La ficha asigna esa frase al dueño."),
        ("{F} ¿Qué año se lanzó la Alianza para el Progreso?", "1961", "La ficha lo indica."),
        ("{F} ¿Qué escala usa el análisis de lo que ocurrió en una sola hacienda?", "La escala local", "La ficha define lo local como una hacienda."),
        ("=", "{F} ¿Cuántas hectáreas de la hacienda de ejemplo no se cultivan?", "2000-500", "Se resta lo cultivado al total.", " hectáreas"),
        ("=", "{F} ¿Qué porcentaje de la hacienda de ejemplo se cultiva?", "500/2000*100", "Se divide lo cultivado por el total y se multiplica por cien.", " %"),
        ("{F} ¿Quién ve el reparto como una solución «con ley y pago»? A) El gobierno reformista B) El gobierno extranjero", "A) El gobierno reformista", "La ficha le asigna esa frase al gobierno reformista."),
        ("{F} Un diario dice: «El reparto de tierras divide a los partidos del país». ¿Qué escala usa? A) Nacional B) Local", "A) Nacional", "Habla de partidos y del país entero."),
        ("{F} ¿Qué perspectiva explica mejor que el gobierno extranjero mirara con recelo el reparto? A) Temía que el país se acercara a la URSS en la Guerra Fría B) Quería defender los intereses del dueño de la hacienda", "A) Temía que el país se acercara a la URSS en la Guerra Fría", "La ficha le atribuye ese interés."),
        ("{F} ¿Por qué el campesino y el dueño no llegan a la misma conclusión sobre el reparto?", "Porque tienen intereses distintos: uno quiere la tierra y el otro conservar su propiedad", "El interés de cada actor explica su perspectiva."),
        ("{F} Un compañero dice: «Comparar perspectivas es aceptar que todas tienen la misma razón». ¿Qué corrección haces? A) Es entender los argumentos y luego evaluar cuál tiene más evidencia B) Es aceptar que el campesino siempre tiene razón", "A) Es entender los argumentos y luego evaluar cuál tiene más evidencia", "Comparar exige entender y evaluar, no aceptar todo."),
        ("{F} Un trabajo explica el golpe de 1954 en Guatemala solo con peleas entre partidos locales. ¿Qué escala le falta? A) La continental, por la Guerra Fría B) La local, por las haciendas", "A) La continental, por la Guerra Fría", "La ficha muestra influencias de la rivalidad entre superpotencias."),
        ("{F} ¿Qué dato apoya mejor el argumento del campesino de que la tierra está mal repartida?", "Que la hacienda de 2.000 hectáreas cultiva solo 500 y 40 familias trabajan en ella como inquilinas", "Ese dato de ejemplo muestra mucha tierra sin cultivar y familias dependientes."),
        ("{F} ¿Cuál es una conclusión proporcional a la ficha? A) Los actores tenían intereses distintos sobre el reparto y la Guerra Fría añadía una mirada externa B) Todos los países tuvieron la misma reforma agraria", "A) Los actores tenían intereses distintos sobre el reparto y la Guerra Fría añadía una mirada externa", "La ficha no afirma que todos los países hicieran lo mismo."),
    ],
    ctx=("Una radio presenta un debate sobre una reforma de tierras con tres invitados: un campesino, un dueño y un político reformista. ¿Qué perspectiva falta para tener una mirada continental? A) La de un gobierno extranjero con intereses en la región B) La de un segundo campesino", "A) La de un gobierno extranjero con intereses en la región", "La escala continental incluye la rivalidad entre superpotencias."),
    sc=[("En Historia: ¿qué es una perspectiva?", "Una forma de mirar un hecho según la posición y los intereses de quien lo mira", "Así se define en la clase."),
        ("Nombra las tres escalas de la ficha.", "Local, nacional y continental", "La ficha las enumera."),
        ("En Historia: ¿qué es una expropiación?", "El traspaso obligatorio de una propiedad al Estado, por lo general con una compensación", "Así se define en el vocabulario.")],
    op=("Arma una matriz con los cuatro actores de la ficha (campesino, dueño, gobierno reformista, gobierno extranjero): para cada uno escribe su argumento, su interés y su escala. Después redacta tres frases: en qué coinciden dos actores, en qué se oponen dos y qué dato de la ficha usarías para evaluar. {F}",
        "Campesino: la tierra debe ser de quien la trabaja; interés, tierra; escala local. Dueño: expropiación injusta; interés, conservar la propiedad; local y nacional. Gobierno reformista: repartir con ley y pago; interés, cambiar por vías legales; nacional. Gobierno extranjero: riesgo ante la URSS; interés político; continental. Dato: 500 de 2.000 hectáreas cultivadas.",
        ["completa los cuatro actores", "separa argumento, interés y escala", "usa un dato para evaluar"], ["matriz completa", "tres frases"], ["repetir el mismo argumento para dos actores", "no distinguir interés de argumento"],
        "Pide que explique por qué comparar no es lo mismo que estar de acuerdo con todos."),
    reinforce="Elige un conflicto de tu curso y di cómo lo ve cada parte y cuál es su interés.",
    extend="Busca un hecho que se vea distinto en escala local y en escala nacional y explica la diferencia.",
)

# ================================================================ OA 10, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; datos de ejemplo cuando se indica). "
     "Causas de largo plazo: desigualdad en la propiedad de la tierra y en los ingresos; organización de campesinos, obreros y estudiantes que pedían cambios; el temor de las élites y de las fuerzas armadas a una revolución como la cubana. "
     "Causas externas: la Guerra Fría, que hizo que Estados Unidos apoyara a gobiernos anticomunistas, incluidos algunos militares. "
     "Idea de la época: la Doctrina de Seguridad Nacional sostenía que las fuerzas armadas debían combatir a un «enemigo interno», es decir, a opositores políticos. "
     "Cambios bajo las dictaduras: se cerraron congresos, se prohibieron o suspendieron partidos, hubo censura, detenciones sin juicio y desapariciones forzadas (detención por agentes del Estado seguida de la negativa a informar dónde está la persona). "
     "En los años setenta, servicios de seguridad de varias dictaduras del cono sur coordinaron acciones (Operación Cóndor). "
     "Continuidades: la desigualdad y las economías que exportaban materias primas. "
     "Dato de ejemplo: un país con 200 diputados cierra su Congreso y queda con 0.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas, cambios y continuidades en los golpes de Estado y las dictaduras, y a no confundir un contexto con una causa única.",
    prior=["Sé distinguir causas de largo plazo y detonante.", "Sé qué es una dictadura.", "Sé comparar perspectivas."],
    explain=[
        "Los golpes de Estado de la segunda mitad del siglo XX no tuvieron una sola causa. Hubo causas internas, como la desigualdad y la movilización social, y causas externas, como la Guerra Fría. Los sectores que temían una revolución apoyaron en varios casos a las fuerzas armadas. Estados Unidos, por su parte, apoyó a gobiernos anticomunistas. Esto no significa que toda decisión viniera de afuera.",
        "La Doctrina de Seguridad Nacional dio una justificación: según ella, la tarea de las fuerzas armadas era combatir a un enemigo interno. Con esa idea, opositores políticos fueron tratados como amenazas. Los cambios que siguieron fueron graves: congresos cerrados, partidos suspendidos, censura, detenciones sin juicio y desapariciones forzadas. Todo eso son violaciones de derechos humanos.",
        "Además hubo continuidades, es decir, cosas que siguieron igual: la desigualdad y las economías que exportaban materias primas. Y en los años setenta, servicios de varias dictaduras coordinaron sus acciones, lo que muestra que el problema fue regional. Un buen análisis separa causa, cambio y continuidad y no usa «causó» sin evidencia.",
    ],
    vocab=[("enemigo interno", "en la Doctrina de Seguridad Nacional, opositor político al que se consideraba amenaza dentro del país"), ("desaparición forzada", "detención por agentes del Estado seguida de la negativa a informar dónde está la persona"), ("censura", "control previo de lo que se puede publicar o decir"), ("continuidad", "aspecto que sigue igual a pesar de un cambio"), ("causa externa", "factor que viene de fuera del país")],
    worked=[
        ("Distinguir cambio y continuidad", "Después de un golpe se cierra el Congreso, pero la propiedad de la tierra sigue concentrada. ¿Qué es cada cosa?", ["Cerrar el Congreso es algo nuevo: un cambio.", "La concentración de la tierra ya existía y sigue: una continuidad."], "Cierre del Congreso = cambio; concentración de la tierra = continuidad"),
        ("Calcular un cambio en cifras de ejemplo", "Un Congreso de ejemplo tiene 150 diputados y pasa a tener 0. ¿Cuántos diputados desaparecen?", ["Tomo la cifra inicial y la final.", "150 − 0 = 150."], "150 diputados"),
    ],
    mistakes=[("Decir que la Guerra Fría explica por sí sola todos los golpes.", "Se ignoran las causas internas y las decisiones de actores del país.", "Usa «contribuyó a» y separa causas internas y externas."),
              ("Creer que bajo una dictadura cambió todo.", "Se olvidan las continuidades, como la desigualdad.", "Pregunta qué siguió igual antes y después del golpe.")],
    T=[
        ("{F} ¿Qué decía la Doctrina de Seguridad Nacional sobre las fuerzas armadas?", "Que debían combatir a un «enemigo interno»", "La ficha lo indica."),
        ("{F} ¿Qué es una desaparición forzada?", "Una detención por agentes del Estado seguida de la negativa a informar dónde está la persona", "La ficha da esa definición."),
        ("{F} ¿Cómo se llamó la coordinación entre servicios de seguridad de varias dictaduras del cono sur?", "Operación Cóndor", "La ficha lo nombra."),
        ("{F} ¿Qué tres causas de largo plazo nombra la ficha?", "La desigualdad en la propiedad de la tierra y en los ingresos, la organización de campesinos, obreros y estudiantes que pedían cambios, y el temor de las élites y de las fuerzas armadas a una revolución", "La ficha enumera exactamente esas tres."),
        ("{F} ¿Cuál es una causa externa? A) La Guerra Fría y el apoyo de Estados Unidos a gobiernos anticomunistas B) La desigualdad en la propiedad de la tierra", "A) La Guerra Fría y el apoyo de Estados Unidos a gobiernos anticomunistas", "La desigualdad es una causa interna; la rivalidad entre superpotencias viene de fuera."),
        ("{F} ¿Cuál es una continuidad? A) La desigualdad y las economías exportadoras de materias primas B) El cierre de los congresos", "A) La desigualdad y las economías exportadoras de materias primas", "Existían antes de los golpes y siguieron; el cierre de congresos es un cambio."),
        ("{F} Un país suspende los partidos políticos y aplica censura a los diarios. ¿Qué es eso respecto del período anterior? A) Un cambio B) Una continuidad", "A) Un cambio", "En democracia había partidos y libertad de prensa; suspenderlos es un cambio."),
        ("{F} Una familia no sabe dónde está su hijo, detenido por agentes del Estado, y la autoridad no informa. ¿Qué situación describe? A) Una desaparición forzada B) Una censura", "A) Una desaparición forzada", "Hay detención por agentes y negativa a informar el paradero."),
        ("{F} ¿Qué muestra la Operación Cóndor sobre el problema de los derechos humanos en la región?", "Que fue un problema regional en que varias dictaduras coordinaron sus acciones", "La ficha dice que servicios de varias dictaduras coordinaron acciones."),
        ("{F} Un compañero afirma: «Los golpes solo ocurrieron por orden de Estados Unidos». ¿Qué corrección haces? A) Hubo también causas internas, como la desigualdad y el temor de las élites a una revolución B) Es correcto porque había Guerra Fría", "A) Hubo también causas internas, como la desigualdad y el temor de las élites a una revolución", "El contexto externo no elimina las decisiones y causas internas."),
        ("{F} ¿Por qué es riesgoso decir que la Doctrina de Seguridad Nacional «justificó» las violaciones de derechos humanos sin decir de quién era la responsabilidad?", "Porque una doctrina no actúa sola: quienes ordenaron y ejecutaron los actos son responsables", "Las ideas se aplican por personas que deciden y actúan."),
        ("{F} ¿Qué evidencia permitiría probar que una dictadura detuvo a una persona sin juicio? A) Registros oficiales, testimonios y recursos legales presentados en la época B) Un discurso del jefe de gobierno sobre la economía", "A) Registros oficiales, testimonios y recursos legales presentados en la época", "Esas fuentes tratan directamente el hecho."),
        ("{F} ¿Cuál es la mejor síntesis? A) Hubo causas internas y externas, cambios graves en las libertades y continuidades como la desigualdad B) Todo cambió y nada siguió igual", "A) Hubo causas internas y externas, cambios graves en las libertades y continuidades como la desigualdad", "Reúne causas, cambios y continuidades."),
    ],
    ctx=("Un cartel de una exposición dice: «La Guerra Fría fue la única causa de los golpes de Estado». ¿Qué problema tiene? A) Ignora causas internas como la desigualdad y las decisiones de actores locales B) No menciona la Revolución cubana", "A) Ignora causas internas como la desigualdad y las decisiones de actores locales", "La ficha muestra causas internas y externas combinadas."),
    sc=[("En Historia: ¿qué es una continuidad?", "Un aspecto que sigue igual a pesar de un cambio", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es la censura?", "Un control previo de lo que se puede publicar o decir", "Así se define en la clase."),
        ("En Historia: ¿qué es una causa externa?", "Un factor que viene de fuera del país", "Así se define en el vocabulario.")],
    op=("Dibuja un esquema con tres columnas: causas (internas y externas), cambios bajo las dictaduras y continuidades. Pon al menos dos elementos de la ficha en cada columna. Debajo escribe una frase con «contribuyó a…» que evite decir que algo fue la única causa. {F}",
        "Causas internas: desigualdad, movilización, temor de las élites. Externas: Guerra Fría, apoyo de Estados Unidos a gobiernos anticomunistas. Cambios: congresos cerrados, censura, detenciones sin juicio, desapariciones forzadas. Continuidades: desigualdad, exportación de materias primas. Frase: el temor a una revolución contribuyó a que sectores apoyaran los golpes, junto con otras causas.",
        ["pone al menos dos elementos en cada columna", "distingue causas internas y externas", "evita causas únicas"], ["esquema de tres columnas", "frase con «contribuyó a…»"], ["poner la desigualdad como un cambio", "usar «causó por sí sola»"],
        "Pide que explique por qué una dictadura puede cambiar las libertades sin cambiar la desigualdad."),
    reinforce="Explica con tus palabras la diferencia entre un cambio y una continuidad usando un ejemplo de la ficha.",
    extend="Piensa en una regla de tu casa o colegio que cambió y otra que siguió igual, y di por qué.",
)

# ================================================================ OA 10, clase 5
F = ("Ficha 5 (evidencias de ejemplo para construir una interpretación; no son documentos históricos reales). "
     "Tesis de ejemplo: «En varios países de América Latina, la tensión entre reforma y revolución, junto con la Guerra Fría, terminó en golpes de Estado y dictaduras que violaron los derechos humanos.» "
     "Evidencia 1: la Revolución cubana triunfa en 1959 y en 1961 Estados Unidos lanza la Alianza para el Progreso. "
     "Evidencia 2: hay golpes de Estado en Brasil (1964), Chile y Uruguay (1973) y Argentina (1976). "
     "Evidencia 3, decreto de ejemplo de una dictadura: «Se disuelve el Congreso y se suspende toda actividad de los partidos.» "
     "Evidencia 4, testimonio de ejemplo, 1984: «Mi padre fue detenido en su casa por agentes del Estado y las autoridades negaron saber dónde estaba.» "
     "Evidencia 5: en Paraguay un mismo gobierno autoritario duró de 1954 a 1989.")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada: plantear una tesis, apoyarla con evidencias de distintos tipos y reconocer sus límites.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé separar causas, cambios y continuidades.", "Sé qué es una conclusión proporcional a la evidencia."],
    explain=[
        "Una interpretación histórica es una explicación razonada de un proceso. Se construye con una tesis, que es la idea central que defiendes, y con evidencias, que son datos y fuentes que la apoyan. No basta con afirmar algo: hay que mostrar de dónde sale. Cada evidencia debe tener relación directa con la tesis y debe estar fechada y ubicada.",
        "Una buena tesis es clara y proporcional. Si dice «todos los países» o «siempre», necesita mucha evidencia; si dice «en varios países», necesita casos concretos. También conviene incluir evidencias de distinto tipo: hechos con fechas, documentos oficiales y testimonios. Así la interpretación no depende de una sola fuente.",
        "Toda interpretación tiene límites. Por ejemplo, un testimonio muestra una vivencia, no el total de las víctimas. Reconocer los límites no debilita el argumento: lo hace más honesto. En el tema de las violaciones de derechos humanos, la interpretación debe nombrar a las personas afectadas con respeto y basarse en registros y testimonios verificables.",
    ],
    vocab=[("tesis", "idea central que se defiende en una interpretación"), ("evidencia", "dato o fuente que apoya una afirmación"), ("interpretación", "explicación razonada de un proceso histórico apoyada en evidencias"), ("límite de una interpretación", "aquello que la evidencia disponible no permite afirmar"), ("proporcional", "que no afirma más de lo que la evidencia permite")],
    worked=[
        ("Elegir la evidencia que apoya", "Tesis: «Hubo golpes de Estado en el cono sur en los años setenta». ¿Qué evidencia de la ficha la apoya?", ["Busco hechos de los años setenta en el cono sur.", "Chile y Uruguay en 1973 y Argentina en 1976."], "La evidencia 2"),
        ("Calcular una duración", "Un gobierno autoritario de ejemplo duró de 1964 a 1985. ¿Cuántos años duró?", ["Tomo el inicio y el fin.", "1985 − 1964 = 21."], "21 años"),
    ],
    mistakes=[("Escribir una tesis que dice «todos los países» sin evidencias de todos.", "Se afirma más de lo que se puede probar.", "Cambia a «varios países» o agrega evidencia de cada país."),
              ("Apoyar la tesis solo con una opinión.", "Una opinión no es una evidencia verificable.", "Agrega hechos fechados, documentos o testimonios.")],
    T=[
        ("{F} ¿En qué año comenzó el gobierno autoritario de Paraguay de la evidencia 5?", "1954", "La evidencia 5 dice que duró de 1954 a 1989."),
        ("{F} ¿Qué tipo de fuente es la evidencia 4?", "Un testimonio", "Relata lo que vivió una persona."),
        ("{F} ¿Qué dice la evidencia 3 sobre los partidos?", "Que se suspende toda su actividad", "El decreto de ejemplo lo establece."),
        ("=", "{F} ¿Cuántos años duró el gobierno autoritario de Paraguay de la evidencia 5?", "1989-1954", "Se resta el año de inicio al de término.", " años"),
        ("{F} ¿Qué evidencia apoya mejor que hubo golpes en distintos países? A) La evidencia 2 B) La evidencia 4", "A) La evidencia 2", "Lista golpes en Brasil, Chile, Uruguay y Argentina."),
        ("{F} ¿Qué evidencia muestra una violación de derechos humanos, desde la vivencia de una familia? A) La evidencia 4 B) La evidencia 1", "A) La evidencia 4", "El testimonio relata una detención con negativa a informar el paradero."),
        ("{F} ¿Cuál es una reformulación más proporcional de la tesis? A) En varios países hubo golpes y dictaduras que violaron los derechos humanos B) En todos los países hubo siempre dictaduras", "A) En varios países hubo golpes y dictaduras que violaron los derechos humanos", "«Todos» y «siempre» afirman más de lo que la ficha permite."),
        ("{F} Un compañero apoya la tesis con la frase «fue una época terrible». ¿Qué le falta? A) Una evidencia fechada y verificable B) Más adjetivos fuertes", "A) Una evidencia fechada y verificable", "Una opinión no es evidencia."),
        ("{F} ¿Por qué conviene que la interpretación use evidencias de varios tipos?", "Porque así no depende de una sola fuente y se pueden contrastar hechos, documentos y testimonios", "Contrastar tipos de fuentes fortalece la conclusión."),
        ("{F} Un compañero concluye: «El testimonio de 1984 prueba cuántas personas fueron detenidas en total». ¿Qué falla? A) Un testimonio muestra una vivencia, no una cifra total B) Que es de 1984", "A) Un testimonio muestra una vivencia, no una cifra total", "Hay un límite: de una vivencia no se deduce el total."),
        ("{F} ¿Qué evidencia de la ficha sirve para el tema de la influencia de Estados Unidos? A) La evidencia 1 B) La evidencia 5", "A) La evidencia 1", "Menciona la Alianza para el Progreso, impulsada por Estados Unidos."),
        ("{F} Para dar más fuerza a la tesis, ¿qué agregarías? A) Un informe de la época sobre las detenciones en uno de los países B) Una opinión sobre qué dictadura fue peor", "A) Un informe de la época sobre las detenciones en uno de los países", "Es una fuente verificable que trata el tema."),
        ("{F} ¿Cuál de estos es un límite honesto de la interpretación? A) La ficha no entrega cifras de víctimas ni cubre todos los países B) La ficha incluye un testimonio y un decreto", "A) La ficha no entrega cifras de víctimas ni cubre todos los países", "Reconocer lo que la evidencia no permite afirmar es un límite."),
    ],
    ctx=("Un compañero prepara una presentación con la tesis «Las dictaduras latinoamericanas fueron todas iguales». ¿Qué le recomiendas? A) Comparar casos con evidencias y precisar en qué se parecían y en qué no B) Repetir la tesis más fuerte", "A) Comparar casos con evidencias y precisar en qué se parecían y en qué no", "La evidencia 5 muestra una duración distinta a la de otros casos."),
    sc=[("En Historia: ¿qué es una tesis?", "La idea central que se defiende en una interpretación", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una evidencia?", "Un dato o fuente que apoya una afirmación", "Así se define en la clase."),
        ("En Historia: ¿qué es una conclusión proporcional?", "Una que no afirma más de lo que la evidencia permite", "Así se define en la clase.")],
    op=("Escribe una interpretación de seis a ocho líneas sobre «reforma, revolución y dictaduras en América Latina». Incluye tu tesis, tres evidencias de la ficha con su fecha y un límite de tu interpretación. Cuida que no afirmes más de lo que muestran las evidencias. {F}",
        "Tesis: «En varios países, la tensión entre reforma y revolución y la Guerra Fría terminaron en dictaduras». Evidencias: Revolución cubana (1959); golpes en Brasil (1964), Chile y Uruguay (1973) y Argentina (1976); testimonio de 1984 sobre una detención. Límite: la ficha no da cifras de víctimas ni cubre todos los países.",
        ["tiene una tesis clara", "usa tres evidencias fechadas", "reconoce un límite"], ["texto de seis a ocho líneas"], ["tesis con «todos» o «siempre»", "evidencias sin fecha"],
        "Pide que explique por qué un testimonio sirve para entender, pero no para cuantificar."),
    reinforce="Explica a alguien de tu casa qué es una tesis y qué es una evidencia con un ejemplo cotidiano.",
    extend="Escribe una tesis sobre un tema de tu colegio y anota dos evidencias que la apoyarían.",
)

OA = "HI2M OA 11"

# ================================================================ OA 11, clase 1
F = ("Ficha 1 (hechos del final del siglo XX; las definiciones valen para esta clase). "
     "Hitos: Mijaíl Gorbachov llega a dirigir la URSS en 1985 e impulsa dos políticas, la glasnost (apertura y mayor libertad de información) y la perestroika (reestructuración de la economía); "
     "cae el Muro de Berlín en 1989; Alemania se reunifica en 1990; la URSS se disuelve en 1991. "
     "Neoliberalismo: ideas que defienden el libre mercado, la privatización de empresas del Estado y un Estado con menos gasto; en los años ochenta las impulsaron los gobiernos de Margaret Thatcher (Reino Unido) y de Ronald Reagan (Estados Unidos). "
     "Globalización: aumento de las conexiones económicas, tecnológicas y culturales entre países. "
     "Sociedad de la información: sociedad donde crear y compartir información es central para la economía y la vida diaria. "
     "Geopolítica: estudio de cómo el poder se reparte entre países.")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo y entre sus actores el fin de la Guerra Fría, el auge del neoliberalismo y la aceleración de la globalización.",
    prior=["Sé qué fue la Guerra Fría y quiénes eran las superpotencias.", "Sé qué es el libre mercado.", "Sé calcular diferencias entre años."],
    explain=[
        "La Guerra Fría terminó entre 1989 y 1991. Dentro de la URSS, el gobierno de Gorbachov impulsó la glasnost, que dio más libertad de información, y la perestroika, que buscaba reestructurar la economía. En 1989 cayó el Muro de Berlín, en 1990 Alemania se reunificó y en 1991 la URSS se disolvió. Estados Unidos quedó como la superpotencia dominante, lo que cambió la geopolítica, es decir, el reparto del poder entre países.",
        "Al mismo tiempo, en los años ochenta ganó fuerza el neoliberalismo, un conjunto de ideas que defiende el libre mercado, la privatización de empresas del Estado y un Estado con menos gasto. Gobiernos como los de Margaret Thatcher en el Reino Unido y de Ronald Reagan en Estados Unidos las aplicaron. Estas ideas se difundieron por muchos países.",
        "La globalización se aceleró: más comercio entre países, empresas que producen en varios lugares y nuevas tecnologías de comunicación que permiten compartir información casi al instante. Por eso se habla de sociedad de la información. Para estudiar estos procesos hay que ubicar cada hecho en su fecha y distinguir los políticos (fin de la URSS) de los económicos (neoliberalismo) y los tecnológicos.",
    ],
    vocab=[("glasnost", "política soviética de apertura y mayor libertad de información"), ("perestroika", "política soviética de reestructuración de la economía"), ("neoliberalismo", "ideas que defienden el libre mercado, las privatizaciones y un Estado con menos gasto"), ("globalización", "aumento de las conexiones económicas, tecnológicas y culturales entre países"), ("geopolítica", "estudio de cómo el poder se reparte entre países"), ("sociedad de la información", "sociedad donde crear y compartir información es central para la economía y la vida diaria")],
    worked=[
        ("Clasificar un hecho", "Una empresa estatal de teléfonos se vende a una empresa privada para reducir el gasto del Estado. ¿Con qué idea se relaciona?", ["Se trata de pasar una empresa del Estado a manos privadas.", "Eso es privatización, idea del neoliberalismo."], "Neoliberalismo"),
        ("Calcular una duración", "¿Cuántos años pasaron entre la llegada de Gorbachov (1985) y la disolución de la URSS (1991)?", ["Tomo los dos años de la ficha.", "1991 − 1985 = 6."], "6 años"),
    ],
    mistakes=[("Pensar que la Guerra Fría terminó en un solo día.", "Se olvida que fue un proceso entre 1985 y 1991, con varios hechos.", "Ubica la llegada de Gorbachov, el Muro, la reunificación y la disolución en una línea de tiempo."),
              ("Confundir neoliberalismo con globalización.", "Una es un conjunto de ideas económicas y la otra un proceso de conexión entre países.", "Define cada término por separado y di cómo se relacionan.")],
    T=[
        ("{F} ¿En qué año se disolvió la URSS?", "1991", "La ficha lo indica."),
        ("{F} ¿Qué es la glasnost?", "Una política soviética de apertura y mayor libertad de información", "La ficha la define así."),
        ("{F} ¿Qué dos gobernantes aplicaron ideas neoliberales en los años ochenta?", "Margaret Thatcher y Ronald Reagan", "La ficha los nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la caída del Muro de Berlín y la disolución de la URSS?", "1991-1989", "Se resta el año de la caída al de la disolución.", " años"),
        ("{F} ¿Qué es la sociedad de la información, según la ficha?", "Una sociedad donde crear y compartir información es central para la economía y la vida diaria", "La ficha la define así."),
        ("{F} El Estado vende una empresa pública de agua a una empresa privada. ¿Qué idea se aplica? A) Privatización neoliberal B) Globalización", "A) Privatización neoliberal", "Pasar empresas del Estado a manos privadas es una idea neoliberal."),
        ("{F} Un diario soviético publica por primera vez críticas al gobierno. ¿A qué política se parece más? A) Glasnost B) Perestroika", "A) Glasnost", "Es una apertura de la información."),
        ("{F} Un gobierno cambia la forma en que se organiza y se paga la producción de las fábricas estatales. ¿A qué política se parece más? A) Perestroika B) Glasnost", "A) Perestroika", "La reestructuración de la economía es la perestroika."),
        ("{F} ¿Por qué la disolución de la URSS cambió la geopolítica mundial?", "Porque terminó la rivalidad de dos superpotencias y Estados Unidos quedó como la superpotencia dominante", "La ficha y la explicación describen ese cambio en el reparto del poder."),
        ("{F} Un compañero dice: «La globalización y el neoliberalismo son lo mismo». ¿Qué respondes? A) No, una es un conjunto de ideas económicas y la otra un aumento de conexiones entre países B) Sí, porque ocurrieron en las mismas décadas", "A) No, una es un conjunto de ideas económicas y la otra un aumento de conexiones entre países", "Coinciden en el tiempo, pero son procesos distintos."),
        ("{F} Ordena de más antiguo a más reciente: a) reunificación de Alemania b) llegada de Gorbachov c) disolución de la URSS d) caída del Muro.", "b, d, a, c", "Las fechas son 1985, 1989, 1990 y 1991."),
        ("{F} Un compañero afirma: «En 1989 terminó la Guerra Fría y ese mismo año se disolvió la URSS». ¿Qué corrección haces? A) La URSS se disolvió en 1991; la caída del Muro fue en 1989 B) Está bien porque fue en el mismo proceso", "A) La URSS se disolvió en 1991; la caída del Muro fue en 1989", "Son hitos del mismo proceso, pero con años distintos."),
        ("¿Cuál es la mejor pregunta guía para este tema? A) ¿Cómo cambiaron el poder mundial, la economía y las comunicaciones entre 1985 y el año 2000? B) ¿Qué país es el mejor del mundo?", "A) ¿Cómo cambiaron el poder mundial, la economía y las comunicaciones entre 1985 y el año 2000?", "La pregunta A tiene tiempo y temas definidos; la B es una opinión."),
    ],
    ctx=("Un afiche escolar dice: «En 1991 se inició el neoliberalismo». ¿Qué error tiene según la ficha? A) Esas ideas ganaron fuerza desde los años ochenta, antes de la disolución de la URSS B) Debería decir 1990", "A) Esas ideas ganaron fuerza desde los años ochenta, antes de la disolución de la URSS", "La ficha las ubica en los años ochenta con Thatcher y Reagan."),
    sc=[("En Historia: ¿qué es la globalización?", "El aumento de las conexiones económicas, tecnológicas y culturales entre países", "Así se define en la clase."),
        ("En Historia: ¿qué es la perestroika?", "Una política soviética de reestructuración de la economía", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es el neoliberalismo?", "Un conjunto de ideas que defiende el libre mercado, las privatizaciones y un Estado con menos gasto", "Así se define en el vocabulario.")],
    op=("Dibuja una línea de tiempo de 1980 a 2000 con escala 1 cm = 4 años. Marca con una raya: llegada de Gorbachov (1985), caída del Muro de Berlín (1989), reunificación de Alemania (1990) y disolución de la URSS (1991). Debajo escribe dos frases: una que defina neoliberalismo y otra que defina globalización. {F}",
        "Posiciones desde 1980: 1,25 cm; 2,25 cm; 2,5 cm; 2,75 cm. Frases: «El neoliberalismo defiende el libre mercado, las privatizaciones y un Estado con menos gasto»; «La globalización es el aumento de las conexiones económicas, tecnológicas y culturales entre países».",
        ["respeta la escala", "ubica bien los cuatro hitos", "las dos definiciones son distintas y correctas"], ["línea de tiempo dibujada", "dos frases escritas"], ["marcar los hitos sin medir", "definir las dos ideas con las mismas palabras"],
        "Pide que explique por qué el fin de la Guerra Fría fue un proceso y no un solo día."),
    reinforce="Explica en voz alta qué pasó entre 1985 y 1991 en la URSS y por qué cambió el mundo.",
    extend="Anota un producto de tu casa que se haya fabricado en otro país y di qué relación tiene con la globalización.",
)

# ================================================================ OA 11, clase 2
F = ("Ficha 2 (fuentes y datos de ejemplo escritos para este cuaderno; no son documentos históricos reales). "
     "Fuente A, discurso de un dirigente reformista de un país del bloque soviético, 1987, dirigido a su partido: «La economía necesita nuevas formas de gestión y la sociedad debe poder discutir sus problemas con franqueza.» "
     "Fuente B, crónica de una estudiante en una gran ciudad europea, 1989, publicada en un diario local: «Anoche cientos de personas se reunieron frente a la frontera; unas lloraban y otras cantaban, y nadie sabía qué ocurriría al amanecer.» "
     "Fuente C, informe de una empresa multinacional a sus accionistas, 1995: «La apertura de mercados permite producir en tres continentes y reducir costos; recomendamos ampliar nuestras plantas en el extranjero.» "
     "Tabla de ejemplo, comercio de un país: en 1985 exportó 40 unidades y en 1995 exportó 90 unidades.")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre el fin de la Guerra Fría y la globalización: quién habla, desde dónde, con qué propósito y qué calla.",
    prior=["Sé qué es la procedencia de una fuente.", "Sé situar el fin de la Guerra Fría.", "Sé leer una tabla sencilla."],
    explain=[
        "Las fuentes de un proceso reciente son muy variadas: discursos, crónicas de diarios, informes de empresas y estadísticas. Cada una tiene un autor, una fecha, un lugar y un propósito. El discurso de un dirigente busca convencer a su partido; la crónica de una testigo busca contar lo que ocurrió y transmitir lo que se sentía; el informe de una empresa busca informar a sus accionistas y justificar decisiones.",
        "Por eso ninguna fuente basta por sí sola. El discurso muestra qué pensaban algunos dirigentes, pero no lo que pensaba la población. La crónica muestra el ambiente de un día, pero no explica las causas. El informe de la empresa muestra una mirada favorable a la apertura de mercados, pero no cuenta los efectos para los trabajadores.",
        "Una tabla de datos también tiene procedencia: hay que saber quién la hizo, qué mide y en qué años. Un aumento en los números no explica por sí solo la causa. Se contrasta con otras fuentes para armar una conclusión proporcional. Por ejemplo, si las exportaciones suben, se puede decir que el comercio creció, pero no que todos ganaron.",
    ],
    vocab=[("crónica", "relato de un hecho escrito por quien lo presenció o lo investigó"), ("accionista", "persona que posee una parte de una empresa"), ("multinacional", "empresa que produce o vende en varios países"), ("apertura de mercados", "reducción de las trabas para comerciar entre países"), ("propósito", "lo que el autor quiere lograr con su fuente")],
    worked=[
        ("Identificar el propósito", "Un folleto de una empresa dice: «Sus ahorros crecen con nosotros». ¿Cuál es su propósito más probable?", ["Una empresa publica para atraer clientes.", "Promete algo para convencer de contratar."], "Convencer de contratar los servicios de la empresa"),
        ("Leer un cambio en una tabla", "Un país de ejemplo exportó 30 unidades en 1980 y 75 en 1990. ¿Cuánto aumentó?", ["Tomo las dos cifras.", "75 − 30 = 45."], "45 unidades"),
    ],
    mistakes=[("Creer que una crónica explica las causas de un hecho.", "Una crónica cuenta lo que se vio, no necesariamente por qué ocurrió.", "Pregunta qué cuenta y qué deja sin explicar."),
              ("Concluir que un aumento de exportaciones significa que todos los habitantes mejoraron.", "Los datos de comercio no muestran cómo se repartieron los beneficios.", "Pide otra fuente sobre empleo o ingresos.")],
    T=[
        ("{F} ¿A quién se dirige la fuente A?", "A su partido", "La ficha dice que el discurso va dirigido al partido del dirigente."),
        ("{F} ¿En qué año se escribió la crónica de la fuente B?", "1989", "La ficha la fecha en 1989."),
        ("{F} ¿A quiénes informa la fuente C?", "A los accionistas de la empresa", "La ficha lo indica."),
        ("=", "{F} ¿Cuánto aumentaron las exportaciones del país de la tabla entre 1985 y 1995?", "90-40", "Se resta la cifra inicial a la final.", " unidades"),
        ("{F} ¿Cuál es el propósito más probable de la fuente C? A) Informar a los accionistas y justificar la ampliación de plantas B) Contar un hecho sin tomar posición", "A) Informar a los accionistas y justificar la ampliación de plantas", "Es un informe de una empresa a sus accionistas con una recomendación."),
        ("{F} ¿Qué se puede afirmar con la fuente B? A) Que el día de la crónica hubo mucha gente reunida y emociones mezcladas B) Que todos los habitantes de la ciudad apoyaban el cambio", "A) Que el día de la crónica hubo mucha gente reunida y emociones mezcladas", "La crónica solo cuenta lo que vio la autora."),
        ("{F} ¿Qué guarda silencio la fuente C? A) Los efectos de la apertura de mercados para los trabajadores B) Que la empresa quiere reducir costos", "A) Los efectos de la apertura de mercados para los trabajadores", "El informe habla de costos y plantas y no de los empleos."),
        ("{F} ¿Qué conclusión permite la tabla? A) Las exportaciones del país aumentaron entre 1985 y 1995 B) Todos los habitantes mejoraron su ingreso", "A) Las exportaciones del país aumentaron entre 1985 y 1995", "La tabla solo mide exportaciones."),
        ("{F} ¿Por qué A y B, juntas, dan una imagen más completa del cambio que cada una por separado?", "Porque A muestra la mirada de un dirigente y B la vivencia de una testigo, dos perspectivas distintas", "Contrastar perspectivas completa los vacíos de cada fuente."),
        ("{F} Un compañero concluye: «La fuente A demuestra que todos en el bloque soviético querían reformas». ¿Qué corrección haces? A) Solo muestra lo que decía un dirigente; hacen falta más fuentes B) Está bien porque es un discurso", "A) Solo muestra lo que decía un dirigente; hacen falta más fuentes", "Una conclusión debe ser proporcional a la evidencia."),
        ("{F} Un compañero dice: «La fuente C es objetiva porque es un informe con cifras». ¿Qué le respondes?", "Que tiene un autor con intereses y propósito: recomienda ampliar plantas a favor de la empresa", "Un informe también tiene perspectiva y propósito."),
        ("{F} ¿Qué segunda fuente ayudaría más a evaluar los efectos de la apertura de mercados sobre el empleo? A) Estadísticas de empleo y testimonios de trabajadores de la época B) Otro informe de otra empresa multinacional", "A) Estadísticas de empleo y testimonios de trabajadores de la época", "Debe tratar el empleo, que es lo que la fuente C calla."),
        ("{F} ¿Cuál de estas preguntas interroga mejor la procedencia de la fuente B? A) ¿Quién la escribió, dónde y para qué fue publicada? B) ¿Qué dice la crónica sobre la frontera?", "A) ¿Quién la escribió, dónde y para qué fue publicada?", "La procedencia es autor, lugar, fecha y propósito."),
    ],
    ctx=("Un canal de televisión muestra solo el informe de la empresa y concluye que «la globalización benefició a todos». ¿Qué falta? A) Fuentes de trabajadores, consumidores y de otros países B) Un segundo informe de otra empresa multinacional", "A) Fuentes de trabajadores, consumidores y de otros países", "Una sola perspectiva no representa a todos los actores."),
    sc=[("En Historia: ¿qué es un accionista?", "Una persona que posee una parte de una empresa", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una multinacional?", "Una empresa que produce o vende en varios países", "Así se define en la clase."),
        ("En Historia: ¿qué es una crónica?", "El relato de un hecho escrito por quien lo presenció o lo investigó", "Así se define en el vocabulario.")],
    op=("Haz una tabla con tres columnas (autor y fecha, propósito, qué calla) para las fuentes A, B y C. Después escribe dos frases de conclusión que usen al menos dos fuentes y el dato de la tabla de exportaciones, sin afirmar más de lo que permiten. {F}",
        "A: dirigente reformista, 1987; convencer a su partido; calla la opinión de la población. B: estudiante, 1989; contar lo vivido; calla causas. C: multinacional, 1995; justificar ampliación; calla efectos en los trabajadores. Conclusión: «Entre 1985 y 1995 las exportaciones del país de ejemplo aumentaron en 50 unidades; las fuentes muestran visiones distintas del cambio».",
        ["completa autor, propósito y silencio de cada fuente", "usa al menos dos fuentes y la tabla", "no generaliza más de lo permitido"], ["tabla completa", "dos frases"], ["confundir contenido con propósito", "decir que todos ganaron con la apertura"],
        "Pide que explique qué fuente agregaría para dar voz a los trabajadores."),
    reinforce="Explica a alguien de tu casa por qué una crónica y un informe de empresa cuentan lo mismo de manera distinta.",
    extend="Elige un anuncio que hayas visto y di quién lo hizo, para qué y qué calla.",
)

# ================================================================ OA 11, clase 3
F = ("Ficha 3 (perspectivas de ejemplo y datos de ejemplo sobre neoliberalismo y globalización). "
     "Perspectiva de un defensor del libre mercado: «Abrir el comercio y privatizar baja los precios y trae inversión y tecnología.» "
     "Perspectiva de una dirigente sindical: «Cuando una empresa se traslada a otro país, los trabajadores pierden el empleo y los sueldos se achican.» "
     "Perspectiva de un consumidor: «Hoy encuentro más productos y más baratos que hace diez años.» "
     "Perspectiva de un país pobre exportador de materias primas: «Vendemos barato y compramos caro; necesitamos industria propia.» "
     "Escalas: local (un barrio o una fábrica), nacional (un país), global (la economía mundial). "
     "Dato de ejemplo: una fábrica de 300 trabajadores traslada su producción a otro país y despide a 90.")
build(
    OA, 3, F,
    use="Aprenderé a comparar perspectivas sobre el neoliberalismo y la globalización, y a mirar sus efectos en escala local, nacional y global.",
    prior=["Sé qué es el neoliberalismo y la globalización.", "Sé interrogar fuentes.", "Sé calcular porcentajes sencillos."],
    explain=[
        "El neoliberalismo y la globalización tienen defensores y críticos. Los defensores dicen que el libre mercado y la apertura bajan los precios, atraen inversión y traen tecnología. Los críticos dicen que algunos trabajadores pierden el empleo cuando una empresa se traslada, que los sueldos pueden bajar y que los países que solo exportan materias primas quedan en desventaja. Ambos argumentos pueden tener parte de verdad.",
        "Para comparar hay que mirar la escala. En escala local, una fábrica que cierra afecta a un barrio. En escala nacional, un país puede crecer en exportaciones pero tener desigualdad. En escala global, la economía mundial puede crecer mientras algunos países se quedan atrás. Un mismo hecho puede ser positivo en una escala y negativo en otra.",
        "Comparar perspectivas no significa aceptar todas por igual: significa entender sus argumentos, sus intereses y las evidencias que usan. Por ejemplo, el consumidor ve más productos baratos, y la dirigente sindical ve empleos perdidos. Los datos de empleo, precios e ingresos ayudan a evaluar cuál afirmación se sostiene mejor.",
    ],
    vocab=[("inversión", "dinero que se pone en una empresa o proyecto para obtener ganancias"), ("sindicato", "organización de trabajadores que defiende sus derechos laborales"), ("materias primas", "productos básicos sin elaborar, como el cobre o el trigo"), ("desventaja", "situación en la que se tiene menos posibilidades que otros"), ("escala global", "nivel de análisis que mira el mundo entero")],
    worked=[
        ("Reconocer una escala", "«El cierre de la fábrica dejó sin ingreso a muchas familias del barrio». ¿Qué escala usa?", ["Habla de una fábrica y un barrio.", "No habla del país ni del mundo."], "Escala local"),
        ("Calcular un porcentaje", "Una fábrica de ejemplo tiene 200 trabajadores y despide a 50. ¿Qué porcentaje despide?", ["Divido: 50 ÷ 200 = 0,25.", "Paso a porcentaje: 25 %."], "25 %"),
    ],
    mistakes=[("Creer que la globalización tiene el mismo efecto para todos.", "Se ignoran las diferencias entre trabajadores, consumidores y países.", "Pregunta quién gana y quién pierde en cada escala."),
              ("Comparar perspectivas como si solo una tuviera datos.", "Se descarta la que no coincide con la propia sin revisar su evidencia.", "Anota qué evidencia usa cada perspectiva.")],
    T=[
        ("{F} ¿Qué perspectiva dice «encuentro más productos y más baratos»?", "La del consumidor", "La ficha le asigna esa frase."),
        ("{F} ¿Qué escala usa el análisis de lo que pasa en una fábrica o un barrio?", "La escala local", "La ficha define lo local como un barrio o una fábrica."),
        ("{F} ¿Qué necesita el país pobre exportador, según su perspectiva?", "Industria propia", "La ficha lo dice en su frase."),
        ("{F} ¿Qué perspectiva dice que los trabajadores pierden el empleo y los sueldos se achican?", "La de la dirigente sindical", "La ficha le asigna esa frase."),
        ("=", "{F} ¿Qué porcentaje de los trabajadores de la fábrica de ejemplo fue despedido?", "90/300*100", "Se divide lo despedido por el total y se multiplica por cien.", " %"),
        ("{F} ¿Quién afirma que abrir el comercio trae inversión y tecnología? A) El defensor del libre mercado B) La dirigente sindical", "A) El defensor del libre mercado", "La ficha le asigna esa frase."),
        ("{F} «El país creció en exportaciones, pero la desigualdad aumentó». ¿Qué escala usa? A) Nacional B) Local", "A) Nacional", "Habla de un país entero."),
        ("{F} Un consumidor compra un producto más barato, pero su vecina pierde el empleo en la fábrica que se trasladó. ¿Qué muestra esto? A) Que un mismo proceso puede tener efectos distintos según quién lo viva B) Que el consumidor y su vecina tienen la misma experiencia", "A) Que un mismo proceso puede tener efectos distintos según quién lo viva", "Ambos viven efectos distintos de un mismo cambio."),
        ("{F} ¿Por qué la dirigente sindical y el defensor del libre mercado no coinciden?", "Porque miran efectos distintos: ella el empleo y los sueldos, él los precios y la inversión", "Cada uno se fija en intereses y efectos distintos."),
        ("{F} Un compañero dice: «Como la globalización baja los precios, nadie sale perdiendo». ¿Qué corrección haces? A) Hay trabajadores que pierden empleo aunque los precios bajen B) Está bien, porque los precios son el único dato que importa", "A) Hay trabajadores que pierden empleo aunque los precios bajen", "La ficha muestra que los efectos no son iguales para todos."),
        ("{F} ¿Qué escala falta si solo se analiza la fábrica que cierra y no se miran los precios mundiales? A) La global B) La local", "A) La global", "Los traslados de empresas responden a la economía mundial."),
        ("{F} ¿Qué dato permitiría evaluar mejor la afirmación de la dirigente sindical?", "Estadísticas de empleo y de sueldos antes y después del traslado de la empresa", "Esos datos prueban si el empleo y los sueldos bajaron."),
        ("{F} ¿Cuál es una conclusión proporcional? A) La globalización trajo ventajas y desventajas distintas según el actor y la escala B) La globalización fue buena para todos", "A) La globalización trajo ventajas y desventajas distintas según el actor y la escala", "Es lo que muestran las perspectivas de la ficha."),
    ],
    ctx=("Un periódico titula: «Todos ganamos con la apertura de mercados». Según la ficha, ¿qué le falta? A) Las voces de los trabajadores que perdieron empleo y de los países exportadores de materias primas B) Más cifras sobre los precios de los productos", "A) Las voces de los trabajadores que perdieron empleo y de los países exportadores de materias primas", "La ficha muestra efectos desiguales."),
    sc=[("En Historia: ¿qué es la escala global?", "El nivel de análisis que mira el mundo entero", "Así se define en la clase."),
        ("En Historia: ¿qué es una materia prima?", "Un producto básico sin elaborar, como el cobre o el trigo", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un sindicato?", "Una organización de trabajadores que defiende sus derechos laborales", "Así se define en el vocabulario.")],
    op=("Arma una matriz con las cuatro perspectivas de la ficha: para cada una escribe el argumento, el interés y la escala (local, nacional o global). Después redacta tres frases: en qué coinciden dos actores, en qué se oponen dos y qué dato usarías para evaluar. {F}",
        "Defensor: precios, inversión; global. Sindical: empleo y sueldos; local. Consumidor: productos baratos; local. País exportador: industria propia; nacional y global. Dato: 90 de 300 trabajadores despedidos (30 %).",
        ["completa las cuatro perspectivas", "separa argumento, interés y escala", "usa un dato para evaluar"], ["matriz completa", "tres frases"], ["repetir el mismo argumento para dos actores", "no distinguir escalas"],
        "Pide que explique por qué ganar como consumidor no impide perder como trabajador."),
    reinforce="Explica con tus palabras por qué la globalización puede ser buena en una escala y mala en otra.",
    extend="Averigua en tu casa qué producto de uso diario se fabrica en otro país y anota una ventaja y una desventaja.",
)

# ================================================================ OA 11, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; datos de ejemplo cuando se indica). "
     "Causas de la crisis de la URSS: una economía con poco crecimiento y escasez de productos; un gran gasto en armas por la competencia con Estados Unidos; la glasnost permitió críticas y la perestroika no resolvió los problemas económicos; movimientos nacionales y protestas en las repúblicas y países del bloque pidieron mayor autonomía. "
     "Detonante: las protestas masivas de 1989 en Europa del Este y la apertura de las fronteras. "
     "Cambios: fin del bloque soviético, Estados Unidos como superpotencia dominante, difusión del libre mercado, nuevas tecnologías de comunicación, más comercio internacional. "
     "Continuidades: las armas nucleares seguían existiendo; muchas desigualdades entre países ricos y pobres persistían. "
     "Dato de ejemplo: un país gasta 30 de cada 100 unidades de su presupuesto en armas.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas del fin de la Guerra Fría con sus cambios y continuidades, y a distinguir causas de largo plazo y detonante.",
    prior=["Sé distinguir una causa de largo plazo y un detonante.", "Sé qué fue la glasnost y la perestroika.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La crisis de la URSS no tuvo una sola causa. Su economía crecía poco y faltaban productos. Además, gastaba mucho en armas por la competencia con Estados Unidos. Las reformas de Gorbachov abrieron un espacio de críticas con la glasnost, pero la perestroika no resolvió los problemas económicos. En las repúblicas y países del bloque crecieron las demandas de autonomía.",
        "El detonante fue la ola de protestas de 1989 en Europa del Este y la apertura de las fronteras, que aceleró el derrumbe de los gobiernos comunistas. Una causa de largo plazo se va acumulando por años, y un detonante es el hecho que dispara el proceso. No hay que confundirlos ni creer que un solo hecho explicó todo.",
        "Hubo cambios importantes: terminó el bloque soviético, Estados Unidos quedó como superpotencia dominante, el libre mercado se extendió y las comunicaciones avanzaron. También hubo continuidades: las armas nucleares seguían existiendo y la desigualdad entre países ricos y pobres persistía. Un cambio grande no borra todo lo anterior.",
    ],
    vocab=[("superpotencia", "país con un poder militar, económico y político muy superior al de la mayoría"), ("autonomía", "capacidad de un grupo o territorio de decidir sus propios asuntos"), ("detonante", "hecho que desencadena una crisis que ya tenía causas previas"), ("bloque soviético", "conjunto de países de Europa del Este aliados de la URSS"), ("presupuesto", "dinero que un Estado planea gastar en un período")],
    worked=[
        ("Distinguir causa y detonante", "Las protestas de 1989 en Europa del Este, ¿son causa de largo plazo o detonante?", ["Aceleraron un proceso que ya estaba en marcha.", "Dispararon el derrumbe de los gobiernos comunistas."], "Detonante"),
        ("Calcular un porcentaje", "Un país de ejemplo gasta 20 de cada 100 unidades del presupuesto en armas. ¿Qué porcentaje es?", ["20 de cada 100 equivale a 20 ÷ 100.", "= 0,20 = 20 %."], "20 %"),
    ],
    mistakes=[("Decir que la glasnost causó por sí sola la caída de la URSS.", "Se ignoran las causas económicas y las demandas de autonomía.", "Usa «contribuyó a» y separa causas de largo plazo y detonante."),
              ("Creer que al terminar la Guerra Fría terminaron las armas nucleares.", "Se olvidan las continuidades.", "Pregunta qué siguió existiendo después del cambio.")],
    T=[
        ("{F} ¿Qué política permitió críticas dentro de la URSS?", "La glasnost", "La ficha la presenta como apertura de información."),
        ("{F} ¿Qué año tuvieron lugar las protestas que la ficha presenta como detonante?", "1989", "La ficha dice «protestas masivas de 1989»."),
        ("{F} ¿Qué quedó como superpotencia dominante?", "Estados Unidos", "La ficha lo indica entre los cambios."),
        ("{F} ¿Qué gasto de la URSS menciona la ficha como efecto de la competencia con Estados Unidos?", "Un gran gasto en armas", "La ficha lo incluye entre las causas de la crisis."),
        ("=", "{F} Si el presupuesto del país de ejemplo es de 400 unidades, ¿cuántas se gastan en armas?", "400*30/100", "Se calcula el 30 % de 400.", " unidades"),
        ("{F} ¿Cuál es una causa de largo plazo? A) La economía con poco crecimiento y escasez de productos B) Las protestas de 1989", "A) La economía con poco crecimiento y escasez de productos", "Se fue acumulando por años; las protestas fueron el detonante."),
        ("{F} ¿Cuál es una continuidad? A) La existencia de armas nucleares B) El fin del bloque soviético", "A) La existencia de armas nucleares", "Seguían existiendo; el fin del bloque soviético es un cambio."),
        ("{F} ¿Cuál es un cambio? A) La difusión del libre mercado B) La desigualdad entre países ricos y pobres", "A) La difusión del libre mercado", "La desigualdad persistió; el avance del libre mercado es un cambio."),
        ("{F} Un país de ejemplo gasta mucho en armas y su economía crece poco. ¿Por qué esto contribuye a una crisis?", "Porque destina muchos recursos a las armas y quedan pocos para producir y mejorar la vida de la gente", "Gastar mucho en armas limita otros gastos."),
        ("{F} Un compañero afirma: «Gorbachov provocó solo la caída de la URSS». ¿Qué corrección haces? A) Sus reformas contribuyeron, pero hubo causas económicas y demandas de autonomía B) Es correcto porque era el dirigente", "A) Sus reformas contribuyeron, pero hubo causas económicas y demandas de autonomía", "Ser dirigente no vuelve única una causa."),
        ("{F} ¿Por qué se dice que la caída del Muro de Berlín fue un detonante y no la causa única?", "Porque aceleró un proceso que tenía causas previas, como la crisis económica y las demandas de autonomía", "El detonante dispara un proceso con causas anteriores."),
        ("{F} ¿Qué evidencia apoyaría mejor que la economía soviética tenía escasez de productos? A) Testimonios y datos de la época sobre filas y abastecimiento B) Un discurso de un dirigente sobre las reformas", "A) Testimonios y datos de la época sobre filas y abastecimiento", "Deben tratar directamente la escasez."),
        ("{F} ¿Cuál es la mejor síntesis? A) Hubo causas de largo plazo y un detonante, con cambios en el poder mundial y continuidades como las armas nucleares B) Todo cambió en 1991 sin ninguna continuidad", "A) Hubo causas de largo plazo y un detonante, con cambios en el poder mundial y continuidades como las armas nucleares", "Reúne causas, cambios y continuidades."),
    ],
    ctx=("Un afiche dice: «La Guerra Fría terminó por culpa de la glasnost». ¿Qué problema tiene? A) Ignora causas económicas y otras causas de largo plazo B) No menciona la caída del Muro", "A) Ignora causas económicas y otras causas de largo plazo", "La ficha muestra varias causas combinadas."),
    sc=[("En Historia: ¿qué es una superpotencia?", "Un país con un poder militar, económico y político muy superior al de la mayoría", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es la autonomía?", "La capacidad de un grupo o territorio de decidir sus propios asuntos", "Así se define en la clase."),
        ("En Historia: ¿qué es un detonante?", "Un hecho que desencadena una crisis que ya tenía causas previas", "Así se define en el vocabulario.")],
    op=("Dibuja un esquema con «fin de la Guerra Fría» al centro. A la izquierda escribe tres causas de largo plazo, arriba el detonante y a la derecha un cambio y una continuidad. Debajo escribe una frase con «contribuyó a…» que evite decir que algo fue la única causa. {F}",
        "Causas de largo plazo: economía con poco crecimiento, gasto en armas, demandas de autonomía. Detonante: protestas de 1989 y apertura de fronteras. Cambio: Estados Unidos como superpotencia dominante. Continuidad: armas nucleares. Frase: la glasnost contribuyó a abrir el debate, junto con otras causas.",
        ["distingue causa de largo plazo y detonante", "incluye un cambio y una continuidad", "evita causas únicas"], ["esquema", "frase con «contribuyó a…»"], ["poner el detonante como causa de largo plazo", "usar «causó por sí sola»"],
        "Pide que explique por qué una coincidencia en el tiempo no basta para probar una causa."),
    reinforce="Explica a alguien de tu casa la diferencia entre una causa de largo plazo y un detonante usando el fin de la URSS.",
    extend="Piensa en un conflicto que empezó por un hecho pequeño y di qué causas anteriores lo hicieron posible.",
)

# ================================================================ OA 11, clase 5
F = ("Ficha 5 (evidencias de ejemplo para construir una interpretación; no son documentos históricos reales). "
     "Tesis de ejemplo: «El fin de la Guerra Fría y la expansión del neoliberalismo aceleraron la globalización, con beneficios y desigualdades distintas según los países y los grupos.» "
     "Evidencia 1: la URSS se disuelve en 1991 y Estados Unidos queda como superpotencia dominante. "
     "Evidencia 2, dato de ejemplo: el comercio entre dos países pasa de 100 unidades en 1985 a 350 en 2000. "
     "Evidencia 3, testimonio de ejemplo, 1998: «Antes tenía un empleo estable en la fábrica de zapatos; hoy trabajo por contrato y gano menos.» "
     "Evidencia 4, encuesta de ejemplo, 2000: de 100 personas consultadas, 70 dicen tener acceso a internet. "
     "Evidencia 5: en los años ochenta, los gobiernos de Thatcher y de Reagan aplicaron políticas de libre mercado y privatización.")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre el fin de la Guerra Fría, el neoliberalismo y la globalización, con tesis, evidencias y límites.",
    prior=["Sé qué es una tesis y qué es una evidencia.", "Sé comparar perspectivas.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una interpretación histórica explica un proceso con una tesis, que es la idea central, y con evidencias que la apoyan. Para este tema una tesis posible es que el fin de la Guerra Fría y el neoliberalismo aceleraron la globalización, con efectos desiguales. Cada afirmación debe apoyarse en una evidencia fechada y ubicada, y no en una simple opinión.",
        "Las evidencias deben ser de distinto tipo: un hecho político (la disolución de la URSS), un dato económico (el comercio que crece), un testimonio (la experiencia de un trabajador) y una encuesta (el acceso a internet). Cada una cuenta algo distinto: la política, la economía, la vida de una persona y una tendencia entre muchas personas.",
        "Una interpretación también tiene límites. Un testimonio no representa a todos los trabajadores; una encuesta de 100 personas no representa a un país entero. Reconocer los límites hace más fuerte el argumento. Una tesis con «todos» o «siempre» necesita mucha evidencia; con «en varios países» o «para algunos grupos» necesita menos y es más precisa.",
    ],
    vocab=[("tesis", "idea central que se defiende en una interpretación"), ("encuesta", "serie de preguntas hechas a un grupo para conocer opiniones o hechos"), ("muestra", "grupo pequeño de personas que se consulta para saber algo sobre un grupo mayor"), ("tendencia", "dirección en que cambia algo con el tiempo"), ("límite de una interpretación", "lo que la evidencia disponible no permite afirmar")],
    worked=[
        ("Elegir la evidencia que apoya", "Tesis: «La globalización aumentó el comercio entre países». ¿Qué evidencia de la ficha la apoya?", ["Busco un dato de comercio.", "El comercio entre dos países pasa de 100 a 350 unidades."], "La evidencia 2"),
        ("Calcular un aumento", "El comercio entre dos países de ejemplo pasa de 80 a 200 unidades. ¿Cuánto aumentó?", ["Tomo ambas cifras.", "200 − 80 = 120."], "120 unidades"),
    ],
    mistakes=[("Escribir una tesis que dice «todos los países ganaron» sin evidencias de todos.", "Se afirma más de lo que se puede probar.", "Cambia a «algunos países y grupos» o agrega evidencias de cada caso."),
              ("Usar una encuesta de 100 personas para hablar de todo un país.", "Una muestra pequeña no representa a todos.", "Indica que es un dato de ejemplo y que tiene límites.")],
    T=[
        ("{F} ¿Qué año se disuelve la URSS, según la evidencia 1?", "1991", "La ficha lo indica."),
        ("{F} ¿Qué tipo de fuente es la evidencia 3?", "Un testimonio", "Relata lo que vivió una persona."),
        ("{F} ¿Cuántas personas fueron consultadas en la encuesta de ejemplo?", "100", "La ficha lo indica."),
        ("=", "{F} ¿Cuánto aumentó el comercio de ejemplo entre 1985 y 2000?", "350-100", "Se resta la cifra inicial a la final.", " unidades"),
        ("=", "{F} ¿Qué porcentaje de las personas consultadas tiene acceso a internet?", "70/100*100", "70 de cada 100 equivale a 70 %.", " %"),
        ("{F} ¿Qué evidencia apoya que el neoliberalismo se aplicó en los años ochenta? A) La evidencia 5 B) La evidencia 4", "A) La evidencia 5", "Menciona las políticas de Thatcher y de Reagan."),
        ("{F} ¿Qué evidencia muestra un efecto negativo para una persona trabajadora? A) La evidencia 3 B) La evidencia 2", "A) La evidencia 3", "El testimonio habla de menor sueldo y de contrato sin estabilidad."),
        ("{F} ¿Cuál es una reformulación más proporcional de la tesis? A) La globalización tuvo beneficios y desigualdades según los grupos B) La globalización benefició a todos por igual", "A) La globalización tuvo beneficios y desigualdades según los grupos", "«Todos» y «por igual» afirman más de lo que la ficha permite."),
        ("{F} ¿Por qué conviene combinar un dato económico y un testimonio?", "Porque el dato muestra una tendencia general y el testimonio muestra cómo la vivió una persona", "Cada tipo de evidencia aporta algo distinto."),
        ("{F} Un compañero concluye: «El testimonio de 1998 prueba que a todos los trabajadores les bajó el sueldo». ¿Qué falla? A) Un testimonio muestra una vivencia, no el total de trabajadores B) Los testimonios nunca sirven como evidencia", "A) Un testimonio muestra una vivencia, no el total de trabajadores", "Hay un límite en lo que un caso puede probar."),
        ("{F} Un compañero concluye: «El 70 % de los habitantes del mundo tiene internet». ¿Qué falla? A) La encuesta de ejemplo solo consultó a 100 personas B) El 70 % es un número muy bajo", "A) La encuesta de ejemplo solo consultó a 100 personas", "Una muestra pequeña no representa a todo el mundo."),
        ("{F} ¿Qué evidencia agregarías para apoyar que la sociedad de la información se extendió? A) Un registro de la época sobre el crecimiento del uso de internet B) Una opinión sobre qué tecnología es mejor", "A) Un registro de la época sobre el crecimiento del uso de internet", "Es una fuente verificable que trata el tema."),
        ("{F} ¿Cuál es un límite honesto de la interpretación? A) La ficha no contiene datos de todos los países ni de todos los grupos B) La ficha incluye un testimonio", "A) La ficha no contiene datos de todos los países ni de todos los grupos", "Reconocer lo que la evidencia no permite afirmar es un límite."),
    ],
    ctx=("Un compañero prepara una presentación con la tesis «La globalización es mala». ¿Qué le recomiendas? A) Precisar qué efectos, para quién y con qué evidencias B) Repetir la tesis con más fuerza", "A) Precisar qué efectos, para quién y con qué evidencias", "La ficha muestra efectos distintos según el grupo."),
    sc=[("En Historia: ¿qué es una tesis?", "La idea central que se defiende en una interpretación", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es una muestra?", "Un grupo pequeño de personas que se consulta para saber algo sobre un grupo mayor", "Así se define en la clase."),
        ("En Historia: ¿qué es una tendencia?", "La dirección en que cambia algo con el tiempo", "Así se define en el vocabulario.")],
    op=("Escribe una interpretación de seis a ocho líneas sobre «el fin de la Guerra Fría y la globalización». Incluye tu tesis, tres evidencias de la ficha con su dato y un límite de tu interpretación. Cuida que no afirmes más de lo que muestran las evidencias. {F}",
        "Tesis: «El fin de la Guerra Fría y el neoliberalismo aceleraron la globalización, con efectos desiguales». Evidencias: disolución de la URSS en 1991; comercio de 100 a 350 unidades; testimonio de 1998. Límite: los datos son de ejemplo y no representan a todos los países ni grupos.",
        ["tiene una tesis clara", "usa tres evidencias de la ficha", "reconoce un límite"], ["texto de seis a ocho líneas"], ["tesis con «todos» o «siempre»", "evidencias sin dato"],
        "Pide que explique por qué una encuesta pequeña no sirve para hablar de un país entero."),
    reinforce="Explica a alguien de tu casa qué es una tesis y qué es una evidencia con un ejemplo cotidiano.",
    extend="Escribe una tesis sobre un tema del colegio y anota dos evidencias que la apoyarían.",
)

# ================================================================ OA 11, clase 6
F = ("Ficha 6 (debate de ejemplo sobre la globalización; los argumentos son de ejemplo). "
     "Tema: ¿la globalización ha traído más beneficios que perjuicios? "
     "Postura 1, a favor: «Hay más comercio, más información y más productos accesibles; muchos países han crecido.» "
     "Postura 2, matizada: «Hay beneficios, pero también desigualdad y pérdida de empleos en algunos sectores; el Estado debería proteger a los afectados.» "
     "Postura 3, crítica: «Los países pobres siguen dependiendo de exportar materias primas y las grandes empresas deciden demasiado.» "
     "Evidencias de ejemplo: el comercio entre dos países pasó de 100 a 350 unidades entre 1985 y 2000; una fábrica de 300 trabajadores despidió a 90 al trasladar su producción; "
     "el 70 % de 100 personas encuestadas tiene acceso a internet. "
     "Reglas del debate: respeto, evidencias, no atacar a las personas.")
build(
    OA, 6, F,
    use="Aprenderé a debatir las consecuencias y los límites del neoliberalismo y la globalización, usando evidencias y reconociendo qué no se puede afirmar.",
    prior=["Sé comparar perspectivas y escalas.", "Sé construir una interpretación con tesis y evidencias.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Un debate histórico no es una pelea: es un intercambio de argumentos con evidencias. Un argumento tiene una afirmación, una razón y una evidencia que la apoya. Por ejemplo: «La globalización aumentó el comercio, porque el comercio de dos países pasó de 100 a 350 unidades». La afirmación debe ser proporcional a los datos.",
        "En el debate es importante reconocer los límites. Un dato de comercio no muestra cómo se repartieron las ganancias. Un testimonio no representa a todos los trabajadores. Una encuesta pequeña no representa a todo un país. También hay que evitar las generalizaciones («todos», «nadie», «siempre») y los ataques personales, que no discuten el argumento.",
        "Un debate responsable puede terminar en una posición matizada: reconocer beneficios, reconocer desigualdades y proponer cómo el Estado y la sociedad pueden reducir los perjuicios. Cambiar de opinión por una buena evidencia no es perder, es razonar.",
    ],
    vocab=[("argumento", "afirmación apoyada en una razón y en una evidencia"), ("matizar", "reconocer que una afirmación es cierta en parte y tiene excepciones"), ("generalización", "afirmación que extiende a todos lo observado en algunos casos"), ("ataque personal", "crítica a la persona que habla y no a su argumento"), ("consecuencia", "efecto que sigue a un hecho o decisión")],
    worked=[
        ("Armar un argumento", "Afirmación: «La apertura de mercados tuvo efectos desiguales». ¿Qué evidencia de la ficha la apoya?", ["Busco un caso con ganadores y perdedores.", "La fábrica que traslada su producción y despide a 90 de 300 trabajadores."], "El caso de la fábrica con 90 despidos de 300"),
        ("Calcular un porcentaje", "En una encuesta de ejemplo de 150 personas, 30 dicen haber perdido su empleo por un traslado de empresa. ¿Qué porcentaje es?", ["Divido: 30 ÷ 150 = 0,2.", "Paso a porcentaje: 20 %."], "20 %"),
    ],
    mistakes=[("Responder a un argumento descalificando a quien lo dice.", "Un ataque personal no discute la evidencia ni la razón.", "Responde al argumento con otra evidencia."),
              ("Usar «todos» o «nadie» sin evidencia de todos.", "Se afirma más de lo que se puede probar.", "Cambia a «algunos» o «muchos» y agrega datos.")],
    T=[
        ("{F} ¿Qué postura propone que el Estado proteja a los afectados?", "La postura 2", "La ficha le asigna esa frase."),
        ("{F} ¿Qué dice la postura 3 sobre los países pobres?", "Que siguen dependiendo de exportar materias primas", "La ficha lo dice."),
        ("{F} ¿Qué reglas se propone cumplir en el debate?", "Respeto, evidencias y no atacar a las personas", "La ficha las enumera."),
        ("=", "{F} ¿Cuántas de las 100 personas encuestadas de la ficha no tienen acceso a internet?", "100-70", "Se resta quienes sí tienen acceso al total.", " personas"),
        ("{F} ¿Qué postura dice que las grandes empresas deciden demasiado?", "La postura 3", "La ficha le asigna esa frase."),
        ("{F} ¿Qué evidencia apoya mejor la postura 1? A) El comercio entre dos países pasó de 100 a 350 unidades B) La fábrica despidió a 90 trabajadores", "A) El comercio entre dos países pasó de 100 a 350 unidades", "Muestra crecimiento del comercio, argumento de la postura 1."),
        ("{F} ¿Qué evidencia apoya mejor la postura 2? A) La fábrica que despide al trasladar su producción, junto con el aumento del comercio B) Solo el acceso a internet", "A) La fábrica que despide al trasladar su producción, junto con el aumento del comercio", "Muestra beneficios y perjuicios a la vez."),
        ("{F} Alguien responde a la postura 3: «Eso lo dice una persona que no sabe nada». ¿Qué es eso? A) Un ataque personal B) Un argumento con evidencia", "A) Un ataque personal", "No discute el argumento sino a la persona."),
        ("{F} Alguien dice: «Con la globalización todos tienen internet». ¿Qué problema tiene? A) Generaliza a todos con una encuesta de 100 personas B) Usa un número", "A) Generaliza a todos con una encuesta de 100 personas", "La muestra no permite hablar de todos."),
        ("{F} ¿Por qué la postura 2 es una posición matizada?", "Porque reconoce beneficios y perjuicios y propone una acción del Estado", "No acepta ni rechaza la globalización por completo."),
        ("{F} ¿Qué dato necesitarías para evaluar si las ganancias del aumento del comercio se repartieron bien?", "Datos de ingresos y de empleo de distintos grupos antes y después del aumento", "El comercio total no dice quién ganó."),
        ("{F} Un compañero dice: «Si cambias de opinión en un debate, pierdes». ¿Qué respondes?", "Que cambiar de opinión por una buena evidencia es razonar, no perder", "Un debate busca entender mejor, no ganar a cualquier costo."),
        ("{F} ¿Cuál de estas afirmaciones es más proporcional a la ficha? A) La globalización trajo beneficios y perjuicios que dependen del grupo B) La globalización fue un desastre", "A) La globalización trajo beneficios y perjuicios que dependen del grupo", "La ficha muestra efectos mixtos."),
    ],
    ctx=("En una clase se debate la globalización y un estudiante cierra con «solo hay que mirar el comercio, que subió, y listo». ¿Qué le falta a su argumento? A) Datos sobre quiénes ganaron y quiénes perdieron B) Una cita de un político famoso", "A) Datos sobre quiénes ganaron y quiénes perdieron", "El comercio total no muestra el reparto de beneficios."),
    sc=[("En Historia: ¿qué es un argumento?", "Una afirmación apoyada en una razón y en una evidencia", "Así se define en el vocabulario."),
        ("En Historia: ¿qué es un ataque personal?", "Una crítica a la persona que habla y no a su argumento", "Así se define en la clase."),
        ("=", "En un grupo de ejemplo de 400 personas, 100 dicen haber ganado con la apertura. ¿Qué porcentaje es?", "100/400*100", "Se divide el grupo por el total y se multiplica por cien.", " %")],
    op=("Prepara un debate de dos minutos sobre «¿la globalización ha traído más beneficios que perjuicios?». Escribe tu postura en una frase, dos argumentos con su evidencia de la ficha, una respuesta a la postura contraria sin atacar a la persona y un límite de tu argumento. {F}",
        "Postura: matizada. Argumento 1: el comercio pasó de 100 a 350 unidades. Argumento 2: una fábrica despidió a 90 de 300 trabajadores. Respuesta: «Entiendo el beneficio del comercio, pero el dato de la fábrica muestra costos para algunos». Límite: los datos son de ejemplo y no representan a todo un país.",
        ["tiene postura clara", "usa dos evidencias de la ficha", "responde sin ataques personales", "reconoce un límite"], ["texto de debate"], ["generalizar con «todos»", "atacar a la persona y no al argumento"],
        "Pide que explique qué evidencia podría hacerlo cambiar de postura."),
    reinforce="Explica a alguien de tu casa una diferencia entre un argumento y una opinión sin evidencia.",
    extend="Piensa en un tema que se discuta en tu curso y escribe un argumento con una evidencia y un límite.",
)
