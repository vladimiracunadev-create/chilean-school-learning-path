"""Cuaderno del estudiante de 5.º básico Matemática: OA 06 (problemas con las cuatro operaciones y dinero) y OA 07 (fracciones propias y equivalencia)."""
from __future__ import annotations

from student_content_ma05_a import M, W, f, lesson, task
from student_lessons import arith, ex

OA6 = "MA05 OA 06"
OA7 = "MA05 OA 07"

# ------------------------------------------------------------------ OA 06 clase 1
lesson(
    OA6, 1,
    use="Aprenderé a leer un problema con dinero, ordenar los datos y elegir la operación que lo resuelve. Sirve para calcular gastos, vueltos y repartos con cantidades de más de cinco cifras.",
    prior=["Sé sumar, restar, multiplicar y dividir números grandes.", "Conozco los billetes de $1.000, $2.000, $5.000, $10.000 y $20.000 y las monedas de $10, $50, $100 y $500."],
    explain=[
        "Para resolver un problema con dinero, primero subraya los datos y la pregunta. Luego pregúntate qué se busca: un total, una diferencia, un reparto o un número de veces. Cada una se relaciona con una operación: sumar para juntar, restar para quitar o comparar, multiplicar para grupos iguales y dividir para repartir en partes iguales.",
        "Un total de compras se calcula sumando o multiplicando. El vuelto es lo que sobra de lo que pagaste, así que se calcula restando: dinero entregado menos total de la compra. Un reparto en partes iguales usa la división. Si un precio se repite varias veces, usa la multiplicación en vez de sumar muchas veces.",
        "Antes de calcular, estima el resultado para saber en qué orden de magnitud debe estar. Después calcula con cuidado, con lápiz o con calculadora. Al final, escribe la respuesta con una frase y con el signo $, y revisa que tenga sentido: un vuelto no puede ser mayor que el dinero entregado.",
    ],
    vocab=[("total", "resultado de juntar varias cantidades"), ("vuelto", "dinero que te devuelven cuando pagas con más de lo que cuesta"), ("diferencia", "lo que hay de más entre dos cantidades"), ("reparto", "dividir una cantidad en partes iguales"), ("estimar", "calcular un valor cercano antes de la cuenta exacta")],
    worked=[
        W("Elegir la operación", "Una tienda vendió $14.500 el lunes y $18.200 el martes. ¿Cuánto vendió en total?", ["Se busca un total: juntar las dos ventas.", "Operación: suma.", "14.500 + 18.200 = 32.700."], "$32.700"),
        W("Calcular un vuelto", "Una compra cuesta $13.800 y se paga con un billete de $20.000. ¿Cuánto es el vuelto?", ["El vuelto es lo que sobra al pagar.", "Operación: resta, 20.000 − 13.800.", "20.000 − 13.800 = 6.200."], "$6.200"),
    ],
    mistakes=[
        M("Sumar $20.000 y $13.800 para calcular el vuelto.", "El vuelto es lo que sobra, así que se resta.", "20.000 − 13.800 = 6.200."),
        M("Sumar 6 veces $3.500 y olvidar una vez.", "Al sumar muchas veces es fácil perder la cuenta.", "Usa multiplicación: 6 × 3.500 = 21.000."),
    ],
    rec=[
        ex("Una tienda vendió $14.500 el lunes y $18.200 el martes. ¿Qué operación da lo vendido en los dos días?", "Suma", "Se juntan las dos ventas."),
        ex("Pagas con $20.000 una compra de $13.800. ¿Qué operación da el vuelto?", "Resta", "El vuelto es lo que sobra del dinero entregado."),
        ex("Cada caja cuesta $12.500 y compras 4. ¿Qué operación da el total?", "Multiplicación", "Son 4 grupos iguales de $12.500."),
    ],
    und=[
        arith("Una tienda vendió $14.500 el lunes y $18.200 el martes. ¿Cuánto vendió entre los dos días?", "14500+18200", "Se suman las dos ventas.", unit=" pesos"),
        arith("Pagas con $20.000 una compra de $13.800. ¿Cuánto vuelto recibes?", "20000-13800", "Dinero entregado menos total.", unit=" pesos"),
        arith("Cada caja cuesta $12.500 y compras 4. ¿Cuánto pagas?", "12500*4", "Cuatro grupos de $12.500.", unit=" pesos"),
    ],
    app=[
        arith("Una escuela recaudó $186.400 en una rifa y gastó $59.700 en premios. ¿Cuánto dinero le queda?", "186400-59700", "Se resta lo gastado a lo recaudado.", unit=" pesos"),
        arith("Un monto de $96.000 se reparte en partes iguales entre 8 cursos. ¿Cuánto recibe cada curso?", "96000//8", "Reparto en partes iguales: división.", unit=" pesos"),
        arith("Tres personas aportan $24.500, $18.750 y $9.800 para un regalo. ¿Cuánto juntaron?", "24500+18750+9800", "Se suman los tres aportes.", unit=" pesos"),
    ],
    rea=[
        ex("Dani dice que para saber cuánto pagará por 6 bolsas de $3.500 debe sumar 3.500 y 6. ¿Qué debe hacer?", "Multiplicar 6 × 3.500", "Son 6 grupos iguales de $3.500."),
        ex("Tienes $50.000 y quieres comprar un artículo de $32.000 y otro de $25.000. ¿Te alcanza?", "No", "Los dos cuestan $57.000, que es más que $50.000."),
    ],
    cha=[
        arith("Un comerciante ficticio compra 15 cajas a $8.400 cada una y las vende todas por $150.000. ¿Cuánto gana?", "150000-15*8400", "Costó 126.000 y vendió por 150.000.", unit=" pesos"),
        arith("Un grupo reúne $240.000 y quiere repartirlos de modo que 5 personas reciban partes iguales, pero antes se descuentan $15.000 para gastos. ¿Cuánto recibe cada una?", "(240000-15000)//5", "Primero se descuentan los gastos y luego se reparte.", unit=" pesos"),
    ],
    ctx=[arith("Una feria ficticia recibió $35.800 por entradas y $12.450 por comida. Los gastos fueron $18.900. ¿Cuánto quedó de ganancia?", "35800+12450-18900", "Se suman los ingresos y se restan los gastos.", unit=" pesos")],
    sc=[
        arith("Compras 4 libros a $9.500 cada uno. ¿Cuánto pagas?", "4*9500", "Cuatro grupos iguales."),
        arith("Pagas $50.000 por algo que cuesta $37.200. ¿Cuánto es el vuelto?", "50000-37200", "Se resta el total al dinero entregado."),
        ex("Si $72.000 se reparte entre 9 personas, ¿qué operación usas?", "División", "Se reparte en partes iguales."),
    ],
    op=task(
        "Elige una situación: (a) una tienda vende $26.400 el sábado y $31.750 el domingo; (b) compras 7 cuadernos a $2.850 cada uno y pagas con $20.000; (c) $144.000 se reparten entre 6 cursos. Escribe los datos, la operación y la respuesta con una frase y el signo $.",
        "(b) Cuadernos: 7 × 2.850 = 19.950. Vuelto: 20.000 − 19.950 = 50. Pago 19.950 y recibo $50 de vuelto.",
        ["subraya los datos", "elige la operación correcta", "responde con frase y $"],
        ["datos y operación en el cuaderno", "frase de respuesta"],
        ["elegir sumar cuando se debe restar", "olvidar el signo $"],
        "Pide que explique en una frase por qué eligió esa operación y que estime antes de calcular.",
    ),
    reinforce="Anota tres precios de productos de tu casa (aunque sean ficticios, mayores de $1.000) y calcula cuánto cuestan 4 de cada uno.",
    extend="Explica con un ejemplo por qué el vuelto nunca puede ser mayor que el dinero entregado.",
)

# ------------------------------------------------------------------ OA 06 clase 2
lesson(
    OA6, 2,
    use="Aprenderé a usar la calculadora para resolver problemas con números grandes y a comprobar el resultado con una estimación. Sirve para evitar errores al teclear.",
    prior=["Sé elegir la operación de un problema con dinero.", "Sé estimar redondeando."],
    explain=[
        "La calculadora ayuda a hacer cuentas con números grandes, pero no piensa por ti. Tú decides la operación y tecleas los números en orden. Si te equivocas en una tecla, el resultado también estará mal, aunque la calculadora no se equivoque.",
        "Por eso conviene estimar antes. Para 1.250 × 48 puedes pensar 1.000 × 50 = 50.000. Si la calculadora muestra 60.000, está cerca de lo estimado y es razonable. Si muestra 6.000, algo falló: probablemente faltó una tecla o un cero.",
        "La calculadora muestra los números sin puntos, por ejemplo 60000. Al escribir la respuesta ponla con puntos: 60.000. En calculadoras simples, algunas hacen las operaciones en el orden en que las tecleas, sin dar prioridad a la multiplicación; para expresiones combinadas calcula por partes y anota los resultados intermedios.",
    ],
    vocab=[("calculadora", "aparato que hace operaciones con números"), ("estimar", "calcular un valor cercano antes de la cuenta exacta"), ("pantalla", "lugar donde la calculadora muestra el resultado"), ("resultado intermedio", "resultado de una parte del cálculo que anotas para seguir"), ("razonable", "que tiene sentido para el problema")],
    worked=[
        W("Calcular y comprobar", "Una librería compra 36 cajas de lápices a $4.850 cada una. ¿Cuánto paga?", ["Estimo: 40 × 5.000 = 200.000.", "Calculadora: 36 × 4.850 = 174.600.", "El resultado está cerca de la estimación, es razonable."], "$174.600"),
        W("Detectar un error de teclas", "La calculadora muestra 6000 para 12.000 × 40. ¿Es razonable?", ["Estimo: 12.000 × 40 es más que 10.000 × 40 = 400.000.", "6.000 es mucho menor: falta un cero o una tecla.", "El resultado correcto es 480.000."], "No es razonable; es 480.000"),
    ],
    mistakes=[
        M("Aceptar 6.000 como resultado de 12.000 × 40 solo porque lo mostró la calculadora.", "No se comparó con una estimación.", "Estima antes: 10.000 × 40 = 400.000. El resultado correcto es 480.000."),
        M("Escribir la respuesta como 174600 pesos.", "Faltan los puntos que separan los miles.", "Se escribe $174.600."),
    ],
    rec=[
        ex("La pantalla muestra 60000. ¿Cómo se escribe con puntos?", "60.000", "Se separan los miles con un punto."),
        arith("Calcula 1.250 × 48 con calculadora.", "1250*48", "1.000 × 48 = 48.000 y 250 × 48 = 12.000."),
        ex("¿Para qué sirve estimar antes de usar la calculadora?", "Para revisar si el resultado tiene sentido", "Una estimación ayuda a detectar errores de teclas."),
    ],
    und=[
        arith("Suma con calculadora 12.480 + 9.750 + 8.365.", "12480+9750+8365", "Se teclean los tres sumandos en orden."),
        arith("Divide con calculadora 84.000 ÷ 12.", "84000//12", "12 × 7.000 = 84.000."),
        ex("Estima 18.900 + 31.200 redondeando cada sumando a la unidad de mil.", "50.000", "19.000 + 31.000 = 50.000."),
    ],
    app=[
        arith("Una librería compra 36 cajas de lápices a $4.850 cada una. ¿Cuánto paga en total?", "36*4850", "Estimo 40 × 5.000 = 200.000.", unit=" pesos"),
        arith("Una empresa pagó $1.248.000 en 12 cuotas iguales. ¿De cuánto es cada cuota?", "1248000//12", "12 × 104.000 = 1.248.000.", unit=" pesos"),
        arith("Un bus ficticio recorre 485 kilómetros por viaje y hace 126 viajes en el año. ¿Cuántos kilómetros recorre?", "485*126", "Estimo 500 × 100 = 50.000, y 61.110 es del mismo orden.", unit=" km"),
    ],
    rea=[
        ex("Rosa debía sumar 12.480 + 9.750, pero tecleó 9.570 y obtuvo 22.050. ¿Cuál es el resultado correcto?", "22.230", "12.480 + 9.750 = 22.230."),
        ex("La calculadora muestra 480 para 12.000 × 40. ¿Es razonable?", "No, debería ser 480.000", "12 × 4 = 48 y se anexan cuatro ceros (tres de 12.000 y uno de 40): 480.000."),
    ],
    cha=[
        ex("Una calculadora muestra 3.540.000 para 7.080 × 500. Estima para decir si es razonable.", "Sí", "7.000 × 500 = 3.500.000, muy cerca."),
        arith("Se compran 25 mesas a $48.500 cada una y se paga con $1.500.000. ¿Cuánto es el vuelto?", "1500000-25*48500", "Primero 25 × 48.500 = 1.212.500.", unit=" pesos"),
    ],
    ctx=[arith("Un club ficticio vende 1.250 entradas a $2.800 cada una. ¿Cuánto dinero recibe?", "1250*2800", "Estimo 1.000 × 3.000 = 3.000.000.", unit=" pesos")],
    sc=[
        arith("Calcula 4.500 × 36 con calculadora.", "4500*36", "4.500 × 36 = 162.000."),
        ex("Estima 52.000 − 19.800 redondeando 19.800 a 20.000.", "32.000", "52.000 − 20.000."),
        ex("¿Cómo se escribe con puntos 1248000?", "1.248.000", "Se separan los periodos de tres cifras."),
    ],
    op=task(
        "Elige: 28 cajas a $6.950 cada una, 145 entradas a $3.600 cada una o $2.376.000 repartidos en 24 cuotas. Estima primero, calcula con calculadora y escribe la respuesta con puntos y $. Anota si tu resultado es razonable y por qué.",
        "145 entradas a $3.600: estimo 150 × 3.600 ≈ 540.000. Calculadora: 145 × 3.600 = 522.000. Es razonable porque está cerca de la estimación. Respuesta: $522.000.",
        ["estima antes", "usa la calculadora para el cálculo exacto", "compara y responde con puntos y $"],
        ["estimación", "resultado de calculadora", "frase de respuesta"],
        ["teclear mal una cifra", "no comparar con la estimación"],
        "Pide que lea en voz alta el número que tecleó y que compare el resultado con la estimación.",
    ),
    reinforce="Con una calculadora, calcula 25 × 48 de dos maneras: 25 × 48 y 48 × 25. Mira que den lo mismo.",
    extend="Explica por qué una calculadora puede mostrar un resultado equivocado aunque no tenga fallas.",
)

# ------------------------------------------------------------------ OA 06 clase 3
lesson(
    OA6, 3,
    use="Aprenderé a elegir y justificar una estrategia para problemas de dinero con varios pasos, comparando ofertas y precios. Sirve para decidir qué conviene comprar.",
    prior=["Sé elegir una operación y calcular con calculadora.", "Sé estimar y comprobar."],
    explain=[
        "Un problema de varios pasos necesita dos o más operaciones seguidas. Para resolverlo, escribe qué debes encontrar primero y qué después. Por ejemplo: para el vuelto de 25 mesas a $48.500 pagadas con $1.500.000, primero se calcula el total (multiplicación) y luego el vuelto (resta).",
        "Para comparar ofertas, calcula el total de cada una con la misma regla y compara los números. Si una oferta es 4 cajas a $12.500 (total $50.000) y la otra es 5 cajas a $10.800 (total $54.000), la primera cuesta menos en total, pero la segunda trae más cajas, así que fíjate bien en qué pregunta el problema.",
        "A veces conviene comparar el precio por unidad. Si un pack de 6 cuesta $4.800, cada unidad cuesta 4.800 ÷ 6 = $800. Si un pack de 8 cuesta $6.000, cada una cuesta $750. El pack de 8 conviene más por unidad. Justifica tu elección con los números.",
    ],
    vocab=[("varios pasos", "problema que necesita más de una operación"), ("oferta", "propuesta de venta con un precio"), ("precio por unidad", "cuánto cuesta cada uno de los productos de un pack"), ("convenir", "ser la mejor opción por costar menos"), ("justificar", "dar razones con números para una decisión")],
    worked=[
        W("Dos pasos: total y vuelto", "Un colegio compra 25 mesas a $48.500 cada una y paga con $1.500.000. ¿Cuánto vuelto recibe?", ["Total: 25 × 48.500 = 1.212.500.", "Vuelto: 1.500.000 − 1.212.500 = 287.500."], "$287.500"),
        W("Comparar por unidad", "Un pack de 6 cuesta $4.800 y un pack de 8 cuesta $6.000. ¿Cuál conviene más por unidad?", ["Pack de 6: 4.800 ÷ 6 = 800.", "Pack de 8: 6.000 ÷ 8 = 750.", "750 < 800, así que conviene el pack de 8."], "El pack de 8"),
    ],
    mistakes=[
        M("Decir que conviene el pack de 6 porque cuesta menos en total ($4.800 contra $6.000).", "No se compararon los precios por unidad.", "Divide cada precio por la cantidad: $800 contra $750."),
        M("Calcular el vuelto restando 1.500.000 − 48.500.", "Solo se usó el precio de una mesa.", "Primero el total de 25 mesas y luego la resta."),
    ],
    rec=[
        arith("Calcula el total de 25 mesas a $48.500 cada una.", "25*48500", "25 grupos de 48.500."),
        arith("Calcula el precio de una unidad de un pack de 6 que cuesta $4.800.", "4800//6", "Se reparte el precio entre 6 unidades."),
        ex("Para comparar dos packs de distinta cantidad, ¿qué conviene calcular?", "El precio por unidad", "Así se comparan con la misma medida."),
    ],
    und=[
        arith("Un colegio compra 25 mesas a $48.500 cada una y paga con $1.500.000. ¿Cuánto vuelto recibe?", "1500000-25*48500", "Primero el total y luego la resta.", unit=" pesos"),
        arith("Un computador cuesta $360.000 y se paga en 12 cuotas iguales. ¿De cuánto es cada cuota?", "360000//12", "Se reparte el precio entre las cuotas.", unit=" pesos"),
        arith("Un pack de 8 cuesta $6.000. ¿Cuánto cuesta cada unidad?", "6000//8", "Se divide el precio entre 8.", unit=" pesos"),
    ],
    app=[
        ex("La oferta A son 4 cajas a $12.500 cada una y la oferta B son 5 cajas a $10.800 cada una. ¿Cuál cuesta menos en total?", "La A, $50.000 contra $54.000", "4 × 12.500 = 50.000 y 5 × 10.800 = 54.000."),
        ex("Un pack de 6 cuesta $4.800 y uno de 8 cuesta $6.000. ¿Cuál tiene menor precio por unidad?", "El de 8", "800 contra 750 pesos por unidad."),
        arith("Una empresa ficticia paga $420.000 a cada uno de 3 trabajadores. Por un convenio, el total a pagar se rebaja en $85.000. ¿Cuánto paga en total?", "3*420000-85000", "Primero los sueldos y luego el descuento.", unit=" pesos"),
    ],
    rea=[
        ex("Ana dice que el pack de 6 a $4.800 conviene porque cuesta menos que el de 8 a $6.000. ¿Es un buen argumento?", "No", "Hay que comparar el precio por unidad: 800 y 750."),
        ex("¿Qué dos operaciones, en orden, resuelven «cuánto pagas por 12 cuadernos de $2.450 si te descuentan $3.000»?", "Multiplicar y restar", "12 × 2.450 = 29.400 y luego 29.400 − 3.000."),
    ],
    cha=[
        ex("La tienda A vende 3 poleras por $29.400 en total y la tienda B vende 4 poleras por $30.400 en total. ¿Cuál tiene menor precio por polera?", "La B: $7.600 contra $9.800", "29.400 ÷ 3 = 9.800 y 30.400 ÷ 4 = 7.600."),
        arith("Un grupo de 6 amigos reúne $150.000. Compran entradas de $12.000 cada una para todos. ¿Cuánto dinero les sobra?", "150000-6*12000", "Las 6 entradas cuestan 72.000.", unit=" pesos"),
    ],
    ctx=[arith("Un club ficticio paga una cuenta de $186.500 con $200.000. El vuelto se reparte en partes iguales entre 3 personas. ¿Cuánto recibe cada una?", "(200000-186500)//3", "El vuelto es 13.500 y se reparte en 3.", unit=" pesos")],
    sc=[
        arith("Un artículo cuesta $14.500 y compras 12. ¿Cuánto pagas?", "12*14500", "12 grupos de 14.500."),
        arith("Un pack de 10 cuesta $8.500 y otro de 12 cuesta $9.600. Calcula cuánto cuesta cada unidad del pack de 12.", "9600//12", "9.600 repartidos en 12."),
        ex("¿Es 4 × 12.500 mayor o menor que 5 × 10.800?", "Menor", "50.000 < 54.000."),
    ],
    op=task(
        "Elige una situación: (a) comparar un pack de 5 a $4.250 y uno de 8 a $6.480; (b) 24 mesas a $39.800 pagadas con $1.000.000; (c) 12 cuotas de $45.500 contra un pago al contado de $520.000. Explica con números qué conviene.",
        "(a) Pack de 5: 4.250 ÷ 5 = 850. Pack de 8: 6.480 ÷ 8 = 810. Conviene el pack de 8 porque 810 < 850.",
        ["plantea los pasos", "compara con la misma medida", "justifica con números"],
        ["cálculos escritos", "frase de justificación"],
        ["comparar totales de packs distintos", "olvidar un paso"],
        "Pide que escriba cada paso en una línea y que diga por qué eligió esa medida de comparación.",
    ),
    reinforce="Elige dos productos de tu casa y calcula el precio por unidad de cada uno, si conoces el precio del paquete (o inventa precios mayores a $1.000).",
    extend="Explica por qué no siempre conviene el producto más barato en total.",
)

# ------------------------------------------------------------------ OA 06 clase 4
lesson(
    OA6, 4,
    use="Aprenderé a resolver problemas de dinero con una condición nueva, como un presupuesto limitado, un descuento fijo o una cantidad desconocida. Sirve para decidir con un límite de dinero.",
    prior=["Sé resolver problemas de varios pasos con dinero.", "Sé interpretar el resto de una división."],
    explain=[
        "Un presupuesto es el dinero máximo que puedes gastar. Cuando hay un presupuesto, la pregunta es qué puedes comprar o cuántas unidades alcanzan. Se divide el presupuesto por el precio y se interpreta el resto: si sobra dinero pero no alcanza para otro artículo, no se cuenta como otra unidad.",
        "Si hay una cantidad desconocida, usa la operación inversa. Si faltan $345.000 y cada persona aporta $15.000, divides 345.000 ÷ 15.000 = 23 personas. Si ya tienes una parte, primero restas lo que ya tienes y luego divides. El orden de los pasos importa.",
        "Una condición nueva puede ser un descuento fijo, como «se descuentan $3.000». Un descuento fijo se resta del total. Si el descuento es por cada unidad, se resta de cada precio antes de multiplicar. Escribe siempre qué calculas en cada paso para no mezclar los datos.",
    ],
    vocab=[("presupuesto", "dinero máximo que se puede gastar"), ("descuento fijo", "cantidad de dinero que se resta al precio"), ("cantidad desconocida", "dato que el problema pide encontrar"), ("alcanzar", "tener suficiente dinero para comprar algo"), ("operación inversa", "operación que deshace a otra")],
    worked=[
        W("Cuántas unidades alcanzan", "Con $150.000 se compran camisetas de $7.500 cada una. ¿Cuántas se pueden comprar?", ["Se divide el presupuesto por el precio.", "150.000 ÷ 7.500 = 20.", "No sobra dinero."], "20 camisetas"),
        W("Cantidad desconocida", "Faltan $345.000 para una compra y cada persona aporta $15.000. ¿Cuántas personas se necesitan?", ["Se divide lo que falta entre el aporte.", "345.000 ÷ 15.000 = 23."], "23 personas"),
    ],
    mistakes=[
        M("Con $250.000 y entradas de $12.000, decir que se compran 21 entradas porque 250.000 ÷ 12.000 es casi 21.", "El resto no alcanza para una entrada más, y 21 pasaría el presupuesto.", "250.000 ÷ 12.000 = 20 resto 10.000: se compran 20 entradas y sobran $10.000."),
        M("Para saber cuántos aportes faltan, dividir el total de la compra entre el aporte sin restar lo que ya hay.", "Se ignoró el dinero ya reunido.", "Primero resta lo que ya se tiene y luego divide."),
    ],
    rec=[
        arith("Con $150.000 se compran camisetas de $7.500 cada una. ¿Cuántas se pueden comprar?", "150000//7500", "El presupuesto se divide por el precio."),
        arith("Calcula 480.000 − 135.000.", "480000-135000", "Se resta lo que ya hay."),
        ex("Con $250.000 y entradas de $12.000, ¿se pueden comprar 21 entradas?", "No", "21 entradas costarían $252.000 y pasarían el presupuesto."),
    ],
    und=[
        ex("Con $250.000 y entradas de $12.000, ¿cuántas entradas se compran y cuánto sobra?", "20 entradas y sobran $10.000", "250.000 ÷ 12.000 = 20 resto 10.000."),
        arith("Para una compra de $480.000 ya se reunieron $135.000 y cada persona aporta $15.000. ¿Cuántas personas faltan por aportar?", "(480000-135000)//15000", "Faltan 345.000 y se reparten en aportes de 15.000."),
        arith("Un pasaje cuesta $6.200 y con descuento fijo de $700. ¿Cuánto cuestan 8 pasajes con el descuento en cada uno?", "8*(6200-700)", "Cada pasaje queda en 5.500.", unit=" pesos"),
    ],
    app=[
        ex("Con $320.000 se compran sillas de $26.500 cada una. ¿Cuántas sillas se compran y cuánto sobra?", "12 sillas y sobran $2.000", "26.500 × 12 = 318.000 y 320.000 − 318.000 = 2.000."),
        arith("Un curso quiere juntar $540.000. Ya tiene $96.000 y 12 familias aportarán lo mismo para completar. ¿Cuánto aporta cada familia?", "(540000-96000)//12", "Faltan 444.000 y se reparten en 12.", unit=" pesos"),
        arith("Un taxi ficticio cobra una base de $2.500 más $900 por cada kilómetro. ¿Cuánto cuesta un viaje de 12 kilómetros?", "2500+12*900", "Primero los kilómetros y luego la base.", unit=" pesos"),
    ],
    rea=[
        ex("Beto dice que con $100.000 y lápices de $3.000 alcanzan 34 lápices porque 34 × 3.000 = 102.000, que es casi 100.000. ¿Está bien?", "No, alcanzan 33", "34 lápices cuestan 102.000, más que el presupuesto; 33 cuestan 99.000."),
        ex("Un problema dice «faltan $60.000 y cada aporte es de $4.000». Lía divide 60.000 ÷ 4.000. ¿Es la operación correcta?", "Sí", "Faltan 60.000 y se reparte en aportes iguales de 4.000."),
    ],
    cha=[
        ex("Un presupuesto de $200.000 alcanza para 8 artículos iguales y sobran $4.000. ¿Cuánto cuesta cada artículo?", "$24.500", "200.000 − 4.000 = 196.000 y 196.000 ÷ 8 = 24.500."),
        ex("Si con $150.000 puedes comprar exactamente 20 camisetas, ¿cuántas compras con el doble de dinero si el precio no cambia?", "40", "Con el doble de dinero alcanza para el doble."),
    ],
    ctx=[ex("Un grupo ficticio quiere organizar un paseo de $360.000 y ya tiene $120.000. Cada una de las 15 familias aportará lo mismo para el resto. ¿Cuánto aporta cada una?", "$16.000", "Faltan 240.000 y 240.000 ÷ 15 = 16.000.")],
    sc=[
        arith("Con $90.000 se compran carpetas de $4.500. ¿Cuántas alcanzan?", "90000//4500", "El presupuesto se divide por el precio."),
        arith("Un vestido cuesta $38.000 y le descuentan $5.500. ¿Cuánto cuesta ahora?", "38000-5500", "El descuento se resta."),
        ex("Con $50.000 y entradas de $12.000, ¿cuántas entradas alcanzan?", "4", "4 × 12.000 = 48.000 y 5 pasaría el presupuesto."),
    ],
    op=task(
        "Elige: (a) un presupuesto de $180.000 para comprar cuadernos de $2.400 cada uno; (b) un curso necesita $420.000, tiene $96.000 y cada una de 18 familias aportará lo mismo; (c) 15 pasajes de $3.800 cada uno con $400 de descuento en cada pasaje. Escribe los pasos, las operaciones y la respuesta con interpretación del resto o del descuento.",
        "(a) 180.000 ÷ 2.400 = 75. Se compran 75 cuadernos y no sobra dinero (2.400 × 75 = 180.000).",
        ["explica el presupuesto o la condición", "calcula en pasos", "interpreta el resultado"],
        ["pasos escritos", "frase de respuesta"],
        ["no restar el dinero ya reunido", "no interpretar el resto"],
        "Pide que compruebe multiplicando y que diga qué haría con el dinero que sobra.",
    ),
    reinforce="Con un presupuesto de $12.000 y objetos de $2.500, escribe cuántos puedes comprar y cuánto sobra.",
    extend="Inventa un problema en que haya que restar primero lo que ya se tiene y dividir después.",
)

# ------------------------------------------------------------------ OA 07 clase 1
lesson(
    OA7, 1,
    use="Aprenderé a representar fracciones propias con dibujos, material y símbolos. Sirve para hablar de partes de un entero o de un grupo.",
    prior=["Conozco fracciones sencillas como 1/2 y 1/4.", "Sé repartir un entero en partes iguales."],
    explain=[
        "Una fracción propia representa una parte de un entero que se ha dividido en partes iguales. Se escribe con dos números separados por una raya: 3/5. El denominador (5) dice en cuántas partes iguales se dividió el entero. El numerador (3) dice cuántas de esas partes se toman. Una fracción propia siempre es menor que 1 porque el numerador es menor que el denominador.",
        "Se puede representar con un dibujo: una barra dividida en 5 partes iguales con 3 sombreadas, ■■■□□. También con material concreto, como una tira de papel doblada en partes iguales. Y con el símbolo 3/5. Las tres formas, concreta, pictórica y simbólica, representan lo mismo.",
        "Las fracciones también sirven para grupos. 3/4 de 12 fichas significa dividir las 12 en 4 grupos iguales (de 3) y tomar 3 de esos grupos: 9 fichas. Las partes deben ser iguales: si no lo son, no es una fracción. Recuerda: el denominador cuenta todas las partes y el numerador cuenta las que tomas.",
    ],
    vocab=[("fracción propia", "fracción donde el numerador es menor que el denominador"), ("numerador", "número de arriba: cuántas partes se toman"), ("denominador", "número de abajo: en cuántas partes iguales se divide el entero"), ("entero", "la cantidad completa que se divide"), ("partes iguales", "partes del mismo tamaño")],
    worked=[
        W("Leer una fracción de un dibujo", "Una barra tiene 5 partes iguales y 3 están sombreadas: ■■■□□. ¿Qué fracción está sombreada?", ["Total de partes iguales: 5, ese es el denominador.", "Partes sombreadas: 3, ese es el numerador.", "Fracción: 3/5."], "3/5"),
        W("Fracción de un grupo", "Calcula 3/4 de 12 fichas.", ["12 ÷ 4 = 3 fichas en cada parte.", "Tomo 3 partes: 3 × 3 = 9."], "9 fichas"),
    ],
    mistakes=[
        M("Decir que ■■□□□ es 2/3 porque hay 2 sombreadas y 3 vacías.", "El denominador cuenta todas las partes, no solo las vacías.", "Hay 5 partes en total: la fracción es 2/5."),
        M("Decir que una barra con 3 partes de distinto tamaño, 2 sombreadas, es 2/3.", "Las partes de una fracción deben ser iguales.", "Primero hay que dividir en partes iguales."),
    ],
    rec=[
        ex("¿Qué fracción está sombreada en ■■■□□?", "3/5", "3 partes sombreadas de 5 iguales."),
        ex("En la fracción 7/9, ¿cuál es el numerador?", "7", "El numerador es el número de arriba."),
        ex("Una pizza se corta en 8 partes iguales y comes 3. ¿Qué fracción de la pizza comiste?", "3/8", "Tomas 3 de las 8 partes."),
    ],
    und=[
        ex("¿Qué fracción está sombreada en ■□□□□□?", "1/6", "Hay 1 parte sombreada de 6 iguales."),
        ex("Una tira de papel se dobla en 4 partes iguales y se pinta 1. ¿Qué fracción se pintó?", "1/4", "Una parte de cuatro iguales."),
        ex("De 12 fichas, 9 son azules. ¿Qué fracción del grupo es azul?", "9/12", "El grupo tiene 12 fichas y 9 son azules."),
    ],
    app=[
        arith("Calcula 3/4 de 12 fichas: primero 12 ÷ 4 y luego multiplica por 3.", "12//4*3", "Cada cuarto tiene 3 fichas y se toman 3 cuartos."),
        arith("Calcula 2/5 de 20 lápices: primero 20 ÷ 5 y luego multiplica por 2.", "20//5*2", "Cada quinto tiene 4 lápices y se toman 2 quintos."),
        ex("Una barra se divide en 10 partes iguales y se sombrean 7. ¿Qué fracción propia representa?", "7/10", "7 de 10 partes iguales."),
    ],
    rea=[
        ex("Ema dice que ■■□□□ es 2/3. ¿Está bien?", "No, es 2/5", "El denominador es el total de partes iguales: 5."),
        ex("¿Se puede llamar fracción a una barra dividida en 3 partes de distinto tamaño con 1 sombreada?", "No", "Las partes de una fracción deben ser iguales."),
    ],
    cha=[
        ex("¿Cuántas fracciones propias con numerador 5 y denominador menor que 10 existen?", "4", "Los denominadores son 6, 7, 8 y 9."),
        ex("Una caja tiene 24 bombones y 5/8 son de chocolate. ¿Cuántos bombones de chocolate hay?", "15", "24 ÷ 8 = 3 y 3 × 5 = 15."),
    ],
    ctx=[ex("Un curso tiene 20 estudiantes y 3/4 llevan colación saludable. ¿Cuántos estudiantes llevan colación saludable?", "15", "20 ÷ 4 = 5 y 5 × 3 = 15.")],
    sc=[
        ex("En ■■□□□□□□, ¿qué fracción está sombreada?", "2/8", "2 partes sombreadas de 8 iguales."),
        ex("¿Qué fracción es menor que 1: 5/4 o 4/5?", "4/5", "Una fracción propia tiene el numerador menor que el denominador."),
        ex("En 3/7, ¿qué indica el denominador?", "En cuántas partes iguales se dividió el entero", "El denominador cuenta las partes iguales."),
    ],
    op=task(
        "Elige: 3/5, 5/8 o 2/3. Dibuja una barra con las partes iguales y sombrea la fracción, escríbela con palabras y calcula esa fracción de un grupo de 24 fichas si es posible.",
        "5/8: dibujo una barra con 8 partes iguales y sombreo 5. Se lee «cinco octavos». En 24 fichas, 24 ÷ 8 = 3 y 3 × 5 = 15 fichas.",
        ["divide en partes iguales", "sombrea la cantidad correcta", "escribe la fracción con palabras"],
        ["dibujo en el cuaderno", "fracción escrita", "cálculo de la fracción del grupo"],
        ["partes desiguales", "confundir numerador y denominador"],
        "Pide que cuente las partes totales y las sombreadas, y que diga qué número va arriba y cuál abajo.",
    ),
    reinforce="Dobla una hoja en 4 partes iguales, pinta 3 y escribe la fracción. Luego dóblala en 8 y pinta 3.",
    extend="Explica por qué una fracción propia siempre es menor que un entero.",
)

# ------------------------------------------------------------------ OA 07 clase 2
lesson(
    OA7, 2,
    use="Aprenderé a crear fracciones equivalentes amplificando. Sirve para ver que partes distintas pueden ser la misma cantidad, como 1/2 y 2/4.",
    prior=["Sé representar fracciones propias.", "Sé multiplicar y dividir con las tablas."],
    explain=[
        "Dos fracciones son equivalentes si representan la misma cantidad aunque se escriban distinto. Si una barra se divide en 2 partes y se toma 1 (1/2) y otra igual se divide en 4 partes y se toman 2 (2/4), las dos sombrean lo mismo. Entonces 1/2 = 2/4.",
        "Amplificar es multiplicar numerador y denominador por el mismo número distinto de cero. Así 1/2 × 3/3 da 3/6. La fracción se escribe con más partes pero cada parte es más pequeña, y la cantidad no cambia. Por eso 1/2 = 2/4 = 3/6 = 4/8.",
        "Para comprobar que dos fracciones son equivalentes, revisa si por el mismo número pasas de una a otra. De 2/5 a 6/15 multiplicaste por 3 arriba y por 3 abajo, entonces son equivalentes. Si multiplicas o sumas distinto arriba y abajo, la cantidad cambia.",
    ],
    vocab=[("fracciones equivalentes", "fracciones que representan la misma cantidad"), ("amplificar", "multiplicar numerador y denominador por el mismo número"), ("mismo número", "el factor igual arriba y abajo"), ("barra de fracciones", "dibujo para comparar fracciones"), ("cantidad", "cuánto del entero se toma")],
    worked=[
        W("Amplificar una fracción", "Amplifica 2/3 por 4.", ["Multiplico el numerador: 2 × 4 = 8.", "Multiplico el denominador: 3 × 4 = 12.", "La fracción equivalente es 8/12."], "8/12"),
        W("Encontrar el número que falta", "Completa 3/5 = __/20.", ["De 5 a 20 se multiplicó por 4.", "El numerador también se multiplica por 4: 3 × 4 = 12."], "12/20"),
    ],
    mistakes=[
        M("Decir que 2/3 = 4/5 porque se sumó 2 arriba y abajo.", "Sumar el mismo número no mantiene la cantidad.", "Se debe multiplicar: 2/3 = 4/6."),
        M("Amplificar 1/4 por 3 como 3/4.", "Solo se multiplicó el numerador.", "También se multiplica el denominador: 3/12."),
    ],
    rec=[
        ex("Amplifica 1/2 multiplicando numerador y denominador por 3.", "3/6", "1 × 3 = 3 y 2 × 3 = 6."),
        ex("Completa: 1/2 = __/4.", "2", "De 2 a 4 se multiplicó por 2; 1 × 2 = 2."),
        ex("Completa: 2/3 = __/9.", "6", "De 3 a 9 se multiplicó por 3; 2 × 3 = 6."),
    ],
    und=[
        ex("Completa: 3/4 = __/12.", "9", "De 4 a 12 se multiplicó por 3; 3 × 3 = 9."),
        ex("Completa: 5/6 = 10/__.", "12", "De 5 a 10 se multiplicó por 2; 6 × 2 = 12."),
        ex("¿Son equivalentes 2/5 y 6/15?", "Sí", "2 × 3 = 6 y 5 × 3 = 15."),
    ],
    app=[
        ex("Una torta se corta en 2 partes iguales y se toma 1. Otra igual se corta en 8 partes iguales. ¿Cuántas de esas 8 partes equivalen a la mitad?", "4/8", "1/2 = 4/8 porque se multiplicó por 4."),
        ex("Pedro comió 3/4 de una barra de chocolate. ¿Cuántos doceavos son?", "9/12", "3 × 3 = 9 y 4 × 3 = 12."),
        ex("Amplifica 5/8 por 2 y por 3. Escribe las dos fracciones equivalentes.", "10/16 y 15/24", "5 × 2 = 10 y 8 × 2 = 16; 5 × 3 = 15 y 8 × 3 = 24."),
    ],
    rea=[
        ex("Luis amplifica 2/3 sumando 2 arriba y abajo y obtiene 4/5. ¿Es equivalente?", "No", "2/3 = 4/6; sumar el mismo número no mantiene la cantidad."),
        ex("¿Cuántas fracciones equivalentes a 1/3 con denominador menor que 13 hay, sin contar 1/3?", "3", "Son 2/6, 3/9 y 4/12."),
    ],
    cha=[
        ex("Encuentra la fracción equivalente a 3/5 que tiene denominador 20.", "12/20", "5 × 4 = 20 y 3 × 4 = 12."),
        ex("Una fracción equivalente a 2/3 tiene numerador y denominador que suman 25. ¿Cuál es?", "10/15", "2 + 3 = 5; 25 ÷ 5 = 5; entonces 2 × 5 = 10 y 3 × 5 = 15."),
    ],
    ctx=[ex("Ana corrió 2/5 de la ruta de una carrera escolar y Beto corrió 4/10 de la misma ruta. ¿Corrieron lo mismo?", "Sí", "2/5 = 4/10 porque se multiplicó por 2 arriba y abajo.")],
    sc=[
        ex("Amplifica 1/5 por 4.", "4/20", "1 × 4 = 4 y 5 × 4 = 20."),
        ex("Completa: 4/7 = 12/__.", "21", "De 4 a 12 se multiplicó por 3; 7 × 3 = 21."),
        ex("¿Son equivalentes 3/4 y 6/10?", "No", "De 3 a 6 se multiplicó por 2, pero de 4 a 10 no es por 2."),
    ],
    op=task(
        "Elige: 1/3, 2/5 o 3/4. Dibuja dos barras iguales para mostrar la fracción y una fracción equivalente. Escribe tres fracciones equivalentes amplificando y explica por qué la cantidad no cambia.",
        "2/5: amplificando por 2, 3 y 4 resultan 4/10, 6/15 y 8/20. La cantidad no cambia porque cada parte se divide en pedazos más pequeños, pero se toman más pedazos.",
        ["amplifica con el mismo número", "dibuja o describe la equivalencia", "explica por qué no cambia la cantidad"],
        ["tres fracciones equivalentes", "dibujo o explicación"],
        ["sumar en vez de multiplicar", "amplificar solo el numerador"],
        "Pide que compare las dos barras dibujadas y que verifique que arriba y abajo se multiplicó por el mismo número.",
    ),
    reinforce="Con una tira de papel, dobla en 2 partes y pinta 1. Luego dobla en 4 y mira cuántas partes pintadas hay. Escribe 1/2 = 2/4.",
    extend="Explica por qué 1/2 y 50/100 son equivalentes, sin dibujar.",
)

# ------------------------------------------------------------------ OA 07 clase 3
lesson(
    OA7, 3,
    use="Aprenderé a simplificar fracciones, es decir, a escribirlas con números más pequeños sin cambiar su cantidad. Sirve para dar una fracción en su forma más simple.",
    prior=["Sé amplificar fracciones.", "Conozco los factores de números hasta 20."],
    explain=[
        "Simplificar es dividir el numerador y el denominador por el mismo número distinto de 1. Así 6/8 se simplifica dividiendo por 2: 3/4. La cantidad no cambia, solo se escribe con números más pequeños. Es lo contrario de amplificar.",
        "Para simplificar necesitas un número que divida exacto a los dos términos. En 12/16, el 4 los divide a ambos: 12 ÷ 4 = 3 y 16 ÷ 4 = 4, así 12/16 = 3/4. Se puede hacer en varios pasos: 12/16 = 6/8 = 3/4. Con la práctica se busca el mayor número que divida a ambos.",
        "Una fracción es irreducible cuando ya no se puede simplificar, porque numerador y denominador no tienen otro divisor común que el 1. Por ejemplo, 3/4 y 7/9 son irreducibles. Si dividieras arriba y abajo por números distintos, cambiarías la cantidad. Siempre divide por el mismo número.",
    ],
    vocab=[("simplificar", "dividir numerador y denominador por el mismo número"), ("irreducible", "fracción que ya no se puede simplificar"), ("divisor común", "número que divide exacto a otros dos"), ("término", "numerador o denominador"), ("forma más simple", "fracción equivalente con los números más pequeños posibles")],
    worked=[
        W("Simplificar una fracción", "Simplifica 12/16.", ["Busco un número que divida a 12 y a 16: el 4.", "12 ÷ 4 = 3 y 16 ÷ 4 = 4.", "3/4 es irreducible."], "3/4"),
        W("Simplificar en dos pasos", "Simplifica 18/24 hasta su forma más simple.", ["18 y 24 se dividen por 2: 9/12.", "9 y 12 se dividen por 3: 3/4.", "También se podría dividir directo por 6."], "3/4"),
    ],
    mistakes=[
        M("Simplificar 8/12 como 2/6 dividiendo el 8 por 4 y el 12 por 2.", "Se dividió arriba y abajo por números distintos.", "Se divide por el mismo número: 8 ÷ 4 = 2 y 12 ÷ 4 = 3, queda 2/3."),
        M("Decir que 7/9 se puede simplificar por 2.", "El 7 no se puede dividir exacto por 2.", "7 y 9 solo tienen el 1 como divisor común: 7/9 es irreducible."),
    ],
    rec=[
        ex("Simplifica 4/8 dividiendo numerador y denominador por 4.", "1/2", "4 ÷ 4 = 1 y 8 ÷ 4 = 2."),
        ex("¿Por qué número se pueden dividir 6 y 9 para simplificar 6/9?", "3", "El 3 divide exacto a 6 y a 9."),
        ex("Simplifica 6/9.", "2/3", "6 ÷ 3 = 2 y 9 ÷ 3 = 3."),
    ],
    und=[
        ex("Simplifica 6/8.", "3/4", "Se divide por 2."),
        ex("Simplifica 10/15.", "2/3", "Se divide por 5."),
        ex("Simplifica 20/25.", "4/5", "Se divide por 5: 20 ÷ 5 = 4 y 25 ÷ 5 = 5."),
    ],
    app=[
        ex("Simplifica 18/24 hasta su forma más simple.", "3/4", "Se divide por 6, o por 2 y luego por 3."),
        ex("Simplifica 8/12.", "2/3", "Se divide por 4."),
        ex("15 de 20 estudiantes de un curso llevan lentes de sol en una salida. Escribe la fracción y simplifícala.", "15/20 = 3/4", "Se divide por 5."),
    ],
    rea=[
        ex("Rosa simplifica 8/12 dividiendo el numerador por 4 y el denominador por 2 y obtiene 2/6. ¿Es válido?", "No", "Se debe dividir arriba y abajo por el mismo número: 8/12 = 2/3."),
        ex("¿Es irreducible 7/9?", "Sí", "7 y 9 no tienen otro divisor común que el 1."),
    ],
    cha=[
        ex("De las fracciones propias con denominador 12 y numerador 1, 5, 7 y 11, ¿cuántas son irreducibles?", "4", "El único divisor común con 12 en esos numeradores es 1."),
        ex("Una fracción simplificada es 3/5 y su denominador original era 20. ¿Cuál era la fracción original?", "12/20", "20 ÷ 5 = 4 y 3 × 4 = 12."),
    ],
    ctx=[ex("Una pizza de 12 trozos tiene 9 trozos con queso. ¿Qué fracción de la pizza tiene queso en su forma más simple?", "3/4", "9/12 se divide por 3.")],
    sc=[
        ex("Simplifica 5/10.", "1/2", "Se divide por 5."),
        ex("Simplifica 14/21.", "2/3", "Se divide por 7."),
        ex("¿Es irreducible 3/4?", "Sí", "3 y 4 solo tienen el 1 como divisor común."),
    ],
    op=task(
        "Elige: 10/12, 16/24 o 9/15. Simplifícala hasta que sea irreducible, escribe los pasos con el número por el que divides y comprueba amplificando el resultado para volver a la fracción original.",
        "16/24: ÷ 2 = 8/12, ÷ 4 = 2/3. Es irreducible. Compruebo: 2/3 × 8/8 = 16/24.",
        ["divide por el mismo número", "llega a una fracción irreducible", "comprueba amplificando"],
        ["pasos escritos", "comprobación"],
        ["dividir por números distintos arriba y abajo", "detenerse antes de terminar"],
        "Pide que revise si el numerador y el denominador finales tienen otro divisor común.",
    ),
    reinforce="Escribe cinco fracciones con denominador 10 y simplifica las que se puedan.",
    extend="Explica cómo saber si una fracción es irreducible sin simplificarla.",
)

# ------------------------------------------------------------------ OA 07 clase 4
lesson(
    OA7, 4,
    use="Aprenderé a comparar fracciones propias con igual y distinto denominador. Sirve para saber cuál parte es mayor.",
    prior=["Sé amplificar y simplificar fracciones.", "Sé que 1/2 equivale a 2/4."],
    explain=[
        "Si dos fracciones tienen el mismo denominador, las partes son del mismo tamaño y gana la que tiene mayor numerador. Así 5/8 > 3/8 porque 5 partes son más que 3 partes iguales. Si tienen el mismo numerador, gana la que tiene menor denominador: 3/5 > 3/8 porque las quintas partes son más grandes que las octavas.",
        "Si tienen distinto denominador, se amplifican hasta tener el mismo. Para 2/3 y 3/5 se usa 15 como denominador común: 2/3 = 10/15 y 3/5 = 9/15. Como 10 > 9, 2/3 > 3/5. Una buena forma de buscar el denominador común es multiplicar los dos denominadores.",
        "También puedes comparar con 1/2. Una fracción es menor que 1/2 si el doble de su numerador es menor que su denominador. Así 3/7 < 1/2 porque 3 + 3 = 6, que es menos que 7. El resultado se escribe con los símbolos < o >.",
    ],
    vocab=[("denominador común", "denominador igual en dos fracciones equivalentes a las originales"), ("comparar", "decidir cuál es mayor o menor"), ("mayor que", "símbolo > que indica que una cantidad es mayor"), ("menor que", "símbolo < que indica que una cantidad es menor"), ("referente", "número conocido, como 1/2, que se usa para comparar")],
    worked=[
        W("Distinto denominador", "Compara 2/3 y 3/5.", ["Denominador común: 3 × 5 = 15.", "2/3 = 10/15 y 3/5 = 9/15.", "10/15 > 9/15."], "2/3 > 3/5"),
        W("Con el referente 1/2", "Compara 5/12 con 1/2.", ["1/2 = 6/12.", "5/12 < 6/12."], "5/12 < 1/2"),
    ],
    mistakes=[
        M("Decir que 1/3 > 1/2 porque 3 es mayor que 2.", "Con el mismo numerador, mayor denominador significa partes más pequeñas.", "1/2 > 1/3."),
        M("Decir que 5/8 es mayor que 3/4 porque 5 y 8 son mayores que 3 y 4.", "Se comparan números sueltos sin igualar los denominadores.", "3/4 = 6/8 y 6/8 > 5/8, así que 3/4 es mayor."),
    ],
    rec=[
        ex("Compara 2/9 y 7/9 con < o >.", "2/9 < 7/9", "Mismo denominador: gana el mayor numerador."),
        ex("¿Cuál es mayor, 1/4 o 1/6?", "1/4", "Con igual numerador, mayor denominador da partes más pequeñas."),
        ex("Escribe 1/2 con denominador 12.", "6/12", "Se multiplica por 6 arriba y abajo."),
    ],
    und=[
        ex("Compara 3/4 y 5/8.", "3/4 > 5/8", "3/4 = 6/8 y 6/8 > 5/8."),
        ex("Compara 2/3 y 3/5.", "2/3 > 3/5", "10/15 > 9/15."),
        ex("Compara 5/12 con 1/2.", "5/12 < 1/2", "1/2 = 6/12 y 5 < 6."),
    ],
    app=[
        ex("Una receta usa 2/3 de taza de harina y otra receta usa 5/8 de taza. ¿Cuál usa más?", "La primera", "2/3 = 16/24 y 5/8 = 15/24."),
        ex("Rita bebió 3/5 de su botella y Jaime bebió 3/8 de otra botella igual. ¿Quién bebió más?", "Rita", "Mismo numerador: 3/5 > 3/8."),
        ex("¿Cuál es menor, 4/9 o 1/2?", "4/9", "El doble de 4 es 8, que es menos que 9, así que 4/9 es menos de la mitad."),
    ],
    rea=[
        ex("José dice que 1/3 > 1/2 porque 3 > 2. ¿Tiene razón?", "No", "Con igual numerador, mayor denominador da partes más pequeñas."),
        ex("Ordena de menor a mayor: 2/5, 1/2 y 3/10.", "3/10 < 2/5 < 1/2", "En décimos: 3/10, 4/10 y 5/10."),
    ],
    cha=[
        ex("Encuentra una fracción con denominador 8 que esté entre 1/2 y 3/4.", "5/8", "1/2 = 4/8 y 3/4 = 6/8; la única entre ellas es 5/8."),
        ex("¿Cuántas fracciones con denominador 10 hay entre 1/5 y 4/5, sin contar los extremos?", "5", "1/5 = 2/10 y 4/5 = 8/10; entre ellas están 3/10, 4/10, 5/10, 6/10 y 7/10."),
    ],
    ctx=[ex("Dos amigos corren la misma pista. Uno recorrió 3/4 y el otro 7/10. ¿Quién recorrió más?", "El primero", "3/4 = 15/20 y 7/10 = 14/20.")],
    sc=[
        ex("Compara 4/7 y 2/7.", "4/7 > 2/7", "Con el mismo denominador gana el mayor numerador."),
        ex("Compara 1/2 y 3/8.", "1/2 > 3/8", "1/2 = 4/8."),
        ex("¿Cuál es mayor, 5/6 o 3/4?", "5/6", "5/6 = 10/12 y 3/4 = 9/12."),
    ],
    op=task(
        "Elige uno de estos pares: 3/5 y 2/3, 5/8 y 3/4 o 7/12 y 1/2. Compáralos usando un denominador común, escribe el símbolo < o > y dibuja dos barras iguales para comprobar.",
        "3/5 y 2/3: denominador común 15. 3/5 = 9/15 y 2/3 = 10/15. Entonces 3/5 < 2/3. En el dibujo, la barra de 2/3 tiene más sombreado.",
        ["amplifica a un denominador común", "usa < o > correctamente", "comprueba con un dibujo"],
        ["cálculo", "símbolo", "dibujo"],
        ["comparar solo los numeradores o solo los denominadores", "amplificar mal"],
        "Pide que compare los numeradores una vez que tengan el mismo denominador y que revise la barra.",
    ),
    reinforce="Compara 1/2 con 1/3, 1/4 y 1/5 y escríbelas de mayor a menor.",
    extend="Explica por qué 3/5 es mayor que 3/8 sin amplificar.",
)

# ------------------------------------------------------------------ OA 07 clase 5
lesson(
    OA7, 5,
    use="Aprenderé a ordenar y comparar varias fracciones, y a explicar mis decisiones. Sirve para comunicar resultados con fracciones con claridad.",
    prior=["Sé amplificar, simplificar y comparar fracciones propias."],
    explain=[
        "Para ordenar varias fracciones con distintos denominadores, busca un denominador común que sirva para todas. Por ejemplo, para 1/2, 2/3, 3/4 y 5/6 sirve el 12: 6/12, 8/12, 9/12 y 10/12. Una vez con el mismo denominador, solo se ordenan los numeradores.",
        "Después de comparar, comunica tu decisión con palabras y símbolos: «5/6 es mayor que 3/4 porque 10/12 > 9/12». Es importante que la justificación incluya la equivalencia usada, no solo el resultado. También puedes verificar con una barra o con la recta numérica entre 0 y 1.",
        "Antes de entregar tu respuesta, revisa cada paso: ¿amplificaste arriba y abajo por el mismo número?, ¿simplificaste al final si se podía?, ¿tu orden de menor a mayor es coherente con las fracciones originales? Si una fracción es mayor que 1/2 y otra menor, ya sabes cuál va antes.",
    ],
    vocab=[("ordenar", "poner en fila de menor a mayor o al revés"), ("denominador común", "denominador igual para varias fracciones"), ("justificar", "dar la razón de una decisión"), ("recta numérica", "línea con números ordenados"), ("coherente", "que no se contradice")],
    worked=[
        W("Ordenar cuatro fracciones", "Ordena de menor a mayor 5/6, 1/2, 3/4 y 2/3.", ["Denominador común 12: 5/6 = 10/12, 1/2 = 6/12, 3/4 = 9/12, 2/3 = 8/12.", "Orden de numeradores: 6, 8, 9, 10."], "1/2 < 2/3 < 3/4 < 5/6"),
        W("Comunicar la decisión", "¿Quién bebió más: Ana 3/4 de litro o Beto 7/10 de litro?", ["Denominador común 20: 3/4 = 15/20 y 7/10 = 14/20.", "15 > 14."], "Ana bebió más, porque 15/20 > 14/20"),
    ],
    mistakes=[
        M("Ordenar 1/2, 2/3 y 3/4 como 3/4 < 2/3 < 1/2 porque 4 > 3 > 2.", "Se miró solo el denominador.", "En doceavos: 6/12, 8/12 y 9/12. Orden: 1/2 < 2/3 < 3/4."),
        M("Decir que 5/6 es mayor sin decir por qué.", "Falta la justificación con la equivalencia.", "Escribe: 5/6 = 10/12 y 3/4 = 9/12, así que 5/6 > 3/4."),
    ],
    rec=[
        ex("Escribe 1/2 y 2/3 con denominador 6.", "3/6 y 4/6", "1/2 × 3/3 y 2/3 × 2/2."),
        ex("¿Cuál es mayor, 3/6 o 4/6?", "4/6", "Mismo denominador, mayor numerador."),
        ex("Si dos fracciones tienen el mismo denominador, ¿qué se compara?", "Los numeradores", "Las partes son del mismo tamaño."),
    ],
    und=[
        ex("Ordena de menor a mayor 5/6, 1/3, 3/4 y 1/2.", "1/3 < 1/2 < 3/4 < 5/6", "En doceavos: 10, 4, 9 y 6."),
        ex("Ordena de mayor a menor 3/10, 2/5 y 1/2.", "1/2 > 2/5 > 3/10", "En décimos: 5, 4 y 3."),
        ex("¿Qué fracción es mayor, 7/10 o 3/4?", "3/4", "20 es el denominador común: 14/20 y 15/20."),
    ],
    app=[
        ex("Tres amigos comieron de una misma barra de cereal: Ana 1/4, Beto 1/3 y Cata 1/6. Ordénalos de quien comió más a quien comió menos.", "Beto, Ana, Cata", "En doceavos: 4, 3 y 2."),
        ex("Un tanque A está lleno hasta 5/8 y un tanque B igual hasta 3/5. ¿Cuál tiene más agua?", "El A", "5/8 = 25/40 y 3/5 = 24/40."),
        ex("Una carrera tiene tres tramos y Ema corrió 2/5, 1/4 y 3/10 de la ruta en distintos días. Ordena de menor a mayor.", "1/4 < 3/10 < 2/5", "En veinteavos: 5, 6 y 8."),
    ],
    rea=[
        ex("Pía ordenó 1/3, 1/4 y 1/5 de menor a mayor como 1/3 < 1/4 < 1/5. ¿Está bien?", "No, es 1/5 < 1/4 < 1/3", "Con igual numerador, mayor denominador es una fracción menor."),
        ex("¿Qué fracción es mayor que 1/2: 4/9, 5/9 o 3/7?", "5/9", "Solo 5/9 cumple que su doble, 10, supera al denominador 9."),
    ],
    cha=[
        ex("Escribe una fracción entre 2/5 y 1/2 con denominador 20.", "9/20", "2/5 = 8/20 y 1/2 = 10/20; entre ellas queda 9/20."),
        ex("Ordena de menor a mayor 3/4, 2/3, 5/8 y 7/12.", "7/12 < 5/8 < 2/3 < 3/4", "En veinticuatroavos: 14, 15, 16 y 18."),
    ],
    ctx=[ex("En una colecta ficticia, el curso A juntó 3/4 de su meta, el B 4/5 y el C 7/10. ¿Cuál se acercó más a su meta?", "El B", "En veinteavos: 15, 16 y 14.")],
    sc=[
        ex("Ordena de menor a mayor: 1/2, 1/4 y 1/3.", "1/4 < 1/3 < 1/2", "En doceavos: 3, 4 y 6."),
        ex("¿Cuál es mayor, 5/9 o 1/2?", "5/9", "Más de la mitad de 9 partes."),
        ex("Escribe 3/5 y 7/10 con denominador 10 y compáralas.", "6/10 < 7/10", "3/5 = 6/10."),
    ],
    op=task(
        "Usa estos datos: en una carrera ficticia, cuatro amigos corrieron 3/4, 5/8, 7/10 y 2/3 de la ruta. Ordénalos de quien corrió menos a quien corrió más usando un denominador común, y escribe una frase que comunique el resultado.",
        "Denominador común 120: 3/4 = 90/120, 5/8 = 75/120, 7/10 = 84/120 y 2/3 = 80/120. Orden: 5/8 < 2/3 < 7/10 < 3/4. Corrió menos el amigo de 5/8 y más el de 3/4.",
        ["encuentra un denominador común", "ordena correctamente", "comunica con una frase"],
        ["fracciones equivalentes", "orden", "frase"],
        ["comparar solo denominadores", "no justificar"],
        "Pide que revise que todos los denominadores sean iguales antes de ordenar y que lea la frase en voz alta.",
    ),
    reinforce="Ordena de menor a mayor 1/2, 3/8 y 5/6 en tu cuaderno usando un denominador común.",
    extend="Explica cuándo conviene comparar con 1/2 en vez de buscar un denominador común.",
)
