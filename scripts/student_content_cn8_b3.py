"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 13 (átomos, partículas y formación de sustancias)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA13 = "CN08 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 13, clase 1
register(
    OA13, 1,
    materials="Papel y lápiz. Todas las fórmulas y descripciones están escritas en el cuaderno.",
    use="Aprenderé a distinguir elementos, compuestos y mezclas desde los átomos que los forman y a plantear preguntas investigables sobre ellos. Sirve para clasificar sustancias con un criterio y no por su apariencia.",
    prior=["Conozco el átomo, el número atómico y las partículas subatómicas.", "Sé que las partículas de la materia se mueven y se atraen."],
    explain=[
        "Toda la materia está formada por átomos que interactúan, es decir, que se atraen y se unen entre sí. Un elemento es una sustancia formada por un solo tipo de átomo, como el oxígeno (O2) o el hierro (Fe). Un compuesto es una sustancia formada por átomos de distintos elementos unidos en proporción fija, como el agua (H2O) o la sal (NaCl). Una molécula es un grupo de átomos unidos, como O2, H2O o CO2.",
        "La fórmula dice qué átomos hay y cuántos. En H2O hay 2 átomos de hidrógeno y 1 de oxígeno: el subíndice indica la cantidad, y si no hay número, es 1. Un número delante de la fórmula, como en 3 H2O, indica cuántas moléculas hay. Una mezcla tiene dos o más sustancias que no están unidas entre sí en proporción fija: el aire, el agua con sal o el jugo. Sus componentes se pueden separar sin cambiarlos.",
        "Una pregunta investigable sobre sustancias se puede responder con una medición, por ejemplo: «¿Qué masa de sal queda al evaporar 100 mL de agua con sal?». Para clasificar, mira primero si es una sola sustancia o varias y, si es una sola, cuántos tipos de átomos tiene.",
    ],
    vocab=[("elemento", "sustancia formada por un solo tipo de átomo"), ("compuesto", "sustancia formada por átomos de distintos elementos en proporción fija"), ("molécula", "grupo de átomos unidos"), ("mezcla", "varias sustancias juntas, sin proporción fija ni enlace entre ellas"), ("fórmula química", "escritura que indica qué átomos hay y cuántos")],
    worked=[
        {"title": "Clasificar por la fórmula", "problem": "Clasifica CO2 y N2 como elemento o compuesto.", "steps": ["CO2 tiene átomos de dos elementos distintos: carbono y oxígeno.", "N2 tiene solo átomos de nitrógeno."], "answer": "CO2 es compuesto y N2 es elemento"},
        {"title": "Contar átomos", "problem": "¿Cuántos átomos hay en 2 moléculas de NH3?", "steps": ["Una molécula de NH3 tiene 1 átomo de N y 3 de H: 4 átomos.", "Dos moléculas tienen 2 × 4 = 8 átomos."], "answer": "8 átomos"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua con sal es un compuesto nuevo.", "why": "Se confunde mezclar con combinar átomos en proporción fija.", "fix": "Es una mezcla: al evaporar el agua, la sal reaparece sin haber cambiado."},
        {"wrong": "Pensar que O2 es un compuesto porque tiene dos átomos.", "why": "Se cuenta el número de átomos y no los tipos.", "fix": "O2 tiene un solo tipo de átomo, así que es un elemento."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es una molécula? A) Un grupo de átomos unidos; B) Un átomo solo", "A)", "Una molécula tiene dos o más átomos unidos."),
            ex("O2 es una sustancia formada por dos átomos de oxígeno. ¿Es un elemento o un compuesto?", "Un elemento", "Solo tiene un tipo de átomo."),
            ex("NaCl es sal de mesa, formada por sodio y cloro en proporción fija. ¿Es un elemento o un compuesto?", "Un compuesto", "Tiene átomos de dos elementos distintos unidos."),
        ],
        "understand": [
            ex("El aire contiene moléculas de nitrógeno, de oxígeno y otras. ¿Es una sustancia pura o una mezcla?", "Una mezcla", "Tiene varias sustancias sin proporción fija."),
            ex("¿Qué átomos indica la fórmula CO2?", "1 átomo de carbono y 2 de oxígeno", "El subíndice 2 corresponde al oxígeno y el carbono tiene 1."),
            ex("H2O y H2O2 ¿son la misma sustancia? Responde sí o no.", "No", "Tienen distinta cantidad de oxígeno por molécula, por lo que son sustancias distintas."),
        ],
        "apply": [
            arith("Una molécula de propano tiene la fórmula C3H8. ¿Cuántos átomos tiene en total?", "3+8", "Se suman los átomos de carbono y de hidrógeno.", " átomos"),
            arith("¿Cuántos átomos hay en 4 moléculas de H2O?", "4*3", "Cada molécula tiene 3 átomos.", " átomos"),
            ex("¿Cuál es una pregunta investigable? A) ¿Cuántos gramos de sal quedan al evaporar 100 mL de agua con sal?; B) ¿Qué sustancia es más bonita?", "A)", "Se puede responder midiendo una masa."),
        ],
        "reason": [
            ex("Alberto dice que el agua con sal es un compuesto porque tiene dos sustancias unidas. ¿Qué dato lo corrige?", "Al evaporar el agua reaparece la sal sin cambios, así que es una mezcla", "Las sustancias de una mezcla se separan sin cambiar."),
            ex("Una sustancia pura tiene átomos de dos tipos unidos siempre en proporción 2 a 1. ¿Es elemento, compuesto o mezcla?", "Compuesto", "Dos tipos de átomos en proporción fija son un compuesto."),
        ],
        "challenge": [
            arith("En 4 moléculas de CO2, ¿cuántos átomos de oxígeno hay?", "4*2", "Cada molécula tiene 2 átomos de oxígeno.", " átomos"),
            arith("Una muestra tiene 100 átomos de oxígeno en parejas (moléculas O2). ¿Cuántas moléculas son?", "100//2", "Cada molécula usa 2 átomos.", " moléculas"),
        ],
    },
    context=[ex("En el aire hay moléculas de N2, O2 y CO2. ¿Cuál de ellas es un compuesto?", "CO2", "Tiene dos elementos distintos, carbono y oxígeno.")],
    selfcheck=[
        ex("¿Cuántos tipos de átomos tiene un elemento?", "Uno", "Un elemento está formado por un solo tipo de átomo."),
        ex("¿Qué indica el número delante de una fórmula, como el 3 en 3 H2O?", "Cuántas moléculas hay", "El subíndice cuenta átomos y el número delante cuenta moléculas."),
        ex("¿Cómo se pueden separar los componentes de una mezcla?", "Sin cambiar las sustancias, por medios físicos como evaporar", "En una mezcla los componentes mantienen su identidad."),
    ],
    open_task=task(
        "Clasifica estas siete sustancias como elemento, compuesto o mezcla: (1) O2; (2) H2O; (3) agua con azúcar; (4) Fe; (5) CO2; (6) aire; (7) N2. Escribe una frase que justifique cada una. Después formula una pregunta investigable sobre el agua con sal indicando qué cambias, qué mides y qué mantienes igual.",
        "(1) elemento, un solo tipo de átomo. (2) compuesto, H y O en proporción fija. (3) mezcla, se puede separar. Pregunta: ¿Cuántos gramos de sal sólida quedan al evaporar 100 mL de agua cuando se disuelven 2 g, 5 g o 10 g de sal? Cambio: los gramos de sal disueltos. Mido: la masa del residuo seco. Mantengo igual: 100 mL de agua y la temperatura.",
        ["siete clasificaciones correctas", "una frase de justificación en cada una", "pregunta con variables"],
        ["tabla de siete filas", "pregunta escrita"],
        ["clasificar por el número de átomos y no por el tipo", "pregunta sin algo que medir"],
        "Pregunta cómo cambiaría la clasificación si el agua con azúcar se hirviera hasta dejar solo azúcar.",
    ),
    reinforce="Escribe una definición propia de elemento, de compuesto y de mezcla, con un ejemplo cada una.",
    extend="Con una persona de tu casa, busca la etiqueta de un producto de cocina y anota una sustancia pura y una mezcla que encuentres.",
)

# ================================================================ OA 13, clase 2
register(
    OA13, 2,
    materials="Papel y lápiz. Los dibujos de partículas están descritos con palabras y símbolos en el cuaderno.",
    use="Aprenderé a leer fórmulas, modelos de átomos unidos y cajas de partículas. Sirve para saber, a partir de una representación, qué sustancia hay y cuántos átomos tiene.",
    prior=["Sé distinguir elemento, compuesto y mezcla.", "Sé leer una fórmula con subíndices."],
    explain=[
        "Las sustancias se representan de varias formas. La fórmula, como CH4, dice cuántos átomos de cada tipo hay. El modelo de líneas dibuja los átomos y une los que están unidos: H–O–H es el agua, O=C=O es el dióxido de carbono y N≡N es el nitrógeno. Cada línea representa un par de electrones compartido, y las dobles o triples son enlaces más fuertes.",
        "En una caja de partículas se dibujan muchas moléculas juntas. En las cajas de esta clase, si todas las moléculas son iguales y tienen un solo tipo de átomo, es un elemento. Si todas son iguales y tienen átomos de dos o más tipos, es un compuesto. Si hay moléculas de distinto tipo, es una mezcla.",
        "Los modelos de átomos y moléculas son representaciones: no muestran el color real ni el tamaño real de los átomos. Sirven para contar y para explicar, y por eso toda representación debe leerse con sus límites.",
    ],
    vocab=[("modelo de líneas", "dibujo que une con líneas los átomos enlazados"), ("enlace", "unión entre átomos"), ("caja de partículas", "dibujo de muchas partículas juntas en un recipiente"), ("representación", "dibujo o fórmula que muestra algo que no se ve")],
    worked=[
        {"title": "Leer un modelo de líneas", "problem": "El modelo O=C=O representa una molécula. ¿Qué fórmula tiene y cuántos átomos?", "steps": ["Hay un átomo de C en el centro y dos átomos de O.", "La fórmula es CO2 y tiene 3 átomos."], "answer": "CO2, con 3 átomos"},
        {"title": "Leer una caja de partículas", "problem": "Una caja tiene cuatro moléculas iguales, cada una con un átomo de hidrógeno y uno de cloro. ¿Elemento, compuesto o mezcla?", "steps": ["Todas las moléculas son iguales: es una sola sustancia.", "Cada molécula tiene dos tipos de átomos: es un compuesto."], "answer": "Compuesto"},
    ],
    mistakes=[
        {"wrong": "Creer que un átomo es del color de la bolita del modelo.", "why": "Se toma el color como un dato real.", "fix": "El color de los modelos es solo una convención para distinguir átomos."},
        {"wrong": "Clasificar como compuesto una caja con moléculas O2 y N2.", "why": "Se piensa que dos tipos de átomos siempre forman un compuesto.", "fix": "Hay dos tipos de moléculas distintas: es una mezcla de elementos."},
    ],
    tiers={
        "recovery": [
            ex("En el modelo H–O–H, ¿cuántos átomos de hidrógeno hay?", "2", "Hay uno en cada extremo de la molécula."),
            ex("¿Qué representa cada línea en un modelo de líneas?", "Un enlace, un par de electrones compartido", "Las líneas muestran qué átomos están unidos."),
            ex("¿Qué fórmula tiene la molécula O=C=O?", "CO2", "Tiene un carbono y dos oxígenos."),
        ],
        "understand": [
            ex("Caja 1: tres moléculas iguales, cada una con dos átomos del mismo tipo. ¿Qué es?", "Un elemento", "Una sola sustancia con un solo tipo de átomo."),
            ex("Caja 2: tres moléculas iguales, cada una con un átomo de tipo ○ y uno de tipo ●. ¿Qué es?", "Un compuesto", "Una sola sustancia con dos tipos de átomos."),
            ex("Caja 3: dos moléculas con dos átomos ○ y dos moléculas con un ○ y un ●. ¿Qué es?", "Una mezcla", "Hay dos sustancias distintas juntas."),
        ],
        "apply": [
            ex("Una molécula de metano tiene un átomo de carbono unido a cuatro de hidrógeno. ¿Qué fórmula tiene?", "CH4", "Un carbono y cuatro hidrógenos."),
            arith("¿Cuántos átomos hay en 5 moléculas de CH4?", "5*5", "Cada molécula tiene 5 átomos.", " átomos"),
            arith("¿Cuántos átomos de hidrógeno hay en 7 moléculas de H2O?", "7*2", "Cada molécula tiene 2 átomos de hidrógeno.", " átomos"),
        ],
        "reason": [
            ex("Una caja tiene dos moléculas con dos átomos ○ y dos moléculas con un ○ y un ●. Un compañero dice que es un compuesto porque tiene dos tipos de átomos. ¿Qué dato lo corrige?", "Hay dos tipos de moléculas distintas, por lo que es una mezcla", "Un compuesto tiene todas las moléculas iguales."),
            ex("Hay dos sustancias: N2 y NH3. ¿Cuál es un compuesto y por qué?", "NH3, porque tiene dos tipos de átomos unidos", "N2 tiene un solo tipo de átomo."),
        ],
        "challenge": [
            arith("Una molécula de glucosa tiene 6 átomos de carbono, 12 de hidrógeno y 6 de oxígeno. ¿Cuántos átomos de hidrógeno hay en 2 moléculas?", "2*12", "Se multiplica por la cantidad de moléculas.", " átomos"),
            ex("¿Los modelos de bolas muestran el color real de los átomos? A) Sí; B) No, el color es una convención", "B)", "Los átomos no tienen colores como las bolitas de los modelos."),
        ],
    },
    context=[ex("Un dibujo muestra moléculas de agua en el hielo y luego el mismo hielo derretido. ¿Qué cambia? A) Las moléculas se separan en átomos; B) Las moléculas se mueven más y siguen siendo H2O", "B)", "Derretir es un cambio de estado, no rompe las moléculas.")],
    selfcheck=[
        ex("¿Cuántos átomos de oxígeno hay en la molécula O=C=O?", "2", "Hay uno en cada extremo."),
        ex("¿Cuándo una caja de partículas representa un elemento?", "Cuando todas las moléculas son iguales y tienen un solo tipo de átomo", "Es una sola sustancia con un único tipo de átomo."),
        ex("¿Qué limitación tiene un modelo de bolas?", "No muestra el color ni el tamaño real", "Es una representación, no una fotografía."),
    ],
    open_task=task(
        "Observa estas tres cajas descritas con letras. Caja X: cinco moléculas H–H. Caja Y: cuatro moléculas H–O–H. Caja Z: tres moléculas H–H y tres moléculas O=O. Para cada una escribe: fórmula de las moléculas, total de átomos, y si es elemento, compuesto o mezcla. Después dibuja con líneas una molécula de CH4.",
        "X: H2, 10 átomos, elemento. Y: H2O, 12 átomos, compuesto. Z: H2 y O2, 12 átomos, mezcla. CH4: un C en el centro con cuatro líneas, cada una hacia un H.",
        ["tres cajas con fórmula", "total de átomos correcto", "clasificación correcta", "dibujo de CH4"],
        ["tabla de tres filas", "dibujo"],
        ["contar moléculas en vez de átomos", "decir que Z es compuesto"],
        "Pregunta cuántos átomos tendría la caja Z si se agregaran dos moléculas H–H.",
    ),
    reinforce="Dibuja con líneas las moléculas H2 y O2 y escribe su fórmula.",
    extend="Con una persona de tu casa, armen una molécula de agua con tres bolitas de plasticina de dos colores y expliquen qué limitaciones tiene su modelo.",
)

# ================================================================ OA 13, clase 3
register(
    OA13, 3,
    materials="Papel y lápiz. La lista de metales y no metales está escrita en la explicación.",
    use="Aprenderé el modelo de los enlaces covalente, iónico y metálico para explicar cómo los átomos forman sustancias. Sirve para predecir qué tipo de enlace une a dos átomos.",
    prior=["Sé qué es un ion y cómo se calcula su carga.", "Sé cuántos electrones caben en cada nivel."],
    explain=[
        "Los átomos se unen porque así quedan más estables, normalmente con su último nivel de energía lleno. Hay tres tipos de enlace. En el enlace covalente, dos átomos de no metales comparten electrones, como en H2, O2, H2O y CO2. En el enlace iónico, un átomo de metal cede electrones a uno de no metal: el metal queda como ion positivo y el no metal como ion negativo, y se unen porque las cargas opuestas se atraen, como Na+ y Cl− en la sal. En el enlace metálico, los átomos de metales comparten electrones que se mueven libremente, y por eso los metales conducen la electricidad.",
        "Metales de esta clase: Na, K, Mg, Ca, Fe, Cu y Al. No metales: H, C, N, O, S y Cl. Para predecir: metal con no metal da enlace iónico; no metal con no metal, covalente; metal con metal, metálico. Ejemplo: el sodio (2, 8, 1) cede su electrón externo y queda con 11 protones y 10 electrones: carga +1. El cloro recibe un electrón y queda con carga −1.",
        "Los compuestos iónicos como la sal no forman moléculas aisladas: forman cristales con muchos iones alternados. Los modelos de enlaces son representaciones, y no reemplazan las propiedades que se miden.",
    ],
    vocab=[("enlace covalente", "unión en que dos no metales comparten electrones"), ("enlace iónico", "unión por atracción entre un ion positivo y uno negativo"), ("enlace metálico", "unión de metales con electrones libres compartidos"), ("catión", "ion con carga positiva"), ("anión", "ion con carga negativa")],
    worked=[
        {"title": "Predecir el tipo de enlace", "problem": "¿Qué enlace une al magnesio (Mg) con el oxígeno (O)?", "steps": ["Mg es un metal y O es un no metal.", "Metal con no metal forma enlace iónico."], "answer": "Enlace iónico"},
        {"title": "Carga de un ion", "problem": "Un átomo de cloro (17 protones) recibe un electrón y pasa de 17 a 18 electrones. ¿Qué carga tiene?", "steps": ["Carga es protones menos electrones.", "17 − 18 = −1."], "answer": "Carga −1"},
    ],
    mistakes=[
        {"wrong": "Decir que en la sal existen moléculas de NaCl iguales a las del agua.", "why": "Se aplica el modelo covalente a un compuesto iónico.", "fix": "La sal es un cristal de iones Na+ y Cl− alternados."},
        {"wrong": "Pensar que en un enlace iónico se comparten los electrones.", "why": "Se confunde con el enlace covalente.", "fix": "En el enlace iónico un átomo cede electrones y otro los recibe."},
    ],
    tiers={
        "recovery": [
            ex("En un enlace covalente, ¿qué hacen los átomos con sus electrones?", "Los comparten", "Los comparten átomos de no metales."),
            ex("En un enlace iónico, ¿qué ocurre con los electrones?", "Un átomo los cede y otro los recibe", "Se forman iones de carga opuesta."),
            ex("El sodio (metal) se une con el cloro (no metal). ¿Qué tipo de enlace forma?", "Iónico", "Metal con no metal da enlace iónico."),
        ],
        "understand": [
            ex("El sodio queda con 11 protones y 10 electrones al ceder uno. ¿Qué carga tiene?", "+1", "Hay un protón más que electrones.", calc="11-10"),
            ex("¿Qué mantiene unidos a Na+ y Cl− en la sal?", "La atracción entre cargas opuestas", "Un ion positivo y uno negativo se atraen."),
            ex("¿Por qué los metales conducen la electricidad? A) Porque tienen electrones libres que se mueven; B) Porque no tienen electrones", "A)", "Los electrones libres transportan la carga."),
        ],
        "apply": [
            ex("¿Qué enlace une al carbono (C) con el oxígeno (O) en el CO2? A) Iónico; B) Covalente", "B)", "Son dos no metales, que comparten electrones."),
            ex("¿Qué enlace une al calcio (Ca) con el cloro (Cl)? A) Iónico; B) Covalente; C) Metálico", "A)", "Un metal y un no metal forman enlace iónico."),
            ex("Un alambre está hecho solo de átomos de cobre (Cu). ¿Qué enlace hay entre ellos?", "Metálico", "Solo hay átomos de un metal."),
        ],
        "reason": [
            ex("Un compañero dice que en la sal hay moléculas NaCl como las de H2O. Corrige su afirmación.", "La sal es un cristal de iones Na+ y Cl− y no forma moléculas aisladas", "El enlace iónico forma redes de iones."),
            ex("El oxígeno del aire está formado por dos átomos de O unidos. ¿Qué enlace los une?", "Covalente", "Dos no metales comparten electrones."),
        ],
        "challenge": [
            arith("El aluminio tiene 13 protones. Al ceder 3 electrones queda con 10. ¿Cuál es su carga?", "13-10", "Carga es protones menos electrones.", ""),
            arith("Un ion de oxígeno tiene 8 protones y 10 electrones. ¿Cuál es su carga?", "8-10", "Los electrones superan a los protones en dos.", ""),
        ],
    },
    context=[ex("Una olla de aluminio conduce bien la electricidad y el calor y tiene brillo. ¿Qué enlace hay entre sus átomos?", "Metálico", "Los electrones libres de los metales explican esas propiedades.")],
    selfcheck=[
        ex("¿Qué tipo de átomos forman enlace covalente?", "Los de no metales", "Dos no metales comparten electrones."),
        ex("¿Qué carga tiene un ion que cedió electrones?", "Positiva", "Quedan más protones que electrones."),
        ex("¿Qué enlace explica que un metal conduzca la electricidad?", "El metálico", "Tiene electrones que se mueven libres."),
    ],
    open_task=task(
        "Predice el tipo de enlace de cada pareja y justifica con la regla metal / no metal: (1) K con Cl; (2) H con O; (3) Fe con Fe; (4) N con N; (5) Ca con O. Después explica con un dibujo o texto qué pasa con los electrones en el KCl, indicando la carga del K y la del Cl.",
        "(1) iónico; (2) covalente; (3) metálico; (4) covalente; (5) iónico. En KCl, el K cede un electrón y queda +1, y el Cl lo recibe y queda −1; se atraen.",
        ["cinco predicciones con justificación", "uso de la regla metal / no metal", "cargas correctas de K y Cl"],
        ["tabla de cinco filas", "dibujo o texto del KCl"],
        ["llamar covalente al enlace de Ca con O", "no indicar la carga"],
        "Pregunta qué enlace habría entre Mg y Mg.",
    ),
    reinforce="Escribe una oración que diferencie enlace iónico y covalente por lo que ocurre con los electrones.",
    extend="Con una persona de tu casa, busquen tres objetos de metal y expliquen qué propiedad de ellos tiene que ver con los electrones libres.",
)

# ================================================================ OA 13, clase 4
register(
    OA13, 4,
    materials="Papel y lápiz. Las ecuaciones y las masas están escritas en el cuaderno.",
    use="Aprenderé a ver cómo se forman nuevas sustancias reordenando átomos y a contar átomos en una ecuación química. Sirve para comprobar si una ecuación está balanceada y para relacionar masas.",
    prior=["Sé contar átomos en fórmulas.", "Conozco la conservación de la masa."],
    explain=[
        "En una reacción química las sustancias iniciales (reactantes) se transforman en sustancias nuevas (productos). Los átomos no se crean ni se destruyen: se reordenan, y cambian los enlaces. Una ecuación se escribe con una flecha: reactantes → productos. Un número delante de la fórmula, llamado coeficiente, indica cuántas moléculas hay.",
        "Una ecuación está balanceada cuando hay igual número de átomos de cada elemento a ambos lados. Por ejemplo, 2 H2 + O2 → 2 H2O tiene 4 H y 2 O a cada lado. El número de moléculas puede cambiar (aquí hay 3 a la izquierda y 2 a la derecha), pero los átomos se conservan. Para balancear se cambian los coeficientes y nunca los subíndices, porque cambiar un subíndice cambia la sustancia.",
        "Como los átomos se conservan, la masa total de los reactantes es igual a la masa total de los productos en un recipiente cerrado. Esta es la conservación de la masa. Si los datos no cuadran, se revisa si algún gas escapó o si hubo un error de medición.",
    ],
    vocab=[("reactante", "sustancia que reacciona y está antes de la flecha"), ("producto", "sustancia que se forma y está después de la flecha"), ("coeficiente", "número delante de una fórmula que indica cuántas moléculas hay"), ("ecuación balanceada", "ecuación con igual cantidad de átomos de cada elemento a ambos lados"), ("subíndice", "número pequeño dentro de una fórmula que cuenta átomos")],
    worked=[
        {"title": "Comprobar una ecuación", "problem": "¿Está balanceada CH4 + 2 O2 → CO2 + 2 H2O?", "steps": ["A la izquierda: 1 C, 4 H y 4 O (2 × 2).", "A la derecha: 1 C, 4 H (2 × 2) y 4 O (2 en CO2 y 2 en el agua)."], "answer": "Sí, tiene 1 C, 4 H y 4 O a cada lado"},
        {"title": "Masa de los productos", "problem": "En un recipiente cerrado, 14 g de una sustancia reaccionan con 6 g de otra y forman un solo producto. ¿Qué masa tiene el producto?", "steps": ["La masa se conserva.", "14 + 6 = 20."], "answer": "20 g"},
    ],
    mistakes=[
        {"wrong": "Balancear cambiando el subíndice de H2O a H2O2.", "why": "Se cambia la sustancia y no la cantidad de moléculas.", "fix": "Se cambian solo los coeficientes."},
        {"wrong": "Decir que si hay menos moléculas en los productos, desaparecieron átomos.", "why": "Se cuentan moléculas y no átomos.", "fix": "Los átomos se conservan aunque cambie el número de moléculas."},
    ],
    tiers={
        "recovery": [
            ex("En 2 H2O, ¿qué indica el coeficiente 2?", "Que hay dos moléculas de agua", "El coeficiente multiplica toda la fórmula."),
            arith("¿Cuántos átomos de hidrógeno hay en 2 H2O?", "2*2", "Dos moléculas con 2 hidrógenos cada una.", " átomos"),
            ex("En una reacción química, ¿qué pasa con los átomos?", "Se reordenan y se conservan", "Cambian los enlaces, no la cantidad de átomos."),
        ],
        "understand": [
            ex("N2 + 3 H2 → 2 NH3. ¿Cuántos átomos de H hay en los reactantes?", "6", "3 moléculas de H2 aportan 3 × 2 átomos.", calc="3*2"),
            ex("En la misma ecuación, ¿cuántos átomos de H hay en los productos?", "6", "2 moléculas de NH3 aportan 2 × 3 átomos.", calc="2*3"),
            ex("¿Por qué no se cambia un subíndice para balancear? A) Porque cambia la sustancia; B) Porque no se puede escribir", "A)", "H2O y H2O2 son sustancias distintas."),
        ],
        "apply": [
            ex("N2 + O2 → NO. Para balancear, ¿qué coeficiente debe llevar NO?", "2", "Con 2 NO hay 2 N y 2 O en cada lado."),
            arith("Reaccionan 2 g de hidrógeno con oxígeno en la proporción 1 g de H por 8 g de O. ¿Cuántos gramos de oxígeno reaccionan?", "2*8", "Se multiplica por la proporción.", " g"),
            arith("En un recipiente cerrado reaccionan 28 g de nitrógeno y 6 g de hidrógeno y forman amoníaco. ¿Cuántos gramos de amoníaco se forman?", "28+6", "La masa total se conserva.", " g"),
        ],
        "reason": [
            ex("Joaquín mira 2 H2 + O2 → 2 H2O: «A la izquierda hay 3 moléculas y a la derecha 2, así que desaparecieron átomos». Corrígelo.", "Los átomos se conservan: hay 4 H y 2 O a cada lado; solo cambia el número de moléculas", "Se cuentan átomos, no moléculas."),
            ex("Un recipiente cerrado contiene 12 g de reactantes y, tras la reacción, los productos pesan 10 g. ¿Qué conviene revisar primero?", "Si escapó un gas o si hubo un error de medición", "La masa debería conservarse en un sistema cerrado."),
        ],
        "challenge": [
            arith("En CH4 + 2 O2 → CO2 + 2 H2O, ¿cuántos átomos hay en total en los productos?", "3+2*3", "CO2 tiene 3 átomos y cada H2O también.", " átomos"),
            ex("¿Está balanceada H2 + O2 → H2O? Responde sí o no.", "No", "Hay 2 átomos de oxígeno a la izquierda y solo 1 a la derecha."),
        ],
    },
    context=[ex("El gas de cocina reacciona así: C3H8 + 5 O2 → 3 CO2 + 4 H2O. ¿Cuántos átomos de oxígeno hay en los productos?", "10", "Hay 3 × 2 en el CO2 y 4 en el agua.", calc="3*2+4")],
    selfcheck=[
        ex("¿Qué se escribe antes de la flecha en una ecuación?", "Los reactantes", "Son las sustancias que reaccionan."),
        ex("¿Qué se debe cambiar para balancear una ecuación?", "Los coeficientes", "Los subíndices definen la sustancia."),
        ex("¿Qué se conserva en un recipiente cerrado durante una reacción?", "La masa total", "Los átomos solo se reordenan."),
    ],
    open_task=task(
        "Comprueba si estas dos ecuaciones están balanceadas, contando los átomos de cada lado: (a) 2 H2 + O2 → 2 H2O; (b) CH4 + O2 → CO2 + 2 H2O. Si una no lo está, corrígela cambiando solo coeficientes. Después usa la proporción 1 g de H por 8 g de O para calcular cuántos gramos de agua se forman con 3 g de hidrógeno.",
        "(a) Sí: 4 H y 2 O a cada lado. (b) No: 4 O a la derecha y 2 a la izquierda; queda CH4 + 2 O2 → CO2 + 2 H2O. Con 3 g de H se necesitan 24 g de O y se forman 27 g de agua.",
        ["conteo de átomos de cada lado", "corrección solo con coeficientes", "masa de agua = 27 g"],
        ["tabla de conteo", "ecuación corregida", "cálculo de masa"],
        ["cambiar subíndices", "olvidar sumar la masa del oxígeno"],
        "Pregunta cuántos gramos de oxígeno hacen falta si se quisieran formar 54 g de agua.",
    ),
    reinforce="Explica con tus palabras por qué un cambio químico no destruye átomos.",
    extend="Con una persona de tu casa, busca un cambio químico cotidiano que veas (oxidación de un clavo, por ejemplo) y escribe qué crees que se transforma, sin experimentar.",
)
