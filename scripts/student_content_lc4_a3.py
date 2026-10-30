"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 11 (arte y técnicas ancestrales en diálogo con la naturaleza) y OA 12 (normas en eventos socioculturales y espirituales).

Criterio de autoría: las comunidades, las personas, las técnicas y los eventos de práctica son INVENTADOS y se
rotulan así. No se describe ninguna técnica, diseño, ceremonia, rito, discurso ni norma de un pueblo concreto.
Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad; ningún ejercicio exige saber
una lengua indígena ni reproducir un evento.
"""
from __future__ import annotations

from student_content_lc4_a import FC4, FV4, L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA11, OA12 = "LC04 OA 11", "LC04 OA 12"

DISC = "Discurso de práctica (inventado): «Bienvenidos a Valle Alto. Hoy agradecemos el agua. Escuchemos en silencio y compartamos lo que traemos.»"

CESTO = ("Ficha de práctica (inventada). Comunidad: Valle Alto (no es un pueblo real). Fuente: doña Rosa, maestra artesana de la comunidad. "
         "Técnica: cestos tejidos con fibras de junco que crecen en la orilla del río. Cómo se cuida el junco: se recoge solo lo necesario, "
         "nunca en la época en que está creciendo, y se deja la mitad de cada mata. Cómo se enseña: los niños aprenden mirando y practicando junto a una persona mayor. "
         "Permiso: sí. Límite: no se muestran los diseños que la comunidad reserva.")
REDES = ("Ficha de práctica (inventada). Comunidad: Costa Clara (no es un pueblo real). Fuente: don Luis, pescador. "
         "Técnica: redes anudadas a mano con hilo resistente, que se arreglan en comunidad en las rocas planas. Cómo se cuida el mar: se usan redes del tamaño justo y no se pesca todos los días. "
         "Cómo se enseña: los más jóvenes aprenden anudando junto a los mayores. Permiso: sí. Límite: no se cuentan las historias reservadas de la caleta.")
EVENTO = ("Ficha de práctica (inventada). Comunidad: Valle Alto (no es un pueblo real). Evento: Encuentro del Agua (inventado, no corresponde a ninguna ceremonia real). "
          "Fuente: doña Rosa. Para qué se hace: la comunidad se junta a agradecer el agua de la vertiente. Quién guía: una persona mayor elegida por la comunidad. "
          "Normas: llegar a tiempo, saludar, escuchar en silencio, no sacar fotos sin permiso. Permiso: sí. Límite: no se cuenta lo que se hace en el centro del círculo.")

# ============================================================ OA 11 · Arte y técnicas ancestrales en diálogo con la naturaleza
L(
    OA11, 1,
    materials="Lápiz y hojas. La ficha de práctica está escrita aquí y es inventada.",
    use="Aprenderé a reconocer de dónde viene una técnica o un arte, quiénes la guardan y cómo se transmite. Sirve para valorar los saberes de una comunidad sin atribuírselos a otros.",
    prior=["Sé situar una fuente con permiso y límite.", "Sé que los saberes de una comunidad no son iguales a los de otra."],
    explain=[
        "Un arte o una técnica ancestral es un saber que una comunidad practica desde hace mucho tiempo para hacer objetos, obras o trabajos con materiales de su territorio. Se llama ancestral porque viene de las generaciones anteriores, pero se sigue practicando hoy.",
        "Los saberes se construyen y se validan en la comunidad. Eso significa que las personas de la comunidad los practican, los comparan y los reconocen como bien hechos. Las personas que guardan un saber se llaman portadoras o portadores, y tienen la responsabilidad de enseñarlo a otros con cuidado. A esa entrega se la llama transmisión.",
        "Para reconocer el origen de una técnica, preguntamos: ¿de qué comunidad es?, ¿quién la guarda?, ¿con qué materiales de la naturaleza se hace?, ¿cómo se enseña? y ¿qué parte se comparte? No decimos que una técnica es de todos los pueblos, ni la mostramos como si fuera nuestra.",
    ],
    vocab=[("técnica ancestral", "saber que se practica desde hace mucho tiempo, de generación en generación"), ("portador o portadora", "persona de la comunidad que guarda un saber y lo enseña"), ("transmisión", "entrega de un saber a otras personas"), ("validar", "reconocer que algo está bien hecho según la comunidad"), ("material", "cosa de la que está hecho un objeto")],
    worked=[
        W("Leer una ficha", "Lee: «" + CESTO + "» ¿De qué comunidad es la técnica, quién la guarda y cómo se enseña?", ["Comunidad: Valle Alto.", "Quien guarda: doña Rosa, maestra artesana.", "Se enseña mirando y practicando con una persona mayor."], "De Valle Alto; la guarda doña Rosa; se enseña mirando y practicando con una persona mayor."),
        W("Atribuir bien", "Un niño dice: «Los pueblos indígenas tejen todos con junco». ¿Qué error hay?", ["La ficha es de Valle Alto.", "No dice nada de otros pueblos.", "Generaliza."], "Generaliza una ficha a todos los pueblos."),
    ],
    mistakes=[
        M("Decir que una técnica es de todos los pueblos originarios.", "Cada comunidad tiene sus técnicas y materiales.", "Nombra la comunidad y la fuente."),
        M("Presentar una técnica como si la hubiera creado el curso.", "No se reconoce a quien la guarda.", "Nombra a la persona o comunidad portadora."),
    ],
    R=[
        ex("Según la ficha de Valle Alto, ¿con qué material se tejen los cestos?", "Fibras de junco", "La ficha lo dice."),
        ex("¿Quién es la fuente de la ficha de Valle Alto: doña Rosa o don Luis?", "Doña Rosa", "Ella es la maestra artesana de la ficha."),
        ex("¿Cómo aprenden los niños la técnica según la ficha? A) mirando y practicando con una persona mayor B) leyendo un libro", "A", "La ficha lo dice así."),
    ],
    C=[
        ex("¿Qué es un portador o portadora? A) persona que guarda un saber y lo enseña B) persona que compra un saber", "A", "Es quien guarda y transmite."),
        ex("Verdadero o falso: una técnica ancestral ya no se practica hoy.", "Falso", "Se sigue practicando hoy."),
        ex("Verdadero o falso: un saber se valida cuando la comunidad lo reconoce como bien hecho.", "Verdadero", "Los saberes se construyen y validan en la comunidad."),
    ],
    A=[
        ex("Ficha de Costa Clara (inventada): «Técnica: redes anudadas a mano con hilo resistente. Fuente: don Luis». Escribe el material y la persona que aparece en esa frase.", "Hilo resistente y don Luis", "La ficha lo dice."),
        ex("Une cada técnica con su comunidad. 1) cestos de junco 2) redes anudadas a mano a) Valle Alto b) Costa Clara", "1-a, 2-b", "Cada ficha nombra su comunidad."),
        ex("Una ficha dice «Técnica: tejido en palma» pero no dice quién la guarda ni si hay permiso. ¿Puedes usarla en un trabajo? Responde Sí o No.", "No", "Faltan la fuente y el permiso."),
    ],
    Z=[
        ex("Tomás dice: «Aprendí a tejer cestos viendo un video, así que ya soy portador del saber de Valle Alto». ¿Qué error comete?", "Un video no valida el saber: lo valida la comunidad", "Ser portador lo reconoce la comunidad."),
        ex("¿Por qué conviene decir quién guarda una técnica? A) porque se reconoce a quien la guarda y se evita apropiársela B) porque queda más largo el texto", "A", "Es dar crédito."),
    ],
    D=[
        ex("Dos frases: 1) «Los cestos de junco son una técnica que guarda doña Rosa, de Valle Alto» 2) «Los cestos de junco son de todos los pueblos». ¿Cuál atribuye bien?", "La primera", "La segunda generaliza."),
        ex("La ficha dice que no se muestran los diseños reservados. ¿Qué haces si un compañero quiere dibujarlos? A) respetar el límite y no mostrarlos B) buscarlos en internet", "A", "Lo reservado no se publica."),
    ],
    context=[ex("Tu curso hará una exposición sobre los cestos de Valle Alto (inventados). ¿Qué escribes junto a la imagen? A) comunidad y persona que guarda la técnica B) nada", "A", "Es dar crédito.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es la transmisión de un saber.", "Entrega de un saber a otras personas", "Es la definición de la clase."),
        ex("Verdadero o falso: puedo decir que una técnica es de todos los pueblos.", "Falso", "Cada comunidad tiene la suya."),
        ex("¿Qué haces antes de usar un saber de una comunidad? A) pregunto a la comunidad y pido permiso B) lo copio", "A", "El permiso lo da la comunidad."),
    ],
    task=T("Lee la ficha de práctica de Costa Clara: «" + REDES + "» Haz una tabla con cuatro filas: comunidad, persona que guarda la técnica, material y cómo se enseña. Escribe una frase que atribuya bien la técnica y una pregunta que le harías al educador tradicional sobre un arte de tu zona.",
           "Comunidad: Costa Clara. Guarda: don Luis. Material: hilo resistente. Se enseña anudando junto a los mayores. Frase: La comunidad de Costa Clara arregla redes anudadas a mano. Pregunta: ¿qué artes o técnicas se practican en nuestra comunidad?",
           ["completa la tabla con datos de la ficha", "atribuye bien la técnica", "formula una pregunta respetuosa"], ["tabla de cuatro filas", "frase de atribución", "pregunta"], ["decir que es de todos los pueblos", "agregar datos que la ficha no tiene"],
           "Pedir que muestre en la ficha cada dato; valorar que nombre a la comunidad."),
    reinforce="Subraya en la ficha de Valle Alto el material y la persona que guarda la técnica.",
    extend="Explica con tus palabras por qué un saber validado por la comunidad es distinto de una técnica aprendida en un video.",
)

L(
    OA11, 2,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a relacionar el material, la técnica y la naturaleza en un arte ancestral. Sirve para entender que estas técnicas dialogan con el territorio y lo cuidan.",
    prior=["Sé reconocer origen y portadores de una técnica.", "Sé que los materiales vienen del territorio."],
    explain=[
        "Un arte ancestral dialoga con la naturaleza: toma materiales del territorio, aprende de sus ciclos y los cuida para poder volver a usarlos. Decimos que hay una relación armónica cuando se toma lo necesario, se respeta la época de cada material y se deja que la naturaleza se recupere.",
        "Para relacionar material, técnica y naturaleza, miramos tres cosas: qué material se usa, cómo se transforma con la técnica y qué cuidados se tienen para no dañar el lugar de donde viene. En Valle Alto (inventada), el junco se recoge en la orilla del río, se teje y se deja la mitad de cada mata.",
        "Cada comunidad tiene sus materiales y sus cuidados. No sirve decir que todas las técnicas usan lo mismo. Y para conocer una técnica real, la guía es el educador o educadora tradicional, que explica qué se puede mostrar y cómo.",
    ],
    vocab=[("relación armónica", "convivencia respetuosa y de equilibrio con la naturaleza"), ("ciclo natural", "cambio que se repite en la naturaleza, como las estaciones"), ("recolectar", "recoger materiales de la naturaleza"), ("transformar", "cambiar un material para hacer otra cosa"), ("cuidado", "acción para no dañar algo")],
    worked=[
        W("Relacionar tres cosas", "Lee: «" + CESTO + "» ¿Qué material, qué técnica y qué cuidado hay?", ["Material: fibras de junco.", "Técnica: tejer cestos.", "Cuidado: recoger solo lo necesario, no cuando crece y dejar la mitad de la mata."], "Junco, tejido de cestos y recolección con cuidado."),
        W("Cuenta del cuidado", "En una mata hay 12 tallos de junco. Si se deja la mitad, ¿cuántos tallos se recogen?", ["Hay 12 tallos.", "Se deja la mitad: 12 ÷ 2 = 6.", "Se recogen los otros 6."], "6 tallos."),
    ],
    mistakes=[
        M("Pensar que recolectar es sacar todo lo que se pueda.", "La naturaleza necesita recuperarse.", "Toma solo lo necesario."),
        M("Decir que todas las técnicas usan el mismo material.", "Cada territorio ofrece materiales distintos.", "Nombra el material de la ficha."),
    ],
    R=[
        ex("En la ficha de Valle Alto, ¿dónde crece el junco: en la orilla del río o en la playa?", "En la orilla del río", "La ficha lo dice."),
        ex("¿Cuánto se deja de cada mata de junco según la ficha?", "La mitad", "La ficha dice que se deja la mitad."),
        ex("¿Se recoge junco cuando está creciendo? Responde Sí o No.", "No", "La ficha dice que nunca en esa época."),
    ],
    C=[
        ex("¿Qué es una relación armónica con la naturaleza? A) tomar lo necesario y dejar que se recupere B) tomar todo lo que se pueda", "A", "Armonía es equilibrio y respeto."),
        ex("Verdadero o falso: un arte ancestral dialoga con la naturaleza porque usa materiales del territorio.", "Verdadero", "Es la idea de la clase."),
        ex("Verdadero o falso: todas las comunidades usan los mismos materiales.", "Falso", "Cada territorio ofrece materiales distintos."),
    ],
    A=[
        arith("En una mata hay 18 tallos de junco y se deja la mitad. ¿Cuántos tallos se pueden recoger?", "18//2", "Se divide en dos partes iguales y se deja una."),
        arith("Una cestera usa 5 tallos por cesto y quiere hacer 4 cestos. ¿Cuántos tallos necesita?", "5*4", "Se repite 5 tallos cuatro veces."),
        ex("Clasifica en MATERIAL, TÉCNICA o CUIDADO según Valle Alto: a) tejer b) fibras de junco c) dejar la mitad de cada mata.", "a técnica, b material, c cuidado", "Tejer es la técnica, el junco es el material y dejar la mitad es el cuidado."),
    ],
    Z=[
        ex("Ema recoge todo el junco de una mata «porque hay mucho». ¿Qué cuidado no respeta?", "Dejar la mitad de la mata", "La ficha pide dejar la mitad."),
        ex("¿Por qué no se recoge junco cuando está creciendo? A) para que la planta se recupere B) porque es más difícil de tejer", "A", "Es un cuidado del ciclo natural."),
    ],
    D=[
        arith("Una cestera recoge la mitad de los 12 tallos de cada una de 5 matas. ¿Cuántos tallos recoge en total?", "5*(12//2)", "Cada mata da 6 tallos y son 5 matas."),
        ex("Dos frases: 1) «La comunidad recoge solo lo necesario del junco» 2) «El junco es mágico». ¿Cuál sale de la ficha?", "La primera", "La ficha habla de cuidado, no de magia."),
    ],
    context=[ex("Tu curso quiere hacer cestos de papel inspirados en Valle Alto. ¿Qué cuidado puedes imitar con el papel? A) usar solo las tiras necesarias y reutilizar B) gastar muchas hojas", "A", "Es el mismo cuidado del recurso.")],
    selfcheck=[
        ex("Nombra los tres elementos para relacionar material, técnica y naturaleza.", "Material, técnica y cuidado", "Son los tres que se miran."),
        ex("Verdadero o falso: recolectar sin dejar nada es una relación armónica.", "Falso", "Armonía exige dejar que la naturaleza se recupere."),
        ex("¿Qué haces para conocer una técnica real? A) pregunto al educador tradicional B) la invento", "A", "Es la fuente."),
    ],
    task=T("Usa la ficha de Costa Clara: «" + REDES + "» Haz una tabla con cuatro filas: material, técnica, cuidado del mar y cómo se enseña. Escribe una frase que explique cómo esta técnica dialoga con el mar. Si quieres practicar, imita el anudado con dos hilos de lana o cordel en casa, con ayuda de una persona de tu casa y sin tijeras.",
           "Material: hilo resistente. Técnica: redes anudadas a mano. Cuidado: redes del tamaño justo y no pescar todos los días. Se enseña anudando junto a los mayores. Frase: la comunidad cuida el mar usando redes del tamaño justo y no pescando todos los días.",
           ["usa datos de la ficha", "relaciona técnica y cuidado de la naturaleza", "si practica, usa un material seguro"], ["tabla de cuatro filas", "frase explicativa"], ["agregar datos que la ficha no trae", "decir que la técnica es de todos"],
           "Pedir que muestre en la ficha cada dato; valorar que relacione la técnica con el cuidado."),
    reinforce="Subraya el cuidado de la ficha de Valle Alto y explica con una frase para qué sirve.",
    extend="Escribe un cuidado de la naturaleza que podrías aplicar en tu escuela al usar un material.",
)

L(
    OA11, 3,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a analizar las decisiones y resguardos de una comunidad sobre su arte: qué comparte y qué no, y por qué. Sirve para respetar el saber de la comunidad.",
    prior=["Sé relacionar material, técnica y naturaleza.", "Sé que algunos saberes se resguardan."],
    explain=[
        "Una comunidad toma decisiones sobre su arte: qué materiales usa, cuándo los recoge, quién enseña y qué se muestra a otras personas. Esas decisiones expresan sus valores, por ejemplo el cuidado de la naturaleza y el respeto a quienes guardan los saberes.",
        "Un resguardo es el cuidado para que algo no se use sin permiso. Algunos diseños, palabras o procesos pueden ser resguardados porque tienen un significado especial o porque solo corresponden a ciertas personas. Que un saber se resguarde no es un secreto malo: es una decisión de la comunidad que se respeta.",
        "Para analizar decisiones y resguardos, leemos la ficha y respondemos: ¿qué decide la comunidad?, ¿por qué podría decidirlo? y ¿qué parte no corresponde mostrar? Si no sabemos por qué, lo preguntamos al educador o educadora tradicional; no lo inventamos.",
    ],
    vocab=[("decisión", "elección que hace una persona o comunidad"), ("resguardo", "cuidado para que algo no se use sin permiso"), ("significado", "sentido que algo tiene para una comunidad"), ("valor", "idea que una comunidad considera importante"), ("consentimiento", "acuerdo claro de quien puede dar el permiso")],
    worked=[
        W("Analizar decisiones", "Lee: «" + CESTO + "» ¿Qué decisiones toma la comunidad y qué valor muestran?", ["No recoge junco cuando crece.", "Deja la mitad de cada mata.", "Muestran el cuidado de la naturaleza."], "Decide cuándo y cuánto recoger; muestra cuidado de la naturaleza."),
        W("Respetar un resguardo", "La ficha dice que los diseños reservados no se muestran. Un niño pregunta si puede dibujarlos. ¿Qué se responde?", ["El límite lo prohíbe.", "Es una decisión de la comunidad.", "Se respeta sin inventarlos."], "No: la comunidad decidió resguardarlos."),
    ],
    mistakes=[
        M("Pensar que un resguardo es un secreto malo.", "Es una decisión de cuidado de la comunidad.", "Respétalo sin insistir."),
        M("Inventar por qué la comunidad resguarda algo.", "Solo la comunidad puede decirlo.", "Escribe «la comunidad no lo cuenta» o pregunta."),
    ],
    R=[
        ex("En la ficha de Valle Alto, ¿qué diseños no se muestran?", "Los que la comunidad reserva", "El límite de la ficha lo dice."),
        ex("¿Quién decide qué se muestra de un arte: la comunidad o un visitante?", "La comunidad", "Es su saber."),
        ex("¿Es una decisión de cuidado no recoger junco cuando está creciendo? Responde Sí o No.", "Sí", "Cuida la planta."),
    ],
    C=[
        ex("¿Qué es un resguardo? A) cuidado para que algo no se use sin permiso B) un tipo de material", "A", "Es protección del saber."),
        ex("Verdadero o falso: se puede inventar la razón de un resguardo.", "Falso", "Solo la comunidad puede explicarla."),
        ex("Verdadero o falso: respetar un resguardo es respetar al portador del saber.", "Verdadero", "Es reconocer su decisión."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «No se pesca todos los días. No se cuentan las historias reservadas de la caleta». Escribe una decisión de cuidado y un resguardo.", "Cuidado: no pescar todos los días; resguardo: las historias reservadas", "Están en la ficha."),
        ex("Clasifica en DECISIÓN DE CUIDADO o RESGUARDO: a) dejar la mitad de cada mata b) no mostrar los diseños reservados.", "a decisión de cuidado, b resguardo", "La primera cuida la planta; la segunda protege un saber."),
        ex("Un compañero quiere sacar fotos de los diseños reservados «para estudiar». ¿Qué respondes? A) no, la comunidad los resguarda B) sí, solo una", "A", "El límite se respeta."),
    ],
    Z=[
        ex("Pedro dice: «Si la comunidad no muestra sus diseños, es porque no quiere enseñar». ¿Qué error comete?", "Supone una razón que la ficha no dice", "La razón la explica la comunidad."),
        ex("¿Qué haces si quieres saber por qué un diseño está resguardado? A) pregunto al educador tradicional B) busco en internet", "A", "Él es la guía de la comunidad."),
    ],
    D=[
        ex("Dos informes: uno dice «hay diseños que la comunidad no muestra» y otro dice «los diseños son feos y por eso no los muestran». ¿Cuál es respetuoso?", "El primero", "El segundo inventa una razón."),
        ex("Si una comunidad real da permiso para mostrar un diseño, ¿puedes cambiarlo y decir que es de la comunidad? Responde Sí o No.", "No", "Cambiarlo cambia lo que se autorizó."),
    ],
    context=[ex("En la feria de la escuela te preguntan por los diseños reservados de Valle Alto. ¿Qué respondes? A) esa parte no se cuenta B) te los dibujo de memoria", "A", "Es el límite de la ficha.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un resguardo.", "Cuidado para que algo no se use sin permiso", "Es la definición de la clase."),
        ex("Verdadero o falso: puedo cambiar un saber de una comunidad y decir que es suyo.", "Falso", "Se altera lo autorizado."),
        ex("¿Qué haces cuando algo está resguardado? A) lo respeto y no lo busco B) lo busco por otro lado", "A", "Se respeta el límite."),
    ],
    task=T("Lee las dos fichas inventadas: «" + CESTO + "» y «" + REDES + "» Haz una tabla de tres columnas: decisión de cuidado, resguardo y valor que muestra. Completa una fila por comunidad. Después escribe cómo explicarías a un compañero que no es un «secreto malo», usando dos oraciones.",
           "Valle Alto: cuidado: dejar la mitad de la mata; resguardo: diseños reservados; valor: cuidado de la naturaleza. Costa Clara: cuidado: no pescar todos los días; resguardo: historias reservadas de la caleta; valor: cuidado del mar. Explicación: Un resguardo es una decisión de cuidado de la comunidad. La comunidad decide qué se muestra y se respeta.",
           ["completa la tabla con datos de las fichas", "relaciona cada decisión con un valor", "explica el resguardo con respeto"], ["tabla de tres columnas", "dos oraciones"], ["inventar la razón del resguardo", "decir que es un secreto malo"],
           "Pedir que muestre en la ficha cada dato; valorar que respete el resguardo."),
    reinforce="Marca en la ficha de Valle Alto con un color las decisiones de cuidado y con otro el resguardo.",
    extend="Explica por qué cambiar un diseño autorizado y decir que es de la comunidad no es respetuoso.",
)

L(
    OA11, 4,
    materials="Lápiz, hojas de papel o cartulina y tijera de punta redondeada solo si una persona de tu casa te acompaña; también se puede rasgar el papel con las manos.",
    use="Aprenderé a responder de manera creativa a una técnica ancestral sin copiar lo que no corresponde. Sirve para crear algo propio, inspirado y respetuoso.",
    prior=["Sé reconocer origen, materiales y resguardos de una técnica.", "Sé que lo reservado no se copia."],
    explain=[
        "Responder creativamente es crear algo propio a partir de lo que aprendimos. Podemos inspirarnos en la idea de una técnica, por ejemplo entrelazar tiras, pero con materiales sencillos de la casa o de la escuela y un diseño nuestro. No es lo mismo que copiar el diseño de una comunidad.",
        "Una obra inspirada tiene tres rasgos: usa un material propio y seguro (como papel), tiene un diseño que inventamos nosotros y dice con claridad en qué se inspira y a quién reconoce. Escribimos, por ejemplo: «Inspirado en los cestos tejidos que cuenta la comunidad de Valle Alto (ficha de práctica)».",
        "No copiamos diseños resguardados ni decimos que nuestra obra es la técnica de la comunidad. Tampoco usamos materiales peligrosos ni dañamos la naturaleza. Mostramos la obra con humildad y, si es posible, la mostramos al educador o educadora tradicional para recibir su opinión.",
    ],
    vocab=[("inspirarse", "tomar una idea para crear algo propio"), ("copiar", "hacer algo igual a otra obra"), ("obra inspirada", "obra propia que reconoce en qué se inspiró"), ("reconocer", "decir públicamente a quién se debe una idea"), ("material seguro", "material que no es peligroso para quien lo usa")],
    worked=[
        W("Crear una obra inspirada", "Quieres hacer un tejido de papel inspirado en los cestos de Valle Alto (ficha inventada). ¿Qué haces?", ["Elijo papel y tiras que puedo rasgar o cortar con ayuda.", "Invento mi propio diseño de colores.", "Escribo: inspirado en los cestos tejidos de Valle Alto."], "Hago un tejido de papel con diseño propio y reconozco la inspiración."),
        W("Revisar si copié", "Un compañero me avisa que mi diseño se parece mucho a uno que la comunidad reserva. ¿Qué hago?", ["La ficha dice que ese diseño no se muestra.", "El mío podría copiarlo.", "Lo cambio y creo uno nuevo."], "Creo un diseño propio distinto del reservado."),
    ],
    mistakes=[
        M("Copiar un diseño de la comunidad «porque se ve lindo».", "Puede estar resguardado y tiene un significado.", "Crea un diseño propio."),
        M("No decir en qué te inspiraste.", "Parece que la idea es solo tuya.", "Escribe una nota de inspiración."),
    ],
    R=[
        ex("¿Una obra inspirada tiene un diseño propio o un diseño copiado?", "Un diseño propio", "Se inspira, no copia."),
        ex("¿Qué material seguro puedes usar para un tejido inspirado: papel o un vidrio roto?", "Papel", "El papel es seguro."),
        ex("¿Qué debe decir la nota de una obra inspirada: en qué se inspira o nada?", "En qué se inspira", "Es el reconocimiento."),
    ],
    C=[
        ex("¿Qué significa inspirarse? A) tomar una idea para crear algo propio B) copiar exactamente una obra", "A", "Inspirarse es crear algo nuevo."),
        ex("Verdadero o falso: puedo copiar un diseño resguardado si lo hago con papel.", "Falso", "El resguardo no depende del material."),
        ex("Verdadero o falso: una nota de inspiración reconoce a la comunidad.", "Verdadero", "Es dar crédito."),
    ],
    A=[
        ex("Escribe una nota de inspiración para un tejido de papel inspirado en Valle Alto (ficha inventada).", "Inspirado en los cestos tejidos que cuenta la comunidad de Valle Alto", "Debe nombrar a la comunidad."),
        arith("Para tu tejido de papel usas 6 tiras verticales y 6 horizontales. ¿Cuántas tiras usas en total?", "6+6", "Se suman las dos direcciones."),
        ex("Clasifica en COPIA o INSPIRACIÓN: a) hacer el mismo diseño reservado b) inventar un diseño propio con el mismo entrelazado de tiras.", "a copia, b inspiración", "La primera repite el diseño; la segunda crea uno nuevo."),
    ],
    Z=[
        ex("Lucas dice: «Mi tejido de papel es la técnica de Valle Alto». ¿Qué error comete?", "Presenta su obra como si fuera la técnica de la comunidad", "Su obra es inspirada, no la técnica de la comunidad."),
        ex("¿Por qué conviene mostrar tu obra a una persona de la comunidad si es posible? A) para escuchar su opinión B) para que la compre", "A", "La comunidad puede orientarte."),
    ],
    D=[
        ex("Dos notas: 1) «Inspirado en los cestos de Valle Alto (ficha inventada)» 2) «Técnica creada por mi curso». ¿Cuál es respetuosa?", "La primera", "Reconoce la inspiración."),
        ex("Tu compañera hace un diseño que se parece mucho a uno que sabes que es reservado. ¿Qué haces? A) le aviso con respeto y le propongo cambiarlo B) lo ignoro", "A", "Se evita copiar lo resguardado."),
    ],
    context=[ex("Para la feria de la escuela harás un tejido de papel. ¿Qué acompañará a tu obra? A) una nota de inspiración con la comunidad B) nada", "A", "Reconoce el origen de la idea.")],
    selfcheck=[
        ex("Nombra dos rasgos de una obra inspirada.", "Dos entre: material seguro, diseño propio, nota de inspiración", "Son los tres rasgos de la explicación."),
        ex("Verdadero o falso: copiar y inspirarse son lo mismo.", "Falso", "Inspirarse crea algo nuevo."),
        ex("¿Con qué materiales puedes practicar? A) papel y cordel con ayuda B) objetos filosos sin ayuda", "A", "Se eligen materiales seguros."),
    ],
    task=T("Crea un tejido de papel inspirado en los cestos de Valle Alto (ficha inventada). Usa 6 tiras de papel de un color y 6 de otro, que puedes rasgar con las manos o cortar con ayuda de una persona de tu casa. Entrelaza las tiras formando un cuadrado. Inventa tu propio diseño de colores y escribe una nota de inspiración. Anota cuántas tiras usaste en total.",
           "Tejido con 6 tiras azules y 6 amarillas entrelazadas: 6 + 6 = 12 tiras. Nota: inspirado en los cestos tejidos que cuenta la comunidad de Valle Alto (ficha inventada). Diseño propio de rayas.",
           ["crea un diseño propio", "escribe la nota de inspiración", "usa materiales seguros"], ["tejido de papel", "nota", "conteo de tiras"], ["copiar un diseño reservado", "no reconocer la inspiración"],
           "Pedir que explique en qué se inspiró y qué inventó; valorar el material seguro."),
    reinforce="Escribe tu nota de inspiración con una frase corta y clara.",
    extend="Muestra tu tejido a una persona de tu casa y registra una opinión suya en una línea.",
)

# ============================================================ OA 12 · Normas en eventos socioculturales y espirituales
L(
    OA12, 1,
    materials="Lápiz y hojas. La ficha del evento está escrita aquí y es inventada. No corresponde a ninguna ceremonia real.",
    use="Aprenderé a situar un evento sociocultural o espiritual y a reconocer qué significa para la comunidad. Sirve para participar con respeto y sin inventar.",
    prior=["Sé situar un territorio y una fuente.", "Sé que hay saberes que se resguardan."],
    explain=[
        "Un evento sociocultural es un momento en que una comunidad se junta con un propósito: celebrar, agradecer, recordar, decidir o compartir. Cuando el propósito tiene que ver con lo que la comunidad considera sagrado, hablamos de un evento espiritual. Cada comunidad tiene los suyos y los vive con su manera de entender el mundo.",
        "Para situar un evento preguntamos: ¿qué comunidad lo hace?, ¿quién lo cuenta?, ¿para qué se hace?, ¿qué significado tiene y qué parte no se cuenta? El significado lo explica la comunidad; nosotros no lo adivinamos viendo una foto o un video. Y no todos los eventos se pueden conocer ni participar en ellos.",
        "En esta clase usamos un evento inventado, el Encuentro del Agua de Valle Alto, solo para practicar. No es una ceremonia real de ningún pueblo. Sirve para aprender a leer una ficha de evento sin inventar nada más allá de lo que dice.",
    ],
    vocab=[("evento sociocultural", "momento en que una comunidad se junta con un propósito"), ("evento espiritual", "evento ligado a lo que la comunidad considera sagrado"), ("significado", "sentido que algo tiene para la comunidad"), ("propósito", "para qué se hace algo"), ("situar", "decir qué comunidad lo hace y quién lo cuenta")],
    worked=[
        W("Situar el evento", "Con la ficha: «" + EVENTO + "» ¿Qué comunidad lo hace, para qué y qué no se cuenta?", ["Comunidad: Valle Alto.", "Para qué: agradecer el agua de la vertiente.", "Límite: no se cuenta lo que se hace en el centro del círculo."], "Lo hace Valle Alto para agradecer el agua; no se cuenta lo del centro del círculo."),
        W("No adivinar", "Un niño dice: «En el centro del círculo se hace una danza». ¿Se puede decir?", ["La ficha dice que eso no se cuenta.", "La danza no aparece.", "No se puede afirmar."], "No, porque es parte del límite."),
    ],
    mistakes=[
        M("Imaginar qué ocurre en las partes que la comunidad no cuenta.", "Puede ser falso y faltar al respeto.", "Escribe «esa parte no se cuenta»."),
        M("Creer que un evento de práctica es una ceremonia real.", "Es un ejemplo inventado.", "Lee el rótulo de la ficha."),
    ],
    R=[
        ex("Según la ficha, ¿para qué se hace el Encuentro del Agua?", "Para agradecer el agua de la vertiente", "La ficha lo dice."),
        ex("¿Quién guía el encuentro según la ficha: una persona mayor elegida por la comunidad o un visitante?", "Una persona mayor elegida por la comunidad", "La ficha lo dice."),
        ex("¿Es el Encuentro del Agua una ceremonia real de un pueblo? Responde Sí o No.", "No", "Es un ejemplo inventado."),
    ],
    C=[
        ex("¿Qué es un evento espiritual? A) evento ligado a lo que la comunidad considera sagrado B) evento deportivo", "A", "La espiritualidad es lo sagrado para la comunidad."),
        ex("Verdadero o falso: puedo adivinar el significado de un evento mirando una foto.", "Falso", "El significado lo explica la comunidad."),
        ex("Verdadero o falso: todos los eventos de una comunidad están abiertos a cualquier persona.", "Falso", "Algunos son solo para la comunidad."),
    ],
    A=[
        ex("Escribe dos datos para situar el Encuentro del Agua.", "Dos entre: comunidad Valle Alto, fuente doña Rosa, propósito agradecer el agua, guía una persona mayor", "Están en la ficha."),
        ex("Une cada dato con su parte de la ficha. 1) agradecer el agua 2) lo del centro del círculo a) propósito b) límite", "1-a, 2-b", "La primera dice para qué; la segunda es lo que no se cuenta."),
        ex("Una niña dice: «Seguro tiene música». La ficha no menciona música. ¿Es una afirmación de la ficha? Responde Sí o No.", "No", "Es una suposición."),
    ],
    Z=[
        ex("Tomás escribe en su trabajo: «Todas las comunidades hacen un encuentro del agua». ¿Qué error comete?", "Generaliza un evento inventado a todas las comunidades", "Es un ejemplo de una sola comunidad."),
        ex("¿Por qué se declara en la ficha lo que no se cuenta? A) para respetar la decisión de la comunidad B) para que la ficha sea corta", "A", "Es un resguardo."),
    ],
    D=[
        ex("Dos frases: 1) «El Encuentro del Agua es para agradecer el agua» 2) «El Encuentro del Agua incluye una ceremonia con fuego». ¿Cuál sale de la ficha?", "La primera", "La segunda no aparece."),
        ex("Si quieres conocer el significado de un evento real de una comunidad, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a quien lo grabó", "A", "Ellos pueden explicar su sentido."),
    ],
    context=[ex("Un compañero quiere hacer un video del Encuentro del Agua inventado para ponerlo en internet. La ficha dice «no sacar fotos sin permiso». ¿Qué respondes? A) primero hay que pedir permiso B) hazlo igual", "A", "La norma lo pide.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un evento sociocultural.", "Momento en que una comunidad se junta con un propósito", "Es la definición de la clase."),
        ex("Verdadero o falso: el significado de un evento lo explica la comunidad.", "Verdadero", "Es la fuente."),
        ex("¿Qué haces con la parte que no se cuenta? A) la respeto B) la invento", "A", "Lo reservado no se inventa."),
    ],
    task=T("Lee esta ficha inventada: «Comunidad: Costa Clara. Evento: Encuentro del Mar (inventado, no es una ceremonia real). Fuente: don Luis. Para qué: la caleta se junta a agradecer la pesca. Quién guía: un pescador mayor elegido por la comunidad. Límite: no se cuenta lo que se dice al comienzo.» Completa una ficha con cinco partes: comunidad, fuente, propósito, quién guía y límite. Escribe una frase que diga qué no sabes y una pregunta para el educador tradicional.",
           "Comunidad: Costa Clara. Fuente: don Luis. Propósito: agradecer la pesca. Guía: un pescador mayor elegido. Límite: lo que se dice al comienzo. No sé qué se dice al comienzo. Pregunta: ¿qué eventos de nuestra comunidad se pueden conocer?",
           ["completa las cinco partes con datos de la ficha", "declara lo que no sabe", "formula una pregunta respetuosa"], ["ficha de cinco partes", "frase de límite", "pregunta"], ["inventar lo que se dice o hace en la parte reservada", "tomar el evento como real"],
           "Pedir que muestre en la ficha cada dato; valorar que deje en blanco lo no contado."),
    reinforce="Subraya el propósito y el límite en la ficha del Encuentro del Agua con colores distintos.",
    extend="Explica por qué la ficha de un evento debe decir qué comunidad lo hace y quién lo cuenta.",
)

L(
    OA12, 2,
    materials="Lápiz y hojas. La ficha y el discurso están escritos aquí y son inventados. No corresponden a ninguna ceremonia real.",
    use="Aprenderé a reconocer los roles y las normas de un evento, y el sentido de las palabras que se dicen en él. Sirve para participar con respeto en una reunión importante.",
    prior=["Sé situar un evento y reconocer su propósito.", "Sé que hay partes que no se cuentan."],
    explain=[
        "En un evento hay roles: quien guía, quienes participan y quienes visitan. Cada rol tiene su responsabilidad. Quien guía organiza y orienta; los participantes colaboran; los visitantes escuchan y respetan. Los roles los define la comunidad, no los inventamos desde afuera.",
        "Las normas son reglas de comportamiento que ayudan a cuidar el evento y a las personas. En el Encuentro del Agua inventado, las normas son: llegar a tiempo, saludar, escuchar en silencio y no sacar fotos sin permiso. Cada norma tiene un sentido: cuidar el respeto y el significado del momento.",
        "En un evento también hay discursos, es decir, palabras que se dicen con un propósito. Un discurso de práctica podría ser: «Bienvenidos a Valle Alto. Hoy agradecemos el agua. Escuchemos en silencio y compartamos lo que traemos». Aprendemos a mirar qué dice, a quién se dirige y qué norma enseña, sin copiarlo como si fuera real.",
    ],
    vocab=[("rol", "responsabilidad que tiene una persona en un evento"), ("norma", "regla de comportamiento"), ("discurso", "palabras que se dicen con un propósito"), ("participante", "persona que forma parte del evento"), ("visitante", "persona que asiste con permiso, sin ser de la comunidad")],
    worked=[
        W("Roles", "Lee: «" + EVENTO + "» ¿Qué rol tiene una persona mayor elegida por la comunidad?", ["La ficha dice que guía.", "Guiar es organizar y orientar.", "Los demás participan o visitan."], "Guía el encuentro."),
        W("Norma y sentido", "¿Qué sentido puede tener la norma «escuchar en silencio» en este encuentro?", ["Se agradece el agua.", "El silencio muestra respeto.", "Se dice como posible sentido, no como certeza."], "Mostrar respeto al momento, según la ficha."),
    ],
    mistakes=[
        M("Pensar que los visitantes pueden hacer lo que quieran.", "Las normas valen para todos.", "Cumple las normas de la ficha."),
        M("Repetir un discurso de práctica como si fuera de una comunidad real.", "Es inventado.", "Léelo solo como ejemplo."),
    ],
    R=[
        ex("¿Quién guía el Encuentro del Agua inventado?", "Una persona mayor elegida por la comunidad", "Lo dice la ficha."),
        ex("¿Se puede sacar fotos sin permiso en el encuentro? Responde Sí o No.", "No", "Es una de las normas."),
        ex(DISC + " ¿Qué se agradece: el agua o la lluvia de otro lugar?", "El agua", "El discurso dice que agradecen el agua."),
    ],
    C=[
        ex("¿Qué es una norma? A) regla de comportamiento B) tipo de comida", "A", "Es una regla."),
        ex("Verdadero o falso: los roles de un evento los define la comunidad.", "Verdadero", "Los define quien lo hace."),
        ex("Verdadero o falso: un discurso es una canción obligatoria.", "Falso", "Es palabras con un propósito."),
    ],
    A=[
        ex(DISC + " ¿Qué norma se menciona? A) escuchar en silencio B) correr por el centro", "A", "El discurso dice que escuchemos en silencio."),
        ex("Clasifica en ROL o NORMA: a) guiar el encuentro b) llegar a tiempo.", "a rol, b norma", "Guiar es una responsabilidad; llegar a tiempo es una regla."),
        ex(DISC + " ¿Qué se invita a compartir?", "Lo que cada uno trae", "El discurso lo dice."),
    ],
    Z=[
        ex("Lucía dice: «Como soy visitante, puedo entrar al centro del círculo». ¿Qué error comete?", "Ignora el límite de la ficha", "El centro del círculo no se cuenta ni se comparte."),
        ex(DISC + " ¿Qué se aprende sobre el sentido del encuentro? A) que se agradece el agua B) que hay una competencia", "A", "El discurso lo dice."),
    ],
    D=[
        ex("Un niño escribe un nuevo discurso con un saludo especial y dice que es el discurso real de Valle Alto. ¿Qué falla?", "Inventó algo y lo presentó como real", "El discurso es de práctica."),
        ex("Si quieres conocer las palabras reales de un evento, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a quien lo grabó", "A", "Ellos pueden compartirlas o no."),
    ],
    context=[ex("Vas de visita al Encuentro del Agua inventado. ¿Qué haces al llegar? A) saludo y escucho en silencio B) saco fotos de inmediato", "A", "Cumples las normas.")],
    selfcheck=[
        ex("Escribe dos normas del Encuentro del Agua inventado.", "Dos entre: llegar a tiempo, saludar, escuchar en silencio, no sacar fotos sin permiso", "Están en la ficha."),
        ex("Verdadero o falso: las normas valen para todos los asistentes.", "Verdadero", "Las normas cuidan el evento."),
        ex("¿Quién define los roles de un evento real? A) la comunidad B) los visitantes", "A", "Son decisiones de la comunidad."),
    ],
    task=T("Lee esta ficha inventada de Costa Clara: «Encuentro del Mar (inventado). Roles: un pescador mayor guía; las familias participan; las visitas escuchan. Normas: llegar con la marea baja, saludar, no hablar mientras habla quien guía, no sacar fotos sin permiso.» Haz una tabla de dos columnas: roles y normas. Escribe qué sentido podría tener una de las normas, diciendo que es una posibilidad y que la explicación real la da la comunidad.",
           "Roles: guía, familias, visitas. Normas: llegar con la marea baja, saludar, no hablar mientras habla quien guía, no sacar fotos sin permiso. Sentido posible: no hablar mientras habla quien guía podría mostrar respeto; la explicación real la da la comunidad.",
           ["completa la tabla con datos de la ficha", "propone un sentido como posibilidad", "reconoce que la comunidad lo explica"], ["tabla", "frase de sentido"], ["presentar su hipótesis como certeza", "inventar normas"],
           "Pedir que muestre en la ficha cada dato; valorar que diga que es una posibilidad."),
    reinforce="Subraya las normas con un color y los roles con otro en la ficha del Encuentro del Agua.",
    extend="Escribe en dos líneas cómo se aplicaría una de las normas en un acto de tu escuela.",
)

L(
    OA12, 3,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a analizar cómo se participa en un evento y qué se resguarda. Sirve para decidir con respeto cuándo y cómo participar.",
    prior=["Sé reconocer roles y normas.", "Sé que algunos eventos tienen partes que no se cuentan."],
    explain=[
        "Participar en un evento significa ser parte de él con un rol. No siempre se puede participar: a veces la comunidad invita, a veces el evento es solo para ella. La invitación y el consentimiento (acuerdo claro de quien puede darlo) son clave para participar.",
        "Los resguardos protegen lo que no corresponde mostrar: ciertas palabras, objetos o momentos. Si un evento tiene resguardos, no se graba, no se fotografía ni se cuenta lo que no se autorizó. Respetar un resguardo es una forma de cuidado hacia la comunidad.",
        "Al analizar un evento, miramos tres cosas: quién puede participar, cómo se pide permiso y qué se resguarda. Con eso decidimos nuestra manera de actuar. Cuando no hay invitación ni permiso, la decisión más respetuosa es observar desde la distancia o no asistir.",
    ],
    vocab=[("participar", "ser parte de un evento con un rol"), ("invitación", "aviso de la comunidad para que alguien asista"), ("consentimiento", "acuerdo claro de quien puede dar el permiso"), ("resguardo", "cuidado para no mostrar lo que no se autorizó"), ("distancia respetuosa", "mirar sin entrar ni grabar cuando no hay permiso")],
    worked=[
        W("Decidir si participar", "La ficha dice: «El Encuentro del Agua está abierto a visitas invitadas por la comunidad». Tú no tienes invitación. ¿Qué haces?", ["No tengo invitación.", "No tengo consentimiento.", "No participo ni grabo."], "No participo ni grabo; respeto la decisión."),
        W("Pedir permiso", "Quieres sacar una foto del encuentro. ¿Qué haces?", ["La norma lo prohíbe sin permiso.", "Pido permiso a la persona que guía o al educador.", "Si no hay permiso, no la saco."], "Pido permiso antes y no la saco si no me lo dan."),
    ],
    mistakes=[
        M("Participar porque «seguro nadie se enoja».", "No hay consentimiento.", "Espera invitación."),
        M("Grabar para «conservar» sin permiso.", "Puede revelar lo resguardado.", "Pide permiso y respeta la respuesta."),
    ],
    R=[
        ex("La ficha dice: «Pueden asistir las personas invitadas por la comunidad». ¿Qué necesitas para asistir: invitación o ganas de ir?", "Invitación", "La ficha pide invitación."),
        ex("Si no te dan permiso para grabar, ¿grabas igual? Responde Sí o No.", "No", "Se respeta la respuesta."),
        ex("¿Qué es el consentimiento: un acuerdo claro de quien puede darlo o una suposición?", "Un acuerdo claro de quien puede darlo", "Es la definición."),
    ],
    C=[
        ex("¿Qué es un resguardo en un evento? A) cuidado para no mostrar lo que no se autorizó B) un lugar de descanso", "A", "Es protección de lo no autorizado."),
        ex("Verdadero o falso: toda persona puede participar en cualquier evento de una comunidad.", "Falso", "Depende de la invitación y el permiso."),
        ex("Verdadero o falso: observar desde la distancia puede ser una forma de respeto.", "Verdadero", "Respeta cuando no hay permiso."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «Se puede observar desde la playa. No se entra al círculo. No se graba». Escribe qué sí se puede hacer.", "Observar desde la playa", "La ficha lo permite."),
        ex("Clasifica en PERMITIDO o NO PERMITIDO según esa ficha: a) observar desde la playa b) grabar.", "a permitido, b no permitido", "Lo dice la ficha."),
        ex("Quieres asistir a un evento real y no sabes si puedes. ¿Qué haces primero? A) preguntar al educador tradicional o a la comunidad B) ir igual", "A", "Ellos dan la invitación o el permiso."),
    ],
    Z=[
        ex("Camila dice: «Si no me invitan, igual puedo entrar porque no molesto». ¿Qué error comete?", "Ignora la necesidad de invitación y consentimiento", "El permiso lo da la comunidad."),
        ex("¿Por qué se resguardan ciertas partes de un evento? A) porque la comunidad decide cuidar su significado B) porque son aburridas", "A", "Es una decisión de cuidado."),
    ],
    D=[
        ex("Dos conductas: 1) pedir permiso para escuchar y aceptar la respuesta 2) grabar a escondidas. ¿Cuál es respetuosa?", "La primera", "Respeta el consentimiento."),
        ex("Si la comunidad dice «puedes observar, pero no grabar», ¿qué haces? A) observo y no grabo B) grabo un poco", "A", "Se respeta el permiso parcial."),
    ],
    context=[ex("Tu curso asistirá a una muestra pública organizada por una comunidad. ¿Cuál es la conducta respetuosa? A) seguir las normas y pedir permiso para fotos B) tomar fotos sin preguntar", "A", "Cumples normas y consentimiento.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es el consentimiento.", "Acuerdo claro de quien puede dar el permiso", "Es la definición de la clase."),
        ex("Verdadero o falso: puedo grabar un evento sin permiso si lo hago a escondidas.", "Falso", "Es una falta de respeto."),
        ex("¿Qué haces cuando no tienes invitación? A) no participo B) participo igual", "A", "Se respeta la decisión."),
    ],
    task=T("Lee esta ficha inventada de Valle Alto: «Encuentro del Agua (inventado). Pueden asistir las personas invitadas por la comunidad. No se graba ni se fotografía. Se puede conversar con la persona que guía después del encuentro.» Responde en una tabla con tres filas: quién puede participar, qué está prohibido y qué sí se puede hacer. Escribe un mensaje breve (dos oraciones) pidiendo permiso para asistir a un encuentro real de tu zona, dirigido al educador tradicional.",
           "Pueden asistir las personas invitadas. Prohibido: grabar y fotografiar. Se puede conversar con quien guía después. Mensaje: Estimado educador, ¿podría orientarnos sobre qué eventos de nuestra comunidad podemos conocer? Nos gustaría saber si el curso puede asistir y cómo debemos comportarnos. Gracias.",
           ["completa la tabla con datos de la ficha", "pide permiso con respeto", "no asume que puede asistir"], ["tabla de tres filas", "mensaje de dos oraciones"], ["asumir que puede asistir", "pedir que se cuente lo resguardado"],
           "Pedir que muestre en la ficha cada dato; valorar el tono respetuoso."),
    reinforce="Subraya en la ficha lo que está prohibido y lo que está permitido con colores distintos.",
    extend="Escribe una regla de tres puntos para tu curso al visitar un evento comunitario.",
)

L(
    OA12, 4,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a comunicar lo que aprendí de un evento sin reproducir lo restringido. Sirve para informar con respeto y precisión.",
    prior=["Sé reconocer roles, normas, participación y resguardos.", "Sé que lo que no se autoriza no se cuenta."],
    explain=[
        "Comunicar sobre un evento significa contarlo a otras personas. Para hacerlo con respeto, separamos tres tipos de información: lo público (lo que la comunidad autorizó compartir), lo que desconocemos y lo restringido (lo que la comunidad reserva). Solo contamos lo primero.",
        "Un buen texto sobre un evento nombra la comunidad y la fuente, dice el propósito y las normas autorizadas, y declara que hay partes que no se cuentan. No describe lo que no vimos, no inventa y no usa palabras o gestos de una comunidad como si fueran nuestros.",
        "También conviene pedir a la comunidad o al educador tradicional que revise el texto antes de compartirlo. Si algo no les parece, se corrige. Así el texto es respetuoso y verdadero. Un texto breve y claro vale más que uno largo con datos inventados.",
    ],
    vocab=[("público", "lo que la comunidad autorizó compartir"), ("restringido", "lo que la comunidad reserva"), ("autorizar", "dar permiso para compartir algo"), ("revisar", "mirar con cuidado para corregir"), ("informar", "contar con claridad lo que se sabe")],
    worked=[
        W("Separar información", "Lee: «" + EVENTO + "» ¿Qué es público y qué es restringido?", ["Público: se agradece el agua, hay normas y guía.", "Restringido: lo que se hace en el centro del círculo.", "Desconocido: cuánto dura."], "Público: propósito y normas; restringido: lo del centro; desconocido: la duración."),
        W("Escribir un párrafo", "Escribe un párrafo corto y respetuoso sobre el evento.", ["Nombro la comunidad y la fuente.", "Digo el propósito y dos normas.", "Declaro que hay partes que no se cuentan."], "«Según doña Rosa, en Valle Alto (comunidad inventada) hay un encuentro para agradecer el agua. Hay normas como escuchar en silencio. Hay partes que la comunidad no cuenta.»"),
    ],
    mistakes=[
        M("Contar lo restringido porque «es interesante».", "Se falta al respeto a la comunidad.", "Cuenta solo lo autorizado."),
        M("Escribir un texto sin nombrar la fuente.", "No se sabe de dónde salen los datos.", "Nombra la comunidad y la persona."),
    ],
    R=[
        ex("¿Qué tipo de información se puede contar de un evento: la pública o la restringida?", "La pública", "La restringida no se cuenta."),
        ex("En la ficha del Encuentro del Agua, ¿qué no se cuenta?", "Lo que se hace en el centro del círculo", "Es el límite."),
        ex("¿Cuántos tipos de información se separan en esta clase? Escribe el número.", "3", "Son público, desconocido y restringido."),
    ],
    C=[
        ex("¿Qué es la información restringida? A) la que la comunidad reserva B) la que se publica", "A", "No corresponde compartirla."),
        ex("Verdadero o falso: un buen texto sobre un evento nombra la fuente.", "Verdadero", "Así se sabe de dónde salen los datos."),
        ex("Verdadero o falso: si no sé algo, lo invento para completar.", "Falso", "Se declara que no se sabe."),
    ],
    A=[
        ex("Clasifica en PÚBLICO, DESCONOCIDO o RESTRINGIDO según la ficha: a) se agradece el agua b) lo del centro del círculo c) cuánto dura el encuentro.", "a público, b restringido, c desconocido", "Lo primero está autorizado, lo segundo se reserva y lo tercero no se sabe."),
        ex("Escribe una frase que nombre la fuente: «___ cuenta que en Valle Alto hay un encuentro para agradecer el agua». Completa con el nombre.", "Doña Rosa", "Es la fuente de la ficha."),
        ex("¿Qué agregas al final de un texto respetuoso sobre el evento? A) que hay partes que no se cuentan B) detalles inventados", "A", "Declara el límite."),
    ],
    Z=[
        ex("Felipe escribió que en el centro se hace un baile, aunque la ficha no lo dice. ¿Qué falla?", "Inventó una parte restringida", "No se puede afirmar."),
        ex("¿Por qué conviene que la comunidad revise el texto? A) para corregir errores y cuidar lo reservado B) para que lo apruebe una nota", "A", "Ellos conocen su evento."),
    ],
    D=[
        ex("Dos textos: 1) «Hay un encuentro para agradecer el agua y no sé qué más hacen» 2) «En el encuentro hay una danza especial». ¿Cuál es respetuoso con la ficha?", "El primero", "El segundo inventa."),
        ex("Si la comunidad te autoriza a escribir sobre el evento, pero te pide no incluir una parte, ¿qué haces? A) la dejo fuera B) la incluyo con otras palabras", "A", "Se respeta el permiso parcial."),
    ],
    context=[ex("Tu curso hará un afiche del Encuentro del Agua inventado. ¿Qué incluye? A) propósito, normas y una nota de límites B) lo que ocurre en el centro", "A", "Lo restringido no se incluye.")],
    selfcheck=[
        ex("Nombra los tres tipos de información que se separan.", "Público, desconocido y restringido", "Son los de la clase."),
        ex("Verdadero o falso: se puede contar lo restringido si es interesante.", "Falso", "Se respeta el resguardo."),
        ex("¿A quién pides revisar tu texto? A) a la comunidad o al educador tradicional B) a nadie", "A", "Ellos conocen su evento y corrigen."),
    ],
    task=T("Usa la ficha del Encuentro del Mar de Costa Clara: «Fuente: don Luis. Para qué: agradecer la pesca. Guía: un pescador mayor. Normas: saludar, escuchar a quien guía. Límite: no se cuenta lo que se dice al comienzo.» Escribe un párrafo de cuatro oraciones que nombre la fuente, el propósito y dos normas, y que declare un límite. Después clasifica cada dato en público, desconocido o restringido.",
           "Según don Luis, en Costa Clara (comunidad inventada) hay un encuentro para agradecer la pesca. Lo guía un pescador mayor. Hay normas como saludar y escuchar. Hay una parte que no se cuenta. Público: propósito y normas. Restringido: lo del comienzo. Desconocido: cuánto dura.",
           ["nombra la fuente", "incluye propósito y dos normas", "declara el límite y clasifica"], ["párrafo de cuatro oraciones", "clasificación de datos"], ["incluir lo restringido", "inventar detalles"],
           "Pedir que señale la línea de la ficha de cada dato; valorar que deje el límite sin completar."),
    reinforce="Reescribe una frase de tu párrafo para que suene más clara y respetuosa.",
    extend="Escribe un mensaje breve para pedir a un educador tradicional que revise tu texto.",
)

L(
    OA12, 5,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a aplicar lo aprendido en una condición diferente: otro evento, otra comunidad, otra fuente. Sirve para comprobar que mi forma de respetar normas funciona en nuevos casos.",
    prior=["Sé situar, reconocer roles y normas, analizar participación y comunicar sin reproducir lo restringido.", "Sé que cada comunidad es distinta."],
    explain=[
        "Transferir es usar lo que aprendimos en una situación nueva. Hasta ahora estudiamos eventos de práctica de Valle Alto y Costa Clara. Ahora aplicamos los mismos pasos a una tercera ficha, de una comunidad inventada distinta, para comprobar que sabemos qué buscar sin copiar las respuestas.",
        "Los pasos son: situar el evento (comunidad, fuente, propósito), reconocer roles y normas, analizar la participación y los resguardos, y comunicar sin reproducir lo restringido. Si una norma coincide con otra comunidad, no se asume: se comprueba en la ficha. Cada comunidad tiene sus normas.",
        "También cambia la condición: por ejemplo, el evento ocurre en una ciudad y no en el campo, o hay una visita de otra escuela. Las normas del evento no cambian por eso: las define la comunidad. Lo que cambia es nuestra preparación para cumplirlas.",
    ],
    vocab=[("transferir", "usar lo aprendido en una situación nueva"), ("condición diferente", "situación en la que cambia el lugar, las personas o el momento"), ("coincidir", "ser igual en algo"), ("preparación", "acciones previas para llegar bien a un evento"), ("comprobar", "revisar que algo es cierto")],
    worked=[
        W("Aplicar los pasos", "Ficha inventada de la comunidad Llano Verde: «Evento: Encuentro de Siembra (inventado). Fuente: don Pedro. Para qué: compartir las semillas. Guía: una persona mayor. Normas: saludar, no pisar el terreno marcado, no grabar. Límite: no se cuenta quién recibe las semillas especiales.» Aplica los pasos.", ["Situar: Llano Verde, don Pedro, compartir semillas.", "Roles y normas: guía una persona mayor; saludar, no pisar el terreno marcado, no grabar.", "Resguardos: quién recibe las semillas especiales."], "Es un evento de Llano Verde para compartir semillas; no se graba y no se cuenta quién recibe las especiales."),
        W("No asumir", "Una niña dice: «En Llano Verde también se escucha en silencio, como en Valle Alto». ¿Es válido?", ["Reviso la ficha de Llano Verde.", "No menciona escuchar en silencio.", "No puedo afirmarlo."], "No, porque la ficha no lo dice."),
    ],
    mistakes=[
        M("Copiar las normas de Valle Alto al evento de Llano Verde.", "Cada comunidad define las suyas.", "Lee la ficha nueva."),
        M("Pensar que si el evento ocurre en una ciudad las normas cambian.", "Las normas las define la comunidad.", "Cumple las mismas normas de la ficha."),
    ],
    R=[
        ex("Según la ficha de Llano Verde, ¿para qué es el Encuentro de Siembra?", "Para compartir las semillas", "La ficha lo dice."),
        ex("¿Se puede grabar el encuentro de Llano Verde? Responde Sí o No.", "No", "Una norma lo prohíbe."),
        ex("¿Quién es la fuente de la ficha de Llano Verde: don Pedro o doña Rosa?", "Don Pedro", "La ficha lo nombra."),
    ],
    C=[
        ex("¿Qué es transferir? A) usar lo aprendido en una situación nueva B) repetir sin pensar", "A", "Es aplicar lo aprendido en otro caso."),
        ex("Verdadero o falso: las normas de Valle Alto sirven para todas las comunidades.", "Falso", "Cada comunidad define las suyas."),
        ex("Verdadero o falso: si el evento ocurre en una ciudad, las normas de la ficha ya no valen.", "Falso", "Las define la comunidad, no el lugar."),
    ],
    A=[
        ex("Escribe dos normas del Encuentro de Siembra de Llano Verde.", "Dos entre: saludar, no pisar el terreno marcado, no grabar", "Están en la ficha."),
        ex("Clasifica en PÚBLICO o RESTRINGIDO según la ficha de Llano Verde: a) el propósito de compartir semillas b) quién recibe las semillas especiales.", "a público, b restringido", "El propósito se cuenta; lo otro no."),
        ex("Un curso visita el encuentro de Llano Verde desde otra ciudad. ¿Qué debe cumplir? A) las normas de la ficha de Llano Verde B) las de Valle Alto", "A", "Valen las normas de esa comunidad."),
    ],
    Z=[
        ex("Ignacio escribe: «En Llano Verde se agradece el agua». ¿Qué falla?", "Toma el propósito de otra ficha", "La ficha de Llano Verde habla de compartir semillas."),
        ex("¿Por qué se compara sin jerarquizar? A) porque ninguna comunidad es mejor que otra B) porque es difícil", "A", "Cada comunidad vale por igual."),
    ],
    D=[
        ex("Dos frases: 1) «Valle Alto y Llano Verde tienen normas distintas» 2) «Llano Verde tiene mejores normas». ¿Cuál es válida?", "La primera", "La segunda jerarquiza."),
        ex("Tienes que preparar una visita a un evento real. ¿Cuál es la mejor primera acción? A) consultar al educador tradicional o a la comunidad B) buscar fotos", "A", "Ellos orientan a quienes visitan."),
    ],
    context=[ex("Tu curso asiste a una muestra pública de una comunidad en una ciudad. ¿Qué haces? A) preguntar qué normas rigen y cumplirlas B) asumir que valen las de la sala", "A", "La norma la define la comunidad.")],
    selfcheck=[
        ex("Nombra los cuatro pasos para estudiar un evento.", "Situar, roles y normas, participación y resguardos, comunicar", "Son los pasos de la clase."),
        ex("Verdadero o falso: puedo copiar las normas de una ficha a otra.", "Falso", "Cada ficha tiene las suyas."),
        ex("¿Qué haces con lo restringido? A) lo respeto B) lo busco", "A", "Se respeta el límite."),
    ],
    task=T("Lee la ficha inventada de Llano Verde y aplica los cuatro pasos: 1) situar (comunidad, fuente, propósito), 2) roles y normas, 3) participación y resguardos, 4) un párrafo breve respetuoso. Agrega una frase que compare con el Encuentro del Agua de Valle Alto sin decir cuál es mejor. Ficha: «Comunidad: Llano Verde. Evento: Encuentro de Siembra (inventado). Fuente: don Pedro. Para qué: compartir las semillas. Guía: una persona mayor. Normas: saludar, no pisar el terreno marcado, no grabar. Límite: no se cuenta quién recibe las semillas especiales.»",
           "Situar: Llano Verde, don Pedro, compartir semillas. Roles y normas: guía una persona mayor; saludar, no pisar el terreno marcado, no grabar. Participación y resguardos: no se cuenta quién recibe las semillas especiales. Párrafo: Según don Pedro, en Llano Verde hay un encuentro para compartir semillas. Hay normas como saludar. Hay partes que no se cuentan. Comparación: ambos encuentros tienen guía y normas, pero con propósitos distintos.",
           ["aplica los cuatro pasos con datos de la ficha", "respeta el límite", "compara sin jerarquizar"], ["cuatro pasos escritos", "párrafo", "frase comparativa"], ["copiar normas de otra ficha", "jerarquizar comunidades"],
           "Pedir que muestre en la ficha cada dato; valorar que compare sin jerarquía."),
    reinforce="Escribe qué norma de Valle Alto no puedes usar para Llano Verde y por qué.",
    extend="Explica cómo te prepararías para cumplir las normas de un evento real en una ciudad.",
)
