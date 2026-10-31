"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 14 (sustancias puras, mezclas y métodos de separación)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA14 = "CN07 OA 14"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 14, clase 1
register(
    OA14, 1,
    materials="Papel y lápiz. Para la tarea abierta: una lista de ocho materiales de la cocina, escrita en el cuaderno. No pruebes ni mezcles productos de limpieza.",
    use="Aprenderé a distinguir una sustancia pura de una mezcla usando evidencia, como la composición y la temperatura de ebullición. Sirve para clasificar la materia que nos rodea.",
    prior=["Conozco los estados de la materia.", "Sé leer una tabla de temperaturas."],
    explain=[
        "Una sustancia pura tiene una composición fija y propiedades constantes. Son sustancias puras el oxígeno, el cobre, el oro puro, el agua destilada y la sal pura (cloruro de sodio). Una mezcla está formada por dos o más sustancias que se pueden separar y su composición puede variar. Son mezclas el aire, el agua con sal, el jugo y el granito.",
        "Una prueba útil es la temperatura de ebullición. Una sustancia pura hierve a una temperatura fija: el agua pura hierve a 100 °C al nivel del mar y mantiene esa temperatura mientras hierve. Una mezcla no tiene una temperatura de ebullición fija: depende de cuánto de cada componente haya, y la temperatura cambia mientras hierve. Los datos de temperatura de esta clase son de ejemplo.",
        "No te guíes por el aspecto: que algo sea transparente no lo hace puro. El agua mineral y el agua de la llave son mezclas porque llevan sales y gases disueltos. Para decidir, pregúntate: ¿tiene una sola sustancia o varias? ¿tiene propiedades fijas o variables?",
    ],
    vocab=[("sustancia pura", "material de composición fija y propiedades constantes"), ("mezcla", "unión de dos o más sustancias que se pueden separar"), ("composición", "qué sustancias hay y en qué cantidad"), ("punto de ebullición", "temperatura a la que un líquido hierve"), ("propiedad", "característica que se puede observar o medir")],
    worked=[
        {"title": "Clasificar materiales", "problem": "Clasifica como sustancia pura (P) o mezcla (M): oxígeno, aire, cobre, jugo de naranja.", "steps": ["El oxígeno y el cobre tienen una sola sustancia.", "El aire y el jugo tienen varios componentes."], "answer": "Oxígeno P, aire M, cobre P, jugo M"},
        {"title": "Usar la temperatura de ebullición", "problem": "Se calienta una muestra y se miden estas temperaturas durante la ebullición: 100, 100, 100 °C. Otra muestra marca 101, 103, 106 °C. ¿Cuál se comporta como sustancia pura?", "steps": ["La primera mantiene una temperatura fija.", "La segunda cambia mientras hierve."], "answer": "La primera muestra"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua transparente es una sustancia pura.", "why": "Se usa el aspecto como criterio.", "fix": "El agua de la llave tiene minerales y gases disueltos: es una mezcla."},
        {"wrong": "Creer que una mezcla siempre tiene la misma composición.", "why": "Se confunde con una sustancia pura.", "fix": "En una mezcla las cantidades de cada componente pueden variar."},
    ],
    tiers={
        "recovery": [
            ex("El agua con sal disuelta, ¿es una sustancia pura o una mezcla?", "Mezcla", "Tiene al menos dos sustancias: agua y sal."),
            ex("El cobre, ¿es una sustancia pura o una mezcla?", "Sustancia pura", "Tiene una sola sustancia."),
            ex("El aire, ¿es una sustancia pura o una mezcla?", "Mezcla", "Contiene oxígeno, nitrógeno y otros gases."),
        ],
        "understand": [
            ex("¿Qué diferencia a una sustancia pura de una mezcla: la composición fija o el color?", "La composición fija", "Una sustancia pura tiene una composición fija."),
            ex("Una muestra hierve a una temperatura que sube de 101 °C a 105 °C mientras hierve. ¿Es más probable que sea sustancia pura o mezcla?", "Mezcla", "Una sustancia pura mantiene su temperatura de ebullición."),
            ex("¿Por qué el agua mineral embotellada no es una sustancia pura?", "Porque lleva sales disueltas", "Tiene más de una sustancia."),
        ],
        "apply": [
            ex("De estos ocho materiales, ¿cuántos son mezclas? Agua destilada, aire, oro puro, jugo de fruta, oxígeno, ensalada, cobre, granito.", "4", "Son mezclas el aire, el jugo, la ensalada y el granito."),
            arith("Una mezcla tiene 40 g de sal y 160 g de agua. ¿Cuál es el porcentaje de sal en la mezcla total?", "40*100//(40+160)", "Se divide la masa de sal por la masa total y se multiplica por 100.", " %"),
            arith("Otra mezcla de agua y sal tiene 10 g de sal y 190 g de agua. ¿Cuál es el porcentaje de sal?", "10*100//(10+190)", "Se divide la masa de sal por la masa total y se multiplica por 100.", " %"),
        ],
        "reason": [
            ex("Ana dice que el agua mineral es pura porque es transparente. ¿Qué dato muestra que se equivoca?", "Lleva sales disueltas, aunque no se vean", "Transparente no significa pura."),
            ex("Una mezcla de agua y sal tiene 20 % de sal y otra mezcla de agua y sal tiene 5 % de sal. ¿Qué característica de las mezclas muestran?", "Que su composición puede variar", "Una sustancia pura tendría composición fija."),
        ],
        "challenge": [
            ex("Muestra X: 100, 100, 100 °C durante la ebullición. Muestra Y: 99, 101, 104 °C. ¿Cuál es consistente con una sustancia pura?", "La muestra X", "Mantiene una temperatura constante."),
            ex("Una persona dice que el agua de mar es una sustancia pura porque se ve uniforme. ¿Tiene razón? Responde y justifica.", "No, es una mezcla porque contiene sales disueltas", "Un aspecto uniforme no basta para ser sustancia pura."),
        ],
    },
    context=[ex("Una persona llena un vaso con agua de la llave. El agua contiene minerales disueltos y gases como el oxígeno. ¿Es sustancia pura o mezcla?", "Mezcla", "Tiene varias sustancias disueltas.")],
    selfcheck=[
        ex("¿Una sustancia pura puede tener composición variable?", "No", "Su composición es fija."),
        ex("¿Qué temperatura mantiene el agua pura mientras hierve al nivel del mar?", "100 °C", "Es su punto de ebullición."),
        ex("¿Cuál de las dos tiene composición variable: sustancia pura o mezcla?", "Mezcla", "Los componentes pueden estar en distintas cantidades."),
    ],
    open_task=task(
        "Clasifica estos ocho materiales de cocina como sustancia pura o mezcla y escribe el argumento de cada uno: sal pura, azúcar pura, leche, agua de la llave, aceite de oliva, vinagre, jugo de manzana y agua destilada. Haz una tabla con tres columnas: material, clasificación y argumento (composición fija, o varios componentes). Ayúdate de la etiqueta de los envases si tienes alguno, y anota qué otra información necesitarías si no estás seguro.",
        "Sal pura: sustancia pura, un solo compuesto. Jugo de manzana: mezcla, tiene agua, azúcares y otras sustancias. Agua destilada: sustancia pura, solo agua.",
        ["ocho materiales clasificados", "argumento con composición", "duda anotada cuando falta información"],
        ["tabla de tres columnas", "frase sobre la información faltante"],
        ["clasificar por el color", "no escribir argumento"],
        "Pregunta cuál de tus clasificaciones cambiarías si la etiqueta dijera otra cosa.",
    ),
    reinforce="Escribe dos ejemplos de sustancias puras y dos de mezclas que uses en tu casa.",
    extend="Averigua con una persona de tu casa qué contiene la etiqueta de una botella de agua mineral y qué indica sobre minerales disueltos.",
)

# ================================================================ OA 14, clase 2
register(
    OA14, 2,
    materials="Papel y lápiz. Para la tarea abierta: tres vasos transparentes, agua, sal, aceite de cocina y arena o tierra. No pruebes ninguna de las mezclas.",
    use="Aprenderé a comparar mezclas homogéneas y heterogéneas y a reconocer sus fases. Sirve para elegir después cómo separarlas.",
    prior=["Sé qué es una mezcla y qué es una sustancia pura.", "Sé que algunos sólidos se disuelven en agua."],
    explain=[
        "Una mezcla homogénea tiene un aspecto uniforme: no se distinguen sus componentes a simple vista, y toda ella tiene las mismas propiedades. El agua con sal disuelta, el aire y el vinagre son homogéneas. A estas mezclas con un componente disuelto se les llama disoluciones: el soluto es lo que se disuelve (la sal) y el solvente es donde se disuelve (el agua).",
        "Una mezcla heterogénea tiene componentes que se distinguen y forman partes distintas, llamadas fases. Una fase es una porción de la mezcla con propiedades uniformes. El agua con aceite tiene 2 fases; el agua con aceite y arena tiene 3 fases. La ensalada y el granito también son heterogéneos.",
        "Para clasificar, observa y pregunta: ¿puedo ver partes distintas? Si la respuesta es sí, es heterogénea. Si no, es homogénea. Algunas mezclas parecen homogéneas a simple vista, pero con un microscopio se ven partes distintas; en esta clase clasificamos según lo que se observa a simple vista.",
    ],
    vocab=[("mezcla homogénea", "mezcla de aspecto uniforme en todas sus partes"), ("mezcla heterogénea", "mezcla con partes distintas que se distinguen"), ("fase", "porción de una mezcla con propiedades uniformes"), ("soluto", "sustancia que se disuelve"), ("solvente", "sustancia en la que se disuelve el soluto")],
    worked=[
        {"title": "Mezcla con soluto y solvente", "problem": "Se disuelve azúcar en agua hasta que no se ve. ¿Es homogénea o heterogénea y cuál es el soluto?", "steps": ["No se ven partes distintas.", "El azúcar es lo que se disuelve."], "answer": "Homogénea; el soluto es el azúcar"},
        {"title": "Contar fases", "problem": "Un vaso con agua y arena. ¿Cuántas fases hay?", "steps": ["El agua es una fase.", "La arena sin disolver es otra fase."], "answer": "2 fases"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua con sal es heterogénea porque tiene dos sustancias.", "why": "Se cuenta sustancias en vez de mirar el aspecto.", "fix": "Si la sal queda disuelta y no se ven partes, es homogénea."},
        {"wrong": "Contar un solo grano de arena como una fase aparte de la arena.", "why": "Se confunde grano con fase.", "fix": "La arena entera es una sola fase."},
    ],
    tiers={
        "recovery": [
            ex("El aire, ¿es una mezcla homogénea o heterogénea?", "Homogénea", "No se distinguen sus componentes a simple vista."),
            ex("El agua con aceite, ¿es una mezcla homogénea o heterogénea?", "Heterogénea", "Se ven dos capas distintas."),
            ex("En una disolución de sal en agua, ¿cuál es el soluto?", "La sal", "Es la sustancia que se disuelve."),
        ],
        "understand": [
            ex("¿Qué es una fase de una mezcla?", "Una porción con propiedades uniformes", "Cada parte distinta es una fase."),
            ex("En una disolución de azúcar en agua, ¿cuál es el solvente?", "El agua", "Es la sustancia donde se disuelve el soluto."),
            ex("¿Qué pregunta te ayuda a decidir si una mezcla es heterogénea: ¿puedo ver partes distintas? o ¿tiene color?", "¿Puedo ver partes distintas?", "El color no distingue una mezcla homogénea de una heterogénea."),
        ],
        "apply": [
            ex("Un vaso tiene agua con sal disuelta, aceite y arena. ¿Cuántas fases tiene?", "3 fases", "El agua con la sal disuelta es una sola fase; el aceite y la arena son las otras dos."),
            arith("Se disuelven 30 g de sal en 270 g de agua. ¿Cuántos gramos tiene la disolución?", "30+270", "La masa total es la suma de soluto y solvente.", " g"),
            ex("Clasifica en el orden dado: vinagre, ensalada, granito, aire. Escribe Ho si es homogénea y He si es heterogénea.", "Ho, He, He, Ho", "El vinagre y el aire son uniformes; la ensalada y el granito tienen partes distintas."),
        ],
        "reason": [
            ex("Marco dice que el agua con sal es heterogénea porque tiene dos sustancias. Pero no se ven partes distintas. ¿Cuál es el error?", "Cuenta las sustancias en vez de observar las fases", "Si no se ven partes distintas, la mezcla es homogénea."),
            ex("Dos vasos, A y B. A: agua con pulpa de fruta que se ve en el fondo. B: agua con azúcar disuelta. ¿Cuál es heterogéneo?", "El vaso A", "Se distingue la pulpa como una fase aparte."),
        ],
        "challenge": [
            ex("Si se agrega más sal al agua con sal hasta que quede sal sin disolver en el fondo, ¿cuántas fases habrá y qué tipo de mezcla es?", "2 fases; heterogénea", "La sal sin disolver forma una fase aparte."),
            arith("Una disolución tiene 50 g de azúcar y 450 g de agua. ¿Qué porcentaje de la masa total es azúcar?", "50*100//(50+450)", "Se divide el soluto por la masa total y se multiplica por 100.", " %"),
        ],
    },
    context=[ex("Una persona prepara limonada disolviendo azúcar en agua con jugo de limón colado, sin pulpa. ¿La limonada es homogénea o heterogénea?", "Homogénea", "Colada y sin pulpa, no se distinguen partes.")],
    selfcheck=[
        ex("¿Qué fases tiene el agua con aceite?", "Dos fases", "El agua y el aceite forman capas distintas."),
        ex("¿Qué nombre recibe una mezcla homogénea con un soluto y un solvente?", "Disolución", "Es la mezcla uniforme de un soluto en un solvente."),
        ex("¿Se distinguen las partes de una mezcla homogénea?", "No", "Toda la mezcla se ve igual."),
    ],
    open_task=task(
        "Prepara con ayuda de una persona adulta tres vasos transparentes. Vaso 1: agua con dos cucharaditas de sal, revuelta hasta que no se vea sal. Vaso 2: agua con una cucharada de aceite. Vaso 3: agua con una cucharada de arena o tierra. Observa cada uno, sin probarlos. Haz una tabla con vaso, número de fases y tipo de mezcla. Anota cuál es el soluto y el solvente en el vaso 1.",
        "Vaso 1: 1 fase, homogénea, soluto sal, solvente agua. Vaso 2: 2 fases, heterogénea. Vaso 3: 2 fases, heterogénea.",
        ["tres vasos observados", "fases contadas", "soluto y solvente identificados"],
        ["tabla completa", "frase sobre soluto y solvente"],
        ["probar las mezclas", "contar sustancias en vez de fases"],
        "Pregunta qué pasaría con el vaso 1 si agregaras mucha más sal.",
    ),
    reinforce="Escribe tres mezclas homogéneas y tres heterogéneas que veas en tu casa.",
    extend="Averigua con una persona de tu casa qué es una aleación, como el bronce, y si es homogénea o heterogénea.",
)

# ================================================================ OA 14, clase 3
register(
    OA14, 3,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a elegir la propiedad que sirve para separar cada mezcla: tamaño, insolubilidad, densidad o punto de ebullición. Sirve para decidir entre tamizado, filtración, decantación y destilación.",
    prior=["Sé distinguir mezclas homogéneas y heterogéneas.", "Conozco sustancias que hierven a distintas temperaturas."],
    explain=[
        "Para separar una mezcla se aprovecha una propiedad en la que sus componentes se diferencian. El tamizado separa sólidos por el tamaño de sus partículas: un tamiz o colador deja pasar lo pequeño y retiene lo grande. La filtración separa un sólido que no se disuelve de un líquido: el papel de filtro deja pasar el líquido y retiene el sólido. La decantación separa líquidos que no se mezclan, o un sólido que se asienta, porque tienen densidades distintas: el más denso queda abajo y se separa.",
        "La destilación separa líquidos que tienen distinto punto de ebullición, o un líquido de una sustancia disuelta. Se calienta la mezcla, el componente que hierve primero se convierte en vapor, el vapor se enfría y se condensa en otro recipiente. Por ejemplo, el alcohol (aproximadamente 78 °C) hierve antes que el agua (100 °C). La destilación necesita calor y equipos especiales, así que se hace en laboratorios o industrias, no en casa.",
        "Si solo interesa recuperar un sólido disuelto, se puede evaporar el líquido: el líquido se va como vapor y el sólido queda. Otra propiedad útil es el magnetismo: un imán separa clavos de hierro de la arena. En la industria, estos métodos se usan en la minería, la metalurgia y el tratamiento de aguas.",
    ],
    vocab=[("tamizado", "separación de sólidos por el tamaño de sus partículas"), ("filtración", "separación de un sólido insoluble de un líquido con un filtro"), ("decantación", "separación de líquidos que no se mezclan o de un sólido que se asienta"), ("destilación", "separación por diferencia de punto de ebullición"), ("densidad", "cuánta masa hay en un volumen determinado")],
    worked=[
        {"title": "Elegir con el tamaño", "problem": "Una mezcla de arena fina y piedras grandes. ¿Qué método y qué propiedad sirven para separarla?", "steps": ["Los dos son sólidos que no se disuelven.", "Difieren en tamaño: un tamiz retiene las piedras."], "answer": "Tamizado, por el tamaño"},
        {"title": "Elegir con la densidad", "problem": "Una mezcla de agua y aceite que no se mezclan. ¿Cómo se separan?", "steps": ["Forman dos capas.", "Se separa por decantación porque difieren en densidad."], "answer": "Decantación, por la densidad"},
    ],
    mistakes=[
        {"wrong": "Usar filtración para separar sal disuelta en agua.", "why": "La sal disuelta pasa por el papel junto con el agua.", "fix": "Para separar una sal disuelta se usa evaporación o destilación."},
        {"wrong": "Hacer una destilación en casa con una olla y una tapa.", "why": "Se ignora el riesgo de quemaduras y de vapor.", "fix": "La destilación se demuestra solo en un laboratorio, con un adulto especialista."},
    ],
    tiers={
        "recovery": [
            ex("Para separar arena fina de piedras grandes, ¿se usa tamizado o destilación?", "Tamizado", "Se aprovecha el tamaño de las partículas."),
            ex("Para separar un sólido que no se disuelve de un líquido, ¿se usa filtración o decantación de líquidos?", "Filtración", "El filtro retiene el sólido."),
            ex("Para separar agua de aceite, ¿se usa decantación o tamizado?", "Decantación", "Los líquidos que no se mezclan forman capas."),
        ],
        "understand": [
            ex("¿Qué propiedad aprovecha la destilación: el tamaño o el punto de ebullición?", "El punto de ebullición", "Un componente hierve antes que otro."),
            ex("¿Por qué la decantación separa agua y aceite: por la densidad o por el color?", "Por la densidad", "El líquido más denso queda abajo."),
            ex("El alcohol hierve cerca de los 78 °C y el agua a 100 °C. Al destilar una mezcla de ambos, ¿qué componente se recoge primero, en su mayor parte?", "El alcohol", "Tiene el menor punto de ebullición y pasa antes a vapor."),
        ],
        "apply": [
            arith("Una mezcla de 100 g tiene 60 g de arena y 40 g de piedras. Se tamiza y las piedras quedan retenidas. ¿Cuántos gramos pasaron por el tamiz?", "100-40", "Pasa todo lo que no es retenido por el tamiz.", " g"),
            ex("Mezcla de limaduras de hierro y arena. ¿Qué propiedad permite separarlas con un imán?", "El magnetismo", "El hierro es atraído por el imán y la arena no."),
            ex("Los líquidos P, Q y R hierven a 65 °C, 80 °C y 118 °C. Si se destila la mezcla, ¿en qué orden se van obteniendo?", "P, Q, R", "Primero se evapora el de menor punto de ebullición."),
        ],
        "reason": [
            ex("Sofía propone filtrar agua con sal para obtener la sal. ¿Por qué no funciona y qué método sirve en cambio?", "La sal disuelta pasa por el filtro; sirve evaporar el agua o destilar", "El filtro solo retiene sólidos que no se disuelven."),
            ex("Una compañera quiere separar con un tamiz de agujeros de 2 mm una mezcla de arena de granos de 1 mm y de gravilla de 5 mm. ¿Qué componente pasa y cuál queda retenido?", "Pasa la arena; queda retenida la gravilla", "Los granos de 1 mm caben en los agujeros de 2 mm y los de 5 mm no."),
        ],
        "challenge": [
            ex("Una mezcla tiene sal, arena y agua. La sal está disuelta. ¿Qué método separa la arena del resto, y qué método podría separar después la sal del agua?", "Filtración; evaporación o destilación", "Primero se retira el sólido insoluble y luego se trabaja con la disolución."),
            ex("Dos líquidos que se mezclan por completo hierven a 56 °C y a 118 °C. ¿Se pueden separar por decantación? ¿Qué método sirve?", "No; destilación", "Al ser una mezcla homogénea no forma capas, pero sus puntos de ebullición son distintos."),
        ],
    },
    context=[ex("En una planta de tratamiento de aguas, el agua pasa primero por rejas que retienen ramas y basuras grandes. ¿Qué propiedad aprovecha este paso?", "El tamaño de los trozos", "Las rejas funcionan como un tamiz grande.")],
    selfcheck=[
        ex("¿Qué método separa un sólido insoluble de un líquido?", "Filtración", "Usa un filtro que retiene el sólido."),
        ex("¿Qué propiedad aprovecha la destilación?", "El punto de ebullición", "Un componente hierve antes."),
        ex("¿Se debe hacer una destilación en casa?", "No", "Requiere calor y equipos especiales."),
    ],
    open_task=task(
        "Observa esta lista de cinco mezclas de ejemplo y escribe para cada una el método y la propiedad que usarías. M1: arena y gravilla. M2: agua y aceite. M3: agua y arena. M4: agua y alcohol. M5: clavos de hierro y arena. Indica además cuáles de esos métodos pueden hacerse en casa y cuál requiere un laboratorio.",
        "M1: tamizado, tamaño. M2: decantación, densidad. M3: filtración, insolubilidad. M4: destilación, punto de ebullición (laboratorio). M5: imán, magnetismo.",
        ["cinco mezclas con método", "propiedad indicada", "mención de qué método requiere laboratorio"],
        ["lista de cinco filas", "frase sobre la seguridad"],
        ["usar filtración para sal disuelta", "proponer destilación casera"],
        "Pregunta qué cambiaría en tu respuesta si el alcohol de M4 fuera otro líquido con el mismo punto de ebullición que el agua.",
    ),
    reinforce="Escribe una mezcla de tu casa y el método que usarías para separar sus componentes.",
    extend="Averigua con una persona de tu casa en qué lugar usan un colador, un filtro o un imán para separar algo.",
)

# ================================================================ OA 14, clase 4
register(
    OA14, 4,
    materials="Papel y lápiz. Para la tarea abierta: una mezcla de ejemplo de arena, sal y piedrecitas, escrita en el cuaderno. No calientes nada sin una persona adulta.",
    use="Aprenderé a planificar una separación en pasos y a identificar riesgos. Sirve para organizar una investigación segura y justa.",
    prior=["Conozco el tamizado, la filtración, la decantación y la destilación.", "Sé ordenar pasos y anotar datos."],
    explain=[
        "Un plan de separación se construye en cuatro pasos. Primero, identifica los componentes de la mezcla y qué propiedad los diferencia. Segundo, elige el método para cada componente. Tercero, ordena los pasos: se separa primero lo más fácil, como un sólido grande con un tamiz, y se dejan para el final los pasos que requieren calor o más tiempo. Cuarto, anota qué materiales necesitas, cómo trabajar de forma segura y qué vas a registrar.",
        "Por ejemplo, para separar piedrecitas, arena y sal fina, se tamiza para sacar las piedrecitas; se agrega agua y se revuelve para disolver la sal; se filtra para retener la arena; y se deja evaporar el agua del filtrado al sol para recuperar la sal. Se agrega agua antes de filtrar para que la sal se disuelva y pase por el filtro, mientras la arena queda retenida.",
        "La seguridad es parte del plan. Trabaja con una persona adulta, no pruebes ningún material, no uses vidrio ni fuego, y deja la destilación para el laboratorio. Registra todo con unidades, porque un plan sin registro no se puede revisar.",
    ],
    vocab=[("plan", "secuencia ordenada de pasos para lograr algo"), ("evaporación", "paso de líquido a gas en la superficie, que deja el soluto"), ("filtrado", "líquido que pasa por el filtro"), ("registro", "anotación ordenada de datos y observaciones"), ("riesgo", "posibilidad de que algo cause daño")],
    worked=[
        {"title": "Ordenar los pasos", "problem": "Ordena para separar una mezcla de piedrecitas, arena y sal: (a) filtrar, (b) tamizar, (c) agregar agua y revolver.", "steps": ["Primero se saca lo más grande: tamizar.", "Después se disuelve la sal con agua y luego se filtra."], "answer": "b, c, a"},
        {"title": "Detectar un riesgo", "problem": "Un plan dice: «Hervir el agua para evaporarla». ¿Qué riesgo hay y cómo se evita?", "steps": ["El agua hirviendo puede quemar.", "Se evita evaporándola al sol, con una persona adulta presente."], "answer": "Riesgo de quemaduras; evaporar al sol"},
    ],
    mistakes=[
        {"wrong": "Filtrar la mezcla de arena y sal sin agregar agua.", "why": "La sal sólida no se separa con el filtro.", "fix": "Primero se disuelve la sal para que pase por el filtro y la arena quede retenida."},
        {"wrong": "No anotar las masas antes y después de cada paso.", "why": "No se podrá revisar el plan.", "fix": "Registra con unidades en cada paso."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué se hace primero al planificar una separación: identificar los componentes o elegir el material?", "Identificar los componentes", "Sin conocerlos no se puede elegir el método."),
            ex("¿Para qué se agrega agua a una mezcla de arena y sal antes de filtrarla?", "Para disolver la sal", "La sal disuelta pasa por el filtro."),
            ex("¿Se puede probar con la lengua una mezcla en una investigación? Responde sí o no.", "No", "Nunca se prueban los materiales."),
        ],
        "understand": [
            ex("¿Por qué se tamiza al comienzo: porque retira lo más grande sin necesitar otros pasos o porque es el único método que recupera la sal?", "Porque retira lo más grande sin necesitar otros pasos", "Se separa primero lo que no necesita otros pasos."),
            ex("¿Qué se obtiene al evaporar el agua del filtrado de la mezcla de arena y sal?", "La sal", "Al evaporarse el agua queda la sal."),
            ex("¿Por qué el plan debe incluir un registro con unidades?", "Para poder revisar y comparar resultados", "Sin registro no se puede verificar el trabajo."),
        ],
        "apply": [
            ex("Ordena estos pasos para separar arena, sal y gravilla: (a) evaporar el agua, (b) tamizar, (c) disolver la sal con agua, (d) filtrar. Escribe las letras en orden.", "b, c, d, a", "Se saca lo grande, se disuelve la sal, se retiene la arena y al final se recupera la sal."),
            arith("Un filtrado de ejemplo tiene 200 mL de agua. Al sol se evaporan 50 mL cada hora. ¿Cuántas horas tarda en evaporarse toda?", "200//50", "Se divide el volumen por lo que se evapora cada hora.", " horas"),
            ex("Una mezcla de piedrecitas de 8 mm y arena de 1 mm pasa por un tamiz de agujeros de 3 mm. ¿Qué queda sobre el tamiz?", "Las piedrecitas", "Son más grandes que los agujeros y quedan retenidas."),
        ],
        "reason": [
            ex("Un compañero propone calentar la mezcla de sal y agua sobre la llama de una cocina para evaporarla más rápido. ¿Qué riesgo hay y qué alternativa del plan es más segura?", "Riesgo de quemaduras; evaporar al sol con un adulto", "La alternativa evita fuego y agua hirviendo."),
            ex("Un plan dice: «Filtrar, tamizar, agregar agua, evaporar». ¿Qué error de orden tiene?", "Filtra antes de disolver la sal y antes de tamizar", "Hay que tamizar y disolver la sal antes de filtrar."),
        ],
        "challenge": [
            ex("Una mezcla tiene limaduras de hierro, arena y sal. Propón un orden de tres métodos distintos para separar los tres componentes.", "Imán, agregar agua y filtrar, evaporar el agua", "El imán retira el hierro; luego se disuelve la sal y la arena queda en el filtro."),
            ex("Un plan dice: «Destilar la mezcla de agua y alcohol en la cocina». ¿Qué debe hacerse para que sea seguro?", "Dejarlo para un laboratorio con un adulto especialista", "La destilación usa calor y vapores que pueden ser peligrosos."),
        ],
    },
    context=[ex("Una persona tiene clavos de hierro mezclados con tierra seca y quiere recuperar los clavos. ¿Qué método simple y seguro propondrías?", "Pasar un imán", "El imán atrae el hierro.")],
    selfcheck=[
        ex("¿Qué cuatro cosas incluye un plan de separación?", "Componentes y propiedad que los diferencia, método, orden de pasos, y materiales con seguridad y registro", "Son los cuatro pasos para construir un plan completo."),
        ex("¿Se separa primero lo más fácil o lo más difícil?", "Lo más fácil", "Así se simplifica la mezcla."),
        ex("¿Con quién se trabaja en una investigación con calor?", "Con una persona adulta", "La seguridad es parte del plan."),
    ],
    open_task=task(
        "Usa esta mezcla de ejemplo: 20 g de arena, 10 g de sal fina y 30 g de gravilla. Escribe un plan de cuatro pasos para separarla, indicando para cada paso qué método usas y qué propiedad aprovechas. Agrega una línea de seguridad y una tabla de registro con tres filas (arena, sal, gravilla) donde anotarías la masa recuperada.",
        "Paso 1: tamizar para sacar la gravilla (tamaño). Paso 2: agregar agua para disolver la sal. Paso 3: filtrar para retener la arena (insoluble). Paso 4: evaporar el agua al sol para recuperar la sal. Seguridad: no probar nada y trabajar con un adulto.",
        ["cuatro pasos en orden", "método y propiedad en cada paso", "seguridad y registro"],
        ["plan escrito", "tabla de registro"],
        ["filtrar antes de agregar agua", "proponer calentar sin adulto"],
        "Pregunta cuánta masa esperas recuperar de cada componente si no hubiera pérdidas.",
    ),
    reinforce="Reescribe tu plan con otra mezcla: piedrecitas, arena fina y clavos de hierro.",
    extend="Averigua con una persona de tu casa cómo se separa la cáscara de la harina o el salvado en una receta, y qué método se parece a lo que aprendiste.",
)

# ================================================================ OA 14, clase 5
register(
    OA14, 5,
    materials="Papel y lápiz. Los datos de las masas son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a registrar los resultados de una separación, calcular cuánto se recuperó y explicar las pérdidas. Sirve para evaluar si un procedimiento fue eficaz.",
    prior=["Sé planificar una separación en pasos.", "Sé calcular porcentajes con números enteros."],
    explain=[
        "Al separar una mezcla se mide la masa inicial y la masa recuperada de cada componente. Con estos datos se hace un balance. La pérdida es la masa inicial menos la suma de las masas recuperadas. El porcentaje recuperado se calcula como la masa recuperada, dividida por la masa inicial y multiplicada por 100.",
        "Por ejemplo, si la mezcla inicial pesa 100 g y se recuperan 38 g de arena y 55 g de sal, en total se recuperaron 93 g y se perdieron 7 g. El porcentaje recuperado es 93 %. Un resultado válido necesita una tabla con unidades y una explicación de por qué hay pérdidas: arena que queda pegada en el filtro, sal que queda en el vaso, o agua que no se evaporó del todo y se pesa junto con la sal.",
        "Las pérdidas pequeñas son normales; una pérdida grande, o una masa recuperada mayor que la inicial, indica un error, por ejemplo, que la sal todavía tenía agua. Una conclusión debe decir qué método funcionó y qué se podría mejorar.",
    ],
    vocab=[("masa", "cantidad de materia, medida en gramos"), ("balance", "comparación entre lo que había y lo que se recuperó"), ("pérdida", "masa inicial menos masa recuperada"), ("porcentaje recuperado", "masa recuperada dividida por la inicial, por 100"), ("error", "diferencia entre el resultado y lo esperado, por una falla del procedimiento")],
    worked=[
        {"title": "Calcular pérdida", "problem": "Una mezcla de 100 g se separa y se recuperan 38 g de arena y 55 g de sal. ¿Cuántos gramos se perdieron?", "steps": ["Se suman las masas recuperadas: 38 + 55 = 93.", "Se resta de la inicial: 100 − 93 = 7."], "answer": "7 g"},
        {"title": "Calcular porcentaje", "problem": "De una mezcla de 50 g se recuperan 45 g. ¿Qué porcentaje se recuperó?", "steps": ["45 ÷ 50 = 0,9.", "0,9 × 100 = 90."], "answer": "90 %"},
    ],
    mistakes=[
        {"wrong": "Dar por válido un resultado en que se recuperan 105 g de una mezcla inicial de 100 g.", "why": "No se revisó el balance.", "fix": "No se puede recuperar más de lo que había: revisa si la sal tenía agua."},
        {"wrong": "No indicar unidades en la tabla.", "why": "Los números sin unidad no se pueden interpretar.", "fix": "Anota gramos (g) en cada masa."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué unidad se registra la masa en una separación casera?", "Gramos (g)", "Es la unidad habitual para masas pequeñas."),
            ex("La masa inicial era 80 g y se recuperaron 80 g. ¿Hubo pérdida?", "No", "Se recuperó todo."),
            ex("¿Se puede recuperar más masa que la inicial en un procedimiento correcto? Responde sí o no.", "No", "Si ocurre, hay un error."),
        ],
        "understand": [
            ex("¿Qué indica una pérdida de masa pequeña en una separación casera?", "Que es normal por el material que queda pegado", "Siempre queda algo en el filtro o en el vaso."),
            ex("Si se pesa la sal todavía húmeda, ¿el resultado será mayor o menor que el real?", "Mayor", "El agua suma masa."),
            ex("¿Qué debe incluir una conclusión: solo el resultado o también qué mejorar?", "También qué mejorar", "Reflexionar sobre el procedimiento forma parte de la conclusión."),
        ],
        "apply": [
            arith("Una mezcla de 120 g se separa y se recuperan 70 g de arena y 40 g de sal. ¿Cuántos gramos se perdieron?", "120-(70+40)", "Se resta de la masa inicial la suma de las masas recuperadas.", " g"),
            arith("De una mezcla de 200 g se recuperan 150 g en total. ¿Qué porcentaje se recuperó?", "150*100//200", "Se divide la masa recuperada por la inicial y se multiplica por 100.", " %"),
            arith("En una separación se recuperan 25 g de arena, 12 g de gravilla y 8 g de sal. ¿Cuántos gramos se recuperaron en total?", "25+12+8", "Se suman las masas de los tres componentes.", " g"),
        ],
        "reason": [
            ex("Un grupo recuperó 105 g de una mezcla inicial de 100 g. ¿Qué error probable explica el resultado?", "La sal aún tenía agua", "El agua suma masa a la sal."),
            ex("Tomás propone anotar «recuperé casi todo» sin cifras. ¿Qué le falta a su registro?", "Las masas con sus unidades", "Sin números no se puede calcular el balance."),
        ],
        "challenge": [
            ex("Un grupo recuperó 36 g de arena y 54 g de sal de una mezcla de 100 g. Otro grupo recuperó 30 g de arena y 40 g de sal de una mezcla de 100 g. ¿Qué grupo tuvo menos pérdida y de cuántos gramos fue la diferencia de pérdidas?", "El primero; 20 g", "Pérdida del primero: 10 g; del segundo: 30 g; la diferencia es 20 g."),
            ex("Menciona dos causas de pérdida en una filtración casera y una forma de reducirlas.", "Material pegado en el filtro y derrames; enjuagar el filtro y verter con cuidado", "Cualquier par de causas con su mejora."),
        ],
    },
    context=[ex("Una persona separó 50 g de una mezcla de arena y sal y recuperó 20 g de arena y 25 g de sal. ¿Cuántos gramos se perdieron?", "5 g", "20 + 25 = 45 y 50 − 45 = 5.")],
    selfcheck=[
        ex("¿Cómo se calcula la pérdida?", "Masa inicial menos masas recuperadas", "Es la resta entre lo que había y lo que se recuperó."),
        ex("¿Qué indica un resultado de más masa que la inicial?", "Un error", "No se puede recuperar más de lo que había."),
        ex("¿Cómo se calcula el porcentaje recuperado?", "Masa recuperada dividida por masa inicial, por 100", "Esa es la fórmula."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo de dos grupos que separaron 100 g de una mezcla de arena y sal. Grupo A: arena 40 g, sal 52 g. Grupo B: arena 35 g, sal 50 g. Haz una tabla con las masas recuperadas, la pérdida y el porcentaje recuperado de cada grupo. Escribe una conclusión: qué grupo tuvo menos pérdida y dos posibles causas de pérdida.",
        "Grupo A: recuperó 92 g, perdió 8 g, 92 %. Grupo B: recuperó 85 g, perdió 15 g, 85 %. El grupo A tuvo menos pérdida. Causas: arena pegada al filtro y sal que quedó en el vaso.",
        ["tabla con masas, pérdida y porcentaje", "grupo con menos pérdida identificado", "dos causas de pérdida"],
        ["tabla completa", "conclusión escrita"],
        ["olvidar las unidades", "no calcular el porcentaje"],
        "Pregunta qué cambio en el procedimiento reduciría la pérdida del grupo B.",
    ),
    reinforce="Calcula la pérdida y el porcentaje recuperado si de 40 g de una mezcla se recuperan 30 g.",
    extend="Averigua con una persona de tu casa por qué al cocinar se pesan los ingredientes antes y después, y qué se pierde.",
)

# ================================================================ OA 14, clase 6
register(
    OA14, 6,
    materials="Papel y lápiz. Las mezclas nuevas están descritas en el cuaderno.",
    use="Aprenderé a aplicar los criterios de clasificación y separación a una mezcla nueva, y a reconocer usos en la minería, la metalurgia y el tratamiento de aguas. Sirve para explicar procesos de la industria.",
    prior=["Sé clasificar mezclas y elegir métodos de separación.", "Sé registrar pérdidas."],
    explain=[
        "Para analizar una mezcla nueva aplica estos criterios: ¿es sustancia pura o mezcla?, ¿es homogénea o heterogénea?, ¿qué propiedad diferencia a sus componentes?, ¿qué método sirve?, ¿cómo se hace de forma segura? y ¿cómo se registra el resultado?",
        "En la industria se usan los mismos métodos. En la minería, la roca que contiene el mineral valioso, llamada mena, se tritura y se tamiza para separar por tamaño; Chile es un gran productor de cobre. En la metalurgia, el metal fundido se separa de la escoria por diferencia de densidad. En el tratamiento de aguas servidas, el agua pasa por rejas (tamizado), luego por estanques donde los sólidos se asientan (decantación) y por filtros (filtración). La destilación se usa, por ejemplo, para separar el petróleo en combustibles según su punto de ebullición.",
        "Siempre que enfrentes una mezcla nueva, pregunta por la propiedad que diferencia a los componentes y verifica que el método elegido no cree riesgos para las personas ni para el ambiente. Los datos de esta clase son de ejemplo.",
    ],
    vocab=[("mena", "roca que contiene un mineral valioso, como el cobre"), ("escoria", "residuo que se forma al fundir un metal"), ("aguas servidas", "aguas usadas en casas y servicios"), ("combustible", "sustancia que se usa para producir energía"), ("criterio", "regla para comparar y decidir")],
    worked=[
        {"title": "Aplicar los criterios", "problem": "Mezcla nueva: agua con trozos de hojas y tierra fina. Clasifica y elige un método.", "steps": ["Se ven partes distintas: es heterogénea.", "Los trozos grandes se retiran con un colador y la tierra fina con un filtro."], "answer": "Heterogénea; tamizado y luego filtración"},
        {"title": "Un uso industrial", "problem": "En una planta de aguas servidas, los sólidos se asientan en un estanque. ¿Qué método es y qué propiedad aprovecha?", "steps": ["Los sólidos se asientan por su mayor densidad.", "Eso es decantación."], "answer": "Decantación, por la densidad"},
    ],
    mistakes=[
        {"wrong": "Elegir un método sin decir qué propiedad aprovecha.", "why": "No se justifica con evidencia.", "fix": "Cada método debe ir acompañado de la propiedad que diferencia a los componentes."},
        {"wrong": "Pensar que los métodos solo sirven en el laboratorio.", "why": "Se ignora su uso industrial.", "fix": "La minería, la metalurgia y el tratamiento de aguas usan los mismos métodos."},
    ],
    tiers={
        "recovery": [
            ex("En una planta de aguas servidas, las rejas retienen trozos grandes. ¿Qué método es?", "Tamizado", "Retienen por tamaño."),
            ex("En una planta de aguas servidas, los sólidos se asientan en un estanque. ¿Qué método es?", "Decantación", "Se separan por densidad."),
            ex("En la minería, la roca se tritura y se tamiza. ¿Qué propiedad se aprovecha?", "El tamaño", "El tamiz separa por el tamaño de los trozos."),
        ],
        "understand": [
            ex("¿Por qué se separa el metal fundido de la escoria: por diferencia de densidad o por diferencia de color?", "Por diferencia de densidad", "Quedan en capas distintas."),
            ex("¿Para qué se usa la destilación en la industria del petróleo?", "Para separarlo en combustibles según su punto de ebullición", "Cada componente hierve a una temperatura distinta."),
            ex("¿Qué método usan los filtros de una planta de tratamiento de aguas?", "Filtración", "Retienen sólidos pequeños que no se disuelven."),
        ],
        "apply": [
            ex("Mezcla nueva: agua con aceite y tierra. ¿Cuántas fases tiene y qué tipo de mezcla es?", "3 fases; heterogénea", "Agua, aceite y tierra forman partes distintas."),
            arith("Una planta de ejemplo trata 5.000 litros de aguas servidas cada hora. ¿Cuántos litros trata en 8 horas?", "5000*8", "Se multiplica el volumen por hora por las horas.", " L"),
            ex("Mezcla nueva: arena, clavos de hierro y agua con sal disuelta. Escribe el orden de métodos: filtrar, evaporar, imán.", "Imán, filtrar, evaporar", "Se retira el hierro, luego la arena y al final se recupera la sal."),
        ],
        "reason": [
            ex("Un grupo propone destilar una mezcla de arena y gravilla. ¿Por qué no es el método adecuado y cuál sí lo es?", "Porque son sólidos que no hierven; basta un tamiz", "La destilación separa por punto de ebullición, no por tamaño."),
            ex("Una persona afirma que el tratamiento de aguas servidas es solo filtrar. ¿Qué otros dos métodos de esta unidad participan?", "Tamizado y decantación", "Hay rejas y estanques de sedimentación antes de los filtros."),
        ],
        "challenge": [
            ex("Una mezcla homogénea de dos líquidos, P y Q, no se puede filtrar ni decantar. P hierve a 70 °C y Q a 110 °C. ¿Qué método sirve y cuál sale primero?", "Destilación; sale primero P", "P tiene el menor punto de ebullición."),
            ex("Una planta devuelve al río agua con una capa de aceite en la superficie. ¿Qué método de esta unidad permite retirar el aceite antes de devolver el agua?", "Decantación", "El aceite forma una capa aparte por su distinta densidad y se puede retirar."),
        ],
    },
    context=[ex("En una faena minera, un camión lleva roca triturada a una máquina con mallas de distintos tamaños. ¿Qué método se usa y qué propiedad se aprovecha?", "Tamizado; el tamaño", "Las mallas dejan pasar solo los trozos pequeños.")],
    selfcheck=[
        ex("¿Qué método se usa para separar el petróleo en combustibles?", "Destilación", "Cada componente hierve a una temperatura distinta."),
        ex("¿Qué propiedad se aprovecha en la decantación?", "La densidad", "El más denso queda abajo."),
        ex("¿Qué debe acompañar a cada método que se elige?", "La propiedad que se aprovecha", "Así se justifica con evidencia."),
    ],
    open_task=task(
        "Analiza esta mezcla nueva de ejemplo: agua turbia con hojas, arena fina y una gota de aceite. Escribe una tabla con los criterios (sustancia pura o mezcla, tipo de mezcla, número de fases, propiedades útiles) y un plan de tres métodos en orden, con la propiedad de cada uno. Añade un riesgo y cómo lo controlas, y una frase que relacione tu plan con una planta de tratamiento de aguas.",
        "Mezcla heterogénea con 4 fases. Plan: colar las hojas (tamaño), filtrar la arena (insoluble), dejar reposar y decantar el aceite (densidad). Riesgo: no beber el agua; se trabaja con un adulto. Una planta usa rejas, decantación y filtros.",
        ["criterios aplicados", "tres métodos en orden con propiedad", "riesgo y relación con la industria"],
        ["tabla de criterios", "plan de tres pasos"],
        ["proponer beber el agua", "olvidar la propiedad de cada método"],
        "Pregunta cómo cambiaría el plan si el agua tuviera sal disuelta.",
    ),
    reinforce="Elige una mezcla de tu casa y aplica los seis criterios de la explicación.",
    extend="Averigua con una persona de tu casa si en tu comuna hay una planta de tratamiento de aguas y qué hace con los sólidos que retiene.",
)
