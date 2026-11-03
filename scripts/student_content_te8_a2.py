"""Cuaderno del estudiante, 8.º básico Tecnología: OA 02 (diseño sustentable y creación con herramientas TIC), clases 1 a 5.

Seguridad: las tareas son de lectura, cálculo y escritura; si se construye, solo con papel, cartón, cinta, cordel, pegamento en barra y tijeras de punta roma, sin herramientas con filo, fuego, vidrio ni electricidad de red.
Cifras enteras. Los precios, las medidas y los resultados de pruebas son de ejemplo, para practicar. Las herramientas TIC se nombran por tipo (planilla, buscador, programa de dibujo), no por marca.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te8_a import reg
from student_lessons import arith, ex

OA2 = "TE08 OA 02"

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a escribir criterios de eficiencia y de sustentabilidad con un indicador y un valor límite, y a revisar un diseño a lo largo de su ciclo de vida. Sirve para diseñar un producto que gaste poco y cause menos daño.",
    prior=["Sé formular una oportunidad con una meta medible.", "Sé calcular porcentajes.", "Sé que un producto tiene materiales, uso y un final."],
    explain=[
        "La eficiencia es lograr la función del producto gastando pocos recursos: material, energía, tiempo o dinero. Se mide con un indicador, por ejemplo «gramos de cartón por soporte» o «minutos de armado». La sustentabilidad es satisfacer una necesidad sin agotar recursos ni dañar el ambiente ni a las personas. Tiene tres dimensiones: ambiental (materiales, energía, residuos), social (seguridad, acceso, trabajo justo) y económica (costo y duración).",
        "Para revisar un diseño se recorre su ciclo de vida, que son las etapas por las que pasa un producto: obtener las materias primas, fabricar, usar y llegar al fin de vida, cuando se reutiliza, repara, recicla o desecha. Un diseño sustentable se pregunta en cada etapa qué gasta y qué deja. Un producto reparable, con piezas que se pueden cambiar o desarmar, alarga su vida y retrasa el desecho.",
        "Un criterio de diseño se escribe con un indicador y un umbral, que es el valor límite que debe cumplirse. «Que sea muy ecológico» no se puede comprobar; «al menos 60 % de las piezas reutilizadas» sí. El porcentaje de reutilización es piezas reutilizadas × 100 ÷ piezas totales. El material aprovechado es el que queda en el producto, dividido entre el material usado.",
    ],
    vocab=[("eficiencia", "lograr la función gastando pocos recursos"), ("sustentabilidad", "satisfacer una necesidad sin agotar recursos ni dañar al ambiente ni a las personas"), ("ciclo de vida", "etapas de un producto, desde sus materias primas hasta su fin de vida"), ("indicador", "dato medible de un criterio"), ("umbral", "valor límite que debe cumplirse")],
    worked=[
        ("Calcular el porcentaje de reutilización", "Un organizador tiene 20 piezas y 14 son de cartón de cajas ya usadas. El criterio pide al menos 60 %. ¿Cumple?", ["Calculo 14 × 100 ÷ 20 = 70.", "Comparo con el umbral: 70 es mayor que 60."], "Sí cumple, con 70 %"),
        ("Ubicar una decisión en el ciclo de vida", "Un grupo arma un portalápices con una caja que ya existía. ¿En qué etapa del ciclo de vida se ahorra?", ["Al reutilizar la caja no hace falta producir cartón nuevo.", "El ahorro ocurre al obtener la materia prima."], "En la obtención de la materia prima"),
    ],
    mistakes=[
        ("Escribir un criterio como «que sea ecológico».", "No tiene indicador ni umbral, así que no se puede comprobar.", "Escribe una cantidad: «al menos 60 % de piezas reutilizadas»."),
        ("Creer que un diseño es sustentable solo porque usa poco material.", "Puede ser eficiente y aun así no poder repararse ni reciclarse.", "Revisa también uso, reparación y fin de vida."),
    ],
    R=[
        ("El ciclo de vida de un producto, ¿empieza con la obtención de materias primas o con el desecho?", "Con la obtención de materias primas", "Las etapas van en orden: materias primas, fabricación, uso y fin de vida."),
        ("¿Cuál es una exigencia de la dimensión social de la sustentabilidad? A) que el producto sea seguro y accesible para quien lo usa B) que cueste poco", "A", "La seguridad y el acceso son dimensión social; el costo es dimensión económica."),
        ("¿Cuál es un criterio bien escrito? A) «que sea muy ecológico» B) «al menos 60 % de piezas reutilizadas»", "B", "Solo el segundo tiene indicador y umbral que se pueden comprobar."),
    ],
    C=[
        ("Dos soportes de lápices: el primero tiene 4 piezas pegadas que no se pueden separar; el segundo tiene 4 piezas unidas con pestañas que se desarman. ¿Cuál se repara más fácilmente?", "El segundo", "Se puede cambiar una pieza sin romper las demás."),
        ("¿Qué diferencia hay entre eficiencia y sustentabilidad? A) la eficiencia logra la función con pocos recursos y la sustentabilidad cuida además el ambiente y a las personas B) la eficiencia cuida el ambiente y la sustentabilidad solo el dinero", "A", "La sustentabilidad abarca más dimensiones que el uso de recursos."),
        ("Un soporte es barato y reutiliza cajas, pero sus grapas cortan a los niños pequeños. ¿Qué dimensión de la sustentabilidad falla?", "La social", "Falla la seguridad de las personas que lo usan."),
    ],
    A=[
        arith("Un organizador de ejemplo tiene 24 piezas y 18 son reutilizadas. ¿Qué porcentaje de piezas reutilizadas tiene?", "18*100//24", "Se divide la parte entre el total y se multiplica por 100.", " %"),
        arith("De 40 hojas de cartulina usadas en un modelo, 34 quedaron en el producto final y el resto fue desperdicio. ¿Qué porcentaje del material se aprovechó?", "34*100//40", "Se compara el material que quedó con el material usado.", " %"),
        ("Criterio: al menos 60 % de piezas reutilizadas y 5 piezas o menos. P: 8 piezas, 6 reutilizadas. Q: 5 piezas, 4 reutilizadas. R: 4 piezas, 2 reutilizadas. ¿Cuál cumple los dos?", "Q", "Q tiene 5 piezas y 80 % reutilizado; P tiene demasiadas piezas y R solo 50 %."),
    ],
    Z=[
        ("Un diseño usa muy poco material, pero solo se arma con un pegamento fuerte y no se puede reparar ni reciclar. ¿Es suficiente para llamarlo sustentable? A) no, porque falta mirar la reparación y el fin de vida B) sí, porque usa poco material", "A", "Un diseño sustentable considera todas las etapas del ciclo de vida."),
        ("El curso quiere un criterio de bajo impacto para un portalápices. ¿Cuál lo expresa mejor? A) «pesar menos de 80 g y no usar adhesivos» B) «que pese poco y no sea malo»", "A", "El primero tiene indicadores y umbrales que se pueden medir."),
    ],
    D=[
        ex("Un soporte con material nuevo cuesta $4.500 en materiales y el mismo soporte con material reutilizado cuesta $1.500. Para fabricar 12 soportes, ¿cuánto se ahorra?", "$36.000", "Se calcula el ahorro de uno, 3.000, y se multiplica por 12.", calc="(4500-1500)*12"),
        ("Se da 1 punto por cada criterio cumplido: al menos 50 % reutilizado, 6 piezas o menos, se puede desarmar. U: 10 piezas, 6 reutilizadas, se desarma. V: 6 piezas, 2 reutilizadas, no se desarma. W: 5 piezas, 3 reutilizadas, se desarma. ¿Cuál suma más y cuántos puntos?", "W, con 3 puntos", "W cumple los tres; U falla las piezas y V falla la reutilización y el desarme."),
    ],
    ctx=ex("En tu casa planeas armar un organizador de 20 piezas, de las cuales 12 vienen de cajas ya usadas. El criterio pide al menos 60 % reutilizado. ¿Qué porcentaje tiene y cumple?", "60 %; sí cumple, porque el criterio dice al menos 60 %", "Se calcula 12 × 100 ÷ 20 = 60, que alcanza el umbral.", calc="12*100//20"),
    sc=[
        ("¿Qué etapas tiene el ciclo de vida de un producto?", "Materias primas, fabricación, uso y fin de vida", "Son las etapas del recorrido del producto."),
        ("¿Cuáles son las tres dimensiones de la sustentabilidad?", "Ambiental, social y económica", "Cuidan el ambiente, a las personas y los recursos económicos."),
        ("¿Qué es un umbral?", "El valor límite que debe cumplirse", "Permite decidir si el criterio se cumple."),
    ],
    open_task=(
        "Evalúa este diseño de ejemplo: un organizador de escritorio de 9 piezas; 6 son de cartón reutilizado y 3 son cintas nuevas; se arma sin pegamento con pestañas; pesa 300 g y los materiales nuevos cuestan $1.200. Escribe tres criterios, uno ambiental, uno social y uno económico, cada uno con indicador y umbral; indica si el diseño cumple cada uno (inventa el umbral con sentido) y qué cambiarías en el fin de vida.",
        "Ambiental: al menos 60 % de piezas reutilizadas; cumple, 6 de 9 es 67 %. Social: bordes sin grapas; cumple, no tiene. Económica: materiales nuevos bajo $1.500; cumple, gasta $1.200. Fin de vida: como se desarma, las piezas de cartón pueden reutilizarse",
        ["escribe tres criterios con indicador y umbral", "calcula el porcentaje de reutilización", "indica si cumple cada uno", "considera el fin de vida"],
        ["ficha con tres criterios y su revisión"],
        ["escribir criterios sin número", "olvidar el fin de vida"],
        "Pregunta: «¿cómo se comprobaría ese criterio con un número?». Si no hay número, pídele reescribirlo.",
    ),
    reinforce="Elige un objeto de tu casa y recorre su ciclo de vida: de dónde viene el material, cómo se usa y qué se puede hacer cuando deje de servir.",
    extend="Compara dos objetos que cumplen la misma función y explica cuál es más sustentable en cada dimensión.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja, lápiz y las tablas escritas en este cuaderno. Si tienes computador, una planilla de cálculo para practicar; si no, hazlo en papel.",
    use="Aprenderé a elegir la herramienta TIC adecuada para cada etapa del diseño: buscar información confiable, calcular costos, dibujar, documentar y respaldar. Sirve para trabajar con orden y sin perder el trabajo.",
    prior=["Sé que un diseño tiene etapas.", "Sé hacer cálculos con dinero.", "Sé qué es un criterio de diseño."],
    explain=[
        "Las herramientas TIC (tecnologías de la información y la comunicación) ayudan en cada etapa del diseño. Para investigar se usa un buscador y se leen fuentes; para calcular costos y cantidades, una planilla de cálculo; para representar la idea, un programa de dibujo; para documentar el proceso, un procesador de texto o una presentación; y para no perder el trabajo, copias de respaldo.",
        "No toda fuente es confiable. Se revisa quién es el autor, la fecha, el propósito de la página y si cita sus fuentes, y se contrastan los datos importantes en al menos dos fuentes distintas. Cuando se usa un texto o un dato ajeno, se indica de dónde salió. En una planilla, cada dato va en una celda. Una fórmula empieza con el signo igual: =B2*C2 multiplica los valores de dos celdas y =SUMA(D2:D5) suma de la celda D2 a la D5.",
        "El respaldo es una copia del archivo guardada en otro lugar. La regla básica es tener el archivo en dos lugares distintos, por ejemplo el computador y un dispositivo externo, porque un solo lugar puede fallar. Todo debe tener una alternativa sin computador: una tabla dibujada en papel cumple la misma función.",
    ],
    vocab=[("TIC", "tecnologías de la información y la comunicación"), ("fuente confiable", "fuente con autor, fecha, propósito claro y datos citados"), ("planilla de cálculo", "programa que ordena datos en celdas y calcula con fórmulas"), ("fórmula", "instrucción de cálculo que empieza con el signo igual"), ("respaldo", "copia guardada en otro lugar")],
    worked=[
        ("Calcular con una fórmula", "En una planilla, B2 vale 5 (cantidad) y C2 vale 400 (precio de cada uno, en pesos). ¿Qué muestra D2 con la fórmula =B2*C2?", ["La fórmula multiplica la cantidad por el precio.", "5 × 400 = 2.000."], "$2.000"),
        ("Elegir entre dos fuentes", "Para saber cuánto peso soporta el cartón corrugado hay dos páginas: una sin autor ni fecha y otra de un centro técnico, con autor, fecha y fuentes. ¿Cuál se usa primero?", ["Reviso autor, fecha y fuentes en cada una.", "La segunda cumple los tres requisitos."], "La del centro técnico, y se contrasta con otra fuente"),
    ],
    mistakes=[
        ("Usar la primera página que muestra el buscador sin revisarla.", "Salir primero no garantiza que la información sea correcta.", "Revisa autor, fecha y fuentes, y contrasta con una segunda fuente."),
        ("Guardar el plano en un solo computador.", "Si ese equipo falla, se pierde el trabajo.", "Guarda una copia en otro lugar."),
    ],
    R=[
        ("Para calcular el costo total de muchos materiales, ¿conviene una planilla de cálculo o un procesador de texto?", "Una planilla de cálculo", "La planilla calcula automáticamente con fórmulas."),
        ("¿En qué etapa se usa un programa de dibujo: al representar la solución o al buscar información?", "Al representar la solución", "Sirve para dibujar el plano o el croquis."),
        ("Una copia de respaldo, ¿sirve para recuperar un archivo perdido o para que el archivo se vea mejor?", "Para recuperar un archivo perdido", "Es una copia guardada en otro lugar."),
    ],
    C=[
        ("En una planilla, B2 vale 6 y C2 vale 250. ¿Qué muestra la celda D2 si contiene =B2*C2?", "1.500", "Multiplica 6 × 250 = 1.500."),
        ("¿Por qué conviene contrastar un dato con dos fuentes? A) para comprobar que los datos coinciden B) para que el dato se vea más importante", "A", "Si dos fuentes independientes coinciden, el dato es más confiable."),
        ("Un compañero pega en su informe un texto técnico sin decir de dónde lo sacó. ¿Qué falta? A) citar la fuente B) cambiar algunas palabras para que no se note", "A", "Se debe indicar el origen de lo que no es propio."),
    ],
    A=[
        ex("Una planilla de ejemplo tiene en la columna D, de la fila 2 a la 5, estos costos: cartón $1.800, cinta $950, cordel $650 y pegamento $1.100. ¿Qué valor muestra =SUMA(D2:D5)?", "$4.500", "La función suma los cuatro valores: 1.800 + 950 + 650 + 1.100 = 4.500.", calc="1800+950+650+1100"),
        ex("Una planilla de ejemplo lista 12 hojas de cartulina a $150 cada una y 3 pliegos de cartón a $700 cada uno. ¿Cuál es el total?", "$3.900", "Se calcula 12 × 150 = 1.800 y 3 × 700 = 2.100, y se suman.", calc="12*150+3*700"),
        ("Asigna a cada etapa su herramienta (P planilla, D programa de dibujo, T procesador de texto): (1) calcular costos, (2) dibujar el plano, (3) escribir el informe final.", "1 P, 2 D, 3 T", "Cada herramienta se usa donde es más útil."),
    ],
    Z=[
        ("Un grupo guarda su único archivo del plano en el computador de la sala, y un día ese computador falla. ¿Qué regla habría evitado perder el trabajo? A) guardar copias en dos lugares distintos B) cambiar el nombre del archivo", "A", "Con una copia en otro lugar se puede recuperar el plano."),
        ("Una página afirma que un cartón soporta «el doble que cualquiera», sin autor ni datos, y otra, con tabla de ensayos y fecha, dice que soporta 40 kg. ¿Cuál es más confiable? A) la de la tabla de ensayos y fecha B) la que usa palabras más fuertes", "A", "Los datos y la fecha permiten comprobar la afirmación."),
    ],
    D=[
        ex("Planilla de presupuesto de ejemplo: fila 1, 4 unidades a $750; fila 2, 10 unidades a $120; fila 3, 2 unidades a $1.350. ¿Qué valor muestra la suma de la columna total?", "$6.900", "Se calcula 3.000 + 1.200 + 2.700 = 6.900.", calc="4*750+10*120+2*1350"),
        ("Tres tareas: (a) encontrar normas de seguridad para el cartón, (b) hacer un plano con medidas, (c) graficar el gasto por semana. Herramientas: B buscador, D programa de dibujo, P planilla con gráfico. Asigna una a cada tarea en orden.", "a B, b D, c P", "Cada tarea necesita la herramienta que mejor la resuelve."),
    ],
    ctx=ex("Para una maqueta compras 15 palitos de helado a $20 cada uno y 4 láminas de cartón a $450 cada una. ¿Qué total debería mostrar tu planilla?", "$2.100", "Se calcula 15 × 20 = 300 y 4 × 450 = 1.800, y se suman.", calc="15*20+4*450"),
    sc=[
        ("¿Con qué signo empieza una fórmula?", "Con el signo igual", "Así la planilla sabe que debe calcular."),
        ("¿Qué datos conviene revisar de una fuente?", "Autor, fecha, propósito y si cita fuentes", "Permiten juzgar si es confiable."),
        ("¿Dónde conviene guardar un archivo importante?", "En dos lugares distintos", "Así existe un respaldo."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: arma una tabla de presupuesto para un soporte de libros con estos materiales de ejemplo: 3 láminas de cartón a $500, 2 rollos de cinta a $800, 5 metros de cordel a $150 cada metro. Escribe las fórmulas de cada fila, la del total y el valor del total. Caso 2: compara dos fuentes de ejemplo sobre cuánta carga soporta una repisa de cartón: la fuente A es de un centro técnico (con autor, fecha y tabla) y la fuente B es un comentario anónimo sin fecha. Decide cuál usarías y qué harías para contrastar el dato.",
        "Caso 1: fila 1 =B2*C2 da $1.500; fila 2 da $1.600; fila 3 da $750; total =SUMA(D2:D4) da $3.850",
        ["usa fórmulas o cálculos correctos", "calcula bien el total", "o bien elige fuente con criterios", "propone contrastar con otra fuente"],
        ["tabla de presupuesto o juicio de fuentes"],
        ["no usar el signo igual en la fórmula", "fiarse de una fuente anónima"],
        "Pregunta: «¿cómo sabes que esta fuente es confiable?». Pídele nombrar autor, fecha y datos.",
    ),
    reinforce="Dibuja en papel una tabla de presupuesto de tres materiales con cantidad, precio y total, y calcula el total general.",
    extend="Explica por qué una tabla en papel puede reemplazar a una planilla cuando no hay computador.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja, lápiz, regla y los datos escritos en este cuaderno.",
    use="Aprenderé a representar un diseño con un croquis acotado y a escala, a escribir la lista de materiales y a calcular cuántas piezas salen de una plancha. Sirve para construir con precisión y sin desperdiciar material.",
    prior=["Sé medir en centímetros.", "Sé multiplicar y dividir.", "Sé que 1 m equivale a 100 cm."],
    explain=[
        "Antes de construir se representa el diseño. El croquis acotado es un dibujo con las medidas escritas, que se llaman cotas, siempre con su unidad (por ejemplo 24 cm). Se dibujan varias vistas: frontal, lateral y superior. Un programa de dibujo permite copiar piezas y corregir medidas sin borrar todo.",
        "La escala es la relación entre el dibujo y la realidad. En la escala 1:10, 1 cm del dibujo representa 10 cm reales. Para pasar del dibujo a la realidad se multiplica por 10; para pasar de la realidad al dibujo se divide entre 10. Recuerda que 1 m son 100 cm. En el plano se escriben las cotas reales, no las del dibujo, porque con ellas se cortan las piezas.",
        "La lista de materiales dice, para cada pieza, su nombre, cantidad, medidas y material. Para saber cuántas piezas salen de una plancha, se divide cada lado de la plancha entre el de la pieza (solo la parte entera) y se multiplican los resultados. Así se ve el desperdicio antes de cortar.",
    ],
    vocab=[("cota", "medida escrita en el dibujo, con su unidad"), ("escala", "relación entre el tamaño del dibujo y el real"), ("croquis", "dibujo rápido con las medidas principales"), ("vista", "forma de mirar el objeto: frontal, lateral o superior"), ("lista de materiales", "tabla de piezas con cantidad, medidas y material")],
    worked=[
        ("Pasar del dibujo a la realidad", "En un plano a escala 1:10, una pieza mide 4 cm. ¿Cuánto mide en la realidad?", ["En 1:10, 1 cm del dibujo son 10 cm reales.", "Multiplico 4 × 10."], "40 cm"),
        ("Calcular piezas por plancha", "De una plancha de 90 cm × 60 cm se cortan piezas de 15 cm × 10 cm. ¿Cuántas salen sin girarlas?", ["A lo largo: 90 ÷ 15 = 6. A lo ancho: 60 ÷ 10 = 6.", "Multiplico las filas por las columnas: 6 × 6."], "36 piezas"),
    ],
    mistakes=[
        ("Escribir en las cotas las medidas del dibujo y no las reales.", "Quien corta fabricará piezas con el tamaño equivocado.", "Escribe siempre la medida real con su unidad."),
        ("Calcular las piezas por plancha dividiendo solo las áreas.", "El área ignora que sobran bordes que no alcanzan para una pieza más.", "Divide cada lado por separado y multiplica."),
    ],
    R=[
        ("En escala 1:10, ¿1 cm del plano representa 10 cm reales o 1 cm real?", "10 cm reales", "La escala 1:10 multiplica el dibujo por 10 para obtener la realidad."),
        ("Una cota, ¿incluye la unidad (por ejemplo cm) o solo el número?", "Incluye la unidad", "Sin unidad no se sabe si son centímetros o metros."),
        ("La lista de materiales, ¿indica cantidad y medidas de cada pieza o solo el nombre del producto final?", "Cantidad y medidas de cada pieza", "Sirve para comprar y cortar con exactitud."),
    ],
    C=[
        ("¿Cuál escala muestra el objeto más grande en el papel? A) 1:5 B) 1:50", "A", "Con 1:5 el dibujo es la quinta parte de la realidad; con 1:50 es la cincuentava parte."),
        ("Un plano sin cotas, ¿qué problema produce? A) no se sabe de qué tamaño cortar las piezas B) el dibujo se ve menos bonito", "A", "Las cotas entregan las medidas necesarias para construir."),
        ("Una mesa de 80 cm de alto se dibuja a escala 1:10 con 8 cm de alto. ¿Está bien dibujada?", "Sí", "8 cm × 10 = 80 cm."),
    ],
    A=[
        arith("En un plano a escala 1:10 un lado mide 7 cm. ¿Cuánto mide en la realidad?", "7*10", "Se multiplica por 10.", " cm"),
        arith("Una repisa real mide 90 cm de largo. ¿Cuántos centímetros mide en un plano a escala 1:10?", "90//10", "Se divide la medida real entre 10.", " cm"),
        arith("De una plancha de 120 cm × 80 cm se cortan piezas de 30 cm × 20 cm, sin girarlas. ¿Cuántas piezas salen?", "(120//30)*(80//20)", "Se divide cada lado y se multiplican las cantidades.", " piezas"),
    ],
    Z=[
        ("Un grupo dibuja un plano a escala 1:10 y escribe como cota 7 cm en vez de la medida real, 70 cm. ¿Qué pasará cuando alguien corte? A) cortará piezas diez veces más pequeñas que las necesarias B) las piezas quedarán del tamaño correcto", "A", "Se cortó con la medida del dibujo y no con la real."),
        ("Para una plancha de 100 cm × 60 cm y piezas de 35 cm × 25 cm, un compañero divide el área de la plancha entre el área de la pieza y dice que caben 6 piezas. Otro divide cada lado de la plancha entre el lado de la pieza. ¿Cuántas salen realmente sin girarlas?", "4", "100 ÷ 35 da 2 y 60 ÷ 25 da 2, así que salen 2 × 2 = 4; el cálculo por área ignora los sobrantes."),
    ],
    D=[
        arith("Un proyecto necesita 48 piezas de 20 cm × 15 cm. De cada plancha de 100 cm × 60 cm salen 20 piezas. ¿Cuántas planchas se necesitan como mínimo?", "(48+19)//20", "Se divide 48 entre 20 y se sube al siguiente número entero.", " planchas"),
        ("Una pieza de 3 m × 2 m se dibuja a escala 1:50. ¿Cuáles son sus medidas en el plano?", "6 cm × 4 cm", "3 m son 300 cm y 300 ÷ 50 = 6; 2 m son 200 cm y 200 ÷ 50 = 4."),
    ],
    ctx=ex("Quieres hacer el plano de un mesón de 120 cm de largo y 60 cm de ancho a escala 1:10. ¿Qué medidas tiene en el plano?", "12 cm × 6 cm", "Se dividen las medidas reales entre 10: 120 ÷ 10 = 12 y 60 ÷ 10 = 6.", calc="120//10"),
    sc=[
        ("¿Qué es una cota?", "Una medida escrita en el dibujo con su unidad", "Indica el tamaño real que se debe fabricar."),
        ("En Tecnología: ¿Cuántos centímetros son 2 metros?", "200 cm", "1 m son 100 cm."),
        ("¿Qué contiene una lista de materiales?", "Pieza, cantidad, medidas y material", "Permite comprar y cortar."),
    ],
    open_task=(
        "Diseña en papel un soporte para libros con estas piezas reales: base de 24 cm × 16 cm, respaldo de 24 cm × 12 cm y sostén de 16 cm × 8 cm. Dibuja las tres piezas a escala 1:2 con sus cotas reales, escribe la lista de materiales y calcula cuántas bases de 24 cm × 16 cm salen de una plancha de cartón de 48 cm × 32 cm.",
        "A escala 1:2 la base mide 12 cm × 8 cm en el dibujo y se escribe 24 cm × 16 cm como cota; de la plancha salen (48 ÷ 24) × (32 ÷ 16) = 2 × 2 = 4 bases",
        ["dibuja las piezas a escala 1:2", "escribe cotas reales con unidad", "arma la lista de materiales", "calcula bien las piezas por plancha"],
        ["croquis acotado, lista de materiales y cálculo"],
        ["escribir las cotas del dibujo en vez de las reales", "calcular las piezas por plancha con el área"],
        "Pregunta: «¿esta medida es la del papel o la real?». Pídele escribir la medida real con unidad.",
    ),
    reinforce="Mide un objeto pequeño de tu casa y dibújalo a escala 1:2, anotando sus cotas reales.",
    extend="Explica por qué una buena distribución de piezas en la plancha puede reducir el desperdicio.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a planificar la construcción con un cronograma, un presupuesto y un análisis de riesgos, y a implementar con seguridad. Sirve para terminar a tiempo, sin pasarse del dinero y sin accidentes.",
    prior=["Sé calcular tiempos y presupuestos simples.", "Sé qué materiales y herramientas son seguros.", "Sé leer una tabla de tareas."],
    explain=[
        "Un plan de trabajo ordena las tareas, quién las hace, cuánto demoran y qué materiales usan. Las tareas pueden ir una después de otra (en serie) o al mismo tiempo (en paralelo) cuando no dependen entre sí. El tiempo total suma las tareas en serie y, en las paralelas, solo cuenta la más larga. El presupuesto es el dinero disponible; se compara con el gasto y queda un saldo.",
        "Un riesgo es algo que puede causar daño. Para controlarlo se prefiere primero eliminarlo, por ejemplo cambiando el material por uno más seguro; si no se puede, se reduce, por ejemplo con otro orden de trabajo; y como último recurso se usa protección. Con cartón y papel se trabaja con tijeras de punta roma, sobre una base firme, con la mano lejos de la línea de corte y con el puesto ordenado.",
        "Si una tarea no se puede hacer con seguridad, se cambia el diseño o se pide ayuda a una persona adulta; nunca se hace igual. Durante el trabajo se registran los cambios y el motivo de cada uno, para que quede evidencia de cómo se llegó al producto final.",
    ],
    vocab=[("cronograma", "plan que ordena tareas y tiempos"), ("tareas en paralelo", "tareas que se hacen al mismo tiempo"), ("presupuesto", "dinero disponible para el proyecto"), ("riesgo", "algo que puede causar daño"), ("saldo", "dinero que queda después de gastar")],
    worked=[
        ("Calcular el tiempo total", "Tareas: medir 15 min; luego cortar 25 min y preparar la cinta 10 min al mismo tiempo; luego armar 30 min. ¿Cuánto dura el trabajo?", ["Cortar y preparar la cinta son paralelas: cuenta la más larga, 25 min.", "Sumo: 15 + 25 + 30."], "70 minutos"),
        ("Controlar un riesgo", "Al cortar cartón grueso con tijeras, la mano se presiona contra el borde. ¿Qué medida reduce el riesgo?", ["Apoyo el cartón sobre una base firme.", "Mantengo la mano lejos de la línea de corte y uso tijeras de punta roma."], "Apoyar sobre una base y mantener la mano lejos de la línea de corte"),
    ],
    mistakes=[
        ("Hacer una tarea insegura «con mucho cuidado» en vez de cambiarla.", "El cuidado no elimina el riesgo.", "Cambia el diseño o pide ayuda a una persona adulta."),
        ("Sumar el tiempo de todas las tareas, incluidas las paralelas.", "Las paralelas ocurren al mismo tiempo.", "En las paralelas cuenta solo la más larga."),
    ],
    R=[
        ("Un riesgo, ¿es algo que puede causar daño o algo que ya lo causó?", "Algo que puede causar daño", "Se trata de prevenir antes de que ocurra."),
        ("Al cortar con tijeras de punta roma, ¿la mano debe estar lejos de la línea de corte o cerca de la hoja?", "Lejos de la línea de corte", "Así no se corta la mano."),
        ("Si una tarea no se puede hacer con seguridad, ¿se cambia el diseño o se hace igual con mucho cuidado?", "Se cambia el diseño", "El cuidado no reemplaza una medida que elimine el riesgo."),
    ],
    C=[
        ("Para evitar cortes con el borde de una lata, un grupo rediseña la pieza con cartón. ¿Qué tipo de medida es? A) eliminar el riesgo B) usar protección personal", "A", "Se quitó la causa del riesgo al cambiar el material."),
        ("¿Cuándo pueden hacerse dos tareas al mismo tiempo? A) cuando no dependen una de la otra B) cuando las hace la misma persona", "A", "Si una necesita el resultado de la otra, deben ir en serie."),
        ("¿Por qué se registran los cambios durante el trabajo? A) para saber qué se modificó y por qué B) para que el trabajo dure más", "A", "El registro es evidencia del proceso."),
    ],
    A=[
        arith("Tareas: medir 20 min; luego cortar 30 min y preparar la cinta 10 min al mismo tiempo; luego armar 25 min. ¿Cuánto dura el trabajo si la cinta se prepara mientras se corta?", "20+30+25", "Se suma la medición, la tarea paralela más larga y el armado.", " minutos"),
        ex("Un grupo tiene un presupuesto de $5.000 y gastó cartón $1.850, cinta $900 y cordel $650. ¿Cuánto saldo le queda?", "$1.600", "Se restan los tres gastos del presupuesto: 5.000 − 3.400 = 1.600.", calc="5000-1850-900-650"),
        arith("Cortar 24 piezas demora 48 minutos para una persona. Si el trabajo se reparte entre 3 personas por igual, al mismo ritmo y al mismo tiempo, ¿cuánto demora?", "48//3", "Se divide el tiempo entre las personas.", " minutos"),
    ],
    Z=[
        ("Un grupo propone cortar cartón muy grueso con una herramienta de filo fuerte porque «es más rápido». ¿Qué responde un diseño seguro? A) cambiar a cartón más delgado y cortar con tijeras de punta roma B) usarla con mucho cuidado", "A", "Se elimina el riesgo en vez de depender del cuidado."),
        ("En el cronograma, «armar» depende de «cortar» (30 min) y de «preparar la cinta» (10 min), que empiezan juntas. ¿Cuándo puede empezar «armar»? A) a los 30 minutos B) a los 10 minutos", "A", "Debe esperar a que terminen las dos tareas, y la más larga dura 30 minutos."),
    ],
    D=[
        arith("Un plan tiene: medir 15 min, cortar 20 min, preparar el adhesivo 10 min (en paralelo con cortar), armar 25 min y revisar 5 min. ¿Cuánto dura en total?", "15+20+25+5", "El adhesivo corre en paralelo con cortar, por lo que no suma.", " minutos"),
        ("Hay $6.000 y 70 minutos. Plan A: $4.500 y 80 minutos. Plan B: $5.800 y 65 minutos. Plan C: $6.500 y 60 minutos. ¿Cuál respeta los dos límites?", "El plan B", "B gasta menos de $6.000 y dura menos de 70 minutos."),
    ],
    ctx=ex("Vas a armar un organizador de cartón y las tareas van una después de otra: marcar 10 min, cortar 20 min, doblar 15 min y pegar con pegamento en barra 20 min. ¿Cuánto demora el trabajo y qué medida de seguridad usas al cortar?", "65 minutos; tijeras de punta roma sobre una base firme y con la mano lejos de la línea de corte", "Se suman 10 + 20 + 15 + 20 = 65 minutos.", calc="10+20+15+20"),
    sc=[
        ("En Tecnología: ¿Qué es un cronograma?", "Un plan que ordena tareas y tiempos", "Indica qué se hace y cuándo."),
        ("En tareas paralelas, ¿qué tiempo se cuenta?", "El de la más larga", "Las demás ocurren dentro de ese tiempo."),
        ("¿Qué se prefiere primero ante un riesgo?", "Eliminarlo", "Es la medida más eficaz."),
    ],
    open_task=(
        "Planifica la construcción de un soporte de libros de cartón con estos datos de ejemplo: tareas medir 10 min, cortar 25 min, preparar la cinta 5 min (en paralelo con cortar), armar 20 min, revisar 5 min; presupuesto $4.000; gastos de cartón $1.700 y cinta $800. Escribe el cronograma, calcula el tiempo total y el saldo, y señala un riesgo con su medida de control.",
        "Tiempo: 10 + 25 + 20 + 5 = 60 minutos (la cinta va en paralelo); saldo: 4.000 − 1.700 − 800 = $1.500; riesgo: corte con tijeras, se controla con tijeras de punta roma y la mano lejos de la línea",
        ["ordena las tareas", "calcula bien el tiempo con la tarea paralela", "calcula el saldo", "señala un riesgo y su medida"],
        ["cronograma y cálculos"],
        ["sumar la tarea paralela", "no indicar una medida de control"],
        "Pregunta: «¿qué tareas se hacen a la vez?». Si las suma todas, pídele revisar cuáles son paralelas.",
    ),
    reinforce="Escribe los pasos para ordenar tu mesa de trabajo antes de cortar papel o cartón y cuánto tiempo estimas para cada uno.",
    extend="Explica por qué cambiar el diseño es una mejor medida de seguridad que pedirle a alguien que tenga más cuidado.",
)

# ------------------------------------------------------------------ OA 02, clase 5
reg(
    OA2, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los registros escritos en este cuaderno.",
    use="Aprenderé a planificar una prueba justa, a registrar y graficar los resultados y a decidir con evidencia si un prototipo cumple los criterios. Sirve para mejorar el producto con datos y no con impresiones.",
    prior=["Sé calcular un promedio.", "Sé calcular un porcentaje.", "Sé qué es un criterio con umbral."],
    explain=[
        "Un prototipo es una primera versión del producto que sirve para probar el diseño. Una prueba justa cambia una sola variable, que es lo que se quiere comparar (por ejemplo el grosor del cartón), y mantiene iguales las demás (las dimensiones, la persona que prueba, cómo se colocan los pesos). Se mide un resultado, como la cantidad de monedas que sostiene, y se repite la prueba tres veces o más.",
        "Los datos se anotan en una tabla y se calcula el promedio de cada prototipo. Un gráfico de barras compara bien los promedios de varios prototipos, porque cada barra representa uno. Para saber cuánto mejoró un prototipo se calcula (nuevo − anterior) × 100 ÷ anterior, que da el porcentaje de mejora. La eficiencia se calcula como lo logrado dividido entre lo gastado, por ejemplo monedas sostenidas por gramo de cartón.",
        "Con la evidencia se decide: el prototipo cumple si alcanza el umbral de cada criterio, no solo uno. Si falla, se cambia una cosa a la vez y se vuelve a probar. Una prueba sin procedimiento ni repeticiones no es evidencia, porque nadie puede repetirla.",
    ],
    vocab=[("prototipo", "primera versión de un producto para probar el diseño"), ("variable", "factor que puede cambiar en una prueba"), ("prueba justa", "prueba que cambia una sola variable"), ("porcentaje de mejora", "cuánto subió o bajó un resultado respecto del anterior"), ("evidencia", "datos que permiten decidir")],
    worked=[
        ("Reconocer una prueba injusta", "Un grupo compara un soporte de cartón de 2 mm con otro de 4 mm, pero el segundo además es más ancho. ¿La prueba es justa?", ["Cuento qué cambia: el grosor y el ancho.", "Con dos variables no sé a cuál se debe la diferencia."], "No es justa, porque cambian dos variables"),
        ("Calcular el porcentaje de mejora", "El prototipo A sostuvo 30, 34 y 32 monedas. El prototipo B sostuvo 40, 38 y 42. ¿Cuánto mejoró B respecto de A?", ["Promedio A = 96 ÷ 3 = 32. Promedio B = 120 ÷ 3 = 40.", "Mejora = (40 − 32) × 100 ÷ 32 = 25."], "Mejoró 25 %"),
    ],
    mistakes=[
        ("Cambiar dos cosas a la vez entre un prototipo y otro.", "No se sabe qué cambio causó el resultado.", "Cambia una variable y mantén iguales las demás."),
        ("Decidir con una sola prueba.", "Un resultado puede ser casualidad.", "Repite al menos tres veces y usa el promedio."),
    ],
    R=[
        ("En una prueba justa, ¿cuántas variables cambian a la vez: una o varias?", "Una", "Así se sabe a qué se debe la diferencia."),
        ("La cantidad de monedas que sostiene el soporte, ¿es lo que se cambia o lo que se registra como resultado?", "Lo que se registra como resultado", "Es el dato que se mide en la prueba."),
        ("Repetir la prueba tres veces, ¿ayuda a descubrir casualidades o solo gasta material?", "Ayuda a descubrir casualidades", "Si los resultados se parecen, el dato es más confiable."),
    ],
    C=[
        ("Un grupo prueba el cierre A con la mano de Ana y el cierre B con la mano de Luis, y B parece mejor. ¿Qué falla en la prueba? A) cambió la persona además del cierre B) usó pocos cierres", "A", "Hay dos variables distintas y no se sabe cuál influyó."),
        ("¿Qué gráfico compara mejor el promedio de tres prototipos: de barras o circular?", "De barras", "Cada barra muestra un prototipo y se comparan sus alturas."),
        ("El criterio es «soporta al menos 35 monedas». Un prototipo dio 36, 33 y 38. ¿Cumple en todas las pruebas?", "No", "En una prueba sostuvo 33, menos que el umbral."),
    ],
    A=[
        arith("El prototipo C sostuvo 21, 27, 24 y 24 monedas en cuatro pruebas. ¿Cuál es su promedio?", "(21+27+24+24)//4", "Se suman y se divide entre 4.", " monedas"),
        arith("El promedio del prototipo anterior fue 40 monedas y el del nuevo, 46. ¿Qué porcentaje mejoró?", "(46-40)*100//40", "Se calcula la diferencia respecto del anterior.", " %"),
        arith("Un prototipo sostiene 48 monedas y usa 12 g de cartón. ¿Cuántas monedas sostiene por cada gramo?", "48//12", "Se divide lo logrado entre lo gastado.", " monedas por gramo"),
    ],
    Z=[
        ("Un informe dice «el soporte aguanta 30 libros», sin decir cómo se colocaron ni cuántas veces se probó. ¿Qué le falta para ser evidencia? A) el procedimiento y las repeticiones B) una foto del soporte", "A", "Sin procedimiento nadie puede repetir la prueba."),
        ("Criterios: promedio de al menos 40 monedas y peso menor que 60 g. El prototipo 1 dio 30, 32 y 34 monedas y pesa 40 g. El prototipo 2 dio 41, 44 y 47 monedas y pesa 62 g. ¿Cuál cumple ambos criterios?", "Ninguno", "El primero promedia 32 y el segundo pesa 62 g, más que el límite."),
    ],
    D=[
        ("Prototipo viejo: promedio 24 monedas con 8 g de cartón. Prototipo nuevo: promedio 40 monedas con 10 g de cartón. ¿Cuál es más eficiente y cuánto vale cada eficiencia?", "El nuevo: 4 monedas por gramo contra 3", "40 ÷ 10 = 4 y 24 ÷ 8 = 3."),
        arith("Una puerta de cartón tardaba 50 segundos en abrirse con el cierre antiguo y 35 con el nuevo. ¿Qué porcentaje bajó el tiempo?", "(50-35)*100//50", "Se calcula la diferencia respecto del tiempo anterior.", " %"),
    ],
    ctx=ex("Tres ensayos de ejemplo de un puente de papel sostuvieron 14, 16 y 18 monedas. El criterio es un promedio de al menos 15. ¿Cuál es el promedio y cumple?", "16 monedas; sí cumple", "Se calcula (14 + 16 + 18) ÷ 3 = 16, mayor que 15.", calc="(14+16+18)//3"),
    sc=[
        ("En Tecnología: ¿Qué es una prueba justa?", "Una prueba que cambia una sola variable", "Así la diferencia se debe a ese cambio."),
        ("¿Qué datos hacen falta para calcular un porcentaje de mejora?", "El resultado anterior y el nuevo", "Se calcula la diferencia respecto del anterior."),
        ("¿Cuándo cumple un prototipo?", "Cuando alcanza el umbral de cada criterio", "Todos los criterios cuentan."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: portalápices A sostuvo 9, 11 y 10 lápices; portalápices B sostuvo 13, 14 y 12; B pesa 90 g y A pesa 70 g; criterios: promedio de al menos 12 lápices y peso de 100 g o menos. Registro 2: cierre de cartón viejo abrió y cerró sin romperse 20, 22 y 18 veces; el nuevo, 27, 30 y 27; criterio: promedio de al menos 25. Calcula los promedios y el porcentaje de mejora, y decide si cumple los criterios, explicando si la prueba fue justa.",
        "Registro 1: promedio A = 10, promedio B = 13; mejora = 30 %; B cumple ambos criterios (13 ≥ 12 y 90 g ≤ 100 g)",
        ["calcula bien los promedios", "calcula el porcentaje de mejora", "compara con cada criterio", "comenta si la prueba fue justa"],
        ["hoja con cálculos y decisión"],
        ["comparar solo un criterio", "olvidar las variables que se mantuvieron iguales"],
        "Pregunta: «¿qué mantuviste igual en las dos pruebas?». Si no lo menciona, pídele agregarlo.",
    ),
    reinforce="Con una hoja doblada como puente entre dos libros, prueba tres veces cuántas monedas sostiene, anota los datos y calcula el promedio.",
    extend="Explica cómo cambiarías una sola variable del puente de papel para mejorar su resistencia y cómo comprobarías la mejora.",
)
