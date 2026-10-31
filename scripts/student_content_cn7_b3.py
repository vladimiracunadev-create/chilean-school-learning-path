"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 13 (comportamiento de los gases)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA13 = "CN07 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 13, clase 1
register(
    OA13, 1,
    materials="Papel y lápiz. Para la tarea abierta: una botella plástica vacía con tapa y un globo. No uses calor ni objetos filosos.",
    use="Aprenderé a observar cómo los gases se comprimen y se expanden, y a nombrar las tres variables que los describen: presión, volumen y temperatura. Sirve para prepararme a estudiar las leyes de los gases.",
    prior=["Sé que un gas ocupa todo el espacio que tiene disponible.", "Conozco el modelo de partículas de los gases."],
    explain=[
        "Un gas se comprime cuando su volumen disminuye al aplicar una fuerza, y se expande cuando ocupa más espacio. En un gas hay mucho espacio vacío entre sus partículas, por eso se puede comprimir. Los líquidos y los sólidos casi no se comprimen. Un gas, además, llena todo el recipiente que lo contiene.",
        "Tres variables describen a un gas encerrado. El volumen (V) es el espacio que ocupa y se mide en litros (L). La presión (P) es la fuerza que el gas ejerce sobre cada unidad de superficie de las paredes del recipiente; la mediremos en atmósferas (atm). Esa fuerza nace de los choques de las partículas del gas contra las paredes. La temperatura (T) indica qué tan caliente está el gas. Además, importa la cantidad de gas: si no se escapa ni entra gas, la cantidad se mantiene.",
        "En Ciencias, un gas ideal es un modelo en el que las partículas son muy pequeñas, están muy separadas y no se atraen. Los gases reales se parecen a este modelo en condiciones cotidianas. Observa primero y recién después interpreta: «la botella se arruga» es una observación; «la presión de afuera es mayor» es una interpretación.",
    ],
    vocab=[("gas ideal", "modelo de gas con partículas muy pequeñas y muy separadas que no se atraen"), ("presión", "fuerza que el gas ejerce por cada unidad de superficie"), ("volumen", "espacio que ocupa el gas, en litros (L)"), ("compresión", "disminución del volumen de un gas al aplicar fuerza"), ("expansión", "aumento del volumen de un gas")],
    worked=[
        {"title": "Comprimir un gas", "problem": "Un gas ocupa 8 L en un cilindro. Se empuja el émbolo hasta que ocupa 2 L. ¿Cuántas veces menor es su volumen?", "steps": ["El volumen inicial es 8 L y el final es 2 L.", "8 ÷ 2 = 4."], "answer": "4 veces menor"},
        {"title": "Un gas llena el recipiente", "problem": "Un gas que ocupaba 2 L se pasa a un recipiente vacío de 10 L. ¿Cuánto volumen ocupa ahora?", "steps": ["Un gas se esparce por todo el espacio que tiene.", "Ocupa todo el recipiente disponible."], "answer": "10 L"},
    ],
    mistakes=[
        {"wrong": "Decir que al comprimir un gas hay menos gas.", "why": "Se confunde volumen con cantidad.", "fix": "Si no se escapa gas, la cantidad es la misma; solo ocupa menos espacio."},
        {"wrong": "Mezclar observación con interpretación: «la botella se arruga porque la presión de afuera es mayor».", "why": "Se anota una explicación como si fuera un dato.", "fix": "Anota primero «se arruga» y deja la explicación para después."},
    ],
    tiers={
        "recovery": [
            ex("Un gas, ¿ocupa solo una parte del recipiente o todo el recipiente?", "Todo el recipiente", "Las partículas del gas se esparcen por todo el espacio."),
            ex("Si se aprieta un gas y su volumen disminuye, ¿se llama compresión o expansión?", "Compresión", "Comprimir es reducir el volumen."),
            ex("Cuando se infla un globo, ¿el gas de su interior se comprime o se expande?", "Se expande", "Su volumen aumenta."),
        ],
        "understand": [
            ex("¿Por qué un gas se puede comprimir mucho más que un líquido?", "Porque entre sus partículas hay mucho espacio vacío", "Al apretar, las partículas se acercan."),
            ex("Frase: «El globo se infló hasta medir 24 cm de ancho». ¿Es una observación o una interpretación?", "Observación", "Es un dato medido."),
            ex("¿Qué variable del gas se relaciona con los choques de sus partículas contra las paredes: la presión o el volumen?", "La presión", "Los choques de las partículas contra la pared producen la presión."),
        ],
        "apply": [
            arith("Una bomba de bicicleta contiene 600 mL de aire y se comprime a 150 mL sin que se escape aire. ¿Cuántas veces menor es el volumen?", "600//150", "Se divide el volumen inicial por el final.", " veces"),
            arith("Un globo se infla desde 3 L hasta 9 L. ¿Cuántos litros aumentó su volumen?", "9-3", "Se resta el volumen inicial al final.", " L"),
            ex("Un gas de 5 L se pasa a un recipiente de 20 L vacío. ¿Qué volumen ocupa el gas ahora?", "20 L", "Un gas ocupa todo el recipiente que tiene."),
        ],
        "reason": [
            ex("Ema aprieta una botella cerrada y dice: «Hay menos aire ahora». Midió que el aire sigue siendo el mismo y la botella se achicó. ¿Qué error comete?", "Confunde menor volumen con menor cantidad de aire", "El aire solo ocupa menos espacio."),
            ex("Lucas dice que los gases no se pueden comprimir porque «el aire no se aprieta». ¿Qué observación lo contradice?", "El aire de una bomba de bicicleta se comprime", "Su volumen disminuye cuando se empuja."),
        ],
        "challenge": [
            ex("Un gas ideal tiene partículas muy separadas que casi no se atraen. ¿Un gas real se parece más a ese modelo cuando está muy comprimido o en condiciones cotidianas, como el aire de una pieza?", "En condiciones cotidianas", "Muy comprimido, las partículas están cerca y se atraen más."),
            ex("Un recipiente cerrado contiene 12 g de un gas. Se comprime sin que se escape y su volumen pasa de 6 L a 2 L. ¿Cuánto pesa el gas después?", "12 g", "La cantidad de gas no cambia al comprimirlo, solo cambia su volumen."),
        ],
    },
    context=[ex("Una persona de tu casa infla el neumático de una bicicleta con una bomba. Cada empuje mete más aire en un espacio pequeño. ¿Qué propiedad de los gases hace posible que quepa tanto aire?", "Que se pueden comprimir", "Al comprimirse, el mismo aire ocupa menos volumen.")],
    selfcheck=[
        ex("¿Cuáles son las tres variables que describen un gas?", "Presión, volumen y temperatura", "Son las variables de esta unidad."),
        ex("Si comprimes un gas sin dejar que escape, ¿cambia su cantidad?", "No", "Solo cambia su volumen."),
        ex("¿Qué es un gas ideal?", "Un modelo con partículas muy pequeñas y separadas que no se atraen", "Es una simplificación de los gases reales."),
    ],
    open_task=task(
        "Con una botella plástica vacía con tapa y un globo, haz dos observaciones. Primero, tapa la botella y aprieta suavemente con las manos: anota qué le pasa a su forma y qué sientes. Segundo, infla un globo y anota su ancho con una regla. Escribe una tabla con tres columnas: qué observo, qué variable del gas cambia (presión, volumen) y qué interpreto. Marca con O las observaciones y con I las interpretaciones.",
        "Botella tapada: O, se achica y la siento dura. Variable: volumen disminuye, presión aumenta. I, el aire se comprimió y empuja más las paredes.",
        ["dos observaciones", "variable nombrada", "marcas O e I"],
        ["tabla de tres columnas", "marcas O e I"],
        ["anotar la explicación como observación", "no nombrar la variable"],
        "Pregunta qué cambió en tu botella cuando la soltaste.",
    ),
    reinforce="Escribe dos observaciones sobre gases que hayas visto hoy y marca cuál es observación y cuál interpretación.",
    extend="Averigua con una persona de tu casa cómo se infla un neumático y por qué la bomba requiere fuerza al final.",
)

# ================================================================ OA 13, clase 2
register(
    OA13, 2,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé la relación entre presión y volumen de un gas a temperatura constante (ley de Boyle). Sirve para calcular cuánto cambia el volumen cuando cambia la presión.",
    prior=["Sé que la presión y el volumen son variables de un gas.", "Sé multiplicar, dividir y hacer tablas."],
    explain=[
        "La ley de Boyle dice que, si la temperatura y la cantidad de gas no cambian, el volumen de un gas es inversamente proporcional a su presión. Eso quiere decir que si la presión se duplica, el volumen se reduce a la mitad; si la presión se triplica, el volumen baja a la tercera parte.",
        "También se puede decir que el producto P × V es constante. Por ejemplo, un gas a 1 atm ocupa 12 L: 1 × 12 = 12. A 2 atm ocupa 6 L (2 × 6 = 12), a 3 atm ocupa 4 L (3 × 4 = 12) y a 4 atm ocupa 3 L (4 × 3 = 12). Para dos estados del mismo gas se cumple P1 × V1 = P2 × V2.",
        "Esta ley sirve para describir la bomba de aire, el aire en una jeringa o un globo que sube por la atmósfera, donde la presión baja y el volumen aumenta. Recuerda que los números de esta clase son de ejemplo y que la ley solo vale con temperatura constante.",
    ],
    vocab=[("ley de Boyle", "relación inversa entre presión y volumen de un gas a temperatura constante"), ("inversamente proporcional", "si una variable sube, la otra baja en la misma proporción"), ("constante", "que no cambia"), ("atmósfera (atm)", "unidad de presión, cercana a la presión del aire al nivel del mar"), ("producto", "resultado de multiplicar")],
    worked=[
        {"title": "Calcular el volumen final", "problem": "Un gas tiene 2 atm y 6 L. Se sube su presión a 4 atm sin cambiar la temperatura. ¿Cuál es el volumen?", "steps": ["P1 × V1 = 2 × 6 = 12.", "P2 × V2 = 4 × V2 = 12, entonces V2 = 3."], "answer": "3 L"},
        {"title": "Revisar una tabla", "problem": "Tabla: 1 atm, 12 L; 2 atm, 6 L; 3 atm, 4 L. ¿El producto P × V se mantiene constante?", "steps": ["1 × 12 = 12; 2 × 6 = 12; 3 × 4 = 12.", "Todos dan 12."], "answer": "Sí, el producto es 12"},
    ],
    mistakes=[
        {"wrong": "Pensar que al duplicar la presión se duplica el volumen.", "why": "Se confunde relación inversa con directa.", "fix": "Si la presión sube, el volumen baja."},
        {"wrong": "Usar la ley de Boyle cuando la temperatura cambia.", "why": "Se olvida la condición de temperatura constante.", "fix": "Comprueba que la temperatura y la cantidad de gas no cambian."},
    ],
    tiers={
        "recovery": [
            ex("Si la presión de un gas aumenta y la temperatura no cambia, ¿el volumen aumenta o disminuye?", "Disminuye", "Boyle: la relación es inversa."),
            ex("Si la presión de un gas se duplica, ¿qué pasa con su volumen?", "Se reduce a la mitad", "Es inversamente proporcional."),
            ex("¿Qué condición debe mantenerse constante para usar la ley de Boyle?", "La temperatura (y la cantidad de gas)", "La ley solo vale si no cambia la temperatura."),
        ],
        "understand": [
            ex("En una tabla de ejemplo, la fila 1 dice 1 atm y 20 L, y la fila 2 dice 2 atm y 10 L. ¿Qué valor tiene P × V en la fila 2 y es igual al de la fila 1?", "20; sí, es igual", "2 × 10 = 20 y 1 × 20 = 20: el producto se mantiene."),
            ex("Un globo sube por la atmósfera y la presión a su alrededor baja. Sin que cambie la temperatura, ¿su volumen aumenta o disminuye?", "Aumenta", "Si baja la presión, el volumen sube."),
            ex("Si la presión se triplica, ¿a qué fracción del volumen original baja el volumen?", "A la tercera parte", "El volumen es inversamente proporcional a la presión."),
        ],
        "apply": [
            arith("Una bomba de aire contiene 300 mL de aire a 1 atm. Se empuja hasta que la presión es 3 atm, con temperatura constante. ¿Cuántos mL de volumen tiene el aire?", "1*300//3", "Se usa P1 × V1 = P2 × V2.", " mL"),
            arith("Un gas ocupa 10 L a 2 atm. Si la presión sube a 5 atm, con la misma temperatura, ¿qué volumen ocupa?", "2*10//5", "Se calcula el producto inicial y se divide por la presión final.", " L"),
            arith("Un tanque de ejemplo tiene gas a 8 atm y 3 L. Al abrir una válvula la presión baja a 2 atm, con temperatura constante. ¿Qué volumen ocupa ese gas?", "8*3//2", "Se multiplica la presión inicial por el volumen inicial y se divide por la presión final.", " L"),
        ],
        "reason": [
            ex("María midió: 1 atm, 12 L; 2 atm, 6 L; 4 atm, 4 L. Sospecha que una medición es errónea. ¿Cuál es y qué volumen debería marcar?", "La de 4 atm; debería marcar 3 L", "Para 4 atm, 12 ÷ 4 = 3 L."),
            ex("Pedro dice: «Al duplicar la presión, el volumen también se duplica». ¿Cuál es su error?", "La relación es inversa, no directa", "Al duplicar la presión, el volumen baja a la mitad."),
        ],
        "challenge": [
            arith("Una burbuja bajo el agua, a 20 m de profundidad, está a 3 atm y mide 1 L (datos de ejemplo). Sube a la superficie, a 1 atm, y la temperatura no cambia. ¿Cuántos litros mide?", "3*1//1", "Se usa P1 × V1 = P2 × V2.", " L"),
            ex("Un estudiante usó la ley de Boyle con un gas que se calentó mientras cambiaba su presión. ¿Por qué su resultado no es confiable?", "Porque la temperatura cambió", "La ley solo vale a temperatura constante."),
        ],
    },
    context=[ex("Una persona usa una bomba de aire para inflar un colchón inflable. Cada vez que empuja el émbolo hasta el fondo, el aire pasa de un cilindro grande a un espacio pequeño. Si el aire pasa de 4 L a 1 L sin cambiar la temperatura, ¿cuántas veces aumenta su presión?", "4 veces", "Si el volumen baja a la cuarta parte, la presión sube 4 veces.")],
    selfcheck=[
        ex("Según la ley de Boyle, ¿qué producto es constante?", "P × V", "Presión por volumen se mantiene constante."),
        ex("Si el volumen se reduce a la mitad, ¿qué pasa con la presión?", "Se duplica", "La relación es inversa."),
        ex("¿Qué dos cosas deben mantenerse constantes para aplicar la ley de Boyle?", "La temperatura y la cantidad de gas", "Sin ellas no vale la ley."),
    ],
    open_task=task(
        "Completa esta tabla de ejemplo de un gas a temperatura constante. Fila 1: 1 atm, 24 L. Fila 2: 2 atm, ___ L. Fila 3: 3 atm, ___ L. Fila 4: 6 atm, ___ L. Calcula cada volumen con P × V = 24. Después escribe una predicción para 12 atm y explica con una frase por qué los números de volumen bajan.",
        "Fila 2: 12 L. Fila 3: 8 L. Fila 4: 4 L. Predicción para 12 atm: 2 L. Los volúmenes bajan porque, al subir la presión, el gas se comprime.",
        ["tabla completa", "volúmenes calculados con P × V = 24", "predicción para 12 atm"],
        ["tabla con los cálculos", "frase de explicación"],
        ["sumar en vez de multiplicar", "no usar la constante 24"],
        "Pregunta qué cambiaría en tu tabla si el gas tuviera 30 L a 1 atm.",
    ),
    reinforce="Inventa una tabla de cuatro filas para un gas que a 1 atm ocupe 18 L y comprueba que P × V es constante.",
    extend="Averigua con una persona de tu casa por qué una bomba de bicicleta se siente más dura de empujar al final, y explícalo con la ley de Boyle.",
)

# ================================================================ OA 13, clase 3
register(
    OA13, 3,
    materials="Papel y lápiz. Para la tarea abierta: un globo, una botella plástica limpia y un recipiente con agua tibia y otro con agua fría. El agua tibia debe poder tocarse con la mano sin quemar, y una persona adulta debe estar presente.",
    use="Aprenderé cómo cambia el volumen o la presión de un gas cuando cambia su temperatura (leyes de Charles y de Gay-Lussac). Sirve para predecir y para entender por qué no se deben calentar recipientes cerrados.",
    prior=["Conozco la ley de Boyle.", "Sé sumar, multiplicar y dividir enteros."],
    explain=[
        "Para trabajar con gases se usa la temperatura absoluta, medida en kelvin (K). Se convierte así: K = °C + 273. Por ejemplo, 27 °C son 300 K. Se usa esta escala porque en ella el 0 K es la menor temperatura posible y las proporciones funcionan bien.",
        "La ley de Charles dice que, a presión constante, el volumen de un gas es directamente proporcional a su temperatura en kelvin: V1 ÷ T1 = V2 ÷ T2. Si la temperatura en kelvin se duplica, el volumen se duplica. La ley de Gay-Lussac dice que, si el volumen es constante, la presión es directamente proporcional a la temperatura en kelvin: P1 ÷ T1 = P2 ÷ T2. Si la temperatura en kelvin se duplica, la presión se duplica.",
        "Esto explica por qué un recipiente cerrado y rígido no debe calentarse: la presión sube y puede reventar. Nunca calientes recipientes cerrados ni aerosoles. En la tarea abierta solo se usa agua tibia.",
    ],
    vocab=[("kelvin (K)", "unidad de temperatura absoluta; K = °C + 273"), ("ley de Charles", "relación directa entre volumen y temperatura en K a presión constante"), ("ley de Gay-Lussac", "relación directa entre presión y temperatura en K a volumen constante"), ("directamente proporcional", "si una variable sube, la otra sube en la misma proporción"), ("rígido", "que no cambia su forma ni su volumen")],
    worked=[
        {"title": "Convertir a kelvin", "problem": "Un gas está a 27 °C. ¿Cuántos kelvin son?", "steps": ["K = °C + 273.", "27 + 273 = 300."], "answer": "300 K"},
        {"title": "Charles con números", "problem": "Un gas ocupa 4 L a 200 K. Se calienta a 400 K, con presión constante. ¿Qué volumen ocupa?", "steps": ["La temperatura en kelvin se duplicó.", "Entonces el volumen se duplicó: 4 × 2 = 8."], "answer": "8 L"},
    ],
    mistakes=[
        {"wrong": "Concluir que de 20 °C a 40 °C el volumen se duplica.", "why": "Se usa la escala Celsius para la proporción.", "fix": "Convierte a kelvin: 293 K a 313 K no es el doble."},
        {"wrong": "Calentar una botella cerrada para ver qué pasa.", "why": "No se considera el riesgo de que la presión aumente.", "fix": "Nunca se calientan recipientes cerrados; usa solo agua tibia y un adulto."},
    ],
    tiers={
        "recovery": [
            ex("Si la temperatura de un gas sube, con presión constante, ¿el volumen aumenta o disminuye?", "Aumenta", "Charles: el volumen es directamente proporcional a la temperatura en K."),
            ex("En un recipiente rígido cerrado la temperatura del gas sube. ¿La presión aumenta o disminuye?", "Aumenta", "Gay-Lussac: la presión sube con la temperatura."),
            arith("Convierte 7 °C a kelvin con la regla K = °C + 273.", "7+273", "Se suma 273 a la temperatura en Celsius.", " K"),
        ],
        "understand": [
            ex("¿Por qué las leyes de los gases se calculan con kelvin y no con °C?", "Porque el 0 K es la menor temperatura posible y las proporciones funcionan con esa escala", "Con la escala Celsius las proporciones no se cumplen."),
            ex("Dos leyes: A relaciona V y T con P constante; B relaciona P y T con V constante. ¿Cuál es la ley de Charles?", "A", "Charles relaciona volumen y temperatura."),
            ex("Si la temperatura en kelvin de un gas se triplica con volumen constante, ¿qué pasa con su presión?", "Se triplica", "Es directamente proporcional."),
        ],
        "apply": [
            arith("Un globo tiene 6 L a 300 K. Se calienta a 450 K, a presión constante. ¿Cuántos litros ocupa?", "6*450//300", "Se multiplica el volumen inicial por la razón entre las temperaturas.", " L"),
            arith("Un recipiente rígido de ejemplo tiene gas a 2 atm y 250 K. Si la temperatura sube a 500 K, ¿qué presión alcanza?", "2*500//250", "Se multiplica la presión inicial por la razón entre las temperaturas.", " atm"),
            arith("Un gas está a −73 °C. ¿Cuántos kelvin son?", "-73+273", "Se suma 273, aun con temperatura negativa.", " K"),
        ],
        "reason": [
            ex("Ana dice: «Si el gas pasa de 20 °C a 40 °C, su volumen se duplica». ¿Cuál es el error?", "Debe convertir a kelvin: 293 K a 313 K no es el doble", "Las leyes de los gases usan la escala Kelvin."),
            ex("Un aerosol cerrado dice «no exponer al calor». ¿Qué ley explica el riesgo?", "Gay-Lussac: al subir la temperatura sube la presión en un envase rígido", "La presión creciente puede reventar el envase."),
        ],
        "challenge": [
            ex("Un envase rígido tiene gas a 2 atm y 300 K y se calienta a 600 K. ¿Qué presión alcanza y por qué esto es peligroso?", "4 atm; el envase podría reventar", "La presión se duplicó con un volumen que no puede aumentar."),
            arith("Un envase rígido cerrado de ejemplo tiene gas a 4 atm y 400 K, y se deja enfriar hasta 200 K. ¿Qué presión alcanza el gas?", "4*200//400", "La presión es directamente proporcional a la temperatura en kelvin.", " atm"),
        ],
    },
    context=[ex("Una persona deja una botella plástica cerrada con aire dentro de un auto bajo el sol de verano. Según Gay-Lussac, ¿qué pasa con la presión del aire dentro de la botella?", "Aumenta", "Al subir la temperatura sube la presión del aire encerrado.")],
    selfcheck=[
        ex("¿Cuál es la regla para pasar de °C a K?", "K = °C + 273", "Se suma 273."),
        ex("¿Qué dos variables relaciona la ley de Charles?", "Volumen y temperatura", "A presión constante."),
        ex("¿Se puede calentar un recipiente cerrado?", "No", "La presión puede aumentar y reventarlo."),
    ],
    open_task=task(
        "Con ayuda de una persona adulta, coloca un globo en la boca de una botella plástica limpia. Pon la botella en agua fría y luego en agua tibia (que puedas tocar). Anota en cada caso qué ve que le pasa al globo. Después responde: qué variable del gas cambió, cuál se mantuvo constante, y cuál ley explica lo observado. Registra una limitación, por ejemplo que el globo no se ajusta perfectamente.",
        "En agua fría el globo se mete un poco o se arruga; en agua tibia se infla. Cambió la temperatura y el volumen del aire; la presión casi no. Ley de Charles. Limitación: el globo no sella perfecto.",
        ["dos observaciones", "variable que cambia y variable constante", "ley nombrada"],
        ["registro del globo en agua fría y tibia", "ley mencionada"],
        ["usar agua hirviendo", "no mencionar qué variable se mantiene constante"],
        "Pregunta cómo cambiaría el resultado si el agua tibia estuviera aún más tibia.",
    ),
    reinforce="Convierte a kelvin 0 °C, 25 °C y 100 °C.",
    extend="Averigua con una persona de tu casa por qué los envases de aerosol traen la advertencia de no exponerlos al calor.",
)

# ================================================================ OA 13, clase 4
register(
    OA13, 4,
    materials="Papel y lápiz. Los dibujos de partículas se describen con palabras; puedes hacerlos con puntos.",
    use="Aprenderé la teoría cinético-molecular y a usarla para explicar las leyes de los gases con partículas. Sirve para entender por qué los gases se comportan así.",
    prior=["Conozco las leyes de Boyle, Charles y Gay-Lussac.", "Sé que un modelo explica lo que no se ve."],
    explain=[
        "La teoría cinético-molecular dice que un gas está formado por partículas muy pequeñas y muy separadas, que se mueven sin parar en todas direcciones y chocan entre sí y con las paredes. Casi no se atraen. La energía de movimiento de las partículas es mayor cuanto mayor es la temperatura en kelvin. Un gas ideal cumple de forma exacta estas ideas.",
        "Con este modelo se explican las leyes. La presión es el resultado de los choques de las partículas contra las paredes: más choques por segundo o choques más fuertes, más presión. En la ley de Boyle, si el volumen se reduce a la mitad, las partículas chocan el doble de veces con las paredes y la presión se duplica. En la ley de Charles, al subir la temperatura las partículas se mueven más rápido, empujan más las paredes y, si la presión es constante, el volumen aumenta. En la de Gay-Lussac, en un recipiente rígido, más rapidez significa más choques y más presión.",
        "El modelo tiene límites: dibuja las partículas como puntos y no muestra su tamaño real ni sus atracciones. Un gas real se aparta del ideal cuando está muy comprimido o muy frío.",
    ],
    vocab=[("teoría cinético-molecular", "modelo que explica los gases con partículas en movimiento"), ("choque", "golpe de una partícula contra otra o contra una pared"), ("energía de movimiento", "energía que tienen las partículas por moverse"), ("gas real", "gas que se aparta del modelo ideal a baja temperatura o alta presión"), ("partícula", "pieza muy pequeña de la que está hecha la materia")],
    worked=[
        {"title": "Explicar Boyle con partículas", "problem": "El volumen de un gas se reduce a la mitad, con la misma temperatura. ¿Qué pasa con el número de choques por segundo en las paredes?", "steps": ["Las partículas tienen menos espacio.", "Chocan más veces con las paredes: se duplica el número de choques."], "answer": "Se duplica el número de choques, y por eso sube la presión"},
        {"title": "Cuenta de choques de ejemplo", "problem": "En un modelo, una pared recibe 40 choques por segundo. Si el volumen se reduce a la mitad y la temperatura es igual, ¿cuántos choques recibe por segundo?", "steps": ["El número de choques se duplica.", "40 × 2 = 80."], "answer": "80 choques por segundo"},
    ],
    mistakes=[
        {"wrong": "Decir que las partículas de un gas caliente son más grandes.", "why": "Se confunde tamaño con movimiento.", "fix": "Al calentar, las partículas se mueven más rápido; su tamaño no cambia."},
        {"wrong": "Creer que el modelo muestra el tamaño y la forma reales de las partículas.", "why": "Se olvida que el dibujo es una representación.", "fix": "Anota una limitación del dibujo."},
    ],
    tiers={
        "recovery": [
            ex("Según el modelo, ¿qué produce la presión de un gas: los choques de las partículas contra las paredes o la atracción entre las partículas?", "Los choques contra las paredes", "Cada choque empuja la pared."),
            ex("Si la temperatura de un gas sube, ¿las partículas se mueven más rápido o más lento?", "Más rápido", "La temperatura mide la energía de movimiento."),
            ex("En un gas ideal, ¿las partículas están muy juntas o muy separadas?", "Muy separadas", "Hay mucho espacio vacío entre ellas."),
        ],
        "understand": [
            ex("Un gas se calienta en un recipiente rígido. ¿Por qué su presión aumenta?", "Porque las partículas se mueven más rápido y chocan más y más fuerte con las paredes", "Más choques y más fuertes significan más presión."),
            ex("En un cilindro con émbolo, el volumen se reduce y la presión sube. ¿Qué cambió en los choques con las paredes?", "Ocurren más veces por segundo", "Con menos espacio, las partículas llegan antes a las paredes."),
            ex("¿Cuál es una limitación del modelo: (a) explica las leyes de los gases o (b) dibuja las partículas como puntos del mismo tamaño?", "(b)", "Las partículas reales no son puntos."),
        ],
        "apply": [
            arith("En un modelo de ejemplo, el volumen de un gas pasa de 6 L a 2 L con la misma temperatura. ¿Cuántas veces más choques por segundo recibe la pared?", "6//2", "El número de choques aumenta en la misma razón en que baja el volumen.", " veces"),
            ex("Dibujo A: 6 puntos con flechas cortas. Dibujo B: 6 puntos con flechas largas. ¿Cuál representa un gas a mayor temperatura?", "El dibujo B", "Las flechas largas indican mayor rapidez."),
            ex("Un cilindro con émbolo móvil se calienta y sus partículas se mueven más rápido. Para que la presión se mantenga constante, ¿el émbolo sube o baja?", "Sube", "El volumen aumenta, como dice la ley de Charles."),
        ],
        "reason": [
            ex("Lucía dice que «el gas caliente sube la presión porque sus partículas crecen». ¿Qué dice la teoría en cambio?", "Que se mueven más rápido, no que crezcan", "El tamaño de las partículas no cambia con la temperatura."),
            ex("Un modelo A solo muestra puntos quietos y otro modelo B muestra puntos con flechas que chocan con las paredes. ¿Cuál explica mejor la presión?", "El modelo B", "La presión viene de los choques."),
        ],
        "challenge": [
            ex("Un gas real muy comprimido y muy frío se aparta del comportamiento ideal. ¿Qué supuesto del modelo ideal deja de cumplirse?", "Que las partículas casi no se atraen y están muy separadas", "Cerca unas de otras, las partículas se atraen."),
            ex("Dos recipientes iguales tienen la misma cantidad de gas. En el A la temperatura es 300 K; en el B, 600 K. ¿En cuál esperas mayor presión y por qué?", "En el B, porque las partículas chocan más rápido y más veces", "Más temperatura implica más energía de movimiento."),
        ],
    },
    context=[ex("Una persona deja una pelota inflada al sol y la nota más dura. Con la teoría cinético-molecular, ¿qué cambió dentro de la pelota?", "Las partículas del aire se mueven más rápido y chocan más con las paredes", "La temperatura aumentó y la presión subió.")],
    selfcheck=[
        ex("¿Qué explica la presión de un gas en el modelo cinético-molecular?", "Los choques de las partículas contra las paredes", "Cada choque ejerce una fuerza."),
        ex("Al calentar un gas, ¿qué cambia en sus partículas?", "Se mueven más rápido", "Aumenta su energía de movimiento."),
        ex("¿Un gas real siempre se comporta como ideal?", "No", "Se aparta del ideal a alta presión o baja temperatura."),
    ],
    open_task=task(
        "Dibuja tres cajas con partículas. Caja 1: 8 puntos con flechas cortas, a temperatura baja. Caja 2: 8 puntos con flechas largas, a temperatura alta. Caja 3: 8 puntos en la mitad del espacio de la caja 1 (con una pared que se acerca) y con flechas cortas, como en la caja 1. Debajo de cada caja escribe qué pasa con los choques contra las paredes y qué ley de los gases representa cada comparación. Anota una limitación del dibujo.",
        "Caja 2 frente a caja 1: más choques y más fuertes; es Gay-Lussac si el recipiente es rígido y Charles si puede expandirse. Caja 3 frente a caja 1: menos espacio, más choques por segundo, ley de Boyle. Limitación: los puntos no tienen tamaño real.",
        ["tres cajas con 8 puntos", "choques explicados", "ley relacionada con cada comparación"],
        ["dibujos con flechas", "frases bajo cada caja"],
        ["dibujar partículas más grandes al calentar", "no anotar la ley"],
        "Pregunta qué cambiarías en tu dibujo para mostrar un gas real muy comprimido.",
    ),
    reinforce="Explica con partículas por qué una pelota inflada se vuelve más dura cuando se calienta.",
    extend="Averigua con una persona de tu casa qué otros objetos con aire a presión conoce, como un neumático o un balón, y qué cuidados hay que tener con el calor.",
)

# ================================================================ OA 13, clase 5
register(
    OA13, 5,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a argumentar sobre el comportamiento de los gases con datos, y a decidir si un plan de investigación es seguro y justo. Sirve para sacar conclusiones confiables.",
    prior=["Conozco las leyes de Boyle, Charles y Gay-Lussac.", "Sé que un modelo explica con partículas."],
    explain=[
        "Un buen argumento tiene cuatro partes: una afirmación, la evidencia (los datos), el razonamiento (el modelo o la ley que conecta los datos con la afirmación) y una limitación. Por ejemplo: «Al aumentar la presión, el volumen baja» (afirmación); «a 1 atm hay 12 L y a 3 atm hay 4 L» (evidencia); «el producto P × V se mantiene en 12, como dice la ley de Boyle» (razonamiento); «las mediciones tienen un pequeño error» (limitación).",
        "Una investigación justa cambia una sola variable, mide su efecto y mantiene constantes las demás. En un estudio de Boyle se cambia la presión y se mide el volumen, y se mantienen constantes la temperatura y la cantidad de gas. Pequeñas diferencias entre los datos se llaman error de medición; no invalidan la ley si son pequeñas.",
        "La seguridad es parte del método. Nunca calientes recipientes cerrados, no uses aerosoles ni acerques nada al fuego, no uses vidrio, no uses agua que queme y trabaja con una persona adulta. Si un plan es inseguro, se rediseña antes de ejecutarlo.",
    ],
    vocab=[("afirmación", "lo que se quiere demostrar"), ("evidencia", "datos que apoyan la afirmación"), ("razonamiento", "ley o modelo que une evidencia y afirmación"), ("error de medición", "pequeña diferencia entre lo medido y lo esperado"), ("variable controlada", "variable que se mantiene constante a propósito")],
    worked=[
        {"title": "Revisar si los datos apoyan Boyle", "problem": "Datos de ejemplo: 1 atm, 12 L; 2 atm, 6 L; 3 atm, 4 L; 4 atm, 3 L. ¿Apoyan que P × V es constante?", "steps": ["Los productos son 12, 12, 12 y 12.", "Todos son iguales."], "answer": "Sí, apoyan la ley de Boyle"},
        {"title": "Elegir el plan seguro", "problem": "Plan A: calentar una botella cerrada en una cocina. Plan B: poner un globo en una botella dentro de agua tibia que se pueda tocar, con un adulto. ¿Cuál es seguro?", "steps": ["El plan A calienta un envase cerrado: la presión puede reventarlo.", "El plan B usa agua que no quema y un recipiente abierto con globo."], "answer": "El plan B"},
    ],
    mistakes=[
        {"wrong": "Cambiar la presión y la temperatura al mismo tiempo en una prueba.", "why": "No se sabe cuál variable produjo el efecto.", "fix": "Cambia una sola variable y controla las demás."},
        {"wrong": "Descartar la ley porque un dato difiere por 1 L.", "why": "Se ignora el error de medición.", "fix": "Una diferencia pequeña es esperable; compara todos los datos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas variables se cambian a propósito en una investigación justa?", "Una", "Así se sabe cuál produjo el efecto."),
            ex("¿Qué parte de un argumento son los datos que apoyan la afirmación?", "La evidencia", "La evidencia son los datos medidos."),
            ex("¿Se puede calentar un recipiente cerrado en un experimento casero? Responde sí o no.", "No", "La presión puede reventarlo."),
        ],
        "understand": [
            ex("En un estudio de la ley de Charles, ¿qué variable se mantiene constante: la presión o la temperatura?", "La presión", "Charles relaciona volumen y temperatura a presión constante."),
            ex("¿Qué es el error de medición?", "Una pequeña diferencia entre lo medido y lo esperado", "Aparece en todo instrumento."),
            ex("¿Cuál de las partes de un argumento dice «según la ley de Boyle…»: la afirmación, el razonamiento o la limitación?", "El razonamiento", "Une los datos con la ley."),
        ],
        "apply": [
            ex("Datos de ejemplo de un gas a temperatura constante: 2 atm, 10 L; 4 atm, 5 L; 5 atm, 4 L. ¿Apoyan la ley de Boyle?", "Sí; los tres productos son 20", "2 × 10, 4 × 5 y 5 × 4 dan 20."),
            ex("Datos de ejemplo de un gas a presión constante: 300 K, 6 L; 450 K, 9 L; 600 K, 12 L. ¿Qué ley apoyan y qué relación muestran?", "Charles; a más temperatura, más volumen", "El volumen crece en proporción a la temperatura en K."),
            arith("En un ensayo se midieron 8 L, 8 L, 7 L y 9 L. ¿Cuál es el promedio?", "(8+8+7+9)//4", "Se suman las cuatro mediciones y se divide por cuatro.", " L"),
        ],
        "reason": [
            ex("Un estudiante cambia la presión y calienta el gas a la vez, y afirma que «la presión hizo que el volumen bajara». ¿Qué falla en su diseño?", "Cambió dos variables a la vez", "No se puede atribuir el efecto a la presión."),
            ex("Datos de ejemplo de un gas a temperatura constante: 1 atm, 12 L; 2 atm, 6,2 L; 3 atm, 4 L. Un compañero dice que no se cumple Boyle porque 6,2 no da exactamente 6. ¿Qué respuesta corresponde?", "La diferencia es pequeña, un error de medición", "Los datos se parecen mucho a lo esperado."),
        ],
        "challenge": [
            ex("Un plan propone «calentar una lata de aerosol vacía para ver cuánto sube la presión». ¿Por qué es inseguro y cómo se rediseñaría?", "Porque la lata cerrada puede reventar; se haría con un globo en agua tibia que se pueda tocar", "Un recipiente abierto o flexible con agua tibia es seguro."),
            ex("En un recipiente rígido la temperatura pasa de 300 K a 600 K y la presión pasa de 1 atm a 2 atm. ¿Qué ley conecta esos dos datos?", "Gay-Lussac", "La presión es directamente proporcional a la temperatura en K."),
        ],
    },
    context=[ex("Una persona dice que su balón de fútbol se siente más duro en un día de calor. Con lo aprendido, ¿cómo debería explicarlo en una frase: nombra la ley y la variable que cambia?", "Gay-Lussac, la presión sube con la temperatura", "El volumen casi no cambia y la temperatura sube.")],
    selfcheck=[
        ex("¿Cuáles son las cuatro partes de un buen argumento?", "Afirmación, evidencia, razonamiento y limitación", "Son las partes enseñadas en esta clase."),
        ex("En una investigación justa, ¿cuántas variables se mantienen constantes?", "Todas las demás", "Solo cambia la variable que se estudia."),
        ex("¿Qué haces si un plan es inseguro?", "Lo rediseño antes de ejecutarlo", "La seguridad va primero."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo de un gas a temperatura constante: 1 atm, 18 L; 2 atm, 9 L; 3 atm, 6 L; 6 atm, 3 L. Escribe un argumento de cuatro partes: afirmación, evidencia (calcula P × V en cada fila), razonamiento (nombra la ley) y limitación. Después escribe un plan seguro con globo, botella y agua tibia (que se pueda tocar) para mostrar la ley de Charles, indicando qué variable cambia, cuál se mide y cuáles se mantienen constantes.",
        "Afirmación: al subir la presión, el volumen baja. Evidencia: los productos son 18, 18, 18, 18. Razonamiento: ley de Boyle. Limitación: son datos de ejemplo. Plan: cambia la temperatura del agua, se mide el tamaño del globo, se mantienen la botella y el globo.",
        ["argumento de cuatro partes", "productos calculados", "plan seguro con variables nombradas"],
        ["texto con cuatro partes", "plan escrito"],
        ["omitir la limitación", "usar un plan que caliente un envase cerrado"],
        "Pregunta qué cambiarías para que tu plan sea aún más seguro.",
    ),
    reinforce="Escribe un argumento de cuatro partes para la ley de Gay-Lussac usando una pelota inflada.",
    extend="Averigua con una persona de tu casa qué cuidados tiene con los envases a presión, como los aerosoles o los balones de gas, y relaciónalo con las leyes.",
)
