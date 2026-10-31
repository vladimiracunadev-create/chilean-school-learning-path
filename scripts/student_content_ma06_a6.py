"""Cuaderno del estudiante de 6.º básico Matemática: OA 11 (ecuaciones de primer grado) y OA 12 (construcción y clasificación de triángulos)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma06_a import M, W, lesson, task

OA11 = "MA06 OA 11"

# ------------------------------------------------------------------ OA 11 clase 1
lesson(
    OA11, 1,
    use="Aprenderé a resolver ecuaciones sencillas pensando en una balanza en equilibrio. Sirve para entender por qué lo que haces en un lado de la igualdad lo debes hacer en el otro.",
    prior=["Sé qué es una ecuación y su solución.", "Sé comprobar una solución reemplazando."],
    explain=[
        "Una balanza en equilibrio sirve de modelo para una ecuación. Los dos platos pesan lo mismo, como los dos lados de una igualdad. Una bolsa cuyo peso no conocemos es x. La ecuación x + 4 = 9 se ve como una bolsa y 4 pesas en un plato y 9 pesas en el otro.",
        "Para encontrar el peso de la bolsa, puedes quitar la misma cantidad de ambos platos y la balanza sigue en equilibrio. Quitas 4 pesas de cada lado: queda la bolsa sola en un plato y 5 pesas en el otro. Entonces x = 5. Si quitas pesas de un solo plato, la balanza se desequilibra.",
        "Si hay varias bolsas iguales, repartes igual en ambos lados. Para 2x = 14, dos bolsas iguales pesan 14, y una bolsa pesa la mitad: x = 7. La regla de oro es hacer siempre lo mismo en los dos platos. Al final comprueba reemplazando el valor en la ecuación.",
    ],
    vocab=[("equilibrio", "estado en que dos cantidades son iguales, como los platos de una balanza"), ("incógnita", "peso o número que se quiere encontrar"), ("quitar lo mismo", "restar la misma cantidad en ambos lados"), ("repartir igual", "dividir ambos lados por el mismo número"), ("solución", "valor que hace verdadera la ecuación")],
    worked=[
        W("Quitar lo mismo de ambos platos", "En una balanza en equilibrio hay una bolsa x y 4 pesas en un plato, y 9 pesas en el otro. ¿Cuánto pesa la bolsa? (Pesas de 1 kg cada una.)", ["Ecuación: x + 4 = 9.", "Quito 4 pesas de cada plato: queda x en un plato y 9 − 4 = 5 en el otro.", "Compruebo: 5 + 4 = 9."], "5 kg"),
        W("Repartir en partes iguales", "Dos bolsas iguales pesan lo mismo que 14 pesas de 1 kg. ¿Cuánto pesa cada bolsa?", ["Ecuación: 2x = 14.", "Divido ambos platos en 2 grupos iguales: una bolsa y 14 ÷ 2 pesas.", "Compruebo: 2 × 7 = 14."], "7 kg"),
    ],
    mistakes=[
        M("Quitar 3 pesas de un plato y ninguna del otro, y decir que la balanza sigue igual.", "Se rompió el equilibrio.", "Lo que se quita de un plato se debe quitar del otro."),
        M("Resolver x + 6 = 15 como x = 15 + 6.", "Se hizo la operación contraria al revés, sumando en vez de quitar.", "Se quitan 6 de ambos lados: x = 15 − 6 = 9."),
    ],
    rec=[
        ex("En una balanza en equilibrio hay una bolsa y 2 pesas de 1 kg en un plato, y 7 pesas en el otro. ¿Cuánto pesa la bolsa?", "5 kg", "Se quitan 2 pesas de cada plato."),
        ex("Resuelve x + 5 = 12.", "x = 7", "12 − 5 = 7."),
        ex("Si en una balanza en equilibrio se quitan 3 pesas de un plato y ninguna del otro, ¿sigue en equilibrio? Responde sí o no.", "No", "Los platos dejan de pesar lo mismo."),
    ],
    und=[
        ex("Resuelve x + 6 = 15.", "x = 9", "Se quitan 6 de ambos lados."),
        ex("Resuelve 3x = 18.", "x = 6", "Se reparte 18 en 3 grupos iguales."),
        ex("Una balanza tiene dos bolsas iguales y 4 pesas de 1 kg en un plato y 10 pesas en el otro. ¿Cuánto pesa cada bolsa?", "3 kg", "Se quitan 4 pesas de cada lado, quedan dos bolsas y 6 pesas; 6 ÷ 2 = 3."),
    ],
    app=[
        ex("En un plato hay una bolsa de arroz y 8 pesas de 1 kg; en el otro hay 20 pesas. ¿Cuánto pesa la bolsa?", "12 kg", "20 − 8 = 12."),
        ex("En un plato hay 2 bolsas iguales y 3 pesas de 1 kg; en el otro hay 17 pesas. ¿Cuánto pesa cada bolsa?", "7 kg", "17 − 3 = 14 y 14 ÷ 2 = 7."),
        ex("En un plato hay 4 cajas iguales y en el otro hay 28 kg. ¿Cuántos kg pesa cada caja?", "7 kg", "28 ÷ 4 = 7."),
    ],
    rea=[
        ex("Lía quitó 3 pesas del plato izquierdo y 5 del derecho, y dice que sigue en equilibrio. ¿Tiene razón? Responde sí o no.", "No", "Se debe quitar la misma cantidad en ambos platos."),
        ex("En x + 9 = 15 se quitan 9 de cada lado. ¿Qué número queda en el plato derecho?", "6", "15 − 9 = 6."),
    ],
    cha=[
        ex("Resuelve 2x + 3 = 11 pensando en una balanza.", "x = 4", "Quitas 3 de cada lado, queda 2x = 8, y x = 4."),
        ex("Un plato tiene 3 bolsas y 2 pesas; el otro tiene 1 bolsa y 10 pesas. Todas las bolsas son iguales. ¿Cuánto pesa una bolsa?", "4", "Quitas 1 bolsa de cada lado: 2 bolsas y 2 pesas equilibran 10 pesas; luego 2 bolsas son 8 y una bolsa es 4."),
    ],
    ctx=[ex("En una feria ficticia, un plato tiene una bolsa de arroz y una pesa de 2 kg, y el otro tiene dos pesas de 5 kg. ¿Cuánto pesa la bolsa?", "8 kg", "Dos pesas de 5 kg son 10 kg y 10 − 2 = 8.")],
    sc=[
        ex("Resuelve x + 8 = 13.", "x = 5", "13 − 8 = 5."),
        ex("Resuelve 4x = 20.", "x = 5", "20 ÷ 4 = 5."),
        ex("Si a un plato de una balanza en equilibrio le agregas 2 pesas iguales, ¿qué debes hacer para que siga en equilibrio?", "Agregar 2 pesas iguales al otro plato", "Lo que se hace en un lado se hace en el otro."),
    ],
    op=task(
        "Dibuja en tu cuaderno una balanza en equilibrio para la ecuación 3x + 2 = 14 (tres bolsas iguales y 2 pesas de 1 kg en un plato, 14 pesas en el otro). Escribe qué quitas de cada lado, qué repartes y cuánto pesa cada bolsa. Comprueba reemplazando.",
        "Quito 2 pesas de cada plato: 3x = 12. Reparto 12 en 3 grupos iguales: cada bolsa pesa 4 kg. Compruebo: 3 × 4 + 2 = 14.",
        ["dibuja la balanza", "hace lo mismo en los dos platos", "comprueba la solución"],
        ["dibujo de la balanza", "pasos escritos y comprobación"],
        ["quitar solo de un lado", "olvidar repartir en partes iguales"],
        "Pide que explique en voz alta por qué la balanza sigue en equilibrio después de cada paso.",
    ),
    reinforce="Resuelve x + 7 = 11, 2x = 10 y 2x + 1 = 9 con ayuda de una balanza dibujada.",
    extend="Inventa una balanza con dos bolsas iguales y algunas pesas en cada plato, escribe la ecuación y resuélvela.",
)

# ------------------------------------------------------------------ OA 11 clase 2
lesson(
    OA11, 2,
    use="Aprenderé a resolver ecuaciones descomponiendo números y haciendo corresponder uno a uno los términos de cada lado. Sirve para resolver sin tanto cálculo.",
    prior=["Sé resolver ecuaciones con una balanza.", "Sé descomponer números en sumandos."],
    explain=[
        "En la ecuación 3x + 2 = 14 hay dos términos a la izquierda: 3x y 2. Para hacerlos corresponder con la derecha, descompón el 14 en dos sumandos de modo que uno sea 2: 14 = 12 + 2. Ahora los lados se parecen: 3x + 2 = 12 + 2. El 2 corresponde al 2, así que 3x corresponde a 12.",
        "Si 3x es 12, piensa qué número multiplicado por 3 da 12: x = 4. Esa idea de hacer corresponder término con término se llama correspondencia uno a uno. Sirve cuando el número se puede descomponer de forma cómoda. Si no, usarás los procedimientos de la próxima clase.",
        "Para comprobar, reemplaza x por 4 en la ecuación original: 3 × 4 + 2 = 14. Si no coincide, revisa la descomposición. Descomponer bien es el paso clave: el sumando que corresponde al número suelto debe ser exactamente igual a ese número.",
    ],
    vocab=[("descomponer", "separar un número en sumandos"), ("correspondencia uno a uno", "hacer coincidir cada término de un lado con el del otro"), ("término", "cada parte de una suma en una expresión"), ("coeficiente", "número que multiplica a la letra, como el 3 en 3x"), ("comprobar", "reemplazar para ver que se cumple la igualdad")],
    worked=[
        W("Descomponer el lado derecho", "Resuelve 2x + 3 = 13.", ["Descompongo 13 = 10 + 3.", "Entonces 2x + 3 = 10 + 3, y el 3 corresponde al 3.", "2x = 10, así que x = 5. Compruebo: 2 × 5 + 3 = 13."], "x = 5"),
        W("Otra ecuación", "Resuelve 4x + 7 = 31.", ["Descompongo 31 = 24 + 7.", "4x corresponde a 24.", "x = 6. Compruebo: 4 × 6 + 7 = 31."], "x = 6"),
    ],
    mistakes=[
        M("Descomponer 13 como 8 + 3 en 2x + 3 = 13.", "El sumando que no es 3 debería ser 10, porque 8 + 3 = 11.", "Revisa que la descomposición sume 13: 10 + 3."),
        M("Resolver 3x + 2 = 14 como x = 14 − 2 = 12.", "Se olvidó que 3x es tres veces x.", "3x = 12 y x = 12 ÷ 3 = 4."),
    ],
    rec=[
        ex("Descompón 15 como un sumando más 4. ¿Cuál es el otro sumando?", "11", "11 + 4 = 15."),
        ex("En 3x + 5 = 17 se descompone 17 = ? + 5. ¿Qué número va en lugar del signo de interrogación?", "12", "12 + 5 = 17."),
        ex("Si 3x = 12, ¿cuánto vale x?", "4", "3 × 4 = 12."),
    ],
    und=[
        ex("Resuelve x + 9 = 20.", "x = 11", "20 = 11 + 9."),
        ex("Resuelve 5x + 2 = 27.", "x = 5", "27 = 25 + 2 y 5x = 25."),
        ex("Resuelve 2x + 6 = 18.", "x = 6", "18 = 12 + 6 y 2x = 12."),
    ],
    app=[
        ex("Una persona tiene 3 cajas iguales de lápices y 4 lápices sueltos; en total tiene 22 lápices. ¿Cuántos lápices hay en cada caja?", "6", "3x + 4 = 22; 22 = 18 + 4 y 3x = 18."),
        ex("Un taller cobra $2.000 fijos más 3 veces un precio por hora x. Un trabajo costó $8.000. ¿Cuánto es el precio por hora?", "$2.000", "2.000 + 3x = 8.000; 8.000 = 6.000 + 2.000 y 3x = 6.000."),
        ex("Resuelve 6x + 1 = 25.", "x = 4", "25 = 24 + 1 y 6x = 24."),
    ],
    rea=[
        ex("Ana resolvió 3x + 2 = 14 haciendo 14 − 2 = 12 y dijo que x = 12. ¿Cuál es el valor correcto de x?", "4", "3x = 12 y 12 ÷ 3 = 4."),
        ex("Para resolver 4x + 8 = 20, ¿es correcto descomponer 20 como 12 + 8? Responde sí o no.", "Sí", "12 + 8 = 20 y 4x corresponde a 12."),
    ],
    cha=[
        ex("Resuelve 7x + 3 = 38.", "x = 5", "38 = 35 + 3."),
        ex("Resuelve 2x + x + 4 = 19.", "x = 5", "2x + x = 3x; 19 = 15 + 4, y 3x = 15."),
    ],
    ctx=[ex("En una escuela ficticia se reparten 4 cajas iguales de lápices y 6 lápices más a un curso, con un total de 50 lápices. ¿Cuántos lápices tiene cada caja?", "11", "4x + 6 = 50; 50 = 44 + 6 y 4x = 44.")],
    sc=[
        ex("Resuelve x + 14 = 30.", "x = 16", "30 = 16 + 14."),
        ex("Resuelve 8x + 4 = 36.", "x = 4", "36 = 32 + 4."),
        ex("Resuelve 9x + 5 = 50.", "x = 5", "50 = 45 + 5."),
    ],
    op=task(
        "Resuelve estas tres ecuaciones usando descomposición: 5x + 4 = 29, 3x + 7 = 28 y 6x + 5 = 41. Para cada una escribe la descomposición del número de la derecha, qué término corresponde a qué, y comprueba.",
        "5x + 4 = 29: 29 = 25 + 4, x = 5. 3x + 7 = 28: 28 = 21 + 7, x = 7. 6x + 5 = 41: 41 = 36 + 5, x = 6. Compruebo: 5 × 5 + 4 = 29; 3 × 7 + 7 = 28; 6 × 6 + 5 = 41.",
        ["descompone bien el número", "hace corresponder los términos", "comprueba cada solución"],
        ["tres descomposiciones", "tres comprobaciones"],
        ["descomponer sin que sume", "olvidar dividir por el coeficiente"],
        "Pide que verifique que cada descomposición suma el número original.",
    ),
    reinforce="Resuelve 2x + 5 = 15, 4x + 1 = 13 y 5x + 3 = 28 por descomposición.",
    extend="Explica con un ejemplo por qué la descomposición funciona mejor cuando los números son cómodos y qué harías si no lo fueran, como en 7x + 2 = 100.",
)

# ------------------------------------------------------------------ OA 11 clase 3
lesson(
    OA11, 3,
    use="Aprenderé el procedimiento formal para resolver ecuaciones de primer grado: aplicar operaciones inversas a ambos lados. Sirve para resolver cualquier ecuación de este tipo, aunque los números sean difíciles.",
    prior=["Sé resolver ecuaciones con una balanza y por descomposición.", "Sé que sumar y restar son operaciones inversas, igual que multiplicar y dividir."],
    explain=[
        "El procedimiento formal usa operaciones inversas. Si algo se suma, se resta; si se resta, se suma; si se multiplica, se divide; si se divide, se multiplica. Siempre se hace lo mismo en los dos lados de la igualdad, para mantener el equilibrio. En x − 7 = 9 se suma 7 a ambos lados: x = 16.",
        "Para ecuaciones de dos pasos como 5x − 8 = 27, primero se deshace la suma o la resta: sumas 8 a ambos lados y queda 5x = 35. Luego se deshace la multiplicación: divides ambos lados por 5 y queda x = 7. En x ÷ 3 + 2 = 9, primero restas 2 (x ÷ 3 = 7) y después multiplicas por 3 (x = 21).",
        "Si hay letras en los dos lados, como en 5x = 2x + 9, resta la misma cantidad de x en ambos lados para dejar la letra en uno solo: 3x = 9. Escribe cada paso en una línea nueva y anota la operación que hiciste a cada lado. Al final, comprueba reemplazando en la ecuación original. Si no se cumple, revisa el orden: primero se deshacen las sumas y restas y después las multiplicaciones y divisiones.",
    ],
    vocab=[("operación inversa", "operación que deshace a otra"), ("ambos lados", "los dos miembros de la igualdad"), ("despejar", "dejar la letra sola en un lado"), ("paso", "cada línea del procedimiento"), ("comprobar", "reemplazar la solución en la ecuación original")],
    worked=[
        W("Ecuación de dos pasos", "Resuelve 5x − 8 = 27.", ["Sumo 8 a ambos lados: 5x = 35.", "Divido ambos lados por 5: x = 7.", "Compruebo: 5 × 7 − 8 = 27."], "x = 7"),
        W("Ecuación con división", "Resuelve x ÷ 3 + 2 = 9.", ["Resto 2 a ambos lados: x ÷ 3 = 7.", "Multiplico ambos lados por 3: x = 21.", "Compruebo: 21 ÷ 3 + 2 = 9."], "x = 21"),
    ],
    mistakes=[
        M("Resolver 4x + 8 = 32 dividiendo 32 ÷ 4 = 8 y luego restando 8.", "Se dividió antes de deshacer la suma y se alteró el orden.", "Primero resta 8 a ambos lados (4x = 24) y luego divide por 4: x = 6."),
        M("Hacer una operación en un solo lado.", "Se rompe la igualdad.", "Lo que se hace a un lado se hace al otro."),
    ],
    rec=[
        ex("Resuelve x − 7 = 9.", "x = 16", "Se suma 7 a ambos lados."),
        ex("Resuelve x ÷ 4 = 6.", "x = 24", "Se multiplica por 4 a ambos lados."),
        ex("Para resolver 8x = 56, ¿por qué número se divide a ambos lados?", "8", "El inverso de multiplicar por 8 es dividir por 8."),
    ],
    und=[
        ex("Resuelve 6x − 4 = 20.", "x = 4", "6x = 24 y x = 4."),
        ex("Resuelve x ÷ 5 + 1 = 4.", "x = 15", "x ÷ 5 = 3 y x = 15."),
        ex("Resuelve 9x + 5 = 68.", "x = 7", "9x = 63 y x = 7."),
    ],
    app=[
        ex("Sofía pagó $6.600 por 3 cuadernos iguales y $1.200 de transporte. ¿Cuánto cuesta cada cuaderno?", "$1.800", "3c + 1.200 = 6.600; 3c = 5.400 y c = 1.800."),
        ex("Un número dividido por 6 y aumentado en 4 da 10. ¿Cuál es el número?", "36", "x ÷ 6 + 4 = 10; x ÷ 6 = 6 y x = 36."),
        ex("Resuelve 12x − 5 = 79.", "x = 7", "12x = 84 y x = 7."),
    ],
    rea=[
        ex("Tomás resolvió 4x + 8 = 32 así: 32 ÷ 4 = 8, 8 − 8 = 0. ¿Cuál es la solución correcta?", "x = 6", "4x = 24 y x = 6."),
        ex("Ana divide todos los términos de 4x + 8 = 32 por 4 y obtiene x + 2 = 8. ¿Llega a la misma solución? Responde sí o no.", "Sí", "x = 6 en ambos casos."),
    ],
    cha=[
        ex("Resuelve x ÷ 2 − 3 = 5.", "x = 16", "x ÷ 2 = 8 y x = 16."),
        ex("Resuelve 7x − 12 = 3x + 8.", "x = 5", "Restas 3x: 4x − 12 = 8; 4x = 20 y x = 5."),
    ],
    ctx=[ex("Una niña tiene ahorrados $9.000 y ahorra la misma cantidad cada semana. En 5 semanas tendrá $24.000. ¿Cuánto ahorra cada semana?", "$3.000", "9.000 + 5x = 24.000; 5x = 15.000 y x = 3.000.")],
    sc=[
        ex("Resuelve x − 12 = 30.", "x = 42", "Se suma 12 a ambos lados."),
        ex("Resuelve 5x − 10 = 35.", "x = 9", "5x = 45."),
        ex("Resuelve x ÷ 7 + 3 = 8.", "x = 35", "x ÷ 7 = 5 y x = 35."),
    ],
    op=task(
        "Resuelve con el procedimiento formal, escribiendo una línea por paso y la operación que haces a ambos lados: 7x + 6 = 55, x ÷ 4 − 2 = 6 y 10x − 9 = 71. Comprueba cada solución reemplazando.",
        "7x + 6 = 55: resto 6, 7x = 49, divido por 7, x = 7. x ÷ 4 − 2 = 6: sumo 2, x ÷ 4 = 8, multiplico por 4, x = 32. 10x − 9 = 71: sumo 9, 10x = 80, x = 8. Compruebo: 7 × 7 + 6 = 55; 32 ÷ 4 − 2 = 6; 10 × 8 − 9 = 71.",
        ["usa operaciones inversas", "hace lo mismo en ambos lados", "comprueba cada solución"],
        ["tres procedimientos con pasos", "tres comprobaciones"],
        ["cambiar el orden de los pasos", "operar solo un lado"],
        "Pide que mire cada línea y nombre la operación inversa que usó.",
    ),
    reinforce="Resuelve x + 9 = 20, 3x = 27 y 2x − 5 = 11 con el procedimiento formal.",
    extend="Inventa una ecuación de dos pasos cuya solución sea x = 12 y pide a alguien que la resuelva. Explica cómo la construiste.",
)

# ------------------------------------------------------------------ OA 11 clase 4
lesson(
    OA11, 4,
    use="Aprenderé a plantear y resolver problemas con ecuaciones que incluyen paréntesis y situaciones nuevas. Sirve para resolver problemas de dinero, medidas y números.",
    prior=["Sé resolver ecuaciones de dos pasos.", "Sé traducir frases a expresiones con letras."],
    explain=[
        "Para resolver un problema con una ecuación sigue estos pasos: define la letra, traduce la historia a una ecuación, resuélvela con operaciones inversas y comprueba la respuesta en el problema. A veces la historia lleva un paréntesis. «El doble de la suma de un número y 3 es 20» se escribe 2(x + 3) = 20.",
        "Para resolver una ecuación con paréntesis, puedes dividir primero ambos lados por el número que multiplica al paréntesis: x + 3 = 10, y luego restar: x = 7. Otra forma es distribuir: 2x + 6 = 20, restar 6 y dividir por 2. Las dos maneras dan el mismo resultado.",
        "Cuando termines, responde la pregunta con unidades y comprueba que el resultado tiene sentido: no puedes tener personas con coma ni un precio negativo. Reemplaza la solución en la historia, no solo en la ecuación.",
    ],
    vocab=[("paréntesis", "signo que agrupa lo que se calcula junto"), ("distribuir", "multiplicar el número de afuera por cada término del paréntesis"), ("definir la letra", "decir qué representa x en el problema"), ("operación inversa", "operación que deshace a otra"), ("verificar en el problema", "comprobar que la solución cumple la historia")],
    worked=[
        W("Ecuación con paréntesis", "El doble de la suma de un número y 3 es 20. ¿Cuál es el número?", ["Ecuación: 2(x + 3) = 20.", "Divido ambos lados por 2: x + 3 = 10.", "Resto 3: x = 7. Compruebo: 2 × (7 + 3) = 20."], "x = 7"),
        W("Problema de compras", "Pagué con $20.000 y me devolvieron $4.000. Compré 4 poleras iguales. ¿Cuánto cuesta cada una?", ["Sea p el precio de una polera. Ecuación: 4p + 4.000 = 20.000.", "Resto 4.000: 4p = 16.000.", "Divido por 4: p = 4.000."], "$4.000"),
    ],
    mistakes=[
        M("Resolver 2(x + 3) = 20 como 2x + 3 = 20.", "El 2 multiplica a todo el paréntesis, no solo a x.", "2(x + 3) = 2x + 6 o se divide por 2 para tener x + 3 = 10."),
        M("Dar x = 7 sin explicar qué significa.", "No se interpretó la solución en la historia.", "Escribe la respuesta con las unidades del problema."),
    ],
    rec=[
        ex("Si 3(x + 1) = 15, ¿cuánto vale x + 1?", "5", "15 ÷ 3 = 5."),
        ex("Si x + 4 = 9, ¿cuánto vale x?", "5", "9 − 4."),
        ex("Escribe «el triple de un número es 24».", "3x = 24", "El triple de x es 3x."),
    ],
    und=[
        ex("Resuelve 5(x + 2) = 35.", "x = 5", "x + 2 = 7."),
        ex("Resuelve 4(x − 1) = 20.", "x = 6", "x − 1 = 5."),
        ex("Un número aumentado en 6 y multiplicado por 3 da 27. ¿Cuál es el número?", "3", "3(x + 6) = 27; x + 6 = 9 y x = 3."),
    ],
    app=[
        ex("Cuatro amigos pagan en partes iguales una cuenta de $24.000 más $4.000 de propina. ¿Cuánto paga cada uno?", "$7.000", "24.000 + 4.000 = 28.000 y 28.000 ÷ 4 = 7.000."),
        ex("Una persona compra 3 entradas iguales y paga además $2.500 de servicio. En total paga $14.500. ¿Cuánto cuesta cada entrada?", "$4.000", "3x + 2.500 = 14.500; 3x = 12.000 y x = 4.000."),
        ex("El perímetro de un cuadrado es 36 cm. ¿Cuánto mide su lado?", "9 cm", "Los cuatro lados son iguales: 36 ÷ 4 = 9."),
    ],
    rea=[
        ex("Eva resolvió 2(x + 3) = 20 como 2x + 3 = 20. ¿Cuál es el valor correcto de x?", "7", "2(x + 3) = 20 da x + 3 = 10 y x = 7."),
        ex("¿Es x = 4 solución de 3(x + 1) = 15? Responde sí o no.", "Sí", "3 × (4 + 1) = 3 × 5 = 15, la igualdad es verdadera."),
    ],
    cha=[
        ex("En un rectángulo el largo es 5 cm mayor que el ancho y el perímetro es 34 cm. ¿Cuánto mide el ancho?", "6 cm", "2x + 2(x + 5) = 34; 4x + 10 = 34; 4x = 24 y x = 6."),
        ex("Tres hermanos tienen edades consecutivas y entre los tres suman 42 años. ¿Cuántos años tiene el menor?", "13", "x + (x + 1) + (x + 2) = 42; 3x = 39 y x = 13."),
    ],
    ctx=[ex("Una pastelería ficticia vende cajas con x galletas cada una. Se llevan 5 cajas y 3 galletas sueltas, es decir 5x + 3 = 58 galletas. ¿Cuántas galletas tiene cada caja?", "11", "5x = 55 y x = 11.")],
    sc=[
        ex("Resuelve 6(x + 1) = 30.", "x = 4", "x + 1 = 5."),
        ex("Resuelve 8x + 4 = 52.", "x = 6", "8x = 48."),
        ex("Escribe «el doble de un número, más 5, es 21».", "2x + 5 = 21", "El doble de x es 2x."),
    ],
    op=task(
        "Resuelve este problema con una ecuación: «En una tienda ficticia se compran 3 libros iguales y un lápiz de $900. Se paga con un billete de $20.000 y se reciben $4.100 de vuelto». Define la letra, escribe la ecuación, resuélvela con operaciones inversas y comprueba en el problema.",
        "Sea x el precio de un libro. Lo gastado es 20.000 − 4.100 = 15.900, entonces 3x + 900 = 15.900. Resto 900: 3x = 15.000 y x = 5.000. Compruebo: 3 × 5.000 + 900 + 4.100 = 20.000.",
        ["define la letra", "plantea la ecuación correcta", "resuelve y comprueba en el problema"],
        ["definición de la incógnita", "ecuación resuelta y comprobación"],
        ["no restar el vuelto", "olvidar el lápiz"],
        "Pide que sume lo gastado y el vuelto para comprobar que da $20.000.",
    ),
    reinforce="Resuelve 2(x + 4) = 18 de dos maneras: dividiendo primero y distribuyendo primero.",
    extend="Escribe un problema que lleve a la ecuación 3(x + 2) = 27 y resuélvelo.",
)

# ================================================================== OA 12
OA12 = "MA06 OA 12"

# ------------------------------------------------------------------ OA 12 clase 1
lesson(
    OA12, 1,
    use="Aprenderé a clasificar triángulos según la medida de sus lados. Sirve para describir y construir triángulos con precisión.",
    prior=["Sé qué es un triángulo y sus elementos: lados, vértices y ángulos.", "Sé medir segmentos con una regla."],
    explain=[
        "Un triángulo tiene 3 lados, 3 vértices y 3 ángulos. Según la medida de sus lados, se clasifica en tres tipos. Un triángulo equilátero tiene los tres lados iguales. Un triángulo isósceles tiene exactamente dos lados iguales. Un triángulo escaleno tiene los tres lados de medidas distintas.",
        "Para clasificar, mide los tres lados con una regla y compara. Si los lados miden 5 cm, 5 cm y 5 cm, es equilátero. Si miden 6 cm, 6 cm y 4 cm, es isósceles. Si miden 3 cm, 4 cm y 5 cm, es escaleno. El perímetro es la suma de las medidas de los tres lados.",
        "El nombre depende solo de cuántos lados iguales hay, y no del tamaño. Un equilátero pequeño y uno grande son del mismo tipo. Al nombrar los lados, el lado distinto de un isósceles se suele llamar base. Siempre incluye la unidad de medida, como centímetros.",
    ],
    vocab=[("triángulo equilátero", "triángulo con los tres lados iguales"), ("triángulo isósceles", "triángulo con exactamente dos lados iguales"), ("triángulo escaleno", "triángulo con los tres lados distintos"), ("perímetro", "suma de las medidas de todos los lados"), ("base", "lado distinto de un triángulo isósceles")],
    worked=[
        W("Clasificar por lados", "Clasifica los triángulos de lados: A) 5 cm, 5 cm, 5 cm; B) 6 cm, 6 cm, 4 cm; C) 3 cm, 4 cm, 5 cm.", ["A: los tres lados iguales, equilátero.", "B: dos lados iguales (6 y 6), isósceles.", "C: los tres lados distintos, escaleno."], "A equilátero, B isósceles, C escaleno"),
        W("Perímetro de un triángulo", "Calcula el perímetro del triángulo C: 3 cm, 4 cm y 5 cm.", ["Sumo las medidas de los tres lados.", "3 + 4 + 5 = 12."], "12 cm"),
    ],
    mistakes=[
        M("Decir que un triángulo de lados 3, 4 y 5 es isósceles.", "Se pensó que cualquier triángulo con 3 lados es isósceles.", "Los tres lados son distintos: es escaleno."),
        M("Decir que un triángulo equilátero grande es isósceles.", "Se confundió el tamaño con el tipo.", "El tipo depende de los lados iguales: tres iguales, equilátero."),
    ],
    rec=[
        ex("¿Cuántos lados iguales tiene un triángulo equilátero?", "3", "Sus tres lados miden lo mismo."),
        ex("Un triángulo tiene lados de 7 cm, 7 cm y 3 cm. ¿Qué tipo de triángulo es por sus lados?", "Isósceles", "Tiene exactamente dos lados iguales."),
        ex("Un triángulo tiene lados de 4 cm, 5 cm y 6 cm. ¿Qué tipo de triángulo es por sus lados?", "Escaleno", "Los tres lados son distintos."),
    ],
    und=[
        ex("Un triángulo equilátero tiene lados de 8 cm. ¿Cuántos centímetros mide su perímetro?", "24 cm", "8 + 8 + 8 = 24."),
        ex("Un triángulo isósceles tiene dos lados de 9 cm y la base de 5 cm. ¿Cuánto mide su perímetro?", "23 cm", "9 + 9 + 5 = 23."),
        ex("Un triángulo tiene lados de 12 cm, 9 cm y 12 cm. ¿Qué tipo de triángulo es por sus lados?", "Isósceles", "Dos lados miden 12 cm y el otro, 9 cm."),
    ],
    app=[
        ex("Un triángulo tiene dos lados de 6 cm y otro de 10 cm. ¿Cuánto mide el lado distinto?", "10 cm", "Es un isósceles y el lado distinto es el de 10 cm."),
        ex("Un triángulo tiene lados de 5 cm, 7 cm y 9 cm. ¿Qué tipo de triángulo es y cuánto mide su perímetro?", "Escaleno, 21 cm", "Los lados son distintos y 5 + 7 + 9 = 21."),
        ex("Un triángulo isósceles tiene perímetro 20 cm y su lado distinto mide 8 cm. ¿Cuánto mide cada lado igual?", "6 cm", "20 − 8 = 12 y 12 ÷ 2 = 6."),
    ],
    rea=[
        ex("Pía dice que un triángulo de lados 8, 9 y 10 cm es isósceles porque tiene 3 lados. ¿Qué tipo de triángulo es?", "Escaleno", "Sus tres lados son distintos."),
        ex("Un triángulo tiene lados de 5 cm, 5 cm y 5 cm. ¿Puede ser escaleno? Responde sí o no.", "No", "Sus tres lados son iguales, entonces es equilátero."),
    ],
    cha=[
        ex("Un triángulo equilátero tiene perímetro 36 cm. ¿Cuánto mide cada lado?", "12 cm", "36 ÷ 3 = 12."),
        ex("Tres números consecutivos son las medidas de los lados de un triángulo y suman 15 cm. ¿Cuáles son?", "4, 5 y 6", "4 + 5 + 6 = 15; es un triángulo escaleno."),
    ],
    ctx=[ex("Una bandera triangular ficticia tiene lados de 40 cm, 40 cm y 30 cm. ¿Qué tipo de triángulo es por sus lados?", "Isósceles", "Dos lados miden 40 cm y el otro, 30 cm.")],
    sc=[
        ex("¿Qué tipo de triángulo tiene sus tres lados distintos?", "Escaleno", "Escaleno significa sin lados iguales."),
        ex("Un triángulo tiene lados de 10 cm, 10 cm y 10 cm. ¿Cuántos centímetros mide su perímetro?", "30 cm", "10 + 10 + 10."),
        ex("Un triángulo tiene lados de 8 cm, 3 cm y 8 cm. ¿Qué tipo es?", "Isósceles", "Dos lados son iguales."),
    ],
    op=task(
        "Mide con una regla tres objetos con forma triangular o dibuja tres triángulos con estas medidas: A) 6 cm, 6 cm y 6 cm; B) 7 cm, 7 cm y 4 cm; C) 5 cm, 6 cm y 8 cm. Escribe el tipo de cada uno por sus lados y calcula su perímetro.",
        "A: equilátero, 18 cm. B: isósceles, 18 cm. C: escaleno, 19 cm.",
        ["clasifica por sus lados", "calcula el perímetro", "usa unidad de medida"],
        ["tabla con tipo y perímetro", "medidas escritas con unidad"],
        ["confundir isósceles con escaleno", "olvidar la unidad"],
        "Pide que cuente cuántos lados son iguales antes de nombrar el triángulo.",
    ),
    reinforce="Clasifica los triángulos de lados 4-4-4, 5-5-8 y 3-5-7 y calcula su perímetro.",
    extend="Explica con tus palabras por qué un triángulo equilátero también puede describirse como un triángulo con todos sus lados iguales, y dibuja uno de 6 cm de lado.",
)

# ------------------------------------------------------------------ OA 12 clase 2
lesson(
    OA12, 2,
    use="Aprenderé a clasificar triángulos según la medida de sus ángulos. Sirve para describir cómo se abre cada vértice y para reconocer ángulos rectos.",
    prior=["Sé qué es un ángulo y que se mide en grados con un transportador.", "Sé reconocer ángulos agudos, rectos y obtusos."],
    explain=[
        "Un ángulo agudo mide menos de 90°, un ángulo recto mide exactamente 90° y un ángulo obtuso mide más de 90° y menos de 180°. Según sus ángulos, un triángulo se clasifica en tres tipos. Un triángulo acutángulo tiene sus tres ángulos agudos. Un triángulo rectángulo tiene un ángulo recto. Un triángulo obtusángulo tiene un ángulo obtuso.",
        "Para clasificar, mide los tres ángulos con un transportador. Si los ángulos miden 50°, 60° y 70°, todos son agudos: el triángulo es acutángulo. Si miden 90°, 35° y 55°, tiene un ángulo recto: es rectángulo. Si miden 120°, 30° y 30°, tiene un ángulo obtuso: es obtusángulo.",
        "Un truco para reconocer un ángulo recto es compararlo con la esquina de una hoja o de una escuadra. Las clasificaciones por lados y por ángulos son distintas: un mismo triángulo tiene un nombre de cada tipo. Un triángulo no tiene dos ángulos rectos ni dos obtusos, porque los tres ángulos de un triángulo suman 180°.",
    ],
    vocab=[("triángulo acutángulo", "triángulo con tres ángulos agudos"), ("triángulo rectángulo", "triángulo con un ángulo recto"), ("triángulo obtusángulo", "triángulo con un ángulo obtuso"), ("ángulo recto", "ángulo de 90°, como la esquina de una hoja"), ("grado", "unidad para medir ángulos: °")],
    worked=[
        W("Clasificar por ángulos", "Clasifica los triángulos con ángulos: A) 50°, 60°, 70°; B) 90°, 35°, 55°; C) 120°, 30°, 30°.", ["A: los tres ángulos son menores que 90°, acutángulo.", "B: tiene un ángulo de 90°, rectángulo.", "C: 120° es mayor que 90°, obtusángulo."], "A acutángulo, B rectángulo, C obtusángulo"),
        W("Reconocer el ángulo que decide", "Un triángulo tiene ángulos de 100°, 40° y 40°. ¿Qué ángulo decide su tipo?", ["100° es mayor que 90°, es un ángulo obtuso.", "Con un ángulo obtuso, el triángulo es obtusángulo."], "El de 100°: obtusángulo"),
    ],
    mistakes=[
        M("Decir que un triángulo con ángulos 80°, 85° y 15° es rectángulo.", "Se confundió casi recto con recto.", "Ningún ángulo mide exactamente 90°: todos son agudos, es acutángulo."),
        M("Clasificar por lados un triángulo con ángulos conocidos.", "Se mezclaron los dos criterios.", "Para clasificar por ángulos mira solo las medidas de los ángulos."),
    ],
    rec=[
        ex("¿Cuánto mide un ángulo recto?", "90°", "Es la esquina de una hoja."),
        ex("Un ángulo mide 45°. ¿Es agudo, recto u obtuso?", "Agudo", "45° es menor que 90°."),
        ex("Un ángulo mide 130°. ¿Es agudo, recto u obtuso?", "Obtuso", "130° está entre 90° y 180°."),
    ],
    und=[
        ex("Un triángulo tiene ángulos de 40°, 60° y 80°. ¿Qué tipo de triángulo es por sus ángulos?", "Acutángulo", "Sus tres ángulos son agudos."),
        ex("Un triángulo tiene ángulos de 90°, 40° y 50°. ¿Qué tipo de triángulo es por sus ángulos?", "Rectángulo", "Tiene un ángulo recto."),
        ex("Un triángulo tiene ángulos de 110°, 35° y 35°. ¿Qué tipo de triángulo es por sus ángulos?", "Obtusángulo", "110° es un ángulo obtuso."),
    ],
    app=[
        ex("Una escuadra de dibujo tiene ángulos de 90°, 45° y 45°. ¿Qué tipo de triángulo es por sus ángulos?", "Rectángulo", "Tiene un ángulo de 90°."),
        ex("Un techo triangular ficticio tiene ángulos de 70°, 55° y 55°. ¿Qué tipo de triángulo es por sus ángulos?", "Acutángulo", "Los tres ángulos son menores que 90°."),
        ex("Un triángulo tiene ángulos de 20°, 30° y 130°. ¿Cuál es el ángulo obtuso?", "130°", "Es el único mayor que 90°."),
    ],
    rea=[
        ex("Luis dice que un triángulo con ángulos de 80°, 85° y 15° es rectángulo porque 85° es casi 90°. ¿Qué tipo de triángulo es?", "Acutángulo", "Ninguno mide exactamente 90°, todos son agudos."),
        ex("¿Puede un triángulo tener dos ángulos rectos? Responde sí o no.", "No", "Los tres ángulos de un triángulo suman 180°; dos ángulos rectos ya suman 180° y no quedaría nada para el tercero."),
    ],
    cha=[
        ex("Un triángulo tiene un ángulo de 90°. Los otros dos ángulos miden lo mismo y suman 90°. ¿Cuánto mide cada uno?", "45°", "90° ÷ 2 = 45°."),
        ex("Ángulos de un triángulo: 60°, 60° y 60°. ¿Qué tipo de triángulo es por sus ángulos?", "Acutángulo", "Los tres ángulos son menores que 90°."),
    ],
    ctx=[ex("Un marco triangular ficticio de madera tiene una esquina que calza exactamente con la esquina de una hoja de cuaderno. ¿Qué tipo de triángulo es por sus ángulos?", "Rectángulo", "La esquina de la hoja mide 90°.")],
    sc=[
        ex("Un triángulo con un ángulo de 100°, ¿es acutángulo, rectángulo u obtusángulo?", "Obtusángulo", "100° es obtuso."),
        ex("Un triángulo con ángulos de 30°, 70° y 80°, ¿es acutángulo, rectángulo u obtusángulo?", "Acutángulo", "Todos son agudos."),
        ex("Un ángulo mide 90°. ¿Es agudo, recto u obtuso?", "Recto", "90° es un ángulo recto."),
    ],
    op=task(
        "Con estas tres listas de ángulos, dibuja o imagina cada triángulo y clasifícalo por sus ángulos: A) 55°, 55° y 70°; B) 90°, 30° y 60°; C) 25°, 125° y 30°. Escribe para cada uno el ángulo que decide el tipo y explica cómo reconocerías un ángulo recto con una hoja.",
        "A: acutángulo (todos menores que 90°). B: rectángulo (decide 90°). C: obtusángulo (decide 125°). Un ángulo recto calza con la esquina de una hoja.",
        ["clasifica por ángulos", "nombra el ángulo que decide", "reconoce el recto con una hoja"],
        ["tres clasificaciones", "frase sobre el ángulo recto"],
        ["confundir casi recto con recto", "mezclar con la clasificación por lados"],
        "Pide que compare cada ángulo con 90° y diga si es menor, igual o mayor.",
    ),
    reinforce="Clasifica los triángulos con ángulos 60°-60°-60°, 90°-50°-40° y 100°-40°-40°.",
    extend="Busca en tu casa una esquina de 90° y compárala con el ángulo de un triángulo de papel que dibujes. Explica cómo decides si es recto, agudo u obtuso.",
)

# ------------------------------------------------------------------ OA 12 clase 3
lesson(
    OA12, 3,
    use="Aprenderé a construir triángulos con regla, compás y transportador a partir de medidas de lados o ángulos. Sirve para dibujar figuras exactas.",
    prior=["Sé clasificar triángulos por lados y ángulos.", "Sé usar regla y transportador."],
    explain=[
        "Para construir un triángulo conociendo sus tres lados usa regla y compás. Por ejemplo, con lados de 6 cm, 4 cm y 5 cm: primero traza con la regla un segmento de 6 cm. Abre el compás a 4 cm, pon la punta en un extremo y traza un arco. Abre el compás a 5 cm, pon la punta en el otro extremo y traza otro arco. Donde se cruzan los arcos está el tercer vértice. Únelo con los extremos.",
        "Si conoces un lado y los ángulos de sus extremos, usa regla y transportador. Traza el lado, mide cada ángulo en un extremo con el transportador y traza las semirrectas hasta que se crucen. Si conoces dos lados y el ángulo entre ellos, dibuja el ángulo y marca las medidas sobre sus brazos. Después une los extremos.",
        "No siempre se puede construir un triángulo con tres medidas cualquiera. Con lados de 3 cm, 3 cm y 8 cm, los arcos de 3 cm no se alcanzan a cruzar: los dos lados cortos no llegan a cerrar la figura. Para que se pueda, la suma de los dos lados más cortos debe ser mayor que el lado más largo. Tampoco bastan los ángulos solos: ángulos de 60°, 60° y 60° sirven para triángulos de muchos tamaños.",
    ],
    vocab=[("compás", "instrumento para trazar arcos y circunferencias"), ("transportador", "instrumento para medir ángulos en grados"), ("arco", "parte de una circunferencia"), ("vértice", "punto donde se juntan dos lados"), ("semirrecta", "recta que empieza en un punto y sigue sin fin")],
    worked=[
        W("Construir con tres lados", "Describe cómo construir un triángulo de lados 6 cm, 4 cm y 5 cm.", ["Con la regla traza un segmento de 6 cm.", "Con el compás abierto 4 cm y centro en un extremo, traza un arco; con el compás abierto 5 cm y centro en el otro extremo, traza otro arco.", "Une el punto donde se cruzan los arcos con los dos extremos."], "Triángulo escaleno de 6 cm, 4 cm y 5 cm"),
        W("Comprobar si se puede construir", "¿Se puede construir un triángulo de lados 3 cm, 3 cm y 8 cm?", ["Los dos lados de 3 cm suman 6 cm.", "6 cm es menor que 8 cm, los arcos no se cruzan."], "No se puede"),
    ],
    mistakes=[
        M("Medir el ángulo con la regla.", "La regla mide longitudes y no ángulos.", "Los ángulos se miden con el transportador."),
        M("Creer que cualquier tres medidas forman un triángulo.", "No se comprobó si los lados cortos alcanzan.", "La suma de dos lados debe ser mayor que el tercero."),
    ],
    rec=[
        ex("¿Qué instrumento se usa para trazar un arco con una abertura de 4 cm?", "El compás", "El compás se abre a la medida pedida."),
        ex("¿Qué instrumento se usa para medir un ángulo?", "El transportador", "Mide en grados."),
        ex("¿Qué instrumento se usa para trazar un segmento de 5 cm?", "La regla", "La regla mide longitudes."),
    ],
    und=[
        ex("Para construir un triángulo de lados 4, 5 y 6 cm se hacen tres pasos: A) trazar arcos de 4 cm y 5 cm desde los extremos; B) trazar el lado de 6 cm; C) unir el cruce de los arcos con los extremos. ¿Cuál es el orden correcto?", "B, A, C", "Primero el lado base, luego los arcos y al final se une."),
        ex("En un triángulo construido con compás, el arco de 4 cm con centro en un extremo contiene todos los puntos que están a ¿cuántos centímetros de ese extremo?", "4 cm", "Todos los puntos de un arco están a la misma distancia del centro."),
        ex("Se traza un lado de 5 cm y desde cada extremo se traza un arco con el compás abierto 5 cm. ¿Cuántos lados iguales tendrá el triángulo?", "3", "Los tres lados miden 5 cm: es equilátero."),
    ],
    app=[
        ex("¿Se puede construir un triángulo de lados 3 cm, 3 cm y 8 cm? Responde sí o no.", "No", "3 + 3 = 6 es menor que 8; los arcos no se cruzan."),
        ex("¿Se puede construir un triángulo de lados 5 cm, 6 cm y 10 cm? Responde sí o no.", "Sí", "5 + 6 = 11 es mayor que 10."),
        ex("Quieres construir un triángulo con un lado de 6 cm y ángulos de 50° y 70° en sus extremos. ¿Qué instrumento necesitas para los ángulos?", "El transportador", "Mide ángulos en grados."),
    ],
    rea=[
        ex("Luis dice que se puede construir un triángulo con lados 2 cm, 3 cm y 7 cm porque son tres medidas. ¿Es cierto? Responde sí o no.", "No", "2 + 3 = 5 es menor que 7."),
        ex("Con solo saber que los tres ángulos miden 60°, ¿hay un único tamaño de triángulo? Responde sí o no.", "No", "Hay triángulos con ángulos 60° de muchos tamaños."),
    ],
    cha=[
        ex("Un triángulo tiene lados de 5 cm, 5 cm y x cm, con x un número entero positivo. ¿Cuántos valores de x permiten construirlo?", "9", "x debe ser menor que 5 + 5 = 10: son 1, 2, 3, 4, 5, 6, 7, 8 y 9."),
        ex("Un triángulo isósceles tiene perímetro 15 cm y sus dos lados iguales miden 6 cm. ¿Cuánto mide el tercer lado?", "3 cm", "15 − 6 − 6 = 3."),
    ],
    ctx=[ex("Un carpintero ficticio dispone de varillas de 30 cm, 40 cm y 50 cm. ¿Puede armar un triángulo con ellas? Responde sí o no.", "Sí", "30 + 40 = 70 es mayor que 50, entonces los lados se cierran.")],
    sc=[
        ex("¿Qué instrumento se usa para marcar un punto que esté a 3 cm de otro y trazar un arco?", "El compás", "Se abre a 3 cm."),
        ex("¿Se puede construir un triángulo de lados 4 cm, 4 cm y 4 cm? Responde sí o no.", "Sí", "4 + 4 = 8 es mayor que 4."),
        ex("¿Se puede construir un triángulo de lados 1 cm, 2 cm y 6 cm? Responde sí o no.", "No", "1 + 2 = 3 es menor que 6."),
    ],
    op=task(
        "Construye en tu cuaderno, con regla y compás, un triángulo de lados 7 cm, 5 cm y 6 cm, siguiendo los pasos de la explicación. Luego mide sus tres ángulos con un transportador, clasifícalo por lados y por ángulos y explica con una frase por qué los arcos se cruzan.",
        "Se traza el lado de 7 cm y se hacen arcos de 5 cm y 6 cm desde los extremos. Es escaleno (lados 7, 5 y 6 cm distintos). Sus ángulos son agudos, es acutángulo. Los arcos se cruzan porque 5 + 6 es mayor que 7.",
        ["sigue los pasos con regla y compás", "clasifica por lados y por ángulos", "explica por qué los arcos se cruzan"],
        ["triángulo dibujado", "medidas de los ángulos y clasificaciones"],
        ["abrir mal el compás", "medir los ángulos con la regla"],
        "Pide que mida los tres lados con la regla para comprobar que son los pedidos.",
    ),
    reinforce="Construye un triángulo de lados 4 cm, 4 cm y 6 cm y escribe su tipo por los lados.",
    extend="Dibuja un triángulo con un lado de 6 cm y ángulos de 45° y 45° en sus extremos. Clasifícalo por lados y por ángulos.",
)

# ------------------------------------------------------------------ OA 12 clase 4
lesson(
    OA12, 4,
    use="Aprenderé a combinar las dos clasificaciones de los triángulos (por lados y por ángulos) y a resolver casos nuevos. Sirve para describir un triángulo con exactitud.",
    prior=["Sé clasificar triángulos por lados.", "Sé clasificar triángulos por ángulos."],
    explain=[
        "Un mismo triángulo se puede describir de dos maneras: por sus lados y por sus ángulos. Un triángulo con ángulos de 60°, 60° y 60° y lados de 5 cm, 5 cm y 5 cm es equilátero y acutángulo. Un triángulo con lados de 3 cm, 4 cm y 5 cm y un ángulo de 90° es escaleno y rectángulo.",
        "No todas las combinaciones existen. Un triángulo equilátero siempre tiene tres ángulos de 60°, así que nunca es rectángulo. En cambio, un triángulo con ángulos de 90°, 45° y 45° tiene dos lados iguales: es isósceles y rectángulo. Un triángulo con un ángulo de 120° y otros dos de 30° es isósceles y obtusángulo.",
        "Para resolver un caso nuevo, pregúntate dos cosas: ¿cuántos lados iguales hay? y ¿cuál es el ángulo mayor, es agudo, recto u obtuso? Junta las dos respuestas para dar un nombre completo. Dibujar un esquema ayuda a ver las relaciones.",
    ],
    vocab=[("isósceles rectángulo", "triángulo con dos lados iguales y un ángulo recto"), ("escaleno rectángulo", "triángulo con tres lados distintos y un ángulo recto"), ("equilátero acutángulo", "triángulo con tres lados iguales y tres ángulos agudos"), ("clasificar", "agrupar según un criterio"), ("criterio", "regla para decidir en qué grupo va algo")],
    worked=[
        W("Dos clasificaciones a la vez", "Clasifica por lados y por ángulos un triángulo de lados 3 cm, 4 cm y 5 cm que tiene un ángulo de 90°.", ["Por lados: los tres lados son distintos, escaleno.", "Por ángulos: tiene un ángulo recto, rectángulo."], "Escaleno y rectángulo"),
        W("Descartar una combinación", "¿Puede un triángulo ser equilátero y rectángulo?", ["Un triángulo equilátero tiene tres ángulos de 60°.", "60° es agudo; no hay ningún ángulo de 90°."], "No puede ser equilátero y rectángulo"),
    ],
    mistakes=[
        M("Decir que un triángulo con ángulos de 90°, 45° y 45° es equilátero.", "Se miraron los ángulos pero no se razonó sobre los lados iguales.", "Tiene dos lados iguales, es isósceles; además es rectángulo."),
        M("Dar solo un nombre a un triángulo cuando se pide una descripción completa.", "No se aplicaron los dos criterios.", "Da un nombre por lados y otro por ángulos."),
    ],
    rec=[
        ex("Un triángulo tiene lados de 6 cm, 6 cm y 6 cm. ¿Qué tipo de triángulo es por sus lados?", "Equilátero", "Los tres lados son iguales."),
        ex("Un triángulo tiene ángulos de 90°, 20° y 70°. ¿Qué tipo de triángulo es por sus ángulos?", "Rectángulo", "Tiene un ángulo de 90°."),
        ex("Un triángulo tiene lados de 7 cm, 7 cm y 5 cm. ¿Cuántos lados iguales tiene?", "2", "Dos lados miden 7 cm."),
    ],
    und=[
        ex("Un triángulo tiene lados de 8 cm, 8 cm y 8 cm y ángulos de 60°. Clasifícalo por lados y por ángulos.", "Equilátero y acutángulo", "Tres lados iguales y tres ángulos agudos."),
        ex("Un triángulo tiene dos lados iguales y ángulos de 120°, 30° y 30°. Clasifícalo por lados y por ángulos.", "Isósceles y obtusángulo", "Dos lados iguales y un ángulo de 120°."),
        ex("Un triángulo tiene lados de 5 cm, 12 cm y 13 cm y un ángulo de 90°. Clasifícalo por lados y por ángulos.", "Escaleno y rectángulo", "Tres lados distintos y un ángulo recto."),
    ],
    app=[
        ex("Una escuadra tiene ángulos de 90°, 45° y 45°. ¿Es isósceles o escaleno?", "Isósceles", "Con dos ángulos iguales hay dos lados iguales."),
        ex("Una señal triangular ficticia tiene lados de 40 cm, 40 cm y 40 cm. ¿Qué tipo de triángulo es por sus lados?", "Equilátero", "Los tres lados son iguales."),
        ex("Un triángulo tiene lados de 6 cm, 6 cm y 9 cm. ¿Cuánto mide su perímetro y qué tipo es por lados?", "21 cm, isósceles", "6 + 6 + 9 = 21."),
    ],
    rea=[
        ex("Luis dice que un triángulo con ángulos de 90°, 45° y 45° es equilátero. ¿Qué tipo es por sus lados?", "Isósceles", "Dos ángulos iguales indican dos lados iguales."),
        ex("¿Puede un triángulo ser rectángulo y escaleno a la vez? Responde sí o no.", "Sí", "Un triángulo de lados 8, 15 y 17 cm con un ángulo de 90° lo muestra."),
    ],
    cha=[
        ex("Un triángulo equilátero tiene perímetro 27 cm. ¿Cuánto mide cada lado y cuánto mide cada ángulo?", "9 cm y 60°", "27 ÷ 3 = 9 y un triángulo equilátero tiene tres ángulos de 60°."),
        ex("Un triángulo isósceles obtusángulo tiene un ángulo de 120° y otros dos iguales de 30°. ¿Qué ángulo es el mayor?", "120°", "120° es mayor que 30°."),
    ],
    ctx=[ex("Una vela triangular ficticia tiene lados de 2 m, 2 m y 3 m y su ángulo mayor mide 97°. Clasifícala por lados y por ángulos.", "Isósceles y obtusángulo", "Dos lados iguales y un ángulo de 97°, que es mayor que 90°.")],
    sc=[
        ex("¿Puede un triángulo ser isósceles y rectángulo a la vez? Responde sí o no.", "Sí", "Por ejemplo, ángulos de 90°, 45° y 45°."),
        ex("Un triángulo tiene lados de 4 cm, 5 cm y 6 cm. ¿Es equilátero, isósceles o escaleno?", "Escaleno", "Los tres lados son distintos."),
        ex("Un triángulo tiene ángulos de 50°, 60° y 70°. ¿Es acutángulo, rectángulo u obtusángulo?", "Acutángulo", "Los tres ángulos son menores que 90°."),
    ],
    op=task(
        "Escribe en tu cuaderno la descripción completa (por lados y por ángulos) de estos tres triángulos: A) lados de 4 cm, 4 cm y 4 cm; B) dos lados de 5 cm y ángulos de 90°, 45° y 45°; C) lados de 6 cm, 8 cm y 10 cm con un ángulo de 90°. Después responde: ¿puede existir un triángulo equilátero y rectángulo a la vez? Explica por qué.",
        "A: equilátero y acutángulo (un equilátero tiene tres ángulos de 60°). B: isósceles y rectángulo. C: escaleno y rectángulo. Un triángulo equilátero y rectángulo no puede existir, porque el equilátero tiene tres ángulos de 60° y ninguno mide 90°.",
        ["aplica los dos criterios", "revisa si la combinación es posible", "explica con ángulos de 60°"],
        ["tabla de descripciones", "frase que explica lo imposible"],
        ["dar solo un nombre", "aceptar combinaciones imposibles"],
        "Pide que justifique cada nombre con el número de lados iguales y el ángulo mayor.",
    ),
    reinforce="Clasifica por lados y por ángulos: un triángulo de lados 3-3-3, otro de ángulos 90°-30°-60° y otro con un ángulo de 110°.",
    extend="Dibuja un triángulo isósceles rectángulo con regla y escuadra. Explica cómo sabes que es isósceles y rectángulo a la vez.",
)
