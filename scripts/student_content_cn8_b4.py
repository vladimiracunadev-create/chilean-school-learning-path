"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 14 (tabla periódica, patrones y predicciones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA14 = "CN08 OA 14"

TABLA = "H (Z 1, grupo 1, período 1), He (2, g18, p1); Li (3, g1, p2), Be (4, g2), B (5, g13), C (6, g14), N (7, g15), O (8, g16), F (9, g17), Ne (10, g18), todos del período 2; Na (11, g1, p3), Mg (12, g2), Al (13, g13), Si (14, g14), P (15, g15), S (16, g16), Cl (17, g17), Ar (18, g18), todos del período 3; K (19, g1, p4) y Ca (20, g2, p4)"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 14, clase 1
register(
    OA14, 1,
    materials="Papel y lápiz. La tabla con los primeros 20 elementos está escrita en la explicación. Si quieres, usa un clip de metal y un palito de madera y agua tibia (nunca caliente).",
    use="Aprenderé cómo se organiza la tabla periódica y a formular preguntas investigables sobre los patrones de los elementos. Sirve para ubicar un elemento y comparar sus propiedades.",
    prior=["Conozco el número atómico y las partículas del átomo.", "Sé distinguir metales de no metales por su aspecto y uso."],
    explain=[
        "La tabla periódica ordena los elementos por su número atómico (Z) creciente. Las filas se llaman períodos y hay 7; las columnas se llaman grupos y hay 18. Los elementos de un mismo grupo tienen propiedades parecidas, y por eso la tabla sirve para predecir. Los metales están a la izquierda y al centro, los no metales a la derecha, y entre ambos hay una franja de metaloides. El grupo 18, los gases nobles, casi no forma compuestos.",
        "Los primeros 20 elementos son: " + TABLA + ". Cada elemento tiene un símbolo (H, He, Li...) y un número atómico. Un período nuevo comienza cuando se empieza a llenar un nuevo nivel de energía.",
        "Una pregunta investigable sobre propiedades debe poder medirse. «¿Cuántos °C sube en 2 minutos un clip de metal y un palito de madera dejados en agua tibia?» es investigable. «¿Cuál elemento es el mejor?» no lo es, porque «mejor» no se mide.",
    ],
    vocab=[("tabla periódica", "ordenamiento de los elementos por número atómico en períodos y grupos"), ("período", "fila de la tabla"), ("grupo", "columna de la tabla"), ("metaloide", "elemento con propiedades intermedias entre metal y no metal"), ("gas noble", "elemento del grupo 18, poco reactivo")],
    worked=[
        {"title": "Ubicar un elemento", "problem": "¿En qué período y grupo está el azufre (S)?", "steps": ["En la lista, S tiene Z = 16 y está entre los elementos del período 3.", "Su grupo es el 16."], "answer": "Período 3, grupo 16"},
        {"title": "Una pregunta investigable", "problem": "Convierte «¿Los metales conducen mejor el calor?» en una pregunta investigable.", "steps": ["Elige qué cambiar (material: clip de metal o palito de madera) y qué medir (temperatura del objeto).", "Fija lo que se mantiene igual: agua tibia, tiempo y tamaño."], "answer": "¿Cuántos °C sube en 2 minutos un clip de metal y un palito de madera del mismo largo en la misma agua tibia?"},
    ],
    mistakes=[
        {"wrong": "Pensar que los elementos de un período se parecen entre sí.", "why": "Se confunden filas con columnas.", "fix": "Se parecen los elementos de un mismo grupo (columna)."},
        {"wrong": "Ordenar los elementos por su masa en vez de por su número atómico.", "why": "Se usa un criterio que no es el de la tabla.", "fix": "El orden es por número atómico creciente."},
    ],
    tiers={
        "recovery": [
            ex("¿Por qué propiedad se ordenan los elementos en la tabla periódica?", "Por su número atómico creciente", "Cada elemento tiene un protón más que el anterior."),
            ex("¿Cómo se llaman las filas de la tabla?", "Períodos", "Cada fila es un período."),
            ex("¿Cómo se llama cada columna de la tabla?", "Grupo", "Los elementos de una columna tienen propiedades parecidas."),
        ],
        "understand": [
            ex("Escribe el período y el grupo del nitrógeno (N, Z = 7).", "Período 2, grupo 15", "Está entre Li y Ne, que son del período 2."),
            ex("¿Qué tienen en común los elementos de un mismo grupo?", "Propiedades parecidas", "Por eso la tabla sirve para predecir."),
            ex("¿Qué elemento sigue al magnesio (Z = 12) en la tabla?", "El aluminio (Al)", "El siguiente número atómico es 13."),
        ],
        "apply": [
            ex("¿Cuál es el número atómico del fósforo (P) según la lista?", "15", "Está después del silicio (14)."),
            ex("¿Cuál de estos elementos está en el mismo grupo que el oxígeno? A) N; B) S; C) Cl", "B)", "O y S están en el grupo 16."),
            arith("¿Cuántos elementos hay en el período 2, desde el litio (Z = 3) hasta el neón (Z = 10), ambos incluidos?", "10-3+1", "Se cuentan los números atómicos del 3 al 10.", " elementos"),
        ],
        "reason": [
            ex("Un estudiante dice que el neón (Z = 10) y el sodio (Z = 11) se parecen porque están seguidos. ¿Es correcto?", "No; el neón es del grupo 18 y el sodio del grupo 1, y el orden es por número atómico, no por parecido", "El parecido depende del grupo, no de estar uno a continuación del otro."),
            ex("El potasio (K) está en el grupo 1, igual que el sodio. ¿Se parece más al sodio o al calcio (grupo 2)?", "Al sodio", "Los elementos de un mismo grupo tienen propiedades parecidas."),
        ],
        "challenge": [
            ex("Quieres saber si un clip de metal conduce mejor el calor que un palito de madera. Elige el plan correcto. A) Cambiar el material, medir la temperatura y mantener igual el largo, el tiempo y el agua; B) Cambiar la temperatura del agua y medir el material; C) Cambiar el largo y no medir nada", "A)", "Se cambia una variable y se mide el efecto, manteniendo lo demás igual."),
            arith("¿Cuántos elementos hay en total en los períodos 1, 2 y 3 de la tabla completa (2, 8 y 8 elementos)?", "2+8+8", "Se suman los elementos de cada período.", " elementos"),
        ],
    },
    context=[ex("Una etiqueta de agua mineral menciona calcio (Ca) y magnesio (Mg). ¿Están en el mismo grupo?", "Sí, en el grupo 2", "Ambos aparecen en el grupo 2 de la tabla.")],
    selfcheck=[
        ex("¿Cuántos grupos tiene la tabla periódica?", "18", "Son las 18 columnas."),
        ex("¿Dónde están los metales: a la izquierda o a la derecha de la tabla?", "A la izquierda y al centro", "Los no metales están a la derecha."),
        ex("¿Qué grupo forman los gases nobles?", "El grupo 18", "Es la última columna."),
    ],
    open_task=task(
        "Usando los primeros 20 elementos de la explicación, completa una tabla de seis elementos: Li, C, O, Mg, Cl y Ca, con su Z, período y grupo. Después escribe una pregunta investigable sobre qué material conduce más calor, entre un clip de metal y un palito de madera, indicando qué cambias, qué mides y qué mantienes igual.",
        "Li: 3, p2, g1. C: 6, p2, g14. O: 8, p2, g16. Mg: 12, p3, g2. Cl: 17, p3, g17. Ca: 20, p4, g2. Pregunta: ¿Cuántos °C sube en 2 minutos un clip y un palito del mismo largo en la misma agua tibia?",
        ["seis filas correctas", "pregunta con variable que cambia, que se mide y controladas"],
        ["tabla", "pregunta escrita"],
        ["confundir período con grupo", "pregunta sin algo que medir"],
        "Pregunta qué cambiarías si no tuvieras termómetro.",
    ),
    reinforce="Escribe tres elementos que sean del mismo grupo y explica cómo lo sabes.",
    extend="Con una persona de tu casa, busca un objeto de metal y uno de otro material y anota cuál se siente más frío al tocarlo y por qué podría ser.",
)

# ================================================================ OA 14, clase 2
register(
    OA14, 2,
    materials="Papel y lápiz. Los datos de las sustancias están escritos en el cuaderno.",
    use="Aprenderé a clasificar elementos como metales, no metales o metaloides usando su conductividad eléctrica, su conductividad térmica y su brillo. Sirve para predecir cómo se comportará un elemento.",
    prior=["Sé ubicar un elemento en la tabla.", "Sé qué es conducir el calor."],
    explain=[
        "Los metales conducen bien la electricidad y el calor, tienen brillo metálico y son maleables, es decir, se pueden aplanar sin romperse. Ejemplos: cobre (Cu), aluminio (Al) y hierro (Fe). Los no metales conducen mal la electricidad y el calor, no tienen brillo metálico y, si son sólidos, son frágiles, es decir, se quiebran al golpearlos. Ejemplo: el azufre (S).",
        "Los metaloides tienen propiedades intermedias: brillan como un metal, pero son frágiles y conducen la electricidad solo un poco. Ejemplo: el silicio (Si). Por eso se usan en aparatos electrónicos.",
        "Para clasificar con evidencia, mira varias propiedades y no solo una: el brillo por sí solo no basta, porque los metaloides también brillan. Una tabla de datos permite comparar y decidir.",
    ],
    vocab=[("conductividad eléctrica", "capacidad de dejar pasar la corriente eléctrica"), ("conductividad térmica", "capacidad de dejar pasar el calor"), ("brillo metálico", "brillo de superficie pulida como el de un metal"), ("maleable", "que se puede aplanar sin romperse"), ("frágil", "que se quiebra al golpearlo")],
    worked=[
        {"title": "Clasificar con una tabla", "problem": "La sustancia R conduce bien la electricidad y el calor, tiene brillo y se aplana al golpearla con un martillo de goma. ¿Qué tipo de elemento es?", "steps": ["Conduce bien, brilla y es maleable.", "Esas propiedades son las de un metal."], "answer": "Metal"},
        {"title": "Un caso intermedio", "problem": "La sustancia T brilla, se quiebra al golpearla y conduce poco la electricidad. ¿Qué tipo es?", "steps": ["Brilla como un metal, pero es frágil y conduce poco.", "Las propiedades son intermedias."], "answer": "Metaloide"},
    ],
    mistakes=[
        {"wrong": "Clasificar como metal todo lo que brilla.", "why": "Se usa una sola propiedad.", "fix": "Revisa también la conductividad y si es maleable o frágil."},
        {"wrong": "Pensar que los no metales conducen bien el calor.", "why": "Se generaliza desde los metales.", "fix": "Los no metales suelen ser malos conductores."},
    ],
    tiers={
        "recovery": [
            ex("Tabla de ejemplo. Sustancia X: conduce electricidad, conduce calor, brilla y se aplana. Sustancia Y: no conduce electricidad ni calor, no brilla y se quiebra. Sustancia Z: conduce poco, brilla y se quiebra. ¿Cuál es el metal?", "X", "Reúne conducción, brillo y maleabilidad."),
            ex("Tabla de ejemplo. Sustancia X: conduce electricidad, conduce calor, brilla y se aplana. Sustancia Y: no conduce electricidad ni calor, no brilla y se quiebra. Sustancia Z: conduce poco, brilla y se quiebra. ¿Cuál es el no metal?", "Y", "No conduce, no brilla y es frágil."),
            ex("Tabla de ejemplo. Sustancia X: conduce electricidad, conduce calor, brilla y se aplana. Sustancia Y: no conduce electricidad ni calor, no brilla y se quiebra. Sustancia Z: conduce poco, brilla y se quiebra. ¿Cuál es el metaloide?", "Z", "Brilla pero es frágil y conduce poco."),
        ],
        "understand": [
            ex("¿Por qué los cables eléctricos se hacen de cobre? A) Porque conduce bien la electricidad; B) Porque es frágil", "A)", "El cobre es un buen conductor eléctrico."),
            ex("Un trozo de azufre se golpea y se rompe en pedazos. ¿Qué propiedad muestra? A) Maleabilidad; B) Fragilidad", "B)", "Se quiebra, como la mayoría de los no metales sólidos."),
            ex("¿Por qué una sartén de aluminio calienta bien los alimentos?", "Porque conduce bien el calor", "Los metales son buenos conductores térmicos."),
        ],
        "apply": [
            ex("Una sustancia nueva conduce bien la electricidad, brilla y se aplana. ¿Qué tipo de elemento es?", "Metal", "Reúne las tres propiedades de los metales."),
            ex("Una sustancia sólida no conduce, no brilla y se quiebra. ¿Qué tipo de elemento es?", "No metal", "Esas propiedades son las de un no metal."),
            arith("Un clip de metal sube de 25 °C a 41 °C en 2 minutos en agua tibia, y un palito de madera sube de 25 °C a 28 °C. ¿Cuántos °C más subió el clip?", "(41-25)-(28-25)", "Se restan los aumentos de cada uno.", " °C"),
        ],
        "reason": [
            ex("Sofía dice: «si una sustancia brilla, es metal». ¿Qué ejemplo la contradice?", "El silicio, que brilla pero es frágil y conduce poco", "El brillo solo no basta para clasificar."),
            ex("Un sólido gris brilla, se quiebra al golpearlo y conduce poco la electricidad. ¿Metal, no metal o metaloide?", "Metaloide", "Mezcla propiedades de metal y de no metal."),
        ],
        "challenge": [
            ex("Un grupo midió solo una vez la temperatura del clip y del palito. ¿Qué limitación tiene su conclusión?", "Con una sola medición no se sabe si la diferencia es casual", "Repetir las mediciones da más confianza."),
            ex("Magnesio (Mg) está en el grupo 2. Usando su posición en la tabla, ¿es un metal?", "Sí, los elementos del grupo 2 son metales", "Los grupos 1 y 2 están a la izquierda y son metales."),
        ],
    },
    context=[ex("Una cocinera debe elegir entre una cuchara de madera y una de aluminio para revolver una olla caliente. ¿Cuál protege mejor su mano y por qué?", "La de madera, porque conduce mal el calor", "Un mal conductor térmico frena el paso del calor hacia la mano.")],
    selfcheck=[
        ex("¿Qué propiedad tienen los metales de poder aplanarse sin romperse?", "Maleabilidad", "Es lo contrario de ser frágil."),
        ex("¿Los no metales conducen bien la electricidad?", "No, la conducen mal", "Esto los diferencia de los metales."),
        ex("¿Qué elemento de la lista de la clase es un metaloide?", "El silicio (Si)", "Brilla, es frágil y conduce poco."),
    ],
    open_task=task(
        "Clasifica cuatro sustancias de ejemplo. P: conduce bien electricidad y calor, brilla y se aplana. Q: no conduce, no brilla, se quiebra. R: brilla, se quiebra y conduce poco la electricidad. S: conduce bien, brilla y se aplana, y está en el grupo 1. Escribe el tipo de cada una, la propiedad que decide y una predicción para la sustancia S si fuera parte de un cable. Cuida que cada decisión use al menos dos propiedades.",
        "P: metal (conduce y se aplana). Q: no metal (no conduce y se quiebra). R: metaloide (brilla pero se quiebra). S: metal; serviría para un cable porque conduce bien.",
        ["cuatro clasificaciones", "dos propiedades por decisión", "predicción para S"],
        ["tabla", "frase de predicción"],
        ["usar solo el brillo", "decir que Q conduce"],
        "Pregunta qué medirías para estar seguro de que R es metaloide.",
    ),
    reinforce="Escribe una tabla con tres columnas: metal, no metal y metaloide, y dos propiedades en cada una.",
    extend="Con una persona de tu casa, busca tres objetos de tu casa hechos de metal y anota para qué sirve su conductividad o su brillo.",
)

# ================================================================ OA 14, clase 3
register(
    OA14, 3,
    materials="Papel y lápiz. Las reglas y la lista de los primeros 20 elementos están escritas en la explicación.",
    use="Aprenderé a usar el grupo y el período de un elemento para predecir sus electrones externos y los enlaces que forma. Sirve para escribir fórmulas de compuestos sin memorizarlas.",
    prior=["Sé cuántos electrones caben en cada nivel.", "Conozco los enlaces covalente e iónico."],
    explain=[
        "La tabla es un modelo que predice con los electrones. El período es el número de niveles de energía del átomo. El grupo (1, 2, 13 a 18) dice cuántos electrones tiene en el último nivel: grupos 1 y 2, 1 y 2 electrones; grupos 13 a 18, el último dígito (13 da 3, 14 da 4, hasta 18 que da 8). Excepción: el helio tiene 2. Por ejemplo, el fósforo (Z = 15, período 3, grupo 15) tiene 3 niveles con 2, 8 y 5 electrones.",
        "Los átomos se unen para llegar a 8 electrones externos (el H busca 2). Los no metales comparten electrones y forman tantos enlaces como electrones les faltan para llegar a 8: O (6 e) forma 2 enlaces, N (5) forma 3, C (4) forma 4, Cl (7) forma 1. Así se predicen H2O, NH3, CH4 y HCl. Los metales ceden sus electrones externos a no metales, y el compuesto iónico queda neutro: Na (cede 1) con Cl (recibe 1) da NaCl; Mg (cede 2) con Cl da MgCl2.",
        "Los gases nobles (grupo 18) ya tienen el último nivel lleno, por eso casi no forman enlaces.",
        "Recuerda la lista de los primeros 20 elementos, con su número atómico, grupo y período: " + TABLA + ".",
    ],
    vocab=[("electrón externo", "electrón del último nivel de energía"), ("modelo predictivo", "modelo que permite anticipar propiedades"), ("fórmula", "escritura de los átomos de un compuesto y su cantidad"), ("ion", "átomo con carga por ganar o perder electrones")],
    worked=[
        {"title": "Fórmula del fluoruro de litio", "problem": "Predice la fórmula del compuesto de litio (Li) con flúor (F).", "steps": ["Li es del grupo 1: cede 1 electrón. F es del grupo 17: recibe 1.", "Un Li y un F se compensan."], "answer": "LiF"},
        {"title": "Azufre con hidrógeno", "problem": "Predice la fórmula del compuesto de azufre (S) con hidrógeno (H).", "steps": ["S es del grupo 16: tiene 6 electrones externos y forma 8 − 6 = 2 enlaces.", "Cada H forma 1 enlace, así que se necesitan 2 H."], "answer": "H2S"},
    ],
    mistakes=[
        {"wrong": "Decir que el período indica los electrones externos.", "why": "Se confunde período con grupo.", "fix": "El período da el número de niveles; el grupo da los electrones externos."},
        {"wrong": "Escribir NaCl2 para el compuesto de sodio y cloro.", "why": "No se compensa lo que cede uno y recibe el otro.", "fix": "Na cede 1 y Cl recibe 1: la fórmula es NaCl."},
    ],
    tiers={
        "recovery": [
            ex("El sodio (Na) está en el grupo 1. ¿Cuántos electrones tiene en su último nivel?", "1", "El grupo 1 tiene un electrón externo."),
            ex("El cloro (Cl) está en el grupo 17. ¿Cuántos electrones tiene en su último nivel?", "7", "El último dígito del grupo da los electrones externos."),
            ex("El sodio está en el período 3. ¿Cuántos niveles de energía tiene?", "3", "El período es el número de niveles."),
        ],
        "understand": [
            arith("El oxígeno (grupo 16) tiene 6 electrones externos. ¿Cuántos electrones le faltan para completar 8?", "8-6", "Le faltan los que permiten formar enlaces covalentes.", " electrones"),
            ex("El carbono está en el grupo 14. ¿Cuántos enlaces covalentes forma?", "4", "8 menos 4 electrones externos."),
            ex("¿Por qué el neón (grupo 18) casi no forma enlaces?", "Porque su último nivel ya está lleno", "No necesita ganar ni ceder electrones."),
        ],
        "apply": [
            ex("Predice la fórmula del compuesto de nitrógeno (N) con hidrógeno (H).", "NH3", "N forma 3 enlaces y cada H forma 1."),
            ex("Predice la fórmula del compuesto de magnesio (Mg, grupo 2) con cloro (Cl, grupo 17).", "MgCl2", "Mg cede 2 electrones y cada Cl recibe 1."),
            arith("El aluminio (Z = 13) tiene 2 electrones en el primer nivel y 8 en el segundo. ¿Cuántos tiene en el tercero?", "13-2-8", "El resto de los electrones va al último nivel.", " electrones"),
        ],
        "reason": [
            ex("Un estudiante dice que Na (Z = 11) y K (Z = 19) se parecen porque sus números atómicos son cercanos. ¿Qué los hace parecidos realmente?", "Los dos están en el grupo 1 y tienen un electrón externo", "El parecido viene del mismo número de electrones externos."),
            ex("Predice la fórmula del compuesto de potasio (K, grupo 1) con cloro (Cl).", "KCl", "Cada uno cede o recibe un electrón."),
        ],
        "challenge": [
            ex("Predice la fórmula del compuesto de aluminio (Al, grupo 13) con cloro (Cl, grupo 17).", "AlCl3", "Al cede 3 electrones y cada Cl recibe 1."),
            ex("Predice la fórmula del compuesto de calcio (Ca, grupo 2) con oxígeno (O, grupo 16).", "CaO", "Ca cede 2 y O recibe 2."),
        ],
    },
    context=[ex("Si el carbono (C) forma CH4, y el silicio (Si) está en el mismo grupo, ¿qué fórmula predices para el compuesto de silicio con hidrógeno?", "SiH4", "Mismo grupo, mismo número de electrones externos y mismos enlaces.")],
    selfcheck=[
        ex("¿Qué indica el número de período?", "El número de niveles de energía", "Cada período agrega un nivel."),
        ex("¿Cuántos enlaces forma un átomo del grupo 17?", "1", "8 menos 7 electrones externos."),
        ex("¿Qué se compensa en un compuesto iónico?", "Lo que cede el metal y lo que recibe el no metal", "El compuesto resulta neutro."),
    ],
    open_task=task(
        "Completa una tabla con estos elementos: Na, O, Mg, Cl y N. Para cada uno escribe período, grupo, electrones externos y número de niveles. Luego predice las fórmulas de: (a) Na con Cl; (b) H con O; (c) Mg con O. Explica cada fórmula con una frase sobre electrones.",
        "Na: p3, g1, 1 e, 3 niveles. O: p2, g16, 6 e, 2 niveles. Mg: p3, g2, 2 e. Cl: p3, g17, 7 e. N: p2, g15, 5 e. (a) NaCl, (b) H2O, (c) MgO.",
        ["tabla completa", "tres fórmulas correctas", "explicación con electrones"],
        ["tabla", "fórmulas con frase"],
        ["escribir MgO2", "confundir período y grupo"],
        "Pregunta cuál sería la fórmula del compuesto de Al con O.",
    ),
    reinforce="Explica con un ejemplo cómo se predice cuántos enlaces forma un no metal.",
    extend="Con una persona de tu casa, busca una etiqueta que mencione sodio o calcio y anota la cantidad.",
)

# ================================================================ OA 14, clase 4
register(
    OA14, 4,
    materials="Papel y lápiz. Los datos y la lista de los primeros 20 elementos están escritos en la explicación.",
    use="Aprenderé a relacionar el número atómico y la masa atómica con la posición en la tabla y con el carácter metálico. Sirve para predecir qué elemento de dos es más metálico.",
    prior=["Sé ubicar elementos por período y grupo.", "Sé calcular neutrones con A − Z."],
    explain=[
        "Dentro de la tabla hay tendencias. Al avanzar por un período de izquierda a derecha, los elementos pasan de metales a no metales: el carácter metálico disminuye. Al bajar por un grupo, el carácter metálico aumenta. Así, el potasio es más metálico que el litio, y el litio más metálico que el flúor.",
        "Masas atómicas redondeadas de ejemplo (símbolo, Z, A): Li 3, 7; Ne 10, 20; Na 11, 23; Si 14, 28; P 15, 31; S 16, 32; K 19, 39; Ca 20, 40. La masa atómica tiende a aumentar con el número atómico, porque cada elemento tiene más protones y neutrones. Pero la masa atómica no ordena la tabla: la ordena Z.",
        "Para investigar una relación entre variables, se compara cómo cambia una al cambiar la otra. Aquí, por ejemplo, cómo cambia la masa atómica al aumentar Z. Una relación en una tabla de ejemplo no prueba que sea cierta para todos los elementos: solo es un patrón observado.",
        "Para ubicar un elemento, recuerda la lista de los primeros 20 elementos, con su número atómico, grupo y período: " + TABLA + ".",
    ],
    vocab=[("carácter metálico", "grado en que un elemento se comporta como metal"), ("tendencia", "cambio regular de una propiedad en la tabla"), ("masa atómica", "valor aproximado de protones más neutrones"), ("variable", "cantidad que puede cambiar")],
    worked=[
        {"title": "Neutrones del fósforo", "problem": "El fósforo tiene Z = 15 y A = 31. ¿Cuántos neutrones tiene?", "steps": ["Neutrones = A − Z.", "31 − 15 = 16."], "answer": "16 neutrones"},
        {"title": "Comparar carácter metálico", "problem": "¿Qué elemento es más metálico: el sodio (g1, p3) o el azufre (g16, p3)?", "steps": ["Están en el mismo período; al avanzar a la derecha el carácter metálico disminuye.", "El sodio está más a la izquierda."], "answer": "El sodio"},
    ],
    mistakes=[
        {"wrong": "Decir que el elemento con mayor masa atómica es el más metálico.", "why": "Se confunde masa con carácter metálico.", "fix": "El carácter metálico depende de la posición en el grupo y en el período."},
        {"wrong": "Afirmar que la tabla se ordena por masa atómica.", "why": "Se usa la variable equivocada.", "fix": "Se ordena por número atómico."},
    ],
    tiers={
        "recovery": [
            ex("Al avanzar de izquierda a derecha por un período, ¿el carácter metálico aumenta o disminuye?", "Disminuye", "Se pasa de metales a no metales."),
            ex("Al bajar por un grupo, ¿el carácter metálico aumenta o disminuye?", "Aumenta", "Los elementos de abajo son más metálicos."),
            ex("¿Cuál es más metálico: el litio (Li) o el flúor (F)?", "El litio", "Está a la izquierda del período 2."),
        ],
        "understand": [
            arith("El azufre tiene Z = 16 y A = 32. ¿Cuántos neutrones tiene?", "32-16", "Neutrones es A menos Z.", " neutrones"),
            arith("El potasio tiene Z = 19 y A = 39. ¿Cuántos neutrones tiene?", "39-19", "Se resta Z a A.", " neutrones"),
            arith("¿Cuántos elementos hay entre el sodio (Z = 11) y el cloro (Z = 17), sin contarlos?", "17-11-1", "Se cuentan los números atómicos intermedios.", " elementos"),
        ],
        "apply": [
            arith("¿Cuánto aumenta la masa atómica al pasar del litio (A = 7) al neón (A = 20)?", "20-7", "Se resta la masa menor a la mayor.", ""),
            arith("¿Cuánto aumenta el número atómico al pasar del litio (Z = 3) al flúor (Z = 9)?", "9-3", "Se resta el Z menor al mayor.", ""),
            ex("¿Cuál es más metálico? A) Mg (g2, p3); B) Cl (g17, p3)", "A)", "Está más a la izquierda del mismo período."),
        ],
        "reason": [
            ex("El silicio queda entre los metales y los no metales. ¿Qué propiedades explican su posición?", "Brilla como un metal, pero es frágil y conduce poco", "Tiene propiedades intermedias."),
            ex("Joaquín dice que el azufre (A = 32) es más metálico que el sodio (A = 23) porque su masa es mayor. ¿Qué le responderías?", "Que el carácter metálico no depende de la masa; el sodio es más metálico por su posición", "La tendencia se explica por el grupo y el período."),
        ],
        "challenge": [
            ex("El sodio (período 3) y el potasio (período 4) están en el grupo 1. ¿Cuál cede con más facilidad su electrón externo?", "El potasio", "Es más metálico por estar más abajo en el grupo."),
            arith("¿Cuántos elementos hay del Z = 11 al Z = 18, ambos incluidos?", "18-11+1", "Es el período 3 de la tabla.", " elementos"),
        ],
    },
    context=[ex("Un fabricante busca un metal para cables y mira el período 3. ¿Por qué el aluminio (Al) es mejor candidato que el azufre (S)?", "Porque el aluminio es un metal que conduce bien y el azufre es un no metal que conduce mal", "La posición en la tabla anticipa la conductividad.")],
    selfcheck=[
        ex("¿Qué variable ordena los elementos en la tabla?", "El número atómico", "No es la masa atómica."),
        ex("¿Qué elemento es más metálico, el sodio o el cloro?", "El sodio", "El sodio está a la izquierda en el período 3."),
        ex("¿La masa atómica tiende a aumentar o a disminuir al aumentar Z?", "Aumentar", "Hay más partículas en el núcleo."),
    ],
    open_task=task(
        "Con los datos de la explicación (Li 3, 7; Ne 10, 20; Na 11, 23; Si 14, 28; P 15, 31; S 16, 32; K 19, 39; Ca 20, 40), calcula el número de neutrones de Li, Na, Si y Ca. Luego, para el grupo 1 (Li, Na, K) ordénalos de menos a más metálico y explica en una frase por qué. Finalmente escribe una limitación de sacar una regla con tan pocos elementos.",
        "Neutrones: Li 4, Na 12, Si 14, Ca 20. Orden: Li, Na, K, porque el carácter metálico aumenta al bajar por el grupo. Limitación: son pocos elementos y puede no valer para todos.",
        ["cuatro neutrones correctos", "orden Li, Na, K con explicación", "una limitación"],
        ["cálculos", "orden", "frase de limitación"],
        ["ordenar por masa atómica", "restar al revés"],
        "Pregunta qué dato añadirías para comprobar la regla del orden.",
    ),
    reinforce="Escribe la tendencia del carácter metálico en un período y en un grupo, con un ejemplo cada una.",
    extend="Con una persona de tu casa, busquen dos metales de uso cotidiano y comparen cuál conduce mejor el calor al tocarlos, sin usar fuego ni agua caliente.",
)

# ================================================================ OA 14, clase 5
register(
    OA14, 5,
    materials="Papel y lápiz. Las reglas de predicción están en la explicación.",
    use="Aprenderé a explicar con electrones los patrones de la tabla y a predecir propiedades de un elemento poco conocido. Sirve para argumentar con evidencia y reconocer los límites de una predicción.",
    prior=["Sé usar grupo y período para obtener electrones externos.", "Sé las tendencias del carácter metálico."],
    explain=[
        "La tabla periódica es un modelo muy poderoso porque permite predecir. Mendeleev dejó espacios vacíos para elementos que aún no se conocían y anticipó sus propiedades por los vecinos de su grupo; después se descubrieron elementos con propiedades parecidas a las que predijo. La predicción se basa en un patrón, y se comprueba con evidencia.",
        "Los patrones se explican con electrones. Los elementos del mismo grupo tienen el mismo número de electrones externos, por eso reaccionan de forma parecida. Los metales ceden sus electrones externos y forman iones positivos: grupo 1 da carga +1 y grupo 2 da +2. Los no metales del grupo 17 reciben 1 y forman iones con carga −1. Los del grupo 16 reciben 2. Un elemento del período n tiene n niveles de energía.",
        "Una predicción no es una certeza: debe decir en qué se apoya y qué dato la confirmaría o la descartaría. Una limitación frecuente es que una tendencia vale en general, pero puede tener excepciones.",
    ],
    vocab=[("predicción", "afirmación sobre algo aún no medido, basada en un patrón"), ("patrón", "regularidad que se repite"), ("ion positivo", "átomo que perdió electrones"), ("ion negativo", "átomo que ganó electrones")],
    worked=[
        {"title": "Elemento desconocido del grupo 2", "problem": "El elemento Q está en el grupo 2, período 5. ¿Qué predices de él?", "steps": ["Tiene 2 electrones externos y 5 niveles de energía.", "Es un metal que cede 2 electrones y forma un ion con carga +2."], "answer": "Metal, 2 electrones externos, 5 niveles e ion +2"},
        {"title": "Dos elementos parecidos", "problem": "¿Por qué el sodio y el potasio reaccionan de forma parecida?", "steps": ["Ambos están en el grupo 1.", "Tienen un electrón externo, que ceden con facilidad."], "answer": "Porque tienen el mismo número de electrones externos"},
    ],
    mistakes=[
        {"wrong": "Afirmar que una predicción de la tabla es una certeza.", "why": "Se olvida que es un modelo con excepciones.", "fix": "Dilo como probable y propone cómo comprobarla."},
        {"wrong": "Predecir que un elemento del grupo 17 forma un ion positivo.", "why": "Se confunden los grupos que ceden y los que reciben.", "fix": "El grupo 17 recibe 1 electrón y forma ion con carga −1."},
    ],
    tiers={
        "recovery": [
            ex("Un elemento del grupo 2, ¿cuántos electrones externos tiene?", "2", "El grupo 2 tiene dos electrones externos."),
            ex("¿Un elemento del grupo 2 es un metal o un no metal?", "Un metal", "Los grupos 1 y 2 son metales."),
            ex("¿Qué carga tiene el ion de un elemento del grupo 1?", "+1", "Cede un electrón."),
        ],
        "understand": [
            ex("¿Qué carga tiene el ion de un elemento del grupo 17?", "-1", "Recibe un electrón para completar 8."),
            ex("Un elemento está en el período 5. ¿Cuántos niveles de energía tiene?", "5", "El período es el número de niveles."),
            ex("¿Por qué los elementos del grupo 18 son poco reactivos?", "Porque su último nivel ya está lleno", "No necesitan ganar ni ceder electrones."),
        ],
        "apply": [
            ex("Un elemento M está en el grupo 1. Predice la fórmula de su compuesto con el cloro.", "MCl", "Cede 1 electrón y el cloro recibe 1."),
            ex("Un elemento M está en el grupo 2. Predice la fórmula de su compuesto con el oxígeno.", "MO", "Cede 2 y el oxígeno recibe 2."),
            ex("Con el mismo elemento M del grupo 2, predice la fórmula de su compuesto con el cloro.", "MCl2", "Cede 2 electrones y cada Cl recibe 1."),
        ],
        "reason": [
            ex("Un hueco de la tabla queda entre dos metales brillantes del mismo grupo. ¿Qué predices del elemento del hueco?", "Que será un metal brillante de propiedades parecidas", "Los elementos de un grupo tienen propiedades parecidas."),
            ex("Explica con electrones por qué el sodio y el potasio reaccionan de forma parecida.", "Los dos tienen un electrón externo", "Es la misma estructura externa."),
        ],
        "challenge": [
            ex("Un átomo tiene 3 niveles con 2, 8 y 6 electrones. ¿En qué período y grupo está, y qué tipo de elemento es?", "Período 3, grupo 16; no metal", "Tiene 3 niveles y 6 electrones externos."),
            ex("Un átomo tiene 3 niveles con 2, 8 y 2 electrones. ¿Qué carga tendrá su ion?", "+2", "Cede sus 2 electrones externos."),
        ],
    },
    context=[ex("Un laboratorio anuncia un elemento nuevo ubicado en el grupo 1 y el período 7. ¿Qué predicción razonable puede hacerse?", "Será un metal con un electrón externo que forma un ion +1", "El grupo 1 predice ese comportamiento.")],
    selfcheck=[
        ex("¿Qué dejó Mendeleev en su tabla para elementos aún no descubiertos?", "Espacios vacíos", "Anticipó sus propiedades por los vecinos del grupo."),
        ex("¿Qué debe decir una buena predicción además de lo que se espera?", "En qué se apoya y cómo comprobarla", "Una predicción no es una certeza."),
        ex("¿Cuántos electrones recibe un elemento del grupo 16 para completar 8?", "2", "Tiene 6 electrones externos."),
    ],
    open_task=task(
        "Un elemento de ejemplo, X, está en el grupo 17 y el período 3 y otro, Y, en el grupo 1 y el período 4. Para cada uno escribe: número de niveles, electrones externos, tipo de elemento (metal o no metal), carga probable de su ion y una propiedad que esperarías. Después predice la fórmula del compuesto de X con Y y escribe una limitación de tu predicción.",
        "X: 3 niveles, 7 e, no metal, ion -1, mala conductora. Y: 4 niveles, 1 e, metal, ion +1, buena conductora. Fórmula: YX. Limitación: es una tendencia y puede haber excepciones.",
        ["cinco datos por elemento", "fórmula YX", "una limitación"],
        ["tabla de dos filas", "fórmula y frase"],
        ["decir que Y es no metal", "no escribir la limitación"],
        "Pregunta qué medición confirmaría que X es un no metal.",
    ),
    reinforce="Escribe una predicción para un elemento del grupo 1 y cómo la comprobarías.",
    extend="Con una persona de tu casa, comenten otra situación en que se usa un patrón para predecir, como el clima o los horarios.",
)
