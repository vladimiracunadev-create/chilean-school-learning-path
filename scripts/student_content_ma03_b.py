"""Student material for 3.º básico Matemática, OA 10 (dinero y cuatro operaciones) y OA 11 (fracciones de uso común)."""
from __future__ import annotations

from student_lessons import arith, evaluate, ex, fmt, register

OA10, OA11 = "MA03 OA 10", "MA03 OA 11"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def mon(q: str, expr: str, why: str) -> dict:
    """Closed exercise whose answer is an amount of money computed from `expr`."""
    value = evaluate(expr)
    shown = " ".join(expr.replace("//", " ÷ ").replace("*", " × ").replace("-", " − ").replace("+", " + ").split())
    return ex(q, f"${fmt(value)}", f"{why} Cálculo: {shown} = {fmt(value)}.", calc=expr)


PRICES = "Los precios están escritos en pesos ($). Las monedas son de $10, $50, $100 y $500; los billetes, de $1.000, $2.000, $5.000 y más."

# ================================================================ OA 10
register(
    OA10, 1,
    materials=f"Lápiz y papel. {PRICES} Si quieres, usa monedas de juguete o de verdad con una persona de tu casa.",
    use="Aprenderé a calcular cuánto cuesta una compra de varios productos. Sirve para saber cuánto dinero llevar y cuánto hay que pagar.",
    prior=["Sé sumar números de hasta tres cifras.", "Conozco las monedas de $10, $50, $100 y $500."],
    explain=[
        "El precio es lo que cuesta un producto. El total es todo lo que hay que pagar por la compra completa. Si compras dos o más productos distintos, el total se calcula sumando los precios.",
        "Por ejemplo, un jugo cuesta $250 y un pan cuesta $180. Para saber el total, sumas: 250 + 180 = 430. El total es $430. Puedes sumar por partes: primero las centenas, luego las decenas.",
        "No elijas la operación por una palabra suelta. Primero pregúntate qué pasa con el dinero: ¿se junta o se separa? Aquí los precios se juntan en una sola cuenta, así que se suma. Al final, escribe la respuesta con el signo $.",
    ],
    vocab=[("precio", "lo que cuesta un producto"), ("total", "todo lo que hay que pagar por la compra"), ("compra", "productos que se pagan juntos"), ("sumar", "juntar cantidades para saber cuánto hay en total"), ("pesos ($)", "unidad de dinero que se usa en Chile")],
    worked=[
        {"title": "Dos productos", "problem": "Un cuaderno cuesta $450 y un lápiz cuesta $200. ¿Cuánto cuesta comprar los dos?", "steps": ["Los precios se juntan en una sola compra, así que sumo.", "450 + 200: 400 + 200 = 600 y queda el 50.", "600 + 50 = 650."], "answer": "$650"},
        {"title": "Tres productos", "problem": "Una caja de lápices cuesta $350, un borrador $150 y una regla $200. ¿Cuál es el total?", "steps": ["Sumo los tres precios: 350 + 150 + 200.", "350 + 150 = 500.", "500 + 200 = 700."], "answer": "$700"},
    ],
    mistakes=[
        {"wrong": "Ana tiene $300 y compra un cuaderno de $120 más una goma de $60. Resta porque ve la palabra «compra».", "why": "Elige la operación por una palabra y no por lo que pasa con los precios.", "fix": "Los dos precios se juntan en un total: 120 + 60 = 180."},
        {"wrong": "Escribir el total sin el signo $, solo 430.", "why": "Se olvida que la respuesta es una cantidad de dinero.", "fix": "Escribe $430."},
    ],
    tiers={
        "recovery": [
            mon("Un helado cuesta $300 y una galleta $200. ¿Cuánto cuesta comprar los dos?", "300+200", "Los precios se juntan."),
            mon("Un jugo cuesta $250 y un pan $150. ¿Cuánto pagas por los dos?", "250+150", "Se suman los dos precios."),
            mon("Tienes una moneda de $500 y una de $100. ¿Cuánto dinero tienes en total?", "500+100", "Se juntan los dos valores."),
        ],
        "understand": [
            ex("¿Qué significa «total» en una compra?", "Todo lo que hay que pagar por la compra completa", "El total junta el precio de todos los productos."),
            ex("Estás comprando productos distintos y quieres el total. ¿Sumas o restas los precios?", "Sumas", "Los precios se juntan en una sola cuenta."),
            ex("Una compra cuesta $400. Agregas un producto más a la compra. ¿El total sube o baja?", "Sube", "Agregar un producto hace que haya más que pagar."),
        ],
        "apply": [
            mon("Un libro cuesta $340 y un cuaderno $230. ¿Cuál es el total?", "340+230", "Se suman centenas, decenas y unidades."),
            mon("En el kiosco compras una bebida de $120, un sándwich de $250 y una fruta de $310. ¿Cuánto es el total?", "120+250+310", "Se suman los tres precios."),
            mon("Tienes $180 en tu alcancía y recibes $320 más. ¿Cuánto dinero tienes ahora?", "180+320", "El dinero que tenías y el nuevo se juntan."),
        ],
        "reason": [
            ex("Sofía compra una regla de $240 y una goma de $160. Paga con un billete de $1.000. Joaquín dice que el total es $1.000. ¿Tiene razón? Explica.", "No; el total es $400", "El total es la suma de los precios, 240 + 160 = 400, no el billete con que se paga."),
            ex("Dante quiere un cuaderno de $650 y un lápiz de $300. Tiene $900. ¿Le alcanza?", "No; necesita $950", "650 + 300 = 950 y 950 es mayor que 900."),
        ],
        "challenge": [
            ex("Tienes $800. Los productos son: pelota $450, cuerda $350, globo $200 y silbato $400. ¿Qué dos productos suman exactamente $800?", "La pelota y la cuerda", "450 + 350 = 800, y ninguna otra pareja da 800."),
            mon("En una compra, el primer producto cuesta $210, el segundo cuesta $100 más que el primero y el tercero cuesta $90. ¿Cuál es el total de los tres?", "210+(210+100)+90", "El segundo cuesta 210 + 100 = 310."),
        ],
    },
    context=[mon("En la feria compras un kilo de papas por $700 y un kilo de cebollas por $250. ¿Cuánto pagas por los dos kilos?", "700+250", "Los dos precios se juntan.")],
    selfcheck=[
        mon("Un lápiz cuesta $120 y un cuaderno $380. ¿Cuánto cuestan juntos?", "120+380", "Se suman los precios."),
        ex("Si el total de una compra es $600 y agregas un producto, ¿el nuevo total es mayor o menor que $600?", "Mayor", "Se agrega más dinero a pagar."),
        mon("Escribe el total de comprar productos de $200, $350 y $100.", "200+350+100", "Se suman los tres."),
    ],
    open_task=task(
        "Elige uno de estos pedidos y calcula su total: A) un pan de $250, una leche de $400 y un queso de $300; B) un cuaderno de $500, un lápiz de $150 y una goma de $100. Escribe la suma, el total y una frase que explique por qué sumaste.",
        "Pedido B: 500 + 150 + 100 = 750. El total es $750. Sumé porque los tres precios se juntan en una sola compra.",
        ["escribe la suma con los tres precios", "calcula el total correcto", "usa el signo $", "explica por qué suma"],
        ["suma escrita", "total", "frase de explicación"],
        ["restar por la palabra «compra»", "olvidar el signo $"],
        "Pide que cuente en voz alta qué pasa con el dinero (se junta). Reconoce la explicación, no solo el resultado.",
    ),
    reinforce="Con una persona de tu casa, elige tres productos de un folleto de supermercado o inventa precios redondos, y calcula el total de cada pareja de productos.",
    extend="Escribe un problema de compra con tres productos de precios distintos cuyo total sea $900. Resuélvelo.",
)

register(
    OA10, 2,
    materials=f"Lápiz y papel. {PRICES}",
    use="Aprenderé a calcular el vuelto cuando pago con más dinero del que cuesta lo que compro. Sirve para comprobar que me devuelvan lo justo.",
    prior=["Sé restar números de hasta tres cifras.", "Sé qué es el precio y el total."],
    explain=[
        "Cuando pagas con más dinero del que cuesta lo que compras, te devuelven la diferencia. Ese dinero se llama vuelto. El vuelto es lo que sobra al pagar.",
        "Para calcularlo, restas el precio al dinero con que pagas. Por ejemplo, pagas con $1.000 un pan que cuesta $650. El vuelto es 1.000 − 650 = 350. Recibes $350.",
        "Puedes comprobar sumando: precio más vuelto debe dar el dinero con que pagaste. Aquí, 650 + 350 = 1.000, así que está bien. Si te falta dinero, también restas: lo que cuesta menos lo que tienes es lo que te falta.",
    ],
    vocab=[("vuelto", "dinero que te devuelven al pagar con más de lo que cuesta"), ("diferencia", "resultado de restar dos cantidades"), ("restar", "quitar una cantidad de otra para ver cuánto queda"), ("pagar con", "entregar dinero para pagar una compra"), ("comprobar", "revisar que un resultado sea correcto")],
    worked=[
        {"title": "Calcular el vuelto", "problem": "Pagas con $500 una compra de $280. ¿Cuánto es el vuelto?", "steps": ["Pago más de lo que cuesta, así que me devuelven dinero.", "Resto el precio al dinero con que pago: 500 − 280.", "500 − 280 = 220.", "Compruebo: 280 + 220 = 500."], "answer": "$220"},
        {"title": "Cuánto falta", "problem": "Un juguete cuesta $700 y tienes $450. ¿Cuánto dinero te falta?", "steps": ["Te falta la diferencia entre el precio y lo que tienes.", "700 − 450 = 250.", "Compruebo: 450 + 250 = 700."], "answer": "$250"},
    ],
    mistakes=[
        {"wrong": "Pagar con $500 una compra de $300 y decir que el vuelto es $800.", "why": "Se suma porque «vuelto» suena a juntar.", "fix": "El vuelto es lo que sobra, así que se resta: 500 − 300 = 200."},
        {"wrong": "Calcular 280 − 500 para el vuelto.", "why": "Se resta en el orden contrario.", "fix": "Se parte desde el dinero con que pagas: 500 − 280."},
    ],
    tiers={
        "recovery": [
            mon("Pagas con $500 un pan de $200. ¿Cuánto es el vuelto?", "500-200", "Se resta el precio al dinero entregado."),
            mon("Pagas con un billete de $1.000 un helado de $400. ¿Cuánto es el vuelto?", "1000-400", "Se resta el precio al billete."),
            mon("Pagas con una moneda de $100 un chicle de $60. ¿Cuánto es el vuelto?", "100-60", "Se resta el precio a la moneda."),
        ],
        "understand": [
            ex("¿Qué es el vuelto?", "El dinero que te devuelven cuando pagas con más de lo que cuesta", "Es la diferencia entre lo que entregas y el precio."),
            ex("Pagas con $500 un producto de $350. ¿El vuelto es mayor o menor que $500?", "Menor", "Solo sobra una parte del dinero entregado."),
            ex("Para calcular el vuelto, ¿qué operación haces con el precio y el dinero con que pagas?", "Restar el precio al dinero con que pagas", "El vuelto es lo que sobra."),
        ],
        "apply": [
            mon("Pagas con $1.000 un juguete de $740. ¿Cuánto es el vuelto?", "1000-740", "Se resta el precio al billete."),
            mon("Un cuaderno cuesta $850 y tienes $600. ¿Cuánto dinero te falta?", "850-600", "Falta la diferencia entre el precio y lo que tienes."),
            mon("Tenías $900 y gastaste $570 en una compra. ¿Cuánto dinero te queda?", "900-570", "Se quita lo gastado a lo que tenías."),
        ],
        "reason": [
            ex("Marta paga con $1.000 un juguete de $450 y recibe $550 de vuelto. ¿Es correcto? Comprueba.", "Sí; 450 + 550 = 1.000", "El precio más el vuelto debe dar lo que se entregó."),
            ex("Tomás paga con $500 algo de $300 y dice que el vuelto es $800. ¿Cuál es su error y cuál es el vuelto correcto?", "Sumó en vez de restar; el vuelto es $200", "El vuelto es lo que sobra: 500 − 300 = 200."),
        ],
        "challenge": [
            mon("Pagaste con $1.000 y recibiste $270 de vuelto. ¿Cuánto costó lo que compraste?", "1000-270", "El precio es lo que entregaste menos el vuelto."),
            mon("Pagaste con una moneda de $500 y te dieron $120 de vuelto. ¿Cuál era el precio?", "500-120", "El precio es el dinero entregado menos el vuelto."),
        ],
    },
    context=[mon("En el almacén, un paquete de fideos cuesta $650. Pagas con un billete de $1.000. ¿Cuánto vuelto debe darte el vendedor?", "1000-650", "Se resta el precio al billete.")],
    selfcheck=[
        mon("Pagas con $500 una compra de $420. ¿Cuánto es el vuelto?", "500-420", "Se resta el precio al dinero entregado."),
        ex("Pagas justo lo que cuesta un producto. ¿Cuánto es el vuelto?", "$0", "No sobra dinero."),
        ex("Escribe la resta que calcula el vuelto al pagar con $1.000 una compra de $560 y su resultado.", "1.000 − 560 = 440", "Se resta el precio al billete.", calc="1000-560"),
    ],
    open_task=task(
        "Elige una de estas situaciones y calcula el vuelto: A) pagas con $1.000 un helado de $450; B) pagas con $500 un jugo de $330. Escribe la resta y comprueba sumando precio y vuelto.",
        "Situación B: 500 − 330 = 170. El vuelto es $170. Comprobación: 330 + 170 = 500.",
        ["escribe la resta en el orden correcto", "calcula el vuelto", "comprueba sumando", "usa el signo $"],
        ["resta escrita", "comprobación", "respuesta con $"],
        ["sumar en vez de restar", "restar al revés"],
        "Pide que explique con qué dinero se parte. Reconoce la comprobación como una buena costumbre.",
    ),
    reinforce="Con monedas de juguete, «compra» algo de $300 pagando con $500 y revisa que el vuelto, sumado al precio, dé $500.",
    extend="Inventa un problema de vuelto con un billete de $1.000 donde el vuelto sea justo $250. ¿Cuál sería el precio?",
)

register(
    OA10, 3,
    materials=f"Lápiz y papel. {PRICES} Todas las cuentas usan precios de hasta $100 por unidad.",
    use="Aprenderé a calcular el costo de varias unidades que cuestan lo mismo. Sirve para saber cuánto pagar por 5 cuadernos iguales o 6 bebidas iguales.",
    prior=["Conozco las tablas de multiplicar hasta el 10.", "Sé que multiplicar es sumar muchas veces el mismo número."],
    explain=[
        "Cuando compras varias unidades que cuestan lo mismo, el total es el precio de una unidad repetido muchas veces. Esa suma repetida se escribe como una multiplicación. Cantidad × precio de una unidad = total.",
        "Por ejemplo, 4 chocolates a $30 cada uno. Puedes sumar 30 + 30 + 30 + 30 = 120, o multiplicar 4 × 30 = 120. Para 4 × 30 piensa que 30 son 3 decenas: 4 × 3 = 12 decenas, o sea 120.",
        "Antes de calcular, identifica dos datos: cuántas unidades compras y cuánto cuesta cada una. Multiplicas esos dos números. No sumes la cantidad con el precio, porque no son dinero que se junte.",
    ],
    vocab=[("unidad", "una de las cosas iguales que se compran"), ("cantidad", "cuántas unidades se compran"), ("precio de una unidad", "lo que cuesta una sola cosa"), ("multiplicación", "operación que repite una suma de sumandos iguales"), ("suma repetida", "sumar muchas veces el mismo número")],
    worked=[
        {"title": "Multiplicar cantidad por precio", "problem": "Un chicle cuesta $20. ¿Cuánto cuestan 6 chicles?", "steps": ["Hay 6 unidades que cuestan $20 cada una.", "Multiplico: 6 × 20.", "6 × 2 decenas = 12 decenas = 120."], "answer": "$120"},
        {"title": "Comprobar con suma repetida", "problem": "Un lápiz cuesta $50. ¿Cuánto cuestan 3 lápices? Comprueba sumando.", "steps": ["Multiplico: 3 × 50 = 150.", "Compruebo con suma repetida: 50 + 50 + 50 = 150.", "Los dos resultados coinciden."], "answer": "$150"},
    ],
    mistakes=[
        {"wrong": "Camila compra 5 manzanas de $40 cada una y escribe 5 + 40 = 45.", "why": "Suma la cantidad con el precio, que no son dinero que se junte.", "fix": "Hay 5 grupos de $40: 5 × 40 = 200."},
        {"wrong": "Multiplicar bien 4 × 3 = 12 y responder $12 para 4 productos de $30.", "why": "Se olvida que 30 son 3 decenas.", "fix": "12 decenas son 120, así que son $120."},
    ],
    tiers={
        "recovery": [
            mon("Un chicle cuesta $20. ¿Cuánto cuestan 3 chicles?", "3*20", "Hay 3 grupos de $20."),
            mon("Una bolsa de caramelos cuesta $10. ¿Cuánto cuestan 4 bolsas?", "4*10", "Hay 4 grupos de $10."),
            ex("Escribe la suma repetida para 3 caramelos de $50 cada uno y su total.", "50 + 50 + 50 = 150", "Cada caramelo suma $50 y son tres.", calc="3*50"),
        ],
        "understand": [
            ex("¿Qué operación resume sumar muchas veces el mismo precio?", "La multiplicación", "Multiplicar es repetir una suma de sumandos iguales."),
            ex("En «6 × $40», ¿cuál número es la cantidad y cuál es el precio de una unidad?", "La cantidad es 6 y el precio es $40", "El primer número cuenta unidades y el segundo dice cuánto vale cada una."),
            ex("¿Es mayor el total de 7 cuadernos de $50 o el de 7 cuadernos de $30?", "El de los cuadernos de $50", "Con la misma cantidad, el precio mayor da mayor total."),
        ],
        "apply": [
            mon("Un paquete de stickers cuesta $30. Compras 8 paquetes. ¿Cuánto pagas?", "8*30", "Hay 8 grupos de $30."),
            mon("Una bebida cuesta $70. ¿Cuánto cuestan 6 bebidas?", "6*70", "6 × 7 = 42 decenas."),
            mon("Compras 9 globos a $100 cada uno. ¿Cuánto pagas en total?", "9*100", "Hay 9 grupos de $100."),
        ],
        "reason": [
            ex("Camila compró 5 manzanas a $40 cada una y escribió 5 + 40 = 45. ¿Cuál es su error y cuánto debía pagar?", "Sumó la cantidad con el precio; debía multiplicar y pagar $200", "Son 5 grupos de $40: 5 × 40 = 200.", calc="5*40"),
            ex("Leo compra 4 globos de $60 cada uno. Eva compra 6 globos de $40 cada uno. ¿Quién paga más?", "Pagan lo mismo, $240", "4 × 60 = 240 y 6 × 40 = 240.", calc="4*60"),
        ],
        "challenge": [
            mon("Una caja de lápices cuesta $90. Para un curso se compran 9 cajas iguales. ¿Cuál es el total?", "9*90", "Hay 9 grupos de $90."),
            ex("Necesitas 8 pliegos de cartulina a $70 cada uno y tienes una moneda de $500. Calcula el total de los pliegos y responde si te alcanza.", "El total es $560 y no te alcanza", "8 × 70 = 560 y 560 es mayor que 500.", calc="8*70"),
        ],
    },
    context=[mon("En la feria del colegio, 6 empanadas cuestan $90 cada una. ¿Cuánto cuestan las 6 empanadas?", "6*90", "Hay 6 grupos de $90.")],
    selfcheck=[
        mon("Una paleta cuesta $60. ¿Cuánto cuestan 5 paletas?", "5*60", "Hay 5 grupos de $60."),
        mon("¿Cuánto cuestan 10 bolsas de pan a $50 cada una?", "10*50", "Hay 10 grupos de $50."),
        ex("Para calcular el costo de 4 unidades iguales de $80, ¿qué escribes: 4 + 80 o 4 × 80?", "4 × 80", "Hay 4 grupos iguales de $80."),
    ],
    open_task=task(
        "Elige una situación: A) 7 cuadernos de $60 cada uno; B) 5 bebidas de $90 cada una. Escribe la multiplicación, el total, y comprueba con la suma repetida.",
        "Situación A: 7 × 60 = 420. Total $420. Comprobación: 60 + 60 + 60 + 60 + 60 + 60 + 60 = 420.",
        ["escribe cantidad × precio", "calcula el total correcto", "comprueba con suma repetida", "usa el signo $"],
        ["multiplicación escrita", "suma repetida", "respuesta con $"],
        ["sumar cantidad más precio", "olvidar los ceros"],
        "Pide que diga qué número es la cantidad y cuál es el precio. Reconoce la comprobación con suma repetida.",
    ),
    reinforce="Con una persona de tu casa, di el precio de un producto (redondo, como $20 o $50) y calcula cuánto cuestan 2, 3, 4 y 5 unidades.",
    extend="Un producto cuesta $80. Haz una tabla con el costo de 1, 2, 3, 4 y 5 unidades y escribe qué notas.",
)

register(
    OA10, 4,
    materials=f"Lápiz y papel. {PRICES} Puedes usar fichas o semillas para repartir.",
    use="Aprenderé a repartir un monto o una colección en partes iguales. Sirve para saber cuánto toca a cada persona o cuántos grupos se forman.",
    prior=["Sé las tablas de multiplicar hasta el 10.", "Sé que dividir y multiplicar se relacionan."],
    explain=[
        "Dividir sirve para repartir en partes iguales. Si repartes $40 entre 4 amigos, cada uno recibe lo mismo. Calculas 40 ÷ 4 = 10. A cada uno le toca $10.",
        "También se divide para armar grupos. Si tienes 20 lápices y guardas 5 en cada caja, ¿cuántas cajas necesitas? Calculas 20 ÷ 5 = 4. Se llenan 4 cajas.",
        "La tabla de multiplicar te ayuda a dividir. Para 24 ÷ 6 piensa: ¿qué número por 6 da 24? Es 4, porque 4 × 6 = 24. Si el dinero es en decenas, también funciona: $240 son 24 decenas; 24 decenas ÷ 4 = 6 decenas, o sea $60.",
    ],
    vocab=[("dividir", "repartir en partes iguales o armar grupos iguales"), ("repartir", "dar la misma cantidad a cada uno"), ("partes iguales", "partes que tienen exactamente lo mismo"), ("grupo", "conjunto de cosas que se juntan"), ("tabla de multiplicar", "lista de multiplicaciones que ayuda a dividir")],
    worked=[
        {"title": "Repartir un monto", "problem": "Se reparten $240 en partes iguales entre 4 niños. ¿Cuánto recibe cada uno?", "steps": ["Se reparte en partes iguales, así que divido: 240 ÷ 4.", "$240 son 24 decenas.", "24 ÷ 4 = 6 decenas, o sea 60.", "Compruebo: 4 × 60 = 240."], "answer": "$60"},
        {"title": "Armar grupos", "problem": "Hay 35 stickers y se pone 5 en cada sobre. ¿Cuántos sobres se llenan?", "steps": ["Quiero saber cuántos grupos de 5 caben en 35.", "35 ÷ 5 = 7, porque 7 × 5 = 35.", "Se llenan 7 sobres."], "answer": "7 sobres"},
    ],
    mistakes=[
        {"wrong": "Pedro reparte 18 caramelos entre 3 niños y calcula 18 − 3 = 15.", "why": "Resta el número de niños en vez de repartir en partes iguales.", "fix": "Divide: 18 ÷ 3 = 6 caramelos para cada niño."},
        {"wrong": "Responder que $240 entre 4 son $6.", "why": "Se divide solo 24 ÷ 4 y se olvida que eran decenas.", "fix": "6 decenas son $60."},
    ],
    tiers={
        "recovery": [
            mon("Repartes $40 en partes iguales entre 4 amigos. ¿Cuánto recibe cada uno?", "40//4", "Cada amigo recibe lo mismo."),
            arith("Hay 12 galletas y se ponen en 3 platos con la misma cantidad. ¿Cuántas galletas hay en cada plato?", "12//3", "Se reparte en partes iguales.", " galletas"),
            arith("Hay 20 lápices y se guardan 5 en cada caja. ¿Cuántas cajas se llenan?", "20//5", "Se arman grupos de 5.", " cajas"),
        ],
        "understand": [
            ex("¿Qué significa repartir en partes iguales?", "Dar la misma cantidad a cada uno, sin que sobre", "Todos reciben exactamente lo mismo."),
            ex("¿Qué operación usas para repartir un monto de dinero en partes iguales?", "La división", "Dividir sirve para repartir en partes iguales."),
            ex("Repartes $60 entre 2 personas. ¿Cada una recibe más o menos de $60?", "Menos", "Cada persona recibe solo una parte del monto."),
        ],
        "apply": [
            mon("Repartes $240 entre 4 amigos en partes iguales. ¿Cuánto recibe cada uno?", "240//4", "24 decenas entre 4 son 6 decenas."),
            arith("Hay 35 stickers y se ponen 5 en cada sobre. ¿Cuántos sobres se llenan?", "35//5", "Se arman grupos de 5.", " sobres"),
            mon("Cinco amigos pagan una cuenta de $450 en partes iguales. ¿Cuánto paga cada uno?", "450//5", "45 decenas entre 5 son 9 decenas."),
        ],
        "reason": [
            ex("Pedro reparte 18 caramelos entre 3 niños y dice que a cada uno le tocan 15, porque 18 − 3 = 15. ¿Qué error comete y cuántos le tocan?", "Resta en vez de dividir; le tocan 6", "Repartir en partes iguales es dividir: 18 ÷ 3 = 6.", calc="18//3"),
            ex("Se reparten 28 bolitas entre 4 niños, o bien entre 7 niños. ¿En cuál reparto recibe más bolitas cada niño?", "Entre 4 niños, con 7 cada uno", "28 ÷ 4 = 7 y 28 ÷ 7 = 4.", calc="28//4"),
        ],
        "challenge": [
            mon("Tres amigos juntaron $210 poniendo todos lo mismo. ¿Cuánto puso cada uno?", "210//3", "21 decenas entre 3 son 7 decenas."),
            mon("Seis amigos juntaron $420 poniendo cada uno la misma cantidad. ¿Cuánto puso cada uno?", "420//6", "42 decenas entre 6 son 7 decenas."),
        ],
    },
    context=[mon("Seis amigos compran una pizza de $480 y la pagan en partes iguales. ¿Cuánto paga cada uno?", "480//6", "48 decenas entre 6 son 8 decenas.")],
    selfcheck=[
        arith("¿Cuánto es 36 ÷ 4?", "36//4", "Porque 9 × 4 = 36."),
        mon("Repartes $100 en partes iguales entre 5 personas. ¿Cuánto recibe cada una?", "100//5", "Porque 5 × 20 = 100."),
        ex("Si 7 × 8 = 56, ¿cuánto es 56 ÷ 8?", "7", "La división deshace la multiplicación.", calc="56//8"),
    ],
    open_task=task(
        "Elige un reparto y resuélvelo: A) $320 entre 4 personas; B) 48 lápices en cajas de 6. Escribe la división, la respuesta con su unidad y una multiplicación que la compruebe.",
        "Reparto B: 48 ÷ 6 = 8. Se necesitan 8 cajas. Comprobación: 8 × 6 = 48.",
        ["escribe la división correcta", "responde con unidad ($ o cajas)", "comprueba con una multiplicación", "dice si repartió o armó grupos"],
        ["división escrita", "comprobación", "respuesta con unidad"],
        ["restar en vez de dividir", "olvidar que son decenas"],
        "Pide que diga si está repartiendo o armando grupos. Reconoce la comprobación con la tabla.",
    ),
    reinforce="Con 24 semillas o fichas, reparte en partes iguales entre 2, 3, 4 y 6 platos y anota cuántas quedan en cada plato.",
    extend="Reparte $600 en partes iguales entre 2, 3, 5 y 6 personas. ¿Entre cuántas personas cada una recibe más?",
)

# ================================================================ OA 11
KEY = "Clave de dibujo: ▮ es una parte pintada y ▯ una parte sin pintar. Todas las partes del dibujo son iguales."

register(
    OA11, 1,
    materials="Una hoja de papel, lápiz y regla. Si quieres, cinta o cordel. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé qué es una fracción y cómo nace al repartir un entero en partes iguales. Sirve para decir qué parte de una torta o de una cinta te toca.",
    prior=["Sé contar hasta 10.", "Sé repartir un objeto en partes y decir cuántas hay."],
    explain=[
        "El entero es la cosa completa que repartimos, como un pan, una torta o una cinta. Para hacer una fracción, el entero se divide en partes iguales. Si las partes no son iguales, no hay fracción.",
        "Una fracción se escribe con dos números separados por una raya. El de abajo se llama denominador y dice en cuántas partes iguales se dividió el entero. El de arriba se llama numerador y dice cuántas partes se toman. En 3/4, el entero tiene 4 partes iguales y se toman 3.",
        "Se leen así: 1/2 es un medio, 1/3 es un tercio, 1/4 es un cuarto, 2/3 es dos tercios y 3/4 es tres cuartos. Una fracción siempre habla de una parte de un mismo todo.",
    ],
    vocab=[("entero", "la cosa completa que se reparte"), ("partes iguales", "partes del mismo tamaño"), ("denominador", "número de abajo: en cuántas partes iguales se dividió el entero"), ("numerador", "número de arriba: cuántas partes se toman"), ("fracción", "número que muestra una parte de un entero dividido en partes iguales")],
    worked=[
        {"title": "Un cuarto de una pizza", "problem": "Una pizza se corta en 4 partes iguales y tú comes 1. ¿Qué fracción comiste?", "steps": ["El entero es la pizza completa.", "Se dividió en 4 partes iguales: el denominador es 4.", "Tomaste 1 parte: el numerador es 1."], "answer": "1/4 (un cuarto)"},
        {"title": "Revisar si las partes son iguales", "problem": "Una cinta de 12 cm se corta en 3 pedazos de 4 cm, 4 cm y 4 cm. ¿Cada pedazo es 1/3?", "steps": ["Reviso si los tres pedazos son iguales.", "Los tres miden 4 cm.", "Hay 3 partes iguales, así que cada pedazo es 1/3."], "answer": "Sí, cada pedazo es 1/3"},
    ],
    mistakes=[
        {"wrong": "Cortar una barra en dos partes de distinto tamaño y llamar 1/2 a cada una.", "why": "Se olvida que las partes deben ser iguales.", "fix": "Solo es 1/2 si las dos partes miden lo mismo."},
        {"wrong": "Escribir 4/1 para un cuarto.", "why": "Se invierten el numerador y el denominador.", "fix": "El denominador (abajo) cuenta las partes iguales del entero: 1/4."},
    ],
    tiers={
        "recovery": [
            ex("Un pan se corta en 2 partes iguales. ¿Qué fracción es cada parte?", "1/2 (un medio)", "Hay dos partes iguales y se toma una."),
            ex("Una barra de chocolate se divide en 4 partes iguales. ¿Qué fracción es una parte?", "1/4 (un cuarto)", "Hay cuatro partes iguales y se toma una."),
            ex("Una cinta se corta en 3 pedazos iguales. ¿Qué fracción del largo es un pedazo?", "1/3 (un tercio)", "Hay tres partes iguales y se toma una."),
        ],
        "understand": [
            ex("En la fracción 1/4, ¿qué dice el número 4?", "Que el entero se divide en 4 partes iguales", "El número de abajo cuenta las partes iguales del entero."),
            ex("En la fracción 1/4, ¿qué dice el número 1?", "Que se toma 1 parte", "El número de arriba cuenta las partes que se toman."),
            ex("Un cuadrado de papel se corta en dos partes, una de 3 cm de ancho y otra de 5 cm. ¿Cada parte es 1/2 del cuadrado?", "No; las partes no son iguales", "Para que sea un medio, las dos partes deben ser iguales."),
        ],
        "apply": [
            ex("Una pizza se divide en 4 partes iguales y comes 3. ¿Qué fracción comiste?", "3/4 (tres cuartos)", "Hay 4 partes iguales y se toman 3."),
            ex("Un listón se divide en 3 partes iguales y pintas 2. ¿Qué fracción pintaste?", "2/3 (dos tercios)", "Hay 3 partes iguales y se toman 2."),
            ex("Una torta se divide en 3 partes iguales y se come 1. ¿Qué fracción de la torta queda sin comer?", "2/3 (dos tercios)", "De 3 partes iguales quedan 2."),
        ],
        "reason": [
            ex("Ana cortó una barra en 3 partes: una de 2 cm, otra de 2 cm y otra de 6 cm. Dice que cada parte es 1/3. ¿Tiene razón?", "No; las partes no son iguales", "Un tercio exige tres partes del mismo tamaño."),
            ex("Se corta una hoja en 2 partes iguales y otra hoja igual en 4 partes iguales. ¿Qué parte es más grande: 1/2 de la primera hoja o 1/4 de la segunda?", "1/2 de la primera hoja", "Al cortar la misma hoja en menos partes, cada parte es más grande."),
        ],
        "challenge": [
            arith("Una cinta de 12 cm se corta en 4 partes iguales. ¿Cuántos centímetros mide cada parte, que es 1/4 de la cinta?", "12//4", "Se reparte el largo en 4 partes iguales.", " cm"),
            ex("Doblas una hoja por la mitad y luego doblas otra vez por la mitad. Al abrirla, ¿en cuántas partes iguales quedó y qué fracción es cada una?", "En 4 partes iguales; cada una es 1/4", "Dos dobleces por la mitad hacen 2 × 2 = 4 partes iguales.", calc="2*2"),
        ],
    },
    context=[ex("Cuatro hermanos comparten una torta cortada en 4 partes iguales y cada uno toma una parte. ¿Qué fracción de la torta come cada uno?", "1/4 (un cuarto)", "Hay 4 partes iguales y cada uno toma 1.")],
    selfcheck=[
        ex("¿Cómo se lee la fracción 1/2?", "Un medio", "El 1 es la parte tomada y el 2, las partes iguales."),
        ex("¿Cuántas partes iguales tiene el entero en la fracción 3/4?", "4", "El número de abajo cuenta las partes iguales."),
        ex("¿Cómo se lee la fracción 1/3?", "Un tercio", "Es una de tres partes iguales."),
    ],
    open_task=task(
        "Con una hoja de papel, dobla y marca: una hoja en 2 partes iguales, otra en 4 partes iguales y otra en 3 partes iguales (para esta última puedes dibujar una tira y medirla con regla). Pinta una parte de cada una y escribe la fracción pintada.",
        "Hoja en 2 partes: pinto 1, es 1/2. Hoja en 4 partes: pinto 1, es 1/4. Tira de 12 cm en 3 partes de 4 cm: pinto 1, es 1/3. Comprobé que las partes son iguales doblando y midiendo.",
        ["las partes de cada hoja son iguales", "pinta una parte de cada una", "escribe 1/2, 1/4 y 1/3", "explica cómo comprobó que eran iguales"],
        ["tres hojas o tiras marcadas", "fracciones escritas", "explicación"],
        ["partes desiguales", "invertir numerador y denominador"],
        "Pide que superponga las partes para comprobar que son iguales. Reconoce que explique qué dice cada número.",
    ),
    reinforce="Corta o dobla una hoja en 2 y luego en 4 partes iguales. Pinta 3 partes y escribe qué fracción pintaste.",
    extend="Una persona dice que 1/3 de una cinta de 12 cm mide 6 cm. ¿Está bien? Haz el dibujo y explica.",
)

register(
    OA11, 2,
    materials=f"Lápiz y papel. {KEY}",
    use="Aprenderé a mostrar la misma fracción con objetos, dibujos, palabras y símbolos. Sirve para entender una fracción aunque se vea de distinta manera.",
    prior=["Sé que una fracción nace al repartir un entero en partes iguales.", "Sé qué dicen el numerador y el denominador."],
    explain=[
        "Una fracción puede mostrarse de cuatro maneras. Con objetos, como una cinta doblada. Con un dibujo, como ▮▮▯. Con palabras, como «dos tercios». Y con símbolos, como 2/3. Las cuatro dicen lo mismo.",
        "En un dibujo, primero cuenta todas las partes: eso es el denominador. Luego cuenta las partes pintadas: eso es el numerador. En ▮▮▯ hay 3 partes en total y 2 pintadas. Es 2/3.",
        "Para que todo esté bien, el entero debe ser el mismo y las partes deben ser iguales. Un dibujo con partes desiguales no representa una fracción.",
    ],
    vocab=[("representar", "mostrar algo con objetos, dibujos o símbolos"), ("dibujo", "forma de mostrar una fracción con partes pintadas"), ("símbolo", "forma escrita con números, como 3/4"), ("pintada", "parte que se toma del entero"), ("sin pintar", "parte que no se toma del entero")],
    worked=[
        {"title": "Del dibujo al símbolo", "problem": f"Mira el dibujo ▮▯▯▯. ¿Qué fracción está pintada? {KEY}", "steps": ["Cuento todas las partes: 4. Ese es el denominador.", "Cuento las pintadas: 1. Ese es el numerador.", "La fracción es 1/4."], "answer": "1/4, un cuarto"},
        {"title": "De las palabras al dibujo", "problem": "Dibuja «tres cuartos» con ▮ y ▯.", "steps": ["Cuartos significa 4 partes iguales en total.", "Tres cuartos significa pintar 3 de ellas.", "Dibujo ▮▮▮▯."], "answer": "▮▮▮▯"},
    ],
    mistakes=[
        {"wrong": "Ver ▮▯▯ y escribir 1/2 porque hay una parte pintada y otra «sin pintar».", "why": "Se cuentan mal las partes del entero.", "fix": "Hay 3 partes en total, una pintada: 1/3."},
        {"wrong": "Mirar ▮▮▯ y escribir 3/2.", "why": "Se pone el número de partes de arriba y las pintadas abajo.", "fix": "Arriba van las pintadas (2) y abajo el total (3): 2/3."},
    ],
    tiers={
        "recovery": [
            ex(f"En el dibujo ▮▯▯▯ hay una parte pintada. ¿Qué fracción está pintada? {KEY}", "1/4", "Hay 1 parte pintada de 4 partes iguales."),
            ex(f"En el dibujo ▮▮▯, ¿qué fracción está pintada? {KEY}", "2/3", "Hay 2 partes pintadas de 3 partes iguales."),
            ex(f"En el dibujo ▮▯, ¿qué fracción está pintada? {KEY}", "1/2", "Hay 1 parte pintada de 2 partes iguales."),
        ],
        "understand": [
            ex("¿Cuál es el símbolo de la fracción «tres cuartos»?", "3/4", "Cuartos son 4 partes y tres cuartos toma 3 de ellas."),
            ex(f"¿Cuál dibujo muestra 2/3: ▮▮▯ o ▮▯▯? {KEY}", "▮▮▯", "Tiene 2 partes pintadas de 3."),
            ex("Un dibujo tiene 4 partes iguales y 3 están pintadas. ¿Cómo se lee la fracción pintada?", "Tres cuartos", "Cuartos por las 4 partes y tres por las pintadas."),
        ],
        "apply": [
            ex(f"Con ▮ y ▯, dibuja la fracción 3/4. {KEY}", "▮▮▮▯ (tres ▮ y un ▯, en cualquier orden)", "Hay 4 partes en total y 3 pintadas."),
            ex("Una barra se divide en 4 partes iguales y se pinta 1. Escribe la fracción en palabras.", "Un cuarto", "Se toma 1 de 4 partes iguales."),
            ex("Escribe con símbolos la fracción «dos tercios».", "2/3", "Tercios son 3 partes iguales y se toman 2."),
        ],
        "reason": [
            ex(f"Mateo mira ▮▯▯ y escribe 1/2. ¿Cuál es su error y cuál es la fracción correcta? {KEY}", "Contó mal el total; hay 3 partes y la fracción es 1/3", "El denominador es el total de partes iguales, que es 3."),
            ex(f"Julia mira dos dibujos, ▮▮▮▯ y ▮▮▯, y dice que muestran la misma fracción porque en los dos aparece un 3. ¿Qué fracción muestra cada uno? {KEY}", "El primero 3/4 y el segundo 2/3", "En el primero hay 3 pintadas de 4; en el segundo, 2 de 3."),
        ],
        "challenge": [
            ex(f"Dibuja una barra de 3 partes iguales con ▮ y ▯ en la que la parte pintada sea 2/3. Luego escribe la fracción que quedó sin pintar. {KEY}", "▮▮▯ y la parte sin pintar es 1/3", "Si 2 de 3 partes están pintadas, queda 1 sin pintar."),
            ex("Una barra está pintada en 3/4. ¿Qué fracción falta por pintar?", "1/4", "El entero tiene 4 partes; si 3 están pintadas, falta 1."),
        ],
    },
    context=[ex("El patio de una escuela se divide en 4 zonas iguales. En 3 de ellas hay juegos. ¿Qué fracción del patio tiene juegos? Escríbela con símbolos.", "3/4", "Hay 4 zonas iguales y 3 tienen juegos.")],
    selfcheck=[
        ex("¿Cómo se lee la fracción 2/3?", "Dos tercios", "Tercios por las 3 partes y dos por las tomadas."),
        ex(f"Escribe con símbolos la parte pintada de ▮▮▮▯. {KEY}", "3/4", "Hay 3 pintadas de 4 partes iguales."),
        ex("En la fracción 3/4, ¿el número 3 dice cuántas partes iguales tiene el entero o cuántas se toman?", "Cuántas se toman", "El número de arriba cuenta las partes tomadas."),
    ],
    open_task=task(
        "Representa la fracción 2/3 de cuatro maneras: con una tira de papel doblada en 3 partes iguales y 2 pintadas, con un dibujo hecho con ▮ y ▯, con palabras y con símbolos. Luego explica qué dice cada número.",
        "Tira doblada en 3 partes, 2 pintadas. Dibujo: ▮▮▯. Palabras: dos tercios. Símbolo: 2/3. El 3 dice que el entero tiene 3 partes iguales; el 2 dice que se toman 2.",
        ["usa las cuatro representaciones", "mantiene el mismo entero y partes iguales", "explica el numerador y el denominador"],
        ["tira de papel", "dibujo", "palabras y símbolo"],
        ["partes desiguales", "invertir numerador y denominador"],
        "Pide que muestre con el dedo las partes pintadas y las totales. Reconoce que explique ambos números.",
    ),
    reinforce="Elige 3/4 y represéntala con un dibujo, con una tira de papel doblada y con palabras.",
    extend="Dibuja con ▮ y ▯ las fracciones 1/3, 2/3 y 3/4 y escribe cómo se lee cada una.",
)

register(
    OA11, 3,
    materials="Lápiz, regla y una tira de papel de 12 cm. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a ubicar fracciones entre 0 y 1 en una recta. Sirve para ver que una fracción es un número, menor que 1 y mayor que 0.",
    prior=["Sé qué es una fracción y qué dicen sus dos números.", "Sé ubicar números en una recta."],
    explain=[
        "Las fracciones que usamos aquí están entre 0 y 1. Imagina una recta que empieza en 0 y termina en 1. El 0 y el 1 son los extremos. Todo el espacio entre ellos es un entero.",
        "Para ubicar una fracción, divide ese espacio en partes iguales. Si el denominador es 4, haces 4 intervalos iguales. Las marcas, de izquierda a derecha, son 1/4, la mitad (que es 1/2), 3/4 y por último el 1. Cuentas desde el 0 tantos intervalos como diga el numerador.",
        "Mientras más intervalos cuentes desde el 0, más lejos del 0 estás. Por eso 1/3 está antes de 2/3, y 2/3 llega antes que el 1. Los intervalos siempre deben ser del mismo largo.",
    ],
    vocab=[("recta numérica", "línea donde se ubican números en orden"), ("extremo", "punto donde empieza o termina la recta: aquí 0 y 1"), ("intervalo", "espacio entre dos marcas seguidas"), ("marca", "raya que señala un punto de la recta"), ("mitad", "una de dos partes iguales, o sea 1/2")],
    worked=[
        {"title": "Ubicar tercios", "problem": "Una recta del 0 al 1 está dividida en 3 intervalos iguales, con marcas P y Q de izquierda a derecha. ¿Qué fracción es cada marca?", "steps": ["Hay 3 intervalos iguales, así que el denominador es 3.", "P está a 1 intervalo del 0: es 1/3.", "Q está a 2 intervalos del 0: es 2/3."], "answer": "P es 1/3 y Q es 2/3"},
        {"title": "Ubicar tres cuartos", "problem": "Quieres ubicar 3/4 entre 0 y 1. ¿Cómo lo haces?", "steps": ["Divido el espacio entre 0 y 1 en 4 intervalos iguales.", "Parto del 0 y cuento 3 intervalos.", "Ahí marco 3/4, cerca del 1."], "answer": "Cuento 3 de 4 intervalos desde el 0"},
    ],
    mistakes=[
        {"wrong": "Dividir la recta entre 0 y 1 en tres partes de distinto largo y marcar 1/3 en la primera marca.", "why": "Los intervalos no son iguales.", "fix": "Mide para que los tres intervalos tengan el mismo largo."},
        {"wrong": "Poner 3/4 más cerca del 0 que 1/4.", "why": "Se confunde el orden de las fracciones sobre la recta.", "fix": "3/4 está a 3 intervalos del 0 y 1/4 a solo 1: 3/4 está más lejos."},
    ],
    tiers={
        "recovery": [
            ex("En una recta del 0 al 1 se marca justo el punto del medio. ¿Qué fracción es?", "1/2", "La mitad del entero es un medio."),
            ex("Una recta del 0 al 1 está dividida en 3 intervalos iguales, con marcas P y Q de izquierda a derecha. ¿Qué fracción es la marca P?", "1/3", "P está a 1 intervalo del 0 de un total de 3."),
            ex("En esa misma recta de 3 intervalos, ¿qué fracción es la marca Q?", "2/3", "Q está a 2 intervalos del 0 de un total de 3."),
        ],
        "understand": [
            ex("¿Qué número está en el extremo derecho de la recta, donde termina el entero?", "1", "La recta entre 0 y 1 muestra un entero."),
            ex("En una recta del 0 al 1, ¿la fracción 1/4 está más cerca del 0 o del 1?", "Del 0", "Solo avanza 1 intervalo de 4 desde el 0."),
            ex("En una recta del 0 al 1, ¿la fracción 3/4 está más cerca del 0 o del 1?", "Del 1", "Avanza 3 de 4 intervalos y le falta solo 1."),
        ],
        "apply": [
            ex("Una recta del 0 al 1 tiene 4 intervalos iguales, con marcas A, B y C de izquierda a derecha. ¿Qué fracción es la marca C?", "3/4", "C está a 3 intervalos del 0 de un total de 4."),
            ex("Para ubicar 2/3 entre 0 y 1, ¿en cuántos intervalos iguales divides la recta y cuántos intervalos cuentas desde el 0?", "En 3 intervalos; cuentas 2", "El denominador dice cuántos intervalos y el numerador cuántos se cuentan."),
            ex("En una recta del 0 al 1 con 4 intervalos iguales, el punto del medio es 1/2. Ordena de menor a mayor 3/4, 1/4 y 1/2.", "1/4, 1/2, 3/4", "Están más lejos del 0 mientras más intervalos se cuentan."),
        ],
        "reason": [
            ex("Luis dibujó una recta del 0 al 1 con 3 intervalos: el primero de 2 cm, el segundo de 4 cm y el tercero de 6 cm. Marcó 1/3 al final del primero. ¿Está bien?", "No; los intervalos deben ser iguales", "Si los intervalos son distintos, la marca no es 1/3."),
            ex("Ema dice que 2/3 está después de 1/3 y antes del 1. ¿Tiene razón?", "Sí; 2 intervalos son más que 1 y menos que 3", "2/3 está a 2 de 3 intervalos desde el 0."),
        ],
        "challenge": [
            ex("En una recta del 0 al 1 con 4 intervalos iguales, Sofía parte del 0 y avanza 3 intervalos. ¿En qué fracción llega y cuántos intervalos le faltan para llegar al 1?", "A 3/4; le falta 1 intervalo", "Avanzó 3 de 4 intervalos."),
            ex("Un caracol avanza por una recta del 0 al 1 con 3 intervalos iguales y está en 2/3. ¿Cuántos intervalos le faltan y qué fracción de la recta es eso?", "Le falta 1 intervalo, que es 1/3", "De 3 intervalos ya recorrió 2."),
        ],
    },
    context=[ex("Un camino a la escuela se muestra como una tira del 0 al 1 con 4 partes iguales. Rosa va en la marca 3, contada desde la casa (el 0). ¿Qué fracción del camino recorrió?", "3/4", "Recorrió 3 de las 4 partes iguales.")],
    selfcheck=[
        ex("¿Cuáles son los dos números extremos de la recta de un entero?", "0 y 1", "El entero va desde 0 hasta 1."),
        ex("En la recta del 0 al 1 con 3 intervalos y marcas P y Q de izquierda a derecha, ¿la fracción 2/3 es la marca P o la Q?", "La Q", "2/3 está a 2 intervalos del 0, en la segunda marca."),
        ex("Una recta del 0 al 1 tiene intervalos de 2 cm y 4 cm. ¿Son iguales los intervalos?", "No", "2 cm y 4 cm miden distinto, así que no sirve para fracciones."),
    ],
    open_task=task(
        "Con una tira de papel de 12 cm, dibuja una recta del 0 al 1. Márcala en 4 intervalos iguales de 3 cm cada uno y escribe sobre las marcas 0, 1/4, 1/2, 3/4 y 1. Luego haz otra tira del mismo largo y márcala en 3 intervalos de 4 cm con 0, 1/3, 2/3 y 1. Explica cómo sabes que los intervalos son iguales.",
        "Primera tira: marcas a los 3, 6 y 9 cm; 1/4, 1/2 y 3/4. Segunda tira: marcas a los 4 y 8 cm; 1/3 y 2/3. Medí cada intervalo con la regla: todos del mismo largo.",
        ["usa extremos 0 y 1", "intervalos iguales medidos", "escribe las fracciones sobre las marcas", "justifica con medidas"],
        ["dos tiras marcadas", "fracciones escritas", "explicación"],
        ["intervalos desiguales", "poner 0 fuera del extremo"],
        "Pide que mida cada intervalo. Reconoce que use la regla para justificar.",
    ),
    reinforce="Dibuja una recta de 8 cm del 0 al 1 y márcala en 2 partes iguales. Escribe 1/2 en la marca del medio.",
    extend="En una recta del 0 al 1 con 4 intervalos iguales, ubica 1/4 y 3/4 y escribe cuánto mide cada intervalo si toda la recta mide 20 cm.",
)

register(
    OA11, 4,
    materials=f"Lápiz y papel. {KEY}",
    use="Aprenderé a elegir y usar fracciones en situaciones de reparto y a comparar fracciones del mismo denominador. Sirve para decir quién comió más o cuánto queda.",
    prior=["Sé representar 1/4, 1/3, 1/2, 2/3 y 3/4.", "Sé ubicarlas entre 0 y 1."],
    explain=[
        "Usamos fracciones cuando repartimos un entero en partes iguales: una torta, una cinta, una pared que se pinta. No se usan para contar objetos sueltos, como 6 manzanas. Primero identifica el entero y revisa que las partes sean iguales.",
        "Para comparar fracciones con el mismo denominador, mira solo el numerador. Si dos fracciones tienen el mismo número abajo, sus partes son del mismo tamaño. Entonces la que toma más partes es mayor. Por eso 3/4 es mayor que 1/4, y 2/3 es mayor que 1/3.",
        "Solo se pueden comparar fracciones de enteros iguales. Un cuarto de una pizza grande no es igual a un cuarto de una pizza chica. Siempre pregunta: ¿es el mismo entero?",
    ],
    vocab=[("mismo denominador", "fracciones con el mismo número abajo"), ("comparar", "decir cuál es mayor, menor o igual"), ("mayor que", "más grande que"), ("menor que", "más pequeño que"), ("situación", "caso de la vida donde se usa una fracción")],
    worked=[
        {"title": "Comparar fracciones del mismo entero", "problem": "Una torta se corta en 4 partes iguales. Ana come 1 parte y Beto come 3 partes. ¿Quién comió más y qué fracciones comieron?", "steps": ["El entero es la misma torta y tiene 4 partes iguales.", "Ana comió 1/4 y Beto 3/4.", "Los denominadores son iguales; 3 partes son más que 1 parte."], "answer": "Beto comió más: 3/4 es mayor que 1/4"},
        {"title": "Elegir la fracción para una situación", "problem": "Una pared tiene 3 franjas iguales y pintas 1. ¿Qué fracción pintaste y cuál falta?", "steps": ["El entero es la pared, con 3 franjas iguales.", "Pintaste 1, o sea 1/3.", "Faltan 2 franjas, o sea 2/3."], "answer": "Pintaste 1/3 y faltan 2/3"},
    ],
    mistakes=[
        {"wrong": "Decir que 1/4 es mayor que 3/4 porque «el 4 está en los dos».", "why": "Se mira el denominador, que es igual en las dos, y no el numerador, que es el que decide.", "fix": "Con el mismo denominador, la fracción con el mayor numerador es mayor: 3/4 es mayor."},
        {"wrong": "Comparar un cuarto de una pizza grande con un cuarto de una pizza chica como si fueran lo mismo.", "why": "Los enteros son distintos.", "fix": "Solo se comparan fracciones del mismo entero."},
    ],
    tiers={
        "recovery": [
            ex("Una torta se corta en 4 partes iguales. Tú comes 1 parte y tu amigo come 3. ¿Quién comió más?", "Tu amigo", "3 partes son más que 1 parte del mismo entero."),
            ex("¿Cuál es mayor, 2/3 o 1/3?", "2/3", "Las partes son iguales y 2 son más que 1."),
            ex("¿Cuál es menor, 3/4 o 1/4?", "1/4", "Las partes son iguales y 1 es menos que 3."),
        ],
        "understand": [
            ex("¿Por qué puedo comparar 1/4 y 3/4 mirando solo el número de arriba?", "Porque tienen el mismo denominador, así que las partes son del mismo tamaño", "Cuando las partes son iguales, gana quien toma más."),
            ex("¿En cuál situación sirve una fracción: (a) contar 6 manzanas sueltas o (b) repartir una pizza en partes iguales?", "En (b)", "Las fracciones muestran partes iguales de un entero."),
            ex("Se pintó 1 de 2 partes iguales de una pared. ¿Qué fracción se pintó?", "1/2", "Se tomó 1 de 2 partes iguales."),
        ],
        "apply": [
            ex("Una cinta entera se divide en 3 partes iguales. Ana usa 2 partes y Beto usa 1 parte. ¿Qué fracción usó cada uno?", "Ana usó 2/3 y Beto 1/3", "Hay 3 partes iguales y cada uno toma las suyas."),
            ex("Una pizza se corta en 4 partes iguales y quedan 3 partes sin comer. ¿Qué fracción de la pizza se comió?", "1/4", "Se comió la parte que falta, 1 de las 4."),
            ex("Dos jarras iguales tienen jugo: la primera tiene 1/3 de jarra y la segunda 2/3 de jarra. ¿En cuál hay más jugo?", "En la segunda", "Con el mismo entero, 2/3 es mayor que 1/3."),
        ],
        "reason": [
            ex("Una pizza grande y una chica se cortan, cada una, en 4 partes iguales. ¿Una parte de la grande es igual a una parte de la chica?", "No; los enteros son distintos", "Un cuarto del entero grande es más grande que un cuarto del entero chico."),
            ex("Pablo dice que 1/4 es mayor que 3/4 porque en 1/4 «las partes son más grandes». ¿Qué error comete?", "Las partes son del mismo tamaño; 3 partes son más que 1", "Con el mismo denominador, las partes son iguales."),
        ],
        "challenge": [
            ex("Ana, Beto y Carla comen un trozo cada uno de una barra de 4 trozos iguales. ¿Qué fracción de la barra queda?", "1/4", "Se comieron 3 de 4 trozos y queda 1."),
            ex("Una cinta entera se corta en 3 partes iguales. Pones 2 partes en una caja y 1 parte en otra. ¿En qué caja hay más cinta y qué fracción es?", "En la primera, con 2/3", "2 partes iguales son más que 1."),
        ],
    },
    context=[ex("En una fiesta, una pizza se corta en 4 partes iguales y se sirven 3. ¿Qué fracción se sirvió y qué fracción sobró?", "Se sirvió 3/4 y sobró 1/4", "De 4 partes iguales, se sirven 3 y sobra 1.")],
    selfcheck=[
        ex("Entre 3/4 y 1/4, ¿cuál es mayor?", "3/4", "Las partes son iguales y 3 es mayor que 1."),
        ex("Para comparar dos fracciones con el mismo denominador, ¿qué número miras?", "El numerador", "El numerador dice cuántas partes iguales se toman."),
        ex("¿Cuándo no se pueden comparar dos fracciones?", "Cuando son de enteros distintos", "Las partes de enteros distintos no son del mismo tamaño."),
    ],
    open_task=task(
        "Elige una situación: A) una barra de queso cortada en 4 partes iguales, donde Ana toma 1 y Luis toma 3; B) una cinta cortada en 3 partes iguales, donde Eva usa 1 y Pía usa 2. Escribe las fracciones, di quién tiene más y por qué puedes compararlas.",
        "Situación B: Eva usa 1/3 y Pía usa 2/3. Pía tiene más porque las dos fracciones tienen el mismo denominador y es el mismo entero: 2 partes son más que 1.",
        ["identifica el entero", "escribe las dos fracciones", "dice quién tiene más", "justifica con el mismo entero y denominador"],
        ["fracciones escritas", "comparación", "justificación"],
        ["comparar enteros distintos", "decir que gana el denominador"],
        "Pide que diga cuál es el entero y cuántas partes iguales tiene. Reconoce que explique por qué se puede comparar.",
    ),
    reinforce="Corta una tira de papel en 4 partes iguales. Pinta 1 de rojo y 3 de azul y escribe las dos fracciones.",
    extend="Escribe una situación de tu casa en la que se use 1/2 de algo y otra en la que se use 3/4. Haz un dibujo de cada una.",
)

register(
    OA11, 5,
    materials=f"Lápiz, regla y papel. {KEY}",
    use="Aprenderé a juntar todo lo que sé de fracciones: representar, ubicar, comparar, explicar y comprobar. Sirve para resolver un problema de fracciones y estar seguro de la respuesta.",
    prior=["Sé que una fracción es una parte de un entero con partes iguales.", "Sé representarla, ubicarla entre 0 y 1 y compararla con otra de igual denominador."],
    explain=[
        "Un buen desafío de fracciones tiene cuatro pasos. Primero, identifica el entero y revisa que las partes sean iguales. Segundo, cuenta las partes totales (denominador) y las partes que se toman (numerador).",
        "Tercero, representa la fracción con un dibujo o una recta del 0 al 1. Si el problema compara dos fracciones, mira que tengan el mismo denominador y el mismo entero. Cuarto, comprueba tu respuesta en el contexto: ¿tiene sentido que sea menor que 1?",
        "Para explicar, usa palabras claras: «el entero tiene 4 partes iguales y yo tomo 3, por eso es 3/4». Una explicación completa nombra el entero, el denominador y el numerador.",
    ],
    vocab=[("representar", "mostrar una fracción con un dibujo, objeto o símbolo"), ("comprobar", "revisar que la respuesta tiene sentido"), ("explicar", "decir con palabras cómo se llegó a una respuesta"), ("entero", "la cosa completa que se reparte"), ("fracción", "parte de un entero dividido en partes iguales")],
    worked=[
        {"title": "Representar y comprobar", "problem": "Una cinta se divide en 4 partes iguales y se cortan 3. ¿Qué fracción se cortó y qué fracción queda?", "steps": ["El entero es la cinta, con 4 partes iguales.", "Se cortaron 3: son 3/4.", "Queda 1 parte: es 1/4.", "Compruebo: 3 partes y 1 parte suman las 4 partes del entero."], "answer": "Se cortaron 3/4 y queda 1/4"},
        {"title": "Comparar y justificar", "problem": f"Dos barras iguales. La primera es ▮▯▯, la segunda es ▮▮▯. ¿Cuál tiene más parte pintada? {KEY}", "steps": ["Las dos barras son iguales y tienen 3 partes iguales.", "La primera tiene 1/3 pintado y la segunda 2/3.", "Con el mismo denominador, 2 partes son más que 1."], "answer": "La segunda barra, con 2/3"},
    ],
    mistakes=[
        {"wrong": "Escribir 1/3 para un dibujo con 4 partes iguales y una pintada.", "why": "Se pone mal el denominador.", "fix": "Cuenta todas las partes del entero: son 4, así que es 1/4."},
        {"wrong": "Dar la respuesta «3/4» sin decir de qué entero.", "why": "La fracción no tiene un entero claro.", "fix": "Escribe «3/4 de la pizza» o «3/4 de la cinta»."},
    ],
    tiers={
        "recovery": [
            ex("Una barra se divide en 3 partes iguales y se come 1. ¿Qué fracción se comió?", "1/3", "Se toma 1 de 3 partes iguales."),
            ex(f"¿Qué fracción está pintada en ▮▮▮▯? {KEY}", "3/4", "Hay 3 partes pintadas de 4 iguales."),
            ex("¿Cómo se lee la fracción 2/3?", "Dos tercios", "Tercios por 3 partes y dos por las tomadas."),
        ],
        "understand": [
            ex("En la fracción 2/3, ¿qué dice el 3 y qué dice el 2?", "El 3 dice que hay 3 partes iguales y el 2 que se toman 2", "El denominador cuenta partes del entero y el numerador las tomadas."),
            ex("Una recta del 0 al 1 tiene 4 intervalos iguales. ¿Cuántos intervalos cuentas desde el 0 para ubicar 3/4?", "3", "El numerador dice cuántos intervalos se cuentan."),
            ex("¿Cuál es mayor, 1/3 o 2/3, si ambas son de la misma cinta?", "2/3", "Con el mismo denominador, gana el mayor numerador."),
        ],
        "apply": [
            ex("Una pizza se corta en 4 partes iguales y se sirven 3. ¿Qué fracción queda sin servir?", "1/4", "De 4 partes iguales, queda 1."),
            ex("Una tira de 12 cm del 0 al 1 se divide en 3 intervalos iguales. ¿A cuántos cm del 0 queda la marca 2/3?", "A 8 cm", "Cada intervalo mide 4 cm y 2 intervalos miden 8 cm.", calc="2*4"),
            ex("Ordena de menor a mayor 3/4, 1/4 y 1/2 sobre una recta del 0 al 1.", "1/4, 1/2, 3/4", "Mientras más lejos del 0, mayor la fracción."),
        ],
        "reason": [
            ex("Elisa dice que 3/4 de una pizza pequeña es más que 1/4 de una pizza gigante. ¿Se puede asegurar? Explica.", "No se puede asegurar; son enteros distintos", "Solo se comparan fracciones del mismo entero."),
            ex("Hugo dibujó una barra con 4 partes de distinto tamaño y pintó una. Dice que pintó 1/4. ¿Está bien?", "No; las partes deben ser iguales", "Sin partes iguales no se puede hablar de un cuarto."),
        ],
        "challenge": [
            ex("Una cinta entera se divide en 3 partes iguales. Pablo toma 1 parte y Ema toma otra parte. ¿Qué fracción de la cinta queda?", "1/3", "De 3 partes iguales se toman 2 y queda 1."),
            ex(f"Mira el dibujo ▮▮▯ y escribe la fracción que queda sin pintar. {KEY}", "1/3 (una sola parte sin pintar)", "En ▮▮▯ solo 1 de 3 partes está sin pintar."),
        ],
    },
    context=[ex("Un parque se divide en 3 zonas iguales. Una zona tiene árboles, otra juegos y otra canchas. ¿Qué fracción del parque tiene juegos?", "1/3", "Hay 3 zonas iguales y juegos en 1.")],
    selfcheck=[
        ex("¿Qué fracción es la mitad de un entero?", "1/2", "La mitad son 2 partes iguales, y se toma 1."),
        ex("En 3/4, ¿cuántas partes iguales tiene el entero?", "4", "El denominador cuenta las partes iguales."),
        ex("¿Cuál es menor: 1/4 o 3/4?", "1/4", "Con igual denominador, gana el menor numerador."),
    ],
    open_task=task(
        "Resuelve y explica: «Una cinta de 12 cm se divide en 4 partes iguales. Ana usa 3 partes y Beto usa 1 parte.» a) Escribe la fracción de cada uno. b) Dibuja la cinta con ▮ y ▯. c) Ubica 3/4 en una recta de 0 a 1. d) Explica quién usó más y cómo comprobaste.",
        "a) Ana usa 3/4 y Beto 1/4. b) ▮▮▮▯. c) Recta de 0 a 1 con 4 intervalos de 3 cm; 3/4 está a 9 cm del 0. d) Ana usó más porque son del mismo entero y 3 partes son más que 1. Comprobé: 3 partes y 1 parte son las 4 partes de la cinta.",
        ["usa partes iguales", "conecta el dibujo con el símbolo", "ubica 3/4 como número entre 0 y 1", "explica y comprueba"],
        ["fracciones escritas", "dibujo", "recta", "explicación"],
        ["partes desiguales", "invertir numerador y denominador"],
        "Pide que explique en voz alta usando entero, denominador y numerador. Reconoce la comprobación final.",
    ),
    reinforce="Dibuja una barra, divídela en 4 partes iguales y pinta 3. Escribe la fracción en palabras y en símbolos.",
    extend="Inventa una situación con fracciones de 2 o 3 partes iguales, resuélvela y comprueba con un dibujo.",
)
