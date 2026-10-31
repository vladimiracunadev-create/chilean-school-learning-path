"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 17 (lenguajes artísticos propios de su pueblo y diálogo con otras culturas).

Las comunidades, personas, obras y testimonios son INVENTADOS y se rotulan así; no se describe ningún arte, símbolo,
canto ni danza de un pueblo real. Las tareas abiertas piden consultar al educador o a la educadora tradicional del
pueblo del propio estudiante y crear una expresión propia, sin reproducir lo que la comunidad guarda.
"""
from __future__ import annotations

from student_content_lc6_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA17 = "LC06 OA 17"

FQF = ("Ficha situada (inventada). Comunidad: Quebrada Florida (no es un pueblo real). Territorio: una quebrada con huertos, una sede y un camino hacia la ciudad. "
       "Fuente y responsable: doña Rosario, tejedora de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Rosario autorizó usar esta ficha en la escuela. "
       "Límite: no se cuenta el significado de los dibujos del tejido que la comunidad reserva.")
TQF = ("Testimonio inventado de doña Rosario, de Quebrada Florida: «Cuando tejo, pienso en mi abuela, que me enseñó los dibujos. Cada dibujo de nuestro tejido tiene un sentido que la comunidad conoce; no todos se cuentan. "
       "Una vez expusimos tejidos en la ciudad, con nuestro nombre y una explicación. Una niña dibujó lo que sintió al verlos, y eso me emocionó.»")
TBS = ("Testimonio inventado de Matías, de Barrio Sur (barrio de una ciudad, no indígena): «Con los vecinos pintamos un mural en el muro de la plaza. Cada familia dibujó algo de su historia. "
       "Pedimos permiso al dueño del muro y firmamos todos al final.»")
TCE = ("Testimonio inventado de la profesora Elena, de una escuela de ciudad: «Mi curso canta en un coro. Una vez invitamos a un artista de una comunidad a conversar sobre su música. "
       "Pidió que no grabáramos ciertas partes, y lo respetamos. Después compusimos una canción propia inspirada en su charla, y dijimos que era nuestra.»")

L(
    OA17, 1, materials=MAT,
    use="Aprenderé a situar un lenguaje artístico: de qué comunidad es, quién lo cuenta y qué no se cuenta. Sirve para entender cómo el arte de un pueblo puede dialogar con otras culturas sin que nadie hable por otros.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada pueblo tiene formas propias de expresarse."],
    explain=[
        "Un lenguaje artístico es una forma de expresar ideas y sentimientos con recursos propios del arte. Hay lenguajes visuales (dibujo, pintura, tejido), sonoros (música y canto), corporales (danza y teatro), literarios y orales (poemas, relatos). Cada pueblo tiene lenguajes artísticos propios, que se aprenden en la familia y en la comunidad y que no siempre se parecen a los de otros pueblos.",
        "El arte tiene un sentido para quienes lo crean: puede recordar a los antepasados, agradecer, enseñar, expresar la identidad o simplemente embellecer la vida. Ese sentido lo define la comunidad. Cuando un arte se comparte con otras culturas, puede abrir un diálogo: personas distintas se conocen, se emocionan y responden con su propia expresión. Pero el diálogo es respetuoso solo si hay permiso y se reconoce a quien creó la obra.",
        "Antes de conversar con el arte de una comunidad hay que situarlo. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es el relato y qué no se cuenta. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("lenguaje artístico", "forma de expresar ideas y sentimientos con recursos del arte, como el dibujo, la música o la danza"), ("sentido", "lo que algo significa para quienes lo crean"), ("diálogo", "intercambio respetuoso en que cada parte escucha y responde"), ("autoría", "reconocimiento de quién creó una obra"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FQF + " ¿De quién es el relato y qué no se cuenta?", ["La comunidad es Quebrada Florida y la fuente es doña Rosario.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuenta el significado reservado de los dibujos del tejido."], "El relato es de doña Rosario, de Quebrada Florida; no se cuenta el significado reservado de los dibujos."),
        W("Reconocer un lenguaje y un sentido", "Doña Rosario teje y dice: «Pienso en mi abuela, que me enseñó los dibujos». ¿Qué lenguaje artístico y qué sentido aparecen?", ["Tejer con dibujos es un lenguaje visual y textil.", "Pensar en su abuela muestra un sentido de memoria familiar.", "Así, el tejido une arte y memoria."], "Lenguaje: textil y visual. Sentido: memoria de su abuela."),
    ],
    mistakes=[
        M("Pensar que el arte de un pueblo es solo adorno.", "Tiene un sentido que define la comunidad.", "Pregunta qué significa para quienes lo crean."),
        M("Decir que el arte de Quebrada Florida es el arte de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según doña Rosario, en Quebrada Florida…»."),
    ],
    R=[
        ex("Según la ficha de Quebrada Florida, ¿quién es la fuente?", "Doña Rosario", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Quebrada Florida? A) una quebrada con huertos, una sede y un camino a la ciudad B) un puerto y una caleta", "A", "El puerto y la caleta son de otras fichas."),
        ex("La ficha de Quebrada Florida dice que no se cuenta el significado reservado de los dibujos. ¿Lo inventas para completar tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es un lenguaje artístico? A) un idioma extranjero B) una forma de expresar ideas y sentimientos con recursos del arte", "B", "El arte tiene lenguajes como dibujo, música y danza."),
        ex("Verdadero o falso: el sentido de un arte lo define la comunidad que lo crea.", "Verdadero", "Es ella quien sabe qué significa."),
        ex("Verdadero o falso: el arte de Quebrada Florida sirve para hablar de todos los pueblos indígenas.", "Falso", "Una comunidad no representa a todos los pueblos."),
    ],
    A=[
        ex("Clasifica en VISUAL, SONORO o CORPORAL: a) un tejido con dibujos b) un canto en coro c) una danza.", "a visual, b sonoro, c corporal", "Cada lenguaje usa un recurso distinto."),
        ex("Doña Rosario dice: «Expusimos tejidos en la ciudad, con nuestro nombre y una explicación». ¿Qué cuidado muestra? A) reconocer la autoría de la comunidad B) ocultar quién los hizo", "A", "Poner el nombre reconoce a quienes los crearon."),
        ex("Tema: el arte y el diálogo. Una compañera trae una ficha con comunidad y fuente, pero sin permiso. ¿Qué falta? A) el color del papel B) la autorización de la fuente para compartir", "B", "El permiso es parte de una ficha situada."),
    ],
    Z=[
        ex("Pablo escribe: «Como Quebrada Florida teje, todos los pueblos indígenas tejen». ¿Qué error comete?", "Generaliza una comunidad a todos los pueblos", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de dialogar con un arte? A) para escribir más rápido B) porque cada comunidad define el sentido de su arte", "B", "Situar muestra de quién es el arte."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Quebrada Florida. Arte: tejido». ¿Qué datos faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todos los pueblos expresan su memoria en tejidos, como en Quebrada Florida». ¿Qué corriges? A) lo dejo igual B) escribo «según doña Rosario (persona inventada), en Quebrada Florida…»", "B", "El cartel debe atribuir el dato a esa fuente."),
    ],
    context=[ex("En una exposición escolar, un compañero quiere copiar el dibujo de un tejido de una comunidad real y firmarlo como suyo. ¿Qué haces? A) le explico que debe pedir permiso y reconocer a la comunidad, o crear algo propio B) lo dejo, porque es solo un dibujo", "A", "Copiar y firmar como propio es apropiación.")],
    selfcheck=[
        ex("Nombra dos lenguajes artísticos de esta clase.", "Dos entre: visual, sonoro, corporal, literario u oral", "Son los lenguajes de la explicación."),
        ex("Verdadero o falso: dialogar con el arte de otra cultura exige permiso y reconocer a quien lo creó.", "Verdadero", "Es la base del diálogo respetuoso."),
        ex("Ante una duda sobre el arte de una comunidad real, ¿qué haces? A) pregunto al educador tradicional B) lo supongo", "A", "Él o ella es la fuente."),
    ],
    task=T("Lee esta nota inventada de doña Rosario: «En Quebrada Florida tejemos con lana teñida con colores de la quebrada. Los dibujos nos los enseñaron los mayores y tienen sentidos que no siempre contamos. Cuando exponemos, ponemos nuestro nombre.» Haz una ficha con: comunidad, fuente, lenguaje artístico, qué dice la fuente, un sentido que aparezca y un límite. Luego escribe una frase con «Yo pienso que…» sobre qué puede aprender una persona de otra cultura al ver un tejido como ese.",
           "Comunidad: Quebrada Florida. Fuente: doña Rosario. Lenguaje: tejido visual y textil. Dice: tejen con lana teñida con colores de la quebrada y los dibujos los enseñaron los mayores; al exponer ponen su nombre. Sentido: memoria y enseñanza de los mayores. Límite: no se cuentan los sentidos reservados. Yo pienso que una persona de otra cultura puede aprender que un tejido guarda la memoria de la comunidad.",
           ["completa la ficha con datos de la nota", "separa la fuente de su opinión", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["inventar el significado de los dibujos", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Quebrada Florida la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué poner el nombre de quienes crearon una obra es parte de un diálogo respetuoso.",
)

L(
    OA17, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre arte con límites declarados: qué dice la fuente, qué lenguaje y qué sentido muestra, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar un arte con su ficha.", "Sé distinguir un lenguaje artístico de su sentido."],
    explain=[
        "Un testimonio sobre arte cuenta qué se crea, con qué recursos, para qué y cómo se comparte. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. El lenguaje artístico y el sentido que muestra. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de doña Rosario, tejer es un lenguaje textil y visual, y pensar en su abuela muestra un sentido de memoria. Ella dice que los dibujos tienen sentidos que la comunidad conoce y que no todos se cuentan. Si yo invento qué significa un dibujo, estoy atribuyendo a la comunidad algo que no dijo y, además, rompo el límite que ella puso.",
        "También cuenta un diálogo: una niña dibujó lo que sintió al ver los tejidos. Esa respuesta es de la niña, no de la comunidad. Leer con límites declarados es distinguir ambas voces. Para saber más sobre el arte de un pueblo real, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("recurso", "material o medio que se usa para crear, como lana, voz o color"), ("sentido", "lo que algo significa para quienes lo crean"), ("respuesta artística", "obra que alguien crea en respuesta a otra, con su propia voz"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TQF + " Separa lo que dice, el lenguaje y el sentido, lo que interpreto y lo que no se cuenta.", ["Dice: expusieron tejidos en la ciudad con su nombre y una explicación.", "Lenguaje y sentido: tejido textil y visual; memoria de la abuela.", "Interpreto: yo pienso que poner el nombre muestra orgullo por su trabajo.", "No se cuenta: qué significan los dibujos que la comunidad reserva."], "Dice: expusieron con su nombre. Lenguaje y sentido: textil y memoria. Interpreto: orgullo por su trabajo. No se cuenta: el significado reservado de los dibujos."),
        W("Distinguir dos voces", "Una niña dibujó lo que sintió al ver los tejidos. ¿De quién es ese dibujo y qué no puede afirmar?", ["El dibujo es de la niña.", "Es su respuesta a lo que sintió.", "No puede afirmar que sea el significado del tejido para la comunidad."], "El dibujo es de la niña; no puede afirmar que sea el significado del tejido para la comunidad."),
    ],
    mistakes=[
        M("Inventar el significado de un dibujo o símbolo.", "El sentido lo define la comunidad y puede estar reservado.", "Escribe «el testimonio no lo dice»."),
        M("Confundir la respuesta de una persona de afuera con la voz de la comunidad.", "Son voces distintas.", "Atribuye cada dato a quien lo dijo o creó."),
    ],
    R=[
        ex("Según doña Rosario, ¿en qué pensaba al tejer: en su abuela o en un viaje?", "En su abuela", "El testimonio lo dice así."),
        ex("Tema: el arte y el diálogo. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no dice qué significa un dibujo, ¿qué escribes? A) el testimonio no lo dice B) significa el sol", "A", "No se inventan significados."),
    ],
    C=[
        ex("Doña Rosario dice: «Pienso en mi abuela, que me enseñó los dibujos». ¿Qué sentido muestra? A) memoria familiar B) competencia", "A", "Recuerda a quien le enseñó."),
        ex("Verdadero o falso: el dibujo de la niña que vio los tejidos es la voz de la comunidad.", "Falso", "Es la respuesta de la niña."),
        ex("Verdadero o falso: respetar los sentidos que la comunidad reserva es parte de leer con límites.", "Verdadero", "Lo reservado no se pide ni se inventa."),
    ],
    A=[
        ex("Matías, de un barrio de ciudad, dice: «Pintamos un mural con los vecinos». Clasifica en DICE LA FUENTE o INTERPRETO: a) pintaron un mural con los vecinos b) el mural los hizo más amigos.", "a dice la fuente, b interpreto", "La segunda es una idea de quien lee."),
        ex("Matías dice: «Pedimos permiso al dueño del muro y firmamos todos al final». ¿Qué dos cuidados muestra? A) copia y secreto B) permiso y reconocimiento de autoría", "B", "Pidieron permiso y firmaron."),
        ex("Un niño escribe: «Doña Rosario cuenta que el dibujo del tejido representa un río». ¿Qué dato no está en el testimonio?", "Que el dibujo representa un río", "El testimonio no dice qué significan los dibujos."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «Los tejidos de Quebrada Florida son más bonitos que los murales de la ciudad». ¿Qué debería hacer con esa frase?", "Quitarla porque ordena y no está en la fuente", "No está en el testimonio y jerarquiza."),
        ex("Tema: el arte y el diálogo. ¿Por qué conviene escribir los límites al final del trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Doña Rosario cuenta que expusieron con su nombre». 2) «Doña Rosario cuenta que el tejido es un mapa secreto». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no contiene."),
        ex("Doña Rosario no contó cuántos tejidos expusieron. ¿Qué escribes en los límites? A) expusieron veinte B) no sé cuántos tejidos expusieron", "B", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere escribir debajo de un dibujo: «Este símbolo significa la unión del cielo con la tierra para los pueblos indígenas». No tiene fuente. ¿Qué le dices? A) que no lo escriba porque no tiene fuente y generaliza B) que lo escriba con letra grande", "A", "Sin fuente no se afirman significados de un pueblo.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre arte.", "Lo que dice la fuente, el lenguaje y el sentido, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Verdadero o falso: puedo inventar el significado de un símbolo si la comunidad no lo contó.", "Falso", "Eso sería inventar."),
        ex("Tema: el arte y el diálogo. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Rosario: «Hoy tejemos en la sede mientras los mayores cuentan cómo era la quebrada. Cuando vienen visitas, les mostramos los tejidos terminados, no los que están en proceso. Los sentidos de los dibujos los explicamos solo en la comunidad.» Haz cuatro columnas: «La fuente dice», «Lenguaje y sentido», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: tejen en la sede mientras los mayores cuentan cómo era la quebrada; a las visitas les muestran los tejidos terminados. Lenguaje y sentido: textil; memoria de la quebrada. Yo interpreto: yo pienso que contar mientras tejen une el arte con la memoria. No se cuenta: los sentidos de los dibujos. Límite: no sé qué cuentan los mayores.",
           ["separa cuatro columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar significados"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Rosario.",
    extend="Explica por qué mostrar solo los tejidos terminados puede ser una manera de cuidar lo que la comunidad guarda.",
)

L(
    OA17, 3, materials=MAT,
    use="Aprenderé a reconocer cómo el arte puede dialogar con otras culturas: qué condiciones hacen respetuoso el diálogo y qué casos no lo son, comparando dos testimonios inventados.",
    prior=["Sé leer un testimonio con límites.", "Sé que el arte tiene un sentido que define la comunidad."],
    explain=[
        "El arte puede abrir un diálogo con otras culturas cuando se comparte para que otras personas conozcan, se emocionen y respondan con su propia voz. Para que ese diálogo sea respetuoso hay cuatro condiciones: tener permiso, reconocer quién creó la obra, respetar el sentido que le da la comunidad y dar espacio para que todas las partes participen.",
        "Comparamos dos testimonios inventados. En Quebrada Florida, una comunidad expuso sus tejidos con su nombre y una explicación, y una niña respondió con un dibujo propio. En Barrio Sur, vecinos de una ciudad pintaron un mural entre todos, pidieron permiso y firmaron. Ambos cumplen las condiciones. Un caso distinto sería copiar un diseño de otro pueblo sin permiso y venderlo como propio.",
        "Para analizar un caso usamos las cuatro condiciones como preguntas iguales para todos: ¿hay permiso?, ¿se reconoce la autoría?, ¿se respeta el sentido?, ¿participan todas las partes? Así comparamos sin decir que un arte es mejor que otro. Y dos testimonios no bastan para decir que todo diálogo artístico es igual.",
    ],
    vocab=[("diálogo artístico", "encuentro en que el arte de unos recibe una respuesta de otros, con respeto"), ("permiso", "autorización de quien comparte algo suyo"), ("autoría", "reconocimiento de quién creó una obra"), ("participación", "que todas las partes tomen parte y puedan responder"), ("apropiación", "usar como propio algo de otra cultura sin permiso ni reconocimiento")],
    worked=[
        W("Analizar un caso", "Caso de Quebrada Florida: la comunidad expone sus tejidos en la ciudad, con su nombre y una explicación; una niña responde con un dibujo propio. ¿Cumple las cuatro condiciones?", ["Permiso: la comunidad decidió exponer.", "Autoría: pusieron su nombre.", "Sentido: dieron una explicación y reservaron lo que no se cuenta.", "Participación: la niña respondió con su voz."], "Sí: hay permiso, reconocimiento de autoría, respeto del sentido y participación."),
        W("Reconocer una apropiación", "Caso inventado: una empresa copia un diseño de una comunidad, lo imprime en ropa y lo vende como propio, sin permiso. ¿Qué condiciones faltan?", ["No hay permiso.", "No hay reconocimiento de la autoría.", "No se respeta el sentido ni participa la comunidad."], "Faltan permiso, autoría, respeto del sentido y participación: es apropiación."),
    ],
    mistakes=[
        M("Pensar que compartir un arte sin permiso ayuda a difundirlo.", "Sin permiso es apropiación y puede dañar a la comunidad.", "Pide permiso y reconoce la autoría."),
        M("Concluir que todo diálogo artístico es igual porque dos casos se parecen.", "Dos ejemplos no representan todos los casos.", "Escribe «en estos dos casos»."),
    ],
    R=[
        ex("En Barrio Sur, ¿pidieron permiso para pintar el mural: sí o no?", "Sí", "Matías cuenta que pidieron permiso al dueño del muro."),
        ex("¿Qué pusieron los vecinos al final del mural: sus firmas o ningún nombre?", "Sus firmas", "Firmaron todos al final."),
        ex("Usar como propio un diseño de otra cultura sin permiso, ¿es apropiación o diálogo?", "Apropiación", "Esa es la definición de apropiación."),
    ],
    C=[
        ex("Verdadero o falso: para un diálogo artístico respetuoso hace falta tener permiso.", "Verdadero", "El permiso es una condición."),
        ex("¿Cuántas condiciones usamos para analizar un diálogo artístico? Escribe el número.", "4", "Son permiso, autoría, sentido y participación."),
        ex("Verdadero o falso: si dos casos cumplen las condiciones, todos los diálogos artísticos son iguales.", "Falso", "Dos casos no representan todos los casos."),
    ],
    A=[
        ex("Caso inventado: un grupo de estudiantes presenta una danza de una comunidad real sin avisarle y dice que la inventó. ¿Qué dos condiciones faltan? A) permiso y autoría B) permiso y participación del grupo", "A", "No pidieron permiso ni reconocieron a la comunidad."),
        ex("Clasifica en DIÁLOGO o APROPIACIÓN: a) una escuela invita a un artista de una comunidad y le agradece nombrándolo b) una tienda imprime un diseño de una comunidad sin avisar.", "a diálogo, b apropiación", "La primera cumple las condiciones; la segunda, no."),
        ex("Criterio: «participación». Quebrada Florida: una niña respondió con un dibujo. Barrio Sur: cada familia dibujó algo. ¿Qué semejanza hay? A) en ambos participaron otras personas además de quienes empezaron la obra B) en ambos participó una sola persona", "A", "En los dos casos hubo participación ampliada."),
    ],
    Z=[
        ex("Ana dice: «El mural de Barrio Sur es mejor arte que los tejidos de Quebrada Florida». ¿Qué falla en su comparación?", "Ordena dos artes sin criterio ni fuente", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como estas dos comunidades pidieron permiso, todas las comunidades lo hacen». ¿Qué debería escribir? A) «en estos dos casos» B) «en todos los casos»", "A", "Dos casos no representan a todos."),
    ],
    D=[
        ex("La profesora Elena cuenta que su curso no grabó ciertas partes que el artista pidió no grabar. ¿Qué condición respeta? A) la apropiación B) el sentido y los límites que fija la comunidad", "B", "Respetó lo que el artista pidió reservar."),
        ex("Dos conclusiones. 1) «En estos casos, el arte dialoga cuando hay permiso, autoría, sentido y participación». 2) «Solo el arte de las ciudades dialoga con otras culturas». ¿Cuál está bien formulada?", "La primera", "La segunda ordena sin datos."),
    ],
    context=[ex("Tu curso quiere hacer un mural con símbolos de varias culturas. Un compañero propone copiar de internet el diseño de una comunidad real sin consultar. ¿Qué haces para que sea un diálogo respetuoso? A) copiarlo igual B) pedir permiso, reconocer la autoría y respetar el sentido que ella indique", "B", "Cumple las cuatro condiciones.")],
    selfcheck=[
        ex("Nombra dos condiciones para un diálogo artístico respetuoso.", "Dos entre: permiso, autoría, sentido, participación", "Son las condiciones de la explicación."),
        ex("Verdadero o falso: puedo ordenar dos artes de mejor a peor.", "Falso", "Cada arte tiene su sentido."),
        ex("Escribe una pregunta para analizar un caso de diálogo artístico.", "Por ejemplo: ¿hay permiso?", "Es una de las cuatro preguntas."),
    ],
    task=T("Analiza estos dos casos inventados. Caso 1: una comunidad expone sus tejidos en una biblioteca, con su nombre y una explicación; los visitantes dejan dibujos propios como respuesta. Caso 2: un grupo de estudiantes toma el diseño de un tejido de una comunidad desde una foto y lo estampa en poleras para vender, sin avisar. Haz una tabla con cuatro preguntas: «¿hay permiso?», «¿se reconoce la autoría?», «¿se respeta el sentido?» y «¿participan todas las partes?». Responde para cada caso y escribe si es un diálogo respetuoso o una apropiación.",
           "Caso 1: permiso sí; autoría sí; sentido sí, con explicación; participan, con dibujos de respuesta. Es un diálogo respetuoso. Caso 2: permiso no; autoría no; sentido no se respeta; la comunidad no participa. Es una apropiación.",
           ["responde las cuatro preguntas por caso", "decide con base en las respuestas", "no jerarquiza artes"], ["tabla con cuatro preguntas y dos casos"], ["generalizar a todos los grupos", "no usar los criterios"],
           "Pedir que señale en el caso la frase que justifica cada respuesta; valorar que no ordene las artes."),
    reinforce="Marca con verde las respuestas «sí» y con rojo las «no» en tu tabla para ver cómo cambia el resultado.",
    extend="Propón un cambio para que el caso 2 se vuelva un diálogo respetuoso, indicando qué permiso y qué reconocimiento harían falta.",
)

L(
    OA17, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida y una expresión artística propia que muestre cómo el arte puede dialogar con otras culturas, con fuente, reflexión, límite y pregunta.",
    prior=["Sé analizar un diálogo artístico con cuatro preguntas.", "Sé leer un testimonio con límites."],
    explain=[
        "Una respuesta atribuida sobre arte y diálogo tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Rosario cuenta que…». Segundo, el lenguaje artístico y el sentido que aparecen. Tercero, cómo ese arte dialoga con otra cultura y qué condiciones cumple. Cuarto, tu reflexión con «yo pienso que» y un límite. Quinto, una pregunta para el educador tradicional.",
        "Además, esta clase te invita a crear una expresión artística propia, con un lenguaje que sea tuyo o de tu pueblo si puedes consultarlo con tu educador o educadora tradicional: un dibujo, un poema de dos líneas, un ritmo con palmas. La expresión es tuya. No reproduce lo que la comunidad guarda ni inventa un símbolo ancestral. Al presentarla, dices que es propia e invitas a otras personas a responder con la suya.",
        "Una buena respuesta no exagera, no inventa significados y no habla por todo un pueblo. Reconoce lo que no sabe y respeta lo que la comunidad reserva. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("expresión propia", "obra que creas tú, sin copiar ni inventar algo ajeno"), ("invitar a responder", "abrir un espacio para que otra persona responda con su propia obra"), ("símbolo ancestral", "símbolo que una comunidad recibe de sus antepasados"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TQF + " Arma una respuesta atribuida de cinco partes.", ["Dato: doña Rosario cuenta que expusieron tejidos en la ciudad con su nombre y una explicación.", "Lenguaje y sentido: tejido textil y visual; memoria de su abuela.", "Diálogo: una niña respondió con un dibujo; hubo autoría, explicación y participación.", "Reflexión, límite y pregunta: yo pienso que el dibujo de la niña fue una respuesta respetuosa; no sé qué significan los dibujos reservados; preguntaré al educador tradicional."], "Respuesta con dato atribuido, lenguaje y sentido, diálogo, reflexión con límite y pregunta."),
        W("Revisar una expresión propia", "Una niña dibuja una figura y escribe: «Símbolo ancestral de mi pueblo». No consultó a nadie. ¿Qué debe cambiar?", ["No sabe si esa figura es de su pueblo.", "No consultó al educador tradicional.", "Debe decir que es un dibujo propio, o consultar antes."], "Debe decir que es un dibujo propio, o consultar antes de llamarlo ancestral."),
    ],
    mistakes=[
        M("Presentar un dibujo inventado como símbolo ancestral.", "Se falsea un saber que no consultaste.", "Escribe que es una expresión propia o consulta al educador."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Rosario? A) «Todos saben que…» B) «Doña Rosario cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: el arte y el diálogo. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, lenguaje y sentido, diálogo, reflexión con límite y pregunta."),
        ex("Tema: el arte y el diálogo. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué es una expresión propia? A) una copia de un diseño de una comunidad B) una obra que creo yo sin copiar ni inventar algo ajeno", "B", "Es mía y no pretende ser ancestral."),
        ex("Verdadero o falso: puedo llamar «símbolo ancestral» a un dibujo que inventé.", "Falso", "Sería presentar algo inventado como ajeno."),
        ex("Tema: el arte y el diálogo. ¿Para qué sirve la pregunta final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de doña Rosario: «Una niña dibujó lo que sintió al ver los tejidos». Completa la atribución: «Doña Rosario cuenta que una niña…»", "Dibujó lo que sintió al ver los tejidos", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Rosario cuenta que pusieron su nombre al exponer b) yo pienso que poner el nombre ayuda a que se reconozca a la comunidad.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una nota dice: «Poema de dos líneas, expresión propia inspirada en el testimonio de doña Rosario». ¿Qué hace bien? A) la presenta como ancestral B) aclara que la expresión es propia", "B", "Dice que es propia e inspirada en el testimonio."),
    ],
    Z=[
        ex("Tema: el arte y el diálogo. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar lo que no sé o no se cuenta B) agregar más datos inventados", "A", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta y tu expresión al educador tradicional? A) porque es una tarea de decoración B) porque conoce el arte de su pueblo y puede corregir errores", "B", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Rosario cuenta que expusieron con su nombre; yo pienso que eso reconoce a la comunidad». 2) «Doña Rosario demuestra que el arte de su pueblo es el mejor». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega que en Quebrada Florida «seguro cantan una canción al tejer». El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre cómo el tejido de Quebrada Florida dialogó con la niña que lo vio. ¿Qué empieza mejor? A) «Todos los pueblos indígenas dialogan con el arte porque…» B) «Doña Rosario cuenta que…»", "B", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre arte y diálogo.", "Dato de la fuente, lenguaje y sentido, diálogo, reflexión con límite y pregunta", "Están en la explicación."),
        ex("Tema: el arte y el diálogo. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: el arte y el diálogo. ¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) guardarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Rosario: «Cuando exponemos tejidos, ponemos nuestro nombre y explicamos lo que podemos contar. Algunas personas nos responden con dibujos o con palabras, y eso nos gusta. Los sentidos reservados de los dibujos no los explicamos.» Escribe una respuesta de cinco partes: 1) dato de doña Rosario, 2) lenguaje y sentido, 3) cómo ese arte dialoga con otra cultura, 4) tu reflexión con «yo pienso que» y un límite, 5) una pregunta para el educador tradicional. Después crea una expresión propia (un dibujo simple o un poema de dos líneas sobre tu territorio o tu familia) y escribe debajo «expresión propia, inspirada en el testimonio de doña Rosario». Si quieres usar algo de tu pueblo, consúltalo antes.",
           "1) Doña Rosario cuenta que al exponer ponen su nombre y explican lo que pueden contar. 2) Lenguaje: tejido textil; sentido: reconocer a la comunidad y proteger lo reservado. 3) Dialoga cuando otras personas responden con dibujos o palabras. 4) Yo pienso que responder con una obra propia es una forma de agradecer; no sé qué significan los dibujos reservados. 5) Pregunta: ¿cómo pueden las personas de otras culturas responder al arte de mi pueblo con respeto? Expresión: poema «Mi cerro tiene nubes / y mi casa, su ventana». Expresión propia, inspirada en el testimonio de doña Rosario.",
           ["atribuye cada dato", "incluye límite y pregunta", "aclara que la expresión es propia"], ["texto de cinco partes", "dibujo o poema con nota de autoría"], ["presentar la expresión como ancestral", "inventar significados"],
           "Pedir que señale la línea del testimonio que respalda su reflexión; valorar que la expresión diga que es propia."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Escribe una invitación de dos líneas para que un compañero responda a tu expresión con la suya.",
)

L(
    OA17, 5, materials=MAT,
    use="Aprenderé a contrastar sin jerarquizar tres lenguajes artísticos (un tejido, un coro y un mural) y a ver que el arte de un pueblo no es una «artesanía menor» frente a otros artes.",
    prior=["Sé armar una respuesta atribuida.", "Sé analizar un diálogo artístico con cuatro preguntas."],
    explain=[
        "Contrastar es poner varios lenguajes artísticos uno al lado del otro para ver en qué coinciden y en qué se diferencian. Sin jerarquizar quiere decir que no los ordenamos de «más arte» a «menos arte». Un tejido, un coro y un mural son lenguajes distintos, y los tres expresan ideas y sentimientos de quienes los crean.",
        "Un error frecuente es llamar «artesanía» a lo que hacen los pueblos indígenas y «arte» a lo que hacen otros, como si lo primero valiera menos. Esas palabras ordenan sin mirar el sentido de cada obra. Para evitarlo, describimos el lenguaje, el sentido y cómo dialoga cada una con otras personas.",
        "Contrastamos tres casos inventados: los tejidos de Quebrada Florida, el coro de la profesora Elena y el mural de Barrio Sur. Usamos criterios iguales: qué lenguaje usan, qué sentido tienen y cómo cuidan el diálogo. Y tres casos no bastan para decir que todo el arte de un pueblo, de un colegio o de un barrio es igual.",
    ],
    vocab=[("contrastar", "poner varios lenguajes artísticos juntos para ver en qué coinciden y en qué se diferencian"), ("jerarquizar", "ordenar de más a menos valioso"), ("artesanía", "obra hecha a mano con técnica tradicional; no es menos arte que otras obras"), ("criterio", "punto de comparación igual para todos"), ("sentido", "lo que algo significa para quienes lo crean")],
    worked=[
        W("Contrastar tres artes", TQF + " " + TBS + " " + TCE + " Criterio: «cómo cuidan el diálogo». ¿En qué coinciden?", ["Quebrada Florida: puso su nombre y explicó lo que podía contar.", "Barrio Sur: pidió permiso y firmó.", "Coro de la profesora Elena: respetó lo que el artista pidió no grabar y dijo que su canción era propia.", "Los tres casos cuidan la autoría o los límites."], "Coinciden en que los tres casos cuidan la autoría o los límites del diálogo."),
        W("Evitar una jerarquía", "Un niño dice: «El mural de Barrio Sur es arte, pero el tejido de Quebrada Florida es solo artesanía». ¿Qué error hay?", ["Usa «solo artesanía» para ordenar el tejido como menos importante.", "Los dos expresan ideas y sentimientos.", "Debería describir el lenguaje y el sentido de cada uno."], "Jerarquiza con «solo artesanía»: debe describir el lenguaje y el sentido de cada obra."),
    ],
    mistakes=[
        M("Decir que lo que hace un pueblo indígena es «solo artesanía».", "Es un lenguaje artístico con sentido propio.", "Describe el lenguaje, el sentido y cómo dialoga."),
        M("Pensar que contrastar significa decir que todas las obras son iguales.", "Cada una tiene su lenguaje y su sentido.", "Compara con criterios iguales y anota semejanzas y diferencias."),
    ],
    R=[
        ex("¿Qué lenguaje usa Quebrada Florida: tejido textil o coro?", "Tejido textil", "El coro es de la escuela de la profesora Elena."),
        ex("En Barrio Sur, ¿qué pintaron los vecinos: un mural o un tejido?", "Un mural", "Matías cuenta que pintaron un mural."),
        ex("Contrastar, ¿es poner artes juntos para ver coincidencias y diferencias o es elegir el mejor?", "Poner artes juntos para ver coincidencias y diferencias", "Contrastar no es elegir el mejor."),
    ],
    C=[
        ex("Verdadero o falso: llamar «solo artesanía» a una obra indígena ayuda a describirla.", "Falso", "Es un juicio que no describe."),
        ex("¿Por qué se usan criterios iguales para los tres artes? A) para no tratar a uno mejor que otro B) para llenar la tabla", "A", "Los criterios iguales evitan el trato desigual."),
        ex("Verdadero o falso: tres casos bastan para describir el arte de todos los pueblos.", "Falso", "Tres casos no representan a todos."),
    ],
    A=[
        ex("Criterio: «qué recurso usan». Quebrada Florida: lana y colores. Coro: voces. Barrio Sur: pintura sobre un muro. ¿Qué diferencia hay? A) cada arte usa un recurso distinto B) los tres usan el mismo recurso", "A", "Lana, voces y pintura son recursos distintos."),
        ex("Clasifica en COINCIDENCIA o DIFERENCIA: a) los tres artes expresan ideas o sentimientos de quienes los crean b) uno es textil, otro sonoro y otro visual en un muro.", "a coincidencia, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Un joven dice: «El coro es arte de verdad y el tejido es solo una costumbre». ¿Qué falla? A) usa el nombre del coro B) ordena artes sin criterio ni fuente", "B", "Contrastar no es jerarquizar."),
    ],
    Z=[
        ex("Ana dice: «El arte de los pueblos indígenas es antiguo y por eso menos creativo». ¿Qué evidencia de la clase la contradice?", "Una niña respondió con un dibujo propio al ver los tejidos", "El arte actual de la comunidad sigue dialogando con otras personas."),
        ex("Un compañero concluye: «Todo el arte de ciudad pide permiso y firma». ¿Qué debería escribir? A) «en el caso de Barrio Sur, pidieron permiso y firmaron» B) «en todas las ciudades»", "A", "Un caso no representa a todas las ciudades."),
    ],
    D=[
        arith("Los vecinos de Barrio Sur son 8 familias y cada una dibujó 3 elementos en el mural. ¿Cuántos elementos tiene el mural?", "8*3", "Se multiplica el número de familias por los elementos de cada una."),
        ex("Dos conclusiones. 1) «En estos tres casos, el arte expresa algo de quienes lo crean y cuida el diálogo de maneras distintas». 2) «El arte de ciudad es más libre que el de las comunidades». ¿Cuál está bien formulada?", "La primera", "La segunda ordena sin datos."),
    ],
    context=[ex("En tu escuela hacen una feria de arte. Una compañera quiere separar «arte» y «artesanía de pueblos indígenas» en dos secciones con diferente prestigio. ¿Qué le propones? A) mantener las dos secciones B) presentar todas las obras con su lenguaje, su sentido y su autoría, sin separar por prestigio", "B", "Se describe cada obra sin jerarquizar.")],
    selfcheck=[
        ex("Escribe una palabra que no debes usar para menospreciar la obra de un pueblo.", "Solo artesanía", "Es un juicio que ordena sin describir."),
        ex("Verdadero o falso: puedo ordenar tres artes de más a menos valioso.", "Falso", "Contrastar no es jerarquizar."),
        ex("Nombra un criterio de contraste para tres artes.", "Por ejemplo: qué recurso usan", "Debe ser un punto igual para todos."),
    ],
    task=T("Contrasta estos tres casos inventados. Quebrada Florida: «Tejemos con lana y colores de la quebrada y exponemos con nuestro nombre». Coro de la escuela: «Cantamos entre todos y respetamos lo que un invitado pidió no grabar». Mural de Barrio Sur: «Pintamos entre vecinos, pedimos permiso y firmamos». Haz una tabla con tres criterios: «qué lenguaje y recurso usan», «quiénes lo crean» y «cómo cuidan el diálogo». Escribe una coincidencia, una diferencia y una frase que muestre cómo evitarías decir «solo artesanía».",
           "Lenguaje y recurso: textil con lana; sonoro con voces; visual con pintura sobre un muro. Quiénes lo crean: la comunidad de Quebrada Florida; el coro de la escuela; los vecinos del barrio. Cuidado del diálogo: poner el nombre; respetar lo que se pidió no grabar; pedir permiso y firmar. Coincidencia: los tres cuidan la autoría o los límites. Diferencia: cada uno usa un lenguaje distinto. Describiría el tejido por su lenguaje y su sentido, no como «solo artesanía».",
           ["usa los mismos criterios para los tres", "distingue coincidencia y diferencia", "describe sin jerarquizar"], ["tabla de tres criterios", "coincidencia, diferencia y frase"], ["usar «solo artesanía»", "inventar significados"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que no ordene las artes."),
    reinforce="Marca en la tabla con un color las coincidencias y con otro las diferencias.",
    extend="Agrega un cuarto lenguaje artístico (por ejemplo, la danza) y explica qué criterio permitiría compararlo con los otros tres.",
)
