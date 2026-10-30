"""Student material for 1.º básico Matemática, OA 09 (problemas), OA 10 (operaciones inversas) y OA 11 (patrones)."""
from __future__ import annotations

from student_content_ma01_a import dots
from student_content_ma01_b import task
from student_content_ma02_a import fill
from student_lessons import arith, ex, register

OA9, OA10, OA11 = "MA01 OA 09", "MA01 OA 10", "MA01 OA 11"


def pat(unit: str, count: int, blank_from: int | None = None) -> str:
    """Repeating pattern as text; items from `blank_from` on become __."""
    items = [unit[i % len(unit)] for i in range(count)]
    if blank_from is not None:
        items = items[:blank_from] + ["__"] * (count - blank_from)
    return " ".join(items)


def next_items(unit: str, shown: int, count: int) -> str:
    return " ".join(unit[(shown + i) % len(unit)] for i in range(count))


# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Hasta 5 fichas o tapas por problema; los datos de cada problema están escritos en este cuaderno.",
    use="Aprenderé a resolver problemas en que se agregan o se reúnen cosas, con números hasta 5. Sirve para saber cuántas hay después de juntar.",
    prior=["Sé contar hasta 5.", "Sé qué significa agregar."],
    explain=[
        "Un problema de agregar cuenta una historia: había algunas cosas y llegan más. Para resolverlo, primero identifica cuántas había, luego cuántas llegan y por último junta todo. Si hay 2 pájaros en una rama y llegan 3, ahora hay 5.",
        "También hay problemas de reunir: dos grupos distintos se juntan, como 2 niñas y 1 niño. Se escribe 2 + 1 = 3. Para resolver, puedes representar con fichas, dibujar o contar con los dedos.",
        "Siempre termina con una respuesta completa: «Ahora hay 5 pájaros». Así compruebas que respondes lo que preguntan, no sólo el número.",
    ],
    vocab=[("agregar", "poner más a lo que ya hay"), ("reunir", "juntar dos grupos"), ("sumar", "juntar cantidades"), ("total", "cuántos hay al final"), ("problema", "historia con una pregunta")],
    worked=[
        {"title": "Agregar", "problem": "En una rama hay 2 pájaros. Llegan 3 más. ¿Cuántos pájaros hay ahora?", "steps": ["Había 2.", "Llegan 3 más.", "Junto: 2 + 3 = 5."], "answer": "Hay 5 pájaros"},
        {"title": "Reunir", "problem": "Hay 2 niñas y 1 niño en una mesa. ¿Cuántas personas hay en total?", "steps": ["Grupo 1: 2 niñas.", "Grupo 2: 1 niño.", "2 + 1 = 3."], "answer": "Hay 3 personas"},
    ],
    mistakes=[
        {"wrong": "Responder sólo con la cantidad que llega.", "why": "No se junta con lo que ya había.", "fix": "Suma lo que había y lo que llega."},
        {"wrong": "Restar en un problema de agregar.", "why": "Se confunde la operación.", "fix": "Agregar o reunir se suma."},
    ],
    tiers={
        "recovery": [arith("Hay 1 gato en el patio y llega 1 más. ¿Cuántos gatos hay?", "1+1", "Llega uno y se junta."), arith("Hay 2 globos y agrego 2 globos. ¿Cuántos globos hay?", "2+2", "Se juntan los dos grupos."), arith("Hay 3 lápices y llega 1 lápiz. ¿Cuántos lápices hay?", "3+1", "Se agrega uno.")],
        "understand": [
            ex("En «hay 2 pájaros y llegan 3», ¿cuántos pájaros había al principio?", "2", "Es la cantidad inicial."),
            ex("En «hay 2 pájaros y llegan 3», ¿cuántos llegaron?", "3", "Es lo que se agrega."),
            ex("¿Qué operación resuelve un problema donde llegan más?", "Una suma", "Se juntan las cantidades."),
        ],
        "apply": [
            arith("En una mesa hay 4 vasos. Pongo 1 vaso más. ¿Cuántos vasos hay?", "4+1", "Se agrega un vaso."),
            arith("Tomás tiene 3 autitos y su amigo le regala 2. ¿Cuántos autitos tiene?", "3+2", "Se juntan los autitos."),
            arith("En una bandeja hay 2 galletas y en otra 3. ¿Cuántas galletas hay en total?", "2+3", "Se reúnen las dos bandejas."),
        ],
        "reason": [
            ex("Lucía dice que 3 + 2 es 1 porque «sobra uno». ¿Qué error comete?", "Resta en vez de sumar; son 5", "Agregar se resuelve sumando."),
            ex("Si llegan 0 pájaros a una rama con 4, ¿cuántos hay?", "4", "Agregar cero no cambia la cantidad."),
        ],
        "challenge": [
            ex("Hay 5 fichas. Algunas son rojas y las otras azules. Si hay 2 rojas, ¿cuántas son azules?", "3", "2 + 3 = 5."),
            ex("Dibuja una historia para 3 + 2 = 5.", "Por ejemplo: 3 flores y 2 más hacen 5", "La historia debe agregar 2 a 3."),
        ],
    },
    context=[arith("En el recreo, 3 niños juegan y llegan 2 más. ¿Cuántos niños juegan ahora?", "3+2", "Los que juegan y los que llegan se juntan.")],
    selfcheck=[arith("Si tengo 1 ficha y recibo 4, ¿cuántas tengo?", "1+4", "Se agregan cuatro."), ex("¿Se suma o se resta cuando llegan más?", "Se suma", "Hay más cantidad."), arith("Hay 2 y 2. ¿Cuántos son?", "2+2", "Dos grupos de dos.")],
    open_task=task("Observa esta historia: hay 3 ovejas y llegan 2 más. Haz un dibujo, escribe la suma y responde con una frase completa.", f"Dibujé {dots(3)} y {dots(2)}. 3 + 2 = 5. Ahora hay 5 ovejas.", ["dibuja la historia", "escribe la suma", "responde con frase completa"], ["dibujo", "suma", "frase"], ["restar", "responder sin frase"], "Pide leer el problema y comprobar que la frase responde la pregunta."),
    reinforce="Con 5 fichas, representa y resuelve tres historias de agregar.",
    extend="Cambia la historia para que llegue una cantidad distinta y escribe la nueva suma.",
)

register(
    OA9, 2,
    materials="Hasta 10 fichas por problema; los datos de cada problema están escritos en este cuaderno.",
    use="Aprenderé a resolver problemas en que se quitan o se separan cosas, con números hasta 10. Sirve para saber cuántas quedan.",
    prior=["Sé sumar hasta 5.", "Sé contar hacia atrás."],
    explain=[
        "En un problema de quitar, había algo y se va una parte. Si había 8 galletas y se comen 3, quedan 5. Se escribe 8 − 3 = 5. Lo que queda es el resultado de la resta.",
        "También hay problemas de separar: un grupo se divide en dos partes. Si hay 9 niños y 4 son niñas, los otros 5 son niños. Para resolver, representa con fichas, quita las que dice y cuenta las que quedan.",
        "Para comprobar, suma lo que quitaste y lo que quedó: 3 + 5 = 8. Debe dar lo que había al comienzo.",
    ],
    vocab=[("quitar", "sacar una parte"), ("separar", "dividir un grupo en dos partes"), ("restar", "quitar una cantidad"), ("quedan", "lo que sobra después de quitar"), ("comprobar", "revisar con una suma")],
    worked=[
        {"title": "Quitar", "problem": "Había 8 galletas y se comen 3. ¿Cuántas quedan?", "steps": ["Parto de 8.", "Quito 3.", "8 − 3 = 5.", "Compruebo: 3 + 5 = 8."], "answer": "Quedan 5 galletas"},
        {"title": "Separar", "problem": "Hay 9 niños. 4 son niñas. ¿Cuántos son niños?", "steps": ["Total 9.", "Quito las 4 niñas.", "9 − 4 = 5."], "answer": "Son 5 niños"},
    ],
    mistakes=[
        {"wrong": "Sumar los dos números del problema.", "why": "Se confunde juntar con quitar.", "fix": "Si algo se va, resta."},
        {"wrong": "No comprobar el resultado.", "why": "Se confía en el primer cálculo.", "fix": "Suma lo que quitaste y lo que quedó."},
    ],
    tiers={
        "recovery": [arith("Hay 6 manzanas y me como 1. ¿Cuántas quedan?", "6-1", "Se quita una."), arith("Hay 7 globos y se revientan 2. ¿Cuántos quedan?", "7-2", "Se quitan dos."), arith("Hay 10 lápices y regalo 4. ¿Cuántos quedan?", "10-4", "Se quitan cuatro.")],
        "understand": [
            ex("En «había 8 y se comen 3», ¿cuántas había al principio?", "8", "Es la cantidad inicial."),
            ex("¿Qué operación resuelve un problema donde se quita?", "Una resta", "Se saca una parte."),
            ex("¿Cómo compruebas 8 − 3 = 5?", "Con 3 + 5 = 8", "Lo que quité más lo que quedó es lo que había."),
        ],
        "apply": [
            arith("En un jardín hay 9 flores y se cortan 3. ¿Cuántas quedan?", "9-3", "Se cortan tres."),
            arith("Matías tiene 10 canicas y pierde 6. ¿Cuántas le quedan?", "10-6", "Se pierden seis."),
            arith("En una fila hay 7 niños. 2 se sientan. ¿Cuántos siguen de pie?", "7-2", "Se separan los que se sientan."),
        ],
        "reason": [
            ex("Ema dice que 8 − 3 = 11. ¿Qué error comete?", "Suma en vez de restar; es 5", "Quitar hace que haya menos."),
            ex("Si quito 0 de un grupo de 6, ¿cuántos quedan?", "6", "Quitar cero no cambia."),
        ],
        "challenge": [
            ex("Había 10 fichas, se quitaron algunas y quedan 4. ¿Cuántas se quitaron?", "6", "10 − 6 = 4."),
            ex("Inventa una historia para 7 − 2 = 5.", "Por ejemplo: había 7 pelotas y se perdieron 2", "Hay que quitar 2 de 7."),
        ],
    },
    context=[arith("En una caja hay 10 crayones y 3 se rompen. ¿Cuántos crayones sirven aún?", "10-3", "Se quitan los rotos.")],
    selfcheck=[arith("Hay 8 y se quitan 2. ¿Cuántos quedan?", "8-2", "Se quitan dos."), ex("¿Se suma o se resta cuando se va algo?", "Se resta", "Hay menos cantidad."), arith("Hay 5 y quito 5. ¿Cuántos quedan?", "5-5", "Se quita todo.")],
    open_task=task("Observa esta historia: hay 9 globos y se escapan 4. Dibuja, tacha los que se escapan, escribe la resta y responde con una frase.", f"Dibujé {dots(9)} y taché 4. 9 − 4 = 5. Quedan 5 globos.", ["dibuja y tacha", "escribe la resta", "responde con frase"], ["dibujo", "resta", "frase"], ["sumar", "no tachar la cantidad correcta"], "Pide comprobar con la suma 4 + 5 = 9."),
    reinforce="Con 10 fichas, representa y resuelve tres historias de quitar.",
    extend="Cambia la historia para que se vayan más globos y escribe la nueva resta.",
)

register(
    OA9, 3,
    materials="Dibujos con puntos y marcos de diez en cada problema; recta numérica de 0 a 20 en este cuaderno.",
    use="Aprenderé a sumar hasta 20 usando dibujos, marcos de diez y la recta numérica. Sirve para resolver problemas con números más grandes.",
    prior=["Sé sumar y restar hasta 10.", "Sé completar diez."],
    explain=[
        "Para sumar hasta 20 puedes usar representaciones. Con el marco de diez llenas uno y lo que sobra va al segundo. En 8 + 6, llenas el primer marco con 8 y 2 del 6; en el segundo quedan 4. El total es 14.",
        "En la recta numérica parte en el primer sumando y salta el segundo. Para 12 + 5, parte en 12 y da cinco saltos: 13, 14, 15, 16, 17. Llegas a 17.",
        "Cualquiera de las dos representaciones sirve; elige la que te resulte más clara. Comprueba que el total sea mayor que cada sumando.",
    ],
    vocab=[("representación", "dibujo o material que muestra el problema"), ("marco de diez", "dos filas de cinco"), ("salto", "movimiento en la recta"), ("sumando", "cada número que se suma"), ("total", "resultado de la suma")],
    worked=[
        {"title": "Con el marco de diez", "problem": "Hay 8 patos en un estanque y llegan 6. ¿Cuántos hay?", "steps": ["Lleno un marco con 8 y 2 del 6.", "Quedan 4 en el segundo marco.", "10 + 4 = 14."], "answer": "14 patos"},
        {"title": "Con la recta", "problem": "Hay 12 manzanas y agrego 5. ¿Cuántas hay?", "steps": ["Parto en 12.", "Salto cinco: 13, 14, 15, 16, 17.", "Llego a 17."], "answer": "17 manzanas"},
    ],
    mistakes=[
        {"wrong": "Saltar seis lugares en vez de cinco.", "why": "Se cuenta el punto de partida.", "fix": "No cuentes el 12; parte desde él y salta cinco."},
        {"wrong": "Olvidar lo que queda en el segundo marco.", "why": "Se queda en el 10.", "fix": "Suma lo que quedó al 10."},
    ],
    tiers={
        "recovery": [arith("Hay 9 y agrego 3. ¿Cuántos hay?", "9+3", "Completo diez con 1 y quedan 2."), arith("Hay 10 y agrego 4. ¿Cuántos hay?", "10+4", "Diez y cuatro."), arith("Hay 7 y agrego 5. ¿Cuántos hay?", "7+5", "Completo diez con 3 y quedan 2.")],
        "understand": [
            ex("¿Qué pasa en el marco de diez cuando se llena?", "Se pasa al siguiente marco", "Después del diez empieza otro marco."),
            ex("En la recta, ¿cuántos saltos hago para sumar 5?", "5 saltos", "Un salto por cada unidad."),
            ex("¿Es el total mayor o menor que cada sumando?", "Mayor", "Al agregar hay más."),
        ],
        "apply": [
            arith("En un bus hay 13 personas y suben 4. ¿Cuántas hay?", "13+4", "Parto en 13 y salto cuatro."),
            arith("Una niña tiene 8 cintas y compra 7. ¿Cuántas cintas tiene?", "8+7", "Completo diez con 2 y quedan 5."),
            arith("En una pecera hay 11 peces y ponen 6 más. ¿Cuántos peces hay?", "11+6", "Parto en 11 y salto seis."),
        ],
        "reason": [
            ex("Beto dice que 9 + 4 = 12. ¿Qué error pudo cometer?", "Contó mal los saltos; es 13", "9, 10, 11, 12, 13."),
            ex("¿Por qué ayuda el marco de diez en 8 + 6?", "Porque se completa un diez y se suma el resto", "10 + 4 es más fácil."),
        ],
        "challenge": [
            arith("Una caja tiene 12 bolitas y otra 8. ¿Cuántas bolitas hay en total?", "12+8", "Parto en 12 y salto ocho."),
            ex("Sumo 7 a un número y llego a 15. ¿De qué número partí?", "8", "8 + 7 = 15."),
        ],
    },
    context=[arith("En una sala hay 9 niños y llegan 8 más. ¿Cuántos niños hay en total?", "9+8", "Completo diez con 1 y quedan 7.")],
    selfcheck=[arith("Calcula 6 + 5.", "6+5", "Completo diez con 4."), arith("Calcula 14 + 3.", "14+3", "Parto en 14 y salto tres."), ex("¿Puede el total ser menor que un sumando?", "No", "Al sumar hay más.")],
    open_task=task("Resuelve 8 + 7 de dos maneras: con el marco de diez y con la recta numérica. Escribe el resultado de cada una y comprueba que coinciden.", "Marco de diez: lleno 10 con 2 del 7 y quedan 5, 15. Recta: parto en 8 y salto siete, llego a 15. Los dos dan 15.", ["usa las dos representaciones", "los resultados coinciden", "explica una de ellas"], ["marco", "recta", "comparación"], ["no coinciden", "saltos mal contados"], "Pide contar los saltos con el dedo."),
    reinforce="Resuelve 6 sumas hasta 20 con el marco de diez.",
    extend="Resuelve una suma hasta 20 de una tercera manera, por ejemplo con dobles.",
)

register(
    OA9, 4,
    materials="Dibujos con puntos y la recta numérica de 0 a 20 en este cuaderno; datos de cada problema escritos.",
    use="Aprenderé a restar y a comparar con números hasta 20. Sirve para saber cuántos quedan o cuántos más tiene alguien.",
    prior=["Sé sumar hasta 20.", "Sé restar hasta 10."],
    explain=[
        "Con números hasta 20 también puedes quitar. Si hay 15 manzanas y se comen 4, quedan 11. Parte en 15 y retrocede cuatro lugares en la recta: 14, 13, 12, 11.",
        "Otra situación es comparar: ¿cuántos más? Si Ana tiene 14 y Beto tiene 9, para saber cuántos más tiene Ana, empareja o cuenta cuánto le falta a 9 para llegar a 14. Son 5.",
        "Por eso 14 − 9 = 5 sirve para quitar y para comparar. Lee bien la pregunta para saber de qué situación se trata, y escribe siempre la respuesta con una frase que diga qué se contó.",
    ],
    vocab=[("restar", "quitar o comparar"), ("comparar", "ver cuántos más o cuántos menos"), ("cuántos más", "la diferencia entre dos cantidades"), ("retroceder", "contar hacia atrás"), ("diferencia", "lo que separa dos números")],
    worked=[
        {"title": "Quitar", "problem": "Hay 15 manzanas y se comen 4. ¿Cuántas quedan?", "steps": ["Parto en 15.", "Retrocedo cuatro: 14, 13, 12, 11.", "Quedan 11."], "answer": "11 manzanas"},
        {"title": "Comparar", "problem": "Ana tiene 14 figuritas y Beto 9. ¿Cuántas más tiene Ana?", "steps": ["Parto en 9 y sumo hasta 14: 10, 11, 12, 13, 14.", "Conté 5 saltos.", "14 − 9 = 5."], "answer": "Ana tiene 5 más"},
    ],
    mistakes=[
        {"wrong": "Decir que Ana tiene 14 más.", "why": "Se confunde cuántas tiene con cuántas más tiene.", "fix": "La pregunta es la diferencia: 14 − 9."},
        {"wrong": "Retroceder cinco lugares en vez de cuatro.", "why": "Se cuenta el punto de partida.", "fix": "Parte en 15 y di los números que van antes."},
    ],
    tiers={
        "recovery": [arith("Hay 12 sillas y se llevan 2. ¿Cuántas quedan?", "12-2", "Desde el inicio retrocedo dos lugares."), arith("Hay 16 tapas y pierdo 4. ¿Cuántas quedan?", "16-4", "Desde el inicio retrocedo cuatro lugares."), arith("Hay 20 palitos y uso 5. ¿Cuántos quedan?", "20-5", "Desde el inicio retrocedo cinco lugares.")],
        "understand": [
            ex("¿Cuántos más tiene Ana si tiene 14 y Beto 9?", "5 más", "14 − 9 = 5."),
            ex("En 14 − 9, ¿se puede comparar y también quitar?", "Sí", "La resta sirve para ambas situaciones."),
            ex("¿Qué debo leer para saber si quito o comparo?", "La pregunta", "Dice qué se pide."),
        ],
        "apply": [
            arith("Luis tiene 17 cartas y Mara 11. ¿Cuántas más tiene Luis?", "17-11", "Es la diferencia."),
            arith("En una caja hay 18 bolitas y se sacan 9. ¿Cuántas quedan?", "18-9", "Se sacan nueve."),
            arith("Una torre tiene 13 cubos y otra 8. ¿Cuántos cubos menos tiene la segunda?", "13-8", "Es la diferencia."),
        ],
        "reason": [
            ex("Raúl dice que 14 − 9 = 23. ¿Qué error comete?", "Suma en vez de restar; es 5", "Restar da una cantidad menor."),
            ex("Si Ana tiene 5 más que Beto, ¿Beto tiene más o menos que Ana?", "Menos", "Ana tiene mayor cantidad."),
        ],
        "challenge": [
            ex("Tengo 20 fichas y regalo 12. ¿Cuántas me quedan?", "8", "20 − 12 = 8."),
            ex("Una niña tiene 9 y quiere tener 15. ¿Cuántas le faltan?", "6", "15 − 9 = 6."),
        ],
    },
    context=[arith("En un autobús caben 20 pasajeros. Ya hay 13. ¿Cuántos asientos quedan libres?", "20-13", "Lo que falta para llegar a 20.")],
    selfcheck=[arith("Calcula 15 − 3.", "15-3", "Desde el inicio retrocedo tres lugares."), arith("Ana tiene 12 y Beto 7. ¿Cuántas más tiene Ana?", "12-7", "Es la diferencia."), ex("¿La resta sirve para comparar?", "Sí", "Da cuántos más.")],
    open_task=task("Resuelve estos dos problemas: (1) Hay 16 galletas y se comen 7. ¿Cuántas quedan? (2) Sofi tiene 16 figuritas y Teo 7. ¿Cuántas más tiene Sofi? Compara tus dos soluciones y explica por qué la cuenta es la misma.", "(1) 16 − 7 = 9. (2) 16 − 7 = 9. La cuenta es la misma porque en las dos se separa un 7 de un 16: una vez para quitar y otra para ver la diferencia.", ["resuelve los dos", "usa la resta", "explica la diferencia de situaciones"], ["dos soluciones", "explicación"], ["no ver que es la misma cuenta", "calcular mal"], "Pide comprobar sumando 7 + 9."),
    reinforce="Resuelve 6 restas hasta 20 con la recta numérica.",
    extend="Inventa un problema de quitar y otro de comparar con los mismos números.",
)

register(
    OA9, 5,
    materials="Una lista de situaciones y de números del 0 al 20 en cada ejercicio; lápiz.",
    use="Aprenderé a crear mis propios problemas de sumar y de restar, a resolverlos y a revisarlos. Sirve para comprobar que entiendo cuándo sumar y cuándo restar.",
    prior=["Sé resolver problemas de agregar y quitar.", "Sé comparar."],
    explain=[
        "Para crear un problema, elige una situación (animales, frutas, juguetes), una acción (agregar o quitar) y dos números. Por ejemplo: «Hay 12 pájaros y se van 5. ¿Cuántos quedan?». La pregunta debe tener una sola respuesta.",
        "Para resolverlo, haz un dibujo o usa la recta. Escribe la operación (12 − 5 = 7) y responde con una frase completa: «Quedan 7 pájaros».",
        "Para revisarlo, comprueba tres cosas: ¿la respuesta tiene sentido? ¿La operación coincide con la historia? ¿Comprobé con la operación inversa? Si algo falla, corrígelo y vuelve a revisar hasta que todo coincida con la historia que inventaste.",
    ],
    vocab=[("crear", "inventar un problema nuevo"), ("revisar", "comprobar que todo está bien"), ("operación inversa", "la operación contraria que comprueba"), ("tiene sentido", "la respuesta es posible en la historia"), ("pregunta", "lo que se quiere saber")],
    worked=[
        {"title": "Crear y resolver", "problem": "Crea un problema con 12 y 5 que se resuelva con una resta.", "steps": ["Elijo pájaros y la acción de irse.", "Escribo: «Hay 12 pájaros y se van 5. ¿Cuántos quedan?».", "12 − 5 = 7.", "Compruebo: 7 + 5 = 12."], "answer": "Quedan 7 pájaros"},
        {"title": "Revisar", "problem": "Un amigo resolvió «hay 9 flores y se cortan 3» como 9 + 3 = 12. ¿Qué corriges?", "steps": ["Se cortan flores: se quitan.", "Corresponde una resta.", "9 − 3 = 6."], "answer": "9 − 3 = 6; quedan 6 flores"},
    ],
    mistakes=[
        {"wrong": "Un problema sin pregunta.", "why": "Se olvida lo que se quiere saber.", "fix": "Termina con una pregunta clara."},
        {"wrong": "No revisar si la respuesta tiene sentido.", "why": "Se acepta el primer resultado.", "fix": "Pregunta si el número es posible en la historia."},
    ],
    tiers={
        "recovery": [ex("Completa: «Hay 8 peces y llegan 3. ¿____ peces hay?».", "Cuántos", "La pregunta pide una cantidad."), arith("Resuelve: 8 + 3.", "8+3", "Llegan peces, se suma."), arith("Resuelve: 8 − 3.", "8-3", "Se van peces, se resta.")],
        "understand": [
            ex("¿Qué debe tener todo problema al final?", "Una pregunta", "Dice lo que se busca."),
            ex("Hice una resta y quiero revisarla. ¿Qué operación uso?", "Una suma", "La suma deshace la resta."),
            ex("Una respuesta dice «hay 25 gatos» en un problema con 5 y 4. ¿Tiene sentido?", "No", "5 + 4 = 9, no 25."),
        ],
        "apply": [
            ex("Crea un problema de sumar con 6 y 7 y resuélvelo.", "Por ejemplo: Hay 6 lápices y agrego 7. ¿Cuántos hay? 6 + 7 = 13", "Se agrega y se suma."),
            ex("Crea un problema de restar con 15 y 8 y resuélvelo.", "Por ejemplo: Hay 15 caramelos y me como 8. ¿Cuántos quedan? 15 − 8 = 7", "Se quita y se resta."),
            ex("Resuelve y comprueba: 18 − 9.", "9; 9 + 9 = 18", "La suma deshace la resta."),
        ],
        "reason": [
            ex("Un compañero escribió «hay 10 y se van 4, ¿cuántos hay?» y respondió 14. ¿Qué corriges?", "Debe restar: quedan 6", "Si se van, se resta."),
            ex("¿Por qué conviene comprobar con la operación inversa?", "Porque muestra si el resultado vuelve al inicio", "Si no vuelve, hay error."),
        ],
        "challenge": [
            ex("Inventa un problema que se resuelva con 20 − 12.", "Por ejemplo: Había 20 sillas y se llevaron 12", "Hay que quitar 12 de 20."),
            ex("Dos problemas distintos usan 9 y 6. Uno se suma y otro se resta. ¿Qué resultados dan?", "15 y 3", "9 + 6 = 15 y 9 − 6 = 3."),
        ],
    },
    context=[ex("Un niño dice: «tengo 14 autitos, regalo 5 y me quedan 9». Escribe la operación y comprueba con la inversa.", "14 − 5 = 9; 9 + 5 = 14", "La suma devuelve al total.")],
    selfcheck=[ex("¿Cómo sé que un problema se resuelve con una resta?", "Porque se quita o se compara", "Es la acción de la historia."), arith("Resuelve y comprueba: 13 − 6.", "13-6", "6 + 7 = 13."), ex("¿Qué debe tener la respuesta final?", "Una frase completa", "Dice qué se contó.")],
    open_task=task("Crea un problema de sumar y uno de restar, cada uno con dos números del 0 al 20. Resuélvelos con dibujo o recta, responde con frase y comprueba el de restar con una suma.", "Sumar: Hay 7 gatos y llegan 6. 7 + 6 = 13. Hay 13 gatos. Restar: Hay 15 uvas y me como 9. 15 − 9 = 6. Quedan 6 uvas. Comprobación: 6 + 9 = 15.", ["dos problemas con pregunta", "resuelve con operación", "responde con frase", "comprueba la resta"], ["dos problemas", "resoluciones", "comprobación"], ["problema sin pregunta", "operación equivocada"], "Pide leer cada problema a otra persona para ver si se entiende."),
    reinforce="Crea tres problemas con los números 4, 9 y 13.",
    extend="Crea un problema con dos pasos (primero se agrega y luego se quita) y resuélvelo.",
)

# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="10 fichas y un vaso; las acciones y los números están escritos en cada ejercicio.",
    use="Aprenderé que algunas acciones se pueden deshacer: agregar se deshace quitando. Sirve para entender por qué sumar y restar están relacionados.",
    prior=["Sé sumar y restar hasta 10.", "Sé qué significa deshacer."],
    explain=[
        "Hacer y deshacer una acción es volver al punto de partida. Si tienes 5 fichas y agregas 3, tienes 8. Si luego quitas 3, vuelves a 5. Agregar 3 y quitar 3 se deshacen.",
        "Esto es lo que significa que la suma y la resta sean operaciones inversas: una deshace a la otra. 5 + 3 = 8 y 8 − 3 = 5 muestran la misma historia hacia adelante y hacia atrás.",
        "Siempre debes deshacer con el mismo número: si agregaste 3, quitas 3. Si quitas otro número, no vuelves al principio. Comprueba con fichas.",
    ],
    vocab=[("deshacer", "volver al estado anterior"), ("inversa", "la operación que deshace a otra"), ("operación", "suma o resta"), ("volver al inicio", "quedar con la cantidad original"), ("mismo número", "la misma cantidad")],
    worked=[
        {"title": "Agregar y quitar", "problem": "Tengo 5 fichas, agrego 3 y luego quito 3. ¿Cuántas tengo?", "steps": ["5 + 3 = 8.", "8 − 3 = 5.", "Volví a 5."], "answer": "5"},
        {"title": "Quitar y agregar", "problem": "Tengo 9 fichas, quito 4 y luego agrego 4. ¿Cuántas tengo?", "steps": ["9 − 4 = 5.", "5 + 4 = 9.", "Volví a 9."], "answer": "9"},
    ],
    mistakes=[
        {"wrong": "Agregar 3 y quitar 2 y pensar que se vuelve al inicio.", "why": "Se deshace con otro número.", "fix": "Para deshacer, usa el mismo número."},
        {"wrong": "Pensar que sumar y restar no se relacionan.", "why": "Se miran por separado.", "fix": "Una deshace a la otra."},
    ],
    tiers={
        "recovery": [ex("Tengo 4 fichas, agrego 2 y quito 2. ¿Cuántas tengo?", "4", "Agregar y quitar 2 se deshacen."), ex("Tengo 6 fichas, quito 1 y agrego 1. ¿Cuántas tengo?", "6", "Quitar y agregar 1 se deshacen."), ex("Tengo 7 fichas, agrego 3 y quito 3. ¿Cuántas tengo?", "7", "Volví al inicio.")],
        "understand": [
            ex("¿Qué operación deshace una suma?", "La resta", "Quita lo que se agregó."),
            ex("¿Qué operación deshace una resta?", "La suma", "Agrega lo que se quitó."),
            ex("Si agrego 5 y quito 5, ¿vuelvo al inicio?", "Sí", "Es el mismo número."),
        ],
        "apply": [
            ex("Parto en 8, sumo 2 y resto 2. ¿A qué número llego?", "8", "Volví al inicio."),
            ex("Parto en 10, resto 6 y sumo 6. ¿A qué número llego?", "10", "Volví al inicio."),
            ex("Parto en 3, sumo 5 y resto 5. ¿A qué número llego?", "3", "Volví al inicio."),
        ],
        "reason": [
            ex("Ana parte en 6, suma 4 y resta 3. Dice que vuelve a 6. ¿Qué error comete?", "Resta otro número; llega a 7", "Debía restar 4."),
            ex("¿Por qué sumar 0 y restar 0 también se deshacen?", "Porque no cambian la cantidad", "El número queda igual."),
        ],
        "challenge": [
            ex("Parto en un número, sumo 4 y resto 4, y llego a 9. ¿De qué número partí?", "9", "Se vuelve al mismo número."),
            ex("Parto en 12, resto 5, resto 3 y luego sumo 8. ¿A qué número llego?", "12", "5 + 3 = 8 se deshace con +8."),
        ],
    },
    context=[ex("En una caja hay 6 lápices. Meto 4 y luego saco 4. ¿Cuántos lápices hay?", "6", "Meter y sacar 4 se deshacen.")],
    selfcheck=[ex("Si sumo 2 y resto 2, ¿qué pasa?", "Vuelvo al inicio", "Sumar y restar lo mismo se deshace."), ex("Si quito 3 fichas, ¿qué operación me devuelve al inicio?", "La suma", "Agrega lo quitado."), ex("Parto en 7, resto 3 y sumo 3. ¿Llego a?", "7", "Volví al inicio.")],
    open_task=task("Elige el 6, el 8 o el 9 como punto de partida. Usa fichas: agrega 3, escribe cuántas hay; luego quita 3 y escribe cuántas hay. Explica qué notas.", "Elegí 8. 8 + 3 = 11. 11 − 3 = 8. Noto que vuelvo al 8 porque quité lo mismo que agregué.", ["usa el mismo número", "escribe ambos pasos", "explica que vuelve al inicio"], ["fichas o dibujo", "dos operaciones", "explicación"], ["cambiar el número que se quita", "no escribir los dos pasos"], "Pide mostrar con fichas que se vuelve al principio."),
    reinforce="Haz tres veces con fichas: agregar un número y deshacerlo.",
    extend="Descubre qué pasa si agregas 5 y luego quitas 3. ¿Qué número tendrías que quitar para volver?",
)

register(
    OA10, 2,
    materials="Diagramas de parte-parte-todo y fichas; los números están escritos en cada ejercicio.",
    use="Aprenderé que con tres números se escriben cuatro operaciones: dos sumas y dos restas. Sirve para ver cómo se relacionan.",
    prior=["Sé que dos partes forman un todo.", "Sé que suma y resta se deshacen."],
    explain=[
        "Si las partes son 3 y 5 y el todo es 8, puedes escribir 3 + 5 = 8 y 5 + 3 = 8. Son las dos sumas. Y también 8 − 3 = 5 y 8 − 5 = 3. Son las dos restas.",
        "Los tres números 3, 5 y 8 aparecen en las cuatro operaciones. El todo siempre es el mayor y va primero en las restas o al final en las sumas. Esto se llama familia de operaciones.",
        "Conocer la familia ayuda a encontrar un número que falta: si sabes que 8 − 3 = 5, entonces 3 + 5 = 8. Cada operación te da información de las otras tres.",
    ],
    vocab=[("familia de operaciones", "las cuatro operaciones con los mismos tres números"), ("parte", "uno de los sumandos"), ("todo", "el número mayor, el resultado de la suma"), ("suma", "juntar partes"), ("resta", "quitar una parte del todo")],
    worked=[
        {"title": "Las cuatro operaciones", "problem": "Escribe la familia con partes 3 y 5 y todo 8.", "steps": ["Sumas: 3 + 5 = 8 y 5 + 3 = 8.", "Restas: 8 − 3 = 5 y 8 − 5 = 3."], "answer": "3 + 5 = 8; 5 + 3 = 8; 8 − 3 = 5; 8 − 5 = 3"},
        {"title": "Una parte que falta", "problem": "Sé que 9 − 4 = 5. ¿Cuál es la suma de la familia?", "steps": ["Los tres números son 4, 5 y 9.", "El todo es 9.", "4 + 5 = 9."], "answer": "4 + 5 = 9"},
    ],
    mistakes=[
        {"wrong": "Escribir 3 − 8 = 5.", "why": "Se pone el todo al final de la resta.", "fix": "En la resta el todo va primero: 8 − 3."},
        {"wrong": "Cambiar un número de la familia.", "why": "Se pierde de vista que son tres.", "fix": "Son siempre los mismos tres números."},
    ],
    tiers={
        "recovery": [ex("Partes 2 y 4, todo 6. Escribe 2 + 4 = ?.", "6", "Dos partes forman el todo."), ex("Partes 2 y 4, todo 6. Escribe 6 − 2 = ?.", "4", "Quito una parte del todo."), ex("Partes 2 y 4, todo 6. Escribe 6 − 4 = ?.", "2", "Quito la otra parte.")],
        "understand": [
            ex("¿Cuántos números distintos hay en una familia de operaciones?", "3", "Dos partes y un todo."),
            ex("¿Cuál de los tres números es el mayor?", "El todo", "Es el resultado de juntar."),
            ex("¿Cuántas operaciones tiene una familia?", "4", "Dos sumas y dos restas."),
        ],
        "apply": [
            ex("Escribe la familia con partes 4 y 5 y todo 9.", "4 + 5 = 9; 5 + 4 = 9; 9 − 4 = 5; 9 − 5 = 4", "La familia tiene cuatro operaciones."),
            ex("Escribe la familia con partes 6 y 7 y todo 13.", "6 + 7 = 13; 7 + 6 = 13; 13 − 6 = 7; 13 − 7 = 6", "La familia tiene cuatro operaciones."),
            ex("Escribe la familia con partes 10 y 8 y todo 18.", "10 + 8 = 18; 8 + 10 = 18; 18 − 10 = 8; 18 − 8 = 10", "La familia tiene cuatro operaciones."),
        ],
        "reason": [
            ex("Pablo escribió 4 + 5 = 9 y 5 − 4 = 9. ¿Qué error cometió?", "La resta debía ser 9 − 4 = 5", "El todo va primero en la resta."),
            ex("¿Es posible una familia con partes 3 y 3?", "Sí; da 3 + 3 = 6 y 6 − 3 = 3", "Las dos partes pueden ser iguales."),
        ],
        "challenge": [
            ex("Sé que 12 − 5 = 7. Escribe las otras tres operaciones.", "5 + 7 = 12; 7 + 5 = 12; 12 − 7 = 5", "Con los mismos tres números."),
            ex("Dos números de una familia son 6 y 15, y 15 es el todo. ¿Cuál es el tercer número?", "9", "6 + 9 = 15."),
        ],
    },
    context=[ex("En un curso hay 7 niñas y 8 niños, 15 estudiantes en total. Escribe una suma y una resta que cuenten esta historia.", "Por ejemplo: 7 + 8 = 15 y 15 − 7 = 8", "Los tres números de la historia forman la familia.")],
    selfcheck=[ex("Escribe una resta de la familia 4, 6, 10.", "Por ejemplo: 10 − 4 = 6", "El todo va primero."), ex("¿Qué número es el todo en la familia 5, 7, 12?", "12", "Es el mayor."), ex("Escribe una suma de la familia 3, 9, 12.", "Por ejemplo: 3 + 9 = 12", "Dos partes forman el todo.")],
    open_task=task("Elige la familia 5, 8 y 13. Escribe las cuatro operaciones, dibuja un diagrama de partes y todo, y explica cuál de los tres números es el todo y por qué.", "5 + 8 = 13, 8 + 5 = 13, 13 − 5 = 8, 13 − 8 = 5. El todo es 13 porque es el mayor y es lo que resulta al juntar 5 y 8.", ["escribe las cuatro operaciones", "dibuja el diagrama", "explica el todo"], ["cuatro operaciones", "diagrama", "explicación"], ["resta con el todo al final", "olvidar una operación"], "Pide comprobar cada operación con fichas."),
    reinforce="Escribe la familia de operaciones de 2, 7 y 9.",
    extend="Busca una familia en la que una parte sea 0 y escribe sus operaciones.",
)

register(
    OA10, 3,
    materials="Cálculos escritos en cada ejercicio; fichas y lápiz.",
    use="Aprenderé a comprobar una suma con una resta y una resta con una suma. Sirve para estar seguro de mis resultados.",
    prior=["Sé la familia de operaciones.", "Sé sumar y restar hasta 20."],
    explain=[
        "Para comprobar una suma, usa la resta. Si calculaste 7 + 6 = 13, resta 13 − 6: si da 7, tu suma está bien. Si no da 7, hay un error.",
        "Para comprobar una resta, usa la suma. Si calculaste 15 − 8 = 7, suma 7 + 8: si da 15, tu resta está bien. La operación inversa te devuelve al número del comienzo.",
        "Esto es útil porque no necesitas a nadie más: tú mismo puedes saber si te equivocaste. Si la comprobación no coincide, repite el cálculo con calma.",
    ],
    vocab=[("comprobar", "revisar si un resultado está bien"), ("inversa", "operación que deshace a otra"), ("coincidir", "dar el mismo número"), ("error", "algo que no está bien"), ("repetir", "calcular otra vez")],
    worked=[
        {"title": "Comprobar una suma", "problem": "Comprueba 7 + 6 = 13.", "steps": ["Hago la resta inversa: 13 − 6.", "13 − 6 = 7.", "Da 7, el otro sumando."], "answer": "La suma está bien"},
        {"title": "Comprobar una resta", "problem": "Comprueba 15 − 8 = 7.", "steps": ["Hago la suma inversa: 7 + 8.", "7 + 8 = 15.", "Da 15, el número del comienzo."], "answer": "La resta está bien"},
    ],
    mistakes=[
        {"wrong": "Comprobar una suma con otra suma.", "why": "No se usa la operación inversa.", "fix": "Para una suma, usa una resta."},
        {"wrong": "Dar por bueno un resultado sin comprobar.", "why": "Se confía en el primer cálculo.", "fix": "Siempre comprueba con la inversa."},
    ],
    tiers={
        "recovery": [ex("Comprueba 5 + 4 = 9 con 9 − 4.", "9 − 4 = 5; está bien", "Da el otro sumando."), ex("Comprueba 10 − 3 = 7 con 7 + 3.", "7 + 3 = 10; está bien", "Da el número de inicio."), ex("Comprueba 6 + 6 = 12 con 12 − 6.", "12 − 6 = 6; está bien", "Da el otro sumando.")],
        "understand": [
            ex("¿Con qué operación compruebo una suma?", "Con una resta", "La resta deshace la suma."),
            ex("Calculé 9 − 4 = 5. ¿Con qué operación puedo revisarla?", "Una suma", "La suma deshace la resta."),
            ex("Si la comprobación no coincide, ¿qué hago?", "Repito el cálculo", "Hay un error en alguno."),
        ],
        "apply": [
            ex("Calcula 8 + 7 y comprueba con la resta.", "15; 15 − 7 = 8", "La resta devuelve el otro sumando."),
            ex("Calcula 14 − 6 y comprueba con la suma.", "8; 8 + 6 = 14", "La suma devuelve el inicio."),
            ex("Calcula 9 + 9 y comprueba con la resta.", "18; 18 − 9 = 9", "La resta devuelve el otro sumando."),
        ],
        "reason": [
            ex("Luis dice 8 + 5 = 12. Comprueba: 12 − 5 = 7, no 8. ¿Qué concluyes?", "Se equivocó; 8 + 5 = 13", "La comprobación no coincide con el dato."),
            ex("Rosa dice 11 − 4 = 8. Comprueba: 8 + 4 = 12, no 11. ¿Qué concluyes?", "Se equivocó; 11 − 4 = 7", "La comprobación no coincide con el dato."),
        ],
        "challenge": [
            ex("Un cálculo 13 − 5 = 9 está mal. ¿Cuál es el correcto y cómo lo compruebas?", "8; 8 + 5 = 13", "La suma devuelve el 13."),
            ex("Dos amigos calcularon 6 + 9 = 15 y 6 + 9 = 14. ¿Quién tiene razón? Compruébalo.", "El de 15; 15 − 9 = 6", "La resta devuelve el sumando."),
        ],
    },
    context=[ex("Una niña tenía 16 pegatinas, regaló 7 y dice que le quedan 9. ¿Está bien? Comprueba.", "Sí; 9 + 7 = 16", "La suma devuelve el total.")],
    selfcheck=[ex("Comprueba 4 + 8 = 12.", "12 − 8 = 4; está bien", "Da el otro sumando."), ex("Comprueba 13 − 7 = 6.", "6 + 7 = 13; está bien", "Da el número de inicio."), ex("¿Sirve la inversa para detectar errores?", "Sí", "Si no coincide, hay error.")],
    open_task=task("Resuelve 9 + 8 y 17 − 9. Comprueba cada una con su operación inversa y escribe si coinciden. Si no coinciden, corrige.", "9 + 8 = 17; comprobación 17 − 8 = 9, coincide. 17 − 9 = 8; comprobación 8 + 9 = 17, coincide.", ["resuelve las dos", "comprueba con la inversa", "decide si coinciden"], ["dos cálculos", "dos comprobaciones"], ["comprobar con la misma operación", "no corregir un error"], "Pide explicar por qué la comprobación funciona."),
    reinforce="Haz 5 sumas y comprueba cada una con una resta.",
    extend="Inventa un cálculo con un error y pide a otra persona que lo encuentre con la inversa.",
)

register(
    OA10, 4,
    materials="Diagramas con un círculo vacío y fichas; los números están escritos en cada ejercicio.",
    use="Aprenderé a encontrar una parte que falta usando la operación inversa. Sirve para resolver problemas donde no sé uno de los números.",
    prior=["Sé la familia de operaciones.", "Sé comprobar con la inversa."],
    explain=[
        "A veces falta una parte: 5 + __ = 12. Para encontrarla, usa la resta: 12 − 5 = 7. Entonces el número que falta es 7. La operación inversa te da la parte desconocida.",
        "También falta a veces el todo o la primera parte: __ + 4 = 10 se resuelve con 10 − 4 = 6. Y __ − 3 = 5 se resuelve con 5 + 3 = 8, porque antes de quitar 3 había 8.",
        "Siempre comprueba reemplazando: 5 + 7 = 12, y 8 − 3 = 5. Si da, el número es correcto.",
    ],
    vocab=[("parte desconocida", "el número que falta"), ("todo", "el número mayor de la familia"), ("reemplazar", "poner el número en el lugar vacío"), ("operación inversa", "la que deshace a otra"), ("comprobar", "revisar que encaja")],
    worked=[
        {"title": "Falta un sumando", "problem": "Completa 5 + __ = 12.", "steps": ["Uso la resta: 12 − 5.", "12 − 5 = 7.", "Compruebo: 5 + 7 = 12."], "answer": "7"},
        {"title": "Falta el número que se quita", "problem": "Completa __ − 3 = 5.", "steps": ["Antes de quitar 3 había más.", "Uso la suma: 5 + 3 = 8.", "Compruebo: 8 − 3 = 5."], "answer": "8"},
    ],
    mistakes=[
        {"wrong": "Responder 17 a 5 + __ = 12 sumando 5 y 12.", "why": "Se suma lo que hay que restar.", "fix": "Falta una parte: resta el todo menos la parte que conoces."},
        {"wrong": "Restar en vez de sumar en __ − 3 = 5.", "why": "Se confunde la inversa.", "fix": "Para saber cuánto había antes de quitar, suma."},
    ],
    tiers={
        "recovery": [arith("Completa: 4 + __ = 9.", "9-4", "Uso la resta inversa."), arith("Completa: 6 + __ = 10.", "10-6", "Uso la resta inversa."), arith("Completa: 3 + __ = 8.", "8-3", "Uso la resta inversa.")],
        "understand": [
            ex("En 5 + __ = 12, ¿qué operación me da el número que falta?", "Una resta", "12 − 5."),
            ex("En __ − 3 = 5, ¿qué operación me da el número que falta?", "Una suma", "5 + 3."),
            ex("¿Cómo compruebo que un número encaja?", "Lo reemplazo y miro si da", "El cálculo debe cuadrar."),
        ],
        "apply": [
            arith("Completa: 7 + __ = 15.", "15-7", "Uso la resta inversa."),
            arith("Completa: __ + 6 = 14.", "14-6", "Uso la resta inversa."),
            arith("Completa: __ − 4 = 9.", "9+4", "Antes de quitar 4 había más."),
        ],
        "reason": [
            ex("Sofía dice que en 8 + __ = 15 falta 23. ¿Qué error comete?", "Suma en vez de restar; falta 7", "15 − 8 = 7."),
            ex("En __ − 5 = 6, ¿el número que falta es mayor o menor que 6?", "Mayor", "Antes de quitar había más."),
        ],
        "challenge": [
            arith("Completa: 9 + __ = 20.", "20-9", "Uso la resta inversa."),
            ex("Falta un número: __ + __ = 10 y los dos son iguales. ¿Cuál es?", "5", "5 + 5 = 10."),
        ],
    },
    context=[arith("Marcos tenía algunas figuritas, regaló 5 y le quedan 8. ¿Cuántas tenía? (__ − 5 = 8)", "8+5", "Antes de regalar tenía más.")],
    selfcheck=[arith("Completa: 5 + __ = 11.", "11-5", "Uso la resta inversa."), ex("En __ − 2 = 7, ¿falta una suma o una resta?", "Una suma", "7 + 2."), arith("Completa: __ + 3 = 9.", "9-3", "Uso la resta inversa.")],
    open_task=task("Resuelve estos dos: 6 + __ = 14 y __ − 4 = 9. Escribe qué operación usaste en cada uno, el número que falta y la comprobación.", "6 + __ = 14: uso 14 − 6 = 8; compruebo 6 + 8 = 14. __ − 4 = 9: uso 9 + 4 = 13; compruebo 13 − 4 = 9.", ["usa la inversa", "encuentra el número", "comprueba"], ["dos resoluciones", "dos comprobaciones"], ["sumar en vez de restar", "no comprobar"], "Pide explicar por qué una necesita resta y la otra suma."),
    reinforce="Resuelve 5 sumas con un número que falta hasta 12.",
    extend="Inventa tres sumas con un número que falta y deja que otra persona las resuelva.",
)

# ---------------------------------------------------------------- OA 11
register(
    OA11, 1,
    materials="Palmadas, pasos y sonidos que se describen por escrito en cada ejercicio (A = palmada, B = golpe de pie).",
    use="Aprenderé a reconocer y continuar patrones hechos con el cuerpo y con sonidos. Sirve para entender ritmos y cosas que se repiten.",
    prior=["Sé contar hasta 10.", "Sé repetir un ritmo."],
    explain=[
        "Un patrón es algo que se repite siguiendo una regla. Con el cuerpo podemos hacer patrones: palmada, golpe de pie, palmada, golpe de pie. Lo escribimos A B A B A B, donde A es palmada y B es golpe de pie.",
        "La parte que se repite se llama unidad del patrón. En A B A B la unidad es A B. Para continuar un patrón, mira la unidad y sigue repitiéndola. Después de A B A B viene A, luego B.",
        "Hay patrones de 2 elementos (A B), de 3 (A A B) y más. Para descubrirlos, repite en voz alta el ritmo y encuentra desde dónde se repite.",
    ],
    vocab=[("patrón", "algo que se repite siguiendo una regla"), ("unidad", "la parte que se repite"), ("continuar", "seguir el patrón"), ("ritmo", "orden de sonidos o movimientos"), ("repetir", "hacer de nuevo igual")],
    worked=[
        {"title": "Encontrar la unidad", "problem": "Patrón A B A B A B. ¿Cuál es la unidad?", "steps": ["Miro desde el principio.", "Se repite A B.", "La unidad es A B."], "answer": "A B"},
        {"title": "Continuar", "problem": "Patrón A A B A A B A. ¿Qué viene?", "steps": ["La unidad es A A B.", "Llevo A A B A A B A.", "Falta A B para completar."], "answer": "A y luego B"},
    ],
    mistakes=[
        {"wrong": "Cambiar el orden de la unidad.", "why": "No se mira bien lo que se repite.", "fix": "Repite la unidad completa en el mismo orden."},
        {"wrong": "Parar a mitad de la unidad.", "why": "No se completa.", "fix": "Termina la unidad antes de parar."},
    ],
    tiers={
        "recovery": [ex(f"Continúa el patrón: {pat('AB', 6, 4)}.", next_items('AB', 4, 2), "La unidad es A B."), ex(f"Continúa el patrón: {pat('ABB', 6, 4)}.", next_items('ABB', 4, 2), "La unidad es A B B."), ex(f"Continúa el patrón: {pat('AAB', 6, 4)}.", next_items('AAB', 4, 2), "La unidad es A A B.")],
        "understand": [
            ex("En A B A B, ¿cuál es la unidad?", "A B", "Es lo que se repite."),
            ex("En A A B A A B, ¿cuál es la unidad?", "A A B", "Se repiten tres elementos."),
            ex("¿Qué es un patrón?", "Algo que se repite con una regla", "Siempre sigue el mismo orden."),
        ],
        "apply": [
            ex(f"Escribe los siguientes 3 elementos de: {pat('AB', 5)}.", next_items('AB', 5, 3), "La unidad es A B."),
            ex(f"Escribe los siguientes 3 elementos de: {pat('ABC', 5)}.", next_items('ABC', 5, 3), "La unidad es A B C."),
            ex("Haz un patrón con una palmada (A) y dos golpes de pie (B B). Escribe 9 elementos.", "A B B A B B A B B", "La unidad es A B B."),
        ],
        "reason": [
            ex("Ana dice que A B B A B A no es un patrón. ¿Por qué?", "Porque no se repite la misma unidad", "Primero A B B y luego A B A."),
            ex("Un patrón tiene unidad A B C. ¿Qué elemento está en el lugar 6?", "C", "A B C A B C: el sexto es C."),
        ],
        "challenge": [
            ex("Un patrón A B A B A B tiene 6 elementos. ¿Cuántas A hay?", "3", "Una A cada dos elementos."),
            ex("Dos patrones: A B A B y A A B B. ¿Cuál tiene una unidad más larga?", "A A B B", "Tiene cuatro elementos; el otro, dos."),
        ],
    },
    context=[ex("En una canción se hace: palmada, palmada, pie, palmada, palmada, pie. ¿Qué viene después?", "Palmada", "La unidad es palmada, palmada, pie.")],
    selfcheck=[ex(f"Continúa: {pat('AB', 4, 2)}.", next_items('AB', 2, 2), "La unidad es A B."), ex("¿Qué se repite en A B C A B C?", "A B C", "Es la unidad."), ex("¿Cuál es el siguiente de A A B A A B A?", "A", "La unidad es A A B.")],
    open_task=task("Inventa un patrón de ritmo con tres sonidos: palmada (A), pie (B) y chasquido (C). Escribe 9 elementos, marca la unidad y explícalo a otra persona.", "A B C A B C A B C. La unidad es A B C y se repite tres veces.", ["usa una unidad que se repite", "escribe 9 elementos", "marca la unidad"], ["secuencia", "unidad marcada", "explicación"], ["cambiar la regla a mitad", "olvidar marcar la unidad"], "Pide ejecutar el ritmo en voz alta."),
    reinforce="Haz un patrón de dos movimientos con tu cuerpo y repítelo seis veces.",
    extend="Inventa un patrón con una unidad de cuatro elementos y continúalo dos veces.",
)

register(
    OA11, 2,
    materials="Figuras y objetos descritos con letras o símbolos en cada ejercicio (▲ triángulo, ● círculo, ■ cuadrado).",
    use="Aprenderé a reconocer, describir y continuar patrones de figuras y de objetos. Sirve para ordenar y para predecir qué viene.",
    prior=["Sé qué es una unidad de un patrón.", "Conozco círculo, cuadrado y triángulo."],
    explain=[
        "Los patrones también se hacen con objetos y figuras: ▲ ● ▲ ● ▲ ●. La unidad es ▲ ●. También con colores, tamaños o direcciones. Lo importante es que la regla se repita siempre igual.",
        "Para describir un patrón, nombra la unidad con palabras: «triángulo, círculo». Para continuar, repite la unidad hasta donde pidan. Para saber qué hay en un lugar lejano, cuenta de a una unidad.",
        "Los patrones de figuras tienen un lugar para cada elemento. Si la unidad tiene 2 elementos, todos los lugares pares tienen el segundo. Si la unidad tiene 3 elementos, los lugares 3, 6, 9 y 12 tienen el tercero. Esto sirve para saber qué hay en un lugar lejano sin dibujar todo.",
    ],
    vocab=[("figura", "dibujo con forma, como ▲ ● ■"), ("unidad", "lo que se repite"), ("describir", "decir cómo es el patrón"), ("lugar", "posición dentro del patrón"), ("regla", "lo que siempre se cumple")],
    worked=[
        {"title": "Describir", "problem": "Patrón ▲ ● ▲ ● ▲ ●. Describe la regla.", "steps": ["Se repite ▲ ●.", "La regla: triángulo, círculo, y otra vez."], "answer": "Se repite triángulo, círculo"},
        {"title": "Lugar lejano", "problem": "En ■ ● ■ ● ■ ● ■ ●, ¿qué figura está en el lugar 8?", "steps": ["Los lugares pares tienen ●.", "El 8 es par.", "Hay un círculo."], "answer": "●"},
    ],
    mistakes=[
        {"wrong": "Cambiar el tamaño sin cambiar la regla y creer que es otro patrón.", "why": "No se fija en la regla.", "fix": "Mira cuál es la regla; si se repite igual, es el mismo patrón."},
        {"wrong": "Terminar el patrón con la unidad incompleta.", "why": "Se corta antes.", "fix": "Completa la unidad."},
    ],
    tiers={
        "recovery": [ex(f"Continúa con ▲ y ●: {pat('▲●', 6, 4)}.", next_items('▲●', 4, 2), "La unidad es ▲ ●."), ex(f"Continúa con ■ y ●: {pat('■●●', 7, 4)}.", next_items('■●●', 4, 3), "La unidad es ■ ● ●."), ex(f"Continúa con ▲ ■ ●: {pat('▲■●', 6, 3)}.", next_items('▲■●', 3, 3), "La unidad es ▲ ■ ●.")],
        "understand": [
            ex("En ▲ ● ▲ ● ▲ ●, ¿cuál es la unidad?", "▲ ●", "Es lo que se repite."),
            ex("En ■ ■ ● ■ ■ ●, ¿cuál es la unidad?", "■ ■ ●", "Tres elementos que se repiten."),
            ex("¿Puede un patrón estar hecho con colores o tamaños?", "Sí", "Lo importante es la regla."),
        ],
        "apply": [
            ex(f"Escribe los 3 elementos siguientes: {pat('▲●', 4)}.", next_items('▲●', 4, 3), "La unidad es ▲ ●."),
            ex("Crea un patrón con rojo (R), azul (A): unidad R A A. Escribe 9 elementos.", "R A A R A A R A A", "La unidad se repite tres veces."),
            ex(f"En {pat('■●▲', 9)}, ¿qué figura está en el lugar 9?", "▲", "La unidad ■ ● ▲ se repite tres veces y el lugar 9 es el último de la tercera: ▲."),
        ],
        "reason": [
            ex("Mateo dice que ▲ ● ● ▲ ● ▲ es un patrón. ¿Tiene razón?", "No", "No se repite la misma unidad."),
            ex("Ema dice que en ▲ ● ▲ ● el lugar 5 es ●. ¿Tiene razón?", "No; es ▲", "Los lugares impares tienen ▲."),
        ],
        "challenge": [
            ex(f"En {pat('■●', 10)}, ¿cuántos círculos hay?", "5", "Uno cada dos lugares."),
            ex("Un patrón tiene unidad ▲ ■ ● y 12 elementos. ¿Cuántas veces aparece ●?", "4", "Una vez en cada unidad de 3 y hay 4 unidades."),
        ],
    },
    context=[ex("Una guirnalda tiene: banderita roja, azul, azul, roja, azul, azul. ¿De qué color es la banderita 9?", "Azul", "La unidad es roja, azul, azul y el 9 es el tercer lugar de una unidad.")],
    selfcheck=[ex(f"Continúa: {pat('▲●', 4, 2)}.", next_items('▲●', 2, 2), "La unidad es ▲ ●."), ex("¿Qué figura sigue en ■ ● ■ ● ■?", "●", "La unidad es ■ ●."), ex("¿Qué define a un patrón?", "Una regla que se repite", "La unidad se repite igual.")],
    open_task=task("Crea un patrón de figuras con tres figuras (▲, ● y ■) y una unidad de tres elementos. Dibuja 12 elementos, marca la unidad, y di qué figura estará en el lugar 15 sin dibujarla.", "▲ ● ■ ▲ ● ■ ▲ ● ■ ▲ ● ■. Unidad ▲ ● ■. Cinco unidades de 3 llegan justo al lugar 15, así que ahí está el último elemento de la unidad: ■.", ["unidad de tres elementos", "12 elementos correctos", "predice el lugar 15"], ["dibujo", "unidad marcada", "predicción"], ["cambiar la unidad a mitad", "no justificar la predicción"], "Pide completar hasta 15 para comprobar."),
    reinforce="Haz un patrón con tres colores de lápiz y continúalo dos veces.",
    extend="Descubre qué figura hay en el lugar 20 de un patrón con unidad de cuatro figuras.",
)

register(
    OA11, 3,
    materials="Tablas numéricas del 1 al 20 y la recta numérica; los números están escritos en cada ejercicio.",
    use="Aprenderé a reconocer y continuar patrones numéricos que crecen hasta 20. Sirve para anticipar el número siguiente y entender regularidades.",
    prior=["Sé contar de 1 en 1, de 2 en 2 y de 5 en 5.", "Sé qué es una regla."],
    explain=[
        "Un patrón creciente es una lista de números que aumenta con una regla. En 2, 4, 6, 8, la regla es «sumar 2». Cada número es 2 más que el anterior. Para continuar, aplica la regla al último.",
        "Para descubrir la regla, resta los números vecinos: 8 − 6 = 2, 6 − 4 = 2. Si la diferencia siempre es la misma, ésa es la regla. El patrón 1, 3, 5, 7 suma 2 y empieza en 1.",
        "Con la regla puedes completar números que faltan: 5, 10, __, 20 suma 5 y falta 15. Siempre comprueba que la regla funcione en toda la lista.",
    ],
    vocab=[("patrón creciente", "los números aumentan"), ("regla", "lo que se suma cada vez"), ("diferencia", "cuánto aumenta"), ("continuar", "seguir aplicando la regla"), ("término", "cada número de la lista")],
    worked=[
        {"title": "Descubrir la regla", "problem": "Descubre la regla de 3, 6, 9, 12.", "steps": ["6 − 3 = 3.", "9 − 6 = 3.", "12 − 9 = 3.", "La regla es sumar 3."], "answer": "Sumar 3; sigue 15"},
        {"title": "Completar", "problem": "Completa 5, 10, __, 20.", "steps": ["10 − 5 = 5, la regla es sumar 5.", "10 + 5 = 15.", "15 + 5 = 20 confirma."], "answer": "15"},
    ],
    mistakes=[
        {"wrong": "Decir que 3, 6, 9 suma 6.", "why": "Se mira sólo el primer salto desde cero.", "fix": "Resta los vecinos: 6 − 3 = 3."},
        {"wrong": "Cambiar la regla a mitad de la lista.", "why": "No se comprueba toda la lista.", "fix": "Verifica que la diferencia sea la misma siempre."},
    ],
    tiers={
        "recovery": [fill(1, 1, 6, (4, 5), "Se suma 1."), fill(2, 2, 6, (3, 5), "Se suma 2."), fill(5, 5, 4, (2, 3), "Se suma 5.")],
        "understand": [
            ex("En 4, 8, 12, 16, ¿cuál es la regla?", "Sumar 4", "8 − 4 = 4."),
            ex("En 1, 3, 5, 7, ¿cuál es la regla?", "Sumar 2", "3 − 1 = 2."),
            ex("¿Cómo se descubre la regla de un patrón creciente?", "Restando los números vecinos", "La diferencia es la regla."),
        ],
        "apply": [fill(3, 3, 6, (3, 4, 5), "Se suma 3."), fill(4, 4, 5, (2, 4), "Se suma 4."), ex("Escribe 6 números empezando en 2 con la regla «suma 3».", "2, 5, 8, 11, 14, 17", "Se suma 3 cada vez.")],
        "reason": [
            ex("Pía dice que 2, 4, 7, 8 es un patrón de sumar 2. ¿Qué error ve?", "De 4 a 7 se suma 3; debería ser 6", "La diferencia debe ser siempre 2."),
            ex("¿Pueden dos patrones distintos empezar en 2?", "Sí; por ejemplo suma 2 y suma 3", "La regla los distingue."),
        ],
        "challenge": [
            ex("Un patrón suma 4 y empieza en 3. ¿Qué número ocupa el lugar 5?", "19", "3, 7, 11, 15, 19."),
            ex("Un patrón creciente llega a 20 sumando 5 desde 0. ¿Cuántos saltos da?", "4", "5, 10, 15, 20."),
        ],
    },
    context=[ex("Cada día una planta crece 2 cm. El lunes mide 4 cm. ¿Cuánto mide el miércoles?", "8 cm", "4, 6, 8 cm.")],
    selfcheck=[fill(10, 2, 5, (2, 4), "Se suma 2."), ex("En 5, 10, 15, ¿qué sigue?", "20", "La regla es sumar 5."), ex("¿La regla de 1, 4, 7 es sumar 3?", "Sí", "4 − 1 = 3 y 7 − 4 = 3.")],
    open_task=task("Crea un patrón creciente que empiece en 1 y use la regla «suma 3» hasta pasar de 15. Escribe la lista, comprueba la diferencia entre cada par de vecinos y señala el número más grande menor que 20.", "1, 4, 7, 10, 13, 16, 19. Diferencias: 3 en todos los pares. El mayor menor que 20 es 19.", ["aplica la regla", "comprueba las diferencias", "encuentra el número pedido"], ["lista", "diferencias", "respuesta"], ["cambiar la regla", "no comprobar"], "Pide recorrer la lista con la recta."),
    reinforce="Marca en la tabla del 20 los números de 2 en 2 y de 5 en 5.",
    extend="Descubre qué pasa si combinas dos patrones crecientes (de 2 y de 3) y marca los números que comparten.",
)

register(
    OA11, 4,
    materials="Listas numéricas y la recta numérica; los números están escritos en cada ejercicio.",
    use="Aprenderé a reconocer y continuar patrones numéricos que decrecen hasta 20. Sirve para contar hacia atrás con una regla.",
    prior=["Conozco los patrones crecientes.", "Sé restar números pequeños."],
    explain=[
        "Un patrón decreciente es una lista de números que baja con una regla. En 20, 18, 16, 14, la regla es «restar 2». Cada número es 2 menos que el anterior. Para continuar, aplica la regla al último.",
        "Para descubrir la regla, resta el número siguiente al anterior: 20 − 18 = 2, 18 − 16 = 2. Si la diferencia siempre es la misma, ésa es la regla. El patrón 15, 10, 5 resta 5 y se acerca a 0.",
        "Un patrón decreciente tiene un final natural: si llegas a 0 ya no puedes restar. Por eso hay que mirar si la regla permite seguir sin pasar de 0.",
    ],
    vocab=[("patrón decreciente", "los números disminuyen"), ("restar", "bajar con la regla"), ("regla", "lo que se resta cada vez"), ("cero", "el número más pequeño al contar"), ("continuar", "seguir aplicando la regla")],
    worked=[
        {"title": "Descubrir la regla", "problem": "Descubre la regla de 20, 18, 16, 14.", "steps": ["20 − 18 = 2.", "18 − 16 = 2.", "16 − 14 = 2.", "La regla es restar 2."], "answer": "Restar 2; sigue 12"},
        {"title": "Completar", "problem": "Completa 15, __, 5, 0.", "steps": ["5 − 0 = 5, la regla es restar 5.", "15 − 5 = 10."], "answer": "10"},
    ],
    mistakes=[
        {"wrong": "Sumar en un patrón decreciente.", "why": "No se mira que baja.", "fix": "Si los números bajan, la regla es restar."},
        {"wrong": "Seguir restando más allá de 0.", "why": "No se mira el final.", "fix": "Detente cuando llegues a 0."},
    ],
    tiers={
        "recovery": [fill(10, -1, 6, (3, 5), "Se resta 1."), fill(20, -2, 6, (2, 4), "Se resta 2."), fill(20, -5, 5, (2, 4), "Se resta 5.")],
        "understand": [
            ex("En 18, 15, 12, 9, ¿cuál es la regla?", "Restar 3", "18 − 15 = 3."),
            ex("En 16, 12, 8, 4, ¿cuál es la regla?", "Restar 4", "16 − 12 = 4."),
            ex("¿Cómo sé que un patrón es decreciente?", "Porque los números bajan", "Cada uno es menor que el anterior."),
        ],
        "apply": [fill(18, -3, 6, (3, 4, 5), "Se resta 3."), ex("Escribe 5 números empezando en 20 con la regla «resta 4».", "20, 16, 12, 8, 4", "Se resta 4 cada vez."), fill(19, -2, 5, (2, 3), "Se resta 2.")],
        "reason": [
            ex("Rocío dice que 10, 8, 5, 4 baja de 2 en 2. ¿Qué error ve?", "De 8 a 5 baja 3", "Debería ser 6."),
            ex("¿Se puede seguir restando 5 desde 4?", "No", "Desde 4 no se pueden quitar 5: no alcanzan."),
        ],
        "challenge": [
            ex("Un patrón resta 3 y empieza en 20. ¿Qué número ocupa el lugar 5?", "8", "20, 17, 14, 11, 8."),
            ex("Desde 20, ¿cuántos saltos de 4 se dan hasta llegar a 0?", "5", "20, 16, 12, 8, 4, 0."),
        ],
    },
    context=[ex("Una vela mide 20 cm y se gasta 2 cm cada hora. ¿Cuánto mide después de 4 horas?", "12 cm", "20, 18, 16, 14, 12.")],
    selfcheck=[fill(16, -2, 5, (2, 4), "Se resta 2."), ex("En 15, 12, 9, ¿qué sigue?", "6", "La regla es restar 3."), ex("¿Qué número no se puede pasar al restar?", "0", "Es el menor al contar.")],
    open_task=task("Crea un patrón decreciente que empiece en 20 y use la regla «resta 3». Escribe todos los números hasta que no puedas seguir, cuenta cuántos escribiste y explica por qué te detuviste.", "20, 17, 14, 11, 8, 5, 2. Escribí 7 números. Me detuve porque desde 2 no se pueden quitar 3.", ["aplica la regla", "cuenta los números", "explica por qué se detuvo"], ["lista", "conteo", "explicación"], ["pasar de cero", "cambiar la regla"], "Pide recorrer la recta hacia atrás."),
    reinforce="Cuenta hacia atrás de 2 en 2 y de 5 en 5 desde 20.",
    extend="Compara un patrón creciente y uno decreciente que usen la misma regla.",
)

register(
    OA11, 5,
    materials="Fichas, figuras y números descritos en cada ejercicio; lápiz.",
    use="Aprenderé a crear mi propio patrón y a desafiar a otros a continuarlo. Sirve para mostrar que entiendo la regla.",
    prior=["Sé patrones de figuras y de números.", "Sé describir una regla."],
    explain=[
        "Para crear un patrón elige primero qué tipo: de figuras, de colores o de números. Luego elige la unidad o la regla. Por ejemplo: «unidad ▲ ●» o «sumar 2 desde 1».",
        "Escribe suficientes elementos para que se vea la regla, por lo menos dos veces completa la unidad o cuatro números. Así otra persona puede descubrir y continuar tu patrón.",
        "Para desafiar a otros, borra algunos elementos y pídeles que los completen. Después revisa: ¿encontraron la regla? ¿Completaron bien? Si no, explícales cuál es y muéstrales cómo la descubriste tú, paso a paso.",
    ],
    vocab=[("crear", "inventar algo nuevo"), ("desafiar", "proponer un reto a otra persona"), ("completar", "poner lo que falta"), ("regla", "lo que se repite o se suma"), ("descubrir", "encontrar la regla")],
    worked=[
        {"title": "Crear y desafiar", "problem": "Crea un patrón con la regla «suma 2» empezando en 4 y bórralo en dos lugares.", "steps": ["Escribo 4, 6, 8, 10, 12, 14.", "Borro dos: 4, 6, __, 10, __, 14.", "Los faltantes son 8 y 12."], "answer": "4, 6, __, 10, __, 14 (faltan 8 y 12)"},
        {"title": "Revisar un patrón", "problem": "Un amigo creó 2, 5, 8, 12. ¿Es correcto con la regla suma 3?", "steps": ["2 + 3 = 5.", "5 + 3 = 8.", "8 + 3 = 11, no 12."], "answer": "No; el último debe ser 11"},
    ],
    mistakes=[
        {"wrong": "Dar muy pocos elementos.", "why": "No se ve la regla.", "fix": "Escribe al menos dos veces la unidad."},
        {"wrong": "Borrar tantos que no se puede descubrir.", "why": "El desafío es imposible.", "fix": "Borra pocos y deja pistas."},
    ],
    tiers={
        "recovery": [ex("Completa el patrón ▲ ● __ ● ▲ ●.", "▲", "La unidad es ▲ ●."), ex("Completa el patrón 3, 6, __, 12.", "9", "Se suma 3."), ex("Completa el patrón 14, 12, __, 8.", "10", "Se resta 2.")],
        "understand": [
            ex("Para que otra persona descubra mi patrón, ¿cuántas veces repito la unidad?", "Al menos dos veces", "Así se ve la regla."),
            ex("¿Qué debo dar como pista en un desafío?", "Suficientes elementos para ver la regla", "Sin pistas no se puede resolver."),
            ex("¿Qué hago si la otra persona no encuentra la regla?", "Se la explico", "Compartir la regla ayuda."),
        ],
        "apply": [
            ex("Crea un patrón de figuras con unidad ■ ● ● y 9 elementos.", "■ ● ● ■ ● ● ■ ● ●", "La unidad se repite tres veces."),
            ex("Crea un patrón numérico con la regla «suma 5» desde 5 hasta 20.", "5, 10, 15, 20", "Se suma 5 cada vez."),
            ex("Convierte en desafío el patrón 20, 17, 14, 11, 8 borrando dos números.", "Por ejemplo 20, __, 14, 11, __", "Los faltantes son 17 y 8."),
        ],
        "reason": [
            ex("Un desafío muestra sólo el 2 y deja el resto en blanco: 2, __, __, __. ¿Se puede descubrir la regla?", "No; faltan pistas", "Podría ser sumar 2, sumar 3 u otra regla."),
            ex("¿Por qué conviene revisar un patrón antes de entregarlo?", "Para que no tenga errores", "Un error confunde."),
        ],
        "challenge": [
            ex("Crea un patrón decreciente de 4 números con la regla «resta 5» desde 20.", "20, 15, 10, 5", "Se resta 5 cada vez."),
            ex("Crea un patrón que combine un color y una figura con unidad de 4 elementos.", "Por ejemplo: rojo ▲, azul ●, rojo ▲, azul ●", "Los colores y las figuras se repiten."),
        ],
    },
    context=[ex("Dani quiere un collar con cuentas: roja, azul, azul, roja, azul, azul, ... Si tiene 12 cuentas, ¿cuántas son rojas?", "4", "La unidad roja, azul, azul tiene 1 roja y hay 4 unidades.")],
    selfcheck=[ex("Completa: ■ ● ■ __ ■ ●.", "●", "La unidad es ■ ●."), ex("¿Qué es un desafío de patrón?", "Un patrón con espacios para completar", "Otra persona debe descubrir la regla."), ex("Completa: 7, 9, 11, __.", "13", "Se suma 2.")],
    open_task=task("Crea un patrón (de figuras o de números) con al menos 8 elementos. Dibújalo completo, luego escríbelo borrando 2 elementos como desafío, y escribe la regla y las respuestas.", "Patrón: 1, 3, 5, 7, 9, 11, 13, 15 (suma 2). Desafío: 1, 3, __, 7, 9, __, 13, 15. Respuestas: 5 y 11.", ["patrón completo con regla clara", "desafío con dos espacios", "respuestas correctas"], ["patrón", "desafío", "respuestas"], ["regla que no se cumple", "borrar demasiados elementos"], "Pide que otra persona lo resuelva y comente."),
    reinforce="Crea un patrón con tapas de dos colores y pide que un compañero lo continúe.",
    extend="Crea un patrón que use dos reglas a la vez (una de figura y una de números) y explícalo.",
)
