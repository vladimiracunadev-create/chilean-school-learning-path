"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 12 (evolución de los modelos atómicos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12 = "CN08 OA 12"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 12, clase 1
register(
    OA12, 1,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé la teoría atómica de Dalton y a formular preguntas que se pueden investigar con datos de masas. Sirve para entender cómo se llegó a la idea de átomo.",
    prior=["Sé que la materia está formada por partículas.", "Sé que un modelo explica algo que no se ve y tiene límites."],
    explain=[
        "A comienzos del siglo XIX, John Dalton propuso una teoría para explicar por qué las sustancias se combinan siempre en las mismas proporciones de masa. Según Dalton, toda la materia está formada por átomos, que son esferas macizas, indivisibles e indestructibles. Los átomos de un mismo elemento son iguales entre sí, y los de elementos distintos se diferencian, sobre todo, en su masa.",
        "Para Dalton, un compuesto se forma cuando átomos de distintos elementos se unen en una proporción fija. En un cambio químico los átomos no se crean ni se destruyen: solo se reordenan, y por eso la masa total se conserva. Por ejemplo, el agua pura siempre tiene 1 g de hidrógeno por cada 8 g de oxígeno, en cualquier muestra.",
        "Una pregunta investigable sobre este modelo debe poder responderse midiendo. «¿Se mantiene la masa total antes y después de un cambio en un recipiente cerrado?» se puede medir con una balanza. «¿Qué átomo es más simpático?» no se puede investigar. Recuerda que el modelo de Dalton no se vio directamente: se propuso para explicar mediciones de masa.",
    ],
    vocab=[("átomo", "partícula muy pequeña de la que está hecha la materia"), ("elemento", "sustancia formada por un solo tipo de átomo"), ("compuesto", "sustancia formada por átomos de distintos elementos unidos en proporción fija"), ("proporción fija", "relación de masas que es siempre la misma en un compuesto"), ("conservación de la masa", "la masa total no cambia en un cambio químico en un recipiente cerrado")],
    worked=[
        {"title": "Proporción fija en el agua", "problem": "Una muestra de 18 g de agua pura, ¿qué masa de hidrógeno y de oxígeno contiene, si la proporción es 1 g de hidrógeno por cada 8 g de oxígeno?", "steps": ["Cada 9 g de agua contienen 1 g de hidrógeno y 8 g de oxígeno.", "18 g son dos veces 9 g: 2 g de hidrógeno y 16 g de oxígeno."], "answer": "2 g de hidrógeno y 16 g de oxígeno"},
        {"title": "Conservación de la masa", "problem": "En un recipiente cerrado, 12 g de una sustancia A reaccionan con 20 g de una sustancia B y forman una sola sustancia nueva. ¿Qué masa tendrá, según Dalton?", "steps": ["Los átomos solo se reordenan, no se destruyen.", "La masa de lo que se forma es la suma de las masas de las sustancias que reaccionaron: 12 + 20 = 32."], "answer": "32 g"},
    ],
    mistakes=[
        {"wrong": "Decir que Dalton observó los átomos con un microscopio.", "why": "Se confunde un modelo con una observación directa.", "fix": "Dalton propuso los átomos como explicación de las mediciones de masa."},
        {"wrong": "Creer que en un cambio químico los átomos se destruyen y aparecen otros.", "why": "No se considera que los átomos se reordenan.", "fix": "Los átomos se conservan; solo cambia cómo están unidos."},
    ],
    tiers={
        "recovery": [
            ex("Según Dalton, ¿cómo era el átomo? A) Divisible en varias partes; B) Una esfera maciza e indivisible", "B)", "Para Dalton el átomo era la partícula más pequeña, sin partes."),
            ex("Según Dalton, ¿en qué se diferencian los átomos de elementos distintos?", "En su masa", "Los átomos del mismo elemento son iguales y los de otro elemento difieren, sobre todo, en masa."),
            ex("¿Qué se hace con los átomos en un cambio químico según Dalton? A) Se destruyen; B) Se crean nuevos; C) Se reordenan", "C)", "Los átomos se conservan y solo cambian sus uniones."),
        ],
        "understand": [
            arith("En un recipiente cerrado, 6 g de hidrógeno reaccionan con 48 g de oxígeno y forman agua. ¿Cuántos gramos de agua se espera obtener?", "6+48", "La masa total se conserva, por lo que se suman las masas.", " g"),
            ex("Muestras de agua pura obtenidas de lluvia, de un río y del mar dan siempre 1 g de hidrógeno por 8 g de oxígeno. ¿Qué idea de Dalton apoya esto?", "Que los compuestos tienen proporciones fijas", "Si la relación se repite, el compuesto tiene proporción fija de átomos."),
            ex("¿Cuál pregunta puede investigarse con datos de masa? A) ¿Se mantiene la masa total antes y después de una reacción en un recipiente cerrado?; B) ¿Qué átomo es más simpático?", "A)", "Se puede responder con una balanza y comparando números."),
        ],
        "apply": [
            arith("Una muestra de agua pura tiene 27 g. Si la proporción es 1 g de hidrógeno por cada 8 g de oxígeno, ¿cuántos gramos de oxígeno contiene?", "27//9*8", "Cada 9 g de agua tienen 8 g de oxígeno; en 27 g hay tres veces esa masa.", " g"),
            arith("Una muestra de agua pura contiene 40 g de oxígeno. ¿Cuántos gramos de hidrógeno tiene?", "40//8", "Hay 1 g de hidrógeno por cada 8 g de oxígeno.", " g"),
            ex("Se pesa una taza tapada con 90 g de hielo y marca 250 g. Luego el hielo se derrite dentro de la taza tapada. ¿Cuánto marcará la balanza?", "250 g", "La materia no desaparece al cambiar de estado; con la taza tapada la masa total se conserva."),
        ],
        "reason": [
            ex("Un compañero dice que Dalton demostró con un microscopio que el átomo es indivisible. ¿Qué es más correcto? A) Dalton propuso un modelo que explicaba las medidas de masa; B) Dalton vio átomos con un microscopio", "A)", "Los átomos no se veían, y el modelo explicaba mediciones."),
            ex("Una muestra supuestamente de agua pura tiene 1 g de hidrógeno por cada 5 g de oxígeno. Según la proporción fija del agua, ¿qué se concluye?", "Que no es agua pura", "El agua pura tiene siempre 1 g de hidrógeno por 8 g de oxígeno."),
        ],
        "challenge": [
            ex("Un recipiente cerrado pesa 50 g antes y 50 g después de una reacción dentro de él. ¿Qué idea de la teoría de Dalton apoya este dato?", "Que los átomos solo se reordenan y la masa total se conserva", "No hubo pérdida ni ganancia de masa, igual que si los átomos se hubieran conservado."),
            ex("En otra prueba, el recipiente pesa 50 g antes y 46 g después. ¿Cuál es la explicación más probable? A) Se destruyeron átomos; B) Se escapó gas por un cierre defectuoso o hubo un error de medición", "B)", "La teoría predice que la masa se conserva en un sistema cerrado, así que se revisa el cierre y la medición."),
        ],
    },
    context=[ex("Un grupo mide la masa de una vela encendida y esta disminuye. Antes de decir que la masa no se conserva, ¿qué deben revisar?", "Si los gases producidos escaparon al aire", "Hay que pesar todo el sistema cerrado, incluidos los gases.")],
    selfcheck=[
        ex("¿Qué propuso Dalton sobre la forma del átomo?", "Que es una esfera maciza", "Para Dalton era una partícula sin partes."),
        ex("¿Un modelo atómico es una observación directa del átomo?", "No, es una representación para explicar mediciones", "Los modelos se proponen a partir de evidencias."),
        ex("¿Qué se conserva en un cambio químico en un recipiente cerrado?", "La masa total", "Los átomos solo se reordenan."),
    ],
    open_task=task(
        "Con estos datos de ejemplo escribe un informe corto. Tres muestras de agua pura tienen: muestra 1, 9 g con 1 g de hidrógeno y 8 g de oxígeno; muestra 2, 36 g con 4 g de hidrógeno y 32 g de oxígeno; muestra 3, 63 g con 7 g de hidrógeno y 56 g de oxígeno. Calcula la razón oxígeno/hidrógeno de cada una, explica qué idea de Dalton apoya y escribe una limitación de usar solo tres muestras.",
        "Razones: 8, 8 y 8. Apoya la idea de proporción fija. Limitación: son tres muestras y no se sabe si lo mismo ocurre con muestras de otros lugares.",
        ["tres razones calculadas", "idea de proporción fija", "una limitación"],
        ["tres divisiones", "frase de conclusión"],
        ["calcular la razón al revés", "concluir que se vieron los átomos"],
        "Pregunta cómo cambiaría el resultado si una muestra tuviera 9 g de oxígeno por cada 1 g de hidrógeno.",
    ),
    reinforce="Escribe con tus palabras tres ideas de la teoría de Dalton.",
    extend="Averigua con una persona de tu casa cómo ellos imaginaban de pequeños que estaba hecha la materia y compáralo con la idea de Dalton.",
)

# ================================================================ OA 12, clase 2
register(
    OA12, 2,
    materials="Papel y lápiz. Todos los resultados de los experimentos están escritos en el cuaderno.",
    use="Aprenderé a leer la evidencia de tres experimentos: los rayos catódicos, la lámina de oro y los espectros de luz. Sirve para ver qué dato obligó a cambiar cada modelo.",
    prior=["Conozco el modelo atómico de Dalton.", "Sé que las cargas opuestas se atraen y las iguales se repelen."],
    explain=[
        "En 1897, Thomson estudió los rayos catódicos, que son haces de partículas en un tubo con gas a muy baja presión. Los rayos se desviaban hacia una placa con carga positiva, así que tenían carga negativa. Eran los mismos con cualquier gas, por lo que esas partículas, los electrones, estaban en todos los átomos. Esto contradijo que el átomo fuera indivisible. Thomson imaginó el átomo como una esfera de carga positiva con electrones incrustados.",
        "Hacia 1911, Rutherford interpretó un experimento en que partículas con carga positiva atravesaban una lámina muy delgada de oro. Casi todas pasaban sin desviarse, algunas se desviaban mucho y muy pocas rebotaban. Concluyó que el átomo es casi todo espacio vacío y que tiene un núcleo muy pequeño, denso y positivo.",
        "Hacia 1913, Bohr explicó los espectros: el hidrógeno calentado emite luz de solo algunos colores definidos. Propuso que los electrones solo pueden estar en ciertos niveles de energía y que al bajar de uno a otro emiten luz de un color definido. Estos modelos se infieren de evidencia indirecta.",
    ],
    vocab=[("electrón", "partícula con carga negativa que forma parte de los átomos"), ("núcleo", "centro pequeño, denso y de carga positiva del átomo"), ("espectro", "conjunto de colores o líneas de luz que emite una sustancia"), ("nivel de energía", "valor de energía permitido para un electrón"), ("evidencia indirecta", "dato del que se infiere algo que no se ve")],
    worked=[
        {"title": "Rayos que se desvían", "problem": "En un tubo, un haz de partículas se desvía hacia una placa positiva. ¿Qué carga tienen y qué concluyó Thomson?", "steps": ["Las cargas opuestas se atraen: lo que se atrae a la placa positiva es negativo.", "Eran las mismas con cualquier gas, así que forman parte de todos los átomos."], "answer": "Carga negativa; los átomos tienen partículas más pequeñas dentro"},
        {"title": "Datos de la lámina de oro", "problem": "En una simulación de ejemplo, de 5.000 partículas, 4.995 atraviesan sin desviarse notoriamente y 5 rebotan o se desvían mucho. ¿Qué indican ambos datos?", "steps": ["Que casi todas atraviesen indica que el átomo es casi todo espacio vacío.", "Que muy pocas reboten indica una zona muy pequeña, densa y positiva."], "answer": "Espacio vacío en su mayor parte y un núcleo pequeño, denso y positivo"},
    ],
    mistakes=[
        {"wrong": "Decir que Rutherford vio los electrones girando alrededor del núcleo.", "why": "Se toma la interpretación como observación.", "fix": "Rutherford observó desviaciones de partículas y de ellas infirió el núcleo."},
        {"wrong": "Pensar que todos los gases dan el mismo espectro.", "why": "Se ignora que cada elemento tiene sus propias líneas.", "fix": "Cada elemento emite sus colores propios, como una huella."},
    ],
    tiers={
        "recovery": [
            ex("Los rayos de un tubo se desvían hacia una placa con carga positiva. ¿Qué carga tienen las partículas del rayo?", "Negativa", "Las cargas opuestas se atraen."),
            ex("En la lámina de oro casi todas las partículas atraviesan sin desviarse. ¿Qué indica sobre el átomo? A) Que es casi todo espacio vacío; B) Que es una esfera maciza", "A)", "Si casi nada choca, entre las partes del átomo hay mucho espacio vacío."),
            ex("Un gas calentado emite luz de solo algunos colores definidos. ¿Qué modelo lo explica mejor? A) Dalton; B) Rutherford; C) Bohr", "C)", "Los niveles de energía permitidos dan colores definidos."),
        ],
        "understand": [
            arith("En una simulación de ejemplo, de 10.000 partículas, 9.990 atraviesan sin desviarse notoriamente. ¿Cuántas no lo hacen?", "10000-9990", "Se restan las que atraviesan al total de partículas.", " partículas"),
            ex("Thomson obtuvo las mismas partículas con distintos gases en el tubo. ¿Qué concluyó?", "Que los electrones están en los átomos de todos los elementos", "Si no depende del gas, es un componente común de los átomos."),
            ex("En la lámina de oro algunas partículas rebotan. ¿Qué indican esos rebotes?", "Que hay una zona pequeña, densa y positiva en el átomo", "Una partícula positiva rebota al chocar con algo muy denso y positivo."),
        ],
        "apply": [
            ex("Líneas de luz de ejemplo: el elemento X emite rojo y verde; el Y, azul y violeta; el Z, rojo y azul. Una muestra desconocida emite rojo y azul. ¿Qué elemento contiene?", "El elemento Z", "Cada elemento tiene su conjunto de líneas, y solo Z tiene rojo y azul."),
            arith("En una simulación de ejemplo rebotan 4 de cada 10.000 partículas. Con la misma proporción, ¿cuántas rebotarían de 50.000?", "4*50000//10000", "Se multiplica la proporción por cinco veces más partículas.", " partículas"),
            ex("Une cada evidencia con su conclusión. Evidencias: (1) rayos desviados por una placa positiva; (2) algunas partículas rebotan en la lámina; (3) colores definidos al calentar un gas. Conclusiones: (a) niveles de energía; (b) partículas negativas en el átomo; (c) núcleo.", "(1) b; (2) c; (3) a", "Cada dato se relaciona con la conclusión del modelo que lo explica."),
        ],
        "reason": [
            ex("Gonzalo dice que el experimento de Rutherford demuestra que los electrones giran en círculos. ¿Qué dato sí apoya ese experimento?", "La existencia de un núcleo pequeño, denso y positivo", "El experimento muestra desviaciones de partículas, no trayectorias de electrones."),
            ex("El modelo de Thomson era una esfera positiva continua con electrones incrustados. ¿Qué dato de la lámina de oro lo contradice?", "Que algunas partículas rebotan", "Una esfera positiva uniforme no tendría un punto tan denso como para hacer rebotar."),
        ],
        "challenge": [
            ex("Un grupo repite la prueba con otra lámina y, de 10.000 partículas, 9.985 atraviesan. Pierre dice que esto refuta la idea de núcleo. ¿Tiene razón?", "No; que casi todas atraviesen es lo esperado con un núcleo muy pequeño", "Un núcleo muy pequeño ocupa poco espacio y casi todas pasan lejos de él."),
            ex("¿Por qué se dice que la estructura del átomo se conoce con evidencia indirecta?", "Porque se infiere a partir de efectos como desviaciones y colores, no se observa directamente su interior", "Las mediciones muestran efectos y de ellos se deduce la estructura."),
        ],
    },
    context=[ex("Un letrero con gas encerrado brilla con un color definido. Según el modelo de Bohr, ¿qué ocurre con los electrones del gas?", "Absorben energía, suben de nivel y al bajar emiten luz de un color definido", "La diferencia de energía entre niveles se emite como luz de un color definido.")],
    selfcheck=[
        ex("¿Qué experimento llevó a descubrir el electrón?", "El de los rayos catódicos de Thomson", "Los rayos se desviaban hacia una placa positiva."),
        ex("¿Qué carga tiene el núcleo del átomo?", "Positiva", "Hace rebotar partículas de carga positiva."),
        ex("¿Qué evidencia usó Bohr para su modelo?", "Los espectros de luz del hidrógeno", "Solo se emiten algunos colores definidos."),
    ],
    open_task=task(
        "Observa estos resultados de ejemplo de una lámina de oro: de 20.000 partículas, 19.996 atraviesan sin desviarse notoriamente y 4 rebotan. (1) Calcula cuántas no atraviesan. (2) Escribe qué dice cada dato sobre el átomo. (3) Explica por qué este resultado no cabe en un modelo de esfera positiva continua.",
        "(1) 4 partículas. (2) Casi todas atraviesan: el átomo es casi todo espacio vacío. Algunas rebotan: hay un núcleo pequeño y denso. (3) Una esfera positiva continua no tendría un centro tan denso como para hacer rebotar partículas.",
        ["resta correcta", "cada dato con su conclusión", "contraste con el modelo de Thomson"],
        ["tres respuestas escritas", "uso de las palabras núcleo y espacio vacío"],
        ["decir que los rebotes prueban electrones en órbita", "no explicar el contraste"],
        "Pregunta qué cambiaría si rebotaran 4.000 de 20.000 partículas.",
    ),
    reinforce="Escribe en una tabla de tres filas: experimento, qué se observó y qué concluyó cada científico.",
    extend="Averigua con una persona de tu casa cómo funciona un letrero luminoso con gas y qué colores tiene, sin tocar nada eléctrico.",
)

# ================================================================ OA 12, clase 3
register(
    OA12, 3,
    materials="Papel y lápiz. Las descripciones de los modelos están en el cuaderno.",
    use="Aprenderé a contrastar los modelos atómicos de Dalton, Thomson, Rutherford y Bohr y a ubicar las partículas del átomo. Sirve para saber qué explica cada modelo y qué le falta.",
    prior=["Conozco la evidencia de los tres experimentos.", "Sé que las cargas opuestas se atraen."],
    explain=[
        "Dalton: átomo como esfera maciza e indivisible. Thomson: esfera de carga positiva con electrones incrustados, como un pudín con pasas. Rutherford: un núcleo pequeño, denso y positivo, con electrones alrededor y mucho espacio vacío. Bohr: el núcleo de Rutherford, con electrones en niveles de energía definidos. Cada modelo explica los datos de su época y deja preguntas.",
        "El átomo tiene tres partículas. Los protones tienen carga positiva y están en el núcleo. Los neutrones no tienen carga y también están en el núcleo. Los electrones tienen carga negativa y están fuera del núcleo. Protones y neutrones tienen casi la misma masa; un electrón tiene una masa unas 2.000 veces menor. Un átomo es neutro cuando tiene igual número de protones que de electrones.",
        "Si un átomo gana o pierde electrones, se transforma en un ion. Su carga neta es el número de protones menos el de electrones. Por ejemplo, 11 protones y 10 electrones dan carga +1. Los niveles de Bohr se llenan desde el más cercano al núcleo: el primero admite hasta 2 electrones y el segundo hasta 8.",
    ],
    vocab=[("protón", "partícula positiva del núcleo"), ("neutrón", "partícula sin carga del núcleo"), ("ion", "átomo con carga neta por ganar o perder electrones"), ("átomo neutro", "átomo con igual número de protones y de electrones"), ("subatómica", "partícula más pequeña que el átomo")],
    worked=[
        {"title": "Qué explica cada modelo", "problem": "Un modelo debe explicar que las partículas positivas rebotan en una lámina de oro. ¿Cuál lo hace: Thomson o Rutherford?", "steps": ["El modelo de Thomson no tiene un centro denso.", "El modelo de Rutherford tiene un núcleo denso y positivo que repele y hace rebotar."], "answer": "El de Rutherford"},
        {"title": "Carga de un ion", "problem": "Un átomo tiene 12 protones y 10 electrones. ¿Cuál es su carga neta?", "steps": ["Carga neta es protones menos electrones.", "12 − 10 = 2, así que tiene carga +2."], "answer": "+2"},
    ],
    mistakes=[
        {"wrong": "Decir que el núcleo contiene los electrones.", "why": "Se confunden las partículas del núcleo con las que están fuera.", "fix": "El núcleo tiene protones y neutrones; los electrones están fuera."},
        {"wrong": "Pensar que un modelo anterior era una mentira.", "why": "Se ignora que explicaba la evidencia de su tiempo.", "fix": "Cada modelo fue útil y se mejoró con nueva evidencia."},
    ],
    tiers={
        "recovery": [
            ex("¿Dónde se encuentran los protones del átomo?", "En el núcleo", "Junto con los neutrones forman el núcleo."),
            ex("¿Qué carga tiene el neutrón?", "Ninguna, es neutro", "Su nombre indica que no tiene carga."),
            ex("¿Qué modelo propone un núcleo central y electrones en niveles de energía definidos?", "El de Bohr", "Bohr agregó niveles al núcleo de Rutherford."),
        ],
        "understand": [
            ex("¿Qué agregó Rutherford al modelo de Thomson?", "Un núcleo pequeño, denso y positivo", "La esfera de Thomson no tenía un centro denso."),
            ex("Un átomo neutro tiene 11 protones. ¿Cuántos electrones tiene?", "11", "En un átomo neutro la carga positiva y la negativa se igualan."),
            ex("¿Por qué en el modelo de Rutherford la mayor parte del átomo es espacio vacío?", "Porque el núcleo es muy pequeño frente al tamaño total del átomo", "Casi todo el volumen es el espacio donde están los electrones."),
        ],
        "apply": [
            arith("Un ion tiene 17 protones y 18 electrones. ¿Cuál es su carga neta, en unidades de carga? Escribe el signo si es negativa.", "17-18", "Carga neta es protones menos electrones.", ""),
            arith("Un ion tiene 20 protones y 18 electrones. ¿Cuál es su carga neta?", "20-18", "Se restan los electrones a los protones.", ""),
            ex("¿Qué observación no puede explicar el modelo de Dalton? A) Que existen partículas con carga dentro del átomo; B) Que los átomos se reordenan en un cambio químico", "A)", "Dalton no tenía partes dentro del átomo; la segunda sí la explicaba."),
        ],
        "reason": [
            ex("Un compañero dice que los modelos atómicos son fotografías de átomos. Corrige su afirmación.", "Son representaciones propuestas a partir de evidencia indirecta", "Un átomo no se ve como en un dibujo; el modelo explica los datos."),
            ex("Marta dice que el modelo de Bohr dejó falso el de Rutherford. ¿Qué es más preciso? A) Bohr conservó el núcleo y agregó niveles de energía; B) Bohr eliminó el núcleo", "A)", "Los modelos se mejoran sin descartar lo que sigue siendo válido."),
        ],
        "challenge": [
            arith("En un átomo neutro de 3 protones, el primer nivel se llena con 2 electrones. ¿Cuántos electrones van en el segundo nivel?", "3-2", "El total de electrones es 3 y 2 ya están en el primer nivel.", " electrón"),
            ex("En el modelo de Rutherford el núcleo tenía solo protones. Más tarde se halló que también tiene neutrones. ¿Qué parte del modelo se modificó?", "La composición del núcleo", "El resto del modelo sigue siendo útil."),
        ],
    },
    context=[ex("Una página web muestra un átomo con electrones girando como planetas alrededor de una bolita. ¿Qué advertencia hay que hacer?", "Es un modelo, no la forma real del átomo", "Los dibujos son representaciones, con límites.")],
    selfcheck=[
        ex("¿Qué carga tiene un electrón?", "Negativa", "Es atraído por placas positivas."),
        ex("¿Qué partículas forman el núcleo?", "Protones y neutrones", "Ambas están en el centro del átomo."),
        ex("¿Cuántos electrones caben en el primer nivel de energía?", "Hasta 2", "El primer nivel se llena con 2."),
    ],
    open_task=task(
        "Completa una tabla de comparación con cuatro filas (Dalton, Thomson, Rutherford y Bohr) y tres columnas: cómo es el átomo, qué evidencia explica y qué le falta. Luego dibuja un átomo neutro con 5 protones, 6 neutrones y 5 electrones, indicando cuántos electrones van en cada nivel (2 y 3).",
        "Fila Rutherford: núcleo pequeño y positivo con electrones alrededor; explica el rebote de partículas; le falta explicar los colores. Dibujo: núcleo con 5 p y 6 n; nivel 1 con 2 e; nivel 2 con 3 e.",
        ["cuatro filas completas", "una evidencia correcta por fila", "dibujo con 5 + 6 + 5 partículas"],
        ["tabla", "dibujo con los niveles"],
        ["poner electrones en el núcleo", "dibujar 4 electrones"],
        "Pregunta qué carga neta tendría el dibujo si se quitara un electrón.",
    ),
    reinforce="Escribe una oración que describa cada partícula subatómica con su carga y su lugar.",
    extend="Haz con papel un modelo de núcleo con bolitas de dos colores, sin tijeras peligrosas, y cuenta cuántos protones y neutrones usaste.",
)

# ================================================================ OA 12, clase 4
register(
    OA12, 4,
    materials="Papel y lápiz. La tabla de ejemplo está escrita en el cuaderno.",
    use="Aprenderé a relacionar número atómico, masa atómica y número de partículas. Sirve para calcular cuántos protones, neutrones y electrones tiene un átomo.",
    prior=["Conozco protón, neutrón y electrón.", "Sé que un átomo neutro tiene igual número de protones y electrones."],
    explain=[
        "El número atómico (Z) es el número de protones de un átomo. Identifica al elemento: todos los átomos con 6 protones son de carbono. En un átomo neutro, Z es también el número de electrones. La masa atómica (A) es, aproximadamente, la suma de protones y neutrones, porque los electrones pesan muy poco. En la tabla periódica se da un valor promedio.",
        "Con estos dos datos se calcula el número de neutrones: neutrones = A − Z. Tabla de ejemplo (símbolo: Z, A redondeada): H: 1 y 1; C: 6 y 12; N: 7 y 14; O: 8 y 16; Na: 11 y 23; Al: 13 y 27.",
        "Los átomos de un mismo elemento pueden tener distinto número de neutrones. Se llaman isótopos. Tienen el mismo Z y distinta masa atómica. Número atómico y masa atómica no son lo mismo: Z cuenta solo protones, A cuenta protones y neutrones.",
    ],
    vocab=[("número atómico (Z)", "número de protones de un átomo"), ("masa atómica (A)", "valor aproximado de protones más neutrones"), ("isótopo", "átomo del mismo elemento con distinto número de neutrones"), ("símbolo químico", "letra o letras que representan un elemento")],
    worked=[
        {"title": "Neutrones del sodio", "problem": "El sodio (Na) tiene Z = 11 y A = 23. ¿Cuántos protones, neutrones y electrones tiene un átomo neutro?", "steps": ["Protones = Z = 11 y electrones = 11 en un átomo neutro.", "Neutrones = A − Z = 23 − 11 = 12."], "answer": "11 protones, 12 neutrones y 11 electrones"},
        {"title": "Identificar el elemento", "problem": "Un átomo tiene 8 protones y 8 neutrones. ¿Qué elemento es y cuál es su A?", "steps": ["Z = 8 corresponde al oxígeno en la tabla de ejemplo.", "A = 8 + 8 = 16."], "answer": "Oxígeno, A = 16"},
    ],
    mistakes=[
        {"wrong": "Confundir número atómico con masa atómica.", "why": "Se piensa que ambos cuentan lo mismo.", "fix": "Z cuenta protones; A cuenta protones más neutrones."},
        {"wrong": "Decir que dos átomos con distinto número de neutrones son elementos distintos.", "why": "Se identifica el elemento por la masa y no por Z.", "fix": "El elemento lo define Z; distinto número de neutrones da isótopos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué cuenta el número atómico (Z)?", "Los protones", "Z es el número de protones."),
            arith("Un átomo de carbono tiene Z = 6 y A = 12. ¿Cuántos neutrones tiene?", "12-6", "Neutrones es A menos Z.", " neutrones"),
            ex("¿Cuántos electrones tiene un átomo neutro de nitrógeno (Z = 7)?", "7", "Un átomo neutro tiene tantos electrones como protones."),
        ],
        "understand": [
            ex("Dos átomos tienen 8 protones; uno tiene 8 neutrones y el otro 10. ¿Son del mismo elemento?", "Sí, porque tienen el mismo Z", "El elemento lo define el número de protones."),
            ex("¿Qué número identifica a un elemento? A) El número de neutrones; B) El número atómico", "B)", "Cada elemento tiene un Z propio."),
            ex("¿Por qué A es casi la suma de protones y neutrones y no incluye a los electrones?", "Porque los electrones tienen una masa muy pequeña", "El electrón pesa unas 2.000 veces menos que un protón."),
        ],
        "apply": [
            arith("El aluminio (Al) tiene Z = 13 y A = 27. ¿Cuántos neutrones tiene?", "27-13", "Se resta Z a A.", " neutrones"),
            arith("Un átomo tiene 16 protones y 16 neutrones. ¿Cuál es su masa atómica aproximada?", "16+16", "A es la suma de protones y neutrones.", ""),
            arith("Un átomo tiene A = 19 y 10 neutrones. ¿Cuál es su número atómico?", "19-10", "Z es A menos los neutrones.", ""),
        ],
        "reason": [
            ex("Un átomo X tiene Z = 18 y A = 40. Otro átomo Y tiene Z = 19 y A = 39. ¿El de mayor masa atómica tiene más protones?", "No; X tiene mayor masa (40) pero menos protones (18)", "La masa depende de protones y neutrones, no solo de Z."),
            arith("Un átomo neutro tiene Z = 15 y A = 31. ¿Cuántos neutrones tiene?", "31-15", "Se resta Z a A. Tiene además 15 electrones.", " neutrones"),
        ],
        "challenge": [
            ex("Un ion tiene 12 protones, 12 neutrones y 10 electrones. ¿Cuál es su carga neta?", "+2", "12 − 10 = 2, y hay más protones que electrones.", calc="12-10"),
            ex("El núcleo X tiene 6 protones y 6 neutrones, y el núcleo Y tiene 6 protones y 8 neutrones. ¿Qué tienen en común y en qué difieren?", "Son del mismo elemento (Z = 6) y difieren en A: 12 y 14", "Son isótopos del mismo elemento."),
        ],
    },
    context=[ex("Una etiqueta de ejemplo dice: «oxígeno, Z = 8, A = 16». ¿Cuántos protones, neutrones y electrones tiene un átomo neutro?", "8 protones, 8 neutrones y 8 electrones", "Z da protones y electrones, y A − Z da neutrones.")],
    selfcheck=[
        ex("¿Qué se obtiene al restar Z a A?", "El número de neutrones", "A es protones más neutrones."),
        ex("¿Cómo se llama el átomo del mismo elemento con distinto número de neutrones?", "Isótopo", "Cambian en masa pero no en Z."),
        ex("¿Qué partícula tiene una masa muy pequeña comparada con las demás?", "El electrón", "Pesa unas 2.000 veces menos que un protón."),
    ],
    open_task=task(
        "Con la tabla de ejemplo de la explicación (H: 1 y 1; C: 6 y 12; N: 7 y 14; O: 8 y 16; Na: 11 y 23; Al: 13 y 27), arma una tabla con columnas: elemento, protones, neutrones y electrones del átomo neutro. Completa las seis filas. Después responde: ¿cuál de los seis tiene más neutrones y cuántos?",
        "H: 1, 0, 1; C: 6, 6, 6; N: 7, 7, 7; O: 8, 8, 8; Na: 11, 12, 11; Al: 13, 14, 13. Más neutrones: Al, con 14.",
        ["seis filas calculadas", "uso de A − Z", "respuesta final correcta"],
        ["tabla de seis filas", "frase final"],
        ["poner igual neutrones y protones en todos", "restar A y Z al revés"],
        "Pregunta cuántos neutrones tendría un isótopo del carbono con A = 14.",
    ),
    reinforce="Escribe la fórmula para calcular los neutrones y un ejemplo propio con números.",
    extend="Busca con una persona de tu casa dónde ven símbolos químicos (envases, etiquetas) y anota tres símbolos y su elemento.",
)

# ================================================================ OA 12, clase 5
register(
    OA12, 5,
    materials="Papel y lápiz. Las tablas están escritas en el cuaderno.",
    use="Aprenderé a explicar cómo y por qué cambiaron los modelos atómicos con la evidencia, y a comunicar los límites. Sirve para argumentar con datos en vez de memorizar nombres.",
    prior=["Conozco los cuatro modelos y la evidencia de cada uno.", "Sé calcular partículas con Z y A."],
    explain=[
        "Los modelos científicos cambian cuando aparece evidencia que no explican. Orden histórico: Dalton (átomo macizo), Thomson (electrones dentro de una esfera positiva), Rutherford (núcleo) y Bohr (niveles de energía). Cada cambio tiene un dato que lo obligó: el electrón desvió los rayos catódicos, los rebotes en la lámina mostraron el núcleo y los colores definidos mostraron niveles.",
        "Al ubicar los electrones, el primer nivel admite 2 electrones y el segundo hasta 8. El neón (10 electrones) tiene niveles llenos: 2 y 8. El litio (3 electrones) tiene 2 y 1. Cuando el segundo nivel está lleno, los electrones siguientes van al tercero. Un electrón que absorbe energía sube de nivel, y cuando baja emite luz de un color definido. Cada elemento tiene niveles distintos, por eso emite colores distintos.",
        "El modelo de Bohr explica bien al hidrógeno, pero no a todos los átomos; por eso la ciencia lo mejoró con modelos posteriores que verás más adelante. Una buena conclusión dice qué explica el modelo y qué límites tiene. Nunca presentes un dibujo como si fuera la imagen real de un átomo.",
    ],
    vocab=[("evidencia", "dato medido que apoya o contradice una idea"), ("modelo científico", "representación que explica datos y puede cambiar"), ("nivel lleno", "nivel con el número máximo de electrones"), ("limitación", "parte que el modelo o el estudio no alcanza a explicar")],
    worked=[
        {"title": "De Dalton a Thomson", "problem": "¿Qué evidencia obligó a cambiar el modelo de átomo indivisible?", "steps": ["Los rayos catódicos se desviaban hacia una placa positiva y eran los mismos con cualquier gas.", "Eso mostró partículas negativas dentro de todos los átomos, así que el átomo tiene partes."], "answer": "El descubrimiento del electrón"},
        {"title": "Electrones por nivel", "problem": "Distribuye los 9 electrones del átomo de flúor en niveles.", "steps": ["El primer nivel se llena con 2.", "Quedan 7, que caben en el segundo nivel, que admite hasta 8."], "answer": "2 en el primer nivel y 7 en el segundo"},
    ],
    mistakes=[
        {"wrong": "Decir que el modelo de Bohr es la imagen real de un átomo.", "why": "Se toma una representación como fotografía.", "fix": "Es un modelo con límites, útil para explicar ciertos datos."},
        {"wrong": "Ordenar los modelos por lo que más se parece a un dibujo.", "why": "No se usa el orden en que apareció la evidencia.", "fix": "El orden histórico es Dalton, Thomson, Rutherford y Bohr."},
    ],
    tiers={
        "recovery": [
            ex("Escribe en orden histórico los cuatro modelos: Bohr, Dalton, Rutherford y Thomson.", "Dalton, Thomson, Rutherford, Bohr", "Cada modelo cambió por nueva evidencia posterior."),
            ex("¿Qué evidencia llevó a pasar del modelo de Thomson al de Rutherford?", "Los rebotes de partículas en la lámina de oro", "Mostraron un núcleo pequeño y denso."),
            ex("¿Qué hace que un modelo científico cambie?", "Evidencia nueva que el modelo no explica", "Un modelo se modifica cuando no explica los datos."),
        ],
        "understand": [
            ex("¿Qué evidencia llevó a Bohr a proponer niveles de energía? A) Los rebotes en la lámina de oro; B) Los colores definidos que emite un gas", "B)", "Solo se emitían ciertos colores, lo que sugiere energías permitidas."),
            ex("¿Por qué no se descarta del todo el modelo de Bohr aunque tiene límites?", "Porque explica bien datos del hidrógeno y sirve como base de modelos posteriores", "Un modelo limitado sigue siendo útil donde funciona."),
            ex("Un electrón sube de nivel y luego vuelve al inferior. ¿Qué ocurre al volver?", "Emite luz de un color definido", "La energía sobrante sale como luz."),
        ],
        "apply": [
            arith("¿Cuántos electrones caben como máximo en los dos primeros niveles juntos?", "2+8", "El primer nivel admite 2 y el segundo hasta 8.", " electrones"),
            ex("El neón (Z = 10) tiene 10 electrones. ¿Cómo se distribuyen en los niveles?", "2 en el primer nivel y 8 en el segundo", "Primero se llena el nivel de 2 y luego el de 8."),
            ex("El litio (Z = 3) tiene 3 electrones. ¿Cómo se distribuyen?", "2 en el primer nivel y 1 en el segundo", "El primer nivel se llena antes de usar el siguiente."),
        ],
        "reason": [
            ex("Gonzalo dice que Bohr descubrió los niveles viendo directamente a los electrones. ¿Qué evidencia usó en realidad?", "Los espectros de luz, que son evidencia indirecta", "Infirió los niveles a partir de los colores emitidos."),
            ex("¿Cuál es la conclusión mejor redactada? A) Los átomos son exactamente como en la figura de Bohr; B) El modelo de Bohr explica los colores del hidrógeno, pero es un modelo y tiene límites", "B)", "Una buena conclusión dice lo que explica y lo que no."),
        ],
        "challenge": [
            ex("Tabla de ejemplo (explica sí o no). Observación 1, existen electrones: Dalton no, Thomson sí, Rutherford sí, Bohr sí. Observación 2, hay un núcleo: Dalton no, Thomson no, Rutherford sí, Bohr sí. Observación 3, colores definidos: solo Bohr sí. ¿Qué modelo explica las tres observaciones?", "El de Bohr", "Es el único que tiene un sí en las tres filas."),
            ex("Si apareciera evidencia de que el electrón no sigue una órbita fija, ¿qué debería hacer la ciencia con el modelo de Bohr? A) Ignorar la evidencia; B) Revisarlo y ajustarlo", "B)", "Los modelos se corrigen con nueva evidencia."),
        ],
    },
    context=[ex("Un video de fuegos artificiales muestra luces de distintos colores. ¿Qué idea de Bohr explica que distintos elementos den colores distintos?", "Cada elemento tiene niveles de energía distintos, así que emite colores distintos", "Los saltos entre niveles de cada elemento emiten luz propia.")],
    selfcheck=[
        ex("¿Qué científico propuso el núcleo del átomo?", "Rutherford", "Interpretó los rebotes de la lámina de oro."),
        ex("¿Cuántos electrones tiene el segundo nivel lleno de un átomo?", "8", "El segundo nivel admite hasta 8."),
        ex("¿Qué parte debe tener una buena conclusión además de lo que el modelo explica?", "Su limitación", "Un modelo no explica todo."),
    ],
    open_task=task(
        "Escribe una línea de tiempo de cuatro pasos con los modelos Dalton, Thomson, Rutherford y Bohr. En cada paso anota: qué evidencia nueva apareció, qué cambió en el modelo y una limitación del modelo. Después, usando los niveles de energía, dibuja la distribución de electrones del sodio (11 electrones).",
        "Paso Rutherford: evidencia, rebotes en la lámina; cambio, aparece el núcleo; limitación, no explica los colores. Sodio: 2 electrones en el primer nivel, 8 en el segundo y 1 en el tercero.",
        ["cuatro pasos en orden correcto", "evidencia, cambio y limitación en cada uno", "distribución 2, 8, 1"],
        ["línea de tiempo", "dibujo de niveles"],
        ["ordenar mal los modelos", "poner 11 electrones en un solo nivel"],
        "Pregunta qué evidencia nueva podría obligar a cambiar el modelo de Bohr.",
    ),
    reinforce="Explica en dos oraciones por qué se dice que los modelos atómicos son provisionales.",
    extend="Con una persona de tu casa, comenten qué otra idea científica que hayan aprendido cambió con el tiempo.",
)
