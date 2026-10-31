"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 15 (esfuerzo, mérito y reconocimiento) y OA 16 (actitudes cívicas en la vida cotidiana)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA15, OA16 = "HI05 OA 15", "HI05 OA 16"
E = ex


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


# ================================================================ OA 15
register(
    OA15, 1,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a distinguir lo que es un derecho de lo que es un logro que depende del esfuerzo, el mérito y el comportamiento. Sirve para entender por qué algunas cosas se ganan y otras se tienen por ser persona.",
    prior=["Sé que los derechos son de todas las personas.", "Sé que las normas tienen derechos y deberes."],
    explain=[
        "Un derecho se tiene por ser persona y no se pierde por tener un mal día. Ir a la escuela y recibir atención de salud son derechos. En cambio, algunos beneficios y logros dependen de lo que cada persona hace: una buena calificación, un premio deportivo, un premio por compañerismo, el aprecio de los compañeros o ser elegido líder de un grupo.",
        "El mérito es el valor que se reconoce a una persona por su esfuerzo y sus resultados, según reglas conocidas. Dos estudiantes pueden tener el mismo derecho a aprender, pero obtener notas distintas porque estudiaron de manera diferente. Eso no quiere decir que uno tenga más derechos que el otro.",
        "El comportamiento también cuenta. Ayudar a otros, cumplir los acuerdos y trabajar en equipo puede dar reconocimiento, como un diploma o la confianza del curso. Para ubicar cada caso, preguntamos: ¿esto lo tienen todas las personas, o depende de lo que la persona hace?",
    ],
    vocab=[("mérito", "valor que se reconoce por el esfuerzo y los resultados"), ("logro", "algo que se alcanza con esfuerzo"), ("reconocimiento", "aprecio o premio por algo bien hecho"), ("liderazgo", "capacidad de guiar a un grupo y ayudarlo a lograr algo"), ("calificación", "nota que mide cuánto se aprendió")],
    worked=[
        W("Derecho o logro", "Clasifica: A) recibir atención de salud; B) ganar una medalla en una carrera. ¿Cuál es derecho y cuál logro?",
          ["Pregunto si lo tienen todas las personas.", "La atención de salud la tienen todas.", "La medalla depende del resultado."], "A es un derecho; B es un logro"),
        W("Qué depende de la persona", "Dos estudiantes tienen igual derecho a aprender. Uno estudia todos los días y el otro no. ¿Qué podría diferir?",
          ["El derecho es igual.", "El esfuerzo es distinto.", "Las notas pueden ser distintas."], "Las calificaciones"),
    ],
    mistakes=[
        M("Pensar que tener una mala nota significa perder el derecho a seguir estudiando.", "El derecho a aprender no depende de las notas.", "Distingue la calificación del derecho."),
        M("Creer que un premio es un derecho que todos deben recibir sin esfuerzo.", "Un premio reconoce un logro según reglas.", "Pregunta qué hay que lograr."),
    ],
    tiers=tiers(
        [E("Una buena calificación, ¿depende del esfuerzo o la tienen todas las personas por ser personas?", "Del esfuerzo", "Se obtiene según lo que cada uno aprende."),
         E("Recibir atención de salud, ¿es un derecho o un premio?", "Un derecho", "Lo tienen todas las personas."),
         E("Un premio por compañerismo, ¿se gana por el comportamiento o se tiene por haber nacido?", "Por el comportamiento", "Reconoce cómo trata la persona a otros.")],
        [E("¿Qué es el mérito?", "El valor que se reconoce por el esfuerzo y los resultados", "Es la definición de la clase."),
         E("¿Por qué dos estudiantes con el mismo derecho a aprender pueden tener notas distintas?", "Porque estudiaron o se esforzaron de manera distinta", "La nota mide lo aprendido."),
         E("¿Qué pregunta ayuda a distinguir un derecho de un logro?", "Si lo tienen todas las personas o depende de lo que hace cada una", "Esa es la pregunta de la clase.")],
        [E("Clasifica cada caso como derecho o logro: a) ser escuchado; b) ganar un campeonato de ajedrez; c) recibir un diploma por ayudar a compañeros.", "a derecho; b logro; c logro", "Ser escuchado es de todos; el campeonato y el diploma se ganan."),
         E("Una niña estudió dos semanas para una prueba y sacó nota 7. ¿Es un derecho o un logro?", "Un logro", "Fue resultado de su esfuerzo."),
         E("Un grupo elige a Tomás como líder del curso porque ayuda y organiza. ¿Qué reconocimiento recibió: aprecio de pares o un derecho?", "Aprecio de sus pares", "Fue elegido por su comportamiento.")],
        [E("Leo dice: «Si saco mala nota, pierdo mi derecho a la educación». ¿Qué error tiene?", "El derecho a la educación no depende de las notas", "La nota es un logro, el derecho es de todos."),
         E("Una escuela no deja entrar a un estudiante porque perdió un partido. ¿Respeta su derecho a la educación? Responde sí o no.", "No", "Perder un partido no quita ese derecho.")],
        [E("Une cada caso con su tipo: premio al mejor promedio, atención en un consultorio, medalla de natación. Tipos: derecho, logro.", "Mejor promedio: logro; consultorio: derecho; medalla: logro", "Los premios y medallas se ganan; la atención de salud es un derecho."),
         E("Estas tres cosas: A) recibir un diploma de compañerismo, B) obtener un 7 en una prueba, C) recibir atención de salud. Escribe las dos que dependen de lo que hace la persona.", "A y B", "El diploma y la nota dependen del comportamiento o del esfuerzo; la atención de salud no.")],
    ),
    context=[E("En un colegio, todos pueden usar la biblioteca y además hay un premio al estudiante que más libros lee en el año. ¿Cuál de las dos cosas es un logro que se gana?", "El premio al que más libros lee", "Depende del esfuerzo de cada estudiante.")],
    selfcheck=[E("Explica con una frase qué significa mérito.", "El valor que se reconoce por esfuerzo y resultados", "Es la definición de la clase."), E("¿La atención de salud depende de las notas?", "No", "Es un derecho de todos."), E("Nombra un logro que se gana con esfuerzo.", "Por ejemplo: una buena calificación", "Depende de lo que hace la persona.")],
    open_task=task("Haz una tabla con tres derechos y tres logros. Para cada logro anota qué esfuerzo o comportamiento ayuda a lograrlo. Usa como ayuda estos ejemplos: derecho a estudiar, derecho a ser escuchado, derecho a la salud, premio deportivo, nota 7, diploma de compañerismo.", "Derechos: estudiar, ser escuchado, salud. Logros: premio deportivo (entrenar), nota 7 (estudiar), diploma (ayudar).", ["clasifica los seis ejemplos correctamente", "explica el esfuerzo de cada logro", "separa claramente derecho de logro"], ["tabla de dos columnas"], ["poner un derecho como logro", "no explicar el esfuerzo"], "Pide a una persona que diga si está de acuerdo con tu clasificación."),
    reinforce="Escribe un logro que obtuviste con esfuerzo y qué hiciste para alcanzarlo.",
    extend="Escribe por qué es importante que los premios tengan reglas conocidas.",
)

register(
    OA15, 2,
    materials="Este cuaderno y un lápiz. Los textos y tablas están escritos en los ejercicios.",
    use="Aprenderé a leer bases de un premio o una tabla de resultados y a preguntar quién reconoce, con qué reglas y para qué. Sirve para saber si un reconocimiento es justo.",
    prior=["Sé distinguir derechos de logros.", "Sé preguntar por la procedencia de una fuente."],
    explain=[
        "Los reconocimientos tienen reglas. Las bases son el documento que dice quién puede participar, qué se evalúa y cómo se decide el ganador. Una tabla de puntajes muestra los resultados de cada participante. Un diploma dice quién lo entrega y por qué.",
        "Para leer una fuente de este tipo preguntamos: ¿quién otorga el premio?, ¿qué criterios usa?, ¿son iguales para todos?, ¿se conocían antes? Un reconocimiento es más justo si las reglas se informan antes y se aplican igual a todos.",
        "También hay que ver lo que la fuente no dice. Una tabla de puntajes no explica si alguien tuvo menos oportunidades de practicar o si estuvo enfermo. Por eso hablamos de mérito con cuidado: miramos el esfuerzo y las reglas, sin burlarnos de quien no ganó.",
    ],
    vocab=[("bases", "documento que explica las reglas de un premio o concurso"), ("criterio", "regla para decidir quién gana"), ("puntaje", "número que mide el desempeño"), ("otorgar", "dar un premio o reconocimiento"), ("justo", "que trata igual a todos con reglas conocidas")],
    worked=[
        W("Leer unas bases", "Bases de ejemplo: «Premio al compañerismo: se evaluará si el estudiante ayuda a otros, respeta turnos y escucha». ¿Cuáles son los criterios?",
          ["Busco lo que se evaluará.", "Ayudar a otros, respetar turnos y escuchar.", "Son tres criterios."], "Ayudar a otros, respetar turnos y escuchar"),
        W("Leer una tabla", "Puntajes de ejemplo: Ana 18, Beto 21, Carla 19. ¿Quién obtuvo el mayor puntaje?",
          ["Comparo los números.", "21 es el mayor.", "Corresponde a Beto."], "Beto"),
    ],
    mistakes=[
        M("Pensar que un premio es justo aunque nadie conozca las reglas.", "Las reglas deben conocerse antes.", "Pide las bases."),
        M("Creer que quien no ganó no se esforzó.", "Un puntaje no muestra todo el esfuerzo.", "Reconoce el esfuerzo aunque no gane."),
    ],
    tiers=tiers(
        [E("El documento que explica las reglas de un premio, ¿son las bases o el diploma?", "Las bases", "El diploma es el reconocimiento."),
         E("Un número que mide el desempeño, ¿es un puntaje o una base?", "Un puntaje", "Es el número que se compara."),
         E("Dar un premio, ¿es otorgar o evaluar?", "Otorgar", "Evaluar es medir.")],
        [E("¿Qué datos conviene preguntar sobre un premio?", "Quién lo otorga, qué criterios usa y si son iguales para todos", "Así se juzga si es justo."),
         E("¿Por qué las reglas de un premio deben conocerse antes?", "Para que todos puedan prepararse en igualdad de condiciones", "Evita sorpresas e injusticias."),
         E("¿Qué no explica una tabla de puntajes?", "Las razones personales o las oportunidades de cada participante", "Solo muestra números.")],
        [E("Bases de ejemplo: «Gana el estudiante con más puntos en tres pruebas». Puntos de ejemplo: Luis 15, Mía 17, Ro 16. ¿Quién ganó?", "Mía", "17 es el mayor puntaje."),
         arith("Puntos de Lía en tres pruebas: 6, 7 y 5. ¿Cuántos puntos sumó?", "6+7+5", "Se suman los puntos de las tres pruebas."),
         E("Un diploma dice «Entregado por la directora por ayudar a compañeros». ¿Quién lo otorga?", "La directora", "El texto lo dice.")],
        [E("Marcos dice: «Si no ganó, no se esforzó». ¿Qué error tiene?", "El resultado no muestra todo el esfuerzo", "Alguien puede esforzarse y no ganar."),
         E("Un premio cambia sus reglas el día de la competencia sin avisar. ¿Es justo? Responde sí o no.", "No", "Las reglas deben conocerse antes.")],
        [E("Ordena los pasos al leer unas bases: A) ver si las reglas valen para todos, B) leer quién otorga el premio, C) identificar los criterios.", "B, C, A", "Primero la procedencia, luego los criterios y después si son iguales."),
         arith("Tabla de ejemplo: Ana 18, Beto 21, Carla 19. ¿Cuántos puntos menos que Beto tiene Ana?", "21-18", "Se resta el puntaje de Ana al de Beto.")],
    ),
    context=[E("En un campeonato escolar de ejemplo, las bases dicen que solo participan estudiantes de 5.º básico. Un niño de 3.º reclama. ¿Dónde se puede comprobar esa regla: en las bases o en un rumor?", "En las bases", "Allí están escritas las reglas.")],
    selfcheck=[E("¿Qué son las bases de un premio?", "El documento que explica las reglas", "Es la definición de la clase."), E("¿Qué hace justo a un reconocimiento?", "Reglas conocidas y aplicadas igual a todos", "Esa es la idea central."), E("¿Un puntaje muestra todo el esfuerzo?", "No", "Solo muestra un resultado.")],
    open_task=task("Lee estas bases de ejemplo: «Premio al esfuerzo: se entrega al estudiante que más puntos suba entre la primera y la segunda prueba de lectura». Datos: Rosa pasó de 50 a 58 puntos; Pedro de 60 a 64. Escribe quién cumple mejor el criterio, cuántos puntos subió cada uno y una pregunta sobre las reglas que te haría falta responder antes de dar el premio.", "Rosa subió 8 puntos y Pedro 4. Cumple mejor Rosa. Pregunta: ¿qué pasa si hay un empate?", ["identifica el criterio", "compara con datos", "formula una pregunta sobre las reglas"], ["tres frases escritas"], ["decidir sin usar el criterio", "olvidar la pregunta"], "Pide a una persona que diga si las bases son claras y qué cambiaría."),
    reinforce="Busca el nombre de un premio o campeonato que conozcas y escribe quién lo organiza.",
    extend="Escribe una regla para que un premio de tu curso sea justo.",
)

register(
    OA15, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar el esfuerzo con los logros y a reconocer que otros factores también influyen. Sirve para valorar el esfuerzo sin pensar que todo depende de una sola cosa.",
    prior=["Sé que hay logros que dependen del esfuerzo.", "Sé leer las reglas de un premio."],
    explain=[
        "El esfuerzo es una de las causas de un logro. Estudiar todos los días ayuda a mejorar una nota. Entrenar con constancia ayuda a mejorar en un deporte. Pero el esfuerzo no es la única causa: también influyen el apoyo de la familia, la ayuda de profesores, las oportunidades, la salud y los materiales disponibles.",
        "Los actores que influyen en un logro son la persona, su familia, sus compañeros, sus profesores y la comunidad. Las consecuencias de reconocer un logro son buenas: la persona se motiva y otros aprenden. Pero si solo premiamos el resultado, pueden aparecer la envidia o la presión excesiva.",
        "Por eso conviene reconocer también el esfuerzo y los avances, no solo el primer lugar. Un reconocimiento bien dado ayuda a seguir mejorando y no humilla a quienes aún no lo logran.",
    ],
    vocab=[("constancia", "seguir haciendo algo cada día aunque cueste"), ("oportunidad", "momento o condición que permite lograr algo"), ("avance", "mejora que se logra respecto de antes"), ("motivación", "ganas de seguir esforzándose"), ("presión", "sentir que se debe lograr algo sí o sí")],
    worked=[
        W("Esfuerzo y otras causas", "Una niña entrenó todos los días y ganó una carrera. Sus vecinos le prestaron una pista. ¿Qué causas influyeron?",
          ["Su esfuerzo y constancia.", "La oportunidad de usar una pista.", "Ambas causas influyeron."], "Su esfuerzo y la oportunidad de la pista"),
        W("Consecuencias de reconocer", "Un curso aplaude los avances de un compañero que mejoró en lectura. ¿Qué consecuencia positiva tiene?",
          ["Reconocen su avance.", "Él se siente motivado.", "Otros aprenden que mejorar vale."], "El compañero se motiva y otros aprenden"),
    ],
    mistakes=[
        M("Pensar que el logro depende solo del esfuerzo de la persona.", "También influyen el apoyo y las oportunidades.", "Reconoce todos los factores."),
        M("Premiar solo al primer lugar.", "Puede desanimar a quienes mejoran mucho.", "Reconoce también los avances."),
    ],
    tiers=tiers(
        [E("Seguir haciendo algo cada día aunque cueste, ¿es constancia o presión?", "Constancia", "La presión es sentir que hay que lograrlo sí o sí."),
         E("Una mejora respecto de antes, ¿es un avance o una oportunidad?", "Un avance", "Es la mejora que se logra."),
         E("Las ganas de seguir esforzándose, ¿son motivación o envidia?", "Motivación", "Son las ganas de seguir.")],
        [E("¿Por qué el esfuerzo no es la única causa de un logro?", "Porque también influyen el apoyo, las oportunidades y otros factores", "El contexto también cuenta."),
         E("¿Qué consecuencia buena tiene reconocer un logro?", "La persona se motiva y otros aprenden", "El reconocimiento anima."),
         E("¿Qué problema puede aparecer si solo se premia el primer lugar?", "Envidia o presión excesiva", "Puede desanimar a otros.")],
        [E("Un estudiante pasó de nota 4 a nota 6 en una prueba. Otro sacó 6 en las dos pruebas. ¿A quién conviene reconocer también por su avance?", "Al que pasó de 4 a 6", "Mejoró dos notas."),
         E("Una familia ayuda a su hijo a estudiar y su profesora le explica dudas. Aprobó con nota 6. ¿Qué actores apoyaron su logro además de él?", "La familia y la profesora", "Colaboraron en su aprendizaje."),
         arith("Mara entrenó 3 horas por semana durante 4 semanas. ¿Cuántas horas entrenó en total?", "3*4", "Se multiplican las horas por semana por las semanas.")],
        [E("Nico dice: «Si no gané es porque no me esfuerzo». ¿Qué factor olvida?", "Las oportunidades y el apoyo también influyen", "El esfuerzo no explica todo."),
         E("Un curso se ríe de quien sacó la nota más baja. ¿Ayuda eso a que mejore? Responde sí o no y explica.", "No; lo desanima", "El reconocimiento y el respeto ayudan más.")],
        [E("Ordena la cadena: A) mejora su nota, B) estudia a diario con ayuda de su familia, C) recibe un reconocimiento por su avance.", "B, A, C", "Primero estudia, luego mejora y luego se reconoce."),
         E("Tres estudiantes suben sus puntos en una prueba: Ana 3, Pía 5 y Gil 2. ¿Quién avanzó más?", "Pía", "5 es el mayor aumento.")],
    ),
    context=[E("En un colegio un niño que tuvo una enfermedad faltó un mes y luego estudió mucho, subiendo su nota de 4 a 5. El curso lo aplaude. ¿Qué reconocen: su avance o solo un primer lugar?", "Su avance", "Su nota mejoró aunque no fue la más alta.")],
    selfcheck=[E("¿Qué es la constancia?", "Seguir haciendo algo cada día aunque cueste", "Es la definición de la clase."), E("¿Solo el esfuerzo causa los logros?", "No", "Influyen otros factores."), E("¿Qué conviene reconocer además del primer lugar?", "Los avances", "Motiva a más personas.")],
    open_task=task("Caso de ejemplo: Sofía llegó a la final del campeonato de atletismo del colegio. Entrenó 5 días por semana, su abuelo la acompañó, el colegio le prestó la cancha y quedó en tercer lugar. Escribe los factores que influyeron en su logro, una consecuencia positiva de reconocerla y una forma de reconocer también a quien no llegó a la final.", "Factores: entrenamiento, apoyo del abuelo, cancha del colegio. Consecuencia: motiva. Reconocimiento: aplaudir avances de todos.", ["nombra al menos tres factores", "indica una consecuencia positiva", "propone reconocer a otros"], ["tres frases escritas"], ["decir que solo influyó su esfuerzo", "ignorar a los demás"], "Pide a una persona que diga qué factor le parece más importante y por qué."),
    reinforce="Escribe una persona que te apoyó en un logro y cómo lo hizo.",
    extend="Escribe cómo un curso puede reconocer a quienes mejoran aunque no sean los primeros.",
)

register(
    OA15, 4,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a comparar las perspectivas de quienes ganan, de quienes no ganan y de quienes juzgan un reconocimiento. Sirve para competir y premiar con respeto.",
    prior=["Sé que el mérito depende del esfuerzo y de las reglas.", "Sé que también influyen el apoyo y las oportunidades."],
    explain=[
        "En un reconocimiento participan varias personas con miradas distintas. Quien gana se siente orgulloso y puede agradecer a quienes lo ayudaron. Quien no gana puede sentirse triste, pero también puede aprender y felicitar al ganador. Quien evalúa debe aplicar las reglas con justicia. Los compañeros que observan pueden aplaudir o burlarse.",
        "Una competencia sana respeta las reglas, reconoce al ganador y valora el esfuerzo de todos. El liderazgo también es un mérito: un buen líder escucha, reparte tareas y ayuda a que el grupo logre metas. Un líder no es quien manda más fuerte.",
        "También se puede comparar entre lugares: dos escuelas pueden premiar de formas distintas según su historia y sus recursos. Lo importante es que los criterios sean claros, iguales para todos y respeten la dignidad de las personas.",
    ],
    vocab=[("competencia sana", "competir respetando reglas y a las demás personas"), ("liderazgo", "capacidad de guiar a un grupo para lograr algo"), ("dignidad", "valor que tiene toda persona y que debe respetarse"), ("empatía", "ponerse en el lugar de otra persona"), ("felicitar", "decir a alguien que lo hizo bien")],
    worked=[
        W("Varias perspectivas", "En una carrera, Ana ganó y Beto quedó último. ¿Qué actitud respeta a ambos?",
          ["Ana puede agradecer a quienes la apoyaron.", "Beto puede felicitarla y seguir practicando.", "El curso puede aplaudir a los dos."], "Felicitar a la ganadora y reconocer el esfuerzo de Beto"),
        W("Líder verdadero", "Un estudiante manda a todos con gritos y un compañero pregunta qué piensa cada uno. ¿Quién muestra liderazgo?",
          ["El liderazgo escucha y ayuda al grupo.", "El primero solo manda.", "El segundo es el líder."], "El que pregunta qué piensa cada uno"),
    ],
    mistakes=[
        M("Pensar que ser líder es mandar a los demás.", "El líder escucha y ayuda a todos.", "Observa si el grupo logra la meta unido."),
        M("Burlarse de quien perdió.", "Daña su dignidad.", "Felicita al ganador y respeta a todos."),
    ],
    tiers=tiers(
        [E("Competir respetando reglas y personas, ¿es una competencia sana o una pelea?", "Una competencia sana", "Respeta a todos."),
         E("Ponerse en el lugar de otra persona, ¿es empatía o presión?", "Empatía", "Permite comprender cómo se siente."),
         E("Decir a alguien que lo hizo bien, ¿es felicitar o ignorar?", "Felicitar", "Reconoce su logro.")],
        [E("¿Qué hace un buen líder?", "Escucha, reparte tareas y ayuda al grupo a lograr metas", "No solo manda."),
         E("¿Por qué no hay que burlarse de quien perdió?", "Porque daña su dignidad", "Todas las personas merecen respeto."),
         E("¿Qué puede hacer quien no gana para aprender?", "Felicitar al ganador y seguir practicando", "Así valora el esfuerzo.")],
        [E("Un juez aplica las reglas distinto a dos equipos. ¿Es justo? Responde sí o no.", "No", "Debe aplicarlas igual a todos."),
         arith("Tras un partido, un equipo gana 3 a 1. ¿Cuántos goles más que el perdedor anotó?", "3-1", "Se resta los goles del perdedor a los del ganador."),
         E("Un curso elige como líder a quien escucha a todos y reparte tareas. ¿Qué valora: el mérito de liderar o solo la fuerza?", "El mérito de liderar", "Escucha y ayuda al grupo.")],
        [E("Dana dice: «Un buen líder siempre manda más fuerte que los demás». ¿Qué error tiene?", "El líder escucha y ayuda, no solo manda", "Liderar es guiar al grupo."),
         E("Una escuela con pocos materiales decide premiar el esfuerzo y la asistencia, y otra con muchos materiales premia solo los resultados. ¿Los criterios son iguales? Responde sí o no.", "No", "Cada una premia aspectos diferentes.")],
        [E("Ordena una competencia sana: A) felicitar al ganador, B) respetar las reglas durante el juego, C) reconocer el esfuerzo de todos.", "B, A, C", "Primero se juega con reglas, luego se felicita y después se reconoce a todos."),
         arith("En un curso de 32 estudiantes, 24 votan por Elena como líder y el resto por otro. ¿Cuántos votaron por el otro?", "32-24", "Se resta los votos de Elena al total.")],
    ),
    context=[E("En una competencia de lectura, Camila no ganó y se siente triste. Sus amigos le dicen que su avance fue enorme. ¿Qué valoran con eso: el esfuerzo o solo el primer lugar?", "El esfuerzo", "Reconocen su avance aunque no ganó.")],
    selfcheck=[E("¿Qué es una competencia sana?", "Competir respetando reglas y a las personas", "Es la definición de la clase."), E("¿Qué hace un líder?", "Escucha y ayuda al grupo", "Guía a todos."), E("¿Qué es la empatía?", "Ponerse en el lugar de otra persona", "Es la definición del vocabulario.")],
    open_task=task("Elige un caso: a) un campeonato de fútbol del curso; b) una feria de ciencias; c) la elección de la persona que presentará al curso en un acto. Escribe qué sentiría y haría quien gana, quien no gana y quien evalúa, y una regla para que todos se sientan respetados.", "Campeonato: ganador agradece, perdedor felicita, árbitro aplica reglas igual. Regla: nadie se burla de otros.", ["describe tres perspectivas", "propone una regla de respeto", "no juzga a ninguna persona"], ["tres frases y una regla"], ["burlarse del que perdió", "dar más derechos al ganador"], "Pide a una persona que diga si tu regla de respeto se puede cumplir."),
    reinforce="Escribe cómo felicitarías a alguien que ganó un premio que tú también querías.",
    extend="Escribe qué cualidades tiene un buen líder de curso.",
)

# ================================================================ OA 16
register(
    OA16, 1,
    materials="Este cuaderno y un lápiz. Las situaciones están escritas en los ejercicios.",
    use="Aprenderé qué son las actitudes cívicas y en qué lugares de mi vida diaria las puedo practicar: la casa, la escuela, el barrio y la comunidad. Sirve para saber cómo actuar bien con los demás.",
    prior=["Sé que los derechos traen deberes.", "Conozco normas de convivencia de mi curso."],
    explain=[
        "Una actitud cívica es una forma de actuar que ayuda a vivir bien con los demás y a cuidar lo que es de todos. Hay cuatro grupos de actitudes. Primero, actuar con honestidad y responsabilidad: cumplir acuerdos, respetar la autoría de la música y las películas y no copiar el trabajo de otro. Segundo, respetar a todas las personas: no discriminar y escuchar opiniones distintas.",
        "Tercero, contribuir a la buena convivencia: resolver los problemas de manera pacífica y ser empático. Cuarto, cuidar y valorar el patrimonio y el medioambiente: cuidar plazas, monumentos y tradiciones, y usar la energía con eficiencia.",
        "Estas actitudes se practican en distintos lugares y momentos: en casa al compartir tareas, en la sala al esperar el turno, en el barrio al cuidar la plaza y en el país al respetar las leyes. Ubicar dónde y cuándo ayuda a reconocer qué hacer en cada caso.",
    ],
    vocab=[("actitud cívica", "forma de actuar que ayuda a convivir y cuidar lo de todos"), ("honestidad", "decir y hacer lo verdadero, sin engañar"), ("autoría", "reconocer quién creó una obra"), ("patrimonio", "bienes y tradiciones heredados que queremos conservar"), ("medioambiente", "naturaleza y lugares que nos rodean")],
    worked=[
        W("Clasificar una actitud", "Una niña devuelve un lápiz que encontró. ¿A qué grupo de actitudes corresponde?",
          ["Devolver lo ajeno es actuar con verdad.", "Corresponde a honestidad y responsabilidad.", "Respeta la propiedad de otros."], "Honestidad y responsabilidad"),
        W("Ubicar el lugar", "Un grupo limpia una plaza del barrio. ¿Dónde se practica y qué se cuida?",
          ["Se practica en el barrio.", "Se cuida el espacio público y el medioambiente.", "Es una actitud cívica."], "En el barrio; cuida el espacio público y el medioambiente"),
    ],
    mistakes=[
        M("Pensar que las actitudes cívicas solo se practican en actos oficiales.", "Se practican todos los días.", "Busca ejemplos en tu casa, curso y barrio."),
        M("Creer que cuidar el medioambiente es tarea solo de otros.", "Cada persona puede contribuir.", "Elige una acción que puedas hacer."),
    ],
    tiers=tiers(
        [E("Una forma de actuar que ayuda a convivir y cuidar lo de todos, ¿es una actitud cívica o un juego?", "Una actitud cívica", "Es lo que se define en la clase."),
         E("Devolver un lápiz que no es tuyo, ¿es honestidad o desorden?", "Honestidad", "Es actuar con la verdad."),
         E("Reconocer quién creó una canción, ¿es respetar la autoría o el patrimonio?", "Respetar la autoría", "Se reconoce al creador.")],
        [E("Nombra los cuatro grupos de actitudes cívicas de la clase.", "Honestidad y responsabilidad, respeto, buena convivencia y cuidado del patrimonio y medioambiente", "Son los cuatro grupos de la clase."),
         E("¿Por qué las actitudes cívicas se practican todos los días?", "Porque convivimos siempre con otras personas", "Se aplican en casa, escuela y barrio."),
         E("¿Qué es el patrimonio?", "Bienes y tradiciones heredados que queremos conservar", "Es la definición del vocabulario.")],
        [E("Clasifica: a) esperar el turno para hablar; b) apagar la luz de una sala vacía; c) cumplir un acuerdo del curso. Grupos: respeto, cuidado del medioambiente, responsabilidad.", "a respeto; b cuidado del medioambiente; c responsabilidad", "Cada acción corresponde a un grupo."),
         E("Un niño ve a un compañero solo en el recreo y lo invita a jugar. ¿Qué actitud demuestra?", "Empatía y buena convivencia", "Se pone en el lugar del otro."),
         E("Un vecino riega con cuidado la plaza y no malgasta agua. ¿Qué cuida?", "El medioambiente", "Evita el gasto excesivo.")],
        [E("Valentín dice: «Las actitudes cívicas son solo para el 18 de septiembre». ¿Qué error tiene?", "Se practican todos los días", "Son parte de la vida diaria."),
         E("Un estudiante copia un trabajo de internet y lo entrega como suyo. ¿Qué actitud no cumple?", "La honestidad y el respeto a la autoría", "No reconoce quién lo escribió.")],
        [E("Ordena de más cercano a más amplio el lugar donde practicas actitudes: A) tu país, B) tu casa, C) tu barrio.", "B, C, A", "La casa es lo más cercano y el país lo más amplio."),
         arith("Un curso tiene 30 estudiantes y 24 cumplen el acuerdo de llegar a la hora. ¿Cuántos no lo cumplen?", "30-24", "Se resta los que cumplen al total.")],
    ),
    context=[E("En el recreo, un niño recoge un papel del suelo aunque él no lo tiró. ¿Qué grupo de actitudes ejerce: cuidado del patrimonio y medioambiente o respeto a opiniones distintas?", "Cuidado del patrimonio y medioambiente", "Cuida el espacio compartido.")],
    selfcheck=[E("¿Qué es una actitud cívica?", "Una forma de actuar que ayuda a convivir y cuidar lo de todos", "Es la definición de la clase."), E("Nombra una actitud de honestidad.", "Por ejemplo: devolver lo que no es mío", "Es actuar con verdad."), E("¿Dónde se practican las actitudes cívicas?", "En casa, escuela, barrio y país", "En todos lados.")],
    open_task=task("Haz una tabla con cuatro filas, una por cada grupo de actitudes (honestidad y responsabilidad, respeto, buena convivencia, cuidado del patrimonio y medioambiente). En cada fila escribe una acción que puedes hacer esta semana y el lugar donde la harás.", "Respeto: escuchar a un compañero con otra opinión, en la sala. Medioambiente: apagar luces, en casa.", ["una acción por grupo", "indica el lugar", "las acciones son posibles de realizar"], ["tabla de cuatro filas"], ["escribir acciones que no se pueden cumplir", "repetir la misma acción"], "Pide a una persona que elija una acción y te recuerde hacerla esta semana."),
    reinforce="Anota una acción cívica que viste hacer a alguien hoy.",
    extend="Escribe qué cambia en tu curso cuando todos practican una actitud cívica.",
)

register(
    OA16, 2,
    materials="Este cuaderno y un lápiz. Los textos están escritos en los ejercicios.",
    use="Aprenderé a usar y citar fuentes con honestidad: no copiar, reconocer la autoría y respetar la música y las películas. Sirve para hacer trabajos propios y respetar el trabajo de otros.",
    prior=["Sé qué es una actitud cívica.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Toda obra tiene un autor: un texto, una canción, una película o un dibujo. Respetar la autoría significa reconocer quién la creó y no usarla como propia. El plagio es copiar el trabajo de otra persona y presentarlo como si fuera tuyo. Es una falta de honestidad que daña al autor y a quien copia, porque no aprende.",
        "Podemos usar la información de una fuente de forma honesta. Si copiamos palabras exactas, las ponemos entre comillas y decimos de dónde vienen. Si la explicamos con nuestras palabras, también anotamos la fuente. Para citar basta decir el autor o el título, y el lugar donde lo leímos.",
        "Respetar la autoría de la música y las películas significa usarlas por canales permitidos y no copiarlas ni repartirlas sin permiso del creador. Así quienes crean pueden vivir de su trabajo.",
    ],
    vocab=[("autor", "persona que crea una obra"), ("plagio", "copiar el trabajo de otra persona y decir que es propio"), ("cita", "palabras de otra persona, escritas entre comillas con su fuente"), ("parafrasear", "explicar con tus palabras lo que dice una fuente"), ("fuente", "lugar de donde se saca información")],
    worked=[
        W("Citar con comillas", "Copias una frase exacta de un libro de Historia. ¿Cómo la usas honestamente?",
          ["Ponerla entre comillas.", "Decir el libro o autor.", "Así reconoces la fuente."], "Entre comillas y con la fuente"),
        W("Parafrasear", "El texto dice «La plaza se construyó para reunir a la comunidad». Escribes: «Se hizo para que los vecinos se encontraran». ¿Qué hiciste?",
          ["Cambié las palabras pero dije lo mismo.", "Eso es parafrasear.", "Aun así debo anotar la fuente."], "Parafrasear; hay que anotar la fuente"),
    ],
    mistakes=[
        M("Pensar que si cambias un par de palabras ya no es plagio.", "Sigue siendo la idea de otro sin reconocerla.", "Cita siempre la fuente."),
        M("Creer que copiar una canción o película no daña a nadie.", "Los autores viven de su trabajo.", "Usa canales permitidos."),
    ],
    tiers=tiers(
        [E("Copiar el trabajo de otro y decir que es tuyo, ¿es plagio o cita?", "Plagio", "Cita es reconocer la fuente."),
         E("Quien crea una obra, ¿es el autor o el plagiador?", "El autor", "Es quien la crea."),
         E("Explicar con tus palabras lo que dice una fuente, ¿es parafrasear o copiar?", "Parafrasear", "Cambias las palabras manteniendo la idea.")],
        [E("¿Por qué el plagio es una falta de honestidad?", "Porque presenta como propio el trabajo de otro", "Engaña sobre quién hizo la obra."),
         E("¿Cómo se usan palabras exactas de una fuente?", "Entre comillas y diciendo de dónde son", "Así se reconoce al autor."),
         E("¿Por qué respetar la autoría de canciones y películas?", "Para que los creadores puedan vivir de su trabajo", "Es su trabajo.")],
        [E("Frase copiada de un texto: «El río es largo». Escribe cómo la citarías si el título es «Ríos de Chile».", "«El río es largo» (Ríos de Chile)", "Está entre comillas y con la fuente."),
         E("Un compañero entrega un trabajo con párrafos de internet, sin decir de dónde. ¿Cometió plagio? Responde sí o no.", "Sí", "No reconoció la fuente."),
         E("Un niño escucha música en un servicio permitido por el autor. ¿Respeta la autoría? Responde sí o no.", "Sí", "Usa un canal permitido.")],
        [E("Bruno dice: «Si cambio dos palabras ya no es plagio». ¿Qué error tiene?", "Sigue usando la idea de otro sin reconocerla", "Hay que citar la fuente."),
         E("Una niña quiere repartir una película a todo el curso copiándola sin permiso. ¿Qué actitud no respeta?", "La autoría", "El creador no autorizó la copia.")],
        [E("Ordena los pasos para usar una fuente: A) escribir tu texto con tus palabras, B) leer la fuente, C) anotar de dónde sacaste la idea.", "B, A, C", "Primero se lee, luego se redacta y se anota la fuente."),
         arith("Un trabajo tiene 5 párrafos y 2 son copiados sin citar. ¿Cuántos párrafos son propios?", "5-2", "Se resta los copiados al total.")],
    ),
    context=[E("Una estudiante debe presentar un trabajo sobre un monumento y encuentra un texto largo. ¿Qué es más honesto: copiar el texto completo o leerlo y escribir con sus palabras anotando la fuente?", "Leerlo y escribir con sus palabras anotando la fuente", "Respeta la autoría y demuestra que aprendió.")],
    selfcheck=[E("¿Qué es el plagio?", "Copiar el trabajo de otro y decir que es propio", "Es la definición de la clase."), E("¿Cómo se usan palabras exactas de otro?", "Entre comillas y con la fuente", "Así se cita."), E("¿Por qué respetar la autoría?", "Porque reconoce y protege el trabajo del creador", "Es honesto y justo.")],
    open_task=task("Lee este texto de ejemplo: «El faro de la costa guía a los barcos de noche con su luz». Escribe una cita textual con comillas y fuente (el título es «Faros de Chile»), una versión con tus palabras y una frase que explique por qué es importante anotar la fuente.", "Cita: «El faro de la costa guía a los barcos de noche con su luz» (Faros de Chile). Mis palabras: el faro ilumina para orientar a los barcos. Importante: reconoce al autor.", ["cita con comillas y fuente", "parafrasea con otras palabras", "explica la importancia de anotar la fuente"], ["tres frases escritas"], ["copiar sin comillas", "olvidar la fuente"], "Pide a una persona que compare tu versión con el texto original."),
    reinforce="Busca un libro de tu casa y anota su título y su autor.",
    extend="Escribe qué harías si ves a un compañero copiando un trabajo.",
)

register(
    OA16, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar el respeto y la empatía con sus consecuencias en la convivencia y a resolver conflictos de manera pacífica. Sirve para convivir mejor.",
    prior=["Sé qué son las actitudes cívicas.", "Sé que discriminar daña a las personas."],
    explain=[
        "Respetar a todas las personas significa no discriminar por condiciones físicas, sociales, culturales o étnicas, escuchar con respeto opiniones distintas y respetar los espacios y las cosas de los demás. Cuando hay respeto, hay confianza y se puede trabajar mejor. Cuando hay discriminación o burla, aparecen miedo, aislamiento y peleas.",
        "Los conflictos son parte de la vida. Se pueden resolver de manera pacífica con estos pasos: calmarse, escuchar a cada parte, decir cómo se siente cada uno sin insultar, proponer soluciones y elegir una que ambos acepten. La empatía ayuda porque permite entender lo que siente el otro. Si hay peligro o golpes, no se intenta resolver solo: se pide ayuda de inmediato a un adulto.",
        "Los actores de un conflicto son las personas involucradas, quienes miran y los adultos que ayudan. Cada uno puede empeorar o mejorar la situación. Las consecuencias de resolver pacíficamente son que se repara la relación y se aprende. Las de resolver con violencia son daño y más conflicto.",
    ],
    vocab=[("empatía", "ponerse en el lugar de otra persona"), ("conflicto", "desacuerdo entre personas"), ("mediar", "ayudar a que dos personas lleguen a un acuerdo"), ("acuerdo", "solución que ambas partes aceptan"), ("violencia", "uso de la fuerza o de insultos para dañar")],
    worked=[
        W("Pasos para resolver", "Dos niños discuten por un balón. ¿Cuál es un primer paso para resolver pacíficamente?",
          ["Primero deben calmarse.", "Luego escuchar a cada uno.", "Después proponer soluciones."], "Calmarse"),
        W("Empatía en acción", "Un niño no entiende un juego porque llegó recién al curso. Un compañero le explica con paciencia. ¿Qué actitud muestra?",
          ["Se pone en el lugar del nuevo.", "Lo ayuda a participar.", "Es empatía y respeto."], "Empatía y respeto"),
    ],
    mistakes=[
        M("Resolver un problema gritando o con golpes.", "Aumenta el daño y no soluciona.", "Calmarse y dialogar."),
        M("Pensar que respetar es estar siempre de acuerdo.", "Se puede discrepar con respeto.", "Escucha y explica tu opinión sin insultar."),
    ],
    tiers=tiers(
        [E("Ponerse en el lugar de otro, ¿es empatía o rivalidad?", "Empatía", "Permite entender al otro."),
         E("Un desacuerdo entre personas, ¿es un conflicto o un acuerdo?", "Un conflicto", "El acuerdo es la solución."),
         E("Usar la fuerza o insultos para dañar, ¿es violencia o mediación?", "Violencia", "Mediar es ayudar a acordar.")],
        [E("¿Por qué conviene calmarse antes de hablar en un conflicto?", "Para poder escuchar y no insultar", "Con calma se piensa mejor."),
         E("¿Qué consecuencia tiene resolver pacíficamente un conflicto?", "Se repara la relación y se aprende", "Se evita más daño."),
         E("¿Qué es mediar?", "Ayudar a que dos personas lleguen a un acuerdo", "Es la definición del vocabulario.")],
        [E("Dos amigas quieren el mismo asiento. Una propone turnarse cada día. ¿Qué paso del proceso hizo: proponer una solución o gritar?", "Proponer una solución", "Ofreció un acuerdo posible."),
         E("Un niño insulta a otro por su manera de hablar. ¿Qué actitud no cumple: respetar a todas las personas o cuidar el medioambiente?", "Respetar a todas las personas", "Discriminó por su manera de hablar."),
         E("Un compañero rompió sin querer tu dibujo y te pide perdón. ¿Qué respuesta es pacífica: aceptar sus disculpas y proponer hacer otro dibujo juntos, o romper algo suyo para quedar a mano?", "Aceptar sus disculpas y proponer hacer otro dibujo juntos", "Repara la relación y no agrega más daño.")],
        [E("Fabián dice: «Si no pienso como tú, no debo escucharte». ¿Qué error tiene?", "Respetar es escuchar opiniones distintas", "Se puede discrepar con respeto."),
         E("Dos compañeros resuelven un problema golpeándose. ¿Se arregló el conflicto? Responde sí o no.", "No", "La violencia solo aumenta el daño.")],
        [E("Ordena los pasos de una solución pacífica: A) elegir un acuerdo, B) calmarse, C) escuchar a cada uno.", "B, C, A", "Primero calma, luego escuchar y al final acordar."),
         E("Una profesora ayuda a dos estudiantes a llegar a un acuerdo sin tomar partido por ninguno. ¿Qué hace: mediar o castigar?", "Mediar", "Mediar es ayudar a que dos personas lleguen a un acuerdo.")],
    ),
    context=[E("Dos estudiantes pelean porque uno rompió sin querer el dibujo del otro. ¿Qué paso conviene primero: calmarse o castigar a todos?", "Calmarse", "Así pueden escucharse.")],
    selfcheck=[E("¿Qué es la empatía?", "Ponerse en el lugar de otra persona", "Es la definición de la clase."), E("¿Cuál es el primer paso para resolver un conflicto?", "Calmarse", "Permite pensar y escuchar."), E("¿La violencia soluciona los conflictos?", "No", "Aumenta el daño.")],
    open_task=task("Caso de ejemplo: dos compañeros se pelean porque uno dice que el otro nunca comparte los materiales del grupo. Escribe los cinco pasos para resolverlo pacíficamente, aplicados al caso, y una frase empática que diría cada uno.", "Pasos: calmarse, escuchar, decir cómo se sienten, proponer turnos y acordar. Frase: entiendo que te enojaste porque no compartí.", ["cinco pasos aplicados al caso", "frase empática para cada uno", "sin insultos ni culpas"], ["lista de pasos y dos frases"], ["omitir escuchar", "usar frases que insulten"], "Pide a una persona que represente a un compañero y practica tus frases."),
    reinforce="Escribe una frase empática para decirle a alguien que está molesto.",
    extend="Escribe cómo ayudarías a dos compañeros a acordar un turno para usar un juego.",
)

register(
    OA16, 4,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a comparar perspectivas distintas sobre un mismo hecho y a respetarlas sin discriminar. Sirve para escuchar opiniones diferentes y buscar acuerdos.",
    prior=["Sé resolver conflictos de manera pacífica.", "Sé qué es la empatía."],
    explain=[
        "Dos personas pueden ver un mismo hecho de forma distinta. Una niña de la ciudad y un niño del campo pueden valorar de manera diferente el uso de un terreno: ella ve una plaza para jugar; él, un lugar para cultivar. Cada perspectiva responde a su experiencia y a sus necesidades.",
        "Respetar opiniones distintas no significa estar de acuerdo con todo. Significa escuchar sin burlarse, preguntar para entender, decir la propia opinión con respeto y buscar un acuerdo si hay que decidir juntos. Discriminar es tratar peor a alguien por su condición física, social, cultural o étnica.",
        "Comparar perspectivas también puede hacerse entre territorios y culturas: cada comunidad tiene tradiciones propias, como comidas, fiestas y formas de hablar. Valorarlas enriquece la convivencia y es parte del respeto al patrimonio cultural.",
    ],
    vocab=[("perspectiva", "mirada de una persona según su experiencia"), ("discriminar", "tratar peor a alguien por una característica suya"), ("cultura", "formas de vivir, hablar, comer y celebrar de un grupo"), ("tradición", "costumbre que se transmite de generación en generación"), ("opinión", "lo que una persona piensa sobre algo")],
    worked=[
        W("Dos perspectivas", "Un grupo quiere usar una cancha para fútbol y otro para vóleibol. ¿Cómo se respeta a ambos?",
          ["Escucho a cada grupo.", "Propongo turnos por día.", "Ambos usan la cancha."], "Con turnos acordados"),
        W("Cultura distinta", "Un niño de otra región cuenta que en su pueblo celebran una fiesta con comidas típicas. ¿Qué actitud es respetuosa?",
          ["Escuchar con interés.", "Preguntar sin burlarse.", "Valorar su cultura."], "Escuchar con interés y sin burlarse"),
    ],
    mistakes=[
        M("Burlarse de una costumbre distinta a la propia.", "Discrimina y daña a la persona.", "Pregunta y aprende."),
        M("Pensar que respetar una opinión es obligación de cambiar la propia.", "Respetar no es estar de acuerdo.", "Escucha y expresa tu opinión con respeto."),
    ],
    tiers=tiers(
        [E("Lo que una persona piensa sobre algo, ¿es una opinión o una tradición?", "Una opinión", "Una tradición es una costumbre."),
         E("Tratar peor a alguien por una característica suya, ¿es discriminar o compartir?", "Discriminar", "Es un trato injusto."),
         E("Una costumbre que se transmite de generación en generación, ¿es una tradición o un conflicto?", "Una tradición", "Se hereda de generaciones anteriores.")],
        [E("¿Por qué dos personas pueden ver distinto un mismo hecho?", "Porque tienen experiencias y necesidades distintas", "Eso es una perspectiva."),
         E("¿Respetar una opinión distinta significa estar de acuerdo?", "No", "Significa escuchar con respeto."),
         E("¿Por qué valorar tradiciones distintas enriquece la convivencia?", "Porque aprendemos de otras formas de vivir", "Amplía nuestra comprensión.")],
        [E("Dos grupos opinan distinto sobre el tema de la fiesta del curso. ¿Qué conviene hacer: votar con respeto o imponer una opinión?", "Votar con respeto", "Permite decidir entre todos."),
         E("Un compañero habla con un acento distinto y otros se ríen. ¿Qué debería hacer el curso: escuchar con respeto o imitarlo?", "Escuchar con respeto", "Imitar es burla."),
         arith("En un curso de 30 estudiantes, 18 prefieren una actividad y 12 otra. ¿Cuántos estudiantes más prefieren la primera?", "18-12", "Se resta los votos de la segunda a los de la primera.")],
        [E("Isabel dice: «Mi opinión es la única válida». ¿Qué error tiene?", "Hay otras perspectivas que también merecen ser escuchadas", "Cada persona tiene su mirada."),
         E("Un grupo excluye a un compañero porque su familia cocina platos distintos. ¿Es discriminación? Responde sí o no.", "Sí", "Lo trata peor por su cultura.")],
        [E("Ordena los pasos para compartir una opinión distinta: A) explicar con respeto tu opinión, B) escuchar la otra opinión, C) buscar un acuerdo.", "B, A, C", "Primero escuchas, luego dices tu opinión y luego buscas acuerdo."),
         arith("Dos propuestas de actividad: A tiene 12 votos y B tiene 9 votos. ¿Cuántos votos hubo en total?", "12+9", "Se suman los votos de ambas propuestas.")],
    ),
    context=[E("En una comunidad, a un grupo le gusta una fiesta con música y a otro le gusta más tranquila. ¿Qué solución respeta a ambos: alternar los años o que solo se haga una de ellas?", "Alternar los años", "Se respeta a las dos preferencias.")],
    selfcheck=[E("¿Qué es una perspectiva?", "La mirada de una persona según su experiencia", "Es la definición de la clase."), E("¿Qué es discriminar?", "Tratar peor a alguien por una característica suya", "Es la definición del vocabulario."), E("¿Respetar es estar de acuerdo siempre?", "No", "Es escuchar con respeto.")],
    open_task=task("Caso de ejemplo: un curso debe decidir entre una excursión a un museo y una salida a un parque. Escribe dos perspectivas posibles, cómo escuchar a cada una con respeto y un acuerdo que podría aceptar la mayoría.", "Perspectivas: unos quieren aprender de historia, otros jugar al aire libre. Acuerdo: museo este mes, parque el próximo.", ["dos perspectivas distintas", "cómo escuchar con respeto", "un acuerdo posible"], ["tres frases escritas"], ["decidir sin escuchar", "burlarse de una opción"], "Pide a una persona que diga si tu acuerdo tomó en cuenta a las dos partes."),
    reinforce="Pregunta a alguien de tu casa por una tradición familiar y anótala.",
    extend="Escribe cómo reaccionarías si alguien se burla de una tradición que no conoces.",
)

register(
    OA16, 5,
    materials="Este cuaderno y un lápiz. Los datos están escritos en los ejercicios.",
    use="Aprenderé a argumentar con evidencia por qué cuidar el patrimonio y usar la energía con eficiencia, y a diseñar una campaña simple. Sirve para convencer a otros con razones.",
    prior=["Sé que cuidar el patrimonio y el medioambiente es una actitud cívica.", "Sé argumentar con afirmación, evidencia y razón."],
    explain=[
        "El patrimonio es lo que heredamos y queremos conservar: monumentos, plazas, edificios antiguos, fiestas y tradiciones. Cuidarlo permite que las próximas generaciones lo conozcan. El medioambiente también se cuida: usar la energía con eficiencia significa lograr lo mismo gastando menos, por ejemplo apagando luces que no se usan.",
        "Para convencer a otros de cuidar algo, hacemos una campaña de información. Una campaña tiene un mensaje claro, datos que lo apoyan y una acción concreta que se pide. Por ejemplo: «Apaga la luz al salir de la sala». Evidencia: una sala con 8 luces encendidas 6 horas gasta más luz que una con 8 luces encendidas 4 horas.",
        "El argumento mejora si se miden resultados antes y después. Si tras la campaña disminuye el gasto, la evidencia apoya la afirmación. Se debe indicar también hasta dónde llega el dato: un solo mes no prueba lo que pasa todo el año.",
    ],
    vocab=[("campaña", "conjunto de acciones para informar y convencer sobre un tema"), ("eficiencia", "lograr lo mismo gastando menos"), ("generación", "grupo de personas que nacen en la misma época"), ("conservar", "cuidar algo para que dure"), ("gasto", "cantidad de energía, agua o dinero que se usa")],
    worked=[
        W("Evidencia en una campaña", "Una sala tenía 8 luces encendidas durante 6 horas y después de la campaña 8 luces durante 4 horas. ¿Qué ahorro hay por luz?",
          ["Comparo 6 con 4 horas.", "Hay 2 horas menos por luz.", "Es el ahorro."], "2 horas menos por luz"),
        W("Mensaje claro", "¿Cuál mensaje es mejor: «Cuidemos» o «Apaga la luz al salir de la sala»? ¿Por qué?",
          ["El segundo dice la acción concreta.", "El primero es muy general.", "Una campaña necesita una acción clara."], "El segundo; tiene una acción concreta"),
    ],
    mistakes=[
        M("Hacer una campaña sin datos ni acción concreta.", "No convence ni ayuda a cambiar.", "Incluye evidencia y una acción pedida."),
        M("Generalizar con un solo dato.", "Un mes no prueba todo el año.", "Indica el límite del dato."),
    ],
    tiers=tiers(
        [E("Lograr lo mismo gastando menos, ¿es eficiencia o gasto excesivo?", "Eficiencia", "El gasto excesivo es lo contrario."),
         E("Cuidar algo para que dure, ¿es conservar o botar?", "Conservar", "Botar es lo contrario."),
         E("Un conjunto de acciones para informar y convencer sobre un tema, ¿es una campaña o una nota?", "Una campaña", "Informa y convence.")],
        [E("¿Por qué es importante cuidar el patrimonio para las próximas generaciones?", "Para que también puedan conocerlo", "Lo heredan las próximas generaciones."),
         E("¿Qué partes tiene una buena campaña?", "Un mensaje claro, datos que lo apoyan y una acción concreta", "Así la campaña convence."),
         E("¿Por qué conviene medir antes y después de una campaña?", "Para saber si el gasto realmente bajó", "Es la evidencia del resultado.")],
        [arith("Una sala tiene 8 luces encendidas 6 horas al día. ¿Cuántas horas de luz encendida se gastan por día en total antes de la campaña?", "8*6", "Se multiplican las luces por las horas.", " horas de luz encendida"),
         arith("Después de la campaña, la misma sala mantiene 8 luces encendidas 4 horas. ¿Cuántas horas de luz encendida se gastan por día?", "8*4", "Se multiplican las luces por las nuevas horas.", " horas de luz encendida"),
         arith("Una plaza antigua tiene 20 bancas y 5 están rayadas. ¿Cuántas están sin rayar?", "20-5", "Se resta las rayadas al total.")],
        [E("Tomás dice: «Cuidar el patrimonio no sirve». ¿Qué argumento le darías?", "Que permite que otras generaciones lo conozcan y valoren", "El patrimonio se hereda."),
         E("Un curso ahorró luz un solo mes y afirma que ahorrará lo mismo todo el año. ¿Qué límite olvida?", "Un mes no prueba lo que pasa todo el año", "Falta más evidencia.")],
        [E("Afirmación: «Apagar luces ahorra energía». ¿Qué evidencia la apoya: «la sala usó 48 horas de luz encendida y bajó a 32» o «las luces son blancas»?", "«La sala usó 48 horas de luz encendida y bajó a 32»", "El dato habla del gasto."),
         arith("Con esos datos (de 48 a 32 horas de luz encendida), ¿cuántas horas de luz encendida se ahorraron?", "48-32", "Se resta el gasto nuevo al anterior.", " horas de luz encendida")],
    ),
    context=[arith("Un grupo organiza una campaña para limpiar una plaza antigua. Antes había 12 bolsas de basura por semana y después 5. ¿Cuántas bolsas menos hay por semana?", "12-5", "Se resta las bolsas de después a las de antes.", " bolsas")],
    selfcheck=[E("¿Qué es el patrimonio?", "Lo que heredamos y queremos conservar", "Es la definición de la clase."), E("¿Qué es la eficiencia?", "Lograr lo mismo gastando menos", "Es la definición del vocabulario."), E("¿Qué necesita una campaña?", "Mensaje claro, datos y una acción", "Así la campaña convence.")],
    open_task=task("Diseña una mini campaña para tu curso con uno de estos temas: a) apagar luces que no se usan; b) cuidar una plaza o edificio antiguo del barrio. Escribe el mensaje, un dato de ejemplo (por ejemplo, «8 luces encendidas 6 horas»), la acción que pides y qué medirías después.", "Mensaje: apaga la luz al salir. Dato: 8 luces, 6 horas. Acción: apagarlas en el recreo. Mediré las horas encendidas por semana.", ["mensaje claro", "dato que lo apoya", "acción concreta y forma de medir"], ["afiche escrito de cuatro líneas"], ["mensaje demasiado general", "no decir qué se medirá"], "Muestra tu mensaje a una persona y pídele que diga cuál acción haría."),
    reinforce="Anota tres luces o aparatos de tu casa que podrían apagarse cuando no se usan.",
    extend="Escribe cómo cuidarías un lugar patrimonial de tu zona.",
)
