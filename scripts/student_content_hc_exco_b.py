"""Expresión corporal 3.º y 4.º medio HC: OAC-03 (usar las leyes del movimiento y las fuerzas externas: tiempo, espacio, peso, flujo y energía), clases 1 a 5. Fichas inventadas, todo por escrito; las acciones con objetos son imaginarias."""
from __future__ import annotations

from hc_exco_common import build

O3 = "EF-EXCO-3y4-OAC-03"

# ============================================================ OAC-03, clase 1
F = ("Ficha 9 (pruebas de base de apoyo de ejemplo, inventadas). Se hacen en la propia zona, con una mano cerca de una pared y sin forzar. "
     "Prueba 1: de pie con los pies juntos, balancear el cuerpo un poco hacia adelante y atrás durante 5 segundos; anotó: oscila mucho. "
     "Prueba 2: igual, pero con los pies separados al ancho de los hombros; anotó: oscila poco. "
     "Prueba 3: con los pies al ancho de los hombros, flexionar las rodillas despacio en 4 tiempos y volver a subir en 4 tiempos; anotó: el cuerpo se siente más pesado y estable abajo. "
     "Prueba 4: con los pies al ancho de los hombros, subir los brazos sobre la cabeza en 4 tiempos; anotó: el cuerpo se siente más liviano y menos estable.")
build(
    O3, 1, F,
    use="Aprenderé cómo la gravedad, el peso, el centro de gravedad y la base de apoyo influyen en el movimiento y en lo que comunica, y a explorarlos con seguridad y a mi rango.",
    prior=["Sé explorar con conciencia a mi rango.", "Sé que el cuerpo tiene apoyos y un eje.", "Sé que la gravedad existe y atrae los cuerpos hacia el suelo."],
    explain=[
        "El movimiento ocurre bajo fuerzas externas. La principal es la gravedad, que tira del cuerpo hacia el suelo y se siente como peso. El suelo responde empujando de vuelta, y esa reacción nos permite estar de pie y caminar. El centro de gravedad es el punto donde parece concentrarse el peso del cuerpo; la base de apoyo es la zona del suelo que queda entre los apoyos, por ejemplo entre los dos pies.",
        "Cuanto más ancha es la base de apoyo y más bajo está el centro de gravedad, más estable es el cuerpo. Con los pies juntos y los brazos arriba la estabilidad baja; con los pies separados y las rodillas flexionadas sube. En expresión, el peso también es una cualidad: un movimiento es firme cuando cede a la gravedad y empuja el suelo, y es liviano cuando parece resistir la gravedad, como subir con suavidad.",
        "Se explora con seguridad: cerca de una pared o una silla, sin saltos, sin caídas y sin perder el control. «Ceder al peso» significa flexionar las rodillas despacio y a tu rango, nunca dejarse caer. Si hay dolor, mareo o pérdida de equilibrio que no controlas, se detiene la prueba y se avisa a una persona adulta.",
    ],
    vocab=[("gravedad", "fuerza que tira del cuerpo hacia el suelo y se siente como peso"), ("centro de gravedad", "punto donde parece concentrarse el peso del cuerpo"), ("base de apoyo", "zona del suelo que queda entre los apoyos del cuerpo"), ("peso firme", "movimiento que cede a la gravedad y empuja el suelo"), ("peso liviano", "movimiento que parece resistir la gravedad")],
    worked=[
        ("Comparar dos bases", "Una persona se balancea con los pies juntos y luego con los pies separados al ancho de los hombros. ¿En cuál oscila menos y por qué?", ["Con los pies separados la base de apoyo es más ancha.", "Una base más ancha da mayor estabilidad."], "Oscila menos con los pies separados, porque la base es más ancha"),
        ("Identificar un peso liviano", "Alguien sube un brazo lentamente como si la mano fuera de pluma. ¿Qué cualidad de peso comunica?", ["Subir con suavidad parece resistir la gravedad.", "Eso corresponde al peso liviano."], "Peso liviano"),
    ],
    mistakes=[("Creer que «ceder al peso» es dejarse caer.", "Dejarse caer pierde el control y es inseguro; ceder es bajar con control.", "Flexiona las rodillas despacio, a tu rango y con apoyo cerca."),
              ("Pensar que una base angosta siempre es mala.", "Una base angosta da menos estabilidad pero permite girar y desplazarse con ligereza; depende de la intención.", "Elige la base según lo que quieres comunicar y lo que es seguro.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es la base de apoyo?", "La zona del suelo que queda entre los apoyos del cuerpo", "El punto donde parece concentrarse todo el peso del cuerpo", "La cantidad de energía que se usa al empujar el suelo con fuerza", "La base es la superficie entre los apoyos; el punto del peso es el centro de gravedad."),
        ("abc", "{F} ¿Qué cambia entre la prueba 1 y la prueba 2?", "El ancho de la base de apoyo", "La velocidad del balanceo del cuerpo", "El tiempo que dura cada una de las dos pruebas", "Ambas duran 5 segundos con el mismo balanceo; solo cambia la separación de los pies."),
        ("abc", "En Expresión corporal: ¿qué papel tiene la gravedad en el movimiento?", "Tira del cuerpo hacia el suelo y se siente como peso", "Impulsa el cuerpo hacia arriba cada vez que se estira", "Mueve el cuerpo hacia adelante cuando se camina con rapidez", "La gravedad atrae hacia el suelo; no impulsa hacia arriba ni empuja hacia adelante."),
        ("abc", "{F} ¿Qué muestra la prueba 3 sobre el centro de gravedad?", "Al bajarlo, el cuerpo se siente más estable", "Al bajarlo, el cuerpo se siente más liviano y menos estable", "Su altura no cambia al flexionar las rodillas con los pies fijos", "Flexionar baja el centro de gravedad, y un centro más bajo da más estabilidad."),
        ("abc", "{F} ¿Por qué en la prueba 4 el cuerpo se siente menos estable?", "Los brazos arriba suben el centro de gravedad", "Los brazos arriba ensanchan la base de apoyo en el suelo", "La gravedad deja de actuar sobre el cuerpo al subir los brazos", "Con la misma base y un centro de gravedad más alto, la estabilidad baja."),
        ("abc", "En Expresión corporal: ¿qué es un peso liviano en el movimiento?", "Un movimiento que parece resistir la gravedad", "Un movimiento que cede a la gravedad y empuja el suelo con firmeza", "Un movimiento hecho siempre con poca energía y sin apoyo en el suelo", "El peso liviano resiste la gravedad; el firme cede a ella."),
        ("=", "{F} La prueba 3 se hace 3 veces: en cada una se baja en 4 tiempos y se sube en 4 tiempos, y hay una pausa de 2 tiempos entre repeticiones (2 pausas en total). ¿Cuántos tiempos dura todo?", "3*(4+4)+2*2", "Tres repeticiones de 8 tiempos suman 24 y las dos pausas de 2 tiempos suman 4.", " tiempos"),
        ("abc", "{F} Se quiere un movimiento de peso firme, que ceda a la gravedad. ¿Qué opción corresponde?", "Bajar despacio flexionando las rodillas y empujando el suelo", "Subir los brazos y la cabeza, como si algo tirara hacia arriba", "Dar pasos muy rápidos y livianos, apenas tocando el suelo", "Ceder al peso y empujar el suelo es peso firme; subir o apenas tocar el suelo es liviano."),
        ("abc", "Una estudiante siente mareo al balancearse en la prueba 1. ¿Qué corresponde?", "Detenerse, sentarse y avisar a una persona adulta", "Seguir con los ojos cerrados para concentrarse más", "Balancearse más rápido hasta que el mareo pase", "El mareo obliga a detenerse y avisar; cerrar los ojos o acelerar aumenta el riesgo."),
        ("abc", "Alguien dice: «si ensancho la base siempre me muevo mejor». ¿Qué respuesta es más sólida?", "Da estabilidad, pero limita el desplazamiento; depende de la intención", "Tiene razón, porque una base ancha permite cualquier movimiento sin riesgo", "Tiene razón, y por eso conviene mantener los pies siempre separados", "Una base ancha estabiliza pero limita; se elige según la intención y la seguridad."),
        ("abc", "{F} Se quiere comprobar el efecto de la altura de los brazos en la estabilidad. ¿Qué plan es válido?", "Mantener la base ancha y comparar brazos abajo con brazos arriba", "Comparar brazos arriba con pies juntos y brazos abajo con pies separados", "Comparar brazos arriba mirando al frente y brazos abajo con los ojos cerrados", "Para atribuir el efecto a los brazos, la base y lo demás deben quedar iguales."),
        ("abc", "{F} Camila anota: «con los pies juntos oscilo más; entonces los pies juntos son una mala postura». ¿Qué falla en su conclusión?", "Convierte un dato en un juicio sobre la postura", "No midió cuántos segundos duró la prueba con cada postura", "Debió hacer la prueba con los ojos cerrados para ver más", "Los pies juntos dan menos estabilidad, pero no son malos: comunican otra cosa."),
        ("abc", "{F} Para comunicar «aguantar una carga pesada» con el cuerpo, ¿qué combinación es más coherente?", "Base ancha, rodillas flexionadas y descenso lento", "Base angosta, brazos arriba y movimiento rápido hacia arriba", "Base ancha, brazos arriba y pasos pequeños y ligeros", "Peso firme significa base ancha, rodillas flexionadas y movimiento que cede."),
    ],
    ctx=("abc", "Un grupo quiere mostrar «cansancio» con peso firme: hombros caídos, rodillas algo flexionadas, pies separados y movimientos lentos, sin dejarse caer. ¿Qué rasgo hace seguro el plan?", "Ceder al peso con control, con la base ancha y sin caídas", "Dejarse caer en el último tiempo para que se note el cansancio", "Cerrar los ojos mientras se baja para sentir más el peso", "Ceder con control mantiene la intención y evita caídas y pérdida del equilibrio."),
    sc=[
        ("En Expresión corporal: ¿qué es el centro de gravedad?", "El punto donde parece concentrarse el peso del cuerpo", "Es una referencia para entender el equilibrio y la estabilidad."),
        ("¿Qué base y qué centro de gravedad dan más estabilidad?", "Una base ancha y un centro de gravedad bajo", "Con más apoyo y más cerca del suelo el cuerpo se sostiene mejor."),
        ("¿Qué significa «ceder al peso» con seguridad?", "Bajar con control flexionando las rodillas, nunca dejarse caer", "Ceder es un descenso controlado dentro del rango propio."),
    ],
    op=("Haz las cuatro pruebas de la ficha 9 en tu zona, cerca de una pared, sin forzar y con respiración calma. Anota para cada una cómo se siente el equilibrio y el peso. Después elige una de estas intenciones: «aguantar» (peso firme) o «flotar» (peso liviano) y escribe qué base, qué altura del centro de gravedad y qué movimiento usarías.",
        "Prueba 1: oscilo mucho. Prueba 2: oscilo poco. Prueba 3: abajo me siento pesado y estable. Prueba 4: con brazos arriba me siento más liviano e inestable. Intención «aguantar»: base ancha, rodillas flexionadas, bajar en 4 tiempos empujando el suelo, sin caer.",
        ["anota hechos del equilibrio y del peso en cada prueba", "relaciona base y centro de gravedad con la estabilidad", "elige una intención y la traduce en decisiones seguras"],
        ["hoja con cuatro anotaciones y las decisiones para la intención elegida"],
        ["dejarse caer en vez de ceder con control", "forzar la flexión de rodillas", "hacer las pruebas lejos de un apoyo"],
        "Pregunta: «¿qué cambió entre una prueba y otra?». Si cambió más de una cosa, pídele que repita cambiando solo una."),
    reinforce="Escribe tres posturas distintas (por ejemplo, de pie con pies juntos, con pies separados y con rodillas flexionadas) y ordénalas de menos a más estable según base y centro de gravedad.",
    extend="Explica por qué un movimiento que parece «muy pesado» puede ser seguro y otro «muy liviano» puede ser inseguro, y da una regla para elegir.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 10 (ocho acciones de movimiento de ejemplo, inventadas; todos los objetos son imaginarios). Cada acción combina tres factores. "
     "Espacio: directo (camino recto hacia un punto) o indirecto (camino ondulado que se abre). "
     "Tiempo: sostenido (se prolonga) o súbito (breve y repentino). "
     "Peso: firme (se siente la fuerza) o liviano (se siente ligereza). "
     "Un cuarto factor, el flujo, puede ser libre (sigue y sería difícil detenerlo de golpe) o contenido (se puede detener en cualquier instante). "
     "Acción 1, empujar una pared: directo, sostenido, firme. Acción 2, deslizar la mano sobre una mesa: directo, sostenido, liviano. "
     "Acción 3, marcar un punto en el aire con un toque seco: directo, súbito, firme. Acción 4, tocar una burbuja sin romperla: directo, súbito, liviano. "
     "Acción 5, estrujar una toalla: indirecto, sostenido, firme. Acción 6, flotar como una pluma: indirecto, sostenido, liviano. "
     "Acción 7, sacudir una cuerda con fuerza: indirecto, súbito, firme. Acción 8, sacudir unas gotas de las manos: indirecto, súbito, liviano.")
build(
    O3, 2, F,
    use="Aprenderé a describir un movimiento con cuatro factores (espacio, tiempo, peso y flujo), a combinarlos de forma ordenada y a predecir qué calidad de movimiento resulta.",
    prior=["Sé que el espacio, el tiempo y la energía cambian lo que comunica un gesto.", "Sé describir el peso como firme o liviano.", "Sé contar combinaciones multiplicando opciones."],
    explain=[
        "Un movimiento se puede describir con cuatro factores. El espacio puede ser directo, si sigue un camino recto hacia un punto, o indirecto, si sigue un camino ondulado que se abre. El tiempo puede ser sostenido, si se prolonga, o súbito, si es breve y repentino. El peso puede ser firme, si se siente la fuerza, o liviano, si se siente ligereza. El flujo puede ser libre o contenido.",
        "Cuando cada factor tiene dos opciones, 2 × 2 × 2 = 8 combinaciones posibles para espacio, tiempo y peso; si se suma el flujo, hay 2 × 2 × 2 × 2 = 16. Cada combinación da una calidad distinta: directo, sostenido y firme se siente como empujar una pared; indirecto, sostenido y liviano, como flotar. Son ejemplos para practicar, no reglas rígidas: dependen del contexto y de la intención.",
        "Para investigar, se cambia un factor por vez y se anota el efecto. Las acciones se hacen en el aire, con objetos imaginarios, sin lanzar nada ni forzar el cuerpo: una acción firme es controlada, no violenta. Si algo duele o marea, se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("espacio directo", "camino recto hacia un punto"), ("espacio indirecto", "camino ondulado que se abre en varias direcciones"), ("tiempo sostenido", "movimiento que se prolonga"), ("tiempo súbito", "movimiento breve y repentino"), ("flujo libre", "movimiento que sigue y cuesta detener de golpe")],
    worked=[
        ("Describir una acción con los factores", "Describe «deslizar la mano sobre una mesa» con espacio, tiempo y peso.", ["Se mueve en línea recta sobre la mesa: espacio directo.", "Dura un buen rato y es suave: tiempo sostenido y peso liviano."], "Directo, sostenido y liviano"),
        ("Contar combinaciones con un factor fijo", "Si el peso queda fijo en «liviano», ¿cuántas combinaciones hay de espacio y tiempo, con dos opciones cada uno?", ["El peso fijo no multiplica.", "Se multiplican espacio y tiempo: 2 × 2 = 4."], "4 combinaciones"),
    ],
    mistakes=[("Creer que «sostenido» significa lo mismo que «lento» en todos los casos.", "Sostenido significa que el movimiento se prolonga; puede ser suave o muy firme.", "Describe por separado el tiempo (se prolonga o es breve) y el peso (firme o liviano)."),
              ("Hacer una acción firme con tensión y violencia.", "Firme es sentir la fuerza con control, no golpear ni forzar el cuerpo.", "Usa la fuerza justa, a tu rango, y detente si algo duele.")],
    T=[
        ("abc", "{F} ¿Qué factor distingue la acción 1 de la acción 2?", "El peso: firme en la 1 y liviano en la 2", "El tiempo: sostenido en la 1 y súbito en la 2", "El espacio: directo en la 1 e indirecto en la 2", "Ambas son directas y sostenidas; solo cambia el peso."),
        ("abc", "En Expresión corporal: ¿qué significa que un movimiento sea indirecto?", "Sigue un camino ondulado que se abre en varias direcciones", "Se hace muy despacio y se prolonga en el tiempo, sin cortes", "Se hace con poca fuerza y se siente muy ligero, como una pluma", "Indirecto es un tipo de espacio; prolongarse es tiempo y ligereza es peso."),
        ("abc", "{F} ¿Cuál acción combina espacio directo, tiempo súbito y peso liviano?", "La acción 4, tocar una burbuja sin romperla", "La acción 3, marcar un punto con un toque seco", "La acción 8, sacudir unas gotas de las manos", "La 4 es directa, súbita y liviana; la 3 es firme y la 8 es indirecta."),
        ("=", "{F} Si se suman los cuatro factores (espacio, tiempo, peso y flujo) con dos opciones cada uno, ¿cuántas combinaciones hay?", "2*2*2*2", "Cada factor tiene dos opciones y se multiplican las cuatro dimensiones.", ""),
        ("abc", "{F} ¿Qué acción es indirecta, sostenida y liviana?", "La acción 6, flotar como una pluma", "La acción 2, deslizar la mano sobre una mesa", "La acción 5, estrujar una toalla", "Solo la 6 cumple indirecta, sostenida y liviana a la vez."),
        ("abc", "{F} Se quiere comunicar «urgencia fuerte». ¿Qué combinación de espacio, tiempo y peso es más coherente?", "Directo, súbito y firme, como la acción 3", "Indirecto, sostenido y liviano, como la acción 6", "Directo, sostenido y liviano, como la acción 2", "Un camino recto, repentino y con fuerza comunica urgencia."),
        ("abc", "{F} ¿Qué acción cambiaría solo el peso respecto de la acción 7, sacudir una cuerda con fuerza?", "La acción 8", "La acción 3", "La acción 5", "La 8 es indirecta y súbita como la 7, pero liviana; la 3 cambia el espacio y la 5 cambia el tiempo."),
        ("abc", "{F} Las acciones 1 y 5 son ambas firmes y sostenidas. ¿Qué las diferencia?", "El espacio: la 5 es indirecta, la 1 directa", "El peso: la 5 es liviana y la 1 es firme en todo momento", "El tiempo: la 5 es súbita y la 1 es sostenida de principio a fin", "Solo cambia el espacio: empujar una pared es directo y estrujar una toalla es indirecto."),
        ("abc", "{F} ¿Qué dos acciones se parecen en espacio y peso, pero difieren en el tiempo?", "Las acciones 1 y 3", "Las acciones 1 y 6", "Las acciones 2 y 7", "La 1 y la 3 son directas y firmes; una es sostenida y la otra súbita."),
        ("abc", "Una persona hace «deslizar la mano sobre una mesa» con mucha tensión en el brazo y se cansa. ¿Qué indica?", "Que usó más fuerza de la necesaria: la acción pide peso liviano", "Que la acción es muy difícil y siempre conviene reemplazarla por la 1", "Que debe hacerla más rápido para que el cansancio pase antes", "Una acción liviana se hace con la fuerza justa; la tensión extra es ineficiente."),
        ("abc", "{F} Se quiere averiguar el efecto del peso sin cambiar nada más. ¿Qué par de acciones sirve?", "Las acciones 5 y 6", "Las acciones 3 y 6", "Las acciones 1 y 8", "La 5 y la 6 son indirectas y sostenidas, y solo se diferencian en el peso."),
        ("abc", "{F} ¿Cuántos factores cambian entre la acción 2 y la acción 3?", "Dos factores: tiempo y peso", "Un factor: el tiempo", "Tres factores: espacio, tiempo y peso", "La 2 es directa, sostenida y liviana; la 3 es directa, súbita y firme."),
        ("=", "{F} Un grupo ensaya cada una de las 16 combinaciones de los cuatro factores durante 15 segundos, con 5 segundos de pausa entre combinaciones (15 pausas). ¿Cuántos segundos dura el ensayo?", "16*15+15*5", "Son 16 ensayos de 15 segundos y 15 pausas de 5 segundos entre ellos.", " segundos"),
    ],
    ctx=("abc", "En un trabajo sobre «tormenta», un grupo usa la acción 7 (sacudir una cuerda con fuerza) en el momento más intenso y la acción 6 (flotar como una pluma) en la calma posterior. ¿Qué cambia entre ambas?", "El tiempo y el peso; el espacio sigue igual", "Solo el peso, porque ambas son sostenidas e indirectas", "El espacio y el tiempo, porque la 6 es recta y breve", "La 7 es súbita y firme y la 6 es sostenida y liviana; ambas son indirectas."),
    sc=[
        ("En Expresión corporal: ¿qué cuatro factores describen un movimiento en esta clase?", "Espacio, tiempo, peso y flujo", "Esos cuatro factores permiten describir y comparar movimientos."),
        ("¿Qué significa tiempo súbito?", "Un movimiento breve y repentino", "Súbito se opone a sostenido, que se prolonga."),
        ("¿Cómo se investiga el efecto de un factor?", "Cambiando un solo factor y anotando el efecto", "Con un solo cambio se sabe qué produjo el efecto."),
    ],
    op=("Elige tres acciones de la ficha 10 (por ejemplo la 1, la 6 y la 8) y hazlas en tu zona, sin forzar y con objetos imaginarios. Para cada una describe espacio, tiempo y peso, y anota qué podría comunicar. Luego cambia un solo factor de una acción y anota qué cambia en lo que comunica.",
        "Acción 6, flotar como una pluma: indirecto, sostenido, liviano; comunica calma. Acción 8, sacudir gotas: indirecto, súbito, liviano; comunica inquietud. Cambié el tiempo de la acción 6 (de sostenido a súbito) y se parece a la 8: comunica apuro en vez de calma.",
        ["describe espacio, tiempo y peso de cada acción", "cambia solo un factor en la comparación", "relaciona el cambio con lo que comunica"],
        ["hoja con tres acciones descritas y una comparación de un factor cambiado"],
        ["confundir sostenido con lento siempre", "cambiar varios factores a la vez", "usar fuerza excesiva en una acción firme"],
        "Pregunta: «¿qué factor cambiaste y qué cambió en lo que comunica?». Si cambió dos, pídele que repita con uno."),
    reinforce="Inventa una acción cotidiana (por ejemplo, abrir una ventana) y descríbela con espacio, tiempo y peso. Luego cambia un factor y escribe cómo cambiaría su efecto.",
    extend="Explica por qué las ocho combinaciones de espacio, tiempo y peso no son reglas fijas y cómo el contexto puede cambiar la lectura de una acción.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 11 (frases de acciones de ejemplo, inventadas), con las ocho acciones de la clase anterior. Duración de cada acción: acciones 1 y 2, 4 tiempos; 3 y 4, 2 tiempos; 5, 4 tiempos; 6, 6 tiempos; 7 y 8, 2 tiempos. "
     "Factores: acción 1, directo-sostenido-firme; 2, directo-sostenido-liviano; 3, directo-súbito-firme; 4, directo-súbito-liviano; 5, indirecto-sostenido-firme; 6, indirecto-sostenido-liviano; 7, indirecto-súbito-firme; 8, indirecto-súbito-liviano. "
     "Transición suave: entre dos acciones seguidas cambia un solo factor. Contraste: cambian dos o tres. "
     "Después de cada acción súbita se agrega 1 tiempo de recuperación para frenar con control. "
     "Frase A: 7, 8, 4, 2, 6. Frase B: 1, 4, 5, 8.")
build(
    O3, 3, F,
    use="Aprenderé a componer una frase con acciones de movimiento eligiendo transiciones suaves y contrastes, a contar su duración con recuperaciones y a prever la inercia al frenar.",
    prior=["Sé describir un movimiento con espacio, tiempo, peso y flujo.", "Sé sumar tiempos de una frase.", "Sé que frenar con control forma parte de moverse con seguridad."],
    explain=[
        "Al componer una frase de acciones se decide cómo se pasa de una a otra. Una transición suave cambia un solo factor entre acciones seguidas: por ejemplo, de directo a indirecto manteniendo igual el tiempo y el peso. Un contraste cambia dos o tres factores y se nota como un quiebre. Una frase con solo transiciones suaves fluye; una con contrastes sorprende. Conviene decidir dónde se quiere cada efecto.",
        "La inercia es la tendencia de un cuerpo en movimiento a seguir moviéndose. En el cuerpo, un movimiento súbito y firme no se detiene de golpe: necesita un tiempo de recuperación para frenar con control. Esa recuperación se cuenta en la duración de la frase. Además, al empujar el suelo con el pie, el suelo empuja de vuelta; esa reacción ayuda a frenar y a cambiar de dirección con seguridad.",
        "Para calcular la duración se suman los tiempos de cada acción y las recuperaciones. Se compone y ensaya con seguridad: frena con control, evita giros bruscos y mantiene una zona libre alrededor. Si frenas con dificultad o sientes mareo, baja la velocidad y avisa a una persona adulta.",
    ],
    vocab=[("transición suave", "paso entre acciones en que cambia un solo factor"), ("contraste", "paso entre acciones en que cambian dos o tres factores"), ("inercia", "tendencia del cuerpo en movimiento a seguir moviéndose"), ("recuperación", "tiempo extra para frenar con control después de una acción súbita"), ("reacción del suelo", "empuje que el suelo devuelve al empujarlo con el pie")],
    worked=[
        ("Contar factores que cambian", "Una frase pasa de la acción 1 (directo-sostenido-firme) a la acción 6 (indirecto-sostenido-liviano). ¿Es transición suave o contraste?", ["Se comparan factor por factor: el espacio cambia y el peso cambia.", "El tiempo es el mismo en ambas: sostenido."], "Contraste: cambian dos factores"),
        ("Calcular una duración con recuperación", "Una frase tiene una acción súbita de 2 tiempos, una sostenida de 5 tiempos y otra súbita de 3 tiempos. Cada súbita añade 1 tiempo de recuperación. ¿Cuántos tiempos dura?", ["Se suman las tres acciones: 2 + 5 + 3 = 10.", "Se agregan 2 recuperaciones, una por cada súbita: 10 + 2 = 12."], "12 tiempos"),
    ],
    mistakes=[("No contar los tiempos de recuperación después de una acción súbita.", "Frenar con control lleva tiempo, y sin él la frase se acorta en el papel pero no en el cuerpo.", "Suma 1 tiempo de recuperación después de cada acción súbita."),
              ("Frenar de golpe un movimiento súbito y firme.", "La inercia hace que el cuerpo siga y un freno brusco puede causar una molestia o una caída.", "Baja la velocidad y frena con control durante la recuperación.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es una transición suave entre dos acciones?", "Un paso en que cambia un solo factor", "Un paso en que cambian los tres factores a la vez", "Un paso que se hace siempre con peso liviano", "La transición suave cambia un solo factor; los tres a la vez serían un contraste."),
        ("abc", "{F} ¿Qué factor cambia entre las acciones 7 y 8?", "El peso, de firme a liviano", "El espacio, de indirecto a directo", "El tiempo, de súbito a sostenido", "Ambas son indirectas y súbitas; la 7 es firme y la 8 es liviana."),
        ("abc", "En Expresión corporal: ¿qué es la inercia?", "La tendencia a seguir moviéndose", "La fuerza que empuja el cuerpo hacia el suelo siempre", "La energía que se pierde cuando se baja el peso", "La inercia es la tendencia a seguir en movimiento; la fuerza hacia el suelo es la gravedad."),
        ("=", "{F} ¿Cuántos tiempos dura la frase A, sin contar recuperaciones?", "2+2+2+4+6", "Se suman las acciones 7, 8, 4 (2 tiempos cada una), 2 (4 tiempos) y 6 (6 tiempos).", " tiempos"),
        ("=", "{F} ¿Cuántos tiempos dura la frase A con las recuperaciones de las acciones súbitas (7, 8 y 4)?", "2+2+2+4+6+3", "A los 16 tiempos de las acciones se suma 1 tiempo de recuperación por cada una de las 3 acciones súbitas.", " tiempos"),
        ("abc", "{F} ¿Qué tipo de transición hay entre las acciones 8 y 4 de la frase A?", "Suave, porque solo cambia el espacio", "Contraste, porque cambian espacio y tiempo", "Contraste, porque cambian espacio y peso", "La 8 es indirecta, súbita y liviana; la 4 es directa, súbita y liviana: cambia solo el espacio."),
        ("abc", "{F} ¿Qué tipo de transición hay entre las acciones 1 y 4 de la frase B?", "Contraste: cambian tiempo y peso", "Suave, porque ambas son directas y firmes", "Suave, porque solo cambia el tiempo de ambas", "La 1 es sostenida y firme y la 4 es súbita y liviana: cambian dos factores."),
        ("abc", "{F} En la frase B, ¿cuántos factores cambian entre la acción 4 y la acción 5?", "Tres factores", "Solo dos factores", "Solo un factor", "La 4 es directa, súbita y liviana; la 5 es indirecta, sostenida y firme: cambian los tres."),
        ("abc", "Un estudiante hace una acción súbita y firme y trata de detenerse en seco, sin recuperación. ¿Qué es lo más probable?", "Que el cuerpo siga un poco más por inercia", "Que la acción dure menos tiempo y no pase nada", "Que la reacción del suelo se anule por completo", "La inercia hace que el cuerpo siga; sin recuperación se pierde control y aumenta el riesgo."),
        ("abc", "{F} Se quiere una frase con puras transiciones suaves que parta en la acción 7. ¿Qué secuencia lo cumple?", "7, 8, 4", "7, 4, 1", "7, 2, 8", "7→8 cambia el peso y 8→4 el espacio; en las otras secuencias cambian dos o tres factores."),
        ("abc", "Alguien dice: «una frase con puros contrastes siempre es mejor porque sorprende». ¿Qué respuesta es más sólida?", "Depende de la intención: sin transiciones suaves no hay fluidez", "Tiene razón, porque la sorpresa es lo que más atrae a quien mira", "Tiene razón, salvo cuando la frase dura menos de diez tiempos", "Los contrastes y las transiciones suaves cumplen funciones distintas y se eligen por intención."),
        ("abc", "{F} Se quiere una frase de 4 acciones que no pase de 14 tiempos con recuperaciones y que parta con la acción 7. ¿Cuál cumple?", "7, 8, 4, 2", "7, 8, 4, 6", "7, 5, 6, 2", "7, 8, 4, 2 suma 10 tiempos más 3 recuperaciones, 13 en total; con la acción 6 serían 15 y 7, 5, 6, 2 llega a 17."),
        ("abc", "{F} Se quiere frenar con seguridad después de la acción 3 (súbita y firme). ¿Qué decisión es más segura?", "Sumar 1 tiempo de recuperación y bajar la velocidad", "Girar con rapidez para aprovechar el impulso de la acción 3", "Pasar de inmediato a otra acción súbita sin pausa alguna", "Frenar con control usa la recuperación; girar rápido o encadenar súbitas aumenta el riesgo."),
    ],
    ctx=("abc", "Una frase quiere pasar de «tormenta» (acciones 7 y 3) a «calma» (acciones 6 y 2) sin quiebres bruscos. ¿Qué decisión es más coherente?", "Usar acciones intermedias con transiciones suaves", "Saltar directo de la acción 3 a la 6 y dejar el cambio como sorpresa", "Mantener las acciones súbitas hasta el final y luego quedarse quieto", "Las transiciones suaves y la recuperación llevan de una a otra con control."),
    sc=[
        ("En Expresión corporal: ¿qué es un contraste entre dos acciones?", "Un paso en que cambian dos o tres factores", "El contraste se nota como un quiebre en la frase."),
        ("¿Qué se suma después de cada acción súbita?", "1 tiempo de recuperación para frenar con control", "La recuperación evita frenar de golpe por la inercia."),
        ("¿Por qué no se frena en seco un movimiento súbito y firme?", "Porque la inercia lo hace seguir y se pierde el control", "Frenar con control protege al cuerpo."),
    ],
    op=("Compón una frase de 4 o 5 acciones de la ficha 11 que parta de «tormenta» y termine en «calma». Escribe la partitura, marca cada paso como transición suave o contraste, calcula su duración con las recuperaciones de las acciones súbitas y ensáyala en tu zona sin forzar.",
        "Frase: 7, 8, 4, 2, 6. Pasos: 7→8 suave (peso); 8→4 suave (espacio); 4→2 suave (tiempo); 2→6 suave (espacio). Duración: 2+2+2+4+6 = 16 tiempos más 3 recuperaciones = 19 tiempos. Terminé en la 6, flotar, para cerrar en calma.",
        ["escribe la partitura y marca cada transición", "calcula la duración con las recuperaciones", "frena con control y respeta su rango"],
        ["partitura con transiciones marcadas y cálculo de la duración total"],
        ["no contar las recuperaciones", "frenar de golpe", "marcar mal los factores que cambian"],
        "Pregunta: «¿cuántos factores cambian en cada paso y cuántas recuperaciones sumaste?». Si no sumó recuperaciones, pídele que cuente las acciones súbitas."),
    reinforce="Elige dos acciones de la ficha 11 y escribe una transición suave y un contraste entre acciones distintas, indicando qué factores cambian.",
    extend="Explica cómo cambiaría la duración y la seguridad de tu frase si todas las acciones fueran súbitas y por qué conviene intercalar acciones sostenidas.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 12 (propósitos, contextos y reglas de seguridad de ejemplo, inventados). Propósitos con combinaciones sugeridas (tendencias, no reglas): «calma»: sostenido, liviano, flujo libre; «determinación»: directo, firme, flujo contenido; «sorpresa»: súbito, liviano, indirecto. "
     "Contexto 1: sala con piso liso y seco, de 5 m por 4 m. Contexto 2: patio con pasto irregular y desnivel. Contexto 3: pasillo de 2 m de ancho, con público de pie a un lado. "
     "Objeto: un pañuelo liviano de tela, sostenido con la mano, nunca atado al cuerpo ni al cuello. "
     "Reglas de seguridad: en piso liso, pasos cortos y base ancha en los giros; en pasto irregular, sin giros rápidos ni saltos y con la base ancha; en un pasillo, sin desplazamientos largos. Cada persona necesita una zona de 2 m por 2 m.")
build(
    O3, 4, F,
    use="Aprenderé a traducir un propósito en factores de movimiento y a adaptar mis decisiones a las fuerzas externas del contexto (suelo, aire, espacio y objetos) manteniendo la seguridad y la intención.",
    prior=["Sé describir un movimiento con cuatro factores.", "Sé que la base ancha da estabilidad.", "Sé que cada persona necesita una zona libre."],
    explain=[
        "Un propósito se traduce en factores de movimiento: «calma» tiende a ser sostenido, liviano y con flujo libre; «determinación» tiende a ser directo y firme, con flujo contenido; «sorpresa» tiende a ser súbito, liviano e indirecto. Son tendencias para empezar a probar, no reglas. Se prueba, se observa y se ajusta hasta que la intención se entienda.",
        "El contexto trae fuerzas externas que cambian lo que es posible y seguro. El suelo puede ser liso, irregular o desnivelado: un piso liso pide pasos cortos y base ancha en los giros; un pasto irregular pide evitar giros rápidos y saltos. El aire frena o mueve objetos livianos, como un pañuelo. El espacio disponible fija cuántas personas caben a la vez y cuánto se puede desplazar cada una.",
        "Adaptar es cambiar cómo se hace sin cambiar lo que se quiere comunicar. Si el contexto no permite una acción de forma segura, se reemplaza por otra con los mismos factores o se simplifica. Los objetos son livianos, se sostienen con la mano y nunca se atan al cuerpo. Si algo resbala, duele o marea, se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("propósito", "lo que se quiere comunicar con el movimiento"), ("contexto", "lugar, suelo, espacio y público donde se muestra el movimiento"), ("superficie", "tipo de suelo donde se apoya el cuerpo"), ("resistencia del aire", "fuerza del aire que frena o mueve un objeto liviano"), ("adaptar", "cambiar cómo se hace una acción sin cambiar lo que se quiere comunicar")],
    worked=[
        ("Traducir un propósito en factores", "Quieres comunicar «sorpresa» con el pañuelo. ¿Qué factores eliges y cómo se vería?", ["Según la ficha, sorpresa es súbito, liviano e indirecto.", "Un ejemplo es soltar el pañuelo en el aire con un movimiento breve y recoger la tela con la mano enseguida, sin lanzarlo a alguien."], "Súbito, liviano e indirecto, con movimientos breves y ondulados de la tela"),
        ("Contar personas en un espacio", "Un espacio libre de 6 m por 4 m y zonas de 2 m por 2 m. ¿Cuántas personas trabajan a la vez?", ["El área es 6 × 4 = 24 metros cuadrados.", "Cada zona usa 4 metros cuadrados y 24 ÷ 4 = 6."], "6 personas"),
    ],
    mistakes=[("Hacer la misma acción igual en un piso liso y en uno irregular.", "La superficie cambia el riesgo: lo que es seguro en una sala puede no serlo en un patio.", "Revisa el suelo y adapta los pasos, la base y el tamaño de los giros."),
              ("Atar el pañuelo a la muñeca o al cuello para que «no se pierda».", "Un objeto atado puede enredarse y causar una caída o una molestia.", "Sostén el pañuelo con la mano y suéltalo con cuidado, sin lanzarlo.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es adaptar una acción a un contexto?", "Cambiar cómo se hace sin cambiar lo que se quiere comunicar", "Cambiar la intención de la acción hasta que se vea más fácil", "Mantener la acción igual sin importar el suelo ni el espacio", "Adaptar cambia la forma de hacer, no la intención."),
        ("abc", "{F} ¿Qué factores sugiere la ficha para el propósito «calma»?", "Sostenido, liviano y flujo libre", "Directo, firme y flujo contenido", "Súbito, liviano e indirecto", "La ficha asocia calma con sostenido, liviano y flujo libre."),
        ("abc", "{F} ¿Qué regla de seguridad corresponde al contexto 1, de piso liso y seco?", "Pasos cortos y base ancha en los giros", "Giros rápidos para aprovechar lo liso del piso", "Desplazamientos largos con los pies juntos", "En un piso liso se acortan los pasos y se ensancha la base para no resbalar."),
        ("=", "{F} En el contexto 1 (5 m por 4 m), ¿cuántas personas pueden trabajar a la vez, cada una en su zona de 2 m por 2 m?", "(5//2)*(4//2)", "A lo largo de 5 m caben 2 zonas de 2 m (sobra 1 m) y a lo ancho de 4 m caben 2: 2 × 2 = 4.", " personas"),
        ("abc", "{F} ¿Qué decisión es más segura en el contexto 2, de pasto irregular?", "Pies bien separados y sin giros rápidos ni saltos", "Aprovechar el desnivel para dar un salto con giro", "Hacer giros rápidos con los pies juntos para tener más impulso", "En el pasto irregular se amplía la base y se evitan giros rápidos y saltos."),
        ("abc", "{F} ¿Qué se puede hacer con el pañuelo?", "Sostenerlo con la mano, sin atarlo", "Atarlo a la muñeca para que no se pierda", "Lanzarlo a otra persona con fuerza", "La ficha pide sostenerlo con la mano, nunca atarlo ni lanzarlo."),
        ("abc", "{F} En el contexto 3 (pasillo de 2 m de ancho, con público a un lado), ¿qué decisión es más coherente?", "Hacer gestos en el lugar, sin desplazamientos largos", "Recorrer todo el pasillo con pasos grandes y giros", "Ampliar el movimiento hacia el lado donde está el público", "En un pasillo estrecho se trabaja sin desplazamientos largos."),
        ("abc", "{F} Quieres comunicar «determinación» en el contexto 1. ¿Qué plan es más coherente y seguro?", "Movimientos directos y firmes, con base ancha y flujo contenido", "Movimientos súbitos e indirectos con pasos largos y giros rápidos", "Movimientos sostenidos y livianos que se prolongan con flujo libre", "Determinación es directa, firme y contenida; en un piso liso se usa base ancha."),
        ("abc", "Una persona nota que su zapato resbala en el piso liso. ¿Qué corresponde?", "Acortar los pasos y ensanchar la base", "Acelerar los pasos para que el resbalón se note menos", "Girar más rápido para mantener el impulso de la frase", "Si se resbala, se reducen los pasos y se amplía la base, con aviso a una persona adulta."),
        ("abc", "Alguien dice: «adaptar la frase al contexto cambia lo que quiero decir». ¿Qué respuesta es más sólida?", "Se adapta cómo se hace; la intención se mantiene", "Tiene razón, por eso la frase debe ser igual en todos los lugares", "Tiene razón solo cuando el público es mayor de diez personas", "Adaptar cambia las decisiones de realización, no el propósito."),
        ("abc", "{F} Dos estudiantes prueban «calma» con el pañuelo: una lo mueve rápido y con fuerza, y otra lo desliza despacio con flujo libre. ¿Cuál comunica mejor la calma según la ficha?", "La que lo desliza despacio con flujo libre", "La que lo mueve rápido porque el pañuelo se ve más", "Ambas, porque en el movimiento no hay propósitos incorrectos", "Calma es sostenida, liviana y con flujo libre; rápido y fuerte comunica otra cosa."),
        ("abc", "{F} Quieres comunicar «sorpresa» en el contexto 2, de pasto irregular. ¿Qué decisión conserva la intención de forma segura?", "Movimientos súbitos y breves, sin giros, con pies apoyados", "Una serie de giros rápidos con saltos para que se note la sorpresa", "Movimientos lentos y suaves para evitar cualquier riesgo del suelo", "Se conserva súbito, liviano e indirecto con movimientos breves y base firme."),
        ("=", "{F} En el contexto 3, cada persona tiene su zona de 2 m por 2 m y el pasillo es de 2 m de ancho y 8 m de largo, con una sola fila de zonas. ¿Cuántas personas caben a la vez?", "8//2", "Con un ancho de 2 m cabe una fila, y en 8 m de largo entran 8 ÷ 2 zonas.", " personas"),
    ],
    ctx=("abc", "Un grupo quiere mostrar «calma» con un pañuelo en un patio de pasto irregular. Quieren flujo libre y gestos amplios con giros. ¿Qué ajuste mantiene la intención y es más seguro?", "Gestos amplios en el lugar, con pies separados y sin giros", "Mantener los giros amplios y agregar saltos pequeños para dar ligereza", "Cambiar el propósito a «determinación», que es más fácil de hacer en ese suelo", "Se conserva la calma con el pañuelo y se reemplazan giros por gestos en el lugar."),
    sc=[
        ("En Expresión corporal: ¿qué factores sugiere la ficha para «determinación»?", "Directo, firme y flujo contenido", "Son tendencias para probar, no reglas fijas."),
        ("¿Qué se hace si el contexto no permite una acción de forma segura?", "Se reemplaza o se simplifica la acción, manteniendo la intención", "La seguridad va antes que hacer la acción original."),
        ("¿Cómo se usa un pañuelo en una práctica?", "Sostenido con la mano, nunca atado al cuerpo ni lanzado", "Un objeto atado puede enredarse y causar un accidente."),
    ],
    op=("Elige un propósito de la ficha 12 («calma», «determinación» o «sorpresa») y un contexto (1, 2 o 3). Escribe los factores que usarás (espacio, tiempo, peso y flujo), cómo adaptas pasos, base y desplazamientos a las fuerzas externas del lugar, y qué acción reemplazarías por seguridad. Ensaya en tu zona sin forzar, con o sin pañuelo.",
        "Propósito «calma», contexto 1 (piso liso). Factores: sostenido, liviano, flujo libre. Pasos cortos, base ancha en los giros, sin desplazamientos largos. Reemplazo un giro rápido por un giro lento de 8 tiempos. El pañuelo lo sostengo con la mano y lo muevo despacio.",
        ["traduce el propósito en factores", "adapta las decisiones al suelo y al espacio", "propone un reemplazo seguro y mantiene la intención"],
        ["hoja con propósito, contexto, factores, adaptaciones y reemplazo"],
        ["hacer la acción igual sin mirar el suelo", "cambiar la intención al adaptar", "atar el pañuelo al cuerpo"],
        "Pregunta: «¿qué adaptaste del suelo o del espacio y qué mantuviste de tu intención?». Si cambió la intención, pídele que vuelva al propósito."),
    reinforce="Elige dos contextos de la ficha 12 y escribe una regla de seguridad distinta para cada uno, con la razón.",
    extend="Explica cómo cambiarían tus decisiones si el pañuelo fuera más pesado y por qué conviene seguir usando solo objetos livianos.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 13 (bitácora de ensayos de ejemplo, inventada). Intención: «saludo amable». Acción base: acción 1 de la ficha 10 (directo, sostenido, firme) adaptada a un gesto de saludo. "
     "Ensayo 1: acción base; cinco personas leen «decidido»; esfuerzo anotado: 3 de 5. "
     "Ensayo 2: se cambia el peso a liviano; cuatro de cinco leen «amable»; esfuerzo: 2 de 5. "
     "Ensayo 3: sobre el ensayo 2 se cambia el espacio a indirecto; tres de cinco leen «amable» y dos leen «confuso»; esfuerzo: 2 de 5. "
     "Ensayo 4: sobre el ensayo 2 se cambia el tiempo a súbito; dos de cinco leen «amable» y tres leen «apurado»; esfuerzo: 3 de 5. "
     "Escala de esfuerzo de 1 (muy suave) a 5 (muy intenso); se busca mantenerse entre 1 y 3.")
build(
    O3, 5, F,
    use="Aprenderé a evaluar y revisar mi proceso con una bitácora: relacionar cada cambio de factor con su efecto, calcular qué porcentaje entendió la intención, decidir qué conservar y planear el siguiente cambio.",
    prior=["Sé cambiar un factor por vez.", "Sé describir un movimiento con cuatro factores.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Evaluar el proceso es mirar con evidencia cómo cambió lo que comunica el movimiento al cambiar un factor. La bitácora anota, en cada ensayo, qué cambió, cuántas personas leyeron la intención y cuánto esfuerzo costó. Con esos datos se calcula, por ejemplo, el porcentaje de lectores que entendió la intención: si 4 de 5 lo entendieron, es 4 × 100 ÷ 5 = 80 %.",
        "Para decidir qué conservar se comparan ensayos que difieren en un solo factor: si el ensayo 2 cambia solo el peso y mejora la lectura, el peso liviano ayuda a la intención. Se cuida también el esfuerzo: un cambio que mejora la lectura pero sube el esfuerzo sobre 3 puede ser poco sostenible. Con cinco personas es una muestra pequeña: sirve para decidir el próximo ensayo, no para afirmar una regla general.",
        "El siguiente paso es un solo cambio por probar, con una predicción: «si cambio X, espero que Y». La revisión honesta anota también lo que no funcionó. Se hace con respeto: se agradece a quien lee la intención, no se discuten los cuerpos y nadie está obligado a mostrar. Si el cuerpo se cansa, duele o marea, se para y se avisa a una persona adulta.",
    ],
    vocab=[("bitácora", "registro ordenado de ensayos, cambios y efectos"), ("evidencia", "dato observable que respalda una decisión"), ("muestra pequeña", "pocos lectores: sirve para decidir un ensayo, no para afirmar una regla"), ("predicción", "lo que se espera que pase al hacer un cambio"), ("revisión", "decisión sobre qué conservar y qué cambiar después de mirar la evidencia")],
    worked=[
        ("Calcular el porcentaje de lecturas", "En un ensayo, 3 de 5 personas leyeron la intención. ¿Qué porcentaje es?", ["Se multiplica 3 por 100: 300.", "Se divide entre 5: 300 ÷ 5 = 60."], "60 %"),
        ("Atribuir un efecto a un cambio", "El ensayo A cambia solo el tiempo y la lectura baja de 4 a 2 personas de 5. ¿Qué se puede decir?", ["Como cambió un solo factor, el efecto se atribuye a él.", "Se dice con cautela, porque la muestra es pequeña."], "Probablemente el cambio de tiempo empeora la lectura; conviene repetir para confirmar"),
    ],
    mistakes=[("Concluir una regla general con solo cinco personas.", "Una muestra pequeña sirve para decidir un ensayo, pero no para afirmar una regla.", "Di «parece que» y repite el ensayo con otras personas antes de afirmar."),
              ("Ocultar en la bitácora los ensayos que salieron mal.", "Esos ensayos aportan evidencia de qué no comunica la intención.", "Anota todos los ensayos, también los que no funcionaron.")],
    T=[
        ("abc", "En Expresión corporal: ¿qué es una bitácora de ensayos?", "Un registro ordenado de ensayos, cambios y efectos", "Una lista de movimientos que ya se aprendieron de memoria", "Una pauta para ordenar las frases de la más a la menos expresiva", "La bitácora registra qué se cambió y qué efecto tuvo; no compara ni jerarquiza frases."),
        ("=", "{F} ¿Qué porcentaje de lectores entendió «amable» en el ensayo 2?", "4*100//5", "Cuatro de cinco equivale a 80 de cada 100, porque 4 × 100 ÷ 5 = 80.", " %"),
        ("abc", "{F} ¿Qué factor cambió en el ensayo 2 respecto de la acción base?", "El peso, de firme a liviano", "El espacio, de directo a indirecto", "El tiempo, de sostenido a súbito", "El ensayo 2 solo cambia el peso a liviano; los otros ensayos cambian espacio y tiempo."),
        ("abc", "{F} Entre los ensayos 2, 3 y 4, ¿cuál tuvo la lectura de «amable» más baja?", "El ensayo 4, con dos de cinco", "El ensayo 3, con tres de cinco", "El ensayo 2, con cuatro de cinco", "Entre esos tres ensayos, el 4 tuvo dos de cinco, la cifra más baja."),
        ("abc", "{F} ¿Por qué el ensayo 3 no se compara directamente con la acción base?", "Porque partió del ensayo 2 y cambió otro factor", "Porque tuvo más lectores que la acción base en la bitácora", "Porque el esfuerzo del ensayo 3 fue mayor que el de la acción base", "El ensayo 3 parte del 2: mezcla el peso liviano con el cambio de espacio."),
        ("abc", "{F} ¿Qué conclusión es prudente al comparar los ensayos 2 y 3?", "Cambiar a indirecto parece haber reducido la lectura de «amable»", "El espacio indirecto demuestra que el saludo se vuelve confuso siempre", "El ensayo 3 es mejor, porque tuvo menos esfuerzo que el ensayo 1", "Con cinco lectores se dice «parece»; no se afirma una regla general."),
        ("=", "{F} ¿Cuántas lecturas de «amable» hubo en total sumando los ensayos 2, 3 y 4?", "4+3+2", "Se suman las lecturas de «amable» de los tres ensayos: 4, 3 y 2.", " lecturas"),
        ("abc", "{F} ¿Qué ensayo combina mejor buena lectura de la intención y esfuerzo dentro del rango de 1 a 3?", "El ensayo 2: cuatro lecturas y esfuerzo 2", "El ensayo 4: dos lecturas y esfuerzo 3", "El ensayo 1: cinco lecturas de «decidido» y esfuerzo 3", "El ensayo 1 leyó «decidido», no «amable»; el 2 tiene la mejor lectura y un esfuerzo bajo."),
        ("abc", "{F} Se planea el siguiente ensayo sobre el ensayo 2. ¿Qué plan tiene una predicción clara y un solo cambio?", "Cambiar el flujo a libre; espero que la lectura de «amable» suba", "Cambiar espacio y tiempo a la vez; espero que todo mejore", "Repetir el ensayo 2 sin cambios; espero que cambie sola la lectura", "Un cambio por ensayo con una predicción permite atribuir el efecto."),
        ("abc", "Una estudiante no anota en la bitácora un ensayo en el que hubo molestia en el hombro. ¿Qué corresponde?", "Anotarlo, detenerse y avisar a una persona adulta", "Omitirlo para que la bitácora quede completa en lecturas", "Repetir el ensayo con más fuerza para ver si la molestia se va", "La molestia es un dato de seguridad: se anota, se detiene y se avisa."),
        ("abc", "Alguien dice: «con cinco lectores ya está comprobado que el peso liviano comunica amabilidad». ¿Qué respuesta es más sólida?", "Es una muestra pequeña: no basta para una regla", "Tiene razón, porque cuatro de cinco es más del 75 %", "Tiene razón, siempre que los lectores sean amigos de quien actúa", "Una muestra pequeña no basta para una regla general."),
        ("abc", "{F} Alguien anota: «el ensayo 4 salió mal, soy poco expresivo». ¿Cómo se reescribe como evidencia?", "«En el ensayo 4, dos de cinco leyeron amable y tres apurado»", "«El ensayo 4 fue el peor de todos y debería borrarse de la bitácora»", "«En el ensayo 4 me costó mucho y no sirvo para esta intención»", "La evidencia describe lo observado sin juzgar a la persona."),
        ("=", "{F} Se repite el ensayo 2 con 12 lectores y 9 leen «amable». ¿Qué porcentaje es?", "9*100//12", "Nueve de doce equivale a 75 de cada 100, porque 9 × 100 ÷ 12 = 75.", " %"),
    ],
    ctx=("abc", "Un grupo prueba tres versiones de «espera tranquila» y registra: versión 1, 2 de 5 la leen «tranquila»; versión 2, 4 de 5; versión 3, 4 de 5 pero con esfuerzo 4. Debe elegir una para ensayar con más lectores. ¿Cuál elige?", "La versión 2: buena lectura y poco esfuerzo", "La versión 3, porque su lectura es igual y exige más trabajo", "La versión 1, porque es la primera y la que menos se cambió", "La versión 2 iguala la lectura de la 3 con menos esfuerzo, que debe mantenerse entre 1 y 3."),
    sc=[
        ("En Expresión corporal: ¿para qué sirve una bitácora?", "Para relacionar cada cambio con su efecto y decidir qué conservar", "Reúne evidencia de qué cambió y qué resultó."),
        ("¿Por qué una muestra de cinco lectores no basta para afirmar una regla?", "Porque es pequeña y solo sirve para decidir el próximo ensayo", "Con pocos lectores el resultado puede deberse al azar."),
        ("¿Qué incluye un buen plan para el siguiente ensayo?", "Un solo cambio y una predicción", "Así se puede atribuir el efecto y revisar la predicción."),
    ],
    op=("Elige una intención («saludo amable», «espera tranquila» o «despedida cálida») y una acción base de la ficha 10. Haz tres ensayos cambiando un solo factor entre uno y otro y anótalos en una bitácora con: qué cambió, qué leyó una persona de confianza (si quiere ayudarte) y tu esfuerzo (1 a 5). Calcula un porcentaje, decide qué conservas y planea un solo cambio con predicción.",
        "Intención «saludo amable». Ensayo 1: acción base, la lectura fue «decidido», esfuerzo 3. Ensayo 2: peso liviano; mi persona lectora dijo «amable», esfuerzo 2. Ensayo 3: peso liviano más tiempo súbito; dijo «apurado», esfuerzo 3. Conservo el ensayo 2. Próximo cambio: flujo libre; espero que se vea más cálido.",
        ["cambia un solo factor entre ensayos y los registra", "calcula un porcentaje o conteo con sus datos", "decide qué conservar y planea un cambio con predicción"],
        ["bitácora con tres ensayos, un cálculo, una decisión y un plan"],
        ["afirmar una regla con pocos lectores", "omitir los ensayos que no funcionaron", "cambiar varios factores en un solo ensayo"],
        "Pregunta: «¿qué conservas y qué cambio con qué predicción probarás?». Si propone dos cambios, pídele que elija uno."),
    reinforce="Con los datos de la ficha 13, calcula el porcentaje de lectores que leyó «amable» en cada uno de los ensayos 2, 3 y 4.",
    extend="Explica por qué conviene repetir un ensayo con más lectores antes de afirmar que un factor produce un efecto, y cuántos cambios harías por vez.",
)
