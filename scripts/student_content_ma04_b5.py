"""Student material for 4.º básico Matemática, OA 18 (transformaciones isométricas), OA 19 (ángulos con transportador) y OA 20 (hora en A.M., P.M. y 24 horas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA18, OA19, OA20 = "MA04 OA 18", "MA04 OA 19", "MA04 OA 20"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


POS = "Un punto se nombra (columna, fila): las columnas se cuentan de izquierda a derecha y las filas, de abajo hacia arriba. Por ejemplo, (2, 3) es la columna 2 y la fila 3."

# ================================================================ OA 18
register(
    OA18, 1,
    materials=f"Lápiz y papel cuadriculado. {POS}",
    use="Aprenderé a trasladar una figura: moverla sin girarla ni darla vuelta. Sirve para describir cómo se mueve una pieza en un juego.",
    prior=["Sé ubicar un punto con columna y fila.", "Sé contar cuadritos a la derecha, izquierda, arriba y abajo."],
    explain=[
        "Una traslación es mover una figura a otro lugar sin girarla ni darla vuelta. La figura conserva su forma, su tamaño y hacia dónde apunta. Todos sus puntos se mueven lo mismo, en la misma dirección.",
        "Para describir una traslación, di la dirección y cuántos cuadritos se mueve. Por ejemplo, «3 cuadritos a la derecha y 2 hacia arriba». Si un punto está en (1, 1), pasa a (4, 3): sumas 3 a la columna y 2 a la fila.",
        "Si el movimiento es a la izquierda, restas a la columna. Si es hacia abajo, restas a la fila. Una flecha que apunta hacia arriba sigue apuntando hacia arriba después de trasladarla. Si cambia, hubo un giro o un reflejo, no una traslación.",
    ],
    vocab=[("traslación", "movimiento de una figura sin girarla ni darla vuelta"), ("dirección", "hacia dónde se mueve: izquierda, derecha, arriba o abajo"), ("conservar", "mantener igual"), ("orientación", "hacia dónde apunta o mira una figura"), ("vértice", "punto donde se juntan dos lados")],
    worked=[
        {"title": "Trasladar un punto", "problem": "El punto (2, 3) se traslada 4 cuadritos a la derecha. ¿Dónde queda?", "steps": ["Un movimiento a la derecha cambia la columna: 2 + 4 = 6.", "La fila no cambia."], "answer": "(6, 3)"},
        {"title": "Trasladar un vértice", "problem": "Un vértice está en (3, 1). La figura se traslada 2 a la derecha y 3 hacia arriba. ¿Dónde queda ese vértice?", "steps": ["Columna: 3 + 2 = 5.", "Fila: 1 + 3 = 4."], "answer": "(5, 4)"},
    ],
    mistakes=[
        {"wrong": "Trasladar una flecha que apunta a la derecha y dibujarla apuntando a la izquierda.", "why": "Se da vuelta la figura, lo que es una reflexión.", "fix": "En una traslación la flecha sigue apuntando a la derecha."},
        {"wrong": "Decir que trasladar (1, 1) tres a la derecha y dos arriba da (3, 2).", "why": "Se mezclan las cantidades.", "fix": "A la columna se le suma 3 y a la fila se le suma 2: (4, 3)."},
    ],
    tiers={
        "recovery": [
            ex("El punto (3, 2) se traslada 5 cuadritos a la derecha. ¿Dónde queda? Escribe (columna, fila).", "(8, 2)", "Se suma 5 a la columna y la fila no cambia."),
            ex("El punto (5, 1) se traslada 2 cuadritos hacia arriba. ¿Dónde queda?", "(5, 3)", "Se suma 2 a la fila."),
            ex("Al trasladar una figura, ¿cambia su forma o su tamaño?", "No", "La traslación solo cambia el lugar."),
        ],
        "understand": [
            ex("Una flecha que apunta hacia arriba se traslada 3 cuadritos a la derecha. ¿Hacia dónde apunta después?", "Hacia arriba", "En una traslación la orientación se conserva."),
            ex("¿Qué se conserva al trasladar una figura?", "La forma, el tamaño y la orientación", "Solo cambia su posición."),
            ex("Para describir una traslación, ¿qué dos datos necesitas?", "La dirección y cuántos cuadritos se mueve", "Con ellos se sabe dónde queda cada punto."),
        ],
        "apply": [
            ex("Un triángulo tiene un vértice en (4, 2). Se traslada 3 a la derecha y 1 hacia abajo. ¿Dónde queda ese vértice?", "(7, 1)", "4 + 3 = 7 y 2 − 1 = 1."),
            ex("El punto (4, 5) se traslada 3 cuadritos hacia abajo y 2 a la izquierda. ¿Dónde queda?", "(2, 2)", "Columna: 4 − 2 = 2. Fila: 5 − 3 = 2."),
            ex("Un cuadrado de 2 por 2 tiene su esquina inferior izquierda en (1, 1). Se traslada 4 cuadritos a la derecha. ¿Dónde queda esa esquina?", "(5, 1)", "Solo cambia la columna: 1 + 4 = 5."),
        ],
        "reason": [
            ex("Eva trasladó una flecha que apunta a la derecha y la dibujó apuntando a la izquierda. ¿Hizo una traslación?", "No; la dio vuelta", "La traslación conserva hacia dónde apunta la figura."),
            ex("Iván dice que al trasladar (1, 1) tres a la derecha y dos arriba queda en (3, 2). ¿Es correcto?", "No; queda en (4, 3)", "A la columna se suma 3 y a la fila se suma 2."),
        ],
        "challenge": [
            ex("Un punto pasa de (2, 3) a (6, 5) por una traslación. ¿Cuántos cuadritos se movió a la derecha y cuántos hacia arriba?", "4 a la derecha y 2 hacia arriba", "6 − 2 = 4 y 5 − 3 = 2."),
            ex("Un punto se traslada 3 cuadritos a la derecha y luego 2 a la izquierda. ¿Cuál es el movimiento total?", "1 cuadrito a la derecha", "3 − 2 = 1."),
        ],
    },
    context=[ex("En un tablero, una pieza está en (3, 2). La mueves 2 cuadritos a la derecha y 1 hacia arriba, sin girarla. ¿Dónde queda?", "(5, 3)", "3 + 2 = 5 y 2 + 1 = 3.")],
    selfcheck=[
        ex("El punto (1, 4) se traslada 5 cuadritos a la derecha. ¿Dónde queda?", "(6, 4)", "Se suma 5 a la columna."),
        ex("El punto (6, 6) se traslada 2 cuadritos hacia abajo. ¿Dónde queda?", "(6, 4)", "Se resta 2 a la fila."),
        ex("¿Una traslación puede cambiar hacia dónde apunta una flecha?", "No", "Conserva la orientación."),
    ],
    open_task=task(
        "En papel cuadriculado dibuja un triángulo con vértices en (1, 1), (3, 1) y (1, 2). Elige una traslación: A) 4 a la derecha y 1 arriba, o B) 2 a la derecha y 3 arriba. Dibuja el triángulo trasladado y escribe las nuevas coordenadas de los tres vértices.",
        "Traslación A: (1, 1) → (5, 2); (3, 1) → (7, 2); (1, 2) → (5, 3).",
        ["dibuja la figura inicial", "suma las cantidades a columna y fila", "dibuja la figura trasladada sin girarla"],
        ["dos triángulos", "tres coordenadas nuevas"],
        ["girar la figura", "mezclar columna y fila"],
        "Pide que compare la forma y la orientación de ambos triángulos. Reconoce la comprobación de que la figura no giró.",
    ),
    reinforce="Mueve una moneda sobre una cuadrícula 3 cuadritos a la derecha y 2 hacia arriba. Anota la posición antes y después.",
    extend="Traslada un cuadrado de 2 por 2 en dos pasos distintos y comprueba que llega al mismo lugar.",
)

register(
    OA18, 2,
    materials=f"Lápiz y papel cuadriculado. Si quieres, un espejo pequeño de plástico. {POS}",
    use="Aprenderé a reflejar una figura respecto de un eje, como en un espejo. Sirve para dibujar la imagen de una figura.",
    prior=["Sé qué es una línea de simetría.", "Sé trasladar una figura."],
    explain=[
        "Una reflexión es reflejar una figura respecto de una línea llamada eje, como en un espejo. Cada punto de la figura y su reflejo están a la misma distancia del eje, pero en lados opuestos. La figura conserva su forma y su tamaño.",
        "Con un eje vertical entre las columnas 3 y 4, la columna c pasa a la columna 7 − c. La fila no cambia. Por ejemplo, el punto (2, 3) pasa a (5, 3). Con un eje horizontal entre las filas 2 y 3, la fila f pasa a la fila 5 − f y la columna no cambia.",
        "En una reflexión, la figura queda «al revés», como en un espejo. Una flecha que apunta a la derecha, reflejada con un eje vertical, apunta a la izquierda. Una flecha que apunta hacia arriba sigue apuntando hacia arriba, porque el eje vertical no la voltea de arriba a abajo.",
    ],
    vocab=[("reflexión", "transformación que da la imagen de una figura como en un espejo"), ("eje de reflexión", "línea respecto de la cual se refleja una figura"), ("simétrico", "punto que es el reflejo de otro"), ("misma distancia", "igual cantidad de cuadritos hasta el eje"), ("orientación", "hacia dónde apunta una figura")],
    worked=[
        {"title": "Reflejar un punto", "problem": "El eje vertical está entre las columnas 3 y 4. ¿Dónde queda el reflejo del punto (2, 3)?", "steps": ["La columna 2 está a 2 cuadritos del eje.", "El reflejo está a 2 cuadritos del otro lado: columna 5.", "La fila no cambia."], "answer": "(5, 3)"},
        {"title": "Eje horizontal", "problem": "El eje horizontal está entre las filas 2 y 3. ¿Dónde queda el reflejo del punto (2, 4)?", "steps": ["La fila 4 está a 2 cuadritos del eje (la fila 3 está a 1).", "El reflejo está a 2 del otro lado: fila 1.", "La columna no cambia."], "answer": "(2, 1)"},
    ],
    mistakes=[
        {"wrong": "Reflejar (2, 3) con el eje entre las columnas 3 y 4 y escribir (4, 3).", "why": "No se respeta la misma distancia al eje.", "fix": "La columna 2 está a 2 del eje. El reflejo es la columna 5: (5, 3)."},
        {"wrong": "Dibujar el reflejo de una flecha que apunta a la derecha como otra flecha que también apunta a la derecha.", "why": "Se traslada la figura en vez de reflejarla.", "fix": "Con un eje vertical, la flecha del reflejo apunta a la izquierda."},
    ],
    tiers={
        "recovery": [
            ex("El eje vertical está entre las columnas 3 y 4. ¿Dónde queda el reflejo del punto (4, 2)?", "(3, 2)", "La columna 4 está pegada al eje y su reflejo también."),
            ex("Con el mismo eje, ¿dónde queda el reflejo del punto (3, 1)?", "(4, 1)", "La columna 3 está pegada al eje y su reflejo también."),
            ex("Con el mismo eje, ¿dónde queda el reflejo del punto (1, 2)?", "(6, 2)", "La columna 1 está a 3 del eje y la 6 también."),
        ],
        "understand": [
            ex("Una flecha que apunta a la derecha se refleja con un eje vertical. ¿Hacia dónde apunta el reflejo?", "Hacia la izquierda", "Un espejo vertical cambia la derecha por la izquierda."),
            ex("Una flecha que apunta hacia arriba se refleja con un eje vertical. ¿Hacia dónde apunta el reflejo?", "Hacia arriba", "El eje vertical no cambia arriba por abajo."),
            ex("¿Una reflexión conserva el tamaño de la figura?", "Sí", "El reflejo es una imagen del mismo tamaño."),
        ],
        "apply": [
            ex("El eje horizontal está entre las filas 2 y 3. ¿Dónde queda el reflejo del punto (5, 1)?", "(5, 4)", "La fila 1 está a 2 del eje y la fila 4 también."),
            ex("Un triángulo tiene un vértice en (2, 1). El eje vertical está entre las columnas 3 y 4. ¿Dónde queda ese vértice reflejado?", "(5, 1)", "La columna 2 está a 2 del eje y la 5 también."),
            ex("Con el eje vertical entre las columnas 3 y 4, ¿dónde queda el reflejo del punto (5, 2)?", "(2, 2)", "La columna 5 está a 2 del eje y la 2 también."),
        ],
        "reason": [
            ex("Leo dice que el reflejo de (2, 3), con el eje entre las columnas 3 y 4, es (4, 3) porque queda al lado. ¿Es correcto?", "No; es (5, 3)", "Debe estar a la misma distancia del eje, o sea a 2 cuadritos."),
            ex("Ana dibuja el reflejo de una flecha que apunta a la derecha y su dibujo también apunta a la derecha. ¿Qué transformación hizo en realidad?", "Una traslación", "En un reflejo con eje vertical, la flecha apuntaría a la izquierda."),
        ],
        "challenge": [
            ex("Un punto está en la columna 6 y se refleja con un eje vertical entre las columnas 3 y 4. ¿En qué columna queda su reflejo?", "En la columna 1", "La columna 6 está a 3 del eje y la 1 también."),
            ex("El reflejo de (2, 4) con el eje horizontal entre las filas 2 y 3 es (2, 1). Si se refleja otra vez con el mismo eje, ¿dónde queda?", "(2, 4)", "Reflejar dos veces con el mismo eje devuelve el punto."),
        ],
    },
    context=[ex("Pones una figura frente a un espejo y una flecha de la figura apunta hacia el espejo. En el reflejo, ¿la flecha apunta hacia el espejo o se aleja de él?", "Hacia el espejo", "El reflejo está a la misma distancia al otro lado y apunta hacia el mismo espejo.")],
    selfcheck=[
        ex("Con el eje vertical entre las columnas 3 y 4, ¿dónde queda el reflejo de (1, 5)?", "(6, 5)", "La columna 1 está a 3 del eje."),
        ex("Con el eje horizontal entre las filas 2 y 3, ¿dónde queda el reflejo de (4, 1)?", "(4, 4)", "La fila 1 está a 2 del eje y la 4 también."),
        ex("¿El reflejo de una figura puede ser más grande que ella?", "No", "La reflexión conserva el tamaño."),
    ],
    open_task=task(
        "Dibuja un eje vertical entre las columnas 3 y 4 de una cuadrícula de 6 columnas. Elige una figura: A) un triángulo con vértices en (1, 1), (2, 1) y (1, 3); B) un cuadrilátero con vértices en (1, 1), (3, 1), (3, 2) y (1, 2). Dibuja su reflejo y escribe las coordenadas de los vértices reflejados.",
        "Figura B: (1, 1) → (6, 1); (3, 1) → (4, 1); (3, 2) → (4, 2); (1, 2) → (6, 2).",
        ["dibuja el eje", "refleja cada vértice a la misma distancia", "escribe las coordenadas del reflejo"],
        ["dibujo", "coordenadas del reflejo"],
        ["usar la distancia equivocada", "trasladar en vez de reflejar"],
        "Pide que cuente la distancia al eje con el dedo. Reconoce el control de la distancia.",
    ),
    reinforce="Con un espejo pequeño o doblando una hoja, observa cómo cambia la izquierda y la derecha en una flecha dibujada.",
    extend="Refleja una figura con un eje vertical y el resultado con un eje horizontal. Describe qué pasó con una flecha.",
)

register(
    OA18, 3,
    materials="Lápiz y papel. Si quieres, un reloj de pared para mirar el sentido de giro.",
    use="Aprenderé a rotar una figura alrededor de un punto. Sirve para describir giros, como los de una puerta o un volante de juguete.",
    prior=["Conozco izquierda, derecha, arriba y abajo.", "Sé trasladar y reflejar figuras."],
    explain=[
        "Una rotación es girar una figura alrededor de un punto llamado centro de giro. La figura conserva su forma y su tamaño, pero cambia hacia dónde apunta. Para rotar necesitas tres datos: el centro, cuánto girar y el sentido.",
        "El sentido horario es el mismo en que giran las agujas del reloj. Una flecha que gira de cuarto en cuarto pasa por estas posiciones, en este orden: arriba, derecha, abajo, izquierda, y vuelve a arriba. Una flecha que apunta hacia arriba, con un cuarto de vuelta horario, apunta a la derecha. Con media vuelta apunta hacia abajo.",
        "Un punto que está 3 cuadritos a la derecha del centro, con un cuarto de vuelta horario, pasa a estar 3 cuadritos abajo del centro. Cuatro cuartos de vuelta forman una vuelta completa y la figura queda igual que al principio.",
    ],
    vocab=[("rotación", "giro de una figura alrededor de un punto"), ("centro de giro", "punto que no se mueve cuando se gira"), ("sentido horario", "el mismo sentido en que giran las agujas del reloj"), ("cuarto de vuelta", "giro de un cuarto de círculo"), ("media vuelta", "giro de dos cuartos de vuelta")],
    worked=[
        {"title": "Girar una flecha", "problem": "Una flecha apunta hacia arriba. Se gira un cuarto de vuelta en sentido horario. ¿Hacia dónde apunta?", "steps": ["En sentido horario, de arriba se pasa a la derecha.", "Un cuarto de vuelta es un solo paso."], "answer": "Hacia la derecha"},
        {"title": "Girar un punto", "problem": "Un punto está 3 cuadritos a la derecha del centro de giro. Se gira un cuarto de vuelta horario. ¿Dónde queda?", "steps": ["De la derecha, un cuarto de vuelta horario pasa a abajo.", "La distancia al centro se mantiene: 3 cuadritos."], "answer": "3 cuadritos abajo del centro"},
    ],
    mistakes=[
        {"wrong": "Girar una flecha que apunta hacia arriba un cuarto de vuelta horario y dibujarla hacia la izquierda.", "why": "Se gira en sentido contrario al reloj.", "fix": "En sentido horario, de arriba se pasa a la derecha."},
        {"wrong": "Decir que una flecha que apunta a la derecha, con media vuelta, sigue apuntando a la derecha.", "why": "Se confunde media vuelta con cero giro.", "fix": "Media vuelta cambia la flecha al lado opuesto: apunta a la izquierda."},
    ],
    tiers={
        "recovery": [
            ex("Una flecha apunta hacia abajo. Gira media vuelta. ¿Hacia dónde apunta?", "Hacia arriba", "Media vuelta la deja en el lado opuesto."),
            ex("Una flecha apunta hacia la derecha. Gira media vuelta. ¿Hacia dónde apunta?", "Hacia la izquierda", "Media vuelta la deja en el lado opuesto."),
            ex("Una flecha apunta hacia abajo. Gira un cuarto de vuelta en sentido horario. ¿Hacia dónde apunta?", "Hacia la izquierda", "En sentido horario, de abajo se pasa a la izquierda."),
        ],
        "understand": [
            ex("¿Qué tres datos se necesitan para describir una rotación?", "El centro de giro, cuánto gira y el sentido", "Con ellos se sabe dónde queda la figura."),
            ex("¿Cuántos cuartos de vuelta forman una vuelta completa?", "4", "Cuatro cuartos son un entero."),
            ex("Al rotar una figura, ¿cambia su tamaño?", "No", "La rotación conserva forma y tamaño."),
        ],
        "apply": [
            ex("Un punto está 4 cuadritos abajo del centro de giro. Gira un cuarto de vuelta horario. ¿Dónde queda?", "4 cuadritos a la izquierda del centro", "En sentido horario, de abajo se pasa a la izquierda."),
            ex("Un punto está 2 cuadritos arriba del centro de giro. Gira media vuelta. ¿Dónde queda?", "2 cuadritos abajo del centro", "Media vuelta lo deja al lado opuesto del centro."),
            ex("Una flecha apunta hacia la izquierda y gira un cuarto de vuelta en sentido horario. ¿Hacia dónde apunta?", "Hacia arriba", "En sentido horario, de la izquierda se pasa a arriba."),
        ],
        "reason": [
            ex("Mía giró una flecha que apunta hacia arriba un cuarto de vuelta horario y la dibujó hacia la izquierda. ¿Qué hizo mal?", "Giró en el sentido contrario al reloj", "En sentido horario apunta a la derecha."),
            ex("Tomás dice que media vuelta deja una flecha que apunta a la derecha apuntando a la derecha. ¿Tiene razón?", "No; apunta a la izquierda", "Media vuelta la deja al lado opuesto."),
        ],
        "challenge": [
            ex("Una flecha apunta hacia arriba. ¿Cuántos cuartos de vuelta en sentido horario necesita para apuntar hacia abajo?", "2", "Arriba, derecha, abajo: 2 cuartos de vuelta."),
            ex("Una flecha apunta hacia arriba y gira 3 cuartos de vuelta en sentido horario. ¿Hacia dónde apunta?", "Hacia la izquierda", "Arriba, derecha, abajo, izquierda."),
        ],
    },
    context=[ex("La aguja larga de un reloj apunta al 12. Gira un cuarto de vuelta en el sentido del reloj. ¿A qué número apunta?", "Al 3", "Un cuarto de vuelta va del 12 al 3.")],
    selfcheck=[
        ex("Una flecha apunta hacia la derecha y gira un cuarto de vuelta horario. ¿Hacia dónde apunta?", "Hacia abajo", "De la derecha se pasa a abajo."),
        ex("Una aguja apunta al 6 y gira media vuelta. ¿A qué número apunta?", "Al 12", "Media vuelta la lleva al lado opuesto del reloj."),
        ex("¿Qué punto no se mueve en una rotación?", "El centro de giro", "Todo gira alrededor de él."),
    ],
    open_task=task(
        "Dibuja una flecha en el centro de una hoja. Elige un giro: A) un cuarto de vuelta en sentido horario, o B) media vuelta. Dibuja la flecha en su nueva posición y escribe hacia dónde apunta antes y después.",
        "Giro A: antes apuntaba hacia arriba, después hacia la derecha.",
        ["elige un giro", "dibuja la flecha girada", "describe antes y después"],
        ["dos dibujos", "descripción"],
        ["girar en sentido contrario", "confundir un cuarto con media vuelta"],
        "Pide que gire una hoja con la flecha para comprobar. Reconoce el sentido horario.",
    ),
    reinforce="Mira un reloj de pared o dibújalo. Marca hacia dónde apunta la aguja larga al pasar 15 minutos, 30 minutos y 45 minutos.",
    extend="Gira un punto 2 cuadritos a la derecha del centro un cuarto de vuelta, media vuelta y tres cuartos de vuelta. Anota dónde queda cada vez.",
)

register(
    OA18, 4,
    materials=f"Lápiz y papel cuadriculado. {POS}",
    use="Aprenderé a describir y combinar traslaciones, reflexiones y rotaciones. Sirve para explicar cómo llegó una figura de un lugar a otro.",
    prior=["Sé trasladar, reflejar y rotar.", "Sé ubicar puntos con columna y fila."],
    explain=[
        "Las tres transformaciones isométricas son la traslación (mover), la reflexión (espejo) y la rotación (girar). Las tres conservan el tamaño y la forma. Solo cambian el lugar de la figura o hacia dónde apunta.",
        "Para describir una transformación, nómbrala y da sus datos. Traslación: dirección y cuadritos. Reflexión: el eje. Rotación: el centro, el giro y el sentido. Puedes combinar dos transformaciones y hacerlas en orden, una después de la otra.",
        "El orden importa. Si trasladas (1, 2) dos cuadritos a la derecha, queda en (3, 2); si luego reflejas con el eje entre las columnas 3 y 4, queda en (4, 2). Si primero reflejas, queda en (6, 2), y al trasladar queda en (8, 2). El resultado es distinto.",
    ],
    vocab=[("transformación isométrica", "movimiento que conserva forma y tamaño"), ("composición", "hacer una transformación después de otra"), ("traslación", "mover sin girar ni dar vuelta"), ("reflexión", "dar vuelta como en un espejo"), ("rotación", "girar alrededor de un punto")],
    worked=[
        {"title": "Reconocer la transformación", "problem": "Una figura queda como imagen en espejo de la original. ¿Qué transformación es?", "steps": ["El espejo da vuelta la figura.", "Eso es una reflexión."], "answer": "Una reflexión"},
        {"title": "Componer dos pasos", "problem": "El punto (1, 2) se traslada 2 cuadritos a la derecha y luego se refleja con el eje vertical entre las columnas 3 y 4. ¿Dónde queda?", "steps": ["Después de la traslación está en (3, 2).", "La columna 3 se refleja en la columna 4."], "answer": "(4, 2)"},
    ],
    mistakes=[
        {"wrong": "Decir que trasladar y luego reflejar da lo mismo que reflejar y luego trasladar.", "why": "Se piensa que el orden no importa.", "fix": "Con (1, 2), un orden da (4, 2) y el otro da (8, 2). Son distintos."},
        {"wrong": "Decir que girar media vuelta es lo mismo que reflejar con un eje vertical.", "why": "Se miran solo algunas flechas.", "fix": "Una flecha hacia arriba apunta hacia abajo tras media vuelta, pero sigue hacia arriba tras el reflejo vertical."},
    ],
    tiers={
        "recovery": [
            ex("La figura se mueve 4 cuadritos a la derecha sin girar ni darse vuelta. ¿Qué transformación es?", "Una traslación", "Solo cambia el lugar."),
            ex("La figura queda como su imagen en un espejo. ¿Qué transformación es?", "Una reflexión", "El espejo da vuelta la figura."),
            ex("La figura gira alrededor de un punto fijo. ¿Qué transformación es?", "Una rotación", "El giro alrededor de un punto es una rotación."),
        ],
        "understand": [
            ex("¿Las tres transformaciones (traslación, reflexión y rotación) conservan el tamaño de la figura?", "Sí", "Son isométricas: no cambian forma ni tamaño."),
            ex("¿Cuál de las tres transformaciones es la que da vuelta la figura como un espejo?", "La reflexión", "El espejo cambia la derecha por la izquierda."),
            ex("Para describir una rotación, ¿qué tres datos necesitas?", "El centro de giro, cuánto gira y el sentido", "Con eso se ubica la figura girada."),
        ],
        "apply": [
            ex("El punto (1, 3) se traslada 1 cuadrito a la derecha y luego se refleja con el eje vertical entre las columnas 3 y 4. ¿Dónde queda?", "(5, 3)", "Primero queda en (2, 3) y luego su reflejo está en la columna 5."),
            ex("El punto (2, 1) se refleja con el eje horizontal entre las filas 2 y 3 y luego se traslada 3 a la derecha. ¿Dónde queda?", "(5, 4)", "Primero queda en (2, 4) y luego 2 + 3 = 5."),
            ex("Una flecha apunta hacia arriba. Primero gira un cuarto de vuelta horario y luego se traslada 2 cuadritos a la derecha. ¿Hacia dónde apunta al final?", "Hacia la derecha", "El giro la deja a la derecha y la traslación no cambia hacia dónde apunta."),
        ],
        "reason": [
            ex("Pedro dice que trasladar y luego reflejar da siempre lo mismo que reflejar y luego trasladar. Prueba con (1, 2): 2 a la derecha y el eje entre las columnas 3 y 4. ¿Tiene razón?", "No; un orden da (4, 2) y el otro da (8, 2)", "El reflejo de (1, 2) es (6, 2) y trasladado 2 a la derecha queda en (8, 2)."),
            ex("Sol dice que girar media vuelta es lo mismo que reflejar con un eje vertical. Prueba con una flecha que apunta hacia arriba. ¿Tiene razón?", "No; la media vuelta la deja hacia abajo y el reflejo, hacia arriba", "Los resultados son distintos."),
        ],
        "challenge": [
            ex("Un punto pasa de (2, 2) a (5, 4) por una traslación. Luego se traslada 1 cuadrito a la izquierda y 3 hacia arriba. ¿Dónde queda?", "(4, 7)", "5 − 1 = 4 y 4 + 3 = 7."),
            ex("Una traslación de 3 a la derecha y 2 arriba, seguida de otra de 1 a la derecha y 4 arriba. ¿Qué traslación única equivale?", "4 a la derecha y 6 arriba", "3 + 1 = 4 y 2 + 4 = 6."),
        ],
    },
    context=[ex("Una pieza cuadrada empieza en (1, 1). Primero se mueve 2 cuadritos a la derecha y 3 hacia arriba. Después retrocede 1 cuadrito a la izquierda. ¿Dónde queda?", "(2, 4)", "Columna: 1 + 2 − 1 = 2. Fila: 1 + 3 = 4.")],
    selfcheck=[
        ex("Una figura se mueve hacia arriba sin girar ni darse vuelta. ¿Qué transformación es?", "Una traslación", "Solo cambia el lugar."),
        ex("Para describir una reflexión, ¿qué dato necesitas?", "El eje", "El eje dice dónde está el espejo."),
        ex("El punto (4, 3) se traslada 2 a la izquierda y 1 abajo. ¿Dónde queda?", "(2, 2)", "4 − 2 = 2 y 3 − 1 = 2."),
    ],
    open_task=task(
        "Elige un punto de partida: (1, 1) o (2, 3). Hazle una traslación de 2 cuadritos a la derecha y 1 hacia arriba, y luego refléjalo con un eje vertical entre las columnas 3 y 4. Escribe dónde queda después de cada paso. Después haz las dos transformaciones en el orden contrario y compara.",
        "Desde (1, 1): traslación a (3, 2), reflexión a (4, 2). En orden contrario: reflexión a (6, 1), traslación a (8, 2). Los resultados son distintos.",
        ["hace cada transformación bien", "escribe las posiciones intermedias", "compara los dos órdenes"],
        ["pasos con coordenadas", "comparación"],
        ["pensar que el orden no importa", "mezclar columna y fila"],
        "Pide que dibuje los pasos en la cuadrícula. Reconoce comparar los dos órdenes.",
    ),
    reinforce="Mueve una moneda por una cuadrícula con tres instrucciones (traslación, reflexión, traslación) y anota dónde queda en cada paso.",
    extend="Describe con dos transformaciones cómo llevar el punto (1, 1) hasta (6, 3).",
)

# ================================================================ OA 19
register(
    OA19, 1,
    materials="Lápiz, papel y, si tienes, una hoja rectangular con esquinas rectas para comparar. El transportador se usa en las clases siguientes.",
    use="Aprenderé a estimar la medida de un ángulo antes de medirlo. Sirve para detectar errores al leer el transportador.",
    prior=["Sé qué es un ángulo.", "Conozco el ángulo recto y la vuelta completa."],
    explain=[
        "Un ángulo se forma por dos lados que parten de un mismo punto, el vértice. Se mide en grados (°). Un ángulo recto mide 90° y se parece a la esquina de una hoja. Un ángulo llano mide 180° y se ve como una línea recta.",
        "Un ángulo agudo mide menos de 90°. Un ángulo obtuso mide más de 90° y menos de 180°. Para estimar, compara con la esquina de una hoja. Si es más cerrado, es agudo. Si es más abierto, es obtuso. La mitad de un ángulo recto mide 45°.",
        "Estimar antes de medir ayuda a corregir. Si ves un ángulo agudo y al medir lees 130°, tienes un error: seguramente leíste la escala equivocada. Debes tener una idea aproximada del resultado antes de usar el transportador.",
    ],
    vocab=[("ángulo", "abertura entre dos lados que parten de un mismo punto"), ("grado (°)", "unidad para medir ángulos"), ("ángulo recto", "ángulo de 90°, como la esquina de una hoja"), ("ángulo agudo", "ángulo menor que 90°"), ("ángulo obtuso", "ángulo mayor que 90° y menor que 180°")],
    worked=[
        {"title": "Clasificar por estimación", "problem": "Un ángulo se ve más abierto que la esquina de una hoja, pero menos que una línea recta. ¿Qué tipo es?", "steps": ["Lo comparo con la esquina de una hoja, que mide 90°: este ángulo es más abierto.", "También es más cerrado que una línea recta, que mide 180°.", "Más abierto que 90° y menos que 180° es obtuso."], "answer": "Obtuso"},
        {"title": "Estimar un valor", "problem": "Un ángulo se ve como la mitad de la esquina de una hoja. ¿Cuánto mide, aproximadamente?", "steps": ["La esquina de una hoja mide 90°.", "La mitad de 90° es 45°."], "answer": "45°"},
    ],
    mistakes=[
        {"wrong": "Decir que 100° es un ángulo agudo porque es «poquito más» que 90°.", "why": "No se compara con 90°.", "fix": "Mayor que 90° y menor que 180° es obtuso."},
        {"wrong": "Medir un ángulo agudo y escribir 130° sin revisar.", "why": "No se estimó antes de medir.", "fix": "Un ángulo agudo mide menos de 90°. Seguramente leíste la otra escala del transportador."},
    ],
    tiers={
        "recovery": [
            ex("Un ángulo es más abierto que la esquina de una hoja y más cerrado que una línea recta. ¿Qué tipo de ángulo es?", "Obtuso", "Mide más de 90° y menos de 180°."),
            ex("Un ángulo es más cerrado que la esquina de una hoja. ¿Qué tipo de ángulo es?", "Agudo", "Mide menos de 90°."),
            ex("¿Cuántos grados mide la esquina de una hoja de cuaderno?", "90°", "Es un ángulo recto."),
        ],
        "understand": [
            ex("Un ángulo parece la mitad de un ángulo recto. ¿Cuánto mide, aproximadamente?", "45°", "La mitad de 90° es 45°."),
            ex("¿Por qué conviene estimar antes de medir un ángulo?", "Para detectar errores al leer el transportador", "Así sabes si el resultado tiene sentido."),
            ex("¿Cómo se ve un ángulo de 180°?", "Como una línea recta", "Sus dos lados forman una línea."),
        ],
        "apply": [
            ex("Clasifica los ángulos de 30°, 90°, 130° y 180° en orden como agudo, recto, obtuso o llano.", "30° agudo; 90° recto; 130° obtuso; 180° llano", "Se compara cada medida con 90° y 180°."),
            ex("Un ángulo se ve apenas más abierto que la esquina de una hoja. ¿Cuál es la mejor estimación: 60°, 100° o 170°?", "100°", "Es un poco más que 90°."),
            ex("Un ángulo se ve como la mitad de la esquina de una hoja. ¿Cuál es la mejor estimación: 20°, 45° o 135°?", "45°", "La mitad de 90° es 45°."),
        ],
        "reason": [
            ex("Ana midió un ángulo agudo y leyó 130°. ¿Es razonable? ¿Qué pudo pasar?", "No; un agudo mide menos de 90°, así que leyó la escala equivocada", "130° es mayor que 90°, por eso no puede ser un ángulo agudo."),
            ex("Beto dice que 100° es agudo porque es poquito más que 90°. ¿Tiene razón?", "No; es obtuso", "Todo ángulo mayor que 90° y menor que 180° es obtuso."),
        ],
        "challenge": [
            ex("Se juntan un ángulo recto y un ángulo de 45° uno al lado del otro. ¿Cuánto mide el ángulo total?", "135°", "90° + 45° = 135°."),
            ex("Se juntan dos ángulos rectos uno al lado del otro. ¿Qué ángulo forman?", "Un ángulo llano de 180°", "90° + 90° = 180°."),
        ],
    },
    context=[ex("A las 3:00 en punto, la aguja larga de un reloj apunta al 12 y la corta al 3. ¿Qué tipo de ángulo forman las agujas?", "Un ángulo recto", "Del 12 al 3 hay un cuarto de vuelta, o 90°.")],
    selfcheck=[
        ex("¿Un ángulo de 60° es agudo, recto u obtuso?", "Agudo", "Es menor que 90°."),
        ex("¿Un ángulo de 150° es agudo, recto u obtuso?", "Obtuso", "Es mayor que 90° y menor que 180°."),
        ex("¿Cuántos grados mide un ángulo llano?", "180°", "Es una línea recta."),
    ],
    open_task=task(
        "Mira tres esquinas u objetos de tu casa (por ejemplo, la esquina de una hoja, el ángulo entre la tapa abierta de un libro y la mesa, o las agujas de un reloj a las 2:00). Compáralos con la esquina de una hoja y clasifícalos como agudos, rectos u obtusos. Escribe una estimación en grados para cada uno.",
        "Esquina de hoja: recto, 90°. Libro medio abierto: obtuso, unos 120°. Agujas a las 2:00: agudo, unos 60°.",
        ["compara con la esquina de una hoja", "clasifica cada ángulo", "escribe una estimación razonable"],
        ["tres ángulos", "clasificación y estimación"],
        ["no comparar con 90°", "estimar fuera del rango del tipo"],
        "Pide que ponga la esquina de la hoja sobre cada ángulo. Reconoce la comparación con el ángulo recto.",
    ),
    reinforce="Abre y cierra un libro y observa cuándo el ángulo es agudo, recto y obtuso. Estima cuántos grados mide cada vez.",
    extend="Dibuja a mano alzada ángulos que estimes de 45°, 90° y 135° y luego compáralos con la esquina de una hoja.",
)

register(
    OA19, 2,
    materials="Lápiz, papel y un transportador (instrumento semicircular con grados). Si no tienes, imagina uno con las lecturas que se dan en cada ejercicio.",
    use="Aprenderé a colocar bien el transportador y a leer la escala correcta. Sirve para medir con precisión.",
    prior=["Sé estimar si un ángulo es agudo, recto u obtuso.", "Sé qué es el vértice."],
    explain=[
        "El transportador tiene forma de medio círculo y una escala de 0° a 180°. Casi todos tienen dos escalas, una de izquierda a derecha y otra de derecha a izquierda. Para medir, sigue estos pasos: pon el centro del transportador sobre el vértice del ángulo.",
        "Luego alinea la línea base del transportador, la que marca el 0°, con uno de los lados del ángulo. Lee en la escala que empieza en 0° en ese lado. El otro lado del ángulo pasa por un número: esa es la medida.",
        "Las dos escalas se complementan: en una misma raya, los dos números suman 180°. Por ejemplo, si una raya marca 65° en una escala, marca 115° en la otra. Usa la estimación: si el ángulo es agudo, elige el número menor que 90°.",
    ],
    vocab=[("transportador", "instrumento para medir ángulos"), ("centro del transportador", "punto que se pone sobre el vértice"), ("línea base", "línea del transportador que marca el 0°"), ("escala", "serie de números ordenados para leer una medida"), ("vértice", "punto donde se juntan los dos lados del ángulo")],
    worked=[
        {"title": "Leer en la escala correcta", "problem": "Un lado del ángulo pasa por el 0° de la escala exterior. El otro lado pasa por 65° en esa escala y por 115° en la interior. ¿Cuánto mide?", "steps": ["Se lee la escala que empieza en 0° sobre el lado base.", "Esa escala marca 65°.", "Estimación: se ve agudo, y 65° es menor que 90°."], "answer": "65°"},
        {"title": "Las escalas suman 180°", "problem": "Una raya marca 40° en una escala. ¿Qué marca en la otra?", "steps": ["Las dos lecturas suman 180°.", "180° − 40° = 140°."], "answer": "140°"},
    ],
    mistakes=[
        {"wrong": "Poner el centro del transportador en el extremo de un lado y no en el vértice.", "why": "El centro no coincide con el vértice.", "fix": "El centro del transportador va justo sobre el vértice."},
        {"wrong": "Leer 120° para un ángulo agudo, porque usó la escala que no empieza en 0° sobre su lado.", "why": "No se alinea la lectura con la línea base.", "fix": "La medida correcta es 180° − 120° = 60°."},
    ],
    tiers={
        "recovery": [
            ex("¿Dónde se coloca el centro del transportador?", "Sobre el vértice del ángulo", "Ahí se juntan los lados."),
            ex("¿Con qué se alinea la línea base (el 0°) del transportador?", "Con uno de los lados del ángulo", "Desde ahí se lee la medida."),
            ex("Un lado del ángulo pasa por el 0° de una escala y el otro lado pasa por 65° en esa misma escala. ¿Cuánto mide el ángulo?", "65°", "Se lee el número de la escala que parte en 0°."),
        ],
        "understand": [
            ex("Si un ángulo agudo marca 72° y 108° en las dos escalas, ¿cuál es su medida correcta?", "72°", "Un agudo mide menos de 90°."),
            ex("En una raya del transportador, ¿cuánto suman los dos números de las escalas?", "180°", "Las escalas se complementan."),
            ex("Si el centro del transportador no está en el vértice, ¿la lectura es confiable?", "No", "Hay que alinear el centro con el vértice."),
        ],
        "apply": [
            ex("Un lado pasa por el 0° y el otro por 130° en la misma escala. ¿Cuánto mide y qué tipo es?", "130°; obtuso", "Es mayor que 90° y menor que 180°."),
            ex("La línea base está sobre el 0° de la escala de la derecha. El otro lado cruza 40° en esa escala y 140° en la de la izquierda. ¿Cuánto mide?", "40°", "Se lee la escala que parte en 0° sobre el lado."),
            ex("Una raya marca 115° en una escala. ¿Cuánto marca en la otra?", "65°", "180° − 115° = 65°."),
        ],
        "reason": [
            ex("Pía puso el centro del transportador en la punta de un lado en vez de en el vértice y leyó 70°. ¿Qué error cometió?", "No alineó el centro con el vértice", "La lectura no es confiable así."),
            ex("Raúl leyó 120° en un ángulo agudo porque usó la escala que no parte en 0° sobre su lado. ¿Cuál es la medida correcta?", "60°", "180° − 120° = 60° y 60° es agudo."),
        ],
        "challenge": [
            ex("Una raya marca 35° en una escala. ¿Cuánto marca en la otra?", "145°", "180° − 35° = 145°."),
            ex("Una raya marca 95° en una escala. ¿Cuánto marca en la otra?", "85°", "180° − 95° = 85°."),
        ],
    },
    context=[ex("Mides la inclinación de una rampa de juguete, que se ve como un ángulo agudo, y la raya marca 25° y 155°. ¿Cuál es la medida?", "25°", "Un ángulo agudo mide menos de 90°.")],
    selfcheck=[
        ex("Un ángulo obtuso marca 70° y 110° en las dos escalas. ¿Cuál es su medida?", "110°", "Un obtuso mide más de 90°."),
        ex("¿Qué número de la otra escala corresponde a 90°?", "90°", "180° − 90° = 90°."),
        ex("¿En qué punto del ángulo va el centro del transportador?", "En el vértice", "Ahí se juntan los lados."),
    ],
    open_task=task(
        "Describe en una lista de pasos cómo medir un ángulo con el transportador. Luego aplica los pasos a este caso: un ángulo agudo, cuya raya marca 50° en una escala y 130° en la otra. Escribe qué medida eliges y por qué.",
        "Pasos: centro en el vértice; línea base sobre un lado; leer la escala que parte en 0°. Caso: elijo 50° porque el ángulo es agudo.",
        ["lista los pasos en orden", "elige la escala correcta", "explica con la estimación"],
        ["lista de pasos", "medida y razón"],
        ["no poner el centro en el vértice", "leer la escala equivocada"],
        "Pide que verifique cada paso con el instrumento. Reconoce la estimación como control de la lectura.",
    ),
    reinforce="Si tienes transportador, mide la esquina de una hoja y comprueba que da 90°.",
    extend="Escribe, para cinco medidas que elijas, el número de la otra escala. Por ejemplo, 20° y 160°.",
)

register(
    OA19, 3,
    materials="Lápiz, regla y transportador. Si no tienes transportador, imagina uno con las lecturas que se dan.",
    use="Aprenderé a construir un ángulo de una medida dada con el transportador. Sirve para dibujar figuras con ángulos exactos.",
    prior=["Sé colocar el transportador sobre un ángulo.", "Sé leer la escala correcta."],
    explain=[
        "Para construir un ángulo de una medida dada, primero dibuja un lado con la regla. Marca un punto en un extremo: ese es el vértice. Luego coloca el centro del transportador sobre el vértice y la línea base sobre el lado dibujado.",
        "Busca en la escala que parte en 0° sobre tu lado el número pedido y marca un punto junto a él. Saca el transportador y une el vértice con ese punto usando la regla. El segundo lado forma con el primero el ángulo que querías.",
        "Antes de dibujar, estima: un ángulo de 110° debe verse obtuso; uno de 35°, agudo. Después de dibujarlo, comprueba con la esquina de una hoja o midiéndolo de nuevo. Si te equivocaste de escala, formarás el ángulo suplementario: 180° menos la medida pedida.",
    ],
    vocab=[("construir", "dibujar un ángulo con una medida pedida"), ("vértice", "punto donde empiezan los dos lados"), ("lado", "cada una de las líneas del ángulo"), ("suplementario", "que suma 180° con otro ángulo"), ("estimar", "calcular una medida aproximada")],
    worked=[
        {"title": "Ordenar los pasos", "problem": "Ordena los pasos para construir un ángulo de 70°: A) marcar un punto junto a la raya del 70° en la escala que parte en 0°; B) dibujar un lado y marcar el vértice; C) poner el centro en el vértice y el 0° sobre el lado; D) unir el vértice con el punto marcado.", "steps": ["Primero se dibuja el lado y el vértice: B.", "Luego se coloca el transportador: C.", "Se marca el punto en 70°: A.", "Finalmente se une con la regla: D."], "answer": "B, C, A, D"},
        {"title": "Corregir una escala", "problem": "Quieres construir 50°, pero marcaste el punto junto al 130° de la otra escala. ¿Qué ángulo formaste?", "steps": ["El punto marcado está en 130° en la escala que parte en 0° sobre tu lado.", "Entonces formaste un ángulo de 130°."], "answer": "130°, que es obtuso"},
    ],
    mistakes=[
        {"wrong": "Construir 40° y marcar el punto en 140° de la otra escala.", "why": "Se usa la escala que no parte en 0° sobre el lado dibujado.", "fix": "Marca el punto junto al 40° en la escala que parte en 0° sobre tu lado."},
        {"wrong": "Dibujar los dos lados sin marcar el vértice y luego medir.", "why": "Sin el vértice no sabes dónde poner el centro del transportador.", "fix": "Marca el vértice al comenzar."},
    ],
    tiers={
        "recovery": [
            ex("Ordena los pasos para construir un ángulo de 55°: A) marcar un punto junto a la raya del 55°; B) unir el vértice con el punto marcado; C) dibujar un lado y marcar el vértice; D) poner el centro del transportador en el vértice y el 0° sobre el lado. Escribe las letras en orden.", "C, D, A, B", "Primero el lado y el vértice, luego el transportador, la marca y el segundo lado."),
            ex("Para construir un ángulo de 70°, ¿junto a qué número marcas el punto?", "Junto al 70°", "Es la medida pedida en la escala que parte en 0°."),
            ex("Para construir un ángulo de 90°, ¿qué tipo de ángulo formas?", "Un ángulo recto", "90° es un ángulo recto."),
        ],
        "understand": [
            ex("¿Por qué se dibuja primero un lado y se marca el vértice?", "Para tener la línea base y el lugar del centro del transportador", "Sin ellos no se puede colocar el instrumento."),
            ex("Quieres construir 35°, pero marcas el punto junto al 145° de la otra escala. ¿Qué ángulo formaste?", "Uno de 145°", "El punto marca la abertura que formó."),
            ex("¿Cómo puedes revisar un ángulo recién construido de 90°?", "Con la esquina de una hoja", "Una esquina de hoja mide 90°."),
        ],
        "apply": [
            ex("Vas a construir 110°. ¿Será un ángulo agudo, recto u obtuso?", "Obtuso", "110° es mayor que 90° y menor que 180°."),
            ex("Vas a construir 35°. ¿Será un ángulo agudo, recto u obtuso?", "Agudo", "35° es menor que 90°."),
            ex("Construyes 60° y luego 120° desde el mismo lado base. ¿Cuál de los dos está más abierto?", "El de 120°", "120° es mayor que 60°."),
        ],
        "reason": [
            ex("Tomás quería 40° y marcó el punto en 140°. ¿Qué escala usó mal y qué ángulo formó?", "Usó la escala que no parte en 0° sobre su lado; formó 140°", "La medida pedida estaba en la otra escala."),
            ex("Eli dibujó dos lados sin marcar el vértice. ¿Qué dificultad tendrá para usar el transportador?", "No sabrá dónde poner el centro", "El centro debe ir sobre el vértice."),
        ],
        "challenge": [
            ex("Construyes un ángulo de 50° y justo al lado otro de 40°, compartiendo un lado. ¿Cuánto mide el ángulo total?", "90°", "50° + 40° = 90°."),
            ex("Un ángulo llano de 180° se divide en dos ángulos y uno mide 75°. ¿Cuánto mide el otro?", "105°", "180° − 75° = 105°."),
        ],
    },
    context=[ex("Quieres dibujar la abertura de un abanico de papel de 120°. ¿Será un ángulo agudo, recto u obtuso?", "Obtuso", "120° es mayor que 90°.")],
    selfcheck=[
        ex("¿En qué escala marcas el punto para construir 65°?", "En la que parte en 0° sobre el lado dibujado", "Así la lectura es la medida pedida."),
        ex("Quieres un ángulo de 30°. ¿Se verá más cerrado o más abierto que la esquina de una hoja?", "Más cerrado", "30° es menor que 90°."),
        ex("Construyes 25° y 65° juntos. ¿Cuánto mide el ángulo total?", "90°", "25° + 65° = 90°."),
    ],
    open_task=task(
        "Con regla y transportador (o con las lecturas imaginadas), construye dos ángulos: uno de 40° y otro de 130°. Escribe qué tipo de ángulo es cada uno antes de dibujarlo. Después comprueba comparando con la esquina de una hoja.",
        "40°: agudo, más cerrado que la esquina de la hoja. 130°: obtuso, más abierto que la esquina.",
        ["estima el tipo antes de construir", "dibuja con vértice y dos lados", "comprueba con la esquina de una hoja"],
        ["dos ángulos", "comprobación"],
        ["leer la escala equivocada", "no marcar el vértice"],
        "Pide que compare cada ángulo con la esquina de una hoja. Reconoce la estimación como control.",
    ),
    reinforce="Dibuja un ángulo de 60° y otro de 120° con el mismo lado base. Compara cuál está más abierto.",
    extend="Construye dos ángulos que juntos formen 180° y comprueba que sus lados exteriores forman una línea recta.",
)

register(
    OA19, 4,
    materials="Lápiz y papel. Si tienes, un transportador.",
    use="Aprenderé a comparar ángulos, calcular cuánto más grande es uno que otro y corregir construcciones. Sirve para revisar mi trabajo.",
    prior=["Sé construir un ángulo con el transportador.", "Sé que dos escalas suman 180°."],
    explain=[
        "Para comparar ángulos, compara sus medidas en grados. 120° es mayor que 70°. Para saber cuánto más grande es, resta: 120° − 70° = 50°. El tamaño de un ángulo no depende del largo de sus lados, sino de su abertura.",
        "Dos ángulos de 60° son iguales aunque uno tenga los lados más largos. Si dos ángulos suman 180°, uno se llama suplementario del otro. Por ejemplo, 35° y 145° suman 180°.",
        "Para corregir una construcción, compara con tu estimación. Si pediste 35° y tu ángulo parece obtuso, lo hiciste con la escala equivocada. La medida correcta es 180° menos la que te salió. Ordena ángulos por su medida, no por cómo se ven los lados.",
    ],
    vocab=[("comparar", "ver cuál es mayor, menor o igual"), ("abertura", "qué tan abiertos están los lados del ángulo"), ("diferencia", "resultado de restar dos medidas"), ("suplementarios", "dos ángulos que suman 180°"), ("corregir", "arreglar un error")],
    worked=[
        {"title": "Cuánto más grande", "problem": "¿Cuántos grados más mide un ángulo de 150° que uno de 70°?", "steps": ["Se resta la medida menor a la mayor.", "150° − 70° = 80°."], "answer": "80°"},
        {"title": "Lados largos no importan", "problem": "Un ángulo de 60° tiene lados muy largos y otro de 60° tiene lados cortos. ¿Cuál es mayor?", "steps": ["El tamaño depende de la abertura, no del largo de los lados.", "Ambos miden 60°."], "answer": "Son iguales"},
    ],
    mistakes=[
        {"wrong": "Decir que el ángulo con los lados más largos es mayor.", "why": "Se confunde la abertura con el largo.", "fix": "La abertura es lo que se mide. Mide los grados."},
        {"wrong": "Decir que un ángulo de 80° es mayor que 90° porque «se ve grande».", "why": "No se compara con 90°.", "fix": "80° es menor que 90°: es agudo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál ángulo es mayor: 70° o 110°?", "110°", "110° es mayor que 70°."),
            ex("Ordena de menor a mayor los ángulos de 90°, 30° y 150°.", "30°, 90°, 150°", "Se comparan los números de grados."),
            arith("¿Cuántos grados más mide un ángulo de 120° que uno de 45°?", "120-45", "Se resta la medida menor a la mayor."),
        ],
        "understand": [
            ex("¿El tamaño de un ángulo depende del largo de sus lados?", "No; depende de su abertura", "Se mide en grados."),
            ex("Dos ángulos de 60° tienen lados de distinto largo. ¿Son iguales?", "Sí", "Los dos tienen la misma abertura."),
            ex("Mides un ángulo que ves obtuso y lees 40°. ¿Qué debes revisar?", "La escala que usaste; sería 140°", "Un obtuso mide más de 90°."),
        ],
        "apply": [
            arith("¿Cuántos grados más mide un ángulo de 160° que uno de 85°?", "160-85", "Se resta la medida menor a la mayor."),
            ex("Entre los ángulos de 25°, 100° y 60°, ¿cuál es el mayor ángulo agudo?", "60°", "100° es obtuso, así que no cuenta."),
            arith("Dos ángulos suman 180° y uno mide 35°. ¿Cuánto mide el otro?", "180-35", "Se resta al ángulo llano."),
        ],
        "reason": [
            ex("Iván dice que el ángulo con los lados más largos es mayor. ¿Tiene razón?", "No; importa la abertura", "El largo de los lados no cambia los grados."),
            ex("Sofía construyó un ángulo de 80° y dice que es mayor que un recto porque se ve grande. ¿Qué le dirías?", "Que es agudo, porque 80° es menor que 90°", "Se compara con 90°."),
        ],
        "challenge": [
            ex("Ordena de mayor a menor los ángulos de 45°, 135°, 90° y 20°.", "135°, 90°, 45°, 20°", "Se comparan los grados."),
            ex("Un ángulo mide el doble de 35° y otro mide la mitad de 100°. ¿Cuál es mayor?", "El primero, de 70°", "El segundo mide 50°."),
        ],
    },
    context=[arith("Una puerta se abre 30° y otra se abre 75°. ¿Cuántos grados más está abierta la segunda?", "75-30", "Se resta la abertura menor a la mayor.")],
    selfcheck=[
        ex("¿Cuál ángulo es menor: 95° o 85°?", "85°", "85° es menor que 95°."),
        arith("¿Cuántos grados más mide 160° que 100°?", "160-100", "Se resta la medida menor a la mayor."),
        ex("Si un ángulo parece obtuso y mides 50°, ¿qué número esperas en la otra escala?", "130°", "180° − 50° = 130°."),
    ],
    open_task=task(
        "Elige tres medidas: A) 30°, 90°, 150°; o B) 45°, 100°, 135°. Ordénalas de menor a mayor, calcula cuántos grados más es la mayor que la menor, y clasifica cada una como aguda, recta u obtusa.",
        "A) 30° (aguda), 90° (recta), 150° (obtusa). La mayor excede a la menor en 150° − 30° = 120°.",
        ["ordena bien las medidas", "calcula la diferencia", "clasifica cada ángulo"],
        ["lista ordenada", "diferencia", "clasificación"],
        ["restar al revés", "confundir tipos de ángulo"],
        "Pide que justifique cada clasificación con 90° y 180°. Reconoce la comparación con los referentes.",
    ),
    reinforce="Dibuja a mano tres ángulos y ordénalos a ojo de menor a mayor. Después compruébalo con transportador o con la esquina de una hoja.",
    extend="Escribe cinco pares de ángulos suplementarios que sumen 180°.",
)

# ================================================================ OA 20
register(
    OA20, 1,
    materials="Lápiz y papel. Si quieres, un reloj de pared o un reloj digital.",
    use="Aprenderé a distinguir si una hora es de la mañana (a.m.) o de la tarde y la noche (p.m.). Sirve para no confundir las 7:00 de la mañana con las 7:00 de la noche.",
    prior=["Sé leer horas y medias horas en relojes con agujas.", "Sé que un día tiene 24 horas."],
    explain=[
        "El día tiene 24 horas, pero el reloj de agujas solo tiene 12 números. Por eso la aguja de las horas da dos vueltas completas en un día. Para distinguir las dos vueltas se usan las letras a.m. y p.m.",
        "a.m. se usa para las horas desde la medianoche hasta antes del mediodía. Por ejemplo, las 7:00 de la mañana son 7:00 a.m. p.m. se usa desde el mediodía hasta antes de la medianoche. Las 3:00 de la tarde y las 9:00 de la noche son 3:00 p.m. y 9:00 p.m.",
        "El mediodía es las 12:00 del día y se escribe 12:00 p.m. La medianoche marca el comienzo de un nuevo día. Para saber cuántas horas pasan entre dos momentos, cuenta desde uno hasta el otro. Si cruzas el mediodía o la medianoche, ten cuidado con a.m. y p.m.",
    ],
    vocab=[("a.m.", "horas desde la medianoche hasta antes del mediodía"), ("p.m.", "horas desde el mediodía hasta antes de la medianoche"), ("mediodía", "las 12:00 del día"), ("medianoche", "momento en que termina un día y empieza otro"), ("reloj análogo", "reloj con agujas")],
    worked=[
        {"title": "Elegir a.m. o p.m.", "problem": "Tomas desayuno a las 8:15 de la mañana. ¿Cómo se escribe esa hora?", "steps": ["La mañana va entre la medianoche y el mediodía.", "Por eso se usa a.m."], "answer": "8:15 a.m."},
        {"title": "Contar horas entre dos momentos", "problem": "¿Cuántas horas pasan desde las 10:00 a.m. hasta las 2:00 p.m.?", "steps": ["De 10:00 a.m. a 12:00 hay 2 horas.", "De las 12:00 a las 2:00 p.m. hay 2 horas más.", "2 + 2 = 4."], "answer": "4 horas"},
    ],
    mistakes=[
        {"wrong": "Decir que las 9:00 de la noche son 9:00 a.m.", "why": "Se confunde la noche con la mañana.", "fix": "La noche está después del mediodía: 9:00 p.m."},
        {"wrong": "Decir que de las 10:00 a.m. a las 2:00 p.m. pasan 8 horas porque 10 − 2 = 8.", "why": "Se restan los números sin pasar por las 12:00.", "fix": "Cuenta 2 horas hasta las 12:00 y 2 más: 4 horas."},
    ],
    tiers={
        "recovery": [
            ex("Te despiertas a las 7:00 de la mañana. ¿Es a.m. o p.m.?", "a.m.", "Es antes del mediodía."),
            ex("Cenas a las 8:00 de la noche. ¿Es a.m. o p.m.?", "p.m.", "Es después del mediodía."),
            ex("Almuerzas a la 1:00 de la tarde. ¿Es a.m. o p.m.?", "p.m.", "La tarde es después del mediodía."),
        ],
        "understand": [
            ex("¿Qué horas del día se marcan con a.m.?", "Desde la medianoche hasta antes del mediodía", "Es la primera mitad del día."),
            ex("¿Cuántas horas tiene un día completo?", "24", "Son dos vueltas del reloj de 12 horas."),
            ex("¿Cuántas vueltas da la aguja de las horas en un día?", "2", "Cada vuelta mide 12 horas."),
        ],
        "apply": [
            ex("Escribe con a.m. o p.m.: desayunas a las 8:15 de la mañana.", "8:15 a.m.", "La mañana es a.m."),
            ex("Escribe con a.m. o p.m.: sales del colegio a las 3:30 de la tarde.", "3:30 p.m.", "La tarde es p.m."),
            ex("Escribe con a.m. o p.m.: te acuestas a las 11:45 de la noche.", "11:45 p.m.", "La noche antes de la medianoche es p.m."),
        ],
        "reason": [
            ex("Ana dice que las 9:00 de la noche son 9:00 a.m. ¿Qué error cometió?", "La noche es p.m., no a.m.", "Después del mediodía se usa p.m."),
            ex("Beto dice que de las 10:00 a.m. a las 2:00 p.m. pasan 8 horas porque 10 − 2 = 8. ¿Tiene razón?", "No; pasan 4 horas", "Hay 2 horas hasta el mediodía y 2 después."),
        ],
        "challenge": [
            arith("¿Cuántas horas pasan desde las 8:00 a.m. hasta las 5:00 p.m.? Cuenta 4 horas hasta las 12:00 y suma las horas desde el mediodía.", "4+5", "Se suman las dos partes."),
            arith("¿Cuántas horas pasan desde las 9:00 p.m. hasta las 6:00 a.m. del día siguiente? Hay 3 horas hasta la medianoche.", "3+6", "Se suman las horas hasta la medianoche y desde ella."),
        ],
    },
    context=[ex("Un niño duerme desde las 9:30 p.m. hasta las 7:30 a.m. del día siguiente. Hasta la medianoche hay 2 horas y 30 minutos, y de la medianoche a las 7:30 a.m. hay 7 horas y 30 minutos. ¿Cuántas horas durmió?", "10 horas", "2 h 30 min más 7 h 30 min son 10 horas.")],
    selfcheck=[
        ex("¿Las 6:00 de la mañana son a.m. o p.m.?", "a.m.", "Es antes del mediodía."),
        ex("¿Las 5:00 de la tarde son a.m. o p.m.?", "p.m.", "Es después del mediodía."),
        ex("¿Cómo se escribe el mediodía?", "12:00 p.m.", "Ahí empieza la tarde."),
    ],
    open_task=task(
        "Escribe cinco actividades de un día normal tuyo con su hora y a.m. o p.m. Por ejemplo: desayuno, ir al colegio, almuerzo, tarea y dormir. Marca la actividad que ocurre antes del mediodía y la que ocurre más cerca de la medianoche.",
        "Desayuno 8:00 a.m.; colegio 9:00 a.m.; almuerzo 1:00 p.m.; tarea 5:00 p.m.; dormir 9:30 p.m. Antes del mediodía: desayuno. Más cerca de la medianoche: dormir.",
        ["cinco actividades con hora", "usa a.m. y p.m. correctamente", "marca la más cercana a la medianoche"],
        ["lista de actividades"],
        ["usar a.m. para horas de la noche", "olvidar p.m."],
        "Pide que explique por qué eligió a.m. o p.m. para cada hora. Reconoce que ubica la hora en el día.",
    ),
    reinforce="Mira un reloj de agujas durante un día y anota una hora a.m. y una hora p.m. en que ves la aguja corta en el mismo número.",
    extend="Escribe dos horas en punto en que la aguja corta esté en el 4, una a.m. y otra p.m., y di qué haces tú en cada una.",
)

register(
    OA20, 2,
    materials="Lápiz y papel.",
    use="Aprenderé a pasar entre el formato de 12 horas y el de 24 horas. Sirve para leer horarios de buses, trenes y aviones.",
    prior=["Sé distinguir a.m. y p.m.", "Sé sumar 12."],
    explain=[
        "El formato de 24 horas cuenta las horas del día de 00 a 23 sin usar a.m. ni p.m. La medianoche es 00:00. Las horas de la mañana se escriben igual, con dos dígitos: 7:30 a.m. es 07:30. El mediodía es 12:00.",
        "Para las horas p.m. desde la 1:00 p.m., se suman 12 horas. 1:00 p.m. es 13:00, 3:00 p.m. es 15:00 y 9:30 p.m. es 21:30. Los minutos no cambian.",
        "Para volver al formato de 12 horas, resta 12 a las horas desde 13:00 en adelante y escribe p.m. 18:45 es 6:45 p.m. Las horas de 01:00 a 11:59 se escriben a.m. Después de las 23:59 comienza 00:00 del día siguiente.",
    ],
    vocab=[("formato de 24 horas", "forma de escribir la hora con números de 00 a 23"), ("00:00", "la medianoche, comienzo del día"), ("12:00", "el mediodía"), ("sumar 12", "paso para pasar de p.m. a 24 horas"), ("minutos", "parte de la hora que no cambia al convertir")],
    worked=[
        {"title": "De p.m. a 24 horas", "problem": "Escribe 9:30 p.m. en formato de 24 horas.", "steps": ["Es p.m., así que sumo 12 a las horas.", "9 + 12 = 21.", "Los minutos no cambian."], "answer": "21:30"},
        {"title": "De 24 horas a p.m.", "problem": "Escribe 18:45 en formato de 12 horas.", "steps": ["18 es mayor que 12, así que resto 12.", "18 − 12 = 6.", "Es p.m."], "answer": "6:45 p.m."},
    ],
    mistakes=[
        {"wrong": "Escribir 4:00 p.m. como 14:00 por sumar 10.", "why": "Se suma una cantidad equivocada.", "fix": "Se suman 12: 4 + 12 = 16, o sea 16:00."},
        {"wrong": "Escribir 24:30 para la media hora después de la medianoche.", "why": "Se usa 24 como hora.", "fix": "La hora después de las 23:59 es 00:00; media hora después es 00:30."},
    ],
    tiers={
        "recovery": [
            ex("Escribe 3:00 p.m. en formato de 24 horas.", "15:00", "3 + 12 = 15."),
            ex("Escribe 7:30 a.m. en formato de 24 horas.", "07:30", "Las horas de la mañana no cambian."),
            ex("Escribe las 12:00 del día (mediodía) en formato de 24 horas.", "12:00", "El mediodía se escribe igual."),
        ],
        "understand": [
            ex("¿Cuántas horas se suman a una hora p.m. (de 1 a 11) para escribirla en formato de 24 horas?", "12", "Así se pasa a la segunda mitad del día."),
            ex("Al pasar una hora a.m. a formato de 24 horas, ¿cambia el número de la hora?", "No", "Solo se escribe con dos dígitos."),
            ex("¿Qué hora representa 00:00?", "La medianoche", "Es el comienzo del día."),
        ],
        "apply": [
            ex("Escribe 10:20 p.m. en formato de 24 horas.", "22:20", "10 + 12 = 22."),
            ex("Escribe 17:05 en formato de 12 horas, con a.m. o p.m.", "5:05 p.m.", "17 − 12 = 5."),
            ex("Escribe 05:10 en formato de 12 horas, con a.m. o p.m.", "5:10 a.m.", "Es una hora de la mañana."),
        ],
        "reason": [
            ex("Luis dice que 4:00 p.m. es 14:00 porque sumó 10. ¿Qué error cometió y cuál es la respuesta?", "Debió sumar 12; es 16:00", "4 + 12 = 16."),
            ex("Ema escribe 24:30 para la media hora después de la medianoche. ¿Cómo se escribe bien?", "00:30", "La medianoche es 00:00."),
        ],
        "challenge": [
            arith("¿Cuántas horas hay entre las 08:00 y las 17:00?", "17-8", "Se resta la hora de inicio a la de término."),
            ex("Una película empieza a las 19:30 y dura 2 horas. ¿A qué hora termina, en formato de 24 horas?", "21:30", "19 + 2 = 21 y los minutos no cambian."),
        ],
    },
    context=[ex("Un bus sale a las 14:20. ¿Cómo se escribe esa hora en formato de 12 horas?", "2:20 p.m.", "14 − 12 = 2.")],
    selfcheck=[
        ex("Escribe 8:15 p.m. en formato de 24 horas.", "20:15", "8 + 12 = 20."),
        ex("Escribe 23:05 en formato de 12 horas.", "11:05 p.m.", "23 − 12 = 11."),
        ex("Escribe 1:00 a.m. en formato de 24 horas.", "01:00", "Las horas a.m. no cambian."),
    ],
    open_task=task(
        "Elige cuatro horas de tu rutina del día (por ejemplo, levantarte, almorzar, estudiar y dormir) y escríbelas en formato de 12 horas con a.m. o p.m. y en formato de 24 horas.",
        "Levantarme: 7:30 a.m. = 07:30. Almorzar: 1:00 p.m. = 13:00. Estudiar: 5:00 p.m. = 17:00. Dormir: 9:30 p.m. = 21:30.",
        ["escribe cuatro horas en ambos formatos", "suma 12 a las p.m.", "mantiene los minutos"],
        ["tabla de horas"],
        ["sumar un número distinto de 12", "escribir 24:00"],
        "Pide que explique la suma de 12 en cada hora p.m. Reconoce la conversión correcta.",
    ),
    reinforce="Mira un horario de buses o la programación de un canal y convierte cinco horas a formato de 12 horas.",
    extend="Crea una tabla de las 24 horas, de 00:00 a 23:00, con su equivalente en formato de 12 horas.",
)

register(
    OA20, 3,
    materials="Lápiz y papel. Si quieres, un reloj de agujas de verdad.",
    use="Aprenderé a leer la hora en relojes de agujas y en relojes digitales. Sirve para entender la hora en cualquier reloj.",
    prior=["Sé leer horas en punto y medias horas.", "Sé contar de 5 en 5."],
    explain=[
        "En un reloj de agujas, la aguja corta marca las horas y la aguja larga marca los minutos. Cada número del reloj representa 5 minutos: el 1 es 5 minutos, el 2 es 10, el 3 es 15, el 6 es 30 y el 9 es 45. Cuando la aguja larga está en el 12, son minutos en punto.",
        "Primero mira la aguja corta. Si está entre dos números, la hora es el número menor (entre el 12 y el 1, la hora es 12). Luego mira la larga. Por ejemplo, si la corta está entre el 4 y el 5 y la larga está en el 6, la hora es 4:30. En un reloj digital, la hora aparece con números, como 4:30 o 16:30.",
        "Para pasar del reloj de agujas al digital, escribe la hora, dos puntos y los minutos con dos dígitos. 7:05 se escribe con un 0 delante del 5. Si el reloj digital usa 24 horas, recuerda sumar 12 a las horas de la tarde y la noche.",
    ],
    vocab=[("aguja corta", "aguja que marca las horas"), ("aguja larga", "aguja que marca los minutos"), ("reloj digital", "reloj que muestra la hora con números"), ("minutos", "partes de la hora: 60 minutos son una hora"), ("en punto", "cuando la aguja larga está en el 12")],
    worked=[
        {"title": "Leer un reloj de agujas", "problem": "La aguja larga está en el 3 y la corta está entre el 7 y el 8. ¿Qué hora es?", "steps": ["La aguja larga en el 3 marca 15 minutos.", "La corta entre el 7 y el 8 marca la hora 7.", "La hora es 7:15."], "answer": "7:15"},
        {"title": "Del reloj digital a 12 horas", "problem": "Un reloj digital muestra 15:40. Escríbelo en formato de 12 horas.", "steps": ["15 es mayor que 12, así que resto 12: 3.", "Es p.m."], "answer": "3:40 p.m."},
    ],
    mistakes=[
        {"wrong": "Leer la aguja larga en el 3 como 3 minutos.", "why": "Se lee el número y no el valor de cada marca.", "fix": "Cada número vale 5 minutos: el 3 es 15 minutos."},
        {"wrong": "Leer larga en el 12 y corta en el 6 como 12:06.", "why": "Se intercambian las agujas.", "fix": "La corta marca la hora: son las 6:00."},
    ],
    tiers={
        "recovery": [
            ex("La aguja larga está en el 3 y la corta está entre el 11 y el 12. ¿Qué hora es?", "11:15", "El 3 son 15 minutos y la hora es 11."),
            ex("La aguja larga está en el 12 y la corta está en el 5. ¿Qué hora es?", "5:00", "La larga en el 12 son minutos en punto."),
            ex("La aguja larga está en el 6 y la corta está entre el 2 y el 3. ¿Qué hora es?", "2:30", "El 6 son 30 minutos y la hora es 2."),
        ],
        "understand": [
            ex("En un reloj de agujas, ¿cuántos minutos representa cada número?", "5", "Los 60 minutos se reparten en 12 números."),
            ex("¿Qué indica la aguja larga?", "Los minutos", "La corta indica las horas."),
            ex("Entre los relojes digitales 4:05 y 4:50, ¿cuál está más cerca de las 5:00?", "4:50", "Faltan 10 minutos para las 5:00."),
        ],
        "apply": [
            ex("La aguja larga está en el 9 y la corta está entre el 10 y el 11. ¿Qué hora es?", "10:45", "El 9 son 45 minutos y la hora es 10."),
            ex("La aguja larga está en el 4 y la corta está entre el 1 y el 2. ¿Qué hora es?", "1:20", "El 4 son 20 minutos y la hora es 1."),
            ex("Un reloj digital muestra 19:25. Escribe la hora en formato de 12 horas.", "7:25 p.m.", "19 − 12 = 7."),
        ],
        "reason": [
            ex("Pablo lee la aguja larga en el 3 y la corta entre el 8 y el 9 como 8:03. ¿Qué error cometió y cuál es la hora?", "Leyó 3 minutos; son 8:15", "Cada número vale 5 minutos."),
            ex("Mía dice que con la aguja larga en el 12 y la corta en el 6 son las 12:06. ¿Tiene razón?", "No; son las 6:00", "La corta marca la hora."),
        ],
        "challenge": [
            ex("¿A qué hora la aguja larga y la aguja corta están las dos justo en el 12?", "A las 12:00", "Es el mediodía o la medianoche."),
            ex("Es de noche. La aguja larga está en el 6 y la corta entre el 11 y el 12. ¿Qué hora es en formato de 24 horas?", "23:30", "Son las 11:30 p.m., y 11 + 12 = 23."),
        ],
    },
    context=[ex("En un reloj de cocina, la aguja larga está en el 9 y la corta entre el 6 y el 7. Es de la mañana. ¿Qué hora es en formato de 24 horas?", "06:45", "El 9 son 45 minutos y la hora es 6.")],
    selfcheck=[
        ex("La aguja larga está en el 2. ¿Cuántos minutos marca?", "10", "Cada número vale 5 minutos y 2 × 5 = 10."),
        ex("Un reloj digital muestra 08:20. ¿Es a.m. o p.m.?", "a.m.", "Es una hora de la mañana."),
        ex("Un reloj digital muestra 21:05. Escríbelo en formato de 12 horas.", "9:05 p.m.", "21 − 12 = 9."),
    ],
    open_task=task(
        "Dibuja dos relojes de agujas con estas horas: 4:30 y 9:45. Escribe cada hora en forma digital de 12 horas con a.m. o p.m. (elige tú la parte del día) y en formato de 24 horas.",
        "4:30 p.m. = 16:30 y 9:45 a.m. = 09:45. La aguja larga marca el 6 y el 9.",
        ["dibuja bien la aguja corta y la larga", "escribe las horas en ambos formatos", "relaciona a.m. o p.m. con las 24 horas"],
        ["dos relojes", "horas escritas"],
        ["intercambiar las agujas", "leer el número como minutos"],
        "Pide que lea cada reloj en voz alta. Reconoce el uso de las dos agujas.",
    ),
    reinforce="Mira un reloj de agujas tres veces durante el día y anota la hora en formato digital.",
    extend="Anota cinco horas en un reloj de agujas dibujado y escribe cada hora en formato de 24 horas.",
)

register(
    OA20, 4,
    materials="Lápiz y papel.",
    use="Aprenderé a leer horarios de la vida diaria y a calcular cuánto dura algo. Sirve para organizar mi día y no llegar tarde.",
    prior=["Sé pasar entre 12 y 24 horas.", "Sé leer la hora en relojes de agujas y digitales."],
    explain=[
        "En la vida diaria, los horarios de buses, trenes y clases suelen usar 24 horas. Así no se confunden las 7:00 de la mañana (07:00) con las 7:00 de la noche (19:00). Para saber cuánto dura algo, resta la hora de inicio a la de término.",
        "Por ejemplo, un bus sale a las 07:40 y otro a las 08:15. De 07:40 a 08:00 hay 20 minutos y de 08:00 a 08:15 hay 15 minutos. En total hay 35 minutos. Una clase de 08:30 a 13:30 dura 5 horas.",
        "Si el inicio no está en punto, cuenta hasta la siguiente hora en punto y suma el resto. De 08:30 a 13:15 son 4 horas y 45 minutos: de 08:30 a 13:30 serían 5 horas, pero faltan 15 minutos. Para saber la hora de término, suma la duración a la hora de inicio.",
    ],
    vocab=[("horario", "lista de horas en que ocurre algo"), ("duración", "tiempo que dura algo"), ("inicio", "hora en que empieza"), ("término", "hora en que termina"), ("intervalo", "tiempo entre dos horas")],
    worked=[
        {"title": "Duración entre dos horas", "problem": "Un bus sale a las 07:40 y otro a las 08:15. ¿Cuántos minutos hay entre ellos?", "steps": ["De 07:40 a 08:00 hay 20 minutos.", "De 08:00 a 08:15 hay 15 minutos.", "20 + 15 = 35."], "answer": "35 minutos"},
        {"title": "Hora de término", "problem": "Un taller empieza a las 15:30 y dura 1 hora 45 minutos. ¿A qué hora termina?", "steps": ["15:30 más 1 hora es 16:30.", "16:30 más 45 minutos: 30 + 45 = 75 minutos, o sea 1 hora y 15 minutos.", "16:30 + 45 min = 17:15."], "answer": "17:15"},
    ],
    mistakes=[
        {"wrong": "Decir que de 08:30 a 13:15 pasan 5 horas 15 minutos.", "why": "Se restan horas y minutos por separado sin considerar que 15 es menor que 30.", "fix": "De 08:30 a 13:30 son 5 horas, y 13:15 es 15 minutos antes: 4 horas 45 minutos."},
        {"wrong": "Decir que el bus de las 7:40 p.m. sale antes que el de las 18:00.", "why": "No se convierte a 24 horas.", "fix": "7:40 p.m. es 19:40, que es después de las 18:00."},
    ],
    tiers={
        "recovery": [
            ex("Un bus sale a las 09:50 y otro a las 10:20. ¿Cuántos minutos hay entre ellos?", "30", "De 09:50 a 10:00 son 10 minutos y de 10:00 a 10:20, 20 minutos."),
            arith("Las clases empiezan a las 08:30 y terminan a las 13:30. ¿Cuántas horas duran?", "13-8", "Los minutos son iguales, así que se restan las horas."),
            ex("Un recreo empieza a las 10:00 y dura 20 minutos. ¿A qué hora termina?", "10:20", "Se suman 20 minutos a las 10:00."),
        ],
        "understand": [
            ex("¿Por qué los horarios de buses suelen usar el formato de 24 horas?", "Para no confundir la mañana con la tarde y la noche", "Cada hora tiene un solo número."),
            ex("¿14:00 y 2:00 a.m. son la misma hora?", "No", "14:00 es 2:00 p.m."),
            ex("Para saber cuánto dura algo, ¿qué operación haces con la hora de término y la de inicio?", "Restar la de inicio a la de término", "La diferencia es el tiempo transcurrido."),
        ],
        "apply": [
            ex("Una película dura de 16:45 a 18:30. ¿Cuánto dura?", "1 hora 45 minutos", "De 16:45 a 17:45 es 1 hora y de 17:45 a 18:30, 45 minutos."),
            ex("Un tren sale a las 21:15 y llega a las 23:20. ¿Cuánto dura el viaje?", "2 horas 5 minutos", "De 21:15 a 23:15 son 2 horas y 5 minutos más."),
            ex("Un taller es de 15:30 a 17:00. Escribe las dos horas en formato de 12 horas.", "3:30 p.m. a 5:00 p.m.", "15 − 12 = 3 y 17 − 12 = 5."),
        ],
        "reason": [
            ex("Jaime dice que de 08:30 a 13:15 pasan 5 horas 15 minutos. ¿Es correcto?", "No; pasan 4 horas 45 minutos", "De 08:30 a 13:30 son 5 horas, y faltan 15 minutos."),
            ex("Sara dice que un bus de las 7:40 p.m. sale antes que otro de las 18:00. ¿Tiene razón?", "No; 7:40 p.m. es 19:40 y sale después", "19:40 es mayor que 18:00."),
        ],
        "challenge": [
            ex("Un taller dura 2 horas 20 minutos y termina a las 17:10. ¿A qué hora empezó?", "14:50", "17:10 menos 2 horas es 15:10 y menos 20 minutos es 14:50."),
            ex("¿Cuánto tiempo pasa desde las 22:30 hasta las 06:15 del día siguiente?", "7 horas 45 minutos", "Hasta la medianoche son 1 hora 30 minutos y luego 6 horas 15 minutos."),
        ],
    },
    context=[arith("Un bus sale a las 16:20 y llega a las 17:05. ¿Cuántos minutos dura el viaje? Hay 40 minutos hasta las 17:00 y 5 minutos más.", "40+5", "Se suman los minutos hasta la hora en punto y los restantes.")],
    selfcheck=[
        ex("Un recreo va de 10:15 a 10:40. ¿Cuántos minutos dura?", "25", "De 10:15 a 10:40 hay 25 minutos."),
        ex("Una clase empieza a las 09:00 y dura 1 hora 30 minutos. ¿A qué hora termina?", "10:30", "09:00 más 1 hora 30 minutos."),
        ex("¿A qué hora en formato de 12 horas corresponde 20:00?", "8:00 p.m.", "20 − 12 = 8."),
    ],
    open_task=task(
        "Elige uno de estos horarios y responde. A) Un bus sale a las 06:50 y llega a las 08:10: ¿cuánto dura el viaje? B) Un curso comienza a las 14:15 y dura 1 hora 50 minutos: ¿a qué hora termina? Escribe cómo contaste y la hora en formato de 12 horas.",
        "B) De 14:15 sumo 1 hora: 15:15; sumo 50 minutos: 16:05. Termina a las 16:05, o sea 4:05 p.m.",
        ["usa la hora en punto para contar", "calcula la duración o la hora de término", "escribe la hora en formato de 12 horas"],
        ["cálculo", "respuesta en 12 horas"],
        ["restar horas y minutos por separado", "olvidar pasar de 60 minutos a 1 hora"],
        "Pide que muestre dónde contó hasta la hora en punto. Reconoce el paso por las horas en punto.",
    ),
    reinforce="Con el horario de tu día en el colegio, calcula cuánto dura cada actividad y escribe la hora en 24 horas.",
    extend="Crea un horario de tu día de sábado con cinco actividades y calcula cuánto dura cada una.",
)
