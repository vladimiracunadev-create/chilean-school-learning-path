"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 14 (calor y temperatura) y OA 15 (calentar y enfriar agua)."""
from __future__ import annotations

from student_content_cn6_b import task
from student_lessons import arith, ex, register

OA14 = "CN06 OA 14"
OA15 = "CN06 OA 15"

# ================================================================ OA 14, clase 1
register(
    OA14, 1,
    materials="Papel y lápiz. Para la tarea abierta: una cuchara de metal, una cuchara de madera o plástico y un paño de tela, todos dentro de la misma pieza. No uses agua caliente.",
    use="Aprenderé a distinguir lo que mide un termómetro de lo que siente mi mano. Sirve para no confundir una sensación con un dato.",
    prior=["Sé leer números en un termómetro y sé que se mide en grados Celsius (°C).", "Sé separar una observación de una interpretación."],
    explain=[
        "La temperatura es una medida de qué tan caliente o frío está un objeto. Se mide con un termómetro y se expresa en grados Celsius (°C). Dos objetos que marcan lo mismo en el termómetro tienen la misma temperatura, aunque nuestra mano sienta algo distinto.",
        "El calor, en cambio, es una forma de energía que pasa de un objeto más caliente a uno más frío. No se mide con el termómetro: el termómetro mide temperatura. Por eso decir «el calor de la taza es 60 °C» es un error; lo correcto es «la temperatura de la taza es 60 °C».",
        "Un ejemplo: en una pieza, una cuchara de metal y una de madera marcan 20 °C en el termómetro. Sin embargo, la de metal se siente más fría. Observación: ambas marcan 20 °C. Interpretación: el metal quita calor a la mano más rápido que la madera. La mano no es un buen termómetro; el termómetro entrega un dato que otra persona puede repetir.",
    ],
    vocab=[("temperatura", "medida de qué tan caliente o frío está un objeto"), ("calor", "energía que pasa de un objeto más caliente a uno más frío"), ("termómetro", "instrumento que mide la temperatura"), ("grado Celsius (°C)", "unidad con la que se mide la temperatura"), ("sensación térmica", "lo caliente o frío que nos parece algo al tocarlo")],
    worked=[
        {"title": "Dato o sensación", "problem": "Frase A: «El termómetro marca 20 °C en la cuchara de metal y en la de madera». Frase B: «La cuchara de metal está más fría que la de madera». ¿Cuál se apoya en el dato medido?", "steps": ["La frase A cita la medición del termómetro.", "La frase B viene de la sensación de la mano y el termómetro dice lo contrario."], "answer": "La frase A; la B es una sensación que no coincide con los datos"},
        {"title": "Leer una diferencia de temperatura", "problem": "Una sopa marca 75 °C y un jugo marca 15 °C. ¿Cuántos °C más caliente está la sopa?", "steps": ["Las dos temperaturas están en °C.", "Resto: 75 − 15 = 60."], "answer": "60 °C más caliente"},
    ],
    mistakes=[
        {"wrong": "Decir que el calor se mide en °C.", "why": "Se confunden calor y temperatura.", "fix": "En °C se mide la temperatura. El calor es energía que pasa de un objeto a otro."},
        {"wrong": "Creer que lo que se siente más frío tiene menor temperatura.", "why": "Se usa la mano como instrumento.", "fix": "Mira el termómetro: dos objetos pueden tener la misma temperatura y sentirse distinto."},
    ],
    tiers={
        "recovery": [
            ex("Para saber cuántos °C marca la sopa de la olla, ¿qué instrumento usas?", "Un termómetro", "El termómetro entrega un dato en grados Celsius."),
            ex("Un té marca 62 °C y una leche marca 38 °C. ¿Cuál está a mayor temperatura?", "El té", "62 es mayor que 38."),
            ex("¿En qué unidad se mide la temperatura en Chile?", "Grados Celsius", "El termómetro de uso diario marca °C."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es el calor: energía que pasa de un objeto caliente a uno frío o una medida de lo caliente que está algo?", "Energía que pasa de un objeto caliente a uno frío", "La medida de lo caliente es la temperatura."),
            ex("Frase: «El termómetro marca 5 °C en el agua del refrigerador». ¿Observación o interpretación?", "Observación", "Es un dato medido."),
            ex("Frase: «Esa cuchara se siente fría porque el metal le quita calor a la mano más rápido». ¿Observación o interpretación?", "Interpretación", "Explica la sensación con una causa."),
        ],
        "apply": [
            arith("Una habitación está a 22 °C y la cocina a 31 °C. ¿Cuántos °C más caliente está la cocina?", "31-22", "Se resta la temperatura menor a la mayor.", " °C"),
            arith("A las 8:00 el termómetro de un patio marcaba 12 °C y a las 15:00 marcaba 27 °C. ¿Cuántos °C subió la temperatura?", "27-12", "Se resta la temperatura inicial a la final.", " °C"),
            ex("Ordena de menor a mayor temperatura: agua de la llave a 18 °C, agua del refrigerador a 6 °C, agua tibia a 35 °C.", "6 °C, 18 °C, 35 °C", "Se ordenan por el número de grados."),
        ],
        "reason": [
            ex("Ana dice: «La cuchara de metal está más fría que la de madera porque se siente más fría». El termómetro marca 20 °C en ambas. ¿Qué dato contradice a Ana?", "Ambas marcan 20 °C", "Tienen la misma temperatura aunque una se sienta más fría."),
            ex("Pedro escribe: «El calor del agua es 40 °C». ¿Qué palabra debe cambiar para que la frase sea correcta?", "Calor por temperatura", "En °C se mide la temperatura."),
        ],
        "challenge": [
            ex("Dos platos están en la misma pieza durante horas. El de cerámica y el de plástico marcan 19 °C. Al tocarlos, el de cerámica se siente más frío. ¿Qué dos conceptos permiten explicarlo: temperatura igual y distinta rapidez para sacar calor de la mano, o temperatura distinta?", "Temperatura igual y distinta rapidez para sacar calor de la mano", "El termómetro mide lo mismo y cambia la rapidez con que el material toma calor de la mano."),
            arith("En cuatro horas distintas se anotó 14 °C, 18 °C, 23 °C y 25 °C. ¿Cuántos °C subió la temperatura entre la primera y la última?", "25-14", "Se resta el primer dato al último.", " °C"),
        ],
    },
    context=[ex("Una persona de tu casa toca el pomo metálico de una puerta y dice «está helado», y toca la madera de la puerta y dice «está más tibia». Todo está dentro de la misma casa. ¿Qué dato necesitas para decidir si de verdad tienen distinta temperatura?", "La medición de un termómetro", "Solo una medición permite comparar las temperaturas.")],
    selfcheck=[
        ex("¿Qué se mide en °C: el calor o la temperatura?", "La temperatura", "El calor es energía transferida."),
        ex("Dos objetos marcan 25 °C en un termómetro. ¿Tienen igual o distinta temperatura?", "Igual", "El termómetro entrega el dato, aunque al tocarlos se sientan distintos."),
        ex("Una sensación al tocar algo, ¿es una medición de temperatura?", "No", "La mano puede equivocarse."),
    ],
    open_task=task(
        "Dentro de una misma pieza toca una cuchara de metal, una cuchara de madera o plástico y un paño de tela. Con tu mano ordénalas de la que se siente más fría a la menos fría. Luego supón que un termómetro marcó 20 °C en las tres y escribe una observación, una interpretación y una frase que explique por qué las sensaciones son distintas.",
        "Observación: el termómetro marcó 20 °C en las tres. Interpretación: el metal toma calor de la mano más rápido que la madera o la tela. Por eso se siente más frío, aunque la temperatura es la misma.",
        ["orden de sensaciones", "una observación y una interpretación separadas", "distingue temperatura de sensación"],
        ["orden escrito", "dos frases rotuladas"],
        ["decir que la temperatura de las tres es distinta", "no separar observación e interpretación"],
        "Pregunta qué diría un termómetro si lo pusieras en cada objeto y por qué.",
    ),
    reinforce="Escribe una frase que use bien la palabra temperatura y otra que use bien la palabra calor.",
    extend="Averigua con una persona de tu casa qué materiales usan para que las ollas no quemen las manos y por qué.",
)

# ================================================================ OA 14, clase 2
register(
    OA14, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno. No uses agua caliente sin una persona adulta.",
    use="Aprenderé a predecir cómo cambia la temperatura cuando un objeto caliente está en un lugar más frío. Sirve para anticipar hacia dónde viaja el calor.",
    prior=["Sé que el calor pasa de lo más caliente a lo más frío.", "Sé que la temperatura se mide con un termómetro."],
    explain=[
        "Una taza de té caliente que se deja en una mesa se va enfriando. Una pregunta comprobable es: «¿cómo cambia la temperatura del té en una pieza a 20 °C a medida que pasan los minutos?». Se responde midiendo con un termómetro cada cierto tiempo y anotando los datos.",
        "La predicción se apoya en una idea: el calor pasa del objeto más caliente al más frío. Entonces predecimos: «Si el té está a 60 °C y la pieza a 20 °C, entonces el té perderá calor y bajará su temperatura, hasta acercarse a 20 °C». No bajará mucho más, porque cuando las temperaturas se igualan el calor ya no fluye.",
        "Datos de una prueba con té (datos de ejemplo): a los 0 minutos 60 °C, a los 10 minutos 45 °C, a los 20 minutos 35 °C, a los 30 minutos 28 °C. Baja rápido al principio y cada vez más despacio. Si el dato no coincide con la predicción, se corrige la predicción.",
    ],
    vocab=[("pregunta comprobable", "pregunta que se responde con mediciones"), ("predicción", "resultado esperado apoyado en una idea"), ("flujo de calor", "paso de calor de un objeto caliente a uno frío"), ("temperatura ambiente", "temperatura del aire del lugar"), ("igualarse", "llegar a la misma temperatura")],
    worked=[
        {"title": "Predecir el sentido del calor", "problem": "Un vaso de jugo a 8 °C se deja en una pieza a 22 °C. ¿Su temperatura subirá o bajará?", "steps": ["El jugo está más frío que la pieza.", "El calor pasa de la pieza (más caliente) al jugo (más frío).", "Por eso la temperatura del jugo sube hacia 22 °C."], "answer": "Subirá, acercándose a 22 °C"},
        {"title": "Medir el cambio", "problem": "El té bajó de 60 °C a 45 °C en los primeros 10 minutos. ¿Cuántos °C bajó?", "steps": ["Se restan los dos datos en °C.", "60 − 45 = 15."], "answer": "15 °C"},
    ],
    mistakes=[
        {"wrong": "Predecir que el té bajará hasta 0 °C porque se enfría.", "why": "Se olvida que el calor deja de fluir cuando las temperaturas se igualan.", "fix": "El té solo baja hasta la temperatura de la pieza."},
        {"wrong": "Predecir que el calor pasa del jugo frío a la pieza más caliente.", "why": "Se invierte el sentido del calor.", "fix": "El calor siempre va del más caliente al más frío."},
    ],
    tiers={
        "recovery": [
            ex("¿Hacia qué objeto pasa el calor: el más caliente o el más frío?", "Hacia el más frío", "El calor pasa del más caliente al más frío."),
            ex("Una bebida a 4 °C se deja en una pieza a 20 °C. ¿Su temperatura sube o baja?", "Sube", "Recibe calor de la pieza."),
            ex("Una sopa a 70 °C se deja en una pieza a 20 °C. ¿Su temperatura sube o baja?", "Baja", "Pierde calor hacia la pieza."),
        ],
        "understand": [
            ex("Un té a 60 °C está en una pieza a 20 °C. Según la predicción, ¿a qué temperatura se acerca?", "A 20 °C", "Se iguala con la temperatura de la pieza."),
            ex("¿Es comprobable la pregunta «¿Cuántos °C baja un té de 60 °C en 10 minutos?»?", "Sí", "Se responde midiendo con un termómetro."),
            ex("¿Cuál es una predicción bien escrita: (a) «El té es rico» o (b) «Si el té está más caliente que la pieza, entonces perderá calor y bajará su temperatura»?", "(b)", "Usa una idea y se puede comprobar."),
        ],
        "apply": [
            arith("En la prueba del té, a los 10 minutos marcaba 45 °C y a los 20 minutos 35 °C. ¿Cuántos °C bajó en esos 10 minutos?", "45-35", "Se resta la temperatura final a la inicial.", " °C"),
            arith("A los 20 minutos marcaba 35 °C y a los 30 minutos 28 °C. ¿Cuántos °C bajó en esos 10 minutos?", "35-28", "Se resta la temperatura final a la inicial.", " °C"),
            ex("Con los tres descensos de 10 minutos (15 °C, 10 °C y 7 °C), ¿el té se enfría cada vez más rápido o cada vez más despacio?", "Cada vez más despacio", "Los descensos son cada vez menores."),
        ],
        "reason": [
            ex("Laura predijo que el té llegaría a 10 °C en una pieza de 20 °C. ¿Qué idea muestra que su predicción falla?", "El calor deja de fluir cuando se igualan las temperaturas, a 20 °C", "El té no puede bajar de la temperatura de la pieza solo por estar en ella."),
            ex("Un dato dice que un vaso a 5 °C llegó a 21 °C en una pieza de 21 °C. ¿La predicción «se iguala con la pieza» se cumplió?", "Sí", "Terminó con la misma temperatura que la pieza."),
        ],
        "challenge": [
            ex("Dos tazas iguales de té están a 60 °C. La taza A se deja en una pieza a 20 °C y la B en un refrigerador a 5 °C. ¿Cuál predices que se enfría más rápido?", "La B", "La diferencia de temperatura es mayor, así que el calor sale más rápido."),
            arith("Una taza baja de 90 °C a 50 °C en 20 minutos en una pieza a 20 °C. ¿Cuántos °C baja por cada 10 minutos si el descenso fuera igual en cada tramo?", "(90-50)//2", "Se reparte el descenso total en dos tramos de 10 minutos.", " °C"),
        ],
    },
    context=[ex("Una persona de tu casa saca una bebida del refrigerador a 5 °C y la deja en la mesa de una cocina a 25 °C. ¿Qué predicción puedes hacer sobre la temperatura de la bebida y hacia cuál valor se acerca?", "Subirá y se acercará a 25 °C", "El calor pasa del aire más caliente a la bebida más fría.")],
    selfcheck=[
        ex("¿En qué sentido pasa el calor?", "De lo más caliente a lo más frío", "Ese es el sentido natural."),
        ex("Si dos objetos tienen la misma temperatura, ¿el calor pasa de uno a otro?", "No", "El calor deja de fluir al igualarse."),
        ex("Un té marcó 31 °C y tu predicción decía 25 °C. ¿Qué número es la evidencia?", "31 °C", "Es el valor medido; la predicción se corrige."),
    ],
    open_task=task(
        "Usa los datos de una taza de té en una pieza a 20 °C: 0 min 60 °C, 10 min 45 °C, 20 min 35 °C, 30 min 28 °C. Escribe una pregunta comprobable, una predicción con «Si…, entonces…» para los 40 minutos (entre 20 °C y 28 °C) y explica en una frase por qué la temperatura no puede bajar de 20 °C.",
        "Pregunta: ¿cuántos °C baja el té entre los 30 y los 40 minutos? Predicción: si ya está a 28 °C, entonces bajará poco, quizá a 24 °C. No baja de 20 °C porque el calor deja de fluir cuando se iguala con la pieza.",
        ["pregunta comprobable", "predicción con «si» entre 20 °C y 28 °C", "explicación de por qué se detiene"],
        ["pregunta", "predicción", "explicación"],
        ["predecir menos de 20 °C", "no usar los datos"],
        "Pregunta cuánto subiría la temperatura del té si la pieza estuviera a 30 °C.",
    ),
    reinforce="Haz una predicción sobre un vaso de agua con hielo en una pieza caliente y di en qué sentido pasa el calor.",
    extend="Averigua con una persona de tu casa cuánto demora en enfriarse un plato de sopa y qué hacen para acelerarlo.",
)

# ================================================================ OA 14, clase 3
register(
    OA14, 3,
    materials="Papel y lápiz. Dibuja los esquemas con flechas.",
    use="Aprenderé un modelo del paso de calor entre dos objetos y qué le pasa a su temperatura. Sirve para explicar por qué se enfría una taza y se calienta el aire a su alrededor.",
    prior=["Sé que el calor pasa de lo más caliente a lo más frío.", "Conozco el modelo de partículas en movimiento."],
    explain=[
        "El modelo de partículas ayuda a explicar la diferencia entre calor y temperatura. La temperatura se relaciona con qué tan rápido, en promedio, se mueven las partículas de un objeto: más rápido, más caliente. El calor es la energía que pasa de las partículas rápidas de un objeto a las más lentas de otro cuando se tocan.",
        "Si juntas agua caliente y agua fría, las partículas rápidas chocan con las lentas y les pasan energía. El agua caliente se enfría y la fría se calienta, hasta que ambas tienen la misma temperatura. Se llama equilibrio térmico, y entonces el calor deja de pasar.",
        "Un modelo simple: si mezclas partes iguales de agua a 80 °C y a 20 °C, sin pérdidas, la temperatura final es la mitad entre ambas: 50 °C. El modelo tiene límites, porque en la realidad parte del calor se pierde al aire y al vaso, y las cantidades distintas de agua cambian el resultado.",
    ],
    vocab=[("equilibrio térmico", "situación en que dos objetos tienen igual temperatura y el calor deja de pasar"), ("partícula rápida", "partícula que se mueve con más energía"), ("transferencia", "paso de energía de un lugar a otro"), ("promedio", "valor intermedio entre varios datos"), ("pérdida de calor", "calor que se va al ambiente")],
    worked=[
        {"title": "Mezcla de partes iguales", "problem": "Se mezclan 200 mL de agua a 70 °C con 200 mL de agua a 30 °C, sin pérdidas de calor. ¿Cuál es la temperatura final?", "steps": ["Son partes iguales, así que el resultado es la mitad entre las dos temperaturas.", "Suma: 70 + 30 = 100.", "Mitad: 100 ÷ 2 = 50."], "answer": "50 °C"},
        {"title": "Explicar con partículas", "problem": "¿Por qué una cuchara caliente se enfría al meterla en agua fría?", "steps": ["Las partículas rápidas de la cuchara chocan con las lentas del agua.", "Le pasan energía: la cuchara baja su temperatura y el agua sube un poco."], "answer": "Porque las partículas rápidas transfieren energía a las lentas"},
    ],
    mistakes=[
        {"wrong": "Pensar que el frío pasa del hielo a la mano.", "why": "Se piensa que existe «frío» que se mueve.", "fix": "Lo que pasa es calor, de la mano al hielo."},
        {"wrong": "Esperar que la mezcla de agua caliente y fría quede más caliente que la más caliente.", "why": "No se entendió que ambas se acercan.", "fix": "La temperatura final queda entre las dos."},
    ],
    tiers={
        "recovery": [
            ex("En el modelo de partículas, ¿un objeto más caliente tiene partículas que se mueven más rápido o más lento?", "Más rápido", "Más temperatura se relaciona con más rapidez."),
            ex("Cuando dos objetos llegan a la misma temperatura, ¿el calor sigue pasando?", "No", "Hay equilibrio térmico."),
            ex("Una cuchara a 80 °C se pone en agua a 20 °C. ¿La cuchara gana o pierde calor?", "Pierde calor", "Pasa calor a la más fría."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué significa equilibrio térmico?", "Que dos objetos tienen igual temperatura y el calor deja de pasar", "La temperatura se iguala."),
            ex("Con partículas, ¿qué explica que el agua fría se caliente al mezclarla con agua caliente?", "Las partículas rápidas pasan energía a las lentas", "La energía se transfiere en los choques."),
            ex("¿Cuál es una limitación del modelo de mezcla: que supone que no se pierde calor al aire o que mezcla agua?", "Que supone que no se pierde calor al aire", "En la realidad parte del calor se escapa."),
        ],
        "apply": [
            arith("Se mezclan partes iguales de agua a 90 °C y a 30 °C, sin pérdidas. ¿Cuál es la temperatura final? Calcula la mitad entre ambas.", "(90+30)//2", "Con cantidades iguales, la temperatura final es el promedio.", " °C"),
            arith("Se mezclan partes iguales de agua a 64 °C y a 16 °C. ¿Cuál es la temperatura final?", "(64+16)//2", "Se suma y se divide por dos.", " °C"),
            ex("Una taza a 60 °C y un vaso a 20 °C, con la misma cantidad de agua, se dejan juntos dentro de una caja aislada. Después de un largo tiempo, ambos están a 40 °C. ¿Qué nombre tiene esa situación?", "Equilibrio térmico", "Los dos tienen igual temperatura."),
        ],
        "reason": [
            ex("Sofía dice que al mezclar agua a 70 °C y a 30 °C, de partes iguales, la mezcla quedará a 90 °C. ¿Qué dato muestra que se equivoca?", "La temperatura final debe quedar entre 30 °C y 70 °C", "La mezcla no puede quedar más caliente que la más caliente."),
            ex("En una mezcla real, el resultado es 48 °C en lugar de 50 °C. ¿Qué pérdida del modelo explica la diferencia?", "El calor que se fue al aire y al vaso", "El modelo ideal no considera esas pérdidas."),
        ],
        "challenge": [
            ex("Un cubo de hielo a 0 °C se pone en la mano a 33 °C. Con partículas, ¿qué pasa con la energía: pasa de la mano al hielo o del hielo a la mano?", "De la mano al hielo", "La mano está más caliente."),
            arith("Se mezclan 150 mL de agua a 24 °C con 150 mL de agua a 76 °C, sin pérdidas de calor. ¿A cuántos °C queda la mezcla?", "(24+76)//2", "Con partes iguales, es el promedio de las dos temperaturas.", " °C"),
        ],
    },
    context=[ex("Al preparar un té, una persona agrega agua fría para que no queme. ¿Qué pasa con la temperatura de la mezcla respecto al agua caliente y al agua fría?", "Queda entre las dos", "La temperatura se iguala en un valor intermedio.")],
    selfcheck=[
        ex("En el modelo, ¿qué pasa con la energía de las partículas rápidas al chocar con las lentas?", "Pasa a las lentas", "Así se transfiere el calor."),
        ex("¿Qué es el equilibrio térmico?", "Igual temperatura y sin paso de calor", "Es el final del traspaso."),
        ex("¿El modelo de la mezcla considera pérdidas de calor?", "No", "Por eso es una limitación."),
    ],
    open_task=task(
        "Dibuja dos cajas: una con agua a 90 °C y otra con agua a 30 °C, de igual cantidad. Dibuja partículas rápidas (flechas largas) en la primera y lentas (flechas cortas) en la segunda. Dibuja una flecha de calor de la primera a la segunda. Calcula la temperatura final de la mezcla y escribe una limitación del modelo.",
        "Flecha de calor del agua a 90 °C hacia el agua a 30 °C. Temperatura final: 60 °C. Limitación: el modelo no incluye el calor que se pierde al aire.",
        ["dos cajas con partículas rápidas y lentas", "flecha de calor en el sentido correcto", "60 °C calculado y una limitación"],
        ["dibujo", "cálculo", "limitación"],
        ["flecha en sentido contrario", "olvidar la limitación"],
        "Pregunta qué cambiaría en el dibujo si el agua caliente fuera el doble de cantidad.",
    ),
    reinforce="Dibuja cómo cambian las partículas de una cuchara caliente cuando se mete en agua fría.",
    extend="Averigua con una persona de tu casa qué pasa con la temperatura de una sopa al agregarle agua fría y relaciónalo con el equilibrio térmico.",
)

# ================================================================ OA 14, clase 4
register(
    OA14, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a comparar con un criterio dos casos con la misma temperatura pero distinta cantidad de calor. Sirve para entender por qué temperatura y calor no son lo mismo.",
    prior=["Sé que el calor es energía que pasa de lo caliente a lo frío.", "Sé que la temperatura se mide en °C."],
    explain=[
        "Dos recipientes pueden tener la misma temperatura y no tener la misma cantidad de calor para entregar. Un balde con 1.000 mL de agua a 50 °C tiene más energía que una taza con 200 mL de agua a 50 °C, porque tiene más partículas moviéndose. La temperatura es igual: 50 °C.",
        "¿Cómo se comparan? Con un criterio que no sea la temperatura. Un criterio posible es cuánto hielo se derrite, porque derretir hielo exige calor. En datos de ejemplo, la taza de 200 mL derrite 120 g de hielo y el balde de 1.000 mL derrite 600 g. El balde entregó más calor.",
        "También se puede variar la temperatura y mantener el volumen. Dos tazas de 200 mL, una a 80 °C y otra a 40 °C, derriten 200 g y 100 g. La de 80 °C entregó más calor. Por eso se dice que la temperatura mide lo caliente, mientras que el calor depende de la temperatura y de la cantidad. Los datos son de ejemplo y se necesitarían muchas pruebas para estar seguros.",
    ],
    vocab=[("cantidad de calor", "energía que un objeto puede entregar"), ("criterio", "regla para comparar"), ("derretir", "pasar de sólido a líquido"), ("variable", "condición que cambia en una prueba"), ("datos de ejemplo", "datos inventados para practicar, no medidos")],
    worked=[
        {"title": "Comparar con el hielo derretido", "problem": "La taza de 200 mL derrite 120 g de hielo y el balde de 1.000 mL derrite 600 g, ambos a 50 °C. ¿Cuántos gramos más derrite el balde?", "steps": ["Los dos datos están en gramos.", "Resto: 600 − 120 = 480."], "answer": "480 g más"},
        {"title": "Misma temperatura, distinto calor", "problem": "Un balde y una taza están a 50 °C. ¿Tienen la misma temperatura? ¿Entregan la misma cantidad de calor?", "steps": ["El termómetro marca lo mismo en ambos: igual temperatura.", "El balde tiene más agua, y entrega más calor."], "answer": "Igual temperatura, pero el balde entrega más calor"},
    ],
    mistakes=[
        {"wrong": "Decir que si la temperatura es la misma, el calor también es el mismo.", "why": "Se confunden los dos conceptos.", "fix": "El calor depende de la temperatura y de la cantidad."},
        {"wrong": "Comparar solo la temperatura para saber cuánto hielo derretirá algo.", "why": "No se considera la cantidad de agua.", "fix": "Compara el hielo derretido o el calor entregado."},
    ],
    tiers={
        "recovery": [
            ex("Una taza y un balde de agua marcan 50 °C. ¿Tienen igual o distinta temperatura?", "Igual", "El termómetro marca lo mismo."),
            ex("Entre un balde con 1.000 mL de agua a 50 °C y una taza con 200 mL a 50 °C, ¿cuál entrega más calor?", "El balde", "Tiene más agua y más partículas con energía."),
            ex("¿Cuál criterio es mejor para comparar el calor entregado: el hielo derretido o el color del recipiente?", "El hielo derretido", "El calor derrite hielo; el color no mide calor."),
        ],
        "understand": [
            ex("En Ciencias, ¿de qué dos cosas depende la cantidad de calor de un objeto?", "De su temperatura y de su cantidad de materia", "No depende solo de la temperatura."),
            ex("Dos tazas de 200 mL, una a 80 °C y otra a 40 °C. ¿Cuál tiene más calor para entregar?", "La de 80 °C", "A igual cantidad, mayor temperatura entrega más calor."),
            ex("¿Qué es una limitación de datos de ejemplo?", "Que no son mediciones reales y no prueban nada", "Sirven para practicar, no para concluir."),
        ],
        "apply": [
            arith("Dos tazas iguales derriten hielo: la caliente 180 g y la tibia 90 g. ¿Cuántos gramos más derrite la caliente?", "180-90", "Se resta el menor al mayor.", " g"),
            arith("Un balde derrite 400 g de hielo y una taza derrite 100 g. ¿Cuántas veces más hielo derrite el balde?", "400//100", "Se divide el mayor por el menor.", " veces"),
            arith("Cuatro tazas iguales derriten 120 g cada una. ¿Cuántos gramos derriten en total?", "4*120", "Se multiplican las tazas por los gramos.", " g"),
        ],
        "reason": [
            ex("Beto dice: «El balde y la taza están a 50 °C, así que tienen la misma cantidad de calor». ¿Qué dato de la clase contradice a Beto?", "El balde derritió 600 g y la taza solo 120 g", "Igual temperatura no significa igual calor."),
            ex("Camila compara dos tazas iguales: una de 80 °C y otra de 40 °C. Dice que la de 80 °C tiene más temperatura y más calor. ¿Tiene razón?", "Sí", "A igual cantidad, más temperatura implica más calor."),
        ],
        "challenge": [
            ex("Un compañero propone medir el calor con el tiempo que demora en enfriarse. Si los dos parten de la misma temperatura y el balde demora más que la taza en enfriarse, ¿qué indica?", "Que el balde tiene más calor para perder", "Tarda más porque tiene más energía que entregar."),
            arith("Una prueba dio 118 g, otra 122 g y otra 120 g de hielo derretido con la misma taza. ¿Cuál es el promedio? Suma y divide por 3.", "(118+122+120)//3", "El promedio resume pruebas repetidas.", " g"),
        ],
    },
    context=[ex("Una persona de tu casa quiere calentar una pieza con una olla grande de agua a 60 °C o con una taza de agua a 60 °C. ¿Cuál entregaría más calor a la pieza y por qué?", "La olla grande, porque tiene más agua a la misma temperatura", "A igual temperatura, la mayor cantidad entrega más calor.")],
    selfcheck=[
        ex("¿La misma temperatura implica la misma cantidad de calor?", "No", "También depende de la cantidad."),
        ex("¿Qué criterio usamos en esta clase para comparar calor entregado?", "El hielo derretido", "Derretir hielo exige calor."),
        ex("Entre dos tazas iguales, ¿cuál tiene más calor: la más caliente o la más fría?", "La más caliente", "Tiene partículas más energéticas."),
    ],
    open_task=task(
        "Con estos datos de ejemplo escribe una conclusión: Taza A, 200 mL a 80 °C, derritió 200 g de hielo. Taza B, 200 mL a 40 °C, derritió 100 g. Balde C, 1.000 mL a 40 °C, derritió 500 g. Compara A con B (misma cantidad) y B con C (misma temperatura) y di qué factor influye en el calor.",
        "A y B tienen igual cantidad y A derritió 100 g más porque estaba a mayor temperatura. B y C tienen igual temperatura y C derritió 400 g más porque tiene más agua. El calor depende de la temperatura y de la cantidad.",
        ["dos comparaciones con datos", "diferencias calculadas", "conclusión sobre temperatura y cantidad"],
        ["dos comparaciones escritas"],
        ["comparar pruebas donde cambian dos cosas", "calcular mal las diferencias"],
        "Pregunta qué cambiaría si los datos fueran medidos y no de ejemplo.",
    ),
    reinforce="Explica con tus palabras por qué un balde de agua a 50 °C derrite más hielo que una taza a 50 °C.",
    extend="Averigua con una persona de tu casa por qué una olla grande con agua caliente tarda más en enfriarse que una taza.",
)

# ================================================================ OA 15, clase 1
register(
    OA15, 1,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno; son datos de ejemplo. El agua que se calienta siempre debe manejarla una persona adulta.",
    use="Aprenderé a leer una tabla de temperaturas del agua al calentarla y a separar lo que muestran los datos de lo que explico. Sirve para interpretar mediciones.",
    prior=["Sé que la temperatura se mide con un termómetro en °C.", "Sé nombrar los cambios de estado."],
    explain=[
        "Se puede estudiar el agua midiendo su temperatura cada cierto tiempo mientras se calienta. Los datos de esta clase son de ejemplo (no medidos por ti): minuto 0, 20 °C; minuto 2, 36 °C; minuto 4, 52 °C; minuto 6, 68 °C; minuto 8, 84 °C; minuto 10, 100 °C; minuto 12, 100 °C; minuto 14, 100 °C.",
        "Observaciones que salen directo de la tabla: la temperatura sube 16 °C cada 2 minutos hasta el minuto 10; después se mantiene en 100 °C en los minutos 10, 12 y 14. Interpretaciones son las explicaciones que agregamos, por ejemplo «el agua está hirviendo» o «el calor ya no sirve para subir la temperatura».",
        "Una buena práctica es escribir primero lo que dice la tabla y marcar con claridad lo que es una explicación. Un solo conjunto de datos de ejemplo no prueba nada sobre el agua real, pero sirve para practicar a leer una tabla de mediciones.",
    ],
    vocab=[("tabla de datos", "orden de datos en filas y columnas"), ("temperatura", "medida de lo caliente que está algo"), ("intervalo", "tiempo entre dos mediciones"), ("meseta", "parte de la tabla donde el dato no cambia"), ("datos de ejemplo", "datos inventados para practicar")],
    worked=[
        {"title": "Leer un cambio", "problem": "En la tabla, ¿cuántos °C subió la temperatura entre el minuto 4 (52 °C) y el minuto 8 (84 °C)?", "steps": ["Se usan los dos datos de la tabla.", "Resto: 84 − 52 = 32."], "answer": "32 °C"},
        {"title": "Observación o interpretación", "problem": "Frase A: «Del minuto 10 al 14 la temperatura marcó 100 °C». Frase B: «El agua hierve porque tiene mucha energía». ¿Cuál es la observación?", "steps": ["La frase A está escrita en la tabla.", "La frase B explica una causa que la tabla no muestra."], "answer": "La frase A es observación; la B es una interpretación"},
    ],
    mistakes=[
        {"wrong": "Decir que la tabla prueba cuándo hierve cualquier agua.", "why": "Se generaliza desde datos de ejemplo.", "fix": "Di que son datos de ejemplo y que se necesitaría medir."},
        {"wrong": "Mezclar la causa con el dato: «subió porque el agua tiene ganas de hervir».", "why": "Se agregan explicaciones sin evidencia.", "fix": "Primero el dato (de 20 °C a 36 °C); la causa se escribe aparte."},
    ],
    tiers={
        "recovery": [
            ex("En la tabla de ejemplo, ¿cuál es la temperatura en el minuto 6?", "68 °C", "Se lee directo de la tabla."),
            ex("En la tabla de ejemplo, ¿cuál es la temperatura en el minuto 0?", "20 °C", "Se lee directo de la tabla."),
            ex("En la tabla de ejemplo, ¿qué temperatura marca en el minuto 12?", "100 °C", "Se lee directo de la tabla."),
        ],
        "understand": [
            ex("Frase: «Entre el minuto 0 y el minuto 2 la temperatura subió de 20 °C a 36 °C». ¿Observación o interpretación?", "Observación", "Es un dato de la tabla."),
            ex("Frase: «Después del minuto 10 el agua deja de calentarse porque está hirviendo». ¿Observación o interpretación?", "Interpretación", "La causa «porque está hirviendo» no está en la tabla."),
            ex("¿Qué es una meseta en la tabla: una parte donde el dato cambia mucho o una parte donde se mantiene igual?", "Una parte donde se mantiene igual", "Aquí, la temperatura se mantiene en 100 °C."),
        ],
        "apply": [
            arith("¿Cuántos °C subió la temperatura entre el minuto 0 (20 °C) y el minuto 6 (68 °C)?", "68-20", "Se resta el dato inicial al final.", " °C"),
            arith("La temperatura subió 16 °C cada 2 minutos desde el minuto 0. ¿Cuántos °C subió en total en 5 intervalos de 2 minutos?", "5*16", "Se multiplica el aumento por intervalo por el número de intervalos.", " °C"),
            ex("Con la tabla de ejemplo, ¿en cuántos registros la temperatura marca 100 °C?", "3", "Son los registros de los minutos 10, 12 y 14."),
        ],
        "reason": [
            ex("Ema dice: «La tabla prueba que el agua siempre hierve a los 10 minutos». ¿Qué le falta considerar?", "Que son datos de ejemplo y que dependen de la cantidad de agua y del calor", "Una tabla de ejemplo no prueba nada general."),
            ex("Luis escribió: «A los 8 minutos marcaba 94 °C». ¿Qué dato de la tabla lo contradice?", "A los 8 minutos marcaba 84 °C", "Se compara con el dato original."),
        ],
        "challenge": [
            ex("Hay dos conjuntos: A (20, 36, 52 °C) y B (20, 28, 36 °C), en los mismos minutos 0, 2 y 4. ¿Cuál se calentó más rápido en esos 4 minutos?", "A", "Subió 32 °C, frente a 16 °C en B."),
            arith("Se hacen tres lecturas del mismo momento: 99 °C, 100 °C y 101 °C. ¿Cuántos grados abarca el rango (mayor menos menor)?", "101-99", "El rango muestra cuánto varían las lecturas.", " °C"),
        ],
    },
    context=[ex("Una persona de tu casa calienta agua en una tetera y ve que el termómetro de cocina deja de subir cuando el agua hierve. ¿Qué parte de esa frase es la observación?", "Que el termómetro deja de subir", "La explicación de por qué no se observa directamente.")],
    selfcheck=[
        ex("En la tabla de ejemplo, ¿cuál es el dato del minuto 4?", "52 °C", "Se lee directo."),
        ex("Una interpretación, ¿está en la tabla o la agregamos nosotros?", "La agregamos nosotros", "La tabla solo tiene datos."),
        ex("¿Los datos de ejemplo prueban cómo se comporta el agua real?", "No", "Sirven para practicar."),
    ],
    open_task=task(
        "Copia la tabla de ejemplo (minutos 0 a 14: 20, 36, 52, 68, 84, 100, 100, 100 °C, de 2 en 2 minutos). Escribe tres observaciones y una interpretación. Marca con O las observaciones y con I la interpretación, y agrega una frase que diga por qué son datos de ejemplo.",
        "O: en el minuto 6 marca 68 °C. O: sube 16 °C cada 2 minutos hasta los 100 °C. O: después de 10 minutos se mantiene en 100 °C. I: el agua está hirviendo. Son datos de ejemplo porque nadie los midió.",
        ["tres observaciones de la tabla", "una interpretación marcada", "aclara que son datos de ejemplo"],
        ["tabla copiada", "frases rotuladas"],
        ["escribir una explicación como observación", "no aclarar que son datos de ejemplo"],
        "Pregunta cuál de tus frases cambiaría si la medición fuera real.",
    ),
    reinforce="Escribe otras tres observaciones de la tabla usando los minutos 2, 8 y 14.",
    extend="Averigua con una persona de tu casa qué instrumento usan para medir la temperatura de los alimentos y cómo se lee.",
)

# ================================================================ OA 15, clase 2
register(
    OA15, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno. Todo calentamiento de agua lo hace una persona adulta.",
    use="Aprenderé a hacer preguntas y predicciones sobre cómo cambia la temperatura del agua al calentarla y al enfriarla. Sirve para anticipar resultados antes de medir.",
    prior=["Sé leer la tabla del agua que se calienta.", "Sé que una predicción usa «Si…, entonces…»."],
    explain=[
        "Una pregunta comprobable puede ser: «¿qué temperatura marcará el agua en el minuto 12 si sigo calentando con la misma llama?». Para predecir usamos el patrón de los datos: en la tabla de ejemplo, la temperatura sube 16 °C cada 2 minutos mientras es agua líquida: 20, 36, 52, 68, 84, 100.",
        "Una predicción con el patrón: «Si sigo el patrón, entonces a los 12 minutos marcará 116 °C». Pero la tabla dice 100 °C. La predicción falla porque el agua hierve y no pasa de 100 °C cuando hierve a esa presión. Se corrige la predicción: mientras el agua hierve, su temperatura se mantiene.",
        "Al enfriar agua en un congelador pasa algo parecido. Datos de ejemplo: minuto 0, 20 °C; minuto 10, 10 °C; minuto 20, 2 °C; minuto 30, 0 °C; minuto 40, 0 °C; minuto 50, 0 °C. Mientras se hace hielo, la temperatura se queda en 0 °C. Predecimos con «si»: si el agua se está solidificando, entonces su temperatura se mantendrá en 0 °C.",
    ],
    vocab=[("patrón", "regularidad que se repite en los datos"), ("predicción", "resultado esperado apoyado en datos"), ("hervir", "pasar de líquido a gas con burbujas en todo el líquido"), ("congelar", "pasar de líquido a sólido enfriando"), ("presión", "fuerza del aire sobre una superficie; aquí, lo que influye en cuándo hierve el agua")],
    worked=[
        {"title": "Predecir con un patrón", "problem": "El agua sube 16 °C cada 2 minutos. Si a los 4 minutos marca 52 °C, ¿cuánto predices a los 6 minutos?", "steps": ["Cada 2 minutos suma 16 °C.", "52 + 16 = 68."], "answer": "68 °C"},
        {"title": "Predecir en una meseta", "problem": "Si el agua ya marca 100 °C y sigue hirviendo, ¿qué temperatura predices dos minutos después?", "steps": ["Durante la ebullición la temperatura se mantiene.", "Por eso sigue en 100 °C."], "answer": "100 °C"},
    ],
    mistakes=[
        {"wrong": "Seguir sumando 16 °C aunque el agua ya esté hirviendo.", "why": "Se aplica un patrón donde ya no vale.", "fix": "Revisa si cambió el estado: al hervir, la temperatura se mantiene."},
        {"wrong": "Predecir que el agua al congelarse baja de 0 °C de inmediato.", "why": "Se olvida la meseta.", "fix": "Mientras se solidifica, la temperatura se mantiene en 0 °C."},
    ],
    tiers={
        "recovery": [
            ex("Si el agua sube 16 °C cada 2 minutos y marca 36 °C, ¿cuánto marcará 2 minutos después?", "52 °C", "36 más 16 son 52."),
            ex("Mientras el agua hierve, ¿su temperatura sigue subiendo o se mantiene?", "Se mantiene", "La energía se usa en cambiar de estado."),
            ex("Mientras el agua se hace hielo, ¿qué temperatura se mantiene?", "0 °C", "La meseta del congelamiento está en 0 °C."),
        ],
        "understand": [
            ex("¿Es comprobable la pregunta «¿cuántos °C sube el agua en 2 minutos?»?", "Sí", "Se responde con un termómetro y un reloj."),
            ex("¿Cuál es una predicción bien escrita: (a) «El agua es bonita cuando hierve» o (b) «Si el agua ya hierve, entonces su temperatura se mantendrá»?", "(b)", "Se apoya en la meseta de los datos."),
            ex("Si el dato contradice la predicción, ¿cuál se corrige?", "La predicción", "El dato es la evidencia."),
        ],
        "apply": [
            arith("Con el patrón de 16 °C cada 2 minutos desde 20 °C, ¿qué temperatura predices en el minuto 8?", "20+4*16", "Hay 4 intervalos de 2 minutos hasta el minuto 8.", " °C"),
            arith("Un agua sube 8 °C por minuto desde 20 °C. ¿Qué temperatura predices a los 5 minutos?", "20+5*8", "Se suma el aumento total al valor inicial.", " °C"),
            ex("Una bandeja con agua se deja en el congelador y, después de un rato, ya se está haciendo hielo. ¿Qué temperatura predices mientras se solidifica?", "0 °C", "La temperatura se mantiene durante el cambio de estado."),
        ],
        "reason": [
            ex("Jaime predijo 116 °C en el minuto 12 y la tabla marca 100 °C. ¿Qué debe cambiar: la predicción o la tabla?", "La predicción", "La tabla es la evidencia."),
            ex("Con datos de ejemplo, el agua baja 10 °C en los primeros 10 minutos y 8 °C en los siguientes 10. ¿Se enfría más rápido al principio o después?", "Al principio", "Primero baja más."),
        ],
        "challenge": [
            ex("Una amiga dice: «Si el agua sigue en el congelador, a los 60 minutos habrá bajado a -5 °C». ¿Qué debe ocurrir antes para que sea posible?", "Que toda el agua se haya vuelto hielo", "La temperatura baja de 0 °C cuando ya no hay líquido."),
            arith("En el congelador, el agua marcó 20 °C al inicio y 10 °C a los 10 minutos. Si siguiera bajando parejo, 10 °C cada 10 minutos, ¿cuánto marcaría a los 30 minutos?", "20-3*10", "Tres tramos de 10 minutos bajan 30 °C desde 20 °C. Esa predicción no se cumple porque el agua llega a 0 °C y se congela.", " °C"),
        ],
    },
    context=[ex("Una persona de tu casa calienta agua para un té y ve que el termómetro marca 100 °C. Si deja la olla 5 minutos más con la misma llama, ¿qué predices que marcará?", "100 °C", "Mientras hierve, la temperatura se mantiene.")],
    selfcheck=[
        ex("¿Qué temperatura se mantiene mientras el agua se solidifica?", "0 °C", "Es la meseta del congelamiento."),
        ex("¿Qué se corrige cuando el dato contradice la predicción?", "La predicción", "Los datos son la evidencia."),
        ex("Un patrón, ¿es una regularidad que se repite?", "Sí", "Con él se puede predecir."),
    ],
    open_task=task(
        "Usa la tabla de calentamiento (20, 36, 52, 68, 84, 100 °C cada 2 minutos, y luego 100 °C) y la de enfriamiento (20, 10, 2, 0, 0, 0 °C cada 10 minutos). Escribe dos preguntas comprobables y dos predicciones con «Si…, entonces…», una para cada tabla. Revisa cada predicción con la tabla.",
        "Pregunta: ¿cuánto marcará a los 12 minutos? Predicción: si el agua ya hierve, entonces seguirá en 100 °C. Se cumple. Pregunta: ¿cuánto marcará el agua a los 40 minutos? Predicción: si se está congelando, entonces marcará 0 °C. Se cumple.",
        ["dos preguntas comprobables", "dos predicciones con «si»", "revisión con la tabla"],
        ["preguntas", "predicciones", "revisión"],
        ["predecir sin usar la meseta", "no revisar la predicción"],
        "Pregunta qué haría con una predicción que no coincidió con la tabla.",
    ),
    reinforce="Escribe una predicción para el minuto 14 de la tabla de calentamiento y revísala.",
    extend="Averigua con una persona de tu casa cuánto demora en hervir agua en una tetera y compara con los datos de ejemplo.",
)

# ================================================================ OA 15, clase 3
register(
    OA15, 3,
    materials="Papel y lápiz; papel cuadriculado si tienes. Los datos están escritos en el cuaderno.",
    use="Aprenderé a modelar el calentamiento y enfriamiento del agua con un gráfico de líneas y con partículas. Sirve para ver dónde cambia de estado el agua.",
    prior=["Sé leer la tabla de calentamiento del agua.", "Conozco el modelo de partículas y los cambios de estado."],
    explain=[
        "Un gráfico de líneas es un modelo que muestra cómo cambia la temperatura con el tiempo. Se dibuja el tiempo en el eje horizontal y la temperatura en el vertical. Con los datos de ejemplo (0 min 20 °C; 10 min 100 °C; 14 min 100 °C), la línea sube hasta 100 °C y luego queda horizontal.",
        "Cada parte de la línea tiene una explicación con partículas. En la parte que sube, el agua es líquida y las partículas se mueven cada vez más rápido: la temperatura sube. En la parte horizontal, el agua hierve: la energía se usa en separar las partículas para que pasen a gas, y la temperatura no cambia. Si hay mezcla de agua líquida y vapor, hay dos estados a la vez.",
        "Con el hielo pasa algo parecido: durante la fusión (hielo que se derrite) la temperatura se mantiene en 0 °C, mientras hay hielo y agua líquida juntos. El gráfico es un modelo, así que tiene límites: no muestra las partículas ni cuánta agua hay, y los puntos se unen con una línea aunque no se midió entre uno y otro.",
    ],
    vocab=[("gráfico de líneas", "dibujo que une puntos de datos para ver cómo cambia algo en el tiempo"), ("eje", "línea del gráfico donde se escriben los valores"), ("tramo horizontal", "parte del gráfico donde el dato no cambia"), ("ebullición", "paso de líquido a gas con burbujas en todo el líquido"), ("fusión", "paso de sólido a líquido")],
    worked=[
        {"title": "Leer el gráfico", "problem": "En el gráfico, la línea sube de 20 °C (0 min) a 100 °C (10 min) y luego queda horizontal hasta los 14 min. ¿Qué pasa con el agua en el tramo horizontal?", "steps": ["Un tramo horizontal significa que la temperatura no cambia.", "A 100 °C, el agua hierve."], "answer": "El agua hierve y su temperatura se mantiene en 100 °C"},
        {"title": "Explicar con partículas", "problem": "¿Qué hace la energía que recibe el agua durante la ebullición?", "steps": ["La energía separa las partículas para pasar de líquido a gas.", "Por eso la temperatura no sube."], "answer": "Separa las partículas para formar vapor"},
    ],
    mistakes=[
        {"wrong": "Pensar que el tramo horizontal significa que no pasa nada.", "why": "Se mira solo la temperatura.", "fix": "Ahí ocurre un cambio de estado."},
        {"wrong": "Creer que el gráfico muestra lo que pasa entre los puntos medidos.", "why": "La línea une puntos, pero no se midió entre ellos.", "fix": "Di que es un modelo con límites."},
    ],
    tiers={
        "recovery": [
            ex("En un gráfico de calentamiento, ¿qué eje muestra la temperatura: el horizontal o el vertical?", "El vertical", "El eje horizontal es el tiempo."),
            ex("¿Una línea que sube significa que la temperatura aumenta o se mantiene?", "Aumenta", "Cada punto es mayor que el anterior."),
            ex("¿Un tramo horizontal significa que la temperatura aumenta o se mantiene?", "Se mantiene", "El valor no cambia."),
        ],
        "understand": [
            ex("Durante la ebullición, ¿qué hace la energía que recibe el agua: subir la temperatura o separar las partículas?", "Separar las partículas", "Pasa de líquido a gas."),
            ex("Durante la fusión del hielo, ¿qué temperatura se mantiene?", "0 °C", "La meseta de la fusión está en 0 °C."),
            ex("¿Cuál es una limitación del gráfico: que muestra el tiempo o que une puntos sin medir lo que ocurrió entre ellos?", "Que une puntos sin medir lo que ocurrió entre ellos", "La línea es una suposición entre mediciones."),
        ],
        "apply": [
            ex("Hielo a -6 °C marca -2 °C a los 5 minutos, 0 °C a los 10, 0 °C a los 15, 0 °C a los 20 y 3 °C a los 25. ¿Entre qué minutos hay un tramo horizontal?", "Entre los minutos 10 y 20", "Marca 0 °C en esos tres registros."),
            arith("En ese registro, ¿cuántos minutos dura el tramo horizontal si va del minuto 10 al minuto 20?", "20-10", "Se resta el tiempo inicial al final.", " minutos"),
            ex("En ese registro, ¿qué estados hay juntos en el tramo de 0 °C?", "Sólido y líquido", "El hielo y el agua conviven mientras se derrite."),
        ],
        "reason": [
            ex("Un compañero dice que la temperatura no sube en el tramo horizontal porque el fuego «se apagó». ¿Qué explicación con partículas lo contradice?", "La energía se usa en separar partículas, aunque el fuego siga", "Siguen recibiendo energía, pero se usa en el cambio de estado."),
            ex("Dos gráficos tienen el mismo tramo de 100 °C, pero A dura 4 minutos y B dura 8 minutos. ¿En cuál había más agua para hervir si se calentó igual?", "En B", "Con más agua el cambio de estado dura más."),
        ],
        "challenge": [
            arith("El tramo sube de 20 °C a 100 °C en 10 minutos. ¿Cuántos °C sube por minuto en promedio?", "(100-20)//10", "Se divide el aumento total por los minutos.", " °C por minuto"),
            ex("Un gráfico de enfriamiento baja de 20 °C a 0 °C, se mantiene en 0 °C durante 20 minutos y luego baja de nuevo. ¿Qué estado tiene el agua en el tramo plano?", "Hay líquido y sólido juntos (se está solidificando)", "En el tramo de 0 °C el agua se está haciendo hielo."),
        ],
    },
    context=[ex("Al hervir agua en una olla, la persona de tu casa dice que subir el fuego no hace que el agua pase de 100 °C. ¿Qué parte del gráfico representa esa observación?", "El tramo horizontal", "La temperatura se mantiene mientras hierve.")],
    selfcheck=[
        ex("¿Qué eje del gráfico muestra el tiempo?", "El horizontal", "Es la convención."),
        ex("En el tramo horizontal de la ebullición, ¿qué temperatura se mantiene?", "100 °C", "Es el dato del ejemplo."),
        ex("¿Un gráfico es una copia exacta de lo que pasa?", "No", "Es un modelo con límites."),
    ],
    open_task=task(
        "Con papel cuadriculado o con una hoja, dibuja un gráfico: tiempo en el eje horizontal (0, 2, 4, 6, 8, 10, 12, 14 minutos) y temperatura en el eje vertical (20 a 100 °C). Marca los puntos 20, 36, 52, 68, 84, 100, 100, 100 °C y únelos. Rotula el tramo que sube («agua líquida se calienta») y el tramo horizontal («ebullición») y escribe una limitación del gráfico.",
        "La línea sube de 20 a 100 °C y luego queda horizontal. Tramo que sube: agua líquida se calienta. Tramo horizontal: ebullición. Limitación: la línea une puntos y no sabemos qué pasó entre las mediciones.",
        ["ejes con unidades", "puntos bien ubicados", "tramos rotulados y una limitación"],
        ["gráfico", "rótulos"],
        ["ubicar el tiempo en el eje vertical", "no rotular el tramo horizontal"],
        "Pregunta qué cambiaría en el gráfico si se midiera cada minuto.",
    ),
    reinforce="Dibuja el gráfico de enfriamiento 20, 10, 2, 0, 0, 0 °C cada 10 minutos y rotula el tramo en 0 °C.",
    extend="Averigua con una persona de tu casa qué otra cosa de la cocina muestra un cambio de estado con temperatura constante.",
)

# ================================================================ OA 15, clase 4
register(
    OA15, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a comparar con un criterio dos calentamientos del agua con distinta cantidad. Sirve para decidir qué cambia el tiempo que se demora en llegar a una temperatura.",
    prior=["Sé leer una tabla de calentamiento.", "Sé qué es una prueba justa."],
    explain=[
        "Para comparar dos calentamientos usamos un criterio: cuántos °C sube la temperatura por minuto, que llamamos rapidez de calentamiento. Se calcula dividiendo el aumento de temperatura por los minutos. Es justo comparar solo si la fuente de calor y el recipiente son iguales y únicamente cambia la cantidad de agua.",
        "Datos de ejemplo. Prueba A: 100 mL de agua pasan de 20 °C a 100 °C en 10 minutos. Prueba B: 200 mL de agua, con la misma fuente de calor, pasan de 20 °C a 100 °C en 20 minutos. En A sube 8 °C por minuto: 80 ÷ 10. En B sube 4 °C por minuto: 80 ÷ 20.",
        "Conclusión con evidencia: con el doble de agua, el calentamiento fue la mitad de rápido. Una limitación: se hizo una sola prueba con cada cantidad y el termómetro tiene un error de alrededor de 1 °C. Para estar más seguros habría que repetir las pruebas.",
    ],
    vocab=[("rapidez de calentamiento", "°C que sube la temperatura por cada minuto"), ("criterio", "regla para comparar"), ("fuente de calor", "lo que entrega el calor"), ("prueba justa", "prueba en que cambia solo una condición"), ("repetir", "hacer otra vez la prueba")],
    worked=[
        {"title": "Calcular la rapidez", "problem": "Prueba A: 100 mL pasan de 20 °C a 100 °C en 10 minutos. ¿Cuántos °C sube por minuto?", "steps": ["Aumento: 100 − 20 = 80 °C.", "Rapidez: 80 ÷ 10 = 8."], "answer": "8 °C por minuto"},
        {"title": "Comparar con el criterio", "problem": "La prueba A sube 8 °C por minuto y la B sube 4 °C por minuto. ¿Cuál se calienta más rápido?", "steps": ["Se comparan los °C por minuto.", "8 es mayor que 4."], "answer": "La prueba A"},
    ],
    mistakes=[
        {"wrong": "Comparar el aumento de temperatura sin considerar el tiempo.", "why": "No se usó el criterio de °C por minuto.", "fix": "Divide el aumento por los minutos."},
        {"wrong": "Comparar dos pruebas con distinta cantidad de agua y distinta fuente de calor.", "why": "No es una prueba justa.", "fix": "Cambia una sola condición."},
    ],
    tiers={
        "recovery": [
            ex("Una prueba sube 6 °C por minuto y otra 3 °C por minuto. ¿Cuál se calienta más rápido?", "La que sube 6 °C por minuto", "6 es mayor que 3."),
            ex("Para comparar justo dos calentamientos, ¿cuántas condiciones deben cambiar?", "Una", "Así se sabe qué causó la diferencia."),
            ex("¿Cuál es el criterio que usamos en la clase para comparar calentamientos: °C por minuto o color del agua?", "°C por minuto", "Mide qué tan rápido sube."),
        ],
        "understand": [
            ex("La prueba A (100 mL) y la prueba B (200 mL) usan la misma fuente de calor. ¿Qué condición cambia?", "La cantidad de agua", "Es lo único que difiere."),
            ex("¿Qué es una limitación de haber hecho una sola prueba?", "Que el resultado puede ser casual y no se sabe si se repetiría", "Falta repetir para estar seguros."),
            ex("Con el doble de agua y la misma fuente de calor, ¿el calentamiento fue más rápido o más lento?", "Más lento", "Se necesitó más tiempo para llegar a 100 °C."),
        ],
        "apply": [
            arith("Una prueba pasa de 20 °C a 80 °C en 6 minutos. ¿Cuántos °C sube por minuto?", "(80-20)//6", "Se divide el aumento por los minutos.", " °C por minuto"),
            arith("Otra prueba pasa de 15 °C a 95 °C en 20 minutos. ¿Cuántos °C sube por minuto?", "(95-15)//20", "Se divide el aumento por los minutos.", " °C por minuto"),
            arith("Una tercera prueba sube 5 °C por minuto durante 12 minutos. ¿Cuántos °C sube en total?", "5*12", "Se multiplica la rapidez por los minutos.", " °C"),
        ],
        "reason": [
            ex("Hugo compara una prueba de 100 mL con llama baja y otra de 200 mL con llama alta. Dice que la cantidad de agua no influye. ¿Qué error tiene su prueba?", "Cambió también la llama, así que no es una prueba justa", "No se puede saber cuál condición causó la diferencia."),
            ex("Dos pruebas con 150 mL y la misma fuente dieron 7 y 8 °C por minuto. ¿Son parecidas o muy distintas?", "Parecidas", "Difieren solo en 1 °C por minuto."),
        ],
        "challenge": [
            arith("Una prueba pasó de 25 °C a 85 °C en 12 minutos. ¿Cuántos °C sube por minuto en promedio?", "(85-25)//12", "Se divide el aumento total por los minutos.", " °C por minuto"),
            ex("Si la rapidez de calentamiento del agua de 100 mL es 8 °C por minuto y la de 200 mL es 4 °C por minuto, ¿qué predices para 400 mL con la misma fuente?", "2 °C por minuto", "Cada vez que se duplica el agua, la rapidez baja a la mitad."),
        ],
    },
    context=[ex("En una casa se calienta una olla pequeña y una olla grande con la misma llama. La grande tarda más en llegar a 100 °C. Con lo aprendido, ¿cuál es la razón principal?", "Tiene más agua para calentar", "Con más agua se necesita más energía.")],
    selfcheck=[
        ex("¿Qué se divide para obtener los °C por minuto?", "El aumento de temperatura por los minutos", "Esa es la rapidez de calentamiento."),
        ex("¿Qué condición debe cambiar en una prueba justa?", "Solo una", "Así se sabe la causa."),
        ex("Con el doble de agua y la misma fuente, ¿el agua sube más o menos °C por minuto?", "Menos", "Se calienta más lento."),
    ],
    open_task=task(
        "Con los datos de ejemplo (A: 100 mL, 20 a 100 °C en 8 minutos; B: 200 mL, 20 a 100 °C en 16 minutos), escribe una tabla con el aumento, el tiempo y los °C por minuto de cada prueba, y una conclusión que cite tres datos y una limitación.",
        "A: 80 °C en 8 minutos = 10 °C por minuto. B: 80 °C en 16 minutos = 5 °C por minuto. Con el doble de agua se calentó a la mitad de rapidez. Limitación: se hizo una sola prueba con cada cantidad.",
        ["tabla con los cálculos correctos", "conclusión con tres datos", "limitación escrita"],
        ["tabla", "conclusión"],
        ["dividir al revés", "no citar datos en la conclusión"],
        "Pregunta qué mediría para saber si la fuente de calor fue la misma.",
    ),
    reinforce="Calcula los °C por minuto de otra prueba inventada con aumento de 60 °C en 15 minutos.",
    extend="Averigua con una persona de tu casa qué olla se calienta más rápido para la misma cantidad de agua: una delgada o una gruesa.",
)

# ================================================================ OA 15, clase 5
register(
    OA15, 5,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a explicar con evidencia qué le pasa al agua cuando se calienta y se enfría, y a decir hasta dónde llegan mis conclusiones. Sirve para comunicar resultados con honestidad.",
    prior=["Sé interpretar tablas y gráficos de calentamiento.", "Sé calcular los °C por minuto."],
    explain=[
        "Una explicación científica tiene una afirmación, evidencia y una razón. Afirmación: «Mientras el agua hierve, su temperatura se mantiene». Evidencia: la tabla de ejemplo muestra 100 °C en los minutos 10, 12 y 14. Razón: la energía recibida se usa en separar las partículas y pasar de líquido a gas.",
        "También hay que declarar los límites. Primero, los datos son de ejemplo. Segundo, el termómetro tiene un error de alrededor de 1 °C. Tercero, la temperatura de ebullición del agua depende de la altura: en lugares altos, como en la cordillera, el agua hierve a menos de 100 °C porque hay menos presión del aire. Cuarto, una sola prueba no es suficiente.",
        "Con el enfriamiento ocurre algo similar: mientras el agua se solidifica, la temperatura se mantiene en 0 °C. Las dos mesetas, la de 100 °C y la de 0 °C, muestran cambios de estado. Una buena conclusión sobre calentar y enfriar agua cita al menos dos datos, usa partículas para la razón y dice cuáles son sus límites.",
    ],
    vocab=[("afirmación", "idea principal que se quiere probar"), ("evidencia", "dato que apoya la afirmación"), ("razón", "explicación que une la evidencia con la afirmación"), ("error de medición", "pequeña diferencia entre la lectura y el valor real"), ("presión", "fuerza del aire sobre una superficie")],
    worked=[
        {"title": "Armar una explicación", "problem": "Escribe una explicación sobre la meseta de 100 °C con afirmación, evidencia y razón.", "steps": ["Afirmación: mientras hierve, la temperatura se mantiene.", "Evidencia: marcó 100 °C en los minutos 10, 12 y 14.", "Razón: la energía se usa en separar las partículas."], "answer": "Se mantiene en 100 °C porque la energía separa partículas, y la tabla lo muestra en tres registros"},
        {"title": "Reconocer un límite", "problem": "Un termómetro tiene error de 1 °C y marca 99 °C. ¿Entre qué valores puede estar la temperatura real?", "steps": ["Puede ser 1 °C menos o 1 °C más.", "Entre 98 °C y 100 °C."], "answer": "Entre 98 °C y 100 °C"},
    ],
    mistakes=[
        {"wrong": "Afirmar sin citar ningún dato.", "why": "Se confunde opinión con explicación.", "fix": "Agrega al menos dos datos de la tabla."},
        {"wrong": "Decir que el agua siempre hierve a 100 °C en cualquier lugar.", "why": "Se olvida que depende de la altura.", "fix": "Di que a nivel del mar hierve cerca de 100 °C y que en lugares altos hierve a menos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es la temperatura de ebullición del agua a nivel del mar, según la tabla de la clase?", "100 °C", "Es el dato de la meseta."),
            ex("¿Qué temperatura se mantiene mientras el agua se solidifica en el congelador?", "0 °C", "Es la meseta del congelamiento."),
            ex("Una explicación científica, ¿lleva evidencia o solo opinión?", "Evidencia", "Los datos sostienen la explicación."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué parte de una explicación une la evidencia con la afirmación?", "La razón", "Explica por qué el dato apoya la idea."),
            ex("¿Cuál es una limitación válida: (a) «el termómetro tiene un error de alrededor de 1 °C» o (b) «el agua es transparente»?", "(a)", "El error del instrumento limita la precisión."),
            ex("En lugares altos, ¿el agua hierve a más, igual o menos de 100 °C?", "A menos de 100 °C", "Hay menos presión del aire."),
        ],
        "apply": [
            arith("Un termómetro tiene error de 1 °C y marca 99 °C. ¿Cuál es el valor más alto que podría tener la temperatura real?", "99+1", "Se suma el error al valor leído.", " °C"),
            arith("La meseta de ebullición se registró en los minutos 10, 12 y 14. ¿Cuántos minutos hay entre el primer y el último registro?", "14-10", "Se resta el tiempo inicial al final.", " minutos"),
            ex("Escribe en orden las tres partes de una explicación científica: razón, afirmación, evidencia.", "Afirmación, evidencia, razón", "Primero la idea, luego el dato y después el porqué."),
        ],
        "reason": [
            ex("Marta escribe: «El agua hierve siempre a 100 °C». ¿Qué límite olvidó?", "Que depende de la altura", "A menos presión, hierve a menos de 100 °C."),
            ex("Teo concluye: «Con una sola prueba ya sé que el agua con doble cantidad tarda el doble». ¿Qué le falta?", "Repetir la prueba más veces", "Una sola medición puede ser casual."),
        ],
        "challenge": [
            ex("Dos explicaciones sobre la meseta. A: «Se queda en 100 °C porque sí». B: «Se queda en 100 °C en tres registros porque la energía separa partículas». ¿Cuál tiene afirmación, evidencia y razón?", "B", "A no entrega razón ni datos."),
            arith("Tres lecturas de la meseta fueron 99 °C, 100 °C y 101 °C. ¿Cuál es el promedio? Suma y divide por 3.", "(99+100+101)//3", "El promedio resume las lecturas.", " °C"),
        ],
    },
    context=[ex("Una persona de tu casa dice que el agua para fideos hierve más rápido con la olla tapada. Como científico, ¿qué dato necesitas para sostenerlo?", "Medir el tiempo en que llega a hervir con y sin tapa", "Se necesita una comparación con datos y una prueba justa.")],
    selfcheck=[
        ex("Una explicación sobre la meseta de 100 °C lleva una idea, un dato y un porqué. ¿Cómo se llama cada parte, en ese orden?", "Afirmación, evidencia y razón", "Así se sostiene una idea."),
        ex("¿Qué temperatura marca la meseta de ebullición de la tabla?", "100 °C", "Es el dato de ejemplo."),
        ex("Una sola prueba, ¿alcanza para estar seguros?", "No", "Hay que repetir."),
    ],
    open_task=task(
        "Escribe un párrafo corto sobre el agua que se calienta y se enfría usando los datos de ejemplo (calentamiento: 20, 36, 52, 68, 84, 100, 100, 100 °C cada 2 minutos; enfriamiento: 20, 10, 2, 0, 0, 0 °C cada 10 minutos). Debe tener afirmación, dos datos de evidencia, una razón con partículas y dos límites.",
        "Mientras el agua cambia de estado, su temperatura se mantiene. En el calentamiento marcó 100 °C en tres registros y en el enfriamiento 0 °C en tres registros. La energía se usa en cambiar las partículas de lugar. Límites: son datos de ejemplo y el termómetro tiene error de 1 °C.",
        ["afirmación clara", "dos datos citados", "razón con partículas y dos límites"],
        ["párrafo escrito"],
        ["olvidar los límites", "no citar datos"],
        "Pregunta qué experimento real propondría para comprobar su afirmación.",
    ),
    reinforce="Reescribe tu párrafo cambiando la afirmación a la meseta de 0 °C y vuelve a citar datos.",
    extend="Averigua con una persona de tu casa por qué en lugares muy altos la comida tarda más en cocerse y relaciónalo con la temperatura de ebullición del agua.",
)
