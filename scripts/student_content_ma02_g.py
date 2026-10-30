"""Student material for 2.º básico Matemática, OA 15 (figuras 2D) y OA 16 (figuras 3D)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA15, OA16 = "MA02 OA 15", "MA02 OA 16"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 15
register(
    OA15, 1,
    materials="Lápiz, regla y papel. Si quieres, palitos de helado o fósforos sin cabeza para armar las figuras. Todos los datos están escritos en cada ejercicio.",
    use="Aprenderé a describir figuras por sus lados y sus vértices. Sirve para reconocer un triángulo o un cuadrado aunque esté girado.",
    prior=["Reconozco triángulos, cuadrados, rectángulos y círculos por su forma.", "Sé contar hasta 20."],
    explain=[
        "Una figura 2D es plana, como un dibujo en una hoja. Sus bordes rectos se llaman lados. El punto donde se juntan dos lados se llama vértice. Un vértice es como una esquina de la figura.",
        "El triángulo tiene 3 lados y 3 vértices. El cuadrado y el rectángulo tienen 4 lados y 4 vértices. En estas figuras cerradas siempre hay tantos vértices como lados.",
        "Si giras una figura, sigue siendo la misma. Un triángulo con la punta hacia abajo tiene 3 lados y 3 vértices, igual que uno con la punta hacia arriba. Para saber qué figura es, cuenta sus lados y sus vértices.",
    ],
    vocab=[("figura 2D", "figura plana, como un dibujo en el papel"), ("lado", "borde recto de una figura"), ("vértice", "punto donde se juntan dos lados"), ("triángulo", "figura de 3 lados y 3 vértices"), ("cuadrado y rectángulo", "figuras de 4 lados y 4 vértices")],
    worked=[
        {"title": "Contar lados y vértices", "problem": "Una figura tiene 3 lados rectos. ¿Cuántos vértices tiene y cómo se llama?", "steps": ["Cada vértice está donde se juntan dos lados.", "En una figura cerrada hay tantos vértices como lados.", "Si hay 3 lados, hay 3 vértices.", "Una figura de 3 lados se llama triángulo."], "answer": "3 vértices; es un triángulo"},
        {"title": "Figura girada", "problem": "Un triángulo está apoyado sobre una de sus puntas, con un lado hacia arriba. ¿Sigue siendo triángulo?", "steps": ["Cuento sus lados: 3 lados rectos.", "Cuento sus vértices: 3 puntos donde se juntan los lados.", "Girar una figura no cambia sus lados ni sus vértices.", "Sigue siendo un triángulo."], "answer": "Sí, sigue siendo un triángulo"},
    ],
    mistakes=[
        {"wrong": "Decir que un triángulo con la punta hacia abajo no es triángulo.", "why": "Se reconoce la figura sólo cuando está en la posición de siempre.", "fix": "Cuenta los lados y los vértices: si son 3, es un triángulo en cualquier posición."},
        {"wrong": "Contar un vértice por cada lado y quedarse con 8 vértices en un cuadrado.", "why": "Se cuentan dos veces las esquinas donde se juntan los lados.", "fix": "Marca cada esquina con un punto una sola vez y cuenta los puntos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos lados tiene un triángulo?", "3", "El triángulo tiene tres bordes rectos."),
            ex("¿Cuántos vértices tiene un cuadrado?", "4", "Un cuadrado tiene cuatro esquinas, que son sus vértices."),
            ex("Una figura tiene 3 vértices. ¿Es un triángulo o un cuadrado?", "Un triángulo", "Tres vértices significan tres lados, y eso es un triángulo."),
        ],
        "understand": [
            ex("¿Qué es un vértice?", "El punto donde se juntan dos lados", "Un vértice es una esquina de la figura."),
            ex("¿Cuántos lados tiene un rectángulo?", "4", "El rectángulo tiene cuatro bordes rectos."),
            arith("¿Cuántos lados más tiene un rectángulo que un triángulo?", "4-3", "El rectángulo tiene 4 lados y el triángulo 3."),
        ],
        "apply": [
            ex("Una figura tiene 4 lados rectos, 4 vértices y esquinas rectas. Escribe los dos nombres que puede tener.", "Cuadrado o rectángulo", "Las dos figuras tienen cuatro lados y cuatro vértices."),
            arith("Un triángulo y un cuadrado están dibujados juntos. ¿Cuántos vértices hay en total?", "3+4", "El triángulo aporta 3 vértices y el cuadrado 4."),
            arith("Dibujas dos triángulos y un rectángulo. ¿Cuántos lados dibujaste en total?", "3+3+4", "Cada triángulo tiene 3 lados y el rectángulo tiene 4."),
        ],
        "reason": [
            ex("Lía dice que un triángulo con la punta hacia abajo ya no es triángulo. ¿Tiene razón? Explica.", "No; sigue teniendo 3 lados y 3 vértices", "Girar una figura no cambia sus lados ni sus vértices."),
            ex("Tomás dibujó una figura cerrada con 5 lados rectos y dice que tiene 4 vértices. ¿Es posible?", "No; tendría 5 vértices", "En una figura cerrada hay tantos vértices como lados."),
        ],
        "challenge": [
            ex("Tienes 7 palitos iguales. Quieres armar un triángulo y un cuadrado, usando todos y sin que sobre ninguno. ¿Cuántos palitos usa cada figura?", "3 para el triángulo y 4 para el cuadrado", "Cada palito es un lado: 3 + 4 = 7."),
            ex("Tienes 10 palitos iguales. Arma sólo triángulos y cuadrados, usando todos los palitos. ¿Cuántos triángulos y cuántos cuadrados hacen?", "2 triángulos y 1 cuadrado", "Dos triángulos usan 6 palitos y un cuadrado usa 4: 6 + 4 = 10."),
        ],
    },
    context=[arith("Pedro dibuja una casa con un cuadrado de pared y un triángulo de techo. ¿Cuántos lados dibujó en total?", "4+3", "La pared tiene 4 lados y el techo tiene 3.")],
    selfcheck=[
        ex("¿Cuántos vértices tiene un triángulo?", "3", "Tiene una esquina entre cada par de lados, y son tres."),
        ex("¿Cómo se llama la figura de 4 lados iguales y esquinas rectas?", "Cuadrado", "El cuadrado tiene los cuatro lados iguales."),
        ex("Una figura gira. ¿Cambia el número de sus lados?", "No", "Girar mueve la figura pero no cambia sus lados."),
    ],
    open_task=task(
        "Con regla, dibuja tres triángulos: uno con la punta hacia arriba, otro con la punta hacia abajo y otro apoyado de lado. Marca con un punto cada vértice y escribe cuántos lados y cuántos vértices tiene cada uno.",
        "Triángulo 1 (punta arriba): 3 lados y 3 vértices. Triángulo 2 (punta abajo): 3 lados y 3 vértices. Triángulo 3 (de lado): 3 lados y 3 vértices. Aunque giran, el número no cambia.",
        ["dibuja tres triángulos en posiciones distintas", "marca los tres vértices de cada uno", "escribe 3 lados y 3 vértices", "explica que girar no cambia el número"],
        ["dibujos con vértices marcados", "números escritos", "explicación"],
        ["marcar más de 3 puntos", "decir que el triángulo girado es otra figura"],
        "Pide contar en voz alta los lados tocando cada uno. Reconoce cuando explica que la figura es la misma aunque gire.",
    ),
    reinforce="Camina por tu casa y busca tres objetos con forma de rectángulo. Cuenta sus lados y sus esquinas.",
    extend="Dibuja una figura de 4 lados que no sea cuadrado y cuenta sus vértices. Explica cómo sabes que son 4.",
)

register(
    OA15, 2,
    materials="Lápiz, regla y papel. Los largos de los lados están escritos en cada ejercicio, en centímetros (cm).",
    use="Aprenderé a comparar cuadrados y rectángulos usando el largo de sus lados. Sirve para decidir qué figura es cuando miro sus medidas.",
    prior=["Sé que el cuadrado y el rectángulo tienen 4 lados y 4 vértices.", "Sé leer medidas en centímetros."],
    explain=[
        "El cuadrado y el rectángulo se parecen mucho. Los dos tienen 4 lados y 4 esquinas rectas. Para distinguirlos hay que mirar el largo de sus lados.",
        "En un cuadrado, los cuatro lados miden lo mismo. Por ejemplo, 5 cm, 5 cm, 5 cm y 5 cm. En un rectángulo hay dos lados largos que miden lo mismo y dos lados cortos que miden lo mismo. Por ejemplo, 8 cm, 3 cm, 8 cm y 3 cm.",
        "Un cuadrado sigue siendo cuadrado aunque lo gires o lo hagas más grande o más chico. Lo que importa es que sus cuatro lados sean iguales y sus esquinas sean rectas.",
    ],
    vocab=[("lados iguales", "lados que miden lo mismo"), ("lado largo", "el lado más extenso de un rectángulo"), ("lado corto", "el lado menos extenso de un rectángulo"), ("esquina recta", "vértice que forma una esquina como la de una hoja"), ("cuadrado", "4 lados iguales y 4 esquinas rectas")],
    worked=[
        {"title": "Reconocer un cuadrado", "problem": "Una figura de 4 esquinas rectas tiene lados de 6 cm, 6 cm, 6 cm y 6 cm. ¿Qué figura es?", "steps": ["Miro el largo de los cuatro lados.", "Los cuatro miden 6 cm: son iguales.", "Cuatro lados iguales y esquinas rectas forman un cuadrado."], "answer": "Un cuadrado"},
        {"title": "Reconocer un rectángulo", "problem": "Una figura de 4 esquinas rectas tiene lados de 9 cm, 4 cm, 9 cm y 4 cm. ¿Qué figura es?", "steps": ["Comparo los lados: 9 cm y 4 cm son distintos.", "Los dos lados de 9 cm son iguales entre sí.", "Los dos lados de 4 cm también son iguales entre sí.", "Eso es un rectángulo."], "answer": "Un rectángulo"},
    ],
    mistakes=[
        {"wrong": "Decir que una figura con lados de 7 cm, 2 cm, 7 cm y 2 cm es un cuadrado.", "why": "Sólo se cuentan los lados y no se comparan sus largos.", "fix": "Un cuadrado necesita los cuatro lados iguales; aquí hay dos largos y dos cortos."},
        {"wrong": "Decir que un cuadrado girado ya no es cuadrado.", "why": "Se confunde la posición con la forma.", "fix": "Mide sus lados: si siguen siendo iguales, es un cuadrado en cualquier posición."},
    ],
    tiers={
        "recovery": [
            ex("Una figura de 4 esquinas rectas mide 4 cm, 4 cm, 4 cm y 4 cm. ¿Es cuadrado o rectángulo?", "Cuadrado", "Sus cuatro lados miden lo mismo."),
            ex("Una figura de 4 esquinas rectas mide 10 cm, 5 cm, 10 cm y 5 cm. ¿Es cuadrado o rectángulo?", "Rectángulo", "Tiene dos lados largos y dos cortos."),
            ex("¿Cuántos lados iguales tiene un cuadrado?", "4", "Todos sus lados miden lo mismo."),
        ],
        "understand": [
            ex("¿En qué se parecen el cuadrado y el rectángulo?", "Los dos tienen 4 lados y 4 esquinas rectas", "Ambos son figuras de cuatro lados con esquinas rectas."),
            ex("¿En qué se diferencian el cuadrado y el rectángulo?", "El cuadrado tiene los 4 lados iguales; el rectángulo tiene lados largos y cortos", "Se distinguen por el largo de los lados."),
            ex("Un rectángulo tiene un lado de 8 cm. ¿Cuánto mide el lado de enfrente, que es su pareja?", "8 cm", "Los lados que se enfrentan miden lo mismo."),
        ],
        "apply": [
            ex("Un rectángulo mide 12 cm de largo y 5 cm de ancho. Escribe los cuatro lados en orden.", "12 cm, 5 cm, 12 cm y 5 cm", "Los lados que se enfrentan son iguales."),
            ex("Un cuadrado tiene un lado de 9 cm. ¿Cuánto miden los otros tres lados?", "9 cm cada uno", "En el cuadrado todos los lados son iguales."),
            ex("Tienes cuatro palitos: 6 cm, 6 cm, 6 cm y 6 cm. ¿Qué figura de esquinas rectas puedes armar?", "Un cuadrado", "Los cuatro palitos miden lo mismo."),
        ],
        "reason": [
            ex("Un cuadrado está apoyado sobre una de sus esquinas. Ana dice que ahora es otra figura. ¿Está bien?", "No; sigue siendo cuadrado", "Girar no cambia que sus cuatro lados sean iguales."),
            ex("Beto dice que una figura de lados 5 cm, 5 cm, 5 cm y 8 cm es un cuadrado. ¿Qué error comete?", "Un lado mide distinto; no tiene los 4 lados iguales", "El cuadrado necesita cuatro lados iguales."),
        ],
        "challenge": [
            ex("Tienes 2 palitos de 7 cm y 2 palitos de 3 cm. Con los cuatro armas una figura de esquinas rectas. ¿Cuál es?", "Un rectángulo", "Hay dos lados largos iguales y dos cortos iguales."),
            ex("Tienes 8 palitos de 5 cm cada uno. ¿Cuántos cuadrados de lado 5 cm puedes armar con todos ellos?", "2 cuadrados", "Cada cuadrado necesita 4 palitos: 4 + 4 = 8, así que se arman 2 cuadrados."),
        ],
    },
    context=[ex("Una tarjeta de cumpleaños mide 15 cm de largo y 10 cm de ancho, con esquinas rectas. ¿Es cuadrada o rectangular?", "Rectangular", "Sus lados miden 15 cm y 10 cm, que no son iguales.")],
    selfcheck=[
        ex("¿Cuál figura tiene los 4 lados iguales?", "El cuadrado", "Por eso se distingue del rectángulo."),
        ex("Una figura de 4 esquinas rectas mide 3 cm, 6 cm, 3 cm y 6 cm. ¿Qué es?", "Rectángulo", "Tiene dos pares de lados iguales."),
        ex("Un rectángulo mide 20 cm de largo. ¿Cuánto mide el lado largo que está enfrente?", "20 cm", "Los lados largos son iguales."),
    ],
    open_task=task(
        "Con regla, dibuja un cuadrado de 4 cm de lado y un rectángulo de 6 cm de largo por 3 cm de ancho. Escribe cuánto mide cada lado de las dos figuras. Luego gira la hoja y explica por qué el cuadrado sigue siendo cuadrado.",
        "Cuadrado: 4 cm, 4 cm, 4 cm y 4 cm. Rectángulo: 6 cm, 3 cm, 6 cm y 3 cm. Al girar la hoja, el cuadrado tiene los mismos cuatro lados iguales, por eso sigue siendo cuadrado.",
        ["dibuja las dos figuras con las medidas pedidas", "escribe los cuatro lados de cada una", "esquinas rectas", "explica con lados iguales"],
        ["dibujos medidos", "medidas escritas", "explicación"],
        ["lados desiguales en el cuadrado", "decir que girar cambia la figura"],
        "Pide medir cada lado con la regla antes de decidir. Reconoce que use lados iguales para explicar.",
    ),
    reinforce="Busca una hoja de cuaderno y un posavasos o tarjeta cuadrada. Mide sus lados y di cuál es cuadrado y cuál rectángulo.",
    extend="Dibuja tres rectángulos distintos que tengan un lado de 4 cm. Anota las medidas de todos sus lados.",
)

register(
    OA15, 3,
    materials="Lápiz y papel. Si quieres, un plato, una moneda, un trozo de lana y una tarjeta. Las descripciones están escritas en cada ejercicio.",
    use="Aprenderé a distinguir los bordes curvos de los lados rectos. Sirve para reconocer el círculo y diferenciarlo de las figuras con lados.",
    prior=["Sé que un lado es un borde recto.", "Sé contar los vértices de un cuadrado y de un triángulo."],
    explain=[
        "El círculo es una figura plana con un borde curvo. Su borde es una línea redonda que da la vuelta completa. No tiene lados rectos ni vértices, porque no tiene esquinas.",
        "Una moneda, una tapa y una galleta redonda tienen forma de círculo. Si pasas el dedo por el borde de un círculo, nunca sientes una esquina. En cambio, si lo haces en un cuadrado, sientes cuatro esquinas.",
        "Una figura con muchos lados rectos puede parecer redonda de lejos. Pero si tiene lados y vértices, no es un círculo. Para decidir, revisa el borde: ¿es curvo y continuo o tiene lados rectos?",
    ],
    vocab=[("círculo", "figura plana con borde curvo y sin vértices"), ("borde curvo", "línea redonda sin esquinas"), ("lado recto", "borde que no se curva"), ("vértice", "esquina donde se juntan dos lados"), ("continuo", "que sigue sin cortes ni esquinas")],
    worked=[
        {"title": "Elegir el círculo", "problem": "Hay tres figuras. La A tiene 4 lados rectos. La B tiene 3 lados rectos. La C tiene un borde curvo sin esquinas. ¿Cuál es el círculo?", "steps": ["Busco la figura sin lados rectos.", "La A tiene lados y vértices, la B también.", "La C tiene un borde curvo y no tiene esquinas."], "answer": "La figura C"},
        {"title": "Una figura engañosa", "problem": "Una figura parece redonda, pero tiene 6 lados rectos pequeños y 6 vértices. ¿Es un círculo?", "steps": ["Reviso su borde: tiene lados rectos.", "Un círculo no tiene lados rectos ni vértices.", "Esta figura tiene 6 lados y 6 vértices."], "answer": "No, no es un círculo"},
    ],
    mistakes=[
        {"wrong": "Decir que el círculo tiene 1 lado y 1 vértice.", "why": "Se piensa que todas las figuras tienen lados rectos y esquinas.", "fix": "El círculo tiene un borde curvo; no tiene lados rectos ni vértices."},
        {"wrong": "Llamar círculo a una figura de muchos lados rectos porque parece redonda.", "why": "Se decide por la apariencia y no por el borde.", "fix": "Revisa el borde: si hay lados rectos y esquinas, no es un círculo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos vértices tiene un círculo?", "0", "Su borde es curvo y no tiene esquinas."),
            ex("¿Cuál de estas figuras tiene un borde curvo: cuadrado, círculo o triángulo?", "El círculo", "Sólo el círculo tiene un borde redondo."),
            ex("¿Una moneda tiene forma de círculo o de rectángulo?", "De círculo", "El borde de una moneda es redondo y sin esquinas."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre el borde de un círculo y el de un cuadrado?", "El círculo tiene borde curvo; el cuadrado tiene lados rectos", "Una línea es curva y las otras son rectas."),
            ex("¿Cuántos lados rectos tiene un círculo?", "0", "Todo su borde es curvo."),
            arith("Un triángulo tiene 3 vértices y un círculo tiene 0. ¿Cuántos vértices hay entre las dos figuras?", "3+0", "El círculo no aporta vértices."),
        ],
        "apply": [
            ex("Tres figuras: A tiene 5 lados rectos, B tiene un borde curvo sin esquinas, C tiene 4 lados iguales. ¿Cuál es el círculo?", "La B", "Es la única sin lados rectos ni esquinas."),
            ex("Una galleta redonda, una ventana cuadrada, una tapa de frasco y una hoja rectangular. ¿Cuántos objetos tienen forma de círculo?", "2", "La galleta y la tapa tienen borde curvo."),
            ex("Sigues con el dedo el borde de una figura y no sientes ninguna esquina. ¿Qué figura puede ser?", "Un círculo", "Sin esquinas hay un borde curvo continuo."),
        ],
        "reason": [
            ex("Sofía dice que una figura con 8 lados rectos pequeños es un círculo porque parece redonda. ¿Qué le responderías?", "No lo es; tiene lados rectos y vértices", "Un círculo tiene el borde curvo y sin esquinas."),
            ex("Mario dice que el círculo es la única figura de esta lección sin vértices. ¿Tiene razón?", "Sí", "El triángulo, el cuadrado y el rectángulo tienen vértices."),
        ],
        "challenge": [
            ex("Una figura tiene borde curvo. Otra tiene 3 lados. Otra tiene 4 lados iguales. Ordénalas de menos a más vértices.", "Círculo (0), triángulo (3), cuadrado (4)", "Se ordenan 0, 3 y 4 vértices."),
            ex("Dibujas un círculo y un rectángulo. Cuentas todas las esquinas de los dos. ¿Cuántas son?", "4", "El círculo tiene 0 y el rectángulo tiene 4."),
        ],
    },
    context=[ex("En una mesa hay una pizza redonda, una caja de pizza cuadrada y un pañuelo triangular. ¿Cuál tiene el borde curvo?", "La pizza", "La pizza redonda tiene el borde sin esquinas.")],
    selfcheck=[
        ex("¿Cómo es el borde de un círculo?", "Curvo y sin esquinas", "No tiene lados rectos."),
        ex("¿Un cuadrado tiene borde curvo?", "No", "Sus cuatro lados son rectos."),
        ex("¿Un círculo tiene esquinas en su borde?", "No", "Su borde curvo no tiene vértices."),
    ],
    open_task=task(
        "Mira estas cuatro figuras: A tiene 3 lados rectos, B tiene un borde curvo, C tiene 4 lados iguales y D tiene 4 lados de dos medidas. Escribe cuál es círculo, cuál es triángulo, cuál es cuadrado y cuál es rectángulo. Explica tu decisión sobre B mirando el borde.",
        "A es triángulo, B es círculo, C es cuadrado y D es rectángulo. B es círculo porque su borde es curvo y no tiene lados rectos ni vértices.",
        ["nombra bien las cuatro figuras", "explica B con el borde curvo", "menciona que no tiene vértices"],
        ["cuatro nombres", "explicación escrita"],
        ["decir que el círculo tiene un lado", "decidir sólo por la apariencia"],
        "Pide recorrer con el dedo cada borde. Reconoce cuando nombra el borde curvo como la razón.",
    ),
    reinforce="Con lana, forma un círculo y luego un triángulo sobre la mesa. Cuenta las esquinas de cada uno.",
    extend="Haz una lista de cinco cosas de tu casa con borde curvo y cinco con lados rectos.",
)

register(
    OA15, 4,
    materials="Lápiz, regla y papel. Si quieres, palitos de helado de distintos largos. Los largos disponibles están escritos en cada ejercicio.",
    use="Aprenderé a construir figuras que cumplan condiciones dadas, como cuántos lados tienen o cómo son sus lados. Sirve para crear y comprobar figuras.",
    prior=["Sé contar lados y vértices.", "Sé comparar cuadrados, rectángulos y círculos."],
    explain=[
        "Construir una figura es armarla con material concreto, como palitos, lana o papel. Las condiciones dicen cómo debe ser: cuántos lados tiene o si sus lados son iguales o distintos.",
        "Para cumplir las condiciones, primero léelas una por una. Después arma la figura y comprueba cada condición. Por ejemplo, si pide 4 lados, dos largos y dos cortos, armas un rectángulo y revisas que tenga 4 lados.",
        "Una misma condición se puede cumplir de más de una manera. Un triángulo puede estar apoyado en un lado o en una punta. Lo importante es que la figura cumpla todo lo que se pide.",
    ],
    vocab=[("construir", "armar una figura con material"), ("condición", "algo que la figura debe cumplir"), ("comprobar", "revisar que se cumple lo pedido"), ("palito", "tira recta que sirve de lado"), ("cerrada", "figura sin partes abiertas")],
    worked=[
        {"title": "Construir con condiciones", "problem": "Construye una figura cerrada con 4 lados: dos de 8 cm y dos de 3 cm. Tienes palitos de 8 cm y de 3 cm.", "steps": ["Elijo 2 palitos de 8 cm y 2 de 3 cm.", "Los uno de modo que los iguales queden enfrentados y las esquinas sean rectas.", "Compruebo: 4 lados, dos largos y dos cortos."], "answer": "Un rectángulo de 8 cm por 3 cm"},
        {"title": "Una figura girada", "problem": "Construye un triángulo que no tenga un lado horizontal apoyado abajo.", "steps": ["Uno 3 palitos formando una figura cerrada.", "Giro el triángulo hasta que quede apoyado en una punta.", "Cuento 3 lados y 3 vértices: se cumple."], "answer": "Un triángulo apoyado en una punta"},
    ],
    mistakes=[
        {"wrong": "Armar una figura con un hueco entre dos palitos.", "why": "La figura quedó abierta y no se comprobó.", "fix": "Revisa que cada palito toque al siguiente en un vértice."},
        {"wrong": "Cumplir sólo una condición y olvidar las demás.", "why": "No se lee la lista completa.", "fix": "Marca con un visto cada condición cumplida."},
    ],
    tiers={
        "recovery": [
            ex("Tienes 3 palitos del mismo largo. ¿Qué figura cerrada puedes armar?", "Un triángulo", "Tres lados forman un triángulo."),
            ex("Tienes 4 palitos de 5 cm cada uno. ¿Qué figura de esquinas rectas puedes armar?", "Un cuadrado", "Cuatro lados iguales forman un cuadrado."),
            ex("Quieres una figura sin lados rectos y sin vértices. ¿Cuál construyes?", "Un círculo", "Es la figura de borde curvo."),
        ],
        "understand": [
            ex("¿Qué debes hacer después de armar una figura?", "Comprobar cada condición pedida", "Así sabes que cumple lo que se pidió."),
            ex("Una condición dice «4 lados iguales». ¿Qué figura sirve?", "El cuadrado", "El cuadrado tiene los cuatro lados iguales."),
            ex("Una figura queda con un hueco entre dos palitos. ¿Está cerrada?", "No", "Los palitos deben tocarse en los vértices."),
        ],
        "apply": [
            ex("Tienes palitos de 9 cm, 9 cm, 4 cm y 4 cm. Construye una figura de 4 lados con dos largos y dos cortos. ¿Qué figura es y cuánto mide cada lado?", "Un rectángulo con lados de 9 cm, 4 cm, 9 cm y 4 cm", "Los lados largos son iguales y los cortos también."),
            ex("Tienes 5 palitos iguales. Quieres armar un cuadrado. ¿Cuántos palitos sobran?", "1", "El cuadrado usa 4 palitos: 5 − 4 = 1."),
            arith("Quieres armar un triángulo y un cuadrado con palitos. ¿Cuántos palitos necesitas?", "3+4", "El triángulo usa 3 y el cuadrado usa 4."),
        ],
        "reason": [
            ex("Pedro armó una figura con 3 palitos de 4 cm, 4 cm y 4 cm. Dice que es un cuadrado. ¿Qué error cometió?", "Sólo tiene 3 lados; es un triángulo", "El cuadrado necesita 4 lados."),
            ex("Rita dice que para hacer un triángulo siempre debe haber un lado abajo, apoyado en el suelo. ¿Está bien?", "No; puede estar girado", "Un triángulo girado conserva 3 lados y 3 vértices."),
        ],
        "challenge": [
            ex("Tienes 2 palitos de 10 cm, 2 de 6 cm y 2 de 4 cm. Quieres armar un rectángulo que use los dos palitos más largos y los dos más cortos. ¿Qué medidas tiene?", "10 cm, 4 cm, 10 cm y 4 cm", "Los más largos miden 10 cm y los más cortos 4 cm."),
            ex("Hay que construir una figura cerrada con 3 lados que quede apoyada sólo en una de sus puntas. ¿Cuántos vértices tiene y cuántos tocan el suelo?", "3 vértices; 1 toca el suelo", "Es un triángulo girado y apoya una sola punta."),
        ],
    },
    context=[ex("Para un marco de foto cuadrado tienes 4 tiras de cartón de 12 cm cada una. ¿Cuántas tiras sobran si usas todas las que necesitas?", "0", "El marco cuadrado necesita 4 tiras y tienes 4.")],
    selfcheck=[
        ex("¿Cuántos palitos necesitas para armar un rectángulo?", "4", "Un rectángulo tiene 4 lados."),
        ex("¿Qué palitos necesitas para un cuadrado: 4 iguales o 4 distintos?", "4 iguales", "El cuadrado tiene los lados iguales."),
        ex("¿Qué haces cuando terminas de armar la figura?", "Compruebo las condiciones", "Se revisa que se cumpla todo lo pedido."),
    ],
    open_task=task(
        "Tienes 6 palitos de 6 cm y 4 palitos de 3 cm. Construye o dibuja primero un cuadrado de 6 cm de lado y luego un rectángulo de 6 cm por 3 cm. Anota cuántos palitos usó cada figura, cuántos vértices tienen y qué condición cumple cada una.",
        "Cuadrado: 4 palitos de 6 cm, 4 vértices y 4 lados iguales. Rectángulo: 2 palitos de 6 cm y 2 de 3 cm, 4 vértices, dos lados largos y dos cortos. Sobran 2 palitos de 3 cm.",
        ["arma o dibuja las dos figuras", "cuenta palitos y vértices", "nombra la condición que cumple cada figura", "figuras cerradas"],
        ["figuras construidas o dibujadas", "conteos escritos", "explicación"],
        ["dejar huecos entre los palitos", "usar lados desiguales en el cuadrado"],
        "Pide leer las condiciones y marcar cuál cumplió cada figura. Reconoce las comprobaciones.",
    ),
    reinforce="Con 12 palitos o lápices iguales, arma tres cuadrados. Cuenta cuántos lados armaste en total.",
    extend="Escribe tres condiciones para que tu compañero construya una figura. Después arma tú la figura para comprobar que se puede.",
)

# ================================================================ OA 16
register(
    OA16, 1,
    materials="Una caja pequeña, una pelota o fruta redonda, un cubo (dado), un gorro de cumpleaños de cartón y un libro grande como rampa. Los resultados de la tabla están escritos en el cuaderno.",
    use="Aprenderé cómo la forma de un cuerpo cambia lo que hace: rodar, deslizar o apilar. Sirve para elegir el cuerpo adecuado para cada tarea.",
    prior=["Reconozco objetos redondos y objetos con esquinas.", "Sé comparar si algo rueda o no."],
    explain=[
        "Una figura 3D es un cuerpo que ocupa espacio, como un dado o una pelota. Tiene superficies. Una superficie plana se llama cara. Una superficie redondeada se llama superficie curva.",
        "Si apoyas un cuerpo en una rampa, puede rodar, deslizarse o quedarse quieto. La esfera tiene toda su superficie curva y por eso rueda para todos lados. El cubo y la caja tienen caras planas y se deslizan, pero no ruedan.",
        "El cono tiene una cara plana y una superficie curva. Rueda dando vueltas en círculo, porque tiene punta en un lado. Para apilar sirven los cuerpos con caras planas, como el cubo y la caja.",
    ],
    vocab=[("figura 3D", "cuerpo que ocupa espacio"), ("cara", "superficie plana de un cuerpo"), ("superficie curva", "superficie redondeada sin esquinas"), ("rodar", "avanzar dando vueltas"), ("apilar", "poner un cuerpo sobre otro")],
    worked=[
        {"title": "Leer una tabla", "problem": "En la rampa: la esfera rueda; el cubo se desliza; el cono rueda en círculo. ¿Cuál rueda para todos lados?", "steps": ["Miro qué cuerpo tiene toda su superficie curva.", "La esfera es completamente curva.", "Por eso rueda para cualquier lado."], "answer": "La esfera"},
        {"title": "Predecir y comprobar", "problem": "Una caja de zapatos tiene caras planas. Predice qué hará en la rampa.", "steps": ["Tiene 6 caras planas.", "Los cuerpos con caras planas no ruedan.", "Se desliza o se queda quieta."], "answer": "Se desliza, no rueda"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los cuerpos ruedan igual.", "why": "No se mira la superficie del cuerpo.", "fix": "Los que tienen superficie curva ruedan; los de caras planas se deslizan."},
        {"wrong": "Intentar apilar esferas una sobre otra y decir que se puede.", "why": "Se olvida que la superficie curva se mueve.", "fix": "Los cuerpos con caras planas se apilan mejor."},
    ],
    tiers={
        "recovery": [
            ex("¿Una pelota rueda o se desliza sin rodar?", "Rueda", "La pelota es una esfera y toda su superficie es curva."),
            ex("¿Un dado se puede apilar sobre otro dado?", "Sí", "Los dados tienen caras planas."),
            ex("¿Un dado rueda como una pelota?", "No", "Un dado tiene caras planas y esquinas."),
        ],
        "understand": [
            ex("¿Qué es una cara de un cuerpo?", "Una superficie plana", "Las caras son las partes planas del cuerpo."),
            ex("¿Qué cuerpo tiene toda su superficie curva?", "La esfera", "No tiene ninguna cara plana."),
            ex("¿Por qué una caja se desliza y no rueda?", "Porque tiene caras planas", "Las caras planas no giran como una superficie curva."),
        ],
        "apply": [
            ex("En la rampa, Ema probó: esfera, cubo y cono. Sólo uno rueda para todos lados. ¿Cuál es?", "La esfera", "La esfera tiene superficie curva completa."),
            ex("Quieres construir una torre con tres cuerpos. Tienes una esfera, un cubo y una caja rectangular. ¿Cuál no sirve para la base?", "La esfera", "Rueda y no se queda quieta."),
            ex("Empujas un cono tumbado sobre la mesa. ¿Qué movimiento hace?", "Rueda dando vueltas en círculo", "Tiene punta de un lado y base ancha del otro."),
        ],
        "reason": [
            ex("Pablo dice que el cono y la esfera ruedan exactamente igual. ¿Está bien?", "No; el cono rueda en círculo y la esfera para todos lados", "El cono tiene punta y una cara plana."),
            ex("Una caja se desliza en la rampa. Lola dice que es porque es pesada. ¿Qué razón es más correcta?", "Porque tiene caras planas", "La forma de la superficie decide si rueda."),
        ],
        "challenge": [
            ex("Quieres una torre de 3 pisos con un cubo, una caja rectangular y un cono con la punta hacia arriba. ¿Cuál debe ir arriba?", "El cono", "Sobre su punta no se apila nada, y el cubo y la caja sirven de base."),
            ex("Hay 4 cuerpos: esfera, cubo, caja y cono. ¿Cuántos de ellos tienen alguna superficie curva?", "2", "La esfera y el cono tienen superficie curva."),
        ],
    },
    context=[ex("En una caja de juguetes hay 3 pelotas, 2 dados y 1 gorro cónico. Quieres sacar los que ruedan para todos lados. ¿Cuántos son?", "3", "Las tres pelotas son esferas y ruedan para todos lados.")],
    selfcheck=[
        ex("¿Qué cuerpo se desliza en vez de rodar: la esfera o el cubo?", "El cubo", "Tiene caras planas."),
        ex("¿Qué cuerpo no se puede apilar bien: la esfera o la caja?", "La esfera", "Rueda y no queda firme."),
        ex("¿Qué es una superficie curva?", "Una superficie redondeada sin esquinas", "Se curva en vez de ser plana."),
    ],
    open_task=task(
        "Con una pelota, un dado y una caja, apoya cada uno en una rampa suave hecha con un libro. Antes de probar, escribe tu predicción: ¿rueda, se desliza o se queda quieto? Luego anota lo que pasó. Si no tienes un objeto, usa esta tabla de resultados: pelota rueda para todos lados, dado se desliza, caja se desliza.",
        "Predicción: pelota rueda, dado se desliza, caja se desliza. Resultado: pelota rueda para todos lados; dado y caja se deslizan. Porque la pelota tiene superficie curva y los otros caras planas.",
        ["escribe una predicción para cada cuerpo", "anota el resultado", "explica con superficie curva o caras planas"],
        ["tabla de predicciones y resultados", "explicación"],
        ["no escribir la predicción antes de probar", "decir que ruedan todos"],
        "Pide mostrar la rampa y repetir la prueba. Reconoce las predicciones que se comprueban.",
    ),
    reinforce="Prueba tres objetos de tu casa en una rampa suave y cuenta cuántos ruedan.",
    extend="Predice qué hará una naranja y qué hará una caja de fósforos cerrada en la rampa. Explica tu predicción.",
)

register(
    OA16, 2,
    materials="Un dado, una pelota, una caja y un gorro de cumpleaños de cartón (opcional). Los datos están escritos en cada ejercicio.",
    use="Aprenderé a describir los cuerpos por sus caras planas y sus superficies curvas. Sirve para que otra persona adivine qué cuerpo estoy mirando.",
    prior=["Sé qué es una cara plana y una superficie curva.", "Sé que algunos cuerpos ruedan y otros se deslizan."],
    explain=[
        "Para describir un cuerpo se cuentan sus caras planas y se mira si tiene superficie curva. El cubo tiene 6 caras planas, todas cuadradas. No tiene superficies curvas.",
        "La esfera no tiene ninguna cara plana. Toda su superficie es curva. El cono tiene 1 cara plana, que es un círculo, y 1 superficie curva. Además, tiene una punta.",
        "La caja con forma de ladrillo se llama paralelepípedo. Tiene 6 caras planas con forma de rectángulo. Para adivinar un cuerpo sin decir su nombre, usa pistas como estas: cuántas caras planas tiene y si tiene superficie curva.",
    ],
    vocab=[("cara plana", "parte plana de un cuerpo"), ("superficie curva", "parte redondeada de un cuerpo"), ("cubo", "cuerpo de 6 caras cuadradas iguales"), ("esfera", "cuerpo de una sola superficie curva"), ("cono", "cuerpo con una cara plana circular y una superficie curva")],
    worked=[
        {"title": "Describir un cuerpo", "problem": "Describe un cono sin decir su nombre.", "steps": ["Cuento sus caras planas: tiene 1 y es un círculo.", "Miro si tiene superficie curva: sí, 1.", "Tiene una punta."], "answer": "Tiene 1 cara plana circular, 1 superficie curva y una punta"},
        {"title": "Adivinar con pistas", "problem": "Tiene 6 caras planas y todas son cuadrados iguales. ¿Qué cuerpo es?", "steps": ["Tiene caras planas, así que no es una esfera.", "Son 6 caras, y todas cuadradas iguales.", "Eso describe un cubo."], "answer": "Un cubo"},
    ],
    mistakes=[
        {"wrong": "Decir que la esfera tiene una cara.", "why": "Se confunde cara plana con superficie.", "fix": "La esfera tiene cero caras planas; toda su superficie es curva."},
        {"wrong": "Decir que el cono sólo tiene superficie curva.", "why": "Se olvida su base.", "fix": "El cono tiene también 1 cara plana, que es un círculo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas caras planas tiene un cubo?", "6", "Un cubo tiene seis caras cuadradas."),
            ex("¿Cuántas caras planas tiene una esfera?", "0", "Toda su superficie es curva."),
            ex("¿Cuántas caras planas tiene un cono?", "1", "Su base es la única cara plana."),
        ],
        "understand": [
            ex("¿Qué forma tiene la cara plana de un cono?", "De círculo", "La base del cono es un círculo."),
            ex("¿Qué forma tienen las caras de un cubo?", "De cuadrado", "Sus seis caras son cuadrados iguales."),
            ex("¿Qué forma tienen las caras de una caja con forma de ladrillo?", "De rectángulo", "El paralelepípedo tiene caras rectangulares."),
        ],
        "apply": [
            ex("Pista: tiene sólo una superficie y es curva. ¿Qué cuerpo es?", "Una esfera", "No tiene caras planas."),
            ex("Pista: tiene 1 cara plana circular, 1 superficie curva y una punta. ¿Qué cuerpo es?", "Un cono", "Eso describe el cono."),
            arith("Un cubo tiene 6 caras planas y un cono tiene 1. ¿Cuántas caras planas hay entre los dos?", "6+1", "Se suman las caras de cada cuerpo."),
        ],
        "reason": [
            ex("Andrea dice «mi cuerpo tiene 6 caras planas» y Lalo dice «es una esfera». ¿Lalo acierta?", "No", "La esfera no tiene caras planas."),
            ex("Una pista dice: «tiene una superficie curva y una cara plana». Fabián piensa que es un cubo. ¿Qué error comete?", "El cubo no tiene superficie curva", "El cuerpo descrito es un cono."),
        ],
        "challenge": [
            ex("Quieres que tu amigo adivine un cubo con 2 pistas. ¿Cuáles escribes?", "Tiene 6 caras planas y todas son cuadrados iguales", "Con esas pistas sólo puede ser un cubo."),
            arith("Tienes 2 cubos y 1 esfera. ¿Cuántas caras planas hay en total?", "6+6+0", "Cada cubo tiene 6 caras y la esfera 0."),
        ],
    },
    context=[ex("Una pelota, un dado y un gorro de cumpleaños de cartón están sobre la mesa. ¿Cuál tiene una cara plana y una superficie curva?", "El gorro", "Es un cono y tiene base circular más superficie curva.")],
    selfcheck=[
        ex("¿Cuál cuerpo no tiene caras planas?", "La esfera", "Es completamente curva."),
        ex("¿Cuántas caras tiene una caja con forma de ladrillo?", "6", "Tiene seis caras rectangulares."),
        ex("¿Qué cuerpo tiene 1 cara plana y 1 superficie curva?", "El cono", "La base es plana y el resto es curvo."),
    ],
    open_task=task(
        "Elige uno de estos cuerpos: cubo, esfera, cono o caja con forma de ladrillo. Escribe tres pistas sobre sus caras y sus superficies, sin decir su nombre. Luego escribe cuál es la respuesta.",
        "Pistas: tiene 1 cara plana, tiene 1 superficie curva y tiene una punta. Respuesta: es un cono.",
        ["escribe tres pistas", "usa caras planas y superficies curvas", "la respuesta coincide con las pistas", "no dice el nombre en las pistas"],
        ["tres pistas", "respuesta"],
        ["dar pistas que sirven para varios cuerpos", "decir el nombre en las pistas"],
        "Pide que otra persona adivine con tus pistas. Reconoce cuando las pistas son suficientes.",
    ),
    reinforce="Mira objetos de la cocina y busca uno con caras planas y otro con superficie curva.",
    extend="Escribe la ficha de un cubo, una esfera y un cono: cuántas caras planas y cuántas superficies curvas tiene cada uno.",
)

register(
    OA16, 3,
    materials="Un dado y una caja con forma de ladrillo (por ejemplo, de cereal). Los datos de cada cuerpo están escritos en los ejercicios.",
    use="Aprenderé a comparar el cubo y el paralelepípedo, que tienen seis caras cada uno. Sirve para saber en qué se parecen y en qué se diferencian.",
    prior=["Sé que el cubo y la caja tienen caras planas.", "Sé distinguir cuadrados y rectángulos."],
    explain=[
        "El cubo y el paralelepípedo tienen 6 caras planas cada uno. También tienen 12 aristas, que son las líneas donde se juntan dos caras, y 8 vértices, que son las esquinas. En eso se parecen.",
        "La diferencia está en las caras. En el cubo, las 6 caras son cuadrados iguales. En el paralelepípedo, las caras son rectángulos, como las de una caja de cereal, y suelen ser de distinto tamaño.",
        "Para comparar, cuenta primero lo que se parece y luego mira la forma de las caras. Un dado es un cubo, y una caja de zapatos es un paralelepípedo. No te guíes por el objeto, sino por sus caras.",
    ],
    vocab=[("cubo", "6 caras cuadradas iguales"), ("paralelepípedo", "6 caras rectangulares"), ("arista", "línea donde se juntan dos caras"), ("vértice", "esquina donde se juntan aristas"), ("comparar", "decir en qué se parecen y en qué se diferencian")],
    worked=[
        {"title": "Parecidos", "problem": "Compara un cubo y un paralelepípedo. ¿Cuántas caras y vértices tiene cada uno?", "steps": ["Cubo: 6 caras y 8 vértices.", "Paralelepípedo: 6 caras y 8 vértices.", "Tienen el mismo número."], "answer": "Los dos tienen 6 caras y 8 vértices"},
        {"title": "Diferencia", "problem": "Un cuerpo de 6 caras tiene 2 caras de 10 cm × 6 cm, 2 de 10 cm × 4 cm y 2 de 6 cm × 4 cm. ¿Es cubo?", "steps": ["Miro el tamaño de las caras.", "No son todas iguales.", "Un cubo tendría 6 caras cuadradas iguales."], "answer": "No, es un paralelepípedo"},
    ],
    mistakes=[
        {"wrong": "Decir que un dado y una caja de zapatos son iguales porque ambos tienen 6 caras.", "why": "Sólo se mira lo que se parece.", "fix": "Mira también la forma de las caras: cuadrados iguales (cubo) o rectángulos (paralelepípedo)."},
        {"wrong": "Decir que la caja de zapatos es un cubo.", "why": "Se nombra por el objeto y no por las caras.", "fix": "Revisa las caras: si hay rectángulos, es un paralelepípedo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas caras tiene un cubo?", "6", "Un cubo tiene seis caras cuadradas."),
            ex("¿Cuántas caras tiene un paralelepípedo?", "6", "Tiene seis caras rectangulares."),
            ex("¿Qué cuerpo tiene las 6 caras cuadradas e iguales: el cubo o el paralelepípedo?", "El cubo", "En el paralelepípedo las caras son rectángulos."),
        ],
        "understand": [
            ex("¿Qué es una arista?", "La línea donde se juntan dos caras", "Es el borde entre dos caras planas."),
            ex("¿Cuántos vértices tiene un cubo?", "8", "Tiene ocho esquinas."),
            ex("Escribe una cosa en que se parecen el cubo y el paralelepípedo.", "Tienen 6 caras, 12 aristas y 8 vértices", "Los dos tienen el mismo número de caras, aristas y vértices."),
        ],
        "apply": [
            ex("Un cuerpo tiene 6 caras cuadradas de 5 cm de lado. ¿Es cubo o paralelepípedo?", "Cubo", "Las seis caras son cuadrados iguales."),
            ex("Un cuerpo tiene 2 caras de 12 cm × 8 cm, 2 de 12 cm × 3 cm y 2 de 8 cm × 3 cm. ¿Es cubo o paralelepípedo?", "Paralelepípedo", "Las caras son rectángulos distintos."),
            arith("Un cubo y un paralelepípedo están en la mesa. ¿Cuántas caras hay entre los dos?", "6+6", "Cada uno tiene seis caras."),
        ],
        "reason": [
            ex("Mía dice que una caja de zapatos es un cubo porque tiene 6 caras. ¿Qué le falta revisar?", "Si sus caras son cuadrados iguales", "Tiene 6 caras, pero son rectángulos."),
            ex("Raúl dice que el dado tiene más vértices que la caja de cereal. ¿Es cierto?", "No; los dos tienen 8", "El cubo y el paralelepípedo tienen 8 vértices."),
        ],
        "challenge": [
            arith("Cada cubo y cada paralelepípedo tiene 12 aristas. Tienes 2 cubos y 1 paralelepípedo. ¿Cuántas aristas hay en total?", "12+12+12", "Cada cuerpo aporta 12 aristas."),
            ex("Una caja tiene 6 caras largas y angostas, y ninguna es cuadrada. ¿Puede ser un cubo?", "No", "Un cubo tiene todas sus caras cuadradas."),
        ],
    },
    context=[ex("Un dado mide 2 cm por cada lado. Una caja de cereal mide 20 cm de alto, 15 cm de ancho y 6 cm de fondo. ¿Cuál de los dos es un cubo?", "El dado", "Sus lados son iguales; la caja tiene tres medidas distintas.")],
    selfcheck=[
        ex("¿Cuántas aristas tiene un cubo?", "12", "El cubo tiene doce bordes entre caras."),
        ex("¿Qué forma tienen las caras de un paralelepípedo?", "De rectángulo", "Es como una caja de cereal."),
        ex("¿Qué cuerpo tiene todas sus caras iguales?", "El cubo", "Sus seis caras son cuadrados iguales."),
    ],
    open_task=task(
        "Compara un dado (cubo) y una caja de cereal (paralelepípedo). Escribe dos cosas en que se parecen y una cosa en que se diferencian. Si no tienes los objetos, usa estos datos: el dado mide 2 cm en cada lado; la caja mide 20 cm × 15 cm × 6 cm.",
        "Se parecen en que los dos tienen 6 caras y 8 vértices. Se diferencian en que las caras del dado son cuadrados iguales, y las de la caja son rectángulos de distinto tamaño.",
        ["escribe dos parecidos", "escribe una diferencia comprobable", "usa caras, aristas o vértices"],
        ["dos parecidos y una diferencia", "uso de datos"],
        ["decir que son iguales", "usar sólo el nombre del objeto"],
        "Pide mostrar con el objeto o con los datos cada afirmación. Reconoce las diferencias comprobables.",
    ),
    reinforce="Cuenta las caras, las aristas y los vértices de una caja de tu casa y anótalas.",
    extend="Dibuja un cubo y un paralelepípedo y marca una arista y un vértice en cada uno.",
)

register(
    OA16, 4,
    materials="Papel, tijeras de punta redonda, regla, plasticina o palitos. Todas las medidas están escritas en los ejercicios.",
    use="Aprenderé a construir un cuerpo a partir de lo que necesita. Sirve para armar un cubo o una caja y comprobar que no sobran ni faltan caras.",
    prior=["Sé que el cubo tiene 6 caras cuadradas.", "Sé que el paralelepípedo tiene 6 caras rectangulares."],
    explain=[
        "Para construir un cubo de papel necesitas 6 cuadrados iguales. Los uno por sus bordes formando una red, la doblas y se arma el cubo. Si falta o sobra un cuadrado, el cubo no queda bien.",
        "Otra forma de construir es con palitos y plasticina. Los palitos son las aristas y las bolitas de plasticina son los vértices. Un cubo necesita 12 palitos iguales y 8 bolitas.",
        "Una caja con forma de ladrillo se arma con 6 rectángulos o con 12 palitos de tres medidas distintas: 4 de cada medida. Una esfera se hace con plasticina, sin palitos. Antes de construir, elige los materiales que se parecen al cuerpo.",
    ],
    vocab=[("red", "dibujo plano que se dobla para armar un cuerpo"), ("arista", "palito o borde entre dos caras"), ("vértice", "bolita donde se juntan los palitos"), ("construir", "armar un cuerpo con material"), ("comprobar", "revisar que no falten ni sobren partes")],
    worked=[
        {"title": "Materiales de un cubo", "problem": "Quieres armar un cubo con palitos y bolitas de plasticina. ¿Cuántos necesitas de cada uno?", "steps": ["Un cubo tiene 12 aristas: 12 palitos.", "Un cubo tiene 8 vértices: 8 bolitas.", "Los 12 palitos deben medir lo mismo."], "answer": "12 palitos iguales y 8 bolitas"},
        {"title": "Revisar una red", "problem": "Una red tiene 5 cuadrados iguales unidos. ¿Sirve para armar un cubo?", "steps": ["Un cubo necesita 6 cuadrados.", "La red tiene sólo 5.", "Falta una cara."], "answer": "No sirve; falta 1 cuadrado"},
    ],
    mistakes=[
        {"wrong": "Cortar 6 cuadrados de tamaños distintos para armar un cubo.", "why": "Las caras no encajan.", "fix": "Los seis cuadrados deben medir lo mismo en cada lado."},
        {"wrong": "Usar 12 palitos de distinto largo para un cubo.", "why": "Un cubo tiene todas sus aristas iguales.", "fix": "Usa 12 palitos del mismo largo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos cuadrados iguales necesitas para armar un cubo de papel?", "6", "El cubo tiene seis caras."),
            ex("¿Cuántas bolitas de plasticina necesitas para los vértices de un cubo?", "8", "Un cubo tiene ocho vértices."),
            ex("¿Con qué material haces una esfera: palitos o plasticina?", "Plasticina", "Es un cuerpo curvo, sin aristas."),
        ],
        "understand": [
            ex("En un cubo de palitos, ¿qué representan los palitos?", "Las aristas", "Son los bordes entre las caras."),
            ex("En un cubo de palitos, ¿qué representan las bolitas?", "Los vértices", "Son las esquinas del cubo."),
            ex("¿Cuántos palitos necesita un cubo?", "12", "Un cubo tiene doce aristas."),
        ],
        "apply": [
            ex("Tienes 12 palitos: 4 de 8 cm, 4 de 5 cm y 4 de 3 cm. ¿Qué cuerpo armas con ellos?", "Un paralelepípedo", "Tiene tres medidas distintas, cuatro de cada una."),
            ex("Tienes 12 palitos iguales de 6 cm y 8 bolitas de plasticina. ¿Qué cuerpo armas?", "Un cubo", "Las 12 aristas son iguales y hay 8 vértices."),
            arith("Quieres armar 2 cubos de palitos. ¿Cuántos palitos necesitas en total?", "12*2", "Cada cubo necesita 12 palitos."),
        ],
        "reason": [
            ex("Dani armó una red con 7 cuadrados iguales para un cubo. ¿Qué pasará al doblarla?", "Sobrará un cuadrado", "Un cubo sólo necesita 6 caras."),
            ex("Tere dice que un cono se arma con 6 cuadrados. ¿Está bien?", "No", "El cono tiene una cara circular y una superficie curva."),
        ],
        "challenge": [
            ex("Quieres armar un cubo de 4 cm de arista con palitos de 4 cm. Tienes 10 palitos. ¿Cuántos palitos te faltan?", "2", "Necesitas 12 y tienes 10: 12 − 10 = 2."),
            ex("Una caja de ladrillo necesita 12 palitos: 4 largos, 4 medianos y 4 cortos. Tienes 4 largos, 3 medianos y 4 cortos. ¿Qué palitos te faltan?", "1 palito mediano", "Faltan 4 − 3 = 1 palito mediano."),
        ],
    },
    context=[ex("Cami quiere hacer un dado de cartón con 6 cuadrados iguales de 5 cm. Ya cortó 4. ¿Cuántos le faltan?", "2", "Necesita 6 y tiene 4: 6 − 4 = 2.")],
    selfcheck=[
        ex("¿Cuántas caras tiene la red de un cubo?", "6", "El cubo tiene seis caras."),
        ex("¿Cuántos palitos hacen las aristas de un cubo?", "12", "Un cubo tiene 12 aristas."),
        ex("¿Qué pasa si una red de cubo tiene un cuadrado más pequeño?", "El cubo no queda bien", "Las caras no encajan."),
    ],
    open_task=task(
        "Quieres construir un cubo. Elige entre estas dos opciones y escribe qué materiales necesitas: opción A, 6 cuadrados de papel de 5 cm de lado; opción B, 12 palitos iguales de 5 cm y 8 bolitas de plasticina. Escribe cuántas piezas usarás y cómo comprobarás que no falta ni sobra nada.",
        "Elijo la opción A: 6 cuadrados de 5 cm de lado. Comprobaré que los 6 cuadrados midan lo mismo, que formen una red y que al doblar no sobre ni falte ninguno.",
        ["elige una opción", "indica la cantidad correcta de piezas", "explica cómo comprobar", "justifica con las caras o las aristas"],
        ["opción elegida", "cantidades", "explicación"],
        ["usar piezas de tamaños distintos", "contar mal las aristas"],
        "Pide contar las piezas en voz alta. Reconoce las comprobaciones.",
    ),
    reinforce="Dibuja una red de cubo con 6 cuadrados y recórtala para ver si se dobla bien.",
    extend="Arma una caja con forma de ladrillo con 12 palitos de tres medidas, cuatro de cada una, y escribe sus medidas.",
)
