"""Student material for 1.º medio Música, OA 05 (improvisar y crear música dando énfasis a la experimentación con el material sonoro, arreglos de canciones y secciones musicales, basándose en ideas musicales y extramusicales).

Todas las fichas, melodías y arreglos de los ejercicios son inventados («de ejemplo»); los materiales son objetos cotidianos seguros, sin vidrio, filos ni fuego.
"""
from __future__ import annotations

from student_content_mu_m1_a import L
from student_lessons import arith, ex

OA5 = "MU1M OA 05"

OBJ = ("Objetos de ejemplo y su sonido: caja de cartón, golpe seco, grave y corto; hoja de papel, roce suave, agudo y largo; "
       "tapa de plástico sobre la mesa, golpe claro, medio y corto; botella plástica con arroz, agitada, sonido de granos, largo y continuo; "
       "cuchara de madera sobre una mesa, golpe seco, agudo y corto")

# ---------------------------------------------------------------- OA 05 · clase 1 (material sonoro y motivo)
L(
    OA5, 1,
    f"Lápiz y papel; si quieres probar, objetos cotidianos seguros (caja de cartón, hoja de papel, tapa de plástico, botella plástica con arroz, cuchara de madera) y volumen bajo. Fichas de ejemplo, que se repiten en los ejercicios: {OBJ}.",
    "Aprenderé a experimentar con el material sonoro (voz, cuerpo y objetos), a describir sus rasgos y a armar un motivo, que es una idea musical breve que se puede repetir y variar. Sirve para comenzar a crear música a partir de sonidos que ya tengo a mano.",
    ["Sé reconocer timbre, duración y volumen.", "Sé qué es la repetición y la variación.", "Sé marcar un pulso con palmas."],
    [
        "El material sonoro es todo lo que se puede usar para hacer música: la voz, el cuerpo (palmas, chasquidos, pasos suaves), los instrumentos y los objetos cotidianos. Experimentar es probar con curiosidad cómo suena cada cosa. Para registrar lo que se descubre, se describe cada sonido con cuatro rasgos: el timbre (seco, claro, suave, de granos), la altura (grave, medio o agudo), la duración (corto, largo o continuo) y la intensidad (suave o fuerte).",
        "Con esos sonidos se arma un motivo: una idea musical breve, de tres a seis sonidos, que se puede repetir y variar. Por ejemplo, un motivo con caja de cartón, caja de cartón, papel y tapa. Se puede variar cambiando el orden, el instrumento, la duración o la intensidad, pero conservando algo que lo hace reconocible. Un motivo que se repite sin cambios cansa; uno que cambia todo se pierde. El equilibrio entre repetir y variar da forma a la música.",
        "Al experimentar se cuida la seguridad: se usan objetos livianos, sin vidrio ni filos, con volumen bajo para no dañar los oídos y sin molestar a otras personas. Para crear con otros, se acuerda quién prueba, quién escucha y quién anota. Registrar el motivo con una frase o dibujo permite repetirlo mañana: «caja, caja, papel, tapa», o bien con líneas cortas y largas.",
    ],
    [("material sonoro", "voz, cuerpo, instrumentos u objetos que se usan para hacer sonidos"), ("experimentar", "probar con curiosidad cómo suena algo"), ("timbre", "color del sonido de cada fuente"), ("motivo", "idea musical breve que se puede repetir y variar"), ("variar", "cambiar algo de un motivo, conservando una parte")],
    [
        ("Describir un sonido", f"{OBJ}. Describe el sonido de la caja de cartón con cuatro rasgos.", ["Timbre: seco.", "Altura: grave.", "Duración: corta.", "Intensidad: la que usemos al golpear."], "Seco, grave y corto; la intensidad depende de cómo se golpee"),
        ("Armar un motivo", f"{OBJ}. Arma un motivo de cuatro sonidos con contraste de altura entre el primero y el tercero.", ["Elegir un sonido grave: caja.", "Elegir uno agudo: papel o cuchara.", "Ordenar: caja, tapa, papel, tapa."], "Por ejemplo: caja, tapa, papel, tapa"),
    ],
    [
        ("Usar objetos frágiles o con filo para «sonar mejor».", "Pueden causar daño; la creatividad no necesita riesgo.", "Elige objetos livianos y seguros."),
        ("Repetir el motivo sin cambiar nada, o cambiarlo por completo.", "Sin variación cansa; sin repetición no hay motivo reconocible.", "Conserva una parte y cambia otra."),
    ],
    [
        ex(f"{OBJ}. ¿Qué sonido es continuo: la botella con arroz agitada o la cuchara de madera?", "La botella con arroz agitada", "Los granos suenan de manera sostenida, y la cuchara da un golpe corto."),
        ex(f"{OBJ}. ¿Qué objeto produce el sonido más grave?", "La caja de cartón", "La ficha la describe como grave."),
        ex("¿Cuál de los siguientes materiales NO es seguro para experimentar con sonidos? Un vaso de vidrio, una caja de cartón o una hoja de papel.", "Un vaso de vidrio", "El vidrio se puede romper y cortar."),
    ],
    [
        ex("¿Qué es un motivo? A) Una idea musical breve que se puede repetir y variar. B) Una canción completa de varias estrofas.", "A", "Es la unidad pequeña a partir de la cual se arma una pieza."),
        ex(f"{OBJ}. ¿Qué objeto sirve para un sonido agudo, corto y seco? A) La cuchara de madera sobre una mesa. B) La caja de cartón.", "A", "La caja es grave; la cuchara es aguda."),
        ex("Un motivo se repite 8 veces sin ningún cambio y el grupo lo siente aburrido. ¿Qué conviene? A) Variar una parte, como el orden o la intensidad. B) Subir el volumen sin cambiar nada.", "A", "La variación mantiene el interés sin perder el motivo."),
    ],
    [
        arith("Un motivo tiene 4 sonidos y se toca 6 veces seguidas, uno por pulso. ¿Cuántos pulsos suenan?", "4*6", "Se multiplican los sonidos por las veces que se repite.", " pulsos"),
        ex(f"{OBJ}. Un motivo es: caja, caja, papel, tapa. Se varía cambiando solo el tercer sonido por la cuchara. ¿Cuál es el motivo variado?", "Caja, caja, cuchara, tapa", "Se reemplaza el tercer sonido y se conservan los demás."),
        ex(f"{OBJ}. Un motivo usa caja, papel y botella con arroz. ¿Cuántos timbres distintos hay?", "3", "Cada objeto tiene un timbre propio."),
    ],
    [
        ex("Un grupo prueba un motivo con tres sonidos. Después de variarlo, solo conservó el ritmo, pero cambió todos los sonidos y la intensidad. Otra persona dice que ya no se reconoce el motivo. ¿Por qué? A) Porque cambió casi todo lo que lo hacía reconocible. B) Porque se repitió demasiado.", "A", "Si solo se conserva una parte pequeña, es difícil reconocerlo."),
        ex("Una frase de ejemplo tiene 8 pulsos: un motivo de 4 pulsos y luego su variación de 4 pulsos. Si la frase completa se toca 3 veces seguidas, ¿cuántas veces suena el motivo original?", "3", "Cada frase tiene un motivo original y una variación, así que el original suena una vez por frase."),
    ],
    [
        arith("En el patio del liceo cuatro estudiantes crean un motivo de 5 sonidos y lo repiten 3 veces cada uno. ¿Cuántos sonidos tocan en total entre los cuatro?", "4*5*3", "Se multiplican personas, sonidos y repeticiones.", " sonidos"),
        ex("Un grupo usa objetos con el volumen bajo para no molestar. Uno propone golpear con fuerza una tapa de olla de metal contra el piso. ¿Es una buena idea? Responde sí o no.", "No", "Un volumen muy alto puede dañar el oído y molestar a otras personas."),
    ],
    [ex(f"{OBJ}. Quieres un motivo que suene suave y largo para una escena tranquila. ¿Qué objeto eliges? A) La hoja de papel, con roce suave. B) La cuchara de madera sobre una mesa.", "A", "El papel produce un sonido suave y largo.")],
    [ex("¿Cuántos rasgos usamos para describir un sonido?", "Cuatro", "Son timbre, altura, duración e intensidad."), ex("¿Qué se puede cambiar en una variación?", "El orden, el instrumento, la duración o la intensidad", "Se conserva una parte del motivo."), ex("¿Por qué se usa volumen bajo al experimentar?", "Para no dañar los oídos ni molestar", "Se cuida la salud auditiva y a las demás personas.")],
    (
        "Con las fichas de objetos de ejemplo (caja, papel, tapa, botella con arroz, cuchara), crea un motivo de cuatro sonidos. Escribe: a) tu motivo en palabras (por ejemplo «caja, tapa, papel, tapa»), b) dos rasgos de cada sonido que uses, c) una variación en la que cambies solo un sonido, d) una regla de seguridad que cumplirás.",
        "a) Caja, tapa, papel, tapa. b) Caja: grave y corta; tapa: media y corta; papel: aguda y larga. c) Caja, tapa, cuchara, tapa. d) Volumen bajo y objetos sin vidrio ni filos.",
        ["motivo de cuatro sonidos con objetos de las fichas", "describe rasgos según las fichas", "la variación cambia solo un sonido"],
        ["motivo y variación escritos", "regla de seguridad"],
        ["variar todo a la vez", "usar objetos peligrosos"],
        "Reconoce el motivo y pide explicar qué parte se conservó para que siga siendo reconocible.",
    ),
    "Prueba tres sonidos con tu cuerpo (palma, chasquido, golpe suave en el muslo) y descríbelos con cuatro rasgos.",
    "Crea otro motivo de cinco sonidos con tu voz y tu cuerpo y varíalo dos veces.",
)

# ---------------------------------------------------------------- OA 05 · clase 2 (ideas extramusicales)
IDEAS = ("Idea 1 (de ejemplo): lluvia que empieza suave y se hace fuerte. Idea 2: un mercado lleno de gente. Idea 3: el mar en calma. "
         "Decisiones posibles: golpes cortos y agudos; sonidos largos y suaves; ritmo irregular con muchos timbres; volumen que crece poco a poco")
L(
    OA5, 2,
    f"Lápiz y papel; objetos cotidianos seguros si quieres probar. Ideas de ejemplo, que se repiten en los ejercicios: {IDEAS}.",
    "Aprenderé a partir de ideas extramusicales (imágenes, historias, emociones o lugares) para tomar decisiones musicales concretas, y a explicar la relación. Sirve para improvisar y crear con una intención clara y no al azar.",
    ["Sé describir sonidos con cuatro rasgos.", "Sé armar y variar un motivo.", "Sé relacionar rasgos con un propósito."],
    [
        "Una idea musical es algo propio de la música, como un ritmo, una melodía, un motivo o un cambio de volumen. Una idea extramusical viene de fuera de la música: una imagen (la lluvia), una historia (un viaje), una emoción (nostalgia) o un lugar (una plaza). Los compositores y compositoras suelen partir de una idea extramusical y la traducen en decisiones musicales: qué ritmo, qué timbre, qué altura, qué volumen y qué cambios en el tiempo.",
        "Traducir es relacionar. La lluvia suave puede ser golpes cortos y agudos con volumen bajo; si se vuelve tormenta, los golpes se multiplican y el volumen crece poco a poco. Un mercado lleno de gente puede ser un ritmo irregular con muchos timbres distintos. El mar en calma puede ser sonidos largos y suaves que suben y bajan. Cada decisión se explica con una frase: «uso golpes cortos porque la lluvia cae en gotas».",
        "Lo importante es que otra persona pueda reconocer la relación entre la idea y lo que suena. No hay una sola traducción correcta: varias personas pueden representar la lluvia de maneras distintas, y todas valen si se justifican con lo que se oye. Para mejorar, se escucha la creación, se pregunta qué imagen sugiere y se comprueba si coincide con la idea original.",
    ],
    [("idea musical", "idea propia de la música: ritmo, melodía, motivo o cambio de volumen"), ("idea extramusical", "idea que viene de fuera de la música: imagen, historia, emoción o lugar"), ("traducir", "convertir una idea en decisiones musicales concretas"), ("representar", "hacer que un sonido sugiera algo"), ("justificar", "explicar una decisión con una razón")],
    [
        ("Traducir una imagen", f"{IDEAS}. ¿Qué decisiones sirven para la idea 1, lluvia que empieza suave y se hace fuerte?", ["Empieza suave y crece: volumen que crece poco a poco.", "La lluvia cae en gotas: golpes cortos y agudos."], "Golpes cortos y agudos, y volumen que crece poco a poco"),
        ("Justificar", f"{IDEAS}. Escribe una frase que justifique sonidos largos y suaves para la idea 3.", ["El mar en calma no tiene golpes bruscos.", "Los sonidos largos y suaves se parecen al vaivén."], "Uso sonidos largos y suaves porque el mar en calma se mueve despacio"),
    ],
    [
        ("Creer que solo hay una traducción correcta de una idea.", "Varias traducciones pueden valer si se justifican con lo que se oye.", "Explica tu decisión con «porque»."),
        ("Elegir los sonidos al azar y decir después qué representan.", "La idea guía las decisiones desde el comienzo.", "Primero la idea, luego los sonidos."),
    ],
    [
        ex("¿Una lluvia es una idea musical o una idea extramusical?", "Extramusical", "Viene de fuera de la música: es una imagen."),
        ex("¿Un cambio gradual de volumen suave a fuerte es una idea musical o una idea extramusical?", "Musical", "Es un cambio de volumen, propio de la música."),
        ex(f"{IDEAS}. ¿Qué decisión sirve para la idea 2, un mercado lleno de gente?", "Ritmo irregular con muchos timbres", "Un mercado tiene muchos sonidos distintos, sin un orden regular."),
    ],
    [
        ex(f"{IDEAS}. ¿Qué conviene para la idea 3, el mar en calma? A) Sonidos largos y suaves. B) Golpes cortos y agudos.", "A", "El mar en calma se mueve despacio y suave."),
        ex("¿Qué es traducir una idea extramusical? A) Convertirla en decisiones musicales concretas. B) Escribirla en otro idioma.", "A", "En música, traducir es relacionar una idea con ritmo, timbre, altura y volumen."),
        ex("Una estudiante dice «mi lluvia es mejor que la tuya». ¿Qué respuesta corresponde? A) Ambas pueden valer si cada una se justifica con lo que se oye. B) Solo vale la de quien habla más fuerte.", "A", "Existen varias traducciones válidas de una misma idea."),
    ],
    [
        arith("Una lluvia de ejemplo tiene 3 tramos de 8 pulsos cada uno: suave, media y fuerte. ¿Cuántos pulsos dura la lluvia completa?", "3*8", "Se multiplican los tramos por los pulsos de cada tramo.", " pulsos"),
        ex(f"{IDEAS}. Un grupo representa el mercado con un ritmo muy regular y un solo timbre. ¿Qué rasgos de la idea 2 no logra transmitir? A) La variedad de sonidos y el desorden. B) El volumen creciente.", "A", "Un mercado tiene muchos sonidos distintos y desorden."),
        ex("Una estudiante quiere representar «una tarde de espera» con sonidos. ¿Qué decisiones se relacionan mejor? A) Pulso lento, sonidos largos y pausas. B) Ritmo muy rápido y fuerte.", "A", "La espera se sugiere con calma y pausas."),
    ],
    [
        ex(f"{IDEAS}. Para la idea 1, la lluvia se hace tormenta en el tramo final. ¿Qué decisión de volumen conviene en ese tramo?", "Volumen fuerte", "La tormenta es la parte más intensa de la lluvia."),
        arith("Una escena de ejemplo tiene 4 tramos de 6 pulsos: calma, inquietud, tormenta y calma. ¿Cuántos pulsos hay entre el inicio de la inquietud y el final de la tormenta?", "2*6", "Los tramos 2 y 3 suman 12 pulsos.", " pulsos"),
    ],
    [
        ex("Una profesora pide una música que represente una despedida. Un grupo propone un ritmo muy rápido y estruendoso. Otro grupo propone sonidos lentos y suaves con pausas. ¿Cuál sugiere mejor una despedida emotiva? A) El segundo grupo. B) El primero.", "A", "Lo lento y suave con pausas transmite emoción tranquila."),
        arith("Un grupo de 5 estudiantes crea una escena de 4 tramos y cada estudiante hace sonidos en 2 tramos distintos. ¿Cuántos «turnos» de sonido hay en total?", "5*2", "Se multiplican los estudiantes por los tramos de cada uno.", " turnos"),
    ],
    [ex(f"{IDEAS}. Te piden música para una escena escolar de un día de lluvia que termina con sol. ¿Qué decisión representa el final? A) Sonidos suaves y largos al final. B) Golpes cortos y fuertes al final.", "A", "El final es calmado: la lluvia cesa y se aquieta.")],
    [ex("¿Una historia es una idea musical o extramusical?", "Extramusical", "Viene de fuera de la música."), ex("¿Qué se hace primero: la idea o los sonidos?", "La idea", "La idea guía las decisiones."), ex("¿Cómo justificas una decisión?", "Con una razón, usando «porque»", "Se explica la relación con la idea.")],
    (
        "Elige una idea extramusical: «una tarde de verano en la plaza» o «un viaje en micro». Escribe: a) tres decisiones musicales (ritmo, timbre y volumen), b) una frase de justificación para cada una con «porque», c) un cambio de volumen o de ritmo a lo largo de la escena. Si quieres, pruébalo con objetos cotidianos seguros y volumen bajo.",
        "Tarde de verano en la plaza. a) Ritmo lento, sonidos largos de papel, volumen bajo; entran golpes cortos de tapa cuando llegan los niños. b) Uso ritmo lento porque la tarde pasa tranquila; uso golpes cortos porque llegan niños jugando. c) El volumen sube un poco cuando llegan y vuelve a bajar.",
        ["traduce una idea elegida", "justifica con «porque»", "incluye un cambio a lo largo del tiempo"],
        ["tres decisiones", "tres justificaciones y un cambio"],
        ["decisiones sin relación con la idea", "no justificar"],
        "Reconoce la traducción y pide explicar qué otra decisión alternativa funcionaría para la misma idea.",
    ),
    "Elige una imagen (por ejemplo, el viento) y describe en una frase cómo la harías sonar.",
    "Traduce una emoción (por ejemplo, alegría) en tres decisiones musicales y justifícalas.",
)

# ---------------------------------------------------------------- OA 05 · clase 3 (arreglo de canciones y secciones)
SEC = ("Canción de ejemplo «Canción del río», con secciones: introducción (4 compases), estrofa (8 compases), estribillo (8 compases), puente (4 compases) y final (4 compases). "
       "Orden del arreglo 1: introducción, estrofa, estribillo, estrofa, estribillo, puente, estribillo, final. Cada compás tiene 4 pulsos y se toca a 96 pulsos por minuto")
L(
    OA5, 3,
    f"Lápiz y papel. Canción y arreglo de ejemplo, que se repiten en los ejercicios: {SEC}.",
    "Aprenderé a arreglar una canción: organizar sus secciones (introducción, estrofa, estribillo, puente y final) y decidir en cada una el tempo, quién toca o canta y el volumen. Sirve para darle forma y personalidad propia a una canción conocida.",
    ["Sé armar y variar un motivo.", "Sé traducir una idea a decisiones musicales.", "Sé calcular pulsos y compases."],
    [
        "Un arreglo es la manera particular en que se organiza una canción: qué secciones tiene, en qué orden van y cómo suena cada una. Las secciones más comunes son la introducción, que prepara; la estrofa, que cuenta; el estribillo, que se repite y es lo que más se recuerda; el puente, que contrasta con lo anterior; y el final, que cierra. Cambiar el orden o repetir una sección cambia la forma de la canción.",
        "En cada sección se pueden tomar decisiones distintas: una introducción con una sola guitarra y volumen suave; una estrofa con voz y guitarra; un estribillo con todos los instrumentos y volumen más fuerte; un puente en que se detiene el pulso o se cambia el timbre; un final lento. Así se crea un recorrido de la música en el tiempo, con momentos de calma, de energía y de contraste.",
        "Los arreglos se calculan con números. Si el arreglo 1 suma 52 compases de 4 pulsos, son 208 pulsos; a 96 pulsos por minuto, la canción dura 208 × 60 ÷ 96 = 130 segundos. Mantener un registro del orden de las secciones y de sus compases ayuda a repetir el arreglo y a compararlo con otros. Un buen arreglo respeta la canción original, pero se anima a proponer algo propio.",
    ],
    [("arreglo", "manera particular de organizar y hacer sonar una canción"), ("sección", "parte de una canción con una función, como la estrofa o el estribillo"), ("estribillo", "sección que se repite y es la más recordada"), ("puente", "sección que contrasta con las anteriores"), ("introducción", "sección que prepara el comienzo de la canción")],
    [
        ("Contar compases de un arreglo", f"{SEC}. ¿Cuántos compases tiene el arreglo 1 completo?", ["Introducción 4; estrofa 8 y estribillo 8; otra estrofa 8 y otro estribillo 8; puente 4; estribillo 8; final 4.", "4 + 8 + 8 + 8 + 8 + 4 + 8 + 4 = 52."], "52 compases"),
        ("Calcular la duración", f"{SEC}. ¿Cuántos segundos dura el arreglo 1?", ["52 compases de 4 pulsos son 208 pulsos.", "208 × 60 ÷ 96 = 130."], "130 segundos"),
    ],
    [
        ("Cambiar tantas cosas que la canción ya no se reconoce.", "Un arreglo conserva la melodía o el carácter principal de la canción.", "Cambia el orden, el volumen o el timbre, pero conserva la melodía."),
        ("Tocar todas las secciones con el mismo volumen y los mismos instrumentos.", "Sin contraste, la canción suena plana.", "Planifica un cambio en cada sección."),
    ],
    [
        ex(f"{SEC}. ¿Cuántos compases tiene la estrofa?", "8", "Así lo indica la descripción."),
        ex(f"{SEC}. ¿Qué sección se repite más veces en el arreglo 1?", "El estribillo", "Aparece tres veces."),
        ex(f"{SEC}. ¿Qué sección contrasta con las anteriores?", "El puente", "Esa es la función del puente."),
    ],
    [
        ex("¿Qué es un arreglo? A) La manera particular de organizar y hacer sonar una canción. B) Una canción nueva sin relación con otra.", "A", "El arreglo parte de una canción existente."),
        ex(f"{SEC}. Una versión del arreglo empieza con una introducción de una sola guitarra a volumen suave. ¿Qué función cumple? A) Preparar el comienzo de la canción. B) Contrastar con el estribillo.", "A", "La introducción prepara lo que viene."),
        ex("En un arreglo, ¿qué sección conviene hacer más fuerte para que se recuerde? A) El estribillo. B) La introducción.", "A", "El estribillo es la sección que más se recuerda."),
    ],
    [
        arith(f"{SEC}. Un arreglo 2 solo tiene introducción, estrofa, estribillo y final (cada una una vez). ¿Cuántos compases tiene?", "4+8+8+4", "Se suman los compases de las cuatro secciones.", " compases"),
        arith(f"{SEC}. ¿Cuántos pulsos tiene el arreglo 2 de introducción, estrofa, estribillo y final?", "(4+8+8+4)*4", "Son 24 compases de 4 pulsos.", " pulsos"),
        ex(f"{SEC}. Un grupo quiere un arreglo más corto que el arreglo 1. ¿Qué cambio lo acorta? A) Quitar una estrofa y un estribillo. B) Repetir el puente tres veces.", "A", "Quitar secciones reduce los compases; repetir los aumenta."),
    ],
    [
        arith(f"{SEC}. ¿Cuántos segundos dura el arreglo 2, de 24 compases?", "24*4*60//96", "Son 96 pulsos, a 96 por minuto.", " segundos"),
        arith(f"{SEC}. ¿Cuántos segundos más dura el arreglo 1 que el arreglo 2?", "130-60", "Se restan los segundos del arreglo 2 a los del arreglo 1.", " segundos"),
    ],
    [
        ex(f"{SEC}. Un grupo propone cambiar el tempo del arreglo 1 de 96 a 120 pulsos por minuto. ¿Qué pasa con la duración total? A) Dura menos. B) Dura más.", "A", "Con más pulsos por minuto, los mismos pulsos pasan más rápido."),
        arith(f"{SEC}. Con el arreglo 1 a 120 pulsos por minuto, ¿cuántos segundos dura?", "208*60//120", "Son 208 pulsos, a 120 por minuto.", " segundos"),
    ],
    [ex(f"{SEC}. Para un acto de aniversario necesitas un arreglo de máximo 100 segundos a 96 pulsos por minuto. ¿Cuál cumple? A) El arreglo 2, que dura 60 segundos. B) El arreglo 1, que dura 130 segundos.", "A", "60 segundos es menor que el máximo; 130 lo supera.")],
    [ex("¿Qué sección prepara el comienzo de la canción?", "La introducción", "Prepara lo que viene."), ex("¿Qué sección es la más recordada?", "El estribillo", "Se repite varias veces."), ex(f"{SEC}. ¿Cuántos compases tiene el puente?", "4", "Así lo dice la descripción.")],
    (
        "Usa la «Canción del río» de ejemplo. Escribe un arreglo propio (arreglo 3) con las secciones en el orden que elijas (puedes repetir o quitar secciones). Para cada sección anota qué instrumentos suenan y el volumen. Calcula cuántos compases y cuántos segundos dura a 96 pulsos por minuto.",
        "Arreglo 3: introducción (guitarra, suave), estrofa (voz y guitarra, medio), estribillo (todos, fuerte), puente (solo percusión), estribillo (todos, fuerte), final (voz y guitarra, suave). Compases: 4 + 8 + 8 + 4 + 8 + 4 = 36. Pulsos: 144. Segundos: 144 × 60 ÷ 96 = 90.",
        ["usa las secciones de la canción", "indica instrumentos y volumen por sección", "el cálculo de compases y segundos es correcto"],
        ["orden de secciones", "cálculo de compases y duración"],
        ["cambiar tantas cosas que no se reconoce", "errores de cálculo"],
        "Reconoce el arreglo y pide explicar qué sección es el momento de mayor energía y por qué.",
    ),
    "Escribe el orden de secciones de una canción que conozcas (introducción, estrofa, estribillo...).",
    "Haz un arreglo con otro orden de secciones para una canción conocida y calcula su duración.",
)

# ---------------------------------------------------------------- OA 05 · clase 4 (improvisar con una escala pentatónica)
PEN = ("Escala de ejemplo (pentatónica sobre do): 1 = do, 2 = re, 3 = mi, 5 = sol, 6 = la. Fuera de la escala: 4 = fa y 7 = si. "
       "Base de ejemplo: una persona toca el ostinato do-sol-do-sol, un grupo de 4 pulsos que se repite sin parar")
L(
    OA5, 4,
    f"Lápiz y papel; si quieres, tu voz, un instrumento o tarareo con volumen bajo. Escala y base de ejemplo, que se repiten en los ejercicios: {PEN}.",
    "Aprenderé a improvisar con reglas sencillas: usar las notas de una escala pentatónica sobre una base que se repite, repetir un motivo y terminar en la nota de reposo. Sirve para inventar melodías en el momento con seguridad y sin miedo a equivocarme.",
    ["Sé qué es un motivo.", "Sé que un ostinato repite un patrón.", "Sé numerar las notas del 1 al 7."],
    [
        "Improvisar es inventar música en el momento, mientras se toca o se canta. No es hacer cualquier cosa: se improvisa con reglas que dan seguridad. Una regla común es usar una escala pentatónica, que es una escala de cinco notas. La pentatónica sobre do usa do, re, mi, sol y la, que se numeran 1, 2, 3, 5 y 6. Estas cinco notas suenan bien juntas, de modo que es difícil que choquen entre sí al combinarlas sobre una base.",
        "Otras reglas ayudan a dar forma. Se parte de un motivo corto, por ejemplo 1 2 3 5, y se repite con variaciones. Se alternan notas que se mueven con notas que se repiten. Se dejan silencios para respirar. Y se termina en la nota de reposo, que en esta escala es el 1 (do): al llegar a ella, la melodía suena como si cerrara la frase. La base, por ejemplo un ostinato de 4 pulsos, da el pulso y el apoyo.",
        "Lo más importante al improvisar es escuchar a la base y a las demás personas, y no tener miedo de equivocarse: si una nota suena fuera de lugar, se sigue con calma, ya que la siguiente nota puede corregirlo. Con la práctica se improvisa mejor. Para recordar una improvisación, se anota con números o se graba con permiso, y se comparan las versiones para decidir qué conservar.",
    ],
    [("improvisar", "inventar música en el momento, con reglas"), ("pentatónica", "escala de cinco notas"), ("nota de reposo", "nota en la que la melodía suena como si cerrara"), ("base", "acompañamiento que se repite y sostiene la improvisación"), ("silencio", "pausa que da respiro a la melodía")],
    [
        ("Comprobar la escala", f"{PEN}. ¿La melodía 1 2 3 5 6 5 3 1 pertenece a la escala?", ["Las notas son 1, 2, 3, 5 y 6.", "Todas están en la escala."], "Sí, todas sus notas están en la escala"),
        ("Terminar en reposo", f"{PEN}. La melodía 2 3 5 6 5 3 2 termina en el 2. ¿Cómo la cambias para que termine en la nota de reposo?", ["La nota de reposo es el 1.", "Se agrega el 1 al final."], "2 3 5 6 5 3 2 1"),
    ],
    [
        ("Pensar que improvisar es tocar sin reglas.", "Las reglas dan seguridad y forma.", "Elige una escala, un motivo y una nota final."),
        ("Detenerse por una nota que no gustó.", "Seguir con calma mantiene la música y permite corregir con la siguiente nota.", "Continúa y busca la siguiente nota de la escala."),
    ],
    [
        ex(f"{PEN}. ¿Cuántas notas tiene la escala pentatónica de ejemplo?", "5", "Son 1, 2, 3, 5 y 6."),
        ex(f"{PEN}. ¿La nota 4 (fa) está en la escala de ejemplo? Responde sí o no.", "No", "Está fuera de la escala."),
        ex(f"{PEN}. ¿Cuál es la nota de reposo de la escala de ejemplo?", "El 1 (do)", "La melodía suena cerrada al llegar al 1."),
    ],
    [
        ex(f"{PEN}. ¿Qué melodía pertenece a la escala? A) 1 3 5 6 5 3 1. B) 1 4 5 7 5 4 1.", "A", "La segunda usa las notas 4 y 7, que están fuera de la escala."),
        ex(f"{PEN}. ¿Qué cumple la regla de terminar en la nota de reposo? A) 2 3 5 3 2 1. B) 1 2 3 5 6 5.", "A", "La primera termina en el 1; la segunda termina en el 5."),
        ex("Durante una improvisación suena una nota fuera de lugar. ¿Qué conviene hacer? A) Seguir con calma y tocar la siguiente nota de la escala. B) Detener todo y empezar de nuevo.", "A", "Seguir mantiene la música y permite corregir."),
    ],
    [
        arith("El ostinato de la base dura 4 pulsos y se repite 6 veces. ¿Cuántos pulsos suena la base?", "4*6", "Se multiplican los pulsos del ostinato por las repeticiones.", " pulsos"),
        ex(f"{PEN}. ¿Cuántas notas de la melodía 1 2 4 5 7 1 están fuera de la escala?", "2", "Las notas 4 y 7 están fuera de la escala."),
        ex(f"{PEN}. Un motivo es 1 2 3 5. Se varía cambiando solo la última nota por 6. ¿Cuál es la variación?", "1 2 3 6", "Se conserva el comienzo y se cambia la última nota."),
    ],
    [
        ex(f"{PEN}. Una persona improvisa: 5 5 6 5 3 2 1 1. ¿Cuántas veces repite una misma nota seguida?", "2", "Repite el 5 al inicio y el 1 al final."),
        arith("Una improvisación dura 8 compases de 4 pulsos, y en cada pulso hay una nota o un silencio. Si 10 pulsos son silencios, ¿cuántas notas toca?", "8*4-10", "Se restan los pulsos de silencio al total de pulsos.", " notas"),
    ],
    [
        ex(f"{PEN}. Compara A) 1 3 5 6 5 2 3 1 y B) 6 6 6 6 6 6 6 6. ¿Cuál tiene más variedad de notas y por qué se prefiere para improvisar?", "A", "Usa cinco notas diferentes y se mueve; la otra repite una sola nota."),
        arith("Un grupo de 3 estudiantes improvisa por turnos sobre la misma base. Cada turno dura 4 compases de 4 pulsos. ¿Cuántos pulsos dura la ronda completa?", "3*4*4", "Se multiplican estudiantes, compases y pulsos por compás.", " pulsos"),
    ],
    [ex("Tu curso hace una ronda de improvisación sobre una base. Una compañera dice que no se atreve. ¿Qué la ayuda más? A) Recordar que puede usar las cinco notas de la escala y repetir un motivo corto. B) Pedirle que toque lo más rápido que pueda.", "A", "Las reglas simples dan seguridad.")],
    [ex("¿Cuántas notas tiene una escala pentatónica?", "Cinco", "Penta significa cinco."), ex("¿En qué nota termina una improvisación que cierra bien?", "En la nota de reposo", "Da sensación de cierre."), ex("¿Qué haces si suena una nota fuera de lugar?", "Sigo con calma", "La siguiente nota puede corregirlo.")],
    (
        "Con la escala de ejemplo (1 2 3 5 6) y la base (do-sol-do-sol), improvisa dos veces de 8 notas cada una. Escribe: a) tu motivo de 4 notas, b) la primera improvisación en números, c) la segunda improvisación en números, que debe terminar en 1, d) una regla que usaste (repetir, variar, silencio o reposo).",
        "a) 1 2 3 5. b) 1 2 3 5 3 2 1 2. c) 5 6 5 3 2 3 2 1. d) Terminé en el 1 para cerrar y repetí el motivo con una variación.",
        ["todas las notas pertenecen a la escala", "la segunda improvisación termina en 1", "nombra una regla usada"],
        ["dos improvisaciones de 8 notas", "regla indicada"],
        ["usar notas fuera de la escala sin intención", "no terminar en reposo"],
        "Reconoce las improvisaciones y pide cambiar una nota de la segunda y explicar el efecto.",
    ),
    "Tararea una melodía de 8 notas usando solo do, re, mi, sol y la, y termina en do.",
    "Inventa una base de 4 pulsos con palmas y improvisa una melodía de 8 notas sobre ella.",
)

# ---------------------------------------------------------------- OA 05 · clase 5 (registrar y contrastar versiones)
VER = ("Versión 1 (de ejemplo) de una improvisación: 12 notas, de las cuales 4 repiten el motivo 1 2 3 5; termina en la nota 2; 80 pulsos por minuto; 16 compases de 4 pulsos. "
       "Versión 2: 14 notas, de las cuales 8 repiten el motivo 1 2 3 5; termina en la nota 1; 96 pulsos por minuto; 16 compases de 4 pulsos")
L(
    OA5, 5,
    f"Lápiz y papel; para registrar pueden servir números, dibujos o una grabación de audio con el permiso de todas las personas. Datos de ejemplo, que se repiten en los ejercicios: {VER}.",
    "Aprenderé a registrar mis versiones de una improvisación o creación (con números, dibujo o grabación) y a contrastarlas con una ficha para decidir qué conservar. Sirve para mejorar mi música con evidencia y para recordar lo que inventé.",
    ["Sé improvisar con una escala pentatónica.", "Sé armar y variar motivos.", "Sé calcular duraciones."],
    [
        "Una improvisación se escucha una vez y desaparece. Registrarla permite volver a ella. Hay tres formas simples: anotarla con números (1 2 3 5), dibujarla con líneas que suben y bajan y puntos para las notas, o grabarla en audio. Para grabar, se pide el permiso de todas las personas que suenan, se guarda el archivo solo para trabajo del grupo y no se comparte sin acuerdo.",
        "Contrastar versiones es compararlas con una ficha de criterios. Por ejemplo: cantidad de notas, cuántas veces aparece el motivo, en qué nota termina, tempo y duración. Si en la versión 1 el motivo aparece 1 vez y en la versión 2 aparece 2 veces, la versión 2 tiene más repetición del motivo. Con esos datos se decide qué conservar y qué cambiar, según el propósito de la música.",
        "Una buena ficha termina con una decisión: «conservo la nota final en 1 porque cierra mejor» o «bajo el tempo porque se enredan las notas». Los comentarios se refieren a la música y no a las personas. Cuando la creación es colectiva, se agrega quién propuso cada cambio y cómo se acordó, para que el aporte de todos quede registrado.",
    ],
    [("registrar", "dejar constancia de una versión con números, dibujo o grabación"), ("contrastar", "comparar versiones con criterios para ver en qué cambian"), ("ficha de criterios", "lista de aspectos que se revisan en cada versión"), ("conservar", "mantener un elemento de una versión"), ("permiso", "acuerdo de las personas antes de grabar o compartir")],
    [
        ("Comparar dos datos", f"{VER}. ¿En qué versión aparece más veces el motivo, y cuántas más?", ["La versión 1 repite el motivo 4 veces y la 2 lo repite 8.", "8 − 4 = 4."], "En la versión 2, 4 notas más"),
        ("Decidir con evidencia", f"{VER}. ¿Qué versión termina en la nota de reposo?", ["La nota de reposo es 1.", "La versión 2 termina en 1."], "La versión 2"),
    ],
    [
        ("Anotar «la versión 2 es mejor» sin datos.", "Sin criterios no se puede comprobar ni mejorar.", "Anota datos de ambas versiones y concluye con una razón."),
        ("Compartir una grabación sin permiso.", "Se necesita el acuerdo de todas las personas grabadas.", "Pide permiso y explica para qué será."),
    ],
    [
        ex(f"{VER}. ¿Cuántas notas tiene la versión 1?", "12", "Así lo indica la ficha."),
        ex(f"{VER}. ¿A cuántos pulsos por minuto se toca la versión 2?", "96", "Así lo indica la ficha."),
        ex("¿Qué se necesita antes de grabar a un grupo?", "El permiso de todas las personas", "Es una norma de respeto."),
    ],
    [
        ex(f"{VER}. ¿Qué versión tiene un tempo más lento? A) La versión 1. B) La versión 2.", "A", "80 pulsos por minuto es menos que 96."),
        ex("¿Para qué sirve una ficha de criterios? A) Para comparar versiones con los mismos datos. B) Para decidir quién tiene la razón.", "A", "Compara con evidencia, no con opiniones sobre las personas."),
        ex("Una versión de una improvisación fue grabada por un compañero y quiere subirla a una red pública sin avisar. ¿Qué corresponde? A) Pedir permiso a todas las personas grabadas antes de publicar. B) Publicar y avisar después.", "A", "El permiso se pide antes."),
    ],
    [
        arith(f"{VER}. ¿Cuántos pulsos por minuto más tiene la versión 2 que la versión 1?", "96-80", "Se restan los pulsos de la versión 1 a los de la 2.", " pulsos por minuto"),
        arith(f"{VER}. ¿Cuántos segundos dura la versión 1? Son 16 compases de 4 pulsos a 80 pulsos por minuto.", "16*4*60//80", "Son 64 pulsos; se dividen entre los pulsos por segundo.", " segundos"),
        ex(f"{VER}. Un comentario dice: «La versión 2 repite más el motivo, y por eso se reconoce mejor». ¿Es un comentario con evidencia? Responde sí o no.", "Sí", "Se apoya en el dato de 8 notas del motivo contra 4."),
    ],
    [
        arith(f"{VER}. ¿Cuántas notas de la versión 2 no pertenecen al motivo repetido?", "14-8", "Se restan las notas del motivo al total de notas.", " notas"),
        ex(f"{VER}. El grupo quiere una versión final que combine lo mejor de las dos: el tempo de la versión 1 y la terminación de la versión 2. ¿Cuál es el tempo y en qué nota termina?", "80 pulsos por minuto y la nota 1", "Toma el tempo de la versión 1 y la nota final de la versión 2."),
    ],
    [
        ex("Dos estudiantes registran su improvisación. Ana la graba con permiso y la comparte con el grupo. Beto la graba sin avisar y la sube a una red pública. ¿Quién cumple las reglas del taller? A) Ana. B) Beto.", "A", "Ana pidió permiso y compartió solo con el grupo."),
        arith("Un grupo de 4 registra 3 versiones cada uno. ¿Cuántas versiones hay en total para contrastar?", "4*3", "Se multiplican las personas por las versiones de cada una.", " versiones"),
    ],
    [ex(f"{VER}. El propósito de la música es dar sensación de cierre al final de un acto. ¿Qué versión conserva mejor el final? A) La versión 2, porque termina en la nota de reposo. B) La versión 1, porque es más lenta.", "A", "La nota de reposo da sensación de cierre.")],
    [ex("¿Con qué tres formas se puede registrar una improvisación?", "Números, dibujo o grabación", "Son las formas simples vistas en la clase."), ex("¿Qué se hace después de comparar versiones?", "Se decide qué conservar y qué cambiar", "La ficha termina con una decisión."), ex("¿Sobre qué hablan los comentarios: la música o las personas?", "La música", "Los comentarios evalúan lo que suena.")],
    (
        "Crea dos versiones de una improvisación de 8 notas con la escala 1 2 3 5 6. Escribe: a) cada versión en números, b) una ficha con cuatro criterios (notas del motivo 1 2 3 5, nota final, tempo que usarías y una sensación), c) una decisión final con «porque», d) una regla de permiso si quisieras grabarla.",
        "a) V1: 1 2 3 5 6 5 3 2. V2: 1 2 3 5 1 2 3 1. b) V1: motivo 1 vez, termina en 2, tempo 80, sensación abierta. V2: motivo completo 1 vez más su variación 1 2 3 1, termina en 1, tempo 80, sensación de cierre. c) Conservo la V2 porque repite y varía el motivo y termina en reposo. d) Grabaré solo si todos aceptan.",
        ["usa solo notas de la escala", "la ficha tiene cuatro criterios con datos", "la decisión final se apoya en los datos"],
        ["dos versiones en números", "ficha y decisión"],
        ["comparar sin datos", "grabar sin permiso"],
        "Reconoce la ficha y pide proponer una tercera versión que cambie solo un criterio.",
    ),
    "Escribe en números una melodía de 6 notas y dibújala con puntos que suben y bajan.",
    "Compara dos versiones de la misma melodía tuya usando tres criterios.",
)
