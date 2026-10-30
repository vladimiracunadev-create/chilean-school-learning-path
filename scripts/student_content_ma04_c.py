"""Student material for 4.º básico Matemática, OA 21 (conversiones de unidades de tiempo) y OA 22 (longitud en m y cm)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA21, OA22 = "MA04 OA 21", "MA04 OA 22"

MESES = "enero 31 días, febrero 28 días (29 en año bisiesto), marzo 31, abril 30, mayo 31, junio 30, julio 31, agosto 31, septiembre 30, octubre 31, noviembre 30 y diciembre 31"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 21
register(
    OA21, 1,
    materials="Lápiz y papel. Si tienes un reloj con segundero o un celular con cronómetro, un adulto puede ayudarte a mirar cuánto dura un minuto.",
    use="Aprenderé a convertir segundos en minutos y minutos en segundos. Sirve para entender cuánto dura una canción, un juego o una carrera.",
    prior=["Sé multiplicar y dividir con las tablas.", "Sé que un reloj marca horas, minutos y segundos."],
    explain=[
        "Los segundos y los minutos son unidades de tiempo. Un minuto tiene 60 segundos. Convertir es escribir la misma cantidad de tiempo con otra unidad, sin que el tiempo cambie.",
        "Para pasar de minutos a segundos, multiplicas por 60. Por ejemplo, 3 minutos son 3 × 60 = 180 segundos. Para pasar de segundos a minutos, divides por 60: 240 segundos son 240 ÷ 60 = 4 minutos.",
        "A veces sobran segundos. 130 segundos son 2 minutos y 10 segundos, porque 2 × 60 = 120 y 130 − 120 = 10. Cuida la unidad: 60 sirve para segundos y minutos, pero no para días ni meses.",
    ],
    vocab=[("segundo", "unidad de tiempo muy corta; 60 segundos forman un minuto"), ("minuto", "unidad de tiempo que dura 60 segundos"), ("convertir", "escribir la misma cantidad con otra unidad"), ("equivalencia", "dos cantidades distintas que valen lo mismo, como 1 minuto y 60 segundos")],
    worked=[
        {"title": "De minutos a segundos", "problem": "Una canción dura 4 minutos. ¿Cuántos segundos dura?", "steps": ["Cada minuto tiene 60 segundos.", "Multiplico: 4 × 60 = 240."], "answer": "Dura 240 segundos"},
        {"title": "De segundos a minutos y segundos", "problem": "Un corredor tardó 150 segundos en una vuelta. ¿Cuántos minutos y segundos son?", "steps": ["Veo cuántos grupos de 60 caben en 150: 2 grupos, porque 2 × 60 = 120.", "Resto lo que sobra: 150 − 120 = 30."], "answer": "Son 2 minutos y 30 segundos"},
    ],
    mistakes=[
        {"wrong": "Decir que 2 minutos son 100 segundos.", "why": "Se usa 50 o 100 en vez de 60, como si el minuto fuera como el metro.", "fix": "En el tiempo, 1 minuto = 60 segundos. Entonces 2 × 60 = 120."},
        {"wrong": "Escribir 90 segundos como 1,90 minutos.", "why": "Se separa el número sin pensar en que sobran segundos.", "fix": "90 − 60 = 30, así que son 1 minuto y 30 segundos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos segundos tiene 1 minuto?", "60", "La equivalencia básica es 1 minuto = 60 segundos."),
            arith("¿Cuántos segundos hay en 2 minutos?", "2*60", "Se multiplica la cantidad de minutos por 60.", " segundos"),
            arith("¿Cuántos minutos son 180 segundos?", "180//60", "Se divide por 60 porque cada minuto tiene 60 segundos.", " minutos"),
        ],
        "understand": [
            ex("¿Qué operación usas para pasar de minutos a segundos: multiplicar o dividir por 60?", "Multiplicar por 60", "Un minuto es más largo, y cada uno trae 60 segundos."),
            arith("Un video dura 5 minutos. ¿Cuántos segundos dura?", "5*60", "Cada uno de los 5 minutos tiene 60 segundos.", " segundos"),
            ex("Pasa 130 segundos a minutos y segundos.", "2 minutos y 10 segundos", "En 130 caben 2 grupos de 60 (120) y sobran 10.", calc="130-2*60"),
        ],
        "apply": [
            ex("Una prueba de natación dura 3 minutos y 20 segundos. ¿Cuántos segundos son en total?", "200 segundos", "3 × 60 = 180 y se suman los 20 segundos que sobran.", calc="3*60+20"),
            arith("Ana tardó 75 segundos en armar un rompecabezas. ¿Cuántos segundos sobran después de completar 1 minuto?", "75-60", "Se quita 1 minuto (60 segundos) a los 75.", " segundos"),
            arith("Un juego dura 360 segundos. ¿Cuántos minutos dura?", "360//60", "Se divide la cantidad de segundos por 60.", " minutos"),
        ],
        "reason": [
            ex("Luis dice que 2 minutos son 100 segundos. ¿Tiene razón? Explica con el 60.", "No; son 120 segundos porque 2 × 60 = 120", "Cada minuto vale 60 segundos, no 50."),
            ex("Una tortuga avanza 1 metro cada 45 segundos. ¿Tarda más o menos de 1 minuto en avanzar ese metro?", "Menos de 1 minuto", "45 segundos son menos que 60 segundos."),
        ],
        "challenge": [
            ex("Una canción A dura 4 minutos y otra canción B dura 250 segundos. ¿Cuál dura más?", "La canción B", "4 minutos son 240 segundos y 250 es mayor que 240."),
            ex("Una vela de cumpleaños se apaga en 10 minutos. ¿Cuántos segundos son? Responde con el número.", "600", "10 × 60 = 600.", calc="10*60"),
        ],
    },
    context=[ex("Tomás hizo una pausa de lectura de 2 minutos y 15 segundos. Su hermana hizo una de 140 segundos. ¿Quién leyó por más tiempo, y por cuántos segundos más?", "Su hermana, por 5 segundos más", "2 minutos y 15 segundos son 135 segundos; 140 es mayor, así que su hermana leyó más.", calc="140-135")],
    selfcheck=[
        ex("¿Cuántos segundos hay en 6 minutos?", "360", "6 × 60 = 360.", calc="6*60"),
        ex("¿Cuántos minutos son 300 segundos?", "5", "300 ÷ 60 = 5.", calc="300//60"),
        ex("¿Cuántos segundos son 1 minuto y 5 segundos?", "65 segundos", "60 + 5 = 65.", calc="60+5"),
    ],
    open_task=task(
        "Elige una de estas actividades: cepillarse los dientes por 2 minutos, ver un video de 3 minutos y 30 segundos o jugar 5 minutos. Escribe cuántos segundos dura y muestra la operación. Si tienes reloj, intenta hacer solo 1 minuto de la actividad y comprueba.",
        "Cepillarse 2 minutos: 2 × 60 = 120 segundos.",
        ["elige una de las tres actividades", "usa 1 minuto = 60 segundos", "muestra la operación", "escribe la unidad"],
        ["operación escrita", "resultado con unidad"],
        ["usar 100 en vez de 60", "olvidar sumar los segundos extra"],
        "Pide decir en voz alta por qué se multiplica por 60. Reconoce que escriba la unidad.",
    ),
    reinforce="Mira un reloj con segundero y cuenta cuántos segundos pasan en una vuelta completa de la aguja de los segundos.",
    extend="Calcula cuántos segundos hay en 10 minutos y explica cómo lo hiciste sin sumar 60 diez veces.",
)

register(
    OA21, 2,
    materials="Lápiz y papel. Si tienes un reloj de pared, úsalo para mirar el avance del minutero en una hora.",
    use="Aprenderé a convertir horas en minutos y minutos en horas. Sirve para saber cuánto dura una película, un viaje o una clase.",
    prior=["Sé que un minuto tiene 60 segundos.", "Sé multiplicar y dividir con las tablas."],
    explain=[
        "Una hora tiene 60 minutos. Para pasar de horas a minutos, multiplicas por 60. Por ejemplo, 2 horas son 2 × 60 = 120 minutos. Es la misma relación de 60 que usaste con segundos y minutos.",
        "Para pasar de minutos a horas, divides por 60. 180 minutos son 180 ÷ 60 = 3 horas. Si sobra, lo que queda son minutos: 150 minutos son 2 horas y 30 minutos, porque 2 × 60 = 120 y 150 − 120 = 30.",
        "Una media hora son 30 minutos y un cuarto de hora son 15 minutos. Cuando una duración tiene horas y minutos, convierte las horas y luego suma los minutos: 1 hora y 20 minutos es 60 + 20 = 80 minutos.",
    ],
    vocab=[("hora", "unidad de tiempo que dura 60 minutos"), ("media hora", "30 minutos"), ("cuarto de hora", "15 minutos"), ("duración", "tiempo que dura algo, desde que empieza hasta que termina")],
    worked=[
        {"title": "De horas a minutos", "problem": "Una película dura 2 horas y 10 minutos. ¿Cuántos minutos dura?", "steps": ["Paso las horas a minutos: 2 × 60 = 120.", "Sumo los minutos que sobran: 120 + 10 = 130."], "answer": "Dura 130 minutos"},
        {"title": "De minutos a horas y minutos", "problem": "Un viaje duró 200 minutos. ¿Cuántas horas y minutos son?", "steps": ["En 200 caben 3 grupos de 60, porque 3 × 60 = 180.", "Sobran 200 − 180 = 20 minutos."], "answer": "Son 3 horas y 20 minutos"},
    ],
    mistakes=[
        {"wrong": "Decir que 90 minutos son 1 hora y 90 minutos.", "why": "Se deja el número completo sin sacar los 60 minutos de la hora.", "fix": "90 − 60 = 30, entonces son 1 hora y 30 minutos."},
        {"wrong": "Multiplicar 3 horas por 100 para obtener 300 minutos.", "why": "Se usa 100 porque se parece a la conversión de metros a centímetros.", "fix": "En el tiempo, 1 hora = 60 minutos: 3 × 60 = 180 minutos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos minutos tiene 1 hora?", "60", "La equivalencia básica es 1 hora = 60 minutos."),
            arith("¿Cuántos minutos hay en 3 horas?", "3*60", "Se multiplica la cantidad de horas por 60.", " minutos"),
            arith("¿Cuántas horas son 240 minutos?", "240//60", "Se divide por 60 porque cada hora tiene 60 minutos.", " horas"),
        ],
        "understand": [
            ex("¿Cuántos minutos son media hora?", "30 minutos", "Media hora es la mitad de 60 minutos.", calc="60//2"),
            ex("Escribe 150 minutos en horas y minutos.", "2 horas y 30 minutos", "Caben 2 horas (120 minutos) y sobran 30.", calc="150-2*60"),
            ex("Un cuarto de hora, ¿cuántos minutos es?", "15 minutos", "Un cuarto de 60 es 15.", calc="60//4"),
        ],
        "apply": [
            ex("La clase de arte dura 1 hora y 30 minutos. ¿Cuántos minutos dura?", "90 minutos", "60 + 30 = 90.", calc="60+30"),
            arith("Una excursión al parque dura 120 minutos. ¿Cuántas horas dura?", "120//60", "Se divide por 60 para obtener las horas.", " horas"),
            ex("Una función de títeres dura 45 minutos. ¿Cuántos minutos le faltan para durar 1 hora completa?", "15 minutos", "60 − 45 = 15.", calc="60-45"),
        ],
        "reason": [
            ex("Ema dice que 90 minutos son 1 hora y 90 minutos. ¿Qué error tiene y cuál es la respuesta correcta?", "Debía sacar los 60 minutos de la hora; son 1 hora y 30 minutos", "90 − 60 = 30 minutos."),
            ex("¿Cuál es mayor: 2 horas o 100 minutos? Explica con minutos.", "2 horas, porque son 120 minutos", "2 × 60 = 120, que es mayor que 100.", calc="2*60"),
        ],
        "challenge": [
            ex("Un tren sale a las 9:00 y llega a las 11:45. ¿Cuántos minutos dura el viaje?", "165 minutos", "Son 2 horas (120 minutos) y 45 minutos más.", calc="2*60+45"),
            ex("Una tarea de 3 horas y 15 minutos, ¿cuántos minutos son?", "195 minutos", "3 × 60 = 180 y se suman 15.", calc="3*60+15"),
        ],
    },
    context=[ex("Sofía ve dos capítulos de una serie: uno de 25 minutos y otro de 35 minutos. ¿Cuánto tiempo ve en total? Escribe horas y minutos.", "60 minutos, o sea 1 hora", "25 + 35 = 60 minutos, que es exactamente 1 hora.", calc="25+35")],
    selfcheck=[
        ex("¿Cuántos minutos hay en 5 horas?", "300", "5 × 60 = 300.", calc="5*60"),
        ex("Escribe 100 minutos en horas y minutos.", "1 hora y 40 minutos", "100 − 60 = 40.", calc="100-60"),
        ex("¿Cuántas horas son 360 minutos?", "6", "360 ÷ 60 = 6.", calc="360//60"),
    ],
    open_task=task(
        "Elige uno de estos tiempos: un recreo de 20 minutos, una película de 1 hora y 45 minutos o un paseo de 150 minutos. Conviértelo: si está en minutos, a horas y minutos; si está en horas y minutos, a minutos. Muestra la operación.",
        "Película 1 hora y 45 minutos: 1 × 60 + 45 = 105 minutos.",
        ["elige una de las tres duraciones", "usa 1 hora = 60 minutos", "muestra la operación", "da el resultado con su unidad"],
        ["operación escrita", "respuesta con unidad"],
        ["escribir 1 hora 45 como 145 minutos", "usar 100 en lugar de 60"],
        "Pide verificar convirtiendo de vuelta. Reconoce que el estudiante no mezcle horas y minutos en un solo número.",
    ),
    reinforce="Mira la hora ahora y la hora dentro de un rato. Calcula cuántos minutos pasaron.",
    extend="Escribe cuántos minutos tiene medio día de 12 horas y cuántos minutos tiene un día entero de 24 horas.",
)

register(
    OA21, 3,
    materials="Lápiz y papel. La lista de meses y días está escrita dentro de la clase. Puedes usar el calendario de tu casa para comprobar.",
    use="Aprenderé cuántos días tiene cada mes y cuántos meses tiene un año. Sirve para calcular cuánto falta para una fecha y cuánto dura un proyecto.",
    prior=["Sé el orden de los meses del año.", "Sé sumar y multiplicar números hasta 100."],
    explain=[
        "Un año tiene 12 meses. Para pasar de años a meses, multiplicas por 12: 2 años son 2 × 12 = 24 meses. Para pasar de meses a años, divides por 12: 36 meses son 3 años.",
        "Los meses no tienen todos la misma cantidad de días. Estos son los días de cada mes: enero 31 días, febrero 28 días (29 en año bisiesto), marzo 31, abril 30, mayo 31, junio 30, julio 31, agosto 31, septiembre 30, octubre 31, noviembre 30 y diciembre 31.",
        "Por eso, no siempre sirve decir que un mes tiene 30 días. Si quieres saber los días de dos meses seguidos, busca cada mes en la lista y suma. Abril y mayo son 30 + 31 = 61 días. En esta clase usa febrero con 28 días, salvo que el problema diga que es bisiesto.",
    ],
    vocab=[("mes", "parte del año que tiene entre 28 y 31 días"), ("año", "tiempo que tiene 12 meses"), ("año bisiesto", "año en que febrero tiene 29 días"), ("convertir", "escribir la misma duración con otra unidad")],
    worked=[
        {"title": "De años a meses", "problem": "Un árbol tiene 3 años. ¿Cuántos meses de vida tiene?", "steps": ["Cada año tiene 12 meses.", "Multiplico: 3 × 12 = 36."], "answer": "Tiene 36 meses"},
        {"title": "Sumar días de meses distintos", "problem": "¿Cuántos días hay en abril y mayo juntos? Abril tiene 30 días y mayo tiene 31 días.", "steps": ["Anoto los días de cada mes: abril 30 y mayo 31.", "Sumo: 30 + 31 = 61."], "answer": "Hay 61 días"},
    ],
    mistakes=[
        {"wrong": "Decir que todos los meses tienen 30 días.", "why": "Se generaliza un mes a todos los demás.", "fix": "Busca cada mes en la lista de días: unos tienen 31, otros 30 y febrero 28."},
        {"wrong": "Calcular los meses de 2 años como 2 × 10 = 20.", "why": "Se usa un número de 10 en vez de 12, que es la cantidad de meses del año.", "fix": "1 año tiene 12 meses: 2 × 12 = 24."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos meses tiene un año?", "12", "Enero a diciembre son doce meses."),
            ex("En Matemática: ¿Cuántos días tiene abril?", "30", "Abril es uno de los meses de 30 días."),
            arith("¿Cuántos meses hay en 2 años?", "2*12", "Se multiplica la cantidad de años por 12.", " meses"),
        ],
        "understand": [
            ex("¿Cuántos días tiene febrero en un año que no es bisiesto?", "28", "Febrero es el único mes con 28 días."),
            arith("¿Cuántos años son 48 meses?", "48//12", "Se divide la cantidad de meses por 12.", " años"),
            ex("Abril y mayo son meses seguidos. ¿Cuál de los dos tiene 31 días?", "Mayo", "Mayo tiene 31 días y abril solo 30."),
        ],
        "apply": [
            ex("Mateo nació hace 9 años. ¿Cuántos meses han pasado desde que nació, contando solo años completos?", "108 meses", "9 × 12 = 108.", calc="9*12"),
            ex("Un proyecto de ciencias dura junio y julio completos. Junio tiene 30 días y julio 31. ¿Cuántos días dura?", "61 días", "30 + 31 = 61.", calc="30+31"),
            ex("En un año no bisiesto, ¿cuántos días tienen enero y febrero juntos?", "59 días", "Enero 31 y febrero 28: 31 + 28 = 59.", calc="31+28"),
        ],
        "reason": [
            ex("Pía dice que todos los meses tienen 30 días, así que marzo y abril suman 60. ¿Tiene razón? Marzo tiene 31 días y abril 30.", "No; suman 61 días", "31 + 30 = 61, porque marzo tiene 31 días.", calc="31+30"),
            ex("¿Es verdad que 18 meses son más de 1 año? ¿Cuánto es 18 meses en años y meses?", "Sí; son 1 año y 6 meses", "18 − 12 = 6 meses sobran después de 1 año.", calc="18-12"),
        ],
        "challenge": [
            ex("Septiembre y octubre juntos, ¿cuántos días tienen? Septiembre tiene 30 y octubre 31.", "61 días", "30 + 31 = 61.", calc="30+31"),
            ex("Escribe 30 meses en años y meses.", "2 años y 6 meses", "2 años son 24 meses y sobran 6.", calc="30-2*12"),
        ],
    },
    context=[ex("Una cápsula del tiempo se abre en 3 años y 4 meses más. ¿Cuántos meses faltan?", "40 meses", "3 × 12 = 36 y se suman 4 meses.", calc="3*12+4")],
    selfcheck=[
        ex("¿Cuántos meses hay en 4 años?", "48", "4 × 12 = 48.", calc="4*12"),
        ex("¿Cuántos años son 60 meses?", "5", "60 ÷ 12 = 5.", calc="60//12"),
        ex("¿Cuántos días tiene noviembre?", "30", "Noviembre es uno de los meses de 30 días."),
    ],
    open_task=task(
        "Usa la lista de días de la clase. Elige un periodo: de marzo a mayo (3 meses), de junio a agosto (3 meses) o de diciembre a febrero (3 meses, febrero con 28 días). Calcula cuántos días tiene en total y escribe cómo sumaste.",
        "De marzo a mayo: marzo 31 + abril 30 + mayo 31 = 92 días.",
        ["elige un periodo de la lista", "busca los días de cada mes", "suma los tres meses", "escribe el total con su unidad"],
        ["cantidad de días de cada mes", "suma escrita", "total con unidad"],
        ["suponer que todos los meses tienen 30 días", "olvidar un mes en la suma"],
        "Pide mostrar los tres números que sumó. Reconoce que haya respetado los días distintos de cada mes.",
    ),
    reinforce="Con el calendario de tu casa, cuenta cuántos días tiene este mes y cuántos tiene el siguiente.",
    extend="Calcula cuántos días tiene un año no bisiesto sumando los 12 meses de la lista. Comprueba que obtienes un número cercano a 365.",
)

register(
    OA21, 4,
    materials="Lápiz y papel. Todas las equivalencias necesarias están en el cuaderno: 1 minuto = 60 segundos, 1 hora = 60 minutos, 1 año = 12 meses.",
    use="Aprenderé a resolver problemas con varias conversiones de tiempo. Sirve para decidir si un plan cabe en el tiempo que tengo.",
    prior=["Sé convertir segundos, minutos y horas.", "Sé cuántos meses tiene un año y los días de cada mes."],
    explain=[
        "Para resolver un problema de tiempo, primero lee qué unidad se pide en la respuesta. Después escribe las equivalencias que necesitas: 1 minuto = 60 segundos, 1 hora = 60 minutos, 1 año = 12 meses.",
        "Convierte todas las cantidades a una misma unidad antes de comparar o sumar. No puedes sumar 2 minutos con 30 segundos como si fueran números iguales. Pasa todo a segundos: 120 + 30 = 150 segundos.",
        "Comprueba si tu respuesta es razonable. Una canción no puede durar 4.000 horas, y un año no puede tener 30 meses. Una buena forma de comprobar es convertir de vuelta y ver si obtienes el dato inicial.",
    ],
    vocab=[("unidad común", "la misma unidad para todas las cantidades, para poder compararlas"), ("convertir de vuelta", "volver a la unidad inicial para comprobar"), ("razonable", "que tiene sentido para la situación"), ("duración total", "suma de todos los tiempos")],
    worked=[
        {"title": "Sumar tiempos con distinta unidad", "problem": "Un trabajo de arte lleva 1 hora y luego 40 minutos de pintura. ¿Cuántos minutos dura en total?", "steps": ["Paso la hora a minutos: 60.", "Sumo: 60 + 40 = 100."], "answer": "Dura 100 minutos"},
        {"title": "Comparar con una unidad común", "problem": "Un juego dura 2 minutos y otro dura 100 segundos. ¿Cuál dura más?", "steps": ["Paso 2 minutos a segundos: 2 × 60 = 120.", "Comparo 120 con 100."], "answer": "Dura más el juego de 2 minutos"},
    ],
    mistakes=[
        {"wrong": "Sumar 2 horas y 30 minutos como 32.", "why": "Se suman números de unidades distintas.", "fix": "Pasa a minutos: 2 × 60 + 30 = 150, o responde 2 horas y 30 minutos."},
        {"wrong": "Usar 60 para convertir meses en años.", "why": "Se aplica el 60 de segundos y minutos por costumbre.", "fix": "Para meses y años se usa 12: 36 meses ÷ 12 = 3 años."},
    ],
    tiers={
        "recovery": [
            arith("Un cuento se lee en 3 minutos. ¿Cuántos segundos dura?", "3*60", "Se multiplica por 60 porque cada minuto tiene 60 segundos.", " segundos"),
            arith("Una clase dura 2 horas. ¿Cuántos minutos dura?", "2*60", "Se multiplica por 60 porque cada hora tiene 60 minutos.", " minutos"),
            arith("Un gato tiene 36 meses. ¿Cuántos años tiene?", "36//12", "Se divide por 12 porque cada año tiene 12 meses.", " años"),
        ],
        "understand": [
            ex("Para comparar 2 minutos con 100 segundos, ¿en qué unidad conviene pasar ambos tiempos?", "En segundos", "Así los dos números están en la misma unidad y se pueden comparar."),
            ex("Una receta pide 1 hora y luego 15 minutos más de reposo. ¿Cuántos minutos son en total?", "75 minutos", "60 + 15 = 75.", calc="60+15"),
            ex("¿Cuál es mayor: 2 años o 20 meses?", "2 años, que son 24 meses", "2 años son 24 meses, que es más que 20.", calc="2*12"),
        ],
        "apply": [
            ex("Clara corrió 4 minutos y luego 90 segundos. ¿Cuántos segundos corrió en total?", "330 segundos", "4 × 60 = 240 y se suman 90.", calc="4*60+90"),
            ex("Una plantita nació en enero y hoy tiene 15 meses. ¿Cuántos años y meses tiene?", "1 año y 3 meses", "15 − 12 = 3 meses sobran.", calc="15-12"),
            ex("Una película dura 2 horas y 5 minutos. La función ya duró 80 minutos. ¿Cuántos minutos faltan para que termine?", "45 minutos", "2 horas y 5 minutos son 125 minutos; 125 − 80 = 45.", calc="125-80"),
        ],
        "reason": [
            ex("Beto dice: «2 horas y 30 minutos son 32 minutos». ¿Qué error hizo y cuál es la respuesta correcta en minutos?", "Sumó 2 y 30 sin convertir; son 150 minutos", "2 × 60 + 30 = 150 minutos.", calc="2*60+30"),
            ex("Una carrera se hace en 3.000 horas. ¿Es una respuesta razonable? Explica.", "No; una carrera dura segundos, minutos o pocas horas, no miles de horas", "3.000 horas son más de 100 días seguidos; el resultado no tiene sentido para una carrera."),
        ],
        "challenge": [
            ex("Una banda toca 3 canciones de 4 minutos cada una. ¿Cuántos segundos toca en total?", "720 segundos", "3 × 4 = 12 minutos y 12 × 60 = 720.", calc="3*4*60"),
            ex("Un niño tiene 9 años y 6 meses. ¿Cuántos meses tiene?", "114 meses", "9 × 12 = 108 y se suman 6.", calc="9*12+6"),
        ],
    },
    context=[ex("Una escuela organiza un taller que dura 2 horas. Hay 3 actividades iguales y cada una dura 30 minutos, y el resto es descanso. ¿Cuántos minutos de descanso hay?", "30 minutos", "2 horas son 120 minutos; 3 × 30 = 90 y 120 − 90 = 30.", calc="120-3*30")],
    selfcheck=[
        ex("¿Cuántos segundos hay en 7 minutos?", "420", "7 × 60 = 420.", calc="7*60"),
        ex("¿Cuántos minutos son 4 horas?", "240", "4 × 60 = 240.", calc="4*60"),
        ex("¿Cuántos meses hay en 5 años?", "60", "5 × 12 = 60.", calc="5*12"),
    ],
    open_task=task(
        "Inventa un horario de una tarde con tres actividades. Elige entre: leer 40 minutos, dibujar 1 hora, jugar 30 minutos o pausa de 10 minutos. Suma el tiempo total en minutos y escríbelo también en horas y minutos.",
        "Dibujar 1 hora (60) + leer 40 + jugar 30 = 130 minutos, o sea 2 horas y 10 minutos.",
        ["usa tres actividades de la lista", "convierte horas a minutos", "suma todo en minutos", "escribe el total en horas y minutos"],
        ["tres actividades escritas", "suma", "total en dos formas"],
        ["sumar horas y minutos sin convertir", "no pasar el total a horas y minutos"],
        "Pide explicar por qué convirtió antes de sumar. Reconoce las dos formas de escribir el total.",
    ),
    reinforce="Escribe cuánto dura tu recreo y tu hora de almuerzo en minutos, y luego en segundos.",
    extend="Un año tiene 12 meses y un mes tiene unos 30 días. Calcula, con esas cifras, cuántos días tiene aproximadamente un año y compáralo con 365.",
)

# ================================================================ OA 22
register(
    OA22, 1,
    materials="Una regla de 30 cm o una huincha de medir si la tienes. Si no, usa las medidas escritas en cada ejercicio.",
    use="Aprenderé a elegir si conviene medir con metro o con centímetro. Sirve para medir bien una mesa, un lápiz o una pieza de tela.",
    prior=["Sé medir con regla en centímetros.", "Sé que un metro es una unidad de longitud."],
    explain=[
        "Las unidades de longitud sirven para medir cuán largo es algo. El centímetro (cm) es pequeño: mide cosas como un lápiz, una goma o el ancho de tu mano. El metro (m) es más grande: mide cosas como una sala, una puerta o una cancha.",
        "Un metro tiene 100 centímetros. Por eso, el número cambia según la unidad que usas: una mesa de 1 m es lo mismo que una mesa de 100 cm. Si usas la unidad equivocada, el número parece raro.",
        "Para elegir la unidad, piensa en el tamaño. Si la cosa cabe en la mano, usa cm. Si es tan larga como una persona o más, usa m. Después comprueba: un lápiz que mide 15 m no es razonable, pero 15 cm sí.",
    ],
    vocab=[("centímetro (cm)", "unidad de longitud pequeña; 100 de ellos forman un metro"), ("metro (m)", "unidad de longitud que mide 100 centímetros"), ("longitud", "cuán largo es algo"), ("estimar", "decir una medida aproximada sin medir con exactitud")],
    worked=[
        {"title": "Elegir la unidad", "problem": "¿Conviene medir el largo de un cuaderno en metros o en centímetros?", "steps": ["Un cuaderno es pequeño y cabe en la mano.", "Un metro sería demasiado grande; 100 cm formaría un metro."], "answer": "Conviene medirlo en centímetros"},
        {"title": "Revisar si una medida es razonable", "problem": "Julia escribió que su estuche mide 20 m de largo. ¿Es razonable?", "steps": ["20 m es más largo que una sala de clases.", "Un estuche mide cerca de 20 cm."], "answer": "No es razonable; debía ser 20 cm"},
    ],
    mistakes=[
        {"wrong": "Medir el largo de una sala en centímetros y dar un número pequeño como 8.", "why": "Se anota la medida sin fijarse en la unidad.", "fix": "Una sala mide cerca de 8 m. Escribe siempre la unidad."},
        {"wrong": "Pensar que 1 m tiene 10 cm.", "why": "Se confunde con el sistema de 10 de otras unidades.", "fix": "1 m = 100 cm."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántos centímetros tiene 1 metro?", "100", "La equivalencia es 1 m = 100 cm."),
            ex("Para medir el largo de un lápiz, ¿usas metros o centímetros?", "Centímetros", "El lápiz es pequeño y cabe en la mano."),
            ex("Para medir el largo de una sala de clases, ¿usas metros o centímetros?", "Metros", "La sala es larga y los metros dan números más fáciles."),
        ],
        "understand": [
            ex("¿Qué unidad conviene para medir el ancho de una goma: m o cm?", "cm", "La goma es muy pequeña."),
            ex("¿Qué unidad conviene para medir el largo de una cancha de fútbol: m o cm?", "m", "La cancha es muy larga."),
            ex("Una puerta mide 2 m de alto. ¿Es lo mismo que 200 cm?", "Sí", "1 m = 100 cm y 2 × 100 = 200."),
        ],
        "apply": [
            ex("Elige la medida razonable para el largo de una mesa de comedor: 18 cm, 180 cm o 18 m.", "180 cm", "Una mesa mide cerca de 2 m, y 180 cm es casi 2 m."),
            ex("Elige la medida razonable para el largo de un lápiz nuevo: 19 cm, 19 m o 190 cm.", "19 cm", "Un lápiz cabe en la mano; 19 cm es razonable."),
            ex("Una persona adulta mide cerca de 170. ¿Con qué unidad tiene sentido: m o cm?", "cm", "170 cm es lo mismo que 1 m y 70 cm; 170 m sería gigante."),
        ],
        "reason": [
            ex("Rosa midió su estuche y escribió 25 m. ¿Qué error cometió y cuál sería una unidad razonable?", "Usó metros; debería usar centímetros", "Un estuche no puede medir 25 m, casi el largo de una piscina grande."),
            ex("Teo dice que 1 m mide 10 cm. ¿Es verdad? Justifica con la regla de 100.", "No; 1 m mide 100 cm", "La equivalencia es 1 m = 100 cm."),
        ],
        "challenge": [
            ex("Tres cintas miden 50 cm, 1 m y 80 cm. Escribe todo en cm y di cuál es la más larga.", "La de 1 m, que mide 100 cm", "1 m = 100 cm; 100 es mayor que 80 y que 50.", calc="1*100"),
            ex("Una cuerda mide 3 m. Ana dice que mide más de 250 cm. ¿Tiene razón? Explica pasando a cm.", "Sí; 3 m son 300 cm y 300 es mayor que 250", "3 × 100 = 300.", calc="3*100"),
        ],
    },
    context=[ex("Camilo quiere medir su lápiz, el alto de la puerta de su pieza y el largo de su patio. ¿Cuántas de esas tres medidas conviene dar en metros?", "2", "El alto de la puerta y el largo del patio conviene medirlos en metros; el lápiz en centímetros.", calc="3-1")],
    selfcheck=[
        ex("¿Con qué unidad medirías el largo de una hoja: m o cm?", "cm", "La hoja es pequeña."),
        ex("¿Cuántos centímetros son 2 metros?", "200", "2 × 100 = 200.", calc="2*100"),
        ex("¿Cuál medida es razonable para una pizarra: 2 m o 2 cm?", "2 m", "Una pizarra mide cerca de dos metros."),
    ],
    open_task=task(
        "Elige tres objetos de la lista: lápiz, mesa del colegio, puerta, goma, cama. Para cada uno escribe qué unidad usarías (m o cm) y una medida aproximada que sea razonable.",
        "Lápiz: cm, unos 15 cm. Alto de la puerta: m, cerca de 2 m. Goma: cm, unos 4 cm.",
        ["elige tres objetos de la lista", "dice m o cm para cada uno", "da una medida razonable", "justifica con el tamaño"],
        ["tres objetos con unidad y medida"],
        ["usar m para objetos pequeños", "anotar una medida sin unidad"],
        "Pide comparar la medida con su mano o con una regla si puede. Reconoce que la unidad coincida con el tamaño.",
    ),
    reinforce="Elige dos objetos de tu casa y di si los medirías en cm o en m. Después comprueba con una regla o una huincha si tienes.",
    extend="Estima cuántos centímetros mide tu paso y cuántos pasos harían falta para recorrer 1 metro.",
)

register(
    OA22, 2,
    materials="Regla de 30 cm o una regla dibujada en una hoja. Los ejercicios describen la regla con números, para que puedas resolver aunque no la tengas.",
    use="Aprenderé a medir con la regla empezando en el lugar correcto. Sirve para no equivocarte cuando mides un lápiz o una cinta.",
    prior=["Sé qué es un centímetro.", "Sé restar números hasta 100."],
    explain=[
        "Al medir con una regla, debes poner el objeto donde empieza el 0. Si el objeto empieza en el 0, la medida es el número donde termina. Por ejemplo, un lápiz que empieza en 0 y termina en 14 mide 14 cm.",
        "A veces el objeto no empieza en el 0. Si empieza en la marca 3 y termina en la marca 11, no mide 11 cm. Mide la distancia entre las marcas: 11 − 3 = 8 cm.",
        "Para evitar errores, mira el lugar donde empieza el objeto y el lugar donde termina. Si el borde de la regla está gastado, usa otra marca como inicio y resta. Escribe siempre la medida con su unidad, por ejemplo 8 cm.",
    ],
    vocab=[("origen", "punto donde empieza a contar la medida; en la regla es el 0"), ("marca", "raya con un número en la regla"), ("diferencia", "resultado de restar dos números"), ("medida", "número con su unidad que dice cuán largo es algo")],
    worked=[
        {"title": "Objeto que empieza en 0", "problem": "Una goma empieza en el 0 de la regla y termina en el 5. ¿Cuánto mide?", "steps": ["Empieza en 0, así que no hay que restar.", "Leo dónde termina: 5."], "answer": "Mide 5 cm"},
        {"title": "Objeto que no empieza en 0", "problem": "Un lápiz empieza en la marca 4 y termina en la marca 19. ¿Cuánto mide?", "steps": ["Resto las marcas: 19 − 4.", "19 − 4 = 15."], "answer": "Mide 15 cm"},
    ],
    mistakes=[
        {"wrong": "Decir que un lápiz que va de la marca 4 a la marca 19 mide 19 cm.", "why": "Se lee solo el final y se olvida dónde empezó.", "fix": "Resta el inicio al final: 19 − 4 = 15 cm."},
        {"wrong": "Medir una cinta sin poner su borde en el 0 y no restar.", "why": "No se fija el punto de inicio.", "fix": "Alinea el borde con el 0 o resta las marcas."},
    ],
    tiers={
        "recovery": [
            ex("Una tira empieza en 0 y termina en la marca 12. ¿Cuánto mide?", "12 cm", "Si empieza en 0, la medida es la marca final."),
            arith("Un lápiz empieza en la marca 3 y termina en la marca 18. ¿Cuántos cm mide?", "18-3", "Se resta la marca inicial a la final.", " cm"),
            ex("¿En qué número de la regla se debe poner el borde del objeto para medir fácil?", "0", "El 0 es el origen de la medida."),
        ],
        "understand": [
            ex("Una goma va de la marca 2 a la marca 7. ¿Mide 7 cm? Explica.", "No; mide 5 cm porque empieza en el 2", "7 − 2 = 5.", calc="7-2"),
            arith("Una cinta empieza en la marca 5 y termina en la marca 26. ¿Cuánto mide?", "26-5", "Se resta la marca inicial a la final.", " cm"),
            ex("Un sacapuntas empieza en 0 y termina en 4. Otro empieza en 1 y termina en 6. ¿Cuál mide más?", "El segundo, con 5 cm", "El primero mide 4 cm y el segundo 6 − 1 = 5 cm.", calc="6-1"),
        ],
        "apply": [
            ex("Una hoja va de la marca 0 a la marca 21. ¿Cuántos cm mide de largo?", "21 cm", "Empieza en 0, así que se lee el final."),
            arith("Un lápiz va de la marca 6 a la marca 20. ¿Cuántos cm mide?", "20-6", "Se resta la marca inicial a la final.", " cm"),
            ex("Una regla gastada empieza en la marca 2. Un clip va de la marca 2 a la marca 8. ¿Cuánto mide el clip?", "6 cm", "Se resta 8 − 2.", calc="8-2"),
        ],
        "reason": [
            ex("Ana dice que un lápiz de la marca 3 a la marca 15 mide 15 cm. ¿Qué hizo mal y cuánto mide en realidad?", "No restó el inicio; mide 12 cm", "15 − 3 = 12.", calc="15-3"),
            ex("Dos amigos miden el mismo lápiz. Uno lo pone de 0 a 15 y otro de 5 a 20. ¿Hay diferencia en la medida?", "No; en ambos casos mide 15 cm", "20 − 5 = 15, igual que 15 − 0.", calc="20-5"),
        ],
        "challenge": [
            ex("Una cinta va de la marca 7 a la marca 30. Otra va de la marca 0 a la marca 20. ¿Cuántos cm más larga es la primera?", "3 cm", "La primera mide 23 cm y la segunda 20 cm.", calc="30-7-20"),
            ex("Para dibujar una línea de 12 cm que empiece en la marca 4, ¿en qué marca debe terminar?", "En la marca 16", "4 + 12 = 16.", calc="4+12"),
        ],
    },
    context=[ex("Una regla se rompió y comienza en la marca 3. Medimos un bloque desde 3 hasta 14. ¿Cuántos centímetros mide el bloque?", "11 cm", "Se resta la marca inicial a la final: 14 − 3.", calc="14-3")],
    selfcheck=[
        ex("Un objeto va de la marca 0 a la 9. ¿Cuánto mide?", "9 cm", "Empieza en el 0."),
        ex("Un objeto va de la marca 8 a la 17. ¿Cuánto mide?", "9 cm", "17 − 8 = 9.", calc="17-8"),
        ex("¿Qué debes hacer si el objeto no empieza en 0?", "Restar la marca inicial a la final", "Así mides la distancia entre las dos marcas."),
    ],
    open_task=task(
        "Mide un lápiz, una goma o una hoja con una regla si la tienes. Si no, usa estos datos: lápiz de la marca 2 a la 17, goma de la marca 0 a la 5, hoja de la marca 1 a la 22. Escribe la medida de cada objeto con la resta o la lectura que usaste.",
        "Lápiz: 17 − 2 = 15 cm. Goma: empieza en 0, mide 5 cm.",
        ["identifica dónde empieza cada objeto", "resta cuando no empieza en 0", "escribe la unidad cm", "revisa que la medida sea razonable"],
        ["tres medidas con operación", "unidad escrita"],
        ["leer solo el final", "restar al revés"],
        "Pide mostrar con el dedo dónde empieza y dónde termina cada objeto. Reconoce que use la resta cuando corresponde.",
    ),
    reinforce="Con una regla, mide el largo de tu estuche. Pon el borde en el 0 y escribe la medida.",
    extend="Mide el mismo objeto empezando desde la marca 3 y comprueba que obtienes el mismo resultado después de restar.",
)

register(
    OA22, 3,
    materials="Lápiz y papel. Si tienes una huincha de medir, puedes comprobar que 1 metro llega hasta la marca 100 cm.",
    use="Aprenderé a pasar metros a centímetros y centímetros a metros. Sirve para entender medidas de telas, cintas y alturas.",
    prior=["Sé que 1 m tiene 100 cm.", "Sé multiplicar y dividir por 100 con números pequeños."],
    explain=[
        "Un metro son 100 centímetros. Para pasar de metros a centímetros, multiplicas por 100. Por ejemplo, 3 m son 3 × 100 = 300 cm. Cada metro trae 100 centímetros.",
        "Para pasar de centímetros a metros, divides por 100. 500 cm son 500 ÷ 100 = 5 m. Si no se puede repartir exacto, sobran centímetros: 250 cm son 2 m y 50 cm, porque 2 × 100 = 200 y 250 − 200 = 50.",
        "Si una medida tiene metros y centímetros, convierte los metros y suma los centímetros. 1 m y 20 cm son 100 + 20 = 120 cm. No olvides escribir la unidad: la medida cambia de número pero el largo es el mismo.",
    ],
    vocab=[("transformar", "escribir la misma medida con otra unidad"), ("equivalencia", "dos medidas distintas que valen lo mismo, como 1 m y 100 cm"), ("multiplicar por 100", "pasar de metros a centímetros"), ("dividir por 100", "pasar de centímetros a metros")],
    worked=[
        {"title": "De metros a centímetros", "problem": "Una cinta mide 4 m. ¿Cuántos centímetros mide?", "steps": ["Cada metro tiene 100 cm.", "Multiplico: 4 × 100 = 400."], "answer": "Mide 400 cm"},
        {"title": "De centímetros a metros y centímetros", "problem": "Una tela mide 270 cm. ¿Cuántos metros y centímetros son?", "steps": ["Veo cuántos grupos de 100 caben: 2, porque 2 × 100 = 200.", "Sobran 270 − 200 = 70 cm."], "answer": "Son 2 m y 70 cm"},
    ],
    mistakes=[
        {"wrong": "Decir que 3 m son 30 cm.", "why": "Se multiplica por 10 en vez de 100.", "fix": "1 m = 100 cm, así que 3 m = 300 cm."},
        {"wrong": "Escribir 150 cm como 1 m y 150 cm.", "why": "Se deja todo el número en centímetros.", "fix": "Saca los 100 cm: 150 − 100 = 50. Son 1 m y 50 cm."},
    ],
    tiers={
        "recovery": [
            arith("Una soga mide 2 m. ¿Cuántos cm mide?", "2*100", "Se multiplica por 100 la cantidad de metros.", " cm"),
            arith("Un listón mide 300 cm. ¿Cuántos metros mide?", "300//100", "Se divide por 100 la cantidad de centímetros.", " m"),
            arith("Una cinta mide 5 m. ¿Cuántos cm mide?", "5*100", "Se multiplica por 100 la cantidad de metros.", " cm"),
        ],
        "understand": [
            ex("¿Por cuánto se multiplica para pasar de metros a centímetros?", "Por 100", "Cada metro tiene 100 centímetros."),
            ex("Escribe 250 cm en metros y centímetros.", "2 m y 50 cm", "Caben 2 grupos de 100 y sobran 50.", calc="250-2*100"),
            ex("Una tela mide 1 m y 30 cm. ¿Cuántos cm mide?", "130 cm", "100 + 30 = 130.", calc="100+30"),
        ],
        "apply": [
            arith("Un cordón de zapatilla mide 90 cm. Una cinta mide 1 m. ¿Cuántos cm más larga es la cinta?", "100-90", "Se pasa 1 m a 100 cm y se resta.", " cm"),
            arith("Una mesa mide 2 m de largo. ¿Cuántos cm mide?", "2*100", "Se multiplica por 100 la cantidad de metros.", " cm"),
            ex("Una pared mide 4 m y 20 cm. ¿Cuántos cm mide?", "420 cm", "4 × 100 = 400 y se suman 20.", calc="4*100+20"),
        ],
        "reason": [
            ex("Ema dice que 3 m son 30 cm. ¿Tiene razón? Explica con la regla de 100.", "No; 3 m son 300 cm", "1 m = 100 cm, entonces 3 × 100 = 300."),
            ex("¿Es verdad que 150 cm miden más de 1 m? Explica.", "Sí; 150 cm son 1 m y 50 cm", "150 − 100 = 50 cm de más.", calc="150-100"),
        ],
        "challenge": [
            ex("Pablo tiene una cinta de 3 m y recorta 1 m y 20 cm. ¿Cuántos cm quedan?", "180 cm", "300 − 120 = 180.", calc="300-120"),
            ex("Una pared mide 600 cm. ¿Cuántos metros mide?", "6 m", "600 ÷ 100 = 6.", calc="600//100"),
        ],
    },
    context=[ex("Para decorar una pared, Lola necesita una guirnalda de 5 m. Compró 4 tramos de 120 cm. ¿Alcanza? Responde con la cantidad de cm que le sobran o le faltan.", "No alcanza; le faltan 20 cm", "4 × 120 = 480 cm y 5 m son 500 cm; 500 − 480 = 20.", calc="500-4*120")],
    selfcheck=[
        ex("¿Cuántos cm son 7 m?", "700", "7 × 100 = 700.", calc="7*100"),
        ex("¿Cuántos metros son 800 cm?", "8", "800 ÷ 100 = 8.", calc="800//100"),
        ex("Escribe 1 m y 45 cm en cm.", "145 cm", "100 + 45 = 145.", calc="100+45"),
    ],
    open_task=task(
        "Elige una medida de la lista: una tela de 3 m, una soga de 2 m y 40 cm, un tablón de 450 cm. Conviértela: a cm si está en metros, a metros y cm si está en cm. Escribe la operación.",
        "Tablón de 450 cm: 4 × 100 = 400 y sobran 50, entonces mide 4 m y 50 cm.",
        ["elige una medida de la lista", "usa 1 m = 100 cm", "muestra la operación", "escribe la unidad"],
        ["operación escrita", "respuesta con unidad"],
        ["multiplicar por 10", "olvidar sumar los centímetros extra"],
        "Pide comprobar convirtiendo de vuelta. Reconoce que el largo no cambia aunque cambie el número.",
    ),
    reinforce="Mide con una huincha o una cinta algo de tu casa y escribe su medida en cm y en m y cm.",
    extend="Calcula cuántos centímetros hay en 10 m y explica cómo lo calculaste.",
)

register(
    OA22, 4,
    materials="Lápiz y papel. Todos los datos están escritos en los ejercicios. Recuerda: 1 m = 100 cm.",
    use="Aprenderé a resolver problemas donde aparecen metros y centímetros juntos. Sirve para cortar cintas, medir telas y comparar alturas.",
    prior=["Sé pasar de m a cm y de cm a m.", "Sé sumar y restar números hasta 1.000."],
    explain=[
        "En muchos problemas, las medidas vienen en unidades distintas. Antes de sumar, restar o comparar, pasa todas las medidas a la misma unidad. Lo más simple suele ser pasarlas todas a centímetros.",
        "Por ejemplo, una cinta de 2 m y otra de 50 cm: 2 m son 200 cm, y 200 + 50 = 250 cm en total. Si te piden la respuesta en metros, puedes volver: 250 cm son 2 m y 50 cm.",
        "Después revisa si la respuesta es razonable. Si una puerta mide 20 m, algo anda mal. Para comprobar, convierte de vuelta a la unidad inicial. Escribe siempre la unidad en la respuesta.",
    ],
    vocab=[("unidad común", "la misma unidad para todas las medidas del problema"), ("comparar", "decir cuál medida es mayor, menor o si son iguales"), ("sobrante", "lo que queda después de cortar o gastar una parte"), ("razonable", "que tiene sentido en la situación")],
    worked=[
        {"title": "Sumar medidas en unidades distintas", "problem": "Una cinta mide 2 m y otra mide 50 cm. ¿Cuántos cm miden juntas?", "steps": ["Paso 2 m a cm: 2 × 100 = 200.", "Sumo: 200 + 50 = 250."], "answer": "Miden 250 cm juntas"},
        {"title": "Comparar y restar", "problem": "Una tela mide 3 m y se usa 1 m y 20 cm. ¿Cuántos cm quedan?", "steps": ["Paso todo a cm: 3 m = 300 cm y 1 m 20 cm = 120 cm.", "Resto: 300 − 120 = 180."], "answer": "Quedan 180 cm"},
    ],
    mistakes=[
        {"wrong": "Sumar 2 m y 50 cm como 52.", "why": "Se suman números con unidades distintas.", "fix": "Pasa a cm: 200 + 50 = 250 cm."},
        {"wrong": "Restar 1 m menos 20 cm como 1 − 20.", "why": "No se convirtió la medida a una unidad común.", "fix": "100 cm − 20 cm = 80 cm."},
    ],
    tiers={
        "recovery": [
            arith("Una cuerda mide 2 m y otra mide 100 cm. ¿Cuántos cm miden juntas?", "2*100+100", "Se pasa 2 m a cm y se suma.", " cm"),
            arith("Una cinta de 1 m se corta en un trozo de 40 cm. ¿Cuántos cm quedan?", "100-40", "Se pasa 1 m a 100 cm y se resta.", " cm"),
            ex("¿Qué debes hacer antes de sumar 3 m con 60 cm?", "Pasar todo a la misma unidad", "Así sumas números que cuentan lo mismo."),
        ],
        "understand": [
            ex("Una cinta mide 1 m y 20 cm. ¿Cuántos cm mide?", "120 cm", "100 + 20 = 120.", calc="100+20"),
            ex("¿Es mayor 2 m o 150 cm? Explica pasando a cm.", "2 m, porque son 200 cm", "200 es mayor que 150.", calc="2*100"),
            ex("Dos tablas miden 80 cm cada una. ¿Cuántos cm miden juntas y es más o menos de 1 m?", "160 cm, más de 1 m", "80 + 80 = 160 y 160 es mayor que 100.", calc="80+80"),
        ],
        "apply": [
            ex("Marta tiene una cinta de 2 m. Corta 3 trozos de 50 cm. ¿Cuántos cm le quedan?", "50 cm", "2 m son 200 cm; 3 × 50 = 150 y 200 − 150 = 50.", calc="200-3*50"),
            arith("Un tren de juguete tiene 3 vagones de 25 cm cada uno. ¿Cuántos cm mide en total?", "3*25", "Se multiplica el largo de un vagón por 3.", " cm"),
            ex("Luis mide 1 m y 30 cm y su hermana 1 m y 15 cm. ¿Cuántos cm más alto es Luis?", "15 cm", "130 − 115 = 15.", calc="130-115"),
        ],
        "reason": [
            ex("Un estudiante sumó 2 m y 50 cm y respondió 52. ¿Qué error cometió y cuál es la respuesta correcta en cm?", "Sumó números con unidades distintas; son 250 cm", "2 m = 200 cm y 200 + 50 = 250.", calc="200+50"),
            ex("Se necesitan 4 m de cinta para decorar. Hay 3 rollos de 120 cm. ¿Alcanza? Explica.", "No; 3 rollos suman 360 cm y se necesitan 400 cm", "3 × 120 = 360, que es menos que 400.", calc="3*120"),
        ],
        "challenge": [
            ex("En 1 m caben 2 tablas de 50 cm puestas una tras otra. ¿Cuántas tablas se necesitan para cubrir un camino de 10 m?", "20 tablas", "Son 2 tablas por cada metro: 10 × 2 = 20.", calc="10*2"),
            ex("En 1 m caben 4 trozos de 25 cm. Una tira de 5 m se corta en trozos de 25 cm. ¿Cuántos trozos salen?", "20 trozos", "Son 4 trozos por cada metro: 5 × 4 = 20.", calc="5*4"),
        ],
    },
    context=[ex("Un cordel de 3 m sirve para colgar dibujos. Cada dibujo ocupa 25 cm de ancho y se cuelgan 8 dibujos, uno al lado del otro. ¿Cuántos cm del cordel quedan libres?", "100 cm", "8 × 25 = 200 cm y 3 m son 300 cm; 300 − 200 = 100.", calc="300-8*25")],
    selfcheck=[
        ex("¿Cuántos cm son 2 m y 10 cm?", "210 cm", "200 + 10 = 210.", calc="200+10"),
        ex("Una tabla de 1 m se corta en un trozo de 35 cm. ¿Cuántos cm quedan?", "65 cm", "100 − 35 = 65.", calc="100-35"),
        ex("¿Qué pasa si sumas metros con centímetros sin convertir?", "El resultado es incorrecto", "Las unidades son distintas y no se pueden juntar así."),
    ],
    open_task=task(
        "Resuelve un problema con la cinta: tienes una cinta de 3 m. Elige una de estas opciones: cortar 5 trozos de 40 cm, cortar 2 trozos de 1 m y 20 cm, o cortar 3 trozos de 75 cm. Calcula cuántos cm gastas y cuántos cm te sobran. Muestra las operaciones.",
        "5 trozos de 40 cm: 5 × 40 = 200 cm gastados; 300 − 200 = 100 cm sobran.",
        ["elige una de las tres opciones", "pasa 3 m a cm", "calcula lo que se gasta", "calcula lo que sobra y escribe la unidad"],
        ["operaciones escritas", "gasto y sobrante con unidad"],
        ["no convertir 3 m a cm", "olvidar la unidad"],
        "Pide revisar si lo que sobra es razonable. Reconoce el uso de una unidad común.",
    ),
    reinforce="Mide dos objetos de tu casa con regla o huincha. Escribe sus medidas en cm y suma sus largos.",
    extend="Una persona da pasos de 50 cm. Dos pasos de 50 cm hacen 1 m. Calcula cuántos pasos da para recorrer 10 m.",
)
