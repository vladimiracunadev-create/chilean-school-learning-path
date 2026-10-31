"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 12 (clima terrestre como sistema dinámico)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12 = "CN07 OA 12"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 12, clase 1
register(
    OA12, 1,
    materials="Papel y lápiz. Para la tarea abierta: una linterna o el celular con la luz encendida, una hoja y una pelota o naranja (nunca mires la luz directamente a los ojos).",
    use="Aprenderé a relacionar la energía del Sol, la latitud y las estaciones del año. Sirve para explicar por qué algunos lugares son más cálidos que otros y por qué cambian las estaciones.",
    prior=["Sé que la Tierra gira sobre su eje y gira alrededor del Sol.", "Sé leer grados en un mapa y calcular diferencias."],
    explain=[
        "El Sol es la principal fuente de energía del clima. La latitud es la distancia angular, en grados, entre un lugar y el ecuador (latitud 0°), hacia el norte o hacia el sur. Como la Tierra es esférica, en latitudes bajas, cerca del ecuador, los rayos llegan casi perpendiculares y la misma cantidad de energía se reparte en una superficie pequeña. En latitudes altas, cerca de los polos, llegan inclinados y se reparten en una superficie mayor, por eso hace más frío.",
        "El eje de la Tierra está inclinado unos 23° respecto del plano de su órbita. Durante la traslación, que es una vuelta completa alrededor del Sol en aproximadamente 365 días, el hemisferio inclinado hacia el Sol recibe rayos más directos y días más largos: es verano allí. El otro hemisferio recibe rayos más inclinados y días más cortos: es invierno. Por eso las estaciones son opuestas: en Chile el verano va de fines de diciembre a fines de marzo, y en esos meses es invierno en el hemisferio norte.",
        "Cuidado con dos errores frecuentes. La rotación, una vuelta sobre su eje cada 24 horas, produce el día y la noche, no las estaciones. Y las estaciones no ocurren porque la Tierra esté más cerca o más lejos del Sol, ya que los dos hemisferios tienen estaciones opuestas al mismo tiempo.",
    ],
    vocab=[("latitud", "distancia en grados entre un lugar y el ecuador"), ("ecuador", "línea imaginaria de latitud 0°"), ("rotación", "giro de la Tierra sobre su eje, cada 24 horas"), ("traslación", "vuelta de la Tierra alrededor del Sol, en aproximadamente 365 días"), ("hemisferio", "cada mitad de la Tierra, norte o sur")],
    worked=[
        {"title": "Comparar dos latitudes", "problem": "La ciudad A está a 10° de latitud sur y la ciudad B a 50° de latitud sur. ¿Cuál recibe los rayos solares más directos, en promedio anual?", "steps": ["A está más cerca del ecuador.", "Más cerca del ecuador, los rayos llegan más perpendiculares."], "answer": "La ciudad A"},
        {"title": "Estaciones opuestas", "problem": "En enero es verano en Chile. ¿Qué estación es en ese mes en un país del hemisferio norte con cuatro estaciones marcadas?", "steps": ["Los hemisferios reciben los rayos del Sol de forma opuesta.", "Cuando el sur tiene verano, el norte tiene invierno."], "answer": "Invierno"},
    ],
    mistakes=[
        {"wrong": "Decir que hay verano porque la Tierra está más cerca del Sol.", "why": "Se usa una causa que no explica las estaciones opuestas.", "fix": "Las estaciones se deben a la inclinación del eje durante la traslación."},
        {"wrong": "Decir que la rotación produce las estaciones.", "why": "Se confunden rotación y traslación.", "fix": "La rotación produce el día y la noche; la traslación, junto con la inclinación, produce las estaciones."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué movimiento de la Tierra produce el día y la noche: rotación o traslación?", "Rotación", "La Tierra gira sobre su eje cada 24 horas."),
            ex("¿Qué movimiento de la Tierra dura aproximadamente un año?", "Traslación", "Es la vuelta completa alrededor del Sol."),
            ex("¿En qué latitud está el ecuador?", "0°", "El ecuador es el punto de partida para medir la latitud."),
        ],
        "understand": [
            ex("Dos ciudades tienen latitud 5° y latitud 60°. Con todo lo demás igual, ¿cuál tiene mayor temperatura media por la energía solar?", "La de 5°", "Cerca del ecuador los rayos llegan más directos."),
            ex("¿Por qué hay estaciones: (a) cambia la distancia entre la Tierra y el Sol, (b) el eje inclinado durante la traslación o (c) la rotación cada 24 horas?", "(b)", "La inclinación hace que un hemisferio reciba rayos más directos en cada época."),
            ex("En Chile es invierno. ¿Qué estación es en ese momento en el hemisferio norte?", "Verano", "Las estaciones son opuestas entre hemisferios."),
        ],
        "apply": [
            arith("Una ciudad está a 33° de latitud sur y otra a 53° de latitud sur. ¿Cuántos grados de latitud las separan?", "53-33", "Se restan las latitudes, porque ambas están en el mismo hemisferio.", "°"),
            arith("La Tierra gira 360° en 24 horas. ¿Cuántos grados gira en cada hora?", "360//24", "Se divide el giro total por las horas.", "°"),
            ex("Una persona viaja desde Chile en julio a un país del hemisferio norte que tiene cuatro estaciones marcadas. ¿Qué estación encontrará allá?", "Verano", "Cuando es invierno en Chile, es verano en el hemisferio norte."),
        ],
        "reason": [
            ex("Luis dice que hace calor en verano porque la Tierra está más cerca del Sol. Sabemos que en diciembre es verano en Chile e invierno en Canadá. ¿Qué dato contradice a Luis?", "Los dos países están a la misma distancia del Sol y tienen estaciones opuestas", "Si la distancia fuera la causa, los dos hemisferios tendrían la misma estación."),
            ex("En verano los días son más largos. ¿Por qué eso contribuye a que haga más calor?", "Porque el Sol calienta durante más horas", "Más horas de luz significan más energía recibida en el día."),
        ],
        "challenge": [
            ex("El mismo haz de luz cae sobre un lugar de latitud 5° y sobre otro de latitud 55°. En el segundo, el haz llega inclinado. ¿Por qué ese lugar recibe menos energía en cada metro cuadrado?", "Porque la misma luz se reparte en una superficie mayor", "Un haz inclinado ilumina un área más grande y la energía queda más repartida."),
            ex("Si el eje de la Tierra no estuviera inclinado, ¿habría estaciones como las conocemos? Responde sí o no.", "No", "Sin inclinación, cada hemisferio recibiría rayos de forma similar todo el año."),
        ],
    },
    context=[ex("Arica está cerca de los 18° de latitud sur y Punta Arenas cerca de los 53° de latitud sur. ¿Cuál de las dos ciudades recibe, en promedio, los rayos solares más directos?", "Arica", "Está más cerca del ecuador.")],
    selfcheck=[
        ex("¿Qué es la latitud?", "La distancia en grados entre un lugar y el ecuador", "Se mide hacia el norte o el sur desde 0°."),
        ex("¿Cuántos días dura aproximadamente la traslación?", "365 días", "Es la duración aproximada de un año."),
        ex("Las estaciones, ¿dependen de la distancia al Sol o de la inclinación del eje?", "De la inclinación del eje", "Los hemisferios tienen estaciones opuestas."),
    ],
    open_task=task(
        "Haz un modelo con una linterna (o la luz del celular), una hoja y una pelota o naranja. En una pieza oscura, ilumina la hoja desde arriba, con la luz perpendicular, y dibuja el contorno de la mancha. Luego inclina la hoja y vuelve a dibujar el contorno. Anota en cuál posición la mancha es más grande y más débil. Escribe qué latitud representa cada posición y una limitación del modelo.",
        "Con la hoja perpendicular, la mancha es pequeña y brillante: representa la latitud baja, cerca del ecuador. Con la hoja inclinada, la mancha es grande y más débil: representa una latitud alta. Limitación: la hoja es plana y la Tierra es esférica.",
        ["dos posiciones comparadas", "mancha pequeña y brillante frente a grande y débil", "una limitación del modelo"],
        ["dos dibujos de la mancha", "frase con latitud baja y alta"],
        ["mirar la luz directamente a los ojos", "decir que la luz es más fuerte porque está más cerca"],
        "Pregunta qué parte de las estaciones no puede mostrar este modelo.",
    ),
    reinforce="Explica con una frase por qué los dos hemisferios tienen estaciones opuestas.",
    extend="Averigua con una persona de tu casa cuántas horas de luz tiene el día más corto y el más largo en tu ciudad y calcula la diferencia.",
)

# ================================================================ OA 12, clase 2
register(
    OA12, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a modelar cómo el aire y el agua del océano se mueven y reparten la energía del Sol. Sirve para explicar los vientos, las nubes y las corrientes marinas.",
    prior=["Sé que el Sol calienta de forma desigual la Tierra.", "Sé que un gas se expande al calentarse."],
    explain=[
        "La atmósfera es la capa de gases que rodea la Tierra. La presión atmosférica es la fuerza que el aire ejerce sobre cada unidad de superficie y se mide en hectopascales (hPa). El aire que se calienta se expande y sube, y deja una zona de baja presión. El aire frío baja y forma una zona de alta presión. El viento es aire que se mueve desde la zona de alta presión hacia la de baja presión. Cuanto mayor es la diferencia de presión entre las dos zonas, más fuerte es el viento.",
        "La humedad atmosférica es el vapor de agua que hay en el aire. Cuando el aire cálido y húmedo sube, se enfría; el vapor se condensa y forma nubes y, a veces, lluvia. Por eso las zonas de baja presión suelen traer nubosidad y las de alta presión, cielo despejado. A gran escala, el aire cálido sube cerca del ecuador y el aire frío baja en latitudes altas, y así la atmósfera reparte energía por el planeta.",
        "El océano también reparte energía. Las corrientes marinas son grandes masas de agua que se mueven y transportan calor. La corriente de Humboldt es fría y recorre la costa de Chile hacia el norte, lo que enfría el aire de la costa. Los modelos del clima combinan aire, agua y energía solar.",
    ],
    vocab=[("presión atmosférica", "fuerza del aire sobre una superficie, medida en hPa"), ("viento", "aire que se mueve de alta a baja presión"), ("humedad atmosférica", "vapor de agua presente en el aire"), ("corriente marina", "movimiento de grandes masas de agua que transporta calor"), ("hectopascal (hPa)", "unidad usada para medir la presión atmosférica")],
    worked=[
        {"title": "Dirección del viento", "problem": "En un mapa, la zona A tiene 1.020 hPa y la zona B tiene 1.000 hPa. ¿Hacia dónde sopla el viento?", "steps": ["A tiene la presión más alta; B, la más baja.", "El viento va de alta a baja presión."], "answer": "De A hacia B"},
        {"title": "Brisa de mar", "problem": "Al mediodía de verano la tierra se calienta más que el mar. ¿De dónde a dónde sopla la brisa?", "steps": ["El aire sobre la tierra se calienta, sube y baja la presión.", "El aire más fresco del mar se mueve para ocupar ese espacio."], "answer": "Del mar hacia la tierra"},
    ],
    mistakes=[
        {"wrong": "Decir que el viento sopla desde la baja presión hacia la alta.", "why": "Se invierte la dirección del movimiento.", "fix": "El aire se mueve de alta a baja presión."},
        {"wrong": "Pensar que las corrientes marinas no afectan el aire.", "why": "Se separa el océano de la atmósfera.", "fix": "El agua fría o cálida cambia la temperatura del aire que está sobre ella."},
    ],
    tiers={
        "recovery": [
            ex("El viento sopla desde una zona de presión ¿alta o baja? hacia una zona de presión ¿alta o baja?", "De alta a baja", "El aire se mueve hacia donde hay menos presión."),
            ex("El aire que se calienta, ¿sube o baja?", "Sube", "Se expande y se vuelve más liviano."),
            ex("La corriente de Humboldt, ¿es cálida o fría?", "Fría", "Es una corriente fría que baja la temperatura de la costa."),
        ],
        "understand": [
            ex("En un mapa, la zona P tiene 1.012 hPa y la zona Q tiene 1.004 hPa. ¿Hacia dónde sopla el viento?", "De P hacia Q", "Va de la presión más alta a la más baja."),
            ex("El aire cálido y húmedo sube y se enfría. ¿Qué se forma cuando el vapor se condensa?", "Nubes", "El vapor se vuelve gotitas de agua que forman nubes."),
            ex("¿Qué transportan las corrientes marinas de una zona a otra?", "Calor", "Las masas de agua llevan energía térmica."),
        ],
        "apply": [
            arith("Una zona tiene 1.024 hPa y otra tiene 996 hPa. ¿Cuántos hPa de diferencia hay?", "1024-996", "A mayor diferencia de presión, más fuerte es el viento.", " hPa"),
            arith("Una corriente marina de ejemplo avanza 2 km cada hora. ¿Cuántos kilómetros avanza en un día completo?", "2*24", "Se multiplican los kilómetros por hora por las 24 horas.", " km"),
            ex("En la noche, el mar conserva más calor que la tierra. ¿De dónde a dónde sopla la brisa?", "De la tierra hacia el mar", "El aire sobre el mar, más cálido, sube; el aire de la tierra ocupa ese lugar."),
        ],
        "reason": [
            ex("Tomás dice que el viento sopla de baja a alta presión. El mapa muestra A con 1.018 hPa y B con 1.006 hPa. ¿Cuál es su error?", "El viento sopla de A (alta) hacia B (baja)", "El aire se mueve hacia donde hay menos presión."),
            ex("¿Por qué una zona de alta presión suele traer cielo despejado?", "Porque el aire baja y no sube a enfriarse para formar nubes", "Las nubes se forman cuando el aire húmedo sube."),
        ],
        "challenge": [
            ex("Si la corriente de Humboldt se debilitara y sus aguas fueran más cálidas, ¿qué esperarías para la temperatura del aire de la costa de Chile: más cálida o más fría?", "Más cálida", "El agua más cálida calienta el aire que está sobre ella."),
            ex("Un meteorólogo dice: «El aire de la ciudad X sube porque está más caliente que el de la ciudad Y». Si X y Y están una al lado de la otra, ¿cómo será la presión en X en comparación con Y?", "Más baja", "El aire que sube deja una zona de menor presión."),
        ],
    },
    context=[ex("Una persona que vive en la costa nota que en verano, a mediodía, el viento viene del mar. ¿Qué explicación con presión corresponde?", "La tierra se calienta, el aire sube, baja la presión y entra el aire del mar", "El aire se mueve hacia la zona de menor presión.")],
    selfcheck=[
        ex("¿Qué unidad se usa para medir la presión atmosférica en un mapa?", "Hectopascal (hPa)", "Es la unidad habitual de los mapas del tiempo."),
        ex("¿Qué es el viento?", "Aire que se mueve de alta a baja presión", "Esa es su definición."),
        ex("¿Qué dos cosas reparten energía por el planeta?", "La atmósfera y el océano", "El aire y las corrientes marinas transportan calor."),
    ],
    open_task=task(
        "Dibuja un corte de una costa con el mar a la izquierda y la tierra a la derecha. Dibuja dos situaciones: un día de verano al mediodía y esa misma noche. En cada una, marca con flechas cómo se mueve el aire (sube, baja y viento horizontal) y escribe dónde hay baja presión y dónde alta. Termina con una limitación del dibujo.",
        "Mediodía: la tierra se calienta, el aire sube sobre la tierra (baja presión) y el viento sopla del mar a la tierra. Noche: el mar está más cálido, el aire sube sobre el mar y el viento sopla de la tierra al mar. Limitación: el dibujo no muestra la humedad.",
        ["dos dibujos con flechas", "baja y alta presión bien ubicadas", "una limitación"],
        ["dibujos rotulados", "frase de limitación"],
        ["flechas del viento en sentido contrario", "no indicar la presión"],
        "Pregunta qué cambiaría en el dibujo si el mar estuviera más frío por la corriente de Humboldt.",
    ),
    reinforce="Explica con tus palabras por qué se forman nubes cuando el aire cálido y húmedo sube.",
    extend="Averigua con una persona de tu casa de qué dirección suele soplar el viento en tu zona y en qué época del año es más fuerte.",
)

# ================================================================ OA 12, clase 3
register(
    OA12, 3,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a explicar cómo el relieve, la altitud y la cercanía al mar cambian el clima de un lugar. Sirve para entender por qué ciudades a la misma latitud pueden tener climas distintos.",
    prior=["Sé que el sol y la latitud influyen en la temperatura.", "Sé leer datos de temperatura y calcular diferencias."],
    explain=[
        "La altitud es la altura de un lugar sobre el nivel del mar. La temperatura baja a medida que se sube: aproximadamente 6 °C por cada 1.000 m (valor de ejemplo, cambia según el lugar y la época). Por eso hay nieve en la cima de montañas, aunque estén en latitudes cálidas.",
        "El relieve también modifica la humedad. Cuando el viento húmedo choca con una cordillera, el aire sube por la ladera, se enfría y el vapor se condensa: en esa ladera hay nubes y precipitaciones. Al otro lado el aire baja, ya perdió su humedad y la zona es más seca. En Chile, la cordillera de los Andes y la cordillera de la Costa influyen en las precipitaciones de esa manera.",
        "La cercanía al mar también cambia el clima. El agua se calienta y se enfría más lento que la tierra, por eso las costas tienen temperaturas más parejas. En el interior, lejos del mar, la amplitud térmica, que es la diferencia entre la temperatura máxima y la mínima, suele ser mayor.",
    ],
    vocab=[("altitud", "altura sobre el nivel del mar"), ("relieve", "conjunto de formas de la superficie, como montañas y valles"), ("ladera", "pendiente de una montaña"), ("amplitud térmica", "diferencia entre temperatura máxima y mínima"), ("precipitación", "agua que cae desde las nubes, como lluvia o nieve")],
    worked=[
        {"title": "Temperatura según la altitud", "problem": "Un pueblo a nivel del mar tiene 20 °C. Con la regla de 6 °C por cada 1.000 m, ¿qué temperatura se espera en otro pueblo a 2.000 m de altitud?", "steps": ["2.000 m son dos tramos de 1.000 m.", "Baja 6 × 2 = 12 °C: 20 − 12 = 8 °C."], "answer": "8 °C"},
        {"title": "Calcular la amplitud térmica", "problem": "En una ciudad costera las temperaturas del día son: máxima 22 °C y mínima 14 °C. ¿Cuál es la amplitud térmica?", "steps": ["Se resta la mínima a la máxima.", "22 − 14 = 8."], "answer": "8 °C"},
    ],
    mistakes=[
        {"wrong": "Explicar que hace frío en la cima de una montaña porque está más cerca del Sol.", "why": "La distancia al Sol casi no cambia con la altitud.", "fix": "Con la altitud la temperatura baja aproximadamente 6 °C por cada 1.000 m."},
        {"wrong": "Pensar que ambos lados de una cordillera reciben igual lluvia.", "why": "Se ignora el efecto del relieve sobre el aire húmedo.", "fix": "La ladera hacia donde sopla el viento húmedo recibe más precipitaciones."},
    ],
    tiers={
        "recovery": [
            ex("Al subir una montaña, ¿la temperatura baja o sube?", "Baja", "El aire se enfría con la altitud."),
            ex("¿Cómo se llama la diferencia entre la temperatura máxima y la mínima?", "Amplitud térmica", "Mide cuánto cambia la temperatura en el período considerado."),
            ex("El agua del mar, ¿se calienta y enfría más lento o más rápido que la tierra?", "Más lento", "Por eso el mar modera la temperatura de la costa."),
        ],
        "understand": [
            ex("Una ciudad de la costa y una del interior están a la misma latitud. ¿Cuál tiene mayor amplitud térmica?", "La del interior", "Lejos del mar, el aire cambia más de temperatura."),
            ex("Cuando el viento húmedo choca con una cordillera, ¿en qué ladera hay más nubes y lluvia: en la que el aire sube o en la que baja?", "En la que el aire sube", "Al subir se enfría y el vapor se condensa."),
            ex("¿Por qué el aire que sube por una ladera forma nubes?", "Porque se enfría y el vapor de agua se condensa", "Las nubes se forman por condensación."),
        ],
        "apply": [
            arith("Un pueblo a nivel del mar marca 24 °C. Con la regla de 6 °C por cada 1.000 m, ¿qué temperatura se espera a 3.000 m?", "24-3*6", "Se multiplica el descenso por kilómetro por los kilómetros de altura y se resta.", " °C"),
            arith("Una ciudad del interior tuvo una máxima de 31 °C y una mínima de 9 °C. ¿Cuál es su amplitud térmica?", "31-9", "Se resta la mínima a la máxima.", " °C"),
            arith("La ciudad de la costa M tiene una amplitud de 8 °C y la ciudad del interior N tiene una amplitud de 21 °C. ¿Cuántos grados de amplitud más tiene N?", "21-8", "Se resta la amplitud menor a la mayor.", " °C"),
        ],
        "reason": [
            ex("Pedro dice que en la ciudad X, a 2.500 m de altitud, hace más frío porque está más lejos del Sol. ¿Cuál es la explicación correcta según esta clase?", "La temperatura baja con la altitud, aproximadamente 6 °C por cada 1.000 m", "La distancia al Sol casi no cambia con la altitud."),
            ex("La ciudad P (costa) tiene máxima 20 °C y mínima 14 °C. La ciudad Q (interior), a la misma latitud, tiene máxima 30 °C y mínima 6 °C. ¿Qué factor explica mejor la diferencia entre las amplitudes?", "La cercanía al mar", "El mar modera la temperatura de P."),
        ],
        "challenge": [
            arith("Una ciudad a 500 m de altitud marca 20 °C. Con la misma regla, ¿cuántos °C se esperan en un punto a 3.500 m?", "20-(3500-500)//1000*6", "Primero se calcula la diferencia de altitud, luego el descenso de temperatura.", " °C"),
            ex("En la ladera oeste de una cordillera caen 900 mm de lluvia al año y en la ladera este caen 200 mm. El viento húmedo llega desde el oeste. ¿Qué explica la diferencia?", "El aire sube por la ladera oeste y se enfría, y al bajar por el este ya perdió su humedad", "El relieve hace que una ladera reciba más precipitación."),
        ],
    },
    context=[ex("Una persona viaja de un balneario a un pueblo cordillerano ubicado mucho más arriba. Lleva abrigo extra. ¿Qué factor del clima justifica esa decisión?", "La altitud, porque la temperatura baja al subir", "A más altura, más frío.")],
    selfcheck=[
        ex("¿Cuánto baja aproximadamente la temperatura por cada 1.000 m de altitud, según el valor de ejemplo de esta clase?", "6 °C", "Es el valor de ejemplo de la clase."),
        ex("¿Qué es el relieve?", "El conjunto de formas de la superficie, como montañas y valles", "Incluye cordilleras, valles y llanuras."),
        ex("¿Qué zona tiene temperaturas más parejas: la costa o el interior?", "La costa", "El mar modera la temperatura."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo: Ciudad A, altitud 100 m, junto al mar, máxima 24 °C y mínima 15 °C. Ciudad B, misma latitud, altitud 100 m, lejos del mar, máxima 33 °C y mínima 6 °C. Ciudad C, misma latitud, junto al mar, altitud 2.100 m. Calcula la amplitud térmica de A y B. Con la regla de 6 °C por cada 1.000 m, estima la máxima de C desde la máxima de A. Explica qué factor explica cada diferencia.",
        "Amplitud de A: 9 °C. Amplitud de B: 27 °C, por la lejanía del mar. Máxima de C: 24 − 12 = 12 °C, por la altitud (2.000 m más arriba que A).",
        ["amplitudes correctas", "máxima estimada de C", "un factor explicado por cada diferencia"],
        ["cálculos escritos", "factor nombrado"],
        ["restar mal la altitud", "no nombrar el factor"],
        "Pregunta qué factor usarías para explicar que C tenga más nieve.",
    ),
    reinforce="Escribe una frase con la palabra «ladera» y otra con «amplitud térmica».",
    extend="Averigua con una persona de tu casa la altitud de un pueblo o cerro que conozca y calcula cuánto más frío esperarías respecto del nivel del mar.",
)

# ================================================================ OA 12, clase 4
register(
    OA12, 4,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a distinguir el tiempo atmosférico del clima y a reconocer la variabilidad. Sirve para no concluir sobre el clima a partir de un solo día.",
    prior=["Sé calcular promedios.", "Sé que el clima depende de varios factores."],
    explain=[
        "El tiempo atmosférico es el estado de la atmósfera en un lugar y en un momento: «hoy hay lluvia y 12 °C». Cambia de hora en hora. El clima es el patrón promedio del tiempo en un lugar durante muchos años. Por convención, se usan períodos de unos 30 años o más. «En Chile central llueve en invierno y el verano es seco» describe un clima.",
        "La variabilidad climática es el cambio natural de un año a otro alrededor del promedio: hay años más lluviosos y años más secos. Un invierno seco no basta para afirmar que el clima cambió; hay que mirar muchos años. Para eso se calcula un promedio: se suman los valores y se divide por la cantidad de datos.",
        "El clima puede estudiarse a escala local, como una ciudad, o a escala global, como el promedio de todo el planeta. Un día frío no desmiente un aumento de la temperatura global, porque el tiempo de un día es una cosa y el promedio de muchos años es otra.",
    ],
    vocab=[("tiempo atmosférico", "estado de la atmósfera en un lugar y un momento"), ("clima", "patrón promedio del tiempo durante muchos años"), ("variabilidad", "cambio natural de un año a otro alrededor del promedio"), ("promedio", "suma de los datos dividida por la cantidad de datos"), ("escala", "tamaño del lugar estudiado: local o global")],
    worked=[
        {"title": "Calcular un promedio", "problem": "Las temperaturas máximas de cinco días fueron 20, 22, 24, 22 y 22 °C. ¿Cuál fue el promedio?", "steps": ["Se suman: 20 + 22 + 24 + 22 + 22 = 110.", "Se divide por 5: 110 ÷ 5 = 22."], "answer": "22 °C"},
        {"title": "Tiempo o clima", "problem": "¿Qué describe «hoy llovió 12 mm en esta ciudad», el tiempo o el clima?", "steps": ["Habla de un solo día.", "Un solo día es el tiempo atmosférico."], "answer": "El tiempo atmosférico"},
    ],
    mistakes=[
        {"wrong": "Decir que el clima cambió porque este año llovió poco.", "why": "Se confunde un año con el patrón de muchos años.", "fix": "Un año seco es variabilidad; para hablar de clima hay que mirar décadas."},
        {"wrong": "Usar «clima» para hablar del día de hoy.", "why": "Se confunde con el tiempo atmosférico.", "fix": "Lo de hoy es tiempo; el patrón de muchos años es clima."},
    ],
    tiers={
        "recovery": [
            ex("«Mañana habrá 25 °C y viento». ¿Es tiempo o clima?", "Tiempo", "Habla de un día específico."),
            ex("«En esta zona llueve poco en verano, año tras año». ¿Es tiempo o clima?", "Clima", "Es un patrón que se repite."),
            ex("¿Cuántos años se usan, por convención, al menos para describir un clima?", "Unos 30 años", "Se necesita un período largo para ver el patrón."),
        ],
        "understand": [
            ex("¿Por qué un día muy frío no cambia el clima de una zona?", "Porque el clima es el promedio de muchos años", "Un día es tiempo atmosférico."),
            ex("¿Qué es la variabilidad climática?", "El cambio natural de un año a otro alrededor del promedio", "Hay años más lluviosos y más secos que el promedio."),
            ex("¿En qué se diferencian clima local y clima global: en la cantidad de agua o en el tamaño del lugar estudiado?", "En el tamaño del lugar estudiado", "Local es una zona; global es todo el planeta."),
        ],
        "apply": [
            arith("Las lluvias anuales de una ciudad en cinco años fueron 300, 250, 400, 350 y 200 mm (datos de ejemplo). ¿Cuál es el promedio anual?", "(300+250+400+350+200)//5", "Se suman los cinco valores y se divide por cinco.", " mm"),
            arith("Las temperaturas medias de enero en seis años fueron 20, 22, 19, 23, 21 y 21 °C (datos de ejemplo). ¿Cuál es el promedio?", "(20+22+19+23+21+21)//6", "Se suman los seis valores y se divide por seis.", " °C"),
            arith("El promedio de lluvia de un año en una ciudad es 300 mm, pero un año cayeron 420 mm. ¿Cuántos mm sobre el promedio cayeron?", "420-300", "Se resta el promedio al valor del año.", " mm"),
        ],
        "reason": [
            ex("La ciudad A tuvo lluvias de 580, 600, 620 y 600 mm en cuatro años. La ciudad B tuvo 200, 1.000, 300 y 900 mm. Las dos tienen promedio de 600 mm. ¿Cuál tiene más variabilidad?", "La ciudad B", "Sus valores se alejan mucho más del promedio."),
            ex("María dice: «Este invierno fue más seco de lo normal, así que el clima de mi región cambió». ¿Qué evidencia falta para afirmarlo?", "Datos de muchos años, no de uno solo", "Un año seco puede ser variabilidad natural."),
        ],
        "challenge": [
            ex("Un mes tiene un promedio de 60 mm en 30 años. Un año cayeron 15 mm y otro, 105 mm. ¿Cuántos mm se alejó cada año del promedio?", "45 mm menos y 45 mm más", "60 − 15 = 45 y 105 − 60 = 45."),
            ex("Una persona dice «hoy hace 3 °C bajo lo normal, entonces el planeta no se calienta». ¿Qué diferencia de escala ignora?", "Compara el tiempo de un día local con el promedio global de muchos años", "Son escalas distintas de lugar y de tiempo."),
        ],
    },
    context=[ex("Dos frases sobre una misma ciudad: (1) «Ayer hubo neblina y 14 °C». (2) «Los inviernos son fríos y lluviosos, año tras año». ¿Cuál describe el clima?", "La frase (2)", "Es un patrón que se repite durante muchos años; la (1) describe un día.")],
    selfcheck=[
        ex("¿Cuál cambia de hora en hora: el tiempo atmosférico o el clima?", "El tiempo atmosférico", "El clima es un patrón de largo plazo."),
        ex("¿Cómo se calcula un promedio?", "Se suman los datos y se divide por la cantidad", "Esa es la regla del promedio."),
        ex("¿Qué es un año más seco que el promedio, variabilidad o cambio de clima?", "Variabilidad", "Un solo año no cambia el clima."),
    ],
    open_task=task(
        "Con estos datos de ejemplo de lluvia de julio en una ciudad, en mm: 2019: 110, 2020: 60, 2021: 140, 2022: 80, 2023: 110. Calcula el promedio, di en qué años la lluvia estuvo sobre el promedio y bajo el promedio, y escribe una frase que diferencie tiempo atmosférico de clima usando estos datos. Termina con una limitación: cinco años no alcanzan para definir un clima.",
        "Promedio: (110 + 60 + 140 + 80 + 110) ÷ 5 = 100 mm. Sobre el promedio: 2019, 2021 y 2023. Bajo el promedio: 2020 y 2022. Limitación: se usan 5 años y se necesitan unos 30.",
        ["promedio correcto", "años sobre y bajo el promedio", "limitación de 5 años"],
        ["cálculo escrito", "lista de años", "frase final"],
        ["no sumar todos los datos", "usar un solo año para hablar de clima"],
        "Pregunta qué datos agregarías para describir mejor el clima de julio.",
    ),
    reinforce="Escribe dos frases sobre el lugar donde vives: una de tiempo y otra de clima.",
    extend="Averigua con una persona de tu casa si recuerda un año muy lluvioso o muy seco en tu zona y escribe qué diferencia habría respecto del promedio.",
)

# ================================================================ OA 12, clase 5
register(
    OA12, 5,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a integrar varios factores en una explicación del clima de un lugar. Sirve para evitar explicaciones de una sola causa.",
    prior=["Conozco latitud, circulación del aire y del agua, relieve, altitud y cercanía al mar.", "Sé calcular amplitud térmica y promedios."],
    explain=[
        "El clima de un lugar resulta de varias variables que interactúan: la energía solar según la latitud, la rotación y la traslación de la Tierra, la presión, la temperatura y la humedad del aire, la circulación de la atmósfera y de las corrientes marinas, la posición geográfica, la altitud y el relieve. Por eso una explicación con una sola causa casi siempre queda incompleta.",
        "Para explicar el clima con varios factores sigue estos pasos. Primero, nombra los datos del lugar: latitud, altitud, distancia al mar y corrientes. Segundo, di qué hace cada factor con un dato concreto, por ejemplo «el mar modera la temperatura: la amplitud es 8 °C». Tercero, une los factores: cuál empuja la temperatura hacia arriba y cuál hacia abajo.",
        "Termina con una limitación: el modelo no puede predecir un día en particular, y los valores de esta clase son de ejemplo. Un clima local siempre es dinámico, porque los factores cambian durante el año y de un año a otro.",
    ],
    vocab=[("variable", "factor que puede cambiar y afecta el resultado"), ("interactuar", "influirse unos con otros"), ("multicausal", "con más de una causa"), ("dinámico", "que cambia con el tiempo"), ("posición geográfica", "ubicación de un lugar en el planeta")],
    worked=[
        {"title": "Dos factores sobre la temperatura", "problem": "Una ciudad costera a 100 m de altitud tiene una máxima de 24 °C. Otra ciudad en la misma latitud, a 2.100 m, ¿qué máxima aproximada esperarías con 6 °C por cada 1.000 m?", "steps": ["La diferencia de altitud es 2.000 m.", "Baja 6 × 2 = 12 °C: 24 − 12 = 12 °C."], "answer": "12 °C"},
        {"title": "Reconocer los factores", "problem": "«El pueblo está cerca del mar, a 20° de latitud sur, con una corriente fría frente a la costa». ¿Cuántos factores del clima se nombran?", "steps": ["Cercanía al mar, latitud y corriente fría.", "Son tres factores."], "answer": "Tres factores"},
    ],
    mistakes=[
        {"wrong": "Explicar el clima de una ciudad con un solo factor.", "why": "Se ignora que el clima depende de varias variables.", "fix": "Nombra al menos dos o tres factores y di qué hace cada uno."},
        {"wrong": "Usar la palabra «factor» sin dar un dato.", "why": "La explicación no se apoya en evidencia.", "fix": "Agrega una cifra o una observación a cada factor."},
    ],
    tiers={
        "recovery": [
            ex("Altitud, latitud y cercanía al mar, ¿son factores del clima? Responde sí o no.", "Sí", "Los tres cambian la temperatura o la humedad de un lugar."),
            ex("Una explicación multicausal, ¿tiene una causa o varias?", "Varias", "Multicausal significa con muchas causas."),
            ex("¿Qué factor modera la temperatura de una costa: el mar o la altitud?", "El mar", "El agua cambia de temperatura más despacio que la tierra."),
        ],
        "understand": [
            ex("Una frase dice: «Hace frío porque es alto». ¿Qué le falta para ser una buena explicación?", "Un dato concreto, como cuántos metros y cuánto baja la temperatura", "La explicación debe apoyarse en datos."),
            ex("¿Qué factor del clima explica que un lado de la cordillera sea más lluvioso que el otro: el relieve o la rotación?", "El relieve", "La ladera hace subir el aire húmedo."),
            ex("¿Por qué se dice que el clima es dinámico?", "Porque los factores cambian durante el año y de un año a otro", "Dinámico quiere decir que cambia."),
        ],
        "apply": [
            arith("La ciudad M tiene una máxima de 26 °C a 100 m de altitud. Con 6 °C por cada 1.000 m, ¿qué máxima se espera en un punto a 3.100 m, a la misma latitud?", "26-(3100-100)//1000*6", "La diferencia de altitud es 3.000 m, o sea, 3 tramos de 1.000 m.", " °C"),
            arith("La ciudad X tiene máxima 28 °C y mínima 12 °C. La ciudad Y tiene máxima 20 °C y mínima 14 °C. ¿Cuántos °C más de amplitud tiene X?", "(28-12)-(20-14)", "Se calcula la amplitud de cada una y se restan.", " °C"),
            ex("Una ciudad está al lado del mar, a 100 m de altitud, con corriente fría frente a la costa. ¿Esperas que su amplitud térmica sea mayor o menor que la de una ciudad del interior en la misma latitud?", "Menor", "El mar modera las temperaturas."),
        ],
        "reason": [
            ex("Lucas dice: «Mi pueblo es frío solo por su latitud». Su pueblo está a 33° de latitud sur y a 2.400 m. ¿Qué otro factor debe sumar a su explicación?", "La altitud", "A 2.400 m la temperatura es varios grados más baja que a nivel del mar."),
            ex("Una explicación dice: «Hay neblina junto a una costa con corriente fría porque el aire húmedo se enfría sobre el agua». ¿Qué proceso del vapor de agua usa esa explicación?", "La condensación", "Al enfriarse, el vapor del aire se vuelve gotitas."),
        ],
        "challenge": [
            ex("Ciudad C: 33° sur, 700 m, a 90 km del mar, amplitud 22 °C. Ciudad D: 33° sur, 700 m, junto al mar, amplitud 9 °C. ¿Qué factor explica la diferencia y qué otros dos factores iguales permiten compararlas?", "La cercanía al mar; igual latitud e igual altitud", "Si solo cambia una variable, se puede atribuir la diferencia a ella."),
            ex("Un estudiante propone explicar el clima de una ciudad solo con la traslación de la Tierra. Nombra dos factores más que necesita agregar.", "Cualquier par entre latitud, altitud, cercanía al mar, corrientes y presión", "El clima depende de varias variables que interactúan."),
        ],
    },
    context=[ex("Una persona de tu casa dice: «Donde yo vivía hacía menos calor en verano que aquí, aunque ambos lugares están en la misma latitud». Nombra un factor de esta unidad, distinto de la latitud, que podría explicar la diferencia.", "Altitud, cercanía al mar, corriente marina o relieve (una de ellas)", "Con igual latitud, la diferencia debe venir de otro factor del clima.")],
    selfcheck=[
        ex("¿Qué dos movimientos de la Tierra intervienen en el clima?", "La rotación y la traslación", "Determinan el día y la noche y las estaciones."),
        ex("¿Una explicación con una sola causa suele ser completa?", "No", "El clima es multicausal."),
        ex("¿Qué debe llevar cada factor de una explicación?", "Un dato concreto", "Así la explicación se apoya en evidencia."),
    ],
    open_task=task(
        "Compara estas dos ciudades de ejemplo. Ciudad P: latitud 30° sur, altitud 50 m, junto al mar con corriente fría, máxima media de enero 23 °C, mínima media de julio 11 °C. Ciudad Q: latitud 30° sur, altitud 1.850 m, lejos del mar, máxima media de enero 26 °C, mínima media de julio −2 °C. Escribe una explicación de tres frases: calcula la amplitud entre la máxima de enero y la mínima de julio de cada ciudad, nombra al menos tres factores que explican las diferencias con un dato cada uno, y cierra con una limitación.",
        "Amplitud de P: 23 − 11 = 12 °C. Amplitud de Q: 26 − (−2) = 28 °C. El mar y la corriente fría moderan P. Q, lejos del mar, tiene máximas más altas y mínimas más bajas, y su altitud (1.800 m más que P) ayuda a que las mínimas sean tan bajas. Limitación: son datos de ejemplo y dos meses no describen todo el clima.",
        ["amplitudes correctas", "tres factores con dato", "una limitación"],
        ["cálculos escritos", "tres frases"],
        ["usar un solo factor", "factores sin dato"],
        "Pregunta qué dato nuevo cambiaría tu explicación.",
    ),
    reinforce="Escribe tres factores que expliquen por qué una ciudad cerca del mar tiene temperaturas parejas.",
    extend="Averigua con una persona de tu casa cómo cambia el clima entre dos lugares que conozca, uno cercano al mar y otro lejano, y relaciona con lo aprendido.",
)
