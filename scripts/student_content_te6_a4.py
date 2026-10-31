"""Cuaderno del estudiante, 6.º básico Tecnología: OA 04 (probar y evaluar la calidad de trabajos propios o de otros), clases 1 a 6.

Clase 1 criterios de funcionamiento y técnicos, 2 medioambientales, 3 estéticos y de seguridad, 4 evaluar con pauta (individual y en equipo),
5 dialogar sobre los resultados, 6 aplicar correcciones. Los trabajos evaluados son ficticios y de materiales seguros (papel, cartón, tapas, cordel).
Simplificación declarada: la ficha oficial usa los mismos títulos de clase en todos los OA; aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te6_a import reg
from student_lessons import arith

OA4 = "TE06 OA 04"

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja y lápiz. Los trabajos y sus datos están escritos en este cuaderno.",
    use="Aprenderé a evaluar si un trabajo funciona y si cumple los criterios técnicos, como medidas y resistencia. Sirve para saber si un producto es de buena calidad.",
    prior=["Sé hacer pruebas con datos.", "Sé calcular un promedio.", "Sé leer una tolerancia."],
    explain=[
        "La calidad de un trabajo se evalúa con criterios. Los criterios de funcionamiento preguntan si el producto cumple su función: por ejemplo, un portalápices debe sostener los lápices sin caerse. Se comprueban con una prueba y se anota el resultado.",
        "Los criterios técnicos miran cómo está hecho: si las medidas están dentro de la tolerancia, si las uniones aguantan, si los cortes son limpios y si el material es el adecuado. Se comprueban midiendo, tirando suavemente de una unión o mirando el corte de cerca. Cada criterio debe poder observarse o medirse.",
        "Puedes evaluar tu propio trabajo o el de otras personas, solo o en equipo. Siempre se usa la misma lista de criterios y se registra la evidencia: un número, una medida o una descripción. Evaluar no es decir si algo te gusta, sino comprobar con datos qué criterios cumple y cuáles no.",
    ],
    vocab=[("calidad", "grado en que un trabajo cumple sus criterios"), ("criterio de funcionamiento", "condición sobre si el producto cumple su función"), ("criterio técnico", "condición sobre cómo está hecho"), ("evidencia", "dato que apoya una evaluación"), ("evaluar", "comprobar con criterios qué cumple un trabajo")],
    worked=[
        ("Evaluar el funcionamiento", "Un portalápices debe sostener 10 lápices sin caerse. En una prueba sostuvo 10 y no se cayó. ¿Cumple el criterio de funcionamiento?", ["El criterio es sostener 10 lápices sin caerse.", "El resultado fue 10 lápices y no se cayó."], "Sí cumple"),
        ("Evaluar un criterio técnico", "Una pared debe medir 120 mm con tolerancia de 2 mm. Mide 125 mm. ¿Cumple?", ["El rango va de 118 a 122 mm.", "125 mm está fuera del rango."], "No cumple"),
    ],
    mistakes=[
        ("Evaluar solo si el trabajo se ve bonito.", "La calidad también incluye funcionamiento y medidas.", "Evalúa con criterios de funcionamiento y técnicos y registra datos."),
        ("Anotar «está bien» sin dato.", "No se puede comprobar.", "Anota un número, una medida o una descripción."),
    ],
    R=[
        ("¿Un criterio de funcionamiento pregunta si el producto cumple su función o si es de un color?", "Si cumple su función", "Es la definición de funcionamiento."),
        ("Un corte limpio y medidas dentro de tolerancia, ¿son criterios técnicos o de funcionamiento?", "Técnicos", "Se refieren a cómo está hecho."),
        ("¿Qué se anota al evaluar un criterio?", "La evidencia", "Es un número, medida o descripción."),
    ],
    C=[
        ("¿Por qué es importante que un criterio pueda observarse o medirse?", "Porque así se puede comprobar", "Un criterio vago no se puede evaluar."),
        ("Un puente de papel se pandea con 80 g. El criterio pide 100 g. ¿Qué tipo de criterio es?", "De funcionamiento", "Mide si cumple su función de aguantar peso."),
        ("¿Se pueden usar los mismos criterios para evaluar tu trabajo y el de otra persona?", "Sí", "Siempre se usa la misma lista."),
    ],
    A=[
        arith("Un soporte debe sostener 12 fichas. En la prueba sostuvo 9. ¿Cuántas fichas le faltan para cumplir?", "12-9", "Se resta lo que sostuvo de lo que se pide.", " fichas"),
        ("Una pieza debe medir 80 mm con tolerancia de 3 mm. Mide 82 mm. ¿Cumple?", "Sí", "El rango aceptado va de 77 a 83 mm."),
        ("Una unión se despega al tirar suavemente. ¿Qué criterio técnico no cumple? A uniones firmes, B colores parejos.", "A", "La unión no aguanta."),
    ],
    Z=[
        ("Ana dice que su trabajo es excelente porque «se ve bien». Pablo muestra que sostuvo 10 lápices y que sus medidas están en tolerancia. ¿Quién evaluó mejor?", "Pablo", "Usó criterios con evidencia."),
        ("Un grupo prueba un producto una sola vez y concluye que funciona. ¿Qué mejora la evaluación?", "Repetir la prueba al menos tres veces", "Una prueba puede salir bien por casualidad."),
    ],
    D=[
        arith("Tres pruebas de resistencia dan 14, 16 y 12 fichas. El criterio pide un promedio de 14 o más. ¿Cuál es el promedio?", "(14+16+12)//3", "Se suman los datos y se divide entre 3.", " fichas"),
        ("Un producto cumple función pero tiene medidas fuera de tolerancia en 2 de 5 piezas. ¿Qué evaluación es correcta? A cumple todo, B cumple funcionamiento y falla un criterio técnico.", "B", "Funciona, pero las medidas no son todas correctas."),
    ],
    ctx=("Evalúas una caja de cartón hecha por un compañero. Debe cerrar bien, aguantar 5 libros y tener paredes de 150 mm con tolerancia de 2 mm. La tapa cierra, aguanta 5 libros y las paredes miden 149, 151, 150 y 154 mm. Escribe cuántos criterios cumple y cuál no.", "Cumple funcionamiento (cierra y aguanta 5 libros) y falla un criterio técnico: la pared de 154 mm", "Se revisa cada medida contra el rango de 148 a 152 mm."),
    sc=[
        ("¿Qué tipos de criterios usaste hoy?", "De funcionamiento y técnicos", "Son los dos tipos de la clase."),
        ("¿Qué se registra al evaluar?", "La evidencia", "Apoya la evaluación."),
        ("¿Cuántas veces conviene repetir una prueba?", "Al menos tres", "Así se comprueba mejor."),
    ],
    open_task=(
        "Escoge un trabajo para evaluar. Trabajo 1: un marcador de libros de cartulina que debe medir 20 cm con tolerancia de 1 cm y mantenerse en el lugar; mide 22 cm y se cae en 2 de 3 pruebas. Trabajo 2: un soporte para 8 tapas que debe tener una base de 15 cm con tolerancia de 1 cm; mide 15 cm y sostiene 8 tapas en 3 de 3 pruebas. Escribe un criterio de funcionamiento y uno técnico, el dato de cada uno y si cumple.",
        "Trabajo 2: funcionamiento: sostiene 8 tapas, 3 de 3 pruebas, cumple. Técnico: base de 15 cm dentro de tolerancia, cumple",
        ["un criterio de funcionamiento", "un criterio técnico", "dato como evidencia", "dice si cumple"],
        ["tabla con criterios, evidencia y decisión"],
        ["evaluar sin datos", "mezclar los tipos de criterio"],
        "Pregunta: «¿qué dato muestra que cumple?». Si no cita número, pídele volver al trabajo.",
    ),
    reinforce="Elige un objeto de tu casa y escribe un criterio de funcionamiento y uno técnico para evaluarlo.",
    extend="Explica por qué dos personas deben usar la misma lista de criterios para comparar trabajos.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja y lápiz. Los datos están escritos en este cuaderno.",
    use="Aprenderé a evaluar el impacto ambiental de un trabajo con criterios medibles. Sirve para elegir productos que cuidan el ambiente.",
    prior=["Sé qué son reducir, reutilizar y reciclar.", "Sé calcular porcentajes sencillos.", "Sé que un criterio se puede medir."],
    explain=[
        "Un criterio medioambiental evalúa el efecto de un trabajo en la naturaleza. Algunos criterios son: cuánto material reutilizado usa, cuántos residuos genera, cuánta energía o agua gasta y cuánto dura el producto. Un producto que dura más y se puede reparar genera menos basura.",
        "Para medir el material reutilizado se compara el peso reutilizado con el peso total. Si de 400 g, 300 g son reutilizados, la fracción es 300 de 400, o sea 75 de cada 100 (75 %). Para calcular un porcentaje se multiplica por 100 y se divide entre el total. Un 75 % significa 75 de cada 100.",
        "Los criterios ambientales se combinan con los demás. Un producto puede funcionar muy bien y producir muchos residuos; entonces debe mejorar. Se evalúa con datos: peso reutilizado, número de piezas desechadas, vida útil. Al evaluar a otra persona se señala qué hizo bien y qué podría mejorar, sin burlarse.",
    ],
    vocab=[("criterio medioambiental", "condición sobre el efecto en la naturaleza"), ("residuo", "material que se bota"), ("vida útil", "tiempo que dura un producto"), ("porcentaje", "cantidad de cada 100"), ("reparar", "arreglar un objeto para seguir usándolo")],
    worked=[
        ("Calcular material reutilizado", "Un objeto pesa 500 g y 200 g son de material reutilizado. ¿Qué porcentaje es reutilizado?", ["Multiplico 200 por 100: 20.000.", "Divido 20.000 entre 500."], "40 %"),
        ("Comparar la vida útil", "Producto A dura 2 semanas y no se puede reparar. Producto B dura 8 semanas y se repara. ¿Cuál es mejor ambientalmente?", ["B dura más.", "B se repara, así que genera menos residuos."], "El producto B"),
    ],
    mistakes=[
        ("Decir «es ecológico» sin datos.", "No se puede comprobar.", "Muestra el porcentaje de material reutilizado o los residuos generados."),
        ("Medir solo el material reutilizado y olvidar la durabilidad.", "Un producto que se rompe pronto genera más basura.", "Considera también cuánto dura y si se repara."),
    ],
    R=[
        ("¿Un producto que dura mucho genera más o menos basura?", "Menos", "Se usa más tiempo antes de botarlo."),
        ("Usar un envase limpio que ya existe, ¿es reducir, reutilizar o reciclar?", "Reutilizar", "Se vuelve a usar sin transformarlo."),
        ("¿Qué significa 50 % de material reutilizado?", "50 de cada 100 partes son reutilizadas", "Un porcentaje es cuántas partes de cada 100."),
    ],
    C=[
        ("¿Cuál es un criterio medioambiental? A «gasta poca agua», B «usa tres colores».", "A", "El gasto de agua afecta la naturaleza."),
        ("¿Por qué reparar un objeto es bueno para el ambiente?", "Porque evita botarlo y generar residuos", "Se usa más tiempo."),
        ("Un producto funciona muy bien y genera 40 residuos. ¿Sirve decir que es de buena calidad?", "No, debe mejorar en lo ambiental", "La calidad incluye todos los criterios."),
    ],
    A=[
        arith("Un objeto pesa 400 g y 300 g son de material reutilizado. ¿Qué porcentaje es reutilizado?", "300*100//400", "Se multiplica por 100 y se divide entre el peso total.", " %"),
        arith("Un grupo botaba 12 residuos por semana y ahora bota 7. ¿Cuántos residuos menos?", "12-7", "Se resta lo que bota ahora de lo que botaba.", " residuos"),
        arith("Un producto dura 3 semanas y su versión mejorada dura 5 veces lo que dura la primera. ¿Cuántas semanas dura la mejorada?", "3*5", "Se multiplica la duración por 5.", " semanas"),
    ],
    Z=[
        ("Producto A: 80 % reutilizado pero se rompe en 1 semana. Producto B: 50 % reutilizado y dura 10 semanas. ¿Cuál puede ser mejor ambientalmente y por qué?", "B, porque dura más y genera menos basura", "La durabilidad también cuenta."),
        ("Un grupo dice que su trabajo es ecológico porque es verde. ¿Qué respuesta es correcta?", "El color no mide el efecto ambiental", "Se necesitan datos como residuos o material reutilizado."),
    ],
    D=[
        arith("De 250 g de un objeto, 125 g son reutilizados. ¿Qué porcentaje es?", "125*100//250", "Se multiplica por 100 y se divide entre 250.", " %"),
        arith("Un trabajo usa 60 g de material nuevo y 140 g de reutilizado. ¿Qué porcentaje del total es reutilizado?", "140*100//(60+140)", "Primero se obtiene el peso total y luego el porcentaje.", " %"),
    ],
    ctx=("Evalúas dos portalápices. A pesa 200 g, con 150 g de cartón reutilizado, y dura 6 semanas. B pesa 250 g, con 50 g de cartón reutilizado, y dura 3 semanas. Calcula el porcentaje reutilizado de cada uno y di cuál es mejor ambientalmente.", "A: 75 %; B: 20 %. A es mejor: más reutilizado y dura más", "Se calcula 150 ÷ 200 y 50 ÷ 250."),
    sc=[
        ("¿Qué mide un criterio medioambiental?", "El efecto del trabajo en la naturaleza", "Es el tema de la clase."),
        ("¿Qué significa 75 %?", "75 de cada 100", "Es la definición de porcentaje."),
        ("¿Por qué importa la vida útil?", "Un producto duradero genera menos residuos", "Se bota con menos frecuencia."),
    ],
    open_task=(
        "Escoge un par de trabajos. Par 1: un organizador de 300 g con 150 g reutilizados que dura 4 semanas y un organizador de 200 g con 40 g reutilizados que dura 4 semanas. Par 2: una caja de 400 g con 100 g reutilizados que se repara y una caja de 400 g con 100 g reutilizados que no se repara. Calcula los porcentajes, compara la durabilidad y decide cuál es mejor ambientalmente.",
        "Par 2: ambas 25 % reutilizado; la que se repara es mejor porque genera menos residuos",
        ["calcula los porcentajes", "compara la durabilidad o reparación", "decide y justifica", "usa datos"],
        ["tabla con porcentajes y decisión"],
        ["decidir sin datos", "ignorar la durabilidad"],
        "Pregunta: «¿qué dato muestra que uno es mejor?». Si no cita porcentaje o duración, pídelo.",
    ),
    reinforce="Observa tres envases de tu casa y anota cuáles podrías reutilizar y para qué.",
    extend="Explica con un ejemplo por qué un producto puede tener muy buen funcionamiento y mala evaluación ambiental.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a evaluar criterios estéticos, como el orden y el acabado, y criterios de seguridad, como bordes lisos y estabilidad. Sirve para que un producto sea agradable y no lastime.",
    prior=["Sé que un criterio se puede observar.", "Sé qué es la estabilidad.", "Sé que los bordes pueden lastimar."],
    explain=[
        "Un criterio estético evalúa la presentación de un trabajo: el orden, la limpieza, la simetría, los colores y el acabado. Aunque parezca opinión, se puede escribir de forma observable: «usa como máximo 3 colores», «las dos mitades son iguales» o «no tiene manchas de pegamento».",
        "Un criterio de seguridad evalúa si el producto puede lastimar o fallar de forma peligrosa. Algunos criterios son: bordes lisos y sin puntas, sin piezas pequeñas sueltas, estabilidad que evita vuelcos, materiales que no se rompen en astillas y sin partes que atrapen los dedos. La seguridad es el criterio más importante: si falla, se corrige antes que los demás.",
        "Cada criterio se comprueba con una acción: pasar un dedo con cuidado por el borde, empujar suavemente el producto para ver si se vuelca, o contar las piezas sueltas. Si un criterio estético y uno de seguridad chocan, gana la seguridad. Evalúa siempre con respeto y señala qué hizo bien la persona.",
    ],
    vocab=[("criterio estético", "condición sobre la presentación de un trabajo"), ("acabado", "cómo queda la superficie terminada"), ("simetría", "cuando dos mitades son iguales como en un espejo"), ("criterio de seguridad", "condición para que el producto no lastime"), ("estabilidad", "capacidad de no volcarse")],
    worked=[
        ("Escribir un criterio estético observable", "Quieres evaluar si un cartel «se ve ordenado». Escribe un criterio observable.", ["Pienso en lo que se puede ver o contar.", "Escribo: tiene máximo 3 colores y el texto no se sale del borde."], "Tiene máximo 3 colores y el texto no se sale del borde"),
        ("Evaluar una seguridad", "Un portalápices tiene un borde de cartón con una punta que sobresale. ¿Qué criterio de seguridad falla y qué se hace?", ["Falla el criterio de bordes lisos y sin puntas.", "Se corrige antes que lo estético: se corta o dobla la punta."], "Falla bordes lisos; se corrige la punta primero"),
    ],
    mistakes=[
        ("Escribir «se ve lindo» como criterio estético.", "Es una opinión que no se puede comprobar.", "Escribe algo observable, como el número de colores."),
        ("Corregir los colores antes de una punta peligrosa.", "La seguridad es lo primero.", "Corrige primero lo que puede lastimar."),
    ],
    R=[
        ("¿Qué criterio es más importante si falla: el estético o el de seguridad?", "El de seguridad", "Se corrige antes."),
        ("Dos mitades iguales, como en un espejo, ¿es simetría o estabilidad?", "Simetría", "Es un criterio estético."),
        ("Un borde sin puntas, ¿es un criterio estético o de seguridad?", "De seguridad", "Evita que el producto lastime."),
    ],
    C=[
        ("¿Cuál es un criterio estético observable? A «Se ve genial», B «Usa máximo 3 colores».", "B", "Se puede contar."),
        ("¿Cómo compruebas la estabilidad de un soporte?", "Lo empujas suavemente para ver si se vuelca", "Es una prueba observable."),
        ("¿Por qué una pieza pequeña suelta es un riesgo?", "Puede perderse o tragarse", "Es un riesgo en objetos para niños."),
    ],
    A=[
        arith("Un cartel debe usar como máximo 3 colores. Usa 5. ¿Cuántos colores le sobran?", "5-3", "Se resta el máximo de los que usa.", " colores"),
        ("Un trabajo tiene una mancha de pegamento en el frente y un borde afilado. ¿Cuál se corrige primero?", "El borde afilado", "La seguridad va primero."),
        ("Un organizador se vuelca con un empujón suave. ¿Qué criterio de seguridad no cumple?", "La estabilidad", "Un producto estable no se vuelca fácilmente."),
    ],
    Z=[
        ("Rosa dice: «Prefiero dejar el borde filudo porque se ve más prolijo». ¿Está en lo correcto?", "No", "La seguridad prevalece sobre lo estético."),
        ("Un grupo evalúa dos carteles. El cartel A tiene 2 colores y el texto dentro del borde; el B tiene 6 colores y texto fuera del borde. Con criterios de máximo 3 colores y texto dentro del borde, ¿cuál cumple?", "El cartel A", "Cumple ambos criterios."),
    ],
    D=[
        arith("Una lista tiene 8 criterios, 5 estéticos y el resto de seguridad. ¿Cuántos son de seguridad?", "8-5", "Se resta lo estético del total.", " criterios"),
        ("Un producto cumple 4 de 5 criterios de seguridad y 5 de 5 estéticos. ¿Qué se corrige primero?", "El criterio de seguridad que falla", "Lo que puede lastimar va primero."),
    ],
    ctx=("Evalúas una repisa de cartón. Tiene esquinas lisas, no se vuelca al empujarla suave, tiene 4 colores y una mancha de pegamento. Los criterios son: esquinas lisas, no se vuelca, máximo 3 colores y sin manchas. Marca cuáles cumple y cuáles no.", "Cumple esquinas lisas y no se vuelca; no cumple máximo 3 colores ni sin manchas", "Se revisa cada criterio con lo observado."),
    sc=[
        ("¿Cómo se escribe un criterio estético?", "De forma observable", "Se puede contar o ver."),
        ("¿Qué gana si chocan lo estético y la seguridad?", "La seguridad", "Es el criterio más importante."),
        ("¿Cómo se comprueba que un borde es seguro?", "Pasando con cuidado un dedo por el borde", "Se detecta si hay puntas."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: un portalápices de cartón con 2 colores, un borde con una punta y una mancha de pegamento. Trabajo 2: una caja de cartulina con 5 colores, bordes lisos y estable. Escribe dos criterios estéticos observables y dos de seguridad, marca cuáles cumple, y qué corriges primero.",
        "Trabajo 1: estéticos: máximo 3 colores (cumple) y sin manchas (no). Seguridad: sin puntas (no) y estable (sí). Primero corrijo la punta",
        ["dos criterios estéticos observables", "dos criterios de seguridad", "marca lo que cumple", "prioriza la seguridad"],
        ["tabla de cuatro criterios con decisión"],
        ["criterios estéticos vagos", "corregir lo estético antes de lo seguro"],
        "Pregunta: «¿qué se ve u observa para saber si cumple?». Si es vago, pídele hacerlo medible.",
    ),
    reinforce="Escribe un criterio estético observable y uno de seguridad para un cuaderno forrado.",
    extend="Explica una situación en que un acabado muy bonito podría ser inseguro.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja y lápiz. Las pautas y los trabajos están escritos en este cuaderno.",
    use="Aprenderé a usar una pauta con niveles y puntajes para evaluar trabajos propios, de otros y en equipo. Sirve para evaluar de forma justa y comparable.",
    prior=["Sé qué son criterios de funcionamiento, técnicos, ambientales, estéticos y de seguridad.", "Sé sumar puntajes.", "Sé calcular un porcentaje."],
    explain=[
        "Una pauta de evaluación es una tabla con criterios y niveles. Por ejemplo: 3 puntos es «cumple totalmente», 2 es «cumple en parte» y 1 es «aún no cumple». Cada criterio recibe un puntaje y se suman para obtener el total. El total máximo es el número de criterios por 3.",
        "Evaluar en equipo significa que varias personas usan la misma pauta y comparan los resultados. Si dos personas ponen puntajes distintos, vuelven a mirar el trabajo y la evidencia hasta acordar. Evaluar el trabajo de otra persona exige respeto: se evalúa el producto, no a la persona.",
        "Para comunicar el resultado se puede usar el porcentaje de logro: puntaje obtenido por 100 dividido entre el puntaje máximo. Si un trabajo obtiene 12 de 15 puntos, el logro es 12 por 100 dividido en 15, o sea 80 %. El puntaje sirve para decidir qué criterio mejorar primero: el que tiene menos puntos. La excepción es la seguridad: si un criterio de seguridad falla, se corrige antes, aunque otro tenga menos puntos.",
    ],
    vocab=[("pauta", "tabla con criterios y niveles para evaluar"), ("nivel", "grado de logro de un criterio"), ("puntaje máximo", "mayor puntaje posible"), ("porcentaje de logro", "puntaje obtenido en relación con el máximo, sobre 100"), ("acordar", "ponerse de acuerdo después de revisar la evidencia")],
    worked=[
        ("Sumar los puntajes", "Una pauta tiene 5 criterios. Los puntajes de un trabajo son 3, 2, 3, 1 y 3. ¿Cuál es el total y el máximo?", ["Sumo: 3 + 2 + 3 + 1 + 3 = 12.", "Máximo: 5 criterios por 3 puntos son 15."], "12 de 15"),
        ("Calcular el porcentaje de logro", "Un trabajo obtiene 12 de 15 puntos. ¿Qué porcentaje de logro tiene?", ["Multiplico 12 por 100: 1.200.", "Divido 1.200 entre 15."], "80 %"),
    ],
    mistakes=[
        ("Evaluar a la persona y no al trabajo.", "No es justo ni útil para mejorar.", "Evalúa el producto con la pauta y la evidencia."),
        ("Poner puntaje sin mirar la evidencia.", "La evaluación no se puede explicar.", "Anota el dato que justifica cada puntaje."),
    ],
    R=[
        ("En una pauta de 3 niveles, ¿cuál es el puntaje más alto?", "3", "Cumple totalmente vale 3."),
        ("En Tecnología: ¿Se evalúa el trabajo o a la persona?", "El trabajo", "Se evalúa el producto, no a quien lo hizo."),
        ("Si dos personas ponen puntajes distintos, ¿qué hacen?", "Vuelven a mirar la evidencia hasta acordar", "Así la evaluación es justa."),
    ],
    C=[
        ("¿Para qué sirve una pauta?", "Para evaluar con criterios y niveles", "Permite comparar trabajos."),
        ("Si no hay ningún riesgo de seguridad, ¿qué criterio conviene mejorar primero?", "El que tiene menos puntos", "Es donde más falta."),
        ("¿Por qué anotar la evidencia al dar un puntaje?", "Para poder explicar la evaluación", "Sin evidencia no se justifica."),
    ],
    A=[
        arith("Una pauta tiene 4 criterios con puntajes 3, 3, 2 y 1. ¿Cuál es el total?", "3+3+2+1", "Se suman los puntajes.", " puntos"),
        arith("Una pauta tiene 6 criterios de 3 puntos máximos cada uno. ¿Cuál es el puntaje máximo?", "6*3", "Se multiplica el número de criterios por 3.", " puntos"),
        arith("Un trabajo obtiene 9 de 12 puntos. ¿Qué porcentaje de logro tiene?", "9*100//12", "Se multiplica por 100 y se divide entre el máximo.", " %"),
    ],
    Z=[
        ("Dos equipos evaluaron el mismo trabajo: uno dio 13 de 15 puntos y el otro 8 de 15. ¿Qué hacen?", "Revisar juntos la evidencia hasta acordar", "Una diferencia grande indica que miraron cosas distintas."),
        ("Un compañero obtiene 6 de 15 y otro dice: «Eres malo para esto». ¿Qué se debió decir?", "Que el trabajo cumple pocos criterios y cuáles mejorar", "Se evalúa el producto con respeto."),
    ],
    D=[
        arith("En una pauta de 5 criterios, un trabajo tiene puntajes 2, 1, 1, 1 y 1. ¿Qué porcentaje de logro obtiene sobre el máximo?", "(2+1+1+1+1)*100//15", "Se suma el total, se multiplica por 100 y se divide entre 15.", " %"),
        ("Un trabajo obtiene 3 en funcionamiento, 3 en técnico, 1 en ambiental, 2 en estético y 3 en seguridad. ¿Cuál criterio se mejora primero?", "El ambiental", "Es el que tiene menor puntaje."),
    ],
    ctx=("Tu equipo evalúa un organizador de cartón con la pauta de 5 criterios: funcionamiento 2, técnico 1, ambiental 3, estético 1 y seguridad 2. Calcula el total, el máximo, el porcentaje de logro y el criterio a mejorar primero.", "Total 9 de 15; logro 60 %; mejorar primero el técnico o el estético, ambos con 1", "9 × 100 ÷ 15 = 60; hay dos criterios con el menor puntaje."),
    sc=[
        ("¿Qué incluye una pauta?", "Criterios y niveles con puntajes", "Se evalúa con ellos."),
        ("¿Cómo se calcula el porcentaje de logro?", "Puntaje obtenido por 100 dividido entre el máximo", "Relaciona lo obtenido con lo posible."),
        ("¿Qué se evalúa: el producto o la persona?", "El producto", "Se cuida el respeto."),
    ],
    open_task=(
        "Escoge un trabajo ficticio. Trabajo 1: un marcador de libros con funcionamiento 3, técnico 3, ambiental 1, estético 2 y seguridad 3. Trabajo 2: una caja con funcionamiento 2, técnico 2, ambiental 3, estético 1 y seguridad 1. Calcula el total sobre 15, el porcentaje de logro y escribe qué criterio mejorarías primero y por qué.",
        "Trabajo 1: 12 de 15; 80 %. Mejorar primero el ambiental, que tiene 1 punto",
        ["suma el total", "calcula el máximo", "calcula el porcentaje", "elige el criterio a mejorar con razón"],
        ["tabla con totales y decisión"],
        ["sumar mal", "evaluar a la persona"],
        "Pregunta: «¿cuál criterio tiene el puntaje más bajo?». Revisa el orden de mejora.",
    ),
    reinforce="Evalúa con una pauta de 3 criterios un dibujo tuyo: está limpio, usa dos colores y tiene título.",
    extend="Explica por qué dos personas pueden dar puntajes distintos y cómo resolverlo.",
)

# ------------------------------------------------------------------ OA 04, clase 5
reg(
    OA4, 5,
    materials="Hoja y lápiz. Los comentarios y casos están escritos en este cuaderno.",
    use="Aprenderé a dialogar sobre los resultados de una evaluación con respeto, usando evidencia. Sirve para que las demás personas entiendan y puedan mejorar su trabajo.",
    prior=["Sé evaluar con una pauta.", "Sé calcular un porcentaje de logro.", "Sé escuchar sin interrumpir."],
    explain=[
        "Dialogar sobre los resultados es conversar para entender qué salió bien, qué falló y qué se puede mejorar. Una buena retroalimentación tiene tres partes: lo que se observa con un dato, el criterio al que se refiere y una sugerencia. Ejemplo: «Tu base mide 18 cm y el criterio pedía 20 cm; podrías agrandarla 2 cm».",
        "Cuando recibes comentarios, escucha completo, pregunta si no entiendes y agradece. No tienes que estar de acuerdo con todo, pero sí revisar la evidencia. Cuando das comentarios, habla del trabajo y no de la persona, usa un tono amable, empieza por algo que sí cumple y propone mejoras posibles de hacer.",
        "Si tu equipo no está de acuerdo, vuelvan al criterio y a la evidencia. Decidan juntos qué corregir primero y quién lo hará. Anoten el acuerdo. Un diálogo respetuoso permite mejorar el trabajo y ayuda a que todas las personas se sientan escuchadas.",
    ],
    vocab=[("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("sugerencia", "propuesta de mejora"), ("evidencia", "dato que apoya un comentario"), ("acuerdo", "decisión tomada entre varias personas"), ("respeto", "tratar con consideración a las demás personas")],
    worked=[
        ("Armar un comentario con tres partes", "Observas que un puente de papel soportó 80 g y el criterio pedía 100 g. Escribe un comentario con dato, criterio y sugerencia.", ["Dato: soportó 80 g.", "Criterio: pedía 100 g. Sugerencia: aumentar el grosor del papel."], "«Tu puente soportó 80 g y el criterio pedía 100 g; podrías usar un papel más grueso»"),
        ("Revisar un comentario", "«Tu trabajo está feo y eres desordenado.» ¿Cómo lo reescribes?", ["Quito lo que habla de la persona.", "Hablo del trabajo con un dato y una sugerencia."], "«Tu trabajo tiene 3 manchas de pegamento; podrías limpiarlas con un trapo húmedo»"),
    ],
    mistakes=[
        ("Decir «me gustó» o «no me gustó» sin motivo.", "No ayuda a mejorar.", "Agrega un dato, un criterio y una sugerencia."),
        ("Defenderse de inmediato ante un comentario.", "No se escucha la evidencia.", "Escucha completo, pregunta y revisa el dato."),
    ],
    R=[
        ("¿Cuántas partes tiene un buen comentario en esta clase?", "Tres", "Dato, criterio y sugerencia."),
        ("¿Se habla del trabajo o de la persona?", "Del trabajo", "Es un comentario respetuoso."),
        ("¿Qué se hace primero al recibir un comentario?", "Escuchar completo", "Así se entiende bien."),
    ],
    C=[
        ("¿Cuál comentario es mejor? A «Está mal», B «La base mide 18 cm y el criterio pedía 20 cm; podrías agrandarla».", "B", "Tiene dato, criterio y sugerencia."),
        ("¿Por qué conviene empezar por algo que sí cumple?", "Porque muestra respeto y reconoce lo logrado", "Ayuda a recibir bien la mejora."),
        ("Si tu equipo no está de acuerdo, ¿qué hacen?", "Volver al criterio y a la evidencia", "Así deciden con datos."),
    ],
    A=[
        arith("El criterio pedía 25 cm de alto y el trabajo mide 21 cm. ¿Cuántos centímetros debería agregar según tu sugerencia?", "25-21", "Se resta lo que mide del criterio.", " cm"),
        ("Elige la sugerencia con respeto y dato. A «Eres lento, apúrate», B «El trabajo está terminado al 60 %; podrías dedicar 15 minutos a pegar las partes».", "B", "Habla del trabajo con un dato."),
        ("Una compañera te dice que tu cartel tiene 6 colores y el criterio permite 3. ¿Qué haces primero?", "Reviso el criterio y cuento los colores", "La evidencia permite decidir."),
    ],
    Z=[
        ("Un grupo dice: «Los comentarios son para molestar». ¿Qué respuesta explica mejor para qué sirven?", "Sirven para mejorar el trabajo con evidencia", "Una buena retroalimentación ayuda."),
        ("Dos personas discuten si la caja cierra bien. ¿Qué dato resuelve la discusión?", "Probar tres veces y anotar los resultados", "La evidencia resuelve sin pelear."),
    ],
    D=[
        arith("Un comentario sugiere reducir el peso de 450 g a 400 g. ¿Cuántos gramos hay que sacar?", "450-400", "Se resta el peso meta del actual.", " g"),
        ("Un compañero responde a un comentario diciendo «no me importa». ¿Qué conviene? A burlarse de él, B preguntarle qué dato cree que muestra que cumple el criterio.", "B", "Vuelve a la evidencia sin atacar."),
    ],
    ctx=("Revisas un marcador de libros que mide 18 cm y el criterio pedía 20 cm, y la tira se despega en una de tres pruebas. Escribe un comentario con dato, criterio y sugerencia, y una cosa que sí cumple.", "Tu marcador mide 18 cm y el criterio pedía 20 cm; podrías agregar 2 cm. Sí cumple el pegado en 2 de 3 pruebas", "Incluye un dato, un criterio, una sugerencia y algo positivo."),
    sc=[
        ("¿Qué partes tiene un buen comentario?", "Dato, criterio y sugerencia", "Es la estructura de la clase."),
        ("¿Se critica a la persona?", "No", "Se habla del trabajo."),
        ("¿Qué se anota al llegar a un acuerdo?", "Qué se corrige y quién lo hará", "Deja claro el plan."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: un portalápices que mide 12 cm y el criterio pedía 14 cm, con una unión suelta. Trabajo 2: un afiche con 5 colores cuando el criterio permitía 3, pero con letras legibles. Escribe un comentario con dato, criterio, sugerencia y algo positivo, y una pregunta para entender el punto de vista de quien lo hizo.",
        "Trabajo 2: tu afiche tiene letras legibles; usa 5 colores y el criterio permitía 3; podrías quitar 2 colores. ¿Qué colores te parecen más importantes?",
        ["dato, criterio y sugerencia", "algo positivo", "habla del trabajo", "incluye una pregunta"],
        ["comentario escrito con pregunta"],
        ["opinar sin dato", "hablar de la persona"],
        "Pregunta: «¿cuál es el dato y cuál la sugerencia?». Si falta alguno, pídele completarlo.",
    ),
    reinforce="Reescribe este comentario con respeto y dato: «Tu dibujo es horrible».",
    extend="Explica cómo cambia un diálogo cuando se vuelve a la evidencia en vez de discutir quién tiene razón.",
)

# ------------------------------------------------------------------ OA 04, clase 6
reg(
    OA4, 6,
    materials="Hoja y lápiz. Los registros están escritos en este cuaderno.",
    use="Aprenderé a decidir qué corregir primero, a aplicar correcciones y a volver a evaluar. Sirve para que el producto mejore de verdad.",
    prior=["Sé evaluar con una pauta.", "Sé dar retroalimentación.", "Sé comparar datos antes y después."],
    explain=[
        "Aplicar correcciones es cambiar el trabajo para cumplir mejor los criterios. Primero se ordenan los problemas: los de seguridad van primero, luego los de funcionamiento, los técnicos, los ambientales y al final los estéticos. Así se evita que un producto bonito siga siendo peligroso.",
        "Cada corrección se hace con una sola acción clara y se anota en un registro: qué problema era, qué se cambió, quién lo hizo y cuándo. Después se vuelve a evaluar con la misma pauta. Se comparan los puntajes de antes y de después. Si mejoran, la corrección funcionó; si no, se prueba otra.",
        "Evaluar y corregir son un ciclo: evaluar, dialogar, corregir y volver a evaluar. Nunca se termina del todo, pero se puede decidir que el producto ya cumple lo necesario. Cuando el producto cumple los criterios acordados, se escribe una conclusión con datos: qué mejoró, cuánto y qué se aprendió.",
    ],
    vocab=[("corrección", "cambio que mejora un criterio que no se cumple"), ("prioridad", "lo que se atiende primero"), ("registro", "anotación de lo que se hizo"), ("ciclo", "pasos que se repiten: evaluar, corregir y volver a evaluar"), ("conclusión", "decisión final apoyada en datos")],
    worked=[
        ("Ordenar las correcciones", "Problemas de un soporte: A color despareja, B punta que sobresale, C base que se vuelca. ¿En qué orden se corrigen?", ["La punta y el vuelco son de seguridad; van primero.", "Luego lo estético."], "Punta, vuelco (base) y por último el color"),
        ("Comparar antes y después", "Antes la pauta dio 9 de 15 puntos. Después de corregir dio 13 de 15. ¿Cuánto mejoró?", ["Resto 13 − 9.", "Son 4 puntos más."], "Mejoró 4 puntos"),
    ],
    mistakes=[
        ("Corregir varias cosas a la vez sin anotar.", "Después no se sabe qué cambió el resultado.", "Corrige y anota una cosa por vez."),
        ("No volver a evaluar tras corregir.", "No se sabe si mejoró.", "Aplica de nuevo la pauta."),
    ],
    R=[
        ("¿Qué se corrige primero: lo de seguridad o lo estético?", "Lo de seguridad", "Evita que el producto lastime."),
        ("¿Qué se hace después de corregir?", "Volver a evaluar", "Para saber si mejoró."),
        ("¿Qué se anota en el registro de correcciones?", "Qué problema había, qué se cambió, quién y cuándo", "Deja evidencia del proceso."),
    ],
    C=[
        ("¿Por qué conviene corregir una cosa por vez?", "Para saber qué cambió el resultado", "Así se entiende el efecto."),
        ("Si tras corregir los puntajes no mejoran, ¿qué se hace?", "Probar otra corrección", "La primera no funcionó."),
        ("¿Qué significa que evaluar y corregir son un ciclo?", "Que se repiten hasta cumplir los criterios", "Cada ciclo busca mejorar."),
    ],
    A=[
        arith("Antes de corregir un trabajo tenía 8 de 15 puntos y después tiene 12. ¿Cuántos puntos subió?", "12-8", "Se resta el puntaje de antes del de después.", " puntos"),
        arith("Un trabajo tenía 40 % de logro y ahora tiene 85 %. ¿Cuántos puntos porcentuales subió?", "85-40", "Se resta el logro anterior del actual.", " puntos"),
        ("Problemas: A pared sin pintar, B esquina filuda, C pieza floja. ¿Cuál se corrige primero?", "La esquina filuda", "Es un riesgo de seguridad."),
    ],
    Z=[
        ("Un grupo cambió el color, el tamaño y el material a la vez y el puntaje subió. ¿Por qué no saben cuál corrección ayudó?", "Porque cambiaron varias cosas a la vez", "No se puede aislar el efecto."),
        ("Una corrección bajó el puntaje de 12 a 10. ¿Qué se hace?", "Volver a la versión anterior y probar otra corrección", "Una corrección debe mejorar."),
    ],
    D=[
        arith("En 3 ciclos de evaluación, un trabajo subió 2 puntos en cada uno. Partió con 7 puntos. ¿Cuántos puntos tiene al final?", "7+3*2", "Se suman 3 aumentos de 2 puntos.", " puntos"),
        arith("Un trabajo obtiene 10 de 15 puntos. Para llegar a un logro de 100 % (15 de 15), ¿cuántos puntos debe ganar?", "15-10", "Se resta lo obtenido del máximo.", " puntos"),
    ],
    ctx=("Una repisa de cartón obtuvo 9 de 15 puntos. Los problemas son: base que se vuelca, pared con mancha y color desparejo. Escribe el orden de corrección, una acción para el primer problema y el puntaje que esperas tras corregir.", "Orden: base que se vuelca, mancha, color. Acción: ensanchar la base 4 cm. Puntaje esperado: más de 9", "Se prioriza la seguridad y se vuelve a evaluar."),
    sc=[
        ("¿Qué problema se corrige primero?", "El de seguridad", "Es lo más importante."),
        ("¿Qué se hace tras corregir?", "Volver a evaluar con la misma pauta", "Así se pueden comparar los puntajes."),
        ("¿Qué se escribe al terminar?", "Una conclusión con datos", "Resume qué mejoró."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un puente de cartón con puntajes antes de 8 de 15, con una pieza floja, un borde filudo y manchas. Caso 2: una caja con puntaje antes de 10 de 15, con tapa que no cierra, esquina rota y color desparejo. Ordena los problemas, escribe una corrección para cada uno, un registro y el puntaje que esperas lograr.",
        "Caso 2: esquina rota, tapa que no cierra, color desparejo. Correcciones: reforzar la esquina con cartón y cola fría, ajustar la tapa, repintar. Puntaje esperado: 13",
        ["ordena los problemas", "una corrección por problema", "registro con qué, quién y cuándo", "puntaje esperado"],
        ["lista ordenada de correcciones con registro"],
        ["corregir sin orden", "no volver a evaluar"],
        "Pregunta: «¿qué corriges primero y por qué?». Si no es la seguridad, repasa la prioridad.",
    ),
    reinforce="Elige un trabajo escolar tuyo, escribe un problema y una corrección y anota cómo comprobarás que mejoró.",
    extend="Explica por qué evaluar, corregir y volver a evaluar es un ciclo que mejora un producto.",
)
