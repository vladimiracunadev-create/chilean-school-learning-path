"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 13 (características de océanos y lagos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA13 = "CN05 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 13, clase 1
register(
    OA13, 1,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno; no hace falta ir al mar ni a un lago.",
    use="Aprenderé a leer cómo cambian la temperatura, la luz y la presión del agua cuando aumenta la profundidad, y a separar lo que muestran los datos de lo que yo supongo. Sirve para entender cómo es el interior de un océano o de un lago.",
    prior=["Sé leer una tabla con unidades.", "Sé que la luz del Sol calienta el agua de la superficie."],
    explain=[
        "La profundidad es la distancia desde la superficie del agua hacia el fondo. En los océanos y en los lagos grandes, algunas características cambian con la profundidad. Tres de ellas son la temperatura, la luminosidad y la presión.",
        "La temperatura baja al aumentar la profundidad: en general, el agua de la superficie está más tibia y la del fondo es más fría. La luminosidad es la cantidad de luz. También disminuye: cerca de la superficie hay luz del Sol, y a unos 200 metros ya llega muy poca. Bajo unos 1.000 metros no llega nada de luz del Sol.",
        "La presión es la fuerza que el agua ejerce sobre un cuerpo. Aumenta con la profundidad, porque hay más agua encima que pesa. Cada 10 metros que bajas, la presión suma aproximadamente 1 atmósfera (atm). En la superficie es 1 atm. En esta clase los datos de temperatura son de ejemplo, no una medición real.",
    ],
    vocab=[("profundidad", "distancia desde la superficie del agua hacia abajo"), ("luminosidad", "cantidad de luz que hay en un lugar"), ("presión", "fuerza que el agua ejerce sobre un cuerpo, repartida en toda su superficie"), ("atmósfera (atm)", "unidad de presión; en la superficie es 1 atm"), ("variable", "algo que puede cambiar en una observación")],
    worked=[
        {"title": "Leer una tabla de temperatura", "problem": "Datos de ejemplo: a 0 m hay 20 °C, a 100 m hay 15 °C, a 500 m hay 8 °C y a 1.000 m hay 4 °C. ¿Cuánto bajó la temperatura de 0 m a 1.000 m?", "steps": ["En la superficie hay 20 °C y a 1.000 m hay 4 °C.", "Resto: 20 − 4 = 16."], "answer": "16 °C"},
        {"title": "Calcular la presión", "problem": "En la superficie la presión es 1 atm y suma 1 atm cada 10 m. ¿Cuál es la presión a 30 m?", "steps": ["En 30 m hay 3 tramos de 10 m, entonces suma 3 atm.", "La presión es 1 + 3 = 4."], "answer": "4 atm"},
    ],
    mistakes=[
        {"wrong": "Decir que a más profundidad el agua está más caliente.", "why": "Se piensa que el fondo guarda el calor del Sol.", "fix": "Mira la tabla: la temperatura baja al aumentar la profundidad."},
        {"wrong": "Usar los datos de 100 m y de 500 m para afirmar con seguridad el valor exacto a 300 m.", "why": "Se inventa un dato que no se midió.", "fix": "Di que probablemente estará entre ambos valores, sin dar una cifra segura."},
    ],
    tiers={
        "recovery": [
            ex("En la tabla de ejemplo (0 m: 20 °C; 100 m: 15 °C; 500 m: 8 °C; 1.000 m: 4 °C), ¿qué temperatura hay a 500 m?", "8 °C", "Se lee directo de la tabla."),
            ex("Al bajar más profundo en el mar, ¿la luz del Sol aumenta o disminuye?", "Disminuye", "A mayor profundidad llega menos luz."),
            ex("Al bajar más profundo en el agua, ¿la presión aumenta o disminuye?", "Aumenta", "Hay más agua encima, que pesa."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la presión del agua?", "La fuerza que el agua ejerce sobre un cuerpo", "La presión es una fuerza repartida sobre una superficie."),
            ex("Lee esta frase: «A 1.000 m, la temperatura del ejemplo es 4 °C». ¿Es una observación o una interpretación?", "Observación", "Es un dato que está en la tabla."),
            ex("Lee esta frase: «El agua se enfría porque el Sol no llega hasta el fondo». ¿Es una observación o una interpretación?", "Interpretación", "Es una explicación que se agrega al dato."),
        ],
        "apply": [
            arith("Con la tabla de ejemplo, ¿cuántos °C baja la temperatura entre 0 m (20 °C) y 1.000 m (4 °C)?", "20-4", "Se resta la temperatura del fondo a la de la superficie.", " °C"),
            arith("La presión en la superficie es 1 atm y suma 1 atm cada 10 m. ¿Cuál es la presión a 50 m de profundidad?", "1+50//10", "Hay 5 tramos de 10 m, y se suma la presión de la superficie.", " atm"),
            ex("Una buzo profesional baja 20 m en el mar. ¿La presión sobre su cuerpo será mayor o menor que en la superficie?", "Mayor", "Más profundidad significa más presión."),
        ],
        "reason": [
            ex("Laura dice: «a 100 m hay 15 °C y a 500 m hay 8 °C, así que a 300 m hay exactamente 11 °C». ¿Qué error comete?", "Inventa un dato que no se midió; solo puede decir que estará entre 15 °C y 8 °C", "La tabla no tiene dato a 300 m."),
            ex("Un lago profundo tiene 18 °C en la superficie y 6 °C en el fondo. ¿Qué patrón comparte con el océano de la tabla?", "La temperatura baja al aumentar la profundidad", "En ambos casos el fondo es más frío."),
        ],
        "challenge": [
            arith("La presión es 1 atm en la superficie y suma 1 atm cada 10 m. ¿A cuántos metros de profundidad la presión llega a 8 atm?", "(8-1)*10", "Se restan los 7 atm que se suman al bajar y se multiplican por 10 m.", " m"),
            ex("Un alga necesita luz para fabricar su alimento. ¿Dónde esperas encontrarla: a 50 m o a 800 m de profundidad?", "A 50 m", "A 800 m casi no llega luz del Sol."),
        ],
    },
    context=[ex("Una buceadora siente que le aprietan los oídos al bajar a 5 m en una piscina profunda. ¿Con qué característica del agua se relaciona esa sensación?", "Con el aumento de la presión", "La presión crece con la profundidad y se nota en los oídos.")],
    selfcheck=[
        ex("¿Qué pasa con la temperatura del agua al aumentar la profundidad?", "Baja", "El agua más profunda es más fría."),
        ex("¿Qué pasa con la presión al aumentar la profundidad?", "Aumenta", "Hay más agua encima."),
        ex("¿Qué pasa con la luz al aumentar la profundidad?", "Disminuye", "Llega menos luz del Sol."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo de un lago: superficie 18 °C, a 10 m 14 °C, a 30 m 9 °C, a 50 m 6 °C. Dibuja un gráfico simple con la profundidad hacia abajo y escribe tres observaciones y una interpretación. Marca cuál es cuál.",
        "Observación: a 30 m hay 9 °C. Observación: la temperatura baja 12 °C de la superficie a 50 m. Interpretación: el Sol calienta solo el agua cercana a la superficie.",
        ["gráfico o dibujo con la profundidad", "tres observaciones tomadas de los datos", "una interpretación marcada"],
        ["gráfico", "frases rotuladas"],
        ["inventar valores que no están", "mezclar observación e interpretación"],
        "Pregunta qué dato apoyó su interpretación.",
    ),
    reinforce="Haz una tabla con tres profundidades y escribe cómo cambia la presión en cada una.",
    extend="Averigua con una persona de tu casa por qué los buzos usan equipos especiales cuando bajan muy profundo.",
)

# ---------------------------------------------------------------- OA 13, clase 2
register(
    OA13, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a hacer preguntas y predicciones sobre cómo cambia la flora y la fauna de océanos y lagos con la profundidad. Sirve para explicar por qué ciertos seres vivos viven en un lugar y no en otro.",
    prior=["Sé que las plantas y las algas fabrican su alimento con luz.", "Sé que la luz, la temperatura y la presión cambian con la profundidad."],
    explain=[
        "La flora son las plantas y las algas de un lugar, y la fauna son los animales. En océanos y lagos, los seres vivos no se reparten al azar: dependen de la luz, la temperatura y la presión. La diversidad es la variedad de especies distintas que viven en un lugar.",
        "Cerca de la superficie, donde llega la luz del Sol, viven algas, plantas acuáticas y muchos animales, porque ahí hay alimento. Un ejemplo es el cochayuyo, un alga que vive pegada a las rocas de la costa de Chile. En la zona oscura, bajo unos 200 metros, no hay algas, pues no pueden fabricar su alimento sin luz.",
        "Aun así, en el fondo viven animales. Se alimentan de restos que caen desde arriba, y algunos producen su propia luz. A mayor profundidad hay menos especies. En un lago ocurre algo parecido: las plantas crecen cerca de la orilla, donde el agua es poco profunda y llega luz. En esta clase, las cifras son datos de ejemplo.",
    ],
    vocab=[("flora", "plantas y algas de un lugar"), ("fauna", "animales de un lugar"), ("diversidad", "variedad de especies distintas en un lugar"), ("zona iluminada", "parte del agua a la que llega luz del Sol, hasta unos 200 m"), ("zona oscura", "parte del agua a la que casi no llega luz del Sol")],
    worked=[
        {"title": "Predecir dónde viven las algas", "problem": "Las algas necesitan luz. ¿Dónde predices que habrá más algas: a 20 m o a 900 m de profundidad?", "steps": ["Las algas fabrican su alimento con luz solar.", "A 20 m llega luz; a 900 m casi no llega."], "answer": "A 20 m, porque ahí llega la luz que necesitan"},
        {"title": "Contar zona oscura", "problem": "La zona iluminada llega hasta 200 m. Un robot explorador baja a 1.000 m. ¿Cuántos metros recorre dentro de la zona oscura?", "steps": ["Pasa por la zona oscura desde los 200 m.", "Resto: 1.000 − 200 = 800."], "answer": "800 m"},
    ],
    mistakes=[
        {"wrong": "Decir que en el fondo no hay vida porque no hay luz.", "why": "Se cree que sin luz del Sol no puede vivir nada.", "fix": "Hay animales que se alimentan de restos que caen desde arriba, y algunos producen su propia luz."},
        {"wrong": "Pensar que mientras más profundo, más especies hay.", "why": "Se confunde profundidad con variedad.", "fix": "La mayor variedad está donde llega la luz, cerca de la superficie y de la costa."},
    ],
    tiers={
        "recovery": [
            ex("Las algas fabrican su alimento con luz del Sol. ¿Viven en la zona iluminada o en la zona oscura?", "En la zona iluminada", "Sin luz no pueden fabricar su alimento."),
            ex("¿Llega luz del Sol a 2.000 m de profundidad en el mar?", "No", "La luz solar solo llega hasta unos 200 m con fuerza suficiente para las algas."),
            ex("El cochayuyo es un alga que vive pegada a las rocas de la costa. ¿Esperas encontrarla en agua poco profunda o en el fondo oscuro?", "En agua poco profunda", "Necesita luz para vivir."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la diversidad de seres vivos de un lugar?", "La variedad de especies distintas que viven en él", "Diversidad es cuántas clases de seres vivos hay."),
            ex("Dato de ejemplo: entre 0 y 200 m se cuentan 40 especies; bajo 1.000 m se cuentan 6. ¿En qué zona hay más diversidad?", "Entre 0 y 200 m", "40 especies es mayor que 6."),
            ex("¿Por qué no hay algas en la zona oscura?", "Porque sin luz no pueden fabricar su alimento", "Las algas necesitan luz para vivir."),
        ],
        "apply": [
            ex("De estos dos seres vivos, ¿cuál vive en la zona oscura: una alga microscópica que fabrica su alimento con luz o un pez que produce su propia luz a 1.500 m?", "El pez que produce su propia luz", "El alga necesita la luz del Sol y la zona oscura no la tiene."),
            arith("La zona iluminada llega hasta 200 m. Un submarino baja hasta 3.000 m. ¿Cuántos metros recorre dentro de la zona oscura?", "3000-200", "Se resta el tramo iluminado a la profundidad total.", " m"),
            ex("Un lago tiene una orilla de poca profundidad y un centro muy profundo. ¿Dónde esperas que crezcan más plantas acuáticas?", "En la orilla", "Allí llega luz hasta el fondo."),
        ],
        "reason": [
            ex("Tomás dice: «en el fondo del mar no hay vida porque no hay plantas». ¿Qué dato de la clase lo contradice?", "En la zona oscura viven animales que se alimentan de restos que caen desde arriba", "Hay vida aunque no haya algas."),
            ex("Daniela afirma: «mientras más profundo, más especies hay». Con los datos de ejemplo (40 especies entre 0 y 200 m y 6 bajo 1.000 m), ¿tiene razón?", "No, hay menos especies a mayor profundidad", "6 es menor que 40."),
        ],
        "challenge": [
            ex("El fitoplancton son algas microscópicas que sirven de alimento a peces pequeños. Si el agua se vuelve tan turbia que no deja pasar la luz, ¿qué predices que pasará con el fitoplancton?", "Disminuirá", "Sin luz no puede fabricar su alimento."),
            arith("Un estudiante cuenta en un lago de ejemplo 12 especies cerca de la orilla y 5 en el centro profundo. ¿Cuántas especies más hay en la orilla?", "12-5", "Se resta el centro de la orilla.", " especies"),
        ],
    },
    context=[ex("Un pescador de lago nota que hay más peces cerca de la orilla con plantas que en el centro profundo. ¿Qué característica del agua poco profunda puede explicarlo?", "Llega luz, hay plantas y alimento", "Las plantas dan alimento y refugio a los peces.")],
    selfcheck=[
        ex("¿Dónde hay más diversidad: cerca de la superficie o en el fondo oscuro?", "Cerca de la superficie", "Allí llega la luz y hay más alimento."),
        ex("¿Qué necesitan las algas para fabricar su alimento?", "Luz", "Sin luz no hay fabricación de alimento."),
        ex("¿Cómo se llama el conjunto de animales de un lugar?", "Fauna", "La flora son las plantas y algas."),
    ],
    open_task=task(
        "Dibuja un corte de un océano con tres franjas: de 0 a 200 m, de 200 a 1.000 m y bajo 1.000 m. En cada franja escribe una predicción con «Si…, entonces…» sobre qué tipo de seres vivos podrían vivir según la luz, la temperatura y la presión. Usa los datos de ejemplo de la clase.",
        "0 a 200 m: si llega luz, entonces hay algas y muchos peces. 200 a 1.000 m: si llega muy poca luz, entonces no hay algas, pero sí algunos animales. Bajo 1.000 m: si no llega luz, entonces solo viven animales que comen restos que caen o producen su luz.",
        ["tres franjas rotuladas", "una predicción por franja", "relaciona con la luz"],
        ["dibujo del corte", "tres predicciones"],
        ["poner algas en la zona oscura", "decir que no hay vida abajo"],
        "Pregunta qué evidencia necesitaría para comprobar cada predicción.",
    ),
    reinforce="Escribe dos seres vivos que vivan cerca de la superficie y explica por qué necesitan luz.",
    extend="Averigua qué es la bioluminiscencia y escribe un ejemplo de animal marino que la tenga.",
)

# ---------------------------------------------------------------- OA 13, clase 3
register(
    OA13, 3,
    materials="Una bandeja o fuente con un poco de agua de la llave, solo si una persona de tu casa te acompaña; si no, usa los datos escritos. Seca el agua derramada.",
    use="Aprenderé a explicar las olas y las mareas con un modelo sencillo. Sirve para entender por qué el mar se mueve y por qué es peligroso quedarse en la orilla sin saberlo.",
    prior=["Sé que el viento puede mover objetos livianos.", "Sé que la Luna es un cuerpo que gira alrededor de la Tierra."],
    explain=[
        "Las olas se forman cuando el viento empuja la superficie del agua. El agua sube y baja en el lugar, y lo que avanza es la forma de la ola. Un modelo simple es soplar sobre una bandeja con agua: aparecen ondas.",
        "Las mareas son la subida y la bajada del nivel del mar. Se producen principalmente por la atracción de la Luna y, en menor medida, del Sol. Cuando el mar está más alto se llama pleamar o marea alta, y cuando está más bajo, bajamar o marea baja. En muchas costas hay dos mareas altas y dos bajas al día, con unas 6 horas de diferencia entre una alta y una baja.",
        "Los lagos también tienen olas, producidas por el viento, pero casi no tienen mareas porque son pequeños comparados con el océano. El modelo de la bandeja tiene límites: no muestra la Luna ni la profundidad real del mar. Para observar el mar, ve siempre con una persona adulta.",
    ],
    vocab=[("ola", "onda de la superficie del agua producida por el viento"), ("marea", "subida y bajada del nivel del mar"), ("pleamar", "momento en que el mar está más alto"), ("bajamar", "momento en que el mar está más bajo"), ("modelo", "representación simple de algo para estudiarlo")],
    worked=[
        {"title": "Horas entre mareas", "problem": "En un puerto de ejemplo hay marea alta a las 03:00 y marea baja a las 09:00. ¿Cuántas horas pasan entre ambas?", "steps": ["Parto en las 03:00 y llego a las 09:00.", "Calculo 9 − 3 = 6."], "answer": "6 horas"},
        {"title": "Qué representa el soplido", "problem": "En una bandeja con agua soplas y se forman olitas. ¿Qué representa tu soplido en el modelo?", "steps": ["Las olas del mar se forman por el viento.", "El soplido empuja el agua como el viento."], "answer": "El viento"},
    ],
    mistakes=[
        {"wrong": "Decir que las mareas las produce el viento.", "why": "Se mezclan olas y mareas.", "fix": "El viento produce olas; las mareas se deben a la atracción de la Luna y del Sol."},
        {"wrong": "Pensar que el agua de una ola avanza completa hasta la playa.", "why": "Se mira solo el movimiento de la espuma.", "fix": "En el agua abierta sube y baja; lo que avanza es la forma de la ola."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué produce las olas más comunes: el viento o la Luna?", "El viento", "El viento empuja la superficie del agua."),
            ex("¿Cómo se llama el momento en que el mar está más alto: pleamar o bajamar?", "Pleamar", "Pleamar es marea alta."),
            ex("¿Qué cuerpo del cielo influye más en las mareas?", "La Luna", "Su atracción levanta el agua del mar."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una marea?", "La subida y la bajada del nivel del mar", "No es una corriente ni una ola."),
            ex("En una bandeja con agua, soplas y aparecen olitas. ¿Qué representa tu soplido?", "El viento", "El viento es lo que forma las olas del mar."),
            ex("En el mar abierto, ¿qué avanza con la ola: la forma de la ola o toda el agua?", "La forma de la ola", "El agua sube y baja casi en el mismo lugar."),
        ],
        "apply": [
            arith("En otro puerto de ejemplo hay marea baja a las 07:00 y la siguiente marea alta a las 13:00. ¿Cuántas horas pasan entre ambas?", "13-7", "Se resta la hora de la marea baja a la de la marea alta.", " horas"),
            arith("En el mismo puerto de ejemplo hay mareas altas a las 03:00 y a las 15:00. ¿Cuántas horas pasan entre las dos mareas altas?", "15-3", "Se restan las horas de las dos mareas altas.", " horas"),
            ex("En un puerto de ejemplo hay marea alta a las 03:00 y 15:00, y marea baja a las 09:00 y 21:00. ¿Cómo estará la marea a las 21:00?", "Baja", "A las 21:00 está en la marea baja del ejemplo."),
        ],
        "reason": [
            ex("Un compañero dice que las mareas ocurren por el viento. ¿Es correcto?", "No, el viento produce olas y las mareas se deben a la atracción de la Luna y del Sol", "Son dos fenómenos con causas distintas."),
            ex("En un lago pequeño hay olas con viento, pero casi no hay mareas. ¿Cuál es una explicación posible?", "El viento mueve la superficie y el lago es muy pequeño comparado con el océano para que la atracción de la Luna se note", "Las mareas se notan en masas de agua muy grandes."),
        ],
        "challenge": [
            arith("En una bahía de ejemplo el nivel del mar en marea alta es 3 m y en marea baja es 1 m. ¿Cuántos metros sube el mar de la marea baja a la alta?", "3-1", "Se resta el nivel bajo al alto.", " m"),
            ex("El modelo de la bandeja tiene una limitación. ¿Cuál es: (a) no muestra la Luna ni la profundidad real del mar, o (b) muestra exactamente el océano?", "(a)", "Un modelo simple no reproduce todos los elementos del fenómeno."),
        ],
    },
    context=[ex("Una familia quiere pasear por unas rocas de la orilla, que quedan cubiertas cuando la marea está alta. ¿Qué dato debe averiguar antes de ir, con una persona adulta?", "La hora de la marea alta y de la marea baja", "Así saben cuándo el agua cubre las rocas.")],
    selfcheck=[
        ex("¿Qué forma las olas?", "El viento", "El viento empuja la superficie."),
        ex("¿Cuál es la causa principal de las mareas?", "La atracción de la Luna", "La Luna influye más que el Sol por estar más cerca."),
        ex("¿Qué es la bajamar?", "El momento en que el mar está más bajo", "Es la marea baja."),
    ],
    open_task=task(
        "Con una persona de tu casa, sopla suavemente sobre una bandeja con agua y mira las olitas, o imagina el modelo si no tienes bandeja. Luego usa esta tabla de ejemplo: marea alta 03:00 y 15:00; marea baja 09:00 y 21:00. Escribe qué representa cada elemento de tu modelo, a qué horas de la tabla el mar está más bajo y una regla de seguridad para pasear por la orilla de rocas.",
        "Soplido = viento; agua = mar. El mar está más bajo a las 09:00 y a las 21:00. Regla de seguridad: ir de día y con una persona adulta, y salir de las rocas antes de que suba la marea.",
        ["relaciona el soplido con el viento", "usa la tabla para elegir las horas de marea baja", "nombra una regla de seguridad"],
        ["frases del modelo", "dos horas y una regla de seguridad"],
        ["elegir horas de marea alta", "no nombrar una regla de seguridad"],
        "Pregunta qué cambiaría en el modelo para mostrar las mareas.",
    ),
    reinforce="Dibuja una playa en marea alta y otra en marea baja.",
    extend="Averigua en un calendario de mareas de tu región a qué hora será la próxima marea alta.",
)

# ---------------------------------------------------------------- OA 13, clase 4
register(
    OA13, 4,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a comparar con un criterio común dos corrientes del océano Pacífico: la de Humboldt y El Niño. Sirve para entender por qué cambian el clima, la pesca y la vida en la costa de Chile.",
    prior=["Sé que el agua del mar se mueve.", "Sé comparar temperaturas con una resta."],
    explain=[
        "Una corriente marina es una masa de agua que se mueve de manera continua en una dirección por el océano. Hay corrientes frías y corrientes cálidas.",
        "La corriente de Humboldt es una corriente fría que viaja de sur a norte por la costa de Chile y del Perú. Trae aguas frías y ricas en nutrientes, por eso hay muchas algas y muchos peces, como la anchoveta y la sardina. También hace que la costa del norte de Chile sea más fresca y con neblinas.",
        "El Niño es un fenómeno en el que, cada varios años, el agua superficial del Pacífico cerca de la costa de Sudamérica se calienta más de lo normal. No es lo mismo que la corriente de Humboldt: la altera. Con El Niño suele haber menos peces y, en varias zonas de Chile, más lluvia. Para comparar un año normal con un año de El Niño usamos el mismo criterio: la misma profundidad y la misma unidad. Los datos son de ejemplo.",
    ],
    vocab=[("corriente marina", "masa de agua que se mueve de forma continua por el océano"), ("corriente de Humboldt", "corriente fría que recorre la costa de Chile de sur a norte"), ("El Niño", "calentamiento del agua del Pacífico frente a Sudamérica que ocurre cada varios años"), ("nutrientes", "sustancias del agua que alimentan a algas y otros seres vivos"), ("criterio común", "regla igual para todos los datos comparados")],
    worked=[
        {"title": "Diferencia de temperatura", "problem": "Datos de ejemplo: frente a una costa, la temperatura del mar es 17 °C en un año normal y 21 °C en un año de El Niño. ¿Cuántos grados más cálido es el mar en El Niño?", "steps": ["Los dos datos están en °C y a la misma profundidad.", "Resto: 21 − 17 = 4."], "answer": "4 °C más cálido"},
        {"title": "Elegir criterio común", "problem": "El equipo A midió el mar a 10 m de profundidad y el equipo B a 100 m. ¿Pueden comparar sus datos?", "steps": ["La temperatura cambia con la profundidad.", "Para comparar, ambos deben medir a la misma profundidad."], "answer": "No, deben usar la misma profundidad"},
    ],
    mistakes=[
        {"wrong": "Creer que El Niño y la corriente de Humboldt son la misma cosa.", "why": "Ambos se relacionan con el mar frío o cálido frente a Chile.", "fix": "Humboldt es una corriente fría siempre presente; El Niño es un calentamiento que ocurre cada varios años."},
        {"wrong": "Comparar datos medidos a distintas profundidades.", "why": "Se compara sin un criterio común.", "fix": "Mide o compara siempre a la misma profundidad."},
    ],
    tiers={
        "recovery": [
            ex("La corriente de Humboldt, ¿es fría o cálida?", "Fría", "Trae agua fría desde el sur."),
            ex("La corriente de Humboldt recorre la costa de Chile, ¿de sur a norte o de norte a sur?", "De sur a norte", "Viaja hacia el norte por la costa."),
            ex("Durante El Niño, ¿el agua del mar frente a Sudamérica está más cálida o más fría de lo normal?", "Más cálida", "El Niño es un calentamiento del agua."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una corriente marina?", "Una masa de agua que se mueve de forma continua por el océano", "No es una ola ni una marea."),
            ex("La corriente de Humboldt trae aguas ricas en nutrientes. ¿Hay muchos o pocos peces donde llega?", "Muchos", "Los nutrientes alimentan algas, y las algas alimentan a los peces."),
            ex("Durante El Niño, ¿la pesca suele aumentar o disminuir?", "Disminuir", "Hay menos nutrientes y menos alimento para los peces."),
        ],
        "apply": [
            arith("Datos de ejemplo de otra costa: el mar marca 15 °C en un año normal y 20 °C en un año de El Niño, a la misma profundidad. ¿Cuántos °C más cálido está en El Niño?", "20-15", "Se resta la temperatura normal a la del Niño.", " °C"),
            arith("En una caleta de ejemplo se pescan 100 toneladas en un año normal y 40 toneladas en un año de El Niño. ¿Cuántas toneladas menos se pescan?", "100-40", "Se resta lo pescado en El Niño a lo normal.", " toneladas"),
            ex("Un pescador mide el mar y anota 17 °C. Según los datos de ejemplo, ¿es un año normal o de El Niño?", "Un año normal", "Para el ejemplo, 17 °C corresponde al año normal."),
        ],
        "reason": [
            ex("Sofía dice que El Niño y la corriente de Humboldt son lo mismo. ¿Qué le dirías?", "Humboldt es una corriente fría siempre presente y El Niño es un calentamiento que ocurre cada varios años", "Son fenómenos distintos."),
            ex("Dos equipos miden la temperatura del mar, uno a 5 m y otro a 200 m, y comparan sus números. ¿Qué deben cambiar para que la comparación sea justa?", "Medir los dos a la misma profundidad", "Hace falta un criterio común, porque la temperatura cambia con la profundidad."),
        ],
        "challenge": [
            arith("En tres meses seguidos de un año de El Niño, los datos de ejemplo del mar son 20 °C, 21 °C y 22 °C. ¿Cuántos °C subió el mar entre el primer y el tercer mes?", "22-20", "Se resta el primer dato al tercero.", " °C"),
            ex("Durante El Niño llega menos agua fría y rica en nutrientes a la costa. ¿Qué predices que pasará con la cantidad de algas que alimentan a los peces?", "Disminuirá", "Sin nutrientes las algas crecen menos."),
        ],
    },
    context=[ex("Un noticiero dice que este año hay mucha lluvia en la zona central y que el mar está más cálido que lo normal. ¿Con cuál de estos fenómenos podría relacionarse?", "Con El Niño", "El calentamiento del agua y más lluvia son rasgos de El Niño.")],
    selfcheck=[
        ex("¿Cuál es una corriente fría que recorre la costa de Chile?", "La corriente de Humboldt", "Es la corriente fría del Pacífico sudoriental."),
        ex("¿Cada cuánto ocurre El Niño: todos los días o cada varios años?", "Cada varios años", "No es un fenómeno diario."),
        ex("Para comparar temperaturas del mar, ¿qué debe ser igual: la profundidad o el color?", "La profundidad", "Es el criterio común."),
    ],
    open_task=task(
        "Copia esta tabla de ejemplo: año normal, mar a 17 °C y 100 toneladas de pesca; año de El Niño, mar a 21 °C y 40 toneladas de pesca. Escribe dos comparaciones con números, una explicación de por qué cambia la pesca y una limitación de estos datos.",
        "El mar está 4 °C más cálido en El Niño y se pescan 60 toneladas menos. Con menos nutrientes hay menos algas y menos peces. Limitación: son datos de ejemplo de un solo lugar.",
        ["dos comparaciones con números", "explicación con nutrientes o algas", "nombra una limitación"],
        ["tabla copiada", "comparaciones escritas"],
        ["comparar sin restar bien", "decir que El Niño y Humboldt son iguales"],
        "Pregunta qué otro dato necesitaría para estar más segura de su explicación.",
    ),
    reinforce="Escribe tres diferencias entre la corriente de Humboldt y El Niño.",
    extend="Averigua con una persona de tu casa si recuerdan un año de mucha lluvia asociado a El Niño y qué pasó en tu zona.",
)

# ---------------------------------------------------------------- OA 13, clase 5
register(
    OA13, 5,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a explicar las características de océanos y lagos con evidencia y a decir hasta dónde llegan mis conclusiones. Sirve para hablar de la naturaleza sin exagerar.",
    prior=["Sé cómo cambian temperatura, luz y presión con la profundidad.", "Conozco las olas, las mareas y las corrientes."],
    explain=[
        "Una explicación científica tiene tres partes: una afirmación, la evidencia que la apoya y una limitación, es decir, hasta dónde llegan los datos. Por ejemplo: afirmación, «en un lago profundo el fondo es más frío»; evidencia, «los datos de ejemplo marcan 18 °C arriba y 6 °C abajo»; limitación, «es un solo lago y un solo día».",
        "Océanos y lagos se parecen y se diferencian. En ambos, la temperatura y la luz bajan con la profundidad y la presión aumenta. En ambos el viento forma olas. Pero el océano es salado, enorme y tiene mareas y grandes corrientes, como la de Humboldt. Un lago, como el lago Llanquihue en el sur de Chile, es una masa de agua mucho más pequeña, generalmente dulce, con olas pero casi sin mareas.",
        "Una buena explicación no dice «siempre» cuando solo tiene un dato. Dice «en este caso» y propone qué más medir. Así se separa lo que se sabe de lo que se supone.",
    ],
    vocab=[("afirmación", "idea que quiero demostrar"), ("evidencia", "dato que apoya una afirmación"), ("limitación", "aspecto que los datos no permiten asegurar"), ("océano", "gran masa de agua salada que cubre gran parte de la Tierra"), ("lago", "masa de agua rodeada de tierra, generalmente dulce")],
    worked=[
        {"title": "Afirmación, evidencia y limitación", "problem": "Datos de ejemplo de un lago: 18 °C en la superficie y 6 °C a 50 m. Escribe una explicación con las tres partes.", "steps": ["Afirmación: en este lago el agua profunda es más fría.", "Evidencia: 18 °C arriba y 6 °C abajo, o sea 12 °C menos.", "Limitación: es un solo lago y un solo momento."], "answer": "Afirmación, evidencia con números y una limitación"},
        {"title": "Comparar océano y lago", "problem": "¿Cuál de las dos masas de agua tiene mareas notorias: el océano o un lago pequeño?", "steps": ["Las mareas se notan en masas de agua muy grandes.", "El océano lo es; el lago pequeño no."], "answer": "El océano"},
    ],
    mistakes=[
        {"wrong": "Decir «todos los lagos del mundo tienen 6 °C en el fondo» con un solo dato.", "why": "Se generaliza con muy poca evidencia.", "fix": "Di «en este lago de ejemplo» y propone medir otros."},
        {"wrong": "Escribir una explicación sin ninguna cifra o dato.", "why": "Se cree que basta con una frase convincente.", "fix": "Cita al menos un dato con su unidad."},
    ],
    tiers={
        "recovery": [
            ex("¿Dónde puede estar la corriente de Humboldt: en un océano o en un lago pequeño?", "En un océano", "Las corrientes marinas grandes recorren masas de agua enormes."),
            ex("¿El agua de los océanos es dulce o salada?", "Salada", "Los océanos tienen sales disueltas."),
            ex("En un lago profundo, ¿la luz llega hasta el fondo o disminuye con la profundidad?", "Disminuye con la profundidad", "También en los lagos la luz disminuye al bajar."),
        ],
        "understand": [
            ex("En una explicación científica, ¿qué es la evidencia?", "El dato que apoya la afirmación", "Sin evidencia, una afirmación es solo una opinión."),
            ex("Lee: «A 1.000 m la temperatura del ejemplo es 4 °C». ¿Es afirmación, evidencia o limitación?", "Evidencia", "Es un dato medido en el ejemplo."),
            ex("Lee: «Es solo un lago medido un solo día». ¿Es afirmación, evidencia o limitación?", "Limitación", "Dice hasta dónde llegan los datos."),
        ],
        "apply": [
            arith("Datos de ejemplo de un lago: 18 °C en la superficie y 6 °C a 50 m. ¿Cuántos °C menos hay a 50 m?", "18-6", "Se resta la temperatura del fondo a la de la superficie.", " °C"),
            ex("Elige el dato que apoya mejor la afirmación «en el océano la presión es mayor a 40 m que en la superficie»: (a) «la presión en la superficie es 1 atm y suma 1 atm cada 10 m» o (b) «el océano es azul».", "(a)", "Aporta datos de presión y profundidad."),
            arith("Una fosa oceánica de ejemplo llega a 11.000 m de profundidad y la luz suficiente para las algas llega hasta 200 m. ¿Cuántos metros de la fosa quedan en la oscuridad?", "11000-200", "Se resta la zona iluminada a la profundidad total.", " m"),
        ],
        "reason": [
            ex("Un compañero midió un lago un día y escribe: «todos los lagos del mundo son iguales». ¿Qué limitación tiene su explicación?", "Tiene datos de un solo lago y un solo día, así que no puede generalizar", "Una conclusión necesita más casos."),
            ex("¿Qué dos características comparten un océano y un lago grande: (a) la temperatura baja y la presión sube con la profundidad, o (b) ambos son salados y tienen mareas notorias?", "(a)", "En ambos la profundidad cambia esas variables; la salinidad y las mareas son distintas."),
        ],
        "challenge": [
            ex("¿Cuál de estas explicaciones es mejor: (a) «En el lago de ejemplo hay 18 °C arriba y 6 °C a 50 m; es un solo lago, así que faltan más datos» o (b) «Todos los lagos son más fríos abajo, no hay duda»?", "(a)", "Cita datos y reconoce la limitación."),
            arith("En un lago de ejemplo, la temperatura baja 12 °C entre la superficie y 60 m. En otro baja 9 °C entre la superficie y 60 m. ¿Cuántos °C más baja en el primero?", "12-9", "Se restan las dos bajas.", " °C"),
        ],
    },
    context=[ex("Una persona dice: «en el mar siempre hace frío en el fondo». ¿Qué le pedirías para apoyar la afirmación?", "Datos de temperatura a distintas profundidades", "Una afirmación se apoya con evidencia medida.")],
    selfcheck=[
        ex("¿Qué tres partes tiene una buena explicación científica?", "Afirmación, evidencia y limitación", "Cada una cumple un papel."),
        ex("¿Qué tiene el océano que casi no tiene un lago pequeño?", "Mareas notorias", "El océano es una masa de agua enorme."),
        ex("¿Qué palabra evita exagerar: «siempre» o «en este caso»?", "En este caso", "Reconoce que los datos son pocos."),
    ],
    open_task=task(
        "Con los datos de ejemplo del océano (0 m: 20 °C; 100 m: 15 °C; 500 m: 8 °C; 1.000 m: 4 °C) y de un lago (superficie 18 °C; 50 m: 6 °C), escribe una comparación en tres partes: una afirmación sobre qué comparten, dos datos como evidencia y una limitación. Agrega una diferencia entre océano y lago.",
        "Afirmación: en ambos el agua profunda es más fría. Evidencia: 20 °C a 4 °C en el océano; 18 °C a 6 °C en el lago. Limitación: son datos de ejemplo. Diferencia: el océano es salado y el lago generalmente dulce.",
        ["tres partes completas", "dos datos con unidad", "una diferencia correcta"],
        ["texto de tres partes"],
        ["omitir la limitación", "generalizar con un dato"],
        "Pregunta qué otro dato haría más fuerte la afirmación.",
    ),
    reinforce="Escribe una afirmación sobre la luz en el mar y su evidencia.",
    extend="Averigua en qué se diferencian el agua de un lago y la de un océano para los seres vivos que viven en ellos.",
)
