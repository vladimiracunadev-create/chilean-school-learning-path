"""Student material for 2.º básico Matemática, OA 04 (estimación) y OA 05 (composición y descomposición)."""
from __future__ import annotations

from student_content_ma02_a import bars
from student_lessons import arith, ex, register

OA4 = "MA02 OA 04"
OA5 = "MA02 OA 05"
ROW = "●●●●●●●●●●"
KEY = "Clave de dibujo: ▮ es una barra de 10 y ● es un cubo de 1."


def near(estimate: int, real: int) -> str:
    gap = abs(estimate - real)
    return f"{gap} de diferencia; " + ("es una estimación razonable" if gap <= 10 else "se aleja demasiado")


register(
    OA4, 1,
    materials=f"Una fila de referencia de 10 puntos ({ROW}), lápiz de color y las colecciones descritas en cada ejercicio.",
    use="Aprenderé a estimar cuántos objetos hay usando un grupo de 10 como medida. Sirve para decidir rápido cuántas cosas hay cuando no es posible contarlas una por una.",
    prior=["Sé contar de 10 en 10 hasta 100.", "Sé qué es una decena."],
    explain=[
        "Estimar es decir un número cercano a la cantidad real, sin contar todo. Para hacerlo bien necesitas un referente: algo que conoces. Aquí usamos un grupo de 10 puntos, que se ve así: ●●●●●●●●●●.",
        "Imagina que miras una colección grande y ves que ocupa más o menos el espacio de cuatro de esos grupos. Si cada grupo vale 10, tu estimación es 4 × 10 = 40, o sea, cerca de 40. Lo importante no es acertar exacto, sino acercarte.",
        "Una buena estimación se explica: «cerca de 40 porque caben unos cuatro grupos de 10». Después, si puedes, cuentas de verdad para comprobar. Si la diferencia entre tu estimación y el número real es pequeña, tu estimación fue buena.",
    ],
    vocab=[("estimar", "decir una cantidad cercana sin contar todo"), ("referente", "una cantidad conocida que sirve para comparar, como 10 puntos"), ("cerca de", "casi igual a un número"), ("cantidad real", "lo que da al contar de verdad"), ("comprobar", "contar para ver si la estimación fue buena")],
    worked=[
        {"title": "Estimar con grupos de 10", "problem": f"La fila de referencia es {ROW} (10 puntos). Una colección ocupa el espacio de 3 filas como esa. ¿Cuántos puntos estimas?", "steps": ["Una fila vale 10.", "La colección cabe en 3 filas.", "3 × 10 = 30; también cuento de 10 en 10: 10, 20, 30.", "Estimo que hay cerca de 30."], "answer": "Cerca de 30 puntos"},
        {"title": "Comprobar la estimación", "problem": "Estimé 30 y al contar de verdad había 34. ¿Qué tan buena fue mi estimación?", "steps": ["Calculo la diferencia: 34 − 30 = 4.", "Una diferencia de 4 es pequeña, menos que una decena.", "Concluyo que mi estimación fue buena."], "answer": "Muy buena: 4 de diferencia"},
    ],
    mistakes=[
        {"wrong": "Decir que hay 3 si ocupa 3 filas.", "why": "Se confunde el número de filas con el de puntos.", "fix": "Cada fila vale 10, así que 3 filas valen 30."},
        {"wrong": "Estimar 100 sin mirar el referente.", "why": "Se inventa un número sin comparar.", "fix": "Cuenta cuántas veces cabe el referente: 3 veces, estima 30."},
    ],
    tiers={
        "recovery": [
            arith(f"La fila de referencia tiene 10 puntos ({ROW}). Una colección ocupa 2 filas iguales. ¿Cuántos puntos hay?", "2*10", "Dos filas de 10 son 20."),
            arith("La colección ocupa 5 filas iguales a la de referencia (10 puntos cada una). ¿Cuántos puntos estimas?", "5*10", "Cinco filas de 10 son 50."),
            arith("La colección ocupa 1 fila de referencia y 4 puntos más. ¿Cuántos puntos hay?", "10+4", "10 + 4 = 14."),
        ],
        "understand": [
            ex("¿Para qué sirve el grupo de 10 puntos cuando estimo?", "Es el referente con el que comparo", "Permite ver cuántas veces cabe en la colección."),
            ex("Una estimación dice «cerca de 40». ¿Significa que hay exactamente 40?", "No", "Estimar es acercarse sin contar uno por uno."),
            ex("Una colección ocupa 4 filas de 10 puntos. ¿Cuántos puntos hay, más o menos?", "Cerca de 40", "Cada fila vale 10; 4 filas valen 40 puntos."),
        ],
        "apply": [
            ex("Una colección ocupa más o menos 3 filas de 10 y 2 puntos. ¿Cuál es tu estimación?", "Cerca de 32", "30 + 2 = 32."),
            arith("Se ven 6 filas de 10 granos de arroz. ¿Cuántos granos estimas?", "6*10", "Seis filas de 10 son 60."),
            ex("La colección ocupa casi 5 filas de 10. ¿Cuál número es mejor estimación: 5, 50 o 500?", "50", "5 filas de 10 son 50; 5 y 500 están muy lejos."),
        ],
        "reason": [
            ex("Alicia dice que una colección de 4 filas de 10 tiene 4 puntos. ¿Qué error comete y qué debería decir?", "Cuenta filas, no puntos; debería decir cerca de 40", "Cada fila vale 10 puntos: 4 × 10 = 40."),
            ex("Dos amigos estiman una colección que tiene 47 puntos. Uno dice 50 y otro 80. ¿Quién estimó mejor y por qué?", "El que dijo 50", "50 está a 3 de 47; 80 está a 33 de 47."),
        ],
        "challenge": [
            ex("La colección es el doble de grande que otra que tiene 4 filas de 10. ¿Cuántos puntos estimas en la grande?", "Cerca de 80", "4 filas son 40; el doble de 40 es 80."),
            ex("Estimé 60 puntos. Había 52. Otra persona estimó 40. ¿Quién se acercó más?", "La estimación de 60", "60 − 52 = 8, y 52 − 40 = 12; 8 es menor que 12."),
        ],
    },
    context=[arith("Se plantaron lechugas en 4 filas parejas de 10. En la última fila faltan 3. Estima cuántas lechugas se plantaron y calcula cuántas son realmente.", "4*10-3", "Cuatro filas de 10 son 40; si en una faltan 3, hay 40 − 3 = 37. Una estimación razonable era cerca de 40.")],
    selfcheck=[ex("Una colección ocupa 7 filas de 10. ¿Cuántos estimas?", "Cerca de 70", "7 × 10 = 70."), ex("Estimé 20 y hay 23. ¿Qué diferencia hay?", "3", "23 − 20 = 3."), ex("¿Qué es un referente?", "Una cantidad conocida para comparar", "Se usa para ver cuántas veces cabe en la colección.")],
    open_task={
        "statement": f"Mira esta colección y estímala: {ROW} {ROW} {ROW} ●●●●●●. Escribe tu estimación, explica qué referente usaste y luego cuenta para comprobar.",
        "example": "Veo 3 filas de 10 y unos 6 puntos más. Estimo cerca de 36. Usé la fila de 10 como referente. Al contar de verdad hay 36 puntos: coincidió.",
        "criteria": ["usa el grupo de 10 como referente", "da un número cercano", "comprueba contando", "explica la diferencia o coincidencia"],
        "evidence": ["estimación escrita", "explicación del referente", "conteo final"],
        "errors": ["estimar sin referente", "confundir el número de filas con el de puntos"],
        "feedback": "Reconoce el uso del referente y pide que cuente de 10 en 10; si hubo diferencia grande, que identifique si se equivocó al mirar o al contar.",
    },
    reinforce="Con 30 fichas haz tres filas de 10. Luego júntalas en un montón y estima cuántas hay sin contar; después cuenta para comprobar.",
    extend="Una colección ocupa 4 filas de 10. Si usaras filas de 5 como referente, ¿cuántas filas necesitarías? Explica por qué cambia el número de filas pero no la cantidad.",
)

register(
    OA4, 2,
    materials="Un vaso lleno con 50 semillas dibujado (referente de 50), un vaso a la mitad (referente de 25) y las colecciones de este cuaderno.",
    use="Aprenderé a usar 25 y 50 como referentes para estimar cantidades hasta 100. Sirve para saber rápido si una colección tiene más o menos que una cantidad conocida.",
    prior=["Sé estimar con grupos de 10.", "Sé que 50 es la mitad de 100 y que 25 es la mitad de 50."],
    explain=[
        "A veces conviene usar referentes más grandes que 10. El 50 es un buen referente: es la mitad de 100. El 25 es la mitad de 50. Si sabes cómo se ve un vaso con 50 semillas, puedes comparar otro vaso con él.",
        "Por ejemplo, si un vaso está lleno hasta la mitad del vaso de 50, tiene cerca de 25. Si está lleno hasta un poco más de la mitad, tiene un poco más de 25. Si llega casi hasta arriba, tiene cerca de 50.",
        "Para estimar, primero decide si hay más o menos que el referente. Luego ajusta: «más que 25, pero menos que 50, entonces cerca de 40». Compara siempre con el referente y no con tu intuición solamente.",
    ],
    vocab=[("referente de 50", "una colección que sabemos que tiene 50"), ("mitad", "una de dos partes iguales"), ("más que", "mayor que"), ("menos que", "menor que"), ("ajustar", "corregir mi estimación al comparar de nuevo")],
    worked=[
        {"title": "Comparar con 50", "problem": "Un vaso A tiene 50 semillas y está lleno. El vaso B es igual y está lleno a la mitad. ¿Cuántas semillas estimas en B?", "steps": ["La mitad de 50 es 25: 50 ÷ 2.", "B está a la mitad, así que tiene cerca de 25.", "Respondo: cerca de 25 semillas."], "answer": "Cerca de 25 semillas"},
        {"title": "Entre dos referentes", "problem": "Un vaso está lleno más que la mitad pero menos que lleno. ¿Entre qué números está la cantidad?", "steps": ["La mitad es 25 y lleno es 50.", "Más que la mitad: más de 25.", "Menos que lleno: menos de 50.", "Entonces está entre 25 y 50; podría estimar 40."], "answer": "Entre 25 y 50, por ejemplo cerca de 40"},
    ],
    mistakes=[
        {"wrong": "Decir que un vaso a la mitad tiene 50 semillas.", "why": "Se confunde la mitad con el vaso lleno.", "fix": "La mitad de 50 es 25; compara siempre con el referente de 50."},
        {"wrong": "Comparar dos vasos de distinto tamaño.", "why": "Se pierde el referente.", "fix": "El referente solo sirve con un vaso igual al de referencia."},
    ],
    tiers={
        "recovery": [
            ex("El vaso lleno tiene 50. ¿Cuántas semillas hay en la mitad del vaso?", "25", "50 ÷ 2 = 25."),
            ex("Si un vaso está vacío, ¿cuántas semillas tiene?", "0", "Vacío significa ninguna semilla."),
            ex("Si dos vasos llenos de 50 se juntan, ¿cuántas semillas hay?", "100", "50 + 50 = 100."),
        ],
        "understand": [
            ex("¿Es 25 la mitad de 50?", "Sí", "25 + 25 = 50."),
            ex("Un vaso está lleno hasta la mitad. ¿Tiene más o menos que 50?", "Menos que 50", "La mitad es 25 y 25 es menor que 50."),
            ex("¿Qué número está justo en el medio entre 0 y 50?", "25", "25 está a la misma distancia de 0 y de 50."),
        ],
        "apply": [
            ex("Un vaso tiene un poco menos que la mitad. ¿Cuál estimación es mejor: 5, 20 o 45?", "20", "Menos que 25, pero no muy lejos de 25."),
            ex("Otro vaso está casi lleno. ¿Cuál estimación es mejor: 10, 25 o 45?", "45", "Casi lleno se parece a 50."),
            arith("Tengo 2 vasos como el de referencia: uno lleno (50 semillas) y otro a la mitad (25). ¿Cuántas semillas hay en total?", "50+25", "Un vaso lleno y uno a la mitad hacen 75."),
        ],
        "reason": [
            ex("Un vaso a la mitad y otro con casi 50 se juntan. Lucía dice «hay 25». ¿Tiene razón?", "No; hay cerca de 75", "25 + casi 50 se acerca a 75, no a 25."),
            ex("¿Por qué el 25 sirve como referente en un vaso de 50 semillas?", "Porque es la mitad de 50 y es fácil de comparar", "Con 25 y 50 es sencillo ver mitades y compararlas con la colección."),
        ],
        "challenge": [
            ex("Un frasco tiene la mitad de 50 y otro la mitad de 100. ¿Cuántas más tiene el segundo?", "25 más", "La mitad de 100 es 50, y 50 − 25 = 25."),
            ex("Una colección tiene 50 semillas y 25 más. Estimé 60. ¿Qué diferencia hay con la cantidad real?", "15", "50 + 25 = 75; 75 − 60 = 15."),
        ],
    },
    context=[ex("En una caja caben 50 lápices cuando está llena. Ahora está llena hasta la mitad. ¿Cuántos lápices estimas? Si ponen 10 lápices más, ¿cuántos hay?", "25; 35", "La mitad de 50 es 25 y 25 + 10 = 35.")],
    selfcheck=[ex("La mitad de 100 es __.", "50", "100 ÷ 2 = 50."), ex("Un vaso a la mitad de 50 tiene cerca de __.", "25", "50 ÷ 2 = 25."), ex("¿Cuál es mayor: 25 o 50?", "50", "50 es mayor que 25.")],
    open_task={
        "statement": "Dibuja dos vasos del mismo tamaño: uno lleno hasta arriba (50 semillas) y otro lleno un poco más arriba de la mitad. Estima cuántas semillas tiene el segundo y explica con qué referente lo hiciste.",
        "example": "El vaso lleno tiene 50. El otro llega un poco más arriba de la mitad. Estimo cerca de 35, entre 25 y 50, porque 25 es la mitad y 50 es lleno.",
        "criteria": ["dibuja vasos iguales", "usa 25 y 50 como referentes", "estima un número entre 25 y 50", "explica con palabras"],
        "evidence": ["dibujo", "estimación escrita", "explicación"],
        "errors": ["estimar un número fuera del rango 25–50", "no usar el vaso de referencia"],
        "feedback": "Pide que marque en el dibujo dónde está la mitad; si la estimación queda fuera de 25–50, que compare el nivel con la marca.",
    },
    reinforce="Llena un vaso con arroz hasta la mitad y otro hasta arriba; compara con tu estimación.",
    extend="Estima la cantidad con referentes de 25 y 50 en un frasco que tiene 75 semillas. Explica cómo usarías ambos referentes.",
)

register(
    OA4, 3,
    materials=f"Dos colecciones de 30 puntos: A) juntos en 3 filas ({ROW} {ROW} {ROW}) y B) esparcidos en una hoja que dibujas tú; lápiz de color.",
    use="Aprenderé que la misma cantidad se ve distinta si está junta o separada. Sirve para no engañarme cuando estimo.",
    prior=["Sé estimar con grupos de 10 y con referentes de 25 y 50.", "Sé comparar dos cantidades."],
    explain=[
        "Una colección ordenada en filas parece más pequeña que la misma colección repartida por toda la hoja. Si los objetos están muy juntos, ocupan poco espacio. Si están separados, ocupan mucho. Pero la cantidad es la misma.",
        "Por eso, al estimar hay que mirar cuántos hay y no cuánto espacio ocupan. Una buena idea es imaginar que los acomodas en filas de 10. Si tienes 3 filas completas, hay 30, aunque estén esparcidos.",
        "Para evitar el engaño, usa el referente de 10 y cuenta mentalmente cuántas filas formarías. Si no puedes, agrupa con lápiz: rodea 10 objetos, otros 10 y así hasta el final.",
    ],
    vocab=[("disposición", "la forma en que están puestos los objetos"), ("juntos", "muy cerca unos de otros"), ("esparcidos", "repartidos por todo el espacio"), ("misma cantidad", "igual número de objetos"), ("rodear", "dibujar una línea alrededor de un grupo")],
    worked=[
        {"title": "Mismo número, distinta disposición", "problem": "En la hoja A hay 30 puntos en 3 filas de 10. En la hoja B hay 30 puntos repartidos. ¿Cuál tiene más?", "steps": ["En A hay 3 filas de 10: 10 + 10 + 10 = 30.", "En B también hay 30, aunque se vea más grande.", "Ocupar más espacio no significa tener más objetos."], "answer": "Tienen la misma cantidad"},
        {"title": "Rodear grupos de 10", "problem": "En una hoja hay puntos esparcidos. Rodeas 10, otros 10, otros 10 y quedan 5 sin rodear. ¿Cuántos hay?", "steps": ["Tres grupos rodeados valen 10, 20, 30.", "Quedan 5 sueltos.", "30 + 5 = 35."], "answer": "35 puntos"},
    ],
    mistakes=[
        {"wrong": "Decir que la hoja con puntos esparcidos tiene más.", "why": "Se confunde el espacio con la cantidad.", "fix": "Agrupa en 10 y cuenta los grupos; la cantidad no cambia por la disposición."},
        {"wrong": "Estimar sin agrupar.", "why": "Se estima por el tamaño de la mancha de puntos.", "fix": "Rodea grupos de 10 antes de dar la estimación."},
    ],
    tiers={
        "recovery": [
            ex("Hay 20 fichas juntas y 20 fichas separadas. ¿Cuál tiene más?", "Ninguna; tienen la misma cantidad", "Ambas colecciones tienen 20 fichas."),
            ex("Rodeé 2 grupos de 10 y quedaron 3 sueltas. ¿Cuántas hay?", "23", "20 + 3 = 23."),
            ex("Rodeé 4 grupos de 10 y no quedan sueltas. ¿Cuántas hay?", "40", "Cuatro grupos de 10 son 40."),
        ],
        "understand": [
            ex("¿Cambia la cantidad si muevo los objetos de lugar sin quitar ni agregar?", "No", "La cantidad solo cambia si agrego o quito."),
            ex("¿Por qué conviene rodear grupos de 10?", "Porque ayuda a contar y a estimar sin perderse", "Cada grupo vale 10 y se cuenta de 10 en 10."),
            ex("Una hoja tiene los objetos muy juntos y otra muy separados, con la misma cantidad. ¿En cuál se ve más espacio?", "En la de objetos separados", "Ocupan más espacio, pero no son más."),
        ],
        "apply": [
            arith("En una hoja rodeaste 5 grupos de 10 y hay 6 sueltas. ¿Cuántas hay en total?", "5*10+6", "Cinco grupos son 50 y 6 sueltas hacen 56."),
            ex("En una hoja hay 3 grupos de 10 rodeados y 9 sueltas. Otra tiene 4 grupos de 10 y 2 sueltas. ¿Cuál tiene más?", "La segunda", "39 es menor que 42."),
            arith("En el patio hay 2 grupos de 10 niños y 8 niños más. ¿Cuántos niños hay?", "2*10+8", "Dos grupos son 20 y 8 más hacen 28."),
        ],
        "reason": [
            ex("Tomás dice que 25 fichas esparcidas son más que 25 fichas juntas. ¿Tiene razón?", "No", "Son 25 en ambos casos; solo cambia el espacio que ocupan."),
            ex("Luz estimó mal porque estaban esparcidas. ¿Qué debe hacer para estimar mejor?", "Rodear grupos de 10", "Los grupos de 10 le permiten contar sin importar el espacio."),
        ],
        "challenge": [
            ex("Hay 36 fichas esparcidas. Las acomodas en filas de 10. ¿Cuántas filas completas hay y cuántas sobran?", "3 filas y 6 fichas", "36 = 30 + 6."),
            ex("Hay 40 puntos juntos y 45 puntos esparcidos. ¿En cuál hay más puntos?", "En los esparcidos", "45 es mayor que 40."),
        ],
    },
    context=[arith("En un patio 3 grupos de 10 niños juegan juntos y otros 7 niños están repartidos por el patio. ¿Cuántos niños hay en total?", "3*10+7", "Tres grupos son 30 y 7 más hacen 37.")],
    selfcheck=[ex("Si no agrego ni quito, ¿cambia la cantidad al mover los objetos?", "No", "La cantidad se conserva."), ex("Rodeaste 3 grupos de 10. ¿Cuántos hay?", "30", "3 × 10 = 30."), ex("Dos grupos de 10 y 4 sueltas, ¿cuántos hay?", "24", "20 + 4 = 24.")],
    open_task={
        "statement": "Dibuja 24 puntos esparcidos en una hoja. Rodea grupos de 10, cuenta cuántos hay y explica cómo evitaste engañarte por el espacio.",
        "example": "Dibujé 24 puntos. Rodeé 2 grupos de 10 y quedaron 4 sueltos: 20 + 4 = 24. No me engañó el espacio porque conté por grupos.",
        "criteria": ["dibuja la cantidad pedida", "rodea grupos de 10", "calcula el total", "explica cómo evitó el engaño"],
        "evidence": ["dibujo con grupos", "registro 20 + 4", "frase de explicación"],
        "errors": ["rodear grupos de distinto tamaño", "no contar los sueltos"],
        "feedback": "Pide que cuente cada grupo para confirmar que tiene 10; reconoce la estrategia de agrupar.",
    },
    reinforce="Pon 20 fichas en una fila y luego repártelas por la mesa; cuenta de nuevo y comprueba que sigue habiendo 20.",
    extend="Diseña un dibujo donde 30 puntos parezcan más y otro donde parezcan menos. Explica cómo lo lograste.",
)

register(
    OA4, 4,
    materials="Tres colecciones descritas en los ejercicios: A) 47 puntos, B) 62 puntos, C) 38 puntos; lápiz.",
    use="Aprenderé a decidir si una estimación es razonable comparándola con el conteo real. Sirve para saber cuándo una estimación sirve y cuándo hay que revisar.",
    prior=["Sé estimar con referentes de 10, 25 y 50.", "Sé restar para encontrar una diferencia."],
    explain=[
        "Una estimación se evalúa mirando la diferencia con el número real. Si estimaste 50 y hay 47, la diferencia es 3: muy buena. Si estimaste 80 y hay 47, la diferencia es 33: se aleja mucho.",
        "En esta clase usaremos una regla: una estimación es razonable si se aleja menos de 10 del número real. Si la diferencia es 10 o más, hay que mirar de nuevo el referente. No importa si estimaste de más o de menos; lo que mide es la distancia.",
        "Cuando una estimación no es razonable, hay que averiguar qué falló: ¿me equivoqué al contar filas? ¿Usé mal el referente? ¿Me dejé engañar por el espacio? Con esa pregunta se mejora la próxima estimación.",
    ],
    vocab=[("diferencia", "lo que separa a dos números; se calcula restando el menor del mayor"), ("razonable", "que se acerca lo suficiente"), ("de más", "estimar un número mayor que el real"), ("de menos", "estimar un número menor que el real"), ("revisar", "mirar de nuevo para encontrar el error")],
    worked=[
        {"title": "Calcular la diferencia", "problem": "Estimé 50 y al contar había 47. ¿Fue razonable?", "steps": ["Resto el menor al mayor: 50 − 47 = 3.", "3 es menor que 10.", "La estimación es razonable."], "answer": "Sí, razonable: 3 de diferencia"},
        {"title": "Corregir una estimación lejana", "problem": "Estimé 80 y había 47. ¿Qué hago?", "steps": ["80 − 47 = 33.", "33 es mayor que 10, no es razonable.", "Reviso: usé 8 filas de 10, pero solo hay unas 4 filas y 7 puntos.", "Corrijo: 4 filas de 10 y 7 puntos es cerca de 47."], "answer": "Se aleja demasiado; la nueva estimación es cerca de 47"},
    ],
    mistakes=[
        {"wrong": "Calcular 47 − 50 para hallar la diferencia.", "why": "Se resta en el orden equivocado y no se puede.", "fix": "Siempre resta el número menor al mayor: 50 − 47 = 3."},
        {"wrong": "Decir que estimar más es mejor que estimar menos.", "why": "Se piensa que sobrepasar es seguro.", "fix": "Una estimación es buena cuando está cerca, sea mayor o menor."},
    ],
    tiers={
        "recovery": [
            arith("Estimé 40 y había 43. ¿Cuál es la diferencia?", "43-40", "43 − 40 = 3."),
            arith("Estimé 60 y había 52. ¿Cuál es la diferencia?", "60-52", "60 − 52 = 8."),
            arith("Estimé 20 y había 38. ¿Cuál es la diferencia?", "38-20", "38 − 20 = 18."),
        ],
        "understand": [
            ex("¿Una diferencia de 3 es pequeña o grande según la regla de esta clase?", "Pequeña", "Menos de 10 es razonable."),
            ex("¿Una diferencia de 18 es razonable?", "No", "18 es mayor que 10."),
            ex("¿Importa si estimé de más o de menos?", "No importa; importa la diferencia", "La diferencia mide qué tan lejos estuve."),
        ],
        "apply": [
            ex("La colección A tiene 47 puntos. Estimé 50. Calcula la diferencia: ¿es razonable?", near(50, 47), "50 − 47 = 3 y 3 es menos de 10."),
            ex("La colección B tiene 62 puntos. Estimé 40. Calcula la diferencia: ¿es razonable?", near(40, 62), "62 − 40 = 22 y 22 es más de 10."),
            ex("La colección C tiene 38 puntos. Estimé 30. Calcula la diferencia: ¿es razonable?", near(30, 38), "38 − 30 = 8 y 8 es menos de 10."),
        ],
        "reason": [
            ex("Dos amigos estiman una colección que tiene 47 puntos. Uno dice 40 y el otro 55. ¿Quién se acercó más?", "El que dijo 40", "47 − 40 = 7 y 55 − 47 = 8; 7 es menor que 8."),
            ex("Una amiga estimó 70 para una colección de 62. Otra estimó 50. ¿Cuál es más razonable?", "La de 70", "70 − 62 = 8 y 62 − 50 = 12."),
        ],
        "challenge": [
            ex("Estimé 45 y la diferencia con el número real fue 6. ¿Qué dos números reales son posibles?", "39 o 51", "45 − 6 = 39 y 45 + 6 = 51."),
            ex("Una estimación fue razonable (diferencia menor que 10) y estimé 60. ¿Cuál es el número real más grande posible?", "69", "La diferencia puede ser 9 como máximo: 60 + 9 = 69."),
        ],
    },
    context=[arith("En un cumpleaños se estimó que había 30 globos y luego se contaron 41. ¿Qué diferencia hubo? ¿Fue razonable la estimación?", "41-30", "41 − 30 = 11; 11 es mayor que 10, así que no fue razonable.")],
    selfcheck=[ex("Estimé 50 y había 48. ¿Diferencia?", "2", "50 − 48 = 2."), ex("¿Es razonable una diferencia de 9?", "Sí", "Es una diferencia menor que 10."), ex("¿Se calcula la diferencia sumando o restando?", "Restando", "Se resta el menor al mayor.")],
    open_task={
        "statement": "Observa la colección C con 38 puntos. Un amigo dice «hay cerca de 60». Calcula la diferencia, decide si es razonable y escribe cómo lo ayudarías a mejorar su estimación.",
        "example": "60 − 38 = 22. 22 es mayor que 10, no es razonable. Le diría que forme filas de 10: hay 3 filas y 8 puntos, entonces estima cerca de 38.",
        "criteria": ["calcula bien la diferencia", "decide con el criterio de 10", "da una sugerencia concreta", "usa filas de 10"],
        "evidence": ["resta escrita", "decisión", "consejo escrito"],
        "errors": ["restar al revés", "no justificar la decisión"],
        "feedback": "Reconoce la corrección del cálculo y la amabilidad del consejo; si no usó el criterio, vuelve a mostrar la comparación con 10.",
    },
    reinforce="Estima, cuenta y calcula la diferencia con 3 colecciones pequeñas de objetos de tu casa.",
    extend="Descubre cuántas estimaciones razonables hay para un número real de 47. Escribe las que se te ocurran y comprueba cada una.",
)

register(
    OA5, 1,
    materials=f"Material base diez (o su dibujo): barras y cubos. {KEY} Los números de trabajo están escritos en cada ejercicio.",
    use="Aprenderé a descomponer un número en decenas y unidades y a volver a componerlo. Sirve para entender de qué está hecho un número y para sumar y restar más fácil.",
    prior=["Sé leer y representar números hasta 100.", "Sé que una decena es un grupo de 10."],
    explain=[
        "Descomponer un número es separarlo en partes que, al juntarse, lo forman otra vez. El número 63 se puede separar en 6 decenas y 3 unidades, o sea, 60 + 3. Al juntar las partes, 60 + 3 vuelve a ser 63.",
        "Componer es lo contrario: juntar las partes para armar el número. Si tienes 4 barras y 7 cubos, compones 40 + 7 = 47. El total siempre se conserva: no se pierde ni se agrega nada al separar o juntar.",
        "Hay una descomposición «estándar» en decenas y unidades, pero no es la única. 63 también es 50 + 13, porque 13 es una decena y 3 unidades. Por ahora, practica la estándar, y mira que siempre reconstruyas el mismo número.",
    ],
    vocab=[("descomponer", "separar un número en partes"), ("componer", "juntar partes para formar un número"), ("sumando", "cada número que se suma"), ("parte", "una de las cantidades que forman el total"), ("total", "lo que resulta al juntar todas las partes")],
    worked=[
        {"title": "Descomponer 47", "problem": "Descompón el 47 en decenas y unidades.", "steps": ["47 tiene 4 decenas y 7 unidades.", f"Con material: {bars(47)}.", "Escribo 40 + 7.", "Compruebo: 40 + 7 = 47."], "answer": "40 + 7"},
        {"title": "Componer desde las partes", "problem": "Tengo 5 barras de 10 y 8 cubos. ¿Qué número formo?", "steps": ["Cinco barras son 5 × 10 = 50.", "Los 8 cubos son 8.", "50 + 8 = 58."], "answer": "58"},
    ],
    mistakes=[
        {"wrong": "Escribir 63 = 6 + 3.", "why": "Se olvidan las decenas: el 6 vale 60.", "fix": "El 6 está en el lugar de las decenas, entonces vale 60: 63 = 60 + 3."},
        {"wrong": "Decir que 60 + 3 = 603.", "why": "Se pegan las cifras en vez de sumar.", "fix": "60 + 3 es una suma: 60 y 3 más son 63."},
    ],
    tiers={
        "recovery": [
            ex("Descompón 25 en decenas y unidades.", "20 + 5", "25 tiene 2 decenas y 5 unidades."),
            ex("Descompón 34 en decenas y unidades.", "30 + 4", "34 tiene 3 decenas y 4 unidades."),
            ex("Descompón 70 en decenas y unidades.", "70 + 0", "70 son 7 decenas y 0 unidades."),
        ],
        "understand": [
            arith("¿Qué número es 40 + 6?", "40+6", "4 decenas y 6 unidades forman 46."),
            ex("Dibujo: ▮ ▮ ▮ ▮ | ● ● ● ● ● ● ● ●. ¿Qué número y qué descomposición muestra?", "48; 40 + 8", "Cuatro barras son 40 y ocho cubos son 8."),
            ex("¿Cuántas decenas tiene 56?", "5", "El 5 de 56 está en el lugar de las decenas."),
        ],
        "apply": [
            ex("Descompón 63 en decenas y unidades y dibújalo con barras y cubos.", f"60 + 3; {bars(63)}", "Seis barras son 60 y tres cubos son 3."),
            ex("Compón: 70 + 4.", "74", "7 decenas y 4 unidades."),
            arith("Una caja tiene 3 bolsas con 10 caramelos y 8 caramelos sueltos. ¿Cuántos caramelos hay?", "3*10+8", "30 + 8 = 38."),
        ],
        "reason": [
            ex("Pablo dice que 63 = 6 + 3. ¿Qué error comete y cuál es la descomposición correcta?", "Olvidó que 6 son decenas; es 60 + 3", "El 6 está en el lugar de las decenas y vale 60."),
            ex("Ema dice que 50 + 9 y 9 + 50 son números distintos. ¿Tiene razón?", "No", "Ambas dan 59; cambiar el orden de la suma no cambia el total."),
        ],
        "challenge": [
            ex("Descompón 63 de otra forma, distinta a 60 + 3, y comprueba que sigue siendo 63.", "Por ejemplo 50 + 13 (o 40 + 23)", "50 + 13 = 63 porque 13 tiene una decena y 3 unidades."),
            ex("Un número tiene 5 decenas y la suma de sus cifras es 9. ¿Cuál es?", "54", "La cifra de las unidades es 9 − 5 = 4; el número es 54."),
        ],
    },
    context=[arith("Un panadero hace bolsas de 10 panes. Hoy llenó 4 bolsas y le sobraron 6 panes. ¿Cuántos panes hizo? Escribe la descomposición.", "4*10+6", "Cuatro bolsas son 40 panes y 6 más hacen 46: 40 + 6.")],
    selfcheck=[ex("Descompón 82.", "80 + 2", "82 tiene 8 decenas y 2 unidades."), ex("Compón: 90 + 1.", "91", "9 decenas y 1 unidad."), ex("¿Qué valor tiene la cifra 3 en 36?", "30", "El 3 está en el lugar de las decenas.")],
    open_task={
        "statement": "Representa 63 en tres formas: con barras y cubos, con una suma de decenas y unidades, y con una frase. Comprueba con una resta que no se perdió nada.",
        "example": f"{bars(63)}; 60 + 3 = 63; «seis decenas y tres unidades forman sesenta y tres». Comprobación: 63 − 60 = 3.",
        "criteria": ["las tres formas representan 63", "la suma conserva el total", "la comprobación es coherente"],
        "evidence": ["dibujo", "suma escrita", "frase", "comprobación"],
        "errors": ["escribir 6 + 3", "dibujar 63 barras"],
        "feedback": "Reconoce las representaciones correctas y pide que lea su suma en voz alta; ante el error 6 + 3, que cuente las decenas.",
    },
    reinforce="Arma con material base diez los números 32, 45 y 71 y escribe su descomposición.",
    extend="Encuentra todas las maneras de descomponer 63 usando una o más decenas completas y unidades (por ejemplo, 60 + 3 y 50 + 13).",
)

register(
    OA5, 2,
    materials="Fichas de dos colores (o su dibujo), recta numérica y los totales del ejercicio: 35, 52, 24 y 41. Los números de trabajo están escritos en cada ejercicio.",
    use="Aprenderé que un mismo número se forma con muchas parejas de sumandos distintas. Sirve para calcular mentalmente y para comprobar que un resultado conserva el total.",
    prior=["Sé descomponer números en decenas y unidades.", "Sé que sumar es juntar partes."],
    explain=[
        "El número 35 se puede formar con 30 + 5, pero también con 20 + 15 o con 18 + 17. Todas esas sumas dan 35. Es como repartir 35 fichas en dos montones de distintas maneras: siempre quedan 35 fichas en total.",
        "Si un sumando crece, el otro debe disminuir en la misma cantidad. Si pasas de 30 + 5 a 20 + 15, quitas 10 al primero y se los agregas al segundo. El total se conserva.",
        "Para encontrar una pareja, elige un primer sumando y calcula cuánto falta para llegar al total. Si el total es 52 y eliges 20, resta: 52 − 20 = 32. Entonces 20 + 32 = 52.",
    ],
    vocab=[("pareja de sumandos", "dos números que suman el total"), ("conservar", "mantener igual"), ("total", "resultado de juntar las partes"), ("compensar", "quitar a un sumando lo que se agrega al otro"), ("equivalente", "que vale lo mismo")],
    worked=[
        {"title": "Tres parejas para 35", "problem": "Encuentra tres parejas de sumandos que formen 35.", "steps": ["Primera: 30 + 5 = 35.", "Quito 10 a 30 y se los doy al 5: 20 + 15 = 35.", "Pruebo con otro: 18 + 17 = 35.", "Compruebo cada suma."], "answer": "30 + 5, 20 + 15 y 18 + 17"},
        {"title": "Encontrar el sumando que falta", "problem": "Si un sumando es 20, ¿cuál es el otro para formar 52?", "steps": ["Calculo cuánto falta: 52 − 20 = 32.", "Escribo 20 + 32.", "Compruebo: 20 + 32 = 52."], "answer": "32"},
    ],
    mistakes=[
        {"wrong": "Pensar que 20 + 15 no es 35 porque no son decenas y unidades.", "why": "Se cree que la única descomposición válida es la estándar.", "fix": "Cualquier pareja de números que sumen 35 es válida."},
        {"wrong": "Cambiar un sumando sin cambiar el otro (30 + 5 = 20 + 5).", "why": "No se compensa.", "fix": "Si quitas 10 a un sumando, súmalos al otro: 20 + 15."},
    ],
    tiers={
        "recovery": [
            arith("¿Cuánto es 30 + 5?", "30+5", "30 + 5 = 35."),
            arith("¿Cuánto es 20 + 15?", "20+15", "20 + 15 = 35."),
            arith("¿Cuánto es 18 + 17?", "18+17", "18 + 17 = 35."),
        ],
        "understand": [
            ex("¿30 + 5 y 20 + 15 forman el mismo número?", "Sí, ambas forman 35", "30 + 5 = 35 y 20 + 15 = 35."),
            ex("Si 30 pasa a ser 20, ¿cuánto debe aumentar el otro sumando para conservar el total?", "10", "Lo que quito a uno se lo agrego al otro."),
            ex("¿Cuál pareja no forma 24: 20 + 4, 10 + 14 o 15 + 8?", "15 + 8", "15 + 8 = 23, no 24."),
        ],
        "apply": [
            ex("Escribe dos parejas de sumandos distintas para formar 52 que no sean 50 + 2.", "40 + 12 y 30 + 22", "40 + 12 = 52 y 30 + 22 = 52."),
            arith("Si un sumando es 25, ¿cuál es el otro para formar 52?", "52-25", "52 − 25 = 27."),
            arith("Un sumando es 17 y el total es 41. ¿Cuál es el otro sumando?", "41-17", "41 − 17 = 24, y 17 + 24 = 41."),
        ],
        "reason": [
            ex("Marta escribió 20 + 14 = 35. ¿Es correcto? Si no, corrígelo.", "No; 20 + 14 = 34. Corrección: 20 + 15", "Faltaba 1 para llegar a 35."),
            ex("Rodrigo dice que 25 + 10 y 10 + 25 no son el mismo total. ¿Tiene razón?", "No", "Las dos dan 35; el orden de los sumandos no cambia el resultado."),
        ],
        "challenge": [
            ex("¿Cuántas parejas de números mayores que 0 suman 6? Escríbelas sin repetir el orden (1 + 5 es lo mismo que 5 + 1).", "3 parejas: 1 + 5, 2 + 4 y 3 + 3", "Probando 1, 2 y 3 como primer sumando aparece la pareja complementaria."),
            ex("Encuentra una pareja para 41 con un sumando mayor que 30 y el otro menor que 10.", "Por ejemplo 35 + 6", "35 + 6 = 41."),
        ],
    },
    context=[arith("Entre dos niñas juntaron 24 figuritas. Una tiene 9. ¿Cuántas tiene la otra? Comprueba sumando.", "24-9", "24 − 9 = 15 y 9 + 15 = 24.")],
    selfcheck=[ex("Completa: 40 + __ = 52.", "12", "52 − 40 = 12."), ex("¿Cuál suma forma 30: 20 + 15, 10 + 20 o 25 + 5?", "25 + 5", "25 + 5 = 30."), ex("Escribe dos sumas distintas con total 20.", "10 + 10 y 15 + 5", "Las dos parejas suman exactamente 20.")],
    open_task={
        "statement": "Escribe cuatro sumas distintas cuyo total sea 41, sin usar 40 + 1. Comprueba cada una y explica cómo supiste cuál era el segundo sumando.",
        "example": "30 + 11, 25 + 16, 20 + 21, 18 + 23. Para cada una resté el primer sumando a 41: 41 − 30 = 11, 41 − 25 = 16, 41 − 20 = 21 y 41 − 18 = 23.",
        "criteria": ["las cuatro sumas dan 41", "no repite 40 + 1", "justifica con una resta"],
        "evidence": ["sumas escritas", "comprobación", "explicación"],
        "errors": ["sumas que no dan 41", "repetir la misma pareja"],
        "feedback": "Si una suma no da 41, que ajuste el segundo sumando con una resta; reconoce las estrategias de compensación.",
    },
    reinforce="Con 12 fichas, arma todas las parejas de montones posibles y anótalas.",
    extend="Con 10 fichas arma todas las parejas de montones que se puedan, sin repetir el orden. Haz lo mismo con 11 fichas. ¿Qué pareja aparece con 10 y no con 11? ¿Por qué?",
)

register(
    OA5, 3,
    materials=f"Dibujos con barras y cubos de este cuaderno. {KEY}",
    use="Aprenderé a pasar de un dibujo a una suma que lo describe y a revisar que el total sea el mismo. Sirve para leer representaciones y expresarlas con números.",
    prior=["Sé descomponer números.", "Sé leer dibujos con barras y cubos."],
    explain=[
        "Un dibujo con barras y cubos es una manera de mostrar cuánto vale un número. Para escribir la expresión que lo describe, cuenta primero las barras de 10 en 10 y luego los cubos de 1 en 1. El dibujo ▮ ▮ ▮ | ● ● ● ● ● es 30 + 5.",
        "Después de escribir la suma, calcula el total: 30 + 5 = 35. El total debe coincidir con el número que cuentas en el dibujo. Si no coincide, hay que revisar si faltó contar una barra o un cubo.",
        "También puedes hacer el camino inverso: a partir de una suma, dibujar las barras y los cubos que la describen. Con eso compruebas que entiendes qué significa cada número de la suma.",
    ],
    vocab=[("expresión", "una suma escrita con números y el signo +"), ("dibujo pictórico", "dibujo que representa cantidades"), ("barra", "vale 10"), ("cubo", "vale 1"), ("coincidir", "ser igual")],
    worked=[
        {"title": "Del dibujo a la suma", "problem": f"Escribe la suma del dibujo: {bars(52)}", "steps": ["Cuento las barras: 5 barras son 50.", "Cuento los cubos: 2 cubos son 2.", "Escribo 50 + 2.", "Calculo: 50 + 2 = 52."], "answer": "50 + 2 = 52"},
        {"title": "De la suma al dibujo", "problem": "Dibuja la suma 20 + 7.", "steps": ["20 son 2 barras.", "7 son 7 cubos.", f"Dibujo: {bars(27)}.", "Compruebo: 20 + 7 = 27."], "answer": bars(27)},
    ],
    mistakes=[
        {"wrong": "Escribir 5 + 2 para cinco barras y dos cubos.", "why": "Se olvida que las barras valen 10.", "fix": "5 barras son 50: la suma es 50 + 2."},
        {"wrong": "Contar un cubo de más al pasar de un grupo a otro.", "why": "No se separaron barras y cubos.", "fix": "Cuenta primero todas las barras y después todos los cubos."},
    ],
    tiers={
        "recovery": [
            ex(f"Escribe la suma del dibujo: {bars(31)}", "30 + 1", "Tres barras son 30 y un cubo es 1."),
            ex(f"Escribe la suma del dibujo: {bars(24)}", "20 + 4", "Dos barras son 20 y cuatro cubos son 4."),
            ex(f"Escribe la suma del dibujo: {bars(60)}", "60 + 0", "Seis barras son 60 y no hay cubos."),
        ],
        "understand": [
            ex("¿Qué número muestra 40 + 8 si lo dibujas?", f"48; {bars(48)}", "4 barras y 8 cubos."),
            ex("En el dibujo, ¿qué parte de la suma 50 + 3 representa 50?", "Las 5 barras", "Cada barra vale 10."),
            ex("¿Coincide el dibujo " + bars(36) + " con 30 + 6?", "Sí", "Tres barras y seis cubos son 30 + 6."),
        ],
        "apply": [
            ex("Dibuja 30 + 4 y escribe el número.", f"{bars(34)}; 34", "Tres barras y cuatro cubos."),
            ex(f"Escribe la suma y el total del dibujo: {bars(45)}", "40 + 5 = 45", "Cuatro barras y cinco cubos."),
            arith("Un dibujo tiene 4 barras y 9 cubos. ¿Qué número es?", "4*10+9", "40 + 9 = 49."),
        ],
        "reason": [
            ex(f"Gabi escribió 6 + 2 para el dibujo {bars(62)}. ¿Qué error cometió?", "Contó barras como unidades; debe escribir 60 + 2", "Cada barra vale 10."),
            ex(f"Dos dibujos: A = {bars(27)} y B = {bars(72)}. ¿Muestran el mismo número?", "No; A es 27 y B es 72", "Cambian las barras y los cubos."),
        ],
        "challenge": [
            ex("Dibuja 53 de una forma distinta: 4 barras y varios cubos.", "4 barras y 13 cubos", "40 + 13 = 53."),
            ex("Un dibujo tiene el doble de cubos que de barras y 3 barras. ¿Qué número es?", "36", "3 barras son 30 y 6 cubos son 6."),
        ],
    },
    context=[ex("En una tienda hay cajas de 10 lápices. Se ven 5 cajas y 3 lápices sueltos. Escribe la suma y cuántos lápices hay.", "50 + 3 = 53", "Cinco cajas son 50 y 3 sueltos suman 53.")],
    selfcheck=[ex("¿Qué suma describe 4 barras y 6 cubos?", "40 + 6", "Cada barra vale 10."), ex(f"¿Qué número muestra {bars(18)}?", "18", "Una barra son 10 y ocho cubos son 8."), ex("Dibuja 70 + 1.", bars(71), "Siete barras y un cubo.")],
    open_task={
        "statement": "Dibuja el número 56 con barras y cubos, escribe la suma que lo representa y explica cuál es la diferencia entre el 5 y el 6 del número.",
        "example": f"{bars(56)}. Suma: 50 + 6 = 56. El 5 está en el lugar de las decenas y vale 50; el 6 está en el lugar de las unidades y vale 6.",
        "criteria": ["el dibujo muestra 5 barras y 6 cubos", "la suma coincide", "explica el valor de cada cifra"],
        "evidence": ["dibujo", "suma", "explicación"],
        "errors": ["valorar el 5 como 5", "dibujar 56 cubos"],
        "feedback": "Pide que señale qué parte del dibujo corresponde a cada sumando; felicita las explicaciones que usan «decenas» y «unidades».",
    },
    reinforce="Dibuja los números 21, 38 y 44 con barras y cubos y escribe su suma.",
    extend="Dibuja 45 de dos maneras: con 4 barras y 5 cubos, y con 3 barras y 15 cubos. Explica por qué son iguales.",
)

register(
    OA5, 4,
    materials="Totales de trabajo: 52, 38, 70, 45, 63 y 91; recta numérica. Los números están escritos en cada ejercicio.",
    use="Aprenderé a encontrar la parte desconocida de una suma cuando conozco el total y una parte. Sirve para completar números que faltan en problemas.",
    prior=["Sé que dos partes forman un total.", "Sé restar para comparar números hasta 100."],
    explain=[
        "A veces conocemos el total y solo una de las partes. Por ejemplo: 30 + __ = 52. La parte que falta es lo que hay que agregar a 30 para llegar a 52. Se calcula restando: 52 − 30 = 22.",
        "Para comprobar, vuelve a sumar las partes: 30 + 22 = 52. Si coincide con el total, el número que encontraste es correcto. Esto es la idea del «todo» y las «partes»: parte + parte = todo, y todo − parte = otra parte.",
        "También puedes encontrar la parte que falta con una recta numérica: parte desde 30 y salta hasta 52. Das saltos de 10 (40, 50) y luego de 1 (51, 52): en total saltaste 22.",
    ],
    vocab=[("parte desconocida", "el número que falta en una suma"), ("todo o total", "el resultado de juntar las partes"), ("completar", "encontrar lo que falta"), ("diferencia", "lo que hay entre dos números"), ("comprobar", "sumar de nuevo para confirmar")],
    worked=[
        {"title": "Parte desconocida", "problem": "Completa: 30 + __ = 52.", "steps": ["Conozco el total 52 y una parte 30.", "Calculo 52 − 30 = 22.", "Compruebo: 30 + 22 = 52."], "answer": "22"},
        {"title": "Con la recta numérica", "problem": "Completa: 38 + __ = 70.", "steps": ["Parto en 38 y salto 2 para llegar a 40.", "De 40 a 70 son 30.", "Sumo los saltos: 2 + 30 = 32.", "Compruebo: 38 + 32 = 70."], "answer": "32"},
    ],
    mistakes=[
        {"wrong": "Responder 82 a 30 + __ = 52 porque se suman los números.", "why": "Se suman las partes conocidas en lugar de restar.", "fix": "Cuando falta una parte, resta el total menos la parte conocida."},
        {"wrong": "Responder 52 − 30 = 28.", "why": "Se resta mal sin revisar.", "fix": "Comprueba sumando: 30 + 28 = 58, no 52; el resultado correcto es 22."},
    ],
    tiers={
        "recovery": [
            arith("Completa: 30 + __ = 52. ¿Cuál es el número que falta?", "52-30", "52 − 30 = 22."),
            arith("Completa: 20 + __ = 45. ¿Cuál es el número que falta?", "45-20", "45 − 20 = 25."),
            arith("Completa: 60 + __ = 63. ¿Cuál es el número que falta?", "63-60", "63 − 60 = 3."),
        ],
        "understand": [
            ex("En 30 + __ = 52, ¿cuál es el total y cuál la parte que conoces?", "Total 52; parte conocida 30", "El total es el número que está después del igual."),
            ex("¿Hay que sumar o restar para encontrar una parte desconocida?", "Restar", "Todo − parte conocida = parte que falta."),
            ex("¿Cómo compruebo que 22 es la parte que falta en 30 + __ = 52?", "Sumo 30 + 22 y veo que da 52", "Si la suma coincide con el total, es correcto."),
        ],
        "apply": [
            arith("Completa: 47 + __ = 81.", "81-47", "81 − 47 = 34."),
            arith("Completa: __ + 25 = 91.", "91-25", "91 − 25 = 66."),
            arith("En una bolsa hay 45 caramelos. Si 28 son rojos y los demás verdes, ¿cuántos son verdes?", "45-28", "45 − 28 = 17."),
        ],
        "reason": [
            ex("Luis completó 30 + __ = 52 con 82. ¿Qué hizo mal?", "Sumó en vez de restar", "30 + 52 = 82, pero se necesitaba 52 − 30 = 22."),
            ex("Ana dice que en 40 + __ = 63 falta 23. ¿Es correcto?", "Sí", "63 − 40 = 23 y 40 + 23 = 63."),
        ],
        "challenge": [
            ex("Dos partes suman 90 y una de ellas es el doble de la otra. ¿Cuáles son?", "30 y 60", "30 + 60 = 90 y 60 es el doble de 30."),
            ex("Dos números suman 70 y su diferencia es 10. ¿Cuáles son?", "40 y 30", "40 + 30 = 70 y 40 − 30 = 10."),
        ],
    },
    context=[arith("En una biblioteca hay 63 libros en total. 40 son de cuentos y el resto son de ciencias. ¿Cuántos son de ciencias?", "63-40", "63 − 40 = 23; compruebo con 40 + 23 = 63.")],
    selfcheck=[ex("Completa: 20 + __ = 35.", "15", "35 − 20 = 15."), ex("Completa: __ + 6 = 50.", "44", "50 − 6 = 44."), ex("Comprueba: ¿es 30 + 22 igual a 52?", "Sí", "30 + 22 = 52.")],
    open_task={
        "statement": "Inventa un problema de una bolsa con 52 caramelos de los cuales 30 son rojos. Plantea la suma con parte desconocida, resuélvela y comprueba.",
        "example": "En una bolsa hay 52 caramelos. 30 son rojos y el resto verdes. 30 + __ = 52. Resto 52 − 30 = 22. Hay 22 verdes. Compruebo: 30 + 22 = 52.",
        "criteria": ["plantea la suma con parte desconocida", "calcula con una resta", "comprueba sumando", "responde con la unidad"],
        "evidence": ["planteamiento", "resta", "comprobación", "respuesta"],
        "errors": ["sumar en vez de restar", "no comprobar"],
        "feedback": "Reconoce el planteamiento; si sumó, pide que lea el problema y diga qué parte se desconoce; si no comprobó, que sume las partes.",
    },
    reinforce="Con 20 fichas, esconde algunas bajo un vaso, cuenta las que ves y calcula las escondidas.",
    extend="Inventa tres sumas con parte desconocida cuyo total sea 100 y resuélvelas; explica qué patrón ves en las partes que faltan.",
)
