"""Cuaderno del estudiante de 5.º básico Matemática: OA 08 (fracciones impropias y números mixtos) y OA 09 (suma y resta de fracciones propias)."""
from __future__ import annotations

from student_content_ma05_a import M, W, f, lesson, task
from student_lessons import arith, ex

OA8 = "MA05 OA 08"
OA9 = "MA05 OA 09"


def mix(n, d):
    """Fracción n/d como número mixto, escrito como texto."""
    q, r = divmod(n, d)
    return f"{q} {r}/{d}" if r else str(q)


def imp(q, r, d):
    """Número mixto q r/d como fracción impropia, escrita como texto."""
    return f"{q * d + r}/{d}"


# ------------------------------------------------------------------ OA 08 clase 1
lesson(
    OA8, 1,
    use="Aprenderé a representar fracciones impropias con material, dibujos y símbolos. Sirve para hablar de cantidades que son más que un entero, como 7 cuartos de pizza.",
    prior=["Sé representar fracciones propias.", "Sé que el denominador cuenta las partes iguales de un entero."],
    explain=[
        "Una fracción impropia tiene el numerador mayor o igual que el denominador, por ejemplo 7/4 o 6/6. Representa un entero completo o más. En 7/4, el denominador 4 dice que cada entero se divide en 4 partes iguales, y el numerador 7 dice que se toman 7 de esas partes.",
        "Para dibujarla, usa tantas figuras iguales como necesites. Con 7/4 se dibujan dos figuras divididas en cuartos. La primera se sombrea completa (4 cuartos) y la segunda con 3 cuartos sombreados: ■■■■ y ■■■□. En total hay 7 cuartos sombreados, es decir un entero y tres cuartos más.",
        "Las fracciones impropias que usamos más son las que tienen denominador 2, 3, 4, 5, 6, 8, 10 y 12. Cuando el numerador es igual al denominador, la fracción vale exactamente un entero, como 6/6. Cuando es mayor, vale más que un entero. Siempre la parte de abajo cuenta las partes de un entero.",
    ],
    vocab=[("fracción impropia", "fracción con numerador mayor o igual que el denominador"), ("entero", "la unidad completa que se divide en partes iguales"), ("numerador", "número de arriba: cuántas partes se toman"), ("denominador", "número de abajo: en cuántas partes iguales se divide un entero"), ("más que un entero", "cantidad que supera una unidad completa")],
    worked=[
        W("Representar una fracción impropia", "Dibuja y escribe 7/4.", ["Cada entero se divide en 4 partes iguales.", "Una figura completa: ■■■■ (4 cuartos). Otra con 3: ■■■□.", "En total 4 + 3 = 7 cuartos."], "7/4"),
        W("Escribir la fracción de lo que se ve", "Hay tres figuras iguales divididas en 2 partes. Las dos primeras están completas y la tercera tiene 1 parte sombreada. ¿Qué fracción impropia es?", ["Cada figura tiene 2 mitades.", "Las dos primeras: 2 + 2 = 4 mitades; la tercera: 1 mitad.", "4 + 1 = 5 mitades."], "5/2"),
    ],
    mistakes=[
        M("Decir que 5/3 es menor que 1 porque tiene números pequeños.", "Se miró el tamaño de los números y no la relación entre numerador y denominador.", "5 es mayor que 3, entonces hay más de 3 tercios: 5/3 es más que un entero."),
        M("Dibujar 7/4 con una sola figura de 7 partes.", "El denominador 4 dice que cada entero tiene 4 partes iguales.", "Se necesitan dos figuras de 4 partes cada una."),
    ],
    rec=[
        ex("Se cortan dos pizzas iguales en 4 partes cada una y comes 5 partes en total. ¿Qué fracción de pizza escribes?", "5/4", "Se toman 5 partes de tamaño un cuarto."),
        ex("¿Cuántos cuartos hay en un entero?", "4", "Un entero se divide en 4 cuartos."),
        ex("¿7/4 es mayor, menor o igual que un entero?", "Mayor", "7 es mayor que 4."),
    ],
    und=[
        ex("Se sombrearon ■■■■ y ■■■□, donde cada figura es un entero dividido en 4 partes. ¿Qué fracción impropia representa?", "7/4", "4 + 3 = 7 cuartos."),
        ex("¿Cuántos medios hay en 3 enteros?", "6", "Cada entero tiene 2 medios y 3 × 2 = 6."),
        ex("¿Cuál de estas fracciones es impropia: 3/5, 5/3 o 4/9?", "5/3", "Su numerador es mayor que el denominador."),
    ],
    app=[
        ex("Un vaso es 1/2 litro. Se sirven 7 vasos iguales. ¿Cuántos litros son, escrito como fracción?", "7/2", "7 medios de litro."),
        ex("Una tira está dividida en 8 partes iguales. Se pintan 11 partes en total, pasando a una segunda tira igual. ¿Qué fracción se pintó?", "11/8", "Hay 11 octavos pintados."),
        ex("Escribe «dos enteros» como fracción con denominador 6.", "12/6", "Cada entero tiene 6 sextos y 2 × 6 = 12."),
    ],
    rea=[
        ex("Rita sombrea 7 partes de una sola figura dividida en 4 partes. ¿Es posible?", "No", "Una figura de 4 partes solo tiene 4 partes: necesita otra figura."),
        ex("¿Cuántas fracciones impropias con denominador 4 y numerador menor que 9 existen, contando 4/4?", "5", "Son 4/4, 5/4, 6/4, 7/4 y 8/4."),
    ],
    cha=[
        ex("¿Cuántos cuartos hay en 2 enteros y 1 cuarto más?", "9", "2 × 4 = 8 y 8 + 1 = 9."),
        ex("Una tira de 1/6 de metro se pega varias veces hasta tener 2 metros. ¿Cuántas tiras se usan?", "12", "En cada metro caben 6 tiras y 2 × 6 = 12."),
    ],
    ctx=[ex("Una receta ficticia pide 7 medidas de 1/4 de taza de harina. ¿Qué fracción de taza es en total?", "7/4 de taza", "7 cuartos de taza.")],
    sc=[
        ex("¿Cuántos tercios hay en 2 enteros?", "6", "2 × 3 = 6."),
        ex("¿Qué fracción vale exactamente un entero: 6/6 o 6/7?", "6/6", "Numerador y denominador son iguales."),
        ex("Escribe «cuatro enteros» como fracción con denominador 5.", "20/5", "4 × 5 = 20."),
    ],
    op=task(
        "Elige una de estas fracciones: 7/4, 9/5 o 11/6. Dibuja las figuras necesarias divididas en partes iguales, sombrea la cantidad y explica cuántas figuras completas se ven y cuántas partes sobran.",
        "9/5: dibujo dos figuras de 5 partes. La primera la sombreo completa y en la segunda sombreo 4 partes. Hay 1 figura completa y sobran 4 quintos.",
        ["usa partes iguales", "sombrea la cantidad correcta", "explica enteros y partes"],
        ["dibujo en el cuaderno", "frase de explicación"],
        ["dibujar una sola figura", "partes desiguales"],
        "Pide que cuente las partes sombreadas en total y que verifique que coincidan con el numerador.",
    ),
    reinforce="Con una hoja doblada en 4 partes iguales, representa 5/4 usando dos hojas. Dibuja lo que hiciste.",
    extend="Explica por qué una fracción con numerador igual al denominador vale exactamente un entero.",
)

# ------------------------------------------------------------------ OA 08 clase 2
lesson(
    OA8, 2,
    use="Aprenderé a pasar de una fracción impropia a un número mixto y al revés. Sirve para decir cuántos enteros hay y cuánto sobra.",
    prior=["Sé representar fracciones impropias.", "Sé dividir con resto."],
    explain=[
        "Un número mixto tiene una parte entera y una fracción propia, como 1 3/4. Significa un entero y tres cuartos más. Es otra forma de escribir una fracción impropia. Por ejemplo, 7/4 = 1 3/4.",
        "Para pasar de fracción impropia a número mixto, divide el numerador por el denominador. El cociente es la parte entera y el resto es el nuevo numerador; el denominador no cambia. En 7/4: 7 ÷ 4 = 1 resto 3, entonces 7/4 = 1 3/4.",
        "Para pasar de número mixto a fracción impropia, multiplica la parte entera por el denominador y suma el numerador. En 2 1/3: 2 × 3 = 6 y 6 + 1 = 7, entonces 2 1/3 = 7/3. El denominador se mantiene. Comprueba siempre con un dibujo o con la operación contraria.",
    ],
    vocab=[("número mixto", "número formado por una parte entera y una fracción propia"), ("parte entera", "cuántos enteros completos hay"), ("cociente", "resultado de una división"), ("resto", "lo que sobra en una división"), ("equivalente", "que representa la misma cantidad")],
    worked=[
        W("De impropia a mixto", "Escribe 17/5 como número mixto.", ["17 ÷ 5 = 3 resto 2.", "La parte entera es 3 y la fracción es 2/5.", "Compruebo: 3 × 5 + 2 = 17."], "3 2/5"),
        W("De mixto a impropia", "Escribe 2 1/3 como fracción impropia.", ["Multiplico el entero por el denominador: 2 × 3 = 6.", "Sumo el numerador: 6 + 1 = 7.", "El denominador sigue siendo 3."], "7/3"),
    ],
    mistakes=[
        M("Escribir 3 1/2 como 4/2 sumando 3 + 1 arriba.", "Se sumaron la parte entera y el numerador sin multiplicar por el denominador.", "3 × 2 + 1 = 7, entonces 3 1/2 = 7/2."),
        M("Escribir 13/5 como 2 5/3 porque se mezclaron el resto y el denominador.", "El denominador no cambia al pasar a mixto.", "13 ÷ 5 = 2 resto 3, entonces 13/5 = 2 3/5."),
    ],
    rec=[
        ex("Al dividir 7 ÷ 4 sale cociente 1 y resto 3. ¿Cuál es el número mixto de 7/4?", "1 3/4", "El cociente es la parte entera y el resto es el nuevo numerador."),
        ex("En el número mixto 2 1/3, ¿cuál es la parte entera?", "2", "El número que está a la izquierda de la fracción."),
        ex("¿Cuántos tercios hay en 2 enteros?", "6", "2 × 3 = 6."),
    ],
    und=[
        ex("Escribe 11/4 como número mixto.", mix(11, 4), "11 ÷ 4 = 2 resto 3."),
        ex("Escribe 3 2/5 como fracción impropia.", imp(3, 2, 5), "3 × 5 + 2 = 17."),
        ex("Escribe 9/2 como número mixto.", mix(9, 2), "9 ÷ 2 = 4 resto 1."),
    ],
    app=[
        ex("Escribe 23/8 como número mixto y verifica con una multiplicación.", mix(23, 8) + " (8 × 2 + 7 = 23)", "23 ÷ 8 = 2 resto 7."),
        ex("Escribe 5 3/8 como fracción impropia.", imp(5, 3, 8), "5 × 8 + 3 = 43."),
        ex("Escribe 29/12 como número mixto.", mix(29, 12), "29 ÷ 12 = 2 resto 5."),
    ],
    rea=[
        ex("Pablo escribió 3 1/2 = 4/2. ¿Cuál es el error y cuál es la fracción correcta?", "Sumó 3 + 1; es 7/2", "Debe hacer 3 × 2 + 1 = 7."),
        ex("Sara dice que 13/5 = 2 3/5. ¿Está bien?", "Sí", "13 ÷ 5 = 2 resto 3."),
    ],
    cha=[
        ex("Un número mixto con denominador 6 es igual a 19/6. ¿Cuál es?", mix(19, 6), "19 ÷ 6 = 3 resto 1."),
        ex("Escribe 5 como fracción impropia con denominador 8.", "40/8", "5 × 8 = 40."),
    ],
    ctx=[ex("Tres jarros iguales de 1 litro están completos y un cuarto jarro tiene la mitad. Escribe el agua total como número mixto y como fracción impropia (en medios de litro).", "3 1/2 litros = 7/2 litros", "3 × 2 + 1 = 7 medios.")],
    sc=[
        ex("Escribe 7/3 como número mixto.", mix(7, 3), "7 ÷ 3 = 2 resto 1."),
        ex("Escribe 4 3/4 como fracción impropia.", imp(4, 3, 4), "4 × 4 + 3 = 19."),
        ex("¿Qué dos números se multiplican para pasar 2 1/3 a impropia?", "2 × 3", "Parte entera por denominador."),
    ],
    op=task(
        "Elige: 13/4, 22/5 o 31/6. Escríbela como número mixto, dibuja las figuras que muestran los enteros y las partes que sobran, y comprueba pasando el mixto de vuelta a fracción impropia.",
        "22/5: 22 ÷ 5 = 4 resto 2, entonces 4 2/5. Dibujo 4 figuras de 5 partes completas y una con 2 partes. Compruebo: 4 × 5 + 2 = 22.",
        ["divide correctamente", "escribe cociente y resto en su lugar", "comprueba de vuelta"],
        ["división", "número mixto", "comprobación"],
        ["cambiar el denominador", "sumar en vez de multiplicar"],
        "Pide que verifique con la operación contraria y que cuente las figuras de su dibujo.",
    ),
    reinforce="Convierte en tu cuaderno 5/2, 7/3 y 9/4 a número mixto. Dibuja una figura para cada una.",
    extend="Explica por qué el denominador no cambia al pasar de fracción impropia a número mixto.",
)

# ------------------------------------------------------------------ OA 08 clase 3
lesson(
    OA8, 3,
    use="Aprenderé a elegir la mejor estrategia para convertir entre fracciones impropias y números mixtos, según lo que me pidan. Sirve para resolver problemas con medidas.",
    prior=["Sé pasar de impropia a mixto y de mixto a impropia."],
    explain=[
        "Hay dos estrategias principales. La primera es dividir: sirve para saber cuántos enteros hay en una fracción impropia. En 25/6, 25 ÷ 6 = 4 resto 1, entonces 4 1/6. La segunda es multiplicar y sumar: sirve para pasar un número mixto a fracción. En 4 3/8, 4 × 8 + 3 = 35, entonces 35/8.",
        "Antes de elegir, lee qué pide el problema. Si dice «cuántos enteros completos», conviene el número mixto. Si dice «cuántas partes en total» o quieres sumar o comparar, conviene la fracción impropia. Cuando el numerador es múltiplo del denominador, la fracción es un número natural: 12/4 = 3.",
        "Comprueba siempre. Si pasas de impropia a mixto, haz la operación contraria: parte entera por denominador más numerador debe dar el numerador original. Si el resultado no tiene sentido en la situación, por ejemplo un número mixto con fracción mayor que 1, revisa el cálculo.",
    ],
    vocab=[("estrategia", "forma de resolver un problema"), ("múltiplo", "número que aparece en la tabla de otro"), ("comprobar", "revisar el resultado con la operación contraria"), ("equivalente", "que vale lo mismo"), ("natural", "número entero como 1, 2, 3")],
    worked=[
        W("Elegir dividir", "Una cinta mide 17/4 metros. ¿Cuántos metros enteros tiene y cuánto sobra?", ["Pregunta por enteros: divido 17 ÷ 4 = 4 resto 1.", "Tiene 4 metros y sobra 1/4 de metro."], "4 1/4 metros"),
        W("Elegir multiplicar y sumar", "Mateo bebe 2 3/4 litros en un día. Escribe la cantidad en cuartos de litro.", ["Piden cuartos en total: paso a impropia.", "2 × 4 + 3 = 11.", "11 cuartos."], "11/4 litros"),
    ],
    mistakes=[
        M("Para pasar 17/4 a mixto, multiplicar 17 por 4.", "Se eligió la estrategia contraria.", "Para obtener enteros hay que dividir: 17 ÷ 4 = 4 resto 1."),
        M("Escribir 12/4 como 3/4.", "No se vio que 12 es múltiplo de 4.", "12 ÷ 4 = 3 exacto: 12/4 = 3."),
    ],
    rec=[
        ex("Para pasar 17/5 a número mixto, ¿qué operación haces: dividir 17 entre 5 o multiplicar 17 por 5?", "Dividir 17 entre 5", "El cociente da los enteros."),
        ex("Para pasar 3 2/5 a fracción impropia, ¿qué haces primero: 3 × 5 o 3 + 5?", "3 × 5", "Se multiplica la parte entera por el denominador."),
        ex("¿Qué número natural es 12/4?", "3", "12 ÷ 4 = 3."),
    ],
    und=[
        ex("Escribe 23/6 como número mixto.", mix(23, 6), "23 ÷ 6 = 3 resto 5."),
        ex("Escribe 4 3/8 como fracción impropia.", imp(4, 3, 8), "4 × 8 + 3 = 35."),
        ex("¿Qué número natural es 20/5?", "4", "20 ÷ 5 = 4."),
    ],
    app=[
        ex("Una cinta mide 23/4 metros. Escribe su largo como número mixto.", mix(23, 4) + " metros", "23 ÷ 4 = 5 resto 3."),
        ex("Lía bebe 3 1/4 litros de agua. Escribe esa cantidad como fracción impropia.", imp(3, 1, 4) + " litros", "3 × 4 + 1 = 13."),
        ex("Una receta pide 5 1/2 tazas de harina. Escríbelo como fracción impropia.", imp(5, 1, 2) + " tazas", "5 × 2 + 1 = 11."),
    ],
    rea=[
        ex("Lola dice que 25/6 tiene 4 enteros y sobra 1/6. ¿Tiene razón?", "Sí", "6 × 4 + 1 = 25."),
        ex("Tomás dice que 4 1/3 = 5/3 porque suma 4 + 1 en el numerador. ¿Es correcto?", "No, es 13/3", "4 × 3 + 1 = 13."),
    ],
    cha=[
        ex("Una fracción impropia con denominador 7 es igual al número mixto 3 5/7. ¿Cuál es?", imp(3, 5, 7), "3 × 7 + 5 = 26."),
        ex("¿Cuántos números mixtos con denominador 3, parte entera 1 o 2 y fracción propia distinta de cero existen?", "4", "Son 1 1/3, 1 2/3, 2 1/3 y 2 2/3."),
    ],
    ctx=[ex("Una caja ficticia pesa 13/2 kilogramos. Escribe el peso como número mixto en kilogramos.", mix(13, 2) + " kilogramos", "13 ÷ 2 = 6 resto 1.")],
    sc=[
        ex("Escribe 14/5 como número mixto.", mix(14, 5), "14 ÷ 5 = 2 resto 4."),
        ex("Escribe 6 1/2 como fracción impropia.", imp(6, 1, 2), "6 × 2 + 1 = 13."),
        ex("Si piden «cuántos enteros completos» hay en 19/4, ¿cuál es la respuesta?", "4", "19 ÷ 4 = 4 resto 3."),
    ],
    op=task(
        "Elige una de estas medidas: una tabla de 19/4 metros, una jarra con 3 5/6 litros o un camino de 27/10 kilómetros. Escribe la medida en las dos formas (impropia y mixta), explica qué estrategia usaste en cada paso y en qué situación usarías cada forma.",
        "Tabla de 19/4 metros: 19 ÷ 4 = 4 resto 3, entonces 4 3/4 metros. Para saber cuántos metros enteros tiene uso el número mixto; para sumar con otra tabla en cuartos uso 19/4.",
        ["escribe las dos formas", "explica la estrategia", "dice cuándo usa cada forma"],
        ["cálculos", "explicación"],
        ["usar la estrategia contraria", "olvidar comprobar"],
        "Pide que compruebe con la operación contraria y que explique cuál forma ayuda a cada pregunta.",
    ),
    reinforce="Escribe tres medidas de tu casa que sean más de un entero (por ejemplo 1 1/2 litros) y pásalas a fracción impropia.",
    extend="Explica por qué 12/4 y 3 son lo mismo, usando un dibujo.",
)

# ------------------------------------------------------------------ OA 08 clase 4
lesson(
    OA8, 4,
    use="Aprenderé a ubicar fracciones impropias y números mixtos en la recta numérica. Sirve para ver dónde están y compararlos.",
    prior=["Sé pasar entre fracción impropia y número mixto.", "Sé usar una recta numérica con números naturales."],
    explain=[
        "La recta numérica es una línea con números ordenados. Para ubicar una fracción, primero mira entre qué dos enteros está. Luego divide cada espacio entre enteros en tantas partes iguales como dice el denominador. Por ejemplo, 7/4 está entre 1 y 2, porque 4/4 = 1 y 8/4 = 2.",
        "Para ubicar 7/4, divide cada espacio entre 0 y 1, entre 1 y 2, etc., en 4 partes iguales. Cuenta 7 marcas desde el 0. La séptima marca queda una antes del 2 y es la misma que el número mixto 1 3/4: se avanza 1 entero y luego 3 cuartos.",
        "Las fracciones impropias y los números mixtos equivalentes caen en el mismo punto. Así 5/3 y 1 2/3 están en la misma marca. Si la recta está dividida en medios, la marca 3/2 está justo entre el 1 y el 2. Siempre revisa que las partes entre marcas sean iguales.",
    ],
    vocab=[("recta numérica", "línea donde los números se ubican en orden"), ("marca", "señal que indica un número en la recta"), ("entre", "en el espacio que hay entre dos números"), ("partes iguales", "partes del mismo tamaño"), ("ubicar", "poner un número en el lugar que le corresponde")],
    worked=[
        W("Ubicar una fracción impropia", "Ubica 7/4 en una recta dividida en cuartos.", ["Cuento 7 marcas desde el 0, de cuarto en cuarto.", "4 marcas llegan al 1, y 3 más llegan a 1 3/4.", "Queda entre 1 y 2, una marca antes del 2."], "Entre 1 y 2, en 1 3/4"),
        W("Qué fracción marca un punto", "En una recta dividida en quintos, un punto está en la séptima marca desde el 0. ¿Qué fracción es?", ["Cada marca avanza 1/5.", "7 marcas son 7/5.", "7/5 = 1 2/5."], "7/5 = 1 2/5"),
    ],
    mistakes=[
        M("Ubicar 5/3 antes del 1 porque 5 y 3 son números pequeños.", "5/3 es mayor que 1 porque 5 > 3.", "5/3 = 1 2/3, está entre 1 y 2."),
        M("Contar las marcas de la recta desde el 1 en vez del 0.", "Se perdió una marca al empezar en el lugar equivocado.", "Se cuenta desde el 0: la primera marca es 1/4."),
    ],
    rec=[
        ex("¿Entre qué dos enteros está 7/4?", "Entre 1 y 2", "7/4 = 1 3/4."),
        ex("En una recta dividida en medios, ¿cuántas marcas hay desde el 0 hasta el 1, sin contar el 0?", "2", "Son 1/2 y 2/2."),
        ex("¿En qué entero cae 6/3?", "En el 2", "6 ÷ 3 = 2."),
    ],
    und=[
        ex("En una recta dividida en quintos, un punto está en la novena marca desde el 0. ¿Qué fracción es?", "9/5", "Cada marca avanza 1/5 y 9 marcas son 9/5."),
        ex("En una recta dividida en cuartos, ¿qué fracción está en la marca 11 desde el 0?", "11/4", "Cada marca avanza 1/4."),
        ex("¿Entre qué dos enteros está 2 3/4?", "Entre 2 y 3", "La parte entera es 2."),
    ],
    app=[
        ex("Ubica 3/2 en una recta dividida en medios. ¿Cuántas marcas desde el 0 la separan?", "3", "Cada marca avanza 1/2."),
        ex("En una recta dividida en octavos, ¿cuál es el número mixto de la marca 13 desde el 0?", mix(13, 8), "13 ÷ 8 = 1 resto 5."),
        ex("Una recta dividida en tercios llega hasta el 3. ¿Cuántas marcas hay desde el 0 hasta el 3 sin contar el 0?", "9", "3 × 3 = 9."),
    ],
    rea=[
        ex("Fer ubicó 5/3 antes del 1. ¿Está bien?", "No, está entre 1 y 2", "5/3 = 1 2/3."),
        ex("¿Caen 5/3 y 1 2/3 en la misma marca de la recta?", "Sí", "1 × 3 + 2 = 5 y 5/3 es lo mismo que 1 2/3."),
    ],
    cha=[
        ex("En una recta de medios de 0 a 3, ¿cuántas marcas hay contando el 0 y el 3?", "7", "Son 0, 1/2, 1, 3/2, 2, 5/2 y 3."),
        ex("¿Qué fracción impropia con denominador 4 está justo entre 5/4 y 7/4?", "6/4", "Es la que sigue a 5/4."),
    ],
    ctx=[ex("En un camino ficticio hay postes cada 1/4 de kilómetro, partiendo del kilómetro 0. ¿Cuántos postes hay que contar después del que está en el 0 para llegar al kilómetro 1 3/4?", "7", "1 3/4 = 7/4, es decir 7 cuartos.")],
    sc=[
        ex("¿Entre qué enteros está 9/4?", "Entre 2 y 3", "9 ÷ 4 = 2 resto 1."),
        ex("En una recta dividida en sextos, ¿qué fracción está en la marca 8?", "8/6", "Cada marca avanza 1/6."),
        ex("¿Cuál es mayor, 3/2 o 4/3?", "3/2", "3/2 = 1 1/2 y 4/3 = 1 1/3."),
    ],
    op=task(
        "Dibuja una recta de 0 a 3. Elige un denominador (2, 4 o 5), divide cada espacio entre enteros en partes iguales y ubica 4 fracciones impropias con ese denominador. Escribe debajo de cada una su número mixto.",
        "Denominador 4: ubico 5/4, 6/4, 9/4 y 11/4. Sus mixtos son 1 1/4, 1 2/4, 2 1/4 y 2 3/4.",
        ["divide en partes iguales", "ubica cada fracción en su marca", "escribe su número mixto"],
        ["recta dibujada", "mixtos escritos"],
        ["marcas desiguales", "contar desde 1 en vez de 0"],
        "Pide que cuente las marcas desde el 0 y que revise que las equivalentes caigan en el mismo lugar.",
    ),
    reinforce="Dibuja una recta de 0 a 2 dividida en cuartos y marca con color 3/4, 5/4 y 7/4.",
    extend="Explica por qué 8/4 y 2 caen en la misma marca de la recta.",
)

# ------------------------------------------------------------------ OA 08 clase 5
lesson(
    OA8, 5,
    use="Aprenderé a comparar y ordenar fracciones impropias y números mixtos, y a comunicar mis resultados. Sirve para decidir cuál medida es mayor.",
    prior=["Sé pasar entre fracción impropia y número mixto.", "Sé comparar fracciones propias."],
    explain=[
        "Para comparar un número mixto con otro, compara primero las partes enteras. El que tiene mayor parte entera es mayor. Si las partes enteras son iguales, compara las fracciones propias. Así 1 4/5 > 1 3/5 porque 4/5 > 3/5, y 3 1/2 > 2 7/8 porque 3 > 2.",
        "Si tienes una fracción impropia y un mixto, pasa uno a la forma del otro. Para 7/4 y 1 1/2, 7/4 = 1 3/4, y como 3/4 > 1/2, 7/4 > 1 1/2. También puedes pasar los dos a fracción impropia con el mismo denominador y comparar los numeradores.",
        "Para ordenar varias medidas, ubícalas en la recta numérica o pásalas todas a números mixtos. Comunica el resultado con una frase y con las unidades: «La tabla de 5/2 metros es más larga que la de 2 metros». Revisa si tu orden tiene sentido con un dibujo.",
    ],
    vocab=[("comparar", "decidir cuál es mayor, menor o igual"), ("ordenar", "poner en fila de menor a mayor o al revés"), ("parte entera", "cuántos enteros completos hay"), ("medida", "cantidad con unidad, como metros o litros"), ("comunicar", "explicar el resultado con claridad")],
    worked=[
        W("Comparar un impropio con un mixto", "Compara 7/4 y 1 1/2.", ["Paso 7/4 a mixto: 7 ÷ 4 = 1 resto 3, entonces 1 3/4.", "Las dos partes enteras son 1: comparo 3/4 y 1/2.", "Comparo 3/4 con 1/2 = 2/4; 3/4 > 2/4."], "7/4 > 1 1/2"),
        W("Ordenar varias medidas", "Ordena de menor a mayor 5/2, 2 y 7/4.", ["5/2 = 2 1/2 y 7/4 = 1 3/4.", "Orden: 1 3/4, 2, 2 1/2."], "7/4 < 2 < 5/2"),
    ],
    mistakes=[
        M("Decir que 2 7/8 > 3 1/2 porque 7/8 es mayor que 1/2.", "Se comparó solo la fracción sin ver la parte entera.", "Primero se comparan los enteros: 3 > 2, entonces 3 1/2 es mayor."),
        M("Decir que 9/5 y 1 3/5 son iguales porque ambos tienen un 5.", "Se miró el denominador y no el valor.", "9 ÷ 5 = 1 resto 4, entonces 9/5 = 1 4/5, que es mayor que 1 3/5."),
    ],
    rec=[
        ex("¿Es 3 igual a 6/2?", "Sí", "6 ÷ 2 = 3."),
        ex("¿Cuál es mayor, 5/4 o 3/4?", "5/4", "5 cuartos son más que 3 cuartos."),
        ex("¿Cuál es mayor, 1 3/4 o 2?", "2", "1 3/4 es menos que 2."),
    ],
    und=[
        ex("Compara 9/5 y 1 3/5 con < o >.", "9/5 > 1 3/5", "9/5 = 1 4/5 y 4/5 > 3/5."),
        ex("Ordena de menor a mayor 7/3, 2 y 9/4.", "2 < 9/4 < 7/3", "9/4 = 2 1/4 y 7/3 = 2 1/3; 1/4 < 1/3."),
        ex("¿Son iguales 11/4 y 2 3/4?", "Sí", "11 ÷ 4 = 2 resto 3."),
    ],
    app=[
        ex("Ana corrió 8/3 kilómetros y Bea corrió 2 1/2 kilómetros. ¿Quién corrió más?", "Ana", "8/3 = 2 2/3 y 2/3 > 1/2."),
        ex("Una tabla mide 11/4 metros y otra 2 3/4 metros. ¿Cuál es más larga?", "Miden lo mismo", "11/4 = 2 3/4."),
        ex("Tres jarras tienen 2 1/2, 9/4 y 3 litros. Ordénalas de menor a mayor.", "9/4 < 2 1/2 < 3", "9/4 = 2 1/4."),
    ],
    rea=[
        ex("Teo dice que 5/3 es menor que 1 1/2 porque 5 es menor que 11. ¿Tiene razón?", "No", "5/3 = 1 2/3 y 2/3 > 1/2."),
        ex("¿Cuál es mayor, 17/5 o 3 1/2?", "3 1/2", "17/5 = 3 2/5; 2/5 = 4/10 y 1/2 = 5/10."),
    ],
    cha=[
        ex("Ordena de menor a mayor 11/4, 2 3/4, 5/2 y 3.", "5/2 < 11/4 = 2 3/4 < 3", "5/2 = 2 2/4; 11/4 = 2 3/4."),
        ex("¿Cuántas fracciones con denominador 3 hay entre 1 y 3, sin contar los extremos?", "5", "Son 4/3, 5/3, 6/3, 7/3 y 8/3."),
    ],
    ctx=[ex("Dos recetas ficticias piden 9/4 y 2 1/3 tazas de harina. ¿Cuál pide más harina?", "La de 2 1/3", "9/4 = 2 1/4 y 1/4 es menos que 1/3.")],
    sc=[
        ex("¿Cuál es mayor, 2 1/2 o 5/3?", "2 1/2", "5/3 = 1 2/3, que es menos de 2."),
        ex("Ordena de menor a mayor 3/2, 1 y 7/4.", "1 < 3/2 < 7/4", "3/2 = 1 2/4 y 7/4 = 1 3/4."),
        ex("¿Son iguales 8/4 y 2?", "Sí", "8 ÷ 4 = 2."),
    ],
    op=task(
        "Usa estas medidas: 9/4 m, 2 1/3 m, 5/2 m y 2 m. Ordénalas de la más corta a la más larga, explica cómo las convertiste y escribe una frase que comunique cuál es la más larga.",
        "En números mixtos: 9/4 = 2 1/4, 2 1/3, 5/2 = 2 1/2 y 2. Orden: 2 m < 2 1/4 m < 2 1/3 m < 2 1/2 m. La más larga es la de 5/2 metros.",
        ["convierte para comparar", "ordena correctamente", "comunica con unidad"],
        ["conversiones", "orden", "frase"],
        ["comparar solo fracciones sin enteros", "olvidar la unidad"],
        "Pide que compare primero los enteros y después las fracciones propias, y que lea la frase en voz alta.",
    ),
    reinforce="Escribe 5/2, 2 y 7/4 en una recta de 0 a 3 y mira cuál está más a la derecha.",
    extend="Explica cuándo conviene comparar con números mixtos y cuándo con fracciones impropias.",
)

# ------------------------------------------------------------------ OA 09 clase 1
lesson(
    OA9, 1,
    use="Aprenderé a sumar y restar fracciones propias con el mismo denominador, con dibujos y con símbolos. Sirve para juntar o quitar partes iguales.",
    prior=["Sé representar fracciones propias.", "Sé simplificar fracciones."],
    explain=[
        "Cuando las fracciones tienen el mismo denominador, las partes son del mismo tamaño y solo se cuentan. Para sumar, se suman los numeradores y el denominador queda igual: 2/7 + 3/7 = 5/7. Para restar, se restan los numeradores: 6/8 − 1/8 = 5/8.",
        "Puedes verlo con barras. Una barra de 7 partes con 2 sombreadas más otra igual con 3 sombreadas dan 5 partes sombreadas de 7. El denominador no cambia, porque no cambia el tamaño de las partes. Si sumaras también los denominadores, el tamaño cambiaría y el resultado estaría mal.",
        "Después de calcular, mira si el resultado se puede simplificar: 4/9 + 2/9 = 6/9 = 2/3. Si el numerador llega a ser igual al denominador, el resultado es un entero: 4/5 + 1/5 = 5/5 = 1. Comprueba con un dibujo o con la operación contraria.",
    ],
    vocab=[("sumar fracciones", "juntar partes del mismo tamaño"), ("restar fracciones", "quitar partes del mismo tamaño"), ("mismo denominador", "partes iguales de igual tamaño"), ("simplificar", "dividir numerador y denominador por el mismo número"), ("resultado", "lo que sale de la operación")],
    worked=[
        W("Sumar con el mismo denominador", "Calcula 4/9 + 2/9 y simplifica.", ["Sumo los numeradores: 4 + 2 = 6.", "El denominador queda 9: 6/9.", "Simplifico por 3: 2/3."], "2/3"),
        W("Restar con el mismo denominador", "Calcula 7/10 − 3/10 y simplifica.", ["Resto los numeradores: 7 − 3 = 4.", "El denominador queda 10: 4/10.", "Simplifico por 2: 2/5."], "2/5"),
    ],
    mistakes=[
        M("Calcular 2/7 + 3/7 = 5/14.", "Se sumaron también los denominadores.", "El tamaño de las partes no cambia: 2/7 + 3/7 = 5/7."),
        M("Dejar 6/9 sin simplificar cuando se pide la forma más simple.", "Faltó un último paso.", "6/9 se divide por 3: 2/3."),
    ],
    rec=[
        ex("Completa: 2/7 + 3/7 = __/7.", "5", "2 + 3 = 5."),
        ex("Cuando sumas fracciones con el mismo denominador, ¿qué números se suman?", "Solo los numeradores", "El denominador indica el tamaño de las partes y no cambia."),
        ex("Calcula 6/8 − 1/8.", "5/8", "6 − 1 = 5."),
    ],
    und=[
        ex("Calcula 3/10 + 5/10 y simplifica el resultado.", "4/5", "8/10 se divide por 2."),
        ex("Calcula 11/12 − 5/12 y simplifica el resultado.", "1/2", "6/12 se divide por 6."),
        ex("Una barra de 6 partes tiene 3 sombreadas y otra barra igual tiene 2 sombreadas. ¿Cuánto hay sombreado en total, como fracción?", "5/6", "3/6 + 2/6 = 5/6."),
    ],
    app=[
        ex("Ema comió 3/8 de una pizza y Beto 2/8 de la misma pizza. ¿Qué fracción comieron entre los dos?", "5/8", "3/8 + 2/8."),
        ex("De una cinta de 9/12 de metro se cortan 4/12 de metro. ¿Cuánto queda?", "5/12", "9/12 − 4/12."),
        ex("Calcula 4/5 + 1/5.", "1", "5/5 es un entero."),
    ],
    rea=[
        ex("Marta calculó 2/7 + 3/7 = 5/14. ¿Cuál es el error y cuál es el resultado correcto?", "Sumó los denominadores; es 5/7", "El denominador no cambia."),
        ex("¿Cuánto falta a 5/8 para llegar a un entero?", "3/8", "8/8 − 5/8 = 3/8."),
    ],
    cha=[
        ex("Dos fracciones con denominador 12 tienen numeradores consecutivos y suman 11/12. ¿Cuáles son?", "5/12 y 6/12", "5 + 6 = 11."),
        ex("¿Qué fracción hay que sumar a 3/10 para llegar a un entero?", "7/10", "10/10 − 3/10."),
    ],
    ctx=[ex("Un jarrón ficticio tiene 5/12 de agua y se agregan 4/12 más. ¿Qué fracción del jarrón está llena ahora?", "9/12 = 3/4", "5/12 + 4/12 = 9/12 y se simplifica por 3.")],
    sc=[
        ex("Calcula 3/11 + 5/11.", "8/11", "3 + 5 = 8."),
        ex("Calcula 9/10 − 4/10.", "5/10 = 1/2", "9 − 4 = 5 y se simplifica por 5."),
        ex("¿Se pueden sumar también los denominadores al sumar fracciones con igual denominador?", "No", "El tamaño de las partes no cambia."),
    ],
    op=task(
        "Elige una de estas operaciones: 5/12 + 4/12, 7/9 − 4/9 o 3/10 + 6/10. Dibuja barras iguales para mostrarla, calcula con símbolos, simplifica si se puede y explica por qué el denominador no cambia.",
        "7/9 − 4/9: dibujo una barra de 9 partes con 7 sombreadas y tacho 4. Quedan 3/9 = 1/3. El denominador no cambia porque las partes son del mismo tamaño.",
        ["dibuja con partes iguales", "calcula correctamente", "explica el denominador"],
        ["dibujo", "cálculo", "frase"],
        ["sumar los denominadores", "no simplificar"],
        "Pide que cuente las partes sombreadas en el dibujo y las compare con el cálculo.",
    ),
    reinforce="Dibuja dos barras de 8 partes con 3 y 2 partes sombreadas. Escribe la suma 3/8 + 2/8.",
    extend="Explica con un dibujo por qué 1/4 + 1/4 no es 2/8.",
)

# ------------------------------------------------------------------ OA 09 clase 2
lesson(
    OA9, 2,
    use="Aprenderé a sumar y restar fracciones con distinto denominador cuando uno es múltiplo del otro, amplificando una de ellas. Sirve para juntar partes de tamaños distintos.",
    prior=["Sé sumar fracciones con igual denominador.", "Sé amplificar y simplificar."],
    explain=[
        "Si los denominadores son distintos, las partes tienen tamaños diferentes y no se pueden contar juntas. Primero hay que dejarlas con el mismo denominador. Cuando un denominador es múltiplo del otro, basta amplificar la fracción con el denominador menor.",
        "Por ejemplo, 1/2 + 1/4. Como 4 es múltiplo de 2, amplifico 1/2 por 2: 2/4. Ahora sumo 2/4 + 1/4 = 3/4. En 5/6 − 1/2, como 6 es múltiplo de 2, amplifico 1/2 por 3 y queda 3/6. Luego resto 5/6 − 3/6 = 2/6 = 1/3.",
        "Siempre se mantiene el mismo denominador en el resultado y se opera con los numeradores. Al final, simplifica si se puede. Si la fracción que amplificaste cambia el valor del denominador, revisa que hayas multiplicado arriba y abajo por el mismo número.",
    ],
    vocab=[("denominador común", "denominador igual para las dos fracciones"), ("múltiplo", "número que aparece en la tabla de otro"), ("amplificar", "multiplicar numerador y denominador por el mismo número"), ("equivalente", "que vale lo mismo"), ("simplificar", "dividir numerador y denominador por el mismo número")],
    worked=[
        W("Sumar con un denominador múltiplo del otro", "Calcula 1/2 + 1/4.", ["4 es múltiplo de 2: amplifico 1/2 por 2.", "1/2 = 2/4.", "2/4 + 1/4 = 3/4."], "3/4"),
        W("Restar con un denominador múltiplo del otro", "Calcula 5/6 − 1/2 y simplifica.", ["6 es múltiplo de 2: amplifico 1/2 por 3.", "1/2 = 3/6.", "5/6 − 3/6 = 2/6, que simplificado por 2 es 1/3."], "1/3"),
    ],
    mistakes=[
        M("Calcular 1/2 + 1/4 = 2/6.", "Se sumaron numeradores con numeradores y denominadores con denominadores.", "Primero se amplifica 1/2 a 2/4 y luego 2/4 + 1/4 = 3/4."),
        M("Amplificar 1/2 a 2/2 para sumar con 1/4.", "Solo se multiplicó el numerador.", "También se multiplica el denominador: 1/2 = 2/4."),
    ],
    rec=[
        ex("Escribe 1/2 con denominador 4.", "2/4", "Se amplifica por 2."),
        ex("Escribe 1/3 con denominador 6.", "2/6", "Se amplifica por 2."),
        ex("Calcula 1/2 + 1/4.", "3/4", "2/4 + 1/4."),
    ],
    und=[
        ex("Calcula 3/4 − 1/8.", "5/8", "3/4 = 6/8 y 6/8 − 1/8."),
        ex("Calcula 1/3 + 1/6 y simplifica.", "1/2", "1/3 = 2/6; 3/6 se divide por 3."),
        ex("Calcula 3/4 − 1/2.", "1/4", "1/2 = 2/4 y 3/4 − 2/4 = 1/4."),
    ],
    app=[
        ex("Calcula 2/5 + 3/10.", "7/10", "2/5 = 4/10 y 4/10 + 3/10."),
        ex("Calcula 7/12 − 1/4 y simplifica.", "1/3", "1/4 = 3/12 y 7/12 − 3/12 = 4/12."),
        ex("Un jarro tiene 2/3 de litro de jugo y se bebe 1/6 de litro. ¿Cuánto queda?", "1/2 de litro", "2/3 = 4/6; 4/6 − 1/6 = 3/6, que simplificado es 1/2."),
    ],
    rea=[
        ex("Lola calcula 1/2 + 1/4 = 2/6. ¿Cuál es el error y el resultado correcto?", "Sumó numeradores con numeradores y denominadores con denominadores; es 3/4", "Hay que igualar denominadores primero."),
        ex("Para sumar 5/6 y 1/3, ¿qué denominador común es más cómodo?", "6", "6 es múltiplo de 3."),
    ],
    cha=[
        ex("Calcula 1/2 + 1/4 + 1/8.", "7/8", "4/8 + 2/8 + 1/8."),
        ex("Encuentra la fracción que sumada con 1/6 da 1/2.", "1/3", "1/2 = 3/6 y 3/6 − 1/6 = 2/6 = 1/3."),
    ],
    ctx=[ex("Pedro pintó 1/2 de un muro un día y 1/8 el siguiente. ¿Qué fracción del muro pintó en total?", "5/8", "1/2 = 4/8 y 4/8 + 1/8.")],
    sc=[
        ex("Calcula 1/5 + 3/10.", "1/2", "1/5 = 2/10 y 5/10 se divide por 5."),
        ex("Calcula 7/8 − 1/4.", "5/8", "1/4 = 2/8."),
        ex("¿Qué se amplifica en 1/3 + 5/6: la fracción con denominador 3 o la de 6?", "La de denominador 3", "6 es múltiplo de 3."),
    ],
    op=task(
        "Elige: 1/2 + 3/8, 5/6 − 1/3 o 7/10 − 2/5. Amplifica la fracción que haga falta, calcula, simplifica si se puede y dibuja dos barras iguales para comprobar.",
        "5/6 − 1/3: 1/3 = 2/6 y 5/6 − 2/6 = 3/6 = 1/2. En el dibujo, la barra de sextos con 5 sombreadas y 2 quitadas deja 3 sombreadas, que es la mitad.",
        ["amplifica bien", "calcula con el mismo denominador", "simplifica y comprueba"],
        ["fracciones equivalentes", "cálculo", "dibujo"],
        ["sumar los denominadores", "amplificar solo el numerador"],
        "Pide que revise que los dos denominadores sean iguales antes de operar.",
    ),
    reinforce="Escribe 1/2 como cuartos, sextos y octavos. Luego suma 1/2 + 1/4 en cuartos.",
    extend="Explica por qué no se pueden sumar medios con cuartos sin cambiar uno de ellos.",
)

# ------------------------------------------------------------------ OA 09 clase 3
lesson(
    OA9, 3,
    use="Aprenderé a sumar y restar fracciones cuando ninguno de los denominadores es múltiplo del otro, buscando un denominador común. Sirve para operar con partes como tercios y cuartos.",
    prior=["Sé sumar y restar fracciones cuando un denominador es múltiplo del otro.", "Sé amplificar."],
    explain=[
        "Cuando ninguno de los denominadores es múltiplo del otro, hay que amplificar las dos fracciones para llegar a un denominador común. Una forma sencilla es multiplicar los dos denominadores. Para 1/3 y 1/4, 3 × 4 = 12. También sirve cualquier múltiplo común, como 12.",
        "Para 1/3 + 1/4: amplifico 1/3 por 4 y obtengo 4/12; amplifico 1/4 por 3 y obtengo 3/12. Ahora sumo: 4/12 + 3/12 = 7/12. Para 2/3 − 1/4: 8/12 − 3/12 = 5/12. Después simplifica si se puede.",
        "En todos los casos los pasos son los mismos: buscar un denominador común, amplificar las dos fracciones, operar con los numeradores y simplificar. Las fracciones del problema tienen denominadores de 12 o menos, pero el denominador común puede ser mayor, como 15 para 1/3 y 1/5. Si puedes, busca el múltiplo común más pequeño.",
    ],
    vocab=[("denominador común", "un múltiplo de los dos denominadores"), ("múltiplo común", "número que aparece en las tablas de los dos denominadores"), ("amplificar", "multiplicar numerador y denominador por el mismo número"), ("operar", "sumar o restar"), ("simplificar", "dividir numerador y denominador por el mismo número")],
    worked=[
        W("Sumar con denominadores sin relación", "Calcula 1/3 + 1/4.", ["Denominador común: 3 × 4 = 12.", "1/3 = 4/12 y 1/4 = 3/12.", "4/12 + 3/12 = 7/12."], "7/12"),
        W("Restar con denominadores sin relación", "Calcula 2/3 − 1/4.", ["Denominador común 12.", "2/3 = 8/12 y 1/4 = 3/12.", "8/12 − 3/12 = 5/12."], "5/12"),
    ],
    mistakes=[
        M("Calcular 1/3 + 1/4 = 2/7.", "Se sumaron numeradores y denominadores sin igualar partes.", "Se necesita un denominador común: 7/12."),
        M("Amplificar solo una de las dos fracciones a 12 y dejar la otra con su denominador.", "Las dos deben quedar con el mismo denominador.", "1/3 = 4/12 y 1/4 = 3/12."),
    ],
    rec=[
        ex("Escribe 1/3 con denominador 12.", "4/12", "Se amplifica por 4."),
        ex("Escribe 1/4 con denominador 12.", "3/12", "Se amplifica por 3."),
        ex("¿Cuál es un denominador común de 3 y 4?", "12", "3 × 4 = 12."),
    ],
    und=[
        ex("Calcula 1/2 + 1/3.", "5/6", "3/6 + 2/6."),
        ex("Calcula 3/4 − 2/3.", "1/12", "9/12 − 8/12."),
        ex("Calcula 2/5 + 1/2.", "9/10", "4/10 + 5/10."),
    ],
    app=[
        ex("Calcula 5/6 − 1/4.", "7/12", "10/12 − 3/12."),
        ex("Rita recorrió 1/3 de un camino en la mañana y 1/5 en la tarde. ¿Qué fracción recorrió en total?", "8/15", "5/15 + 3/15."),
        ex("Un tanque está lleno hasta 3/4 y se usa 1/3 de la capacidad total. ¿Qué fracción queda?", "5/12", "9/12 − 4/12."),
    ],
    rea=[
        ex("Pablo calculó 1/3 + 1/4 = 2/7. ¿Es posible, sabiendo que 1/3 + 1/4 es mayor que 1/2?", "No", "2/7 es menor que 1/2, y el resultado correcto es 7/12."),
        ex("Camila dice que 1/2 + 1/3 = 5/6 usando denominador 6. ¿Es correcto?", "Sí", "3/6 + 2/6 = 5/6."),
    ],
    cha=[
        ex("¿Qué fracción hay que sumar a 1/3 para obtener 7/12?", "1/4", "7/12 − 4/12 = 3/12."),
        ex("¿Cuánto falta a 2/3 + 1/4 para llegar a un entero?", "1/12", "8/12 + 3/12 = 11/12."),
    ],
    ctx=[ex("En un huerto ficticio se plantó 1/2 con lechugas y 1/3 con tomates. ¿Qué fracción del huerto se usó?", "5/6", "3/6 + 2/6.")],
    sc=[
        ex("Calcula 1/4 + 1/5.", "9/20", "5/20 + 4/20."),
        ex("Calcula 2/3 − 1/2.", "1/6", "4/6 − 3/6."),
        ex("Calcula 1/2 − 1/5.", "3/10", "5/10 − 2/10."),
    ],
    op=task(
        "Elige: 1/4 + 2/3, 5/6 − 1/4 o 3/5 − 1/2. Busca el denominador común, amplifica las dos fracciones, calcula y simplifica. Dibuja dos barras iguales divididas en el denominador común para comprobar.",
        "5/6 − 1/4: denominador 12. 10/12 − 3/12 = 7/12. En una barra de 12 partes sombreo 10 y quito 3: quedan 7.",
        ["encuentra denominador común", "amplifica las dos", "calcula y comprueba"],
        ["fracciones equivalentes", "cálculo", "dibujo"],
        ["amplificar solo una fracción", "sumar denominadores"],
        "Pide que verifique que ambas fracciones tienen el mismo denominador antes de operar.",
    ),
    reinforce="Escribe 1/3 y 1/4 como doceavos. Súmalas y resta la menor de la mayor.",
    extend="Explica por qué 6 también sirve como denominador común de 1/2 y 1/3.",
)

# ------------------------------------------------------------------ OA 09 clase 4
lesson(
    OA9, 4,
    use="Aprenderé a resolver problemas con suma y resta de fracciones propias, incluyendo completar un entero y juntar tres partes. Sirve para repartir y medir con partes.",
    prior=["Sé sumar y restar fracciones con distinto denominador.", "Sé simplificar."],
    explain=[
        "Un problema con fracciones se resuelve igual que uno con números: entiendes la situación, eliges la operación, calculas y compruebas. Si juntas partes, sumas. Si quitas una parte, restas. Si preguntas cuánto falta para completar un entero, restas la fracción de 1.",
        "Para «cuánto falta», escribe el entero como fracción con el mismo denominador. Por ejemplo, 1 − 3/8 = 8/8 − 3/8 = 5/8. Si hay tres fracciones, súmalas con un denominador común: 1/3 + 1/6 + 1/4 con denominador 12 es 4/12 + 2/12 + 3/12 = 9/12 = 3/4.",
        "Siempre comprueba si el resultado tiene sentido. Una suma de fracciones propias debe ser mayor que cada sumando. Una resta debe ser menor que la fracción de la que partes. Responde con una frase completa, la unidad y la fracción simplificada.",
    ],
    vocab=[("completar un entero", "encontrar lo que falta para llegar a 1"), ("sumando", "cada fracción que se suma"), ("situación", "historia del problema"), ("razonable", "que tiene sentido"), ("simplificada", "escrita con los números más pequeños posibles")],
    worked=[
        W("Cuánto falta para el entero", "Ema leyó 3/8 de un libro. ¿Qué fracción le falta por leer?", ["El libro entero es 8/8.", "8/8 − 3/8 = 5/8."], "5/8"),
        W("Juntar tres partes", "Tres amigos pintan un mural: Pía 1/3, Sofi 1/6 y Lía 1/4. ¿Qué fracción pintaron entre las tres?", ["Denominador común 12: 4/12, 2/12 y 3/12.", "4 + 2 + 3 = 9, entonces 9/12.", "Simplifico por 3: 3/4."], "3/4"),
    ],
    mistakes=[
        M("Responder 3/8 a «cuánto falta» cuando ya se leyó 3/8.", "Se repite lo que ya se leyó.", "Falta 1 − 3/8 = 5/8."),
        M("Sumar 1/3 + 1/6 + 1/4 como 3/13.", "Se sumaron numeradores con numeradores y denominadores con denominadores.", "Con denominador 12, el resultado es 9/12 = 3/4."),
    ],
    rec=[
        ex("Si comiste 3/8 de una torta, ¿qué fracción queda?", "5/8", "8/8 − 3/8."),
        ex("Calcula 1 − 2/5.", "3/5", "5/5 − 2/5."),
        ex("Si los denominadores son distintos, ¿qué debes hacer primero?", "Amplificar para igualarlos", "No se pueden operar partes de distinto tamaño."),
    ],
    und=[
        ex("Calcula 1/2 + 1/5.", "7/10", "5/10 + 2/10."),
        ex("Calcula 7/10 − 1/2 y simplifica.", "1/5", "7/10 − 5/10 = 2/10."),
        ex("Calcula 1/3 + 1/6 + 1/2.", "1", "2/6 + 1/6 + 3/6 = 6/6."),
    ],
    app=[
        ex("Un tanque tiene 3/4 de agua y se saca 1/6 de la capacidad. ¿Qué fracción queda?", "7/12", "9/12 − 2/12."),
        ex("Tres amigos limpian un jardín: Pía 1/2, Sofi 1/6 y Lía 1/12. ¿Qué fracción del jardín limpiaron entre las tres?", "3/4", "6/12 + 2/12 + 1/12 = 9/12."),
        ex("Una cinta de 1 metro se corta 1/4 y luego 1/5. ¿Qué fracción del metro queda?", "11/20", "20/20 − 5/20 − 4/20."),
    ],
    rea=[
        ex("Beto obtuvo 2/5 para 1/2 + 1/3. Sin calcular, ¿puede ser correcto si el resultado debe ser mayor que 1/2?", "No", "2/5 es menor que 1/2; el resultado correcto es 5/6."),
        ex("Un estudiante obtuvo 2/1 al calcular 3/4 − 1/3. ¿Es razonable?", "No", "Una resta da menos que 3/4; el resultado correcto es 5/12."),
    ],
    cha=[
        ex("Dos fracciones con denominador 12 suman 7/12 y su diferencia es 1/12. ¿Cuáles son?", "4/12 y 3/12", "4 + 3 = 7 y 4 − 3 = 1."),
        ex("Un jardín tiene 1/2 con flores, 1/3 con pasto y el resto con árboles. ¿Qué fracción tiene árboles?", "1/6", "1 − 1/2 − 1/3 = 6/6 − 3/6 − 2/6."),
    ],
    ctx=[ex("Una receta ficticia usa 1/2 taza de harina y 1/3 de taza de azúcar. ¿Cuánta harina y azúcar hay en total, como fracción de taza?", "5/6 de taza", "3/6 + 2/6.")],
    sc=[
        ex("Calcula 1 − 3/10.", "7/10", "10/10 − 3/10."),
        ex("Calcula 1/3 + 1/6.", "1/2", "2/6 + 1/6 = 3/6."),
        ex("Al sumar 1/2 + 1/4, ¿el resultado puede ser menor que 1/2?", "No", "Al sumar se obtiene más que cada sumando."),
    ],
    op=task(
        "Elige un problema: (a) una torta de la que se comió 1/4 el sábado y 1/3 el domingo; (b) una pista donde se corrió 3/4 y se caminó 1/6; (c) una jarra con 5/6 de jugo de la que se bebe 1/4. Escribe la operación, calcula con denominador común, simplifica y responde con una frase.",
        "(a) 1/4 + 1/3 = 3/12 + 4/12 = 7/12. Se comió 7/12 de la torta. Queda 5/12.",
        ["elige la operación", "calcula con denominador común", "responde con una frase"],
        ["operación y cálculo", "frase de respuesta"],
        ["restar cuando debía sumar", "no simplificar"],
        "Pide que compruebe con una resta o suma contraria y que explique si la respuesta es razonable.",
    ),
    reinforce="Dibuja una barra y pinta 1/2, 1/4 y 1/8 en ella. Escribe la suma y comprueba con el dibujo.",
    extend="Explica cómo saber, sin calcular, si 1/3 + 1/4 es mayor o menor que 1.",
)
