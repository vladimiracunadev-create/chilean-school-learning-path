"""Física (electivo HC, 3.º y 4.º medio): OAC-03 (movimiento bajo una fuerza central, mecánica clásica), clases 1 a 5, y OAC-04 (física moderna y debate sobre la realidad), clases 1 a 5.
Todo en papel: sin laboratorio, sin electricidad de red ni fuentes de calor. Los datos son de ejemplo y están escritos en cada ficha."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla y papel; calculadora simple opcional. No se necesita laboratorio, instrumentos, fuentes de calor ni electricidad de red: "
             "todos los datos son de ejemplo (inventados o redondeados para practicar) y están escritos en la ficha. Las constantes que aparecen "
             "(π ≈ 3 para simplificar, g ≈ 10 m/s², c ≈ 300.000 km/s) son valores aproximados y se rotulan como tales. "
             "Nunca se hace girar objetos con cuerdas ni se prueban curvas con vehículos: los casos se resuelven por cálculo.")
build = make_build(MATERIALS)

O3 = "CN-FISI-3y4-OAC-03"
O4 = "CN-FISI-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 1 (de ejemplo; usa π ≈ 3 para simplificar). Un carrusel ficticio tiene radio 4 m y da una vuelta completa cada 12 s (período T = 12 s). "
     "Una niña de 30 kg viaja en su borde con rapidez constante.")
build(
    O3, 1, F,
    use="Aprenderé a delimitar qué es una fuerza central y cómo se describe el movimiento circular uniforme: radio, período, rapidez y dirección de la fuerza.",
    prior=["Sé que la velocidad tiene rapidez y dirección.", "Sé que una fuerza neta cambia el movimiento de un cuerpo (segunda ley de Newton).", "Sé calcular rapidez como distancia ÷ tiempo."],
    explain=[
        "Una fuerza central es una fuerza que siempre apunta hacia un punto fijo llamado centro. La gravedad de la Tierra sobre la Luna, la tensión de una cuerda en un carrusel o el roce de los neumáticos en una curva son ejemplos. Cuando una fuerza central actúa sobre un cuerpo que se mueve de lado, puede hacerlo girar en una trayectoria circular. Si la fuerza desaparece, la primera ley de Newton indica que el cuerpo sigue en línea recta tangente al círculo.",
        "En el movimiento circular uniforme (MCU) la trayectoria es un círculo y la rapidez es constante, pero la velocidad cambia porque su dirección cambia en cada instante. Un cambio de velocidad es una aceleración: la aceleración centrípeta apunta hacia el centro. Por la segunda ley de Newton, la fuerza neta sobre el cuerpo también apunta hacia el centro. Por eso, en un sistema de referencia inercial, no hace falta una fuerza «hacia afuera» para describir el movimiento.",
        "Para describir un MCU se usan el radio r (en m), el período T (tiempo de una vuelta, en s) y la frecuencia f = 1 ÷ T (vueltas por segundo, en Hz). En una vuelta el cuerpo recorre el perímetro 2πr, así que su rapidez es v = 2πr ÷ T. Para delimitar un problema se nombra el cuerpo que gira, el cuerpo que ejerce la fuerza, el centro, y las variables que se miden con sus unidades.",
    ],
    vocab=[("fuerza central", "fuerza que siempre apunta hacia un punto fijo"), ("movimiento circular uniforme", "movimiento en círculo con rapidez constante"), ("período (T)", "tiempo de una vuelta completa"), ("frecuencia (f)", "número de vueltas por segundo, f = 1 ÷ T"), ("aceleración centrípeta", "aceleración dirigida hacia el centro"), ("tangente", "recta que toca el círculo en un solo punto")],
    worked=[
        ("Rapidez en el MCU", "Un punto ficticio gira en un círculo de radio 5 m y da una vuelta cada 10 s. Con π ≈ 3, ¿cuál es su rapidez?", ["Perímetro: 2 × 3 × 5 = 30 m.", "Rapidez = distancia ÷ tiempo = 30 ÷ 10."], "3 m/s"),
        ("Qué pasa si falta la fuerza", "Un cuerpo ficticio gira sobre una mesa lisa unido a un centro por un hilo y el hilo se corta cuando el cuerpo pasa por el punto P. ¿Qué trayectoria sigue?", ["Sin fuerza neta, el cuerpo conserva su velocidad (primera ley de Newton).", "En P esa velocidad es tangente al círculo."], "Sigue en línea recta, tangente al círculo en P"),
    ],
    mistakes=[("Creer que en el MCU hay una fuerza real que empuja hacia afuera.", "La sensación de ir hacia afuera se debe a la inercia: el cuerpo tiende a seguir recto.", "Dibuja la fuerza real hacia el centro y la velocidad tangente."),
              ("Usar el diámetro en lugar del radio en 2πr.", "Se confunde la distancia al centro con el ancho del círculo.", "Mide siempre desde el centro hasta el borde.")],
    T=[
        ("abc", "¿Hacia dónde apunta una fuerza central?", "Hacia un punto fijo llamado centro", "En la dirección del movimiento", "Hacia afuera del círculo", "Por definición, una fuerza central tiene dirección hacia un punto fijo."),
        ("abc", "En un movimiento circular uniforme, ¿qué pasa con la rapidez?", "Es constante", "Aumenta en cada vuelta", "Es siempre cero", "Uniforme significa que el valor de la rapidez no cambia."),
        ("ab", "En un movimiento circular uniforme, ¿cambia el vector velocidad?", "Sí, porque cambia su dirección", "No, porque la rapidez es constante", "La velocidad incluye la dirección y esta cambia continuamente."),
        ("abc", "¿Qué ejerce la fuerza central que mantiene a la Luna girando alrededor de la Tierra?", "La gravedad de la Tierra", "El empuje del aire", "El roce con el espacio", "La atracción gravitatoria apunta hacia la Tierra, que es el centro de la órbita."),
        ("abc", "¿Cuál de estas preguntas está mejor delimitada para estudiar el carrusel?", "¿Con qué rapidez se mueve el borde si da una vuelta cada 12 s y su radio es 4 m?", "¿Es divertido el carrusel?", "¿Por qué los carruseles son redondos?", "La primera tiene sistema, variables y unidades; las otras son opiniones."),
        ("abc", "El período T es", "el tiempo que tarda en dar una vuelta completa", "el número de vueltas por hora", "la distancia de una vuelta", "El período se mide en segundos y la frecuencia es su inverso."),
        ("=", "{F} ¿Cuántos metros recorre en una vuelta el borde del carrusel? (perímetro = 2 × π × r)", "2*3*4", "El perímetro es 2 por π por el radio.", " m"),
        ("=", "{F} ¿Cuál es la rapidez del borde del carrusel, en m/s?", "2*3*4//12", "La rapidez es el perímetro dividido por el período.", " m/s"),
        ("=", "Un cuerpo da 5 vueltas en 20 s. ¿Cuántos segundos dura cada vuelta?", "20//5", "El período es el tiempo total dividido por el número de vueltas.", " s"),
        ("abc", "Un satélite ficticio gira con rapidez constante. Un estudiante dice: «como su rapidez no cambia, no hay fuerza neta sobre él». ¿Qué falla?", "Su dirección cambia continuamente y para eso hace falta una fuerza hacia el centro", "Nada: sin cambio de rapidez no hay fuerza", "La fuerza apunta en la dirección del movimiento", "Cambiar la dirección del movimiento también es acelerar y exige una fuerza neta."),
        ("abc", "{F} Se dice que la niña «sale despedida hacia afuera» por una fuerza. Si se soltara del carrusel en un punto, ¿qué haría realmente?", "Saldría en línea recta, tangente al círculo", "Saldría hacia el centro", "Seguiría moviéndose en círculo", "Al desaparecer la fuerza hacia el centro, se mueve con la velocidad que tenía, que es tangente."),
        ("=", "{F} Otra niña viaja a 2 m del centro, con el mismo período. ¿Cuál es su rapidez, en m/s?", "2*3*2//12", "Recorre un perímetro menor en el mismo tiempo.", " m/s"),
        ("abc", "{F} Las dos niñas del carrusel dan una vuelta cada 12 s. ¿Cómo se comparan sus períodos?", "Son iguales", "El de la niña del borde es mayor", "El de la niña más cercana al centro es mayor", "Ambas completan una vuelta en el mismo tiempo, aunque recorran distancias distintas."),
    ],
    ctx=("abc", "Un auto ficticio toma una curva circular con rapidez constante. ¿Qué cuerpo ejerce la fuerza central que lo mantiene en la curva?", "El suelo, mediante el roce de los neumáticos", "El motor, que empuja hacia afuera", "El aire, que lo sostiene", "Sin roce el auto seguiría recto; el roce con el suelo entrega la fuerza hacia el centro."),
    sc=[
        ("En Física: ¿cómo se calcula la rapidez en un movimiento circular uniforme?", "Perímetro 2πr dividido por el período T", "Es la distancia de una vuelta dividida por su tiempo."),
        ("¿Hacia dónde apunta la aceleración centrípeta?", "Hacia el centro del círculo", "La fuerza neta y la aceleración tienen la misma dirección."),
        ("Con π ≈ 3, ¿cuántos metros recorre un cuerpo en una vuelta de radio 5 m?", "30 m", "Se calcula 2 × 3 × 5."),
    ],
    op=("Elige un caso. Caso 1: una rueda ficticia de radio 2 m que da una vuelta cada 4 s. Caso 2: una plataforma ficticia de radio 6 m que da una vuelta cada 12 s. Con π ≈ 3, calcula la distancia de una vuelta y la rapidez; dibuja el círculo con tres puntos y marca en cada uno la dirección de la velocidad (tangente) y de la fuerza central (hacia el centro); y escribe una limitación de usar π ≈ 3.",
        "Caso 1: perímetro = 2 × 3 × 2 = 12 m; rapidez = 12 ÷ 4 = 3 m/s. En cada punto, la velocidad es tangente y la fuerza apunta al centro. Limitación: π vale un poco más que 3, y el cálculo da una rapidez algo menor que la real.",
        ["calcula perímetro y rapidez con unidades", "dibuja velocidad tangente y fuerza hacia el centro en tres puntos", "nombra una limitación de la aproximación"],
        ["hoja con el cálculo, un dibujo con flechas y una frase sobre la limitación"],
        ["dibujar la fuerza hacia afuera", "usar el diámetro como radio", "olvidar las unidades"],
        "Pregunta: «¿en qué dirección se movería el cuerpo si desapareciera la fuerza en ese punto?»."),
    reinforce="Dibuja un círculo, marca cuatro puntos y traza en cada uno una flecha tangente (velocidad) y una flecha hacia el centro (fuerza).",
    extend="Explica por qué en el MCU la rapidez es constante y aun así hay aceleración.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 2 (de ejemplo, datos de un cálculo; fuerza central F = m × v² ÷ r, con F en newtons (N), m en kg, v en m/s y r en m). "
     "Ensayo 1: m = 2 kg, v = 2 m/s, r = 4 m. Ensayo 2: m = 2 kg, v = 4 m/s, r = 4 m. Ensayo 3: m = 2 kg, v = 2 m/s, r = 8 m. Ensayo 4: m = 4 kg, v = 2 m/s, r = 4 m.")
build(
    O3, 2, F,
    use="Aprenderé a identificar y relacionar las variables de la fuerza central, a comparar ensayos cambiando una variable a la vez y a evaluar si una comparación es válida.",
    prior=["Sé que el MCU tiene aceleración dirigida al centro.", "Sé usar la segunda ley de Newton F = m × a.", "Sé multiplicar y dividir con números enteros."],
    explain=[
        "La aceleración centrípeta de un cuerpo con rapidez v en una trayectoria circular de radio r es a = v² ÷ r, y apunta hacia el centro. Aplicando la segunda ley de Newton, la fuerza central necesaria es F = m × v² ÷ r. La fuerza se mide en newton (N): 1 N es la fuerza que da una aceleración de 1 m/s² a una masa de 1 kg.",
        "La fórmula muestra cómo se relacionan las variables. Si se duplica la masa, la fuerza se duplica (es proporcional a m). Si se duplica la rapidez, la fuerza se multiplica por 4, porque v está al cuadrado. Si se duplica el radio con la misma rapidez, la fuerza se reduce a la mitad (es inversamente proporcional a r). Por eso las curvas cerradas y las rapideces altas exigen fuerzas mayores.",
        "Para comparar ensayos hay que cambiar una sola variable a la vez y mantener las otras controladas; si cambian dos al mismo tiempo, no se puede saber cuál produjo el efecto. Al evaluar una tabla de datos se revisa si las unidades están claras, si los valores se calcularon con la misma fórmula y si la comparación es justa. Una fuente sin unidades o con variables mezcladas no sirve como evidencia.",
    ],
    vocab=[("newton (N)", "unidad de fuerza: kg · m/s²"), ("variable controlada", "variable que se mantiene igual para comparar"), ("proporcional", "que crece en la misma razón que otra cantidad"), ("inversamente proporcional", "que disminuye cuando otra aumenta, en la misma razón"), ("aceleración centrípeta", "a = v² ÷ r, hacia el centro"), ("ensayo", "caso de cálculo o medición con valores definidos")],
    worked=[
        ("Calcular una fuerza", "Un cuerpo de 2 kg gira con v = 3 m/s en radio 6 m. ¿Qué fuerza central necesita?", ["Calcula v²: 3 × 3 = 9.", "F = 2 × 9 ÷ 6 = 3."], "3 N"),
        ("Cambiar una variable", "Con las demás variables iguales, el radio se triplica. ¿Qué pasa con la fuerza?", ["F es inversamente proporcional a r.", "Si r se multiplica por 3, F se divide por 3."], "La fuerza se reduce a un tercio"),
    ],
    mistakes=[("Duplicar la rapidez y creer que la fuerza solo se duplica.", "Se olvida que la rapidez está elevada al cuadrado.", "Calcula v × v antes de dividir por r."),
              ("Comparar dos ensayos que cambian dos variables a la vez.", "No se puede saber cuál variable causó el cambio.", "Elige ensayos donde cambie una sola variable.")],
    T=[
        ("abc", "En el movimiento circular uniforme, la aceleración centrípeta se calcula con", "a = v² ÷ r", "a = v × r", "a = r ÷ v", "La aceleración centrípeta crece con el cuadrado de la rapidez y disminuye con el radio."),
        ("abc", "La unidad de fuerza en el Sistema Internacional es", "el newton (N)", "el kilogramo (kg)", "el metro por segundo (m/s)", "El newton mide fuerza; el kilogramo, masa; y m/s, rapidez."),
        ("ab", "Si aumenta la masa del cuerpo y v y r no cambian, la fuerza central", "aumenta", "disminuye", "La fuerza es proporcional a la masa en F = m × v² ÷ r."),
        ("=", "{F} Calcula la fuerza central del ensayo 1 usando F = m × v² ÷ r.", "2*2*2//4", "Se multiplica la masa por v² y se divide por el radio.", " N"),
        ("abc", "{F} Comparando los ensayos 1 y 2, ¿qué variable cambió y qué pasó con la fuerza?", "Cambió v, de 2 a 4 m/s, y la fuerza se multiplicó por 4", "Cambió v y la fuerza se duplicó", "Cambió r y la fuerza se duplicó", "La fuerza pasó de 2 a 8 N: al duplicar v se multiplica por 2 al cuadrado."),
        ("abc", "{F} Comparando los ensayos 1 y 3, ¿qué variable cambió y qué pasó con la fuerza?", "Cambió r, de 4 a 8 m, y la fuerza bajó a la mitad", "Cambió m y la fuerza bajó a la mitad", "Cambió r y la fuerza se duplicó", "La fuerza pasó de 2 a 1 N porque es inversamente proporcional a r."),
        ("=", "{F} Calcula la fuerza central del ensayo 4.", "4*2*2//4", "Se usa la misma fórmula con m = 4 kg.", " N"),
        ("=", "Un cuerpo de 3 kg gira con v = 4 m/s en un radio de 8 m. ¿Cuánto vale la fuerza central?", "3*4*4//8", "Se calcula m × v² ÷ r con los datos dados.", " N"),
        ("=", "Un cuerpo gira con v = 6 m/s en un radio de 9 m. ¿Cuánto vale su aceleración centrípeta?", "6*6//9", "La aceleración centrípeta es v² ÷ r.", " m/s²"),
        ("abc", "Si se duplica la rapidez de un cuerpo con el mismo radio y la misma masa, la fuerza central", "se multiplica por 4", "se duplica", "no cambia", "La rapidez está elevada al cuadrado en la fórmula."),
        ("abc", "{F} Para saber cómo influye solo la masa en la fuerza, ¿qué ensayos conviene comparar?", "Los ensayos 1 y 4, porque solo cambia la masa", "Los ensayos 1 y 2, porque cambia la rapidez", "Los ensayos 2 y 3, porque cambian dos variables", "Para aislar una variable, las demás deben quedar iguales."),
        ("abc", "Un estudiante compara dos ensayos en que cambia a la vez la rapidez y el radio, y dice que el cambio de fuerza se debe «al radio». ¿Qué falla?", "No puede atribuir el cambio al radio, porque también cambió la rapidez", "Nada, el radio siempre es la causa", "Los ensayos deben cambiar todas las variables a la vez", "Con dos variables cambiadas no se puede separar el efecto de cada una."),
        ("Una fuerza central de 8 N actúa sobre un cuerpo de 2 kg que gira en un radio de 4 m. Con F = m × v² ÷ r, ¿cuál es su rapidez, en m/s?", "4 m/s", "Se despeja v² = F × r ÷ m = 8 × 4 ÷ 2 = 16, y la raíz de 16 es 4."),
    ],
    ctx=("abc", "Un auto toma una curva de radio 50 m. Si duplica su rapidez en esa misma curva, ¿cómo cambia la fuerza de roce necesaria?", "Se multiplica por 4", "Se duplica", "Se reduce a la mitad", "La fuerza central crece con el cuadrado de la rapidez."),
    sc=[
        ("En Física: ¿qué pasa con la fuerza central si el radio se duplica y lo demás no cambia?", "Se reduce a la mitad", "La fuerza es inversamente proporcional al radio."),
        ("¿Cuántas variables deben cambiar entre dos ensayos para comparar de forma válida?", "Una sola", "Así se puede atribuir el cambio a esa variable."),
        ("¿Cuál es la fuerza central de un cuerpo de 1 kg con v = 2 m/s en un radio de 2 m?", "2 N", "Se calcula 1 × 2 × 2 ÷ 2."),
    ],
    op=("Elige un cuerpo ficticio. Cuerpo 1: m = 3 kg, v = 2 m/s, r = 6 m. Cuerpo 2: m = 5 kg, v = 4 m/s, r = 10 m. Calcula su fuerza central. Después diseña una segunda fila de datos donde solo cambie una variable (elige cuál) y calcula la nueva fuerza. Explica cómo cambió la fuerza y por qué la comparación es válida.",
        "Cuerpo 1: F = 3 × 2 × 2 ÷ 6 = 2 N. Segunda fila: cambio solo la rapidez a 4 m/s: F = 3 × 16 ÷ 6 = 8 N. La fuerza se multiplicó por 4 al duplicar v. La comparación es válida porque m y r quedaron iguales.",
        ["calcula la fuerza con la fórmula y unidades", "cambia una sola variable", "explica el efecto con proporcionalidad"],
        ["hoja con dos filas de datos, el cálculo y la explicación"],
        ["cambiar dos variables a la vez", "olvidar elevar v al cuadrado", "olvidar la unidad"],
        "Pregunta: «¿qué variable cambió y cuáles quedaron iguales?»."),
    reinforce="Calcula la fuerza central para m = 1 kg, v = 1, 2 y 3 m/s y r = 1 m, y observa cómo crece.",
    extend="Explica por qué, con el mismo radio, un auto cargado necesita más fuerza de roce para tomar una curva que uno vacío.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 3 (de ejemplo). Para razonar sin la constante de gravitación usa solo proporciones. La distancia r se mide desde el centro de la Tierra, en radios terrestres (R). "
     "La fuerza gravitatoria sobre un satélite ficticio es F0 = 800 N cuando r = 1 R (superficie). Usa g ≈ 10 m/s² en la superficie (valor aproximado).")
build(
    O3, 3, F,
    use="Aprenderé a usar la ley de gravitación universal como modelo de una fuerza central y a razonar con proporciones sobre órbitas y satélites.",
    prior=["Sé que la gravedad es una fuerza de atracción.", "Sé usar proporciones y potencias.", "Sé que una fuerza central puede mantener un movimiento circular."],
    explain=[
        "La ley de gravitación universal de Newton dice que dos masas M y m se atraen con una fuerza F = G × M × m ÷ r², donde r es la distancia entre sus centros y G es una constante muy pequeña. La fuerza es proporcional a cada masa e inversamente proporcional al cuadrado de la distancia: si la distancia se duplica, la fuerza se divide por 4; si se triplica, por 9. Esta fuerza siempre apunta hacia el centro del otro cuerpo: es una fuerza central.",
        "En una órbita circular, la gravedad cumple el papel de fuerza centrípeta: G × M × m ÷ r² = m × v² ÷ r. De aquí resulta que v² = G × M ÷ r: a mayor distancia, menor rapidez orbital. Un satélite no «escapa» de la gravedad: está en caída libre alrededor de la Tierra, porque su rapidez horizontal hace que la superficie curva se aleje a la misma tasa con que él cae. Por eso los astronautas flotan: ellos y la estación caen juntos.",
        "El peso de un cuerpo es la fuerza gravitatoria sobre él: P = m × g, con g ≈ 10 m/s² en la superficie. Como g depende de 1 ÷ r², a doble distancia del centro g vale la cuarta parte. Con proporciones se resuelven muchos problemas sin conocer G: se compara la situación nueva con una de referencia y se aplica el factor 1 ÷ (cambio de distancia)².",
    ],
    vocab=[("gravitación universal", "atracción mutua entre todas las masas"), ("órbita", "trayectoria de un cuerpo alrededor de otro por la gravedad"), ("caída libre", "movimiento en que solo actúa la gravedad"), ("peso", "fuerza gravitatoria sobre un cuerpo, P = m × g"), ("inversamente proporcional al cuadrado", "se divide por el cuadrado del cambio de distancia"), ("rapidez orbital", "rapidez con que un cuerpo recorre su órbita")],
    worked=[
        ("Proporciones de distancia", "Una fuerza gravitatoria vale 90 N a 1 unidad de distancia. ¿Cuánto vale a 3 unidades?", ["Al triplicar la distancia, la fuerza se divide por 3² = 9.", "Calcula 90 ÷ 9."], "10 N"),
        ("Masa y distancia a la vez", "Dos cuerpos se atraen con 60 N. Se duplica la masa de uno y se duplica la distancia. ¿Cuánto vale la fuerza?", ["Duplicar una masa multiplica la fuerza por 2.", "Duplicar la distancia la divide por 4: 60 × 2 ÷ 4."], "30 N"),
    ],
    mistakes=[("Creer que la fuerza se divide por 2 cuando la distancia se duplica.", "Se olvida que la distancia está al cuadrado.", "Eleva el factor al cuadrado: doble distancia, fuerza ÷ 4."),
              ("Decir que en la estación espacial no hay gravedad.", "Se confunde estar en caída libre con ausencia de gravedad.", "A esa altura la gravedad sigue siendo fuerte; ellos caen junto con la estación.")],
    T=[
        ("abc", "La ley de gravitación universal dice que la fuerza entre dos masas", "es mayor cuando las masas son mayores y menor cuando están más lejos", "no depende de la distancia", "solo existe entre planetas", "La fórmula incluye el producto de masas y la distancia al cuadrado."),
        ("abc", "Si se duplica la masa de uno de los dos cuerpos, la fuerza gravitatoria entre ambos", "se duplica", "se reduce a la mitad", "se multiplica por 4", "La fuerza es proporcional a cada masa."),
        ("ab", "Un satélite en órbita circular está", "en caída libre alrededor de la Tierra", "fuera del alcance de la gravedad terrestre", "La gravedad actúa y lo hace caer, pero su rapidez lateral lo mantiene en órbita."),
        ("=", "{F} ¿Cuántos N vale la fuerza sobre el satélite a 2 R? (la fuerza se divide por 2²)", "800//4", "Al doble de distancia la fuerza es la cuarta parte.", " N"),
        ("abc", "{F} Si el satélite se aleja a 4 R, la fuerza gravitatoria es", "16 veces menor que en la superficie", "4 veces menor que en la superficie", "igual que en la superficie", "El factor es 4², es decir, 16."),
        ("abc", "¿Por qué los astronautas flotan dentro de una estación orbital?", "Porque ellos y la estación caen juntos alrededor de la Tierra", "Porque a esa altura no hay gravedad", "Porque la Tierra deja de atraerlos al girar", "La gravedad sigue actuando; la sensación de flotar viene de la caída libre."),
        ("=", "{F} ¿Cuántos N vale la fuerza a 4 R?", "800//16", "La fuerza se divide por el cuadrado del cambio de distancia.", " N"),
        ("=", "{F} ¿Cuántos N vale la fuerza a 5 R?", "800//25", "Se divide 800 entre 5², es decir, entre 25.", " N"),
        ("=", "Un cuerpo de 70 kg está en la superficie. Con g ≈ 10 m/s², ¿cuánto vale su peso?", "70*10", "El peso es la masa por la aceleración de gravedad.", " N"),
        ("abc", "La fuerza gravitatoria entre dos cuerpos es 100 N. Se duplica la distancia y se triplica la masa de uno. ¿Cuánto vale ahora?", "75 N", "300 N", "150 N", "Triplicar la masa da 300 N y duplicar la distancia divide por 4: 300 ÷ 4 = 75 N."),
        ("abc", "En la ley de gravitación aparece r al cuadrado. Si se triplica la distancia, la fuerza", "se divide por 9", "se divide por 3", "se divide por 6", "El factor es 3², es decir, 9."),
        ("abc", "Dos satélites circulan en órbitas circulares de la misma Tierra, uno más bajo y otro más alto. ¿Cuál tiene mayor rapidez orbital?", "El más bajo", "El más alto", "Ambos tienen la misma", "De v² = G × M ÷ r, un radio menor da mayor rapidez."),
        ("abc", "Newton imaginó un cañón en una montaña muy alta. Si la bala sale con rapidez horizontal suficiente, ¿qué sucede?", "Cae continuamente, pero la superficie curva se aleja a la misma tasa, y queda en órbita", "Sube y escapa del planeta", "Se queda quieta en el aire", "La bala cae, pero la Tierra curva se aleja de ella al mismo ritmo."),
    ],
    ctx=("=", "Un objeto de 10 kg se lleva al doble de distancia del centro de la Tierra (2 R). Con g ≈ 10 m/s² en la superficie, ¿qué valor tiene su peso allí? (g se divide por 4)", "10*10//4", "A doble distancia, g es la cuarta parte y el peso baja en esa proporción.", " N"),
    sc=[
        ("En Física: ¿qué le ocurre a la fuerza gravitatoria si la distancia se duplica?", "Se divide por 4", "La distancia está elevada al cuadrado."),
        ("¿Un satélite en órbita está fuera de la gravedad?", "No", "Está en caída libre, atraído por la gravedad."),
        ("¿Cuánto pesa en N un cuerpo de 50 kg con g ≈ 10 m/s²?", "500 N", "El peso es masa por g."),
    ],
    op=("Elige un caso. Caso 1: un satélite ficticio de masa m con F0 = 600 N en la superficie, llevado a 3 R. Caso 2: un satélite ficticio con F0 = 1.000 N, llevado a 5 R. Calcula la fuerza gravitatoria a esa distancia, explica con proporciones por qué disminuye, y escribe qué fuerza cumple el papel de fuerza central y en qué sentido apunta.",
        "Caso 1: a 3 R la fuerza es 600 ÷ 3² = 600 ÷ 9, aproximadamente 66,7 N. Disminuye porque depende de 1 ÷ r². La fuerza central es la gravedad terrestre y apunta hacia el centro de la Tierra.",
        ["calcula la fuerza con el factor 1 ÷ r²", "explica la disminución con proporciones", "identifica la fuerza central y su sentido"],
        ["hoja con el cálculo, la explicación y un dibujo con el satélite y la flecha hacia el centro"],
        ["dividir por 3 en lugar de por 9", "dibujar la fuerza hacia afuera", "decir que en órbita no hay gravedad"],
        "Pregunta: «¿por cuánto se divide la fuerza cuando la distancia se multiplica por k?»."),
    reinforce="Haz una tabla con la fuerza del satélite de la ficha a 1 R, 2 R, 4 R y 5 R.",
    extend="Explica por qué dos satélites de distinta masa pueden tener la misma rapidez orbital en la misma órbita.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 4 (de ejemplo). Planetas ficticios de una misma estrella; r es la distancia media a la estrella, en unidades astronómicas (UA, 1 UA es la distancia media entre la Tierra y el Sol), y T el período en años. "
     "Planeta A: r = 1, T = 1. Planeta B: r = 4, T = 8. Planeta C: r = 9, T = 27. Tercera ley de Kepler: T² = r³ en estas unidades.")
build(
    O3, 4, F,
    use="Aprenderé a analizar datos de órbitas con las leyes de Kepler, a contrastar una ley con una tabla y a evaluar si una conclusión es coherente con la evidencia.",
    prior=["Sé que la gravedad es una fuerza central.", "Sé calcular cuadrados y cubos.", "Sé leer tablas de datos."],
    explain=[
        "Las tres leyes de Kepler resumen observaciones de las órbitas planetarias. Primera ley: cada planeta describe una elipse (círculo alargado) con la estrella en uno de sus focos. Segunda ley: la línea que une el planeta con la estrella barre áreas iguales en tiempos iguales; por eso el planeta se mueve más rápido cuando está más cerca de la estrella. Tercera ley: para los planetas de una misma estrella, el cuadrado del período dividido por el cubo del radio medio es constante (T² ÷ r³ es constante).",
        "Newton mostró que estas leyes se deducen de la gravitación universal: la fuerza central cambia con 1 ÷ r², y de eso resulta T² proporcional a r³. En las unidades de UA y años, la constante vale 1, así que T² = r³. Para comprobarlo con una tabla se calculan T² y r³ de cada planeta y se ve si coinciden dentro de la incertidumbre de las mediciones.",
        "Analizar evidencia es contrastar una ley con datos. Si los valores coinciden, la ley queda respaldada; si no coinciden, hay que revisar primero los datos (¿unidades?, ¿medición?, ¿otro tipo de órbita?) antes de descartar la ley. Una explicación debe también ser coherente con otras observaciones. Por ejemplo, las estaciones del año se deben a la inclinación del eje terrestre y no a la distancia al Sol.",
    ],
    vocab=[("elipse", "círculo alargado, con dos focos"), ("foco", "uno de los dos puntos que definen una elipse"), ("unidad astronómica (UA)", "distancia media entre la Tierra y el Sol"), ("radio medio", "distancia media entre el planeta y su estrella"), ("tercera ley de Kepler", "T² ÷ r³ es constante para una misma estrella"), ("incertidumbre", "margen de error de una medición")],
    worked=[
        ("Verificar la ley", "Un planeta ficticio tiene r = 2 UA y T = 3 años. ¿Cumple T² = r³?", ["Calcula T² = 3 × 3 = 9.", "Calcula r³ = 2 × 2 × 2 = 8; 9 y 8 no coinciden."], "No cumple con esos datos; habría que revisar las mediciones"),
        ("Aplicar la ley", "Un planeta ficticio está a r = 25 UA. ¿Cuál es su período?", ["T² = r³ = 25 × 25 × 25 = 15.625.", "El número que multiplicado por sí mismo da 15.625 es 125."], "T = 125 años"),
    ],
    mistakes=[("Pensar que las órbitas son círculos perfectos.", "Se simplifica el modelo y se olvida la elipse.", "Recuerda que la estrella está en un foco, no en el centro de la elipse."),
              ("Explicar las estaciones por la distancia al Sol.", "Se confunde cercanía con inclinación del eje.", "Comprueba con datos: cuando es verano en un hemisferio, es invierno en el otro.")],
    T=[
        ("abc", "Según la tercera ley de Kepler, para los planetas de una misma estrella", "T² ÷ r³ es constante", "T ÷ r es constante", "T × r es constante", "La ley relaciona el cuadrado del período con el cubo del radio."),
        ("abc", "Según la segunda ley de Kepler, un planeta se mueve más rápido cuando está", "más cerca de su estrella", "más lejos de su estrella", "a la misma rapidez siempre", "Para barrer áreas iguales en tiempos iguales, cerca de la estrella debe ir más rápido."),
        ("ab", "La primera ley de Kepler dice que las órbitas son", "elipses con la estrella en un foco", "círculos perfectos con la estrella en el centro", "La primera ley describe órbitas elípticas con la estrella en un foco."),
        ("=", "{F} ¿Cuánto vale r³ para el planeta B (r = 4)?", "4*4*4", "El cubo es r por r por r.", ""),
        ("=", "{F} ¿Cuánto vale T² para el planeta B (T = 8)?", "8*8", "El cuadrado es T por T.", ""),
        ("abc", "{F} Con los datos de A, B y C, ¿qué se concluye?", "T² y r³ coinciden en los tres: los datos respaldan la tercera ley", "Los datos contradicen la tercera ley", "No se puede concluir nada", "Para A, B y C los valores de T² son 1, 64 y 729, iguales a r³."),
        ("{F} Un planeta D está a r = 16 UA, de modo que T² = r³ = 4.096. ¿Cuántos años dura su período? (un número multiplicado por sí mismo que dé 4.096)", "64 años", "64 × 64 = 4.096, así que T = 64."),
        ("{F} Un planeta E tiene T = 1.000 años, de modo que T² = 1.000.000. ¿A qué distancia está si r³ = T²? (busca el número cuyo cubo es 1.000.000)", "100 UA", "100 × 100 × 100 = 1.000.000, así que r = 100."),
        ("Un planeta barre un área de 12 unidades en 30 días cuando está lejos de su estrella. ¿Qué área barre en otros 30 días cuando está cerca?", "12 unidades, la misma", "La segunda ley dice que se barren áreas iguales en tiempos iguales."),
        ("abc", "Dos estudiantes miden la órbita de un planeta y obtienen valores levemente distintos de T² ÷ r³. ¿Qué es lo más razonable?", "Revisar la incertidumbre de cada medición y ver si la diferencia cabe dentro del error", "Concluir que la ley es falsa", "Descartar el valor que no calza", "Las mediciones tienen margen de error; la diferencia pequeña no refuta la ley por sí sola."),
        ("abc", "La Tierra pasa más cerca del Sol a comienzos de enero que a comienzos de julio. Según la segunda ley de Kepler, ¿cuándo se mueve más rápido?", "A comienzos de enero", "A comienzos de julio", "Igual en ambos", "Más cerca de la estrella, mayor rapidez orbital."),
        ("abc", "Alguien dice: «las estaciones ocurren porque la Tierra está más cerca del Sol en verano». ¿Qué dato lo contradice?", "Cuando es verano en un hemisferio, es invierno en el otro, aunque la distancia al Sol es la misma para ambos", "Que la Tierra tiene forma de esfera", "Que el Sol es una estrella", "Si la distancia fuera la causa, ambos hemisferios tendrían la misma estación a la vez."),
        ("abc", "Una tabla ficticia dice que un planeta tiene r = 4 UA y T = 6 años. ¿Es coherente con T² = r³?", "No: T² = 36 y r³ = 64, no coinciden", "Sí: 6 es mayor que 4", "Sí: 36 y 64 son números pares", "Al calcular T² y r³ se ve que difieren; habría que revisar los datos."),
    ],
    ctx=("abc", "Una estación espacial ficticia mide tres lunas de un planeta, en unidades de ejemplo: r = 4 con T = 8; r = 9 con T = 20; r = 16 con T = 64. ¿Siguen la regla T² = r³?", "No: la segunda falla, porque T² = 400 y r³ = 729", "Sí: las tres la cumplen", "No: la primera falla, porque T² = 64 y r³ = 64", "En la primera y la tercera T² y r³ coinciden (64 y 4.096), pero en la segunda no; habría que revisar esa medición."),
    sc=[
        ("En Física: ¿qué constante se mantiene en la tercera ley de Kepler?", "T² dividido por r³", "Es la misma para los planetas de una misma estrella."),
        ("¿Cuándo se mueve más rápido un planeta en su órbita?", "Cuando está más cerca de su estrella", "Lo exige la ley de las áreas iguales."),
        ("¿Las estaciones se deben a la inclinación del eje o a la distancia al Sol?", "A la inclinación del eje", "Los hemisferios tienen estaciones opuestas a la misma distancia."),
    ],
    op=("Elige un conjunto de datos ficticios. Conjunto 1: r = 1 con T = 1; r = 4 con T = 8; r = 16 con T = 64. Conjunto 2: r = 1 con T = 1; r = 9 con T = 27; r = 4 con T = 9. Calcula T² y r³ de cada planeta, indica si el conjunto respalda la tercera ley, y si alguno falla, escribe dos cosas que revisarías antes de descartar la ley.",
        "Conjunto 1: T² = 1, 64 y 4.096; r³ = 1, 64 y 4.096: coinciden en los tres, así que respalda la ley. Conjunto 2 tendría un planeta que falla; revisaría las unidades de los datos y la incertidumbre de la medición.",
        ["calcula T² y r³ de cada planeta", "concluye si respalda la ley", "propone qué revisar si hay una discrepancia"],
        ["hoja con una tabla de tres filas y la conclusión"],
        ["calcular T³ y r² al revés", "descartar la ley sin revisar los datos", "olvidar las unidades"],
        "Pregunta: «¿qué valor te parece sospechoso y por qué?»."),
    reinforce="Con la ficha, calcula T² y r³ para A, B y C y comprueba que son iguales en cada fila.",
    extend="Explica cómo la tercera ley de Kepler permite estimar la distancia de un planeta a su estrella si se conoce su período.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 5 (de ejemplo; g ≈ 10 m/s²). En una curva plana circular de radio r, un auto no desliza si v² ≤ μ × g × r, donde μ es el coeficiente de roce (sin unidades). "
     "Valores de ejemplo: μ = 0,5 con pavimento seco y μ = 0,2 con pavimento mojado. Es decir, v² ≤ 5 × r en seco y v² ≤ 2 × r en mojado.")
build(
    O3, 5, F,
    use="Aprenderé a comparar soluciones y modelos para una curva: qué fuerza real la sostiene, cómo cambia el límite de rapidez y por qué la «fuerza centrífuga» no es una fuerza real en un sistema inercial.",
    prior=["Sé calcular la fuerza central m × v² ÷ r.", "Sé qué es el roce y que depende de las superficies.", "Sé que la primera ley de Newton implica seguir recto sin fuerza neta."],
    explain=[
        "En una curva plana, la fuerza central que mantiene al auto en la trayectoria es el roce estático entre los neumáticos y el suelo. El roce máximo es μ × N, y en una calzada plana N es igual al peso m × g. Para no deslizar se necesita m × v² ÷ r ≤ μ × m × g. La masa se simplifica y queda v² ≤ μ × g × r: el límite de rapidez depende del roce y del radio, no de cuánto pese el auto.",
        "De la condición salen las soluciones para una curva peligrosa: bajar la rapidez, aumentar el radio de la curva, mejorar el roce del pavimento o inclinar la calzada (peralte), de modo que parte de la fuerza del suelo apunte al centro. Al comparar soluciones se verifican con la condición, se revisa su margen de seguridad y se consideran costos y efectos para las personas.",
        "Los pasajeros sienten que «algo» los empuja hacia afuera. En un sistema de referencia inercial no existe una fuerza real hacia afuera: la sensación se debe a la inercia, porque el cuerpo tiende a seguir recto mientras el auto gira. Si se describe el movimiento desde el auto que gira (un sistema no inercial), se puede introducir una fuerza ficticia llamada centrífuga para facilitar los cálculos, pero no es causada por ningún cuerpo.",
    ],
    vocab=[("roce estático", "roce que evita que dos superficies en contacto deslicen"), ("coeficiente de roce (μ)", "número sin unidades que mide la fuerza de roce máxima respecto de la fuerza normal"), ("peralte", "inclinación de la calzada en una curva"), ("sistema inercial", "sistema de referencia sin aceleración"), ("fuerza ficticia", "fuerza que aparece al describir desde un sistema que acelera"), ("margen de seguridad", "holgura entre el valor real y el límite")],
    worked=[
        ("Rapidez máxima", "Con μ = 0,5, g ≈ 10 m/s² y r = 80 m, ¿cuál es la rapidez máxima sin deslizar?", ["v² máximo = 5 × 80 = 400.", "La raíz de 400 es 20."], "20 m/s"),
        ("Revisar una solución", "En una curva de 32 m de radio con pavimento mojado (μ = 0,2) se propone un límite de 9 m/s. ¿Cumple?", ["El límite de v² es 2 × 32 = 64, así que v máxima es 8 m/s.", "Con 9 m/s, v² = 81, mayor que 64."], "No cumple: el límite de 9 m/s es demasiado alto"),
    ],
    mistakes=[("Creer que un auto más pesado necesita un límite de rapidez menor en la curva.", "No se nota que la masa se simplifica en la condición.", "Resuelve v² ≤ μ × g × r sin usar la masa."),
              ("Dibujar una fuerza centrífuga real que tira el auto hacia afuera.", "Se describe la sensación y no la fuerza real.", "Dibuja solo el roce hacia el centro; el resto es inercia.")],
    T=[
        ("abc", "En un auto que toma una curva plana, ¿qué fuerza real apunta hacia el centro de la curva?", "El roce de los neumáticos con el suelo", "La fuerza centrífuga", "El peso del auto", "Entre las fuerzas de la lista, el roce es la única horizontal que ejerce el suelo sobre el auto."),
        ("abc", "¿Qué es el coeficiente de roce μ?", "Un número sin unidades que indica qué tan fuerte puede ser el roce entre dos superficies", "La rapidez máxima de un auto", "La masa del auto", "Es una razón entre fuerzas y por eso no tiene unidades."),
        ("ab", "Al mojarse el pavimento, el coeficiente de roce", "disminuye", "aumenta", "El agua reduce el agarre entre neumático y suelo."),
        ("=", "{F} Con μ = 0,5 y r = 20 m, ¿cuál es el límite de v² (v² ≤ 5 × r), en m²/s²?", "5*20", "Se multiplica 5 por el radio.", " m²/s²"),
        ("abc", "{F} ¿Por qué la masa del auto no aparece en la condición v² ≤ μ × g × r?", "Porque la masa aparece en la fuerza necesaria y en el roce máximo, y se simplifica", "Porque la masa nunca importa", "Porque se ignora por error", "Ambos lados de la desigualdad tienen m y se cancelan."),
        ("abc", "¿Qué es la «fuerza centrífuga» que sienten los pasajeros dentro del auto?", "Una sensación debida a la inercia, no una fuerza real en un sistema inercial", "Una fuerza real que empuja hacia afuera", "La misma fuerza que la gravedad", "El cuerpo tiende a seguir recto mientras el auto gira."),
        ("=", "{F} Con μ = 0,5 y r = 45 m, ¿cuál es el límite de v², en m²/s²?", "5*45", "Se multiplica 5 por el radio de 45 m.", " m²/s²"),
        ("{F} Con μ = 0,2 (mojado) y r = 50 m, ¿cuál es la rapidez máxima, en m/s?", "10 m/s", "v² máximo = 2 × 50 = 100, y la raíz de 100 es 10."),
        ("=", "Un auto de 1.000 kg viaja a 10 m/s en una curva de 25 m de radio. ¿Qué fuerza central necesita?", "1000*10*10//25", "Se usa F = m × v² ÷ r con los datos dados.", " N"),
        ("abc", "{F} En una curva de 45 m con pavimento seco, un conductor pasa de 15 m/s a 20 m/s. ¿Qué ocurre?", "Supera el límite de 15 m/s y tiende a deslizar hacia afuera de la curva", "Nada: sigue sin deslizar", "Gira con más seguridad", "A 20 m/s, v² = 400 y el límite era 225."),
        ("abc", "¿Cuál es una solución de diseño que aumenta la seguridad en una curva?", "Aumentar el radio de la curva o mejorar el roce del pavimento", "Disminuir el radio de la curva", "Quitar las señales de rapidez", "Un mayor radio o mayor roce aumenta el límite de rapidez."),
        ("abc", "{F} Dos soluciones para una curva de 20 m de radio con pavimento seco: bajar el límite de 15 a 10 m/s, o rediseñar con radio 45 m y mantener 15 m/s. ¿Qué se concluye?", "Ambas cumplen justo en el límite, sin margen de seguridad", "Solo la primera cumple", "Ninguna cumple", "En ambos casos v² es igual al máximo (100 y 225), así que no queda holgura."),
        ("abc", "{F} En una curva mojada de 50 m de radio, un conductor va a 11 m/s. ¿Qué dice la condición?", "No cumple: 121 es mayor que 100", "Cumple: 11 es menor que 50", "Cumple: 121 es menor que 200", "El límite de v² es 100 y 11 × 11 = 121."),
    ],
    ctx=("abc", "Un ingeniero ficticio compara dos curvas con el mismo pavimento: una de radio 20 m y otra de radio 60 m. ¿Cuál permite una rapidez máxima mayor sin deslizar?", "La de radio 60 m", "La de radio 20 m", "Ambas por igual", "Con v² ≤ μ × g × r, un radio mayor permite una rapidez máxima mayor."),
    sc=[
        ("En Física: ¿qué fuerza real mantiene a un auto en una curva plana?", "El roce de los neumáticos con el suelo", "Es la única fuerza horizontal sobre el auto."),
        ("¿La masa del auto cambia el límite de rapidez de la curva?", "No", "Se simplifica en la condición v² ≤ μ × g × r."),
        ("¿Es la fuerza centrífuga una fuerza real en un sistema inercial?", "No", "Es la sensación de inercia o una fuerza ficticia."),
    ],
    op=("Elige una curva ficticia. Curva 1: radio 45 m con pavimento mojado (μ = 0,2) y un límite propuesto de 10 m/s. Curva 2: radio 80 m con pavimento seco (μ = 0,5) y un límite propuesto de 22 m/s. Verifica con la condición si el límite es seguro, propone una solución alternativa (otro límite, otro radio u otro pavimento) y explica en dos líneas qué fuerza real mantiene al auto y por qué los pasajeros sienten ir hacia afuera.",
        "Curva 1: el límite de v² es 2 × 45 = 90, y 10 × 10 = 100 es mayor, así que el límite propuesto no es seguro. Solución: bajar el límite a 9 m/s (81 es menor que 90). La fuerza real es el roce hacia el centro; los pasajeros sienten ir hacia afuera por inercia.",
        ["verifica el límite con la condición", "propone una alternativa que cumple", "explica la fuerza real y la sensación"],
        ["hoja con el cálculo del límite, la alternativa y la explicación"],
        ["usar la masa en la condición", "dibujar una fuerza centrífuga real", "proponer una solución sin verificarla"],
        "Pregunta: «¿cuánto margen queda entre tu v² y el máximo?»."),
    reinforce="Con la ficha, calcula la rapidez máxima en seco y en mojado para una curva de radio 50 m.",
    extend="Explica cómo un peralte ayuda a tomar una curva más rápido sin depender solo del roce.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (de ejemplo, escalas aproximadas). Situaciones: (1) un balón que cae desde una mesa; (2) una partícula que viaja a 0,9 veces la rapidez de la luz; "
     "(3) un electrón dentro de un átomo; (4) un auto que viaja a 20 m/s. Rapidez de la luz: c ≈ 300.000 km/s, es decir, unos 300.000.000 m/s.")
build(
    O4, 1, F,
    use="Aprenderé a delimitar qué problemas llevaron a la física moderna y qué teoría (clásica, relatividad o cuántica) conviene usar según la escala del fenómeno.",
    prior=["Sé las leyes de Newton.", "Sé que la luz tiene una rapidez finita.", "Sé que la materia está formada por átomos."],
    explain=[
        "La física clásica (leyes de Newton, electromagnetismo, termodinámica) explica con gran precisión los fenómenos de escala humana a rapideces pequeñas. A fines del siglo XIX y comienzos del XX aparecieron problemas que no resolvía: la rapidez de la luz parecía ser la misma para todos los observadores, la radiación de los cuerpos calientes y la emisión de electrones por la luz (efecto fotoeléctrico). Esos problemas llevaron a dos teorías estructuradoras: la relatividad y la mecánica cuántica.",
        "La relatividad de Einstein (especial, 1905; general, 1915) describe fenómenos con rapideces cercanas a la de la luz y con gravedad intensa, y modifica ideas sobre el tiempo y el espacio. La mecánica cuántica (nacida con Planck en 1900 y desarrollada en las décadas siguientes) describe lo muy pequeño: átomos, luz y partículas. En ambos casos, a escalas cotidianas las predicciones se parecen mucho a las de la física clásica, que sigue siendo válida como aproximación.",
        "La física moderna abrió un debate sobre la naturaleza de la realidad: ¿el tiempo es igual para todos los observadores?, ¿las propiedades de un sistema existen antes de medirlas?, ¿el resultado de una medición se puede predecir con certeza o solo con probabilidad? Para delimitar una pregunta se nombra la situación, la escala (tamaño y rapidez) y la teoría que se pondrá a prueba. Una teoría científica no es una opinión: es un conjunto de explicaciones contrastadas con observaciones.",
    ],
    vocab=[("física clásica", "mecánica de Newton, electromagnetismo y termodinámica"), ("relatividad", "teoría sobre espacio, tiempo y gravedad, importante a rapideces altas o gravedad intensa"), ("mecánica cuántica", "teoría de lo muy pequeño: átomos, luz y partículas"), ("teoría estructuradora", "teoría que organiza gran parte de la física"), ("escala", "tamaño y rapidez típicos de un fenómeno"), ("aproximación", "resultado suficientemente cercano al exacto en ciertas condiciones")],
    worked=[
        ("Elegir la teoría", "Para calcular cuánto tarda en caer una maceta desde un balcón de 5 m, ¿qué teoría conviene usar?", ["Escala: tamaño humano y rapidez pequeña, muy lejos de la de la luz.", "En ese rango, la mecánica clásica da resultados suficientes."], "Mecánica clásica"),
        ("Delimitar una pregunta", "Mejora «¿Qué es la relatividad?» para convertirla en una pregunta investigable.", ["Nombra un fenómeno: el tiempo medido por observadores con distinta rapidez.", "Agrega la teoría y la escala: relatividad especial, rapideces cercanas a la de la luz."], "«¿Qué predice la relatividad especial sobre el tiempo medido por observadores con distinta rapidez?»"),
    ],
    mistakes=[("Pensar que la física moderna demostró que la física clásica estaba mal.", "Se ignora que la clásica es una buena aproximación a escalas cotidianas.", "Pregunta siempre por la escala del fenómeno."),
              ("Creer que una teoría científica es solo una opinión.", "Se confunde el uso cotidiano de «teoría» con el científico.", "Recuerda que una teoría está contrastada con observaciones.")],
    T=[
        ("abc", "¿Qué teoría describe mejor el comportamiento de los electrones dentro de un átomo?", "La mecánica cuántica", "La relatividad", "La mecánica clásica sin correcciones", "Los fenómenos atómicos exigen la mecánica cuántica."),
        ("abc", "¿Qué teoría es clave para objetos que viajan a rapideces cercanas a la de la luz?", "La relatividad especial", "La mecánica cuántica", "La termodinámica", "La relatividad especial modifica las ideas de tiempo y espacio a rapideces altas."),
        ("ab", "Para un balón que cae desde una mesa, la teoría adecuada y suficiente es", "la mecánica clásica", "la mecánica cuántica", "A escala humana y rapidez pequeña la clásica da resultados muy precisos."),
        ("abc", "{F} ¿Qué situación se estudia con mecánica cuántica?", "La 3, un electrón dentro de un átomo", "La 1, un balón que cae", "La 4, un auto a 20 m/s", "Lo muy pequeño pertenece al dominio de la cuántica."),
        ("abc", "¿Por qué no se dice que la mecánica clásica quedó refutada por la física moderna?", "Porque sigue funcionando muy bien a escalas cotidianas y es el límite de las teorías modernas", "Porque la física moderna se equivocó", "Porque nunca se aplicó a nada", "Las teorías modernas coinciden con la clásica en su rango de validez."),
        ("abc", "¿Cuál es una pregunta delimitada para esta unidad?", "¿Qué predice la relatividad especial sobre el tiempo medido por observadores con distinta rapidez?", "¿Es la física moderna mejor que la clásica?", "¿Quién fue más inteligente, Newton o Einstein?", "Nombra teoría, fenómeno y escala, y puede contrastarse con evidencia."),
        ("=", "{F} Una partícula viaja a 0,9 veces la rapidez de la luz. ¿Cuántos km/s son?", "300000*9//10", "Se toma el 90 % de 300.000 km/s.", " km/s"),
        ("abc", "Clasifica cada caso con su teoría, en este orden: I) un electrón en un átomo, II) un auto a 20 m/s, III) una nave a 0,8 veces la rapidez de la luz.", "Cuántica, clásica, relatividad", "Clásica, cuántica, relatividad", "Relatividad, clásica, cuántica", "El electrón pertenece a lo muy pequeño, el auto a lo cotidiano y la nave a lo muy rápido."),
        ("=", "{F} ¿Cuántas veces cabe la rapidez del auto de 20 m/s en la rapidez de la luz?", "300000000//20", "Se divide la rapidez de la luz entre la del auto.", " veces"),
        ("abc", "Alguien dice: «si la relatividad es verdadera, los cálculos de Newton para un puente están equivocados». ¿Cuál es la mejor respuesta?", "Para rapideces pequeñas la diferencia es tan pequeña que los cálculos de Newton son suficientes", "Tiene razón: los puentes se deben calcular con relatividad", "La relatividad solo se usa en laboratorios", "La clásica es una excelente aproximación en su rango de validez."),
        ("abc", "El debate sobre la naturaleza de la realidad en la física moderna incluye preguntas como", "si el tiempo es igual para todos los observadores o depende de su movimiento", "cuál es el mejor instrumento de medida", "cuál país descubrió más leyes", "Es un debate sobre conceptos de tiempo, espacio y medición."),
        ("abc", "Un estudiante dice: «la mecánica cuántica es solo una teoría, o sea una opinión». ¿Qué falla?", "En ciencia, una teoría es un conjunto de explicaciones contrastadas con observaciones y no una opinión", "Nada: las teorías no se contrastan", "Que la cuántica no es teoría sino ley", "El uso científico de «teoría» exige respaldo de datos."),
        ("abc", "Se quiere calcular la estructura de un puente y también cómo se comporta un electrón en un átomo. ¿Qué teorías conviene usar, en ese orden?", "Clásica y cuántica", "Cuántica y clásica", "Relatividad y relatividad", "El puente es cotidiano y el electrón pertenece a la escala atómica."),
    ],
    ctx=("abc", "Un museo ficticio tiene tres paneles: «Lo muy pequeño», «Lo muy rápido» y «Lo cotidiano». ¿Qué teoría corresponde a cada uno, en ese orden?", "Cuántica, relatividad, clásica", "Clásica, cuántica, relatividad", "Relatividad, clásica, cuántica", "Cada teoría se aplica en su escala: átomos, rapideces altas y fenómenos del día a día."),
    sc=[
        ("En Física moderna: ¿qué teoría describe lo muy pequeño?", "La mecánica cuántica", "Estudia el comportamiento de átomos, luz y partículas."),
        ("¿La física clásica es inútil después de la relatividad?", "No", "Sigue siendo una aproximación excelente a escalas cotidianas."),
        ("¿Una teoría científica es solo una opinión?", "No", "Es un conjunto de explicaciones contrastadas con observaciones."),
    ],
    op=("Elige tres fenómenos de esta lista: la caída de una fruta, el movimiento de un electrón en un átomo, una nave a 0,8 veces la rapidez de la luz, una pelota que rueda por una cancha, la luz que libera electrones de un metal. Para cada uno escribe la escala (tamaño y rapidez), la teoría que usarías y una frase de por qué. Después escribe una pregunta delimitada sobre uno de ellos.",
        "Fruta que cae: escala humana y rapidez pequeña; mecánica clásica. Electrón en un átomo: escala atómica; mecánica cuántica. Nave a 0,8 c: rapidez cercana a la de la luz; relatividad especial. Pregunta: ¿cómo se mide el tiempo en una nave a 0,8 c respecto de la Tierra?",
        ["asigna una teoría a cada fenómeno", "justifica con la escala", "formula una pregunta delimitada"],
        ["hoja con tres filas (fenómeno, escala, teoría, razón) y una pregunta"],
        ["asignar siempre la cuántica", "ignorar la escala", "formular preguntas valorativas"],
        "Pregunta: «¿qué tan grande y qué tan rápido es el fenómeno que elegiste?»."),
    reinforce="Anota cinco situaciones de tu día y escribe al lado qué teoría conviene usar para cada una.",
    extend="Explica por qué una teoría nueva suele contener a la anterior como caso límite.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (de ejemplo). c ≈ 300.000 km/s. Factor de dilatación del tiempo (redondeado): a 0,6 c, γ = 5/4; a 0,8 c, γ = 5/3. "
     "El tiempo medido por un observador en reposo es Δt = γ × Δt0, donde Δt0 es el tiempo propio (el que mide el reloj que viaja con la nave).")
build(
    O4, 2, F,
    use="Aprenderé los postulados de la relatividad especial, calcularé la dilatación del tiempo con factores dados y evaluaré fuentes sobre este tema.",
    prior=["Sé que la rapidez de la luz es finita.", "Sé multiplicar y dividir con fracciones simples.", "Sé qué es un sistema de referencia."],
    explain=[
        "La relatividad especial parte de dos postulados. Primero: las leyes de la física son las mismas en todos los sistemas inerciales (los que se mueven con rapidez constante). Segundo: la rapidez de la luz en el vacío es la misma para todos los observadores, sin importar el movimiento de la fuente o del observador, y ningún objeto con masa puede alcanzarla. De ellos se deduce que el tiempo medido depende del movimiento relativo.",
        "La dilatación del tiempo dice que un reloj en movimiento marca menos tiempo que uno en reposo, medido por el observador en reposo: Δt = γ × Δt0, con γ mayor que 1 y que crece cuando la rapidez se acerca a c. Por ejemplo, a 0,6 c, γ = 5/4: si en la nave pasan 8 años, en la Tierra pasan 8 × 5/4 = 10 años. El efecto es mínimo a rapideces cotidianas, porque estas son muy pequeñas comparadas con c.",
        "Hay evidencia experimental: partículas inestables llamadas muones, creadas en la atmósfera alta, alcanzan el suelo en mayor número que el esperado si no hubiera dilatación del tiempo, y los relojes de los satélites de posicionamiento requieren correcciones relativistas para dar la posición con exactitud. Al evaluar una fuente sobre relatividad se revisa si distingue lo que la teoría predice, lo que se ha medido y lo que es especulación.",
    ],
    vocab=[("sistema inercial", "sistema que se mueve con rapidez constante"), ("postulado", "supuesto básico de una teoría"), ("tiempo propio (Δt0)", "tiempo medido por el reloj que viaja con el objeto"), ("dilatación del tiempo", "aumento del tiempo medido para un reloj en movimiento"), ("factor γ", "número mayor que 1 que depende de la rapidez"), ("muón", "partícula inestable producida en la atmósfera alta")],
    worked=[
        ("Calcular el tiempo del observador", "Una nave ficticia viaja a 0,6 c y su reloj marca 4 años. ¿Cuántos años pasan para un observador en reposo?", ["γ = 5/4 a 0,6 c.", "Δt = 4 × 5/4 = 5."], "5 años"),
        ("Calcular el tiempo propio", "Un observador en reposo mide 15 años para una nave a 0,8 c. ¿Cuánto marca el reloj de la nave?", ["Δt0 = Δt ÷ γ = 15 × 3/5.", "15 × 3 ÷ 5 = 9."], "9 años"),
    ],
    mistakes=[("Pensar que el reloj de la nave se descompone o va «mal».", "El reloj funciona bien en su sistema; el efecto aparece al comparar sistemas.", "Distingue tiempo propio y tiempo del observador."),
              ("Usar γ menor que 1.", "Se multiplica o divide al revés.", "El tiempo del observador en reposo siempre es mayor que el propio.")],
    T=[
        ("abc", "Uno de los postulados de la relatividad especial es que la rapidez de la luz en el vacío", "es la misma para todos los observadores", "depende de la rapidez de la fuente", "puede superarse con cohetes", "Este postulado es la base de la dilatación del tiempo."),
        ("abc", "¿Qué significa tiempo propio?", "El tiempo medido por un reloj que viaja junto con el objeto", "El tiempo medido solo por relojes de pared", "El tiempo medido en la Tierra siempre", "Es el que marca el reloj que está en reposo respecto del objeto."),
        ("ab", "Según la relatividad especial, el tiempo que mide un observador en reposo para un reloj en movimiento rápido es", "mayor que el tiempo propio", "menor que el tiempo propio", "Δt = γ × Δt0 con γ mayor que 1, así que Δt supera a Δt0."),
        ("=", "{F} Una nave viaja a 0,6 c y en su reloj pasan 24 años. ¿Cuántos años pasan para un observador en reposo?", "24*5//4", "Se multiplica el tiempo propio por γ = 5/4.", " años"),
        ("abc", "{F} ¿Qué pasa con la dilatación del tiempo a rapideces pequeñas, como 20 m/s?", "Es tan pequeña que no se nota en la vida diaria", "Es enorme y se nota siempre", "El tiempo se detiene", "A rapideces mucho menores que c, γ es casi 1."),
        ("abc", "¿Qué observación experimental respalda la dilatación del tiempo?", "Los muones creados en la atmósfera alta alcanzan el suelo en mayor número del esperado sin dilatación", "Que los relojes de pared se atrasan", "Que la Luna tiene fases", "Su vida media aumenta para un observador en reposo cuando se mueven rápido."),
        ("=", "{F} Una nave viaja a 0,8 c y en su reloj pasan 6 años. ¿Cuántos años pasan para un observador en reposo?", "6*5//3", "Se multiplica el tiempo propio por γ = 5/3.", " años"),
        ("=", "{F} Una nave viaja a 0,6 c y para un observador en reposo pasan 20 años. ¿Cuántos años pasan en el reloj de la nave? (Δt0 = Δt ÷ γ)", "20*4//5", "Se divide por 5/4, que es multiplicar por 4/5.", " años"),
        ("=", "A 0,8 veces la rapidez de la luz, ¿cuántos km/s es la rapidez de la nave?", "300000*8//10", "Se toma el 80 % de 300.000 km/s.", " km/s"),
        ("abc", "Un estudiante dice: «si el tiempo se dilata, entonces los relojes de la nave se descomponen». ¿Qué falla?", "El reloj funciona perfectamente en su sistema; es el tiempo medido desde otro sistema el que difiere", "Nada: los relojes en movimiento se descomponen", "El tiempo no cambia nunca", "Cada observador mide correctamente en su propio sistema."),
        ("abc", "{F} ¿Por qué el valor 5/3 a 0,8 c es mayor que 5/4 a 0,6 c?", "Porque el efecto crece cuando la rapidez se acerca a c", "Porque 0,8 es menor que 0,6", "Porque la nave pesa más", "Cuanto más rápido, mayor la dilatación."),
        ("abc", "Un divulgador escribe que «según Einstein, viajando muy rápido se puede cambiar el pasado». ¿Cuál es la mejor evaluación de esa fuente?", "No lo respalda la relatividad especial, que solo predice diferencias en la medición del tiempo entre observadores", "Es correcta porque Einstein lo dijo", "No se puede evaluar ninguna fuente", "La teoría predice diferencias de medición, no cambios del pasado."),
        ("abc", "Un tripulante de una nave a 0,6 c mide 8 años de viaje y un observador en la Tierra mide 10 años. ¿Quién se equivoca?", "Ninguno: cada uno mide correctamente en su sistema", "El de la nave", "El de la Tierra", "Los dos resultados son consistentes con Δt = γ × Δt0."),
    ],
    ctx=("=", "Un viaje ficticio dura 12 años en el reloj de la nave, que viaja a 0,8 c. ¿Cuántos años pasan para observadores en reposo?", "12*5//3", "Se multiplica por γ = 5/3 el tiempo propio.", " años"),
    sc=[
        ("En Física moderna: ¿qué dice el segundo postulado de la relatividad especial?", "La rapidez de la luz en el vacío es la misma para todos los observadores", "Es la base del resto de la teoría."),
        ("¿El tiempo medido por el observador en reposo es mayor o menor que el tiempo propio?", "Mayor", "Δt = γ × Δt0 con γ mayor que 1."),
        ("Si γ = 5/4 y Δt0 = 12 años, ¿cuánto vale Δt?", "15 años", "Se calcula 12 × 5/4 = 15."),
    ],
    op=("Elige un viaje. Viaje 1: una nave ficticia a 0,6 c con 16 años de tiempo propio. Viaje 2: una nave ficticia a 0,8 c con 9 años de tiempo propio. Calcula el tiempo para un observador en reposo, explica en dos líneas por qué ambos tiempos son correctos y evalúa esta frase: «la nave rejuvenece a su tripulación».",
        "Viaje 1: Δt = 16 × 5/4 = 20 años. Ambos son correctos: cada uno mide con su reloj en su sistema. Frase: es una exageración; la teoría dice que el reloj marca menos tiempo medido desde fuera, y la tripulación vive su tiempo propio con normalidad.",
        ["calcula con γ y unidades", "explica por qué ambos tiempos son correctos", "evalúa la frase con la teoría"],
        ["hoja con cálculo, explicación y evaluación"],
        ["dividir en vez de multiplicar", "decir que el reloj se descompone", "aceptar la frase sin revisarla"],
        "Pregunta: «¿quién mide el tiempo propio y quién el tiempo del observador?»."),
    reinforce="Con la ficha, calcula el tiempo del observador para una nave a 0,6 c con 12 años de tiempo propio.",
    extend="Explica por qué la dilatación del tiempo es imperceptible en un viaje en avión pero relevante para partículas muy rápidas.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (de ejemplo, energías en electronvoltios, eV, unidad de energía de la física atómica). Un metal ficticio necesita al menos W = 2 eV para liberar un electrón. "
     "Tres luces de ejemplo: luz 1, fotones de 1 eV; luz 2, fotones de 3 eV; luz 3, fotones de 5 eV. Un átomo ficticio tiene niveles de energía de 0 eV, 4 eV y 6 eV.")
build(
    O4, 3, F,
    use="Aprenderé el modelo del fotón y de los niveles de energía, y lo usaré para explicar el efecto fotoeléctrico y la emisión de luz de un átomo.",
    prior=["Sé que la luz puede describirse como onda.", "Sé qué es la energía y que se mide en unidades.", "Sé restar y comparar números enteros."],
    explain=[
        "En la mecánica cuántica la energía no siempre varía de forma continua: se intercambia en paquetes llamados cuantos. Einstein propuso que la luz está formada por fotones, cada uno con energía E = h × f, donde f es la frecuencia de la luz y h la constante de Planck. A mayor frecuencia, mayor energía por fotón. La intensidad de la luz indica cuántos fotones llegan por segundo, no cuánta energía lleva cada uno.",
        "En el efecto fotoeléctrico, la luz libera electrones de un metal solo si la energía de cada fotón es al menos igual a la energía mínima W del metal. Si es menor, no se libera ningún electrón aunque la luz sea muy intensa. Si es mayor, el sobrante es la energía cinética del electrón: E cinética = E fotón − W. La física clásica de ondas esperaba que una luz intensa de cualquier frecuencia bastara, y los experimentos mostraron lo contrario.",
        "En un átomo los electrones solo pueden ocupar ciertos niveles de energía. Al pasar de un nivel superior a uno inferior, el átomo emite un fotón con la diferencia de energías; para subir, absorbe un fotón de esa diferencia exacta. Además, la luz y las partículas muestran un comportamiento dual: según el experimento se manifiestan como onda (difracción) o como partícula (choques individuales). Este modelo tiene límites: describe energías, pero no dice dónde está el electrón en cada instante.",
    ],
    vocab=[("fotón", "paquete de energía de la luz, E = h × f"), ("cuanto", "cantidad mínima de energía que se intercambia"), ("efecto fotoeléctrico", "emisión de electrones de un metal por luz de frecuencia suficiente"), ("nivel de energía", "valor permitido de energía de un electrón en un átomo"), ("electronvoltio (eV)", "unidad de energía a escala atómica"), ("dualidad onda-partícula", "comportamiento de onda o de partícula según el experimento")],
    worked=[
        ("Efecto fotoeléctrico", "Un metal ficticio tiene W = 3 eV. Llega luz con fotones de 5 eV. ¿Se liberan electrones y con qué energía cinética?", ["Compara: 5 eV es mayor que 3 eV, así que sí se liberan.", "Energía cinética: 5 − 3."], "Sí, con 2 eV de energía cinética"),
        ("Fotón emitido", "Un átomo ficticio con niveles de 0, 3 y 7 eV. Un electrón baja del nivel de 7 al de 3 eV. ¿Qué energía tiene el fotón emitido?", ["La energía del fotón es la diferencia entre niveles.", "7 − 3."], "4 eV"),
    ],
    mistakes=[("Creer que una luz más intensa siempre libera electrones.", "Se confunde cantidad de fotones con energía de cada fotón.", "Compara primero la energía de un fotón con W."),
              ("Creer que el electrón en un átomo puede tener cualquier energía intermedia.", "Se aplica la idea continua de la física clásica.", "Solo valen los niveles permitidos.")],
    T=[
        ("abc", "En el modelo del fotón, la energía de cada fotón depende de", "la frecuencia de la luz", "la intensidad de la luz", "el tamaño del metal", "Se cumple E = h × f: a mayor frecuencia, mayor energía por fotón."),
        ("abc", "En el efecto fotoeléctrico, ¿qué pasa si la energía de cada fotón es menor que W?", "No se liberan electrones, aunque la luz sea muy intensa", "Se liberan electrones si la luz es intensa", "Se libera uno por cada hora de exposición", "Un electrón absorbe un solo fotón: si no alcanza W, no sale."),
        ("ab", "Aumentar la intensidad de una luz sin cambiar su frecuencia aumenta", "el número de fotones por segundo", "la energía de cada fotón", "La intensidad indica cuántos fotones llegan, y no cuánta energía lleva cada uno."),
        ("abc", "{F} ¿Qué luces liberan electrones del metal ficticio?", "Luz 2 y luz 3", "Solo luz 1", "Solo luz 3", "Los fotones de 3 eV y 5 eV superan W = 2 eV; los de 1 eV no."),
        ("=", "{F} Con luz 3, ¿cuántos eV de energía cinética tiene cada electrón liberado? (E cinética = E fotón − W)", "5-2", "Se resta W a la energía del fotón.", " eV"),
        ("abc", "¿Por qué el efecto fotoeléctrico fue difícil de explicar con la física clásica de ondas?", "Porque predecía que una luz intensa de cualquier frecuencia liberaría electrones y los experimentos mostraron que no", "Porque la luz no existe", "Porque los electrones no tienen carga", "Los datos mostraban un umbral de frecuencia."),
        ("=", "{F} Con luz 2, ¿cuántos eV de energía cinética tiene cada electrón liberado?", "3-2", "Se resta W a la energía del fotón de 3 eV.", " eV"),
        ("=", "{F} Un electrón del átomo ficticio baja del nivel de 6 eV al de 4 eV. ¿Cuántos eV tiene el fotón emitido?", "6-4", "La energía del fotón es la diferencia entre niveles.", " eV"),
        ("=", "{F} ¿Qué energía, en eV, debe tener un fotón para subir un electrón del nivel de 0 eV al de 4 eV?", "4-0", "El fotón absorbido tiene la diferencia entre niveles.", " eV"),
        ("abc", "{F} Una luz con fotones de 1 eV se vuelve 100 veces más intensa. ¿Libera electrones en el metal ficticio?", "No: cada fotón sigue teniendo solo 1 eV", "Sí: ahora hay mucha energía total", "Sí, pero solo la mitad de los electrones", "La energía individual del fotón no cambia con la intensidad."),
        ("abc", "{F} ¿Qué fotón podría ser absorbido por un electrón del nivel de 0 eV del átomo ficticio para subir exactamente a un nivel permitido?", "Uno de 4 eV", "Uno de 5 eV", "Uno de 3 eV", "Solo se absorben fotones cuya energía coincide con la diferencia entre niveles: 4 o 6 eV."),
        ("abc", "Un estudiante dice: «como hay niveles de energía, el electrón puede tener cualquier energía entre 0 y 6 eV». ¿Qué falla?", "Solo puede ocupar los niveles permitidos, sin valores intermedios", "Nada: la energía es continua", "Que el electrón no tiene energía", "La cuantización significa que solo ciertos valores son posibles."),
        ("abc", "La luz muestra difracción (como onda) y también choques individuales con electrones (como partícula). ¿Cómo lo resume la física moderna?", "Tiene comportamiento dual: según el experimento se manifiesta como onda o como partícula", "Es solo una onda", "Es solo una partícula", "Ambos aspectos se necesitan para explicar todos los resultados."),
    ],
    ctx=("=", "Una celda solar ficticia usa un material que necesita 1 eV para liberar un electrón. Llega un fotón de 3 eV. ¿Cuántos eV de energía cinética tiene el electrón liberado?", "3-1", "Se resta la energía mínima a la energía del fotón.", " eV"),
    sc=[
        ("En Física moderna: ¿de qué depende la energía de un fotón?", "De su frecuencia", "Se calcula con E = h × f."),
        ("¿Qué indica la intensidad de la luz?", "Cuántos fotones llegan por segundo", "No cambia la energía de cada fotón."),
        ("Si un electrón baja de 9 eV a 4 eV, ¿qué energía tiene el fotón emitido?", "5 eV", "Es la diferencia entre niveles: 9 − 4."),
    ],
    op=("Elige un metal ficticio. Metal 1: W = 3 eV. Metal 2: W = 4 eV. Lo iluminan luces de fotones de 2 eV, 4 eV y 6 eV. Para cada luz di si libera electrones y calcula su energía cinética. Después escribe qué pasaría si la luz de 2 eV se volviera mil veces más intensa y por qué.",
        "Metal 1 (W = 3 eV): 2 eV, no libera; 4 eV, sí, 1 eV de energía cinética; 6 eV, sí, 3 eV. Con la luz de 2 eV mil veces más intensa seguiría sin liberar electrones, porque cada fotón tiene 2 eV, menos que W.",
        ["compara cada fotón con W", "calcula la energía cinética cuando corresponde", "explica el efecto de la intensidad"],
        ["hoja con una tabla de tres filas y la explicación final"],
        ["liberar electrones solo por la intensidad", "restar al revés", "olvidar las unidades"],
        "Pregunta: «¿cuánta energía lleva un solo fotón y cuánta necesita el electrón?»."),
    reinforce="Con la ficha, dibuja los tres niveles del átomo y marca con flechas las transiciones posibles y la energía de cada fotón.",
    extend="Explica por qué la existencia de un umbral de frecuencia apoya la idea de que la luz tiene un aspecto de partículas.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (de ejemplo, cifras aproximadas). E = m × c², con c² ≈ 9 × 10^16 m²/s² (c ≈ 3 × 10^8 m/s); 10^16 es un 1 seguido de 16 ceros. 1 g = 0,001 kg. "
     "Luz: recorre unos 300 m en una millonésima de segundo (1 µs). Tecnologías y teorías: sistema de posicionamiento satelital (relatividad), láser y transistor (cuántica), paneles fotovoltaicos (efecto fotoeléctrico).")
build(
    O4, 4, F,
    use="Aprenderé a analizar cómo la relatividad y la cuántica se relacionan con tecnologías actuales y a evaluar sus beneficios y riesgos para la sociedad y los sistemas naturales.",
    prior=["Sé qué es el efecto fotoeléctrico y la dilatación del tiempo.", "Sé usar potencias de 10 de forma simple.", "Sé comparar beneficios y riesgos."],
    explain=[
        "La física moderna sostiene tecnologías de uso diario. Los transistores de los chips y los láseres se basan en la mecánica cuántica de los materiales y de la luz. Los paneles fotovoltaicos aprovechan que la luz libera electrones en un material, idea cercana al efecto fotoeléctrico. El sistema de posicionamiento satelital necesita correcciones relativistas: sin ellas, un reloj de satélite que se adelanta decenas de millonésimas de segundo por día acumularía errores de posición de varios kilómetros diarios.",
        "La relación E = m × c² dice que la masa es una forma de energía: una masa pequeña equivale a una energía muy grande, porque c² es enorme. Por ejemplo, 1 g (0,001 kg) tiene una energía equivalente a 0,001 × 9 × 10^16 = 9 × 10^13 J. En las reacciones nucleares una pequeña parte de la masa se transforma en energía. Esto permite producir mucha energía eléctrica con bajas emisiones de CO2 durante su operación, pero también plantea riesgos de accidentes, residuos radiactivos y usos bélicos.",
        "Evaluar el impacto implica mirar sociedad, tecnología y sistemas naturales: beneficios (medicina, comunicaciones, energía), riesgos (radiación, residuos, desigualdad de acceso) y quiénes deciden. Una buena evaluación usa evidencia, distingue entre hechos y valoraciones y evita extrapolar la física atómica a la vida cotidiana sin pruebas, como decir que «la cuántica demuestra que el pensamiento controla la realidad». La investigación básica, pensada para entender la naturaleza, produjo después muchas aplicaciones.",
    ],
    vocab=[("E = m × c²", "relación entre la masa y la energía equivalente"), ("fotovoltaico", "que produce corriente eléctrica a partir de la luz"), ("semiconductor", "material cuyo comportamiento eléctrico se controla, base de los chips"), ("residuo radiactivo", "material que sigue emitiendo radiación y debe almacenarse con seguridad"), ("investigación básica", "investigación orientada a entender la naturaleza, sin una aplicación fija"), ("extrapolar", "aplicar una idea fuera del rango donde se probó")],
    worked=[
        ("Energía de una masa", "Una masa ficticia de 2 g se transforma por completo en energía. ¿Cuánta energía es? (c² = 9 × 10^16)", ["2 g = 0,002 kg.", "0,002 × 9 × 10^16 = 18 × 10^13 = 1,8 × 10^14."], "1,8 × 10^14 J"),
        ("Error por un reloj", "Un reloj de satélite se adelanta 10 µs. Si la luz recorre 300 m por µs, ¿qué error de distancia produce?", ["Multiplica el tiempo por el recorrido de la luz por µs.", "10 × 300 = 3.000."], "3.000 m"),
    ],
    mistakes=[("Extrapolar una idea de la escala atómica a la vida cotidiana sin evidencia.", "Se usan palabras de la cuántica fuera de su contexto.", "Pregunta qué experimento respalda la afirmación y a qué escala."),
              ("Valorar una tecnología solo por sus beneficios o solo por sus riesgos.", "Se mira un único criterio.", "Haz una tabla con beneficios, riesgos y quiénes se ven afectados.")],
    T=[
        ("abc", "¿Qué ecuación relaciona masa y energía en la relatividad?", "E = m × c²", "E = m × g × h", "F = m × a", "La relación E = m c² dice que la masa equivale a energía."),
        ("abc", "¿Qué teoría explica el funcionamiento del láser y de los transistores?", "La mecánica cuántica", "La mecánica clásica de Newton", "La teoría geocéntrica", "Ambos dependen de los niveles de energía y del comportamiento de electrones y luz."),
        ("ab", "El sistema de posicionamiento satelital necesita correcciones de", "relatividad", "mecánica clásica sin correcciones", "Los relojes de los satélites se desfasan por efectos relativistas."),
        ("abc", "{F} ¿Qué representa m en E = m × c²?", "La masa que se transforma en energía", "La velocidad del satélite", "La distancia recorrida", "Es la masa que se convierte en energía."),
        ("abc", "¿Por qué los paneles fotovoltaicos se relacionan con la física moderna?", "Porque aprovechan que la luz libera electrones en un material, idea cercana al efecto fotoeléctrico", "Porque usan reactores nucleares", "Porque funcionan solo de noche", "La liberación de electrones por fotones es un fenómeno cuántico."),
        ("abc", "La física moderna también trae riesgos. ¿Cuál es un ejemplo correcto?", "La energía nuclear exige manejar residuos radiactivos y evitar accidentes", "Los riesgos no existen", "Solo afectan a los satélites", "Toda tecnología poderosa debe evaluarse también por sus riesgos."),
        ("{F} Una masa de 4 g (0,004 kg) se transforma por completo en energía. ¿Cuántos J se liberan? Responde en la forma 36 × 10^n.", "36 × 10^13 J", "0,004 × 9 × 10^16 = 36 × 10^13, que también se escribe 3,6 × 10^14."),
        ("{F} Una masa de 3 g se transforma por completo en energía. Con c² ≈ 9 × 10^16, ¿cuántos J son? Responde en la forma 27 × 10^n.", "27 × 10^13 J", "0,003 × 9 × 10^16 = 27 × 10^13, que también se escribe 2,7 × 10^14."),
        ("=", "{F} Un reloj de satélite se adelanta 40 µs en un día (cifra de ejemplo). ¿Qué error de distancia, en m, produciría?", "40*300", "Se multiplica el tiempo por los 300 m que recorre la luz en cada µs.", " m"),
        ("abc", "Una persona dice: «la energía nuclear es siempre mala» y otra «siempre buena». ¿Cuál es la evaluación más razonable?", "Tiene beneficios (mucha energía con bajas emisiones de CO2 durante su operación) y riesgos (residuos, accidentes) que deben pesarse con evidencia", "Solo tiene riesgos", "Solo tiene beneficios", "Una evaluación honesta compara beneficios y riesgos con datos."),
        ("abc", "Un titular dice: «La física cuántica demuestra que tu pensamiento controla la realidad». ¿Qué problema tiene?", "Extrapola de forma no respaldada una idea de la escala atómica a la vida cotidiana", "Ninguno, porque está demostrado", "Que usa la palabra «física»", "No hay evidencia que apoye ese paso desde el nivel atómico."),
        ("abc", "Se discute si financiar una investigación sobre materiales cuánticos. ¿Qué argumento histórico apoya valorar la investigación básica?", "Aplicaciones como el transistor y el láser surgieron de preguntas sobre cómo funciona la materia a escala atómica", "La investigación básica nunca produce aplicaciones", "Solo importa la que da ganancias en un año", "Muchas tecnologías clave nacieron de preguntas básicas."),
        ("abc", "{F} Si en un cálculo de ejemplo la masa transformada fuera 10 veces mayor, la energía liberada sería", "10 veces mayor", "100 veces mayor", "igual", "E es proporcional a la masa en E = m × c²."),
    ],
    ctx=("abc", "Una comunidad ficticia evalúa instalar paneles fotovoltaicos. ¿En qué fenómeno de la física moderna se basa su funcionamiento?", "En la liberación de electrones de un material por la luz", "En reacciones de fisión de uranio", "En la dilatación del tiempo", "Un fotón con energía suficiente libera un electrón, y eso produce corriente."),
    sc=[
        ("En Física moderna: ¿qué dice E = m × c²?", "Que masa y energía son equivalentes", "Una masa pequeña equivale a mucha energía."),
        ("¿Qué teoría necesita el sistema de posicionamiento satelital para corregir sus relojes?", "La relatividad", "Los relojes en órbita se desfasan por efectos relativistas."),
        ("¿Basta mirar solo los beneficios de una tecnología para evaluarla?", "No", "También se revisan riesgos y a quiénes afectan."),
    ],
    op=("Elige una tecnología: sistema de posicionamiento satelital, láser médico, paneles fotovoltaicos o central nuclear. Escribe (a) qué idea de la física moderna usa, (b) dos beneficios, (c) dos riesgos o límites, (d) quién se ve afectado y (e) una decisión que tomarías con las evidencias que tienes, señalando qué más necesitarías saber.",
        "Paneles fotovoltaicos: (a) la luz libera electrones en un material. (b) Producen electricidad sin emisiones de CO2 durante su operación; se instalan en techos. (c) Dependen de la luz solar; su fabricación y su desecho requieren manejo. (d) Hogares y empresas. (e) Los instalaría en techos y exigiría un plan de reciclaje; necesitaría datos de costos.",
        ["nombra la idea física", "da beneficios y riesgos específicos", "justifica una decisión y declara qué falta saber"],
        ["hoja con las partes (a) a (e)"],
        ["decir solo beneficios", "afirmar sin evidencia", "mezclar tecnologías"],
        "Pregunta: «¿a quién beneficia y a quién podría perjudicar tu decisión?»."),
    reinforce="Con la ficha, calcula cuántos J libera la transformación completa de 5 g de masa y escribe el resultado en la forma 45 × 10^n.",
    extend="Explica por qué una investigación básica sobre el átomo pudo terminar produciendo tecnologías como los chips.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (de ejemplo). Una muestra ficticia tiene 800 átomos radiactivos de un tipo con vida media de 10 minutos: cada 10 minutos decae la mitad de los átomos que quedan sin decaer. "
     "Para un átomo individual solo se puede dar una probabilidad de decaer en cada intervalo.")
build(
    O4, 5, F,
    use="Aprenderé a comparar modelos y posturas de la física moderna sobre lo predecible y lo probable, y a decidir qué teoría usar según el fenómeno.",
    prior=["Sé que la cuántica describe lo muy pequeño.", "Sé calcular mitades sucesivas.", "Sé qué es una probabilidad."],
    explain=[
        "En la física clásica, si se conocen las condiciones iniciales, se puede predecir con certeza el resultado (determinismo). En la mecánica cuántica, para un sistema individual solo se pueden predecir probabilidades de los resultados de una medición. Un ejemplo es el decaimiento radiactivo: no se puede saber cuándo decaerá un átomo en particular, pero en una muestra grande, la vida media indica el tiempo en que decae la mitad de los átomos. Así, el comportamiento del conjunto es muy predecible aunque el de cada átomo no lo sea.",
        "La interpretación de la mecánica cuántica es un debate abierto: ¿las propiedades existen antes de medirse?, ¿la probabilidad es una limitación nuestra o una característica de la naturaleza? Distintas interpretaciones hacen las mismas predicciones medibles hoy; se dice que son empíricamente equivalentes, por lo que ningún experimento actual permite decidir entre ellas. Avanzar de forma científica exige buscar predicciones distintas que puedan contrastarse.",
        "Al comparar teorías para un problema se usan criterios: el rango de validez (escala y rapidez), la precisión de sus predicciones y la simplicidad del cálculo. Para el movimiento de una piedra o de un puente basta la mecánica clásica; para un electrón en un átomo se usa la cuántica; para rapideces cercanas a c se usa la relatividad. Elegir el modelo más simple que sea suficientemente preciso es una decisión razonable, y debe declararse su límite.",
    ],
    vocab=[("determinismo", "idea de que las condiciones iniciales fijan el resultado con certeza"), ("probabilidad", "medida de qué tan posible es un resultado"), ("vida media", "tiempo en que decae la mitad de los átomos radiactivos de una muestra"), ("interpretación", "explicación de lo que significa una teoría"), ("empíricamente equivalentes", "con las mismas predicciones medibles"), ("rango de validez", "condiciones en que una teoría funciona bien")],
    worked=[
        ("Vida media", "Una muestra ficticia de 640 átomos tiene vida media de 5 minutos. ¿Cuántos quedan a los 15 minutos?", ["15 minutos son 3 vidas medias.", "640 ÷ 2 = 320; 320 ÷ 2 = 160; 160 ÷ 2 = 80."], "80 átomos"),
        ("Elegir teoría", "Para calcular la trayectoria de una pelota lanzada por una persona, ¿conviene usar mecánica clásica o cuántica?", ["La pelota es cotidiana y lenta frente a la luz.", "La mecánica clásica es suficiente y más simple."], "Mecánica clásica"),
    ],
    mistakes=[("Creer que si cada átomo es impredecible, la muestra completa también lo es.", "Se confunde un caso individual con el comportamiento de muchos.", "Distingue entre predicción individual (probabilidad) y colectiva (ley estadística)."),
              ("Creer que cada 10 minutos decae la misma cantidad de átomos.", "Se confunde mitad de los que quedan con mitad de los iniciales.", "Divide por 2 la cantidad que queda en cada paso.")],
    T=[
        ("abc", "La vida media de una muestra radiactiva es", "el tiempo en que decae la mitad de sus átomos", "el tiempo en que decaen todos", "la duración de la vida de un átomo individual", "Se define como el tiempo en que decae la mitad de los átomos."),
        ("abc", "Según la mecánica cuántica, el resultado de una medición individual suele predecirse", "solo como probabilidades", "siempre con certeza total", "nunca, ni siquiera con probabilidades", "La teoría entrega probabilidades de cada resultado."),
        ("ab", "En una muestra grande de átomos radiactivos, el comportamiento del conjunto es", "predecible, aunque el de cada átomo no lo sea", "tan impredecible como el de cada átomo", "Con muchos átomos aparece una ley estadística clara."),
        ("=", "{F} ¿Cuántos átomos quedan sin decaer tras 10 minutos?", "800//2", "En una vida media decae la mitad.", " átomos"),
        ("abc", "¿Qué significa que dos interpretaciones de la mecánica cuántica sean empíricamente equivalentes?", "Que hacen las mismas predicciones medibles, por lo que los experimentos actuales no permiten decidir entre ellas", "Que son idénticas en todo", "Que ambas son falsas", "Coinciden en lo medible aunque difieran en su explicación."),
        ("abc", "El debate sobre la naturaleza de la realidad en física moderna incluye la pregunta de si", "las propiedades de un sistema existen antes de medirlas o solo se definen al medir", "los instrumentos tienen suficiente precisión", "las ecuaciones se escriben con letras", "Es una cuestión de interpretación sobre qué es una propiedad física."),
        ("=", "{F} ¿Cuántos átomos quedan sin decaer tras 30 minutos?", "800//2//2//2", "En 30 minutos pasan 3 vidas medias y se divide por 2 tres veces.", " átomos"),
        ("=", "Otra muestra de 960 átomos tiene vida media de 5 minutos. ¿Cuántos átomos quedan tras 20 minutos?", "960//2//2//2//2", "En 20 minutos pasan 4 vidas medias.", " átomos"),
        ("=", "{F} ¿Cuántos átomos habrán decaído tras 20 minutos?", "800-800//4", "Quedan 200; los que decayeron son los 800 iniciales menos los que quedan.", " átomos"),
        ("abc", "Un estudiante afirma: «si la mitad decae en 10 minutos, toda la muestra decae en 20 minutos». ¿Qué falla?", "Cada 10 minutos decae la mitad de los que quedan, no la misma cantidad", "Nada: decae el resto en el segundo intervalo", "Que 10 minutos es demasiado poco", "Tras 20 minutos aún quedan 200 de los 800 átomos."),
        ("abc", "Dos profesores discuten dos interpretaciones de la cuántica. ¿Qué criterio permite avanzar de forma científica?", "Buscar una predicción distinta que pueda contrastarse con un experimento", "Votar la que tenga más partidarios", "Elegir la más antigua", "La ciencia decide con evidencia contrastable y no por votación o antigüedad."),
        ("abc", "Para calcular la caída de una piedra desde un balcón y el comportamiento de un electrón en un átomo, ¿qué modelos conviene usar y por qué?", "Clásico para la piedra y cuántico para el electrón, porque cada uno funciona en su escala", "Cuántico para ambos", "Relatividad para ambos", "Cada teoría tiene su rango de validez y se elige el modelo más simple suficiente."),
        ("abc", "{F} Un reportaje dice: «es imposible predecir cuándo decaerá la muestra de la ficha, porque la cuántica es puro azar». ¿Cómo se corrige?", "Para un átomo solo hay probabilidad, pero el conjunto grande sigue una ley estadística (la vida media)", "No se corrige: no se puede predecir nada", "No se corrige: se puede predecir cada átomo con exactitud", "Los comportamientos colectivos son muy predecibles."),
    ],
    ctx=("abc", "Un museo ficticio debe elegir entre dos paneles. Panel 1: «Los átomos son impredecibles y nada se puede calcular». Panel 2: «Para un átomo solo hay probabilidades y para muchos átomos hay leyes estadísticas precisas». ¿Cuál es más fiel a lo estudiado?", "El panel 2", "El panel 1", "Ninguno de los dos", "El panel 2 distingue entre lo individual y lo colectivo."),
    sc=[
        ("En Física moderna: ¿qué es la vida media?", "El tiempo en que decae la mitad de los átomos de una muestra", "Se aplica a conjuntos de átomos y no a uno solo."),
        ("¿Con qué teoría se calcula la trayectoria de una pelota lanzada a mano?", "Con la mecánica clásica", "Es suficiente y más simple en esa escala."),
        ("Si hay 400 átomos y la vida media es 6 minutos, ¿cuántos quedan a los 12 minutos?", "100", "Pasan dos vidas medias y se divide por 2 dos veces."),
    ],
    op=("Elige una discusión. Discusión 1: una persona dice «la cuántica prueba que nada es predecible». Discusión 2: otra dice «con la relatividad ya no sirve la mecánica de Newton». Evalúa la afirmación con tres pasos: qué parte es correcta, qué parte es exagerada y qué ejemplo de esta clase lo muestra (usa la vida media o la elección de teoría según la escala). Escribe una versión corregida de la frase.",
        "Discusión 1: es correcto que para un átomo solo hay probabilidades; es exagerado decir que nada es predecible. Ejemplo: una muestra grande de átomos sigue la vida media. Frase corregida: «para un átomo solo hay probabilidades, pero el conjunto grande sigue leyes estadísticas precisas».",
        ["separa lo correcto de lo exagerado", "usa un ejemplo de la clase", "escribe una frase corregida"],
        ["hoja con los tres pasos y la frase corregida"],
        ["aceptar la frase completa", "rechazarla completa sin matices", "no usar un ejemplo"],
        "Pregunta: «¿qué teoría y qué escala aplican a tu ejemplo?»."),
    reinforce="Calcula cuántos átomos quedan de una muestra de 1.600 con vida media de 4 minutos después de 12 minutos.",
    extend="Explica por qué dos interpretaciones con las mismas predicciones pueden coexistir durante décadas en la ciencia.",
)
