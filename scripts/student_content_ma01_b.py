"""Student material for 1.º básico Matemática, OA 04 (comparar), OA 05 (estimar), OA 06 (componer) y OA 07 (cálculo mental) y OA 08 (decenas y unidades)."""
from __future__ import annotations

from student_content_ma01_a import dots, frame
from student_content_ma02_a import fill
from student_content_ma02_c import cmp_ex
from student_lessons import arith, ex, register

OA4, OA5, OA6, OA7, OA8 = "MA01 OA 04", "MA01 OA 05", "MA01 OA 06", "MA01 OA 07", "MA01 OA 08"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def pairs_ex(total: int) -> dict:
    parts = ", ".join(f"{a} + {total - a}" for a in range(total // 2 + 1))
    return ex(f"Escribe todas las parejas de sumandos que forman {total}, sin repetir el orden.", parts, f"Se parte de 0 y se sube el primer sumando hasta la mitad de {total}.")


# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Dos filas de fichas de colores distintos dibujadas en este cuaderno y lápiz. Las cantidades están escritas en cada ejercicio.",
    use="Aprenderé a comparar dos colecciones emparejando objeto con objeto. Sirve para saber, sin contar, si hay más, menos o la misma cantidad.",
    prior=["Sé contar hasta 20.", "Sé que más significa mayor cantidad y menos menor cantidad."],
    explain=[
        "Para comparar dos colecciones puedes emparejarlas: pones una ficha roja frente a una ficha azul y las unes con una línea. Si todas tienen pareja, hay la misma cantidad. Si sobran fichas de un color, ese color tiene más.",
        "Fíjate en lo que sobra. Si en la fila roja ● ● ● ● ● y en la azul ● ● ● quedan 2 rojas sin pareja, entonces hay más rojas que azules, y hay 2 más. Las azules son menos.",
        "Emparejar sirve aunque las fichas estén muy separadas o muy juntas. Lo que importa no es cuánto espacio ocupan, sino si cada una tiene su pareja. Después puedes contar para confirmar.",
    ],
    vocab=[("emparejar", "unir cada objeto de una colección con uno de la otra"), ("más", "tiene sobrantes al emparejar"), ("menos", "se quedó sin pareja para algunos de la otra"), ("la misma cantidad", "todos tienen pareja y no sobra nadie"), ("sobrante", "objeto que queda sin pareja")],
    worked=[
        {"title": "Emparejar dos filas", "problem": f"Fila roja: {dots(5)}. Fila azul: {dots(3)}. ¿Cuál tiene más?", "steps": ["Uno cada roja con una azul.", "Se acaban las azules con 3 parejas.", "Sobran 2 rojas.", "Las rojas tienen más."], "answer": "Las rojas tienen más; hay 2 más"},
        {"title": "La misma cantidad", "problem": f"Fila verde: {dots(4)}. Fila amarilla: {dots(4)}. ¿Hay más en alguna?", "steps": ["Emparejo una verde con una amarilla.", "Hay 4 parejas.", "No sobra ninguna."], "answer": "Hay la misma cantidad"},
    ],
    mistakes=[
        {"wrong": "Decir que la fila más larga tiene más.", "why": "Se compara el largo y no la cantidad.", "fix": "Empareja objeto con objeto; la fila más larga puede tener la misma cantidad."},
        {"wrong": "No contar lo que sobra.", "why": "Se ve que hay más pero no cuánto.", "fix": "Cuenta los sobrantes para decir cuántos más hay."},
    ],
    tiers={
        "recovery": [ex(f"Rojas: {dots(4)}. Azules: {dots(2)}. ¿Cuál color tiene más?", "Rojas", "Al emparejar sobran dos rojas."), ex(f"Tazas: {dots(3)}. Platos: {dots(3)}. ¿Hay más tazas, más platos o la misma cantidad?", "La misma cantidad", "Cada taza tiene su plato."), ex(f"Gatos: {dots(1)}. Perros: {dots(5)}. ¿Cuál tiene menos?", "Los gatos", "Hay un gato y cinco perros.")],
        "understand": [
            ex("Al emparejar, sobran 3 sillas. ¿Qué colección tiene más?", "La de las sillas", "Lo que sobra indica la colección mayor."),
            ex("¿Qué quiere decir «la misma cantidad» al emparejar?", "Que todos tienen pareja y no sobra ninguno", "Si no sobra nadie, son iguales."),
            ex("¿Importa si los objetos están muy separados para comparar?", "No", "Lo que cuenta es si cada uno tiene pareja."),
        ],
        "apply": [
            ex(f"Cuadernos: {dots(7)}. Lápices: {dots(4)}. ¿Cuál es mayor y cuántos más?", "Los cuadernos; 3 más", "Al emparejar sobran 3 cuadernos."),
            ex(f"Manzanas: {dots(6)}. Peras: {dots(8)}. ¿Cuál tiene menos y cuántas menos?", "Las manzanas; 2 menos", "Faltan 2 manzanas para igualar."),
            ex(f"Niños: {dots(9)}. Sillas: {dots(9)}. ¿Alcanzan las sillas sin que sobre ni falte?", "Sí", "Cada niño tiene su silla."),
        ],
        "reason": [
            ex("Juan dice que 5 fichas muy separadas son más que 5 fichas juntas. ¿Tiene razón?", "No", "Emparejándolas todas tienen pareja."),
            ex("En un baile hay 6 niñas y 5 niños. Si todos bailan en pareja, ¿qué pasa?", "Sobra una niña", "Hay una niña más."),
        ],
        "challenge": [
            ex("Tengo 8 fichas rojas. ¿Cuántas azules necesito para tener la misma cantidad?", "8", "Cada roja necesita su pareja azul."),
            ex("Hay 10 vasos y 7 tapas. ¿Cuántas tapas faltan para que cada vaso tenga una?", "3", "Sobran 3 vasos sin tapa."),
        ],
    },
    context=[ex(f"En una fiesta hay {dots(6)} globos y {dots(4)} niños. Si cada niño recibe un globo, ¿sobran o faltan globos? ¿Cuántos?", "Sobran 2 globos", "Cuatro globos se reparten y quedan dos.")],
    selfcheck=[ex(f"Soles: {dots(2)}. Lunas: {dots(5)}. ¿Cuál es mayor?", "Las lunas", "Cinco es más que dos."), ex("Si no sobra ninguno al emparejar, ¿qué cantidad tienen?", "La misma", "Todos tienen pareja."), ex("¿Cómo se llama unir cada objeto con otro?", "Emparejar", "Es unir uno con uno.")],
    open_task=task("Con 8 tapas rojas y 5 tapas azules (o dibújalas), empareja y escribe cuál color tiene más, cuántos más y cuántos menos tiene el otro.", "Emparejé 5 rojas con 5 azules y me sobraron 3 rojas. Las rojas tienen más (3 más) y las azules tienen menos (3 menos).", ["empareja uno con uno", "dice qué color tiene más", "cuenta cuántos más"], ["dibujo con líneas de pareja", "frase de comparación"], ["comparar por el largo de la fila", "no contar los sobrantes"], "Reconoce el emparejamiento y pide contar cuántas rojas sobraron."),
    reinforce="Compara dos montones de fichas emparejándolas sobre la mesa.",
    extend="Compara tres colecciones y ordénalas de menos a más sin contarlas, sólo emparejando.",
)

register(
    OA4, 2,
    materials="Tarjetas con los números del 0 al 20 en este cuaderno, recta numérica y lápiz. Las comparaciones están escritas en cada ejercicio.",
    use="Aprenderé a decir cuál de dos números es mayor, menor o igual y a escribirlo con los signos >, < e =. Sirve para decidir quién tiene más figuritas o puntos.",
    prior=["Sé comparar colecciones emparejando.", "Sé leer los números hasta 20."],
    explain=[
        "El número que aparece más tarde al contar es el mayor. Si cuentas 1, 2, 3, 4, 5, el 5 aparece después del 3: 5 es mayor que 3. En la recta numérica, el mayor está más a la derecha.",
        "Los signos son una boca que se abre hacia el número mayor. 8 > 5 se lee «ocho es mayor que cinco». 5 < 8 se lee «cinco es menor que ocho». Si los dos números son iguales se usa =: 7 = 7.",
        "Para estar seguro, dibuja los dos números con puntos y empareja. El número con sobrantes es el mayor. Esto sirve cuando dudas: por ejemplo, entre 12 y 9, 12 tiene diez y dos y 9 no llega a diez.",
    ],
    vocab=[("mayor que (>)", "tiene más cantidad"), ("menor que (<)", "tiene menos cantidad"), ("igual (=)", "tiene la misma cantidad"), ("recta numérica", "línea con los números en orden"), ("signo", "dibujo especial que escribe la comparación")],
    worked=[
        {"title": "Elegir el signo", "problem": "Compara 12 y 9.", "steps": ["12 tiene un diez y 2 unidades; 9 no llega a diez.", "En la recta, 12 está más a la derecha.", "12 es mayor: 12 > 9."], "answer": "12 > 9"},
        {"title": "Números iguales", "problem": "Compara 15 y 15.", "steps": ["Los dos números son el mismo.", "Tienen la misma cantidad.", "Uso el signo =."], "answer": "15 = 15"},
    ],
    mistakes=[
        {"wrong": "Escribir 5 > 8.", "why": "Se invierte la dirección del signo.", "fix": "La boca se abre hacia el mayor: 8 > 5."},
        {"wrong": "Decir que 9 es mayor que 12 porque 9 es una cifra grande.", "why": "Se mira la cifra y no la cantidad.", "fix": "12 es un diez y dos; 9 es menos de un diez."},
    ],
    tiers={
        "recovery": [cmp_ex(7, 4, "7 aparece después de 4 al contar."), cmp_ex(3, 9, "3 aparece antes que 9."), cmp_ex(10, 10, "Son el mismo número.")],
        "understand": [
            ex("¿Hacia qué número se abre la boca del signo > o <?", "Hacia el mayor", "Se abre donde hay más cantidad."),
            ex("En la recta numérica, ¿dónde está el mayor?", "Más a la derecha", "Al contar se avanza hacia la derecha."),
            ex("¿Cómo se lee 6 < 13?", "Seis es menor que trece", "El signo < dice menor."),
        ],
        "apply": [cmp_ex(14, 11, "14 aparece después de 11."), cmp_ex(8, 17, "8 aparece antes que 17."), cmp_ex(20, 19, "20 va justo después de 19.")],
        "reason": [
            ex("Ema escribió 9 > 12. ¿Qué error cometió?", "Invirtió el signo; es 9 < 12", "12 es mayor que 9."),
            ex("¿Es verdadero que 15 > 15? Explica.", "No; son iguales", "Dos números iguales no son uno mayor que el otro."),
        ],
        "challenge": [
            ex("Escribe un número que sea mayor que 12 y menor que 15.", "13 o 14", "Entre 12 y 15 están el 13 y el 14."),
            ex("Escribe tres números menores que 6.", "Por ejemplo 0, 3 y 5", "Todos aparecen antes que 6 al contar."),
        ],
    },
    context=[ex("Lila tiene 13 figuritas y Tomás tiene 16. Escribe la comparación con un signo y di quién tiene menos.", "13 < 16; Lila tiene menos", "16 aparece después que 13.")],
    selfcheck=[cmp_ex(2, 12, "2 está antes del 12."), cmp_ex(18, 8, "18 es un diez y ocho."), ex("¿Qué signo se usa cuando hay la misma cantidad?", "=", "Igual se escribe con dos rayitas.")],
    open_task=task("Elige los pares 6 y 11, 15 y 9, 13 y 13. Escribe el signo en cada par y dibuja con puntos uno de los números para comprobar.", "6 < 11, 15 > 9 y 13 = 13. Dibujé 11 puntos y vi que es un diez y uno, más que 6.", ["usa el signo correcto", "dibuja para comprobar", "lee la comparación"], ["tres signos", "dibujo", "lectura"], ["invertir el signo", "no comprobar"], "Pide leer cada comparación en voz alta usando mayor, menor o igual."),
    reinforce="Saca dos tarjetas del 0 al 20 y di cuál es mayor.",
    extend="Busca todos los números que son mayores que 8 y menores que 14.",
)

register(
    OA4, 3,
    materials="Tarjetas con los números 3, 17, 9, 14, 6, 20, 11 y 0 en este cuaderno y una recta numérica de 0 a 20.",
    use="Aprenderé a ordenar varios números del 0 al 20 de menor a mayor y de mayor a menor. Sirve para armar filas de puntajes o tarjetas.",
    prior=["Sé comparar dos números.", "Sé ubicar números en la recta."],
    explain=[
        "Ordenar es poner los números en una fila según su tamaño. De menor a mayor empiezas con el número más pequeño y terminas con el más grande. De mayor a menor haces lo contrario.",
        "Una buena forma es buscar primero el menor de todos, luego el menor de los que quedan, y así hasta terminar. También puedes ubicar cada número en la recta numérica y leerla de izquierda a derecha.",
        "Cuando termines, comprueba que cada número sea mayor que el anterior si ordenaste de menor a mayor. Si alguno no cumple, hay que cambiarlo de lugar.",
    ],
    vocab=[("ordenar", "poner en fila según un criterio"), ("de menor a mayor", "del más pequeño al más grande"), ("de mayor a menor", "del más grande al más pequeño"), ("el menor", "el más pequeño de todos"), ("el mayor", "el más grande de todos")],
    worked=[
        {"title": "Ordenar de menor a mayor", "problem": "Ordena: 17, 3, 9, 14.", "steps": ["El menor es 3.", "Entre 17, 9 y 14, el menor es 9.", "Entre 17 y 14, el menor es 14.", "Queda 17."], "answer": "3, 9, 14, 17"},
        {"title": "Ordenar de mayor a menor", "problem": "Ordena: 6, 20, 11, 0.", "steps": ["El mayor es 20.", "Luego 11.", "Luego 6.", "Al final 0."], "answer": "20, 11, 6, 0"},
    ],
    mistakes=[
        {"wrong": "Ordenar 9, 14, 3 como 3, 14, 9.", "why": "No se compara el 14 con el 9.", "fix": "Compara cada número con el anterior: 9 va antes que 14."},
        {"wrong": "Mezclar menor a mayor con mayor a menor.", "why": "No se lee el sentido pedido.", "fix": "Antes de ordenar, lee si piden menor a mayor o mayor a menor."},
    ],
    tiers={
        "recovery": [ex("Ordena de menor a mayor: 5, 2, 8.", "2, 5, 8", "El menor es 2, luego 5 y el mayor 8."), ex("Ordena de menor a mayor: 10, 4, 7.", "4, 7, 10", "4 antes que 7 y 7 antes que 10."), ex("Ordena de mayor a menor: 3, 9, 6.", "9, 6, 3", "El mayor es 9, luego 6, luego 3.")],
        "understand": [
            ex("¿Cuál es el menor de 12, 5 y 19?", "5", "5 aparece antes que 12 y 19."),
            ex("¿Cuál es el mayor de 12, 5 y 19?", "19", "19 aparece después que 12 y 5."),
            ex("En una lista ordenada de menor a mayor, ¿qué número va al final?", "El mayor", "Termina con el más grande."),
        ],
        "apply": [
            ex("Ordena de menor a mayor: 17, 3, 9, 14.", "3, 9, 14, 17", "Se busca siempre el menor que queda."),
            ex("Ordena de mayor a menor: 6, 20, 11, 0.", "20, 11, 6, 0", "Se parte por el mayor."),
            ex("Ordena de menor a mayor: 13, 18, 12, 15, 11.", "11, 12, 13, 15, 18", "Todos tienen un diez, luego decide la unidad."),
        ],
        "reason": [
            ex("Pablo ordenó 4, 14, 9, 19 como 4, 9, 14, 19. ¿Está de menor a mayor?", "Sí", "Cada número es mayor que el anterior."),
            ex("Ana ordenó 2, 12, 7 como 2, 12, 7. ¿Qué número cambia de lugar?", "El 7 va antes del 12", "Menor a mayor es 2, 7, 12."),
        ],
        "challenge": [
            ex("Escribe tres números entre 5 y 15 y ordénalos de mayor a menor.", "Por ejemplo 12, 9, 7", "Los tres están entre 5 y 15."),
            ex("Hay números de 0 a 20 en una fila de menor a mayor. ¿Qué número va justo antes del 13?", "12", "Antes del 13 va el 12."),
        ],
    },
    context=[ex("Cuatro niños saltaron 8, 15, 11 y 6 veces la cuerda. Ordena de menor a mayor y di quién saltó más.", "6, 8, 11, 15; saltó más quien hizo 15", "El mayor va al final.")],
    selfcheck=[ex("Ordena de menor a mayor: 9, 1, 5.", "1, 5, 9", "1 es el menor y 9 el mayor."), ex("¿Cuál es el mayor de 14, 7 y 16?", "16", "16 aparece después de 14 y 7."), ex("Ordena de mayor a menor: 2, 10, 6.", "10, 6, 2", "Se empieza por el mayor.")],
    open_task=task("Escribe en tarjetas los números 7, 16, 2, 12 y 19. Ordénalos de menor a mayor y luego de mayor a menor. Explica cómo encontraste el primero de cada fila.", "Menor a mayor: 2, 7, 12, 16, 19. Mayor a menor: 19, 16, 12, 7, 2. Para menor a mayor busqué el que está primero al contar, el 2; para mayor a menor busqué el último, el 19.", ["ordena las dos filas", "las filas son inversas", "explica cómo eligió el primero"], ["dos listas", "explicación"], ["listas no inversas", "olvidar un número"], "Pide comprobar que cada lista tenga los cinco números."),
    reinforce="Ordena 5 tarjetas con números del 0 al 20 sobre la recta.",
    extend="Ordena 6 números y luego cambia sólo uno para que la lista no quede ordenada; explica cuál cambiaste.",
)

register(
    OA4, 4,
    materials="Problemas escritos en cada ejercicio, fichas y recta numérica de este cuaderno.",
    use="Aprenderé a usar la comparación para resolver problemas, por ejemplo saber cuántos más o cuántos menos hay. Sirve para repartir y para decidir.",
    prior=["Sé comparar y ordenar números hasta 20.", "Sé emparejar colecciones y contar lo que sobra."],
    explain=[
        "En un problema de comparar, hay dos cantidades y se pregunta cuál es mayor, cuál es menor o cuánto más hay. Primero identifica las dos cantidades. Luego usa los signos o el emparejamiento. Lo que sobra también se puede escribir como resta: 9 − 6 = 3.",
        "Para saber cuántos más hay, empareja: si Ana tiene 9 y Beto tiene 6, empareja 6 con 6 y cuenta lo que sobra, que son 3. Ana tiene 3 más. Beto tiene 3 menos.",
        "Revisa siempre la pregunta. A veces pide «quién tiene más» y a veces «cuántos más». La primera se responde con un nombre; la segunda, con un número.",
    ],
    vocab=[("cuántos más", "la diferencia entre dos cantidades"), ("cuántos menos", "lo que le falta a la menor para igualar"), ("diferencia", "lo que sobra al emparejar"), ("igualar", "hacer que tengan la misma cantidad"), ("problema", "situación con una pregunta")],
    worked=[
        {"title": "Cuántos más", "problem": "Ana tiene 9 figuritas y Beto tiene 6. ¿Quién tiene más y cuántas más?", "steps": ["Empareja 6 con 6.", "Sobran 3 de Ana.", "Ana tiene 9 > 6.", "Tiene 3 más."], "answer": "Ana; 3 más"},
        {"title": "Igualar", "problem": "Hay 12 pelotas y 8 niños. ¿Cuántas pelotas sobran si cada niño toma una?", "steps": ["Empareja 8 niños con 8 pelotas.", "Sobran 4 pelotas."], "answer": "Sobran 4 pelotas"},
    ],
    mistakes=[
        {"wrong": "Responder con un número cuando preguntan quién.", "why": "No se lee la pregunta.", "fix": "Si preguntan quién, responde un nombre."},
        {"wrong": "Sumar en vez de comparar.", "why": "Se confunde juntar con comparar.", "fix": "Comparar es mirar la diferencia; juntar sería sumar."},
    ],
    tiers={
        "recovery": [ex("Lucía tiene 8 lápices y Mario tiene 5. ¿Quién tiene más?", "Lucía", "8 es mayor que 5."), ex("Hay 6 niños y 6 sillas. ¿Sobran sillas?", "No", "Hay la misma cantidad."), ex("Pedro tiene 4 globos y Sara tiene 7. ¿Quién tiene menos?", "Pedro", "4 es menor que 7.")],
        "understand": [
            ex("¿Cómo averiguas cuántos más tiene Ana si tiene 9 y Beto 6?", "Emparejo y cuento lo que sobra", "La diferencia es lo que sobra."),
            ex("Si Ana tiene 3 más que Beto, ¿Beto tiene más o menos?", "Menos", "Beto tiene 3 menos que Ana."),
            ex("¿Qué debes leer antes de responder un problema?", "La pregunta", "Dice si piden un nombre o un número."),
        ],
        "apply": [
            arith("Tengo 14 fichas azules y 9 rojas. ¿Cuántas más azules que rojas hay?", "14-9", "Al emparejar sobran las azules que no tienen pareja."),
            arith("En un curso hay 18 niños y 12 niñas. ¿Cuántos más niños que niñas hay?", "18-12", "Se empareja cada niña con un niño y se cuenta lo que sobra."),
            arith("Tengo 10 galletas y 3 niños quieren una cada uno. ¿Cuántas galletas sobran?", "10-3", "Tres galletas se reparten y el resto sobra."),
        ],
        "reason": [
            ex("Joaquín dice que Ana tiene 9 y Beto 6, así que Beto tiene más porque 6 es el último. ¿Qué error comete?", "Compara el orden en que se dicen y no las cantidades; Ana tiene más", "9 es mayor que 6."),
            ex("Si una caja tiene 11 lápices y otra tiene 11, ¿cuántos más tiene una?", "0; tienen la misma cantidad", "Al emparejar no sobra ninguno."),
        ],
        "challenge": [
            ex("Mara tiene 7 y Teo tiene 3 más que Mara. ¿Cuántos tiene Teo?", "10", "7 y 3 más son 10."),
            ex("Ema tiene 15 y quiere igualar a Lola, que tiene 11. ¿Cuántos debe regalar?", "4", "15 − 11 = 4."),
        ],
    },
    context=[arith("En un bus hay 16 asientos y 9 pasajeros. ¿Cuántos asientos están vacíos?", "16-9", "Se empareja cada pasajero con un asiento y se cuenta lo que sobra.")],
    selfcheck=[ex("¿Qué es mayor: 13 o 10?", "13", "13 es un diez y tres."), arith("Ana tiene 12 y Beto tiene 7. ¿Cuántos más tiene Ana?", "12-7", "Se resta lo menor a lo mayor."), ex("Si no sobra ninguno al emparejar, ¿las cantidades son...?", "Iguales", "No hay diferencia.")],
    open_task=task("Inventa un problema sobre comparar dos colecciones con números del 0 al 20 (por ejemplo 15 y 9). Escribe la pregunta, resuélvelo con emparejamiento y escribe el signo.", "Tengo 15 canicas y mi amigo 9. ¿Cuántas más tengo? Emparejé 9 con 9 y sobraron 6. 15 > 9 y tengo 6 más.", ["usa dos números del 0 al 20", "escribe la pregunta", "resuelve y usa el signo"], ["problema", "dibujo o emparejamiento", "signo"], ["pregunta confusa", "resultado sin explicación"], "Pide leer el problema y revisar que la pregunta tenga una sola respuesta."),
    reinforce="Compara dos montones de tapas y averigua cuántas más hay en uno.",
    extend="Crea un problema en que haya que igualar dos colecciones y resuélvelo.",
)

# ---------------------------------------------------------------- OA 05
register(
    OA5, 1,
    materials=f"Un marco de cinco ({dots(5)}) y las colecciones dibujadas en cada ejercicio; lápiz.",
    use="Aprenderé a estimar cuántos objetos hay mirando cuántos grupos de cinco caben. Sirve para decir rápido «hay más o menos tantos» sin contar uno por uno.",
    prior=["Sé contar de 5 en 5.", "Sé qué es estimar: decir una cantidad cercana."],
    explain=[
        "Estimar es decir un número cercano a la cantidad real sin contar todo. Para estimar bien necesitas un referente, una cantidad que conoces. Aquí usamos el cinco: ● ● ● ● ●.",
        "Mira cuántos grupos de cinco te parece que caben en la colección. Si caben dos grupos, estimas cerca de 10; si caben tres, cerca de 15. No es exacto, pero te acerca.",
        "Después de estimar puedes contar para comprobar. Si estimaste 10 y había 11, tu estimación fue muy buena. Si estimaste 10 y había 18, hay que mirar de nuevo el referente.",
    ],
    vocab=[("estimar", "decir una cantidad cercana sin contar todo"), ("referente", "cantidad conocida para comparar, como 5"), ("cerca de", "casi igual a"), ("grupo de cinco", "cinco objetos juntos"), ("comprobar", "contar para ver qué tan cerca estuve")],
    worked=[
        {"title": "Estimar con cinco", "problem": "Una colección parece ocupar el espacio de tres grupos de cinco. ¿Cuánto estimas?", "steps": ["Un grupo vale 5.", "Tres grupos: 5, 10, 15.", "Estimo cerca de 15."], "answer": "Cerca de 15"},
        {"title": "Comprobar", "problem": "Estimé 10 y al contar había 12. ¿Estimé bien?", "steps": ["De 10 a 12 hay 2 lugares: la diferencia es 2.", "2 es una diferencia pequeña.", "Estimé bien."], "answer": "Sí, 2 de diferencia"},
    ],
    mistakes=[
        {"wrong": "Estimar 3 si caben tres grupos de cinco.", "why": "Se cuenta el número de grupos y no el de objetos.", "fix": "Cada grupo vale 5: tres grupos son 15."},
        {"wrong": "Estimar sin comparar con el referente.", "why": "Se dice un número al azar.", "fix": "Usa el grupo de cinco como medida."},
    ],
    tiers={
        "recovery": [arith("Una colección ocupa 2 grupos de cinco. ¿Cuánto estimas?", "2*5", "Dos grupos de 5 son 10."), arith("Otra ocupa 1 grupo de cinco. ¿Cuánto estimas?", "1*5", "Un grupo vale 5."), arith("Otra ocupa 4 grupos de cinco. ¿Cuánto estimas?", "4*5", "Cuatro grupos son 20.")],
        "understand": [
            ex("¿Para qué sirve un referente al estimar?", "Para comparar con una cantidad conocida", "Sirve como medida."),
            ex("Si estimo «cerca de 15», ¿hay exactamente 15?", "No necesariamente", "Estimar es acercarse."),
            ex("¿Cuántos puntos tiene un grupo de cinco?", "5", "Así se define el referente."),
        ],
        "apply": [
            ex(f"Hay {dots(5)} y un grupo parecido. ¿Cuánto estimas en total?", "Cerca de 10", "Son dos grupos de cinco."),
            arith("Una caja tiene tres grupos de cinco bolitas y 2 sueltas. ¿Cuántas bolitas hay?", "3*5+2", "15 y 2 más."),
            ex("Estimé 15 y había 14. ¿Qué tan buena fue mi estimación?", "Muy buena; 1 de diferencia", "15 − 14 = 1."),
        ],
        "reason": [
            ex("Rocío dice que tres grupos de cinco son 3. ¿Qué error comete?", "Cuenta grupos y no objetos; son 15", "Cada grupo vale 5."),
            ex("¿Por qué conviene comparar con un grupo de cinco al estimar?", "Porque da una medida conocida", "Se ve cuántas veces cabe."),
        ],
        "challenge": [
            ex("Estimé 20 y había 16. Otra persona estimó 10. ¿Quién se acercó más?", "Yo (20)", "20 − 16 = 4 y 16 − 10 = 6."),
            ex("Una colección ocupa 4 grupos de cinco menos 2 objetos. ¿Cuántos hay?", "18", "20 − 2 = 18."),
        ],
    },
    context=[arith("En una bandeja hay 3 filas de 5 galletas. Estima y calcula cuántas galletas hay.", "3*5", "Tres filas de 5 son 15 galletas.")],
    selfcheck=[ex("¿Qué número estimas si caben 2 grupos de cinco?", "Cerca de 10", "Dos grupos de cinco: 5 y 5 son 10."), ex("¿Qué es estimar?", "Decir un número cercano sin contar todo", "No es contar uno por uno."), arith("¿Cuántos son 4 grupos de cinco?", "4*5", "Cuatro grupos de 5 son 20.")],
    open_task=task(f"Mira esta colección: {dots(5)} {dots(5)} {dots(3)}. Estima cuántos puntos hay usando el grupo de cinco, escribe tu estimación y luego cuenta para comprobar.", "Veo dos grupos de cinco y casi otro más, estimo cerca de 13. Al contar hay 13 puntos: coincidió.", ["usa el referente de cinco", "da un número cercano", "comprueba contando"], ["estimación", "conteo", "diferencia"], ["estimar sin referente", "no comprobar"], "Reconoce el uso del referente y pide calcular la diferencia."),
    reinforce="Con 12 fichas, arma grupos de cinco y estima cuántos hay antes de contar.",
    extend="Estima una colección de 18 objetos usando cinco como referente y compara con tu amigo.",
)

register(
    OA5, 2,
    materials=f"Un marco de diez ({frame(10)}) y las colecciones dibujadas en cada ejercicio; lápiz.",
    use="Aprenderé a estimar usando el diez como referente. Sirve para estimar cantidades mayores sin contar de a una.",
    prior=["Sé estimar con grupos de cinco.", "Sé que diez llena un marco de diez."],
    explain=[
        "El diez es un buen referente: un marco lleno. Si miras una colección y piensas que llenaría un marco y un poco más, estimas entre 10 y 15. Si llenaría casi dos marcos, estimas cerca de 20.",
        "Compara siempre con el marco. Si la colección es menos que el marco, tiene menos de 10; si es más, tiene más de 10. Esto ya te dice si tu estimación está bien dirigida.",
        "Después ajusta: «es más que 10, pero no llega a 20, estimo 15». Y comprueba contando. Cada vez que compruebes, tu ojo mejora.",
    ],
    vocab=[("marco de diez", "dos filas de cinco casillas"), ("referente de diez", "una colección conocida que tiene diez"), ("más que diez", "supera el marco lleno"), ("menos que diez", "no llena el marco"), ("ajustar", "corregir mi estimación al comparar de nuevo")],
    worked=[
        {"title": "Comparar con diez", "problem": "Una colección llena un marco de diez y parece tener un poco más. ¿Cuánto estimas?", "steps": ["Un marco lleno es 10.", "Un poco más que 10.", "Estimo entre 11 y 13, por ejemplo 12."], "answer": "Cerca de 12"},
        {"title": "Casi dos marcos", "problem": "Una colección casi llena dos marcos de diez. ¿Cuánto estimas?", "steps": ["Dos marcos llenos son 20.", "Casi llena: un poco menos que 20.", "Estimo cerca de 18."], "answer": "Cerca de 18"},
    ],
    mistakes=[
        {"wrong": "Estimar 20 para una colección que no llena un marco.", "why": "No se compara con el referente.", "fix": "Si no llena el marco de diez, tiene menos de diez."},
        {"wrong": "Estimar 1 para un marco lleno.", "why": "Se cuentan marcos y no objetos.", "fix": "Un marco lleno son diez objetos."},
    ],
    tiers={
        "recovery": [ex("Una colección llena exactamente un marco de diez. ¿Cuánto es?", "10", "Un marco lleno es diez."), ex("Una colección no llena un marco. ¿Tiene más o menos de diez?", "Menos", "El marco no se llenó."), ex("Dos marcos de diez llenos, ¿cuánto son?", "20", "10 y 10 son 20.")],
        "understand": [
            ex("Si una colección es más que un marco lleno, ¿tiene más o menos de diez?", "Más", "Supera el marco lleno."),
            ex("¿Qué estimas para una colección entre uno y dos marcos?", "Entre 10 y 20", "Es más que uno y menos que dos."),
            ex("¿Para qué sirve comparar con el marco de diez?", "Para saber si hay más o menos de diez", "Es la medida conocida."),
        ],
        "apply": [
            ex(f"En un frasco hay una colección que parece {dots(10)} y 3 más. ¿Cuánto estimas?", "Cerca de 13", "Diez y tres más."),
            ex("Una bolsa casi llena un marco de diez: le faltan 2 casillas para llenarlo. ¿Cuántos hay?", "8", "Faltan 2 para llegar a 10, así que hay 8."),
            ex("Un frasco llena un marco y medio marco más. ¿Cuánto estimas?", "Cerca de 15", "Diez y cinco."),
        ],
        "reason": [
            ex("Beto dice que si llena un marco hay exactamente 10 y nada más. ¿Tiene razón?", "Sí", "Un marco lleno es diez."),
            ex("Estimé 10 y había 17. ¿Qué debo mirar de nuevo?", "Que se pasaba del marco lleno", "17 es mucho más que 10."),
        ],
        "challenge": [
            ex("Estimé 15 y había 13. Mi amigo estimó 18. ¿Quién se acercó más?", "Yo (15)", "15 − 13 = 2 y 18 − 13 = 5."),
            ex("Dos marcos llenos y otro con 3. ¿Cuántos hay en total?", "23", "10, 20 y 3 más."),
        ],
    },
    context=[ex("En una caja hay lápices que llenan un marco de diez y sobran 4. Estima y calcula cuántos hay.", "14", "Diez y cuatro más.")],
    selfcheck=[ex("¿Cuánto es un marco de diez lleno?", "10", "Un marco lleno tiene diez objetos."), ex("Estimé 12 y había 11. ¿Diferencia?", "1", "12 − 11 = 1."), ex("Si no llena el marco, ¿hay más o menos de 10?", "Menos", "No llega a diez.")],
    open_task=task(f"Mira esta colección: {dots(10)} {dots(6)}. Compárala con el marco de diez, estima cuántos puntos hay y cuenta para comprobar.", "Llena un marco de diez y sobra un poco más de medio marco; estimo cerca de 16. Al contar hay 16.", ["compara con el marco", "da una estimación cercana", "comprueba contando"], ["estimación", "conteo"], ["no comparar con el referente", "estimar al azar"], "Pide explicar con palabras qué parte del marco se llenó."),
    reinforce="Llena marcos de diez con fichas y estima antes de contar.",
    extend="Estima el número de tapas que caben en una caja pequeña y comprueba.",
)

register(
    OA5, 3,
    materials=f"Dos dibujos del mismo número de objetos (12) en este cuaderno: A) {dots(12)} juntos en una fila y B) objetos esparcidos descritos en el texto.",
    use="Aprenderé que la misma cantidad puede verse más grande o más pequeña según cómo esté puesta. Sirve para no engañarme al estimar.",
    prior=["Sé estimar con referentes de cinco y diez.", "Sé comparar cantidades."],
    explain=[
        "Dos grupos con la misma cantidad pueden parecer distintos. Si 12 fichas están muy juntas ocupan poco espacio; si están muy separadas ocupan mucho. Pero siguen siendo 12.",
        "Para no engañarte, imagina que acomodas todo en filas de cinco o en marcos de diez. Así comparas la cantidad y no el espacio. Si cabe un marco de diez y 2 más, hay 12, aunque estén separados.",
        "Cuando estimes, no te fijes sólo en si ocupa mucho lugar. Pregunta: ¿cuántos grupos de cinco o diez formaría? Esa pregunta te ayuda a estimar mejor.",
    ],
    vocab=[("disposición", "cómo están puestos los objetos"), ("juntos", "muy cerca unos de otros"), ("esparcidos", "repartidos por todo el espacio"), ("misma cantidad", "igual número de objetos"), ("engañar", "hacer creer algo que no es cierto")],
    worked=[
        {"title": "Mismo número, distinta disposición", "problem": "Hay 12 fichas juntas en una fila y 12 fichas esparcidas en una hoja. ¿Dónde hay más?", "steps": ["Las dos tienen 12.", "En la hoja ocupan más espacio, pero la cantidad es la misma.", "No hay más en ninguna."], "answer": "Hay la misma cantidad"},
        {"title": "Imaginar los marcos", "problem": "Hay fichas esparcidas. Pienso que cabrían en un marco de diez y 3 más. ¿Cuánto estimo?", "steps": ["Un marco de diez lleno es 10.", "Más 3 es 13.", "Estimo 13."], "answer": "Cerca de 13"},
    ],
    mistakes=[
        {"wrong": "Decir que lo más esparcido es más.", "why": "Se compara el espacio y no la cantidad.", "fix": "Agrupa mentalmente en cinco o diez."},
        {"wrong": "Estimar sin agrupar.", "why": "Se estima por la mancha.", "fix": "Pregunta cuántos grupos de cinco formarías."},
    ],
    tiers={
        "recovery": [ex("Hay 8 fichas juntas y 8 fichas separadas. ¿Dónde hay más?", "En ninguna; hay la misma cantidad", "Ambas son 8."), ex("Muevo 6 fichas de un lado a otro. ¿Cuántas hay ahora?", "6", "Mover no cambia la cantidad."), ex("¿Cambia la cantidad si pongo las fichas más lejos?", "No", "Sólo cambia dónde están.")],
        "understand": [
            ex("¿Qué debo mirar al estimar: el espacio que ocupan o cuántos grupos de cinco o diez forman?", "Cuántos grupos forman", "Eso mide la cantidad."),
            ex("Dos grupos tienen 9 objetos. Uno está esparcido. ¿Cuál parece más grande?", "El esparcido", "Ocupa más espacio."),
            ex("¿Parecer más grande significa tener más?", "No siempre", "Puede ocupar más espacio."),
        ],
        "apply": [
            arith("Imagino que las fichas esparcidas llenan un marco de diez y 4 más. ¿Cuántas son?", "10+4", "Diez y cuatro."),
            ex("Imagino que unas fichas esparcidas forman dos grupos de cinco. ¿Cuánto estimo?", "Cerca de 10", "Dos grupos de cinco."),
            ex("Pongo 7 fichas muy juntas y otras 7 muy separadas. ¿Cuántas fichas hay en total?", "14", "7 y 7 son 14."),
        ],
        "reason": [
            ex("Tomás dice que 9 fichas esparcidas son más que 9 fichas juntas. ¿Tiene razón?", "No", "Son 9 en ambos casos."),
            ex("¿Por qué conviene agrupar mentalmente al estimar?", "Para comparar cantidad y no espacio", "Los grupos no cambian con el espacio."),
        ],
        "challenge": [
            ex("Hay 15 fichas esparcidas. ¿Cuántos grupos de cinco forman?", "3", "Cuento de 5 en 5: 5, 10, 15. Son 3 grupos."),
            ex("Hay 10 fichas juntas y 12 esparcidas. ¿Dónde hay más?", "En las esparcidas", "12 es mayor que 10."),
        ],
    },
    context=[ex("En el patio hay 11 niños jugando por todas partes y en la sala 11 sentados. ¿Dónde hay más niños?", "Hay los mismos", "11 y 11 son iguales.")],
    selfcheck=[ex("Si mueves las fichas sin quitar ni agregar, ¿cambia la cantidad?", "No", "Sigue siendo la misma."), arith("Dos grupos de cinco y 3 más, ¿cuántos son?", "2*5+3", "10 y 3 más."), ex("¿Qué grupo ocupa más espacio: uno junto o uno esparcido?", "El esparcido", "Está más separado.")],
    open_task=task("Pon 9 fichas muy juntas y luego esparcidas. Dibuja las dos disposiciones, estima cuántas hay en cada una y explica por qué el número es el mismo.", "Dibujé 9 juntas y 9 separadas. Estimé 10 en las dos. Son 9 porque no agregué ni quité ninguna.", ["dibuja las dos disposiciones", "estima en ambas", "explica por qué son iguales"], ["dibujos", "estimaciones", "explicación"], ["decir que una tiene más", "no agrupar"], "Pide contar de nuevo para confirmar que no cambia."),
    reinforce="Mueve 8 fichas de lugar y cuenta cada vez.",
    extend="Diseña un dibujo donde 10 objetos parezcan muchos y otro donde parezcan pocos.",
)

register(
    OA5, 4,
    materials="Tres colecciones escritas con su conteo real en cada ejercicio; marco de diez; lápiz.",
    use="Aprenderé a elegir una estimación razonable y a comprobarla contando. Sirve para saber si una estimación sirve o hay que mejorarla.",
    prior=["Sé estimar con cinco y con diez.", "Sé contar en la recta numérica de un número a otro."],
    explain=[
        "Una estimación razonable es la que se acerca bastante a la cantidad real. Aquí diremos que es razonable si se aleja 3 o menos del número real. La diferencia es cuántos lugares hay de un número al otro en la recta. De 12 a 14 hay 2 lugares, así que la diferencia es 2: razonable. También se escribe como resta: 14 − 12 = 2.",
        "Para elegir entre varias estimaciones, ve cuál queda más cerca. Si hay 13 y las opciones son 5, 12 y 20, la más cercana es 12, porque 13 − 12 = 1.",
        "Cuando una estimación no es razonable, pregúntate qué falló: ¿usé bien el referente? ¿Me engañó el espacio? Con esa pregunta mejoras la próxima.",
    ],
    vocab=[("razonable", "que se acerca bastante a lo real"), ("diferencia", "lo que separa dos números; se calcula restando el menor al mayor"), ("más cercana", "la que tiene menor diferencia"), ("cantidad real", "lo que da al contar"), ("mejorar", "acercarse más la próxima vez")],
    worked=[
        {"title": "Evaluar una estimación", "problem": "Estimé 12 y al contar había 14. ¿Fue razonable?", "steps": ["14 − 12 = 2.", "2 es menor o igual que 3.", "Es razonable."], "answer": "Sí, razonable"},
        {"title": "Elegir la más cercana", "problem": "Hay 13 objetos. Opciones: 5, 12, 20. ¿Cuál es la más cercana?", "steps": ["13 − 5 = 8.", "13 − 12 = 1.", "20 − 13 = 7.", "La menor diferencia es 1."], "answer": "12"},
    ],
    mistakes=[
        {"wrong": "Restar el mayor al menor.", "why": "Se resta al revés.", "fix": "Siempre resta el menor al mayor para obtener la diferencia."},
        {"wrong": "Decir que estimar de más es mejor.", "why": "Se cree que pasarse es seguro.", "fix": "Una estimación es buena cuando está cerca, sea mayor o menor."},
    ],
    tiers={
        "recovery": [arith("Estimé 10 y había 12. ¿Cuál es la diferencia?", "12-10", "12 − 10 = 2."), arith("Estimé 15 y había 14. ¿Cuál es la diferencia?", "15-14", "15 − 14 = 1."), arith("Estimé 8 y había 13. ¿Cuál es la diferencia?", "13-8", "13 − 8 = 5.")],
        "understand": [
            ex("¿Una diferencia de 2 es razonable en este curso?", "Sí", "Es menor o igual que 3."),
            ex("¿Una diferencia de 6 es razonable?", "No", "Es mayor que 3."),
            ex("¿Qué se hace para encontrar la diferencia?", "Se resta el menor al mayor", "Así sale la distancia entre ambos."),
        ],
        "apply": [
            ex("Hay 17 objetos. Opciones: 10, 16, 20. ¿Cuál es la más cercana?", "16", "17 − 16 = 1 es la menor diferencia."),
            ex("Hay 9 objetos. Opciones: 5, 8, 15. ¿Cuál es la más cercana?", "8", "9 − 8 = 1."),
            ex("Estimé 18 y había 15. ¿Fue razonable?", "Sí; 3 de diferencia", "18 − 15 = 3."),
        ],
        "reason": [
            ex("Ema estimó 20 para 11 objetos. ¿Fue razonable? ¿Qué falló?", "No; se pasó mucho del referente", "20 − 11 = 9."),
            ex("Hay 14 objetos y dos amigos estimaron 12 y 17. ¿Quién se acercó más?", "El que dijo 12", "14 − 12 = 2 y 17 − 14 = 3."),
        ],
        "challenge": [
            ex("Estimé 12 y la diferencia con el número real fue 3. ¿Qué dos números reales son posibles?", "9 o 15", "12 − 3 = 9 y 12 + 3 = 15."),
            ex("Hay 16. ¿Cuántas estimaciones razonables (diferencia 3 o menos) hay entre 13 y 19?", "7", "Son 13, 14, 15, 16, 17, 18 y 19."),
        ],
    },
    context=[ex("Se estimó que en una caja había 12 bolitas; Luis las contó y había 17. ¿Fue razonable la estimación?", "No; 5 de diferencia", "17 − 12 = 5, mayor que 3.")],
    selfcheck=[arith("Estimé 10 y había 11. ¿Diferencia?", "11-10", "11 − 10 = 1."), ex("¿Es razonable una diferencia de 3?", "Sí", "Es menor o igual que 3."), ex("¿Qué es la cantidad real?", "Lo que da al contar", "Es el conteo verdadero.")],
    open_task=task("Mira 14 puntos agrupados como 10 y 4 más. Escribe tres estimaciones posibles (por ejemplo 6, 13 y 20), calcula la diferencia de cada una con 14 y elige la más cercana.", "6 → 8 de diferencia; 13 → 1 de diferencia; 20 → 6 de diferencia. La más cercana es 13.", ["calcula las tres diferencias", "elige la menor", "explica con palabras"], ["tres restas", "elección"], ["restar al revés", "no justificar"], "Pide comprobar cada resta con la recta numérica."),
    reinforce="Estima y cuenta tres colecciones pequeñas; anota la diferencia.",
    extend="Descubre cuántas estimaciones razonables hay para una colección de 10.",
)

# ---------------------------------------------------------------- OA 06
register(
    OA6, 1,
    materials="Veinte fichas de dos colores (o su dibujo), vasos y diagramas de parte-parte-todo en este cuaderno.",
    use="Aprenderé que un número se puede formar con dos partes. Sirve para entender de qué está hecho un número y para sumar y restar después.",
    prior=["Sé contar hasta 20.", "Sé que sumar es juntar."],
    explain=[
        "Un todo se forma con dos partes. Si tengo 3 fichas rojas y 2 fichas azules, el todo es 5. Las partes son 3 y 2. El todo es lo que sale al juntar todas.",
        "Se escribe así: 3 + 2 = 5. El signo + dice que juntas las partes y el signo = dice que el resultado es el todo. También puedes dibujar un diagrama con un círculo grande (el todo) y dos círculos pequeños (las partes).",
        "Siempre puedes comprobar contando todo: cuentas las fichas rojas y las azules juntas y el resultado debe ser el todo. Si no coincide, revisa que no te falte ninguna.",
    ],
    vocab=[("parte", "una de las cantidades que forman el todo"), ("todo", "lo que resulta al juntar las partes"), ("sumar", "juntar partes"), ("diagrama", "dibujo que muestra las partes y el todo"), ("signo +", "dice que se juntan las partes")],
    worked=[
        {"title": "Dos partes forman un todo", "problem": "Hay 3 fichas rojas y 2 azules. ¿Cuál es el todo?", "steps": ["Las partes son 3 y 2.", "Junto las fichas: 3 y 2 más.", "Cuento todo: 5."], "answer": "3 + 2 = 5"},
        {"title": "Encontrar una parte", "problem": "El todo es 8 y una parte es 5. ¿Cuál es la otra parte?", "steps": ["Parto de 5 y agrego fichas hasta 8.", "Agrego 3.", "Compruebo: 5 + 3 = 8."], "answer": "3"},
    ],
    mistakes=[
        {"wrong": "Decir que el todo es una de las partes.", "why": "Se confunden todo y parte.", "fix": "El todo es el total cuando juntas las dos partes."},
        {"wrong": "Olvidar contar una ficha al juntar.", "why": "Se cuenta incompleto.", "fix": "Mueve las fichas a un solo montón mientras cuentas."},
    ],
    tiers={
        "recovery": [arith("Hay 2 fichas rojas y 4 azules. ¿Cuántas hay en total?", "2+4", "Dos partes forman el todo."), arith("Hay 5 fichas rojas y 1 azul. ¿Cuántas hay en total?", "5+1", "Se juntan las dos partes."), arith("Hay 3 fichas rojas y 3 azules. ¿Cuántas hay en total?", "3+3", "Dos partes iguales.")],
        "understand": [
            ex("En 4 + 3 = 7, ¿cuál es el todo?", "7", "El todo es el resultado."),
            ex("En 4 + 3 = 7, ¿cuáles son las partes?", "4 y 3", "Son los números que se juntan."),
            ex("¿Qué signo dice que juntas las partes?", "+", "El signo más junta."),
        ],
        "apply": [
            arith("El todo es 9 y una parte es 6. ¿Cuál es la otra parte?", "9-6", "Falta lo que hay que juntar para llegar a 9."),
            arith("El todo es 10 y una parte es 4. ¿Cuál es la otra parte?", "10-4", "10 − 4 = 6."),
            arith("Un jardín tiene 7 flores rojas y 5 amarillas. ¿Cuántas flores hay?", "7+5", "Se juntan las dos partes."),
        ],
        "reason": [
            ex("Ana dice que en 5 + 2 = 7 el todo es 5. ¿Tiene razón?", "No; el todo es 7", "El todo es el resultado de juntar."),
            ex("¿Puede el todo ser menor que una de sus partes?", "No", "El todo contiene a las partes."),
        ],
        "challenge": [
            ex("Tengo 12 fichas y las separo en dos partes iguales. ¿Cuántas fichas hay en cada parte?", "6", "6 + 6 = 12."),
            ex("Dibuja un diagrama con todo 6 y partes 2 y 4. ¿Cuánto es 2 + 4?", "6", "Las partes juntas forman 6."),
        ],
    },
    context=[arith("En una caja hay 6 lápices rojos y 8 azules. ¿Cuántos lápices hay en total?", "6+8", "Se juntan las dos partes para obtener el todo.")],
    selfcheck=[arith("Cuenta: 4 + 5.", "4+5", "Las partes forman el todo."), ex("En 3 + 6 = 9, ¿cuál es una parte?", "3 o 6", "Las partes son los sumandos."), arith("El todo es 7, una parte es 2. ¿Cuál es la otra?", "7-2", "A 2 le faltan 5 para llegar a 7.")],
    open_task=task("Con 8 fichas de dos colores, forma el 8 de tres maneras distintas (por ejemplo 5 y 3). Dibuja un diagrama de partes y todo para una de ellas.", "8 = 5 + 3, 8 = 6 + 2 y 8 = 4 + 4. Dibujé un círculo grande con 8 y dos pequeños con 5 y 3.", ["tres maneras distintas", "las tres suman 8", "diagrama correcto"], ["tres sumas", "diagrama"], ["sumas que no dan 8", "diagrama sin el todo"], "Pide comprobar cada suma contando fichas."),
    reinforce="Separa 10 fichas en dos montones de varias maneras.",
    extend="Descubre cuántas maneras hay de formar 6 con dos partes, contando 0 como parte y sin repetir el orden (1 + 5 y 5 + 1 cuentan como una).",
)

register(
    OA6, 2,
    materials="Fichas de dos colores, un vaso y la cinta de los números del 0 al 20 en este cuaderno.",
    use="Aprenderé que al separar un número en partes distintas el total no cambia. Sirve para calcular de varias maneras y comprobar.",
    prior=["Sé que dos partes forman un todo.", "Sé escribir sumas hasta 20."],
    explain=[
        "Un número se puede separar de muchas maneras sin perder nada. El 7 es 3 + 4, y también 5 + 2, y también 6 + 1. Las partes cambian, pero el todo siempre sigue siendo 7.",
        "Si una parte sube, la otra baja la misma cantidad. De 3 + 4 pasas a 4 + 3, o a 2 + 5: subes una y bajas la otra, y el total se conserva. Puedes mostrarlo moviendo fichas de un vaso a otro.",
        "Esto sirve para comprobar: si separas 9 en 4 y 5, y vuelves a juntarlas, deben dar 9. Si no da 9, se perdió o agregó una ficha.",
    ],
    vocab=[("conservar", "mantener igual"), ("separar", "partir un todo en partes más pequeñas"), ("total", "el todo"), ("pasar una ficha", "mover una ficha de una parte a otra"), ("otra manera", "otra pareja de partes con el mismo todo")],
    worked=[
        {"title": "Mover una ficha", "problem": "Tengo 3 + 4 = 7. Paso una ficha de la parte de 4 a la parte de 3. ¿Qué queda?", "steps": ["La parte de 3 sube a 4.", "La parte de 4 baja a 3.", "Ahora es 4 + 3.", "El total sigue siendo 7."], "answer": "4 + 3 = 7"},
        {"title": "Otra separación", "problem": "Separa el 9 de otra manera que 4 + 5.", "steps": ["Pruebo con 6 y 3.", "6 + 3 = 9.", "Compruebo juntando."], "answer": "6 + 3 = 9"},
    ],
    mistakes=[
        {"wrong": "Pasar una ficha y sumar una al total.", "why": "Se cree que mover agrega.", "fix": "Mover una ficha de una parte a otra no cambia el total."},
        {"wrong": "Separar 8 en 5 y 4.", "why": "Se pierde el control del total.", "fix": "Revisa: 5 + 4 = 9, no 8."},
    ],
    tiers={
        "recovery": [arith("¿Cuánto es 3 + 4?", "3+4", "Las partes forman 7."), arith("¿Cuánto es 5 + 2?", "5+2", "Otra manera de formar 7."), arith("¿Cuánto es 6 + 1?", "6+1", "Otra manera de formar 7.")],
        "understand": [
            ex("¿Cambia el total si paso una ficha de una parte a otra?", "No", "Sólo cambian las partes."),
            ex("¿Es verdad que 3 + 4 y 5 + 2 dan el mismo total?", "Sí; ambos dan 7", "Son otras partes del mismo 7."),
            ex("Si una parte sube 1, ¿qué pasa con la otra?", "Baja 1", "Para conservar el total."),
        ],
        "apply": [
            ex("Separa el 8 en 3 y en otro número.", "3 + 5", "3 + 5 = 8."),
            ex("Separa el 10 en 7 y en otro número.", "7 + 3", "7 + 3 = 10."),
            ex("Separa el 9 de otra manera que 4 + 5.", "6 + 3", "6 + 3 = 9."),
        ],
        "reason": [
            ex("Beto dice que 6 + 2 = 8 y 5 + 3 = 9 son otras maneras del 8. ¿Tiene razón?", "No; 5 + 3 = 8, no 9", "Una de las sumas está mal."),
            ex("¿Por qué 2 + 6 y 6 + 2 dan lo mismo?", "Son las mismas partes en otro orden", "El total no depende del orden."),
        ],
        "challenge": [
            ex("De 4 + 6 paso 2 fichas de la parte de 6 a la parte de 4. ¿Qué suma queda?", "6 + 4", "4 sube a 6 y 6 baja a 4."),
            ex("Separa el 12 en dos partes distintas y comprueba que suman 12.", "Por ejemplo 7 + 5", "7 + 5 = 12."),
        ],
    },
    context=[ex("Marta tiene 9 galletas en dos platos: 5 en uno y 4 en otro. Pasa una galleta del primer plato al segundo. ¿Cuántas galletas hay ahora en cada plato y en total?", "4 y 5; 9 en total", "El total no cambia al mover una galleta.")],
    selfcheck=[arith("¿Cuánto es 4 + 4?", "4+4", "Dos partes iguales."), ex("¿Qué se conserva al separar?", "El total", "Las partes cambian, el total no."), ex("Escribe otra manera del 6.", "Por ejemplo 2 + 4", "2 + 4 = 6.")],
    open_task=task("Con 9 fichas en dos vasos, muéveles fichas de a una y escribe cada nueva suma. Anota al menos cuatro sumas diferentes que den 9.", "8 + 1, 7 + 2, 6 + 3, 5 + 4. Moví una ficha de un vaso a otro cada vez y el total siguió siendo 9.", ["cuatro sumas distintas", "todas dan 9", "describe cómo las encontró"], ["lista de sumas", "descripción"], ["una suma que no da 9", "repetir sumas"], "Pide contar de nuevo las fichas para comprobar."),
    reinforce="Con 7 fichas y dos vasos, escribe cada separación que formas.",
    extend="Descubre cuántas separaciones distintas tiene el número 10.",
)

register(
    OA6, 3,
    materials="Diagramas de parte-parte-todo dibujados en cada ejercicio y lápiz.",
    use="Aprenderé a leer un diagrama de partes y todo y escribir la suma que lo describe. Sirve para traducir un dibujo a números.",
    prior=["Sé separar un número en partes.", "Sé escribir sumas."],
    explain=[
        "Un diagrama de parte-parte-todo tiene un círculo grande (el todo) y dos círculos pequeños (las partes). Si el todo es 9 y una parte es 4, la otra parte es 5. Se escribe 4 + 5 = 9.",
        "Para leer un diagrama, primero identifica qué número está en el círculo grande. Ése es el todo. Los otros dos son las partes. Si falta uno, se calcula con lo que falta para llegar al todo.",
        "Después escribe la suma: las partes se escriben antes del signo = y el todo después. Comprueba contando fichas o con los dedos.",
    ],
    vocab=[("diagrama", "dibujo con círculos para partes y todo"), ("círculo grande", "el todo"), ("círculo pequeño", "una parte"), ("expresión", "una suma escrita con números y signos"), ("traducir", "pasar de un dibujo a números")],
    worked=[
        {"title": "Leer un diagrama", "problem": "Diagrama: todo = 9, partes 4 y ?. ¿Qué número falta y cuál es la suma?", "steps": ["El todo es 9 y una parte es 4.", "A 4 le faltan 5 para llegar a 9: 4 + 5 = 9.", "Escribo 4 + 5 = 9."], "answer": "5; 4 + 5 = 9"},
        {"title": "Escribir la expresión", "problem": "Diagrama: partes 6 y 2, todo ?. Escribe la suma.", "steps": ["Las partes son 6 y 2.", "6 + 2 = 8.", "El todo es 8."], "answer": "6 + 2 = 8"},
    ],
    mistakes=[
        {"wrong": "Escribir 9 + 4 = 5.", "why": "Se suma el todo con una parte, pero el todo es el resultado de juntar.", "fix": "Se suman las partes y sale el todo: 4 + 5 = 9."},
        {"wrong": "No distinguir el círculo del todo.", "why": "Se confunden los círculos.", "fix": "El todo es el círculo grande o el que reúne a los demás."},
    ],
    tiers={
        "recovery": [ex("Diagrama: partes 2 y 3. ¿Cuál es el todo?", "5", "2 + 3 = 5."), ex("Diagrama: partes 4 y 4. ¿Cuál es el todo?", "8", "4 + 4 = 8."), ex("Diagrama: partes 6 y 1. ¿Cuál es el todo?", "7", "6 + 1 = 7.")],
        "understand": [
            ex("En un diagrama, ¿qué número va en el círculo grande?", "El todo", "El grande reúne las partes."),
            ex("En 5 + 3 = 8, ¿cuál es el todo?", "8", "Es el resultado."),
            ex("Diagrama: todo 10, partes 7 y ?. ¿Qué número falta?", "3", "7 y 3 forman 10."),
        ],
        "apply": [
            ex("Diagrama: todo 12, partes 5 y ?. Escribe la suma completa.", "5 + 7 = 12", "5 y 7 forman 12."),
            ex("Diagrama: todo 15, partes ? y 6. Escribe la suma completa.", "9 + 6 = 15", "9 y 6 forman 15."),
            ex("Diagrama: partes 8 y 8. Escribe la suma completa.", "8 + 8 = 16", "Las dos partes forman 16."),
        ],
        "reason": [
            ex("Rosa escribió 3 + 7 = 4 para un diagrama con todo 10. ¿Qué error cometió?", "Escribió mal el todo; es 10", "3 + 7 = 10."),
            ex("¿Pueden las dos partes ser iguales? Da un ejemplo.", "Sí; 5 + 5 = 10", "Las partes pueden ser iguales."),
        ],
        "challenge": [
            ex("Diagrama: todo 13, una parte es 5 más que la otra. ¿Cuáles son?", "4 y 9", "4 + 9 = 13 y 9 es 5 más que 4."),
            ex("Diagrama: todo 11. Escribe dos diagramas distintos.", "6 + 5 y 7 + 4", "Ambos suman 11."),
        ],
    },
    context=[ex("En un jardín hay 13 flores: 8 rojas y el resto blancas. Completa el diagrama y escribe la suma.", "8 + 5 = 13", "8 y 5 forman 13: hay 5 blancas.")],
    selfcheck=[ex("Diagrama: partes 5 y 4. ¿Todo?", "9", "5 + 4 = 9."), ex("Diagrama: todo 6, partes 2 y ?.", "4", "2 y 4 forman 6."), ex("¿Qué va antes del signo =: las partes o el todo?", "Las partes", "Las partes se suman y dan el todo.")],
    open_task=task("Dibuja un diagrama de parte-parte-todo con todo 14. Elige una parte (por ejemplo 9), calcula la otra y escribe la suma.", "Todo 14, partes 9 y 5. 9 + 5 = 14. Comprobé con los dedos: 9 y 5 más llegan a 14.", ["diagrama correcto", "calcula la parte que falta", "suma coherente"], ["dibujo", "suma"], ["poner el todo en una parte", "calcular mal la parte"], "Pide comprobar sumando las partes."),
    reinforce="Con 10 fichas, arma diagramas con tapas y escribe la suma.",
    extend="Dibuja un diagrama con 3 partes y todo 15 y escribe la suma de 3 sumandos.",
)

register(
    OA6, 4,
    materials="Fichas de dos colores, tabla en blanco y lápiz; el número de trabajo (8, 9 y 10) está escrito en cada ejercicio.",
    use="Aprenderé a encontrar todas las maneras de formar un número con dos partes. Sirve para no olvidar ninguna posibilidad.",
    prior=["Sé separar números en partes.", "Sé escribir sumas."],
    explain=[
        "Para encontrar todas las maneras de formar un número, trabaja con orden. Empieza con 0 en una parte y sube de a uno: 0 + 8, 1 + 7, 2 + 6, 3 + 5, 4 + 4. Luego se repiten al revés.",
        "El orden de las partes no cambia el total: 3 + 5 y 5 + 3 dan lo mismo. Así que a veces se cuentan como una sola manera. Si cuentas las dos, hay más parejas.",
        "Una tabla ayuda: en una columna la primera parte, en otra la segunda, y en la tercera el todo. Mira el patrón: cuando una parte sube, la otra baja y el total no cambia.",
    ],
    vocab=[("todas las maneras", "todas las parejas que forman el número"), ("patrón", "algo que se repite con una regla"), ("tabla", "cuadro con columnas"), ("orden", "ir de a uno sin saltarse"), ("pareja", "dos números que forman el total")],
    worked=[
        {"title": "Todas las maneras del 6", "problem": "Escribe todas las parejas que forman 6, sin repetir el orden.", "steps": ["Empiezo con 0: 0 + 6.", "Sigo 1 + 5, 2 + 4, 3 + 3.", "Después se repiten al revés.", "Son 4 parejas."], "answer": "0 + 6, 1 + 5, 2 + 4, 3 + 3"},
        {"title": "Ver el patrón", "problem": "En 1 + 7, 2 + 6, 3 + 5, ¿qué pasa?", "steps": ["La primera parte sube de 1 en 1.", "La segunda baja de 1 en 1.", "El total siempre es 8."], "answer": "Una sube y la otra baja; el total es 8"},
    ],
    mistakes=[
        {"wrong": "Olvidar la pareja con 0.", "why": "Se piensa que 0 no cuenta.", "fix": "0 + 6 también forma 6: una parte vacía."},
        {"wrong": "Repetir la misma pareja en otro orden y contarla dos veces.", "why": "No se acordó cómo contar.", "fix": "Define si 3 + 5 y 5 + 3 cuentan como una o como dos."},
    ],
    tiers={
        "recovery": [pairs_ex(4), pairs_ex(5), pairs_ex(6)],
        "understand": [
            ex("¿Cambia el total cuando una parte sube y la otra baja lo mismo?", "No", "El todo se conserva."),
            ex("¿Es 0 + 7 una manera de formar 7?", "Sí", "Una parte vacía y todo en la otra."),
            ex("¿Son 2 + 5 y 5 + 2 el mismo total?", "Sí, ambos dan 7", "El orden no cambia el total."),
        ],
        "apply": [pairs_ex(8), pairs_ex(9), pairs_ex(10)],
        "reason": [
            ex("Pía dice que 8 tiene 4 parejas distintas sin repetir el orden. Otra dice 5. ¿Cuál es correcta?", "5; 0 + 8, 1 + 7, 2 + 6, 3 + 5 y 4 + 4", "Hay que contar la pareja con 0 y la de partes iguales."),
            ex("¿Por qué una tabla ayuda a no olvidar parejas?", "Porque se ordena y se ve el patrón", "Se sube una parte y se baja la otra."),
        ],
        "challenge": [
            ex("¿Cuántas parejas tiene el 12 (sin repetir el orden)?", "7", "De 0 + 12 hasta 6 + 6."),
            ex("¿Cuántas parejas tiene el 11 (sin repetir el orden)?", "6", "De 0 + 11 hasta 5 + 6."),
        ],
    },
    context=[ex("Un panadero tiene 7 panes para guardar en dos bolsas. Escribe todas las maneras de repartirlos (sin repetir el orden).", "0 + 7, 1 + 6, 2 + 5, 3 + 4", "Son todas las parejas del 7.")],
    selfcheck=[ex("¿Cuántas parejas tiene el 4 (sin repetir)?", "3", "0 + 4, 1 + 3 y 2 + 2."), ex("¿Es 3 + 3 una manera de formar 6?", "Sí", "Dos partes iguales."), ex("Si la primera parte sube 1, ¿qué hace la segunda?", "Baja 1", "El total se conserva.")],
    open_task=task("Elige el 7 y escribe en una tabla todas las parejas que lo forman. Pinta de rojo la pareja de partes iguales si existe y explica por qué existe o no.", "0 + 7, 1 + 6, 2 + 5, 3 + 4. No existe pareja de partes iguales: 3 + 3 es 6 y 4 + 4 es 8, ninguna da 7.", ["lista completa", "usa orden", "explica la pareja de partes iguales"], ["tabla", "explicación"], ["olvidar una pareja", "repetir parejas"], "Pide comprobar sumando cada pareja."),
    reinforce="Con 6 fichas, encuentra todas las parejas moviendo de a una ficha.",
    extend="Descubre qué números tienen una pareja de partes iguales y cuáles no.",
)

# ---------------------------------------------------------------- OA 07
register(
    OA7, 1,
    materials="Recta numérica de 0 a 20 en el cuaderno y dedos; los cálculos están escritos en cada ejercicio.",
    use="Aprenderé a sumar contando desde el número mayor. Sirve para calcular rápido sin contar todo.",
    prior=["Sé contar hacia adelante hasta 20.", "Sé sumar números pequeños."],
    explain=[
        "Para sumar 5 + 2 no hace falta contar 1, 2, 3, 4, 5 y luego 6, 7. Basta con partir en el número mayor, 5, y contar dos más: 6, 7. El resultado es 7.",
        "Contar desde el mayor es más rápido porque cuentas menos números. En 3 + 8 conviene partir en 8 y contar tres más: 9, 10, 11. El orden de la suma no cambia el resultado: 3 + 8 = 8 + 3.",
        "Puedes ayudarte con los dedos para llevar la cuenta de cuántos agregaste, o con la recta numérica dando saltos. Siempre comprueba que contaste exactamente el segundo número.",
    ],
    vocab=[("contar desde el mayor", "partir en el número más grande y agregar el otro"), ("sumando", "cada número de una suma"), ("el mayor", "el número más grande de la suma"), ("saltos", "movimientos en la recta"), ("cálculo mental", "calcular sin escribir")],
    worked=[
        {"title": "Contar desde el mayor", "problem": "Calcula 5 + 2.", "steps": ["El mayor es 5.", "Parto en 5 y cuento dos más: 6, 7.", "Respuesta: 7."], "answer": "7"},
        {"title": "Cambiar el orden", "problem": "Calcula 3 + 8.", "steps": ["Es lo mismo que 8 + 3.", "Parto en 8 y cuento tres más: 9, 10, 11."], "answer": "11"},
    ],
    mistakes=[
        {"wrong": "Empezar en 5 y contar 5, 6.", "why": "Se cuenta el 5 de nuevo.", "fix": "Parte en 5 y di los números que siguen: 6, 7."},
        {"wrong": "Contar una cantidad distinta a la que se suma.", "why": "Se pierde la cuenta.", "fix": "Usa los dedos para contar exactamente cuántos agregaste."},
    ],
    tiers={
        "recovery": [arith("Calcula 4 + 1 partiendo desde 4.", "4+1", "Cuento un número más."), arith("Calcula 6 + 2 partiendo desde 6.", "6+2", "Cuento dos más: 7, 8."), arith("Calcula 7 + 3 partiendo desde 7.", "7+3", "Cuento tres más: 8, 9, 10.")],
        "understand": [
            ex("En 2 + 9, ¿desde qué número conviene partir?", "Desde 9", "Es el mayor."),
            ex("¿Cambia el resultado si cambio el orden: 3 + 8 y 8 + 3?", "No", "Ambos dan 11."),
            ex("¿Por qué conviene partir desde el mayor?", "Porque se cuentan menos números", "Es más rápido."),
        ],
        "apply": [arith("Calcula 2 + 9.", "2+9", "Parto en 9 y cuento 2 más."), arith("Calcula 3 + 12.", "3+12", "Parto en 12 y cuento 3 más."), arith("Calcula 1 + 14.", "1+14", "Parto en 14 y cuento 1 más.")],
        "reason": [
            ex("Carla calculó 4 + 3 contando 1, 2, 3, 4 y luego 5, 6, 7. ¿Cómo podría hacerlo más rápido?", "Partiendo en 4 y contando 3 más", "Así cuenta menos."),
            ex("Beto dice que 2 + 9 = 10. ¿Qué error pudo cometer?", "Contó sólo uno; es 11", "Debe contar dos más desde 9: 10, 11."),
        ],
        "challenge": [
            arith("Calcula 15 + 4.", "15+4", "Parto en 15 y cuento 4 más."),
            ex("Un número más 3 da 9. ¿Cuál es el número?", "6", "Cuento hacia atrás: 9, 8, 7, 6."),
        ],
    },
    context=[arith("En una caja hay 11 lápices y agrego 3 más. ¿Cuántos lápices hay?", "11+3", "Parto en 11 y cuento 3 más.")],
    selfcheck=[arith("Calcula 6 + 3.", "6+3", "Parto en 6 y cuento 3 más."), ex("¿Desde cuál número parto en 4 + 10?", "10", "Es el mayor."), arith("Calcula 2 + 8.", "2+8", "Parto en 8 y cuento 2 más.")],
    open_task=task("Calcula 4 + 9, 3 + 12 y 2 + 15 contando desde el mayor. Para cada una escribe desde dónde partiste y cuántos números contaste.", "4 + 9: parto en 9, cuento 4 más y llego a 13. 3 + 12: parto en 12, cuento 3 más y llego a 15. 2 + 15: parto en 15, cuento 2 más y llego a 17.", ["parte desde el mayor", "cuenta la cantidad correcta", "da el resultado"], ["tres cálculos", "explicación"], ["partir en el menor", "contar de más"], "Pide mostrar los saltos en la recta."),
    reinforce="Usa los dedos para contar 2, 3 y 4 más desde cualquier número.",
    extend="Descubre qué pasa si cuentas 0 más desde un número y explica por qué.",
)

register(
    OA7, 2,
    materials="Recta numérica de 0 a 20 en el cuaderno; los cálculos están escritos en cada ejercicio.",
    use="Aprenderé a restar contando hacia atrás. Sirve para saber cuántos quedan cuando quito objetos.",
    prior=["Sé contar hacia atrás.", "Sé que restar es quitar."],
    explain=[
        "Para restar puedes contar hacia atrás. En 9 − 3 partes en 9 y retrocedes tres lugares: 8, 7, 6. El resultado es 6. Cada vez que dices un número, quitas uno.",
        "Es útil cuando se quita poco. Por ahora practica con cantidades pequeñas, de 1 a 4. Puedes ayudarte con los dedos o con la recta numérica para no perder la cuenta de cuántos lugares retrocediste.",
        "Comprueba con una suma: 6 + 3 = 9, así que 9 − 3 = 6 está bien. La resta y la suma están relacionadas y una sirve para verificar la otra.",
    ],
    vocab=[("restar", "quitar una cantidad"), ("retroceder", "contar hacia atrás"), ("resultado", "lo que queda"), ("comprobar", "revisar con otra operación"), ("quitar", "sacar parte de una cantidad")],
    worked=[
        {"title": "Retroceder", "problem": "Calcula 9 − 3.", "steps": ["Parto en 9.", "Retrocedo tres lugares: 8, 7, 6.", "Comprueba: 6 + 3 = 9."], "answer": "6"},
        {"title": "Quitar objetos", "problem": "Había 12 galletas y se comieron 2. ¿Cuántas quedan?", "steps": ["Parto en 12.", "Retrocedo dos: 11, 10.", "Quedan 10."], "answer": "10"},
    ],
    mistakes=[
        {"wrong": "Decir 9, 8, 7 y responder 7 para 9 − 3.", "why": "Se cuenta el 9 como un retroceso.", "fix": "Parte en 9 y retrocede tres números: 8, 7, 6."},
        {"wrong": "Sumar en vez de restar.", "why": "Se confunde la operación.", "fix": "Restar es quitar: el resultado es menor."},
    ],
    tiers={
        "recovery": [ex("Tengo 8 caramelos y me como 1. ¿Cuántos quedan?", "7", "Retrocedo un lugar desde 8."), ex("Parto en 7 y retrocedo dos lugares. ¿A qué número llego?", "5", "Retrocedo: 6, 5."), arith("Calcula 10 − 3.", "10-3", "Retrocedo tres lugares: 9, 8, 7.")],
        "understand": [
            ex("En 9 − 3, ¿desde dónde parto?", "Desde 9", "El primer número de la resta."),
            ex("¿Hacia dónde cuento al restar?", "Hacia atrás", "Quito, así que retrocedo."),
            ex("¿Cómo compruebo 9 − 3 = 6?", "Sumando 6 + 3", "Debe dar 9."),
        ],
        "apply": [ex("En una fila hay 14 niños y se van 2. ¿Cuántos quedan?", "12", "Retrocedo dos lugares."), ex("Parto en 17 y retrocedo 3 lugares. ¿A qué número llego?", "14", "Retrocedo: 16, 15, 14."), ex("En una caja hay 20 lápices y se cae 1. ¿Cuántos quedan?", "19", "Retrocedo un lugar desde 20.")],
        "reason": [
            ex("Raúl calculó 10 − 2 = 12. ¿Qué error cometió?", "Sumó en vez de restar; es 8", "Restar hace que el número baje."),
            ex("¿Por qué la resta 9 − 3 se puede comprobar con 6 + 3?", "Porque quitar y juntar se deshacen", "Si agrego lo que quité, vuelvo al inicio."),
        ],
        "challenge": [
            ex("Hay 19 globos y se revientan 4. ¿Cuántos quedan?", "15", "Retrocedo: 18, 17, 16, 15."),
            ex("Resto 2 de un número y llego a 11. ¿De qué número partí?", "13", "11 + 2 = 13."),
        ],
    },
    context=[arith("En una bolsa hay 15 bolitas y se pierden 3. ¿Cuántas bolitas quedan?", "15-3", "Parto en 15 y retrocedo tres.")],
    selfcheck=[arith("Calcula 6 − 2.", "6-2", "Desde 6 retrocedo dos lugares."), ex("¿Hacia dónde se cuenta al restar?", "Hacia atrás", "Al restar se quita."), arith("Calcula 18 − 1.", "18-1", "Desde 18 retrocedo un lugar.")],
    open_task=task("Calcula 11 − 3, 16 − 2 y 20 − 4 contando hacia atrás. Escribe los números que dijiste y comprueba cada resta con una suma.", "11 − 3: 10, 9, 8, resultado 8 (8 + 3 = 11). 16 − 2: 15, 14, resultado 14 (14 + 2 = 16). 20 − 4: 19, 18, 17, 16, resultado 16 (16 + 4 = 20).", ["cuenta hacia atrás correctamente", "da el resultado", "comprueba con suma"], ["tres restas", "tres comprobaciones"], ["contar de más o de menos", "no comprobar"], "Pide recorrer la recta con el dedo y comprobar con la suma."),
    reinforce="Con 10 fichas, quita 1, 2 y 3 y cuenta hacia atrás.",
    extend="Descubre qué pasa si restas 0 y si restas el mismo número que tienes.",
)

register(
    OA7, 3,
    materials="Marco de diez dibujado en este cuaderno y fichas; los cálculos están escritos en cada ejercicio.",
    use="Aprenderé a completar diez para sumar más fácil. Sirve para calcular sumas como 8 + 5 pensando en el diez.",
    prior=["Sé qué pares de números forman 10.", "Sé usar el marco de diez."],
    explain=[
        "Completar diez es una estrategia: para sumar 8 + 5, primero completo el 10 con 2 que saco del 5. Queda 10 + 3 = 13. Así la suma es más fácil, porque sumar a 10 es sencillo.",
        "Los pasos son: 1) veo cuánto le falta al primer número para llegar a 10. 2) saco esa cantidad del segundo número. 3) sumo lo que queda al 10. Con 9 + 4: a 9 le falta 1, saco 1 del 4, queda 10 + 3 = 13.",
        "Esta estrategia funciona cuando uno de los números está cerca de 10. Con el marco de diez lo ves claro: llenas el marco y lo que sobra lo escribes aparte.",
    ],
    vocab=[("completar diez", "agregar lo que falta para llegar a 10"), ("lo que falta", "lo que necesito para llegar a 10"), ("sobra", "lo que queda al sacar lo que completó el diez"), ("marco de diez", "dos filas de cinco casillas"), ("estrategia", "una forma de calcular más fácil")],
    worked=[
        {"title": "8 + 5 con diez", "problem": "Calcula 8 + 5 completando diez.", "steps": ["A 8 le faltan 2 para 10.", "Saco 2 del 5: queda 3.", "10 + 3 = 13."], "answer": "13"},
        {"title": "9 + 4", "problem": "Calcula 9 + 4 completando diez.", "steps": ["A 9 le falta 1 para 10.", "Saco 1 del 4: quedan 3.", "10 + 3 = 13."], "answer": "13"},
    ],
    mistakes=[
        {"wrong": "Sacar 2 del 8 en vez de del 5.", "why": "Se saca del número equivocado.", "fix": "Lo que falta para el diez se saca del otro sumando."},
        {"wrong": "Olvidar lo que quedó del segundo número.", "why": "Se queda en 10.", "fix": "Después de llegar a 10, suma lo que sobró."},
    ],
    tiers={
        "recovery": [ex("¿Cuánto le falta a 7 para llegar a 10?", "3", "7 y 3 forman 10."), ex("¿Cuánto le falta a 9 para llegar a 10?", "1", "9 y 1 forman 10."), ex("¿Cuánto le falta a 6 para llegar a 10?", "4", "6 y 4 forman 10.")],
        "understand": [
            ex("En 8 + 5, ¿cuánto se saca del 5 para completar diez?", "2", "A 8 le faltan 2."),
            ex("En 8 + 5, ¿cuánto queda del 5 después de sacar 2?", "3", "5 − 2 = 3."),
            ex("¿Cuál es el resultado de 10 + 3?", "13", "Diez más tres."),
        ],
        "apply": [arith("Calcula 7 + 5 completando diez.", "7+5", "A 7 le faltan 3; queda 10 + 2."), arith("Calcula 9 + 6 completando diez.", "9+6", "A 9 le falta 1; queda 10 + 5."), arith("Calcula 6 + 8 completando diez.", "6+8", "A 6 le faltan 4; queda 10 + 4.")],
        "reason": [
            ex("Tomás dice que en 9 + 4 conviene sacar 4 del 9. ¿Está bien?", "No; se saca 1 del 4", "A 9 le falta 1 para llegar a 10."),
            ex("¿Por qué es más fácil sumar a 10?", "Porque 10 más un número se lee fácil, como 10 + 3 = 13", "Después del diez se dicen once, doce, trece…"),
        ],
        "challenge": [
            arith("Calcula 8 + 9.", "8+9", "A 8 le faltan 2; queda 10 + 7."),
            ex("Dos números suman 14 y uno es 8. ¿Cuál es el otro? Usa el diez.", "6", "8 + 2 = 10 y 10 + 4 = 14; el otro es 2 + 4 = 6."),
        ],
    },
    context=[arith("Un niño tiene 8 canicas y gana 7. ¿Cuántas tiene? Calcula completando diez.", "8+7", "A 8 le faltan 2; queda 10 + 5.")],
    selfcheck=[arith("Calcula 9 + 5.", "9+5", "A 9 le falta 1; queda 10 + 4."), ex("¿Cuánto le falta a 8 para 10?", "2", "8 y 2 forman 10."), arith("Calcula 7 + 6.", "7+6", "A 7 le faltan 3; queda 10 + 3.")],
    open_task=task("Calcula 8 + 6, 9 + 7 y 7 + 8 completando diez. Para cada suma escribe cuánto sacaste del segundo número y qué suma quedó.", "8 + 6: saco 2 del 6, queda 10 + 4 = 14. 9 + 7: saco 1 del 7, queda 10 + 6 = 16. 7 + 8: saco 3 del 8, queda 10 + 5 = 15.", ["completa diez", "indica lo que sacó", "da el resultado"], ["tres cálculos"], ["sacar del número equivocado", "olvidar lo que sobra"], "Pide dibujar los dos marcos de diez para cada suma."),
    reinforce="Con dos marcos de diez, llena uno y mira cuánto sobra en el otro.",
    extend="Descubre cómo completar diez cuando uno de los números es 10 u 11.",
)

register(
    OA7, 4,
    materials="Marco de diez y fichas de dos colores; los cálculos están escritos en cada ejercicio.",
    use="Aprenderé a usar los dobles y a elegir la estrategia que mejor sirve para cada cálculo. Sirve para calcular rápido y sin equivocarse.",
    prior=["Sé contar desde el mayor y completar diez.", "Sé sumar números pequeños."],
    explain=[
        "Un doble es sumar un número consigo mismo: 4 + 4 = 8, 6 + 6 = 12, 8 + 8 = 16. Conviene aprenderlos de memoria, porque ayudan a calcular otras sumas.",
        "Con un doble puedes calcular casi dobles: 6 + 7 es un doble más 1, porque 6 + 6 = 12 y 7 es uno más que 6. Entonces 6 + 7 = 13. También 8 + 7 es 8 + 8 menos 1: 16 − 1 = 15.",
        "Hay varias estrategias: contar desde el mayor, completar diez y usar dobles. Elige la que sea más fácil para los números dados: 9 + 8 se resuelve fácil con el diez; 6 + 7 con los dobles; 2 + 15 contando desde el mayor.",
    ],
    vocab=[("doble", "sumar un número consigo mismo"), ("casi doble", "suma de dos números seguidos, como 6 + 7"), ("estrategia", "forma de calcular más fácil"), ("elegir", "decidir cuál es la mejor"), ("verificar", "comprobar con otra forma")],
    worked=[
        {"title": "Usar un casi doble", "problem": "Calcula 6 + 7.", "steps": ["6 + 6 = 12 (doble de 6).", "7 es uno más que 6.", "12 + 1 = 13."], "answer": "13"},
        {"title": "Elegir estrategia", "problem": "Calcula 9 + 8 y explica qué estrategia usas.", "steps": ["Uno de los números es 9, cerca de 10.", "Completo diez: a 9 le falta 1, saco 1 del 8, queda 7.", "10 + 7 = 17."], "answer": "17, completando diez"},
    ],
    mistakes=[
        {"wrong": "Decir que 6 + 7 = 12.", "why": "Se queda en el doble.", "fix": "7 es uno más que 6, así que el resultado es uno más que 12."},
        {"wrong": "Usar siempre la misma estrategia aunque no sirva.", "why": "No se compara.", "fix": "Mira los números y elige la más fácil."},
    ],
    tiers={
        "recovery": [arith("Calcula 3 + 3.", "3+3", "Es un doble."), arith("Calcula 5 + 5.", "5+5", "Es un doble."), arith("Calcula 7 + 7.", "7+7", "Es un doble.")],
        "understand": [
            ex("¿Qué es un doble?", "Un número sumado consigo mismo", "Por ejemplo 4 + 4."),
            ex("¿Cómo se relaciona 6 + 7 con 6 + 6?", "Es uno más", "7 es uno más que 6."),
            ex("¿Qué estrategia conviene para 9 + 8?", "Completar diez", "9 está cerca de 10."),
        ],
        "apply": [arith("Calcula 8 + 9 usando el doble de 8.", "8+9", "8 + 8 = 16 y 9 es uno más."), arith("Calcula 7 + 8 usando el doble de 7.", "7+8", "7 + 7 = 14 y 8 es uno más."), arith("Calcula 9 + 9.", "9+9", "Es un doble.")],
        "reason": [
            ex("Rosa calculó 5 + 6 como 5 + 5 = 10 y luego 10 + 1 = 11. ¿Está bien?", "Sí", "6 es uno más que 5."),
            ex("¿Por qué 8 + 7 es uno menos que 8 + 8?", "Porque 7 es uno menos que 8", "El segundo número baja uno."),
        ],
        "challenge": [
            arith("Calcula 10 + 10.", "10+10", "Es el doble de 10."),
            ex("Dos números seguidos suman 15. ¿Cuáles son?", "7 y 8", "7 + 8 = 15."),
        ],
    },
    context=[arith("Un niño tiene 6 autitos rojos y 7 azules. ¿Cuántos autitos tiene? Usa un doble.", "6+7", "6 + 6 = 12 y uno más es 13.")],
    selfcheck=[arith("Calcula 4 + 4.", "4+4", "Es un doble."), arith("Calcula 5 + 6.", "5+6", "5 + 5 = 10 y uno más."), ex("Para 9 + 5, ¿qué estrategia usarías?", "Completar diez", "A 9 le falta 1.")],
    open_task=task("Calcula 7 + 8, 9 + 6 y 6 + 6. Para cada una escribe qué estrategia usaste (doble, casi doble, completar diez o contar desde el mayor) y por qué.", "7 + 8 = 15 con casi doble (7 + 7 + 1). 9 + 6 = 15 completando diez (9 + 1 + 5). 6 + 6 = 12 es un doble.", ["calcula bien", "nombra la estrategia", "justifica la elección"], ["tres cálculos", "justificación"], ["estrategia que no corresponde", "no justificar"], "Pide verificar con otra estrategia."),
    reinforce="Aprende de memoria los dobles de 1 a 10.",
    extend="Compara dos estrategias para el mismo cálculo y decide cuál es más rápida.",
)

# ---------------------------------------------------------------- OA 08
register(
    OA8, 1,
    materials="Hasta 20 fichas o palitos y bandas para agrupar de a diez, dibujadas en este cuaderno.",
    use="Aprenderé a formar una decena juntando diez objetos. Sirve para contar y escribir cantidades más grandes sin perderse.",
    prior=["Sé contar hasta 20.", "Sé qué es un grupo de diez."],
    explain=[
        "Una decena es un grupo de diez objetos. Si tienes diez palitos y los amarras con una banda, formaste una decena. Con una decena puedes contar más rápido: en vez de diez, ves un solo paquete.",
        "Para formar una decena, cuenta diez objetos y sepáralos en un grupo. Los que sobran son unidades sueltas. Con 13 palitos formas una decena y quedan 3 unidades.",
        "Puedes dibujar una decena como una barra ▮ y las unidades como puntos ●. Así 13 se dibuja ▮ ● ● ●. La barra vale diez y cada punto vale uno.",
    ],
    vocab=[("decena", "grupo de diez"), ("unidad", "un objeto suelto"), ("formar una decena", "juntar diez objetos en un grupo"), ("sobrar", "quedar sin agrupar"), ("barra", "dibujo que vale diez")],
    worked=[
        {"title": "Formar una decena", "problem": "Hay 13 palitos. ¿Cuántas decenas puedo formar y cuántos quedan sueltos?", "steps": ["Cuento diez palitos y los amarro.", "Quedan 3 sueltos.", "Formé 1 decena y 3 unidades."], "answer": "1 decena y 3 unidades"},
        {"title": "No alcanza una decena", "problem": "Hay 8 palitos. ¿Puedo formar una decena?", "steps": ["Una decena necesita 10.", "Tengo 8.", "No alcanza."], "answer": "No; hay 0 decenas y 8 unidades"},
    ],
    mistakes=[
        {"wrong": "Decir que 8 palitos forman una decena.", "why": "No se cuenta hasta diez.", "fix": "Una decena necesita diez."},
        {"wrong": "Contar la decena como 1 palito.", "why": "No se sabe que la decena es diez.", "fix": "Una decena vale diez."},
    ],
    tiers={
        "recovery": [ex("¿Cuántos objetos tiene una decena?", "10", "Una decena es diez."), ex("Tengo 10 palitos. ¿Cuántas decenas formo?", "1", "Diez palitos son una decena."), ex("Tengo 5 palitos. ¿Cuántas decenas formo?", "0", "No llegan a diez.")],
        "understand": [
            ex("¿Qué es una unidad?", "Un objeto suelto", "No está dentro de un grupo de diez."),
            ex("Con 12 palitos, ¿cuántos quedan sueltos después de formar una decena?", "2", "10 y 2 forman 12."),
            ex("¿Cuánto vale una barra ▮?", "10", "Es una decena."),
        ],
        "apply": [
            ex("Tengo 14 fichas. ¿Cuántas decenas y cuántas unidades hay?", "1 decena y 4 unidades", "10 y 4 sueltas."),
            ex("Tengo 17 fichas. ¿Cuántas decenas y cuántas unidades hay?", "1 decena y 7 unidades", "10 y 7 sueltas."),
            ex("Tengo 11 fichas. ¿Cuántas decenas y cuántas unidades hay?", "1 decena y 1 unidad", "10 y una suelta."),
        ],
        "reason": [
            ex("Ema dice que con 9 fichas se forma una decena. ¿Qué le falta?", "Una ficha", "Una decena necesita diez."),
            ex("¿Por qué conviene amarrar los palitos de a diez?", "Porque se cuenta más rápido", "Se cuentan paquetes y sueltos."),
        ],
        "challenge": [
            ex("Tengo 2 decenas completas. ¿Cuántos objetos son?", "20", "10 y 10."),
            ex("Con 15 palitos, ¿cuántos faltan para formar dos decenas?", "5", "15 y 5 forman 20."),
        ],
    },
    context=[ex("Una profesora tiene 16 lápices y los quiere guardar en cajas de 10. ¿Cuántas cajas llena y cuántos lápices quedan fuera?", "1 caja y 6 lápices", "10 en la caja y 6 sueltos.")],
    selfcheck=[ex("¿Cuántos palitos hay en dos decenas?", "20", "Una decena tiene diez objetos."), ex("Con 13 fichas, ¿cuántas decenas formo?", "1", "Diez fichas forman una."), ex("¿Cómo se dibuja una decena?", "Con una barra ▮", "La barra vale diez.")],
    open_task=task("Con 15 fichas o palitos (o dibújalos), forma una decena, dibuja el resultado con una barra y puntos y escribe cuántas decenas y unidades hay.", "Formé una decena con 10 fichas y quedaron 5 sueltas. Dibujé ▮ ● ● ● ● ●. Hay 1 decena y 5 unidades.", ["forma una decena", "dibuja barra y puntos", "escribe decenas y unidades"], ["dibujo", "frase"], ["agrupar menos de diez", "no contar las sueltas"], "Pide contar la barra como diez y los puntos como uno."),
    reinforce="Amarra de a diez 10, 20 y 30 palitos (si hay) y cuenta.",
    extend="Descubre cuántas decenas se pueden formar con 20 palitos.",
)

register(
    OA8, 2,
    materials="Fichas, barras y puntos dibujados en cada ejercicio; lápiz.",
    use="Aprenderé a describir un número como una decena y unidades sueltas. Sirve para entender de qué está hecho un número del 11 al 19.",
    prior=["Sé formar una decena.", "Sé contar hasta 20."],
    explain=[
        "Todos los números entre 11 y 19 tienen una decena y algunas unidades. 14 es una decena y 4 unidades. Se lee «catorce». En el numeral 14, la cifra de la izquierda es la decena y la de la derecha son las unidades.",
        "Si miras 17, el 1 es una decena y el 7 son siete unidades. Si lo dibujas, es una barra y siete puntos: ▮ ● ● ● ● ● ● ●. Puedes comprobar que 10 más 7 son 17.",
        "Para no equivocarte, siempre pregunta: ¿cuántas decenas? ¿Cuántas unidades? Y comprueba sumando: 10 + 4 = 14.",
    ],
    vocab=[("decena", "grupo de diez"), ("unidades sueltas", "objetos que no completan otra decena"), ("cifra", "cada número que forma un numeral"), ("lugar de las decenas", "la cifra de la izquierda"), ("lugar de las unidades", "la cifra de la derecha")],
    worked=[
        {"title": "Descomponer 14", "problem": "¿Cuántas decenas y unidades tiene el 14?", "steps": ["El 1 de la izquierda es una decena.", "El 4 de la derecha son 4 unidades.", "Compruebo: 10 + 4 = 14."], "answer": "1 decena y 4 unidades"},
        {"title": "De decenas y unidades al numeral", "problem": "Una decena y 8 unidades. ¿Qué numeral es?", "steps": ["Decena: 10.", "Unidades: 8.", "10 + 8 = 18."], "answer": "18"},
    ],
    mistakes=[
        {"wrong": "Escribir 41 para una decena y cuatro unidades.", "why": "Se invierten las cifras.", "fix": "La decena va a la izquierda: 14."},
        {"wrong": "Decir que 14 tiene 14 decenas.", "why": "Se confunde la cifra con el grupo.", "fix": "14 tiene una decena y cuatro unidades."},
    ],
    tiers={
        "recovery": [ex("Una decena y 2 unidades, ¿qué numeral es?", "12", "10 + 2 = 12."), ex("Una decena y 6 unidades, ¿qué numeral es?", "16", "10 + 6 = 16."), ex("Una decena y 9 unidades, ¿qué numeral es?", "19", "10 + 9 = 19.")],
        "understand": [
            ex("En 15, ¿qué cifra es la decena?", "1", "La de la izquierda."),
            ex("En 15, ¿cuántas unidades hay?", "5", "La de la derecha."),
            ex("¿Cuántas decenas tiene 17?", "1", "Una decena y siete unidades."),
        ],
        "apply": [
            ex("Descompón 13 en decenas y unidades.", "1 decena y 3 unidades", "10 + 3 = 13."),
            ex("Descompón 18 en decenas y unidades.", "1 decena y 8 unidades", "10 + 8 = 18."),
            ex("Descompón 11 en decenas y unidades.", "1 decena y 1 unidad", "10 + 1 = 11."),
        ],
        "reason": [
            ex("Pedro dice que 12 es 2 decenas y 1 unidad. ¿Qué error comete?", "Invirtió las cifras; es 1 decena y 2 unidades", "La decena va a la izquierda."),
            ex("¿Por qué todos los números del 11 al 19 tienen una sola decena?", "Porque 20 ya son dos decenas", "Entre 10 y 19 no se llegan a dos grupos."),
        ],
        "challenge": [
            ex("Un número tiene una decena y su cifra de unidades es el doble de 3. ¿Cuál es?", "16", "El doble de 3 es 6."),
            ex("Si a 14 le agrego 6 unidades, ¿cuántas decenas hay?", "2", "14 + 6 = 20."),
        ],
    },
    context=[ex("Una caja tiene 10 chocolates y hay 7 más afuera. ¿Cuántos chocolates hay y cómo se descompone el número?", "17; 1 decena y 7 unidades", "10 + 7 = 17.")],
    selfcheck=[ex("Descompón 16.", "1 decena y 6 unidades", "10 + 6 = 16."), ex("Una decena y 3 unidades, ¿qué numeral?", "13", "10 + 3 = 13."), ex("¿Qué cifra es la decena en 19?", "1", "La de la izquierda.")],
    open_task=task("Elige 12, 15 o 18. Dibújalo con una barra y puntos, escribe cuántas decenas y unidades tiene y comprueba con una suma.", "Elegí 15: ▮ ● ● ● ● ●. Tiene 1 decena y 5 unidades. Comprobación: 10 + 5 = 15.", ["dibujo correcto", "decenas y unidades", "comprobación con suma"], ["dibujo", "frase", "suma"], ["invertir cifras", "no comprobar"], "Pide leer el número en voz alta y señalar la barra y los puntos."),
    reinforce="Dibuja con barra y puntos los números 11 a 15.",
    extend="Descubre qué pasa con las unidades cuando sumas 1 a 19.",
)

register(
    OA8, 3,
    materials="Tabla de decenas (D) y unidades (U) dibujada en este cuaderno; barras y puntos en cada ejercicio.",
    use="Aprenderé a leer una tabla de decenas y unidades y a dibujar un número con barras y puntos. Sirve para escribir números con orden.",
    prior=["Sé descomponer números del 11 al 19.", "Sé dibujar con barras y puntos."],
    explain=[
        "Una tabla D U tiene dos columnas: D para decenas y U para unidades. En 14 escribes 1 en D y 4 en U. La tabla ordena las cifras y muestra lo que vale cada una.",
        "Para dibujar un número, mira la tabla: tantas barras como dice D y tantos puntos como dice U. Con D = 1 y U = 6 dibujas una barra y seis puntos: ▮ ● ● ● ● ● ●, que es 16.",
        "Para leer un dibujo, cuenta las barras (cada una vale diez) y los puntos (cada uno vale uno), y escribe el número. Verifica que la tabla y el dibujo digan lo mismo.",
    ],
    vocab=[("tabla D U", "tabla de decenas y unidades"), ("D", "columna de las decenas"), ("U", "columna de las unidades"), ("barra", "vale diez"), ("punto", "vale uno")],
    worked=[
        {"title": "De la tabla al dibujo", "problem": "D = 1, U = 6. Dibuja y escribe el número.", "steps": ["Una barra: ▮.", "Seis puntos: ● ● ● ● ● ●.", "Número: 16."], "answer": "▮ ● ● ● ● ● ●; 16"},
        {"title": "Del dibujo a la tabla", "problem": "Dibujo: ▮ ● ● ●. Completa la tabla.", "steps": ["Una barra: D = 1.", "Tres puntos: U = 3.", "El número es 13."], "answer": "D = 1, U = 3; 13"},
    ],
    mistakes=[
        {"wrong": "Poner los puntos en la columna D.", "why": "Se mezclan las columnas.", "fix": "Los puntos van en U; las barras, en D."},
        {"wrong": "Contar la barra como uno.", "why": "No se recuerda que vale diez.", "fix": "Cada barra vale diez."},
    ],
    tiers={
        "recovery": [ex("D = 1, U = 2. ¿Qué número es?", "12", "10 + 2."), ex("D = 1, U = 5. ¿Qué número es?", "15", "10 + 5."), ex("D = 1, U = 0. ¿Qué número es?", "10", "10 + 0.")],
        "understand": [
            ex("¿En qué columna va el número de barras?", "En D", "D es de decenas."),
            ex("¿En qué columna va el número de puntos?", "En U", "U es de unidades."),
            ex("Dibujo: ▮ ● ● ● ● ● ● ●. ¿Qué número es?", "17", "Una barra y siete puntos."),
        ],
        "apply": [
            ex("Dibuja 14 y completa la tabla D U.", "▮ ● ● ● ●; D = 1, U = 4", "Una barra y cuatro puntos."),
            ex("Dibuja 19 y completa la tabla D U.", "▮ ● ● ● ● ● ● ● ● ●; D = 1, U = 9", "Una barra y nueve puntos."),
            ex("Dibuja 11 y completa la tabla D U.", "▮ ●; D = 1, U = 1", "Una barra y un punto."),
        ],
        "reason": [
            ex("Beto puso D = 4, U = 1 para 14. ¿Qué error cometió?", "Invirtió las columnas; es D = 1, U = 4", "La decena se escribe en D."),
            ex("Si la tabla dice D = 1 y U = 0, ¿cuántos puntos dibujas?", "Ninguno", "Sólo hay una barra, es el 10."),
        ],
        "challenge": [
            ex("Un número tiene D = 1 y U = 9. Si le agrego 1, ¿cuál es la nueva tabla?", "D = 2, U = 0", "19 + 1 = 20."),
            ex("Dibuja un número del 11 al 19 que tenga más unidades que 5.", "Por ejemplo 17", "Una barra y siete puntos."),
        ],
    },
    context=[ex("Una caja tiene una barra de 10 clips y 8 clips sueltos. Completa la tabla D U y escribe el número.", "D = 1, U = 8; 18", "10 + 8 = 18.")],
    selfcheck=[ex("D = 1, U = 7. ¿Qué número es?", "17", "10 + 7."), ex("Dibujo ▮ ● ●. ¿Qué número?", "12", "Una barra y dos puntos."), ex("¿Cuánto vale la barra?", "10", "Es una decena.")],
    open_task=task("Elige 13, 16 o 19. Completa la tabla D U, haz el dibujo con barras y puntos y escribe una frase que diga qué significa cada cifra.", "Elegí 16. D = 1, U = 6. Dibujo: ▮ ● ● ● ● ● ●. El 1 es una decena y el 6 son seis unidades.", ["tabla correcta", "dibujo correcto", "frase con las dos cifras"], ["tabla", "dibujo", "frase"], ["mezclar columnas", "dibujar de más"], "Pide leer la tabla y el dibujo de forma que digan lo mismo."),
    reinforce="Completa tablas D U para los números 11 a 19.",
    extend="Explica cómo cambia la tabla D U cuando pasas de 19 a 20.",
)

register(
    OA8, 4,
    materials="Dos filas de diez y números del 15 al 20 en los ejercicios; tabla D U; barras y puntos.",
    use="Aprenderé qué es el 20 como dos decenas y a comparar números del 15 al 20 por sus decenas y unidades. Sirve para ordenar cantidades hasta 20.",
    prior=["Sé la tabla D U.", "Sé comparar números."],
    explain=[
        "El 20 son dos decenas y ninguna unidad: D = 2 y U = 0. Se dibuja con dos barras: ▮ ▮. Es el primer número que tiene dos decenas.",
        "Para comparar números del 15 al 20, mira primero las decenas. Los del 15 al 19 tienen una decena; el 20 tiene dos, así que el 20 es mayor. Si tienen la misma cantidad de decenas, compara las unidades: 17 > 15 porque 7 > 5.",
        "En una recta numérica, el 20 está al final. Puedes usar las tablas D U para comparar: lee primero D, luego U. Así sabes cuál es mayor sin contar.",
    ],
    vocab=[("veinte", "dos decenas"), ("comparar", "decidir cuál es mayor"), ("misma decena", "tienen la misma cifra a la izquierda"), ("unidades", "la cifra de la derecha"), ("mayor", "el que tiene más")],
    worked=[
        {"title": "El 20", "problem": "Escribe 20 en una tabla D U y dibújalo.", "steps": ["D = 2 porque son dos decenas.", "U = 0 porque no hay sueltas.", "Dibujo: ▮ ▮."], "answer": "D = 2, U = 0; ▮ ▮"},
        {"title": "Comparar", "problem": "Compara 17 y 15.", "steps": ["Los dos tienen una decena.", "Comparo las unidades: 7 y 5.", "7 > 5, entonces 17 > 15."], "answer": "17 > 15"},
    ],
    mistakes=[
        {"wrong": "Decir que 19 > 20 porque 9 es una cifra grande.", "why": "Se miran las unidades primero.", "fix": "Compara primero las decenas: 20 tiene dos."},
        {"wrong": "Dibujar el 20 con una sola barra.", "why": "No se reconoce que son dos decenas.", "fix": "Veinte son dos decenas."},
    ],
    tiers={
        "recovery": [ex("¿Cuántas decenas tiene el 20?", "2", "Veinte son dos decenas."), ex("¿Cuántas unidades tiene el 20?", "0", "No hay unidades sueltas."), ex("¿Cuántas barras se dibujan para 20?", "2", "Una por cada decena.")],
        "understand": [
            ex("¿Cuál es mayor: 19 o 20?", "20", "Tiene dos decenas."),
            ex("Si dos números tienen la misma decena, ¿qué comparo?", "Las unidades", "La siguiente cifra."),
            ex("¿Cuál es el primer número con dos decenas?", "20", "Después de 19."),
        ],
        "apply": [cmp_ex(16, 18, "Misma decena; 6 es menor que 8."), cmp_ex(19, 20, "20 tiene dos decenas."), cmp_ex(15, 15, "Son el mismo número.")],
        "reason": [
            ex("Ana dice que 19 > 20 porque 9 > 0. ¿Qué error cometió?", "Comparó las unidades primero; 20 es mayor", "Se compara primero la decena."),
            ex("¿Por qué 20 no tiene punto en la tabla D U?", "Porque no hay unidades sueltas", "U = 0."),
        ],
        "challenge": [
            ex("Ordena de menor a mayor: 20, 15, 18, 12.", "12, 15, 18, 20", "Una decena y luego 20."),
            ex("¿Cuántos números hay entre 15 y 20 (sin contar esos)?", "4", "16, 17, 18 y 19."),
        ],
    },
    context=[ex("Una profesora tiene 2 cajas de 10 lápices. ¿Cuántos lápices tiene y cómo se escribe en la tabla D U?", "20 lápices; D = 2, U = 0", "Son dos decenas completas.")],
    selfcheck=[cmp_ex(14, 20, "20 tiene dos decenas."), ex("¿Cuántas decenas tiene 18?", "1", "Una decena y ocho unidades."), ex("¿Cómo se escribe veinte en la tabla D U?", "D = 2, U = 0", "Son dos decenas completas.")],
    open_task=task("Compara 16, 19 y 20. Escribe los tres en tablas D U, ordénalos de menor a mayor y explica por qué el 20 es el mayor.", "16 (D = 1, U = 6), 19 (D = 1, U = 9), 20 (D = 2, U = 0). Orden: 16, 19, 20. El 20 es el mayor porque tiene dos decenas y los otros una.", ["tablas correctas", "orden correcto", "explica con decenas"], ["tablas", "lista", "explicación"], ["mirar las unidades primero", "tablas con columnas invertidas"], "Pide comparar primero D y luego U."),
    reinforce="Haz tarjetas del 15 al 20 y ordénalas en la recta.",
    extend="Explica cómo se ve el 20 en la tabla D U y por qué U es 0.",
)
