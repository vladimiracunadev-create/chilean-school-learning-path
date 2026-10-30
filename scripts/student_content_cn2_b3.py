"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 13 (instrumentos del tiempo) y OA 14 (estaciones y seres vivos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA13, OA14 = "CN02 OA 13", "CN02 OA 14"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 13
register(
    OA13, 1,
    materials="Una hoja, lápices y este cuaderno con las tarjetas de cada instrumento: termómetro, pluviómetro y veleta. No se necesitan instrumentos reales para esta clase.",
    use="Aprenderé qué instrumento sirve para medir cada característica del tiempo atmosférico. Sirve para elegir bien el instrumento y registrar datos que se puedan comparar.",
    prior=["Sé que el tiempo atmosférico tiene cielo, lluvia, viento y temperatura.", "Sé que medir es comparar con una unidad, como los centímetros."],
    explain=[
        "Un instrumento es una herramienta para medir. Con los sentidos puedo decir «hace frío», pero con un instrumento puedo decir cuánto: 8 °C. Así otras personas entienden y podemos comparar días distintos.",
        "Cada característica del tiempo tiene su instrumento. El termómetro mide la temperatura en grados Celsius. El pluviómetro mide cuánta lluvia cayó, en milímetros. La veleta muestra de dónde viene el viento, con una flecha que gira.",
        "Un instrumento sirve si tiene marcas con unidades y si siempre se usa igual: en el mismo lugar y a la misma hora. Si lo muevo entre mediciones, no puedo comparar los datos. Un objeto bonito sin marcas es un adorno, no un instrumento.",
    ],
    vocab=[("instrumento", "herramienta para medir"), ("termómetro", "instrumento que mide la temperatura"), ("pluviómetro", "instrumento que mide cuánta lluvia cayó"), ("veleta", "instrumento que muestra de dónde viene el viento"), ("escala", "marcas con números y unidades en un instrumento")],
    worked=[
        {"title": "Elegir el instrumento", "problem": "Quieres saber cuántos milímetros de lluvia cayeron anoche. ¿Qué instrumento usas?", "steps": ["La característica es la cantidad de lluvia.", "El instrumento que la mide es el pluviómetro.", "Se mide en milímetros."], "answer": "El pluviómetro, en milímetros"},
        {"title": "Un instrumento sin escala", "problem": "Tomás hizo una flecha de cartulina que gira con el viento y una botella sin marcas para la lluvia. ¿Sirven para medir?", "steps": ["Una flecha que gira muestra la dirección del viento, como una veleta.", "Una botella sin marcas no mide cuánta lluvia.", "Para medir cantidad se necesitan marcas con unidades."], "answer": "La flecha puede servir como veleta; la botella sin marcas no mide lluvia"},
    ],
    mistakes=[
        {"wrong": "Decir que un objeto decorativo sirve de instrumento.", "why": "Se piensa que basta con que se parezca.", "fix": "Un instrumento necesita marcas, unidad y uso constante."},
        {"wrong": "Mover el instrumento a otro lugar cada día.", "why": "Se piensa que da lo mismo dónde esté.", "fix": "Déjalo siempre en el mismo lugar para comparar datos."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué instrumento mide la temperatura?", "El termómetro", "El termómetro mide grados Celsius."),
            ex("¿Qué instrumento mide cuánta lluvia cayó?", "El pluviómetro", "Mide la lluvia en milímetros."),
            ex("¿Qué instrumento muestra de dónde viene el viento?", "La veleta", "Su flecha gira con el viento."),
        ],
        "understand": [
            ex("¿Para qué sirve usar un instrumento en vez de solo decir «hace frío»?", "Para saber cuánto y poder comparar", "Un número permite comparar días distintos."),
            ex("¿Por qué es importante que el instrumento tenga una escala?", "Para poder leer un número con unidad", "Las marcas permiten medir."),
            ex("¿Qué unidad usa el termómetro?", "Grados Celsius", "Se escribe °C."),
        ],
        "apply": [
            ex("Quieres medir cuánta lluvia cayó. ¿Qué instrumento eliges y en qué unidad?", "Pluviómetro, en milímetros", "El pluviómetro mide la lluvia en milímetros."),
            ex("Quieres saber si el viento viene del norte o del sur. ¿Qué instrumento eliges?", "La veleta", "Muestra la dirección del viento."),
            ex("Quieres saber si hace más calor en la mañana o en la tarde. ¿Qué instrumento eliges?", "El termómetro", "Mide la temperatura."),
        ],
        "reason": [
            ex("Un compañero deja su termómetro un día al sol y otro día a la sombra. ¿Por qué no podrá comparar los datos?", "Porque lo movió de lugar", "La temperatura al sol y a la sombra es distinta."),
            ex("Dos niños miden la lluvia con vasos de distinto tamaño sin marcas. ¿Pueden comparar sus resultados? Explica.", "No", "Sin escala común no se pueden comparar."),
        ],
        "challenge": [
            ex("Empareja: A «temperatura», B «lluvia», C «dirección del viento» con 1 «veleta», 2 «termómetro», 3 «pluviómetro».", "A con 2, B con 3, C con 1", "Cada instrumento mide una característica."),
            ex("Una veleta de adorno siempre apunta al mismo lugar porque está pegada. ¿Sirve como instrumento? Explica.", "No", "Debe girar libremente con el viento."),
        ],
    },
    context=[ex("Mi tía tiene una huerta y quiere saber cuánta lluvia cayó sobre sus plantas. ¿Qué instrumento le conviene y por qué?", "Un pluviómetro, porque mide cuánta lluvia cae", "Con milímetros puede saber si cayó mucha o poca agua.")],
    selfcheck=[
        ex("¿Qué instrumento mide grados Celsius?", "El termómetro", "Mide la temperatura."),
        ex("¿Qué debe tener un instrumento para medir?", "Una escala con unidades", "Las marcas permiten leer un número."),
        ex("¿Se debe cambiar de lugar el instrumento entre mediciones?", "No", "Hay que dejarlo siempre en el mismo lugar."),
    ],
    open_task=task(
        "Haz una tabla de tres filas con estas características: temperatura, lluvia y dirección del viento. En cada fila escribe el instrumento que usarías, la unidad (si tiene) y dibuja el instrumento. Después escribe una regla para usarlos bien.",
        "Temperatura: termómetro, °C. Lluvia: pluviómetro, mm. Dirección del viento: veleta, sin número (norte, sur, este, oeste). Regla: dejar el instrumento siempre en el mismo lugar y medir a la misma hora.",
        ["relaciona cada característica con su instrumento", "indica la unidad", "escribe una regla de uso"],
        ["tabla completa", "dibujos", "regla escrita"],
        ["mezclar instrumentos y características", "olvidar la unidad"],
        "Valora la tabla completa y pide que explique por qué hay que usar el instrumento en el mismo lugar.",
    ),
    reinforce="Haz tres tarjetas con cada instrumento y su unidad, y mézclalas con las características para emparejarlas.",
    extend="Averigua si en tu colegio o comuna hay algún instrumento del tiempo y escribe cuál es.",
)

register(
    OA13, 2,
    materials="Una botella plástica transparente de 2 litros cortada por un adulto (se usa la parte de abajo), una regla, cinta adhesiva y un lugar abierto. Este cuaderno trae los datos si no puedes hacerlo.",
    use="Aprenderé a construir un pluviómetro simple y a leer la lluvia en milímetros. Sirve para saber cuánta lluvia cae en mi casa.",
    prior=["Sé que el pluviómetro mide lluvia.", "Sé que 10 milímetros (mm) son 1 centímetro (cm)."],
    explain=[
        "Un pluviómetro simple se hace con una botella transparente cortada, con la parte de abajo hacia arriba. Pego una regla en el costado, con el 0 cerca del fondo, y lo pongo en un lugar abierto y firme. Así la lluvia cae dentro y no se escapa.",
        "Para que mida bien, primero calibro: echo agua hasta que el nivel llegue justo al 0 de la regla. Después de la lluvia, leo en milímetros hasta dónde subió el agua y la vacío para la próxima medición. Si el agua sube 5 mm, cayeron 5 milímetros de lluvia.",
        "El pluviómetro debe estar siempre en el mismo lugar, lejos de techos y árboles que echen agua dentro. Si lo muevo o no lo vacío, los datos no sirven. 10 mm son 1 cm: si el agua subió 1 cm, cayeron 10 milímetros.",
    ],
    vocab=[("pluviómetro", "instrumento que mide la lluvia"), ("milímetro (mm)", "unidad pequeña de longitud; 10 mm son 1 cm"), ("calibrar", "ajustar un instrumento para que mida bien desde el cero"), ("nivel", "altura a la que llega el agua"), ("vaciar", "sacar el agua para la siguiente medición")],
    worked=[
        {"title": "Leer el pluviómetro", "problem": "Después de una lluvia, el agua llega a la marca 7 de la regla (en mm). ¿Cuánta lluvia cayó?", "steps": ["La regla parte en 0 en el fondo.", "El agua llegó a la marca 7.", "Cada marca es 1 mm."], "answer": "7 mm"},
        {"title": "De centímetros a milímetros", "problem": "Un día el agua subió 2 cm. ¿Cuántos milímetros son?", "steps": ["1 cm son 10 mm.", "Para 2 cm, multiplico 2 × 10.", "2 × 10 = 20."], "answer": "20 mm"},
    ],
    mistakes=[
        {"wrong": "Medir sin vaciar el pluviómetro entre lluvias.", "why": "Se suman lluvias de distintos días sin darse cuenta.", "fix": "Lee, anota y vacía el pluviómetro después de cada medición."},
        {"wrong": "Poner el pluviómetro bajo el borde del techo.", "why": "El techo echa agua extra adentro.", "fix": "Ponlo en un lugar abierto, lejos de techos y árboles."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué mide un pluviómetro?", "Cuánta lluvia cayó", "Mide la lluvia."),
            ex("¿En qué unidad se lee la lluvia en el pluviómetro?", "Milímetros", "La regla tiene marcas en mm."),
            ex("Completa: antes de usar el pluviómetro hay que ___ el agua para llegar al 0.", "calibrar", "Calibrar es ajustar para medir desde 0."),
        ],
        "understand": [
            ex("¿Por qué se vacía el pluviómetro después de leer?", "Para medir solo la lluvia siguiente", "Si no, se suma agua de días anteriores."),
            ex("¿Por qué debe estar en un lugar abierto?", "Para que solo caiga lluvia y no agua de un techo", "Los techos y árboles añaden agua."),
            ex("¿Cuántos milímetros son 1 cm?", "10 mm", "Un centímetro tiene 10 milímetros."),
        ],
        "apply": [
            ex("El agua llegó a la marca 12 de la regla. ¿Cuántos milímetros de lluvia cayeron?", "12 mm", "Cada marca es 1 mm."),
            arith("Lunes cayeron 4 mm, martes 0 mm y miércoles 9 mm. ¿Cuántos mm cayeron en total?", "4+0+9", "Se suman las lluvias de los tres días.", " mm"),
            arith("El agua subió 3 cm en un pluviómetro. ¿Cuántos mm son?", "3*10", "1 cm son 10 mm, por eso se multiplica por 10.", " mm"),
        ],
        "reason": [
            ex("Sara dice que cayeron 15 mm de lluvia porque su pluviómetro marca 15, pero no lo vació desde ayer, y ayer se midieron 6 mm. ¿Cuánto cayó hoy?", "9 mm", "15 − 6 = 9 mm cayeron hoy."),
            ex("Luis puso su pluviómetro bajo el techo y marcó 25 mm mientras el de su vecino, al aire libre, marcó 5 mm. ¿Cuál es más confiable y por qué?", "El del vecino, porque está al aire libre", "El techo agregó agua al de Luis."),
        ],
        "challenge": [
            arith("Una semana tuvo lluvias de 6 mm, 0 mm, 0 mm, 14 mm, 3 mm, 0 mm y 7 mm. ¿Cuántos mm cayeron en total?", "6+0+0+14+3+0+7", "Se suman todos los días de la semana.", " mm"),
            ex("En una semana, ¿qué día llovió más: lunes 8 mm, martes 11 mm, miércoles 5 mm o jueves 2 mm?", "Martes", "11 mm es el mayor valor."),
        ],
    },
    context=[ex("En la casa de Mateo llovió toda una noche. Por la mañana, el agua en su pluviómetro llegó a 1 cm y 5 mm. ¿Cuántos mm de lluvia cayeron?", "15 mm", "1 cm son 10 mm y 10 + 5 = 15 mm.")],
    selfcheck=[
        ex("¿Dónde conviene poner el pluviómetro: bajo un techo o en un lugar abierto?", "En un lugar abierto", "Para que solo entre lluvia."),
        ex("¿Cuántos milímetros son 2 cm?", "20 mm", "2 × 10 = 20 mm."),
        ex("¿Qué se hace con el agua después de leer?", "Se vacía", "Para empezar de nuevo desde 0."),
    ],
    open_task=task(
        "Con una botella cortada por un adulto, una regla pegada y un poco de agua para calibrar, arma un pluviómetro y ponlo en el patio. Echa un poco de agua para calibrarlo hasta el 0. Si no puedes, usa este registro de ejemplo: lunes 0 mm, martes 6 mm, miércoles 12 mm. Anota los datos en una tabla, calcula el total y dibuja el pluviómetro con el nivel del miércoles.",
        "Lunes 0 mm, martes 6 mm, miércoles 12 mm. Total: 0 + 6 + 12 = 18 mm. El dibujo muestra el agua en la marca 12.",
        ["anota los datos en una tabla", "calcula el total", "dibuja el nivel de la medición"],
        ["tabla con los datos", "cálculo escrito", "dibujo del pluviómetro"],
        ["no vaciar entre mediciones", "poner el pluviómetro bajo un techo"],
        "Reconoce el cuidado en anotar y pide que cuente dónde pondría el pluviómetro para que mida bien.",
    ),
    reinforce="Mide con una regla la altura de agua en un vaso y exprésala en milímetros.",
    extend="Compara los datos de tu pluviómetro con los de un compañero y explica por qué pueden ser distintos.",
)

register(
    OA13, 3,
    materials="Un termómetro de pared o ambiental seguro (no de mercurio) si tienes uno, y un lugar con sombra. Este cuaderno trae las escalas y los datos por si no lo tienes.",
    use="Aprenderé a leer un termómetro y a registrar la temperatura. Sirve para comparar el frío y el calor de distintos momentos.",
    prior=["Sé que la temperatura se mide en grados Celsius.", "Sé contar de 2 en 2."],
    explain=[
        "El termómetro tiene una escala con marcas y números. Dentro hay una columna de líquido que sube cuando hace calor y baja cuando hace frío. Para leer, miro hasta qué marca llega el final de la columna, con la vista a esa altura.",
        "Muchos termómetros marcan de 2 en 2 grados. Si la columna termina justo en una marca, leo ese número. Si termina en el medio de dos marcas, el valor está entre ellos: entre 14 y 16 es 15 °C. Los números bajo 0 se llaman negativos, como −3 °C.",
        "Para que los datos sirvan, pongo el termómetro a la sombra, siempre en el mismo lugar y mido a la misma hora. Si lo pongo al sol directo, marca más que el aire. No lo toco con la mano mucho rato porque mi calor cambia la medida.",
    ],
    vocab=[("escala", "marcas con números en un instrumento"), ("columna", "línea de líquido que sube y baja en el termómetro"), ("negativo", "número menor que 0, como −3"), ("sombra", "lugar donde no da el sol directo"), ("lectura", "número que leo en un instrumento")],
    worked=[
        {"title": "Leer una marca", "problem": "Un termómetro tiene marcas 10, 12, 14, 16, 18. La columna termina justo en la marca 16. ¿Qué temperatura es?", "steps": ["Miro dónde termina la columna.", "Termina exactamente en la marca 16.", "Leo 16 °C."], "answer": "16 °C"},
        {"title": "Entre dos marcas", "problem": "Con las mismas marcas, la columna termina justo en el medio entre 14 y 16. ¿Qué temperatura es?", "steps": ["El medio entre 14 y 16 es 15.", "La columna está exactamente en la mitad.", "Leo 15 °C."], "answer": "15 °C"},
    ],
    mistakes=[
        {"wrong": "Dejar el termómetro al sol directo y decir que esa es la temperatura del aire.", "why": "El termómetro se calienta más que el aire.", "fix": "Ponlo a la sombra y siempre en el mismo lugar."},
        {"wrong": "Leer solo la marca de más arriba cuando la columna está en el medio.", "why": "Se redondea sin pensar.", "fix": "Si está en el medio entre dos marcas, el valor está en el medio."},
    ],
    tiers={
        "recovery": [
            ex("Un termómetro marca 12 °C. ¿Qué hay que anotar?", "12 °C", "Se anota el número y la unidad."),
            ex("¿La columna sube cuando hace calor o cuando hace frío?", "Cuando hace calor", "El calor hace subir el líquido."),
            ex("Completa: el termómetro se pone a la ___ para medir el aire.", "sombra", "Así no se calienta de más."),
        ],
        "understand": [
            ex("¿Por qué no debes sostener el termómetro mucho rato con la mano?", "Porque mi calor cambia la medida", "La mano lo calienta."),
            ex("¿Qué significa −3 °C?", "Una temperatura bajo cero", "−3 está por debajo de 0."),
            ex("¿Por qué se mide siempre a la misma hora?", "Para poder comparar los datos", "La temperatura cambia durante el día."),
        ],
        "apply": [
            ex("Un termómetro marca de 2 en 2: 20, 22, 24, 26. La columna llega a la marca 24. ¿Qué lees?", "24 °C", "Se lee el número de la marca."),
            ex("Con esa misma escala, la columna queda en el medio entre 22 y 24. ¿Qué lees?", "23 °C", "El medio entre 22 y 24 es 23."),
            arith("La mañana marcó 11 °C y la tarde 19 °C. ¿Cuántos grados subió?", "19-11", "Se resta la temperatura baja a la alta.", " °C"),
        ],
        "reason": [
            ex("Claudia midió el lunes a las 8:00 a la sombra y el martes a las 15:00 al sol. Dice que el martes fue más caluroso. ¿Qué problema tiene su comparación?", "Cambió la hora y el lugar", "Así no se puede saber si cambió el día o las condiciones."),
            ex("Dos termómetros en el mismo lugar marcan 14 °C y 21 °C. ¿Qué debería hacerse?", "Revisar cuál está bien puesto o cuál está dañado", "El mismo lugar debería dar valores casi iguales."),
        ],
        "challenge": [
            ex("Ordena de menor a mayor: 6 °C, −2 °C, 13 °C, 0 °C.", "−2 °C, 0 °C, 6 °C, 13 °C", "Los negativos son menores que 0."),
            arith("Un día, a las 8:00, la temperatura fue 7 °C. A las 14:00 fue 15 °C. ¿Cuánto subió?", "15-7", "Se resta lo de la mañana a lo de la tarde.", " °C"),
        ],
    },
    context=[ex("Laura registra la temperatura a las 8:00 durante 3 días: martes 9 °C, miércoles 11 °C, jueves 8 °C. ¿Qué día fue el más frío?", "Jueves", "8 °C es el menor valor.")],
    selfcheck=[
        ex("¿Qué se lee en la escala del termómetro?", "Hasta dónde llega la columna", "El final de la columna da la temperatura."),
        ex("¿Dónde se pone el termómetro para medir el aire?", "A la sombra", "Así no se calienta de más."),
        ex("¿−4 °C es mayor o menor que 0 °C?", "Menor", "Los negativos son menores que 0."),
    ],
    open_task=task(
        "Con estos datos de una semana, tomados a las 9:00 en el mismo lugar a la sombra: lunes 12 °C, martes 14 °C, miércoles 10 °C, jueves 13 °C, viernes 16 °C. Haz una tabla, subraya el día más frío y el más cálido, y calcula cuántos grados cambió la temperatura entre el miércoles y el viernes.",
        "Más frío: miércoles (10 °C). Más cálido: viernes (16 °C). Entre miércoles y viernes: 16 − 10 = 6 °C más.",
        ["completa la tabla con los datos", "identifica el día más frío y el más cálido", "calcula la diferencia"],
        ["tabla con datos", "cálculo escrito", "frase de conclusión"],
        ["restar al revés", "no usar la unidad °C"],
        "Reconoce la tabla ordenada y pide que explique por qué se midió siempre a la misma hora y lugar.",
    ),
    reinforce="Dibuja un termómetro con la columna en 18 °C y otro en 5 °C, y rotúlalos.",
    extend="Anota la temperatura de un día a tres horas distintas, con el mismo termómetro y lugar, y describe cuándo sube y cuándo baja.",
)

register(
    OA13, 4,
    materials="Cartulina, un sorbete, un lápiz con goma de borrar, plasticina, una brújula o un mapa para ubicar el norte (con ayuda de un adulto), tijeras. Un adulto une el sorbete a la goma del lápiz con un alfiler con cabeza; los niños no manipulan alfileres. Los datos vienen en el cuaderno.",
    use="Aprenderé a hacer y leer una veleta y a juntar instrumentos en una estación del tiempo en casa. Sirve para registrar el tiempo de mi localidad.",
    prior=["Sé que el viento es aire que se mueve.", "Sé los puntos cardinales: norte, sur, este y oeste."],
    explain=[
        "La veleta tiene una flecha que gira libremente. El viento empuja la cola ancha y la punta apunta hacia el lugar de donde viene el viento. Si la punta mira al sur, el viento viene del sur y sopla hacia el norte.",
        "El sorbete con la flecha se une a la goma del lápiz con un alfiler, que pone un adulto, para que gire. Para que sirva, la fijo en un lugar abierto y marco los puntos cardinales con ayuda de un adulto y una brújula o un mapa. Debe estar firme y siempre en el mismo lugar. Si no gira, está mal armada.",
        "Una estación del tiempo en casa junta tres instrumentos: termómetro en la sombra, pluviómetro en un lugar abierto y veleta. Cada día anoto en una tabla, a la misma hora, temperatura, lluvia y dirección del viento. Con varios días puedo ver patrones.",
    ],
    vocab=[("veleta", "instrumento con una flecha que muestra de dónde viene el viento"), ("punto cardinal", "norte, sur, este u oeste"), ("dirección", "hacia dónde está o va algo"), ("estación del tiempo", "lugar donde se juntan instrumentos para medir el tiempo (no es una estación del año)"), ("patrón", "algo que se repite")],
    worked=[
        {"title": "Leer una veleta", "problem": "La punta de la veleta apunta al oeste. ¿De dónde viene el viento y hacia dónde sopla?", "steps": ["La punta apunta hacia donde viene el viento.", "Apunta al oeste.", "El viento viene del oeste y sopla hacia el este."], "answer": "Viene del oeste y sopla hacia el este"},
        {"title": "Armar el registro", "problem": "Hoy el termómetro marca 13 °C, el pluviómetro 0 mm y la veleta apunta al sur. ¿Cómo lo anotas?", "steps": ["Temperatura: 13 °C.", "Lluvia: 0 mm.", "Viento del sur."], "answer": "13 °C, 0 mm, viento del sur"},
    ],
    mistakes=[
        {"wrong": "Decir que el viento va hacia donde apunta la punta.", "why": "Se confunde dirección del viento con hacia dónde sopla.", "fix": "La punta mira de dónde viene el viento."},
        {"wrong": "Fabricar una veleta pegada que no gira.", "why": "Se arma solo para adornar.", "fix": "Prueba soplando suavemente: si no gira, debes volver a armarla."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué muestra una veleta?", "De dónde viene el viento", "La punta apunta hacia el origen del viento."),
            ex("La punta de la veleta apunta al norte. ¿De dónde viene el viento?", "Del norte", "La punta mira de donde viene."),
            ex("Completa: norte, sur, este y ___.", "oeste", "Son los cuatro puntos cardinales."),
        ],
        "understand": [
            ex("¿Por qué la veleta debe girar libremente?", "Para poder apuntar a donde viene el viento", "Si no gira, no se orienta."),
            ex("¿Qué junta una estación del tiempo en casa?", "Un termómetro, un pluviómetro y una veleta", "Cada uno mide una característica distinta."),
            ex("¿Por qué se anota siempre a la misma hora?", "Para comparar días distintos", "Así los datos son comparables."),
        ],
        "apply": [
            ex("La punta de la veleta apunta al este. ¿Hacia dónde sopla el viento?", "Hacia el oeste", "Si viene del este, va hacia el oeste."),
            ex("Registro: martes 11 °C, 4 mm de lluvia, viento del sur. ¿Qué día hubo lluvia?", "El martes", "Cayeron 4 mm."),
            ex("Registro: miércoles 14 °C, 0 mm de lluvia, viento del oeste. ¿Hubo lluvia el miércoles?", "No", "0 mm quiere decir que no llovió."),
        ],
        "reason": [
            ex("Ema dice: «Si la punta de la veleta apunta al norte, el viento va hacia el norte». ¿Tiene razón?", "No; viene del norte y va hacia el sur", "La punta señala de dónde viene."),
            ex("Una veleta pegada con cinta al palo no gira. ¿Qué datos dará?", "Siempre la misma dirección, aunque el viento cambie", "No sigue al viento y por eso no sirve."),
        ],
        "challenge": [
            ex("Lunes: viento del sur y 9 °C. Martes: viento del norte y 17 °C. ¿Qué día fue más cálido y de dónde venía el viento ese día?", "El martes; del norte", "17 °C es mayor que 9 °C."),
            ex("Con tres días de registro, ¿puedes asegurar cómo es el tiempo de todo el año? Explica.", "No", "Se necesitan muchos más días para ver un patrón."),
        ],
    },
    context=[ex("Los datos de la estación del tiempo de Beatriz son: lunes 15 °C, 0 mm, viento del oeste; martes 12 °C, 8 mm, viento del sur; miércoles 13 °C, 2 mm, viento del sur. ¿En cuántos días llovió?", "En 2 días", "Martes y miércoles tuvieron lluvia.")],
    selfcheck=[
        ex("¿Qué indica la punta de una veleta?", "De dónde viene el viento", "Apunta al origen del viento."),
        ex("¿Qué instrumento de la estación mide la lluvia?", "El pluviómetro", "Mide en milímetros."),
        ex("¿Dónde se pone la veleta?", "En un lugar abierto", "Donde el viento llegue sin obstáculos."),
    ],
    open_task=task(
        "Dibuja una estación del tiempo con termómetro, pluviómetro y veleta. Con estos datos de dos días, completa un registro: viernes 14 °C, 0 mm, la punta apunta al sur; sábado 10 °C, 5 mm, la punta apunta al oeste. Escribe de dónde vino el viento cada día.",
        "Viernes: 14 °C, sin lluvia, viento del sur. Sábado: 10 °C, 5 mm, viento del oeste.",
        ["dibuja los tres instrumentos", "completa el registro con los datos", "dice de dónde viene el viento"],
        ["dibujo de la estación", "registro completo", "frase sobre el viento"],
        ["decir hacia dónde va en vez de de dónde viene", "mezclar los datos de los días"],
        "Valora la precisión del registro y pide que explique cómo sabría si el viento cambia de dirección.",
    ),
    reinforce="Arma una veleta con cartulina y un sorbete y pruébala soplando suavemente desde distintos lados.",
    extend="Anota la dirección del viento tres días y escribe si cambió.",
)

# ---------------------------------------------------------------- OA 14
register(
    OA14, 1,
    materials="Una hoja con la tabla de este cuaderno, lápices de colores. Si quieres, una ventana para mirar el cielo. Los datos vienen en el cuaderno.",
    use="Aprenderé que una estación del año no es un tipo de día, sino un patrón de varios meses con más luz, calor, frío o lluvia. Sirve para no confundir el tiempo de hoy con la estación.",
    prior=["Sé las cuatro estaciones: verano, otoño, invierno y primavera.", "Sé que el tiempo atmosférico cambia de un día a otro."],
    explain=[
        "Una estación es una parte del año que dura unos tres meses. En cada una se repite un patrón: cuánta luz hay en el día, qué temperatura suele haber y cuánta lluvia cae. El patrón se ve mirando muchos días, no uno solo.",
        "El tiempo de hoy y la estación son cosas distintas. Un día de invierno puede ser soleado y un día de verano puede ser nublado. Una estación se reconoce por lo que pasa casi siempre en esos meses. En verano los días son más largos que en invierno.",
        "En Chile, el verano va desde cerca del 21 de diciembre hasta cerca del 20 de marzo y el invierno, desde cerca del 21 de junio hasta cerca del 22 de septiembre. Cuando aquí es verano, en el hemisferio norte (por ejemplo, en Canadá) es invierno. Pero lo que se vive en cada lugar de Chile puede ser distinto.",
    ],
    vocab=[("estación", "parte del año con un patrón de tiempo"), ("patrón", "algo que se repite"), ("horas de luz", "cuántas horas del día hay luz del sol"), ("tendencia", "lo que suele pasar casi siempre"), ("tiempo atmosférico", "cómo está el día hoy")],
    worked=[
        {"title": "Tiempo de hoy o estación", "problem": "Hoy, 10 de julio, salió el sol y marcó 17 °C. Rafael dice que ya no es invierno. ¿Tiene razón?", "steps": ["Julio está en el invierno en Chile.", "Un día soleado es el tiempo de hoy.", "La estación se decide mirando varios días, no uno."], "answer": "No; sigue siendo invierno"},
        {"title": "Horas de luz", "problem": "Datos de ejemplo: en un día de verano hay 14 horas de luz y en un día de invierno hay 10. ¿Cuántas horas más tiene el día de verano?", "steps": ["Verano: 14 horas.", "Invierno: 10 horas.", "Resto: 14 − 10 = 4."], "answer": "4 horas más"},
    ],
    mistakes=[
        {"wrong": "Decir que como llovió hoy ya es invierno.", "why": "Se usa un solo día para decidir.", "fix": "La estación se reconoce por el patrón de muchos días."},
        {"wrong": "Pensar que en todos los países las estaciones son iguales al mismo tiempo.", "why": "Se piensa que el calendario es igual en todas partes.", "fix": "Cuando en Chile es verano, en el hemisferio norte (por ejemplo, en Canadá) es invierno."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuánto dura más o menos una estación: un día o unos tres meses?", "Unos tres meses", "Cada estación dura unos tres meses."),
            ex("¿En qué estación los días son más largos?", "En verano", "En verano hay más horas de luz."),
            ex("Completa: la lluvia de hoy es el ___ atmosférico.", "tiempo", "Describe el día, no la estación."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre el tiempo de hoy y la estación?", "El tiempo es de hoy y la estación es un patrón de varios meses", "Una estación dura meses."),
            ex("¿Por qué se necesitan muchos días para reconocer una estación?", "Porque un solo día puede ser distinto del patrón", "El patrón se ve repetido."),
            ex("¿Qué estación es en Chile en enero?", "Verano", "Enero está entre diciembre y marzo."),
        ],
        "apply": [
            arith("Datos de ejemplo: en verano hay 15 horas de luz y en invierno 10. ¿Cuántas horas más hay en verano?", "15-10", "Se resta las horas de invierno a las de verano.", " horas"),
            ex("Es 20 de enero y cae una lluvia suave. ¿En qué estación estamos?", "Verano", "Una lluvia no cambia la estación."),
            ex("Es 15 de julio y hay sol y 15 °C. ¿En qué estación estamos?", "Invierno", "Julio es invierno en Chile."),
        ],
        "reason": [
            ex("Un compañero dice: «Hoy hay mucho sol, entonces es verano». Es 5 de agosto. ¿Qué evidencia dice que no?", "Que agosto es invierno en Chile", "Un día de sol no cambia la estación."),
            ex("En una ciudad de Chile, en enero es verano. Un amigo vive en Canadá y dice que allí hace mucho frío en enero. ¿Cómo se explica?", "Porque en Canadá, en el hemisferio norte, las estaciones son opuestas", "Cuando aquí es verano, allá es invierno."),
        ],
        "challenge": [
            ex("Si tienes datos de 7 días seguidos de julio y 5 fueron fríos, ¿cuál es el patrón?", "Que en julio suele hacer frío", "La mayoría de los días mostró frío."),
            ex("Explica por qué no podemos decir que estamos en primavera solo porque vimos una flor en el invierno.", "Porque una flor no define la estación", "La estación se ve en el patrón de muchos días."),
        ],
    },
    context=[ex("Un 3 de enero hay nubes y llovizna. Valeria dice: «Hoy ya no es verano». ¿Qué le respondes con datos?", "Que enero es verano; el tiempo de hoy no cambia la estación", "La estación dura meses y hoy es solo un día.")],
    selfcheck=[
        ex("¿Una estación dura un día o varios meses?", "Varios meses", "Es parte del año."),
        ex("¿En qué estación hay menos horas de luz?", "En invierno", "Los días son más cortos."),
        ex("¿Un día de lluvia en verano cambia la estación?", "No", "El tiempo de hoy no es la estación."),
    ],
    open_task=task(
        "Con estos datos de ejemplo de Chile central, escribe si cada fecha es verano, otoño, invierno o primavera, y si el tiempo del día es típico o no: 10 de enero, sol y 29 °C; 12 de julio, lluvia y 8 °C; 14 de julio, sol y 18 °C; 5 de octubre, flores y 20 °C. Explica por qué el 14 de julio sigue siendo invierno.",
        "10 de enero: verano, típico. 12 de julio: invierno, típico. 14 de julio: invierno, día soleado menos típico. 5 de octubre: primavera, típico. El 14 de julio sigue siendo invierno porque la estación depende de muchos días.",
        ["identifica la estación de cada fecha", "distingue tiempo y estación", "explica con evidencia"],
        ["tabla completa", "frase explicativa", "dibujo de dos estaciones"],
        ["cambiar la estación según un día", "no usar las fechas"],
        "Reconoce el uso de las fechas y pide que explique qué otro dato ayudaría a confirmar la estación.",
    ),
    reinforce="Anota el tiempo durante 5 días y escribe cuál estación es y por qué.",
    extend="Averigua qué estación es ahora en un país del hemisferio norte y compárala con la de Chile.",
)

register(
    OA14, 2,
    materials="Un mapa de Chile dibujado o impreso (norte, centro, sur) y lápices de colores. Los datos de cada zona vienen en este cuaderno. ",
    use="Aprenderé que el tiempo y las estaciones no son iguales en todo Chile. Sirve para entender por qué en el norte, en el centro y en el sur se vive distinto.",
    prior=["Sé que Chile es largo y angosto.", "Sé qué son el norte, el centro y el sur."],
    explain=[
        "Chile es muy largo, por eso el tiempo cambia mucho entre el norte y el sur. En el norte hay un desierto, el desierto de Atacama, uno de los más secos del mundo, donde casi no llueve. En el altiplano del norte, las lluvias suelen llegar en el verano.",
        "En la zona central los veranos son calurosos y secos y los inviernos son más fríos con lluvia. En el sur llueve gran parte del año y las temperaturas son más bajas. En la zona austral hace frío, hay mucho viento y puede nevar.",
        "Por eso no puedo aplicar a todo Chile la misma idea de las cuatro estaciones. En la zona central se notan bien. En el desierto casi no cambia la lluvia en el año. En el sur llueve todo el año, más en invierno. Para cada lugar hay que mirar sus propios datos.",
    ],
    vocab=[("desierto", "lugar donde llueve muy poco"), ("zona central", "parte de Chile con veranos secos e inviernos con lluvia"), ("zona austral", "parte más al sur de Chile, fría y ventosa"), ("contraste", "diferencia grande entre dos cosas"), ("región", "parte de un país con características propias")],
    worked=[
        {"title": "Comparar dos zonas", "problem": "Datos de ejemplo de lluvia anual: una ciudad del desierto del norte tiene 2 mm al año y una ciudad del sur tiene 1.500 mm. ¿Cuál es más lluviosa?", "steps": ["Comparo 2 y 1.500.", "1.500 es mucho mayor que 2.", "La ciudad del sur es mucho más lluviosa."], "answer": "La ciudad del sur"},
        {"title": "No aplicar el mismo modelo", "problem": "Un niño dice: «En todo Chile el invierno trae lluvia». ¿Es cierto en el desierto del norte?", "steps": ["En el desierto casi no llueve en todo el año.", "El invierno no trae lluvias importantes allí.", "La idea no sirve para todo Chile."], "answer": "No; en el desierto casi no llueve ni en invierno"},
    ],
    mistakes=[
        {"wrong": "Decir que en todo Chile las estaciones son iguales.", "why": "Se usa solo la zona donde se vive como modelo.", "fix": "Compara datos de cada zona."},
        {"wrong": "Pensar que en el sur nunca hace calor.", "why": "Se generaliza una idea.", "fix": "En el sur también hay días cálidos, pero en general es más frío y lluvioso."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué zona de Chile está el desierto de Atacama: norte, centro o sur?", "Norte", "Atacama está en el norte de Chile."),
            ex("¿En qué zona llueve gran parte del año?", "El sur", "En el sur la lluvia es frecuente."),
            ex("Completa: Chile es largo y por eso su tiempo es muy ___ según la zona.", "distinto", "Cambia entre el norte y el sur."),
        ],
        "understand": [
            ex("¿Por qué el tiempo cambia tanto entre el norte y el sur de Chile?", "Porque Chile es muy largo", "Va desde lugares muy calurosos hasta lugares muy fríos."),
            ex("¿Cómo son los veranos en la zona central?", "Calurosos y secos", "Casi no llueve en verano."),
            ex("¿Qué es un contraste?", "Una diferencia grande entre dos cosas", "Entre las zonas de Chile hay contrastes."),
        ],
        "apply": [
            ex("Datos de ejemplo de lluvia anual: norte 5 mm, centro 350 mm, sur 1.800 mm. ¿Qué zona es la más seca?", "El norte", "5 mm es la menor."),
            arith("Con los mismos datos, ¿cuántos mm más llueve en el sur (1.800) que en el centro (350)?", "1800-350", "Se resta el menor al mayor.", " mm"),
            ex("En una zona hace frío, llueve casi todo el año y hay viento fuerte. ¿Cuál zona de Chile se parece a esa descripción?", "La zona austral o sur", "Es lo típico del sur de Chile."),
        ],
        "reason": [
            ex("Vicente vive en la zona central y dice que en todo Chile los veranos son secos. ¿Qué dato lo contradice?", "El altiplano del norte tiene lluvias en verano", "No siempre el verano es seco en todo Chile."),
            ex("Dos niños comparan: en la ciudad A llueven 4 mm al año y en la B, 900 mm. ¿Cuál puede estar en el desierto?", "La A", "Casi no llueve en la ciudad A."),
        ],
        "challenge": [
            ex("Explica por qué no sirve usar los mismos meses de lluvia para todo Chile.", "Porque cada zona tiene sus propios patrones", "Chile tiene muchos contrastes."),
            ex("Si en tu ciudad hay mucha lluvia en invierno, ¿qué puedes decir de su zona?", "Que probablemente es de la zona central o sur", "Allí el invierno es lluvioso."),
        ],
    },
    context=[ex("La familia de Tomás viaja en febrero del norte desértico al sur. En el norte hace calor y no llueve, en el sur hace fresco y hay chubascos. ¿Qué enseñanza deja ese viaje sobre Chile?", "Que el tiempo cambia entre zonas aunque sea la misma estación", "En la misma fecha hay climas distintos.")],
    selfcheck=[
        ex("¿Dónde llueve muy poco en Chile?", "En el desierto del norte", "Atacama casi no recibe lluvia."),
        ex("¿Qué zona de Chile tiene inviernos más fríos y lluviosos?", "La zona central y el sur", "Allí llueve más en invierno."),
        ex("¿Todas las zonas de Chile tienen las mismas estaciones?", "No", "Hay contrastes entre ellas."),
    ],
    open_task=task(
        "Dibuja Chile en una franja vertical y divídela en norte, centro y sur. En cada parte pega un dibujo: desierto con sol, árboles con lluvia en invierno y paisaje frío con nubes y lluvia. Escribe una frase en cada zona que diga cómo es el tiempo. Cierra con una frase: «Chile tiene contrastes porque…».",
        "Norte: desierto con casi nada de lluvia. Centro: veranos calurosos y secos, inviernos con lluvia. Sur: frío y lluvioso. Chile tiene contrastes porque es muy largo.",
        ["dibuja las tres zonas", "describe el tiempo de cada una", "explica por qué hay contrastes"],
        ["dibujo de Chile", "frases por zona", "frase final"],
        ["usar una sola zona como modelo de todo Chile", "mezclar las zonas"],
        "Reconoce el dibujo ordenado y pide que cuente en qué zona vive y cómo es su tiempo.",
    ),
    reinforce="Haz una tabla con tres columnas, norte, centro y sur, y anota una palabra para el tiempo de cada zona.",
    extend="Averigua en qué zona vive un familiar o amigo y compara su tiempo de hoy con el tuyo.",
)

register(
    OA14, 3,
    materials="Una hoja y lápices de colores. Si puedes, observa una planta o árbol cercano a lo largo de los meses. Este cuaderno trae descripciones por si no puedes salir.",
    use="Aprenderé cómo los cambios de las estaciones afectan a plantas, animales, personas y al ambiente. Sirve para entender por qué los árboles cambian y por qué usamos ropa distinta.",
    prior=["Sé que las plantas y los animales son seres vivos.", "Sé que las estaciones cambian la temperatura y la lluvia."],
    explain=[
        "Los seres vivos responden a los cambios de las estaciones. Algunos árboles pierden sus hojas en otoño y las vuelven a sacar en primavera. Otros, como el pino y el peumo, mantienen sus hojas todo el año. Muchas plantas florecen en primavera, cuando hay más luz y calor.",
        "Los animales también responden. En invierno, algunos animales buscan lugares más abrigados y otros comen más en otoño. Algunas aves viajan a lugares más cálidos cuando empieza el frío. Las personas cambian su ropa y sus actividades según la estación.",
        "El ambiente también cambia. Con la lluvia del invierno los ríos llevan más agua y el pasto se pone verde en la zona central. En verano el pasto se seca y hay menos agua. Estos cambios se repiten cada año.",
    ],
    vocab=[("hojas caducas", "hojas que el árbol pierde en otoño"), ("florecer", "echar flores una planta"), ("ambiente", "lo que rodea a los seres vivos: aire, agua, suelo"), ("migrar", "viajar un animal a otro lugar en cierta época del año"), ("responder", "cambiar o actuar por lo que pasa alrededor")],
    worked=[
        {"title": "Un árbol en el año", "problem": "Un árbol tiene hojas verdes en verano, amarillas en otoño, ninguna en invierno y brotes en primavera. ¿Qué tipo de árbol es?", "steps": ["Pierde las hojas en otoño.", "Las vuelve a sacar en primavera.", "Es un árbol de hojas caducas."], "answer": "Un árbol de hojas caducas"},
        {"title": "Efectos de la lluvia", "problem": "En invierno llueve mucho en la zona central. ¿Qué pasa con el pasto y con el río?", "steps": ["Llueve más y hay más agua en el suelo.", "El pasto crece y se pone verde.", "El río lleva más agua."], "answer": "El pasto se pone verde y el río lleva más agua"},
    ],
    mistakes=[
        {"wrong": "Decir que un árbol que pierde las hojas en otoño está muerto.", "why": "Se piensa que sin hojas no hay vida.", "fix": "Las hojas caducas vuelven en primavera, así que el árbol sigue vivo."},
        {"wrong": "Creer que todos los animales hacen lo mismo en invierno.", "why": "Se generaliza.", "fix": "Cada animal responde a su manera: algunos buscan abrigo, otros migran."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué estación muchas plantas echan flores?", "Primavera", "Hay más luz y calor."),
            ex("¿Qué estación hace que algunos árboles pierdan sus hojas?", "Otoño", "Es cuando caen las hojas caducas."),
            ex("Completa: las personas usan ropa más abrigada en ___.", "invierno", "En invierno hace más frío."),
        ],
        "understand": [
            ex("¿Qué quiere decir que un ser vivo «responde» a la estación?", "Que cambia o actúa por lo que pasa alrededor", "Responde a la luz, el frío o la lluvia."),
            ex("¿Por qué el pasto se seca en verano en la zona central?", "Porque hay poca lluvia y mucho calor", "Sin agua el pasto se seca."),
            ex("¿Por qué un árbol sin hojas en invierno no está muerto?", "Porque vuelve a sacar hojas en primavera", "Es un árbol de hojas caducas."),
        ],
        "apply": [
            ex("Un árbol está sin hojas en julio y con brotes verdes en octubre. ¿Qué estación le hace sacar hojas nuevas?", "La primavera", "Con más luz y calor brotan hojas."),
            ex("Una niña ve que las aves del humedal ya no están en invierno y que han viajado a otro lugar. ¿Cómo se llama ese viaje?", "Migrar", "Migrar es viajar en cierta época del año."),
            arith("Una rama tiene 80 hojas. En otoño pierde 55 hojas. ¿Cuántas hojas le quedan?", "80-55", "Se resta lo que perdió a lo que tenía.", " hojas"),
        ],
        "reason": [
            ex("Matías dice: «Mi árbol perdió todas las hojas, entonces se murió». ¿Qué observación podría hacer para saber?", "Ver si le salen hojas nuevas en primavera", "Si brotan, está vivo."),
            ex("En invierno el río tiene mucha agua y en verano casi no tiene. ¿Qué explica el cambio?", "La lluvia del invierno", "En invierno cae más agua que escurre al río."),
        ],
        "challenge": [
            ex("Nombra una respuesta de una planta, una de un animal y una de una persona a la llegada del invierno.", "Planta: pierde hojas; animal: busca abrigo; persona: usa abrigo", "Cada ser vivo responde a su manera."),
            ex("¿Por qué las flores de primavera se ven en muchas partes a la vez?", "Porque muchas plantas responden a la misma luz y calor", "Los cambios de la estación son los mismos para todas."),
        ],
    },
    context=[ex("En el parque de Camila, en abril las hojas del plátano oriental se ponen amarillas, y en octubre aparecen brotes verdes. ¿Qué estaciones indican esos cambios?", "Otoño y primavera", "Abril es otoño y octubre es primavera.")],
    selfcheck=[
        ex("¿Qué hacen los árboles de hojas caducas en otoño?", "Pierden sus hojas", "Las hojas caen."),
        ex("¿Qué estación trae más flores?", "Primavera", "Hay más luz y calor."),
        ex("¿Los animales responden todos igual al invierno?", "No", "Cada uno responde a su manera."),
    ],
    open_task=task(
        "Dibuja un mismo árbol en cuatro cuadros: verano, otoño, invierno y primavera. Debajo de cada uno escribe qué le pasa al árbol. Agrega una persona en cada cuadro con la ropa que usa y una frase que diga cómo cambió el ambiente (lluvia, pasto, río).",
        "Verano: hojas verdes, persona en polera, pasto seco. Otoño: hojas amarillas que caen, persona con chaleco. Invierno: árbol sin hojas, persona con abrigo, río con más agua. Primavera: brotes y flores, persona con ropa liviana.",
        ["dibuja las cuatro estaciones", "describe los cambios del árbol", "relaciona ropa y ambiente con la estación"],
        ["cuatro dibujos", "frases por cuadro", "frase final"],
        ["dibujar el árbol idéntico en todas", "no relacionar con la estación"],
        "Valora los detalles de cada cuadro y pide que explique qué estación fue la más difícil de dibujar y por qué.",
    ),
    reinforce="Pega o dibuja una hoja de cada estación y escribe de qué color era.",
    extend="Averigua qué animal de tu zona cambia su conducta con la llegada del invierno y explícalo.",
)

register(
    OA14, 4,
    materials="Una hoja con la tabla de datos de ejemplo de este cuaderno (ciudad de Chile central) y lápices. Los datos son de práctica y no representan una ciudad real.",
    use="Aprenderé a explicar un patrón local del tiempo y de los seres vivos usando datos. Sirve para decir «lo veo en los datos» en vez de adivinar.",
    prior=["Sé leer una tabla de datos.", "Sé que las estaciones cambian el tiempo y a los seres vivos."],
    explain=[
        "Un patrón es algo que se repite. Para explicarlo, uso tres pasos. Primero digo lo que veo en los datos. Después doy una evidencia con números. Por último explico qué relación tiene con la estación o con los seres vivos.",
        "Por ejemplo, con datos de una ciudad de ejemplo: en julio hay 9 °C y 90 mm de lluvia, y en enero hay 26 °C y 0 mm. Puedo decir: «En invierno hace más frío y llueve más», porque 9 °C es menos que 26 °C y 90 mm es más que 0 mm.",
        "Un solo dato no alcanza para un patrón. Necesito al menos varios meses. Y no puedo decir que todo Chile es igual: el patrón sirve para el lugar de los datos. Si cambio de lugar, tengo que mirar nuevos datos.",
    ],
    vocab=[("patrón", "algo que se repite"), ("evidencia", "dato o observación que apoya una idea"), ("explicar", "decir por qué pasa algo usando datos"), ("relación", "forma en que dos cosas se conectan"), ("dato", "número o información que se anota")],
    worked=[
        {"title": "Explicar con datos", "problem": "Datos de ejemplo: enero 26 °C y 0 mm de lluvia; julio 9 °C y 90 mm de lluvia. Explica el patrón.", "steps": ["Veo que enero es más cálido y julio más frío.", "Evidencia: 26 °C contra 9 °C. Lluvia: 0 mm contra 90 mm.", "Relación: el verano es cálido y seco; el invierno es frío y lluvioso."], "answer": "Verano cálido y seco; invierno frío y lluvioso"},
        {"title": "Dato con ser vivo", "problem": "En octubre, con 16 °C y 30 mm de lluvia, los árboles del parque tienen brotes y flores. ¿Qué relación hay?", "steps": ["En octubre es primavera.", "Hay más luz y calor que en invierno.", "Las plantas responden brotando y floreciendo."], "answer": "La primavera hace que las plantas broten y florezcan"},
    ],
    mistakes=[
        {"wrong": "Explicar un patrón con un solo día.", "why": "Se piensa que un dato basta.", "fix": "Usa varios meses o muchos días."},
        {"wrong": "Aplicar el patrón de una ciudad a todo Chile.", "why": "Se generaliza sin datos de otros lugares.", "fix": "Di que el patrón es del lugar de los datos."},
    ],
    tiers={
        "recovery": [
            ex("Datos de ejemplo: enero 26 °C, julio 9 °C. ¿Qué mes es más frío?", "Julio", "9 °C es menor que 26 °C."),
            ex("Datos de ejemplo: enero 0 mm, julio 90 mm. ¿Qué mes llueve más?", "Julio", "90 mm es mayor que 0 mm."),
            ex("Completa: un ___ es algo que se repite.", "patrón", "Un patrón se ve en varios datos."),
        ],
        "understand": [
            ex("¿Para qué sirve dar una evidencia con números?", "Para apoyar mi idea con datos", "Los números muestran que no estoy adivinando."),
            ex("¿Por qué un solo día no basta para hablar de un patrón?", "Porque puede ser distinto de los demás", "Un patrón se ve cuando se repite."),
            ex("¿Para qué lugar sirve un patrón sacado de los datos de una ciudad?", "Para esa ciudad", "No se puede asegurar que sea igual en todo Chile."),
        ],
        "apply": [
            arith("Datos de ejemplo: enero 26 °C y julio 9 °C. ¿Cuántos grados más cálido es enero?", "26-9", "Se resta el valor frío al cálido.", " °C"),
            arith("Datos de ejemplo: abril 25 mm, mayo 40 mm, junio 60 mm de lluvia. ¿Cuántos mm cayeron en total?", "25+40+60", "Se suman las lluvias de los tres meses.", " mm"),
            ex("Datos de ejemplo: enero 26 °C, abril 17 °C, julio 9 °C, octubre 16 °C. Describe cómo cambia la temperatura de enero a julio.", "Baja", "Pasa de 26 a 9 °C."),
        ],
        "reason": [
            ex("Alicia observó solo el 3 de enero, que fue nublado y fresco, y dice: «El verano es siempre fresco». ¿Qué le falta?", "Más días o meses de datos", "Un día no muestra el patrón."),
            ex("En una ciudad de ejemplo, los álamos pierden las hojas en mayo. Pedro dice: «Como los álamos ya perdieron las hojas, ya es invierno». ¿Qué dato falta para afirmarlo?", "Datos de temperatura y lluvia de varios días", "No basta con las hojas, que también caen en otoño; hay que revisar el patrón del tiempo."),
        ],
        "challenge": [
            ex("Escribe una explicación completa con tres partes (qué veo, evidencia, relación) usando: julio 9 °C y 90 mm; enero 26 °C y 0 mm.", "Veo que en julio hace más frío y llueve más que en enero; julio tiene 9 °C y 90 mm contra 26 °C y 0 mm; por eso el invierno es frío y lluvioso", "Incluye los tres pasos."),
            ex("Si un compañero de otra zona tiene datos distintos, ¿qué deben hacer?", "Comparar los datos y explicar por qué cambian entre lugares", "Los patrones pueden ser distintos por zona."),
        ],
    },
    context=[ex("Mariana anotó que en el jardín las flores aparecen cuando los días tienen más horas de luz y más calor, y que en julio no hay flores. ¿Qué patrón puede explicar con esos datos?", "Las flores aparecen en primavera y verano, con más luz y calor", "Los datos relacionan flores con más luz y calor.")],
    selfcheck=[
        ex("¿Cuántos pasos tiene explicar un patrón?", "Tres", "Veo, evidencia y relación."),
        ex("¿Qué es una evidencia?", "Un dato que apoya mi idea", "Sirve para demostrar."),
        ex("¿Un solo día muestra un patrón?", "No", "Un patrón se repite."),
    ],
    open_task=task(
        "Usa estos datos de ejemplo: enero 28 °C, 0 mm, el pasto está seco; abril 18 °C, 25 mm, las hojas de los árboles se ponen amarillas; julio 8 °C, 85 mm, el río lleva mucha agua; octubre 15 °C, 30 mm, hay flores en el jardín. Escribe una explicación en tres partes: lo que ves, la evidencia con números y la relación con la estación y los seres vivos.",
        "Veo que en julio hace más frío y llueve más que en enero. Evidencia: julio tiene 8 °C y 85 mm, enero 28 °C y 0 mm. Relación: el invierno es frío y lluvioso, el río lleva más agua, y en primavera hay flores.",
        ["incluye lo que ve", "usa números como evidencia", "relaciona con la estación y los seres vivos"],
        ["texto de tres partes", "tabla con datos", "dibujo de una estación"],
        ["explicar con un solo dato", "generalizar a todo Chile"],
        "Reconoce el uso de números y pide que explique qué otro dato ayudaría a confirmar su explicación.",
    ),
    reinforce="Elige dos meses de la tabla y escribe una frase que los compare usando números.",
    extend="Anota durante un mes qué hacen las plantas del barrio y compara con los datos de este cuaderno.",
)
