"""Student material for 2.º básico Matemática, OA 03 (comparación y orden hasta 100, con monedas)."""
from __future__ import annotations

from student_content_ma02_a import bars
from student_content_ma02_c import KEY, OA3, cmp_ex, sign
from student_lessons import arith, ex, register


def order_ex(values: list[int], why: str) -> dict:
    asc = ", ".join(str(v) for v in sorted(values))
    return ex(f"Ordena de menor a mayor: {', '.join(str(v) for v in values)}.", asc, why)


register(
    OA3, 1,
    materials=f"Barras y cubos dibujados en este cuaderno. {KEY} Los números a comparar están escritos en cada ejercicio.",
    use="Aprenderé a comparar dos números mirando primero las decenas. Sirve para saber quién tiene más figuritas, puntos o dinero.",
    prior=["Sé representar números con barras y cubos.", "Conozco los signos mayor que (>), menor que (<) e igual (=)."],
    explain=[
        "Para comparar dos números de dos cifras, mira primero las decenas, que son la cifra de la izquierda. El número con más decenas es el mayor. Así, 47 es mayor que 39, porque 47 tiene 4 decenas y 39 tiene sólo 3.",
        "No importa que 9 sea una unidad más grande que 7: las decenas valen mucho más que las unidades. Por eso 47 > 39 aunque 9 > 7. En el dibujo se ve fácil: cuatro barras de 10 son más que tres barras de 10 con cualquier cantidad de cubos sueltos menor que 10.",
        "Los signos > y < se leen como una boca que se abre hacia el número mayor: 47 > 39 se lee «cuarenta y siete es mayor que treinta y nueve», y 39 < 47 se lee «treinta y nueve es menor que cuarenta y siete».",
    ],
    vocab=[("mayor que (>)", "tiene más cantidad"), ("menor que (<)", "tiene menos cantidad"), ("igual (=)", "tiene la misma cantidad"), ("decenas", "la cifra de la izquierda en un número de dos cifras"), ("comparar", "decidir cuál número es mayor, menor o si son iguales")],
    worked=[
        {"title": "Comparar mirando las decenas", "problem": "Compara 47 y 39.", "steps": [f"Dibujo 47: {bars(47)}.", f"Dibujo 39: {bars(39)}.", "Miro las decenas: 4 decenas y 3 decenas. 4 es mayor que 3.", "Entonces 47 > 39."], "answer": "47 > 39"},
        {"title": "Cuando las unidades engañan", "problem": "Compara 61 y 59. Las unidades de 59 son mayores.", "steps": ["Comparo primero las decenas: 6 decenas y 5 decenas.", "6 es mayor que 5, entonces el primero es mayor.", "No miro las unidades porque las decenas ya decidieron.", "61 > 59."], "answer": "61 > 59"},
    ],
    mistakes=[
        {"wrong": "Decir que 39 > 47 porque 9 es mayor que 7.", "why": "Se comparan primero las unidades.", "fix": "Compara siempre primero la cifra de las decenas."},
        {"wrong": "Escribir 47 < 39.", "why": "Se confunde la dirección del signo.", "fix": "El signo se abre hacia el número mayor: 47 > 39."},
    ],
    tiers={
        "recovery": [cmp_ex(52, 38, "52 tiene 5 decenas y 38 sólo 3."), cmp_ex(27, 61, "27 tiene 2 decenas y 61 tiene 6."), cmp_ex(74, 45, "74 tiene 7 decenas, más que 4.")],
        "understand": [
            ex("¿Qué cifra comparas primero en números de dos cifras?", "La de las decenas", "Las decenas valen más que las unidades."),
            ex("¿Qué número es mayor, 83 o 79?", "83", "8 decenas es mayor que 7 decenas."),
            ex("¿Qué número es menor, 18 o 41?", "18", "1 decena es menor que 4 decenas."),
        ],
        "apply": [cmp_ex(66, 59, "6 decenas es mayor que 5 decenas."), cmp_ex(18, 81, "1 decena es menor que 8 decenas."), cmp_ex(90, 89, "9 decenas es mayor que 8 decenas aunque 89 tenga 9 unidades.")],
        "reason": [
            ex("Dani dice que 39 > 41 porque 9 > 1. ¿Qué error comete?", "Compara las unidades antes que las decenas", "3 decenas es menor que 4 decenas, entonces 39 < 41."),
            ex("Dos números tienen las mismas decenas. ¿Se pueden comparar mirando sólo las decenas?", "No; hay que mirar las unidades", "Si las decenas son iguales, decide la siguiente cifra."),
        ],
        "challenge": [
            ex("Escribe un número mayor que 58 pero menor que 61.", "59 o 60", "Entre 58 y 61 están 59 y 60."),
            ex("Escribe un número de dos cifras que sea menor que 20 y que tenga 5 unidades.", "15", "15 tiene 1 decena y 5 unidades, y es menor que 20."),
        ],
    },
    context=[ex("Ana tiene 47 figuritas y Beto tiene 39. ¿Quién tiene más? ¿Cuántas más?", "Ana tiene más; 8 más", "47 > 39 y 47 − 39 = 8.")],
    selfcheck=[cmp_ex(60, 45, "6 decenas es mayor que 4 decenas."), ex("¿Qué se mira primero para comparar 34 y 51?", "Las decenas", "3 decenas es menor que 5 decenas."), ex("¿Cuál signo va: 29 __ 31?", "<", "2 decenas es menor que 3 decenas.")],
    open_task={
        "statement": "Compara los pares 48 y 53, 76 y 67, y 35 y 35. Para cada par escribe el signo correcto, dibuja con barras y cubos uno de los números y explica tu decisión.",
        "example": "48 < 53 porque 4 decenas es menor que 5 decenas. 76 > 67 porque 7 decenas es mayor que 6 decenas. 35 = 35 porque tienen las mismas decenas y unidades. Dibujo de 48: " + bars(48) + ".",
        "criteria": ["usa el signo correcto en los tres pares", "compara primero las decenas", "dibuja correctamente", "explica con decenas"],
        "evidence": ["signos escritos", "dibujo", "explicación"],
        "errors": ["comparar unidades primero", "invertir el signo"],
        "feedback": "Pide leer cada comparación en voz alta usando «mayor que» o «menor que»; reconoce el uso de las decenas.",
    },
    reinforce="Con tarjetas de 10 a 99, saca dos y di cuál es mayor mirando las decenas.",
    extend="Escribe cinco pares de números donde las unidades del número menor sean mayores que las del mayor (como 39 y 41).",
)

register(
    OA3, 2,
    materials=f"Barras y cubos dibujados en este cuaderno. {KEY}",
    use="Aprenderé a comparar dos números que tienen las mismas decenas, mirando las unidades. Sirve para decidir con precisión cuando los números son parecidos.",
    prior=["Sé comparar dos números mirando las decenas.", "Sé usar los signos >, < e =."],
    explain=[
        "Si dos números tienen las mismas decenas, ya no puedes decidir por ellas. Por ejemplo, 52 y 58 tienen 5 decenas cada uno. Ahora mira las unidades: 2 y 8. Como 2 es menor que 8, 52 es menor que 58.",
        "En el dibujo se ve que las barras son iguales: ▮ ▮ ▮ ▮ ▮. La diferencia está en los cubos sueltos: 52 tiene 2 y 58 tiene 8. Quien tiene más cubos sueltos tiene el número mayor.",
        "La regla completa es: primero compara las decenas; si son iguales, compara las unidades; si también son iguales, los números son iguales.",
    ],
    vocab=[("mismas decenas", "la cifra de la izquierda es igual en ambos números"), ("unidades", "la cifra de la derecha"), ("empate", "cuando las decenas son iguales y hay que mirar las unidades"), ("igual", "tienen la misma cantidad"), ("regla", "pasos para comparar siempre bien")],
    worked=[
        {"title": "Desempatar con las unidades", "problem": "Compara 52 y 58.", "steps": ["Las decenas son 5 y 5: iguales.", "Comparo las unidades: 2 y 8.", "2 < 8, entonces 52 < 58.", f"Compruebo con dibujos: {bars(52)} y {bars(58)}."], "answer": "52 < 58"},
        {"title": "Completar un signo", "problem": "Elige el signo: 73 __ 73.", "steps": ["Decenas: 7 y 7, son iguales.", "Unidades: 3 y 3, son iguales.", "Los números son iguales."], "answer": "73 = 73"},
    ],
    mistakes=[
        {"wrong": "Decir que 52 y 58 son iguales porque tienen la misma decena.", "why": "No se miran las unidades.", "fix": "Si las decenas son iguales, hay que comparar las unidades."},
        {"wrong": "Comparar las unidades antes de las decenas.", "why": "Se salta la regla de orden.", "fix": "Primero decenas; luego unidades."},
    ],
    tiers={
        "recovery": [cmp_ex(52, 58, "Mismas decenas; 2 es menor que 8."), cmp_ex(34, 31, "Mismas decenas; 4 es mayor que 1."), cmp_ex(66, 66, "Las decenas y las unidades son iguales.")],
        "understand": [
            ex("52 y 58 tienen las mismas decenas. ¿Qué cifra decide cuál es mayor?", "La de las unidades", "Con decenas iguales, decide la cifra siguiente."),
            ex("¿Cuál es mayor: 45 o 49?", "49", "Mismas decenas y 9 es mayor que 5."),
            ex("¿Cuál es menor: 71 o 78?", "71", "Mismas decenas y 1 es menor que 8."),
        ],
        "apply": [cmp_ex(23, 29, "Mismas decenas; 3 es menor que 9."), cmp_ex(87, 82, "Mismas decenas; 7 es mayor que 2."), cmp_ex(90, 99, "Mismas decenas; 0 es menor que 9.")],
        "reason": [
            ex("Romina dice que 41 > 48 porque 1 < 8. ¿Qué error comete?", "Invirtió el signo: 41 < 48", "Con mismas decenas y 1 < 8, el menor es 41."),
            ex("¿Puede ser 56 mayor que 61? Explica.", "No", "56 tiene 5 decenas y 61 tiene 6 decenas."),
        ],
        "challenge": [
            ex("Escribe tres números mayores que 42 pero con 4 decenas.", "43, 44, 45 (u otros hasta 49)", "Con 4 decenas y unidades mayores que 2."),
            ex("¿Cuántos números entre 30 y 40 son mayores que 35?", "4 números: 36, 37, 38 y 39", "Mayores que 35 y con 3 decenas: 36, 37, 38 y 39."),
        ],
    },
    context=[ex("En un curso, Camila lee 52 páginas y Pablo lee 58. ¿Quién leyó más páginas? ¿Cuántas más?", "Pablo; 6 más", "58 > 52 y 58 − 52 = 6.")],
    selfcheck=[cmp_ex(19, 15, "Mismas decenas; 9 es mayor que 5."), cmp_ex(77, 70, "Mismas decenas; 7 es mayor que 0."), ex("¿Qué miras si las decenas son iguales?", "Las unidades", "Es la siguiente cifra de la derecha.")],
    open_task={
        "statement": "Compara 64 y 68, 35 y 38, 90 y 90. Dibuja con barras y cubos 64 y 68, escribe el signo y explica qué cifra decidió.",
        "example": f"64 < 68 porque las decenas son iguales y 4 < 8. 35 < 38 porque 5 < 8. 90 = 90. Dibujo: {bars(64)} y {bars(68)}.",
        "criteria": ["signos correctos", "dibujos coherentes", "nombra la cifra que decidió"],
        "evidence": ["signos", "dibujos", "explicación"],
        "errors": ["decidir sin mirar las unidades", "dibujar barras distintas para números con las mismas decenas"],
        "feedback": "Pide señalar en el dibujo la parte que cambia (los cubos sueltos); reconoce la explicación con unidades.",
    },
    reinforce="Con dos dados, arma números de dos cifras (primero decenas, luego unidades) y compáralos.",
    extend="Crea tres comparaciones con las mismas decenas y signos distintos, y comprueba cada una con material.",
)

register(
    OA3, 3,
    materials="Monedas dibujadas de $1, $5, $10 y $50 (las cantidades de cada ejercicio están escritas) y el cuaderno.",
    use="Aprenderé a comparar cantidades de dinero formadas por monedas chilenas. Sirve para saber quién tiene más dinero y qué puedo comprar.",
    prior=["Sé comparar números de dos cifras.", "Conozco las monedas de $1, $5, $10 y $50."],
    explain=[
        "En Chile usamos monedas de distinto valor: $1, $5, $10 y $50. Para comparar dinero primero hay que saber cuánto vale lo que hay. Si tienes 3 monedas de $10 y 2 monedas de $5, tienes $30 y $10: en total $40.",
        "Después de calcular el total de cada persona, compara los dos números como lo has hecho: primero las decenas y luego las unidades. Así puedes decir quién tiene más.",
        "Ojo: tener más monedas no siempre significa tener más dinero. Cuatro monedas de $1 son $4, y una moneda de $10 es $10. Lo que cuenta es el valor, no cuántas monedas hay.",
    ],
    vocab=[("moneda", "pieza de metal con un valor, como $10"), ("valor", "cuánto dinero representa"), ("total", "el dinero de todas las monedas juntas"), ("peso", "unidad del dinero en Chile, se escribe con $"), ("comparar", "decidir quién tiene más o menos")],
    worked=[
        {"title": "Calcular el total", "problem": "Tomás tiene 3 monedas de $10 y 2 monedas de $5. ¿Cuánto dinero tiene?", "steps": ["Tres monedas de $10: $30.", "Dos monedas de $5: $5 + $5 = $10.", "Sumo: $30 + $10 = $40."], "answer": "$40"},
        {"title": "Comparar dos totales", "problem": "Tomás tiene $40 y Elisa tiene 4 monedas de $5 y 3 monedas de $10. ¿Quién tiene más?", "steps": ["Elisa: 4 × $5 = $20 y 3 × $10 = $30.", "Total de Elisa: $20 + $30 = $50.", "Comparo $40 y $50: 4 decenas < 5 decenas.", "Elisa tiene más."], "answer": "Elisa, con $10 más"},
    ],
    mistakes=[
        {"wrong": "Decir que quien tiene más monedas tiene más dinero.", "why": "Se compara la cantidad de monedas y no su valor.", "fix": "Calcula el total en pesos de cada uno y compara esos totales."},
        {"wrong": "Contar todas las monedas como $1.", "why": "No se reconoce el valor de cada moneda.", "fix": "Una moneda de $10 vale 10 pesos; una de $5 vale 5."},
    ],
    tiers={
        "recovery": [
            arith("Tengo 2 monedas de $10. ¿Cuánto dinero tengo?", "2*10", "Dos monedas de $10 son $20."),
            arith("Tengo 3 monedas de $5. ¿Cuánto dinero tengo?", "3*5", "Tres monedas de $5 son $15."),
            arith("Tengo una moneda de $50 y una de $10. ¿Cuánto dinero tengo?", "50+10", "$50 y $10 hacen $60."),
        ],
        "understand": [
            ex("¿Vale más una moneda de $10 o cuatro monedas de $1?", "Una moneda de $10", "$10 es mayor que $4."),
            ex("¿Vale lo mismo una moneda de $50 y cinco monedas de $10?", "Sí", "5 × $10 = $50."),
            ex("¿Importa cuántas monedas hay para saber quién tiene más dinero?", "No; importa el valor total", "El valor cambia con cada moneda."),
        ],
        "apply": [
            ex("Sofía tiene 2 monedas de $50. Mateo tiene 7 monedas de $10. ¿Quién tiene más?", "Sofía ($100) frente a Mateo ($70)", "2 × $50 = $100 y 7 × $10 = $70; 100 > 70."),
            ex("Ana tiene 4 monedas de $5 y 3 de $1. Luis tiene 2 monedas de $10. ¿Cuánto tiene cada uno y quién tiene más?", "Ana $23; Luis $20; Ana tiene más", "4 × 5 + 3 = 23 y 2 × 10 = 20."),
            cmp_ex(45, 54, "4 decenas es menor que 5 decenas."),
        ],
        "reason": [
            ex("Pía tiene 9 monedas de $1 y Rafa tiene 2 monedas de $10. Pía dice que ella tiene más. ¿Tiene razón?", "No", "Pía tiene $9 y Rafa $20."),
            ex("¿Por qué 3 monedas de $10 valen más que 5 monedas de $5?", "Porque $30 es mayor que $25", "3 × 10 = 30 y 5 × 5 = 25."),
        ],
        "challenge": [
            ex("Quiero formar exactamente $35 con monedas de $10 y de $5. Escribe una forma.", "3 monedas de $10 y 1 de $5", "30 + 5 = 35."),
            ex("Con 6 monedas, todas de $5 o de $10, ¿cuál es el mayor dinero posible y cuál el menor?", "$60 y $30", "6 × 10 = 60 y 6 × 5 = 30."),
        ],
    },
    context=[ex("Un helado cuesta $50. Valentina tiene 4 monedas de $10 y 2 monedas de $5. ¿Le alcanza para comprarlo?", "Sí; tiene exactamente $50", "Valentina tiene $40 + $10 = $50, igual al precio, por eso le alcanza justo.")],
    selfcheck=[ex("¿Cuánto son 2 monedas de $5 y 1 de $10?", "$20", "10 + 10 = 20."), ex("¿Qué es más: $45 o $54?", "$54", "5 decenas es mayor que 4 decenas."), ex("¿Cuántas monedas de $10 hacen $50?", "5", "5 × 10 = 50.")],
    open_task={
        "statement": "Dos amigos tienen monedas. Lola: 3 monedas de $10, 1 de $5 y 4 de $1. Ian: 2 monedas de $10 y 3 de $5. Calcula el total de cada uno, compáralos con un signo y escribe quién tiene más y cuánto más.",
        "example": "Lola: 30 + 5 + 4 = $39. Ian: 20 + 15 = $35. $39 > $35. Lola tiene $4 más.",
        "criteria": ["calcula bien ambos totales", "compara con el signo correcto", "indica quién tiene más y cuánto"],
        "evidence": ["cálculo de cada total", "signo", "frase con la diferencia"],
        "errors": ["contar monedas como $1", "comparar la cantidad de monedas"],
        "feedback": "Pide que explique por qué no basta con contar monedas; reconoce el cálculo ordenado de los totales.",
    },
    reinforce="Arma con monedas de juguete o papel $23, $35 y $41 de dos maneras distintas.",
    extend="Averigua cuántas formas hay de pagar $20 con monedas de $10 y $5.",
)

register(
    OA3, 4,
    materials="Tarjetas de números en este cuaderno: 52, 25, 63, 36, 41, 14, 78, 87; cinta con casillas para ordenar.",
    use="Aprenderé a ordenar varios números de menor a mayor y a cumplir condiciones al ordenarlos. Sirve para organizar listas, puntajes y resultados.",
    prior=["Sé comparar dos números.", "Sé que menor a mayor es del más pequeño al más grande."],
    explain=[
        "Para ordenar varios números, compáralos de a pares. Primero encuentra el menor, luego el siguiente menor y así hasta el mayor. Para listas largas conviene mirar primero las decenas y agrupar los números con las mismas.",
        "Por ejemplo, para ordenar 52, 25, 63 y 36: las decenas son 5, 2, 6 y 3. Ordeno por decenas: 25 (2), 36 (3), 52 (5), 63 (6). Si dos números tienen las mismas decenas, desempato por las unidades.",
        "Algunas tareas piden condiciones: «un número mayor que 35 y menor que 41». Revisa en la lista los números que cumplen ambas condiciones. Debes comprobar las dos al mismo tiempo; si una falla, ese número no sirve.",
    ],
    vocab=[("ordenar", "poner en fila según un criterio"), ("de menor a mayor", "del más pequeño al más grande"), ("de mayor a menor", "del más grande al más pequeño"), ("condición", "regla que un número debe cumplir"), ("entre", "mayor que uno y menor que otro")],
    worked=[
        {"title": "Ordenar cuatro números", "problem": "Ordena de menor a mayor: 52, 25, 63, 36.", "steps": ["Decenas: 52→5, 25→2, 63→6, 36→3.", "Menor decena: 25. Luego 36, 52 y 63.", "Escribo la lista: 25, 36, 52, 63."], "answer": "25, 36, 52, 63"},
        {"title": "Cumplir dos condiciones", "problem": "Elige el número que es mayor que 35 y menor que 41: 33, 38, 44, 40.", "steps": ["Mayor que 35: 38, 44 y 40.", "Menor que 41: 33, 38 y 40.", "Cumple ambas: 38 y 40."], "answer": "38 y 40"},
    ],
    mistakes=[
        {"wrong": "Ordenar 36, 41, 14 como 14, 41, 36.", "why": "Se miró sólo la primera cifra de 41 sin comparar 3 y 4.", "fix": "Compara las decenas: 1, 3, 4; el orden correcto es 14, 36, 41."},
        {"wrong": "Cumplir sólo una de las condiciones.", "why": "Se revisa una condición y se olvida la otra.", "fix": "Revisa las dos condiciones en cada número."},
    ],
    tiers={
        "recovery": [order_ex([52, 25, 63, 36], "Se ordenan por decenas: 2, 3, 5, 6."), order_ex([41, 14, 78, 87], "Decenas: 1, 4, 7, 8."), order_ex([61, 59, 60], "59 tiene 5 decenas; 60 y 61 tienen 6 decenas y 0 es menor que 1.")],
        "understand": [
            ex("¿Qué significa «de menor a mayor»?", "Del más pequeño al más grande", "Se empieza por el número con menos cantidad."),
            ex("¿Qué significa «mayor que 35 y menor que 41»?", "Un número entre 36 y 40", "Debe cumplir las dos condiciones."),
            ex("Si dos números tienen las mismas decenas, ¿qué miras para ordenarlos?", "Las unidades", "Con decenas iguales decide la cifra de la derecha."),
        ],
        "apply": [
            ex("Ordena de mayor a menor: 41, 14, 78, 87.", "87, 78, 41, 14", "Decenas: 8, 7, 4, 1."),
            ex("De la lista 22, 38, 44, 29, ¿cuáles son mayores que 25 y menores que 40?", "38 y 29", "Ambos están entre 25 y 40."),
            ex("Ordena de menor a mayor: 27, 72, 22, 77.", "22, 27, 72, 77", "Primero 2 decenas (22, 27), luego 7 decenas (72, 77)."),
        ],
        "reason": [
            ex("Marcos ordenó 36, 41, 14 como 14, 41, 36. ¿Dónde está el error?", "41 debe ir después de 36", "36 tiene 3 decenas y 41 tiene 4."),
            ex("¿Existe un número mayor que 58 y menor que 60?", "Sí, el 59", "Es el único entero entre 58 y 60."),
        ],
        "challenge": [
            ex("Escribe tres números entre 70 y 80 y ordénalos de mayor a menor.", "Por ejemplo 78, 75, 71", "Todos están entre 70 y 80 y van de mayor a menor."),
            ex("Quiero un número de dos cifras con 5 decenas, mayor que 55 y menor que 58. ¿Cuál es?", "56 o 57", "Con 5 decenas, está entre 55 y 58."),
        ],
    },
    context=[ex("En una carrera, cuatro niños tardaron 52, 45, 49 y 51 segundos. Ordénalos de menor a mayor y di quién ganó (el que tardó menos).", "45, 49, 51, 52; ganó el de 45", "Menor tiempo significa llegar antes.")],
    selfcheck=[order_ex([30, 13, 31], "13 tiene 1 decena y 30 y 31 tienen 3."), ex("Elige el mayor: 59, 61, 60.", "61", "6 decenas es mayor que 5."), ex("Elige un número mayor que 20 y menor que 23.", "21 o 22", "Está entre 20 y 23.")],
    open_task={
        "statement": "Ordena de menor a mayor los números 47, 74, 44, 77. Luego busca todos los que son mayores que 45 y menores que 75. Explica cómo ordenaste.",
        "example": "Ordenados: 44, 47, 74, 77. Mayores que 45 y menores que 75: 47 y 74. Ordené mirando primero las decenas (4 y 7) y luego las unidades.",
        "criteria": ["orden correcto", "elige ambos números", "explica el procedimiento"],
        "evidence": ["lista ordenada", "números elegidos", "explicación"],
        "errors": ["mirar sólo la primera cifra de cada número", "olvidar una condición"],
        "feedback": "Si el orden es incorrecto, pide que compare de a dos y registre cada comparación; reconoce el desempate por unidades.",
    },
    reinforce="Con 6 tarjetas de números, ordénalas y fotografía o dibuja el resultado.",
    extend="Crea una condición doble que sólo cumpla un número en la lista 41, 44, 47, 49 y explica por qué.",
)
