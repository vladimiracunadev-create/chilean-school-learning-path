"""Student material for 5.º básico Matemática, OA 12 (adición y sustracción de decimales), OA 13 (problemas con fracciones y decimales) y OA 14 (reglas de sucesiones)."""
from __future__ import annotations

import ast
import operator
from decimal import Decimal

from student_lessons import arith, ex, register

OA12, OA13, OA14 = "MA05 OA 12", "MA05 OA 13", "MA05 OA 14"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, mat, use, prior, explain, vocab, worked, mist, R, C, A, Z, D, ctx, chk, open, reinforce, extend):
    """Registra una clase con una forma compacta (misma estructura que register)."""
    register(
        oa, n,
        materials=mat, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mist],
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=chk, open_task=task(*open), reinforce=reinforce, extend=extend,
    )


_DOPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv}


def _deval(expr):
    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return Decimal(repr(node.value))
        if isinstance(node, ast.BinOp) and type(node.op) in _DOPS:
            return _DOPS[type(node.op)](walk(node.left), walk(node.right))
        raise ValueError(expr)
    return walk(ast.parse(expr, mode="eval"))


def fmtd(value: Decimal, places: int | None = None) -> str:
    """Formato chileno: coma decimal y punto de miles; sin ceros de sobra salvo que se pidan."""
    if places is None:
        value = value.normalize()
        text = format(value, "f")
    else:
        text = format(value.quantize(Decimal(1).scaleb(-places)), "f")
    whole, _, frac = text.partition(".")
    sign = "-" if whole.startswith("-") else ""
    whole = whole.lstrip("-")
    if len(whole) > 3:
        whole = f"{int(whole):,}".replace(",", ".")
    return sign + whole + ("," + frac if frac else "")


def da(q, expr, why, unit="", places=None):
    """Ejercicio cerrado con decimales: la respuesta se calcula con Decimal, sin errores de coma flotante."""
    value = _deval(expr)
    shown = expr.replace("*", " × ").replace("/", " ÷ ").replace("-", " − ").replace("+", " + ")
    shown = " ".join(shown.split())
    for token in sorted(set(__import__("re").findall(r"\d+\.\d+", shown)), key=len, reverse=True):
        shown = shown.replace(token, token.replace(".", ","))
    result = fmtd(value, places)
    return ex(q, f"{result}{unit}", f"{why} Cálculo: {shown} = {result}.")


# ================================================================ OA 12
L(OA12, 1,
  mat="Lápiz y papel. Si quieres, dibuja una tabla con tres columnas llamadas décimas, centésimas y milésimas.",
  use="Aprenderé el valor de cada cifra de un número decimal hasta las milésimas. Sirve para leer medidas y precios con exactitud y para poder sumarlos y restarlos bien.",
  prior=["Sé el valor posicional de los números naturales (unidades, decenas, centenas).", "Sé que una décima es una parte de diez partes iguales."],
  explain=[
      "Un número decimal tiene una parte entera y una parte decimal, separadas por una coma. Después de la coma, la primera cifra son las décimas, la segunda las centésimas y la tercera las milésimas. En 3,457 hay 3 unidades, 4 décimas, 5 centésimas y 7 milésimas.",
      "Cada lugar vale 10 veces menos que el lugar de su izquierda. Por eso 1 unidad son 10 décimas, 100 centésimas o 1.000 milésimas; y 1 décima son 10 centésimas o 100 milésimas. Con esto puedes decir, por ejemplo, que 0,305 tiene 305 milésimas.",
      "El cero también ocupa un lugar. En 2,05 hay 0 décimas y 5 centésimas. Además, puedes agregar ceros al final de la parte decimal sin cambiar el valor: 0,5 = 0,50 = 0,500, porque 5 décimas son 50 centésimas.",
  ],
  vocab=[("décima", "una de las 10 partes iguales de una unidad; se escribe 0,1"), ("centésima", "una de las 100 partes iguales de una unidad; se escribe 0,01"), ("milésima", "una de las 1.000 partes iguales de una unidad; se escribe 0,001"), ("valor posicional", "lo que vale una cifra según el lugar en que está escrita")],
  worked=[
      ("Leer cada cifra", "Di cuánto vale cada cifra de 6,284.", ["La cifra antes de la coma es 6: son 6 unidades.", "Después de la coma: 2 décimas, 8 centésimas y 4 milésimas."], "6 unidades, 2 décimas, 8 centésimas y 4 milésimas"),
      ("Escribir con cero", "Escribe en cifras: 3 unidades y 8 milésimas.", ["Las unidades van antes de la coma: 3.", "No hay décimas ni centésimas, así que escribo ceros en esos lugares: 0 décimas y 0 centésimas, y luego 8 milésimas."], "3,008"),
  ],
  mist=[
      ("Escribir 3 unidades y 8 milésimas como 3,8.", "Se pone el 8 en las décimas porque es la primera cifra después de la coma.", "Las milésimas son el tercer lugar. Rellena con ceros: 3,008."),
      ("Pensar que 0,45 es mayor que 0,5 porque 45 es mayor que 5.", "Se miran los números después de la coma como si fueran naturales.", "Compara por lugar: 0,5 son 5 décimas, igual a 50 centésimas, y 0,45 son 45 centésimas."),
  ],
  R=[ex("En 6,284, ¿qué cifra está en el lugar de las décimas?", "2", "La primera cifra después de la coma son las décimas."),
     ex("En 6,284, ¿en qué lugar está la cifra 8?", "Centésimas", "Es la segunda cifra después de la coma."),
     ex("Escribe con cifras: 5 unidades y 3 décimas.", "5,3", "Las unidades van antes de la coma y las décimas después.")],
  C=[ex("En el número 4,073, ¿qué cifra está en el lugar de las décimas?", "0", "La primera cifra después de la coma es 0: hay 0 décimas."),
     ex("¿Cuánto vale la cifra 9 en el número 0,092?", "9 centésimas", "Después de la coma, el 9 es la segunda cifra: centésimas."),
     ex("¿Cuántas milésimas hay en el número 0,305?", "305", "3 décimas son 300 milésimas, y se suman las 5 milésimas.")],
  A=[ex("Escribe en cifras: 2 unidades, 0 décimas, 7 centésimas y 4 milésimas.", "2,074", "Se escribe cada lugar en orden; el cero ocupa las décimas."),
     ex("¿Cuánto vale la cifra 5 en el número 12,456?", "5 centésimas", "El 5 es la segunda cifra después de la coma."),
     ex("Escribe en cifras: 7 unidades y 6 milésimas.", "7,006", "Las décimas y centésimas valen cero; las 6 milésimas van en el tercer lugar.")],
  Z=[ex("Camila dice que 0,5 y 0,50 son números distintos porque el segundo tiene más cifras. ¿Tiene razón?", "No; los dos valen lo mismo", "5 décimas son lo mismo que 50 centésimas, así que 0,5 = 0,50."),
     ex("En los números 0,45 y 0,045, ¿en cuál vale más la cifra 4?", "En 0,45", "En 0,45 el 4 son 4 décimas; en 0,045 son 4 centésimas, que valen 10 veces menos.")],
  D=[ex("Un número tiene 2 unidades y su parte decimal vale exactamente 12 milésimas. ¿Cuál es el número?", "2,012", "12 milésimas son 0 décimas, 1 centésima y 2 milésimas, por eso se escribe 2,012."),
     ex("¿Cuántas centésimas hay en total en el número 3,4?", "340", "3 unidades son 300 centésimas y 4 décimas son 40 centésimas: 300 + 40.", calc="300+40")],
  ctx=[ex("Un paquete de arroz marca 2,046 kg en la balanza. ¿Qué cifra está en las centésimas?", "4", "Después de la coma están 0 décimas, 4 centésimas y 6 milésimas.")],
  chk=[ex("¿Cuántas milésimas son 0,7?", "700", "7 décimas son 70 centésimas y 700 milésimas."),
       ex("Escribe en cifras: 4 centésimas.", "0,04", "Las centésimas son el segundo lugar; antes hay 0 unidades y 0 décimas."),
       ex("¿En qué lugar está la cifra 6 en 9,126?", "Milésimas", "Es la tercera cifra después de la coma.")],
  open=("Con las cifras 4, 0, 6 y 9, usando cada una una vez, forma el número decimal más grande y el más pequeño que tengan una cifra antes de la coma y tres después. Puedes poner el 0 antes de la coma. Di qué vale cada cifra de cada número.",
        "El más grande es 9,640 (9 unidades, 6 décimas, 4 centésimas y 0 milésimas); el más pequeño es 0,469.",
        ["usa cada cifra una sola vez", "pone la cifra mayor en el lugar de mayor valor para el número grande", "dice el valor de cada cifra", "usa la coma en el lugar correcto"],
        ["dos números escritos", "valor de cada cifra"],
        ["poner la cifra mayor en las milésimas", "olvidar la coma o cambiarla de lugar"],
        "Pide que explique por qué el 9 va antes de la coma en el número grande. Reconoce que nombre bien los lugares."),
  reinforce="Escribe tu estatura o el peso de un objeto liviano con un decimal y di el valor de cada cifra.",
  extend="Escribe 1,2 con tres cifras decimales y explica por qué sigue valiendo lo mismo.")

L(OA12, 2,
  mat="Lápiz y papel cuadriculado o rayado. Dibuja una tabla de valor posicional: U , d c m (unidades, décimas, centésimas, milésimas).",
  use="Aprenderé a sumar números decimales alineando la coma. Sirve para sumar pesos, largos o tiempos con partes de unidad.",
  prior=["Sé el valor de cada cifra decimal hasta las milésimas.", "Sé sumar números naturales en forma vertical con reagrupación."],
  explain=[
      "Para sumar decimales, escribe un número bajo el otro de modo que las comas queden alineadas en una columna. Así cada valor posicional queda en su propia columna: décimas con décimas, centésimas con centésimas.",
      "Suma de derecha a izquierda, como con los naturales. Si una columna suma 10 o más, reagrupas: 10 centésimas pasan a ser 1 décima. La coma del resultado queda justo debajo de las otras comas.",
      "Si un número tiene menos cifras decimales, agrega ceros a su derecha para llenar columnas. Por ejemplo, 3,45 + 2,3 se escribe 3,45 + 2,30. Agregar ceros al final no cambia el valor.",
  ],
  vocab=[("alinear la coma", "escribir los números con las comas una bajo otra"), ("reagrupar", "cambiar 10 de un lugar por 1 del lugar siguiente a la izquierda"), ("sumando", "cada número que se suma"), ("columna", "cifras que están una bajo otra y valen lo mismo")],
  worked=[
      ("Suma con reagrupación", "Calcula 2,36 + 1,48.", ["Alineo las comas: 2,36 sobre 1,48.", "Centésimas: 6 + 8 = 14, escribo 4 y reagrupo 1 décima.", "Décimas: 3 + 4 + 1 = 8. Unidades: 2 + 1 = 3."], "3,84"),
      ("Sumar con distinto número de decimales", "Calcula 4,7 + 0,85.", ["Agrego un cero: 4,70 + 0,85.", "Centésimas: 0 + 5 = 5. Décimas: 7 + 8 = 15, escribo 5 y reagrupo 1 unidad.", "Unidades: 4 + 0 + 1 = 5."], "5,55"),
  ],
  mist=[
      ("Calcular 1,4 + 2,35 = 2,49.", "Se alinean los últimos dígitos y no las comas: se suma 14 + 235 sin pensar en el valor de cada lugar.", "Escribe 1,40 + 2,35 con las comas alineadas: da 3,75."),
      ("Olvidar la reagrupación: 0,8 + 0,9 = 0,17.", "Se escribe 17 décimas sin pasar 10 décimas a 1 unidad.", "10 décimas forman 1 unidad: 17 décimas son 1 unidad y 7 décimas, o sea 1,7."),
  ],
  R=[ex("Al sumar decimales en forma vertical, ¿qué debes alinear: las comas o el último dígito de cada número?", "Las comas", "Alinear las comas deja cada valor posicional en su columna."),
     da("¿Cuánto es 0,3 + 0,4?", "0.3+0.4", "3 décimas más 4 décimas son 7 décimas."),
     da("Resuelve 1,2 + 2,5.", "1.2+2.5", "Se suman unidades con unidades y décimas con décimas.")],
  C=[ex("Para sumar 3,45 + 2,3 en vertical, ¿qué número escribes en lugar de 2,3 para llenar las columnas?", "2,30", "Se agrega un cero a la derecha, sin cambiar su valor, para tener centésimas."),
     ex("Al sumar 2,8 + 1,5, las décimas dan 13. ¿Cómo queda escrito el resultado final?", "4,3", "13 décimas son 1 unidad y 3 décimas; con las 3 unidades de antes quedan 4 unidades y 3 décimas."),
     da("Calcula 0,64 + 0,28.", "0.64+0.28", "4 + 8 = 12 centésimas: se escribe 2 y se reagrupa 1 décima.")],
  A=[da("Suma en vertical 5,27 y 3,64.", "5.27+3.64", "Se suma por columnas reagrupando 11 centésimas."),
     da("Halla el resultado de 12,5 + 3,75.", "12.5+3.75", "Se escribe 12,50 + 3,75 para alinear las columnas."),
     da("Calcula 0,125 + 0,375.", "0.125+0.375", "125 + 375 milésimas son 500 milésimas, o sea 5 décimas.")],
  Z=[ex("Pedro calculó 1,4 + 2,35 y obtuvo 2,49. ¿Cuál es el resultado correcto?", "3,75", "Pedro no alineó las comas. Con 1,40 + 2,35 las columnas dan 3,75."),
     ex("¿Puede la suma 0,8 + 0,9 ser menor que 1? Responde sí o no y explica con las décimas.", "No; da 1,7", "8 décimas más 9 décimas son 17 décimas, que es más que 10 décimas (1 unidad).")],
  D=[da("Calcula 0,45 + 1,6 + 2,305.", "0.45+1.6+2.305", "Se escribe 0,450 + 1,600 + 2,305 y se suma por columnas."),
     da("Calcula 9,99 + 0,01.", "9.99+0.01", "1 centésima completa 10 centésimas y la reagrupación llega hasta las decenas.")],
  ctx=[da("Andrea compra 1,25 kg de manzanas y 0,75 kg de peras. ¿Cuántos kilogramos lleva en total?", "1.25+0.75", "Se suman los dos pesos alineando las comas.", " kg")],
  chk=[da("¿Cuánto da 3,6 + 2,7?", "3.6+2.7", "6 + 7 = 13 décimas, que son 1 unidad y 3 décimas."),
       da("Calcula 0,45 + 0,5.", "0.45+0.5", "Se escribe 0,50 y se suman las columnas."),
       ex("Al sumar 0,9 + 0,2 las décimas dan 11. ¿Cómo escribes el resultado?", "1,1", "11 décimas son 1 unidad y 1 décima.")],
  open=("Una cinta mide 1,35 m y otra mide 2,8 m. Las unes. Escribe la suma en forma vertical con las comas alineadas, rellena con ceros donde haga falta y escribe cuánto mide la cinta completa con su unidad.",
        "1,35 + 2,80 = 4,15. La cinta mide 4,15 m.",
        ["alinea las comas", "agrega el cero que falta", "reagrupa bien", "escribe la unidad (m)"],
        ["suma vertical escrita", "resultado con unidad"],
        ["alinear el último dígito en vez de la coma", "olvidar reagrupar"],
        "Pide que diga qué columna reagrupó y por qué. Reconoce el uso del cero para alinear."),
  reinforce="Suma 0,6 + 0,7 con dibujos de barras divididas en 10 partes y comprueba que obtienes 1,3.",
  extend="Inventa dos decimales con tres cifras decimales que sumen exactamente 1 y comprueba tu suma en forma vertical.")

L(OA12, 3,
  mat="Lápiz y papel. Una recta numérica dibujada de 0 a 5 puede ayudarte.",
  use="Aprenderé a restar números decimales eligiendo una buena estrategia y comprobando el resultado. Sirve para saber cuánto falta o cuánto sobra en una medida.",
  prior=["Sé sumar decimales alineando la coma.", "Sé que 1 unidad son 10 décimas, 100 centésimas y 1.000 milésimas."],
  explain=[
      "Para restar decimales también alineas las comas. Agrega ceros para que ambos números tengan la misma cantidad de cifras decimales, y resta de derecha a izquierda. Si una cifra de arriba es menor, pides prestado a la columna de la izquierda: 1 unidad se vuelve 10 décimas.",
      "Otra estrategia es sumar hacia arriba. Para 5 − 2,375, parte de 2,375 y suma hasta llegar a 5: de 2,375 a 3 faltan 0,625, y de 3 a 5 faltan 2. En total son 2,625.",
      "Antes de calcular, estima redondeando a números enteros: 7,9 − 3,1 es cercano a 8 − 3 = 5. Después comprueba con la operación inversa: si 5,2 − 1,87 = 3,33, entonces 3,33 + 1,87 debe dar 5,2.",
  ],
  vocab=[("minuendo", "el número del que se resta; es el primero"), ("sustraendo", "el número que se resta; es el segundo"), ("estimar", "calcular un valor cercano, redondeando los números"), ("operación inversa", "operación que deshace a otra: la suma deshace la resta")],
  worked=[
      ("Restar con reagrupación", "Calcula 6,3 − 2,8.", ["Alineo: 6,3 − 2,8. En las décimas, 3 es menor que 8.", "Pido 1 unidad prestada: 6 pasa a 5 y 3 décimas pasan a 13 décimas.", "13 − 8 = 5 décimas; 5 − 2 = 3 unidades."], "3,5"),
      ("Restar con ceros agregados", "Calcula 4,2 − 1,75.", ["Escribo 4,20 − 1,75 para alinear las columnas.", "Centésimas: 0 es menor que 5; pido prestado y queda 10 − 5 = 5. Décimas: 1 − 7 no se puede, pido prestado: 11 − 7 = 4. Unidades: 3 − 1 = 2."], "2,45"),
  ],
  mist=[
      ("Restar 5,20 − 1,87 como 4,67.", "En cada columna se resta el dígito menor del mayor, sin importar cuál está arriba.", "Si el de arriba es menor, hay que pedir prestado. Resultado correcto: 3,33."),
      ("Calcular 5 − 2,4 como 3,4.", "Se resta 5 − 2 = 3 y se copia el 4, sin alinear las comas ni escribir 5,0.", "Escribe 5,0 − 2,4 con las comas alineadas: da 2,6."),
  ],
  R=[da("Calcula 0,9 − 0,4.", "0.9-0.4", "9 décimas menos 4 décimas son 5 décimas."),
     da("Calcula 3,8 − 1,5.", "3.8-1.5", "Se restan décimas con décimas y unidades con unidades."),
     ex("Para restar 2,4 de 5, ¿cómo escribes el 5 para alinear las columnas?", "5,0", "Se agrega la coma y un cero en las décimas.")],
  C=[da("Calcula 6,3 − 2,8.", "6.3-2.8", "Se pide prestada 1 unidad para restar 8 décimas."),
     ex("Para restar 4,2 − 1,75, ¿cómo escribes el 4,2 para tener las mismas cifras decimales?", "4,20", "Se agrega un cero a la derecha para tener centésimas."),
     ex("Estima 9,8 − 4,2 redondeando cada número al entero más cercano. ¿Cuánto da la estimación?", "6", "9,8 se redondea a 10 y 4,2 a 4; 10 − 4 = 6.", calc="10-4")],
  A=[da("Calcula 8,05 − 3,6.", "8.05-3.6", "Se escribe 8,05 − 3,60 y se resta por columnas."),
     da("Calcula 10 − 4,375.", "10-4.375", "Se escribe 10,000 − 4,375 y se pide prestado en cadena."),
     da("Calcula 0,5 − 0,125.", "0.5-0.125", "500 milésimas menos 125 milésimas son 375 milésimas.")],
  Z=[ex("Tomás obtuvo 4,67 para 5,2 − 1,87 restando en cada columna el dígito menor del mayor. ¿Cuál es el resultado correcto?", "3,33", "Con 5,20 − 1,87 hay que pedir prestado, no restar al revés. Se comprueba: 3,33 + 1,87 = 5,20."),
     da("¿Cuánto hay que sumar a 2,375 para llegar a 5?", "5-2.375", "Esa diferencia es lo que falta, igual que la resta 5 − 2,375.")],
  D=[da("Una cinta mide 3,5 m. Se cortan primero 0,85 m y después 0,9 m. ¿Cuánto mide lo que queda?", "3.5-0.85-0.9", "Se restan las dos partes cortadas, una tras otra.", " m"),
     ex("¿Cuál resultado es mayor: 3,2 − 1,95 o 2,1 − 0,9?", "3,2 − 1,95", "3,2 − 1,95 = 1,25 y 2,1 − 0,9 = 1,2; 1,25 es mayor que 1,2.")],
  ctx=[da("Una jarra tiene 2 L de jugo. Se sirven dos vasos: uno de 0,75 L y otro de 0,6 L. ¿Cuántos litros quedan en la jarra?", "2-0.75-0.6", "Se restan los dos vasos servidos al total de la jarra.", " L")],
  chk=[da("Calcula 7,5 − 2,8.", "7.5-2.8", "Se pide prestado para restar 8 décimas."),
       da("Calcula 1 − 0,36.", "1-0.36", "1,00 − 0,36 se resuelve pidiendo prestado en las dos columnas."),
       ex("Comprueba: si 5,2 − 1,87 = 3,33, ¿qué suma debe dar 5,2?", "3,33 + 1,87", "La suma deshace la resta: resultado más sustraendo da el minuendo.")],
  open=("Una cuerda mide 5 m. Usas 2,375 m para un trabajo. Calcula cuánto queda con la resta en vertical y compruébalo con una suma. Escribe una estimación antes de calcular.",
        "Estimo 5 − 2 = 3. Resta: 5,000 − 2,375 = 2,625 m. Comprobación: 2,625 + 2,375 = 5,000.",
        ["escribe una estimación antes", "alinea comas y agrega ceros", "resta con préstamo", "comprueba con una suma"],
        ["estimación", "resta vertical", "comprobación con suma"],
        ["restar al revés en una columna", "no agregar ceros"],
        "Pide que compare la estimación con el resultado y diga si es razonable. Reconoce la comprobación."),
  reinforce="Resta 1 − 0,4 y 1 − 0,04 usando una barra dividida en 10 y en 100 partes.",
  extend="Explica por qué 1 − 0,001 da 0,999 sin hacer la resta vertical.")

L(OA12, 4,
  mat="Lápiz y papel. Ten a mano tu tabla de valor posicional.",
  use="Aprenderé a resolver sumas y restas de decimales en casos nuevos: con distinta cantidad de cifras, con varios términos y con números que faltan. Sirve para revisar cuentas de medidas y de datos.",
  prior=["Sé sumar y restar decimales alineando las comas.", "Sé estimar y comprobar con la operación inversa."],
  explain=[
      "Cuando hay varias operaciones, resuelve primero lo que está entre paréntesis y luego sigue de izquierda a derecha. Por ejemplo, 6 − (1,5 + 2,25) primero suma 3,75 y después resta: 6 − 3,75 = 2,25.",
      "Para buscar un número que falta, usa la operación inversa. En 9 − ___ = 4,125, el número que falta es 9 − 4,125 = 4,875. En ___ + 2,5 = 7,1, falta 7,1 − 2,5 = 4,6.",
      "Siempre revisa si tu resultado es razonable: estima con números redondeados o comprueba con la operación inversa. Si el resultado de una resta es mayor que el número inicial, hay un error.",
  ],
  vocab=[("paréntesis", "signos ( ) que indican qué operación se hace primero"), ("término que falta", "número que no conocemos y que buscamos con la operación inversa"), ("razonable", "que tiene sentido y está cerca de lo esperado"), ("comprobar", "revisar un resultado con otra operación o con una estimación")],
  worked=[
      ("Operaciones combinadas", "Calcula 3,25 + 4,8 − 2,05.", ["Voy de izquierda a derecha: 3,25 + 4,80 = 8,05.", "Luego resto: 8,05 − 2,05 = 6,00."], "6"),
      ("Número que falta", "¿Qué número falta en 9 − ___ = 4,125?", ["Para hallar el sustraendo, resto el resultado al minuendo: 9 − 4,125.", "Escribo 9,000 − 4,125 = 4,875. Comprobación: 4,875 + 4,125 = 9."], "4,875"),
  ],
  mist=[
      ("Calcular 6 − (1,5 + 2,25) como 6 − 1,5 + 2,25 = 6,75.", "Se ignoran los paréntesis y se suma lo que había que restar.", "Primero el paréntesis: 1,5 + 2,25 = 3,75 y luego 6 − 3,75 = 2,25."),
      ("Decir que 7,375 − 7,3 es 0,75.", "Se resta 375 − 3 sin alinear los lugares.", "7,375 − 7,300 = 0,075, que son 75 milésimas."),
  ],
  R=[ex("Para comprobar que 4,6 − 1,9 = 2,7, ¿qué suma haces y cuánto debe dar?", "2,7 + 1,9 = 4,6", "La suma de la diferencia y el sustraendo vuelve al minuendo."),
     da("Calcula 1,5 + 0,25.", "1.5+0.25", "Se escribe 1,50 + 0,25 para alinear."),
     da("Calcula 3,4 − 0,6.", "3.4-0.6", "Se pide prestado para restar 6 décimas.")],
  C=[da("Calcula 0,4 + 0,35 − 0,25.", "0.4+0.35-0.25", "Primero se suma 0,4 + 0,35 y luego se resta 0,25."),
     da("Calcula 8 − (2,5 + 1,75).", "8-(2.5+1.75)", "Se resuelve primero el paréntesis."),
     ex("Estima 6,95 + 2,1 redondeando cada sumando al entero más cercano. ¿Cuánto da?", "9", "6,95 se redondea a 7 y 2,1 a 2; 7 + 2 = 9.", calc="7+2")],
  A=[da("Calcula 12,408 + 5,59.", "12.408+5.59", "Se escribe 5,590 para alinear las milésimas."),
     da("Calcula 20,1 − 7,255.", "20.1-7.255", "Se escribe 20,100 − 7,255 y se pide prestado."),
     da("Calcula 5,75 + 3,6 − 2,35.", "5.75+3.6-2.35", "Se resuelve de izquierda a derecha.")],
  Z=[ex("A 0,999 le faltan algunas milésimas para completar 1 unidad. ¿Cuántas milésimas faltan?", "1", "1 es 1.000 milésimas y 0,999 son 999 milésimas."),
     da("Calcula 1 − 0,001 y explica que no puede ser mayor que 1.", "1-0.001", "Restar algo positivo siempre deja un número menor que el inicial.")],
  D=[da("Completa: 8 − ___ = 3,625.", "8-3.625", "El número que falta se halla restando el resultado al minuendo."),
     da("¿Cuánto más es 4,215 que 4,2?", "4.215-4.2", "Se alinean 4,215 y 4,200 y se restan; son 15 milésimas.")],
  ctx=[da("En una ciudad llovió 12,4 mm el lunes, 8,75 mm el martes y 15,2 mm el miércoles. ¿Cuántos milímetros llovió en los tres días?", "12.4+8.75+15.2", "Se suman tres medidas alineando las comas.", " mm")],
  chk=[da("Calcula 2,5 + 1,75 − 1,25.", "2.5+1.75-1.25", "Se suma primero y luego se resta."),
       da("¿Qué número falta? ___ + 3,4 = 8,2", "8.2-3.4", "Se resta el sumando conocido al total."),
       ex("En una resta el resultado es 8,2 y el minuendo es 5,9. ¿Es posible? Responde sí o no.", "No", "El resultado de una resta no puede ser mayor que el minuendo si se resta un número positivo.")],
  open=("Cuatro amigos corren distintos tramos: 1,25 km, 0,8 km, 2,125 km y 0,5 km. Calcula cuántos km corrieron en total y cuánto falta o sobra para llegar a 5 km. Escribe una estimación antes y una comprobación después.",
        "Estimo 1 + 1 + 2 + 1 = 5. Total: 1,25 + 0,8 + 2,125 + 0,5 = 4,675 km. Faltan 5 − 4,675 = 0,325 km para 5 km.",
        ["estima antes", "suma con comas alineadas", "resta el total a 5 km", "comprueba con una operación inversa"],
        ["suma", "resta", "comprobación"],
        ["no agregar ceros", "restar al revés"],
        "Pide que explique cómo supo que el resultado era razonable. Reconoce el orden claro de las operaciones."),
  reinforce="Repasa la suma y la resta vertical con 3 números decimales de dos cifras decimales de tu elección.",
  extend="Inventa un problema donde se sume y luego se reste con decimales y resuélvelo.")


# ================================================================ OA 13
L(OA13, 1,
  mat="Lápiz y papel. Dibuja barras de 10 cuadritos de ancho para representar fracciones.",
  use="Aprenderé a resolver problemas que se calculan con fracciones propias del mismo denominador. Sirve para repartir y comparar partes de un todo.",
  prior=["Sé qué es una fracción propia: el numerador es menor que el denominador.", "Sé sumar y restar números naturales."],
  explain=[
      "Una fracción propia es menor que 1 entero. El denominador dice en cuántas partes iguales se dividió el entero y el numerador dice cuántas partes se toman. En 3/8, el entero se dividió en 8 partes y se toman 3.",
      "Si los denominadores son iguales, las partes son del mismo tamaño y solo sumas o restas los numeradores. 2/8 + 3/8 = 5/8. El denominador no cambia porque las partes siguen siendo octavos.",
      "En un problema, primero lee qué es el entero, dibuja una barra y pinta las partes. Después decide si juntas (sumas) o quitas (restas). Revisa que el resultado sea una parte del mismo entero. Si la suma llega a 8/8, ya tienes el entero completo.",
  ],
  vocab=[("fracción propia", "fracción con el numerador menor que el denominador; vale menos que 1"), ("numerador", "número de arriba: cuántas partes se toman"), ("denominador", "número de abajo: en cuántas partes iguales se divide el entero"), ("entero", "la cantidad completa que se divide en partes")],
  worked=[
      ("Sumar partes", "Una pizza se corta en 8 trozos iguales. Ana come 2 trozos y Luis come 3. ¿Qué fracción de la pizza comieron?", ["Cada trozo es 1/8. Ana come 2/8 y Luis 3/8.", "Sumo los numeradores y dejo el denominador: 2 + 3 = 5."], "Comieron 5/8 de la pizza"),
      ("Restar partes", "Un frasco tiene 9/10 de su capacidad con agua. Se usan 4/10 del frasco. ¿Qué fracción queda con agua?", ["Las partes son décimos, así que resto los numeradores: 9 − 4 = 5.", "El denominador se mantiene: 10."], "Queda 5/10 del frasco"),
  ],
  mist=[
      ("Calcular 2/8 + 3/8 = 5/16.", "Se suman también los denominadores.", "El denominador dice el tamaño de las partes y no cambia: 2/8 + 3/8 = 5/8."),
      ("Pensar que 4/10 − 1/10 = 3/0.", "Se restan los denominadores y queda 0.", "Solo se restan numeradores: 4/10 − 1/10 = 3/10."),
  ],
  R=[ex("Una barra se divide en 6 partes iguales y se pintan 2. ¿Qué fracción está pintada?", "2/6", "Se pintan 2 de 6 partes iguales."),
     ex("Calcula 1/5 + 2/5.", "3/5", "Los denominadores son iguales: 1 + 2 = 3 quintos."),
     ex("Calcula 5/6 − 2/6.", "3/6", "Se restan los numeradores: 5 − 2 = 3 sextos.")],
  C=[ex("En 3/8 + 4/8, ¿qué número queda como denominador del resultado?", "8", "Los octavos no cambian de tamaño al sumarse."),
     ex("Calcula 3/8 + 4/8.", "7/8", "3 + 4 = 7 octavos."),
     ex("Una torta se divide en 10 partes iguales. Se comen 3 y quedan 7. ¿Qué fracción quedó?", "7/10", "Quedan 7 de las 10 partes iguales.")],
  A=[ex("Marta pinta 3/12 de un mural el lunes y 5/12 el martes. ¿Qué fracción del mural ha pintado?", "8/12", "Se suman 3 + 5 = 8 doceavos."),
     ex("De una botella llena de agua se toma 4/9. ¿Qué fracción de la botella queda?", "5/9", "La botella llena es 9/9 y 9/9 − 4/9 = 5/9."),
     ex("Calcula 2/7 + 3/7 + 1/7.", "6/7", "Se suman los tres numeradores: 2 + 3 + 1 = 6.")],
  Z=[ex("Ema dice que 3/10 + 4/10 = 7/20. ¿Cuál es el error?", "Sumó también los denominadores; lo correcto es 7/10", "Los décimos siguen siendo décimos al sumarlos, por eso el denominador queda en 10."),
     ex("¿Cuál es mayor: la suma 5/12 + 4/12 o la fracción 8/12?", "5/12 + 4/12", "La suma da 9/12 y 9/12 es mayor que 8/12.")],
  D=[ex("Una cuerda se divide en 12 partes iguales. Se usan 5/12 en una tarea y 4/12 en otra. ¿Qué fracción de la cuerda sobra?", "3/12", "Se usan 9/12 en total y sobran 12/12 − 9/12 = 3/12."),
     ex("Dos fracciones del mismo denominador 9 suman 8/9 y una de ellas es 3/9. ¿Cuál es la otra?", "5/9", "8/9 − 3/9 = 5/9.")],
  ctx=[ex("Un curso de 12 grupos iguales hace una tarea. 7 grupos entregan el lunes y 3 grupos el martes. ¿Qué fracción del curso falta por entregar? Responde con el denominador 12.", "2/12", "Entregaron 7/12 + 3/12 = 10/12, así que faltan 12/12 − 10/12 = 2/12.")],
  chk=[ex("Calcula 4/9 + 3/9.", "7/9", "Se suman los numeradores y el denominador no cambia."),
       ex("Calcula 7/10 − 2/10.", "5/10", "7 − 2 = 5 décimos."),
       ex("¿Cuánto es 6/6 de un entero?", "El entero completo", "Si se toman todas las partes, se tiene 1 entero.")],
  open=("Se tiene un chocolate dividido en 12 partes iguales. Inventa una historia donde alguien come 3/12 y otra persona come 4/12. Dibuja la barra, pinta las partes y escribe qué fracción queda.",
        "Barra de 12 partes: Ema come 3/12 y Tito 4/12. Comieron 7/12 y quedan 5/12.",
        ["usa el denominador 12", "dibuja las partes", "suma y resta los numeradores", "escribe la fracción que queda"],
        ["dibujo", "operaciones escritas"],
        ["sumar denominadores", "no revisar si la barra completa es 12/12"],
        "Pide que muestre en el dibujo la fracción que queda. Reconoce que respete el denominador."),
  reinforce="Dibuja una barra de 8 partes y pinta 2/8 y luego 3/8 más. Escribe cuántas quedan sin pintar.",
  extend="Escribe una resta de fracciones con denominador 10 cuyo resultado sea 3/10 y explica cómo la armaste.")

L(OA13, 2,
  mat="Lápiz y papel. Dibuja una cuadrícula de 10 × 10 para ver centésimas y una barra de 10 partes para ver décimas.",
  use="Aprenderé a relacionar fracciones con decimales y a resolver problemas con medidas decimales. Sirve para sumar longitudes, pesos y capacidades.",
  prior=["Sé que 1/10 = 0,1 y 1/100 = 0,01.", "Sé sumar y restar decimales alineando la coma."],
  explain=[
      "Una fracción con denominador 10 se escribe como decimal con décimas: 3/10 = 0,3. Una fracción con denominador 100 se escribe con centésimas: 25/100 = 0,25. También sabes que 1/2 = 0,5 y 1/4 = 0,25.",
      "En un problema puedes mezclar fracciones y decimales. Lo más cómodo es escribir todo con la misma representación. Por ejemplo, 1/2 + 0,25 se escribe 0,5 + 0,25 = 0,75.",
      "Una cuadrícula de 10 × 10 sirve para ver las dos formas: cada cuadrito es 1/100 = 0,01 y cada fila es 1/10 = 0,1. Si pintas 4 filas y 5 cuadritos más, pintaste 0,45 de la cuadrícula.",
  ],
  vocab=[("equivalente", "que vale lo mismo aunque se escriba distinto, como 1/2 y 0,5"), ("décimo", "fracción con denominador 10"), ("centésimo", "fracción con denominador 100"), ("representación", "forma de mostrar una cantidad: dibujo, fracción o decimal")],
  worked=[
      ("Pasar a decimal y sumar", "Un listón mide 1/2 m y otro mide 0,25 m. ¿Cuánto miden juntos?", ["Paso 1/2 a decimal: 1/2 = 0,5.", "Sumo con las comas alineadas: 0,50 + 0,25 = 0,75."], "0,75 m"),
      ("Pintar en una cuadrícula", "En una cuadrícula de 100 cuadritos se pintan 4 filas completas y 5 cuadritos más. ¿Qué decimal está pintado?", ["Cada fila es 10 cuadritos: 4 filas son 40 cuadritos.", "40 + 5 = 45 cuadritos de 100: 45/100 = 0,45."], "0,45"),
  ],
  mist=[
      ("Escribir 3/10 como 0,03.", "Se confunde décimas con centésimas.", "3/10 son 3 décimas: 0,3. Para 0,03 se necesitaría 3/100."),
      ("Escribir 1/2 como 0,2.", "Se toma el denominador como cifra decimal.", "1/2 es la mitad de 1 y vale 0,5. Entonces 1/2 + 0,25 = 0,5 + 0,25 = 0,75."),
  ],
  R=[ex("Escribe 3/10 como número decimal.", "0,3", "Tres décimos son tres décimas."),
     ex("Escribe 25/100 como número decimal.", "0,25", "Veinticinco centésimos son 0,25."),
     ex("¿Qué decimal es igual a 1/2?", "0,5", "La mitad de una unidad es 5 décimas.")],
  C=[ex("¿Qué fracción con denominador 10 es igual a 0,7?", "7/10", "0,7 son 7 décimas."),
     ex("En una cuadrícula de 100 cuadritos se pintan 3 filas completas de 10 cuadritos. ¿Qué decimal está pintado?", "0,3", "30 cuadritos de 100 son 30/100, igual a 0,3."),
     ex("¿Qué decimal es igual a 3/4?", "0,75", "1/4 es 0,25, así que 3/4 son 3 × 0,25 = 0,75.")],
  A=[da("Un listón mide 1/4 m y otro mide 0,5 m. ¿Cuánto miden juntos?", "0.25+0.5", "Se pasa 1/4 a 0,25 y se suma.", " m"),
     da("Una botella tiene 0,75 L y se bebe 1/4 de litro. ¿Cuántos litros quedan?", "0.75-0.25", "1/4 L es 0,25 L; se resta.", " L"),
     da("Una cinta mide 3/10 m y otra mide 0,4 m. ¿Cuánto miden juntas?", "0.3+0.4", "3/10 m es 0,3 m y se suma 0,4 m.", " m")],
  Z=[ex("Paula escribió 3/10 = 0,03. ¿Cuál es el decimal correcto?", "0,3", "Tres décimos son tres décimas, no tres centésimas."),
     ex("¿Es mayor 0,5 o 1/4? Responde y explica con decimales.", "0,5 es mayor", "1/4 = 0,25 y 0,5 = 0,50; 50 centésimas es más que 25 centésimas.")],
  D=[da("Calcula 7/10 + 0,25 + 1/4 y da el resultado como decimal.", "0.7+0.25+0.25", "Se pasan todos a decimal: 0,7 + 0,25 + 0,25."),
     da("En una cuadrícula de 100 cuadritos hay 0,35 pintado de azul y 0,4 de rojo. ¿Qué decimal queda sin pintar?", "1-0.35-0.4", "Todo es 1 y se quitan las dos partes pintadas.")],
  ctx=[da("Una receta usa 0,5 kg de harina y 1/4 kg de azúcar. ¿Cuántos kilogramos de ingredientes secos son en total?", "0.5+0.25", "1/4 kg es 0,25 kg y se suman las dos masas.", " kg")],
  chk=[ex("Escribe 9/10 como decimal.", "0,9", "Nueve décimas se escriben 0,9."),
       ex("Escribe 0,05 como fracción con denominador 100.", "5/100", "0,05 son 5 centésimas."),
       da("Calcula 1/2 + 0,3.", "0.5+0.3", "1/2 es 0,5 y se suman décimas.")],
  open=("Una cinta mide 3/4 m. Otra mide 0,4 m. Escribe las dos medidas como decimales, calcula cuánto miden juntas y cuánto más mide la primera que la segunda. Dibuja una barra de 100 cuadritos para el primer largo.",
        "3/4 = 0,75 m. Juntas: 0,75 + 0,4 = 1,15 m. La primera mide 0,35 m más.",
        ["escribe 3/4 como 0,75", "suma con comas alineadas", "resta para comparar", "dibuja la barra"],
        ["dos medidas en decimal", "suma y resta", "dibujo"],
        ["escribir 3/4 como 0,34", "olvidar la unidad"],
        "Pide que explique en la cuadrícula por qué 75 de 100 cuadritos son 3/4. Reconoce que use una sola representación al calcular."),
  reinforce="Escribe en tu cuaderno 1/2, 1/4, 3/4 y 1/10 como decimales y pinta cada uno en una cuadrícula de 100.",
  extend="Explica con una cuadrícula por qué 0,5 y 0,50 son el mismo número.")

L(OA13, 3,
  mat="Lápiz y papel. Usa una recta numérica de 0 a 2 con marcas cada 0,25 si quieres.",
  use="Aprenderé a elegir si conviene trabajar con fracciones o con decimales y a justificar mi decisión. Sirve para resolver problemas con menos errores.",
  prior=["Sé pasar fracciones simples a decimales.", "Sé sumar y restar fracciones del mismo denominador y decimales."],
  explain=[
      "Un mismo problema se puede resolver con fracciones o con decimales. Si todos los datos son fracciones del mismo denominador, conviene sumar fracciones. Si hay datos de medidas con coma, conviene trabajar con decimales.",
      "Cuando mezclas, cambia todo a una sola forma. Con denominadores 2, 4, 5 o 10 pasar a decimal es fácil: 1/5 = 0,2. También puedes sumar fracciones de distinto denominador si uno es múltiplo del otro: 1/2 + 1/4 = 2/4 + 1/4 = 3/4.",
      "Justifica tu elección con una razón concreta: «Elegí decimales porque la balanza muestra 0,75 kg». Después comprueba que el resultado tenga sentido, por ejemplo comparando con 1 entero o con una estimación.",
  ],
  vocab=[("estrategia", "plan elegido para resolver un problema"), ("justificar", "dar una razón de por qué hiciste algo"), ("múltiplo", "número que aparece al contar de a saltos iguales: 4 es múltiplo de 2"), ("estimación", "valor aproximado que ayuda a revisar un resultado")],
  worked=[
      ("Elegir decimales", "Una balanza muestra 0,6 kg de tomates y 0,75 kg de cebollas. ¿Cuántos kilos hay?", ["Los datos ya vienen con coma: conviene decimales.", "Sumo 0,60 + 0,75 = 1,35."], "1,35 kg"),
      ("Elegir fracciones", "Un jardín tiene 1/2 con flores y 1/4 con pasto. ¿Qué fracción del jardín está ocupada?", ["Un medio es 2/4 porque 1/2 = 2/4.", "Sumo: 2/4 + 1/4 = 3/4."], "3/4 del jardín"),
  ],
  mist=[
      ("Sumar 1/2 + 1/4 = 2/6.", "Se suman numeradores y denominadores por separado.", "Pasa 1/2 a 2/4 y suma 2/4 + 1/4 = 3/4."),
      ("Sumar 0,6 + 0,75 alineando los últimos dígitos.", "Se obtiene 0,81, porque se suma 6 con 5 y 7 con nada.", "Alinea las comas: 0,60 + 0,75 = 1,35."),
  ],
  R=[ex("¿Cuál es el denominador común para sumar 1/2 + 1/4?", "4", "Un medio es igual a 2/4; así ambas fracciones tienen cuartos."),
     da("Calcula 0,6 + 0,75.", "0.6+0.75", "Se escribe 0,60 + 0,75 y se alinean las comas."),
     ex("Calcula 1/2 + 1/4.", "3/4", "1/2 = 2/4 y 2/4 + 1/4 = 3/4.")],
  C=[ex("Un dato dice 0,5 kg y otro dice 1/4 kg. Si quieres sumar con decimales, ¿cómo escribes 1/4 kg?", "0,25 kg", "Un cuarto vale 0,25."),
     ex("Calcula 3/10 + 1/5 con denominador 10.", "5/10", "1/5 = 2/10 y 3/10 + 2/10 = 5/10."),
     da("Calcula 0,2 + 1/5, pasando 1/5 a decimal.", "0.2+0.2", "1/5 = 0,2.")],
  A=[ex("Un huerto tiene 1/4 con lechugas y 1/8 con zanahorias. ¿Qué fracción está ocupada?", "3/8", "1/4 = 2/8 y 2/8 + 1/8 = 3/8."),
     da("Una cinta de 2 m pierde 0,35 m en un nudo y 0,4 m en otro. ¿Cuánto mide ahora?", "2-0.35-0.4", "Se restan las dos pérdidas de la longitud inicial.", " m"),
     ex("Una torta se divide en 10 partes. Se comen 2/10 y 1/5. ¿Qué fracción se comió?", "4/10", "1/5 = 2/10 y 2/10 + 2/10 = 4/10.")],
  Z=[ex("Rosa dice: «Para 1/2 + 1/4 sumo arriba 1 + 1 y abajo 2 + 4: me da 2/6». ¿Qué respondes?", "Está mal; lo correcto es 3/4", "Los denominadores distintos no se suman; se busca un denominador común."),
     ex("¿Qué es mayor: 1/4 + 0,6 o 0,9? Compáralos como decimales.", "0,9", "1/4 + 0,6 = 0,25 + 0,6 = 0,85, que es menor que 0,9.")],
  D=[da("Calcula 0,75 + 0,5 + 1/4 + 0,125.", "0.75+0.5+0.25+0.125", "Se pasan todo a decimales y se suman."),
     ex("Una jarra tiene 1 L. Se sirven 0,3 L, 1/4 L y 0,2 L. ¿Cuántos litros quedan? Responde en decimal.", "0,25 L", "Se sirven 0,3 + 0,25 + 0,2 = 0,75 L y 1 − 0,75 = 0,25 L.")],
  ctx=[da("Un recorrido de 3,2 km se hace así: 1,05 km caminando, 0,75 km en micro y el resto corriendo. ¿Cuántos km corrió?", "3.2-1.05-0.75", "Se restan los dos tramos del total.", " km")],
  chk=[ex("Calcula 1/3 + 1/3.", "2/3", "Los denominadores son iguales: 1 + 1 = 2 tercios."),
       da("Calcula 0,5 + 0,3.", "0.5+0.3", "Se suman décimas."),
       ex("Para sumar 3/5 + 1/10, ¿en qué fracción conviene convertir 3/5?", "6/10", "3/5 = 6/10 porque se multiplica numerador y denominador por 2.")],
  open=("Elige entre estos dos datos: «una botella tiene 0,6 L y otra tiene 1/4 L» o «un tramo mide 0,5 km y otro 3/4 km». Escribe qué representación elegiste, por qué, calcula la suma y comprueba con otra representación.",
        "Elijo decimales: 0,6 + 0,25 = 0,85 L. Comprobación: 6/10 + 25/100 = 60/100 + 25/100 = 85/100.",
        ["elige una forma y la justifica", "calcula bien", "comprueba con otra forma", "escribe la unidad"],
        ["justificación escrita", "cálculo", "comprobación"],
        ["sumar denominadores", "mezclar fracciones y decimales sin convertir"],
        "Pide que diga qué la otra forma habría demostrado. Reconoce la justificación."),
  reinforce="Escribe las cinco fracciones 1/2, 1/4, 1/5, 3/10, 3/4 como decimales.",
  extend="Inventa un problema donde convenga sumar fracciones y otro donde convenga sumar decimales.")

L(OA13, 4,
  mat="Lápiz y papel. Puedes dibujar barras para ayudarte.",
  use="Aprenderé a resolver problemas más difíciles con fracciones y decimales: con datos de sobra, con varios pasos o con datos que faltan. Sirve para resolver situaciones reales.",
  prior=["Sé sumar y restar fracciones propias con denominadores 2, 4, 5 y 10.", "Sé sumar y restar decimales hasta la milésima."],
  explain=[
      "Un problema rutinario se parece a otros que ya resolviste. Un problema no rutinario tiene algo distinto: datos de sobra, un dato escondido o varios pasos. Para empezar, subraya la pregunta y lista los datos útiles.",
      "A veces hay que hacer dos operaciones: primero sumas para saber cuánto se usó, después restas para saber cuánto queda. También puedes usar la operación inversa para encontrar un dato que falta: si total − usado = queda, entonces total = queda + usado.",
      "Haz una estimación y comprueba el resultado con una segunda estrategia. Termina siempre con una respuesta completa: número, unidad y qué significa en la historia.",
  ],
  vocab=[("dato de sobra", "información del problema que no se necesita para responder"), ("problema no rutinario", "problema que no se resuelve con un solo cálculo conocido"), ("operación inversa", "operación que deshace otra"), ("respuesta completa", "número con su unidad y su significado en la historia")],
  worked=[
      ("Dato de sobra", "Una caja pesa 2,4 kg. Se agregan 1,35 kg de libros y 0,5 kg de lápices. Hay 3 estudiantes. ¿Cuánto pesa la caja ahora?", ["El número de estudiantes no sirve para el peso.", "Sumo 2,4 + 1,35 + 0,5 = 4,25."], "4,25 kg"),
      ("Dato que falta", "Un bidón tenía agua, se sacaron 0,8 L y quedaron 2,45 L. ¿Cuántos litros había al comienzo?", ["Total = lo que quedó + lo que se sacó.", "2,45 + 0,8 = 3,25."], "3,25 L"),
  ],
  mist=[
      ("Sumar el dato de sobra (el número de estudiantes) al peso.", "Se usan todos los números sin pensar en la pregunta.", "Pregúntate si cada dato sirve para la pregunta. Los estudiantes no cambian el peso."),
      ("Restar en vez de sumar para hallar el total inicial: 2,45 − 0,8.", "No se piensa en la historia: se sacó agua, entonces antes había más.", "Había más antes: se suma lo que se sacó."),
  ],
  R=[ex("En un problema, ¿qué debes subrayar primero: la pregunta o los datos de sobra?", "La pregunta", "Con la pregunta clara decides qué datos sirven."),
     da("Calcula 2,4 + 1,35.", "2.4+1.35", "Se escribe 2,40 + 1,35 y se suma."),
     ex("Calcula 5/10 − 2/10.", "3/10", "Se restan numeradores: 5 − 2 = 3.")],
  C=[ex("Una mochila pesa 1,2 kg y se le agrega un libro de 0,8 kg. El libro tiene 150 páginas. ¿Qué dato no sirve para calcular el peso?", "Las 150 páginas", "El número de páginas no se suma al peso: ya está incluido en los 0,8 kg."),
     da("Un bidón queda con 1,35 L después de sacar 0,6 L. ¿Cuántos litros había antes?", "1.35+0.6", "El total inicial es lo que quedó más lo que se sacó.", " L"),
     ex("Se usan 3/10 de una tela y luego 2/5. ¿Qué fracción de tela se usó en total, en décimos?", "7/10", "2/5 = 4/10 y 3/10 + 4/10 = 7/10.")],
  A=[da("Una caja pesa 1,8 kg. Se agregan 2,25 kg de libros y 0,6 kg de lápices. ¿Cuánto pesa ahora?", "1.8+2.25+0.6", "Se suman las tres masas.", " kg"),
     da("Un tramo de 5 km se hace así: 1,75 km en bicicleta, 2,5 km en micro y el resto a pie. ¿Cuántos km fueron a pie?", "5-1.75-2.5", "Se restan los dos tramos del total.", " km"),
     ex("Una pared se pinta así: 1/4 de rojo, 3/10 de azul. ¿Qué decimal queda sin pintar?", "0,45", "1/4 = 0,25 y 3/10 = 0,3; 0,25 + 0,3 = 0,55 y 1 − 0,55 = 0,45.")],
  Z=[ex("Un jugo tenía 3,25 L, se sirvieron 1,5 L y se agregaron 0,75 L. Camila dice que quedaron 1,0 L. ¿Cuál es el resultado correcto?", "2,5 L", "3,25 − 1,5 = 1,75 y 1,75 + 0,75 = 2,5; Camila restó lo que se agregó en vez de sumarlo."),
     ex("Mateo dice que 5 − 2,3 + 2,3 vale 0. ¿Cuánto vale en realidad?", "5", "5 − 2,3 = 2,7 y 2,7 + 2,3 = 5; restar y sumar lo mismo vuelve al número inicial.")],
  D=[da("Mateo ahorra 12,5 kg de tapitas. Si junta 3,75 kg más y entrega 6,25 kg, ¿cuántos kg le quedan?", "12.5+3.75-6.25", "Se suma lo agregado y se resta lo entregado.", " kg"),
     ex("Dos cintas miden juntas 2,5 m. La primera mide 3/4 m. ¿Cuánto mide la segunda?", "1,75 m", "3/4 m = 0,75 m y 2,5 − 0,75 = 1,75 m.")],
  ctx=[da("Una carrera de 4 km se corre en tres tramos. El primero mide 0,75 km y el segundo 1,2 km. ¿Cuánto mide el tercero?", "4-0.75-1.2", "Al total se le restan los dos tramos conocidos.", " km")],
  chk=[da("Calcula 4,5 − 1,25.", "4.5-1.25", "Se escribe 4,50 − 1,25."),
       ex("En un problema piden «cuánto queda». ¿Qué operación usas casi siempre?", "Resta", "Quitar una parte de un todo se resuelve restando."),
       ex("Calcula 7/10 − 3/10 + 1/10.", "5/10", "7 − 3 + 1 = 5 décimos.")],
  open=("Una mochila vacía pesa 0,8 kg. Se le agregan un cuaderno de 0,35 kg, un estuche de 0,25 kg y una botella de 0,6 kg. Hay 4 libros sobre la mesa que no se guardan. Calcula cuánto pesa la mochila llena, di qué dato sobra y comprueba con una estimación.",
        "Sobra: los 4 libros. Peso: 0,8 + 0,35 + 0,25 + 0,6 = 2 kg. Estimación: 1 + 0 + 0 + 1 = 2 kg.",
        ["identifica el dato de sobra", "suma bien", "estima y compara", "escribe la respuesta con unidad"],
        ["operación", "estimación", "respuesta completa"],
        ["sumar el dato de sobra", "olvidar la unidad"],
        "Pide que justifique por qué los libros no cambian el peso de la mochila. Reconoce el orden."),
  reinforce="Resuelve de nuevo el problema de la caja cambiando un dato y compara con el original.",
  extend="Crea un problema con un dato de sobra y resuélvelo.")


# ================================================================ OA 14
L(OA14, 1,
  mat="Lápiz y papel. Si quieres, usa palitos de helado o lápices para armar los patrones.",
  use="Aprenderé a encontrar la regla de una sucesión de números y a usarla para continuar la serie. Sirve para predecir qué sigue en un patrón.",
  prior=["Sé sumar y restar con números hasta 1.000.", "Sé contar de 2 en 2, de 5 en 5 y de 10 en 10."],
  explain=[
      "Una sucesión es una lista de números ordenada que sigue una regla. Cada número se llama término. En 4, 9, 14, 19 cada término es 5 más que el anterior: la regla es «sumar 5».",
      "Para descubrir la regla, calcula la diferencia entre términos que están uno al lado del otro. Si la diferencia es siempre la misma, la regla es una suma o una resta. Si la sucesión baja, como 50, 44, 38, la regla es «restar 6».",
      "Con la regla puedes predecir. Después de 19 viene 24 y luego 29. Siempre comprueba que la regla funcione para todos los términos dados, no solo para los dos primeros.",
  ],
  vocab=[("sucesión", "lista ordenada de números que sigue una regla"), ("término", "cada número de la sucesión"), ("regla", "lo que haces para pasar de un término al siguiente"), ("predecir", "decir qué viene antes de que ocurra, usando la regla")],
  worked=[
      ("Sucesión creciente", "Encuentra la regla de 4, 9, 14, 19 y escribe los dos términos siguientes.", ["9 − 4 = 5, 14 − 9 = 5, 19 − 14 = 5.", "La regla es sumar 5. Sigo: 19 + 5 = 24, 24 + 5 = 29."], "Regla: +5. Siguen 24 y 29"),
      ("Sucesión decreciente", "Encuentra la regla de 50, 44, 38, 32 y escribe el siguiente término.", ["50 − 44 = 6, 44 − 38 = 6, 38 − 32 = 6.", "La regla es restar 6: 32 − 6 = 26."], "Regla: −6. Sigue 26"),
  ],
  mist=[
      ("Decir que la regla de 4, 9, 14, 19 es «sumar 5» solo porque 9 − 4 = 5, sin mirar el resto.", "Se revisa un solo par de términos.", "Comprueba todos: 14 − 9 = 5 y 19 − 14 = 5. Funciona."),
      ("Continuar 50, 44, 38 con 32, 28.", "Se cambia la regla a mitad de camino.", "La regla debe mantenerse: siempre −6. Los siguientes son 32 y 26."),
  ],
  R=[ex("En la sucesión 3, 6, 9, 12, ¿cuánto se suma de un término al siguiente?", "3", "6 − 3 = 3, 9 − 6 = 3 y 12 − 9 = 3."),
     ex("¿Qué número sigue en 10, 20, 30, 40?", "50", "La regla es sumar 10."),
     ex("¿Qué número sigue en 100, 95, 90, 85?", "80", "La regla es restar 5.")],
  C=[ex("Escribe la regla de 4, 9, 14, 19.", "Sumar 5", "Entre términos consecutivos la diferencia siempre es 5."),
     ex("Escribe la regla de 50, 44, 38, 32.", "Restar 6", "Cada término es 6 menos que el anterior."),
     ex("¿Cuál es el término que sigue a 19 en la sucesión 4, 9, 14, 19?", "24", "19 + 5 = 24.", calc="19+5")],
  A=[ex("Continúa con los tres términos que siguen: 7, 15, 23, 31, …", "39, 47, 55", "La regla es sumar 8."),
     ex("Continúa con los dos términos que siguen: 120, 108, 96, …", "84, 72", "La regla es restar 12."),
     ex("Una sucesión empieza en 3 y la regla es sumar 7. Escribe los cuatro primeros términos.", "3, 10, 17, 24", "Se suma 7 cada vez desde el 3.")],
  Z=[ex("Un estudiante dice que la regla de 2, 5, 9, 14 es «sumar 3». ¿Tiene razón?", "No; las diferencias son 3, 4 y 5", "5 − 2 = 3, 9 − 5 = 4 y 14 − 9 = 5; la diferencia crece y no es una suma fija."),
     ex("La sucesión parte en 10 y resta 3 cada vez: 10, 7, 4, 1, … ¿llega justo al 0? Responde sí o no.", "No", "Después de 1 sigue −2; la sucesión salta el 0.")],
  D=[ex("La sucesión 5, 8, 11, 14 sigue con la misma regla. ¿Cuál es el décimo término? Cuenta los 10 términos de la lista.", "32", "Es 5 más 9 veces 3: 5 + 27 = 32.", calc="5+9*3"),
     ex("En la sucesión 200, 190, 180, …, ¿cuántos términos hay hasta llegar a 100, contando el 200 y el 100?", "11", "De 200 a 100 hay 100 de diferencia y se resta de 10 en 10, o sea 10 saltos y 11 términos.")],
  ctx=[ex("Mía ahorra $500 cada semana y empezó con $1.500. Escribe el ahorro durante las próximas 4 semanas después de empezar (primera, segunda, tercera y cuarta), separados por comas.", "$2.000, $2.500, $3.000, $3.500", "Se suma $500 cada semana a $1.500.")],
  chk=[ex("¿Qué número sigue en 6, 12, 18, 24?", "30", "La regla es sumar 6."),
       ex("¿Cuál es la regla de 90, 80, 70, 60?", "Restar 10", "Cada término es 10 menos."),
       ex("¿Qué número falta? 11, 16, __, 26", "21", "La regla es sumar 5: 16 + 5 = 21.")],
  open=("Elige una de estas sucesiones: 6, 11, 16, 21 o 80, 71, 62, 53. Escribe la regla, completa los tres términos siguientes y explica cómo comprobaste que la regla funciona en todos los pasos.",
        "6, 11, 16, 21: regla +5. Siguen 26, 31, 36. Comprobé 11 − 6, 16 − 11 y 21 − 16: todas dan 5.",
        ["identifica la regla", "continúa bien", "comprueba con todos los términos", "explica con palabras"],
        ["regla escrita", "términos nuevos", "comprobación"],
        ["revisar solo dos términos", "cambiar la regla a mitad de camino"],
        "Pide que diga qué diferencia calculó en cada paso. Reconoce la comprobación completa."),
  reinforce="Cuenta de 3 en 3 desde el 0 hasta 30 y escribe la regla.",
  extend="Inventa una sucesión que baje y escribe la regla para que otra persona la descubra.")

L(OA14, 2,
  mat="Lápiz y papel cuadriculado. Cuadrados de papel o monedas de juguete para armar figuras (opcional).",
  use="Aprenderé a conectar una sucesión con una tabla y con una regla que sirve para cualquier posición. Sirve para saber el término número 20 sin escribir todos los anteriores.",
  prior=["Sé encontrar la regla de una sucesión creciente o decreciente.", "Sé multiplicar con las tablas."],
  explain=[
      "Puedes organizar una sucesión en una tabla con dos filas: la posición (1.º, 2.º, 3.º…) y el término. Así ves cómo cambia el término cuando cambia la posición.",
      "En 5, 8, 11, 14 la posición 1 vale 5, la 2 vale 8 y la 3 vale 11. El término crece 3 cada vez. Una regla para cualquier posición es «multiplica la posición por 3 y suma 2»: posición 1: 1 × 3 + 2 = 5; posición 4: 4 × 3 + 2 = 14.",
      "Con esa regla, la posición 10 vale 10 × 3 + 2 = 32, sin escribir los términos del 5 al 9. Comprueba siempre la regla con dos posiciones que ya conoces.",
  ],
  vocab=[("posición", "lugar que ocupa un término en la lista: 1.º, 2.º, 3.º…"), ("tabla", "cuadro con filas y columnas que ordena datos"), ("regla general", "instrucción que sirve para obtener cualquier término desde su posición"), ("figura", "dibujo que forma parte de un patrón")],
  worked=[
      ("Completar una tabla", "En la sucesión 5, 8, 11, 14, ¿qué valor tiene la posición 10?", ["La sucesión crece 3 por posición. La regla es posición × 3 + 2.", "Para la posición 10: 10 × 3 = 30 y 30 + 2 = 32."], "32"),
      ("Patrón de palitos", "La figura 1 tiene 4 palitos, la figura 2 tiene 7 y la figura 3 tiene 10. ¿Cuántos palitos tiene la figura 5?", ["Cada figura tiene 3 palitos más que la anterior: la regla es posición × 3 + 1.", "Para la posición 5: 5 × 3 + 1 = 16."], "16 palitos"),
  ],
  mist=[
      ("Decir que el término de la posición 10 es 5 + 10 = 15 en la sucesión 5, 8, 11, 14.", "Se suma la posición al primer término sin usar la regla.", "El término crece de a 3: usa posición × 3 + 2 y obtienes 32."),
      ("Confundir el término con la posición.", "Se mezcla el número de lugar con el valor que hay en ese lugar.", "La posición es 1.º, 2.º, 3.º… y el término es el número escrito en ese lugar."),
  ],
  R=[ex("En la sucesión 5, 8, 11, 14, ¿cuál es el valor de la posición 3?", "11", "La posición 3 es el tercer número de la lista."),
     ex("En la sucesión 2, 4, 6, 8, ¿en qué posición está el 6?", "3", "El 6 es el tercer número."),
     ex("Si la regla es «posición × 2», ¿cuánto vale la posición 5?", "10", "5 × 2 = 10.", calc="5*2")],
  C=[ex("Si la regla es «posición × 3 + 2», ¿cuánto vale la posición 6?", "20", "6 × 3 = 18 y 18 + 2 = 20.", calc="6*3+2"),
     ex("Si la regla es «posición × 3 + 2», ¿cuánto vale la posición 7?", "23", "7 × 3 = 21 y 21 + 2 = 23.", calc="7*3+2"),
     ex("La tabla tiene posiciones 1, 2, 3 y términos 7, 10, 13. ¿Cuánto crece el término por cada posición?", "3", "10 − 7 = 3 y 13 − 10 = 3.")],
  A=[ex("Con la regla «posición × 4 + 1», completa los términos de las posiciones 1, 2 y 3.", "5, 9, 13", "1 × 4 + 1 = 5; 2 × 4 + 1 = 9; 3 × 4 + 1 = 13."),
     ex("La sucesión es 6, 11, 16, 21 y la regla es «posición × 5 + 1». ¿Cuánto vale la posición 8?", "41", "8 × 5 = 40 y 40 + 1 = 41.", calc="8*5+1"),
     ex("Una tabla tiene posiciones 1 a 4 y términos 10, 20, 30, 40. ¿Qué regla tiene?", "Posición × 10", "Cada término es 10 veces su posición.")],
  Z=[ex("Ema dice que en 5, 8, 11, 14 la posición 5 vale 17 porque «hay que sumar 3 al 14». Julio dice que vale 17 con la regla posición × 3 + 2. ¿Quién tiene razón?", "Ambos, porque dan 17", "14 + 3 = 17 y 5 × 3 + 2 = 17; las dos formas coinciden."),
     ex("La regla «posición × 2 + 1» y la sucesión 3, 5, 7, 9. ¿La regla funciona? Comprueba con la posición 4.", "Sí", "4 × 2 + 1 = 9, que es el cuarto término.")],
  D=[ex("Con la regla «posición × 6 − 1», ¿en qué posición el término vale 29?", "5", "Se prueba la posición 5: 5 × 6 = 30 y 30 − 1 = 29."),
     ex("Una sucesión empieza en 4 y suma 5 cada vez. ¿Cuál es el término de la posición 12?", "59", "4 + 11 × 5 = 4 + 55 = 59.", calc="4+11*5")],
  ctx=[ex("Un taller cobra $1.000 fijos más $500 por cada hora. La regla es «horas × 500 + 1.000». ¿Cuánto cuesta una reparación de 6 horas?", "$4.000", "6 × 500 = 3.000 y 3.000 + 1.000 = 4.000.")],
  chk=[ex("Con la regla «posición × 2 + 3», ¿cuánto vale la posición 5?", "13", "5 × 2 = 10 y 10 + 3 = 13.", calc="5*2+3"),
       ex("En la tabla 1→7, 2→9, 3→11, ¿cuánto se suma cada vez?", "2", "9 − 7 = 2 y 11 − 9 = 2."),
       ex("¿La posición es el número de lugar o el valor de ese lugar?", "El número de lugar", "El valor es el término, no la posición.")],
  open=("Arma una tabla con las posiciones 1, 2, 3, 4 y los términos 9, 13, 17, 21. Escribe la regla general, calcula el término de la posición 10 y comprueba con otra posición.",
        "Crece 4 por posición y 9 = 4 × 1 + 5. Regla: posición × 4 + 5. Posición 10: 45. Comprobación: posición 3 es 3 × 4 + 5 = 17, correcto.",
        ["completa la tabla", "escribe la regla general", "calcula la posición 10", "comprueba con otra posición"],
        ["tabla", "regla", "comprobación"],
        ["usar solo la diferencia sin la regla general", "no comprobar"],
        "Pide que diga qué cambió para pasar de una posición a la siguiente. Reconoce la comprobación."),
  reinforce="Completa una tabla con la regla «posición × 3» para las posiciones 1 a 6.",
  extend="Descubre la regla general de 3, 7, 11, 15 y calcula el término de la posición 20.")

L(OA14, 3,
  mat="Lápiz y papel. Pueden servir fichas o monedas de un tipo.",
  use="Aprenderé a elegir la mejor estrategia para descubrir una regla, incluso cuando la sucesión se multiplica o mezcla operaciones. Sirve para predecir con seguridad.",
  prior=["Sé encontrar reglas de suma y de resta.", "Sé multiplicar y dividir con las tablas."],
  explain=[
      "Algunas sucesiones se multiplican. En 2, 4, 8, 16 cada término es el doble del anterior: la regla es «multiplicar por 2». En 81, 27, 9, 3 cada término es la tercera parte del anterior: la regla es «dividir por 3».",
      "Para elegir la estrategia, prueba primero la diferencia entre términos. Si las diferencias no son iguales, prueba con el cociente: divide un término por el anterior. En 3, 6, 12, 24 las diferencias son 3, 6 y 12, pero los cocientes son siempre 2.",
      "Con la regla puedes predecir, pero también verificar si un número pertenece a la sucesión. En 5, 10, 15, … el 60 pertenece porque 60 se obtiene al contar de 5 en 5. El 62 no pertenece, porque no termina en 0 ni en 5.",
  ],
  vocab=[("doble", "dos veces una cantidad"), ("cociente", "resultado de una división"), ("pertenecer", "estar dentro de la sucesión"), ("verificar", "comprobar que algo es correcto")],
  worked=[
      ("Sucesión que se multiplica", "Descubre la regla de 3, 6, 12, 24 y escribe los dos términos que siguen.", ["Las diferencias son 3, 6 y 12: no son iguales.", "Los cocientes 6 ÷ 3, 12 ÷ 6 y 24 ÷ 12 son siempre 2: la regla es multiplicar por 2. Siguen 48 y 96."], "Regla: ×2. Siguen 48 y 96"),
      ("¿Pertenece a la sucesión?", "¿El número 62 pertenece a la sucesión 5, 10, 15, 20, …?", ["La regla es sumar 5, así que todos los términos terminan en 0 o en 5.", "62 termina en 2."], "No pertenece"),
  ],
  mist=[
      ("Decir que 3, 6, 12, 24 suma 3, 6, 12 (sumas distintas).", "Se fija solo en las diferencias y no ve que se duplica.", "Divide: 6 ÷ 3, 12 ÷ 6 y 24 ÷ 12 siempre dan 2."),
      ("Pensar que 62 pertenece a 5, 10, 15, … porque es mayor.", "Se mira solo el tamaño y no la regla.", "Revisa cómo terminan los términos: solo hay cifras 0 y 5."),
  ],
  R=[ex("¿Qué número sigue en 2, 4, 8, 16?", "32", "La regla es multiplicar por 2."),
     ex("¿Cuál es la regla de 81, 27, 9, 3?", "Dividir por 3", "Cada término es la tercera parte del anterior."),
     ex("¿Qué número sigue en 1, 3, 5, 7?", "9", "La regla es sumar 2.")],
  C=[ex("En 3, 6, 12, 24, las diferencias, ¿son siempre iguales?", "No", "Las diferencias son 3, 6 y 12."),
     ex("¿Qué número sigue en 5, 10, 20, 40?", "80", "La regla es multiplicar por 2.", calc="40*2"),
     ex("¿Qué número sigue en 1.000, 100, 10?", "1", "La regla es dividir por 10.")],
  A=[ex("Continúa con los tres términos que siguen: 2, 6, 18, …", "54, 162, 486", "La regla es multiplicar por 3."),
     ex("Continúa con los dos términos que siguen: 800, 400, 200, …", "100, 50", "La regla es dividir por 2."),
     ex("Continúa con los dos términos que siguen: 7, 14, 21, 28, …", "35, 42", "La regla es sumar 7.")],
  Z=[ex("¿Pertenece el 78 a la sucesión 5, 10, 15, 20, …?", "No", "Los términos terminan en 0 o en 5, y 78 termina en 8."),
     ex("¿Pertenece el 96 a la sucesión 3, 6, 12, 24, 48, …?", "Sí", "La regla es ×2 y 48 × 2 = 96.")],
  D=[ex("La sucesión empieza con 2 y cada término es el doble del anterior. ¿Cuál es el sexto término?", "64", "2, 4, 8, 16, 32, 64.", calc="2*2*2*2*2*2"),
     ex("En la sucesión 1.000, 500, 250, ¿cuál es el término que sigue a 250?", "125", "250 dividido por 2 es 125.", calc="250//2")],
  ctx=[ex("Al doblar una hoja de papel por la mitad, las capas se duplican. Después de 1 doblez hay 2 capas. ¿Cuántas capas hay después de 4 dobleces?", "16", "2, 4, 8, 16.")],
  chk=[ex("¿Qué número sigue en 4, 8, 16?", "32", "Se multiplica por 2."),
       ex("¿Qué regla tiene 64, 32, 16?", "Dividir por 2", "Cada término es la mitad del anterior."),
       ex("¿Pertenece el 55 a la sucesión 5, 10, 15, …?", "Sí", "55 = 5 × 11.")],
  open=("Elige una de estas sucesiones: 3, 9, 27, … o 4, 12, 20, 28, …. Escribe la regla, tres términos que siguen y explica cómo decidiste si había que sumar o multiplicar.",
        "3, 9, 27: regla ×3. Siguen 81, 243, 729. Decidí multiplicar porque las diferencias (6 y 18) no son iguales, pero 9 ÷ 3 y 27 ÷ 9 sí dan 3.",
        ["identifica la regla", "continúa bien", "explica cómo eligió la operación"],
        ["regla", "términos", "explicación"],
        ["usar solo la diferencia", "no probar el cociente"],
        "Pide que compare dos estrategias. Reconoce la justificación."),
  reinforce="Escribe una sucesión que se multiplique por 2 empezando desde 1 hasta 6 términos.",
  extend="Escribe una sucesión que pertenezca y otra que no pertenezca, con la misma regla.")

L(OA14, 4,
  mat="Lápiz y papel.",
  use="Aprenderé a usar la regla de una sucesión en casos nuevos: con números grandes, con sucesiones decrecientes y con una condición especial. Sirve para decidir si una predicción es posible.",
  prior=["Sé descubrir reglas de suma, resta y multiplicación.", "Sé comprobar una regla con todos los términos."],
  explain=[
      "Cuando la sucesión baja, la regla es una resta y puede llegar a un límite. Si empiezas en 40 y restas 6, obtienes 40, 34, 28, 22, 16, 10, 4: el siguiente paso, 4 − 6, ya no se puede hacer sin pasar de 0. Así que la sucesión termina en 4.",
      "Cuando hay una condición nueva, adapta la regla. Por ejemplo: «parte en 3, suma 4, pero el máximo permitido es 40». Puedes continuar mientras no pases el máximo.",
      "Para decidir si un número aparece, resta el primer término y revisa si la diferencia se puede formar con saltos de la misma regla. En 3, 7, 11, … el 31 aparece porque 31 − 3 = 28 y 28 es 7 veces 4.",
  ],
  vocab=[("límite", "valor que no se puede pasar"), ("natural", "número 0, 1, 2, 3, … sin decimales ni negativos"), ("salto", "lo que cambia de un término al siguiente"), ("condición", "restricción que debe cumplirse")],
  worked=[
      ("Sucesión con límite", "Parte en 40 y resta 6 cada vez, sin pasar de 0. ¿Cuántos términos tiene la sucesión?", ["Escribo: 40, 34, 28, 22, 16, 10, 4.", "A 4 no se le puede restar 6 sin pasar de 0. Hay 7 términos."], "7 términos"),
      ("¿Aparece el 31?", "¿Aparece 31 en 3, 7, 11, …?", ["31 − 3 = 28.", "28 ÷ 4 = 7: se necesitan 7 saltos de 4 desde el primer término."], "Sí, aparece (es el 8.º término)"),
  ],
  mist=[
      ("Continuar 40, 34, 28, …, 4 con un término más.", "No se mira que 4 es menor que 6 y la resta pasaría de 0.", "Detén la sucesión en el último natural."),
      ("Pensar que 31 no aparece en 3, 7, 11 porque 31 no termina en 3 o 7.", "Se usa una regla de cómo terminan, que no funciona aquí.", "Resta el primer término y revisa si la diferencia es múltiplo de 4."),
  ],
  R=[ex("¿Qué número sigue en 40, 34, 28?", "22", "La regla es restar 6."),
     ex("La regla de 10, 7, 4, 1 es restar 3. ¿Se puede escribir un término más sin pasar de 0? Responde sí o no.", "No", "A 1 no se le puede restar 3 sin pasar de 0."),
     ex("¿Qué número sigue en 9, 18, 27?", "36", "La regla es sumar 9.")],
  C=[ex("¿Cuántos términos tiene la sucesión 40, 34, 28, 22, 16, 10, 4?", "7", "Se cuentan uno por uno."),
     ex("Una sucesión parte en 50 y resta 8. ¿Cuántos términos hay sin pasar de 0?", "7", "50, 42, 34, 26, 18, 10, 2; a 2 no se le pueden restar 8."),
     ex("¿Aparece el 43 en la sucesión 3, 7, 11, 15, …?", "Sí", "43 − 3 = 40, que es 10 veces 4.")],
  A=[ex("Una sucesión parte en 100 y resta 15. ¿Cuál es el último término sin pasar de 0?", "10", "100, 85, 70, 55, 40, 25, 10; a 10 no se le pueden restar 15."),
     ex("¿Aparece 50 en la sucesión 2, 7, 12, 17, …?", "No", "50 − 2 = 48 y 48 no es múltiplo de 5."),
     ex("Una sucesión parte en 3, suma 4 y no puede pasar de 30. ¿Cuál es el último término?", "27", "3, 7, 11, 15, 19, 23, 27; 31 se pasa de 30.")],
  Z=[ex("Julieta dice que 48 aparece en 6, 12, 18, 24, …. ¿Tiene razón?", "Sí", "48 es 8 veces 6."),
     ex("Dos sucesiones empiezan en 10: una suma 3 y otra suma 4. ¿Cuál llega primero a 30 o más?", "La que suma 4", "Con +4 se llega a 30 en 5 pasos (10, 14, 18, 22, 26, 30) y con +3 se llega a 31 en 7 pasos.")],
  D=[ex("¿Aparece el 100 en la sucesión que parte en 4 y suma 6?", "Sí", "100 − 4 = 96 y 96 ÷ 6 = 16, un número entero de saltos."),
     ex("Una sucesión parte en 2 y suma 5. ¿Cuántos términos son menores que 40?", "8", "2, 7, 12, 17, 22, 27, 32, 37; el siguiente, 42, ya no.")],
  ctx=[ex("Lucía parte con $9.000 y gasta $2.000 cada semana. ¿Cuántas semanas completas puede gastar sin que le falte plata?", "4 semanas", "Le quedan 7.000, 5.000, 3.000 y 1.000; una quinta semana necesitaría 2.000.")],
  chk=[ex("¿Aparece el 21 en la sucesión 3, 6, 9, …?", "Sí", "21 = 3 × 7."),
       ex("Una sucesión parte en 20 y resta 3. ¿Cuál es el último término sin pasar de 0?", "2", "20, 17, 14, 11, 8, 5, 2."),
       ex("¿Cuántos términos tiene 12, 9, 6, 3, 0?", "5", "Se cuentan del 12 al 0.")],
  open=("Parte en 5 y suma 6 cada vez. Escribe los primeros 6 términos, decide si 41 aparece y si 100 aparece, y explica cómo lo averiguaste.",
        "5, 11, 17, 23, 29, 35. 41 aparece: 41 − 5 = 36 = 6 × 6. 100 no aparece: 100 − 5 = 95 y 95 no es múltiplo de 6.",
        ["escribe los términos", "usa la diferencia múltiplo del salto", "explica con palabras"],
        ["lista de términos", "respuestas y explicación"],
        ["usar solo cómo terminan los números", "no restar el primer término"],
        "Pide que justifique con el múltiplo del salto. Reconoce el método."),
  reinforce="Escribe una sucesión que parta en 30 y baje de 4 en 4 hasta llegar a un número natural.",
  extend="Inventa una sucesión con un límite y pregunta a otra persona hasta dónde llega.")
