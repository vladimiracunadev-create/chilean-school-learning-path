"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 12 (eventos socioculturales y ceremoniales) y OA 13 (valores comunitarios y espirituales).

Los eventos, comunidades y personas son INVENTADOS y se rotulan así. No se describe ningún rito, ceremonia ni
fecha de un pueblo real: lo ceremonial real lo enseña la comunidad o el educador/a tradicional y, muchas veces,
no se cuenta. Único dato cultural general: algunas palabras del español que vienen del quechua (papa, palta,
cóndor), anotadas para revisión de especialista.
"""
from __future__ import annotations

from student_content_lc5_a import L, M, MAT, T, W
from student_lessons import arith, ex

OA12, OA13 = "LC05 OA 12", "LC05 OA 13"

ECO = ("Testimonio inventado de doña Elena, de Ladera Verde: «El Encuentro de la Cosecha lo organizan las familias cuando termina la cosecha. Nos juntamos en la explanada, "
       "cada familia trae lo que cosechó y lo compartimos. Hay juegos para los niños y todos conversamos. Cualquier persona de la comunidad puede venir.»")
EAG = ("Testimonio inventado de doña Elena, de Ladera Verde: «La Mañana del Agua la hacemos junto a la quebrada, al amanecer. Se avisa a todos, se llega en silencio y quien quiera acompañar "
       "pide permiso antes. Lo que se dice en esa mañana no se cuenta fuera de la comunidad.»")
EIN = ("Testimonio inventado de don Camilo, de Isla Niebla: «La Fiesta de la Caleta la hacemos cuando vuelven los botes. Hay comida compartida, música tocada por quienes quieren y juegos en la playa. "
       "Se invita a los vecinos de la isla.»")
ECL = ("Evento inventado de Costa Lejana (cultura inventada): «La Noche de las Linternas: las familias hacen linternas de papel y las cuelgan frente a su casa. Los vecinos pasean para verlas. "
       "Al final se comparte pan.»")

# ============================================================ OA 12 · Eventos socioculturales y ceremoniales
L(
    OA12, 1, materials=MAT,
    use="Aprenderé a situar un evento de una comunidad y a distinguir si es sociocultural, ceremonial o ambas cosas. Sirve para estudiar celebraciones y ceremonias de distintos pueblos sin confundirlas ni inventar nada.",
    prior=["Sé situar una fuente con su ficha.", "Sé que lo ceremonial lo enseña la comunidad."],
    explain=[
        "Un evento sociocultural es una reunión en que una comunidad se junta para compartir: celebrar, conversar, jugar, intercambiar o trabajar. Un evento ceremonial es uno que tiene un sentido espiritual o sagrado para esa comunidad y que suele tener normas especiales de respeto. Algunos eventos tienen una parte social y otra ceremonial. Una pista para distinguirlos es que tengan normas especiales de respeto y partes que se guardan; pero solo la comunidad dice si su evento es ceremonial.",
        "Para situar un evento preguntamos: ¿cómo se llama?, ¿qué comunidad lo hace?, ¿quién lo cuenta?, ¿quién puede participar?, ¿qué normas hay? y ¿qué no se cuenta? Un evento sociocultural suele contarse con más detalle. Un evento ceremonial se cuenta con cuidado y muchas veces la comunidad guarda sus partes para sí.",
        "En este cuaderno los eventos son inventados. Lo que hace cada pueblo real, cuándo lo hace y cómo, lo explican su comunidad o su educador o educadora tradicional. Nosotros no adivinamos ceremonias, no las describimos si no las cuentan y no las imitamos como juego.",
    ],
    vocab=[("evento sociocultural", "reunión en que la comunidad se junta a compartir, celebrar o trabajar"), ("evento ceremonial", "reunión con sentido espiritual o sagrado y normas especiales"), ("participante", "persona que toma parte en un evento"), ("norma de respeto", "regla para comportarse en un evento"), ("resguardo", "cuidado de lo que no se cuenta")],
    worked=[
        W("Clasificar un evento", ECO + " ¿Es sociocultural o ceremonial?", ["Se juntan, comparten lo cosechado, juegan y conversan.", "El testimonio no habla de normas espirituales.", "Es un evento sociocultural."], "Es un evento sociocultural."),
        W("Reconocer un resguardo", EAG + " ¿Qué parte se resguarda?", ["Busco qué no se cuenta.", "Lo que se dice en esa mañana no se cuenta fuera.", "Esa parte se respeta."], "Lo que se dice en la Mañana del Agua no se cuenta fuera de la comunidad."),
    ],
    mistakes=[
        M("Describir una ceremonia que no se contó.", "Es adivinar y puede ser falso o irrespetuoso.", "Escribe solo lo que dice la fuente."),
        M("Imitar una ceremonia como juego.", "Puede faltar al respeto a lo sagrado.", "Aprende sobre ella con la comunidad."),
    ],
    R=[
        ex("Testimonio inventado: «El Encuentro de la Cosecha lo organizan las familias cuando termina la cosecha». ¿Cuándo se hace?", "Cuando termina la cosecha", "El testimonio lo dice."),
        ex("Testimonio inventado: «La Mañana del Agua la hacemos junto a la quebrada, al amanecer». ¿Dónde se hace? A) junto a la quebrada B) en la explanada", "A", "El testimonio lo dice."),
        ex("En la Fiesta de la Caleta (inventada) hay comida compartida y juegos en la playa. ¿Es una reunión para compartir? Responde Sí o No.", "Sí", "Se junta la comunidad a compartir."),
    ],
    C=[
        ex("Verdadero o falso: un evento sociocultural es una reunión en que la comunidad se junta a compartir.", "Verdadero", "Es la definición de la clase."),
        ex("¿Qué es un evento ceremonial? A) uno con sentido espiritual y normas especiales B) cualquier reunión", "A", "Se diferencia por su sentido espiritual."),
        ex("Verdadero o falso: puedo imitar una ceremonia como juego en el patio.", "Falso", "Puede faltar al respeto a lo sagrado."),
    ],
    A=[
        ex("Clasifica en SOCIOCULTURAL o CEREMONIAL, según la pista de la clase y los testimonios inventados: a) «Hay juegos para los niños y todos conversamos» b) «Quien quiera acompañar pide permiso antes y llega en silencio».", "a sociocultural, b ceremonial", "La primera comparte; la segunda tiene normas de respeto."),
        ex("Testimonio inventado de don Camilo: «Se invita a los vecinos de la isla». ¿Quién puede participar en la Fiesta de la Caleta?", "Los vecinos de la isla", "El testimonio lo dice."),
        ex("Una ficha de evento no dice si la comunidad autorizó contarlo. ¿Puedes usarla en tu trabajo? Responde Sí o No.", "No", "Sin permiso no se comparte."),
    ],
    Z=[
        ex("Camila dice: «La Mañana del Agua seguro es una ceremonia con música». El testimonio no habla de música. ¿Qué error comete?", "Adivina algo que la fuente no dice", "No se rellena lo no contado."),
        ex("Un compañero propone jugar a la «ceremonia del agua» en el recreo. ¿Qué le dices? A) que no se imita lo sagrado de una comunidad B) que sí, pero con cuidado", "A", "No se imita como juego."),
    ],
    D=[
        ex("Un evento inventado reúne a la comunidad para compartir comida y también tiene una parte reservada. ¿Cómo lo clasificas? A) tiene parte sociocultural y parte ceremonial B) solo sociocultural", "A", "Puede tener ambas partes."),
        ex("Quieres contar la Mañana del Agua en un cartel. ¿Qué escribes de lo que se dice esa mañana? A) que no se cuenta B) lo que imagino", "A", "El testimonio dice que no se cuenta fuera."),
    ],
    context=[ex("Un periodista escolar quiere fotografiar la Mañana del Agua para el diario mural. ¿Qué haces? A) pedir permiso a la comunidad antes B) sacarla a escondidas", "A", "La imagen de un evento ceremonial requiere permiso.")],
    selfcheck=[
        ex("Nombra dos preguntas para situar un evento.", "Dos entre: cómo se llama, qué comunidad, quién lo cuenta, quién participa, qué normas hay", "Están en la explicación."),
        ex("Verdadero o falso: un evento puede tener una parte sociocultural y otra ceremonial.", "Verdadero", "Algunos eventos las mezclan."),
        ex("¿Quién explica lo ceremonial de un pueblo real? A) su comunidad o el educador tradicional B) cualquiera", "A", "Ellos son la fuente."),
    ],
    task=T("Lee este evento inventado de Pampa Larga, contado por doña Marta: «El Día del Pozo lo hacemos cuando se limpia el pozo. Las familias traen agua en baldes, se limpia entre todos y después compartimos la comida. Se invita a todas las personas de la comunidad. Hay una parte que solo hacen las personas mayores y no se cuenta.» Haz una ficha con: nombre, comunidad, fuente, quién participa, qué es sociocultural, qué se resguarda y qué norma respetarías.",
           "Nombre: Día del Pozo. Comunidad: Pampa Larga. Fuente: doña Marta. Participan todas las personas de la comunidad. Sociocultural: limpiar el pozo entre todos y compartir la comida. Se resguarda: la parte que hacen las personas mayores. Norma: no preguntar ni imaginar esa parte.",
           ["completa la ficha con datos del texto", "separa lo social de lo resguardado", "indica una norma"], ["ficha completa"], ["describir la parte resguardada", "agregar datos que no están"],
           "Pedir que muestre la frase del texto de cada dato."),
    reinforce="Pinta de verde lo sociocultural y de azul lo resguardado en el testimonio de doña Marta.",
    extend="Escribe una pregunta que le harías al educador tradicional sobre los eventos de tu zona.",
)

L(
    OA12, 2, materials=MAT,
    use="Aprenderé a leer la descripción de un evento con límites declarados: qué dice la fuente, qué no se cuenta y qué normas debo respetar si fuera invitado. Sirve para analizar eventos sin faltar al respeto.",
    prior=["Sé distinguir un evento sociocultural de uno ceremonial.", "Sé separar lo que dice la fuente de lo que interpreto."],
    explain=[
        "Al leer la descripción de un evento hacemos cuatro preguntas. ¿Qué pasa? ¿Quiénes participan y qué hace cada uno? ¿Qué normas hay? ¿Qué no se cuenta? Las respuestas se escriben con las palabras de la fuente. Así describimos el evento sin agregar nada.",
        "Las normas de respeto nos dicen cómo comportarnos si somos invitados. Pueden ser: llegar a tiempo, ir en silencio, pedir permiso para acompañar, no grabar ni fotografiar sin autorización y no tocar objetos que no son nuestros. Cada comunidad tiene las suyas, y las informa su fuente.",
        "Cuando algo no se cuenta, lo escribimos como límite: «la comunidad no cuenta esta parte». No la reemplazamos con ideas nuestras. Si queremos aprender más, preguntamos al educador o educadora tradicional con respeto y aceptamos que a veces la respuesta sea «eso no se cuenta».",
    ],
    vocab=[("rol", "tarea que cumple una persona en un evento"), ("norma de respeto", "regla para comportarse como invitado"), ("invitado", "persona que participa porque la comunidad la recibe"), ("límite", "lo que no se cuenta"), ("autorización", "permiso para grabar, fotografiar o compartir")],
    worked=[
        W("Aplicar las cuatro preguntas", EAG + " Responde: ¿qué pasa?, ¿qué normas hay?, ¿qué no se cuenta?", ["Pasa: se hace una mañana junto a la quebrada, al amanecer.", "Normas: llegar en silencio y pedir permiso para acompañar.", "No se cuenta lo que se dice esa mañana."], "Pasa una mañana junto a la quebrada; normas: llegar en silencio y pedir permiso; no se cuenta lo que se dice."),
        W("Reconocer un límite", "Un niño escribe: «En la Mañana del Agua dicen palabras para el agua». ¿Está bien?", ["El testimonio dice que lo que se dice no se cuenta.", "El niño cuenta lo que se dice.", "Debe quitar o aclarar que no se cuenta."], "No: esa parte no se cuenta y no puede inventarse."),
    ],
    mistakes=[
        M("Escribir lo que «seguramente» pasa en la parte que no se cuenta.", "Es inventar una ceremonia.", "Escribe «la comunidad no cuenta esta parte»."),
        M("Grabar o fotografiar un evento sin permiso.", "Puede violar una norma de la comunidad.", "Pide autorización a la comunidad."),
    ],
    R=[
        ex("Testimonio inventado: «Se avisa a todos, se llega en silencio». ¿Cómo se llega al evento?", "En silencio", "El testimonio lo dice."),
        ex("Testimonio inventado: «Quien quiera acompañar pide permiso antes». ¿Qué se hace antes de acompañar? A) pedir permiso B) llegar tarde", "A", "El testimonio lo dice."),
        ex("Si la comunidad no cuenta una parte del evento, ¿se puede inventar? Responde Sí o No.", "No", "Lo no contado se respeta."),
    ],
    C=[
        ex("Verdadero o falso: las normas de respeto las informa la comunidad.", "Verdadero", "Cada comunidad tiene las suyas."),
        ex("¿Qué es un invitado? A) una persona que participa porque la comunidad la recibe B) una persona que entra sin avisar", "A", "Se participa con permiso."),
        ex("Verdadero o falso: puedo grabar un evento si no molesto a nadie.", "Falso", "Hace falta autorización."),
    ],
    A=[
        ex("Don Camilo (inventado) cuenta: «La música la tocan quienes quieren». ¿Quiénes tocan la música?", "Quienes quieren", "El testimonio lo dice."),
        ex("Clasifica en NORMA o ROL: a) llegar en silencio b) organizar los juegos para los niños.", "a norma, b rol", "La primera es una regla; la segunda es una tarea."),
        ex("Una descripción dice: «Hay una parte que solo hacen las personas mayores y no se cuenta». ¿Cuál es el límite? A) la parte de las personas mayores B) el nombre de la comunidad", "A", "Es la parte que no se cuenta."),
    ],
    Z=[
        ex("Mateo escribe: «En la parte que solo hacen las personas mayores, cantan». El texto no lo dice. ¿Qué error comete?", "Inventa una parte no contada", "No se rellena lo reservado."),
        ex("¿Por qué se pide autorización antes de fotografiar? A) porque el evento y las personas pertenecen a la comunidad B) para tener más fotos", "A", "La comunidad decide qué se muestra."),
    ],
    D=[
        ex("Dos descripciones de la Mañana del Agua. A: «Se llega en silencio y lo que se dice no se cuenta». B: «Se llega en silencio y se canta una oración». ¿Cuál respeta el testimonio?", "A", "B agrega algo que no se contó."),
        ex("Un visitante quiere acompañar el evento y llega con un grupo grande. ¿Qué norma debió seguir primero? A) pedir permiso antes B) llevar más invitados", "A", "El testimonio dice que quien quiera acompañar pide permiso antes."),
    ],
    context=[ex("Tu curso fue invitado a un Encuentro de la Cosecha inventado. Una compañera quiere pasar por la zona reservada. ¿Qué le dices? A) que respete los límites que dio la comunidad B) que pase rápido", "A", "Se respetan los límites.")],
    selfcheck=[
        ex("Nombra las cuatro preguntas para leer un evento.", "Qué pasa, quiénes participan, qué normas hay y qué no se cuenta", "Están en la explicación."),
        ex("Verdadero o falso: un invitado respeta las normas de la comunidad.", "Verdadero", "Es parte del respeto."),
        ex("¿Qué escribes ante lo que no se cuenta? A) la comunidad no cuenta esta parte B) una versión probable", "A", "Es la forma de respetar."),
    ],
    task=T("Lee este testimonio inventado de don Aurelio, de Río Hondo: «La Reunión del Río se hace en la orilla del río cuando sube el agua. Llegan las familias, se hacen turnos para cuidar la orilla y compartimos el almuerzo. Quien visite debe pedir permiso a la comunidad. Hay una parte de la reunión que no contamos.» Responde por escrito: ¿qué pasa?, ¿quiénes participan?, ¿qué normas hay?, ¿qué no se cuenta? Agrega una pregunta que harías al educador tradicional.",
           "Pasa: se reúnen en la orilla cuando sube el agua. Participan las familias; hacen turnos y comparten el almuerzo. Norma: quien visite pide permiso. No se cuenta: una parte de la reunión. Pregunta: ¿qué reuniones de nuestra comunidad se pueden compartir con la escuela?",
           ["responde las cuatro preguntas", "usa solo datos del texto", "respeta el límite"], ["cuatro respuestas", "pregunta"], ["describir la parte que no se cuenta", "agregar datos"],
           "Pedir que señale en el texto cada respuesta."),
    reinforce="Subraya en el testimonio las normas de respeto con un color.",
    extend="Escribe tres normas de respeto que usarías si una comunidad te invitara a un evento.",
)

L(
    OA12, 3, materials=MAT,
    use="Aprenderé a reconocer relaciones entre un evento, el territorio, la producción y los valores de una comunidad. Sirve para entender por qué las comunidades hacen sus eventos.",
    prior=["Sé leer un evento con límites.", "Sé relacionar producción y territorio."],
    explain=[
        "Los eventos de una comunidad se relacionan con su vida. Algunos aparecen cuando termina un trabajo, como la cosecha o la pesca. Otros se hacen en un lugar importante del territorio. Otros reúnen a las personas para cuidar algo que es de todos, como el agua. Esas conexiones se llaman relaciones entre el evento y la vida de la comunidad.",
        "Para encontrar relaciones usamos tres preguntas. ¿Con qué lugar del territorio se relaciona el evento? ¿Con qué trabajo o producción? ¿Qué valor muestra, como compartir, cuidar o agradecer? Las respuestas se anotan con la fuente, y si la relación es solo mi idea, la marco con «puedo pensar que».",
        "También podemos hacer cuentas para entender la organización. Si en un evento participan 6 familias y cada una trae 5 canastos, se juntan 30 canastos. Las cuentas muestran cuánto se comparte, pero no explican el sentido del evento: eso lo cuenta la comunidad.",
    ],
    vocab=[("relación", "conexión entre un evento y algo de la vida de la comunidad"), ("producción", "lo que una comunidad cultiva, pesca, cría o elabora"), ("valor", "idea que guía cómo convivir, como compartir o cuidar"), ("organización", "manera en que se reparten las tareas"), ("cuenta", "operación con números")],
    worked=[
        W("Relacionar evento y producción", ECO + " ¿Con qué producción se relaciona?", ["El evento ocurre al terminar la cosecha.", "Cada familia trae lo que cosechó.", "La producción es la cosecha."], "Se relaciona con la cosecha de la huerta."),
        W("Hacer una cuenta del evento", "En el Encuentro de la Cosecha participan 6 familias y cada una trae 5 canastos. ¿Cuántos canastos hay?", ["Cada familia trae 5.", "Hay 6 familias.", "Multiplico 6 × 5."], "30 canastos."),
    ],
    mistakes=[
        M("Afirmar que un evento tiene una relación que la fuente no menciona.", "Sería inventar el sentido del evento.", "Escribe «puedo pensar que…»."),
        M("Pensar que las cuentas explican el sentido del evento.", "Muestran cantidades, no significados.", "El sentido lo cuenta la comunidad."),
    ],
    R=[
        ex("Testimonio inventado: «Cada familia trae lo que cosechó y lo compartimos». ¿Qué se hace con lo cosechado?", "Se comparte", "El testimonio lo dice."),
        ex("La Fiesta de la Caleta (inventada) se hace cuando vuelven los botes. ¿Con qué trabajo se relaciona? A) la pesca B) la tejeduría", "A", "Los botes vuelven de pescar."),
        ex("¿La Mañana del Agua se hace junto a una quebrada? Responde Sí o No.", "Sí", "El testimonio dice que se hace junto a la quebrada."),
    ],
    C=[
        ex("Verdadero o falso: los eventos de una comunidad pueden relacionarse con su trabajo.", "Verdadero", "Algunos se hacen al terminar una tarea."),
        ex("¿Qué es un valor? A) una idea que guía cómo convivir, como compartir B) un precio", "A", "Los valores guían la convivencia."),
        ex("Verdadero o falso: una cuenta puede decirme el sentido de un evento.", "Falso", "Solo muestra cantidades."),
    ],
    A=[
        arith("En una Fiesta de la Caleta (inventada) participan 7 familias y cada una aporta 4 fuentes de comida. ¿Cuántas fuentes de comida hay?", "7*4", "Se repite 4 siete veces."),
        arith("Las 28 fuentes de comida se reparten en partes iguales en 4 mesas. ¿Cuántas fuentes hay en cada mesa?", "28//4", "Se reparte en partes iguales."),
        ex("Testimonio inventado: «La Reunión del Río se hace para cuidar la orilla». ¿Qué valor se muestra? A) cuidar un lugar que es de todos B) competir", "A", "Cuidar la orilla muestra cuidado de lo común."),
    ],
    Z=[
        ex("Valeria dice: «Como en la cosecha llevan canastos, el evento es para vender». El testimonio dice que se comparte. ¿Qué error comete?", "Inventa un fin que la fuente no dice", "El testimonio habla de compartir."),
        ex("¿Por qué se hace una cuenta de los canastos? A) para entender cuánto se comparte B) para saber el sentido espiritual del evento", "A", "Las cuentas muestran cantidades, no sentidos."),
    ],
    D=[
        arith("Un grupo de 5 familias de Pampa Larga trae 9 baldes de agua cada una para limpiar el pozo. Se usan todos los baldes en 3 turnos iguales. ¿Cuántos baldes hay por turno?", "(5*9)//3", "Primero el total: 5 × 9 = 45; luego se reparte en 3 turnos."),
        ex("Quieres relacionar la Mañana del Agua con una producción, pero el testimonio no habla de ninguna. ¿Qué escribes? A) el testimonio no lo dice B) la relaciono con la cosecha", "A", "No se inventa."),
    ],
    context=[ex("Tu curso organiza una once compartida inspirada en el Encuentro de la Cosecha inventado. Hay 24 sándwiches y 6 mesas. ¿Cuántos sándwiches hay por mesa si se reparten por igual? Responde con un número.", "4", "24 ÷ 6 = 4.")],
    selfcheck=[
        ex("Nombra las tres preguntas para encontrar relaciones de un evento.", "Con qué lugar, con qué trabajo y qué valor muestra", "Están en la explicación."),
        ex("Verdadero o falso: si la relación es solo mi idea, la marco con «puedo pensar que».", "Verdadero", "Así no se atribuye a la comunidad."),
        ex("¿Quién explica el sentido de un evento de un pueblo real? A) su comunidad B) una cuenta", "A", "Ella lo cuenta."),
    ],
    task=T("Lee: «Fiesta de la Caleta (inventada). Se hace cuando vuelven los botes. Participan 8 familias y cada una aporta 3 ollas de comida. Hay juegos en la playa y se invita a los vecinos.» Responde: ¿con qué lugar, con qué trabajo y con qué valor se relaciona?, ¿cuántas ollas hay?, y escribe una relación tuya marcada con «puedo pensar que».",
           "Lugar: la playa de la caleta. Trabajo: la pesca. Valor: compartir con los vecinos. Hay 8 × 3 = 24 ollas. Puedo pensar que se juntan para agradecer una buena pesca, aunque el texto no lo dice.",
           ["relaciona lugar, trabajo y valor", "calcula bien", "marca su idea"], ["tres respuestas", "cuenta", "frase"], ["afirmar sentidos no contados", "error de cuenta"],
           "Pedir que muestre la cuenta y la frase de la fuente."),
    reinforce="Dibuja un esquema con tres flechas que salen del evento: lugar, trabajo y valor.",
    extend="Inventa una cuenta para otro evento con 4 familias que aportan 5 cosas cada una y resuélvela.",
)

L(
    OA12, 4, materials=MAT,
    use="Aprenderé a escribir una descripción atribuida de un evento: qué cuenta la fuente, normas, relaciones y límites. Sirve para presentar un evento de una comunidad con respeto.",
    prior=["Sé leer un evento con límites.", "Sé relacionar un evento con la vida de la comunidad."],
    explain=[
        "Una descripción atribuida de un evento tiene cinco partes. Primero, el nombre del evento y la fuente. Segundo, qué pasa, según la fuente. Tercero, quiénes participan y qué normas hay. Cuarto, las relaciones que encuentro, con la marca de quién las dice. Quinto, los límites: lo que no se cuenta y lo que preguntaré.",
        "Se escribe con frases como «según don Camilo…» y «yo pienso que…». No se usan verbos que den certeza donde no la hay: en vez de «seguro que», usamos «puede ser que» o «el testimonio no lo dice». Tampoco se afirma que todos los pueblos hacen eventos iguales.",
        "Una descripción atribuida de un evento ceremonial es breve. Dice solo lo que la comunidad contó y lo demás se escribe como límite. Cuando la terminamos, se la mostramos a la comunidad o al educador tradicional para que corrijan lo necesario.",
    ],
    vocab=[("descripción atribuida", "descripción en que cada dato dice de quién viene"), ("certeza", "seguridad de que algo es cierto"), ("breve", "corto y con lo necesario"), ("corregir", "cambiar lo que quedó mal"), ("devolución", "mostrar el trabajo a la comunidad")],
    worked=[
        W("Escribir una descripción", EIN + " Escribe una descripción atribuida.", ["Nombro el evento y la fuente.", "Cuento qué pasa y quiénes participan.", "Agrego un límite."], "Según don Camilo, de Isla Niebla (inventado), la Fiesta de la Caleta se hace cuando vuelven los botes. Hay comida compartida, música y juegos en la playa, y se invita a los vecinos. El testimonio no dice cómo se organiza la comida."),
        W("Cambiar certeza por límite", "Un niño escribe: «Seguro que antes de la fiesta rezan». ¿Cómo lo corriges?", ["El testimonio no habla de rezar.", "«Seguro» da certeza falsa.", "Cambio a un límite."], "«El testimonio no dice qué se hace antes de la fiesta»."),
    ],
    mistakes=[
        M("Usar «seguro que» para algo que la fuente no dijo.", "Da certeza falsa.", "Usa «el testimonio no lo dice»."),
        M("Escribir un texto largo sobre un evento ceremonial que se contó poco.", "Se rellena con ideas propias.", "Sé breve y declara el límite."),
    ],
    R=[
        ex("¿Cuántas partes tiene la descripción atribuida de un evento? Escribe el número.", "5", "Nombre y fuente, qué pasa, participantes y normas, relaciones, límites."),
        ex("Don Camilo cuenta que la Fiesta de la Caleta se hace cuando vuelven los botes. ¿Quién es la fuente?", "Don Camilo", "Es quien lo cuenta."),
        ex("¿Qué usas en vez de «seguro que»? A) «el testimonio no lo dice» B) «de todas formas»", "A", "Declara el límite."),
    ],
    C=[
        ex("Verdadero o falso: la descripción de un evento ceremonial debe ser breve y respetar lo que se contó.", "Verdadero", "Se evita rellenar."),
        ex("¿Para qué se muestra el texto a la comunidad? A) para que corrija lo necesario B) para presumir", "A", "Ellos conocen su evento."),
        ex("Verdadero o falso: puedo escribir que todos los pueblos hacen eventos iguales.", "Falso", "Cada pueblo tiene los suyos."),
    ],
    A=[
        ex("Ordena las partes de la descripción: A) límites B) nombre y fuente C) qué pasa. ¿Cuál va primero?", "B", "Se empieza nombrando el evento y la fuente."),
        ex("Clasifica en DATO DE LA FUENTE o MI IDEA: a) según don Camilo, se invita a los vecinos b) puedo pensar que la fiesta alegra a la comunidad.", "a dato de la fuente, b mi idea", "La primera está escrita; la segunda es mía."),
        ex("El testimonio de la Fiesta de la Caleta no dice quién prepara la comida. ¿Cuál es un límite bien escrito? A) El testimonio no dice quién prepara la comida B) Seguro que la prepara una sola familia", "A", "El límite declara lo que la fuente no cuenta."),
    ],
    Z=[
        ex("Paula escribe cinco párrafos sobre una ceremonia de la que solo se contó una frase. ¿Qué problema tiene?", "Rellena con ideas propias", "Debe ser breve."),
        ex("¿Por qué conviene marcar quién dice cada dato? A) para saber qué viene de la comunidad y qué es mío B) para alargar", "A", "La atribución distingue voces."),
    ],
    D=[
        ex("Dos descripciones de la Noche de las Linternas (evento de cultura inventada). A: «Según el texto, las familias cuelgan linternas y los vecinos pasean». B: «Seguro que cantan canciones tristes». ¿Cuál es atribuida?", "A", "B agrega algo no dicho."),
        ex("Tu descripción está lista. ¿Qué haces antes de presentarla? A) la muestro a la comunidad o al educador B) la presento ya", "A", "Se pide revisión."),
    ],
    context=[ex("Preparas un cartel sobre un evento para la feria de la escuela. ¿Qué frase pones? A) «Según don Camilo, de Isla Niebla (inventado)…» B) «Todos los pueblos hacen una fiesta así»", "A", "Se atribuye al testimonio.")],
    selfcheck=[
        ex("Nombra tres de las cinco partes de la descripción.", "Tres entre: nombre y fuente, qué pasa, participantes y normas, relaciones, límites", "Están en la explicación."),
        ex("Verdadero o falso: puedo decir «seguro que…» cuando la fuente no lo dijo.", "Falso", "Da certeza falsa."),
        ex("¿Qué haces con un evento ceremonial del que sabes poco? A) escribo poco y declaro el límite B) invento el resto", "A", "Se respeta lo que la comunidad contó."),
    ],
    task=T("Usa este texto inventado de Ladera Verde, de doña Elena: «El Encuentro de la Cosecha lo organizan las familias cuando termina la cosecha. Nos juntamos en la explanada y compartimos lo cosechado. Hay una despedida del día que es solo para la comunidad.» Escribe una descripción de cinco partes: nombre y fuente, qué pasa, participantes y normas, una relación (con «yo pienso que») y límites con una pregunta para el educador tradicional.",
           "Encuentro de la Cosecha, según doña Elena, de Ladera Verde (inventado). Pasa: las familias se juntan en la explanada al terminar la cosecha y comparten lo cosechado. Participan las familias; hay una despedida solo para la comunidad. Yo pienso que el evento une la cosecha con compartir. No se cuenta la despedida. Pregunta: ¿qué eventos de nuestra zona se pueden conocer en la escuela?",
           ["incluye las cinco partes", "usa solo datos del texto", "respeta la despedida"], ["descripción de cinco partes"], ["describir la despedida", "usar certezas falsas"],
           "Pedir que señale en el texto de qué línea sale cada parte."),
    reinforce="Numera las cinco partes de tu descripción para comprobar que están todas.",
    extend="Reescribe la descripción en tres líneas para un afiche, sin perder la fuente ni los límites.",
)

L(
    OA12, 5, materials=MAT,
    use="Aprenderé a contrastar eventos de distintos pueblos y de otras culturas, sin decir que uno es más importante o más auténtico. Sirve para comprender la diversidad de formas de reunirse y celebrar.",
    prior=["Sé describir un evento con fuente y límites.", "Sé comparar sin jerarquizar."],
    explain=[
        "Para contrastar eventos usamos criterios iguales. Tres criterios útiles son: para qué se reúne la comunidad, quién participa y qué normas hay. Con ellos comparamos el Encuentro de la Cosecha (Ladera Verde), la Fiesta de la Caleta (Isla Niebla) y la Noche de las Linternas (Costa Lejana), todos inventados.",
        "En los tres, la comunidad se reúne y comparte algo. Pero cada uno tiene su sentido y su forma: uno celebra una cosecha, otro la vuelta de los botes y el tercero se vive caminando por las calles. También hay diferencias en quién participa y en qué normas se cuentan.",
        "Contrastar no es decir cuál evento es más importante, más auténtico o «más indígena». Tampoco se compara un evento ceremonial con uno festivo para decir cuál vale más. Cada evento se comprende por lo que significa para su comunidad. Las conclusiones valen solo para los casos que leímos.",
    ],
    vocab=[("contrastar", "ver semejanzas y diferencias"), ("auténtico", "que se considera verdadero o propio; no se usa para ordenar eventos"), ("criterio", "punto igual para comparar"), ("festivo", "de fiesta"), ("generalizar", "decir que algo vale para todos")],
    worked=[
        W("Contrastar con un criterio", "Criterio: «cómo se comparte». Encuentro de la Cosecha: cada familia trae lo cosechado. Fiesta de la Caleta: comida compartida. Noche de las Linternas: se comparte pan. ¿Qué tienen en común?", ["En los tres se comparte comida.", "Cambia qué se trae y cuándo.", "Es una semejanza."], "En los tres se comparte comida; cambian qué se trae y cuándo."),
        W("Evitar la jerarquía", "Un niño dice: «La Mañana del Agua es más auténtica que la Fiesta de la Caleta». ¿Qué corriges?", ["Auténtica no sirve para ordenar eventos.", "Son eventos distintos.", "Cada uno tiene su sentido."], "Corrijo: son eventos con sentidos distintos y no se ordenan."),
    ],
    mistakes=[
        M("Decir que un evento es más auténtico que otro.", "Jerarquiza sin fuente.", "Compara con criterios iguales."),
        M("Concluir que todos los pueblos comparten comida en sus eventos.", "Solo se compararon tres casos.", "Escribe «en estos tres eventos»."),
    ],
    R=[
        ex("En la Noche de las Linternas (inventada), ¿qué se comparte al final?", "Pan", "El texto lo dice."),
        ex("En la Fiesta de la Caleta, ¿cuándo se hace? A) cuando vuelven los botes B) cuando termina la cosecha", "A", "Don Camilo lo cuenta así."),
        ex("¿Qué evento se hace junto a la quebrada al amanecer, según doña Elena? A) la Mañana del Agua B) el Encuentro de la Cosecha", "A", "El testimonio lo dice."),
    ],
    C=[
        ex("Verdadero o falso: contrastar eventos es decir cuál es más importante.", "Falso", "Contrastar es ver semejanzas y diferencias."),
        ex("¿Qué es un criterio? A) un punto igual para comparar todos los eventos B) una opinión", "A", "Así la comparación es justa."),
        ex("Verdadero o falso: puedo comparar un evento ceremonial con uno festivo para decir cuál vale más.", "Falso", "Cada evento tiene su sentido."),
    ],
    A=[
        ex("Criterio: «para qué se reúnen». Encuentro de la Cosecha: compartir lo cosechado. Fiesta de la Caleta: celebrar la vuelta de los botes. ¿Qué semejanza hay? A) en ambos se reúnen para compartir tras un trabajo B) en ambos no hay comida", "A", "Los dos ocurren después de un trabajo de la comunidad."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en ambos eventos se invita a la comunidad b) uno es en una explanada y el otro en una playa.", "a semejanza, b diferencia", "La primera es común; la segunda cambia."),
        ex("Norma de la Mañana del Agua: llegar en silencio. Norma de la Fiesta de la Caleta: según el testimonio, no se menciona ninguna. ¿Qué escribes en la columna «normas» de la Fiesta? A) el testimonio no las dice B) llegar en silencio", "A", "No se inventan normas."),
    ],
    Z=[
        ex("Hugo concluye: «En todos los pueblos hay eventos con comida». ¿Qué error comete?", "Generaliza desde tres casos", "Tres casos no representan a todos los pueblos."),
        ex("Una niña pregunta cuál de los tres eventos es el mejor. ¿Qué respondes? A) no se ordenan: cada uno tiene su sentido B) el de la caleta", "A", "Comparar no es jerarquizar."),
    ],
    D=[
        ex("Cuadro con el criterio «dónde ocurre»: Encuentro de la Cosecha, la explanada; Fiesta de la Caleta, la playa; Noche de las Linternas, frente a las casas. ¿Cuál afirmación es correcta? A) los tres ocurren en lugares de la comunidad B) los tres ocurren en la playa", "A", "Todos son lugares comunes."),
        ex("Quieres incluir en tu cuadro un evento de una familia del curso, que autorizó contarlo. ¿Qué haces? A) lo trato con el mismo respeto B) lo pongo al final por ser menos conocido", "A", "No se jerarquiza."),
    ],
    context=[ex("En una exposición, un visitante pregunta cuál evento es más indígena. ¿Qué respondes? A) los eventos de este cuaderno son inventados y no se ordenan B) el más antiguo", "A", "Aclara la naturaleza de los ejemplos.")],
    selfcheck=[
        ex("Nombra dos criterios para contrastar eventos.", "Dos entre: para qué se reúnen, quién participa, qué normas hay, dónde ocurre", "Están en la explicación."),
        ex("Verdadero o falso: puedo decir que un evento es más auténtico que otro.", "Falso", "No hay fuente que lo diga."),
        ex("¿Qué escribes si un texto no dice las normas? A) el texto no las dice B) las invento", "A", "No se inventa."),
    ],
    task=T("Compara dos eventos inventados con tres criterios: para qué se reúne la comunidad, quién participa y qué normas hay. Evento 1: «Día del Pozo (Pampa Larga): se limpia el pozo entre todos y se comparte la comida; participan todas las personas; hay una parte que no se cuenta.» Evento 2: «Noche de las Linternas (Costa Lejana): las familias cuelgan linternas y los vecinos pasean; no se mencionan normas.» Escribe una semejanza, una diferencia y qué no puedes concluir.",
           "Día del Pozo: cuidar el pozo y compartir; participan todas las personas; hay una parte reservada. Noche de las Linternas: mostrar linternas y pasear; participan familias y vecinos; no se mencionan normas. Semejanza: en ambos participa la comunidad. Diferencia: uno cuida un lugar y el otro muestra linternas. No puedo concluir que todos los pueblos hagan eventos así.",
           ["usa tres criterios iguales", "semejanza y diferencia", "no jerarquiza ni generaliza"], ["tabla de tres criterios", "tres frases"], ["decir cuál es mejor", "inventar normas"],
           "Pedir que indique la fuente de cada celda."),
    reinforce="Pinta de verde las semejanzas y de azul las diferencias en tu tabla.",
    extend="Agrega la Mañana del Agua a tu tabla y explica por qué la columna de normas cambia.",
)

L(
    OA12, 6, materials=MAT,
    use="Aprenderé a comunicar un análisis de eventos y a revisarlo con la validación de la comunidad o del educador tradicional. Sirve para presentar un trabajo respetuoso sobre eventos que no son míos.",
    prior=["Sé describir y contrastar eventos con fuente y límites.", "Sé que la validación va antes de presentar."],
    explain=[
        "Al comunicar un análisis de eventos, la presentación debe ser clara y respetuosa. Dice qué evento es, de quién es la fuente, qué aprendí, qué relaciones encontré y qué no corresponde divulgar. También avisa que los eventos de este cuaderno son inventados y que los reales los cuenta la comunidad.",
        "Una presentación respetuosa no usa imágenes ni dramatizaciones de ceremonias de un pueblo sin su permiso. Si se quiere mostrar algo, se usan dibujos propios sobre partes públicas, como el lugar, los alimentos compartidos o los carteles de invitación. Las partes reservadas no se dibujan.",
        "La revisión con validación pertinente sigue una lista: ¿hay fuente?, ¿está atribuido cada dato?, ¿hay límites?, ¿no jerarquicé?, ¿no imité una ceremonia?, ¿pedí permiso para imágenes? Si algo falla, se corrige antes de mostrar. Si la comunidad pide quitar algo, se quita y se agradece.",
    ],
    vocab=[("dramatización", "representación de una escena con personas"), ("parte pública", "lo que la comunidad acepta que se cuente"), ("parte reservada", "lo que la comunidad decide no contar"), ("validación", "revisión por quien conoce la cultura"), ("presentación", "exposición ante otras personas")],
    worked=[
        W("Elegir qué dibujar", "Para un cartel de la Mañana del Agua (inventada), ¿qué puedes dibujar? A) la quebrada al amanecer B) lo que se dice esa mañana", ["Lo que se dice no se cuenta.", "La quebrada es un lugar público.", "Elijo la A."], "A"),
        W("Revisar un cartel", "Un cartel dice: «Todos los pueblos hacen una ceremonia del agua». ¿Qué falla?", ["Generaliza a todos los pueblos.", "No nombra fuente.", "Hay que corregir ambas cosas."], "Generaliza y no tiene fuente; debo atribuirlo a doña Elena, de Ladera Verde (inventado), y quitar «todos los pueblos»."),
    ],
    mistakes=[
        M("Dramatizar una ceremonia en la presentación.", "Es imitar lo sagrado sin permiso.", "Usa dibujos de lugares y objetos públicos."),
        M("Mostrar imágenes de personas de la comunidad sin permiso.", "La imagen es de la persona.", "Pide autorización o usa dibujos."),
    ],
    R=[
        ex("Para un cartel del Encuentro de la Cosecha (inventado), ¿qué puedes dibujar? A) la explanada con canastos B) una parte que la comunidad decidió no contar", "A", "Lo que no se cuenta no se dibuja."),
        ex("¿Se puede dramatizar una ceremonia de un pueblo sin permiso? Responde Sí o No.", "No", "Se faltaría al respeto a lo sagrado."),
        ex("¿Quién cuenta los eventos reales de un pueblo? A) la comunidad B) cualquier persona", "A", "Ella es la fuente."),
    ],
    C=[
        ex("Verdadero o falso: se puede mostrar la imagen de una persona de la comunidad sin su permiso.", "Falso", "La imagen necesita autorización."),
        ex("¿Qué es una parte reservada? A) lo que la comunidad decide no contar B) lo que está en el cartel", "A", "Esa parte se respeta."),
        ex("Verdadero o falso: antes de presentar, se revisa con una lista.", "Verdadero", "La lista ayuda a evitar errores."),
    ],
    A=[
        ex("Borrador: «Todos los pueblos hacen eventos de agradecimiento». ¿Qué falla principal tiene? A) generaliza sin fuente B) tiene tildes", "A", "No hay fuente de todos los pueblos."),
        ex("Clasifica en PARTE PÚBLICA o RESERVADA, según el testimonio de doña Elena: a) la quebrada donde se hace la Mañana del Agua b) lo que se dice esa mañana.", "a pública, b reservada", "La primera se cuenta; la segunda no."),
        ex("¿Cuál es un recurso respetuoso para una presentación? A) un dibujo de la explanada B) una dramatización de una ceremonia", "A", "La explanada es un lugar público."),
    ],
    Z=[
        ex("Andrés dice: «Si no me dejan mostrar la ceremonia, la mostraré igual con disfraces». ¿Qué error comete?", "No respeta el límite de la comunidad", "Los límites se respetan."),
        ex("¿Por qué se avisa que los eventos del cuaderno son inventados? A) para no confundirlos con eventos reales de un pueblo B) para que parezcan reales", "A", "Evita atribuir a un pueblo algo inventado."),
    ],
    D=[
        ex("Revisa: «Según doña Elena, de Ladera Verde (inventado), el Encuentro de la Cosecha reúne a las familias. Yo pienso que une a la comunidad. No sé cómo se organiza el reparto». ¿Qué falta antes de presentarlo? A) pedir revisión B) más datos inventados", "A", "Ya tiene fuente, idea y límite."),
        ex("La comunidad te pide quitar de tu panel la foto de la quebrada. ¿Qué haces? A) la quito y agradezco B) la dejo porque es bonita", "A", "Se obedece la validación."),
    ],
    context=[ex("En la muestra de la escuela, un grupo propone representar la Mañana del Agua con disfraces. ¿Qué dices? A) mejor presentar un cartel con datos públicos B) que lo hagan igual", "A", "No se dramatiza lo ceremonial.")],
    selfcheck=[
        ex("Nombra dos preguntas de la lista de revisión.", "Dos entre: fuente, atribución, límites, no jerarquizar, no imitar, permisos", "Están en la explicación."),
        ex("Verdadero o falso: una comunidad puede pedir quitar algo de mi trabajo.", "Verdadero", "Su validación manda."),
        ex("¿Qué haces con las partes reservadas? A) no las dibujo ni las cuento B) las adivino", "A", "Las partes reservadas se respetan."),
    ],
    task=T("Prepara un cartel de 5 líneas sobre el Encuentro de la Cosecha inventado de Ladera Verde (testimonio de doña Elena: «Las familias se juntan en la explanada cuando termina la cosecha, comparten lo cosechado y hay juegos para los niños. La despedida es solo para la comunidad»). Incluye: título, fuente, dos datos públicos, una frase «yo pienso que…» y una nota que diga que el evento es inventado y que la despedida no se cuenta. Describe qué dibujo pondrías.",
           "Título: Encuentro de la Cosecha (inventado). Fuente: doña Elena, de Ladera Verde. Las familias se juntan en la explanada y comparten lo cosechado. Hay juegos para los niños. Yo pienso que el evento une a la comunidad. Nota: la despedida no se cuenta. Dibujo: la explanada con canastos.",
           ["incluye título, fuente, dos datos, idea y nota", "no cuenta la despedida", "dibujo de lo público"], ["cartel de cinco líneas", "descripción del dibujo"], ["dramatizar", "contar la despedida"],
           "Pedir que explique por qué eligió ese dibujo."),
    reinforce="Haz una lista de revisión de seis preguntas con casilla y úsala con tu cartel.",
    extend="Escribe cómo pedirías permiso a la comunidad para exponer tu cartel en la escuela.",
)

# ============================================================ OA 13 · Valores comunitarios y espirituales
L(
    OA13, 1, materials=MAT,
    use="Aprenderé a situar los valores comunitarios y espirituales que una comunidad expresa en lo que hace y dice. Sirve para comparar valores de distintos pueblos sin inventarlos.",
    prior=["Sé situar una fuente con su ficha.", "Sé que la visión de mundo es una manera de entender la vida."],
    explain=[
        "Un valor es una idea que guía cómo convivir y qué cuidar. Los valores comunitarios guían la vida entre las personas, como ayudar, compartir, respetar a las personas mayores o trabajar juntos. Los valores espirituales guían el cuidado de lo que la comunidad considera sagrado, como agradecer, guardar silencio o respetar ciertos lugares.",
        "Un valor se reconoce en lo que una comunidad hace y dice, y no solo en palabras bonitas. Si una comunidad reparte la cosecha, se puede reconocer el valor de compartir. Pero esa idea debe aparecer en la fuente. Los valores de un pueblo real los explica su comunidad, y no deben inventarse ni simplificarse en una lista.",
        "En esta clase usamos testimonios inventados. Cada ficha dice quién habla, de qué comunidad, con qué permiso y qué no se cuenta. Con esos datos podemos decir qué valor se expresa en una acción, siempre con la marca «según la fuente».",
    ],
    vocab=[("valor", "idea que guía cómo convivir y qué cuidar"), ("valor comunitario", "valor que guía la vida entre las personas"), ("valor espiritual", "valor que guía el cuidado de lo sagrado"), ("acción", "algo que una persona o comunidad hace"), ("simplificar", "reducir algo complejo a una frase que lo deforma")],
    worked=[
        W("Reconocer un valor", "Testimonio inventado de doña Elena: «Cuando alguien enferma, las familias le llevan comida y cuidan su huerta». ¿Qué valor se muestra?", ["La acción es ayudar a quien lo necesita.", "Las familias lo hacen juntas.", "El valor es la ayuda mutua."], "La ayuda mutua, según el testimonio."),
        W("Valor espiritual", "Testimonio inventado de don Camilo: «Antes de entrar al bosque pedimos permiso en silencio». ¿Qué valor espiritual se muestra?", ["La acción es pedir permiso en silencio.", "Muestra respeto por el bosque.", "El valor es el respeto a lo sagrado."], "El respeto por el bosque, según el testimonio."),
    ],
    mistakes=[
        M("Decir que una comunidad tiene un valor porque «suena bien».", "Falta una acción o una frase de la fuente.", "Busca la acción que lo muestra."),
        M("Reducir los valores de un pueblo a una lista de palabras.", "Los pueblos explican sus valores con sus propias formas.", "Pregunta al educador tradicional."),
    ],
    R=[
        ex("Testimonio inventado: «Las familias le llevan comida a quien enferma». ¿Qué hacen las familias?", "Llevan comida a quien enferma", "El testimonio lo dice."),
        ex("Testimonio inventado: «Antes de entrar al bosque pedimos permiso en silencio». ¿Qué se hace antes de entrar al bosque? A) pedir permiso en silencio B) cortar leña", "A", "El testimonio lo dice."),
        ex("¿Los valores se reconocen en lo que la comunidad hace y dice? Responde Sí o No.", "Sí", "Se ven en las acciones."),
    ],
    C=[
        ex("Verdadero o falso: un valor es una idea que guía cómo convivir.", "Verdadero", "Es la definición de la clase."),
        ex("¿Cuál es un valor espiritual? A) respetar un lugar que se considera sagrado B) comprar pan", "A", "Cuida lo sagrado."),
        ex("Verdadero o falso: puedo decidir los valores de un pueblo mirando su ropa.", "Falso", "Los explica el pueblo."),
    ],
    A=[
        ex("Clasifica en COMUNITARIO o ESPIRITUAL, según la clase: a) compartir la cosecha entre familias b) agradecer el agua en silencio.", "a comunitario, b espiritual", "El primero guía la vida entre personas; el segundo, el cuidado de lo sagrado."),
        ex("Testimonio inventado: «Entre todas las familias arreglamos el techo de la sede». ¿Qué valor se muestra? A) trabajar juntos B) competir", "A", "Todos participan en una tarea común."),
        ex("Una ficha trae un valor, pero no dice quién lo cuenta. ¿Qué falta? A) la fuente B) un título más largo", "A", "Sin fuente no se puede atribuir."),
    ],
    Z=[
        ex("Rebeca escribe: «Esta comunidad tiene el valor de la libertad». El testimonio solo dice que reparten semillas. ¿Qué error comete?", "Inventa un valor que no se ve en la fuente", "El testimonio muestra compartir."),
        ex("¿Por qué conviene buscar una acción antes de nombrar un valor? A) porque las acciones muestran el valor B) para escribir más", "A", "Las acciones respaldan el valor."),
    ],
    D=[
        ex("Una acción puede mostrar dos valores. Testimonio inventado: «Compartimos la cosecha y agradecemos la tierra en silencio». ¿Qué dos valores se muestran? A) compartir y agradecer B) competir y apurarse", "A", "Las dos acciones muestran esos valores."),
        ex("Un compañero quiere hacer un cartel con «los valores de los pueblos indígenas» en una lista. ¿Qué le sugieres? A) usar los de una comunidad y su fuente B) mezclar todos", "A", "Cada pueblo tiene los suyos."),
    ],
    context=[ex("En tu curso proponen un día de ayuda mutua inspirado en lo que cuentan los testimonios inventados. ¿Qué acción se parece al valor de la ayuda mutua? A) arreglar entre todos algo del curso B) cada uno hace lo suyo sin ayudar", "A", "Trabajar juntos muestra ayuda mutua.")],
    selfcheck=[
        ex("Explica con tus palabras qué es un valor.", "Una idea que guía cómo convivir y qué cuidar", "Es la definición de la clase."),
        ex("Verdadero o falso: un valor se apoya en una acción de la fuente.", "Verdadero", "Así se evita inventar valores."),
        ex("¿Quién explica los valores de un pueblo real? A) su comunidad o el educador tradicional B) cualquiera", "A", "Ellos son la fuente."),
    ],
    task=T("Lee estos testimonios inventados de Río Hondo. Don Aurelio: «Entre todos limpiamos la orilla del río cada año». Doña Inés: «Antes de cortar lana nos quedamos un momento en silencio para agradecer al rebaño». Para cada uno escribe: la acción, el valor que muestra, si es comunitario o espiritual y una cosa que no sabes. No agregues datos nuevos.",
           "Don Aurelio: limpian la orilla entre todos; trabajar juntos; comunitario; no sé cómo se organizan los turnos. Doña Inés: guardan un momento de silencio para agradecer; agradecimiento y respeto; espiritual; no sé cómo agradecen ni qué significa para ellos.",
           ["identifica acciones", "nombra valores", "clasifica y señala un límite"], ["tabla de dos filas"], ["inventar valores", "inventar cómo agradecen"],
           "Pedir que señale la frase del testimonio de cada acción."),
    reinforce="Dibuja las dos acciones con una flecha hacia el valor que muestran.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo su comunidad explica el valor de compartir.",
)

L(
    OA13, 2, materials=MAT,
    use="Aprenderé a leer testimonios sobre valores con límites: qué dice la fuente, qué interpreto y qué no se cuenta. Sirve para comparar valores sin deformarlos.",
    prior=["Sé que un valor se reconoce en una acción.", "Sé separar fuente e interpretación."],
    explain=[
        "Al leer un testimonio sobre valores seguimos tres pasos. Primero, subrayamos las acciones que cuenta la fuente. Segundo, decimos qué valor podría mostrar cada acción, con la frase «según la fuente» si ella lo dice y «puedo pensar que» si es mi interpretación. Tercero, escribimos qué no se cuenta.",
        "Un valor no se prueba con una sola acción. Una comunidad puede tener muchas formas de mostrar un valor, y una misma acción puede mostrar más de un valor. Por eso evitamos frases absolutas como «siempre» o «todas las familias» si la fuente no las usa.",
        "También debemos tener cuidado con los valores espirituales. Lo que una comunidad considera sagrado se respeta aunque no se explique. Si no se cuenta, escribimos «no se cuenta». Y si queremos saber más, preguntamos al educador o educadora tradicional, sin insistir.",
    ],
    vocab=[("acción", "algo que una persona o comunidad hace"), ("absoluto", "que no admite excepciones, como «siempre» o «todos»"), ("interpretación", "idea propia sobre lo que muestra una acción"), ("sagrado", "muy importante y digno de respeto"), ("límite", "lo que no se cuenta")],
    worked=[
        W("Separar fuente e interpretación", "Doña Elena (inventada): «En mi comunidad compartimos las semillas en cada siembra». Escribe un dato de la fuente y una interpretación.", ["Fuente: comparten las semillas en cada siembra.", "Interpretación: puedo pensar que valoran compartir.", "Los marco distinto."], "Según doña Elena, comparten las semillas en cada siembra. Puedo pensar que valoran compartir."),
        W("Evitar frases absolutas", "Un niño escribe: «Todas las familias siempre comparten sus semillas». ¿Qué corriges?", ["Doña Elena dice «en cada siembra» sobre su comunidad.", "No dice «todas» ni «siempre».", "Quito las palabras absolutas."], "Corrijo: «Según doña Elena, en su comunidad comparten semillas en cada siembra»."),
    ],
    mistakes=[
        M("Usar «siempre» o «todos» sin que la fuente lo diga.", "Exagera lo que se contó.", "Usa solo lo que dice el testimonio."),
        M("Explicar el significado de un valor espiritual que no se contó.", "Se inventa su sentido.", "Escribe «no se cuenta»."),
    ],
    R=[
        ex("Doña Elena (inventada): «Compartimos las semillas en cada siembra». ¿Qué comparten?", "Las semillas", "El testimonio lo dice."),
        ex("Don Aurelio (inventado): «Cuidamos entre todos la orilla del río». ¿Quiénes cuidan la orilla? A) entre todos B) solo don Aurelio", "A", "El testimonio dice «entre todos»."),
        ex("¿Qué palabras evitas si la fuente no las usa? A) siempre y todos B) según", "A", "Son palabras absolutas que exageran."),
    ],
    C=[
        ex("Verdadero o falso: una misma acción puede mostrar más de un valor.", "Verdadero", "Una acción puede expresar varios."),
        ex("Verdadero o falso: un valor se prueba con una sola acción.", "Falso", "Una acción no basta para afirmar un valor."),
        ex("¿Qué haces con un valor espiritual que la comunidad no explicó? A) escribo que no se cuenta B) invento su sentido", "A", "Lo reservado se respeta."),
    ],
    A=[
        ex("Testimonio inventado: «Los niños saludan a las personas mayores al pasar». Clasifica en ACCIÓN o VALOR: a) los niños saludan a las personas mayores b) respeto por las personas mayores.", "a acción, b valor", "El saludo se ve; el respeto es el valor."),
        ex("Don Camilo (inventado): «Cada familia deja un poco de leña para quien la necesite». Escribe una interpretación marcada correctamente. A) Puedo pensar que valoran ayudar a otros B) Don Camilo dice que valoran ayudar", "A", "Don Camilo no usó esa palabra."),
        ex("Una frase dice: «Todas las comunidades indígenas comparten sus cosechas». ¿Qué palabra la hace absoluta?", "Todas", "No se puede generalizar así."),
    ],
    Z=[
        ex("Víctor escribe que la comunidad «adora» el bosque porque piden permiso antes de entrar. ¿Qué error comete?", "Interpreta un rito que no se contó", "La fuente solo dice que piden permiso."),
        ex("¿Por qué evitar «siempre» y «todos»? A) porque la fuente habla de casos concretos B) porque son palabras largas", "A", "Así se evita exagerar lo contado."),
    ],
    D=[
        ex("Dos frases sobre el testimonio «Los niños saludan a las personas mayores». 1) «Según el testimonio, los niños saludan a las personas mayores». 2) «Todos los niños indígenas respetan a los mayores». ¿Cuál se queda en la fuente?", "La primera", "La segunda generaliza."),
        ex("Un valor espiritual se menciona pero no se explica. ¿Qué escribes en tus límites? A) no se cuenta su sentido B) lo explico a mi manera", "A", "Se respeta lo reservado."),
    ],
    context=[ex("Un afiche de tu escuela dice «Los pueblos indígenas siempre comparten todo». ¿Qué cambiarías? A) hablar de una comunidad y su fuente B) agregar más ejemplos", "A", "Evita la generalización.")],
    selfcheck=[
        ex("Nombra los tres pasos para leer un testimonio sobre valores.", "Subrayar acciones, decir qué valor muestran y escribir qué no se cuenta", "Están en la explicación."),
        ex("Verdadero o falso: puedo usar «siempre» aunque la fuente no lo diga.", "Falso", "Exagera lo que dijo la fuente."),
        ex("¿Cómo marcas tu interpretación? Escribe una frase de inicio.", "Puedo pensar que", "Así se distingue de la fuente."),
    ],
    task=T("Lee este testimonio inventado de doña Marta, de Pampa Larga: «Quien llega al pozo con sed puede tomar agua primero. Después de tomar agradecemos en silencio. Hay cosas del pozo que solo contamos a la comunidad.» Haz tres columnas: acción, valor que podría mostrar (con «puedo pensar que») y límite. Revisa que no uses «siempre» ni «todos».",
           "Acción: quien llega con sed toma agua primero; agradecen en silencio. Valor: puedo pensar que valoran ayudar a quien lo necesita y agradecer. Límite: hay cosas del pozo que no se cuentan.",
           ["identifica acciones", "marca interpretaciones", "señala el límite", "no usa absolutos"], ["tabla de tres columnas"], ["usar «siempre»", "inventar el sentido del agradecimiento"],
           "Pedir que señale la frase del testimonio de cada acción."),
    reinforce="Subraya en el testimonio las acciones y rodea con círculo los valores que propones.",
    extend="Escribe una frase absoluta y reescríbela sin absolutos.",
)

L(
    OA13, 3, materials=MAT,
    use="Aprenderé a comparar valores comunitarios y espirituales de dos comunidades, sin decir que unos valen más. Sirve para reconocer semejanzas y diferencias entre los pueblos.",
    prior=["Sé reconocer valores en acciones.", "Sé comparar con criterios iguales."],
    explain=[
        "Comparar valores es ver qué acciones y valores aparecen en cada comunidad y en qué se parecen o se diferencian. Usamos criterios iguales, por ejemplo: qué se comparte, cómo se cuida lo común y cómo se agradece. Comparamos los testimonios de Ladera Verde y de Isla Niebla.",
        "En Ladera Verde se reparten las semillas cada siembra y se agradece el agua en silencio. En Isla Niebla se deja leña para quien la necesite y se pide permiso al bosque en silencio. Ambas comunidades muestran valores como compartir y respetar lo que cuidan, aunque lo hacen de formas distintas.",
        "Comparar no es dar puntajes ni decir qué comunidad es «más generosa». Tampoco se concluye que todos los pueblos tienen estos valores iguales. Solo describimos lo que dicen las fuentes y marcamos con claridad lo que es una idea propia.",
    ],
    vocab=[("comparar", "ver semejanzas y diferencias"), ("generoso", "que da con gusto lo que tiene"), ("puntaje", "número que ordena a alguien"), ("criterio", "punto igual para comparar"), ("semejanza", "algo parecido")],
    worked=[
        W("Comparar con criterios", "Criterio «qué se comparte». Ladera Verde: semillas. Isla Niebla: leña. ¿Qué semejanza hay?", ["En las dos se comparte algo necesario.", "Cambia qué se comparte.", "El valor de compartir aparece en ambas."], "En ambas se comparte algo necesario; cambian las cosas compartidas."),
        W("Evitar el puntaje", "Un niño dice: «Ladera Verde es más generosa porque comparte semillas». ¿Está bien?", ["Isla Niebla comparte leña.", "No hay forma de medir cuál es más generosa.", "No se ordenan."], "No: ambas comparten algo y no se ordenan."),
    ],
    mistakes=[
        M("Poner puntajes a los valores de las comunidades.", "Los valores no se miden con números.", "Describe semejanzas y diferencias."),
        M("Concluir que todos los pueblos tienen los mismos valores.", "Solo se compararon dos comunidades.", "Escribe «en estas dos comunidades»."),
    ],
    R=[
        ex("En Ladera Verde (inventada), ¿qué se reparte en cada siembra?", "Las semillas", "Doña Elena lo cuenta así."),
        ex("En Isla Niebla (inventada), ¿qué se deja para quien lo necesite? A) leña B) semillas", "A", "Don Camilo lo cuenta."),
        ex("En ambas comunidades se agradece o se pide permiso en silencio. ¿Es una semejanza? Responde Sí o No.", "Sí", "Aparece en las dos."),
    ],
    C=[
        ex("Verdadero o falso: comparar valores es decir cuál comunidad es mejor.", "Falso", "Comparar es describir semejanzas y diferencias."),
        ex("¿Qué es un criterio de comparación? A) un punto igual para las dos comunidades B) una opinión", "A", "Así se compara con justicia."),
        ex("Verdadero o falso: puedo concluir que todos los pueblos tienen estos valores a partir de dos comunidades.", "Falso", "Dos casos no representan a todos."),
    ],
    A=[
        ex("Criterio «cómo se agradece»: Ladera Verde, el agua en silencio; Isla Niebla, pedir permiso al bosque en silencio. ¿Qué semejanza hay? A) en ambas hay silencio como gesto de respeto B) en ambas hay música", "A", "El silencio aparece en las dos."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas comunidades comparten algo necesario b) una reparte semillas y la otra leña.", "a semejanza, b diferencia", "La primera es común; la segunda cambia."),
        ex("Un cuadro dice: «Ladera Verde, 8 puntos de generosidad; Isla Niebla, 6». ¿Qué falla tiene? A) pone puntaje a los valores B) usa números", "A", "Los valores no se miden con puntajes."),
    ],
    Z=[
        ex("Carolina dice: «Como las dos comunidades comparten, todas las comunidades indígenas comparten». ¿Qué error comete?", "Generaliza desde dos casos", "Dos casos no representan a todos."),
        ex("¿Por qué no se dice cuál comunidad es más generosa? A) porque no hay forma justa de medirlo B) porque no comparten", "A", "Los valores no se miden con puntajes."),
    ],
    D=[
        ex("Criterio «cómo se cuida lo común». Ladera Verde: se turnan para cuidar el corral. Isla Niebla: se limpia el sendero entre todos. ¿Qué afirmación es correcta? A) en ambas hay trabajo compartido para cuidar lo común B) solo una cuida lo común", "A", "Las dos muestran cuidado de lo común."),
        ex("Quieres comparar con los valores del pueblo que corresponde a tu escuela. ¿Qué necesitas? A) un testimonio del educador tradicional B) una suposición", "A", "La fuente es el educador o la comunidad."),
    ],
    context=[ex("Un periodista escolar pregunta qué comunidad tiene los valores más importantes. ¿Qué respondes? A) los valores no se ordenan y cada comunidad los vive a su manera B) la de Ladera Verde", "A", "No se jerarquiza.")],
    selfcheck=[
        ex("Escribe una semejanza entre los valores de Ladera Verde e Isla Niebla.", "En ambas se comparte algo necesario y se respeta con silencio", "Aparecen en los testimonios."),
        ex("Verdadero o falso: puedo ponerle puntaje a los valores.", "Falso", "No se miden."),
        ex("¿Qué necesitas para comparar con otro pueblo? A) su fuente B) una idea", "A", "Sin fuente no se compara."),
    ],
    task=T("Compara estos dos testimonios inventados. Pampa Larga (doña Marta): «Quien llega con sed toma agua primero y después agradecemos en silencio.» Río Hondo (don Aurelio): «Entre todos limpiamos la orilla del río cada año.» Usa dos criterios: qué se hace por los demás y qué se cuida. Escribe una semejanza, una diferencia, una frase que no jerarquice y una que diga qué no puedes concluir.",
           "Pampa Larga: dan agua primero a quien tiene sed; cuidan el agua y agradecen. Río Hondo: limpian la orilla entre todos; cuidan el río. Semejanza: ambas cuidan un lugar de agua (el pozo y la orilla del río). Diferencia: una atiende a quien llega y la otra trabaja en grupo. Ninguna es mejor. No puedo concluir que todos los pueblos cuiden el agua igual.",
           ["usa dos criterios iguales", "semejanza y diferencia", "no jerarquiza ni generaliza"], ["tabla de dos criterios", "tres frases"], ["poner puntajes", "generalizar"],
           "Pedir que muestre la frase de cada fuente."),
    reinforce="Marca con verde las semejanzas y con azul las diferencias en tu tabla.",
    extend="Escribe una pregunta para el educador tradicional sobre los valores de la comunidad de tu zona.",
)

L(
    OA13, 4, materials=MAT,
    use="Aprenderé a escribir una respuesta atribuida sobre el aporte de los valores de los pueblos indígenas a la sociedad chilena. Sirve para valorar lo que los pueblos entregan a todos, sin quitarles su voz.",
    prior=["Sé comparar valores sin jerarquizar.", "Sé atribuir cada dato a su fuente."],
    explain=[
        "Los pueblos indígenas han aportado a la sociedad chilena de muchas maneras. Pueden aportar valores (como el cuidado de la naturaleza o la ayuda mutua), saberes (como el cultivo o el tejido) y palabras que hoy usamos en español; cada pueblo cuenta cuáles son los suyos. Por ejemplo, palabras como papa, palta y cóndor vienen del quechua. Estos son datos generales y los especialistas pueden ampliarlos.",
        "Un aporte se explica con una estructura: cuál es el aporte, de qué comunidad o pueblo viene, qué fuente lo cuenta y cómo puede ayudar a la sociedad. Por ejemplo: «Según doña Elena, en Ladera Verde (inventada) comparten el agua entre familias; yo pienso que ese valor puede ayudar a cuidar el agua en mi barrio».",
        "Cuando hablamos de aportes no usamos a los pueblos como adornos ni decimos que «todos los indígenas» ofrecen lo mismo. Nombramos la fuente y cuidamos de no apropiarnos. Si queremos usar un valor en la escuela, lo hacemos con permiso y reconociendo de dónde viene.",
    ],
    vocab=[("aporte", "lo que un pueblo entrega a toda la sociedad"), ("sociedad chilena", "conjunto de las personas que viven en Chile"), ("préstamo lingüístico", "palabra de una lengua que otra lengua usa"), ("reconocer", "decir de dónde viene algo"), ("apropiarse", "usar algo ajeno como propio")],
    worked=[
        W("Escribir un aporte", "Testimonio inventado de doña Elena: «En Ladera Verde compartimos el agua entre las familias». Escribe el aporte con la estructura.", ["Aporte: compartir el agua.", "De dónde viene: Ladera Verde (inventada), según doña Elena.", "Cómo ayuda: puede ayudar a cuidar el agua en mi barrio (idea mía)."], "Según doña Elena, en Ladera Verde comparten el agua entre familias. Puedo pensar que ese valor ayuda a cuidar el agua en mi barrio."),
        W("Reconocer un préstamo", "La palabra «papa» que usamos en español viene del quechua. ¿Es un aporte de un pueblo?", ["Es una palabra que usamos hoy.", "Viene de una lengua indígena.", "Es un aporte lingüístico."], "Sí, es un aporte lingüístico del quechua."),
    ],
    mistakes=[
        M("Decir que «todos los indígenas» aportan lo mismo.", "Cada pueblo aporta de manera distinta.", "Nombra el pueblo o la comunidad y la fuente."),
        M("Usar un valor de una comunidad en la escuela sin reconocer de dónde viene.", "Es apropiarse.", "Nombra la fuente y pide permiso."),
    ],
    R=[
        ex("Según la clase, ¿de qué lengua vienen las palabras «papa», «palta» y «cóndor»? A) del quechua B) del inglés", "A", "Son préstamos del quechua al español."),
        ex("¿Qué es un aporte? A) lo que un pueblo entrega a toda la sociedad B) un regalo de cumpleaños", "A", "Es lo que comparte con todos."),
        ex("¿Qué debes decir al usar una idea de una comunidad? A) de dónde viene B) que es mía", "A", "Reconocer la fuente."),
    ],
    C=[
        ex("Verdadero o falso: el cuidado de la naturaleza es un aporte que se atribuye a una fuente concreta.", "Verdadero", "Se explica con la comunidad que lo cuenta."),
        ex("Verdadero o falso: puedo decir que todos los pueblos aportan exactamente lo mismo.", "Falso", "Cada pueblo aporta distinto."),
        ex("Verdadero o falso: las palabras de lenguas indígenas que usamos en español son un aporte.", "Verdadero", "Muestran la presencia de esas lenguas."),
    ],
    A=[
        ex("Ordena la estructura de un aporte: A) cómo ayuda B) cuál es el aporte C) de qué comunidad viene. ¿Cuál va primero?", "B", "Se empieza nombrando el aporte."),
        ex("Clasifica en VALOR o PALABRA: a) la ayuda mutua b) la palabra «palta».", "a valor, b palabra", "La primera guía la convivencia; la segunda es una palabra."),
        ex("Según doña Marta, en Pampa Larga se da agua primero a quien tiene sed. Completa con una idea propia bien marcada: «Puedo pensar que ese valor puede ayudar a…» A) cuidar y compartir el agua en mi barrio B) olvidar el agua", "A", "Es una aplicación razonable marcada como idea propia."),
    ],
    Z=[
        ex("Gonzalo dice: «Los pueblos indígenas solo aportan comida y bailes». ¿Qué error comete?", "Reduce los aportes a pocos aspectos", "Aportan también valores, saberes y lenguas."),
        ex("¿Por qué se reconoce de dónde viene un valor? A) para no apropiarse B) para ocupar espacio", "A", "Reconocer evita usar algo ajeno como propio."),
    ],
    D=[
        ex("Dos frases. 1) «Según don Aurelio, en Río Hondo limpian la orilla entre todos; puedo pensar que eso ayuda a cuidar nuestras playas». 2) «Los indígenas nos enseñaron todo». ¿Cuál es atribuida?", "La primera", "La segunda generaliza."),
        ex("Quieres que tu curso adopte el valor de ayudarse entre todos, que viste en un testimonio. ¿Qué haces? A) lo nombras con su fuente B) lo presentas como invento tuyo", "A", "Se reconoce la fuente."),
    ],
    context=[ex("Tu escuela quiere cuidar el agua del patio con turnos entre cursos. Alguien dice que se inspiraron en el testimonio de Pampa Larga. ¿Qué cartel es mejor? A) «Inspirado en un testimonio inventado de Pampa Larga» B) «Idea de la escuela»", "A", "Reconoce la fuente.")],
    selfcheck=[
        ex("Nombra la estructura de un aporte.", "Cuál es, de qué comunidad viene, qué fuente lo cuenta y cómo ayuda", "Está en la explicación."),
        ex("Verdadero o falso: debo reconocer de dónde viene un valor.", "Verdadero", "Así se evita apropiarse."),
        ex("¿Qué lengua indígena dio al español la palabra «cóndor»? Escribe una palabra.", "Quechua", "Es el dato general de la clase."),
    ],
    task=T("Usa este testimonio inventado de don Aurelio, de Río Hondo: «Entre todos limpiamos la orilla del río cada año; el río es de todos». Escribe un párrafo de aporte con la estructura: cuál es el aporte, de qué comunidad viene y quién lo cuenta, cómo puede ayudar a la sociedad chilena (con «yo pienso que») y un límite. Agrega una frase que reconozca que las palabras «papa» y «palta» vienen del quechua.",
           "Según don Aurelio, de Río Hondo (inventado), la comunidad limpia entre todos la orilla del río cada año. Yo pienso que ese valor puede ayudar a cuidar los ríos de mi comuna. No sé cómo se organizan los turnos. Además, palabras como papa y palta vienen del quechua.",
           ["incluye aporte, comunidad, fuente, idea y límite", "reconoce el préstamo lingüístico", "no generaliza"], ["párrafo de aporte"], ["decir que todos los pueblos aportan igual", "apropiarse"],
           "Pedir que señale la frase de la fuente y la marca de su idea."),
    reinforce="Escribe un aporte con la estructura usando el testimonio de doña Elena sobre las semillas.",
    extend="Escribe qué pregunta le harías al educador tradicional sobre los aportes del pueblo que corresponde a tu escuela.",
)
