"""Student material for 4.º básico Matemática, OA 23 (área de rectángulos y cuadrados en cm² y m²) y OA 24 (volumen en unidades cúbicas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA23, OA24 = "MA04 OA 23", "MA04 OA 24"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 23
register(
    OA23, 1,
    materials="Papel cuadriculado o una hoja en que dibujes cuadrados iguales de 1 cm de lado. Si no tienes, sigue los dibujos descritos con palabras.",
    use="Aprenderé qué es el área y cómo se mide con cuadrados iguales. Sirve para saber cuánto papel, tela o piso se necesita.",
    prior=["Sé multiplicar con las tablas.", "Sé que un cuadrado tiene 4 lados iguales."],
    explain=[
        "El área es cuánta superficie cubre una figura plana, por ejemplo una hoja, una pared o un piso. Para medirla, se la cubre con cuadrados del mismo tamaño llamados unidades cuadradas, y se cuenta cuántos hay.",
        "Para cubrir bien una superficie, los cuadrados deben ser todos iguales, no deben dejar huecos y tampoco deben montarse unos sobre otros, a eso se le llama traslape. Si hay un hueco o un traslape, el conteo no mide el área.",
        "Un cuadrado de 1 cm de lado es una unidad cuadrada llamada 1 cm². Si una figura se cubre exactamente con 12 de ellos, su área es 12 cm². El número dice cuántas unidades caben y la unidad dice con qué cuadrado se midió.",
    ],
    vocab=[("área", "cantidad de superficie que cubre una figura plana"), ("unidad cuadrada", "cuadrado de lado conocido que se usa para medir área"), ("traslape", "cuando una pieza queda encima de otra"), ("hueco", "espacio sin cubrir entre las piezas")],
    worked=[
        {"title": "Contar unidades cuadradas", "problem": "Un rectángulo se cubre con 3 filas de 5 cuadrados de 1 cm de lado, sin huecos ni traslapes. ¿Cuál es su área?", "steps": ["Cada fila tiene 5 cuadrados y hay 3 filas.", "Cuento todos: 5 + 5 + 5 = 15."], "answer": "El área es 15 cm²"},
        {"title": "Detectar un recubrimiento incorrecto", "problem": "Ana cubrió una hoja con 10 cuadrados, pero dejó un hueco del tamaño de 2 cuadrados. ¿Sirve su conteo para dar el área?", "steps": ["Hay un hueco, así que la superficie no está toda cubierta.", "Si completa el hueco, faltan 2 cuadrados: 10 + 2 = 12."], "answer": "No sirve; el área verdadera es 12 unidades cuadradas"},
    ],
    mistakes=[
        {"wrong": "Cubrir una figura con cuadrados de tamaños distintos.", "why": "Las unidades no son iguales y no se pueden comparar.", "fix": "Usa siempre cuadrados del mismo tamaño."},
        {"wrong": "Medir el área sumando los lados.", "why": "Los lados son largos, y el área mide superficie.", "fix": "Cuenta los cuadrados que cubren toda la superficie."},
    ],
    tiers={
        "recovery": [
            ex("Una figura se cubre exactamente con 8 cuadrados de 1 cm de lado. ¿Cuál es su área?", "8 cm²", "Cada cuadrado es 1 cm² y hay 8."),
            ex("¿Con qué tipo de figura se mide el área: cuadrados iguales o barras de distinto largo?", "Cuadrados iguales", "El área se mide con unidades cuadradas del mismo tamaño."),
            arith("Un rectángulo tiene 2 filas de 6 cuadrados de 1 cm de lado. ¿Cuántos cuadrados hay?", "2*6", "Se multiplican las filas por los cuadrados de cada fila.", " cuadrados"),
        ],
        "understand": [
            ex("Al cubrir una superficie, se dejaron huecos sin tapar. ¿El conteo de cuadrados da el área completa?", "No", "Faltan los cuadrados que llenarían los huecos."),
            ex("Dos cuadrados quedaron uno encima del otro. ¿Cómo se llama ese defecto?", "Traslape", "Traslape es cuando una pieza queda sobre otra."),
            arith("Una tarjeta se cubre con 4 filas de 3 cuadrados de 1 cm². ¿Cuántos cm² es su área?", "4*3", "Se cuentan todos los cuadrados: filas por cuadrados por fila.", " cm²"),
        ],
        "apply": [
            ex("Una hoja se cubre con 5 filas de 4 cuadrados de 1 cm² y no queda ningún hueco. ¿Cuál es el área de la hoja?", "20 cm²", "5 × 4 = 20 unidades de 1 cm².", calc="5*4"),
            ex("Un rectángulo de 3 por 7 cuadrados de 1 cm tiene un cuadrado más pegado arriba para formar otra figura. ¿Cuántos cm² tiene la nueva figura?", "22 cm²", "3 × 7 = 21 y se suma 1 cuadrado más.", calc="3*7+1"),
            ex("Una figura de 6 cm² y otra figura de 9 cm² se pegan sin traslape ni huecos. ¿Cuál es el área total?", "15 cm²", "Las áreas se suman: 6 + 9.", calc="6+9"),
        ],
        "reason": [
            ex("Pía cubrió una figura con 15 cuadrados, pero dos quedaron exactamente uno encima del otro. ¿El área es 15? Explica.", "No; el área es 14 cm², porque un cuadrado se repite", "Un traslape cuenta una superficie dos veces.", calc="15-1"),
            ex("Tomás dice que el área de una mesa es la suma de sus 4 lados. ¿Qué mide eso realmente y qué mide el área?", "Eso mide el contorno; el área mide la superficie cubierta", "Los lados dan el borde, no la superficie."),
        ],
        "challenge": [
            ex("Dos rectángulos: uno cubierto con 3 filas de 6 cuadrados y otro con 4 filas de 5 cuadrados. ¿Cuál tiene mayor área y por cuántos cm²?", "El de 4 filas de 5, por 2 cm²", "El primero tiene 18 cm² y el segundo 20 cm²; 20 − 18 = 2.", calc="4*5-3*6"),
            ex("Una figura tiene 24 cm² de área y se cubrió con filas de 6 cuadrados cada una. ¿Cuántas filas son?", "4 filas", "24 ÷ 6 = 4.", calc="24//6"),
        ],
    },
    context=[ex("Para forrar la tapa de un cuaderno, Sofía usa papel de colores cortado en cuadrados de 1 cm de lado. La tapa se cubre con 20 filas de 15 cuadrados, sin huecos. ¿Cuántos cuadrados necesita?", "300 cuadrados", "20 × 15 = 300.", calc="20*15")],
    selfcheck=[
        ex("¿Qué mide el área: el borde de una figura o la superficie que cubre?", "La superficie que cubre", "El área es cuánta superficie hay dentro de la figura."),
        ex("Una figura se cubre con 3 filas de 8 cuadrados de 1 cm². ¿Cuál es su área?", "24 cm²", "3 × 8 = 24.", calc="3*8"),
        ex("Si dos cuadrados quedan uno sobre otro, ¿el conteo da el área?", "No", "Hay un traslape y se cuenta de más."),
    ],
    open_task=task(
        "Dibuja en un papel un rectángulo de 4 filas por 6 columnas de cuadrados de 1 cm, o usa papel cuadriculado. Cuéntalos de dos formas: uno por uno y con una multiplicación. Escribe el área en cm² y explica por qué ambos conteos coinciden.",
        "4 filas de 6: 4 × 6 = 24 cuadrados. Los conté uno por uno y también dio 24. El área es 24 cm².",
        ["dibuja la figura con cuadrados iguales", "cuenta de dos formas", "escribe el área con cm²", "explica por qué coinciden"],
        ["dibujo", "dos conteos", "unidad cm²"],
        ["dejar huecos en el dibujo", "olvidar la unidad"],
        "Pide mostrar cada fila con el dedo. Reconoce que escriba cm² en la respuesta.",
    ),
    reinforce="Cubre la tapa de un cuaderno con cuadrados de papel y cuenta cuántos usaste. Anota el número.",
    extend="Explica por qué dos figuras con formas distintas pueden tener el mismo número de cuadrados.",
)

register(
    OA23, 2,
    materials="Una regla. Si quieres, mide la hoja de tu cuaderno y marca un cuadrado de 1 cm de lado. Las medidas aparecen escritas en los ejercicios.",
    use="Aprenderé cuándo conviene medir un área en cm² y cuándo en m². Sirve para saber el tamaño de una hoja, una sala o un patio.",
    prior=["Sé que 1 cm² es un cuadrado de 1 cm de lado.", "Sé usar metros y centímetros."],
    explain=[
        "El centímetro cuadrado (cm²) es un cuadrado de 1 cm de lado. Es una unidad pequeña. Sirve para medir superficies chicas como una tarjeta, una estampilla o la hoja de un cuaderno.",
        "El metro cuadrado (m²) es un cuadrado de 1 m de lado. Es una unidad grande. Sirve para medir superficies grandes como una sala, un patio o una cancha.",
        "Para elegir, piensa en el tamaño de la superficie. Si usas cm² para un patio, saldrá un número gigante. Si usas m² para una tarjeta, saldrá un número muy chico. Elige la unidad que dé un número cómodo y escribe siempre cm² o m².",
    ],
    vocab=[("cm²", "centímetro cuadrado: cuadrado de 1 cm de lado"), ("m²", "metro cuadrado: cuadrado de 1 m de lado"), ("superficie", "parte plana que se puede cubrir"), ("unidad estandarizada", "unidad que todos usan y que tiene siempre el mismo tamaño")],
    worked=[
        {"title": "Elegir la unidad para una tarjeta", "problem": "¿Conviene medir el área de una tarjeta de saludo en cm² o en m²?", "steps": ["Una tarjeta es pequeña, cabe en la mano.", "Un metro cuadrado es mucho más grande que la tarjeta."], "answer": "Conviene medirla en cm²"},
        {"title": "Elegir la unidad para un patio", "problem": "El patio tiene 4 m de largo y 5 m de ancho. ¿Qué unidad conviene para su área?", "steps": ["El patio se mide en metros.", "Las filas y columnas de cuadrados son de 1 m de lado."], "answer": "Conviene m²"},
    ],
    mistakes=[
        {"wrong": "Escribir el área de una sala como 40 cm.", "why": "Se usa una unidad de largo (cm) para medir superficie.", "fix": "El área se mide en unidades cuadradas: 40 m²."},
        {"wrong": "Medir el área de un cuaderno en m² y escribir 600 m².", "why": "No se compara la unidad con el tamaño de la superficie.", "fix": "Un cuaderno es chico: se mide en cm²."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué unidad de área es un cuadrado de 1 cm de lado?", "1 cm²", "Es un centímetro cuadrado."),
            ex("¿Qué unidad conviene para el área de una estampilla: cm² o m²?", "cm²", "Una estampilla es muy pequeña."),
            ex("¿Qué unidad conviene para el área de un patio de colegio: cm² o m²?", "m²", "El patio es muy grande."),
        ],
        "understand": [
            ex("¿El área se mide en unidades de largo, como cm, o en unidades cuadradas, como cm²?", "En unidades cuadradas", "El área mide superficie, no longitud."),
            ex("Una sala de clases tiene un área de 48. ¿Con qué unidad tiene sentido: cm² o m²?", "m²", "48 cm² cabrían en la palma de la mano; la sala es mucho más grande."),
            ex("Una hoja de cuaderno tiene un área de 600. ¿Con qué unidad tiene sentido: cm² o m²?", "cm²", "Una hoja es pequeña, 600 cm² es casi el tamaño de una hoja grande."),
        ],
        "apply": [
            ex("Una pared mide 3 m por 4 m. Se cubre con cuadrados de 1 m de lado. ¿Cuántos cuadrados caben y en qué unidad se expresa el área?", "12 y se expresa en m²", "3 × 4 = 12 cuadrados de 1 m².", calc="3*4"),
            ex("Una tarjeta mide 5 cm por 8 cm. Se cubre con cuadrados de 1 cm de lado. ¿Cuántos caben y en qué unidad se expresa?", "40 y se expresa en cm²", "5 × 8 = 40 cuadrados de 1 cm².", calc="5*8"),
            ex("Elige la medida razonable para el área de una mesa de comedor: 2 cm², 2 m² o 2.000 m².", "2 m²", "Una mesa cubre un par de metros cuadrados."),
        ],
        "reason": [
            ex("Rosa escribió que el área de su pieza es 12 cm. ¿Qué dos errores hay?", "Usó una unidad de largo y una unidad muy pequeña; debía ser m²", "El área necesita unidad cuadrada y la pieza es grande."),
            ex("Un piso grande se mide en m². ¿Por qué no conviene medirlo en cm²?", "Porque el número sería muy grande e incómodo", "Hay muchos cm² en un piso; con m² el número es más corto."),
        ],
        "challenge": [
            ex("Un pizarrón mide 2 m por 3 m. Un cuaderno mide 20 cm por 30 cm. ¿Qué unidad usarías para cada uno?", "Pizarrón en m²; cuaderno en cm²", "El pizarrón es grande y el cuaderno es chico."),
            ex("Un rectángulo mide 10 cm por 10 cm. ¿Cuántos cm² tiene?", "100 cm²", "10 × 10 = 100.", calc="10*10"),
        ],
    },
    context=[ex("En una feria, un puesto ocupa un rectángulo de 3 m por 2 m y un cartel mide 40 cm por 30 cm. ¿En qué unidad medirías el área del puesto y en cuál la del cartel?", "El puesto en m²; el cartel en cm²", "El puesto es grande y el cartel es chico.")],
    selfcheck=[
        ex("Escribe la unidad correcta para el área de una cancha: cm o m².", "m²", "El área necesita unidad cuadrada y la cancha es grande."),
        ex("¿Qué unidad conviene para el área de una goma de borrar: cm² o m²?", "cm²", "Una goma es muy pequeña."),
        ex("¿Qué significa m²?", "Metro cuadrado, un cuadrado de 1 m de lado", "Es la unidad de área que mide un cuadrado de un metro por un metro."),
    ],
    open_task=task(
        "Elige tres superficies de la lista: tapa de un cuaderno, piso de la sala, estampilla, patio del colegio, tarjeta de saludo. Para cada una escribe si la medirías en cm² o en m² y una frase que explique por qué.",
        "Tapa de un cuaderno: cm², porque es chica. Patio del colegio: m², porque es muy grande.",
        ["elige tres superficies de la lista", "elige la unidad para cada una", "justifica con el tamaño", "usa la forma cm² o m²"],
        ["tres unidades elegidas", "tres justificaciones"],
        ["usar cm o m sin cuadrado", "no relacionar con el tamaño"],
        "Pide comparar con algo conocido. Reconoce que la unidad tenga el exponente 2.",
    ),
    reinforce="Mira dos superficies de tu casa, una chica y una grande. Escribe qué unidad usarías para cada una.",
    extend="Explica con tus palabras por qué no se dice «el área mide 12 cm» sino «el área mide 12 cm²».",
)

register(
    OA23, 3,
    materials="Papel cuadriculado o lápiz y papel para dibujar filas y columnas. Si no tienes, usa los números de cada ejercicio.",
    use="Aprenderé a contar un área con filas y columnas, usando la multiplicación. Sirve para contar rápido baldosas, cuadrados de una tableta de chocolate o mosaicos.",
    prior=["Sé multiplicar con las tablas.", "Sé que el área se mide con unidades cuadradas."],
    explain=[
        "Cuando un rectángulo se cubre con cuadrados, estos forman filas y columnas. Una fila es una línea de cuadrados de lado a lado. Una columna es una línea de arriba hacia abajo.",
        "Si hay 4 filas y cada fila tiene 6 cuadrados, el total es 6 + 6 + 6 + 6 = 24. Pero es más rápido multiplicar: 4 × 6 = 24. El producto del número de filas por el número de columnas da el número de cuadrados.",
        "El orden no cambia el resultado: 4 × 6 es igual que 6 × 4. Si contaste por filas o por columnas, obtienes el mismo número. Después escribe la unidad, por ejemplo 24 cm² si cada cuadrado era de 1 cm².",
    ],
    vocab=[("fila", "línea de cuadrados de lado a lado, en horizontal"), ("columna", "línea de cuadrados de arriba hacia abajo, en vertical"), ("producto", "resultado de multiplicar"), ("arreglo rectangular", "cuadrados ordenados en filas y columnas")],
    worked=[
        {"title": "Multiplicar filas por columnas", "problem": "Un mosaico tiene 5 filas y 8 columnas de cuadrados de 1 cm de lado. ¿Cuál es su área?", "steps": ["Multiplico filas por columnas: 5 × 8.", "5 × 8 = 40."], "answer": "El área es 40 cm²"},
        {"title": "Cambiar el orden", "problem": "¿Dará lo mismo contar 7 filas de 3 que 3 filas de 7?", "steps": ["7 × 3 = 21.", "3 × 7 = 21."], "answer": "Sí, da 21 en ambos casos"},
    ],
    mistakes=[
        {"wrong": "Sumar filas y columnas: 5 + 8 = 13.", "why": "Se suman los números en vez de multiplicarlos.", "fix": "Multiplica: 5 × 8 = 40 cuadrados."},
        {"wrong": "Contar solo el borde de cuadrados y no los del medio.", "why": "Se olvida que el interior también está cubierto.", "fix": "Cuenta todos los cuadrados, o multiplica filas por columnas."},
    ],
    tiers={
        "recovery": [
            arith("Un rectángulo tiene 3 filas y 4 columnas de cuadrados. ¿Cuántos cuadrados tiene?", "3*4", "Se multiplica el número de filas por el de columnas.", " cuadrados"),
            ex("En un arreglo, ¿qué es una fila: una línea horizontal o una vertical?", "Una línea horizontal", "Las filas van de lado a lado."),
            arith("Un tablero tiene 2 filas y 9 columnas de cuadrados de 1 cm². ¿Cuál es su área en cm²?", "2*9", "Cada cuadrado es 1 cm² y se multiplican filas por columnas.", " cm²"),
        ],
        "understand": [
            ex("¿Por qué es mejor multiplicar que sumar muchas veces el mismo número para contar un rectángulo?", "Porque es más rápido y se llega al mismo resultado", "Multiplicar es una suma repetida abreviada."),
            ex("Un rectángulo tiene 6 filas de 5 cuadrados. Otro tiene 5 filas de 6 cuadrados. ¿Tienen la misma área?", "Sí, 30 cuadrados en ambos", "6 × 5 = 5 × 6 = 30.", calc="6*5"),
            arith("Un piso tiene 8 filas y 7 columnas de baldosas de 1 m². ¿Cuántos m² tiene?", "8*7", "Se multiplican filas por columnas.", " m²"),
        ],
        "apply": [
            arith("Una tableta tiene 4 filas de 9 cuadritos. ¿Cuántos cuadritos hay?", "4*9", "Se multiplican filas por cuadritos de cada fila.", " cuadritos"),
            arith("Un huerto cubre 6 filas por 10 columnas de cuadrados de 1 m². ¿Cuál es su área?", "6*10", "Se multiplican filas por columnas.", " m²"),
            ex("Un mantel está cubierto con 12 columnas de 5 cuadrados cada una. ¿Cuántos cuadrados hay?", "60", "12 × 5 = 60.", calc="12*5"),
        ],
        "reason": [
            ex("Ana dice que 5 filas y 8 columnas dan 13 cuadrados. ¿Qué hizo mal?", "Sumó en vez de multiplicar; son 40", "5 × 8 = 40.", calc="5*8"),
            ex("En un arreglo de 4 filas y 6 columnas, Beto cuenta por columnas: 4 + 4 + 4 + 4 + 4 + 4. ¿Llega al mismo resultado que 4 × 6? Explica.", "Sí; son 6 grupos de 4, o sea 24", "Contar por columnas o por filas da el mismo total.", calc="4*6"),
        ],
        "challenge": [
            ex("Un rectángulo tiene 36 cuadrados en 4 filas. ¿Cuántas columnas tiene?", "9 columnas", "36 ÷ 4 = 9.", calc="36//4"),
            ex("Un arreglo de 7 filas y 9 columnas pierde 3 cuadrados. ¿Cuántos quedan?", "60", "7 × 9 = 63 y 63 − 3 = 60.", calc="7*9-3"),
        ],
    },
    context=[ex("En el patio se pintaron cuadrados de 1 m de lado en 8 filas y 6 columnas para jugar. ¿Cuántos m² se pintaron?", "48 m²", "8 × 6 = 48.", calc="8*6")],
    selfcheck=[
        ex("¿Cuántos cuadrados hay en 5 filas de 7?", "35", "5 × 7 = 35.", calc="5*7"),
        ex("¿Cuántos cuadrados hay en 9 filas de 3?", "27", "9 × 3 = 27.", calc="9*3"),
        ex("¿Se obtiene lo mismo con 4 × 8 que con 8 × 4?", "Sí", "Los dos productos son 32."),
    ],
    open_task=task(
        "Elige un tamaño de la lista: 3 filas por 8 columnas, 5 filas por 6 columnas o 4 filas por 9 columnas. Dibuja los cuadrados (o imagínalos) y escribe la multiplicación que da el área. Después escribe el área con la unidad cm².",
        "5 filas por 6 columnas: 5 × 6 = 30, o sea 30 cm².",
        ["elige un tamaño de la lista", "dibuja filas y columnas", "escribe la multiplicación", "escribe el área con la unidad"],
        ["dibujo", "multiplicación", "área con unidad"],
        ["sumar en vez de multiplicar", "olvidar el cm²"],
        "Pide explicar qué número representa las filas y qué número las columnas. Reconoce el uso de la unidad.",
    ),
    reinforce="Cuenta cuántos cuadrados de una baldosa o de una cuadrícula hay en una fila y cuántas filas hay. Multiplícalos.",
    extend="Un arreglo tiene 24 cuadrados. Escribe todos los pares de filas y columnas que lo forman.",
)

register(
    OA23, 4,
    materials="Lápiz y papel. Los datos de largo y ancho están en cada ejercicio. Una regla sirve para comprobar medidas reales.",
    use="Aprenderé a calcular el área de rectángulos y cuadrados multiplicando sus lados. Sirve para saber cuánto papel, pintura o piso se necesita.",
    prior=["Sé que el área se cuenta con cuadrados de 1 cm² o 1 m².", "Sé multiplicar con las tablas."],
    explain=[
        "El área de un rectángulo es su largo por su ancho. Si un rectángulo mide 7 cm de largo y 4 cm de ancho, caben 7 cuadrados de 1 cm en cada fila y hay 4 filas, así que el área es 7 × 4 = 28 cm².",
        "Un cuadrado es un rectángulo con los 4 lados iguales. Su área es el lado por el lado. Por ejemplo, un cuadrado de 5 cm de lado tiene área 5 × 5 = 25 cm².",
        "La unidad del área depende de la unidad de los lados. Si los lados están en cm, el área es en cm². Si los lados están en m, el área es en m². Usa siempre la misma unidad para los dos lados antes de multiplicar.",
    ],
    vocab=[("largo", "lado más largo de un rectángulo"), ("ancho", "lado más corto de un rectángulo"), ("lado", "segmento que forma el borde de una figura"), ("cuadrado", "rectángulo con sus 4 lados iguales")],
    worked=[
        {"title": "Área de un rectángulo", "problem": "Un cartel mide 9 cm de largo y 6 cm de ancho. ¿Cuál es su área?", "steps": ["Multiplico largo por ancho: 9 × 6.", "9 × 6 = 54."], "answer": "El área es 54 cm²"},
        {"title": "Área de un cuadrado", "problem": "Un cuadrado de papel tiene lados de 8 cm. ¿Cuál es su área?", "steps": ["En un cuadrado los dos lados son iguales: 8 × 8.", "8 × 8 = 64."], "answer": "El área es 64 cm²"},
    ],
    mistakes=[
        {"wrong": "Calcular el área de un rectángulo de 7 cm por 4 cm como 7 + 4 = 11.", "why": "Se suman los lados en vez de multiplicar.", "fix": "Multiplica: 7 × 4 = 28 cm²."},
        {"wrong": "Escribir el área de un cuadrado de 5 m de lado como 20 m².", "why": "Se multiplican 5 × 4 (los cuatro lados) en vez de 5 × 5.", "fix": "Multiplica el lado por sí mismo: 5 × 5 = 25 m²."},
    ],
    tiers={
        "recovery": [
            arith("Un rectángulo mide 5 cm de largo y 3 cm de ancho. ¿Cuál es su área?", "5*3", "Se multiplica el largo por el ancho.", " cm²"),
            arith("Un cuadrado tiene 4 cm de lado. ¿Cuál es su área?", "4*4", "En un cuadrado se multiplica el lado por sí mismo.", " cm²"),
            ex("Los lados de un rectángulo están en metros. ¿En qué unidad queda el área?", "m²", "Si los lados están en m, el área está en m²."),
        ],
        "understand": [
            ex("¿Qué se hace con el largo y el ancho para obtener el área de un rectángulo?", "Se multiplican", "Largo por ancho da la cantidad de cuadrados."),
            arith("Una mesa mide 2 m de largo y 1 m de ancho. ¿Cuántos m² cubre?", "2*1", "Se multiplica el largo por el ancho.", " m²"),
            ex("¿Cuál es el área de un cuadrado de 6 m de lado?", "36 m²", "6 × 6 = 36.", calc="6*6"),
        ],
        "apply": [
            arith("Una pared mide 4 m de largo y 3 m de ancho. ¿Cuál es su área?", "4*3", "Se multiplica el largo por el ancho.", " m²"),
            arith("Un papel lustre cuadrado mide 9 cm de lado. ¿Cuál es su área?", "9*9", "En un cuadrado se multiplica el lado por sí mismo.", " cm²"),
            arith("Una cartulina mide 12 cm de largo y 8 cm de ancho. ¿Cuál es su área?", "12*8", "Se multiplica el largo por el ancho.", " cm²"),
        ],
        "reason": [
            ex("Pablo calculó el área de un rectángulo de 7 cm por 4 cm como 11 cm². ¿Qué error cometió y cuál es el área?", "Sumó los lados; el área es 28 cm²", "7 × 4 = 28.", calc="7*4"),
            ex("Ema dice que un cuadrado de 5 m de lado tiene 20 m² de área. ¿Tiene razón?", "No; tiene 25 m²", "5 × 5 = 25, no 5 × 4.", calc="5*5"),
        ],
        "challenge": [
            ex("Un rectángulo tiene 48 cm² de área y su largo es 8 cm. ¿Cuál es su ancho?", "6 cm", "48 ÷ 8 = 6.", calc="48//8"),
            ex("Un piso rectangular de 5 m por 4 m se cubre con cuadrados de 1 m². ¿Cuántos faltan si ya hay 12 colocados?", "8", "5 × 4 = 20 y 20 − 12 = 8.", calc="5*4-12"),
        ],
    },
    context=[ex("Un salón mide 7 m de largo y 6 m de ancho. Para cubrir el piso se vende alfombra por m². ¿Cuántos m² de alfombra se necesitan?", "42 m²", "7 × 6 = 42.", calc="7*6")],
    selfcheck=[
        ex("¿Cuál es el área de un rectángulo de 10 cm por 3 cm?", "30 cm²", "10 × 3 = 30.", calc="10*3"),
        ex("¿Cuál es el área de un cuadrado de 7 cm de lado?", "49 cm²", "7 × 7 = 49.", calc="7*7"),
        ex("Un rectángulo mide 5 m por 5 m. ¿Es un cuadrado?", "Sí", "Tiene los lados iguales."),
    ],
    open_task=task(
        "Elige una de estas superficies: un cartel de 12 cm por 9 cm, un cuadrado de 8 cm de lado o un patio de 10 m por 6 m. Calcula su área, escribe la multiplicación y la unidad. Después dibuja un esquema simple con las medidas.",
        "Cuadrado de 8 cm de lado: 8 × 8 = 64 cm².",
        ["elige una de las tres superficies", "multiplica las medidas", "escribe la unidad cuadrada", "dibuja el esquema con las medidas"],
        ["multiplicación", "área con unidad", "esquema"],
        ["sumar en vez de multiplicar", "no usar la unidad cuadrada"],
        "Pide explicar por qué se multiplica. Reconoce la unidad correcta.",
    ),
    reinforce="Mide el largo y el ancho de una hoja con regla. Calcula su área y escribe la unidad.",
    extend="Escribe cuánto da el área de un cuadrado de 1 cm, 2 cm, 3 cm y 4 cm de lado. ¿Qué patrón notas?",
)

register(
    OA23, 5,
    materials="Papel cuadriculado o lápiz y papel. Si tienes acceso a un programa de geometría (como uno educativo) un adulto puede ayudarte a probar; no es necesario.",
    use="Aprenderé que rectángulos distintos pueden tener la misma área. Sirve para diseñar huertos, carteles o mesas con el mismo espacio y distinta forma.",
    prior=["Sé calcular el área de un rectángulo.", "Sé qué pares de números multiplican para dar un número."],
    explain=[
        "Dos rectángulos pueden verse muy distintos y tener la misma área. Por ejemplo, un rectángulo de 2 cm por 6 cm y otro de 3 cm por 4 cm tienen los dos 12 cm². Cubren la misma cantidad de superficie.",
        "Para construir rectángulos de un área dada, busca pares de números que multipliquen para dar esa área. Para 12: 1 × 12, 2 × 6 y 3 × 4. Cada par da un rectángulo distinto: largo y ancho cambian, el área no.",
        "Un cuadrado también puede tener una de esas áreas si el número es un producto de dos iguales. Por ejemplo, 16 = 4 × 4. En un programa de geometría puedes arrastrar los lados de un rectángulo y ver cómo cambia la forma. Para mantener el área, si un lado crece, el otro debe achicarse.",
    ],
    vocab=[("misma área", "igual cantidad de superficie cubierta"), ("factores", "los números que se multiplican para obtener un producto"), ("par de factores", "dos números que multiplicados dan el área"), ("software geométrico", "programa que permite dibujar y mover figuras en pantalla")],
    worked=[
        {"title": "Buscar rectángulos de 12 cm²", "problem": "Encuentra tres rectángulos con área 12 cm², con medidas enteras en cm.", "steps": ["Busco pares de números que multiplicados den 12: 1 y 12, 2 y 6, 3 y 4.", "Cada par da un rectángulo: largo y ancho."], "answer": "1 cm × 12 cm, 2 cm × 6 cm y 3 cm × 4 cm"},
        {"title": "Comparar áreas", "problem": "¿Tienen la misma área un rectángulo de 5 cm por 4 cm y uno de 2 cm por 10 cm?", "steps": ["El primero: 5 × 4 = 20.", "El segundo: 2 × 10 = 20."], "answer": "Sí, ambos tienen 20 cm²"},
    ],
    mistakes=[
        {"wrong": "Pensar que si un rectángulo es más largo, entonces tiene más área.", "why": "Se mira solo un lado y no se multiplica por el otro.", "fix": "Multiplica largo por ancho y compara los productos."},
        {"wrong": "Usar 3 + 5 = 8 como área y buscar otro rectángulo con suma 8.", "why": "Se confunde la suma de los lados con el producto.", "fix": "Busca pares que multipliquen para dar el área."},
    ],
    tiers={
        "recovery": [
            arith("Un rectángulo mide 2 cm por 6 cm. ¿Cuál es su área?", "2*6", "Se multiplican largo y ancho.", " cm²"),
            arith("Otro rectángulo mide 3 cm por 4 cm. ¿Cuál es su área?", "3*4", "Se multiplican largo y ancho.", " cm²"),
            ex("¿Los dos rectángulos anteriores (2 por 6 y 3 por 4) tienen la misma área?", "Sí, 12 cm² los dos", "Los dos productos son 12."),
        ],
        "understand": [
            ex("¿Qué rectángulo de medidas enteras tiene 10 cm² y un lado de 2 cm?", "2 cm por 5 cm", "2 × 5 = 10."),
            ex("Un rectángulo mide 1 cm por 8 cm. ¿Qué medidas enteras tiene otro rectángulo con la misma área, si uno de sus lados es 2 cm?", "2 cm por 4 cm", "1 × 8 = 8 y 2 × 4 = 8."),
            ex("¿Es posible que un rectángulo largo y delgado tenga la misma área que uno corto y ancho?", "Sí", "Lo que importa es el producto largo × ancho."),
        ],
        "apply": [
            ex("Un huerto necesita 20 m². Si el ancho es 4 m, ¿cuánto debe medir el largo?", "5 m", "20 ÷ 4 = 5.", calc="20//4"),
            ex("Escribe un rectángulo de medidas enteras en m con 18 m² y un lado de 3 m.", "3 m por 6 m", "3 × 6 = 18."),
            ex("Un rectángulo mide 6 cm por 4 cm. Otro mide 8 cm por 3 cm. ¿Tienen la misma área?", "Sí, los dos tienen 24 cm²", "6 × 4 = 8 × 3 = 24.", calc="6*4"),
        ],
        "reason": [
            ex("Ema dice que un rectángulo de 3 cm por 8 cm tiene menos área que uno de 6 cm por 4 cm porque tiene un lado más corto. ¿Tiene razón?", "No; los dos tienen 24 cm²", "3 × 8 = 6 × 4 = 24.", calc="3*8"),
            ex("Para mantener 24 cm² de área, si un lado se duplica de 3 cm a 6 cm, ¿qué le pasa al otro lado, que era de 8 cm?", "Se reduce a la mitad: 4 cm", "6 × 4 = 24."),
        ],
        "challenge": [
            ex("¿Cuántos rectángulos distintos de medidas enteras en cm (sin contar el giro) tienen 16 cm² de área? Incluye el cuadrado.", "3", "Son 1 × 16, 2 × 8 y 4 × 4."),
            ex("Un cuadrado de lado 4 cm tiene la misma área que un rectángulo de ancho 2 cm. ¿Cuánto mide el largo?", "8 cm", "4 × 4 = 16 y 16 ÷ 2 = 8.", calc="16//2"),
        ],
    },
    context=[ex("Una profesora quiere una tarjeta de 36 cm² con medidas enteras en cm y un lado de 4 cm. ¿Cuánto mide el otro lado?", "9 cm", "36 ÷ 4 = 9.", calc="36//4")],
    selfcheck=[
        ex("¿Qué área tiene un rectángulo de 2 cm por 9 cm?", "18 cm²", "2 × 9 = 18.", calc="2*9"),
        ex("¿Qué otro rectángulo de medidas enteras tiene 18 cm² y un lado de 3 cm?", "3 cm por 6 cm", "3 × 6 = 18."),
        ex("¿El área cambia si se intercambian el largo y el ancho?", "No", "Largo × ancho es igual que ancho × largo."),
    ],
    open_task=task(
        "Elige un área de la lista: 12 cm², 16 cm² o 20 cm². Dibuja en papel cuadriculado, o describe con medidas, tres rectángulos distintos con esa área. Escribe la multiplicación de cada uno. Si tienes un programa de geometría, puedes comprobar arrastrando los lados.",
        "Área 12 cm²: 1 × 12, 2 × 6 y 3 × 4.",
        ["elige un área de la lista", "propone tres rectángulos distintos", "escribe las multiplicaciones", "comprueba que todas den el mismo producto"],
        ["tres medidas", "tres multiplicaciones"],
        ["repetir el mismo rectángulo girado", "usar sumas en vez de productos"],
        "Pide explicar por qué las formas son distintas pero el área es igual. Reconoce que compare con un dibujo.",
    ),
    reinforce="Corta en un papel cuadriculado dos rectángulos de forma distinta con 12 cuadrados. Cuéntalos para comprobar.",
    extend="Busca todos los rectángulos de medidas enteras que tengan 24 cm² y ordénalos de más largo a más corto.",
)

# ================================================================ OA 24
register(
    OA24, 1,
    materials="Cubos de juego del mismo tamaño o cuadraditos de papel doblados como cubos, si los tienes. Los ejercicios describen todo con números.",
    use="Aprenderé qué es el volumen y cómo elegir un cubo como unidad para medirlo. Sirve para saber cuánto espacio ocupa una caja o una construcción.",
    prior=["Sé qué es un cubo.", "Sé contar y multiplicar con números pequeños."],
    explain=[
        "El volumen es cuánto espacio ocupa un cuerpo, por ejemplo una caja o una construcción de bloques. Se mide con una unidad que también ocupa espacio: un cubo pequeño, llamado unidad cúbica.",
        "Para medir bien, elige una unidad que sea siempre el mismo cubo, que se pueda apilar sin dejar huecos y que sea más pequeña que el cuerpo. Si usas cubos de distinto tamaño, no puedes comparar. Y no sirve usar una esfera, porque deja huecos al apilarla.",
        "Si un cuerpo se llena con 12 cubos iguales, su volumen es de 12 unidades cúbicas. Si otro cuerpo se llena con 20 cubos iguales, tiene más volumen. El número solo tiene sentido si se dice cuál cubo se usó.",
    ],
    vocab=[("volumen", "cantidad de espacio que ocupa un cuerpo"), ("unidad cúbica", "cubo pequeño que se usa para medir volumen"), ("cuerpo", "objeto con largo, ancho y alto, como una caja"), ("apilar", "poner cubos unos sobre otros")],
    worked=[
        {"title": "Elegir una buena unidad", "problem": "Quieres medir el volumen de una caja de zapatos. ¿Sirven mejor cubos iguales pequeños o pelotas?", "steps": ["Los cubos iguales se apilan sin dejar huecos.", "Las pelotas dejan huecos entre ellas."], "answer": "Sirven los cubos iguales"},
        {"title": "Contar y comparar", "problem": "Una caja se llena con 24 cubos y otra con 30 cubos del mismo tamaño. ¿Cuál tiene más volumen?", "steps": ["Comparo 24 y 30.", "30 es mayor."], "answer": "La segunda caja tiene más volumen"},
    ],
    mistakes=[
        {"wrong": "Medir volumen con cubos de distintos tamaños.", "why": "El conteo no se puede comparar si las unidades no son iguales.", "fix": "Usa siempre cubos del mismo tamaño."},
        {"wrong": "Pensar que el cuerpo más alto siempre tiene más volumen.", "why": "Se mira solo una medida.", "fix": "Cuenta todos los cubos que lo llenan."},
    ],
    tiers={
        "recovery": [
            ex("¿El volumen mide la superficie de una hoja o el espacio que ocupa un cuerpo?", "El espacio que ocupa un cuerpo", "El volumen es el espacio que ocupa algo."),
            ex("¿Qué forma tiene la unidad que se usa para medir volumen?", "Un cubo", "Los cubos se apilan sin dejar huecos."),
            ex("Una caja se llena con 15 cubos iguales. ¿Cuál es su volumen?", "15 cubos", "Se cuenta cuántos cubos caben."),
        ],
        "understand": [
            ex("¿Por qué no sirven pelotas para medir volumen?", "Porque dejan huecos al juntarlas", "Los huecos hacen que el conteo no cubra todo el espacio."),
            ex("Para medir con cubos, ¿deben ser todos del mismo tamaño o pueden ser distintos?", "Del mismo tamaño", "Así cada cubo vale lo mismo."),
            ex("Un cuerpo A se llena con 18 cubos y un cuerpo B con 12 cubos iguales. ¿Cuál ocupa más espacio?", "El cuerpo A", "18 es mayor que 12."),
        ],
        "apply": [
            ex("Una caja se llena con 4 cubos a lo largo, 3 a lo ancho y 1 de alto. ¿Cuántos cubos caben?", "12", "4 × 3 × 1 = 12.", calc="4*3*1"),
            ex("Un cuerpo A necesita 20 cubos y un cuerpo B necesita 25 cubos del mismo tamaño. ¿Cuántos cubos más necesita B?", "5", "25 − 20 = 5.", calc="25-20"),
            ex("Dos cajas se llenan con 10 cubos del mismo tamaño cada una. ¿Cuál tiene más volumen?", "Ninguna; tienen el mismo volumen", "10 es igual a 10."),
        ],
        "reason": [
            ex("Luis dice que un cuerpo alto siempre tiene más volumen que uno bajo. Si el cuerpo alto usa 12 cubos y el bajo usa 18, ¿tiene razón?", "No; el bajo tiene más volumen", "18 es mayor que 12."),
            ex("Una caja se midió con cubos grandes y otra con cubos chicos, y las dos dieron 10. ¿Se puede decir que tienen el mismo volumen? Explica.", "No; los cubos son de tamaños distintos", "Para comparar, los cubos deben ser iguales."),
        ],
        "challenge": [
            ex("Un cuerpo se llena con 2 cubos por fila, 2 filas y 3 capas. ¿Cuántos cubos usa?", "12", "2 × 2 × 3 = 12.", calc="2*2*3"),
            ex("Si cada cubo ocupa 1 unidad cúbica, ¿cuántas unidades cúbicas ocupa un cuerpo de 9 cubos?", "9 unidades cúbicas", "Cada cubo vale 1 unidad cúbica."),
        ],
    },
    context=[ex("Un niño arma una torre con 5 cubos en la base y dos pisos más de 5 cubos cada uno. ¿Cuántos cubos usa en total?", "15 cubos", "Son 3 pisos de 5 cubos: 3 × 5.", calc="3*5")],
    selfcheck=[
        ex("En Matemática: ¿Qué mide el volumen?", "El espacio que ocupa un cuerpo", "Es la cantidad de espacio de un objeto."),
        ex("¿Qué unidad usas para medir volumen: cuadrados o cubos?", "Cubos", "Los cubos ocupan espacio en las tres direcciones."),
        ex("Un cuerpo se llena con 30 cubos. Otro con 28 cubos iguales. ¿Cuál tiene más volumen?", "El de 30 cubos", "30 es mayor que 28."),
    ],
    open_task=task(
        "Elige una de estas tres cajas ficticias: A llena con 8 cubos, B llena con 12 cubos, C llena con 6 cubos. Ordénalas de menor a mayor volumen y explica cómo lo decidiste. Si tienes cubos de juego, arma cada una y comprueba.",
        "C (6) < A (8) < B (12). Comparé cuántos cubos iguales caben en cada una.",
        ["ordena las tres cajas según el número de cubos", "habla de cubos iguales", "explica la comparación", "usa la palabra volumen"],
        ["orden escrito", "explicación"],
        ["pensar que más alto es más volumen", "ordenar al revés"],
        "Pide que diga por qué los cubos deben ser iguales. Reconoce que use la palabra volumen.",
    ),
    reinforce="Con cubos de juego o bloques, llena una cajita y cuenta cuántos usaste.",
    extend="Explica por qué no podrías medir el volumen de una caja con cubos de dos tamaños mezclados.",
)
