"""Cuaderno del estudiante, 7.º básico Tecnología: OA 06 (efectos sociales y ambientales de la tecnología), clases 1 a 4.

Seguridad: las tareas son de lectura, cálculo y escritura; no se manipulan pilas, baterías, vidrio ni productos químicos, y la separación de residuos se hace solo con papel, cartón y envases limpios y sin filo.
Todas las cifras de residuos, tiempos y costos son de ejemplo, para practicar; no son estadísticas reales. Cifras enteras.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te7_a import reg
from student_lessons import arith

OA6 = "TE07 OA 06"

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a describir los efectos sociales de una solución de reparación, adaptación o mejora: a quién ayuda, a quién puede afectar y cómo cambia la vida de las personas. Sirve para valorar una solución más allá de que funcione.",
    prior=["Sé distinguir reparar, adaptar y mejorar.", "Sé que una solución puede tener efectos buscados y no buscados.", "Sé qué es un usuario."],
    explain=[
        "Los efectos sociales son los cambios que una solución produce en las personas y en cómo viven juntas. Se pueden ver en el acceso (quiénes pueden usar algo), la inclusión (que nadie quede fuera), el trabajo y el oficio, el tiempo que se gasta, el dinero que se ahorra o se gasta, la salud, la seguridad y las costumbres. Caracterizar un efecto es describirlo: qué cambia, para quién y qué tan grande es.",
        "Un efecto puede ser positivo (beneficia) o negativo (perjudica), y puede ser buscado o no buscado. Ejemplo: una rampa en una escuela facilita el acceso a una compañera con muletas (efecto buscado y positivo) y también a quien lleva un carro de útiles (efecto no buscado y positivo). Pero si la rampa ocupa el pasillo, puede dificultar el paso (efecto no buscado y negativo).",
        "Los efectos también pueden ser inmediatos o de largo plazo. Un taller comunitario de reparación ahorra dinero ahora, pero con los años puede crear un oficio y una costumbre de cuidar los objetos. En cambio, si todo se reemplaza en vez de repararse, a la larga se pierden esos oficios. Para caracterizar bien, usa datos o ejemplos concretos y nombra a quiénes afecta.",
    ],
    vocab=[("efecto social", "cambio que una solución produce en las personas"), ("inclusión", "que todas las personas puedan participar y usar algo"), ("acceso", "posibilidad de usar o llegar a algo"), ("efecto buscado", "cambio que se quería lograr"), ("largo plazo", "tiempo prolongado, después de muchos usos o años")],
    worked=[
        ("Caracterizar un efecto social", "Un barrio instala una luz con sensor de movimiento en un pasaje oscuro. ¿Qué efecto social tiene y para quién?", ["Más personas pueden caminar de noche con mayor seguridad.", "Beneficia a vecinos, estudiantes que vuelven tarde y personas mayores."], "Aumenta la seguridad al caminar de noche para vecinos, estudiantes y personas mayores"),
        ("Distinguir efecto buscado y no buscado", "Un taller de reparación de bicicletas se abre para que los estudiantes arreglen la suya. Muchos vecinos empiezan a usar el taller para sus bicicletas. ¿Cuál es buscado y cuál no?", ["Buscado: que los estudiantes arreglen su bicicleta.", "No buscado: que los vecinos también lo usen y se forme una comunidad."], "Buscado: estudiantes arreglan su bicicleta. No buscado: vecinos que también la usan"),
    ],
    mistakes=[
        ("Decir que una solución solo tiene efectos positivos.", "Casi toda solución también puede perjudicar a alguien.", "Pregunta «¿a quién podría afectar de forma negativa?»."),
        ("Describir los efectos con palabras vagas como «ayuda mucho».", "No se sabe a quién ni cuánto.", "Nombra a quién y agrega un dato o ejemplo."),
    ],
    R=[
        ("Una rampa que permite a más personas entrar a un lugar, ¿mejora el acceso o lo empeora?", "Lo mejora", "Más personas pueden usar el lugar."),
        ("Un cambio que una solución produce sin que se haya buscado, ¿es un efecto buscado o no buscado?", "No buscado", "Es lo que ocurre sin planearlo."),
        ("Que una solución ahorre dinero a una familia, ¿es un efecto social o un efecto sobre el clima?", "Un efecto social", "Cambia la vida de las personas."),
    ],
    C=[
        ("¿Cuál describe mejor un efecto social? A «las familias gastan $2.000 menos al mes en reparar», B «es bonito».", "A", "A dice a quién y cuánto cambia."),
        ("Una solución facilita la vida de un grupo y dificulta la de otro. ¿Qué haces al evaluarla?", "Analizar los efectos positivos y los negativos", "Se miran todos los grupos afectados."),
        ("Un compañero dice: «Si ayuda a mucha gente, no importa a quién perjudique». ¿Qué le respondes?", "Que también se deben considerar y reducir los perjuicios", "Una evaluación justa mira a todas las personas afectadas."),
    ],
    A=[
        arith("Un taller comunitario repara 15 objetos por semana. ¿Cuántos objetos repara en 4 semanas?", "15*4", "Se multiplica por las semanas.", " objetos"),
        arith("Una familia ahorra $3.000 por cada objeto reparado en vez de comprarlo nuevo. Repara 5 en un año. ¿Cuánto ahorra?", "3000*5", "Se multiplica el ahorro por los objetos.", " pesos"),
        ("Clasifica en orden con P (positivo) o N (negativo): (1) una rampa que da acceso, (2) una máquina que reemplaza el oficio de reparar sin ofrecer otro trabajo, (3) un taller que enseña a arreglar bicicletas.", "1 P, 2 N, 3 P", "Los efectos 1 y 3 benefician y el 2 quita oportunidades de trabajo."),
    ],
    Z=[
        ("Un cartel con letras grandes se instala en un pasillo. Ayuda a personas con visión baja, pero tapa el paso de una puerta. ¿Qué haces para reducir el perjuicio?", "Moverlo a una pared donde no tape el paso", "Se mantiene el beneficio y se elimina el perjuicio."),
        ("Mateo dice que un taller de reparación de bicicletas es solo para quienes tienen bicicleta. Elena dice que también sirve a quien quiere aprender un oficio. ¿Quién identifica más efectos sociales?", "Elena", "Considera el aprendizaje y el oficio además del uso."),
    ],
    D=[
        arith("En una comunidad hay 120 familias. Un taller de reparación ayuda a 45 familias en el primer año y a 30 más en el segundo. ¿Cuántas familias quedan por ayudar?", "120-45-30", "Se restan las familias ayudadas del total.", " familias"),
        ("Una solución ahorra 10 minutos diarios a cada una de 30 personas, 5 días a la semana. ¿Cuántos minutos ahorran juntas en una semana?", "1.500 minutos", "10 × 30 × 5 = 1.500 minutos."),
    ],
    ctx=("En la escuela se pone un banco bajo y ancho en el patio para que se sienten estudiantes con poca fuerza en las piernas. Los bancos antiguos eran altos. Escribe un efecto social positivo, uno posible negativo y cómo reducirlo.", "Positivo: más estudiantes pueden sentarse y descansar. Negativo posible: el banco ocupa espacio donde juegan otros. Se reduce ubicándolo al borde del patio", "Se nombran un efecto positivo, uno posible negativo y una forma de reducirlo."),
    sc=[
        ("En Tecnología: ¿Qué es un efecto social?", "Un cambio que una solución produce en las personas", "Es la definición de la clase."),
        ("¿Un efecto puede no haber sido buscado?", "Sí", "Algunos ocurren sin planearlos."),
        ("¿Qué debe decir una buena descripción de un efecto?", "Qué cambia, para quién y qué tan grande es", "Así se caracteriza con precisión."),
    ],
    open_task=(
        "Escoge una solución. Solución 1: una rampa de concreto, hecha por una empresa constructora, en la entrada de una biblioteca del barrio. Solución 2: un taller de reparación de bicicletas gratuito los sábados en la escuela. Solución 3: carteles con letras grandes y dibujos en el pasillo de la escuela. Escribe dos efectos sociales positivos, uno posible negativo, quiénes lo viven, un dato o ejemplo de ejemplo para cada uno y una forma de reducir el efecto negativo.",
        "Solución 2: positivos: ahorro de dinero en reparaciones (por ejemplo, $2.000 por bicicleta) y aprendizaje de un oficio. Negativo posible: el taller ocupa el patio y quita espacio de juego. Se reduce haciéndolo en un horario sin juego",
        ["dos efectos positivos con quiénes los viven", "un posible efecto negativo", "usa datos o ejemplos concretos", "propone una forma de reducir el negativo"],
        ["hoja con efectos y propuesta"],
        ["solo efectos positivos", "descripciones vagas"],
        "Pregunta: «¿para quién es y cuánto cambia?». Si no puede responder, pídele agregar un dato.",
    ),
    reinforce="Piensa en un objeto adaptado que veas a diario y escribe qué cambió en la vida de quienes lo usan.",
    extend="Explica un ejemplo en que una solución que ayuda mucho a un grupo perjudica sin querer a otro.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja, lápiz y los datos de ejemplo escritos en este cuaderno.",
    use="Aprenderé a describir los efectos ambientales de una solución a lo largo de su vida: obtener materiales, fabricar, usar y desechar. Sirve para comparar reparar, reemplazar y reutilizar con datos.",
    prior=["Sé qué es un residuo.", "Sé que reparar gasta menos material que reemplazar.", "Sé calcular con kilogramos y litros."],
    explain=[
        "Los efectos ambientales son los cambios que una solución produce en el aire, el agua, el suelo y los seres vivos. Para describirlos conviene mirar el ciclo de vida de un objeto, que tiene cuatro etapas: obtener los materiales de la naturaleza, fabricar el objeto, usarlo y desecharlo. En cada etapa se gastan recursos, como agua, energía y materiales, y se generan residuos.",
        "Reparar o reutilizar un objeto alarga su vida útil: se compra menos, se fabrica menos y se bota menos. Por eso suele reducir el efecto ambiental. Pero no siempre: si la reparación usa mucha energía o materiales que contaminan, el efecto puede ser peor. Para decidir se comparan datos, como los kilogramos de residuos que se evitan, la energía que se gasta y los materiales nuevos que se necesitan.",
        "También hay efectos ambientales positivos de largo plazo, como mantener limpios los espacios del barrio. Y hay efectos negativos que no se ven de inmediato, como los residuos que se acumulan. Al caracterizar un efecto ambiental, escribe en qué etapa del ciclo de vida ocurre, qué recurso afecta y cuánto. Los datos de esta clase son de ejemplo, para practicar.",
    ],
    vocab=[("efecto ambiental", "cambio que algo produce en el aire, el agua, el suelo o los seres vivos"), ("ciclo de vida", "etapas de un objeto: obtener materiales, fabricar, usar y desechar"), ("residuo", "material que se bota"), ("vida útil", "tiempo durante el cual un objeto sirve"), ("recurso natural", "material o energía que viene de la naturaleza")],
    worked=[
        ("Ubicar un efecto en el ciclo de vida", "Una botella se bota después de usarse una vez. ¿En qué etapa del ciclo de vida ocurre el efecto ambiental de los residuos?", ["Las etapas son obtener, fabricar, usar y desechar.", "El residuo aparece cuando se bota: es la etapa de desechar."], "En la etapa de desechar"),
        ("Calcular residuos evitados", "Una familia bota 12 objetos al año. Si repara 5 de ellos, ¿cuántos objetos dejan de botarse? Y si cada objeto pesa 2 kg, ¿cuántos kilogramos son?", ["Dejan de botarse 5 objetos.", "Multiplico 5 × 2."], "5 objetos y 10 kg de residuos evitados"),
    ],
    mistakes=[
        ("Creer que un objeto solo tiene efecto ambiental cuando se bota.", "También se gastan recursos al obtener los materiales, fabricarlo y usarlo.", "Revisa las cuatro etapas del ciclo de vida."),
        ("Pensar que reparar siempre es mejor para el ambiente.", "Una reparación con mucha energía o materiales contaminantes puede ser peor.", "Compara datos antes de decidir."),
    ],
    R=[
        ("¿Cuántas etapas tiene el ciclo de vida que se estudia?", "Cuatro", "Obtener, fabricar, usar y desechar."),
        ("Un material que se bota, ¿es un residuo o un recurso natural?", "Un residuo", "Es lo que se bota."),
        ("Alargar la vida útil de un objeto, ¿reduce o aumenta los residuos?", "Los reduce", "Se bota menos."),
    ],
    C=[
        ("Extraer arcilla de un cerro para fabricar ladrillos, ¿en qué etapa ocurre? A obtener materiales, B desechar.", "A", "Se toma de la naturaleza."),
        ("¿Por qué reparar suele ayudar al ambiente? A porque se compra y se fabrica menos, B porque los objetos reparados no tienen ciclo de vida.", "A", "Se evita usar recursos nuevos."),
        ("Un compañero dice: «Reparar con un material muy contaminante es igual de bueno». ¿Qué le respondes?", "Que hay que comparar los efectos", "El material de la reparación también cuenta."),
    ],
    A=[
        arith("Un curso usa 40 botellas por semana y reutiliza 15 de ellas. ¿Cuántas botellas bota?", "40-15", "Se restan las reutilizadas de las usadas.", " botellas"),
        arith("Cada objeto reparado evita 3 kg de residuos. Una comunidad repara 20 objetos. ¿Cuántos kilogramos de residuos evita?", "3*20", "Se multiplica por los objetos reparados.", " kg"),
        arith("Un objeto nuevo necesita 50 litros de agua para fabricarse. Reparar uno usa 5 litros. ¿Cuántos litros se ahorran al reparar en vez de reemplazar?", "50-5", "Se resta el agua de la reparación del agua de fabricar.", " litros"),
    ],
    Z=[
        ("Reparar una lámpara usa 2 kg de material nuevo y evita botar 5 kg. Reemplazarla usa 8 kg de material nuevo y bota 5 kg. ¿Cuál gasta menos material nuevo?", "Reparar", "Usa 2 kg contra 8 kg."),
        ("Dos grupos describen la botella de plástico. Uno dice que solo contamina cuando se bota. Otro dice que se gasta agua y energía al fabricarla. ¿Cuál describe mejor el ciclo de vida?", "El segundo", "Mira más etapas que solo desechar."),
    ],
    D=[
        arith("Una escuela bota 12 kg de residuos de cartón por semana. Con una campaña, reutiliza 4 kg por semana. ¿Cuántos kilogramos bota en 5 semanas?", "(12-4)*5", "Se calcula lo que bota por semana y se multiplica por 5.", " kg"),
        ("Un objeto A dura 2 años y bota 4 kg al final. Un objeto B dura 6 años y bota 6 kg al final. ¿Cuántos kilogramos de residuos produce cada uno por año?", "A 2 kg por año y B 1 kg por año", "4 ÷ 2 = 2 y 6 ÷ 6 = 1: B produce menos por año."),
    ],
    ctx=("En tu casa se bota una mochila cada año. Si la reparas, dura 3 años. Una mochila pesa 1 kg. Calcula cuántos kilogramos de mochila se botan en 3 años si se reemplaza cada año y cuántos si se repara, y qué ahorras.", "Reemplazando se botan 3 kg; reparando se bota 1 kg; se ahorran 2 kg", "Se calcula 3 × 1 = 3 y 1 al final, y la diferencia es 2."),
    sc=[
        ("¿Cuáles son las etapas del ciclo de vida?", "Obtener, fabricar, usar y desechar", "Son las cuatro etapas de la clase."),
        ("¿Reparar reduce los residuos?", "Sí, porque alarga la vida útil", "Se bota menos."),
        ("¿Por qué comparar datos antes de decidir?", "Porque una reparación puede tener efectos negativos", "Los datos permiten decidir bien."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: una mochila de 1 kg que se bota cada año; reparada, dura 3 años. Objeto 2: una silla de 4 kg que se reemplaza cada 2 años; arreglada, dura 6 años. Escribe las cuatro etapas del ciclo de vida para ese objeto, calcula los kilogramos de residuos en un período largo con y sin reparar, y explica qué recurso (agua, energía o materiales) se ahorra.",
        "Objeto 1 en 3 años: reemplazar bota 3 kg y reparar bota 1 kg. Se ahorran 2 kg. Etapas: obtener la tela, fabricar, usar, desechar. Se ahorran materiales",
        ["describe las cuatro etapas", "calcula los residuos con y sin reparar", "dice qué recurso se ahorra", "usa datos de ejemplo rotulados"],
        ["hoja con ciclo de vida y cálculos"],
        ["mirar solo cuando se bota", "no calcular la diferencia"],
        "Pregunta: «¿cuánto se evita al reparar?». Si no calcula, pídele hacer la resta.",
    ),
    reinforce="Anota cuántos envases botó tu casa en un día y qué podrías reutilizar.",
    extend="Explica un caso en que reemplazar un objeto podría ser mejor para el ambiente que repararlo.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja, lápiz y las tablas escritas en este cuaderno.",
    use="Aprenderé a ordenar los efectos sociales y ambientales de una solución en una tabla y a hacer un balance. Sirve para decidir con una visión completa.",
    prior=["Sé describir efectos sociales.", "Sé describir efectos ambientales.", "Sé sumar y restar números enteros."],
    explain=[
        "Para representar los efectos de una solución se usa una tabla con dos columnas, social y ambiental, y dos filas, positivos y negativos. En cada casilla se anota un efecto concreto con su dato. Se puede agregar si es de corto plazo (se nota enseguida) o de largo plazo (se nota con los años). Una tabla completa muestra qué gana y qué pierde cada grupo y el ambiente.",
        "Para hacer un balance, se asigna un puntaje a cada efecto: de +1 a +3 para los positivos y de −1 a −3 para los negativos, según su importancia. La suma de los puntajes indica si la solución, en total, suma o resta valor. Pero el balance no reemplaza al análisis: un efecto negativo grave, como un riesgo para la salud, puede pesar más que muchos positivos pequeños.",
        "Después del balance se propone cómo reducir los efectos negativos. Por ejemplo, si una solución genera residuos, se puede usar material reutilizado; si ocupa mucho espacio, se puede cambiar su ubicación. Una solución mejorada puede cambiar el balance: la tabla se vuelve a hacer y se compara con la anterior. Los datos de la clase son de ejemplo.",
    ],
    vocab=[("balance", "suma de efectos positivos y negativos"), ("corto plazo", "efecto que se nota enseguida"), ("largo plazo", "efecto que se nota con los años"), ("puntaje", "número que indica la importancia de un efecto"), ("mitigar", "reducir un efecto negativo")],
    worked=[
        ("Completar y sumar un balance", "Taller de reparación de bicicletas. Efectos: +3 ahorro de dinero de las familias (social), +2 menos residuos metálicos (ambiental), −1 ruido en el patio (social). ¿Cuál es el balance?", ["Sumo los positivos: 3 + 2 = 5.", "Resto el negativo: 5 − 1."], "Balance de 4 puntos"),
        ("Revisar que un balance no oculte un efecto grave", "Una solución suma +6 pero tiene un efecto de −3 por riesgo de golpes a niños pequeños. ¿Se acepta solo por el +6?", ["El balance total es +3, pero hay un riesgo para la salud.", "Se debe reducir el riesgo antes de aceptar la solución."], "No se acepta aún; hay que reducir el riesgo"),
    ],
    mistakes=[
        ("Considerar solo el balance numérico y olvidar un efecto grave.", "Un riesgo para la salud no se compensa con ahorros pequeños.", "Revisa por separado los efectos graves."),
        ("Poner efectos sin datos en la tabla.", "No se sabe cuánto importan ni a quién afectan.", "Anota quiénes y cuánto, con un dato o ejemplo."),
    ],
    R=[
        ("Un ahorro de dinero para las familias, ¿es un efecto social o ambiental?", "Social", "Cambia la vida de las personas."),
        ("Menos residuos en el barrio, ¿es un efecto social o ambiental?", "Ambiental", "Afecta el entorno natural y urbano."),
        ("Un efecto que se nota con los años, ¿es de corto o de largo plazo?", "De largo plazo", "Se nota con el tiempo."),
    ],
    C=[
        ("¿Para qué sirve el balance? A para ver si en total una solución suma o resta valor, B para elegir siempre la solución más barata.", "A", "El balance resume todos los efectos."),
        ("¿Qué se hace después de identificar un efecto negativo? A se propone cómo reducirlo, B se borra de la tabla.", "A", "Mitigar mejora la solución."),
        ("Un balance de +5 tiene un efecto de −3 por riesgo para la salud. ¿Qué haces?", "Reducir el riesgo antes de aceptar", "Un efecto grave no se compensa con otros."),
    ],
    A=[
        arith("Efectos: +2, +3, −1 y −2. ¿Cuál es el balance?", "2+3-1-2", "Se suman positivos y se restan negativos.", " puntos"),
        arith("Una solución tiene tres efectos positivos de +2 cada uno y dos negativos de −1 cada uno. ¿Cuál es el balance?", "3*2-2*1", "Se suman los positivos y se restan los negativos.", " puntos"),
        ("Anota en la tabla el efecto «las familias ahorran $2.000 al mes». ¿En qué casilla va? A social positivo, B ambiental negativo.", "A", "Es un cambio en el dinero de las personas y es favorable."),
    ],
    Z=[
        ("Solución 1: balance +4 sin riesgos. Solución 2: balance +6 con un riesgo grave para la salud. ¿Cuál conviene primero y por qué?", "La solución 1", "La 2 necesita reducir su riesgo grave antes de elegirse."),
        ("Ana cambia el puntaje de un efecto negativo de −3 a −1 para que el balance dé positivo. ¿Es correcto?", "No", "Se manipulan los datos y el resultado deja de ser honesto."),
    ],
    D=[
        arith("Una solución tiene balance +5. Se agrega una medida que reduce un efecto negativo de −3 a −1. ¿Cuál es el nuevo balance?", "5+3-1", "Se quita el efecto de −3 y se agrega el de −1.", " puntos"),
        ("Tabla (de ejemplo): social positivo +3, social negativo −2, ambiental positivo +2, ambiental negativo −3. ¿Cuál es el balance y qué ámbito pierde más?", "Balance 0; el ámbito ambiental (−1) pierde más", "3 − 2 + 2 − 3 = 0; ambiental suma 2 − 3 = −1."),
    ],
    ctx=("Un curso arma un puesto de trueque de ropa: los estudiantes intercambian prendas que ya no usan. Efectos: +3 ahorro de dinero, +2 menos ropa botada, −1 el trueque ocupa el patio. Calcula el balance y propón cómo reducir el efecto negativo.", "Balance: +4. Para reducir el efecto del patio: hacerlo en un horario en que no se juega, o en un solo rincón", "Se calcula 3 + 2 − 1 = 4 y se propone una mitigación."),
    sc=[
        ("¿Qué dos columnas tiene la tabla de efectos?", "Social y ambiental", "Son los dos tipos de efectos."),
        ("¿Qué indica un balance positivo?", "Que en total la solución suma más de lo que resta", "Resume ganancias y pérdidas."),
        ("¿Se pueden cambiar los puntajes para que el resultado salga como uno quiere?", "No", "Sería manipular los datos."),
    ],
    open_task=(
        "Escoge una solución. Solución 1: un puesto de trueque de ropa en la escuela. Solución 2: un taller para poner fundas anchas de espuma a los lápices de estudiantes con poca fuerza en las manos. Solución 3: una compostera comunitaria de restos de comida. Completa una tabla con efectos sociales y ambientales, positivos y negativos, con dato y puntaje, calcula el balance y propón cómo reducir el efecto negativo.",
        "Solución 1: social positivo +3 (ahorro); ambiental positivo +2 (menos ropa botada); social negativo −1 (ocupa el patio); ambiental negativo 0. Balance +4. Mitigación: hacerlo en un horario sin juego",
        ["tabla con las cuatro casillas", "datos y puntajes razonables", "suma bien el balance", "propone cómo reducir el negativo"],
        ["hoja con tabla y balance"],
        ["no incluir efectos negativos", "cambiar puntajes para obtener un resultado deseado"],
        "Pregunta: «¿qué dato apoya este puntaje?». Si no hay, pídele agregar un ejemplo.",
    ),
    reinforce="Elige un objeto de tu casa y escribe un efecto social positivo y uno ambiental negativo posible.",
    extend="Explica por qué un balance positivo no basta si hay un efecto negativo grave.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Para practicar la separación de residuos, solo papel, cartón y envases limpios y sin filo.",
    use="Aprenderé a proponer acciones que reduzcan los efectos negativos de una solución y a implementarlas con seguridad. Sirve para que la tecnología cause menos daño y beneficie a más personas.",
    prior=["Sé hacer una tabla de efectos.", "Sé calcular residuos evitados.", "Sé que hay riesgos al construir y manipular."],
    explain=[
        "Para reducir los efectos negativos se pueden aplicar cuatro acciones: reducir (usar menos), reutilizar (darle otro uso), reparar (arreglar para alargar la vida) y reciclar (convertir un residuo en materia prima). Se prefiere el orden: primero reducir, luego reutilizar y reparar, y al final reciclar, porque reciclar también gasta energía. Se elige según el objeto y el contexto.",
        "En lo social, los efectos negativos se reducen incluyendo a las personas afectadas: se las consulta, se explican los cambios y se busca que nadie quede fuera. En lo ambiental, se mide cuánto cambia con cada acción: por ejemplo, cuántos kilogramos de cartón dejan de botarse al reutilizar cajas. Los números de esta clase son de ejemplo.",
        "Al implementar acciones de residuos se cuida la seguridad. Se separan solo papel, cartón y envases limpios y sin filo; no se tocan vidrios rotos, pilas, baterías ni productos químicos, porque esos los maneja una persona adulta. Se usan guantes de trabajo si hay suciedad, se recoge el pelo y se lava las manos al terminar. Si hay duda, se pregunta antes de manipular.",
    ],
    vocab=[("reducir", "usar menos material o energía"), ("reutilizar", "darle un nuevo uso a un objeto"), ("reciclar", "convertir un residuo en materia prima"), ("mitigar", "disminuir un efecto negativo"), ("separar residuos", "ordenar los residuos por tipo para su manejo")],
    worked=[
        ("Elegir la acción adecuada", "Un curso bota las cajas de cartón de sus útiles cada semana. ¿Qué acción conviene primero?", ["Primero conviene reducir o reutilizar antes que reciclar.", "Las cajas pueden servir otra vez para guardar materiales."], "Reutilizar las cajas para guardar materiales"),
        ("Calcular lo que se evita", "Un curso reutiliza 6 cajas por semana. Cada caja pesa 300 g. ¿Cuántos gramos de cartón evita botar en una semana?", ["Son 6 cajas.", "Multiplico 6 × 300."], "1.800 g"),
    ],
    mistakes=[
        ("Reciclar todo sin pensar en reducir o reutilizar.", "Reciclar también gasta energía; usar menos evita el problema desde el inicio.", "Aplica primero reducir y reutilizar."),
        ("Manipular pilas, vidrios rotos o productos químicos al separar residuos.", "Son peligrosos y requieren a una persona adulta.", "Separa solo papel, cartón y envases limpios sin filo."),
    ],
    R=[
        ("Usar menos material desde el comienzo, ¿es reducir o reciclar?", "Reducir", "Se evita gastar."),
        ("Convertir un residuo en materia prima, ¿es reutilizar o reciclar?", "Reciclar", "Se transforma el residuo."),
        ("¿Quién maneja pilas, baterías y vidrios rotos?", "Una persona adulta", "Son peligrosos para estudiantes."),
    ],
    C=[
        ("¿Qué orden de acciones se prefiere? A reducir, reutilizar o reparar y al final reciclar, B reciclar primero.", "A", "Reciclar también gasta energía."),
        ("Un compañero propone recoger vidrios rotos del patio para separarlos. ¿Qué haces?", "Avisar a una persona adulta, que lo recogerá", "Los vidrios cortan."),
        ("¿Cómo se reducen los efectos sociales negativos? A incluyendo a las personas afectadas, B decidiendo sin consultar a nadie.", "A", "Escucharlas permite corregir."),
    ],
    A=[
        arith("Un curso reutiliza 8 cajas por semana de 250 g cada una. ¿Cuántos gramos de cartón evita botar en una semana?", "8*250", "Se multiplican las cajas por su peso.", " g"),
        arith("Un colegio bota 30 kg de papel al mes y con una campaña bota 12 kg menos. ¿Cuántos kilogramos bota ahora?", "30-12", "Se resta lo que se dejó de botar.", " kg"),
        ("Ordena de más a menos conveniente: reciclar, reducir, reutilizar. ¿Cuál es el orden?", "Reducir, reutilizar, reciclar", "Se prefiere evitar y reutilizar antes de reciclar."),
    ],
    Z=[
        ("Un grupo propone reciclar 100 botellas en vez de usar bidones reutilizables. Otro propone usar bidones reutilizables. ¿Cuál acción es preferible según el orden de la clase?", "Usar bidones reutilizables", "Reutilizar y reducir se prefieren antes que reciclar."),
        ("Una vecina dice: «La compostera nos huele mal y los vecinos se quejan». ¿Qué haces para reducir el efecto social negativo?", "Cambiarla de lugar y taparla mejor", "Se escucha el problema y se corrige."),
    ],
    D=[
        arith("En un barrio, 10 familias dejan de botar 2 kg de cartón cada semana gracias a una campaña. ¿Cuántos kilogramos dejan de botarse en 4 semanas?", "10*2*4", "Se multiplican las familias, los kilogramos y las semanas.", " kg"),
        ("Una campaña tiene 3 acciones: reducir (ahorra 4 kg), reutilizar (ahorra 3 kg) y reciclar (ahorra 2 kg). Si el curso solo puede hacer dos, ¿cuál combinación ahorra más?", "Reducir y reutilizar", "Suman 7 kg, más que las otras combinaciones."),
    ],
    ctx=("Tu curso quiere reducir el cartón que bota. Propón una acción de cada tipo (reducir, reutilizar y reciclar) con una medida de seguridad, y calcula cuántos kilogramos se evitan si se reutilizan 5 cajas de 400 g.", "Reducir: usar menos cajas en los útiles. Reutilizar: guardar materiales en cajas. Reciclar: llevar lo que sobre al punto de reciclaje. Seguridad: no tocar vidrios ni pilas. Se evitan 2 kg", "Tres acciones, una medida de seguridad y 5 × 400 = 2.000 g, es decir, 2 kg."),
    sc=[
        ("¿Qué acción se prefiere primero?", "Reducir", "Evita el residuo desde el inicio."),
        ("¿Quién maneja los vidrios rotos?", "Una persona adulta", "Son objetos peligrosos."),
        ("¿Cómo se reducen los efectos sociales negativos?", "Incluyendo y escuchando a las personas afectadas", "Se corrige con sus aportes."),
    ],
    open_task=(
        "Escoge un plan. Plan 1: reducir el papel que bota el curso, que es de 20 hojas por estudiante a la semana, con 30 estudiantes; con una campaña, cada estudiante bota 5 hojas menos a la semana. Plan 2: reutilizar 12 cajas de cartón de 250 g cada una para guardar materiales. Escribe las acciones (reducir, reutilizar, reparar y reciclar) con el orden de prioridad, calcula cuánto se evita, escribe una medida para reducir un efecto social negativo y una medida de seguridad.",
        "Plan 2: reducir: pedir menos cajas; reutilizar: usar las 12 cajas; reciclar: lo que ya no sirva. Se evitan 3.000 g de cartón. Efecto social: avisar a todo el curso dónde guardar. Seguridad: no tocar vidrios ni pilas",
        ["acciones en el orden de prioridad", "calcula lo que se evita", "medida para reducir un efecto social negativo", "medida de seguridad"],
        ["hoja con plan y cálculo"],
        ["reciclar antes que reducir", "no incluir medidas de seguridad"],
        "Pregunta: «¿qué haces si hay un vidrio o una pila?». Si responde que lo toma, pídele repasar la regla.",
    ),
    reinforce="Haz una lista de tres objetos de tu casa que podrías reutilizar antes de botarlos.",
    extend="Explica por qué reducir es más eficaz que reciclar cuando se quiere cuidar el ambiente.",
)
