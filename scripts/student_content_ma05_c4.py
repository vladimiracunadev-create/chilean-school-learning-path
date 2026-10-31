"""Student material for 5.º básico Matemática, OA 27 (diagramas de tallo y hojas con datos de muestras aleatorias)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA27 = "MA05 OA 27"

DIAG1 = "Diagrama de tallo y hojas «Minutos para llegar al colegio» (muestra sorteada de 12 estudiantes). Clave: 2 | 5 significa 25 minutos. Tallo 1: hojas 2, 4, 8. Tallo 2: hojas 2, 5, 5, 5, 7. Tallo 3: hojas 1, 1, 5. Tallo 4: hoja 0."
LIBROS = "Datos de una muestra sorteada de 10 estudiantes: páginas leídas en una semana: 45, 52, 38, 45, 61, 52, 47, 38, 55, 45."
DIAG2 = "Diagrama de esos datos: tallo 3 con hojas 8, 8; tallo 4 con hojas 5, 5, 5, 7; tallo 5 con hojas 2, 2, 5; tallo 6 con hoja 1. Clave: 4 | 7 significa 47 páginas."
PUNTOS = "Diagrama de tallo y hojas «Puntos en un juego» (muestra sorteada de 15 estudiantes). Clave: 3 | 5 significa 35 puntos. Tallo 2: hojas 8, 8, 8. Tallo 3: hojas 3, 5, 5, 7, 9. Tallo 4: hojas 1, 3, 4, 7. Tallo 5: hojas 0, 2, 6."
PASOS = "Diagrama de tallo y hojas «Pasos en un minuto de caminata» (muestra sorteada de 10 estudiantes). Clave: 11 | 2 significa 112 pasos. Tallo 10: hojas 5, 8, 8. Tallo 11: hojas 2, 2, 2, 8. Tallo 12: hojas 0, 5. Tallo 13: hoja 0."
SEG = "Diagrama de tallo y hojas «Segundos en armar un rompecabezas pequeño» (muestra sorteada de 8 estudiantes). Clave: 1 | 2 significa 12 segundos. Tallo 1: hojas 2, 2, 4, 4. Tallo 2: sin hojas. Tallo 3: hojas 1, 3, 5, 8."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA27, 1,
    materials="Lápiz y papel. Los diagramas están descritos con palabras y números dentro de cada ejercicio; puedes dibujarlos en tu cuaderno.",
    use="Aprenderé qué es una muestra aleatoria y cómo leer un diagrama de tallo y hojas con su clave. Sirve para ordenar muchos datos de manera que se vean todos a la vez.",
    prior=["Sé leer números de dos cifras: decenas y unidades.", "Sé leer tablas y gráficos de barras."],
    explain=[
        "A veces no se puede preguntar a todos. Entonces se elige una muestra, que es una parte pequeña del grupo. Si la muestra se elige por sorteo, de modo que todos tengan la misma posibilidad de salir, se llama muestra aleatoria. Sus datos sirven para saber cómo es todo el grupo.",
        "Un diagrama de tallo y hojas ordena los datos usando las cifras de cada número. El tallo es lo que queda a la izquierda, las decenas. La hoja es la última cifra, las unidades. El número 35 tiene tallo 3 y hoja 5. Todos los números de la misma decena comparten el tallo.",
        "La clave explica qué significa una pareja tallo y hoja. «Clave: 2 | 5 significa 25 minutos» dice que el tallo 2 con la hoja 5 es 25 y que los datos son minutos. Cada hoja es un dato: si un tallo tiene cinco hojas, hay cinco datos en esa decena. Los números repetidos se escriben una vez por cada dato.",
    ],
    vocab=[("muestra", "parte del grupo de la que se obtienen datos"), ("muestra aleatoria", "muestra elegida por sorteo, donde todos tienen la misma posibilidad de salir"), ("tallo", "las decenas de cada número, a la izquierda"), ("hoja", "la cifra de las unidades, a la derecha"), ("clave", "frase que dice qué significa un tallo con una hoja")],
    worked=[
        {"title": "Leer una pareja tallo y hoja", "problem": DIAG1 + " ¿Qué número es el tallo 3 con la hoja 5?", "steps": ["El tallo 3 son las decenas: 30.", "La hoja 5 son las unidades: 30 + 5 = 35."], "answer": "Es 35 minutos"},
        {"title": "Contar datos", "problem": DIAG1 + " ¿Cuántos estudiantes tiene la muestra?", "steps": ["Cuento las hojas de cada tallo: 3, 5, 3 y 1.", "3 + 5 + 3 + 1 = 12."], "answer": "La muestra tiene 12 estudiantes"},
    ],
    mistakes=[
        {"wrong": "Sumar el tallo y todas las hojas, como 2 + 2 + 5 + 5 + 5 + 7.", "why": "Se piensa que el tallo y las hojas forman un solo número.", "fix": "Cada hoja forma un número con el tallo: 22, 25, 25, 25 y 27."},
        {"wrong": "Ignorar la clave y leer 2 | 5 como dos coma cinco.", "why": "Se olvida que la clave dice que el tallo son decenas.", "fix": "Lee la clave: 2 | 5 significa 25."},
    ],
    tiers={
        "recovery": [
            ex(DIAG1 + " ¿Qué número es el tallo 1 con la hoja 4?", "14 minutos", "Tallo 1 es 10 y la hoja 4 se suma."),
            ex(DIAG1 + " ¿Cuántas hojas tiene el tallo 4?", "1", "Solo está la hoja 0."),
            ex(DIAG1 + " ¿Cuántos estudiantes tiene la muestra?", "12", "Hay 3 + 5 + 3 + 1 hojas.", calc="3+5+3+1"),
        ],
        "understand": [
            ex(DIAG1 + " ¿Cuántos estudiantes tardan 25 minutos?", "3", "El tallo 2 tiene tres hojas 5."),
            ex(DIAG1 + " ¿Cuál es el menor tiempo de la muestra?", "12 minutos", "Es la primera hoja del primer tallo."),
            ex(DIAG1 + " ¿Cuál es el mayor tiempo de la muestra?", "40 minutos", "Es el tallo 4 con la hoja 0."),
        ],
        "apply": [
            ex(DIAG1 + " ¿Cuántos estudiantes tardan menos de 20 minutos?", "3", "Son 12, 14 y 18."),
            ex(DIAG1 + " ¿Cuántos estudiantes tardan 30 minutos o más?", "4", "Son 31, 31, 35 y 40."),
            ex(DIAG1 + " Escribe los números del tallo 3.", "31, 31 y 35", "El tallo 3 con cada hoja forma esos números."),
        ],
        "reason": [
            ex("Camila dice que el tallo 2 con hojas 2, 5, 5, 5 y 7 vale 2 + 2 + 5 + 5 + 5 + 7. ¿Qué error tiene?", "Cada hoja forma un número con el tallo: 22, 25, 25, 25 y 27", "Las hojas son datos separados."),
            ex("En un diagrama de minutos, ¿por qué es importante la clave?", "Dice que 2 | 5 es 25 minutos y no, por ejemplo, 2,5", "Sin clave no se sabe qué número ni qué unidad es."),
        ],
        "challenge": [
            ex(DIAG1 + " Se agrega un estudiante que tarda 33 minutos. ¿En qué tallo va y con qué hoja?", "Tallo 3, hoja 3", "33 son 3 decenas y 3 unidades."),
            arith(DIAG1 + " ¿Cuántos minutos separan al estudiante que tarda menos del que tarda más?", "40-12", "Se resta el menor al mayor.", " minutos"),
        ],
    },
    context=[ex("Para saber cuánto tardan los 200 estudiantes de un colegio en llegar, se sortean 12 nombres de la lista completa. ¿Es una muestra aleatoria?", "Sí", "Todos tienen la misma posibilidad de salir en el sorteo.")],
    selfcheck=[
        ex("Una muestra se elige solo entre los amigos de Ema. ¿Es aleatoria?", "No", "Los otros estudiantes no tienen posibilidad de salir."),
        ex(DIAG1 + " ¿Qué número es el tallo 2 con la hoja 7?", "27 minutos", "El tallo 2 es 20 y se suma 7."),
        ex("En el número 48, ¿cuál es el tallo y cuál es la hoja?", "Tallo 4, hoja 8", "El tallo son las decenas y la hoja las unidades."),
    ],
    open_task=task(
        "Usa estos datos de una muestra sorteada de 12 estudiantes, que dicen los minutos que tardan en llegar al colegio: 12, 25, 31, 18, 25, 40, 22, 35, 14, 27, 31, 25. Dibuja el diagrama de tallo y hojas con los tallos 1, 2, 3 y 4, escribe la clave y di dos cosas que ves en él.",
        "Tallo 1: 2 4 8. Tallo 2: 2 5 5 5 7. Tallo 3: 1 1 5. Tallo 4: 0. Clave: 2 | 5 significa 25 minutos. Veo que muchos tardan entre 20 y 29 y que el que más tarda llega a 40.",
        ["los cuatro tallos están escritos", "cada dato aparece una vez", "escribe la clave", "dos observaciones con números"],
        ["diagrama", "clave", "observaciones"],
        ["olvidar un dato repetido", "no escribir la clave"],
        "Pide contar las hojas y comparar con los 12 datos. Reconoce que la clave esté completa.",
    ),
    reinforce="Escribe diez números de dos cifras que quieras y di el tallo y la hoja de cada uno.",
    extend="Explica con tus palabras por qué una muestra elegida por sorteo representa mejor al grupo que una elegida entre amigos.",
)

register(
    OA27, 2,
    materials="Lápiz y papel. En la actividad final, 8 papelitos para sortear. Los diagramas están descritos con palabras y números en cada ejercicio.",
    use="Aprenderé a construir un diagrama de tallo y hojas desde una lista de datos y a volver del diagrama a la lista. Sirve para pasar de una representación a otra sin perder datos.",
    prior=["Sé qué es el tallo, la hoja y la clave.", "Sé ordenar números de menor a mayor."],
    explain=[
        "Para construir un diagrama desde una lista, sigue cuatro pasos. Primero, escribe en una columna los tallos que necesitas, de menor a mayor. Segundo, para cada dato, escribe su hoja junto al tallo que le corresponde. Tercero, ordena las hojas de cada tallo de menor a mayor. Cuarto, escribe la clave.",
        "Para volver a la lista, une cada tallo con cada una de sus hojas. El tallo 4 con las hojas 5, 5, 5 y 7 da los datos 45, 45, 45 y 47. Un diagrama bien hecho tiene tantas hojas como datos tiene la lista, y por eso puedes comprobar contando.",
        "Los errores más comunes son olvidar una hoja repetida, poner las hojas sin orden y usar mal el tallo. Para comprobar, cuenta las hojas del diagrama y compáralas con los datos de la lista. Si el número de hojas es distinto del de datos, falta algo o sobra algo.",
    ],
    vocab=[("lista de datos", "datos escritos uno tras otro, sin orden"), ("construir", "armar el diagrama a partir de los datos"), ("ordenar las hojas", "escribirlas de menor a mayor en cada tallo"), ("comprobar", "contar las hojas y compararlas con los datos")],
    worked=[
        {"title": "De la lista al diagrama", "problem": LIBROS + " Construye el diagrama.", "steps": ["Los tallos son 3, 4, 5 y 6. Pongo cada hoja en su tallo.", "Ordeno: tallo 3 con 8, 8; tallo 4 con 5, 5, 5, 7; tallo 5 con 2, 2, 5; tallo 6 con 1."], "answer": "El diagrama tiene 2 + 4 + 3 + 1 = 10 hojas, igual que los datos"},
        {"title": "Del diagrama a la lista", "problem": "Un diagrama tiene tallo 2 con hojas 0 y 5, y tallo 3 con hojas 1, 1 y 9. Clave: 3 | 1 significa 31. Escribe los datos.", "steps": ["El tallo 2 da 20 y 25.", "El tallo 3 da 31, 31 y 39."], "answer": "Los datos son 20, 25, 31, 31 y 39"},
    ],
    mistakes=[
        {"wrong": "Escribir el número 38 como tallo 8 y hoja 3.", "why": "Se invierten las decenas y las unidades.", "fix": "En 38 el tallo es 3 y la hoja es 8."},
        {"wrong": "Escribir las hojas de un tallo en el orden en que aparecieron los datos.", "why": "No se ordenan las hojas.", "fix": "Ordena las hojas de menor a mayor en cada tallo."},
    ],
    tiers={
        "recovery": [
            ex(LIBROS + " ¿Qué tallos usa el diagrama que representa estos datos?", "3, 4, 5 y 6", "Son las decenas de 38, 45, 52 y 61."),
            ex("¿Cuál es la hoja del número 47?", "7", "La hoja es la cifra de las unidades."),
            ex("¿Cuál es el tallo del número 61?", "6", "El tallo son las decenas."),
        ],
        "understand": [
            ex(DIAG2 + " ¿Cuántas hojas tiene el tallo 4?", "4", "Son 5, 5, 5 y 7."),
            ex(DIAG2 + " ¿Cuántos datos tiene el diagrama en total?", "10", "2 + 4 + 3 + 1 hojas.", calc="2+4+3+1"),
            ex(DIAG2 + " Escribe los números que representa el tallo 5.", "52, 52 y 55", "El tallo 5 se une a las hojas 2, 2 y 5."),
        ],
        "apply": [
            ex("Datos: 21, 34, 25, 31, 22. ¿Cuántas hojas tendrá el tallo 2 del diagrama?", "3", "Los datos 21, 25 y 22 empiezan en 2."),
            ex("Datos: 21, 34, 25, 31, 22. ¿En qué orden van las hojas del tallo 2?", "1, 2, 5", "Se ordenan de menor a mayor."),
            ex("Datos: 21, 34, 25, 31, 22. ¿Qué números van en el tallo 3, ordenados?", "31 y 34", "Son los datos que empiezan en 3."),
        ],
        "reason": [
            ex("Tomás escribió el tallo 4 con las hojas 7, 5, 5 y 5. Dice que está bien. ¿Qué le falta?", "Ordenar las hojas: 5, 5, 5 y 7", "Las hojas deben ir de menor a mayor."),
            ex("Ana escribió el 38 en el tallo 8 con la hoja 3. ¿Qué error hay?", "Invirtió las cifras; el tallo es 3 y la hoja es 8", "El tallo son las decenas."),
        ],
        "challenge": [
            ex("Un diagrama tiene tallo 2 con hojas 0 y 5, y tallo 3 con hojas 1, 1 y 9. Escribe todos los datos.", "20, 25, 31, 31 y 39", "Cada hoja se une a su tallo."),
            ex("Un diagrama tiene 7 hojas en total y solo los tallos 1, 2 y 3. El tallo 1 tiene 2 hojas y el tallo 3 tiene 4. ¿Cuántas hojas tiene el tallo 2?", "1", "7 − 2 − 4 = 1.", calc="7-2-4"),
        ],
    },
    context=[ex("Una profesora sorteó 6 estudiantes y anotó cuántos libros leyó cada uno este año: 14, 23, 18, 23, 31, 14. Al armar el diagrama, ¿cuántas hojas tiene el tallo 1?", "3", "Los datos 14, 18 y 14 empiezan en 1.")],
    selfcheck=[
        ex("¿Cuál es la hoja del número 52?", "2", "Es la cifra de las unidades."),
        ex("Un diagrama tiene tallo 6 con las hojas 0 y 4. ¿Qué datos representa?", "60 y 64", "Se une el tallo con cada hoja."),
        ex("Una lista tiene 9 datos. ¿Cuántas hojas debe tener su diagrama?", "9", "Cada hoja es un dato."),
    ],
    open_task=task(
        "Estos son los minutos que tardan en llegar al colegio 20 estudiantes: 12, 25, 31, 18, 25, 40, 22, 35, 14, 27, 31, 25, 19, 33, 28, 42, 16, 30, 24, 37. Escribe cada número en un papelito, mézclalos y saca 8 sin mirar. Con esos 8 datos construye un diagrama de tallo y hojas con su clave y comprueba que tenga 8 hojas.",
        "Si salieron 25, 31, 18, 40, 22, 35, 14 y 27: Tallo 1: 4 8. Tallo 2: 2 5 7. Tallo 3: 1 5. Tallo 4: 0. Clave: 2 | 5 significa 25 minutos. Hay 8 hojas.",
        ["usa un sorteo para elegir la muestra", "los tallos están ordenados", "las hojas están ordenadas", "la clave está escrita", "las hojas son 8"],
        ["muestra sorteada", "diagrama", "clave y conteo"],
        ["elegir los datos a gusto", "no ordenar las hojas"],
        "Pide contar las hojas y comparar con 8. Reconoce que haya hecho el sorteo.",
    ),
    reinforce="Elige seis números de dos cifras y arma un diagrama de tallo y hojas con su clave.",
    extend="Escribe los pasos para construir un diagrama de tallo y hojas para que otra persona pueda seguirlos.",
)

register(
    OA27, 3,
    materials="Lápiz y papel. El diagrama está descrito con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a elegir una estrategia para sacar información de un diagrama de tallo y hojas: menor, mayor, el valor que más se repite y cuántos datos cumplen una condición. Sirve para responder preguntas sobre los datos de una muestra.",
    prior=["Sé leer un diagrama de tallo y hojas.", "Sé sumar y restar números de dos cifras."],
    explain=[
        "El diagrama deja ver varias cosas de un vistazo. El menor dato es la primera hoja del primer tallo, y el mayor es la última hoja del último tallo. El tallo con más hojas es la decena donde hay más datos. Un valor repetido aparece con la misma hoja varias veces seguidas.",
        "Para contar cuántos datos cumplen una condición, como «menos de 40», suma las hojas de los tallos que cumplen. Si la condición corta un tallo, mira cada hoja. Para saber el valor que más se repite, busca, en cada tallo, la hoja que más se repite; compara entre tallos y arma el número con su tallo.",
        "Para justificar tu respuesta, escribe los números que usaste. El diagrama es útil porque guarda los datos exactos y los ordena. Una lista desordenada también los guarda, pero cuesta más encontrar el menor, el mayor o los repetidos. El tallo más largo muestra dónde se concentran los datos.",
    ],
    vocab=[("valor que más se repite", "dato que aparece más veces"), ("concentración", "decena donde hay más datos"), ("condición", "regla que deben cumplir los datos, como «menos de 40»"), ("estrategia", "método para resolver una pregunta")],
    worked=[
        {"title": "Datos que cumplen una condición", "problem": PUNTOS + " ¿Cuántos estudiantes sacaron menos de 40 puntos?", "steps": ["Los tallos 2 y 3 son menores que 40.", "El tallo 2 tiene 3 hojas y el tallo 3 tiene 5: 3 + 5 = 8."], "answer": "Sacaron menos de 40 puntos 8 estudiantes"},
        {"title": "El valor que más se repite", "problem": PUNTOS + " ¿Qué puntaje se repite más?", "steps": ["En el tallo 2, la hoja 8 aparece 3 veces.", "El puntaje es 28 y no hay otra hoja que aparezca tantas veces."], "answer": "El puntaje que más se repite es 28"},
    ],
    mistakes=[
        {"wrong": "Decir que el tallo con más hojas es el que tiene el número mayor.", "why": "Se confunde la decena más alta con la decena con más datos.", "fix": "El tallo con más hojas es el que tiene más datos; en el ejemplo es el tallo 3."},
        {"wrong": "Contar los tallos en lugar de las hojas para saber cuántos datos hay.", "why": "Cada hoja es un dato y no cada tallo.", "fix": "Cuenta las hojas de todos los tallos."},
    ],
    tiers={
        "recovery": [
            ex(PUNTOS + " ¿Cuál es el menor puntaje?", "28 puntos", "Es la primera hoja del primer tallo."),
            ex(PUNTOS + " ¿Cuál es el mayor puntaje?", "56 puntos", "Es la última hoja del último tallo."),
            ex(PUNTOS + " ¿Cuántos estudiantes hay en la muestra?", "15", "Hay 3 + 5 + 4 + 3 hojas.", calc="3+5+4+3"),
        ],
        "understand": [
            ex(PUNTOS + " ¿Qué puntaje se repite más veces?", "28", "La hoja 8 aparece 3 veces en el tallo 2."),
            ex(PUNTOS + " ¿Qué tallo tiene más hojas?", "El tallo 3", "Tiene 5 hojas, más que los otros."),
            ex(PUNTOS + " ¿Cuántos estudiantes sacaron menos de 40 puntos?", "8", "El tallo 2 tiene 3 hojas y el tallo 3 tiene 5.", calc="3+5"),
        ],
        "apply": [
            ex(PUNTOS + " ¿Cuántos estudiantes sacaron 40 puntos o más?", "7", "El tallo 4 tiene 4 hojas y el tallo 5 tiene 3.", calc="4+3"),
            arith(PUNTOS + " ¿Cuántos puntos hay de diferencia entre el mayor y el menor puntaje?", "56-28", "Se resta el menor al mayor.", " puntos"),
            ex(PUNTOS + " ¿Cuántos estudiantes sacaron entre 30 y 39 puntos?", "5", "Es el tallo 3, que tiene 5 hojas."),
        ],
        "reason": [
            ex("Dani dice que el tallo con más hojas es el que tiene el número mayor. ¿Qué error tiene?", "El tallo con más hojas es el que tiene más datos, sin importar su valor", "Cada hoja es un dato."),
            ex("Ema dice que para ver cuántas veces se repite un número es mejor una lista desordenada que el diagrama. ¿Estás de acuerdo?", "No; en el diagrama los repetidos quedan juntos y ordenados", "Las hojas iguales se ven seguidas."),
        ],
        "challenge": [
            ex(PUNTOS + " ¿Cuántos estudiantes sacaron más de 45 puntos?", "4", "Son 47, 50, 52 y 56."),
            ex(PUNTOS + " Si se ordenan los 15 puntajes de menor a mayor, ¿qué puntaje ocupa el lugar 8?", "39", "Hay 3 en el tallo 2 y 5 en el tallo 3; el lugar 8 es la última hoja del tallo 3."),
        ],
    },
    context=[ex(PUNTOS + " ¿Más de la mitad de la muestra sacó menos de 40 puntos?", "Sí", "8 de 15 es más que la mitad, que es 7 y medio.")],
    selfcheck=[
        ex(PUNTOS + " ¿Cuántos estudiantes sacaron 50 puntos o más?", "3", "El tallo 5 tiene tres hojas."),
        ex(PUNTOS + " ¿Cuántos estudiantes sacaron 35 puntos?", "2", "El tallo 3 tiene dos hojas 5."),
        ex("¿Qué dato es el menor en un diagrama: la primera hoja del primer tallo o la última del último?", "La primera hoja del primer tallo", "Los datos están ordenados de menor a mayor."),
    ],
    open_task=task(
        "Usa el diagrama de puntos de esta clase. Escribe cinco datos que descubras en él, por ejemplo el menor, el mayor, el puntaje que más se repite, cuántos sacaron menos de 40 y cuántos sacaron 50 o más. Después explica con una frase por qué el diagrama ayudó a encontrarlos. " + PUNTOS,
        "Menor 28; mayor 56; el puntaje que más se repite es 28; 8 sacaron menos de 40; 3 sacaron 50 o más. El diagrama los ordena y se ven rápido.",
        ["los cinco datos son correctos", "indica cómo contó", "explica una ventaja del diagrama"],
        ["cinco datos", "justificación"],
        ["confundir tallo con hoja", "contar tallos en vez de hojas"],
        "Pide mostrar con el dedo qué hojas contó. Reconoce la explicación de la ventaja.",
    ),
    reinforce="Dibuja un diagrama con ocho datos tuyos y busca el mayor, el menor y el que más se repite.",
    extend="Escribe dos preguntas distintas sobre el diagrama de puntos y responde cada una con números.",
)

register(
    OA27, 4,
    materials="Lápiz y papel. Los diagramas están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a usar diagramas de tallo y hojas en casos nuevos: números de tres cifras, tallos vacíos y datos que se agregan. Sirve para usar el diagrama aunque los datos no sean como los de antes.",
    prior=["Sé construir y leer diagramas de tallo y hojas.", "Sé que la hoja es la última cifra del número."],
    explain=[
        "En un número de tres cifras, la hoja sigue siendo la última cifra, y el tallo son todas las cifras anteriores. El número 105 tiene tallo 10 y hoja 5. El número 125 tiene tallo 12 y hoja 5. La clave dice, por ejemplo, 11 | 2 significa 112.",
        "Si entre dos tallos no hay ningún dato, igual se escribe el tallo sin hojas. Así se ve que no hay datos en esa decena. Si se borra ese tallo, parece que los datos están seguidos, aunque hay un salto.",
        "Cuando se agrega un dato nuevo, se busca su tallo y se escribe su hoja en el lugar correcto, sin romper el orden. Después se vuelve a contar el total de hojas. Es lo mismo que en los casos de dos cifras: solo cambia cuántas cifras tiene el tallo.",
    ],
    vocab=[("tallo vacío", "tallo sin hojas, que muestra que no hay datos en esa decena"), ("tres cifras", "números como 105, que tienen centenas, decenas y unidades"), ("dato nuevo", "dato que se agrega después de armar el diagrama"), ("clave", "frase que dice qué significa una pareja tallo y hoja")],
    worked=[
        {"title": "Números de tres cifras", "problem": PASOS + " ¿Cuántos estudiantes dieron 112 pasos?", "steps": ["El tallo 11 con la hoja 2 es 112.", "La hoja 2 aparece 3 veces en el tallo 11."], "answer": "Dieron 112 pasos 3 estudiantes"},
        {"title": "Un tallo vacío", "problem": SEG + " ¿Cuántos estudiantes tardan entre 20 y 29 segundos?", "steps": ["Miro el tallo 2.", "No tiene hojas."], "answer": "Ningún estudiante, porque el tallo 2 no tiene hojas"},
    ],
    mistakes=[
        {"wrong": "Escribir el 108 con tallo 1 y hoja 08.", "why": "Se separa mal el número de tres cifras.", "fix": "En 108 el tallo es 10 y la hoja es 8."},
        {"wrong": "Borrar un tallo sin hojas del diagrama.", "why": "Se pierde la información de que no hay datos en esa decena.", "fix": "Escribe el tallo vacío para que se vea el salto."},
    ],
    tiers={
        "recovery": [
            ex(PASOS + " ¿Qué número es el tallo 10 con la hoja 5?", "105 pasos", "El tallo es 10 y la hoja es 5."),
            ex(PASOS + " ¿Qué número es el tallo 12 con la hoja 5?", "125 pasos", "El tallo es 12 y la hoja es 5."),
            ex(PASOS + " ¿Cuántos estudiantes tiene la muestra?", "10", "Hay 3 + 4 + 2 + 1 hojas.", calc="3+4+2+1"),
        ],
        "understand": [
            ex(PASOS + " ¿Cuántos estudiantes dieron 112 pasos?", "3", "La hoja 2 aparece tres veces en el tallo 11."),
            ex(PASOS + " ¿Cuál es el mayor número de pasos?", "130 pasos", "Es el tallo 13 con la hoja 0."),
            ex(PASOS + " ¿Cuántos estudiantes dieron menos de 110 pasos?", "3", "Son 105, 108 y 108."),
        ],
        "apply": [
            ex(SEG + " ¿Cuántos estudiantes tardan entre 20 y 29 segundos?", "0", "El tallo 2 no tiene hojas."),
            ex(SEG + " Se agrega un dato de 27 segundos. ¿En qué tallo va y con qué hoja?", "Tallo 2, hoja 7", "27 son 2 decenas y 7 unidades."),
            arith(SEG + " Se agregan los datos 27 y 31. ¿Cuántos datos tiene ahora el diagrama?", "8+2", "Se suman los 8 datos antes y los 2 nuevos.", " datos"),
        ],
        "reason": [
            ex(SEG + " Beto dice que borrar el tallo 2, que no tiene hojas, no cambia nada. ¿Qué le respondes?", "Sí cambia: sin él no se ve que no hay datos entre 20 y 29", "El tallo vacío muestra el salto."),
            ex("Lía escribió el número 108 como tallo 1 y hoja 08. ¿Qué error hay?", "En un número de tres cifras, el tallo es 10 y la hoja es 8", "La hoja es solo la última cifra."),
        ],
        "challenge": [
            ex("Datos de una muestra sorteada: 132, 128, 135, 141, 128, 139. ¿Cuántas hojas tiene el tallo 12?", "2", "Los datos 128 y 128 tienen tallo 12."),
            arith("Datos de una muestra sorteada: 132, 128, 135, 141, 128, 139. ¿Cuántas unidades separan al mayor y al menor?", "141-128", "Se resta el menor al mayor.", " unidades"),
        ],
    },
    context=[ex(PASOS + " ¿Más de la mitad de la muestra dio 112 pasos o más?", "Sí", "Son 7 de 10 estudiantes: 4 en el tallo 11, 2 en el tallo 12 y 1 en el tallo 13.")],
    selfcheck=[
        ex("En el número 119, ¿cuál es el tallo y cuál es la hoja?", "Tallo 11, hoja 9", "La hoja es la última cifra."),
        ex(SEG + " ¿Cuántos estudiantes tardan 14 segundos?", "2", "El tallo 1 tiene dos hojas 4."),
        ex("Un tallo sin hojas en un diagrama, ¿significa que hay datos o que no hay datos?", "Que no hay datos", "No tiene ninguna hoja."),
    ],
    open_task=task(
        "Estos son los pasos que dan en un minuto de caminata 10 estudiantes sorteados: 105, 112, 108, 120, 112, 125, 118, 112, 130, 108. Construye el diagrama de tallo y hojas con su clave y escribe tres conclusiones con números. Después agrega un dato nuevo de 123 y explica dónde lo escribes.",
        "Tallo 10: 5 8 8. Tallo 11: 2 2 2 8. Tallo 12: 0 5. Tallo 13: 0. Clave: 11 | 2 significa 112. Conclusiones: el menor es 105 y el mayor es 130; 112 se repite 3 veces; 7 estudiantes dieron 112 o más. El 123 va en el tallo 12, entre 0 y 5.",
        ["tallos 10, 11, 12 y 13 bien escritos", "10 hojas ordenadas", "clave escrita", "tres conclusiones con números", "ubica 123 en el tallo 12 entre 0 y 5"],
        ["diagrama", "tres conclusiones", "dato nuevo"],
        ["separar mal las cifras", "no ordenar las hojas"],
        "Pide mostrar de dónde sacó cada número. Reconoce que ubique el dato nuevo en orden.",
    ),
    reinforce="Escribe cinco números entre 100 y 150 y di el tallo y la hoja de cada uno.",
    extend="Arma un diagrama de tallo y hojas con un tallo vacío y escribe una frase que explique qué dice ese tallo.",
)
