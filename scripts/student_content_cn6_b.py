"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 12 (modelo de partículas) y OA 13 (cambios de estado)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12 = "CN06 OA 12"
OA13 = "CN06 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 12, clase 1
register(
    OA12, 1,
    materials="Papel y lápiz. Para la tarea abierta: una cuchara, un vaso con agua y una bolsa plástica cerrada con aire (nunca la pongas sobre la cara).",
    use="Aprenderé a separar lo que observo en un sólido, un líquido y un gas de la explicación que doy sobre ellos. Sirve para no confundir un dato con una idea.",
    prior=["Sé que el agua puede ser hielo, agua líquida y vapor.", "Sé medir en mililitros (mL) y en centímetros (cm)."],
    explain=[
        "La materia es todo lo que tiene masa y ocupa espacio: una piedra, el agua de un vaso o el aire de un globo. Se presenta en tres estados: sólido, líquido y gaseoso. Un científico empieza observando con cuidado qué hace cada estado y lo anota sin adornos.",
        "Estas son observaciones típicas. Un sólido conserva su forma y su volumen. Un líquido toma la forma del recipiente, pero mantiene su volumen. Un gas toma la forma del recipiente y se reparte por todo el espacio que tiene. El volumen es el espacio que ocupa algo.",
        "Una observación es lo que se ve o se mide. Una interpretación es la explicación que damos, por ejemplo «la materia está hecha de partículas muy pequeñas». Las partículas no se ven a simple vista, así que esa idea es una interpretación apoyada en modelos. Para separar ambas pregúntate: ¿lo puedo ver o medir, o lo estoy explicando?",
    ],
    vocab=[("materia", "todo lo que tiene masa y ocupa espacio"), ("volumen", "espacio que ocupa un material"), ("estado de la materia", "forma en que se presenta un material: sólido, líquido o gaseoso"), ("observación", "dato que se ve o se mide"), ("interpretación", "explicación que agregamos a lo observado")],
    worked=[
        {"title": "La forma cambia, el volumen no", "problem": "Una persona mide 100 mL de jugo. En un vaso alto y delgado llega a 10 cm de altura; en un plato hondo y ancho llega a 2 cm. ¿Cambió la cantidad de jugo?", "steps": ["La altura cambió porque cambió la forma del recipiente.", "El jugo es un líquido: toma la forma del recipiente, pero su volumen se mantiene.", "Sigue habiendo 100 mL."], "answer": "No cambió: son 100 mL en los dos recipientes"},
        {"title": "Observación o interpretación", "problem": "Frase A: «La plasticina no cambia de forma cuando la paso de un plato a otro». Frase B: «No cambia de forma porque sus partículas están muy juntas y ordenadas». ¿Cuál es la observación?", "steps": ["La frase A se puede ver al pasar la plasticina de plato.", "La frase B explica algo que no se ve: las partículas."], "answer": "A es observación; B es interpretación"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua «tiene menos cantidad» porque en un plato ancho se ve más baja.", "why": "Se mira la altura y no el volumen.", "fix": "Mide los mL: un líquido mantiene su volumen aunque cambie su forma."},
        {"wrong": "Escribir «las partículas se ven con una lupa» como si fuera una observación.", "why": "Se presenta una idea del modelo como si fuera un dato visto.", "fix": "Las partículas son parte de una explicación; lo observable es la forma y el volumen."},
    ],
    tiers={
        "recovery": [
            ex("Un ladrillo pasa de una caja a otra y no cambia su forma. ¿Es sólido, líquido o gas?", "Sólido", "Conserva su forma al cambiar de recipiente."),
            ex("El aire de un globo se reparte por todo el espacio del globo. ¿Qué estado de la materia es el aire?", "Gaseoso", "Un gas llena todo el espacio disponible."),
            ex("La leche de una botella toma la forma del vaso donde la sirves y mantiene su volumen. ¿Qué estado es?", "Líquido", "Toma la forma del recipiente, pero mantiene su volumen."),
        ],
        "understand": [
            ex("Frase: «El trozo de hielo mide 4 cm de largo». ¿Es una observación o una interpretación?", "Observación", "Es un dato medido con una regla."),
            ex("Frase: «El agua se desliza porque sus partículas pueden moverse unas sobre otras». ¿Es una observación o una interpretación?", "Interpretación", "Explica con partículas, que no se ven."),
            ex("Tres materiales. A: conserva su forma y su volumen. B: toma la forma del recipiente y mantiene su volumen. C: llena todo el recipiente. ¿Cuál es el líquido?", "B", "El líquido cambia de forma, pero mantiene su volumen."),
        ],
        "apply": [
            arith("En una jarra hay 250 mL de agua y se sirven 100 mL en un vaso. El resto se pasa a una botella. ¿Cuántos mL de agua hay en la botella?", "250-100", "El volumen del líquido se conserva al pasarlo de un recipiente a otro.", " mL"),
            ex("Clasifica estos tres materiales en el orden dado: aceite de una botella, madera de una mesa, vapor de agua de una olla.", "Líquido, sólido, gas", "El aceite fluye, la madera conserva su forma y el vapor llena el espacio."),
            arith("Una jarra con 1.000 mL de agua se reparte en vasos que se llenan con 250 mL cada uno. ¿Cuántos vasos se llenan completos?", "1000//250", "Se divide el volumen total por el volumen de cada vaso.", " vasos"),
        ],
        "reason": [
            ex("Pedro anota: «El gas se reparte por todo el frasco porque sus partículas se mueven en todas direcciones». ¿Qué parte de su frase es interpretación?", "«Porque sus partículas se mueven en todas direcciones»", "Lo observable es que el gas se reparte; la causa con partículas es una explicación."),
            ex("Lucía observó que 120 mL de agua llegan a 5 cm de altura en un vaso y a 2 cm en una bandeja. Dice: «En la bandeja hay menos agua». ¿Qué dato muestra que se equivoca?", "En los dos recipientes hay 120 mL", "La altura depende de la forma del recipiente, no cambia la cantidad."),
        ],
        "challenge": [
            ex("Un frasco con 1 L de aire se conecta con otro frasco vacío de 1 L y el aire se reparte entre los dos. ¿Qué propiedad de los gases muestra esto: (a) tiene forma fija o (b) llena todo el espacio disponible?", "(b)", "El gas se extiende por todo el espacio que le dan."),
            ex("Observación: la piedra mide 6 cm de largo en una caja y 6 cm sobre la mesa. ¿Qué propiedad de los sólidos muestra: forma fija o forma del recipiente?", "Forma fija", "La piedra no cambia su forma al cambiar de lugar."),
        ],
    },
    context=[ex("Una persona de tu casa dice: «Cuando abro una botella de colonia, el olor llega a toda la pieza». Según lo que aprendiste, ¿qué propiedad de los gases es la observación?", "Que llenan todo el espacio disponible", "El olor viaja porque el gas se reparte por toda la pieza.")],
    selfcheck=[
        ex("¿Qué estado de la materia conserva su forma y su volumen?", "El sólido", "Es la propiedad que distingue al sólido."),
        ex("Una interpretación, ¿se ve o se explica?", "Se explica", "Una interpretación es la idea que agregamos a lo observado."),
        ex("Si 180 mL de agua se pasan a otro recipiente, ¿cuántos mL hay después?", "180 mL", "El volumen de un líquido se mantiene."),
    ],
    open_task=task(
        "Observa una cuchara, un vaso con agua y una bolsa plástica cerrada con aire. Dibuja una tabla con tres columnas (material, lo que observo, lo que interpreto). En «lo que observo» anota qué pasa con la forma y el volumen al cambiarlos de lugar o de recipiente; en «lo que interpreto» agrega una explicación breve. Marca con O las observaciones y con I las interpretaciones.",
        "Cuchara: O, no cambia su forma al pasarla de la mesa al plato. I, es sólida porque sus partículas están muy juntas. Agua: O, toma la forma del vaso. Aire en la bolsa: O, la bolsa se infla por todos lados.",
        ["tres materiales observados", "observaciones que se pueden ver o medir", "interpretaciones marcadas y distintas de las observaciones"],
        ["tabla con tres filas", "marcas O e I"],
        ["escribir una explicación en la columna de observación", "no comparar forma y volumen"],
        "Pregunta cuál de tus frases no se puede ver ni medir y por qué es una interpretación.",
    ),
    reinforce="Escribe dos observaciones y una interpretación sobre el hielo, el agua y el vapor.",
    extend="Averigua con una persona de tu casa qué estado de la materia es la masa de pan y cuál es la harina, y qué observación te lo muestra.",
)

# ================================================================ OA 12, clase 2
register(
    OA12, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a hacer preguntas que se puedan comprobar y a predecir qué pasa con sólidos, líquidos y gases. Sirve para preparar explicaciones con partículas.",
    prior=["Sé que un líquido mantiene su volumen y que un gas llena el recipiente.", "Sé que una predicción se apoya en un dato."],
    explain=[
        "Una pregunta comprobable se responde midiendo u observando. «¿Cuántos mL ocupa el aire de una jeringa al empujar el émbolo?» se puede comprobar. «¿Qué estado de la materia es más simpático?» no, porque depende de opiniones.",
        "Una predicción dice qué resultado esperamos y por qué, por ejemplo «Si empujo el émbolo de una jeringa con aire, entonces el volumen bajará». Se apoya en lo que ya sabemos: los gases se pueden comprimir (apretar para que ocupen menos espacio), pero los líquidos casi no.",
        "Después se comprueba. En una jeringa tapada en la punta, 60 mL de aire bajan a 30 mL al empujar. Con 60 mL de agua, el émbolo casi no avanza. Si la predicción falla, se corrige la predicción y se piensa otra explicación; los datos no se cambian.",
    ],
    vocab=[("comprimir", "apretar para que algo ocupe menos espacio"), ("pregunta comprobable", "pregunta que se responde con una medición u observación"), ("predicción", "resultado que se espera, apoyado en lo que ya sabemos"), ("jeringa", "tubo con émbolo que se empuja; aquí, sin aguja"), ("émbolo", "pieza que se empuja dentro de la jeringa")],
    worked=[
        {"title": "Predecir con un sólido", "problem": "Un bloque de madera ocupa 30 cm³ en una mesa. Se guarda en una caja de 100 cm³. Predice cuánto espacio ocupará la madera.", "steps": ["La madera es un sólido: conserva forma y volumen.", "Entonces seguirá ocupando lo mismo, aunque la caja sea mayor."], "answer": "Ocupará 30 cm³"},
        {"title": "Elegir la pregunta comprobable", "problem": "¿Cuál se puede comprobar: «¿Qué es más lindo, el agua o el aire?» o «¿Cuántos mL de aire hay en la jeringa después de empujar?»?", "steps": ["La primera depende de gustos.", "La segunda se responde leyendo la escala de la jeringa."], "answer": "La segunda"},
    ],
    mistakes=[
        {"wrong": "Predecir sin decir en qué se apoya.", "why": "Se confunde predecir con adivinar.", "fix": "Empieza con «Si…» y nombra la propiedad del estado que usas."},
        {"wrong": "Cambiar los números medidos cuando la predicción falla.", "why": "Se quiere tener razón.", "fix": "Los datos son la evidencia: se corrige la predicción."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál se puede comprobar midiendo: «¿Cuántos mL ocupa el aire?» o «¿Qué gas es más bonito?»?", "¿Cuántos mL ocupa el aire?", "Se responde con una medición, no con opinión."),
            ex("Completa con comprimir o no comprimir: los gases se pueden ___ con facilidad.", "comprimir", "El aire de una jeringa puede ocupar menos espacio al empujar."),
            ex("Si pasas 80 mL de jugo de un vaso a una jarra, ¿cuántos mL predices que habrá en la jarra?", "80 mL", "Un líquido mantiene su volumen."),
        ],
        "understand": [
            ex("¿Cuál es una predicción bien escrita: (a) «El aire es divertido» o (b) «Si empujo el émbolo con aire, entonces el volumen bajará»?", "(b)", "Tiene «si… entonces» y se puede medir."),
            ex("En una jeringa, el aire baja de 60 mL a 30 mL y el agua casi no baja. ¿Qué estado se puede comprimir más?", "El gas", "El aire redujo su volumen y el agua casi no."),
            ex("¿Por qué no se puede comprobar la pregunta «¿Qué estado de la materia es el más simpático?»?", "Porque depende de opiniones y no de mediciones", "Una pregunta comprobable necesita datos."),
        ],
        "apply": [
            arith("Una jeringa tiene 60 mL de aire y se empuja hasta que marca 30 mL. ¿Cuántos mL se redujo el volumen?", "60-30", "Se resta el volumen final al inicial.", " mL"),
            arith("Otra jeringa tiene 20 mL de aire y se suelta hasta que marca 50 mL. ¿Cuántos mL aumentó el volumen?", "50-20", "Se resta el volumen inicial al final.", " mL"),
            ex("Predice: un trozo de hielo de 40 cm³ se pone en una caja grande de 500 cm³. ¿Qué volumen ocupa el hielo mientras sigue siendo sólido?", "40 cm³", "Un sólido conserva su volumen."),
        ],
        "reason": [
            ex("Nico predijo que la jeringa con agua bajaría de 60 mL a 30 mL. Midió 59 mL. ¿Qué debe corregir?", "La predicción", "Los datos medidos son la evidencia."),
            ex("Dos amigos usan una jeringa con aire a 60 mL. Ana empuja hasta 40 mL y Beto hasta 20 mL. ¿Quién comprimió más el aire?", "Beto", "Su volumen final es menor, así que el aire quedó más apretado."),
        ],
        "challenge": [
            ex("Se tapa una jeringa con 90 mL de aire y se empuja hasta 45 mL. Una amiga dice: «El aire desapareció». ¿Qué dato lo contradice?", "El aire sigue ahí, solo ocupa menos espacio, 45 mL", "Se comprimió, pero no desapareció."),
            arith("Un grupo de 3 jeringas marca 40 mL cada una antes de empujar. Después de empujar marcan 25 mL cada una. ¿Cuántos mL en total se redujeron entre las 3?", "3*(40-25)", "Cada jeringa redujo 15 mL y hay 3.", " mL"),
        ],
    },
    context=[ex("En una bicicleta, la bomba de aire aprieta el aire para meterlo al neumático. Con lo que sabes, ¿qué propiedad de los gases permite meter tanto aire en un espacio pequeño?", "Que se pueden comprimir", "Al comprimir, el mismo aire ocupa menos espacio.")],
    selfcheck=[
        ex("¿Qué estado se comprime más fácilmente: sólido, líquido o gas?", "Gas", "Su volumen cambia al empujar."),
        ex("En una predicción escrita como «Si…, entonces…», ¿qué palabra introduce el resultado que esperamos?", "Entonces", "Después del «si» se nombra la condición y después del «entonces», el resultado esperado."),
        ex("Si el resultado contradice tu predicción, ¿qué cambias?", "La predicción", "Los datos no se cambian."),
    ],
    open_task=task(
        "Con la información de esta clase (el aire de una jeringa baja de 60 mL a 30 mL; el agua casi no baja), escribe una pregunta comprobable y una predicción con «Si…, entonces…» sobre qué pasará con 80 mL de aire si el émbolo se empuja hasta la mitad. Luego escribe cuánto marcaría la jeringa y qué estado de la materia explica tu predicción.",
        "Pregunta: ¿cuántos mL marcará la jeringa? Predicción: si empujo el émbolo hasta la mitad, entonces marcará 40 mL, porque el aire es un gas y se comprime.",
        ["pregunta comprobable", "predicción con «Si…, entonces…»", "valor calculado y estado nombrado"],
        ["pregunta", "predicción", "cálculo de la mitad"],
        ["hacer preguntas de gusto", "predecir sin decir por qué"],
        "Pregunta qué cambiarías si el resultado real fuera distinto de 40 mL.",
    ),
    reinforce="Escribe otra predicción con «Si…, entonces…» sobre un líquido que se pasa de recipiente.",
    extend="Averigua con una persona de tu casa qué pasa con el aire de un globo cuando se aprieta con las manos y anota la observación.",
)

# ================================================================ OA 12, clase 3
register(
    OA12, 3,
    materials="Papel y lápiz. Los dibujos de partículas se describen con palabras en el cuaderno; puedes dibujarlos con puntos.",
    use="Aprenderé el modelo de partículas: cómo se imaginan las partículas en un sólido, un líquido y un gas, y qué límites tiene ese modelo. Sirve para explicar por qué los estados se comportan distinto.",
    prior=["Sé que un sólido conserva su forma, un líquido toma la del recipiente y un gas llena el espacio.", "Sé que una interpretación explica lo observado."],
    explain=[
        "Un modelo es una representación que ayuda a explicar algo que no podemos ver. El modelo de partículas dice que toda la materia está formada por partículas muy pequeñas que están siempre en movimiento. Lo que cambia entre estados es qué tan juntas están y cómo se mueven.",
        "En un sólido, las partículas están muy juntas y ordenadas, y solo vibran (tiemblan) en su lugar. En un líquido están juntas pero desordenadas y se deslizan unas sobre otras. En un gas están muy separadas, se mueven rápido en todas direcciones y chocan con las paredes del recipiente.",
        "El modelo explica lo observado: el sólido conserva su forma porque sus partículas no se desplazan; el líquido fluye porque se deslizan; el gas se comprime porque tiene mucho espacio vacío entre partículas. Pero tiene límites: los dibujos son planos, las partículas reales no son bolitas de colores y el dibujo no muestra todo el movimiento.",
    ],
    vocab=[("modelo", "representación que ayuda a explicar algo que no se ve"), ("partícula", "pieza muy pequeña de la que está hecha la materia"), ("vibrar", "temblar o moverse de un lado a otro sin cambiar de lugar"), ("deslizarse", "moverse pasando unas sobre otras"), ("limitación", "algo que el modelo no muestra o muestra de forma distinta a la realidad")],
    worked=[
        {"title": "Elegir el modelo de un líquido", "problem": "Modelo X: puntos muy juntos y ordenados que solo tiemblan. Modelo Y: puntos juntos pero desordenados que se deslizan. Modelo Z: puntos muy separados que se mueven rápido. ¿Cuál representa el agua líquida?", "steps": ["El agua fluye, así que sus partículas deben poder deslizarse.", "Eso describe al modelo Y: juntas pero desordenadas."], "answer": "Modelo Y"},
        {"title": "Contar partículas del modelo", "problem": "El modelo de un sólido dibuja 3 filas con 6 partículas cada una. ¿Cuántas partículas dibuja?", "steps": ["Hay 3 filas.", "Cada fila tiene 6 partículas: 3 × 6 = 18."], "answer": "18 partículas"},
    ],
    mistakes=[
        {"wrong": "Pensar que las partículas de un sólido están quietas.", "why": "Se confunde sólido con sin movimiento.", "fix": "Vibran en su lugar, aunque no se desplacen."},
        {"wrong": "Creer que el dibujo del modelo es una foto de las partículas reales.", "why": "Se olvida que un modelo es una representación.", "fix": "Pregúntate qué cosa no muestra el dibujo."},
    ],
    tiers={
        "recovery": [
            ex("Partículas muy juntas y ordenadas que solo vibran en su lugar. ¿Qué estado representan?", "Sólido", "No se desplazan y mantienen el orden."),
            ex("Partículas muy separadas que se mueven rápido en todas direcciones. ¿Qué estado representan?", "Gas", "Hay mucho espacio entre ellas."),
            ex("Partículas juntas, pero desordenadas, que se deslizan. ¿Qué estado representan?", "Líquido", "Pueden pasar unas sobre otras, por eso el líquido fluye."),
        ],
        "understand": [
            ex("Según el modelo de partículas, ¿por qué un sólido conserva su forma?", "Porque sus partículas no se desplazan y mantienen su orden", "Solo vibran en su lugar."),
            ex("Según el modelo, ¿por qué un gas se puede comprimir?", "Porque tiene mucho espacio vacío entre sus partículas", "Al apretar, las partículas se acercan."),
            ex("¿Cuál es una limitación del modelo: (a) explica por qué un líquido fluye o (b) dibuja las partículas como bolitas planas de colores?", "(b)", "Las partículas reales no son bolitas de colores ni planas."),
        ],
        "apply": [
            arith("El modelo de un sólido dibuja 4 filas con 5 partículas cada una. ¿Cuántas partículas dibuja?", "4*5", "Se multiplican filas por partículas por fila.", " partículas"),
            ex("Un cubo de hielo se pone en un plato y mantiene su forma. ¿Qué movimiento de las partículas explica esto: vibrar en su lugar o desplazarse por todo el plato?", "Vibrar en su lugar", "Si se desplazaran, el hielo cambiaría de forma."),
            arith("Un modelo de gas dibuja 12 partículas en una caja y otro modelo dibuja 30 partículas en la misma caja. ¿Cuántas partículas más tiene el segundo modelo?", "30-12", "Se resta para saber la diferencia.", " partículas"),
        ],
        "reason": [
            ex("Mateo dice: «Si las partículas de un gas están muy separadas, el aire debería poder apretarse hasta ocupar menos espacio». ¿Qué dato de la clase anterior apoya su idea?", "El aire de la jeringa bajó de 60 mL a 30 mL al empujar", "Al apretar, las partículas se acercan y el mismo aire ocupa menos volumen."),
            ex("Un modelo A dibuja partículas de líquido en filas ordenadas que no se mueven. ¿Qué observación de los líquidos contradice a ese modelo?", "Que el líquido fluye", "Si no se movieran ni se deslizaran, no fluiría."),
        ],
        "challenge": [
            ex("Según el modelo, el sólido solo vibra, el líquido se desliza y el gas se mueve libre. Ordena los estados desde el que tiene partículas con más libertad de movimiento al que tiene menos.", "Gas, líquido, sólido", "El gas se mueve libre, el líquido se desliza y el sólido solo vibra."),
            arith("Un dibujo de líquido tiene 24 partículas, y se dibujan en 4 grupos iguales para mostrar movimiento. ¿Cuántas partículas hay en cada grupo?", "24//4", "Se reparte el total en grupos iguales.", " partículas"),
        ],
    },
    context=[ex("Un amigo dice: «El olor de una naranja recién pelada llega a toda la cocina porque sus partículas se mueven en todas direcciones». ¿Con qué estado de la materia explica el modelo ese comportamiento?", "Con el estado gaseoso", "En el gas las partículas se mueven libres y se esparcen.")],
    selfcheck=[
        ex("¿Qué partículas están más separadas: las de un sólido o las de un gas?", "Las de un gas", "En el gas hay más espacio entre partículas."),
        ex("En el modelo, ¿qué hacen las partículas de un sólido?", "Vibran en su lugar", "No se desplazan."),
        ex("¿Un modelo es una copia exacta de la realidad?", "No", "Es una representación con limitaciones."),
    ],
    open_task=task(
        "Dibuja tres cajas. En la primera, 12 puntos ordenados en 3 filas de 4, con flechitas cortas para mostrar que vibran. En la segunda, 12 puntos juntos y desordenados con flechas largas que se deslizan. En la tercera, 12 puntos muy separados con flechas largas hacia distintos lados. Rotula cada caja con su estado y escribe una limitación de tu dibujo.",
        "Caja 1: sólido. Caja 2: líquido. Caja 3: gas. Limitación: las partículas reales no son puntos y no están en un plano.",
        ["tres cajas con 12 puntos cada una", "arreglo y movimiento coinciden con el estado", "una limitación escrita"],
        ["tres dibujos rotulados", "limitación escrita"],
        ["dibujar el sólido sin orden", "no mostrar el movimiento"],
        "Pregunta qué observación (forma o volumen) explica cada caja.",
    ),
    reinforce="Dibuja de nuevo el estado que te costó más y explica en una frase cómo se mueven sus partículas.",
    extend="Averigua con una persona de tu casa cómo se explica que el olor de la comida llegue a otra pieza y relaciónalo con el modelo de partículas.",
)

# ================================================================ OA 12, clase 4
register(
    OA12, 4,
    materials="Papel y lápiz. Las tablas están escritas en el cuaderno.",
    use="Aprenderé a comparar dos modelos usando un criterio: cuántas observaciones explica cada uno. Sirve para decidir cuál modelo es más útil.",
    prior=["Conozco el modelo de partículas de los tres estados.", "Sé que un modelo se juzga por lo que explica y por sus límites."],
    explain=[
        "Un buen modelo explica muchas observaciones. Para comparar dos modelos usamos un criterio claro: contamos cuántas observaciones explica cada uno. El que explica más observaciones es el más útil, aunque ninguno sea perfecto.",
        "Imagina cuatro observaciones: (1) un sólido conserva su forma, (2) un líquido fluye, (3) un gas se puede comprimir, (4) el olor de un perfume se esparce por una pieza. El modelo A dice que la materia está hecha de partículas quietas. El modelo B dice que está hecha de partículas en movimiento, con más o menos espacio entre ellas según el estado.",
        "El modelo A solo explica la observación 1. El modelo B explica las cuatro, porque el movimiento explica que el líquido fluya y que el olor viaje, y el espacio entre partículas explica la compresión. Con este criterio, el modelo B es el mejor. Aun así, B tiene limitaciones, porque no muestra el tamaño real de las partículas.",
    ],
    vocab=[("criterio", "regla para comparar y decidir"), ("compresión", "reducción del volumen al apretar"), ("difusión", "esparcirse una sustancia, como un olor, por el aire"), ("evidencia", "dato que apoya una explicación"), ("conclusión", "idea final apoyada en los datos")],
    worked=[
        {"title": "Contar observaciones explicadas", "problem": "El modelo A explica 2 de 4 observaciones y el modelo B explica 4 de 4. ¿Cuántas observaciones más explica B?", "steps": ["B explica 4.", "A explica 2: 4 − 2 = 2."], "answer": "2 observaciones más"},
        {"title": "Elegir con un criterio", "problem": "Con el criterio «explica más observaciones», ¿cuál es mejor: un modelo que explica 3 o uno que explica 1?", "steps": ["Se comparan los números de observaciones.", "3 es mayor que 1."], "answer": "El que explica 3"},
    ],
    mistakes=[
        {"wrong": "Elegir un modelo porque su dibujo es más bonito.", "why": "No se usó el criterio acordado.", "fix": "Cuenta cuántas observaciones explica cada modelo."},
        {"wrong": "Decir que el mejor modelo no tiene ninguna limitación.", "why": "Se piensa que un modelo útil es perfecto.", "fix": "Anota igual qué cosa no muestra."},
    ],
    tiers={
        "recovery": [
            ex("El modelo A explica 1 observación y el modelo B explica 4. Con el criterio «explica más observaciones», ¿cuál es mejor?", "El modelo B", "4 es mayor que 1."),
            ex("¿Qué es un criterio en Ciencias: una regla para comparar o un dibujo bonito?", "Una regla para comparar", "Permite decidir con un mismo patrón."),
            ex("Si dos modelos explican las mismas 3 observaciones, ¿alguno explica más?", "No", "Empatan con el criterio del número de observaciones."),
        ],
        "understand": [
            ex("El olor de un perfume se esparce por la pieza. ¿Qué modelo lo explica: partículas quietas o partículas en movimiento?", "Partículas en movimiento", "Para esparcirse hay que moverse."),
            ex("Un gas se puede comprimir. ¿Qué dice el modelo de partículas sobre eso?", "Que hay espacio entre sus partículas", "Al apretar, se acercan las partículas."),
            ex("¿Qué debe llevar una buena comparación de modelos: un criterio y datos o solo una opinión?", "Un criterio y datos", "Así otra persona puede repetir la comparación."),
        ],
        "apply": [
            arith("Se revisan 5 observaciones. El modelo P explica 4 de ellas y el modelo Q explica 2. ¿Cuántas observaciones más explica P que Q?", "4-2", "Se restan las observaciones explicadas por cada modelo.", " observaciones"),
            arith("En 3 pruebas distintas, el modelo B explicó 4, 3 y 5 observaciones. ¿Cuántas observaciones explicó en total?", "4+3+5", "Se suman los resultados de las tres pruebas.", " observaciones"),
            ex("Observaciones: (1) el hielo mantiene su forma, (2) el agua fluye. ¿Qué dos movimientos de partículas las explican, en ese orden?", "Vibrar en su lugar y deslizarse", "El sólido vibra sin desplazarse y el líquido se desliza."),
        ],
        "reason": [
            ex("Ema dice que su modelo es mejor porque tiene colores bonitos. ¿Qué criterio olvidó?", "El número de observaciones que explica", "El color no ayuda a explicar fenómenos."),
            ex("Un modelo explica que el aire se comprime y que el olor se esparce, pero no que el hielo conserve su forma. ¿Qué le falta explicar?", "Por qué un sólido conserva su forma", "Debe explicar la observación del sólido."),
        ],
        "challenge": [
            ex("Dos modelos explican 4 de 4 observaciones. El modelo C usa un dibujo en un plano y el modelo D usa un dibujo en tres dimensiones. ¿Cuál tiene menos limitaciones al representar el espacio?", "El modelo D", "Un dibujo de tres dimensiones muestra mejor el espacio."),
            arith("Un modelo explica 6 de las 8 observaciones de un cuadro. Otro modelo explica 5. ¿Cuántas observaciones del cuadro no explica el primer modelo?", "8-6", "Se resta lo explicado al total de observaciones.", " observaciones"),
        ],
    },
    context=[ex("Al abrir una botella de bebida, se oye un siseo y salen gases. Un modelo dice que el gas está comprimido en la botella. ¿Qué observación explica ese modelo?", "Que el gas se escapa al abrir, porque estaba apretado", "El gas comprimido ocupa menos espacio y sale al abrir.")],
    selfcheck=[
        ex("¿Qué modelo explica más observaciones: partículas quietas o partículas en movimiento?", "Partículas en movimiento", "Explica fluir, comprimir y esparcir."),
        ex("¿Cómo se llama la regla que se usa para comparar modelos?", "Criterio", "Es el patrón para decidir."),
        ex("Un buen modelo, ¿tiene limitaciones?", "Sí", "Ningún modelo es una copia exacta."),
    ],
    open_task=task(
        "Compara dos modelos con este criterio: cuántas de estas cuatro observaciones explica cada uno. Observaciones: (1) el hielo mantiene su forma, (2) el agua fluye, (3) el aire se comprime, (4) el olor se esparce. Modelo A: partículas quietas siempre. Modelo B: partículas en movimiento, juntas en sólidos y líquidos, separadas en gases. Escribe un cuadro con sí o no para cada observación y una conclusión con una limitación.",
        "A: 1 sí, 2 no, 3 no, 4 no. B: 1 sí, 2 sí, 3 sí, 4 sí. Conclusión: B explica 4 y A explica 1. Limitación: ningún dibujo muestra el tamaño real.",
        ["cuadro con las cuatro observaciones", "número de observaciones por modelo", "conclusión con una limitación"],
        ["cuadro completo", "conclusión escrita"],
        ["no usar el mismo criterio para los dos modelos", "concluir sin contar"],
        "Pregunta qué observación nueva podría hacer que cambies de modelo.",
    ),
    reinforce="Inventa una quinta observación sobre los estados y decide si el modelo B la explica.",
    extend="Averigua con una persona de tu casa qué ejemplo de la cocina muestra que un gas se mueve y se esparce.",
)

# ================================================================ OA 13, clase 1
register(
    OA13, 1,
    materials="Papel y lápiz. Para la tarea abierta: hielo en un plato, un vaso con agua fría y ropa o paño húmedo. No uses estufa ni agua hirviendo.",
    use="Aprenderé a nombrar los cambios de estado (fusión, solidificación, evaporación, ebullición, condensación y sublimación) a partir de observaciones. Sirve para describir lo que pasa con el agua sin confundirse.",
    prior=["Sé que el agua puede estar en estado sólido, líquido y gaseoso.", "Conozco el modelo de partículas de los estados."],
    explain=[
        "Un cambio de estado ocurre cuando una sustancia pasa de un estado a otro por ganar o perder calor. La fusión es de sólido a líquido (el hielo se derrite). La solidificación es de líquido a sólido (el agua se hace hielo). La evaporación y la ebullición son de líquido a gas. La condensación es de gas a líquido. La sublimación es de sólido directo a gas.",
        "La evaporación y la ebullición se parecen, pero se observan distinto. La evaporación ocurre solo en la superficie del líquido, es lenta y puede pasar a cualquier temperatura, como cuando se seca la ropa. La ebullición ocurre en todo el líquido, con burbujas, y para el agua a nivel del mar ocurre a 100 °C.",
        "Recuerda separar observación e interpretación. Observación: «aparecen gotas en la parte de afuera de un vaso con agua fría». Interpretación: «el vapor de agua del aire se enfrió y se hizo líquido». Un ejemplo de sublimación es la ropa congelada que se seca en invierno sin derretirse: el hielo pasa directo a vapor.",
    ],
    vocab=[("fusión", "paso de sólido a líquido"), ("solidificación", "paso de líquido a sólido"), ("evaporación", "paso lento de líquido a gas en la superficie"), ("ebullición", "paso rápido de líquido a gas en todo el líquido, con burbujas"), ("condensación", "paso de gas a líquido"), ("sublimación", "paso de sólido directo a gas")],
    worked=[
        {"title": "Nombrar un cambio", "problem": "Observación: un hielo sobre un plato se convierte en agua líquida. ¿Qué cambio de estado es?", "steps": ["Antes: sólido. Después: líquido.", "De sólido a líquido se llama fusión."], "answer": "Fusión"},
        {"title": "Evaporación o ebullición", "problem": "Un charco de agua en una vereda desaparece en un día soleado, sin burbujas. ¿Es evaporación o ebullición?", "steps": ["Hay paso de líquido a gas.", "Es lento, solo en la superficie y no hay burbujas: es evaporación."], "answer": "Evaporación"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua que desaparece de un charco «hirvió».", "why": "Se confunde evaporación con ebullición.", "fix": "Sin burbujas y a temperatura ambiente, es evaporación."},
        {"wrong": "Decir que las gotas de afuera del vaso frío salieron del agua del vaso.", "why": "Se interpreta sin evidencia.", "fix": "Las gotas se forman por condensación del vapor de agua del aire."},
    ],
    tiers={
        "recovery": [
            ex("Un helado de agua se derrite en tu mano. ¿Qué cambio de estado ocurre?", "Fusión", "Pasa de sólido a líquido."),
            ex("El agua de una bandeja se transforma en hielo en el congelador. ¿Qué cambio de estado ocurre?", "Solidificación", "Pasa de líquido a sólido."),
            ex("El vapor de agua del aire se vuelve gotitas sobre un espejo frío. ¿Qué cambio de estado ocurre?", "Condensación", "Pasa de gas a líquido."),
        ],
        "understand": [
            ex("En Ciencias, ¿en qué se diferencia la ebullición de la evaporación: tiene burbujas en todo el líquido o solo ocurre en la superficie?", "La ebullición tiene burbujas en todo el líquido", "La evaporación ocurre en la superficie y es más lenta."),
            ex("Frase: «Aparecen gotas en un vaso con agua fría». ¿Es una observación o una interpretación?", "Observación", "Se ve directamente."),
            ex("Frase: «Las gotas del vaso salieron del vapor de agua del aire». ¿Es una observación o una interpretación?", "Interpretación", "Explica de dónde vino el agua y no se ve."),
        ],
        "apply": [
            ex("La ropa congelada en invierno se seca sin derretirse. ¿Qué cambio de estado explica esto?", "Sublimación", "El hielo pasa directo a vapor."),
            ex("En una olla grande hay agua con burbujas por todos lados a 100 °C. ¿Evaporación o ebullición?", "Ebullición", "Hay burbujas en todo el líquido."),
            arith("Un congelador tiene una bandeja con 12 cubos. Cada cubo se hizo de 25 mL de agua. ¿Cuántos mL de agua se solidificaron?", "12*25", "Se multiplica el número de cubos por el volumen de cada uno.", " mL"),
        ],
        "reason": [
            ex("Mateo dice que el charco desapareció «porque el suelo se lo bebió». Lo observado fue que el agua de una bandeja de plástico, dejada al sol, bajó de 3 mm a 0 mm de altura. ¿Qué cambio de estado explica mejor lo observado?", "Evaporación", "La bandeja no absorbe ni deja salir el agua, así que solo puede pasar a vapor."),
            ex("Camila ve que un cubo de hielo en un plato se hace agua y dice «el calor del aire entró al hielo». ¿Cuál es el cambio de estado y cuál palabra es interpretación?", "Fusión; «el calor del aire entró al hielo»", "Lo observado es el derretirse; la causa es la explicación."),
        ],
        "challenge": [
            ex("Un vaso con hielo, afuera, se cubre de gotas. Pedro dice que es fusión. ¿Por qué se equivoca?", "Porque las gotas vienen de un gas que pasó a líquido, y eso es condensación", "La fusión sería del hielo del vaso, pero las gotas están afuera."),
            arith("Un congelador tiene 3 bandejas con 8 cubos cada una. Cada cubo tiene 20 mL de agua. ¿Cuántos mL se solidificaron en total?", "3*8*20", "Se multiplican bandejas, cubos y mL por cubo.", " mL"),
        ],
    },
    context=[ex("Una persona de tu casa tiende ropa mojada en un día de viento. Después de dos horas está seca. ¿Qué cambio de estado ocurrió con el agua de la ropa?", "Evaporación", "El agua líquida pasó lentamente a gas.")],
    selfcheck=[
        ex("¿Cómo se llama el paso de sólido a líquido?", "Fusión", "Es el derretirse."),
        ex("¿Cómo se llama el paso de gas a líquido?", "Condensación", "Es lo contrario de evaporación."),
        ex("¿Cómo se llama el paso de sólido directo a gas?", "Sublimación", "No pasa por el estado líquido."),
    ],
    open_task=task(
        "Observa en tu casa un hielo en un plato, un vaso con agua fría y un paño húmedo. Escribe tres observaciones (una por cada situación) y, al lado, el cambio de estado que crees que ocurre. Marca cuál parte de tu frase es observación (O) y cuál es interpretación (I).",
        "Hielo en el plato: O, el hielo se hizo agua. I, fusión por el calor de la pieza. Vaso frío: O, gotas afuera. I, condensación del vapor del aire.",
        ["tres situaciones", "observación y cambio de estado nombrados", "marcas O e I"],
        ["lista de tres situaciones", "cambio nombrado"],
        ["confundir evaporación y ebullición", "no marcar O e I"],
        "Pregunta cuál de tus frases dependía de ideas y cuál se veía directamente.",
    ),
    reinforce="Nombra tres cambios de estado que viste esta semana en tu casa y marca cuál observación te permitió nombrarlos.",
    extend="Averigua con una persona de tu casa si en invierno la ropa se seca estando congelada y compara con lo que aprendiste de sublimación.",
)

# ================================================================ OA 13, clase 2
register(
    OA13, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno. No uses agua caliente sin una persona adulta.",
    use="Aprenderé a formular una pregunta comprobable y una predicción sobre qué hace más rápido un cambio de estado. Sirve para diseñar pruebas justas.",
    prior=["Sé nombrar los seis cambios de estado.", "Sé que en una prueba justa solo cambia una condición."],
    explain=[
        "Una pregunta comprobable puede ser: «¿se evapora más rápido el agua en un plato ancho o en un vaso angosto?». Para responderla hay que cambiar una sola condición (la forma del recipiente) y mantener iguales las demás: la misma cantidad de agua, el mismo lugar y el mismo tiempo. Eso es una prueba justa.",
        "La condición que cambiamos es la variable que cambia. Lo que medimos es la variable que medimos, por ejemplo el tiempo en minutos que demora en desaparecer el agua. Las condiciones que mantenemos iguales son las constantes.",
        "Una predicción usa lo que sabemos: si el agua tiene más superficie, hay más lugares por donde las partículas pueden escapar al aire. Entonces predecimos: «Si uso un plato ancho, entonces el agua se evaporará más rápido». También sabemos que más calor acelera el cambio. Después se comparan los datos con la predicción.",
    ],
    vocab=[("variable que cambia", "condición que se modifica a propósito"), ("variable que se mide", "dato que se observa o mide"), ("constante", "condición que se mantiene igual"), ("prueba justa", "prueba en que solo cambia una condición"), ("superficie", "parte de afuera del agua, en contacto con el aire")],
    worked=[
        {"title": "Reconocer variables", "problem": "Se ponen 50 mL de agua en un plato ancho y 50 mL en un vaso angosto, ambos en la misma ventana. Se mide cuántas horas demoran en secarse. ¿Qué variable cambia y qué variable se mide?", "steps": ["Cambia la forma del recipiente.", "Se mide el tiempo en horas hasta secarse."], "answer": "Cambia la forma del recipiente; se mide el tiempo en horas"},
        {"title": "Una predicción con «si»", "problem": "Escribe una predicción para la prueba del plato ancho y el vaso angosto.", "steps": ["El plato ancho tiene más superficie.", "Con más superficie escapan más partículas al aire."], "answer": "Si uso un plato ancho, entonces el agua se evaporará más rápido que en el vaso angosto"},
    ],
    mistakes=[
        {"wrong": "Cambiar la forma del recipiente y la cantidad de agua al mismo tiempo.", "why": "No se puede saber cuál variable causó la diferencia.", "fix": "Cambia solo una condición y mantén igual lo demás."},
        {"wrong": "Predecir sin decir por qué.", "why": "Se parece más a adivinar.", "fix": "Usa lo que sabes: más superficie, más evaporación."},
    ],
    tiers={
        "recovery": [
            ex("En una prueba justa, ¿cuántas condiciones se cambian a propósito: una o muchas?", "Una", "Así se sabe qué causó el resultado."),
            ex("Las condiciones que se mantienen iguales en una prueba, ¿cómo se llaman?", "Constantes", "No cambian durante la prueba."),
            ex("¿Cuál es una pregunta comprobable: «¿Qué recipiente es más lindo?» o «¿En cuántos minutos se derrite un hielo en un plato?»?", "¿En cuántos minutos se derrite un hielo en un plato?", "Se responde midiendo tiempo."),
        ],
        "understand": [
            ex("Dos platos con 50 mL de agua: uno en la sombra y otro al sol. ¿Qué variable cambia?", "El lugar (sombra o sol)", "Es lo único que se modifica a propósito."),
            ex("En esa prueba, ¿qué variable se mide: el color del plato o el tiempo que demora en secarse el agua?", "El tiempo que demora en secarse el agua", "Es el resultado que se mide."),
            ex("Predicción: «Si el agua está al sol, entonces se evaporará más rápido». ¿En qué idea se apoya: más calor acelera el cambio o el agua sabe cuándo secarse?", "Más calor acelera el cambio", "Se apoya en una idea con evidencia."),
        ],
        "apply": [
            arith("Una persona mide que 50 mL de agua demoran 9 horas en secarse en un vaso y 3 horas en un plato. ¿Cuántas horas menos demora en el plato?", "9-3", "Se resta el menor tiempo al mayor.", " horas"),
            ex("Un grupo quiere probar si más calor acelera la fusión de un hielo. Pone un hielo en un plato en la sombra y otro de igual tamaño en un plato al sol. ¿Cuál es una constante: el tamaño del hielo o el lugar?", "El tamaño del hielo", "El lugar es lo que cambia; el tamaño se mantiene igual."),
            arith("Una bandeja de hielo tiene 10 espacios. Se llena cada uno con 30 mL de agua para estudiar la solidificación. ¿Cuántos mL de agua se usan en total?", "10*30", "Se multiplican los espacios por los mL de cada uno.", " mL"),
        ],
        "reason": [
            ex("Sofía mide el tiempo de secado de un plato con 50 mL de agua y de un vaso con 100 mL. Dice que el plato es más rápido por ser más ancho. ¿Qué error tiene su prueba?", "Cambió también la cantidad de agua", "No es una prueba justa."),
            ex("La predicción de Tomás fue «el hielo grande se derrite en el mismo tiempo que el pequeño». Midió 20 minutos para el grande y 8 para el pequeño. ¿Qué debe cambiar?", "La predicción", "Los datos son la evidencia."),
        ],
        "challenge": [
            ex("Dos platos iguales con 40 mL de agua: uno cerca de una ventana abierta con viento y otro en un lugar sin viento. ¿Qué predicción es razonable?", "Si hay viento, entonces el agua se evaporará más rápido", "El viento se lleva el vapor de la superficie y acelera la evaporación."),
            arith("En la prueba justa del plato ancho, el agua se secó en 4 horas. En el vaso angosto, el agua demoró el triple. ¿Cuántas horas demoró en el vaso?", "4*3", "El triple de 4 es 4 por 3.", " horas"),
        ],
    },
    context=[ex("Una persona de tu casa quiere que la ropa se seque más rápido. ¿Qué dos condiciones puede cambiar para acelerar la evaporación: más calor y más viento, o más sombra y menos viento?", "Más calor y más viento", "Ambos aceleran la evaporación.")],
    selfcheck=[
        ex("¿Qué es una constante en una prueba?", "Una condición que se mantiene igual", "No cambia durante la prueba."),
        ex("¿Qué variable se mide cuando comparamos qué hielo se derrite primero?", "El tiempo", "Es el dato que usamos para comparar."),
        ex("Un hielo se derritió en 7 minutos y tu predicción decía 15. ¿Qué número es la evidencia y se queda igual?", "7 minutos", "El dato medido no se cambia; lo que se corrige es la predicción."),
    ],
    open_task=task(
        "Diseña una prueba justa en papel: quieres saber si un hielo se derrite más rápido en un plato con agua tibia de la llave o en un plato seco, ambos a la sombra y con hielos del mismo tamaño. Escribe: la pregunta comprobable, la variable que cambia, la variable que mides, dos constantes y una predicción con «Si…, entonces…».",
        "Pregunta: ¿se derrite más rápido en agua tibia? Cambia: agua tibia o plato seco. Mido: minutos. Constantes: tamaño del hielo y lugar. Predicción: si el hielo está en agua tibia, entonces se derretirá más rápido.",
        ["pregunta comprobable", "variable que cambia y variable que se mide", "dos constantes y una predicción con «si»"],
        ["diseño escrito"],
        ["cambiar dos condiciones", "no nombrar la variable que se mide"],
        "Pregunta qué cambiaría en su diseño si no tuviera reloj.",
    ),
    reinforce="Escribe otra pregunta comprobable sobre evaporación y nombra su variable que cambia y la que se mide.",
    extend="Averigua con una persona de tu casa si la ropa se seca más rápido extendida o doblada, y explícalo con la superficie.",
)

# ================================================================ OA 13, clase 3
register(
    OA13, 3,
    materials="Papel y lápiz. Dibuja los esquemas con flechas.",
    use="Aprenderé a representar los cambios de estado con un esquema de flechas y a explicarlos con partículas y energía. Sirve para saber cuándo una sustancia gana calor y cuándo lo pierde.",
    prior=["Sé nombrar los seis cambios de estado.", "Conozco el modelo de partículas de los tres estados."],
    explain=[
        "Un esquema de flechas es un modelo de los cambios de estado. De sólido a líquido va la fusión; de líquido a gas va la evaporación (o ebullición); de sólido a gas, la sublimación. Las flechas de regreso son la solidificación (de líquido a sólido) y la condensación (de gas a líquido). De gas directo a sólido se llama sublimación inversa.",
        "Los cambios que van hacia un estado más movido necesitan que la sustancia gane calor: fusión, evaporación, ebullición y sublimación. Los que van hacia un estado menos movido necesitan que pierda calor: solidificación, condensación y sublimación inversa. Con partículas: al ganar calor se mueven más y se separan; al perder calor se mueven menos y se juntan.",
        "El modelo tiene límites. El esquema muestra solo los estados y las flechas, pero no cuánto calor hace falta, ni cuánto tiempo, ni que en un cambio también pueden mezclarse dos estados al mismo tiempo (por ejemplo, agua con hielo). Por eso se completa con mediciones.",
    ],
    vocab=[("calor", "energía que pasa de un cuerpo más caliente a uno más frío"), ("ganar calor", "recibir energía de afuera"), ("perder calor", "entregar energía al entorno"), ("esquema", "dibujo simple con palabras y flechas"), ("energía", "capacidad de producir cambios")],
    worked=[
        {"title": "Leer el esquema", "problem": "Un esquema muestra: hielo → agua → vapor. ¿Qué dos cambios hay, en orden, y si la sustancia gana o pierde calor?", "steps": ["De hielo a agua: fusión.", "De agua a vapor: evaporación o ebullición.", "En ambos pasos va hacia un estado más movido: gana calor."], "answer": "Fusión y evaporación (o ebullición); gana calor en ambos"},
        {"title": "Explicar con partículas", "problem": "¿Qué pasa con las partículas del agua cuando se solidifica?", "steps": ["Para solidificar, el agua pierde calor.", "Sus partículas se mueven menos y se ordenan juntas."], "answer": "Se mueven menos y se ordenan"},
    ],
    mistakes=[
        {"wrong": "Decir que en la condensación el gas gana calor.", "why": "Se confunde la dirección del cambio.", "fix": "En la condensación, el gas pierde calor y pasa a líquido."},
        {"wrong": "Creer que el esquema de flechas muestra cuánto tarda cada cambio.", "why": "Se pide al modelo algo que no representa.", "fix": "Para saber el tiempo y la cantidad de calor se necesitan mediciones."},
    ],
    tiers={
        "recovery": [
            ex("En el esquema de flechas, ¿qué cambio va de líquido a sólido?", "Solidificación", "El agua se hace hielo."),
            ex("¿La fusión necesita que la sustancia gane o pierda calor?", "Gane calor", "Para derretirse hace falta calor."),
            ex("¿La condensación necesita que el vapor gane o pierda calor?", "Pierda calor", "Al enfriarse, el vapor pasa a líquido."),
        ],
        "understand": [
            ex("Con el modelo de partículas, ¿qué pasa con las partículas cuando una sustancia gana calor: se mueven más o menos?", "Se mueven más", "Más energía significa más movimiento."),
            ex("¿Cuál cambio va de sólido directo a gas sin pasar por líquido?", "Sublimación", "Salta el estado líquido."),
            ex("Un esquema dice que el vapor se enfría y se hace gotas. ¿Qué cambio es?", "Condensación", "Pasa de gas a líquido al perder calor."),
        ],
        "apply": [
            ex("Un hielo (A) se derrite en un plato hasta ser agua (B) y esa agua se seca lentamente al aire, sin burbujas (C). Escribe los nombres de los dos cambios: de A a B y de B a C.", "Fusión y evaporación", "El agua se seca lentamente en la superficie, sin burbujas."),
            ex("En un esquema, los seis cambios son fusión, solidificación, evaporación, ebullición, condensación y sublimación. ¿Cuántos de ellos necesitan ganar calor?", "4", "Ganan calor la fusión, la evaporación, la ebullición y la sublimación."),
            ex("Ordena de más a menos movimiento de partículas: hielo, vapor, agua líquida.", "Vapor, agua líquida, hielo", "El gas se mueve más que el líquido y este más que el sólido."),
        ],
        "reason": [
            ex("Un compañero dice que la ebullición ocurre porque el agua pierde calor. ¿Qué parte del esquema muestra que se equivoca?", "Que de líquido a gas va con ganancia de calor", "La ebullición necesita calor."),
            ex("En un congelador, el agua líquida se hace hielo. Con partículas, ¿qué cambió: la rapidez de movimiento o el número de partículas?", "La rapidez de movimiento", "Las partículas se mueven menos, pero el número no cambia."),
        ],
        "challenge": [
            ex("Un vaso con hielo tiene gotas afuera. Usa el esquema: ¿qué gas pasó a líquido y por qué perdió calor?", "El vapor de agua del aire, que perdió calor al tocar el vaso frío", "El vaso frío enfría el vapor del aire y este se condensa."),
            arith("En un esquema con 12 partículas de gas, 4 se condensan y se hacen líquido. ¿Cuántas siguen siendo gas?", "12-4", "Se restan las que cambiaron de estado.", " partículas"),
        ],
    },
    context=[ex("Al ducharte con agua caliente, el espejo del baño se empaña. ¿Qué cambio de estado ocurrió con el vapor al tocar el espejo más frío?", "Condensación", "El vapor perdió calor y pasó a líquido.")],
    selfcheck=[
        ex("¿Qué cambio de estado necesita ganar calor: fusión o solidificación?", "Fusión", "Es sólido a líquido."),
        ex("Al perder calor, las partículas, ¿se mueven más o menos?", "Menos", "Hay menos energía."),
        ex("¿Un esquema de flechas muestra cuánto tarda cada cambio?", "No", "Solo muestra qué cambia."),
    ],
    open_task=task(
        "Dibuja un esquema con tres cajas (SÓLIDO, LÍQUIDO, GAS) y flechas dobles entre ellas. Rotula cada flecha con el nombre del cambio de estado y con «gana calor» o «pierde calor». Escribe debajo una frase con partículas para uno de los cambios y una limitación de tu esquema.",
        "Sólido a líquido: fusión, gana calor. Líquido a sólido: solidificación, pierde calor. Frase: al ganar calor, las partículas se mueven más. Limitación: el esquema no muestra cuánto calor hace falta.",
        ["tres estados y todas las flechas", "nombre y calor correctos en cada flecha", "frase con partículas y limitación"],
        ["esquema completo"],
        ["invertir ganar y perder calor", "olvidar la sublimación"],
        "Pregunta qué cambios de tu esquema ocurren en una cocina.",
    ),
    reinforce="Agrega al esquema la sublimación y la flecha de regreso desde gas a sólido, y escribe si gana o pierde calor.",
    extend="Averigua con una persona de tu casa dónde ve condensación en la cocina o el baño y qué la provoca.",
)

# ================================================================ OA 13, clase 4
register(
    OA13, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno.",
    use="Aprenderé a comparar resultados de experimentos de cambios de estado con un criterio justo. Sirve para concluir con datos y no con opiniones.",
    prior=["Sé qué es una prueba justa.", "Sé calcular diferencias y comparar tiempos."],
    explain=[
        "Para comparar resultados de dos pruebas necesitamos un criterio. En el cambio de estado, un criterio útil es el tiempo: el cambio que ocurre en menos minutos es más rápido. Antes de comparar hay que revisar que la prueba sea justa: misma cantidad de sustancia, mismas condiciones y una sola variable que cambia.",
        "Veamos un ejemplo. Tres cubos de hielo de 30 g cada uno se derriten en distintas condiciones: en un plato a la sombra demora 25 minutos, en un plato al sol demora 12 minutos y en un plato con agua tibia de la llave demora 6 minutos. Con el criterio del tiempo, el más rápido es el del agua tibia, porque tiene el menor tiempo.",
        "Para concluir con evidencia, cita dos datos y la condición que cambió. Por ejemplo: «El hielo en agua tibia demoró 6 minutos y el de la sombra 25; la diferencia son 19 minutos». También hay que decir una limitación: se usaron pocos hielos y el reloj mide en minutos y no en segundos.",
    ],
    vocab=[("criterio de comparación", "regla que se usa para decidir cuál resultado es mejor o más rápido"), ("diferencia", "resultado de restar dos datos"), ("evidencia", "dato que apoya una conclusión"), ("limitación", "aspecto que puede afectar la confianza en el resultado"), ("repetir la prueba", "hacer de nuevo el experimento para ver si da algo parecido")],
    worked=[
        {"title": "Comparar tiempos", "problem": "Con los datos de la explicación, ¿cuántos minutos más demora el hielo de la sombra (25 minutos) que el del sol (12 minutos)?", "steps": ["Ambos tiempos están en minutos.", "Resto: 25 − 12 = 13."], "answer": "13 minutos más"},
        {"title": "Revisar si la prueba es justa", "problem": "Un hielo de 30 g está al sol y otro de 60 g está en agua tibia. Una persona dice que el agua tibia es más rápida. ¿La prueba es justa?", "steps": ["Cambian dos condiciones: el tamaño del hielo y el lugar.", "No se sabe cuál causó la diferencia."], "answer": "No es justa, porque cambian dos condiciones"},
    ],
    mistakes=[
        {"wrong": "Concluir sin citar ningún dato.", "why": "Se piensa que la conclusión es una opinión.", "fix": "Cita al menos dos datos medidos."},
        {"wrong": "Comparar pruebas donde cambian varias condiciones.", "why": "No se sabe qué causó la diferencia.", "fix": "Revisa primero que la prueba sea justa."},
    ],
    tiers={
        "recovery": [
            ex("Con el criterio «menos minutos = más rápido», ¿qué hielo es más rápido: el que demora 8 minutos o el que demora 15?", "El que demora 8 minutos", "Menos minutos significa más rápido."),
            ex("Para que una prueba sea justa, ¿cuántas variables deben cambiar?", "Una", "Así se identifica la causa."),
            ex("Un hielo tarda 10 minutos y otro 20. ¿Cuál tarda más?", "El de 20 minutos", "20 es mayor que 10."),
        ],
        "understand": [
            ex("En la prueba de los tres hielos de 30 g, ¿qué condición cambió: el tamaño del hielo o el lugar donde se puso?", "El lugar donde se puso", "Los hielos eran del mismo tamaño."),
            ex("¿Cuál es una conclusión con evidencia: (a) «El agua tibia es mejor» o (b) «El hielo en agua tibia demoró 6 minutos y el de la sombra 25»?", "(b)", "Cita datos medidos."),
            ex("¿Qué es una limitación en un experimento: un dato que afecta la confianza en el resultado o un resultado inventado?", "Un dato que afecta la confianza en el resultado", "Por ejemplo, haber hecho una sola prueba."),
        ],
        "apply": [
            arith("Un hielo en la sombra demora 30 minutos y otro en agua tibia 9 minutos. ¿Cuántos minutos de diferencia hay?", "30-9", "Se resta el menor tiempo al mayor.", " minutos"),
            arith("Un plato ancho seca el agua en 4 horas y un vaso angosto en 12 horas. ¿Cuántas veces más demora el vaso?", "12//4", "Se divide el tiempo mayor por el menor.", " veces"),
            arith("Tres pruebas con el mismo hielo en el sol dieron 11, 12 y 13 minutos. ¿Cuántos minutos suman en total?", "11+12+13", "Se suman los tres tiempos.", " minutos"),
        ],
        "reason": [
            ex("Luisa dice que el sol derrite más rápido el hielo porque un hielo demoró 12 minutos y el otro 25. Revisa su prueba: los hielos eran de 30 g y de 60 g. ¿Es válida su conclusión?", "No", "Cambia el tamaño además del lugar."),
            ex("Un equipo midió con un reloj que marca solo minutos y sin decimales. ¿Cuál es una limitación de sus datos?", "No miden segundos, así que las diferencias pequeñas no se ven", "El instrumento limita la precisión."),
        ],
        "challenge": [
            ex("En tres pruebas con un mismo hielo al sol se obtuvieron 14, 15 y 16 minutos. Otro equipo con un hielo parecido obtuvo 15 minutos. ¿Qué indican los datos: que los resultados son parecidos o muy distintos?", "Parecidos", "Todos están entre 14 y 16."),
            ex("El equipo A midió 6 minutos con un hielo en agua tibia. El equipo B midió 18 minutos con un hielo igual en la sombra. B dice: «Mi hielo demoró el triple». ¿Tiene razón?", "Sí", "18 minutos es 3 veces 6 minutos."),
        ],
    },
    context=[ex("En una casa se prueba qué plato seca más rápido el agua: uno ancho de 6 horas o uno angosto de 15 horas. Una persona dice que el angosto es más rápido. ¿Qué dato muestra que se equivoca?", "El ancho demoró 6 horas y el angosto 15", "Menos horas es más rápido.")],
    selfcheck=[
        ex("¿Qué criterio usamos para decidir qué cambio fue más rápido?", "El tiempo", "Menos tiempo significa más rápido."),
        ex("Una conclusión con evidencia, ¿cita datos o solo opiniones?", "Datos", "La evidencia son los datos."),
        ex("Si cambian dos condiciones, ¿la prueba es justa?", "No", "No se puede saber cuál causó el resultado."),
    ],
    open_task=task(
        "Con estos datos de tres pruebas (hielos de 30 g: sombra 28 minutos, sol 15 minutos, agua tibia 8 minutos), escribe una conclusión de dos oraciones que cite dos datos y una diferencia, y una limitación del experimento. Luego dibuja una tabla de dos columnas (condición, minutos).",
        "El hielo al sol demoró 15 minutos y el de la sombra 28; la diferencia es de 13 minutos. Limitación: se hizo una sola prueba por condición.",
        ["conclusión que cita dos datos", "diferencia calculada", "limitación escrita"],
        ["tabla", "conclusión"],
        ["concluir sin datos", "calcular mal la diferencia"],
        "Pregunta cuántas pruebas más haría para estar más segura o seguro.",
    ),
    reinforce="Invéntate dos datos de tiempo para otros dos hielos y escribe cuál fue más rápido y por cuántos minutos.",
    extend="Averigua con una persona de tu casa si un charco se seca más rápido al sol o a la sombra y registra lo que observas.",
)
