"""Student material for 3.º básico Matemática, OA 19 (calendarios y líneas de tiempo) y OA 20 (hora, medias horas, cuartos y minutos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA19, OA20 = "MA03 OA 19", "MA03 OA 20"

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def cal(nombre: str, primero: int, n: int) -> str:
    """Calendario en texto: para cada día de la semana, las fechas del mes (primero: 0 = lunes)."""
    partes = []
    for i, dia in enumerate(DIAS):
        fechas = [str(d) for d in range(1, n + 1) if (d - 1 + primero) % 7 == i]
        partes.append(f"{dia} {', '.join(fechas)}")
    return f"Calendario de {nombre} ({n} días): " + "; ".join(partes) + "."


ABRIL = cal("abril", 0, 30)
MAYO = cal("mayo", 2, 31)


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 19
register(
    OA19, 1,
    materials="Lápiz y papel. El calendario está escrito dentro de cada ejercicio, con los días de la semana y sus fechas.",
    use="Aprenderé a leer un calendario: encontrar el día de la semana de una fecha y las fechas de un mismo día. Sirve para no olvidar cumpleaños, tareas ni paseos.",
    prior=["Sé que la semana tiene 7 días.", "Sé el orden de los meses del año."],
    explain=[
        "Un calendario muestra los días de un mes ordenados por semanas. Una semana tiene 7 días: lunes, martes, miércoles, jueves, viernes, sábado y domingo. Un año tiene 12 meses, y cada mes tiene entre 28 y 31 días.",
        "En estos ejercicios, el calendario dice qué fechas caen en cada día de la semana. Por ejemplo: «lunes 1, 8, 15». Si buscas el 8, lo encuentras en la lista del lunes, así que el 8 es lunes.",
        "Fíjate en que las fechas de un mismo día de la semana se separan de 7 en 7: 1, 8, 15, 22. Así puedes saber cuántos lunes hay en el mes y qué fechas son.",
    ],
    vocab=[("calendario", "tabla que ordena los días de un mes por semanas"), ("fecha", "día y mes en que ocurre algo, como el 8 de abril"), ("semana", "7 días seguidos"), ("mes", "parte del año con 28 a 31 días"), ("fila de un día", "lista de las fechas que caen en el mismo día de la semana")],
    worked=[
        {"title": "Buscar el día de una fecha", "problem": f"{ABRIL} ¿Qué día de la semana es el 16 de abril?", "steps": ["Busco el número 16 en las listas de cada día.", "El 16 está en la lista del martes: martes 2, 9, 16, 23, 30."], "answer": "El 16 de abril es martes"},
        {"title": "Contar un mismo día en el mes", "problem": f"{ABRIL} ¿Cuántos jueves hay en abril y qué fechas son?", "steps": ["Miro la lista del jueves: 4, 11, 18, 25.", "Cuento las fechas: son 4."], "answer": "Hay 4 jueves: el 4, 11, 18 y 25"},
    ],
    mistakes=[
        {"wrong": "Decir que abril tiene 28 días porque tiene 4 semanas.", "why": "Se cuentan sólo las semanas completas y se olvida el resto.", "fix": "Lee cuántos días tiene el mes en el calendario: abril tiene 30 días."},
        {"wrong": "Buscar una fecha y quedarse con la primera lista que se mira.", "why": "No se revisan todos los días de la semana.", "fix": "Recorre las listas hasta encontrar el número: cada fecha está en una sola lista."},
    ],
    tiers={
        "recovery": [
            ex(f"{ABRIL} ¿Qué día de la semana es el 9 de abril?", "Martes", "El 9 está en la lista del martes."),
            ex(f"{ABRIL} ¿Cuántos días tiene abril?", "30", "El calendario dice que abril tiene 30 días."),
            ex("¿Cuántos días tiene una semana?", "7", "Lunes, martes, miércoles, jueves, viernes, sábado y domingo son siete."),
        ],
        "understand": [
            ex(f"{ABRIL} ¿Qué fechas de abril son viernes?", "5, 12, 19 y 26", "Son las fechas de la lista del viernes."),
            ex(f"{ABRIL} ¿Cuántos lunes hay en abril?", "5", "La lista del lunes tiene 1, 8, 15, 22 y 29."),
            ex(f"{ABRIL} ¿Qué día de la semana es el 30 de abril?", "Martes", "El 30 está en la lista del martes."),
        ],
        "apply": [
            ex(f"{ABRIL} Pedro va a la piscina sólo los sábados. ¿Qué fechas de abril puede ir?", "6, 13, 20 y 27", "Son las fechas de la lista del sábado."),
            ex(f"{ABRIL} Teo cumple años el 14 de abril. ¿Qué día de la semana es su cumpleaños?", "Domingo", "El 14 está en la lista del domingo."),
            ex(f"{ABRIL} Hay taller todos los miércoles de abril. ¿Cuántos días de taller hay?", "4", "Los miércoles son el 3, 10, 17 y 24."),
        ],
        "reason": [
            ex("Rosa dice que abril tiene 28 días porque tiene 4 semanas. ¿Tiene razón? Usa el dato de que abril tiene 30 días.", "No; abril tiene 30 días y sobran 2 días", "Cuatro semanas son 28 días, pero abril llega hasta el 30."),
            ex(f"{ABRIL} Tomás dice que el 15 y el 22 de abril caen en días distintos de la semana. ¿Es verdad?", "No; los dos son lunes", "Las fechas de un mismo día se separan de 7 en 7."),
        ],
        "challenge": [
            ex(f"{MAYO} ¿Cuántos jueves hay en mayo?", "5", "La lista del jueves tiene 2, 9, 16, 23 y 30."),
            ex("El 30 de abril es martes. ¿Qué día de la semana es el 1 de mayo?", "Miércoles", "Después del martes viene el miércoles."),
        ],
    },
    context=[ex(f"{ABRIL} Sacas un libro de la biblioteca el lunes 8 de abril y debes devolverlo una semana después. ¿Qué día y fecha lo devuelves?", "Lunes 15 de abril", "Una semana después es el mismo día, 7 fechas más adelante.")],
    selfcheck=[
        ex("¿Cuántos meses tiene un año?", "12", "Desde enero hasta diciembre hay doce meses."),
        ex(f"{ABRIL} ¿Qué día de la semana es el 21 de abril?", "Domingo", "El 21 está en la lista del domingo."),
        ex(f"{ABRIL} ¿En qué fecha cae el primer miércoles de abril?", "3", "La lista del miércoles empieza con el 3."),
    ],
    open_task=task(
        f"Usa este calendario: {ABRIL} Elige una de estas tres fechas: 7, 18 o 21 de abril. Escribe qué día de la semana es y qué fecha será el mismo día de la semana siguiente. Explica cómo lo encontraste.",
        "El 18 de abril es jueves. Lo encontré en la lista del jueves: 4, 11, 18, 25. El jueves siguiente es el 25, porque se suman 7.",
        ["identifica el día de la semana", "usa la lista del calendario", "suma 7 para la semana siguiente", "explica el procedimiento"],
        ["fecha elegida y día escrito", "fecha de la semana siguiente", "explicación"],
        ["sumar 1 en vez de 7", "confundir la lista de un día con otra"],
        "Pide mostrar con el dedo la lista del calendario donde encontró la fecha. Reconoce que use el salto de 7 en 7.",
    ),
    reinforce="Mira el calendario de tu casa. Busca el día de la semana de tu cumpleaños y di cuántos martes tiene este mes.",
    extend="Escribe las fechas de todos los domingos de mayo con el calendario de mayo de esta clase. Explica qué notas en los números.",
)

register(
    OA19, 2,
    materials="Lápiz y papel. Los calendarios están escritos en cada ejercicio. Abril tiene 30 días.",
    use="Aprenderé a calcular cuántos días pasan entre dos fechas. Sirve para saber cuánto falta para un paseo o una prueba.",
    prior=["Sé leer un calendario.", "Sé restar números hasta 100."],
    explain=[
        "El intervalo es el tiempo que pasa entre dos fechas. Para calcular cuántos días pasan del 5 al 12, restas: 12 − 5 = 7. Pasan 7 días. No cuentas el día 5 otra vez, porque ya estás parado en ese día.",
        "Una semana son 7 días. Del 3 al 17 pasan 14 días, que son 2 semanas. Si las fechas están en meses distintos, cuenta primero los días que faltan para terminar el mes y luego suma los días del mes siguiente.",
        "Por ejemplo, del 27 de abril al 3 de mayo: abril tiene 30 días, así que del 27 al 30 pasan 3 días. Luego del 30 de abril al 3 de mayo pasan 3 días más. En total pasan 6 días.",
    ],
    vocab=[("intervalo", "tiempo que pasa entre dos fechas"), ("antes", "ocurre primero"), ("después", "ocurre más tarde"), ("días que pasan", "resultado de restar la fecha de inicio a la fecha final"), ("semana completa", "7 días seguidos")],
    worked=[
        {"title": "Dos fechas del mismo mes", "problem": "La feria empieza el 4 de abril y termina el 11 de abril. ¿Cuántos días pasan entre el inicio y el término?", "steps": ["Resto la fecha final menos la inicial.", "11 − 4 = 7.", "No cuento el día 4 otra vez."], "answer": "Pasan 7 días, o sea 1 semana"},
        {"title": "Dos fechas de meses distintos", "problem": "Ana viaja el 27 de abril y vuelve el 3 de mayo. Abril tiene 30 días. ¿Cuántos días pasan?", "steps": ["Del 27 al 30 de abril pasan 30 − 27 = 3 días.", "Del 30 de abril al 3 de mayo pasan 3 días más.", "Sumo: 3 + 3 = 6."], "answer": "Pasan 6 días"},
    ],
    mistakes=[
        {"wrong": "Decir que del 6 al 13 de abril pasan 8 días porque se cuentan el 6 y el 13.", "why": "Se cuenta dos veces el extremo y no los saltos entre fechas.", "fix": "Resta 13 − 6 = 7. Piensa en cuántos días avanzas."},
        {"wrong": "Restar 3 − 28 cuando las fechas están en meses distintos.", "why": "No se usa que el mes tiene un número de días.", "fix": "Cuenta primero hasta el fin del mes y luego suma los días del mes siguiente."},
    ],
    tiers={
        "recovery": [
            arith("¿Cuántos días pasan desde el 4 hasta el 9 de abril?", "9-4", "Se resta la fecha de inicio a la fecha final."),
            ex("Del 1 al 8 de abril, ¿cuántas semanas pasan?", "1 semana", "Pasan 7 días y 7 días son una semana."),
            arith("Hoy es 10 de abril. ¿Cuántos días faltan para el 15 de abril?", "15-10", "Se resta la fecha de hoy a la fecha que esperas."),
        ],
        "understand": [
            ex("¿Por qué del 3 al 10 pasan 7 días y no 8?", "Porque se restan las fechas y no se cuenta el 3 otra vez", "10 − 3 = 7: el día de inicio no se cuenta."),
            arith("Del 12 al 26 de abril, ¿cuántos días pasan?", "26-12", "Se resta la fecha de inicio a la fecha final."),
            ex("Hoy es 8 de abril. ¿Qué fecha será dentro de 3 días?", "11 de abril", "Se suma 3 a la fecha de hoy.", calc="8+3"),
        ],
        "apply": [
            arith("La feria empieza el 7 de abril y termina el 19 de abril. ¿Cuántos días pasan entre el inicio y el término?", "19-7", "Se resta la fecha de inicio a la fecha final."),
            ex("Ana viaja el 26 de abril y vuelve el 4 de mayo. Abril tiene 30 días. ¿Cuántos días pasan?", "8 días", "Del 26 al 30 pasan 4 días y del 30 de abril al 4 de mayo pasan 4 días más: 4 + 4.", calc="30-26+4"),
            ex("Una planta se riega el 5 de abril. Se vuelve a regar 10 días después. ¿En qué fecha se riega?", "15 de abril", "Se suman 10 días a la fecha 5.", calc="5+10"),
        ],
        "reason": [
            ex("Luis dice que del 6 al 13 de abril pasan 8 días porque cuenta el 6 y el 13. ¿Qué error comete?", "Cuenta el día de inicio; en realidad pasan 7 días", "Se resta 13 − 6 = 7 y no se cuenta el día inicial."),
            ex("Pasan 14 días desde el 1 de abril. ¿Cae en el mismo día de la semana que el 1 de abril? Explica.", "Sí, porque 14 días son 2 semanas", "Cada 7 días se repite el mismo día de la semana."),
        ],
        "challenge": [
            ex("Un curso empieza el 22 de abril y dura 3 semanas. Abril tiene 30 días. ¿En qué fecha termina? Escribe día y mes.", "13 de mayo", "3 semanas son 21 días: 22 + 21 = 43; como abril tiene 30 días, quedan 43 − 30 = 13 de mayo."),
            ex("Del 20 de abril al 8 de mayo, ¿cuántos días pasan? Abril tiene 30 días.", "18 días", "Del 20 al 30 de abril pasan 10 días y del 30 de abril al 8 de mayo pasan 8 días: 10 + 8.", calc="30-20+8"),
        ],
    },
    context=[ex("Tomás tiene control de lectura el 24 de abril. Hoy es 9 de abril. ¿Cuántos días tiene para estudiar y cuántas semanas completas son?", "15 días, o sea 2 semanas y 1 día", "24 − 9 = 15; 14 días son 2 semanas y sobra 1 día.", calc="24-9")],
    selfcheck=[
        arith("¿Cuántos días pasan del 10 al 17 de abril?", "17-10", "Se resta la fecha de inicio a la fecha final."),
        ex("¿Cada cuántos días se repite el mismo día de la semana?", "Cada 7 días", "La semana tiene siete días."),
        ex("Hoy es 28 de abril. ¿Qué fecha será dentro de 4 días? Abril tiene 30 días.", "2 de mayo", "El 28 + 2 llega al 30; faltan 2 días más, que son el 1 y el 2 de mayo."),
    ],
    open_task=task(
        "Escoge una de estas actividades: una excursión el 25 de abril, un cumpleaños el 12 de mayo o una prueba el 2 de mayo. Hoy es 10 de abril y abril tiene 30 días. Escribe cuántos días faltan para la actividad que elegiste y muestra el cálculo.",
        "Excursión el 25 de abril: 25 − 10 = 15. Faltan 15 días, o sea 2 semanas y 1 día.",
        ["elige una de las tres actividades", "calcula con una resta o con el paso por fin de mes", "escribe el resultado en días", "no cuenta dos veces el día inicial"],
        ["cálculo escrito", "respuesta en días", "explicación del procedimiento"],
        ["contar el día de hoy como un día más", "olvidar que abril termina el 30"],
        "Si dudas, pide dibujar saltos en una línea de números. Reconoce el uso correcto del fin de mes.",
    ),
    reinforce="Pregunta qué fecha es hoy y calcula cuántos días faltan para el último día de este mes.",
    extend="Calcula cuántos días pasan del 15 de abril al 15 de mayo. Explica por qué no son 31.",
)

register(
    OA19, 3,
    materials="Lápiz y papel. Las líneas de tiempo están escritas con edades o con meses, en el enunciado de cada ejercicio.",
    use="Aprenderé a ordenar hechos en una línea de tiempo, de lo que pasó primero a lo que pasó después. Sirve para contar una historia en orden.",
    prior=["Sé leer fechas en un calendario.", "Sé comparar números hasta 100."],
    explain=[
        "Una línea de tiempo es una recta donde se marcan hechos en el orden en que ocurrieron. Se lee de izquierda a derecha. Lo que está más a la izquierda ocurrió antes. Lo que está más a la derecha ocurrió después.",
        "Los hechos se pueden ordenar con edades o con meses. Por ejemplo, un niño camina al año, entra al jardín a los 3 años y entra a primero básico a los 6 años. El orden es 1, 3, 6.",
        "Si dos hechos ocurren al mismo tiempo, se dice que son simultáneos y se marcan en el mismo lugar. Los meses van así: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre y diciembre.",
    ],
    vocab=[("línea de tiempo", "recta con hechos ordenados según cuándo ocurrieron"), ("antes", "más a la izquierda en la línea"), ("después", "más a la derecha en la línea"), ("simultáneo", "que ocurre al mismo tiempo"), ("hecho", "algo que ocurre, como entrar al jardín")],
    worked=[
        {"title": "Ordenar hechos por edad", "problem": "Tomás aprendió a caminar al año, entró al jardín a los 3 años, entró a primero básico a los 6 años y pasó a tercero básico a los 8 años. ¿Qué hecho va más a la derecha?", "steps": ["Pongo las edades en orden: 1, 3, 6, 8.", "El número mayor va más a la derecha: 8.", "A los 8 años pasó a tercero básico."], "answer": "Pasar a tercero básico"},
        {"title": "Años entre dos hechos", "problem": "¿Cuántos años pasaron entre entrar al jardín (3 años) y entrar a primero básico (6 años)?", "steps": ["Resto la edad mayor menos la menor.", "6 − 3 = 3."], "answer": "Pasaron 3 años"},
    ],
    mistakes=[
        {"wrong": "Poner el hecho de los 7 años antes del hecho de los 5 años.", "why": "Se ordena por cómo se cuenta la historia y no por el tiempo.", "fix": "Compara las edades: el número menor va primero."},
        {"wrong": "Marcar hechos simultáneos en lugares distintos.", "why": "Se piensa que cada hecho necesita su propia marca.", "fix": "Si pasan al mismo tiempo, van en la misma marca."},
    ],
    tiers={
        "recovery": [
            ex("Tomás entró al jardín a los 3 años y a primero básico a los 6 años. ¿Qué pasó primero?", "Entró al jardín", "3 años es menos que 6 años."),
            ex("Tomás entró al jardín a los 3 años y a primero básico a los 6 años. ¿Qué pasó después?", "Entró a primero básico", "6 años es más que 3 años."),
            ex("En una línea de tiempo que se lee de izquierda a derecha, ¿dónde va lo que pasó antes?", "A la izquierda", "Lo más antiguo se pone primero."),
        ],
        "understand": [
            ex("Ordena de primero a último: entrar a primero básico (6 años), caminar (1 año), pasar a tercero básico (8 años), entrar al jardín (3 años).", "Caminar, entrar al jardín, entrar a primero básico y pasar a tercero básico", "Las edades 1, 3, 6 y 8 están de menor a mayor."),
            arith("¿Cuántos años pasaron entre entrar al jardín (3 años) y pasar a tercero básico (8 años)?", "8-3", "Se resta la edad menor a la mayor."),
            ex("Dos hechos están marcados en el mismo lugar de la línea. ¿Qué quiere decir?", "Que ocurrieron al mismo tiempo", "Un mismo lugar significa un mismo momento."),
        ],
        "apply": [
            ex("El lunes hay lectura, el miércoles un experimento y el viernes una exposición. ¿Qué hecho ocurre justo después del experimento?", "La exposición", "El viernes viene después del miércoles."),
            ex("Se plantaron semillas en marzo, brotaron en abril, florecieron en junio y se cosecharon en septiembre. ¿Cuántos meses pasaron desde plantar hasta florecer?", "3 meses", "De marzo a abril, mayo y junio son 3 meses.", calc="6-3"),
            ex("Ana aprendió a nadar a los 5 años, a leer a los 6 años y a andar en bicicleta a los 7 años. ¿Cuál queda más a la derecha en su línea de tiempo?", "Andar en bicicleta", "7 años es la edad mayor."),
        ],
        "reason": [
            ex("Pía puso «a los 7 años: bicicleta» antes de «a los 5 años: nadar». ¿Qué error cometió?", "Puso primero el hecho de más edad", "5 es menor que 7, así que nadar va antes."),
            ex("Dos hechos pasaron el mismo día. ¿Cómo se marcan en la línea de tiempo?", "En la misma marca", "Si son simultáneos, se marcan en el mismo lugar."),
        ],
        "challenge": [
            ex("Tomás caminó al año, entró al jardín a los 3 años, a primero básico a los 6 años y a tercero básico a los 8 años. Aprendió a dibujar a los 4 años. ¿Entre cuáles dos hechos va?", "Entre entrar al jardín y entrar a primero básico", "4 está entre 3 y 6."),
            arith("¿Cuántos años pasaron entre caminar (1 año) y pasar a tercero básico (8 años)?", "8-1", "Se resta la edad menor a la mayor."),
        ],
    },
    context=[ex("Una familia anota: 5 de mayo compra de semillas; 12 de mayo siembra; 26 de mayo primeros brotes. ¿Cuántos días pasaron desde la siembra hasta los primeros brotes?", "14 días", "26 − 12 = 14.", calc="26-12")],
    selfcheck=[
        ex("En Matemática: ¿Qué mes viene después de abril?", "Mayo", "El orden es marzo, abril, mayo."),
        ex("Un hecho ocurrió a los 2 años y otro a los 9 años. ¿Cuál va más a la izquierda?", "El de los 2 años", "2 es menor que 9."),
        ex("¿Cuántos meses hay entre enero y abril, contando los saltos de mes en mes?", "3 meses", "De enero a febrero, marzo y abril hay tres saltos.", calc="4-1"),
    ],
    open_task=task(
        "Usa estos cuatro hechos de Ema: nació (0 años), aprendió a nadar (5 años), aprendió a leer (6 años) y aprendió a andar en bicicleta (7 años). Dibuja una línea de tiempo con los hechos en orden y escribe cuántos años pasaron entre nadar y andar en bicicleta.",
        "Línea: nació (0), nadar (5), leer (6), bicicleta (7). Entre nadar y bicicleta pasaron 7 − 5 = 2 años.",
        ["ordena los cuatro hechos de izquierda a derecha", "escribe la edad bajo cada marca", "calcula el intervalo con una resta", "responde con la unidad años"],
        ["dibujo de la línea", "resta escrita", "respuesta"],
        ["poner un hecho fuera de orden", "contar dos veces el año inicial"],
        "Pide leer la línea en voz alta usando antes y después. Reconoce el orden y la resta correcta.",
    ),
    reinforce="Escribe tres cosas que hiciste hoy con la hora aproximada y ordénalas en una línea de tiempo.",
    extend="Agrega a la línea de Ema un hecho nuevo a los 3 años y ubícalo en el lugar correcto. Explica por qué va ahí.",
)

register(
    OA19, 4,
    materials="Lápiz y papel. Las escalas de las líneas están escritas en cada ejercicio. Una escala dice cuánto tiempo hay entre una marca y la siguiente.",
    use="Aprenderé a leer una línea de tiempo con escala: cuánto vale cada marca. Sirve para saber cuándo ocurrió un hecho sin que esté escrita su fecha.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10.", "Sé ordenar hechos en una línea de tiempo."],
    explain=[
        "La escala de una línea de tiempo dice cuánto tiempo hay entre una marca y la siguiente. Si las marcas son 0, 5, 10, 15 y 20, la escala es de 5 en 5. La tercera marca después del 0 no vale 3, vale 15.",
        "Para leer un hecho, mira en qué marca está. Si está en la marca 10, ocurrió a los 10 años. Si está justo a la mitad entre la marca 10 y la marca 20, ocurrió a los 15 años, más o menos.",
        "Para calcular cuánto tiempo pasó entre dos hechos, resta sus números. Si un hecho está en la marca 30 y otro en la marca 50, pasaron 50 − 30 = 20 años. Siempre mira la escala antes de responder.",
    ],
    vocab=[("escala", "lo que vale cada marca de la línea"), ("marca", "raya de la línea con un número"), ("a mitad de camino", "justo en el medio entre dos marcas"), ("acontecimiento", "hecho importante que ocurre en un momento"), ("de 5 en 5", "escala en que cada marca suma 5")],
    worked=[
        {"title": "Leer una marca con escala", "problem": "Una línea tiene las marcas 0, 5, 10, 15 y 20. Un hecho está en la tercera marca después del 0. ¿En qué número ocurrió?", "steps": ["Cuento de 5 en 5: 5, 10, 15.", "La tercera marca después del 0 es el 15."], "answer": "Ocurrió en el 15"},
        {"title": "Mitad entre dos marcas", "problem": "En una línea con marcas de 10 en 10, un hecho está justo a mitad de camino entre el 20 y el 30. ¿Qué número le corresponde?", "steps": ["La mitad de 10 es 5.", "20 + 5 = 25."], "answer": "Aproximadamente el 25"},
    ],
    mistakes=[
        {"wrong": "Leer una línea de 5 en 5 como si fuera de 1 en 1 y decir que la tercera marca es 3.", "why": "No se mira la escala.", "fix": "Antes de responder, lee cuánto sube cada marca."},
        {"wrong": "Restar las posiciones de las marcas y no los números que valen.", "why": "Se cuentan las rayas y no el tiempo.", "fix": "Lee el número de cada marca y réstalos."},
    ],
    tiers={
        "recovery": [
            ex("En una línea con marcas 0, 2, 4, 6, 8, 10 de 2 en 2, ¿qué número sigue después del 6?", "8", "Se suma 2 al 6."),
            ex("La línea de la vida de Ana va de 0 a 10 años con marcas de 2 en 2. Un hecho está en la marca 4. ¿A qué edad ocurrió?", "A los 4 años", "El número de la marca es la edad."),
            ex("¿Qué dice la escala de una línea de tiempo?", "Cuánto vale cada marca", "La escala indica el tiempo entre dos marcas."),
        ],
        "understand": [
            ex("Una línea tiene marcas 0, 5, 10, 15 y 20. Un hecho está en la marca 15. ¿Cuántos años pasaron desde el inicio?", "15 años", "El número de la marca dice cuánto tiempo pasó."),
            ex("En una línea con marcas de 10 en 10 (0, 10, 20, 30, 40), un hecho está justo a mitad de camino entre el 20 y el 30. ¿Qué número le corresponde?", "25", "La mitad de 10 es 5 y 20 + 5 = 25.", calc="20+5"),
            arith("En la línea de una plaza, cada marca vale 10 años. La biblioteca está en la marca 30 y la escuela en la marca 50. ¿Cuántos años pasaron entre las dos?", "50-30", "Se resta el número menor al mayor."),
        ],
        "apply": [
            arith("En un campamento cada marca vale 1 día. La caminata ocurre el día 2 y la función de títeres el día 5. ¿Cuántos días pasan entre las dos?", "5-2", "Se resta el día menor al día mayor."),
            ex("Una línea tiene marcas de 5 en 5. Hay tres hechos: A en la marca 10, B en la marca 25 y C en la marca 40. ¿Cuál es el más reciente?", "C", "40 es el número mayor."),
            ex("En una línea con marcas 0, 20, 40, 60, 80 y 100, un puente está en la marca 60. Un parque se hizo 40 años después. ¿En qué marca está el parque?", "En la marca 100", "60 + 40 = 100.", calc="60+40"),
        ],
        "reason": [
            ex("Mateo lee una línea con marcas de 5 en 5 como si fueran de 1 en 1. Dice que el hecho de la tercera marca después del 0 ocurrió en el 3. ¿Qué hizo mal?", "No miró la escala; esa marca vale 15", "5, 10 y 15: la tercera marca vale 15."),
            ex("Dos hechos están en la misma marca de una línea. ¿Qué se puede decir de ellos?", "Que ocurrieron al mismo tiempo", "Una misma marca es un mismo momento."),
        ],
        "challenge": [
            arith("Una línea tiene marcas de 20 en 20, de 0 a 100. Un hecho está a mitad de camino entre el 40 y el 60, o sea en el 50. Otro hecho está en el 80. ¿Cuántos años pasaron entre ambos?", "80-50", "Se resta 50 al 80."),
            ex("En una línea de 0 a 12 con marcas de 2 en 2, el hecho A está en el 4 y el hecho B en el 10. El hecho C está justo en el medio entre A y B. ¿En qué número está C?", "En el 7", "10 − 4 = 6; la mitad de 6 es 3 y 4 + 3 = 7.", calc="4+3"),
        ],
    },
    context=[ex("En el museo escolar, una línea de tiempo tiene marcas cada 10 años desde que abrió la escuela (0). El gimnasio está en la marca 20 y el patio nuevo en la marca 40. ¿Qué hecho ocurrió hace menos tiempo y cuántos años después del otro?", "El patio nuevo, 20 años después", "40 es mayor que 20 y 40 − 20 = 20.", calc="40-20")],
    selfcheck=[
        ex("En una línea con marcas de 2 en 2, ¿qué número sigue después del 12?", "14", "Se suma 2 al 12."),
        ex("En una línea con marcas de 10 en 10, un hecho está en la quinta marca después del 0. ¿Qué número es?", "50", "10, 20, 30, 40, 50."),
        arith("Un hecho está en la marca 35 y otro en la marca 60. ¿Cuántos años pasaron entre ambos?", "60-35", "Se resta la marca menor a la mayor."),
    ],
    open_task=task(
        "Una línea de tiempo de un árbol que se plantó tiene marcas de 5 en 5 desde 0 hasta 30 años. Tiene estos hechos: se plantó (marca 0), dio la primera flor (marca 10), se hizo un columpio (marca 20) y se podó (marca 30). Dibuja la línea con la escala y escribe cuántos años pasaron entre la primera flor y el columpio.",
        "Línea con 0, 5, 10, 15, 20, 25, 30 y los hechos en 0, 10, 20 y 30. Entre la primera flor y el columpio pasaron 20 − 10 = 10 años.",
        ["dibuja marcas de 5 en 5", "ubica los cuatro hechos en su marca", "calcula la resta 20 − 10", "responde en años"],
        ["línea dibujada con escala", "resta escrita", "respuesta"],
        ["usar marcas de 1 en 1", "poner los hechos fuera de su marca"],
        "Pide decir en voz alta la escala antes de ubicar los hechos. Reconoce que use la escala de 5 en 5.",
    ),
    reinforce="Dibuja una línea con marcas de 2 en 2 hasta 20 y marca el número 14 y el número 18.",
    extend="Inventa una línea de tiempo con marcas de 10 en 10 y tres hechos. Calcula cuánto pasa entre el primero y el último.",
)

register(
    OA19, 5,
    materials="Lápiz y papel. Los calendarios de abril y mayo están escritos en cada ejercicio. Abril tiene 30 días y mayo tiene 31.",
    use="Aprenderé a planificar un trabajo con fechas: cuándo empieza, cuánto dura y cuándo termina. Sirve para organizar tareas y proyectos.",
    prior=["Sé leer un calendario.", "Sé calcular cuántos días pasan entre dos fechas."],
    explain=[
        "Planificar es decidir en qué fecha empieza cada tarea y en qué fecha termina. Para eso usas el calendario y sumas o restas días. Una tarea que empieza el día 8 y dura 5 días termina el día 13, porque 8 + 5 = 13.",
        "Una semana son 7 días y dos semanas son 14 días. Si una tarea dura 2 semanas y empieza un lunes, termina otro lunes. Así puedes saber el día de la semana de la fecha final.",
        "Revisa siempre que el plan tenga sentido. Una tarea no puede empezar antes de que termine la anterior si depende de ella. Y no puedes usar fechas que el mes no tiene, como el 31 de abril.",
    ],
    vocab=[("planificación", "plan que dice cuándo empieza y termina cada tarea"), ("duración", "tiempo que dura una tarea"), ("inicio y término", "fecha en que empieza y fecha en que termina"), ("en orden", "una tarea después de otra, sin mezclarlas"), ("plazo", "fecha máxima para terminar")],
    worked=[
        {"title": "Fecha de término", "problem": f"{ABRIL} Una tarea empieza el lunes 8 de abril y dura 2 semanas. ¿En qué fecha termina?", "steps": ["2 semanas son 14 días.", "8 + 14 = 22.", "El 22 está en la lista del lunes."], "answer": "Termina el lunes 22 de abril"},
        {"title": "Dos tareas seguidas", "problem": "La tarea A empieza el 8 y dura 5 días. La tarea B empieza cuando termina A y dura 7 días. ¿En qué fecha termina B?", "steps": ["A termina el 8 + 5 = 13.", "B empieza el 13 y termina el 13 + 7 = 20."], "answer": "B termina el 20"},
    ],
    mistakes=[
        {"wrong": "Planificar algo para el 31 de abril.", "why": "No se revisa cuántos días tiene el mes.", "fix": "Mira el calendario: abril llega sólo hasta el 30."},
        {"wrong": "Poner el término de una tarea antes de su inicio.", "why": "Se suma mal o se leen las fechas al revés.", "fix": "La fecha final siempre es mayor que la inicial; revisa tu cuenta."},
    ],
    tiers={
        "recovery": [
            ex(f"{ABRIL} Se siembra el 3 de abril. ¿Qué día de la semana es?", "Miércoles", "El 3 está en la lista del miércoles."),
            ex("Se riega cada 3 días empezando el 3 de abril: 3, 6, 9, 12... ¿Qué fecha tiene el quinto riego?", "15 de abril", "La lista es 3, 6, 9, 12, 15."),
            arith("Se riega el 6 y el 13 de abril. ¿Cuántos días pasan entre los dos riegos?", "13-6", "Se resta la fecha menor a la mayor."),
        ],
        "understand": [
            ex("Un brote aparece 10 días después de sembrar el 3 de abril. ¿En qué fecha aparece?", "13 de abril", "Se suman 10 días a la fecha 3.", calc="3+10"),
            ex(f"{ABRIL} Se siembra el miércoles 3 de abril. ¿Qué día de la semana será 10 días después?", "Sábado", "El 13 de abril está en la lista del sábado."),
            arith("Plan: sembrar el 3, medir el 13 y mostrar el 27 de abril. ¿Cuántos días pasan entre medir y mostrar?", "27-13", "Se resta la fecha menor a la mayor."),
        ],
        "apply": [
            arith("Hay 4 etapas seguidas de 5 días cada una. Empiezan el 1 de abril. ¿Qué fecha termina la última etapa?", "1+4*5", "Las 4 etapas suman 20 días y se suman a la fecha 1."),
            ex(f"{ABRIL} La exposición será el último viernes de abril. ¿Qué fecha es?", "26 de abril", "El último número de la lista del viernes es el 26."),
            ex(f"{ABRIL} Hay que entregar un trabajo 2 semanas después del lunes 8 de abril. ¿Qué día y fecha es?", "Lunes 22 de abril", "2 semanas son 14 días y 8 + 14 = 22.", calc="8+14"),
        ],
        "reason": [
            ex("Un plan dice «regar el 31 de abril». ¿Qué error tiene?", "Abril no tiene día 31; sólo llega al 30", "El mes tiene 30 días."),
            ex("Ema planifica pintar un afiche desde el 15 de abril hasta el 12 de abril. ¿Qué error hay?", "El término (12) está antes del inicio (15)", "El término debe ser después del inicio."),
        ],
        "challenge": [
            arith("La tarea A empieza el 8 de abril y dura 5 días. La tarea B empieza cuando termina A y dura 7 días. ¿En qué fecha de abril termina B?", "8+5+7", "A termina el 13 y B termina 7 días después."),
            ex(f"{MAYO} Un proyecto empieza el 29 de abril y dura 4 semanas. Abril tiene 30 días. ¿En qué fecha de mayo termina y qué día es?", "27 de mayo, lunes", "4 semanas son 28 días: 29 + 28 = 57; 57 − 30 = 27 de mayo, que está en la lista del lunes.", calc="29+28-30"),
        ],
    },
    context=[ex(f"{ABRIL} La feria del colegio es el sábado 20 de abril. Las invitaciones se entregan 2 semanas antes. ¿Qué día y fecha se entregan?", "Sábado 6 de abril", "2 semanas son 14 días y 20 − 14 = 6.", calc="20-14")],
    selfcheck=[
        arith("Una tarea empieza el 10 de abril y dura 6 días. ¿En qué fecha termina?", "10+6", "Se suma la duración a la fecha de inicio."),
        ex("¿Una tarea puede terminar antes de empezar?", "No", "El término siempre ocurre después del inicio."),
        ex("Una tarea dura 2 semanas. ¿Cuántos días son?", "14 días", "Cada semana tiene 7 días.", calc="2*7"),
    ],
    open_task=task(
        f"{ABRIL} Planifica el cartel de un huerto con tres tareas seguidas: dibujar (3 días), pintar (4 días) y exponer (1 día). Empieza el lunes 1 de abril. Escribe la fecha de inicio y de término de cada tarea. Cada tarea empieza el día en que termina la anterior.",
        "Dibujar: del 1 al 4 de abril. Pintar: del 4 al 8 de abril. Exponer: del 8 al 9 de abril. Uso 1 + 3 = 4, 4 + 4 = 8 y 8 + 1 = 9.",
        ["usa el 1 de abril como inicio", "suma la duración de cada tarea", "cada tarea empieza donde termina la anterior", "no usa fechas que no existen"],
        ["tabla o lista de fechas", "cálculos escritos", "plan en orden"],
        ["empezar una tarea antes de terminar la anterior", "sumar mal la duración"],
        "Pide revisar con el dedo en el calendario cada fecha. Reconoce que el plan va en orden.",
    ),
    reinforce="Dibuja un plan de tres tareas para esta semana, con el día en que empieza cada una.",
    extend="Calcula en qué fecha termina un proyecto de 5 semanas que empieza el 1 de abril. Abril tiene 30 días.",
)


# ================================================================ OA 20
register(
    OA20, 1,
    materials="Lápiz y papel. Si tienes un reloj de manecillas en casa, puedes mirarlo. Todas las posiciones de las manecillas están escritas en cada ejercicio.",
    use="Aprenderé a relacionar las manecillas del reloj con las horas y los minutos. Sirve para leer la hora en un reloj de manecillas.",
    prior=["Sé contar de 5 en 5 hasta 60.", "Sé que el reloj tiene números del 1 al 12."],
    explain=[
        "El reloj de manecillas tiene dos agujas. La manecilla corta marca las horas. La manecilla larga marca los minutos. Una hora tiene 60 minutos.",
        "Los números del reloj son 12. Cuando la manecilla larga apunta al 12, son cero minutos y la hora es en punto. Si apunta al 1, son 5 minutos; al 2, 10 minutos; al 3, 15 minutos. Cada número que avanza suma 5 minutos.",
        "Por eso, para leer los minutos, cuentas de 5 en 5 desde el 12 hasta el número que apunta la manecilla larga. Si apunta al 6, cuentas 5, 10, 15, 20, 25, 30. Son 30 minutos.",
        "Entre un número y el siguiente hay 4 rayitas pequeñas. Cada rayita vale 1 minuto. Si la larga pasó el 4 y avanzó 2 rayitas más, son 20 + 2 = 22 minutos.",
    ],
    vocab=[("manecilla corta", "aguja que marca las horas"), ("manecilla larga", "aguja que marca los minutos"), ("minuto", "unidad de tiempo; 60 minutos son una hora"), ("en punto", "cuando la manecilla larga apunta al 12"), ("hora", "unidad de tiempo que tiene 60 minutos")],
    worked=[
        {"title": "Minutos con la manecilla larga", "problem": "La manecilla larga apunta al 4. ¿Cuántos minutos pasaron de la hora?", "steps": ["Cuento de 5 en 5 hasta el 4: 5, 10, 15, 20.", "También puedo calcular 4 × 5 = 20."], "answer": "20 minutos"},
        {"title": "Leer la hora completa", "problem": "La manecilla corta apunta al 3 y la manecilla larga apunta al 12. ¿Qué hora es?", "steps": ["La corta apunta al 3: son las 3.", "La larga en el 12 significa cero minutos."], "answer": "Las 3 en punto (3:00)"},
    ],
    mistakes=[
        {"wrong": "Decir que la manecilla larga apunta al 2, entonces son 2 minutos.", "why": "Se lee el número sin pensar que cada número vale 5 minutos.", "fix": "Cuenta de 5 en 5: al 2 le corresponden 10 minutos."},
        {"wrong": "Mezclar las manecillas y leer la hora con la larga.", "why": "No se recuerda cuál es cuál.", "fix": "La corta marca las horas; la larga marca los minutos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué manecilla es más corta: la de las horas o la de los minutos?", "La de las horas", "La manecilla corta marca las horas."),
            ex("La manecilla larga apunta al 12. ¿Cuántos minutos pasaron de la hora?", "0 minutos", "Cuando apunta al 12, la hora es en punto."),
            arith("La manecilla larga apunta al 6. ¿Cuántos minutos son?", "6*5", "Cada número del reloj vale 5 minutos."),
        ],
        "understand": [
            arith("La manecilla larga apunta al 4. ¿Cuántos minutos son?", "4*5", "Cada número del reloj vale 5 minutos."),
            ex("¿Cuántos minutos hay en una hora?", "60", "Una hora completa tiene sesenta minutos."),
            ex("La manecilla larga pasó el 4 y avanzó 3 rayitas más. Cada rayita vale 1 minuto. ¿Cuántos minutos son?", "23", "El 4 vale 20 minutos y 3 rayitas suman 3 minutos más.", calc="20+3"),
        ],
        "apply": [
            ex("La manecilla corta apunta al 3 y la larga al 12. ¿Qué hora es?", "3:00", "La corta marca la hora y la larga en el 12 son cero minutos."),
            ex("La manecilla corta pasó el 5 y todavía no llega al 6. La larga apunta al 3. ¿Qué hora es?", "5:15", "La hora es 5 y la larga al 3 son 15 minutos."),
            ex("La manecilla corta apunta justo al 8 y la larga al 12. Pasa una hora. ¿A qué número apunta la corta?", "Al 9", "En una hora, la corta avanza de un número al siguiente."),
        ],
        "reason": [
            ex("Rita dice: «la manecilla larga apunta al 2, entonces son 2 minutos». ¿Qué error comete?", "Cada número vale 5 minutos; son 10 minutos", "2 × 5 = 10 minutos."),
            ex("Tomás dice que si la corta pasó el 4 y la larga está en el 6, son las 6:04. ¿Está bien?", "No; son las 4:30", "La corta pasó el 4, así que son las 4; la larga en el 6 son 30 minutos."),
        ],
        "challenge": [
            ex("La manecilla larga está en el 12 y avanza hasta llegar otra vez al 12. ¿Cuántos minutos pasaron?", "60 minutos", "Una vuelta completa son 60 minutos, o sea 1 hora."),
            arith("La manecilla larga avanza del 2 al 8. ¿Cuántos minutos pasaron?", "8*5-2*5", "Pasa de 10 minutos a 40 minutos."),
        ],
    },
    context=[ex("Una clase empieza cuando la manecilla corta apunta al 9 y la larga al 12. ¿A qué hora empieza?", "A las 9:00", "La corta en el 9 y la larga en el 12 es hora en punto.")],
    selfcheck=[
        ex("¿Qué manecilla marca los minutos?", "La manecilla larga", "La larga es la de los minutos."),
        arith("La manecilla larga apunta al 3. ¿Cuántos minutos son?", "3*5", "Cada número del reloj vale 5 minutos."),
        ex("La corta apunta al 11 y la larga al 12. ¿Qué hora es?", "11:00", "La larga en el 12 es hora en punto."),
    ],
    open_task=task(
        "Elige una de estas horas: 4:00, 7:25 o 10:40. Dibuja un reloj con las dos manecillas en su lugar y escribe en qué número apunta la manecilla larga y cuántos minutos son.",
        "7:25: la corta pasó el 7 y la larga apunta al 5, porque 5 × 5 = 25 minutos. Dibujo un reloj con ambas manecillas.",
        ["elige una de las tres horas", "ubica la corta en la hora y la larga en el número correcto", "escribe los minutos con cuenta de 5 en 5", "no mezcla las manecillas"],
        ["dibujo del reloj", "número y minutos escritos"],
        ["intercambiar las manecillas", "usar el número como minuto"],
        "Pide explicar cuál manecilla es la corta. Reconoce que cuente de 5 en 5.",
    ),
    reinforce="Mira un reloj de manecillas y di en qué número apunta la manecilla larga. Calcula cuántos minutos son.",
    extend="Dibuja un reloj en que la manecilla larga esté a los 50 minutos y explica a qué número apunta.",
)

register(
    OA20, 2,
    materials="Lápiz y papel. Todas las posiciones de las manecillas están escritas en los ejercicios.",
    use="Aprenderé a leer medias horas y cuartos de hora, y a decirlos. Sirve para entender frases como «las ocho y cuarto».",
    prior=["Sé que una hora tiene 60 minutos.", "Sé leer los minutos con la manecilla larga."],
    explain=[
        "Una hora se puede partir en partes iguales. La mitad de una hora es media hora: son 30 minutos. Un cuarto de hora es la cuarta parte de una hora: son 15 minutos. Hay 4 cuartos en una hora.",
        "Cuando la manecilla larga apunta al 3, ya pasó un cuarto de hora y se dice «y cuarto». Cuando apunta al 6, ya pasó media hora y se dice «y media». Cuando apunta al 9, pasaron 45 minutos y se dice «menos cuarto», porque falta un cuarto de hora para la hora siguiente.",
        "Por ejemplo, si la corta pasó el 8 y la larga apunta al 3, son las ocho y cuarto. Si la corta pasó el 8 y la larga apunta al 9, son las nueve menos cuarto, que es lo mismo que 8:45.",
    ],
    vocab=[("media hora", "30 minutos"), ("cuarto de hora", "15 minutos"), ("y cuarto", "la larga apunta al 3"), ("y media", "la larga apunta al 6"), ("menos cuarto", "la larga apunta al 9; falta un cuarto de hora")],
    worked=[
        {"title": "Decir una hora con cuartos", "problem": "La manecilla corta pasó el 2 y la larga apunta al 3. ¿Cómo se dice la hora?", "steps": ["La hora es 2 porque la corta pasó el 2.", "La larga en el 3 son 15 minutos: un cuarto."], "answer": "Las dos y cuarto (2:15)"},
        {"title": "Menos cuarto", "problem": "La manecilla corta está cerca del 6, pero todavía no llega a él. Pasó el 5. La larga apunta al 9. ¿Qué hora es?", "steps": ["La hora de la corta es 5 porque no llegó al 6.", "La larga en el 9 son 45 minutos.", "Se dice seis menos cuarto, porque falta un cuarto para las 6."], "answer": "5:45, o seis menos cuarto"},
    ],
    mistakes=[
        {"wrong": "Decir que «las ocho menos cuarto» es 8:15.", "why": "Se confunde «menos» con «y».", "fix": "«Menos cuarto» es antes de la hora: las ocho menos cuarto es 7:45."},
        {"wrong": "Pensar que un cuarto de hora son 25 minutos.", "why": "Se confunde con un cuarto de 100.", "fix": "Una hora tiene 60 minutos y un cuarto de 60 es 15."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos minutos tiene media hora?", "30 minutos", "La mitad de 60 es 30."),
            ex("¿Cuántos minutos tiene un cuarto de hora?", "15 minutos", "Un cuarto de 60 minutos es 15."),
            ex("La manecilla larga apunta al 3. ¿Se dice «y cuarto» o «y media»?", "Y cuarto", "El 3 corresponde a 15 minutos."),
        ],
        "understand": [
            ex("¿Cuántos cuartos de hora hay en una hora?", "4", "Cuatro partes de 15 minutos hacen 60 minutos.", calc="60//15"),
            ex("Escribe «las siete y media» con números.", "7:30", "Y media son 30 minutos."),
            ex("La manecilla larga apunta al 9. ¿Cuántos minutos son y cómo se dice con la palabra «cuarto»?", "45 minutos; menos cuarto", "9 × 5 = 45, y falta un cuarto para la hora siguiente.", calc="9*5"),
        ],
        "apply": [
            ex("La manecilla corta pasó el 2 y la larga apunta al 6. ¿Qué hora se dice?", "Las dos y media", "La hora es 2 y la larga en el 6 son 30 minutos."),
            ex("La manecilla corta pasó el 5 y todavía no llega al 6. La larga apunta al 9. Escribe la hora con números.", "5:45", "La hora es 5 y la larga en el 9 son 45 minutos."),
            ex("Son las cuatro y cuarto. ¿A qué número apunta la manecilla larga?", "Al 3", "Un cuarto de hora son 15 minutos y 15 corresponde al 3."),
        ],
        "reason": [
            ex("Pedro dice que «las ocho menos cuarto» es 8:15. ¿Es correcto?", "No; es 7:45", "«Menos cuarto» es un cuarto de hora antes de las ocho."),
            ex("Ana dice que dos cuartos de hora son una media hora. ¿Es verdad?", "Sí; 15 + 15 = 30", "Dos cuartos de 15 minutos suman 30 minutos.", calc="15+15"),
        ],
        "challenge": [
            arith("¿Cuántos minutos son tres cuartos de hora?", "3*15", "Cada cuarto de hora son 15 minutos."),
            arith("Una película dura 2 horas y media. ¿Cuántos minutos son en total?", "2*60+30", "Dos horas son 120 minutos y media hora son 30 minutos."),
        ],
    },
    context=[ex("Elena sale de su casa a las ocho y media. Escribe la hora con números.", "8:30", "Y media son 30 minutos después de las ocho.")],
    selfcheck=[
        ex("¿Cuántos minutos hay en media hora?", "30", "La mitad de una hora son treinta minutos."),
        ex("La corta pasó el 10 y la larga apunta al 3. ¿Qué hora es?", "Las diez y cuarto", "El 3 en la larga son 15 minutos."),
        ex("Un cuarto de hora más otro cuarto de hora más otro cuarto de hora, ¿cuántos minutos son?", "45 minutos", "15 + 15 + 15 = 45.", calc="15+15+15"),
    ],
    open_task=task(
        "Elige una de estas tres horas: las seis y cuarto, las nueve y media o las cuatro menos cuarto. Escríbela con números, dibuja el reloj con sus manecillas y explica a qué número apunta la manecilla larga.",
        "Las nueve y media es 9:30. La corta pasó el 9 y la larga apunta al 6, porque 30 minutos corresponden al 6.",
        ["escribe la hora con números", "dibuja la corta y la larga bien ubicadas", "explica con minutos", "distingue «y» de «menos»"],
        ["hora en números", "dibujo del reloj", "explicación"],
        ["confundir «menos cuarto» con «y cuarto»", "leer el 6 como 6 minutos"],
        "Pide decir en voz alta cuántos minutos son. Reconoce la diferencia entre «y cuarto» y «menos cuarto».",
    ),
    reinforce="Pregunta a alguien de tu casa qué hora es y di si es y cuarto, y media o menos cuarto.",
    extend="Escribe cómo se dicen las 3:15, las 3:30 y las 3:45 usando «y cuarto», «y media» y «menos cuarto».",
)

register(
    OA20, 3,
    materials="Lápiz y papel. Todas las horas están escritas en cada ejercicio.",
    use="Aprenderé a pasar de la hora del reloj de manecillas a la hora del reloj digital, y al revés. Sirve para leer cualquier reloj.",
    prior=["Sé leer horas, medias horas y cuartos en un reloj de manecillas.", "Sé que cada número del reloj vale 5 minutos."],
    explain=[
        "Un reloj digital muestra la hora con números, como 8:45. El número de la izquierda son las horas. Los dos números de la derecha son los minutos. Entonces 8:45 se lee ocho cuarenta y cinco: son las 8 horas y 45 minutos.",
        "Para pasar de un reloj de manecillas a uno digital, mira la corta para la hora y cuenta de 5 en 5 con la larga para los minutos. Si la corta pasó el 8 y la larga apunta al 9, son 8 y 45 minutos: 8:45.",
        "Para pasar de digital a manecillas, usa los minutos. Si ves 3:20, la corta pasó el 3 y la larga apunta al 4, porque 4 × 5 = 20. Los minutos nunca son más de 59, porque con 60 minutos empieza otra hora.",
    ],
    vocab=[("reloj digital", "reloj que muestra la hora con números"), ("reloj análogo", "reloj de manecillas"), ("dos puntos", "signo que separa las horas de los minutos"), ("formato digital", "forma de escribir la hora, como 8:45"), ("minutos de la hora", "los dos números que van después de los dos puntos")],
    worked=[
        {"title": "De manecillas a digital", "problem": "La manecilla corta pasó el 2 y la larga apunta al 9. ¿Cómo se escribe la hora en un reloj digital?", "steps": ["La hora es 2.", "La larga en el 9 son 9 × 5 = 45 minutos.", "Escribo 2:45."], "answer": "2:45"},
        {"title": "De digital a manecillas", "problem": "Un reloj digital marca 11:20. ¿En qué número apunta la manecilla larga?", "steps": ["Los minutos son 20.", "20 ÷ 5 = 4.", "La larga apunta al 4."], "answer": "Al 4"},
    ],
    mistakes=[
        {"wrong": "Leer 8:45 como «ocho horas con cuarenta y cinco horas».", "why": "Se piensa que los dos números son horas.", "fix": "El número de la izquierda son horas y el de la derecha son minutos: 8 horas y 45 minutos."},
        {"wrong": "Decir que si la larga apunta al 5, el reloj digital marca :5.", "why": "Se copia el número del reloj como minutos.", "fix": "Multiplica por 5: el 5 son 25 minutos."},
    ],
    tiers={
        "recovery": [
            ex("El reloj digital marca 6:00. ¿A qué número apunta la manecilla larga?", "Al 12", "Cero minutos corresponde al 12."),
            ex("El reloj digital marca 3:30. ¿A qué número apunta la manecilla larga?", "Al 6", "30 minutos corresponden al 6."),
            ex("La corta apunta al 10 y la larga al 12. Escribe la hora en un reloj digital.", "10:00", "La larga en el 12 son cero minutos."),
        ],
        "understand": [
            ex("La corta pasó el 2 y la larga apunta al 9. Escribe la hora en un reloj digital.", "2:45", "9 × 5 = 45 minutos.", calc="9*5"),
            ex("El reloj digital marca 11:20. ¿A qué número apunta la manecilla larga?", "Al 4", "20 minutos son 4 números de 5 minutos.", calc="20//5"),
            ex("¿Cómo se dice 8:45 usando «menos cuarto»?", "Las nueve menos cuarto", "Faltan 15 minutos para las 9."),
        ],
        "apply": [
            ex("El reloj digital marca 4:23. Cada rayita del reloj vale 1 minuto. ¿Entre qué números está la manecilla larga?", "Entre el 4 y el 5, a 3 rayitas del 4", "El 4 vale 20 minutos y el 5 vale 25; 23 son 3 rayitas después del 20."),
            ex("La corta pasó el 12 y la larga apunta al 7. Escribe la hora en un reloj digital.", "12:35", "7 × 5 = 35 minutos.", calc="7*5"),
            ex("El reloj digital marca 5:05. ¿A qué número apunta la manecilla larga?", "Al 1", "5 minutos corresponden al 1."),
        ],
        "reason": [
            ex("Rosa leyó 8:45 como «ocho horas y cuarenta y cinco horas». ¿Qué error cometió?", "Leyó los minutos como si fueran horas", "El 45 son minutos."),
            ex("Leo dice que si la larga apunta al 5, la hora digital termina en :5. ¿Cómo se corrige?", "Termina en :25, porque 5 × 5 = 25", "Cada número vale 5 minutos.", calc="5*5"),
        ],
        "challenge": [
            ex("El reloj digital marca 7:55. ¿Cuántos minutos faltan para las 8:00?", "5 minutos", "60 − 55 = 5.", calc="60-55"),
            arith("¿Cuántos minutos pasan entre las 3:20 y las 3:50?", "50-20", "Se restan los minutos de las dos horas."),
        ],
    },
    context=[ex("El bus sale a las 7:40. ¿Dónde apuntan las manecillas del reloj de manecillas?", "La corta pasó el 7 y la larga apunta al 8", "40 minutos son 8 números de 5 minutos.", calc="40//5")],
    selfcheck=[
        ex("En 9:30, ¿qué número son los minutos?", "30", "Los minutos son los números de la derecha de los dos puntos."),
        ex("La corta pasó el 4 y la larga apunta al 12. ¿Cómo se escribe en un reloj digital?", "4:00", "La larga en el 12 es hora en punto."),
        ex("El reloj digital marca 2:10. ¿A qué número apunta la manecilla larga?", "Al 2", "10 minutos corresponden al 2."),
    ],
    open_task=task(
        "Elige tres de estas horas: 2:10, 5:45, 8:30, 9:15 o 12:55. Para cada una, escribe a qué número apunta la manecilla larga y dibuja un reloj de manecillas. Luego escribe cómo se lee en palabras una de ellas.",
        "5:45: la larga apunta al 9 (9 × 5 = 45) y la corta pasó el 5. Se lee cinco cuarenta y cinco, o seis menos cuarto.",
        ["elige tres horas", "dice el número de la larga con la cuenta de 5 en 5", "dibuja la corta y la larga", "lee los minutos como minutos"],
        ["tres relojes dibujados", "números escritos", "lectura en palabras"],
        ["leer los minutos como horas", "usar el número del reloj como minutos"],
        "Pide explicar qué son los números a la derecha de los dos puntos. Reconoce la cuenta de 5 en 5.",
    ),
    reinforce="Mira un reloj digital en tu casa y dibuja cómo se vería en uno de manecillas.",
    extend="Escribe en digital la hora «las cinco menos cuarto». Explica por qué no es 5:15.",
)

register(
    OA20, 4,
    materials="Lápiz y papel. Todas las horas están escritas en los ejercicios. Considera que las horas son de la misma jornada, sin pasar de la medianoche.",
    use="Aprenderé a calcular cuánto dura algo y a qué hora termina, usando horas, medias horas, cuartos y minutos. Sirve para organizar el día.",
    prior=["Sé leer y escribir horas, medias horas y cuartos.", "Sé sumar y restar números hasta 100."],
    explain=[
        "Para saber cuánto dura algo, miras la hora en que empieza y la hora en que termina. Si una clase empieza a las 9:00 y termina a las 10:00, dura 1 hora. Si empieza a las 4:00 y termina a las 4:30, dura media hora.",
        "Para saber a qué hora termina, suma la duración a la hora de inicio. Si algo empieza a las 4:00 y dura 1 hora y media, primero sumas 1 hora: 5:00. Luego sumas media hora: 5:30.",
        "Cuando sumas minutos, recuerda que 60 minutos son una hora. Si algo empieza a las 7:45 y dura un cuarto de hora, suma 15 minutos: 7:45 y 15 minutos llegan a las 8:00. Si dura media hora, sumas 15 minutos para llegar a las 8:00 y otros 15 minutos: son las 8:15.",
    ],
    vocab=[("duración", "tiempo que pasa entre el inicio y el término"), ("inicio", "hora en que empieza algo"), ("término", "hora en que termina algo"), ("horario", "lista de actividades con su hora"), ("más tarde", "después en el tiempo")],
    worked=[
        {"title": "Hora de término", "problem": "La película empieza a las 4:00 y dura 1 hora y media. ¿A qué hora termina?", "steps": ["Sumo 1 hora a las 4:00: son las 5:00.", "Sumo media hora: 5:30."], "answer": "Termina a las 5:30"},
        {"title": "Duración", "problem": "Lía llega al parque a las 3:15 y se va a las 4:45. ¿Cuánto tiempo estuvo?", "steps": ["De 3:15 a 4:15 pasa 1 hora.", "De 4:15 a 4:45 pasan 30 minutos."], "answer": "1 hora y 30 minutos"},
    ],
    mistakes=[
        {"wrong": "Decir que de 3:30 a 5:00 pasan 2 horas.", "why": "Se restan sólo los números de la hora y se olvidan los minutos.", "fix": "De 3:30 a 4:30 es 1 hora y de 4:30 a 5:00 son 30 minutos: 1 hora y 30 minutos."},
        {"wrong": "Sumar 40 minutos a las 5:30 y escribir 5:70.", "why": "Se suman minutos sin cuidar el máximo de 59.", "fix": "30 minutos llegan a las 6:00 y quedan 10 más: son las 6:10."},
    ],
    tiers={
        "recovery": [
            ex("Una clase empieza a las 9:00 y termina a las 10:00. ¿Cuánto dura?", "1 hora", "De 9 a 10 hay una hora."),
            ex("Una actividad empieza a las 4:00 y termina a las 4:30. ¿Cuánto dura?", "Media hora", "Pasan 30 minutos."),
            arith("Un recreo va de las 2:15 a las 2:30. ¿Cuántos minutos dura?", "30-15", "Se restan los minutos de las dos horas."),
        ],
        "understand": [
            ex("¿Qué hora será 1 hora después de las 5:30?", "6:30", "Se suma 1 a las horas y los minutos quedan igual."),
            ex("¿Qué hora fue media hora antes de las 8:00?", "7:30", "Media hora antes de las 8:00 es 7:30."),
            ex("¿Cuántas medias horas hay en 2 horas?", "4", "Cada hora tiene 2 medias horas y 2 × 2 = 4.", calc="2*2"),
        ],
        "apply": [
            ex("Una película empieza a las 3:00 y dura 1 hora y media. ¿A qué hora termina?", "4:30", "3:00 más 1 hora es 4:00 y media hora más es 4:30."),
            ex("Salgo a las 6:45 y el viaje dura media hora. ¿A qué hora llego?", "7:15", "6:45 más 15 minutos es 7:00; faltan otros 15 minutos: 7:15."),
            ex("Una siesta empieza a las 2:30 y termina a las 4:00. ¿Cuánto dura?", "1 hora y 30 minutos", "De 2:30 a 3:30 es 1 hora y de 3:30 a 4:00 son 30 minutos."),
        ],
        "reason": [
            ex("Beto dice que de 3:30 a 5:00 pasan 2 horas. ¿Qué error comete?", "Olvidó los minutos; pasan 1 hora y 30 minutos", "De 3:30 a 5:00 faltan 30 minutos para completar 2 horas."),
            ex("Una tarea de 40 minutos empieza a las 5:30. Dani dice que termina a las 5:70. ¿Qué error comete y a qué hora termina?", "Los minutos no pasan de 59; termina a las 6:10", "5:30 más 30 minutos es 6:00 y quedan 10 minutos."),
        ],
        "challenge": [
            ex("Una clase empieza a las 10:15 y dura tres cuartos de hora. ¿A qué hora termina?", "11:00", "Tres cuartos de hora son 45 minutos; 10:15 más 45 minutos llega a 11:00."),
            ex("Teo llega a la plaza a las 2:45 y se va a las 4:30. ¿Cuánto estuvo allí?", "1 hora y 45 minutos", "De 2:45 a 3:45 es 1 hora y de 3:45 a 4:30 son 45 minutos."),
        ],
    },
    context=[ex("El almuerzo empieza a la 1:00 y dura 45 minutos. Después hay un recreo de un cuarto de hora. ¿A qué hora termina el recreo?", "A las 2:00", "1:00 más 45 minutos es 1:45; más 15 minutos es 2:00.")],
    selfcheck=[
        ex("¿Qué hora será 2 horas después de las 3:15?", "5:15", "Se suman 2 horas y los minutos quedan igual."),
        arith("Una actividad va de las 6:10 a las 6:50. ¿Cuántos minutos dura?", "50-10", "Se restan los minutos de las dos horas."),
        ex("Una obra empieza a las 5:00 y dura media hora. ¿A qué hora termina?", "5:30", "Media hora son 30 minutos."),
    ],
    open_task=task(
        "Planifica una tarde con estas tres actividades seguidas: lectura de 30 minutos, juego de 1 hora y merienda de un cuarto de hora. Empieza a las 4:00. Escribe la hora de inicio y de término de cada actividad.",
        "Lectura: 4:00 a 4:30. Juego: 4:30 a 5:30. Merienda: 5:30 a 5:45. Cada actividad empieza donde termina la anterior.",
        ["empieza a las 4:00", "suma cada duración correctamente", "cada actividad empieza donde termina la anterior", "escribe las horas en formato digital"],
        ["tres líneas con inicio y término", "cálculos de apoyo"],
        ["olvidar los minutos al sumar", "pasar de 59 minutos sin cambiar de hora"],
        "Pide revisar con un reloj dibujado cada término. Reconoce que respete el orden.",
    ),
    reinforce="Anota la hora en que empiezas y terminas tu tarea hoy, y calcula cuánto duró.",
    extend="Calcula cuánto tiempo pasa desde las 7:45 hasta las 9:15 y explica los pasos.",
)
