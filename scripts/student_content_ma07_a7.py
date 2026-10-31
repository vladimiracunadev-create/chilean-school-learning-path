"""Cuaderno del estudiante de 7.º básico Matemática: OA 10 (ángulos interiores y exteriores de polígonos)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, lesson, task

OA10 = "MA07 OA 10"

# ------------------------------------------------------------------ OA 10 clase 1
lesson(
    OA10, 1,
    use="Aprenderé a descubrir cuánto suman los ángulos interiores de un triángulo y de un cuadrilátero, y a usarlo para hallar un ángulo que falta. Sirve para construir, medir y diseñar figuras.",
    prior=["Sé medir ángulos con transportador y reconocer ángulos rectos.", "Sé clasificar triángulos y cuadriláteros."],
    explain=[
        "Un ángulo interior de un polígono es el que se forma dentro de la figura, entre dos lados que se juntan en un vértice. Los triángulos tienen 3, los cuadriláteros 4. Para descubrir cuánto suman, haz un experimento: dibuja un triángulo cualquiera en una hoja, pinta sus tres esquinas, rásgalas con cuidado y júntalas por el vértice. Siempre forman una línea recta, que mide 180°. Por eso los ángulos interiores de un triángulo suman 180°.",
        "Con esto se puede hallar un ángulo que falta. Si un triángulo tiene ángulos de 50° y 65°, el tercero mide 180° − 50° − 65° = 65°. En un triángulo equilátero, los tres ángulos son iguales: 180° ÷ 3 = 60°. En un triángulo isósceles, los dos ángulos de la base son iguales. En un triángulo rectángulo, un ángulo mide 90° y los otros dos suman 90°.",
        "Un cuadrilátero se puede dividir con una diagonal (un segmento que une dos vértices que no son vecinos) en dos triángulos. Como cada triángulo suma 180°, el cuadrilátero suma 2 · 180° = 360°. Un rectángulo lo comprueba: 4 ángulos de 90° suman 360°. Para hallar el ángulo que falta en un cuadrilátero, resta de 360° los otros tres.",
    ],
    vocab=[("polígono", "figura plana cerrada formada solo por segmentos"), ("ángulo interior", "ángulo que se forma dentro de un polígono en un vértice"), ("vértice", "punto donde se juntan dos lados"), ("diagonal", "segmento que une dos vértices que no son vecinos"), ("conjetura", "idea que se prueba con casos antes de afirmarla")],
    worked=[
        W("Ángulo que falta en un triángulo", "Un triángulo tiene ángulos de 50° y 65°. ¿Cuánto mide el tercero?", ["Los tres ángulos suman 180°.", "180° − 50° − 65° = 65°."], "65°"),
        W("Ángulo que falta en un cuadrilátero", "Un cuadrilátero tiene ángulos de 90°, 90° y 110°. ¿Cuánto mide el cuarto?", ["Los cuatro ángulos suman 360°.", "360° − 90° − 90° − 110° = 70°."], "70°"),
    ],
    mistakes=[
        M("Decir que los ángulos de un cuadrilátero suman 180°.", "Se aplicó la regla del triángulo.", "Un cuadrilátero se divide en dos triángulos: 2 · 180° = 360°."),
        M("Restar de 360° al buscar el tercer ángulo de un triángulo.", "Se usó la suma del cuadrilátero.", "El triángulo suma 180°."),
    ],
    rec=[
        ex("Un triángulo tiene ángulos de 60° y 80°. ¿Cuánto mide el tercero?", "40°", "180° − 60° − 80° = 40°."),
        ex("¿Cuánto suman los ángulos interiores de cualquier cuadrilátero?", "360°", "Se divide en dos triángulos de 180°."),
        ex("¿Cuánto mide cada ángulo de un triángulo equilátero?", "60°", "180° ÷ 3."),
    ],
    und=[
        ex("Un triángulo rectángulo tiene un ángulo de 35° además del recto. ¿Cuánto mide el tercero?", "55°", "180° − 90° − 35° = 55°."),
        ex("Un triángulo isósceles tiene un ángulo de 40° distinto de los otros dos. ¿Cuánto mide cada uno de los ángulos iguales?", "70°", "(180° − 40°) ÷ 2 = 70°."),
        ex("Un cuadrilátero tiene ángulos de 100°, 80° y 95°. ¿Cuánto mide el cuarto?", "85°", "360° − 100° − 80° − 95° = 85°."),
    ],
    app=[
        ex("Un terreno triangular de ejemplo tiene dos esquinas de 72° y 48°. ¿Cuánto mide la tercera esquina?", "60°", "180° − 72° − 48° = 60°."),
        ex("Una cometa de ejemplo tiene ángulos de 110°, 70° y 70°. ¿Cuánto mide el cuarto ángulo?", "110°", "360° − 110° − 70° − 70° = 110°."),
        ex("Un trapecio de ejemplo tiene ángulos de 90°, 90° y 65°. ¿Cuánto mide el cuarto?", "115°", "360° − 90° − 90° − 65° = 115°."),
    ],
    rea=[
        ex("Ana dice que existe un triángulo con ángulos de 70°, 60° y 60°. ¿Es posible?", "No", "Suman 190° y deberían sumar 180°."),
        ex("¿Existe un triángulo con dos ángulos de 90°? Responde sí o no.", "No", "Dos ángulos rectos suman 180° y no quedaría nada para el tercero."),
    ],
    cha=[
        ex("Un triángulo isósceles tiene dos ángulos iguales de x y el tercero mide 2x. ¿Cuánto mide x?", "45°", "x + x + 2x = 180° da 4x = 180° y x = 45°."),
        ex("Un cuadrilátero tiene ángulos de x, x + 10°, x + 20° y x + 30°. ¿Cuánto mide x?", "75°", "4x + 60° = 360° da x = 75°."),
    ],
    ctx=[ex("Un marco de ejemplo tiene forma de cuadrilátero con ángulos de 88°, 92°, 76° y un cuarto desconocido. ¿Cuánto mide el cuarto?", "104°", "360° − 88° − 92° − 76° = 104°.")],
    sc=[
        ex("Un triángulo tiene ángulos de 45° y 45°. ¿Cuánto mide el tercero?", "90°", "180° − 45° − 45°."),
        ex("Un cuadrilátero tiene tres ángulos de 100°. ¿Cuánto mide el cuarto?", "60°", "360° − 300°."),
        ex("¿Cuántos triángulos hay en un cuadrilátero dividido por una diagonal?", "2", "Una diagonal lo parte en dos."),
    ],
    op=task(
        "Con una hoja de papel, dibuja un triángulo cualquiera grande y un cuadrilátero cualquiera grande. (1) Mide los ángulos del triángulo con un transportador y suma. (2) Haz lo mismo con el cuadrilátero. (3) Rasga las tres esquinas del triángulo y júntalas por el vértice para ver qué forman. (4) Escribe qué descubriste. Si tus sumas se alejan un poco de 180° y 360°, explica por qué pudo pasar.",
        "Triángulo: la suma de los tres ángulos medidos es cercana a 180° y las esquinas rasgadas forman una línea recta. Cuadrilátero: la suma es cercana a 360°. Las diferencias de uno o dos grados se deben a errores al medir.",
        ["mide y suma los ángulos de ambas figuras", "relaciona la suma con 180° y 360°", "explica las diferencias por errores de medición"],
        ["dibujos con medidas", "sumas escritas", "frase de conclusión"],
        ["medir desde la marca equivocada del transportador", "no usar ambas figuras"],
        "Pide que repita la medición de un ángulo para comprobar y que compare con otra persona.",
    ),
    reinforce="Un triángulo tiene ángulos de 28° y 73°. Calcula el tercero. Luego calcula el cuarto ángulo de un cuadrilátero con 84°, 112° y 76°.",
    extend="Explica con un dibujo por qué la suma de los ángulos de un cuadrilátero es el doble de la de un triángulo.",
)

# ------------------------------------------------------------------ OA 10 clase 2
lesson(
    OA10, 2,
    use="Aprenderé a dividir un polígono en triángulos para encontrar una regla que da la suma de sus ángulos interiores. Sirve para calcular ángulos en pentágonos, hexágonos y otras figuras.",
    prior=["Sé que los ángulos de un triángulo suman 180° y los de un cuadrilátero 360°.", "Sé qué es una diagonal."],
    explain=[
        "Un polígono de n lados tiene n vértices. Si eliges un vértice y trazas todas las diagonales que salen de él, el polígono queda dividido en triángulos. Desde un vértice no se puede trazar diagonal hacia sí mismo ni hacia sus 2 vecinos, así que salen n − 3 diagonales. Estas diagonales forman n − 2 triángulos. Un pentágono (5 lados) tiene 2 diagonales desde un vértice y 3 triángulos.",
        "Como cada triángulo suma 180°, la suma de los ángulos interiores de un polígono de n lados es (n − 2) · 180°. Para un cuadrilátero: 2 · 180° = 360°. Para un pentágono: 3 · 180° = 540°. Para un hexágono: 4 · 180° = 720°. Esta es la regla general que descubrimos con el dibujo, una conjetura que se comprueba con cada caso.",
        "En un polígono regular, todos los lados y todos los ángulos son iguales. Entonces cada ángulo interior mide la suma dividida por el número de lados: (n − 2) · 180° ÷ n. Un hexágono regular tiene 720° ÷ 6 = 120° en cada ángulo. Un octágono regular tiene 1.080° ÷ 8 = 135°. Siempre es una cantidad entera de triángulos, así que la suma es múltiplo de 180°.",
    ],
    vocab=[("polígono regular", "polígono con todos sus lados y ángulos iguales"), ("n", "letra que representa el número de lados de un polígono"), ("triangular", "dividir un polígono en triángulos con diagonales desde un vértice"), ("pentágono", "polígono de 5 lados"), ("hexágono", "polígono de 6 lados")],
    worked=[
        W("Triangular un hexágono", "Calcula la suma de los ángulos interiores de un hexágono.", ["Desde un vértice se trazan 6 − 3 = 3 diagonales y quedan 6 − 2 = 4 triángulos.", "4 · 180° = 720°."], "720°"),
        W("Ángulo de un polígono regular", "¿Cuánto mide cada ángulo interior de un pentágono regular?", ["Suma: (5 − 2) · 180° = 540°.", "Cada ángulo: 540° ÷ 5 = 108°."], "108°"),
    ],
    mistakes=[
        M("Calcular la suma de un octágono como 8 · 180°.", "Se multiplicó por el número de lados en vez de por n − 2.", "(8 − 2) · 180° = 1.080°."),
        M("Creer que un polígono de 7 lados forma 7 triángulos.", "Se contaron todos los lados.", "Salen 7 − 3 = 4 diagonales y se forman 7 − 2 = 5 triángulos."),
    ],
    rec=[
        ex("¿Cuántos triángulos se forman al triangular un pentágono desde un vértice?", "3", "5 − 2 = 3."),
        ex("¿Cuántas diagonales salen de un vértice de un octágono (8 lados)?", "5", "8 − 3 = 5."),
        ex("¿Cuánto suman los ángulos interiores de un heptágono (7 lados)?", "900°", "(7 − 2) · 180° = 900°."),
    ],
    und=[
        ex("¿Cuánto suman los ángulos interiores de un decágono (10 lados)?", "1.440°", "(10 − 2) · 180° = 1.440°."),
        ex("Un polígono tiene ángulos interiores que suman 1.080°. ¿Cuántos lados tiene?", "8", "1.080° ÷ 180° = 6 triángulos y 6 + 2 = 8 lados."),
        ex("¿Cuánto mide cada ángulo interior de un octágono regular?", "135°", "1.080° ÷ 8 = 135°."),
    ],
    app=[
        ex("Un mosaico de ejemplo usa baldosas con forma de pentágono regular. ¿Cuánto mide cada ángulo de una baldosa?", "108°", "540° ÷ 5."),
        ex("Un hexágono irregular de ejemplo tiene cinco ángulos de 130°, 110°, 120°, 125° y 115°. ¿Cuánto mide el sexto ángulo?", "120°", "720° − (130° + 110° + 120° + 125° + 115°) = 720° − 600° = 120°."),
        ex("¿Cuántas diagonales salen de un vértice de un polígono de 12 lados?", "9", "12 − 3 = 9."),
    ],
    rea=[
        ex("Pía calculó la suma de los ángulos de un nonágono (9 lados) como 9 · 180° = 1.620°. ¿Cuál es el resultado correcto?", "1.260°", "La regla es (n − 2) · 180°: 7 · 180° = 1.260°."),
        ex("¿Puede un polígono tener ángulos interiores que sumen 1.000°? Responde sí o no.", "No", "1.000 ÷ 180 no es un número entero de triángulos."),
    ],
    cha=[
        ex("Un polígono regular tiene ángulos interiores de 150°. ¿Cuántos lados tiene? (Prueba con 10, 12 o 15 lados.)", "12", "Con 12 lados: 1.800° ÷ 12 = 150°."),
        ex("¿Cuánto suman los ángulos interiores de un polígono de 15 lados?", "2.340°", "(15 − 2) · 180° = 13 · 180°."),
    ],
    ctx=[ex("Un escudo de ejemplo tiene forma de hexágono regular. ¿Cuánto mide cada ángulo interior?", "120°", "720° ÷ 6 = 120°.")],
    sc=[
        ex("¿Cuántos triángulos se forman al triangular un hexágono?", "4", "6 − 2."),
        ex("¿Cuánto suman los ángulos interiores de un pentágono?", "540°", "3 · 180°."),
        ex("¿Cuánto mide cada ángulo interior de un cuadrado?", "90°", "360° ÷ 4."),
    ],
    op=task(
        "Completa esta tabla de ejemplo con las columnas «lados (n)», «diagonales desde un vértice», «triángulos» y «suma de ángulos interiores» para n = 3, 4, 5, 6, 7 y 8. Dibuja la triangulación del pentágono y del hexágono. Luego escribe la regla con letras y úsala para calcular la suma de un polígono de 11 lados.",
        "n = 3: 0 diagonales, 1 triángulo, 180°. n = 4: 1, 2, 360°. n = 5: 2, 3, 540°. n = 6: 3, 4, 720°. n = 7: 4, 5, 900°. n = 8: 5, 6, 1.080°. Regla: (n − 2) · 180°. Con n = 11: 9 · 180° = 1.620°.",
        ["completa bien la tabla", "dibuja las triangulaciones", "formula y usa la regla"],
        ["tabla completa", "dos dibujos", "regla con letras y un cálculo"],
        ["olvidar el −2", "trazar diagonales desde varios vértices"],
        "Pide que cuente los triángulos del dibujo y compare con n − 2.",
    ),
    reinforce="Calcula la suma de los ángulos de un polígono de 7 lados y el ángulo interior de un polígono regular de 9 lados.",
    extend="Explica por qué la fórmula (n − 2) · 180° da 180° para el triángulo y 360° para el cuadrilátero.",
)

# ------------------------------------------------------------------ OA 10 clase 3
lesson(
    OA10, 3,
    use="Aprenderé la relación entre ángulos interiores y exteriores de un polígono y que los ángulos exteriores suman 360°. Sirve para calcular ángulos y para saber cuántos lados tiene un polígono regular.",
    prior=["Sé la suma de los ángulos interiores de un polígono.", "Sé que ángulos que forman una línea recta suman 180°."],
    explain=[
        "Un ángulo exterior de un polígono se forma al prolongar uno de sus lados. Junto con el ángulo interior del mismo vértice forman una línea recta, así que interior + exterior = 180°. Si el ángulo interior mide 70°, el exterior mide 110°. Si el exterior mide 45°, el interior mide 135°.",
        "Si se toma un ángulo exterior por cada vértice, todos esos ángulos juntos suman 360°, sin importar el número de lados. Es como dar una vuelta completa al recorrer la figura por afuera. En un polígono regular los exteriores son iguales: cada uno mide 360° ÷ n. Un pentágono regular tiene exteriores de 72°, y entonces interiores de 108°.",
        "En un triángulo hay otra relación: un ángulo exterior es igual a la suma de los dos ángulos interiores que no están a su lado. Si el exterior mide 110°, los otros dos interiores suman 110°. Así se pueden hallar ángulos faltantes de dos maneras y se comprueban entre sí.",
    ],
    vocab=[("ángulo exterior", "ángulo entre un lado y la prolongación del lado vecino"), ("prolongar", "extender un lado más allá de un vértice"), ("ángulos suplementarios", "dos ángulos que suman 180°"), ("vuelta completa", "ángulo de 360°"), ("interior no adyacente", "ángulo interior de un triángulo que no está pegado al exterior")],
    worked=[
        W("Interior y exterior", "Un ángulo interior mide 70°. ¿Cuánto mide el exterior del mismo vértice?", ["Interior + exterior = 180°.", "180° − 70° = 110°."], "110°"),
        W("Polígono regular", "¿Cuánto mide cada ángulo exterior de un hexágono regular y cada interior?", ["Exterior: 360° ÷ 6 = 60°.", "Interior: 180° − 60° = 120°."], "60° exterior y 120° interior"),
    ],
    mistakes=[
        M("Decir que los tres ángulos exteriores de un triángulo suman 180°.", "Se confundió con la suma de los interiores.", "Los exteriores (uno por vértice) suman 360°."),
        M("Calcular el ángulo exterior de un cuadrado como 360° ÷ 90°.", "Se dividió entre el ángulo en vez de entre los lados.", "Exterior = 360° ÷ 4 = 90°, o 180° − 90° = 90°."),
    ],
    rec=[
        ex("Un ángulo interior mide 100°. ¿Cuánto mide su ángulo exterior?", "80°", "180° − 100°."),
        ex("Un ángulo exterior mide 45°. ¿Cuánto mide su ángulo interior?", "135°", "180° − 45°."),
        ex("¿Cuánto suman los ángulos exteriores (uno por vértice) de cualquier polígono?", "360°", "Es una vuelta completa."),
    ],
    und=[
        ex("¿Cuánto mide cada ángulo exterior de un pentágono regular?", "72°", "360° ÷ 5."),
        ex("¿Cuánto mide cada ángulo exterior de un octágono regular?", "45°", "360° ÷ 8."),
        ex("Dos ángulos exteriores de un triángulo miden 110° y 130°. ¿Cuánto mide el tercero?", "120°", "360° − 110° − 130°."),
    ],
    app=[
        ex("Un polígono regular tiene ángulos exteriores de 36°. ¿Cuántos lados tiene?", "10", "360° ÷ 36° = 10."),
        ex("Un polígono regular tiene ángulos exteriores de 40°. ¿Cuánto mide cada ángulo interior?", "140°", "180° − 40°."),
        ex("En un triángulo, un ángulo exterior mide 110° y uno de los interiores no adyacentes mide 45°. ¿Cuánto mide el otro interior no adyacente?", "65°", "Los dos suman 110° y 110° − 45° = 65°."),
    ],
    rea=[
        ex("Luis dice que los ángulos exteriores de un triángulo suman 180°. ¿Tiene razón?", "No", "Suman 360°, igual que en cualquier polígono."),
        ex("¿Puede un polígono regular tener ángulos exteriores de 50°? Responde sí o no.", "No", "360 ÷ 50 = 7,2 y el número de lados debe ser entero."),
    ],
    cha=[
        ex("En un polígono regular, el ángulo interior es 8 veces el exterior. ¿Cuántos lados tiene?", "18", "Interior + exterior = 180° da 9 · exterior = 180° y exterior = 20°; 360 ÷ 20 = 18."),
        ex("En un triángulo isósceles, el ángulo exterior en un vértice de la base mide 110°. ¿Cuánto mide el ángulo de la cima?", "40°", "Los ángulos de la base miden 70° cada uno y 180° − 140° = 40°."),
    ],
    ctx=[ex("Un tapiz de ejemplo tiene forma de nonágono regular (9 lados). ¿Cuánto mide cada ángulo exterior?", "40°", "360° ÷ 9.")],
    sc=[
        ex("Un ángulo interior mide 128°. ¿Cuánto mide su exterior?", "52°", "180° − 128°."),
        ex("¿Cuánto mide cada ángulo exterior de un cuadrado?", "90°", "360° ÷ 4."),
        ex("En un triángulo, un ángulo exterior mide 120°. ¿Cuánto suman los dos interiores no adyacentes?", "120°", "Es igual al exterior."),
    ],
    op=task(
        "Dibuja un triángulo cualquiera con regla. Prolonga uno de sus lados en cada vértice para marcar los tres ángulos exteriores (uno por vértice, siguiendo siempre el mismo sentido). (1) Mide con transportador los tres ángulos interiores y los tres exteriores. (2) Comprueba que cada interior más su exterior suma 180°. (3) Suma los tres exteriores y compara con 360°. (4) Escribe qué relación encuentras entre un exterior y los dos interiores no adyacentes.",
        "Cada par interior-exterior suma 180° (con pequeñas diferencias de medición). Los tres exteriores suman cerca de 360°. Cada exterior es igual a la suma de los dos interiores que no están a su lado.",
        ["mide e interpreta los seis ángulos", "comprueba las sumas 180° y 360°", "formula la relación del triángulo"],
        ["dibujo con medidas", "sumas escritas", "frase de conclusión"],
        ["prolongar el lado en dirección distinta en cada vértice", "confundir interior y exterior"],
        "Pide que repita la construcción con otro triángulo y vea si la relación se mantiene.",
    ),
    reinforce="Un ángulo interior mide 112°. Calcula el exterior. Luego calcula el ángulo exterior de un cuadrado y de un decágono regular (10 lados).",
    extend="Demuestra con letras que, en un polígono regular de n lados, el ángulo interior es 180° − 360°/n.",
)

# ------------------------------------------------------------------ OA 10 clase 4
lesson(
    OA10, 4,
    use="Aprenderé a resolver problemas con medidas de ángulos que faltan y a justificar cada paso con una propiedad. Sirve para explicar por qué un resultado es correcto.",
    prior=["Sé la suma de los ángulos interiores de un polígono.", "Sé la relación entre ángulos interiores y exteriores."],
    explain=[
        "Para resolver un problema de ángulos faltantes sigue estos pasos. Primero, haz un dibujo y anota los datos. Segundo, elige la propiedad: suma de interiores del polígono, interior + exterior = 180°, o suma de exteriores = 360°. Tercero, plantea la cuenta, que puede ser una ecuación con una letra. Cuarto, resuelve. Quinto, comprueba que los ángulos sumen lo que corresponde.",
        "Justificar significa decir qué propiedad usaste en cada paso. Por ejemplo: «El pentágono suma 540° porque se forma con 3 triángulos». O: «El ángulo interior mide 50° porque forma una línea recta con el exterior de 130°». Una buena justificación nombra la propiedad y muestra la cuenta.",
        "También puedes plantear una ecuación cuando los ángulos tienen una letra. Si un pentágono tiene ángulos de x, x, 100°, 110° y 130°, la suma es 2x + 340° = 540°, entonces 2x = 200° y x = 100°. Comprueba sumando los cinco ángulos: 100° + 100° + 100° + 110° + 130° = 540°. Revisa siempre que las respuestas tengan sentido en la figura.",
    ],
    vocab=[("justificar", "explicar con qué propiedad se obtiene un resultado"), ("ecuación", "igualdad con una letra que representa un valor desconocido"), ("propiedad", "regla que siempre se cumple"), ("medida faltante", "ángulo o lado que se debe calcular"), ("comprobar", "revisar el resultado con otra vía")],
    worked=[
        W("Con una ecuación", "Un pentágono de ejemplo tiene ángulos de x, x, 100°, 110° y 130°. ¿Cuánto vale x?", ["Un pentágono suma 540°: 2x + 340° = 540°.", "2x = 200°, entonces x = 100°. Compruebo: 100° + 100° + 100° + 110° + 130° = 540°."], "100°"),
        W("Con ángulo exterior", "En un triángulo isósceles el ángulo exterior en un vértice de la base mide 130°. ¿Cuánto mide el ángulo del vértice opuesto a la base?", ["El interior de ese vértice mide 180° − 130° = 50°, y el otro ángulo de la base también.", "El tercero mide 180° − 50° − 50° = 80°."], "80°"),
    ],
    mistakes=[
        M("Resolver un pentágono con ángulos x, x, 90°, 110° y 120° usando 360° en vez de 540°.", "Se usó la suma del cuadrilátero.", "Un pentágono suma 540°: 2x + 320° = 540° y x = 110°."),
        M("No justificar el resultado y escribir solo «50°».", "Falta nombrar la propiedad usada.", "Escribir: «50° porque 180° − 130° = 50° por ser ángulos que forman una línea recta»."),
    ],
    rec=[
        ex("Un triángulo tiene ángulos de 55° y 65°. ¿Cuánto mide el tercero?", "60°", "180° − 55° − 65°."),
        ex("Un ángulo exterior mide 80°. ¿Cuánto mide el interior del mismo vértice?", "100°", "180° − 80°."),
        ex("¿Cuánto suman los ángulos interiores de un hexágono?", "720°", "(6 − 2) · 180°."),
    ],
    und=[
        ex("Un cuadrilátero tiene ángulos de 85°, 95° y 100°. ¿Cuánto mide el cuarto?", "80°", "360° − 280°."),
        ex("Cinco ángulos de un hexágono suman 600°. ¿Cuánto mide el sexto?", "120°", "720° − 600°."),
        ex("¿Cuánto mide el ángulo exterior de un nonágono regular (9 lados)?", "40°", "360° ÷ 9."),
    ],
    app=[
        ex("Un pentágono de ejemplo tiene ángulos de x, x, 80°, 120° y 140°. ¿Cuánto vale x?", "100°", "2x + 340° = 540°; 2x = 200°."),
        ex("En un hexágono regular, ¿cuánto miden el ángulo exterior y el interior?", "60° y 120°", "Exterior: 360° ÷ 6. Interior: 180° − 60°."),
        ex("Un triángulo tiene un ángulo exterior de 150° y un interior no adyacente de 90°. ¿Cuánto mide el otro interior no adyacente?", "60°", "150° − 90° = 60°."),
    ],
    rea=[
        ex("Dani dice que un triángulo tiene ángulos exteriores de 100°, 120° y 130°. ¿Es posible?", "No", "Suman 350° y deberían sumar 360°."),
        ex("Marta dice que un ángulo exterior de un triángulo mide 150° y los interiores no adyacentes miden 90° y 70°. ¿Es posible?", "No", "90° + 70° = 160° y debería ser 150°."),
    ],
    cha=[
        ex("Un pentágono tiene ángulos exteriores de 60°, 70°, 80° y 90° en cuatro vértices. ¿Cuánto mide el exterior del quinto vértice?", "60°", "360° − (60° + 70° + 80° + 90°) = 60°."),
        ex("Un polígono regular tiene ángulos interiores que suman 1.440°. ¿Cuántos lados tiene y cuánto mide cada ángulo interior?", "10 lados; 144°", "1.440 ÷ 180 = 8 triángulos y 8 + 2 = 10 lados; 1.440° ÷ 10 = 144°."),
    ],
    ctx=[ex("Una señal de ejemplo tiene forma de octágono regular. ¿Cuánto mide cada ángulo exterior y cada ángulo interior?", "45° y 135°", "Exterior: 360° ÷ 8 = 45°. Interior: 180° − 45° = 135°.")],
    sc=[
        ex("Un triángulo tiene ángulos de 90° y 30°. ¿Cuánto mide el tercero?", "60°", "180° − 120°."),
        ex("Un cuadrilátero tiene ángulos de 120°, 60° y 80°. ¿Cuánto mide el cuarto?", "100°", "360° − 260°."),
        ex("Un ángulo interior de un polígono mide 125°. ¿Cuánto mide su exterior?", "55°", "180° − 125°."),
    ],
    op=task(
        "Resuelve este problema de ejemplo y justifica cada paso. Un jardín tiene forma de pentágono con cinco ángulos interiores: 100°, 110°, 120°, 130° y x. (a) Calcula x usando la suma de ángulos interiores. (b) Calcula el ángulo exterior del vértice de 110°. (c) Escribe una frase que justifique cada resultado, nombrando la propiedad usada. (d) Comprueba que los cinco ángulos suman lo que corresponde.",
        "(a) La suma de un pentágono es 540°; 100° + 110° + 120° + 130° = 460° y x = 80°. (b) 180° − 110° = 70°. (c) Cada paso se justifica con la propiedad: pentágono = 3 triángulos = 540°; interior + exterior = 180°. (d) 100° + 110° + 120° + 130° + 80° = 540°.",
        ["usa la suma de interiores del pentágono", "calcula el exterior", "justifica con propiedades", "comprueba el resultado"],
        ["cálculos escritos", "justificación por frase", "comprobación"],
        ["usar 360° para un pentágono", "no nombrar la propiedad"],
        "Pide que lea su justificación como si se la explicara a otra persona.",
    ),
    reinforce="Un hexágono tiene cinco ángulos de 100°, 110°, 130°, 120° y 125°. Calcula el sexto y justifica.",
    extend="Plantea un problema de ángulos de un polígono con una letra en dos de sus ángulos y resuélvelo con una ecuación.",
)
