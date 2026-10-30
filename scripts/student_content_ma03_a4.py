"""Student material for 3.º básico Matemática, OA 06 (adición y sustracción hasta 1.000) y OA 07 (familias de operaciones)."""
from __future__ import annotations

from student_content_ma03_a import blk, task
from student_lessons import arith, ex, register

OA6 = "MA03 OA 06"
OA7 = "MA03 OA 07"

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Lápiz, cuaderno y, si quieres, tapas o dibujos de ▣ (centenas), ▮ (decenas) y ● (unidades). Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a sumar y restar números hasta 1.000 con mi propia estrategia y con material. Sirve para resolver cuentas de la vida diaria sin tener que seguir una sola receta.",
    prior=["Sé sumar y restar números hasta 100.", "Sé armar números de tres cifras con centenas, decenas y unidades."],
    explain=[
        "Para sumar números de tres cifras puedes juntar las piezas del mismo tipo: centenas con centenas, decenas con decenas y unidades con unidades. Para 245 + 130, juntas 200 + 100 = 300, 40 + 30 = 70 y 5 + 0 = 5. Después sumas las partes: 300 + 70 + 5 = 375.",
        "Hay muchas estrategias correctas. Puedes redondear y compensar: 250 + 190 es 250 + 200 − 10 = 440. O contar hacia arriba desde un número. Lo importante es que expliques cada paso y que el resultado sea el mismo, sea cual sea tu camino.",
        "Para restar con material, quitas piezas. En 500 − 230, quitas 2 centenas y 3 decenas, y quedan 270. Si no alcanzan las piezas, cambias una más grande por diez más pequeñas. Dibujar ▣ ▮ ● o usar tapas te ayuda a ver lo que haces.",
    ],
    vocab=[("estrategia personal", "tu propia manera de resolver un cálculo"), ("material concreto", "objetos que se pueden mover, como tapas"), ("compensar", "agregar o quitar algo para arreglar un cambio hecho antes"), ("sumandos", "los números que se suman"), ("resultado", "número que se obtiene al terminar el cálculo")],
    worked=[
        {"title": "Sumar con material", "problem": f"Junta {blk(2, 3, 4)} con {blk(1, 2, 3)}. ¿Qué número formas?", "steps": ["Junto las centenas: 2 + 1 = 3.", "Junto las decenas: 3 + 2 = 5.", "Junto las unidades: 4 + 3 = 7.", "El número tiene 3 centenas, 5 decenas y 7 unidades."], "answer": "357"},
        {"title": "Una estrategia con compensación", "problem": "Calcula 250 + 190 sumando 200 y arreglando después.", "steps": ["190 es 10 menos que 200.", "Sumo 200: 250 + 200 = 450.", "Como sumé 10 de más, quito 10: 450 − 10 = 440."], "answer": "440"},
    ],
    mistakes=[
        {"wrong": "Calcular 250 + 190 sumando 2 + 1 = 3 centenas y 5 + 9 = 14 decenas, y escribir 340.", "why": "Se escribe 14 decenas como si fueran 4 decenas y se pierde la centena que se forma.", "fix": "10 decenas son 1 centena. Suma los valores: 200 + 100 = 300 y 50 + 90 = 140; 300 + 140 = 440."},
        {"wrong": "Usar 250 + 200 = 450 y dejar 450 como respuesta de 250 + 190.", "why": "Se suma 10 de más y no se corrige.", "fix": "Si sumaste 200 en vez de 190, quita 10: 440."},
    ],
    tiers={
        "recovery": [
            ex(f"Junta {blk(2, 3, 4)} con {blk(1, 2, 3)}. ¿Qué número formas?", "357", "Se juntan centenas, decenas y unidades: 3, 5 y 7."),
            arith("Tienes 345 y quitas 2 centenas. ¿Qué número queda?", "345-200", "Solo cambia la cifra de las centenas."),
            arith("Calcula 134 + 215 juntando piezas del mismo tipo.", "134+215", "100 + 200 = 300, 30 + 10 = 40 y 4 + 5 = 9."),
        ],
        "understand": [
            ex("Para sumar 245 + 130, ¿cuánto suman las centenas, cuánto las decenas y cuánto las unidades?", "300, 70 y 5", "200 + 100 = 300, 40 + 30 = 70 y 5 + 0 = 5; en total 375."),
            ex("Una niña calcula 250 + 190 así: 250 + 200 − 10. Otra: 200 + 100, 50 + 90 y junta. ¿Ambas llegan al mismo resultado?", "Sí, 440", "250 + 200 − 10 = 440 y 300 + 140 = 440."),
            ex("¿Hay una sola estrategia correcta para sumar 128 + 135?", "No; hay varias y el resultado es 263", "Todas llegan al mismo número si se hacen bien."),
        ],
        "apply": [
            arith("Una biblioteca tiene 245 libros de cuentos y 130 de ciencia. ¿Cuántos libros hay?", "245+130", "Se suman las partes de cada lugar."),
            arith("Un camión lleva 480 cajas y descarga 150. ¿Cuántas cajas quedan en el camión?", "480-150", "Se quitan 1 centena y 5 decenas."),
            arith("En una feria hay 326 sillas y traen 175 más. ¿Cuántas sillas hay ahora?", "326+175", "Se suman centenas, decenas y unidades, y se cambian 10 unidades por una decena."),
        ],
        "reason": [
            ex("Pedro calcula 326 + 175 así: 300 + 100 = 400, 20 + 70 = 90, 6 + 5 = 11 y luego 400 + 90 + 11. ¿Está bien su estrategia?", "Sí; el resultado es 501", "400 + 90 + 11 = 501."),
            ex("Luisa calculó 250 + 190 = 340. Revisa su cuenta con 250 + 200 − 10. ¿Está bien?", "No; el resultado es 440", "250 + 200 = 450 y 450 − 10 = 440."),
        ],
        "challenge": [
            arith("Resuelve 603 − 258 con la estrategia que prefieras.", "603-258", "Se pueden restar 258 en partes: primero 200, después 50 y después 8."),
            ex("Dos números suman 500 y uno de ellos es 275. ¿Cuál es el otro?", "225", "500 − 275 = 225."),
        ],
    },
    context=[arith("Un almacén tiene 435 lápices, vende 120 y recibe 85 más. ¿Cuántos lápices tiene al final?", "435-120+85", "Primero se resta 120 y después se suma 85.")],
    selfcheck=[
        arith("¿Cuánto es 125 + 110?", "125+110", "Se suman centenas, decenas y unidades."),
        arith("¿Cuánto es 400 − 150?", "400-150", "Se quitan 1 centena y 5 decenas."),
        ex("Si dos personas calculan 128 + 135 por caminos distintos y ambas lo hacen bien, ¿el resultado es el mismo?", "Sí", "El resultado de una suma no depende de la estrategia."),
    ],
    open_task=task(
        "Resuelve 247 + 138 y 520 − 275 con tu propia estrategia. Puedes usar tapas, dibujos de ▣ ▮ ● o una recta. Escribe o dibuja los pasos y comprueba cada resultado haciendo la operación contraria.",
        "247 + 138: 200 + 100 = 300, 40 + 30 = 70, 7 + 8 = 15, y 300 + 70 + 15 = 385. Compruebo: 385 − 138 = 247. 520 − 275: 520 − 200 = 320, 320 − 70 = 250, 250 − 5 = 245. Compruebo: 245 + 275 = 520.",
        ["resuelve las dos operaciones", "muestra los pasos", "el resultado es correcto", "comprueba con la operación contraria"],
        ["pasos escritos o dibujados en el cuaderno", "comprobación escrita"],
        ["olvidar partes del resultado", "no comprobar"],
        "Reconoce la estrategia usada aunque sea distinta a la del libro; pide explicar un paso en voz alta. Si hay error, que repita con tapas.",
    ),
    reinforce="Con 3 tapas de 100, 5 de 10 y 7 de 1 forma el 357. Luego agrega 1 de 100, 2 de 10 y 3 de 1 y cuenta el nuevo total.",
    extend="Calcula 398 + 245 de dos maneras: una compensando con 400 y otra separando centenas, decenas y unidades. ¿Obtienes el mismo número?",
)

register(
    OA6, 2,
    materials="Lápiz y cuaderno cuadriculado, para alinear cada cifra en su columna. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a sumar hasta cuatro números de tres cifras con el algoritmo, llevando cuando las cifras de una columna pasan de 9. Sirve para totalizar cantidades grandes.",
    prior=["Sé sumar dos números en columnas, con y sin reserva.", "Sé que 10 unidades forman una decena y 10 decenas una centena."],
    explain=[
        "El algoritmo de la suma ordena los números en columnas: unidades abajo de unidades, decenas abajo de decenas y centenas abajo de centenas. Se empieza por las unidades, de derecha a izquierda. Si la columna suma 10 o más, se escribe la unidad y se lleva el resto a la columna siguiente.",
        "Veamos 248 + 175 + 39. Unidades: 8 + 5 + 9 = 22; escribo 2 y llevo 2 decenas. Decenas: 4 + 7 + 3 + 2 que llevo = 16; escribo 6 y llevo 1 centena. Centenas: 2 + 1 + 0 + 1 que llevo = 4. El resultado es 462.",
        "Cuando hay más sumandos, puede que lleves más de 1. Con 126 + 214 + 57 + 303, las unidades suman 20: escribo 0 y llevo 2. Al final revisa con una estimación: 248 + 175 + 39 es cerca de 250 + 175 + 40 = 465, y 462 es parecido.",
    ],
    vocab=[("algoritmo", "pasos ordenados para hacer una cuenta"), ("columna", "cifras puestas una bajo otra del mismo lugar"), ("llevar o reserva", "la parte que pasa a la columna siguiente"), ("sumando", "cada número que se suma"), ("estimar", "calcular una respuesta cercana")],
    worked=[
        {"title": "Tres sumandos con reserva", "problem": "Calcula 248 + 175 + 39 con el algoritmo.", "steps": ["Unidades: 8 + 5 + 9 = 22. Escribo 2 y llevo 2 decenas.", "Decenas: 4 + 7 + 3 = 14, más 2 que llevo = 16. Escribo 6 y llevo 1 centena.", "Centenas: 2 + 1 + 0 = 3, más 1 que llevo = 4. Escribo 4.", "Leo el resultado: 462."], "answer": "462"},
        {"title": "Cuatro sumandos", "problem": "Calcula 126 + 214 + 57 + 303 con el algoritmo.", "steps": ["Unidades: 6 + 4 + 7 + 3 = 20. Escribo 0 y llevo 2.", "Decenas: 2 + 1 + 5 + 0 = 8, más 2 = 10. Escribo 0 y llevo 1.", "Centenas: 1 + 2 + 0 + 3 = 6, más 1 = 7. Escribo 7."], "answer": "700"},
    ],
    mistakes=[
        {"wrong": "Sumar 57 + 68 y escribir 1115.", "why": "Se escriben los dos resultados de las columnas, 11 y 15, sin llevar.", "fix": "Unidades: 7 + 8 = 15; escribo 5 y llevo 1. Decenas: 5 + 6 + 1 = 12. El resultado es 125."},
        {"wrong": "Alinear 248 + 39 con las cifras a la izquierda.", "why": "Las unidades de 39 quedan bajo las decenas de 248.", "fix": "Alinea por la derecha: unidades bajo unidades."},
    ],
    tiers={
        "recovery": [
            arith("Suma 134 + 215 en columnas.", "134+215", "No hay reserva: 4 + 5 = 9, 3 + 1 = 4 y 1 + 2 = 3."),
            ex("En 247 + 85, las unidades suman 7 + 5 = 12. ¿Cuántas unidades escribes y cuántas decenas llevas?", "Escribo 2 y llevo 1 decena", "12 unidades son 1 decena y 2 unidades."),
            arith("Suma 258 + 164 en columnas.", "258+164", "8 + 4 = 12; 5 + 6 + 1 = 12; 2 + 1 + 1 = 4."),
        ],
        "understand": [
            ex("En 248 + 175 + 39, las unidades suman 8 + 5 + 9. ¿Cuánto es y qué escribes y qué llevas?", "22; escribo 2 y llevo 2", "22 unidades son 2 decenas y 2 unidades."),
            ex("En 126 + 214 + 57 + 303 las unidades suman 20. ¿Qué escribes y qué llevas?", "Escribo 0 y llevo 2", "20 unidades son 2 decenas y 0 unidades."),
            ex("Cuando las unidades suman más de 9, ¿a qué columna se lleva la reserva?", "A la de las decenas", "10 unidades forman una decena."),
        ],
        "apply": [
            arith("Calcula 248 + 175 + 39.", "248+175+39", "Se suman las tres columnas, llevando cuando pasan de 9."),
            arith("Calcula 126 + 214 + 57 + 303.", "126+214+57+303", "Las unidades suman 20 y las decenas 10 con la reserva."),
            arith("Tres cursos reúnen 135, 148 y 126 tapas. ¿Cuántas tapas juntaron en total?", "135+148+126", "Unidades: 5 + 8 + 6 = 19; decenas: 3 + 4 + 2 + 1 = 10."),
        ],
        "reason": [
            ex("Tomás sumó 57 + 68 y escribió 1115. ¿Qué hizo mal y cuál es el resultado?", "No llevó la reserva; es 125", "7 + 8 = 15, se escribe 5 y se lleva 1; 5 + 6 + 1 = 12."),
            ex("Ana obtuvo 600 al sumar 365 + 258 + 77. Estima aproximando cada número a la decena más cercana (370 + 260 + 80) y di si 600 es razonable.", "No; el resultado correcto es 700", "Estimando: 370 + 260 + 80 = 710, y 600 está lejos de 710. El cálculo exacto da 700."),
        ],
        "challenge": [
            ex("¿Qué cifra va en el cuadrado para que 2▢8 + 175 = 463?", "8", "463 − 175 = 288."),
            arith("Calcula 250 + 250 + 250 + 250.", "250+250+250+250", "Cuatro veces 250 llegan justo a mil."),
        ],
    },
    context=[arith("Una escuela recibe donaciones de 187, 94 y 215 libros. ¿Cuántos libros recibe en total?", "187+94+215", "Unidades: 7 + 4 + 5 = 16; decenas: 8 + 9 + 1 + 1 = 19.")],
    selfcheck=[
        arith("¿Cuánto es 164 + 37?", "164+37", "4 + 7 = 11, 6 + 3 + 1 = 10 y 1 + 1."),
        ex("En una suma en columnas, ¿por qué columna se empieza?", "Por las unidades", "Las reservas van hacia la izquierda."),
        arith("¿Cuánto es 118 + 205 + 76?", "118+205+76", "8 + 5 + 6 = 19; 1 + 0 + 7 + 1 = 9; 1 + 2 = 3."),
    ],
    open_task=task(
        "Suma en columnas estos tres números: 347, 168 y 94. Escribe cada reserva que llevas y comprueba el resultado con una estimación redondeando a la decena más cercana.",
        "347 + 168 + 94: unidades 7 + 8 + 4 = 19, escribo 9 y llevo 1. Decenas: 4 + 6 + 9 + 1 = 20, escribo 0 y llevo 2. Centenas: 3 + 1 + 0 + 2 = 6. Resultado: 609. Estimación: 350 + 170 + 90 = 610, que es cercano.",
        ["alinea bien las columnas", "escribe las reservas", "el resultado es 609", "estima y compara"],
        ["suma escrita en columnas", "reservas anotadas", "estimación escrita"],
        ["no llevar", "alinear mal las columnas"],
        "Reconoce el orden de las columnas y pregunta por cada reserva; si hay error, que lo revise con tapas de 100, 10 y 1.",
    ),
    reinforce="Suma 56 + 78 + 29 en columnas y comprueba con tapas. Después, 134 + 87.",
    extend="Suma 333 + 333 + 333. Luego cambia solo uno de los tres sumandos para que el total sea exactamente 1.000. ¿Qué número pusiste?",
)

register(
    OA6, 3,
    materials="Lápiz, cuaderno cuadriculado y, si quieres, tapas para representar centenas, decenas y unidades. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a restar números de tres cifras cambiando una pieza por diez cuando no alcanzan. Sirve para calcular cuánto queda o cuánto falta.",
    prior=["Sé restar números hasta 100.", "Sé canjear 1 centena por 10 decenas y 1 decena por 10 unidades."],
    explain=[
        "Para restar en columnas se empieza por las unidades. Si arriba hay menos que abajo, como 2 − 5, se canjea: una decena de arriba se cambia por 10 unidades. En 432 − 175, el 432 pasa a 4 centenas, 2 decenas y 12 unidades. Ahora 12 − 5 = 7.",
        "En las decenas ahora hay 2 y hay que restar 7. Otra vez no alcanza, y se canjea una centena por 10 decenas: quedan 3 centenas y 12 decenas. Entonces 12 − 7 = 5 y 3 − 1 = 2. El resultado es 257.",
        "Cuando hay ceros arriba, el canje es más largo. En 500 − 238, el 500 se muestra como 4 centenas, 9 decenas y 10 unidades. Entonces 10 − 8 = 2, 9 − 3 = 6 y 4 − 2 = 2: resultado 262. Siempre comprueba sumando: 262 + 238 = 500.",
    ],
    vocab=[("canje", "cambio de una pieza por 10 del lugar de la derecha"), ("restar", "quitar o encontrar lo que falta"), ("diferencia", "resultado de una resta"), ("comprobar", "revisar si el resultado es correcto, por ejemplo sumando"), ("reagrupar", "mostrar un número con otras piezas sin cambiar su valor")],
    worked=[
        {"title": "Restar con canje", "problem": "Calcula 432 − 175.", "steps": ["Unidades: 2 − 5 no se puede. Canjeo 1 decena por 10 unidades: 12 − 5 = 7.", "Decenas: ahora hay 2 y debo restar 7. Canjeo 1 centena por 10 decenas: 12 − 7 = 5.", "Centenas: quedan 3 y resto 1: 3 − 1 = 2.", "Resultado: 257. Compruebo: 257 + 175 = 432."], "answer": "257"},
        {"title": "Restar desde un número con ceros", "problem": "Calcula 500 − 238.", "steps": ["Muestro 500 como 4 centenas, 9 decenas y 10 unidades.", "Unidades: 10 − 8 = 2. Decenas: 9 − 3 = 6. Centenas: 4 − 2 = 2.", "Resultado: 262. Compruebo: 262 + 238 = 500."], "answer": "262"},
    ],
    mistakes=[
        {"wrong": "Restar 432 − 175 y escribir 343.", "why": "En cada columna se resta el menor del mayor, aunque el mayor esté abajo.", "fix": "Si arriba hay menos, canjea. 2 − 5 no se puede; usa 12 − 5 = 7."},
        {"wrong": "Canjear una decena por 10 unidades pero no bajar la decena.", "why": "Se suma el canje pero no se quita la decena que se cambió.", "fix": "Después del canje, las decenas pasan de 3 a 2."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 586 − 243 en columnas.", "586-243", "En cada columna el número de arriba es mayor: 6 − 3, 8 − 4 y 5 − 2."),
            ex("En 432 − 175 no se puede 2 − 5. ¿Qué canje se hace?", "1 decena por 10 unidades", "Quedan 12 unidades y 2 decenas."),
            arith("Calcula 345 − 128.", "345-128", "Se canjea una decena: 15 − 8 = 7, 3 − 2 = 1 y 3 − 1 = 2."),
        ],
        "understand": [
            ex("En 432 − 175, ¿cuántas unidades hay en el 432 después del primer canje?", "12", "2 unidades más 10 unidades del canje."),
            ex("En 500 − 238 no hay decenas ni unidades. ¿Cómo se muestra el 500 con canjes?", "4 centenas, 9 decenas y 10 unidades", "Una centena se canjea por 10 decenas y una decena por 10 unidades."),
            ex("Para comprobar que 432 − 175 = 257, ¿qué suma haces?", "257 + 175 = 432", "Si la suma da el número de arriba, la resta está bien."),
        ],
        "apply": [
            arith("Calcula 432 − 175.", "432-175", "Se canjea una decena y una centena."),
            arith("Calcula 500 − 238.", "500-238", "Se muestra 500 como 4 centenas, 9 decenas y 10 unidades."),
            arith("Una escuela tenía 604 hojas y usó 328. ¿Cuántas hojas quedan?", "604-328", "Se canjea una centena por decenas y una decena por unidades."),
        ],
        "reason": [
            ex("Luis restó 432 − 175 y obtuvo 343, porque restó la cifra menor de la mayor en cada columna. ¿Cuál es el resultado correcto?", "257", "En las columnas donde arriba hay menos, se canjea."),
            ex("Ana dice que 500 − 238 = 362. Comprueba sumando 362 + 238. ¿Está bien?", "No; el resultado correcto es 262", "362 + 238 = 600, no 500."),
        ],
        "challenge": [
            arith("Calcula 1.000 − 468.", "1000-468", "Se muestra 1.000 con 9 centenas, 9 decenas y 10 unidades."),
            ex("¿Qué número falta: 704 − ___ = 429?", "275", "704 − 429 = 275."),
        ],
    },
    context=[arith("Una panadería hizo 620 panes y vendió 345. ¿Cuántos panes quedan?", "620-345", "Se canjea una decena y una centena.")],
    selfcheck=[
        arith("¿Cuánto es 850 − 391?", "850-391", "Se canjea una decena por unidades y una centena por decenas."),
        ex("Si arriba hay menos unidades que abajo, ¿qué haces?", "Canjeo una decena por 10 unidades", "Así arriba hay suficientes unidades para restar."),
        arith("¿Cuánto es 700 − 256?", "700-256", "Se canjea por pasos desde 7 centenas."),
    ],
    open_task=task(
        "Resuelve en columnas 523 − 276 y 800 − 345. Dibuja con ▣ ▮ ● los canjes que haces en la primera y comprueba las dos restas con una suma.",
        "523 − 276: 13 − 6 = 7, 11 − 7 = 4 (canjeé una centena), 4 − 2 = 2. Resultado 247. Compruebo: 247 + 276 = 523. 800 − 345: 7 centenas, 9 decenas y 10 unidades; 10 − 5 = 5, 9 − 4 = 5, 7 − 3 = 4. Resultado 455. Compruebo: 455 + 345 = 800.",
        ["resuelve las dos restas", "dibuja los canjes", "los resultados son 247 y 455", "comprueba con una suma"],
        ["restas en columnas", "dibujo de canjes", "sumas de comprobación"],
        ["restar al revés", "no bajar la pieza canjeada"],
        "Reconoce los canjes y pregunta por qué cambió una centena por decenas; si hay error, que lo repita con tapas.",
    ),
    reinforce="Con 4 tapas de 100, 3 de 10 y 2 de 1 (432) quita 175 y haz los canjes necesarios con tapas.",
    extend="Resta 1.000 − 100, 1.000 − 10 y 1.000 − 1. ¿Qué observas en las respuestas?",
)

register(
    OA6, 4,
    materials="Lápiz y cuaderno. Todos los datos están escritos en cada problema; puedes dibujar cajas o barras para ordenar los números.",
    use="Aprenderé a resolver problemas con más de una operación y a inventar los míos. Sirve para seguir lo que ocurre con una cantidad cuando suben y bajan cosas.",
    prior=["Sé sumar y restar números hasta 1.000.", "Sé decidir si un problema se resuelve con suma o con resta."],
    explain=[
        "En un problema con varias operaciones, la cantidad cambia en etapas. «Tenía 300 figuritas, regalé 120 y después recibí 50.» Primero se resta 300 − 120 = 180. Después se suma 180 + 50 = 230. Se hace en el orden en que ocurren las cosas.",
        "Una buena manera es escribir una línea con cada cambio: 300, −120, +50. Los verbos ayudan: «regalé» o «gasté» indican resta, y «recibí» o «gané» indican suma. Anota lo que queda después de cada paso para no perderte.",
        "También puedes inventar un problema para una cuenta. La cuenta 500 − 120 + 80 puede ser: «Una tienda tenía 500 cuadernos, vendió 120 y recibió 80». Un problema bien inventado tiene una pregunta clara y datos suficientes.",
    ],
    vocab=[("operaciones sucesivas", "operaciones que se hacen una después de otra"), ("cantidad inicial", "la que hay al comienzo"), ("resultado parcial", "lo que queda después de un paso"), ("dato", "número o información que da el problema"), ("pregunta", "lo que se quiere saber")],
    worked=[
        {"title": "Dos etapas", "problem": "Tenía 300 figuritas, regalé 120 y después recibí 50. ¿Cuántas tengo ahora?", "steps": ["Primero regalé: 300 − 120 = 180.", "Después recibí: 180 + 50 = 230.", "Escribo la respuesta con la unidad: 230 figuritas."], "answer": "230 figuritas"},
        {"title": "Resta sucesiva", "problem": "Una librería tiene 600 cuadernos. Vende 245 el lunes y 130 el martes. ¿Cuántos cuadernos quedan?", "steps": ["Después del lunes: 600 − 245 = 355.", "Después del martes: 355 − 130 = 225.", "Quedan 225 cuadernos."], "answer": "225 cuadernos"},
    ],
    mistakes=[
        {"wrong": "Resolver «Tenía 300, gasté 120 y recibí 50» como 300 + 120 + 50.", "why": "Se suman todos los datos sin pensar si suben o bajan.", "fix": "«Gasté» resta. Resuelve en orden: 300 − 120 = 180 y 180 + 50 = 230."},
        {"wrong": "Responder solo con el resultado del primer paso.", "why": "Se olvida que la pregunta es por el final.", "fix": "Termina todos los pasos y relee la pregunta."},
    ],
    tiers={
        "recovery": [
            arith("Hay 250 sillas y llegan 130 más. ¿Cuántas sillas hay?", "250+130", "Llegan más, entonces se suma."),
            arith("Un tren llevaba 400 personas y bajaron 125. ¿Cuántas personas quedan?", "400-125", "Bajan personas, entonces se resta."),
            ex("En «Tenía 300, gasté 120 y luego recibí 50», ¿qué operación se hace primero?", "300 − 120", "Primero ocurrió el gasto."),
        ],
        "understand": [
            ex("En «Tenía 400, gasté 150 y luego recibí 60», ¿cuántos tengo al final?", "310", "400 − 150 = 250 y 250 + 60 = 310."),
            ex("Escribe la cuenta para: Luis tenía 450 figuritas, regaló 90 y le dieron 35.", "450 − 90 + 35 = 395", "Regalar resta y recibir suma."),
            ex("Sumo 120 y 85 y después resto 60. ¿Cuánto da?", "145", "120 + 85 = 205 y 205 − 60 = 145."),
        ],
        "apply": [
            arith("En un colegio hay 438 niños. Se van 52 y llegan 87. ¿Cuántos niños hay ahora?", "438-52+87", "Primero 438 − 52 = 386 y después 386 + 87."),
            arith("Un kiosco tiene 700 revistas, vende 260 el viernes y 150 el sábado. ¿Cuántas quedan?", "700-260-150", "Se restan las dos ventas, una tras otra."),
            arith("Marta ahorró 275, Pedro ahorró 190 y gastaron 150 juntos en un regalo. ¿Cuánto les queda?", "275+190-150", "Primero se juntan los ahorros y luego se resta el gasto."),
        ],
        "reason": [
            ex("Ema resolvió «Tenía 300, gasté 120 y recibí 50» con 300 + 120 + 50. ¿Qué error cometió y cuál es el resultado?", "Sumó el gasto; el resultado es 230", "Gastar resta, no suma."),
            ex("«Tenía 250 y después gasté algo.» ¿Se puede saber cuánto me queda?", "No; falta saber cuánto gasté", "Sin ese dato no se puede restar."),
        ],
        "challenge": [
            arith("Calcula 600 − 175 − 225.", "600-175-225", "Se resta 175 y después 225."),
            ex("Tenía figuritas, regalé 45 y quedaron 130. ¿Cuántas tenía?", "175", "130 + 45 = 175."),
        ],
    },
    context=[arith("Un estadio tiene 800 asientos libres. Se venden 325 entradas el sábado y 275 el domingo. ¿Cuántos asientos libres quedan?", "800-325-275", "Cada venta ocupa asientos, se restan una tras otra.")],
    selfcheck=[
        arith("¿Cuánto es 120 + 80 − 50?", "120+80-50", "Primero 120 + 80 = 200."),
        ex("En «Tenía 90, gané 60 y gasté 40», ¿cuánto tengo?", "110", "90 + 60 = 150 y 150 − 40 = 110."),
        ex("¿Qué palabra indica una resta: «regalé» o «recibí»?", "Regalé", "Regalar es dar, entonces la cantidad baja."),
    ],
    open_task=task(
        "Resuelve y luego inventa. Primero resuelve: «Una tienda tenía 500 cuadernos, vendió 120 y recibió 80». Después inventa un problema con la cuenta 400 + 150 − 90, escribe su pregunta y su respuesta.",
        "Resuelvo: 500 − 120 = 380 y 380 + 80 = 460 cuadernos. Mi problema: «Había 400 vasos en una bodega, llegaron 150 más y se rompieron 90. ¿Cuántos vasos quedan?» 400 + 150 = 550 y 550 − 90 = 460.",
        ["resuelve el primero con 460", "inventa un problema coherente con la cuenta", "incluye una pregunta clara", "calcula la respuesta"],
        ["cálculos en el cuaderno", "problema inventado escrito"],
        ["sumar todos los datos", "inventar sin pregunta"],
        "Reconoce el problema inventado y pregunta si los datos alcanzan para responderlo; si hay error, que escriba una línea con cada cambio.",
    ),
    reinforce="Escribe una línea con +, − y los números de este problema: tenía 250, gasté 100 y recibí 75. Calcula el final.",
    extend="Inventa un problema con tres operaciones (por ejemplo +, − y −) con números hasta 1.000 y resuélvelo.",
)

register(
    OA6, 5,
    materials="Lápiz y cuaderno. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a estimar el resultado antes de calcular y a comprobar después si lo calculado es razonable. Sirve para descubrir errores antes de entregar una respuesta.",
    prior=["Sé sumar y restar con el algoritmo.", "Sé que la suma y la resta se deshacen entre sí."],
    explain=[
        "Estimar es calcular una respuesta cercana con números fáciles. Para 487 + 312, aproximas cada número a la centena más cercana. Para elegir, mira la cifra de las decenas: si es 0, 1, 2, 3 o 4, te quedas con la centena de abajo; si es 5, 6, 7, 8 o 9, subes a la centena siguiente. Así 487 es casi 500 y 312 es casi 300. Entonces 487 + 312 es cerca de 800. El resultado exacto, 799, está muy cerca.",
        "La estimación sirve para ver si el resultado exacto es razonable. Si alguien dice que 498 + 399 = 997, tú estimas 500 + 400 = 900. Como 997 es muy distinto de 900, hay un error. El resultado correcto es 897.",
        "Para comprobar de forma exacta, usas la operación contraria. Si 432 − 175 = 257, entonces 257 + 175 debe ser 432. Si 345 + 278 = 623, entonces 623 − 278 debe ser 345. Estimar antes y comprobar después evita muchos errores.",
    ],
    vocab=[("estimar", "calcular un resultado cercano usando números fáciles"), ("aproximar", "cambiar un número por otro cercano más fácil, como 487 por 500"), ("razonable", "que tiene sentido y es cercano a lo esperado"), ("comprobar", "revisar con otra operación si el resultado exacto es correcto"), ("operación contraria", "la que deshace a la otra: suma y resta")],
    worked=[
        {"title": "Estimar y calcular", "problem": "Estima y luego calcula 487 + 312.", "steps": ["Aproximo a centenas: 487 ≈ 500 y 312 ≈ 300.", "Estimación: 500 + 300 = 800.", "Cálculo exacto: 487 + 312 = 799.", "799 está cerca de 800, entonces es razonable."], "answer": "Estimación 800; exacto 799"},
        {"title": "Comprobar con la operación contraria", "problem": "Ana dice que 345 + 278 = 623. Comprueba con una resta.", "steps": ["Hago 623 − 278.", "623 − 278 = 345.", "Obtuve el primer sumando, entonces la suma está bien."], "answer": "Está bien; 623 − 278 = 345"},
    ],
    mistakes=[
        {"wrong": "Aceptar 997 como resultado de 498 + 399 sin revisar.", "why": "No se estimó antes de aceptar el resultado.", "fix": "500 + 400 = 900. 997 se aleja mucho; el resultado es 897."},
        {"wrong": "Comprobar 432 − 175 = 257 repitiendo la misma resta.", "why": "Repetir el mismo cálculo puede repetir el mismo error.", "fix": "Comprueba con la operación contraria: 257 + 175 = 432."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es la centena más cercana a 487?", "500", "487 está más cerca de 500 que de 400."),
            ex("¿Cuál es la centena más cercana a 312?", "300", "312 está más cerca de 300 que de 400."),
            ex("Estima 487 + 312 aproximando a centenas.", "800", "500 + 300 = 800."),
        ],
        "understand": [
            ex("¿Cuál es la centena más cercana a 349: 300 o 400?", "300", "349 está a 49 de 300 y a 51 de 400."),
            ex("La estimación de una suma es 800 y el cálculo exacto es 799. ¿Es razonable?", "Sí", "799 está muy cerca de 800."),
            ex("Para comprobar 432 − 175 = 257, ¿qué haces?", "Sumo 257 + 175 y debe dar 432", "La suma deshace la resta."),
        ],
        "apply": [
            ex("Estima 298 + 405 con centenas y luego calcula el valor exacto.", "Estimación 700; exacto 703", "300 + 400 = 700 y 298 + 405 = 703."),
            ex("Estima 612 − 189 con centenas y luego calcula el valor exacto.", "Estimación 400; exacto 423", "600 − 200 = 400 y 612 − 189 = 423."),
            ex("Ana dice que 345 + 278 = 623. Comprueba con 623 − 278.", "345; la suma está bien", "623 − 278 = 345."),
        ],
        "reason": [
            ex("Pedro obtuvo 997 para 498 + 399. Estima con centenas: ¿es razonable?", "No; el resultado correcto es 897", "500 + 400 = 900 y 997 se aleja de 900."),
            ex("Alguien dice que 700 − 298 = 502. Comprueba con una suma: ¿qué pasa?", "502 + 298 = 800, no 700; el resultado correcto es 402", "La suma de comprobación no da el número inicial."),
        ],
        "challenge": [
            ex("Estima y calcula 399 + 298.", "Estimación 700; exacto 697", "400 + 300 = 700 y 399 + 298 = 697."),
            ex("Resta 903 − 497 y comprueba con una suma.", "406; 406 + 497 = 903", "903 − 497 = 406."),
        ],
    },
    context=[ex("Una tienda recibe 312 cajas el lunes y 489 el martes. Estima el total con centenas y calcula el exacto.", "Estimación 800; exacto 801", "300 + 500 = 800 y 312 + 489 = 801.")],
    selfcheck=[
        ex("Estima 205 + 296 con centenas.", "500", "200 + 300 = 500."),
        ex("Para comprobar 500 − 240 = 260, ¿qué suma haces?", "260 + 240 = 500", "La suma deshace la resta."),
        ex("¿Cuál es la centena más cercana a 651?", "700", "651 está a 49 de 700 y a 51 de 600."),
    ],
    open_task=task(
        "Resuelve 386 + 417 y 702 − 358. Antes de calcular, escribe una estimación con centenas. Después calcula y comprueba con la operación contraria. Escribe si tu resultado es razonable.",
        "386 + 417: estimo 400 + 400 = 800. Calculo: 803. Compruebo: 803 − 417 = 386. Es razonable. 702 − 358: estimo 700 − 400 = 300. Calculo: 344. Compruebo: 344 + 358 = 702. Es razonable.",
        ["escribe la estimación antes de calcular", "calcula bien las dos operaciones", "comprueba con la operación contraria", "dice si es razonable"],
        ["estimaciones", "cálculos", "comprobaciones"],
        ["estimar después de calcular", "comprobar repitiendo la misma operación"],
        "Reconoce la estimación previa y pregunta qué haría si el resultado exacto estuviera lejos; si hay error, que revise las columnas.",
    ),
    reinforce="Estima con centenas 215 + 389, 703 − 198 y 466 + 120, y luego calcula el valor exacto de cada una.",
    extend="Explica con una frase por qué estimar antes ayuda a descubrir un error de llevar o de canjear.",
)

# ---------------------------------------------------------------- OA 07
register(
    OA7, 1,
    materials="Lápiz, cuaderno y una caja dibujada con una línea que separa dos partes. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a escribir todas las sumas y restas que se forman con las mismas tres cantidades: dos partes y el total. Sirve para ver cómo la suma y la resta se relacionan.",
    prior=["Sé sumar y restar números hasta 1.000.", "Sé que dos partes juntas forman un total."],
    explain=[
        "Con dos partes y un total puedes escribir cuatro operaciones que van juntas. Si las partes son 25 y 38 y el total es 63, las operaciones son 25 + 38 = 63, 38 + 25 = 63, 63 − 25 = 38 y 63 − 38 = 25. A ese grupo se le llama familia de operaciones.",
        "En la familia siempre aparecen los mismos tres números. El total es el más grande y está solo en una posición especial: al principio de las restas y al final de las sumas. Las partes son los otros dos.",
        "Dibuja una caja con una parte a cada lado y el total arriba. Para escribir la familia, junta las partes con + y llega al total; luego quita cada parte al total con −. Si las dos partes son iguales, como 20 y 20, solo hay una suma y una resta diferentes.",
    ],
    vocab=[("familia de operaciones", "grupo de sumas y restas con los mismos tres números"), ("parte", "una de las cantidades que se juntan"), ("total", "cantidad que resulta de juntar las partes"), ("operación inversa", "la que deshace a otra: la resta deshace la suma"), ("sumandos", "los números que se suman")],
    worked=[
        {"title": "Escribir la familia", "problem": "Las partes son 25 y 38 y el total es 63. Escribe las cuatro operaciones.", "steps": ["Sumas: 25 + 38 = 63 y 38 + 25 = 63.", "Restas: al total le quito una parte: 63 − 25 = 38.", "Quito la otra parte: 63 − 38 = 25.", "Reviso que las cuatro usen 25, 38 y 63."], "answer": "25 + 38 = 63, 38 + 25 = 63, 63 − 25 = 38, 63 − 38 = 25"},
        {"title": "Completar una operación de la familia", "problem": "Las partes son 125 y 175 y el total es 300. Completa 300 − ___ = 125.", "steps": ["En la familia está 125 + 175 = 300.", "Al total le quito 175 y queda la otra parte, 125.", "Entonces falta 175."], "answer": "175"},
    ],
    mistakes=[
        {"wrong": "Escribir 15 + 20 = 35 y 35 − 15 = 25 como familia.", "why": "En la resta se usó un número que no es parte: 35 − 15 da 20.", "fix": "Comprueba cada resta: 35 − 15 = 20 y 35 − 20 = 15."},
        {"wrong": "Escribir 63 − 25 = 88.", "why": "Se suma en lugar de restar, o se usa el total mal.", "fix": "En una resta el total va primero. 63 − 25 = 38."},
    ],
    tiers={
        "recovery": [
            ex("Las partes son 5 y 8 y el total es 13. Escribe la otra suma de la familia.", "8 + 5 = 13", "Se cambia el orden de los sumandos."),
            ex("Con 34, 27 y 61, si 34 + 27 = 61, escribe las otras tres operaciones.", "27 + 34 = 61; 61 − 34 = 27; 61 − 27 = 34", "Se cambia el orden y se quita cada parte al total."),
            ex("En la familia de 40, 60 y 100, ¿cuál es el total?", "100", "40 + 60 = 100."),
        ],
        "understand": [
            ex("¿Cuál número es el total en la familia de 45, 55 y 100?", "100", "45 + 55 = 100."),
            ex("La resta 63 − 25 = 38 es de una familia. ¿Qué suma pertenece a esa familia?", "25 + 38 = 63", "Las partes son 25 y 38 y el total es 63."),
            ex("Una familia con partes distintas, ¿cuántas operaciones tiene en total: 2 sumas y 2 restas?", "4", "Dos sumas y dos restas."),
        ],
        "apply": [
            ex("Escribe las cuatro operaciones de la familia de 250, 130 y 380.", "250 + 130 = 380; 130 + 250 = 380; 380 − 250 = 130; 380 − 130 = 250", "Primero las sumas y luego las restas."),
            ex("Las partes son 240 y 160 y el total es 400. Completa 400 − ___ = 240.", "160", "Al total le quitas una parte y queda la otra."),
            ex("En una caja hay 48 pelotas rojas y 37 azules, 85 en total. Escribe la resta que te dice cuántas son rojas.", "85 − 37 = 48", "Al total le quito las azules y quedan las rojas."),
        ],
        "reason": [
            ex("Ana dice que 15 + 20 = 35 y 35 − 15 = 25 son de la misma familia. ¿Tiene razón?", "No", "35 − 15 = 20, no 25."),
            ex("¿Pertenece 40 + 45 = 85 a la misma familia que 85 − 40 = 45?", "Sí", "Usan los mismos números: 40, 45 y 85."),
        ],
        "challenge": [
            ex("Con 47, 58 y 105, ¿cuál es el total? Escribe las cuatro operaciones.", "105; 47 + 58 = 105, 58 + 47 = 105, 105 − 47 = 58, 105 − 58 = 47", "47 + 58 = 105, por lo tanto 105 es el total."),
            ex("Con 9, 16 y 25, ¿cuál es la resta de la familia que da 9?", "25 − 16 = 9", "El total es 25 y 25 − 16 = 9."),
        ],
    },
    context=[ex("En un curso hay 18 niñas y 14 niños, 32 estudiantes en total. Escribe una resta que diga cuántos niños hay.", "32 − 18 = 14", "Al total le quito las niñas y quedan los niños.")],
    selfcheck=[
        ex("Completa la familia: 7 + 6 = 13, 13 − 7 = ___.", "6", "Al total le quito una parte y queda la otra."),
        ex("En la familia de 90, 45 y 45, ¿cuál es el total?", "90", "45 + 45 = 90."),
        ex("Escribe la otra suma de la familia: 20 + 35 = 55.", "35 + 20 = 55", "Se cambia el orden de los sumandos."),
    ],
    open_task=task(
        "Escoge una de estas tres familias: 120, 80 y 200; 345, 155 y 500; 67, 29 y 96. Dibuja una caja con las dos partes y el total. Escribe las cuatro operaciones y revisa cada una.",
        "Elijo 120, 80 y 200. La caja tiene 120 y 80 como partes y 200 como total. Escribo 120 + 80 = 200, 80 + 120 = 200, 200 − 120 = 80 y 200 − 80 = 120.",
        ["identifica el total", "escribe las cuatro operaciones", "dibuja la caja", "revisa cada una"],
        ["caja dibujada", "cuatro operaciones escritas"],
        ["poner una parte como total", "escribir una resta que no es de la familia"],
        "Reconoce el total bien identificado y pide que lea cada operación; si hay error, que revise con tapas cuál grupo es el total.",
    ),
    reinforce="Con 12 tapas separadas en 7 y 5, escribe las cuatro operaciones y muévelas para comprobar cada una.",
    extend="¿Por qué la familia de 30, 30 y 60 tiene solo dos operaciones distintas?",
)

register(
    OA7, 2,
    materials="Lápiz y cuaderno. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a comprobar una suma con una resta. Sirve para descubrir si me equivoqué sin pedir ayuda.",
    prior=["Sé escribir una familia de operaciones.", "Sé sumar y restar números hasta 1.000."],
    explain=[
        "Si sumas dos números y luego restas uno de ellos al total, debes volver al otro. En 345 + 278 = 623, la resta 623 − 278 debe dar 345. Si da otro número, hay un error en la suma o en la resta.",
        "Puedes elegir cuál sumando restas: 623 − 278 da 345 y 623 − 345 da 278. Cualquiera de las dos comprobaciones sirve. Si las dos dan el otro sumando, es casi seguro que la suma está bien.",
        "Si la comprobación no da lo esperado, vuelve a calcular. Por ejemplo, si al comprobar 238 + 154 = 382 haces 382 − 238 y obtienes 144, y no 154, la suma estaba mal. La suma correcta es 392. Comprobar es una forma de revisar tu trabajo.",
    ],
    vocab=[("comprobar", "revisar si un resultado es correcto"), ("operación inversa", "la que deshace a otra"), ("sumando", "cada número que se suma"), ("total", "resultado de la suma"), ("error", "algo que quedó mal calculado")],
    worked=[
        {"title": "La resta devuelve el sumando", "problem": "Ana sumó 345 + 278 y obtuvo 623. Comprueba con una resta.", "steps": ["Resto uno de los sumandos del total: 623 − 278.", "623 − 278 = 345.", "Obtuve el otro sumando, entonces la suma está bien."], "answer": "Está bien; 623 − 278 = 345"},
        {"title": "Detectar un error", "problem": "Marta sumó 238 + 154 y obtuvo 382. Comprueba con 382 − 238.", "steps": ["382 − 238 = 144.", "Debería haber obtenido 154, pero obtuve 144.", "La suma estaba mal. Calculo de nuevo: 238 + 154 = 392."], "answer": "Estaba mal; el resultado correcto es 392"},
    ],
    mistakes=[
        {"wrong": "Comprobar 345 + 278 = 623 sumando de nuevo 345 + 278.", "why": "Repetir la misma operación puede repetir el mismo error.", "fix": "Usa la operación inversa: 623 − 278 debe dar 345."},
        {"wrong": "Restar los sumandos entre sí para comprobar.", "why": "La resta de comprobación parte del total, no de un sumando.", "fix": "Al total le restas uno de los sumandos."},
    ],
    tiers={
        "recovery": [
            ex("Para comprobar 12 + 8 = 20, ¿qué resta usas?", "20 − 8 = 12", "Al total le restas un sumando."),
            ex("Sumaste 40 + 35 = 75. Comprueba con 75 − 35. ¿Cuánto da?", "40", "75 − 35 = 40, que es el otro sumando."),
            ex("Para comprobar 25 + 17 = 42, ¿qué otra resta puedes hacer además de 42 − 17?", "42 − 25 = 17", "También sirve restar el otro sumando."),
        ],
        "understand": [
            ex("Hiciste 345 + 278 = 623. Si 623 − 278 da 345, ¿la suma está bien?", "Sí", "La resta devolvió el otro sumando."),
            ex("Al comprobar 56 + 27 = 83, ¿sirven 83 − 27 y 83 − 56?", "Sí, ambas", "Cada una devuelve un sumando."),
            ex("Al comprobar 120 + 85 = 215 haces 215 − 85 y te da 130. ¿Qué significa?", "Hay un error; la suma correcta es 205", "Debía dar 120."),
        ],
        "apply": [
            ex("Comprueba 463 + 259 = 722 con una resta. ¿Qué resta haces y cuánto da?", "722 − 259 = 463", "La resta devuelve el otro sumando."),
            ex("Ana sumó 487 + 215 y obtuvo 702. Comprueba con una resta.", "702 − 215 = 487; está bien", "La resta devuelve 487."),
            ex("Luis sumó 359 + 128 y obtuvo 477. Comprueba con 477 − 128 y corrige si hace falta.", "Da 349, no 359; la suma correcta es 487", "359 + 128 = 487."),
        ],
        "reason": [
            ex("María sumó 238 + 154 = 382 y comprobó con 382 − 238 = 144. ¿Está bien su suma?", "No; la suma correcta es 392", "La comprobación debía dar 154."),
            ex("Sofía comprueba 85 + 47 = 132 con 132 − 47 y Tomás con 132 − 85. ¿Qué debe dar cada resta?", "85 y 47", "Cada resta devuelve el otro sumando."),
        ],
        "challenge": [
            ex("Si 4▢3 + 258 = 701, ¿qué cifra falta? Usa 701 − 258.", "4", "701 − 258 = 443."),
            ex("Se sabe que 999 − 625 = 374. ¿Qué suma comprueba esta resta?", "374 + 625 = 999", "La suma deshace la resta."),
        ],
    },
    context=[ex("En un tren viajan 238 personas y suben 154 más: ahora son 392. Comprueba con una resta.", "392 − 154 = 238", "La resta devuelve la cantidad inicial.")],
    selfcheck=[
        ex("¿Qué resta comprueba 60 + 25 = 85?", "85 − 25 = 60", "Al total le quito un sumando."),
        ex("Si 150 + 275 = 425, ¿cuánto da 425 − 275?", "150", "Devuelve el otro sumando."),
        ex("¿Por qué no sirve comprobar una suma repitiendo la misma suma?", "Puede repetir el mismo error", "Una operación distinta revisa de verdad."),
    ],
    open_task=task(
        "Un compañero hizo estas tres sumas: 156 + 227 = 383, 438 + 395 = 823 y 264 + 389 = 643. Comprueba cada una con una resta y escribe cuáles están bien y cuáles mal. Corrige las que estén mal.",
        "383 − 227 = 156: bien. 823 − 395 = 428, no 438: mal; la suma correcta es 833. 643 − 389 = 254, no 264: mal; la suma correcta es 653.",
        ["comprueba las tres sumas", "usa una resta", "dice cuáles están bien y cuáles mal", "corrige las incorrectas"],
        ["restas de comprobación escritas", "correcciones"],
        ["comprobar repitiendo la suma", "no corregir"],
        "Reconoce las restas y pregunta qué número esperaba obtener en cada una; si hay error, que repita la suma por partes.",
    ),
    reinforce="Haz 5 sumas de dos números y comprueba cada una con una resta. Marca con una estrella las que te salieron bien.",
    extend="Explica con tus palabras por qué una resta puede comprobar una suma.",
)

register(
    OA7, 3,
    materials="Lápiz, cuaderno y un cuadrado vacío ▢ para representar el número desconocido. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a encontrar el número que falta en una suma o en una resta, usando la familia de operaciones. Sirve para resolver enigmas como «¿cuánto tenía antes?».",
    prior=["Sé escribir la familia de una suma.", "Sé comprobar una suma con una resta."],
    explain=[
        "A veces falta un número, y se escribe con un cuadrado: ▢ + 25 = 63. Para encontrarlo, piensa en la familia. Si el total es 63 y una parte es 25, la otra parte es 63 − 25 = 38. Comprueba: 38 + 25 = 63.",
        "Si falta el total, se suma: 40 + 35 = ▢ da 75. Si falta una parte en una suma, se resta: 40 + ▢ = 90 es 90 − 40 = 50. Si falta el primer número de una resta, se suma: ▢ − 45 = 30 es 30 + 45 = 75, porque 75 − 45 = 30.",
        "Si falta el número que se resta, se resta: 90 − ▢ = 35 es 90 − 35 = 55. Siempre piensa en cuál de los tres números es el total y qué falta. Después elige la operación y comprueba el resultado en la ecuación original.",
    ],
    vocab=[("término desconocido", "número que falta, escrito como ▢"), ("total", "el número que se obtiene al juntar las partes"), ("parte", "uno de los números que se juntan"), ("ecuación", "igualdad con un número desconocido, como ▢ + 25 = 63"), ("comprobar", "reemplazar el número encontrado y revisar que se cumple")],
    worked=[
        {"title": "Falta un sumando", "problem": "Encuentra el número: ▢ + 25 = 63.", "steps": ["63 es el total y 25 es una parte.", "La otra parte es 63 − 25 = 38.", "Compruebo: 38 + 25 = 63."], "answer": "38"},
        {"title": "Falta el primer número de una resta", "problem": "Encuentra el número: ▢ − 45 = 30.", "steps": ["En la resta, el primer número es el total.", "Total = 30 + 45 = 75.", "Compruebo: 75 − 45 = 30."], "answer": "75"},
    ],
    mistakes=[
        {"wrong": "Resolver ▢ − 45 = 30 como 45 − 30 = 15.", "why": "Se restan los números que se ven, sin pensar cuál es el total.", "fix": "El número que falta es el total: 30 + 45 = 75."},
        {"wrong": "Resolver 90 − ▢ = 35 como 90 + 35 = 125.", "why": "Se suma porque falta un número, sin ver que el 90 es el total.", "fix": "90 es el total; 90 − 35 = 55."},
    ],
    tiers={
        "recovery": [
            ex("Encuentra el número: ▢ + 27 = 61.", "34", "61 − 27 = 34."),
            ex("Encuentra el número: 40 + ▢ = 90.", "50", "90 − 40 = 50."),
            ex("Encuentra el número: ▢ − 5 = 10.", "15", "10 + 5 = 15."),
        ],
        "understand": [
            ex("Para hallar el sumando que falta en ▢ + 25 = 63, ¿haces 63 + 25 o 63 − 25?", "63 − 25", "63 es el total y se le quita una parte."),
            ex("Para hallar el número en ▢ − 45 = 30, ¿haces 30 + 45 o 30 − 45?", "30 + 45", "El número que falta es el total."),
            ex("En 90 − ▢ = 35, ¿qué cálculo encuentra el número?", "90 − 35", "El total 90 menos la parte conocida."),
        ],
        "apply": [
            ex("Encuentra el número: ▢ + 148 = 500.", "352", "500 − 148 = 352."),
            ex("Encuentra el número: 623 − ▢ = 245.", "378", "623 − 245 = 378."),
            ex("Encuentra el número: ▢ − 175 = 320.", "495", "320 + 175 = 495."),
        ],
        "reason": [
            ex("Pedro resolvió ▢ − 45 = 30 y escribió 15, porque hizo 45 − 30. ¿Qué error cometió y cuál es el número?", "Debía sumar; es 75", "El número que falta es el total: 30 + 45."),
            ex("Rosa dice que en 90 − ▢ = 35 el número es 125 (90 + 35). ¿Tiene razón?", "No; es 55", "90 − 55 = 35."),
        ],
        "challenge": [
            ex("Encuentra el número: ▢ − 238 = 417.", "655", "417 + 238 = 655."),
            ex("Encuentra el número: 806 − ▢ = 449.", "357", "806 − 449 = 357."),
        ],
    },
    context=[ex("A Marta le regalaron 25 figuritas y ahora tiene 63. ¿Cuántas tenía antes del regalo?", "38", "63 − 25 = 38.")],
    selfcheck=[
        ex("Encuentra el número: 18 + ▢ = 50.", "32", "50 − 18 = 32."),
        ex("Encuentra el número: ▢ − 20 = 45.", "65", "45 + 20 = 65."),
        ex("Encuentra el número: 70 − ▢ = 28.", "42", "70 − 28 = 42."),
    ],
    open_task=task(
        "Resuelve estos tres enigmas y comprueba cada uno: ▢ + 36 = 90; ▢ − 52 = 40; 130 − ▢ = 85. Escribe qué número es el total en cada caso.",
        "▢ + 36 = 90: el total es 90; 90 − 36 = 54. ▢ − 52 = 40: el total es el número que falta; 40 + 52 = 92. 130 − ▢ = 85: el total es 130; 130 − 85 = 45.",
        ["resuelve los tres", "dice quién es el total", "usa la operación correcta", "comprueba reemplazando"],
        ["cálculos en el cuaderno", "frases con el total y la comprobación"],
        ["sumar donde corresponde restar", "no comprobar"],
        "Reconoce que identificó el total y pide leer la comprobación; si hay error, que arme la familia con los tres números.",
    ),
    reinforce="Con tapas, esconde parte de 10 tapas bajo un vaso y adivina cuántas hay debajo: siempre comprueba restando.",
    extend="Inventa tres enigmas con ▢ cuyas respuestas sean 20, 45 y 100. Resuélvelos.",
)

register(
    OA7, 4,
    materials="Lápiz y cuaderno. Todos los datos están escritos en cada problema. Puedes dibujar una caja con partes y total.",
    use="Aprenderé a resolver problemas en que lo que se busca es el estado inicial o lo que ocurrió, usando la familia de operaciones. Sirve para saber cuánto había antes o cuánto cambió.",
    prior=["Sé encontrar el término desconocido.", "Sé escribir la familia de una suma."],
    explain=[
        "En un problema inverso la pregunta pide algo que ocurrió antes. «Tenía fichas, perdí 35 y me quedan 48. ¿Cuántas tenía?» Aquí falta el número inicial. Escribe ▢ − 35 = 48. El total es lo que tenía al inicio, entonces es 48 + 35 = 83.",
        "Mira otro: «Había pasajeros en un bus, subieron 15 y ahora hay 60». Escribe ▢ + 15 = 60. Ahora 60 es el total, entonces antes había 60 − 15 = 45. No tiene sentido hacer 60 + 15, porque sería un número mayor que el total.",
        "Para decidir, pregúntate: ¿lo que busco es el total o una parte? Si busco una parte, resta; si busco un total, suma. Después comprueba que tu respuesta cuenta bien la historia: 83 − 35 = 48 y 45 + 15 = 60.",
    ],
    vocab=[("problema inverso", "problema donde se busca lo que había antes o lo que cambió"), ("estado inicial", "cantidad que había al comienzo"), ("cambio", "lo que se agrega o se quita"), ("estado final", "cantidad que hay al terminar"), ("familia de operaciones", "suma y resta con los mismos tres números")],
    worked=[
        {"title": "Buscar lo que había al inicio (quité)", "problem": "Tenía fichas, perdí 35 y me quedan 48. ¿Cuántas tenía?", "steps": ["Escribo ▢ − 35 = 48.", "Lo que tenía es el total: 48 + 35 = 83.", "Compruebo: 83 − 35 = 48."], "answer": "83 fichas"},
        {"title": "Buscar lo que había al inicio (agregué)", "problem": "En un bus subieron 15 pasajeros y ahora hay 60. ¿Cuántos había antes?", "steps": ["Escribo ▢ + 15 = 60.", "60 es el total; antes había 60 − 15 = 45.", "Compruebo: 45 + 15 = 60."], "answer": "45 pasajeros"},
    ],
    mistakes=[
        {"wrong": "Resolver «Tenía fichas, perdí 35 y me quedan 48» con 48 − 35 = 13.", "why": "Se resta sin pensar que falta el número inicial.", "fix": "Lo que tenía es más que lo que quedó: 48 + 35 = 83."},
        {"wrong": "Resolver «subieron 15 y ahora hay 60» con 60 + 15 = 75.", "why": "Se suma lo que subió al total que ya incluye a esas personas.", "fix": "60 ya incluye a los 15; antes había 60 − 15 = 45."},
    ],
    tiers={
        "recovery": [
            arith("Tenía lápices, regalé 40 y me quedan 56. ¿Cuántos tenía?", "56+40", "Lo que tenía es lo que quedó más lo que regalé."),
            arith("Juan ahorró dinero y gastó 20. Le quedan 45. ¿Cuánto había ahorrado?", "45+20", "Había ahorrado lo que gastó más lo que le quedó."),
            arith("Un bus tiene 60 pasajeros después de que subieron 15. ¿Cuántos había antes?", "60-15", "Antes de subir 15, había 15 menos."),
        ],
        "understand": [
            ex("En «Tenía fichas, perdí 35 y me quedan 48», ¿se resuelve con suma o con resta?", "Con suma: 48 + 35", "Falta lo que tenía antes de perder."),
            ex("En «Había pasajeros, subieron 15 y ahora hay 60», ¿suma o resta?", "Resta: 60 − 15", "El total ya incluye a los que subieron."),
            ex("En «Gasté 120 y me quedan 380», ¿qué cantidad es desconocida?", "La cantidad inicial", "Se pregunta cuánto tenía antes de gastar."),
        ],
        "apply": [
            arith("Una biblioteca tiene 825 libros después de comprar 140. ¿Cuántos tenía antes de comprar?", "825-140", "Antes de comprar, tenía 140 menos."),
            arith("Después de vender 235 entradas, quedan 365. ¿Cuántas entradas había?", "365+235", "Había lo que quedó más lo que se vendió."),
            arith("Un estanque tiene 480 litros después de sacar 120. ¿Cuántos litros tenía antes?", "480+120", "Tenía lo que queda más lo que se sacó."),
        ],
        "reason": [
            ex("Dani dice que en «Tenía fichas, perdí 35 y me quedan 48» la respuesta es 13. ¿Tiene razón?", "No; son 83", "Debía tener más que 48, no menos."),
            ex("Problema A: «Tengo 70 y regalo 25». Problema B: «Regalé 25 y me quedan 70». ¿Cuál se resuelve sumando 70 + 25?", "El B", "En B falta lo que tenía al inicio."),
        ],
        "challenge": [
            ex("Ema tenía dinero. Gastó 125 y luego recibió 80. Ahora tiene 300. ¿Cuánto tenía al inicio?", "345", "300 − 80 = 220 y 220 + 125 = 345."),
            ex("Pedro pegó láminas en un álbum de 500 y le faltan 135. ¿Cuántas pegó?", "365", "500 − 135 = 365."),
        ],
    },
    context=[arith("En un teatro hay 640 personas después de que entraron 210 más. ¿Cuántas personas había antes?", "640-210", "Antes de entrar 210, había 210 menos.")],
    selfcheck=[
        ex("Tenía figuritas, regalé 30 y me quedan 50. ¿Cuántas tenía?", "80", "50 + 30 = 80."),
        ex("Llegaron 40 personas y ahora hay 100. ¿Cuántas había antes?", "60", "100 − 40 = 60."),
        ex("En «Compré 5 y ahora tengo 12», ¿cuántas tenía antes?", "7", "12 − 5 = 7."),
    ],
    open_task=task(
        "Resuelve estos dos problemas y comprueba cada uno: A) Una tienda vendió 175 cuadernos y le quedan 325, ¿cuántos tenía? B) Un cine recibió 90 personas más y ahora hay 250, ¿cuántas había antes? Luego inventa un problema inverso con el número 100 y resuélvelo.",
        "A) ▢ − 175 = 325; 325 + 175 = 500 cuadernos. Compruebo: 500 − 175 = 325. B) ▢ + 90 = 250; 250 − 90 = 160 personas. Compruebo: 160 + 90 = 250. Mi problema: «Tenía fichas, perdí 40 y me quedan 100». 100 + 40 = 140.",
        ["resuelve A con 500", "resuelve B con 160", "comprueba ambos", "inventa un problema inverso coherente"],
        ["ecuaciones escritas", "comprobaciones", "problema inventado"],
        ["restar donde corresponde sumar", "inventar sin dato inicial"],
        "Reconoce el uso de la familia y pide leer la ecuación de cada problema; si hay error, que dibuje la caja de partes y total.",
    ),
    reinforce="Con 20 tapas escondidas en parte bajo un vaso, practica: ves 12 tapas y sabes que bajo el vaso hay otras. ¿Cuántas hay si en total son 20?",
    extend="Explica con tus palabras cómo reconoces, en un problema, si lo que falta es el total o una parte.",
)
