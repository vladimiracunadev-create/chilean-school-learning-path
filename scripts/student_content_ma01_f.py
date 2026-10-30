"""Student material for 1.º básico Matemática, OA 19 (recolección de datos) y OA 20 (pictogramas)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA19, OA20 = "MA01 OA 19", "MA01 OA 20"


# ---------------------------------------------------------------- OA 19
register(
    OA19, 1,
    materials="Una hoja, lápiz y las preguntas escritas en cada ejercicio; sin materiales especiales.",
    use="Aprenderé a hacer preguntas cuyas respuestas se puedan contar. Sirve para averiguar cosas sobre mi curso, mi familia o mi barrio.",
    prior=["Sé hacer preguntas.", "Sé contar hasta 20."],
    explain=[
        "Una pregunta estadística es una pregunta que se responde juntando datos de varias personas o cosas. Por ejemplo: «¿Qué fruta prefieres: manzana, plátano o naranja?». Cada persona da una respuesta, y después las contamos.",
        "No sirven las preguntas que tienen una sola respuesta para todos, como «¿Cuántos días tiene una semana?», porque no cambia. Tampoco las que se responden con una frase larga, porque es difícil contarlas. Una buena pregunta tiene pocas opciones claras.",
        "Para que los datos sirvan, escribe la pregunta con las opciones: «¿Cuál es tu mascota favorita: perro, gato o pez?». Así todos eligen una de las opciones y se pueden contar sin confundirse.",
    ],
    vocab=[("dato", "una respuesta que se registra"), ("pregunta", "lo que quiero saber"), ("opciones", "las respuestas posibles"), ("favorito", "el que más me gusta"), ("contar", "ver cuántos eligieron cada opción")],
    worked=[
        {"title": "Una buena pregunta", "problem": "¿Es buena la pregunta «¿Qué fruta prefieres: manzana, plátano o naranja?» para juntar datos?", "steps": ["Tiene opciones claras.", "Cada persona puede elegir una.", "Se puede contar cuántas eligieron cada una."], "answer": "Sí, es una buena pregunta"},
        {"title": "Una pregunta que no sirve", "problem": "¿Sirve la pregunta «¿Cuántos días tiene una semana?»?", "steps": ["La respuesta es 7 para todos.", "No hay datos que contar."], "answer": "No sirve para juntar datos"},
    ],
    mistakes=[
        {"wrong": "Hacer preguntas con una respuesta larga.", "why": "Es difícil contar respuestas distintas.", "fix": "Da pocas opciones claras."},
        {"wrong": "Hacer una pregunta sin opciones.", "why": "Cada persona responde algo distinto.", "fix": "Escribe las opciones en la pregunta."},
    ],
    tiers={
        "recovery": [ex("«¿Cuál es tu color favorito: rojo, azul o verde?» ¿Tiene opciones?", "Sí", "Menciona tres colores."), ex("¿Cuántas opciones tiene «¿Prefieres perro o gato?»?", "2", "Perro y gato."), ex("¿Sirve «¿Cuántos dedos tiene una mano?» para juntar datos?", "No", "Todos responden 5.")],
        "understand": [
            ex("¿Qué es un dato?", "Una respuesta que se registra", "Se puede contar."),
            ex("¿Por qué conviene dar opciones?", "Para que las respuestas se puedan contar", "Todos eligen entre las mismas."),
            ex("¿Qué tipo de pregunta sirve para juntar datos?", "Una con pocas opciones claras", "Cambia entre las personas."),
        ],
        "apply": [
            ex("Escribe una pregunta con tres opciones sobre juegos favoritos.", "Por ejemplo: ¿Qué juego prefieres: pelota, cuerda o escondida?", "Tiene tres opciones."),
            ex("Escribe una pregunta con dos opciones sobre mascotas.", "Por ejemplo: ¿Qué mascota prefieres: perro o gato?", "Tiene dos opciones."),
            ex("Convierte «¿Qué te gusta comer?» en una pregunta con opciones.", "Por ejemplo: ¿Qué prefieres: pizza, arroz o ensalada?", "Ahora tiene opciones claras."),
        ],
        "reason": [
            ex("Ana preguntó «¿Cómo te llamas?» a todo su curso. ¿Sirve para contar?", "No; cada persona tiene un nombre distinto", "Las respuestas no se agrupan."),
            ex("¿Por qué «¿Te gusta el helado: sí o no?» sirve?", "Porque tiene dos opciones que se pueden contar", "Se agrupan en sí y no."),
        ],
        "challenge": [
            ex("Escribe una pregunta sobre el día de la semana favorito con tres opciones.", "Por ejemplo: ¿Qué día prefieres: viernes, sábado o domingo?", "Las opciones agrupan las respuestas."),
            ex("Si 12 niños responden una pregunta con 3 opciones, ¿puede cada opción tener 4 respuestas?", "Sí", "4 + 4 + 4 = 12."),
        ],
    },
    context=[ex("La profesora quiere saber qué actividad prefiere el curso en el recreo: fútbol, saltar la cuerda o conversar. Escribe la pregunta.", "¿Qué actividad prefieres en el recreo: fútbol, saltar la cuerda o conversar?", "Tiene tres opciones.")],
    selfcheck=[ex("¿Una pregunta con opciones es útil para contar?", "Sí", "Se agrupan las respuestas."), ex("Escribe una pregunta con dos opciones de colores.", "Por ejemplo: ¿Prefieres rojo o azul?", "La pregunta ofrece dos opciones."), ex("¿Qué se hace con los datos?", "Se cuentan", "Se ve cuántos eligieron cada opción.")],
    open_task=task("Escribe tres preguntas con opciones para tu curso o tu familia: una sobre comida, una sobre juegos y otra sobre animales. Anota las opciones de cada una.", "1) ¿Qué prefieres: pizza, arroz o ensalada? 2) ¿Qué juego prefieres: pelota, cuerda o escondida? 3) ¿Qué animal prefieres: perro, gato o pez?", ["tres preguntas con opciones", "temas pedidos", "opciones claras"], ["tres preguntas"], ["preguntas sin opciones", "opciones confusas"], "Pide que otra persona la responda para ver si se entiende."),
    reinforce="Escribe una pregunta con opciones sobre tu familia.",
    extend="Reescribe una pregunta mal hecha para que tenga opciones claras.",
)

register(
    OA19, 2,
    materials="Una lista de cinco personas (nombres) y una hoja para registrar; los datos están escritos en cada ejercicio.",
    use="Aprenderé a registrar una respuesta por persona y a no olvidar ni repetir. Sirve para tener un registro ordenado.",
    prior=["Sé hacer preguntas con opciones.", "Sé contar hasta 20."],
    explain=[
        "Para recolectar datos, pregunta lo mismo a cada persona y anota una sola respuesta por persona. Si preguntas a 10 personas, debes tener 10 respuestas. Si tienes 11, repetiste una; si tienes 9, olvidaste una.",
        "Una forma de registrar es una lista con el nombre y la respuesta: Ana, manzana; Beto, plátano. Otra forma es usar bloques o fichas: un bloque por cada respuesta, del color de la opción. Así cada persona es un bloque.",
        "Al terminar, revisa: ¿preguntaste a todos? ¿Cada persona tiene una sola respuesta? Cuenta el total de respuestas y compáralo con el número de personas. Deben coincidir.",
    ],
    vocab=[("recolectar", "juntar datos"), ("registrar", "anotar lo que se averigua"), ("una por persona", "cada persona da una respuesta"), ("total", "cuántas respuestas hay en todo"), ("repetir", "contar dos veces la misma respuesta")],
    worked=[
        {"title": "Registrar", "problem": "Ana, manzana; Beto, plátano; Carla, manzana. Registra con bloques.", "steps": ["Un bloque por persona.", "Manzana: 2 bloques.", "Plátano: 1 bloque."], "answer": "Manzana 2, plátano 1"},
        {"title": "Revisar", "problem": "Pregunté a 5 personas y tengo 6 respuestas. ¿Qué pasó?", "steps": ["Debería haber 5.", "Hay 6, entonces repetí una."], "answer": "Se repitió una respuesta"},
    ],
    mistakes=[
        {"wrong": "Anotar dos respuestas de la misma persona.", "why": "Se cuenta dos veces a la misma persona.", "fix": "Anota sólo una por persona."},
        {"wrong": "No revisar el total.", "why": "Se confía en el registro.", "fix": "Compara respuestas con personas."},
    ],
    tiers={
        "recovery": [ex("Ana: perro. Beto: gato. Carla: perro. ¿Cuántas respuestas hay?", "3", "Una por persona."), ex("Ana: rojo. Beto: azul. ¿Cuántos bloques necesito?", "2", "Un bloque por persona."), ex("Pregunté a 4 personas. ¿Cuántas respuestas debo tener?", "4", "Una por persona.")],
        "understand": [
            ex("¿Cuántas respuestas anoto por persona?", "Una", "Cada persona da una respuesta."),
            ex("Si pregunté a 8 y tengo 7 respuestas, ¿qué pasó?", "Olvidé una", "Falta una respuesta."),
            ex("¿Qué es un bloque en el registro?", "Una respuesta de una persona", "Un bloque por persona."),
        ],
        "apply": [
            ex("Ana: manzana. Beto: plátano. Carla: manzana. Dani: manzana. ¿Cuántos eligieron manzana?", "3", "Ana, Carla y Dani."),
            ex("Ana: manzana. Beto: plátano. Carla: manzana. Dani: manzana. ¿Cuántos eligieron plátano?", "1", "Sólo Beto eligió plátano."),
            arith("Ana, Beto, Carla y Dani respondieron. Luego respondió Eva. ¿Cuántas respuestas hay?", "4+1", "Una más por cada persona."),
        ],
        "reason": [
            ex("Luis preguntó a 6 y tiene 8 respuestas. ¿Qué pudo hacer mal?", "Contar respuestas repetidas", "Debería haber 6."),
            ex("¿Por qué conviene usar un bloque por persona?", "Para no olvidar ni repetir", "Cada bloque es una persona."),
        ],
        "challenge": [
            ex("De 10 personas, 6 eligen A y el resto B. ¿Cuántas eligen B?", "4", "10 − 6 = 4."),
            ex("En un curso de 20, 12 prefieren perro. ¿Cuántos no prefieren perro?", "8", "20 − 12 = 8."),
        ],
    },
    context=[ex("En un grupo, 3 niños eligen pelota y 2 eligen cuerda. ¿Cuántos niños respondieron?", "5", "3 + 2 = 5.")],
    selfcheck=[ex("Pregunté a 7 y tengo 7 respuestas. ¿Está bien?", "Sí", "Las respuestas coinciden con las personas."), ex("¿Cuántos bloques para 5 respuestas?", "5", "Un bloque por respuesta."), ex("¿Qué debo revisar al final?", "Que las respuestas sean igual a las personas", "Para no olvidar ni repetir.")],
    open_task=task("Pregunta a cinco personas de tu casa o curso «¿Prefieres perro o gato?». Registra cada respuesta con un bloque (cuadrado de color) y escribe cuántos hay de cada uno y el total.", "Perro: 3 bloques. Gato: 2 bloques. Total: 5 personas y 5 respuestas.", ["5 respuestas", "un bloque por persona", "cuenta cada opción"], ["bloques", "conteo", "total"], ["más o menos de 5", "respuestas repetidas"], "Pide contar los bloques y comparar con las personas."),
    reinforce="Registra con fichas las respuestas de tu familia sobre una pregunta.",
    extend="Haz el mismo registro con otra pregunta y compara los resultados.",
)

register(
    OA19, 3,
    materials="Un registro de bloques y marcas descrito en cada ejercicio; lápiz.",
    use="Aprenderé a pasar los datos de bloques a una tabla de conteo con marcas. Sirve para organizar muchas respuestas con orden.",
    prior=["Sé registrar con bloques.", "Sé contar de 5 en 5."],
    explain=[
        "Una tabla de conteo tiene una fila por opción y una marca por cada respuesta. Se escribe una raya (|) por cada persona. Después de cuatro rayas, la quinta cruza las cuatro: ||||. Así se cuenta de 5 en 5.",
        "Por ejemplo, 7 respuestas a «perro» se anotan con un grupo de cinco más dos rayas. Al terminar, escribe en otra columna el número total de cada opción. La suma de todos los totales debe ser el número de personas.",
        "La tabla es más ordenada que una lista y es más fácil de contar. Revisa siempre que la suma de totales sea igual al número de personas que respondieron.",
    ],
    vocab=[("tabla de conteo", "tabla con marcas para contar"), ("marca", "una raya por respuesta"), ("grupo de cinco", "cuatro rayas cruzadas por una quinta"), ("total", "cuántas marcas hay en una fila"), ("fila", "línea horizontal de la tabla")],
    worked=[
        {"title": "Pasar de bloques a marcas", "problem": "Bloques: perro 6, gato 3. Haz la tabla de conteo.", "steps": ["Perro: un grupo de cinco y una raya.", "Gato: tres rayas.", "Totales: 6 y 3."], "answer": "Perro 6, gato 3"},
        {"title": "Revisar", "problem": "La tabla dice perro 6, gato 3. ¿Cuántas personas respondieron?", "steps": ["Sumo los totales.", "6 + 3 = 9."], "answer": "9 personas"},
    ],
    mistakes=[
        {"wrong": "Olvidar cruzar la quinta raya.", "why": "No se agrupa de a cinco.", "fix": "La quinta raya cruza las cuatro anteriores."},
        {"wrong": "Contar mal los grupos de cinco.", "why": "Se cuenta como 1.", "fix": "Cada grupo de cinco vale 5."},
    ],
    tiers={
        "recovery": [ex("¿Cuántas rayas tiene un grupo de cinco?", "5", "Cuatro y una que las cruza."), ex("Anota 3 respuestas con rayas.", "|||", "Una raya por respuesta."), ex("Anota 5 respuestas con rayas.", "||||/ (cuatro rayas y una que las cruza)", "Es un grupo de cinco.")],
        "understand": [
            ex("¿Para qué sirve el grupo de cinco?", "Para contar de 5 en 5", "Es más rápido."),
            ex("¿Cuántas marcas hay en un grupo de cinco más tres rayas?", "8", "5 + 3 = 8."),
            ex("¿Cómo comprobar que la tabla está completa?", "Sumo los totales y comparo con las personas", "Los totales deben coincidir con las personas."),
        ],
        "apply": [
            arith("Una tabla tiene un grupo de cinco y dos rayas. ¿Cuántas respuestas hay?", "5+2", "Cinco más dos."),
            arith("Una tabla tiene dos grupos de cinco. ¿Cuántas respuestas hay?", "5+5", "Dos grupos de cinco."),
            arith("Totales: manzana 7, plátano 4, naranja 5. ¿Cuántas personas respondieron?", "7+4+5", "La suma de los totales."),
        ],
        "reason": [
            ex("Pía anotó 4 respuestas con un grupo de cinco. ¿Qué error cometió?", "Hizo una raya de más; son 4 rayas", "Un grupo de cinco tiene 5."),
            ex("Una tabla dice 10 personas pero los totales suman 11. ¿Qué pasó?", "Se anotó una respuesta de más", "Los totales deben igualar a las personas."),
        ],
        "challenge": [
            ex("En una tabla, manzana tiene 12 marcas y plátano 8. ¿Cuántos grupos de cinco completos tiene manzana?", "2", "10 de 12 son dos grupos y quedan 2 rayas."),
            ex("¿Cuántas rayas sueltas quedan en plátano (8) después de formar grupos de cinco?", "3", "5 + 3 = 8."),
        ],
    },
    context=[arith("En un curso, 9 niños eligen fútbol, 6 eligen cuerda y 5 eligen conversar. ¿Cuántos niños respondieron?", "9+6+5", "Se suman los totales de cada opción.")],
    selfcheck=[arith("Un grupo de cinco y 4 rayas, ¿cuántas respuestas?", "5+4", "Cinco más cuatro."), ex("¿Qué fila tiene más: 8 o 5 marcas?", "8", "8 es mayor."), arith("Totales 4 y 6, ¿cuántas personas?", "4+6", "Se suman.")],
    open_task=task("Con los datos «Ana: A, Beto: B, Carla: A, Dani: A, Eva: B, Fer: A, Gabi: B, Hugo: A», haz una tabla de conteo con marcas para las opciones A y B y escribe los totales y la suma.", "A tiene 5 marcas (un grupo de cinco cruzado) y B tiene 3 marcas (|||). Totales: A 5, B 3. Suma: 5 + 3 = 8 personas.", ["marcas correctas", "totales", "suma que coincide con las 8 personas"], ["tabla", "totales", "suma"], ["contar mal", "no cruzar la quinta raya"], "Pide verificar que 5 + 3 = 8."),
    reinforce="Haz una tabla de conteo con 10 marcas sobre tu pregunta favorita.",
    extend="Haz una tabla con tres opciones y 15 respuestas.",
)

register(
    OA19, 4,
    materials="Datos ya registrados en tablas y bloques, descritos en cada ejercicio.",
    use="Aprenderé a responder una pregunta usando los datos como evidencia. Sirve para tomar decisiones con información real.",
    prior=["Sé hacer una tabla de conteo.", "Sé comparar números."],
    explain=[
        "Responder con evidencia significa usar los datos para contestar y decir cuáles datos lo demuestran. Si la pregunta es «¿Qué fruta es la más elegida?», miras la tabla y encuentras la fila con el total mayor.",
        "Una respuesta con evidencia dice qué es y cuánto: «La manzana es la más elegida, con 7 votos, más que el plátano, que tuvo 4». Así otra persona puede comprobar mirando la tabla.",
        "No debes decir más de lo que muestran los datos: si sólo preguntaste a un curso, no puedes decir que «a todos los niños de Chile» les gusta algo. Limítate a tu grupo.",
    ],
    vocab=[("evidencia", "datos que prueban una respuesta"), ("más elegida", "la opción con mayor total"), ("menos elegida", "la opción con menor total"), ("diferencia", "cuántos más tiene una que otra"), ("conclusión", "lo que digo después de mirar los datos")],
    worked=[
        {"title": "Responder con evidencia", "problem": "Manzana 7, plátano 4, naranja 5. ¿Cuál es la más elegida?", "steps": ["Comparo los totales.", "7 es el mayor.", "La manzana es la más elegida con 7."], "answer": "La manzana, con 7"},
        {"title": "No decir de más", "problem": "Preguntaste a tu curso (20 niños). ¿Puedes decir que a todos los niños de Chile les gusta la manzana?", "steps": ["Sólo preguntaste a 20.", "Los datos no hablan de todos los niños."], "answer": "No, sólo puedo hablar de mi curso"},
    ],
    mistakes=[
        {"wrong": "Responder sin citar los datos.", "why": "Se da una opinión.", "fix": "Cita el número que lo prueba."},
        {"wrong": "Generalizar a todas las personas.", "why": "Se piensa que el grupo representa a todos.", "fix": "Habla sólo del grupo que preguntaste."},
    ],
    tiers={
        "recovery": [ex("Manzana 7, plátano 4. ¿Cuál es la más elegida?", "La manzana", "7 es mayor que 4."), ex("Perro 8, gato 5. ¿Cuál es la menos elegida?", "El gato", "5 es menor que 8."), ex("Rojo 6, azul 6. ¿Cuál es la más elegida?", "Empatan", "Los totales son iguales.")],
        "understand": [
            ex("¿Qué es evidencia?", "Datos que prueban una respuesta", "Los números de la tabla."),
            ex("¿Qué debe tener una respuesta con evidencia?", "Qué es la más elegida y cuánto", "Cita los números."),
            ex("¿Puedo hablar de todo Chile si pregunté a mi curso?", "No", "Los datos son sólo de mi curso."),
        ],
        "apply": [
            ex("Totales: pelota 9, cuerda 6, escondida 4. Escribe la respuesta con evidencia sobre cuál es la más elegida.", "La pelota es la más elegida, con 9", "Cita el número."),
            arith("Totales: pelota 9, cuerda 6. ¿Cuántos más eligieron pelota que cuerda?", "9-6", "La diferencia."),
            arith("Totales: pelota 9, cuerda 6, escondida 4. ¿Cuántas personas respondieron?", "9+6+4", "Se suman."),
        ],
        "reason": [
            ex("Mateo dice que la manzana es la favorita de todos los niños de Chile. ¿Qué error comete?", "Preguntó sólo a su curso", "No puede generalizar."),
            ex("Dos opciones tienen el mismo total. ¿Qué respondes a «¿cuál es la más elegida?»", "Hay un empate", "No hay una sola más elegida."),
        ],
        "challenge": [
            ex("Totales: A 8, B 5, C 7. Ordena de la más a la menos elegida.", "A, C, B", "8 > 7 > 5."),
            ex("Si se suman 2 votos a B (que tenía 5), ¿cuál sigue siendo la más elegida: A (8), B o C (7)?", "A, con 8", "B pasaría a 7 y A sigue teniendo más."),
        ],
    },
    context=[ex("En un curso de 20 niños: 11 prefieren fútbol, 6 prefieren cuerda y 3 prefieren conversar. ¿Cuál es la actividad más elegida y cuántos más la eligieron que la cuerda?", "El fútbol; 5 más", "11 − 6 = 5.")],
    selfcheck=[ex("Perro 10, gato 4. ¿Cuántos más eligieron perro?", "6", "10 − 4 = 6."), ex("¿Qué es una conclusión?", "Lo que digo mirando los datos", "Se apoya en la evidencia."), ex("¿Debo citar números en mi respuesta?", "Sí", "Son la evidencia.")],
    open_task=task("Con los datos «Perro 9, gato 6, pez 3», responde por escrito: ¿qué mascota es la más elegida? ¿Y la menos? ¿Cuántas personas respondieron? Cita los números y escribe una conclusión que no diga más de lo que muestran los datos.", "El perro es la más elegida (9) y el pez la menos (3). Respondieron 9 + 6 + 3 = 18 personas. Conclusión: en este grupo, el perro fue la mascota preferida.", ["cita los números", "responde las tres preguntas", "no generaliza"], ["respuesta escrita", "conclusión"], ["no citar datos", "generalizar"], "Pide releer la tabla y comprobar cada afirmación."),
    reinforce="Responde una pregunta con evidencia usando tus propios datos.",
    extend="Diseña una pregunta cuya respuesta pueda cambiar un compañero y explica cómo cambiaría la evidencia.",
)

# ---------------------------------------------------------------- OA 20
register(
    OA20, 1,
    materials="Un pictograma descrito con símbolos en cada ejercicio (cada ● representa una persona).",
    use="Aprenderé a leer un pictograma: un gráfico que usa dibujos para mostrar cantidades. Sirve para entender datos rápidamente.",
    prior=["Sé hacer tablas de conteo.", "Sé contar hasta 20."],
    explain=[
        "Un pictograma es un gráfico hecho con dibujos o símbolos. Cada símbolo representa una cantidad. Tiene un título, categorías (como frutas) y una clave que dice cuánto vale cada símbolo.",
        "Por ejemplo, en el pictograma «Frutas favoritas», la fila de manzana tiene ● ● ● ● ● ● ●: siete símbolos. Si la clave dice «● = 1 persona», entonces siete personas eligieron manzana. Para leerlo, cuenta los símbolos de cada fila.",
        "Para comparar, mira cuál fila tiene más símbolos: esa categoría fue la más elegida. Para encontrar el total, suma los símbolos de todas las filas.",
    ],
    vocab=[("pictograma", "gráfico hecho con símbolos"), ("categoría", "cada grupo del gráfico"), ("clave", "dice cuánto vale cada símbolo"), ("símbolo", "dibujo que representa una cantidad"), ("título", "dice de qué trata el gráfico")],
    worked=[
        {"title": "Leer una fila", "problem": "Manzana: ● ● ● ● ● ● ●. Clave: ● = 1 persona. ¿Cuántas personas eligieron manzana?", "steps": ["Cuento los símbolos: 7.", "Cada uno vale 1 persona.", "Son 7 personas."], "answer": "7 personas"},
        {"title": "Comparar filas", "problem": "Manzana ● ● ● ● ● ● ● y plátano ● ● ● ●. ¿Cuál tiene más?", "steps": ["Manzana: 7.", "Plátano: 4.", "7 > 4."], "answer": "Manzana"},
    ],
    mistakes=[
        {"wrong": "No mirar la clave.", "why": "Se supone que cada símbolo vale uno.", "fix": "Lee primero la clave."},
        {"wrong": "Contar mal los símbolos.", "why": "Se salta alguno.", "fix": "Tacha cada símbolo que cuentas."},
    ],
    tiers={
        "recovery": [ex("Fila: ● ● ●. Clave: ● = 1. ¿Cuánto vale?", "3", "Tres símbolos de uno."), ex("Fila: ● ● ● ● ●. Clave: ● = 1. ¿Cuánto vale?", "5", "Hay cinco símbolos en la fila."), ex("Fila: ●. Clave: ● = 1. ¿Cuánto vale?", "1", "Hay un solo símbolo en la fila.")],
        "understand": [
            ex("¿Para qué sirve la clave de un pictograma?", "Para saber cuánto vale cada símbolo", "Sin la clave no se lee bien."),
            ex("¿Qué dice el título?", "De qué trata el gráfico", "Es lo primero que se lee."),
            ex("¿Qué es una categoría?", "Cada grupo del gráfico", "Por ejemplo, cada fruta."),
        ],
        "apply": [
            ex("Perro: ● ● ● ● ● ● ● ●. Gato: ● ● ● ●. ¿Cuántos eligieron perro y cuántos gato?", "Perro 8, gato 4", "Se cuentan los símbolos de cada fila."),
            arith("Perro tiene 8 símbolos y gato 4. ¿Cuántos más eligieron perro?", "8-4", "Diferencia de los símbolos."),
            arith("Perro tiene 8 símbolos, gato 4 y pez 3. ¿Cuántas personas respondieron en total?", "8+4+3", "Se suman todos."),
        ],
        "reason": [
            ex("Ana cuenta 5 símbolos en la fila de gato y dice que 5 personas eligieron gato. ¿Qué debe revisar?", "La clave", "Si cada símbolo vale 1, está bien."),
            ex("¿Cómo sé cuál categoría es la más elegida?", "Es la fila con más símbolos", "Más símbolos es más personas."),
        ],
        "challenge": [
            ex("Hay filas con 6, 3 y 7 símbolos. ¿Cuál es la menos elegida y cuánto se diferencia de la más elegida?", "La de 3; 4 menos que la de 7", "7 − 3 = 4."),
            arith("Si la fila de pez crece en 2 símbolos y tenía 3, ¿cuántos tiene ahora?", "3+2", "Se suman 2."),
        ],
    },
    context=[arith("En el pictograma de «Juegos favoritos», pelota tiene 6 símbolos y cuerda 5. ¿Cuántos niños respondieron en total?", "6+5", "Se suman los símbolos de las dos filas.")],
    selfcheck=[ex("Fila: ● ● ● ● ● ●. Clave: ● = 1. ¿Cuánto vale?", "6", "Hay seis símbolos en la fila."), ex("¿Qué fila tiene más: 5 o 7 símbolos?", "La de 7", "7 > 5."), ex("¿Qué leo primero en un pictograma?", "El título y la clave", "Dicen qué muestra y cuánto vale.")],
    open_task=task("Observa este pictograma: Pelota ● ● ● ● ● ●; Cuerda ● ● ● ●; Escondida ● ● ● ●. Clave: ● = 1 niño. Escribe cuántos niños eligieron cada juego, cuál es el más elegido y cuántos niños respondieron.", "Pelota 6, cuerda 4, escondida 4. El más elegido es la pelota. Respondieron 6 + 4 + 4 = 14 niños.", ["cuenta cada fila", "identifica la más elegida", "suma el total"], ["tres números", "frase", "total"], ["no leer la clave", "contar mal"], "Pide tachar cada símbolo al contarlo."),
    reinforce="Lee un pictograma del diario o de un libro y cuenta sus símbolos.",
    extend="Descubre cuántos símbolos más necesita la fila menor para igualar a la mayor.",
)

register(
    OA20, 2,
    materials="Pictogramas descritos en cada ejercicio con clave ● = 1.",
    use="Aprenderé a comparar categorías en un pictograma y a calcular cuántos más o cuántos menos hay. Sirve para sacar conclusiones de los datos.",
    prior=["Sé leer un pictograma.", "Sé restar hasta 20."],
    explain=[
        "Para comparar dos categorías, cuenta sus símbolos y mira cuál tiene más. Para saber cuántos más, resta: si manzana tiene 9 y naranja 5, manzana tiene 9 − 5 = 4 más. También puedes emparejar símbolo con símbolo y contar los que sobran.",
        "Para encontrar el total, suma todos los símbolos. Para saber cuántos menos tiene una categoría que otra, también restas y dices «tiene 4 menos». Así se responde cualquier pregunta de comparación.",
        "Escribe siempre la respuesta con una frase: «La manzana tiene 4 más que la naranja». Esa frase demuestra que entendiste el gráfico.",
    ],
    vocab=[("comparar", "decir cuál tiene más o menos"), ("cuántos más", "la diferencia"), ("total", "todos los símbolos juntos"), ("empate", "cuando dos categorías tienen lo mismo"), ("frase", "respuesta escrita completa")],
    worked=[
        {"title": "Cuántos más", "problem": "Manzana 9, naranja 5. ¿Cuántos más eligieron manzana?", "steps": ["Resto: 9 − 5.", "9 − 5 = 4.", "Escribo: la manzana tiene 4 más."], "answer": "4 más"},
        {"title": "Total", "problem": "Manzana 9, naranja 5, plátano 6. ¿Cuántos respondieron?", "steps": ["Sumo 9 + 5.", "14 + 6 = 20."], "answer": "20 personas"},
    ],
    mistakes=[
        {"wrong": "Sumar para saber cuántos más.", "why": "Se confunde juntar con comparar.", "fix": "Para cuántos más, resta."},
        {"wrong": "Responder sin frase.", "why": "Se da sólo un número.", "fix": "Escribe una frase completa."},
    ],
    tiers={
        "recovery": [arith("Perro 7, gato 4. ¿Cuántos más eligieron perro?", "7-4", "Se resta."), arith("Rojo 8, azul 3. ¿Cuántos menos eligieron azul?", "8-3", "Se resta."), arith("Pelota 5, cuerda 5. ¿Cuántos más eligieron pelota?", "5-5", "Si hay empate, no hay diferencia.")],
        "understand": [
            ex("¿Qué operación uso para cuántos más?", "Una resta", "Comparar cantidades se hace con resta."),
            ex("¿Qué operación uso para el total?", "Una suma", "Se juntan todos."),
            ex("Si dos categorías tienen lo mismo, ¿cuántos más tiene una?", "Cero", "Si hay empate, no hay diferencia."),
        ],
        "apply": [
            arith("Manzana 9, naranja 5, plátano 6. ¿Cuántos respondieron?", "9+5+6", "Se suman."),
            arith("Manzana 9, plátano 6. ¿Cuántos más eligieron manzana?", "9-6", "Se resta."),
            arith("Naranja 5, plátano 6. ¿Cuántos menos eligieron naranja?", "6-5", "Se resta."),
        ],
        "reason": [
            ex("Luis dice que 9 + 5 = 14 es cuántos más tiene manzana que naranja. ¿Qué error comete?", "Suma en vez de restar; son 4 más", "Más se calcula con resta."),
            ex("¿Por qué conviene escribir la respuesta en una frase?", "Porque muestra que entendí el gráfico", "Dice qué se compara."),
        ],
        "challenge": [
            ex("Manzana 9, naranja 5, plátano 6. Ordena de la más a la menos elegida.", "Manzana, plátano, naranja", "9 > 6 > 5."),
            ex("¿Cuántos símbolos debe agregar la naranja para igualar a la manzana?", "4", "9 − 5 = 4."),
        ],
    },
    context=[arith("En una fiesta, 8 niños eligen jugo y 5 eligen leche. ¿Cuántos niños más prefieren jugo?", "8-5", "Se resta.")],
    selfcheck=[arith("A 7 y B 3. ¿Cuántos más tiene A?", "7-3", "Se resta."), arith("A 7 y B 3. ¿Cuántos en total?", "7+3", "Se suma."), ex("¿Cómo respondo?", "Con una frase", "La frase completa muestra que entendí.")],
    open_task=task("Con el pictograma Pelota 7, Cuerda 4 y Escondida 6 (cada símbolo es un niño), escribe tres frases: cuántos más eligieron pelota que cuerda, cuántos menos eligieron cuerda que escondida y cuántos niños respondieron en total.", "Pelota tiene 3 más que cuerda (7 − 4). Cuerda tiene 2 menos que escondida (6 − 4). Respondieron 7 + 4 + 6 = 17 niños.", ["tres frases", "usa resta y suma", "resultados correctos"], ["tres frases"], ["sumar en vez de restar", "no escribir frase"], "Pide comprobar con símbolos emparejados."),
    reinforce="Compara dos filas de un pictograma con los dedos.",
    extend="Haz una pregunta nueva sobre el pictograma y respóndela.",
)

register(
    OA20, 3,
    materials="Objetos de tu casa (por ejemplo 3 tipos de botones o tapas) y una hoja para dibujar; los datos se anotan en el cuaderno.",
    use="Aprenderé a construir un pictograma a partir de objetos reales. Sirve para ordenar y mostrar cuántos hay de cada tipo.",
    prior=["Sé leer un pictograma.", "Sé contar y clasificar objetos."],
    explain=[
        "Para construir un pictograma desde objetos, primero clasifica: separa los objetos por tipo (por ejemplo, tapas rojas, azules y verdes). Cuenta cuántos hay de cada tipo.",
        "Luego dibuja el gráfico: escribe el título, dibuja una fila para cada tipo y pon un símbolo por cada objeto. Escribe la clave: «● = 1 tapa». Deja un espacio igual entre los símbolos para que se vea ordenado.",
        "Al final comprueba: la suma de símbolos debe ser el total de objetos. Si no, cuenta de nuevo. Después escribe dos frases que describan lo que muestra el pictograma.",
    ],
    vocab=[("clasificar", "separar por tipo"), ("fila", "línea con los símbolos de un tipo"), ("clave", "dice cuánto vale cada símbolo"), ("título", "nombre del gráfico"), ("comprobar", "revisar que todo coincida")],
    worked=[
        {"title": "Construir", "problem": "Hay 5 tapas rojas, 3 azules y 4 verdes. Construye el pictograma.", "steps": ["Título: «Tapas por color».", "Rojas: ● ● ● ● ●.", "Azules: ● ● ●.", "Verdes: ● ● ● ●.", "Clave: ● = 1 tapa."], "answer": "Rojas 5, azules 3, verdes 4"},
        {"title": "Comprobar", "problem": "¿Cuántas tapas hay en total?", "steps": ["5 + 3 + 4.", "5 + 3 = 8; 8 + 4 = 12."], "answer": "12"},
    ],
    mistakes=[
        {"wrong": "Olvidar la clave.", "why": "No se explica qué vale el símbolo.", "fix": "Siempre escribe la clave."},
        {"wrong": "Símbolos de distinto tamaño.", "why": "Se dibuja al apuro.", "fix": "Dibuja símbolos iguales y parejos."},
    ],
    tiers={
        "recovery": [ex("¿Qué debe tener un pictograma: título, filas y clave?", "Sí, las tres cosas", "Son las partes básicas."), ex("Clasifica: botón rojo, botón azul, botón rojo. ¿Cuántos rojos?", "2", "Hay dos rojos."), ex("¿Cuántos símbolos dibujo para 4 objetos si ● = 1?", "4", "Un símbolo por objeto.")],
        "understand": [
            ex("¿Qué es clasificar?", "Separar por tipo", "Cada grupo tiene el mismo tipo."),
            ex("¿Para qué sirve la clave?", "Para decir cuánto vale cada símbolo", "Sin clave no se lee."),
            ex("¿Cómo compruebo mi pictograma?", "Sumo los símbolos y comparo con los objetos", "Los totales deben coincidir con los objetos."),
        ],
        "apply": [
            ex("Hay 6 lápices rojos y 2 azules. Dibuja el pictograma.", "Rojos: ● ● ● ● ● ●; Azules: ● ●; clave ● = 1 lápiz", "Un símbolo por lápiz."),
            ex("Hay 3 galletas, 5 caramelos y 4 chocolates. Dibuja el pictograma.", "Galletas ●●●; caramelos ●●●●●; chocolates ●●●●; clave ● = 1", "Un símbolo por cada uno."),
            arith("¿Cuántos objetos hay en total: 3 galletas, 5 caramelos y 4 chocolates?", "3+5+4", "Se suman."),
        ],
        "reason": [
            ex("Pía dibujó 5 símbolos para 4 tapas verdes. ¿Qué error cometió?", "Dibujó uno de más", "Debe haber 4."),
            ex("¿Por qué conviene un título?", "Para saber de qué trata el gráfico", "Es la primera pista."),
        ],
        "challenge": [
            ex("Una fila de un pictograma tiene 6 símbolos y otra tiene 3 menos. ¿Cuántos símbolos tiene la otra?", "3", "6 − 3 = 3."),
            ex("Construye un pictograma para 10 objetos de 3 tipos distintos.", "Por ejemplo 5, 3 y 2", "5 + 3 + 2 = 10."),
        ],
    },
    context=[arith("Una profesora tiene 7 lápices, 4 gomas y 3 reglas. ¿Cuántos útiles son en total y cuántos símbolos dibujarías?", "7+4+3", "14 útiles y 14 símbolos.")],
    selfcheck=[ex("¿Cuántos símbolos para 6 objetos?", "6", "Uno por cada objeto."), ex("¿Qué escribo debajo del gráfico?", "La clave", "Dice cuánto vale cada símbolo."), ex("¿Qué hago primero con los objetos?", "Clasificarlos", "Separar por tipo.")],
    open_task=task("Junta 12 objetos de tu casa de tres tipos (por ejemplo botones, tapas y piedras). Clasifícalos, cuenta cuántos hay de cada tipo, dibuja el pictograma con título y clave y escribe dos frases sobre lo que muestra.", "Título: «Mis objetos». Botones ●●●●●, tapas ●●●●, piedras ●●●. Clave: ● = 1. Hay más botones que tapas. En total hay 12 objetos.", ["clasifica", "título y clave", "dos frases"], ["pictograma", "frases"], ["falta clave", "símbolos de más"], "Pide comparar con los objetos reales."),
    reinforce="Haz un pictograma con las prendas de tu ropa.",
    extend="Haz un pictograma donde cada símbolo vale 2 objetos.",
)

register(
    OA20, 4,
    materials="Una tabla de datos escrita en cada ejercicio (por ejemplo: perro 6, gato 4, pez 2); una hoja para dibujar.",
    use="Aprenderé a construir un pictograma a partir de una tabla de datos. Sirve para mostrar información ya registrada.",
    prior=["Sé construir un pictograma desde objetos.", "Sé leer una tabla."],
    explain=[
        "Si ya tienes una tabla con los totales, construir el pictograma es traducir números a símbolos. Para cada fila de la tabla dibujas tantos símbolos como indica el total. Si la tabla dice perro 6, dibujas seis símbolos.",
        "Elige un símbolo simple, como un círculo o un cuadrado, y úsalo igual en todas las filas. Escribe el título (de qué trata) y la clave («● = 1 persona»). Deja el mismo espacio entre símbolos.",
        "Comprueba que cada fila tenga tantos símbolos como el número de la tabla y que el total coincida. Así tu gráfico dice lo mismo que la tabla.",
    ],
    vocab=[("tabla de datos", "tabla con totales por categoría"), ("traducir", "pasar de números a símbolos"), ("símbolo", "dibujo que representa una cantidad"), ("coincidir", "ser igual"), ("total", "cuántos hay en cada categoría")],
    worked=[
        {"title": "De la tabla al pictograma", "problem": "Perro 6, gato 4, pez 2. Construye el pictograma.", "steps": ["Título: «Mascotas favoritas».", "Perro: ● ● ● ● ● ●.", "Gato: ● ● ● ●.", "Pez: ● ●.", "Clave: ● = 1 persona."], "answer": "Perro 6, gato 4, pez 2"},
        {"title": "Comprobar", "problem": "¿Coincide el total del gráfico con la tabla?", "steps": ["6 + 4 + 2 = 12 en el gráfico.", "La tabla suma 12.", "Las respuestas coinciden con las personas."], "answer": "Sí"},
    ],
    mistakes=[
        {"wrong": "Dibujar un símbolo distinto en cada fila.", "why": "No se mantiene una clave.", "fix": "Usa el mismo símbolo en todo el gráfico."},
        {"wrong": "No comprobar con la tabla.", "why": "Se confía en la primera cuenta.", "fix": "Compara cada fila con el número de la tabla."},
    ],
    tiers={
        "recovery": [ex("Tabla: perro 3. ¿Cuántos símbolos dibujas en la fila de perro si ● = 1?", "3", "Uno por cada unidad."), ex("Tabla: gato 5. ¿Cuántos símbolos dibujas?", "5", "Uno por cada unidad."), ex("Tabla: pez 0. ¿Cuántos símbolos dibujas?", "0", "Con cero no se dibuja ningún símbolo.")],
        "understand": [
            ex("¿Qué escribo en la clave?", "Cuánto vale cada símbolo", "Por ejemplo ● = 1 persona."),
            ex("¿Por qué uso el mismo símbolo en todas las filas?", "Para que se pueda comparar", "Todos valen lo mismo."),
            ex("¿Cómo comprobar que el gráfico dice lo mismo que la tabla?", "Comparar cada fila con el número", "Deben ser iguales."),
        ],
        "apply": [
            ex("Tabla: manzana 5, plátano 3, naranja 4. Dibuja el pictograma.", "Manzana ●●●●●; plátano ●●●; naranja ●●●●; clave ● = 1", "Un símbolo por número."),
            ex("Tabla: rojo 2, azul 6, verde 3. Dibuja el pictograma.", "Rojo ●●; azul ●●●●●●; verde ●●●; clave ● = 1", "Un símbolo por número."),
            arith("Tabla: manzana 5, plátano 3, naranja 4. ¿Cuántos símbolos habrá en total?", "5+3+4", "Se suman."),
        ],
        "reason": [
            ex("Ana dibujó 4 símbolos para plátano 3. ¿Qué error cometió?", "Dibujó uno de más", "Debe haber 3."),
            ex("¿Es lo mismo la tabla que el pictograma?", "Sí, muestran los mismos datos", "Cambia la forma."),
        ],
        "challenge": [
            ex("Tabla: A 10, B 4. ¿Cuántos símbolos más tiene la fila de A que la de B?", "6", "10 − 4 = 6."),
            ex("Con los datos A 10 y B 4, ¿cuántos símbolos hay en total?", "14", "10 + 4 = 14."),
        ],
    },
    context=[arith("Una escuela pidió: 8 paquetes de cuadernos, 5 de lápices y 3 de gomas. ¿Cuántos símbolos tiene el pictograma si ● = 1 paquete?", "8+5+3", "Un símbolo por cada paquete.")],
    selfcheck=[ex("Tabla: cuerda 6. ¿Cuántos símbolos?", "6", "Uno por unidad."), ex("¿Qué va al principio del gráfico?", "El título", "Dice de qué trata."), ex("¿Qué hay que comprobar al final?", "Que el gráfico coincida con la tabla", "Se revisa cada fila contra la tabla.")],
    open_task=task("Con la tabla «pelota 7, cuerda 5, escondida 3», construye un pictograma con título y clave. Comprueba cada fila con la tabla y escribe dos frases de lo que muestra.", "Título: «Juegos favoritos». Pelota ●●●●●●●; cuerda ●●●●●; escondida ●●●. Clave: ● = 1 niño. La pelota es la más elegida. Respondieron 15 niños.", ["traduce la tabla", "título y clave", "dos frases"], ["pictograma", "comprobación", "frases"], ["símbolos de más o de menos", "sin clave"], "Pide contar cada fila con el dedo."),
    reinforce="Convierte una tabla de tu cuaderno en un pictograma.",
    extend="Construye un pictograma donde cada símbolo vale 2.",
)

register(
    OA20, 5,
    materials="Una pregunta de investigación elegida por ti y una hoja para registrar; los pasos están descritos aquí.",
    use="Aprenderé a hacer una pequeña investigación completa: preguntar, recolectar, representar en un pictograma y comunicar lo que descubrí. Sirve para contar a otros lo que averigüé.",
    prior=["Sé hacer preguntas con opciones.", "Sé construir y leer pictogramas."],
    explain=[
        "Una investigación tiene cinco pasos. Primero, elige una pregunta con opciones y pregúntala a un grupo de personas, anotando una respuesta por persona. Segundo, haz una tabla de conteo. Tercero, construye un pictograma con título y clave.",
        "Cuarto, interpreta: ¿qué opción fue la más elegida? ¿Cuántos más que la menos elegida? ¿Cuántas personas respondieron? Escribe tus conclusiones en frases que citen los números del gráfico.",
        "Quinto, comunica. Muestra tu pictograma a otra persona y explícale qué descubriste. Dile también qué no puedes saber con tus datos, por ejemplo qué piensan personas a las que no preguntaste.",
    ],
    vocab=[("investigación", "proceso de preguntar y averiguar"), ("recolectar", "juntar datos"), ("representar", "mostrar en un gráfico"), ("interpretar", "decir qué significan los datos"), ("comunicar", "contarle a otros lo descubierto")],
    worked=[
        {"title": "Los cinco pasos", "problem": "Ordena los pasos: construir el pictograma, preguntar, hacer la tabla, comunicar, interpretar.", "steps": ["Primero preguntar.", "Luego hacer la tabla.", "Después construir el pictograma.", "Interpretar.", "Comunicar."], "answer": "Preguntar, tabla, pictograma, interpretar, comunicar"},
        {"title": "Una conclusión", "problem": "Perro 6, gato 4, pez 2. Escribe una conclusión.", "steps": ["El perro es el más elegido.", "6 − 2 = 4 más que el pez.", "Respondieron 12 personas."], "answer": "El perro fue el más elegido (6), 4 más que el pez; respondieron 12 personas"},
    ],
    mistakes=[
        {"wrong": "Saltarse el paso de la tabla.", "why": "Se pasa directo al gráfico.", "fix": "Primero ordena los datos en una tabla."},
        {"wrong": "Concluir sobre personas a las que no se preguntó.", "why": "Se generaliza.", "fix": "Habla sólo del grupo que respondió."},
    ],
    tiers={
        "recovery": [ex("¿Cuál es el primer paso de una investigación?", "Hacer una pregunta con opciones", "De ahí salen los datos."), ex("¿Qué hago después de recolectar las respuestas?", "Hago una tabla de conteo", "Ordena los datos."), ex("¿Qué se construye con la tabla?", "Un pictograma", "Muestra los datos.")],
        "understand": [
            ex("¿Qué significa interpretar?", "Decir qué significan los datos", "Se responde la pregunta."),
            ex("¿Por qué comunicar?", "Para que otros sepan lo que descubrí", "Así se comparte lo descubierto."),
            ex("¿A quién puedo atribuir mis conclusiones?", "Sólo al grupo que respondió", "No a otros."),
        ],
        "apply": [
            ex("Pregunta a 5 personas «¿Prefieres perro o gato?» y anota sus respuestas con rayas.", "Por ejemplo: perro |||, gato ||", "Una raya por persona."),
            arith("En tu investigación, 3 prefieren perro y 2 prefieren gato. ¿Cuántas personas respondieron?", "3+2", "Se suman."),
            arith("En tu investigación, 3 prefieren perro y 2 prefieren gato. ¿Cuántas más prefirieron perro?", "3-2", "Se resta."),
        ],
        "reason": [
            ex("Ema dice que a todo Chile le gustan los perros porque en su curso ganaron. ¿Qué error comete?", "Generaliza; sólo habla de su curso", "Los datos son de su grupo."),
            ex("¿Por qué conviene hacer la tabla antes del pictograma?", "Para tener los totales ordenados", "Se traduce de números a símbolos."),
        ],
        "challenge": [
            ex("Si tu pictograma tiene 8, 5 y 2 símbolos, ¿cuántas personas respondieron y cuál es la diferencia entre la mayor y la menor?", "15 personas; 6 de diferencia", "8 + 5 + 2 = 15 y 8 − 2 = 6."),
            ex("Escribe una conclusión con evidencia para 8, 5 y 2.", "La opción de 8 fue la más elegida, 6 más que la de 2", "Cita los números."),
        ],
    },
    context=[ex("Un curso quiere elegir una excursión: plaza, museo o parque. Si 9 votan plaza, 6 museo y 5 parque, ¿cuál se elige y cuántos votaron?", "La plaza; 20 votaron", "9 + 6 + 5 = 20.")],
    selfcheck=[ex("¿Cuántos pasos tiene la investigación del cuaderno?", "5", "Preguntar, tabla, pictograma, interpretar y comunicar."), ex("¿Qué debe tener el pictograma?", "Título y clave", "Es lo mínimo."), ex("¿Qué hago al final?", "Comunicar", "Cuento lo que descubrí.")],
    open_task=task("Haz tu propia investigación: elige una pregunta con tres opciones, pregunta a 10 personas, haz la tabla de conteo, construye el pictograma con título y clave, escribe tres frases de conclusión con números y cuéntaselo a alguien.", "Pregunta: ¿Qué fruta prefieres: manzana, plátano o naranja? Tabla: manzana 5, plátano 3, naranja 2. Pictograma: ●●●●● / ●●● / ●● (● = 1 persona). Conclusiones: La manzana fue la más elegida (5). La naranja tuvo 3 menos. Respondieron 10 personas.", ["cumple los cinco pasos", "pictograma con título y clave", "tres frases con números"], ["tabla", "pictograma", "frases"], ["saltarse un paso", "generalizar"], "Pide presentarlo a otra persona y recoger una pregunta."),
    reinforce="Repite tu investigación con otro grupo de personas y compara.",
    extend="Haz una segunda pregunta y compara los dos pictogramas.",
)
