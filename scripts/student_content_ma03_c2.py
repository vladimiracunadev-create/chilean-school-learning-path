"""Student material for 3.º básico Matemática, OA 21 (perímetro) y OA 22 (peso en gramos y kilogramos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA21, OA22 = "MA03 OA 21", "MA03 OA 22"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 21
register(
    OA21, 1,
    materials="Lápiz, regla y una cuerda o lana. Todas las medidas de los lados están escritas en los ejercicios.",
    use="Aprenderé qué es el perímetro y cómo se calcula sumando los lados. Sirve para saber cuánta cinta, lana o malla se necesita para rodear algo.",
    prior=["Sé medir con regla en centímetros.", "Sé sumar números hasta 100."],
    explain=[
        "El perímetro es el largo del contorno de una figura. Es la distancia que recorres si caminas por todo el borde y vuelves al punto de partida. Para calcularlo, mides cada lado y sumas todas las medidas.",
        "Una figura regular tiene todos sus lados y todas sus esquinas iguales, como un cuadrado. Una figura irregular tiene lados de distintos largos. En las dos, el perímetro es la suma de todos los lados. Por ejemplo, un triángulo con lados de 3 cm, 4 cm y 5 cm tiene perímetro 3 + 4 + 5 = 12 cm.",
        "El perímetro se escribe con una unidad de largo, como centímetros (cm) o metros (m). Para rodear un cuaderno sirven los centímetros. Para rodear una cancha, los metros.",
    ],
    vocab=[("perímetro", "largo del contorno de una figura; suma de todos sus lados"), ("lado", "borde recto de una figura"), ("figura regular", "figura con todos sus lados y esquinas iguales"), ("figura irregular", "figura con lados de distinto largo"), ("contorno", "línea que rodea una figura")],
    worked=[
        {"title": "Perímetro de una figura irregular", "problem": "Una figura tiene lados de 4 cm, 6 cm, 3 cm, 5 cm y 2 cm. ¿Cuál es su perímetro?", "steps": ["Escribo todos los lados: 4, 6, 3, 5 y 2.", "Los sumo: 4 + 6 = 10; 10 + 3 = 13; 13 + 5 = 18; 18 + 2 = 20."], "answer": "20 cm"},
        {"title": "Perímetro de una figura regular", "problem": "Un pentágono regular tiene 5 lados de 2 cm cada uno. ¿Cuál es su perímetro?", "steps": ["Los 5 lados miden lo mismo: 2 cm.", "Sumo: 2 + 2 + 2 + 2 + 2 = 10."], "answer": "10 cm"},
    ],
    mistakes=[
        {"wrong": "Sumar sólo tres lados de una figura de cuatro lados.", "why": "Se olvida uno de los lados.", "fix": "Marca cada lado con un punto al sumarlo y cuenta cuántos sumaste."},
        {"wrong": "Escribir el perímetro sin unidad.", "why": "Se olvida que es una medida de largo.", "fix": "Escribe siempre cm o m junto al resultado."},
    ],
    tiers={
        "recovery": [
            arith("Un triángulo tiene lados de 3 cm, 4 cm y 5 cm. ¿Cuál es su perímetro en cm?", "3+4+5", "Se suman los tres lados."),
            ex("Caminas alrededor de una mesa. ¿Qué medida recorres: el perímetro o el espacio que ocupa la mesa?", "El perímetro", "El perímetro es el largo del contorno."),
            arith("Un pentágono regular tiene 5 lados de 2 cm. ¿Cuál es su perímetro en cm?", "2+2+2+2+2", "Los cinco lados miden lo mismo y se suman."),
        ],
        "understand": [
            ex("¿Qué se suma para hallar el perímetro de una figura?", "Todos sus lados", "El perímetro es el largo de todo el contorno."),
            arith("Una figura irregular tiene lados de 4 cm, 6 cm, 3 cm, 5 cm y 2 cm. ¿Cuál es su perímetro en cm?", "4+6+3+5+2", "Se suman los cinco lados."),
            ex("Quieres medir el contorno de una cancha de fútbol. ¿Usarías cm o m?", "Metros (m)", "La cancha es muy grande para medirla en centímetros."),
        ],
        "apply": [
            arith("Un marco tiene lados de 20 cm, 15 cm, 20 cm y 15 cm. ¿Cuánta lana, en cm, se necesita para rodearlo?", "20+15+20+15", "Se suman los cuatro lados."),
            arith("Un jardín irregular tiene lados de 8 m, 5 m, 3 m, 4 m y 6 m. ¿Cuántos metros de cerco necesita?", "8+5+3+4+6", "El cerco rodea todo el contorno."),
            arith("Un triángulo tiene sus tres lados iguales de 9 cm. ¿Cuál es su perímetro en cm?", "9+9+9", "Los tres lados miden lo mismo."),
        ],
        "reason": [
            ex("Sofía sumó sólo 5 cm, 6 cm y 7 cm de una figura con lados de 5 cm, 6 cm, 7 cm y 8 cm, y dijo que el perímetro es 18 cm. ¿Qué error hizo y cuál es el perímetro?", "Olvidó el lado de 8 cm; el perímetro es 26 cm", "Faltaba un lado: 5 + 6 + 7 + 8 = 26.", calc="5+6+7+8"),
            ex("Juan dice que un rectángulo de 6 cm por 4 cm tiene perímetro 10 cm porque sumó 6 + 4. ¿Qué le falta?", "Sumar los otros dos lados; el perímetro es 20 cm", "Un rectángulo tiene cuatro lados: 6 + 4 + 6 + 4 = 20.", calc="6+4+6+4"),
        ],
        "challenge": [
            arith("Un triángulo tiene perímetro 24 cm. Dos de sus lados miden 8 cm y 9 cm. ¿Cuánto mide el tercer lado en cm?", "24-8-9", "Al perímetro se le quitan los dos lados conocidos."),
            arith("Un cuadrilátero tiene perímetro 30 cm. Tres de sus lados miden 7 cm, 8 cm y 9 cm. ¿Cuánto mide el cuarto lado en cm?", "30-7-8-9", "Al perímetro se le quitan los tres lados conocidos."),
        ],
    },
    context=[arith("Quieres poner una cinta alrededor de una caja de base rectangular, con lados de 12 cm, 9 cm, 12 cm y 9 cm. ¿Cuántos cm de cinta necesitas?", "12+9+12+9", "La cinta rodea los cuatro lados de la base.")],
    selfcheck=[
        ex("En Matemática, ¿qué es el perímetro de una figura?", "El largo del contorno de una figura", "Es lo que mide el borde que rodea la figura."),
        arith("Un triángulo tiene lados de 5 cm, 5 cm y 5 cm. ¿Cuál es su perímetro en cm?", "5+5+5", "Se suman los tres lados."),
        ex("Un cuadrado tiene sus 4 lados iguales. ¿Es una figura regular o irregular?", "Regular", "Todos sus lados miden lo mismo."),
    ],
    open_task=task(
        "Mide con la regla el contorno de la tapa de un cuaderno, lado por lado, y escribe las cuatro medidas. Suma y escribe el perímetro con su unidad. Si no tienes cuaderno, usa un rectángulo de 21 cm por 15 cm.",
        "Cuaderno de 21 cm, 15 cm, 21 cm y 15 cm. Perímetro: 21 + 15 + 21 + 15 = 72 cm.",
        ["mide los cuatro lados con la regla", "suma todos los lados", "escribe la unidad cm", "no omite ningún lado"],
        ["cuatro medidas escritas", "suma", "resultado con unidad"],
        ["sumar menos de cuatro lados", "escribir el resultado sin unidad"],
        "Pide marcar cada lado con un punto al sumarlo. Reconoce que revise que sumó todos los lados.",
    ),
    reinforce="Mide con una cuerda el contorno de un plato y luego estírala sobre una regla. Anota cuántos cm mide.",
    extend="Dibuja una figura irregular de cinco lados con medidas que tú elijas y calcula su perímetro. Escribe las cinco medidas.",
)

register(
    OA21, 2,
    materials="Lápiz y papel cuadriculado. En cada ejercicio se indica cuántos cuadraditos tiene cada figura. El lado de cada cuadradito mide 1 cm.",
    use="Aprenderé a calcular el perímetro de figuras en una cuadrícula contando los lados de los cuadraditos. Sirve para medir figuras dibujadas sin regla.",
    prior=["Sé que el perímetro es el largo del contorno.", "Sé sumar números hasta 100."],
    explain=[
        "En una hoja cuadriculada, cada cuadradito tiene lados de 1 cm. Para hallar el perímetro de una figura, cuentas cuántos lados de cuadradito forman su contorno. Cada lado de cuadradito vale 1 cm.",
        "Un cuadradito solo tiene 4 lados, así que su perímetro es 4 cm. Un rectángulo de 3 cuadraditos de largo y 1 de alto tiene 3 + 1 + 3 + 1 = 8 cm de perímetro. Sólo cuentas el borde de afuera.",
        "No confundas perímetro con la cantidad de cuadraditos. Los cuadraditos que están adentro no se cuentan. Perímetro es el contorno. La cantidad de cuadraditos mide el espacio de adentro, que es otra cosa.",
    ],
    vocab=[("cuadrícula", "hoja con cuadraditos iguales"), ("lado de cuadradito", "borde de un cuadradito; mide 1 cm"), ("contorno", "borde de afuera de la figura"), ("unidad", "medida que se repite, aquí el cm"), ("superficie", "espacio de adentro de la figura; no es el perímetro")],
    worked=[
        {"title": "Rectángulo en la cuadrícula", "problem": "Un rectángulo mide 4 cuadraditos de largo y 2 de alto. ¿Cuál es su perímetro?", "steps": ["El contorno tiene 4 + 2 + 4 + 2 lados de cuadradito.", "4 + 2 + 4 + 2 = 12."], "answer": "12 cm"},
        {"title": "Figura en L", "problem": "Una figura en L tiene estos lados, uno tras otro: 5, 2, 2, 2, 3 y 4 cuadraditos. ¿Cuál es su perímetro?", "steps": ["Escribo los seis lados en orden: 5, 2, 2, 2, 3 y 4.", "Sumo de a uno: 5 + 2 = 7; 7 + 2 = 9; 9 + 2 = 11; 11 + 3 = 14; 14 + 4 = 18."], "answer": "18 cm"},
    ],
    mistakes=[
        {"wrong": "Contar los cuadraditos de adentro y decir que ese es el perímetro.", "why": "Se confunde el contorno con el espacio de adentro.", "fix": "Recorre sólo el borde de afuera y cuenta los lados de cuadradito."},
        {"wrong": "Contar una esquina dos veces.", "why": "Se cuenta el punto en que se juntan dos lados como si fuera un lado.", "fix": "Cuenta lados de cuadradito, no las esquinas."},
    ],
    tiers={
        "recovery": [
            ex("Una figura es un solo cuadradito. ¿Cuál es su perímetro en cm?", "4 cm", "Un cuadradito tiene 4 lados de 1 cm."),
            arith("Un rectángulo mide 3 cuadraditos de largo y 1 de alto. ¿Cuál es su perímetro en cm?", "3+1+3+1", "Se suman los cuatro lados del rectángulo."),
            ex("Cada lado de cuadradito mide 1 cm. Recorres 7 lados de cuadradito. ¿Cuántos cm recorres?", "7 cm", "7 lados de 1 cm suman 7 cm.", calc="7*1"),
        ],
        "understand": [
            arith("Un rectángulo mide 4 cuadraditos de largo y 2 de alto. ¿Cuál es su perímetro en cm?", "4+2+4+2", "Se suman los cuatro lados del rectángulo."),
            ex("Dos cuadraditos están pegados formando un rectángulo. ¿Cuántos lados de cuadradito tiene su contorno?", "6", "Hay 2 + 1 + 2 + 1 lados de cuadradito en el borde.", calc="2+1+2+1"),
            ex("Tres cuadraditos forman una figura en L: dos en una fila y uno encima del primero. ¿Cuál es su perímetro en cm?", "8 cm", "Sus lados son 2, 1, 1, 1, 1 y 2: la suma es 8.", calc="2+1+1+1+1+2"),
        ],
        "apply": [
            arith("Un cuadrado mide 5 cuadraditos de lado. ¿Cuál es su perímetro en cm?", "5+5+5+5", "Se suman los cuatro lados iguales."),
            arith("Otra figura en L tiene estos lados, uno tras otro: 6, 3, 3, 2, 3 y 5 cuadraditos. ¿Cuál es su perímetro en cm?", "6+3+3+2+3+5", "Se suman todos los lados del contorno."),
            arith("Un rectángulo mide 6 cuadraditos de largo y 2 de alto. ¿Cuál es su perímetro en cm?", "6+2+6+2", "Se suman los cuatro lados del rectángulo."),
        ],
        "reason": [
            ex("Pía contó los 6 cuadraditos de un rectángulo de 3 por 2 y dijo que su perímetro es 6 cm. ¿Qué hizo mal y cuál es el perímetro?", "Contó los cuadraditos de adentro; el perímetro es 10 cm", "El contorno es 3 + 2 + 3 + 2 = 10.", calc="3+2+3+2"),
            ex("Un cuadrado de 2 por 2 cuadraditos y una barra de 4 por 1 tienen 4 cuadraditos cada uno. ¿Tienen el mismo perímetro?", "No; 8 cm y 10 cm", "El cuadrado tiene 2+2+2+2 = 8 y la barra 4+1+4+1 = 10."),
        ],
        "challenge": [
            ex("Con 4 cuadraditos pegados puedes formar un cuadrado de 2 por 2 o una barra de 4 por 1. ¿Cuál tiene el menor perímetro y cuánto es?", "El cuadrado de 2 por 2; 8 cm", "El cuadrado mide 8 cm y la barra 10 cm."),
            ex("Con 6 cuadraditos puedes formar un rectángulo de 6 por 1 o uno de 3 por 2. ¿Cuál tiene menor perímetro y cuánto es?", "El de 3 por 2; 10 cm", "6+1+6+1 = 14 y 3+2+3+2 = 10."),
        ],
    },
    context=[arith("Quieres rodear con lana un parche de un huerto dibujado en tu cuaderno. Es un rectángulo de 7 cuadraditos de largo y 3 de alto. ¿Cuántos cm de lana necesitas?", "7+3+7+3", "La lana rodea los cuatro lados del rectángulo.")],
    selfcheck=[
        ex("Cada lado de cuadradito mide 1 cm. ¿Cuánto mide el perímetro de un cuadrado de 3 cuadraditos de lado?", "12 cm", "3 + 3 + 3 + 3 = 12.", calc="3+3+3+3"),
        ex("¿Se cuentan los cuadraditos de adentro para hallar el perímetro?", "No", "El perímetro es sólo el contorno."),
        arith("Un rectángulo mide 5 cuadraditos de largo y 1 de alto. ¿Cuál es su perímetro en cm?", "5+1+5+1", "Se suman los cuatro lados."),
    ],
    open_task=task(
        "En una hoja cuadriculada dibuja un rectángulo de 5 cuadraditos de largo y 3 de alto, y una figura en L con lados de 4, 1, 2, 2, 2 y 3 cuadraditos (recorre el contorno en ese orden). Calcula el perímetro de las dos figuras.",
        "Rectángulo: 5 + 3 + 5 + 3 = 16 cm. Figura en L: 4 + 1 + 2 + 2 + 2 + 3 = 14 cm.",
        ["dibuja las dos figuras", "suma los lados del contorno de cada una", "escribe cm", "no cuenta cuadraditos de adentro"],
        ["dibujos en la cuadrícula", "sumas escritas", "resultados con unidad"],
        ["contar los cuadraditos de adentro", "olvidar un lado"],
        "Pide pintar el contorno de cada figura con un color. Reconoce que sume sólo los lados pintados.",
    ),
    reinforce="Dibuja en una hoja cuadriculada un cuadrado de 4 por 4 y pinta su borde. Cuenta los lados de cuadradito.",
    extend="Dibuja dos figuras diferentes con 6 cuadraditos cada una y compara sus perímetros.",
)

register(
    OA21, 3,
    materials="Lápiz y papel. Las medidas de los lados están escritas en cada ejercicio.",
    use="Aprenderé a calcular el perímetro de un cuadrado y de un rectángulo sin medir los cuatro lados. Sirve para ahorrar pasos al medir.",
    prior=["Sé que el perímetro es la suma de los lados.", "Sé las tablas de multiplicar del 2 y del 4."],
    explain=[
        "Un cuadrado tiene sus 4 lados iguales. Por eso su perímetro es el lado multiplicado por 4. Si el lado mide 7 cm, el perímetro es 7 × 4 = 28 cm.",
        "Un rectángulo tiene dos lados largos iguales y dos lados cortos iguales. Entonces sólo necesitas medir el largo y el ancho. El perímetro es largo + ancho + largo + ancho, o también el doble de largo más el doble de ancho. Para un rectángulo de 9 cm por 4 cm: 9 + 4 + 9 + 4 = 26 cm.",
        "Cuando falta un dato, puedes usar lo que sabes. Si un rectángulo mide 8 cm de largo, el lado de enfrente también mide 8 cm. Y no confundas el perímetro con multiplicar largo por ancho: eso mide otra cosa, el espacio de adentro.",
    ],
    vocab=[("largo", "lado más extenso de un rectángulo"), ("ancho", "lado menos extenso de un rectángulo"), ("lados opuestos", "lados que se enfrentan y miden lo mismo"), ("cuadrado", "4 lados iguales y esquinas rectas"), ("rectángulo", "2 lados largos iguales y 2 lados cortos iguales")],
    worked=[
        {"title": "Perímetro de un cuadrado", "problem": "Un cuadrado tiene 7 cm de lado. ¿Cuál es su perímetro?", "steps": ["Sus 4 lados miden 7 cm.", "7 × 4 = 28."], "answer": "28 cm"},
        {"title": "Perímetro de un rectángulo", "problem": "Un rectángulo mide 9 cm de largo y 4 cm de ancho. ¿Cuál es su perímetro?", "steps": ["Los lados son 9, 4, 9 y 4.", "9 + 4 + 9 + 4 = 26."], "answer": "26 cm"},
    ],
    mistakes=[
        {"wrong": "Calcular el perímetro de un rectángulo de 8 cm por 3 cm como 8 × 3 = 24.", "why": "Se multiplica largo por ancho, que mide el espacio de adentro.", "fix": "Suma los cuatro lados: 8 + 3 + 8 + 3 = 22 cm."},
        {"wrong": "Sumar sólo el largo y el ancho de un rectángulo.", "why": "Se olvidan los lados de enfrente.", "fix": "Un rectángulo tiene 4 lados: suma largo, ancho, largo y ancho."},
    ],
    tiers={
        "recovery": [
            arith("Un cuadrado tiene 3 cm de lado. ¿Cuál es su perímetro en cm?", "3*4", "El perímetro es el lado por 4."),
            arith("Un rectángulo mide 5 cm de largo y 2 cm de ancho. ¿Cuál es su perímetro en cm?", "5+2+5+2", "Se suman los cuatro lados."),
            ex("Un rectángulo tiene un lado largo de 8 cm. ¿Cuánto mide el lado largo de enfrente?", "8 cm", "Los lados de enfrente miden lo mismo."),
        ],
        "understand": [
            arith("Un cuadrado tiene 8 cm de lado. ¿Cuál es su perímetro en cm?", "8*4", "Los cuatro lados miden lo mismo."),
            arith("Un rectángulo mide 12 cm de largo y 5 cm de ancho. ¿Cuál es su perímetro en cm?", "12+5+12+5", "Se suman los cuatro lados."),
            ex("Explica con tus palabras cómo se halla el perímetro de un rectángulo si sabes su largo y su ancho.", "Se suman largo, ancho, largo y ancho; o se suma largo más ancho y se duplica", "Un rectángulo tiene dos lados largos y dos cortos."),
        ],
        "apply": [
            arith("Una huerta cuadrada mide 10 m de lado. ¿Cuántos metros de cerco rodean la huerta?", "10*4", "El cerco rodea los cuatro lados iguales."),
            arith("Una cartulina rectangular mide 30 cm de largo y 20 cm de ancho. ¿Cuántos cm de cinta se necesitan para el borde?", "30+20+30+20", "La cinta rodea los cuatro lados."),
            arith("Un marco cuadrado mide 15 cm de lado. ¿Cuántos cm de madera hacen falta para los 4 lados?", "15*4", "Los cuatro lados miden lo mismo."),
        ],
        "reason": [
            ex("Tomás calcula el perímetro de un rectángulo de 7 cm por 4 cm como 7 × 4 = 28 cm. ¿Qué hizo mal y cuál es el perímetro?", "Multiplicó largo por ancho; el perímetro es 22 cm", "Hay que sumar los cuatro lados: 7 + 4 + 7 + 4 = 22.", calc="7+4+7+4"),
            ex("Ana dice que un cuadrado de perímetro 20 cm tiene un lado de 4 cm. ¿Es correcto?", "No; el lado es 5 cm, porque 5 × 4 = 20", "El lado multiplicado por 4 debe dar 20.", calc="5*4"),
        ],
        "challenge": [
            ex("Un rectángulo tiene perímetro 24 cm y su largo es 8 cm. ¿Cuánto mide su ancho?", "4 cm", "Los dos largos suman 16 cm; quedan 24 − 16 = 8 cm para los dos anchos, o sea 4 cm cada uno."),
            ex("Un cuadrado y un rectángulo de 6 cm de largo por 2 cm de ancho tienen el mismo perímetro. ¿Cuánto mide el lado del cuadrado?", "4 cm", "El rectángulo mide 6+2+6+2 = 16 y 4 × 4 = 16."),
        ],
    },
    context=[arith("Quieres poner una cinta alrededor de un cuadro cuadrado de 25 cm de lado. ¿Cuántos cm de cinta necesitas?", "25*4", "La cinta rodea los cuatro lados iguales.")],
    selfcheck=[
        arith("Un cuadrado tiene 6 cm de lado. ¿Cuál es su perímetro en cm?", "6*4", "El perímetro es el lado por 4."),
        arith("Un rectángulo mide 10 cm de largo y 5 cm de ancho. ¿Cuál es su perímetro en cm?", "10+5+10+5", "Se suman los cuatro lados."),
        ex("¿Cuántos lados iguales tiene un cuadrado?", "4", "Los cuatro lados de un cuadrado miden lo mismo."),
    ],
    open_task=task(
        "Elige uno de estos dos objetos: una tarjeta cuadrada de 12 cm de lado o una hoja rectangular de 18 cm por 12 cm. Calcula cuántos cm de cinta necesitas para rodear su borde. Escribe cómo lo calculaste y explica por qué no hace falta medir los cuatro lados.",
        "Tarjeta cuadrada de 12 cm: 12 × 4 = 48 cm. No hace falta medir los cuatro lados porque son iguales.",
        ["elige un objeto", "usa lado × 4 o largo + ancho + largo + ancho", "escribe cm", "explica por qué no mide los cuatro lados"],
        ["cálculo escrito", "resultado con unidad", "explicación"],
        ["multiplicar largo por ancho", "sumar sólo dos lados del rectángulo"],
        "Pide decir cuántos lados tiene la figura y cuáles son iguales. Reconoce que use esa idea para calcular.",
    ),
    reinforce="Busca un objeto cuadrado y otro rectangular en tu casa, mide un lado de cada uno y calcula su perímetro.",
    extend="Busca dos rectángulos distintos con perímetro 20 cm y escribe el largo y el ancho de cada uno.",
)

register(
    OA21, 4,
    materials="Lápiz y papel cuadriculado. Las medidas están escritas en los ejercicios, en cm.",
    use="Aprenderé a diseñar y comparar figuras que tienen el mismo perímetro aunque sean distintas. Sirve para decidir cómo usar un largo fijo de cinta, lana o malla.",
    prior=["Sé calcular el perímetro de cuadrados y rectángulos.", "Sé sumar y restar números hasta 100."],
    explain=[
        "Dos figuras diferentes pueden tener el mismo perímetro. Por ejemplo, un rectángulo de 5 cm por 1 cm tiene perímetro 5 + 1 + 5 + 1 = 12 cm. Un cuadrado de 3 cm de lado también tiene 12 cm.",
        "Si tienes una cinta de un largo fijo, puedes armar muchos rectángulos con ella. Para un perímetro de 12 cm, la mitad es 6 cm; entonces el largo y el ancho deben sumar 6. Pueden ser 5 y 1, 4 y 2, o 3 y 3.",
        "Para decidir si dos figuras tienen el mismo perímetro, calcula cada uno y compara. Misma cinta no significa misma forma, y no es lo mismo que tengan el mismo espacio de adentro.",
    ],
    vocab=[("mismo perímetro", "el contorno de las dos figuras mide lo mismo"), ("mitad del perímetro", "lo que suman largo y ancho de un rectángulo"), ("diseño", "dibujo o plan de una figura"), ("comparar", "decir si dos medidas son iguales o cuál es mayor"), ("forma", "cómo se ve una figura")],
    worked=[
        {"title": "Mismo perímetro, distinta figura", "problem": "Un rectángulo mide 5 cm por 1 cm. Un cuadrado mide 3 cm de lado. ¿Tienen el mismo perímetro?", "steps": ["Rectángulo: 5 + 1 + 5 + 1 = 12.", "Cuadrado: 3 × 4 = 12.", "Los dos dan 12."], "answer": "Sí, los dos tienen perímetro 12 cm"},
        {"title": "Buscar el ancho", "problem": "Tienes 20 cm de cinta para rodear un rectángulo de 7 cm de largo. ¿Cuánto debe medir el ancho?", "steps": ["La mitad de la cinta es 10 cm: largo + ancho = 10.", "10 − 7 = 3."], "answer": "El ancho es 3 cm"},
    ],
    mistakes=[
        {"wrong": "Pensar que dos figuras con el mismo perímetro son iguales.", "why": "Se mira sólo un dato de la figura.", "fix": "Dibuja las dos: pueden tener lados distintos y el mismo perímetro."},
        {"wrong": "Usar la cinta completa como suma de largo y ancho.", "why": "Se olvida que el perímetro suma dos largos y dos anchos.", "fix": "Divide el perímetro por la mitad: esa mitad es largo + ancho."},
    ],
    tiers={
        "recovery": [
            arith("Un rectángulo mide 5 cm por 1 cm. ¿Cuál es su perímetro en cm?", "5+1+5+1", "Se suman los cuatro lados."),
            arith("Un cuadrado mide 3 cm de lado. ¿Cuál es su perímetro en cm?", "3*4", "El perímetro es el lado por 4."),
            ex("El rectángulo de 5 cm por 1 cm y el cuadrado de 3 cm de lado, ¿tienen el mismo perímetro?", "Sí", "Los dos tienen perímetro 12 cm."),
        ],
        "understand": [
            ex("Un rectángulo tiene perímetro 10 cm y su largo es 4 cm. ¿Cuánto mide el ancho?", "1 cm", "4 + 1 = 5, la mitad de 10; el ancho es 1 cm.", calc="5-4"),
            arith("Un rectángulo mide 3 cm de largo y 2 cm de ancho. ¿Cuál es su perímetro en cm?", "3+2+3+2", "Se suman los cuatro lados."),
            ex("El marco A mide 6 cm por 2 cm y el marco B mide 5 cm por 3 cm. ¿Tienen el mismo perímetro?", "Sí; los dos tienen 16 cm", "A: 6+2+6+2 = 16 y B: 5+3+5+3 = 16.", calc="6+2+6+2"),
        ],
        "apply": [
            ex("Tienes 20 m de malla para un cerco rectangular. ¿Cuál de estos rectángulos usa justo los 20 m: 7 m por 3 m, 6 m por 5 m o 9 m por 2 m?", "El de 7 m por 3 m", "7+3+7+3 = 20; los otros dan 22."),
            arith("Un rectángulo mide 9 cm de largo y 3 cm de ancho. ¿Cuántos cm de lana se necesitan para su borde?", "9+3+9+3", "La lana rodea los cuatro lados."),
            ex("Tienes 24 cm de cinta para rodear un rectángulo de 8 cm de largo, usándola toda. ¿Qué ancho debe tener?", "4 cm", "La mitad de 24 es 12 y 12 − 8 = 4.", calc="12-8"),
        ],
        "reason": [
            ex("Pedro dice que dos figuras con el mismo perímetro son siempre iguales. Un rectángulo de 6 cm por 2 cm y un cuadrado de 4 cm de lado, ¿confirman o contradicen a Pedro?", "Lo contradicen; los dos tienen 16 cm y no son iguales", "6+2+6+2 = 16 y 4 × 4 = 16, pero las formas son distintas.", calc="6+2+6+2"),
            ex("Ema dice que el rectángulo de 6 cm por 1 cm tiene el mismo perímetro que el de 4 cm por 3 cm. ¿Tiene razón?", "Sí; los dos tienen 14 cm", "6+1+6+1 = 14 y 4+3+4+3 = 14.", calc="6+1+6+1"),
        ],
        "challenge": [
            ex("Con 14 cm de cinta se arman rectángulos con medidas enteras en cm. Un rectángulo de 6 por 1 y uno de 1 por 6 cuentan como el mismo. ¿Cuántos rectángulos distintos hay?", "3 (6 por 1, 5 por 2 y 4 por 3)", "La mitad es 7: 6+1, 5+2 y 4+3 suman 7."),
            ex("Un cuadrado y un rectángulo de 6 cm de largo tienen el mismo perímetro de 16 cm. ¿Cuánto mide el lado del cuadrado y el ancho del rectángulo?", "Lado 4 cm y ancho 2 cm", "4 × 4 = 16, y 6 + 2 = 8, la mitad de 16."),
        ],
    },
    context=[ex("Dos amigos cercan huertas: la huerta de Ana mide 6 m por 4 m y la de Beto 7 m por 3 m. ¿Quién necesita más malla?", "Ninguno; los dos necesitan 20 m", "6+4+6+4 = 20 y 7+3+7+3 = 20.", calc="6+4+6+4")],
    selfcheck=[
        arith("Un rectángulo mide 8 cm por 2 cm. ¿Cuál es su perímetro en cm?", "8+2+8+2", "Se suman los cuatro lados."),
        ex("Un cuadrado de 4 cm de lado y un rectángulo de 5 cm por 3 cm, ¿tienen el mismo perímetro?", "Sí; los dos tienen 16 cm", "4 × 4 = 16 y 5+3+5+3 = 16.", calc="4*4"),
        ex("Si dos figuras tienen el mismo perímetro, ¿tienen que ser iguales?", "No", "Pueden tener lados distintos y la misma suma."),
    ],
    open_task=task(
        "Tienes una cinta de 16 cm. Dibuja en papel cuadriculado dos figuras distintas que usen justo toda la cinta: un cuadrado y un rectángulo que no sea cuadrado. Escribe las medidas y comprueba con una suma.",
        "Cuadrado de 4 cm de lado: 4 × 4 = 16 cm. Rectángulo de 6 cm por 2 cm: 6 + 2 + 6 + 2 = 16 cm. Los dos usan toda la cinta, pero tienen formas distintas.",
        ["dibuja un cuadrado de lado 4", "dibuja un rectángulo con largo + ancho = 8", "comprueba cada perímetro", "escribe cm"],
        ["dos figuras dibujadas", "sumas de comprobación", "medidas escritas"],
        ["usar la cinta entera como largo más ancho", "no comprobar el perímetro"],
        "Pide comprobar sumando en voz alta los cuatro lados. Reconoce que use la mitad de 16 para largo más ancho.",
    ),
    reinforce="Con un cordel de 20 cm arma sobre la mesa un rectángulo y un cuadrado distintos. Mide sus lados.",
    extend="Busca todos los rectángulos de lados enteros con perímetro 18 cm y anota largo y ancho de cada uno.",
)


# ================================================================ OA 22
register(
    OA22, 1,
    materials="Una regla de 30 cm y dos vasos livianos o dos bolsas, para hacer una balanza sencilla con un lápiz (opcional). Los resultados de las balanzas están escritos en los ejercicios.",
    use="Aprenderé a comparar el peso de dos objetos con una balanza. Sirve para saber qué cosa pesa más sin usar números.",
    prior=["Sé que algunas cosas son más pesadas que otras.", "Sé ordenar tres cosas de menos a más."],
    explain=[
        "El peso dice qué tan pesado es un objeto. Una balanza de platillos tiene dos platillos. Pones un objeto en cada platillo. El platillo que baja tiene el objeto más pesado. El platillo que sube tiene el objeto más liviano.",
        "Si los dos platillos quedan a la misma altura, los objetos pesan lo mismo. Con la balanza puedes ordenar varios objetos: los comparas de a dos y ordenas del más liviano al más pesado.",
        "El tamaño no dice cuánto pesa algo. Un globo grande lleno de aire pesa muy poco. Una piedra del tamaño de un puño pesa más. Por eso hay que comparar con la balanza o con las manos, y no sólo mirar.",
    ],
    vocab=[("peso", "qué tan pesado es un objeto"), ("balanza de platillos", "instrumento con dos platillos para comparar pesos"), ("más pesado", "el objeto cuyo platillo baja"), ("más liviano", "el objeto cuyo platillo sube"), ("equilibrio", "los dos platillos a la misma altura")],
    worked=[
        {"title": "Leer una balanza", "problem": "En una balanza, el platillo del libro baja y el platillo del cuaderno sube. ¿Cuál pesa más?", "steps": ["El platillo que baja tiene el objeto más pesado.", "Baja el del libro."], "answer": "El libro pesa más"},
        {"title": "Ordenar tres objetos", "problem": "La mochila pesa más que el estuche, y el estuche pesa más que la goma. Ordena de más liviano a más pesado.", "steps": ["El más liviano es el que pesa menos que los otros: la goma.", "Sigue el estuche.", "El más pesado es la mochila."], "answer": "Goma, estuche, mochila"},
    ],
    mistakes=[
        {"wrong": "Decir que el objeto más grande es siempre el más pesado.", "why": "Se usa el tamaño en vez del peso.", "fix": "Compara con la balanza o con las manos."},
        {"wrong": "Creer que el platillo que sube tiene el objeto más pesado.", "why": "Se confunde subir con pesar más.", "fix": "Recuerda: lo más pesado baja."},
    ],
    tiers={
        "recovery": [
            ex("En una balanza, el platillo de la manzana baja y el de la naranja sube. ¿Cuál pesa más?", "La manzana", "El platillo que baja tiene el objeto más pesado."),
            ex("Los dos platillos de una balanza quedan a la misma altura. ¿Cómo pesan los objetos?", "Pesan lo mismo", "En equilibrio, los pesos son iguales."),
            ex("Un globo grande inflado con aire y una piedra del tamaño de un puño. ¿Cuál suele pesar más?", "La piedra", "El globo, aunque grande, tiene casi sólo aire."),
        ],
        "understand": [
            ex("En una balanza, el libro baja frente al cuaderno y el cuaderno baja frente al lápiz. Ordena de más pesado a más liviano.", "Libro, cuaderno, lápiz", "Cada uno pesa más que el siguiente."),
            ex("¿Por qué no se puede saber cuánto pesa algo sólo por su tamaño?", "Porque depende de lo que tiene adentro o del material", "Un objeto grande puede ser liviano y uno pequeño pesado."),
            ex("A pesa más que B, y B pesa más que C. ¿Cuál pesa menos de los tres?", "C", "C es el más liviano de la cadena."),
        ],
        "apply": [
            ex("La sandía pesa más que el melón, y el melón pesa más que la manzana. Ordena de más liviano a más pesado.", "Manzana, melón, sandía", "La manzana es la más liviana y la sandía la más pesada."),
            ex("En un platillo de una balanza hay dos bolsas de arroz y en el otro una caja. El platillo de las bolsas sube. ¿Qué pesa más: las dos bolsas juntas o la caja?", "La caja", "Baja el platillo que tiene el objeto más pesado."),
            ex("Tres tazas iguales en un platillo equilibran una olla en el otro. ¿Una taza pesa más o menos que la olla?", "Menos", "La olla pesa lo mismo que tres tazas, así que una taza es sólo una parte."),
        ],
        "reason": [
            ex("Dani dice que una bolsa grande de algodón pesa más que una piedra del tamaño de un puño porque es más grande. ¿Siempre es cierto?", "No; el tamaño no dice el peso", "El algodón es muy liviano para su tamaño."),
            ex("Una balanza queda equilibrada con A y B. Otra queda equilibrada con B y C. ¿Cómo pesan A y C?", "Pesan lo mismo", "Si A pesa lo mismo que B y B lo mismo que C, A y C pesan lo mismo."),
        ],
        "challenge": [
            ex("El objeto A baja frente a B, y B baja frente a C. ¿Hace falta comparar A con C para saber cuál pesa más de los tres?", "No; A pesa más", "A pesa más que B y B más que C, por lo tanto A pesa más que C."),
            ex("En una balanza, 4 cubos iguales equilibran un bloque. Pones 2 de esos cubos en un platillo y el bloque en el otro. ¿Qué platillo baja?", "El del bloque", "Dos cubos pesan menos que cuatro cubos, que son lo que pesa el bloque."),
        ],
    },
    context=[ex("Haces una balanza con una regla, un lápiz y dos vasos. El vaso con la bolsa de pan A baja y el vaso con la bolsa B sube. ¿Qué bolsa pesa más?", "La bolsa A", "Baja el lado de lo más pesado.")],
    selfcheck=[
        ex("¿Qué platillo baja en una balanza: el del objeto más pesado o el del más liviano?", "El del más pesado", "Lo más pesado baja."),
        ex("Si los dos platillos quedan a la misma altura, ¿cuál objeto pesa más?", "Ninguno; pesan lo mismo", "Equilibrio es peso igual."),
        ex("Un clavo y una pluma de pájaro, ¿cuál suele pesar más?", "El clavo", "Una pluma es muy liviana."),
    ],
    open_task=task(
        "Elige tres objetos de tu casa que no se rompan: por ejemplo un libro, una cuchara de madera y una goma. Con tus manos o con una balanza hecha con una regla, un lápiz y dos vasos, ordénalos del más liviano al más pesado. Escribe el orden y cómo lo comprobaste.",
        "Goma, cuchara, libro. Comparé de a dos con la balanza: el libro bajó frente a la cuchara y la cuchara bajó frente a la goma.",
        ["elige tres objetos seguros", "compara de a dos", "ordena del más liviano al más pesado", "explica cómo comprobó"],
        ["lista ordenada", "explicación de las comparaciones"],
        ["ordenar por tamaño", "no comparar de a dos"],
        "Pide decir qué platillo baja cada vez. Reconoce que use la comparación y no el tamaño.",
    ),
    reinforce="Toma dos objetos con una mano cada uno y di cuál sientes más pesado. Compruébalo con una balanza casera.",
    extend="Encuentra un objeto grande que pese poco y uno pequeño que pese mucho. Explica por qué.",
)

register(
    OA22, 2,
    materials="Un clip, y si tienes un paquete de 1 kg de azúcar o de arroz, para sentir cuánto pesa. Los datos de cada ejercicio están escritos.",
    use="Aprenderé a usar referentes para imaginar cuánto pesa un gramo y un kilogramo. Sirve para estimar el peso de objetos de uso diario.",
    prior=["Sé comparar el peso de dos objetos.", "Sé que hay objetos livianos y pesados."],
    explain=[
        "Para medir el peso usamos gramos (g) y kilogramos (kg). El gramo es una unidad pequeña. Un clip pequeño pesa más o menos 1 gramo. El kilogramo es una unidad grande. Un paquete de azúcar o de arroz de 1 kilogramo es un buen referente.",
        "Un referente es un objeto conocido que usas para comparar. Si algo se siente como un clip, pesa unos pocos gramos. Si se siente como un paquete de azúcar, pesa más o menos 1 kg.",
        "Los gramos sirven para cosas livianas, como un lápiz o un clip. Los kilogramos sirven para cosas pesadas, como una sandía o un saco de papas. Un kilogramo pesa mucho más que un gramo.",
    ],
    vocab=[("gramo (g)", "unidad pequeña de peso; un clip pequeño pesa cerca de 1 g"), ("kilogramo (kg)", "unidad grande de peso; un paquete de azúcar de 1 kg"), ("referente", "objeto conocido para comparar y estimar"), ("estimar", "decir un valor aproximado, sin medir exacto"), ("liviano y pesado", "poco o mucho peso")],
    worked=[
        {"title": "Elegir la unidad", "problem": "¿Qué unidad usarías para el peso de una sandía: g o kg?", "steps": ["Una sandía es pesada, mucho más que un paquete pequeño.", "Para cosas pesadas se usan kilogramos."], "answer": "Kilogramos (kg)"},
        {"title": "Usar un referente", "problem": "Supón que un clip pesa 1 g. ¿Cuánto pesan 8 clips iguales?", "steps": ["Cada clip pesa 1 g.", "8 clips pesan 8 × 1 = 8 g."], "answer": "8 g"},
    ],
    mistakes=[
        {"wrong": "Decir que 5 g pesan más que 2 kg porque 5 es mayor que 2.", "why": "Se comparan los números y no las unidades.", "fix": "Un kilogramo es mucho más pesado que un gramo; mira la unidad antes del número."},
        {"wrong": "Estimar que una mochila escolar llena pesa 1 g.", "why": "No se usa un referente.", "fix": "1 g es un clip; una mochila se parece más a varios paquetes de 1 kg."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué unidad usarías para el peso de un clip: gramos o kilogramos?", "Gramos", "Un clip es muy liviano."),
            ex("¿Qué unidad usarías para el peso de una sandía: gramos o kilogramos?", "Kilogramos", "Una sandía es pesada."),
            ex("¿Qué pesa más: 1 g o 1 kg?", "1 kg", "El kilogramo es una unidad mucho más grande."),
        ],
        "understand": [
            ex("Un paquete de azúcar pesa 1 kg. Una bolsa pesa lo mismo que 3 de esos paquetes. ¿Cuántos kg pesa la bolsa?", "3 kg", "3 paquetes de 1 kg pesan 3 kg.", calc="3*1"),
            ex("En Matemática, ¿qué es un referente para estimar el peso?", "Un objeto conocido que se usa para comparar y estimar", "Sirve para imaginar el peso de otros objetos."),
            ex("¿Qué pesa más: un paquete de 1 kg o 10 clips de 1 g cada uno?", "El paquete de 1 kg", "10 clips pesan 10 g y el paquete pesa mucho más."),
        ],
        "apply": [
            arith("Supón que un clip pesa 1 g. ¿Cuántos g pesan 8 clips?", "8*1", "Cada clip pesa 1 g."),
            arith("Una bolsa pesa lo mismo que 4 paquetes de 1 kg. ¿Cuántos kg pesa la bolsa?", "4*1", "Cada paquete pesa 1 kg."),
            ex("¿Qué unidad usarías para el peso de un lápiz: g o kg?", "g", "Un lápiz es liviano."),
        ],
        "reason": [
            ex("Mía dice que 5 g pesan más que 2 kg porque 5 es mayor que 2. ¿Tiene razón?", "No; 2 kg pesan mucho más que 5 g", "El kilogramo es mucho más pesado que el gramo."),
            ex("Beto estima que una mochila llena pesa 1 g. ¿Es razonable?", "No; 1 g es lo que pesa un clip", "Una mochila pesa varios kilogramos."),
        ],
        "challenge": [
            arith("Hay 6 paquetes de 1 kg en una caja y 2 paquetes más en una bolsa. ¿Cuántos kg hay en total?", "6+2", "Cada paquete pesa 1 kg."),
            ex("Un saco de papas pesa 10 kg. ¿Cuántos paquetes de 1 kg pesan lo mismo que el saco?", "10 paquetes", "Cada paquete pesa 1 kg y 10 × 1 = 10.", calc="10*1"),
        ],
    },
    context=[arith("Ana compra 3 bolsas de harina de 1 kg cada una. ¿Cuántos kg de harina lleva?", "3*1", "Cada bolsa pesa 1 kg.")],
    selfcheck=[
        ex("¿Qué unidad es más grande: el gramo o el kilogramo?", "El kilogramo", "Un kilogramo pesa muchísimo más que un gramo."),
        ex("Un clip pesa cerca de 1 g. ¿Cuánto pesan 5 clips?", "5 g", "Cada clip pesa 1 g.", calc="5*1"),
        ex("¿En qué unidad medirías el peso de un saco de papas?", "Kilogramos", "Es una cosa pesada."),
    ],
    open_task=task(
        "Elige tres objetos de tu casa que no se rompan, por ejemplo un lápiz, un libro y un paquete de arroz de 1 kg. Para cada uno, escribe si lo medirías en gramos o en kilogramos y por qué. Compara cada uno con un referente: un clip (1 g) o un paquete de 1 kg.",
        "Lápiz: gramos, es mucho más liviano que un paquete de 1 kg y se parece a unos pocos clips. Paquete de arroz: kilogramos, pesa 1 kg. Libro: gramos o kilogramos, es un poco menos que un paquete de 1 kg.",
        ["elige tres objetos", "decide la unidad", "usa un referente para justificar", "no confunde g con kg"],
        ["lista de objetos con unidad", "frase con el referente"],
        ["usar kg para objetos livianos", "decidir sólo por el número"],
        "Pide sostener cada objeto y compararlo con el referente. Reconoce que justifique con un referente.",
    ),
    reinforce="Compara con las manos un clip y un paquete de 1 kg, y cuenta lo que sientes.",
    extend="Haz una lista de cinco objetos de tu casa y escribe cuáles medirías en gramos y cuáles en kilogramos.",
)

register(
    OA22, 3,
    materials="Lápiz y papel. Las cantidades están escritas en cada ejercicio. Si tienes una bolsa de 1 kg, puedes imaginar que se reparte en partes.",
    use="Aprenderé que 1 kilogramo es igual a 1.000 gramos. Sirve para pasar de una unidad a otra al medir el peso.",
    prior=["Sé que el gramo es pequeño y el kilogramo es grande.", "Sé contar de 100 en 100 hasta 1.000."],
    explain=[
        "Un kilogramo es igual a 1.000 gramos. Se escribe 1 kg = 1.000 g. Imagina una bolsa de 1 kg dividida en 10 paquetes iguales de 100 g. Los 10 paquetes juntos pesan 1.000 g.",
        "Para pasar de kilogramos a gramos, multiplica por 1.000. Por ejemplo, 2 kg son 2 × 1.000 = 2.000 g. Para pasar de gramos a kilogramos, ve cuántos grupos de 1.000 g hay. 3.000 g son 3 kg.",
        "También puedes sumar: 500 g más 500 g son 1.000 g, o sea 1 kg. Si pesas algo que mide 1.500 g, son 1 kg y 500 g. Recuerda siempre escribir la unidad: g o kg.",
    ],
    vocab=[("1 kg = 1.000 g", "equivalencia entre kilogramo y gramos"), ("equivalencia", "dos medidas distintas que valen lo mismo"), ("convertir", "pasar una medida de una unidad a otra"), ("1.000", "mil; diez grupos de cien"), ("gramos sueltos", "gramos que sobran después de formar kilogramos")],
    worked=[
        {"title": "De kilogramos a gramos", "problem": "Una bolsa pesa 2 kg. ¿Cuántos gramos pesa?", "steps": ["1 kg = 1.000 g.", "2 kg son 2 veces 1.000 g: 1.000 + 1.000 = 2.000."], "answer": "2.000 g"},
        {"title": "Sumar medios kilos", "problem": "Hay dos bolsas de 500 g cada una. ¿Cuánto pesan juntas en gramos y en kilogramos?", "steps": ["500 + 500 = 1.000 g.", "1.000 g es 1 kg."], "answer": "1.000 g, o sea 1 kg"},
    ],
    mistakes=[
        {"wrong": "Decir que 1 kg = 100 g.", "why": "Se mezcla con otras unidades que van de 100 en 100.", "fix": "Recuerda que 1 kg = 1.000 g; son 10 paquetes de 100 g."},
        {"wrong": "Escribir 3 kg = 300 g.", "why": "Se agregan dos ceros en vez de tres.", "fix": "Multiplica por 1.000: 3 kg = 3.000 g."},
    ],
    tiers={
        "recovery": [
            ex("1 kg es igual a ¿cuántos gramos?", "1.000 g", "Esa es la equivalencia entre kilogramo y gramo."),
            arith("2 kg son ¿cuántos gramos?", "2*1000", "Cada kilogramo tiene 1.000 g."),
            ex("3.000 g son ¿cuántos kilogramos?", "3 kg", "Hay tres grupos de 1.000 g.", calc="3000//1000"),
        ],
        "understand": [
            ex("¿Qué pesa más: 800 g o 1 kg?", "1 kg", "1 kg son 1.000 g y 1.000 es mayor que 800."),
            ex("¿Cuántos paquetes de 100 g forman 1 kg?", "10", "10 × 100 = 1.000 g.", calc="1000//100"),
            arith("Convierte 5 kg a gramos.", "5*1000", "Cada kilogramo tiene 1.000 g."),
        ],
        "apply": [
            arith("Dos bolsas de 500 g se ponen juntas. ¿Cuántos gramos pesan?", "500+500", "Se suman los pesos de las dos bolsas."),
            arith("Una caja pesa 1 kg y otra pesa 500 g. ¿Cuántos g pesan las dos juntas?", "1000+500", "1 kg son 1.000 g y se suman 500 g."),
            ex("Tienes 4 kg de papas y vendes 1.000 g. ¿Cuántos kg te quedan?", "3 kg", "1.000 g son 1 kg y 4 − 1 = 3.", calc="4-1"),
        ],
        "reason": [
            ex("Pepe dice que 1 kg = 100 g. ¿Qué error comete?", "1 kg son 1.000 g, no 100 g", "El kilogramo tiene mil gramos."),
            ex("Ana dice que 3 kg son 300 g. ¿Cuántos gramos son en realidad?", "3.000 g", "3 × 1.000 = 3.000.", calc="3*1000"),
        ],
        "challenge": [
            arith("Una caja pesa 2 kg y 500 g. ¿Cuántos gramos pesa en total?", "2*1000+500", "2 kg son 2.000 g y se suman 500 g."),
            ex("Mezclas 700 g de harina y 300 g de azúcar. ¿Cuántos kg pesa la mezcla?", "1 kg", "700 + 300 = 1.000 g, que es 1 kg."),
        ],
    },
    context=[ex("Una receta pide 1 kg de harina. En casa hay bolsas de 500 g. ¿Cuántas bolsas necesitas?", "2 bolsas", "Cada bolsa es media parte de 1.000 g: 500 + 500 = 1.000.")],
    selfcheck=[
        ex("¿Cuántos gramos tiene 1 kg?", "1.000", "Un kilogramo equivale a mil gramos."),
        arith("4 kg son ¿cuántos gramos?", "4*1000", "Cada kilogramo tiene 1.000 g."),
        ex("5.000 g son ¿cuántos kg?", "5 kg", "Hay cinco grupos de 1.000 g.", calc="5000//1000"),
    ],
    open_task=task(
        "Usa estas tres medidas de una compra: 2 kg de papas, 1.500 g de harina y 500 g de queso. Escribe las papas y el queso en gramos y la harina en kilogramos y gramos. Luego explica con un dibujo o una frase por qué 1 kg son 1.000 g.",
        "Papas: 2.000 g. Queso: 500 g. Harina: 1 kg y 500 g. 1 kg son 1.000 g porque son 10 paquetes de 100 g.",
        ["convierte kg a g multiplicando por 1.000", "separa 1.500 g en 1 kg y 500 g", "explica la equivalencia", "escribe las unidades"],
        ["tres conversiones", "explicación"],
        ["usar 100 g como equivalencia de 1 kg", "olvidar la unidad"],
        "Pide mostrar con 10 paquetes de 100 g el 1 kg. Reconoce el uso correcto del 1.000.",
    ),
    reinforce="Si tienes un paquete de 1 kg en casa, lee su etiqueta y busca cuántos gramos dice que tiene.",
    extend="Escribe en gramos y en kilogramos y gramos el peso de 2 bolsas de 750 g juntas.",
)

register(
    OA22, 4,
    materials="Lápiz y papel. Los resultados de las balanzas de cocina están escritos en cada ejercicio.",
    use="Aprenderé a estimar el peso y luego compararlo con la medida de una balanza. Sirve para saber si mi cálculo fue razonable.",
    prior=["Sé que 1 kg = 1.000 g.", "Sé usar referentes de 1 g y 1 kg."],
    explain=[
        "Estimar es decir cuánto crees que pesa algo antes de medirlo. Para estimar, comparas con un referente: un clip es 1 g y un paquete de azúcar es 1 kg. Primero estimas y después mides con la balanza.",
        "Las balanzas muestran el peso con un número y una unidad, como 750 g o 2 kg. Lee la unidad antes de anotar. Luego compara tu estimación con la medida y calcula cuánto te equivocaste restando el número menor al mayor.",
        "Una buena estimación se acerca a lo que mide la balanza. Si estimaste 500 g y la balanza marca 650 g, te equivocaste en 150 g. Anota siempre tus mediciones con su unidad para no mezclarlas.",
    ],
    vocab=[("estimación", "valor aproximado que se dice antes de medir"), ("balanza", "instrumento que mide el peso"), ("medición", "valor que entrega el instrumento"), ("diferencia", "cuánto más pesa uno que el otro; se calcula restando"), ("razonable", "cercano a lo que se espera")],
    worked=[
        {"title": "Comparar estimación y medida", "problem": "Estimaste que una bolsa de uvas pesaba 600 g. La balanza marca 1 kg. ¿Cuántos gramos te equivocaste?", "steps": ["Paso 1 kg a gramos: 1.000 g.", "Resto 1.000 − 600 = 400."], "answer": "Te equivocaste en 400 g"},
        {"title": "Peso de uno entre varios", "problem": "Tres manzanas iguales pesan 600 g en total. ¿Cuánto pesa cada una?", "steps": ["Reparto 600 en 3 partes iguales.", "600 ÷ 3 = 200."], "answer": "Cada manzana pesa 200 g"},
    ],
    mistakes=[
        {"wrong": "Anotar la medida de la balanza sin la unidad.", "why": "Se piensa que el número basta.", "fix": "Escribe siempre g o kg junto al número."},
        {"wrong": "Restar 600 − 1 sin pasar a la misma unidad.", "why": "Se mezclan gramos y kilogramos.", "fix": "Pasa 1 kg a 1.000 g antes de restar."},
    ],
    tiers={
        "recovery": [
            ex("La balanza marca 300 g. ¿Cuántos gramos pesa el objeto?", "300 g", "Se lee el número y la unidad."),
            ex("Estimaste 2 kg y la balanza marca 2 kg. ¿Acertaste?", "Sí", "Los dos valores son iguales."),
            ex("¿Qué haces primero: estimar o medir?", "Estimar", "Primero estimas y después compruebas con la balanza."),
        ],
        "understand": [
            ex("Una bolsa pesa lo mismo que 3 paquetes de 1 kg. ¿Cuántos kg estimas que pesa?", "3 kg", "Cada paquete pesa 1 kg.", calc="3*1"),
            arith("Estimaste 500 g y la balanza marca 650 g. ¿Cuántos g te equivocaste?", "650-500", "Se resta el valor menor al mayor."),
            ex("¿Cuál estimación está más cerca de 400 g: 350 g o 800 g?", "350 g", "350 está a 50 g de 400 y 800 está a 400 g."),
        ],
        "apply": [
            arith("Estimaste 800 g de papas. La balanza marca 1 kg. ¿Cuántos gramos te equivocaste?", "1000-800", "1 kg son 1.000 g y se resta."),
            arith("Dos paltas iguales pesan 360 g en total. ¿Cuántos g pesa cada una?", "360//2", "Se reparte el peso total en 3 partes iguales."),
            arith("El lunes se compraron 400 g de pan, el martes 300 g y el miércoles 500 g. ¿Cuántos g se compraron en total?", "400+300+500", "Se suman los tres pesos."),
        ],
        "reason": [
            ex("Rafa mide 1.000 g y lo escribe como 1 g. ¿Qué error hizo?", "Confundió 1.000 g con 1 g; son 1 kg", "1.000 g equivalen a 1 kg."),
            ex("Ana estima que un lápiz pesa 1 kg. ¿Es razonable?", "No; un lápiz es mucho más liviano", "1 kg es como un paquete de azúcar."),
        ],
        "challenge": [
            ex("Estimaste que tres objetos pesan 1 kg en total. Después mediste 300 g, 450 g y 200 g. ¿Faltó o sobró, y cuántos g?", "Faltaron 50 g", "300 + 450 + 200 = 950 y 1.000 − 950 = 50."),
            ex("Estimaste 100 g, 400 g y 900 g para un objeto que pesa 450 g. ¿Cuál estimación fue la más cercana?", "400 g", "Está a 50 g de 450 g."),
        ],
    },
    context=[ex("Marta pesa una bolsa de naranjas y la balanza marca 1.500 g. ¿Cuántos kg y g son?", "1 kg y 500 g", "1.500 = 1.000 + 500.")],
    selfcheck=[
        arith("Estimaste 400 g y la balanza marca 550 g. ¿Cuántos g te equivocaste?", "550-400", "Se resta el valor menor al mayor."),
        ex("La balanza marca 2 kg. ¿Cuántos g son?", "2.000 g", "2 × 1.000 = 2.000.", calc="2*1000"),
        ex("¿Por qué conviene estimar antes de medir?", "Para comprobar si mi cálculo fue razonable", "Compara tu idea con la medida real."),
    ],
    open_task=task(
        "Elige tres objetos de tu casa que no se rompan. Estima cuánto pesa cada uno comparándolo con un clip (cerca de 1 g) o un paquete de 1 kg. Si tienes balanza, mídelos. Si no, usa estas medidas: lápiz 8 g, cuaderno 250 g, paquete de arroz 1.000 g. Anota estimación, medida y diferencia.",
        "Cuaderno: estimé 300 g, la medida es 250 g, me equivoqué en 50 g. Lápiz: estimé 10 g, medida 8 g, 2 g de diferencia.",
        ["estima antes de medir", "anota la medida con unidad", "calcula la diferencia con una resta", "usa un referente"],
        ["tabla con estimación y medida", "resta escrita"],
        ["no escribir la unidad", "restar números de unidades distintas"],
        "Pide decir el referente que usó para estimar. Reconoce que compare su estimación con la medida.",
    ),
    reinforce="Con ayuda, estima y luego pesa una fruta en una balanza de cocina. Anota las dos cantidades.",
    extend="Estima cuántos gramos tiene una bolsa de 1 kg dividida en 4 partes iguales y compruébalo con una cuenta.",
)

register(
    OA22, 5,
    materials="Lápiz y papel. Las cantidades y los pesos están escritos en cada ejercicio.",
    use="Aprenderé a resolver problemas con medio kilogramo y un cuarto de kilogramo. Sirve para entender las compras en el mercado.",
    prior=["Sé que 1 kg = 1.000 g.", "Sé sumar y restar números hasta 1.000."],
    explain=[
        "Medio kilogramo es la mitad de un kilogramo. Como 1 kg son 1.000 g, medio kilogramo son 500 g. Dos medios kilogramos forman 1 kg.",
        "Un cuarto de kilogramo es la cuarta parte de 1 kg. Entonces son 250 g. Cuatro cuartos forman 1 kg: 250 + 250 + 250 + 250 = 1.000 g. Tres cuartos de kilogramo son 750 g.",
        "Para resolver problemas, pasa todo a gramos antes de sumar o restar. Por ejemplo, ½ kg de pan y ¼ kg de queso pesan 500 + 250 = 750 g. Luego dices el resultado con su unidad.",
    ],
    vocab=[("medio kilogramo (½ kg)", "500 gramos"), ("cuarto de kilogramo (¼ kg)", "250 gramos"), ("tres cuartos (¾ kg)", "750 gramos"), ("fracción", "parte de un entero, como la mitad o un cuarto"), ("entero", "un kilogramo completo")],
    worked=[
        {"title": "Sumar medio y cuarto", "problem": "Compras ½ kg de pan y ¼ kg de queso. ¿Cuántos gramos compras?", "steps": ["½ kg son 500 g.", "¼ kg son 250 g.", "500 + 250 = 750."], "answer": "750 g"},
        {"title": "Lo que queda", "problem": "Hay 1 kg de harina. Usas ¼ kg. ¿Cuántos gramos quedan?", "steps": ["1 kg son 1.000 g.", "¼ kg son 250 g.", "1.000 − 250 = 750."], "answer": "Quedan 750 g"},
    ],
    mistakes=[
        {"wrong": "Decir que ¼ kg son 25 g.", "why": "Se confunde con un cuarto de 100.", "fix": "Un cuarto de 1.000 g son 250 g."},
        {"wrong": "Decir que medio kilogramo y medio kilogramo son otro medio.", "why": "No se suman las partes.", "fix": "500 g + 500 g = 1.000 g, que es 1 kg."},
    ],
    tiers={
        "recovery": [
            ex("Medio kilogramo, ¿cuántos gramos es?", "500 g", "La mitad de 1.000 g es 500 g."),
            ex("Un cuarto de kilogramo, ¿cuántos gramos es?", "250 g", "Un cuarto de 1.000 g es 250 g.", calc="1000//4"),
            ex("¿Cuántos cuartos de kilogramo forman 1 kg?", "4", "Cuatro partes de 250 g hacen 1.000 g.", calc="1000//250"),
        ],
        "understand": [
            arith("Tres cuartos de kilogramo, ¿cuántos gramos son?", "3*250", "Cada cuarto de kilogramo son 250 g."),
            ex("Dos medios kilogramos juntos, ¿cuántos kg son?", "1 kg", "500 g + 500 g = 1.000 g."),
            ex("¿Qué pesa más: ½ kg o 300 g?", "½ kg", "½ kg son 500 g y 500 es mayor que 300."),
        ],
        "apply": [
            arith("Compras ¾ kg de papas y ¼ kg de cebollas. ¿Cuántos gramos compras en total?", "750+250", "Se suman las dos cantidades en gramos."),
            arith("Hay 1 kg de azúcar y usas ¾ kg. ¿Cuántos gramos quedan?", "1000-750", "Se resta lo usado al total."),
            arith("Quieres llenar bolsas de ¼ kg con 2 kg de lentejas. ¿Cuántas bolsas llenas?", "2*4", "Cada kilogramo da 4 bolsas de ¼ kg."),
        ],
        "reason": [
            ex("Rita dice que ¼ kg son 25 g. ¿Qué error comete?", "Un cuarto de 1.000 g son 250 g", "El kilogramo tiene mil gramos y no cien."),
            ex("Teo dice que ½ kg más ½ kg son 1 kg y medio. ¿Es cierto?", "No; son 1 kg", "500 g + 500 g = 1.000 g."),
        ],
        "challenge": [
            arith("Una torta lleva 1 kg y ¼ kg de harina. ¿Cuántos gramos de harina lleva en total?", "1000+250", "1 kg son 1.000 g y se suma el cuarto."),
            ex("Compraste 3 bolsas de ¼ kg de nueces. ¿Cuántos gramos son y es más o menos que ½ kg?", "750 g; es más que ½ kg", "3 × 250 = 750 y 750 es mayor que 500.", calc="3*250"),
        ],
    },
    context=[arith("En la feria la vendedora pesa ¾ kg de tomates. ¿Cuántos gramos faltan para completar 1 kg?", "1000-750", "Se resta lo que hay al kilogramo completo.")],
    selfcheck=[
        ex("¿Cuántos gramos son ½ kg?", "500", "La mitad de 1.000 es 500."),
        arith("Dos cuartos de kilogramo son ¿cuántos gramos?", "2*250", "Cada cuarto son 250 g."),
        arith("Compras ¼ kg de arroz y ¼ kg de lentejas. ¿Cuántos gramos compras?", "250+250", "Se suman las dos cantidades."),
    ],
    open_task=task(
        "Una familia hace una compra: ½ kg de pan, ¼ kg de queso y ¾ kg de tomates. Escribe cuántos gramos pesa cada producto, cuántos gramos pesa toda la compra y cuántos kg y g son.",
        "Pan: 500 g. Queso: 250 g. Tomates: 750 g. Total: 500 + 250 + 750 = 1.500 g, o sea 1 kg y 500 g.",
        ["convierte cada fracción a gramos", "suma las tres cantidades", "escribe el total en g y en kg y g", "usa las unidades"],
        ["tres conversiones", "suma", "total en dos formas"],
        ["decir que ¼ kg son 25 g", "sumar fracciones sin pasar a gramos"],
        "Pide pasar todo a gramos antes de sumar. Reconoce que exprese el total de dos maneras.",
    ),
    reinforce="Busca una receta o una bolsa en tu casa que diga ½ kg o ¼ kg y escribe cuántos gramos son.",
    extend="Calcula cuántos gramos pesan 5 bolsas de ¼ kg y escríbelo en kg y g.",
)
