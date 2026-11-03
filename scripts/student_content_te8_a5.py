"""Cuaderno del estudiante, 8.º básico Tecnología: OA 05 (análisis de soluciones existentes: destinatarios, aspectos técnicos y funcionales), clases 1 a 4.

Los productos son ejemplos generales de uso común (sin marcas ni fechas) y los datos numéricos son «de ejemplo», para practicar.
Seguridad: las tareas son de lectura, cálculo y escritura; no se manipulan herramientas ni materiales. Cifras enteras.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te8_a import reg
from student_lessons import arith, ex

OA5 = "TE08 OA 05"

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a identificar para quién fue creada una solución existente, a reconocer a quienes quedan fuera y a reconocer ideas de diseño universal. Sirve para analizar si una solución realmente responde a las personas que la necesitan.",
    prior=["Sé identificar una necesidad y a su usuario.", "Sé calcular porcentajes.", "Sé qué es un producto tecnológico."],
    explain=[
        "Examinar una solución existente es analizarla con criterios para entender si responde bien a la necesidad. El primer paso es identificar su destinatario, que es la persona o el grupo para quien fue diseñada. Una ficha del destinatario dice quién es, qué necesita, en qué lugar lo usa y qué límites tiene: fuerza, visión, audición, edad, dinero o acceso a internet.",
        "Una misma solución puede servir bien a unas personas y mal a otras. Los usuarios excluidos son quienes no pueden usarla bien porque el diseño no pensó en ellos: unas tijeras para mano derecha complican a una persona zurda. El diseño universal busca que el producto lo pueda usar la mayor cantidad de personas posible, sin adaptaciones especiales, como una rampa con baranda o un semáforo con luz y sonido. La accesibilidad es la facilidad con que todas las personas pueden usar algo.",
        "Para analizar se compara la ficha del destinatario con las características del producto. Si no calzan, se anota qué se podría adaptar. También se calcula qué porcentaje de las personas del grupo puede usar la solución sin ayuda: es el número de personas que pueden usarla × 100 ÷ el total del grupo.",
    ],
    vocab=[("destinatario", "persona o grupo para quien se diseñó la solución"), ("usuario excluido", "persona que no puede usar bien la solución"), ("diseño universal", "diseño que puede usar la mayor cantidad de personas posible"), ("accesibilidad", "facilidad para que todas las personas usen algo"), ("ficha del destinatario", "descripción de quién usa la solución y sus límites")],
    worked=[
        ("Reconocer el diseño universal", "Un semáforo tiene luz y también un aviso sonoro al cambiar. ¿A quiénes ayuda cada señal?", ["La luz ayuda a quien ve el color; el sonido ayuda a quien no ve o ve poco.", "Con las dos señales lo usan personas con distintas capacidades."], "La luz ayuda a quien ve y el sonido a quien no ve; juntos sirven a más personas"),
        ("Calcular quiénes pueden usar la solución", "Una aplicación para pedir horas en el consultorio exige un celular con internet. De 40 adultos mayores de ejemplo, 10 lo tienen. ¿Qué porcentaje puede usarla sin ayuda?", ["Personas que pueden: 10 de 40.", "10 × 100 ÷ 40 = 25."], "25 %"),
    ],
    mistakes=[
        ("Pensar que una solución «para todos» sirve a todas las personas.", "Quien la diseñó puede no haber pensado en algunas capacidades.", "Prueba con personas distintas y revisa quiénes quedan fuera."),
        ("Creer que la accesibilidad es solo para personas con discapacidad.", "Una rampa también ayuda a quien lleva un coche o una carga pesada.", "Mira todos los grupos que se benefician."),
    ],
    R=[
        ("El destinatario de un producto, ¿es la persona para quien se diseñó o quien lo vende?", "La persona para quien se diseñó", "Es quien se espera que lo use."),
        ("Unas tijeras diseñadas para mano derecha complican el uso a un estudiante zurdo. ¿Él es un usuario excluido o un destinatario previsto?", "Un usuario excluido", "El diseño no pensó en su mano."),
        ("El diseño universal, ¿piensa en que lo use la mayor cantidad de personas posible o una sola persona?", "La mayor cantidad de personas posible", "Es su principio."),
    ],
    C=[
        ("Una rampa con baranda en la entrada de una escuela beneficia a: A) personas en silla de ruedas, con coche de bebé, con muletas o con una carga pesada B) solo a quienes usan silla de ruedas", "A", "Una solución accesible ayuda a muchos grupos."),
        ("Una máquina de pago solo da instrucciones en una pantalla táctil, sin sonido. ¿A quiénes deja fuera? A) a personas ciegas o con baja visión B) a personas con buena vista", "A", "No pueden leer ni recibir las instrucciones."),
        ("Para diseñar una cuchara para niños de 2 años, ¿qué dato de la ficha del destinatario pesa más? A) su fuerza y habilidad de la mano B) el precio de la cuchara", "A", "Define el tamaño y la forma del mango."),
    ],
    A=[
        arith("En un curso de ejemplo de 200 estudiantes, 6 de cada 40 necesitan letra grande. ¿Cuántos estudiantes del curso la necesitan?", "200*6//40", "Se calcula cuántos hay en 200 si en cada 40 hay 6.", " estudiantes"),
        ("Une cada producto con su destinatario principal (P poca fuerza en la mano, C ciegas o baja visión, S silla de ruedas o coche): (1) cuchara con mango grueso, (2) semáforo con sonido, (3) rampa con baranda.", "1 P, 2 C, 3 S", "Cada producto responde a una necesidad distinta."),
        ("El mango de una manivela es delgado y corto, y a una persona con poca fuerza en las manos le cuesta girarla. ¿Qué cambio ayuda? A) un mango más grueso y largo con superficie antideslizante B) un mango más delgado y liso", "A", "Un mango grueso y antideslizante exige menos fuerza de agarre."),
    ],
    Z=[
        ("Una empresa dice que su botella es «para todos», pero la tapa exige girar con mucha fuerza. ¿Qué evidencia mostraría que no es para todos? A) personas con poca fuerza en las manos no logran abrirla en una prueba B) hay pocos colores", "A", "La prueba muestra quiénes quedan excluidos."),
        ("Un puente peatonal cambia escalones por una rampa tan empinada que nadie en silla de ruedas puede subirla solo. ¿Cumple su propósito de accesibilidad?", "No", "La rampa existe, pero sus destinatarios no pueden usarla."),
    ],
    D=[
        arith("Un cine de ejemplo tiene 240 asientos y 12 espacios para sillas de ruedas. ¿Qué porcentaje de la sala son espacios accesibles?", "12*100//240", "Se divide la parte entre el total y se multiplica por 100.", " %"),
        arith("Un grupo de 25 adultos mayores de ejemplo: 5 necesitan lentes para leer, 10 no manejan celular y 3 tienen poca audición, sin repetirse entre grupos. ¿Cuántos no tienen ninguna de esas limitaciones?", "25-(5+10+3)", "Se suman las limitaciones y se restan del total.", " personas"),
    ],
    ctx=ex("En una plaza hay una escalera de 8 escalones sin rampa. ¿Qué grupo queda excluido de usarla bien? A) personas que llevan un coche de bebé B) personas que caminan sin dificultad", "A", "Quienes llevan un coche necesitan una superficie sin escalones; quienes caminan sin dificultad suben igual."),
    sc=[
        ("¿Qué es un destinatario?", "La persona o grupo para quien se diseñó la solución", "Es quien se espera que la use."),
        ("¿Qué busca el diseño universal?", "Que lo pueda usar la mayor cantidad de personas posible", "Evita excluir sin adaptaciones especiales."),
        ("¿Cómo se calcula el porcentaje de quienes pueden usar una solución?", "Personas que pueden usarla por 100 dividido entre el total", "Compara una parte con el total."),
    ],
    open_task=(
        "Escoge un caso y completa una ficha. Caso 1: un buzón de calle con la ranura a 160 cm de altura. Caso 2: una tabla de cortar con una base que se desliza sobre la mesa. Caso 3: una caja de herramientas de 12 kg con un asa pequeña en el centro. Escribe el destinatario previsto, dos usuarios que podrían quedar excluidos y por qué, y una adaptación concreta de diseño.",
        "Caso 1: destinatario, adultos de estatura media; excluidos, niños y personas en silla de ruedas, porque no alcanzan la ranura; adaptación, una ranura baja o dos ranuras a distinta altura",
        ["identifica el destinatario previsto", "nombra dos excluidos con razón", "propone una adaptación concreta", "usa los datos del caso"],
        ["ficha del destinatario"],
        ["decir que el producto sirve a todos", "proponer una adaptación sin relación con el problema"],
        "Pregunta: «¿quién no podría usarlo y por qué?». Si no responde, pídele pensar en otra capacidad.",
    ),
    reinforce="Elige un objeto que uses y escribe quién lo diseñó pensando que lo usaría, y quién podría tener dificultades con él.",
    extend="Explica por qué una adaptación pensada para un grupo, como una rampa, puede ayudar también a otros grupos.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a analizar los aspectos técnicos de una solución: sus partes, sus materiales, sus uniones y su principio de funcionamiento. Sirve para entender cómo está hecha y por qué funciona.",
    prior=["Sé qué es un producto tecnológico.", "Sé que los materiales tienen propiedades.", "Sé multiplicar y dividir."],
    explain=[
        "Los aspectos técnicos describen cómo está hecha una solución y cómo funciona. Se identifican sus partes y la función de cada una, los materiales y sus propiedades, las uniones (pegadas, encajadas, atornilladas) y el principio de funcionamiento, que es la idea que hace que funcione. Un sistema técnico recibe entradas (fuerza, energía, materiales), las transforma en un proceso y entrega salidas.",
        "Los materiales se eligen por sus propiedades. El cartón es liviano y barato, pero se debilita con la humedad. La madera es liviana y fácil de trabajar, pero se hincha con el agua. El plástico es liviano y no se oxida. Algunos metales son resistentes y pesados, y pueden oxidarse. Una unión pegada es firme pero difícil de desarmar; una encajada se desarma y se repara más fácilmente.",
        "Muchas soluciones usan palancas, barras que giran en torno a un punto de apoyo. La ventaja mecánica es el brazo de esfuerzo dividido entre el brazo de carga; mide cuántas veces se reduce la fuerza necesaria. Si es 3, se hace un tercio de la fuerza que se necesitaría sin la palanca. Es un valor ideal: en la práctica, el roce lo reduce un poco.",
    ],
    vocab=[("sistema técnico", "conjunto de partes con entradas, proceso y salidas"), ("principio de funcionamiento", "idea que hace que funcione"), ("propiedad", "característica de un material, como resistencia o peso"), ("palanca", "barra que gira en torno a un punto de apoyo"), ("ventaja mecánica", "brazo de esfuerzo dividido entre brazo de carga")],
    worked=[
        ("Analizar un sistema técnico", "Una pinza de ropa sujeta una prenda. Describe su entrada, proceso y salida.", ["Entrada: la fuerza de los dedos para abrirla.", "Proceso: la palanca abre los extremos y un resorte los cierra. Salida: la prenda queda sujeta."], "Entrada: fuerza de los dedos; proceso: palanca y resorte; salida: prenda sujeta"),
        ("Calcular la ventaja mecánica", "En una carretilla de ejemplo, las manos están a 120 cm del eje de la rueda y el centro de la carga a 40 cm. ¿Cuál es la ventaja mecánica?", ["Divido el brazo de esfuerzo entre el brazo de carga.", "120 ÷ 40 = 3."], "3: se necesita un tercio de la fuerza"),
    ],
    mistakes=[
        ("Describir solo cómo se ve el producto.", "El aspecto técnico explica cómo funciona, no cómo luce.", "Nombra partes, materiales, uniones y el principio de funcionamiento."),
        ("Elegir un material sin mirar dónde se usará.", "El cartón a la lluvia se deshace.", "Relaciona la propiedad del material con las condiciones de uso."),
    ],
    R=[
        ("En un sistema técnico, lo que se recibe, como fuerza o energía, ¿es la entrada o la salida?", "La entrada", "Es lo que ingresa al sistema."),
        ("Una unión pegada, ¿se desarma fácilmente o es difícil de desarmar?", "Es difícil de desarmar", "Al pegar las partes quedan fijas."),
        ("Un material que se debilita con la humedad, ¿es el cartón o el plástico?", "El cartón", "El agua ablanda sus fibras."),
    ],
    C=[
        ("Una pieza quedará a la intemperie, con lluvia frecuente. ¿Qué material conviene? A) plástico B) cartón sin proteger", "A", "El plástico no se debilita con la humedad."),
        ("En una pinza de ropa, ¿qué función cumple el resorte? A) hace que la pinza vuelva a cerrarse y apriete B) hace que la pinza se abra sola", "A", "Mantiene los extremos cerrados presionando la prenda."),
        ("Una carretilla tiene ventaja mecánica 3. ¿Qué significa? A) se hace un tercio de la fuerza que se haría sin ella B) se hace el triple de la fuerza", "A", "La ventaja mecánica reduce la fuerza necesaria."),
    ],
    A=[
        arith("En una carretilla de ejemplo, las manos están a 100 cm del eje y la carga a 25 cm. ¿Cuál es la ventaja mecánica?", "100//25", "Se divide el brazo de esfuerzo entre el brazo de carga.", ""),
        arith("Una palanca de ventaja mecánica 4 levanta una carga equivalente a 80 kg. ¿Cuántos kilos de fuerza se necesitan?", "80//4", "Se divide la carga entre la ventaja mecánica.", " kg"),
        ("Asigna el material (M metal, C cartón, P plástico): (1) resistente y pesado, (2) liviano y se debilita con la humedad, (3) liviano y no se oxida.", "1 M, 2 C, 3 P", "Cada propiedad corresponde a un material distinto."),
    ],
    Z=[
        ("Un grupo afirma que una pieza de cartón sirve como asiento para una plaza al aire libre. ¿Qué dato técnico lo refuta? A) el cartón se debilita con la humedad B) el cartón es liviano", "A", "La lluvia lo deterioraría."),
        ("Una pinza se rompe en la unión de sus dos partes cuando se aprieta mucho. ¿Qué aspecto técnico conviene analizar primero? A) la unión y el material en ese punto B) el precio del material", "A", "La falla ocurrió en ese lugar."),
    ],
    D=[
        arith("Para levantar una carga de 90 kg con una palanca de ventaja mecánica 3, ¿cuántos kilos de fuerza se necesitan?", "90//3", "Se divide la carga entre la ventaja mecánica.", " kg"),
        ("La carretilla A tiene ventaja mecánica 4 y la B, 3. Para una carga de 48 kg, ¿qué fuerza se necesita en cada una?", "A 12 kg y B 16 kg", "48 ÷ 4 = 12 y 48 ÷ 3 = 16, así que A requiere menos fuerza."),
    ],
    ctx=ex("En un balancín de plaza, ¿cuál es la entrada, el proceso y la salida? Elige la descripción correcta: A) entrada, el peso de las personas; proceso, el giro en el punto de apoyo; salida, subir y bajar los extremos B) entrada, subir y bajar; proceso, el peso; salida, el punto de apoyo", "A", "El peso entra, la barra gira y los extremos suben y bajan."),
    sc=[
        ("¿Qué es el principio de funcionamiento?", "La idea que hace que funcione", "Explica por qué el objeto cumple su función."),
        ("¿Cómo se calcula la ventaja mecánica?", "Brazo de esfuerzo dividido entre brazo de carga", "Mide cuánto se reduce la fuerza necesaria."),
        ("¿Qué partes tiene un sistema técnico?", "Entradas, proceso y salidas", "Transforma lo que recibe."),
    ],
    open_task=(
        "Escoge un objeto y completa una ficha técnica. Objeto 1: pinza de ropa con dos partes de plástico y un resorte metálico unidos por un pasador. Objeto 2: carretilla de jardín con caja de metal, dos mangos de madera, una rueda de goma y un eje; manos a 100 cm del eje y carga a 25 cm. Escribe sus partes con su función, los materiales con una propiedad, el tipo de unión, el principio de funcionamiento y, si corresponde, la ventaja mecánica.",
        "Objeto 2: caja de metal (soporta la carga), mangos de madera (agarre), rueda (rueda), eje (apoya); ventaja mecánica 100 ÷ 25 = 4; principio: palanca con el eje como apoyo",
        ["nombra partes y su función", "relaciona materiales con propiedades", "describe uniones y principio", "calcula la ventaja mecánica si corresponde"],
        ["ficha técnica"],
        ["describir solo el aspecto", "calcular la ventaja mecánica al revés"],
        "Pregunta: «¿por qué funciona?». Debe nombrar el principio, no solo las partes.",
    ),
    reinforce="Observa un objeto sencillo de tu casa con una parte que se mueve y nombra su entrada, su proceso y su salida.",
    extend="Explica por qué dos objetos que cumplen la misma función pueden estar hechos con materiales distintos.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a analizar los aspectos funcionales de una solución: su función principal y secundarias, su desempeño, su ergonomía, su mantención y su costo de uso. Sirve para juzgar qué tan bien funciona en el uso real.",
    prior=["Sé analizar partes y materiales de un objeto.", "Sé calcular costos por unidad.", "Sé qué es un indicador."],
    explain=[
        "Los aspectos funcionales describen qué hace la solución y qué tan bien lo hace al usarla. La función principal es el motivo por el cual existe; las funciones secundarias son otras tareas que también cumple. Una mochila con ruedas tiene como función principal transportar útiles, y como secundarias rodar y distribuir el peso.",
        "El desempeño es qué tan bien cumple su función, medido con un indicador: cuántas hojas une una engrapadora sin atascarse, cuánto tiempo mantiene frío un líquido una botella o cuántos kilos soporta una repisa. La ergonomía es el ajuste del objeto al cuerpo de quien lo usa: esfuerzo, postura, agarre. También se analiza la seguridad, la facilidad de mantención y reparación, y el costo de uso.",
        "El costo de uso compara el gasto con el tiempo o las veces que se aprovecha: costo por año = precio ÷ años de duración; costo por uso = precio ÷ cantidad de usos. Una solución barata puede salir cara si dura poco. Los datos del fabricante conviene comprobarlos con una prueba.",
    ],
    vocab=[("función principal", "motivo por el que existe el producto"), ("función secundaria", "otra tarea que también cumple"), ("desempeño", "qué tan bien cumple su función, medido con un indicador"), ("ergonomía", "ajuste del objeto al cuerpo de quien lo usa"), ("costo de uso", "gasto dividido entre el tiempo o las veces de uso")],
    worked=[
        ("Separar función principal y secundarias", "Una mochila con ruedas permite transportar útiles, rodar y repartir el peso. ¿Cuál es la función principal?", ["Pregunto para qué existe: para llevar útiles.", "Rodar y repartir el peso son ayudas que mejoran cómo lo hace."], "Principal: transportar útiles; secundarias: rodar y repartir el peso"),
        ("Calcular el costo por año", "Una mochila de ejemplo cuesta $24.000 y dura 4 años. ¿Cuál es su costo por año?", ["Divido el precio entre los años.", "24.000 ÷ 4 = 6.000."], "$6.000 por año"),
    ],
    mistakes=[
        ("Elegir siempre el producto más barato.", "Si dura poco, cuesta más por año.", "Compara el costo por año o por uso."),
        ("Creer lo que dice el fabricante sin comprobarlo.", "Los datos pueden no coincidir con el uso real.", "Mide el desempeño con una prueba."),
    ],
    R=[
        ("La función principal de un objeto, ¿es para qué fue creado o un detalle extra?", "Para qué fue creado", "Es el motivo principal de su existencia."),
        ("La ergonomía, ¿es el ajuste del objeto al cuerpo de quien lo usa o su precio?", "El ajuste al cuerpo de quien lo usa", "Considera esfuerzo, postura y agarre."),
        ("El desempeño, ¿se mide con un indicador o solo con la opinión de quien vende?", "Con un indicador", "Un indicador permite comprobarlo."),
    ],
    C=[
        ("¿Cuál es una función secundaria de una mochila con ruedas? A) rodar para no cargar el peso en la espalda B) llevar útiles", "A", "Llevar útiles es la principal; rodar la complementa."),
        ("¿Qué indicador mide el desempeño de una engrapadora de escritorio? A) cuántas hojas une sin atascarse B) cuánto cuesta en la tienda", "A", "Mide qué tan bien cumple su función."),
        ("Un producto sin repuestos, ¿es más fácil o más difícil de mantener?", "Más difícil", "Si algo se daña, no se puede reemplazar solo esa pieza."),
    ],
    A=[
        arith("Una mochila de ejemplo cuesta $30.000 y dura 6 años. ¿Cuál es su costo por año?", "30000//6", "Se divide el precio entre los años de duración.", " pesos por año"),
        arith("Unos zapatos de ejemplo cuestan $36.000 y duran 18 meses. ¿Cuál es el costo por mes?", "36000//18", "Se divide el precio entre los meses de duración.", " pesos por mes"),
        ex("La mochila A cuesta $18.000 y dura 3 años; la mochila B cuesta $30.000 y dura 6 años. ¿Cuál tiene menor costo por año y cuánto se ahorra por año?", "La B; ahorra $1.000 por año", "A cuesta 6.000 por año y B cuesta 5.000 por año.", calc="18000//3-30000//6"),
    ],
    Z=[
        ("Un producto barato recibe reclamos porque se rompe a los 2 meses. ¿Qué criterios funcionales falla? A) la durabilidad y el costo de uso B) la apariencia", "A", "Dura muy poco y por lo tanto su costo por mes resulta alto."),
        ("Una botella dice mantener el agua fría 12 horas, pero en tu prueba la mantuvo 5. ¿Qué haces con la afirmación del fabricante? A) comprobarla con una prueba midiendo la temperatura cada hora y reportar tus datos B) aceptarla sin más", "A", "Las afirmaciones se verifican con evidencia."),
    ],
    D=[
        arith("Un cartucho de tinta de ejemplo cuesta $12.000 y rinde 300 páginas. ¿Cuál es el costo por página?", "12000//300", "Se divide el precio entre las páginas que rinde.", " pesos por página"),
        ("La linterna A cuesta $3.000 y gasta $1.000 en pilas por mes. La linterna B cuesta $7.000 y gasta $400 por mes. ¿Desde qué mes completo el costo total de B es menor que el de A?", "Desde el mes 7", "En el mes 7, A suma 10.000 y B suma 9.800; en el mes 6, A suma 9.000 y B suma 9.400."),
    ],
    ctx=ex("Una botella reutilizable de ejemplo cuesta $6.000 y la usarás 300 veces. ¿Cuál es su costo por uso?", "$20", "Se calcula 6.000 ÷ 300 = 20.", calc="6000//300"),
    sc=[
        ("¿Qué mide el desempeño?", "Qué tan bien cumple su función", "Se mide con un indicador."),
        ("¿Cómo se calcula el costo por año?", "Precio dividido entre los años de duración", "Compara el gasto con el tiempo de uso."),
        ("¿Qué es la ergonomía?", "El ajuste del objeto al cuerpo de quien lo usa", "Evita esfuerzos y malas posturas."),
    ],
    open_task=(
        "Compara dos productos de ejemplo. Mesa plegable A: $24.000, dura 8 años, pesa 6 kg y se pliega en 10 segundos. Mesa plegable B: $15.000, dura 3 años, pesa 9 kg y se pliega en 40 segundos. Escribe la función principal, calcula el costo por año de cada una, compara su desempeño (peso y tiempo de plegado) y recomienda una para una persona que la guardará y sacará todos los días, justificando con datos.",
        "Función principal: servir de superficie de trabajo plegable. A cuesta $3.000 por año y B $5.000; A pesa 3 kg menos y se pliega en 30 segundos menos. Recomiendo A porque cuesta menos por año y es más fácil de guardar cada día",
        ["indica la función principal", "calcula el costo por año de cada mesa", "compara peso y tiempo", "recomienda con datos"],
        ["tabla comparativa y recomendación"],
        ["elegir solo por el precio", "recomendar sin datos"],
        "Pregunta: «¿qué dato apoya tu recomendación?». Debe nombrar al menos dos.",
    ),
    reinforce="Elige un objeto de tu casa y escribe su función principal, una secundaria y un indicador con el que medirías su desempeño.",
    extend="Explica por qué el costo por año puede cambiar la decisión de compra.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y las matrices escritas en este cuaderno.",
    use="Aprenderé a comparar soluciones existentes con una matriz ponderada según el destinatario y a escribir una recomendación con datos. Sirve para decidir con argumentos cuál solución es mejor para cada persona.",
    prior=["Sé analizar destinatarios, aspectos técnicos y funcionales.", "Sé calcular puntajes ponderados.", "Sé qué es un criterio."],
    explain=[
        "Para decidir entre soluciones se arma una matriz de comparación. Las filas son las soluciones y las columnas, los criterios: costo, durabilidad, facilidad de uso, seguridad y otros. Cada solución recibe un puntaje de 1 a 5 en cada criterio, donde 5 es el mejor cumplimiento. Los puntajes salen de datos: medidas, pruebas y fichas técnicas, y no de gustos.",
        "Cada criterio recibe un peso según qué tan importante es para el destinatario. El puntaje ponderado de la solución es la suma de peso × puntaje de cada criterio. Cuando cambia el destinatario, cambian los pesos y puede cambiar la mejor solución. Algunos criterios son obligatorios, como la seguridad: si una solución no alcanza el mínimo, se descarta aunque tenga un puntaje total alto.",
        "La recomendación dice qué solución se elige, para quién, con dos o tres razones basadas en datos, qué limitaciones tiene y qué se elegiría si el destinatario fuera otro. Si dos soluciones empatan, se aplica un criterio de desempate que se acordó antes de calcular.",
    ],
    vocab=[("matriz de comparación", "tabla de soluciones y criterios con puntajes"), ("peso", "importancia de un criterio para el destinatario"), ("criterio obligatorio", "mínimo que debe cumplirse para no descartar la solución"), ("recomendación", "decisión justificada con datos y para un destinatario"), ("desempate", "regla acordada antes para resolver empates")],
    worked=[
        ("Comparar según el destinatario", "Puntajes (costo, durabilidad, facilidad): solución A 2, 4 y 5; solución B 5, 3 y 2. Pesos para una estudiante con poco dinero: costo 3, durabilidad 1, facilidad 1. ¿Cuál se recomienda?", ["A: 3×2 + 1×4 + 1×5 = 6 + 4 + 5 = 15.", "B: 3×5 + 1×3 + 1×2 = 15 + 3 + 2 = 20."], "La solución B, con 20 puntos contra 15"),
        ("Cambiar el destinatario", "Con los mismos puntajes, un adulto mayor da pesos costo 1, durabilidad 1 y facilidad 3. ¿Cuál se recomienda?", ["A: 1×2 + 1×4 + 3×5 = 2 + 4 + 15 = 21.", "B: 1×5 + 1×3 + 3×2 = 5 + 3 + 6 = 14."], "La solución A, con 21 puntos contra 14"),
    ],
    mistakes=[
        ("Usar siempre los mismos pesos para cualquier destinatario.", "Lo importante cambia según quién use la solución.", "Define los pesos pensando en el destinatario."),
        ("Elegir la solución de mayor puntaje aunque falle un criterio obligatorio.", "Un puntaje total alto puede ocultar un riesgo grave.", "Descarta primero las que no cumplen los mínimos."),
    ],
    R=[
        ("Cuando cambia el destinatario, ¿pueden cambiar los pesos de los criterios?", "Sí", "Lo importante depende de quién use la solución."),
        ("En una recomendación, ¿se escriben razones con datos o basta con decir «me gusta»?", "Razones con datos", "La decisión debe poder comprobarse."),
        ("Un puntaje ponderado mayor, ¿indica un mejor o un peor cumplimiento de lo que más importa?", "Un mejor cumplimiento", "Los criterios de más peso influyen más."),
    ],
    C=[
        ("Una solución cuesta poco, pero sus botones son muy pequeños para una persona con poca precisión en las manos. Para esa persona, ¿qué criterio debe pesar más? A) facilidad de uso B) costo", "A", "Es el criterio que define si puede usarla."),
        ("Alguien escribe: «el producto B es mejor». ¿Qué falta? A) para quién y las razones con datos B) un adjetivo", "A", "Una recomendación se justifica con el destinatario y la evidencia."),
        ("Seguridad es un criterio obligatorio con mínimo 3. Una solución tiene seguridad 2 y un puntaje total muy alto. ¿Qué se hace? A) se descarta B) se recomienda por su puntaje", "A", "No cumple el mínimo obligatorio."),
    ],
    A=[
        arith("Pesos: costo 2, seguridad 3, facilidad 1. La solución P tiene puntajes 4, 3 y 2. ¿Cuál es su puntaje ponderado?", "2*4+3*3+1*2", "Se multiplica cada puntaje por su peso y se suman.", " puntos"),
        ex("Con los mismos pesos (2, 3 y 1), la solución Q tiene puntajes 5, 2 y 4. ¿Cuál es su puntaje y supera a P, que obtuvo 19?", "20; sí supera a P", "Q suma 10 + 6 + 4 = 20, mayor que 19.", calc="2*5+3*2+1*4"),
        arith("Con puntajes de hasta 5 y pesos 2, 2 y 1, una solución obtiene 4, 3 y 5. ¿Qué porcentaje del máximo posible logra?", "(2*4+2*3+1*5)*100//25", "El máximo es 5 × 5 = 25 y obtiene 19.", " %"),
    ],
    Z=[
        ("Puntajes (costo, durabilidad, facilidad): C 4, 2 y 3; D 2, 5 y 4. El destinatario es una escuela que usará el producto a diario durante años, con pesos costo 1, durabilidad 3 y facilidad 1. ¿Cuál se recomienda?", "D, con 21 puntos contra 13", "C suma 4 + 6 + 3 = 13 y D suma 2 + 15 + 4 = 21."),
        ("Un grupo recomienda el producto de mayor puntaje sin notar que su seguridad es 1 de 5. ¿Qué error cometió? A) dejó que otros criterios compensaran un criterio obligatorio B) usó pesos distintos para cada criterio", "A", "La seguridad no puede compensarse con un buen precio."),
    ],
    D=[
        ex("Pesos: accesibilidad 3, costo 2, durabilidad 1. X tiene puntajes 5, 2 y 3; Y tiene 3, 5 y 4; Z tiene 4, 4 y 3. En caso de empate gana la de mayor accesibilidad. ¿Cuál se recomienda?", "Z", "X suma 22, Y suma 23 y Z suma 23; Z y Y empatan y Z tiene accesibilidad 4 contra 3."),
        ex("Pesos: seguridad 2, costo 3, facilidad 3. Seguridad es obligatoria con mínimo 3. M tiene puntajes 4, 2 y 2; N tiene 2, 5 y 5. ¿Cuál se recomienda?", "M", "N suma 34 y M suma 20, pero N no cumple el mínimo de seguridad y se descarta."),
    ],
    ctx=ex("Matriz de ejemplo para una mochila: pesos ergonomía 3 y costo 2. La mochila R tiene ergonomía 4 y costo 3; la mochila S tiene ergonomía 2 y costo 5. ¿Cuál gana y con cuántos puntos?", "R, con 18 puntos contra 16", "R suma 12 + 6 = 18 y S suma 6 + 10 = 16."),
    sc=[
        ("¿Qué es un criterio obligatorio?", "Un mínimo que debe cumplirse para no descartar la solución", "Evita aceptar soluciones peligrosas."),
        ("¿Por qué cambian los pesos entre destinatarios?", "Porque cada destinatario valora distinto los criterios", "La importancia depende de quién usa la solución."),
        ("¿Qué incluye una recomendación?", "Solución, destinatario y razones con datos", "Se justifica con evidencia."),
    ],
    open_task=(
        "Compara dos soluciones de ejemplo para guardar útiles en una sala. A: cajonera de cartón con puntajes costo 5, durabilidad 2 y facilidad 4. B: estante de madera con costo 2, durabilidad 5 y facilidad 3. Calcula el puntaje ponderado para dos destinatarios: (1) un curso de 1.º básico con poco presupuesto, con pesos costo 3, durabilidad 1 y facilidad 2; (2) una biblioteca escolar que lo usará 10 años, con pesos costo 1, durabilidad 3 y facilidad 1. Escribe una recomendación para cada uno.",
        "Curso: A 25 y B 17, se recomienda A. Biblioteca: A 15 y B 20, se recomienda B porque durará 10 años",
        ["calcula los cuatro puntajes", "recomienda una solución por destinatario", "justifica con datos", "explica por qué cambia la recomendación"],
        ["matriz y recomendación"],
        ["usar los mismos pesos para ambos destinatarios", "recomendar sin explicar"],
        "Pregunta: «¿qué cambió entre los dos destinatarios?». Debe responder que los pesos.",
    ),
    reinforce="Compara dos objetos de tu casa para una misma tarea y pon puntajes de 1 a 5 en tres criterios.",
    extend="Explica por qué una solución muy buena para un destinatario puede ser mala para otro.",
)
