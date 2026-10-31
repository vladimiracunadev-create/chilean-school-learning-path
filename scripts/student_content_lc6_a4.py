"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 13 (formación de una persona íntegra según cada pueblo, en tensión con otros sistemas de valores) y
OA 14 (técnicas y actividades de producción de otros pueblos indígenas y de otras culturas).

Las comunidades, personas, técnicas y testimonios son INVENTADOS y se rotulan así; no se describe ninguna técnica
ni valor de un pueblo real. Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc6_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA13, OA14 = "LC06 OA 13", "LC06 OA 14"

# ------------------------------------------------------------------ OA 13
FLD = ("Ficha situada (inventada). Comunidad: Loma Dorada (no es un pueblo real). Territorio: una loma con chacras, una sede comunitaria y un camino a la escuela. "
       "Fuente y responsable: doña Gladys, abuela y educadora de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Gladys autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan las enseñanzas que la comunidad entrega solo a sus jóvenes.")
TLD = ("Testimonio inventado de doña Gladys, de Loma Dorada: «Una persona íntegra es la que dice la verdad, ayuda en las tareas de todos y escucha antes de hablar. "
       "Los niños aprenden mirando a los adultos y participando, no solo con palabras. En la ciudad a veces les enseñan que lo importante es ganar; nosotros les decimos que también importa cómo se gana.»")

L(
    OA13, 1, materials=MAT,
    use="Aprenderé a situar una concepción de la persona íntegra: de qué comunidad es, quién la cuenta y qué no se cuenta. Sirve para valorar cómo un pueblo entiende la buena formación de las personas sin hablar por otros.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada comunidad cuenta su forma de vida a su manera."],
    explain=[
        "Una persona íntegra es una persona completa y coherente: lo que piensa, lo que dice y lo que hace van juntos, y actúa con respeto, honestidad y responsabilidad hacia los demás y la naturaleza. Cada pueblo indígena tiene su propia concepción de cómo se forma una persona así, y la transmite a los niños en la familia y en la comunidad.",
        "Un valor es una idea que una comunidad considera importante para vivir bien, como la verdad, la ayuda mutua o el respeto. Un sistema de valores es el conjunto de valores que orienta a un grupo. En la sociedad global conviven muchos sistemas de valores, y algunos ponen más énfasis en competir o tener más. Los valores de un pueblo y los de la sociedad global pueden coincidir o tensionarse.",
        "Antes de valorar, hay que situar. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es la concepción y qué no se cuenta. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("persona íntegra", "persona coherente: lo que piensa, dice y hace van juntos, y actúa con respeto y responsabilidad"), ("valor", "idea que una comunidad considera importante para vivir bien"), ("sistema de valores", "conjunto de valores que orienta a un grupo"), ("sociedad global", "conjunto de sociedades conectadas entre sí en el mundo actual"), ("tensión", "dificultad que aparece cuando dos formas de ver las cosas no coinciden")],
    worked=[
        W("Leer una ficha situada", FLD + " ¿De quién es la concepción y qué no se cuenta?", ["La comunidad es Loma Dorada y la fuente es doña Gladys.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuentan las enseñanzas que entregan solo a sus jóvenes."], "La concepción es de doña Gladys, de Loma Dorada; no se cuentan las enseñanzas reservadas a sus jóvenes."),
        W("Reconocer un valor", "Doña Gladys dice: «Una persona íntegra ayuda en las tareas de todos». ¿Qué valor aparece?", ["Ayudar en las tareas de todos es compartir el trabajo.", "El valor es la ayuda mutua.", "Se aprende participando, según la fuente."], "El valor que aparece es la ayuda mutua."),
    ],
    mistakes=[
        M("Pensar que una persona íntegra es la que no comete ningún error.", "La integridad es coherencia entre lo que se piensa, dice y hace, no perfección.", "Busca si lo que dice y lo que hace van juntos."),
        M("Decir que el valor de Loma Dorada es el de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según doña Gladys, en Loma Dorada…»."),
    ],
    R=[
        ex("Según la ficha de Loma Dorada, ¿quién es la fuente?", "Doña Gladys", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Loma Dorada? A) una loma con chacras, una sede y un camino a la escuela B) un lago con un puerto", "A", "El lago y el puerto son de otras fichas."),
        ex("La ficha de Loma Dorada dice que no se cuentan ciertas enseñanzas reservadas a los jóvenes. ¿Las inventas para completar tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es una persona íntegra? A) una persona cuyo pensar, decir y hacer van juntos B) una persona que nunca se equivoca", "A", "La integridad es coherencia, no perfección."),
        ex("Verdadero o falso: un valor es una idea que una comunidad considera importante para vivir bien.", "Verdadero", "Esa es la definición de valor."),
        ex("Verdadero o falso: la concepción de persona íntegra de Loma Dorada vale para todos los pueblos indígenas.", "Falso", "Cada pueblo tiene la suya."),
    ],
    A=[
        ex("Doña Gladys dice: «Los niños aprenden mirando a los adultos y participando». ¿Cómo se forma una persona según esa frase? A) solo memorizando B) observando y participando", "B", "La frase habla de aprender mirando y participando."),
        ex("Clasifica en VALOR o ACCIÓN: a) la honestidad b) decir la verdad cuando cuesta.", "a valor, b acción", "La honestidad es la idea; decir la verdad es lo que se hace."),
        ex("Tema: la persona íntegra. Una compañera trae una ficha con comunidad y fuente, pero sin permiso. ¿Qué falta? A) el color del papel B) la autorización de la fuente para compartir", "B", "El permiso es parte de una ficha situada."),
    ],
    Z=[
        ex("Pablo escribe: «Como doña Gladys valora escuchar antes de hablar, todos los pueblos indígenas valoran el silencio». ¿Qué error comete?", "Generaliza el testimonio de una persona a todos los pueblos", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de hablar de la formación de las personas? A) para escribir más rápido B) porque cada comunidad entiende la formación de manera distinta", "B", "Situar muestra de quién es la mirada."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Loma Dorada. Territorio: loma con chacras». ¿Qué datos faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todos los pueblos educan a sus hijos como doña Gladys». ¿Qué corriges? A) lo dejo igual B) escribo «según doña Gladys (persona inventada), en Loma Dorada…»", "B", "El cartel debe atribuir el dato a esa fuente."),
    ],
    context=[ex("En una reunión de apoderados alguien dice que «los pueblos indígenas educan mejor» sin dar fuente. ¿Qué haces? A) lo anoto como verdad B) pregunto de qué pueblo habla y quién lo cuenta", "B", "Hay que situar el dato antes de aceptarlo.")],
    selfcheck=[
        ex("Escribe qué es un sistema de valores con tus palabras.", "Conjunto de valores que orienta a un grupo", "Es la definición de la explicación."),
        ex("Verdadero o falso: la integridad significa no equivocarse nunca.", "Falso", "Significa coherencia entre pensar, decir y hacer."),
        ex("Tema: la persona íntegra. Ante una duda sobre una comunidad real, ¿qué haces? A) lo supongo B) pregunto al educador tradicional o a la comunidad", "B", "Ellos son la fuente."),
    ],
    task=T("Lee esta nota inventada de doña Gladys: «En Loma Dorada, cuando hay una tarea en la sede, vamos todos. Los niños aprenden a cumplir lo que prometen. Hay enseñanzas que damos solo a los jóvenes.» Haz una ficha con: comunidad, fuente, qué valores aparecen, qué dice la fuente y un límite. Luego escribe una frase con «Yo pienso que…» sobre qué significa ser una persona íntegra en esa comunidad.",
           "Comunidad: Loma Dorada. Fuente: doña Gladys. Valores: ayuda mutua y cumplir la palabra. Dice: todos van a las tareas de la sede y los niños aprenden a cumplir lo que prometen. Límite: no se cuentan las enseñanzas para jóvenes. Yo pienso que una persona íntegra en Loma Dorada cumple lo que promete y ayuda en lo de todos.",
           ["completa la ficha con datos de la nota", "separa la fuente de su opinión", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["inventar las enseñanzas reservadas", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Loma Dorada la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué ser coherente entre lo que se dice y lo que se hace es parte de ser una persona íntegra.",
)

L(
    OA13, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre la formación de las personas con límites declarados: qué dice la fuente, qué valor muestra, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar una comunidad con su ficha.", "Sé qué es un valor y una persona íntegra."],
    explain=[
        "Un testimonio sobre cómo se forma una persona cuenta valores, formas de enseñar y personas que enseñan. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. El valor que muestra cada frase. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de doña Gladys, «dice la verdad» muestra el valor de la honestidad y «ayuda en las tareas de todos» muestra la ayuda mutua. Ella también cuenta una diferencia: en la ciudad, a veces enseñan que lo importante es ganar, mientras que ellos dicen que también importa cómo se gana. Eso es lo que ella dice; no sabemos qué opinan todas las personas de la ciudad.",
        "Leer con límites declarados significa no atribuir a la sociedad global ni a la comunidad cosas que la fuente no dijo. Si dudamos, escribimos «el testimonio no lo dice». Y si queremos saber más sobre cómo forma a sus jóvenes un pueblo real, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("honestidad", "decir y hacer lo que es verdadero, sin engañar"), ("ayuda mutua", "ayudarse entre personas para lograr algo de todos"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("generalizar", "extender un caso a todos los casos sin pruebas"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TLD + " Separa lo que dice, el valor, lo que interpreto y lo que no se cuenta.", ["Dice: los niños aprenden mirando a los adultos y participando.", "Valor: aprender con el ejemplo y la participación.", "Interpreto: yo pienso que los adultos tienen una gran responsabilidad.", "No se cuenta: qué opinan las demás personas de la ciudad."], "Dice: aprenden mirando y participando. Valor: el ejemplo y la participación. Interpreto: los adultos tienen gran responsabilidad. No se cuenta: qué opinan las personas de la ciudad."),
        W("Detectar una generalización", "Un niño escribe: «Doña Gladys dice que en la ciudad todos enseñan a ganar a toda costa». ¿Está bien?", ["Reviso el testimonio: dice que «a veces» les enseñan que lo importante es ganar.", "El niño cambió «a veces» por «todos».", "Generalizó lo que la fuente dijo con cautela."], "No: convierte «a veces» en «todos»."),
    ],
    mistakes=[
        M("Convertir «a veces» o «algunos» en «todos».", "Cambia el sentido de lo que dijo la fuente.", "Copia las palabras de cantidad tal como están."),
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
    ],
    R=[
        ex("Según doña Gladys, ¿cómo aprenden los niños: mirando a los adultos y participando, o solo leyendo?", "Mirando a los adultos y participando", "El testimonio lo dice así."),
        ex("Tema: la persona íntegra. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no dice qué piensa la gente de la ciudad, ¿qué escribes? A) la gente de la ciudad piensa mal B) el testimonio no lo dice", "B", "No se inventan opiniones."),
    ],
    C=[
        ex("Doña Gladys dice: «Una persona íntegra dice la verdad». ¿Qué valor muestra? A) competencia B) honestidad", "B", "Decir la verdad es honestidad."),
        ex("Verdadero o falso: «a veces enseñan a ganar» significa lo mismo que «todos enseñan a ganar».", "Falso", "«A veces» no es «todos»."),
        ex("Verdadero o falso: respetar las enseñanzas que la comunidad reserva es parte de leer con límites.", "Verdadero", "Lo reservado no se pide ni se inventa."),
    ],
    A=[
        ex("Doña Gladys dice: «En la ciudad a veces les enseñan que lo importante es ganar». Clasifica en DICE LA FUENTE o INTERPRETO: a) a veces enseñan que lo importante es ganar b) en la ciudad no existe la ayuda mutua.", "a dice la fuente, b interpreto", "La segunda no está en el testimonio y es falsa como generalización."),
        ex("Doña Gladys dice: «Nosotros les decimos que también importa cómo se gana». ¿Qué valor muestra? A) la honestidad al competir B) la rapidez", "A", "Importa cómo se gana, no solo ganar."),
        ex("Un niño escribe: «Doña Gladys cuenta que los jóvenes reciben una prueba secreta». ¿Qué dato no está en el testimonio?", "La prueba secreta", "El testimonio solo habla de enseñanzas que no se cuentan, no de pruebas."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «La ciudad enseña peores valores que la comunidad». ¿Qué debería hacer con esa frase?", "Quitarla porque ordena culturas y no está en la fuente", "No está en el testimonio y jerarquiza."),
        ex("Tema: la persona íntegra. ¿Por qué conviene escribir los límites al final del trabajo? A) para llenar la hoja B) para mostrar hasta dónde llega lo afirmado", "B", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Doña Gladys cuenta que los niños aprenden participando». 2) «Doña Gladys cuenta que los niños de la ciudad no aprenden participando». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no contiene."),
        ex("Doña Gladys no contó cómo reaccionan los niños cuando pierden. ¿Qué escribes en los límites? A) no sé cómo reaccionan cuando pierden B) se enojan pocas veces", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("En un trabajo grupal, una compañera dice: «La ciudad solo enseña a competir». El único texto que leyeron es el de doña Gladys. ¿Qué cambio respeta la fuente? A) dejar la frase B) «Doña Gladys cuenta que a veces enseñan que lo importante es ganar»", "B", "La frase A usa la cantidad que la fuente indicó.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre la formación de las personas.", "Lo que dice la fuente, el valor que muestra, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: la persona íntegra. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: la persona íntegra. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Gladys: «Cuando un niño se equivoca, lo escuchamos y lo ayudamos a arreglar lo que hizo. A veces en la escuela de la ciudad los castigan sin preguntar. Nosotros creemos que se aprende más cuando uno repara el daño. Hay enseñanzas que damos solo a los jóvenes.» Haz cuatro columnas: «La fuente dice», «Valor que muestra», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: escuchan al niño que se equivoca y lo ayudan a arreglar lo que hizo; a veces en la escuela de la ciudad los castigan sin preguntar. Valor: responsabilidad y reparación. Yo interpreto: yo pienso que escuchar ayuda a entender por qué ocurrió. No se cuenta: las enseñanzas para jóvenes. Límite: no sé cómo es la escuela de la ciudad en todos los casos.",
           ["separa cuatro columnas", "usa datos del testimonio", "conserva las palabras de cantidad"], ["tabla de cuatro columnas", "frase de límites"], ["convertir «a veces» en «siempre»", "inventar lo reservado"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que respete «a veces»."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Gladys.",
    extend="Explica por qué «reparar el daño» y «castigar» pueden formar a una persona de maneras distintas, según este testimonio.",
)

L(
    OA13, 3, materials=MAT,
    use="Aprenderé a reconocer tensiones entre el sistema de valores de una comunidad y otros presentes en la sociedad global, sin decir que uno es bueno y otro malo, para valorar cómo se forma una persona íntegra.",
    prior=["Sé leer un testimonio con límites.", "Sé qué es un valor y un sistema de valores."],
    explain=[
        "Una tensión entre sistemas de valores aparece cuando dos formas de orientar la vida piden cosas distintas. Por ejemplo, un sistema puede poner mucho énfasis en competir y ganar, y otro, en cooperar y compartir. En la sociedad global ambos aparecen: se compite en deportes y en trabajos, pero también hay solidaridad y colaboración.",
        "Estas tensiones se viven en situaciones concretas. En Loma Dorada, doña Gladys cuenta que el trabajo de todos se hace entre todos. Un niño de la comunidad que va a un colegio de ciudad puede encontrarse con un premio que se da solo al más rápido. Entonces tiene que pensar qué valores quiere cuidar y cómo explicarlos a otros.",
        "Para analizar una tensión usamos preguntas iguales para ambos lados: ¿qué valor aparece?, ¿qué pide hacer?, ¿qué puede aportar?, ¿qué riesgo tiene? No decimos que un sistema sea «bueno» y el otro «malo»: reconocemos lo que cada uno aporta y dónde chocan. Y un caso no representa a toda la sociedad ni a todos los pueblos.",
    ],
    vocab=[("tensión", "dificultad que aparece cuando dos formas de orientar la vida piden cosas distintas"), ("cooperar", "trabajar con otros para lograr algo de todos"), ("competir", "esforzarse por ganar a otros en algo"), ("solidaridad", "ayudar a otros porque se sienten parte de un mismo grupo"), ("riesgo", "posibilidad de que algo salga mal")],
    worked=[
        W("Analizar una tensión", "Caso inventado: en un colegio de ciudad dan un premio solo al más rápido en resolver una tarea. Un niño de Loma Dorada, que aprendió a ayudar a quien se atrasa, no sabe qué hacer. ¿Qué valores chocan?", ["El premio pone el énfasis en ser el más rápido (competir).", "El niño aprendió la ayuda mutua (cooperar).", "Los dos valores piden cosas distintas en esa situación."], "Chocan competir (ser el más rápido) y cooperar (ayudar a quien se atrasa)."),
        W("Reconocer lo que aporta cada lado", "En el mismo caso: ¿qué puede aportar competir y qué puede aportar cooperar?", ["Competir puede motivar a mejorar.", "Cooperar permite que nadie se quede atrás.", "Cada valor aporta algo, aunque pueden chocar."], "Competir puede motivar a mejorar; cooperar evita que alguien se quede atrás."),
    ],
    mistakes=[
        M("Decir que competir es malo y cooperar es bueno, siempre.", "Cada valor aporta algo según la situación.", "Describe qué aporta y qué riesgo tiene cada uno."),
        M("Concluir que toda la sociedad global solo compite.", "En la sociedad global también hay solidaridad y colaboración.", "Escribe «en este caso» y no más."),
    ],
    R=[
        ex("En el caso del premio al más rápido, ¿qué valor pone el énfasis en ganar: competir o cooperar?", "Competir", "El premio es para quien gana en rapidez."),
        ex("El niño de Loma Dorada aprendió a ayudar a quien se atrasa. ¿Qué valor es? A) la ayuda mutua B) la rapidez", "A", "Ayudar a quien se atrasa es ayuda mutua."),
        ex("Una tensión, ¿es una dificultad entre dos formas de orientar la vida o es un acuerdo total?", "Una dificultad entre dos formas de orientar la vida", "Esa es la definición de tensión."),
    ],
    C=[
        ex("Verdadero o falso: competir siempre es malo y cooperar siempre es bueno.", "Falso", "Cada uno aporta algo según la situación."),
        ex("¿Qué se hace al analizar una tensión de valores? A) elegir un lado sin mirar al otro B) usar las mismas preguntas para ambos lados", "B", "Las preguntas iguales evitan el trato desigual."),
        ex("Verdadero o falso: en la sociedad global también hay solidaridad y colaboración.", "Verdadero", "No toda la sociedad global se reduce a competir."),
    ],
    A=[
        ex("Pregunta: «qué puede aportar». Competir: motiva a mejorar. Cooperar: nadie se queda atrás. ¿Qué aporta cooperar? A) que haya un solo ganador B) que nadie se quede atrás", "B", "Esa es la ventaja de cooperar en el caso."),
        ex("Clasifica en COMPETIR o COOPERAR: a) repartirse las tareas para terminar todos b) intentar llegar primero para ganar un premio.", "a cooperar, b competir", "La primera comparte el trabajo; la segunda busca ganar."),
        ex("Caso inventado: un equipo deportivo de una escuela celebra juntos tanto cuando gana como cuando pierde, y ayuda al que se lesionó. ¿Qué dos valores aparecen? A) competir y acumular B) cooperar y solidaridad", "B", "Celebran juntos y ayudan al lesionado."),
    ],
    Z=[
        ex("Ana dice: «Los valores de la sociedad global son malos y los de las comunidades indígenas, buenos». ¿Qué error comete?", "Ordena sistemas de valores en buenos y malos", "Cada uno aporta algo y tiene riesgos."),
        ex("Un compañero escribe: «Como el niño de Loma Dorada ayuda, todos los niños indígenas ayudan». ¿Qué debería escribir? A) «en este caso inventado» B) «en todos los casos»", "A", "Un caso no representa a todos."),
    ],
    D=[
        ex("Caso inventado: una empresa de una ciudad da el mismo bono a todo el equipo cuando se cumple la meta. ¿Qué valor muestra esa decisión? A) competir B) cooperar", "B", "Todos reciben lo mismo por el trabajo de todos."),
        ex("Una niña dice que para resolver la tensión del premio al más rápido hay que «ignorar a quien se atrasa». ¿Qué valor deja de lado? A) la ayuda mutua B) la honestidad", "A", "Ignorar a quien se atrasa va contra ayudar a quien lo necesita."),
    ],
    context=[ex("En tu curso se organiza una competencia de dibujo con premio al mejor. Un compañero dice que prefiere hacer un mural entre todos. ¿Qué haces para valorar ambas ideas? A) analizo qué aporta y qué riesgo tiene cada una y propongo juntar ambas B) elijo solo una sin discutir", "A", "Se reconocen los aportes de ambos valores.")],
    selfcheck=[
        ex("Escribe una pregunta para analizar una tensión de valores.", "Por ejemplo: ¿qué puede aportar cada valor?", "Debe ser igual para ambos lados."),
        ex("Verdadero o falso: puedo decir que un sistema de valores es el bueno y otro el malo.", "Falso", "Se reconoce lo que cada uno aporta y dónde chocan."),
        ex("Nombra dos valores que pueden tensionarse.", "Por ejemplo: competir y cooperar", "Son los del caso estudiado."),
    ],
    task=T("Analiza este caso inventado. Un niño de Loma Dorada va a un colegio donde el profesor anuncia: «El primero en terminar la tarea gana un diploma». Él aprendió en su comunidad a ayudar a quien se atrasa. Haz una tabla con dos columnas, «competir» y «cooperar», y cuatro filas: «qué valor aparece», «qué pide hacer», «qué aporta» y «qué riesgo tiene». Escribe después qué propondrías al niño para cuidar ambos valores.",
           "Competir: valor: esforzarse por ganar; pide terminar primero; aporta motivación; riesgo: dejar a otros atrás. Cooperar: valor: ayuda mutua; pide ayudar a quien se atrasa; aporta que nadie quede atrás; riesgo: no avanzar al ritmo propio. Propuesta: que termine su tarea y luego ayude a quien se atrasa, y que le pregunte al profesor si el diploma puede ser también para quien ayudó.",
           ["usa las mismas filas para ambos valores", "reconoce aportes y riesgos de cada uno", "propone sin descartar un valor"], ["tabla de dos columnas y cuatro filas", "propuesta"], ["decir que uno es bueno y otro malo", "generalizar a todos los pueblos"],
           "Pedir que muestre que cada celda tiene un dato; valorar que la propuesta cuide ambos valores."),
    reinforce="Marca con un color los aportes y con otro los riesgos en tu tabla.",
    extend="Escribe qué cambiarías en el anuncio del profesor para que cuide ambos valores.",
)

L(
    OA13, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore la formación de una persona íntegra según una comunidad y la ponga en diálogo con otros sistemas de valores, con fuente, reflexión, límite y pregunta.",
    prior=["Sé reconocer tensiones entre valores.", "Sé leer un testimonio con límites."],
    explain=[
        "Una respuesta atribuida sobre la persona íntegra tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Gladys cuenta que…». Segundo, el valor que aparece. Tercero, la tensión o coincidencia con otros sistemas de valores. Cuarto, tu reflexión con «yo pienso que», más un límite. Quinto, una pregunta para el educador o la educadora tradicional.",
        "Valorar la formación de una persona íntegra según una comunidad es reconocer que esa concepción tiene sentido para quienes la viven y que puede enseñarnos algo. No significa que debamos copiarla ni que otros sistemas de valores sean peores. Podemos preguntarnos qué de esa concepción nos ayudaría en nuestra propia vida.",
        "Una buena respuesta no exagera, no pone en boca de la comunidad lo que no dijo y no generaliza a toda la sociedad global. Reconoce lo que no sabe y respeta lo que la comunidad reserva. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("valorar", "reconocer que algo tiene importancia y sentido para quienes lo viven"), ("coincidencia", "punto en que dos sistemas de valores piden algo parecido"), ("compromiso", "decisión propia de hacer algo que se considera importante"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TLD + " Arma una respuesta atribuida de cinco partes.", ["Dato: doña Gladys cuenta que una persona íntegra dice la verdad, ayuda en las tareas de todos y escucha antes de hablar.", "Valores: honestidad, ayuda mutua y respeto por la palabra del otro.", "Tensión: ella dice que a veces en la ciudad enseñan que lo importante es ganar.", "Reflexión y límite: yo pienso que escuchar antes de hablar ayuda a convivir; no sé cómo lo enseñan en otras familias; preguntaré al educador tradicional."], "Respuesta con dato atribuido, valores, tensión, reflexión con límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «La sociedad global no tiene valores y las comunidades indígenas sí». ¿Qué le falta a la respuesta?", ["No dice de qué fuente viene el dato.", "Generaliza y ordena en «con valores» y «sin valores».", "No tiene límite ni pregunta."], "Le falta atribuir, no jerarquizar y agregar límite y pregunta."),
    ],
    mistakes=[
        M("Decir que un sistema de valores no tiene valores.", "Todos los sistemas tienen valores, aunque sean distintos.", "Describe qué valores pone cada uno."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Gladys? A) «Todos saben que…» B) «Doña Gladys cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: la persona íntegra. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, valor, tensión, reflexión con límite y pregunta."),
        ex("Tema: la persona íntegra. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué significa valorar la formación de una persona íntegra según una comunidad? A) reconocer que tiene sentido para quienes la viven B) copiarla sin pensar", "A", "Valorar no es copiar."),
        ex("Verdadero o falso: valorar una concepción de la persona íntegra significa decir que los demás sistemas de valores son peores.", "Falso", "Se valora sin ordenar."),
        ex("Tema: la persona íntegra. ¿Para qué sirve la pregunta final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de doña Gladys: «Los niños aprenden mirando a los adultos». Completa la atribución: «Doña Gladys cuenta que los niños aprenden…»", "Mirando a los adultos", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Gladys cuenta que una persona íntegra escucha antes de hablar b) yo pienso que escuchar ayuda a no pelear.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Un compromiso personal dice: «Esta semana voy a cumplir lo que prometa y ayudar en una tarea de mi casa». ¿Qué dos valores practica? A) competir y acumular B) cumplir la palabra y ayuda mutua", "B", "El compromiso incluye cumplir lo prometido y ayudar."),
    ],
    Z=[
        ex("Tema: la persona íntegra. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar más datos inventados B) agregar lo que no sé o no se cuenta", "B", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque es una tarea de decoración B) porque conoce la formación de las personas en su pueblo y puede corregir errores", "B", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Gladys cuenta que los niños aprenden participando; yo pienso que eso los hace sentir parte de la comunidad». 2) «Doña Gladys demuestra que su forma de educar es la única buena». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega que en Loma Dorada «seguro hay una prueba para ser adulto». El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre qué significa ser una persona íntegra para la comunidad de Loma Dorada. ¿Qué empieza mejor? A) «Doña Gladys cuenta que…» B) «Todos los pueblos indígenas piensan que…»", "A", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre la persona íntegra.", "Dato de la fuente, valor, tensión o coincidencia, reflexión con límite y pregunta", "Están en la explicación."),
        ex("Tema: la persona íntegra. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: la persona íntegra. ¿Qué haces al terminar? A) guardarlo sin mostrarlo B) mostrarlo a la comunidad o al educador para que lo revise", "B", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Gladys: «En la sede aprendemos que quien se compromete, cumple. Si alguien no puede cumplir, avisa y pide ayuda. A veces en el colegio de la ciudad dicen que pedir ayuda es de débiles; nosotros decimos que pedir ayuda a tiempo es de personas responsables. Hay enseñanzas que damos solo a los jóvenes.» Escribe una respuesta de cinco partes: 1) dato de doña Gladys, 2) valor que aparece, 3) tensión con otro sistema de valores, 4) tu reflexión con «yo pienso que» y un límite, 5) una pregunta para el educador tradicional. Agrega un compromiso personal de una frase.",
           "1) Doña Gladys cuenta que quien se compromete, cumple, y que si no puede, avisa y pide ayuda. 2) Valor: responsabilidad. 3) A veces en el colegio de la ciudad dicen que pedir ayuda es de débiles. 4) Yo pienso que avisar a tiempo evita problemas; no sé qué piensan todos en la ciudad. 5) Pregunta: ¿cómo enseña mi pueblo a pedir ayuda? Compromiso: esta semana avisaré con tiempo si no puedo cumplir algo.",
           ["atribuye cada dato", "reconoce la tensión sin jerarquizar", "incluye límite, pregunta y compromiso"], ["texto de cinco partes", "compromiso personal"], ["generalizar a toda la ciudad", "no marcar la opinión propia"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu compromiso personal para que tenga una acción que puedas observar en una semana.",
)

# ------------------------------------------------------------------ OA 14
FCR = ("Ficha situada (inventada). Comunidad: Cerro Rojo (no es un pueblo real). Territorio: cerros con un barranco de greda y una feria cercana. "
       "Fuente y responsable: doña Olga, alfarera de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Olga autorizó usar esta ficha en la escuela. "
       "Límite: no se cuenta dónde está el barranco de greda que la comunidad cuida.")
TCR = ("Testimonio inventado de doña Olga, de Cerro Rojo: «Primero buscamos la greda en un barranco que la comunidad cuida. Después la limpiamos de piedritas y la amasamos con agua. "
       "Con las manos damos forma a las ollas y las dejamos secar a la sombra tres días. Al final las pulimos con una piedra suave y las cuece el horno de la comunidad. "
       "Cada semana hacemos 12 ollas; vendemos 8 en la feria y el resto lo guardamos para la comunidad. Mi madre me enseñó mirando.»")
TPL = ("Testimonio inventado de don Raúl, de Playa Larga: «Tejemos las redes con hilo resistente en invierno, cuando hay menos pesca. Primero se mide el hilo, luego se anudan las mallas una por una "
       "y al final se revisa que no queden agujeros. Cada red nos toma 5 días. Mi abuelo me enseñó a anudar. Hay lugares de pesca que cuidamos y no mostramos.»")
TTC = ("Testimonio inventado de doña Pilar, de un taller de carpintería de una ciudad: «Hacemos sillas. Primero se mide, luego se corta la madera con máquinas, se une y al final se lija. "
       "Cada silla nos toma 2 días. Aprendí en un curso y trabajo con tres compañeros.»")

L(
    OA14, 1, materials=MAT,
    use="Aprenderé a situar una técnica de producción: de qué comunidad es, quién la cuenta y qué no se cuenta. Sirve para valorar cómo distintas culturas elaboran lo que necesitan sin hablar por otros.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada comunidad cuenta su forma de vida a su manera."],
    explain=[
        "Una actividad de producción es una forma de obtener o elaborar lo que una comunidad necesita: alimentos, herramientas, ropa o vasijas. Una técnica es la manera de hacerlo, con pasos, materiales y conocimientos que se transmiten de unas personas a otras. La agricultura, la pesca, el tejido y la alfarería son actividades de producción que existen en muchas culturas.",
        "Las técnicas de un pueblo se relacionan con su territorio, porque usan lo que ese lugar ofrece, y con su forma de vida, porque se aprenden en la familia o en la comunidad. Valorarlas es reconocer los conocimientos que tienen detrás y el trabajo de las personas que las practican, y compararlas con las propias para ver semejanzas y diferencias.",
        "Antes de valorar una técnica hay que situarla. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es el relato y qué no se cuenta. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("actividad de producción", "forma de obtener o elaborar lo que una comunidad necesita"), ("técnica", "manera de hacer algo, con pasos, materiales y conocimientos"), ("alfarería", "elaboración de ollas y vasijas con greda u otro barro"), ("greda", "barro especial que sirve para modelar ollas y vasijas"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FCR + " ¿De quién es el relato y qué no se cuenta?", ["La comunidad es Cerro Rojo y la fuente es doña Olga.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuenta dónde está el barranco de greda."], "El relato es de doña Olga, de Cerro Rojo; no se cuenta dónde está el barranco de greda."),
        W("Reconocer una técnica", "Doña Olga amasa la greda, da forma a las ollas con las manos y las deja secar a la sombra. ¿Qué actividad y qué técnica son?", ["La actividad es elaborar ollas: alfarería.", "La técnica es el conjunto de pasos: amasar, modelar con las manos y secar.", "El material viene del territorio: la greda del barranco."], "La actividad es la alfarería y la técnica son sus pasos con greda del territorio."),
    ],
    mistakes=[
        M("Pensar que una técnica es solo el producto final.", "La técnica es la manera de hacerlo, con pasos y conocimientos.", "Mira los pasos y los materiales, no solo el resultado."),
        M("Decir que la técnica de Cerro Rojo es la de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según doña Olga, en Cerro Rojo…»."),
    ],
    R=[
        ex("Según la ficha de Cerro Rojo, ¿quién es la fuente?", "Doña Olga", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Cerro Rojo? A) cerros con un barranco de greda y una feria cercana B) una playa con redes", "A", "La playa y las redes son de otra comunidad."),
        ex("La ficha de Cerro Rojo dice que no se cuenta dónde está el barranco. ¿Lo ubicas en un mapa de tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es una técnica de producción? A) el nombre de un producto B) la manera de hacer algo, con pasos, materiales y conocimientos", "B", "La técnica incluye los pasos y los conocimientos."),
        ex("Verdadero o falso: la alfarería es la elaboración de ollas y vasijas con greda u otro barro.", "Verdadero", "Esa es la definición de alfarería."),
        ex("Verdadero o falso: la técnica de Cerro Rojo vale para todos los pueblos indígenas.", "Falso", "Cada pueblo tiene las suyas."),
    ],
    A=[
        ex("Clasifica en MATERIAL o PASO: a) la greda b) amasar con agua.", "a material, b paso", "La greda es lo que se usa; amasar es lo que se hace."),
        ex("Doña Olga dice: «Mi madre me enseñó mirando». ¿Cómo aprendió la técnica? A) en un curso escrito B) observando a su madre", "B", "La frase habla de aprender mirando."),
        arith("Doña Olga cuenta que cada semana hacen 12 ollas y venden 8 en la feria. ¿Cuántas ollas guardan para la comunidad?", "12-8", "Se restan las vendidas a las hechas."),
    ],
    Z=[
        ex("Pablo escribe: «Como Cerro Rojo hace ollas, todos los pueblos indígenas son alfareros». ¿Qué error comete?", "Generaliza una comunidad a todos los pueblos", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de valorar una técnica? A) para escribir más rápido B) porque cada comunidad la practica a su manera", "B", "Situar muestra de quién es la técnica."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Cerro Rojo. Actividad: alfarería». ¿Qué datos faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todas las comunidades aprenden mirando como doña Olga». ¿Qué corriges? A) escribo «según doña Olga (persona inventada), en Cerro Rojo…» B) lo dejo igual", "A", "El cartel debe atribuir el dato a esa fuente."),
    ],
    context=[ex("Un compañero quiere fotografiar a doña Olga trabajando, de una comunidad real, para su informe, sin avisar. ¿Qué haces? A) tomo la foto igual B) pido permiso a la persona y a la comunidad antes de usar su imagen", "B", "Las imágenes de personas y de su trabajo se usan con permiso.")],
    selfcheck=[
        ex("Nombra dos actividades de producción que existen en muchas culturas.", "Dos entre: agricultura, pesca, tejido, alfarería", "Son ejemplos de la explicación."),
        ex("Verdadero o falso: una técnica solo es el producto que se obtiene.", "Falso", "Incluye pasos, materiales y conocimientos."),
        ex("Ante una duda sobre una técnica de una comunidad real, ¿qué haces? A) la supongo B) pregunto al educador tradicional", "B", "Él o ella es la fuente."),
    ],
    task=T("Lee esta nota inventada de doña Olga: «En Cerro Rojo elaboramos ollas con greda. Primero la amasamos, luego damos forma con las manos y dejamos secar. Del lugar de la greda no hablamos con visitas.» Haz una ficha con: comunidad, actividad de producción, técnica (los pasos), fuente, qué dice la fuente y un límite. Luego escribe una frase con «Yo pienso que…» sobre qué conocimientos necesita esta técnica.",
           "Comunidad: Cerro Rojo. Actividad: alfarería. Técnica: amasar, dar forma con las manos y dejar secar. Fuente: doña Olga. Dice: elaboran ollas con greda. Límite: no se cuenta dónde está la greda. Yo pienso que esta técnica necesita saber cuánta agua poner y cuánto tiempo secar.",
           ["completa la ficha con datos de la nota", "separa la fuente de su opinión", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["inventar pasos que la nota no dice", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Cerro Rojo la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué una técnica se relaciona con el territorio donde vive la comunidad.",
)

L(
    OA14, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre una técnica de producción con límites declarados: qué dice la fuente, cuáles son los pasos, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar una técnica con su ficha.", "Sé distinguir material y paso."],
    explain=[
        "Un testimonio sobre una técnica cuenta pasos en orden, materiales, cantidades y cómo se aprendió. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. Los pasos, en el orden en que los cuenta. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de doña Olga, los pasos son: buscar la greda, limpiarla, amasarla, dar forma, dejar secar tres días, pulir y cocer en el horno de la comunidad. También cuenta una cantidad: cada semana hacen 12 ollas y venden 8. Pero no dice cuánto tarda cada olla ni dónde está el barranco. Si yo lo agrego, estoy inventando.",
        "Leer con límites declarados significa decir hasta dónde llega lo que afirmo. Si algo no se cuenta, escribo «el testimonio no lo dice». Y si queremos saber más sobre cómo trabaja un pueblo real, preguntamos al educador o a la educadora tradicional y pedimos permiso antes de mostrar su trabajo.",
    ],
    vocab=[("paso", "cada parte de una técnica, en un orden"), ("pulir", "dejar una superficie lisa frotándola"), ("cantidad", "cuánto hay o cuánto se hace de algo"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Ordenar los pasos", TCR + " Escribe los pasos en orden hasta el secado.", ["Primero buscan la greda en el barranco.", "Después la limpian de piedritas y la amasan con agua.", "Luego dan forma a las ollas con las manos.", "Por último las dejan secar tres días a la sombra."], "Buscar la greda, limpiarla y amasarla, dar forma con las manos y dejar secar tres días."),
        W("Detectar un agregado", "Un niño escribe: «Doña Olga cuenta que cada olla tarda una hora en hacerse». ¿Está bien?", ["Reviso el testimonio: dice cuántas ollas hacen por semana y que secan tres días.", "No dice cuánto tarda cada olla.", "El niño inventó un dato."], "No: inventó un tiempo que el testimonio no dice."),
    ],
    mistakes=[
        M("Cambiar el orden de los pasos.", "El orden es parte de la técnica.", "Copia los pasos en el orden que cuenta la fuente."),
        M("Agregar tiempos o cantidades que la fuente no dio.", "Se inventan datos.", "Escribe «el testimonio no lo dice»."),
    ],
    R=[
        ex("Según doña Olga, ¿cuántos días se dejan secar las ollas a la sombra?", "Tres días", "El testimonio lo dice así."),
        ex("Tema: las técnicas de producción. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no dice cuánto tarda cada olla, ¿qué escribes? A) el testimonio no lo dice B) tarda una hora", "A", "No se inventan datos."),
    ],
    C=[
        ex("Verdadero o falso: el orden de los pasos de una técnica es parte de lo que cuenta la fuente.", "Verdadero", "Cambiarlo cambia la técnica."),
        ex("En el testimonio de doña Olga, ¿qué viene primero? A) pulir las ollas B) buscar la greda", "B", "Primero se busca la greda."),
        ex("Verdadero o falso: puedo agregar un tiempo probable si la fuente no lo dio.", "Falso", "Eso sería inventar un dato."),
    ],
    A=[
        ex("Ordena los pasos de las ollas, de primero a último: A) pulir con una piedra B) amasar la greda C) dar forma con las manos. Escribe las letras en orden.", "B, C, A", "Primero se amasa, luego se modela y después se pule."),
        arith("En la primera semana hacen 12 ollas y venden 8; en la segunda hacen 12 y venden 9. ¿Cuántas ollas guardan en total en las dos semanas?", "(12-8)+(12-9)", "Se calculan las ollas guardadas cada semana y se suman."),
        ex("Clasifica en DICE LA FUENTE o INTERPRETO: a) secan las ollas tres días a la sombra b) secarlas a la sombra evita que se rompan.", "a dice la fuente, b interpreto", "La razón no está en el testimonio."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «El barranco de greda está cerca de la feria». ¿Qué debería hacer con esa frase?", "Quitarla porque la ubicación es un límite de la ficha", "La ficha dice que no se cuenta dónde está."),
        ex("Tema: las técnicas de producción. ¿Por qué conviene escribir los límites al final del trabajo? A) para llenar la hoja B) para mostrar hasta dónde llega lo afirmado", "B", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        arith("En 4 semanas, ¿cuántas ollas hacen en Cerro Rojo, si cada semana hacen 12?", "4*12", "Se multiplica ollas por semana por número de semanas."),
        ex("Dos frases. 1) «Doña Olga cuenta que la cuece el horno de la comunidad». 2) «Doña Olga cuenta que el horno es sagrado». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no contiene."),
    ],
    context=[ex("Para un informe escolar, un compañero quiere escribir paso a paso «cómo se hace una olla» con datos que sacó de su imaginación. ¿Qué le dices? A) que complete con lo probable B) que use solo los pasos que cuenta la fuente y marque lo que no sabe", "B", "No se inventan pasos que la fuente no cuenta.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre una técnica.", "Lo que dice la fuente, los pasos, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: las técnicas de producción. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: las técnicas de producción. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Olga: «Para las vasijas pequeñas usamos la misma greda. Las modelamos con las manos y las dejamos secar dos días. Mi hija me ayuda a pulirlas. Hacemos 10 por semana y vendemos 6. Del lugar de la greda no hablamos con visitas.» Haz cuatro columnas: «La fuente dice», «Pasos» (en orden), «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: usan la misma greda, secan dos días, su hija ayuda a pulir, hacen 10 por semana y venden 6. Pasos: modelar con las manos, secar dos días, pulir. Yo interpreto: yo pienso que ayudar a pulir es una forma de aprender. No se cuenta: dónde está la greda. Límite: no sé cuánto tarda cada vasija.",
           ["separa cuatro columnas", "ordena los pasos como los cuenta la fuente", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["cambiar el orden de los pasos", "inventar lo reservado"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Numera los pasos del testimonio con 1, 2 y 3 antes de pasarlos a la tabla.",
    extend="En la actividad abierta, doña Olga hace 10 vasijas y vende 6: calcula cuántas guarda por semana y explica con una frase qué podría hacer la comunidad con ellas, marcándolo como tu idea.",
)

L(
    OA14, 3, materials=MAT,
    use="Aprenderé a reconocer semejanzas y diferencias entre técnicas de producción de dos comunidades y de una cultura de ciudad, y con las mías, sin decir que una técnica es mejor.",
    prior=["Sé leer un testimonio con límites.", "Sé ordenar los pasos de una técnica."],
    explain=[
        "Comparar técnicas de producción es mirarlas con los mismos criterios: qué material usan, qué pasos tienen, cuánto producen, quién enseña y para qué sirve lo que producen. Esta comparación nos ayuda a ver que personas distintas resuelven necesidades parecidas de maneras diferentes, según su territorio y su cultura.",
        "Comparamos tres testimonios inventados: la alfarería de Cerro Rojo, las redes de pesca de Playa Larga y una carpintería de ciudad. En los tres hay pasos en orden, se produce algo útil y alguien enseña. Pero los materiales cambian: greda, hilo y madera. Y también cambia cómo se aprende: mirando a la madre, con el abuelo o en un curso.",
        "Para valorar una técnica también la comparamos con las propias, es decir, con técnicas que usamos en nuestra familia o en nuestro pueblo. No decimos que una sea más avanzada que otra. Y tres testimonios no representan a todos los pueblos ni a todas las ciudades.",
    ],
    vocab=[("criterio", "punto de comparación igual para todas las técnicas"), ("semejanza", "algo parecido entre dos técnicas"), ("diferencia", "algo distinto entre dos técnicas"), ("material", "lo que se usa para hacer algo"), ("técnica propia", "técnica que se practica en tu familia o en tu pueblo")],
    worked=[
        W("Comparar con un criterio", TCR + " " + TPL + " Criterio: «cómo aprendieron». Doña Olga: mirando a su madre. Don Raúl: con su abuelo. ¿Qué semejanza hay?", ["Doña Olga aprendió de su madre.", "Don Raúl aprendió de su abuelo.", "Los dos aprendieron de una persona de su familia."], "Semejanza: los dos aprendieron la técnica de una persona de su familia."),
        W("Comparar con una técnica propia", "Ejemplo inventado: Camila, una niña de ciudad, sabe plantar una semilla en un vaso de tierra y regarla cada dos días. Compara con las ollas de doña Olga: ¿qué semejanza y qué diferencia hay en el material?", ["Camila usa tierra y semilla; doña Olga usa greda.", "Ambas toman un material de la naturaleza.", "Pero los materiales son distintos."], "Semejanza: ambas usan un material de la naturaleza. Diferencia: tierra y semilla frente a greda."),
    ],
    mistakes=[
        M("Decir que una técnica es más avanzada que otra.", "Comparar no es ordenar de más a menos avanzada.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todos los pueblos aprenden igual porque dos testimonios se parecen.", "Dos ejemplos no representan a todos los pueblos.", "Escribe «en estos testimonios» y no más."),
    ],
    R=[
        ex("¿Qué material usa don Raúl, de Playa Larga, para hacer las redes: hilo resistente o greda?", "Hilo resistente", "La greda es de Cerro Rojo."),
        ex("¿Cómo aprendió doña Pilar su técnica: en un curso o mirando a su abuelo?", "En un curso", "Así lo dice su testimonio."),
        ex("Según don Raúl, de Playa Larga, ¿cuántos días toma cada red?", "5", "Es el dato del testimonio."),
    ],
    C=[
        ex("Verdadero o falso: comparar técnicas significa decir cuál es más avanzada.", "Falso", "Comparar es buscar semejanzas y diferencias."),
        ex("¿Qué es un criterio de comparación? A) la opinión de quien compara B) un punto igual para todas las técnicas, como «qué material usan»", "B", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: si dos técnicas se parecen, todos los pueblos trabajan igual.", "Falso", "Dos casos no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «qué material usan». Cerro Rojo: greda. Playa Larga: hilo resistente. Taller de ciudad: madera. ¿Qué diferencia hay? A) cada técnica usa un material distinto B) todas usan el mismo material", "A", "Los tres materiales son distintos."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) las tres técnicas tienen pasos en orden b) una dura 2 días por silla y otra 5 días por red.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        arith("Una red de Playa Larga toma 5 días y una silla del taller, 2 días. ¿Cuántos días más toma una red que una silla?", "5-2", "Se resta el tiempo de la silla al de la red."),
    ],
    Z=[
        ex("Ana dice: «La carpintería de ciudad es una técnica más avanzada que la alfarería de Cerro Rojo». ¿Qué falla en su comparación?", "Ordena técnicas sin criterio ni fuente", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como en estos testimonios alguien enseña a alguien, todos los pueblos enseñan igual». ¿Qué debería escribir? A) «en estos tres testimonios» B) «en todos los pueblos»", "A", "Tres testimonios no representan a todos los pueblos."),
    ],
    D=[
        arith("Si el taller de ciudad hace una silla cada 2 días, ¿cuántas sillas hace en 10 días?", "10//2", "Se divide el total de días por los días de cada silla."),
        ex("Dos conclusiones. 1) «En estos tres testimonios, las personas usan materiales distintos para producir algo útil». 2) «Las técnicas indígenas son más antiguas y por eso menos útiles». ¿Cuál está bien formulada?", "La primera", "La segunda ordena sin datos."),
    ],
    context=[ex("Tu curso arma un panel de técnicas de producción. Una compañera quiere agregar la técnica de su abuela, de su propio pueblo, pero no sabe si puede mostrarla. ¿Qué hace primero? A) mostrarla sin avisar B) preguntar a su abuela y al educador tradicional qué se puede compartir", "B", "Lo propio de una familia o pueblo se comparte con su permiso.")],
    selfcheck=[
        ex("Nombra dos criterios para comparar técnicas de producción.", "Dos entre: material, pasos, cantidad, quién enseña, para qué sirve", "Son los criterios de la explicación."),
        ex("Tema: las técnicas de producción. Verdadero o falso: puedo ordenar tres técnicas de más a menos avanzada.", "Falso", "Cada técnica responde a su territorio y cultura."),
        ex("Verdadero o falso: una técnica de mi familia también puede compararse con las de otras comunidades usando criterios iguales.", "Verdadero", "Los criterios iguales sirven para comparar cualquier técnica."),
    ],
    task=T("Compara estas tres técnicas inventadas. Cerro Rojo: «amasamos greda, damos forma con las manos, secamos tres días, pulimos y cocemos». Playa Larga: «medimos el hilo, anudamos las mallas y revisamos que no haya agujeros». Taller de ciudad: «medimos, cortamos la madera, unimos y lijamos». Haz una tabla con tres criterios: «qué material usan», «cuántos pasos cuentan» y «qué producen». Escribe una semejanza, una diferencia y, al final, una técnica de tu casa (por ejemplo, plantar una semilla en un vaso con tierra) comparada con una de ellas.",
           "Material: greda; hilo; madera. Pasos: 5; 3; 4. Producen: ollas; redes; sillas. Semejanza: las tres tienen pasos en orden y producen algo útil. Diferencia: cada una usa un material distinto. Técnica de mi casa: plantar una semilla usa tierra y agua, como la greda necesita agua; la diferencia es que la semilla crece y la greda se modela.",
           ["usa los mismos criterios para las tres", "distingue semejanza y diferencia", "compara con una técnica propia"], ["tabla de tres criterios", "comparación con técnica propia"], ["decir cuál técnica es mejor", "generalizar a todos los pueblos"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que no ordene las técnicas."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «cuánto tiempo toma cada producto») y completa con los datos de los tres testimonios.",
)

L(
    OA14, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore una técnica de producción, considerando semejanzas y diferencias con las propias, con fuente, reflexión, límite y pregunta.",
    prior=["Sé comparar técnicas con criterios iguales.", "Sé leer un testimonio con límites."],
    explain=[
        "Una respuesta atribuida que valora una técnica de producción tiene cinco partes. Primero, el dato de la fuente con su nombre: «Don Raúl cuenta que…». Segundo, la técnica: material, pasos y cómo se aprendió. Tercero, una semejanza y una diferencia con una técnica propia. Cuarto, tu reflexión con «yo pienso que» y un límite. Quinto, una pregunta para el educador o la educadora tradicional.",
        "Valorar una técnica es reconocer el conocimiento que hay detrás de ella: saber qué material usar, cuánto esperar y cómo cuidar el lugar de donde se saca. Valorar no es lo mismo que copiar: muchas técnicas y sus lugares pertenecen a la comunidad y se miran con respeto, sin reproducirlas ni mostrarlas sin permiso.",
        "Una buena respuesta no exagera, no inventa pasos y no habla por todo un pueblo. Reconoce lo que no sabe y respeta lo que la comunidad reserva. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("valorar", "reconocer que algo tiene importancia y sentido para quienes lo viven"), ("conocimiento", "saber que se aprende y se transmite"), ("técnica propia", "técnica que se practica en tu familia o en tu pueblo"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TPL + " Arma una respuesta atribuida de cinco partes.", ["Dato: don Raúl cuenta que tejen las redes en invierno, cuando hay menos pesca.", "Técnica: mide el hilo, anuda las mallas y revisa que no haya agujeros; aprendió con su abuelo.", "Semejanza y diferencia con una técnica propia: como al plantar una semilla, se sigue un orden de pasos; pero el material es el hilo.", "Reflexión y pregunta: yo pienso que aprovechar el invierno ordena el trabajo del año; no sé cómo eligen el hilo; preguntaré al educador tradicional."], "Respuesta con dato atribuido, técnica, comparación con una propia, reflexión con límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «La técnica de las redes es primitiva». ¿Qué le falta a la respuesta?", ["«Primitiva» es un juicio sin fuente.", "No describe materiales ni pasos.", "No tiene límite ni pregunta."], "Le falta describir con la fuente, no jerarquizar y agregar límite y pregunta."),
    ],
    mistakes=[
        M("Usar palabras como «primitivo» o «atrasado» para una técnica.", "Son juicios que ordenan culturas sin conocerlas.", "Describe materiales, pasos y conocimientos."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a don Raúl? A) «Todos saben que…» B) «Don Raúl cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: las técnicas de producción. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, técnica, comparación con una propia, reflexión con límite y pregunta."),
        ex("Tema: las técnicas de producción. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué significa valorar una técnica de producción? A) copiarla sin permiso B) reconocer el conocimiento que hay detrás", "B", "Valorar no es copiar."),
        ex("Verdadero o falso: valorar una técnica significa decir que es más avanzada que las demás.", "Falso", "Se valora sin ordenar."),
        ex("Tema: las técnicas de producción. ¿Para qué sirve la pregunta final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de don Raúl: «Mi abuelo me enseñó a anudar». Completa la atribución: «Don Raúl cuenta que su abuelo le enseñó a…»", "Anudar", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) don Raúl cuenta que cada red toma 5 días b) yo pienso que 5 días es poco para una red tan grande.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        arith("Don Raúl cuenta que cada red toma 5 días. Si tejen 3 redes, ¿cuántos días necesitan en total?", "3*5", "Se multiplica el número de redes por los días de cada una."),
    ],
    Z=[
        ex("Tema: las técnicas de producción. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque conoce las técnicas de su pueblo y puede corregir errores B) porque es una tarea de decoración", "A", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Don Raúl cuenta que teje redes en invierno; yo pienso que así aprovecha el tiempo con menos pesca». 2) «Don Raúl demuestra que su técnica es la mejor del mundo». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega que en Playa Larga «seguro usan un tipo de nudo especial». El testimonio no lo menciona. ¿Qué debe hacer?", "Quitarlo porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre la técnica de las redes de Playa Larga. ¿Qué empieza mejor? A) «Don Raúl cuenta que…» B) «Todos los pueblos indígenas tejen redes de…»", "A", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre una técnica de producción.", "Dato de la fuente, técnica, comparación con una propia, reflexión con límite y pregunta", "Están en la explicación."),
        ex("Tema: las técnicas de producción. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: las técnicas de producción. ¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) guardarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Olga: «En Cerro Rojo hacemos ollas con greda. Las dejamos secar tres días. Cada semana hacemos 12 y vendemos 8 en la feria; el resto lo guardamos para la comunidad. Mi madre me enseñó mirando. Del lugar de la greda no hablamos con visitas.» Escribe una respuesta de cinco partes: 1) dato de doña Olga, 2) la técnica (material, pasos y cómo aprendió), 3) una semejanza y una diferencia con una técnica de tu casa, 4) tu reflexión con «yo pienso que» y un límite, 5) una pregunta para el educador tradicional.",
           "1) Doña Olga cuenta que hacen ollas con greda, las dejan secar tres días y hacen 12 por semana. 2) Material: greda; pasos: secar tres días; aprendió mirando a su madre. 3) Como al plantar una semilla en un vaso, se espera un tiempo; la diferencia es que la greda se modela y la semilla crece. 4) Yo pienso que guardar ollas para la comunidad muestra que el trabajo es compartido; no sé cuánto tarda cada olla. 5) Pregunta: ¿cómo aprenden las técnicas en mi pueblo?",
           ["atribuye cada dato", "compara con una técnica propia sin jerarquizar", "incluye límite y pregunta"], ["texto de cinco partes"], ["usar «primitivo» o «atrasado»", "inventar pasos"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu respuesta con el testimonio de don Raúl y las redes de Playa Larga.",
)

L(
    OA14, 5, materials=MAT,
    use="Aprenderé a contrastar sin jerarquizar técnicas de producción de comunidades y culturas distintas, y a no usar palabras como «primitivo» o «atrasado».",
    prior=["Sé armar una respuesta atribuida.", "Sé comparar técnicas con criterios iguales."],
    explain=[
        "Contrastar es poner varias técnicas una al lado de otra para ver en qué coinciden y en qué se diferencian. Sin jerarquizar quiere decir que no las ordenamos de «más avanzada» a «menos avanzada». Cada técnica resuelve una necesidad con los materiales, el territorio y los conocimientos de quienes la practican.",
        "Un error frecuente es usar palabras como «primitivo» o «atrasado» para hablar de técnicas de pueblos indígenas, o «moderno» como si fuera siempre mejor. Esas palabras juzgan sin mirar los conocimientos que hay detrás. Para evitarlas describimos qué hace la técnica, qué materiales usa y qué problema resuelve.",
        "Contrastar sin jerarquizar no impide reconocer que algunas técnicas usan máquinas y otras, manos. Solo pide describir cada una con los mismos criterios y con respeto. Y tres testimonios no representan a todos los pueblos ni a todas las ciudades.",
    ],
    vocab=[("contrastar", "poner varias técnicas juntas para ver en qué coinciden y en qué se diferencian"), ("jerarquizar", "ordenar de más a menos avanzado o importante"), ("primitivo", "palabra que juzga una técnica como poco desarrollada sin conocerla"), ("criterio", "punto de comparación igual para todas las técnicas"), ("problema que resuelve", "necesidad a la que responde una técnica")],
    worked=[
        W("Contrastar tres técnicas", "Cerro Rojo: ollas de greda, para cocinar y guardar. Playa Larga: redes de hilo, para pescar. Taller de ciudad: sillas de madera, para sentarse. Criterio: «qué problema resuelve». ¿En qué coinciden?", ["Cerro Rojo resuelve cómo cocinar y guardar.", "Playa Larga resuelve cómo pescar.", "El taller resuelve dónde sentarse.", "Las tres resuelven una necesidad cotidiana."], "Coinciden en que las tres resuelven una necesidad cotidiana."),
        W("Evitar una palabra que jerarquiza", "Un niño dice: «Las redes de Playa Larga son una técnica primitiva». ¿Qué puede decir en su lugar?", ["«Primitiva» juzga sin mirar los conocimientos.", "Puede describir: se mide el hilo, se anudan las mallas y se revisa que no haya agujeros.", "Así explica la técnica sin ordenarla."], "Puede describir los pasos y los conocimientos de la técnica en vez de usar «primitiva»."),
    ],
    mistakes=[
        M("Usar «primitivo» o «atrasado» para una técnica indígena.", "Son juicios que ordenan culturas sin conocerlas.", "Describe materiales, pasos y conocimientos."),
        M("Pensar que contrastar significa decir que todas las técnicas son iguales.", "Cada una tiene sus propios materiales y sentidos.", "Compara con criterios iguales y anota semejanzas y diferencias."),
    ],
    R=[
        ex("¿Qué problema resuelven las redes de Playa Larga: pescar o sentarse?", "Pescar", "Sentarse corresponde a las sillas del taller."),
        ex("Contrastar, ¿es poner técnicas juntas para ver coincidencias y diferencias o es elegir la más avanzada?", "Poner técnicas juntas para ver coincidencias y diferencias", "Contrastar no es elegir la más avanzada."),
        ex("¿Qué material usa el taller de ciudad: madera o greda?", "Madera", "La greda es de Cerro Rojo."),
    ],
    C=[
        ex("Verdadero o falso: llamar «primitiva» a una técnica ayuda a describirla.", "Falso", "Es un juicio que no describe."),
        ex("¿Por qué se usan criterios iguales para las tres técnicas? A) para no tratar a una mejor que otra B) para llenar la tabla", "A", "Los criterios iguales evitan el trato desigual."),
        ex("Verdadero o falso: tres testimonios bastan para describir las técnicas de todos los pueblos.", "Falso", "Tres testimonios no representan a todos."),
    ],
    A=[
        ex("Criterio: «cómo se hace el producto». Cerro Rojo: con las manos. Taller de ciudad: con máquinas para cortar. ¿Qué diferencia hay? A) usan herramientas distintas B) usan las mismas herramientas", "A", "Una usa las manos y la otra, máquinas."),
        ex("Clasifica en COINCIDENCIA o DIFERENCIA: a) las tres técnicas responden a una necesidad cotidiana b) una usa greda, otra hilo y otra madera.", "a coincidencia, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Un joven dice: «Las ollas son más antiguas, entonces valen menos que las sillas». ¿Qué falla? A) ordena sin criterio ni fuente B) usa el nombre de ambas", "A", "Contrastar no es jerarquizar."),
    ],
    Z=[
        ex("Ana dice: «La alfarería de Cerro Rojo es atrasada». ¿Qué frase la describe sin jerarquizar? A) «Es una técnica de otros tiempos» B) «Usa greda, se modela con las manos y se seca tres días»", "B", "La primera describe materiales y pasos sin juzgar."),
        ex("Un compañero concluye: «Todas las técnicas indígenas se hacen con las manos». ¿Qué debería escribir? A) «en todos los pueblos» B) «en este testimonio, la alfarería de Cerro Rojo se modela con las manos»", "B", "Un testimonio no representa a todos los pueblos."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos tres testimonios, cada técnica usa un material distinto para resolver una necesidad cotidiana». 2) «Las técnicas con máquinas son mejores que las de manos». ¿Cuál está bien formulada?", "La primera", "La segunda ordena sin criterio."),
        ex("Un grupo quiere aprender la técnica de una comunidad real para vender productos. ¿Qué debe hacer primero? A) copiarla de internet B) pedir permiso y consultar al educador tradicional y a la comunidad", "B", "Las técnicas de una comunidad se aprenden y usan con su permiso."),
    ],
    context=[ex("En una feria escolar alguien dice: «Aquí mostramos técnicas modernas y técnicas antiguas, para ver cuáles son mejores». ¿Qué cambio respeta lo aprendido? A) «mostramos distintas técnicas para conocer sus materiales y sus pasos» B) dejar la frase", "A", "La frase A describe sin jerarquizar.")],
    selfcheck=[
        ex("Escribe una palabra que no debes usar para describir una técnica indígena.", "Primitiva o atrasada", "Son juicios sin descripción."),
        ex("Tema: las técnicas de producción. Verdadero o falso: al contrastar, puedo clasificar las tres técnicas de la menos a la más avanzada.", "Falso", "Contrastar no es jerarquizar."),
        ex("Nombra un criterio de contraste para tres técnicas.", "Por ejemplo: qué problema resuelve", "Debe ser un punto igual para todas."),
    ],
    task=T("Contrasta estas tres técnicas inventadas. Cerro Rojo: «amasamos greda, modelamos con las manos, secamos y pulimos; hacemos ollas para cocinar y guardar». Playa Larga: «medimos el hilo, anudamos las mallas y revisamos; hacemos redes para pescar». Taller de ciudad: «medimos, cortamos la madera con máquinas, unimos y lijamos; hacemos sillas para sentarse». Haz una tabla con tres criterios: «con qué herramientas», «qué problema resuelve» y «cómo se aprende» (si no lo dice, escribe «no lo dice»). Escribe una coincidencia, una diferencia y una frase que explique cómo describirías una de ellas sin usar «primitiva» ni «moderna».",
           "Herramientas: manos; no lo dice; máquinas para cortar la madera. Problema: cocinar y guardar; pescar; sentarse. Cómo se aprende: no lo dice; no lo dice; no lo dice. Coincidencia: las tres resuelven una necesidad cotidiana con pasos en orden. Diferencia: una usa máquinas para cortar y otra, las manos para modelar. Describiría las redes diciendo que se mide el hilo, se anudan las mallas y se revisa que no haya agujeros.",
           ["usa los mismos criterios para las tres", "distingue coincidencia y diferencia", "describe sin jerarquizar"], ["tabla de tres criterios", "coincidencia, diferencia y frase"], ["usar «primitiva»", "inventar cómo se aprende"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que escriba «no lo dice» donde corresponda."),
    reinforce="Marca en la tabla con un color las coincidencias y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «quién usa el producto») y explica qué deberías preguntar para completarlo.",
)
