"""Student material for 2.º básico Matemática, OA 17 (calendario) y OA 18 (horas y medias horas)."""
from __future__ import annotations

import calendar
import datetime as dt

from student_content_ma02_g import task
from student_lessons import arith, ex, register

OA17, OA18 = "MA02 OA 17", "MA02 OA 18"
YEAR = 2026
MESES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
LARGO = "Días de cada mes de 2026: enero 31, febrero 28, marzo 31, abril 30, mayo 31, junio 30, julio 31, agosto 31, septiembre 30, octubre 31, noviembre 30, diciembre 31."


def dia(month: int, day: int) -> str:
    return DIAS[dt.date(YEAR, month, day).weekday()]


def fecha(month: int, day: int) -> str:
    return f"{day} de {MESES[month]}"


def mas(month: int, day: int, n: int) -> tuple[int, int]:
    moved = dt.date(YEAR, month, day) + dt.timedelta(days=n)
    return moved.month, moved.day


def cal(month: int) -> str:
    """Month calendar as one line: rows are separated by « / », empty cells are «–»."""
    rows = []
    for week in calendar.Calendar(0).monthdayscalendar(YEAR, month):
        rows.append(" ".join(f"{d:>2}" if d else " –" for d in week))
    return f"Calendario de {MESES[month]} de {YEAR} (columnas: Lu Ma Mi Ju Vi Sa Do). " + " / ".join(rows) + "."


ABRIL, MAYO, JUNIO, AGOSTO = cal(4), cal(5), cal(6), cal(8)
assert dia(4, 1) == "miércoles" and dia(5, 1) == "viernes" and dia(8, 1) == "sábado"


# ================================================================ OA 17
register(
    OA17, 1,
    materials=f"Este cuaderno y un lápiz. {ABRIL} Cada fila es una semana.",
    use="Aprenderé a leer un calendario: mes, semana, día y fecha. Sirve para encontrar cuándo ocurre algo, como un cumpleaños o una fiesta.",
    prior=["Sé los días de la semana en orden.", "Sé leer números hasta 31."],
    explain=[
        "Un calendario muestra los días de un mes. Arriba está el nombre del mes y las columnas dicen el día de la semana: lunes, martes, miércoles y así hasta domingo. Cada fila es una semana, y una semana tiene 7 días.",
        "Un número del calendario es un día del mes. Pero para decir una fecha completa necesitas el número del día y el mes. Por ejemplo, 18 de abril. A veces también se dice el año, como 2026.",
        "Para encontrar un día, busca su columna para saber qué día de la semana es. Para encontrar «el segundo martes», mira la columna de los martes y toma el segundo número desde arriba.",
    ],
    vocab=[("calendario", "tabla que muestra los días de un mes"), ("semana", "7 días seguidos, una fila del calendario"), ("fecha", "día y mes, como 18 de abril"), ("fila", "línea de izquierda a derecha"), ("columna", "línea de arriba hacia abajo")],
    worked=[
        {"title": "Leer una fecha", "problem": "En el calendario de abril, ¿qué día de la semana es el 8 de abril?", "steps": ["Busco el número 8 en el calendario.", "Subo por su columna hasta el encabezado.", f"La columna dice {dia(4, 8)}."], "answer": f"El 8 de abril es {dia(4, 8)}"},
        {"title": "Segundo martes", "problem": "¿Cuál es la fecha del segundo martes de abril?", "steps": ["Busco la columna Ma, que es martes.", "Los martes de abril son 7, 14, 21 y 28.", "El segundo de la lista es 14."], "answer": "14 de abril"},
    ],
    mistakes=[
        {"wrong": "Decir que «el 12» es una fecha completa.", "why": "Se lee sólo el número del día.", "fix": "Una fecha necesita el día y el mes: 12 de abril."},
        {"wrong": "Confundir fila con columna y decir que una columna es una semana.", "why": "Se mezclan las direcciones del calendario.", "fix": "La fila (de lado a lado) es una semana; la columna (de arriba abajo) es un día de la semana."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos días tiene una semana?", "7", "Desde lunes hasta domingo hay siete días."),
            ex(f"En el calendario de abril, ¿en qué día de la semana cae el 1 de abril?", dia(4, 1), "Su número está en la columna del miércoles."),
            ex("En el calendario de abril, ¿qué número está justo debajo del 8?", "15", "Debajo hay un número de la misma columna, una semana después."),
        ],
        "understand": [
            ex("¿Qué dos datos forman una fecha, además del año?", "El número del día y el mes", "Con ambos se sabe cuándo ocurre."),
            ex("En «23 de abril», ¿cuál es el mes?", "Abril", "El mes es el nombre que viene después de «de»."),
            ex("¿Qué es una fila del calendario?", "Una semana", "Cada fila tiene siete días."),
        ],
        "apply": [
            ex("¿Qué día de la semana es el 11 de abril?", dia(4, 11), "Está en la columna del sábado."),
            ex("¿Cuál es la fecha completa del segundo martes de abril?", fecha(4, 14), "Los martes son 7, 14, 21 y 28; el segundo es 14."),
            ex("¿Cuántos domingos tiene abril?", "4", "Los domingos son 5, 12, 19 y 26."),
        ],
        "reason": [
            ex("Carla dice que el segundo viernes de abril es el 3. ¿Qué error comete?", "El 3 es el primer viernes; el segundo es el 10", "Los viernes de abril son 3, 10, 17 y 24."),
            ex("Mateo dice que habrá una fiesta el viernes 31 de abril. ¿Qué error comete?", "Abril sólo tiene 30 días; el 31 de abril no existe", "El último número del calendario de abril es 30."),
        ],
        "challenge": [
            ex("Escribe todas las fechas de abril que caen en jueves.", "2, 9, 16, 23 y 30 de abril", "Se cuenta de 7 en 7 desde el primer jueves."),
            ex("El último día de abril es jueves. ¿Qué día de la semana es el 1 de mayo?", dia(5, 1), "Después del jueves viene el viernes."),
        ],
    },
    context=[ex("La fiesta del curso es el tercer sábado de abril. ¿Cuál es la fecha?", fecha(4, 18), "Los sábados de abril son 4, 11, 18 y 25; el tercero es 18.")],
    selfcheck=[
        ex("¿Qué día de la semana es el 1 de abril?", "Miércoles", "Es la primera casilla con número, en la columna del miércoles."),
        ex("¿Cuántos días tiene abril, según el calendario?", "30", "El último número del calendario es 30."),
        ex("¿Cuál es la fecha del primer lunes de abril?", "6 de abril", "El primer lunes con número es el 6."),
    ],
    open_task=task(
        f"Usa el calendario de abril. {ABRIL} Elige tres fechas de abril y, para cada una, escribe qué día de la semana es y a qué fila del calendario pertenece (fila 1, 2, 3, 4 o 5). Escribe también la fecha del cuarto miércoles.",
        "Ejemplo: 9 de abril es jueves, fila 2. 20 de abril es lunes, fila 4. 29 de abril es miércoles, fila 5. El cuarto miércoles es el 22 de abril.",
        ["escribe tres fechas con día y mes", "indica el día de la semana correcto", "indica la fila", "encuentra el cuarto miércoles"],
        ["tres fechas", "día de la semana", "fila"],
        ["escribir sólo el número", "confundir fila y columna"],
        "Pide señalar con el dedo la casilla en el calendario. Reconoce cuando da la fecha completa.",
    ),
    reinforce="Mira el calendario de tu casa y encuentra el día de tu cumpleaños. Di el día de la semana.",
    extend="Busca en el calendario de abril cuántos viernes hay y escribe sus fechas.",
)

register(
    OA17, 2,
    materials=f"Este cuaderno y un lápiz. {MAYO}",
    use="Aprenderé a ir una semana hacia adelante o hacia atrás en el calendario. Sirve para saber cuándo es una actividad que ocurre cada semana.",
    prior=["Sé que una semana tiene 7 días.", "Sé leer una fecha en el calendario."],
    explain=[
        "Una semana después es 7 días después. En el calendario, baja una fila y quedas en el mismo día de la semana. Por ejemplo, si hoy es lunes 4, una semana después es lunes 11.",
        "Para ir una semana antes, sube una fila. Desde el miércoles 20, una semana antes es el miércoles 13. Siempre se suma 7 para avanzar y se resta 7 para retroceder.",
        "Dos semanas son 14 días. Entonces, dos semanas después del lunes 4 es el lunes 18. Sin mirar el calendario puedes calcular con 7, 14 y 21, pero mirar la tabla te ayuda a comprobar.",
    ],
    vocab=[("una semana después", "7 días más tarde, el mismo día de la semana"), ("una semana antes", "7 días antes, el mismo día de la semana"), ("avanzar", "ir a una fecha posterior"), ("retroceder", "ir a una fecha anterior"), ("dos semanas", "14 días")],
    worked=[
        {"title": "Una semana después", "problem": "Hoy es miércoles 6 de mayo. ¿Qué fecha es una semana después?", "steps": ["Sumo 7 días: 6 + 7 = 13.", "En el calendario, bajo una fila desde el 6.", f"Llego al {dia(5, 13)} 13."], "answer": f"{dia(5, 13).capitalize()} 13 de mayo"},
        {"title": "Una semana antes", "problem": "Una reunión es el jueves 21 de mayo. ¿Qué fecha es una semana antes?", "steps": ["Resto 7 días: 21 − 7 = 14.", "En el calendario, subo una fila desde el 21.", "Llego al jueves 14."], "answer": "Jueves 14 de mayo"},
    ],
    mistakes=[
        {"wrong": "Decir que una semana después del 5 es el 6.", "why": "Se cuenta un día en vez de siete.", "fix": "Una semana son 7 días: 5 + 7 = 12."},
        {"wrong": "Cambiar el día de la semana al avanzar siete días.", "why": "No se nota que la semana vuelve al mismo día.", "fix": "Una semana después cae el mismo día de la semana."},
    ],
    tiers={
        "recovery": [
            arith("Hoy es 4 de mayo. ¿Qué número de día es una semana después?", "4+7", "Una semana son 7 días."),
            arith("Es el 20 de mayo. ¿Qué número de día fue una semana antes?", "20-7", "Se resta 7 para ir hacia atrás."),
            ex("Una semana después de un lunes, ¿qué día de la semana cae?", "Lunes", "Siete días después se vuelve al mismo día."),
        ],
        "understand": [
            ex("¿Cuántos días hay en dos semanas?", "14", "Dos veces siete."),
            ex("En el calendario, ¿hacia dónde te mueves para ir una semana después?", "Una fila hacia abajo", "Cada fila siguiente es una semana más tarde."),
            ex("¿Qué se hace con el número del día para ir una semana antes?", "Se resta 7", "Una semana antes son 7 días menos."),
        ],
        "apply": [
            ex("Hoy es jueves 7 de mayo. ¿Qué fecha es una semana después?", fecha(5, 14), "7 + 7 = 14 y sigue siendo jueves."),
            ex("La excursión es el viernes 29 de mayo. ¿Qué fecha es una semana antes?", fecha(5, 22), "29 − 7 = 22."),
            arith("El lunes 4 de mayo empieza un proyecto que dura dos semanas. ¿Qué número de día es el lunes en que termina?", "4+14", "Dos semanas son 14 días."),
        ],
        "reason": [
            ex("Pablo dice que una semana después del domingo 10 es el lunes 17. ¿Qué error comete?", "Una semana después es otro domingo, el 17", "Siete días después cae el mismo día de la semana."),
            ex("Lola quiere saber qué fecha es una semana antes del 3 de mayo, pero 3 − 7 no se puede. Abril tiene 30 días. ¿Qué fecha es?", "26 de abril", "Hacia atrás: 2 y 1 de mayo, y luego 30, 29, 28, 27 y 26 de abril."),
        ],
        "challenge": [
            ex("Un taller es todos los miércoles. Si el primero es el 6 de mayo, escribe las fechas de mayo en que hay taller.", "6, 13, 20 y 27 de mayo", "Se suma 7 cada vez."),
            ex("Hoy es el martes 12 de mayo. Abril tiene 30 días. ¿Qué fecha y día es dos semanas antes?", "Martes 28 de abril", "12 − 14 pasa a abril; abril tiene 30 días: 30 − 2 = 28."),
        ],
    },
    context=[ex("Sofía tiene clases de natación los lunes. Una clase fue el lunes 11 de mayo. ¿Qué fecha será la clase de la semana siguiente?", fecha(5, 18), "11 + 7 = 18.")],
    selfcheck=[
        ex("¿Qué fecha es una semana después del 12 de mayo?", "19 de mayo", "12 + 7 = 19."),
        ex("¿Cuántos días son tres semanas?", "21", "Tres veces siete."),
        ex("¿Qué fecha es una semana antes del 25 de mayo?", "18 de mayo", "25 − 7 = 18."),
    ],
    open_task=task(
        f"Usa el calendario de mayo. {MAYO} Hay una charla el miércoles 13 de mayo. Escribe la fecha de una semana antes, de una semana después y de dos semanas después. Para cada una escribe el día de la semana y muestra cómo lo calculaste.",
        "Una semana antes: miércoles 6 de mayo (13 − 7). Una semana después: miércoles 20 de mayo (13 + 7). Dos semanas después: miércoles 27 de mayo (13 + 14). Siempre es miércoles.",
        ["calcula tres fechas correctas", "indica el día de la semana", "muestra la suma o resta", "comprueba con el calendario"],
        ["tres fechas", "operaciones", "día de la semana"],
        ["sumar un día en vez de siete", "cambiar el día de la semana"],
        "Pide señalar las filas en el calendario. Reconoce cuando usa 7 y 14.",
    ),
    reinforce="Elige un día de esta semana y di qué fecha será una semana después, mirando tu calendario.",
    extend="Calcula qué fecha es tres semanas después del lunes 4 de mayo y comprueba con el calendario.",
)

register(
    OA17, 3,
    materials=f"Este cuaderno y un lápiz. {LARGO} {JUNIO}",
    use="Aprenderé a calcular fechas cuando el mes cambia. Sirve para saber, por ejemplo, qué día es tres días después del último día de un mes.",
    prior=["Sé avanzar una semana en el calendario.", "Sé el orden de los meses."],
    explain=[
        "Cada mes tiene un último día. Después de ese día empieza el mes siguiente con el 1. Por ejemplo, mayo termina el 31 y después viene el 1 de junio. No existe un «32 de mayo».",
        "Para avanzar días cuando cambia el mes, cuenta uno por uno: 30, 31, 1, 2. El mes cambia cuando pasas el último día. Mira cuántos días tiene el mes en la tabla del comienzo.",
        "Para retroceder pasa lo mismo al revés. Un día antes del 1 de junio es el 31 de mayo. Un día antes del 1 de enero es el 31 de diciembre del año anterior.",
    ],
    vocab=[("último día", "el número más alto de un mes"), ("mes siguiente", "el mes que viene después"), ("mes anterior", "el mes que viene antes"), ("cambiar de mes", "pasar del último día al 1 del otro mes"), ("avanzar", "ir hacia fechas más tarde")],
    worked=[
        {"title": "Cruzar el fin de mes", "problem": "¿Qué fecha es cuatro días después del 29 de mayo?", "steps": ["Mayo tiene 31 días.", "Cuento: 30, 31, 1 de junio, 2 de junio.", "Llego a junio."], "answer": "2 de junio"},
        {"title": "Retroceder al mes anterior", "problem": "¿Qué fecha es dos días antes del 1 de julio?", "steps": ["Un día antes del 1 de julio es el último día de junio.", "Junio tiene 30 días: es el 30 de junio.", "Otro día antes es el 29 de junio."], "answer": "29 de junio"},
    ],
    mistakes=[
        {"wrong": "Escribir «32 de mayo» al contar tres días después del 30 de mayo.", "why": "No se recuerda que mayo termina en 31.", "fix": "Después del 31 de mayo viene el 1 de junio."},
        {"wrong": "Pasar a otro mes sin cambiar el nombre del mes en la fecha.", "why": "Se cuentan los números y se olvida el mes.", "fix": "Al llegar al 1, escribe el nombre del mes siguiente."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué día viene después del 31 de mayo?", "1 de junio", "Mayo termina el 31."),
            ex("¿Cuántos días tiene junio?", "30", "Está en la tabla de días de cada mes."),
            ex("¿Qué día viene después del 30 de abril?", "1 de mayo", "Abril termina el 30."),
        ],
        "understand": [
            ex("¿Existe el 31 de junio?", "No", "Junio tiene 30 días."),
            ex("¿Por qué no existe el «32 de mayo»?", "Porque mayo termina el 31", "Después del último día empieza otro mes."),
            ex("¿Qué fecha es un día antes del 1 de junio?", "31 de mayo", "Es el último día del mes anterior."),
        ],
        "apply": [
            ex("¿Qué fecha es tres días después del 30 de noviembre?", "3 de diciembre", "Cuento 1, 2 y 3 de diciembre porque noviembre termina el 30."),
            ex("¿Qué fecha es dos días después del 30 de junio?", "2 de julio", "Junio termina el 30; después vienen 1 y 2 de julio."),
            ex("¿Qué fecha es dos días después del 27 de febrero de 2026?", "1 de marzo", "Febrero tiene 28 días: 28 de febrero y 1 de marzo."),
        ],
        "reason": [
            ex("Dani cuenta cuatro días después del 29 de septiembre y escribe «3 de septiembre». ¿Qué error comete?", "Septiembre termina el 30; es el 3 de octubre", "Después del 30 se pasa al 1 de octubre."),
            ex("Fran dice que tres días antes del 2 de mayo es el −1 de mayo. ¿Cómo se corrige?", "Es el 29 de abril", "Un día antes es 1 de mayo, luego 30 y 29 de abril."),
        ],
        "challenge": [
            ex("¿Qué fecha es una semana después del 28 de abril?", "5 de mayo", "28 + 7 = 35; 35 − 30 = 5, ya en mayo."),
            ex("Un curso empieza el 29 de mayo y dura cinco días contando el primero. ¿En qué fecha termina?", "2 de junio", "Los días son 29, 30, 31, 1 y 2."),
        ],
    },
    context=[ex("El libro debe devolverse tres días después del 28 de mayo. ¿Qué día es la devolución?", "31 de mayo", "28 + 3 = 31 y mayo tiene 31 días.")],
    selfcheck=[
        ex("¿Qué fecha viene después del 30 de septiembre?", "1 de octubre", "Septiembre tiene 30 días."),
        ex("¿Qué fecha es un día después del 31 de diciembre?", "1 de enero", "Termina el año y empieza enero."),
        ex("¿Qué fecha es dos días antes del 1 de agosto?", "30 de julio", "Julio termina el 31: 31 y luego 30."),
    ],
    open_task=task(
        f"Esta tabla muestra cuántos días tiene cada mes: {LARGO} Escribe las fechas pedidas mostrando el recorrido: a) cuatro días después del 28 de abril; b) tres días después del 30 de junio; c) dos días antes del 1 de agosto.",
        "a) 28 de abril + 4: 29, 30, 1 de mayo, 2 de mayo. Es el 2 de mayo. b) 30 de junio + 3: 1, 2 y 3 de julio. c) 1 de agosto − 2: 31 de julio y 30 de julio.",
        ["escribe las tres fechas correctas", "muestra el recorrido día por día", "usa el último día del mes de la tabla", "escribe el nombre del mes nuevo"],
        ["tres fechas", "recorrido escrito"],
        ["escribir «32 de mayo»", "olvidar cambiar el mes"],
        "Pide leer el recorrido en voz alta. Reconoce cuando consulta los días del mes en la tabla.",
    ),
    reinforce="Cuenta con tus dedos cuántos días faltan para que termine este mes y qué fecha es después.",
    extend="Calcula qué fecha es 10 días después del 25 de junio y cómo cruzaste el mes.",
)

register(
    OA17, 4,
    materials=f"Este cuaderno y un lápiz. {LARGO} {cal(8)}",
    use="Aprenderé a usar un calendario para ordenar actividades y contar cuántos días hay entre ellas. Sirve para planificar tareas, paseos y cumpleaños.",
    prior=["Sé avanzar y retroceder días en el calendario.", "Sé cruzar el fin de mes."],
    explain=[
        "Un calendario sirve para planificar. Puedes ordenar actividades de la primera a la última mirando el mes y el día. Primero va el mes más temprano; si el mes es el mismo, va el día más pequeño.",
        "Por ejemplo, 29 de julio es antes que 3 de agosto, aunque 29 sea más grande que 3. Lo importante es el mes: julio viene antes que agosto.",
        "Para saber cuántos días hay entre dos fechas del mismo mes, resta los números. Del 3 al 12 de agosto pasan 9 días, porque 12 − 3 = 9. Si cambia el mes, cuenta hasta el fin de mes y luego suma los días del mes siguiente.",
    ],
    vocab=[("ordenar fechas", "ponerlas de la más temprana a la más tardía"), ("primero", "ocurre antes"), ("después", "ocurre más tarde"), ("entre", "los días que pasan de una fecha a otra"), ("planificar", "decidir qué se hará y cuándo")],
    worked=[
        {"title": "Ordenar fechas", "problem": "Ordena de la más temprana a la más tardía: 12 de agosto, 29 de julio y 3 de agosto.", "steps": ["Miro primero el mes: julio viene antes que agosto.", "29 de julio es la primera.", "Entre 3 y 12 de agosto, el 3 es antes.", "Orden: 29 de julio, 3 de agosto, 12 de agosto."], "answer": "29 de julio, 3 de agosto, 12 de agosto"},
        {"title": "Días entre fechas", "problem": "El paseo es el 3 de agosto y la feria es el 12 de agosto. ¿Cuántos días pasan entre ellos?", "steps": ["Es el mismo mes: resto los números.", "12 − 3 = 9.", "Pasan 9 días."], "answer": "9 días"},
    ],
    mistakes=[
        {"wrong": "Decir que 29 de julio es después que 3 de agosto porque 29 es mayor que 3.", "why": "Se comparan sólo los números del día.", "fix": "Compara primero el mes; el día decide sólo si el mes es el mismo."},
        {"wrong": "Restar 12 − 3 y decir que pasan 15 días.", "why": "Se suma en vez de restar.", "fix": "Para saber cuántos días hay entre dos fechas del mismo mes, resta."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué fecha es antes: 5 de agosto o 9 de agosto?", "5 de agosto", "Es el mismo mes y 5 es menor que 9."),
            ex("¿Qué fecha es después: 20 de agosto o 14 de agosto?", "20 de agosto", "Es el mismo mes y 20 es mayor que 14."),
            arith("El taller empieza el 4 de agosto y termina el 10 de agosto. ¿Cuántos días pasan entre ambas fechas?", "10-4", "Es el mismo mes: se resta."),
        ],
        "understand": [
            ex("Para ordenar fechas, ¿qué se compara primero: el día o el mes?", "El mes", "Un mes más temprano gana al día más pequeño."),
            ex("¿Cuál va antes: 30 de julio o 2 de agosto?", "30 de julio", "Julio viene antes que agosto."),
            ex("¿Qué operación se usa para los días entre dos fechas del mismo mes?", "Resta", "Se quita la fecha menor a la mayor."),
        ],
        "apply": [
            ex("Ordena de la más temprana a la más tardía: 25 de agosto, 8 de agosto y 17 de agosto.", "8, 17 y 25 de agosto", "Todos son de agosto y se ordenan por el día."),
            ex("El cumpleaños de Ema es el 9 de agosto y el de Hugo es el 23 de agosto. ¿Cuántos días hay entre los dos?", "14", "23 − 9 = 14."),
            ex("Ordena de la más temprana a la más tardía: 2 de septiembre, 28 de agosto y 31 de julio.", "31 de julio, 28 de agosto, 2 de septiembre", "Se ordena primero por mes."),
        ],
        "reason": [
            ex("Pía dice que 1 de septiembre es antes que 28 de agosto porque 1 es menor que 28. ¿Qué error comete?", "Comparó sólo el día; septiembre viene después que agosto", "El mes decide primero."),
            ex("Rolo dice que entre el 5 y el 20 de agosto hay 25 días. ¿Qué hizo mal?", "Sumó en vez de restar; son 15 días", "20 − 5 = 15."),
        ],
        "challenge": [
            ex("El 29 de julio empieza una tarea y se entrega el 3 de agosto. ¿Cuántos días pasan entre las dos fechas?", "5", "Del 29 al 31 de julio hay 2 días, y hasta el 3 de agosto 3 más: 2 + 3 = 5."),
            ex("Planifica: ir al museo el 20 de agosto, comprar entradas una semana antes. ¿Qué fecha compras?", "13 de agosto", "20 − 7 = 13."),
        ],
    },
    context=[ex("Una agenda dice: lunes 3 de agosto, entrega de dibujo; jueves 13 de agosto, feria del curso. ¿Cuántos días hay entre ambas fechas?", "10", "13 − 3 = 10.")],
    selfcheck=[
        ex("¿Qué fecha va primero: 15 de agosto o 11 de agosto?", "11 de agosto", "El mismo mes y 11 es menor que 15."),
        ex("¿Cuántos días hay entre el 6 y el 18 de agosto?", "12", "18 − 6 = 12."),
        ex("¿Qué va primero: 1 de agosto o 31 de julio?", "31 de julio", "Julio viene antes que agosto."),
    ],
    open_task=task(
        f"{cal(8)} Planifica tu mes de agosto con estas tres actividades: lectura de cuento el 4 de agosto, ensayo el 11 de agosto y presentación el 18 de agosto. Ordénalas, escribe qué día de la semana es cada una y cuántos días hay entre el ensayo y la presentación.",
        f"Orden: 4 de agosto ({dia(8, 4)}), 11 de agosto ({dia(8, 11)}), 18 de agosto ({dia(8, 18)}). Entre el ensayo y la presentación hay 7 días, una semana.",
        ["ordena las fechas correctamente", "escribe el día de la semana de cada una", "calcula 7 días", "usa el calendario"],
        ["orden", "días de la semana", "cálculo"],
        ["ordenar por el número sin mirar el mes", "sumar en vez de restar"],
        "Pide mostrar en el calendario cada actividad. Reconoce la explicación de por qué hay 7 días.",
    ),
    reinforce="Escribe tres actividades de tu semana y ponlas en orden con sus fechas.",
    extend="Elige dos fechas de meses distintos y calcula cuántos días hay entre ellas contando hasta el fin del primer mes.",
)

# ================================================================ OA 18
register(
    OA18, 1,
    materials="Papel y lápiz. Cada ejercicio trae las horas escritas como las muestra un reloj digital, por ejemplo 09:00.",
    use="Aprenderé a leer y escribir horas en punto en un reloj digital. Sirve para saber a qué hora empieza el colegio o un programa.",
    prior=["Sé leer números hasta 24.", "Sé qué es la mañana, la tarde y la noche."],
    explain=[
        "Un reloj digital muestra la hora con números. A la izquierda de los dos puntos está la hora, y a la derecha están los minutos. En 09:00, la hora es 9 y los minutos son 00.",
        "Cuando los minutos son :00, la hora está en punto. 09:00 se lee «las nueve en punto». 04:00 se lee «las cuatro en punto». Los dos ceros dicen que acaba de empezar esa hora.",
        "Algunos relojes digitales siguen contando después del mediodía. Así, 13:00 son la una de la tarde, 14:00 son las dos de la tarde, 15:00 las tres de la tarde y 18:00 las seis de la tarde. Para pasar una hora de la tarde a la forma corta, resta 12: 16:00 es 16 − 12 = 4, las cuatro de la tarde. Para escribirla, suma 12: las cinco de la tarde son 5 + 12 = 17, o sea 17:00.",
    ],
    vocab=[("reloj digital", "reloj que muestra la hora con números"), ("hora", "el número a la izquierda de los dos puntos"), ("minutos", "el número a la derecha de los dos puntos"), ("en punto", "cuando los minutos son :00"), ("dos puntos", "los dos puntos que separan la hora de los minutos")],
    worked=[
        {"title": "Leer una hora en punto", "problem": "Un reloj digital muestra 07:00. ¿Qué hora es?", "steps": ["A la izquierda de los dos puntos está el 07.", "A la derecha están los minutos: 00.", "Es la hora siete y no pasa ningún minuto."], "answer": "Las siete en punto"},
        {"title": "Escribir una hora en punto", "problem": "Escribe en formato digital las cuatro en punto de la tarde.", "steps": ["Cuatro de la tarde es la hora 16 en formato digital de 24 horas.", "Escribo la hora a la izquierda: 16.", "Pongo dos puntos y 00 a la derecha."], "answer": "16:00"},
    ],
    mistakes=[
        {"wrong": "Leer 09:00 como «nueve cero cero».", "why": "No se entiende que :00 es «en punto».", "fix": "Lee las nueve en punto: no ha pasado ningún minuto."},
        {"wrong": "Escribir 4.00 en vez de 04:00.", "why": "Se usa un punto en vez de los dos puntos.", "fix": "Entre hora y minutos van dos puntos."},
    ],
    tiers={
        "recovery": [
            ex("Un reloj digital muestra 06:00. ¿Qué hora es?", "Las seis en punto", "Los minutos son 00."),
            ex("Escribe en formato digital las ocho en punto de la mañana.", "08:00", "La hora es 8 y los minutos 00."),
            ex("En 11:00, ¿cuál es la hora y cuáles son los minutos?", "La hora es 11 y los minutos son 00", "A la izquierda está la hora y a la derecha los minutos."),
        ],
        "understand": [
            ex("¿Qué indica :00 en un reloj digital?", "Que la hora está en punto", "No han pasado minutos de esa hora."),
            ex("¿Qué separan los dos puntos en un reloj digital?", "La hora de los minutos", "A un lado está la hora y al otro los minutos."),
            ex("¿Qué hora de la tarde es 15:00?", "Las tres de la tarde", "15 − 12 = 3."),
        ],
        "apply": [
            ex("Escribe en formato digital las tres en punto de la tarde, usando 24 horas.", "15:00", "Tres de la tarde es la hora 15."),
            ex("Una clase empieza a las 09:00. ¿Cómo se dice esa hora con palabras?", "Las nueve en punto", "La hora es 9 y los minutos 00."),
            ex("Escribe la hora de cierre de una tienda: seis de la tarde en punto, formato digital de 24 horas.", "18:00", "6 + 12 = 18."),
        ],
        "reason": [
            ex("Lalo dice que 05:00 y 17:00 son la misma hora porque ambas dicen cinco. ¿Está bien?", "No; 05:00 es de la mañana temprano y 17:00 es de la tarde", "17 es cinco de la tarde."),
            ex("Dani lee 12:00 como «las dos» porque ve el 2. ¿Qué error comete?", "Debe leer la hora completa: son las doce", "La hora es 12, no sólo el dígito 2."),
        ],
        "challenge": [
            ex("Una función empieza a las 16:00 y la salida es una hora después. ¿A qué hora es la salida?", "17:00", "16 + 1 = 17."),
            ex("Estás en el colegio de 08:00 a 13:00. ¿A qué hora de la tarde sales, en palabras?", "A la una de la tarde", "13 es la una de la tarde."),
        ],
    },
    context=[ex("El bus escolar pasa por mi casa a las 07:00. ¿Qué hora muestra el reloj digital cuando el bus llega?", "07:00", "Siete en punto se escribe 07:00.")],
    selfcheck=[
        ex("¿Cómo se lee 10:00?", "Las diez en punto", "La hora es 10 y no pasan minutos."),
        ex("¿Cómo se escribe «las doce en punto»?", "12:00", "La hora es 12 y los minutos 00."),
        ex("¿Qué hora es 14:00 de la tarde en palabras?", "Las dos de la tarde", "14 − 12 = 2."),
    ],
    open_task=task(
        "Esta es la agenda de Mía: se levanta a las 07:00, entra al colegio a las 08:00, almuerza a las 13:00 y llega a su casa a las 16:00. Lee cada hora en voz alta, escríbela con palabras (por ejemplo «las siete en punto») y dibuja cada reloj digital.",
        "07:00 son las siete en punto de la mañana. 08:00 son las ocho en punto. 13:00 es la una de la tarde. 16:00 son las cuatro de la tarde. Los relojes se dibujan con la hora a la izquierda, dos puntos y 00 a la derecha.",
        ["escribe con palabras las cuatro horas", "dibuja cuatro relojes digitales", "usa los dos puntos", "escribe 00 en los minutos"],
        ["cuatro frases", "cuatro relojes dibujados"],
        ["usar punto en vez de dos puntos", "no cambiar 13:00 a la una de la tarde"],
        "Pide leer en voz alta cada hora. Reconoce que relaciona 13:00 con la una de la tarde.",
    ),
    reinforce="Mira un reloj digital de tu casa y lee la hora en punto que más se acerca.",
    extend="Escribe en formato digital las horas en punto de tus tres comidas del día.",
)

register(
    OA18, 2,
    materials="Papel y lápiz. Las horas están escritas como en un reloj digital, por ejemplo 10:30.",
    use="Aprenderé a leer :30 como media hora después de la hora en punto. Sirve para saber cuándo empieza algo a las «y media».",
    prior=["Sé leer horas en punto como 09:00.", "Sé que una hora tiene 60 minutos."],
    explain=[
        "Los minutos del reloj digital cuentan cuánto ha pasado de una hora. Cuando marca :30, han pasado 30 minutos. Eso es media hora. Por ejemplo, 10:30 se lee «las diez y media».",
        "Una hora completa tiene 60 minutos. La mitad de 60 es 30. Por eso, media hora es 30 minutos. Desde 10:00 hasta 10:30 pasa media hora, y todavía no son las once.",
        "Si pasan otros 30 minutos desde 10:30, se llega a 11:00. Dos medias horas hacen una hora completa. Así, 30 minutos más 30 minutos son 60 minutos.",
    ],
    vocab=[("media hora", "30 minutos, la mitad de una hora"), ("y media", "30 minutos después de la hora en punto"), ("minutos", "partes pequeñas de una hora"), ("hora completa", "60 minutos"), ("reloj digital", "reloj que muestra números")],
    worked=[
        {"title": "Leer una hora y media", "problem": "El reloj digital muestra 07:30. ¿Qué hora es?", "steps": ["La hora es 07 y los minutos son 30.", "30 minutos es media hora.", "Son las siete y media."], "answer": "Las siete y media"},
        {"title": "Media hora después", "problem": "Son las 10:00. ¿Qué hora será media hora después?", "steps": ["Media hora son 30 minutos.", "Agrego 30 minutos a 10:00.", "El reloj marcará 10:30."], "answer": "10:30"},
    ],
    mistakes=[
        {"wrong": "Leer 08:30 como «ocho treinta horas».", "why": "No se relaciona :30 con media hora.", "fix": "Lee «las ocho y media»: pasó media hora desde las ocho."},
        {"wrong": "Decir que 10:30 ya son las once.", "why": "Se cree que :30 completa la hora.", "fix": "Faltan otros 30 minutos para las once."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos minutos es media hora?", "30 minutos", "Es la mitad de una hora de 60 minutos."),
            ex("¿Cómo se lee 09:30?", "Las nueve y media", "Los minutos :30 son media hora."),
            ex("Escribe en formato digital las cinco y media.", "05:30", "La hora es 5 y los minutos 30."),
        ],
        "understand": [
            ex("¿Cuántas medias horas hay en una hora?", "2", "Dos veces 30 minutos son 60."),
            ex("¿Qué indica :30 en un reloj digital?", "Que pasó media hora desde la hora en punto", "Han pasado 30 minutos."),
            ex("En 10:30, ¿ya son las once?", "No; faltan 30 minutos", "10:30 está a media hora de 11:00."),
        ],
        "apply": [
            ex("Un reloj digital marca 14:00. ¿Qué hora marcará media hora después?", "14:30", "Se agregan 30 minutos."),
            ex("Son las 07:30. ¿Qué hora será media hora después?", "08:00", "Con 30 minutos más se completa la hora."),
            ex("Una función empieza a las 17:00 y la entrada abre media hora antes. ¿A qué hora abre?", "16:30", "Media hora antes de las 17:00 es 16:30."),
        ],
        "reason": [
            ex("Tomás dice que 08:30 es la misma hora que 08:00. ¿Cuál es el error?", "08:30 es media hora después de 08:00", "Los minutos :30 muestran que pasó media hora."),
            ex("Ana dice que desde 12:00 hasta 13:00 pasan dos medias horas. ¿Es cierto?", "Sí", "Dos medias horas son una hora completa."),
        ],
        "challenge": [
            ex("Empiezas a leer a las 15:30 y paras dos medias horas después. ¿A qué hora paras?", "16:30", "Dos medias horas son 1 hora: 15:30 + 1 hora = 16:30."),
            ex("Si son las 09:30, ¿cuántos minutos faltan para las diez en punto?", "30", "De 09:30 a 10:00 pasa media hora."),
        ],
    },
    context=[ex("El recreo empieza a las 10:00 y dura media hora. ¿A qué hora termina el recreo?", "10:30", "10:00 más 30 minutos es 10:30.")],
    selfcheck=[
        ex("¿Cuántos minutos son media hora?", "30", "Es la mitad de 60."),
        ex("¿Cómo se lee 11:30?", "Las once y media", "Los minutos :30 son media hora."),
        ex("Escribe en formato digital las doce y media.", "12:30", "La hora es 12 y los minutos 30."),
    ],
    open_task=task(
        "Mira esta lista de actividades de Sofía: tarea a las 16:00, merienda a las 16:30, juego a las 17:30. Para cada actividad escribe la hora con palabras («las cuatro en punto», «las cuatro y media»...) y escribe cuánto pasa entre la tarea y la merienda.",
        "16:00 son las cuatro en punto de la tarde. 16:30 son las cuatro y media. 17:30 son las cinco y media. Entre la tarea y la merienda pasa media hora, 30 minutos.",
        ["escribe las tres horas con palabras", "usa «y media» en las horas :30", "explica que pasa media hora"],
        ["tres horas escritas", "cálculo de media hora"],
        ["leer :30 como treinta horas", "decir que 16:30 son las cinco"],
        "Pide explicar qué significa «y media». Reconoce cuando relaciona :30 con 30 minutos.",
    ),
    reinforce="Mira un reloj digital y busca una hora que termine en :30. Léela como «y media».",
    extend="Escribe cuatro horas «y media» de tu día, como la de la merienda o el estudio.",
)

register(
    OA18, 3,
    materials="Papel y lápiz. Las horas están escritas como en un reloj digital. Todas son del mismo día.",
    use="Aprenderé a ordenar horas y medias horas del mismo día. Sirve para saber qué ocurre primero en una agenda.",
    prior=["Sé leer horas en punto y horas y media.", "Sé comparar números de dos cifras."],
    explain=[
        "Para ordenar horas, mira primero el número de la izquierda de los dos puntos, que es la hora. La hora más pequeña ocurre antes. Por ejemplo, 08:30 es antes que 09:00.",
        "Si las dos horas tienen la misma hora, mira los minutos. Entre 12:00 y 12:30, ocurre primero 12:00, porque 00 es menor que 30. Las horas del mismo día se leen de la más temprana a la más tardía.",
        "También puedes usar una línea de tiempo: un dibujo con una línea y las horas marcadas de izquierda a derecha. Lo que está más a la izquierda ocurre antes.",
    ],
    vocab=[("ordenar horas", "ponerlas de la más temprana a la más tardía"), ("más temprano", "ocurre antes en el día"), ("más tarde", "ocurre después en el día"), ("línea de tiempo", "línea con horas marcadas de izquierda a derecha"), ("mismo día", "todas las horas ocurren en el mismo día")],
    worked=[
        {"title": "Ordenar tres horas", "problem": "Ordena de más temprano a más tarde: 09:30, 08:30 y 09:00.", "steps": ["Miro la hora de cada una: 09, 08 y 09.", "La más pequeña es 08:30, que va primero.", "Entre 09:00 y 09:30 las horas son iguales; miro los minutos: 00 < 30."], "answer": "08:30, 09:00, 09:30"},
        {"title": "Usar la línea de tiempo", "problem": "Marca 12:00, 12:30 y 11:30 en una línea de tiempo, de izquierda a derecha.", "steps": ["Pongo primero 11:30 a la izquierda.", "Después 12:00.", "Al final 12:30."], "answer": "11:30, 12:00, 12:30"},
    ],
    mistakes=[
        {"wrong": "Ordenar 12:30, 11:30 y 12:00 como 12:00, 12:30, 11:30.", "why": "Se mira primero los minutos y no la hora.", "fix": "Compara primero la hora; después los minutos."},
        {"wrong": "Decir que 09:00 es más tarde que 09:30 porque 0 es menor que 3.", "why": "Se invierte el orden.", "fix": "Mismo número de hora: los minutos mayores son más tarde."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es más temprano: 07:00 o 08:00?", "07:00", "La hora 7 es menor que la hora 8."),
            ex("¿Cuál es más tarde: 10:30 o 10:00?", "10:30", "Tienen la misma hora y 30 minutos son más que 00."),
            ex("¿Cuál ocurre primero: 15:00 o 14:30?", "14:30", "La hora 14 es menor que la 15."),
        ],
        "understand": [
            ex("Al ordenar horas del mismo día, ¿qué se compara primero?", "La hora, el número de la izquierda", "La hora pesa más que los minutos."),
            ex("Si dos horas son 13:00 y 13:30, ¿qué se compara?", "Los minutos", "La hora es la misma."),
            ex("En una línea de tiempo, ¿dónde se pone la hora más temprana?", "A la izquierda", "El tiempo avanza de izquierda a derecha."),
        ],
        "apply": [
            ex("Ordena de la más temprana a la más tardía: 11:30, 10:30 y 11:00.", "10:30, 11:00, 11:30", "Se ordenan por hora y luego por minutos."),
            ex("Ordena de la más temprana a la más tardía: 12:30, 11:30 y 12:00.", "11:30, 12:00, 12:30", "11 es menor que 12 y 00 es menor que 30."),
            ex("Ordena de la más tardía a la más temprana: 18:00, 17:30 y 18:30.", "18:30, 18:00, 17:30", "Se ordena al revés: primero la mayor."),
        ],
        "reason": [
            ex("Carla dice que 09:30 es más tarde que 10:00 porque 30 es mayor que 00. ¿Qué error comete?", "Comparó sólo los minutos; 10 es mayor que 9", "Se compara primero la hora."),
            ex("Beto ordenó 08:30, 08:00 y 07:30 como 08:00, 08:30, 07:30. ¿Qué hora debe ir primero?", "07:30", "La hora 7 es menor que la 8."),
        ],
        "challenge": [
            ex("Ordena de menor a mayor y escribe cuántas medias horas hay entre la primera y la última: 14:00, 15:30, 14:30.", "14:00, 14:30, 15:30; 3 medias horas", "De 14:00 a 15:30 hay 90 minutos, o tres medias horas."),
            ex("Hay 4 actividades: 13:00, 12:30, 14:00 y 13:30. ¿Cuántas ocurren antes de las 13:30?", "2", "Las que ocurren antes son 12:30 y 13:00."),
        ],
    },
    context=[ex("En la agenda de la tarde hay: 16:30 pintar, 15:30 tarea y 16:00 merienda. ¿Qué se hace primero?", "La tarea, a las 15:30", "15:30 es la hora más temprana de las tres.")],
    selfcheck=[
        ex("¿Cuál es más temprano: 10:30 o 11:00?", "10:30", "La hora 10 es menor que la 11."),
        ex("Ordena: 09:30, 09:00.", "09:00, 09:30", "Misma hora y 00 es menor que 30."),
        ex("¿Qué va primero: 12:30 o 12:00?", "12:00", "Con la misma hora, se compara los minutos."),
    ],
    open_task=task(
        "Esta es la agenda de un sábado: ver una película a las 11:30, desayunar a las 09:00, jugar a las 10:00, hacer las compras a las 09:30 y almorzar a las 13:00. Ordena todas las actividades de la más temprana a la más tardía y dibuja una línea de tiempo con las horas.",
        "Orden: desayunar 09:00, compras 09:30, jugar 10:00, película 11:30, almorzar 13:00. La línea de tiempo va de izquierda a derecha con esas horas.",
        ["ordena las cinco horas correctamente", "dibuja la línea de tiempo en el orden correcto", "escribe la actividad de cada hora", "nombra el criterio: primero la hora"],
        ["lista ordenada", "línea de tiempo"],
        ["ordenar sólo por los minutos", "poner una hora fuera de lugar"],
        "Pide leer la línea de tiempo en voz alta. Reconoce que explique primero la hora.",
    ),
    reinforce="Escribe tres horas de tu día en una tarjeta cada una y ordénalas de la más temprana a la más tardía.",
    extend="Ordena 07:30, 07:00, 08:30, 08:00, 06:30 y 06:00 de la más tardía a la más temprana.",
)

register(
    OA18, 4,
    materials="Papel y lápiz. Todas las horas del problema están escritas. Para ayudarte, dibuja una línea de tiempo con las horas marcadas.",
    use="Aprenderé a resolver problemas con cambios de media hora. Sirve para saber cuándo termina o cuándo comenzó una actividad.",
    prior=["Sé que media hora son 30 minutos.", "Sé ordenar horas y medias horas."],
    explain=[
        "En un problema de horas, primero busca la hora que se conoce. Luego decide si debes avanzar (agregar media hora) o retroceder (quitar media hora). Una línea de tiempo te ayuda a ver el cambio.",
        "Si algo empieza a las 15:30 y dura media hora, termina a las 16:00. De 15:30 a 16:00 pasan 30 minutos. Cuando los minutos pasan de :30 a :00, la hora cambia al número siguiente.",
        "Si un taller termina a las 18:30 y duró media hora, empezó a las 18:00. Para retroceder media hora desde :30, los minutos pasan a :00 con la misma hora. Si retrocedes desde :00, la hora baja y los minutos quedan en :30: media hora antes de las 19:00 es 18:30. Siempre revisa tu respuesta con la línea de tiempo.",
    ],
    vocab=[("avanzar media hora", "agregar 30 minutos"), ("retroceder media hora", "quitar 30 minutos"), ("duración", "cuánto tiempo dura algo"), ("comenzar", "empezar"), ("terminar", "acabar")],
    worked=[
        {"title": "Hora de término", "problem": "Una clase empieza a las 15:30 y dura media hora. ¿A qué hora termina?", "steps": ["Dibujo 15:30 en la línea de tiempo.", "Avanzo 30 minutos.", "Los minutos llegan a :00 y la hora sube a 16."], "answer": "16:00"},
        {"title": "Hora de inicio", "problem": "Un taller termina a las 18:30 y duró media hora. ¿A qué hora empezó?", "steps": ["Marco 18:30 en la línea de tiempo.", "Retrocedo 30 minutos.", "Los minutos pasan a :00 con la misma hora."], "answer": "18:00"},
    ],
    mistakes=[
        {"wrong": "Escribir que desde 15:30 y media hora más se llega a 15:60.", "why": "No se cambia a la hora siguiente.", "fix": "30 minutos más 30 minutos son 60, es decir, una hora más: 16:00."},
        {"wrong": "Sumar la media hora en vez de restar al buscar la hora de inicio.", "why": "No se lee si se pide inicio o término.", "fix": "Para saber el inicio, retrocede desde la hora de término."},
    ],
    tiers={
        "recovery": [
            ex("Una película empieza a las 16:00 y dura media hora. ¿A qué hora termina?", "16:30", "Se agregan 30 minutos."),
            ex("Una clase termina a las 12:30 y duró media hora. ¿A qué hora empezó?", "12:00", "Se retrocede 30 minutos."),
            ex("Son las 09:30. ¿Qué hora es media hora después?", "10:00", "Los 30 minutos completan la hora."),
        ],
        "understand": [
            ex("Para saber la hora de término, ¿se avanza o se retrocede?", "Se avanza", "Termina después de comenzar."),
            ex("Para saber la hora de inicio desde la hora de término, ¿se avanza o se retrocede?", "Se retrocede", "El inicio ocurre antes."),
            ex("¿Cuántos minutos hay entre 17:00 y 17:30?", "30", "Es media hora."),
        ],
        "apply": [
            ex("El recreo empieza a las 10:30 y dura media hora. ¿A qué hora termina?", "11:00", "10:30 más 30 minutos llega a las 11."),
            ex("El almuerzo termina a las 13:30 y duró media hora. ¿A qué hora comenzó?", "13:00", "13:30 menos 30 minutos."),
            ex("Una visita al museo empieza a las 14:30 y dura dos medias horas. ¿A qué hora termina?", "15:30", "Dos medias horas son una hora."),
        ],
        "reason": [
            ex("Mara dice que 17:30 más media hora es 17:60. ¿Cómo se corrige?", "Es 18:00", "60 minutos forman una hora más."),
            ex("Joel dice que una actividad que termina a las 19:00 y duró media hora empezó a las 19:30. ¿Qué error comete?", "Sumó en vez de restar; empezó a las 18:30", "Antes de las 19:00 es 18:30."),
        ],
        "challenge": [
            ex("Un cuento empieza a las 20:00 y dura media hora. Después hay media hora para dormir. ¿A qué hora se duerme el niño?", "21:00", "20:00 más 30 minutos y 30 minutos más."),
            ex("Luisa sale del colegio a las 13:00. Tarda media hora en llegar a casa y media hora en almorzar. ¿A qué hora termina de almorzar?", "14:00", "Dos medias horas son una hora."),
        ],
    },
    context=[ex("El bus sale a las 07:30 y el viaje dura media hora. ¿A qué hora llega al colegio?", "08:00", "07:30 más media hora es 08:00.")],
    selfcheck=[
        ex("Si empieza a las 11:30 y dura media hora, ¿cuándo termina?", "12:00", "11:30 más 30 minutos."),
        ex("Si termina a las 14:30 y duró media hora, ¿cuándo empezó?", "14:00", "14:30 menos 30 minutos."),
        ex("¿Cuántos minutos pasan entre 08:00 y 09:00?", "60", "Una hora completa son 60 minutos."),
    ],
    open_task=task(
        "Resuelve estos tres problemas con una línea de tiempo: 1) La clase de arte empieza a las 10:30 y dura media hora. ¿A qué hora termina? 2) El juego termina a las 17:30 y duró media hora. ¿A qué hora empezó? 3) La visita empieza a las 12:00 y dura dos medias horas. ¿A qué hora termina? Explica cuál operación hiciste en cada uno.",
        "1) 10:30 + 30 minutos = 11:00. 2) 17:30 − 30 minutos = 17:00. 3) 12:00 + 2 medias horas = 13:00. En 1 y 3 avancé, en 2 retrocedí.",
        ["resuelve los tres problemas correctamente", "dibuja la línea de tiempo", "dice si avanzó o retrocedió", "escribe horas en formato digital"],
        ["tres respuestas", "línea de tiempo", "explicación"],
        ["escribir :60", "restar en vez de sumar"],
        "Pide mostrar en la línea de tiempo el salto de 30 minutos. Reconoce la decisión de avanzar o retroceder.",
    ),
    reinforce="Elige una actividad de tu casa que dure media hora y escribe cuándo empieza y cuándo termina.",
    extend="Inventa un problema con una actividad que dure tres medias horas y resuélvelo con una línea de tiempo.",
)
