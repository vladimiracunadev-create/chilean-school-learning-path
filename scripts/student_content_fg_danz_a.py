"""Danza 3.º y 4.º medio FG: OAC-01 (conciencia corporal y lenguaje de la danza), clases 1 a 4. Secuencias inventadas descritas por escrito; sin video real."""
from __future__ import annotations

from fg_danz_common import build

O1 = "FG-DANZ-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (exploración de ejemplo, inventada). Todo de pie, cada persona en su zona, sin contacto. "
     "Bloque A (8 tiempos): rotar los hombros, 4 veces hacia adelante y 4 veces hacia atrás, una rotación por tiempo. "
     "Bloque B (8 tiempos): pasar el peso del pie derecho al izquierdo y volver, un cambio por tiempo, mirando al frente. "
     "Bloque C (8 tiempos): subir los brazos despacio durante 4 tiempos y bajarlos durante 4 tiempos, respirando con calma.")
build(
    O1, 1, F,
    use="Aprenderé a explorar mi cuerpo con conciencia: reconocer articulaciones, apoyos, peso y eje, notar mis sensaciones al moverme y hacer un calentamiento y un enfriamiento seguros, respetando el rango de mi cuerpo.",
    prior=["Sé seguir un conteo de ocho tiempos.", "Sé trabajar en mi zona sin tocar a otras personas.", "Sé que cada cuerpo se mueve distinto."],
    explain=[
        "En danza el cuerpo es el instrumento de expresión. Una articulación es el lugar donde se unen dos huesos y permite doblar o girar una parte del cuerpo (hombro, codo, cadera, rodilla, tobillo). El apoyo es la parte del cuerpo que sostiene el peso en cada momento (los dos pies, un pie, un pie y una mano). El eje es una línea vertical imaginaria que pasa por la cabeza y la columna; cuando el cuerpo se equilibra, el peso se organiza alrededor de ese eje.",
        "Tener conciencia corporal es notar lo que ocurre mientras uno se mueve: dónde está mi peso, qué articulación se mueve, dónde siento esfuerzo y cómo respiro. Para explorar se usan preguntas simples y se anota lo observado (por ejemplo: el peso pasó al pie izquierdo y sentí presión en el talón). Cada cuerpo tiene su propio rango de movimiento, es decir, hasta dónde se mueve sin dolor; comparar el rango propio con el de otras personas o con una forma ideal no sirve para aprender.",
        "El calentamiento general prepara el cuerpo con movimientos suaves y progresivos de las articulaciones, de los pies a la cabeza o al revés, sin rebotes bruscos. El enfriamiento baja el ritmo con movimientos lentos, respiración calmada y estiramientos suaves que se sostienen sin dolor. Si aparece dolor, mareo o incomodidad, se detiene el ejercicio, se descansa y se avisa a una persona adulta. Nunca se fuerza el cuerpo ni el de otra persona.",
    ],
    vocab=[("articulación", "unión de dos huesos que permite doblar o girar"), ("apoyo", "parte del cuerpo que sostiene el peso"), ("peso", "cómo se reparte la carga del cuerpo sobre los apoyos"), ("eje", "línea vertical imaginaria por la cabeza y la columna"), ("rango de movimiento", "hasta dónde se mueve una articulación sin dolor"), ("calentamiento", "movimientos suaves que preparan el cuerpo"), ("enfriamiento", "movimientos lentos que bajan el ritmo al terminar")],
    worked=[
        ("Describir una sensación con precisión", "Después del bloque B anotas «me sentí raro». Reescríbelo para que otra persona entienda qué ocurrió.", ["Identifica el apoyo, el peso y la sensación: el peso pasó al pie izquierdo y sentí presión en el talón.", "Agrega la respiración si la notaste: respiré por la nariz sin apuro."], "El peso pasó al pie izquierdo, sentí presión en el talón y respiré con calma"),
        ("Decidir ante una molestia", "En el bloque A, una compañera siente un tirón en el hombro y quiere terminar los 8 tiempos igual. ¿Qué corresponde?", ["Detenerse en cuanto aparece el dolor, sin completar el conteo.", "Descansar y avisar a una persona adulta antes de decidir si vuelve a moverse."], "Detenerse, descansar y avisar a una persona adulta"),
    ],
    mistakes=[("Escribir «me sentí raro» o «me salió bien» como única observación.", "No dice qué apoyo, qué articulación ni qué sensación hubo.", "Anota dónde estaba el peso, qué articulación se movió y qué sensación hubo."),
              ("Estirar o girar hasta sentir dolor para igualar el rango de otra persona.", "El rango de cada cuerpo es distinto y el dolor es una señal de detenerse.", "Mueve hasta donde sea cómodo y avisa si aparece dolor o mareo.")],
    T=[
        ('abc', '¿Qué es un apoyo en danza?', 'La parte del cuerpo que sostiene el peso en ese momento', 'El lugar del espacio donde se ubica el público', 'Una pausa breve entre dos movimientos que sirve para tomar aire', 'El apoyo es lo que sostiene el peso, por ejemplo los pies; la pausa y la ubicación del público son otras cosas.'),
        ('abc', '{F} En el bloque B, ¿qué cambia en cada tiempo?', 'El apoyo donde está el peso', 'La altura de los brazos', 'La dirección de la mirada', 'En el bloque B el peso pasa de un pie al otro; los brazos cambian en el bloque C.'),
        ('abc', '¿Cuál es una articulación?', 'La rodilla, donde se unen huesos y se dobla la pierna', 'La pantorrilla, la parte carnosa de la pierna que se endurece al caminar', 'El muslo, parte alta de la pierna', 'Una articulación es una unión de huesos; la pantorrilla y el muslo son partes del cuerpo que no la son.'),
        ('=', '{F} El ciclo de los tres bloques se hace 2 veces seguidas y cada tiempo dura 2 segundos. ¿Cuántos segundos dura todo?', '3*8*2*2', 'Son 3 bloques de 8 tiempos, repetidos 2 veces, a 2 segundos cada tiempo.', ' segundos'),
        ('abc', '¿Qué describe mejor la conciencia corporal?', 'Notar apoyos, peso, esfuerzo y respiración mientras me muevo', 'Hacer cada movimiento lo más grande posible para que se note que uno se está esforzando', 'Copiar con exactitud la forma de otra persona', 'La conciencia corporal consiste en percibir lo que ocurre en el propio cuerpo mientras se mueve.'),
        ('abc', '¿Qué se entiende por eje del cuerpo?', 'Una línea vertical imaginaria que pasa por la cabeza y la columna', 'La línea del suelo que marca la zona de cada persona', 'El brazo que se usa con más fuerza', 'El eje es una referencia vertical del propio cuerpo, no una línea del suelo ni un brazo.'),
        ('abc', '{F} Durante el bloque C una persona siente mareo. ¿Qué hace?', 'Se detiene, se sienta y avisa a una persona adulta', 'Sigue hasta completar los 8 tiempos para no perder el ritmo del grupo', 'Sigue pero más lento y sin decir nada', 'Ante un mareo se detiene el ejercicio y se avisa; seguir, aunque sea más lento, puede empeorar la situación.'),
        ('abc', '{F} Un compañero sube los brazos en el bloque C menos que tú. ¿Qué es lo más adecuado?', 'Aceptar que cada cuerpo tiene su propio rango y seguir con el tuyo', 'Pedirle que suba más los brazos hasta igualar la altura que tú alcanzas', 'Mostrarle cómo se mueve el brazo tomándolo del codo', 'El rango es personal; corregirlo o tocarlo sin permiso falta el respeto al cuerpo ajeno.'),
        ('abc', 'Quieres explorar si hacer el movimiento más lento cambia lo que sientes en los apoyos. ¿Qué cambias en la prueba?', 'Solo qué tan lento lo haces, manteniendo todo lo demás igual', 'La rapidez, la altura de los brazos y la dirección de la mirada a la vez', 'Nada, y solo repites el mismo movimiento más veces', 'Cambiar una sola variable permite atribuirle a ella lo que sientes; si cambian varias no se sabe cuál influyó.'),
        ('abc', '¿Cuál es una observación bien hecha de la exploración?', 'En el bloque B mi peso pasó al pie izquierdo y sentí presión en el talón', 'Salió muy bien, me sentí genial y creo que se vio mejor que el de las demás personas', 'Fue lindo y quedó perfecto porque yo soy bueno para este tipo de cosas', 'La primera dice apoyo, peso y sensación; las otras son opiniones que otra persona no puede comprobar.'),
        ('abc', 'Para cerrar la sesión de la ficha con un enfriamiento, ¿cuál secuencia es segura y general?', 'Movimientos lentos de brazos, respiración calmada y estiramientos suaves sin dolor', 'Estiramientos con rebotes fuertes hasta sentir el tirón, porque así el músculo se suelta más rápido', 'Una carrera rápida por la sala para bajar el pulso', 'El enfriamiento baja el ritmo de forma gradual; los rebotes fuertes y la carrera no lo hacen.'),
        ('=', 'Un enfriamiento tiene 4 movimientos lentos de 8 tiempos, a 2 segundos por tiempo, y luego 30 segundos de respiración en calma. ¿Cuántos segundos dura?', '4*8*2+30', 'Se calculan los segundos de los movimientos y se suman los de la respiración.', ' segundos'),
        ('abc', 'Una compañera dice: «Mi hombro llega menos arriba que en el afiche del colegio, así que lo hago mal». ¿Qué corresponde responder?', 'Que el afiche no es una medida y que lo importante es moverse sin dolor y con conciencia', 'Que debe practicar más fuerte cada día hasta llegar a la misma altura que muestra el afiche', 'Que mejor deje el ejercicio y mire a las demás', 'Una forma ideal no es meta: se trabaja con el rango propio, sin dolor y sin compararse.'),
    ],
    ctx=('abc', 'Una estudiante repite el bloque B y anota: «peso al pie derecho, el tobillo se sintió inestable, respiré rápido». ¿Qué decisión de exploración es coherente?', 'Repetirlo más lento y con una mano apoyada en una silla si hace falta, observando el tobillo', 'Repetirlo más rápido y varias veces seguidas para que el tobillo se acostumbre a la inestabilidad', 'Eliminar el bloque B porque «no sirve para ella»', 'Bajar la velocidad y dar apoyo extra ayuda a notar el tobillo con seguridad; apurar o descartar no responde a lo observado.'),
    sc=[
        ("En Danza: ¿qué es un apoyo?", "La parte del cuerpo que sostiene el peso", "El apoyo dice dónde está cargado el peso del cuerpo."),
        ("¿Qué se hace ante dolor o mareo durante un ejercicio?", "Detenerse y avisar a una persona adulta", "La seguridad va antes que terminar el conteo."),
        ("¿Qué se anota de una exploración para que otra persona la entienda?", "El apoyo, la articulación que se movió y la sensación observada", "Eso permite comparar pruebas con datos y no solo con opiniones."),
    ],
    op=("Elige un movimiento sencillo de pie (por ejemplo, subir y bajar un brazo en 8 tiempos). Hazlo dos veces, sin forzar. Escribe, por cada vez: qué articulación se movió, dónde estuvo tu peso y una sensación. Después escribe qué cambiarías, solo una variable, en la tercera.",
        "Movimiento: subir el brazo derecho en 4 tiempos y bajarlo en 4. Vez 1: se movió el hombro, el peso estuvo repartido en los dos pies, sentí leve esfuerzo en el hombro. Vez 2: igual, pero respirando al subir. Cambiaría solo qué tan lento lo hago.",
        ["nombra una articulación y un apoyo", "separa lo observado de la opinión", "propone un solo cambio y sin dolor"],
        ["hoja con dos registros y un cambio propuesto"],
        ["escribir solo «me sentí bien»", "cambiar varias cosas a la vez", "forzar el rango para igualar a otra persona"],
        "Pregunta: «¿en qué apoyo estuvo tu peso?». Si responde con una opinión, pídele que nombre la parte del cuerpo."),
    reinforce="Haz en tu casa, con espacio despejado, el bloque C de la ficha tres veces y anota cómo cambia tu respiración. Detente si sientes dolor o mareo.",
    extend="Explica por qué comparar tu rango con el de otra persona no ayuda a explorar y qué harías en su lugar.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (tarjetas de ejemplo, inventadas). Movimiento base: «ola de brazo» (un brazo sube y baja como una ola). "
     "Tarjeta de espacio: nivel medio, dirección hacia adelante, trayectoria recta de 4 pasos. "
     "Tarjeta de tiempo: frase de 8 tiempos, velocidad lenta (un movimiento cada 2 tiempos). "
     "Tarjeta de energía: suave y continua (sin golpes ni cortes).")
build(
    O1, 2, F,
    use="Aprenderé a combinar los elementos espacio, tiempo y energía en un mismo movimiento y a cambiar uno de ellos a la vez para ver qué efecto produce.",
    prior=["Reconozco apoyos, eje y articulaciones.", "Sé contar ocho tiempos.", "Sé observar y describir un movimiento sin juzgarlo."],
    explain=[
        "El lenguaje de la danza se organiza en elementos. El espacio incluye el nivel (alto, medio o bajo), la dirección (adelante, atrás, a los lados, en diagonal) y la trayectoria, que es el camino que sigue el cuerpo por el suelo. El tiempo incluye el pulso (la pulsación regular de base), la velocidad (rápido o lento), la duración y la pausa. La energía es la calidad del esfuerzo: fuerte o suave, continua o cortada.",
        "Un mismo movimiento cambia de sentido según cómo se combinen esos elementos. Una ola de brazo lenta, suave y continua se percibe tranquila; la misma ola rápida, fuerte y cortada se percibe tensa o enérgica. Para comprobarlo se cambia un solo elemento por prueba, se cuenta con claridad (1 a 8, dos veces) y se anota qué efecto se percibe.",
        "En una frase de 8 tiempos con un movimiento cada 2 tiempos caben 4 movimientos; si la velocidad se duplica, caben 8. Para practicar con seguridad se usa un espacio despejado, cada persona en su zona, sin saltos ni contacto, y se detiene el ejercicio ante dolor o mareo.",
    ],
    vocab=[("nivel", "altura del cuerpo: alto, medio o bajo"), ("dirección", "hacia dónde se orienta o avanza el movimiento"), ("trayectoria", "camino que sigue el cuerpo en el espacio"), ("pulso", "pulsación regular que marca los tiempos"), ("velocidad", "qué tan rápido o lento ocurre el movimiento"), ("energía", "calidad del esfuerzo: fuerte o suave, continua o cortada")],
    worked=[
        ("Clasificar la información de una tarjeta", "La tarjeta dice «nivel bajo, hacia atrás, trayectoria curva». ¿A qué elemento pertenece y qué detalle da?", ["Nivel, dirección y trayectoria son datos del espacio.", "Nivel bajo: cuerpo cerca del suelo; hacia atrás: dirección; curva: forma del camino."], "Pertenece al espacio: nivel bajo, dirección atrás y trayectoria curva"),
        ("Calcular movimientos en una frase", "Una frase de 8 tiempos lleva un movimiento cada 2 tiempos y se repite 3 veces. ¿Cuántos movimientos se hacen?", ["En 8 tiempos caben 8 ÷ 2 = 4 movimientos.", "Con 3 repeticiones son 4 × 3 = 12 movimientos."], "12 movimientos"),
    ],
    mistakes=[("Confundir velocidad con energía y decir «fuerte» para un movimiento rápido.", "Un movimiento puede ser rápido y suave, o lento y fuerte: son elementos distintos.", "Pregunta por separado qué tan rápido es (tiempo) y cómo es el esfuerzo (energía)."),
              ("Cambiar nivel, velocidad y energía a la vez y concluir qué produjo el efecto.", "Con varios cambios juntos no se sabe qué lo causó.", "Cambia un elemento por prueba y compara.")],
    T=[
        ('abc', '{F} ¿Qué elemento indica la tarjeta «hacia adelante, 4 pasos»?', 'Espacio, porque da dirección y trayectoria', 'Tiempo, porque cuenta pasos', 'Energía, porque habla de esfuerzo', 'Dirección y trayectoria son datos del espacio; contar pasos no la convierte en una tarjeta de tiempo.'),
        ('abc', '¿Qué es la trayectoria?', 'El camino que sigue el cuerpo por el espacio', 'La rapidez con que se hace un movimiento', 'La fuerza que se usa en un gesto', 'La trayectoria es el recorrido; la rapidez es tiempo y la fuerza es energía.'),
        ('abc', '¿Cuál es un ejemplo de energía cortada?', 'Un brazo que sube en tres detenciones marcadas', 'Un brazo que sube de forma pareja y sin detenerse', 'Un brazo que sube en 8 tiempos lentos', 'Cortada es una energía con detenciones o golpes; pareja y continua es lo contrario.'),
        ('abc', '{F} ¿Cuál cambio modifica solo el tiempo de la ficha?', 'Hacer la ola de brazo un movimiento por tiempo', 'Hacerla en nivel bajo, con las rodillas flexionadas y el cuerpo más cerca del suelo', 'Hacerla fuerte y con golpes', 'Pasar a un movimiento por tiempo cambia la velocidad, que es un asunto del tiempo; los otros cambian espacio y energía.'),
        ('abc', 'Dos personas hacen el mismo gesto: una lo hace lento y suave, la otra rápido y fuerte. ¿Qué es lo más probable?', 'Se percibirán con distinto carácter aunque el gesto sea el mismo', 'Se percibirán igual, porque el gesto es el mismo', 'Se percibirá mejor el rápido porque es más claro', 'El tiempo y la energía cambian la manera en que se percibe un gesto igual.'),
        ('abc', 'El pulso es', 'la pulsación regular que sirve de base para contar los tiempos', 'la zona del suelo que se le asigna a cada estudiante para ensayar en la sala', 'la fuerza máxima de un movimiento', 'El pulso es la base regular de la cuenta; no es una zona ni una fuerza.'),
        ('=', '{F} La frase se repite 3 veces. ¿Cuántos movimientos de ola de brazo se hacen en total?', '8//2*3', 'En 8 tiempos hay un movimiento cada 2 tiempos y eso se multiplica por las repeticiones.'),
        ('abc', '{F} Quieres probar el efecto de la energía sin tocar el espacio ni el tiempo. ¿Qué haces?', 'Mantienes nivel medio, adelante y un movimiento cada 2 tiempos, y cambias suave por fuerte', 'Cambias suave por fuerte y además haces la frase en nivel bajo y al doble de velocidad', 'Haces la frase al doble de velocidad con la misma energía', 'Para aislar la energía se deja igual todo lo demás y se cambia solo esa variable.'),
        ('abc', 'Una frase de 8 tiempos tiene 4 movimientos de 2 tiempos. ¿Cómo se cuenta con claridad?', 'Mover en 1-3-5-7 y mantener la posición en 2-4-6-8', 'Mover en los tiempos 1-2-3-4 y quedarse quieto en 5-6-7-8', 'Mover en el tiempo 1 y mantener la posición hasta el 8', 'Un movimiento cada 2 tiempos cae en los tiempos impares y se mantiene en los pares.'),
        ('abc', 'Una compañera dice que un movimiento «es fuerte porque es rápido». ¿Qué corriges?', 'Que rapidez es tiempo y fuerza es energía; un movimiento puede ser rápido y suave', 'Nada, porque un movimiento rápido siempre se hace con fuerza', 'Que ambos pertenecen al espacio', 'Tiempo y energía son elementos distintos, aunque a veces aparezcan juntos.'),
        ('abc', 'Para dar la idea de «calma que se va apagando» con la ola de brazo, ¿qué combinación elegirías?', 'Velocidad cada vez más lenta, energía suave y nivel que baja de medio a bajo', 'Velocidad cada vez más rápida, energía fuerte y nivel alto', 'Velocidad igual, energía cortada y nivel alto', 'Lento, suave y descendente se asocian con apagarse; las otras combinaciones sugieren aumento o tensión.'),
        ('=', 'Una frase de 8 tiempos con un movimiento cada tiempo se repite 5 veces. ¿Cuántos movimientos más hace que si fuera uno cada 2 tiempos?', '8*5-8//2*5', 'Se restan los movimientos de la versión lenta a los de la versión rápida.'),
        ('abc', 'Una estudiante propone probar tres frases: lenta-suave, rápida-suave y lenta-fuerte, y anotar el efecto de cada una. ¿Qué tiene de bueno la propuesta?', 'Compara de a una variable, porque en cada par cambia un solo elemento', 'Cambia todo en cada frase, así se ven más diferencias', 'No sirve, porque las tres frases son parecidas', 'Lenta-suave frente a rápida-suave cambia el tiempo, y frente a lenta-fuerte cambia la energía: comparaciones limpias.'),
    ],
    ctx=('abc', 'Para mostrar «tensión que sube» con la ola de brazo en 8 tiempos, un grupo decide aumentar la velocidad cada repetición y pasar de energía suave a cortada. ¿Qué decisión es coherente con la idea?', 'Hacer cada repetición con más velocidad y esfuerzo marcado, sin forzar el cuerpo ni saltar', 'Hacer todas las repeticiones exactamente iguales para que la idea se note mejor al repetirse', 'Bajar el nivel y la velocidad en cada repetición', 'Aumentar velocidad y marcación gradualmente refleja una tensión que crece; mantener o desacelerar no.'),
    sc=[
        ("En Danza: ¿qué es la trayectoria?", "El camino que sigue el cuerpo por el espacio", "La trayectoria es el recorrido en el espacio."),
        ("¿Qué elemento de la danza describe «suave y continua»?", "La energía", "Suave o fuerte, continua o cortada es la calidad del esfuerzo."),
        ("Si un movimiento cabe cada 2 tiempos en 8 tiempos, ¿cuántos movimientos hay?", "4", "8 dividido en 2 da 4 movimientos."),
    ],
    op=("Elige un movimiento sencillo y seguro (por ejemplo, un paso al lado y un brazo que sube). Escribe tres versiones de 8 tiempos que cambien solo un elemento cada una: una de espacio, una de tiempo y una de energía. Anota el efecto que percibes en cada una.",
        "Movimiento: paso al lado con brazo arriba. Versión de espacio: nivel bajo (efecto: se ve más contenido). Versión de tiempo: un paso por tiempo (efecto: más apurado). Versión de energía: golpeada (efecto: más tenso).",
        ["cambia un elemento por versión", "nombra el elemento en cada caso", "describe un efecto percibido"],
        ["hoja con tres versiones y su efecto"],
        ["mezclar velocidad con energía", "no decir qué elemento cambió"],
        "Pregunta: «¿qué elemento cambiaste aquí?». Si nombra dos, pídele que haga una versión con uno solo."),
    reinforce="Elige un gesto cotidiano seguro (como saludar) y practícalo en tres velocidades distintas, contando 8 tiempos. Anota cómo cambia lo que transmite.",
    extend="Explica con un ejemplo inventado por qué dos movimientos iguales pueden transmitir cosas distintas si cambian el tiempo y la energía.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (frase de ejemplo, inventada, de 4 conteos de 8 tiempos). "
     "Conteo 1 (tiempos 1 a 8): caminar 4 pasos adelante en nivel medio y subir los brazos durante los otros 4 tiempos. "
     "Conteo 2: repetir exactamente el conteo 1. "
     "Conteo 3: las mismas acciones, pero doblando las rodillas para pasar a nivel bajo. "
     "Conteo 4: 4 tiempos de pausa quieta y 4 tiempos para bajar los brazos y respirar.")
build(
    O1, 3, F,
    use="Aprenderé a componer una frase de danza propia: elegir un motivo, repetirlo, variarlo, contrastarlo y cerrarlo con una pausa, y a justificar mis decisiones con los elementos del lenguaje de la danza.",
    prior=["Reconozco espacio, tiempo y energía.", "Sé contar conteos de 8 tiempos.", "Sé cambiar una variable por vez."],
    explain=[
        "Una frase de danza es una secuencia de movimientos con principio y final, como una oración. Se compone a partir de un motivo, que es una pequeña idea de movimiento (por ejemplo, caminar adelante y subir los brazos). Con ese motivo se usan recursos de composición: la repetición (hacerlo igual), la variación (hacerlo parecido pero cambiando un elemento, como el nivel) y el contraste (hacer algo muy distinto, como una pausa quieta después de movimiento).",
        "Las frases se organizan en conteos de 8 tiempos. Una frase de 4 conteos dura 4 × 8 = 32 tiempos. Un buen cierre es una pausa o una posición final clara, para que la frase no parezca cortada. Componer implica decidir y probar: se crea una versión, se ensaya, se anota qué elemento se cambió y se decide si se conserva o se revisa.",
        "En la práctica de composición se trabaja con espacio despejado y sin contacto. Los niveles bajos se logran con flexión suave de rodillas; no se usan caídas, saltos acrobáticos ni cargas. Cada autora o autor decide cuánto mostrar y puede ensayar en privado; nadie debe ser forzado a exponerse.",
    ],
    vocab=[("frase", "secuencia de movimientos con principio y final"), ("motivo", "pequeña idea de movimiento que se desarrolla"), ("repetición", "hacer el motivo igual otra vez"), ("variación", "hacer el motivo cambiando un elemento"), ("contraste", "introducir algo muy distinto a lo anterior"), ("conteo", "grupo de 8 tiempos que organiza la frase")],
    worked=[
        ("Reconocer repetición y variación", "En la ficha, ¿qué conteo es repetición y cuál variación del conteo 1?", ["El conteo 2 es igual al 1: repetición.", "El conteo 3 mantiene las acciones pero cambia el nivel: variación."], "Conteo 2: repetición; conteo 3: variación de nivel"),
        ("Calcular la duración", "La frase de la ficha se hace a 2 segundos por tiempo. ¿Cuánto dura?", ["Tiene 4 conteos de 8 tiempos: 4 × 8 = 32 tiempos.", "A 2 segundos cada uno: 32 × 2 = 64 segundos."], "64 segundos"),
    ],
    mistakes=[("Poner el motivo igual cuatro veces y llamarlo «frase con variación».", "Sin cambio de ningún elemento solo hay repetición.", "Cambia un elemento, como nivel, dirección o energía, en alguno de los conteos."),
              ("Terminar la frase en pleno movimiento sin cierre.", "El público no percibe un final y la frase parece cortada.", "Termina con una pausa o con una posición final clara.")],
    T=[
        ('abc', '¿Qué es un motivo en una frase de danza?', 'Una pequeña idea de movimiento que se repite y se desarrolla', 'El título que se escribe en el programa para que el público reconozca la obra', 'La música que acompaña la frase', 'El motivo es el material de movimiento de la frase; el título y la música son otros elementos.'),
        ('abc', '{F} ¿Qué conteo es una repetición del conteo 1?', 'El conteo 2', 'El conteo 3', 'El conteo 4', 'El conteo 2 es igual al 1; el 3 cambia de nivel y el 4 cierra con pausa.'),
        ('abc', '{F} ¿Qué elemento cambia en el conteo 3 respecto del conteo 1?', 'El nivel, que pasa de medio a bajo', 'La dirección, que pasa de adelante a atrás', 'La energía, que pasa de suave a fuerte', 'En la ficha el conteo 3 flexiona las rodillas, así que cambia el nivel y no se dice nada de energía.'),
        ('=', '{F} Cada tiempo dura 2 segundos. ¿Cuántos segundos dura toda la frase?', '4*8*2', 'Son 4 conteos de 8 tiempos, cada uno de 2 segundos.', ' segundos'),
        ('abc', '¿Cuál es un contraste dentro de una frase?', 'Una pausa quieta después de varios movimientos continuos', 'Repetir el último movimiento sin cambios, pero un poco más rápido', 'Hacer el motivo un poco más grande', 'El contraste introduce algo muy distinto; repetir o agrandar es repetición o variación.'),
        ('abc', 'Una variación se diferencia de una repetición porque', 'cambia al menos un elemento, como nivel, dirección o energía', 'dura más tiempo que la repetición, porque se hace con más energía y más movimientos', 'se hace con más personas', 'La variación conserva la idea pero modifica un elemento; la duración y el número de personas no la definen.'),
        ('abc', '{F} El conteo 4 tiene 4 tiempos de pausa y 4 de bajar brazos. ¿Qué función cumple?', 'Cerrar la frase con claridad', 'Repetir el motivo por última vez', 'Aumentar la velocidad del final', 'Una pausa y un cierre suave dan sensación de final.'),
        ('abc', '{F} Quieres cambiar la frase para que el conteo 2 sea variación y no repetición. ¿Cuál cambio sirve?', 'Hacer los 4 pasos hacia un lado en vez de hacia adelante', 'Hacer exactamente los mismos pasos con el mismo nivel y la misma velocidad', 'Contar los mismos pasos en voz más baja', 'Cambiar la dirección modifica un elemento; contar más bajo no cambia el movimiento.'),
        ('=', 'Otra frase tiene 6 conteos de 8 tiempos. Los dos últimos son pausa y cierre. ¿Cuántos tiempos tienen movimiento?', '(6-2)*8', 'Se restan los 2 conteos finales y se multiplica por 8 tiempos cada uno.', ' tiempos'),
        ('abc', 'Dos estudiantes componen con el mismo motivo. Una lo repite 4 veces; el otro lo repite, lo varía en nivel y cierra con pausa. ¿Qué frase muestra más recursos de composición?', 'La del segundo, porque combina repetición, variación y cierre', 'La de la primera, porque es más fácil de recordar', 'Ambas muestran lo mismo, porque usan un solo motivo', 'El segundo usa varios recursos; la primera usa solo repetición.'),
        ('abc', 'Para componer un nivel bajo seguro, ¿qué se recomienda?', 'Flexionar las rodillas con suavidad y mantener el apoyo estable en el suelo', 'Dejarse caer al suelo de golpe para que se note el cambio de nivel', 'Apoyarse en otra persona para bajar más rápido', 'Un nivel bajo seguro se logra con flexión controlada, sin caídas ni contacto.'),
        ('abc', 'Una estudiante prefiere ensayar su frase sola antes de mostrarla. ¿Qué corresponde?', 'Respetar su decisión y ofrecerle ensayo en privado', 'Pedirle que la muestre ahora para evaluarla', 'Obligarla a mostrarla porque todas pasaron', 'Mostrar es una decisión de la autora; se puede evaluar el proceso con otras evidencias.'),
        ('abc', 'Una frase de 3 conteos parece incompleta. ¿Qué cambio la mejora más?', 'Agregar un cuarto conteo con pausa y cierre claros', 'Quitar el primer conteo para que sea más corta', 'Repetir todo el tercer conteo sin cambios hasta el final', 'Un cierre claro da sensación de final; repetir sin cambios no resuelve que la frase termine cortada.'),
    ],
    ctx=('abc', 'Un grupo tiene un motivo de 8 tiempos: «un paso al lado y un brazo que se abre». Quiere una frase de 4 conteos con repetición, variación y cierre. ¿Qué plan cumple?', 'Conteo 1 motivo, 2 repetido, 3 con otro nivel, 4 con pausa y cierre', 'Conteo 1 al 4 el motivo exactamente igual', 'Conteo 1 motivo, 2 y 3 distintos entre sí, 4 sin pausa', 'El primer plan usa repetición (2), variación (3) y cierre (4), los tres recursos pedidos.'),
    sc=[
        ("En Danza: ¿qué es una variación?", "Hacer el motivo cambiando un elemento", "La variación conserva la idea pero modifica algo."),
        ("Una frase de 4 conteos de 8 tiempos, ¿cuántos tiempos tiene?", "32", "Cada conteo tiene 8 tiempos y son 4 conteos: 4 por 8 da 32."),
        ("¿Por qué conviene cerrar una frase con una pausa o posición final?", "Para que se perciba un final claro", "Sin cierre la frase parece cortada."),
    ],
    op=("Compón una frase de 4 conteos de 8 tiempos con un motivo seguro y sencillo. Escribe qué hace cada conteo e indica cuál es repetición, cuál variación y cuál cierre. Anota cuánto dura si cada tiempo dura 2 segundos.",
        "Motivo: paso al lado y brazo que se abre. Conteo 1: motivo. Conteo 2: repetición. Conteo 3: variación, en nivel bajo con rodillas flexionadas. Conteo 4: pausa 4 tiempos y cierre. Duración: 32 tiempos × 2 = 64 segundos.",
        ["indica motivo, repetición, variación y cierre", "cada conteo describe espacio, tiempo o energía", "calcula la duración correctamente"],
        ["hoja con los 4 conteos descritos"],
        ["llamar variación a una repetición", "no incluir cierre", "proponer movimientos con riesgo"],
        "Pregunta: «¿qué elemento cambia en tu variación?». Si no nombra uno, pídele que lo indique."),
    reinforce="Escribe con tus palabras los 4 conteos de una frase propia, con motivo, repetición, variación y cierre, y cuenta cuántos tiempos dura.",
    extend="Explica cómo cambiaría el sentido de tu frase si el conteo 4 fuera movimiento continuo en vez de pausa.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (frase de ejemplo «La espera», inventada). Propósito: transmitir una espera cansada. "
     "Acciones: caminar lento hacia adelante 4 pasos, detenerse, mirar hacia arriba, dejar caer los brazos con suavidad. "
     "Contexto A: presentación frente al curso, en el patio de la escuela, durante el recreo largo. "
     "Contexto B: presentación en una sala pequeña, con público a dos metros.")
build(
    O1, 4, F,
    use="Aprenderé a interpretar un propósito en la danza: decidir qué se quiere comunicar con una frase y ajustar el espacio, el tiempo y la energía al contexto en que se presenta, respetando el cuerpo propio y el de los demás.",
    prior=["Sé componer una frase con repetición, variación y cierre.", "Reconozco espacio, tiempo y energía.", "Sé describir sin juzgar los cuerpos."],
    explain=[
        "El propósito expresivo es lo que quiero comunicar con una frase: una emoción, una idea, una imagen. Interpretar es hacer la frase con esa intención, es decir, que la dirección, el nivel, la velocidad y la energía no sean casuales sino elegidos para mostrar el propósito. La misma frase puede significar cosas distintas con distinta intención: «caminar y detenerse» puede verse como espera, como duda o como cansancio.",
        "El contexto es el conjunto de condiciones de la presentación: el lugar, el tamaño del espacio, quién mira, cuánto tiempo hay y qué medios se usan. Un contexto grande y abierto permite trayectorias largas y movimientos amplios; uno pequeño exige acortar trayectorias y cuidar la distancia con el público. Interpretar bien también es adaptar la frase al contexto sin perder el propósito.",
        "Para interpretar con seguridad se cuida el espacio propio, se evita el contacto y se respeta el ritmo de cada persona. Las pausas y la mirada sirven para comunicar sin necesidad de movimientos extremos. Si alguien prefiere no presentar frente a todo el curso, se busca una alternativa, como presentar en grupo pequeño.",
    ],
    vocab=[("propósito expresivo", "idea, emoción o imagen que se quiere comunicar"), ("interpretar", "realizar la frase con una intención elegida"), ("contexto", "lugar, público, tiempo y medios de la presentación"), ("intención", "sentido que se le da a un movimiento al hacerlo"), ("adaptar", "ajustar la frase al contexto sin perder su propósito")],
    worked=[
        ("Reconocer el propósito", "En «La espera», ¿qué rasgos apoyan la idea de cansancio?", ["Caminar lento y dejar caer los brazos con suavidad sugieren poca energía.", "Detenerse y mirar hacia arriba sugieren una espera sin resultado."], "Lentitud, brazos que caen y detención apoyan el propósito de cansancio"),
        ("Adaptar al contexto", "La frase de la ficha pasa del contexto A al contexto B. ¿Qué se ajusta?", ["En la sala pequeña no caben 4 pasos largos: se acortan los pasos o la trayectoria.", "Se mantiene la lentitud y la caída suave de brazos, que son lo que transmite el propósito."], "Se acortan trayectorias y se conserva lentitud y caída de brazos"),
    ],
    mistakes=[("Cambiar el propósito al cambiar de lugar («en la sala pequeña ya no es una espera»).", "El contexto cambia las condiciones, no necesariamente la idea.", "Conserva los rasgos que transmiten el propósito y ajusta solo lo que el espacio exige."),
              ("Creer que interpretar es hacer el movimiento más grande o más fuerte.", "La intención no depende del tamaño o la fuerza.", "Usa las decisiones de tiempo, espacio y energía que apoyan el propósito, aunque sean pequeñas.")],
    T=[
        ('abc', '¿Qué es el propósito expresivo de una frase?', 'Lo que se quiere comunicar con ella', 'La cantidad de conteos que tiene', 'El nombre de quien la crea', 'Es la idea o emoción que se quiere comunicar; los conteos y el nombre son otros datos.'),
        ('abc', '{F} ¿Cuál es el propósito de «La espera»?', 'Transmitir una espera cansada', 'Mostrar velocidad y alegría', 'Mostrar fuerza y poder', 'La ficha lo declara: una espera cansada.'),
        ('abc', '{F} ¿Qué rasgo de la frase apoya el propósito?', 'Dejar caer los brazos con suavidad al final', 'Caminar muy rápido hacia atrás', 'Golpear el suelo con fuerza al final', 'Los brazos que caen con suavidad sugieren cansancio; los otros rasgos sugieren energía o apuro.'),
        ('abc', '¿Qué es el contexto de una presentación?', 'Lugar, público, tiempo y medios disponibles', 'Solo el nombre de la frase y quién la baila', 'La velocidad de los movimientos', 'El contexto reúne las condiciones de la presentación, no una sola característica del movimiento.'),
        ('abc', '{F} ¿Qué diferencia hay entre el contexto A y el B?', 'El A es abierto y el B es pequeño con público muy cerca', 'En el A hay música y baile en grupo y en el B se baila sin música ni público', 'El A es de noche y el B de día', 'La ficha solo distingue el tamaño del espacio y la cercanía del público.'),
        ('abc', 'Interpretar con intención significa', 'hacer la frase con decisiones de espacio, tiempo y energía elegidas para el propósito', 'hacer los movimientos lo más grandes posible', 'repetir la frase más veces hasta que quede perfecta y sin errores', 'La intención se nota en decisiones; el tamaño o las repeticiones no la aseguran.'),
        ('abc', '{F} Al pasar al contexto B, ¿qué se ajusta?', 'La trayectoria, que se acorta, y se conservan la lentitud y la caída suave de brazos', 'El propósito, que cambia a alegría porque el público está más cerca y espera algo más animado', 'Todo, empezando una frase distinta que se adapte mejor a la sala pequeña', 'Se ajusta lo que el espacio obliga y se conserva lo que sostiene el propósito.'),
        ('=', '{F} En el contexto A los 4 pasos tienen 3 tiempos cada uno y luego hay 2 tiempos de detención y 2 de caída de brazos. ¿Cuántos tiempos dura la frase?', '4*3+2+2', 'Se suman los tiempos de los pasos, de la detención y de la caída de brazos.', ' tiempos'),
        ('abc', 'Alguien no quiere presentar frente a todo el curso. ¿Qué alternativa es adecuada?', 'Presentar en un grupo pequeño o entregar un registro escrito de sus decisiones', 'Obligarlo a presentar para que se acostumbre', 'Ponerle una nota mínima por no presentarse y anotar que no participó', 'Se puede evaluar con otras evidencias y respetar su decisión.'),
        ('abc', 'Dos intérpretes hacen «caminar y detenerse». Una lo hace rápido y mirando a los lados; la otra lento y con la mirada fija. ¿Qué es probable?', 'Transmiten propósitos distintos, como apuro o duda frente a espera', 'Transmiten lo mismo, porque la acción de caminar y detenerse es igual', 'Solo cambia el nombre de la frase', 'Cambian tiempo y mirada, y con ellos el sentido que se percibe.'),
        ('abc', 'Debes presentar «La espera» en un pasillo angosto. ¿Qué decisión mantiene el propósito?', 'Acortar los pasos y conservar la lentitud y los brazos que caen', 'Cambiar a movimientos rápidos y más amplios para llenar el pasillo', 'Eliminar la pausa y los brazos', 'Se adapta el espacio y se conserva lo expresivo.'),
        ('=', 'En un ensayo hay 3 grupos que muestran su frase de 40 segundos, con 20 segundos de cambio entre grupos (hay 2 cambios). ¿Cuántos segundos dura la ronda?', '3*40+2*20', 'Se suman las tres frases y los dos cambios entre ellas.', ' segundos'),
        ('abc', 'Para comprobar si el propósito se entendió, ¿qué haces después de mostrar la frase?', 'Preguntar qué rasgos del movimiento vio quien miró y qué idea le dieron', 'Preguntar si le gustó o no le gustó', 'Explicar el propósito antes de mostrarla y no preguntar nada', 'Pedir rasgos observados y la idea que sugieren permite comprobar la comunicación.'),
    ],
    ctx=('abc', 'Un grupo debe mostrar su frase en una sala con poco espacio y cuatro personas. Su propósito es «agruparse para protegerse del frío». ¿Qué decisión de contexto es adecuada?', 'Usar niveles medios y bajos, con trayectorias cortas y sin contacto, formando un círculo cerrado', 'Correr por la sala dando vueltas para mostrar el frío y llamar la atención', 'Pedir a una persona que sostenga a las demás', 'Un círculo cerrado y movimiento acotado cabe en el espacio y mantiene el propósito sin riesgos.'),
    sc=[
        ("En Danza: ¿qué es el contexto de una presentación?", "El lugar, el público, el tiempo y los medios", "Son las condiciones en que se presenta la frase."),
        ("¿Qué se conserva al adaptar una frase a un espacio más pequeño?", "Los rasgos que transmiten el propósito", "Se ajusta el tamaño y se mantiene la idea."),
        ("¿Qué se ofrece a quien no quiere presentar frente a todo el curso?", "Una alternativa, como presentar en grupo pequeño", "La participación se respeta y se evalúa con otras evidencias."),
    ],
    op=("Elige un propósito (por ejemplo, alegría tranquila o duda). Describe una frase corta de 8 tiempos que lo exprese: qué hace el cuerpo, qué nivel, velocidad y energía usa. Luego explica cómo la adaptarías si debes presentarla en un lugar más pequeño.",
        "Propósito: duda. Frase: dar un paso adelante y volver al lugar, dos veces, lento y con la cabeza hacia un lado; nivel medio, energía contenida. En lugar pequeño: pasos más cortos, misma lentitud y misma inclinación de cabeza.",
        ["declara un propósito", "justifica decisiones de espacio, tiempo y energía", "explica una adaptación al contexto"],
        ["hoja con frase, propósito y adaptación"],
        ["cambiar el propósito al cambiar el lugar", "decir solo «con sentimiento»"],
        "Pregunta: «¿qué decisión muestra tu propósito?». Si responde «con ganas», pídele un rasgo concreto de movimiento."),
    reinforce="Describe por escrito un paseo de 8 tiempos con el propósito «prisa» y luego con el propósito «calma», cambiando solo velocidad y energía.",
    extend="Explica por qué un mismo movimiento puede significar algo distinto en un patio y en una sala pequeña.",
)
