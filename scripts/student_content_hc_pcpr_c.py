"""Pensamiento computacional y programación (electivo HC, 3.º y 4.º medio): OAC-05 (aplicaciones para dispositivos móviles y con sensores y control), clases 1 a 4, y OAC-06 (uso creativo, respetuoso y responsable de la tecnología y la información personal), clases 1 a 4. Todo en papel: no se arma ningún circuito ni se instala ninguna aplicación; el código y las lecturas de los sensores se dan de ejemplo y se razonan a mano."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel y calculadora simple opcional. No se necesita computador, teléfono ni circuitos: el código, las lecturas de sensores y los casos están escritos en cada enunciado y se razonan a mano. "
             "En los enunciados, «↵» marca el fin de una línea y «··» marca una línea dentro de un bloque. "
             "Si luego pruebas una aplicación o un dispositivo real, hazlo con la supervisión de tu docente, sin conectar nada a la red eléctrica y sin compartir datos personales reales.")
build = make_build(MATERIALS)

O5 = "MA-PCPR-3y4-OAC-05"
O6 = "MA-PCPR-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (de ejemplo, razonada en papel). Maqueta de riego de una maceta: un sensor de humedad entrega un número de 0 (seco) a 100 (mojado) y una bomba pequeña se enciende (1) o se apaga (0). "
     "Programa de control: humedad = leer_sensor() ↵ if humedad < 30: ↵ ··bomba = 1 ↵ else: ↵ ··bomba = 0. "
     "Una app móvil de la maqueta tiene un botón «Regar ahora» y muestra la humedad en pantalla.")
build(
    O5, 1, F,
    use="Aprenderé a identificar los sensores, los actuadores y los eventos de una aplicación para un dispositivo móvil o con sensores, y a precisar las condiciones de su programa de control.",
    prior=["Sé escribir una condición con if y else.", "Sé qué es una variable.", "Sé que un programa recibe entradas y entrega salidas."],
    explain=[
        "Una aplicación para un dispositivo móvil o con sensores combina tres partes: sensores que miden, un programa que decide y actuadores que hacen algo. Un sensor es un dispositivo de entrada que mide una magnitud (humedad, luz, temperatura, inclinación) y entrega un número. Un actuador es un dispositivo de salida que actúa en el entorno, como una luz, un motor o una bomba. La pantalla también es una salida.",
        "Un teléfono tiene sensores propios: el acelerómetro mide el movimiento y la inclinación, el micrófono capta sonido, la cámara capta imágenes y el GPS estima la ubicación. Una app reacciona a eventos, que son cosas que ocurren, como el toque de un botón, una lectura nueva del sensor o el paso del tiempo. Cada evento dispara una acción del programa.",
        "Precisar las condiciones significa indicar con exactitud qué rango entrega el sensor, cuál es el umbral (valor límite) y qué hacer justo en ese valor. «Regar cuando la tierra esté seca» no alcanza: falta decir qué número de humedad es «seca». En la ficha, humedad < 30 enciende la bomba; con humedad igual a 30 la bomba queda apagada. También hay que decidir que la lectura se repita, porque una sola lectura no vigila nada.",
    ],
    vocab=[("sensor", "dispositivo de entrada que mide algo y entrega un valor"), ("actuador", "dispositivo de salida que actúa, como un motor o una luz"), ("evento", "algo que ocurre y dispara una acción"), ("umbral", "valor límite que separa dos decisiones"), ("acelerómetro", "sensor que mide el movimiento y la inclinación"), ("control", "decisión que el programa toma con la lectura de un sensor")],
    worked=[
        ("Seguir el programa de control", "Si leer_sensor() entrega 22, ¿qué valor toma bomba?", ["22 < 30 es verdadero, así que se ejecuta el bloque del if.", "La bomba toma el valor 1."], "bomba = 1: se enciende"),
        ("Clasificar elementos", "En la maqueta, clasifica el sensor de humedad, la bomba, el botón «Regar ahora» y la pantalla.", ["El sensor y el botón entregan información al programa: son entradas.", "La bomba y la pantalla muestran o ejecutan algo: son salidas."], "Entradas: sensor y botón; salidas: bomba y pantalla"),
    ],
    mistakes=[("Confundir sensor con actuador.", "El sensor mide y entrega un valor; el actuador ejecuta una acción.", "Pregunta: «¿entrega información al programa o la recibe para actuar?»."),
              ("Pedir «cuando esté seca» sin dar el número.", "Un programa necesita un valor concreto para comparar.", "Define el umbral y qué ocurre justo en él.")],
    T=[
        ('abc', '{F} ¿Qué es el sensor de humedad en el sistema?', 'Un dispositivo de entrada que mide y entrega un número', 'Un actuador que riega', 'El programa de control', 'El sensor mide la humedad y le entrega el valor al programa.'),
        ('abc', '{F} ¿Qué valor toma bomba si humedad es 45?', '0', '1', '45', '45 < 30 es falso, así que se ejecuta el bloque else y la bomba queda en 0.'),
        ('ab', '¿Cuál de estos es un actuador?', 'Un motor o una luz', 'Un termómetro', 'Un actuador realiza una acción en el entorno; el termómetro solo mide.'),
        ('abc', '{F} ¿Qué valor toma bomba si humedad es exactamente 30?', '0', '1', '30', 'La condición humedad < 30 es falsa con 30, así que la bomba queda en 0.'),
        ('abc', '{F} Cuando la persona toca «Regar ahora», ¿qué evento ocurre?', 'Un evento de pantalla táctil: la acción se ejecuta cuando ocurre el toque', 'Un evento del sensor de humedad', 'Un evento del reloj', 'El toque del botón es un evento generado por la persona usuaria en la pantalla.'),
        ('abc', 'En un teléfono, ¿qué sensor mide la inclinación o el movimiento?', 'El acelerómetro', 'El micrófono', 'La batería', 'El acelerómetro detecta los cambios de movimiento e inclinación del aparato.'),
        ('{F} Con humedad = 12, ¿qué valor toma bomba?', '1', '12 < 30 es verdadero, así que se enciende la bomba.'),
        ('abc', 'Una luz de pasillo debe encenderse si el sensor de luz mide menos de 20 (0 = oscuro y 100 = claro). ¿Qué condición se usa?', 'luz < 20', 'luz > 20', 'luz == 20', 'La luz debe encenderse cuando hay poca luz, es decir, valores menores que 20.'),
        ('abc', 'En un reloj inteligente de ejemplo, el sensor de pulso entrega un número y la pantalla lo muestra. ¿Cuáles son la entrada y la salida?', 'Entrada: el sensor; salida: la pantalla', 'Entrada: la pantalla; salida: el sensor', 'Ambas son entradas', 'El sensor entrega el dato al programa y la pantalla muestra el resultado.'),
        ('abc', '{F} Alguien cambia la condición a humedad <= 30. ¿Qué cambia?', 'Con humedad exactamente 30 la bomba se enciende (antes no)', 'Nada', 'La bomba nunca se enciende', 'El signo <= incluye el valor 30, que antes quedaba fuera de la condición.'),
        ('abc', 'Un diseñador pide «que el riego se active cuando la tierra esté seca». ¿Por qué falta precisión para programarlo?', 'No dice qué valor del sensor es «seca» (umbral) ni qué hacer en el límite', 'Porque las bombas no se programan', 'Porque no existen sensores de humedad', 'Un programa compara números, y «seca» debe traducirse a un valor concreto.'),
        ('abc', '{F} El programa lee el sensor solo una vez, al encender. ¿Qué problema tiene?', 'No reacciona si la humedad cambia después: falta repetir la lectura en un ciclo', 'Funciona igual que con un ciclo, porque el sensor se lee solo', 'La bomba nunca se enciende porque humedad vale siempre 0', 'Una sola lectura deja la bomba en el estado inicial sin vigilar los cambios.'),
        ('abc', 'Una app de cronómetro necesita mostrar el tiempo y recibir toques en «iniciar» y «detener». ¿Qué sensor del teléfono no necesita?', 'El GPS', 'El reloj interno', 'La pantalla táctil', 'El cronómetro usa el tiempo y los toques; la ubicación no aporta nada.'),
    ],
    ctx=('abc', 'Una maqueta de semáforo para peatones tiene un botón (entrada) y tres luces (salida). Al apretar el botón, 5 segundos después la luz roja de los autos se enciende. ¿Qué evento inicia la secuencia?', 'El toque del botón', 'El paso de los 5 segundos', 'El apagado de la luz verde', 'La secuencia parte cuando la persona aprieta el botón; el paso del tiempo es un evento posterior.'),
    sc=[
        ("En sistemas con sensores: ¿qué hace un sensor?", "Mide algo del entorno y entrega un valor al programa", "El sensor es una entrada que convierte una magnitud en un número."),
        ("En sistemas con sensores: ¿qué hace un actuador?", "Ejecuta una acción, como encender una luz o mover un motor", "El actuador es una salida que actúa en el entorno."),
        ("En una app: ¿qué es un evento?", "Algo que ocurre y dispara una acción, como el toque de un botón", "El programa reacciona a eventos como toques, lecturas o el paso del tiempo."),
    ],
    op=("Elige una idea: (a) lámpara de velador que se enciende si hay poca luz (sensor de luz de 0 a 100); (b) ventilador de maqueta que se enciende sobre 28 °C; (c) alarma de mochila que suena si el acelerómetro detecta movimiento cuando la mochila está bloqueada. "
        "Escribe: los sensores, los actuadores, los eventos, el umbral con su valor, y un programa de control de cinco líneas o menos. Pruébalo a mano con dos lecturas, una de ellas justo en el umbral.",
        "(a) Sensor de luz; actuador: la lámpara; umbral 20. luz = leer_sensor() ↵ if luz < 20: ↵ ··lampara = 1 ↵ else: ↵ ··lampara = 0. Con luz = 10: lámpara 1; con luz = 20, que es el umbral: lámpara 0.",
        ["identifica sensores, actuadores y eventos", "define un umbral concreto", "prueba el programa incluyendo el valor límite"],
        ["hoja con la lista de componentes, el programa y las dos pruebas"],
        ["confundir sensor con actuador", "dejar el umbral sin un número", "no probar el valor del umbral"],
        "Pregunta: «¿qué hace tu programa exactamente en el valor del umbral?». Si no lo sabe, pídele que lo siga a mano."),
    reinforce="Haz una tabla con tres sensores y tres actuadores que conozcas de la vida diaria y escribe qué magnitud mide o qué acción hace cada uno.",
    extend="Explica por qué un programa de control debe repetir la lectura del sensor y qué pasaría si no lo hiciera.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (de ejemplo). Semáforo de una maqueta con tres estados: VERDE, AMARILLO y ROJO. Reglas de cambio: VERDE pasa a AMARILLO cuando han pasado 20 segundos en VERDE; AMARILLO pasa a ROJO tras 3 segundos; ROJO pasa a VERDE tras 25 segundos. "
     "Representación 1: tabla de transiciones con las columnas estado actual, evento y estado siguiente. Representación 2: pseudocódigo, por ejemplo «si el estado es VERDE y pasaron 20 segundos, el estado pasa a AMARILLO y el contador vuelve a 0».")
build(
    O5, 2, F,
    use="Aprenderé a representar el comportamiento de un dispositivo con estados, eventos y transiciones, en una tabla y en pseudocódigo, y a revisar si la representación está completa.",
    prior=["Sé qué es un sensor y un evento.", "Sé leer una tabla de tres columnas.", "Sé escribir condiciones con si… entonces…."],
    explain=[
        "Muchos dispositivos se comportan como una máquina de estados: en cada momento están en un estado (por ejemplo VERDE) y pasan a otro cuando ocurre un evento (como el paso de 20 segundos). El cambio se llama transición. Para describirla se indica el estado actual, el evento y el estado siguiente. El sistema parte en un estado inicial.",
        "Un mismo comportamiento se puede representar de dos maneras: una tabla de transiciones, que permite ver de un vistazo si cada estado tiene todas sus salidas, y un pseudocódigo, que describe los pasos de la lógica. Con el semáforo de la ficha, un ciclo completo dura 20 + 3 + 25 = 48 segundos: de 0 a 20 está en VERDE, de 20 a 23 en AMARILLO y de 23 a 48 en ROJO.",
        "Al diseñar se revisa que la representación esté completa. Si a un estado le falta la regla de salida, el sistema se queda atrapado en él. Si un estado no tiene ninguna transición que llegue a él, es un estado inalcanzable y sobra. También se decide qué pasa con un evento que no está previsto en un estado: la tabla debe indicarlo, por ejemplo, «sin cambio» o un mensaje de error.",
    ],
    vocab=[("estado", "situación en que se encuentra el sistema"), ("evento", "algo que ocurre y puede provocar un cambio"), ("transición", "paso de un estado a otro"), ("estado inicial", "estado en que parte el sistema"), ("estado inalcanzable", "estado al que ninguna transición llega"), ("tabla de transiciones", "lista de estado actual, evento y estado siguiente")],
    worked=[
        ("Ubicar el estado en el tiempo", "Si el semáforo parte en VERDE en t = 0 s, ¿en qué estado está a los 24 s?", ["VERDE dura de 0 a 20 s y AMARILLO de 20 a 23 s.", "A los 24 s ya comenzó ROJO, que va de 23 a 48 s."], "Está en ROJO"),
        ("Revisar una tabla", "Una puerta automática tiene los estados CERRADA y ABIERTA; «persona detectada» lleva de CERRADA a ABIERTA y «pasan 5 s sin persona» lleva de ABIERTA a CERRADA. ¿Está completa?", ["CERRADA tiene salida con «persona detectada»; ABIERTA tiene salida con «pasan 5 s».", "Falta decir qué ocurre con «persona detectada» estando ABIERTA (por ejemplo, reiniciar los 5 s)."], "Casi completa: falta definir un evento en un estado"),
    ],
    mistakes=[("Olvidar la transición de salida de un estado.", "El sistema se queda en ese estado para siempre.", "Revisa que cada estado tenga al menos una salida."),
              ("Contar los tiempos desde el comienzo en cada estado, sin acumularlos.", "El ROJO empieza a los 23 segundos, no a los 3.", "Suma las duraciones de los estados anteriores.")],
    T=[
        ('abc', '{F} ¿Qué estado sigue después de AMARILLO?', 'ROJO', 'VERDE', 'AMARILLO', 'La ficha indica que AMARILLO pasa a ROJO tras 3 segundos.'),
        ('abc', '{F} ¿Cuántos estados tiene el semáforo de la ficha?', '3', '4', '48', 'Los estados son VERDE, AMARILLO y ROJO; 48 es la duración del ciclo en segundos.'),
        ('ab', 'En una tabla de transiciones, ¿qué columnas dan la información para pasar de un estado a otro?', 'Estado actual, evento y estado siguiente', 'Solo el estado siguiente', 'Para cambiar de estado se necesita saber dónde se está, qué ocurrió y a dónde se va.'),
        ('=', '{F} Un ciclo completo dura 48 segundos. ¿Cuántos ciclos completos caben en 100 segundos?', '100//48', 'Con dos ciclos van 96 segundos; con tres serían 144, que no caben en 100.'),
        ('abc', '{F} Si el semáforo parte en VERDE en t = 0 s, ¿en qué estado está a los 21 s?', 'AMARILLO', 'VERDE', 'ROJO', 'VERDE termina a los 20 s y AMARILLO va de 20 a 23 s.'),
        ('abc', '{F} Si parte en VERDE en t = 0 s, ¿en qué estado está a los 30 s?', 'ROJO', 'AMARILLO', 'VERDE', 'ROJO va de 23 a 48 segundos, y 30 está dentro de ese intervalo.'),
        ('abc', '{F} Si parte en VERDE en t = 0 s, ¿en qué estado está a los 50 s?', 'VERDE', 'ROJO', 'AMARILLO', 'El ciclo dura 48 s y 50 − 48 = 2 s, que corresponden a los primeros segundos de VERDE.'),
        ('{F} El semáforo lleva 10 segundos en ROJO. ¿Cuántos segundos faltan para que pase a VERDE?', '15 segundos', 'ROJO dura 25 segundos y ya pasaron 10: 25 − 10 = 15.'),
        ('abc', 'Un portón tiene los estados CERRADO y ABIERTO. Solo existe la regla «se presiona el control» que lleva de CERRADO a ABIERTO. Estando CERRADO, ocurre el evento «pasan 30 s sin nada». ¿Qué estado resulta?', 'CERRADO: no hay transición definida para ese evento en ese estado', 'ABIERTO', 'Un error del sensor', 'La tabla no tiene una regla para ese evento en CERRADO, así que el estado no cambia.'),
        ('abc', '{F} Un programador olvida la regla de salida de ROJO. ¿Qué ocurre?', 'El semáforo se queda en ROJO para siempre', 'Pasa a VERDE igual', 'Se apaga', 'Sin la transición de salida, el sistema no tiene cómo abandonar el estado.'),
        ('abc', '¿Qué ventaja tiene la tabla de transiciones frente al pseudocódigo para revisar un sistema de estados?', 'Permite ver de un vistazo si cada estado tiene todas sus transiciones', 'Se ejecuta más rápido', 'No necesita estados', 'En una tabla las filas muestran cada combinación de estado y evento, así se detectan los vacíos.'),
        ('=', '{F} Se agrega un cuarto estado, PEATONES, de 10 s, entre ROJO y VERDE. ¿Cuánto dura ahora un ciclo completo?', '20+3+25+10', 'Se suma la duración del estado nuevo a las de los tres anteriores.', ' segundos'),
        ('abc', 'Se diseña un estado «TODAS LAS LUCES APAGADAS» al que no llega ninguna transición. ¿Cómo se llama este problema?', 'Estado inalcanzable', 'Evento duplicado', 'Estado inicial', 'Un estado al que ninguna transición lleva nunca se alcanza y sobra en el diseño.'),
    ],
    ctx=('abc', 'Un cajero de estacionamiento de ejemplo tiene los estados ESPERANDO, COBRANDO y PUERTA_ABIERTA. Las transiciones son: llega auto (ESPERANDO a COBRANDO), pago correcto (COBRANDO a PUERTA_ABIERTA) y auto pasó (PUERTA_ABIERTA a ESPERANDO). ¿Qué debe hacerse con el evento «pago incorrecto»?', 'Agregar una regla para ese evento, por ejemplo volver a COBRANDO', 'Dejarlo sin regla', 'Pasar a PUERTA_ABIERTA', 'La tabla no define ese evento; un diseño completo debe indicar qué hace el sistema.'),
    sc=[
        ("En control de dispositivos: ¿qué es un estado?", "La situación en que se encuentra el sistema", "Por ejemplo, un semáforo puede estar en VERDE, AMARILLO o ROJO."),
        ("En control de dispositivos: ¿qué es una transición?", "El paso de un estado a otro cuando ocurre un evento", "La transición une un estado actual con un estado siguiente."),
        ("¿Qué estado debe indicarse para que el sistema pueda comenzar?", "El estado inicial", "Sin un estado inicial no se sabe desde dónde empieza el sistema."),
    ],
    op=("Elige uno. Caso 1: una puerta automática con estados CERRADA, ABIERTA y BLOQUEADA. Caso 2: un ventilador con estados APAGADO, BAJO y ALTO, donde cada vez que se presiona el botón se pasa al siguiente (APAGADO a BAJO, BAJO a ALTO, ALTO a APAGADO). "
        "Escribe la tabla de transiciones completa, el pseudocódigo y la secuencia de estados que resulta de cinco eventos, partiendo del estado inicial. Revisa que cada estado tenga una salida.",
        "Caso 2: estado inicial APAGADO. Cinco presiones del botón dan: BAJO, ALTO, APAGADO, BAJO y ALTO. El estado final es ALTO. Cada estado tiene una salida: APAGADO, BAJO y ALTO.",
        ["escribe una tabla completa con estado, evento y siguiente", "sigue la secuencia de estados correctamente", "revisa que cada estado tenga salida"],
        ["hoja con la tabla, el pseudocódigo y la secuencia de estados"],
        ["dejar un estado sin salida", "no indicar el estado inicial", "equivocarse al seguir la secuencia"],
        "Pregunta: «¿en qué estado estás después del evento 3?». Si no coincide, repasa la tabla fila por fila."),
    reinforce="Con la tabla del ventilador, escribe la secuencia de estados tras 4 presiones del botón, partiendo de APAGADO.",
    extend="Explica cómo cambiarías la tabla de la puerta automática para agregar un botón de bloqueo y qué eventos debería ignorar el estado BLOQUEADA.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (de ejemplo, razonada en papel). Control de un calefactor de maqueta con un sensor de temperatura (°C, números enteros). El calefactor parte apagado (0). "
     "Versión 1: si temp < 20: calefactor = 1; si no: calefactor = 0. "
     "Versión 2 (con histéresis, o sea, dos umbrales): si temp < 18: calefactor = 1; si temp > 22: calefactor = 0; en cualquier otro caso queda como estaba. "
     "Serie de lecturas de ejemplo, una por instante: 17, 19, 21, 19, 17, 19, 23.")
build(
    O5, 3, F,
    use="Aprenderé a diseñar un ciclo de control que lee un sensor, decide y actúa, y a usar dos umbrales para que el actuador no cambie sin parar.",
    prior=["Sé qué es un umbral y un actuador.", "Sé seguir un programa con condiciones.", "Sé leer una serie de datos."],
    explain=[
        "Un programa de control repite tres pasos: leer el sensor, decidir y actuar. Por eso lleva un ciclo que no termina mientras el dispositivo esté encendido. La decisión compara la lectura con un umbral: en la versión 1 del calefactor, con temp < 20 se enciende y en caso contrario se apaga. Con una lectura cerca del umbral, el actuador puede encenderse y apagarse muchas veces seguidas.",
        "La histéresis evita eso con dos umbrales: se enciende bajo 18, se apaga sobre 22 y, entre 18 y 22, queda como estaba. Con la serie 17, 19, 21, 19, 17, 19, 23, la versión 1 produce los estados 1, 1, 0, 1, 1, 1, 0 (cuatro cambios desde el estado inicial 0), mientras la versión 2 produce 1, 1, 1, 1, 1, 1, 0 (solo dos cambios). Menos cambios significan menos desgaste del actuador.",
        "Al diseñar un control también se decide qué hacer si el sensor falla. Por ejemplo, si entrega un valor imposible como −999, lo más seguro para un calefactor es apagarlo y avisar del fallo. Siempre se prueba el control a mano con una serie de lecturas que incluya valores bajo, dentro y sobre los umbrales.",
    ],
    vocab=[("ciclo de control", "repetición de leer, decidir y actuar"), ("histéresis", "uso de dos umbrales para evitar cambios rápidos"), ("umbral", "valor límite que separa dos decisiones"), ("estado anterior", "valor que tenía el actuador antes de la lectura"), ("falla segura", "comportamiento que evita daños si algo falla")],
    worked=[
        ("Versión 1 con la serie", "¿Qué estados toma el calefactor con la versión 1 y las lecturas 17, 19, 21, 19, 17, 19, 23?", ["Con temp < 20: 17 da 1, 19 da 1, 21 da 0, 19 da 1, 17 da 1, 19 da 1 y 23 da 0.", "La serie de estados es 1, 1, 0, 1, 1, 1, 0."], "Estados: 1, 1, 0, 1, 1, 1, 0"),
        ("Versión 2 con la serie", "¿Qué estados toma con la versión 2 (parte en 0)?", ["17 < 18 enciende (1); luego 19, 21, 19, 17 y 19 no superan 22, así que el calefactor sigue en 1.", "23 > 22 apaga (0)."], "Estados: 1, 1, 1, 1, 1, 1, 0"),
    ],
    mistakes=[("Poner el actuador en 0 en la zona intermedia de la histéresis.", "En esa zona debe quedar como estaba.", "Escribe «en otro caso, sin cambio» y úsalo en el programa."),
              ("Leer el sensor una sola vez.", "El control no vigila los cambios posteriores.", "Pon la lectura y la decisión dentro de un ciclo.")],
    T=[
        ('abc', '{F} Con la versión 1, ¿qué valor toma calefactor si temp = 19?', '1', '0', '19', '19 < 20 es verdadero, así que el calefactor se enciende.'),
        ('abc', '{F} Con la versión 2, el calefactor está encendido y la lectura es 20. ¿Qué ocurre?', 'Sigue encendido, igual que antes', 'Se apaga', 'Cambia de estado cada vez que se lee', '20 no es menor que 18 ni mayor que 22, así que no hay cambio.'),
        ('ab', '¿Qué problema busca evitar la histéresis?', 'Que el actuador se encienda y apague sin parar cuando la lectura está cerca del umbral', 'Que el sensor se descargue', 'Con dos umbrales hay una zona intermedia sin cambios, que reduce los encendidos y apagados repetidos.'),
        ('abc', '{F} Con la versión 1, partiendo en 0, y las lecturas 19, 21, 19, 21, 19, 17, ¿cuántas veces cambia de estado el calefactor?', '5', '3', '6', 'Los estados son 1, 0, 1, 0, 1, 1; contando el estado inicial 0 hay cambios en las primeras cinco lecturas y la sexta no cambia.'),
        ('abc', '{F} Con la versión 2, partiendo en 0, y las mismas lecturas 19, 21, 19, 21, 19, 17, ¿cuántas veces cambia de estado el calefactor?', '1', '0', '5', 'Las lecturas entre 18 y 22 no cambian nada; solo el 17 final (menor que 18) lo enciende.'),
        ('abc', '{F} Con la versión 2, el calefactor estaba en 1 y llega la lectura 23. ¿Qué valor toma?', '0', '1', '23', '23 > 22 cumple la regla de apagado.'),
        ('{F} Con la versión 2 y el estado anterior 0, la lectura es 17. ¿Qué valor toma calefactor?', '1', '17 < 18 cumple la regla de encendido.'),
        ('abc', 'Un ventilador de ejemplo debe encenderse sobre 28 °C y apagarse bajo 24 °C (histéresis). Está encendido y la lectura es 26. ¿Qué hace?', 'Sigue encendido', 'Se apaga', 'Se enciende de nuevo', '26 está entre 24 y 28, en la zona intermedia donde no cambia el estado.'),
        ('abc', 'Un estudiante escribe: temp = leer() y luego if temp < 20: calefactor = 1. ¿Qué debe agregar para que el sistema vigile de forma continua?', 'Un ciclo que repita la lectura y la decisión', 'Otra variable', 'Un segundo sensor', 'Sin un ciclo, la lectura y la decisión se hacen una sola vez.'),
        ('abc', '{F} Una persona dice que la versión 1 es «más correcta» porque es más simple. ¿Qué respuesta es más completa?', 'Ambas cumplen su regla, pero la 1 cambia mucho cerca de 20 °C y puede desgastar el calefactor; la 2 lo reduce', 'La 1 siempre es mejor', 'La 2 no funciona', 'La simplicidad tiene un costo: más cambios del actuador cerca del umbral.'),
        ('abc', 'El sensor falla y entrega el valor −999, que es imposible. ¿Qué decisión es más segura para un calefactor?', 'Apagarlo y avisar del fallo', 'Encenderlo al máximo', 'Ignorar el valor y seguir igual', 'Ante un dato imposible, el estado más seguro es el que evita calentar sin control.'),
        ('{F} Con la versión 2 (parte en 0) y las lecturas 20, 17, 20, 23 y 20, ¿qué valores toma calefactor tras cada lectura? Escribe la lista.', '0, 1, 1, 0, 0', '20 no cambia (0); 17 enciende (1); 20 no cambia (1); 23 apaga (0); 20 no cambia (0).'),
        ('abc', 'Un riego con histéresis se enciende bajo 30 y se apaga sobre 60 de humedad. Está apagado y la lectura es 45. ¿Qué ocurre?', 'Sigue apagado', 'Se enciende', 'Alterna entre encendido y apagado', '45 está entre los dos umbrales, así que el riego queda como estaba, apagado.'),
    ],
    ctx=('abc', 'Una maqueta de invernadero abre una ventana (1) si la temperatura supera 26 °C y la cierra (0) si baja de 22 °C; entre ambos valores queda como estaba. Parte cerrada y las lecturas son 20, 24, 27, 25 y 21. ¿En qué estado queda tras la última lectura?', 'Cerrada (0)', 'Abierta (1)', 'Vuelve al estado inicial siempre', '27 la abre y 25 no cambia; 21 es menor que 22 y la cierra.'),
    sc=[
        ("En control de dispositivos: ¿qué tres pasos repite un programa de control?", "Leer el sensor, decidir y actuar", "Ese ciclo permite vigilar el entorno de forma continua."),
        ("En control de dispositivos: ¿qué es un umbral?", "Un valor límite que separa dos decisiones", "Por ejemplo, 20 °C separa «encender» de «apagar»."),
        ("¿Cuántos umbrales usa la histéresis?", "Dos", "Uno para encender y otro para apagar, con una zona intermedia."),
    ],
    op=("Elige una opción. Opción 1: un estanque con un sensor de nivel de 0 a 100 y una bomba que se enciende bajo 20 y se apaga sobre 80 (entre ambos valores queda como estaba). Opción 2: un ventilador que se enciende sobre 28 °C y se apaga bajo 24 °C. "
        "Escribe el programa de control con histéresis y síguelo a mano con una serie de siete lecturas que tú elijas (con valores bajo, dentro y sobre los umbrales), anotando el estado tras cada lectura. Escribe qué haría el sistema si el sensor entrega un valor imposible.",
        "Opción 1 con lecturas 15, 40, 85, 60, 30, 18 y 90, partiendo apagada: estados 1, 1, 0, 0, 0, 1 y 0. Si el sensor entrega −999: apagar la bomba y avisar del fallo.",
        ["escribe el programa con dos umbrales y zona intermedia", "sigue la serie de lecturas sin errores", "define una conducta segura ante un valor imposible"],
        ["hoja con el programa, la tabla de lecturas y estados, y la regla de falla segura"],
        ["cambiar el estado en la zona intermedia", "no incluir un ciclo", "no prever el valor imposible"],
        "Pregunta: «¿qué hace tu sistema con una lectura entre los dos umbrales?». Si responde que cambia, repasa la histéresis."),
    reinforce="Sigue a mano la versión 1 y la versión 2 de la ficha con las lecturas 21, 19, 21, 19 y compara cuántos cambios hace cada una.",
    extend="Explica por qué una zona intermedia más ancha reduce los cambios del actuador pero también hace menos precisa la temperatura.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (de ejemplo). Un sensor de distancia (cm) entrega lecturas con ruido: 50, 52, 48, 90, 51, 49 (el 90 es un pico falso). "
     "Suavizado por promedio de las últimas 3 lecturas: s(k) = (L(k) + L(k−1) + L(k−2)) // 3, desde la tercera lectura. "
     "Una app móvil de ejemplo puede pedir permisos (cámara, micrófono, ubicación, contactos). Principio de mínimo permiso: pedir solo lo que la función necesita. "
     "Leer un sensor 10 veces por segundo gasta más batería que leerlo 1 vez por segundo.")
build(
    O5, 4, F,
    use="Aprenderé a suavizar las lecturas ruidosas de un sensor, a justificar cuántas lecturas hacer y a decidir qué permisos pide una app según lo que realmente necesita.",
    prior=["Sé calcular un promedio con la división entera.", "Sé qué es un sensor y una lectura.", "Sé que una app móvil usa sensores y permisos."],
    explain=[
        "Las lecturas de un sensor traen ruido: variaciones o errores que no corresponden a la realidad. Un pico falso puede hacer que el programa decida mal. Un método simple es suavizar: en vez de usar la última lectura, se usa el promedio de las últimas 3. Con las lecturas 50, 52, 48, 90, 51 y 49, los valores suavizados desde la tercera lectura son 50, 63, 63 y 63.",
        "El suavizado tiene un costo. El pico de 90 no desaparece: entra en tres promedios y los eleva. Y si se promedian muchas lecturas, la respuesta se vuelve lenta para reflejar los cambios reales; un robot que frena al detectar un obstáculo a menos de 20 cm podría frenar tarde. Se elige la cantidad de lecturas comparando suavidad con rapidez de reacción.",
        "También se decide cuántas veces se lee el sensor. Leer 10 veces por segundo durante 60 segundos son 600 lecturas, contra 60 si se lee 1 vez por segundo; más lecturas dan más detalle, pero gastan más batería. Y una app debe pedir solo los permisos que su función necesita: una app de cronómetro no necesita la ubicación ni los contactos. Pedir de más expone datos personales sin motivo.",
    ],
    vocab=[("ruido", "variación o error no deseado en las lecturas"), ("pico falso", "lectura aislada y muy distinta de las demás"), ("promedio móvil", "promedio de las últimas lecturas"), ("frecuencia de lectura", "cuántas veces por segundo se lee el sensor"), ("permiso", "autorización que se da a una app para usar un sensor o dato"), ("mínimo permiso", "pedir solo lo necesario para la función")],
    worked=[
        ("Calcular un valor suavizado", "Con las lecturas de la ficha, calcula s(3) y s(4).", ["s(3) = (50 + 52 + 48) // 3 = 150 // 3 = 50.", "s(4) = (52 + 48 + 90) // 3 = 190 // 3 = 63."], "s(3) = 50 y s(4) = 63"),
        ("Elegir los permisos", "Una app de calculadora pide ubicación, micrófono y contactos. ¿Cuáles son necesarios para sumar y multiplicar?", ["Una calculadora solo recibe toques y muestra números en la pantalla.", "Ninguno de esos permisos aporta a esa función."], "Ninguno: pedirlos viola el principio de mínimo permiso"),
    ],
    mistakes=[("Creer que el promedio de 3 lecturas elimina por completo un pico falso.", "El pico queda repartido en tres valores suavizados.", "Cuenta en cuántos promedios entra cada lectura."),
              ("Aceptar todos los permisos que pide una app.", "Cada permiso innecesario expone datos personales.", "Pregunta si la función funciona sin ese permiso.")],
    T=[
        ('abc', '{F} ¿Qué lectura de la serie parece un pico falso?', '90', '48', '52', 'El 90 está muy lejos de las demás lecturas, que están entre 48 y 52.'),
        ('abc', '{F} ¿Cuánto vale s(5), el promedio de 48, 90 y 51?', '63', '90', '189', 'La suma es 189 y 189 // 3 = 63; 189 es la suma sin dividir y 90 es solo el pico.'),
        ('ab', '¿Para qué sirve suavizar las lecturas de un sensor?', 'Reducir el efecto del ruido', 'Aumentar el ruido', 'Promediar lecturas amortigua los picos falsos y hace más estable el valor.'),
        ('=', '{F} Si la lectura 90 fuera en realidad 50, ¿cuánto valdría s(4), con las lecturas 52, 48 y 50?', '(52+48+50)//3', 'La suma es 150 y 150 // 3 = 50: sin el pico falso, el valor suavizado es parecido al resto.'),
        ('=', '{F} ¿Cuánto vale s(6), con las lecturas 90, 51 y 49?', '(90+51+49)//3', 'La suma es 190 y se divide por 3.'),
        ('abc', '{F} Con el promedio de 3, ¿el pico de 90 desaparece del todo?', 'No: afecta a tres valores suavizados porque entra en tres promedios', 'Sí, desaparece por completo', 'Solo afecta al primer valor suavizado', 'El 90 aparece en s(4), s(5) y s(6), todos cerca de 63.'),
        ('=', 'Tres lecturas de ejemplo son 30, 32 y 31. ¿Cuánto vale su promedio de 3 con //?', '(30+32+31)//3', 'La suma es 93 y 93 // 3 = 31.'),
        ('=', 'Una app lee un sensor 8 veces por segundo durante 45 segundos. ¿Cuántas lecturas hace?', '8*45', 'Se multiplica la frecuencia de lectura por el tiempo.'),
        ('abc', 'Una app de despertador pide permiso de micrófono y de ubicación. ¿Qué decisión respeta el mínimo permiso?', 'No conceder micrófono ni ubicación, porque la función no los necesita', 'Conceder todos los permisos', 'Conceder solo el micrófono', 'Un despertador funciona sin escuchar el ambiente ni saber dónde estás.'),
        ('abc', '{F} Una persona propone promediar las últimas 20 lecturas para eliminar el ruido por completo. ¿Qué inconveniente principal tiene?', 'La respuesta se vuelve lenta: tarda en reflejar los cambios reales', 'No tiene inconvenientes', 'El sensor se rompe', 'Mientras más lecturas se promedian, más tarda en notarse un cambio real.'),
        ('abc', 'Un robot de maqueta debe frenar si algo está a menos de 20 cm, pero usa un promedio de 20 lecturas. Un obstáculo aparece de golpe. ¿Qué riesgo hay?', 'Frenar tarde, porque el promedio tarda en reflejar la distancia real', 'Frenar antes de tiempo', 'Ninguno', 'Un promedio largo retrasa la respuesta, algo grave en una decisión de seguridad.'),
        ('{F} Con las seis lecturas y el promedio de 3 desde la tercera, ¿cuántos valores suavizados superan 60?', '3', 'Los valores suavizados son 50, 63, 63 y 63, y tres superan 60.'),
        ('abc', 'Una app de ejemplo lee el acelerómetro 50 veces por segundo para contar pasos y la batería dura poco. ¿Qué cambio razonable reduce el consumo?', 'Bajar la frecuencia de lectura hasta un valor suficiente para detectar pasos', 'Subir la frecuencia de lectura', 'Quitar la pantalla', 'Menos lecturas gastan menos batería, siempre que alcancen para detectar cada paso.'),
    ],
    ctx=('abc', 'Un sensor de temperatura de ejemplo entrega 20, 21, 20, 35, 21 (el 35 es un error). Con el promedio de 3 desde la tercera lectura, ¿cuál es el mayor valor suavizado?', '25', '35', '20', 's(3) = 20, s(4) = 76 // 3 = 25 y s(5) = 76 // 3 = 25; el error de 35 se reparte.'),
    sc=[
        ("En sensores: ¿qué es el ruido?", "La variación o el error no deseado en las lecturas", "El ruido hace que la lectura se aleje de la realidad."),
        ("En una app móvil: ¿qué principio guía los permisos que se piden?", "Pedir solo los permisos que la función necesita", "Es el principio del mínimo permiso."),
        ("¿Qué ocurre con la batería si se lee un sensor con mucha más frecuencia?", "Se gasta más", "Cada lectura del sensor consume algo de energía de la batería."),
    ],
    op=("Elige una opción. Opción 1: lecturas de un sensor de luz de ejemplo: 80, 82, 81, 10, 83, 82 (el 10 es un error). Calcula los valores suavizados con el promedio de 3 desde la tercera lectura, y escribe cuántos valores quedan afectados por el error. "
        "Opción 2: una app escolar de ejemplo pide los permisos ubicación, cámara, micrófono y contactos; decide cuáles necesita para (a) mostrar el camino a la escuela y (b) escanear un código QR del curso, y justifica.",
        "Opción 1: s(3) = 81, s(4) = 173 // 3 = 57, s(5) = 174 // 3 = 58 y s(6) = 175 // 3 = 58. El error de 10 afecta a tres valores. Opción 2 (a): ubicación; (b): cámara; micrófono y contactos no se necesitan.",
        ["calcula bien los valores suavizados o decide los permisos con criterio", "indica cuántos valores afecta el error o qué se evita", "justifica con el principio del mínimo permiso"],
        ["hoja con los cálculos o la tabla de permisos y la justificación"],
        ["dividir por un número distinto de 3", "pensar que el error desaparece", "conceder permisos sin razón"],
        "Pregunta: «¿en cuántos promedios entra el valor erróneo?». Si dice uno, repasa cómo se arma cada promedio."),
    reinforce="Con las lecturas 10, 12, 11, 40, 13, calcula los valores suavizados desde la tercera lectura.",
    extend="Explica cómo elegirías entre promediar 3 y promediar 10 lecturas para un sensor que debe reaccionar rápido.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (de ejemplo). La app de un club escolar de ejemplo pide, al inscribirse: nombre, curso, correo, teléfono, número de cédula, foto, lugar donde vive la persona y qué alimentos no puede comer (para la once del club). "
     "Un dato personal permite identificar a una persona. Un dato sensible afecta su intimidad, seguridad o dignidad (por ejemplo, salud, ubicación exacta, número de cédula o contraseñas).")
build(
    O6, 1, F,
    use="Aprenderé a distinguir datos personales y sensibles, a reconocer la huella digital y a decidir qué datos pedir y guardar con responsabilidad.",
    prior=["Sé qué es un dato.", "Sé qué es un formulario en una app o una página.", "Sé que lo que se publica en línea puede copiarse."],
    explain=[
        "Un dato personal es cualquier información que permite identificar a una persona: nombre, correo, teléfono, curso, foto. Entre ellos, los datos sensibles afectan más la intimidad o la seguridad: la salud, la ubicación exacta, el número de cédula, las contraseñas. Todo lo que dejamos al usar servicios digitales forma la huella digital, el rastro de datos que queda y puede ser copiado o compartido.",
        "Usar la tecnología de forma responsable incluye pedir y guardar solo lo necesario. Eso se llama minimización: cada dato debe tener una finalidad clara y una persona debe poder aceptar o negarse (consentimiento). Si el club solo necesita avisar la fecha de la once, no necesita el número de cédula ni el lugar donde vives. Cada dato guardado de más puede filtrarse o usarse mal.",
        "Al diseñar o usar una app conviene preguntarse: ¿para qué se pide este dato?, ¿funciona sin él?, ¿quién lo verá y por cuánto tiempo? Si alguien pide datos o claves y te incomoda, no los entregues y avisa a una persona adulta de confianza. Y al publicar la imagen o los datos de otras personas se pide su permiso antes, porque la privacidad de los demás también se respeta.",
    ],
    vocab=[("dato personal", "información que permite identificar a una persona"), ("dato sensible", "dato que afecta la intimidad, la seguridad o la dignidad"), ("huella digital", "rastro de datos que dejamos al usar servicios digitales"), ("minimización", "pedir y guardar solo los datos necesarios"), ("finalidad", "para qué se usa un dato"), ("consentimiento", "aceptación libre e informada de una persona")],
    worked=[
        ("Clasificar datos", "En la ficha, ¿cuáles datos son sensibles?", ["El número de cédula y el lugar donde vive la persona identifican y exponen su seguridad.", "Los alimentos que no puede comer pueden revelar información de salud."], "Son sensibles: la cédula, el lugar donde vive y las restricciones de alimentos"),
        ("Minimizar un formulario", "El club de ajedrez solo necesita saber quién viene a la reunión y cómo avisarle. ¿Qué datos pide?", ["Para saber quién viene: el nombre y el curso.", "Para avisarle: un solo medio de contacto, como el correo."], "Nombre, curso y un medio de contacto"),
    ],
    mistakes=[("Pensar que si un dato no es secreto da lo mismo pedir de más.", "Cada dato guardado puede filtrarse o usarse con otro fin.", "Pide solo lo que necesita la finalidad."),
              ("Publicar una foto de otra persona sin preguntarle.", "No se respetó su consentimiento.", "Pregunta antes de publicar y respeta una negativa.")],
    T=[
        ('abc', '{F} ¿Cuál de estos datos permite contactar directamente a una persona?', 'El teléfono', 'El curso', 'El nombre del club', 'Un teléfono sirve para comunicarse con la persona.'),
        ('abc', '{F} ¿Cuál de estos datos de la ficha es el menos sensible?', 'El curso', 'El número de cédula', 'El lugar donde vive la persona', 'El curso es un dato general; la cédula y el domicilio exponen la identidad y la seguridad.'),
        ('ab', '¿Qué significa la minimización de datos?', 'Pedir y guardar solo los datos necesarios para la finalidad', 'Guardar todos los datos posibles por si acaso', 'Cada dato debe tener un motivo; lo que no se necesita no se pide.'),
        ('abc', '{F} El club necesita avisar la fecha de la once y adaptar la comida. ¿Qué datos son necesarios?', 'Nombre, un medio de contacto y la restricción de alimentos', 'Cédula, dirección y foto', 'Todos los datos del formulario', 'Para avisar y organizar la comida bastan esos tres; los demás no cumplen ninguna finalidad.'),
        ('abc', '{F} ¿Por qué merece cuidado el dato «lugar donde vive la persona»?', 'Permite ubicarla físicamente y puede poner en riesgo su seguridad', 'Porque es un dato muy largo', 'No merece cuidado', 'Un domicilio exacto es un dato sensible: quien lo conozca sabe dónde encontrar a la persona.'),
        ('abc', '¿Qué es la huella digital, entendida como rastro de datos?', 'El rastro de datos que dejas al usar servicios digitales', 'La marca del dedo para desbloquear un teléfono', 'Un virus que borra archivos', 'Cada publicación, búsqueda o registro deja información que puede quedar guardada.'),
        ('abc', 'Una persona publica una foto de una compañera sin preguntarle. ¿Qué principio no respetó?', 'El consentimiento', 'La minimización de datos', 'La seguridad de la contraseña', 'La compañera no aceptó que su imagen se publicara.'),
        ('abc', 'Una app de recetas pide acceso a tus contactos «para mejorar la experiencia». ¿Qué pregunta ayuda a decidir?', '¿Para qué necesita esos datos y funciona la receta sin ellos?', '¿Cuántos usuarios tiene la app?', '¿De qué color es el ícono?', 'Evaluar la finalidad y si hay alternativa sin el dato permite decidir con criterio.'),
        ('abc', '¿Cuál de estos datos se debe proteger más?', 'La contraseña de tu correo', 'El nombre de tu curso', 'Tu color favorito', 'Con la contraseña alguien podría entrar a tu cuenta y suplantarte.'),
        ('abc', '{F} Un compañero dice: «si el dato no es secreto, da lo mismo pedir de más». ¿Qué respuesta es correcta?', 'Cada dato guardado puede filtrarse o usarse mal; por eso se pide solo lo necesario', 'Tiene razón', 'Solo importa si es la cédula', 'Guardar más datos aumenta el daño posible si hay una filtración.'),
        ('abc', 'Alguien te pide la clave de tu cuenta «para ayudarte con el juego». ¿Qué corresponde?', 'No entregarla y contárselo a una persona adulta de confianza', 'Entregarla si es un amigo', 'Cambiarla y entregarla', 'Una clave es personal; si alguien la pide, se avisa a una persona adulta de confianza.'),
        ('abc', '{F} Se quiere reducir los riesgos del formulario del club. ¿Cuál cambio es mejor?', 'Eliminar la cédula y el lugar donde vive, mantener solo lo necesario y explicar para qué se usa cada dato', 'Agregar más preguntas', 'Pedir todo pero ocultarlo en pantalla', 'Menos datos y una finalidad clara reducen los riesgos desde el diseño.'),
        ('abc', 'Una persona sube a una red social el horario y el lugar donde entrena cada día una compañera de curso. ¿Cuál es el riesgo principal?', 'Revelar una rutina y ubicación que otras personas podrían usar para perjudicarla', 'Gastar datos del teléfono', 'Ninguno, porque es información pública', 'Publicar la rutina de alguien expone su seguridad sin que lo haya aceptado.'),
    ],
    ctx=('abc', 'En una feria escolar, un stand pide nombre, teléfono y correo para participar en el sorteo de un libro. ¿Qué mejora respeta mejor la minimización?', 'Pedir solo un medio de contacto, como el correo, y borrar los datos cuando termine el sorteo', 'Pedir también la dirección de la casa', 'Guardar los datos para siempre', 'Un solo medio de contacto cumple la finalidad y borrar al terminar evita riesgos posteriores.'),
    sc=[
        ("En tecnología digital: ¿qué es un dato personal?", "Un dato que permite identificar a una persona", "Nombre, correo, teléfono y foto son ejemplos."),
        ("En tecnología digital: ¿qué dos cosas debe tener claras una app antes de pedir un dato?", "Para qué lo usa (finalidad) y que la persona acepte (consentimiento)", "Sin finalidad y sin consentimiento no se debería pedir el dato."),
        ("¿A quién se avisa si alguien te pide datos privados y te incomoda?", "A una persona adulta de confianza", "Nunca se enfrenta a esa persona ni se guarda en secreto lo que ocurrió."),
    ],
    op=("Elige uno. Caso 1: el carné de una biblioteca escolar de ejemplo pide nombre, curso, número de cédula, teléfono, correo, dirección, foto y libros favoritos. Caso 2: una app de ejemplo para organizar un paseo de curso pide nombre, correo, teléfono, número de cédula, restricciones de alimentos y fotos de todos. "
        "Clasifica cada campo como «necesario», «opcional» o «eliminar», justifica en una frase y escribe dos oraciones de aviso de privacidad (para qué se usan los datos y cuándo se borran).",
        "Caso 1: necesarios: nombre, curso y un medio de contacto; opcional: libros favoritos (si se usa para recomendar); eliminar: cédula, dirección, foto. Aviso: «Usamos tus datos solo para prestar libros. Los borramos al terminar el año escolar».",
        ["clasifica todos los campos con una razón", "aplica la minimización", "redacta un aviso claro con finalidad y plazo"],
        ["hoja con la tabla de campos y el aviso de privacidad"],
        ["pedir datos sin finalidad", "no incluir el plazo de borrado", "olvidar el consentimiento para las fotos"],
        "Pregunta: «¿qué pasaría si este dato se filtrara?». Si el daño es alto y el dato no es necesario, debe eliminarse."),
    reinforce="Haz una lista de cinco datos que has entregado a apps este mes (sin escribir datos reales) y marca cuáles eran sensibles.",
    extend="Explica cómo cambiaría un formulario si cada dato tuviera que justificarse con una finalidad escrita.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (de ejemplo). Cifrado César con desplazamiento 3: cada letra se reemplaza por la que está 3 lugares más adelante en el alfabeto de 26 letras (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z, sin Ñ); después de Z se vuelve a A. Ejemplos: A pasa a D, B pasa a E, X pasa a A. "
     "Es un método antiguo y muy fácil de romper: sirve para entender la idea, no para proteger datos reales. "
     "Cantidad de contraseñas posibles con k posiciones y n símbolos posibles en cada una: n · n · … · n (k veces).")
build(
    O6, 2, F,
    use="Aprenderé a representar un mensaje en claro y cifrado, a calcular cuántas contraseñas son posibles y a decidir cómo proteger información privada.",
    prior=["Sé el orden del alfabeto.", "Sé multiplicar potencias de 10 y de 26 con calculadora.", "Sé qué es una contraseña."],
    explain=[
        "Cifrar es transformar un mensaje con una regla y una clave para que otras personas no lo entiendan; descifrar es volver al mensaje original. El mensaje original se llama texto claro y el transformado, texto cifrado. En el cifrado César se desplaza cada letra una cantidad fija: con desplazamiento 3, HOLA se cifra como KROD, y para descifrar se retrocede 3 letras.",
        "César es muy débil: solo hay 25 desplazamientos posibles y se prueban todos en pocos minutos, por eso no protege información real. Una contraseña, en cambio, es más fuerte mientras más combinaciones posibles tenga: con 4 dígitos hay 10 · 10 · 10 · 10 = 10.000; con 6 dígitos hay 1.000.000, cien veces más; con 4 letras minúsculas hay 26 · 26 · 26 · 26 = 456.976. La longitud y la variedad de símbolos aumentan las combinaciones.",
        "Un servicio responsable no guarda las contraseñas tal como se escriben: guarda una huella que no permite recuperarlas (un hash). Además limita los intentos fallidos, y las personas usuarias no reutilizan la misma contraseña en todos lados, porque si una web se filtra, quien la obtenga podría entrar a otras cuentas. Si sospechas que alguien conoce tu clave, la cambias y avisas a una persona adulta de confianza.",
    ],
    vocab=[("cifrar", "transformar un mensaje con una regla y una clave"), ("descifrar", "volver al mensaje original"), ("texto claro", "mensaje original sin cifrar"), ("texto cifrado", "mensaje transformado"), ("combinación", "una contraseña posible"), ("hash", "huella de una contraseña que no permite recuperarla")],
    worked=[
        ("Cifrar con César", "Cifra «LUZ» con desplazamiento 3.", ["L pasa a O, U pasa a X.", "Z da la vuelta: después de Z viene A, B y C, así que Z pasa a C."], "LUZ se cifra OXC"),
        ("Contar combinaciones", "Compara una clave de 4 dígitos con una de 6 dígitos.", ["4 dígitos: 10 · 10 · 10 · 10 = 10.000.", "6 dígitos: 1.000.000, que es 100 veces más."], "La de 6 dígitos tiene 100 veces más combinaciones"),
    ],
    mistakes=[("Descifrar avanzando letras en vez de retroceder.", "Para volver al mensaje original se hace la operación contraria.", "Si cifraste sumando 3, descifra restando 3."),
              ("Creer que el cifrado César protege datos reales.", "Con solo 25 desplazamientos posibles se prueba cada uno rápidamente.", "Usa servicios y métodos modernos, nunca uno inventado.")],
    T=[
        ('abc', '{F} ¿En qué letra se transforma la D?', 'G', 'A', 'C', 'D es la cuarta letra y 3 lugares más adelante está la G.'),
        ('abc', '{F} ¿En qué letra se transforma la Y?', 'B', 'A', 'C', 'Después de Y vienen Z, A y B: 3 lugares más adelante es la B.'),
        ('ab', '{F} ¿Cómo se llama el mensaje original, antes de cifrar?', 'Texto claro', 'Texto cifrado', 'El mensaje sin transformar es el texto claro.'),
        ('{F} Cifra la palabra «MAR» con desplazamiento 3.', 'PDU', 'M pasa a P, A pasa a D y R pasa a U.'),
        ('{F} Descifra «FDVD» retrocediendo 3 letras.', 'CASA', 'F retrocede a C, D a A, V a S y D a A.'),
        ('abc', '{F} Descifrar «SRU» retrocediendo 3 letras da:', 'POR', 'QPS', 'VUX', 'S retrocede a P, R a O y U a R; las otras opciones avanzan o retroceden mal.'),
        ('=', '{F} ¿Cuántas contraseñas distintas hay de 3 dígitos (10 símbolos en cada posición)?', '10*10*10', 'Cada una de las tres posiciones tiene 10 opciones.'),
        ('=', '{F} ¿Cuántas contraseñas distintas hay formadas por 2 letras minúsculas (26 símbolos) seguidas de 2 dígitos (10 símbolos)?', '26*26*10*10', 'Cada posición de letra tiene 26 opciones y cada posición de dígito tiene 10.'),
        ('abc', '{F} ¿Cuál tiene más combinaciones posibles?', 'Una clave de 8 dígitos', 'Una clave de 5 letras minúsculas', 'Una clave de 6 dígitos', '8 dígitos son 100.000.000 de combinaciones, contra 11.881.376 de 5 letras y 1.000.000 de 6 dígitos.'),
        ('abc', '{F} Un amigo dice: «mi mensaje está seguro porque lo cifré con César». ¿Qué corresponde responder?', 'No: con solo 25 desplazamientos posibles se prueba cada uno rápido; no protege datos reales', 'Sí, es imposible de descifrar', 'Sí, si lo envías de noche', 'César tiene muy pocas claves posibles, así que se rompe probándolas todas.'),
        ('abc', 'Una web guarda las contraseñas tal como las escriben las personas usuarias. ¿Qué riesgo hay?', 'Si alguien accede a los datos, lee todas las contraseñas; conviene guardar una huella (hash)', 'Ninguno, porque son privadas', 'Las contraseñas se olvidan', 'Guardar las claves en claro las expone completas ante una filtración.'),
        ('=', '{F} Se pasa de una contraseña de 4 dígitos (10.000 combinaciones) a una de 5 dígitos (100.000 combinaciones). ¿Cuántas veces más combinaciones hay?', '100000//10000', 'Se divide el número de combinaciones nuevas por las anteriores.'),
        ('abc', 'Un aviso dice: «para tu seguridad, usa la misma contraseña en todos tus servicios así no la olvidas». ¿Qué está mal?', 'Si una web se filtra, quien obtenga la clave podría entrar a todas tus cuentas', 'Nada, es un buen consejo', 'Solo es un problema con César', 'Reutilizar claves hace que un solo problema afecte muchas cuentas.'),
    ],
    ctx=('abc', 'Una app de ejemplo pide una clave de 4 dígitos para abrir un cuaderno privado; alguien podría probar las 10.000 combinaciones. ¿Qué medida es más eficaz para frenarlo?', 'Limitar los intentos fallidos y bloquear un tiempo después de varios errores', 'Reducir la clave a 3 dígitos', 'Guardar la clave en un archivo de texto sin protección', 'Limitar los intentos hace inútil probar todas las combinaciones una por una.'),
    sc=[
        ("En seguridad digital: ¿qué es cifrar?", "Transformar un mensaje con una regla y una clave para que otras personas no lo entiendan", "Solo quien conoce la regla y la clave puede volver al mensaje original."),
        ("En seguridad digital: ¿qué aumenta más las combinaciones de una contraseña?", "Su longitud y la variedad de símbolos", "Cada posición adicional o símbolo nuevo multiplica las opciones."),
        ("En un diseño responsable, ¿qué se guarda en lugar de la contraseña?", "Una huella (hash) de la contraseña", "La huella no permite recuperar la clave original."),
    ],
    op=("Cifra con César (desplazamiento 3) los mensajes «PAZ» y «LUNA», y descifra «DPLJR». Calcula cuántas contraseñas hay de 4 dígitos y de 3 letras minúsculas, y escribe dos reglas para crear una contraseña mejor y una razón para cada una. "
        "No uses contraseñas reales tuyas ni de otras personas.",
        "PAZ se cifra SDC; LUNA se cifra OXQD; DPLJR se descifra AMIGO. 4 dígitos: 10.000; 3 letras minúsculas: 26 · 26 · 26 = 17.576. Reglas: usar una clave larga (más combinaciones) y no repetirla en otros servicios (una filtración no afecta todo).",
        ["cifra y descifra sin errores", "calcula las combinaciones", "escribe dos reglas con una razón cada una"],
        ["hoja con los tres mensajes, los dos cálculos y las dos reglas"],
        ["retroceder al cifrar o avanzar al descifrar", "olvidar la vuelta de la Z", "usar una contraseña real"],
        "Pregunta: «¿qué regla usaste para la letra Z?». Si falla, repasa que después de Z se vuelve a A."),
    reinforce="Cifra una palabra que elijas con César (desplazamiento 3) y pide a una persona de tu casa que la descifre sin ver la regla.",
    extend="Explica por qué guardar una huella de la contraseña protege mejor que guardarla cifrada con una clave que también está en el programa.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (de ejemplo). Dos versiones de una función de registro de una app escolar. "
     "Versión 1: def registrar(nombre, clave, cedula): ↵ ··datos = {\"nombre\": nombre, \"clave\": clave, \"cedula\": cedula} ↵ ··guardar_en_archivo(datos) ↵ ··print(\"Registrado:\", datos). "
     "Versión 2: def registrar2(nombre, clave): ↵ ··huella = hacer_huella(clave) ↵ ··datos = {\"nombre\": nombre, \"huella\": huella} ↵ ··guardar_en_archivo(datos) ↵ ··print(\"Registrado:\", nombre). "
     "(hacer_huella calcula una huella que no permite recuperar la clave.)")
build(
    O6, 3, F,
    use="Aprenderé a diseñar y revisar programas que tratan información personal con responsabilidad: pedir lo mínimo, proteger lo que se guarda y actuar bien ante un problema.",
    prior=["Sé qué es un dato sensible y un hash.", "Sé leer una función breve.", "Sé qué es un diccionario en programación."],
    explain=[
        "Un programa responsable se diseña pensando en la privacidad desde el comienzo. Eso incluye cuatro ideas: pedir solo los datos necesarios, proteger lo que se guarda (por ejemplo, guardar una huella de la contraseña en vez de la contraseña), no mostrar datos sensibles en pantallas ni en registros de errores, y validar las entradas para que cumplan formato y límites razonables.",
        "En la ficha, la versión 1 guarda la clave en claro, pide un número de cédula que no hace falta para registrarse y lo imprime todo en pantalla. La versión 2 mejora tres cosas: guarda una huella, no pide la cédula e imprime solo el nombre. Aun así no es perfecta: falta proteger el archivo donde se guarda, pedir el consentimiento de las personas y borrar los datos cuando ya no se necesiten.",
        "Si ocurre un incidente, como que un archivo con nombres y correos se filtre, la respuesta responsable es avisar de inmediato a la persona adulta responsable (por ejemplo, un docente), cerrar el acceso al archivo, ayudar a informar a las personas afectadas y corregir el error. No se oculta ni se borra todo para que nadie lo note, y no se culpa a una persona sin saber qué pasó.",
    ],
    vocab=[("privacidad por diseño", "pensar en la protección de datos desde el diseño del programa"), ("huella (hash)", "valor que no permite recuperar la contraseña"), ("validar", "comprobar que un dato cumple el formato y los límites"), ("registro de errores", "archivo donde un programa anota lo que falla"), ("incidente", "problema que expone o daña datos"), ("acceso", "permiso para ver o cambiar un dato")],
    worked=[
        ("Revisar la versión 1", "¿Qué problemas de privacidad tiene registrar?", ["Guarda la clave en claro: quien lea el archivo la ve.", "Pide una cédula innecesaria e imprime todos los datos."], "Tres problemas: clave en claro, cédula innecesaria y datos impresos"),
        ("Responder a un incidente", "Se filtra un archivo con nombres y correos de compañeros. ¿Qué haces primero?", ["Avisas a la persona adulta responsable, por ejemplo tu docente.", "Se cierra el acceso al archivo y se informa a las personas afectadas."], "Avisar de inmediato a una persona adulta responsable y cerrar el acceso"),
    ],
    mistakes=[("Mostrar datos sensibles en la pantalla o en los registros de errores.", "Cualquier persona que vea la pantalla o el archivo puede leerlos.", "Registra solo lo necesario, como un número de caso, sin datos personales."),
              ("Ante una filtración, borrar todo y no decir nada.", "Las personas afectadas no pueden protegerse y el problema puede repetirse.", "Avisa a una persona adulta responsable y ayuda a informar.")],
    T=[
        ('abc', '{F} ¿Qué problema tiene registrar respecto de la clave?', 'La guarda tal cual, en texto claro', 'La borra', 'La cifra con César', 'Guardar la clave sin transformar la expone ante cualquier filtración.'),
        ('abc', '{F} ¿Cuántos datos guarda registrar2 dentro del diccionario datos?', '2', '3', '1', 'El diccionario de registrar2 tiene dos claves: nombre y huella; registrar guarda tres.'),
        ('ab', '{F} ¿Qué guarda registrar2 en lugar de la clave?', 'Una huella de la clave', 'La clave sin cambios', 'La huella no permite recuperar la clave, que es lo que se busca proteger.'),
        ('abc', '{F} ¿Qué muestra el print de registrar2?', 'Solo el nombre', 'Todos los datos', 'La clave', 'La versión 2 imprime únicamente el nombre y no expone datos sensibles.'),
        ('abc', '{F} En registrar2, ¿dónde queda la clave original después de calcular la huella?', 'En ningún dato guardado ni impreso: solo se usó para calcular la huella', 'En el diccionario datos', 'En el print', 'La clave solo entra a hacer_huella; datos y print contienen únicamente el nombre y la huella.'),
        ('abc', '¿Qué es validar una entrada?', 'Comprobar que el dato recibido cumple el formato y los límites esperados antes de usarlo', 'Borrarlo después de usarlo', 'Cifrarlo con César', 'La validación evita errores y datos absurdos antes de procesarlos.'),
        ('abc', 'Una función recibe la edad de una persona. ¿Qué validación es razonable?', 'Que sea un número entero entre 0 y 120', 'Que sea un texto', 'Ninguna', 'Una edad es un número entero con un rango razonable.'),
        ('abc', 'Al escribir un registro de errores (log), ¿cuál línea respeta la privacidad?', 'Error al registrar al usuario número 15', 'Error con la clave 1234 de Ana Pérez', 'Error con cédula y dirección de la persona', 'Un número de caso permite revisar el problema sin exponer datos personales.'),
        ('abc', '{F} ¿Qué cambio mínimo en registrar mejora más la privacidad?', 'Quitar la cédula del diccionario y guardar una huella de la clave', 'Cambiar el nombre de la función', 'Agregar más datos', 'Menos datos y una clave protegida reducen directamente los riesgos.'),
        ('abc', '{F} Una persona dice que registrar2 es perfecta. ¿Qué falta considerar?', 'Proteger el archivo, pedir consentimiento y borrar los datos cuando ya no se necesiten', 'Nada', 'Que use César', 'La función mejora, pero la privacidad también depende de dónde y por cuánto tiempo se guardan los datos.'),
        ('abc', 'Descubres que una app que ayudaste a hacer guarda por error las claves en un registro de errores que ve todo el curso. ¿Qué haces primero?', 'Avisar a la persona adulta responsable, cerrar el acceso al registro y corregir el programa', 'Esperar a ver si alguien lo nota', 'Borrar el registro sin decir nada', 'Informar y corregir protege a las personas afectadas y evita que el error se repita.'),
        ('abc', '{F} Una compañera propone guardar la clave con César 3 «para no guardarla en claro». ¿Qué evaluación es correcta?', 'César se revierte con facilidad; una huella unidireccional protege mucho mejor', 'César es suficiente', 'Es peor que guardarla en claro', 'César se deshace probando 25 desplazamientos, mientras que una huella no permite recuperar la clave.'),
        ('abc', 'Un taller de robótica terminó y su inscripción tiene nombres y correos de estudiantes. ¿Cuál decisión es más coherente con la minimización?', 'Borrar los datos cuando ya no se necesiten para su finalidad', 'Guardarlos para siempre', 'Enviar una copia a todos los teléfonos', 'Cuando termina la finalidad, mantener los datos solo agrega riesgo.'),
    ],
    ctx=('abc', 'Un curso programa una app de asistencia. La propuesta A guarda nombre, curso y asistencia; la propuesta B, además, guarda la ubicación GPS de cada estudiante cada minuto. ¿Cuál es más responsable para el fin «registrar asistencia»?', 'A, porque guarda solo lo necesario', 'B, porque más datos son mejores', 'Da lo mismo', 'La ubicación constante no sirve para tomar asistencia y expone la seguridad de las personas.'),
    sc=[
        ("En programación responsable: ¿qué se guarda en lugar de la contraseña?", "Una huella (hash)", "La huella no permite recuperar la contraseña."),
        ("En programación responsable: ¿qué debe evitarse escribir en pantallas y en registros de errores?", "Datos sensibles", "Cualquiera que vea esos lugares podría leerlos."),
        ("Si se detecta una filtración de datos, ¿a quién se avisa primero?", "A la persona adulta responsable, por ejemplo un docente", "Avisar permite cerrar el acceso e informar a las personas afectadas."),
    ],
    op=("Esta función de una app de talleres escolares de ejemplo tiene problemas: def inscribir(nombre, clave, direccion, telefono, foto_ruta): ↵ ··datos = {\"nombre\": nombre, \"clave\": clave, \"direccion\": direccion, \"telefono\": telefono, \"foto\": foto_ruta} ↵ ··guardar_en_archivo(datos) ↵ ··print(\"Datos guardados:\", datos). "
        "Anota cuatro problemas de privacidad y escribe una versión mejorada de cinco líneas o menos; luego explica qué harías si el archivo se filtrara.",
        "Problemas: clave en claro, dirección innecesaria, foto sin consentimiento, e impresión de todos los datos. Versión: def inscribir(nombre, clave, telefono): ↵ ··huella = hacer_huella(clave) ↵ ··guardar_en_archivo({\"nombre\": nombre, \"huella\": huella, \"telefono\": telefono}) ↵ ··print(\"Inscrito:\", nombre). Si el archivo se filtra: avisar a la persona adulta responsable, cerrar el acceso e informar a las personas afectadas.",
        ["identifica problemas reales de privacidad", "propone una versión con menos datos y protegida", "describe una respuesta responsable ante un incidente"],
        ["hoja con la lista de problemas, la función mejorada y el plan de respuesta"],
        ["dejar la clave en claro", "imprimir todos los datos", "no incluir avisar a una persona adulta responsable"],
        "Pregunta: «¿qué datos de la nueva versión se podrían eliminar y por qué?». Si no puede, repasa la finalidad."),
    reinforce="Elige una app que uses y anota qué permisos pide y cuáles crees que no necesita para su función.",
    extend="Explica por qué una buena práctica de privacidad incluye decidir cuánto tiempo se guardan los datos.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (de ejemplo). Cuatro casos. Caso 1: Sofía programa un juego y usa la imagen de una ilustradora sin pedirle permiso. "
     "Caso 2: Tomás usa un fragmento de código publicado con una licencia abierta que pide mencionar al autor, y lo menciona en su proyecto. "
     "Caso 3: Camila toma capturas de pantalla del chat de su curso y las publica en una red pública. "
     "Caso 4: Ian crea una app de recuerdo del curso con los nombres de sus compañeros, con su permiso, y borra los datos al terminar.")
build(
    O6, 4, F,
    use="Aprenderé a usar la tecnología de forma creativa, respetuosa y responsable: respetar la autoría, pedir consentimiento y proteger a las demás personas.",
    prior=["Sé qué es un dato personal.", "Sé que lo publicado puede copiarse.", "Sé qué es una licencia, en términos generales."],
    explain=[
        "Crear con tecnología incluye usar materiales de otras personas con respeto. Toda obra (imagen, música, código) tiene una persona autora. Para usarla se necesita su permiso o una licencia que lo permita. Una licencia abierta no significa «sin condiciones»: puede pedir mencionar a la persona autora (atribución) o limitar usos. Que algo sea visible en internet no significa que sea libre.",
        "El consentimiento también cuenta para las personas. Antes de publicar una foto, un video o un mensaje de otra persona se le pregunta y se respeta si dice que no. El contexto importa: un mensaje compartido en un chat de curso fue dicho para ese grupo; llevarlo a una red pública cambia quién lo ve y puede dañar. Si recibes contenido íntimo de otra persona, no lo reenvías ni lo guardas, no borras la conversación y avisas a una persona adulta de confianza.",
        "Ser creativo y responsable se puede combinar: se puede remezclar el trabajo de otra persona pidiéndole permiso y acordando cómo se la menciona. Si descubres que usaste algo sin permiso, lo correcto es retirarlo, contactar a la persona autora y reemplazarlo por algo con permiso. Y si un contenido daña a alguien, la respuesta es apoyar a la persona afectada y avisar a una persona adulta de confianza.",
    ],
    vocab=[("autoría", "pertenencia de una obra a la persona que la creó"), ("licencia", "permiso con condiciones para usar una obra"), ("atribución", "mencionar a la persona autora cuando la licencia lo pide"), ("consentimiento", "aceptación libre e informada de una persona"), ("remezcla", "crear algo nuevo a partir de obras existentes"), ("contexto", "lugar y grupo para el que se compartió algo")],
    worked=[
        ("Evaluar un caso", "¿Qué faltó en el caso 1 de la ficha?", ["Sofía usó una imagen que tiene autora.", "No tenía permiso ni una licencia que lo permitiera."], "Faltó el permiso de la autora o una licencia que permitiera usar la imagen"),
        ("Decidir antes de publicar", "Quieres subir una foto grupal de tu curso. ¿Qué haces primero?", ["Verificas quiénes salen en la foto.", "Les preguntas si están de acuerdo y respetas si alguien dice que no."], "Pedir el consentimiento de las personas que salen"),
    ],
    mistakes=[("Pensar que si algo está en internet puedes usarlo como quieras.", "Que sea visible no significa que tenga licencia libre.", "Revisa quién es la persona autora y qué condiciones tiene."),
              ("Llevar un mensaje de un chat privado a un lugar público.", "Cambia quién lo ve y puede dañar a las personas.", "Pide permiso antes de compartirlo fuera del grupo.")],
    T=[
        ('abc', '{F} ¿Qué debería hacer Sofía en el caso 1 para respetar la autoría?', 'Pedir permiso a la ilustradora o usar una imagen con licencia que lo permita', 'Escribir «imagen de internet» como fuente y seguir usándola', 'Cambiarle los colores para que parezca propia', 'Una fuente genérica o un cambio de colores no reemplazan el permiso o la licencia.'),
        ('abc', '{F} ¿Qué hizo bien Tomás en el caso 2?', 'Cumplir la condición de la licencia, mencionando al autor', 'Copiar sin decir nada', 'Ocultar el origen del código', 'La licencia pedía atribución y Tomás la dio.'),
        ('ab', '¿Qué es el consentimiento?', 'La aceptación libre e informada de una persona para que se use su imagen o sus datos', 'Un permiso que se supone sin preguntar', 'Consentir exige preguntar y que la persona pueda decir que no.'),
        ('abc', '{F} ¿Qué problema tiene el caso 3?', 'Publica mensajes privados de otras personas sin su permiso', 'Usa muchas capturas', 'Ninguno', 'El chat era de un grupo y sus integrantes no aceptaron que se hiciera público.'),
        ('abc', '{F} ¿Por qué el caso 4 respeta los datos de sus compañeros?', 'Pidió permiso, usó los datos para algo claro y los borró al terminar', 'Porque usó nombres', 'Porque es un recuerdo', 'Tiene consentimiento, finalidad clara y borrado, tres rasgos de un uso responsable.'),
        ('abc', 'Una licencia abierta, ¿significa que el material se puede usar sin condiciones?', 'No: cada licencia tiene condiciones, como mencionar a la persona autora', 'Sí, sin ninguna condición', 'Solo se usa con permiso escrito siempre', 'Abierto no es lo mismo que sin condiciones; hay que leer lo que la licencia pide.'),
        ('abc', 'Quieres usar una canción famosa en un video del curso que subirás a una red. ¿Qué opción respeta los derechos de autoría?', 'Usar música con una licencia que lo permita o creada por ti, cumpliendo lo que la licencia pida', 'Usarla igual porque es un video escolar', 'Cambiarle el nombre al archivo', 'Cambiar el nombre no quita la autoría; hace falta permiso o una licencia adecuada.'),
        ('abc', 'Un compañero te envía una foto íntima de otra persona. ¿Qué haces?', 'No la reenvías ni la guardas, no borras la conversación y avisas a una persona adulta de confianza', 'La reenvías a un amigo', 'La guardas por si acaso', 'Compartir esa imagen daña a la persona; avisar a una persona adulta de confianza es lo correcto.'),
        ('abc', 'Alguien hace un meme con la foto de un compañero, «solo como chiste del curso», sin preguntarle. ¿Qué principio falta?', 'Su consentimiento: puede sentirse humillado aunque quien lo hizo lo vea como broma', 'La atribución a la persona autora', 'La minimización de datos', 'Usar la imagen de alguien exige preguntar antes, y la persona puede decir que no.'),
        ('abc', '{F} Alguien dice: «si algo es público en internet, puedo usarlo como quiera». ¿Qué respuesta es correcta?', 'Que sea visible no significa que tenga licencia libre: hay que revisar la autoría y las condiciones', 'Tiene razón', 'Solo vale para imágenes', 'La visibilidad no entrega derechos de uso.'),
        ('abc', '{F} Camila dice que solo compartió «lo que yo vi». ¿Qué argumento explica el problema?', 'El chat era de un grupo; llevarlo a un espacio público cambia quién lo ve y puede dañar a las personas', 'Los chats no tienen ninguna privacidad', 'Es correcto si son pocas capturas', 'El contexto en que algo se comparte importa: el grupo no aceptó que fuera público.'),
        ('abc', 'Un proyecto combina un dibujo de una compañera con tu animación. ¿Cuál es el procedimiento más respetuoso?', 'Pedirle permiso, acordar cómo se la menciona y respetar si dice que no', 'Usarlo y avisarle después', 'Cambiarle los colores para que parezca tuyo', 'El permiso y la atribución respetan la autoría y la decisión de la compañera.'),
        ('abc', 'Un equipo publica una app y descubre que una imagen era de autoría ajena y se usó sin permiso. ¿Cuál es la mejor reacción?', 'Retirar la imagen, contactar a la autora y reemplazarla por una con permiso', 'Esperar que nadie lo note', 'Quitar el nombre de la autora', 'Corregir el error con la persona afectada es la forma responsable de reparar.'),
    ],
    ctx=('abc', 'En un taller de robótica escolar, el equipo graba un video para mostrar su proyecto. Aparecen tres compañeros: dos aceptan salir y uno no quiere. ¿Qué decisión es adecuada?', 'Editar o grabar de nuevo para que la persona que no quiere no aparezca', 'Dejar el video como está porque la mayoría aceptó', 'Publicarlo y avisarle después', 'El consentimiento es individual: la negativa de una persona se respeta aunque otros acepten.'),
    sc=[
        ("En tecnología digital: ¿qué es la atribución?", "Mencionar a la persona autora cuando la licencia lo pide", "Es una condición frecuente de las licencias abiertas."),
        ("En tecnología digital: ¿qué debe hacerse antes de publicar la imagen de otra persona?", "Pedir su consentimiento", "Se pregunta antes de publicar y se respeta una negativa."),
        ("¿A quién se recurre si alguien comparte contenido que daña a una persona?", "A una persona adulta de confianza", "Avisar a una persona adulta ayuda a detener el daño y apoyar a quien fue afectada."),
    ],
    op=("Elige una opción. Opción 1: escribe una mini política de cinco reglas para una app de tu curso, sobre: qué datos se piden, qué se hace con las fotos de personas, cómo se usa material de otras personas, qué se hace si hay una filtración y qué se hace si alguien comparte algo que daña a otra persona. "
        "Opción 2: analiza el caso de Camila de la ficha y escribe qué debería haber hecho, qué puede hacer ahora y a quién debe avisar. En ambas, usa solo casos de ejemplo y ningún dato real.",
        "Opción 1: (1) Pedimos solo nombre y un contacto. (2) Solo publicamos fotos de quienes aceptaron. (3) Mencionamos a las autoras y autores del material que usemos. (4) Si hay una filtración, avisamos a la persona adulta responsable. (5) Si alguien comparte algo que daña, apoyamos a la persona y avisamos a una persona adulta de confianza.",
        ["cubre las cinco situaciones pedidas", "cada regla es concreta y aplicable", "incluye avisar a una persona adulta de confianza cuando hay riesgo"],
        ["hoja con las cinco reglas numeradas o con el análisis del caso"],
        ["reglas vagas como «ser respetuoso»", "no considerar el consentimiento", "no incluir a quién avisar"],
        "Pregunta: «¿qué haría una persona de tu curso con esta regla en un caso concreto?». Si no se puede aplicar, pídele que la haga más específica."),
    reinforce="Escribe tres frases cortas que podrías decir si te piden usar tu foto en un proyecto y no quieres.",
    extend="Explica cómo cambiaría una app que ya publicaste si una persona retira su consentimiento.",
)
