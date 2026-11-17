"""Expresión corporal 3.º y 4.º medio HC: OAC-04 (manejar la conciencia de la propia corporalidad a partir del desarrollo de la condición física y su eficiencia en la acción motriz), clases 1 a 4. Datos de ejemplo rotulados; sin pruebas de salud ni comparación de cuerpos."""
from __future__ import annotations

from hc_exco_common import build

O4 = "EF-EXCO-3y4-OAC-04"

# ============================================================ OAC-04, clase 1
F = ("Ficha 14 (escaneo corporal de ejemplo de una persona inventada, antes y después de 3 minutos de caminata suave y giros suaves de articulaciones). "
     "Escala de sensación de 1 (muy suave) a 5 (muy intensa); durante la práctica el esfuerzo se mantiene entre 1 y 3. "
     "Registro antes y después: tensión en los hombros, 4 y 2; tensión en el cuello, 3 y 2; agitación de la respiración, 1 y 2; cansancio de las piernas, 1 y 2; claridad del apoyo de los pies, 2 y 3. "
     "Señales de alerta que obligan a detenerse y avisar a una persona adulta: dolor agudo, mareo, falta de aire inusual, náuseas o visión borrosa.")
build(
    O4, 1, F,
    use="Aprenderé a notar con atención lo que ocurre en mi cuerpo al moverme, a registrarlo con una escala sencilla y a distinguir el esfuerzo normal de una señal de alerta, con calentamiento y enfriamiento suaves.",
    prior=["Sé explorar a mi rango sin forzar.", "Sé calentar y enfriar con movimientos suaves.", "Sé que ante dolor o mareo me detengo y aviso."],
    explain=[
        "La conciencia corporal es la capacidad de notar qué ocurre en el propio cuerpo mientras te mueves: dónde hay apoyo, tensión o cansancio, cómo es la respiración y cómo se reparte el peso. Se desarrolla con atención. Un escaneo corporal recorre el cuerpo de los pies a la cabeza, sin juzgar, y anota cada sensación con una escala de 1 a 5.",
        "Se distinguen dos tipos de sensaciones. Las de esfuerzo normal, como un cansancio leve, una respiración algo más rápida o calor, suben y bajan con el ritmo de la práctica, y la práctica de conciencia se mantiene entre 1 y 3. Las señales de alerta (dolor agudo, mareo, falta de aire inusual, náuseas, visión borrosa) no se aguantan: se detiene la práctica, se descansa y se avisa a una persona adulta.",
        "Calentar prepara el cuerpo con movimientos suaves, como girar articulaciones, caminar o balancear los brazos, durante unos minutos; enfriar baja el ritmo con movimientos lentos y respiración calma. Registrar antes y después permite ver tus cambios sin compararte con nadie: los números son tuyos, sirven para decidir cómo seguir y no para evaluar tu cuerpo.",
    ],
    vocab=[("conciencia corporal", "capacidad de notar qué ocurre en el propio cuerpo al moverse"), ("escaneo corporal", "recorrido de atención por el cuerpo, de los pies a la cabeza, sin juzgar"), ("escala de sensación", "números de 1 a 5 para anotar qué tan intensa es una sensación"), ("señal de alerta", "sensación que obliga a detener la práctica y avisar"), ("enfriamiento", "movimientos lentos que bajan el ritmo al terminar")],
    worked=[
        ("Leer un cambio en el registro", "Una persona anota tensión de cuello 5 antes y 3 después de una práctica suave. ¿Qué cambió?", ["Se compara el valor de antes con el de después: 5 y 3.", "Bajó 2 puntos en la escala."], "La tensión del cuello bajó 2 puntos"),
        ("Distinguir esfuerzo y alerta", "Una persona anota: «cansancio leve en las piernas, 2» y otra: «dolor agudo en la rodilla». ¿Cuál es una señal de alerta?", ["El cansancio leve en 2 está dentro del esfuerzo normal (1 a 3).", "El dolor agudo está en la lista de señales de alerta."], "El dolor agudo en la rodilla"),
    ],
    mistakes=[("Aguantar un mareo para terminar la práctica y completar el registro.", "El mareo es una señal de alerta y seguir aumenta el riesgo.", "Detente, siéntate, respira y avisa a una persona adulta."),
              ("Comparar tu registro con el de otra persona para saber quién está mejor.", "Cada cuerpo tiene su rango y los números son personales, no un ranking.", "Compara tu antes y tu después y decide cómo seguir.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es la conciencia corporal?", "Notar qué ocurre en el propio cuerpo mientras te mueves", "Controlar el cuerpo para que se mueva igual que el de otra persona", "Aguantar las molestias hasta terminar toda la práctica del día", "La conciencia corporal es atención a las propias sensaciones, sin comparar ni aguantar molestias."),
        ("abc", "{F} ¿Qué sensación tuvo el mayor cambio entre antes y después?", "La tensión en los hombros", "La tensión en el cuello", "La claridad del apoyo de los pies", "Los hombros pasaron de 4 a 2, un cambio de 2 puntos; las demás cambiaron 1 punto."),
        ("=", "{F} La práctica de ejemplo dura 3 minutos de caminata, 4 giros de articulaciones de 30 segundos cada uno y 2 minutos de enfriamiento. ¿Cuántos segundos dura en total?", "3*60+4*30+2*60", "Se suman 180 segundos de caminata, 120 de giros y 120 de enfriamiento.", " segundos"),
        ("abc", "{F} ¿Cuál es una señal de alerta, según la ficha?", "Un dolor agudo", "Una respiración algo más agitada, nivel 2 de 5", "Un cansancio leve de las piernas, nivel 2 de 5", "El dolor agudo está en la lista de señales de alerta; las otras sensaciones están en el rango normal."),
        ("abc", "{F} Durante la práctica, ¿entre qué valores de la escala se mantiene el esfuerzo?", "Entre 1 y 3", "Entre 3 y 5, para notar mejor los cambios", "En 5 todo el tiempo, para ganar más conciencia", "La ficha pide mantenerse entre 1 y 3 para practicar con seguridad."),
        ("abc", "{F} ¿Qué dato muestra que el apoyo de los pies se volvió más claro?", "Pasó de 2 a 3 en claridad del apoyo", "Pasó de 4 a 2 en tensión de los hombros", "Pasó de 1 a 2 en cansancio de las piernas", "Solo la claridad del apoyo habla de los pies, y subió de 2 a 3."),
        ("abc", "Una persona siente mareo y visión borrosa al terminar la caminata. ¿Qué corresponde?", "Detenerse, sentarse y avisar a una persona adulta", "Hacer los movimientos de enfriamiento más rápido para recuperarse", "Seguir caminando hasta que la sensación desaparezca sola", "Mareo y visión borrosa son señales de alerta: se para, se descansa y se avisa."),
        ("abc", "¿Para qué sirve registrar la sensación antes y después de una práctica?", "Para ver tus cambios sin compararte con nadie", "Para decidir quién tiene mejor condición física del curso", "Para demostrar que la práctica siempre baja la tensión", "El registro personal muestra cambios propios y no sirve para jerarquizar personas."),
        ("abc", "{F} Una persona anota «cansancio de piernas 4» durante la práctica. ¿Qué corresponde?", "Bajar el ritmo o descansar, pues pasa de 3", "Seguir igual, porque 4 es una sensación normal de esfuerzo", "Subir el ritmo para que el cansancio se acostumbre", "Un esfuerzo de 4 pasa el rango de 1 a 3, así que se baja el ritmo o se descansa."),
        ("abc", "Alguien dice: «si no siento tensión, mi cuerpo no está trabajando bien». ¿Qué respuesta es más sólida?", "Sentir poca tensión puede ser normal; se observa sin juzgar", "Tiene razón, porque la tensión es la señal de que hay conciencia", "Tiene razón, por eso conviene apretar los músculos para notarla", "La conciencia es notar lo que hay, no producir tensión; apretar sin necesidad es ineficiente."),
        ("abc", "{F} Una compañera dice: «mi tensión de hombros bajó menos que la de la ficha, así que estoy peor». ¿Qué respuesta es más sólida?", "Cada registro es personal; importa cómo cambia el tuyo", "Tiene razón, porque bajar más puntos indica un cuerpo mejor", "Tiene razón, debería repetir hasta que baje lo mismo", "Los registros no se comparan entre personas: cada cuerpo tiene su rango."),
        ("abc", "{F} Se quiere saber si 3 minutos de caminata suave bajan la tensión de los hombros. ¿Qué plan es más prudente?", "Registrar antes y después varios días seguidos", "Registrar una sola vez y afirmar que siempre baja la tensión", "Comparar tu registro con el de otra persona del curso", "Varios registros con una práctica igual permiten ver si el cambio se repite."),
        ("=", "{F} Una persona repite la práctica cinco días. La tensión de hombros antes fue 4, 4, 3, 4 y 3, y después fue 2, 3, 2, 2 y 2. ¿Cuántos puntos bajó en total sumando los cinco días?", "(4+4+3+4+3)-(2+3+2+2+2)", "Los valores de antes suman 18 y los de después suman 11, y la diferencia es 7.", " puntos"),
    ],
    ctx=("abc", "En un taller, una persona anota «mis hombros están en 4». Un compañero responde: «yo siempre los tengo en 2, ¿qué te pasa?». ¿Qué respuesta del grupo es más adecuada?", "Recordar que cada registro es personal y no se compara", "Pedirle que haga los movimientos igual que su compañero", "Reír para bajar la tensión del grupo y seguir con la práctica", "Cada cuerpo tiene su rango; el registro sirve para decidir el siguiente paso propio."),
    sc=[
        ("En Expresión corporal: ¿entre qué valores de la escala se mantiene el esfuerzo en la práctica?", "Entre 1 y 3", "Ese rango permite practicar con seguridad y sin forzar."),
        ("¿Qué se hace ante una señal de alerta, como un mareo?", "Detenerse, descansar y avisar a una persona adulta", "La seguridad va antes que completar la práctica."),
        ("¿Se pueden comparar los registros de dos personas?", "No: son personales y cada cuerpo tiene su rango", "Los números sirven para decidir cómo seguir, no para ordenar a las personas."),
    ],
    op=("En tu zona, haz un escaneo corporal: anota de 1 a 5 cinco sensaciones (por ejemplo, tensión en hombros, tensión en cuello, respiración, cansancio de piernas, claridad del apoyo de los pies). Camina suave 3 minutos y gira despacio hombros y muñecas, siempre entre 1 y 3 de esfuerzo. Vuelve a anotar las cinco sensaciones, calcula qué cambió y escribe una frase: «Hoy noté que mi cuerpo…».",
        "Antes: hombros 3, cuello 2, respiración 1, piernas 1, apoyo 2. Después: hombros 2, cuello 2, respiración 2, piernas 2, apoyo 3. Cambió la tensión de hombros (bajó 1) y el apoyo (subió 1). Hoy noté que mi cuerpo se afloja cuando camino con calma y respiro por la nariz.",
        ["anota cinco sensaciones antes y después", "calcula qué cambió y evita comparaciones", "respeta el rango de esfuerzo de 1 a 3"],
        ["hoja con dos registros, el cálculo de cambios y la frase final"],
        ["superar el esfuerzo de 3", "aguantar una señal de alerta", "comparar su registro con el de otra persona"],
        "Pregunta: «¿qué sensación cambió más y de cuánto a cuánto?». Si el registro incluye juicios, pídele que los cambie por números y hechos."),
    reinforce="Haz un escaneo corporal de 5 sensaciones al despertar y otro antes de dormir, y anota qué cambió, sin juzgar.",
    extend="Explica por qué una persona puede sentir un esfuerzo de 2 y otra de 4 en la misma práctica y por qué eso no las hace mejores o peores.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 15 (componentes de la condición física y frases de ejemplo, inventados). "
     "Resistencia: mantener un esfuerzo suave durante varios minutos. Fuerza: sostener o empujar con los músculos. Movilidad: rango cómodo de las articulaciones. Equilibrio: mantener la posición del cuerpo sobre sus apoyos. Coordinación: combinar partes del cuerpo con ritmo. "
     "Frase P: 4 minutos de movimientos lentos y continuos, sin pausa. "
     "Frase Q: 6 cambios de nivel flexionando las rodillas, cada uno sostenido 4 tiempos. "
     "Frase R: equilibrios en un pie de 5 segundos cada uno, con la mano cerca de la pared. "
     "Frase S: un patrón de brazos en 3 tiempos y de piernas en 2 tiempos, a la vez. "
     "Frase T: tres giros amplios del torso a cada lado, llegando solo hasta donde es cómodo.")
build(
    O4, 2, F,
    use="Aprenderé qué capacidades de la condición física pide cada frase de movimiento, a desarrollarlas de forma gradual y segura y a adaptar la frase a mi rango sin comparar cuerpos.",
    prior=["Sé registrar sensaciones de 1 a 5.", "Sé que el esfuerzo se mantiene entre 1 y 3.", "Sé calentar y enfriar."],
    explain=[
        "La condición física es el conjunto de capacidades del cuerpo que permiten moverse con seguridad: resistencia (mantener un esfuerzo suave durante varios minutos), fuerza (sostener o empujar con los músculos), movilidad (rango cómodo de las articulaciones), equilibrio (mantener la posición sobre los apoyos) y coordinación (combinar partes del cuerpo con ritmo). Cada frase de movimiento pide algunas más que otras.",
        "Las capacidades se desarrollan con práctica regular y gradual. Se cambia una sola condición por vez, como la duración, las repeticiones o la dificultad, y se observa cómo responde el cuerpo: el esfuerzo debe quedar entre 1 y 3. Las mejoras son lentas, de semanas, y distintas en cada persona. No se compara con otras personas ni se juzga el cuerpo: se compara tu práctica de hoy con la tuya de hace unas semanas.",
        "Si una frase supera tu capacidad actual, se adapta: se divide en tramos con pausas, se reduce la amplitud, se usa un apoyo como la pared o una silla, o se acorta. Adaptar no es rendirse: es un paso del desarrollo. Siempre se calienta antes y se enfría después, y ante dolor, mareo o falta de aire inusual se detiene la práctica y se avisa a una persona adulta.",
    ],
    vocab=[("condición física", "conjunto de capacidades del cuerpo: resistencia, fuerza, movilidad, equilibrio y coordinación"), ("resistencia", "mantener un esfuerzo suave durante varios minutos"), ("movilidad", "rango cómodo de las articulaciones"), ("coordinación", "combinar partes del cuerpo con ritmo"), ("progresión", "aumento gradual de una sola condición de la práctica")],
    worked=[
        ("Reconocer la capacidad que pide una frase", "Una frase pide mantener 5 minutos de movimientos continuos y suaves. ¿Qué capacidad pide sobre todo?", ["Se pide sostener un esfuerzo suave durante varios minutos.", "Eso corresponde a la resistencia."], "Resistencia"),
        ("Aplicar una progresión", "Una persona hace 2 minutos continuos con esfuerzo 2. ¿Cómo progresa de forma gradual?", ["Se cambia una sola condición: la duración, a 3 minutos.", "Se vuelve a registrar el esfuerzo y solo se avanza si sigue entre 1 y 3."], "Pasar a 3 minutos y registrar el esfuerzo"),
    ],
    mistakes=[("Subir la duración, la amplitud y la velocidad de una frase a la vez.", "Con varios cambios juntos no se sabe qué causó el cansancio o la molestia.", "Cambia una sola condición por vez y registra el esfuerzo."),
              ("Creer que adaptar una frase es rendirse.", "Adaptar permite practicar con seguridad y es parte del desarrollo de la condición física.", "Divide, reduce o apoya la frase y avanza cuando el esfuerzo se mantenga entre 1 y 3.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es la resistencia?", "Mantener un esfuerzo suave durante varios minutos", "Sostener o empujar con los músculos durante unos segundos", "Combinar partes del cuerpo con ritmo en un mismo patrón", "La resistencia es sostener un esfuerzo suave en el tiempo; la fuerza y la coordinación son otras capacidades."),
        ("abc", "{F} ¿Qué capacidad pide sobre todo la frase P?", "Resistencia", "Fuerza de piernas", "Equilibrio en un pie", "Cuatro minutos continuos sin pausa piden sostener un esfuerzo suave."),
        ("abc", "{F} ¿Qué capacidad pide sobre todo la frase R?", "Equilibrio", "Movilidad", "Resistencia", "Mantenerse sobre un pie pide equilibrio."),
        ("abc", "{F} ¿Qué capacidad pide sobre todo la frase S?", "Coordinación", "Fuerza de brazos", "Movilidad de caderas", "Combinar brazos y piernas con ritmos distintos pide coordinación."),
        ("abc", "{F} ¿Qué frase pide sobre todo movilidad?", "La frase T, de giros del torso", "La frase Q, de cambios de nivel", "La frase P, de movimientos continuos", "Los giros amplios llegan al rango de las articulaciones; Q pide fuerza de piernas y P pide resistencia."),
        ("=", "{F} La frase Q tiene 6 cambios de nivel de 4 tiempos y 1 tiempo de pausa después de cada uno. ¿Cuántos tiempos dura?", "6*4+6*1", "Seis cambios de 4 tiempos suman 24 y las seis pausas de 1 tiempo suman 6.", " tiempos"),
        ("=", "{F} Se hacen equilibrios de 5 segundos en cada pie, 3 equilibrios por pie (6 en total), con 10 segundos de descanso después de cada uno. ¿Cuántos segundos dura la frase R así?", "6*5+6*10", "Los seis equilibrios suman 30 segundos y los seis descansos suman 60.", " segundos"),
        ("abc", "{F} Hoy una persona hace la frase P durante 3 minutos sin molestias, con esfuerzo 2. ¿Qué paso es más prudente?", "Probar 4 minutos, cambiando solo la duración", "Probar 4 minutos y hacer los movimientos más amplios y rápidos", "Hacer 8 minutos de una vez para ver si se aguanta bien", "Se cambia una sola condición y se avanza solo si el esfuerzo sigue entre 1 y 3."),
        ("abc", "Una persona no logra el equilibrio de la frase R. ¿Qué adaptación respeta su rango?", "Apoyar una mano en la pared o bajar el pie", "Cerrar los ojos para sentirse más seguro", "Intentarlo sin apoyo hasta lograrlo, aunque se caiga", "Un apoyo o menos altura reduce el riesgo; cerrar los ojos o forzar lo aumentan."),
        ("abc", "Alguien dice: «la condición física es solo resistencia». ¿Qué respuesta es más sólida?", "Incluye también fuerza, movilidad, equilibrio y coordinación", "Tiene razón, las demás son habilidades de la danza y no condición física", "Tiene razón, porque la resistencia incluye todas las demás", "La condición física es un conjunto de cinco capacidades, no solo resistencia."),
        ("abc", "{F} Se ensayan las frases Q y T el mismo día. ¿Qué plan respeta el cuidado del cuerpo?", "Calentar, hacer las frases con pausas y terminar con enfriamiento", "Hacer primero la frase más difícil sin calentar, para aprovechar la energía", "Hacer las dos frases seguidas sin pausas para ahorrar tiempo", "Calentar, pausar y enfriar protege al cuerpo."),
        ("abc", "{F} Una persona logra la frase P en 4 minutos, pero sus piernas llegan a 4 de esfuerzo. ¿Qué decisión es más prudente?", "Bajar el ritmo o la duración hasta que quede entre 1 y 3", "Mantener los 4 minutos, porque lograrlos ya muestra buena condición", "Agregar 2 minutos más para que el cansancio se normalice", "Un esfuerzo de 4 supera el rango; se ajusta la duración o el ritmo."),
        ("abc", "{F} Se quiere diseñar una frase de 3 minutos que trabaje resistencia y coordinación sin forzar. ¿Qué diseño es más coherente?", "Movimientos continuos de brazos y piernas con ritmos distintos", "Equilibrios largos de 30 segundos, uno tras otro, sin descanso", "Cambios de nivel muy profundos y rápidos, sin pausa, durante los 3 minutos", "Un patrón continuo con ritmos distintos pide resistencia y coordinación a un esfuerzo seguro."),
    ],
    ctx=("abc", "Un grupo de teatro ensaya una escena de 3 minutos con desplazamiento lento y continuo. Una integrante se agota antes de terminar. ¿Qué ajuste cuida su condición física?", "Dividir la escena en tramos con pausas", "Pedirle que haga solo los últimos 30 segundos y salga del resto", "Aumentar la velocidad para que termine antes de cansarse", "Dividir y progresar de a poco permite desarrollar resistencia sin forzar."),
    sc=[
        ("En Expresión corporal: ¿cuáles son las capacidades de la condición física de esta clase?", "Resistencia, fuerza, movilidad, equilibrio y coordinación", "Cada frase pide algunas de ellas más que otras."),
        ("¿Cuántas condiciones se cambian por vez al progresar?", "Una sola", "Así se sabe qué produjo el cansancio o la molestia."),
        ("¿Adaptar una frase es rendirse?", "No: es parte del desarrollo y permite practicar con seguridad", "Se avanza cuando el esfuerzo sigue entre 1 y 3."),
    ],
    op=("Elige una frase de la ficha 15 (P, Q, R, S o T) y adáptala a tu rango, sin forzar y con un apoyo cerca si lo necesitas. Escribe qué capacidad pide, qué adaptación haces (dividir, reducir, apoyar o acortar), cuánto dura tu versión y cuál sería el único cambio de progresión que probarías la próxima semana.",
        "Frase P (resistencia). Adaptación: 2 minutos con una pausa de 20 segundos en la mitad. Duración: 2 minutos más 20 segundos. Esfuerzo anotado: 2. Cambio de progresión: pasar a 3 minutos manteniendo la pausa y registrar el esfuerzo.",
        ["nombra la capacidad que pide la frase", "propone una adaptación que respeta su rango", "cambia una sola condición en la progresión"],
        ["hoja con la frase, la capacidad, la adaptación, la duración y la progresión"],
        ["cambiar varias condiciones a la vez", "forzar el cuerpo para completar la frase original", "compararse con otras personas"],
        "Pregunta: «¿qué capacidad pide y qué único cambio probarás?». Si propone dos cambios, pídele que elija uno."),
    reinforce="Escribe una frase de movimiento de 2 minutos y nombra qué capacidades de la condición física pide.",
    extend="Explica por qué una progresión de una sola condición por vez es más segura que subir duración y dificultad a la vez.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 16 (cuatro versiones de un mismo gesto, de ejemplo). Gesto: «alcanzar un estante alto» (imaginario), 6 tiempos, en la propia zona; el resultado es llegar con la mano a la altura marcada. "
     "Versión A: hombros subidos, mandíbula apretada y respiración contenida; esfuerzo 4; 3 tensiones innecesarias. "
     "Versión B: hombros sueltos, mandíbula suelta y exhalación al subir el brazo; esfuerzo 2; 0 tensiones innecesarias. "
     "Versión C: hombros sueltos, mandíbula apretada y respiración libre; esfuerzo 3; 1 tensión innecesaria. "
     "Versión D: igual que B, pero en 2 tiempos y con el cuerpo inclinado hacia adelante; esfuerzo 3; 0 tensiones innecesarias; pierde el apoyo estable de los pies.")
build(
    O4, 3, F,
    use="Aprenderé qué es la eficiencia en la acción motriz, a detectar tensiones innecesarias y a mejorar un gesto con la fuerza justa, una buena respiración y un apoyo estable, sin forzar.",
    prior=["Sé registrar el esfuerzo de 1 a 5.", "Sé que la base de apoyo da estabilidad.", "Sé que cada cuerpo tiene su propio rango."],
    explain=[
        "La eficiencia en la acción motriz es lograr el resultado con la fuerza justa, sin tensiones sobrantes, con buena alineación, respiración libre y apoyo estable. No es hacer menos: es hacerlo mejor. Una tensión innecesaria es una parte del cuerpo que se aprieta sin que la acción la necesite, como los hombros subidos, la mandíbula apretada o las manos rígidas.",
        "Para detectar tensiones se repite el gesto despacio y se recorre el cuerpo con la atención. Se registra el esfuerzo y cuántas tensiones sobran. Se mejora soltando una sola tensión por vez, dejando que la respiración acompañe el movimiento (por ejemplo, soltar el aire al subir el brazo) y cuidando que los pies mantengan un apoyo estable. Hacerlo más rápido o con más fuerza no lo vuelve más eficiente.",
        "Se trabaja a tu rango y sin forzar. Si un gesto da dolor agudo, mareo u hormigueo, se detiene y se avisa a una persona adulta. La eficiencia es un asunto del gesto, no del cuerpo: una versión con más tensiones no hace a nadie peor, solo muestra qué se puede soltar.",
    ],
    vocab=[("eficiencia motriz", "lograr el resultado con la fuerza justa y sin tensiones sobrantes"), ("tensión innecesaria", "parte del cuerpo que se aprieta sin que la acción la necesite"), ("alineación", "orden de cabeza, columna y pelvis sobre el eje del cuerpo"), ("respiración libre", "respiración que acompaña el movimiento sin contenerse"), ("apoyo estable", "pies firmes en el suelo con una base suficiente")],
    worked=[
        ("Elegir la versión más eficiente", "La versión 1 de un gesto tiene esfuerzo 4 y 2 tensiones innecesarias; la versión 2 tiene esfuerzo 2 y ninguna. Ambas logran el mismo resultado. ¿Cuál es más eficiente?", ["Ambas cumplen el resultado, así que se compara el esfuerzo y las tensiones.", "La versión 2 usa menos esfuerzo y no tiene tensiones sobrantes."], "La versión 2"),
        ("Soltar una tensión por vez", "Un gesto tiene hombros subidos y mandíbula apretada. ¿Cómo se mejora de forma gradual?", ["Se suelta una sola tensión por ensayo para ver su efecto.", "Primero los hombros y, en otro ensayo, la mandíbula, registrando el esfuerzo."], "Soltar primero los hombros y después la mandíbula, en ensayos separados"),
    ],
    mistakes=[("Hacer un gesto con más fuerza para que se vea más preciso.", "Más fuerza suele sumar tensiones y baja la precisión.", "Usa la fuerza justa y suelta las partes que no se necesitan."),
              ("Mejorar un gesto acortándolo hasta perder el apoyo estable de los pies.", "Perder el apoyo aumenta el esfuerzo y el riesgo de desequilibrio.", "Mantén los pies firmes y una base suficiente.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es una tensión innecesaria?", "Una parte del cuerpo que se aprieta sin necesidad", "Una molestia fuerte que obliga a detener la práctica", "Un esfuerzo que se usa para vencer la gravedad al subir", "Una tensión innecesaria es un apretón sobrante; el dolor es una señal de alerta."),
        ("abc", "En Expresión corporal: ¿qué es la eficiencia en la acción motriz?", "Lograr el resultado con la fuerza justa y sin tensiones sobrantes", "Hacer la acción lo más rápido posible, aunque cueste más esfuerzo", "Hacer la acción con la menor cantidad de movimiento posible", "Eficiencia es el mismo resultado con menos esfuerzo sobrante, no velocidad ni reducción de movimiento."),
        ("abc", "{F} ¿Qué versión tiene más tensiones innecesarias?", "La versión A", "La versión C", "La versión B", "La A tiene 3 tensiones; la C tiene 1 y la B no tiene ninguna."),
        ("abc", "{F} ¿Qué diferencia hay entre las versiones B y C?", "En B la mandíbula está suelta y en C está apretada", "En B los hombros están subidos y en C están sueltos", "En B el gesto dura más tiempos que en C", "Ambas tienen hombros sueltos y respiración libre; solo cambia la mandíbula."),
        ("=", "{F} La versión B se repite 8 veces, y después de cada repetición hay 3 tiempos de pausa. ¿Cuántos tiempos dura la serie?", "8*(6+3)", "Cada repetición dura 6 tiempos más 3 de pausa, y se hacen 8 veces.", " tiempos"),
        ("abc", "{F} ¿Qué versión es más eficiente y segura?", "La versión B", "La versión D", "La versión A", "La B tiene el menor esfuerzo, ninguna tensión innecesaria y mantiene el apoyo."),
        ("abc", "{F} ¿Por qué la versión D no es la más eficiente?", "Pierde el apoyo y exige más esfuerzo que B", "Tiene tensiones innecesarias en los hombros y la mandíbula", "Dura más tiempos que las otras versiones del gesto", "D no tiene tensiones, pero cuesta más esfuerzo que B y pierde el apoyo estable de los pies."),
        ("abc", "{F} Quieres pasar de la versión C a la versión B. ¿Qué cambio haces?", "Soltar la mandíbula", "Subir los hombros para apoyar mejor el brazo en el movimiento", "Contener la respiración para ganar firmeza", "La única diferencia entre C y B es la mandíbula apretada."),
        ("abc", "Mientras sostienes un gesto notas que contienes la respiración. ¿Qué corresponde?", "Soltar el aire de forma natural y seguir con respiración libre", "Inhalar más profundo y aguantar el aire hasta terminar el gesto", "Apretar más el abdomen para mantener el control del gesto", "Contener la respiración suma tensión; dejar que la respiración acompañe es más eficiente."),
        ("abc", "Alguien dice: «si hago el gesto con más fuerza se ve más preciso». ¿Qué respuesta es más sólida?", "Más fuerza suma tensiones; la precisión viene de la fuerza justa", "Tiene razón, porque la fuerza siempre aumenta la precisión del movimiento", "Tiene razón, mientras el gesto dure pocos tiempos en total", "Sumar fuerza agrega tensiones sobrantes y no aumenta la precisión."),
        ("abc", "Una estudiante siente dolor agudo en el hombro al repetir el gesto. ¿Qué corresponde?", "Detenerse y avisar a una persona adulta", "Soltar los hombros y seguir hasta terminar la serie", "Hacer el gesto más rápido para que el dolor pase antes", "El dolor agudo es una señal de alerta: se para y se avisa."),
        ("abc", "{F} Alguien afirma: «la versión B es más eficiente que la A, así que mi cuerpo es peor porque yo hago la A». ¿Qué falla?", "Confunde la forma del gesto con un juicio sobre su cuerpo", "Debió comparar la versión A con la versión D para estar segura", "Debió hacer la versión B con más fuerza para poder compararla", "La eficiencia describe cómo se hace un gesto; no mide ni juzga cuerpos."),
        ("abc", "{F} Se quiere pasar de la versión A a la B en tres sesiones, soltando una tensión por sesión. ¿Qué plan es adecuado?", "Una tensión por sesión: mandíbula, hombros y respiración", "Soltar las tres tensiones a la vez y subir el esfuerzo en la primera sesión", "Hacer la versión D desde la primera sesión para sentir qué cambia más rápido", "Una tensión por sesión permite ver el efecto de cada cambio."),
    ],
    ctx=("abc", "Un grupo debe sostener el gesto de «cargar un peso imaginario» durante 8 tiempos. Una integrante nota que sube los hombros hasta las orejas. ¿Qué ajuste mejora su eficiencia sin perder la intención?", "Soltar los hombros y mantener la intención en la mirada", "Subir más los hombros para que el peso imaginario se note", "Acortar el gesto a 2 tiempos para que no se note la tensión", "Soltar lo que sobra mantiene la intención del peso con menos esfuerzo."),
    sc=[
        ("En Expresión corporal: ¿qué significa ser eficiente al hacer un gesto?", "Lograr el resultado con la fuerza justa y sin tensiones sobrantes", "No es hacer menos, es hacerlo mejor."),
        ("¿Cuántas tensiones se sueltan por ensayo al mejorar un gesto?", "Una sola, para ver su efecto", "Con un cambio por ensayo se sabe qué mejoró el gesto."),
        ("¿La eficiencia mide el cuerpo de una persona?", "No: describe cómo se hace un gesto", "Una versión con más tensiones solo muestra qué se puede soltar."),
    ],
    op=("Elige un gesto cotidiano seguro (como alcanzar un estante alto, imaginario). Hazlo tres veces en tu zona, sin forzar: primero como sale, luego soltando una tensión (hombros o mandíbula) y luego soltando otra o dejando que la respiración lo acompañe. Anota en cada versión el esfuerzo (1 a 5) y las tensiones innecesarias. Elige la más eficiente y explica por qué.",
        "Gesto: alcanzar un estante alto. Versión 1: como sale; esfuerzo 4; 2 tensiones (hombros y mandíbula). Versión 2: hombros sueltos; esfuerzo 3; 1 tensión (mandíbula). Versión 3: hombros y mandíbula sueltos, exhalo al subir; esfuerzo 2; 0 tensiones. Elijo la 3 porque logra lo mismo con menos esfuerzo.",
        ["registra esfuerzo y tensiones de cada versión", "cambia una sola tensión por vez", "elige la versión más eficiente con una razón"],
        ["hoja con tres versiones, esfuerzo, tensiones y la elegida con su razón"],
        ["hacer más fuerza para lograr precisión", "soltar varias tensiones a la vez", "forzar el cuerpo o perder el apoyo de los pies"],
        "Pregunta: «¿qué soltaste en cada versión y cuánto bajó el esfuerzo?». Si cambió más de una cosa por vez, pídele que repita separándolas."),
    reinforce="Describe dos versiones de «levantar los brazos sobre la cabeza»: una con tensiones innecesarias y otra eficiente. Indica el esfuerzo de cada una.",
    extend="Explica por qué mejorar la eficiencia puede dejar a una persona con más energía para expresar, y qué límite pone la seguridad.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 17 (plan de práctica autónoma de ejemplo, de una persona inventada). Meta: «mantener una frase continua de 3 minutos con esfuerzo entre 1 y 3». "
     "Cada sesión tiene calentamiento de 3 minutos, trabajo de 6 minutos y enfriamiento de 3 minutos. Semana 1: lunes, miércoles y viernes. "
     "Semana 2: los mismos días, y el trabajo sube a 8 minutos (solo cambia la duración). "
     "Regla de ajuste: si el esfuerzo pasa de 3 o aparece una señal de alerta, se vuelve a la duración anterior o se detiene la práctica y se avisa a una persona adulta. "
     "Registro después de cada sesión: duración, esfuerzo (1 a 5) y una frase sobre cómo se sintió. Esfuerzos de la semana 1: 2, 3 y 2.")
build(
    O4, 4, F,
    use="Aprenderé a armar una práctica autónoma segura de conciencia corporal: una meta, sesiones con calentamiento y enfriamiento, una progresión gradual, un registro privado y reglas de ajuste.",
    prior=["Sé registrar el esfuerzo de 1 a 5.", "Sé qué capacidades pide una frase.", "Sé que cambio una sola condición por vez."],
    explain=[
        "Una práctica autónoma segura es un plan propio, simple y flexible. Tiene una meta clara y medible (por ejemplo, mantener una frase de 3 minutos con esfuerzo entre 1 y 3), días definidos y una sesión con tres partes: calentamiento, trabajo y enfriamiento. Se registra cada sesión con su duración, su esfuerzo y una frase sobre cómo te sentiste.",
        "El plan avanza de forma gradual: se cambia una sola condición por vez (duración, repeticiones o dificultad) y se observa el esfuerzo. Si el esfuerzo pasa de 3 o aparece una señal de alerta, se vuelve a la condición anterior o se detiene la práctica. El descanso entre sesiones es parte del plan, no una pérdida de tiempo, y el plan se ajusta cuando cambia el espacio o el tiempo disponible.",
        "La práctica es personal y privada: tu registro no se compara ni se comparte si no quieres, y no se miden pesos ni medidas del cuerpo. Si tienes una lesión, una condición de salud o dudas, consulta antes con un profesional de la salud o con tu docente. Se practica en un espacio despejado, con ropa y calzado cómodos y agua a mano.",
    ],
    vocab=[("práctica autónoma", "plan propio de práctica, con meta, sesiones, registro y reglas de ajuste"), ("meta medible", "objetivo que se puede comprobar con un dato, como minutos o esfuerzo"), ("progresión gradual", "aumento de una sola condición por vez"), ("regla de ajuste", "decisión acordada de antemano sobre qué hacer si el esfuerzo sube o hay una alerta"), ("registro privado", "anotación personal que no se compara ni se comparte si no quieres")],
    worked=[
        ("Calcular los minutos de una semana", "Un plan tiene 3 sesiones por semana de 4 + 7 + 4 minutos. ¿Cuántos minutos suma la semana?", ["Una sesión suma 4 + 7 + 4 = 15 minutos.", "Tres sesiones suman 3 × 15 = 45."], "45 minutos"),
        ("Aplicar una regla de ajuste", "Una persona anota esfuerzo 4 en una sesión de duración nueva. ¿Qué dice la regla de ajuste?", ["El esfuerzo pasa de 3.", "Se vuelve a la duración anterior en la siguiente sesión."], "Volver a la duración anterior"),
    ],
    mistakes=[("Subir la duración y la dificultad a la vez para llegar antes a la meta.", "Con dos cambios juntos no se sabe qué subió el esfuerzo y aumenta el riesgo.", "Cambia una sola condición por semana y registra el esfuerzo."),
              ("Compartir el registro para saber quién avanza más.", "El registro es personal y compararlo lleva a juzgar cuerpos.", "Guarda tu registro y compara tu práctica de hoy con la tuya de hace unas semanas.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es una práctica autónoma segura?", "Un plan propio con meta, registro y reglas de ajuste", "Entrenar todo lo posible hasta lograr la meta sin descansar", "Copiar el plan de otra persona sin cambiar nada", "Una práctica autónoma segura es un plan propio con reglas; no es copiar ni forzar."),
        ("=", "{F} ¿Cuántos minutos dura una sesión de la semana 1?", "3+6+3", "Se suman el calentamiento (3), el trabajo (6) y el enfriamiento (3).", " minutos"),
        ("=", "{F} ¿Cuántos minutos suma la semana 2, con tres sesiones?", "3*(3+8+3)", "Cada sesión suma 14 minutos y hay 3 sesiones.", " minutos"),
        ("abc", "{F} ¿Qué condición cambia entre la semana 1 y la semana 2?", "Solo la duración del trabajo", "La duración y los días de la semana", "El calentamiento y el enfriamiento", "La ficha dice que solo cambia la duración, de 6 a 8 minutos."),
        ("abc", "{F} ¿Por qué se cambia una sola condición por vez?", "Para saber qué provocó la sensación de esfuerzo", "Para que el plan quede más corto de escribir", "Para que todas las semanas sumen los mismos minutos", "Con un solo cambio se puede atribuir el efecto sobre el esfuerzo."),
        ("abc", "{F} En la sesión del miércoles de la semana 2 el esfuerzo es 4. ¿Qué dice la regla?", "Volver a la duración anterior", "Subir a 10 minutos para acostumbrarse al esfuerzo", "Terminar la sesión sin anotar nada en el registro", "La regla manda volver a la duración anterior cuando el esfuerzo pasa de 3."),
        ("=", "{F} El plan se adapta a un espacio de 6 m por 3 m, con zonas de 2 m por 2 m. ¿Cuántas personas pueden practicar a la vez?", "(6//2)*(3//2)", "A lo largo de 6 m caben 3 zonas de 2 m y a lo ancho de 3 m cabe 1 (sobra 1 m): 3 × 1 = 3.", " personas"),
        ("abc", "{F} Una persona siente un dolor agudo en la rodilla en el minuto 4 del trabajo. ¿Qué hace?", "Se detiene, descansa y avisa a una persona adulta", "Termina los minutos que faltan con menos velocidad", "Cambia al calentamiento de nuevo y sigue después", "El dolor agudo es una señal de alerta: se detiene la práctica y se avisa."),
        ("abc", "Una estudiante tiene una lesión antigua que a veces duele. ¿Qué es lo más prudente antes de empezar un plan?", "Consultar a un profesional de la salud o a su docente", "Empezar con el plan completo y ver si molesta", "Pedir a una compañera que le diga qué ejercicios hacer", "Con una lesión o duda, la orientación de un profesional va antes de empezar."),
        ("abc", "Alguien dice: «mi plan es mejor que el tuyo porque dura más». ¿Qué respuesta es más sólida?", "Los planes son personales: importa que calcen con cada meta", "Tiene razón, porque más minutos siempre significan mejor condición", "Tiene razón, salvo que el plan incluya días de descanso", "Un plan se valora por su ajuste a la meta y al cuerpo de cada persona, no por su duración."),
        ("abc", "{F} Se quiere llegar a 3 minutos continuos desde 1 minuto. ¿Qué progresión es más prudente?", "1, 2 y 3 minutos en tres sesiones", "1, 3 y 5 minutos en tres sesiones, para avanzar más rápido que antes", "3 minutos desde la primera sesión, para ver si se logra", "Subir de a poco y registrar el esfuerzo es la progresión gradual."),
        ("abc", "{F} Después de cuatro semanas alguien anota: «logré la meta, así que mi cuerpo está en su mejor forma». ¿Qué falla?", "Convierte el logro de una meta en un juicio del cuerpo", "No comparó su resultado con el de otra persona del curso", "No subió la duración en la cuarta semana del plan", "La meta mide una práctica, no el valor ni la forma de un cuerpo."),
        ("abc", "{F} Se quiere medir el avance sin comparar cuerpos. ¿Qué dato es adecuado registrar?", "La duración, el esfuerzo y cómo se sintió", "El peso y las medidas del cuerpo cada semana", "Cuánto aguantó más que otras personas del grupo", "Duración, esfuerzo y sensación son personales y seguros; las medidas del cuerpo y las comparaciones no."),
    ],
    ctx=("abc", "Un grupo de teatro decide hacer prácticas de 10 minutos antes de cada ensayo. Dos integrantes comienzan a comparar quién se cansó menos. ¿Qué decisión mantiene el cuidado de todas?", "Que cada una anote su registro y no se comparen cuerpos ni cansancio", "Anotar los resultados de todas en una tabla para ver quién avanza más", "Pedir a quien se cansó más que descanse hasta alcanzar al resto", "Los registros son personales y comparar cuerpos presiona y no ayuda."),
    sc=[
        ("En Expresión corporal: ¿qué tres partes tiene una sesión de práctica?", "Calentamiento, trabajo y enfriamiento", "Esa estructura prepara y cuida el cuerpo."),
        ("¿Qué dice una regla de ajuste si el esfuerzo pasa de 3?", "Volver a la condición anterior o detener la práctica", "La regla se acuerda de antemano para decidir con calma."),
        ("¿A quién se consulta si hay una lesión o una duda de salud?", "A un profesional de la salud o a tu docente antes de empezar", "Este cuaderno no entrega diagnósticos ni ejercicios personales."),
    ],
    op=("Escribe un plan de 2 semanas para una práctica autónoma de conciencia corporal: una meta medible, tres días por semana, una sesión con calentamiento, trabajo y enfriamiento (con minutos), un solo cambio de progresión entre la semana 1 y la 2, una regla de ajuste y qué registrarás. Calcula los minutos de cada semana. Si tienes una lesión o una duda de salud, anótalo y consulta a un profesional o a tu docente antes de empezar.",
        "Meta: mantener 2 minutos de una frase continua con esfuerzo entre 1 y 3. Sesión semana 1: calentamiento 3, trabajo 5, enfriamiento 3 = 11 minutos; 3 sesiones = 33. Semana 2: trabajo 6 (único cambio) = 12 por sesión; 3 sesiones = 36. Regla: si el esfuerzo pasa de 3 o aparece una alerta, vuelvo a 5 minutos o me detengo y aviso. Registro: duración, esfuerzo y una frase.",
        ["incluye meta, estructura, progresión y regla de ajuste", "calcula los minutos de cada semana", "cuida la privacidad y la seguridad"],
        ["plan escrito de dos semanas con minutos, regla de ajuste y registro"],
        ["cambiar varias condiciones a la vez", "medir el peso o las medidas del cuerpo", "no incluir una regla ante señales de alerta"],
        "Pregunta: «¿qué único cambio haces entre semanas y qué haces si el esfuerzo pasa de 3?». Si cambia más de uno, pídele que elija uno."),
    reinforce="Escribe una sesión de 12 minutos con calentamiento, trabajo y enfriamiento, y la regla de ajuste que usarías si el esfuerzo pasa de 3.",
    extend="Explica por qué una práctica con registro privado y reglas de ajuste cuida mejor al cuerpo que una práctica sin plan.",
)
