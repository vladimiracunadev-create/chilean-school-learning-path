"""Geometría 3D (electivo HC, 3.º y 4.º medio): OAC-04 (conjeturas sobre figuras generadas por traslación y rotación) y OAC-05 (perspectiva, proyecciones, puntos de fuga y elevaciones), clases 1 a 4 y 1 a 5. Todo en papel; las herramientas digitales se describen por escrito."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, regla, escuadra y papel cuadriculado; calculadora simple opcional. No se necesita software: las herramientas digitales "
             "(hoja de cálculo o geometría dinámica) se describen en la ficha y se razonan a mano. Si usas un programa, hazlo con la supervisión de tu docente. "
             "No se corta ni se arma ningún objeto real: los cuerpos se imaginan o se dibujan.")
build = make_build(MATERIALS)

O4 = "MA-GE3D-3y4-OAC-04"
O5 = "MA-GE3D-3y4-OAC-05"

# ============================================================ OAC-04, clase 1
F = ("Ficha 1 (de ejemplo). Una figura plana se traslada perpendicularmente a su plano una distancia h (la altura); el sólido que barre es un prisma si la figura es un polígono y un cilindro si es un círculo. "
     "Caso A: rectángulo de 3 cm por 4 cm trasladado 5 cm. Caso B: triángulo rectángulo de catetos 3 cm y 4 cm (hipotenusa 5 cm) trasladado 6 cm. Caso C: círculo de radio 2 cm trasladado 7 cm. "
     "Conjeturas: volumen = área de la base · h; área lateral = perímetro de la base · h.")
build(
    O4, 1, F,
    use="Aprenderé a formular conjeturas sobre la forma, el área y el volumen de sólidos que resultan de trasladar una figura plana, y a verificarlas con casos y razonamiento.",
    prior=["Sé calcular áreas y perímetros de rectángulos, triángulos y círculos.", "Sé que una traslación conserva la forma de una figura.", "Sé calcular volúmenes de prismas y cilindros con fórmulas."],
    explain=[
        "Si una figura plana se traslada perpendicularmente a su plano, cada punto describe un segmento y la figura barre un sólido. Un polígono produce un prisma; un círculo produce un cilindro. La distancia de la traslación es la altura h. Las dos bases son la figura inicial y la final, y los lados forman la superficie lateral.",
        "Una conjetura es una afirmación que creemos cierta a partir de casos. Para este tema se conjetura que el volumen es el área de la base por la altura, y que el área lateral es el perímetro de la base por la altura (se «desenrolla» la superficie lateral en un rectángulo). El área total suma las dos bases más la lateral. Verificar es probar la conjetura con varios casos y buscar contraejemplos; un caso que falla basta para refutarla.",
        "Si la traslación no es perpendicular, el sólido es un prisma oblicuo. Su volumen sigue siendo el área de la base por la altura perpendicular, que es la distancia entre los planos de las dos bases, y no por el largo del desplazamiento inclinado. Una herramienta digital permite probar muchos casos, pero un resultado válido siempre se respalda con cálculo y con una razón general.",
    ],
    vocab=[("conjetura", "afirmación que se cree cierta y se debe verificar"), ("prisma", "sólido barrido por un polígono trasladado"), ("cilindro", "sólido barrido por un círculo trasladado"), ("altura", "distancia perpendicular entre las bases"), ("área lateral", "área de las caras que unen las bases"), ("contraejemplo", "caso que refuta una conjetura")],
    worked=[
        ("Verificar una conjetura con un caso", "Un cuadrado de lado 5 cm se traslada 2 cm. Calcula el volumen y el área total con las conjeturas.", ["Volumen: 5 · 5 · 2 = 50. Perímetro de la base: 20, así que el área lateral es 20 · 2 = 40.", "Área total: 2 · 25 + 40 = 90."], "Volumen 50 cm³ y área total 90 cm²"),
        ("Verificar contando cubos", "Un rectángulo de 2 cm por 3 cm se traslada 4 cm. ¿Cuántos cubos de 1 cm³ caben?", ["Cada capa tiene 2 · 3 = 6 cubos.", "Hay 4 capas: 6 · 4 = 24 cubos."], "24 cm³, que coincide con área de la base por altura"),
    ],
    mistakes=[("Usar el largo del desplazamiento inclinado como altura.", "La altura es la distancia perpendicular entre las bases.", "Mide la altura en perpendicular al plano de la base."),
              ("Creer que probar un caso demuestra la conjetura.", "Un caso apoya; solo un argumento general la prueba, y un contraejemplo la refuta.", "Prueba varios casos y busca uno que falle.")],
    T=[
        ('abc', '¿Qué sólido se obtiene al trasladar un círculo perpendicularmente a su plano?', 'Un cilindro', 'Un prisma de base cuadrada', 'Un cono', 'El círculo barre un cuerpo con dos bases circulares iguales, es decir, un cilindro.'),
        ('abc', '{F} En el caso A, ¿qué sólido se obtiene y cuántas caras tiene?', 'Un prisma rectangular con 6 caras', 'Un prisma triangular con 5 caras', 'Un cilindro con 3 caras', 'La base rectangular y su copia dan dos caras, y los cuatro lados dan cuatro caras laterales.'),
        ('ab', 'En la conjetura «volumen = área de la base · h», ¿qué medida es h?', 'La distancia de la traslación, medida en perpendicular a la base', 'El perímetro de la base', 'La altura es la distancia entre las dos bases, no una medida de la base misma.'),
        ('=', '{F} ¿Cuál es el volumen del sólido del caso A?', '3*4*5', 'Se multiplica el área de la base, 3 · 4, por la altura 5.', ' cm³'),
        ('=', '{F} ¿Cuál es el área lateral del sólido del caso A? El perímetro de la base es 14 cm.', '(3+4)*2*5', 'El área lateral es el perímetro de la base por la altura.', ' cm²'),
        ('{F} ¿Cuál es el volumen del sólido del caso B? El área de la base es 6 cm².', '36 cm³', 'Se multiplica el área de la base, 6, por la altura 6.'),
        ('{F} ¿Cuál es el volumen del cilindro del caso C? Deja π sin reemplazar.', '28π cm³', 'La base tiene área π · 2² = 4π, y se multiplica por la altura 7.'),
        ('=', '{F} ¿Cuál es el área total del sólido del caso B? Las bases miden 6 cm² y el perímetro de la base es 12 cm.', '2*6+12*6', 'Se suman las dos bases y el área lateral, que es perímetro por altura.', ' cm²'),
        ('abc', 'Un cuadrado de lado 4 cm se traslada 4 cm perpendicularmente. ¿Qué sólido es y cuánto vale su volumen?', 'Un cubo de 64 cm³', 'Un prisma de 32 cm³', 'Un cilindro de 64 cm³', 'La base de 16 cm² multiplicada por la altura 4 da 64 cm³, y todas las aristas miden 4 cm.'),
        ('abc', 'Una estudiante conjetura: «el área lateral es la mitad del área de la base por la altura». ¿Qué prueba la refuta?', 'En el caso A el área lateral es 70 cm², pero esa fórmula daría 30 cm²', 'En el caso A el volumen es 60 cm³', 'La conjetura es cierta en todos los casos', 'Basta un caso donde la fórmula no coincide con el cálculo directo para refutarla.'),
        ('abc', 'El rectángulo del caso A se traslada de manera inclinada: avanza 5 cm de largo pero sube solo 4 cm en perpendicular. ¿Cuál es su volumen?', '48 cm³', '60 cm³', '20 cm³', 'El volumen usa la altura perpendicular: 12 · 4; con 5 cm saldrían 60 cm³, que ya no es la altura.'),
        ('Un cilindro se forma al trasladar 5 cm un círculo y su volumen es 45π cm³. ¿Cuál es el radio del círculo?', '3 cm', 'Se cumple π · r² · 5 = 45π, así que r² = 9 y r = 3.'),
        ('Un prisma de base cuadrada de lado 3 cm y altura 3 cm se agranda duplicando el lado y la altura. ¿Por cuánto se multiplica su volumen?', 'Por 8: pasa de 27 a 216 cm³', 'El volumen depende de tres longitudes, y cada una se duplica: 2 · 2 · 2.'),
    ],
    ctx=('=', 'Un estanque tiene forma de prisma de base rectangular de 3 m por 4 m y 2 m de profundidad. Si 1 m³ equivale a 1.000 litros, ¿cuántos litros caben?', '3*4*2*1000', 'Se calcula el volumen como base por profundidad y se pasa de m³ a litros.', ' litros'),
    sc=[
        ("En Geometría 3D: ¿qué sólido barre un círculo al trasladarse?", "Un cilindro", "Sus dos bases son círculos iguales."),
        ("¿Cómo se calcula el área lateral con la conjetura?", "Perímetro de la base por la altura", "La superficie lateral se desenrolla en un rectángulo."),
        ("¿Cuántos contraejemplos bastan para refutar una conjetura?", "Uno", "Un caso que falla invalida la afirmación general."),
    ],
    op=("Elige un caso: (a) un triángulo rectángulo de catetos 6 cm y 8 cm (hipotenusa 10 cm) trasladado 5 cm; (b) un círculo de radio 3 cm trasladado 4 cm. Calcula el volumen, el área lateral y el área total (deja π). Luego comprueba la conjetura de volumen en un segundo caso que elijas y escribe una frase que justifique por qué vale.",
        "Caso (a): la base tiene área 6 · 8 ÷ 2 = 24 y perímetro 24; el volumen es 24 · 5 = 120 cm³, el área lateral es 24 · 5 = 120 cm² y el área total es 2 · 24 + 120 = 168 cm².",
        ["identifica la base y la altura", "usa las fórmulas con unidades", "compara con un segundo caso"],
        ["hoja con cálculos, unidades y la frase de justificación"],
        ["usar la hipotenusa como altura", "olvidar una base en el área total", "decir que se probó con un solo caso"],
        "Pregunta: «¿cuál es la altura del sólido?». Si usa un lado de la base, pídele que la mida perpendicular."),
    reinforce="Con una caja de fósforos vacía o una hoja doblada, imagina las capas de una torre de cuadrados y cuenta cuántas capas hacen un volumen dado.",
    extend="Explica por qué un prisma oblicuo tiene el mismo volumen que uno recto con igual base y altura perpendicular.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 2 (de ejemplo). Una figura plana gira una vuelta completa alrededor de una recta (el eje) de su mismo plano y barre un sólido de revolución. "
     "Caso A: rectángulo de 3 cm de ancho y 5 cm de alto con un lado sobre el eje (cilindro de radio 3 y altura 5). Caso B: triángulo rectángulo de catetos 3 cm y 4 cm que gira alrededor del cateto de 4 cm (cono de radio 3, altura 4 y generatriz 5). "
     "Caso C: semicírculo de radio 3 cm que gira alrededor de su diámetro (esfera de radio 3). Caso D: rectángulo de 2 cm de ancho y 5 cm de alto, separado 1 cm del eje (cilindro hueco de radio exterior 3 y radio interior 1). "
     "Fórmulas: cilindro π r² h; cono 1/3 π r² h con área lateral π r g; esfera 4/3 π r³; cilindro hueco π (R² − r²) h.")
build(
    O4, 2, F,
    use="Aprenderé a predecir qué sólido genera una figura plana al girar, a calcular su volumen y su área, y a verificar conjeturas con casos y contraejemplos.",
    prior=["Sé calcular volúmenes de cilindro, cono y esfera con fórmulas.", "Sé usar el teorema de Pitágoras.", "Sé formular y probar una conjetura con casos."],
    explain=[
        "Un sólido de revolución se genera al girar una figura plana alrededor de un eje de su plano. Un rectángulo con un lado sobre el eje genera un cilindro; un triángulo rectángulo que gira sobre un cateto genera un cono; un semicírculo que gira sobre su diámetro genera una esfera. Si la figura queda separada del eje, el sólido tiene un hueco central: por ejemplo, un rectángulo alejado del eje genera un cilindro hueco.",
        "La forma se predice imaginando el giro: cada punto de la figura traza una circunferencia cuyo radio es su distancia al eje. Por eso el radio del sólido es la distancia máxima de la figura al eje, y la altura es la medida a lo largo del eje. Con esos dos datos se aplican las fórmulas de volumen y área, y para un cono se usa la generatriz g, que se halla con Pitágoras.",
        "Una conjetura típica es «girar la misma figura alrededor de ejes distintos da el mismo volumen». Se verifica calculando casos y se refuta con un contraejemplo. Para argumentar siempre se declara cuál fue el eje, porque la misma figura genera sólidos distintos con ejes distintos. Un programa de geometría dinámica 3D podría mostrar el giro, pero el cálculo es lo que justifica.",
    ],
    vocab=[("sólido de revolución", "sólido que resulta de girar una figura plana alrededor de un eje"), ("eje de giro", "recta fija alrededor de la cual gira la figura"), ("generatriz", "segmento que une el vértice del cono con el borde de la base"), ("cilindro hueco", "cilindro con un agujero cilíndrico central"), ("radio exterior e interior", "distancias mayor y menor al eje"), ("semicírculo", "mitad de un círculo")],
    worked=[
        ("Cono por giro", "Un triángulo rectángulo de catetos 5 cm y 12 cm (hipotenusa 13 cm) gira alrededor del cateto de 12 cm. Calcula el volumen y el área lateral del cono.", ["El radio es 5 y la altura 12. El volumen es 1/3 · π · 25 · 12 = 100π.", "El área lateral es π · r · g = π · 5 · 13 = 65π."], "Volumen 100π cm³ y área lateral 65π cm²"),
        ("Refutar con un contraejemplo", "Alguien conjetura que un rectángulo de 2 cm por 6 cm genera el mismo volumen al girar sobre el lado de 6 cm que sobre el lado de 2 cm. ¿Es cierto?", ["Sobre el lado de 6: r = 2 y h = 6, volumen π · 4 · 6 = 24π.", "Sobre el lado de 2: r = 6 y h = 2, volumen π · 36 · 2 = 72π."], "Falso: 24π ≠ 72π, así que el eje importa"),
    ],
    mistakes=[("Olvidar que el eje cambia el sólido: usar siempre el mismo lado como radio.", "El radio es la distancia al eje y la altura es la medida a lo largo del eje.", "Marca el eje primero y luego identifica radio y altura."),
              ("Usar la altura en lugar de la generatriz en el área lateral del cono.", "El área lateral usa g, que es la medida inclinada.", "Calcula g con Pitágoras antes de usar π r g.")],
    T=[
        ('abc', 'Un rectángulo gira sobre uno de sus lados. ¿Qué sólido genera?', 'Un cilindro', 'Un cono', 'Una esfera', 'Cada punto del lado opuesto traza una circunferencia a igual distancia, lo que da un cilindro.'),
        ('abc', 'Un triángulo rectángulo gira alrededor de uno de sus catetos. ¿Qué sólido genera?', 'Un cono', 'Un cilindro', 'Una pirámide', 'El otro cateto traza un círculo y la hipotenusa barre la superficie lateral de un cono.'),
        ('ab', 'Un semicírculo que gira alrededor de su diámetro genera:', 'Una esfera', 'Un cilindro', 'El arco del semicírculo traza todos los puntos a igual distancia del centro: una esfera.'),
        ('{F} ¿Cuál es el volumen del cilindro del caso A? Deja π.', '45π cm³', 'Se calcula π · 3² · 5.'),
        ('{F} ¿Cuál es el volumen del cono del caso B? Deja π.', '12π cm³', 'Se calcula 1/3 · π · 9 · 4, que da 12π.'),
        ('=', '{F} ¿Cuál es el coeficiente de π en el área lateral del cono del caso B? Usa π · r · g.', '3*5', 'El área lateral es π por el radio por la generatriz.', 'π cm²'),
        ('{F} ¿Cuál es el volumen de la esfera del caso C? Deja π.', '36π cm³', 'Se calcula 4/3 · π · 27 = 36π.'),
        ('abc', '{F} ¿Qué sólido genera el rectángulo del caso D, separado 1 cm del eje?', 'Un cilindro hueco de radio exterior 3 cm e interior 1 cm', 'Un cilindro macizo de radio 3 cm', 'Un cono de radio 3 cm', 'Al estar separado del eje, el giro deja un agujero de radio 1 cm en el centro.'),
        ('=', '{F} ¿Cuál es el coeficiente de π en el volumen del cilindro hueco del caso D? Usa π (R² − r²) h.', '(9-1)*5', 'Se resta el área del agujero a la del círculo exterior y se multiplica por la altura.', 'π cm³'),
        ('abc', 'Una estudiante dice que girar el triángulo de catetos 3 cm y 4 cm sobre cualquier cateto da el mismo volumen. ¿Qué caso la refuta?', 'Sobre el cateto de 4: 12π; sobre el cateto de 3: 16π', 'Sobre el cateto de 3 el volumen es 0', 'La hipotenusa cambia al girar', 'Con r = 4 y h = 3 el volumen es 1/3 · π · 16 · 3 = 16π, distinto de 12π.'),
        ('abc', 'Alguien dice que al girar un círculo completo sobre un diámetro se obtiene una esfera con el doble de volumen que con un semicírculo. ¿Qué responde?', 'Falso: el semicírculo ya barre toda la esfera y se obtiene la misma', 'Verdadero: hay el doble de superficie girando', 'Verdadero: la esfera queda con dos capas', 'La otra mitad del círculo reproduce los mismos puntos de la esfera, así que no agrega volumen.'),
        ('Un triángulo rectángulo de catetos 6 cm y 8 cm gira alrededor del cateto de 8 cm. ¿Cuál es el volumen del cono? Deja π.', '96π cm³', 'Con r = 6 y h = 8: 1/3 · π · 36 · 8 = 96π.'),
        ('Un cono tiene volumen 12π cm³ y radio 3 cm. ¿Cuánto mide su altura?', '4 cm', 'Se cumple 1/3 · π · 9 · h = 12π, es decir, 3h = 12 y h = 4.'),
    ],
    ctx=('=', 'Un trompo de madera tiene forma de cono generado por el triángulo de catetos 3 cm y 4 cm girado sobre el cateto de 4 cm. Su volumen es 12π cm³. Usa π ≈ 3 para estimar el volumen y, si 1 cm³ de madera pesa 1 g, ¿cuántos gramos pesa?', '12*3', 'Se reemplaza π por 3 en 12π y se multiplica por el peso de cada cm³.', ' g'),
    sc=[
        ("En Geometría 3D: ¿qué determina el radio del sólido de revolución?", "La distancia de la figura al eje", "Cada punto traza una circunferencia con ese radio."),
        ("¿Qué sólido genera un semicírculo girado sobre su diámetro?", "Una esfera", "El arco barre todos los puntos a igual distancia del centro."),
        ("¿Qué medida se usa en el área lateral del cono?", "La generatriz", "La superficie lateral es inclinada, no vertical."),
    ],
    op=("Elige un caso: (a) un rectángulo de 4 cm por 6 cm que gira sobre cada uno de sus dos lados: compara los volúmenes (deja π) y concluye si la conjetura «el eje no importa» es verdadera; (b) un triángulo rectángulo de catetos 9 cm y 12 cm (hipotenusa 15 cm) que gira sobre el cateto de 12 cm: calcula el volumen y el área lateral.",
        "Caso (a): sobre el lado de 6: r = 4 y h = 6, volumen 96π; sobre el lado de 4: r = 6 y h = 4, volumen 144π. Son distintos, así que la conjetura es falsa.",
        ["identifica eje, radio y altura", "calcula con las fórmulas", "concluye con base en los casos"],
        ["hoja con un esquema del giro y los cálculos"],
        ["no indicar cuál es el eje", "usar la altura en vez de la generatriz", "olvidar el cuadrado del radio"],
        "Pregunta: «¿qué lado quedó sobre el eje?». Si no responde, pídele que dibuje el eje."),
    reinforce="Dibuja un triángulo rectángulo y tres rectas distintas (cada cateto y la hipotenusa) y describe con palabras qué sólido imaginas al girar sobre cada una.",
    extend="Explica por qué un triángulo isósceles que gira sobre su altura genera un cono.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 3 (de ejemplo). Se estima el volumen de un cono de radio 4 cm y altura 4 cm apilando 4 discos (cilindros delgados) de 1 cm de altura. "
     "El radio del cono a cada altura sobre la base es 4 en la base, 3 a 1 cm, 2 a 2 cm, 1 a 3 cm y 0 en el vértice. "
     "Aproximación superior: cada disco usa el radio de su borde inferior (4, 3, 2, 1). Aproximación inferior: usa el radio de su borde superior (3, 2, 1, 0). "
     "El volumen de un disco es π · r² · 1. Se anota solo el número que acompaña a π.")
build(
    O4, 3, F,
    use="Aprenderé a aproximar el volumen de un sólido de revolución con discos, a acotarlo entre dos valores y a usar esas cotas para verificar o refutar una conjetura.",
    prior=["Sé calcular el volumen de un cilindro.", "Sé que el cono se genera al girar un triángulo rectángulo.", "Sé comparar un valor con una cota superior y una inferior."],
    explain=[
        "Cuando no se conoce una fórmula, se puede aproximar el volumen de un sólido de revolución cortándolo en discos delgados. Cada disco es un cilindro de altura pequeña y su volumen es π · r² por la altura. Si se elige para cada disco el radio mayor, la suma sobreestima el volumen y es una cota superior; si se elige el menor, subestima y es una cota inferior.",
        "El volumen real queda entre las dos cotas. Con discos más delgados las cotas se acercan entre sí. Esto sirve para verificar o refutar conjeturas: si una conjetura propone un valor mayor que la cota superior o menor que la inferior, esa conjetura es falsa, aunque no se conozca la fórmula exacta. En cambio, que un valor quede entre las cotas no prueba que sea el volumen, solo que es posible.",
        "Un buen argumento declara qué aproximación se usó, calcula con orden las sumas de r² y compara con la conjetura. Una hoja de cálculo repetiría estas sumas para muchos discos, pero no demuestra por sí sola una fórmula; solo permite acumular evidencia numérica que luego se respalda con un razonamiento general.",
    ],
    vocab=[("disco", "cilindro de altura pequeña usado para aproximar"), ("cota superior", "valor que seguro es mayor o igual que el volumen real"), ("cota inferior", "valor que seguro es menor o igual que el volumen real"), ("aproximación", "valor cercano al exacto"), ("acotar", "dar un valor mínimo y uno máximo"), ("evidencia numérica", "resultados de casos que apoyan una conjetura")],
    worked=[
        ("Acotar con tres discos", "Un cono de radio 6 cm y altura 6 cm se corta en 3 discos de 2 cm de altura. Los radios en los bordes son 6, 4, 2 y 0 (de la base al vértice). Halla las dos cotas.", ["Cota superior: π(36 + 16 + 4) · 2 = 112π.", "Cota inferior: π(16 + 4 + 0) · 2 = 40π."], "Entre 40π y 112π cm³"),
        ("Estimar con el promedio", "Usa las cotas del ejemplo anterior para estimar el volumen y compara con 72π, el valor que da la fórmula.", ["Promedio: (112π + 40π) ÷ 2 = 76π.", "La diferencia con 72π es 4π, pequeña frente a las cotas."], "La estimación 76π está cerca de 72π"),
    ],
    mistakes=[("Creer que la cota inferior es el volumen exacto.", "Una cota solo asegura un límite, no el valor.", "Escribe «el volumen está entre la cota inferior y la superior»."),
              ("Usar el mismo radio en las dos aproximaciones.", "La superior usa el radio mayor de cada disco y la inferior el menor.", "Distingue el borde inferior y el borde superior de cada disco.")],
    T=[
        ('abc', 'En una aproximación con discos, la cota superior usa:', 'El radio mayor de cada disco', 'El radio menor de cada disco', 'El promedio de los radios del cono', 'Si cada disco usa su radio mayor, el cilindro contiene al trozo de cono y sobreestima.'),
        ('abc', '{F} ¿Cuánto mide el radio del cono a 2 cm de la base?', '2 cm', '4 cm', '0 cm', 'La ficha indica que a 2 cm de la base el radio es 2.'),
        ('ab', 'Si se usan discos más delgados, las dos cotas:', 'Se acercan entre sí', 'Se alejan entre sí', 'Cada disco es más fino y se ajusta mejor al sólido, así que el intervalo se estrecha.'),
        ('=', '{F} ¿Cuál es la suma de r² de la aproximación superior (4, 3, 2, 1)? Es el coeficiente de π.', '16+9+4+1', 'Se elevan al cuadrado los radios y se suman.', 'π cm³'),
        ('=', '{F} ¿Cuál es la suma de r² de la aproximación inferior (3, 2, 1, 0)? Es el coeficiente de π.', '9+4+1+0', 'Se elevan al cuadrado los radios y se suman.', 'π cm³'),
        ('{F} ¿Cuál es el volumen del cono con la fórmula 1/3 · π · r² · h?', '64π/3 cm³', 'Se calcula 1/3 · π · 16 · 4 = 64π/3.'),
        ('abc', '{F} 64π/3 es un poco más de 21π. ¿Está el volumen real entre las dos cotas?', 'Sí: 14π < 64π/3 < 30π', 'No: 64π/3 es mayor que 30π', 'No: 64π/3 es menor que 14π', 'Las cotas son 14π y 30π, y 21 y un tercio queda entre 14 y 30.'),
        ('=', 'Un cono de radio 3 cm y altura 3 cm se aproxima con 3 discos de 1 cm; los radios del borde inferior son 3, 2 y 1. ¿Cuál es el coeficiente de π de la cota superior?', '9+4+1', 'Se suman los cuadrados de los radios de los bordes inferiores.', 'π cm³'),
        ('=', 'Para ese mismo cono, los radios del borde superior de los discos son 2, 1 y 0. ¿Cuál es el coeficiente de π de la cota inferior?', '4+1+0', 'Se suman los cuadrados de los radios de los bordes superiores.', 'π cm³'),
        ('abc', 'Alguien conjetura que el volumen del cono de la ficha es la mitad del cilindro de igual base y altura, es decir, 32π cm³. ¿Qué argumento la refuta?', 'La cota superior es 30π y 32π la supera', 'La cota inferior es 14π y 32π la supera', 'No se puede refutar con cotas', 'Si el volumen real es a lo más 30π, un valor de 32π no es posible.'),
        ('abc', 'Un estudiante dice: «mi cota inferior es 14π, entonces el volumen del cono es exactamente 14π». ¿Qué error comete?', 'Una cota inferior solo asegura que el volumen es al menos ese valor', 'Las cotas inferiores siempre son exactas', 'Debió calcular una cota superior, que es siempre exacta', 'La cota inferior es un mínimo; el volumen real es mayor que ella.'),
        ('Para el cono de radio 3 cm y altura 3 cm con 3 discos, las cotas son 14π y 5π. ¿Cuánto vale la diferencia entre la cota superior y la inferior?', '9π cm³', 'Se resta 14π − 5π y queda el volumen del disco de la base: π · 3² · 1.'),
        ('abc', 'Un cono de radio 2 cm y altura 2 cm se acota con 2 discos de 1 cm: cota superior 5π y cota inferior π. La conjetura «el volumen es 1/3 del cilindro de igual base y altura» da 8π/3. ¿Es consistente?', 'Sí: π < 8π/3 < 5π', 'No: 8π/3 supera 5π', 'No: 8π/3 es menor que π', 'Dos y dos tercios quedan entre 1 y 5, así que la conjetura no se contradice con las cotas.'),
    ],
    ctx=('abc', 'Un artista apila 5 discos de cartón de 1 cm de grosor, con radios 5, 4, 3, 2 y 1 cm, para modelar un cono. ¿Qué volumen de cartón usa en total?', '55π cm³', '15π cm³', '5π cm³', 'Se suman 25 + 16 + 9 + 4 + 1 = 55 y se multiplica por π y por el grosor 1.'),
    sc=[
        ("En Geometría 3D: ¿qué volumen tiene un disco de radio r y altura 1?", "π r²", "Es el volumen de un cilindro de altura 1."),
        ("¿Qué usa la cota superior en cada disco?", "El radio mayor", "Así cada disco contiene la parte del sólido que representa."),
        ("¿Basta que un valor esté entre las cotas para decir que es el volumen?", "No", "Solo es posible; las cotas no lo fijan."),
    ],
    op=("Elige un cono: (a) radio 6 cm y altura 6 cm con 2 discos de 3 cm (radios de los bordes: 6, 3, 0); (b) radio 4 cm y altura 4 cm con 2 discos de 2 cm (radios de los bordes: 4, 2, 0). Calcula las dos cotas, compara con 1/3 · π · r² · h y escribe si la conjetura «el volumen es la mitad del cilindro» es posible.",
        "Caso (b): cota superior π(16 + 4) · 2 = 40π; cota inferior π(4 + 0) · 2 = 8π; fórmula: 64π/3; la mitad del cilindro sería 32π, que queda entre 8π y 40π, así que las cotas por sí solas no la refutan y hay que usar discos más delgados.",
        ["calcula las dos cotas con orden", "compara con la fórmula", "concluye con base en las cotas"],
        ["hoja con las sumas, la comparación y la conclusión"],
        ["usar el mismo radio en las dos cotas", "olvidar multiplicar por la altura del disco", "decir que la cota es el volumen exacto"],
        "Pregunta: «¿qué radio usa cada disco?». Si responde igual en ambas, repasa borde inferior y superior."),
    reinforce="Dibuja un triángulo con 4 escalones bajo su borde para ver cómo se aproxima un área con rectángulos y piensa cómo sería con discos.",
    extend="Explica por qué usar discos más delgados mejora la aproximación.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (de ejemplo). Tabla de una hoja de cálculo imaginaria para cilindros de 2 cm de altura (generados al trasladar un círculo). Solo se anota el número que acompaña a π. "
     "Radio 1 cm: volumen 2, área lateral 4. Radio 2 cm: volumen 8, área lateral 8. Radio 3 cm: volumen 18, área lateral 12. Radio 4 cm: volumen 32, área lateral 16. "
     "Volumen = π · r² · h; área lateral = 2 · π · r · h. Conjetura A: «al duplicar el radio, el volumen se duplica». Conjetura B: «al duplicar el radio, el área lateral se duplica». Conjetura C: «el volumen siempre es mayor que el área lateral».")
build(
    O4, 4, F,
    use="Aprenderé a usar tablas y herramientas digitales para explorar conjeturas, a refutar con contraejemplos y a justificar con una razón general.",
    prior=["Sé calcular volumen y área lateral de un cilindro.", "Sé qué es una conjetura y un contraejemplo.", "Sé leer una tabla de valores."],
    explain=[
        "Una herramienta digital, como una hoja de cálculo o un programa de geometría dinámica, permite probar muchas medidas rápidamente. Con la tabla de la ficha se puede comparar cómo cambian el volumen y el área lateral cuando cambia el radio. Esa exploración sirve para formular conjeturas y para encontrar contraejemplos, pero no basta para demostrar que algo es siempre cierto.",
        "Para decidir una conjetura se cuentan los casos y se busca una razón general con las fórmulas. Como V = π r² h y el radio está al cuadrado, si el radio se multiplica por k, el volumen se multiplica por k². Como el área lateral es 2 π r h y el radio aparece una vez, si el radio se multiplica por k, el área lateral también se multiplica por k. La conjetura A es falsa y la B es verdadera para cualquier altura.",
        "Las conjeturas con «siempre» exigen cuidado: la conjetura C es verdadera para algunos radios y falsa para otros, así que es falsa como afirmación general. Una buena respuesta declara los casos probados, cita el contraejemplo o la razón general y deja claro el alcance de la herramienta, por ejemplo que solo se probaron radios de 1 a 4.",
    ],
    vocab=[("herramienta digital", "hoja de cálculo o programa de geometría dinámica"), ("evidencia numérica", "casos calculados que apoyan una conjetura"), ("razón general", "argumento que vale para todos los casos"), ("proporcional", "que se multiplica por el mismo factor que otra medida"), ("alcance", "hasta dónde llega lo que se comprobó"), ("contraejemplo", "caso que refuta una afirmación general")],
    worked=[
        ("Conjetura con razón general", "Conjetura: «al duplicar la altura, el volumen del cilindro se duplica». Con r = 1: h = 2 da 2π y h = 4 da 4π. ¿Es verdadera siempre?", ["V = π r² h es proporcional a h cuando r no cambia.", "Si h se multiplica por 2, V se multiplica por 2 para cualquier r."], "Verdadera: hay una razón general, no solo los dos casos"),
        ("Refutar con un caso", "Conjetura: «al duplicar el radio de un cono de altura 3 cm, su volumen se duplica». ¿Qué caso la refuta?", ["Con r = 1: V = 1/3 · π · 1 · 3 = π.", "Con r = 2: V = 1/3 · π · 4 · 3 = 4π, que es 4 veces mayor y no el doble."], "Falsa: el volumen se multiplica por 4"),
    ],
    mistakes=[("Concluir que una conjetura es siempre verdadera porque se cumplió en tres casos.", "Tres casos no prueban nada general.", "Busca un contraejemplo o una razón general con las fórmulas."),
              ("Decir que si el radio se duplica, todo se duplica.", "El volumen depende de r² y el área lateral de r.", "Revisa en cada fórmula cuántas veces aparece el radio.")],
    T=[
        ('abc', '{F} ¿Cuál es el volumen del cilindro de radio 3 cm?', '18π cm³', '12π cm³', '9π cm³', 'La tabla da 18 para el radio 3; 12 es el área lateral y 9 es r².'),
        ('abc', '{F} ¿Cuál es el área lateral del cilindro de radio 4 cm?', '16π cm²', '32π cm²', '8π cm²', 'La tabla da 16 para el área lateral con radio 4; 32 es el volumen.'),
        ('ab', '{F} Con los radios 1 y 2 de la tabla, la conjetura A resulta:', 'Falsa: el volumen pasa de 2π a 8π', 'Verdadera: el volumen pasa de 2π a 4π', 'El volumen se cuadruplica, y no se duplica.'),
        ('=', '{F} ¿Cuántas veces mayor es el volumen con radio 4 que con radio 2?', '32//8', 'Se dividen los valores de la tabla: 32 entre 8.', ' veces'),
        ('=', '{F} ¿Cuántas veces mayor es el área lateral con radio 4 que con radio 2?', '16//8', 'Se dividen los valores de la tabla: 16 entre 8.', ' veces'),
        ('{F} ¿Con qué radio, de los de la tabla, coinciden el volumen y el área lateral?', '2 cm', 'Con radio 2, el volumen y el área lateral valen 8 en la tabla.'),
        ('abc', '{F} ¿Qué se concluye de la conjetura C con la tabla?', 'Es falsa: con radio 1 el volumen 2π es menor que el área lateral 4π', 'Es verdadera: con radio 4 el volumen es mayor', 'Es verdadera porque se cumple en la mayoría de los casos', 'Un solo caso donde no se cumple basta para refutar una afirmación con «siempre».'),
        ('=', 'Un cilindro de altura 2 cm tiene radio 5 cm. ¿Cuál es el coeficiente de π de su volumen?', '5*5*2', 'Se calcula r² · h, que acompaña a π.', 'π cm³'),
        ('=', 'Para ese cilindro de radio 5 cm y altura 2 cm, ¿cuál es el coeficiente de π de su área lateral?', '2*5*2', 'Se calcula 2 · r · h, que acompaña a π.', 'π cm²'),
        ('abc', 'Una estudiante vio en la tabla que el área lateral se duplica al duplicar el radio en tres casos y concluye que siempre ocurre. ¿Qué le falta?', 'Una razón general: 2 π r h es proporcional a r', 'Probar con un cuarto caso, que lo demostraría', 'Nada: tres casos prueban la conjetura', 'La proporcionalidad con el radio explica por qué vale siempre; los casos solo la apoyan.'),
        ('abc', 'Una hoja de cálculo no encuentra contraejemplos al probar 20 radios distintos. ¿Qué se puede decir?', 'Hay evidencia que apoya la conjetura, pero no una prueba general', 'La conjetura queda demostrada para todos los radios', 'La conjetura es falsa', 'Probar casos entrega evidencia; una demostración necesita un argumento general.'),
        ('Si el radio de un cilindro se triplica y la altura no cambia, ¿por cuánto se multiplican el volumen y el área lateral?', 'Volumen por 9 y área lateral por 3', 'El volumen contiene r² (3 · 3) y el área lateral contiene r una sola vez.'),
        ('Si en un cilindro se duplican a la vez el radio y la altura, ¿por cuánto se multiplica el volumen?', 'Por 8', 'El volumen depende de r² · h, así que se multiplica por 2 · 2 · 2.'),
    ],
    ctx=('=', 'Una diseñadora compara dos tarros cilíndricos de 2 cm de altura: uno de radio 1 cm y otro de radio 4 cm. ¿Cuántas veces más contiene el segundo?', '32//2', 'Se dividen los volúmenes de la tabla, 32π entre 2π, y las π se simplifican.', ' veces'),
    sc=[
        ("En Geometría 3D: ¿cuántas veces aparece el radio en la fórmula del volumen del cilindro?", "Dos veces (r²)", "Por eso el volumen se multiplica por k² si el radio se multiplica por k."),
        ("¿Una tabla con muchos casos prueba una conjetura?", "No", "Solo entrega evidencia, no una demostración general."),
        ("¿Qué refuta una conjetura con «siempre»?", "Un contraejemplo", "Basta un caso donde no se cumple."),
    ],
    op=("Elige una conjetura sobre cilindros de 2 cm de altura: (a) «si el radio se triplica, el área lateral se triplica»; (b) «el volumen de un cilindro de radio 6 cm es más del doble del volumen de uno de radio 4 cm». Calcula casos con las fórmulas, decide si es verdadera o falsa y escribe una razón general o un contraejemplo. Declara el alcance de lo que comprobaste.",
        "Caso (a): radio 1: lateral 4π; radio 3: lateral 12π; es el triple. Razón general: 2 π r h es proporcional a r, así que triplicar r triplica el área lateral. Alcance: se probó con altura 2 cm, y la razón vale para cualquier altura.",
        ["calcula al menos dos casos", "da razón general o contraejemplo", "declara el alcance"],
        ["hoja con casos, conclusión y alcance"],
        ["concluir con un solo caso", "confundir r con r²", "no declarar el alcance"],
        "Pregunta: «¿cuántas veces aparece r?». Si no sabe, pídele que reescriba la fórmula."),
    reinforce="Elige un radio y una altura enteros y calcula cómo cambian el volumen y el área lateral al duplicar la altura.",
    extend="Explica por qué la conjetura «el volumen siempre es mayor que el área lateral» depende de las unidades y del tamaño del cilindro.",
)

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (de ejemplo). Un observador mira árboles de 6 m de altura a través de un plano de dibujo (un vidrio imaginario) ubicado a 2 m de su ojo. "
     "En la proyección central, la altura de la imagen es h′ = h · d ÷ D, con d = 2 m (distancia del plano) y D la distancia del objeto al ojo. "
     "Árbol A a 12 m, árbol B a 6 m y árbol C a 24 m. En la proyección paralela los rayos son paralelos entre sí, y los segmentos paralelos al plano conservan su longitud.")
build(
    O5, 1, F,
    use="Aprenderé a distinguir la proyección central de la paralela, a calcular tamaños aparentes y a decidir cuál conviene para un dibujo de arte, arquitectura o construcción.",
    prior=["Sé que dos figuras semejantes tienen razón de semejanza.", "Sé que la homotecia amplía o reduce desde un centro.", "Sé calcular proporciones simples."],
    explain=[
        "Una proyección lleva los puntos de un objeto a un plano de dibujo siguiendo rayos. En la proyección central (perspectiva) todos los rayos salen de un punto, el ojo del observador. Por eso el tamaño aparente disminuye con la distancia: con el plano a distancia d y el objeto a distancia D, la imagen mide h′ = h · d ÷ D. Las rectas paralelas que se alejan del observador parecen juntarse.",
        "En la proyección paralela los rayos son paralelos entre sí; es lo que se usa en planos de ingeniería, elevaciones y dibujos isométricos. Conserva el paralelismo y la razón entre segmentos paralelos, y los segmentos paralelos al plano de dibujo conservan su longitud; no hay efecto de «achicamiento por distancia». Por eso sirve para medir y construir, mientras que la central sirve para mostrar cómo se vería un objeto.",
        "Elegir proyección es una decisión de diseño: un mural o un cuadro que busca profundidad usa perspectiva central; un plano que se entrega a un taller para fabricar una pieza usa proyección paralela. Para argumentar una decisión se nombran el propósito, la propiedad que se necesita (medir o parecer real) y la proyección que la cumple.",
    ],
    vocab=[("proyección central", "rayos que salen de un punto: el ojo"), ("proyección paralela", "rayos paralelos entre sí"), ("plano de dibujo", "plano donde se dibuja la imagen"), ("tamaño aparente", "tamaño de la imagen en el plano de dibujo"), ("perspectiva", "representación que imita cómo se ve en profundidad"), ("razón entre distancias", "cociente entre dos distancias al ojo")],
    worked=[
        ("Altura aparente", "Un poste de 10 m está a 20 m del ojo y el plano de dibujo está a 2 m. ¿Cuánto mide su imagen?", ["Se usa h′ = h · d ÷ D = 10 · 2 ÷ 20.", "El cálculo da 20 ÷ 20 = 1."], "La imagen mide 1 m"),
        ("Elegir la proyección", "Un taller necesita fabricar una repisa y debe medir sus tablas sobre el plano. ¿Qué proyección le conviene?", ["Necesita conservar las longitudes de segmentos paralelos al plano.", "Eso lo cumple la proyección paralela y no la central."], "Proyección paralela"),
    ],
    mistakes=[("Pensar que en perspectiva las rectas paralelas dejan de serlo en la realidad.", "Solo parecen juntarse en la imagen; siguen paralelas.", "Distingue «cómo se ve» de «cómo es»."),
              ("Usar la distancia al plano en lugar de la distancia al objeto en h′ = h · d ÷ D.", "D es la distancia del objeto al ojo; d es la del plano.", "Rotula d y D antes de calcular.")],
    T=[
        ('abc', 'En la proyección central los rayos:', 'Salen de un punto, el ojo del observador', 'Son paralelos entre sí', 'Salen de cada punto del plano de dibujo', 'En la central todos los rayos convergen en el ojo; en la paralela no hay punto de convergencia.'),
        ('abc', 'La proyección paralela conserva:', 'El paralelismo y la razón de segmentos paralelos', 'El achicamiento con la distancia', 'La convergencia de las rectas paralelas', 'Con rayos paralelos, las rectas paralelas siguen paralelas en la imagen.'),
        ('ab', 'Si un objeto se aleja al doble de distancia del observador, su imagen en proyección central:', 'Se reduce a la mitad', 'Se duplica', 'La imagen depende de 1/D, así que al duplicar D la altura aparente se reduce a la mitad.'),
        ('=', '{F} ¿Cuántos metros mide la imagen del árbol A?', '6*2//12', 'Se calcula h · d ÷ D con h = 6, d = 2 y D = 12.', ' m'),
        ('=', '{F} ¿Cuántos metros mide la imagen del árbol B?', '6*2//6', 'Se calcula h · d ÷ D con D = 6.', ' m'),
        ('=', '{F} ¿Cuántos centímetros mide la imagen del árbol C?', '6*2*100//24', 'La imagen mide 6 · 2 ÷ 24 m, que son 50 cm.', ' cm'),
        ('abc', '{F} Según los datos, ¿qué árbol parece más alto en el plano de dibujo?', 'El B, porque es el más cercano', 'El C, porque está más lejos', 'El A, porque tiene altura 6 m', 'Los tres miden igual, y la imagen es mayor cuanto menor sea la distancia al ojo.'),
        ('=', 'Una torre de 30 m está a 60 m del ojo y el plano de dibujo está a 2 m. ¿Cuántos metros mide su imagen?', '30*2//60', 'Se usa h · d ÷ D con los datos dados.', ' m'),
        ('abc', 'Un dibujo de una caja con todas sus aristas paralelas dibujadas también paralelas corresponde a una:', 'Proyección paralela', 'Proyección central, porque las aristas se achican con la distancia', 'Proyección central, porque las aristas parecen juntarse', 'Si los rayos son paralelos, las aristas paralelas se dibujan paralelas.'),
        ('abc', 'Una estudiante dice: «en la foto las vías del tren se juntan, así que dejan de ser paralelas». ¿Qué argumento corresponde?', 'En perspectiva central las paralelas parecen converger; los rieles siguen paralelos en la realidad', 'Tiene razón: las vías se juntan de verdad', 'La proyección central siempre cambia el ancho real', 'El efecto de convergencia es de la imagen y no cambia la separación real.'),
        ('abc', 'Un ingeniero quiere medir con regla en el plano la longitud real de piezas paralelas al plano de dibujo. ¿Qué proyección le conviene?', 'Paralela, porque conserva la longitud de esos segmentos', 'Central, porque achica lo lejano', 'Cualquiera: no hay diferencia', 'La paralela conserva esas longitudes, mientras que la central las modifica según la distancia.'),
        ('El plano de dibujo está a 2 m del ojo. Un poste de 5 m tiene una imagen de 1 m. ¿A qué distancia del ojo está el poste?', '10 m', 'Se cumple 1 = 5 · 2 ÷ D, así que D = 10.'),
        ('Dos postes iguales se miran con proyección central. La imagen del primero es el triple de la del segundo. Si el primero está a 8 m, ¿a qué distancia está el segundo?', '24 m', 'La imagen es inversamente proporcional a la distancia, así que el segundo está 3 veces más lejos.'),
    ],
    ctx=('abc', 'Una pintora quiere que un pasillo pintado en un muro parezca profundo. ¿Qué decisión de proyección es la más adecuada?', 'Usar perspectiva central, con líneas que convergen y objetos más pequeños al fondo', 'Usar proyección paralela, para que todas las líneas se mantengan paralelas', 'Dibujar todos los objetos del mismo tamaño', 'La perspectiva central reproduce la profundidad con convergencia y reducción de tamaño.'),
    sc=[
        ("En Geometría 3D: ¿de dónde salen los rayos en la proyección central?", "Del ojo del observador", "Es el punto desde el que se mira."),
        ("¿Qué proyección se usa para medir piezas en un plano de taller?", "La paralela", "Conserva las longitudes paralelas al plano de dibujo."),
        ("¿Qué pasa con el tamaño aparente cuando la distancia se duplica?", "Se reduce a la mitad", "La imagen es inversamente proporcional a la distancia."),
    ],
    op=("Elige un encargo: (a) un cartel de bienvenida con una calle que se aleja, para el que debes justificar la proyección y calcular la imagen de un poste de 4 m a 16 m del ojo con el plano a 2 m; (b) un plano para fabricar un banco, para el que debes justificar la proyección. Escribe la decisión, la propiedad que la sustenta y el cálculo si lo hay.",
        "Caso (a): la proyección es central porque se busca profundidad. La imagen del poste es h · d ÷ D = 4 · 2 ÷ 16 = 1/2 m, es decir, 50 cm; el poste de fondo se ve más pequeño que uno cercano.",
        ["nombra la proyección elegida", "relaciona con la propiedad que necesita", "calcula con h · d ÷ D si corresponde"],
        ["hoja con la decisión, la justificación y el cálculo"],
        ["confundir d con D", "elegir sin justificar", "decir que la central conserva las medidas"],
        "Pregunta: «¿qué necesitas, parecer real o medir?». La respuesta decide la proyección."),
    reinforce="Mira desde una ventana una fila de postes o de árboles y describe con tus palabras qué pasa con su tamaño aparente a medida que se alejan.",
    extend="Explica por qué la homotecia de la clase de isometrías y homotecias se parece a la proyección central.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (de ejemplo). Modelo de la perspectiva: el ojo está en el origen O(0, 0, 0) y mira hacia +y; el plano de dibujo es y = 1; x es derecha y z es arriba (en metros). "
     "Un punto (x, y, z) con y > 0 se dibuja en el punto (x ÷ y, z ÷ y) del plano. "
     "El punto de fuga de la dirección (a, b, c) con b distinto de 0 es (a ÷ b, c ÷ b). La línea del horizonte es la recta z′ = 0, a la altura del ojo.")
build(
    O5, 2, F,
    use="Aprenderé a calcular la imagen de puntos en perspectiva, a hallar puntos de fuga y la línea del horizonte, y a argumentar por qué las paralelas convergen.",
    prior=["Sé que la proyección central achica con la distancia.", "Sé usar coordenadas (x, y, z).", "Sé calcular divisiones simples de enteros."],
    explain=[
        "En el modelo de la ficha, el ojo mira hacia adelante (eje y) y el plano de dibujo está a 1 m. Un punto (x, y, z) se dibuja en (x ÷ y, z ÷ y): cuanto mayor es y (más lejos), más cerca del centro del dibujo cae. Dos puntos sobre el mismo rayo que sale del ojo tienen la misma imagen. Los puntos con y = 0 o con y negativo no se dibujan en este modelo, porque quedan al lado del ojo o detrás de él.",
        "Una recta con dirección (a, b, c) y b distinto de 0 se acerca a un punto límite en el dibujo: su punto de fuga (a ÷ b, c ÷ b). Todas las rectas paralelas con esa dirección comparten el mismo punto de fuga, que es la razón de que parezcan converger. Las direcciones horizontales tienen c = 0, y su punto de fuga está sobre la línea del horizonte z′ = 0. Si b = 0, la recta es paralela al plano de dibujo, no tiene punto de fuga y se dibuja con la misma dirección.",
        "Para argumentar, se calcula primero la imagen de dos o tres puntos de la recta y se comprueba que se acercan al punto de fuga. El modelo supone un ojo fijo y un plano de dibujo plano, y no recoge la distorsión de una lente real. Una herramienta digital mostraría la escena girando, pero los valores se justifican con la fórmula.",
    ],
    vocab=[("punto de fuga", "punto del dibujo donde convergen las rectas paralelas de una dirección"), ("línea del horizonte", "recta del dibujo a la altura del ojo"), ("plano de dibujo", "plano y = 1 donde se dibuja la imagen"), ("rayo", "recta que une el ojo con un punto del objeto"), ("dirección", "vector que indica hacia dónde va una recta"), ("convergencia", "acercamiento de rectas a un mismo punto")],
    worked=[
        ("Imagen de un punto", "Calcula la imagen del punto (6, 3, 9).", ["La coordenada horizontal es 6 ÷ 3 = 2.", "La coordenada vertical es 9 ÷ 3 = 3."], "La imagen es (2, 3)"),
        ("Punto de fuga", "Halla el punto de fuga de las rectas con dirección (4, 2, 0).", ["Se calcula (4 ÷ 2, 0 ÷ 2).", "Queda (2, 0), sobre el horizonte porque la dirección es horizontal."], "El punto de fuga es (2, 0)"),
    ],
    mistakes=[("Calcular la imagen con (x · y, z · y) o con (y ÷ x, y ÷ z).", "La imagen divide por la distancia y, que es la profundidad.", "Escribe «x ÷ y» y «z ÷ y» antes de reemplazar."),
              ("Decir que cualquier dirección tiene punto de fuga.", "Si b = 0 la recta es paralela al plano de dibujo y sigue paralela.", "Revisa b antes de calcular (a ÷ b, c ÷ b).")],
    T=[
        ('abc', '{F} ¿Cuál es la imagen del punto (4, 2, 4)?', '(2, 2)', '(8, 8)', '(4, 4)', 'Se divide por la profundidad y = 2: 4 ÷ 2 y 4 ÷ 2; (8, 8) multiplica y (4, 4) divide por 1.'),
        ('abc', '{F} ¿Cuál es la imagen del punto (6, 3, 12)?', '(2, 4)', '(18, 36)', '(2, 3)', 'Con y = 3 se calcula 6 ÷ 3 y 12 ÷ 3; (2, 3) divide la z por 4 por error.'),
        ('ab', 'En el modelo de la ficha, cuando un punto se aleja (y aumenta), su imagen:', 'Se acerca al centro (0, 0)', 'Se aleja del centro (0, 0)', 'Se divide por un y mayor, por lo que las coordenadas de la imagen son cada vez menores.'),
        ('{F} ¿Cuál es el punto de fuga de la dirección (0, 1, 0)?', '(0, 0)', 'Se calcula (0 ÷ 1, 0 ÷ 1).'),
        ('{F} ¿Cuál es el punto de fuga de la dirección (2, 1, 1)?', '(2, 1)', 'Se calcula (2 ÷ 1, 1 ÷ 1).'),
        ('{F} ¿Cuál es el punto de fuga de la dirección (−3, 1, 0)?', '(−3, 0)', 'Se calcula (−3 ÷ 1, 0 ÷ 1).'),
        ('=', '{F} ¿Cuál es la primera coordenada de la imagen del punto (12, 6, 18)?', '12//6', 'Se divide la coordenada x por la profundidad y.'),
        ('abc', 'Las direcciones horizontales tienen c = 0. ¿Dónde caen sus puntos de fuga?', 'Sobre la línea del horizonte z′ = 0', 'Sobre el eje vertical x′ = 0', 'En cualquier parte del dibujo', 'Con c = 0, la segunda coordenada (c ÷ b) es 0, es decir, la altura del ojo.'),
        ('abc', 'La dirección (1, 0, 0) es paralela al plano de dibujo (b = 0). ¿Tiene punto de fuga?', 'No: sus rectas se dibujan paralelas', 'Sí, en (1, 0)', 'Sí, en (0, 0)', 'No se puede dividir por b = 0, y esas rectas no convergen en la imagen.'),
        ('abc', 'Los puntos (4, 2, 4) y (8, 4, 8) tienen la misma imagen (2, 2). ¿Por qué?', 'Están sobre el mismo rayo que sale del ojo', 'Porque están a la misma distancia del ojo', 'Porque son simétricos respecto del plano de dibujo', 'El segundo es el doble del primero en cada coordenada, así que están alineados con el ojo.'),
        ('abc', 'Un dibujante marca el punto de fuga de la dirección (2, 1, 0) como (1, 2). ¿Qué error cometió?', 'Invirtió los cocientes: debe ser (a ÷ b, c ÷ b) = (2, 0)', 'No hay error, es correcto', 'Debió usar (b ÷ a, c ÷ a)', 'La fórmula divide por b: 2 ÷ 1 y 0 ÷ 1, que da (2, 0).'),
        ('La recta que pasa por (2, 2, 2) con dirección (1, 1, 0) tiene punto de fuga (1, 0). ¿Cuál es la imagen de su punto con t = 2, es decir, (4, 4, 2)?', '(1, 1/2)', 'Se calcula (4 ÷ 4, 2 ÷ 4) y se acerca al punto de fuga (1, 0) al alejarse.'),
        ('Dos postes verticales de 4 m, uno con base en y = 2 y otro en y = 4, se dibujan con el modelo de la ficha. ¿Cuántas veces mayor es la altura aparente del primero respecto del segundo?', '2 veces', 'Las alturas aparentes son 4 ÷ 2 = 2 y 4 ÷ 4 = 1.'),
    ],
    ctx=('abc', 'Una ilustradora dibuja un pasillo en que las líneas de las baldosas y del techo siguen la dirección (0, 1, 0). ¿Dónde se juntan esas líneas en el dibujo?', 'En el punto (0, 0)', 'En el punto (1, 0)', 'No se juntan en ningún punto', 'El punto de fuga de (0, 1, 0) es (0 ÷ 1, 0 ÷ 1) = (0, 0).'),
    sc=[
        ("En Geometría 3D: ¿qué fórmula da el punto de fuga de la dirección (a, b, c)?", "(a ÷ b, c ÷ b)", "Se divide por la componente de profundidad b."),
        ("¿Dónde caen los puntos de fuga de direcciones horizontales?", "Sobre la línea del horizonte", "La altura de la imagen es 0."),
        ("¿Qué pasa si b = 0?", "La recta no tiene punto de fuga", "Es paralela al plano de dibujo."),
    ],
    op=("Elige un caso: (a) una vereda recta con dirección (3, 1, 0) y dos puntos suyos, (3, 1, −1) y (9, 3, −1): calcula sus imágenes y el punto de fuga; (b) un riel con dirección (−2, 1, 0) y puntos (−2, 1, −1) y (−6, 3, −1). Comprueba si las imágenes se acercan al punto de fuga y explica por qué parecen converger.",
        "Caso (a): imágenes (3, −1) y (3, −1/3); punto de fuga (3, 0). El segundo punto está más cerca del punto de fuga, lo que muestra la convergencia aunque la vereda sea recta y de ancho constante.",
        ["calcula imágenes con x ÷ y y z ÷ y", "calcula el punto de fuga", "explica la convergencia"],
        ["hoja con cálculos, un dibujo esquemático y la explicación"],
        ["invertir los cocientes", "calcular punto de fuga con b = 0", "decir que las rectas dejan de ser paralelas"],
        "Pregunta: «¿por cuál número dividiste?». Si no es la profundidad y, pídele que la ubique."),
    reinforce="En una hoja, marca un punto de fuga en el centro y dibuja cuatro líneas que salen de él como si fueran los bordes de un pasillo.",
    extend="Explica por qué todos los puntos de fuga de direcciones horizontales están a la misma altura en el dibujo.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (de ejemplo). Mismo modelo de la clase anterior: ojo en O(0, 0, 0) mirando hacia +y, plano y = 1, imagen (x ÷ y, z ÷ y). "
     "Un edificio con forma de caja se ve girado 45°: sus aristas horizontales tienen direcciones (1, 1, 0) y (−1, 1, 0), y las verticales (0, 0, 1). "
     "Arista vertical cercana: de B1(0, 8, −8) a T1(0, 8, 8). Esquina vecina a la derecha: B2 = B1 + 8 · (1, 1, 0) = (8, 16, −8).")
build(
    O5, 3, F,
    use="Aprenderé a construir una perspectiva con dos puntos de fuga, a comprobar la construcción con coordenadas y a explicar cuándo hacen falta tres puntos de fuga.",
    prior=["Sé calcular la imagen de un punto y un punto de fuga.", "Sé que las direcciones horizontales tienen su punto de fuga en el horizonte.", "Sé reconocer rectas alineadas."],
    explain=[
        "Cuando una caja se ve de esquina, sus aristas horizontales siguen dos direcciones distintas y cada dirección tiene su propio punto de fuga, ambos sobre la línea del horizonte. Las aristas verticales, que son paralelas al plano de dibujo, se dibujan verticales: este es el dibujo en perspectiva con dos puntos de fuga. Con el modelo de la ficha, los puntos de fuga de las direcciones (1, 1, 0) y (−1, 1, 0) son (1, 0) y (−1, 0).",
        "Un orden de trabajo ayuda: primero se traza el horizonte y se ubican los dos puntos de fuga; luego se dibuja la arista vertical más cercana; después se trazan desde sus extremos líneas hacia cada punto de fuga; por último se cierran las otras aristas verticales. Una arista más lejana aparece más corta: si está al doble de distancia, mide la mitad. Para comprobar una construcción se verifica que las imágenes de los vértices caigan sobre las rectas hacia los puntos de fuga.",
        "Si el observador mira hacia arriba o hacia abajo, las verticales también convergen y se necesitan tres puntos de fuga, como en la vista de un rascacielos desde la calle. La perspectiva de dos puntos supone que el plano de dibujo es vertical, y una herramienta digital permitiría variar la mirada, pero cada paso se justifica con cálculos de coordenadas.",
    ],
    vocab=[("perspectiva de dos puntos", "dibujo con dos puntos de fuga sobre el horizonte"), ("arista vertical", "arista paralela al eje z, que se dibuja vertical"), ("línea hacia el punto de fuga", "recta de construcción que une un vértice con el punto de fuga"), ("tres puntos de fuga", "perspectiva con verticales convergentes"), ("alineados", "sobre una misma recta"), ("construcción", "pasos del dibujo con reglas")],
    worked=[
        ("Esquina opuesta", "Calcula la imagen de B3 = B1 + 8 · (−1, 1, 0) = (−8, 16, −8).", ["La coordenada horizontal es −8 ÷ 16 = −1/2.", "La coordenada vertical es −8 ÷ 16 = −1/2."], "La imagen es (−1/2, −1/2)"),
        ("Comprobación de alineación", "La imagen de B1 es (0, −1) y el punto de fuga de (−1, 1, 0) es (−1, 0). ¿Está (−1/2, −1/2) en la recta entre ellos?", ["La recta por (0, −1) y (−1, 0) es z′ = −x′ − 1.", "Con x′ = −1/2 resulta z′ = 1/2 − 1 = −1/2: coincide."], "Sí, están alineados"),
    ],
    mistakes=[("Dibujar las aristas verticales inclinadas hacia un punto de fuga en un dibujo de dos puntos.", "En dos puntos las verticales son paralelas al plano de dibujo y se dibujan verticales.", "Solo las aristas horizontales van hacia los puntos de fuga."),
              ("Poner los puntos de fuga a alturas distintas.", "Las direcciones horizontales tienen su punto de fuga en el horizonte.", "Ubica ambos sobre la misma línea horizontal, a la altura del ojo.")],
    T=[
        ('abc', '{F} ¿Cuál es el punto de fuga de la dirección (1, 1, 0)?', '(1, 0)', '(0, 1)', '(1, 1)', 'Se calcula (1 ÷ 1, 0 ÷ 1); (1, 1) olvida que c = 0 y (0, 1) intercambia las coordenadas.'),
        ('abc', '{F} ¿Cuál es el punto de fuga de la dirección (−1, 1, 0)?', '(−1, 0)', '(1, 0)', '(0, −1)', 'Se calcula (−1 ÷ 1, 0 ÷ 1), es decir, el simétrico del otro punto de fuga.'),
        ('ab', 'En perspectiva de dos puntos, las aristas verticales se dibujan:', 'Verticales', 'Convergiendo hacia un tercer punto', 'Las verticales son paralelas al plano de dibujo y no convergen.'),
        ('{F} ¿Cuál es la imagen de B1(0, 8, −8)?', '(0, −1)', 'Se calcula (0 ÷ 8, −8 ÷ 8).'),
        ('{F} ¿Cuál es la imagen de T1(0, 8, 8)?', '(0, 1)', 'Se calcula (0 ÷ 8, 8 ÷ 8).'),
        ('{F} ¿Cuál es la imagen de B2 = (8, 16, −8)?', '(1/2, −1/2)', 'Se calcula (8 ÷ 16, −8 ÷ 16).'),
        ('=', 'La arista vertical cercana mide 16 m de altura y está a y = 8 m. ¿Cuántos metros mide su imagen en el plano de dibujo?', '16//8', 'La altura aparente es la altura real dividida por la profundidad.', ' m'),
        ('abc', '{F} La arista vertical lejana, que sube de B2 a (8, 16, 8), está a y = 16. Comparada con la cercana, su altura aparente es:', 'La mitad', 'El doble', 'La misma', 'La distancia se duplicó (de 8 a 16), así que la altura aparente se reduce a la mitad.'),
        ('abc', '{F} La imagen de B1 es (0, −1) y la de B2 es (1/2, −1/2). ¿Están alineadas con el punto de fuga (1, 0)?', 'Sí: están sobre la recta z′ = x′ − 1', 'No: ninguna cae sobre esa recta', 'Solo B1 está alineada', 'Con x′ = 0 resulta −1 y con x′ = 1/2 resulta −1/2, que coinciden con las imágenes.'),
        ('abc', 'Una dibujante coloca el primer punto de fuga a la altura del ojo y el segundo un poco más arriba. ¿Qué error comete?', 'Ambos deben estar sobre el horizonte, a la altura del ojo', 'No hay error, pueden estar a cualquier altura', 'El segundo debe estar más abajo', 'Las dos direcciones son horizontales, así que sus puntos de fuga tienen z′ = 0.'),
        ('abc', 'Alguien dibuja un rascacielos mirando hacia arriba desde la calle y las aristas verticales se ven convergentes. ¿Cuántos puntos de fuga necesita?', 'Tres', 'Dos', 'Uno', 'Las dos direcciones horizontales aportan dos puntos y las verticales convergentes aportan un tercero.'),
        ('Un camino horizontal con dirección (2, 1, 0) pasa por (0, 2, −2). ¿Cuál es su punto de fuga y qué imagen tiene su punto con t = 2, es decir, (4, 4, −2)?', 'Punto de fuga (2, 0); imagen (1, −1/2)', 'Se calcula (2 ÷ 1, 0 ÷ 1) para el punto de fuga y (4 ÷ 4, −2 ÷ 4) para la imagen.'),
        ('Dos postes verticales iguales están a y = 8 e y = 24. ¿Cuántas veces mayor es la altura aparente del primero?', '3 veces', 'La altura aparente es inversamente proporcional a la profundidad: 24 ÷ 8 = 3.'),
    ],
    ctx=('abc', 'Una ilustradora va a dibujar una casa de esquina en perspectiva de dos puntos. ¿Cuál es un orden correcto de trabajo?', 'Horizonte, dos puntos de fuga, arista vertical cercana, líneas hacia los puntos de fuga', 'Arista vertical, techo, horizonte, puntos de fuga', 'Puntos de fuga inclinados, horizonte, aristas', 'Primero se fija la referencia (horizonte y puntos de fuga) y luego se construye la arista cercana y las líneas.'),
    sc=[
        ("En Geometría 3D: ¿cuántos puntos de fuga tiene un dibujo con una caja vista de esquina?", "Dos", "Uno por cada dirección horizontal de aristas."),
        ("¿Cómo se dibujan las aristas verticales en la perspectiva de dos puntos?", "Verticales", "Son paralelas al plano de dibujo."),
        ("¿Dónde se ubican los puntos de fuga de direcciones horizontales?", "Sobre el horizonte", "Están a la altura del ojo."),
    ],
    op=("Elige un caso: (a) una caja vista de esquina con vértice cercano B1(0, 4, −4) y esquina vecina B1 + 4 · (1, 1, 0) = (4, 8, −4): calcula las imágenes de ambos y comprueba que están alineadas con el punto de fuga (1, 0); (b) un edificio de aristas con dirección (2, 1, 0) y (−2, 1, 0): calcula sus puntos de fuga y explica el orden de construcción en papel.",
        "Caso (a): imagen de B1 es (0, −1); imagen de (4, 8, −4) es (1/2, −1/2). Ambas satisfacen z′ = x′ − 1, la recta que va al punto de fuga (1, 0). Por eso la construcción es consistente.",
        ["calcula imágenes y puntos de fuga", "verifica la alineación", "explica el orden de construcción"],
        ["hoja con cálculos y un esquema con horizonte y puntos de fuga"],
        ["inclinar las aristas verticales", "poner los puntos de fuga a alturas distintas", "no comprobar la alineación"],
        "Pregunta: «¿dónde está el horizonte en tu dibujo?». Si no lo marcó, pídele que lo trace primero."),
    reinforce="Dibuja una caja en perspectiva de dos puntos con papel cuadriculado, un horizonte horizontal y dos puntos de fuga a ambos lados.",
    extend="Explica por qué en una perspectiva de dos puntos los lados de la caja que van hacia un mismo punto de fuga son paralelos en la realidad.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (de ejemplo). Casa con forma de caja y techo a dos aguas, en proyección paralela (elevaciones y planta). Medidas reales: ancho de la fachada 8 m, fondo 6 m, altura de los muros 3 m y altura del caballete (punto más alto del techo) 6 m sobre el suelo. "
     "Plano en escala 1:50: 1 cm en el plano son 50 cm reales. La elevación frontal es la vista de la fachada; la planta es la vista desde arriba. "
     "El techo sube 3 m a lo largo de 4 m horizontales (la mitad del ancho), así que cada agua inclinada mide 5 m.")
build(
    O5, 4, F,
    use="Aprenderé a leer y dibujar plantas y elevaciones a escala, a calcular medidas reales y áreas, y a comprobar que las vistas son coherentes entre sí.",
    prior=["Sé que la proyección paralela conserva medidas de segmentos paralelos al plano.", "Sé calcular áreas de rectángulos y triángulos.", "Sé convertir entre metros y centímetros."],
    explain=[
        "Los planos de arquitectura y construcción usan proyección paralela: la planta muestra el objeto visto desde arriba y las elevaciones (frontal, lateral y posterior) lo muestran visto de frente o de lado. Cada una conserva las medidas de lo que es paralelo a su plano, y por eso se puede medir directamente. La escala 1:50 es una razón de homotecia: cada medida del plano se multiplica por 50 para obtener la real.",
        "Con la escala se convierten longitudes: 8 m reales son 800 cm, que en el plano miden 800 ÷ 50 = 16 cm. Las áreas se multiplican por el cuadrado de la razón: 1 cm² en el plano son 50 · 50 = 2.500 cm² reales. La pendiente de un techo es lo que sube dividido por lo que avanza en horizontal; aquí 3 m en 4 m, es decir, 3/4. La longitud inclinada de un agua se halla con Pitágoras, y en este caso mide 5 m.",
        "Para argumentar que un plano es coherente se comparan las vistas: el ancho de la fachada debe ser el mismo en la planta y en la elevación frontal, y el fondo debe coincidir entre la planta y la elevación lateral. Una herramienta digital puede generar las vistas, pero un error de datos se detecta comparando medidas y revisando que la escala se haya aplicado igual en todas.",
    ],
    vocab=[("planta", "vista del objeto desde arriba"), ("elevación", "vista del objeto de frente o de lado"), ("escala", "razón entre una medida del plano y la real"), ("caballete", "punto más alto de un techo a dos aguas"), ("pendiente", "lo que sube dividido por lo que avanza en horizontal"), ("coherencia entre vistas", "las mismas medidas aparecen iguales en todas las vistas")],
    worked=[
        ("Convertir con la escala", "En un plano a escala 1:100, el ancho de una pieza mide 6 cm. ¿Cuánto mide en la realidad?", ["Se multiplica por 100: 6 · 100 = 600 cm.", "Se pasa a metros: 600 cm son 6 m."], "6 m reales"),
        ("Coherencia entre vistas", "En escala 1:25, la elevación frontal de una repisa mide 20 cm de ancho. ¿Cuánto debe medir ese ancho en la planta, y cuánto mide en la realidad?", ["Ambas vistas muestran el mismo ancho, así que la planta también debe medir 20 cm.", "En la realidad: 20 · 25 = 500 cm = 5 m."], "20 cm en la planta y 5 m reales"),
    ],
    mistakes=[("Multiplicar las áreas del plano por la razón de escala en lugar de por su cuadrado.", "El área depende de dos longitudes.", "Para áreas usa 50² en la escala 1:50."),
              ("Mezclar el ancho y el fondo entre la planta y la elevación.", "La elevación frontal muestra el ancho y la altura; el fondo se ve en la lateral.", "Rotula cada medida con su vista antes de dibujar.")],
    T=[
        ('abc', '¿Qué muestra una planta?', 'El objeto visto desde arriba', 'La fachada vista de frente', 'El objeto cortado por la mitad', 'La planta es la proyección del objeto sobre un plano horizontal, mirando desde arriba.'),
        ('abc', 'Una elevación frontal muestra:', 'La fachada vista de frente', 'El objeto visto desde arriba', 'El objeto visto desde un punto de fuga', 'Es la proyección sobre un plano vertical frente al objeto.'),
        ('ab', 'La escala 1:50 significa que:', '1 cm del plano equivale a 50 cm reales', '50 cm del plano equivalen a 1 cm real', 'La razón 1:50 compara una medida del plano con la medida real, que es 50 veces mayor.'),
        ('=', '{F} ¿Cuántos centímetros mide en el plano el ancho de la fachada (8 m)?', '800//50', 'Se pasa a centímetros, 800, y se divide por la razón 50.', ' cm'),
        ('=', '{F} ¿Cuántos centímetros mide en la planta el fondo de la casa (6 m)?', '600//50', 'Se pasa a centímetros y se divide por 50.', ' cm'),
        ('=', '{F} ¿Cuántos centímetros mide en la elevación la altura de los muros (3 m)?', '300//50', 'La altura real de 300 cm se divide por 50.', ' cm'),
        ('=', '{F} La fachada tiene un rectángulo de 8 m por 3 m y encima un triángulo de base 8 m y altura 3 m. ¿Cuál es su área real?', '8*3+8*3//2', 'Se suman el área del rectángulo y la del triángulo.', ' m²'),
        ('=', '{F} ¿Cuál es el área real de la planta de la casa, de 8 m por 6 m?', '8*6', 'La planta es un rectángulo de ancho por fondo.', ' m²'),
        ('{F} ¿Cuál es la pendiente del techo, como fracción?', '3/4', 'El techo sube 3 m y avanza 4 m en horizontal.'),
        ('abc', 'Una estudiante afirma que, en escala 1:50, 1 cm² del plano equivale a 50 cm² reales. ¿Cuál es el error?', 'Las áreas se multiplican por 50² = 2.500: 1 cm² son 2.500 cm²', 'No hay error: el área sigue la misma razón', 'Las áreas se dividen por 50', 'El área depende de dos longitudes, y cada una se multiplica por 50.'),
        ('abc', 'Un dibujante representó en la planta 12 cm de ancho y 16 cm de fondo, pero la fachada mide 16 cm de ancho en la elevación (misma escala). ¿Qué error cometió?', 'Intercambió el ancho y el fondo en la planta', 'No hay error', 'Usó otra escala en la elevación', 'El ancho debe ser 16 cm en ambas vistas y el fondo 12 cm en la planta.'),
        ('=', '{F} Cada agua del techo es un rectángulo de 5 m de largo inclinado por 6 m de fondo, y hay dos aguas. ¿Cuál es el área real del techo?', '2*5*6', 'Se multiplica el número de aguas por el largo inclinado y por el fondo.', ' m²'),
        ('=', 'Una lámina de zinc cuesta $8.000 por m² y el techo de la casa tiene 60 m². ¿Cuánto cuesta cubrirlo en pesos?', '60*8000', 'Se multiplica el área del techo por el precio de cada m².'),
    ],
    ctx=('abc', 'Una dibujante tiene una elevación hecha a escala 1:100 y debe pasarla a escala 1:50 para presentarla más grande. ¿Qué debe hacer?', 'Duplicar todas las medidas del dibujo', 'Dividir todas las medidas por 2', 'Sumar 50 a cada medida', 'Pasar de 1:100 a 1:50 es una homotecia de razón 2: cada longitud del dibujo se multiplica por 2.'),
    sc=[
        ("En Geometría 3D: ¿qué vista muestra la planta?", "La vista desde arriba", "Es la proyección sobre un plano horizontal."),
        ("¿Por cuánto se multiplican las áreas en la escala 1:50?", "Por 2.500", "Es 50 al cuadrado, porque el área usa dos longitudes."),
        ("¿Qué debe coincidir entre la planta y la elevación frontal?", "El ancho de la fachada", "Es la misma medida vista desde dos planos."),
    ],
    op=("Elige un encargo: (a) una caseta con forma de caja de 4 m de ancho, 3 m de fondo y 2 m de alto, para dibujar en escala 1:50 su planta y su elevación frontal; (b) una bodega con techo a dos aguas de 6 m de ancho, 5 m de fondo, muros de 3 m y caballete a 5 m (cada agua sube 2 m en 3 m), para calcular las medidas en el plano a escala 1:50 y el área de la fachada. Escribe las medidas en cm y comprueba que las vistas son coherentes.",
        "Caso (a): planta de 8 cm por 6 cm; elevación frontal de 8 cm por 4 cm; el ancho de 8 cm coincide en ambas vistas. Áreas reales: planta 12 m² y fachada 8 m².",
        ["convierte con la escala", "dibuja o describe las vistas con medidas", "comprueba la coherencia entre vistas"],
        ["hoja con las medidas en cm, el esquema de las vistas y la comprobación"],
        ["multiplicar en vez de dividir al pasar al plano", "mezclar ancho y fondo", "olvidar convertir metros a centímetros"],
        "Pregunta: «¿qué medida compartes entre planta y elevación?». Si no la ubica, pídele que subraye el ancho."),
    reinforce="Mide el largo y el ancho de tu mesa y dibuja su planta en escala 1:10 en papel cuadriculado, indicando las medidas en centímetros.",
    extend="Explica por qué cambiar de escala es una homotecia y cuál es su razón al pasar de 1:100 a 1:20.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (de ejemplo). Encargo: diseñar un mural de pasillo que dé la impresión de seguir avanzando, y decidir cuándo conviene una vista isométrica (proyección paralela). "
     "Modelo: ojo en O(0, 0, 0) mirando hacia +y, plano de dibujo y = 1, imagen (x ÷ y, z ÷ y). El pasillo mide 4 m de ancho (x de −2 a 2) y 4 m de alto (z de −2 a 2, con el ojo a media altura), y va de y = 2 (entrada) a y = 8 (fondo). "
     "Las esquinas de la entrada son (±2, 2, ±2) y las del fondo son (±2, 8, ±2). En la vista isométrica, los tres ejes se dibujan a 120° y se conserva la escala sobre cada eje.")
build(
    O5, 5, F,
    use="Aprenderé a diseñar una propuesta de perspectiva o de vista paralela para arte, arquitectura o diseño, a verificarla con cálculos y a comparar alternativas con criterios.",
    prior=["Sé calcular imágenes y puntos de fuga.", "Sé leer plantas y elevaciones a escala.", "Sé comparar dos soluciones usando criterios."],
    explain=[
        "Diseñar una propuesta es decidir con criterios: qué debe lograr el dibujo (parecer real o permitir medir), qué proyección usa y cómo se comprueba. Para parecer real se usa perspectiva central: la entrada del pasillo del modelo se dibuja con esquinas en (±1, ±1) y el fondo con esquinas en (±1/4, ±1/4), una homotecia de razón 1/4 con centro en el punto de fuga (0, 0). La razón sale del cociente de las distancias: 2 ÷ 8.",
        "Para permitir medir y fabricar se usa la proyección paralela. En la vista isométrica los ejes forman 120° entre sí y las medidas sobre cada eje conservan la escala, por lo que una pieza de madera se puede acotar directamente. Su desventaja es que no da sensación de profundidad ni de lejanía. Cada proyección sirve a un propósito distinto, y una buena propuesta lo declara.",
        "Antes de entregar un diseño se verifica con una lista breve: ¿el horizonte está a la altura del ojo?, ¿las líneas paralelas de una dirección van al mismo punto de fuga?, ¿los tamaños aparentes siguen la razón de distancias?, ¿las vistas son coherentes entre sí? También se declaran los límites: el modelo supone un ojo fijo y un plano plano, y un programa de dibujo no sustituye el razonamiento.",
    ],
    vocab=[("propuesta de diseño", "solución elegida para un encargo, con criterios"), ("vista isométrica", "proyección paralela con tres ejes a 120°"), ("criterio", "condición para decidir si una propuesta sirve"), ("razón de distancias", "cociente entre la distancia de la entrada y la del fondo"), ("verificación", "comprobación con cálculos de que el diseño cumple"), ("límite del modelo", "lo que el modelo no representa")],
    worked=[
        ("Fondo del pasillo", "En otro pasillo, la entrada está en y = 2 y el fondo en y = 5, con esquinas (1, 2, 1) y (1, 5, 1). Calcula la imagen del fondo y su razón respecto de la entrada.", ["La entrada se dibuja en (1 ÷ 2, 1 ÷ 2) = (1/2, 1/2).", "El fondo se dibuja en (1 ÷ 5, 1 ÷ 5) = (1/5, 1/5), que es 2/5 de (1/2, 1/2)."], "Imagen (1/5, 1/5) y razón 2/5"),
        ("Elegir la proyección", "Un taller debe fabricar un banco de madera con medidas exactas. ¿Qué dibujo le entregas?", ["Necesita medir directamente sobre cada eje.", "La vista isométrica conserva la escala en los tres ejes."], "Una vista isométrica (proyección paralela)"),
    ],
    mistakes=[("Dibujar el fondo del pasillo con el mismo tamaño que la entrada.", "En perspectiva central lo lejano aparece más pequeño, según la razón de distancias.", "Calcula la razón de distancias y úsala para el fondo."),
              ("Dibujar paralelas reales como paralelas en perspectiva central.", "Las paralelas que se alejan convergen en un punto de fuga.", "Traza esas líneas hacia el punto de fuga.")],
    T=[
        ('abc', '{F} ¿Cuál es la imagen de la esquina de la entrada (2, 2, 2)?', '(1, 1)', '(4, 4)', '(2, 2)', 'Se divide por la profundidad y = 2: 2 ÷ 2 y 2 ÷ 2.'),
        ('abc', '{F} ¿Cuál es la imagen de la esquina del fondo (2, 8, 2)?', '(1/4, 1/4)', '(1/2, 1/2)', '(4, 4)', 'Se divide por la profundidad y = 8: 2 ÷ 8 y 2 ÷ 8.'),
        ('ab', 'Comparado con el cuadrado de la entrada, el cuadrado del fondo se dibuja:', 'Más pequeño, con razón 1/4', 'Igual de grande', 'Está más lejos (8 m contra 2 m), así que se reduce con razón 2 ÷ 8.'),
        ('=', '{F} ¿Cuántos metros mide el ancho aparente de la entrada, entre x′ = −1 y x′ = 1?', '4//2', 'El ancho real de 4 m se divide por la profundidad 2.', ' m'),
        ('{F} ¿Cuál es el ancho aparente del fondo, en metros, como fracción?', '1/2', 'El ancho real de 4 m dividido por la profundidad 8 da 1/2.'),
        ('{F} ¿Cuál es el punto de fuga de las aristas del pasillo, que van en la dirección (0, 1, 0)?', '(0, 0)', 'Se calcula (0 ÷ 1, 0 ÷ 1).'),
        ('abc', '{F} ¿A qué altura queda la línea del horizonte en la imagen?', 'z′ = 0, porque el ojo está en z = 0', 'z′ = −1, porque el suelo está en z = −2', 'z′ = 1, porque el techo está en z = 2', 'El horizonte es la línea a la altura del ojo, que en el modelo es z = 0.'),
        ('=', '{F} ¿Cuántas veces mayor es la altura aparente de la entrada que la del fondo? Usa las distancias 8 m y 2 m.', '8//2', 'La altura aparente es inversamente proporcional a la distancia al ojo.', ' veces'),
        ('abc', 'Una pieza de metal debe fabricarse y medirse con regla sobre el plano entregado. ¿Qué dibujo conviene?', 'Una vista isométrica, que conserva la escala en cada eje', 'Una perspectiva central de dos puntos de fuga', 'Un dibujo con tres puntos de fuga', 'La proyección paralela permite medir directamente; la central modifica las medidas.'),
        ('abc', 'Una dibujante afirma: «las líneas del techo y del suelo del pasillo deben quedar paralelas en el dibujo porque son paralelas en la realidad». ¿Qué corresponde?', 'En perspectiva central deben converger al punto de fuga', 'Tiene razón siempre', 'Deben cruzarse en el fondo sin llegar al punto de fuga', 'Las paralelas que se alejan del observador se dibujan hacia el punto de fuga.'),
        ('abc', 'Dos propuestas para el mural: A dibuja el fondo con razón 1/4 y líneas hacia (0, 0); B dibuja el fondo con razón 1/2. Con entrada en y = 2 y fondo en y = 8, ¿cuál es consistente?', 'A, porque 2 ÷ 8 = 1/4', 'B, porque 1/2 es mayor y se ve mejor', 'Ninguna', 'La razón debe ser el cociente de distancias, 2 ÷ 8 = 1/4.'),
        ('El pasillo se alarga y el fondo queda en y = 12, con la entrada en y = 2. ¿Cuánto mide el ancho aparente del fondo para un ancho real de 4 m? Responde como fracción.', '1/3', 'Se divide el ancho real por la profundidad: 4 ÷ 12 = 1/3.'),
        ('Se quiere que el fondo del pasillo se vea con 1/8 del tamaño de la entrada, que está en y = 2. ¿A qué distancia del ojo debe estar el fondo?', '16 m', 'La razón es 2 ÷ D = 1/8, así que D = 16.'),
    ],
    ctx=('abc', 'Para pintar en un muro un pasillo que parezca más largo de lo que es, ¿cuál es la decisión de diseño más adecuada?', 'Dibujar líneas que convergen en un punto de fuga sobre el horizonte y figuras más pequeñas al fondo', 'Dibujar todas las líneas paralelas y del mismo tamaño', 'Dibujar el fondo más grande que la entrada', 'La perspectiva central crea profundidad con convergencia y reducción de tamaño.'),
    sc=[
        ("En Geometría 3D: ¿qué proyección conviene para parecer real?", "La central (perspectiva)", "Reproduce la convergencia y el achicamiento."),
        ("¿Qué proyección conviene para medir y fabricar una pieza?", "La paralela, por ejemplo la isométrica", "Conserva la escala sobre los ejes."),
        ("¿De qué distancias sale la razón del fondo?", "Del cociente entre la distancia de la entrada y la del fondo", "La imagen es inversamente proporcional a la distancia."),
    ],
    op=("Elige un encargo y diséñalo en papel con sus cálculos: (a) un mural de pasillo de 4 m de ancho con entrada en y = 2 y fondo en y = 10: calcula las imágenes de las esquinas de la entrada y del fondo, el punto de fuga y la razón, y describe tu dibujo; (b) una vista isométrica de una caja de 4 cuadrados de largo, 2 de ancho y 3 de alto en papel cuadriculado, indicando cómo conservas la escala. Escribe tres criterios con que revisas tu propuesta y qué límite tiene tu modelo.",
        "Caso (a): entrada (±2 ÷ 2, ±2 ÷ 2) = (±1, ±1); fondo (±2 ÷ 10, ±2 ÷ 10) = (±1/5, ±1/5); razón 1/5; punto de fuga (0, 0). Criterios: horizonte a la altura del ojo, líneas hacia el punto de fuga, fondo con razón 2 ÷ 10. Límite: ojo fijo y plano de dibujo plano.",
        ["propuesta justificada con la proyección elegida", "cálculos que respaldan el dibujo", "criterios de revisión y un límite declarado"],
        ["hoja con el diseño, los cálculos y la lista de criterios"],
        ["no justificar la proyección", "dibujar el fondo con tamaño incorrecto", "no declarar límites"],
        "Pregunta: «¿qué criterio usaste para decidir?». Si no tiene, pídele que escriba uno medible."),
    reinforce="Elige un objeto de tu casa, dibuja una vista isométrica con regla y una perspectiva de un punto de fuga, y escribe en cuál se miden mejor sus partes.",
    extend="Explica por qué en una perspectiva central un objeto lejano y uno cercano pueden tener la misma imagen aunque sean de tamaños distintos.",
)
