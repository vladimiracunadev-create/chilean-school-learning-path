"""Student material for 2.º básico Matemática, OA 19 (medición de longitudes) y OA 20 (datos de juegos con monedas y dados)."""
from __future__ import annotations

from collections import Counter

from student_content_ma02_g import task
from student_lessons import arith, ex, register

OA19, OA20 = "MA02 OA 19", "MA02 OA 20"


def tally(n: int) -> str:
    """Tally marks: four bars and a crossed bar make five."""
    return " ".join(["||||/"] * (n // 5) + (["|" * (n % 5)] if n % 5 else [])) or "(nada)"


def sym(symbol: str, n: int) -> str:
    return " ".join([symbol] * n) if n else "(nada)"


# ================================================================ OA 19
register(
    OA19, 1,
    materials="Papel y lápiz. Si quieres practicar, clips iguales o fichas iguales. Todas las medidas de los ejercicios ya están escritas.",
    use="Aprenderé a medir un largo repitiendo una misma unidad, sin dejar huecos ni encimar. Sirve para comparar objetos y decir cuánto miden.",
    prior=["Sé comparar largo: más largo, más corto.", "Sé contar hasta 50."],
    explain=[
        "Medir es decir cuánto mide algo usando una unidad. Una unidad puede ser un clip, una ficha o un borrador. Para medir, pones la misma unidad una tras otra, desde un extremo hasta el otro.",
        "Hay tres reglas. Las unidades deben ser todas iguales. No debe haber huecos entre ellas. Tampoco deben quedar encimadas una sobre otra. Al final, cuentas cuántas unidades usaste.",
        "El resultado siempre lleva un número y una unidad. Un libro puede medir 9 clips. Si sólo dices 9, no se sabe qué mediste. Además, si dos personas usan unidades distintas, no pueden comparar sus números.",
    ],
    vocab=[("medir", "decir cuánto mide algo con una unidad"), ("unidad", "algo que se repite para medir, como un clip"), ("longitud", "largo de un objeto"), ("hueco", "espacio vacío entre unidades"), ("extremo", "el principio o el final de lo que se mide")],
    worked=[
        {"title": "Medir con clips", "problem": "Cubres un libro con clips iguales, desde un extremo al otro, sin huecos. Usas 9 clips. ¿Cuánto mide el libro?", "steps": ["Pongo los clips uno tras otro.", "No dejo huecos ni los encimo.", "Cuento los clips: 9.", "Escribo el número y la unidad."], "answer": "9 clips"},
        {"title": "Comparar con la misma unidad", "problem": "Una tira mide 12 fichas y otra mide 8 fichas. ¿Cuál es más larga y por cuánto?", "steps": ["Las dos usan la misma unidad: fichas.", "12 es mayor que 8, entonces la primera es más larga.", "La diferencia es 12 − 8 = 4."], "answer": "La primera, por 4 fichas"},
    ],
    mistakes=[
        {"wrong": "Escribir que el libro mide «9» sin decir la unidad.", "why": "Falta la unidad que se usó.", "fix": "Escribe número y unidad: 9 clips."},
        {"wrong": "Dejar un hueco entre dos clips y contar igual.", "why": "El largo medido es menor que el real.", "fix": "Pon los clips pegados, sin huecos ni encimados."},
    ],
    tiers={
        "recovery": [
            ex("Mides un lápiz con 7 clips iguales, sin huecos. ¿Cómo escribes el resultado?", "7 clips", "Se escribe el número y la unidad."),
            ex("Un cuaderno mide 10 fichas y un libro mide 6 fichas. ¿Cuál es más largo?", "El cuaderno", "10 fichas es más que 6 fichas, con la misma unidad."),
            ex("¿Deben ser iguales las unidades que usas para medir un objeto?", "Sí", "Si no son iguales, el resultado no es confiable."),
        ],
        "understand": [
            ex("¿Qué dos datos lleva siempre una medida?", "Un número y una unidad", "Sin la unidad no se sabe qué se mide."),
            ex("¿Por qué no debe haber huecos entre las unidades?", "Porque el largo medido sería menor que el real", "Un hueco no se cuenta."),
            ex("Medir una mesa con clips es más lento que medirla con baldosas iguales y grandes. ¿Por qué?", "Porque necesitas muchos más clips que baldosas", "Una unidad pequeña se repite más veces."),
        ],
        "apply": [
            arith("Una tira mide 14 fichas y otra mide 9 fichas. ¿Cuántas fichas más mide la primera?", "14-9", "Con la misma unidad se resta."),
            arith("Un cuaderno mide 8 clips de largo y una regla mide 15 clips. Si los pones uno tras otro, ¿cuántos clips miden en total?", "8+15", "Se suman las dos medidas con la misma unidad."),
            ex("Ana midió una cinta y obtuvo 20 clips. Beto midió la misma cinta con borradores y obtuvo 5. ¿Pueden comparar sus números?", "No; usaron unidades distintas", "Un clip y un borrador no miden lo mismo."),
        ],
        "reason": [
            ex("Lalo dice que su lápiz mide 12, pero no dice la unidad. ¿Qué falta?", "La unidad, por ejemplo clips", "El número solo no dice qué se midió."),
            ex("Sara midió un libro con 6 clips, dejando huecos entre ellos. ¿Su resultado es mayor o menor que el largo verdadero?", "Menor; los huecos no se contaron", "Con huecos se cubre el largo con menos clips de los necesarios."),
        ],
        "challenge": [
            ex("Un pizarrón mide 20 palmos de Camila y 16 palmos de Pedro. ¿Quién tiene el palmo más largo?", "Pedro", "Con un palmo más largo se necesitan menos palmos: 16 es menor que 20."),
            ex("Una cuerda mide 18 clips. Necesitas dos cuerdas iguales. ¿Cuántos clips miden las dos juntas?", "36 clips", "18 + 18 = 36."),
        ],
    },
    context=[arith("Dos niños midieron la misma mesa con fichas iguales. Un niño obtuvo 24 fichas y otro obtuvo 19 fichas con las mismas fichas. ¿Cuántas fichas más obtuvo el primero?", "24-19", "Con la misma unidad se puede restar.")],
    selfcheck=[
        ex("¿Se pueden dejar huecos al medir con clips?", "No", "Los huecos hacen que el resultado quede mal."),
        ex("¿Qué número y unidad escribes si usaste 11 fichas?", "11 fichas", "Se escribe el número y el nombre de la unidad."),
        ex("Una cinta mide 15 clips y otra 9 clips. ¿Cuál es más corta?", "La de 9 clips", "9 es menor que 15."),
    ],
    open_task=task(
        "Mide con clips iguales (o fichas iguales) dos objetos de tu casa, como un lápiz y una tarjeta. Anota cada medida con su unidad. Si no tienes clips, usa estos datos: el lápiz mide 7 clips y la tarjeta mide 4 clips. Escribe cuál es más largo, por cuánto, y explica cómo pusiste los clips.",
        "El lápiz mide 7 clips y la tarjeta 4 clips. El lápiz es más largo por 3 clips (7 − 4). Puse los clips uno tras otro, sin huecos ni encimados, desde el extremo del objeto.",
        ["escribe número y unidad", "compara con una resta", "explica cómo puso las unidades", "usa la misma unidad en los dos objetos"],
        ["medidas escritas", "comparación", "explicación"],
        ["no escribir la unidad", "dejar huecos o encimar"],
        "Pide repetir la medición mostrando dónde empieza el primer clip. Reconoce cuando explica la regla de no dejar huecos.",
    ),
    reinforce="Mide el largo de tu cama con tus pasos y anota el número y la unidad.",
    extend="Mide la misma tira con clips y con fichas. Escribe qué unidad necesitó más repeticiones y por qué.",
)

register(
    OA19, 2,
    materials="Regla de 30 cm (o la regla dibujada en el cuaderno) y lápiz. Las lecturas están descritas en cada ejercicio.",
    use="Aprenderé a medir en centímetros con una regla, alineando el cero. Sirve para saber cuántos centímetros mide un lápiz, un cuaderno o una hoja.",
    prior=["Sé medir con unidades como clips.", "Sé contar hasta 30."],
    explain=[
        "El centímetro es una unidad de longitud y se escribe cm. Una regla tiene marcas numeradas: 0, 1, 2, 3 y así. Cada espacio entre dos marcas mide 1 cm.",
        "Para medir, pon el 0 de la regla justo en un extremo del objeto. Luego mira el número que queda en el otro extremo. Si un lápiz va desde 0 hasta 14, mide 14 cm.",
        "A veces la regla tiene un borde antes del cero, y no sirve para medir. Siempre empieza en la marca 0. Si no puedes empezar en 0, resta: un objeto que va de 3 a 12 mide 12 − 3 = 9 cm.",
    ],
    vocab=[("centímetro (cm)", "unidad de longitud de una regla"), ("regla", "instrumento con marcas para medir"), ("cero", "la marca desde donde se empieza a medir"), ("marca", "raya con un número en la regla"), ("extremo", "el principio o el final del objeto")],
    worked=[
        {"title": "Alinear el cero", "problem": "Un lápiz se pone con su punta en el 0 de la regla y su otro extremo queda en la marca 14. ¿Cuánto mide?", "steps": ["Empiezo en el 0.", "Leo el número del otro extremo: 14.", "Escribo el número con la unidad."], "answer": "14 cm"},
        {"title": "Cuando no se empieza en cero", "problem": "Una cinta va de la marca 1 a la marca 15 de la regla. ¿Cuánto mide?", "steps": ["No empieza en 0, empieza en 1.", "Calculo la diferencia: 15 − 1.", "15 − 1 = 14."], "answer": "14 cm"},
    ],
    mistakes=[
        {"wrong": "Decir que una cinta que va de 1 a 15 mide 15 cm.", "why": "Empezó en 1 y no en 0.", "fix": "Resta el inicio al final: 15 − 1 = 14 cm."},
        {"wrong": "Escribir sólo «14» sin cm.", "why": "Falta la unidad.", "fix": "Escribe 14 cm."},
    ],
    tiers={
        "recovery": [
            ex("Un lápiz empieza en el 0 y termina en la marca 12. ¿Cuánto mide?", "12 cm", "Se lee la marca final."),
            ex("Una tarjeta empieza en el 0 y termina en la marca 9. ¿Cuánto mide?", "9 cm", "Se lee la marca final."),
            ex("¿En qué marca de la regla se empieza a medir?", "En el 0", "El cero es el punto de partida."),
        ],
        "understand": [
            ex("¿Cuánto mide el espacio entre dos marcas seguidas de la regla?", "1 cm", "Cada espacio es un centímetro."),
            ex("¿Cómo se escribe «centímetros» en forma corta?", "cm", "Es la abreviatura."),
            ex("¿Para qué se alinea el cero con un extremo del objeto?", "Para leer la medida en la otra marca", "Así el número final es el largo."),
        ],
        "apply": [
            arith("Una cinta va de la marca 3 a la marca 11. ¿Cuántos centímetros mide?", "11-3", "Se resta la marca inicial a la final."),
            arith("Un cuaderno va de la marca 0 a la marca 21 y un lápiz de 0 a 15. ¿Cuántos centímetros más largo es el cuaderno?", "21-15", "Se resta la medida del lápiz a la del cuaderno."),
            ex("Dibuja en tu cuaderno un segmento de 8 cm. ¿Entre qué marcas lo pones, si empiezas en 0?", "Entre el 0 y el 8", "Una línea de 8 cm termina en la marca 8."),
        ],
        "reason": [
            ex("Marta puso su lápiz de 2 a 13 y dice que mide 13 cm. ¿Qué error comete?", "Empezó en 2, no en 0; mide 11 cm", "13 − 2 = 11."),
            ex("Una regla está rota y su borde empieza en la marca 3. Lucas dice que puede medir poniendo el objeto en el borde y leyendo. ¿Qué debe hacer?", "Restar 3 al número final", "El objeto empieza en 3, no en 0."),
        ],
        "challenge": [
            ex("Un lápiz mide 15 cm. Lo ponemos con la punta en la marca 4. ¿En qué marca termina?", "En la marca 19", "4 + 15 = 19."),
            ex("Dos tiras, una de 7 cm y otra de 5 cm, se ponen una tras otra. ¿Cuántos centímetros miden juntas?", "12 cm", "7 + 5 = 12."),
        ],
    },
    context=[arith("Una cinta para regalo va de la marca 2 a la marca 17 en la regla. ¿Cuántos centímetros mide?", "17-2", "Se resta el inicio al final.")],
    selfcheck=[
        ex("¿Dónde pones el 0 de la regla?", "En el extremo del objeto", "Así lees el largo."),
        ex("Un clip va de 0 a 3. ¿Cuánto mide?", "3 cm", "Se lee la marca final."),
        ex("Una goma va de 5 a 10. ¿Cuánto mide?", "5 cm", "10 − 5 = 5."),
    ],
    open_task=task(
        "Dibuja en tu cuaderno un segmento de 8 cm con regla, empezando desde la marca 0. Luego mide un lápiz (o usa este dato: el lápiz va desde la marca 0 hasta la marca 17). Escribe cuánto mide cada uno y dónde empezaste a medir.",
        "El segmento mide 8 cm porque empecé en 0 y terminé en 8. El lápiz mide 17 cm porque va de 0 a 17. Hice las dos medidas empezando desde el 0.",
        ["dibuja un segmento de 8 cm", "dice dónde empezó a medir", "escribe la medida del lápiz con cm", "alinea el cero"],
        ["segmento dibujado", "medidas escritas"],
        ["empezar a medir en 1", "no escribir la unidad"],
        "Pide mostrar con la regla dónde está el 0. Reconoce cuando explica de dónde empezó.",
    ),
    reinforce="Mide con la regla tu goma, tu lápiz y tu sacapuntas. Anota las tres medidas en cm.",
    extend="Mide tres objetos largos de tu mochila y ordénalos del más corto al más largo.",
)

register(
    OA19, 3,
    materials="Papel y lápiz. Los objetos y sus medidas están descritos en los ejercicios. Una regla de 30 cm y una cinta de 1 metro ayudan, pero no son obligatorias.",
    use="Aprenderé a elegir si conviene medir en centímetros o en metros. Sirve para escoger la unidad adecuada: un lápiz no se mide como una sala.",
    prior=["Sé medir en centímetros con regla.", "Sé que un objeto largo necesita una unidad grande."],
    explain=[
        "El metro es otra unidad de longitud y se escribe m. Un metro es más largo que un centímetro. Un metro tiene 100 cm. La cinta métrica y la huincha miden en metros y centímetros.",
        "Los objetos pequeños se miden en centímetros: un lápiz, un borrador o un cuaderno. Los objetos grandes se miden en metros: una sala, una puerta o una cancha. Si mides una sala en centímetros, el número queda enorme.",
        "Antes de medir, piensa qué unidad conviene. Mide en cm lo que cabe en tu mano o en tu mesa. Mide en m lo que es tan largo como tu cama o más.",
    ],
    vocab=[("metro (m)", "unidad de longitud más larga que el centímetro"), ("centímetro (cm)", "unidad corta de longitud"), ("cinta métrica", "cinta con marcas para medir en cm y m"), ("conviene", "es la mejor opción"), ("estimar", "decir un valor aproximado antes de medir")],
    worked=[
        {"title": "Elegir la unidad de un lápiz", "problem": "¿Mides un lápiz en cm o en m?", "steps": ["Un lápiz cabe en tu mano.", "Es un objeto pequeño.", "Un metro sería demasiado grande."], "answer": "En cm"},
        {"title": "Elegir la unidad de una puerta", "problem": "¿Mides el alto de una puerta en cm o en m? Estima el número.", "steps": ["Una puerta es más alta que un niño.", "Mide cerca de 2 metros.", "Medirla en cm daría un número muy grande."], "answer": "En m; cerca de 2 m"},
    ],
    mistakes=[
        {"wrong": "Medir el largo de la sala en cm y decir que mide 800.", "why": "La unidad es muy pequeña para un largo tan grande.", "fix": "Para largos grandes usa metros: 8 m."},
        {"wrong": "Decir que un lápiz mide 15 m.", "why": "Se confunde la unidad con una más grande.", "fix": "Un lápiz mide cerca de 15 cm, no 15 m."},
    ],
    tiers={
        "recovery": [
            ex("¿Medirías un borrador en cm o en m?", "En cm", "Un borrador es pequeño."),
            ex("¿Medirías el largo de una cancha de fútbol en cm o en m?", "En m", "Una cancha es muy larga."),
            ex("¿Qué unidad es más larga: el cm o el m?", "El m", "Un metro tiene 100 cm."),
        ],
        "understand": [
            ex("¿Cuántos centímetros tiene un metro?", "100", "Un metro equivale a 100 cm."),
            ex("¿Qué es mejor para medir una sala de clases: una regla de 30 cm o una cinta de 5 m?", "La cinta de 5 m", "La regla debería usarse muchas veces."),
            ex("¿Por qué es mejor medir una mesa en m que en clips?", "Porque el metro es una unidad estándar que todos usan", "El metro mide lo mismo para todas las personas."),
        ],
        "apply": [
            ex("Elige cm o m: el largo de tu cuaderno.", "cm", "Un cuaderno es pequeño."),
            ex("Elige cm o m: el largo del patio del colegio.", "m", "Un patio es grande."),
            ex("Elige cm o m: el ancho de una puerta.", "cm", "Una puerta mide cerca de 80 cm de ancho."),
        ],
        "reason": [
            ex("Tomás dice que el largo de su pieza es 4 cm y Ana dice que es 4 m. ¿Quién da una medida razonable?", "Ana; 4 cm cabrían en la mano", "Una pieza mide varios metros, no unos pocos centímetros."),
            ex("Laura dice que su lápiz mide 18 m. ¿Es razonable?", "No; mide cerca de 18 cm", "Dieciocho metros es más que el largo de una sala."),
        ],
        "challenge": [
            ex("Una huincha de 1 m llega hasta la marca 100. Pablo midió una cuerda y quedó justo en esa marca. ¿Cuántos metros mide la cuerda?", "1 m", "La marca 100 cm es el final de 1 metro."),
            ex("Una pared mide 5 m y otra mide 2 m. ¿Cuántos metros miden entre las dos?", "7 m", "5 + 2 = 7."),
        ],
    },
    context=[ex("Para saber cuánta cinta de adorno necesitas para envolver un regalo pequeño, ¿conviene medir en cm o en m?", "En cm", "Un regalo pequeño mide pocos centímetros.")],
    selfcheck=[
        ex("¿Cuántos cm tiene 1 m?", "100", "Es la equivalencia entre las dos unidades."),
        ex("¿Una mesa se mide mejor en cm o en m?", "En m", "Una mesa mide cerca de 1 m."),
        ex("¿Un sacapuntas se mide mejor en cm o en m?", "En cm", "Es un objeto pequeño."),
    ],
    open_task=task(
        "Mira esta lista: lápiz, sala de clases, pasillo del colegio, goma de borrar, cancha de baby fútbol, hoja de cuaderno. Escribe para cada una si la medirías en cm o en m, y estima su medida con un número y una unidad. Ejemplo para guiarte: un cuaderno mide cerca de 25 cm.",
        "Lápiz: cm, cerca de 17 cm. Sala: m, cerca de 8 m. Pasillo: m, cerca de 15 m. Goma: cm, cerca de 4 cm. Cancha de baby fútbol: m, cerca de 30 m. Hoja: cm, cerca de 28 cm.",
        ["elige la unidad para cada objeto", "estima con número y unidad", "explica que los objetos grandes usan m", "estimaciones razonables"],
        ["tabla de objetos y unidades", "estimaciones"],
        ["usar cm para la cancha", "estimar el lápiz en metros"],
        "Pide comparar con un objeto que se conoce. Reconoce las estimaciones razonables.",
    ),
    reinforce="Elige cinco objetos de tu casa y di si los medirías en cm o en m.",
    extend="Mide tu pieza con pasos y estima cuántos metros mide. Luego mide con una huincha si puedes.",
)

register(
    OA19, 4,
    materials="Papel y lápiz. Los objetos con sus estimaciones y medidas están escritos en los ejercicios.",
    use="Aprenderé a estimar una medida, medirla y ver si mi estimación fue razonable. Sirve para detectar errores en una medición.",
    prior=["Sé medir en cm con regla.", "Sé elegir entre cm y m."],
    explain=[
        "Estimar es decir cuánto crees que mide algo antes de medir. No tiene que ser exacto, pero debe ser razonable. Si estimas el largo de una mesa, puedes pensar en 100 cm (1 m), porque cabe en tus brazos abiertos.",
        "Después mides con la regla o la huincha. Compara tu estimación con la medida. Si medida y estimación son parecidas, estimaste bien. Si no, quizás hubo un error al medir.",
        "Por ejemplo, estimas una mesa en 100 cm y mides 120 cm. Está cerca. En cambio, si midieras 12 m, sería poco razonable: una mesa no es tan larga como una sala. Siempre di el resultado con número y unidad.",
    ],
    vocab=[("estimar", "decir una medida aproximada antes de medir"), ("razonable", "que tiene sentido para ese objeto"), ("comparar", "decir cuál es más largo o más corto"), ("medida", "resultado de medir, con número y unidad"), ("diferencia", "cuánto más o menos es una medida que otra")],
    worked=[
        {"title": "Estimar y medir", "problem": "Estimas que una mesa mide 100 cm. La mides y obtienes 120 cm. ¿Fue buena tu estimación?", "steps": ["120 cm es un poco más que 100 cm.", "La diferencia es 120 − 100 = 20 cm.", "Está cerca."], "answer": "Sí, estuvo cerca; la diferencia es 20 cm"},
        {"title": "Detectar una medida poco razonable", "problem": "Mides una mesa y escribes 12 m. ¿Es razonable?", "steps": ["Una mesa es más corta que una sala.", "12 m es el largo de un patio.", "Algo salió mal al medir."], "answer": "No, no es razonable"},
    ],
    mistakes=[
        {"wrong": "Medir sin estimar antes.", "why": "No hay manera de saber si el resultado tiene sentido.", "fix": "Estima primero y luego compara."},
        {"wrong": "Decir que una estimación de 1 m y una medida de 12 m están cerca.", "why": "No se compara con cuidado.", "fix": "Resta las medidas con la misma unidad: la diferencia es grande."},
    ],
    tiers={
        "recovery": [
            ex("Estimas un lápiz en 15 cm y mides 17 cm. ¿Están cerca?", "Sí", "La diferencia es sólo 2 cm."),
            ex("¿Qué haces antes de medir: estimar o escribir el resultado?", "Estimar", "Así puedes comparar después."),
            ex("¿Una mesa de 2 m es razonable para una mesa de comedor?", "Sí", "Una mesa de comedor mide cerca de 2 m."),
        ],
        "understand": [
            ex("¿Qué es estimar?", "Decir una medida aproximada antes de medir", "No hace falta que sea exacta."),
            ex("¿Por qué comparamos la estimación con la medida?", "Para ver si el resultado tiene sentido", "Así se detectan errores."),
            ex("¿Qué se escribe junto al número de una medida?", "La unidad", "Un número solo no dice qué se midió."),
        ],
        "apply": [
            arith("Un lápiz mide 17 cm y un cuaderno mide 28 cm. ¿Cuántos centímetros más largo es el cuaderno?", "28-17", "Se resta la medida menor a la mayor."),
            arith("Estimaste 20 cm para una tarjeta y mediste 25 cm. ¿Cuántos centímetros de diferencia hay?", "25-20", "Se resta la estimación a la medida."),
            ex("Una puerta mide 2 m de alto y una ventana mide 1 m de alto. ¿Cuál es más alta y por cuántos metros?", "La puerta; 1 m más", "2 − 1 = 1."),
        ],
        "reason": [
            ex("Gabi estimó que su sala mide 8 m y midió 8 cm. ¿Qué error probable hubo?", "Confundió la unidad: son 8 m", "Una sala no puede medir 8 cm."),
            ex("Hugo dice que como midió, ya no necesita estimar. ¿Tiene razón?", "No; estimar sirve para ver si la medida es razonable", "Una estimación detecta errores grandes."),
        ],
        "challenge": [
            ex("Tres tiras miden 12 cm, 9 cm y 15 cm. Ordénalas de la más corta a la más larga.", "9 cm, 12 cm, 15 cm", "Se ordenan los números con la misma unidad."),
            ex("Una cinta A mide 30 cm y una cinta B mide 22 cm. Si las pones una tras otra, ¿cuántos centímetros miden juntas y cuál es más larga?", "52 cm; la A", "30 + 22 = 52 y 30 > 22."),
        ],
    },
    context=[ex("Estimas que el largo de tu pieza es 3 m. Con la huincha obtienes 4 m. ¿Cuántos metros de diferencia hay entre la estimación y la medida?", "1 m", "4 − 3 = 1.")],
    selfcheck=[
        ex("¿Qué se hace primero: medir o estimar?", "Estimar", "Se estima antes de medir."),
        ex("Un lápiz mide 18 cm. ¿Es razonable que mida 18 m?", "No", "Dieciocho metros es demasiado."),
        ex("Un libro mide 20 cm y otro 24 cm. ¿Cuál es más largo?", "El de 24 cm", "24 es mayor que 20."),
    ],
    open_task=task(
        "Estima y luego mide dos objetos: tu lápiz y tu cuaderno. Si no puedes medir, usa estos datos: estimaste el lápiz en 15 cm y el cuaderno en 25 cm; las medidas fueron 17 cm y 28 cm. Escribe cuánto fue la diferencia en cada caso y cuál objeto es más largo.",
        "Lápiz: estimé 15 cm, medí 17 cm, la diferencia es 2 cm. Cuaderno: estimé 25 cm, medí 28 cm, la diferencia es 3 cm. El cuaderno es más largo que el lápiz por 11 cm (28 − 17).",
        ["escribe estimación y medida con unidad", "calcula las diferencias", "compara los dos objetos", "usa números razonables"],
        ["estimaciones", "medidas", "diferencias"],
        ["no escribir la unidad", "medir sin comparar con la estimación"],
        "Pide justificar si la estimación fue buena. Reconoce cuando compara con una resta.",
    ),
    reinforce="Estima el largo de tu cama en pasos y luego mídela. Anota las dos cifras.",
    extend="Mide la altura de una mesa y de una silla. Escribe cuántos centímetros más alta es la mesa.",
)

# ================================================================ OA 20
MONEDA_8 = ["cara", "sello", "sello", "cara", "cara", "sello", "cara", "cara"]
DADO_12 = [3, 5, 1, 3, 6, 2, 3, 5, 4, 3, 6, 1]
c8, d12 = Counter(MONEDA_8), Counter(DADO_12)
assert (c8["cara"], c8["sello"]) == (5, 3) and d12[3] == 4 and sum(d12.values()) == 12

register(
    OA20, 1,
    materials="Papel y lápiz. Si quieres, una moneda y un dado. Los resultados posibles de cada juego están explicados en el cuaderno.",
    use="Aprenderé a nombrar los resultados que pueden pasar antes de jugar con una moneda o un dado. Sirve para no sorprenderme y registrar bien después.",
    prior=["Sé contar hasta 10.", "Sé que una moneda tiene dos lados."],
    explain=[
        "Un juego de azar es un juego donde no sabes qué va a pasar. Si lanzas una moneda, puede salir cara o sello. Esos son los resultados posibles. No puedes saber cuál saldrá antes de lanzar.",
        "Un dado común tiene 6 caras con los números 1, 2, 3, 4, 5 y 6. Al lanzarlo puede salir cualquiera de esos seis números. Un 7 no puede salir: es un resultado imposible.",
        "Antes de jugar, escribe todos los resultados posibles. Así, cuando juegues, sabrás qué anotar. No digas qué va a salir, porque el resultado depende del azar.",
    ],
    vocab=[("resultado", "lo que se ve después de lanzar"), ("posible", "que puede ocurrir"), ("imposible", "que no puede ocurrir"), ("al azar", "sin poder saber cuál saldrá"), ("lanzar", "tirar una moneda o un dado")],
    worked=[
        {"title": "Resultados de una moneda", "problem": "Escribe los resultados posibles al lanzar una moneda.", "steps": ["Una moneda tiene dos lados.", "Un lado es cara.", "El otro lado es sello."], "answer": "Cara y sello"},
        {"title": "Imposible o posible", "problem": "Al lanzar un dado común, ¿es posible que salga 7?", "steps": ["El dado tiene los números del 1 al 6.", "El 7 no está en el dado.", "No puede salir."], "answer": "No, es imposible"},
    ],
    mistakes=[
        {"wrong": "Decir «va a salir cara» antes de lanzar la moneda.", "why": "No se puede saber el resultado de un juego de azar.", "fix": "Di «puede salir cara o sello»."},
        {"wrong": "Contar el 0 como resultado posible de un dado.", "why": "El dado común empieza en 1.", "fix": "Los resultados posibles son 1, 2, 3, 4, 5 y 6."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuáles son los resultados posibles al lanzar una moneda?", "Cara y sello", "La moneda tiene dos lados."),
            ex("¿Cuántos resultados posibles tiene un dado común?", "6", "Los números del 1 al 6."),
            ex("¿Puede salir un 9 en un dado común?", "No", "El dado sólo llega hasta 6."),
        ],
        "understand": [
            ex("¿Qué quiere decir «al azar»?", "Que no se puede saber cuál saldrá", "El resultado depende de la suerte."),
            ex("Antes de lanzar una moneda, ¿sabes qué saldrá?", "No", "Puede salir cara o sello."),
            ex("¿Qué es un resultado imposible?", "Uno que no puede ocurrir", "No está entre los resultados posibles."),
        ],
        "apply": [
            ex("Al lanzar un dado común, escribe los resultados que son números pares.", "2, 4 y 6", "Son los pares entre 1 y 6."),
            ex("Una bolsa tiene una ficha roja y una ficha azul. Sacas una sin mirar. ¿Qué resultados posibles hay?", "Roja y azul", "Hay una ficha de cada color."),
            ex("Al lanzar un dado común, ¿cuántos resultados son mayores que 4?", "2 (el 5 y el 6)", "Sólo 5 y 6 son mayores que 4."),
        ],
        "reason": [
            ex("Ana dice que seguro saldrá cara porque la última vez salió cara. ¿Es correcto?", "No; puede salir cara o sello", "Cada lanzamiento es al azar."),
            ex("Beto dice que en un dado común puede salir 0. ¿Qué error comete?", "El 0 no está en el dado; empieza en 1", "Los resultados posibles son del 1 al 6."),
        ],
        "challenge": [
            ex("Lanzas una moneda dos veces. Escribe todas las parejas de resultados posibles en orden (cara = C, sello = S).", "CC, CS, SC y SS", "Cada lanzamiento puede dar C o S."),
            ex("En una caja hay fichas con los números 1, 2 y 3. Sacas una sin mirar. ¿Cuántos resultados posibles hay y cuál es imposible: el 3 o el 5?", "3 resultados; el 5 es imposible", "Sólo están el 1, el 2 y el 3."),
        ],
    },
    context=[ex("En un juego de mesa lanzas un dado común para avanzar. ¿Cuántos casilleros puedes avanzar como mínimo y como máximo?", "Mínimo 1 y máximo 6", "El dado muestra del 1 al 6.")],
    selfcheck=[
        ex("¿Cuántos resultados posibles tiene la moneda?", "2", "Cara y sello."),
        ex("¿Puede salir un 6 en un dado común?", "Sí", "El 6 es una cara del dado."),
        ex("¿Se puede saber con certeza qué saldrá en un lanzamiento?", "No", "Es un juego de azar."),
    ],
    open_task=task(
        "Escribe en una tabla los resultados posibles de estos tres juegos: lanzar una moneda, lanzar un dado común y sacar una ficha de una bolsa con fichas roja, verde y amarilla. En cada juego escribe además un resultado imposible.",
        "Moneda: cara y sello; imposible: que salga un número. Dado: 1, 2, 3, 4, 5 y 6; imposible: 7. Bolsa: roja, verde y amarilla; imposible: azul.",
        ["escribe todos los resultados posibles de cada juego", "escribe un resultado imposible en cada juego", "no dice qué va a salir", "usa los números 1 a 6 en el dado"],
        ["tabla de resultados", "resultados imposibles"],
        ["incluir el 0 o el 7 como posibles", "decir qué saldrá"],
        "Pide explicar por qué un resultado es imposible. Reconoce cuando usa la palabra «al azar».",
    ),
    reinforce="Lanza una moneda 6 veces y di cada vez qué otro resultado pudo salir.",
    extend="Lanza un dado y escribe en una lista los resultados posibles que no han salido todavía.",
)

register(
    OA20, 2,
    materials="Papel y lápiz. Los registros de los lanzamientos están escritos en cada ejercicio; si quieres, repítelos con una moneda y un dado.",
    use="Aprenderé a anotar un lanzamiento a la vez, sin saltarme ninguno ni repetirlo. Sirve para tener datos confiables de un juego.",
    prior=["Sé los resultados posibles de la moneda y del dado.", "Sé contar hasta 20."],
    explain=[
        "Un dato es un resultado que anotamos. Para registrar bien, cada lanzamiento se anota una sola vez. Se hace una marca en la tabla por cada lanzamiento, justo después de lanzar.",
        "Las marcas se agrupan de a cinco: cuatro palitos y uno atravesado (||||/) valen 5. Al final se cuenta cuántas marcas tiene cada resultado. A ese número se le llama frecuencia.",
        "Para comprobar el registro, suma todas las frecuencias. La suma debe ser igual al número de lanzamientos. Si es distinta, se olvidó una marca o se repitió una.",
    ],
    vocab=[("dato", "un resultado que se anota"), ("registro", "lista o tabla donde se anotan los datos"), ("marca", "palito que se anota por cada lanzamiento"), ("frecuencia", "cuántas veces salió un resultado"), ("total", "cuántos lanzamientos se hicieron")],
    worked=[
        {"title": "Contar un registro", "problem": f"Una moneda se lanzó 8 veces: {', '.join(MONEDA_8)}. ¿Cuántas veces salió cada resultado?", "steps": [f"Cuento las caras: {c8['cara']}.", f"Cuento los sellos: {c8['sello']}.", f"Compruebo: {c8['cara']} + {c8['sello']} = 8, igual a los lanzamientos."], "answer": f"{c8['cara']} caras y {c8['sello']} sellos"},
        {"title": "Marcas de a cinco", "problem": "Una tabla muestra ||||/ | para el resultado «3». ¿Cuántas veces salió el 3?", "steps": ["||||/ vale 5.", "| vale 1 más.", "5 + 1 = 6."], "answer": "6 veces"},
    ],
    mistakes=[
        {"wrong": "Anotar dos veces el mismo lanzamiento.", "why": "Se pierde la cuenta y el total no coincide.", "fix": "Haz una marca justo después de cada lanzamiento y no repitas."},
        {"wrong": "Dejar de anotar un resultado que no esperabas.", "why": "Se cambian los datos para que coincidan con lo que se pensaba.", "fix": "Anota siempre lo que realmente salió."},
    ],
    tiers={
        "recovery": [
            ex(f"En este registro de 8 lanzamientos de moneda salió: {', '.join(MONEDA_8)}. ¿Cuántas veces salió cara?", str(c8["cara"]), "Se cuentan las veces que dice cara."),
            ex(f"En ese mismo registro, ¿cuántas veces salió sello?", str(c8["sello"]), "Se cuentan las veces que dice sello."),
            ex("Una marca ||||/ vale 5. ¿Cuánto vale ||||/ ||?", "7", "5 + 2 = 7."),
        ],
        "understand": [
            ex("¿Cuántas marcas haces por cada lanzamiento?", "Una", "Cada lanzamiento se anota una sola vez."),
            ex("¿Qué es la frecuencia de un resultado?", "Cuántas veces salió", "Es el número de veces que se repite."),
            ex("¿Con qué se compara la suma de frecuencias para comprobar?", "Con el número total de lanzamientos", "Las dos cantidades deben ser iguales."),
        ],
        "apply": [
            ex(f"Lanzamientos de un dado: {', '.join(str(v) for v in DADO_12)}. ¿Cuántas veces salió el 3?", str(d12[3]), "Se cuentan los 3 de la lista."),
            ex(f"En ese mismo registro, ¿cuántas veces salió el 6?", str(d12[6]), "Se cuentan los 6 de la lista."),
            arith("En una tabla, el 1 salió 2 veces, el 2 salió 1 vez, el 3 salió 4 veces, el 4 salió 1 vez, el 5 salió 2 veces y el 6 salió 2 veces. ¿Cuántos lanzamientos son?", "2+1+4+1+2+2", "Se suman todas las frecuencias."),
        ],
        "reason": [
            ex("Un registro dice: cara 4, sello 3. Se lanzó 8 veces. Lía dice que está bien. ¿Qué pasó?", "Falta una marca: 4 + 3 = 7, no 8", "La suma debe ser igual a los lanzamientos."),
            ex("Mario anotó dos veces el mismo lanzamiento. ¿Cómo lo notarás al comprobar?", "La suma de frecuencias será mayor que los lanzamientos", "Hay una marca de más."),
        ],
        "challenge": [
            ex("Se lanzó una moneda 10 veces. Salieron 6 caras. ¿Cuántos sellos salieron?", "4", "10 − 6 = 4."),
            ex("En 12 lanzamientos de un dado el 1 salió 2 veces, el 2 salió 1 vez, el 4 salió 1 vez y el 6 salió 2 veces. ¿Cuántos lanzamientos fueron del 3 y del 5 juntos?", "6", "12 − (2 + 1 + 1 + 2) = 6."),
        ],
    },
    context=[ex("Clara lanzó una moneda 8 veces, la misma lista que se mostró arriba: cara, sello, sello, cara, cara, sello, cara, cara. ¿Cuál resultado salió más veces?", "Cara", "Salió 5 veces, más que los 3 sellos.")],
    selfcheck=[
        ex("¿Cuántas marcas se hacen por cada lanzamiento?", "Una", "Cada dato se anota una vez."),
        ex("Si cara salió 6 veces y sello salió 4, ¿cuántos lanzamientos fueron?", "10", "6 + 4 = 10."),
        ex("¿Cuánto vale ||||/ en una tabla de conteo?", "5", "Cuatro palitos y uno atravesado."),
    ],
    open_task=task(
        "Lanza una moneda 10 veces y anota cada resultado en una tabla de conteo. Si no tienes moneda, usa esta lista de 10 lanzamientos: cara, cara, sello, cara, sello, sello, cara, cara, sello, cara. Anota las marcas, cuenta la frecuencia de cada resultado y comprueba que la suma sea 10.",
        "Con la lista dada: cara 6 (||||/ |) y sello 4 (||||). Compruebo: 6 + 4 = 10, igual al número de lanzamientos.",
        ["hace una marca por lanzamiento", "cuenta las frecuencias", "comprueba que la suma sea 10", "usa los dos resultados posibles"],
        ["tabla de conteo", "frecuencias", "comprobación"],
        ["omitir un lanzamiento", "repetir una marca"],
        "Pide releer la lista contando en voz alta. Reconoce la comprobación con la suma.",
    ),
    reinforce="Lanza un dado 10 veces y anota cada resultado con una marca en una tabla.",
    extend="Repite el juego con una moneda 12 veces y compara con el de 10 lanzamientos: ¿cambió cuál salió más?",
)

register(
    OA20, 3,
    materials="Papel cuadriculado o líneas dibujadas en el cuaderno, y lápiz. Los datos de cada juego están escritos en los ejercicios.",
    use="Aprenderé a pasar las marcas de un juego a bloques y a un pictograma. Sirve para ver de un vistazo qué resultado salió más.",
    prior=["Sé hacer una tabla de conteo con marcas.", "Sé contar frecuencias."],
    explain=[
        "Un pictograma es un gráfico hecho con dibujos o símbolos. En nuestro caso, cada símbolo representa un lanzamiento: se dibuja un símbolo por cada vez que salió un resultado.",
        "Primero, cuenta las marcas de la tabla. Por ejemplo, 6 caras y 4 sellos. Luego, puedes hacer torres de bloques: una torre de 6 bloques y otra de 4. Después, cambia cada bloque por un símbolo en el pictograma.",
        "Un pictograma tiene un título, nombres para cada fila y un símbolo por cada dato. Las filas del mismo símbolo deben tener el mismo tamaño. Así puedes comparar quién tiene más símbolos.",
    ],
    vocab=[("pictograma", "gráfico con símbolos o dibujos"), ("símbolo", "dibujo que representa un dato"), ("frecuencia", "cuántas veces salió un resultado"), ("fila", "línea de símbolos de un resultado"), ("título", "nombre del gráfico")],
    worked=[
        {"title": "De marcas a pictograma", "problem": "Una moneda se lanzó 10 veces: 6 caras y 4 sellos. Haz un pictograma con un símbolo por lanzamiento.", "steps": ["Cara: 6 símbolos.", "Sello: 4 símbolos.", f"Cara: {sym('●', 6)}", f"Sello: {sym('●', 4)}"], "answer": f"Cara {sym('●', 6)} / Sello {sym('●', 4)}"},
        {"title": "Leer un pictograma", "problem": f"Pictograma de un dado. Uno: {sym('★', 3)}. Dos: {sym('★', 5)}. Tres: {sym('★', 2)}. ¿Cuál salió más?", "steps": ["Cuento los símbolos de cada fila.", "Uno: 3, Dos: 5, Tres: 2.", "5 es el mayor."], "answer": "El 2, con 5 veces"},
    ],
    mistakes=[
        {"wrong": "Dibujar los símbolos de la fila de «sello» más grandes que los de «cara».", "why": "Los símbolos distintos de tamaño engañan.", "fix": "Todos los símbolos deben ser del mismo tamaño y estar alineados."},
        {"wrong": "Hacer un pictograma con 5 símbolos para 6 caras.", "why": "No se copió la frecuencia.", "fix": "La cantidad de símbolos debe ser igual a la frecuencia."},
    ],
    tiers={
        "recovery": [
            ex(f"En un pictograma, Cara tiene {sym('●', 7)}. ¿Cuántas veces salió cara?", "7", "Cada símbolo es un lanzamiento."),
            ex(f"En un pictograma, Sello tiene {sym('●', 3)}. ¿Cuántas veces salió sello?", "3", "Se cuentan los símbolos."),
            ex("¿Cuántos símbolos dibujas para un resultado que salió 5 veces?", "5", "Un símbolo por cada vez."),
        ],
        "understand": [
            ex("¿Qué representa cada símbolo de este pictograma?", "Un lanzamiento", "La escala es de uno."),
            ex("¿Qué debe tener el pictograma además de los símbolos?", "Un título y nombres de las filas", "Así se entiende de qué trata."),
            ex("¿Por qué deben ser iguales todos los símbolos?", "Para poder comparar", "Si uno es más grande, engaña a la vista."),
        ],
        "apply": [
            ex("Construye un pictograma para 3 unos, 5 doses y 2 treses. Escribe las tres filas con ★.", f"1: {sym('★', 3)} / 2: {sym('★', 5)} / 3: {sym('★', 2)}", "Cada resultado lleva tantos símbolos como veces salió."),
            ex(f"Pictograma de una moneda: Cara {sym('●', 6)}; Sello {sym('●', 4)}. ¿Cuántos lanzamientos hubo en total?", "10", "6 + 4 = 10."),
            ex(f"Pictograma: Rojo {sym('▲', 4)}; Azul {sym('▲', 7)}; Verde {sym('▲', 2)}. ¿Cuántos más hay en Azul que en Verde?", "5", "7 − 2 = 5."),
        ],
        "reason": [
            ex("Pedro dibujó 5 símbolos para el 4, pero el 4 salió 6 veces. ¿Qué debe corregir?", "Agregar un símbolo; debe haber 6", "El número de símbolos es la frecuencia."),
            ex("Una fila tiene símbolos pequeños y otra símbolos grandes. ¿Por qué engaña?", "Porque se ve más grande una fila aunque no tenga más datos", "El tamaño distinto cambia la impresión."),
        ],
        "challenge": [
            ex("Un dado se lanzó 9 veces. El 1 salió 2 veces, el 3 salió 4 veces y el 5 salió 3 veces. Escribe el pictograma con ●.", f"1: {sym('●', 2)} / 3: {sym('●', 4)} / 5: {sym('●', 3)}", "2 + 4 + 3 = 9."),
            ex("En un pictograma hay 4 filas: 3, 5, 1 y 6 símbolos. ¿Cuántos lanzamientos representa?", "15", "3 + 5 + 1 + 6 = 15."),
        ],
    },
    context=[ex("Un grupo lanzó un dado 8 veces: salió 2 una vez, 4 tres veces y 6 cuatro veces. ¿Cuántos símbolos lleva la fila del 6?", "4", "Un símbolo por cada vez que salió.")],
    selfcheck=[
        ex("¿Cuántos símbolos necesitas para un resultado que salió 8 veces?", "8", "Un símbolo por vez."),
        ex(f"Fila de Cara: {sym('●', 5)}; fila de Sello: {sym('●', 6)}. ¿Cuál salió más?", "Sello", "6 es mayor que 5."),
        ex("¿Qué debe tener todo pictograma al comienzo?", "Un título", "Dice de qué trata el gráfico."),
    ],
    open_task=task(
        "Usa esta tabla de un dado lanzado 12 veces: el 1 salió 2 veces, el 2 salió 1 vez, el 3 salió 4 veces, el 4 salió 1 vez, el 5 salió 2 veces y el 6 salió 2 veces. Construye una torre de bloques (o dibuja cuadrados) para cada número. Después haz un pictograma con ★ y pon un título. Escribe qué número salió más.",
        f"Título: Lanzamientos de un dado. 1: {sym('★', 2)}. 2: {sym('★', 1)}. 3: {sym('★', 4)}. 4: {sym('★', 1)}. 5: {sym('★', 2)}. 6: {sym('★', 2)}. El 3 salió más veces: 4.",
        ["dibuja la cantidad correcta de símbolos en cada fila", "pone título y nombres", "usa símbolos del mismo tamaño", "responde cuál salió más"],
        ["pictograma", "respuesta"],
        ["símbolos de tamaños distintos", "contar mal las frecuencias"],
        "Pide contar los símbolos de cada fila en voz alta. Reconoce que el total sea 12.",
    ),
    reinforce="Haz un pictograma con 8 lanzamientos de una moneda: cada símbolo es un lanzamiento.",
    extend="Haz un pictograma con 12 lanzamientos de un dado y escribe qué número salió más.",
)

register(
    OA20, 4,
    materials="Papel y lápiz. Todas las tablas y registros están escritos en los ejercicios.",
    use="Aprenderé a sacar conclusiones verdaderas de los datos que tengo, sin adivinar lo que pasará después. Sirve para no decir cosas que los datos no muestran.",
    prior=["Sé leer tablas y pictogramas de un juego.", "Sé que un juego de azar no se puede predecir."],
    explain=[
        "Una conclusión es una frase que dice lo que muestran los datos. Si en 10 lanzamientos salió cara 7 veces y sello 3, una conclusión verdadera es: «En estos 10 lanzamientos, cara salió más veces que sello».",
        "Pero no podemos decir «siempre saldrá cara» ni «el próximo será cara». Los datos sólo cuentan lo que pasó en esos lanzamientos. En un juego de azar, el siguiente resultado puede ser cualquiera de los posibles.",
        "Una pregunta estadística es una pregunta que se responde juntando datos, como «¿qué resultado salió más veces en 10 lanzamientos?». No sirve para eso «¿qué saldrá ahora?». Para escribir una conclusión válida, usa números de la tabla y la frase «en estos lanzamientos». Evita las palabras «siempre» y «nunca» cuando hables de lo que va a pasar.",
    ],
    vocab=[("conclusión", "frase que dice lo que muestran los datos"), ("verdadera", "que coincide con los datos"), ("predecir", "decir lo que pasará después"), ("ensayo", "cada vez que se repite el juego"), ("dato", "resultado que se anotó")],
    worked=[
        {"title": "Conclusión válida", "problem": "En 10 lanzamientos de una moneda salieron 7 caras y 3 sellos. Escribe una conclusión verdadera.", "steps": ["Uso los números: 7 caras y 3 sellos.", "Comparo: 7 es mayor que 3.", "Digo «en estos 10 lanzamientos»."], "answer": "En estos 10 lanzamientos, cara salió más veces que sello"},
        {"title": "Afirmación que los datos no permiten", "problem": "Con los mismos datos, un niño dice «el próximo lanzamiento será cara». ¿Está bien?", "steps": ["Los datos sólo dicen lo que ya pasó.", "El próximo lanzamiento es al azar.", "Puede salir cara o sello."], "answer": "No; los datos no permiten predecir"},
    ],
    mistakes=[
        {"wrong": "Decir «siempre saldrá cara» porque salió 7 veces de 10.", "why": "Se usan pocos datos para predecir todo.", "fix": "Di lo que pasó en esos lanzamientos, no lo que pasará."},
        {"wrong": "Inventar un dato que no está en la tabla.", "why": "La conclusión no se apoya en el registro.", "fix": "Usa sólo los números de la tabla."},
    ],
    tiers={
        "recovery": [
            ex("En 8 lanzamientos salió cara 5 veces y sello 3 veces. ¿Qué salió más veces?", "Cara", "5 es mayor que 3."),
            ex("En 6 lanzamientos de un dado salió el 4 dos veces y el 1 una vez. ¿Qué número salió más veces entre esos dos?", "El 4", "2 es mayor que 1."),
            ex("¿Cuál se responde con datos de lanzamientos? A) «¿Cuántas veces salió cara en 10 lanzamientos?». B) «¿Saldrá cara en el próximo lanzamiento?».", "A", "Los datos cuentan lo que pasó; no dicen lo que pasará."),
        ],
        "understand": [
            ex("¿Qué es una conclusión?", "Una frase que dice lo que muestran los datos", "Se apoya en el registro."),
            ex("¿Pueden los datos decirte con seguridad qué saldrá en el próximo lanzamiento?", "No", "El siguiente resultado es al azar."),
            ex("¿Qué palabras conviene evitar al hablar del futuro de un juego de azar?", "Siempre y nunca", "No se puede asegurar."),
        ],
        "apply": [
            ex("Tabla de una moneda: cara 4, sello 6. Elige la conclusión verdadera: A) «En estos 10 lanzamientos salió sello más veces que cara». B) «Siempre saldrá sello».", "A", "La B predice el futuro."),
            ex("Tabla de un dado en 9 lanzamientos: el 2 salió 5 veces, el 5 salió 3 veces y el 6 salió 1 vez. Escribe una conclusión verdadera.", "En estos 9 lanzamientos, el 2 salió más veces", "5 es la mayor frecuencia."),
            arith("Tabla: el 1 salió 3 veces, el 3 salió 2 veces y el 6 salió 4 veces. ¿Cuántos lanzamientos hubo?", "3+2+4", "Se suman las frecuencias."),
        ],
        "reason": [
            ex("Óscar dice que, como cara salió 7 veces de 10, la moneda es mágica. ¿Qué responderías?", "Que sólo muestra lo que pasó en esos 10 lanzamientos", "Con pocos datos no se puede asegurar eso."),
            ex("Sofía dice «el 5 nunca saldrá» porque no salió en 6 lanzamientos. ¿Qué error comete?", "Que no haya salido no significa que no pueda salir", "El 5 es un resultado posible."),
        ],
        "challenge": [
            ex("Tabla de 12 lanzamientos: cara 8 y sello 4. Escribe dos conclusiones verdaderas.", "Cara salió más veces; hubo 4 caras más que sellos", "8 > 4 y 8 − 4 = 4."),
            ex("Dos grupos lanzaron una moneda. El grupo A tuvo 6 caras de 10 y el grupo B tuvo 3 caras de 10. ¿Cuántas caras más tuvo el grupo A?", "3", "6 − 3 = 3."),
        ],
    },
    context=[ex("En el recreo, un grupo registró 10 lanzamientos de dado: salió 6 cuatro veces. Pedro dice «el 6 saldrá siempre». ¿Qué conclusión sí se puede decir?", "En estos 10 lanzamientos el 6 salió 4 veces", "Es lo que muestran los datos.")],
    selfcheck=[
        ex("¿Qué dicen los datos: lo que pasó o lo que pasará?", "Lo que pasó", "Son un registro de ensayos ya hechos."),
        ex("Cara salió 5 veces y sello 5 veces. ¿Cuál salió más?", "Ninguno; salieron igual", "5 es igual a 5."),
        ex("¿Se pueden cambiar los datos para que coincidan con lo que esperabas?", "No", "Los datos son lo que realmente salió."),
    ],
    open_task=task(
        "Mira esta tabla de 10 lanzamientos de una moneda: cara 6, sello 4. Escribe una conclusión verdadera con números de la tabla y una afirmación que los datos NO permiten. Explica por qué no se puede afirmar.",
        "Conclusión verdadera: en estos 10 lanzamientos salió cara 6 veces y sello 4, es decir, 2 caras más. Afirmación que los datos no permiten: «el próximo lanzamiento será cara». No se puede afirmar porque el siguiente resultado es al azar.",
        ["escribe una conclusión con números de la tabla", "usa «en estos lanzamientos»", "escribe una afirmación que los datos no permiten", "explica por qué"],
        ["conclusión verdadera", "afirmación inválida", "explicación"],
        ["usar «siempre»", "inventar datos"],
        "Pide mostrar en la tabla de dónde sale cada número. Reconoce cuando distingue entre lo que pasó y lo que pasará.",
    ),
    reinforce="Lanza una moneda 10 veces, anota los resultados y escribe una conclusión que empiece con «En estos 10 lanzamientos…».",
    extend="Repite el juego con un dado y escribe una conclusión verdadera y una afirmación que los datos no permiten.",
)
