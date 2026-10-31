"""Cuaderno del estudiante, 6.º básico Tecnología: OA 02 (planificar la elaboración de objetos o servicios), clases 1 a 5.

Clase 1 secuencia y dependencias, 2 tiempos, 3 costos, 4 recursos necesarios y alternativos, 5 implicancias ambientales y sociales.
Dinero chileno: billetes de $1.000, $2.000, $5.000, $10.000 y $20.000; monedas de $10, $50, $100 y $500. Precios ficticios, sin marcas.
Seguridad: solo papel, cartón, cinta, cordel y tijeras de punta roma. Simplificación declarada: las clases siguen el contenido del OA, no los títulos genéricos de la ficha.
"""
from __future__ import annotations

from student_content_te6_a import reg
from student_lessons import arith

OA2 = "TE06 OA 02"

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja y lápiz. Todas las secuencias están escritas en este cuaderno.",
    use="Aprenderé a ordenar las acciones para elaborar un objeto o un servicio y a ver qué pasos dependen de otros. Sirve para no perder tiempo ni cometer errores de orden.",
    prior=["Sé que un diseño tiene criterios.", "Sé que un dibujo técnico lleva medidas.", "Sé sumar minutos."],
    explain=[
        "Planificar es decidir qué se hará, en qué orden y con qué recursos. La secuencia de acciones es la lista ordenada de pasos. Cada paso empieza con un verbo en infinitivo, como medir, cortar, unir o pintar, y se puede hacer sin adivinar. Se planifica para objetos, como una caja, y también para servicios, como un préstamo de libros en la sala.",
        "El orden importa porque unos pasos dependen de otros. Una dependencia es cuando un paso necesita que otro esté terminado: no puedes pintar antes de que el pegamento seque. Para revisar el orden pregúntate: «¿Qué debe estar terminado antes de este paso?». Los pasos que no dependen entre sí pueden hacerse a la vez.",
        "Si dos personas hacen a la vez dos pasos independientes, el trabajo total se acorta, porque solo cuenta el paso más largo de los dos. Un plan se puede dibujar como cajas con flechas: cada flecha indica una dependencia. Un plan claro sirve para repartir tareas y detectar errores antes de empezar.",
    ],
    vocab=[("secuencia", "lista de pasos en orden"), ("dependencia", "cuando un paso necesita que otro esté terminado"), ("paso independiente", "paso que no necesita a otro para hacerse"), ("servicio", "actividad organizada que ayuda a las personas, como prestar libros"), ("plan", "la secuencia con materiales y tiempos")],
    worked=[
        ("Ordenar los pasos", "Ordena los pasos de una caja de cartón: pintar, medir, cortar, pegar, marcar, dejar secar.", ["Primero medir y marcar: hay que saber el tamaño.", "Luego cortar y pegar; después dejar secar y al final pintar."], "Medir, marcar, cortar, pegar, dejar secar y pintar"),
        ("Pasos a la vez", "Para un banderín: A cortar el papel del banderín (10 min), B preparar el cordel (6 min), C unir A y B (4 min). Dos personas hacen A y B a la vez. ¿Cuánto demora todo?", ["A y B se hacen a la vez: cuenta el más largo, 10 min.", "Luego C, que necesita A y B: 4 min. Sumo 10 + 4."], "14 minutos"),
    ],
    mistakes=[
        ("Poner «pintar» antes de «dejar secar el pegamento».", "La pintura se corre si el pegamento está húmedo.", "Pregunta qué debe estar terminado antes de cada paso."),
        ("Escribir pasos como «cajita» o «bonito».", "No dicen qué acción hacer.", "Empieza cada paso con un verbo en infinitivo."),
    ],
    R=[
        ("¿Con qué clase de palabra empieza cada paso de un plan?", "Con un verbo en infinitivo", "Los pasos indican acciones, como medir o cortar."),
        ("En el plan «cortar, medir, pegar», ¿qué paso está mal ubicado?", "Cortar", "Hay que medir antes de cortar."),
        ("¿Una dependencia es un paso que necesita a otro terminado, o uno que se hace solo?", "Uno que necesita a otro terminado", "Esa es la definición de dependencia."),
    ],
    C=[
        ("¿Cuál pregunta ayuda a revisar el orden de un plan? A «¿Qué debe estar terminado antes?», B «¿Qué color es más lindo?».", "A", "Esa pregunta descubre las dependencias."),
        ("Dos personas hacen a la vez dos pasos independientes. ¿El trabajo total se acorta o se alarga?", "Se acorta", "Solo cuenta el paso más largo de los dos."),
        ("¿Un servicio, como un préstamo de libros en la sala, también necesita un plan?", "Sí", "Un servicio también tiene pasos ordenados."),
    ],
    A=[
        ("Ordena los pasos para armar un puente de palitos de papel: pegar las tiras, medir las tiras, probar con peso, cortar las tiras, marcar las tiras.", "Medir, marcar, cortar, pegar y probar", "Cada paso necesita el anterior terminado."),
        arith("Tres pasos en fila demoran 20, 30 y 15 minutos. ¿Cuántos minutos demora el plan?", "20+30+15", "En fila, los tiempos se suman.", " minutos"),
        ("Plan de préstamo de libros: registrar el libro, entregar el libro, buscar el libro pedido, anotar la devolución. ¿Qué paso va primero?", "Buscar el libro pedido", "Sin el libro no se puede registrar ni entregar."),
    ],
    Z=[
        ("Un plan dice: pegar las patas de una mesa, pegar la tapa, pintar, medir las patas. ¿Qué error tiene?", "Medir las patas está al final", "Medir debe hacerse antes de pegar."),
        ("Camila dice: «Aunque no dependan, mejor hacer todos los pasos en fila». ¿Es mejor cuando hay dos personas?", "No", "Hacer a la vez dos pasos independientes ahorra tiempo."),
    ],
    D=[
        arith("A (20 min) y B (30 min) se hacen a la vez entre dos personas; luego C (15 min) necesita A y B. ¿Cuántos minutos demora todo el plan?", "30+15", "Cuenta el más largo de los dos primeros y luego C.", " minutos"),
        arith("Pasos: P1 medir (5 min), P2 cortar (10 min, necesita P1), P3 preparar cordel (4 min, independiente), P4 unir (12 min, necesita P2 y P3). Con dos personas, ¿cuál es el tiempo mínimo?", "5+10+12", "P3 se hace mientras se hacen P1 y P2.", " minutos"),
    ],
    ctx=("El curso quiere ofrecer un servicio de préstamo de libros en la sala. Pasos: A anotar quién pide el libro (3 min), B buscar el libro en la caja (5 min), C entregar el libro (1 min). Ordena los pasos y calcula el tiempo si una persona hace todo en fila.", "Orden: A, B, C. Tiempo: 3 + 5 + 1 = 9 minutos", "Se ordena por dependencia y se suman los tiempos."),
    sc=[
        ("¿Cómo empieza cada paso de un plan?", "Con un verbo en infinitivo", "Indica la acción."),
        ("¿Qué es una dependencia?", "Un paso que necesita que otro esté terminado", "Marca el orden."),
        ("¿Qué pasos pueden hacerse a la vez?", "Los que no dependen entre sí", "Así se acorta el trabajo."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: un organizador de escritorio de cartón con medir, marcar, cortar las piezas, preparar el pegamento, pegar y decorar. Trabajo 2: un servicio de reparto de la leche de la colación con contar vasos, repartir, anotar quién falta y lavar los vasos. Escribe los pasos con verbo en infinitivo, ordénalos, marca una dependencia y señala dos pasos que se puedan hacer a la vez.",
        "Trabajo 1: medir, marcar, cortar, preparar el pegamento, pegar, decorar. Dependencia: pegar necesita cortar. A la vez: cortar las piezas y preparar el pegamento",
        ["pasos con verbo en infinitivo", "orden correcto", "marca una dependencia", "señala dos pasos simultáneos"],
        ["plan con pasos ordenados y flechas"],
        ["no revisar el orden", "pasos sin verbo"],
        "Pregunta: «¿qué debe estar listo antes de este paso?». Si no sabe, pídele revisar el orden.",
    ),
    reinforce="Escribe los pasos ordenados para preparar y servir un vaso de agua a una persona.",
    extend="Elige un plan de dos personas y explica qué dos pasos harían a la vez y cuánto tiempo ahorrarían.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja y lápiz. Todos los horarios están escritos en este cuaderno.",
    use="Aprenderé a estimar el tiempo de cada paso, a armar un cronograma y a calcular cuándo termina un trabajo. Sirve para entregar a tiempo.",
    prior=["Sé la secuencia de un plan.", "Sé que 1 hora son 60 minutos.", "Sé sumar minutos y horas."],
    explain=[
        "Un cronograma es una tabla que muestra qué paso se hace, cuánto demora y a qué hora o en qué día. Para estimar el tiempo de un paso, piensa en cuánto demoraste en algo parecido y agrega un margen por si hay un problema. Si dudas, estima más tiempo y no menos.",
        "Los minutos se pueden convertir a horas: 60 minutos son 1 hora, y 90 minutos son 1 hora 30 minutos. Para saber a qué hora termina un trabajo, sumas la duración a la hora de inicio. Si empiezas a las 15:00 y el trabajo demora 45 minutos, terminas a las 15:45.",
        "Algunos pasos tienen tiempos de espera, como el secado del pegamento o de la pintura. Mientras tanto se pueden hacer otros pasos independientes. Si el tiempo disponible no alcanza, hay tres opciones: pedir más tiempo, repartir tareas entre más personas o simplificar el diseño. Se decide con los números del cronograma.",
    ],
    vocab=[("cronograma", "tabla con los pasos y el tiempo de cada uno"), ("estimar", "calcular de forma aproximada"), ("margen de tiempo", "tiempo extra por si hay un problema"), ("tiempo de espera", "tiempo en que no puedes avanzar, como el secado"), ("duración", "cuánto demora un paso")],
    worked=[
        ("Calcular la hora de término", "Un grupo empieza a las 10:15. Hace tres pasos de 20, 30 y 25 minutos en fila. ¿A qué hora termina?", ["Sumo los tiempos: 20 + 30 + 25 = 75 minutos, o sea 1 hora 15 minutos.", "A las 10:15 sumo 1 hora y 15 minutos."], "A las 11:30"),
        ("Aprovechar el tiempo de secado", "Un trabajo necesita pegar piezas (15 min), esperar 40 min a que seque y pintar (20 min). Mientras seca, un integrante prepara la pintura (10 min). ¿Cuánto demora todo?", ["La preparación de la pintura cabe dentro de los 40 minutos de secado.", "Sumo 15 + 40 + 20."], "75 minutos"),
    ],
    mistakes=[
        ("Estimar solo el tiempo ideal, sin margen.", "Si hay un problema, el plan se atrasa.", "Agrega un margen de tiempo."),
        ("Mezclar horas y minutos al sumar.", "60 minutos son 1 hora, no 100.", "Convierte minutos a horas antes de sumar a la hora de inicio."),
    ],
    R=[
        ("En Tecnología: ¿Cuántos minutos tiene 1 hora?", "60", "Una hora son 60 minutos."),
        ("Un trabajo empieza a las 9:00 y demora 30 minutos. ¿A qué hora termina?", "A las 9:30", "Se suman 30 minutos a las 9:00."),
        ("¿Cómo se llama la tabla con los pasos y sus tiempos?", "Cronograma", "Muestra qué paso se hace y cuánto demora."),
    ],
    C=[
        ("¿Para qué sirve el margen de tiempo?", "Para enfrentar un problema sin atrasarse", "Evita que un error arruine el plan."),
        ("Mientras seca el pegamento, ¿qué conviene hacer? A esperar sin hacer nada, B hacer un paso independiente.", "B", "Así se aprovecha el tiempo."),
        ("90 minutos, ¿cuántas horas y minutos son?", "1 hora y 30 minutos", "60 minutos son 1 hora y sobran 30."),
    ],
    A=[
        arith("Tres pasos demoran 25, 35 y 20 minutos en fila. ¿Cuántos minutos demora el trabajo?", "25+35+20", "Se suman los tiempos de cada paso.", " minutos"),
        arith("Un grupo tiene 2 horas para terminar. Ya usó 75 minutos. ¿Cuántos minutos le quedan?", "120-75", "2 horas son 120 minutos y se resta lo usado.", " minutos"),
        ("Un trabajo empieza a las 14:20 y demora 50 minutos. ¿A qué hora termina?", "A las 15:10", "14:20 más 40 minutos es 15:00 y faltan 10."),
    ],
    Z=[
        ("Un grupo tiene 60 minutos y su cronograma suma 75 minutos. ¿Alcanza el tiempo?", "No", "El plan dura 15 minutos más de lo disponible."),
        ("Para reducir el tiempo del grupo anterior, ¿qué opción es válida? A repartir pasos independientes entre dos personas, B saltarse la prueba final.", "A", "Hacer pasos a la vez acorta sin perder calidad."),
    ],
    D=[
        arith("Un plan tiene pegar (20 min), secar (45 min, sin trabajo) y pintar (25 min). Con un margen de 10 minutos, ¿cuántos minutos se reservan?", "20+45+25+10", "Se suman los pasos, la espera y el margen.", " minutos"),
        ("Un grupo termina a las 16:05 y empezó a las 14:35. ¿Cuántos minutos demoró en total?", "90 minutos", "De 14:35 a 15:35 hay 60 minutos y de 15:35 a 16:05 hay 30 minutos."),
    ],
    ctx=("El curso debe armar 10 cajitas de cartón en una clase de 90 minutos, que comienza a las 11:00. Cada cajita demora 8 minutos y se arma una por vez. ¿Alcanza el tiempo? ¿A qué hora terminarían?", "10 cajitas × 8 min = 80 minutos; sí alcanza; terminan a las 12:20", "80 minutos son menos que 90; 11:00 más 1 hora 20 minutos."),
    sc=[
        ("¿Cuántos minutos son 2 horas?", "120", "Cada hora tiene 60 minutos."),
        ("¿Qué haces si el tiempo no alcanza?", "Pedir más tiempo, repartir tareas o simplificar", "Se decide con los números del cronograma."),
        ("¿Qué es un tiempo de espera?", "Un tiempo en que no se puede avanzar, como el secado", "Mientras tanto se pueden hacer otros pasos."),
    ],
    open_task=(
        "Escoge un plan. Plan 1: una caja de cartón con medir y marcar (15 min), cortar (25 min), pegar (20 min), secar (30 min de espera) y decorar (20 min); empieza a las 10:00. Plan 2: un cartel con dibujar (30 min), pintar (35 min), secar (20 min de espera) y escribir (15 min); empieza a las 15:30. Arma el cronograma, calcula la hora de término y di si cabe en 2 horas.",
        "Plan 2: 30 + 35 + 20 + 15 = 100 minutos, o sea 1 hora 40; empieza 15:30 y termina 17:10; cabe en 2 horas",
        ["cronograma con tiempos", "suma correcta", "hora de término correcta", "dice si cabe en 2 horas"],
        ["tabla con pasos, tiempos y hora de término"],
        ["olvidar el tiempo de espera", "sumar mal horas y minutos"],
        "Pregunta: «¿cuánto suman los minutos y qué hora es después de sumarlos?». Revisa la conversión a horas.",
    ),
    reinforce="Calcula cuántos minutos demoran tus actividades de la tarde hasta la hora de dormir.",
    extend="Explica con un ejemplo cómo un tiempo de espera puede aprovecharse con un paso independiente.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja, lápiz y las listas de precios escritas en este cuaderno. Los precios son ficticios.",
    use="Aprenderé a calcular el costo de un trabajo con un presupuesto, a comparar precios y a calcular el vuelto. Sirve para saber si el dinero alcanza antes de comprar.",
    prior=["Sé multiplicar y sumar.", "Conozco los billetes y monedas chilenas.", "Sé calcular vueltos."],
    explain=[
        "Un presupuesto es el cálculo del costo de un trabajo antes de hacerlo. Para cada material se anota la cantidad, el precio de una unidad y el costo, que es cantidad por precio unitario. Luego se suman los costos y se obtiene el costo total. Un presupuesto puede incluir también el costo de la energía o del transporte.",
        "Para comparar dos opciones se compara el precio de la misma cantidad. Si un pliego de cartón vale $600 y otro paquete trae 3 pliegos por $1.500, el primero cuesta $1.800 por 3 pliegos y el paquete $1.500: conviene el paquete. También se calcula el vuelto: lo que pagas menos el costo total.",
        "Un presupuesto debe ajustarse al dinero disponible. Si el costo total supera el dinero que hay, se puede reducir cantidad, cambiar un material por otro más barato o reutilizar. En Chile existen billetes de $1.000, $2.000, $5.000, $10.000 y $20.000 y monedas de $10, $50, $100 y $500.",
    ],
    vocab=[("presupuesto", "cálculo del costo de un trabajo antes de hacerlo"), ("precio unitario", "precio de una sola unidad"), ("costo total", "suma de todos los costos"), ("vuelto", "dinero que te devuelven al pagar de más"), ("ahorro", "dinero que no se gasta por elegir mejor")],
    worked=[
        ("Calcular un presupuesto", "Una caja lleva 4 tiras de cartón a $250 cada una y 1 cinta a $800. ¿Cuál es el costo total?", ["Las tiras cuestan 4 × 250 = 1.000.", "Sumo la cinta: 1.000 + 800."], "$1.800"),
        ("Comparar y calcular el vuelto", "Un pliego cuesta $400 en una tienda. En otra, un paquete de 5 pliegos cuesta $1.750. Si necesitas 5 pliegos y pagas con $5.000, ¿cuál conviene y cuál es el vuelto?", ["Cinco pliegos sueltos cuestan 5 × 400 = 2.000.", "El paquete cuesta $1.750, que es menos. El vuelto es 5.000 − 1.750."], "Conviene el paquete; el vuelto es $3.250"),
    ],
    mistakes=[
        ("Sumar solo los precios unitarios sin multiplicar por la cantidad.", "Se cuenta un solo objeto de cada uno.", "Multiplica cantidad por precio de una unidad antes de sumar."),
        ("Comparar el precio de un paquete con el de una sola unidad.", "No se comparan las mismas cantidades.", "Calcula el precio de la misma cantidad en ambas opciones."),
    ],
    R=[
        ("¿Qué se multiplica para obtener el costo de un material?", "La cantidad por el precio unitario", "Así se calcula el costo de varias unidades."),
        ("¿Cuántos pesos son 3 monedas de $100 y 1 moneda de $50?", "$350", "300 más 50 suman 350."),
        ("Pagas con $2.000 un gasto de $1.500. ¿Cuál es el vuelto?", "$500", "2.000 menos 1.500 es 500."),
    ],
    C=[
        ("¿Qué es un presupuesto?", "El cálculo del costo de un trabajo antes de hacerlo", "Sirve para saber si el dinero alcanza."),
        ("Si el costo total supera el dinero disponible, ¿qué puedes hacer?", "Reducir cantidad, cambiar un material o reutilizar", "Así el presupuesto se ajusta."),
        ("¿Qué se compara para saber qué opción conviene?", "El precio de la misma cantidad", "Si no, la comparación es injusta."),
    ],
    A=[
        arith("Un trabajo lleva 6 hojas de papel de colores a $150 cada una. ¿Cuántos pesos cuestan?", "6*150", "Se multiplica la cantidad por el precio unitario.", " pesos"),
        arith("Compras materiales por $3.400 y pagas con un billete de $5.000. ¿Cuántos pesos te devuelven?", "5000-3400", "Se resta el costo del dinero entregado.", " pesos"),
        ("Una tienda vende 1 cordel a $300 y otra vende 3 cordeles por $750. Necesitas 3. ¿Dónde conviene comprar?", "En la que vende 3 por $750", "Tres cordeles sueltos cuestan $900, más que $750."),
    ],
    Z=[
        ("Un grupo tiene $2.000. Su presupuesto da 4 tiras a $300 y 2 pegamentos a $500. ¿Le alcanza el dinero?", "No", "Cuesta 1.200 más 1.000, o sea $2.200."),
        ("Beto sumó $300 + $500 y dijo que gastará $800 por 4 tiras y 2 pegamentos. ¿Qué error cometió?", "No multiplicó por las cantidades", "Debía calcular 4 × 300 y 2 × 500."),
    ],
    D=[
        arith("Presupuesto: 5 pliegos de cartón a $200, 2 cintas a $450 y 1 tijera a $1.200. ¿Cuál es el costo total?", "5*200+2*450+1200", "Se calcula cada costo y se suman.", " pesos"),
        arith("Un paquete de 12 stickers cuesta $2.400. ¿Cuántos pesos cuesta cada sticker?", "2400//12", "Se divide el costo entre la cantidad.", " pesos"),
    ],
    ctx=("El curso hará 8 portalápices de cartón. Cada uno lleva 2 pliegos de cartón a $250 cada pliego y 1 cinta de $600 se reparte entre todos. Tienen $6.000. Calcula el costo total y di cuánto dinero sobra.", "Cartón: 8 × 2 × 250 = $4.000. Con la cinta: $4.600. Sobran $1.400", "Se multiplican cantidades, se suma la cinta y se resta del dinero."),
    sc=[
        ("¿Qué incluye un presupuesto?", "Cantidades, precios unitarios y costo total", "Permite saber si el dinero alcanza."),
        ("¿Cómo se calcula el vuelto?", "Se resta el costo del dinero entregado", "Es lo que te devuelven."),
        ("¿Se compara el precio de una unidad con el de un paquete?", "No, se compara la misma cantidad", "Si no, la comparación no es justa."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: un estante de cartón con 6 tiras a $350 cada una, 1 cinta a $900 y 2 pegamentos a $700 cada uno; dinero disponible $5.000. Trabajo 2: 4 cuadros de papel, cada cuadro con 3 láminas a $200 cada lámina, 4 marcos de cartón a $450 cada marco y 1 cordel a $600; dinero disponible $4.000. Arma el presupuesto, calcula el total y di cuánto sobra o falta. Si falta, propone un cambio.",
        "Trabajo 2: láminas 12 × 200 = 2.400; marcos 4 × 450 = 1.800; cordel 600; total $4.800; faltan $800. Cambio: reutilizar cartón para los marcos",
        ["presupuesto con cantidades y precios", "total correcto", "dice cuánto sobra o falta", "propone un cambio si falta"],
        ["tabla de presupuesto con total"],
        ["no multiplicar por la cantidad", "no comparar con el dinero disponible"],
        "Pregunta: «¿cuántas unidades hay de cada cosa?». Revisa la multiplicación de cada fila.",
    ),
    reinforce="Anota tres cosas que usas en la escuela con un precio ficticio y calcula cuánto costarían 5 de cada una.",
    extend="Explica por qué reutilizar un material puede bajar el costo de un trabajo, con un ejemplo en pesos.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja, lápiz y las tablas escritas en este cuaderno.",
    use="Aprenderé a distinguir los recursos que necesita un trabajo y a elegir recursos alternativos con criterios. Sirve para seguir adelante cuando falta algo.",
    prior=["Sé hacer un presupuesto.", "Sé que un criterio se puede comprobar.", "Sé qué es un material reutilizado."],
    explain=[
        "Los recursos son todo lo que se necesita para lograr un resultado: materiales, herramientas, personas, tiempo, dinero y energía. Un recurso necesario es el que el plan exige. Un recurso alternativo es otro que puede reemplazarlo y sirve para lo mismo. Los servicios también usan recursos: un reparto de colaciones necesita personas, tiempo y bandejas.",
        "Para elegir entre un recurso y su alternativa, compara con criterios: costo, disponibilidad, resistencia, cuidado del ambiente y seguridad. Una forma ordenada es una tabla con puntajes de 1 a 3 para cada criterio y sumar; en todos los criterios 3 es lo mejor (en costo, 3 es lo más barato). El recurso con más puntos cumple mejor, pero siempre revisa que no rompa una restricción.",
        "A veces no hay alternativa: entonces se cambia el diseño, se pide ayuda o se ajusta el plazo. Conviene dejar anotado en el plan qué alternativa elegiste y por qué. Así, otra persona puede repetir el trabajo aunque falte un material.",
    ],
    vocab=[("recurso", "lo que se necesita para lograr un resultado"), ("recurso alternativo", "recurso que puede reemplazar a otro"), ("disponibilidad", "si el recurso está a mano"), ("puntaje", "número que indica cuánto cumple un criterio"), ("restricción", "límite que no se puede romper")],
    worked=[
        ("Elegir una alternativa con puntajes", "Para hacer una base: A cartón nuevo (costo 1, ambiente 1, resistencia 3), B cartón reutilizado (costo 3, ambiente 3, resistencia 2). ¿Cuál suma más?", ["A suma 1 + 1 + 3 = 5.", "B suma 3 + 3 + 2 = 8."], "B, cartón reutilizado, con 8 puntos"),
        ("Verificar la restricción", "El mejor puntaje es una caja de madera, pero el trabajo debe usar solo materiales que se puedan cortar con tijeras de punta roma. ¿La eliges?", ["Reviso la restricción.", "La madera no se corta con tijeras de punta roma, así que rompe la restricción."], "No; se elige la mejor alternativa que cumpla la restricción"),
    ],
    mistakes=[
        ("Elegir la alternativa más barata sin revisar los demás criterios.", "Puede no aguantar el uso o dañar el ambiente.", "Compara todos los criterios y las restricciones."),
        ("Cambiar un material y no anotarlo en el plan.", "Nadie sabrá por qué el resultado es distinto.", "Anota qué alternativa elegiste y por qué."),
    ],
    R=[
        ("¿Una persona que ayuda en el trabajo es un recurso?", "Sí", "Las personas también son un recurso."),
        ("Un cartón reutilizado que reemplaza a uno nuevo, ¿es un recurso necesario o alternativo?", "Alternativo", "Reemplaza a otro recurso."),
        ("¿Qué es una restricción?", "Un límite que no se puede romper", "Marca lo que el plan no puede superar."),
    ],
    C=[
        ("¿Cuál es un criterio para comparar un material con su alternativa? A la resistencia, B el color de la etiqueta del precio.", "A", "La resistencia mide si el material aguanta el uso."),
        ("Si no hay alternativa para un material, ¿qué opción es válida? A cambiar el diseño, B ignorar el problema.", "A", "Se resuelve sin dejar una falla."),
        ("¿Por qué anotar la alternativa elegida en el plan?", "Para que otra persona pueda repetir el trabajo", "Queda claro qué se cambió."),
    ],
    A=[
        arith("Opción A suma 2 + 3 + 1 puntos y opción B suma 3 + 3 + 2 puntos. ¿Cuántos puntos más suma B?", "(3+3+2)-(2+3+1)", "Se comparan los totales de A y de B.", " puntos"),
        ("Una bolsa de tela y una bolsa de plástico desechable sirven para transportar materiales. Con criterio «reutilizable», ¿cuál conviene?", "La bolsa de tela", "Se puede usar muchas veces."),
        ("Para un reparto de colaciones, ¿cuál es un recurso alternativo de una bandeja? A una caja plana de cartón, B un guante.", "A", "La caja plana puede cumplir la misma función."),
    ],
    Z=[
        ("Tabla de puntajes. Cartón A: 5. Cartón B: 5. Cartón C: 4. Con un criterio de desempate, «menor costo», ¿qué falta para decidir?", "El costo de A y de B", "Con el mismo puntaje se necesita el dato del desempate."),
        ("Una alternativa cuesta $0 pero se rompe con una prueba de peso. ¿Se acepta?", "No", "No cumple el criterio de resistencia."),
    ],
    D=[
        arith("Material X: costo 3, ambiente 2, resistencia 3, seguridad 3. Material Y: costo 3, ambiente 3, resistencia 3, seguridad 3. ¿Cuántos puntos más suma Y que X?", "(3+3+3+3)-(3+2+3+3)", "Se suman los cuatro puntajes de cada uno y se restan.", " punto"),
        ("Un material gana en puntaje, pero cuesta $3.000 y el presupuesto es de $2.500. ¿Qué haces?", "Elijo la siguiente mejor opción que respete el presupuesto", "La restricción de dinero no se puede romper."),
    ],
    ctx=("Para un servicio de reparto de colaciones a 12 compañeros, el curso tiene 3 bandejas. Cada bandeja lleva 4 colaciones. Calcula si alcanzan las bandejas y, si no, propón un recurso alternativo.", "3 × 4 = 12; sí alcanzan. Alternativa si se rompe una bandeja: una caja plana de cartón", "Se multiplica y se propone una alternativa que cumpla la misma función."),
    sc=[
        ("¿Qué es un recurso alternativo?", "Uno que puede reemplazar a otro", "Cumple la misma función."),
        ("¿Qué debes revisar siempre antes de elegir una alternativa?", "Las restricciones", "No se pueden romper."),
        ("¿Dónde se anota la alternativa elegida?", "En el plan", "Así otros entienden el cambio."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: haces una maqueta y el cartón grueso se acabó; las opciones son cajas de cereal aplanadas (costo 3, ambiente 3, resistencia 2) y cartón nuevo (costo 1, ambiente 1, resistencia 3). Caso 2: para un servicio de limpieza de la sala faltan 2 paños; las opciones son una tela vieja limpia (costo 3, ambiente 3, resistencia 2) y papel absorbente nuevo (costo 1, ambiente 1, resistencia 2). Suma los puntos, elige y explica tu decisión con una restricción.",
        "Caso 1: cajas de cereal 8 puntos, cartón nuevo 5; elijo cajas porque cuestan menos y cuidan el ambiente",
        ["suma los puntos correctamente", "elige una opción", "explica con criterios", "menciona una restricción"],
        ["tabla de puntajes con decisión"],
        ["elegir solo por costo", "ignorar una restricción"],
        "Pregunta: «¿qué criterio pesó más y por qué?». Si no lo dice, pídele justificar con el puntaje.",
    ),
    reinforce="Elige un objeto de tu casa y nombra otro que podría reemplazarlo para la misma función.",
    extend="Explica una situación en que la alternativa más barata no es la mejor.",
)

# ------------------------------------------------------------------ OA 02, clase 5
reg(
    OA2, 5,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a discutir qué implicancias ambientales y sociales tienen los materiales y los pasos de un plan. Sirve para tomar decisiones que cuidan el ambiente y a las personas.",
    prior=["Sé qué es reutilizar.", "Sé que un recurso puede tener alternativas.", "Sé escuchar opiniones distintas."],
    explain=[
        "Toda elaboración tiene implicancias, es decir, consecuencias. Las ambientales son los efectos en la naturaleza: cuántos residuos se generan, cuánta energía y cuánta agua se usan. Las sociales son los efectos en las personas: quién se beneficia, a quién le sale más caro, quién puede usar el producto y si se respeta a quienes trabajan.",
        "Para reducir el impacto ambiental se usan las tres erres: reducir lo que usas, reutilizar lo que ya existe y reciclar lo que ya no sirve. Un material reutilizado genera menos residuos que uno nuevo. Elegir un material cercano también evita transportar de lejos y gastar más energía.",
        "Discutir implica dar razones y escuchar. Una buena opinión dice qué efecto tiene, a quién afecta y qué alternativa mejora la situación. Se puede decidir cambiar un material o un paso, siempre que el producto siga cumpliendo sus criterios. Anotar la decisión y su razón queda en el plan.",
    ],
    vocab=[("implicancia", "consecuencia de una decisión"), ("residuo", "material que se bota"), ("reducir", "usar menos"), ("reutilizar", "volver a usar sin transformar"), ("reciclar", "transformar un material usado en otro nuevo")],
    worked=[
        ("Clasificar una implicancia", "Un plan usa 20 vasos desechables de plástico para una actividad. ¿Qué implicancia ambiental tiene y qué alternativa propones?", ["Genera 20 residuos que se botan después de usar una vez.", "Alternativa: que cada persona traiga un vaso que se pueda lavar y usar de nuevo."], "Genera residuos; usar vasos reutilizables los reduce"),
        ("Pensar en las personas", "Un curso diseña un banco de cartón y pide a cada integrante $3.000. Es posible que no todas las personas puedan pagar. ¿Qué implicancia social hay y cómo se puede cambiar?", ["No todas las personas pueden participar por el costo.", "Se puede usar cartón reutilizado sin costo para todos."], "Excluye a quienes no pueden pagar; se cambia a cartón reutilizado"),
    ],
    mistakes=[
        ("Pensar que reciclar es lo único que cuida el ambiente.", "Reducir y reutilizar generan aún menos residuos.", "Aplica primero reducir, luego reutilizar y después reciclar."),
        ("Decidir sin preguntar a quienes usarán el producto.", "No se sabrá si el producto les sirve a todos.", "Escucha a las personas afectadas antes de decidir."),
    ],
    R=[
        ("Botar una caja después de un solo uso, ¿genera residuos o los evita?", "Genera residuos", "Se bota un material completo."),
        ("Usar de nuevo una caja de cartón sin transformarla, ¿es reducir, reutilizar o reciclar?", "Reutilizar", "Se vuelve a usar sin transformar."),
        ("Que un producto lo puedan usar personas de todas las edades, ¿es una implicancia ambiental o social?", "Social", "Se refiere a las personas."),
    ],
    C=[
        ("¿Cuáles son las tres erres?", "Reducir, reutilizar y reciclar", "Son las tres formas de cuidar el ambiente con los materiales."),
        ("¿Cuál es una implicancia ambiental? A «gasta mucha agua», B «lo disfrutan los adultos mayores».", "A", "El uso de agua es un efecto en la naturaleza."),
        ("¿Por qué conviene escuchar a quienes usarán un producto antes de decidir?", "Porque el producto debe servirles a ellas", "Sus necesidades definen si el diseño sirve."),
    ],
    A=[
        arith("Un curso botaba 3 bolsas plásticas por día durante 5 días. Si usan una bolsa de tela, ¿cuántas bolsas plásticas dejan de botar?", "3*5", "Se multiplican las bolsas diarias por los días.", " bolsas"),
        ("Una actividad necesita 25 platos. Opción A: platos desechables. Opción B: platos de cada casa que se lavan. ¿Cuál genera menos residuos?", "La opción B", "Se pueden usar muchas veces."),
        ("Un producto es muy caro y solo algunas personas pueden comprarlo. ¿Qué implicancia social tiene?", "Excluye a quienes no pueden pagar", "No todas las personas acceden al producto."),
    ],
    Z=[
        ("Dos grupos eligen materiales. Grupo A: cartón de cajas usadas de la escuela. Grupo B: cartón nuevo traído de lejos. ¿Cuál reduce residuos y transporte, y por qué?", "El grupo A, porque reutiliza y está cerca", "Reutilizar evita residuos y lo cercano gasta menos energía."),
        ("Un grupo dice: «Reciclar es mejor que reutilizar porque se transforma». ¿Qué respuesta da una mejor razón?", "Reutilizar evita transformar y usa menos energía", "No se necesita procesar el material."),
    ],
    D=[
        arith("Una escuela genera 40 residuos por semana en una actividad y logra reducirlos a la mitad. ¿Cuántos residuos genera ahora?", "40//2", "Reducir a la mitad es dividir entre 2.", " residuos"),
        ("Un curso quiere regalar 30 cuadernos de cartón a otro curso. Algunos materiales cuestan mucho. ¿Qué dos efectos, uno ambiental y uno social, conviene considerar?", "Residuos que genera y si el otro curso podrá usarlos", "El primero es ambiental y el segundo, social."),
    ],
    ctx=("El curso hará un mural con 50 tapas de botella plástica recolectadas en la escuela. Describe una implicancia ambiental y una social de usar esas tapas, y una decisión para mejorar.", "Ambiental: evita 50 residuos al reutilizar. Social: todos pueden participar porque no cuesta dinero. Decisión: pedir tapas de varias familias", "Une efectos en la naturaleza y en las personas con una decisión."),
    sc=[
        ("¿Qué son las implicancias ambientales?", "Los efectos en la naturaleza", "Incluyen residuos, energía y agua."),
        ("¿Qué son las implicancias sociales?", "Los efectos en las personas", "Incluyen acceso, costo y respeto."),
        ("¿Qué se anota al decidir cambiar un material?", "La decisión y su razón", "Queda registrado en el plan."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: el curso quiere hacer 20 carpetas de plástico nuevo para guardar trabajos. Caso 2: el curso quiere preparar un servicio de entrega de diarios murales con hojas nuevas todos los meses. Escribe una implicancia ambiental, una implicancia social, una alternativa que mejore ambas y la razón de tu decisión.",
        "Caso 1: ambiental: plástico nuevo genera residuos. Social: cada integrante debería pagar. Alternativa: carpetas de cartón reutilizado. Razón: reduce residuos y no cuesta",
        ["implicancia ambiental", "implicancia social", "alternativa concreta", "razón de la decisión"],
        ["texto con implicancias, alternativa y razón"],
        ["solo hablar del dinero", "no dar razones"],
        "Pregunta: «¿a quién afecta y cómo?». Si no responde, pídele completar la implicancia social.",
    ),
    reinforce="Revisa un objeto desechable de tu casa y escribe cómo podrías reutilizarlo.",
    extend="Explica por qué una decisión puede tener ventaja ambiental y desventaja social al mismo tiempo, con un ejemplo.",
)
