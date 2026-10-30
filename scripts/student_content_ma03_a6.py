"""Student material for 3.º básico Matemática, OA 09 (división como reparto y agrupación)."""
from __future__ import annotations

from student_content_ma03_a import task
from student_lessons import arith, ex, register

OA9 = "MA03 OA 09"

register(
    OA9, 1,
    materials="Lápiz, cuaderno y 20 tapas o porotos para repartir. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a repartir una cantidad en partes iguales y a escribirlo como división. Sirve para saber cuánto le toca a cada uno cuando se comparte.",
    prior=["Sé las tablas del 2, 5 y 10 y otras hasta 10 × 10.", "Sé que una multiplicación cuenta grupos iguales."],
    explain=[
        "Repartir en partes iguales es dar la misma cantidad a cada persona o a cada lugar. Si repartes 12 galletas entre 3 niños, vas dando una a cada uno, y otra, y otra, hasta que no queden. Al final cada niño tiene 4 galletas.",
        "Esto se escribe como división: 12 ÷ 3 = 4. El 12 es el total que se reparte. El 3 es entre cuántos se reparte. El 4 es lo que le toca a cada uno. El signo ÷ se lee «dividido en» o «dividido por».",
        "Para comprobar, mira que todos tengan lo mismo y que al juntar todo vuelvas al total: 4 + 4 + 4 = 12, o 3 × 4 = 12. Si alguien tiene más que otro, no es un reparto igual. Con las tapas puedes hacerlo con tus manos.",
    ],
    vocab=[("repartir", "dar la misma cantidad a cada uno"), ("partes iguales", "partes con la misma cantidad"), ("división", "operación que reparte o agrupa en partes iguales, se escribe con ÷"), ("total", "cantidad que se reparte"), ("cociente", "resultado de una división")],
    worked=[
        {"title": "Repartir galletas", "problem": "Reparte 12 galletas en partes iguales entre 3 niños. ¿Cuántas recibe cada uno?", "steps": ["Doy 1 galleta a cada niño, otra vuelta, y otra, hasta terminar las 12.", "Cada niño termina con 4 galletas.", "Compruebo: 3 × 4 = 12."], "answer": "4 galletas; 12 ÷ 3 = 4"},
        {"title": "Un reparto que no es igual", "problem": "Doy 5, 4 y 3 galletas a tres niños. ¿Es un reparto en partes iguales de las 12?", "steps": ["5, 4 y 3 son distintos.", "Para que sea igual, todos deben tener lo mismo.", "Debía ser 4, 4 y 4."], "answer": "No, no es igual"},
    ],
    mistakes=[
        {"wrong": "Responder 15 a 12 ÷ 3.", "why": "Se suma en vez de repartir.", "fix": "Pregunta: ¿cuánto le toca a cada uno si son 3? 4."},
        {"wrong": "Decir que 12 galletas entre 3 niños son 3 galletas cada uno.", "why": "Se confunde el número de niños con lo que recibe cada uno.", "fix": "Comprueba: 3 × 3 = 9, no 12. Cada uno recibe 4."},
    ],
    tiers={
        "recovery": [
            arith("Reparte 18 galletas en partes iguales entre 3 niños. ¿Cuántas recibe cada uno?", "18//3", "Cada niño recibe 6, porque 3 × 6 = 18."),
            ex("Se reparten 15 tapas por igual en 5 vasos. ¿Cuántas tapas hay en cada vaso?", "3", "5 × 3 = 15."),
            ex("Se reparten 10 lápices por igual en 2 cajas. ¿Cuántos lápices hay en cada caja?", "5", "2 × 5 = 10."),
        ],
        "understand": [
            ex("En 12 ÷ 3 = 4, ¿qué representa cada número?", "12 es el total, 3 los que reciben y 4 lo que recibe cada uno", "El total se reparte entre 3 y cada uno recibe 4."),
            ex("Reparto 10 tapas entre dos vasos: 7 en un vaso y 3 en el otro. ¿Es un reparto en partes iguales?", "No", "Las partes son distintas: debía haber 5 en cada vaso."),
            ex("Al repartir 20 entre 4, ¿cada parte es mayor o menor que 20? ¿Cuánto vale?", "Menor; 5", "Al repartir cada parte es menor que el total: 4 × 5 = 20."),
        ],
        "apply": [
            arith("Se reparten 24 stickers por igual entre 6 niños. ¿Cuántos recibe cada uno?", "24//6", "6 × 4 = 24."),
            arith("Se reparten 30 manzanas por igual en 5 canastos. ¿Cuántas hay en cada canasto?", "30//5", "5 × 6 = 30."),
            arith("Se reparten 36 manzanas en 9 bolsas iguales. ¿Cuántas hay en cada bolsa?", "36//9", "9 × 4 = 36."),
        ],
        "reason": [
            ex("Pedro repartió 18 caramelos entre 3 amigos y dio 5 a cada uno. ¿Está bien? ¿Cuántos corresponden a cada uno?", "No; corresponden 6", "3 × 5 = 15, no 18. Con 6: 3 × 6 = 18."),
            ex("¿Se pueden repartir 7 galletas enteras entre 2 niños en partes iguales sin que sobre alguna?", "No", "Ninguna tabla del 2 llega a 7: 2 × 3 = 6 y 2 × 4 = 8."),
        ],
        "challenge": [
            arith("Se ponen 72 sillas en 8 filas iguales. ¿Cuántas sillas hay en cada fila?", "72//8", "8 × 9 = 72."),
            arith("Se reparten 100 monedas de juguete por igual entre 10 niños. ¿Cuántas recibe cada uno?", "100//10", "10 × 10 = 100."),
        ],
    },
    context=[arith("Una profesora reparte 16 hojas por igual entre 4 mesas. ¿Cuántas hojas recibe cada mesa?", "16//4", "4 × 4 = 16.")],
    selfcheck=[
        arith("¿Cuánto es 20 ÷ 4?", "20//4", "4 × 5 = 20."),
        arith("¿Cuánto es 9 ÷ 3?", "9//3", "3 × 3 = 9."),
        arith("¿Cuánto es 18 ÷ 2?", "18//2", "2 × 9 = 18."),
    ],
    open_task=task(
        "Con 20 tapas haz tres repartos iguales: entre 2 vasos, entre 4 vasos y entre 5 vasos. Escribe la división de cada uno y cuántas tapas hay en cada vaso. Comprueba con una multiplicación.",
        "20 ÷ 2 = 10 (2 × 10 = 20). 20 ÷ 4 = 5 (4 × 5 = 20). 20 ÷ 5 = 4 (5 × 4 = 20).",
        ["hace los tres repartos", "escribe cada división", "da 10, 5 y 4", "comprueba con multiplicación"],
        ["tapas repartidas o dibujo", "divisiones escritas"],
        ["repartir sin igualar", "confundir el total con la parte"],
        "Reconoce los repartos y pregunta qué representa cada número; si hay error, que reparta de a una tapa.",
    ),
    reinforce="Reparte 12 tapas entre 2, 3, 4 y 6 vasos y anota cuántas quedan en cada vaso.",
    extend="¿Qué pasa con lo que recibe cada uno si reparte el mismo total entre más personas? Pruébalo con 12.",
)

register(
    OA9, 2,
    materials="Lápiz, cuaderno y 24 tapas para formar grupos. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a formar grupos de un tamaño dado y a contar cuántos grupos salen. Sirve para saber cuántas cajas o bolsas necesito.",
    prior=["Sé repartir en partes iguales y escribirlo como división.", "Sé las tablas de multiplicar."],
    explain=[
        "Agrupar es juntar los objetos en grupos del mismo tamaño y contar cuántos grupos salen. Si tienes 12 galletas y las pones en bolsas de 3, formas 4 bolsas. Aquí conoces el tamaño de cada grupo y buscas la cantidad de grupos.",
        "También se escribe 12 ÷ 3 = 4. Es la misma cuenta que antes, pero con otro significado. Cuando repartes, el 3 son las personas y el 4 lo que recibe cada una. Cuando agrupas, el 3 es el tamaño de cada grupo y el 4 son los grupos.",
        "Para agrupar, separa de a 3 hasta terminar y cuenta los grupos. Para comprobar, multiplica: 4 grupos de 3 son 4 × 3 = 12. Si sobran objetos, no se alcanzó a formar un grupo completo; por ahora trabajaremos con casos donde no sobra nada.",
    ],
    vocab=[("agrupar", "juntar en grupos del mismo tamaño"), ("tamaño del grupo", "cuántos objetos hay en cada grupo"), ("cantidad de grupos", "cuántos grupos salen"), ("división", "operación para repartir o agrupar"), ("comprobar", "revisar con una multiplicación")],
    worked=[
        {"title": "Armar bolsas", "problem": "Tengo 12 galletas y las pongo en bolsas de 3. ¿Cuántas bolsas armo?", "steps": ["Separo de 3 en 3: 3, 6, 9, 12.", "Cuento los grupos: 4.", "Compruebo: 4 × 3 = 12."], "answer": "4 bolsas; 12 ÷ 3 = 4"},
        {"title": "Reparto o agrupación", "problem": "A) 12 galletas entre 3 niños. B) 12 galletas en bolsas de 3. ¿Cuál es el reparto y cuál la agrupación?", "steps": ["En A conozco cuántos niños y busco lo que recibe cada uno.", "En B conozco el tamaño de la bolsa y busco cuántas bolsas.", "Los dos se escriben 12 ÷ 3 = 4."], "answer": "A es reparto y B es agrupación"},
    ],
    mistakes=[
        {"wrong": "Decir que 30 fichas en grupos de 6 forman 6 grupos.", "why": "Se confunde el tamaño del grupo con la cantidad de grupos.", "fix": "Comprueba: 6 grupos de 6 son 36. 5 grupos de 6 son 30."},
        {"wrong": "Contar los números dichos en vez de los grupos al separar de 3 en 3.", "why": "Se cuenta cada ficha, no cada grupo.", "fix": "Cuenta cuántos grupos de 3 se forman."},
    ],
    tiers={
        "recovery": [
            arith("Tengo 20 galletas y las pongo en bolsas de 4. ¿Cuántas bolsas armo?", "20//4", "5 grupos de 4 son 20."),
            ex("Se juntan 15 tapas en grupos de 5. ¿Cuántos grupos salen?", "3", "3 × 5 = 15."),
            ex("Se guardan 10 lápices en cajas de 2. ¿Cuántas cajas se usan?", "5", "5 × 2 = 10."),
        ],
        "understand": [
            ex("En 12 ÷ 3, si el 3 es el tamaño de cada grupo, ¿qué cuenta el resultado?", "Cuántos grupos salen", "El resultado es la cantidad de grupos."),
            ex("A) 20 tapas entre 4 vasos. B) 20 tapas en vasos de 4 tapas cada uno. ¿Cuál es el reparto y cuál la agrupación?", "A es reparto y B es agrupación", "En A se conoce la cantidad de vasos, en B el tamaño de cada grupo."),
            ex("Si hago grupos de 4 con 20 manzanas, ¿cuántos grupos salen?", "5", "5 × 4 = 20."),
        ],
        "apply": [
            arith("Se forman equipos de 8 niños con 24 niños. ¿Cuántos equipos salen?", "24//8", "3 × 8 = 24."),
            arith("Se hacen pilas de 9 cuadernos con 45 cuadernos. ¿Cuántas pilas salen?", "45//9", "5 × 9 = 45."),
            arith("Se arman cajas de 10 lápices con 60 lápices. ¿Cuántas cajas salen?", "60//10", "6 × 10 = 60."),
        ],
        "reason": [
            ex("Ema dice que 30 fichas en grupos de 6 son 6 grupos. Comprueba y corrige.", "Son 5 grupos", "5 × 6 = 30, y 6 × 6 = 36."),
            ex("Con 24 fichas, ¿salen más grupos si el tamaño es 2 o si es 4?", "Si el tamaño es 2", "Salen 12 grupos de 2 y 6 grupos de 4."),
        ],
        "challenge": [
            arith("Se hacen grupos de 7 con 56 estudiantes. ¿Cuántos grupos salen?", "56//7", "8 × 7 = 56."),
            ex("Con 36 fichas se pueden hacer grupos de 4, de 6 y de 9. ¿Cuántos grupos salen en cada caso?", "9, 6 y 4", "9 × 4 = 36, 6 × 6 = 36 y 4 × 9 = 36."),
        ],
    },
    context=[arith("En un museo caben 8 niños por mesa. Llegan 40 niños. ¿Cuántas mesas se necesitan?", "40//8", "5 × 8 = 40.")],
    selfcheck=[
        ex("Con 18 tapas hago grupos de 3. ¿Cuántos grupos salen?", "6", "6 × 3 = 18."),
        ex("Con 14 tapas hago grupos de 2. ¿Cuántos grupos salen?", "7", "7 × 2 = 14."),
        ex("Con 25 tapas hago grupos de 5. ¿Cuántos grupos salen?", "5", "5 × 5 = 25."),
    ],
    open_task=task(
        "Con 24 tapas forma grupos de 2, de 3, de 4 y de 6. Para cada tamaño escribe cuántos grupos salen y la división que lo muestra. Luego explica una diferencia entre repartir y agrupar.",
        "Grupos de 2: 12 grupos, 24 ÷ 2 = 12. De 3: 8 grupos, 24 ÷ 3 = 8. De 4: 6 grupos, 24 ÷ 4 = 6. De 6: 4 grupos, 24 ÷ 6 = 4. Al repartir sé entre cuántos reparto; al agrupar sé el tamaño de cada grupo.",
        ["forma los cuatro grupos", "da 12, 8, 6 y 4", "escribe cada división", "explica la diferencia"],
        ["tapas agrupadas o dibujo", "divisiones escritas"],
        ["confundir tamaño con cantidad de grupos", "dejar tapas sin agrupar"],
        "Reconoce los grupos y pregunta qué cuenta cada resultado; si hay error, que separe de a poco con tapas.",
    ),
    reinforce="Con 12 tapas haz bolsas de 2, de 3 y de 4 y escribe cuántas bolsas salen.",
    extend="¿Por qué al hacer grupos más grandes salen menos grupos? Pruébalo con 30 tapas.",
)

register(
    OA9, 3,
    materials="Lápiz y cuaderno. Todos los datos están escritos en cada ejercicio. Puedes usar tapas para ir sacando grupos.",
    use="Aprenderé a dividir restando el mismo número varias veces hasta llegar a cero. Sirve para ver paso a paso lo que ocurre cuando se saca un grupo tras otro.",
    prior=["Sé repartir y agrupar.", "Sé restar números hasta 100."],
    explain=[
        "Otra forma de dividir es quitar grupos iguales hasta que no quede nada. Con 12 galletas y bolsas de 3, sacas una bolsa: 12 − 3 = 9. Sacas otra: 9 − 3 = 6. Otra: 6 − 3 = 3. Otra más: 3 − 3 = 0. Quitaste 4 veces el 3.",
        "Eso es una sustracción repetida: restas el mismo número hasta llegar a 0. La cantidad de veces que restaste es el resultado de la división. Entonces 12 ÷ 3 = 4. Cuenta bien las restas, no los números que escribes, porque el número de partida también aparece.",
        "Compara con la multiplicación: sumar 3 cuatro veces da 12, y restar 3 cuatro veces desde 12 da 0. Son operaciones que se deshacen. Si al restar no llegas exactamente a 0, la cuenta no es una división exacta.",
    ],
    vocab=[("sustracción repetida", "restar el mismo número varias veces"), ("llegar a cero", "no quedar nada"), ("paso", "una de las restas"), ("división exacta", "división en que no sobra nada"), ("veces", "cantidad de restas que se hacen")],
    worked=[
        {"title": "Restar de a 3", "problem": "Calcula 12 ÷ 3 con resta repetida.", "steps": ["12 − 3 = 9.", "9 − 3 = 6, 6 − 3 = 3 y 3 − 3 = 0.", "Hice 4 restas.", "Entonces 12 ÷ 3 = 4."], "answer": "4"},
        {"title": "No llegar a cero", "problem": "¿Llegas a 0 restando 4 desde 18?", "steps": ["18 − 4 = 14, 14 − 4 = 10, 10 − 4 = 6, 6 − 4 = 2.", "Quedan 2 y no se puede restar 4 otra vez.", "No se llega a 0."], "answer": "No; queda 2"},
    ],
    mistakes=[
        {"wrong": "Contar los números 12, 9, 6, 3, 0 y decir que 12 ÷ 3 = 5.", "why": "Se cuentan los números escritos, no las restas.", "fix": "Cuenta las restas: son 4."},
        {"wrong": "Parar de restar antes de llegar a 0.", "why": "No se termina de sacar todos los grupos.", "fix": "Sigue hasta que no quede nada."},
    ],
    tiers={
        "recovery": [
            ex("Restando 5 desde 30 se escribe 30, 25, 20, 15, 10, 5, 0. ¿Cuántas veces restaste?", "6", "Hay 6 restas de 5; el 30 es el número de partida."),
            ex("¿Cuántas veces restas 5 desde 15 hasta llegar a 0?", "3", "15, 10, 5, 0: 3 restas."),
            ex("¿Cuántas veces restas 2 desde 10 hasta llegar a 0?", "5", "10, 8, 6, 4, 2, 0: 5 restas."),
        ],
        "understand": [
            ex("Si restas 4 desde 20 cinco veces llegas a 0. ¿Cuánto es 20 ÷ 4?", "5", "El resultado es la cantidad de restas."),
            ex("En 18 ÷ 6, ¿qué número restas cada vez?", "6", "Es el tamaño de cada grupo."),
            ex("Si al restar 7 desde 21 llegas a 0 en 3 pasos, ¿qué multiplicación lo confirma?", "3 × 7 = 21", "3 grupos de 7."),
        ],
        "apply": [
            ex("Escribe 24 ÷ 6 como resta repetida y di el resultado.", "24 − 6 − 6 − 6 − 6 = 0; el resultado es 4", "Cuatro restas de 6 llegan a 0."),
            arith("Calcula 35 ÷ 5 restando 5 hasta llegar a 0.", "35//5", "Se restan siete veces 5."),
            ex("Resta 9 desde 36 hasta llegar a 0. ¿Cuántas veces restas?", "4", "36, 27, 18, 9, 0."),
        ],
        "reason": [
            ex("Tomás restó 3 desde 12 y escribió 12, 9, 6, 3, 0. Dice que 12 ÷ 3 = 5 porque escribió cinco números. ¿Es correcto?", "No; son 4 restas", "El primer número no es una resta."),
            ex("Ana restó 4 desde 20 tres veces y dice que 20 ÷ 4 = 3. ¿Es correcto?", "No; faltan restas, el resultado es 5", "Después de tres restas quedan 8."),
        ],
        "challenge": [
            arith("Calcula 63 ÷ 9 con resta repetida de 9.", "63//9", "Se restan siete veces 9."),
            ex("¿Llegas a 0 restando 5 desde 23?", "No; queda 3", "23, 18, 13, 8, 3."),
        ],
    },
    context=[arith("Una caja tiene 40 galletas y se sacan 8 por día. ¿Cuántos días tardan en vaciarla?", "40//8", "Se resta 8 hasta llegar a 0.")],
    selfcheck=[
        ex("¿Cuántas veces restas 2 desde 8 hasta 0?", "4", "8, 6, 4, 2, 0."),
        ex("Con resta repetida, 15 ÷ 3 es:", "5", "5 restas de 3."),
        ex("¿Es 12 − 3 − 3 − 3 − 3 = 0 una resta repetida de 3?", "Sí", "Siempre se resta 3."),
    ],
    open_task=task(
        "Calcula con resta repetida: 18 ÷ 3, 20 ÷ 5 y 21 ÷ 7. Escribe la fila de restas de cada una y cuenta cuántas hiciste. Comprueba con una multiplicación.",
        "18 ÷ 3: 18, 15, 12, 9, 6, 3, 0; son 6 restas, 6 × 3 = 18. 20 ÷ 5: 20, 15, 10, 5, 0; son 4 restas, 4 × 5 = 20. 21 ÷ 7: 21, 14, 7, 0; son 3 restas, 3 × 7 = 21.",
        ["escribe las tres filas de restas", "cuenta las restas", "da 6, 4 y 3", "comprueba con multiplicación"],
        ["restas escritas", "multiplicaciones de comprobación"],
        ["contar el número de partida", "no llegar a 0"],
        "Reconoce las filas de restas y pregunta qué cuenta el resultado; si hay error, que saque grupos con tapas.",
    ),
    reinforce="Con 12 tapas, saca grupos de 2 y anota cuántas veces lo haces; repite con grupos de 4.",
    extend="¿Qué pasaría con 20 − 6 − 6 − 6? Explica por qué no llegas a 0.",
)

register(
    OA9, 4,
    materials="Lápiz y cuaderno. Todos los datos están escritos en cada ejercicio. Puedes dibujar un arreglo para ver la familia.",
    use="Aprenderé que dividir y multiplicar se relacionan, y usaré las tablas para dividir sin hacer cálculos largos. Sirve para recordar divisiones con las tablas que ya sé.",
    prior=["Sé las tablas de multiplicar.", "Sé repartir, agrupar y restar repetido."],
    explain=[
        "La multiplicación y la división se deshacen entre sí. Si 3 × 4 = 12, entonces 12 ÷ 3 = 4 y 12 ÷ 4 = 3. Los tres números forman una familia: 3, 4 y 12. El total es el 12, y los otros dos son los factores.",
        "Para dividir, pregúntate: ¿qué número multiplicado por el divisor da el total? En 56 ÷ 8, piensa 8 × ? = 56. Como 8 × 7 = 56, entonces 56 ÷ 8 = 7. No necesitas restar muchas veces si sabes la tabla.",
        "Un arreglo lo muestra bien: 3 filas de 4 puntos son 12 puntos. Si repartes los 12 puntos en 3 filas, caben 4 en cada una. Si los separas de a 4, salen 3 filas. Por eso 12 ÷ 3 = 4 y 12 ÷ 4 = 3.",
    ],
    vocab=[("operación inversa", "la que deshace a otra"), ("familia de operaciones", "multiplicaciones y divisiones con los mismos tres números"), ("factor", "cada número que se multiplica"), ("divisor", "número por el que se divide"), ("tabla", "lista de resultados de multiplicar un número por 1, 2, 3 hasta 10")],
    worked=[
        {"title": "De la multiplicación a la división", "problem": "Si 4 × 5 = 20, ¿cuánto es 20 ÷ 5 y cuánto 20 ÷ 4?", "steps": ["Los tres números son 4, 5 y 20.", "20 ÷ 5: ¿qué número por 5 da 20? 4.", "20 ÷ 4: ¿qué número por 4 da 20? 5."], "answer": "20 ÷ 5 = 4 y 20 ÷ 4 = 5"},
        {"title": "Usar la tabla para dividir", "problem": "Calcula 56 ÷ 8 sin restar.", "steps": ["Pienso 8 × ? = 56.", "En la tabla del 8, 8 × 7 = 56.", "Entonces 56 ÷ 8 = 7."], "answer": "7"},
    ],
    mistakes=[
        {"wrong": "Responder 35 a 30 ÷ 5.", "why": "Se suma porque se confunde con otra operación.", "fix": "Piensa en la tabla: 5 × ? = 30. Es 6."},
        {"wrong": "Pensar que 12 ÷ 3 y 3 ÷ 12 son lo mismo.", "why": "Se cambia el orden como en la multiplicación.", "fix": "En una división el orden importa: el total va primero."},
    ],
    tiers={
        "recovery": [
            ex("Si 3 × 8 = 24, ¿cuánto es 24 ÷ 8?", "3", "La división deshace la multiplicación."),
            ex("Si 6 × 3 = 18, ¿cuánto es 18 ÷ 6?", "3", "6 × 3 = 18."),
            ex("Si 7 × 2 = 14, escribe 14 ÷ 2.", "7", "2 × 7 = 14."),
        ],
        "understand": [
            ex("¿Qué multiplicación ayuda a calcular 42 ÷ 7?", "7 × 6 = 42 (o 6 × 7 = 42)", "7 × ? = 42."),
            ex("¿6 × 9 = 54 y 54 ÷ 6 = 9 son de la misma familia?", "Sí", "Usan los mismos números."),
            ex("Escribe las dos divisiones de la familia de 3, 4 y 12.", "12 ÷ 3 = 4 y 12 ÷ 4 = 3", "El total 12 se divide por cada factor."),
        ],
        "apply": [
            arith("Calcula 63 ÷ 7 usando la tabla del 7.", "63//7", "7 × 9 = 63."),
            arith("Calcula 48 ÷ 6 usando la tabla del 6.", "48//6", "6 × 8 = 48."),
            arith("Calcula 81 ÷ 9 usando la tabla del 9.", "81//9", "9 × 9 = 81."),
        ],
        "reason": [
            ex("Rosa dice que 30 ÷ 5 = 35. ¿Qué error cometió y cuál es el resultado?", "Sumó; es 6", "5 × 6 = 30."),
            ex("Si 8 × 7 = 56, ¿cuánto es 56 ÷ 7 y cuánto es 56 ÷ 8?", "8 y 7", "56 ÷ 7 = 8 y 56 ÷ 8 = 7."),
        ],
        "challenge": [
            ex("Completa: ___ × 6 = 42, entonces 42 ÷ 6 = ___.", "7 y 7", "7 × 6 = 42."),
            ex("Completa: 9 × ___ = 72, entonces 72 ÷ 9 = ___.", "8 y 8", "9 × 8 = 72."),
        ],
    },
    context=[arith("Una bodega tiene 100 lápices en cajas de 10. ¿Cuántas cajas hay?", "100//10", "10 × 10 = 100.")],
    selfcheck=[
        ex("Si 5 × 9 = 45, ¿cuánto es 45 ÷ 9?", "5", "9 × 5 = 45."),
        arith("¿Cuánto es 27 ÷ 3?", "27//3", "3 × 9 = 27."),
        ex("¿Qué multiplicación usas para calcular 40 ÷ 5?", "5 × 8 = 40", "5 × ? = 40."),
    ],
    open_task=task(
        "Escoge una de estas multiplicaciones: 6 × 7 = 42, 9 × 4 = 36 o 8 × 5 = 40. Dibuja un arreglo, escribe las dos divisiones de su familia y explica cómo las tablas te ayudaron.",
        "Elijo 9 × 4 = 36. Dibujo 9 filas de 4 puntos. Divisiones: 36 ÷ 9 = 4 y 36 ÷ 4 = 9. Para 36 ÷ 4 pensé 4 × 9 = 36.",
        ["elige una multiplicación", "dibuja el arreglo", "escribe las dos divisiones", "explica el uso de la tabla"],
        ["arreglo dibujado", "divisiones escritas", "explicación"],
        ["dividir en orden equivocado", "no usar la tabla"],
        "Reconoce el arreglo y pregunta cuál es el total; si hay error, que cuente los puntos por filas.",
    ),
    reinforce="Escribe la familia de 6, 4 y 24 con dos multiplicaciones y dos divisiones.",
    extend="¿Por qué saber la tabla del 7 sirve para dividir por 7?",
)

register(
    OA9, 5,
    materials="Lápiz y cuaderno. Todos los datos de los problemas están escritos. Puedes dibujar los grupos.",
    use="Aprenderé a resolver y a crear problemas de reparto y de agrupación con divisiones de las tablas. Sirve para decidir cuánto toca a cada uno o cuántos grupos salen.",
    prior=["Sé dividir con las tablas.", "Sé distinguir reparto de agrupación."],
    explain=[
        "En un problema de reparto conoces el total y cuántos reciben, y buscas lo que recibe cada uno. «20 dulces entre 4 niños» es 20 ÷ 4 = 5. En uno de agrupación conoces el total y el tamaño del grupo, y buscas cuántos grupos salen.",
        "«Bolsas de 5 con 20 dulces» es 20 ÷ 5 = 4 bolsas. Aunque los números sean parecidos, el significado de la respuesta cambia: en el reparto son dulces por niño; en la agrupación son bolsas. Escribe siempre la unidad de la respuesta.",
        "Si un problema tiene dos pasos, resuélvelo en orden: «24 estudiantes forman equipos de 6 y cada equipo recibe 3 pelotas» es 24 ÷ 6 = 4 equipos y luego 4 × 3 = 12 pelotas. Para inventar uno, elige una división y una historia con su pregunta.",
    ],
    vocab=[("problema de reparto", "problema donde se busca lo que recibe cada uno"), ("problema de agrupación", "problema donde se busca cuántos grupos salen"), ("dato", "número o información del problema"), ("pregunta", "lo que se quiere saber"), ("unidad", "lo que se cuenta: dulces, bolsas, niños")],
    worked=[
        {"title": "Reparto", "problem": "Se reparten 20 dulces por igual entre 4 niños. ¿Cuántos recibe cada uno?", "steps": ["Conozco el total (20) y entre cuántos se reparte (4).", "Pienso 4 × ? = 20.", "20 ÷ 4 = 5."], "answer": "5 dulces cada uno"},
        {"title": "Agrupación y un segundo paso", "problem": "24 estudiantes forman equipos de 6 y cada equipo recibe 3 pelotas. ¿Cuántas pelotas se entregan?", "steps": ["Equipos: 24 ÷ 6 = 4.", "Pelotas: 4 × 3 = 12."], "answer": "12 pelotas"},
    ],
    mistakes=[
        {"wrong": "Resolver «20 dulces en bolsas de 5» con 20 − 5 = 15.", "why": "Se hace una sola resta en vez de dividir.", "fix": "Pregunta cuántos grupos de 5 caben en 20: 20 ÷ 5 = 4 bolsas."},
        {"wrong": "No escribir la unidad de la respuesta.", "why": "Se pierde qué se está contando.", "fix": "Escribe «4 bolsas» o «5 dulces»."},
    ],
    tiers={
        "recovery": [
            arith("Se reparten 21 dulces entre 3 niños por igual. ¿Cuántos recibe cada uno?", "21//3", "3 × 7 = 21."),
            arith("Se arman bolsas de 6 dulces con 30 dulces. ¿Cuántas bolsas salen?", "30//6", "5 × 6 = 30."),
            ex("«18 lápices entre 6 niños.» ¿Es reparto o agrupación?", "Reparto", "Se conoce la cantidad de niños y se busca lo que recibe cada uno."),
        ],
        "understand": [
            ex("«18 lápices en cajas de 6.» ¿Es reparto o agrupación?", "Agrupación", "Se conoce el tamaño de la caja y se buscan cuántas cajas."),
            ex("¿Qué división resuelve «Hay 45 sillas, 9 en cada fila»?", "45 ÷ 9", "Se buscan las filas."),
            ex("En «20 dulces entre 4 niños» y «bolsas de 5 con 20 dulces», ¿qué cuenta cada respuesta?", "Dulces por niño y bolsas", "El primero cuenta dulces; el segundo cuenta grupos."),
        ],
        "apply": [
            arith("Se reparten 28 hojas por igual entre 4 cursos. ¿Cuántas hojas recibe cada curso?", "28//4", "4 × 7 = 28."),
            arith("Se guardan 54 manzanas en bolsas de 6. ¿Cuántas bolsas se necesitan?", "54//6", "6 × 9 = 54."),
            arith("Se reparten 90 pegatinas por igual entre 10 niños. ¿Cuántas recibe cada uno?", "90//10", "10 × 9 = 90."),
        ],
        "reason": [
            ex("36 estudiantes forman equipos de 4 y cada equipo recibe 2 pelotas. ¿Cuántas pelotas se entregan en total?", "18", "36 ÷ 4 = 9 equipos y 9 × 2 = 18."),
            ex("Ana dice que repartir 15 entre 3 y formar grupos de 3 con 15 dan el mismo número. ¿Tiene razón? ¿Significan lo mismo?", "Sí, 5; pero significan cosas distintas", "En el reparto 5 es lo que recibe cada uno; en la agrupación 5 son los grupos."),
        ],
        "challenge": [
            arith("Se reparten 72 hojas entre 9 cursos y cada curso las divide en 4 grupos iguales. ¿Cuántas hojas tiene cada grupo?", "72//9//4", "Primero 72 ÷ 9 = 8 y luego 8 ÷ 4 = 2."),
            arith("Una cinta de 100 cm se corta en trozos de 10 cm. ¿Cuántos trozos salen?", "100//10", "10 × 10 = 100."),
        ],
    },
    context=[arith("En un paseo viajan 48 estudiantes y se sientan 6 por fila. ¿Cuántas filas se llenan?", "48//6", "6 × 8 = 48.")],
    selfcheck=[
        arith("Se reparten 32 hojas entre 8 niños. ¿Cuántas recibe cada uno?", "32//8", "8 × 4 = 32."),
        arith("Se forman grupos de 3 con 27 niños. ¿Cuántos grupos salen?", "27//3", "3 × 9 = 27."),
        ex("«25 sillas en filas de 5.» ¿Es reparto o agrupación?", "Agrupación", "Se conoce el tamaño de cada fila."),
    ],
    open_task=task(
        "Inventa un problema de reparto con 24 ÷ 4 y uno de agrupación con 24 ÷ 6. Escribe datos, pregunta, división y respuesta con su unidad. Luego resuelve: «Hay 35 niños en equipos de 5 y cada equipo recibe 2 balones. ¿Cuántos balones?».",
        "Reparto: «Reparto 24 lápices entre 4 niños. ¿Cuántos recibe cada uno?» 24 ÷ 4 = 6 lápices. Agrupación: «Con 24 manzanas armo bolsas de 6. ¿Cuántas bolsas?» 24 ÷ 6 = 4 bolsas. Balones: 35 ÷ 5 = 7 equipos y 7 × 2 = 14 balones.",
        ["inventa un reparto y una agrupación", "escribe pregunta y unidad", "resuelve el problema de dos pasos con 14", "las divisiones son correctas"],
        ["problemas escritos", "cálculos"],
        ["problemas sin pregunta", "olvidar el segundo paso"],
        "Reconoce los problemas inventados y pregunta qué cuenta cada respuesta; si hay error, que dibuje los grupos.",
    ),
    reinforce="Escribe una historia de reparto y otra de agrupación con la misma división 12 ÷ 3.",
    extend="Inventa un problema de dos pasos que use una división y una multiplicación y resuélvelo.",
)
