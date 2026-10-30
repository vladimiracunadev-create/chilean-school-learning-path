"""Cuaderno del estudiante de 4.º básico Matemática: OA 07 (problemas de dinero) y OA 08 (fracciones)."""
from __future__ import annotations

from student_content_ma04_a import M, W, lesson, task
from student_lessons import arith, ex

OA7 = "MA04 OA 07"
OA8 = "MA04 OA 08"

# ------------------------------------------------------------------ OA 07
lesson(
    OA7, 1,
    use="Aprenderé a leer un problema con dinero y a separar los datos de la pregunta. Sirve para saber qué calcular antes de hacer cuentas.",
    prior=["Sé sumar, restar y multiplicar números hasta 10.000.", "Conozco las monedas de $ 10, $ 50, $ 100 y $ 500 y los billetes de $ 1.000, $ 2.000, $ 5.000 y $ 10.000."],
    explain=[
        "En un problema de dinero hay datos y una pregunta. Los datos son los números y lo que significan: el precio es lo que cuesta una cosa, la cantidad es cuántas cosas se compran y el pago es el dinero que entrego. La pregunta dice qué hay que averiguar: el total, el vuelto o cuánto cuesta cada uno.",
        "Antes de calcular, escribe cada dato con su nombre. En «Compro 3 lápices de $ 250 cada uno», el precio es $ 250 y la cantidad es 3. Se busca el total. Un dibujo de barras ayuda: tres barras iguales de $ 250 forman el total.",
        "El vuelto es lo que te devuelven cuando pagas con más dinero que el precio. Se calcula con una resta: lo que pagas menos lo que cuesta. Si pagas con $ 1.000 algo de $ 650, el vuelto es $ 1.000 − $ 650 = $ 350.",
    ],
    vocab=[("precio", "lo que cuesta una cosa"), ("cantidad", "cuántas cosas se compran"), ("total", "todo el dinero que cuesta la compra"), ("vuelto", "dinero que devuelven cuando se paga con más de lo que cuesta"), ("pago", "dinero que se entrega")],
    worked=[
        W("Identificar y calcular el total", "Compro 3 lápices de $ 250 cada uno. ¿Cuánto pago en total?", ["Precio de uno: $ 250. Cantidad: 3. Se busca el total.", "Son 3 grupos iguales de $ 250: multiplico 3 × 250.", "3 × 250 = 750."], "$ 750"),
        W("Calcular el vuelto", "Pago con un billete de $ 1.000 una cuenta de $ 650. ¿Cuánto es el vuelto?", ["Pago: $ 1.000. Precio: $ 650. Se busca el vuelto.", "El vuelto es el pago menos el precio: 1.000 − 650.", "1.000 − 650 = 350."], "$ 350"),
    ],
    mistakes=[
        M("Sumar 3 + 250 en «3 lápices de $ 250».", "Se juntan cantidad y precio, que son datos de distinto tipo.", "Cuando hay una cantidad de cosas iguales, se multiplica: 3 × 250."),
        M("Calcular el vuelto como 650 − 1.000.", "Se resta al revés.", "Al vuelto se llega con el pago menos el precio: 1.000 − 650."),
    ],
    rec=[
        ex("En «Compro 4 reglas de $ 200 cada una», ¿cuál es el precio de una regla y cuál es la cantidad?", "Precio $ 200; cantidad 4", "El precio es lo que cuesta uno y la cantidad es cuántos se compran."),
        arith("Compro 4 reglas de $ 200 cada una. ¿Cuánto pago en total?", "4*200", "Son 4 grupos iguales de $ 200."),
        arith("Pago con $ 1.000 una cuenta de $ 720. ¿Cuánto es el vuelto?", "1000-720", "Vuelto es pago menos precio."),
    ],
    und=[
        ex("En «Pagué con $ 2.000 un juguete de $ 1.350», ¿cuál es el pago y cuál es el precio?", "Pago $ 2.000; precio $ 1.350", "El pago es lo que entregué y el precio es lo que cuesta."),
        ex("En «5 cuadernos a $ 300 cada uno», ¿qué palabras muestran que son grupos iguales?", "Cada uno", "«Cada uno» dice que todos cuestan lo mismo."),
        ex("Si te piden el vuelto, ¿qué se calcula: el pago menos el precio o el precio menos el pago?", "El pago menos el precio", "El vuelto es lo que sobra del pago."),
    ],
    app=[
        arith("Una bolsa de pan cuesta $ 1.200 y una de leche cuesta $ 950. ¿Cuánto cuestan las dos juntas?", "1200+950", "Se juntan los precios: es una suma."),
        arith("Compro 5 cuadernos a $ 300 cada uno. ¿Cuánto pago en total?", "5*300", "5 grupos iguales de $ 300."),
        arith("Pago con $ 2.000 un juguete de $ 1.350. ¿Cuánto es el vuelto?", "2000-1350", "Pago menos precio."),
    ],
    rea=[
        ex("4 cuadernos iguales cuestan $ 2.000 en total. ¿Cuánto cuesta cada uno?", "$ 500", "4 × 500 = 2.000, así que cada uno cuesta $ 500."),
        ex("Lola dice que para el vuelto se suma lo que pagó con el precio. ¿Qué operación corresponde en realidad?", "Una resta", "El vuelto es lo que sobra del pago: pago − precio."),
    ],
    cha=[
        ex("Con $ 5.000 compro 2 cajas de $ 1.500 cada una y un cuaderno de $ 800. ¿Cuánto vuelto recibo?", "$ 1.200", "2 × 1.500 = 3.000; 3.000 + 800 = 3.800; 5.000 − 3.800 = 1.200."),
        ex("¿Cuántos billetes de $ 1.000 se necesitan para pagar exactos $ 7.000?", "7", "7 × 1.000 = 7.000."),
    ],
    ctx=[ex("En la feria, un kilo de tomates cuesta $ 1.200. ¿Cuánto se paga por 2 kilos?", "$ 2.400", "2 grupos iguales de $ 1.200: 2 × 1.200 = 2.400.")],
    sc=[
        arith("3 gomas cuestan $ 150 cada una. ¿Cuánto cuestan en total?", "3*150", "3 grupos iguales de $ 150."),
        ex("En «4 helados a $ 600 cada uno», ¿cuál es la cantidad?", "4", "La cantidad es cuántos helados se compran."),
        arith("Pago con $ 500 algo que cuesta $ 380. ¿Cuánto es el vuelto?", "500-380", "Pago menos precio."),
    ],
    op=task(
        "Lee este problema: «Ema compra 2 jugos de $ 450 cada uno y paga con un billete de $ 2.000». Escribe los datos con su nombre (precio, cantidad, pago), dibuja un esquema de barras y escribe dos preguntas que se pueden responder, una para el total y otra para el vuelto. Responde las dos.",
        "Datos: precio $ 450, cantidad 2, pago $ 2.000. Total: 2 × 450 = $ 900. Vuelto: 2.000 − 900 = $ 1.100. Esquema: dos barras de 450 forman 900; del billete de 2.000 quedan 1.100.",
        ["nombra bien los datos", "dibuja el esquema", "escribe las dos preguntas", "responde con unidad"],
        ["datos escritos", "esquema de barras", "dos preguntas con respuesta"],
        ["restar el pago antes de calcular el total", "olvidar el signo $"],
        "Reconoce el esquema y pide que explique con sus palabras qué representa cada número antes de operar.",
    ),
    reinforce="Con monedas dibujadas, representa un pago de $ 650 con billetes y monedas y calcula el vuelto si pagas con $ 1.000.",
    extend="Escribe un problema en que el precio sea $ 350, la cantidad 4 y el pago $ 2.000, y respóndelo.",
)

lesson(
    OA7, 2,
    use="Aprenderé a elegir la operación correcta en problemas de dinero y a explicar por qué la elegí. Sirve para no confundirme entre sumar, restar, multiplicar o dividir.",
    prior=["Sé identificar el precio, la cantidad, el total y el vuelto.", "Sé sumar, restar, multiplicar y dividir con números de una y dos cifras."],
    explain=[
        "Cada operación responde a una situación. Se suma cuando se juntan precios distintos. Se resta cuando se busca el vuelto, lo que falta o cuánto más cuesta una cosa que otra. Se multiplica cuando hay varias cosas del mismo precio. Se divide cuando se reparte o se paga en cuotas iguales.",
        "Para elegir, pregúntate qué pasa con el dinero en la historia. Si dice «cada uno», «cada» o «por», piensa en grupos iguales. Si dice «en partes iguales» o «entre», piensa en dividir. Si dice «cuánto más» o «cuánto falta», piensa en restar.",
        "Justificar es decir por qué elegiste la operación. Por ejemplo: «Multipliqué porque son 3 jugos del mismo precio». Una buena justificación nombra los datos y la situación. Después calcula y comprueba con la operación inversa.",
    ],
    vocab=[("operación", "cálculo que se hace: suma, resta, multiplicación o división"), ("justificar", "explicar por qué elegí algo"), ("cuota", "parte del pago que se hace cada vez"), ("repartir", "dar partes iguales"), ("operación inversa", "la que deshace a otra")],
    worked=[
        W("Multiplicar y justificar", "Ana compra 3 jugos de $ 450 cada uno. ¿Cuánto paga?", ["Son 3 cosas del mismo precio: «cada uno».", "Elijo multiplicar porque son grupos iguales.", "3 × 450 = 1.350. Compruebo: 450 + 450 + 450 = 1.350."], "$ 1.350"),
        W("Dividir y justificar", "Se reparten $ 1.200 entre 4 hermanos en partes iguales. ¿Cuánto recibe cada uno?", ["Dice «entre» y «partes iguales».", "Elijo dividir: 1.200 ÷ 4.", "1.200 ÷ 4 = 300. Compruebo: 300 × 4 = 1.200."], "$ 300"),
    ],
    mistakes=[
        M("Sumar 3 + 450 para 3 jugos de $ 450.", "Se suman los números sin ver que son grupos iguales.", "Multiplica el precio por la cantidad: 3 × 450."),
        M("Calcular 1.200 × 4 para repartir $ 1.200 entre 4.", "Se multiplica cuando la situación es de reparto.", "Repartir en partes iguales es dividir: 1.200 ÷ 4."),
    ],
    rec=[
        arith("Un jugo cuesta $ 450 y una galleta $ 300. ¿Cuánto cuestan los dos?", "450+300", "Se juntan dos precios distintos."),
        arith("Tomás compra 5 galletas de $ 300 cada una. ¿Cuánto paga?", "5*300", "Grupos iguales: se multiplica."),
        arith("Se reparten $ 1.800 entre 3 hermanos en partes iguales. ¿Cuánto recibe cada uno?", "1800//3", "Partes iguales: se divide."),
    ],
    und=[
        ex("¿Qué operación sirve para saber cuánto toca a cada uno al repartir dinero en partes iguales?", "División", "Repartir en partes iguales es dividir."),
        ex("¿Qué operación sirve para el total de 6 entradas del mismo precio?", "Multiplicación", "Hay 6 grupos iguales."),
        ex("¿Qué operación sirve para saber cuánto más cuesta una polera que un gorro?", "Resta", "Comparar «cuánto más» es restar."),
    ],
    app=[
        arith("Una entrada al teatro cuesta $ 1.500. ¿Cuánto cuestan 4 entradas?", "4*1500", "4 grupos iguales de $ 1.500."),
        arith("Seis amigos pagan en partes iguales una cuenta de $ 4.800. ¿Cuánto paga cada uno?", "4800//6", "Partes iguales: se divide."),
        arith("Una polera cuesta $ 12.000 y un gorro $ 7.000. ¿Cuánto más cuesta la polera?", "12000-7000", "«Cuánto más» se resuelve restando."),
    ],
    rea=[
        ex("Teo sumó 3 + 450 en «3 jugos de $ 450» y obtuvo 453. ¿Qué hizo mal y cuánto es lo correcto?", "Sumó cantidad y precio; es 3 × 450 = $ 1.350", "Son 3 grupos iguales de $ 450."),
        ex("Rosa dice que para repartir $ 1.200 entre 4 se calcula 1.200 × 4. ¿Es correcto?", "No, se divide: $ 300", "Repartir es dividir: 1.200 ÷ 4 = 300."),
    ],
    cha=[
        ex("Compro 3 poleras de $ 2.000 y 3 gorros de $ 1.000. Calcula (3 × 2.000) + (3 × 1.000) y 3 × (2.000 + 1.000). ¿Coinciden?", "Sí, ambos dan $ 9.000", "6.000 + 3.000 = 9.000 y 3 × 3.000 = 9.000."),
        ex("Se pagó $ 3.600 por 6 cosas iguales. ¿Cuánto cuesta cada una?", "$ 600", "6 × 600 = 3.600."),
    ],
    ctx=[ex("Un curso de 5 estudiantes compra una caja de pinturas de $ 4.500 y pagan en partes iguales. ¿Cuánto paga cada uno?", "$ 900", "4.500 ÷ 5 = 900 porque 5 × 900 = 4.500.")],
    sc=[
        arith("Un helado cuesta $ 600. ¿Cuánto cuestan 3 helados?", "3*600", "3 grupos iguales."),
        arith("Se reparten $ 900 entre 3 niños en partes iguales. ¿Cuánto recibe cada uno?", "900//3", "Repartir es dividir."),
        arith("Compro un cuaderno de $ 800 y un lápiz de $ 250. ¿Cuánto pago?", "800+250", "Se juntan dos precios."),
    ],
    op=task(
        "Elige una de estas tres situaciones y resuélvela: a) 5 pasajes de bus a $ 700 cada uno; b) $ 2.400 repartidos entre 6 personas; c) un libro de $ 6.500 y otro de $ 4.200, ¿cuánto más cuesta el primero? Escribe la operación, el cálculo y una frase que justifique por qué elegiste esa operación.",
        "a) 5 × 700 = $ 3.500: multipliqué porque son 5 pasajes del mismo precio. b) 2.400 ÷ 6 = $ 400: dividí porque se reparte en partes iguales. c) 6.500 − 4.200 = $ 2.300: resté porque pide «cuánto más».",
        ["elige la operación correcta", "calcula bien", "justifica con la situación"],
        ["operación y cálculo escritos", "frase de justificación"],
        ["elegir la operación por el tamaño de los números", "no justificar"],
        "Pide que explique la situación con sus palabras antes de calcular; si falla, revisa qué palabra clave del problema lo guía.",
    ),
    reinforce="Escribe una situación de compra para cada operación: sumar, restar, multiplicar y dividir.",
    extend="Calcula el vuelto de pagar con $ 10.000 tres poleras de $ 2.500 cada una y justifica cada operación.",
)

lesson(
    OA7, 3,
    use="Aprenderé a resolver problemas de dinero con varios pasos y a organizar los cálculos. Sirve para manejar un presupuesto y saber cuánto queda después de varias compras.",
    prior=["Sé elegir la operación según la situación.", "Sé calcular el vuelto y el total."],
    explain=[
        "Un problema de varios pasos pide más de una operación. Primero decide qué averiguar en cada paso. Por ejemplo, para saber el vuelto de 3 cuadernos de $ 450 pagados con $ 2.000, primero calculas el total (3 × 450 = 1.350) y después el vuelto (2.000 − 1.350 = 650).",
        "Un presupuesto es el dinero que tienes para gastar. Si tienes $ 5.000 y compras dos entradas de $ 1.200 y un helado de $ 900, calculas cuánto gastas: 2 × 1.200 + 900 = 3.300. Lo que queda es 5.000 − 3.300 = 1.700.",
        "Organiza tus pasos en una lista o un esquema. Escribe qué buscas en cada paso y su resultado. Al final, vuelve a leer la pregunta y comprueba que respondes lo que preguntan: a veces piden lo que queda, no lo que gastaste. Estima para revisar.",
    ],
    vocab=[("presupuesto", "dinero que se tiene o se planea gastar"), ("varios pasos", "más de una operación para llegar a la respuesta"), ("gasto", "dinero que se usa en compras"), ("vuelto", "dinero que devuelven"), ("estimar", "calcular un resultado cercano")],
    worked=[
        W("Total y vuelto", "Compro 3 cuadernos de $ 450 cada uno y pago con un billete de $ 2.000. ¿Cuánto es el vuelto?", ["Paso 1: total de los cuadernos. 3 × 450 = 1.350.", "Paso 2: vuelto. 2.000 − 1.350 = 650.", "Compruebo: 1.350 + 650 = 2.000."], "$ 650"),
        W("Presupuesto", "Tengo $ 5.000. Compro 2 entradas de $ 1.200 y un helado de $ 900. ¿Cuánto me queda?", ["Paso 1: entradas. 2 × 1.200 = 2.400.", "Paso 2: gasto total. 2.400 + 900 = 3.300.", "Paso 3: lo que queda. 5.000 − 3.300 = 1.700."], "$ 1.700"),
    ],
    mistakes=[
        M("Responder $ 1.350 en el problema del vuelto.", "Se responde el resultado del primer paso, no lo que pregunta el problema.", "Vuelve a leer la pregunta: piden el vuelto, 2.000 − 1.350 = 650."),
        M("Restar 5.000 − 1.200 − 900 sin multiplicar las 2 entradas.", "Se olvida la cantidad de entradas.", "Son 2 entradas: 2 × 1.200 = 2.400."),
    ],
    rec=[
        arith("Compro 2 cuadernos de $ 600 cada uno. ¿Cuánto pago?", "2*600", "Paso 1: total."),
        arith("Compro 2 cuadernos de $ 600 y pago con $ 2.000. ¿Cuánto es el vuelto?", "2000-2*600", "Primero el total y luego el vuelto."),
        arith("Gasté $ 1.450 de $ 2.000. ¿Cuánto me queda?", "2000-1450", "Se resta lo gastado."),
    ],
    und=[
        ex("Para saber el vuelto de 3 cuadernos de $ 450 pagados con $ 2.000, ¿qué se calcula primero?", "El total de los cuadernos", "Hay que saber cuánto se gastó antes de restar."),
        ex("En «Tengo $ 5.000 y compro dos entradas y un helado», ¿qué pregunta responde la resta 5.000 − 3.300?", "Cuánto dinero me queda", "Es el presupuesto menos el gasto."),
        ex("Si el problema pide «cuánto me queda» y calculas el gasto, ¿falta un paso?", "Sí, restar el gasto al presupuesto", "El gasto no es lo que queda."),
    ],
    app=[
        arith("Tengo $ 6.000. Compro 2 entradas de $ 1.500 y un helado de $ 800. ¿Cuánto me queda?", "6000-2*1500-800", "Primero el gasto y luego lo que queda."),
        arith("Una familia compra 4 pasajes de $ 1.500 y un seguro de $ 800. ¿Cuánto pagan en total?", "4*1500+800", "Primero los pasajes, luego se suma el seguro."),
        arith("Pago con $ 10.000 dos poleras de $ 3.500 cada una. ¿Cuánto es el vuelto?", "10000-2*3500", "Total de las poleras y luego el vuelto."),
    ],
    rea=[
        ex("Camila calculó el vuelto de 3 cuadernos de $ 450 pagados con $ 2.000 y respondió $ 1.350. ¿Qué respondió en realidad?", "El total de los cuadernos; el vuelto es $ 650", "1.350 es el total; falta restar: 2.000 − 1.350 = 650."),
        ex("Un estudiante dice que con $ 5.000 alcanza para 2 entradas de $ 1.200 y un helado de $ 900. Estima: ¿tiene razón?", "Sí", "Aproximadamente 2.400 + 900 = 3.300, que es menos de 5.000."),
    ],
    cha=[
        ex("Con $ 10.000 compro 3 libros de $ 2.500 cada uno y un juego de $ 1.800. ¿Cuánto me queda?", "$ 700", "3 × 2.500 = 7.500; 7.500 + 1.800 = 9.300; 10.000 − 9.300 = 700."),
        ex("Tengo $ 3.000 y un helado cuesta $ 600. ¿Cuántos helados completos puedo comprar?", "5", "5 × 600 = 3.000 y 6 × 600 = 3.600, que es más de 3.000."),
    ],
    ctx=[ex("Una familia de 4 va al cine. Cada entrada cuesta $ 3.000 y gastan $ 2.500 en palomitas. Pagan con $ 20.000. ¿Cuánto es el vuelto?", "$ 5.500", "4 × 3.000 = 12.000; 12.000 + 2.500 = 14.500; 20.000 − 14.500 = 5.500.")],
    sc=[
        arith("Compro 3 cosas de $ 400 cada una y pago con $ 2.000. ¿Cuánto es el vuelto?", "2000-3*400", "Total 1.200 y vuelto 800."),
        arith("Gasto $ 2.400 en entradas y $ 900 en un helado. ¿Cuánto gasté en total?", "2400+900", "Se suman los gastos."),
        ex("Si piden «cuánto me queda», ¿restas el gasto al presupuesto o sumas ambos?", "Resto el gasto al presupuesto", "Lo que queda es el presupuesto menos el gasto."),
    ],
    op=task(
        "Resuelve en pasos: «Marta tiene $ 8.000. Compra 3 cuadernos de $ 1.200 cada uno y una mochila de $ 3.500. ¿Cuánto dinero le queda?». Escribe un paso por línea, estima antes y comprueba al final sumando lo que gastó y lo que le queda.",
        "Paso 1: 3 × 1.200 = 3.600. Paso 2: 3.600 + 3.500 = 7.100. Paso 3: 8.000 − 7.100 = 900. Estimación: 3 × 1.200 es cerca de 3 × 1.000 = 3.000; 3.000 + 3.500 = 6.500, un poco menos que 7.100 porque redondeé hacia abajo. Comprobación: 7.100 + 900 = 8.000. Respuesta: le quedan $ 900.",
        ["identifica los pasos", "calcula bien", "estima y comprueba", "responde lo que se pregunta"],
        ["pasos escritos", "estimación y comprobación", "respuesta con unidad"],
        ["responder el gasto en vez de lo que queda", "olvidar la cantidad de cuadernos"],
        "Pide que subraye la pregunta y verifique que su respuesta final la contesta.",
    ),
    reinforce="Resuelve «Tengo $ 2.000 y compro 2 helados de $ 700. ¿Cuánto me queda?» en dos pasos.",
    extend="Inventa un problema de tres pasos con un presupuesto de $ 10.000 y resuélvelo.",
)

lesson(
    OA7, 4,
    use="Aprenderé a crear un problema de dinero y a revisar si está completo y bien resuelto. Sirve para entender mejor cómo se arma un problema y detectar errores.",
    prior=["Sé resolver problemas de dinero de uno y varios pasos.", "Sé comprobar con la operación inversa."],
    explain=[
        "Para crear un buen problema de dinero necesitas una historia con datos completos y una pregunta clara. Los datos suelen ser precios, cantidades y pagos. La pregunta debe poder responderse solo con esos datos. Por ejemplo: «Compro cuadernos de $ 700. ¿Cuánto pago?» no tiene respuesta, porque falta la cantidad.",
        "Después resuelve tu problema y escribe la respuesta con unidad. Revisa tres cosas: que la operación sea la correcta, que el cálculo esté bien y que la respuesta tenga sentido. Por ejemplo, un vuelto no puede ser mayor que lo que pagaste.",
        "Verificar es comprobar el resultado de otra manera. Si sumaste, resta; si multiplicaste, divide; si calculaste el vuelto, suma el vuelto y el precio y mira si da el pago. También puedes estimar con números redondeados. Si tu resultado y tu comprobación no coinciden, revisa el problema desde el principio.",
    ],
    vocab=[("dato", "información numérica que da el problema"), ("pregunta", "lo que el problema pide averiguar"), ("verificar", "comprobar que una respuesta está bien"), ("operación inversa", "la que deshace a otra"), ("coherente", "que tiene sentido y no se contradice")],
    worked=[
        W("Completar un problema", "El problema «Compro cuadernos de $ 700. ¿Cuánto pago?» no se puede resolver. ¿Qué falta y cómo se completa?", ["Pregunto: ¿se puede calcular el total? Para eso necesito la cantidad.", "Falta cuántos cuadernos se compran.", "Lo completo: «Compro 3 cuadernos de $ 700 cada uno. ¿Cuánto pago?». Respuesta: 3 × 700 = 2.100."], "Falta la cantidad: con 3 cuadernos son $ 2.100"),
        W("Verificar un vuelto", "Alguien dice que el vuelto de pagar $ 2.000 una cuenta de $ 1.350 es $ 550. Verifica.", ["Comprobación: vuelto + precio debe dar el pago.", "550 + 1.350 = 1.900, y el pago fue 2.000.", "No coincide: el vuelto correcto es 2.000 − 1.350 = 650. Compruebo: 650 + 1.350 = 2.000."], "El vuelto correcto es $ 650"),
    ],
    mistakes=[
        M("Escribir un problema sin pregunta o con una pregunta que no se puede responder.", "Faltan datos o no se dice qué se busca.", "Revisa que cada dato necesario esté escrito y que la pregunta pida algo concreto."),
        M("Dar un vuelto de $ 3.000 al pagar con $ 2.000.", "El resultado no es coherente: el vuelto no puede superar al pago.", "Revisa la operación: el vuelto es pago menos precio y es menor que el pago."),
    ],
    rec=[
        ex("En «Compro cuadernos de $ 700. ¿Cuánto pago?», ¿qué dato falta?", "La cantidad de cuadernos", "Sin saber cuántos son, no se puede calcular el total."),
        arith("Compro 3 cuadernos de $ 700 cada uno. ¿Cuánto pago?", "3*700", "Grupos iguales."),
        ex("Un problema dice «Pagué $ 2.000 y un helado cuesta $ 900». ¿Qué pregunta lleva a calcular 2.000 − 900?", "¿Cuánto es el vuelto?", "La resta pago − precio da el vuelto."),
    ],
    und=[
        ex("Para verificar que 3 × 700 = 2.100, ¿qué división sirve?", "2.100 ÷ 3 = 700", "La división deshace la multiplicación."),
        ex("Para verificar un vuelto de $ 650 al pagar $ 1.350 con $ 2.000, ¿qué suma haces?", "650 + 1.350 = 2.000", "El vuelto y el precio deben sumar el pago."),
        ex("¿Puede el vuelto de un pago de $ 2.000 ser $ 3.000?", "No", "El vuelto es siempre menor que el pago."),
    ],
    app=[
        arith("Verifica el vuelto: pago $ 5.000 una cuenta de $ 3.800. Calcula el vuelto.", "5000-3800", "Pago menos precio."),
        arith("Verifica sumando: vuelto $ 1.200 más precio $ 3.800.", "1200+3800", "Debe dar el pago de $ 5.000."),
        arith("Un problema dice que 4 entradas cuestan $ 6.000. Calcula el precio de una.", "6000//4", "Total dividido en 4 grupos iguales."),
    ],
    rea=[
        ex("Pía dice que 5 helados de $ 600 cuestan $ 3.500. Verifica con la división: ¿está bien?", "No, cuestan $ 3.000", "3.500 ÷ 5 = 700, no 600. Lo correcto: 5 × 600 = 3.000."),
        ex("En «Compro 2 libros y pago $ 7.000. ¿Cuánto paga?» ¿se puede resolver con esos datos?", "No, faltan los precios", "No se conoce el precio de cada libro."),
    ],
    cha=[
        ex("«Pagué con $ 5.000 y recibí $ 1.200 de vuelto. ¿Cuánto costó la compra?» Resuélvelo con una resta.", "$ 3.800", "5.000 − 1.200 = 3.800."),
        ex("Tengo $ 4.000 y quiero comprar 3 útiles de $ 1.200 cada uno. Verifica con una multiplicación: ¿me alcanza el dinero?", "Sí, me alcanza", "3 × 1.200 = 3.600, que es menos de 4.000; sobran $ 400."),
    ],
    ctx=[ex("En la feria, un puesto vende 3 bolsas de manzanas a $ 1.800 cada una. Si pagas con $ 10.000, ¿cuál es el vuelto? Verifica sumando.", "$ 4.600", "3 × 1.800 = 5.400; 10.000 − 5.400 = 4.600; 4.600 + 5.400 = 10.000.")],
    sc=[
        ex("¿Qué debe tener un problema de dinero además de datos?", "Una pregunta", "Sin pregunta no se sabe qué calcular."),
        arith("Verifica: 6 × 500.", "6*500", "El total de 6 cosas de $ 500."),
        ex("Si el total es $ 3.000 por 5 cosas iguales, ¿cuánto cuesta cada una?", "$ 600", "3.000 ÷ 5 = 600."),
    ],
    op=task(
        "Crea un problema de dinero con tres pasos usando estos datos: un jugo de $ 800, una galleta de $ 400 y un pago con billete de $ 5.000, comprando 3 jugos y 2 galletas. Escribe el enunciado con su pregunta, resuélvelo y verifícalo con una operación inversa.",
        "Problema: «Compro 3 jugos de $ 800 y 2 galletas de $ 400 y pago con $ 5.000. ¿Cuánto es el vuelto?». 3 × 800 = 2.400; 2 × 400 = 800; 2.400 + 800 = 3.200; 5.000 − 3.200 = 1.800. Verificación: 1.800 + 3.200 = 5.000.",
        ["problema completo con pregunta", "usa las operaciones correctas", "resuelve bien", "verifica"],
        ["enunciado escrito", "resolución", "verificación"],
        ["pregunta que no se puede responder", "vuelto mayor que el pago"],
        "Pide que otra persona lea el problema y diga si falta algún dato antes de resolverlo.",
    ),
    reinforce="Escribe un problema con 4 helados de $ 500 y un pago de $ 5.000, resuélvelo y verifica.",
    extend="Cambia un dato de tu problema para que el vuelto sea $ 1.000 y vuelve a verificar.",
)

# ------------------------------------------------------------------ OA 08
lesson(
    OA8, 1,
    use="Aprenderé qué es una fracción: cuando un entero se divide en partes iguales y se toman algunas. Sirve para hablar de partes de una pizza, una tira o una hoja.",
    prior=["Sé dividir en partes iguales.", "Conozco las palabras mitad y cuarto."],
    explain=[
        "Un entero es un objeto completo, como una tira, una pizza o una hoja. Una fracción dice cuántas partes iguales se toman de un entero. Se escribe con dos números separados por una raya, por ejemplo 3/8. El denominador, abajo, dice en cuántas partes iguales se dividió el entero.",
        "El numerador, arriba, dice cuántas de esas partes se toman. En 3/8 el entero se dividió en 8 partes iguales y se toman 3. Las partes deben ser iguales: si una parte es más grande, no se puede hablar de octavos. Cada parte de un entero dividido en 4 partes iguales es 1/4, un cuarto.",
        "Algunos nombres: 1/2 se lee un medio, 1/3 un tercio, 1/4 un cuarto, 1/5 un quinto, 1/6 un sexto, 1/8 un octavo, 1/10 un décimo, 1/12 un doceavo y 1/100 un centésimo. Siempre pregúntate: ¿en cuántas partes iguales está dividido el entero y cuántas tomé?",
    ],
    vocab=[("entero", "el objeto o cantidad completa"), ("fracción", "número que dice cuántas partes iguales de un entero se toman"), ("numerador", "número de arriba: cuántas partes se toman"), ("denominador", "número de abajo: en cuántas partes iguales se divide el entero"), ("partes iguales", "partes que tienen el mismo tamaño")],
    worked=[
        W("Leer una fracción", "Una pizza se corta en 8 partes iguales y Ana come 3. ¿Qué fracción comió?", ["El entero (la pizza) se dividió en 8 partes iguales: denominador 8.", "Ana tomó 3 partes: numerador 3.", "Se escribe 3/8 y se lee tres octavos."], "3/8"),
        W("Partes que no son iguales", "Una tira se corta en 3 partes: una grande y dos pequeñas. ¿Cada parte es 1/3?", ["Para hablar de tercios, las 3 partes deben ser iguales.", "Aquí una parte es más grande que las otras.", "Por eso ninguna parte es 1/3."], "No, las partes no son iguales"),
    ],
    mistakes=[
        M("Decir que una tira cortada en 3 partes desiguales tiene tercios.", "Se cuentan las partes sin mirar si son iguales.", "Las partes deben tener el mismo tamaño."),
        M("Escribir 8/3 para 3 partes de un entero dividido en 8.", "Se cambian el numerador y el denominador.", "Abajo va el total de partes iguales (8) y arriba las que se toman (3): 3/8."),
    ],
    rec=[
        ex("Una barra de chocolate se parte en 4 partes iguales. ¿Cómo se escribe cada parte?", "1/4", "Cada parte es una de 4 partes iguales."),
        ex("Una tira se corta en 3 partes iguales y se pinta 1. ¿Qué fracción está pintada?", "1/3", "1 parte de 3 partes iguales."),
        ex("En la fracción 1/5, ¿en cuántas partes iguales se dividió el entero?", "5", "El denominador dice en cuántas partes iguales se divide."),
    ],
    und=[
        ex("En 3/8, ¿cuál es el numerador y cuál es el denominador?", "Numerador 3; denominador 8", "El numerador está arriba y el denominador abajo."),
        ex("Una tira se divide en 4 partes de distinto tamaño. ¿Cada parte es 1/4?", "No", "Las partes deben ser iguales."),
        ex("Un entero se parte en 2 partes iguales. ¿Cómo se lee cada parte?", "Un medio, 1/2", "Dos partes iguales son mitades."),
    ],
    app=[
        ex("Una pizza se corta en 8 partes iguales y Luis come 5. ¿Qué fracción comió?", "5/8", "5 partes de 8 partes iguales."),
        ex("Se pintan 5 de 6 partes iguales de una hoja. ¿Qué fracción está pintada?", "5/6", "5 partes de 6 partes iguales."),
        ex("Una cinta se divide en 10 partes iguales y se cortan 7. ¿Qué fracción se cortó?", "7/10", "7 partes de 10 partes iguales."),
    ],
    rea=[
        ex("Una tira se cortó en 3 partes: una grande y dos pequeñas. Beto dice que cada parte es 1/3. ¿Tiene razón?", "No", "Las partes no son iguales."),
        ex("Dos tiras del mismo tamaño se parten, una en 2 partes iguales y otra en 4. ¿Qué parte es más grande: 1/2 de la primera o 1/4 de la segunda?", "1/2", "Menos partes significa partes más grandes."),
    ],
    cha=[
        ex("Cada parte de un entero es 1/6. ¿Cuántas de esas partes forman el entero?", "6", "6 partes de 1/6 forman todo el entero."),
        ex("Una tira de 12 cm se parte en 4 partes iguales. ¿Cuánto mide cada parte?", "3 cm", "12 ÷ 4 = 3."),
    ],
    ctx=[ex("Una tableta de chocolate tiene 12 cuadraditos iguales. Si comes 5, ¿qué fracción de la tableta comiste?", "5/12", "5 partes de 12 partes iguales.")],
    sc=[
        ex("Si un entero se divide en 5 partes iguales, ¿cómo se escribe 1 parte?", "1/5", "1 parte de 5 partes iguales."),
        ex("En 7/10, ¿cuántas partes se toman?", "7", "El numerador dice cuántas partes se toman."),
        ex("¿Se puede escribir una fracción si las partes son de distinto tamaño?", "No", "Las partes deben ser iguales."),
    ],
    op=task(
        "Dobla una hoja en 4 partes iguales y pinta 3. Escribe la fracción pintada. Después dobla otra hoja en 8 partes iguales y pinta 5. Escribe esa fracción. Explica con tus palabras qué dicen el numerador y el denominador.",
        "Primera hoja: 3/4. Segunda hoja: 5/8. El denominador dice en cuántas partes iguales se dobló la hoja y el numerador cuántas partes se pintaron.",
        ["divide en partes iguales", "escribe bien las dos fracciones", "explica numerador y denominador"],
        ["hojas dobladas y pintadas", "fracciones escritas", "frase de explicación"],
        ["dividir en partes desiguales", "invertir numerador y denominador"],
        "Reconoce las partes iguales y pide que cuente las partes totales y las pintadas para ubicar cada número.",
    ),
    reinforce="Dibuja un rectángulo, divídelo en 5 partes iguales y pinta 2. Escribe la fracción.",
    extend="Dibuja una tira dividida en 100 partes iguales (o explícalo con palabras) y escribe qué fracción es una de esas partes.",
)

lesson(
    OA8, 2,
    use="Aprenderé a representar fracciones de un todo y de un conjunto de objetos. Sirve para hablar de una parte de un grupo, como las fichas rojas de una caja.",
    prior=["Sé qué son el numerador y el denominador.", "Sé dividir en partes iguales."],
    explain=[
        "Una fracción puede ser parte de un todo, como una pizza, o parte de un conjunto, como un grupo de fichas. En ▮▮▮□ hay 4 partes iguales y 3 están pintadas: 3/4 del todo. En un conjunto, el entero es el grupo completo.",
        "Para hallar una fracción de un conjunto, divide el grupo en partes iguales según el denominador y toma las que dice el numerador. Para 2/5 de 10 fichas, divide 10 en 5 grupos iguales: cada grupo tiene 2. Toma 2 grupos: 2 × 2 = 4 fichas. Entonces 2/5 de 10 es 4.",
        "También puedes escribir qué fracción del conjunto cumple una condición. Si hay 8 fichas y 3 son rojas, 3/8 son rojas y 5/8 no lo son. Siempre el denominador es el total de elementos del conjunto, y el numerador los que cumplen la condición.",
    ],
    vocab=[("todo", "un objeto entero, como una tira o un rectángulo"), ("conjunto", "grupo de elementos, como fichas o lápices"), ("fracción de un conjunto", "parte de un grupo, dividido en partes iguales"), ("grupo igual", "cada una de las partes iguales en que se divide un conjunto"), ("condición", "característica que cumplen algunos elementos, como ser rojo")],
    worked=[
        W("Fracción de un conjunto", "Hay 10 fichas. ¿Cuántas fichas son 2/5 del conjunto?", ["Divido 10 en 5 grupos iguales: 10 ÷ 5 = 2 fichas en cada grupo.", "Tomo 2 grupos: 2 × 2 = 4.", "Compruebo: 4 de 10 fichas es lo mismo que 2 grupos de 5."], "4 fichas"),
        W("Qué fracción cumple una condición", "En una caja hay 8 fichas, 3 rojas y 5 azules. ¿Qué fracción son rojas?", ["El conjunto tiene 8 fichas: denominador 8.", "Las rojas son 3: numerador 3.", "Las rojas son 3/8 y las azules 5/8."], "3/8"),
    ],
    mistakes=[
        M("Decir que 1/2 de 10 fichas es 2.", "Se divide por 5 en vez de por 2.", "El denominador es 2: se divide 10 en 2 grupos iguales y cada grupo tiene 5."),
        M("Escribir 5/3 para 3 fichas rojas de 8.", "No se usa el total del conjunto como denominador.", "El denominador es el total de fichas (8) y el numerador las rojas (3): 3/8."),
    ],
    rec=[
        ex("¿Qué fracción está pintada? ▮▮▮□□□□□", "3/8", "Hay 3 pintadas de 8 partes iguales."),
        ex("En un grupo de 8 fichas, 3 son rojas. ¿Qué fracción son rojas?", "3/8", "3 de las 8 fichas."),
        arith("¿Cuántas fichas son 1/4 de 12 fichas?", "12//4", "12 ÷ 4 = 3."),
    ],
    und=[
        ex("Para hallar 2/5 de 10 fichas, ¿en cuántos grupos iguales divides 10?", "5", "El denominador 5 dice en cuántos grupos iguales."),
        ex("En 2/5 de 10, ¿cuántas fichas tiene cada grupo?", "2", "10 ÷ 5 = 2."),
        ex("Si 3/8 de las fichas son rojas, ¿qué fracción no son rojas?", "5/8", "8 partes totales menos 3 rojas = 5."),
    ],
    app=[
        arith("Calcula 3/4 de 12: divide 12 entre 4 y multiplica por 3.", "12//4*3", "12 ÷ 4 = 3 y 3 × 3 = 9."),
        arith("Calcula 2/3 de 9: divide 9 entre 3 y multiplica por 2.", "9//3*2", "9 ÷ 3 = 3 y 3 × 2 = 6."),
        arith("Calcula 5/8 de 16: divide 16 entre 8 y multiplica por 5.", "16//8*5", "16 ÷ 8 = 2 y 2 × 5 = 10."),
    ],
    rea=[
        ex("Eva dice que 1/2 de 10 es 2 porque 10 ÷ 5 = 2. ¿Tiene razón?", "No, es 5", "1/2 pide dividir 10 entre 2: 10 ÷ 2 = 5."),
        ex("Pablo pintó 4 de 10 fichas de un cartón. ¿Qué fracción no está pintada?", "6/10", "10 − 4 = 6 fichas sin pintar."),
    ],
    cha=[
        ex("En un curso de 30 estudiantes, 1/5 va en la sala A y 2/5 en la sala B. ¿Cuántos estudiantes quedan en otras salas?", "12", "1/5 de 30 = 6 y 2/5 de 30 = 12; 30 − 6 − 12 = 12."),
        ex("Si 3/4 de un grupo son 15 fichas, ¿cuántas fichas tiene todo el grupo?", "20", "Cada 1/4 son 5 fichas, y 4 × 5 = 20."),
    ],
    ctx=[ex("En una bolsa hay 12 pelotas y 1/3 son azules. ¿Cuántas pelotas azules hay?", "4", "12 ÷ 3 = 4.")],
    sc=[
        ex("¿Qué fracción está pintada? ▮▮□□□□", "2/6", "2 pintadas de 6 partes iguales."),
        arith("Calcula 1/5 de 20.", "20//5", "20 ÷ 5 = 4."),
        ex("En una caja de 10 lápices, 7 son azules. ¿Qué fracción son azules?", "7/10", "7 de 10 lápices."),
    ],
    op=task(
        "Con 12 tapas (o 12 círculos dibujados), muestra 1/3, 1/4 y 1/2 del conjunto. Para cada fracción, escribe en cuántos grupos iguales dividiste y cuántas tapas hay en cada parte. Luego muestra 3/4 de las 12 tapas y escribe cuántas son.",
        "1/3 de 12: 3 grupos de 4 tapas, entonces 4. 1/4 de 12: 4 grupos de 3 tapas, entonces 3. 1/2 de 12: 2 grupos de 6 tapas, entonces 6. 3/4 de 12: 3 grupos de 3 = 9 tapas.",
        ["divide en grupos iguales", "usa el denominador como cantidad de grupos", "calcula cuántas tapas son"],
        ["tapas o dibujo", "resultados escritos"],
        ["dividir por el numerador", "formar grupos desiguales"],
        "Reconoce los grupos formados y pide que explique por qué el denominador dice cuántos grupos hay.",
    ),
    reinforce="Dibuja 8 círculos, pinta 2 y escribe la fracción pintada y la no pintada.",
    extend="Explica con un ejemplo la diferencia entre 1/2 de una pizza y 1/2 de un grupo de 10 fichas.",
)

lesson(
    OA8, 3,
    use="Aprenderé a ubicar fracciones en la recta numérica entre 0 y 1. Sirve para ver dónde está cada fracción y compararlas.",
    prior=["Sé qué es una fracción y sus partes.", "Sé ubicar números en una recta numérica."],
    explain=[
        "Una fracción también es un número y tiene su lugar en la recta numérica. Entre 0 y 1 se hace un segmento y se divide en partes iguales según el denominador. Para cuartos se hacen 4 partes iguales. Las marcas son 0/4, 1/4, 2/4, 3/4 y 4/4.",
        "Para ubicar 3/4, cuenta 3 partes desde el 0. Para ubicar 5/8, divide el segmento en 8 partes iguales y cuenta 5. La marca final, 4/4 o 8/8, es el 1. La marca inicial, 0/4, es el 0. En la recta de 0 a 1, la marca que está a la mitad del camino es 1/2.",
        "La recta muestra qué fracción es mayor: la que queda más a la derecha. En una recta de cuartos, 3/4 queda a la derecha de 1/4. Dibuja la recta con partes del mismo tamaño y escribe las fracciones bajo cada marca para no equivocarte.",
    ],
    vocab=[("recta numérica", "línea donde se ubican los números en orden"), ("segmento", "parte de una recta entre dos puntos"), ("marca", "raya que indica un número en la recta"), ("partes iguales", "partes del mismo tamaño"), ("mitad", "una de dos partes iguales; 1/2")],
    worked=[
        W("Ubicar 3/4", "Ubica 3/4 en la recta de 0 a 1.", ["Divido el segmento de 0 a 1 en 4 partes iguales.", "Marco 0/4, 1/4, 2/4, 3/4 y 4/4.", "Cuento 3 partes desde el 0: ahí va 3/4."], "En la tercera marca contando desde 0"),
        W("Leer una fracción en la recta", "La recta de 0 a 1 está dividida en 8 partes iguales. ¿Qué fracción está en la quinta marca?", ["El denominador es 8, porque hay 8 partes.", "La quinta marca tiene 5 partes recorridas desde 0.", "Es 5/8."], "5/8"),
    ],
    mistakes=[
        M("Ubicar 3/4 en la tercera marca de una recta dividida en 3 partes.", "El denominador dice cuántas partes iguales hay entre 0 y 1.", "Para cuartos se divide en 4 partes iguales y 3/4 queda en la tercera marca de esas 4."),
        M("Dividir el segmento en partes desiguales.", "Las marcas no están a la misma distancia.", "Mide o dobla para que todas las partes sean iguales."),
    ],
    rec=[
        ex("La recta de 0 a 1 se divide en 4 partes iguales. ¿Cuántas marcas hay desde 0/4 hasta 4/4?", "5", "Las marcas son 0/4, 1/4, 2/4, 3/4 y 4/4."),
        ex("La recta de 0 a 1 está dividida en 8 partes iguales. ¿Qué fracción está en la quinta marca?", "5/8", "Se cuentan 5 partes desde el 0."),
        ex("¿Qué fracción está justo en el medio de la recta de 0 a 1?", "1/2", "La mitad es 1/2."),
    ],
    und=[
        ex("En una recta de 0 a 1 dividida en 5 partes iguales, ¿qué fracción está en la marca 3?", "3/5", "3 partes de 5 recorridas."),
        ex("¿Dónde queda 4/4 en la recta de 0 a 1?", "En el 1", "4 partes de 4 es el entero."),
        ex("En una recta dividida en 6 partes iguales, ¿en qué marca queda 3/6?", "En la marca 3, justo en el medio", "3 de 6 partes es la mitad."),
    ],
    app=[
        ex("Ubica 3/4 en la recta de 0 a 1 dividida en cuartos. ¿En qué marca contando desde 0 está?", "En la tercera", "Se cuentan 3 partes desde el 0."),
        ex("En una recta de 0 a 1 dividida en 10 partes iguales, ¿qué fracción está en la marca 7?", "7/10", "7 partes de 10 recorridas."),
        ex("En una recta de 0 a 1 dividida en 12 partes iguales, ¿qué fracción está a una marca antes del 1?", "11/12", "Una parte antes de las 12 partes: 11/12."),
    ],
    rea=[
        ex("Ana ubicó 3/4 en la tercera marca de una recta dividida en 3 partes. ¿Está bien?", "No", "Para cuartos hay que dividir en 4 partes iguales."),
        ex("En una recta de cuartos, ¿qué queda más a la derecha: 1/4 o 3/4?", "3/4", "A la derecha están los números mayores."),
    ],
    cha=[
        ex("Entre 0 y 1 hay 10 partes iguales. ¿Qué fracción con denominador 10 queda justo en el medio?", "5/10", "La mitad de 10 partes son 5 partes."),
        ex("En una recta dividida en octavos, ¿cuántos octavos hay entre 2/8 y 6/8, sin contar los extremos?", "3", "Entre 2/8 y 6/8 están 3/8, 4/8 y 5/8."),
    ],
    ctx=[ex("Un sendero de 1 km tiene 5 letreros que lo dividen en 5 partes iguales. Si llegaste al tercer letrero contando desde el inicio, ¿qué fracción del km recorriste?", "3/5", "3 de 5 partes iguales.")],
    sc=[
        ex("En una recta dividida en 3 partes iguales, ¿qué fracción hay en la marca 2?", "2/3", "2 de 3 partes."),
        ex("¿Qué fracción hay en la última marca de una recta de 0 a 1 dividida en 6 partes iguales?", "6/6", "Es el entero, o 1."),
        ex("¿Es 1/8 mayor que 5/8 en la recta?", "No", "1/8 queda más a la izquierda."),
    ],
    op=task(
        "Dibuja una recta de 0 a 1 de 16 cuadritos de largo (o 16 cm). Marca en ella los cuartos y escribe 1/4, 2/4, 3/4 y 4/4. Marca en otra recta igual los octavos y escribe 1/8, 2/8, … hasta 8/8. Escribe qué notas sobre las marcas que coinciden.",
        "En la recta de 16 cuadritos, cuartos en las marcas 4, 8, 12 y 16; octavos en 2, 4, 6, 8, 10, 12, 14 y 16. Coinciden 2/8 con 1/4, 4/8 con 2/4, 6/8 con 3/4 y 8/8 con 4/4: son el mismo punto.",
        ["divide en partes iguales", "escribe las fracciones bajo cada marca", "observa que algunas marcas coinciden"],
        ["dos rectas dibujadas", "fracciones escritas", "frase de observación"],
        ["marcas a distinta distancia", "numerar desde 1 en lugar de desde 0"],
        "Pide que superponga las dos rectas y vea qué marcas coinciden para introducir las fracciones equivalentes.",
    ),
    reinforce="Dibuja una recta de 0 a 1 dividida en 5 partes iguales y escribe las fracciones de cada marca.",
    extend="Ubica 1/2, 1/4 y 3/4 en una misma recta y explica cómo supiste dónde poner cada una.",
)

lesson(
    OA8, 4,
    use="Aprenderé que una misma cantidad se puede escribir con fracciones distintas, como 1/2, 2/4 y 4/8. Sirve para comparar y reconocer cuándo dos fracciones valen lo mismo.",
    prior=["Sé ubicar fracciones en la recta.", "Sé dividir tiras y rectángulos en partes iguales."],
    explain=[
        "Dos fracciones son equivalentes cuando representan la misma cantidad del mismo entero. Si doblas una tira por la mitad, 1/2 de la tira ocupa el mismo largo que 2/4 y que 4/8. Se escribe 1/2 = 2/4 = 4/8.",
        "Lo ves dibujando. Toma dos tiras iguales. Pinta 1/2 de la primera. Divide la segunda en 4 partes iguales y pinta 2: queda pintado el mismo largo. Si cortas cada cuarto en 2 partes iguales, la tira tiene 8 partes y la parte pintada es 4/8. Cada parte se parte en 2, y se duplican las partes tomadas y las partes totales. Si cada parte se partiera en 3 o en 4, se triplicarían o cuadruplicarían.",
        "Para reconocer equivalentes puedes mirar la recta: están en el mismo punto. Otros ejemplos: 1/5 = 2/10 y 1/3 = 2/6 = 4/12. Una fracción también puede ser parte de un conjunto: 1/2 de 8 fichas son 4 fichas, igual que 2/4 de 8 fichas.",
    ],
    vocab=[("fracciones equivalentes", "fracciones distintas que representan la misma cantidad"), ("representación", "forma de mostrar una cantidad, con dibujo, recta o número"), ("mitad", "1/2 del entero"), ("igual cantidad", "mismo tamaño o mismo valor"), ("subdividir", "dividir cada parte en partes más pequeñas iguales")],
    worked=[
        W("Mitad y cuartos", "¿Es 1/2 equivalente a 2/4?", ["Dibujo dos tiras iguales. Pinto la mitad de la primera.", "Divido la segunda en 4 partes iguales y pinto 2.", "Las dos partes pintadas tienen el mismo largo."], "Sí, 1/2 = 2/4"),
        W("Subdividir", "1/5 de una tira se corta cada quinto en 2 partes iguales. ¿Qué fracción es ahora?", ["Cada quinto se parte en 2: la tira queda con 10 partes iguales.", "La parte pintada ocupa 2 de esas partes.", "1/5 = 2/10."], "2/10"),
    ],
    mistakes=[
        M("Decir que 1/2 y 2/4 son distintos porque los números son distintos.", "Se mira solo el número y no la cantidad.", "Dibuja el mismo entero: ocupan el mismo largo."),
        M("Creer que 2/4 es más que 1/2 porque 2 y 4 son más grandes.", "Se compara el tamaño de los números en vez de la cantidad del entero.", "Con el mismo entero, 2/4 y 1/2 cubren lo mismo."),
    ],
    rec=[
        ex("Dos tiras iguales: una tiene 2 de 4 partes pintadas (2/4) y otra 1 de 2 partes pintadas (1/2). ¿Cuál tiene más pintado?", "Ninguna, es lo mismo", "2/4 = 1/2: las dos cubren la mitad de la tira."),
        ex("Si cada cuarto de una tira se corta en 2 partes iguales, ¿cuántas partes tiene la tira?", "8", "4 cuartos × 2 partes cada uno = 8 partes."),
        ex("¿Cuántos octavos hacen 1/2?", "4", "1/2 = 4/8."),
    ],
    und=[
        ex("¿Es 1/5 equivalente a 2/10?", "Sí", "Al partir cada quinto en 2 partes, quedan 10 partes, y la parte pintada son 2."),
        ex("¿Es 1/3 equivalente a 2/6?", "Sí", "Cada tercio partido en 2 da 6 partes, y la parte pintada son 2."),
        ex("¿Es 1/4 equivalente a 1/2?", "No", "1/4 es la mitad de 1/2."),
    ],
    app=[
        ex("Completa para que sean equivalentes: 1/2 = __/4.", "2", "1/2 = 2/4."),
        ex("Completa: 1/4 = __/8.", "2", "Cada cuarto partido en 2 da 2 octavos."),
        ex("Completa: 1/3 = __/12.", "4", "Si cada tercio se parte en 4 partes iguales, el entero queda en 12 partes y la parte pintada son 4."),
    ],
    rea=[
        ex("Camila dice que 3/6 es la mitad de la tira. ¿Tiene razón?", "Sí", "3 de 6 partes iguales es la mitad."),
        ex("Nico dice que 2/3 es equivalente a 4/6. Dibuja o razona: ¿tiene razón?", "Sí", "Cada tercio partido en 2 da sextos; 2 tercios son 4 sextos."),
    ],
    cha=[
        ex("¿Cuál fracción es equivalente a 1/3: 2/6 o 3/6?", "2/6", "Cada tercio se parte en 2: 1/3 = 2/6. Y 3/6 es 1/2."),
        ex("En un grupo de 8 fichas, ¿cuántas fichas son 1/2 y cuántas son 2/4?", "4 y 4", "1/2 de 8 = 4 y 2/4 de 8 = 2 × 2 = 4."),
    ],
    ctx=[ex("Dos amigas comparten una barra de chocolate igual. Una come 2/4 y la otra 1/2. ¿Quién comió más?", "Comieron lo mismo", "2/4 = 1/2 de la misma barra.")],
    sc=[
        ex("Completa: 1/2 = __/8.", "4", "La mitad de 8 partes es 4."),
        ex("¿2/4 y 1/2 son equivalentes?", "Sí", "Representan la misma cantidad."),
        ex("Completa: 1/3 = __/6.", "2", "Cada tercio partido en 2 da 2 sextos."),
    ],
    op=task(
        "Con dos tiras de papel iguales, pinta 1/2 de la primera y muéstrala también como 2/4 y 4/8 doblando la misma tira en 4 y en 8 partes. Pinta lo mismo en los dibujos. Escribe cuántas fracciones equivalentes a 1/2 encontraste y explica con una frase por qué son equivalentes.",
        "1/2 = 2/4 = 4/8. Son equivalentes porque la parte pintada cubre el mismo largo aunque la tira esté partida en más pedazos.",
        ["dobla bien", "pinta lo mismo", "escribe las fracciones equivalentes", "explica con el mismo entero"],
        ["tiras dobladas o dibujadas", "fracciones escritas", "frase de explicación"],
        ["partir en partes desiguales", "creer que más partes significa más cantidad"],
        "Pide que ponga las tiras una sobre otra para comprobar que la parte pintada llega al mismo punto.",
    ),
    reinforce="Dibuja un rectángulo, pinta 1/3 y luego divídelo en 6 partes iguales para mostrar la misma parte como 2/6.",
    extend="Busca tres fracciones equivalentes a 1/2 con denominador 6, 10 y 12 y explica cómo las obtuviste.",
)

lesson(
    OA8, 5,
    use="Aprenderé a comparar y ordenar fracciones usando dibujos, tiras y la mitad como referente. Sirve para saber qué parte es mayor, como 1/8 o 1/5 de un mismo entero.",
    prior=["Sé que las fracciones equivalentes valen lo mismo.", "Sé ubicar fracciones en la recta."],
    explain=[
        "Para comparar fracciones, usa siempre el mismo entero. Si el numerador es 1, entre más partes tenga el entero, más pequeñas son esas partes. Por eso 1/8 es menor que 1/5, y 1/5 es menor que 1/4, y 1/4 es menor que 1/2. Con 100 partes, 1/100 es una parte muy pequeña.",
        "Si el denominador es el mismo, compara los numeradores: 3/8 es menor que 5/8, porque 5 partes son más que 3 del mismo tamaño. Si los dos números son distintos, usa 1/2 como referente. 3/8 es menor que 1/2, porque 4/8 es 1/2. Y 3/5 es mayor que 1/2, porque medio entero en quintos serían 2 partes y media.",
        "Para ordenar varias fracciones, compara de a dos o ubícalas en tiras del mismo largo. De menor a mayor: 1/100, 1/8, 1/5, 1/4, 1/2. Recuerda: con numerador 1, mayor denominador significa fracción menor.",
    ],
    vocab=[("comparar", "decidir cuál es mayor, menor o igual"), ("ordenar", "poner en fila de menor a mayor o de mayor a menor"), ("referente", "fracción conocida que sirve para comparar, como 1/2"), ("mismo entero", "tiras o figuras del mismo tamaño"), ("mayor que (>)", "signo que se abre hacia el número más grande")],
    worked=[
        W("Ordenar fracciones con numerador 1", "Ordena de menor a mayor: 1/2, 1/8, 1/4, 1/5, 1/100.", ["Todas tienen numerador 1: entre más partes, menor es cada parte.", "El mayor denominador es 100: 1/100 es la menor.", "Siguen 1/8, 1/5, 1/4 y 1/2."], "1/100, 1/8, 1/5, 1/4, 1/2"),
        W("Comparar con la mitad", "Compara 3/8 con 1/2.", ["1/2 de un entero partido en 8 partes son 4 partes: 1/2 = 4/8.", "Compara 3/8 con 4/8: 3 es menor que 4.", "Entonces 3/8 es menor que 1/2."], "3/8 < 1/2"),
    ],
    mistakes=[
        M("Decir que 1/8 es mayor que 1/4 porque 8 es mayor que 4.", "Se compara el denominador como si fuera el tamaño de la fracción.", "Con el mismo entero, 8 partes son más pequeñas que 4 partes: 1/8 < 1/4."),
        M("Decir que 3/8 es mayor que 1/2 porque tiene números más grandes.", "Se comparan los números y no las cantidades.", "1/2 es 4/8. Como 3 < 4, 3/8 < 1/2."),
    ],
    rec=[
        ex("¿Cuál es mayor: 1/4 o 1/2?", "1/2", "Con el mismo entero, 2 partes son más grandes que 4 partes."),
        ex("¿Cuál es mayor: 3/8 o 5/8?", "5/8", "Mismo denominador: 5 partes son más que 3."),
        ex("¿Cuál es menor: 1/5 o 1/8?", "1/8", "Entre más partes, más pequeñas son."),
    ],
    und=[
        ex("¿Por qué 1/100 es menor que 1/8?", "Porque 100 partes son más pequeñas que 8 partes", "Con el mismo entero, más partes significa partes más pequeñas."),
        ex("¿Cuántos octavos hacen 1/2?", "4", "1/2 = 4/8."),
        ex("Con 3/5 y 1/2, ¿cuál es mayor?", "3/5", "3/5 es más que 2 quintos y medio, que es la mitad."),
    ],
    app=[
        ex("Ordena de menor a mayor: 1/3, 1/10, 1/6, 1/2, 1/12.", "1/12, 1/10, 1/6, 1/3, 1/2", "Con numerador 1, a mayor denominador, menor fracción."),
        ex("Escribe > o < : 3/8 __ 1/2.", "<", "1/2 = 4/8 y 3 < 4."),
        ex("Escribe >, < o = : 5/10 __ 1/2.", "=", "5/10 = 1/2, porque 5 es la mitad de 10."),
    ],
    rea=[
        ex("Lola dice que 1/8 es mayor que 1/5 porque 8 > 5. ¿Tiene razón?", "No", "8 partes son más pequeñas que 5 partes: 1/8 < 1/5."),
        ex("Pía dice que 5/8 es mayor que 1/2. Compara con 4/8: ¿tiene razón?", "Sí", "1/2 = 4/8 y 5 > 4."),
    ],
    cha=[
        ex("Ordena de mayor a menor: 3/4, 1/2, 1/4.", "3/4, 1/2, 1/4", "Mismo entero: 3/4 > 2/4 = 1/2 > 1/4."),
        ex("¿Cuál es mayor: 2/5 o 1/2? Usa que la mitad de 5 es 2 y medio.", "1/2", "2/5 tiene 2 partes, y la mitad serían 2 partes y media."),
    ],
    ctx=[ex("Luis comió 1/4 de una pizza y Ana comió 1/8 de la misma pizza. ¿Quién comió más?", "Luis", "1/4 es mayor que 1/8 porque cada cuarto es más grande que un octavo.")],
    sc=[
        ex("¿Cuál es mayor: 1/3 o 1/6?", "1/3", "Menos partes significa partes más grandes."),
        ex("Escribe > o < : 2/8 __ 6/8.", "<", "Mismo denominador: 2 < 6."),
        ex("¿Es 1/100 mayor o menor que 1/2?", "Menor", "100 partes son muy pequeñas."),
    ],
    op=task(
        "Dibuja cuatro tiras iguales de 40 cm y pinta en ellas 1/2, 1/4, 1/5 y 1/8 del largo. Después explica con una frase cómo sería 1/100 de la tira. Ordena las cinco fracciones de la parte más pequeña a la más grande. Escribe una regla que sirva para comparar fracciones con numerador 1.",
        "1/2 = 20 cm, 1/4 = 10 cm, 1/5 = 8 cm y 1/8 = 5 cm. 1/100 es una parte muy pequeña, de menos de 1 cm. De menor a mayor: 1/100, 1/8, 1/5, 1/4, 1/2. Regla: con numerador 1, a mayor denominador, menor fracción.",
        ["dibuja tiras del mismo largo", "ordena bien", "escribe la regla"],
        ["cinco tiras dibujadas", "orden escrito", "regla escrita"],
        ["usar tiras de distinto largo", "ordenar por el tamaño del denominador al revés"],
        "Pide que compare dos tiras a la vez, superponiéndolas, antes de ordenar las cinco.",
    ),
    reinforce="Compara con dibujos 1/3 y 1/6 de dos tiras iguales y escribe cuál es mayor.",
    extend="Compara 3/8 y 3/4 usando 1/2 como referente y explica tu razonamiento.",
)
