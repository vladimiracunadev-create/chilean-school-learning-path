"""Student material for 8.º básico Música, OA 05 (improvisar y crear música a partir de indicaciones determinadas, con énfasis en acompañamientos y variaciones rítmicas, melódicas y/o armónicas).

Todas las melodías, patrones y casos de los ejercicios son esquemas inventados para esta clase; las músicas reales las selecciona el docente.
"""
from __future__ import annotations

from student_content_mu8_a import L
from student_lessons import arith, ex

OA5 = "MU08 OA 05"

NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"
LEY = "semicorchea = 1 unidad; corchea = 2; negra = 4 (un pulso); negra con puntillo = 6; blanca = 8; redonda = 16; un compás de 4/4 tiene 16 unidades"
ACORDES = "I = do-mi-sol; IV = fa-la-do; V = sol-si-re; vi = la-do-mi"

# ---------------------------------------------------------------- OA 05 · clase 1 (improvisar con indicaciones)
L(
    OA5, 1,
    f"Lápiz y papel. Escala de números: {NOTAS}. Notas permitidas para improvisar en la clase: 1, 2, 3, 5 y 6. Puedes improvisar con la voz («la»), con palmas o con un objeto que suene suave, a volumen bajo.",
    "Aprenderé a improvisar siguiendo indicaciones: qué notas usar, cuántos compases, qué ritmo y en qué nota terminar. Sirve para crear música en el momento sin tocar cualquier cosa.",
    ["Sé leer una melodía escrita con números.", "Sé que una pregunta musical queda en suspenso y una respuesta llega a reposo.", "Sé contar compases y pulsos."],
    [
        "Improvisar es crear música en el momento, pero no es tocar cualquier cosa. Se improvisa a partir de indicaciones determinadas, que son las reglas del juego. Estas pueden decir qué notas usar, cuántos compases tocar, qué ritmo emplear y en qué nota terminar. Con pocas notas permitidas es más fácil que todo suene bien. En la clase usamos las notas 1, 2, 3, 5 y 6, que combinan con facilidad.",
        "Una forma muy usada es la pregunta y respuesta. La pregunta es una frase corta que termina en una nota que deja la sensación de suspenso, como la nota 2. La respuesta es otra frase corta que termina en una nota de reposo, como la nota 1. Así la improvisación tiene sentido y se oye como una conversación. Dos personas pueden improvisar con las mismas reglas y crear melodías distintas.",
        "Para saber si una improvisación cumple las reglas, se revisa cada indicación: ¿usa solo las notas permitidas?, ¿tiene los compases pedidos?, ¿termina donde debe? Como la improvisación desaparece al sonar, conviene registrarla en una partitura de números o en un audio. También se puede contar cuántas melodías distintas caben dentro de las reglas: con 5 notas permitidas, una melodía de 2 notas puede armarse de 5 × 5 = 25 maneras.",
    ],
    [("improvisar", "crear música en el momento, siguiendo indicaciones"), ("indicaciones", "reglas que dicen qué notas, compases y ritmo usar y dónde terminar"), ("pregunta", "frase que termina en suspenso"), ("respuesta", "frase que termina en reposo"), ("nota de reposo", "nota en que la melodía se siente terminada, como la 1")],
    [
        ("Revisar las reglas", "Reglas: usar solo las notas 1, 2, 3, 5 y 6. ¿Cumple la melodía 2-3-5-6-5?", ["Se revisa nota por nota.", "Las notas 2, 3, 5 y 6 están permitidas."], "Sí, cumple"),
        ("Contar posibilidades", "Si solo se permiten las notas 1, 3 y 5, ¿cuántas melodías distintas de 2 notas se pueden armar si las notas pueden repetirse?", ["Hay 3 opciones para la primera nota.", "Hay 3 para la segunda: 3 × 3 = 9."], "9 melodías"),
    ],
    [
        ("Pensar que improvisar es tocar cualquier cosa.", "Improvisar sigue indicaciones; sin reglas, la música no tiene dirección.", "Anota las reglas antes de empezar."),
        ("Terminar la respuesta en una nota que queda en suspenso.", "La respuesta debe llegar a reposo para sonar terminada.", "Termina la respuesta en la nota 1."),
    ],
    [
        ex("Reglas: usar solo las notas 1, 2, 3, 5 y 6. ¿Se puede usar la nota 4? Responde sí o no.", "No", "La nota 4 no está entre las notas permitidas."),
        ex("¿Improvisar significa tocar cualquier cosa sin reglas? Responde sí o no.", "No", "Se improvisa siguiendo indicaciones."),
        ex("La respuesta de una pregunta y respuesta debe terminar en la nota 1. ¿Es una nota de reposo o de suspenso?", "De reposo", "La nota 1 hace sentir que la melodía terminó."),
    ],
    [
        arith("Una improvisación tiene 4 compases con 4 negras cada uno. ¿Cuántas notas toca?", "4*4", "Se multiplican los compases por las notas de cada compás.", " notas"),
        ex("Reglas: solo las notas 1, 2, 3, 5 y 6. ¿Qué melodía cumple? A) 1-3-5-6. B) 1-3-4-5.", "A", "La otra usa la nota 4, que no está permitida."),
        ex("Reglas: la respuesta debe terminar en la nota 1. ¿Qué respuesta cumple? A) 5-3-2-3. B) 5-3-2-1.", "B", "Solo la segunda termina en la nota 1."),
    ],
    [
        arith("Con 5 notas permitidas, ¿cuántas melodías de 2 notas se pueden armar si las notas pueden repetirse?", "5*5", "Hay 5 opciones para cada una de las dos notas.", " melodías"),
        arith("Una improvisación de 8 compases en 3/4 usa una negra por pulso. ¿Cuántas notas toca?", "8*3", "Son 8 compases de 3 pulsos cada uno.", " notas"),
        arith("Una pregunta de 2 compases y una respuesta de 2 compases tienen 4 negras por compás. ¿Cuántas notas hay en total?", "(2+2)*4", "Se suman los compases y se multiplican por las notas de cada uno.", " notas"),
    ],
    [
        ex("Clara improvisó 1-3-4-5-6 con las reglas de usar solo las notas 1, 2, 3, 5 y 6. ¿Qué nota no está permitida?", "La 4", "Es la única que no pertenece al conjunto permitido."),
        ex("Dos estudiantes improvisan con las mismas reglas y sus melodías son distintas. ¿Es un problema? Responde sí o no.", "No", "Las mismas reglas permiten muchos resultados distintos."),
    ],
    [
        arith("Con 5 notas permitidas, ¿cuántas melodías distintas de 3 notas hay si las notas pueden repetirse?", "5*5*5", "Hay 5 opciones para cada una de las tres notas.", " melodías"),
        arith("Con 5 notas permitidas, ¿cuántas melodías de 2 notas hay si la segunda nota no puede repetir la primera?", "5*4", "Hay 5 opciones para la primera y 4 para la segunda.", " melodías"),
    ],
    [ex("En un taller, la profesora pide: 4 compases, solo las notas 1, 2, 3, 5 y 6, y terminar en la nota 1. Un estudiante improvisa 5-6-5-3 | 2-3-5-6 | 6-5-3-2 | 3-2-1-1. ¿Cumple las reglas? Responde sí o no.", "Sí", "Tiene 4 compases, usa solo notas permitidas y termina en la nota 1.")],
    [ex("¿Qué es una pregunta musical?", "Una frase que termina en suspenso", "Deja la sensación de que falta una respuesta."), ex("¿En qué nota termina la respuesta de la clase?", "En la nota 1", "Es la nota de reposo."), ex("¿Por qué conviene registrar una improvisación?", "Porque desaparece al sonar", "Si no se registra, no se puede repetir ni revisar.")],
    (
        f"Reglas de ejemplo: 4 compases de 4 negras, usar solo las notas 1, 2, 3, 5 y 6 ({NOTAS}), una pregunta en los compases 1 y 2 que termine en la nota 2, y una respuesta en los compases 3 y 4 que termine en la nota 1. Crea dos improvisaciones distintas con esas reglas y escríbelas con números. Revisa cada una con una lista: notas permitidas, 4 compases, pregunta que termina en 2, respuesta que termina en 1.",
        "Improvisación 1: 1-2-3-5 | 3-2-3-2 | 5-3-5-3 | 3-2-1-1. Improvisación 2: 5-6-5-3 | 3-5-3-2 | 6-5-3-2 | 3-2-1-1. Revisión: ambas usan solo 1, 2, 3, 5 y 6; tienen 4 compases; la pregunta termina en 2 y la respuesta en 1.",
        ["cumple todas las reglas", "las dos improvisaciones son distintas", "la revisión es una lista con cada regla"],
        ["dos melodías escritas con números", "lista de revisión"],
        ["usar la nota 4", "terminar la respuesta en una nota que no es la 1"],
        "Reconoce las melodías y pide cantar la que más le guste y señalar dónde termina la pregunta y dónde la respuesta.",
    ),
    "Canta con «la» cuatro notas entre 1, 2, 3, 5 y 6 que terminen en la nota 1.",
    "Crea una improvisación de 4 compases que cumpla las reglas de la clase y cambie una nota para hacer una segunda versión.",
)

# ---------------------------------------------------------------- OA 05 · clase 2 (variación rítmica)
L(
    OA5, 2,
    f"Lápiz y papel. Leyenda de duraciones de la clase: {LEY}. Los patrones están escritos en los ejercicios. Si quieres, palmea cada patrón a volumen bajo con un pulso marcado.",
    "Aprenderé a hacer variaciones rítmicas de una melodía: aumentación, disminución, silencios y síncopa. Sirve para que una misma melodía suene distinta sin dejar de reconocerse.",
    ["Sé que cada figura dura un número de unidades.", "Sé sumar las duraciones de un compás.", "Sé que la síncopa es una nota que cruza un pulso."],
    [
        "Una variación rítmica cambia las duraciones de una melodía y mantiene las notas. Por eso la melodía sigue reconociéndose. La aumentación hace que cada figura dure el doble: una negra se convierte en blanca, y la melodía suena más espaciada. La disminución hace que cada figura dure la mitad: una negra se convierte en corchea, y la melodía suena más rápida y ocupa menos tiempo.",
        "También se puede variar el ritmo agregando silencios, que dejan espacios en la melodía, o convirtiendo notas del pulso en síncopas, que empujan la música hacia adelante. Si la duración total del compás es de 16 unidades, la variación debe seguir sumando 16 para llenarlo. En aumentación, el patrón ocupa el doble de unidades y puede ocupar más compases. En disminución ocupa la mitad.",
        "Para crear una variación se escribe el patrón original con sus unidades, se aplica un cambio y se comprueba la suma. Después se palmea o se canta la nueva versión y se compara con la original. Una buena variación se reconoce porque se oye distinta, pero todavía se puede decir de qué melodía viene. Si cambian las notas y también el ritmo, ya no es una variación sino otra melodía.",
    ],
    [("variación rítmica", "cambio de las duraciones manteniendo las notas"), ("aumentación", "cada figura dura el doble"), ("disminución", "cada figura dura la mitad"), ("síncopa", "nota que empieza entre pulsos y sigue sonando sobre el pulso siguiente"), ("unidad", "duración de una semicorchea, que sirve para medir el ritmo")],
    [
        ("Aplicar una disminución", "El patrón original es negra, negra, blanca (16 unidades en 4/4). ¿Cuántas unidades suma en disminución?", ["Cada figura dura la mitad: corchea (2), corchea (2) y negra (4).", "2 + 2 + 4 = 8."], "8 unidades"),
        ("Aplicar una aumentación", "Un patrón de 3 negras (12 unidades) se toca en aumentación. ¿Cuántas unidades dura?", ["Cada figura dura el doble.", "12 × 2 = 24."], "24 unidades"),
    ],
    [
        ("Creer que cambiar las duraciones cambia la melodía.", "Las notas siguen siendo las mismas; solo cambia el ritmo.", "Compara las notas y luego las duraciones."),
        ("Cambiar notas y duraciones a la vez y llamarlo variación rítmica.", "Una variación rítmica mantiene las notas.", "Cambia solo las duraciones."),
    ],
    [
        ex("Cada figura dura el doble. ¿Es aumentación o disminución?", "Aumentación", "Doblar la duración es aumentar."),
        ex("¿Qué figura dura la mitad de una negra?", "La corchea", "La negra dura 4 unidades y la corchea 2."),
        ex("Una variación rítmica, ¿cambia las notas o las duraciones?", "Las duraciones", "Las notas se mantienen."),
    ],
    [
        arith("Un patrón de 2 blancas (16 unidades) se toca en disminución. ¿Cuántas unidades dura?", "16//2", "Cada figura dura la mitad.", " unidades"),
        ex("Una nota empieza en la unidad 10 y dura 4 unidades en 4/4 (pulsos en las unidades 0, 4, 8 y 12). ¿Es síncopa? Responde sí o no.", "Sí", "Empieza entre pulsos y pasa sobre el pulso de la unidad 12."),
        ex("Un grupo quiere que una melodía suene más tranquila y espaciada sin cambiar las notas. ¿Qué variación le sirve: aumentación o disminución?", "Aumentación", "Las notas más largas hacen sonar la melodía más espaciada."),
    ],
    [
        arith("El patrón original en 3/4 es negra con puntillo, corchea y negra. En disminución, ¿cuántas unidades suma? (negra con puntillo 6, corchea 2, negra 4)", "(6+2+4)//2", "Se suman las unidades y se toma la mitad.", " unidades"),
        arith("Una melodía de 8 negras se toca en aumentación (cada negra pasa a blanca de 8 unidades). ¿Cuántos compases de 4/4 ocupa?", "8*8//16", "Son 64 unidades y cada compás tiene 16.", " compases"),
        arith("Una melodía de 8 negras se toca en disminución (cada negra pasa a dos corcheas de 2 unidades). ¿Cuántas notas tiene ahora?", "8*2", "Cada negra se reemplaza por dos corcheas.", " notas"),
    ],
    [
        ex("Ana dice que, si cambia las negras por blancas, la melodía deja de ser la misma. ¿Tiene razón? Responde sí o no.", "No", "Las notas siguen siendo las mismas; solo cambia el ritmo."),
        ex("Una persona cambia las notas y las duraciones de la melodía y dice que hizo una variación rítmica. ¿Por qué no lo es?", "Porque cambió también las notas", "Una variación rítmica solo cambia las duraciones."),
    ],
    [
        arith("Un compás de 4/4 original tiene 16 unidades. Se hace aumentación y el patrón dura el doble. ¿Cuántos compases de 4/4 ocupa?", "(16*2)//16", "El patrón ocupa 32 unidades y cada compás tiene 16.", " compases"),
        arith("Una melodía de 4 compases de 4/4 pasa a disminución. ¿Cuántos compases de 4/4 ocupa ahora?", "4//2", "En disminución dura la mitad.", " compases"),
    ],
    [arith("En la banda escolar, el acompañamiento de 3 compases de 4/4 tiene 12 negras. Para una versión rápida, cada negra se cambia por dos corcheas. ¿Cuántas notas tendrá el acompañamiento?", "12*2", "Cada negra se reemplaza por dos corcheas.", " notas")],
    [ex("¿Qué es la aumentación?", "Que cada figura dure el doble", "Hace sonar la melodía más espaciada."), ex("¿Qué es la disminución?", "Que cada figura dure la mitad", "Hace sonar la melodía más rápida."), ex("¿Una variación rítmica mantiene las notas? Responde sí o no.", "Sí", "Solo se cambian las duraciones.")],
    (
        f"Con la leyenda ({LEY}) toma este patrón de ejemplo en 4/4: negra, negra, blanca. 1) Escribe su aumentación y cuántas unidades y cuántos compases ocupa. 2) Escribe su disminución y cuántas unidades ocupa. 3) Escribe una versión con síncopa: corchea, negra, corchea, blanca, y explica en qué unidad empieza la nota sincopada. Palmea las tres variaciones a volumen bajo, con un pulso marcado.",
        "Aumentación: blanca, blanca, redonda = 8 + 8 + 16 = 32 unidades, 2 compases. Disminución: corchea, corchea, negra = 2 + 2 + 4 = 8 unidades. Síncopa: corchea (0 a 2), negra (2 a 6), corchea, blanca: la negra empieza en la unidad 2 y cruza el pulso de la unidad 4.",
        ["aplica bien aumentación y disminución", "calcula las unidades", "identifica la nota sincopada"],
        ["tres variaciones escritas", "unidades calculadas"],
        ["cambiar también las notas", "no sumar las unidades"],
        "Reconoce las variaciones y pide palmear la original y una variación para comparar cómo cambió el ritmo.",
    ),
    "Palmea cuatro negras y luego cuatro corcheas, y di cuál es la disminución de cuál.",
    "Crea una variación rítmica de un patrón de 4 negras con una síncopa y comprueba que suma 16 unidades.",
)

# ---------------------------------------------------------------- OA 05 · clase 3 (variación melódica)
L(
    OA5, 3,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las melodías están escritas en los ejercicios; puedes cantarlas con «la» o tocarlas para comprobarlas, a volumen cómodo.",
    "Aprenderé a hacer variaciones melódicas de una melodía: transposición, inversión y ornamentación con notas de paso. Sirve para crear versiones nuevas de una melodía manteniendo el pulso.",
    ["Sé leer una melodía escrita con números.", "Sé que una secuencia repite un motivo más arriba o más abajo.", "Sé sumar y restar números pequeños."],
    [
        "Una variación melódica cambia las notas de una melodía y mantiene su ritmo. La transposición mueve todas las notas el mismo número de escalones hacia arriba o hacia abajo (un escalón es pasar a la nota vecina de la escala): 1-2-3 pasa a 4-5-6 si se suben tres escalones. La melodía suena más aguda o más grave, pero conserva su forma. En esta clase las notas deben quedar entre 1 y 8.",
        "En la inversión, cada movimiento se hace en la dirección contraria y con el mismo tamaño, tomando como punto de partida la primera nota. Si la melodía 6-7-6-8 sube 1, baja 1 y sube 2, su inversión baja 1, sube 1 y baja 2: 6-5-6-4. La ornamentación agrega notas de adorno, como una nota de paso entre dos notas separadas: entre 2 y 4 se puede pasar por 3.",
        "Para crear una variación melódica se escribe la melodía original, se elige un procedimiento y se aplica nota por nota. Después se comprueba con una lista que el ritmo no cambió y que todas las notas quedan entre 1 y 8. Al cantarla, se compara con la original: debe oírse distinta, pero reconocible. Si la melodía cambia tanto que ya no se reconoce, es una melodía nueva.",
    ],
    [("variación melódica", "cambio de las notas manteniendo el ritmo"), ("transposición", "mover todas las notas el mismo número de escalones"), ("inversión", "hacer cada movimiento en dirección contraria y con el mismo tamaño"), ("ornamentación", "agregar notas de adorno a la melodía"), ("nota de paso", "nota que une dos notas separadas, pasando por el grado intermedio")],
    [
        ("Transponer", "Transpone la melodía 2-3-4-2 tres escalones hacia arriba.", ["Se suma 3 a cada nota.", "2+3 = 5, 3+3 = 6, 4+3 = 7, 2+3 = 5."], "5-6-7-5"),
        ("Invertir", "Invierte la melodía 5-6-7 tomando la primera nota como punto de partida.", ["La melodía sube 1 y sube 1.", "En la inversión baja 1 y baja 1: 5, 4, 3."], "5-4-3"),
    ],
    [
        ("Cambiar solo algunas notas al transponer.", "La transposición mueve todas las notas el mismo número de escalones.", "Suma o resta lo mismo a cada nota."),
        ("Invertir cambiando el tamaño de los movimientos.", "En la inversión cada movimiento conserva su tamaño, solo cambia de dirección.", "Cuenta los escalones de cada movimiento."),
    ],
    [
        ex("Transpone 1-2-3 dos escalones hacia arriba.", "3-4-5", "A cada nota se le suma 2."),
        ex("En una inversión, si la melodía sube, ¿hacia dónde se mueve la nota correspondiente?", "Hacia abajo", "Cada movimiento va en la dirección contraria."),
        ex("Una nota de paso, ¿se agrega entre dos notas o al final de la melodía?", "Entre dos notas", "Une las dos notas pasando por el grado intermedio."),
    ],
    [
        ex("Invierte la melodía 4-5-6 tomando la primera nota como punto de partida.", "4-3-2", "Cada movimiento va hacia abajo con el mismo tamaño."),
        ex("Transpone la melodía 3-4-5 un escalón hacia abajo.", "2-3-4", "A cada nota se le resta 1."),
        ex("Una variación melódica, ¿cambia las notas o el ritmo?", "Las notas", "El ritmo se mantiene."),
    ],
    [
        ex("Invierte la melodía 5-6-5-7 tomando la primera nota como punto de partida.", "5-4-5-3", "Los movimientos +1, −1 y +2 pasan a −1, +1 y −2."),
        ex("Transpone la melodía 3-5-4-3 dos escalones hacia arriba.", "5-7-6-5", "A cada nota se le suma 2."),
        ex("Quieres agregar una nota de paso entre las notas 6 y 8. ¿Qué nota agregas?", "La nota 7", "Es el grado intermedio entre 6 y 8."),
    ],
    [
        ex("La melodía original es 5-6-5-7. La versión A es 6-7-6-8 y la versión B es 5-4-5-3. ¿Cuál es la transposición y cuál la inversión?", "A es transposición y B es inversión", "A suma 1 a cada nota y B invierte la dirección de cada movimiento."),
        ex("Una transposición, ¿mantiene la forma de la melodía? Responde sí o no.", "Sí", "Todas las notas se mueven lo mismo y los intervalos no cambian."),
    ],
    [
        ex("Invierte la melodía 4-5-7-5 tomando la primera nota como punto de partida.", "4-3-1-3", "Los movimientos +1, +2 y −2 pasan a −1, −2 y +2."),
        arith("A la melodía 1-3-5-3-1 le agregas una nota de paso en cada uno de sus 4 movimientos de tercera. ¿Cuántas notas tiene ahora?", "5+4", "Las 5 notas originales más las 4 notas de paso.", " notas"),
    ],
    [ex("Quieres una versión de una melodía que suene más aguda sin cambiar su forma. ¿Qué procedimiento usas: transposición hacia arriba o inversión?", "Transposición hacia arriba", "Mueve todas las notas el mismo número de escalones sin cambiar la forma.")],
    [ex("¿Qué es transponer?", "Mover todas las notas el mismo número de escalones", "La forma de la melodía se mantiene."), ex("¿Qué es una inversión?", "Cada movimiento va en dirección contraria", "Mantiene el tamaño de cada movimiento."), ex("¿Una variación melódica cambia el ritmo? Responde sí o no.", "No", "Mantiene el ritmo y cambia las notas.")],
    (
        f"Toma esta melodía de ejemplo ({NOTAS}): 5-7-6-8-7, con una nota por pulso. 1) Transpónla un escalón hacia abajo. 2) Escribe su inversión tomando la primera nota como punto de partida. 3) Agrega una nota de paso en cada movimiento de tercera (de 5 a 7 y de 6 a 8) y vuelve a escribirla. 4) Comprueba que el ritmo (una nota por pulso) no cambió en las dos primeras variaciones y que las notas están entre 1 y 8.",
        "1) 4-6-5-7-6. 2) Los movimientos son +2, −1, +2, −1; su inversión es 5-3-4-2-3. 3) Con una nota de paso entre 5 y 7 y otra entre 6 y 8: 5-6-7-6-7-8-7. 4) Las dos primeras variaciones tienen 5 notas, una por pulso, y todas están entre 1 y 8.",
        ["transpone y invierte con el procedimiento correcto", "comprueba que el ritmo no cambió", "las notas quedan entre 1 y 8"],
        ["dos variaciones escritas", "comprobación del ritmo"],
        ["cambiar el tamaño de los movimientos al invertir", "usar notas fuera de 1 a 8"],
        "Reconoce las variaciones y pide cantar la original y una variación para comparar qué cambió y qué se mantuvo.",
    ),
    "Canta 1-2-3 y luego 3-4-5 y di qué procedimiento hiciste.",
    "Crea una variación que combine una transposición y una nota de paso en una melodía de cuatro notas.",
)

# ---------------------------------------------------------------- OA 05 · clase 4 (acompañamiento y variación armónica)
L(
    OA5, 4,
    f"Lápiz y papel. Escala de números: {NOTAS}. Acordes de do mayor y la menor: {ACORDES}. Los patrones de acompañamiento están escritos en los ejercicios; puedes tocarlos o cantarlos nota por nota, a volumen cómodo.",
    "Aprenderé a crear acompañamientos (acordes en bloque, arpegio y bajo-acorde) y a hacer variaciones armónicas cambiando el acorde de un compás por otro compatible. Sirve para que una melodía suene distinta según los acordes que la sostienen.",
    ["Sé que un acorde tiene tres notas.", "Sé elegir un acorde que contiene las notas de la melodía.", "Sé que el acorde V crea tensión y el I da reposo."],
    [
        f"El acompañamiento es lo que sostiene a la melodía. Puede tocarse con los acordes en bloque, con las tres notas a la vez, o en arpegio, con las tres notas una tras otra. En 3/4, un patrón de bajo y acorde suena «bajo – acorde – acorde»: un golpe grave seguido de dos golpes de acorde. Los acordes de do mayor y de la menor son {ACORDES}.",
        "Para elegir un acorde, se miran las notas de la melodía en ese compás y se busca un acorde que las contenga. La variación armónica consiste en reemplazar un acorde por otro compatible. El acorde I (do-mi-sol) y el acorde vi (la-do-mi) comparten dos notas, do y mi. Por eso, si la melodía del compás solo usa do y mi, se puede cambiar el I por el vi. El efecto suele sentirse más suave y melancólico que el original.",
        "El orden de los acordes también cambia la sensación. Una frase que termina en V queda en suspenso, y una que termina en I se siente cerrada. Para variar un acompañamiento, se cambia solo una cosa: el patrón o un acorde. Se canta o se toca la melodía con cada versión y se compara. Una buena variación armónica se oye distinta, pero la melodía sigue encajando con los acordes.",
    ],
    [("acompañamiento", "lo que sostiene a la melodía"), ("arpegio", "las notas de un acorde, una tras otra"), ("acordes en bloque", "las tres notas del acorde a la vez"), ("variación armónica", "cambio de un acorde por otro compatible"), ("acorde compatible", "acorde que contiene las notas que la melodía usa en ese compás")],
    [
        ("Elegir el acorde", f"Un compás tiene la melodía sol-si-re-si. ¿Qué acorde la acompaña mejor? Acordes: {ACORDES}.", ["Se buscan las notas sol, si y re.", "Solo el V las contiene."], "El V"),
        ("Variar un acorde", f"La melodía de un compás es do-mi-do-mi y la acompaña el acorde I. ¿Qué otro acorde puede reemplazarlo? Acordes: {ACORDES}.", ["Se necesita un acorde que contenga do y mi.", "El vi (la-do-mi) tiene las dos."], "El vi"),
    ],
    [
        ("Cambiar un acorde sin mirar las notas de la melodía.", "Si el acorde no contiene las notas de la melodía, suena mal.", "Comprueba que las notas del compás están en el acorde."),
        ("Cambiar el patrón y todos los acordes a la vez.", "No se sabe qué cambio produjo el efecto.", "Cambia una sola cosa y compara."),
    ],
    [
        ex("Un arpegio toca las notas de un acorde, ¿una tras otra o todas a la vez?", "Una tras otra", "Los acordes en bloque son las tres a la vez."),
        ex("El patrón «bajo – acorde – acorde» ¿en qué compás se usa: en 3/4 o en 4/4?", "En 3/4", "Tiene 3 golpes, uno por pulso."),
        ex(f"¿Qué acorde es do-mi-sol? Acordes: {ACORDES}.", "El I", "Es la definición del acorde I."),
    ],
    [
        ex(f"Un compás tiene la melodía mi-sol-mi-sol. ¿Qué acorde la acompaña: I, IV o V? Acordes: {ACORDES}.", "El I", "Solo el I tiene mi y sol juntos."),
        ex("Las notas do-mi-sol tocadas una tras otra forman un arpegio. ¿Cuántas notas tiene una vuelta?", "3", "Son las tres notas del acorde."),
        ex(f"¿Cuántas notas comparten el acorde I y el acorde vi? Acordes: {ACORDES}.", "2", "Comparten do y mi."),
    ],
    [
        ex(f"La melodía del compás es mi-do-mi-do. ¿Qué acorde puede reemplazar al I: el vi o el V? Acordes: {ACORDES}.", "El vi", "El vi tiene mi y do; el V no tiene ninguna de las dos."),
        arith("Una pieza de 8 compases tiene un acorde por compás con la progresión I – IV – V – I repetida 2 veces. ¿Cuántos compases usan el acorde V?", "8//4", "Cada vuelta de 4 compases tiene un compás de V.", " compases"),
        ex("Un arpegio de 4 pulsos toca do-mi-sol-mi. ¿Cuántas veces suena la nota mi?", "2", "Aparece en el segundo y en el cuarto pulso."),
    ],
    [
        ex(f"Acordes: {ACORDES}. El compás tiene una melodía con fa y la, y el acompañamiento usa el acorde V. ¿Qué problema tiene? A) Ninguna de las notas de la melodía está en el acorde. B) El acorde es demasiado largo.", "A", "Ni fa ni la están en sol-si-re."),
        ex("¿Qué final suena más cerrado: V – I o I – V?", "V – I", "Terminar en I da sensación de reposo."),
    ],
    [
        arith("Una progresión de 4 compases I – vi – IV – V se repite 3 veces. ¿Cuántos compases usan IV o V en total?", "3*2", "En cada vuelta hay 2 compases con IV o V.", " compases"),
        arith("Un patrón «bajo – acorde – acorde» se toca durante 10 compases de 3/4. ¿Cuántos golpes de acorde suenan?", "10*2", "En cada compás hay dos golpes de acorde.", " golpes"),
    ],
    [ex(f"Quieres acompañar un compás cuya melodía es fa-la-fa-do. ¿Qué acorde eliges: I, IV o V? Acordes: {ACORDES}.", "El IV", "Es el único acorde que contiene fa, la y do.")],
    [ex("¿Qué es un arpegio?", "Las notas de un acorde, una tras otra", "Suena más suave que los acordes en bloque."), ex("¿Qué es una variación armónica?", "Cambiar un acorde por otro compatible", "Se hace sin que la melodía deje de encajar."), ex("¿Qué acorde da sensación de reposo al final?", "El I", "Es el acorde de llegada.")],
    (
        f"Con la melodía de ejemplo de 2 compases (compás 1: mi-sol-mi-sol; compás 2: do-mi-do-mi) y los acordes ({ACORDES}), crea un acompañamiento en tres versiones. Versión 1: el acorde I en los dos compases en bloque. Versión 2: el acorde I en el compás 1 y el vi en el compás 2. Versión 3: el acorde I en el compás 1 y un arpegio de I en el compás 2. Explica si cada versión sirve para la melodía y qué cambió entre la 1 y la 2. Si puedes, canta la melodía mientras otra persona toca o canta los acordes.",
        "Versión 1 sirve porque el I contiene mi, sol y do. Versión 2 sirve porque el vi contiene do y mi, las notas del compás 2; suena más suave y melancólico. Versión 3 sirve: mismo acorde, otro patrón. Entre la 1 y la 2 cambió el acorde del compás 2.",
        ["comprueba que los acordes contienen las notas de la melodía", "cambia una sola cosa entre versiones", "describe el efecto"],
        ["tres versiones escritas", "explicación de cada una"],
        ["usar un acorde que no contiene las notas", "cambiar varias cosas a la vez"],
        "Reconoce las versiones y pide mostrar, en el compás 2, qué notas de la melodía están en el acorde vi.",
    ),
    "Canta las tres notas do, mi y sol una tras otra y luego juntas con otra persona.",
    "Crea un acompañamiento de bajo – acorde – acorde para un compás de 3/4 con el acorde IV.",
)

# ---------------------------------------------------------------- OA 05 · clase 5 (ensayar y ajustar una creación)
L(
    OA5, 5,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las versiones y los criterios están escritos en los ejercicios. Puedes aplicar lo aprendido con una creación propia de cuatro compases, registrada en números.",
    "Aprenderé a revisar una creación con criterios, ajustarla cambiando una sola cosa y registrar la mejora con evidencia. Sirve para pasar de una primera idea a una versión final bien pensada.",
    ["Sé crear una melodía con reglas.", "Sé hacer una variación rítmica, melódica o armónica.", "Sé contar compases y notas."],
    [
        "Una creación mejora cuando se revisa con criterios. Los criterios son preguntas fijas que se aplican a cada versión. En esta clase usamos cuatro: ¿usa solo las notas permitidas?, ¿tiene los compases pedidos?, ¿tiene una variación que se oye?, ¿termina en la nota 1? Se anota cuántos criterios cumple cada versión, así se puede comparar la versión 1 con la versión 2.",
        "Para ajustar, se elige el criterio que falla y se cambia solo lo necesario. Si una versión no termina en la nota 1, se cambia la última nota y se conserva el resto. Cambiar toda la melodía haría perder lo que ya funcionaba. Después de ajustar, se canta la nueva versión y se vuelve a revisar con los mismos criterios.",
        "Registrar las versiones, en números o en un audio, deja evidencia del trabajo: se puede mostrar cómo era la versión 1, qué se ajustó y cómo quedó la versión 2. Un plan de tiempo también ayuda: por ejemplo, 8 minutos para crear, 4 para revisar, 5 para ajustar y 3 para registrar. Al final se decide si la creación está lista o si hace falta otro ajuste.",
    ],
    [("criterio", "pregunta fija con que se revisa una versión"), ("ajuste", "cambio pequeño que corrige un criterio que falla"), ("versión", "cada forma que toma una creación después de un ajuste"), ("evidencia", "registro que muestra cómo mejoró la creación"), ("variación audible", "cambio que se oye al comparar dos partes de la creación")],
    [
        ("Contar criterios", "Una creación usa solo notas permitidas, tiene 4 compases, no tiene una variación que se oye y termina en la nota 1. ¿Cuántos de los 4 criterios cumple?", ["Cumple notas permitidas, compases y nota final.", "No cumple la variación audible: 3 de 4."], "3 de 4"),
        ("Ajustar una sola cosa", "Una creación termina en la nota 4 y debe terminar en la 1. ¿Qué ajuste conviene: cambiar solo la última nota o rehacer toda la melodía?", ["El único criterio que falla es la nota final.", "Cambiar solo la última nota conserva lo que funcionaba."], "Cambiar solo la última nota"),
    ],
    [
        ("Rehacer toda la creación cuando falla un solo criterio.", "Se pierde lo que ya funcionaba.", "Cambia solo lo que corrige el criterio que falla."),
        ("Mostrar solo la versión final.", "Sin la primera versión no se ve el ajuste.", "Guarda las versiones para mostrar cómo mejoró."),
    ],
    [
        ex("Después de crear la versión 1, ¿qué conviene hacer: revisarla con criterios o borrarla?", "Revisarla con criterios", "Así se detecta qué hay que ajustar."),
        ex("Si un criterio falla, ¿se cambia solo ese aspecto o se rehace todo?", "Solo ese aspecto", "Se conserva lo que funciona."),
        ex("¿Para qué se registra la versión 2?", "Para tener evidencia de la mejora", "Permite compararla con la versión 1."),
    ],
    [
        ex("Reglas: terminar en la nota 1. Una creación termina en 5-3-2-4. ¿Cumple la regla de terminar en la nota 1? Responde sí o no.", "No", "Termina en la nota 4."),
        arith("La versión 1 cumple 2 de 4 criterios y la versión 2 cumple 4 de 4. ¿Cuántos criterios más cumple la versión 2?", "4-2", "Se resta lo que cumple la versión 1 de lo que cumple la 2.", " criterios más"),
        ex("Después de un ajuste, ¿qué es mejor? A) Cambiar solo el último compás para que termine en 1. B) Cambiar toda la melodía.", "A", "Corrige el criterio que falla sin perder lo que ya funcionaba."),
    ],
    [
        ex("Una creación de 4 compases es: 1-2-3-5 | 3-2-1-2 | 1-2-3-5 | 3-2-1-1. ¿Qué compás repite exactamente al compás 1?", "El compás 3", "El compás 3 tiene las mismas notas que el compás 1."),
        ex("En esa misma creación (1-2-3-5 | 3-2-1-2 | 1-2-3-5 | 3-2-1-1), ¿qué compás es una variación del compás 2?", "El compás 4", "Solo cambia la última nota."),
        arith("Un plan de 25 minutos tiene 10 minutos para crear y 5 para revisar. ¿Cuántos minutos quedan para ajustar y registrar?", "25-10-5", "Se restan los minutos ya usados.", " minutos"),
    ],
    [
        ex("La versión 1 cumple las reglas pero no tiene variación. La versión 2 agrega una variación rítmica. ¿Qué criterio mejoró?", "La variación audible", "La versión 2 agrega el cambio que se oye."),
        ex("Un estudiante dice: «Mi primera idea ya cumple las notas permitidas, así que no hace falta revisarla más». ¿Tiene razón? Responde sí o no.", "No", "También hay que revisar los compases, la variación y la nota final."),
    ],
    [
        arith("La versión 1 cumple 1 criterio, la versión 2 cumple 3 y la versión 3 cumple 4. ¿Cuántos criterios más cumple la versión 3 que la versión 1?", "4-1", "Se resta lo que cumple la versión 1 de lo que cumple la 3.", " criterios más"),
        arith("La versión 1 tiene 4 compases con 4 negras cada uno (12 notas en los compases 1 a 3 y 4 notas en el compás 4). En la versión 2, el compás 4 pasa a disminución: cada negra se cambia por dos corcheas. ¿Cuántas notas tiene la versión 2?", "12+8", "Los compases 1 a 3 mantienen sus 12 notas y el compás 4 pasa a 8.", " notas"),
    ],
    [ex("En una muestra de trabajos del curso, ¿qué es mejor mostrar como evidencia? A) La versión 1, el ajuste y la versión 2. B) Solo la última versión.", "A", "Así se ve cómo mejoró la creación.")],
    [ex("¿Qué se hace con los criterios en cada versión?", "Se aplican los mismos", "Así se comparan las versiones."), ex("¿Se puede cambiar toda la melodía para corregir un solo criterio? Responde sí o no.", "No", "Conviene cambiar solo lo necesario."), ex("¿Qué deja evidencia del trabajo?", "Registrar las versiones", "Muestra cómo se avanzó.")],
    (
        f"Usa esta creación de ejemplo ({NOTAS}) con las reglas de la clase (solo notas 1, 2, 3, 5 y 6; 4 compases; terminar en la nota 1): 5-6-5-3 | 3-5-3-2 | 5-6-5-3 | 3-2-1-4. 1) Revisa los cuatro criterios (notas permitidas, compases, variación que se oye, nota final) y anota cuántos cumple. 2) Ajusta una sola cosa (la nota que falla) y escribe la versión 2. 3) Revisa la versión 2 y anota cuántos criterios cumple. 4) Canta las dos versiones y di cuál mostrarías y por qué.",
        "Versión 1: usa la nota 4 (falla), tiene 4 compases, el compás 4 varía respecto de los otros (cumple) y termina en 4 (falla): 2 de 4. Ajuste: cambiar el último compás a 3-2-1-1. Versión 2 cumple los 4 criterios. Se muestran ambas versiones para evidenciar la mejora.",
        ["revisa los cuatro criterios", "ajusta solo lo que falla", "compara las dos versiones con los mismos criterios"],
        ["conteo de criterios por versión", "versión 2 escrita"],
        ["cambiar toda la melodía", "no volver a revisar la versión 2"],
        "Reconoce la revisión y pide explicar qué se conservó de la versión 1 y qué se cambió en la 2.",
    ),
    "Escribe los cuatro criterios de la clase y marca cuántos cumple una melodía de tu cuaderno.",
    "Crea tres versiones de una creación de 4 compases y registra cuántos criterios cumple cada una.",
)
