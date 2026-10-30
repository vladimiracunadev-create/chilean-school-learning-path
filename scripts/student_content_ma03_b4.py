"""Student material for 3.º básico Matemática, OA 16 (descripción de cuerpos geométricos) y OA 17 (traslación, reflexión y rotación)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA16, OA17 = "MA03 OA 16", "MA03 OA 17"

BODIES = (
    "Cuerpo A: 6 caras cuadradas iguales, 12 aristas y 8 vértices. Cuerpo B: una sola superficie curva, sin aristas ni vértices. "
    "Cuerpo C: 2 caras planas circulares y 1 superficie curva, sin vértices. Cuerpo D: 1 cara plana circular, 1 superficie curva y 1 vértice. "
    "Cuerpo E: 1 cara cuadrada, 4 caras triangulares, 8 aristas y 5 vértices. Cuerpo F: 6 caras rectangulares (no todas cuadradas), 12 aristas y 8 vértices."
)
GIRO = "Los giros se hacen en el sentido en que se mueven las manecillas del reloj: arriba, derecha, abajo, izquierda."
CUAD = "Cuadrícula con columnas A, B, C… de izquierda a derecha y filas 1, 2, 3… de arriba hacia abajo."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 16
register(
    OA16, 1,
    materials="Una pelota, una caja y una lata vacía y limpia (sin bordes que corten), una regla. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a distinguir superficies planas y curvas en los cuerpos geométricos. Sirve para describir un cuerpo sin confundirlo con otro.",
    prior=["Reconozco cubos, cajas, pelotas y latas.", "Sé contar hasta 20."],
    explain=[
        "Los cuerpos geométricos son figuras 3D: se pueden tocar y tienen volumen. Su superficie puede ser plana o curva. Una superficie plana es lisa y recta, como la tapa de una caja. Si apoyas una regla sobre ella, en cualquier dirección, queda pegada sin dejar espacio.",
        "Una superficie curva se dobla, como el costado de una lata o toda una pelota. Si cruzas una regla de un lado a otro sobre ella, deja un espacio. Una cara es una superficie plana de un cuerpo. La caja tiene 6 caras planas. La lata tiene 2 caras planas y 1 superficie curva.",
        "La esfera, como una pelota, tiene solo una superficie curva y ninguna cara plana. El cono tiene 1 cara plana (la base) y 1 superficie curva. El cilindro tiene 2 caras planas y 1 curva. Describir un cuerpo por sus superficies es más seguro que decir «se parece a…».",
    ],
    vocab=[("cuerpo geométrico", "figura 3D que ocupa espacio"), ("superficie plana", "superficie recta y lisa, como la tapa de una caja"), ("superficie curva", "superficie que se dobla, como una pelota"), ("cara", "superficie plana de un cuerpo"), ("esfera", "cuerpo con una sola superficie curva, como una pelota")],
    worked=[
        {"title": "Superficies de una lata", "problem": "Una lata de forma cilíndrica tiene tapa, fondo y costado. ¿Cuántas superficies planas y cuántas curvas tiene?", "steps": ["La tapa y el fondo son planas: 2.", "El costado se dobla alrededor: es curvo: 1.", "Entonces tiene 2 planas y 1 curva."], "answer": "2 superficies planas y 1 curva"},
        {"title": "Identificar un cuerpo", "problem": "Un cuerpo tiene 1 superficie plana y 1 superficie curva. ¿Es un cono, una esfera o un cubo?", "steps": ["La esfera no tiene superficies planas: no es.", "El cubo no tiene curvas: no es.", "El cono tiene 1 base plana y 1 superficie curva."], "answer": "Un cono"},
    ],
    mistakes=[
        {"wrong": "Decir que una lata no tiene superficie curva porque su metal es liso.", "why": "Se confunde liso con plano.", "fix": "Una superficie es plana si la regla se apoya sin dejar espacio en cualquier dirección. Al cruzar el costado de la lata, la regla deja espacio: es curvo."},
        {"wrong": "Llamar esfera a un huevo porque «se parece a una pelota».", "why": "Se clasifica solo por parecido con un objeto.", "fix": "Una esfera tiene toda su superficie curva y es igual de redonda en todos lados; describe las superficies."},
    ],
    tiers={
        "recovery": [
            ex("Una pelota de goma, ¿tiene superficie plana o curva?", "Curva", "Una pelota es redonda por todos lados."),
            ex("Una caja de zapatos, ¿tiene caras planas o curvas?", "Planas", "Las caras de una caja son lisas y rectas."),
            ex("Un dado con forma de cubo, ¿tiene caras planas o curvas?", "Planas", "Las caras de un dado son lisas y rectas."),
        ],
        "understand": [
            ex("¿Cómo puedes reconocer una superficie plana con una regla?", "La regla se apoya sin dejar espacio en ninguna dirección", "En una superficie plana la regla queda pegada, la pongas como la pongas."),
            ex("¿La esfera tiene alguna cara plana?", "No", "Toda su superficie es curva."),
            ex("¿Cuántas caras planas tiene un cono?", "1", "Solo tiene la base plana."),
        ],
        "apply": [
            ex("Un cuerpo tiene 6 superficies planas y ninguna curva. ¿Es una esfera, un cilindro o una caja (paralelepípedo)?", "Una caja (paralelepípedo)", "Solo la caja tiene 6 caras planas de esas tres."),
            ex("Un cuerpo tiene 2 superficies planas y 1 curva. ¿Es un cono, un cilindro o una esfera?", "Un cilindro", "Tiene tapa y fondo planos y un costado curvo."),
            ex("Un cuerpo tiene 0 superficies planas y 1 curva. ¿Es una esfera, un cilindro o un cubo?", "Una esfera", "Solo la esfera es toda curva."),
        ],
        "reason": [
            ex("Ana dice que una lata no tiene superficie curva porque es lisa. ¿Qué está mal en su idea?", "Liso no es plano; el costado de la lata es curvo", "Una regla cruzada sobre el costado deja espacio."),
            ex("Pedro dice que un huevo es una esfera porque se parece a una pelota. ¿Qué debe tener su superficie para ser esfera?", "Ser toda curva e igual de redonda por todos lados", "El parecido no basta; hay que mirar las superficies."),
        ],
        "challenge": [
            ex("Ordena de menos a más superficies planas: cubo, esfera, cilindro y cono.", "Esfera, cono, cilindro, cubo", "Tienen 0, 1, 2 y 6 superficies planas."),
            ex("Una pirámide de base cuadrada tiene 5 caras, todas planas. ¿Cuántas superficies curvas tiene?", "Ninguna", "Todas sus caras son planas."),
        ],
    },
    context=[ex("En una mesa hay una caja de pañuelos, una lata y una pelota de tenis. ¿Cuál tiene solo superficie curva y ninguna cara plana?", "La pelota de tenis", "Es una esfera.")],
    selfcheck=[
        ex("¿Cuántas superficies curvas tiene un cilindro?", "1", "Solo su costado es curvo."),
        ex("¿Cuántas caras planas tiene un cubo?", "6", "Todas sus caras son cuadrados planos."),
        ex("¿Cuál cuerpo tiene solo una superficie y es toda curva?", "La esfera", "No tiene caras planas."),
    ],
    open_task=task(
        "Busca en tu casa tres objetos: uno con forma de caja, uno con forma de lata y uno con forma de pelota. Para cada uno, apoya una regla en varias direcciones y escribe si sus superficies son planas o curvas y cuántas planas y cuántas curvas tiene.",
        "Caja de cereal: 6 superficies planas, 0 curvas. Lata de arvejas: 2 planas y 1 curva. Pelota: 0 planas y 1 curva.",
        ["elige tres objetos distintos", "usa la regla para decidir", "cuenta planas y curvas", "escribe los números"],
        ["lista de objetos", "conteos escritos"],
        ["confundir liso con plano", "clasificar solo por parecido"],
        "Pide que muestre dónde apoyó la regla. Reconoce la decisión basada en la regla.",
    ),
    reinforce="Con una caja, una lata y una pelota, pasa la mano por cada superficie y di cuáles se sienten planas y cuáles curvas.",
    extend="Busca un objeto con forma de cono, como un gorro de fiesta, y cuenta sus superficies planas y curvas.",
)

register(
    OA16, 2,
    materials="Una caja pequeña, vacía y limpia, y lápiz. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a contar las caras, las aristas y los vértices de algunos cuerpos. Sirve para describir un cuerpo con números exactos.",
    prior=["Sé qué es una cara plana.", "Sé contar hasta 20."],
    explain=[
        "Una cara es una superficie plana del cuerpo. Una arista es el borde recto donde se juntan dos caras. Un vértice es una esquina o una punta del cuerpo, como la esquina de una caja o la punta de un cono. En una caja es el punto donde se juntan varias aristas.",
        "El cubo tiene 6 caras cuadradas, 12 aristas y 8 vértices. El paralelepípedo, que es una caja alargada, tiene los mismos números: 6 caras, 12 aristas y 8 vértices, pero sus caras son rectángulos. La pirámide de base cuadrada tiene 5 caras (1 cuadrada y 4 triangulares), 8 aristas y 5 vértices.",
        "Para no contar dos veces, cuenta con orden. En un cubo: 4 aristas arriba, 4 abajo y 4 que unen arriba con abajo, o sea 12. Marca con un lápiz cada cosa que cuentas. La esfera no tiene aristas ni vértices. El cilindro no tiene vértices ni aristas rectas. El cono tiene 1 vértice, su punta, pero no tiene aristas rectas.",
    ],
    vocab=[("cara", "superficie plana de un cuerpo"), ("arista", "borde recto donde se juntan dos caras"), ("vértice", "esquina o punta de un cuerpo, donde se juntan aristas"), ("paralelepípedo", "caja alargada con 6 caras rectangulares"), ("pirámide", "cuerpo con una base y caras triangulares que se juntan en un punto")],
    worked=[
        {"title": "Contar aristas de un cubo", "problem": "¿Cuántas aristas tiene un cubo?", "steps": ["La cara de arriba tiene 4 aristas.", "La cara de abajo tiene 4 aristas.", "Hay otras 4 aristas que unen arriba con abajo.", "4 + 4 + 4 = 12."], "answer": "12 aristas"},
        {"title": "Pirámide de base cuadrada", "problem": "Una pirámide tiene 1 base cuadrada y 4 caras triangulares. ¿Cuántas caras tiene?", "steps": ["Cuento la base: 1.", "Cuento las caras triangulares: 4.", "1 + 4 = 5."], "answer": "5 caras"},
    ],
    mistakes=[
        {"wrong": "Contar 9 aristas en un cubo.", "why": "Se salta alguna arista o se cuentan solo las que se ven.", "fix": "Cuenta por grupos: 4 arriba, 4 abajo y 4 que unen: 12."},
        {"wrong": "Decir que un cilindro tiene 8 vértices como el cubo.", "why": "Se confunden las esquinas con los bordes redondos.", "fix": "El cilindro no tiene vértices: no hay puntas donde se junten aristas rectas."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas caras tiene un cubo?", "6", "Un cubo tiene 6 caras cuadradas."),
            ex("¿Cuántas aristas tiene un cubo?", "12", "4 arriba, 4 abajo y 4 que unen."),
            ex("¿Cuántos vértices tiene un cubo?", "8", "4 vértices arriba y 4 abajo."),
        ],
        "understand": [
            ex("¿Qué es una arista de un cuerpo?", "El borde recto donde se juntan dos caras", "Es la línea donde se encuentran dos caras."),
            ex("¿Qué es un vértice de un cuerpo?", "Una esquina o punta del cuerpo, donde se juntan aristas", "Es como la esquina de una caja."),
            ex("Un cubo y un paralelepípedo, ¿tienen la misma cantidad de caras, aristas y vértices?", "Sí; 6, 12 y 8", "Solo cambia la forma de sus caras."),
        ],
        "apply": [
            ex("Una caja tiene 2 caras (arriba y abajo) y 4 caras alrededor. ¿Cuántas caras tiene en total?", "6", "2 + 4 = 6.", calc="2+4"),
            ex("Una pirámide de base cuadrada tiene 4 vértices en la base y 1 en la punta. ¿Cuántos vértices tiene?", "5", "4 + 1 = 5.", calc="4+1"),
            arith("Una pirámide de base cuadrada tiene 4 aristas en la base y 4 que suben a la punta. ¿Cuántas aristas tiene?", "4+4", "Se suman las aristas de la base y las que suben.", " aristas"),
        ],
        "reason": [
            ex("Rosa contó 9 aristas en un cubo. Cuenta tú por grupos (arriba, abajo y las que unen) y di cuántas son en realidad.", "12", "4 + 4 + 4 = 12.", calc="4+4+4"),
            ex("Paulo dice que un cilindro tiene 8 vértices como un cubo. ¿Es correcto?", "No; el cilindro no tiene vértices", "No tiene esquinas donde se junten aristas rectas."),
        ],
        "challenge": [
            ex("Un cuerpo tiene 5 caras (1 cuadrada y 4 triangulares) y 5 vértices. ¿Qué cuerpo es?", "Una pirámide de base cuadrada", "Es el cuerpo con una base cuadrada y caras triangulares."),
            ex("Una pirámide con base triangular tiene 4 caras triangulares y 4 vértices. ¿Cuántas caras tiene más el cubo que esa pirámide?", "2", "6 − 4 = 2.", calc="6-4"),
        ],
    },
    context=[arith("Una caja de regalo cúbica se adorna con cinta pegada en todas sus aristas, una cinta por arista. ¿Cuántas cintas se usan?", "12", "Un cubo tiene 12 aristas.", " cintas")],
    selfcheck=[
        ex("¿Cuántos vértices tiene una pirámide de base cuadrada?", "5", "4 en la base y 1 en la punta."),
        ex("¿Cuántas caras tiene un paralelepípedo?", "6", "Es una caja con 6 caras rectangulares."),
        ex("¿Tiene vértices una esfera?", "No", "Es toda curva, sin esquinas."),
    ],
    open_task=task(
        "Con una caja pequeña vacía, cuenta con un lápiz cuántas caras, aristas y vértices tiene. Marca con un punto cada vértice. Escribe los tres números y compáralos con un cubo.",
        "Mi caja de pasta tiene 6 caras rectangulares, 12 aristas y 8 vértices. Igual que el cubo en la cantidad, pero sus caras son rectángulos, no cuadrados.",
        ["cuenta con orden y marca lo contado", "escribe 6, 12 y 8", "compara con el cubo"],
        ["números escritos", "marcas en el dibujo"],
        ["contar dos veces", "olvidar las aristas escondidas"],
        "Pide que cuente por grupos (arriba, abajo, uniones). Reconoce el orden al contar.",
    ),
    reinforce="Con una caja de cartón, cuenta sus 8 vértices tocándolos con el dedo, uno por uno.",
    extend="Dibuja una pirámide de base cuadrada y marca sus 5 vértices y sus 8 aristas.",
)

register(
    OA16, 3,
    materials="Papel y lápiz. Las propiedades de cada cuerpo están escritas en cada ejercicio.",
    use="Aprenderé a comparar prismas y pirámides. Sirve para decir en qué se parecen y en qué se diferencian dos cuerpos.",
    prior=["Sé contar caras, aristas y vértices del cubo y de la pirámide.", "Sé qué es una cara."],
    explain=[
        "Un prisma tiene dos bases iguales y paralelas, y sus caras laterales son rectángulos. El cubo y el paralelepípedo son prismas: tienen 2 bases (arriba y abajo) y 4 caras laterales rectangulares.",
        "Una pirámide tiene una sola base. Sus caras laterales son triángulos que se juntan en un vértice, la punta. La pirámide de base cuadrada tiene 5 caras, 8 aristas y 5 vértices. La de base triangular tiene 4 caras, 6 aristas y 4 vértices.",
        "Para comparar, mira primero las bases: dos en el prisma, una en la pirámide. Luego mira las caras laterales: rectángulos en el prisma, triángulos en la pirámide. Después compara los números de caras, aristas y vértices.",
    ],
    vocab=[("prisma", "cuerpo con dos bases iguales y caras laterales rectangulares"), ("pirámide", "cuerpo con una base y caras laterales triangulares"), ("base", "cara sobre la que se apoya el cuerpo"), ("cara lateral", "cara que no es base"), ("punta", "vértice donde se juntan las caras laterales de una pirámide")],
    worked=[
        {"title": "Comparar bases", "problem": "¿Cuántas bases tiene un prisma y cuántas una pirámide?", "steps": ["El prisma tiene una base abajo y otra igual arriba: 2.", "La pirámide tiene una base y sus caras suben a una punta: 1."], "answer": "Prisma: 2 bases; pirámide: 1 base"},
        {"title": "Comparar vértices", "problem": "El cubo tiene 8 vértices y la pirámide de base cuadrada tiene 5. ¿Cuántos vértices más tiene el cubo?", "steps": ["Resto: 8 − 5.", "8 − 5 = 3."], "answer": "3 vértices más"},
    ],
    mistakes=[
        {"wrong": "Decir que una pirámide es un prisma porque «las dos tienen caras planas».", "why": "Se ve solo un rasgo parecido.", "fix": "La pirámide tiene una base y una punta; el prisma tiene dos bases iguales."},
        {"wrong": "Decir que las caras laterales de la pirámide son rectángulos.", "why": "Se confunde con el prisma.", "fix": "En la pirámide las caras laterales son triángulos que se juntan en la punta."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas bases tiene un prisma?", "2", "Tiene una base abajo y otra igual arriba."),
            ex("¿Cuántas bases tiene una pirámide?", "1", "Sus caras laterales suben a una punta."),
            ex("Las caras laterales de una pirámide, ¿son rectángulos o triángulos?", "Triángulos", "Todas se juntan en la punta."),
        ],
        "understand": [
            ex("¿Cómo se llama el vértice donde se juntan las caras laterales de una pirámide?", "La punta", "Es el vértice más alto."),
            ex("Un cubo, ¿es un prisma?", "Sí; es un prisma de bases cuadradas", "Tiene dos bases iguales y caras laterales rectangulares."),
            ex("La pirámide de base cuadrada, ¿tiene más o menos caras que el cubo?", "Menos; 5 contra 6", "1 + 4 = 5 y el cubo tiene 6."),
        ],
        "apply": [
            ex("Un paralelepípedo tiene 2 bases rectangulares y 4 caras laterales rectangulares. ¿Cuántas caras tiene?", "6", "2 + 4 = 6.", calc="2+4"),
            ex("Una pirámide de base triangular tiene 1 base y 3 caras laterales. ¿Cuántas caras tiene?", "4", "1 + 3 = 4.", calc="1+3"),
            arith("El cubo tiene 12 aristas y la pirámide de base cuadrada tiene 8. ¿Cuántas aristas más tiene el cubo?", "12-8", "Se resta la cantidad menor de la mayor.", " aristas"),
        ],
        "reason": [
            ex("Ana dice que una pirámide es un prisma porque las dos tienen caras planas. ¿Cuál es la diferencia importante?", "La pirámide tiene 1 base y una punta; el prisma tiene 2 bases iguales", "La forma y el número de bases las distinguen."),
            ex("Tomás dice que la pirámide de base triangular tiene más caras que el cubo. La pirámide tiene 4 y el cubo 6. ¿Tiene razón?", "No; 4 es menor que 6", "Se comparan los números de caras."),
        ],
        "challenge": [
            ex("Un cuerpo tiene 2 bases cuadradas iguales y 4 caras laterales rectangulares. ¿Cuántas caras, aristas y vértices tiene?", "6 caras, 12 aristas y 8 vértices", "Es un paralelepípedo (prisma de base cuadrada).", calc="2+4"),
            ex("Un cuerpo tiene 5 vértices y 8 aristas. ¿Es un cubo o una pirámide de base cuadrada?", "Una pirámide de base cuadrada", "El cubo tiene 8 vértices y 12 aristas."),
        ],
    },
    context=[ex("El techo de una torre tiene forma de pirámide de base cuadrada. Sin contar su base, ¿cuántos triángulos tiene?", "4", "Una pirámide de base cuadrada tiene 4 caras laterales triangulares.")],
    selfcheck=[
        ex("¿Cuántos vértices tiene una pirámide de base triangular?", "4", "3 en la base y 1 en la punta.", calc="3+1"),
        ex("¿Qué cuerpo tiene una punta: el prisma o la pirámide?", "La pirámide", "Sus caras laterales se juntan en un vértice."),
        ex("¿Cuántas caras tiene una pirámide de base cuadrada?", "5", "1 base y 4 triángulos."),
    ],
    open_task=task(
        "Completa una tabla en tu cuaderno que compare un cubo y una pirámide de base cuadrada. Escribe cuántas bases, caras, aristas y vértices tiene cada cuerpo y una frase que diga la diferencia principal.",
        "Cubo: 2 bases, 6 caras, 12 aristas y 8 vértices. Pirámide de base cuadrada: 1 base, 5 caras, 8 aristas y 5 vértices. La diferencia principal: el cubo tiene dos bases y la pirámide una y una punta.",
        ["escribe los números correctos de ambos cuerpos", "compara bases y caras laterales", "da una frase de diferencia"],
        ["tabla", "frase"],
        ["confundir pirámide con prisma", "contar mal las aristas"],
        "Pide que cuente en voz alta tocando una caja. Reconoce que compare bases primero.",
    ),
    reinforce="Con una caja, di cuántas bases tiene. Luego dibuja una pirámide y compara.",
    extend="Compara el cubo y la pirámide de base triangular (4 caras, 6 aristas y 4 vértices): escribe los números de cada uno y di cuál tiene más de cada cosa.",
)

register(
    OA16, 4,
    materials="Papel y lápiz. Las propiedades de los cuerpos A a F están escritas en cada ejercicio.",
    use="Aprenderé a clasificar cuerpos usando sus propiedades y no solo su parecido con objetos. Sirve para nombrar bien un cuerpo.",
    prior=["Sé contar caras, aristas y vértices.", "Sé distinguir superficies planas y curvas."],
    explain=[
        "Clasificar es agrupar cuerpos según una propiedad. Las propiedades son datos que se pueden contar o revisar: si tiene superficie curva, cuántas caras planas, cuántas aristas y cuántos vértices, y cómo son sus caras.",
        "Con esos datos nombramos los cuerpos. Seis caras cuadradas, 12 aristas y 8 vértices: cubo. Una sola superficie curva: esfera. Dos caras circulares y una curva: cilindro. Una cara circular, una curva y un vértice: cono. Una cara cuadrada y cuatro triangulares: pirámide de base cuadrada. Seis caras rectangulares: paralelepípedo.",
        "No clasifiques solo porque algo «parece una caja» o «parece una pelota». Revisa las propiedades. Dos cuerpos pueden parecerse, pero diferir en caras o vértices.",
    ],
    vocab=[("clasificar", "agrupar según una propiedad"), ("propiedad", "dato que se puede contar o revisar"), ("cubo", "6 caras cuadradas, 12 aristas y 8 vértices"), ("cono", "una base circular, una superficie curva y un vértice"), ("paralelepípedo", "6 caras rectangulares, 12 aristas y 8 vértices")],
    worked=[
        {"title": "Nombrar por propiedades", "problem": f"{BODIES} ¿Cómo se llama el cuerpo C?", "steps": ["C tiene 2 caras planas circulares.", "También tiene 1 superficie curva y ningún vértice.", "Eso es un cilindro."], "answer": "Cilindro"},
        {"title": "Agrupar", "problem": f"{BODIES} ¿Cuáles cuerpos no tienen ningún vértice?", "steps": ["Reviso A: 8 vértices. B: 0. C: 0. D: 1. E: 5. F: 8.", "Sin vértices son B y C."], "answer": "B y C"},
    ],
    mistakes=[
        {"wrong": "Llamar cubo al cuerpo F porque «parece una caja».", "why": "Se clasifica por parecido y no por las propiedades.", "fix": "Un cubo tiene todas sus caras cuadradas; F tiene caras rectangulares que no son todas cuadradas: es un paralelepípedo."},
        {"wrong": "Decir que la pirámide y el cono son lo mismo porque ambos terminan en punta.", "why": "Se mira solo la punta.", "fix": "La pirámide tiene solo caras planas; el cono tiene una superficie curva."},
    ],
    tiers={
        "recovery": [
            ex(f"{BODIES} ¿Cuál de los cuerpos es la esfera?", "B", "Es el que tiene una sola superficie curva."),
            ex(f"{BODIES} ¿Cómo se llama el cuerpo E?", "Pirámide de base cuadrada", "Tiene 1 cara cuadrada y 4 triangulares."),
            ex(f"{BODIES} ¿Cómo se llama el cuerpo A?", "Cubo", "Tiene 6 caras cuadradas iguales, 12 aristas y 8 vértices."),
        ],
        "understand": [
            ex(f"{BODIES} ¿Cuáles cuerpos tienen exactamente 8 vértices?", "A y F", "El cubo y el paralelepípedo tienen 8 vértices."),
            ex(f"{BODIES} ¿Cuántos cuerpos tienen alguna superficie curva?", "3", "Son B, C y D."),
            ex(f"{BODIES} ¿Cuál cuerpo es parecido al cubo, pero sus caras no son todas cuadradas?", "F", "F tiene caras rectangulares."),
        ],
        "apply": [
            ex(f"{BODIES} ¿Cuál de los cuerpos es el cono?", "D", "Tiene 1 cara circular, 1 superficie curva y 1 vértice."),
            ex(f"{BODIES} ¿Cuál cuerpo tiene 5 vértices?", "E", "Es la pirámide de base cuadrada."),
            ex(f"{BODIES} Ordena de menos a más vértices los cuerpos B, D, E y A.", "B, D, E, A", "Tienen 0, 1, 5 y 8 vértices."),
        ],
        "reason": [
            ex(f"{BODIES} Camila dice que F es un cubo porque parece una caja. ¿Qué propiedad muestra que se equivoca?", "Sus caras no son todas cuadradas", "El cubo tiene 6 caras cuadradas iguales."),
            ex("Juan dice que una pirámide y un cono son lo mismo porque los dos terminan en punta. ¿Qué propiedad los distingue?", "La pirámide tiene solo caras planas; el cono tiene una superficie curva", "Una pirámide no tiene superficie curva."),
        ],
        "challenge": [
            ex(f"{BODIES} Separa los cuerpos A a F en dos grupos: solo caras planas, y con alguna superficie curva.", "Solo planas: A, E y F; con curva: B, C y D", "B, C y D tienen superficie curva."),
            arith(f"{BODIES} ¿Cuántas aristas más tiene el cuerpo A que el cuerpo E?", "12-8", "Se resta: el cubo tiene 12 aristas y la pirámide, 8.", " aristas"),
        ],
    },
    context=[ex("Un gorro de cumpleaños tiene una superficie curva, una base circular y una punta. ¿Qué cuerpo geométrico es?", "Un cono", "Tiene 1 cara plana circular, 1 superficie curva y 1 vértice.")],
    selfcheck=[
        ex(f"{BODIES} ¿Cuál cuerpo tiene 2 caras planas circulares?", "C", "Es el cilindro."),
        ex("¿Una propiedad se puede contar o revisar?", "Sí", "Por ejemplo, el número de caras o si hay superficie curva."),
        ex(f"{BODIES} ¿Cuál cuerpo tiene 12 aristas y todas sus caras son cuadradas?", "A", "Es el cubo."),
    ],
    open_task=task(
        "Elige cuatro objetos de tu casa que tengan forma de cuerpo geométrico (por ejemplo, una caja, una lata, una pelota y un dado). Para cada uno, escribe qué propiedades tiene (superficies, caras, vértices) y qué cuerpo es. Explica una vez cómo evitaste clasificar solo por parecido.",
        "Dado: 6 caras cuadradas, 8 vértices: cubo. Lata: 2 caras circulares y 1 curva: cilindro. Pelota: 1 superficie curva: esfera. Caja de cereal: 6 caras rectangulares: paralelepípedo. Revisé las propiedades antes de nombrarlos.",
        ["escribe propiedades reales", "nombra correctamente cada cuerpo", "explica que revisó propiedades"],
        ["lista de objetos", "propiedades", "nombres"],
        ["clasificar solo por parecido", "contar mal los vértices"],
        "Pide que cuente las propiedades antes de dar el nombre. Reconoce la explicación.",
    ),
    reinforce="Elige un objeto de tu casa y dime tres propiedades que tenga antes de decir qué cuerpo es.",
    extend="Inventa una adivinanza con tres propiedades de un cuerpo (sin decir su nombre) y pide a alguien que lo descubra.",
)

# ================================================================ OA 17
register(
    OA17, 1,
    materials=f"Lápiz y papel. Si quieres, una moneda o una tarjeta para moverla sobre la mesa. {CUAD}",
    use="Aprenderé qué es trasladar una figura. Sirve para reconocer cuándo algo solo se mueve de lugar, sin cambiar de forma ni de tamaño.",
    prior=["Reconozco figuras 2D como cuadrados y triángulos.", "Sé ubicar un casillero en una cuadrícula."],
    explain=[
        "Trasladar una figura es moverla en línea recta de un lugar a otro, sin girarla. La figura no cambia de tamaño, de forma ni de dirección. Solo cambia de lugar.",
        "Si trasladas la letra b hacia la derecha, sigue siendo b y mira hacia el mismo lado. Si trasladas una flecha que apunta hacia arriba, sigue apuntando hacia arriba. En una cuadrícula, trasladar es sumar o restar casilleros: si un punto está en B2 y lo mueves 3 casilleros a la derecha, queda en E2.",
        "En el entorno hay traslaciones: un cajón que se abre, una cortina que se corre o una persona parada en una escalera mecánica. Todos se mueven en línea recta sin girar.",
    ],
    vocab=[("trasladar", "mover una figura en línea recta, sin girarla"), ("traslación", "movimiento que cambia el lugar de una figura"), ("figura 2D", "figura plana, como un cuadrado"), ("dirección", "hacia dónde apunta o se mueve algo"), ("casillero", "cuadradito de una cuadrícula")],
    worked=[
        {"title": "Trasladar un punto", "problem": f"{CUAD} Un punto está en B2 y la figura se traslada 3 casilleros a la derecha. ¿Dónde queda el punto?", "steps": ["Derecha cambia la letra hacia la siguiente.", "De B a E hay 3 pasos: B→C→D→E.", "La fila no cambia: sigue en 2."], "answer": "E2"},
        {"title": "Qué no cambia", "problem": "Una flecha apunta hacia la derecha y se traslada hacia arriba. ¿Hacia dónde apunta después?", "steps": ["Trasladar no gira la figura.", "La flecha mantiene su dirección.", "Sigue apuntando hacia la derecha."], "answer": "Hacia la derecha"},
    ],
    mistakes=[
        {"wrong": "Trasladar la letra b y dibujar una d.", "why": "Se cambia la dirección de la figura.", "fix": "Al trasladar, la figura no gira: sigue siendo b."},
        {"wrong": "Creer que una figura trasladada se vuelve más grande al alejarse.", "why": "Se confunde mover con cambiar de tamaño.", "fix": "Trasladar solo cambia el lugar; el tamaño y la forma son los mismos."},
    ],
    tiers={
        "recovery": [
            ex("La letra b se traslada hacia la derecha. ¿Qué letra se ve ahora?", "b", "La traslación no gira ni da vuelta la figura."),
            ex("Un cuadrado de 3 cm de lado se traslada. ¿Cambia su tamaño?", "No", "Trasladar solo cambia el lugar."),
            ex("Una flecha apunta hacia arriba y se traslada 2 casilleros hacia abajo. ¿Hacia dónde apunta?", "Hacia arriba", "La traslación no cambia hacia dónde mira."),
        ],
        "understand": [
            ex("Al trasladar una figura, ¿qué cambia: su lugar, su tamaño o su forma?", "Su lugar", "El tamaño y la forma se mantienen."),
            ex("Al trasladar una figura, ¿se gira la figura?", "No", "Se mueve en línea recta, sin girar."),
            ex("¿Qué se mantiene igual al trasladar una figura?", "El tamaño, la forma y la dirección a la que mira", "Solo cambia el lugar."),
        ],
        "apply": [
            ex(f"{CUAD} Un punto de una figura está en C4 y se traslada 2 casilleros a la derecha. ¿Dónde queda el punto?", "E4", "De C a E hay 2 pasos."),
            ex(f"{CUAD} Un punto está en C1 y se traslada 2 casilleros hacia abajo. ¿Dónde queda?", "C3", "La fila pasa de 1 a 3."),
            ex(f"{CUAD} Un punto está en D4, se traslada 2 casilleros a la izquierda y 1 hacia arriba. ¿Dónde queda?", "B3", "D→B con 2 a la izquierda y 4→3 con 1 hacia arriba."),
        ],
        "reason": [
            ex("Lía traslada la letra p hacia la derecha y dibuja una q. ¿Está bien?", "No; la traslación no da vuelta la letra, sigue siendo p", "La q se obtiene al reflejar la p, no al trasladarla."),
            ex("Una persona parada en una escalera mecánica se mueve en línea recta sin girar. ¿Es una traslación?", "Sí", "Cambia de lugar sin girar."),
        ],
        "challenge": [
            ex(f"{CUAD} Un cuadrado tiene sus vértices en A1, B1, A2 y B2. Se traslada 2 casilleros a la derecha y 1 hacia abajo. ¿Dónde quedan sus cuatro vértices?", "C2, D2, C3 y D3", "Cada vértice avanza 2 columnas y 1 fila."),
            ex("¿Cuál de estos movimientos es una traslación: (a) un cajón que se abre, (b) una rueda que gira, (c) una puerta que se abre?", "(a) un cajón que se abre", "Se mueve en línea recta, sin girar."),
        ],
    },
    context=[ex("Un tren de juguete avanza en línea recta sobre rieles. El vagón, ¿se traslada o gira?", "Se traslada", "Cambia de lugar sin girar.")],
    selfcheck=[
        ex("Una flecha apunta a la izquierda y se traslada hacia arriba. ¿Hacia dónde apunta?", "A la izquierda", "No se gira."),
        ex(f"{CUAD} Un punto está en E4 y se traslada 2 casilleros a la izquierda. ¿Dónde queda?", "C4", "De E a C hay 2 pasos hacia la izquierda."),
        ex("¿Una cortina que se corre es una traslación?", "Sí", "Se mueve en línea recta sin girar."),
    ],
    open_task=task(
        "Dibuja en papel cuadriculado la letra b grande en una esquina. Haz una copia de ella trasladada 5 cuadritos a la derecha y otra trasladada 4 cuadritos hacia abajo. Escribe qué letra es cada copia y qué no cambió.",
        "Las dos copias son b. No cambiaron su tamaño ni la dirección a la que mira; solo cambió su lugar.",
        ["dibuja la b y dos copias", "mueve el número de cuadritos pedido", "no gira ni da vuelta la letra", "dice que cambia solo el lugar"],
        ["dibujos", "frase"],
        ["dibujar una d o una p", "cambiar el tamaño"],
        "Pide que cuente los cuadritos al trasladar. Reconoce que explique qué no cambia.",
    ),
    reinforce="Mueve una moneda sobre una hoja en línea recta, sin girarla, y observa que mira hacia el mismo lado.",
    extend="Busca tres movimientos en tu casa que sean traslaciones y tres que no lo sean.",
)

register(
    OA17, 2,
    materials=f"Lápiz y papel; si quieres, un espejo pequeño de plástico, sin bordes que corten. {CUAD}",
    use="Aprenderé qué es reflejar una figura respecto de un eje. Sirve para reconocer simetrías, como las alas de una mariposa.",
    prior=["Sé qué es trasladar una figura.", "Sé ubicar casilleros en una cuadrícula."],
    explain=[
        "Reflejar una figura es verla como en un espejo. Hay una línea llamada eje, que es donde está el espejo. La figura y su reflejo quedan a cada lado del eje, a la misma distancia de él, y tienen el mismo tamaño y la misma forma.",
        "Un reflejo cambia el sentido de la figura, como la mano izquierda y la derecha. Si reflejas la letra b con un eje vertical, obtienes d. Si la reflejas con un eje horizontal, obtienes p. Una flecha que apunta a la derecha, reflejada con un eje vertical, apunta a la izquierda. Una flecha que apunta hacia arriba, reflejada con un eje vertical, sigue apuntando hacia arriba.",
        "En una cuadrícula, si un punto está a 2 casilleros del eje, su reflejo está a 2 casilleros al otro lado del eje. Por ejemplo, con el eje entre las columnas C y D, el punto B2 se refleja en E2.",
    ],
    vocab=[("reflejar", "dar vuelta una figura como en un espejo"), ("reflexión", "movimiento que da vuelta la figura respecto de un eje"), ("eje", "línea donde está el espejo"), ("eje vertical", "línea que va de arriba hacia abajo"), ("eje horizontal", "línea que va de izquierda a derecha")],
    worked=[
        {"title": "Reflejar una letra", "problem": "Se refleja la letra b con un eje vertical a su derecha. ¿Qué letra se ve en el reflejo?", "steps": ["El eje vertical da vuelta la figura de izquierda a derecha.", "La barra de la b, que estaba a la izquierda, queda a la derecha.", "La letra resultante es d."], "answer": "d"},
        {"title": "Reflejar un punto", "problem": f"{CUAD} El eje está entre las columnas C y D. Un punto está en B2. ¿Dónde queda su reflejo?", "steps": ["B está a 2 columnas del eje (C está al lado del eje y B es la segunda).", "El reflejo queda a 2 columnas al otro lado: D es la primera y E la segunda.", "La fila no cambia."], "answer": "E2"},
    ],
    mistakes=[
        {"wrong": "Pensar que reflejar es lo mismo que trasladar.", "why": "Se olvida que el reflejo cambia el sentido de la figura.", "fix": "La traslación no cambia el sentido; el reflejo sí, como en un espejo."},
        {"wrong": "Dibujar el reflejo del mismo lado del eje que la figura.", "why": "No se usa el eje como espejo.", "fix": "El reflejo está al otro lado del eje, a la misma distancia."},
    ],
    tiers={
        "recovery": [
            ex("La letra b se refleja con un eje vertical. ¿Qué letra se ve?", "d", "La barra pasa de la izquierda a la derecha."),
            ex("La letra b se refleja con un eje horizontal. ¿Qué letra se ve?", "p", "La parte de arriba pasa abajo."),
            ex("Una figura y su reflejo, ¿tienen el mismo tamaño?", "Sí", "El espejo no cambia el tamaño."),
        ],
        "understand": [
            ex("¿Qué es el eje en una reflexión?", "La línea donde está el espejo", "La figura y su reflejo quedan a cada lado."),
            ex("¿El reflejo queda del mismo lado del eje que la figura o del otro lado?", "Del otro lado", "Como en un espejo."),
            ex("Un punto está a 3 casilleros del eje. ¿A cuántos casilleros del eje queda su reflejo?", "3", "La distancia al eje es la misma."),
        ],
        "apply": [
            ex("Una flecha apunta hacia la derecha. Se refleja con un eje vertical. ¿Hacia dónde apunta el reflejo?", "Hacia la izquierda", "El eje vertical da vuelta de izquierda a derecha."),
            ex("Una flecha apunta hacia arriba. Se refleja con un eje horizontal. ¿Hacia dónde apunta el reflejo?", "Hacia abajo", "El eje horizontal da vuelta de arriba hacia abajo."),
            ex(f"{CUAD} El eje está entre las columnas C y D. Un punto está en C2. ¿Dónde queda su reflejo?", "D2", "C es la primera columna junto al eje; su reflejo es D."),
        ],
        "reason": [
            ex("Ema dice que reflejar es igual que trasladar. ¿Cuál es la diferencia?", "El reflejo da vuelta la figura como en un espejo; la traslación no", "La traslación mantiene el sentido de la figura."),
            ex("Pedro dice que la letra A mayúscula de molde, al reflejarse con un eje vertical, se ve igual. ¿Es cierto?", "Sí; la A es igual por los dos lados", "Los dos lados de la A son iguales."),
        ],
        "challenge": [
            ex(f"{CUAD} El eje está entre las columnas C y D. Un punto está en A3. ¿Dónde queda su reflejo?", "F3", "A está a 3 columnas del eje (C, B, A) y el reflejo, a 3 del otro lado (D, E, F)."),
            ex("Una flecha apunta hacia arriba y se refleja con un eje vertical. ¿Hacia dónde apunta el reflejo?", "Hacia arriba", "El eje vertical cambia izquierda y derecha, no arriba y abajo."),
        ],
    },
    context=[ex("En un lago tranquilo se ve el reflejo de un árbol. La copa del árbol real apunta hacia arriba. ¿Hacia dónde apunta la copa en el reflejo?", "Hacia abajo", "El agua actúa como un eje horizontal.")],
    selfcheck=[
        ex("¿Qué letra se ve al reflejar la p con un eje vertical?", "q", "Se da vuelta de izquierda a derecha."),
        ex("Un reflejo, ¿cambia el tamaño de la figura?", "No", "Solo cambia el sentido."),
        ex("El reflejo y la figura, ¿están a la misma distancia del eje?", "Sí", "Así funciona un espejo."),
    ],
    open_task=task(
        "Dibuja en papel cuadriculado una línea vertical (el eje) y, a su izquierda, un triángulo pequeño con una esquina a 2 cuadritos del eje. Dibuja su reflejo al otro lado del eje. Luego haz lo mismo con la letra b y un eje horizontal. Escribe qué letra obtuviste.",
        "El reflejo del triángulo está al otro lado del eje, con una esquina a 2 cuadritos del eje. La b reflejada con un eje horizontal se ve como p.",
        ["dibuja el eje y la figura", "el reflejo está al otro lado a la misma distancia", "obtiene la letra correcta"],
        ["dibujo del triángulo y su reflejo", "letra escrita"],
        ["reflejar del mismo lado", "cambiar el tamaño"],
        "Pide que mida la distancia al eje con los cuadritos. Reconoce la letra correcta.",
    ),
    reinforce="Dibuja las letras b, d, p y q y explica cuáles son reflejos de cuáles.",
    extend="Busca en casa o en un dibujo una figura simétrica, como una mariposa, y explica dónde estaría el eje.",
)

register(
    OA17, 3,
    materials=f"Lápiz, papel y una tarjeta para girar sobre la mesa. {GIRO}",
    use="Aprenderé qué es rotar una figura alrededor de un punto. Sirve para reconocer giros, como los de una rueda o las agujas de un reloj.",
    prior=["Sé qué es trasladar y reflejar una figura.", "Sé leer la hora en punto."],
    explain=[
        "Rotar una figura es girarla alrededor de un punto fijo, que se llama centro de giro. La figura no cambia de tamaño ni de forma. Cambia hacia dónde apunta.",
        GIRO + " Un cuarto de vuelta es la cuarta parte de una vuelta completa. Una flecha que apunta hacia arriba, con un cuarto de vuelta, apunta hacia la derecha. Con media vuelta apunta hacia abajo. Con tres cuartos de vuelta apunta hacia la izquierda. Con una vuelta completa vuelve a apuntar hacia arriba.",
        "Un giro de media vuelta de la letra b la convierte en q. Las agujas de un reloj y las aspas de un ventilador rotan. En todos los casos hay un punto central que no se mueve.",
    ],
    vocab=[("rotar", "girar una figura alrededor de un punto"), ("centro de giro", "punto que no se mueve cuando se gira"), ("cuarto de vuelta", "la cuarta parte de una vuelta completa"), ("media vuelta", "dos cuartos de vuelta"), ("vuelta completa", "giro que deja la figura como al principio")],
    worked=[
        {"title": "Giro de una flecha", "problem": f"{GIRO} Una flecha apunta hacia arriba y gira un cuarto de vuelta. ¿Hacia dónde apunta?", "steps": ["El orden de los giros es arriba, derecha, abajo, izquierda.", "Un cuarto de vuelta avanza un lugar en ese orden.", "De arriba pasa a la derecha."], "answer": "Hacia la derecha"},
        {"title": "Media vuelta", "problem": f"{GIRO} Una flecha apunta hacia la derecha y gira media vuelta. ¿Hacia dónde apunta?", "steps": ["Media vuelta son dos cuartos de vuelta.", "De derecha avanza a abajo y luego a izquierda."], "answer": "Hacia la izquierda"},
    ],
    mistakes=[
        {"wrong": "Decir que una flecha hacia arriba, después de una vuelta completa, apunta a la derecha.", "why": "Se confunde la vuelta completa con un cuarto de vuelta.", "fix": "Una vuelta completa son cuatro cuartos y la flecha apunta de nuevo hacia arriba."},
        {"wrong": "Creer que rotar cambia el tamaño de la figura.", "why": "Se confunde girar con agrandar.", "fix": "Rotar solo cambia hacia dónde apunta la figura."},
    ],
    tiers={
        "recovery": [
            ex(f"{GIRO} Una flecha apunta hacia arriba y gira un cuarto de vuelta. ¿Hacia dónde apunta?", "Hacia la derecha", "El cuarto de vuelta lleva de arriba a derecha."),
            ex(f"{GIRO} Una flecha apunta hacia arriba y gira media vuelta. ¿Hacia dónde apunta?", "Hacia abajo", "Media vuelta son dos cuartos."),
            ex(f"{GIRO} Una flecha apunta hacia abajo y gira media vuelta. ¿Hacia dónde apunta?", "Hacia arriba", "De abajo pasa por la izquierda hasta arriba."),
        ],
        "understand": [
            arith("¿Cuántos cuartos de vuelta forman una vuelta completa?", "4", "Cuatro cuartos hacen un entero.", " cuartos"),
            ex("¿Cuántos cuartos de vuelta tiene una media vuelta?", "2", "La mitad de 4 cuartos son 2 cuartos."),
            ex("Cuando una figura rota, ¿qué punto no se mueve?", "El centro de giro", "Gira alrededor de ese punto."),
        ],
        "apply": [
            ex(f"{GIRO} Una flecha apunta hacia abajo y gira un cuarto de vuelta. ¿Hacia dónde apunta?", "Hacia la izquierda", "De abajo pasa a la izquierda."),
            ex(f"{GIRO} Una flecha apunta hacia la izquierda y gira un cuarto de vuelta. ¿Hacia dónde apunta?", "Hacia arriba", "De izquierda pasa a arriba."),
            ex("La letra b gira media vuelta. ¿Qué letra se ve?", "q", "Al girarla media vuelta queda al revés y al otro lado."),
        ],
        "reason": [
            ex(f"{GIRO} Tomás gira una flecha que apunta hacia arriba una vuelta completa y dice que apunta hacia la derecha. ¿Qué error comete?", "Una vuelta completa la deja como al principio: hacia arriba", "Son cuatro cuartos de vuelta."),
            ex("Las aspas de un ventilador, ¿se trasladan o rotan?", "Rotan", "Giran alrededor del centro."),
        ],
        "challenge": [
            ex(f"{GIRO} Una flecha apunta hacia arriba y gira tres cuartos de vuelta. ¿Hacia dónde apunta?", "Hacia la izquierda", "Arriba, derecha, abajo, izquierda: tres lugares."),
            ex(f"{GIRO} Una flecha apunta hacia la derecha. Gira un cuarto de vuelta y luego media vuelta. ¿Hacia dónde apunta?", "Hacia arriba", "Derecha, luego abajo (un cuarto), luego arriba (dos cuartos más)."),
        ],
    },
    context=[ex("La aguja larga de un reloj apunta al 12. Da un cuarto de vuelta en el sentido del reloj. ¿A qué número apunta?", "Al 3", "Un cuarto de vuelta lleva del 12 al 3.")],
    selfcheck=[
        ex(f"{GIRO} Una flecha apunta hacia la derecha y gira un cuarto de vuelta. ¿Hacia dónde apunta?", "Hacia abajo", "De derecha pasa a abajo."),
        ex("¿Cuántos cuartos de vuelta son tres cuartos de vuelta?", "3", "Tres cuartos de vuelta son tres giros de un cuarto."),
        ex("Una figura que rota, ¿cambia de tamaño?", "No", "Solo cambia hacia dónde apunta."),
    ],
    open_task=task(
        "Recorta una tarjeta con forma de flecha, o dibújala, y ponla apuntando hacia arriba. Gírala un cuarto de vuelta, media vuelta y tres cuartos de vuelta, en el sentido del reloj. Dibuja hacia dónde apunta después de cada giro y escribe cuántos cuartos giraste.",
        "Un cuarto: apunta a la derecha. Media vuelta (2 cuartos): apunta hacia abajo. Tres cuartos: apunta a la izquierda. La flecha no cambió de tamaño.",
        ["parte apuntando hacia arriba", "gira en el sentido del reloj", "dibuja los tres resultados", "escribe los cuartos"],
        ["tres dibujos", "frase"],
        ["girar al revés", "cambiar el tamaño"],
        "Pide que gire el papel físicamente. Reconoce que cuente los cuartos.",
    ),
    reinforce="Con una tarjeta, pon la letra b y gírala media vuelta sobre la mesa. ¿Qué letra se ve?",
    extend="Busca tres objetos de tu casa que giren (por ejemplo, una perilla o una tapa) y explica dónde está el centro de giro.",
)

register(
    OA17, 4,
    materials="Lápiz y papel. Las situaciones están descritas en cada ejercicio.",
    use="Aprenderé a reconocer traslaciones, reflexiones y rotaciones en el entorno. Sirve para entender cómo se mueven las cosas que nos rodean.",
    prior=["Sé qué es trasladar, reflejar y rotar una figura.", "Sé que estas transformaciones no cambian el tamaño."],
    explain=[
        "Hay tres movimientos de figuras 2D. En la traslación la figura cambia de lugar en línea recta sin girar. En la reflexión la figura se da vuelta respecto de un eje, como en un espejo. En la rotación la figura gira alrededor de un punto fijo.",
        "En ninguno de los tres cambia el tamaño ni la forma. Para reconocer cuál es, hazte preguntas: ¿se movió en línea recta sin girar? Es traslación. ¿Hay un espejo o un eje y quedó al revés? Es reflexión. ¿Gira alrededor de un punto? Es rotación.",
        "Ejemplos: una cortina corrediza y baldosas con el mismo dibujo repetido en fila son traslaciones. El reflejo de un árbol en un lago y las alas de una mariposa son reflexiones. Una rueda, las agujas de un reloj y una puerta que se abre (gira en torno a las bisagras) son rotaciones.",
    ],
    vocab=[("traslación", "movimiento en línea recta, sin girar"), ("reflexión", "movimiento como en un espejo, respecto de un eje"), ("rotación", "giro alrededor de un punto"), ("entorno", "lo que nos rodea"), ("simetría", "cuando una figura es igual a ambos lados de un eje")],
    worked=[
        {"title": "Clasificar un movimiento", "problem": "Una cortina se corre de un lado a otro de una ventana. ¿Qué movimiento es?", "steps": ["Se mueve en línea recta.", "No gira.", "Eso es una traslación."], "answer": "Traslación"},
        {"title": "Reconocer un reflejo", "problem": "Una mariposa tiene el mismo dibujo en sus dos alas, como un espejo. ¿Qué movimiento se ve?", "steps": ["Las alas se parecen como si hubiera un espejo en el medio.", "Una ala es el reflejo de la otra respecto de un eje.", "Eso es una reflexión."], "answer": "Reflexión"},
    ],
    mistakes=[
        {"wrong": "Decir que una puerta que se abre se traslada.", "why": "Se piensa que como se mueve de lugar es traslación.", "fix": "La puerta gira alrededor de las bisagras: es una rotación."},
        {"wrong": "Creer que en una reflexión la figura cambia de tamaño.", "why": "Se confunde con agrandar.", "fix": "El reflejo tiene el mismo tamaño y forma; solo queda al revés."},
    ],
    tiers={
        "recovery": [
            ex("Un ventilador gira sus aspas alrededor del centro. ¿Es traslación, reflexión o rotación?", "Rotación", "Gira alrededor de un punto fijo."),
            ex("Tu cara se ve en un espejo. ¿Es traslación, reflexión o rotación?", "Reflexión", "El espejo da vuelta la imagen."),
            ex("Un cajón se abre en línea recta. ¿Es traslación, reflexión o rotación?", "Traslación", "Se mueve en línea recta sin girar."),
        ],
        "understand": [
            ex("¿Cambian el tamaño las tres transformaciones: traslación, reflexión y rotación?", "No", "Mantienen el tamaño y la forma."),
            ex("¿Cuál transformación da vuelta la figura como en un espejo?", "La reflexión", "El eje actúa como un espejo."),
            ex("¿Cuál transformación gira la figura alrededor de un punto?", "La rotación", "Hay un centro de giro."),
        ],
        "apply": [
            ex("Una puerta corrediza de un ropero se mueve en línea recta de lado a lado. ¿Es traslación, reflexión o rotación?", "Traslación", "Se mueve sin girar."),
            ex("Un pato se ve en el agua con su imagen al revés. ¿Es traslación, reflexión o rotación?", "Reflexión", "El agua actúa como un espejo."),
            ex("La manilla de una llave de agua se gira alrededor de su centro. ¿Es traslación, reflexión o rotación?", "Rotación", "Gira alrededor de un punto fijo."),
        ],
        "reason": [
            ex("Camila dice que el reflejo de un árbol en un lago es una traslación porque la imagen está en otro lugar. ¿Qué transformación es en realidad?", "Una reflexión", "La imagen queda al otro lado del agua, como en un espejo."),
            ex("Un diseño de baldosas tiene la misma figura repetida en fila, sin girar. ¿Qué transformación se ve?", "Traslación", "Cada figura está en otro lugar, sin girar."),
        ],
        "challenge": [
            ex("Di qué transformación hay en cada caso: (a) mariposa con las dos alas iguales, (b) tren que avanza por una vía recta, (c) rueda de bicicleta.", "(a) reflexión, (b) traslación, (c) rotación", "Cada caso corresponde a un movimiento distinto."),
            ex("Una figura se refleja y luego se traslada. ¿Cambia su tamaño?", "No", "Ninguna de las dos cambia el tamaño."),
        ],
    },
    context=[ex("En una plaza, un carrusel da vueltas alrededor de su centro. ¿Es traslación, reflexión o rotación?", "Rotación", "Gira alrededor de un punto fijo.")],
    selfcheck=[
        ex("Un reflejo en un lago, ¿es traslación, reflexión o rotación?", "Reflexión", "El agua actúa como un espejo."),
        ex("Una escalera mecánica lleva a una persona en línea recta hacia arriba. ¿Es traslación, reflexión o rotación?", "Traslación", "Se mueve sin girar."),
        ex("Las agujas de un reloj, ¿se trasladan, se reflejan o rotan?", "Rotan", "Giran alrededor del centro del reloj."),
    ],
    open_task=task(
        "Recorre tu casa (o el patio) y encuentra tres movimientos: una traslación, una reflexión y una rotación. Para cada uno escribe qué objeto es y por qué lo clasificas así.",
        "Traslación: un cajón que se abre, porque se mueve en línea recta. Reflexión: mi cara en un espejo, porque queda al revés. Rotación: la tapa de un frasco, porque gira alrededor de un centro.",
        ["nombra tres objetos reales", "clasifica correctamente", "da una razón para cada uno"],
        ["lista de tres ejemplos", "razones"],
        ["confundir puerta que gira con traslación", "no dar razón"],
        "Pide que muestre el movimiento con la mano. Reconoce que explique con las palabras línea recta, espejo o giro.",
    ),
    reinforce="Mira tu casa y busca un objeto que gire y otro que se mueva en línea recta. Clasifícalos.",
    extend="Dibuja una figura y muestra cómo se vería trasladada, reflejada y rotada un cuarto de vuelta.",
)
