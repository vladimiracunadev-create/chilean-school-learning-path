"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 13 (personas como sujetos de derecho) y OA 14 (derechos, deberes y responsabilidades del Estado)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA13, OA14 = "HI05 OA 13", "HI05 OA 14"
E = ex


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


# ================================================================ OA 13
register(
    OA13, 1,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé qué significa ser sujeto de derecho y desde cuándo el mundo reconoce que todas las personas tienen derechos. Sirve para reconocer cuándo algo es un derecho y no un favor.",
    prior=["Sé que en el curso y en la familia hay normas de convivencia.", "Sé que Chile es un país con leyes."],
    explain=[
        "Un derecho es algo que toda persona puede pedir y que los demás deben respetar, como ir a la escuela, ser cuidada cuando está enferma o expresar lo que piensa. Ser sujeto de derecho significa que las normas te reconocen derechos por ser persona, no por un favor de nadie.",
        "Los derechos no dependen de características individuales. No importa la etnia, el sexo, el lugar de nacimiento, si se tiene mucho o poco dinero o si se vive en la ciudad o en el campo. Todas las personas los tienen. Los deben respetar los pares, la comunidad y el Estado.",
        "Esta idea se fue afirmando en la historia. En 1948, después de una gran guerra mundial, las Naciones Unidas aprobaron la Declaración Universal de Derechos Humanos. En 1989 se aprobó una convención especial sobre los derechos de niños y niñas. Chile la firmó en 1990 y se comprometió a cumplirla. Saber desde cuándo y dónde existen estas normas ayuda a defenderlas.",
    ],
    vocab=[("derecho", "algo que toda persona puede pedir y que los demás deben respetar"), ("sujeto de derecho", "persona a quien las normas reconocen derechos"), ("par", "persona de tu misma edad o situación, como un compañero de curso"), ("Estado", "conjunto de instituciones que gobiernan y sirven a un país"), ("universal", "que vale para todas las personas")],
    worked=[
        W("Derecho o favor", "Un niño pide ir a la escuela y le dicen «te dejo ir si te portas muy bien». ¿Ir a la escuela es un derecho o un favor?",
          ["Pregunto si le corresponde a todos los niños.", "Sí, todos los niños tienen derecho a la educación.", "Por eso no es un favor sujeto a condiciones personales."], "Es un derecho"),
        W("Derechos y características", "Una niña dice que no tiene los mismos derechos que otros porque nació en otro país. ¿Es correcto?",
          ["Los derechos no dependen del lugar de nacimiento.", "Todas las personas son sujetos de derecho.", "No es correcto."], "No, los derechos no dependen del lugar de nacimiento"),
    ],
    mistakes=[
        M("Creer que los derechos se ganan portándose bien.", "Los derechos se tienen por ser persona.", "Diferencia los derechos de los premios por mérito."),
        M("Pensar que algunas personas tienen más derechos por su etnia o por ser hombre o mujer.", "Los derechos no dependen de esas características.", "Recuerda que son universales."),
    ],
    tiers=tiers(
        [E("Algo que toda persona puede pedir y que los demás deben respetar, ¿es un derecho o un premio?", "Un derecho", "Los premios dependen del mérito."),
         E("Los derechos, ¿valen para todas las personas o solo para algunas?", "Para todas las personas", "Los derechos son universales."),
         E("Un compañero de tu curso, ¿es un par o una autoridad del Estado?", "Un par", "Es una persona de tu misma situación.")],
        [E("Con tus palabras, ¿qué significa ser sujeto de derecho?", "Que las normas te reconocen derechos por ser persona", "No depende de favores."),
         E("¿Quiénes deben respetar los derechos de las personas?", "Los pares, la comunidad y el Estado", "Así lo dice la clase."),
         E("¿Por qué la Declaración Universal de Derechos Humanos se llama «universal»?", "Porque vale para todas las personas", "No excluye a nadie.")],
        [E("Un niño de otro país llega a una escuela de Chile. ¿Tiene derecho a ser tratado con respeto igual que sus compañeros?", "Sí", "El lugar de nacimiento no cambia los derechos."),
         E("Una niña de pueblo originario quiere participar en una actividad escolar y la excluyen por su origen. ¿Se respetó su derecho? Responde sí o no.", "No", "Los derechos no dependen de la etnia."),
         E("Un niño dice: «Mi derecho a la educación es un regalo de mi profesor». ¿Es verdadero o falso?", "Falso", "Es un derecho, no un regalo personal.")],
        [E("Mateo dice: «Las niñas tienen menos derechos que los niños». ¿Qué error tiene?", "Los derechos no dependen del sexo", "Todas las personas son sujetos de derecho."),
         E("Una escuela dice a un estudiante: «Tienes derecho a aprender solo si tienes buenas notas». ¿Está bien? Responde sí o no y explica.", "No; el derecho a aprender no depende de las notas", "Los derechos no dependen de características individuales.")],
        [E("Ordena de más antiguo a más nuevo: A) Convención sobre los derechos del niño, B) Declaración Universal de Derechos Humanos (1948).", "B, A", "La Declaración fue antes que la convención sobre la niñez."),
         E("Un niño dice que su derecho a ser escuchado depende de qué tan fuerte hable. ¿Por qué se equivoca?", "Porque es un derecho de toda persona, sin condiciones", "Los derechos no dependen de características individuales.")],
    ),
    context=[E("Un grupo de estudiantes no deja jugar a un compañero porque nació en otra región. ¿Qué derecho no se respeta: el de ser tratado con respeto o el de recibir un premio?", "El de ser tratado con respeto", "Todo niño merece respeto, sin importar de dónde viene.")],
    selfcheck=[E("¿Qué es un derecho?", "Algo que toda persona puede pedir y que otros deben respetar", "Es la definición de la clase."), E("¿Los derechos dependen de la etnia o del sexo?", "No", "Los derechos son universales."), E("¿Quiénes deben respetar los derechos?", "Pares, comunidad y Estado", "Es lo que dice la clase.")],
    open_task=task("Elige una de estas frases y explícala con tus palabras: a) «Todos los niños y niñas tienen derecho a ir a la escuela»; b) «Todos tienen derecho a ser escuchados»; c) «Todos tienen derecho a recibir atención de salud». Escribe quién debe respetar ese derecho y un ejemplo de tu vida donde se cumpla.", "Frase a: ir a la escuela es un derecho de todos. Lo respetan la familia, la escuela y el Estado. Ejemplo: en mi curso todos tienen su banco.", ["explica la frase con sus palabras", "nombra a quienes deben respetar el derecho", "da un ejemplo cercano"], ["párrafo de tres a cuatro frases"], ["confundir derecho con premio", "decir que el derecho depende de la persona"], "Pide a una persona que diga si tu ejemplo muestra un derecho y no un favor."),
    reinforce="Escribe un derecho que ya ejerces en tu vida diaria.",
    extend="Escribe qué podría hacer un curso para que ninguna persona sea excluida por su origen.",
)

register(
    OA13, 2,
    materials="Este cuaderno y un lápiz. Los textos están escritos en los ejercicios.",
    use="Aprenderé a leer textos sobre derechos y a preguntar quién los escribió y para qué. Sirve para distinguir una norma de una opinión.",
    prior=["Sé qué es un derecho y que es universal.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Hay fuentes distintas sobre los derechos. Una norma es una regla escrita que una autoridad aprobó, como un tratado internacional o una ley. Un afiche de una campaña explica un derecho para convencer a las personas. La opinión de un vecino dice lo que él piensa. Cada fuente sirve para algo diferente.",
        "Para leer una norma buscamos quién la aprobó, cuándo, a quiénes protege y qué dice exactamente. Un texto de una organización social puede defender un derecho, pero no es una ley. Una noticia cuenta un hecho y puede dar la versión de una sola de las partes.",
        "Al leer, separamos lo que la fuente afirma, lo que nosotros entendemos y lo que falta saber. Si un afiche dice «todos los niños tienen derecho a jugar», entendemos que es un mensaje que protege a la niñez, pero para ver qué exige la norma hay que leer el texto original o su versión oficial.",
    ],
    vocab=[("norma", "regla escrita que una autoridad aprobó"), ("tratado", "acuerdo entre países que se comprometen a cumplir ciertas reglas"), ("afiche", "cartel que informa o convence"), ("organización social", "grupo de personas que se une por una causa común"), ("versión oficial", "texto aprobado por la institución que lo creó")],
    worked=[
        W("Norma u opinión", "Texto A: «Ley que establece que la educación básica es obligatoria». Texto B: «Creo que la gente no debería ir a la escuela». ¿Cuál es una norma?",
          ["La ley fue aprobada por una autoridad.", "La frase B es la opinión de una persona.", "Solo A es una norma."], "El texto A"),
        W("Procedencia de un afiche", "Un afiche de una fundación dice «Protege a la niñez». ¿Qué pregunta de procedencia haces?",
          ["Pregunto quién lo hizo y para qué.", "Una fundación quiere convencer y sensibilizar.", "Es útil, pero no es una ley."], "Quién lo hizo y para qué; no es una ley"),
    ],
    mistakes=[
        M("Creer que un afiche es una ley.", "Un afiche informa o convence, pero no obliga.", "Busca la norma original."),
        M("Confiar en un solo texto sin ver quién lo escribió.", "Cada texto responde a un propósito.", "Revisa la procedencia."),
    ],
    tiers=tiers(
        [E("Una regla escrita que una autoridad aprobó, ¿es una norma o un afiche?", "Una norma", "El afiche solo informa o convence."),
         E("Un acuerdo entre países que se comprometen a cumplir reglas, ¿es un tratado o una opinión?", "Un tratado", "Es un acuerdo entre países."),
         E("«Creo que todos deberían ir a la escuela», ¿es una norma o una opinión?", "Una opinión", "Lo dice una persona, no una autoridad que lo apruebe.")],
        [E("¿Por qué un afiche de una campaña no es lo mismo que una ley?", "Porque informa o convence pero no obliga", "La ley la aprueba una autoridad."),
         E("¿Qué datos buscas al leer una norma?", "Quién la aprobó, cuándo, a quiénes protege y qué dice", "Son los datos de procedencia y contenido."),
         E("¿Para qué sirve leer la versión oficial de un texto?", "Para saber qué dice exactamente la norma", "Así se evitan malentendidos.")],
        [E("Texto: «Ley aprobada por el Congreso en el año 2000». ¿Cuál es la procedencia: el Congreso o un vecino?", "El Congreso", "El texto dice quién la aprobó."),
         E("Un afiche de una fundación tiene la frase «Toda niña tiene derecho a aprender». ¿Qué tipo de fuente es: norma o campaña?", "Campaña", "Su objetivo es informar y convencer."),
         E("Una noticia cuenta un reclamo escuchando solo al vecino que reclama. ¿Qué falta: la versión de la otra parte o una foto más grande?", "La versión de la otra parte", "Una fuente puede mostrar solo una versión.")],
        [E("Paula dice: «Vi un afiche con una regla, así que es ley». ¿Qué error tiene?", "Un afiche no es una ley", "Solo una autoridad aprueba las leyes."),
         E("Un texto dice que «los niños de una región no tienen derechos». ¿Qué fuente buscarías para comprobarlo?", "La norma oficial, como la Declaración Universal o la convención", "Dice que los derechos son universales.")],
        [E("Ordena los pasos para analizar un texto sobre derechos: A) identificar lo que dice, B) ver quién lo escribió, C) decidir qué falta saber.", "B, A, C", "Primero la procedencia, luego el contenido y al final los límites."),
         E("Un afiche de una fundación y una ley dicen lo mismo: «la salud es un derecho». ¿Cuál debe cumplirse por obligación legal?", "La ley", "Es la norma aprobada por una autoridad.")],
    ),
    context=[E("Una niña lee un afiche del municipio que dice «Todos los niños pueden ir a la biblioteca gratis». Su amiga dice que es solo propaganda. ¿Qué pregunta de procedencia resuelve la duda?", "Quién lo hizo y si el municipio lo aprobó", "Así se sabe si es una norma o un aviso.")],
    selfcheck=[E("¿Qué es una norma?", "Una regla escrita que una autoridad aprobó", "Es la definición de la clase."), E("¿Un afiche obliga como una ley?", "No", "Solo informa o convence."), E("¿Qué es la procedencia?", "Quién hizo el texto, cuándo y para qué", "Es lo que se pregunta a toda fuente.")],
    open_task=task("Lee estos dos textos: A) «Artículo de ejemplo de una convención: todo niño y niña tiene derecho a expresar su opinión sobre lo que le afecta». B) «Opinión de un vecino: los niños no deberían opinar». Escribe cuál es una norma, cuál es una opinión y una pregunta de procedencia para cada uno.", "A es una norma: viene de una convención. B es una opinión de un vecino. Preguntas: ¿quién la aprobó? ¿en qué se basa?", ["distingue la norma de la opinión", "formula una pregunta de procedencia para cada texto", "usa palabras de la clase"], ["cuatro frases escritas"], ["decir que la opinión es una norma", "olvidar la procedencia"], "Pide a una persona que diga cuál texto sirve para defender un derecho y por qué."),
    reinforce="Mira un cartel o un aviso de tu barrio sobre derechos y escribe quién lo hizo.",
    extend="Escribe qué otra fuente usarías para comprobar lo que dice un afiche.",
)

register(
    OA13, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar por qué no se respetan algunos derechos, quiénes participan y qué consecuencias tiene. Sirve para saber qué hacer cuando un derecho no se respeta.",
    prior=["Sé que los derechos son universales.", "Sé distinguir una norma de una opinión."],
    explain=[
        "A veces los derechos no se respetan. Una causa común es el prejuicio, que es una idea negativa sobre una persona o un grupo que se tiene antes de conocerlos. Otra causa es la ignorancia: no saber que existe un derecho. Otra es no tener reglas ni personas que actúen cuando alguien es maltratado.",
        "Los actores son quienes participan: la persona afectada, los compañeros, las familias, las profesoras, la comunidad y las instituciones del Estado. Las consecuencias son daños a la persona, como tristeza, miedo, exclusión o abandono de la escuela, y también daño a la convivencia de todo el grupo.",
        "Para actuar, la persona afectada puede contar lo que ocurre a un adulto de confianza. Los compañeros pueden no sumarse al maltrato y apoyar. La escuela debe aplicar reglas y las instituciones deben proteger. Ningún niño debe enfrentar solo una situación en que sus derechos no se respetan.",
    ],
    vocab=[("prejuicio", "idea negativa sobre una persona o grupo que se tiene antes de conocerlos"), ("discriminación", "trato injusto a alguien por una característica suya"), ("exclusión", "dejar a alguien fuera de un grupo o actividad"), ("adulto de confianza", "persona mayor a quien se puede contar un problema"), ("convivencia", "forma en que las personas viven y trabajan juntas")],
    worked=[
        W("Causa, actores y consecuencia", "Un grupo se burla de un compañero por su acento. Nombra una causa, los actores y una consecuencia.",
          ["Causa: prejuicio hacia su forma de hablar.", "Actores: los que se burlan, el compañero y quienes miran.", "Consecuencia: el compañero se siente excluido."], "Causa: prejuicio; actores: grupo, compañero y testigos; consecuencia: exclusión"),
        W("Qué hacer", "Una niña ve que a un compañero no le permiten jugar por su origen. ¿Qué puede hacer?",
          ["No sumarse al maltrato.", "Invitarlo a jugar y contar a una profesora.", "Así apoya sin quedarse sola."], "Invitarlo a jugar y avisar a una profesora"),
    ],
    mistakes=[
        M("Pensar que mirar sin hacer nada no tiene consecuencias.", "Quien mira puede ayudar o empeorar la exclusión.", "Apoya a la persona y avisa a un adulto."),
        M("Culpar a la persona maltratada por ser diferente.", "La causa está en el prejuicio, no en la víctima.", "Revisa qué prejuicio explica el maltrato."),
    ],
    tiers=tiers(
        [E("Dejar a alguien fuera de un grupo, ¿es exclusión o convivencia?", "Exclusión", "La convivencia es vivir juntos."),
         E("Un trato injusto a alguien por una característica suya, ¿es discriminación o amistad?", "Discriminación", "Es un trato injusto."),
         E("Un adulto de confianza, ¿es una persona a quien contar un problema o un desconocido?", "Una persona a quien contar un problema", "Puede ayudar a resolverlo.")],
        [E("¿Por qué el prejuicio puede causar que no se respeten derechos?", "Porque se trata mal a alguien sin conocerlo", "El prejuicio es una idea negativa previa."),
         E("Nombra dos actores que participan cuando un compañero es excluido.", "Por ejemplo: el compañero afectado y quienes lo excluyen", "Son los que intervienen en el hecho."),
         E("¿Qué consecuencias puede tener la exclusión en una persona?", "Tristeza, miedo o abandono de la escuela", "Daña su bienestar.")],
        [E("Sofía ve que excluyen a un compañero. ¿Qué acción ayuda más: reírse con el grupo o invitarlo y avisar a un adulto?", "Invitarlo y avisar a un adulto", "Apoya a la persona afectada."),
         E("Un niño no sabe que tiene derecho a ser escuchado y no dice nada. ¿Cuál es la causa: la ignorancia o la lluvia?", "La ignorancia", "No saber de su derecho lo calla."),
         E("En un curso de 30 estudiantes, 5 excluyen a 1. ¿Cuántos estudiantes no participan en la exclusión, contando al excluido?", "25", "30 menos 5 son 25.", "30-5")],
        [E("Juan dice: «Si lo molestan es porque se lo busca». ¿Qué error comete?", "Culpa a la víctima en vez de ver el prejuicio", "La causa está en el trato injusto."),
         E("Un curso nunca ha dicho nada ante un maltrato. ¿Es neutral? Responde sí o no y explica.", "No; callar permite que siga", "Quien mira sin hacer nada deja que continúe.")],
        [E("Ordena la cadena: A) el compañero deja de venir a la escuela, B) un grupo lo excluye por su origen, C) hay prejuicio hacia su origen.", "C, B, A", "Primero el prejuicio, luego la exclusión y después sus efectos."),
         E("Una escuela aplica una regla que sanciona el maltrato y organiza una charla. ¿Qué actor actúa para proteger: la escuela o quienes maltratan?", "La escuela", "Es una institución que puede proteger.")],
    ),
    context=[E("Un niño recién llegado de otro país no entiende algunas palabras y sus compañeros no lo invitan a jugar. ¿Qué podría hacer el curso para respetar su derecho a participar?", "Invitarlo a jugar y ayudarlo con las palabras nuevas", "Así se incluye en vez de excluir.")],
    selfcheck=[E("¿Qué es un prejuicio?", "Una idea negativa sobre alguien antes de conocerlo", "Es la definición de la clase."), E("¿A quién se puede contar un problema de maltrato?", "A un adulto de confianza", "Puede ayudar a resolverlo."), E("¿Qué consecuencia tiene la exclusión?", "Tristeza, miedo o abandono de la escuela", "Daña a la persona.")],
    open_task=task("Caso de ejemplo: un grupo de un curso se burla de una compañera por vivir en el campo. Escribe la causa más probable, tres actores, dos consecuencias y tres acciones concretas que podrían hacer el curso, la profesora y la compañera.", "Causa: prejuicio. Actores: grupo, compañera, profesora. Consecuencias: tristeza, exclusión. Acciones: invitarla, hablar con la profesora, hacer una charla.", ["nombra la causa", "nombra tres actores", "propone acciones para cada uno"], ["ficha escrita"], ["culpar a la compañera", "no incluir acciones"], "Pide a una persona que diga qué acción le parece más útil y por qué."),
    reinforce="Escribe qué harías si ves que a un compañero lo dejan fuera de un juego.",
    extend="Escribe cómo puede una escuela evitar que haya discriminación.",
)

register(
    OA13, 4,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a comparar cómo han cambiado el reconocimiento y el respeto de los derechos en el tiempo y a escuchar perspectivas distintas sin juzgar el pasado solo desde hoy. Sirve para entender que los derechos se han ido ampliando.",
    prior=["Sé que los derechos son universales.", "Sé analizar causas, actores y consecuencias."],
    explain=[
        "Los derechos no siempre se reconocieron para todos. En el pasado hubo personas que no podían ejercer algunos derechos. Por ejemplo, en Chile, las mujeres votaron por primera vez en una elección municipal en 1935 y una ley de 1949 les reconoció el voto en todas las elecciones. Hoy sabemos que ese derecho no debe depender del sexo.",
        "Al comparar épocas hay que evitar juzgar el pasado solo desde el presente, pero también hay que reconocer que las ideas sobre los derechos cambian y mejoran. Comparamos qué se pensaba, quiénes defendieron el cambio y qué normas se aprobaron. Las perspectivas de quienes estaban excluidos y de quienes tenían el poder eran distintas.",
        "También podemos comparar territorios: una niña de una escuela urbana y un niño de una escuela rural pueden enfrentar dificultades distintas para ejercer su derecho a estudiar, como la distancia. Los derechos son los mismos, pero hay que ver cómo se pueden cumplir en cada lugar.",
    ],
    vocab=[("sufragio", "derecho a votar para elegir autoridades"), ("ampliar", "hacer que más personas puedan ejercer un derecho"), ("época", "período largo de la historia"), ("perspectiva", "mirada de una persona según su situación"), ("urbano", "de la ciudad"), ("rural", "del campo")],
    worked=[
        W("Comparar épocas", "Antes de 1949, en Chile las mujeres no votaban en todas las elecciones. Hoy sí votan. ¿Qué cambió?",
          ["Se aprobó una ley que las incluyó.", "Antes el derecho estaba limitado.", "Hoy se reconoce que no depende del sexo."], "Se amplió el derecho a voto a las mujeres"),
        W("Comparar territorios", "Una escuela rural queda a 10 kilómetros de la casa de un niño y una urbana a 5 cuadras de otro. ¿Cuál tiene más dificultad de acceso?",
          ["Comparo las distancias.", "Diez kilómetros es más que cinco cuadras.", "El niño rural tiene más dificultad, pero ambos tienen el mismo derecho."], "El niño de la escuela rural; el derecho es el mismo"),
    ],
    mistakes=[
        M("Pensar que los derechos siempre se respetaron igual para todos.", "Hubo épocas en que se limitaban a algunos grupos.", "Estudia cómo cambiaron las normas."),
        M("Creer que el derecho a estudiar es distinto en campo y ciudad.", "El derecho es igual; cambian las dificultades.", "Compara cómo cumplirlo en cada lugar."),
    ],
    tiers=tiers(
        [E("El derecho a votar para elegir autoridades, ¿se llama sufragio o patrimonio?", "Sufragio", "Es el nombre del derecho a votar."),
         E("Un período largo de la historia, ¿es una época o una región?", "Una época", "Una región es un lugar."),
         E("Hacer que más personas puedan ejercer un derecho, ¿es ampliar o limitar?", "Ampliar", "Limitar es lo contrario.")],
        [E("¿Por qué las mujeres chilenas no votaban en todas las elecciones antes de 1949?", "Porque la ley limitaba ese derecho", "Una norma no les permitía hacerlo."),
         E("¿Por qué el derecho a estudiar es igual en el campo y en la ciudad?", "Porque los derechos no dependen del lugar", "Lo que cambia es la dificultad para cumplirlo."),
         E("¿Qué es una perspectiva?", "La mirada de una persona según su situación", "Cada persona ve según donde está.")],
        [E("Un niño rural debe caminar 10 kilómetros hasta su escuela. ¿Cuántos kilómetros recorre en un viaje de ida y vuelta?", "20", "Ida y vuelta duplica la distancia.", "10*2"),
         E("Las mujeres votaron por primera vez en una elección municipal en 1935 y una ley de 1949 les reconoció el voto en todas las elecciones. ¿Cuántos años pasaron entre ambos hechos?", "14", "1949 menos 1935 son 14.", "1949-1935"),
         E("Una escuela rural recibe un bus escolar. ¿Se amplió o se limitó el derecho a estudiar de los niños de esa zona?", "Se amplió", "Ahora más niños pueden llegar.")],
        [E("Carlos dice: «Los chilenos de hace 100 años eran malos porque no dejaban votar a las mujeres». ¿Qué error puede tener este juicio?", "Juzga el pasado solo desde hoy sin estudiar cómo pensaban y cómo cambió", "Hay que comprender la época y también reconocer el cambio."),
         E("Un niño del campo y otro de la ciudad, ¿tienen derechos distintos? Responde sí o no y explica.", "No; los derechos son iguales", "Cambian las dificultades, no los derechos.")],
        [E("Ordena de más antiguo a más nuevo: A) ley que reconoce el voto de las mujeres en todas las elecciones (1949), B) primer voto de las mujeres en una elección municipal (1935).", "B, A", "1935 es anterior a 1949."),
         E("Una escuela rural a 8 kilómetros y otra a 3 kilómetros. ¿Cuántos kilómetros más lejos queda la primera?", "5", "8 menos 3 son 5.", "8-3")],
    ),
    context=[E("En una comunidad rural, un niño debe cruzar un río para llegar a la escuela y en invierno no puede. Su derecho a estudiar no cambia, pero ¿qué cambia?", "La dificultad para ejercerlo", "El derecho es el mismo; el acceso es más difícil.")],
    selfcheck=[E("¿Qué es el sufragio?", "El derecho a votar", "Es la definición de la clase."), E("¿Qué significa ampliar un derecho?", "Que más personas puedan ejercerlo", "Es lo contrario de limitar."), E("¿Los derechos dependen del lugar donde se vive?", "No", "Son iguales para todos.")],
    open_task=task("Compara dos casos del derecho a estudiar: A) una niña de una ciudad con una escuela a 4 cuadras; B) un niño de un pueblo de montaña con la escuela a 12 kilómetros. Escribe una semejanza, una diferencia y una medida que ayudaría al niño B sin quitarle nada a la niña A.", "Semejanza: ambos tienen derecho a estudiar. Diferencia: el niño B tiene más distancia. Medida: un transporte escolar.", ["escribe una semejanza", "escribe una diferencia", "propone una medida que ayuda sin dañar a nadie"], ["tres frases"], ["decir que los derechos son distintos", "proponer algo que perjudique a A"], "Pide a una persona que opine si la medida es realista y mejórala si hace falta."),
    reinforce="Pregunta a una persona mayor qué derechos recuerda que cambiaron desde que ella era niña.",
    extend="Escribe un derecho que todavía cuesta que se cumpla en algunos lugares y por qué.",
)

# ================================================================ OA 14
register(
    OA14, 1,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé que cada derecho trae deberes y responsabilidades, para las personas y para el Estado. Sirve para entender por qué vivir en comunidad exige cumplir reglas.",
    prior=["Sé que todas las personas son sujetos de derecho.", "Sé qué es el Estado."],
    explain=[
        "Un deber es lo que una persona o institución está obligada a hacer para que los derechos se cumplan. Mi derecho a estudiar en paz obliga a mis compañeros a respetar el silencio y a mí a respetar el de ellos. Mi derecho a la libre expresión exige que respete la honra de otros. Los derechos de unos son deberes de otros.",
        "Las personas deben respetar los derechos de los demás y respetar las leyes. Una ley es una norma que se aprueba para toda la sociedad. El Estado tiene la responsabilidad de asegurar que las personas puedan ejercer sus derechos, como la educación, la protección de la salud, la libertad de expresión, la propiedad privada y la igualdad ante la ley.",
        "El Estado también debe asegurar que las personas puedan participar en la vida pública: formar organizaciones como juntas de vecinos o fundaciones, integrar partidos políticos y votar. Los Estados cumplen estas tareas con instituciones: escuelas públicas, consultorios, tribunales y municipalidades.",
    ],
    vocab=[("deber", "lo que se está obligado a hacer para que se respeten los derechos"), ("ley", "norma que se aprueba para toda la sociedad"), ("propiedad privada", "derecho a tener cosas propias y a que otros las respeten"), ("igualdad ante la ley", "que la ley se aplique igual a todas las personas"), ("responsabilidad", "hacerse cargo de las consecuencias de lo que se hace o se debe hacer")],
    worked=[
        W("Derecho y deber", "Tengo derecho a que no me quiten mis cosas en el curso. ¿Qué deber tienen los demás?",
          ["Mi derecho a la propiedad privada.", "Los demás no deben tomar lo que no es suyo.", "El deber de otros respeta mi derecho."], "No tomar mis cosas sin permiso"),
        W("Qué debe asegurar el Estado", "Una niña vive lejos y no hay escuela en su pueblo. ¿Qué derecho exige acción del Estado?",
          ["El derecho a la educación.", "El Estado debe asegurar que pueda ejercerlo.", "Puede construir una escuela o un transporte."], "El derecho a la educación; el Estado debe asegurarlo"),
    ],
    mistakes=[
        M("Pensar que los derechos no traen deberes.", "Los derechos de unos se respetan cuando otros cumplen deberes.", "Pregunta qué deber corresponde a cada derecho."),
        M("Creer que solo las personas tienen deberes y el Estado no.", "El Estado debe asegurar que se puedan ejercer los derechos.", "Nombra el deber de las personas y el del Estado."),
    ],
    tiers=tiers(
        [E("Lo que se está obligado a hacer para que se respeten los derechos, ¿es un deber o un premio?", "Un deber", "Un premio depende del mérito."),
         E("Una norma aprobada para toda la sociedad, ¿es una ley o una opinión?", "Una ley", "La opinión no es una norma."),
         E("La educación y la salud, ¿son derechos o castigos?", "Derechos", "Son derechos que el Estado debe asegurar.")],
        [E("¿Por qué los derechos de unos son deberes de otros?", "Porque para que un derecho se cumpla, los demás deben respetarlo", "Ambos van siempre unidos."),
         E("¿Qué debe asegurar el Estado respecto de los derechos?", "Que las personas puedan ejercerlos", "Es su responsabilidad."),
         E("Con tus palabras, ¿qué es la igualdad ante la ley?", "Que la ley se aplica igual a todas las personas", "Así se definió.")],
        [E("Mi derecho a opinar en el curso. ¿Qué deber tengo yo con los demás: escuchar con respeto o interrumpir?", "Escuchar con respeto", "Los demás también tienen derecho a opinar."),
         E("Un consultorio atiende a personas enfermas. ¿Qué derecho ayuda a asegurar?", "La protección de la salud", "Cuida la salud de las personas."),
         E("Un pueblo forma una junta de vecinos para mejorar su plaza. ¿Qué derecho ejerce: el de formar organizaciones o el de propiedad privada?", "El de formar organizaciones", "Las juntas de vecinos son organizaciones de participación social.")],
        [E("Ema dice: «Tengo derechos, pero no tengo deberes». ¿Qué error comete?", "Los derechos traen deberes", "Respetar los derechos de otros es un deber."),
         E("Un alcalde dice: «La educación es un derecho, pero no es mi tarea que haya escuelas». ¿Está bien? Responde sí o no y explica.", "No; el Estado debe asegurar que se pueda ejercer el derecho", "Eso incluye contar con escuelas.")],
        [E("Une cada derecho con una institución que lo ayuda a cumplir: educación, salud, igualdad ante la ley. Instituciones: tribunales, escuela pública, consultorio.", "Educación: escuela pública; salud: consultorio; igualdad ante la ley: tribunales", "Cada institución cumple una de esas tareas."),
         E("Una escuela pública tiene 400 estudiantes y 25 de ellos faltan un día. ¿Cuántos asistieron ese día?", "375", "400 menos 25 son 375.", "400-25")],
    ),
    context=[E("Un grupo de vecinos hace mucho ruido de noche y otro vecino no puede dormir. ¿Qué derecho del vecino se afecta y qué deber no se cumple?", "Su derecho al descanso; el deber de respetar a los demás", "Los derechos de unos incluyen deberes de otros.")],
    selfcheck=[E("¿Qué es un deber?", "Lo que se está obligado a hacer para respetar los derechos", "Es la definición de la clase."), E("Nombra un derecho que el Estado debe asegurar.", "Por ejemplo: educación o salud", "Son derechos citados en la clase."), E("¿Quiénes deben respetar las leyes?", "Todas las personas", "La ley rige para todos.")],
    open_task=task("Completa una tabla de cinco filas con un derecho, el deber de las personas y el deber del Estado. Usa estos derechos: educación, salud, libre expresión, propiedad privada, igualdad ante la ley. Escribe una frase por casilla.", "Educación: las personas asisten y respetan; el Estado asegura escuelas. Salud: cuidar la higiene; el Estado entrega atención.", ["incluye los cinco derechos", "separa el deber de las personas del deber del Estado", "usa frases completas"], ["tabla de quince casillas"], ["repetir el mismo deber para todos los derechos", "olvidar el deber del Estado"], "Pide a una persona que escoja una fila y diga si los dos deberes tienen sentido."),
    reinforce="Escribe un derecho que tienes en tu escuela y el deber que debes cumplir tú.",
    extend="Escribe un deber que cumple tu comunidad para cuidar el derecho a la salud.",
)

register(
    OA14, 2,
    materials="Este cuaderno y un lápiz. Los textos están escritos en los ejercicios.",
    use="Aprenderé a leer un reglamento o una ley para encontrar derechos y deberes, y a preguntar quién la creó. Sirve para entender qué se espera de cada persona.",
    prior=["Sé qué es un deber y qué es una ley.", "Sé preguntar por la procedencia de una fuente."],
    explain=[
        "Las reglas escritas son fuentes importantes. Un reglamento de curso o de escuela dice cómo se convive y lo crea la comunidad escolar. Una ley la aprueba el Congreso y vale para todo el país. Una ordenanza es una norma de una municipalidad y vale solo en su comuna.",
        "Para leer una norma buscamos quién la creó, a quiénes se aplica, qué derechos reconoce, qué deberes impone y qué pasa si no se cumple. Si un reglamento dice que «todos deben respetar el turno para hablar», reconoce el derecho a opinar y exige el deber de escuchar.",
        "No todo lo que aparece escrito es una norma. Un aviso, un afiche o un mensaje no son leyes. Hay que fijarse en quién lo emite y si tiene autoridad para obligar.",
    ],
    vocab=[("reglamento", "conjunto de reglas de una institución, como una escuela"), ("Congreso", "institución donde se discuten y aprueban las leyes"), ("ordenanza", "norma de una municipalidad válida solo en su comuna"), ("sanción", "consecuencia por no cumplir una norma"), ("aplicar", "usar una norma en un caso real")],
    worked=[
        W("Buscar el derecho y el deber", "Regla de ejemplo: «Todo estudiante puede pedir la palabra levantando la mano; los demás esperan su turno». ¿Qué derecho y qué deber aparecen?",
          ["Derecho: pedir la palabra.", "Deber: esperar el turno.", "Ambos aparecen en la misma regla."], "Derecho a opinar; deber de esperar el turno"),
        W("Quién la creó", "Una ordenanza dice que no se puede dejar basura en la plaza de una comuna. ¿Quién la creó y dónde vale?",
          ["Las ordenanzas las crea la municipalidad.", "Valen solo en su comuna.", "Esta no vale en todo el país."], "La municipalidad; vale en su comuna"),
    ],
    mistakes=[
        M("Pensar que un mensaje de redes sociales es una ley.", "Solo la autoridad competente crea una ley.", "Verifica quién la emitió."),
        M("Creer que una ordenanza vale en todo el país.", "Solo vale en su comuna.", "Revisa el alcance de cada norma."),
    ],
    tiers=tiers(
        [E("Las reglas de una escuela, ¿están en un reglamento o en una receta?", "En un reglamento", "Un reglamento reúne reglas."),
         E("Una norma de una municipalidad, ¿es una ordenanza o una ley nacional?", "Una ordenanza", "Vale solo en esa comuna."),
         E("Una consecuencia por no cumplir una norma, ¿es una sanción o un derecho?", "Una sanción", "Es lo que sigue a no cumplir.")],
        [E("¿Quién aprueba las leyes que valen en todo Chile?", "El Congreso", "Es la institución que las aprueba."),
         E("¿Qué cuatro cosas buscas al leer una norma?", "Quién la creó, a quiénes se aplica, qué derechos y deberes tiene y qué pasa si no se cumple", "Son los pasos de la clase."),
         E("¿Por qué un afiche no es una norma?", "Porque no tiene autoridad para obligar", "Solo informa o convence.")],
        [E("Regla de ejemplo: «Cada estudiante debe cuidar los libros de la biblioteca; quien los dañe debe reponerlos». ¿Cuál es la sanción?", "Reponer los libros dañados", "Es la consecuencia de no cuidarlos."),
         E("Una ordenanza de una comuna prohíbe estacionar frente a un consultorio. ¿Se aplica en otra comuna distinta?", "No", "Solo vale en su comuna."),
         E("Regla de ejemplo: «Todos pueden usar la cancha en el recreo, por turnos». ¿Qué derecho reconoce: usar la cancha o votar?", "Usar la cancha", "Eso dice la regla.")],
        [E("Rodrigo dice: «Vi un mensaje que prohíbe salir a la calle, así que es ley». ¿Qué debe preguntar primero?", "Quién lo emitió y si tiene autoridad", "No todo lo escrito es una norma."),
         E("Un reglamento escolar dice que «solo los alumnos de 8.° tienen derecho a ser escuchados». ¿Va contra la idea de derechos universales? Responde sí o no.", "Sí", "Todos los estudiantes tienen derecho a opinar.")],
        [E("Ordena de lo más local a lo más amplio: A) ley nacional, B) reglamento de curso, C) ordenanza de comuna.", "B, C, A", "El curso es lo más local y la ley nacional lo más amplio."),
         E("Un reglamento de curso, una ordenanza de comuna y una ley nacional regulan la convivencia. ¿Cuál vale en todo el país?", "La ley nacional", "La aprueba el Congreso para toda la sociedad.")],
    ),
    context=[E("Un reglamento de curso de ejemplo dice: «Cada integrante puede proponer ideas y debe escuchar con respeto». ¿Qué derecho y qué deber aparecen?", "Derecho a proponer ideas; deber de escuchar con respeto", "La regla contiene ambos.")],
    selfcheck=[E("¿Qué es un reglamento?", "Un conjunto de reglas de una institución", "Es la definición de la clase."), E("¿Quién aprueba las leyes?", "El Congreso", "Es parte de sus funciones."), E("¿Qué es una sanción?", "La consecuencia por no cumplir una norma", "Es la definición de la clase.")],
    open_task=task("Lee esta regla de ejemplo de una escuela: «Todo estudiante puede usar la biblioteca en el recreo. Debe cuidar los libros y devolverlos a tiempo. Quien no los devuelva no podrá llevar otros hasta que lo haga». Escribe el derecho, los dos deberes, la sanción y quién creó probablemente esa regla.", "Derecho: usar la biblioteca. Deberes: cuidar y devolver. Sanción: no llevar otros libros. Creó la regla: la escuela.", ["identifica el derecho", "identifica dos deberes", "identifica la sanción y quién la creó"], ["lista de cuatro ítems"], ["confundir derecho con deber", "olvidar la sanción"], "Pide a una persona que subraye en la regla cada ítem que anotaste."),
    reinforce="Busca una regla de tu escuela o de tu casa y escribe el derecho y el deber que contiene.",
    extend="Escribe una regla de convivencia para tu curso con un derecho, un deber y una sanción razonable.",
)

register(
    OA14, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar qué instituciones del Estado aseguran cada derecho y qué pasa si el Estado o las personas no cumplen. Sirve para saber a quién acudir cuando un derecho no se cumple.",
    prior=["Sé que el Estado debe asegurar derechos.", "Sé leer una norma buscando derechos y deberes."],
    explain=[
        "El Estado cumple sus responsabilidades con instituciones. Las escuelas públicas aseguran el derecho a la educación; los consultorios y hospitales, la protección de la salud; los tribunales, la igualdad ante la ley; y las municipalidades, servicios cercanos como plazas y alumbrado. Cada institución tiene funcionarios que trabajan para que el derecho se cumpla.",
        "Cuando una institución no cumple, hay consecuencias: una persona puede quedarse sin atención o sin escuela. Pero también hay caminos para reclamar: hablar con la dirección, presentar un reclamo a la institución o acudir a los tribunales. Las personas, por su parte, deben cumplir sus deberes: pagar impuestos, respetar las leyes y cuidar lo público.",
        "Los impuestos son dineros que las personas y empresas pagan al Estado según las leyes. Con ellos se financian escuelas, consultorios y otros servicios públicos. Por eso cuidar lo público es cuidar algo que pagamos entre todos.",
    ],
    vocab=[("institución", "organización estable que cumple una tarea para la sociedad"), ("funcionario", "persona que trabaja en una institución del Estado"), ("impuesto", "dinero que se paga al Estado según la ley para financiar servicios"), ("reclamo", "aviso formal de que algo no se cumple"), ("servicio público", "servicio que entrega el Estado, como la educación o la salud")],
    worked=[
        W("Institución y derecho", "Un consultorio atiende a una familia enferma. ¿Qué derecho asegura el Estado y con qué institución?",
          ["Derecho: protección de la salud.", "Institución: el consultorio.", "Lo hacen funcionarios del Estado."], "Protección de la salud, con el consultorio"),
        W("Qué hacer si no se cumple", "Una escuela pública no tiene profesor de Matemática hace dos meses. ¿Qué camino existe?",
          ["Conversar con la dirección.", "Presentar un reclamo a la institución encargada.", "Los vecinos pueden pedir ayuda a las autoridades."], "Reclamar a la dirección y a la institución encargada"),
    ],
    mistakes=[
        M("Pensar que los servicios públicos son gratis porque nadie los paga.", "Se financian con impuestos de todos.", "Recuerda que se pagan entre todos."),
        M("Creer que si una institución falla, no hay nada que hacer.", "Existen caminos de reclamo.", "Informa los pasos para reclamar."),
    ],
    tiers=tiers(
        [E("Una escuela pública, ¿asegura el derecho a la educación o a la propiedad privada?", "A la educación", "Esa es su función."),
         E("Dinero que se paga al Estado según la ley para financiar servicios, ¿es un impuesto o un premio?", "Un impuesto", "Con eso se financian los servicios."),
         E("Una persona que trabaja en una institución del Estado, ¿es un funcionario o un cliente?", "Un funcionario", "Trabaja para el Estado.")],
        [E("¿Con qué se financian las escuelas públicas y los consultorios?", "Con impuestos", "Los pagan personas y empresas."),
         E("¿Qué puede hacer una persona si una institución no cumple?", "Reclamar a la institución o a otra autoridad", "Existen caminos de reclamo."),
         E("¿Qué institución del Estado asegura la igualdad ante la ley?", "Los tribunales", "Aplican la ley a todos por igual.")],
        [E("Un municipio arregla el alumbrado de una plaza con dinero de los impuestos. ¿Qué servicio público presta?", "Alumbrado público", "Es un servicio que entrega la municipalidad."),
         E("Un pueblo de 600 familias paga impuestos; 450 familias hacen uso del consultorio este mes. ¿Cuántas familias no lo usaron?", "150", "600 menos 450 son 150.", "600-450"),
         E("Una niña tiene dolor de oído. ¿A qué institución del Estado puede acudir: un consultorio o un tribunal?", "A un consultorio", "Ahí se atiende la salud.")],
        [E("Esteban dice: «Los consultorios son gratis porque no cuestan nada». ¿Qué error tiene?", "Se financian con impuestos de las personas", "Siempre cuestan, aunque no se pague en el momento."),
         E("Una institución no entrega un servicio. ¿Las personas pueden quedarse calladas? Responde sí o no y explica.", "No; pueden reclamar", "El derecho debe asegurarse.")],
        [E("Ordena los pasos para reclamar: A) acudir a una autoridad superior, B) conversar con la dirección, C) anotar qué derecho no se cumple.", "C, B, A", "Primero se aclara el problema y luego se escala."),
         E("La municipalidad recibe 3 reclamos por una plaza sucia y 4 por una luz mala. ¿Cuántos reclamos son en total?", "7", "3 más 4 son 7.", "3+4")],
    ),
    context=[E("En un pueblo el consultorio se quedó sin atención de pediatría. Los vecinos piden una reunión con la autoridad de salud. ¿Qué derecho reclaman?", "La protección de la salud", "Piden que el Estado asegure la atención.")],
    selfcheck=[E("¿Qué es un impuesto?", "Dinero que se paga al Estado para financiar servicios", "Es la definición de la clase."), E("¿Qué institución asegura la educación?", "La escuela pública", "Esa es su función."), E("¿Qué puede hacer una persona si un derecho no se cumple?", "Reclamar", "Existen caminos de reclamo.")],
    open_task=task("Elige uno de estos casos: a) una escuela pública sin calefacción en invierno; b) un consultorio sin médico; c) una plaza sin alumbrado. Escribe qué derecho o servicio se afecta, quién debe asegurarlo, qué consecuencias tiene y qué harías para reclamar.", "Caso c: afecta la seguridad y el uso de la plaza. La municipalidad debe arreglar. Consecuencia: peligro de noche. Reclamo: carta firmada por vecinos.", ["identifica el derecho o servicio", "nombra a quien debe asegurarlo", "propone un camino concreto de reclamo"], ["ficha escrita"], ["culpar a una persona sin revisar la institución", "no proponer acción"], "Pide a una persona que diga si tu carta de reclamo es clara."),
    reinforce="Nombra tres servicios públicos que usas en tu semana.",
    extend="Escribe qué podemos hacer las personas para cuidar los servicios públicos.",
)

register(
    OA14, 4,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a comparar perspectivas cuando dos derechos parecen chocar y cómo se buscan límites justos. Sirve para resolver conflictos entre derechos sin pasar a llevar a nadie.",
    prior=["Sé que los derechos traen deberes.", "Sé que las leyes y reglamentos regulan la convivencia."],
    explain=[
        "A veces dos derechos parecen chocar. La libertad de expresión permite decir lo que pensamos, pero no permite insultar ni dañar la honra de otra persona. La propiedad privada protege lo que es mío, pero no me autoriza a tapar un camino público que usan los demás. El límite de un derecho suele ser el derecho de otro.",
        "Para analizarlo vemos las perspectivas de cada persona. Quien opina quiere ser escuchado; quien es criticado quiere ser respetado. Un vecino quiere cercar su terreno; otro quiere pasar por el camino que usa desde hace años. Ambas miradas importan.",
        "Se busca una solución que respete lo esencial de cada derecho: opinar con respeto, cercar el terreno pero dejar el paso público. Si no hay acuerdo, una autoridad con facultad, como un juez, decide aplicando la ley igual para todos.",
    ],
    vocab=[("límite", "hasta dónde llega un derecho sin dañar el de otro"), ("honra", "buena fama y dignidad de una persona"), ("camino público", "camino que puede usar cualquier persona"), ("conflicto", "desacuerdo entre personas por intereses o derechos distintos"), ("juez", "persona autorizada para decidir según la ley")],
    worked=[
        W("Dos derechos que chocan", "Una niña quiere hacer un dibujo burlándose de un compañero. ¿Qué derechos chocan y cuál es el límite?",
          ["Libertad de expresión de ella.", "Derecho del compañero a ser respetado.", "El límite: no dañar su honra."], "Expresión contra respeto; el límite es no dañar la honra"),
        W("Buscar una solución", "Un vecino quiere cercar su terreno, que cruza un camino usado por todos. ¿Qué solución respeta ambos derechos?",
          ["Reconozco su propiedad privada.", "Reconozco el camino público.", "Puede cercar el terreno dejando libre el paso."], "Cercar el terreno dejando libre el camino público"),
    ],
    mistakes=[
        M("Creer que un derecho no tiene límites.", "Cada derecho termina donde empieza el de otro.", "Pregunta a quién podría dañar."),
        M("Pensar que solo una perspectiva importa en un conflicto.", "Cada persona tiene derechos.", "Escucha a todas las partes."),
    ],
    tiers=tiers(
        [E("Hasta dónde llega un derecho sin dañar el de otro, ¿es su límite o su deber?", "Su límite", "El deber es lo que se debe hacer."),
         E("La buena fama y dignidad de una persona, ¿es su honra o su territorio?", "Su honra", "Es lo que se daña con un insulto."),
         E("Un desacuerdo entre personas por derechos o intereses distintos, ¿es un conflicto o un premio?", "Un conflicto", "Es el nombre de ese desacuerdo.")],
        [E("¿Por qué la libertad de expresión no permite insultar a otra persona?", "Porque daña su honra y su derecho a ser respetada", "El derecho tiene límite en el de otros."),
         E("¿Por qué el dueño de un terreno no puede cerrar un camino público?", "Porque otras personas lo usan y tienen derecho a pasar", "La propiedad privada tiene límites."),
         E("¿Quién decide cuando no hay acuerdo y se aplica la ley?", "Un juez", "Tiene la facultad de decidir según la ley.")],
        [E("Dos hermanos discuten por una pieza que ambos quieren usar para estudiar en silencio y para ver televisión. ¿Qué solución respeta a ambos: un horario compartido o que gane el más fuerte?", "Un horario compartido", "Respeta el derecho de cada uno."),
         E("Un vecino quiere poner música a alto volumen a las 11 de la noche. ¿Qué derecho de los demás se ve afectado: el descanso o la propiedad?", "El descanso", "El ruido impide dormir."),
         E("Un estudiante critica con respeto una decisión del curso. ¿Ejerció bien su libertad de expresión? Responde sí o no.", "Sí", "Opinó sin dañar la honra de nadie.")],
        [E("Carla dice: «Si es mi opinión, puedo decir cualquier cosa de otros». ¿Qué error tiene?", "La expresión tiene como límite la honra de los demás", "Un derecho termina donde empieza el de otro."),
         E("Un conflicto se resuelve dando la razón siempre a quien tiene más dinero. ¿Respeta la igualdad ante la ley? Responde sí o no.", "No", "La ley debe aplicarse igual a todos.")],
        [E("Ordena los pasos para resolver un conflicto de derechos: A) buscar una solución que respete a ambas partes, B) escuchar a cada persona, C) identificar qué derechos chocan.", "C, B, A", "Primero se ve el problema, luego se escucha y al final se busca la solución."),
         E("Dos vecinos reparten 60 minutos de uso de una cancha en partes iguales. ¿Cuántos minutos usa cada uno?", "30", "60 dividido por 2 es 30.", "60//2")],
    ),
    context=[E("En una población, una familia quiere hacer una fiesta hasta tarde y un vecino enfermo necesita descansar. ¿Qué solución respeta a ambos: terminar a una hora acordada o que la familia haga lo que quiera?", "Terminar a una hora acordada", "Respeta el derecho de ambos.")],
    selfcheck=[E("¿Cuál es el límite de un derecho?", "El derecho de otra persona", "Termina donde empieza el de otro."), E("¿Qué es la honra?", "La buena fama y dignidad de una persona", "Es la definición de la clase."), E("¿Quién decide si no hay acuerdo?", "Un juez", "Aplica la ley.")],
    open_task=task("Elige uno de estos conflictos: a) una niña quiere publicar un comentario burlón sobre un compañero; b) un vecino quiere cerrar un pasaje que usa toda la cuadra; c) un grupo quiere hacer una fiesta con mucho ruido. Escribe qué derechos chocan, la perspectiva de cada parte y una solución que respete a todos.", "Caso b: propiedad privada contra libre tránsito. Vecino: quiere cuidar su terreno; cuadra: quiere pasar. Solución: reja con puerta que siempre esté abierta en horario.", ["nombra los dos derechos", "describe las dos perspectivas", "propone una solución que respeta a ambas partes"], ["ficha de tres partes"], ["decir que un derecho no tiene límites", "elegir una solución que perjudique a una parte"], "Cuéntale el caso a una persona de tu casa y pídele que critique tu solución."),
    reinforce="Escribe un conflicto pequeño de tu curso y cómo se resolvió con respeto.",
    extend="Escribe un derecho que tengas y su límite cuando convives con otros.",
)

register(
    OA14, 5,
    materials="Este cuaderno y un lápiz. Los casos y datos están escritos en los ejercicios.",
    use="Aprenderé a argumentar con evidencia por qué participar en la vida pública (organizarse, votar, formar juntas de vecinos) es un derecho y también una responsabilidad. Sirve para decidir cómo participar.",
    prior=["Sé que el Estado debe asegurar derechos.", "Sé argumentar con afirmación, evidencia y razón."],
    explain=[
        "La participación en la vida pública es un derecho. Las personas pueden formar organizaciones de participación social, como las fundaciones y las juntas de vecinos, y también pueden formar o integrar partidos políticos. En Chile, las personas chilenas desde los 18 años pueden votar, lo que se llama sufragio, para elegir a sus autoridades.",
        "El Estado debe asegurar que ese derecho se pueda ejercer: debe permitir que las organizaciones se formen, que se hagan elecciones transparentes y que cada voto cuente una vez. Pero también es una responsabilidad: si las personas no participan, las decisiones las toman otros.",
        "Para argumentar a favor de participar, usamos evidencia: datos de una junta de vecinos que consiguió una mejora, resultados de una elección, o relatos de organizaciones. Una buena evidencia dice dónde, cuándo y cuántas personas participaron.",
    ],
    vocab=[("participación", "tomar parte en las decisiones de la comunidad"), ("junta de vecinos", "organización de los habitantes de un barrio para mejorar su entorno"), ("partido político", "organización de personas con ideas comunes sobre cómo gobernar"), ("sufragio", "derecho a votar para elegir autoridades"), ("elección", "votación para elegir autoridades o representantes")],
    worked=[
        W("Evidencia de participación", "Una junta de vecinos reunió 120 firmas y consiguió luminarias para su pasaje. ¿Qué afirmación apoya?",
          ["La evidencia es el logro de las luminarias con 120 firmas.", "Muestra que organizarse puede mejorar el barrio.", "La afirmación es que participar sirve."], "Que participar y organizarse puede mejorar el barrio"),
        W("Leer un resultado", "Elección de ejemplo: lista A tuvo 180 votos y lista B tuvo 120. ¿Quién ganó y por cuánto?",
          ["Comparo los números.", "180 es mayor que 120.", "Diferencia: 180 menos 120 son 60."], "La lista A, por 60 votos"),
    ],
    mistakes=[
        M("Pensar que votar o participar no sirve porque «uno solo no cambia nada».", "Muchas personas juntas sí cambian decisiones.", "Mira ejemplos de organización y resultados."),
        M("Creer que participar es solo derecho y no responsabilidad.", "Si no participas, otros deciden por ti.", "Considera ambas caras."),
    ],
    tiers=tiers(
        [E("Tomar parte en las decisiones de la comunidad, ¿es participación o aislamiento?", "Participación", "El aislamiento es lo contrario."),
         E("Una organización de vecinos de un barrio, ¿es una junta de vecinos o un partido político?", "Una junta de vecinos", "Los partidos políticos se centran en ideas de gobierno."),
         E("El derecho a votar, ¿se llama sufragio o propiedad?", "Sufragio", "Es el nombre del derecho a votar.")],
        [E("¿Por qué participar es un derecho y también una responsabilidad?", "Porque se puede ejercer, pero si no se hace, otros deciden", "Tiene dos caras."),
         E("¿Qué debe asegurar el Estado en una elección?", "Que sea transparente y que cada voto cuente una vez", "Así el sufragio es justo."),
         E("¿Desde qué edad pueden votar las personas en Chile?", "Desde los 18 años", "Así está definido el derecho a sufragio.")],
        [E("Una junta de vecinos de ejemplo recoge 150 firmas y otra recoge 90. ¿Cuántas firmas más recogió la primera?", "60", "150 menos 90 son 60.", "150-90"),
         E("En una elección de ejemplo participan 500 personas; 320 votan por una lista y el resto por la otra. ¿Cuántas votan por la otra lista?", "180", "500 menos 320 son 180.", "500-320"),
         E("Una fundación organiza una campaña para limpiar una playa. ¿Qué derecho ejercen sus integrantes: formar organizaciones o votar?", "Formar organizaciones", "Una fundación es una organización de participación.")],
        [E("Gaspar dice: «Mi voto no sirve porque somos muchos». ¿Qué argumento le darías?", "Que muchos votos juntos deciden el resultado", "Cada voto suma al total."),
         E("Un vecino afirma que «las juntas de vecinos no logran nada» sin dar datos. ¿Qué le falta?", "Evidencia", "Sin datos no se puede comprobar.")],
        [E("Resultados de ejemplo: A 210 votos, B 195 votos, C 90 votos. ¿Quién ganó?", "A", "210 es el número mayor."),
         E("Con los resultados anteriores, ¿cuántos votos hubo en total?", "495", "210 más 195 más 90 son 495.", "210+195+90")],
    ),
    context=[E("Los vecinos de un pasaje quieren que se instale un semáforo. Reúnen 80 firmas y piden una reunión con el municipio. ¿Qué derecho ejercen: participar en la vida pública o la propiedad privada?", "Participar en la vida pública", "Se organizan para pedir una mejora a la autoridad.")],
    selfcheck=[E("¿Qué es una junta de vecinos?", "Una organización de los habitantes de un barrio", "Es la definición de la clase."), E("¿Qué es el sufragio?", "El derecho a votar", "Es la definición del vocabulario."), E("¿Por qué participar es una responsabilidad?", "Porque si no participas, otros deciden", "Es una de las dos caras.")],
    open_task=task("Datos de ejemplo: en un barrio, una junta de vecinos consiguió con 120 firmas que arreglaran una plaza; después de la mejora, 70 niños usan la plaza cada semana, antes eran 30. Escribe un argumento a favor de participar con afirmación, evidencia, razón y un límite.", "Afirmación: participar mejora el barrio. Evidencia: 120 firmas y 70 niños en vez de 30. Razón: la plaza se arregló. Límite: es un solo barrio.", ["usa los datos entregados", "incluye razón y límite", "relaciona la evidencia con la afirmación"], ["párrafo de cuatro frases"], ["dar una opinión sin datos", "generalizar a todo el país"], "Pide a una persona que subraye la afirmación y la evidencia de tu texto."),
    reinforce="Escribe una forma en que puedes participar en la vida de tu curso o barrio.",
    extend="Escribe una pregunta que le harías a un dirigente vecinal sobre su trabajo.",
)
