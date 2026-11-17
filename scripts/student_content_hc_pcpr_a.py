"""Pensamiento computacional y programación (electivo HC, 3.º y 4.º medio): OAC-01 (abstracción, datos, alternativas, generalización), clases 1 a 5, y OAC-02 (representación de datos), clases 1 a 4. Todo en papel: el código va en el enunciado y se sigue a mano."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel y calculadora simple opcional. No se necesita computador: el código está escrito en cada enunciado y se sigue a mano, "
             "anotando los valores de las variables. En los enunciados, «↵» marca el fin de una línea y «··» marca una línea dentro de un bloque (cada «··» es un nivel). "
             "Si luego pruebas un programa en un computador, hazlo con la supervisión de tu docente.")
build = make_build(MATERIALS)

O1 = "MA-PCPR-3y4-OAC-01"
O2 = "MA-PCPR-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (de ejemplo). Una tienda aplica este descuento: si la compra es de $20.000 o más, se descuenta el 10 %; si no, no hay descuento. "
     "Programa: def pagar(monto): ↵ ··if monto >= 20000: ↵ ····return monto - monto // 10 ↵ ··return monto. "
     "Entrada: monto, un número entero de pesos. Salida: lo que se paga. (// es la división entera y return termina la función entregando un valor.)")
build(
    O1, 1, F,
    use="Aprenderé a abstraer un problema: decidir qué datos son entrada y salida, qué condiciones importan y qué detalles se pueden ignorar, y a seguir un programa breve a mano.",
    prior=["Sé que un programa recibe datos, los procesa y entrega un resultado.", "Sé resolver porcentajes simples con números enteros.", "Sé leer una condición del tipo «si… entonces…»."],
    explain=[
        "Abstraer es quedarse con lo esencial de un problema y dejar fuera los detalles que no cambian el resultado. Para programar, primero se precisan las entradas (los datos que recibe), la salida (lo que entrega) y las condiciones (reglas del tipo «si el monto es 20.000 o más»). Cada dato tiene un tipo: entero, texto o booleano (verdadero o falso). Una comparación como monto >= 20000 produce un booleano.",
        "Una función es un bloque de código con nombre; sus parámetros son las entradas, como monto, y return entrega la salida. Una variable es un nombre que guarda un valor, y el signo = asigna: monto = 20000 no pregunta nada, solo guarda el valor. Para preguntar si dos valores son iguales se usa ==. El orden importa: cuando una línea return se ejecuta, la función termina y las líneas que siguen ya no se leen.",
        "Para comprobar una función se sigue a mano con un caso concreto y se anota qué vale cada variable. Una buena abstracción incluye todo lo necesario y nada más: si el programa pide un dato que no cambia el resultado, sobra; si le falta uno que sí lo cambia, el resultado será incorrecto. También se revisa qué pasa justo en el límite de una condición, por ejemplo con un monto de exactamente 20.000.",
    ],
    vocab=[("abstracción", "quedarse con lo esencial y dejar fuera los detalles"), ("entrada", "dato que recibe un programa"), ("salida", "resultado que entrega"), ("variable", "nombre que guarda un valor"), ("función", "bloque de código con nombre, parámetros y un valor de retorno"), ("booleano", "valor verdadero o falso"), ("condición", "pregunta que decide qué camino sigue el programa")],
    worked=[
        ("Elegir las entradas", "Un programa calcula el total de una compra de entradas al cine. Datos disponibles: cantidad de entradas, precio de cada una, color del cartel y nombre de la sala. ¿Cuáles son las entradas del programa?", ["Pregunta qué necesita el cálculo: el total sale de multiplicar cantidad por precio.", "El color del cartel y el nombre de la sala no cambian el total: se dejan fuera."], "Las entradas son la cantidad de entradas y el precio de cada una"),
        ("Seguir la función a mano", "Con la función pagar de la ficha, ¿qué devuelve pagar(25000)?", ["La condición 25000 >= 20000 es verdadera, así que entra al bloque.", "Calcula 25000 // 10 = 2500 y resta: 25000 − 2500 = 22500."], "Devuelve 22.500"),
    ],
    mistakes=[("Pedir como entrada un dato que no cambia el resultado, como el nombre de la tienda.", "Los detalles irrelevantes complican el programa sin aportar nada.", "Pregunta de cada dato: «¿cambia la salida si lo cambio?»."),
              ("Escribir monto = 20000 para preguntar si el monto vale 20000.", "En Python, = guarda un valor; para comparar se usa ==.", "Usa == para igualdad y >= o > para mayor o igual y mayor.")],
    T=[
        ('abc', '{F} ¿Qué devuelve pagar(30000)?', '27000', '30000', '3000', 'Como 30000 cumple la condición, se descuenta 30000 // 10 = 3000 y queda 27000.'),
        ('abc', 'En la función pagar de la ficha, ¿cuál es la entrada?', 'El monto de la compra', 'El valor que se devuelve al final', 'La tienda donde se compra', 'La entrada es el dato que llega a la función (monto); el valor devuelto es la salida.'),
        ('ab', 'Para calcular lo que se paga en la ficha, ¿qué detalle se puede ignorar al abstraer?', 'El color de la bolsa de la tienda', 'El monto de la compra', 'El color de la bolsa no cambia el cálculo; el monto sí cambia el resultado.'),
        ('{F} ¿Qué devuelve pagar(19990)? Escribe el valor.', '19.990', 'No cumple monto >= 20000, así que no entra al bloque y devuelve el monto sin descuento.'),
        ('abc', '{F} ¿Qué tipo de dato produce la expresión monto >= 20000?', 'Booleano (verdadero o falso)', 'Número entero', 'Texto', 'Una comparación responde si algo es verdadero o falso, no entrega un número ni un texto.'),
        ('abc', '{F} Una persona cambia la condición a monto > 20000. ¿Qué cambia?', 'Una compra de exactamente 20000 deja de recibir descuento', 'Nada, porque 20000 y 20001 pagan lo mismo', 'Todas las compras reciben descuento', 'Con > el valor 20000 ya no cumple la condición, por lo que paga el monto completo.'),
        ('=', '{F} ¿Cuánto devuelve pagar(40000), en pesos?', '40000-40000//10', 'Como 40000 >= 20000, se entra al bloque y se resta la décima parte del monto, 4000.'),
        ('abc', '{F} Se quiere devolver cuánto se descuenta, no cuánto se paga. ¿Qué expresión va en el return del bloque?', 'monto // 10', 'monto - 10', 'monto * 10', 'El descuento es la décima parte del monto, es decir, monto // 10.'),
        ('abc', 'Un programa debe calcular el total de una compra de cuadernos y de lápices con precios fijos. ¿Cuáles son sus entradas y su salida?', 'Entradas: las cantidades de cuadernos y de lápices; salida: el total a pagar', 'Entradas: el total a pagar; salida: las cantidades', 'Entradas: el nombre de la tienda; salida: el precio de cada útil', 'Los precios son datos fijos del programa; lo que cambia en cada compra son las cantidades, y el total es lo que se entrega.'),
        ('abc', '{F} Alguien prueba pagar(10) y obtiene 10; concluye que el programa no sirve para montos chicos. ¿Es válida su conclusión?', 'No: bajo 20000 no hay descuento, así que devolver el mismo monto es lo correcto', 'Sí: un programa debe cambiar siempre el valor', 'Sí: debería restar 10 pesos', 'La regla del problema dice que bajo 20000 no hay descuento, por eso el resultado coincide con lo esperado.'),
        ('abc', 'Dos estudiantes modelan un metro para encontrar la ruta más rápida. El primero guarda estaciones, conexiones y minutos entre estaciones; el segundo guarda además el color de las paredes. ¿Cuál abstracción es mejor?', 'La del primero: conserva lo necesario para la ruta y omite lo que no cambia el resultado', 'La del segundo: más datos siempre dan mejores resultados', 'La del segundo: el color de las paredes ayuda a calcular los tiempos', 'El color no influye en el tiempo de viaje, así que guardarlo solo agrega ruido al modelo.'),
        ('abc', '{F} Se agrega, después de la regla del 20000, otra: if monto >= 50000: ↵ ····return monto - monto // 5. ¿Qué devuelve ahora pagar(60000)?', '54000, porque la primera condición ya devuelve y la nueva regla nunca se alcanza', '48000, porque se aplica la regla más específica', '60000, porque los dos descuentos se anulan', 'La primera condición se cumple y return termina la función con 60000 − 6000 = 54000; el orden de las reglas importa.'),
        ('abc', 'Un colegio quiere un programa que diga si un estudiante aprueba: asistencia de 85 % o más y ninguna prueba pendiente. ¿Qué entradas y qué salida necesita?', 'Dos entradas enteras (asistencia y pruebas pendientes) y una salida verdadero o falso', 'Una entrada de texto y una salida numérica', 'Cuatro entradas de texto y ninguna salida', 'Hay dos datos que cambian por estudiante y la respuesta es sí o no, es decir, un booleano.'),
    ],
    ctx=('abc', 'Una biblioteca cobra $200 por día de atraso, pero si el atraso supera 7 días la multa es fija de $1.500. ¿Cuánto paga quien devuelve un libro con 9 días de atraso?', '$1.500', '$1.800', '$200', 'Como 9 supera 7 días, se aplica la multa fija de 1.500 y no el cobro por día (que daría 1.800).'),
    sc=[
        ("En Pensamiento computacional: ¿qué significa abstraer un problema?", "Quedarse con lo esencial y dejar fuera los detalles que no cambian el resultado", "Abstraer es simplificar sin perder lo necesario para resolver el problema."),
        ("En Pensamiento computacional: ¿qué tipo de dato produce una comparación como edad >= 18?", "Un booleano: verdadero o falso", "Toda comparación responde si algo se cumple o no se cumple."),
        ("En Python, ¿qué operador se usa para preguntar si dos valores son iguales?", "==", "El signo = solo asigna un valor a una variable; para comparar se usa ==."),
    ],
    op=("Elige uno. Caso 1: un estacionamiento cobra $600 por hora y, si la persona se queda 5 horas o más, cobra un máximo fijo de $2.500. Caso 2: un juego escolar deja entrar si la persona tiene 12 años o más, o si va con una persona adulta. "
        "Escribe las entradas, la salida y las condiciones, y luego una función breve (en Python o en pseudocódigo) de cinco líneas o menos. Pruébala a mano con dos casos, uno de ellos en el límite de una condición.",
        "Caso 1: entrada horas; salida el cobro. def cobro(horas): ↵ ··if horas >= 5: ↵ ····return 2500 ↵ ··return 600 * horas. Con 3 horas: 1800; con 5 horas, que es el límite: 2500.",
        ["identifica entradas, salida y condiciones", "escribe una función coherente con las condiciones", "prueba un caso en el límite y anota el resultado"],
        ["hoja con las entradas, la función y la tabla de dos pruebas"],
        ["incluir datos que no cambian el resultado", "confundir = con ==", "no probar el límite de la condición"],
        "Pregunta: «¿qué devuelve tu función justo en el valor límite?». Si no lo probó, pídele que lo siga a mano."),
    reinforce="Toma la función de la ficha y sigue a mano pagar(20000) y pagar(19999), anotando qué condición se cumple en cada caso.",
    extend="Escribe cómo cambiarías la función para que desde $50.000 el descuento sea 20 % y explica por qué el orden de las condiciones importa.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (de ejemplo). Notas de un curso pequeño, en escala de 10 a 70: notas = [45, 60, 38, 52]. Las posiciones (índices) parten en 0: notas[0] vale 45. "
     "Lo mismo como diccionario (cada clave se asocia a un valor): ficha = {\"Ana\": 45, \"Bruno\": 60, \"Cami\": 38, \"Dani\": 52}, y ficha[\"Bruno\"] vale 60. "
     "Programa: suma = 0 ↵ for n in notas: ↵ ··suma = suma + n ↵ promedio = suma // len(notas). (len entrega la cantidad de elementos de la lista.)")
build(
    O1, 2, F,
    use="Aprenderé a organizar datos en listas y diccionarios, a representar los mismos datos de dos maneras y a elegir la organización que conviene según la pregunta.",
    prior=["Sé qué es una variable y un bucle for.", "Sé calcular un promedio con la división entera.", "Sé leer una tabla de dos columnas."],
    explain=[
        "Organizar los datos de forma lógica significa elegir una estructura que permita responder la pregunta con pocos pasos. Una lista guarda valores en orden y cada uno tiene un índice que parte en 0: en una lista de 4 elementos los índices son 0, 1, 2 y 3. La función len entrega la cantidad de elementos, y el último índice vale len menos 1. Leer una posición que no existe produce un error.",
        "Un diccionario asocia una clave con un valor: la clave sirve para consultar sin recordar la posición. La lista conviene cuando importa el orden o se recorre todo; el diccionario conviene cuando se consulta por un nombre o un código. Los mismos datos se pueden representar de dos maneras, por ejemplo como lista de notas y como diccionario nombre-nota, y cada una responde mejor ciertas preguntas.",
        "Para recorrer una lista se usa for n in lista, que entrega cada elemento una vez. Con una variable acumuladora se calcula una suma, y dividiéndola por len se obtiene el promedio. Para estructuras más ricas se combinan: un diccionario por estudiante, con claves como «nombre» y «notas», donde notas es a su vez una lista. Siempre se comprueba con un caso pequeño que la organización permite leer el dato buscado.",
    ],
    vocab=[("lista", "colección ordenada de valores"), ("índice", "posición de un elemento, que parte en 0"), ("diccionario", "colección de pares clave-valor"), ("clave", "nombre con que se consulta un valor"), ("recorrer", "pasar por cada elemento de una lista"), ("acumulador", "variable que va sumando valores")],
    worked=[
        ("Leer posiciones", "Con notas = [45, 60, 38, 52], ¿qué es notas[2] y cuánto vale len(notas)?", ["Los índices parten en 0: notas[0] = 45, notas[1] = 60 y notas[2] = 38.", "Hay cuatro elementos, así que len(notas) = 4."], "notas[2] vale 38 y len(notas) vale 4"),
        ("Elegir la estructura", "Se quiere consultar la nota de «Cami» sin recordar en qué posición está. ¿Qué representación conviene?", ["La lista exige conocer la posición de Cami.", "El diccionario permite escribir ficha[\"Cami\"] con la clave."], "Conviene el diccionario, y ficha[\"Cami\"] vale 38"),
    ],
    mistakes=[("Contar las posiciones desde 1 y escribir notas[4] para el cuarto elemento.", "El primer índice es 0; el cuarto elemento es notas[3].", "Con n elementos, los índices van de 0 a n − 1."),
              ("Creer que el último índice es len(lista).", "len entrega la cantidad de elementos, que es una unidad mayor que el último índice.", "Usa lista[len(lista) - 1] para el último elemento.")],
    T=[
        ('abc', '{F} ¿Cuánto vale notas[3]?', '52', '38', '195', 'Los índices parten en 0, así que notas[3] es el cuarto elemento, 52; 38 resulta de contar una posición menos y 195 es la suma.'),
        ('abc', 'Se agrega la nota de Eli al final y la lista queda notas = [45, 60, 38, 52, 47]. ¿Cuánto vale len(notas)?', '5', '4', '47', 'La lista ahora tiene cinco elementos; 4 es el último índice y 47 es la nota agregada.'),
        ('ab', '{F} Para consultar de inmediato la nota de Dani por su nombre, ¿qué representación es más directa?', 'El diccionario, con ficha["Dani"]', 'La lista de notas, buscando por el nombre', 'La clave "Dani" lleva al valor 52 sin recordar posiciones; la lista no guarda nombres.'),
        ('=', '{F} ¿Cuánto vale suma al terminar el for?', '45+60+38+52', 'El acumulador va sumando cada nota de la lista una vez.'),
        ('=', '{F} ¿Cuánto vale promedio al final del programa?', '(45+60+38+52)//4', 'La suma se divide por len(notas), que es 4, con división entera.'),
        ('abc', '{F} ¿Qué entrega notas[len(notas) - 1]?', '52', 'Un error: la posición 4 no existe', '195', 'len(notas) − 1 es 3, el último índice, y notas[3] vale 52.'),
        ('En una lista temps = [12, 15, 11, 18, 14], ¿cuál es el índice del valor 11?', '2', 'El 12 está en el índice 0, el 15 en el 1 y el 11 en el 2.'),
        ('abc', 'Dos listas se leen en paralelo (misma posición, misma persona): nombres = ["Ana", "Bruno", "Cami"] y edades = [16, 17, 16]. ¿Qué edad tiene Bruno?', '17', '16', '1', 'Bruno está en el índice 1 y edades[1] vale 17; el valor 1 es el índice, no la edad.'),
        ('=', 'Un programa suma los valores de la lista [8, 5, 12, 7] con un for y divide la suma por len de la lista usando //. ¿Qué entrega?', '(8+5+12+7)//4', 'La suma es 32 y la lista tiene 4 elementos.'),
        ('abc', 'Se debe guardar el stock de 200 productos y consultarlo por su código de barras. ¿Qué estructura es más adecuada?', 'Un diccionario con el código como clave, porque se consulta directo por código', 'Una lista, porque los códigos largos sirven como posiciones', 'Una lista, porque no necesita claves y se escribe más corto', 'Un código largo no sirve como índice cómodo; la clave del diccionario permite consultar sin recorrer.'),
        ('abc', '{F} Un compañero escribe notas[4] para leer la nota de Dani. ¿Qué ocurre?', 'Falla: la última posición es la 3 y la 4 no existe', 'Devuelve 52', 'Devuelve 0', 'Con cuatro elementos los índices llegan hasta 3; pedir el 4 produce un error.'),
        ('{F} Se recorre la lista con: conteo = 0 ↵ for n in notas: ↵ ··if n > 50: ↵ ····conteo = conteo + 1. ¿Cuánto vale conteo al final?', '2', 'Solo 60 y 52 son mayores que 50; 45 y 38 no lo son.'),
        ('abc', 'Se quiere guardar, para cada estudiante, su nombre, su curso y todas sus notas. ¿Cuál organización es lógica y completa?', 'Un diccionario por estudiante con las claves "nombre", "curso" y "notas" (esta última, una lista)', 'Una sola lista con nombre, curso y notas mezclados sin orden fijo', 'Un solo número que resuma todo', 'Un diccionario por estudiante deja cada dato con su etiqueta y permite guardar una lista de notas dentro.'),
    ],
    ctx=('abc', 'Un club deportivo guarda las asistencias de la semana como asistencias = [1, 0, 1, 1, 0], donde 1 significa que asistió y el primer valor es el lunes. ¿Qué día es asistencias[3] y cuál es su valor?', 'Jueves, con valor 1 (asistió)', 'Miércoles, con valor 1', 'Jueves, con valor 0', 'Lunes es el índice 0, martes el 1, miércoles el 2 y jueves el 3, donde el valor es 1.'),
    sc=[
        ("En Pensamiento computacional: ¿con qué número parte el primer índice de una lista?", "Con el 0", "Las listas cuentan sus posiciones desde cero."),
        ("En Pensamiento computacional: ¿qué estructura asocia una clave con un valor?", "El diccionario", "Cada clave del diccionario permite consultar su valor directamente."),
        ("¿Qué entrega len(lista)?", "La cantidad de elementos de la lista", "len cuenta los elementos; no entrega el último índice."),
    ],
    op=("Elige uno. Caso 1: cinco productos de una tienda con sus precios: pan $1.200, leche $1.100, arroz $1.500, té $2.500 y azúcar $1.300. Caso 2: las temperaturas máximas de seis días: 18, 21, 19, 24, 22 y 20 grados. "
        "Representa los datos de dos maneras (una lista y un diccionario, o una lista y una tabla), escribe un for que calcule el total (Caso 1) o el promedio con // (Caso 2) y sígueselo a mano, anotando los valores del acumulador.",
        "Caso 1: lista precios = [1200, 1100, 1500, 2500, 1300]; diccionario con la clave «pan» y su valor 1200. El for acumula 1200, 2300, 3800, 6300 y 7600: el total es $7.600.",
        ["representa los mismos datos de dos maneras", "escribe un recorrido con acumulador", "anota los valores sucesivos del acumulador"],
        ["hoja con las dos representaciones, el for y la tabla de seguimiento"],
        ["empezar a contar desde el índice 1", "no iniciar el acumulador en 0", "dividir por un número distinto de len"],
        "Pregunta: «¿qué valor tiene el acumulador después de la segunda vuelta?». Si no coincide con su tabla, repasa el recorrido."),
    reinforce="Con la lista [45, 60, 38, 52], escribe los cuatro índices y el valor de cada uno; luego arma el diccionario con los nombres de la ficha.",
    extend="Explica cuándo conviene una lista de diccionarios (uno por estudiante) y cuándo un solo diccionario de listas.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (de ejemplo). Lista ordenada de menor a mayor: L = [3, 8, 12, 17, 21, 26, 30] (siete valores, posiciones 0 a 6). "
     "Solución A (secuencial): revisar de a un valor desde la posición 0 hasta encontrar el buscado, o hasta el final si no está. "
     "Solución B (binaria): con inicio = 0 y fin = 6, mirar la posición medio = (inicio + fin) // 2. Si ahí está el valor buscado, termina; si el buscado es menor, el tramo pasa a inicio..medio − 1; si es mayor, a medio + 1..fin. "
     "Si inicio supera a fin, el valor no está. Cada valor que se mira cuenta como una comparación.")
build(
    O1, 3, F,
    use="Aprenderé a analizar dos soluciones alternativas para el mismo problema, a contar sus comparaciones y a decidir cuál conviene según las condiciones.",
    prior=["Sé recorrer una lista con un índice.", "Sé usar la división entera y las condiciones.", "Sé que una lista puede estar ordenada."],
    explain=[
        "Un mismo problema puede tener varias soluciones correctas. Para elegir entre ellas se comparan criterios: cuántos pasos hacen, qué condiciones previas exigen y qué tan simples son. Buscar un valor en una lista se puede hacer de a un valor desde el inicio (solución A) o, si la lista está ordenada, mirando el valor del medio y descartando la mitad (solución B, llamada búsqueda binaria).",
        "La solución A funciona con cualquier lista, pero en el peor caso mira todos los valores. La solución B exige que la lista esté ordenada, y a cambio reduce el tramo a casi la mitad en cada comparación. Con 7 valores hace como máximo 3 comparaciones; con 1.000 valores, unas 10. Si la lista no está ordenada, B puede decir que un valor no está aunque sí esté.",
        "Analizar alternativas incluye considerar el costo previo de ordenar la lista: ordenar una lista también toma trabajo, y si la lista cambia a diario o se consulta pocas veces, puede no compensar. Ninguna solución es mejor en todos los casos: para el primer valor de la lista A gana, para el último B gana. Se decide con datos: contar pasos en casos típicos y extremos.",
    ],
    vocab=[("búsqueda secuencial", "revisar los valores de a uno en orden"), ("búsqueda binaria", "mirar el medio de una lista ordenada y descartar la mitad"), ("comparación", "una revisión de un valor de la lista"), ("peor caso", "la entrada que obliga a hacer más pasos"), ("precondición", "condición que debe cumplirse antes de usar el algoritmo")],
    worked=[
        ("Contar comparaciones", "En la lista de la ficha, ¿cuántas comparaciones hacen A y B para encontrar el 8?", ["A revisa 3 y 8: son 2 comparaciones.", "B mira medio = 3 (valor 17); como 8 < 17, el tramo es 0..2; medio = 1 (valor 8): 2 comparaciones."], "A y B hacen 2 comparaciones cada una"),
        ("Una precondición que falla", "La lista [17, 3, 30, 8] no está ordenada. ¿Qué concluye B al buscar el 8?", ["Con inicio = 0 y fin = 3, medio = 1 (valor 3); como 8 > 3, el tramo es 2..3.", "Entonces medio = 2 (valor 30); como 8 < 30, fin = 1 y el tramo queda vacío."], "B concluye que el 8 no está, aunque sí está en la posición 3"),
    ],
    mistakes=[("Afirmar que B es siempre más rápida que A.", "Para un valor cercano al inicio, A termina antes que B.", "Compara con casos concretos antes de decidir."),
              ("Usar B en una lista que no está ordenada.", "B descarta mitades suponiendo el orden; sin orden puede descartar donde está el valor.", "Revisa la precondición del algoritmo antes de aplicarlo.")],
    T=[
        ('abc', '{F} Con la solución A, ¿cuántos valores se miran para encontrar el 12?', '3', '2', '12', 'A revisa 3, 8 y 12 en ese orden; 2 es el índice del 12, no la cantidad de revisiones.'),
        ('abc', '{F} Con la solución B, ¿qué posición se mira primero?', '3', '0', '6', 'medio = (0 + 6) // 2 = 3; 0 y 6 son los extremos del tramo.'),
        ('ab', '¿Qué condición previa exige la solución B?', 'Que la lista esté ordenada', 'Que la lista tenga un número par de valores', 'B descarta mitades usando el orden; la cantidad de valores no influye en que funcione.'),
        ('abc', '{F} Con la solución B, ¿cuántas comparaciones se hacen para encontrar el 26?', '2', '6', '3', 'B mira el 17 y luego el 26; 6 sería lo que hace A.'),
        ('abc', '{F} Con la solución A, ¿cuántas comparaciones se hacen para encontrar el 30?', '7', '6', '3', 'El 30 es el último valor, así que A revisa los siete valores de la lista.'),
        ('abc', '{F} Se busca el 10, que no está en L. ¿Cuántas comparaciones hace B antes de concluir que no está?', '3', '7', '1', 'B mira el 17, luego el 8 y luego el 12, y el tramo queda vacío; 7 son las de A.'),
        ('{F} Se busca el 26. Tras comparar con el valor del medio, ¿qué tramo (inicio..fin) queda en B?', '4..6', 'El medio es la posición 3 (valor 17); como 26 > 17, inicio pasa a ser 3 + 1 = 4 y fin sigue en 6.'),
        ('Una lista ordenada tiene 15 valores y B reduce el tramo así en cada comparación: 15, 7, 3 y 1. ¿Cuántas comparaciones hace como máximo?', '4', 'Hay una comparación por cada tamaño de tramo de la serie: 15, 7, 3 y 1.'),
        ('abc', '{F} Una estudiante cuenta que para el 3 B hace 3 comparaciones y A hace 1; para el 30 B hace 3 y A hace 7. ¿Qué concluye correctamente?', 'Ninguna es mejor en todos los casos: para el 3 gana A y para el 30 gana B', 'B es siempre más rápida', 'A es siempre más rápida', 'Los conteos cambian según el valor buscado, así que la comparación depende del caso.'),
        ('abc', 'Una lista de 6 nombres sin ordenar cambia cada día. ¿Qué solución conviene?', 'La A: no exige orden y con pocos valores revisar todos cuesta poco', 'La B: siempre es más rápida', 'Ninguna: no se puede buscar en listas sin ordenar', 'A funciona con cualquier lista; ordenar a diario para una lista tan pequeña no compensa.'),
        ('abc', 'Dos equipos: el Equipo 1 ordena la lista y usa B; el Equipo 2 usa A sin ordenar. La lista se consulta solo 2 veces al día. ¿Qué criterio decide?', 'Con pocas consultas, ordenar puede no compensar: hay que comparar el trabajo total', 'Siempre gana el equipo que usa B', 'Gana el Equipo 2 porque A siempre es más rápida que B', 'La rapidez de B se paga con el costo de ordenar; con pocas consultas ese costo pesa.'),
        ('abc', '{F} Se agregan dos valores al final sin reordenar: L = [3, 8, 12, 17, 21, 26, 30, 5, 40]. B busca el 5. ¿Qué concluye?', 'Que no está, aunque sí está en la posición 7, porque la lista dejó de estar ordenada', 'Que está en la posición 7', 'Que está en la posición 1', 'B mira posiciones 4 (21), 1 (8) y 0 (3), descarta el tramo donde estaba el 5 y termina sin encontrarlo.'),
        ('Una lista ordenada tiene 63 valores. En B, después de cada comparación el tramo que queda tiene como máximo (n − 1) // 2 valores, donde n es el tamaño del tramo anterior. ¿Cuántas comparaciones hace B como máximo?', '6', 'Los tramos son 63, 31, 15, 7, 3 y 1, y se hace una comparación en cada uno: 6 comparaciones.'),
    ],
    ctx=('=', 'Un catálogo ordenado tiene 100 libros. Buscar un código con la solución A puede requerir hasta 100 comparaciones y con la solución B hasta 7. Para una sola búsqueda, ¿cuántas comparaciones de diferencia hay como máximo entre ambas?', '100-7', 'Se restan las comparaciones máximas de B a las de A.'),
    sc=[
        ("En Pensamiento computacional: ¿qué condición exige la búsqueda binaria?", "Que la lista esté ordenada", "Sin orden no se puede descartar la mitad del tramo con seguridad."),
        ("En Pensamiento computacional: ¿qué criterios se usan para elegir entre dos soluciones correctas?", "Los pasos que hacen, sus condiciones previas y su simplicidad", "Si las dos son correctas, se comparan su costo y sus requisitos."),
        ("¿Qué hace la búsqueda binaria con el tramo en cada comparación?", "Lo reduce a casi la mitad", "Descarta la mitad donde el valor buscado no puede estar."),
    ],
    op=("Se tiene la lista ordenada [4, 9, 15, 22, 27, 33, 41, 48, 56]. Busca el 27 y el 56 con la solución A y con la solución B (medio = (inicio + fin) // 2). "
        "Arma una tabla con las comparaciones de cada solución para cada valor y escribe una conclusión: ¿cuál conviene para cada valor y por qué?",
        "Para 27: A hace 5 comparaciones (4, 9, 15, 22, 27) y B hace 1 (medio = 4). Para 56: A hace 9 y B hace 4 (posiciones 4, 6, 7 y 8). Conviene B para valores lejanos del inicio, y A solo para el primer valor de la lista.",
        ["cuenta las comparaciones de las dos soluciones", "arma una tabla clara", "concluye comparando con los datos"],
        ["hoja con la tabla de comparaciones y una conclusión de dos o tres líneas"],
        ["contar mal las posiciones del medio", "afirmar que una solución es mejor sin datos", "olvidar que B necesita orden"],
        "Pregunta: «¿qué tramo quedó después de la primera comparación de B?». Si falla, repasa medio = (inicio + fin) // 2."),
    reinforce="Con L de la ficha, sigue a mano la búsqueda del 21 con A y con B y anota cuántas comparaciones hace cada una.",
    extend="Explica por qué B funciona con listas de cualquier tamaño y por qué con el doble de valores solo agrega una comparación más.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (de ejemplo). Caso particular: una tienda arma cajas de 6 galletas y quiere saber cuántas cajas completas salen de 50 galletas y cuántas sobran: cajas = 50 // 6 ↵ sobran = 50 % 6. "
     "Versión general: def empacar(total, por_caja): ↵ ··return total // por_caja, total % por_caja. "
     "(// entrega el cociente entero y % entrega el resto de la división; return puede entregar dos valores a la vez.)")
build(
    O1, 4, F,
    use="Aprenderé a generalizar: pasar de un caso particular a una función con parámetros, reconocer el patrón que se repite y justificar hasta dónde sirve la solución general.",
    prior=["Sé usar la división entera y el resto.", "Sé escribir una función con parámetros.", "Sé reconocer qué cambia y qué se repite en varios cálculos parecidos."],
    explain=[
        "Generalizar es reemplazar los valores fijos de un caso particular por parámetros, de modo que la misma solución sirva para muchos casos. Primero se comparan varios casos parecidos y se detecta qué cambia (los datos) y qué se repite (el patrón). Lo que cambia pasa a ser un parámetro; lo que se repite queda en el cuerpo de la función.",
        "Una función general se escribe una vez y se reutiliza: empacar(100, 8) y empacar(50, 6) usan el mismo código. Se justifica comprobándola con los casos particulares que le dieron origen y con otros nuevos. Un error frecuente es dejar un número fijo dentro de la función general, como escribir 6 en vez de por_caja, porque entonces solo sirve para ese caso.",
        "Toda generalización tiene límites que hay que prever. Si por_caja vale 0, la división falla; si total es menor que por_caja, el resultado es 0 cajas con todo sobrante, lo cual es correcto. Por eso se agregan condiciones o validaciones. También se generaliza un patrón de números: si las figuras tienen 4, 7, 10… palitos y cada una agrega 3, la regla general es 3·n + 1 para la figura n.",
    ],
    vocab=[("generalizar", "pasar de casos particulares a una solución válida para muchos"), ("parámetro", "dato que cambia y se pasa a la función"), ("patrón", "regularidad que se repite entre casos"), ("cociente", "resultado de una división entera"), ("resto", "lo que sobra en una división entera"), ("validación", "comprobación de que un dato es aceptable")],
    worked=[
        ("Detectar el patrón", "Tres líneas: a = 2 * 4, b = 5 * 4, c = 9 * 4. Escribe una función general.", ["Compara las líneas: el primer factor cambia (2, 5, 9) y el 4 se repite.", "Lo que cambia pasa a ser el parámetro x y lo que se repite queda en el cuerpo."], "def por4(x): return x * 4"),
        ("Usar la función general", "¿Qué devuelve empacar(100, 8)?", ["100 // 8 = 12, porque 12 · 8 = 96.", "100 % 8 = 4, porque 100 − 96 = 4."], "Devuelve (12, 4): 12 cajas completas y 4 sobrantes"),
    ],
    mistakes=[("Dejar el número 6 escrito dentro de la función general.", "Entonces la función solo sirve para cajas de 6 y no es general.", "Reemplaza cada valor que cambia por un parámetro."),
              ("No prever por_caja = 0.", "Dividir por 0 produce un error y el programa se detiene.", "Valida que por_caja sea mayor que 0 antes de dividir.")],
    T=[
        ('abc', '{F} En el caso particular de 50 galletas, ¿cuántas cajas completas salen?', '8', '9', '2', '50 // 6 = 8 porque 8 · 6 = 48; 9 sería redondear hacia arriba y 2 es lo que sobra.'),
        ('abc', '{F} En el caso particular de 50 galletas, ¿cuántas sobran?', '2', '8', '6', '50 % 6 = 2 porque 50 − 48 = 2; 8 es el número de cajas.'),
        ('ab', 'En la función empacar de la ficha, ¿qué valores pasaron a ser parámetros?', 'total y por_caja, los datos que cambian de un caso a otro', 'Solo la palabra return', 'Los datos que cambian entre casos se convierten en parámetros; return es parte fija del código.'),
        ('abc', '{F} ¿Qué devuelve empacar(70, 8)?', '(8, 6)', '(9, 2)', '(6, 8)', 'El cociente 8 va primero y el resto 6 va segundo, porque 8 · 8 = 64; (6, 8) los invierte y (9, 2) redondea hacia arriba.'),
        ('=', '{F} ¿Cuántas cajas completas devuelve empacar(95, 9)?', '95//9', 'La división entera de 95 por 9 da 10 porque 10 · 9 = 90.'),
        ('abc', '{F} ¿Qué devuelve empacar(5, 6)?', '(0, 5)', '(1, 0)', '(0, 6)', 'No alcanza para una caja completa: 0 cajas y los 5 sobran.'),
        ('abc', 'Tres líneas: a = 2 * 7 + 1, b = 5 * 7 + 1, c = 9 * 7 + 1. ¿Qué función general las reemplaza?', 'def f(n): return n * 7 + 1', 'def f(n): return 7 * 1 + n', 'def f(n): return n + 7 + 1', 'El factor que cambia es el primero, y el patrón es multiplicarlo por 7 y sumar 1.'),
        ('=', 'Una función general es def costo(horas): return 1500 + 600 * horas. ¿Cuánto cuesta (en pesos) un arriendo de 4 horas?', '1500+600*4', 'Se multiplica el costo por hora por 4 y se suma el cargo fijo.'),
        ('abc', 'Una persona llama empacar(6, 40) pensando en repartir 40 objetos en grupos de 6. ¿Qué devuelve esa llamada?', '(0, 6)', '(6, 4)', '(40, 6)', 'El primer parámetro es el total y el segundo el tamaño del grupo; con los valores invertidos, 6 // 40 = 0 y sobran los 6. Lo que buscaba daría (6, 4).'),
        ('abc', '{F} Alguien llama empacar(10, 0). ¿Qué ocurre y qué debe prever la generalización?', 'Falla por dividir por cero; la función debe validar que por_caja sea mayor que 0', 'Devuelve (0, 0)', 'Devuelve (10, 0)', 'La división por cero no está definida y detiene el programa; una función general valida sus entradas.'),
        ('abc', 'Un programa calcula un área como 5 * 3 y otro como 8 * 2. Una persona propone def area(base, altura) y otra def area(): return 5 * 3. ¿Cuál es general?', 'La primera, porque los valores que cambian son parámetros', 'La segunda, porque tiene menos letras', 'Ambas, mientras sea correcta para un caso', 'Una función sin parámetros solo resuelve un caso; los datos que varían deben entrar como parámetros.'),
        ('abc', 'def promedio3(a, b, c): return (a + b + c) // 3. ¿Qué limitación tiene frente a una función que reciba una lista de notas?', 'Solo sirve para exactamente tres notas; con una lista serviría para cualquier cantidad', 'No sirve porque la división entera no existe', 'Da error porque // solo se puede usar con listas', 'La cantidad de notas está fija en el código; recibir una lista generaliza también ese dato.'),
        ('=', 'Las figuras tienen 4, 7, 10… palitos (cada una agrega 3), y la regla general es palitos(n) = 3 * n + 1. ¿Cuántos palitos tiene la figura 20?', '3*20+1', 'Se reemplaza n por 20 en la regla general.'),
    ],
    ctx=('abc', 'Un taller imprime afiches en paquetes de 12 y tiene 100 afiches. Con una función como empacar(100, 12), ¿cuántos afiches sobran?', '4', '8', '9', '100 // 12 = 8 paquetes usan 96 afiches, y quedan 100 − 96 = 4; 8 es el número de paquetes.'),
    sc=[
        ("En Pensamiento computacional: ¿qué significa generalizar una solución?", "Cambiar los valores fijos por parámetros para que sirva en muchos casos", "Una solución general reemplaza lo que cambia por parámetros."),
        ("¿Qué operador de Python entrega el resto de una división entera?", "%", "El operador % entrega lo que sobra al dividir, por ejemplo 50 % 6 = 2."),
        ("En Pensamiento computacional: ¿qué caso hay que prever en una función que divide?", "Que el divisor sea 0", "Dividir por cero produce un error y detiene el programa."),
    ],
    op=("Elige uno. Caso 1: tres cálculos de una tienda: total1 = 3 * 1200, total2 = 5 * 1200 y total3 = 8 * 1200. Caso 2: convertir minutos en horas y minutos para 130, 45 y 200 minutos. "
        "Escribe una función general, pruébala con los tres casos y con un caso extremo (por ejemplo 0), y anota una validación o limitación de tu función.",
        "Caso 2: def a_horas(minutos): return minutos // 60, minutos % 60. a_horas(130) devuelve (2, 10), a_horas(45) devuelve (0, 45) y a_horas(200) devuelve (3, 20). Limitación: no admite minutos negativos.",
        ["identifica qué cambia y qué se repite", "escribe una función con parámetros", "la prueba con tres casos y uno extremo"],
        ["hoja con la función y la tabla de pruebas"],
        ["dejar un número fijo dentro de la función", "invertir el orden del cociente y el resto", "no probar el valor 0"],
        "Pregunta: «¿qué valor de la función es el parámetro?». Si hay números fijos, pídele que los reemplace."),
    reinforce="Escribe tres cálculos parecidos propios (con una multiplicación y una suma) y conviértelos en una función de un parámetro.",
    extend="Explica por qué una función general que valida sus datos es más confiable que una que solo funciona con datos ideales.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (de ejemplo). Se quiere una función que devuelva el mayor de tres enteros. "
     "Solución 1: def mayor1(a, b, c): ↵ ··if a >= b and a >= c: ↵ ····return a ↵ ··if b >= c: ↵ ····return b ↵ ··return c. "
     "Solución 2: def mayor2(a, b, c): ↵ ··if a > b: ↵ ····return a ↵ ··if b > c: ↵ ····return b ↵ ··return c.")
build(
    O1, 5, F,
    use="Aprenderé a comprobar una solución con casos de prueba (típicos y límite), a encontrar un contraejemplo y a comparar dos soluciones solo después de comprobar que son correctas.",
    prior=["Sé seguir una función a mano.", "Sé usar condiciones con and.", "Sé que una solución puede tener errores aunque pase algunas pruebas."],
    explain=[
        "Comprobar una solución es probarla con casos cuyo resultado correcto ya se conoce. Un buen juego de pruebas incluye casos típicos (que ejercitan cada rama, es decir, cada camino posible del programa), casos límite (empates, ceros, valores negativos, extremos) y casos donde la respuesta esté en cada posición posible. Si una prueba da un resultado distinto del esperado, se encontró un contraejemplo: eso demuestra que hay un error.",
        "Pasar varias pruebas no demuestra que un programa sea correcto; solo aumenta la confianza. Un único contraejemplo, en cambio, basta para refutarlo. Por eso se buscan activamente los casos que podrían fallar. En mayor2, por ejemplo, cuando a > b devuelve a sin comparar con c, y eso falla si c es el mayor.",
        "Solo se comparan soluciones que han pasado la comprobación. Una solución más corta o con menos comparaciones no es mejor si da resultados incorrectos. Entre soluciones correctas se comparan la cantidad de pasos, la claridad y qué tan fácil es de modificar. La conclusión siempre debe apoyarse en los casos probados, no en la impresión.",
    ],
    vocab=[("rama", "cada camino posible dentro de un programa, por ejemplo cada return"), ("caso de prueba", "entrada con el resultado esperado conocido"), ("caso límite", "entrada extrema o especial, como un empate o un cero"), ("contraejemplo", "caso que muestra que una solución falla"), ("correcta", "que da el resultado esperado en todos los casos"), ("comparar", "contrastar soluciones por pasos, claridad y facilidad de cambio")],
    worked=[
        ("Buscar un contraejemplo", "Prueba mayor2(5, 3, 9). ¿Qué devuelve y qué muestra?", ["a > b es 5 > 3, verdadero, así que devuelve a = 5.", "El mayor real es 9, de modo que el resultado es incorrecto."], "Devuelve 5 en vez de 9: es un contraejemplo que refuta mayor2"),
        ("Probar un caso con negativos", "¿Qué devuelve mayor1(−2, −8, −5)?", ["a >= b: −2 >= −8 es verdadero; a >= c: −2 >= −5 es verdadero.", "Entonces devuelve a = −2."], "Devuelve −2, que es el mayor"),
    ],
    mistakes=[("Probar con un solo caso y declarar que el programa es correcto.", "Un caso que pasa no demuestra nada sobre los demás.", "Prueba también casos límite y con el mayor en cada posición."),
              ("Elegir todos los casos con el mayor en la primera posición.", "No se ejercitan las otras ramas del programa.", "Cambia la posición del mayor y agrega un empate.")],
    T=[
        ('abc', '{F} ¿Qué devuelve mayor1(4, 9, 6)?', '9', '4', '6', 'La primera condición falla porque 4 no es mayor o igual que 9; luego b >= c es 9 >= 6, verdadero, y devuelve b.'),
        ('abc', '{F} ¿Qué devuelve mayor2(2, 8, 5)?', '8', '2', '5', 'a > b es falso; b > c es verdadero (8 > 5) y devuelve b.'),
        ('ab', '¿Qué demuestra una prueba cuyo resultado difiere del esperado?', 'Que hay un error en el programa (o en lo que se esperaba)', 'Que el programa es correcto para los demás casos', 'Un resultado distinto del esperado es un contraejemplo y obliga a revisar el programa.'),
        ('abc', '{F} ¿Con cuál entrada devuelve un resultado incorrecto la solución 2?', '(6, 2, 8)', '(9, 3, 5)', '(1, 2, 3)', 'Con (6, 2, 8) devuelve 6 porque 6 > 2, pero el mayor es 8; las otras dos entradas dan el resultado correcto.'),
        ('{F} ¿Qué devuelve mayor2(9, 4, 12) y cuál es el valor correcto?', 'Devuelve 9; lo correcto es 12', 'Como 9 > 4 devuelve a sin mirar c, que es mayor.'),
        ('abc', '{F} mayor2(4, 4, 9) devuelve 9, que es correcto. ¿Por qué, si a no es mayor que b?', 'Porque ninguna de las dos condiciones se cumple y llega a return c, que vale 9', 'Porque en un empate la función devuelve b', 'Porque a > b es verdadero', 'a > b y b > c son falsas, así que se ejecuta el return final, que entrega c.'),
        ('{F} ¿Qué devuelve mayor1(7, 7, 1)? Escribe el valor.', '7', 'a >= b y a >= c son verdaderas (7 >= 7 y 7 >= 1), así que devuelve a.'),
        ('abc', '{F} ¿Qué devuelve mayor1(−6, −3, −9)?', '−3', '−6', '−9', 'Entre los negativos el mayor es el más cercano a cero; la primera condición falla (−6 < −3) y b >= c (−3 >= −9) devuelve −3.'),
        ('abc', 'Para probar una función que devuelve el mayor de tres números, ¿qué juego de pruebas es más completo?', 'Un caso con el mayor en cada posición, un empate y uno con negativos', 'Tres casos con el mayor siempre en la primera posición', 'Un único caso con números grandes', 'Un buen juego de pruebas ejercita todas las ramas y los casos límite, no solo una.'),
        ('abc', '{F} Una persona prueba mayor2 con (9, 3, 5), (1, 2, 3) y (2, 8, 5), todas bien, y declara que es correcta. ¿Qué falla en su razonamiento?', 'Que pasar pruebas no demuestra corrección: la entrada (6, 2, 8) la refuta', 'Nada: tres pruebas bastan siempre', 'Que con cuatro pruebas sí bastaría', 'Ninguna cantidad de pruebas que pasan demuestra corrección, pero un solo contraejemplo la refuta.'),
        ('abc', '{F} ¿Cuál es el error lógico de mayor2?', 'Cuando a > b devuelve a sin compararlo con c', 'Usa > en vez de >= y por eso falla en los empates', 'Nunca devuelve c', 'Con a > b verdadero ya no revisa c; los empates los resuelve bien, como en (7, 7, 1).'),
        ('abc', '{F} Una persona prefiere mayor2 «porque hace menos comparaciones». ¿Qué respuesta es correcta?', 'No es buena razón: mayor2 es incorrecta, y una solución incorrecta no se compara por velocidad', 'Sí: menos comparaciones siempre es mejor', 'No: mayor1 hace menos comparaciones', 'Primero se comprueba que sea correcta; solo entre soluciones correctas se compara la eficiencia.'),
        ('abc', '{F} De las seis ordenaciones de los números 1, 2 y 3, ¿con cuál falla mayor2?', '(2, 1, 3)', '(1, 3, 2)', '(3, 2, 1)', 'Con (2, 1, 3) se cumple a > b, devuelve 2 y el mayor es 3; las otras cinco ordenaciones dan el resultado correcto.'),
    ],
    ctx=('abc', 'Una app de puntajes usa mayor1 para destacar el puntaje más alto de tres jueces, que dieron 55, 55 y 40. ¿Qué puntaje destaca?', '55', '40', '110', 'a >= b y a >= c se cumplen (55 >= 55 y 55 >= 40), y el empate se resuelve bien devolviendo 55.'),
    sc=[
        ("En Pensamiento computacional: ¿qué es un caso límite?", "Una entrada extrema o especial, como un empate o un cero, donde suelen aparecer errores", "Ahí se prueban los bordes de las condiciones, donde fallan más los programas."),
        ("En Pensamiento computacional: ¿qué muestra un contraejemplo?", "Que la solución tiene un error", "Un solo caso que falla basta para refutar una solución."),
        ("¿Basta con que pasen tres pruebas para asegurar que un programa es correcto?", "No", "Pasar pruebas aumenta la confianza, pero no demuestra corrección general."),
    ],
    op=("Esta función debería devolver el menor de tres enteros: def menor(a, b, c): ↵ ··if a < b: ↵ ····return a ↵ ··if b < c: ↵ ····return b ↵ ··return c. "
        "Arma una tabla de seis pruebas con el resultado esperado y el que entrega la función (con el menor en cada posición, un empate y un caso con negativos), encuentra un contraejemplo, corrígela y escribe una conclusión.",
        "Con (5, 9, 2) la función devuelve 5 porque 5 < 9, pero el menor es 2: es un contraejemplo. Una corrección es if a <= b and a <= c: return a, luego if b <= c: return b, y por último return c.",
        ["arma seis pruebas variadas", "identifica un contraejemplo concreto", "propone y prueba una corrección"],
        ["tabla de pruebas, el contraejemplo y la versión corregida"],
        ["probar solo casos con el menor al inicio", "no anotar el resultado esperado antes de seguir el código", "corregir sin volver a probar"],
        "Pregunta: «¿qué resultado esperabas antes de seguir el código?». Si no lo tenía, pídele que lo calcule primero."),
    reinforce="Sigue a mano mayor1 y mayor2 con (3, 5, 5) y (8, 8, 8) y anota si los resultados coinciden.",
    extend="Explica por qué en una comparación entre soluciones se verifica primero la corrección y solo después la eficiencia.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (de ejemplo). Un bit es un dígito que vale 0 o 1. Un byte son 8 bits. En un byte, el valor de cada posición, de izquierda a derecha, es 128, 64, 32, 16, 8, 4, 2 y 1. "
     "Ejemplo: 00001101 vale 8 + 4 + 1 = 13. Con 2 bits se pueden formar 4 combinaciones distintas: 00, 01, 10 y 11.")
build(
    O2, 1, F,
    use="Aprenderé cómo se representan los números en el sistema binario, a convertir entre binario y decimal y a calcular cuántos valores permite un número de bits.",
    prior=["Sé que el sistema decimal usa diez dígitos y valores por posición.", "Sé las potencias de 2 hasta 128.", "Sé sumar números enteros."],
    explain=[
        "Los computadores guardan toda la información con bits, cada uno con solo dos valores: 0 o 1. Los números se escriben en el sistema binario, donde cada posición vale el doble de la que está a su derecha: 1, 2, 4, 8, 16, 32, 64, 128. Para pasar de binario a decimal se suman los valores de las posiciones donde hay un 1. Para pasar de decimal a binario se descompone el número en esos valores.",
        "Con n bits se forman 2 · 2 · … · 2 (n veces) combinaciones distintas. Con 3 bits hay 8 y con 8 bits hay 256. Como se parte en 0, el mayor número que se escribe con 8 bits es 255 (11111111). Ese límite es un límite real: si una cuenta supera lo que cabe, ocurre un desborde, y el número «da la vuelta»: en 8 bits, 255 más 1 se guarda como 00000000, porque no hay un noveno bit.",
        "La cantidad de bits que se necesita depende de cuántos valores distintos hay que representar. Para numerar 20 estudiantes distintos hacen falta 5 bits, porque 4 bits dan solo 16 combinaciones y 5 bits dan 32. Siempre se comprueba la conversión al revés: se pasa el resultado otra vez al sistema original y se verifica que coincida.",
    ],
    vocab=[("bit", "dígito binario: 0 o 1"), ("byte", "grupo de 8 bits"), ("sistema binario", "forma de escribir números con solo 0 y 1"), ("combinación", "una disposición posible de bits"), ("desborde", "resultado que no cabe en los bits disponibles")],
    worked=[
        ("De binario a decimal", "Convierte 00101010 a decimal.", ["Los 1 están en las posiciones de valor 32, 8 y 2.", "Se suma 32 + 8 + 2 = 42."], "00101010 vale 42"),
        ("De decimal a binario", "Escribe 37 en 8 bits.", ["Descompón: 37 = 32 + 4 + 1.", "Pon 1 en las posiciones 32, 4 y 1, y 0 en las demás: 00100101."], "37 se escribe 00100101"),
    ],
    mistakes=[("Leer el número binario de derecha a izquierda.", "El valor mayor (128) está a la izquierda y el menor (1) a la derecha.", "Escribe sobre cada bit su valor de posición antes de sumar."),
              ("Decir que el mayor número en 8 bits es 256.", "256 es la cantidad de combinaciones; como se parte en 0, el mayor es 255.", "El mayor valor con n bits es el número de combinaciones menos 1.")],
    T=[
        ('=', '{F} ¿Cuántas combinaciones distintas se forman con 6 bits?', '2*2*2*2*2*2', 'Cada bit agrega un factor 2: se duplica el número de combinaciones.'),
        ('abc', '{F} ¿Cuánto vale 00000110 en decimal?', '6', '96', '2', 'Los 1 están en las posiciones 4 y 2, y 4 + 2 = 6; 96 sale de leer al revés y 2 solo cuenta los unos.'),
        ('ab', '¿Qué valores puede tomar un bit?', '0 o 1', 'Cualquier dígito del 0 al 9', 'Un bit es un dígito binario, así que solo admite dos valores.'),
        ('=', '{F} Convierte 00110011 a decimal.', '32+16+2+1', 'Se suman los valores de las posiciones donde hay un 1.'),
        ('abc', '{F} ¿Cómo se escribe 20 en 8 bits?', '00010100', '00010010', '00101000', '20 = 16 + 4, así que van 1 en las posiciones 16 y 4; 00010010 vale 18 y 00101000 vale 40.'),
        ('abc', '{F} ¿Cuál es el mayor número que se puede escribir con 8 bits?', '255', '256', '128', 'Con 8 bits hay 256 combinaciones y la primera es el 0, así que el mayor es 255.'),
        ('=', '{F} Convierte 11000001 a decimal.', '128+64+1', 'Los 1 están en las posiciones 128, 64 y 1.'),
        ('{F} Escribe 100 en 8 bits.', '01100100', '100 = 64 + 32 + 4, así que van 1 en esas posiciones y 0 en las demás.'),
        ('=', 'Con 7 bits, ¿cuál es el mayor número que se puede escribir?', '2*2*2*2*2*2*2-1', 'Con 7 bits hay 2 · 2 · … · 2 combinaciones y, como se parte en 0, el mayor número es esa cantidad menos 1.'),
        ('abc', '¿Cuántos bits se necesitan como mínimo para dar un código distinto a cada uno de 40 estudiantes?', '6 bits, porque 5 bits dan solo 32 combinaciones y 6 bits dan 64', '5 bits, porque 40 se parece a 32', '40 bits, uno por estudiante', 'Con 5 bits alcanzan 32 códigos, que no bastan para 40; con 6 bits hay 64.'),
        ('abc', 'Un contador de 8 bits está en 255 y recibe una unidad más; pasa a 00000000. ¿Cómo se llama y por qué ocurre?', 'Desborde: no hay un noveno bit para guardar 256', 'Redondeo: el computador aproxima 256 a 0', 'Resta automática: el contador descuenta 255', 'El resultado 256 no cabe en 8 bits, así que se pierde el bit extra y queda en cero.'),
        ('abc', 'Un contador de 8 bits está en 250 y recibe 10 unidades más. ¿Qué número queda guardado?', '4', '260', '10', 'Tras 5 unidades llega a 255, la siguiente lo deja en 0 por el desborde y las 4 restantes lo llevan a 4; 260 no cabe en 8 bits.'),
        ('abc', 'Para pasar 45 a binario, A escribe 00101101 y B escribe 00110101. ¿Quién tiene razón?', 'A: 32 + 8 + 4 + 1 = 45', 'B: 32 + 16 + 4 + 1 = 45', 'Ambos', 'A suma 45; la respuesta de B suma 32 + 16 + 4 + 1 = 53, así que no corresponde.'),
    ],
    ctx=('=', 'Un sensor envía niveles de 0 a 255 en un byte. Si manda 10010110, ¿qué nivel indica?', '128+16+4+2', 'Los 1 están en las posiciones 128, 16, 4 y 2.'),
    sc=[
        ("En Pensamiento computacional: ¿cuántos valores distintos puede tener un bit?", "Dos: 0 y 1", "Un bit es un dígito binario con solo dos valores posibles."),
        ("En un byte, ¿qué valor tiene la posición más a la izquierda?", "128", "Los valores de posición del byte son 128, 64, 32, 16, 8, 4, 2 y 1."),
        ("En Pensamiento computacional: ¿cuántos bits tiene un byte?", "8", "Un byte es un grupo de 8 bits."),
    ],
    op=("Convierte a binario de 8 bits los números 52, 90 y 200, y a decimal los números 00011100, 10100000 y 01111111. Después explica en una frase por qué 8 bits no alcanzan para escribir el número 300.",
        "52 = 00110100; 90 = 01011010; 200 = 11001000. 00011100 vale 28; 10100000 vale 160; 01111111 vale 127. Con 8 bits el mayor número es 255, y 300 es mayor.",
        ["convierte los seis números con el método de posiciones", "comprueba una conversión al revés", "explica el límite de 8 bits"],
        ["hoja con la tabla de conversiones y la frase final"],
        ["leer los bits de derecha a izquierda", "olvidar una posición", "creer que 8 bits llegan hasta 256"],
        "Pregunta: «¿qué valor tiene la posición donde pusiste el primer 1?». Si falla, pídele que escriba los valores sobre cada bit."),
    reinforce="Escribe los valores de posición de un byte y convierte 00000101, 00010000 y 00001111 a decimal.",
    extend="Explica cuántos valores distintos se pueden formar con 10 bits y cuál es el mayor número que se puede escribir.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (de ejemplo). Un computador guarda cada carácter como un número, según una tabla (como el estándar ASCII), usando un byte por carácter. Fragmento de la tabla: "
     "A = 65, B = 66, C = 67 … Z = 90 (las mayúsculas siguen el orden del alfabeto); a = 97, b = 98 … z = 122; los dígitos «0» = 48, «1» = 49 … «9» = 57; el espacio = 32. "
     "Para escribir números largos se usa la base 16 (hexadecimal): los dígitos son 0 a 9 y A = 10, B = 11, C = 12, D = 13, E = 14, F = 15; por ejemplo, 3F vale 3 · 16 + 15 = 63.")
build(
    O2, 2, F,
    use="Aprenderé cómo se representa un texto con números, a codificar y decodificar palabras con una tabla y a escribir un mismo número en decimal, binario y hexadecimal.",
    prior=["Sé convertir entre binario y decimal.", "Sé que el alfabeto tiene un orden.", "Sé que un byte tiene 8 bits."],
    explain=[
        "Un texto se guarda como una secuencia de números: cada carácter (letra, dígito, espacio o signo) tiene un código en una tabla. En la tabla de la ficha, A vale 65 y las demás mayúsculas siguen el orden del alfabeto, así que M vale 65 + 12 = 77. La minúscula de cada letra vale 32 más que su mayúscula: a vale 97 y A vale 65.",
        "El carácter «5» no es el número 5: es el código 53 de un símbolo. Por eso sumar dos caracteres de dígitos como si fueran números da resultados extraños. Esa tabla no incluye la ñ ni las tildes; otros estándares, como Unicode, amplían la tabla para incluirlas, y por eso la mayoría de los textos actuales usa Unicode.",
        "Un mismo código se puede escribir de varias maneras: 65 en decimal es 01000001 en binario (64 + 1) y 41 en hexadecimal (4 · 16 + 1). El hexadecimal es más corto que el binario y se usa mucho para mostrar bytes. Para ordenar nombres por código hay que tener cuidado, porque las mayúsculas tienen códigos menores que las minúsculas.",
    ],
    vocab=[("código", "número que representa un carácter"), ("carácter", "letra, dígito, espacio o signo"), ("tabla de códigos", "lista que asocia cada carácter con un número"), ("hexadecimal", "sistema de base 16 con dígitos 0 a 9 y A a F"), ("Unicode", "estándar que incluye letras y signos de muchos idiomas"), ("decodificar", "volver del número al carácter")],
    worked=[
        ("Codificar una palabra", "Codifica «CAB» con la tabla de la ficha.", ["C = 67, A = 65 y B = 66.", "Se escriben los códigos en el mismo orden de las letras."], "CAB se codifica 67 65 66"),
        ("Mayúscula y minúscula", "¿Qué código tiene la letra d y cuál es el de su mayúscula?", ["d está 3 lugares después de a: 97 + 3 = 100.", "Su mayúscula vale 32 menos: 100 − 32 = 68, que es D."], "d vale 100 y D vale 68"),
    ],
    mistakes=[("Pensar que el carácter «5» vale 5.", "El carácter es un símbolo con código 53; el número 5 es otro tipo de dato.", "Antes de calcular con dígitos escritos, conviértelos a número."),
              ("Creer que la ñ está en la tabla de la ficha.", "Esa tabla solo cubre letras sin tilde, dígitos y algunos signos.", "Para ñ y tildes se usan estándares más amplios, como Unicode.")],
    T=[
        ('abc', '{F} ¿Qué número guarda la letra C?', '67', '3', '99', 'C es la tercera letra después de A, por lo que vale 65 + 2 = 67; 99 corresponde a la minúscula c.'),
        ('abc', '{F} ¿Qué carácter representa el número 70?', 'F', 'E', 'G', '70 = 65 + 5, y la letra 5 lugares después de A es F.'),
        ('ab', '{F} ¿Qué es el carácter «7» en la tabla?', 'Un símbolo guardado con el código 55 (48 + 7)', 'El número 7 guardado en un solo bit', 'Los dígitos escritos son caracteres con código propio; «7» parte de 48 y suma 7.'),
        ('=', '{F} ¿Qué número guarda la letra R? (La A es la letra número 1 del alfabeto y la R es la número 18.)', '65+17', 'Entre A y R hay 17 letras de diferencia, y se suman al código de A.'),
        ('abc', '{F} ¿Cómo se codifica la palabra «BAD»?', '66 65 68', '66 65 67', '65 66 68', 'B vale 66, A vale 65 y D vale 68, en el orden de la palabra.'),
        ('abc', '{F} La palabra «oso» está en minúsculas. ¿Qué números la forman?', '111 115 111', '79 83 79', '111 83 111', 'Con a = 97, o vale 97 + 14 = 111 y s vale 97 + 18 = 115; 79 y 83 son las mayúsculas.'),
        ('=', '{F} ¿Qué número guarda la letra k minúscula? (La a es la letra número 1 y la k es la número 11.)', '97+10', 'Entre a y k hay 10 letras de diferencia, y se suman al código de a.'),
        ('=', '{F} El carácter «9» guarda el número 57. ¿Qué número guarda el carácter «4»?', '48+4', 'Los dígitos parten en 48 para «0» y suben de a uno.'),
        ('abc', '{F} En hexadecimal, ¿cuál es el valor decimal de 2A?', '42', '12', '210', '2A vale 2 · 16 + 10 = 42; 12 suma sin multiplicar y 210 pega los dígitos.'),
        ('abc', 'Un programa suma los caracteres «5» y «2» como si fueran números y obtiene 105. ¿Por qué?', 'Suma sus códigos, 53 y 52, y no los números 5 y 2', 'Porque 5 + 2 es 105 en la tabla', 'Porque el computador redondea', '53 + 52 = 105: lo que se suma son los códigos de los caracteres.'),
        ('abc', 'Una persona dice que la ñ se guarda con la tabla de la ficha entre 65 y 90. ¿Qué es correcto?', 'Esa tabla no incluye la ñ ni las tildes; otros estándares, como Unicode, sí', 'Sí: la ñ se guarda como 110 con un acento', 'Sí: la ñ vale 123', 'El rango 65 a 90 son las letras mayúsculas sin tilde; para ñ se necesitan estándares más amplios.'),
        ('abc', 'Los números 72, 79, 76 y 65 forman una palabra en mayúsculas. ¿Cuál es?', 'HOLA', 'HALO', 'LOHA', '72 es H, 79 es O, 76 es L y 65 es A, leídos en ese orden.'),
        ('=', 'Un mensaje de 12 caracteres se guarda con un byte (8 bits) por carácter. ¿Cuántos bits ocupa?', '12*8', 'Cada carácter ocupa 8 bits y hay 12 caracteres.'),
    ],
    ctx=('abc', 'Un programa ordena nombres comparando los códigos de sus letras. Los nombres «Zoe» y «abel» empiezan con Z (código 90) y a (código 97). ¿Qué orden entrega?', 'Zoe, abel, porque 90 es menor que 97, aunque alfabéticamente abel iría primero', 'abel, Zoe, porque la a va antes en el alfabeto', 'No puede ordenarlos', 'El programa compara números: 90 < 97, así que Zoe va antes; conviene pasar todo a minúsculas antes de comparar.'),
    sc=[
        ("En Pensamiento computacional: ¿qué es un código de carácter?", "El número que representa a un carácter en una tabla", "Cada letra, dígito o signo se guarda con un número."),
        ("¿Qué diferencia numérica hay entre una letra minúscula y su mayúscula en la tabla de la ficha?", "32", "Por ejemplo a vale 97 y A vale 65, una diferencia de 32."),
        ("En Pensamiento computacional: ¿qué letras se usan en hexadecimal además de los dígitos del 0 al 9?", "La A hasta la F", "A, B, C, D, E y F representan los valores del 10 al 15."),
    ],
    op=("Elige una palabra: SOL, MAR o PAZ. Escribe el código decimal de cada letra con la tabla de la ficha, luego cada código en binario de 8 bits y en hexadecimal. Comprueba una de las conversiones al revés.",
        "SOL: S = 83, O = 79, L = 76. En binario: 01010011, 01001111 y 01001100. En hexadecimal: 53, 4F y 4C. Comprobación: 4F = 4 · 16 + 15 = 79.",
        ["obtiene bien los códigos con la tabla", "convierte a binario y a hexadecimal", "comprueba una conversión al revés"],
        ["hoja con una tabla de tres letras y sus tres representaciones"],
        ["contar mal las posiciones desde A", "confundir mayúsculas con minúsculas", "olvidar que 4F es 4 · 16 + 15"],
        "Pregunta: «¿cuántas letras hay entre A y la tuya?». Si falla, pídele que cuente con los dedos desde A = 65."),
    reinforce="Escribe en decimal la palabra «CASA» con la tabla de la ficha y luego pasa el código de A a binario.",
    extend="Explica por qué una lista de nombres con mayúsculas y minúsculas mezcladas se ordena mal si solo se comparan los códigos.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (de ejemplo). Una imagen se guarda como una cuadrícula de píxeles. En blanco y negro: 0 = blanco y 1 = negro, con 1 bit por píxel. Imagen de 4 columnas por 3 filas: fila 1: 0110; fila 2: 1001; fila 3: 0110. "
     "En una imagen a color cada píxel guarda 3 valores (rojo, verde y azul), de 0 a 255, de un byte cada uno; como se mezcla luz, más valor significa más luz de ese color. "
     "Compresión por repeticiones: se anota cada valor con las veces que se repite; por ejemplo, 0000111 se guarda como 0×4, 1×3.")
build(
    O2, 3, F,
    use="Aprenderé cómo se representa una imagen con píxeles y colores, a calcular su tamaño y a ahorrar espacio con una compresión simple.",
    prior=["Sé que un byte tiene 8 bits.", "Sé multiplicar para contar elementos de una cuadrícula.", "Sé leer filas y columnas."],
    explain=[
        "Una imagen digital es una cuadrícula de píxeles, que son los puntos más pequeños con un color. En blanco y negro basta un bit por píxel: 0 para blanco y 1 para negro. El tamaño de una imagen en bits es columnas por filas por bits por píxel. La imagen de 4 columnas por 3 filas tiene 12 píxeles y ocupa 12 bits.",
        "En una imagen a color cada píxel guarda tres valores, para el rojo, el verde y el azul (RGB), de 0 a 255 cada uno, o sea 3 bytes por píxel. Con luz, (255, 0, 0) se ve rojo, (0, 0, 255) azul, (255, 255, 255) blanco y (0, 0, 0) negro. Una imagen de 10 columnas por 5 filas, a 3 bytes por píxel, ocupa 10 · 5 · 3 = 150 bytes.",
        "Más píxeles dan más detalle, pero el archivo pesa más: duplicar columnas y filas multiplica el tamaño por cuatro. Para ahorrar espacio se puede comprimir. La compresión por repeticiones sirve cuando hay zonas uniformes (0×60 para una fila blanca de 60 píxeles) y ayuda poco, o nada, cuando los valores alternan a cada paso. Siempre se comprueba que la imagen descomprimida sea igual a la original.",
    ],
    vocab=[("píxel", "punto más pequeño de una imagen digital"), ("resolución", "cantidad de columnas y filas de píxeles"), ("RGB", "color formado por rojo, verde y azul"), ("compresión", "guardar la información ocupando menos espacio"), ("descomprimir", "recuperar la información original")],
    worked=[
        ("Leer una imagen en bits", "¿Qué forma tiene la imagen de filas 0110, 1001 y 0110 (1 es negro)?", ["En la fila 1 hay dos píxeles negros en el centro; en la fila 2, uno en cada extremo.", "La fila 3 repite la fila 1: forma un óvalo hueco, como la letra O."], "Dibuja un anillo, parecido a una letra O"),
        ("Calcular el tamaño", "¿Cuántos bytes ocupa una imagen a color de 800 por 600 píxeles, a 3 bytes por píxel?", ["Píxeles: 800 · 600 = 480.000.", "Bytes: 480.000 · 3 = 1.440.000."], "Ocupa 1.440.000 bytes"),
    ],
    mistakes=[("Confundir columnas con filas y usar 3×4 en vez de 4×3.", "Para el tamaño da lo mismo, pero al leer la imagen cambia la forma.", "Las columnas son el ancho y las filas el alto."),
              ("Contar bytes cuando se pide bits, o al revés.", "Un byte tiene 8 bits; 12 bits son 1,5 bytes.", "Anota siempre la unidad y convierte con 8.")],
    T=[
        ('abc', 'Una imagen en blanco y negro tiene 6 columnas por 5 filas de píxeles. ¿Cuántos píxeles tiene?', '30', '11', '6', 'Los píxeles son columnas por filas: 6 · 5 = 30; 11 resulta de sumar.'),
        ('abc', '{F} En la imagen en blanco y negro, ¿qué representa el valor 1?', 'Un píxel negro', 'Un píxel blanco', 'Un píxel rojo', 'En la ficha 0 es blanco y 1 es negro.'),
        ('ab', '{F} ¿Cuántos valores se guardan por píxel en una imagen a color?', '3: rojo, verde y azul', '1: un solo número de gris', 'Cada píxel de color combina tres componentes de luz.'),
        ('=', 'Una imagen en blanco y negro de 16 columnas por 9 filas, a 1 bit por píxel, ¿cuántos bits ocupa?', '16*9', 'Hay un bit por cada píxel de la cuadrícula.'),
        ('abc', '{F} ¿Qué color da el píxel (255, 255, 255)?', 'Blanco', 'Negro', 'Rojo', 'Con el máximo de luz de los tres colores se obtiene blanco.'),
        ('abc', '{F} ¿Qué color da el píxel (255, 0, 0)?', 'Rojo', 'Verde', 'Amarillo', 'Solo el componente rojo tiene luz, de modo que el píxel se ve rojo.'),
        ('=', 'Una imagen a color de 12 columnas por 8 filas, a 3 bytes por píxel, ¿cuántos bytes ocupa?', '12*8*3', 'Se multiplican los píxeles por los bytes de cada uno.'),
        ('{F} Comprime la fila 0011100 con el formato valor×cantidad, separando con comas.', '0×2, 1×3, 0×2', 'La fila tiene dos ceros, tres unos y dos ceros, en ese orden.'),
        ('abc', '{F} Se descomprime 1×2, 0×3, 1×1. ¿Qué fila resulta?', '110001', '100011', '110010', 'Se escribe 11, luego 000 y luego 1, en ese orden.'),
        ('abc', 'Una fila de 60 píxeles es toda blanca (0×60). Otra alterna 0, 1, 0, 1… y su compresión por repeticiones necesita 60 pares. ¿Qué conclusión es correcta?', 'La compresión ahorra mucho en zonas uniformes y casi nada en patrones alternados', 'Ahorra lo mismo en ambos casos', 'Solo funciona con fotos a color', 'Una fila uniforme se resume en un par; una alternada necesita un par por cada píxel.'),
        ('abc', 'Una persona dice: «una foto con más píxeles siempre pesa lo mismo, pero se ve mejor». ¿Qué es correcto?', 'Más píxeles dan más detalle, pero el archivo ocupa más espacio', 'Pesa menos', 'Pesa igual', 'El tamaño sin comprimir crece con la cantidad de píxeles.'),
        ('=', 'Una imagen a color de 40 columnas por 30 filas, a 3 bytes por píxel, ¿cuántos bytes ocupa?', '40*30*3', 'Se multiplican columnas, filas y bytes por píxel.'),
        ('abc', 'Una imagen de 1.200 por 800 píxeles se reduce a 600 por 400 píxeles. ¿Cuántas veces menos píxeles tiene?', '4 veces menos', '2 veces menos', '8 veces menos', 'Se reducen a la mitad las columnas y también las filas, por lo que los píxeles se dividen por 2 · 2 = 4.'),
    ],
    ctx=('=', 'Un ícono de 8 por 8 píxeles en blanco y negro (1 bit por píxel) se guarda en un microcontrolador. ¿Cuántos bytes ocupa? (1 byte = 8 bits)', '8*8//8', 'Hay 64 bits y cada byte guarda 8 bits.', ' bytes'),
    sc=[
        ("En Pensamiento computacional: ¿qué es un píxel?", "El punto más pequeño de una imagen digital, con un color", "La imagen se forma al juntar muchos píxeles en una cuadrícula."),
        ("¿Qué tres colores base usa la representación RGB?", "Rojo, verde y azul", "RGB son las iniciales de red, green y blue, es decir, rojo, verde y azul."),
        ("¿Qué ocurre con el tamaño sin comprimir si se duplican las columnas y las filas?", "Se multiplica por cuatro", "Hay el doble de columnas y el doble de filas, así que 2 · 2 = 4 veces los píxeles."),
    ],
    op=("Elige una opción. Opción 1: diseña un ícono de 5 columnas por 5 filas en blanco y negro (una letra T o un corazón), escribe sus cinco filas con 0 y 1, calcula cuántos bits ocupa y comprime cada fila por repeticiones. "
        "Opción 2: escribe el RGB de tres colores (rojo puro, negro y amarillo, que mezcla rojo y verde al máximo) y calcula cuántos bytes ocupa una imagen de 20 por 10 píxeles a color.",
        "Opción 1: letra T. Filas 11111, 00100, 00100, 00100, 00100; ocupa 25 bits. Compresión: 1×5; 0×2, 1×1, 0×2 (cuatro veces). Opción 2: rojo (255, 0, 0), negro (0, 0, 0), amarillo (255, 255, 0); 20 · 10 · 3 = 600 bytes.",
        ["representa la imagen o los colores con valores correctos", "calcula el tamaño con la unidad correcta", "comprueba que la compresión se puede descomprimir"],
        ["hoja con la cuadrícula o los colores, el cálculo de tamaño y la compresión"],
        ["confundir filas con columnas", "mezclar bits con bytes", "comprimir sin poder recuperar la fila"],
        "Pregunta: «¿cuántos píxeles tiene tu imagen y cuántos bits usa cada uno?». Si no coincide con su tamaño, repasa la fórmula."),
    reinforce="Dibuja en papel cuadriculado la imagen de la ficha pintando de negro las celdas con 1.",
    extend="Explica por qué una fotografía con muchos tonos se comprime peor por repeticiones que un dibujo de pocos colores planos.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (de ejemplo; cifras inventadas para practicar). Un sonido se digitaliza midiendo la altura de su onda muchas veces por segundo; cada medición es una muestra. "
     "Frecuencia de muestreo: muestras por segundo. Profundidad: bits por muestra. Canales: 1 (mono) o 2 (estéreo). "
     "Tamaño sin comprimir = muestras por segundo × segundos × bits por muestra × canales. El sonido de la ficha usa 8.000 muestras por segundo, 8 bits por muestra y un canal.")
build(
    O2, 4, F,
    use="Aprenderé cómo se representa un sonido con números, a calcular el tamaño de un audio y a justificar qué configuración conviene según el uso.",
    prior=["Sé que un bit y un byte miden información.", "Sé multiplicar números grandes con calculadora.", "Sé que un sonido es una vibración que cambia en el tiempo."],
    explain=[
        "Un sonido real es continuo; para guardarlo se mide su altura (amplitud) muchas veces por segundo y cada medición se escribe como un número. Cada medición es una muestra. La frecuencia de muestreo indica cuántas muestras se toman por segundo, y la profundidad indica cuántos bits se usan por muestra. Un audio estéreo tiene dos canales (izquierdo y derecho) y un audio mono, uno.",
        "El tamaño sin comprimir se calcula multiplicando muestras por segundo, segundos, bits por muestra y canales. Con 8.000 muestras por segundo, 8 bits y un canal, un segundo ocupa 64.000 bits. Para pasar de bits a bytes se divide por 8. Aumentar la frecuencia, la profundidad o los canales mejora la fidelidad del sonido, pero también el tamaño del archivo.",
        "Para captar bien un tono de f vibraciones por segundo, la frecuencia de muestreo debe ser mayor que 2f; por ejemplo, un tono de 1.000 vibraciones por segundo exige más de 2.000 muestras por segundo. La mejor configuración depende del uso: para una nota de voz basta una calidad menor y pesa poco; para música se necesita más calidad. Se decide comparando el tamaño con la fidelidad que se necesita.",
    ],
    vocab=[("muestra", "una medición de la altura de la onda"), ("frecuencia de muestreo", "cantidad de muestras por segundo"), ("profundidad", "bits que se usan en cada muestra"), ("canal", "pista de audio: mono (1) o estéreo (2)"), ("fidelidad", "parecido entre el sonido guardado y el original")],
    worked=[
        ("Tamaño de un audio mono", "¿Cuántos bits ocupan 10 segundos del sonido de la ficha?", ["Muestras: 8.000 · 10 = 80.000.", "Bits: 80.000 · 8 bits por muestra = 640.000, con un solo canal."], "Ocupan 640.000 bits, es decir, 80.000 bytes"),
        ("Pasar a estéreo", "¿Qué pasa con ese tamaño si el mismo audio se graba en estéreo?", ["El estéreo tiene 2 canales, el doble de datos.", "640.000 · 2 = 1.280.000 bits."], "El tamaño se duplica: 1.280.000 bits"),
    ],
    mistakes=[("Olvidar multiplicar por los canales en un audio estéreo.", "Cada canal guarda sus propias muestras.", "Revisa los cuatro factores del tamaño antes de multiplicar."),
              ("Dar el tamaño en bits cuando se pide bytes.", "Un byte tiene 8 bits.", "Divide por 8 para pasar de bits a bytes.")],
    T=[
        ('abc', '{F} ¿Qué es una muestra de sonido?', 'Una medición de la altura de la onda en un instante', 'Un segundo completo de audio', 'Una nota musical', 'El sonido se guarda como una lista de mediciones, y cada una es una muestra.'),
        ('abc', '{F} ¿Cuántos canales tiene un audio mono?', '1', '2', '8', 'Mono significa un canal; estéreo tiene dos.'),
        ('ab', '{F} Si aumentan las muestras por segundo, ¿qué pasa con el tamaño sin comprimir del archivo?', 'Aumenta', 'Disminuye', 'Más muestras por segundo son más datos, así que el tamaño sube.'),
        ('=', '{F} ¿Cuántas muestras hay en 3 segundos del sonido de la ficha?', '8000*3', 'En cada segundo se toman 8.000 muestras, y hay que contar 3 segundos.'),
        ('=', '{F} ¿Cuántos bits ocupan 5 segundos del sonido de la ficha?', '8000*5*8', 'Se multiplican muestras por segundo, segundos y bits por muestra.'),
        ('abc', '{F} ¿Cuál de estos cambios NO aumenta el tamaño sin comprimir del archivo?', 'Bajar de 16.000 a 8.000 muestras por segundo', 'Pasar de mono a estéreo', 'Pasar de 8 a 16 bits por muestra', 'Menos muestras por segundo son menos datos; más canales o más bits por muestra agregan datos.'),
        ('=', 'Un sonido de ejemplo usa 10.000 muestras por segundo, 16 bits por muestra, un canal y dura 3 segundos. ¿Cuántos bits ocupa?', '10000*3*16', 'Se multiplican los tres factores, con un solo canal.'),
        ('=', 'Un audio ocupa 80.000 bits. ¿Cuántos bytes son? (1 byte = 8 bits)', '80000//8', 'Para pasar de bits a bytes se divide por 8.'),
        ('abc', 'Un tono de 2.500 vibraciones por segundo se graba. ¿Con qué frecuencia de muestreo se capta bien, según la regla de la explicación?', '6.000 muestras por segundo', '4.000 muestras por segundo', '2.500 muestras por segundo', 'La regla exige más del doble de 2.500, es decir, más de 5.000; 4.000 y 2.500 no cumplen.'),
        ('abc', 'Una app de notas de voz debe ahorrar espacio. ¿Qué decisión es razonable?', 'Bajar la frecuencia de muestreo y los bits, aceptando algo menos de fidelidad', 'Usar siempre la máxima calidad', 'Duplicar los canales', 'Para voz basta una calidad menor, y así el archivo pesa menos.'),
        ('abc', 'Una persona dice: «si grabo a 16 bits en vez de 8 bits, el archivo pesa lo mismo pero suena mejor». ¿Qué es correcto?', 'El tamaño se duplica, porque cada muestra usa el doble de bits', 'Pesa lo mismo', 'Pesa la mitad', 'La profundidad es uno de los factores del tamaño: pasar de 8 a 16 bits lo duplica.'),
        ('=', 'Un audio estéreo (2 canales) de 4 segundos usa 6.000 muestras por segundo y 8 bits por muestra. ¿Cuántos bits ocupa?', '6000*4*8*2', 'Se multiplican muestras por segundo, segundos, bits y canales.'),
        ('abc', 'Dos grabaciones del mismo audio mono: A usa 8.000 muestras por segundo y 8 bits; B usa 16.000 muestras por segundo y 8 bits. ¿Cuántas veces más pesa B que A?', '2 veces', '4 veces', '8 veces', 'Solo cambia la frecuencia de muestreo, que se duplica, así que el tamaño también.'),
    ],
    ctx=('=', 'Una radio escolar guarda 30 segundos de un saludo en mono, a 8.000 muestras por segundo y 8 bits por muestra. ¿Cuántos bytes ocupa?', '8000*30*8//8', 'Hay 8.000 · 30 muestras de un byte cada una.', ' bytes'),
    sc=[
        ("En Pensamiento computacional: ¿qué mide la frecuencia de muestreo?", "Cuántas muestras se toman por segundo", "Es la cantidad de mediciones del sonido que se guardan en cada segundo."),
        ("En Pensamiento computacional: ¿qué es un audio estéreo?", "Un audio con dos canales", "Estéreo usa un canal izquierdo y uno derecho."),
        ("¿Qué relación hay entre la calidad de un audio y su tamaño sin comprimir?", "A mayor calidad, mayor tamaño", "Más muestras, más bits o más canales significan más datos que guardar."),
    ],
    op=("Compara tres configuraciones de un audio de 6 segundos: C1 (8.000 muestras por segundo, 8 bits, mono), C2 (16.000 muestras por segundo, 16 bits, mono) y C3 (16.000 muestras por segundo, 16 bits, estéreo). "
        "Calcula el tamaño en bits de cada una y recomienda una configuración para una nota de voz y otra para una canción, con una razón para cada una.",
        "C1: 8.000 · 6 · 8 = 384.000 bits; C2: 16.000 · 6 · 16 = 1.536.000 bits; C3: 3.072.000 bits. Para voz, C1 (pesa poco y basta); para una canción, C3 (más fidelidad y dos canales).",
        ["calcula los tres tamaños con los factores correctos", "recomienda una configuración por uso", "justifica relacionando calidad y tamaño"],
        ["hoja con los tres cálculos y las dos recomendaciones justificadas"],
        ["olvidar los canales", "mezclar bits con bytes", "recomendar sin justificar con el tamaño o la fidelidad"],
        "Pregunta: «¿cuántos factores multiplicaste?». Si faltan canales o segundos, pídele que rehaga el cálculo."),
    reinforce="Calcula los bits de 2 segundos del sonido de la ficha y luego pásalos a bytes.",
    extend="Explica por qué pasar de mono a estéreo y de 8 a 16 bits multiplica el tamaño por cuatro.",
)
