"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 09 (identidad, aportes vivos de culturas indígenas) y OA 10 (relatos fundacionales, nociones de tiempo y espacio).

Criterio de autoría: las comunidades, los lugares, las personas y los relatos de práctica son INVENTADOS y se
rotulan así. Los relatos de práctica de OA 10 NO son relatos fundacionales de ningún pueblo real: sirven solo
para aprender a leer un relato (quién lo cuenta, qué explica, cómo ordena el tiempo y el espacio). Los relatos
reales sobre el origen del mundo los cuenta cada pueblo, por medio del educador o educadora tradicional.
"""
from __future__ import annotations

from student_content_lc4_a import FC4, FV4, L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA9, OA10 = "LC04 OA 09", "LC04 OA 10"

RVA = ("Relato de práctica de Valle Alto (inventado; no es de ningún pueblo real): «Al principio, donde hoy está Valle Alto no había valle. "
       "Cayó una lluvia muy larga desde el cerro Pelado y el agua abrió un camino hacia abajo. Ese camino es hoy el río. "
       "Después llegaron las primeras familias y se quedaron junto a la vertiente. Desde entonces, se siembra cuando terminan las lluvias.»")
RCC = ("Relato de práctica de Costa Clara (inventado; no es de ningún pueblo real): «Al principio, donde hoy está la caleta solo había mar y rocas. "
       "Con las mareas llegó arena y se formó la playa. Después llegaron las primeras familias en botes y se quedaron junto a las rocas. "
       "Desde entonces, se sale a pescar cuando el mar está tranquilo.»")

# ============================================================ OA 09 · Aportes vivos de culturas y visiones indígenas
L(
    OA9, 1,
    materials="Lápiz y hojas. Las tarjetas de personas están escritas aquí y son inventadas.",
    use="Aprenderé a reconocer que las culturas indígenas están vivas hoy y que la identidad de una persona se forma de varias cosas que cambian. Sirve para no creer en imágenes falsas ni en estereotipos.",
    prior=["Sé que los pueblos originarios viven hoy.", "Sé que cada comunidad es distinta y cuenta su propia historia."],
    explain=[
        "Una cultura viva es la que las personas practican, aprenden y renuevan hoy. Incluye saberes, costumbres, formas de convivir y, en muchos casos, una lengua. Las personas de pueblos originarios viven en el campo y en la ciudad, estudian, trabajan y usan tecnología, y también mantienen lo que valoran de su pueblo.",
        "La identidad es la manera en que una persona se reconoce y se presenta: quién es y a qué grupos pertenece. Se forma con varias cosas: la familia, el lugar donde se vive, la comunidad, la escuela, los amigos, los saberes y la historia. Por eso la identidad es dinámica: cambia y se enriquece a lo largo de la vida.",
        "Cada pueblo también tiene su visión de mundo, es decir, su manera de entender la vida, la naturaleza y a las personas. Esa visión la cuenta cada pueblo; nosotros no la adivinamos. Y nadie decide por otro quién es o cómo debe verse: la persona dice cómo se presenta y se la escucha con respeto.",
    ],
    vocab=[("cultura viva", "cultura que las personas practican y renuevan hoy"), ("identidad", "manera en que una persona se reconoce y se presenta"), ("dinámica", "que cambia y se renueva con el tiempo"), ("visión de mundo", "manera en que un pueblo entiende la vida y la naturaleza"), ("estereotipo", "idea simplificada y falsa sobre un grupo")],
    worked=[
        W("Leer una tarjeta", "Tarjeta inventada: «Valentina vive en una ciudad, va a la escuela y usa computador. Los fines de semana ayuda a su abuela a cuidar una huerta de su comunidad.» ¿Qué muestra que su cultura está viva y qué forma su identidad?", ["Usa computador y va a la escuela: vive hoy.", "Aprende de su abuela a cuidar la huerta.", "Familia, ciudad, escuela y comunidad forman su identidad."], "Su cultura está viva porque la practica hoy; su identidad se forma con familia, comunidad, escuela y lugar."),
        W("Desarmar un estereotipo", "Un niño dice: «Una persona indígena siempre se viste con ropa tradicional». ¿Qué responderías con la tarjeta de Valentina?", ["La tarjeta no habla de ropa.", "Valentina va a la escuela y usa computador.", "Una persona no se reconoce por su ropa."], "No es así: la identidad no se reconoce por la ropa ni por el aspecto."),
    ],
    mistakes=[
        M("Decir que una persona es o no es indígena por cómo se ve.", "Es un estereotipo; la identidad no se mide por el aspecto.", "Escucha cómo se presenta la propia persona."),
        M("Hablar de los pueblos originarios solo en pasado.", "Parece que ya no existen.", "Usa el presente: «viven», «practican»."),
    ],
    R=[
        ex("Tarjeta inventada: «Valentina vive en una ciudad». ¿Dónde vive Valentina?", "En una ciudad", "Lo dice la tarjeta."),
        ex("Valentina ayuda a su abuela a cuidar una huerta. ¿Con quién la cuida?", "Con su abuela", "La tarjeta lo dice."),
        ex("¿Una cultura viva se practica hoy o solo en el pasado?", "Hoy", "Una cultura viva se practica y renueva hoy."),
    ],
    C=[
        ex("Verdadero o falso: las personas indígenas no usan tecnología.", "Falso", "Viven hoy y usan lo que hay hoy."),
        ex("En Lengua y Cultura: ¿Qué significa que la identidad es dinámica? A) cambia y se enriquece con el tiempo B) nunca cambia", "A", "Dinámica quiere decir que cambia y se renueva."),
        ex("Verdadero o falso: se puede saber si una persona es indígena solo por su ropa.", "Falso", "La identidad no se reconoce por la ropa."),
    ],
    A=[
        ex("Tarjeta inventada de Joaquín: «Estudia en una escuela rural, juega fútbol y participa en las reuniones de su comunidad con su tío». Escribe una cosa que hace con su comunidad.", "Participa en las reuniones con su tío", "La tarjeta lo dice."),
        ex("Clasifica en SABER DE LA COMUNIDAD o USO DE TECNOLOGÍA: a) cuidar la huerta con la abuela b) usar el computador de la escuela.", "a saber de la comunidad, b tecnología", "Cuidar la huerta se aprende en la comunidad; el computador es tecnología."),
        ex("Dos tarjetas inventadas: Valentina vive en una ciudad; Joaquín vive en el campo. ¿Pueden ambos mantener saberes de su comunidad? Responde Sí o No.", "Sí", "Se puede vivir en la ciudad o en el campo y mantener saberes."),
    ],
    Z=[
        ex("Pedro dice: «Mi compañera no se parece a lo que muestran los libros, así que no puede ser indígena». ¿Qué error comete?", "Juzga por el aspecto", "La identidad no se mide por cómo se ve una persona."),
        ex("Si Valentina aprende de su abuela y también de la escuela, ¿qué muestra esto sobre su identidad? A) que se forma de varias cosas B) que depende de una sola cosa", "A", "Familia y escuela suman a su identidad."),
    ],
    D=[
        ex("Tarjeta inventada: Joaquín aprendió cosas de su tío, de sus amigos y de internet. ¿Su identidad podrá cambiar en el futuro? Responde Sí o No y piensa por qué.", "Sí", "La identidad es dinámica y sigue formándose."),
        ex("Para saber cómo vive una comunidad real hoy, ¿a quién le preguntas primero? A) a esa comunidad o a su educador tradicional B) a una imagen antigua", "A", "Ellos son la fuente confiable."),
    ],
    context=[ex("En el curso ven una imagen de una persona con ropa tradicional y alguien dice: «Así son todos los indígenas hoy». ¿Qué respondes? A) que no se reconoce a una persona por su ropa B) que tiene razón", "A", "Es un estereotipo; hay mucha diversidad.")],
    selfcheck=[
        ex("Nombra dos cosas que forman la identidad de una persona.", "Dos entre: familia, lugar, comunidad, escuela, amigos, saberes", "Están en la explicación."),
        ex("Verdadero o falso: los pueblos originarios solo existieron en el pasado.", "Falso", "Los pueblos viven hoy."),
        ex("¿Quién decide cómo se presenta una persona? A) ella misma B) quien la mira", "A", "Cada persona dice quién es."),
    ],
    task=T("Lee esta tarjeta inventada: «Sofía vive en una caleta, va a la escuela, usa el teléfono de una persona de su casa para hablar con sus primos y los domingos ayuda a su tío a arreglar redes junto a la comunidad.» Haz una lista con tres cosas que muestran que su cultura está viva hoy y tres que forman su identidad. Escribe una frase que desarme este estereotipo: «Las personas indígenas viven solo en el pasado».",
           "Cultura viva: ayuda a arreglar redes con la comunidad; comparte con sus primos y su tío; vive hoy en la caleta. Identidad: su familia, la caleta, la escuela. Frase: Sofía vive hoy, estudia y mantiene saberes de su comunidad.",
           ["usa datos de la tarjeta", "separa cultura viva e identidad", "desarma el estereotipo con una frase en presente"], ["dos listas", "frase en presente"], ["usar el aspecto o la ropa para definir a alguien", "hablar solo en pasado"],
           "Pedir que muestre en la tarjeta de dónde sale cada dato; valorar el uso del presente."),
    reinforce="Escribe tres cosas que forman tu propia identidad, sin datos personales delicados.",
    extend="Explica con tus palabras por qué no se puede reconocer a una persona por su ropa.",
)

L(
    OA9, 2,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a examinar un aporte de una comunidad: qué es, quién lo cuenta y con qué permiso. Sirve para valorar lo que las culturas indígenas entregan a otros sin quedarme con lo que no me corresponde.",
    prior=["Sé que una cultura está viva hoy.", "Sé situar una fuente con permiso y límite."],
    explain=[
        "Un aporte es algo que una comunidad entrega o comparte con otras personas: un saber, un alimento, una forma de cuidar la naturaleza, una manera de convivir. Los aportes no son cosas del pasado. Las culturas indígenas siguen aportando hoy a su localidad, a su región y al país.",
        "Para examinar un aporte, lo situamos: ¿de qué comunidad viene?, ¿quién lo cuenta?, ¿qué se comparte y qué no? No todo aporte puede usarse libremente. Algunos saberes se comparten con permiso y otros se resguardan. Nombrar la fuente es una forma de reconocer y de respetar.",
        "También conviene distinguir el aporte de una idea o de una cosa que se parece. Si una ficha dice que Valle Alto comparte semillas y enseña a sembrar, eso es un aporte de esa comunidad. No decimos que todos los pueblos hagan lo mismo. Cada aporte se atribuye a su comunidad.",
    ],
    vocab=[("aporte", "lo que una comunidad entrega o comparte con otras personas"), ("atribuir", "decir de quién es algo"), ("compartir con permiso", "dar algo a otros con autorización de quien lo guarda"), ("localidad", "lugar donde vive un grupo de personas, como un pueblo o un barrio"), ("reconocer", "decir de manera pública quién hizo o aportó algo")],
    worked=[
        W("Examinar una ficha", "Ficha inventada: «Comunidad: Valle Alto. Fuente: doña Rosa. Permiso: sí. Aporte: la comunidad comparte semillas de su huerta con la escuela y enseña cómo cuidarlas. Límite: no se cuentan los saberes que la comunidad reserva.» ¿Cuál es el aporte y qué no se cuenta?", ["Busco «Aporte»: semillas y enseñanza.", "Busco «Límite»: saberes reservados.", "Junto las dos ideas."], "Aporte: semillas y su cuidado. No se cuentan los saberes reservados."),
        W("Atribuir", "Una niña escribe: «Los pueblos indígenas comparten semillas con las escuelas». ¿Atribuyó bien?", ["La ficha habla de Valle Alto.", "No habla de todos los pueblos.", "Debe nombrar a la comunidad."], "No: debe decir «la comunidad de Valle Alto comparte semillas con la escuela»."),
    ],
    mistakes=[
        M("Atribuir el aporte de una comunidad a todos los pueblos.", "Cada comunidad aporta de una manera distinta.", "Nombra la comunidad y la fuente."),
        M("Creer que un aporte puede usarse sin pedir permiso.", "Algunos saberes se comparten con permiso y otros se resguardan.", "Pregunta a la fuente qué puedes usar."),
    ],
    R=[
        ex("Según la ficha de Valle Alto, ¿qué comparte la comunidad con la escuela?", "Semillas de su huerta", "La ficha lo dice."),
        ex("¿Quién es la fuente de la ficha de Valle Alto?", "Doña Rosa", "Aparece en «Fuente»."),
        ex("¿Qué NO se cuenta según la ficha? A) los saberes que la comunidad reserva B) que hay una huerta", "A", "Es el límite de la ficha."),
    ],
    C=[
        ex("¿Qué es un aporte? A) algo que una comunidad comparte con otras personas B) algo que se compra en una tienda", "A", "Es lo que una comunidad entrega o comparte."),
        ex("Verdadero o falso: los aportes de las culturas indígenas son solo del pasado.", "Falso", "Hoy siguen aportando."),
        ex("Verdadero o falso: atribuir es decir de quién es algo.", "Verdadero", "Es nombrar a la comunidad o persona."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «Fuente: don Luis. Permiso: sí. Aporte: la comunidad enseña en la escuela cómo se arreglan las redes. Límite: no se cuentan las historias reservadas». Escribe el aporte.", "Enseñar en la escuela cómo se arreglan las redes", "Está en la ficha."),
        ex("Une cada frase con la comunidad a la que se atribuye. 1) comparte semillas 2) enseña a arreglar redes a) Valle Alto b) Costa Clara", "1-a, 2-b", "Cada ficha nombra a su comunidad."),
        ex("Una ficha dice «Aporte: cuidar el agua» pero no dice permiso. ¿Puedes usarla en un trabajo? Responde Sí o No.", "No", "Falta el permiso."),
    ],
    Z=[
        ex("Tomás escribe: «Los pueblos indígenas arreglan redes». ¿Qué le falta a la frase?", "Nombrar la comunidad de la ficha", "El aporte pertenece a Costa Clara, no a todos."),
        ex("¿Por qué conviene nombrar la fuente de un aporte? A) porque reconoce y respeta a quien lo cuenta B) porque alarga el trabajo", "A", "Nombrar es dar crédito."),
    ],
    D=[
        ex("Dos frases: 1) «La comunidad de Valle Alto comparte semillas con la escuela» 2) «Los pueblos indígenas comparten semillas con todos». ¿Cuál atribuye bien?", "La primera", "La segunda generaliza."),
        ex("La ficha de Valle Alto dice que hay saberes reservados. ¿Qué haces si un compañero quiere contarlos? A) respetar el límite y no contarlos B) buscarlos en internet", "A", "Lo reservado no se publica."),
    ],
    context=[ex("Tu curso recibirá semillas de la huerta de Valle Alto. ¿Qué es correcto en el afiche? A) escribir «aporte de la comunidad de Valle Alto» B) no nombrar a nadie", "A", "Se atribuye el aporte a su comunidad.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un aporte.", "Algo que una comunidad entrega o comparte con otras personas", "Es la definición de la clase."),
        ex("¿Qué haces con los saberes que una comunidad reserva? A) los respeto y no los cuento B) los publico", "A", "El límite se respeta."),
        ex("Verdadero o falso: el aporte de una comunidad vale como aporte de todos los pueblos.", "Falso", "Cada comunidad aporta a su manera."),
    ],
    task=T("Lee esta ficha inventada: «Comunidad: Costa Clara. Fuente: don Luis. Permiso: sí. Aporte: la comunidad cuida la playa y enseña a los niños a no dejar basura. Límite: no se muestra el lugar donde se guardan los objetos de respeto.» Completa una tabla con tres filas: aporte, quién lo cuenta y límite. Escribe una frase que atribuya bien el aporte y otra que sea una generalización incorrecta, rotulada como incorrecta.",
           "Aporte: cuidar la playa y enseñar a no dejar basura. Quién cuenta: don Luis. Límite: no se muestra el lugar de los objetos de respeto. Correcta: La comunidad de Costa Clara enseña a cuidar la playa. Incorrecta: Todos los pueblos cuidan playas.",
           ["completa la tabla con datos de la ficha", "atribuye bien el aporte", "reconoce el límite"], ["tabla de tres filas", "dos frases rotuladas"], ["generalizar a todos los pueblos", "omitir el límite"],
           "Pedir que muestre en la ficha el aporte y el límite; valorar la frase bien atribuida."),
    reinforce="Escribe una frase que atribuya bien el aporte de Valle Alto de la ficha de esta clase.",
    extend="Explica por qué un aporte puede ser a la vez un saber y una responsabilidad de la comunidad que lo guarda.",
)

L(
    OA9, 3,
    materials="Lápiz y hojas. Los textos están escritos aquí; los de las comunidades son inventados.",
    use="Aprenderé a relacionar lo que aporta una localidad con lo que se comparte en el país. Sirve para ver que las culturas indígenas forman parte de la vida de todos, sin volverla igual para todos.",
    prior=["Sé examinar un aporte situado.", "Sé que la identidad y la cultura son dinámicas."],
    explain=[
        "Una localidad es un lugar concreto, como un pueblo, un barrio o una caleta. El país es el conjunto de todas las localidades. Lo que ocurre en una localidad puede llegar a otras por el intercambio: personas que viajan, mercados, escuelas, medios de comunicación y familias que se mudan.",
        "Los pueblos originarios han aportado a la vida del país. Por ejemplo, alimentos como la papa, el maíz y los porotos fueron cultivados desde antes de la llegada de los europeos por pueblos de América. Hoy se comen en muchas casas de Chile. También hay lugares y palabras del país que provienen de lenguas indígenas, y cada pueblo cuenta su propia historia.",
        "Cuando un aporte pasa de la localidad al país, se debe seguir nombrando a quienes lo originaron. Además, no todo lo de una comunidad se comparte: hay saberes que se resguardan. El intercambio es respetuoso cuando hay permiso, crédito y escucha.",
    ],
    vocab=[("localidad", "lugar concreto donde vive un grupo de personas"), ("país", "conjunto de todas las localidades de un territorio"), ("intercambio", "paso de ideas, productos o saberes entre personas o comunidades"), ("crédito", "reconocimiento a quien originó algo"), ("pueblo originario", "pueblo que vivía en un territorio antes de la formación del Estado actual")],
    worked=[
        W("De la localidad al país", "Ficha inventada: «La comunidad de Valle Alto vende su cosecha en la feria del pueblo vecino. Así, familias de otras localidades comen lo que ellos cultivan.» ¿Cómo llega un aporte de la localidad a otros lugares?", ["La comunidad produce en Valle Alto.", "Lleva la cosecha a la feria.", "Otras familias la consumen."], "Llega por el intercambio, en este caso la feria."),
        W("Dar crédito", "Un cartel de la feria dice solo «Verduras frescas». ¿Qué puede agregar para dar crédito?", ["Falta nombrar a quien las cultivó.", "Se puede escribir «de la comunidad de Valle Alto».", "Así se reconoce el aporte."], "Nombrar a la comunidad de Valle Alto como origen."),
    ],
    mistakes=[
        M("Pensar que lo que aporta una comunidad es igual en todo el país.", "Cada localidad aporta de manera distinta.", "Escribe la localidad y la comunidad."),
        M("Usar un saber de una comunidad sin nombrarla.", "No se reconoce a quienes lo originaron.", "Agrega el crédito."),
    ],
    R=[
        ex("Según la ficha inventada, ¿dónde vende su cosecha Valle Alto: en la feria del pueblo vecino o en otro país?", "En la feria del pueblo vecino", "La ficha lo dice."),
        ex("¿Qué alimentos fueron cultivados por pueblos de América antes de la llegada de los europeos: la papa y el maíz, o el trigo y la manzana?", "La papa y el maíz", "La papa y el maíz fueron cultivados en América desde antiguo."),
        ex("¿Qué es una localidad: un lugar concreto como un pueblo o todo un país?", "Un lugar concreto como un pueblo", "El país reúne muchas localidades."),
    ],
    C=[
        ex("Verdadero o falso: los pueblos originarios no han aportado nada al país de hoy.", "Falso", "Han aportado alimentos, saberes y mucho más."),
        ex("¿Qué es un intercambio? A) paso de ideas o productos entre personas o comunidades B) quedarse con algo sin avisar", "A", "Es compartir y recibir."),
        ex("Verdadero o falso: al compartir un saber de una comunidad, hay que nombrarla.", "Verdadero", "Es dar crédito."),
    ],
    A=[
        arith("Una feria tiene 4 puestos de la comunidad de Valle Alto (inventada) y cada puesto tiene 15 cajas de verduras. ¿Cuántas cajas hay en total?", "4*15", "Se repite 15 cajas cuatro veces."),
        ex("Clasifica en LOCALIDAD o PAÍS: a) la feria del pueblo vecino b) todos los lugares que forman Chile.", "a localidad, b país", "La feria es un lugar concreto; Chile es el conjunto."),
        ex("Un cartel dice: «Papas de la comunidad de Valle Alto». ¿Da crédito a quien las cultivó? Responde Sí o No.", "Sí", "Nombra la comunidad."),
    ],
    Z=[
        ex("Camilo dice: «Las comidas de Chile no tienen que ver con los pueblos originarios». ¿Qué ejemplo lo contradice?", "La papa, el maíz o los porotos", "Esos alimentos fueron cultivados por pueblos de América."),
        ex("Si una comunidad no quiere compartir una parte de su saber, ¿qué es lo correcto? A) respetar su decisión B) buscarla de todos modos", "A", "Lo reservado se respeta."),
    ],
    D=[
        ex("Dos carteles de una feria: 1) «Mermeladas ricas» 2) «Mermeladas de la comunidad de Costa Clara (inventada)». ¿Cuál reconoce mejor el origen?", "El segundo", "Nombra la comunidad."),
        ex("¿Por qué el intercambio respetuoso necesita permiso y crédito? A) porque reconoce a quien originó el saber B) porque hace más caro el producto", "A", "Respeta a quienes aportan."),
    ],
    context=[ex("En tu escuela harán una feria con productos de la comunidad de Valle Alto (inventada). ¿Qué agregas al afiche? A) el nombre de la comunidad B) nada", "A", "Es dar crédito al origen.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un intercambio.", "Paso de ideas, productos o saberes entre personas o comunidades", "Es la definición de la clase."),
        ex("Verdadero o falso: las culturas indígenas aportan solo a su localidad y no al país.", "Falso", "También aportan al país."),
        ex("¿Qué debes decir cuando compartes un saber de una comunidad? A) de qué comunidad viene B) nada", "A", "Es dar crédito."),
    ],
    task=T("Lee esta ficha inventada: «La comunidad de Costa Clara vende pescado seco en la feria de la ciudad cercana. Cada semana lleva 3 cajas y en cada caja caben 12 paquetes.» Calcula cuántos paquetes llevan por semana y escribe el cálculo. Después escribe un cartel breve para la feria que dé crédito a la comunidad y una frase sobre cómo esto conecta la localidad con el país.",
           "3 cajas × 12 paquetes = 36 paquetes por semana. Cartel: Pescado seco de la comunidad de Costa Clara. Conexión: lo que se produce en la caleta llega a familias de la ciudad y de otras localidades.",
           ["hace el cálculo correcto", "da crédito a la comunidad en el cartel", "conecta localidad y país"], ["cálculo escrito", "cartel", "frase de conexión"], ["omitir el crédito", "generalizar a todos los pueblos"],
           "Revisar el cálculo; pedir que explique cómo el cartel reconoce a la comunidad."),
    reinforce="Dibuja un esquema con una flecha de la localidad (Valle Alto) a la feria y al país.",
    extend="Escribe una pregunta que le harías a una persona de tu comunidad sobre un aporte de su pueblo a tu zona.",
)

L(
    OA9, 4,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a valorar la identidad de un pueblo sin apropiarme de lo suyo y sin tratar a todos los pueblos como si fueran iguales. Sirve para convivir con respeto en una sociedad diversa.",
    prior=["Sé que las identidades son dinámicas.", "Sé atribuir los aportes a su comunidad."],
    explain=[
        "Valorar es reconocer que algo importa y tratarlo con respeto. Valorar la identidad de un pueblo significa escuchar cómo se presenta, conocer sus aportes y no burlarse. Una forma de valorar es preguntar y agradecer, no imitar sin saber.",
        "Apropiarse es usar algo que pertenece a una comunidad sin permiso, sin entender su sentido o sin dar crédito, como disfrazarse con prendas que tienen un significado especial o copiar un diseño sin nombrar a quien lo creó. Homogeneizar es tratar a todos los pueblos o a todas las personas como si fueran iguales: «los indígenas hacen todos lo mismo».",
        "En lugar de apropiarnos u homogeneizar, podemos aprender con permiso, dar crédito y mirar la diversidad: cada pueblo, cada comunidad y cada persona son distintos. Esto no impide aprender; al contrario: lo hacemos con la guía del educador o educadora tradicional y de la comunidad.",
    ],
    vocab=[("valorar", "reconocer que algo importa y tratarlo con respeto"), ("apropiarse", "usar algo de una comunidad sin permiso, sin entender su sentido o sin dar crédito"), ("homogeneizar", "tratar a todos como si fueran iguales"), ("diversidad", "existencia de muchas formas distintas de ser y vivir"), ("permiso", "autorización de quien guarda un saber")],
    worked=[
        W("Reconocer una apropiación", "Un curso inventado copia un diseño que usa una comunidad y lo vende en una feria sin avisarle ni nombrarla. ¿Qué problema hay?", ["Usan un diseño ajeno.", "No pidieron permiso.", "No dieron crédito."], "Hay apropiación: sin permiso y sin crédito."),
        W("Reconocer una generalización", "Un niño dice: «Todos los pueblos originarios bailan igual». ¿Qué tipo de error es?", ["Habla de todos los pueblos.", "Los trata como si fueran iguales.", "Eso es homogeneizar."], "Homogeneizar: trata a todos los pueblos como iguales."),
    ],
    mistakes=[
        M("Usar prendas o símbolos de un pueblo como disfraz.", "Pueden tener un significado especial para la comunidad.", "Pregunta a la comunidad qué se puede mostrar y cómo."),
        M("Creer que respetar es no hablar nunca del tema.", "El respeto incluye aprender con permiso.", "Pregunta, escucha y agradece."),
    ],
    R=[
        ex("¿Qué significa homogeneizar: tratar a todos como iguales o reconocer las diferencias?", "Tratar a todos como iguales", "Homogeneizar iguala lo que es distinto."),
        ex("Si copias un diseño sin permiso ni crédito, ¿te apropias de él? Responde Sí o No.", "Sí", "Eso es apropiarse."),
        ex("¿Qué es la diversidad: muchas formas distintas de ser y vivir o una sola forma?", "Muchas formas distintas de ser y vivir", "Es la variedad entre personas y comunidades."),
    ],
    C=[
        ex("¿Qué es valorar? A) reconocer que algo importa y tratarlo con respeto B) burlarse con cariño", "A", "Valorar implica respeto."),
        ex("Verdadero o falso: apropiarse es usar algo de una comunidad sin permiso o sin dar crédito.", "Verdadero", "Es la definición de la clase."),
        ex("Verdadero o falso: todos los pueblos originarios tienen las mismas costumbres.", "Falso", "Cada pueblo es distinto."),
    ],
    A=[
        ex("Clasifica en APROPIARSE o VALORAR: a) pedir permiso a una comunidad para mostrar su trabajo y nombrarla b) copiar su diseño sin avisar.", "a valorar, b apropiarse", "Pedir permiso y dar crédito es valorar."),
        ex("Un cartel dice «Los indígenas son todos iguales». ¿Qué error tiene? A) homogeneiza B) da crédito", "A", "Trata a todos como iguales."),
        ex("Reescribe «Los indígenas hacen todos lo mismo» para que reconozca la diversidad. Escribe una versión posible.", "Cada pueblo y cada comunidad tiene sus propias costumbres", "Reconoce las diferencias."),
    ],
    Z=[
        ex("Lucía quiere usar una prenda con significado especial para una comunidad en un acto escolar. ¿Qué debe hacer antes? A) preguntar a la comunidad o al educador tradicional B) usarla para verse bien", "A", "El significado y el uso lo dice la comunidad."),
        ex("Un trabajo dice «Los pueblos originarios son todos del pasado». ¿Cuáles son los dos problemas? Escribe uno.", "Habla de todos como iguales o los pone solo en el pasado", "Homogeneiza y niega que viven hoy."),
    ],
    D=[
        ex("Dos formas de presentar un baile en la escuela: 1) imitarlo sin saber qué significa 2) invitar a una persona de la comunidad que lo enseñe y presentarlo con su permiso. ¿Cuál valora la identidad del pueblo?", "La segunda", "Cuenta con permiso y guía."),
        ex("¿Por qué reconocer la diversidad ayuda a no homogeneizar? A) porque muestra que cada pueblo es distinto B) porque hay que comparar", "A", "Evita tratar a todos como iguales."),
    ],
    context=[ex("Tu curso hará un afiche sobre pueblos originarios. Alguien propone dibujar a todos con la misma ropa. ¿Qué dices? A) que cada pueblo es distinto y conviene preguntar B) que está bien", "A", "Así se evita homogeneizar.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es apropiarse.", "Usar algo de una comunidad sin permiso, sin entender su sentido o sin crédito", "Es la definición de la clase."),
        ex("Verdadero o falso: se puede valorar una cultura preguntando, escuchando y agradeciendo.", "Verdadero", "Es una forma de respeto."),
        ex("¿Qué haces antes de usar un símbolo de una comunidad? A) pregunto y pido permiso B) lo copio", "A", "Respeta a la comunidad."),
    ],
    task=T("Lee estos tres casos inventados. Caso 1: un curso vende un diseño de una comunidad sin avisarle. Caso 2: un cartel dice «los pueblos indígenas son todos iguales». Caso 3: un curso invita a una persona de la comunidad de Valle Alto a contar un aporte y la nombra en el afiche. Clasifica cada caso en apropiación, homogeneización o valoración y explica en una frase. Después escribe una regla de tres pasos para tu curso que ayude a valorar sin apropiarse.",
           "Caso 1: apropiación, no hay permiso ni crédito. Caso 2: homogeneización, iguala a todos. Caso 3: valoración, hay invitación y crédito. Regla: 1) preguntar a la comunidad, 2) pedir permiso, 3) dar crédito.",
           ["clasifica bien los tres casos", "explica cada clasificación", "propone una regla de tres pasos"], ["tres clasificaciones", "tres pasos"], ["confundir homogeneización con apropiación", "regla sin permiso ni crédito"],
           "Pedir que justifique cada clasificación; valorar la regla con permiso y crédito."),
    reinforce="Escribe una frase que reconozca la diversidad de los pueblos originarios.",
    extend="Piensa en una forma de aprender sobre un pueblo con guía del educador tradicional y escríbela en dos líneas.",
)

# ============================================================ OA 10 · Nociones indígenas de tiempo y espacio (relatos fundacionales)
L(
    OA10, 1,
    materials="Lápiz y hojas. El relato de práctica está escrito aquí y es inventado.",
    use="Aprenderé a situar un relato fundacional: de qué comunidad es, quién lo cuenta y qué explica. Sirve para escuchar relatos sobre el origen con respeto y sin mezclarlos.",
    prior=["Sé situar una fuente con permiso y límite.", "Sé que cada comunidad cuenta su propia historia."],
    explain=[
        "Un relato fundacional es un relato que una comunidad cuenta para explicar cómo comenzó algo importante: el mundo, un lugar, el pueblo o su manera de vivir. No se lee solo para entretenerse. Para quienes lo cuentan, da sentido a su vida y a su territorio.",
        "Los relatos fundacionales de los pueblos originarios los cuenta cada pueblo, con sus palabras y en su momento. En esta clase usamos un relato inventado solo para practicar cómo se lee uno. El relato de práctica no pertenece a ningún pueblo real y no reemplaza a los relatos que cuentan las comunidades.",
        "Para situar un relato preguntamos: ¿de qué comunidad es?, ¿quién lo cuenta?, ¿tiene permiso para compartirse?, ¿qué explica? y ¿qué parte no se cuenta? No se dice que un relato es falso ni se corrige con ciencia: se escucha como la explicación de esa comunidad. Tampoco se mezcla con relatos de otros pueblos.",
    ],
    vocab=[("relato fundacional", "relato que explica cómo comenzó algo importante para una comunidad"), ("origen", "comienzo de algo"), ("situar", "decir de qué comunidad es y quién lo cuenta"), ("explicar", "dar sentido a algo"), ("resguardo", "cuidado para que algo no se use sin permiso")],
    worked=[
        W("Situar el relato", "Relato de práctica inventado: «" + RVA + "» ¿De qué comunidad es y qué explica?", ["La comunidad es Valle Alto, un ejemplo inventado.", "Explica cómo se formó el río y cómo llegaron las familias a vivir junto a la vertiente.", "También menciona cuándo se siembra."], "Es de Valle Alto (inventada); explica el origen del río y de la comunidad."),
        W("No corregir", "Un niño dice: «Eso es falso, los ríos se forman de otra manera». ¿Qué se responde?", ["El relato es una explicación de una comunidad.", "No se corrige desde la sala.", "Se escucha y se pregunta al educador tradicional si se quiere saber más."], "Se escucha con respeto, sin corregir, y se consulta al educador tradicional."),
    ],
    mistakes=[
        M("Decir que un relato fundacional es solo un cuento para niños.", "Para la comunidad tiene un sentido profundo.", "Escúchalo como explicación de esa comunidad."),
        M("Mezclar el relato de una comunidad con el de otra.", "Cada comunidad cuenta el suyo.", "Nombra siempre quién lo cuenta."),
    ],
    R=[
        ex("Según el relato de práctica, ¿qué abrió el camino que hoy es el río: una lluvia larga o un incendio?", "Una lluvia larga", "El relato lo dice."),
        ex("¿Desde qué cerro bajó el agua en el relato de práctica?", "Desde el cerro Pelado", "Lo dice el relato."),
        ex("¿De qué comunidad es el relato de práctica: de Valle Alto o de Costa Clara?", "De Valle Alto", "Así lo rotula el relato."),
    ],
    C=[
        ex("¿Qué es un relato fundacional? A) relato que explica cómo comenzó algo importante para una comunidad B) una receta de cocina", "A", "Explica comienzos importantes."),
        ex("Verdadero o falso: el relato de práctica de esta clase es un relato real de un pueblo originario.", "Falso", "Es un ejemplo inventado."),
        ex("Verdadero o falso: se puede decir que el relato de una comunidad es falso porque no coincide con la ciencia.", "Falso", "Se escucha con respeto; no se corrige desde la sala."),
    ],
    A=[
        ex("Escribe dos preguntas que haces para situar un relato.", "Por ejemplo: ¿quién lo cuenta? y ¿tiene permiso?", "Son parte de situar."),
        ex("Une cada dato con lo que explica el relato de práctica. 1) cómo se formó el río 2) cómo llegaron las familias a vivir junto a la vertiente a) una lluvia larga desde el cerro b) llegaron las primeras familias y se quedaron", "1-a, 2-b", "Son las dos explicaciones del relato."),
        ex("Una ficha trae el relato y quién lo cuenta, pero dice «no se cuenta lo que ocurre en el cerro». ¿Qué haces con esa parte? A) respeto y no la invento B) la imagino", "A", "Lo reservado se respeta."),
    ],
    Z=[
        ex("Pedro dice: «Como el relato habla de lluvia, todos los pueblos explican su origen con lluvia». ¿Qué error comete?", "Generaliza un relato a todos los pueblos", "Cada pueblo cuenta el suyo."),
        ex("Si quieres conocer el relato fundacional de un pueblo real, ¿a quién se lo pides? A) al educador tradicional o a la comunidad B) a un video al azar", "A", "Ellos lo cuentan con permiso."),
    ],
    D=[
        ex("Un cartel dice: «El relato de Valle Alto prueba que los pueblos creían cosas falsas». ¿Qué problema tiene? Escribe uno.", "Lo llama falso y generaliza a todos los pueblos", "Falta respeto y precisión."),
        ex("En el relato de práctica, ¿qué parte explica un origen del lugar? A) «no había valle; una lluvia abrió un camino» B) «se siembra cuando terminan las lluvias»", "A", "La B habla de una costumbre posterior."),
    ],
    context=[ex("En clase leen el relato de práctica de Valle Alto y una compañera pregunta: «¿Así lo cuentan todos los pueblos?». ¿Qué respondes? A) no, es un ejemplo inventado de una comunidad B) sí", "A", "Es un ejemplo inventado.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un relato fundacional.", "Relato que explica cómo comenzó algo importante para una comunidad", "Es la definición de la clase."),
        ex("¿Se puede corregir un relato de una comunidad desde la sala? A) no, se escucha con respeto B) sí", "A", "Se respeta como explicación de esa comunidad."),
        ex("Verdadero o falso: el relato de práctica reemplaza los relatos reales de los pueblos.", "Falso", "Solo sirve para practicar."),
    ],
    task=T("Lee este relato de práctica inventado: «" + RCC + "» Completa una ficha con cinco partes: comunidad, quién lo cuenta (en este caso, es inventado y no hay persona), qué explica, qué no sabemos del relato (por ejemplo, qué historias reserva la comunidad real de tu zona) y una pregunta para el educador tradicional sobre los relatos de tu zona. No corrijas ni compares con la ciencia.",
           "Comunidad: Costa Clara (inventada). Quién cuenta: relato inventado, no hay persona. Explica: cómo se formó la playa y cómo llegaron las primeras familias a quedarse junto a las rocas. Límite: no sabemos qué historias reserva cada comunidad. Pregunta: ¿qué relatos de nuestra zona se pueden compartir con el curso?",
           ["completa las cinco partes", "no corrige ni mezcla relatos", "formula una pregunta respetuosa"], ["ficha de cinco partes"], ["decir que el relato es falso", "mezclar con otro relato"],
           "Pedir que muestre dónde dice el relato lo que explica; valorar el respeto de la pregunta."),
    reinforce="Subraya en el relato de Costa Clara qué explica con un color y quién llegó después con otro.",
    extend="Explica con tus palabras por qué el relato de práctica no reemplaza al de una comunidad real.",
)

L(
    OA10, 2,
    materials="Lápiz y hojas. Los relatos de práctica están escritos aquí y son inventados.",
    use="Aprenderé a reconocer cómo un relato ordena el tiempo: antes, después, desde entonces y ciclos. Sirve para entender nociones de tiempo sin imponer la mía.",
    prior=["Sé situar un relato fundacional.", "Sé que cada comunidad puede ordenar el tiempo a su manera."],
    explain=[
        "El tiempo es la manera en que ordenamos cuándo ocurren las cosas. En la escuela usamos días, meses y años. Un relato también ordena el tiempo, por ejemplo con palabras como «al principio», «después» y «desde entonces». Así se entiende qué pasó primero y qué consecuencias tuvo.",
        "Algunos tiempos se repiten, como las lluvias o las siembras. Se llaman ciclos. Un relato puede unir un hecho del origen con un ciclo que se repite hasta hoy, como «desde entonces, se siembra cuando terminan las lluvias». Así el pasado y el presente quedan conectados.",
        "Cada pueblo tiene su manera de entender el tiempo y la cuenta con sus palabras. Aquí practicamos con relatos inventados. No decimos que una manera de ordenar el tiempo sea mejor que otra: comparamos para comprender. Para conocer la noción de tiempo de un pueblo real, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("tiempo", "manera de ordenar cuándo pasan las cosas"), ("ciclo", "algo que se repite en el tiempo"), ("al principio", "en el comienzo de un relato"), ("desde entonces", "a partir de ese hecho hasta hoy"), ("consecuencia", "lo que ocurre a causa de otro hecho")],
    worked=[
        W("Ordenar con marcas de tiempo", "Con el relato de Valle Alto: «Al principio no había valle… Después llegaron las primeras familias… Desde entonces, se siembra cuando terminan las lluvias.» Ordena los hechos.", ["Primero: no había valle y la lluvia abrió el camino del río.", "Después: llegaron las primeras familias.", "Desde entonces: se siembra cuando terminan las lluvias."], "Lluvia y río, llegada de familias y siembra al terminar las lluvias."),
        W("Encontrar el ciclo", "En el mismo relato, ¿qué ciclo aparece?", ["Busco algo que se repite.", "«Se siembra cuando terminan las lluvias».", "Se repite cada vez que terminan las lluvias."], "La siembra al terminar las lluvias."),
    ],
    mistakes=[
        M("Pensar que el tiempo solo se cuenta en años.", "Un relato puede ordenar el tiempo con ciclos y marcas como «desde entonces».", "Busca esas marcas en el relato."),
        M("Decir que una forma de ordenar el tiempo es mejor que otra.", "Cada comunidad ordena el tiempo a su manera.", "Compara sin jerarquizar."),
    ],
    R=[
        ex("En el relato de Valle Alto, ¿qué ocurrió primero: cayó la lluvia o llegaron las familias?", "Cayó la lluvia", "El relato lo ordena así."),
        ex("¿Qué palabra marca el comienzo del relato de Costa Clara: «al principio» o «mañana»?", "Al principio", "Así empieza el relato."),
        ex("¿Qué es un ciclo: algo que se repite o algo que ocurre una sola vez?", "Algo que se repite", "Es la definición."),
    ],
    C=[
        ex("Verdadero o falso: «desde entonces» une un hecho del origen con lo que ocurre hoy.", "Verdadero", "Conecta pasado y presente."),
        ex("¿Qué ciclo aparece en el relato de Costa Clara? A) salir a pescar cuando el mar está tranquilo B) caer una lluvia larga", "A", "Es lo que se repite desde entonces."),
        ex("Verdadero o falso: todos los pueblos ordenan el tiempo igual que la escuela.", "Falso", "Cada pueblo tiene su manera."),
    ],
    A=[
        ex("Ordena según el relato de Costa Clara: a) llegaron las primeras familias en botes b) solo había mar y rocas c) se formó la playa con la arena. Escribe las letras.", "b, c, a", "Primero mar y rocas, luego la playa y después las familias."),
        ex("Completa con el relato de Valle Alto: «Desde entonces, se siembra cuando terminan las ___». Escribe la palabra.", "lluvias", "El relato lo dice."),
        ex("Clasifica en HECHO DEL ORIGEN o CICLO: a) las mareas trajeron arena b) se sale a pescar cuando el mar está tranquilo.", "a hecho del origen, b ciclo", "El primero ocurrió al principio; el segundo se repite."),
    ],
    Z=[
        ex("Ana dice: «El relato de Valle Alto no tiene tiempo porque no tiene fechas». ¿Qué responde el relato?", "Ordena el tiempo con palabras como al principio, después y desde entonces", "Hay otras formas de ordenar el tiempo."),
        ex("¿Por qué «desde entonces» importa para entender el presente? A) conecta el origen con una costumbre de hoy B) no tiene importancia", "A", "Une pasado y presente."),
    ],
    D=[
        ex("Un relato ordena el tiempo con «al principio… después…» y otro con el vaivén de las mareas. ¿Alguna de las dos maneras es incorrecta?", "Ninguna", "Cada comunidad ordena el tiempo a su manera."),
        ex("Si en una comunidad real el tiempo se ordena con otro ciclo, ¿a quién se pregunta? A) al educador tradicional o a la comunidad B) a nadie, se supone", "A", "Ellos conocen su noción de tiempo."),
    ],
    context=[ex("En tu sala marcan el tiempo con el horario y el calendario. Un compañero dice que eso es «el único tiempo real». ¿Qué le respondes? A) hay otras formas de ordenar el tiempo, como los ciclos del relato B) tiene razón", "A", "No se jerarquiza.")],
    selfcheck=[
        ex("Escribe dos palabras que ordenan el tiempo en un relato.", "Por ejemplo: al principio y después", "Son marcas de tiempo."),
        ex("Verdadero o falso: un ciclo es algo que se repite.", "Verdadero", "Es la definición de la clase."),
        ex("¿Qué haces para conocer la noción de tiempo de un pueblo real? A) pregunto al educador tradicional B) la invento", "A", "Es la fuente."),
    ],
    task=T("Lee los dos relatos de práctica inventados: «" + RVA + "» y «" + RCC + "». Para cada uno, escribe: 1) las marcas de tiempo que usa, 2) el orden de los hechos con números y 3) el ciclo que menciona. Termina con una frase que diga que ninguna forma de ordenar el tiempo es mejor que otra.",
           "Valle Alto: marcas: al principio, después, desde entonces. Orden: 1 lluvia y río, 2 llegan las familias, 3 siembra al terminar las lluvias. Ciclo: siembra. Costa Clara: marcas: al principio, con las mareas, después, desde entonces. Orden: 1 mar y rocas, 2 playa, 3 llegan familias, 4 pesca con mar tranquilo. Ciclo: pesca. Ninguna forma es mejor que otra.",
           ["identifica marcas de tiempo", "ordena los hechos", "identifica un ciclo en cada relato"], ["dos fichas", "frase final"], ["jerarquizar maneras de ordenar el tiempo", "mezclar los dos relatos"],
           "Pedir que muestre dónde está cada marca; valorar la frase sin jerarquía."),
    reinforce="Dibuja una línea con tres recuadros para el relato de Valle Alto: al principio, después y desde entonces.",
    extend="Explica con tus palabras cómo se conecta el pasado con el presente en el relato de Costa Clara.",
)

L(
    OA10, 3,
    materials="Lápiz y hojas. Los relatos de práctica están escritos aquí y son inventados.",
    use="Aprenderé a reconocer cómo un relato ordena el espacio: dónde están los lugares y cómo se relacionan. Sirve para entender nociones de espacio sin imponer la mía.",
    prior=["Sé reconocer marcas de tiempo en un relato.", "Sé describir la organización de un territorio con una ficha."],
    explain=[
        "El espacio es la manera en que ordenamos dónde están las cosas: cerca, lejos, arriba, abajo, junto a, desde dónde viene algo. Un relato también ordena el espacio, por ejemplo cuando dice que el agua bajó desde el cerro o que las familias se quedaron junto a la vertiente.",
        "Esas indicaciones forman una orientación: nos dicen hacia dónde mirar y cómo se conectan los lugares. En el relato de Valle Alto, el cerro está arriba, el río abajo y la vertiente cerca de las familias. En el de Costa Clara, el mar y las rocas están al comienzo y la playa se forma después.",
        "Cada pueblo tiene su manera de entender y nombrar su espacio, y la cuenta con sus palabras. Los relatos de esta clase son inventados. No decimos que una manera de orientarse sea mejor que otra. Para conocer cómo orienta su espacio un pueblo real, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("espacio", "manera de ordenar dónde están las cosas"), ("orientación", "indicación de hacia dónde están los lugares"), ("referencia", "lugar o señal que sirve para ubicarse"), ("junto a", "al lado de algo"), ("desde", "indica el punto de partida")],
    worked=[
        W("Ubicar con el relato", "Con el relato de Valle Alto: ¿dónde está el cerro y hacia dónde bajó el agua?", ["El agua cayó desde el cerro Pelado.", "Abrió un camino hacia abajo.", "Ese camino es el río."], "El cerro está arriba; el agua bajó hacia abajo formando el río."),
        W("Encontrar referencias", "Con el relato de Costa Clara: ¿qué lugares sirven de referencia para ubicar a las familias?", ["Las familias se quedaron junto a las rocas.", "Las rocas son una referencia.", "La playa también se menciona."], "Las rocas y la playa."),
    ],
    mistakes=[
        M("Pensar que el espacio solo se ordena con mapas y puntos cardinales.", "Un relato puede ordenar el espacio con referencias del territorio.", "Busca los lugares nombrados."),
        M("Decir que orientarse con un cerro o un río es menos exacto.", "Es otra forma de ordenar el espacio, no mejor ni peor.", "Compara sin jerarquizar."),
    ],
    R=[
        ex("En el relato de Valle Alto, ¿de dónde cayó la lluvia: del cerro Pelado o de la playa?", "Del cerro Pelado", "El relato lo dice."),
        ex("¿Junto a qué se quedaron las primeras familias de Valle Alto?", "Junto a la vertiente", "Es lo que dice el relato."),
        ex("¿Junto a qué se quedaron las primeras familias de Costa Clara: las rocas o el cerro?", "Las rocas", "El relato de Costa Clara lo dice."),
    ],
    C=[
        ex("¿Qué es una referencia? A) lugar o señal que sirve para ubicarse B) un tipo de relato", "A", "Ayuda a saber dónde está algo."),
        ex("Verdadero o falso: un relato puede ordenar el espacio con lugares del territorio.", "Verdadero", "Por ejemplo el cerro, el río o las rocas."),
        ex("Verdadero o falso: todos los pueblos se orientan igual que un mapa de la escuela.", "Falso", "Cada pueblo tiene su manera."),
    ],
    A=[
        ex("Ubica con el relato de Valle Alto: ¿qué está más arriba, el cerro Pelado o el río?", "El cerro Pelado", "El agua bajó desde el cerro y formó el río."),
        ex("Clasifica en LUGAR DE ORIGEN DEL AGUA o LUGAR A DONDE LLEGA: a) el cerro Pelado b) el río.", "a lugar de origen del agua, b lugar a donde llega", "El agua baja desde el cerro y forma el río."),
        ex("Del relato de Costa Clara, ¿qué palabra indica ubicación: «junto» o «después»? Escribe la palabra.", "Junto", "«Junto a las rocas» indica ubicación."),
    ],
    Z=[
        ex("Lucas dice: «El relato de Valle Alto no ordena el espacio porque no tiene mapa». ¿Qué le respondes?", "Lo ordena con referencias como el cerro, el río y la vertiente", "Usa lugares del territorio."),
        ex("¿Por qué los lugares nombrados en un relato son importantes? A) porque conectan el origen con el territorio B) porque son decorativos", "A", "Unen el relato con el lugar real."),
    ],
    D=[
        ex("Dos formas de ubicar: «junto a la vertiente» o «a 100 metros al norte». ¿Cuál es la que usa el relato de Valle Alto?", "Junto a la vertiente", "Usa una referencia del territorio."),
        ex("Si quieres saber cómo un pueblo real orienta su espacio, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a una página al azar", "A", "Ellos lo explican."),
    ],
    context=[ex("Tu curso dibuja un croquis de Valle Alto con el relato. ¿Qué debe ir arriba? A) el cerro Pelado B) la playa", "A", "El agua bajó desde el cerro.")],
    selfcheck=[
        ex("Escribe dos palabras que indiquen ubicación en un relato.", "Por ejemplo: junto a y desde", "Indican dónde están las cosas."),
        ex("Verdadero o falso: el espacio es la manera de ordenar dónde están las cosas.", "Verdadero", "Es la definición de la clase."),
        ex("¿Se puede decir que una forma de orientarse es mejor? A) no, cada pueblo tiene la suya B) sí", "A", "No se jerarquiza."),
    ],
    task=T("Lee los dos relatos de práctica inventados: «" + RVA + "» y «" + RCC + "». Haz un croquis simple de cada uno con solo los lugares nombrados (cerro, río, vertiente; mar, rocas, playa). Escribe debajo de cada croquis una lista con las referencias de ubicación que usa el relato. Termina con una frase que diga que ninguna manera de ordenar el espacio es mejor que otra.",
           "Valle Alto: cerro arriba, río abajo, vertiente donde se quedan las familias. Referencias: desde el cerro, hacia abajo, junto a la vertiente. Costa Clara: mar, rocas, playa. Referencias: donde hoy está la caleta, junto a las rocas. Ninguna forma es mejor que otra.",
           ["usa solo lugares del relato", "lista las referencias", "no jerarquiza"], ["dos croquis", "dos listas", "frase final"], ["agregar lugares que no están", "jerarquizar maneras de orientarse"],
           "Pedir que muestre dónde dice el relato cada lugar; valorar que no agregue lugares."),
    reinforce="Marca con una flecha el recorrido del agua en el croquis de Valle Alto.",
    extend="Escribe una pregunta que le harías al educador tradicional sobre cómo se ubican los lugares importantes de tu zona.",
)

L(
    OA10, 4,
    materials="Lápiz y hojas. Los relatos de práctica están escritos aquí y son inventados.",
    use="Aprenderé a comparar dos relatos reconociendo qué tienen en común y qué los diferencia, y a decir los límites de la comparación. Sirve para comprender sin jerarquizar.",
    prior=["Sé reconocer cómo un relato ordena el tiempo y el espacio.", "Sé que cada relato vale para su comunidad."],
    explain=[
        "Comparar es mirar dos cosas para ver qué tienen en común y qué las hace diferentes. Con relatos de práctica podemos comparar cómo cuentan el origen de un lugar, cómo ordenan el tiempo y cómo ordenan el espacio. Comparar ayuda a comprender, no a decidir cuál es mejor.",
        "Una buena comparación usa una tabla: filas con los temas (origen, tiempo, espacio) y columnas con cada relato. Cada casilla se llena con datos escritos en el relato. Las semejanzas son lo que se repite en ambos; las diferencias, lo que cambia. No se agregan datos que el relato no trae.",
        "Toda comparación tiene límites: solo comparamos lo que los relatos dicen. No sabemos todo sobre cada comunidad. No se mezclan los relatos ni se dice que uno es más importante. En comunidades reales, la comparación la guía el educador o educadora tradicional, que decide qué relatos se pueden compartir y cómo.",
    ],
    vocab=[("comparar", "mirar dos cosas para ver semejanzas y diferencias"), ("semejanza", "lo que dos cosas tienen en común"), ("diferencia", "lo que distingue una cosa de otra"), ("jerarquizar", "decir que algo es mejor o más importante que otra cosa"), ("límite de la comparación", "lo que no se puede afirmar con los datos que hay")],
    worked=[
        W("Completar la tabla", "Compara los relatos de Valle Alto y Costa Clara en origen, tiempo y espacio.", ["Origen: Valle Alto, lluvia que abre el río; Costa Clara, mareas que forman la playa.", "Tiempo: ambos usan «al principio, después, desde entonces».", "Espacio: Valle Alto, cerro y vertiente; Costa Clara, mar y rocas."], "Se parecen en el orden del tiempo; difieren en el origen y los lugares."),
        W("Escribir un límite", "¿Qué límite tiene decir «las dos comunidades explican igual su origen»?", ["Los orígenes son distintos.", "Solo coinciden en la estructura temporal.", "Hay que decirlo con cuidado."], "Que solo coinciden en la estructura del relato, no en lo que explican."),
    ],
    mistakes=[
        M("Decir que un relato es más antiguo o más importante que otro.", "Eso es jerarquizar y no hay base en los relatos.", "Compara sin ordenar de mejor a peor."),
        M("Agregar a la tabla datos que ningún relato trae.", "Se mezcla lo escrito con lo supuesto.", "Cada casilla se llena con datos del relato."),
    ],
    R=[
        ex("En ambos relatos, ¿qué palabra marca el comienzo: «al principio» o «mañana»?", "Al principio", "Los dos empiezan así."),
        ex("¿Qué formó la playa en el relato de Costa Clara: las mareas o la lluvia?", "Las mareas", "El relato lo dice."),
        ex("¿Qué abrió el camino del río en el relato de Valle Alto: la lluvia o las mareas?", "La lluvia", "El relato lo dice."),
    ],
    C=[
        ex("¿Qué es una semejanza? A) lo que dos cosas tienen en común B) lo que las distingue", "A", "Es lo que comparten."),
        ex("Verdadero o falso: comparar sirve para decidir cuál relato es mejor.", "Falso", "Comparar ayuda a comprender, sin jerarquizar."),
        ex("Verdadero o falso: en una tabla de comparación se pueden agregar datos que ningún relato trae.", "Falso", "Solo se usan datos de los relatos."),
    ],
    A=[
        ex("Escribe una semejanza entre el relato de Valle Alto y el de Costa Clara.", "Ambos relatos usan al principio, después y desde entonces", "Es lo que se repite en los dos."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en uno el origen es una lluvia y en otro las mareas b) ambos cuentan que llegaron familias y se quedaron.", "a diferencia, b semejanza", "El origen cambia; la llegada de familias se repite."),
        ex("Completa: en Valle Alto las familias se quedaron junto a la ___; en Costa Clara, junto a las ___. Escribe las dos palabras.", "vertiente y rocas", "Cada relato nombra un lugar distinto."),
    ],
    Z=[
        ex("Camila dice: «El relato de Costa Clara es mejor porque habla del mar». ¿Qué error comete?", "Jerarquiza sin base", "Comparar no es ordenar de mejor a peor."),
        ex("¿Qué límite tiene comparar solo dos relatos de práctica? A) no se puede decir cómo son todos los relatos B) se puede decir cómo son todos", "A", "Solo hay datos de dos relatos."),
    ],
    D=[
        ex("Dos conclusiones: 1) «En ambos relatos el tiempo se ordena con las mismas palabras» 2) «Todos los pueblos ordenan el tiempo así». ¿Cuál es válida con los dos relatos?", "La primera", "La segunda generaliza sin datos."),
        ex("Si un relato real de una comunidad tiene partes reservadas, ¿qué haces en la comparación? A) respeto el límite y no las incluyo B) las busco", "A", "Lo reservado no se incluye."),
    ],
    context=[ex("Tu curso compara los relatos y alguien propone votar cuál es mejor. ¿Qué dices? A) que no se vota: se comparan sin jerarquizar B) que sí", "A", "Cada relato vale para su comunidad.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es jerarquizar.", "Decir que algo es mejor o más importante que otra cosa", "Es lo que no se hace al comparar."),
        ex("Verdadero o falso: una buena comparación declara sus límites.", "Verdadero", "Reconoce hasta dónde llegan los datos."),
        ex("¿Qué usas para llenar la tabla de comparación? A) solo datos de los relatos B) lo que me parezca", "A", "Cada casilla debe tener fuente."),
    ],
    task=T("Compara los relatos de práctica inventados: «" + RVA + "» y «" + RCC + "». Haz una tabla de tres filas (origen, tiempo, espacio) y dos columnas (Valle Alto, Costa Clara) con datos de los relatos. Escribe dos semejanzas, dos diferencias y un límite de tu comparación. No digas cuál relato es mejor.",
           "Origen: lluvia que abre el río / mareas que forman la playa. Tiempo: al principio, después, desde entonces en ambos. Espacio: cerro y vertiente / mar y rocas. Semejanzas: usan las mismas marcas de tiempo; llegan primeras familias. Diferencias: distinto origen; distintos lugares. Límite: solo comparo dos relatos inventados.",
           ["llena la tabla con datos de los relatos", "escribe semejanzas, diferencias y un límite", "no jerarquiza"], ["tabla", "lista de semejanzas y diferencias", "límite"], ["agregar datos que no están", "decir cuál es mejor"],
           "Pedir que muestre dónde está cada dato; valorar el límite escrito."),
    reinforce="Rodea las semejanzas con un color y las diferencias con otro en tu tabla.",
    extend="Escribe cómo cambiarías la comparación si tuvieras permiso para conocer un relato real de una comunidad de tu zona, y qué le preguntarías al educador tradicional.",
)
