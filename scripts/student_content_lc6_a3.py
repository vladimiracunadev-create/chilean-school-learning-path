"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 11 (relación armónica, física y espiritual de uno mismo y la naturaleza) y
OA 12 (actividades espirituales y socioculturales que mantienen el equilibrio entre ser humano, naturaleza y cosmos).

Las comunidades, personas, actividades y testimonios son INVENTADOS y se rotulan así; no se describe ningún rito,
ceremonia ni creencia de un pueblo real. Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc6_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA11, OA12 = "LC06 OA 11", "LC06 OA 12"

# ------------------------------------------------------------------ OA 11
FBC = ("Ficha situada (inventada). Comunidad: Bosque Claro (no es un pueblo real). Territorio: un bosque, un río y una huerta. "
       "Fuente y responsable: don Elías, vecino de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: don Elías autorizó usar esta ficha en la escuela. "
       "Límite: no se cuentan los lugares del bosque que la comunidad visita en silencio.")
TBC = ("Testimonio inventado de don Elías, de Bosque Claro: «Cuando camino por el bosque me siento tranquilo y duermo mejor. Recojo solo frutos maduros y dejo el resto para los animales. "
       "Mi madre me enseñó a agradecer lo que da la huerta. Hay lugares del bosque a los que vamos con respeto y en silencio, y no los mostramos.»")
TCS = ("Testimonio inventado de doña Berta, de Costa Serena: «Camino por la orilla cada mañana y eso me hace bien al cuerpo. Antes de comer en familia damos las gracias por el alimento que vino del mar. "
       "Hay conversaciones de la caleta que no se cuentan.»")
TCV = ("Testimonio inventado de Valentina, escolar de una ciudad: «Los domingos voy con mi curso a un parque. Cuando miro los árboles me calmo, y cuido de no dejar basura. "
       "No sé mucho de los pueblos indígenas, pero me gusta aprender.»")

L(
    OA11, 1, materials=MAT,
    use="Aprenderé a situar una relación entre una persona y la naturaleza: de qué comunidad es, quién la cuenta y qué no se cuenta. Sirve para analizar cómo el cuerpo y el sentido espiritual se relacionan con la naturaleza sin hablar por otros.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que cada comunidad cuenta su relación con la naturaleza a su manera."],
    explain=[
        "Una relación armónica es una relación de equilibrio y respeto: se toma lo necesario, se cuida lo que da y se agradece. Muchas fuentes indígenas hablan de una relación así entre las personas y la naturaleza. Cada pueblo la entiende a su manera, y por eso no se puede explicar con una sola frase para todos.",
        "Esa relación puede mirarse en dos dimensiones. La dimensión física tiene que ver con el cuerpo: caminar, respirar aire limpio, alimentarse de lo que da la tierra y descansar. La dimensión espiritual tiene que ver con lo que una persona o una comunidad siente y cree sobre el sentido de la vida y el respeto hacia lo que la rodea, y no se puede tocar ni medir.",
        "Antes de analizar, hay que situar. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es el relato y qué no se cuenta. Lo que dice una ficha vale para esa comunidad y no para todos los pueblos.",
    ],
    vocab=[("relación armónica", "relación de equilibrio y respeto, donde se toma lo necesario y se cuida lo que da"), ("dimensión física", "lo que tiene que ver con el cuerpo, como caminar, alimentarse y descansar"), ("dimensión espiritual", "lo que una persona o comunidad siente y cree sobre el sentido de la vida y el respeto hacia lo que la rodea"), ("naturaleza", "plantas, animales, agua, tierra y todo lo vivo que nos rodea"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FBC + " ¿De quién es el relato y qué no se cuenta?", ["La comunidad es Bosque Claro y la fuente es don Elías.", "Él dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuentan los lugares del bosque que visitan en silencio."], "El relato es de don Elías, de Bosque Claro; no se cuentan los lugares que visitan en silencio."),
        W("Clasificar dos dimensiones", "Don Elías dice: «Camino por el bosque y duermo mejor» y «Mi madre me enseñó a agradecer lo que da la huerta». ¿Qué dimensión muestra cada frase?", ["«Duermo mejor» habla del cuerpo: dimensión física.", "«Agradecer lo que da la huerta» habla de respeto y sentido: dimensión espiritual."], "La primera muestra la dimensión física; la segunda, la espiritual."),
    ],
    mistakes=[
        M("Pensar que lo espiritual es lo mismo que lo religioso de un solo pueblo.", "Cada pueblo y cada persona entiende lo espiritual a su manera.", "Escribe qué dice la fuente, sin explicar creencias que no contó."),
        M("Decir que la visión de Bosque Claro es la de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según don Elías, en Bosque Claro…»."),
    ],
    R=[
        ex("Según la ficha de Bosque Claro, ¿quién es la fuente?", "Don Elías", "La ficha lo nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Bosque Claro? A) una caleta y un puerto B) un bosque, un río y una huerta", "B", "La caleta y el puerto son de otras fichas."),
        ex("La ficha de Bosque Claro dice que no se cuentan los lugares que visitan en silencio. ¿Los ubicas en tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es una relación armónica con la naturaleza? A) una relación de equilibrio y respeto B) una relación de dominio", "A", "Se toma lo necesario y se cuida lo que da."),
        ex("Verdadero o falso: la dimensión física de la relación con la naturaleza tiene que ver con el cuerpo.", "Verdadero", "Caminar, respirar y alimentarse son experiencias físicas."),
        ex("Verdadero o falso: la ficha de Bosque Claro sirve para hablar de todos los pueblos indígenas.", "Falso", "Una comunidad no representa a todos los pueblos."),
    ],
    A=[
        ex("Clasifica en FÍSICA o ESPIRITUAL: a) caminar por el bosque y descansar mejor b) agradecer lo que da la huerta.", "a física, b espiritual", "La primera afecta al cuerpo; la segunda, al sentido y al respeto."),
        ex("Don Elías dice: «Recojo solo frutos maduros y dejo el resto para los animales». ¿Qué muestra de la relación con la naturaleza? A) tomar lo necesario B) tomar todo lo que se pueda", "A", "La frase habla de dejar parte para otros seres vivos."),
        ex("Tema: la relación con la naturaleza. Una compañera trae una ficha con comunidad y fuente, pero sin permiso. ¿Qué falta? A) el color del papel B) la autorización de la fuente para compartir", "B", "El permiso es parte de una ficha situada."),
    ],
    Z=[
        ex("Pablo escribe: «Como don Elías duerme mejor, todos los pueblos indígenas se curan en el bosque». ¿Qué error comete?", "Generaliza un caso a todos los pueblos y agrega una cura que nadie dijo", "Un testimonio no representa a todos los pueblos."),
        ex("¿Por qué conviene situar la fuente antes de analizar la relación con la naturaleza? A) para escribir más rápido B) porque el relato es la mirada de una persona de una comunidad", "B", "Situar muestra de quién es la mirada."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Bosque Claro. Territorio: bosque». ¿Qué datos faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todos los pueblos entienden la naturaleza como don Elías». ¿Qué corriges? A) escribo «según don Elías (persona inventada), en Bosque Claro…» B) lo dejo igual", "A", "El cartel debe atribuir el dato a esa fuente."),
    ],
    context=[ex("En una salida de curso, una profesora cuenta una costumbre de «los pueblos indígenas» frente a un bosque, sin decir de qué pueblo ni quién se la contó. ¿Qué preguntas haces después? A) ¿cuánto dura la salida? B) ¿de qué pueblo es y quién lo contó?", "B", "Hay que situar el dato antes de usarlo.")],
    selfcheck=[
        ex("Nombra las dos dimensiones de la relación con la naturaleza de esta clase.", "Física y espiritual", "Son las dos dimensiones de la explicación."),
        ex("Verdadero o falso: la dimensión espiritual se puede medir con una balanza.", "Falso", "No se puede tocar ni medir."),
        ex("Tema: la relación con la naturaleza. Ante una duda sobre una comunidad real, ¿qué haces? A) pregunto al educador tradicional o a la comunidad B) lo supongo", "A", "Ellos son la fuente."),
    ],
    task=T("Lee esta nota inventada de don Elías: «En Bosque Claro la huerta nos da verduras. Los niños ayudan a regar por la tarde. Antes de cosechar, agradecemos. De los lugares del bosque no hablamos con visitas.» Haz una ficha con: comunidad, territorio, fuente, qué dice la fuente y un límite. Luego escribe dos frases: una sobre la dimensión física y otra sobre la espiritual, ambas con «Yo pienso que…».",
           "Comunidad: Bosque Claro. Territorio: bosque, río y huerta. Fuente: don Elías. Dice: la huerta da verduras, los niños riegan y agradecen antes de cosechar. Límite: no se cuentan los lugares del bosque. Física: yo pienso que regar y cosechar es un trabajo del cuerpo. Espiritual: yo pienso que agradecer antes de cosechar muestra respeto por lo que da la huerta.",
           ["completa la ficha con datos de la nota", "separa dimensión física y espiritual", "pone un límite"], ["ficha completa", "dos frases con «Yo pienso que»"], ["agregar datos que la nota no dice", "explicar creencias no contadas"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que separe la fuente de su opinión."),
    reinforce="Subraya en la ficha de Bosque Claro la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué una relación armónica con la naturaleza no es solo una idea, sino también algo que el cuerpo vive.",
)

L(
    OA11, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre la relación con la naturaleza con límites declarados: qué dice la fuente, qué dimensión muestra, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar una comunidad con su ficha.", "Sé distinguir la dimensión física de la espiritual."],
    explain=[
        "Un testimonio sobre la relación con la naturaleza mezcla experiencias del cuerpo y sentidos más profundos. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. La dimensión que muestra cada frase: física o espiritual. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de don Elías, «duermo mejor» muestra la dimensión física y «agradecer lo que da la huerta» muestra la dimensión espiritual. Pero no dice por qué agradecen ni cómo lo hacen. Si yo agrego una ceremonia con detalles, ya no estoy leyendo su testimonio: estoy inventando una práctica que nadie contó.",
        "Leer con límites declarados significa decir hasta dónde llega lo que afirmo. Los lugares que la comunidad visita en silencio se respetan y no se piden ni se describen. Si queremos saber más sobre cómo vive un pueblo real su relación con la naturaleza, preguntamos al educador o a la educadora tradicional.",
    ],
    vocab=[("dimensión", "aspecto desde el que se mira algo, como el cuerpo o el sentido espiritual"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("agradecer", "reconocer con respeto lo que se recibió"), ("reservado", "lo que una comunidad prefiere no compartir con todos"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TBC + " Separa lo que dice, la dimensión, lo que interpreto y lo que no se cuenta.", ["Dice: recoge solo frutos maduros y deja el resto para los animales.", "Dimensión: es una práctica de respeto que se ve en lo que hace (espiritual y social); «duerme mejor» es física.", "Interpreto: yo pienso que cuidar a los animales también cuida el bosque.", "No se cuenta: cuáles son los lugares del bosque que visitan en silencio."], "Dice: toma frutos maduros y deja el resto. Dimensión: respeto (espiritual) y bienestar del cuerpo (física). Interpreto: cuidar a los animales cuida el bosque. No se cuenta: los lugares reservados."),
        W("Detectar un agregado", "Una niña escribe: «Don Elías cuenta que en el bosque hay un espíritu que lo protege». ¿Está bien?", ["Reviso el testimonio: habla de tranquilidad, frutos, agradecimiento y lugares reservados.", "No menciona ningún espíritu.", "La niña agregó una creencia que la fuente no contó."], "No: agrega una creencia que don Elías no contó."),
    ],
    mistakes=[
        M("Agregar creencias o ceremonias que la fuente no contó.", "Se inventa una práctica que puede ser falsa y faltar el respeto.", "Escribe «el testimonio no lo dice»."),
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
    ],
    R=[
        ex("Según don Elías, ¿qué recoge en el bosque: frutos maduros o troncos?", "Frutos maduros", "El testimonio lo dice así."),
        ex("Tema: la relación con la naturaleza. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no explica por qué agradecen, ¿qué escribes? A) agradecen a un espíritu B) el testimonio no lo dice", "B", "No se inventan razones."),
    ],
    C=[
        ex("Don Elías dice: «Duermo mejor cuando camino por el bosque». ¿Qué dimensión muestra? A) física B) espiritual", "A", "Habla del descanso del cuerpo."),
        ex("Verdadero o falso: si no sé por qué una comunidad hace algo, puedo completar con una explicación probable.", "Falso", "Eso sería inventar."),
        ex("Verdadero o falso: respetar los lugares que la comunidad reserva es parte de leer con límites.", "Verdadero", "Lo reservado no se pide ni se describe."),
    ],
    A=[
        ex("Doña Berta dice: «Antes de comer en familia damos las gracias por el alimento que vino del mar». Clasifica en DICE LA FUENTE o INTERPRETO: a) dan las gracias antes de comer b) el mar es muy importante para su fe.", "a dice la fuente, b interpreto", "La segunda no está en el testimonio."),
        ex("Don Elías dice: «Mi madre me enseñó a agradecer lo que da la huerta». ¿Qué cuenta ese dato? A) cómo se transmitió una costumbre de respeto B) cómo se vende la verdura", "A", "El testimonio habla de enseñanza familiar."),
        ex("Un niño escribe: «Don Elías ofrece frutos a los árboles». ¿Qué parte no está en el testimonio?", "Que ofrece frutos a los árboles", "El testimonio dice que deja frutos para los animales."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «Los lugares reservados del bosque son los más sagrados». ¿Qué debería hacer con esa frase?", "Quitarla porque no está en la fuente", "El testimonio no explica por qué se reservan."),
        ex("Tema: la relación con la naturaleza. ¿Por qué conviene escribir los límites al final del trabajo? A) para llenar la hoja B) para mostrar hasta dónde llega lo afirmado", "B", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Don Elías cuenta que dejan frutos para los animales». 2) «Don Elías cuenta que el bosque los cura de todo». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega algo que el testimonio no dice."),
        ex("Don Elías no contó qué hacen en los lugares reservados. ¿Qué escribes en los límites? A) se hacen ceremonias especiales B) no sé qué se hace en esos lugares", "B", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere dibujar una ceremonia en el bosque «como las de los indígenas». El testimonio y la ficha no hablan de ceremonias. ¿Qué le dices? A) que no la dibuje porque no está en la fuente B) que la dibuje con muchos detalles", "A", "No se inventan prácticas que la fuente no cuenta.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre la relación con la naturaleza.", "Lo que dice la fuente, la dimensión que muestra, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: la relación con la naturaleza. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: la relación con la naturaleza. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Berta, de Costa Serena: «Salgo temprano a caminar por la orilla y respiro el aire de la mañana. Cuando mi nieta me acompaña, le enseño a no tomar más conchas de las que necesitamos. Hay oraciones y conversaciones de la caleta que no cuento.» Haz cuatro columnas: «La fuente dice», «Dimensión» (física o espiritual), «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: camina por la orilla, respira el aire de la mañana y enseña a su nieta a no tomar más conchas de las necesarias. Dimensión: caminar y respirar son físicas; no tomar de más es de respeto. Yo interpreto: yo pienso que enseñar a su nieta mantiene viva una costumbre. No se cuenta: las oraciones y conversaciones de la caleta. Límite: no sé en qué situaciones las cuenta.",
           ["separa cuatro columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["escribir interpretaciones como datos", "inventar las oraciones reservadas"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Berta.",
    extend="Explica por qué callar unas conversaciones puede ser una manera de cuidarlas, usando el testimonio de doña Berta.",
)

L(
    OA11, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre el cuerpo, el sentido espiritual y la naturaleza en dos comunidades inventadas, y a compararlas sin decir que una es mejor.",
    prior=["Sé leer un testimonio con límites.", "Sé distinguir la dimensión física de la espiritual."],
    explain=[
        "Una relación cultural une una experiencia con una idea. Por ejemplo: caminar por el bosque (experiencia del cuerpo) se une con sentirse tranquilo y agradecer lo que da la huerta (sentido espiritual). Así, lo físico y lo espiritual no son dos mundos separados: en muchos testimonios aparecen juntos en una misma práctica.",
        "Comparamos dos testimonios inventados: el de don Elías, de Bosque Claro, y el de doña Berta, de Costa Serena. En ambos aparecen caminar y bienestar del cuerpo, y también dar gracias por el alimento. Hay diferencias: el bosque y la huerta en un caso y la orilla y el mar en el otro.",
        "Para comparar usamos los mismos criterios en las dos tablas: qué hace el cuerpo, qué sentido de respeto aparece y qué se reserva. No ordenamos a las comunidades de «más conectada» a «menos conectada». Y dos testimonios no bastan para decir que todos los pueblos viven igual su relación con la naturaleza.",
    ],
    vocab=[("relación cultural", "unión entre una experiencia y una idea de una cultura"), ("bienestar", "sentirse bien en el cuerpo y en el ánimo"), ("semejanza", "algo parecido entre dos testimonios"), ("diferencia", "algo distinto entre dos testimonios"), ("criterio", "punto de comparación igual para los dos casos")],
    worked=[
        W("Relacionar lo físico y lo espiritual", TBC + " ¿Qué relación hay entre caminar por el bosque y agradecer?", ["Caminar por el bosque es una experiencia del cuerpo.", "Don Elías también agradece lo que da la huerta.", "En su testimonio, el cuerpo y el respeto aparecen en la misma forma de vivir."], "En su testimonio, lo físico y lo espiritual aparecen juntos en una misma forma de vivir con la naturaleza."),
        W("Comparar con un criterio", TCS + " Criterio: «qué hace el cuerpo». Don Elías: camina por el bosque. Doña Berta: camina por la orilla. ¿Qué semejanza hay?", ["Don Elías camina en un lugar natural.", "Doña Berta camina en otro lugar natural.", "En los dos casos caminar les hace bien al cuerpo."], "Semejanza: en los dos casos caminar por un lugar natural les hace bien al cuerpo."),
    ],
    mistakes=[
        M("Decir que una comunidad está más conectada con la naturaleza que otra.", "Comparar no es ordenar.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todos los pueblos viven igual su relación con la naturaleza porque dos testimonios se parecen.", "Dos ejemplos no representan a todos los pueblos.", "Escribe «en estos dos testimonios» y no más."),
    ],
    R=[
        ex("¿Qué camina doña Berta cada mañana: la orilla o el bosque?", "La orilla", "El bosque es de don Elías."),
        ex("Don Elías dice que duerme mejor tras caminar. ¿Qué dimensión muestra? A) física B) espiritual", "A", "Habla del cuerpo."),
        ex("¿Qué agradece doña Berta antes de comer en familia?", "El alimento que vino del mar", "Así lo dice su testimonio."),
    ],
    C=[
        ex("Verdadero o falso: lo físico y lo espiritual pueden aparecer juntos en una misma práctica.", "Verdadero", "Caminar y agradecer pueden formar parte de una misma forma de vivir."),
        ex("¿Qué es un criterio de comparación? A) un punto igual para los dos testimonios, como «qué hace el cuerpo» B) la opinión de quien compara", "A", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: si dos testimonios se parecen, todos los pueblos viven igual la relación con la naturaleza.", "Falso", "Dos testimonios no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «qué sentido de respeto aparece». Don Elías: agradece lo que da la huerta. Doña Berta: da las gracias por el alimento del mar. ¿Qué semejanza hay? A) ambos agradecen lo que reciben de la naturaleza B) ninguno agradece", "A", "Los dos testimonios incluyen dar gracias."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambos caminan por un lugar natural b) uno vive junto a un bosque y el otro junto al mar.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Criterio: «qué se reserva». Don Elías: lugares del bosque. Doña Berta: conversaciones de la caleta. ¿Qué diferencia hay? A) ambos reservan lo mismo B) uno reserva lugares y la otra reserva conversaciones", "B", "Cada testimonio reserva algo distinto."),
    ],
    Z=[
        ex("Ana dice: «Doña Berta está más conectada con la naturaleza que don Elías porque vive junto al mar». ¿Qué falla en su comparación?", "Ordena dos casos sin criterio ni fuente", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como estas dos personas agradecen, todos los pueblos indígenas agradecen igual». ¿Qué debería escribir? A) «en todos los pueblos» B) «en estos dos testimonios»", "B", "Dos testimonios no permiten hablar de todos los pueblos."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos dos testimonios, caminar y agradecer aparecen unidos». 2) «Los pueblos de bosque entienden mejor la naturaleza que los de mar». ¿Cuál está bien formulada?", "La primera", "La segunda ordena a dos grupos."),
        ex("Alguien afirma que doña Berta «reza en la orilla». El testimonio solo dice que ella camina por la orilla y que hay conversaciones de la caleta que no cuenta. ¿Qué parte es interpretación? A) que rece en la orilla B) que camine por la orilla", "A", "El testimonio no habla de rezar ni de oraciones."),
    ],
    context=[ex("Tu curso arma un panel con dos formas de vivir la relación con la naturaleza. Una compañera quiere titularlo «Los indígenas sí cuidan y los demás, no». ¿Qué título respeta lo aprendido? A) «Dos testimonios sobre cuerpo, respeto y naturaleza» B) «Quién cuida mejor»", "A", "El título A compara sin jerarquizar.")],
    selfcheck=[
        ex("Escribe una relación entre una experiencia del cuerpo y un sentido de respeto con el testimonio de don Elías.", "Caminar por el bosque y agradecer lo que da la huerta", "Une lo físico con lo espiritual."),
        ex("Verdadero o falso: puedo ordenar dos comunidades de «más conectada» a «menos conectada».", "Falso", "Cada comunidad vive su relación a su manera."),
        ex("Tema: la relación con la naturaleza. Nombra un criterio de comparación para dos testimonios.", "Por ejemplo: qué se reserva", "Debe ser un punto igual para ambos."),
    ],
    task=T("Compara estos dos testimonios inventados. Don Elías, de Bosque Claro: «Camino por el bosque y duermo mejor. Agradezco lo que da la huerta. Hay lugares que no mostramos.» Doña Berta, de Costa Serena: «Camino por la orilla y me hace bien al cuerpo. Damos gracias por el alimento del mar. Hay conversaciones que no contamos.» Haz una tabla con tres criterios: «qué hace el cuerpo», «qué sentido de respeto aparece» y «qué se reserva». Escribe una semejanza, una diferencia y una frase que termine con «en estos dos testimonios».",
           "Cuerpo: camina por el bosque; camina por la orilla. Respeto: agradece lo que da la huerta; da gracias por el alimento del mar. Reserva: lugares; conversaciones. Semejanza: ambos caminan y agradecen. Diferencia: uno reserva lugares y la otra, conversaciones. Esto se ve en estos dos testimonios.",
           ["usa los mismos criterios para ambos", "distingue semejanza y diferencia", "no jerarquiza"], ["tabla de tres criterios", "semejanza y diferencia"], ["decir cuál comunidad está más conectada", "generalizar a todos los pueblos"],
           "Pedir que muestre en la tabla la fila que respalda cada semejanza; valorar que no ordene las comunidades."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «quién enseñó esa costumbre») y explica qué deberías preguntar para completarlo.",
)

L(
    OA11, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que analice la importancia de una relación armónica, física y espiritual con la naturaleza, con fuente, reflexión, límite y pregunta.",
    prior=["Sé relacionar experiencias del cuerpo con sentidos de respeto.", "Sé comparar dos testimonios sin jerarquizar."],
    explain=[
        "Una respuesta atribuida que analiza la relación armónica con la naturaleza tiene cinco partes. Primero, el dato de la fuente con su nombre: «Don Elías cuenta que…». Segundo, la dimensión física y la espiritual que aparecen. Tercero, tu reflexión sobre por qué esa relación es importante, marcada con «yo pienso que». Cuarto, un límite. Quinto, una pregunta para el educador tradicional.",
        "Analizar la importancia es explicar para qué sirve esa relación para la persona y para la comunidad. En los testimonios inventados, tomar solo lo necesario ayuda a que el bosque o el mar sigan dando alimento, y caminar y descansar cuidan el cuerpo. Estas son ideas que sacamos de los testimonios; no afirmamos que todos los pueblos las vivan igual.",
        "Una buena respuesta no inventa ceremonias, no exagera y no habla por todo un pueblo. Reconoce lo que no sabe y lo que la comunidad reserva. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("importancia", "para qué sirve algo y qué cambia si falta"), ("análisis", "explicar partes de algo y cómo se relacionan"), ("exagerar", "decir más de lo que la fuente dijo"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TBC + " Arma una respuesta atribuida de cinco partes.", ["Dato: don Elías cuenta que recoge solo frutos maduros y que agradece lo que da la huerta.", "Dimensiones: física, porque camina y duerme mejor; espiritual, porque agradece.", "Reflexión: yo pienso que tomar lo necesario ayuda a que el bosque siga dando frutos.", "Límite y pregunta: no sé qué se hace en los lugares reservados; preguntaré al educador tradicional."], "Respuesta con dato atribuido, dimensiones, «yo pienso que», límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «Todos los indígenas hablan con el bosque para curarse». ¿Qué le falta a la respuesta?", ["No dice de qué fuente viene el dato.", "Generaliza y agrega una práctica que nadie contó.", "No tiene límite ni pregunta."], "Le falta atribuir, no inventar prácticas y agregar límite y pregunta."),
    ],
    mistakes=[
        M("Inventar prácticas o ceremonias para que la respuesta suene completa.", "Puede ser falso y faltar el respeto a la comunidad.", "Escribe solo lo que la fuente contó y marca el límite."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a don Elías? A) «Don Elías cuenta que…» B) «Todos saben que…»", "A", "Nombra a la fuente."),
        ex("Tema: la relación con la naturaleza. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, dimensiones, reflexión, límite y pregunta."),
        ex("Tema: la relación con la naturaleza. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué es analizar la importancia de una relación con la naturaleza? A) copiar el testimonio B) explicar para qué sirve y qué cambia si falta", "B", "La importancia se explica con razones."),
        ex("Verdadero o falso: puedo afirmar que todos los pueblos viven la relación con la naturaleza igual que don Elías.", "Falso", "Un testimonio no representa a todos los pueblos."),
        ex("Tema: la relación con la naturaleza. ¿Para qué sirve la pregunta final? A) para consultar al educador tradicional lo que no sé B) para terminar rápido", "A", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de doña Berta: «Le enseño a mi nieta a no tomar más conchas de las que necesitamos». Completa la atribución: «Doña Berta cuenta que le enseña a su nieta a…»", "No tomar más conchas de las que necesitan", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Berta cuenta que camina por la orilla cada mañana b) yo pienso que caminar así cuida su cuerpo.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una reflexión dice: «Don Elías cuenta que deja frutos para los animales; yo pienso que eso ayuda a que el bosque siga dando». ¿Qué parte es la reflexión?", "Yo pienso que eso ayuda a que el bosque siga dando", "Es la idea de quien escribe."),
    ],
    Z=[
        ex("Tema: la relación con la naturaleza. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar más datos inventados B) agregar lo que no sé o no se cuenta", "B", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque es una tarea de decoración B) porque conoce la relación de su pueblo con la naturaleza y puede corregir errores", "B", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Berta cuenta que da gracias por el alimento del mar; yo pienso que eso muestra respeto». 2) «Doña Berta demuestra que su pueblo es el que mejor respeta el mar». ¿Cuál está bien construida?", "La primera", "La segunda exagera y jerarquiza."),
        ex("Un compañero agrega que en Costa Serena «seguro hay una ceremonia del mar». El testimonio no la menciona. ¿Qué debe hacer?", "Quitarla porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre por qué es importante la relación con la naturaleza para la comunidad de Bosque Claro. ¿Qué empieza mejor? A) «Todos los pueblos indígenas dicen que…» B) «Don Elías cuenta que…»", "B", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre la relación con la naturaleza.", "Dato de la fuente, dimensiones, reflexión, límite y pregunta", "Están en la explicación."),
        ex("Tema: la relación con la naturaleza. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: la relación con la naturaleza. ¿Qué haces al terminar? A) guardarlo sin mostrarlo B) mostrarlo a la comunidad o al educador para que lo revise", "B", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de don Elías: «Los fines de semana subimos al río con los niños. Les enseño a mirar sin molestar a los animales. Después del paseo, agradecemos lo que vimos. De los lugares del bosque no hablamos con visitas.» Escribe una respuesta de cinco partes sobre la importancia de esta relación con la naturaleza: 1) dato de don Elías, 2) dimensiones física y espiritual que aparecen, 3) tu reflexión con «yo pienso que», 4) un límite y 5) una pregunta para el educador tradicional.",
           "1) Don Elías cuenta que sube al río con los niños, les enseña a mirar sin molestar a los animales y agradecen lo que vieron. 2) Física: caminar y subir al río. Espiritual: agradecer. 3) Yo pienso que enseñar a respetar a los animales ayuda a que los niños cuiden el bosque. 4) No sé por qué agradecen después del paseo. 5) Pregunta: ¿cómo enseña mi pueblo a respetar la naturaleza a los más pequeños?",
           ["atribuye cada dato", "analiza la importancia con razones", "incluye límite y pregunta"], ["texto de cinco partes"], ["generalizar a todos los pueblos", "inventar prácticas"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu respuesta con el testimonio de doña Berta y su caminata por la orilla.",
)

L(
    OA11, 5, materials=MAT,
    use="Aprenderé a contrastar sin jerarquizar la relación con la naturaleza que cuentan tres personas: una de una comunidad indígena inventada y dos de otros contextos. Sirve para considerar la visión de otros pueblos sin dejar de valorar las demás.",
    prior=["Sé armar una respuesta atribuida.", "Sé comparar dos testimonios con criterios iguales."],
    explain=[
        "Contrastar es poner varios testimonios uno al lado de otro para ver en qué coinciden y en qué se diferencian. Sin jerarquizar quiere decir que no ordenamos a las personas de «mejor relación» a «peor relación». El objetivo es entender cómo cada una cuida su cuerpo y su sentido de respeto con la naturaleza.",
        "Comparamos tres testimonios inventados: don Elías, de Bosque Claro; doña Berta, de Costa Serena; y Valentina, una escolar de ciudad que va a un parque. Los tres cuentan una experiencia del cuerpo y un cuidado hacia la naturaleza. Valentina no habla desde una comunidad indígena, pero su testimonio también vale como fuente de lo que ella vive.",
        "Evitamos dos errores. El primero es creer que solo las comunidades indígenas tienen una relación con la naturaleza. El segundo es creer que cualquier relación es igual a otra sin mirar sus diferencias. Para eso usamos criterios iguales para las tres fuentes y aclaramos al final que tres testimonios no representan a todos.",
    ],
    vocab=[("contrastar", "poner varios testimonios juntos para ver en qué coinciden y en qué se diferencian"), ("jerarquizar", "ordenar de mejor a peor"), ("coincidencia", "punto en que dos o más fuentes dicen algo parecido"), ("criterio", "punto de comparación igual para todas las fuentes"), ("contexto", "lugar y situación en que vive una persona")],
    worked=[
        W("Contrastar tres testimonios", TBC + " " + TCS + " " + TCV + " Criterio: «cuidado hacia la naturaleza». ¿En qué coinciden?", ["Don Elías: deja frutos para los animales.", "Doña Berta: no toma más conchas de las que necesitan.", "Valentina: cuida de no dejar basura en el parque.", "Las tres personas cuidan algo de la naturaleza."], "Coinciden en que las tres personas cuidan algo de la naturaleza."),
        W("Detectar una jerarquía", "Un niño dice: «Valentina no sabe de naturaleza porque vive en la ciudad». ¿Qué error hay?", ["Valentina cuenta que se calma con los árboles y cuida el parque.", "Su contexto es distinto, pero su testimonio vale.", "El niño la descarta sin mirar lo que ella dijo."], "Descarta un testimonio por el lugar donde vive la persona, en vez de leerlo."),
    ],
    mistakes=[
        M("Decir que solo las comunidades indígenas se relacionan con la naturaleza.", "Todas las personas tienen alguna relación con ella.", "Describe qué cuenta cada fuente."),
        M("Decir que todas las relaciones son iguales sin mirar sus diferencias.", "Cada contexto tiene sus propias maneras.", "Compara con criterios iguales y anota semejanzas y diferencias."),
    ],
    R=[
        ex("¿Quién cuida de no dejar basura en el parque: Valentina o doña Berta?", "Valentina", "Doña Berta habla de la orilla y las conchas."),
        ex("Contrastar, ¿es poner testimonios juntos para ver coincidencias y diferencias o es elegir el mejor?", "Poner testimonios juntos para ver coincidencias y diferencias", "Contrastar no es elegir el mejor."),
        ex("¿Qué dice don Elías que deja para los animales? A) troncos B) frutos", "B", "Su testimonio dice que deja frutos."),
    ],
    C=[
        ex("Verdadero o falso: el testimonio de una escolar de ciudad no vale porque no es de una comunidad indígena.", "Falso", "Todo testimonio vale como fuente de lo que cuenta su autor."),
        ex("¿Por qué se usan criterios iguales para las tres fuentes? A) para llenar la tabla B) para no tratar a una mejor que otra", "B", "Los criterios iguales evitan el trato desigual."),
        ex("Verdadero o falso: tres testimonios bastan para decir cómo viven todas las personas su relación con la naturaleza.", "Falso", "Tres testimonios no representan a todos."),
    ],
    A=[
        ex("Criterio: «qué hace el cuerpo». Don Elías: camina por el bosque. Doña Berta: camina por la orilla. Valentina: mira los árboles del parque y se calma. ¿Quién menciona sentirse en calma?", "Valentina", "Es la única que lo dice."),
        ex("Clasifica en COINCIDENCIA o DIFERENCIA: a) las tres personas cuidan algo de la naturaleza b) una vive junto a un bosque, otra junto al mar y otra en una ciudad.", "a coincidencia, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Una compañera dice: «Valentina cuida el parque solo porque la profesora la obliga». El testimonio no lo dice. ¿Qué parte es interpretación? A) que va al parque B) toda la frase", "B", "El testimonio no explica la razón."),
    ],
    Z=[
        ex("Ana dice: «Don Elías respeta más la naturaleza que Valentina». ¿Qué falla en su comparación?", "Ordena dos casos sin criterio ni fuente", "Contrastar no es jerarquizar."),
        ex("Un compañero concluye: «Solo las comunidades indígenas cuidan la naturaleza». ¿Qué evidencia contradice esa idea? A) el testimonio de Valentina B) el testimonio de ninguno", "A", "Valentina, que no es de una comunidad indígena, cuida el parque."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos tres testimonios, las personas cuidan algo de la naturaleza de maneras distintas». 2) «Todas las personas de ciudad cuidan menos». ¿Cuál está bien formulada?", "La primera", "La segunda generaliza y ordena."),
        ex("Un grupo quiere preguntarle a una comunidad real cómo vive su relación con la naturaleza. ¿Qué hace primero? A) enviar una encuesta sin avisar B) pedir permiso y preguntar al educador tradicional cómo hacerlo", "B", "Las preguntas a una comunidad se hacen con permiso."),
    ],
    context=[ex("Tu curso arma un cartel sobre cómo cuidar la naturaleza. Una compañera quiere escribir «Cuidar la naturaleza es cosa de indígenas». ¿Qué corrección respeta lo aprendido? A) «Muchas personas, de distintos contextos, cuidan la naturaleza a su manera» B) dejar la frase", "A", "La frase A evita excluir y no jerarquiza.")],
    selfcheck=[
        ex("Nombra dos errores que se evitan al contrastar.", "Creer que solo los indígenas se relacionan con la naturaleza y creer que todas las relaciones son iguales", "Son los dos errores de la explicación."),
        ex("Verdadero o falso: puedo ordenar tres testimonios de mejor a peor.", "Falso", "Contrastar no es jerarquizar."),
        ex("Tema: la relación con la naturaleza. Nombra un criterio de contraste para tres testimonios.", "Por ejemplo: cuidado hacia la naturaleza", "Debe ser un punto igual para todos."),
    ],
    task=T("Contrasta estos tres testimonios inventados. Don Elías: «Dejo frutos para los animales y agradezco lo que da la huerta». Doña Berta: «Camino por la orilla, no tomo más conchas de las que necesito y damos gracias por el alimento del mar». Valentina: «Cuando miro los árboles del parque me calmo y cuido de no dejar basura». Haz una tabla con tres criterios: «qué hace el cuerpo o qué siente», «qué cuidado hacia la naturaleza» y «qué agradece o valora». Escribe una coincidencia, una diferencia y una frase que muestre cómo evitarías jerarquizar.",
           "Cuerpo o sentir: don Elías, en esta cita, no lo dice; doña Berta camina; Valentina se calma. Cuidado: deja frutos; no toma de más; no deja basura. Valora: la huerta; el alimento del mar; los árboles. Coincidencia: las tres cuidan algo de la naturaleza. Diferencia: cada una lo hace en un contexto distinto. Para no jerarquizar, comparo con los mismos criterios y no digo quién respeta más.",
           ["usa los mismos criterios para las tres", "distingue coincidencia y diferencia", "muestra cómo evitar jerarquizar"], ["tabla de tres criterios", "coincidencia, diferencia y frase"], ["decir cuál relación es mejor", "excluir un testimonio por su contexto"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que no ordene las relaciones."),
    reinforce="Marca en la tabla con un color las coincidencias y con otro las diferencias.",
    extend="Agrega un cuarto testimonio inventado de otro contexto y explica qué criterio permitiría compararlo con los otros tres.",
)

# ------------------------------------------------------------------ OA 12
FAV = ("Ficha situada (inventada). Comunidad: Alto Verde (no es un pueblo real). Territorio: un valle con canales de riego, chacras y cerros. "
       "Fuente y responsable: doña Marisol, vecina de la comunidad. Fecha: la de hoy, de ejemplo. Permiso: doña Marisol autorizó usar esta ficha en la escuela. "
       "Límite: no se cuenta cómo es el momento de agradecimiento que la comunidad hace en privado.")
TAV = ("Testimonio inventado de doña Marisol, de Alto Verde: «Antes de sembrar, nos juntamos todas las familias a limpiar el canal. Después hay un momento de agradecimiento que no mostramos a visitas. "
       "Al final compartimos una comida entre todos.»")
TFC = ("Testimonio inventado de don Segundo, de Pueblo Trigal (pueblo campesino, no indígena): «Cuando termina la cosecha, el pueblo hace una fiesta con comida y música para agradecer el año. "
       "Todos ayudan a armar la plaza. Los más viejos cuentan cómo eran las cosechas de antes.»")

L(
    OA12, 1, materials=MAT,
    use="Aprenderé a situar una actividad espiritual o sociocultural: de qué comunidad es, quién la cuenta y qué no se cuenta. Sirve para valorar su importancia sin describir lo que la comunidad reserva.",
    prior=["Sé situar una comunidad con su ficha.", "Sé que una relación armónica con la naturaleza se puede mirar desde el cuerpo y desde el sentido espiritual."],
    explain=[
        "Una actividad sociocultural es algo que una comunidad hace junta y que fortalece su vida compartida: un trabajo en común, una comida, una fiesta, un momento de enseñanza. Una actividad espiritual es una práctica que expresa respeto, gratitud o sentido hacia lo que rodea a la comunidad. Muchas veces ambas se juntan en una misma ocasión.",
        "Estas actividades mantienen el equilibrio entre el ser humano, la naturaleza y el cosmos. El cosmos es el universo que rodea a las personas: la tierra, el cielo y todo lo que existe, y cada cultura lo entiende a su manera. El equilibrio es una relación en que nada se toma ni se da en exceso y todos los elementos se cuidan.",
        "Antes de valorar una actividad hay que situarla. La ficha situada dice la comunidad, el territorio, la fuente, el permiso y el límite. Con ella sabemos de quién es el relato y qué no se cuenta. Muchas actividades espirituales no se describen a quien no pertenece a la comunidad, y respetar ese límite es parte de valorarlas.",
    ],
    vocab=[("actividad sociocultural", "algo que una comunidad hace junta y que fortalece su vida compartida"), ("actividad espiritual", "práctica que expresa respeto, gratitud o sentido hacia lo que rodea a la comunidad"), ("cosmos", "universo que rodea a las personas, que cada cultura entiende a su manera"), ("equilibrio", "relación en que nada se toma ni se da en exceso y todo se cuida"), ("fuente", "persona o texto que entrega el dato")],
    worked=[
        W("Leer una ficha situada", FAV + " ¿De quién es el relato y qué no se cuenta?", ["La comunidad es Alto Verde y la fuente es doña Marisol.", "Ella dio permiso para usar la ficha en la escuela.", "El límite dice que no se cuenta cómo es el momento de agradecimiento privado."], "El relato es de doña Marisol, de Alto Verde; no se cuenta cómo es el momento de agradecimiento privado."),
        W("Distinguir tipos de actividad", "Doña Marisol cuenta que las familias limpian juntas el canal y que después comparten una comida. ¿Qué tipo de actividad es?", ["Limpiar el canal juntas es un trabajo en común.", "Compartir una comida fortalece la vida compartida.", "Las dos son actividades socioculturales."], "Son actividades socioculturales."),
    ],
    mistakes=[
        M("Pensar que toda actividad espiritual se puede describir con detalles a cualquier persona.", "Muchas se reservan dentro de la comunidad.", "Escribe solo lo que la fuente contó y marca el límite."),
        M("Decir que la actividad de Alto Verde es la de todos los pueblos indígenas.", "La ficha habla de una sola comunidad.", "Escribe «según doña Marisol, en Alto Verde…»."),
    ],
    R=[
        ex("Según la ficha de Alto Verde, ¿quién es la fuente?", "Doña Marisol", "La ficha la nombra como fuente y responsable."),
        ex("¿Qué territorio tiene Alto Verde? A) un valle con canales de riego, chacras y cerros B) una caleta con puerto", "A", "La caleta y el puerto son de otras fichas."),
        ex("La ficha de Alto Verde dice que no se cuenta cómo es el momento de agradecimiento. ¿Lo describes en tu trabajo? Responde Sí o No.", "No", "El límite de la ficha lo prohíbe."),
    ],
    C=[
        ex("En Lengua y Cultura, ¿qué es una actividad sociocultural? A) algo que una comunidad hace junta y que fortalece su vida compartida B) algo que hace una sola persona en secreto", "A", "Es una actividad de la comunidad."),
        ex("Verdadero o falso: el cosmos es el universo que rodea a las personas y cada cultura lo entiende a su manera.", "Verdadero", "Esa es la definición de cosmos."),
        ex("Verdadero o falso: las actividades espirituales y socioculturales no pueden darse en una misma ocasión.", "Falso", "Muchas veces ambas se juntan."),
    ],
    A=[
        ex("Clasifica en SOCIOCULTURAL o ESPIRITUAL: a) las familias limpian juntas el canal b) la comunidad hace un momento de agradecimiento.", "a sociocultural, b espiritual", "La primera es un trabajo en común; la segunda expresa gratitud."),
        ex("Doña Marisol dice: «Al final compartimos una comida entre todos». ¿Qué fortalece esa actividad? A) la venta de verdura B) la vida compartida de la comunidad", "B", "Comer juntos une a las personas."),
        ex("Una compañera trae una ficha con comunidad y fuente, pero sin límite. ¿Qué falta? A) la hora de la actividad B) lo que no se puede contar", "B", "El límite dice qué no se cuenta."),
    ],
    Z=[
        ex("Pablo escribe: «En Alto Verde hacen un rito con tales palabras». La ficha no cuenta palabras. ¿Qué error comete?", "Inventa lo que la comunidad reserva", "El límite pide no describir ese momento."),
        ex("¿Por qué respetar el límite de una ficha es parte de valorar una actividad espiritual? A) porque cuidar lo reservado es una forma de respeto B) porque lo reservado no importa", "A", "Respetar lo que la comunidad guarda muestra valoración."),
    ],
    D=[
        ex("Una ficha dice solo: «Comunidad: Alto Verde. Actividad: limpieza del canal». ¿Qué datos de una ficha situada faltan?", "Fuente, permiso y límite", "La ficha situada exige esos tres datos además de comunidad y territorio."),
        ex("Un cartel dice: «Todos los pueblos limpian un canal antes de sembrar». ¿Qué corriges? A) lo dejo igual B) escribo «según doña Marisol, en Alto Verde (comunidad inventada)…»", "B", "El cartel debe atribuir el dato a esa fuente."),
    ],
    context=[ex("Tu escuela quiere invitar a una comunidad real para mostrar una de sus actividades. Un compañero propone filmarla sin avisar. ¿Qué haces? A) pido permiso y consulto qué se puede compartir B) filmamos y preguntamos después", "A", "Las actividades de una comunidad se comparten con su permiso.")],
    selfcheck=[
        ex("Nombra las dos clases de actividad de esta lección.", "Sociocultural y espiritual", "Son las dos de la explicación."),
        ex("Verdadero o falso: el equilibrio es una relación en que nada se toma ni se da en exceso.", "Verdadero", "Esa es la definición de equilibrio."),
        ex("Ante una duda sobre una actividad de una comunidad real, ¿qué haces? A) la supongo B) pregunto al educador tradicional", "B", "Él o ella es la fuente."),
    ],
    task=T("Lee esta nota inventada de doña Marisol: «En Alto Verde las familias nos juntamos al comenzar el riego. Limpiamos los canales y hay una comida compartida. Después hay un momento que no contamos a visitas.» Haz una ficha con: comunidad, actividad sociocultural, fuente, qué dice la fuente y un límite. Luego escribe una frase con «Yo pienso que…» sobre cómo esa actividad puede cuidar el equilibrio entre las personas y la naturaleza.",
           "Comunidad: Alto Verde. Actividad sociocultural: limpiar canales y compartir una comida. Fuente: doña Marisol. Dice: las familias se juntan al comenzar el riego. Límite: no se cuenta el momento privado. Yo pienso que limpiar los canales juntas cuida el agua que usa la comunidad.",
           ["completa la ficha con datos de la nota", "separa lo que dice la fuente de lo que piensa", "pone un límite"], ["ficha completa", "frase con «Yo pienso que»"], ["describir el momento privado", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la nota está cada dato; valorar que respete el límite."),
    reinforce="Subraya en la ficha de Alto Verde la comunidad, la fuente, el permiso y el límite con cuatro colores.",
    extend="Explica con tus palabras por qué una comida compartida puede ser parte del equilibrio de una comunidad.",
)

L(
    OA12, 2, materials=MAT,
    use="Aprenderé a leer un testimonio sobre una actividad espiritual o sociocultural con límites declarados: qué dice la fuente, qué tipo de actividad es, qué interpreto yo y qué no se cuenta.",
    prior=["Sé situar una actividad con su ficha.", "Sé distinguir actividad espiritual de sociocultural."],
    explain=[
        "Un testimonio sobre una actividad puede contar quiénes participan, qué hacen, cuándo y para qué. Para leerlo con respeto separamos cuatro cosas. Lo que la fuente dice, con sus palabras. El tipo de actividad que muestra cada frase: sociocultural o espiritual. Lo que yo interpreto, que es una idea mía. Y lo que no se cuenta o no sé.",
        "En el testimonio de doña Marisol, limpiar el canal y compartir una comida son actividades socioculturales, y el momento de agradecimiento es espiritual y reservado. Ella no dice cómo es ese momento. Si yo lo describo con palabras o gestos, estoy inventando algo que la comunidad decidió no mostrar.",
        "Leer con límites declarados significa decir hasta dónde llega lo que afirmo. Si algo no se cuenta, escribo «el testimonio no lo dice» y no lo rellenamos. Para saber más sobre una actividad real preguntamos al educador o a la educadora tradicional, que sabe qué se puede compartir.",
    ],
    vocab=[("participar", "tomar parte en una actividad"), ("interpretar", "dar una idea propia sobre lo que se lee"), ("reservado", "lo que una comunidad prefiere no compartir con todos"), ("tipo de actividad", "sociocultural o espiritual, según lo que expresa"), ("límite", "lo que no se cuenta o no se sabe")],
    worked=[
        W("Separar cuatro cosas", TAV + " Separa lo que dice, el tipo de actividad, lo que interpreto y lo que no se cuenta.", ["Dice: antes de sembrar, las familias se juntan a limpiar el canal y al final comparten una comida.", "Tipo: limpiar el canal y compartir la comida son socioculturales; el momento de agradecimiento es espiritual.", "Interpreto: yo pienso que limpiar juntos ayuda a que todos tengan agua.", "No se cuenta: cómo es el momento de agradecimiento."], "Dice: se juntan a limpiar el canal y comparten una comida. Tipo: sociocultural y espiritual. Interpreto: ayuda a que todos tengan agua. No se cuenta: cómo es el agradecimiento."),
        W("Detectar una invención", "Un niño escribe: «Doña Marisol cuenta que en el agradecimiento se dicen estas palabras…». ¿Está bien?", ["Reviso el testimonio: dice que hay un momento de agradecimiento que no se muestra.", "No contó palabras ni gestos.", "El niño inventó lo que la comunidad reserva."], "No: inventa lo que la comunidad reserva."),
    ],
    mistakes=[
        M("Describir con detalles lo que la fuente dijo que se reserva.", "Se inventa y se falta el respeto a la comunidad.", "Escribe «el testimonio no lo dice»."),
        M("Escribir mi interpretación como si la hubiera dicho la fuente.", "Se atribuye a la comunidad algo que no dijo.", "Marca mis ideas con «yo pienso que»."),
    ],
    R=[
        ex("Según doña Marisol, ¿qué hacen las familias antes de sembrar: limpiar el canal o cosechar?", "Limpiar el canal", "El testimonio lo dice así."),
        ex("Tema: las actividades de la comunidad. Una interpretación, ¿es una idea mía o un dato de la fuente?", "Una idea mía", "Interpretar es dar mi propia idea."),
        ex("Si el testimonio no cuenta cómo es el agradecimiento, ¿qué escribes? A) lo describo yo B) el testimonio no lo dice", "B", "No se inventan prácticas."),
    ],
    C=[
        ex("Doña Marisol dice: «Al final compartimos una comida entre todos». ¿Qué tipo de actividad es? A) un secreto B) sociocultural", "B", "Comer juntos fortalece la vida compartida."),
        ex("Verdadero o falso: si la comunidad reserva un momento, puedo describirlo «con lo que seguro hacen».", "Falso", "Eso sería inventar."),
        ex("Verdadero o falso: respetar lo reservado es parte de valorar la actividad.", "Verdadero", "Cuidar lo reservado muestra respeto."),
    ],
    A=[
        ex("Doña Marisol dice: «Antes de sembrar, nos juntamos todas las familias a limpiar el canal». Clasifica en DICE LA FUENTE o INTERPRETO: a) las familias se juntan a limpiar el canal b) limpiar juntas hace más fuertes a las familias.", "a dice la fuente, b interpreto", "La segunda es una idea de quien lee."),
        ex("Don Segundo, de un pueblo campesino, dice: «Todos ayudan a armar la plaza». ¿Qué cuenta ese dato? A) que la fiesta se prepara entre todos B) que la plaza es de una persona", "A", "El testimonio habla de ayuda de todos."),
        ex("Un niño escribe: «Doña Marisol cuenta que agradecen al cerro». ¿Qué dato no está en el testimonio?", "Que agradecen al cerro", "El testimonio no dice a quién ni cómo agradecen."),
    ],
    Z=[
        ex("Rodrigo escribe, sin marcarlo: «El agradecimiento de Alto Verde es una ceremonia muy antigua». ¿Qué debería hacer con esa frase?", "Quitarla porque no está en la fuente", "El testimonio no dice nada de antigüedad."),
        ex("Tema: las actividades de la comunidad. ¿Por qué conviene escribir los límites al final del trabajo? A) para mostrar hasta dónde llega lo afirmado B) para llenar la hoja", "A", "Los límites muestran lo que no se sabe ni se cuenta."),
    ],
    D=[
        ex("Dos frases. 1) «Doña Marisol cuenta que comparten una comida al final». 2) «Doña Marisol cuenta que la comida es una ofrenda». ¿Cuál se queda en la fuente?", "La primera", "La segunda agrega un sentido que el testimonio no dice."),
        ex("Doña Marisol no contó cuántas familias participan. ¿Qué escribes en los límites? A) no sé cuántas familias participan B) participan quince familias", "A", "Declarar lo que no sé evita inventar."),
    ],
    context=[ex("Para un afiche escolar, un compañero quiere dibujar el momento de agradecimiento «con gente de rodillas». El testimonio no dice nada de eso. ¿Qué le dices? A) que no lo dibuje porque no está en la fuente B) que lo dibuje igual", "A", "No se inventan prácticas que la fuente no cuenta.")],
    selfcheck=[
        ex("Nombra las cuatro cosas que separo al leer un testimonio sobre una actividad.", "Lo que dice la fuente, el tipo de actividad, lo que interpreto y lo que no se cuenta", "Son los pasos de la lectura con límites."),
        ex("Tema: las actividades de la comunidad. Verdadero o falso: puedo completar con mi imaginación lo que la comunidad no contó.", "Falso", "Eso sería inventar."),
        ex("Tema: las actividades de la comunidad. ¿Qué escribes cuando el testimonio no explica algo? Escribe una frase corta.", "El testimonio no lo dice", "Es la manera honesta de marcar un vacío."),
    ],
    task=T("Lee este testimonio inventado de doña Marisol: «Cuando termina la siembra, las familias nos reunimos en la sede. Los mayores cuentan cómo se trabajaba antes y los niños escuchan. Después hay una comida y un momento de agradecimiento que no mostramos.» Haz cuatro columnas: «La fuente dice», «Tipo de actividad», «Yo interpreto» y «No se cuenta». Pon al menos un dato en cada una. Cierra con una frase de límites.",
           "La fuente dice: las familias se reúnen en la sede; los mayores cuentan cómo se trabajaba antes y los niños escuchan; hay una comida. Tipo: la reunión y la comida son socioculturales; el agradecimiento es espiritual. Yo interpreto: yo pienso que los niños aprenden de los mayores. No se cuenta: el momento de agradecimiento. Límite: no sé cuándo se hace cada parte.",
           ["separa cuatro columnas", "usa datos del testimonio", "marca sus ideas como interpretación"], ["tabla de cuatro columnas", "frase de límites"], ["escribir interpretaciones como datos", "describir el momento privado"],
           "Pedir que indique en qué línea del testimonio está cada dato; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice la fuente y con otro lo que interpretas en el testimonio de doña Marisol.",
    extend="Explica por qué contar solo una parte de una actividad también puede ser una manera de cuidar lo que la comunidad guarda.",
)

L(
    OA12, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre una actividad y el equilibrio entre las personas, la naturaleza y el cosmos, comparando una actividad de una comunidad indígena inventada con la fiesta de un pueblo campesino, sin decir que una es mejor.",
    prior=["Sé leer un testimonio con límites.", "Sé qué es una actividad sociocultural y una espiritual."],
    explain=[
        "Una relación entre una actividad y el equilibrio explica para qué sirve esa actividad. Por ejemplo: limpiar el canal entre todos ayuda a que el agua llegue a todas las chacras (equilibrio entre las personas y la naturaleza). Un momento de agradecimiento puede expresar respeto hacia lo que da la tierra y el cielo (equilibrio con el cosmos). Decimos siempre que es una relación que la fuente nombra o que yo propongo.",
        "Comparamos dos testimonios inventados: el de doña Marisol, de Alto Verde, y el de don Segundo, de Pueblo Trigal, un pueblo campesino no indígena. En ambos, la comunidad se junta a trabajar, a compartir comida y a agradecer. Hay diferencias: una limpia canales antes de sembrar y la otra hace fiesta después de la cosecha.",
        "Para comparar usamos los mismos criterios en las dos tablas: cuándo se hace, quiénes participan y qué se agradece o se cuida. No decimos que una actividad sea «más espiritual» que la otra. Y dos testimonios no bastan para decir que todos los pueblos hacen lo mismo.",
    ],
    vocab=[("equilibrio", "relación en que nada se toma ni se da en exceso y todo se cuida"), ("agradecer", "reconocer con respeto lo que se recibió"), ("cosecha", "recoger lo que dio la siembra"), ("semejanza", "algo parecido entre dos actividades"), ("diferencia", "algo distinto entre dos actividades")],
    worked=[
        W("Relacionar actividad y equilibrio", TAV + " ¿Para qué sirve limpiar el canal entre todos?", ["Antes de sembrar se limpia el canal.", "Un canal limpio deja pasar el agua a las chacras.", "Entonces la actividad ayuda a que el agua llegue a todas: cuida a las personas y a la naturaleza."], "Limpiar el canal entre todos ayuda a que el agua llegue a todas las chacras, cuidando el equilibrio entre las personas y la naturaleza."),
        W("Comparar con un criterio", TFC + " Criterio: «cuándo se hace». Alto Verde: antes de sembrar. Pueblo Trigal: cuando termina la cosecha. ¿Qué diferencia hay?", ["Alto Verde se junta antes de sembrar.", "Pueblo Trigal se junta al terminar la cosecha.", "Una actividad es al comenzar el ciclo y la otra, al terminarlo."], "Diferencia: una actividad es antes de sembrar y la otra, después de la cosecha."),
    ],
    mistakes=[
        M("Decir que una actividad es «más espiritual» que otra.", "Comparar no es ordenar.", "Describe semejanzas y diferencias con los mismos criterios."),
        M("Concluir que todos los pueblos hacen lo mismo porque dos testimonios se parecen.", "Dos ejemplos no representan a todos los pueblos.", "Escribe «en estos dos testimonios» y no más."),
    ],
    R=[
        ex("¿Cuándo se junta Pueblo Trigal para hacer la fiesta: antes de sembrar o cuando termina la cosecha?", "Cuando termina la cosecha", "Así lo dice don Segundo."),
        ex("En Alto Verde, ¿qué limpian las familias? A) la plaza B) el canal", "B", "La plaza es de Pueblo Trigal."),
        ex("En Pueblo Trigal, ¿quiénes ayudan a armar la plaza?", "Todos", "El testimonio lo dice."),
    ],
    C=[
        ex("Verdadero o falso: comparar dos actividades significa decir cuál es más espiritual.", "Falso", "Comparar es buscar semejanzas y diferencias."),
        ex("¿Qué es un criterio de comparación? A) un punto igual para las dos actividades, como «cuándo se hace» B) la opinión de quien compara", "A", "El criterio permite comparar con el mismo punto."),
        ex("Verdadero o falso: si dos testimonios se parecen, todos los pueblos hacen lo mismo.", "Falso", "Dos testimonios no representan a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «quiénes participan». Alto Verde: todas las familias. Pueblo Trigal: todos los vecinos. ¿Qué semejanza hay? A) en ambos participa una sola persona B) en ambos participa toda la comunidad", "B", "Los dos testimonios hablan de participación de todos."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas comunidades comparten comida b) una limpia canales y la otra arma una plaza para la fiesta.", "a semejanza, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Don Segundo dice: «Los más viejos cuentan cómo eran las cosechas de antes». ¿Qué cumple esa práctica? A) transmitir lo vivido a los más jóvenes B) vender la cosecha", "A", "Contar lo de antes enseña a los jóvenes."),
    ],
    Z=[
        ex("Ana dice: «La actividad de Alto Verde es más espiritual que la fiesta de Pueblo Trigal». ¿Qué falla en su comparación?", "Ordena dos actividades sin criterio ni fuente", "Comparar no es jerarquizar."),
        ex("Un compañero escribe: «Como estas dos comunidades se juntan a trabajar y a comer, todos los pueblos lo hacen». ¿Qué debería escribir? A) «en estos dos testimonios» B) «en todos los pueblos»", "A", "Dos testimonios no permiten hablar de todos los pueblos."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos dos testimonios, la comunidad se junta a trabajar, compartir comida y agradecer». 2) «Los pueblos campesinos celebran menos que los indígenas». ¿Cuál está bien formulada?", "La primera", "La segunda ordena a dos grupos."),
        ex("Alguien afirma que don Segundo «hace una ofrenda». El testimonio solo dice que hacen fiesta con comida y música para agradecer el año. ¿Qué parte es interpretación? A) que hagan fiesta B) que sea una ofrenda", "B", "El testimonio no dice nada de ofrendas."),
    ],
    context=[ex("Tu curso prepara un mural sobre actividades de comunidades. Una compañera quiere titularlo «Los indígenas hacen ritos y los demás, fiestas». ¿Qué título respeta lo aprendido? A) «Quién agradece mejor» B) «Dos testimonios de actividades que reúnen a la comunidad»", "B", "El título A compara sin jerarquizar.")],
    selfcheck=[
        ex("Escribe una relación entre una actividad y el equilibrio con el testimonio de doña Marisol.", "Limpiar el canal entre todos ayuda a que el agua llegue a todas las chacras", "Une la actividad con su efecto en el equilibrio."),
        ex("Verdadero o falso: puedo ordenar dos actividades de «más espiritual» a «menos espiritual».", "Falso", "Cada comunidad vive sus actividades a su manera."),
        ex("Nombra un criterio de comparación para dos actividades.", "Por ejemplo: cuándo se hace", "Debe ser un punto igual para ambas."),
    ],
    task=T("Compara estas dos actividades inventadas. Alto Verde (doña Marisol): «Antes de sembrar limpiamos el canal entre todas las familias y compartimos una comida; hay un momento que no contamos». Pueblo Trigal (don Segundo): «Al terminar la cosecha hacemos una fiesta con comida y música para agradecer el año; todos ayudan». Haz una tabla con tres criterios: «cuándo se hace», «quiénes participan» y «qué se agradece o se cuida». Escribe una semejanza, una diferencia y una frase que termine con «en estos dos testimonios».",
           "Cuándo: antes de sembrar; al terminar la cosecha. Quiénes: todas las familias; todos. Se agradece o cuida: el agua del canal; el año de cosecha. Semejanza: ambas reúnen a toda la comunidad y comparten comida. Diferencia: una es antes de sembrar y la otra, después de cosechar. Esto se ve en estos dos testimonios.",
           ["usa los mismos criterios para ambas", "distingue semejanza y diferencia", "no jerarquiza"], ["tabla de tres criterios", "semejanza y diferencia"], ["decir cuál actividad es más espiritual", "generalizar a todos los pueblos"],
           "Pedir que muestre en la tabla la fila que respalda cada semejanza; valorar que no ordene las actividades."),
    reinforce="Marca en la tabla con un color las semejanzas y con otro las diferencias.",
    extend="Agrega un cuarto criterio (por ejemplo, «qué aprenden los niños») y explica qué deberías preguntar para completarlo.",
)

L(
    OA12, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore la importancia de una actividad espiritual o sociocultural para mantener el equilibrio entre las personas, la naturaleza y el cosmos, con fuente, reflexión, límite y pregunta.",
    prior=["Sé relacionar una actividad con el equilibrio.", "Sé comparar dos actividades sin jerarquizar."],
    explain=[
        "Una respuesta atribuida que valora una actividad tiene cinco partes. Primero, el dato de la fuente con su nombre: «Doña Marisol cuenta que…». Segundo, el tipo de actividad: sociocultural o espiritual. Tercero, tu reflexión sobre por qué es importante para el equilibrio, marcada con «yo pienso que». Cuarto, un límite. Quinto, una pregunta para el educador tradicional.",
        "Valorar una actividad es reconocer lo que hace por la comunidad: reúne a las personas, enseña a los más jóvenes, cuida el agua o la tierra y expresa respeto y gratitud. No es lo mismo que participar en ella: muchas actividades espirituales pertenecen solo a la comunidad y se miran desde afuera con respeto, sin imitarlas.",
        "Una buena respuesta no describe lo que la comunidad reserva, no exagera y no habla por todo un pueblo. Reconoce lo que no sabe. Al final se devuelve a la comunidad o al educador, para que la revise y corrija lo que no esté bien dicho.",
    ],
    vocab=[("valorar", "reconocer que algo tiene importancia y sentido para quienes lo viven"), ("respuesta atribuida", "respuesta en que cada dato dice de quién viene"), ("imitar", "copiar lo que hace otra persona o comunidad"), ("reservado", "lo que una comunidad prefiere no compartir con todos"), ("devolución", "mostrar el trabajo a la comunidad o al educador para que lo revisen")],
    worked=[
        W("Armar una respuesta", TAV + " Arma una respuesta atribuida de cinco partes.", ["Dato: doña Marisol cuenta que las familias limpian juntas el canal antes de sembrar y comparten una comida.", "Tipo: actividad sociocultural, con un momento espiritual reservado.", "Reflexión: yo pienso que limpiar juntas el canal cuida el agua que todas necesitan.", "Límite y pregunta: no sé cómo es el momento reservado; preguntaré al educador tradicional."], "Respuesta con dato atribuido, tipo de actividad, «yo pienso que», límite y pregunta."),
        W("Revisar una respuesta", "Una niña escribe: «Los indígenas hacen ceremonias para controlar la lluvia». ¿Qué le falta a la respuesta?", ["No dice de qué fuente viene el dato.", "Generaliza y afirma algo que nadie contó.", "No tiene límite ni pregunta."], "Le falta atribuir, no inventar y agregar límite y pregunta."),
    ],
    mistakes=[
        M("Describir lo que la comunidad reserva para que la respuesta suene completa.", "Se inventa y se falta el respeto.", "Escribe solo lo que la fuente contó y marca el límite."),
        M("No marcar qué parte es opinión mía.", "El lector no distingue la voz de la comunidad de la mía.", "Usa «yo pienso que…»."),
    ],
    R=[
        ex("¿Con qué frase atribuyes un dato a doña Marisol? A) «Todos saben que…» B) «Doña Marisol cuenta que…»", "B", "Nombra a la fuente."),
        ex("Tema: las actividades de la comunidad. ¿Cuántas partes tiene la respuesta atribuida de esta clase? Escribe el número.", "5", "Son dato, tipo de actividad, reflexión, límite y pregunta."),
        ex("Tema: las actividades de la comunidad. Verdadero o falso: mi reflexión es una idea mía y no del testimonio.", "Verdadero", "Por eso se marca como mía."),
    ],
    C=[
        ex("¿Qué significa valorar una actividad de una comunidad? A) reconocer lo que hace por la comunidad B) imitarla sin permiso", "A", "Valorar no es imitar."),
        ex("Verdadero o falso: valorar una actividad espiritual exige participar en ella.", "Falso", "Se puede valorar con respeto desde afuera."),
        ex("Tema: las actividades de la comunidad. ¿Para qué sirve la pregunta final? A) para terminar rápido B) para consultar al educador tradicional lo que no sé", "B", "La pregunta señala lo que se debe consultar."),
    ],
    A=[
        ex("Testimonio de don Segundo: «Los más viejos cuentan cómo eran las cosechas de antes». Completa la atribución: «Don Segundo cuenta que los más viejos…»", "Cuentan cómo eran las cosechas de antes", "Se repite el dato sin cambiarlo."),
        ex("Clasifica en FUENTE o REFLEXIÓN: a) doña Marisol cuenta que comparten una comida al final b) yo pienso que comer juntos refuerza la amistad de las familias.", "a fuente, b reflexión", "La primera es un dato atribuido; la segunda es una idea propia."),
        ex("Una reflexión dice: «Don Segundo cuenta que todos ayudan a armar la plaza; yo pienso que así todos sienten la fiesta como suya». ¿Qué parte es la reflexión?", "Yo pienso que así todos sienten la fiesta como suya", "Es la idea de quien escribe."),
    ],
    Z=[
        ex("Tema: las actividades de la comunidad. Marta escribe una respuesta sin límite. ¿Qué mejoraría? A) agregar más datos inventados B) agregar lo que no sé o no se cuenta", "B", "El límite muestra hasta dónde llega lo afirmado."),
        ex("¿Por qué conviene mostrar tu respuesta al educador tradicional? A) porque es una tarea de decoración B) porque conoce qué se puede contar de las actividades de su pueblo", "B", "Quien conoce su cultura puede corregir lo equivocado."),
    ],
    D=[
        ex("Dos reflexiones. 1) «Doña Marisol cuenta que limpian el canal juntas; yo pienso que eso cuida el agua de todos». 2) «Doña Marisol demuestra que su pueblo mantiene el equilibrio del cosmos». ¿Cuál está bien construida?", "La primera", "La segunda exagera: la fuente no habla del cosmos."),
        ex("Un compañero agrega que en Alto Verde «seguro bailan en círculo». El testimonio no lo menciona. ¿Qué debe hacer?", "Quitarlo porque no está en la fuente", "Lo que la fuente no dijo no se agrega."),
    ],
    context=[ex("Te piden un párrafo sobre la importancia de la limpieza del canal para Alto Verde. ¿Qué empieza mejor? A) «Todos los pueblos indígenas hacen…» B) «Doña Marisol cuenta que…»", "B", "Se atribuye el dato a la fuente.")],
    selfcheck=[
        ex("Nombra las cinco partes de una respuesta atribuida sobre una actividad.", "Dato de la fuente, tipo de actividad, reflexión, límite y pregunta", "Están en la explicación."),
        ex("Tema: las actividades de la comunidad. Verdadero o falso: debo marcar qué parte es mi opinión.", "Verdadero", "Así no se confunde con la fuente."),
        ex("Tema: las actividades de la comunidad. ¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador para que lo revise B) guardarlo sin mostrarlo", "A", "Es la devolución."),
    ],
    task=T("Usa este testimonio inventado de doña Marisol: «En Alto Verde, antes de cosechar, los mayores nos cuentan cómo se cuidaba la tierra. Después las familias recogemos juntas y repartimos la cosecha. Hay un momento de agradecimiento que no mostramos.» Escribe una respuesta de cinco partes sobre la importancia de esta actividad: 1) dato de doña Marisol, 2) tipo de actividad, 3) tu reflexión con «yo pienso que», 4) un límite y 5) una pregunta para el educador tradicional.",
           "1) Doña Marisol cuenta que los mayores cuentan cómo se cuidaba la tierra y que las familias recogen juntas y reparten la cosecha. 2) Es una actividad sociocultural, con un momento espiritual reservado. 3) Yo pienso que repartir la cosecha ayuda a que nadie quede sin alimento. 4) No sé cómo es el momento de agradecimiento. 5) Pregunta: ¿cómo cuida mi pueblo el equilibrio con la tierra en las cosechas?",
           ["atribuye cada dato", "valora con razones", "incluye límite y pregunta"], ["texto de cinco partes"], ["generalizar a todos los pueblos", "describir lo reservado"],
           "Pedir que señale la línea del testimonio que respalda su reflexión."),
    reinforce="Numera del 1 al 5 las partes de tu respuesta para comprobar que están todas.",
    extend="Reescribe tu respuesta con el testimonio de don Segundo y la fiesta de la cosecha de Pueblo Trigal.",
)

L(
    OA12, 5, materials=MAT,
    use="Aprenderé a contrastar sin jerarquizar tres actividades de comunidades distintas (una indígena inventada y dos de otros contextos) y a ver cómo cada una busca cuidar el equilibrio a su manera.",
    prior=["Sé armar una respuesta atribuida.", "Sé comparar dos actividades con criterios iguales."],
    explain=[
        "Contrastar es poner varias actividades una al lado de otra para ver en qué coinciden y en qué se diferencian. Sin jerarquizar quiere decir que no las ordenamos de «más importante» a «menos importante». Cada comunidad vive sus actividades de acuerdo con su historia y su territorio.",
        "Comparamos tres actividades inventadas: la limpieza del canal en Alto Verde (comunidad indígena inventada), la fiesta de cosecha de Pueblo Trigal (pueblo campesino no indígena) y una limpieza del barrio que hace un grupo de vecinos de una ciudad. Las tres reúnen personas y cuidan algo compartido. Una de ellas incluye un momento reservado.",
        "Para contrastar usamos los mismos criterios: quiénes participan, qué cuidan o agradecen y qué se reserva. Evitamos decir que las actividades de las comunidades indígenas son «antiguas» y las otras, «modernas», porque todas son vivas y actuales. Y tres testimonios no representan a todos los pueblos.",
    ],
    vocab=[("contrastar", "poner varias actividades juntas para ver en qué coinciden y en qué se diferencian"), ("jerarquizar", "ordenar de más importante a menos importante"), ("compartido", "que pertenece o beneficia a varias personas"), ("reservado", "lo que una comunidad prefiere no compartir con todos"), ("criterio", "punto de comparación igual para todas las actividades")],
    worked=[
        W("Contrastar tres actividades", "Alto Verde: las familias limpian el canal antes de sembrar. Pueblo Trigal: el pueblo hace una fiesta al terminar la cosecha. Barrio Norte (ciudad, inventado): los vecinos limpian la plaza el primer sábado del mes. Criterio: «qué cuidan o agradecen». ¿En qué coinciden?", ["Alto Verde cuida el canal.", "Pueblo Trigal agradece el año de cosecha.", "Barrio Norte cuida la plaza.", "Las tres comunidades cuidan o agradecen algo que es de todos."], "Coinciden en que cuidan o agradecen algo que es de todos."),
        W("Detectar una jerarquía", "Una niña dice: «La limpieza del barrio es más moderna, entonces es mejor que el momento de agradecimiento de Alto Verde». ¿Qué error hay?", ["Ordena las actividades por «moderno» o «antiguo».", "Nadie dijo que lo moderno sea mejor.", "Todas las actividades son actuales para quienes las viven."], "Jerarquiza por «moderno» sin un criterio ni una fuente."),
    ],
    mistakes=[
        M("Decir que las actividades de pueblos indígenas son antiguas y las demás, modernas.", "Todas las actividades son vivas y actuales para quienes las practican.", "Describe qué hacen hoy y para qué."),
        M("Pensar que contrastar significa que todas las actividades son iguales.", "Cada una tiene su propia historia y sentido.", "Compara con criterios iguales y anota semejanzas y diferencias."),
    ],
    R=[
        ex("¿Qué limpian los vecinos de Barrio Norte: el canal o la plaza?", "La plaza", "El canal es de Alto Verde."),
        ex("Contrastar, ¿es poner actividades juntas para ver coincidencias y diferencias o es elegir la mejor?", "Poner actividades juntas para ver coincidencias y diferencias", "Contrastar no es elegir la mejor."),
        ex("¿Cuándo hace la fiesta Pueblo Trigal: al terminar la cosecha o antes de sembrar?", "Al terminar la cosecha", "Así lo dice el testimonio de don Segundo."),
    ],
    C=[
        ex("Verdadero o falso: las actividades de las comunidades indígenas son solo del pasado.", "Falso", "Son vivas y actuales para quienes las practican."),
        ex("¿Por qué se usan criterios iguales para las tres actividades? A) para no tratar a una mejor que otra B) para llenar la tabla", "A", "Los criterios iguales evitan el trato desigual."),
        ex("Verdadero o falso: tres testimonios bastan para describir las actividades de todos los pueblos.", "Falso", "Tres testimonios no representan a todos."),
    ],
    A=[
        ex("Criterio: «quiénes participan». Alto Verde: las familias. Pueblo Trigal: todos los vecinos. Barrio Norte: los vecinos del barrio. ¿Qué coincidencia hay? A) en las tres participa una sola persona B) en las tres participa un grupo de personas de la misma comunidad", "B", "Las tres reúnen a un grupo."),
        ex("Clasifica en COINCIDENCIA o DIFERENCIA: a) las tres actividades cuidan o agradecen algo de todos b) solo en una hay un momento reservado.", "a coincidencia, b diferencia", "La primera es lo común; la segunda, lo distinto."),
        ex("Un joven dice: «Barrio Norte limpia la plaza, pero eso no es espiritual, así que vale menos». ¿Qué falla? A) ordena actividades sin criterio ni fuente B) usa el nombre de la plaza", "A", "Contrastar no es jerarquizar."),
    ],
    Z=[
        ex("Ana dice: «Alto Verde es una comunidad del pasado». ¿Qué evidencia de los testimonios contradice su idea?", "Que las familias hoy limpian el canal antes de sembrar", "La fuente cuenta que hoy lo hacen."),
        ex("Un compañero concluye: «Todas las comunidades del país hacen actividades parecidas». ¿Qué debería escribir? A) «en estos tres testimonios» B) «en todo el país»", "A", "Tres testimonios no representan al país."),
    ],
    D=[
        ex("Dos conclusiones. 1) «En estos tres testimonios, las comunidades se reúnen para cuidar o agradecer algo compartido». 2) «Las comunidades indígenas se reúnen más que las demás». ¿Cuál está bien formulada?", "La primera", "La segunda ordena a los grupos sin datos."),
        ex("Un grupo quiere participar en el momento reservado de Alto Verde «para conocerlo». ¿Qué debe hacer? A) respetar el límite y preguntar al educador tradicional qué se puede compartir B) ir sin avisar", "A", "Lo reservado se respeta y se consulta."),
    ],
    context=[ex("Tu curso hace un panel de «actividades que cuidan lo que es de todos». Una compañera propone excluir la limpieza del barrio porque «no es cultura». ¿Qué le dices? A) que toda comunidad tiene cultura y esa actividad también cuida algo de todos B) que tiene razón", "A", "Todas las comunidades tienen cultura; no se jerarquiza.")],
    selfcheck=[
        ex("Nombra un criterio de contraste para tres actividades.", "Por ejemplo: quiénes participan", "Debe ser un punto igual para todas."),
        ex("Verdadero o falso: puedo ordenar tres actividades de más importante a menos importante.", "Falso", "Contrastar no es jerarquizar."),
        ex("Escribe una coincidencia entre dos actividades de esta lección.", "Por ejemplo: ambas reúnen a la comunidad para cuidar algo compartido", "Las actividades comparten esa característica."),
    ],
    task=T("Contrasta estas tres actividades inventadas. Alto Verde: «Limpiamos el canal entre todas las familias y compartimos una comida; hay un momento que no contamos». Pueblo Trigal: «Hacemos una fiesta al terminar la cosecha para agradecer el año». Barrio Norte: «El primer sábado de cada mes los vecinos limpiamos la plaza y tomamos once juntos». Haz una tabla con tres criterios: «quiénes participan», «qué cuidan o agradecen» y «qué se reserva». Escribe una coincidencia, una diferencia y una frase que muestre cómo evitarías jerarquizar.",
           "Participan: las familias; los vecinos; los vecinos del barrio. Cuidan o agradecen: el agua del canal; el año de cosecha; la plaza. Se reserva: un momento privado; no dice; no dice. Coincidencia: las tres reúnen a un grupo y comparten algo. Diferencia: solo una reserva un momento. Para no jerarquizar, comparo con los mismos criterios y no digo cuál importa más.",
           ["usa los mismos criterios para las tres", "distingue coincidencia y diferencia", "muestra cómo evitar jerarquizar"], ["tabla de tres criterios", "coincidencia, diferencia y frase"], ["decir cuál actividad es mejor", "llamar antiguas a las indígenas"],
           "Pedir que muestre en la tabla la fila que respalda cada afirmación; valorar que no ordene las actividades."),
    reinforce="Marca en la tabla con un color las coincidencias y con otro las diferencias.",
    extend="Agrega una cuarta actividad inventada de otro contexto y explica qué criterio nuevo permitiría compararla con las otras tres.",
)
