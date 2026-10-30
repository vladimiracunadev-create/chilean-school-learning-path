"""Material del estudiante de 1.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (calendario) y OA 02 (tiempo cotidiano)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1, OA2 = "HI01 OA 01", "HI01 OA 02"

SEP = ("Calendario de septiembre de 2025. Lunes: 1, 8, 15, 22, 29. Martes: 2, 9, 16, 23, 30. Miércoles: 3, 10, 17, 24. "
       "Jueves: 4, 11, 18, 25. Viernes: 5, 12, 19, 26. Sábado: 6, 13, 20, 27. Domingo: 7, 14, 21, 28.")

# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Lápiz y papel. Los nombres de los días están escritos en cada ejercicio; puedes mirar un calendario de tu casa, si hay uno.",
    use="Aprenderé a decir los siete días de la semana en orden y a saber qué día viene antes y cuál después. Sirve para planear qué hago cada día.",
    prior=["Sé que cada día tiene un nombre.", "Sé contar hasta 10."],
    explain=[
        "La semana tiene siete días y siempre van en el mismo orden: lunes, martes, miércoles, jueves, viernes, sábado y domingo. En los calendarios de Chile, la semana empieza en lunes y termina en domingo.",
        "Después del domingo no termina nada: empieza otra vez el lunes. Por eso decimos que la semana se repite. Los días de clases son de lunes a viernes. El sábado y el domingo forman el fin de semana.",
        "Para saber qué día viene después, di los nombres en orden. Si hoy es martes, mañana es miércoles. Si hoy es lunes, ayer fue domingo. Un calendario te ayuda a ver los siete días en una fila.",
    ],
    vocab=[("semana", "siete días seguidos"), ("lunes", "primer día de la semana en Chile"), ("fin de semana", "sábado y domingo"), ("se repite", "después del domingo vuelve el lunes"), ("calendario", "hoja que muestra los días ordenados")],
    worked=[
        {"title": "Qué día viene después", "problem": "Hoy es jueves. ¿Qué día es mañana?", "steps": ["Digo los días en orden: lunes, martes, miércoles, jueves, viernes.", "Después de jueves viene viernes."], "answer": "Mañana es viernes"},
        {"title": "La semana vuelve a empezar", "problem": "Hoy es domingo. ¿Qué día viene después?", "steps": ["El domingo es el último día de la semana.", "Después del domingo empieza otra semana.", "El primer día de la semana es lunes."], "answer": "Viene el lunes"},
    ],
    mistakes=[
        {"wrong": "Decir que después del domingo viene el sábado.", "why": "El sábado va antes del domingo y se mezclan los dos días del fin de semana.", "fix": "Di la fila completa: viernes, sábado, domingo, y luego lunes."},
        {"wrong": "Pensar que la semana termina y no sigue.", "why": "Se olvida que los días vuelven a empezar.", "fix": "Después del domingo viene siempre el lunes de una semana nueva."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué día viene después del martes?", "miércoles", "En la fila de los días, después del martes está el miércoles."),
            ex("Cuenta los días desde el lunes hasta el domingo. ¿Cuántos son?", "7", "Son lunes, martes, miércoles, jueves, viernes, sábado y domingo."),
            ex("¿Qué día de la semana está justo antes del domingo?", "sábado", "El sábado está justo antes del domingo."),
        ],
        "understand": [
            ex("Ordena de primero a último: viernes, lunes, jueves, martes, miércoles.", "lunes, martes, miércoles, jueves, viernes", "Es el orden en que ocurren dentro de la semana."),
            ex("¿Qué dos días forman el fin de semana?", "sábado y domingo", "Son los dos últimos días de la semana."),
            ex("Explica con tus palabras por qué decimos que la semana se repite.", "Porque después del domingo viene otra vez el lunes", "Los siete días vuelven a empezar en el mismo orden."),
        ],
        "apply": [
            ex("Hoy es miércoles. ¿Qué día será mañana?", "jueves", "El jueves viene justo después del miércoles."),
            ex("Hoy es sábado. ¿Qué día fue ayer?", "viernes", "Ayer es el día anterior, y antes del sábado está el viernes."),
            ex("Hoy es jueves. ¿Qué día será dentro de dos días?", "sábado", "Contando: viernes (1) y sábado (2)."),
        ],
        "reason": [
            ex("Lucía dice: «Después del sábado viene el lunes». ¿Qué día se le olvidó?", "domingo", "Entre el sábado y el lunes está el domingo."),
            ex("Hoy es domingo. ¿Qué día empieza la semana de clases y cuántos días faltan para eso?", "lunes; falta 1 día", "El lunes es mañana, un día después del domingo."),
        ],
        "challenge": [
            arith("Cada semana tiene 7 días. ¿Cuántos días hay en 3 semanas?", "7+7+7", "Se suman los 7 días de cada semana."),
            ex("Hoy es lunes. ¿Qué día será dentro de 10 días?", "jueves", "Dentro de 7 días vuelve a ser lunes; faltan 3 más: martes, miércoles, jueves."),
        ],
    },
    context=[ex("Mateo va al taller de dibujo los martes y los jueves. Hoy es lunes. ¿En cuántos días va por primera vez al taller?", "1 día", "Mañana es martes, el primer día del taller.")],
    selfcheck=[
        ex("¿Cuál es el primer día de la semana en un calendario chileno?", "lunes", "Los calendarios de Chile empiezan la semana en lunes."),
        ex("Si hoy es viernes, ¿qué día es mañana?", "sábado", "El sábado viene justo después del viernes."),
        ex("¿Qué día viene después del domingo?", "lunes", "Empieza una semana nueva con el lunes."),
    ],
    open_task=task("Dibuja una tabla con los siete días en orden. Escribe al lado de cada día una actividad, usando estas ideas: ir a la escuela, jugar en la plaza, visitar a la abuela, ver una película, ordenar tu pieza, tomar once con la familia, descansar.", "Lunes: ir a la escuela. Martes: ordenar mi pieza. Miércoles: jugar en la plaza. Jueves: ir a la escuela. Viernes: ver una película. Sábado: visitar a la abuela. Domingo: descansar.", ["siete días", "orden correcto empezando en lunes", "una actividad por día"], ["tabla dibujada con los días"], ["saltarse un día", "empezar en otro día sin avisar"], "Pide que lea la tabla en voz alta y que diga qué día viene después de cada uno."),
    reinforce="Di los siete días en orden, en voz alta, tres veces seguidas sin equivocarte.",
    extend="Escribe cuántos días de clases y cuántos días de descanso tiene tu semana.",
)

register(
    OA1, 2,
    materials="Lápiz y papel. Los doce meses están escritos en cada ejercicio; puedes mirar un calendario de tu casa, si hay uno.",
    use="Aprenderé los doce meses del año en orden y qué estación de Chile corresponde a cada grupo. Sirve para saber cuánto falta para mi cumpleaños o las vacaciones.",
    prior=["Sé decir los siete días de la semana.", "Sé contar hasta 12."],
    explain=[
        "El año tiene doce meses y van siempre en este orden: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre y diciembre. Enero es el primero y diciembre es el último.",
        "Cada mes tiene entre 28 y 31 días. Abril, junio, septiembre y noviembre tienen 30 días. Febrero tiene 28 días, y 29 en un año bisiesto. Los demás meses tienen 31 días.",
        "Los meses se agrupan en estaciones. En Chile, más o menos, el verano es diciembre, enero y febrero; el otoño es marzo, abril y mayo; el invierno es junio, julio y agosto; y la primavera es septiembre, octubre y noviembre.",
    ],
    vocab=[("mes", "una parte del año con nombre propio"), ("año", "doce meses seguidos"), ("estación", "parte del año con un clima parecido: verano, otoño, invierno o primavera"), ("bisiesto", "año en que febrero tiene 29 días"), ("secuencia", "cosas puestas una después de otra en orden")],
    worked=[
        {"title": "El mes que sigue", "problem": "¿Qué mes viene después de marzo?", "steps": ["Digo los meses en orden: enero, febrero, marzo, abril.", "Después de marzo viene abril."], "answer": "abril"},
        {"title": "Un mes entre dos", "problem": "Un mes viene después de julio y antes de septiembre. ¿Cuál es?", "steps": ["Después de julio viene agosto.", "Después de agosto viene septiembre.", "Agosto queda entre julio y septiembre."], "answer": "agosto"},
    ],
    mistakes=[
        {"wrong": "Pensar que el año empieza en marzo porque ahí empiezan las clases.", "why": "El año escolar y el año del calendario no empiezan igual.", "fix": "El año del calendario empieza en enero y termina en diciembre."},
        {"wrong": "Cambiar de lugar dos meses al decir la fila.", "why": "Se memoriza sin mirar el orden.", "fix": "Recita los meses con un calendario al lado y marca cada mes que dices."},
    ],
    tiers={
        "recovery": [
            ex("Cuenta los meses desde enero hasta diciembre. ¿Cuántos son?", "12", "Van de enero a diciembre y son doce."),
            ex("¿Qué mes viene después de abril?", "mayo", "En la fila de los meses, mayo está justo después de abril."),
            ex("¿Cuál es el primer mes del año?", "enero", "El año empieza en enero."),
        ],
        "understand": [
            ex("Ordena de primero a último: mayo, enero, marzo, febrero, abril.", "enero, febrero, marzo, abril, mayo", "Es el orden en que llegan los meses durante el año."),
            ex("¿Cuál es el último mes del año?", "diciembre", "Diciembre cierra el año."),
            ex("En Chile, ¿en qué estación están junio, julio y agosto?", "invierno", "Son los meses de invierno, más o menos."),
        ],
        "apply": [
            ex("¿Qué mes viene justo antes de julio?", "junio", "Junio está al lado de julio, un lugar antes."),
            ex("Completa la fila: septiembre, octubre, ___, diciembre.", "noviembre", "Entre octubre y diciembre está noviembre."),
            ex("Escribe los dos meses del año cuyo nombre empieza con la letra j.", "junio y julio", "Son los únicos meses que empiezan con j."),
        ],
        "reason": [
            ex("Ana nació en el mes que viene después de julio y antes de septiembre. ¿En qué mes nació?", "agosto", "Entre julio y septiembre solo está agosto."),
            ex("Pedro dice que el invierno chileno es en diciembre. ¿Tiene razón?", "No; en Chile diciembre es más o menos verano", "El invierno es por junio, julio y agosto."),
        ],
        "challenge": [
            arith("Un año tiene 12 meses. ¿Cuántos meses hay en 2 años?", "12+12", "Se suman los 12 meses de cada año."),
            ex("Cuenta desde marzo hasta agosto, incluyendo los dos meses. ¿Cuántos meses son?", "6", "Marzo, abril, mayo, junio, julio y agosto son seis."),
        ],
    },
    context=[ex("En el colegio de Sofía las clases empiezan en marzo y las vacaciones de invierno son en julio. ¿Cuántos meses hay entre marzo y julio, sin contar esos dos?", "3", "En medio están abril, mayo y junio.")],
    selfcheck=[
        ex("¿Qué mes viene después de noviembre?", "diciembre", "Diciembre es el siguiente en la fila."),
        ex("¿Cuántos días tiene abril?", "30", "Abril es uno de los meses de 30 días."),
        ex("¿Qué estación empieza en septiembre, más o menos, en Chile?", "primavera", "Septiembre, octubre y noviembre son meses de primavera."),
    ],
    open_task=task("Dibuja una fila con los doce meses y colorea cada grupo de tres meses de un color según su estación en Chile: verano (diciembre, enero, febrero), otoño (marzo, abril, mayo), invierno (junio, julio, agosto) y primavera (septiembre, octubre, noviembre). Anota en qué mes es tu cumpleaños.", "Fila: enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre. Diciembre, enero y febrero en rojo. Marzo, abril y mayo en café. Junio, julio y agosto en azul. Septiembre, octubre y noviembre en verde. Mi cumpleaños: abril.", ["doce meses en orden", "cuatro grupos de tres", "una estación por color"], ["fila dibujada y coloreada", "mes del cumpleaños señalado"], ["empezar la fila en marzo", "poner diciembre en invierno"], "Pide que nombre qué mes viene antes y cuál después del mes de su cumpleaños."),
    reinforce="Recita los doce meses en orden mirando un calendario y marcando cada mes con un dedo.",
    extend="Escribe cuántos meses faltan desde tu cumpleaños hasta fin de año.",
)

register(
    OA1, 3,
    materials="Lápiz y papel. El calendario de septiembre está escrito en cada ejercicio. No necesitas nada más.",
    use="Aprenderé a leer un calendario: ubicar una fecha, decir qué día de la semana es y contar cuántos días faltan. Sirve para no olvidar cumpleaños ni actividades.",
    prior=["Sé decir los días de la semana.", "Sé contar hasta 30."],
    explain=[
        "Un calendario mensual muestra los días de un mes. Cada columna es un día de la semana: lunes, martes y así hasta domingo. Los números de una columna van de siete en siete porque pasa una semana entre uno y otro.",
        "Para ubicar una fecha busca el número. El día de la semana es el nombre de su columna. Si el 1 de septiembre es lunes, el 8 y el 15 también son lunes. Para saber cuántos días faltan, cuenta cada día que pasa o resta los números.",
        "Del 5 al 12 pasan 7 días, es decir, una semana. Del 18 al 24 pasan 6 días. Siempre se cuenta desde el día siguiente al de partida, porque el día de hoy ya está empezado.",
    ],
    vocab=[("fecha", "día, mes y año de un hecho"), ("columna", "fila hacia abajo en el calendario"), ("intervalo", "tiempo que pasa entre dos fechas"), ("mensual", "de un solo mes"), ("faltar", "ser el tiempo que queda hasta una fecha")],
    worked=[
        {"title": "Qué día de la semana es", "problem": f"{SEP} ¿Qué día de la semana es el 11?", "steps": ["Busco el 11 en el calendario.", "El 11 está en la columna del jueves."], "answer": "jueves"},
        {"title": "Contar días que faltan", "problem": f"{SEP} Hoy es 15. ¿Cuántos días faltan para el 19?", "steps": ["Después del 15 vienen 16, 17, 18 y 19.", "Cuento 4 días."], "answer": "4 días"},
    ],
    mistakes=[
        {"wrong": "Contar también el día de partida y decir que del 15 al 19 son 5 días.", "why": "Se cuenta el día de hoy como si ya hubiera pasado.", "fix": "Cuenta desde el día siguiente: 16, 17, 18, 19 son 4."},
        {"wrong": "Mirar la columna equivocada y decir el día de la semana de otro número.", "why": "Los números de al lado parecen cercanos.", "fix": "Pon el dedo en el número y sube hasta el nombre del día."},
    ],
    tiers={
        "recovery": [
            ex(f"{SEP} ¿Qué día de la semana es el 4 de septiembre?", "jueves", "El 4 está en la columna del jueves."),
            ex(f"{SEP} ¿Qué número tiene el primer domingo de septiembre?", "7", "El primer domingo es el 7."),
            ex(f"{SEP} ¿Cuántos lunes tiene septiembre?", "5", "Los lunes son 1, 8, 15, 22 y 29."),
        ],
        "understand": [
            ex(f"{SEP} ¿Qué día de la semana es el 18 de septiembre?", "jueves", "El 18 está en la columna del jueves."),
            ex(f"{SEP} ¿Cuántos días tiene septiembre?", "30", "El último número del calendario es 30."),
            ex(f"{SEP} ¿Qué fecha tiene el tercer viernes de septiembre?", "19", "Los viernes son 5, 12 y 19; el tercero es el 19."),
        ],
        "apply": [
            arith(f"{SEP} Del 5 al 12 de septiembre, ¿cuántos días pasan?", "12-5", "Se restan los números para saber el intervalo."),
            arith(f"{SEP} Luna cumple años el 24 y hoy es 18. ¿Cuántos días faltan?", "24-18", "Se resta la fecha de hoy a la del cumpleaños."),
            ex(f"{SEP} Hay clase de natación todos los miércoles. ¿Qué fechas tienen natación?", "3, 10, 17 y 24", "Son los números de la columna del miércoles."),
        ],
        "reason": [
            ex(f"{SEP} Un niño dice que el 19 de septiembre es sábado. ¿Es correcto?", "No; es viernes", "El 19 está en la columna del viernes."),
            ex(f"{SEP} Una amiga dice que la natación de los miércoles tendrá 5 clases en septiembre. ¿Tiene razón?", "No; son 4", "Los miércoles son solo 3, 10, 17 y 24."),
        ],
        "challenge": [
            ex(f"{SEP} Cuenta cuántos días de lunes a viernes tiene septiembre (no cuentes sábados ni domingos).", "22", "Lunes 5, martes 5, miércoles 4, jueves 4 y viernes 4 suman 22."),
            ex(f"{SEP} El último día de septiembre es el 30. ¿Qué día de la semana es el 1 de octubre?", "miércoles", "El 30 es martes y el día siguiente es miércoles."),
        ],
    },
    context=[arith(f"{SEP} En Chile las Fiestas Patrias son el 18 y el 19 de septiembre. Hoy es 15. ¿Cuántos días faltan para el 18?", "18-15", "Se resta la fecha de hoy a la fecha de la fiesta.")],
    selfcheck=[
        ex(f"{SEP} ¿Qué día de la semana es el 26 de septiembre?", "viernes", "El 26 está en la columna del viernes."),
        ex(f"{SEP} ¿Qué día de la semana es el 1 de septiembre?", "lunes", "El calendario parte con el 1 en la columna del lunes."),
        arith(f"{SEP} ¿Cuántos días pasan entre el 10 y el 17?", "17-10", "Es una semana completa."),
    ],
    open_task=task("Mira el calendario de septiembre escrito arriba. Escribe en una hoja la fecha y el día de la semana de estas tres cosas: el cumpleaños de Luna (24), una fiesta (18) y una visita al doctor (11). Después dibuja un círculo en cada número en tu hoja.", "Visita al doctor: jueves 11. Fiesta: jueves 18. Cumpleaños de Luna: miércoles 24. Entre la visita y la fiesta pasan 7 días.", ["tres fechas con día de la semana", "días correctos", "orden de las fechas de menor a mayor"], ["lista escrita con las tres fechas"], ["decir el día de la semana de otra columna", "cambiar los números"], "Pide que cuente en voz alta cuántos días hay entre dos de sus fechas."),
    reinforce="Mira un calendario de tu casa y di qué día de la semana es el 10 del mes que está abierto.",
    extend="Escribe cuántos lunes tiene el mes actual del calendario de tu casa.",
)

register(
    OA1, 4,
    materials="Lápiz y papel. Los datos de fechas y años están escritos en cada ejercicio; para tu tarea abierta ayuda mirar un calendario de tu casa.",
    use="Aprenderé a decir una fecha completa con día, mes y año, y a nombrar el año en curso. Sirve para firmar mis trabajos y ubicar cuándo ocurre algo.",
    prior=["Sé los días de la semana.", "Sé los doce meses."],
    explain=[
        "Una fecha completa tiene tres partes: el día, el mes y el año. Por ejemplo: «18 de septiembre de 2025». El año se escribe con cuatro números y nos dice en qué grupo de doce meses estamos.",
        "El año en curso es el año en que estás ahora. Cuando llega el 1 de enero, el año cambia. El año pasado es el que viene justo antes y el próximo es el que viene justo después. Un año normal tiene 365 días y un año bisiesto tiene 366.",
        "En Chile también escribimos las fechas con números y barras: 05/03/2025 se lee «5 de marzo de 2025». Primero va el día, luego el mes y al final el año. Mira siempre el año para no confundir fechas de distintos años.",
    ],
    vocab=[("fecha completa", "día, mes y año juntos"), ("año en curso", "el año en que estamos ahora"), ("año bisiesto", "año con 366 días, en que febrero tiene 29"), ("año pasado", "el año que viene justo antes"), ("próximo", "el que viene después")],
    worked=[
        {"title": "Leer una fecha con barras", "problem": "En un cuaderno dice 05/03/2025. ¿Cómo se lee con palabras?", "steps": ["Primero va el día: 5.", "Luego va el mes: 03 es marzo.", "Al final va el año: 2025."], "answer": "5 de marzo de 2025"},
        {"title": "Año pasado y próximo", "problem": "El año en curso es 2030. ¿Cuál es el año próximo?", "steps": ["El próximo es el que viene justo después.", "Después de 2030 viene 2031."], "answer": "2031"},
    ],
    mistakes=[
        {"wrong": "Escribir la fecha sin el año, por ejemplo «8 de julio».", "why": "Se piensa que el año es obvio.", "fix": "Agrega siempre el año: «8 de julio de 2025»."},
        {"wrong": "Leer 05/03/2025 como «3 de mayo».", "why": "Se confunde el orden de día y mes.", "fix": "En Chile primero va el día, luego el mes, y al final el año."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué mes empieza un año del calendario?", "enero", "El año empieza el 1 de enero."),
            ex("Escribe con palabras la fecha 09/10/2025.", "9 de octubre de 2025", "Primero el día 9, luego el mes 10 que es octubre, y el año."),
            ex("Si cuentas enero, febrero y los demás hasta diciembre, ¿cuántos meses forman un año?", "12", "El año tiene doce meses, de enero a diciembre."),
        ],
        "understand": [
            ex("¿Qué parte de la fecha «14 de agosto de 2027» dice el año?", "2027", "El año es el número de cuatro cifras al final."),
            ex("¿En qué fecha cambia el año en curso: el 31 de diciembre o el 1 de enero?", "el 1 de enero", "El año nuevo empieza el 1 de enero."),
            ex("Si una fecha dice 07/04/2025, ¿qué número es el día?", "7", "En Chile el primer número de la fecha es el día."),
        ],
        "apply": [
            ex("Escribe «1 de enero de 2026» con números y barras, con dos cifras para el día y el mes.", "01/01/2026", "Se escribe día, mes y año en ese orden."),
            ex("El año en curso es 2030. ¿Cuál fue el año pasado?", "2029", "El año pasado es el que viene justo antes: 2029."),
            ex("Una carta dice «martes 3 de junio de 2025». ¿Cuál es el mes?", "junio", "El mes es la palabra que está después de «de»."),
        ],
        "reason": [
            ex("Lola dice: «Mi cumpleaños es el 8 de julio». ¿Qué le falta para tener una fecha completa?", "El año", "La fecha completa lleva día, mes y año."),
            ex("En una foto dice 12/05/2023 y en otra 12/05/2024. ¿Son la misma fecha?", "No; cambia el año", "El día y el mes son iguales, pero los años son distintos."),
        ],
        "challenge": [
            ex("El año 2024 fue bisiesto, es decir, febrero tuvo 29 días. ¿Cuál es el próximo año bisiesto después de 2024?", "2028", "Los años bisiestos vienen de cuatro en cuatro."),
            arith("Un año normal tiene 365 días y uno bisiesto 366. ¿Cuántos días más tiene el bisiesto?", "366-365", "Se resta para ver la diferencia."),
        ],
    },
    context=[arith("Jaime empezó su cuaderno el 3 de marzo de 2025 y hoy es 3 de julio de 2025. ¿Cuántos meses han pasado?", "7-3", "Se resta el número del mes de marzo al de julio.")],
    selfcheck=[
        ex("Escribe con palabras la fecha 25/12/2025.", "25 de diciembre de 2025", "Día 25, mes 12 que es diciembre, año 2025."),
        ex("Si el año en curso es 2040, ¿qué año será el próximo?", "2041", "El próximo año viene justo después de 2040."),
        ex("¿Cuántos días tiene un año bisiesto?", "366", "Es un día más que el año normal por el 29 de febrero."),
    ],
    open_task=task("Mira el calendario o un papel con la fecha de hoy en tu casa. Escribe la fecha completa de hoy (día, mes y año) con palabras, luego con números y barras, y por último escribe cuál es el año pasado y cuál será el próximo. Si no encuentras la fecha de hoy, usa esta: 18 de septiembre de 2025.", "Hoy: 18 de septiembre de 2025. Con números: 18/09/2025. El año pasado fue 2024 y el próximo será 2026.", ["fecha completa con tres partes", "forma con números en el orden día, mes y año", "año pasado y próximo correctos"], ["hoja con las fechas escritas"], ["omitir el año", "cambiar el orden de día y mes"], "Pide que lea su fecha en voz alta y diga cuál de las tres partes es el año."),
    reinforce="Escribe con palabras tres fechas de tu calendario que te gusten, siempre con el año.",
    extend="Pregunta en qué año nació alguien de tu familia y escribe el año con un número de cuatro cifras.",
)

# ---------------------------------------------------------------- OA 02
register(
    OA2, 1,
    materials="Lápiz y papel. Las rutinas y tarjetas están escritas en cada ejercicio. No necesitas nada más.",
    use="Aprenderé a decir qué pasó antes y qué pasó después. Sirve para contar mi día en orden y para entender historias.",
    prior=["Sé las rutinas de mi día.", "Sé contar hasta 5."],
    explain=[
        "Antes y después dicen qué ocurre primero y qué ocurre más tarde. Si te pones las medias y luego los zapatos, las medias van antes y los zapatos después. Siempre comparamos dos cosas para usar estas palabras.",
        "Para ordenar varias cosas usamos las palabras primero, luego, después y al final. «Primero me despierto, luego me lavo la cara, después tomo desayuno y al final voy a la escuela». Cada palabra marca un lugar en la fila del tiempo.",
        "Para saber qué va antes, pregúntate qué debe estar hecho para poder hacer lo otro. Para plantar una semilla, primero debes hacer un hoyo; después puedes taparla. Si cambias el orden, la actividad no sale bien.",
    ],
    vocab=[("antes", "pasó primero, antes que otra cosa"), ("después", "pasa más tarde, luego de otra cosa"), ("primero", "lo que va al comienzo"), ("al final", "lo que va último"), ("orden", "el lugar de cada cosa en la fila")],
    worked=[
        {"title": "Antes de salir", "problem": "Camila se puso la chaqueta y después salió a la calle. ¿Qué hizo antes de salir?", "steps": ["Salió después de otra cosa.", "Lo primero que hizo fue ponerse la chaqueta."], "answer": "Se puso la chaqueta"},
        {"title": "Ordenar una rutina", "problem": "Ordena estas tarjetas de la mañana: A) tomar desayuno, B) despertarse, C) ir a la escuela.", "steps": ["Primero te despiertas: B.", "Luego tomas desayuno: A.", "Al final vas a la escuela: C."], "answer": "B, A, C"},
    ],
    mistakes=[
        {"wrong": "Poner el zapato antes que la media.", "why": "Se mira solo una cosa y no se piensa qué debe estar hecho antes.", "fix": "Pregúntate: ¿qué necesito tener listo para poder hacer esto?"},
        {"wrong": "Usar «antes» y «después» al revés.", "why": "Las dos palabras se parecen mucho.", "fix": "Antes es lo primero; después es lo que viene luego."},
    ],
    tiers={
        "recovery": [
            ex("Primero abres la puerta y después entras a la sala. ¿Qué haces después de abrir la puerta?", "entras a la sala", "Entrar es lo que viene después."),
            ex("Camila se puso la chaqueta y después salió a la calle. ¿Qué hizo primero?", "se puso la chaqueta", "La chaqueta va antes de salir."),
            ex("¿Qué va antes de comer: lavarte las manos o lavarte los dientes de la noche?", "lavarte las manos", "Las manos se lavan antes de comer para tenerlas limpias."),
        ],
        "understand": [
            ex("Ordena la noche: A) dormir, B) cenar, C) lavarse los dientes.", "B, C, A", "Se cena, luego se lavan los dientes y al final se duerme."),
            ex("¿Cuál de estas palabras sirve para decir que algo viene luego: antes, después o primero?", "después", "Después marca lo que viene más tarde."),
            ex("Explica por qué las medias van antes que los zapatos.", "Porque los zapatos se ponen encima de las medias", "Para ponerse los zapatos las medias ya deben estar puestas."),
        ],
        "apply": [
            ex("Ordena los pasos para hacer un sándwich: A) poner queso, B) tomar dos panes, C) cerrar el sándwich.", "B, A, C", "Primero van los panes, luego el queso y al final se cierra."),
            ex("Ordena los pasos para plantar una semilla: A) regar, B) hacer un hoyo en la tierra, C) tapar la semilla con tierra.", "B, C, A", "El hoyo va primero, luego se tapa y después se riega."),
            ex("Ordena lo que le pasó a Ana: A) llegó al colegio, B) tomó la micro, C) se despertó.", "C, B, A", "Primero despertó, luego viajó y al final llegó."),
        ],
        "reason": [
            ex("Tomás escribió: «Primero me acosté, después me lavé los dientes y al final cené». ¿Está bien ordenado?", "No; primero cena, luego se lava los dientes y al final se acuesta", "Se cena antes de lavar los dientes y se duerme al final."),
            ex("Hay dos fotos: en una hay un balde con arena y en la otra un castillo de arena terminado. ¿Cuál foto es de antes?", "la del balde con arena", "Primero se junta la arena y después se arma el castillo."),
        ],
        "challenge": [
            ex("Ordena una fiesta: A) comer torta, B) llegan los invitados, C) soplar las velas, D) cantar para el cumpleañero.", "B, D, C, A", "Llegan, cantan, soplan las velas y después comen torta."),
            ex("En un cuento una oruga come hojas, luego hace un capullo y después sale una mariposa. ¿Qué pasa justo antes de que salga la mariposa?", "la oruga hace un capullo", "El capullo está justo antes de la mariposa."),
        ],
    },
    context=[ex("En la pizarra de la sala dice: 1) entrar, 2) saludar, 3) trabajar, 4) recreo. ¿Qué actividad va justo después de saludar?", "trabajar", "Está en el número 3, después del 2.")],
    selfcheck=[
        ex("Si te pones el casco y después andas en bicicleta, ¿qué va antes?", "ponerse el casco", "El casco se pone para proteger antes de salir."),
        ex("Completa: «Primero me mojo las manos, luego me pongo ___ y al final me enjuago».", "jabón", "Para lavarse las manos se usa jabón antes de enjuagar."),
        ex("¿Qué palabra marca lo que va último en una fila de acciones?", "al final", "Al final es la palabra para el último lugar."),
    ],
    open_task=task("Elige una de estas rutinas y dibuja cuatro viñetas en orden, con la palabra primero, luego, después o al final bajo cada una: (a) lavarte los dientes antes de dormir (poner pasta, mojar el cepillo, cepillar, enjuagar); (b) hacer un jugo (lavar la fruta, cortarla, exprimirla, tomarlo).", "Rutina (a): Primero pongo pasta en el cepillo. Luego lo mojo. Después me cepillo. Al final me enjuago.", ["cuatro viñetas en orden", "usa primero, luego, después y al final", "orden lógico"], ["dibujos de cuatro viñetas con palabras"], ["cambiar el orden", "repetir dos veces la misma palabra"], "Pide que explique por qué una viñeta va antes de otra."),
    reinforce="Cuenta en voz alta lo que hiciste esta mañana usando primero, luego y al final.",
    extend="Inventa una rutina de cuatro pasos para tu familia y escríbela con palabras de orden.",
)

register(
    OA2, 2,
    materials="Lápiz y papel. El horario de la semana de un niño está escrito en cada ejercicio.",
    use="Aprenderé a ubicar actividades como ayer, hoy o mañana respecto del día presente. Sirve para recordar lo que hice y planear lo que haré.",
    prior=["Sé los días de la semana.", "Sé qué es antes y después."],
    explain=[
        "Hoy es el día en que estás. Ayer es el día que pasó justo antes de hoy y mañana es el día que llega justo después. Si hoy es miércoles, ayer fue martes y mañana será jueves.",
        "Hay otras palabras parecidas: anteayer fue hace dos días y pasado mañana será dentro de dos días. Con las fechas se cuenta igual: si hoy es 15 de abril, ayer fue 14 y mañana será 16.",
        "Una actividad que ya ocurrió está en el pasado. La que ocurre ahora está en el presente. La que va a ocurrir está en el futuro. Cada día que pasa, hoy cambia de lugar y también cambian ayer y mañana.",
    ],
    vocab=[("ayer", "el día que pasó justo antes de hoy"), ("hoy", "el día en que estamos"), ("mañana", "el día que llega justo después de hoy"), ("pasado mañana", "dentro de dos días"), ("presente", "lo que pasa ahora")],
    worked=[
        {"title": "Ayer y mañana", "problem": "Hoy es miércoles. ¿Qué día fue ayer y qué día será mañana?", "steps": ["Antes del miércoles está el martes: ayer.", "Después del miércoles está el jueves: mañana."], "answer": "Ayer fue martes y mañana será jueves"},
        {"title": "Ayer con fecha", "problem": "Hoy es 15 de abril. ¿Qué fecha fue ayer?", "steps": ["Ayer es un día antes.", "Un día antes del 15 es el 14."], "answer": "14 de abril"},
    ],
    mistakes=[
        {"wrong": "Decir que mañana es el día anterior a hoy.", "why": "Se confunden ayer y mañana.", "fix": "Ayer ya pasó; mañana todavía no llega."},
        {"wrong": "Creer que hoy es siempre el mismo día.", "why": "No se ve que cada día que pasa cambia el presente.", "fix": "Cuando termina el día, mañana se convierte en hoy."},
    ],
    tiers={
        "recovery": [
            ex("Hoy es martes. ¿Qué día será mañana?", "miércoles", "Mañana es el día que llega justo después."),
            ex("Hoy es viernes. ¿Qué día fue ayer?", "jueves", "Ayer es el día de justo antes."),
            ex("¿Cuál palabra significa el día en que estamos: ayer, hoy o mañana?", "hoy", "Hoy es el presente."),
        ],
        "understand": [
            ex("Ayer fue domingo. ¿Qué día es hoy?", "lunes", "Después del domingo viene el lunes."),
            ex("Mañana será sábado. ¿Qué día es hoy?", "viernes", "Hoy es el día antes del sábado."),
            ex("Explica qué significa «pasado mañana».", "Dentro de dos días", "Es el día que viene después de mañana."),
        ],
        "apply": [
            ex("Horario: lunes natación, martes música, miércoles abuela, jueves dibujo, viernes cine. Hoy es miércoles. ¿Qué actividad hubo ayer?", "música", "Ayer fue martes y ese día es la música."),
            ex("Horario: lunes natación, martes música, miércoles abuela, jueves dibujo, viernes cine. Hoy es miércoles. ¿Qué actividad habrá mañana?", "dibujo", "Mañana es jueves y ese día es el dibujo."),
            ex("Hoy es 30 de abril. ¿Qué fecha será mañana?", "1 de mayo", "Abril tiene 30 días, por eso mañana empieza mayo."),
        ],
        "reason": [
            ex("Hoy es lunes. Pedro dice que ayer fue sábado. ¿Qué día fue ayer en realidad?", "domingo", "El día anterior al lunes es el domingo."),
            ex("Hoy es 1 de marzo de 2025. ¿Qué fecha fue ayer? Febrero de 2025 tuvo 28 días.", "28 de febrero", "El día anterior al 1 de marzo es el último de febrero."),
        ],
        "challenge": [
            ex("Hoy es jueves. ¿Qué día fue anteayer, es decir, hace dos días?", "martes", "Hace dos días de un jueves cae un martes."),
            ex("Hoy es sábado. ¿Qué día será pasado mañana?", "lunes", "Contando: domingo (mañana) y lunes (pasado mañana)."),
        ],
    },
    context=[ex("Valentina tiene una prueba el viernes. Hoy es martes. ¿Qué día es pasado mañana y cuántos días faltan para la prueba?", "jueves; faltan 3 días", "Pasado mañana es jueves y para el viernes son miércoles, jueves y viernes.")],
    selfcheck=[
        ex("Si hoy es lunes 7, ¿qué fecha será mañana?", "martes 8", "Mañana es un día después y el número sube en uno."),
        ex("Si mañana es domingo, ¿qué día es hoy?", "sábado", "Hoy es el día de antes del domingo."),
        ex("¿Ayer está en el pasado, el presente o el futuro?", "pasado", "Ayer ya ocurrió antes de hoy."),
    ],
    open_task=task("Completa en tu hoja una tabla con tres columnas: ayer, hoy y mañana. Hoy es miércoles 10. Escribe el día y el número de cada columna, y una actividad que podrías hacer en cada uno (ir a la plaza, tomar once en casa, ayudar con la cena).", "Ayer: martes 9, ir a la plaza. Hoy: miércoles 10, tomar once en casa. Mañana: jueves 11, ayudar con la cena.", ["tres columnas", "días y números correctos", "una actividad por columna"], ["tabla con tres columnas"], ["poner mañana antes que ayer", "cambiar el número"], "Pide que lea la tabla de izquierda a derecha y diga qué sigue después."),
    reinforce="Di en voz alta qué hiciste ayer, qué haces hoy y qué harás mañana.",
    extend="Escribe una actividad de pasado mañana y explica por qué todavía no la haces.",
)

register(
    OA2, 3,
    materials="Lápiz y papel. Las rutinas y las horas están escritas en cada ejercicio.",
    use="Aprenderé a relacionar mis actividades con momentos del día: mañana, tarde y noche. Sirve para ordenar mi rutina y entender por qué algunas cosas se hacen de día y otras de noche.",
    prior=["Sé que hay día y noche.", "Sé qué es antes y después."],
    explain=[
        "El día se divide en mañana, tarde y noche. En la mañana sale el Sol y hay luz. En la tarde el Sol baja. En la noche está oscuro y se ven la Luna y las estrellas, cuando el cielo está despejado.",
        "En Chile el Sol sale por el lado de la cordillera de los Andes y se esconde hacia el lado del mar. Ese camino cuenta el paso del día. Después de la noche vuelve a salir el Sol y empieza otro día.",
        "Hay actividades que hacemos de día, como ir a clases, y otras de noche, como dormir. Las horas también nos ayudan: las 8 de la mañana es temprano, las 12 es el mediodía y las 9 de la noche es tarde. La madrugada es la parte de la noche justo antes de que salga el Sol.",
    ],
    vocab=[("mañana", "parte del día cuando sale el Sol"), ("tarde", "parte del día después del mediodía"), ("noche", "parte del día con cielo oscuro"), ("mediodía", "las 12 del día"), ("rutina", "cosas que hacemos cada día en un orden parecido")],
    worked=[
        {"title": "Momento del día", "problem": "¿En qué momento del día tomas desayuno: mañana, tarde o noche?", "steps": ["El desayuno es lo primero que comemos al despertar.", "Despertamos cuando sale el Sol."], "answer": "En la mañana"},
        {"title": "Relacionar una hora", "problem": "Son las 9 de la noche. ¿Qué actividad es más probable: ir al colegio o dormir?", "steps": ["A las 9 de la noche el cielo está oscuro.", "De noche las personas descansan."], "answer": "Dormir"},
    ],
    mistakes=[
        {"wrong": "Decir que las 8 de la mañana y las 8 de la noche son lo mismo.", "why": "Se mira solo el número de la hora.", "fix": "Mira si es el comienzo del día o si ya está oscuro."},
        {"wrong": "Pensar que de noche no pasa nada.", "why": "Se piensa que solo el día tiene actividades.", "fix": "De noche se cena, se descansa y algunas personas trabajan."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué momento del día vemos las estrellas: día o noche?", "noche", "Las estrellas se ven con el cielo oscuro."),
            ex("¿Cuándo sale el Sol: en la mañana o en la noche?", "en la mañana", "El Sol sale al comenzar el día."),
            ex("¿Cuántas partes tiene el día que estudiamos: mañana, tarde y noche?", "3", "Son tres partes."),
        ],
        "understand": [
            ex("Ordena el día de primero a último: noche, mañana, tarde.", "mañana, tarde, noche", "El día avanza de la mañana a la tarde y luego a la noche."),
            ex("¿Por dónde se esconde el Sol en Chile, hacia la cordillera o hacia el mar?", "hacia el mar", "El Sol sale por la cordillera y se esconde hacia el mar."),
            ex("¿Qué hora es el mediodía?", "las 12 del día", "El mediodía es la mitad del día."),
        ],
        "apply": [
            ex("Clasifica en mañana, tarde o noche: jugar en la plaza cuando el Sol ya va bajando.", "tarde", "En la tarde el Sol baja."),
            ex("Clasifica en mañana, tarde o noche: lavarse la cara al despertar.", "mañana", "Se hace al comenzar el día."),
            ex("Clasifica en mañana, tarde o noche: ponerse la ropa de dormir.", "noche", "Se hace cuando se prepara el descanso."),
        ],
        "reason": [
            ex("Sofía dice que a las 3 de la madrugada hay mucho Sol. ¿Es correcto?", "No; a esa hora es de noche y está oscuro", "A las 3 de la madrugada todavía no sale el Sol."),
            ex("Un panadero se levanta a las 4 de la madrugada para tener pan caliente. ¿Su trabajo empieza de día o de noche?", "de noche", "A las 4 de la madrugada todavía está oscuro."),
        ],
        "challenge": [
            ex("Pedro sale a la escuela cuando recién sale el Sol y vuelve a su casa después del almuerzo. ¿Qué momentos del día pasa en la escuela?", "mañana y parte de la tarde", "Sale de mañana y vuelve cuando la tarde va avanzando."),
            ex("Ordena estas actividades del día: A) cena, B) almuerzo, C) desayuno.", "C, B, A", "Se desayuna en la mañana, se almuerza al mediodía y se cena en la noche."),
        ],
    },
    context=[ex("La abuela de Diego dice: «Me voy a dormir cuando veo las primeras estrellas». ¿En qué parte del día se acuesta?", "en la noche", "Las primeras estrellas se ven cuando oscurece.")],
    selfcheck=[
        ex("¿Qué actividad hacemos de noche: dormir o jugar con el Sol?", "dormir", "De noche hay oscuridad y descansamos."),
        ex("¿La luz del Sol hay de día o de noche?", "de día", "El Sol alumbra durante el día."),
        ex("¿Cuál viene después de la tarde?", "la noche", "El día sigue de tarde a noche."),
    ],
    open_task=task("Dibuja tres cuadros: mañana, tarde y noche. Dentro de cada cuadro dibuja una actividad que haces tú, eligiendo entre estas opciones: desayunar, ir al colegio, jugar en la plaza, tomar once, cenar, dormir, mirar las estrellas.", "Mañana: desayunar. Tarde: jugar en la plaza. Noche: dormir.", ["tres cuadros en orden", "una actividad por momento", "actividades apropiadas para cada momento"], ["tres dibujos con su momento escrito"], ["poner dormir en la mañana", "no rotular los cuadros"], "Pide que explique cómo sabe que esa actividad es de ese momento."),
    reinforce="Mira por una ventana: dime si es mañana, tarde o noche y cómo lo sabes.",
    extend="Averigua a qué hora sale el Sol en tu casa mañana y anótalo con la palabra mañana.",
)

register(
    OA2, 4,
    materials="Lápiz y papel. La línea de tiempo de una niña imaginaria está escrita en cada ejercicio.",
    use="Aprenderé a hablar de este año, del año pasado y del año próximo. Sirve para ubicar recuerdos y planes en una línea de tiempo.",
    prior=["Sé qué es un año.", "Sé decir ayer, hoy y mañana."],
    explain=[
        "Este año es el año en que estamos. El año pasado es el que viene justo antes y el año próximo es el que viene justo después. Si este año es 2030, el año pasado fue 2029 y el año próximo será 2031.",
        "Un año es mucho más largo que un día: tiene doce meses. Por eso las cosas que pasaron el año pasado nos parecen más lejanas que las de ayer. Una línea de tiempo pone los años en fila, de izquierda a derecha, de lo más antiguo a lo más nuevo.",
        "Para ordenar hechos en una línea de tiempo, mira primero el año y, si es el mismo, mira el mes. El hecho con el año menor ocurrió antes. Un hecho con el año mayor ocurrió después.",
    ],
    vocab=[("este año", "el año en que estamos"), ("año pasado", "el año que viene justo antes"), ("año próximo", "el año que viene justo después"), ("línea de tiempo", "fila que ordena hechos de más antiguo a más nuevo"), ("antiguo", "que pasó hace más tiempo")],
    worked=[
        {"title": "Año pasado y próximo", "problem": "En esta historia este año es 2030. ¿Qué año fue el año pasado y cuál será el próximo?", "steps": ["Antes de 2030 está 2029.", "Después de 2030 viene 2031."], "answer": "Año pasado 2029 y año próximo 2031"},
        {"title": "Ordenar hechos", "problem": "Nina aprendió a andar en bicicleta el 2 de mayo de 2028 y entró a primero básico el 3 de marzo de 2030. ¿Qué pasó antes?", "steps": ["Comparo los años: 2028 es menor que 2030.", "El hecho con el año menor ocurrió antes."], "answer": "Primero aprendió a andar en bicicleta"},
    ],
    mistakes=[
        {"wrong": "Creer que el año pasado es el año que viene.", "why": "Se confunde pasado con próximo.", "fix": "El año pasado ya ocurrió; el próximo todavía no."},
        {"wrong": "Ordenar fechas mirando solo el día y el mes.", "why": "No se mira el año primero.", "fix": "Compara primero el año; si son iguales, mira el mes."},
    ],
    tiers={
        "recovery": [
            ex("Este año es 2030. ¿Qué año será el próximo?", "2031", "El próximo año viene justo después."),
            ex("Este año es 2030. ¿Qué año fue el año pasado?", "2029", "El año pasado viene justo antes."),
            ex("Un año del calendario va de enero a diciembre. ¿Cuántos meses completos tiene?", "12", "El año tiene doce meses."),
        ],
        "understand": [
            ex("Línea de tiempo de Nina (en esta historia este año es 2030): 2 de mayo de 2028, aprendió a andar en bicicleta; 3 de marzo de 2030, entró a primero básico. ¿Cuál de estos hechos es más antiguo?", "aprender a andar en bicicleta", "Tiene el año menor, 2028."),
            ex("¿Cuál es más lejana en el tiempo: lo de ayer o lo del año pasado?", "lo del año pasado", "Un año es mucho más largo que un día."),
            ex("¿Qué palabra usamos para hablar del año que viene después de este: pasado o próximo?", "próximo", "El próximo año todavía no llega."),
        ],
        "apply": [
            ex("Nina nació el 7 de agosto de 2023 y empezó el kínder el 4 de marzo de 2029. ¿Qué pasó el año pasado, si este año es 2030?", "empezó el kínder", "El año pasado es 2029, el año del kínder."),
            ex("Si este año es 2030, ¿en qué año fue el año anterior al año pasado?", "2028", "Antes de 2029 está 2028."),
            ex("Ordena de más antiguo a más nuevo: 2031, 2029, 2030.", "2029, 2030, 2031", "En la línea de tiempo van del año menor al mayor."),
        ],
        "reason": [
            ex("Dos hechos son del 9 de abril de 2029 y del 12 de enero de 2029. ¿Cuál fue antes?", "el 12 de enero de 2029", "El año es el mismo y enero viene antes que abril."),
            ex("Pedro dice que lo que ocurrió el año próximo ya pasó. ¿Es correcto?", "No; el próximo año todavía no llega", "Lo próximo va a ocurrir, no ya ocurrió."),
        ],
        "challenge": [
            ex("Ordena de más antiguo a más nuevo estos hechos de Nina: 3 de marzo de 2030 entró a primero; 7 de agosto de 2023 nació; 4 de marzo de 2029 empezó el kínder.", "nació, empezó el kínder, entró a primero", "Se ordenan por año: 2023, 2029 y 2030."),
            arith("Nina nació en 2023 y este año es 2030. ¿Cuántos años pasaron entre 2023 y 2030?", "2030-2023", "Se resta el año menor al año mayor."),
        ],
    },
    context=[ex("La familia de Ana dice: «Este año vamos al sur, el año pasado fuimos a la playa y el año próximo iremos al campo». Si este año es 2030, ¿en qué año vamos al campo?", "2031", "El campo está en el año próximo, que viene después de 2030.")],
    selfcheck=[
        ex("Si este año es 2035, ¿qué año fue el año pasado?", "2034", "El año pasado viene justo antes."),
        ex("En una línea de tiempo, ¿qué va a la izquierda: lo más antiguo o lo más nuevo?", "lo más antiguo", "Los hechos se ordenan de izquierda a derecha, de antiguo a nuevo."),
        ex("Si este año es 2035, ¿qué año será el próximo?", "2036", "Viene justo después de 2035."),
    ],
    open_task=task("Dibuja una línea de tiempo con tres puntos: el año pasado, este año y el año próximo. Para ayudarte, supón que este año es 2030. Escribe bajo cada punto un hecho, por ejemplo: aprendí a leer, entré a primero básico, voy a cumplir 8 años.", "Año pasado 2029: fui al kínder. Este año 2030: entré a primero básico. Año próximo 2031: voy a pasar a segundo básico.", ["tres puntos en orden", "años correctos", "un hecho por punto"], ["línea de tiempo dibujada"], ["poner el año próximo a la izquierda", "repetir un año"], "Pide que explique cuál punto es el más antiguo y cuál el más nuevo."),
    reinforce="Escribe un recuerdo del año pasado y un plan para el año próximo.",
    extend="Haz una línea de tiempo con cinco años seguidos y marca cuál es este año.",
)

register(
    OA2, 5,
    materials="Lápiz y papel. El cuento desordenado está escrito en el ejercicio. No necesitas nada más.",
    use="Aprenderé a contar una historia en orden usando palabras de tiempo. Sirve para que otros entiendan cuándo pasó cada cosa.",
    prior=["Sé qué es antes y después.", "Sé decir ayer, hoy y mañana."],
    explain=[
        "Un relato en orden cuenta primero lo que pasó primero y deja para el final lo que pasó último. Las palabras primero, luego, después y al final ayudan a que el oyente no se pierda en la historia.",
        "También usamos palabras como ayer, hoy y mañana, o el año pasado y el año próximo. Si cuentas un paseo de ayer, usas verbos del pasado: fuimos, comimos. Si cuentas lo que harás mañana, dices: iremos, comeremos.",
        "Para revisar tu relato pregúntate: ¿puse todo en orden? ¿Usé palabras de tiempo? ¿Se entiende cuándo pasó cada cosa? Si cambias el orden de las frases, la historia cambia o deja de tener sentido.",
    ],
    vocab=[("relato", "una historia que se cuenta"), ("secuencia", "cosas ordenadas una después de otra"), ("luego", "palabra que marca lo que viene enseguida"), ("pasado", "lo que ya ocurrió"), ("futuro", "lo que va a ocurrir")],
    worked=[
        {"title": "Ordenar una historia", "problem": "Frases: A) Comimos en el pasto. B) Fuimos al parque en micro. C) Volvimos a casa cansados. Ordénalas.", "steps": ["Primero llegamos al parque: B.", "Luego comemos: A.", "Al final volvemos: C."], "answer": "B, A, C"},
        {"title": "Pasado o futuro", "problem": "«Ayer fuimos al cerro». ¿Esto ya pasó o va a pasar?", "steps": ["La palabra ayer indica un día anterior.", "Ya pasó."], "answer": "Ya pasó"},
    ],
    mistakes=[
        {"wrong": "Contar el final al comienzo del relato.", "why": "Se cuenta lo que más importa primero.", "fix": "Usa primero, luego y al final para guiar el orden."},
        {"wrong": "Mezclar ayer y mañana en una misma frase.", "why": "Se confunde si ya ocurrió o aún no.", "fix": "Pregúntate si el hecho ya pasó o va a pasar."},
    ],
    tiers={
        "recovery": [
            ex("«Ayer fuimos al cerro». ¿Eso ya pasó o va a pasar?", "ya pasó", "La palabra ayer habla de un día anterior."),
            ex("«Mañana iremos al cine». ¿Eso ya pasó o va a pasar?", "va a pasar", "Mañana llega después de hoy."),
            ex("¿Qué palabra va primero en un relato: primero o al final?", "primero", "Primero marca el comienzo de la historia."),
        ],
        "understand": [
            ex("En un relato, ¿qué palabra marca lo que ocurre enseguida: luego o ayer?", "luego", "Luego muestra lo que viene a continuación."),
            ex("¿Para qué sirven las palabras primero, luego y al final?", "para ordenar lo que cuento", "Dicen en qué lugar de la historia ocurre cada cosa."),
            ex("¿Cuál frase está en pasado: «Comimos pan» o «Comeremos pan»?", "Comimos pan", "Comimos habla de algo que ya ocurrió."),
        ],
        "apply": [
            ex("Cuento desordenado: A) Volvieron a casa con sus bolsas llenas. B) Tomás y su abuelo salieron a la feria. C) Compraron manzanas y tomates. Ordénalo.", "B, C, A", "Salen, compran y luego vuelven."),
            ex("Completa con ayer, hoy o mañana: «___ es mi cumpleaños; ayer fue el cumpleaños de mi hermana»; hoy es 12 y ayer fue 11.", "hoy", "La frase cuenta algo que ocurre en el día presente."),
            ex("Convierte a futuro: «Ayer jugué fútbol». Escríbela con la palabra mañana.", "Mañana jugaré fútbol", "El verbo cambia a futuro y ayer cambia por mañana."),
        ],
        "reason": [
            ex("Ana cuenta: «Al final desperté. Primero me lavé los dientes y luego salí al colegio». ¿Qué está mal?", "Al final desperté no va al final", "Despertarse es lo primero que ocurre en la mañana."),
            ex("Dos amigos cuentan el mismo paseo. Uno dice «ayer» y el otro «el año pasado». ¿Quién habla de algo más antiguo?", "el que dice el año pasado", "Un año es mucho más largo que un día."),
        ],
        "challenge": [
            ex("Ordena el relato: A) La semilla se convirtió en planta. B) Lola plantó una semilla. C) Lola regó la tierra cada día. D) La planta dio una flor.", "B, C, A, D", "Se planta, se riega, crece la planta y al final da flor."),
            ex("Escribe el relato anterior con la palabra mañana al inicio: «Mañana plantaremos una semilla». ¿Qué cambia en el verbo de las demás frases?", "Pasan a futuro: regaremos, crecerá, dará", "Algo que va a ocurrir se dice en futuro."),
        ],
    },
    context=[ex("Sebastián cuenta su fin de semana: «El sábado fuimos al mercado y el domingo visitamos a mis primos». Si hoy es lunes, ¿lo que cuenta ya ocurrió?", "Sí", "El sábado y el domingo vienen antes del lunes.")],
    selfcheck=[
        ex("¿Qué palabra de tiempo usarías para el último paso de una receta?", "al final", "Al final marca el cierre de la secuencia."),
        ex("«Dentro de un año seré más alto». ¿Es pasado o futuro?", "futuro", "Dentro de un año todavía no llega."),
        ex("¿Qué va antes en una historia: el comienzo o el final?", "el comienzo", "Un relato en orden parte por lo que ocurrió primero."),
    ],
    open_task=task("Cuenta en cinco frases un día de paseo imaginario usando primero, luego, después y al final. Puedes elegir una de estas ideas: ir a la plaza (columpios, helado, volver a casa), ir a la playa (arena, castillo, once), o ir a la feria (frutas, verduras, volver).", "Primero fuimos a la plaza. Luego jugué en los columpios. Después comimos helado. Al final volvimos a casa. Fue un paseo muy entretenido.", ["cinco frases", "usa las cuatro palabras de orden", "la historia tiene sentido"], ["texto de cinco frases o cinco dibujos con una frase"], ["contar el final primero", "no usar palabras de orden"], "Pide que lea su relato a un adulto y que le diga qué ocurrió después de la tercera frase."),
    reinforce="Cuenta a alguien de tu casa lo que hiciste ayer con primero, luego y al final.",
    extend="Cuenta lo mismo pero para mañana, cambiando los verbos al futuro.",
)
