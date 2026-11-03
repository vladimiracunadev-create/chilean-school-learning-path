"""Cuaderno del estudiante, 8.º básico Tecnología: OA 03 (evaluación técnica y mejora de productos), clases 1 a 5.

Seguridad: las tareas son de lectura, cálculo y escritura; si se hacen pruebas, solo con papel, cartón, monedas, libros livianos y cordel, nunca con cargas que puedan caer sobre los pies.
Cifras enteras. Los casos y los datos de pruebas son inventados («de ejemplo») para practicar y no nombran marcas ni personas reales.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te8_a import reg
from student_lessons import arith, ex

OA3 = "TE08 OA 03"

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a construir un instrumento de evaluación con criterios propios y técnicos, niveles descritos y pesos, y a calcular un porcentaje de logro. Sirve para evaluar un producto con una regla clara y no con gustos.",
    prior=["Sé que un criterio técnico se mide y uno propio depende de preferencias.", "Sé calcular porcentajes.", "Sé calcular un puntaje con pesos."],
    explain=[
        "Evaluar un producto es compararlo con criterios. Los criterios técnicos se miden con una prueba: cuánto peso soporta, cuántos gramos pesa, cuánto dura. Los criterios propios dependen de lo que valora el usuario o el equipo: comodidad, apariencia, facilidad de uso. Un criterio propio se vuelve medible si se pregunta a varias personas y se calcula un promedio, por ejemplo con una escala de 1 a 5.",
        "Un instrumento de evaluación, como una rúbrica o una lista de cotejo, es una tabla con los criterios, los niveles de logro y el peso de cada criterio. Cada nivel se describe con algo que se puede observar, como «soporta 5 libros». Así dos personas que evalúan lo mismo llegan al mismo puntaje. El peso muestra qué tan importante es el criterio; en un juguete, la seguridad debe pesar más que la apariencia.",
        "El puntaje ponderado de un criterio es peso × nivel. El puntaje máximo es el nivel más alto multiplicado por la suma de los pesos. El porcentaje de logro es puntaje obtenido × 100 ÷ puntaje máximo. Se acuerda antes una regla de decisión, por ejemplo «es aceptable desde 75 % y sin fallas de seguridad».",
    ],
    vocab=[("rúbrica", "tabla con criterios y niveles de logro descritos"), ("nivel de logro", "grado en que se cumple un criterio"), ("peso", "importancia de un criterio"), ("puntaje ponderado", "peso multiplicado por el nivel obtenido"), ("regla de decisión", "condición acordada para aceptar el producto")],
    worked=[
        ("Calcular el porcentaje de logro", "Una rúbrica tiene niveles de 1 a 3 y tres criterios: resistencia (peso 3), comodidad (peso 1) y apariencia (peso 1). Un producto obtiene los niveles 2, 3 y 3. ¿Cuál es su porcentaje de logro?", ["Obtenido: 3×2 + 1×3 + 1×3 = 6 + 3 + 3 = 12.", "Máximo: 3 × (3 + 1 + 1) = 15. Logro: 12 × 100 ÷ 15."], "80 %"),
        ("Hacer medible un criterio propio", "El criterio propio es «el asa es cómoda». ¿Cómo se vuelve medible?", ["Pido a 10 usuarios que califiquen la comodidad de 1 a 5.", "Fijo un umbral: el promedio debe ser al menos 4."], "Con una escala de 1 a 5 y un promedio de al menos 4"),
    ],
    mistakes=[
        ("Describir los niveles con palabras como «bien» y «mal».", "Dos evaluadores pueden entenderlas distinto.", "Describe cada nivel con algo observable o medible."),
        ("Darle el mismo peso a todos los criterios.", "Un criterio de seguridad queda tan importante como el color.", "Asigna más peso a lo que más importa para el usuario."),
    ],
    R=[
        ("¿Cuál es un criterio técnico? A) resiste 3 kg sin romperse B) a Marcela le gusta el color", "A", "Se puede comprobar con una prueba; el gusto es personal."),
        ("En una rúbrica, un peso mayor en un criterio, ¿significa que es más importante o más fácil?", "Más importante", "El peso multiplica el puntaje del criterio."),
        ("Un nivel de logro de una rúbrica, ¿describe lo que se observa o lo que a quien evalúa le gustaría que pasara?", "Lo que se observa", "Así la evaluación es repetible."),
    ],
    C=[
        ("Para evaluar el criterio propio «es cómodo», ¿qué da un dato? A) pedir a 10 usuarios que lo califiquen de 1 a 5 y calcular el promedio B) preguntar a una sola persona cómo se siente", "A", "Varias respuestas permiten calcular un promedio más confiable."),
        ("Dos evaluadores deben llegar al mismo puntaje con la misma rúbrica. ¿Qué lo permite? A) niveles descritos con cosas observables B) niveles con palabras como «bien» y «mal»", "A", "Lo observable se entiende igual para todos."),
        ("La regla de decisión dice «aceptable desde 75 %». Un producto logra 70 %. ¿Es aceptable?", "No", "70 es menor que 75."),
    ],
    A=[
        arith("Pesos: resistencia 4, seguridad 2, comodidad 1 y niveles de 1 a 3. Un producto obtiene los niveles 3, 2 y 1. ¿Cuál es su puntaje ponderado?", "4*3+2*2+1*1", "Se multiplica cada nivel por su peso y se suman los resultados.", " puntos"),
        arith("Un producto obtuvo 24 puntos de un máximo de 30. ¿Cuál es su porcentaje de logro?", "24*100//30", "Se divide lo obtenido entre el máximo y se multiplica por 100.", " %"),
        arith("Una rúbrica sin pesos tiene 4 criterios con niveles de 1 a 4. Un producto obtuvo los niveles 3, 4, 2 y 3. ¿Qué porcentaje de logro tiene?", "(3+4+2+3)*100//16", "El máximo es 4 × 4 = 16 y se obtuvieron 12 puntos.", " %"),
    ],
    Z=[
        ("Para un juguete de niños pequeños, un grupo da peso 3 a «se ve bonito» y peso 1 a «es seguro». ¿Qué problema tiene? A) pondera menos un criterio esencial B) los pesos de los criterios deben sumar 100", "A", "La seguridad debería pesar más que la apariencia."),
        ("Con pesos seguridad 3 y belleza 1, el producto M tiene niveles seguridad 1 y belleza 3; el producto N tiene seguridad 3 y belleza 1. ¿Cuál gana y con cuántos puntos?", "N, con 10 puntos contra 6", "N suma 9 + 1 = 10 y M suma 3 + 3 = 6."),
    ],
    D=[
        arith("Pesos: resistencia 4, seguridad 4, comodidad 2, con niveles de 1 a 3. Un producto obtiene los niveles 3, 2 y 2. ¿Qué porcentaje de logro tiene?", "(4*3+4*2+2*2)*100//30", "Obtiene 24 de un máximo de 3 × 10 = 30.", " %"),
        ("Regla: aceptable si el logro es al menos 75 % y la seguridad está en el nivel 3. Producto 1: 80 % y seguridad nivel 2. Producto 2: 72 % y seguridad nivel 3. Producto 3: 78 % y seguridad nivel 3. ¿Cuál es aceptable?", "El producto 3", "Solo el 3 cumple las dos condiciones a la vez."),
    ],
    ctx=ex("Evalúas un organizador de escritorio de ejemplo con niveles de 1 a 3 y pesos 3 para resistencia y 1 para orden. Obtiene nivel 2 en resistencia y nivel 3 en orden. ¿Cuál es su porcentaje de logro?", "75 %", "Obtiene 3×2 + 1×3 = 9 de un máximo de 3 × 4 = 12; 9 × 100 ÷ 12 = 75.", calc="9*100//12"),
    sc=[
        ("¿Para qué sirve el peso de un criterio?", "Para mostrar su importancia", "Un peso mayor aumenta su efecto en el puntaje."),
        ("¿Qué es una regla de decisión?", "Una condición acordada para aceptar el producto", "Se define antes de evaluar."),
        ("¿Cómo se calcula el porcentaje de logro?", "Puntaje obtenido por 100 dividido entre el máximo", "Compara lo logrado con lo posible."),
    ],
    open_task=(
        "Evalúa este producto de ejemplo, un portalápices de cartón, con una rúbrica de niveles de 1 a 3 y estos pesos: resistencia 3, seguridad 3, comodidad 2, apariencia 1. Datos de ejemplo: soportó 5 lápices y cayó con 7 (nivel 2); no tiene bordes cortantes (nivel 3); 10 usuarios lo calificaron de 1 a 5 y el promedio fue 4 (nivel 3); la apariencia fue nivel 1. Calcula el puntaje obtenido, el máximo y el porcentaje de logro, y decide con la regla «aceptable desde 75 %».",
        "Obtenido: 3×2 + 3×3 + 2×3 + 1×1 = 22; máximo: 3 × 9 = 27; logro 81 %; es aceptable porque supera 75 %",
        ["calcula el puntaje ponderado", "calcula el máximo y el porcentaje", "aplica la regla de decisión", "distingue criterios técnicos y propios"],
        ["tabla de cálculo y decisión"],
        ["olvidar multiplicar por el peso", "calcular mal el máximo"],
        "Pregunta: «¿cuál es el mayor puntaje posible?». Si no sabe, pídele multiplicar el nivel más alto por la suma de pesos.",
    ),
    reinforce="Elige un objeto de tu casa y escribe dos criterios técnicos y dos propios con un nivel descrito para cada uno.",
    extend="Explica por qué una regla de decisión debe acordarse antes de evaluar.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los registros escritos en este cuaderno.",
    use="Aprenderé a analizar datos de prueba con la mediana, a reconocer un dato atípico y a verificar medidas con una tolerancia. Sirve para evaluar la calidad técnica de un producto con datos más fiables.",
    prior=["Sé calcular el promedio y el rango.", "Sé calcular un porcentaje.", "Sé que una prueba debe repetirse."],
    explain=[
        "Con los datos de varias pruebas se calcula la media, que es el promedio, y la mediana, que es el valor central cuando los datos se ordenan de menor a mayor. Un dato atípico es un valor muy distinto de los demás. Si hay uno, la media sube o baja mucho y puede engañar; la mediana casi no cambia. Un dato atípico no se borra en silencio: primero se revisa si hubo un error, como un peso mal colocado, y se informa lo que se hizo.",
        "Muchos productos deben tener medidas precisas. La tolerancia es la diferencia máxima aceptada entre la medida de diseño y la medida real, y se escribe con ±. El error es la diferencia entre ambas medidas, sin importar el signo. La pieza cumple si el error es menor o igual que la tolerancia. El error relativo porcentual es error × 100 ÷ medida de diseño y permite comparar piezas de tamaños distintos.",
        "Una evaluación técnica combina estas herramientas: se miden varias veces, se miran la media y la mediana, se analizan los datos atípicos y se comparan las medidas con la tolerancia. Todo con unidades y con el procedimiento escrito para poder repetirlo.",
    ],
    vocab=[("mediana", "valor central de los datos ordenados"), ("dato atípico", "valor muy distinto de los demás"), ("tolerancia", "diferencia máxima aceptada entre la medida de diseño y la real"), ("error", "diferencia entre la medida real y la de diseño"), ("error relativo", "error como porcentaje de la medida de diseño")],
    worked=[
        ("Media, mediana y dato atípico", "Cinco pruebas de resistencia dieron 18, 20, 19, 43 y 20 g. Calcula la media y la mediana. ¿Hay un dato atípico?", ["Media: 18 + 20 + 19 + 43 + 20 = 120; 120 ÷ 5 = 24 g.", "Ordeno: 18, 19, 20, 20, 43; el central es 20. El 43 es muy distinto de los demás."], "Media 24 g, mediana 20 g; el 43 es atípico"),
        ("Verificar una tolerancia", "Una pieza se diseñó de 120 mm con tolerancia de ±2 mm. Se midieron 118, 121 y 123 mm. ¿Cuáles cumplen?", ["Errores: 2, 1 y 3 mm.", "Cumple si el error es 2 mm o menos."], "Cumplen 118 mm y 121 mm; no cumple 123 mm"),
    ],
    mistakes=[
        ("Borrar un dato atípico sin revisar ni informar.", "Se pierde evidencia y se puede engañar a quien lee el informe.", "Revisa si hubo un error, y informa lo que decidiste y por qué."),
        ("Calcular la mediana sin ordenar los datos.", "El valor central solo tiene sentido con datos ordenados.", "Ordena de menor a mayor antes de buscar el centro."),
    ],
    R=[
        ("La mediana, ¿es el valor central de los datos ordenados o la suma de todos los datos?", "El valor central de los datos ordenados", "Es la definición de mediana."),
        ("Una tolerancia, ¿es el error máximo aceptado o el error mínimo posible?", "El error máximo aceptado", "Marca el límite para cumplir la medida."),
        ("Un dato atípico, ¿se parece mucho a los demás datos o es muy distinto de ellos?", "Es muy distinto de ellos", "Por eso conviene revisarlo."),
    ],
    C=[
        ("Los datos son 10, 12, 11, 40 y 12. La media da 17 y la mediana 12. ¿Cuál representa mejor el resultado típico?", "La mediana", "El 40 sube la media, pero casi todos los datos están cerca de 12."),
        ("Aparece un resultado muy distinto de los demás en una prueba. ¿Qué haces primero? A) revisar si hubo un error en la prueba antes de decidir qué hacer B) borrarlo sin decir nada", "A", "Hay que averiguar la causa y ser transparente."),
        ("La medida de diseño es 80 mm con tolerancia ±3 mm y la medida real es 84 mm. ¿Cumple?", "No", "El error es 4 mm y supera la tolerancia de 3 mm."),
    ],
    A=[
        ex("Tiempos de armado de ejemplo, en minutos: 12, 15, 13, 14 y 16. ¿Cuál es la mediana?", "14 minutos", "Ordenados quedan 12, 13, 14, 15, 16 y el valor central es 14."),
        arith("Cinco ensayos dieron 30, 32, 31, 75 y 32 g. ¿Cuál es la media?", "(30+32+31+75+32)//5", "Se suman los datos y se divide entre 5.", " g"),
        arith("Una pieza se diseñó de 200 mm y se midió 190 mm. ¿Cuál es su error relativo porcentual?", "(200-190)*100//200", "Se calcula el error, 10 mm, sobre la medida de diseño.", " %"),
    ],
    Z=[
        ("Las pruebas de resistencia dieron 5, 5, 6, 5 y 19 kg. Un grupo informa «resiste 8 kg» usando la media. ¿Qué problema tiene? A) el dato atípico 19 eleva la media, y casi todas las pruebas dieron 5 o 6 kg B) la media nunca sirve", "A", "La mediana sería 5 kg y representa mejor el resultado típico."),
        ("Piezas de 120 mm con tolerancia ±2 mm. Medidas de P: 119, 121 y 120. Medidas de Q: 118, 122 y 123. ¿Cuál cumple en todas las medidas?", "P", "Los errores de P son 1, 1 y 0 mm; Q tiene un error de 3 mm."),
    ],
    D=[
        arith("En cinco ensayos se obtuvo 22, 26, 24, 60 y 24 g, y se comprobó que el 60 fue un error porque se cayó el peso. ¿Cuál es la media de los otros cuatro datos?", "(22+26+24+24)//4", "Se suman los cuatro datos válidos y se divide entre 4.", " g"),
        ("Regla: cumple si la mediana es al menos 20 y el error relativo de la longitud es 5 % o menos. Datos: 18, 21, 20, 22 y 90. La longitud de diseño es 200 mm y la medida real, 192 mm. ¿Cumple?", "Sí: la mediana es 21 y el error relativo es 4 %", "Ordenados, el central es 21; el error de 8 mm sobre 200 mm es 4 %."),
    ],
    ctx=ex("Mides con una regla el largo de una caja de ejemplo diseñada de 24 cm con tolerancia de ±1 cm. Tus tres medidas son 24, 25 y 23 cm. ¿Cumple en todas?", "Sí cumple", "Los errores son 0, 1 y 1 cm, y ninguno supera 1 cm."),
    sc=[
        ("¿Qué es un dato atípico?", "Un valor muy distinto de los demás", "Puede deberse a un error o a una situación especial."),
        ("¿Cuándo cumple una pieza con su tolerancia?", "Cuando su error es menor o igual que la tolerancia", "Está dentro del límite aceptado."),
        ("¿Qué se hace antes de buscar la mediana?", "Ordenar los datos", "El valor central requiere datos ordenados."),
    ],
    open_task=(
        "Escoge un registro de ejemplo. Registro 1: tiempos de apertura de un cierre de cartón, en segundos: 8, 9, 8, 25 y 10; calcula la media y la mediana y explica qué harías con el dato atípico. Registro 2: tres piezas de 150 mm con tolerancia ±2 mm miden 149, 152 y 156 mm; indica cuáles cumplen y calcula el error relativo de la última.",
        "Registro 1: media 12 s y mediana 9 s; el 25 es atípico, se revisa si se trabó el cierre y se informa si se excluye",
        ["calcula bien media y mediana, o errores", "identifica el dato atípico o la pieza que no cumple", "explica la decisión", "usa unidades"],
        ["hoja con cálculos y explicación"],
        ["no ordenar antes de la mediana", "borrar el atípico sin explicación"],
        "Pregunta: «¿por qué crees que apareció ese dato?». Si no lo explica, pídele proponer una causa a revisar.",
    ),
    reinforce="Mide tres veces el largo de un libro con una regla y anota las medidas; calcula la media y la mediana y compara.",
    extend="Explica por qué dos productos con la misma media pueden tener medianas distintas.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja, lápiz y los registros escritos en este cuaderno.",
    use="Aprenderé a evaluar el proceso de creación comparando lo planificado con lo real en tiempo y costo, y a registrar problemas. Sirve para saber si trabajamos bien, no solo si el producto salió bien.",
    prior=["Sé hacer un cronograma y un presupuesto.", "Sé calcular porcentajes.", "Sé qué es una bitácora."],
    explain=[
        "Se evalúa el producto y también el proceso: cómo se trabajó. Algunos criterios del proceso son cumplir los tiempos, respetar el presupuesto, usar bien los materiales, trabajar con seguridad, cumplir los roles del equipo y registrar lo que pasa. Un producto bueno puede haberse logrado con un proceso malo, por ejemplo con material desperdiciado o sin protección.",
        "Para comparar se usa la desviación: valor real menos valor planificado. Si es positiva, se demoró o gastó más de lo previsto; si es negativa, menos. El porcentaje de desviación es desviación × 100 ÷ valor planificado. También se calcula el cumplimiento de hitos, que son los puntos de control del plan: hitos cumplidos × 100 ÷ hitos totales.",
        "La bitácora es el registro ordenado de lo que ocurrió: fecha, tarea, problema, decisión y resultado. Con ella se detectan las causas de los retrasos y se aprende para la próxima vez. Registrar un error no es buscar culpables; es juntar evidencia para mejorar el proceso.",
    ],
    vocab=[("desviación", "diferencia entre lo real y lo planificado"), ("hito", "punto de control del plan"), ("bitácora", "registro ordenado de lo ocurrido durante el trabajo"), ("proceso", "forma en que se trabaja para llegar al producto"), ("cumplimiento", "porcentaje de lo planificado que se logró")],
    worked=[
        ("Calcular una desviación de costo", "El costo planificado era $4.000 y el real fue $4.600. ¿Cuál es la desviación y el porcentaje?", ["Desviación: 4.600 − 4.000 = 600, positiva: se gastó más.", "Porcentaje: 600 × 100 ÷ 4.000 = 15."], "+$600, un 15 % más de lo planificado"),
        ("Evaluar el proceso con una bitácora", "La bitácora dice: «día 2, faltó cinta; se pidió a otro grupo; se perdieron 20 minutos». ¿Qué criterio del proceso se afectó?", ["Faltó un material que debía estar listo.", "Se perdió tiempo por no revisar la lista de materiales."], "El uso del tiempo y la revisión de materiales"),
    ],
    mistakes=[
        ("Evaluar solo el producto final.", "Un buen producto puede ocultar tiempo perdido, desperdicio o riesgos.", "Evalúa también el proceso con sus propios criterios."),
        ("Usar la bitácora para buscar culpables.", "El registro sirve para encontrar causas, no personas culpables.", "Anota hechos: qué pasó, cuándo y qué se decidió."),
    ],
    R=[
        ("Evaluar el proceso, ¿es revisar cómo se trabajó o solo mirar el producto terminado?", "Revisar cómo se trabajó", "Incluye tiempo, costo, seguridad y organización."),
        ("Una bitácora, ¿registra lo que ocurrió durante el trabajo o solo el resultado final?", "Lo que ocurrió durante el trabajo", "Guarda los hechos para analizarlos después."),
        arith("El plan decía 40 minutos y el trabajo real tomó 52 minutos. ¿Cuántos minutos se desvió?", "52-40", "Se resta lo planificado de lo real.", " minutos"),
    ],
    C=[
        ("Un equipo cumplió el tiempo, pero tres integrantes cortaron sin cuidado y sin una base firme. ¿Cómo se evalúa el proceso? A) falla en seguridad aunque cumple el tiempo B) es excelente porque cumple el tiempo", "A", "Cada criterio se evalúa por separado."),
        ("El costo planificado fue $5.000 y el real, $4.500. ¿La desviación es positiva o negativa?", "Negativa", "Se gastó menos de lo planificado: 4.500 − 5.000 es menor que cero."),
        ("¿Para qué sirve registrar los problemas del proceso? A) para evitar repetir los errores la próxima vez B) para señalar quién tuvo la culpa", "A", "El registro entrega evidencia para mejorar."),
    ],
    A=[
        arith("El plan era de 60 minutos y el trabajo duró 75. ¿Qué porcentaje de desviación tuvo el tiempo?", "(75-60)*100//60", "Se calcula la diferencia sobre lo planificado.", " %"),
        arith("El presupuesto era $5.000 y el gasto real fue $5.500. ¿Qué porcentaje de desviación tuvo el costo?", "(5500-5000)*100//5000", "Se calcula el exceso sobre lo planificado.", " %"),
        arith("De 8 hitos del plan, 6 se cumplieron a tiempo. ¿Qué porcentaje de cumplimiento hay?", "6*100//8", "Se divide lo cumplido entre el total y se multiplica por 100.", " %"),
    ],
    Z=[
        ("Un equipo terminó dos días tarde porque nadie anotó que faltaba cinta. ¿Qué parte del proceso falló? A) el registro y la revisión de materiales B) la calidad del producto", "A", "La falla estuvo en la preparación y en el registro."),
        ("El producto cumplió todo, pero se usó 30 % más material del planificado. ¿Qué mejora al proceso propones? A) calcular las piezas por plancha antes de cortar B) comprar más material por si acaso", "A", "Planificar el corte reduce el desperdicio."),
    ],
    D=[
        ex("Plan: medir 10 min, cortar 20 min, armar 30 min. Real: medir 15 min, cortar 20 min, armar 36 min. ¿Qué tarea tuvo la mayor desviación porcentual y de cuánto fue?", "Medir, con 50 %", "Medir se desvió 5 min sobre 10, o sea 50 %; armar, 6 sobre 30, o sea 20 %.", calc="5*100//10"),
        arith("Presupuesto de $12.000. Gastos reales: material $7.200, transporte $1.300 e imprevistos $3.900. ¿Cuánto fue el sobregasto?", "7200+1300+3900-12000", "Se suman los gastos reales y se resta el presupuesto.", " pesos"),
    ],
    ctx=ex("En tu casa planificaste armar un organizador en 40 minutos y terminaste en 50. ¿Qué porcentaje de desviación tuvo el tiempo?", "25 %", "Se calcula 10 × 100 ÷ 40 = 25.", calc="(50-40)*100//40"),
    sc=[
        ("¿Qué es la desviación?", "La diferencia entre lo real y lo planificado", "Muestra cuánto se alejó el trabajo del plan."),
        ("¿Qué es un hito?", "Un punto de control del plan", "Permite revisar si se avanza como se planificó."),
        ("¿Para qué sirve la bitácora?", "Para registrar lo ocurrido y aprender de ello", "Reúne evidencia del proceso."),
    ],
    open_task=(
        "Evalúa el proceso de este equipo de ejemplo. Plan: 4 hitos, tiempo 90 minutos y presupuesto $6.000. Real: se cumplieron 3 hitos a tiempo, el trabajo tomó 108 minutos y se gastaron $6.600. La bitácora anota: «día 1, se cortó mal una pieza y se desperdició un pliego de cartón; día 2, faltó pegamento». Calcula el porcentaje de cumplimiento de hitos, la desviación porcentual de tiempo y de costo, y propone una mejora para el proceso.",
        "Hitos: 75 %; tiempo: +20 %; costo: +10 %; mejora: marcar las piezas en la plancha antes de cortar y revisar la lista de materiales el día anterior",
        ["calcula los tres porcentajes", "usa la bitácora para detectar causas", "propone una mejora al proceso", "no culpa a personas"],
        ["hoja con cálculos y mejora"],
        ["calcular el porcentaje sobre el valor real", "proponer una mejora sin relación con la bitácora"],
        "Pregunta: «¿sobre qué valor se calcula el porcentaje de desviación?». Debe ser sobre lo planificado.",
    ),
    reinforce="Anota durante una tarea de tu casa el tiempo que pensabas que demoraría y el que demoró, y calcula la desviación.",
    extend="Explica por qué un equipo puede obtener un buen producto y aun así tener un proceso que mejorar.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja, lápiz y los registros escritos en este cuaderno.",
    use="Aprenderé a buscar la causa raíz de una falla con los cinco porqués, a clasificar las causas y a comprobarlas con una prueba. Sirve para mejorar de verdad y no solo tapar el problema.",
    prior=["Sé hacer una prueba justa.", "Sé calcular porcentajes.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Una falla es lo que se observa cuando el producto no cumple: la repisa se dobló, el cierre se soltó. Eso es el síntoma. La causa raíz es la razón más profunda que originó la falla. Para encontrarla se usan los cinco porqués: se pregunta «¿por qué?» y se vuelve a preguntar sobre cada respuesta, hasta llegar a algo que se pueda corregir.",
        "Las causas se pueden ordenar en categorías: diseño (las medidas o la forma estaban mal pensadas), material (no era el adecuado), fabricación (corte o armado mal hecho) y uso (se usó de forma distinta a la prevista). Cuando hay muchas fallas, se cuenta cuántas ocurren por cada causa y se atiende primero la que más fallas produce.",
        "Una causa propuesta es solo una hipótesis hasta que se comprueba. Para comprobarla se cambia solo esa variable y se repite la prueba. Decir «la causa es que el grupo es flojo» no sirve, porque no es un hecho observable. Una causa útil se puede ver, medir y corregir.",
    ],
    vocab=[("síntoma", "lo que se observa de la falla"), ("causa raíz", "razón más profunda que originó la falla"), ("cinco porqués", "preguntar «¿por qué?» varias veces hasta la causa raíz"), ("hipótesis", "explicación que aún se debe comprobar"), ("categoría de causa", "grupo: diseño, material, fabricación o uso")],
    worked=[
        ("Los cinco porqués", "La repisa de cartón se dobló. ¿Cuál es la causa raíz?", ["¿Por qué se dobló? Se despegaron las pestañas. ¿Por qué se despegaron? Se cargó antes de que el pegamento secara.", "¿Por qué se cargó antes? El plan no tenía tiempo de secado."], "Causa raíz: el plan no incluía el tiempo de secado"),
        ("Clasificar una causa", "El cartón usado era de 1 mm y el plano pedía 3 mm. ¿A qué categoría de causa corresponde?", ["El problema está en el tipo de material usado.", "No es de diseño ni de uso."], "Material"),
    ],
    mistakes=[
        ("Quedarse con el síntoma como si fuera la causa.", "Si solo se arregla el síntoma, la falla vuelve a ocurrir.", "Sigue preguntando «¿por qué?» hasta una causa que se pueda corregir."),
        ("Cambiar varias cosas a la vez para arreglar la falla.", "No se sabe cuál cambio funcionó.", "Cambia una variable y vuelve a probar."),
    ],
    R=[
        ("«La repisa se dobló», ¿es un síntoma o una causa raíz?", "Un síntoma", "Es lo que se observa, no la razón profunda."),
        ("Los cinco porqués, ¿consiste en preguntar «¿por qué?» varias veces o en hacer cinco dibujos?", "Preguntar «¿por qué?» varias veces", "Así se llega a la causa raíz."),
        ("Usar el soporte con más peso del que se diseñó, ¿es una causa de uso o de material?", "De uso", "El producto se usó de una forma no prevista."),
    ],
    C=[
        ("Se rompió la unión de un soporte. ¿Cuál es una causa de diseño? A) las pestañas se dibujaron de 5 mm, demasiado cortas B) alguien se sentó encima del soporte", "A", "La medida estaba mal pensada desde el plano."),
        ("Para comprobar una causa propuesta, ¿qué se hace? A) cambiar solo esa variable y volver a probar B) discutir hasta ponerse de acuerdo", "A", "Solo una prueba entrega evidencia."),
        ("Un compañero dice «la causa es que el grupo es flojo». ¿Qué le falta? A) un hecho observable que lo respalde B) otra opinión", "A", "Una causa útil se puede observar y corregir."),
    ],
    A=[
        ("Clasifica cada causa (D diseño, M material, F fabricación, U uso): (1) cartón de 1 mm en vez de 3 mm, (2) corte torcido de una pieza, (3) peso mayor que el previsto, (4) pestañas muy cortas en el plano.", "1 M, 2 F, 3 U, 4 D", "Cada causa corresponde a la etapa donde se originó."),
        ex("De 40 fallas registradas, 18 ocurrieron en el pegado, 10 en el corte, 8 en las medidas y 4 por el uso. ¿Qué porcentaje de las fallas fue por pegado y qué conviene atacar primero?", "45 %; el pegado", "Se calcula 18 × 100 ÷ 40 = 45 y es la causa con más fallas.", calc="18*100//40"),
        arith("De 20 fallas por pegado se pasó a 5 tras reforzar la unión. ¿Qué porcentaje de esas fallas se evitó?", "(20-5)*100//20", "Se calcula la reducción sobre las fallas iniciales.", " %"),
    ],
    Z=[
        ("La estantería se cae. ¿Por qué? La base es angosta. ¿Por qué? El plano pedía 6 cm. ¿Por qué 6 cm? Nadie calculó dónde queda el centro del peso. ¿Cuál es la causa raíz? A) no se revisó la estabilidad al diseñar B) la base es angosta", "A", "La base angosta es un síntoma de un diseño sin cálculo de estabilidad."),
        ("Un grupo cambia el pegamento y el cartón a la vez y la falla desaparece. ¿Puede asegurar cuál era la causa?", "No", "Cambiaron dos variables y no se sabe cuál resolvió la falla."),
    ],
    D=[
        ("En 50 pruebas hubo fallas por pegado (20), material (15), corte (10) y uso (5). Para eliminar más del 60 % de las fallas, ¿qué dos causas hay que atacar?", "Pegado y material", "Suman 35 de 50 fallas, o sea 70 %; ninguna otra pareja pasa del 60 %."),
        arith("Se probaron 3 soportes con 10 minutos de secado, que soportaron 2, 3 y 1 kg, y 3 con 30 minutos de secado, que soportaron 6, 5 y 7 kg. ¿Cuántos kilos más soportan en promedio los de 30 minutos?", "(6+5+7)//3-(2+3+1)//3", "Los promedios son 6 y 2 kg, y la diferencia es 4 kg.", " kg"),
    ],
    ctx=ex("En tu casa armaste 10 soportes de ejemplo y 4 fallaron al cargarlos con libros. De esas 4 fallas, 3 fueron por pegado. ¿Qué porcentaje de las fallas fue por pegado?", "75 %", "Se calcula 3 × 100 ÷ 4 = 75.", calc="3*100//4"),
    sc=[
        ("¿Qué es la causa raíz?", "La razón más profunda que originó la falla", "Corregirla evita que la falla se repita."),
        ("¿Cuáles son las cuatro categorías de causas?", "Diseño, material, fabricación y uso", "Ordenan dónde se originó la falla."),
        ("¿Cómo se comprueba una causa propuesta?", "Cambiando solo esa variable y repitiendo la prueba", "Así se aísla su efecto."),
    ],
    open_task=(
        "Analiza esta falla de ejemplo: un organizador de cartón se pandea al cargarlo con 3 libros. Datos: el cartón es de 1 mm; el plano pedía 2 mm; las pestañas de unión miden 5 mm; el pegamento se aplicó en 2 minutos antes de cargarlo. Haz una cadena de cinco porqués, clasifica la causa raíz, propón una prueba para comprobarla cambiando una sola variable y di qué resultado esperas.",
        "¿Por qué se pandea? El cartón es delgado. ¿Por qué? Se usó uno de 1 mm. ¿Por qué? No se revisó el material del plano. Causa de material; prueba: armar tres organizadores iguales con cartón de 2 mm y cargarlos con 3 libros; se espera que no se pandeen",
        ["hace una cadena de porqués", "clasifica la causa", "propone una prueba con una sola variable", "predice un resultado"],
        ["cadena de porqués y plan de prueba"],
        ["quedarse en el síntoma", "cambiar más de una variable en la prueba"],
        "Pregunta: «¿qué cambiarías solo una vez para ver si esa es la causa?». Si cambia dos cosas, pídele elegir una.",
    ),
    reinforce="Piensa en un objeto de tu casa que se haya roto y escribe tres porqués hasta una causa que se pueda corregir.",
    extend="Explica por qué un registro de fallas con porcentajes ayuda a elegir qué mejorar primero.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a proponer mejoras al producto y al proceso, a priorizarlas por impacto y esfuerzo, y a comprobar con datos si funcionaron. Sirve para que cada versión sea mejor que la anterior.",
    prior=["Sé buscar la causa raíz de una falla.", "Sé calcular porcentajes de mejora.", "Sé hacer una prueba justa."],
    explain=[
        "Una mejora puede apuntar al producto final, como cambiar el grosor del cartón de la base, o al proceso, como agregar un tiempo de secado al plan. Una buena mejora responde a una causa raíz y se escribe con lo que se cambiará, cuánto se espera lograr y cómo se comprobará: «reforzar la unión con una segunda capa para que 9 de 10 soportes resistan 5 kg».",
        "Como casi siempre hay varias mejoras posibles, se priorizan según el impacto que tendrían y el esfuerzo que cuestan en tiempo, dinero y materiales. Conviene hacer primero lo de alto impacto y bajo esfuerzo; después lo de alto impacto y alto esfuerzo; luego lo de bajo impacto y bajo esfuerzo; y al final lo de bajo impacto y alto esfuerzo. También se calcula cuánto cuesta cada falla evitada.",
        "Toda mejora debe verificarse: se repite la prueba con el mismo procedimiento y se compara con los datos de antes. Si una mejora arregla un problema pero crea otro, como un soporte más liviano que ya no resiste, eso es un impacto no deseado de la mejora. Sin una nueva prueba solo se puede decir que algo cambió, no que mejoró.",
    ],
    vocab=[("mejora", "cambio que busca que el producto o el proceso funcione mejor"), ("impacto", "cuánto cambia el resultado"), ("esfuerzo", "tiempo, dinero y materiales que cuesta hacer algo"), ("verificar", "comprobar con una nueva prueba"), ("iteración", "ciclo de probar, mejorar y volver a probar")],
    worked=[
        ("Priorizar mejoras", "Tres mejoras: X (impacto alto, esfuerzo bajo), Y (impacto alto, esfuerzo alto) y Z (impacto bajo, esfuerzo bajo). ¿En qué orden se hacen?", ["Primero va lo de alto impacto y bajo esfuerzo: X.", "Después alto impacto y alto esfuerzo: Y; al final, Z."], "X, Y, Z"),
        ("Verificar una mejora con datos", "Antes de la mejora fallaron 30 de 100 soportes. Después, fallaron 12 de 100. ¿Qué porcentaje bajaron las fallas?", ["Fallas evitadas: 30 − 12 = 18.", "Porcentaje: 18 × 100 ÷ 30 = 60."], "Bajaron 60 %"),
    ],
    mistakes=[
        ("Escribir la mejora como «hacerlo más fuerte».", "No dice qué cambiar ni cómo se comprobará.", "Escribe qué cambias, cuánto esperas lograr y cómo lo vas a medir."),
        ("Decir que mejoró sin volver a probar.", "Un cambio no es lo mismo que una mejora.", "Repite la prueba con el mismo procedimiento y compara."),
    ],
    R=[
        ("Agregar un tiempo de secado al cronograma, ¿es una mejora al proceso o al producto final?", "Al proceso", "Cambia la forma de trabajar y no el producto."),
        ("Cambiar el grosor del cartón de la base, ¿es una mejora al proceso o al producto final?", "Al producto final", "Modifica el producto mismo."),
        ("Después de mejorar, ¿qué hay que hacer para saber si funcionó: volver a probar con el mismo procedimiento o suponer que funcionó?", "Volver a probar con el mismo procedimiento", "Solo así se comparan los resultados antes y después."),
    ],
    C=[
        ("¿Cuál mejora está mejor redactada? A) «reforzar la unión con una segunda capa de cartón para que 9 de 10 soportes resistan 5 kg» B) «hacerlo más fuerte»", "A", "La primera dice qué se cambia y cómo se comprobará."),
        ("Una mejora con alto impacto y bajo esfuerzo, ¿se hace primero o último?", "Primero", "Da un gran resultado con poco costo."),
        ("Una mejora vuelve el soporte más liviano, pero ahora no resiste. ¿Qué se llama este efecto? A) impacto no deseado de la mejora B) mejora completa", "A", "Resuelve una cosa pero perjudica un criterio importante."),
    ],
    A=[
        arith("Un grupo reduce el tiempo de armado de 40 minutos a 28. ¿Qué porcentaje bajó el tiempo?", "(40-28)*100//40", "Se calcula la reducción sobre el tiempo inicial.", " %"),
        arith("Una mejora cuesta $2.400 y evita perder $600 de material por semana. ¿En cuántas semanas se recupera el costo?", "2400//600", "Se divide el costo entre lo que se ahorra cada semana.", " semanas"),
        ("Ordena de primera a última según la regla del cuaderno: 1 (impacto alto, esfuerzo bajo), 2 (impacto bajo, esfuerzo bajo), 3 (impacto alto, esfuerzo alto), 4 (impacto bajo, esfuerzo alto).", "1, 3, 2, 4", "Primero alto impacto con bajo esfuerzo, luego alto con alto, luego bajo con bajo y al final bajo con alto."),
    ],
    Z=[
        ("Antes de la mejora fallaban 12 de 40 soportes; después fallan 8 de 40. La meta era que fallaran 4 o menos. ¿Se logró?", "No", "Hay 8 fallas y la meta pedía 4 o menos."),
        ("Un equipo cambia su diseño pero no vuelve a medir. ¿Qué puede afirmar con evidencia? A) ninguna conclusión sobre si mejoró B) que mejoró porque cambió algo", "A", "Sin nueva prueba solo se sabe que algo cambió."),
    ],
    D=[
        arith("Una mejora toma 20 minutos extra por soporte y se fabrican 12 soportes. ¿Cuántas horas extra de trabajo significa?", "(20*12)//60", "Se calculan los minutos totales, 240, y se pasan a horas.", " horas"),
        ("La mejora X cuesta $3.000 y baja las fallas de 20 a 8 en 40 soportes. La mejora Y cuesta $1.500 y las baja de 20 a 15. ¿Cuál cuesta menos por falla evitada y cuánto?", "X, con $250 por falla evitada", "X evita 12 fallas (3.000 ÷ 12 = 250) e Y evita 5 (1.500 ÷ 5 = 300)."),
    ],
    ctx=ex("Tu grupo mide que el tiempo de armado de un organizador baja de 50 a 40 minutos tras una mejora de ejemplo. ¿Qué porcentaje bajó el tiempo?", "20 %", "Se calcula 10 × 100 ÷ 50 = 20.", calc="(50-40)*100//50"),
    sc=[
        ("¿Una mejora puede apuntar al proceso?", "Sí", "También se mejora la forma de trabajar."),
        ("¿Qué se hace primero al priorizar mejoras?", "Las de alto impacto y bajo esfuerzo", "Dan el mayor resultado con menos costo."),
        ("¿Qué es verificar una mejora?", "Comprobarla con una nueva prueba", "Se comparan los datos de antes y después."),
    ],
    open_task=(
        "Con los datos de ejemplo de la clase anterior (un organizador de cartón de 1 mm que se pandeaba con 3 libros y fallaron 6 de 10 organizadores), propón una mejora al producto y una al proceso. Para cada una escribe qué cambiarías, el impacto y el esfuerzo (alto o bajo), una meta con número y cómo la verificarías. Después ordena las dos mejoras con la regla de impacto y esfuerzo.",
        "Producto: usar cartón de 2 mm (impacto alto, esfuerzo bajo); meta: que fallen 2 o menos de 10; verificación: cargar 10 organizadores con 3 libros. Proceso: revisar el grosor del material antes de cortar (impacto bajo, esfuerzo bajo); orden: primero la mejora del producto y después la del proceso",
        ["propone una mejora al producto y una al proceso", "indica impacto y esfuerzo", "fija una meta con número", "propone cómo verificarla"],
        ["tabla de mejoras con meta y verificación"],
        ["redactar mejoras sin meta", "no explicar cómo se comprobará"],
        "Pregunta: «¿cómo sabrás con un número que mejoró?». Si no puede responder, pídele agregar la meta y la prueba.",
    ),
    reinforce="Elige un objeto de tu casa que funcione mal y escribe una mejora con su meta medible.",
    extend="Explica por qué conviene probar de nuevo después de una mejora, aunque parezca evidente que funcionará.",
)
