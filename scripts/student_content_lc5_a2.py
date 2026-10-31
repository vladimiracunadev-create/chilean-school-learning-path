"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 10 (relatos fundacionales y origen del mundo) y OA 11 (personas portadoras de saberes ancestrales).

Todos los relatos, comunidades y personas son INVENTADOS por el autor del cuaderno (no son relatos de ningún
pueblo real ni de ninguna obra con derechos de autor) y se rotulan así. Los relatos reales los cuenta la
comunidad o el educador/a tradicional; aquí solo se enseña a leerlos con respeto.
"""
from __future__ import annotations

from student_content_lc5_a import FIN, FLV, FPL, FRH, L, M, MAT, T, W
from student_lessons import arith, ex

OA10, OA11 = "LC05 OA 10", "LC05 OA 11"

RLV = ("Relato inventado de Ladera Verde, contado por doña Elena: «Al comienzo, los cerros dormían bajo una niebla espesa. La Abuela Niebla sopló y se despertó la primera quebrada. "
       "Por la quebrada bajó el agua y donde llegó el agua nacieron las primeras semillas. Desde entonces arriba vive el viento, en medio están las terrazas y abajo corre el agua.»")
RIN = ("Relato inventado de Isla Niebla, contado por don Camilo: «Antes de la isla solo había mar. Un Pez Mayor subió a respirar y su lomo quedó sobre el agua: esa fue la isla. "
       "Del lomo nació el bosque y de las aletas, la caleta. Desde entonces el mar da y el bosque cuida.»")
RPL = ("Relato inventado de Pampa Larga, contado por doña Marta: «Al principio la llanura no tenía caminos. Una bandada de aves caminó de un lado a otro y donde pisaron quedaron las huellas que hoy son los caminos. "
       "Donde la bandada descansó, brotó el agua del pozo.»")
RCL = ("Relato inventado de Costa Lejana (una cultura inventada, no es un pueblo real): «Al comienzo había una oscuridad quieta. Una tejedora hizo una trama de hilos de luz "
       "y de la trama salieron el día y la noche. Desde entonces el día trabaja y la noche descansa.»")

# ============================================================ OA 10 · Relatos fundacionales y origen del mundo
L(
    OA10, 1, materials=MAT + " Los relatos son inventados: los relatos reales los cuenta la comunidad.",
    use="Aprenderé a situar un relato fundacional: de qué comunidad es, quién lo cuenta y con qué permiso. Sirve para estudiar cómo distintos pueblos entienden el origen del mundo sin mezclar sus relatos.",
    prior=["Sé situar una fuente con su ficha.", "Sé que la oralidad guarda la historia y los saberes de un pueblo."],
    explain=[
        "Un relato fundacional es una historia que cuenta cómo comenzó algo importante: el mundo, un lugar, un pueblo o la vida. También explica cómo se ordenó lo que existe, por ejemplo qué hay arriba, qué hay abajo y quién cuida cada cosa. Por eso se dice que el relato fundacional cuenta el origen y el ordenamiento del mundo.",
        "Los pueblos del mundo tienen sus propios relatos fundacionales, y cada uno refleja cómo ese pueblo entiende su territorio y su lugar en él. Una persona los cuenta de manera oral, y una misma historia puede tener versiones distintas según quién la cuente o dónde. Esas versiones se llaman variantes.",
        "Para estudiar un relato empezamos por situarlo: quién lo cuenta, de qué comunidad es, si dio permiso y qué parte no se cuenta. Los relatos de este cuaderno son inventados. Los relatos reales de un pueblo los cuenta su comunidad o su educador o educadora tradicional, y no se cambian ni se mezclan con otros.",
    ],
    vocab=[("relato fundacional", "historia que cuenta cómo comenzó y cómo se ordenó algo importante"), ("origen", "comienzo de algo"), ("ordenamiento", "manera en que se organiza lo que existe"), ("variante", "versión distinta de un mismo relato"), ("oral", "que se transmite hablando")],
    worked=[
        W("Situar un relato", RLV + " ¿Quién lo cuenta, de qué comunidad es y qué origen explica?", ["Lo cuenta doña Elena.", "Es de Ladera Verde.", "Explica el origen de la quebrada, el agua y las semillas."], "Lo cuenta doña Elena, de Ladera Verde, y explica cómo nacieron la quebrada, el agua y las semillas."),
        W("Origen y ordenamiento", "En el mismo relato, ¿qué dice del ordenamiento del mundo?", ["Busco la frase que dice «desde entonces».", "Dice que arriba vive el viento, en medio están las terrazas y abajo corre el agua.", "Esa es la forma de ordenar el territorio."], "Ordena el territorio: arriba el viento, en medio las terrazas, abajo el agua."),
    ],
    mistakes=[
        M("Pensar que todas las comunidades tienen el mismo relato de origen.", "Cada pueblo tiene los suyos y pueden tener variantes.", "Nombra siempre la comunidad y la fuente."),
        M("Mezclar partes de dos relatos en uno solo.", "Se pierde la voz de cada comunidad.", "Mantén cada relato separado y atribuido."),
    ],
    R=[
        ex("Relato inventado: «La Abuela Niebla sopló y se despertó la primera quebrada». ¿Qué despertó la Abuela Niebla?", "La primera quebrada", "El relato lo dice así."),
        ex("Un relato inventado de Isla Niebla dice: «Un Pez Mayor subió a respirar y su lomo quedó sobre el agua: esa fue la isla». ¿Qué origen explica? A) el origen de la isla B) el origen de un camino", "A", "El lomo del pez es la isla."),
        ex("¿Qué cuenta un relato fundacional? A) cómo comenzó y se ordenó algo importante B) la lista de compras", "A", "Cuenta el origen y el ordenamiento."),
    ],
    C=[
        ex("Verdadero o falso: un mismo relato oral puede tener variantes.", "Verdadero", "Cambia según quién lo cuente o dónde."),
        ex("¿Qué es el ordenamiento del mundo en un relato? A) cómo se organiza lo que existe B) el nombre del narrador", "A", "Dice qué hay arriba, abajo y quién cuida cada cosa."),
        ex("Verdadero o falso: todas las comunidades indígenas cuentan el mismo relato de origen.", "Falso", "Cada pueblo tiene los suyos."),
    ],
    A=[
        ex("Relato inventado: «Desde entonces arriba vive el viento, en medio están las terrazas y abajo corre el agua». ¿Qué está en el medio?", "Las terrazas", "El relato lo dice."),
        ex("Una ficha dice: «Relato de Pampa Larga. Fuente: doña Marta. Permiso: sí». ¿Quién cuenta el relato?", "Doña Marta", "Es la fuente."),
        ex("Clasifica en ORIGEN u ORDENAMIENTO: a) «brotó el agua del pozo» b) «el mar da y el bosque cuida».", "a origen, b ordenamiento", "La primera cuenta cómo nació algo; la segunda, cómo se ordena la vida."),
    ],
    Z=[
        ex("Daniel mezcla en su cartel el Pez Mayor de Isla Niebla con las aves de Pampa Larga en un solo relato. ¿Qué problema tiene?", "Mezcla relatos de comunidades distintas", "Cada relato pertenece a su comunidad."),
        ex("Un niño pregunta si el relato inventado de la Abuela Niebla es «verdadero o falso». ¿Qué es mejor hacer? A) entender qué dice sobre el origen y el ordenamiento B) decidir si es una mentira", "A", "Un relato fundacional se estudia por lo que explica, no por si coincide con otras ideas."),
    ],
    D=[
        ex("Dos versiones de un relato inventado: una dice que el Pez Mayor «subió a respirar» y otra que «subió a descansar». ¿Qué son? A) variantes B) errores", "A", "Una misma historia puede contarse un poco distinto."),
        ex("Quieres usar un relato de otro pueblo para tu trabajo, pero no tienes la ficha. ¿Qué haces? A) pido la fuente y el permiso B) lo uso igual", "A", "Sin fuente ni permiso no se usa un relato."),
    ],
    context=[ex("En tu curso una compañera cuenta un relato de su familia, pero no dice si puede compartirse. Antes de anotarlo, ¿qué haces? A) le pregunto si lo autoriza B) lo anoto y lo difundo", "A", "La autorización va primero.")],
    selfcheck=[
        ex("Explica con tus palabras qué es un relato fundacional.", "Una historia que cuenta cómo comenzó y se ordenó algo importante", "Es la definición de la clase."),
        ex("Verdadero o falso: los relatos de este cuaderno son inventados.", "Verdadero", "Se rotulan así para no confundirlos con relatos reales."),
        ex("¿Quién cuenta un relato real de un pueblo? A) su comunidad o el educador tradicional B) cualquiera", "A", "Ellos son la fuente."),
    ],
    task=T("Lee este relato inventado: «" + RPL.split("«")[1].rstrip("»") + "» Haz una ficha con estos campos: comunidad, fuente, qué origen explica, cómo ordena el territorio y una variante posible (por ejemplo, cambiar un detalle sin cambiar la idea). Escribe al final qué parte no se cuenta o no sabes.",
           "Comunidad: Pampa Larga. Fuente: doña Marta. Origen: los caminos y el pozo. Ordenamiento: los caminos son las huellas y el pozo está donde las aves descansaron. Variante posible: que las aves vuelen en lugar de caminar. No sé cómo se llamaban las aves.",
           ["completa los campos con datos del relato", "propone una variante sin cambiar la idea", "señala lo que no sabe"], ["ficha completa"], ["mezclar con otros relatos", "agregar partes que el relato no tiene"],
           "Pedir que indique la frase del relato de cada dato."),
    reinforce="Subraya en el relato de Ladera Verde la frase que explica el origen y con otro color la que ordena.",
    extend="Escribe una pregunta que le harías al educador tradicional sobre un relato de origen de tu zona.",
)

L(
    OA10, 2, materials=MAT,
    use="Aprenderé a leer un relato fundacional con límites: separar lo que cuenta, lo que interpreto y lo que no se cuenta. Sirve para comprender cómo se entiende el origen del mundo sin deformar el relato.",
    prior=["Sé situar un relato con su ficha.", "Sé qué son origen y ordenamiento."],
    explain=[
        "Al leer un relato fundacional hacemos preguntas simples. ¿Qué había antes? ¿Quién actúa? ¿Qué cambia? ¿Cómo se ordena lo que nace? Las respuestas están en el propio relato y se anotan con sus palabras. Eso nos permite entender la forma en que ese pueblo explica el origen.",
        "Los relatos se entienden desde su propia manera de explicar el mundo. No los leemos como si fueran un informe científico ni los juzgamos como «verdaderos o falsos». Los leemos para comprender qué dicen del territorio, de las relaciones entre los seres y del cuidado del mundo.",
        "Si el relato no explica algo, escribimos «el relato no lo dice». No agregamos personajes ni finales. También respetamos las partes que la comunidad no cuenta. Mis interpretaciones se marcan como tales, con «yo pienso que», para no mezclarlas con el relato.",
    ],
    vocab=[("personaje", "ser que actúa en un relato"), ("estado inicial", "cómo era el mundo al comienzo del relato"), ("transformación", "cambio que ocurre en el relato"), ("interpretación", "idea propia sobre lo que dice un relato"), ("límite", "lo que el relato no cuenta o no sé")],
    worked=[
        W("Responder con el relato", RIN + " ¿Qué había antes de la isla y quién actúa?", ["Busco «antes».", "Antes solo había mar.", "El que actúa es el Pez Mayor."], "Antes había solo mar y actúa el Pez Mayor."),
        W("Separar interpretación", "Un niño dice: «El Pez Mayor es un protector de la isla». ¿Lo dice el relato?", ["El relato dice que el pez subió a respirar y su lomo fue la isla.", "No dice que sea protector.", "Es una interpretación."], "No: es una interpretación del niño; debe marcarse con «yo pienso que»."),
    ],
    mistakes=[
        M("Decir que un relato de origen es falso porque no coincide con una explicación científica.", "El relato se lee desde su propia forma de explicar el mundo.", "Pregunta qué dice sobre el territorio y las relaciones."),
        M("Agregar un personaje o un final que el relato no tiene.", "Cambia el relato de la comunidad.", "Escribe «el relato no lo dice»."),
    ],
    R=[
        ex("Relato inventado: «Antes de la isla solo había mar». ¿Qué había al comienzo?", "Solo mar", "El relato lo dice."),
        ex("Relato inventado de Costa Lejana: «Una tejedora hizo una trama de hilos de luz». ¿Quién actúa?", "Una tejedora", "Es el personaje que hace la trama."),
        ex("Relato: «Del lomo nació el bosque». ¿De dónde nació el bosque?", "Del lomo del Pez Mayor", "El relato lo dice así."),
    ],
    C=[
        ex("Verdadero o falso: un relato fundacional se lee para saber cómo ese pueblo explica el origen, no para decir si es verdadero o falso.", "Verdadero", "Se comprende desde su propia mirada."),
        ex("¿Qué es una transformación en un relato? A) un cambio que ocurre en el relato B) el título", "A", "Es lo que cambia, como que nazca un lugar."),
        ex("Verdadero o falso: puedo agregar un final al relato si me gusta más.", "Falso", "Se cambia la historia de la comunidad."),
    ],
    A=[
        ex("Relato inventado: «Al comienzo había una oscuridad quieta. Una tejedora hizo una trama de hilos de luz y de ella salieron el día y la noche». Clasifica en ESTADO INICIAL o TRANSFORMACIÓN: a) había una oscuridad quieta b) salieron el día y la noche.", "a estado inicial, b transformación", "La primera describe el comienzo; la segunda, el cambio."),
        ex("Relato inventado de Pampa Larga: «Donde la bandada descansó, brotó el agua del pozo». ¿Dónde brotó el agua?", "Donde la bandada descansó", "El relato lo dice."),
        ex("Un niño escribe: «La Abuela Niebla tiene mucha edad». El relato inventado de Ladera Verde solo dice que sopló y despertó la quebrada. ¿Qué es esa frase? A) una interpretación B) un dato del relato", "A", "El relato no habla de su edad."),
    ],
    Z=[
        ex("Sofía dice: «El relato de Costa Lejana es falso porque la luz no sale de hilos». ¿Qué error comete?", "Lo juzga como informe científico", "El relato se lee desde su forma de explicar el mundo."),
        ex("¿Por qué conviene escribir «el relato no lo dice»? A) para no agregar cosas que no están B) para llenar espacio", "A", "Evita inventar partes del relato."),
    ],
    D=[
        ex("Relato de Ladera Verde: «Por la quebrada bajó el agua y donde llegó el agua nacieron las primeras semillas». Dos frases: 1) «Las semillas nacen donde llega el agua» 2) «Las semillas nacen de noche». ¿Cuál se queda en el relato?", "La primera", "La segunda no está."),
        ex("La comunidad no cuenta la segunda parte de su relato. ¿Qué escribes en tu trabajo? A) esa parte no se cuenta B) invento una segunda parte", "A", "Se respeta lo reservado."),
    ],
    context=[ex("Para una obra de títeres, un grupo quiere cambiar el final del relato de Isla Niebla porque le parece corto. ¿Qué debe hacer? A) pedir permiso al narrador o contar el relato sin cambios B) inventar un final", "A", "No se cambia un relato de una comunidad.")],
    selfcheck=[
        ex("Nombra dos preguntas que ayudan a leer un relato fundacional.", "Dos entre: qué había antes, quién actúa, qué cambia, cómo se ordena", "Están en la explicación."),
        ex("Verdadero o falso: mis interpretaciones se marcan como tales.", "Verdadero", "Así no se mezclan con el relato."),
        ex("¿Qué haces con lo que el relato no explica? A) escribo que no lo dice B) lo invento", "A", "Es la forma honesta."),
    ],
    task=T("Lee el relato inventado de Costa Lejana: «Al comienzo había una oscuridad quieta. Una tejedora hizo una trama de hilos de luz y de la trama salieron el día y la noche. Desde entonces el día trabaja y la noche descansa.» Responde por escrito: ¿qué había antes?, ¿quién actúa?, ¿qué cambia?, ¿cómo queda ordenado el mundo? Agrega una interpretación con «yo pienso que» y una cosa que el relato no dice.",
           "Antes había una oscuridad quieta. Actúa una tejedora. Cambia: aparecen el día y la noche. Ordenamiento: el día trabaja y la noche descansa. Yo pienso que el relato explica el paso del tiempo. El relato no dice cómo se llamaba la tejedora.",
           ["responde las cuatro preguntas con el relato", "marca la interpretación", "señala un vacío"], ["cuatro respuestas", "interpretación", "vacío"], ["agregar personajes", "juzgar si es verdadero o falso"],
           "Pedir que señale en el texto cada respuesta."),
    reinforce="Marca en el relato de Costa Lejana el estado inicial con un color y la transformación con otro.",
    extend="Explica por qué no conviene decir que un relato de origen es «falso».",
)

L(
    OA10, 3, materials=MAT,
    use="Aprenderé a relacionar un relato fundacional con el territorio, la identidad y el ordenamiento de la vida de una comunidad. Sirve para ver que el origen del mundo y la vida de hoy se conectan.",
    prior=["Sé leer un relato con límites.", "Sé que el territorio se relaciona con la visión de mundo."],
    explain=[
        "Un relato fundacional se conecta con la vida de la comunidad que lo cuenta. Por ejemplo, el relato de Ladera Verde ordena el territorio en arriba (viento), en medio (terrazas) y abajo (agua). Si doña Elena cuenta, en su testimonio, que las terrazas se cuidan con el agua de la quebrada, podemos relacionar ese testimonio con el orden del relato: el agua baja y llega a las terrazas.",
        "Para encontrar relaciones hacemos tres preguntas. Primero, ¿qué lugares del territorio aparecen en el relato? Segundo, ¿qué dice el relato sobre cómo se ordenan o se cuidan esos lugares? Tercero, ¿qué relación hay entre eso y lo que la comunidad hace hoy, según su testimonio? Las respuestas se anotan con la fuente.",
        "Es importante no inventar la relación. Si el testimonio no la menciona, escribimos «puedo pensar que…», no «la comunidad dice que…». También recordamos que el relato pertenece a su comunidad y no se usa para hablar de otras.",
    ],
    vocab=[("relación", "unión entre dos datos de una fuente"), ("territorio", "lugar donde vive la comunidad, con sus relaciones"), ("cuidado", "acción de proteger algo importante"), ("ordenar", "organizar lo que existe"), ("testimonio", "lo que una persona cuenta de su vida o saber")],
    worked=[
        W("Relacionar relato y territorio", RLV + " Testimonio de doña Elena: «Cuidamos las terrazas con el agua de la quebrada». ¿Qué relación hay?", ["En el relato, el agua nace de la quebrada y llega a donde nacen las semillas.", "En el testimonio, la quebrada riega las terrazas.", "Ambos unen quebrada, agua y terrazas."], "El relato y el testimonio unen la quebrada, el agua y las terrazas."),
        W("No inventar la relación", "Un niño dice: «Por el relato, la comunidad pide permiso a la niebla para sembrar». ¿Está en las fuentes?", ["El relato menciona la niebla que sopló.", "Ninguna fuente habla de pedir permiso a la niebla.", "Esa relación es inventada."], "No: esa relación no está en las fuentes."),
    ],
    mistakes=[
        M("Decir que el relato demuestra algo que la comunidad no dijo.", "La relación sería inventada.", "Escribe «puedo pensar que…» si es mi idea."),
        M("Usar el relato de una comunidad para explicar a otra.", "Cada relato pertenece a su comunidad.", "Relaciona cada relato con su propio territorio."),
    ],
    R=[
        ex("Relato: «Arriba vive el viento, en medio están las terrazas y abajo corre el agua». ¿Qué corre abajo?", "El agua", "El relato lo dice."),
        ex("Testimonio inventado de don Camilo: «Del bosque sacamos leña y en la caleta pescamos». ¿Qué se saca en la caleta? A) pescado B) leña", "A", "El testimonio lo dice."),
        ex("Relato de Pampa Larga: «Donde la bandada descansó, brotó el agua del pozo». ¿Qué lugar de la comunidad aparece?", "El pozo", "Se menciona en el relato."),
    ],
    C=[
        ex("Verdadero o falso: un relato fundacional puede relacionarse con los lugares que la comunidad usa hoy.", "Verdadero", "El relato nombra lugares del territorio."),
        ex("¿Qué haces si una relación es solo tuya? A) escribo «puedo pensar que…» B) digo que la comunidad lo dice", "A", "Así se marca como idea propia."),
        ex("Verdadero o falso: puedo usar el relato de Ladera Verde para explicar cómo piensa otro pueblo.", "Falso", "Cada relato pertenece a su comunidad."),
    ],
    A=[
        ex("Relato de Isla Niebla: «Del lomo nació el bosque y de las aletas, la caleta». Testimonio de don Camilo: «En la caleta guardamos los botes». ¿Qué lugar une el relato y el testimonio?", "La caleta", "Aparece en ambos."),
        ex("Une: 1) «arriba vive el viento» 2) «abajo corre el agua» con a) lugar alto b) lugar bajo del territorio de Ladera Verde.", "1-a, 2-b", "Arriba es lo alto y abajo es lo bajo."),
        ex("Un testimonio de don Aurelio, de Río Hondo (inventado), dice: «El río nos da agua y camino». Completa la relación: el río es a la vez fuente de agua y…", "Camino", "El testimonio lo dice."),
    ],
    Z=[
        ex("Emilia escribe que, como el relato habla de aves, la comunidad de Pampa Larga no puede cazar aves. ¿Qué error comete?", "Inventa una relación que las fuentes no dicen", "Ninguna fuente habla de cazar aves."),
        ex("¿Por qué la relación entre relato y territorio se escribe con la fuente? A) para saber qué dice la comunidad y qué pienso yo B) para alargar el trabajo", "A", "La fuente distingue mi idea del dato."),
    ],
    D=[
        ex("Relato de Costa Lejana (inventado): «El día trabaja y la noche descansa». Testimonio: «En nuestra costa trabajamos de día y descansamos de noche». ¿Qué relación hay? A) el relato y el testimonio ordenan el tiempo igual B) no hay relación", "A", "Ambos dicen que el día es para trabajar y la noche para descansar."),
        ex("Tienes el relato de Pampa Larga pero ningún testimonio sobre el uso del pozo. ¿Qué escribes sobre la relación con la vida de hoy? A) no puedo afirmar la relación sin testimonio B) todos usan el pozo", "A", "Sin fuente no se afirma."),
    ],
    context=[ex("Un grupo prepara un panel sobre Ladera Verde. Alguien propone decir que la comunidad «adora» a la Abuela Niebla. ¿Qué respondes? A) el relato no dice eso B) sí, es evidente", "A", "No se atribuyen ritos que la fuente no dice.")],
    selfcheck=[
        ex("Nombra una pregunta para encontrar relaciones en un relato.", "Qué lugares aparecen, cómo se ordenan o cómo se relacionan con lo de hoy", "Están en la explicación."),
        ex("Verdadero o falso: si no hay testimonio, no puedo afirmar una relación con la vida de hoy.", "Verdadero", "Se necesita fuente."),
        ex("¿Cómo marcas una relación que es tu idea? Escribe la frase de inicio.", "Puedo pensar que", "Así no se atribuye a la comunidad."),
    ],
    task=T("Lee el relato inventado de Isla Niebla: «Antes de la isla solo había mar. Un Pez Mayor subió a respirar y su lomo quedó sobre el agua: esa fue la isla. Del lomo nació el bosque y de las aletas, la caleta. Desde entonces el mar da y el bosque cuida.» y el testimonio de don Camilo: «Del bosque sacamos leña seca y en la caleta guardamos los botes.» Haz una tabla con tres columnas: lugar, qué dice el relato y qué dice el testimonio. Después escribe una relación atribuida y una idea tuya.",
           "Bosque: el relato dice que cuida; el testimonio, que se saca leña seca. Caleta: el relato dice que nació de las aletas; el testimonio, que se guardan los botes. Relación: según el relato y don Camilo, el bosque y la caleta son importantes para la vida. Puedo pensar que la comunidad cuida el bosque porque lo usa.",
           ["completa la tabla con datos de las dos fuentes", "escribe una relación atribuida", "marca su idea"], ["tabla de tres columnas", "relación e idea"], ["inventar ritos", "mezclar relatos"],
           "Pedir que señale la línea de cada fuente."),
    reinforce="Une con flechas, en un dibujo simple, los lugares del relato con los lugares del testimonio.",
    extend="Escribe una relación entre el relato de Pampa Larga y un uso del camino que te imagines, marcándola como tu idea.",
)

L(
    OA10, 4, materials=MAT,
    use="Aprenderé a construir un análisis atribuido de un relato fundacional: qué cuenta, qué entiendo, qué no sé y qué consultaré. Sirve para analizar relatos de distintos pueblos con respeto.",
    prior=["Sé leer un relato con límites.", "Sé relacionar relato y territorio."],
    explain=[
        "Un análisis de un relato fundacional tiene cuatro partes. Primero, la ficha: quién lo cuenta, de qué comunidad y con qué permiso. Segundo, qué dice el relato sobre el origen y el ordenamiento del mundo. Tercero, mi interpretación, que explica qué creo que significa y por qué. Cuarto, los límites y una pregunta para el educador o educadora tradicional.",
        "Cada parte lleva su marca. Los datos del relato se escriben con «según el relato…». Mi interpretación se escribe con «yo pienso que…» y se apoya en una frase del relato. Los límites se escriben con «no sé…» o «el relato no lo dice».",
        "El análisis no compara con otros pueblos todavía y no juzga el relato. Tampoco lo vuelve a contar con mis palabras como si fuera mío. Si cito una frase, la pongo entre comillas y digo quién la contó. Al final, lo muestro a la comunidad o al educador para que lo revise.",
    ],
    vocab=[("análisis", "estudio de las partes de un relato y de lo que explican"), ("cita", "frase del relato escrita igual, entre comillas"), ("ficha", "datos de quién cuenta y con qué permiso"), ("apoyar", "mostrar con una frase por qué pienso algo"), ("revisión", "lectura del trabajo por la comunidad o el educador")],
    worked=[
        W("Escribir un análisis", RPL + " Escribe un análisis con las partes de la clase.", ["Ficha: doña Marta, Pampa Larga.", "Según el relato, los caminos son las huellas de las aves y el pozo está donde descansaron.", "Yo pienso que el relato explica por qué los caminos llevan al agua."], "Ficha: doña Marta, de Pampa Larga. Según el relato, los caminos son las huellas de las aves y el pozo brotó donde descansaron. Yo pienso que el relato explica por qué los caminos llevan al agua. No sé cómo se cuida el pozo."),
        W("Apoyar con una frase", "Un niño escribe: «Yo pienso que el pozo es importante». ¿Cómo lo apoya con el relato?", ["Busco una frase del relato.", "«Donde la bandada descansó, brotó el agua del pozo».", "La uso como cita."], "Lo apoya con la cita: «Donde la bandada descansó, brotó el agua del pozo»."),
    ],
    mistakes=[
        M("Escribir una interpretación sin apoyarla en una frase del relato.", "No se ve de dónde sale la idea.", "Agrega una cita corta del relato."),
        M("Volver a contar el relato con mis palabras como si fuera mío.", "Se pierde la voz de la comunidad.", "Cita y atribuye."),
    ],
    R=[
        ex("¿Cuántas partes tiene el análisis de esta clase? Escribe el número.", "4", "Ficha, qué dice, interpretación y límites con pregunta."),
        ex("¿Con qué frase empieza el dato del relato? A) «según el relato…» B) «yo pienso que…»", "A", "La segunda es para interpretar."),
        ex("Verdadero o falso: una cita se escribe entre comillas.", "Verdadero", "Las comillas muestran que es el texto original."),
    ],
    C=[
        ex("¿Para qué sirve apoyar mi interpretación en una frase? A) para mostrar de dónde sale mi idea B) para alargar el texto", "A", "La frase muestra la base de la interpretación."),
        ex("Verdadero o falso: puedo contar el relato de otra comunidad como si fuera mío.", "Falso", "Se pierde la voz de la comunidad."),
        ex("Verdadero o falso: el análisis termina con una pregunta para el educador tradicional.", "Verdadero", "Es la forma de consultar lo que falta."),
    ],
    A=[
        ex("Relato de Costa Lejana: «El día trabaja y la noche descansa». Clasifica en CITA o INTERPRETACIÓN: a) «El día trabaja y la noche descansa» b) yo pienso que el relato ordena el tiempo.", "a cita, b interpretación", "La primera es texto original; la segunda es idea de quien lee."),
        ex("Completa la interpretación con una frase del relato de Ladera Verde: «Yo pienso que las semillas dependen del agua, porque el relato dice: …»", "Donde llegó el agua nacieron las primeras semillas", "Es la frase que apoya la idea."),
        ex("Un análisis tiene ficha, qué dice el relato e interpretación, pero ningún límite. ¿Qué le falta? A) los límites y una pregunta B) más adornos", "A", "Sin límites no se ve hasta dónde llega lo afirmado."),
    ],
    Z=[
        ex("Pablo escribe: «Según el relato de Isla Niebla, el Pez Mayor era bueno». ¿Qué problema tiene?", "El relato no dice que fuera bueno", "Atribuye algo que el relato no dice."),
        ex("¿Por qué no se compara todavía con otros pueblos en este análisis? A) porque primero se comprende bien un relato B) porque está prohibido pensar", "A", "Comparar viene después de comprender cada relato."),
    ],
    D=[
        ex("Dos análisis del relato de Pampa Larga. A: «Según el relato, el pozo brotó donde descansó la bandada; no sé cómo se cuida». B: «Los pueblos de la llanura adoran a las aves». ¿Cuál es respetuoso?", "A", "B inventa un rito."),
        ex("Tu análisis usa una frase tuya entre comillas, como si fuera del relato. ¿Qué corriges? A) quito las comillas o uso la frase original B) la dejo", "A", "Las comillas son solo para frases originales."),
    ],
    context=[ex("Te piden un análisis para la revista de la escuela. ¿Qué incluyes al final? A) los límites y una pregunta B) solo la cita", "A", "Son parte del análisis.")],
    selfcheck=[
        ex("Nombra las cuatro partes de un análisis atribuido.", "Ficha, qué dice el relato, interpretación y límites con pregunta", "Están en la explicación."),
        ex("Verdadero o falso: mi interpretación debe apoyarse en una frase del relato.", "Verdadero", "Muestra de dónde sale mi idea."),
        ex("¿Qué haces al terminar? A) mostrarlo a la comunidad o al educador B) archivarlo", "A", "Es la revisión."),
    ],
    task=T("Lee el relato inventado de Ladera Verde: «Al comienzo, los cerros dormían bajo una niebla espesa. La Abuela Niebla sopló y se despertó la primera quebrada. Por la quebrada bajó el agua y donde llegó el agua nacieron las primeras semillas.» Escribe un análisis de cuatro partes: ficha, qué dice el relato, tu interpretación apoyada en una cita y los límites con una pregunta para el educador tradicional.",
           "Ficha: relato de doña Elena, de Ladera Verde. Según el relato, la Abuela Niebla sopló, se despertó la quebrada, bajó el agua y nacieron las semillas. Yo pienso que el relato muestra que las semillas dependen del agua, porque dice: «donde llegó el agua nacieron las primeras semillas». No sé quién es la Abuela Niebla. Pregunta: ¿qué otros relatos de origen conoce nuestra comunidad?",
           ["escribe las cuatro partes", "apoya su interpretación en una cita", "incluye límites y pregunta"], ["análisis de cuatro partes"], ["interpretar sin apoyo", "inventar partes del relato"],
           "Pedir que señale la cita que apoya su interpretación."),
    reinforce="Numera las partes de tu análisis con 1, 2, 3 y 4.",
    extend="Reescribe tu interpretación con otra cita del relato.",
)

L(
    OA10, 5, materials=MAT,
    use="Aprenderé a contrastar relatos fundacionales de distintos pueblos y de otras culturas, sin decir que uno es más importante, más verdadero o más antiguo. Sirve para valorar las distintas formas de comprender el origen del mundo.",
    prior=["Sé analizar un relato con fuente y límites.", "Sé comparar sin jerarquizar."],
    explain=[
        "Contrastar relatos es ver en qué se parecen y en qué se diferencian. Para hacerlo bien usamos los mismos criterios en todos. Tres criterios útiles son: qué había al comienzo, quién o qué actúa y cómo queda ordenado el mundo. Con ellos comparamos los relatos de Ladera Verde, Isla Niebla, Pampa Larga y Costa Lejana, que son inventados.",
        "Por ejemplo, en el relato de Ladera Verde actúa una Abuela Niebla que sopla; en el de Isla Niebla, un Pez Mayor que sube a respirar; en el de Pampa Larga, una bandada de aves; en el de Costa Lejana, una tejedora. Los personajes son distintos, pero en todos algo actúa y de esa acción nace una parte del mundo: eso se parece.",
        "Contrastar no es decir cuál relato es mejor, más verdadero, más antiguo o más completo. Los relatos de otras culturas significativas para nuestro contexto, como las de familias de nuestro curso que lo autoricen, se tratan con la misma consideración. Las conclusiones valen solo para los relatos que leímos.",
    ],
    vocab=[("contrastar", "ver semejanzas y diferencias entre dos o más cosas"), ("criterio", "punto igual para todos los relatos que se comparan"), ("jerarquizar", "decir que algo es mejor, más verdadero o más antiguo"), ("cultura significativa", "cultura importante para el contexto de quien estudia"), ("conclusión", "idea final que se apoya en lo leído")],
    worked=[
        W("Contraste con un criterio", "Criterio: «qué actúa». Ladera Verde: la Abuela Niebla sopla. Isla Niebla: el Pez Mayor sube a respirar. Pampa Larga: una bandada de aves camina. Costa Lejana: una tejedora hace una trama. ¿Qué semejanza hay?", ["En los cuatro relatos hay alguien que actúa.", "Esa acción origina una parte del mundo.", "Lo que cambia es quién actúa."], "En los cuatro, una acción origina una parte del mundo; cambian los personajes."),
        W("Evitar la jerarquía", "Un niño dice: «El relato de Costa Lejana es mejor porque trae luz». ¿Qué corriges?", ["La luz es el tema de ese relato.", "Los otros relatos tratan otros temas.", "No se ordenan por mejores."], "Corrijo: cada relato explica un origen distinto y no se ordenan."),
    ],
    mistakes=[
        M("Decir que un relato es más verdadero o más antiguo que otro.", "Esos datos no están en las fuentes y jerarquizan.", "Compara con criterios iguales."),
        M("Dejar fuera el relato de otra cultura por ser de afuera.", "El OA pide mirar también otras culturas significativas.", "Inclúyelo con su fuente y su permiso."),
    ],
    R=[
        ex("Relato de Pampa Larga: «Una bandada de aves caminó de un lado a otro». ¿Quién actúa en ese relato?", "Una bandada de aves", "El relato lo dice."),
        ex("Relato de Costa Lejana: «Una tejedora hizo una trama de hilos de luz». ¿Qué hace la tejedora?", "Hace una trama de hilos de luz", "El relato lo dice."),
        ex("¿Qué es contrastar? A) ver semejanzas y diferencias B) decir cuál es mejor", "A", "No se ordena."),
    ],
    C=[
        ex("Verdadero o falso: contrastar relatos es decir cuál es el más verdadero.", "Falso", "Contrastar es comparar sin ordenar."),
        ex("¿Qué es un criterio de contraste? A) un punto igual para todos los relatos B) una opinión", "A", "Así la comparación es justa."),
        ex("Verdadero o falso: las conclusiones valen solo para los relatos que leímos.", "Verdadero", "No se generaliza a todos los pueblos."),
    ],
    A=[
        ex("Criterio: «qué había al comienzo». Isla Niebla: solo mar. Costa Lejana: una oscuridad quieta. ¿Qué semejanza hay? A) al comienzo no había un mundo ordenado B) al comienzo había ciudades", "A", "En ambos relatos todo parte de un estado sin forma."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en los dos algo actúa y origina una parte del mundo b) uno cuenta un pez y otro una tejedora.", "a semejanza, b diferencia", "La primera es común; la segunda cambia."),
        ex("Criterio: «cómo queda ordenado el mundo». Ladera Verde: arriba el viento, en medio las terrazas, abajo el agua. Isla Niebla: el mar da y el bosque cuida. ¿Cuál ordena por alturas? A) Ladera Verde B) Isla Niebla", "A", "Menciona arriba, en medio y abajo."),
    ],
    Z=[
        ex("Marcos dice: «El relato de Pampa Larga es menos importante porque es más corto». ¿Qué error comete?", "Jerarquiza por el largo", "El largo no mide el valor de un relato."),
        ex("Valentina concluye que todos los relatos indígenas hablan de animales. ¿Por qué no es válido? A) solo leyó cuatro relatos inventados B) porque no hay animales en ninguno", "A", "Cuatro relatos no representan a todos los pueblos."),
    ],
    D=[
        ex("Cuadro con el criterio «qué actúa»: niebla, pez, aves, tejedora. Una afirmación dice: «En los cuatro relatos algo actúa». ¿Es correcta? Responde Sí o No.", "Sí", "En cada relato hay un personaje que actúa."),
        ex("Tu curso quiere incluir el relato de origen de una familia del curso, que autorizó contarlo. ¿Qué haces? A) lo trato con la misma consideración que los demás B) lo comparo para ver si es mejor", "A", "No se jerarquiza."),
    ],
    context=[ex("En una exposición, alguien pregunta cuál de los cuatro relatos es el más antiguo. ¿Qué respondes? A) las fuentes no lo dicen y no se ordenan B) el de Ladera Verde", "A", "No hay datos de antigüedad y no se jerarquiza.")],
    selfcheck=[
        ex("Nombra dos criterios para contrastar relatos de origen.", "Dos entre: qué había al comienzo, qué actúa, cómo queda ordenado", "Están en la explicación."),
        ex("Verdadero o falso: puedo decir que un relato es mejor porque me gusta más.", "Falso", "Eso es jerarquizar."),
        ex("¿Qué haces con el relato de otra cultura? A) lo incluyo con su fuente B) lo dejo fuera", "A", "El OA lo pide."),
    ],
    task=T("Compara dos relatos inventados. Isla Niebla: «Antes de la isla solo había mar. Un Pez Mayor subió a respirar y su lomo quedó sobre el agua: esa fue la isla.» Costa Lejana: «Al comienzo había una oscuridad quieta. Una tejedora hizo una trama de hilos de luz y salieron el día y la noche.» Usa tres criterios: qué había al comienzo, qué actúa y qué nace. Escribe una semejanza, una diferencia y una frase que diga qué no puedes concluir.",
           "Isla Niebla: mar, el pez, nace la isla. Costa Lejana: oscuridad, la tejedora, nacen el día y la noche. Semejanza: al comienzo no había un mundo ordenado y alguien actúa. Diferencia: un pez y una tejedora. No puedo concluir que todos los pueblos cuenten el origen de esta manera.",
           ["usa tres criterios iguales", "escribe semejanza y diferencia", "no jerarquiza ni generaliza"], ["tabla con tres criterios", "tres frases"], ["decir cuál es mejor", "generalizar"],
           "Pedir que indique en cada relato la frase de cada criterio."),
    reinforce="Pinta de verde las semejanzas y de azul las diferencias en tu tabla.",
    extend="Agrega una tercera columna con el relato de Pampa Larga y revisa si tu semejanza sigue valiendo.",
)

L(
    OA10, 6, materials=MAT,
    use="Aprenderé a comunicar un análisis de relatos fundacionales y a revisarlo con la validación de la comunidad o del educador tradicional. Sirve para presentar un trabajo respetuoso y corregir errores.",
    prior=["Sé analizar y contrastar relatos con fuente y límites.", "Sé devolver el trabajo a la comunidad."],
    explain=[
        "Comunicar es presentar lo aprendido a otras personas. Una buena presentación sobre relatos de origen dice de quién es cada relato, qué cuenta, qué interpreto y qué no sé. Además, deja claro que los relatos de este cuaderno son inventados y que los reales los cuenta la comunidad.",
        "Revisar con validación pertinente significa pedir a la comunidad o al educador o educadora tradicional que lea el trabajo. Ellos pueden decir si algo está mal, si falta permiso o si hay una parte que no debe compartirse. Si algo se corrige, se cambia sin discutir y se agradece.",
        "Una lista de revisión ayuda a encontrar errores antes de presentar: ¿cada relato tiene su fuente y su comunidad?, ¿mis ideas están marcadas?, ¿hay límites?, ¿no jerarquicé?, ¿no inventé nada?, ¿pedí revisión? Si falta algo, lo arreglo antes de mostrar el trabajo.",
    ],
    vocab=[("validación", "revisión de un trabajo por quien conoce la cultura"), ("lista de revisión", "preguntas que ayudan a detectar errores"), ("presentar", "mostrar el trabajo a otras personas"), ("corregir", "cambiar lo que estaba mal"), ("devolución", "mostrar a la comunidad lo escrito para que lo revise")],
    worked=[
        W("Usar la lista de revisión", "Un borrador dice: «El relato de la Abuela Niebla es el mejor de todos». Revisa con la lista.", ["¿Hay fuente? No se nombra.", "¿Jerarquiza? Sí, dice «el mejor».", "Debo corregir ambas cosas."], "Corrijo: agrego la fuente (doña Elena, de Ladera Verde) y quito «el mejor de todos»."),
        W("Aceptar una corrección", "El educador tradicional te dice que una parte de tu trabajo no debe mostrarse. ¿Qué haces?", ["Escucho sin discutir.", "Quito esa parte.", "Agradezco la revisión."], "Quito esa parte y agradezco."),
    ],
    mistakes=[
        M("Presentar el trabajo sin pedir revisión.", "Puede tener errores o partes que no deben compartirse.", "Pide validación antes de presentar."),
        M("Discutir con quien corrige el trabajo.", "Esa persona conoce su cultura.", "Escucha, corrige y agradece."),
    ],
    R=[
        ex("¿Qué hace la comunidad o el educador tradicional con tu trabajo? A) lo revisa y corrige B) lo califica con nota", "A", "Valida y corrige lo que haga falta."),
        ex("¿Qué debe decir tu presentación sobre los relatos de este cuaderno? A) que son inventados B) que son reales", "A", "Se rotulan así."),
        ex("¿Quién cuenta los relatos reales de un pueblo? A) su comunidad B) cualquiera", "A", "Ellos son la fuente."),
    ],
    C=[
        ex("Verdadero o falso: una lista de revisión ayuda a encontrar errores antes de presentar.", "Verdadero", "Sirve para detectar fallas."),
        ex("Verdadero o falso: si el educador tradicional corrige algo, debo discutirlo hasta convencerlo.", "Falso", "Se corrige y se agradece."),
        ex("¿Qué incluye una buena presentación? A) fuente, lo que cuenta, mi interpretación y límites B) solo mi interpretación", "A", "Así se distingue lo que viene de la comunidad."),
    ],
    A=[
        ex("Borrador: «Dicen que los pueblos creen que las aves hicieron el mundo». Marca el problema. A) no nombra fuente ni comunidad B) tiene tildes", "A", "No sabemos de quién es el dato."),
        ex("Pasos de la revisión: 1) escribo 2) pido revisión 3) corrijo 4) presento. ¿Qué paso va justo antes de corregir?", "Pedir revisión", "Primero se revisa y luego se corrige."),
        ex("Un borrador dice: «El relato de Isla Niebla es más importante que el de Pampa Larga». ¿Qué ítem de la lista no cumple? A) no jerarquizar B) incluir límites", "A", "La frase ordena relatos."),
    ],
    Z=[
        ex("Raúl dice que, si él cree que su trabajo está bien, no necesita validación. ¿Qué error comete?", "Cree que no puede tener errores", "La validación la hace quien conoce la cultura."),
        ex("¿Por qué es importante decir que los relatos del cuaderno son inventados? A) para no confundirlos con relatos reales de un pueblo B) para que parezcan reales", "A", "Evita atribuir cosas inventadas a un pueblo."),
    ],
    D=[
        ex("Revisa este borrador con la lista: «Según don Camilo, el Pez Mayor formó la isla (relato inventado de Isla Niebla). Yo pienso que el relato explica el origen de la isla. No sé cómo se cuida el bosque». ¿Qué falta? A) pedir revisión a la comunidad B) más datos inventados", "A", "Tiene fuente, interpretación y límite, pero no revisión."),
        ex("Un compañero quiere agregar al panel un relato que le contó un vecino, sin permiso. ¿Qué le recomiendas? A) pedir permiso antes B) agregarlo", "A", "Hace falta autorización."),
    ],
    context=[ex("Preparan una exposición con los cuatro relatos inventados del cuaderno. La profesora pide que el cartel diga algo importante en la parte de arriba. ¿Qué escribes? A) «Relatos inventados para aprender a leer relatos» B) «Relatos de pueblos indígenas»", "A", "Aclara que no son relatos reales.")],
    selfcheck=[
        ex("Nombra dos preguntas de la lista de revisión.", "Dos entre: fuente, ideas marcadas, límites, no jerarquizar, no inventar, pedir revisión", "Están en la explicación."),
        ex("Verdadero o falso: las correcciones de la comunidad se agradecen.", "Verdadero", "Son parte de aprender con respeto."),
        ex("¿Qué haces si falta una fuente en tu borrador? A) la agrego o quito el dato B) lo dejo", "A", "Un dato sin fuente no se mantiene."),
    ],
    task=T("Este es un borrador inventado: «Los indígenas creen que el mundo lo hizo una niebla. El relato de la niebla es el mejor. Dicen que adoran la quebrada.» Revísalo con la lista: fuente, ideas marcadas, límites, no jerarquizar, no inventar. Escribe una versión mejorada usando solo el relato de Ladera Verde de doña Elena: «Al comienzo, los cerros dormían bajo una niebla espesa. La Abuela Niebla sopló y se despertó la primera quebrada.» Termina con una frase para pedir revisión al educador tradicional.",
           "Versión mejorada: Según doña Elena, de Ladera Verde (relato inventado), al comienzo los cerros dormían bajo una niebla espesa y la Abuela Niebla sopló y despertó la primera quebrada. Yo pienso que el relato explica el origen de la quebrada. No sé cómo se cuida la quebrada hoy. ¿Podría revisar mi texto y decirme qué corregir?",
           ["corrige las tres fallas del borrador", "usa solo el relato dado", "pide revisión"], ["versión mejorada", "frase de revisión"], ["mantener «el mejor»", "mantener «adoran»"],
           "Pedir que marque en su versión cada falla que corrigió."),
    reinforce="Haz una lista de revisión de seis preguntas con casilla para marcar.",
    extend="Escribe cómo reaccionarías si el educador tradicional te pide quitar un párrafo de tu trabajo.",
)

# ============================================================ OA 11 · Personas portadoras de saberes ancestrales
SAB = ("Ficha situada (inventada). Comunidad: Ladera Verde (no es un pueblo real). Persona: don Rubén, que cuida las semillas de la comunidad. Fuente y responsable: don Rubén. "
       "Fecha: la de hoy, de ejemplo. Permiso: don Rubén autorizó usar esta ficha en la escuela. Límite: no se cuenta cómo se guardan ciertas semillas especiales.")

L(
    OA11, 1, materials=MAT,
    use="Aprenderé a situar a una persona portadora de saberes ancestrales y a reconocer su rol en la comunidad. Sirve para valorar a quienes guardan y transmiten los conocimientos de un pueblo.",
    prior=["Sé situar una fuente con su ficha.", "Sé que la visión de mundo es la manera en que un pueblo entiende la vida."],
    explain=[
        "Un saber ancestral es un conocimiento que un pueblo ha cuidado y transmitido por generaciones. Puede ser sobre las semillas, las plantas, el tejido, los cielos, las historias o la manera de convivir. La persona portadora de saberes es quien lo guarda, lo practica y lo enseña a otras personas.",
        "Cada pueblo tiene sus propios nombres para estas personas y sus propias formas de reconocerlas. Esos nombres y roles los enseña el educador o educadora tradicional. En este cuaderno usamos personas inventadas, como don Rubén, que cuida las semillas, para aprender a reconocer su aporte sin inventar roles de un pueblo real.",
        "El saber de una persona portadora muestra la visión de mundo de su pueblo: por ejemplo, cómo entiende la relación con la tierra. No se mide por títulos de escuela: se valora porque la comunidad la reconoce. Se la cuida pidiendo permiso antes de preguntar, agradeciendo lo que enseña y respetando lo que no cuenta.",
    ],
    vocab=[("saber ancestral", "conocimiento que un pueblo cuida y transmite por generaciones"), ("portador o portadora de saberes", "persona que guarda, practica y enseña esos conocimientos"), ("transmitir", "pasar un conocimiento a otras personas"), ("reconocimiento", "valoración que la comunidad hace de una persona"), ("generación", "grupo de personas de edades parecidas")],
    worked=[
        W("Situar a una persona portadora", SAB + " ¿Quién es, qué saber guarda y qué no se cuenta?", ["La persona es don Rubén, de Ladera Verde.", "Guarda saberes sobre las semillas.", "El límite dice que no se cuenta cómo se guardan ciertas semillas especiales."], "Don Rubén, de Ladera Verde, cuida las semillas; no se cuenta cómo guarda ciertas semillas especiales."),
        W("Saber más allá de la escuela", "Una niña dice: «Don Rubén no sabe nada porque no fue a la universidad». ¿Qué corriges?", ["Don Rubén guarda saberes sobre las semillas.", "Ese saber lo reconoce la comunidad.", "La escuela no es la única forma de saber."], "Corrijo: don Rubén es portador de saberes reconocidos por su comunidad."),
    ],
    mistakes=[
        M("Pensar que solo vale el saber que se aprende en la escuela.", "Los pueblos guardan saberes que se transmiten de generación en generación.", "Valora también los saberes ancestrales."),
        M("Inventar el nombre del rol de una persona de un pueblo real.", "Cada pueblo tiene sus propios nombres.", "Pregunta al educador tradicional."),
    ],
    R=[
        ex("Ficha inventada: «Persona: don Rubén, que cuida las semillas». ¿Qué cuida don Rubén?", "Las semillas", "La ficha lo dice."),
        ex("Ficha inventada: «Límite: no se cuenta cómo se guardan ciertas semillas especiales». ¿Escribes cómo se guardan esas semillas? Responde Sí o No.", "No", "El límite lo prohíbe."),
        ex("¿Quién reconoce a una persona portadora de saberes? A) su comunidad B) cualquier visitante", "A", "La comunidad la reconoce."),
    ],
    C=[
        ex("Verdadero o falso: un saber ancestral se transmite de generación en generación.", "Verdadero", "Es parte de la definición."),
        ex("¿Qué es una persona portadora de saberes? A) quien guarda, practica y enseña un conocimiento de su pueblo B) quien tiene un título escolar", "A", "Su saber lo reconoce la comunidad."),
        ex("Verdadero o falso: los nombres de los roles de un pueblo real los puedo inventar.", "Falso", "Los enseña el educador tradicional."),
    ],
    A=[
        ex("Ficha inventada: «Persona: doña Clara, que conoce las plantas de la quebrada». ¿Qué saber guarda doña Clara?", "Sobre las plantas de la quebrada", "La ficha lo dice."),
        ex("Clasifica en SABER ANCESTRAL o NO: a) cuidar y guardar semillas como lo enseñó una persona mayor de la comunidad b) aprender una canción de moda.", "a saber ancestral, b no", "El primero se transmite de generación en generación."),
        ex("Una ficha trae a la persona y el saber, pero no dice si autorizó compartirlo. ¿Puedes usarla? Responde Sí o No.", "No", "Sin permiso no se puede compartir."),
    ],
    Z=[
        ex("Lucas dice: «Como don Rubén guarda semillas, todos los pueblos guardan semillas igual». ¿Qué error comete?", "Generaliza una ficha a todos los pueblos", "Cada pueblo tiene sus saberes."),
        ex("¿Por qué se pide permiso antes de preguntarle a una persona portadora? A) porque su saber es suyo y de su comunidad B) para perder tiempo", "A", "El saber no se toma sin autorización."),
    ],
    D=[
        ex("Hay dos fichas: don Rubén, que cuida semillas, y doña Clara, que conoce plantas. Alguien escribe «sabe dónde crece cada planta de la quebrada». ¿De cuál ficha viene?", "De doña Clara", "Las plantas de la quebrada son de su ficha."),
        ex("Una niña quiere grabar a doña Clara sin avisar para su trabajo. ¿Qué haces? A) le digo que primero pida permiso B) la ayudo a grabar", "A", "La grabación necesita autorización."),
    ],
    context=[ex("Tu curso invitará a una persona de la comunidad a contar un saber. ¿Qué se hace primero? A) preguntar a la persona y al educador tradicional si desea participar y cómo B) enviar una invitación sin consultar", "A", "Primero se consulta y se pide permiso.")],
    selfcheck=[
        ex("Explica con tus palabras qué es un saber ancestral.", "Un conocimiento que un pueblo cuida y transmite por generaciones", "Es la definición de la clase."),
        ex("Verdadero o falso: el saber de una persona portadora se valora aunque no tenga título escolar.", "Verdadero", "La comunidad lo reconoce."),
        ex("¿A quién preguntas por el rol de una persona de un pueblo real? A) al educador tradicional B) a nadie", "A", "Ellos son la fuente."),
    ],
    task=T("Lee esta ficha inventada: «Comunidad: Río Hondo. Persona: doña Inés, que teje con lana. Fuente: doña Inés. Permiso: sí. Límite: no se muestran los diseños que su familia reserva.» Completa una tabla con: persona, saber que guarda, qué la comunidad valora de ella y qué límite debes respetar. Escribe una pregunta respetuosa que le harías a doña Inés.",
           "Persona: doña Inés. Saber: tejer con lana. La comunidad valora que enseña a tejer. Límite: no se muestran los diseños reservados. Pregunta: ¿qué le gustaría que aprendiéramos sobre el tejido?",
           ["completa la tabla con datos de la ficha", "respeta el límite", "formula una pregunta respetuosa"], ["tabla de cuatro filas", "pregunta"], ["inventar diseños", "decir que todos los pueblos tejen igual"],
           "Pedir que muestre cada dato en la ficha."),
    reinforce="Dibuja un cartel de agradecimiento para una persona portadora inventada, sin mostrar nada de lo reservado.",
    extend="Escribe dos saberes que podrían tener las personas mayores de una comunidad, sin atribuirlos a un pueblo real.",
)

L(
    OA11, 2, materials=MAT,
    use="Aprenderé a escuchar el testimonio de una persona portadora de saberes con límites: qué cuenta, qué no cuenta y qué puedo preguntar. Sirve para aprender con respeto de quienes guardan los conocimientos de un pueblo.",
    prior=["Sé situar a una persona portadora de saberes.", "Sé separar lo que dice una fuente de lo que interpreto."],
    explain=[
        "Escuchar un testimonio es una forma de aprender. Cuando una persona portadora de saberes habla, hacemos tres cosas. Escuchamos con atención y sin interrumpir. Anotamos lo que dice con sus palabras. Y marcamos lo que ella no cuenta, que se respeta como parte de su saber.",
        "Algunas cosas se pueden preguntar y otras no. Se pueden preguntar cosas generales, como qué hace, con quién aprendió o qué cuidados tiene su trabajo. No se insiste en lo que no quiere contar, no se pide mostrar lo reservado y no se graba ni fotografía sin permiso.",
        "Cuando el testimonio termina, repasamos con la persona lo que entendimos. Así comprobamos que no cambiamos su mensaje. Mis interpretaciones se marcan con «yo pienso que» y las dudas culturales se llevan al educador o educadora tradicional.",
    ],
    vocab=[("testimonio", "lo que una persona cuenta de su saber o su vida"), ("escuchar con atención", "oír sin interrumpir y sin hacer otra cosa"), ("pregunta general", "pregunta que no pide lo reservado"), ("reservado", "lo que la persona prefiere no contar"), ("repasar", "volver a decir lo entendido para comprobarlo")],
    worked=[
        W("Elegir preguntas", "Don Rubén (inventado) dice: «Cuido las semillas de la comunidad. Hay semillas que guardo aparte y no cuento cómo». ¿Qué preguntas son adecuadas? A) «¿Con quién aprendió a cuidar semillas?» B) «¿Cómo guarda las semillas especiales?»", ["La A pregunta algo general.", "La B pide justo lo que no cuenta.", "Elijo la A."], "A"),
        W("Repasar lo entendido", "Después del testimonio, dices: «Entendí que usted cuida las semillas y que algunas las guarda aparte». ¿Para qué sirve?", ["Muestra lo que entendí.", "Permite que don Rubén corrija.", "Así no cambio su mensaje."], "Sirve para comprobar que entendí bien y evitar cambiar su mensaje."),
    ],
    mistakes=[
        M("Insistir en preguntar lo que la persona no quiere contar.", "No se respeta su decisión.", "Cambia a una pregunta general."),
        M("Grabar o sacar fotos sin pedir permiso.", "El saber y la imagen de la persona le pertenecen.", "Pide permiso antes de grabar."),
    ],
    R=[
        ex("Don Rubén dice: «Hay semillas que guardo aparte y no cuento cómo». ¿Qué no cuenta? A) cómo guarda esas semillas B) que cuida semillas", "A", "Eso es lo que reserva."),
        ex("¿Puedes grabar a la persona que cuenta su saber sin su permiso? Responde Sí o No.", "No", "La grabación necesita autorización."),
        ex("¿Qué haces mientras alguien cuenta su saber? A) escucho sin interrumpir B) hablo de otra cosa", "A", "Escuchar con atención es parte del respeto."),
    ],
    C=[
        ex("Verdadero o falso: puedo insistir hasta que la persona cuente lo que reserva.", "Falso", "Se respeta lo que no cuenta."),
        ex("¿Qué es una pregunta general? A) una que no pide lo reservado B) una que pide secretos", "A", "Así se respeta a la persona."),
        ex("Verdadero o falso: repasar lo entendido permite que la persona corrija.", "Verdadero", "Comprueba que no se cambió su mensaje."),
    ],
    A=[
        ex("Clasifica en PREGUNTA ADECUADA o NO ADECUADA: a) ¿Con quién aprendió su oficio? b) Muéstrenos el lugar que guarda en secreto.", "a adecuada, b no adecuada", "La primera es general; la segunda pide lo reservado."),
        ex("Testimonio inventado de doña Clara: «Conozco las plantas de la quebrada. Las aprendí con mi madre. No cuento para qué sirve cada una». ¿Con quién aprendió doña Clara?", "Con su madre", "El testimonio lo dice."),
        ex("Doña Clara no cuenta para qué sirve cada planta. ¿Qué escribes en tu trabajo? A) que ella no cuenta eso B) lo que creo que sirve", "A", "No se inventa lo no contado."),
    ],
    Z=[
        ex("Julián dice: «Si no me cuenta, lo busco en internet y lo escribo como suyo». ¿Qué error comete?", "Atribuye a la persona algo que no contó", "Se debe respetar lo reservado y no inventar su voz."),
        ex("¿Por qué conviene repasar lo entendido con la persona? A) porque así se corrigen errores de interpretación B) porque ocupa tiempo", "A", "La persona puede aclarar lo mal entendido."),
    ],
    D=[
        ex("Dos preguntas para doña Clara. 1) «¿Cómo cuida usted las plantas en el invierno?» 2) «¿Cuál es la planta que usan para curar a los enfermos?» ¿Cuál es general y adecuada?", "La primera", "La segunda pide un saber que ella puede reservar y toca la salud."),
        ex("Quieres sacar una foto a las manos de doña Clara tejiendo. ¿Qué haces primero? A) pedirle permiso B) sacarla y preguntar después", "A", "La imagen necesita autorización."),
    ],
    context=[ex("En una visita escolar a una artesana inventada, un compañero levanta el celular para filmar. ¿Qué le dices? A) que antes pida permiso a la artesana B) que filme rápido", "A", "La grabación necesita permiso.")],
    selfcheck=[
        ex("Nombra dos cosas que haces al escuchar a una persona portadora de saberes.", "Dos entre: escuchar, anotar, respetar lo reservado, repasar, pedir permiso", "Están en la explicación."),
        ex("Verdadero o falso: puedo preguntar cosas generales sobre su trabajo.", "Verdadero", "Las preguntas generales son adecuadas."),
        ex("¿Qué haces con las dudas culturales? A) las llevo al educador tradicional B) las invento", "A", "Él o ella es la fuente."),
    ],
    task=T("Lee este testimonio inventado de doña Inés, de Río Hondo: «Teje lana desde niña. Aprendió con su abuela. Hay diseños que su familia no muestra a otras personas.» Escribe cinco preguntas para una conversación con ella: tres adecuadas y generales y dos que NO harías porque pedirían lo reservado. Explica en una línea por qué esas dos no son adecuadas.",
           "Adecuadas: ¿Qué es lo que más le gusta de tejer? ¿Qué cuidados tiene la lana? ¿Qué le gustaría que los niños supieran? No adecuadas: ¿Puede mostrarnos los diseños de su familia? ¿Nos cuenta qué significan los diseños reservados? Porque pedirían lo que su familia decidió reservar.",
           ["escribe tres preguntas adecuadas", "reconoce dos preguntas que pedirían lo reservado", "explica la razón"], ["cinco preguntas", "explicación"], ["pedir lo reservado", "insistir"],
           "Pedir que explique cómo cada pregunta respeta lo que la persona cuenta."),
    reinforce="Marca con verde tus preguntas adecuadas y con rojo las que no harías.",
    extend="Escribe una frase con la que repasarías con doña Inés lo que entendiste.",
)

L(
    OA11, 3, materials=MAT,
    use="Aprenderé a reconocer cómo los saberes de las personas portadoras se relacionan con la visión de mundo de su pueblo y con la vida de la comunidad. Sirve para valorar por qué esos saberes importan.",
    prior=["Sé escuchar un testimonio con límites.", "Sé que la visión de mundo es una manera de entender la vida."],
    explain=[
        "Los saberes ancestrales no están aislados: se relacionan con la manera en que un pueblo entiende el mundo. Por ejemplo, si una persona cuida las semillas de la comunidad y las reparte cada temporada, su saber muestra una idea: la tierra y las semillas se cuidan entre todos y se comparten. Esa idea es parte de la visión de mundo.",
        "Los saberes también se relacionan entre sí. Quien cuida semillas, quien conoce plantas y quien teje trabajan en cosas distintas, pero se complementan: las plantas dan fibras para tejer, y el tejido se usa en la huerta. Cada persona aporta algo distinto y ninguna es más importante.",
        "Hay otra relación: la transmisión. Las personas portadoras enseñan a niñas, niños y jóvenes, y la comunidad les devuelve respeto y apoyo. Esto se llama reciprocidad: dar y recibir de manera equilibrada. Así el saber continúa. Estas relaciones se anotan con la fuente y se marcan como idea mía cuando no las dice el testimonio.",
    ],
    vocab=[("complementarse", "completarse unos con otros"), ("transmisión", "paso del saber de una generación a otra"), ("reciprocidad", "dar y recibir de manera equilibrada"), ("temporada", "período del año con tareas propias"), ("aporte", "lo que una persona o grupo da a la comunidad")],
    worked=[
        W("Relacionar saber y visión de mundo", "Testimonio inventado de don Rubén: «Cada temporada reparto semillas entre las familias y ellas me devuelven una parte de lo cosechado». ¿Qué idea de mundo muestra?", ["Reparte semillas entre las familias.", "Las familias devuelven parte de lo cosechado.", "Muestra reciprocidad: se da y se recibe."], "Muestra una idea de reciprocidad: las semillas y la cosecha se comparten."),
        W("Saberes que se complementan", "Don Rubén cuida semillas, doña Clara conoce plantas y doña Inés teje. ¿Cuál es más importante?", ["Cada una aporta algo distinto.", "Los saberes se complementan.", "No se ordenan."], "Ninguna: se complementan y no se ordenan."),
    ],
    mistakes=[
        M("Decir que un saber es más importante que otro.", "Los saberes se complementan.", "Describe qué aporta cada uno."),
        M("Atribuir a la comunidad una idea de mundo que el testimonio no dice.", "Sería inventar su visión de mundo.", "Marca como «yo pienso que» y apoya en una frase."),
    ],
    R=[
        ex("Don Rubén (inventado): «Cada temporada reparto semillas entre las familias». ¿Qué reparte?", "Semillas", "El testimonio lo dice."),
        ex("¿Qué es la reciprocidad? A) dar y recibir de manera equilibrada B) guardar todo para uno", "A", "Es una forma de relación en la comunidad."),
        ex("¿Qué hacen las personas portadoras con niñas, niños y jóvenes? A) enseñan lo que saben B) les piden que se queden en silencio siempre", "A", "Transmiten su saber."),
    ],
    C=[
        ex("Verdadero o falso: los saberes de distintas personas pueden complementarse.", "Verdadero", "Se completan entre sí."),
        ex("Verdadero o falso: un saber se transmite cuando una persona lo enseña a otra generación.", "Verdadero", "Esa es la transmisión."),
        ex("Verdadero o falso: el saber de quien cuida semillas es más importante que el de quien teje.", "Falso", "Los saberes no se ordenan."),
    ],
    A=[
        ex("Clasifica en SABER o APORTE A LA COMUNIDAD: a) conocer cuándo sembrar cada semilla b) repartir semillas entre familias.", "a saber, b aporte", "Conocer es el saber; repartir es lo que aporta."),
        ex("Don Rubén recibe de las familias una parte de lo cosechado como agradecimiento. ¿Qué idea muestra? A) reciprocidad B) competencia", "A", "Da semillas y recibe agradecimiento."),
        ex("Doña Clara conoce plantas que dan fibra y doña Inés teje con fibras. ¿Cómo se relacionan sus saberes? A) se complementan B) se oponen", "A", "Uno aporta lo que el otro usa."),
    ],
    Z=[
        ex("Tomás dice: «La visión de mundo de la comunidad es que todo es de todos». El testimonio solo habla de repartir semillas. ¿Qué problema tiene?", "Generaliza más de lo que dice el testimonio", "El testimonio habla de semillas, no de todo."),
        ex("¿Por qué una persona portadora enseña a niñas y niños? A) para que el saber continúe B) para tener ayuda en tareas", "A", "La transmisión mantiene vivo el saber."),
    ],
    D=[
        ex("Hay tres personas inventadas: don Rubén (semillas), doña Clara (plantas), doña Inés (tejido). Un panel las pone en orden de importancia. ¿Qué corriges? A) no se ordenan: cada una aporta algo distinto B) pongo a doña Inés primero", "A", "No se jerarquizan."),
        ex("Un compañero escribe que la comunidad «adora las semillas». El testimonio solo dice que se reparten cada temporada. ¿Qué haces? A) quito «adora» porque no está en la fuente B) lo dejo", "A", "No se inventan ritos."),
    ],
    context=[ex("Para una feria escolar, un grupo expone a don Rubén. Alguien propone un cartel que diga «el más importante de la comunidad». ¿Qué cambias? A) «una de las personas que cuidan saberes de la comunidad» B) nada", "A", "No se jerarquiza.")],
    selfcheck=[
        ex("Escribe una relación entre un saber y la visión de mundo.", "Repartir semillas muestra una idea de compartir y reciprocidad", "Es el ejemplo de la clase."),
        ex("Verdadero o falso: los saberes de una comunidad se ordenan del más al menos importante.", "Falso", "Los saberes se complementan entre sí."),
        ex("¿Qué es la reciprocidad? Escribe una frase corta.", "Dar y recibir de manera equilibrada", "Es la definición de la clase."),
    ],
    task=T("Lee estos tres testimonios inventados de Río Hondo. Don Aurelio: «Cuido el bosque y sé cuándo se puede recoger leña seca». Doña Inés: «Tejo con lana que me trae mi familia». Don Pedro: «Enseño a los niños a conocer los senderos del bosque». Haz un esquema que muestre qué aporta cada uno y cómo se relacionan entre sí, usando flechas. Escribe una frase sobre qué idea del mundo puede mostrar el conjunto, marcada con «yo pienso que», y un límite.",
           "Don Aurelio aporta conocimiento del bosque. Doña Inés aporta tejido. Don Pedro aporta enseñanza de senderos. Relación: don Aurelio y don Pedro conocen el bosque, uno su leña seca y otro sus senderos; doña Inés teje con lana de su familia; los tres aportan algo distinto. Yo pienso que la comunidad cuida el bosque entre todos. Límite: los testimonios no dicen cómo toman decisiones.",
           ["esquema con tres aportes", "una frase marcada como idea propia", "un límite"], ["esquema con flechas", "frase y límite"], ["ordenar a las personas por importancia", "inventar ideas que no están"],
           "Pedir que muestre en cada flecha qué dice el testimonio."),
    reinforce="Dibuja tres círculos que se tocan, uno por cada persona, y escribe en el centro lo que comparten.",
    extend="Explica por qué la reciprocidad ayuda a que un saber continúe en el tiempo.",
)

L(
    OA11, 4, materials=MAT,
    use="Aprenderé a construir una respuesta atribuida que valore a una persona portadora de saberes, con su permiso y sus límites. Sirve para agradecerle y mostrar lo aprendido sin apropiarse de su saber.",
    prior=["Sé escuchar un testimonio con límites.", "Sé relacionar saberes con visión de mundo."],
    explain=[
        "Valorar a una persona portadora de saberes es reconocer su aporte, agradecer lo que enseña y cuidar su saber. Para eso construimos una respuesta atribuida con cuatro partes: quién es la persona y qué cuenta; qué aprendí y qué idea de mundo me muestra; qué límites respeto; y cómo le agradezco y le devuelvo el trabajo.",
        "Apropiarse de un saber es usarlo como si fuera propio, sin nombrar a quien lo enseñó o sin su permiso. Para evitarlo, nombramos siempre a la persona, no presentamos su saber como nuestro y no lo usamos en un producto comercial sin permiso. Si queremos mostrar algo de lo aprendido, pedimos autorización.",
        "La devolución es parte de la respuesta: le mostramos nuestro texto, escuchamos sus correcciones y la agradecemos. Una buena respuesta termina con una pregunta que llevaremos al educador o educadora tradicional y con una nota de lo que no corresponde divulgar.",
    ],
    vocab=[("apropiarse", "usar un saber como propio, sin nombrar a quien lo enseñó o sin permiso"), ("agradecer", "reconocer con palabras lo recibido"), ("autoría", "reconocimiento de quién creó o enseñó algo"), ("divulgar", "dar a conocer a muchas personas"), ("devolución", "mostrar el trabajo a la persona para que lo revise")],
    worked=[
        W("Escribir un reconocimiento", "Con el testimonio de don Rubén (inventado), que cuida semillas y las reparte cada temporada, escribe un reconocimiento corto.", ["Nombro a don Rubén.", "Cuento qué aprendí: reparte semillas y las familias devuelven parte de la cosecha.", "Agradezco y declaro un límite."], "Don Rubén cuida las semillas de Ladera Verde y las reparte cada temporada. Aprendí que las familias comparten la cosecha. Gracias por enseñarnos; no sé cómo guarda ciertas semillas especiales."),
        W("Evitar apropiarse", "Un niño dice: «Voy a vender dibujos con el método de don Rubén para guardar semillas». ¿Qué problema tiene?", ["No pidió permiso.", "Usa un saber ajeno en un producto comercial.", "Es apropiarse."], "Es apropiarse de un saber ajeno sin permiso."),
    ],
    mistakes=[
        M("Presentar un saber de otra persona como si fuera mío.", "Es apropiarse y borra a quien lo enseñó.", "Nombra a la persona y pide permiso."),
        M("Terminar sin devolver el trabajo a la persona.", "No tuvo oportunidad de corregirlo.", "Muestra el texto y escucha sus correcciones."),
    ],
    R=[
        ex("¿Cuántas partes tiene la respuesta de esta clase? Escribe el número.", "4", "Quién, qué aprendí, límites y agradecimiento."),
        ex("¿Qué haces con el saber que una persona te enseña? A) nombro a quien lo enseñó B) digo que es mío", "A", "Nombrar es reconocer autoría."),
        ex("Verdadero o falso: la devolución es mostrar el trabajo a la persona.", "Verdadero", "Es parte de la respuesta."),
    ],
    C=[
        ex("¿Qué es apropiarse de un saber? A) usarlo como propio sin nombrar a quien lo enseñó B) agradecerlo", "A", "Es lo contrario de reconocer."),
        ex("Verdadero o falso: puedo usar un saber de una persona en un producto para vender sin su permiso.", "Falso", "Eso sería apropiarse."),
        ex("Verdadero o falso: una buena respuesta termina con agradecimiento y una pregunta.", "Verdadero", "Cierra con respeto."),
    ],
    A=[
        ex("Ordena: A) agradecer B) nombrar a la persona C) contar qué aprendí D) declarar un límite. ¿Cuál va primero?", "B", "Primero se nombra a la persona."),
        ex("Clasifica en RECONOCE o SE APROPIA: a) «Doña Clara me enseñó esto» b) «Yo descubrí cómo se hace».", "a reconoce, b se apropia", "La primera da crédito; la segunda lo quita."),
        ex("Completa: «Gracias, don Rubén, por enseñarnos que…» ¿Qué dato de este cuaderno cabe? A) las semillas se reparten cada temporada B) las semillas son mágicas", "A", "El testimonio lo dice; lo mágico no."),
    ],
    Z=[
        ex("Lucía dice que, si pone el nombre de la persona, ya no necesita su permiso. ¿Qué error comete?", "Confunde nombrar con pedir permiso", "El permiso es otra cosa."),
        ex("¿Por qué se devuelve el trabajo a la persona? A) para que corrija lo que quedó mal B) para presumir", "A", "Ella conoce su saber."),
    ],
    D=[
        ex("Un trabajo dice: «Aprendí a guardar semillas». No nombra a don Rubén. ¿Qué cambias? A) agrego su nombre y de quién aprendí B) lo dejo", "A", "Se reconoce a quien enseñó."),
        ex("Quieres incluir en tu trabajo una técnica reservada que don Rubén no contó. ¿Qué haces? A) la omito B) la busco en otra parte y la agrego", "A", "Se respeta lo reservado."),
    ],
    context=[ex("Una empresa de la comuna ofrece pagar por una receta que enseñó una persona de la comunidad, sin consultarle. ¿Qué dices? A) que primero deben pedirle permiso a ella B) que la entreguen", "A", "El saber es de la persona y su comunidad.")],
    selfcheck=[
        ex("Nombra las cuatro partes de la respuesta.", "Quién es, qué aprendí, límites y agradecimiento", "Están en la explicación."),
        ex("Verdadero o falso: apropiarse de un saber es nombrar a quien lo enseñó.", "Falso", "Es lo contrario."),
        ex("¿Qué haces con las correcciones de la persona? A) las acepto y agradezco B) las discuto", "A", "Es parte de la devolución."),
    ],
    task=T("Escribe un reconocimiento de cuatro partes para doña Clara, inventada, que conoce las plantas de la quebrada y dijo: «Aprendí con mi madre. No cuento para qué sirve cada planta». Incluye: quién es y qué cuenta, qué aprendiste, el límite que respetas y un agradecimiento con la promesa de mostrarle el texto. No escribas para qué sirven las plantas.",
           "Doña Clara conoce las plantas de la quebrada y aprendió con su madre. Aprendí que los saberes se transmiten entre generaciones. Respeto que ella no cuente para qué sirve cada planta. Gracias por enseñarnos; le mostraré este texto para que lo revise.",
           ["incluye las cuatro partes", "respeta el límite", "promete devolución"], ["texto de cuatro partes"], ["inventar usos de las plantas", "no nombrar a la persona"],
           "Pedir que indique de dónde sacó cada dato."),
    reinforce="Escribe en una tarjeta el agradecimiento para doña Clara, sin datos reservados.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo reconocer a las personas portadoras de saberes de tu comunidad.",
)
