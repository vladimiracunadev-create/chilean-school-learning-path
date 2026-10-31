"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 16 (Constitución Política) y OA 17 (derechos de todas las personas)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA16, OA17 = "HI06 OA 16", "HI06 OA 17"

# ================================================================ OA 16 · clase 1
lesson(
    OA16, 1,
    "Aprenderé a ubicar en el tiempo y en el espacio la Constitución Política de Chile y a reconocer qué establece. Sirve para saber cuál es la ley más importante del país y por qué todos debemos respetarla.",
    ["Sé cuáles son los tres poderes del Estado.", "Sé que las leyes son reglas que debe cumplir la sociedad."],
    [
        "La Constitución Política de la República es la ley más importante de Chile. Establece cómo se organiza el país: cuáles son los poderes del Estado, cómo se eligen las autoridades y qué debe hacer cada una. También garantiza los derechos y las libertades de las personas y declara que Chile es una república democrática. Todas las leyes y todas las autoridades deben respetarla.",
        "Chile ha tenido varias constituciones. Las más conocidas son la de 1833, la de 1925 y la de 1980, que es la que está vigente, con reformas posteriores. Vigente quiere decir que hoy rige. En 2022 y 2023 la ciudadanía votó en plebiscitos textos de una nueva Constitución y no los aprobó, así que sigue vigente la de 1980. Un plebiscito es una votación directa de las personas para aprobar o rechazar una propuesta.",
        "La Constitución se ordena en capítulos. Por ejemplo, el Capítulo I trata de las bases de la institucionalidad, el III de los derechos y deberes constitucionales, el IV del Gobierno, el V del Congreso Nacional y el VI del Poder Judicial. Se aplica en todo el territorio de Chile y rige a todas las personas.",
    ],
    [("Constitución", "ley más importante del país; organiza el Estado y garantiza derechos"), ("vigente", "que rige hoy"), ("plebiscito", "votación directa para aprobar o rechazar una propuesta"), ("capítulo", "parte grande en que se divide un texto"), ("reforma", "cambio que se hace a un texto ya existente")],
    [
        ("Ordenar en el tiempo", "Ordena de la más antigua a la más reciente: Constitución de 1925, Constitución de 1833, Constitución de 1980.", ["La de 1833 es la menor.", "Luego 1925.", "Por último 1980."], "1833, 1925, 1980"),
        ("Calcular años", "La Constitución de 1980 fue aprobada ese año. ¿Cuántos años han pasado hasta 2025?", ["Resto los años.", "2025 menos 1980.", "Son 45 años."], "45 años"),
    ],
    [
        ("Pensar que Chile siempre tuvo la misma Constitución.", "Chile tuvo varias, como las de 1833, 1925 y 1980.", "Ubica cada una con su año."),
        ("Creer que la Constitución solo trata de las autoridades.", "También garantiza derechos y libertades de todas las personas.", "Recuerda sus dos funciones: organizar el Estado y garantizar derechos."),
    ],
    [
        ("¿Cuál es más antigua: la Constitución de 1833 o la de 1925?", "La de 1833", "1833 es un año anterior a 1925."),
        ("¿La Constitución vigente hoy es la de 1980 o la de 1925?", "La de 1980", "Sigue vigente con reformas."),
        ("¿La Constitución es la ley más importante del país o una ley de una comuna?", "La ley más importante del país", "Organiza todo el Estado."),
    ],
    [
        ("¿Qué dos cosas establece la Constitución según la clase?", "Organiza el Estado y garantiza derechos y libertades", "Esas son sus dos funciones centrales."),
        ("¿Por qué una Constitución puede cambiar con los años?", "Porque la sociedad cambia y se pueden hacer reformas", "Los textos se ajustan a nuevas necesidades."),
        ("¿Qué es un plebiscito?", "Una votación directa para aprobar o rechazar una propuesta", "Así se definió en el vocabulario."),
    ],
    [
        arith("Entre la Constitución de 1925 y la de 1980, ¿cuántos años pasaron?", "1980-1925", "Se resta el año menor al año mayor.", " años"),
        arith("Entre la Constitución de 1833 y la de 1925, ¿cuántos años pasaron?", "1925-1833", "Se resta el año menor al año mayor.", " años"),
        ("¿En qué capítulo de la Constitución se trata de los derechos y deberes: en el III o en el VI?", "En el III", "El VI trata del Poder Judicial."),
    ],
    [
        ("Pía dice: «Chile siempre tuvo la Constitución de 1980». ¿Qué error comete?", "Chile tuvo antes otras, como las de 1833 y 1925", "Las constituciones anteriores existieron antes de 1980."),
        ("Un compañero afirma: «La Constitución sirve solo a los presidentes». ¿Qué error comete?", "También protege los derechos y las libertades de todas las personas", "No es solo para las autoridades."),
    ],
    [
        ("Ordena de la más lejana a la más cercana en el tiempo: A) plebiscitos de 2022 y 2023, B) Constitución de 1925, C) Constitución de 1980.", "B, C, A", "1925 es el año menor y 2022 el mayor."),
        ("En un plebiscito sobre una nueva Constitución, ¿decide directamente cada persona con su voto o deciden solo los diputados?", "Cada persona con su voto", "Un plebiscito es una votación directa de las personas."),
    ],
    [("Un periodista escribe: «Hoy la ley más importante de Chile tiene reformas desde 1980». ¿Qué ley es?", "La Constitución", "Es la ley vigente con reformas.")],
    [("En Historia: ¿qué es la Constitución?", "La ley más importante del país", "Organiza el Estado y garantiza derechos."), ("¿Qué quiere decir «vigente»?", "Que rige hoy", "Es la definición de la clase."), ("¿Qué capítulo trata de los derechos y deberes?", "El III", "Así se enseñó en la clase.")],
    (
        "Haz una línea de tiempo con tres puntos: Constitución de 1833, Constitución de 1925 y Constitución de 1980. Bajo cada una escribe cuántos años pasaron desde la anterior. Escribe además cuál de las tres está vigente hoy y una cosa que establece cualquier Constitución.",
        "1833 (inicio); 1925 (92 años después); 1980 (55 años después). Vigente: 1980. Establece cómo se organiza el Estado.",
        ["ordena las tres constituciones", "calcula bien los años", "indica cuál está vigente"],
        ["línea de tiempo con tres puntos y una frase"],
        ["ordenar mal los años", "restar mal"],
        "Muestra tu línea de tiempo a una persona de tu casa y pídele que compruebe tus restas.",
    ),
    "Pregunta a una persona de tu casa qué recuerda de la Constitución y anótalo.",
    "Escribe una pregunta que te gustaría hacer sobre la Constitución.",
)

# ================================================================ OA 16 · clase 2
lesson(
    OA16, 2,
    "Aprenderé a leer frases de la Constitución explicadas en palabras sencillas y a reconocer si hablan de organización del país o de derechos. Sirve para usar el texto como fuente y no repetir rumores.",
    ["Sé que la Constitución organiza el Estado y garantiza derechos.", "Sé que una fuente tiene una procedencia."],
    [
        "El texto oficial de la Constitución es la fuente principal. Los resúmenes escolares, las explicaciones de un abogado y las noticias son fuentes que lo explican, pero pueden simplificar. Por eso preguntamos la procedencia: quién escribió la fuente, cuándo y para qué. Un resumen escolar busca enseñar; una opinión de un columnista busca convencer.",
        "Algunas ideas, dichas en palabras sencillas: el artículo 1 dice que las personas nacen libres e iguales en dignidad y derechos. El artículo 4 dice que Chile es una república democrática. El artículo 6 dice que los órganos del Estado deben actuar según la Constitución. El artículo 19 enumera derechos y libertades, como el derecho a la educación y la libertad de opinión. Las ideas sobre cómo se organiza el país hablan de poderes y de autoridades; las que hablan de derechos protegen a las personas.",
        "Al leer, separamos lo que dice el texto, lo que interpretamos y lo que no permite saber. Si una frase dice que todas las personas tienen derecho a opinar, no podemos concluir que no existan reglas que lo regulen. Para eso tendríamos que leer las leyes completas.",
    ],
    [("artículo", "parte numerada de un texto legal"), ("dignidad", "valor que tiene toda persona por el solo hecho de serlo"), ("libertad", "poder de actuar sin que otros lo impidan injustamente"), ("órgano del Estado", "institución del Estado, como el Congreso o los tribunales"), ("columnista", "persona que escribe una opinión en un medio")],
    [
        ("Clasificar una frase", "Frase: «Chile es una república democrática». ¿Habla de organización del país o de un derecho de las personas?", ["Dice cómo se gobierna Chile.", "No dice que una persona pueda hacer algo.", "Habla de organización."], "De organización del país"),
        ("Elegir la fuente", "Quieres saber qué dice exactamente el artículo 1. ¿Conviene leer el texto oficial o la opinión de un columnista?", ["El texto oficial es la fuente principal.", "La opinión busca convencer.", "Elijo el texto oficial."], "El texto oficial"),
    ],
    [
        ("Creer que un resumen reemplaza al texto oficial.", "Un resumen puede simplificar o dejar cosas fuera.", "Cuando puedas, compara con el texto oficial."),
        ("Tomar una opinión como si fuera lo que dice la Constitución.", "Una opinión busca convencer y puede no coincidir con el texto.", "Pregunta quién la escribió y para qué."),
    ],
    [
        ("Frase: «Toda persona tiene derecho a la educación». ¿Es un derecho o una regla de organización?", "Un derecho", "Dice qué puede exigir una persona."),
        ("¿El artículo 6 dice que los órganos del Estado deben actuar según la Constitución o según su gusto?", "Según la Constitución", "La Constitución es la regla más alta."),
        ("Una columna de opinión, ¿busca convencer o publicar el texto oficial completo?", "Convencer", "Expresa la opinión de quien escribe."),
    ],
    [
        ("¿Por qué conviene preguntar quién escribió un resumen de la Constitución?", "Para saber con qué propósito lo hizo y si simplificó algo", "La procedencia ayuda a evaluar la fuente."),
        ("¿Qué significa que las personas nacen libres e iguales en dignidad?", "Que todas valen lo mismo y tienen los mismos derechos", "Es la idea central del artículo 1."),
        ("¿Por qué la frase «Todos pueden opinar» no prueba que no haya reglas sobre la opinión?", "Porque una frase sola no muestra todas las leyes", "Habría que leer las leyes completas."),
    ],
    [
        ("Frase de ejemplo: «El Congreso hace las leyes». ¿Habla de derechos o de la organización del Estado?", "De la organización del Estado", "Dice qué función cumple un poder del Estado."),
        ("Frase de ejemplo: «Toda persona puede expresar su opinión». ¿Habla de un derecho o de un poder del Estado?", "De un derecho", "Dice lo que una persona puede hacer."),
        ("Una guía escolar dice: «El artículo 4 afirma que Chile es una república democrática». Para comprobarlo, ¿qué fuente conviene mirar?", "El texto oficial de la Constitución", "Es la fuente de donde sale la frase."),
    ],
    [
        ("Luis lee un resumen que dice que la Constitución protege la libertad de opinión y concluye: «Entonces nadie puede ser sancionado por lo que diga». ¿Qué error comete?", "El resumen no dice todas las reglas y límites que pueden existir", "Una frase no muestra toda la ley."),
        ("Ema encuentra un blog que dice que el artículo 1 cambió hace un mes, sin citar nada. ¿Qué pregunta de procedencia debe hacer?", "Quién lo escribió y de dónde sacó eso", "Sin fuente citada no se puede comprobar."),
    ],
    [
        ("Ordena los pasos para usar una fuente sobre la Constitución: A) sacar una conclusión, B) preguntar quién la escribió, C) leer qué dice.", "B, C, A", "Primero la procedencia, luego el contenido y al final la conclusión."),
        ("Tres frases: A) «Chile es una república democrática», B) «Toda persona tiene derecho a la educación», C) «Las personas nacen libres e iguales». ¿Cuántas hablan de derechos o de igualdad de las personas?", "2", "B y C hablan de las personas; A habla de la organización del país."),
    ],
    [("Una profesora lee en voz alta: «El artículo 19 enumera derechos y libertades». Un alumno pregunta de dónde sacó eso. ¿Qué respuesta la hace más confiable: «lo leí en el texto oficial» o «me lo dijeron»?", "Lo leí en el texto oficial", "Cita la fuente y se puede comprobar.")],
    [("¿Qué dice el artículo 4 en palabras sencillas?", "Que Chile es una república democrática", "Así se enseñó en la clase."), ("¿Cuál es la fuente principal sobre la Constitución?", "El texto oficial", "Los resúmenes lo explican pero pueden simplificar."), ("¿Una opinión de un columnista es el texto oficial?", "No", "Una opinión busca convencer, no es el texto.")],
    (
        "Lee estas cinco frases en palabras sencillas: 1) Las personas nacen libres e iguales. 2) Chile es una república democrática. 3) Toda persona tiene derecho a la educación. 4) Los órganos del Estado deben actuar según la Constitución. 5) Toda persona puede expresar su opinión. Clasifícalas en dos columnas: «derechos de las personas» y «organización del país». Escribe además una pregunta de procedencia para un resumen escolar.",
        "Derechos: 1, 3 y 5. Organización: 2 y 4. Pregunta: ¿quién escribió el resumen y con qué propósito?",
        ["clasifica las cinco frases", "justifica una clasificación", "formula una pregunta de procedencia"],
        ["tabla de dos columnas y una pregunta"],
        ["poner derechos en la columna de organización", "no hacer la pregunta"],
        "Pide a una persona de tu casa que clasifique las frases sin mirar tu tabla y compara.",
    ),
    "Escribe con tus palabras una frase de la Constitución que ya conocías.",
    "Escribe qué otra fuente usarías para entender la Constitución.",
)

# ================================================================ OA 16 · clase 3
lesson(
    OA16, 3,
    "Aprenderé a relacionar por qué existe una Constitución, quiénes la respetan y qué ocurre cuando no se cumple. Sirve para entender cómo se protegen los derechos y se limita el poder.",
    ["Sé qué establece la Constitución.", "Sé que una causa explica por qué ocurre algo."],
    [
        "La causa de tener una Constitución es proteger a las personas y limitar el poder. Si las autoridades pudieran hacer lo que quisieran, podrían abusar. La Constitución dice qué pueden hacer y qué no. Una consecuencia es que todas las autoridades, desde el Presidente hasta un alcalde, deben actuar dentro de lo que ella establece. Esto se llama respetar el Estado de derecho.",
        "Los actores que la respetan y la hacen respetar son muchos. El Congreso hace las leyes sin contradecirla. Los tribunales resuelven conflictos y protegen derechos; por ejemplo, una persona puede presentar un recurso de protección ante una Corte cuando cree que se vulneró un derecho. El Tribunal Constitucional revisa que las leyes no contradigan la Constitución. Y las personas, al votar, participar y cumplir las leyes, también cuentan.",
        "Las consecuencias de respetar la Constitución son buenas: hay democracia, libertades y confianza en las instituciones. Las consecuencias de no respetarla son graves: abusos, decisiones injustas y desconfianza. Por eso las autoridades deben rendir cuentas, que es explicar lo que hacen y asumir sus responsabilidades.",
    ],
    [("Estado de derecho", "situación en que todos, incluidas las autoridades, deben cumplir las leyes"), ("recurso de protección", "acción que presenta una persona ante una Corte cuando cree que se vulneró un derecho"), ("Tribunal Constitucional", "institución que revisa que las leyes no contradigan la Constitución"), ("abuso de poder", "usar el poder para dañar o favorecer a unos pocos"), ("rendir cuentas", "explicar lo que se hace y asumir las responsabilidades")],
    [
        ("Armar una cadena", "Una ley contradice la Constitución. El Tribunal Constitucional la revisa y la declara inconstitucional. Nombra causa, actor y consecuencia.", ["Causa: la ley contradice la Constitución.", "Actor: el Tribunal Constitucional.", "Consecuencia: la ley no se aplica."], "Causa: contradicción; actor: Tribunal Constitucional; consecuencia: la ley no se aplica"),
        ("Un derecho vulnerado", "Una persona cree que le impidieron ejercer un derecho. ¿Qué puede presentar ante una Corte: un recurso de protección o una propaganda?", ["El recurso de protección es la acción para eso.", "La propaganda no protege derechos.", "Elijo el recurso."], "Un recurso de protección"),
    ],
    [
        ("Creer que las autoridades pueden hacer cualquier cosa.", "Deben actuar dentro de lo que dice la Constitución.", "Pregunta qué límite pone la Constitución."),
        ("Pensar que solo las autoridades respetan la Constitución.", "Las personas también cumplen las leyes y participan.", "Incluye a todos los actores."),
    ],
    [
        ("¿Para qué existe una Constitución: para proteger a las personas y limitar el poder o para decidir el menú de la escuela?", "Para proteger a las personas y limitar el poder", "Esa es su causa principal."),
        ("Los tribunales y el Tribunal Constitucional, ¿son actores o consecuencias?", "Actores", "Participan en hacer respetar la Constitución."),
        ("El abuso de poder, ¿es una consecuencia buena o mala de no respetar la Constitución?", "Mala", "Perjudica a las personas."),
    ],
    [
        ("¿Por qué el Presidente también debe respetar la Constitución?", "Porque nadie está por encima de ella", "Todas las autoridades deben actuar dentro de lo que establece."),
        ("¿Qué consecuencia tiene respetar la Constitución?", "Hay democracia, libertades y confianza en las instituciones", "Así se enseñó en la clase."),
        ("¿Por qué las autoridades deben rendir cuentas?", "Para explicar lo que hacen y asumir sus responsabilidades", "Así los ciudadanos pueden controlarlas."),
    ],
    [
        ("Un alcalde de ejemplo quiere cerrar una radio solo porque criticó su gestión. ¿Qué principio de la Constitución estaría vulnerando: la libertad de opinión o la de transporte?", "La libertad de opinión", "Silenciar una crítica la restringe."),
        ("Ordena la cadena: A) la persona presenta un recurso de protección, B) la Corte revisa el caso, C) una autoridad vulnera un derecho.", "C, A, B", "Primero ocurre el hecho, luego se presenta el recurso y después se revisa."),
        ("Si una ley contradice la Constitución, ¿qué institución puede revisarla: el Tribunal Constitucional o el centro de estudiantes?", "El Tribunal Constitucional", "Esa es su función."),
    ],
    [
        ("Teo dice: «Si una autoridad no respeta la Constitución, no pasa nada». ¿Qué error comete?", "Hay consecuencias, como recursos ante los tribunales y la revisión de las leyes", "Existen mecanismos para exigir su cumplimiento."),
        ("Un país de ejemplo no tiene Constitución y el gobernante decide solo todo. ¿Qué riesgo corren las personas?", "Que haya abusos sin límites", "Nadie limita el poder."),
    ],
    [
        ("Ordena la cadena: A) se pierde la confianza en las instituciones, B) las autoridades no cumplen la Constitución, C) las personas se sienten desprotegidas.", "B, C, A", "Primero el incumplimiento, luego la desprotección y al final la desconfianza."),
        ("Un vecino y una alcaldesa discuten. El vecino cree que una decisión vulneró su derecho. ¿Quién puede ayudar a resolverlo: un tribunal o el Servel?", "Un tribunal", "Los tribunales resuelven conflictos y protegen derechos."),
    ],
    [("Una comunidad de ejemplo pide que se respete su derecho a recibir información clara sobre una obra pública. ¿Qué actor puede exigir esa información: los vecinos o un volcán?", "Los vecinos", "Las personas son actores que pueden exigir sus derechos.")],
    [("¿Para qué existe una Constitución?", "Para proteger a las personas y limitar el poder", "Es su causa principal."), ("¿Qué es el Estado de derecho?", "Que todos, incluidas las autoridades, deben cumplir las leyes", "Es la definición de la clase."), ("¿Qué institución revisa que las leyes no contradigan la Constitución?", "El Tribunal Constitucional", "Esa es su función.")],
    (
        "Elige uno de estos casos y escribe causa, actores, acción y dos consecuencias (una buena y una mala si no se actúa). Caso a) una autoridad impide una reunión pacífica de vecinos; caso b) una ley contradice un derecho de las personas; caso c) un ministro no explica en qué gastó el dinero.",
        "Caso c: causa: falta de rendición de cuentas; actores: ministro, Congreso, ciudadanos; acción: pedir explicaciones; consecuencia buena: más confianza; mala: desconfianza si no se explica.",
        ["nombra la causa y al menos dos actores", "explica la acción", "incluye consecuencia buena y mala"],
        ["cadena escrita en cinco partes"],
        ["omitir las consecuencias", "no nombrar actores"],
        "Lee tu cadena a una persona de tu casa y pídele que diga qué actor tiene la responsabilidad principal.",
    ),
    "Escribe una regla de tu curso y a quién obliga: solo a los alumnos o también a los adultos.",
    "Escribe qué pasaría en una escuela si nadie respetara las reglas.",
)

# ================================================================ OA 16 · clase 4
lesson(
    OA16, 4,
    "Aprenderé a comparar dos formas de organizar un país, una democrática con Constitución y otra donde el poder está concentrado, y a reconocer perspectivas distintas. Sirve para ver por qué el sistema democrático protege a las personas.",
    ["Sé qué establece la Constitución y por qué hay que respetarla.", "Sé que comparar exige criterios iguales."],
    [
        "Comparar es ver en qué se parecen y en qué se diferencian dos casos usando los mismos criterios. Aquí los criterios son: quién toma las decisiones, cómo se eligen las autoridades, si se respetan las libertades y si el poder tiene límites. Usaremos dos países inventados para practicar: Valdora y Norten.",
        "Valdora tiene una Constitución. Las autoridades se eligen por voto cada cierto tiempo, los poderes están divididos y las personas pueden opinar libremente. Norten no tiene elecciones; una sola persona decide todo, no se puede criticar y no hay tribunales independientes. Valdora funciona como una democracia; Norten, no. Chile se organiza como Valdora: con Constitución, elecciones y derechos.",
        "También comparamos perspectivas, o sea la mirada de personas distintas. Una estudiante de Valdora valora poder opinar. Un gobernante de Norten puede preferir que nadie lo critique. Un juez valora que las reglas se cumplan. Comparar perspectivas no es decir que todas valen igual; es entender qué valoran y qué consecuencias tiene cada sistema para las personas.",
    ],
    [("democracia", "sistema en que el pueblo elige a sus autoridades y estas tienen límites"), ("criterio", "regla igual para comparar dos cosas"), ("perspectiva", "mirada de una persona según su situación"), ("límite al poder", "regla que impide que una autoridad haga lo que quiera"), ("libertad de opinión", "poder de decir lo que se piensa sin ser castigado injustamente")],
    [
        ("Comparar con un criterio", "Valdora elige a sus autoridades por voto. Norten no tiene elecciones. Compara el criterio «cómo se eligen las autoridades».", ["Valdora: por voto.", "Norten: no hay elecciones.", "La diferencia es que en Valdora el pueblo elige."], "En Valdora se elige por voto; en Norten no hay elecciones"),
        ("Una semejanza", "Valdora y Norten tienen gobernantes. ¿Qué semejanza hay entre ellos en ese punto?", ["Ambos países tienen quien gobierna.", "Eso los hace parecidos en ese criterio.", "Pero se diferencian en cómo llegan y en sus límites."], "Ambos tienen gobernantes"),
    ],
    [
        ("Pensar que todo país con gobernante es una democracia.", "En una democracia el pueblo elige y el poder tiene límites.", "Usa los criterios de la clase."),
        ("Decir que todas las perspectivas valen lo mismo sobre un abuso.", "Entender una mirada no significa justificar un abuso.", "Explica qué valora cada persona y qué efecto tiene."),
    ],
    [
        ("En Valdora, ¿las autoridades se eligen por voto o las impone una sola persona?", "Por voto", "Así se describió en la clase."),
        ("En Norten, ¿se puede criticar al gobernante?", "No", "Así se describió en la clase."),
        ("Chile se organiza, ¿como Valdora o como Norten?", "Como Valdora", "Tiene Constitución, elecciones y derechos."),
    ],
    [
        ("¿Por qué la división de poderes es un límite al poder?", "Porque ninguna autoridad decide sola", "Se controlan unos a otros."),
        ("¿Por qué una estudiante de Valdora valora poder opinar?", "Porque su libertad de opinión está protegida", "Puede expresarse sin ser castigada."),
        ("¿Por qué no basta que haya un gobernante para que haya democracia?", "Porque también se necesitan elecciones y límites al poder", "Esas son las condiciones de la democracia."),
    ],
    [
        ("Tabla: Valdora, libertad de opinión: sí; Norten, libertad de opinión: no. ¿En cuál país una persona puede criticar sin miedo a sanciones injustas?", "En Valdora", "Tiene libertad de opinión."),
        ("Tabla: Valdora, tribunales independientes: sí; Norten, tribunales independientes: no. ¿En cuál país hay un poder que puede revisar a las autoridades?", "En Valdora", "Los tribunales independientes pueden revisar a las autoridades."),
        ("Tabla: Valdora, elecciones cada 4 años; Norten, elecciones: ninguna. ¿Cuántas elecciones habrá en Valdora en 12 años, si se hacen cada 4 años?", "3", "12 dividido en 4 es 3.", "12//4"),
    ],
    [
        ("Marta dice: «Norten es mejor porque las decisiones son más rápidas». ¿Qué falta considerar en su comparación?", "Que sin límites ni libertades las personas quedan desprotegidas", "Rapidez no reemplaza los derechos."),
        ("El gobernante de Norten dice que no se debe criticar. Una estudiante de Valdora dice que sí. ¿Son perspectivas iguales o distintas?", "Distintas", "Valoran cosas diferentes: control del poder y libertad."),
    ],
    [
        ("Ordena de más a menos protección de las personas: A) un país sin Constitución ni elecciones, B) un país con Constitución, elecciones y tribunales independientes, C) un país con Constitución, pero sin elecciones.", "B, C, A", "B tiene todas las protecciones, C tiene una y A ninguna."),
        ("Un país tiene elecciones, pero el gobernante no respeta las sentencias de los tribunales. ¿Cuál de los criterios de la clase falla: los límites al poder o la existencia de gobernantes?", "Los límites al poder", "Las sentencias no limitan al gobernante."),
    ],
    [("Dos países de ejemplo: en uno los vecinos pueden formar una junta para pedir un semáforo y en el otro no. ¿En cuál se respeta mejor la participación ciudadana?", "En el que permite formar la junta", "Permite que las personas se organicen.")],
    [("¿Qué es la democracia?", "El sistema en que el pueblo elige a sus autoridades y estas tienen límites", "Es la definición de la clase."), ("¿Qué es un límite al poder?", "Una regla que impide que una autoridad haga lo que quiera", "Es la definición de la clase."), ("¿Chile se parece a Valdora o a Norten?", "A Valdora", "Tiene elecciones, Constitución y derechos.")],
    (
        "Completa una tabla para comparar Valdora y Norten con estos criterios: quién decide, cómo se eligen las autoridades, libertad de opinión y límites al poder. Luego escribe la perspectiva de una estudiante de Valdora y la de un gobernante de Norten, en una frase cada una, y una frase final sobre por qué Chile necesita su Constitución.",
        "Quién decide: Valdora, varios poderes; Norten, una persona. Elecciones: Valdora sí; Norten no. Libertad de opinión: sí; no. Límites: sí; no.",
        ["usa los cuatro criterios en ambos países", "escribe dos perspectivas distintas", "explica por qué Chile necesita su Constitución"],
        ["tabla de cuatro filas y tres frases"],
        ["comparar con criterios distintos", "justificar un abuso"],
        "Lee tu tabla a una persona de tu casa y pídele que diga qué país protege mejor a las personas.",
    ),
    "Escribe una regla de tu curso que funcione como límite para todos, incluso para el delegado.",
    "Escribe una pregunta que le harías a un juez sobre cómo protege los derechos.",
)

# ================================================================ OA 17 · clase 1
lesson(
    OA17, 1,
    "Aprenderé a ubicar en el tiempo y el espacio la Declaración Universal de los Derechos Humanos y el artículo 19 de la Constitución, y a reconocer algunos derechos. Sirve para saber que todas las personas tienen derechos y que hay textos que los reconocen.",
    ["Sé que la Constitución garantiza derechos.", "Sé ubicar fechas en una línea de tiempo."],
    [
        "Los derechos son cosas que todas las personas pueden exigir por el solo hecho de ser personas, como vivir, aprender, opinar o recibir atención de salud. Deben ser respetados por los pares, es decir, las personas de la misma edad o condición, como tus compañeros; por la comunidad, como el barrio o la escuela; y por el Estado. Cuando se respetan, la sociedad es más justa.",
        "En 1948, la Organización de las Naciones Unidas (ONU) aprobó la Declaración Universal de los Derechos Humanos. Tiene 30 artículos y vale para todas las personas del mundo. Por ejemplo, el artículo 1 dice que todos los seres humanos nacen libres e iguales en dignidad y derechos, el artículo 3 reconoce el derecho a la vida, a la libertad y a la seguridad, y el artículo 26 reconoce el derecho a la educación.",
        "En Chile, la Constitución también reconoce derechos. Su artículo 1 repite que las personas nacen libres e iguales en dignidad y derechos. El artículo 19 enumera derechos y libertades: por ejemplo, el derecho a la vida y a la integridad (Nº 1), la igualdad ante la ley (Nº 2), el derecho a la educación (Nº 10) y la libertad de opinión (Nº 12). Así, los derechos se reconocen en el mundo y en el país.",
    ],
    [("derecho", "algo que toda persona puede exigir por ser persona"), ("par", "persona de tu misma edad o condición, como un compañero"), ("ONU", "organización de países del mundo, creada en 1945"), ("Declaración Universal de los Derechos Humanos", "texto de la ONU de 1948 que reconoce derechos de todas las personas"), ("igualdad ante la ley", "que todas las personas deben ser tratadas igual por la ley")],
    [
        ("Ubicar en el tiempo", "La Declaración Universal de los Derechos Humanos se aprobó en 1948. ¿Cuántos años han pasado hasta 2025?", ["Resto los años.", "2025 menos 1948.", "Son 77 años."], "77 años"),
        ("Identificar el derecho", "Un artículo dice que toda persona tiene derecho a aprender en una escuela. ¿Qué derecho es?", ["Aprender en una escuela es educación.", "La Declaración lo reconoce.", "Es el derecho a la educación."], "El derecho a la educación"),
    ],
    [
        ("Creer que los derechos son premios que se ganan.", "Los derechos corresponden a todas las personas por ser personas.", "Recuerda que no dependen del comportamiento ni de la edad."),
        ("Pensar que solo el Estado debe respetar los derechos.", "También deben respetarlos los pares y la comunidad.", "Piensa en quién debe respetar cada derecho."),
    ],
    [
        ("¿Qué organización aprobó la Declaración Universal de los Derechos Humanos: la ONU o la municipalidad?", "La ONU", "Es la organización de países del mundo."),
        ("¿La Declaración se aprobó en 1948 o en 1980?", "En 1948", "Es el año de su aprobación."),
        ("«Todas las personas deben ser tratadas igual por la ley», ¿es igualdad ante la ley o libertad de opinión?", "Igualdad ante la ley", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué decimos que los derechos son de todas las personas?", "Porque corresponden a las personas por el solo hecho de ser personas", "No dependen de lo que hagan."),
        ("¿Quiénes deben respetar los derechos según la clase?", "Los pares, la comunidad y el Estado", "Así se enseñó."),
        ("¿Por qué la Declaración se llama «universal»?", "Porque vale para todas las personas del mundo", "No se limita a un país."),
    ],
    [
        arith("La ONU se creó en 1945 y aprobó la Declaración en 1948. ¿Cuántos años después de su creación se aprobó?", "1948-1945", "Se resta el año anterior al posterior.", " años"),
        ("Artículo de ejemplo: «Toda persona tiene derecho a expresar su opinión». ¿Qué libertad es: de opinión o de transporte?", "De opinión", "Habla de expresar lo que se piensa."),
        ("Una niña no puede entrar a la escuela por ser mujer. ¿Qué derecho se le niega?", "El derecho a la educación", "Impedir su ingreso le quita su derecho a aprender."),
    ],
    [
        ("Luis dice: «Los derechos son para quienes se portan bien». ¿Qué error comete?", "Los derechos corresponden a todas las personas por ser personas", "No son un premio."),
        ("Un compañero se burla de otro por su origen. ¿Quién está faltando aquí al derecho a la igualdad: un compañero o el Estado?", "Un compañero", "Es un trato entre compañeros, o sea entre pares."),
    ],
    [
        ("Ordena en el tiempo: A) Declaración Universal de 1948, B) creación de la ONU en 1945, C) plebiscito de 1980.", "B, A, C", "1945 es menor que 1948 y este que 1980."),
        ("Un texto dice «Todos nacen libres e iguales en dignidad y derechos». ¿Es del artículo 1 o del artículo 26?", "Del artículo 1", "El artículo 26 trata de la educación."),
    ],
    [("En un patio, algunos niños no dejan jugar a uno por usar lentes. ¿Qué derecho se vulnera: la igualdad en dignidad o el derecho a la vivienda?", "La igualdad en dignidad", "Todos deben ser tratados con el mismo respeto.")],
    [("En Historia: ¿qué es un derecho?", "Algo que toda persona puede exigir por ser persona", "Es la definición de la clase."), ("¿Cuántos artículos tiene la Declaración Universal?", "30", "Así se enseñó en la clase."), ("¿Quién aprobó la Declaración Universal en 1948?", "La ONU", "Es la organización de países del mundo.")],
    (
        "Elige tres derechos de esta lista y escribe, para cada uno, a quién corresponde respetarlo (pares, comunidad o Estado) y un ejemplo cotidiano: vida, educación, opinión, igualdad ante la ley, salud. Añade el año de la Declaración Universal y escribe cuántos años pasaron hasta 2025.",
        "Educación: respetarlo corresponde al Estado y a la comunidad; ejemplo: ir a la escuela. Declaración: 1948; 77 años hasta 2025.",
        ["elige tres derechos", "indica quién debe respetar cada uno", "calcula bien los años"],
        ["tres ejemplos y un cálculo"],
        ["decir que los derechos son premios", "restar mal los años"],
        "Cuéntale tus ejemplos a una persona de tu casa y pídele que diga cuál le parece más fácil de olvidar.",
    ),
    "Escribe un derecho que uses todos los días y cómo lo ejerces.",
    "Escribe cómo puedes ayudar a que tus compañeros respeten un derecho.",
)

# ================================================================ OA 17 · clase 2
lesson(
    OA17, 2,
    "Aprenderé a leer artículos de la Declaración Universal y de la Constitución explicados en palabras sencillas y a reconocer qué derecho protegen. Sirve para identificar el derecho que se vulnera en una situación.",
    ["Sé que los derechos son de todas las personas.", "Sé que una fuente tiene una procedencia."],
    [
        "Para saber qué derechos tenemos, leemos fuentes: la Declaración Universal de los Derechos Humanos, la Constitución y también materiales escolares que las explican. Siempre preguntamos la procedencia, o sea quién lo escribió, cuándo y para qué. El texto original es la fuente más confiable; los resúmenes sirven para entender, pero pueden simplificar.",
        "Veamos algunos artículos de la Declaración en palabras sencillas. Artículo 1: las personas nacen libres e iguales en dignidad y derechos. Artículo 3: toda persona tiene derecho a la vida, a la libertad y a la seguridad. Artículo 7: todas las personas son iguales ante la ley. Artículo 18: libertad de pensamiento, de conciencia y de religión. Artículo 19: libertad de opinión y de expresión. Artículo 25: derecho a un nivel de vida adecuado, con salud, alimentación y vivienda. Artículo 26: derecho a la educación.",
        "Para usar un artículo, relacionamos la situación con el derecho. Si a un niño no lo dejan opinar en clase por ser pequeño, se afecta la libertad de opinión. Si no tiene acceso a una escuela, se afecta el derecho a la educación. No basta con opinar que algo es injusto: buscamos qué artículo apoya la idea.",
    ],
    [("artículo", "parte numerada de un texto legal"), ("libertad de pensamiento", "poder de pensar y creer sin que otros lo impidan"), ("libertad de expresión", "poder de decir lo que se piensa"), ("nivel de vida adecuado", "tener lo necesario para vivir bien: alimentación, salud, vivienda"), ("resumen", "texto corto que explica lo principal de otro")],
    [
        ("Relacionar situación y artículo", "A una niña no la dejan ir a la escuela. ¿Qué artículo de la Declaración se relaciona: el 26 (educación) o el 18 (religión)?", ["Se trata de ir a la escuela.", "Eso es educación.", "El artículo 26."], "El artículo 26"),
        ("Elegir la fuente", "Quieres saber qué dice el artículo 3. ¿Conviene leer el texto de la Declaración o un comentario sin firma?", ["El texto original es más confiable.", "El comentario no dice quién lo escribió.", "Elijo la Declaración."], "El texto de la Declaración"),
    ],
    [
        ("Usar un artículo sin leer qué dice.", "Se puede citar un derecho equivocado.", "Lee la idea del artículo antes de usarlo."),
        ("Creer que un resumen sin autor es tan confiable como el texto original.", "No se sabe quién lo escribió ni para qué.", "Pregunta la procedencia."),
    ],
    [
        ("¿El artículo 26 trata de la educación o de la vivienda?", "De la educación", "El artículo 26 reconoce el derecho a la educación."),
        ("¿El artículo 19 trata de la libertad de opinión y expresión o de la educación?", "De la libertad de opinión y expresión", "El artículo 19 reconoce esa libertad."),
        ("¿El artículo 3 reconoce el derecho a la vida o el derecho al descanso?", "El derecho a la vida", "Es el derecho a la vida, la libertad y la seguridad."),
    ],
    [
        ("¿Por qué conviene preguntar quién escribió un resumen?", "Para saber con qué propósito lo hizo y si simplificó algo", "La procedencia ayuda a evaluar la fuente."),
        ("¿Qué derecho protege el artículo 25 en palabras sencillas?", "Tener alimentación, salud y vivienda para vivir bien", "Se refiere a un nivel de vida adecuado."),
        ("¿Por qué no basta decir «eso es injusto» sin citar un artículo?", "Porque conviene apoyar la idea en un texto que reconozca el derecho", "El artículo es evidencia."),
    ],
    [
        ("Situación: a un niño no lo dejan opinar en clase porque es el más pequeño. ¿Qué libertad se afecta: la de expresión (art. 19) o la de transporte?", "La de expresión", "Se le impide decir lo que piensa."),
        ("Situación: una familia vive sin agua potable ni alimentación suficiente. ¿Qué artículo se relaciona: el 25 o el 18?", "El 25", "Trata de alimentación, salud y vivienda."),
        ("Situación: a un vecino lo tratan distinto ante un trámite por ser extranjero. ¿Qué artículo se relaciona: el 7 (igualdad ante la ley) o el 26?", "El 7", "Habla de que todos son iguales ante la ley."),
    ],
    [
        ("Pía lee un folleto sin firma que dice que el artículo 26 trata del trabajo. ¿Qué debe hacer?", "Comprobar en el texto original de la Declaración", "El artículo 26 trata de educación; un folleto sin firma no es confiable."),
        ("Teo dice: «Si algo me parece injusto, es violación de derechos». ¿Qué le falta a su idea?", "Un artículo o texto que reconozca ese derecho", "La evidencia da fuerza a la idea."),
    ],
    [
        ("Ordena los pasos para analizar un caso: A) buscar el artículo, B) leer la situación, C) explicar por qué el artículo se aplica.", "B, A, C", "Primero la situación, luego el artículo y después la explicación."),
        ("Se prohíbe a un grupo practicar su religión en privado. ¿Qué artículo de la Declaración se relaciona: el 18 o el 25?", "El 18", "Trata de libertad de pensamiento, conciencia y religión."),
    ],
    [("Un club de lectura impide que un socio exprese su opinión sobre un libro. Dos amigos discuten: uno cita el artículo 19 y otro el artículo 25. ¿Quién cita el artículo adecuado?", "El que cita el artículo 19", "Ese artículo trata de la libertad de opinión y expresión.")],
    [("¿Qué derecho reconoce el artículo 26?", "El derecho a la educación", "Así se enseñó en la clase."), ("¿Qué libertad reconoce el artículo 19?", "La libertad de opinión y de expresión", "Así se enseñó en la clase."), ("¿Qué artículo habla de igualdad ante la ley?", "El 7", "Así se enseñó en la clase.")],
    (
        "Une cada situación con el artículo de la Declaración que se relaciona y explica en una frase por qué: Situación 1) a un niño le prohíben hablar en clase; Situación 2) a una niña no la dejan inscribirse en la escuela; Situación 3) una familia no tiene dónde vivir. Artículos: 19 (libertad de expresión), 26 (educación), 25 (nivel de vida adecuado).",
        "Situación 1: artículo 19. Situación 2: artículo 26. Situación 3: artículo 25.",
        ["une bien las tres situaciones", "explica cada una con una frase", "cita el derecho con sus palabras"],
        ["tres uniones con una frase cada una"],
        ["confundir los artículos", "no explicar la relación"],
        "Pide a una persona de tu casa que lea una situación y adivine el artículo sin mirar tu respuesta.",
    ),
    "Escribe con tus palabras un artículo de la Declaración que hayas aprendido.",
    "Escribe una pregunta de procedencia para un folleto sobre derechos.",
)

# ================================================================ OA 17 · clase 3
lesson(
    OA17, 3,
    "Aprenderé a relacionar quién debe respetar cada derecho, qué causa que no se respete y qué consecuencias tiene. Sirve para entender por qué una sociedad justa necesita que pares, comunidad y Estado cumplan su parte.",
    ["Sé reconocer derechos en la Declaración y en la Constitución.", "Sé que una causa explica por qué ocurre algo."],
    [
        "Cada derecho tiene responsables. Los pares deben respetar al compañero que opina distinto o que tiene otro origen. La comunidad, como el barrio o la escuela, debe crear un ambiente donde todos puedan ejercer sus derechos. El Estado debe cumplir leyes, crear escuelas, hospitales y tribunales y proteger a las personas cuando alguien vulnera un derecho.",
        "Que un derecho no se respete tiene causas: prejuicios, ignorancia, falta de recursos o abuso de poder. Un prejuicio es una idea que se tiene sin conocer bien. Las consecuencias pueden ser graves: una persona queda excluida, tiene menos oportunidades o se siente insegura. Y también afectan a la comunidad, porque una sociedad con derechos no respetados es menos justa.",
        "Cuando todos cumplen su parte, la consecuencia es una sociedad más justa, donde las personas pueden desarrollarse y convivir. Por eso es importante identificar a los actores: quién vulnera el derecho, quién lo sufre, quién puede ayudar y quién debe garantizarlo.",
    ],
    [("par", "persona de tu misma edad o condición"), ("prejuicio", "idea que se tiene de alguien sin conocerlo bien"), ("excluir", "dejar fuera a alguien de un grupo o de una actividad"), ("sociedad justa", "sociedad en que los derechos de todos se respetan"), ("garantizar", "asegurar que algo se cumpla")],
    [
        ("Identificar actores", "En un patio, un grupo de niños deja fuera de un juego a una compañera por su acento. Nombra quién vulnera el derecho y quién lo sufre.", ["Quien vulnera es el grupo que la excluye.", "Quien lo sufre es la compañera.", "Respondo con ambos."], "Vulnera el grupo de niños; lo sufre la compañera"),
        ("Una cadena de causa y consecuencia", "Un prejuicio hace que se burlen de un compañero. Nombra una consecuencia para él.", ["El prejuicio causa burlas.", "El compañero se siente excluido.", "Esa es la consecuencia."], "Se siente excluido o inseguro"),
    ],
    [
        ("Creer que solo el Estado debe garantizar derechos.", "Los pares y la comunidad también deben respetarlos.", "Nombra a todos los responsables."),
        ("Pensar que un derecho no respetado solo afecta a una persona.", "También afecta a la comunidad, que se vuelve menos justa.", "Mira las consecuencias para la persona y para todos."),
    ],
    [
        ("Un prejuicio, ¿es una idea sin conocer bien a alguien o un dato comprobado?", "Una idea sin conocer bien a alguien", "Así se definió en el vocabulario."),
        ("Excluir a un compañero de un juego por cómo habla, ¿respeta o vulnera su derecho a la igualdad?", "Vulnera", "Lo trata distinto sin razón."),
        ("¿Quién debe crear escuelas y hospitales: el Estado o un compañero?", "El Estado", "Es una responsabilidad del Estado."),
    ],
    [
        ("¿Por qué la comunidad también tiene responsabilidad con los derechos?", "Porque crea el ambiente donde las personas pueden ejercerlos", "El barrio y la escuela influyen en cómo se vive."),
        ("¿Por qué un prejuicio puede causar que un derecho no se respete?", "Porque lleva a tratar mal a alguien sin conocerlo", "La idea errónea dirige la conducta."),
        ("¿Qué consecuencia tiene que todos respeten los derechos?", "La sociedad es más justa", "Así se enseñó en la clase."),
    ],
    [
        ("Una escuela de ejemplo no tiene rampa y un estudiante en silla de ruedas no puede entrar. ¿Qué derecho se afecta: educación o descanso?", "Educación", "No puede acceder a la escuela."),
        ("En el mismo caso, ¿qué acción garantiza su derecho a aprender: construir una rampa o dejar la escuela como está?", "Construir una rampa", "Una rampa permite que entre a la escuela y ejerza su derecho."),
        arith("Una comunidad de ejemplo reúne 40 familias que aportan $5.000 cada una para una rampa. ¿Cuánto dinero reúnen?", "40*5000", "Se multiplica el número de familias por el aporte.", " pesos"),
    ],
    [
        ("Luis dice: «Si un compañero tiene otra opinión, no tiene los mismos derechos». ¿Qué error comete?", "Todas las personas tienen los mismos derechos aunque piensen distinto", "El derecho no depende de la opinión."),
        ("Una autoridad de ejemplo cierra una escuela sin ofrecer otra cerca. ¿Qué derecho puede afectar y quién es el actor principal?", "El derecho a la educación; el Estado o la autoridad", "La decisión la toma una autoridad."),
    ],
    [
        ("Ordena la cadena: A) el compañero se aleja del curso, B) hay un prejuicio sobre su origen, C) lo excluyen de los juegos.", "B, C, A", "Primero el prejuicio, luego la exclusión y después la consecuencia."),
        ("Un vecino reclama porque su hijo tiene fiebre y el consultorio no lo atiende. ¿Qué derecho defiende: un nivel de vida adecuado, con salud, o la libertad de religión?", "Un nivel de vida adecuado, con salud", "El artículo 25 incluye la salud."),
    ],
    [("En una escuela, un niño con discapacidad auditiva no puede seguir las clases porque no hay ayuda para comunicarse. ¿Qué ayuda concreta garantiza su derecho a aprender: contar con un intérprete de lengua de señas o suspender sus clases?", "Contar con un intérprete de lengua de señas", "Así puede seguir las clases; suspenderlas le quitaría el derecho a aprender.")],
    [("¿Qué es un prejuicio?", "Una idea que se tiene sin conocer bien a alguien", "Es la definición de la clase."), ("¿Quiénes deben respetar los derechos?", "Los pares, la comunidad y el Estado", "Así se enseñó."), ("¿Qué consecuencia tiene que los derechos se respeten?", "Una sociedad más justa", "Es el resultado de que todos cumplan su parte.")],
    (
        "Elige uno de estos casos y escribe: quién vulnera el derecho, quién lo sufre, quién puede ayudar, una consecuencia y una solución. Caso a) a una estudiante no la dejan participar en un taller por su apariencia; caso b) en un barrio no hay ninguna plaza ni lugar para jugar; caso c) un niño es burlado por su acento.",
        "Caso c: vulnera el grupo que se burla; sufre el niño; puede ayudar la profesora; consecuencia: se siente excluido; solución: conversar y respetar.",
        ["nombra los cuatro actores", "explica la consecuencia", "propone una solución"],
        ["cinco frases escritas"],
        ["no distinguir quién vulnera y quién sufre", "no incluir solución"],
        "Lee tu caso a una persona de tu casa y pídele que diga quién podría ayudar además de quien tú escribiste.",
    ),
    "Escribe un derecho que debe respetar tu curso y una acción que lo asegure.",
    "Escribe qué harías si ves que a un compañero no le respetan un derecho.",
)

# ================================================================ OA 17 · clase 4
lesson(
    OA17, 4,
    "Aprenderé a comparar situaciones en las que se respeta o no un derecho y a reconocer perspectivas distintas de las personas involucradas. Sirve para analizar con justicia un caso antes de opinar.",
    ["Sé relacionar causas y consecuencias de no respetar un derecho.", "Sé que comparar exige criterios iguales."],
    [
        "Para comparar dos situaciones usamos los mismos criterios: qué derecho está en juego, quién lo respeta o lo vulnera, qué consecuencias tiene y qué solución existe. Así evitamos juzgar a la ligera. Comparar no significa que todas las situaciones sean iguales; significa fijarnos en lo mismo en cada una.",
        "Veamos dos escuelas de ejemplo. En la Escuela Roble, todos los niños pueden opinar en el consejo de curso y se escuchan los distintos puntos de vista. En la Escuela Pino, solo opinan los más grandes y los demás no son escuchados. El derecho en juego es el mismo, la libertad de expresión. En Roble se respeta y en Pino no. La consecuencia en Pino es que algunos niños se sienten ignorados.",
        "Cada persona tiene una perspectiva, es decir, una mirada según su situación. Un niño pequeño de Pino quiere ser escuchado. Un estudiante mayor puede pensar que así es más rápido. Un director puede querer orden. Entender las perspectivas ayuda a buscar soluciones, pero no significa que todas justifiquen una injusticia.",
    ],
    [("criterio", "regla igual para comparar dos cosas"), ("perspectiva", "mirada de una persona según su situación"), ("vulnerar", "no respetar o dañar un derecho"), ("consejo de curso", "reunión de los estudiantes de un curso para conversar y decidir"), ("solución", "acción que resuelve un problema")],
    [
        ("Comparar con criterios", "Roble escucha las opiniones de todos los cursos; Pino solo escucha a los más grandes. Compara el criterio «a quién se escucha».", ["En Roble, a todos.", "En Pino, solo a los mayores.", "La diferencia es la inclusión."], "Roble escucha a todos; Pino solo a los mayores"),
        ("Una semejanza", "Roble y Pino tienen consejo de curso. ¿Qué semejanza hay entre ambas escuelas?", ["Las dos tienen un espacio para opinar.", "Eso las hace parecidas.", "Cambia a quién escuchan."], "Ambas tienen consejo de curso"),
    ],
    [
        ("Decidir que una situación es injusta sin comparar con criterios.", "Se puede olvidar quién la vive y por qué.", "Usa criterios iguales."),
        ("Pensar que entender una perspectiva justifica vulnerar un derecho.", "Una mirada puede explicar algo, pero no lo hace correcto.", "Distingue entender de justificar."),
    ],
    [
        ("En Pino, ¿se respeta o se vulnera la libertad de expresión de los más chicos?", "Se vulnera", "Los más chicos no son escuchados."),
        ("En Roble, ¿se escucha a todos o solo a los mayores?", "A todos", "Así se describió."),
        ("Un criterio de comparación, ¿es una regla igual para ambos casos o una opinión?", "Una regla igual para ambos casos", "Así se compara lo mismo."),
    ],
    [
        ("¿Por qué conviene usar los mismos criterios al comparar situaciones?", "Para comparar lo mismo en cada una", "Así el análisis es justo."),
        ("¿Por qué entender la perspectiva del director no justifica que se ignore a los más chicos?", "Porque los derechos de los niños deben respetarse igual", "Una mirada no justifica vulnerar un derecho."),
        ("¿Qué consecuencia tiene en Pino que no se escuche a los más chicos?", "Se sienten ignorados", "No se toman en cuenta sus ideas."),
    ],
    [
        ("Tabla: Escuela A, 3 de 5 cursos tienen representante; Escuela B, 5 de 5. ¿En cuál escuela todos los cursos están representados?", "En la B", "5 de 5 son todos los cursos."),
        ("Con la tabla anterior, ¿cuántos cursos no tienen representante en la escuela A?", "2", "5 menos 3 es 2.", "5-3"),
        ("Dos situaciones: en una se prohíbe a un niño ir a la escuela; en otra se prohíbe a un niño jugar en el recreo por mal comportamiento. ¿En cuál se afecta un derecho básico, como la educación?", "En la primera", "Impedir ir a la escuela vulnera el derecho a aprender."),
    ],
    [
        ("Marta dice: «Es lo mismo que no dejen opinar a un niño que perder un recreo». ¿Qué error comete al comparar?", "Compara derechos de distinta importancia como si fueran iguales", "Impedir opinar afecta un derecho; perder un recreo es una sanción pasajera."),
        ("Un estudiante mayor dice que es mejor que solo los grandes opinen para ir más rápido. Una niña pequeña quiere opinar. ¿Son perspectivas iguales o distintas?", "Distintas", "Cada uno parte de su situación."),
    ],
    [
        ("Ordena de más a menos respeto al derecho a opinar: A) se escucha a todos, B) solo se escucha a algunos, C) no se escucha a nadie.", "A, B, C", "Se escucha a más personas en A."),
        arith("En el consejo de la Escuela Roble opinan 6 estudiantes por curso y hay 5 cursos. ¿Cuántos estudiantes opinan en total?", "6*5", "Se multiplica por el número de cursos.", " estudiantes"),
    ],
    [("Dos escuelas deben decidir el color del mural. En una votan todos los cursos y en otra decide la directora sola. ¿Qué criterio permite comparar ambas?", "Quién participa en la decisión", "En una participan todos y en la otra una sola persona.")],
    [("¿Para qué sirven los criterios al comparar?", "Para comparar lo mismo en ambos casos", "Así se compara con justicia."), ("¿Entender una perspectiva justifica vulnerar un derecho?", "No", "Entender no es justificar."), ("¿Qué es vulnerar un derecho?", "No respetarlo o dañarlo", "Es la definición de la clase.")],
    (
        "Completa una tabla para comparar dos situaciones inventadas con estos criterios: derecho en juego, quién lo respeta o vulnera, consecuencia y solución. Situación A: en una biblioteca de barrio pueden entrar todos los niños. Situación B: en otra biblioteca solo entran niños de ciertos colegios. Luego escribe la perspectiva de un bibliotecario y la de un niño que no puede entrar.",
        "Derecho: educación y acceso a la cultura. A respeta; B vulnera. Consecuencia en B: algunos niños no leen. Solución: abrir a todos.",
        ["usa los cuatro criterios en ambas", "escribe dos perspectivas distintas", "propone una solución"],
        ["tabla de cuatro filas y dos frases"],
        ["comparar con criterios distintos", "justificar la exclusión"],
        "Muestra tu tabla a una persona de tu casa y pídele que diga si la solución es realista.",
    ),
    "Escribe una situación de tu barrio donde se respete un derecho y una donde no.",
    "Escribe una pregunta para entender la perspectiva de una persona que vive una injusticia.",
)

# ================================================================ OA 17 · clase 5
lesson(
    OA17, 5,
    "Aprenderé a argumentar con evidencia que una situación respeta o vulnera un derecho, citando un artículo de la Declaración Universal o de la Constitución. Sirve para defender los derechos con razones y no solo con opiniones.",
    ["Sé reconocer derechos y relacionarlos con artículos.", "Sé que un argumento tiene afirmación, evidencia y razón."],
    [
        "Argumentar es defender una idea con evidencia y razones. En derechos humanos, una afirmación puede ser «en esta situación se vulnera un derecho». La evidencia es el hecho concreto que ocurre y el artículo que reconoce ese derecho. La razón explica por qué el hecho contradice el artículo.",
        "Veamos un ejemplo. Afirmación: «Se vulnera la libertad de expresión de los alumnos». Evidencia: el director prohíbe que los alumnos publiquen opiniones en el diario mural, y el artículo 19 de la Declaración reconoce la libertad de opinión y expresión. Razón: prohibir publicar opiniones impide expresarse. Límite: no sabemos si el director tiene una razón válida, como evitar insultos, así que falta información.",
        "Al argumentar, evitamos las exageraciones y las generalizaciones. Un solo hecho no demuestra que siempre ocurra. También escuchamos a quienes piensan distinto. Un buen argumento convence porque se puede comprobar, no porque se diga con fuerza.",
    ],
    [("argumento", "idea defendida con evidencia y razones"), ("afirmación", "lo que se sostiene"), ("evidencia", "hecho o dato que apoya una afirmación"), ("razón", "explicación de por qué la evidencia apoya la afirmación"), ("límite", "lo que la evidencia no permite saber")],
    [
        ("Identificar las partes", "«Se vulnera el derecho a la educación, porque a una niña no la dejan matricularse y el artículo 26 reconoce ese derecho.» ¿Cuál es la evidencia?", ["La afirmación es que se vulnera el derecho.", "La evidencia es el hecho y el artículo 26.", "Los separo."], "Que no la dejan matricularse y el artículo 26"),
        ("Reconocer un límite", "Un alumno ve que en un colegio cerraron una biblioteca y concluye: «En todos los colegios cierran bibliotecas». ¿Qué límite no respeta?", ["Es un solo colegio.", "No muestra otros.", "No se puede generalizar."], "Un colegio no representa a todos"),
    ],
    [
        ("Dar una opinión sin citar un artículo ni un hecho.", "Una opinión sin evidencia no convence.", "Agrega un hecho y un artículo."),
        ("Usar un artículo que no se relaciona con la situación.", "La evidencia debe apoyar justo lo que se afirma.", "Revisa qué dice el artículo."),
    ],
    [
        ("Una afirmación, ¿es lo que alguien sostiene o el dato que lo apoya?", "Lo que alguien sostiene", "El dato que lo apoya es la evidencia."),
        ("El artículo 26, ¿puede ser evidencia para defender el derecho a la educación?", "Sí", "Reconoce ese derecho."),
        ("La razón, ¿explica por qué la evidencia apoya la afirmación o repite el hecho?", "Explica por qué la evidencia apoya la afirmación", "Conecta el hecho con el derecho."),
    ],
    [
        ("¿Por qué conviene citar un artículo al defender un derecho?", "Porque da una base que se puede comprobar", "El artículo es evidencia."),
        ("¿Por qué conviene decir qué no sabemos?", "Para no afirmar más de lo que muestra la evidencia", "Así se evitan las exageraciones."),
        ("¿Por qué un solo hecho no demuestra que algo ocurra siempre?", "Porque puede ser un caso aislado", "Se necesitan más casos."),
    ],
    [
        ("Afirmación: «Se afecta la libertad de expresión». ¿Qué evidencia sirve: «prohibieron publicar opiniones en el diario mural» o «el diario mural es grande»?", "Prohibieron publicar opiniones en el diario mural", "Es un hecho que restringe la expresión."),
        ("Afirmación: «Hay desigualdad ante la ley». ¿Qué artículo sirve: el 7 o el 26?", "El 7", "Reconoce que todas las personas son iguales ante la ley."),
        ("Afirmación: «Una familia no tiene un nivel de vida adecuado». ¿Qué evidencia sirve: «no tiene dónde vivir ni qué comer» o «tiene un perro»?", "No tiene dónde vivir ni qué comer", "Se relaciona con vivienda y alimentación."),
    ],
    [
        ("Eva escribe: «Es injusto porque sí». ¿Qué le falta a su argumento?", "Un hecho concreto y un artículo que lo apoye", "Una frase sin evidencia no se puede comprobar."),
        ("Un alumno cuenta que en su curso se burlaron de él y concluye: «En todo el colegio se burlan de todos». ¿Qué límite no respeta?", "Un caso no representa a todo el colegio", "Generaliza con un solo hecho."),
    ],
    [
        ("Ordena un argumento: A) razón, B) afirmación, C) evidencia.", "B, C, A", "Primero se afirma, luego se muestra el hecho y por último se explica."),
        ("Dos casos: en uno no dejan a una niña estudiar y en otro la dejan estudiar. Afirmación: «Solo en el primero se vulnera el derecho a la educación». ¿Qué hecho es la evidencia principal?", "Que no la dejan estudiar", "Es el hecho que contradice el derecho."),
    ],
    [("Un vecino dice: «Mi derecho a opinar se vulnera porque me quitaron el micrófono en la reunión». Su compañero responde: «Pero ya habías hablado 20 minutos». ¿Qué información falta para evaluar el caso?", "Cuántas personas más querían hablar y si había reglas de tiempo", "Falta saber si se aplicó una regla igual para todos.")],
    [("¿Qué partes tiene un buen argumento?", "Afirmación, evidencia y razón", "Así se enseñó en la clase."), ("¿Qué es un límite?", "Lo que la evidencia no permite saber", "Es la definición del vocabulario."), ("¿Un solo hecho prueba que algo ocurre siempre?", "No", "Puede ser un caso aislado.")],
    (
        "Elige una de estas situaciones inventadas y escribe un argumento de cuatro frases (afirmación, evidencia con artículo, razón y límite). Situación a) en un colegio, un profesor no deja que una alumna hable por su acento. Situación b) en una población, un grupo de niños no puede ir a la escuela porque el bus no pasa. Artículos que puedes usar: 19 (opinión), 26 (educación), 7 (igualdad ante la ley).",
        "Situación b: afirmación: se afecta la educación. Evidencia: los niños no llegan a la escuela; artículo 26. Razón: sin transporte no pueden estudiar. Límite: no sabemos si hay otra ruta.",
        ["incluye afirmación, evidencia y razón", "cita un artículo correcto", "reconoce un límite"],
        ["cuatro frases escritas"],
        ["citar un artículo que no corresponde", "no reconocer el límite"],
        "Lee tu argumento a una persona de tu casa y pídele que diga si la evidencia es suficiente.",
    ),
    "Escribe un hecho que hayas visto en el que se respetó un derecho y cita el artículo que lo reconoce.",
    "Escribe qué otra información necesitarías para estar seguro de que un derecho fue vulnerado.",
)
