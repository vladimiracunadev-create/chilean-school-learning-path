"""Cuaderno del estudiante de 6.º básico Matemática: OA 03 (razones) y OA 04 (porcentajes)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_ma06_a import M, W, lesson, task

OA3 = "MA06 OA 03"

# ------------------------------------------------------------------ OA 03 clase 1
lesson(
    OA3, 1,
    use="Aprenderé qué es una razón y cómo se escribe. Sirve para comparar dos cantidades, por ejemplo cuántas niñas hay por cada niño en un curso.",
    prior=["Sé contar objetos y comparar cantidades.", "Sé qué es una fracción."],
    explain=[
        "Una razón es una comparación entre dos cantidades. Si en una mesa hay 3 gatos de peluche y 5 perros de peluche, la razón entre gatos y perros es 3 a 5. Se escribe 3 : 5 y se lee «tres es a cinco». También se puede escribir como fracción, 3/5.",
        "Cada número de una razón se llama término. El orden de los términos importa mucho. La razón de gatos a perros es 3 : 5, pero la razón de perros a gatos es 5 : 3. Son razones distintas porque comparan en otro orden. Siempre fíjate en qué se pide primero.",
        "Una razón puede comparar una parte con otra parte, como niñas con niños, o una parte con el total, como niñas con todas las personas. En una razón no se resta: se comparan las cantidades tal como son. Las dos cantidades pueden ser del mismo tipo, como personas con personas, o de tipos distintos, como bicicletas con ruedas. Siempre se escribe primero lo que se nombra primero.",
    ],
    vocab=[("razón", "comparación entre dos cantidades"), ("término", "cada uno de los dos números de una razón"), ("a : b", "se lee «a es a b»"), ("parte", "una de las cantidades que forman un grupo"), ("total", "todas las cantidades juntas")],
    worked=[
        W("Escribir una razón en los dos órdenes", "En un curso hay 12 niñas y 18 niños. Escribe la razón entre niñas y niños y la razón entre niños y niñas.", ["Niñas a niños: primero las niñas, 12 : 18.", "Niños a niñas: primero los niños, 18 : 12."], "12 : 18 y 18 : 12"),
        W("Razón de una parte con el total", "Una bolsa tiene 4 bolitas rojas, 6 azules y 2 verdes. Escribe la razón entre las rojas y todas las bolitas.", ["Total de bolitas: 4 + 6 + 2 = 12.", "Rojas a total: 4 : 12."], "4 : 12"),
    ],
    mistakes=[
        M("Escribir 5 : 3 para «3 gatos y 5 perros» cuando se pide gatos a perros.", "Se invirtió el orden de los términos.", "La razón gatos a perros es 3 : 5; el primero que se nombra va primero."),
        M("Restar los términos para decir que la razón es 2.", "Se confundió razón con diferencia.", "La razón 3 : 5 se queda escrita como 3 : 5; no se resta."),
    ],
    rec=[
        ex("Hay 7 libros y 4 revistas. Escribe la razón entre libros y revistas.", "7 : 4", "Se nombran primero los libros."),
        ex("En la razón 9 : 4, ¿cuál es el primer término?", "9", "El primer término es el que está antes de los dos puntos."),
        ex("En una caja hay 3 lápices azules y 8 rojos. Escribe la razón entre lápices rojos y azules.", "8 : 3", "Primero se nombran los rojos."),
    ],
    und=[
        ex("Un equipo ganó 6 partidos y perdió 2. Escribe la razón entre partidos ganados y perdidos.", "6 : 2", "Ganados es lo primero que se nombra."),
        ex("En un grupo de 10 estudiantes, 4 usan lentes. Escribe la razón entre quienes usan lentes y quienes no.", "4 : 6", "Los que no usan lentes son 10 − 4 = 6."),
        ex("En 5 bicicletas hay 10 ruedas. Escribe la razón entre bicicletas y ruedas.", "5 : 10", "Se nombra primero la cantidad de bicicletas."),
    ],
    app=[
        ex("Una receta usa 2 tazas de harina y 3 tazas de agua. Escribe la razón entre el agua y la harina.", "3 : 2", "El agua se nombra primero."),
        ex("En una fila hay 15 estudiantes y 9 son niñas. Escribe la razón entre niñas y todos los estudiantes.", "9 : 15", "Las niñas son la parte y los 15 son el total."),
        ex("En un patio hay 4 mesas y 12 sillas. Escribe la razón entre mesas y sillas.", "4 : 12", "Las mesas se nombran primero."),
    ],
    rea=[
        ex("Ema dice que las razones 3 : 5 y 5 : 3 son lo mismo porque tienen los mismos números. ¿Tiene razón?", "No", "Comparan en distinto orden: una dice 3 de lo primero por 5 de lo segundo, la otra al revés."),
        ex("En un frasco hay 8 bolitas rojas y 12 azules. Tomás escribió 12 : 8 como razón entre rojas y azules. ¿Cuál es la razón correcta?", "8 : 12", "Las rojas se nombran primero, así que va 8 : 12."),
    ],
    cha=[
        ex("Una bolsa tiene fichas rojas y azules. La razón entre rojas y azules es 3 : 2 y hay 3 fichas rojas. ¿Cuántas fichas hay en total?", "5", "Si hay 3 rojas, hay 2 azules, y 3 + 2 = 5."),
        ex("Mira la fila de letras A A B A B B A. Escribe la razón entre la cantidad de A y la cantidad de B.", "4 : 3", "Hay 4 letras A y 3 letras B."),
    ],
    ctx=[ex("En una encuesta ficticia a 20 personas, 13 prefieren té y 7 prefieren café. Escribe la razón entre quienes prefieren té y quienes prefieren café.", "13 : 7", "Se nombra primero a quienes prefieren té.")],
    sc=[
        ex("Hay 5 manzanas y 9 peras. Escribe la razón entre peras y manzanas.", "9 : 5", "Primero se nombran las peras."),
        ex("En la razón 4 : 7, ¿cuál es el segundo término?", "7", "El segundo término es el que va después de los dos puntos."),
        ex("Un curso tiene 14 niños y 16 niñas. Escribe la razón entre niñas y niños.", "16 : 14", "Se nombran primero las niñas."),
    ],
    op=task(
        "En un cajón hay 6 calcetines blancos, 4 negros y 5 azules. Escribe tres razones distintas con estos datos, por ejemplo blancos a negros, azules al total y negros a azules, e indica con una frase qué compara cada una.",
        "Blancos a negros: 6 : 4. Azules al total (6 + 4 + 5 = 15): 5 : 15. Negros a azules: 4 : 5. La primera compara dos partes y la segunda una parte con el total.",
        ["escribe razones con el orden correcto", "calcula bien el total", "explica qué compara cada razón"],
        ["tres razones escritas", "frase que explica cada una"],
        ["invertir el orden de los términos", "olvidar sumar el total"],
        "Pide que lea cada razón con la palabra «es a» y compruebe que nombra primero lo que pide.",
    ),
    reinforce="Cuenta cuántos lápices y cuántos cuadernos tienes en tu mochila o en tu escritorio, o usa 5 lápices y 3 cuadernos. Escribe la razón entre lápices y cuadernos y luego al revés.",
    extend="Inventa una situación con dos cantidades y escribe sus dos razones posibles. Explica qué dice cada una.",
)

# ------------------------------------------------------------------ OA 03 clase 2
lesson(
    OA3, 2,
    use="Aprenderé a representar una razón con dibujos, tablas, la expresión «por cada» y la fracción. Sirve para entender la misma razón de varias maneras.",
    prior=["Sé escribir una razón a : b.", "Sé que el orden de los términos importa."],
    explain=[
        "Una razón se puede representar de varias maneras. Con dibujos: ● ● ● y ○ ○ ○ ○ ○ muestran 3 círculos negros por 5 blancos. Con una tabla que cuenta cuántos hay de cada tipo. Con palabras: «por cada 3 negros hay 5 blancos». Y con símbolos, 3 : 5.",
        "Cuando comparas una parte con el total, la razón se puede escribir como fracción. En ● ● ● ○ ○ ○ ○ ○ hay 8 círculos en total. La razón entre negros y total es 3 : 8, que se escribe como la fracción 3/8. Pero la razón entre negros y blancos, 3 : 5, no es «tres quintos del total».",
        "Para leer una tabla o un gráfico, primero identifica las cantidades que se comparan. Luego escribe la razón en el orden que pide la pregunta. Si hace falta un total, súmalo antes. Cambiar la representación no cambia la razón: es la misma comparación mostrada de otra forma.",
    ],
    vocab=[("representar", "mostrar algo con un dibujo, tabla, símbolo o palabras"), ("por cada", "expresión que indica cuántos hay de una cosa por cierta cantidad de otra"), ("tabla", "cuadro donde se ordenan datos en filas y columnas"), ("parte con parte", "razón que compara dos grupos del mismo todo"), ("parte con total", "razón que compara un grupo con todo el conjunto")],
    worked=[
        W("De un dibujo a una razón", "En un dibujo hay ● ● ● y ○ ○ ○ ○ ○. Escribe la razón entre negros y blancos y la razón entre negros y el total.", ["Negros: 3. Blancos: 5. Total: 3 + 5 = 8.", "Negros a blancos: 3 : 5. Negros a total: 3 : 8, o la fracción 3/8."], "3 : 5 y 3 : 8"),
        W("De una tabla a una razón", "Una tabla dice: manzanas 6, peras 3. Escribe la razón entre peras y manzanas, y entre peras y todas las frutas.", ["Peras: 3, manzanas: 6, total: 6 + 3 = 9.", "Peras a manzanas: 3 : 6. Peras a total: 3 : 9."], "3 : 6 y 3 : 9"),
    ],
    mistakes=[
        M("Decir que ●●● ○○○○○ muestra 3/5 del total son negros.", "Se usó la razón parte con parte como si fuera parte con total.", "Del total de 8, 3 son negros: 3/8."),
        M("Escribir 4 : 6 para ■ ■ ■ ■ ▲ ▲ cuando se pide ■ con ▲.", "Se contó mal una de las dos cantidades.", "Cuenta cada símbolo por separado: hay 4 ■ y 2 ▲, entonces 4 : 2."),
    ],
    rec=[
        ex("«Por cada 3 niños hay 2 niñas». Escribe la razón entre niñas y niños.", "2 : 3", "Se nombran primero las niñas."),
        ex("Mira ■ ■ ■ ■ ▲ ▲. Escribe la razón entre ■ y ▲.", "4 : 2", "Hay 4 cuadrados y 2 triángulos."),
        ex("Escribe la razón 5 : 9 como fracción.", "5/9", "El primer término es el numerador y el segundo el denominador."),
    ],
    und=[
        ex("Mira ★ ★ ✿ ✿ ✿ ✿ ✿ ✿. Escribe la razón entre ✿ y el total de figuras.", "6 : 8", "Hay 6 ✿ y 2 ★, el total es 8."),
        ex("Una tabla de votos dice: rojo 12, azul 8, verde 5. Escribe la razón entre los votos azul y el total de votos.", "8 : 25", "El total de votos es 12 + 8 + 5 = 25."),
        ex("En 10 días hubo 7 con lluvia. Escribe la razón entre los días sin lluvia y los días con lluvia.", "3 : 7", "Días sin lluvia: 10 − 7 = 3."),
    ],
    app=[
        ex("Una semana tiene 7 días y 5 son de clases. Escribe la razón entre días de clases y días sin clases.", "5 : 2", "Días sin clases: 7 − 5 = 2."),
        ex("Una bolsa tiene 6 caramelos de fresa, 8 de limón y 4 de naranja. Escribe la razón entre los de limón y los de las otras dos frutas juntas.", "8 : 10", "Fresa y naranja suman 6 + 4 = 10."),
        ex("En una semana un equipo hizo 4 goles el lunes, 6 el martes y 2 el miércoles. Escribe la razón entre los goles del martes y el total de goles.", "6 : 12", "El total es 4 + 6 + 2 = 12."),
    ],
    rea=[
        ex("En un grupo hay 3 niñas y 5 niños. Lucía dice que 3/5 de las personas son niñas. ¿Qué fracción del total son niñas?", "3/8", "Hay 3 + 5 = 8 personas; 3/5 compara niñas con niños, no con el total."),
        ex("Raúl miró ★ ★ ★ ★ ✿ ✿ y escribió que la razón entre ★ y ✿ es 4 : 6. ¿Cuál es la razón correcta?", "4 : 2", "Hay 4 ★ y solo 2 ✿; el 6 es el total."),
    ],
    cha=[
        ex("Un dibujo repite dos veces el grupo ● ● ○ ○ ○. ¿Cuántos ○ hay en total?", "6", "Cada grupo tiene 3 ○, y 2 × 3 = 6."),
        ex("De 9 personas, 4 son mujeres. Escribe la razón entre hombres y mujeres.", "5 : 4", "Hombres: 9 − 4 = 5."),
    ],
    ctx=[ex("En un curso ficticio de 30 estudiantes, 10 llegan en bicicleta y el resto de otra forma. Escribe la razón entre quienes llegan en bicicleta y todo el curso.", "10 : 30", "Los 10 son la parte y los 30 son el total.")],
    sc=[
        ex("«Por cada 4 vasos de agua se pone 1 vaso de jugo». Escribe la razón entre jugo y agua.", "1 : 4", "Se nombra primero el jugo."),
        ex("Mira ▲ ▲ ▲ ■ ■ ■ ■ ■ ■ ■. Escribe la razón entre ▲ y el total de figuras.", "3 : 10", "Hay 3 ▲ y 7 ■, el total es 10."),
        ex("Escribe la razón 7 : 12 como fracción.", "7/12", "El primer término va arriba."),
    ],
    op=task(
        "Mira este dibujo: ● ● ● ● ○ ○ ○ ▲ ▲. Haz una tabla que cuente cada símbolo y escribe tres razones: ● con ○, ▲ con el total y ○ con ▲. Escribe «por cada» en una de ellas.",
        "● 4, ○ 3, ▲ 2, total 9. ● con ○: 4 : 3. ▲ con el total: 2 : 9. ○ con ▲: 3 : 2. Por cada 4 ● hay 3 ○.",
        ["cuenta bien cada símbolo", "escribe las razones en orden", "usa «por cada» correctamente"],
        ["tabla de conteo", "tres razones y una frase con «por cada»"],
        ["contar mal los símbolos", "confundir parte con total"],
        "Pide que revise que la suma de los símbolos da el total antes de escribir la razón con el total.",
    ),
    reinforce="Dibuja 5 círculos y 2 cuadrados. Escribe la razón entre círculos y cuadrados, y la razón entre cuadrados y el total.",
    extend="Elige dos colores y dibuja un patrón de 12 figuras. Escribe tres razones diferentes con ese patrón y di cuál compara una parte con el total.",
)

# ------------------------------------------------------------------ OA 03 clase 3
lesson(
    OA3, 3,
    use="Aprenderé a encontrar razones equivalentes y a usarlas para completar tablas y comparar mezclas. Sirve para ampliar o reducir recetas sin cambiar el resultado.",
    prior=["Sé escribir una razón.", "Sé multiplicar y dividir."],
    explain=[
        "Dos razones son equivalentes cuando comparan lo mismo, aunque tengan números distintos. Si multiplicas o divides los dos términos de una razón por el mismo número, obtienes una razón equivalente. Por ejemplo, 2 : 3 es equivalente a 4 : 6 (multiplicando por 2) y a 6 : 9 (multiplicando por 3).",
        "Para completar una razón equivalente, busca por cuánto se multiplicó un término y haz lo mismo con el otro. En 3 : 5 = 9 : ?, el 3 se multiplicó por 3, así que el 5 también: 5 × 3 = 15. Para simplificar una razón, divide ambos términos por un factor común: 12 : 18 se divide por 6 y queda 2 : 3.",
        "Para comparar dos mezclas, llévalas al mismo tamaño usando razones equivalentes. Una mezcla con 2 cucharadas por 4 vasos y otra con 3 cucharadas por 8 vasos se comparan llevándolas a 8 vasos: la primera sería 4 cucharadas por 8 vasos. Sumar el mismo número a los dos términos no mantiene la razón.",
    ],
    vocab=[("razones equivalentes", "razones que comparan lo mismo con números distintos"), ("amplificar", "multiplicar los dos términos por el mismo número"), ("simplificar", "dividir los dos términos por el mismo número"), ("factor común", "número que divide a los dos términos"), ("mezcla", "unión de cantidades de dos o más cosas")],
    worked=[
        W("Completar una razón equivalente", "Una pintura usa 2 tarros de amarillo por cada 3 de azul. ¿Cuántos de azul se necesitan para 8 tarros de amarillo?", ["De 2 a 8 se multiplicó por 4.", "El 3 se multiplica también por 4: 3 × 4 = 12."], "12 tarros de azul"),
        W("Decidir si dos razones son equivalentes", "¿Son equivalentes 6 : 9 y 10 : 15?", ["Simplifico 6 : 9 dividiendo por 3: queda 2 : 3.", "Simplifico 10 : 15 dividiendo por 5: queda 2 : 3."], "Sí, las dos son 2 : 3"),
    ],
    mistakes=[
        M("Decir que 2 : 3 y 4 : 5 son equivalentes porque se sumó 2 a cada término.", "Se sumó en vez de multiplicar.", "La equivalente de 2 : 3 multiplicando por 2 es 4 : 6."),
        M("Simplificar 12 : 18 como 6 : 9 y detenerse.", "Se dividió por 2 y aún se puede dividir.", "Divide por 6 de una vez: 2 : 3."),
    ],
    rec=[
        ex("Completa 1 : 2 = 3 : ?", "6", "Se multiplicó por 3, así que 2 × 3 = 6."),
        ex("Escribe una razón equivalente a 2 : 5 multiplicando por 2.", "4 : 10", "2 × 2 = 4 y 5 × 2 = 10."),
        ex("Simplifica 6 : 8 dividiendo por 2.", "3 : 4", "6 ÷ 2 = 3 y 8 ÷ 2 = 4."),
    ],
    und=[
        ex("Simplifica 15 : 20 lo más posible.", "3 : 4", "Se divide por 5 ambos términos."),
        ex("Completa 4 : 7 = 12 : ?", "21", "De 4 a 12 se multiplicó por 3; 7 × 3 = 21."),
        ex("¿Son equivalentes 20 : 12 y 5 : 3? Responde sí o no.", "Sí", "Dividiendo 20 : 12 por 4 resulta 5 : 3."),
    ],
    app=[
        ex("Un jugo usa 3 vasos de concentrado por cada 7 de agua. ¿Cuántos vasos de concentrado se necesitan para 21 vasos de agua?", "9", "De 7 a 21 se multiplicó por 3, y 3 × 3 = 9."),
        ex("Un cemento se prepara con 5 palas de arena por cada 2 de cemento. ¿Cuántas palas de cemento se necesitan para 20 palas de arena?", "8", "De 5 a 20 se multiplicó por 4, y 2 × 4 = 8."),
        ex("La mezcla A lleva 3 cucharadas de azúcar por 5 vasos de agua. La B lleva 5 cucharadas por 8 vasos. ¿Cuál queda más dulce, A o B?", "B", "Con 40 vasos de agua, A llevaría 24 cucharadas (3 : 5 = 24 : 40) y B llevaría 25 (5 : 8 = 25 : 40); B tiene más azúcar por la misma agua."),
    ],
    rea=[
        ex("Carla dice que 2 : 3 y 4 : 5 son equivalentes porque sumó 2 a cada término. ¿Cuál es la razón equivalente a 2 : 3 que tiene 4 como primer término?", "4 : 6", "Se multiplica por 2, no se suma."),
        ex("¿12 : 18 y 18 : 12 son equivalentes? Responde sí o no.", "No", "Una es 2 : 3 y la otra 3 : 2; comparan en distinto orden."),
    ],
    cha=[
        ex("Escribe la razón equivalente a 6 : 10 que tenga 25 como segundo término. ¿Cuál es el primer término?", "15", "6 : 10 se simplifica a 3 : 5 y al multiplicar por 5 resulta 15 : 25."),
        ex("En un curso la razón entre niñas y niños es 3 : 4 y hay 28 estudiantes. ¿Cuántas niñas hay?", "12", "Cada grupo de 7 tiene 3 niñas y 4 niños; 28 son 4 grupos, entonces 3 × 4 = 12 niñas."),
    ],
    ctx=[ex("Una receta de pan para 4 personas usa 6 tazas de harina. ¿Cuántas tazas de harina se necesitan para 12 personas?", "18", "De 4 a 12 personas se multiplicó por 3; 6 × 3 = 18.")],
    sc=[
        ex("Completa 2 : 7 = 6 : ?", "21", "Se multiplicó por 3, y 7 × 3 = 21."),
        ex("Simplifica 18 : 24.", "3 : 4", "Se divide por 6."),
        ex("¿Son equivalentes 3 : 4 y 9 : 12? Responde sí o no.", "Sí", "Multiplicando 3 : 4 por 3 se obtiene 9 : 12."),
    ],
    op=task(
        "Una jarra de limonada usa 2 vasos de jugo por cada 5 vasos de agua. Haz una tabla con cuatro filas, para 1, 2, 3 y 4 jarras, que muestre los vasos de jugo y de agua. Luego responde: ¿cuántos vasos de jugo se necesitan con 20 vasos de agua?",
        "Jarras 1: 2 y 5; jarras 2: 4 y 10; jarras 3: 6 y 15; jarras 4: 8 y 20. Con 20 vasos de agua se necesitan 8 vasos de jugo.",
        ["tabla coherente", "usa razones equivalentes", "responde la pregunta"],
        ["tabla de cuatro filas", "respuesta con unidad"],
        ["sumar en lugar de multiplicar", "romper la razón en alguna fila"],
        "Pide que verifique que cada fila se pueda simplificar a 2 : 5.",
    ),
    reinforce="Escribe tres razones equivalentes a 3 : 5 multiplicando por 2, por 3 y por 4.",
    extend="Compara dos mezclas de pintura: A con 3 de rojo por 5 de blanco y B con 4 de rojo por 7 de blanco. Lleva ambas a la misma cantidad de blanco y di cuál es más roja.",
)

# ------------------------------------------------------------------ OA 03 clase 4
lesson(
    OA3, 4,
    use="Aprenderé a repartir una cantidad según una razón y a resolver problemas con razones entre partes y total. Sirve para repartir justo y para preparar mezclas.",
    prior=["Sé escribir razones y razones equivalentes.", "Sé dividir y multiplicar números naturales."],
    explain=[
        "Si una razón te dice cómo repartir una cantidad, primero cuenta las partes iguales. En la razón 2 : 3 hay 2 + 3 = 5 partes. Si el total es 40, cada parte vale 40 ÷ 5 = 8. Entonces la primera cantidad es 2 × 8 = 16 y la segunda es 3 × 8 = 24.",
        "Siempre comprueba que las partes sumen el total: 16 + 24 = 40. También puedes tener la razón y una de las cantidades. Si la razón entre rojas y azules es 3 : 4 y hay 12 rojas, 12 ÷ 3 = 4 es el valor de una parte, así que las azules son 4 × 4 = 16.",
        "Algunas razones tienen tres términos, como 1 : 2 : 3, que comparan tres cantidades. Se resuelven igual: sumas los términos para saber cuántas partes hay. Si te dan un cambio nuevo, por ejemplo se agregan elementos, calcula primero las cantidades iniciales y después la nueva razón.",
    ],
    vocab=[("parte igual", "cada una de las porciones del mismo tamaño en que se divide un total"), ("repartir en razón", "dividir un total según los términos de una razón"), ("total", "suma de todas las cantidades"), ("razón de tres términos", "razón que compara tres cantidades, como 1 : 2 : 3"), ("comprobar", "revisar que el resultado cumple lo pedido")],
    worked=[
        W("Repartir según una razón", "Se reparten 35 chocolates entre dos hermanos en la razón 2 : 5. ¿Cuántos chocolates recibe cada uno?", ["Partes: 2 + 5 = 7. Cada parte: 35 ÷ 7 = 5.", "Primero: 2 × 5 = 10. Segundo: 5 × 5 = 25.", "Compruebo: 10 + 25 = 35."], "10 y 25 chocolates"),
        W("Conocer una cantidad y la razón", "La razón entre cartulinas rojas y azules es 3 : 4 y hay 12 rojas. ¿Cuántas azules hay?", ["12 rojas son 3 partes, entonces una parte vale 12 ÷ 3 = 4.", "Las azules son 4 partes: 4 × 4 = 16."], "16 cartulinas azules"),
    ],
    mistakes=[
        M("Repartir 40 en razón 2 : 3 dando 2 y 3 a cada uno.", "Se tomaron los términos como si fueran las cantidades.", "Primero 2 + 3 = 5 partes, 40 ÷ 5 = 8, y se reparte 16 y 24."),
        M("Dividir el total por el primer término de la razón.", "Se olvidó sumar los términos para saber el número de partes.", "El número de partes es la suma de los términos."),
    ],
    rec=[
        ex("Se reparten 6 manzanas en la razón 1 : 2. ¿Cuántas manzanas recibe quien tiene la parte mayor?", "4", "Son 3 partes de 2 manzanas cada una; la mayor es 2 × 2 = 4."),
        ex("¿Cuántas partes iguales hay en la razón 3 : 2?", "5", "Se suman los términos: 3 + 2 = 5."),
        ex("Por cada 4 gatos hay 3 perros. Si hay 8 gatos, ¿cuántos perros hay?", "6", "De 4 a 8 se multiplicó por 2; 3 × 2 = 6."),
    ],
    und=[
        ex("Se reparten 20 en la razón 1 : 4. ¿Cuánto recibe la parte menor?", "4", "Son 5 partes de 4 cada una; la menor es 1 × 4."),
        ex("Se reparten 18 en la razón 4 : 5. ¿Cuánto recibe la parte mayor?", "10", "Son 9 partes de 2 cada una; la mayor es 5 × 2 = 10."),
        ex("La razón entre niñas y niños es 3 : 2 y hay 12 niñas. ¿Cuántos niños hay?", "8", "12 niñas son 3 partes de 4; los niños son 2 × 4 = 8."),
    ],
    app=[
        ex("Se mezclan 36 litros de pintura con blanco y azul en la razón 5 : 4. ¿Cuántos litros de azul hay?", "16", "Son 9 partes de 4 litros cada una; el azul es 4 × 4 = 16."),
        ex("Dos hermanos reparten $60.000 en la razón 3 : 2. ¿Cuánto recibe el que obtiene menos?", "$24.000", "Son 5 partes de $12.000 cada una; el menor recibe 2 × 12.000."),
        ex("Una mezcla de 450 gramos lleva almendras y nueces en la razón 2 : 7. ¿Cuántos gramos de almendras tiene?", "100", "Son 9 partes de 50 g cada una; las almendras son 2 × 50 = 100 g."),
    ],
    rea=[
        ex("Luis dice que en una mezcla de 20 litros en la razón 2 : 3 hay 2 litros de uno y 3 litros del otro. ¿Cuántos litros hay de cada uno?", "8 y 12", "Son 5 partes de 4 litros cada una: 2 × 4 = 8 y 3 × 4 = 12."),
        ex("Con la razón 3 : 5, la cantidad menor es 18. ¿Cuál es el total?", "48", "18 son 3 partes, cada parte vale 6; el total son 8 partes: 8 × 6 = 48."),
    ],
    cha=[
        ex("Tres amigos reparten $72.000 en la razón 1 : 2 : 3. ¿Cuánto recibe el que obtiene más?", "$36.000", "Son 6 partes de $12.000 cada una; el mayor recibe 3 × 12.000."),
        ex("En un curso de 36 estudiantes la razón entre niñas y niños es 5 : 4. Llegan 4 niños nuevos. ¿Cuál es la nueva razón entre niñas y niños?", "20 : 20 (que es 1 : 1)", "Eran 20 niñas y 16 niños; con 4 niños más hay 20 niños."),
    ],
    ctx=[ex("En un curso ficticio de 40 estudiantes la razón entre hombres y mujeres es 3 : 5. ¿Cuántas mujeres hay?", "25", "Son 8 partes de 5 estudiantes cada una; las mujeres son 5 × 5 = 25.")],
    sc=[
        ex("Se reparten 24 en la razón 1 : 3. ¿Cuánto recibe la parte mayor?", "18", "Son 4 partes de 6 cada una; la mayor es 3 × 6 = 18."),
        ex("La razón entre dos cantidades es 2 : 3 y la primera es 10. ¿Cuánto es la segunda?", "15", "10 son 2 partes de 5; la segunda es 3 × 5 = 15."),
        ex("Se reparten 21 en la razón 2 : 1. ¿Cuánto recibe la parte menor?", "7", "Son 3 partes de 7 cada una; la menor es 1 × 7."),
    ],
    op=task(
        "Tres amigas juntan $48.000 para un regalo y aportan en la razón 1 : 2 : 3. Calcula cuánto aporta cada una, comprueba que sumen $48.000 y explica con una frase por qué hiciste 1 + 2 + 3.",
        "Partes: 1 + 2 + 3 = 6. Cada parte: 48.000 ÷ 6 = 8.000. Aportan $8.000, $16.000 y $24.000. Suman 48.000. Hice 1 + 2 + 3 para saber en cuántas partes iguales se divide el total.",
        ["suma los términos de la razón", "calcula el valor de una parte", "comprueba que la suma da el total"],
        ["cálculo de partes", "tres aportes y comprobación"],
        ["usar los términos como cantidades", "no comprobar la suma"],
        "Pide que sume los tres aportes y compare con el total antes de dar la respuesta.",
    ),
    reinforce="Reparte 30 fichas entre dos personas en la razón 2 : 3. Calcula cuántas recibe cada una y comprueba la suma.",
    extend="En un curso de 30 estudiantes, la razón entre quienes van en bus y quienes caminan es 3 : 2. Calcula cuántos van en bus y cuántos caminan. Inventa una pregunta nueva con los mismos datos.",
)

# ================================================================== OA 04
OA4 = "MA06 OA 04"

# ------------------------------------------------------------------ OA 04 clase 1
lesson(
    OA4, 1,
    use="Aprenderé qué es un porcentaje y cómo se representa en una cuadrícula de 100. Sirve para entender datos como descuentos, encuestas y resultados.",
    prior=["Sé qué es una razón.", "Sé contar hasta 100 y sé qué es una fracción."],
    explain=[
        "Un porcentaje es una razón cuyo segundo término es 100. Se escribe con el símbolo % y se lee «por ciento». Decir 35 % es decir «35 de cada 100». Se puede escribir 35 : 100 o como fracción 35/100.",
        "Una cuadrícula de 100 cuadritos sirve para ver los porcentajes. Si se pintan 35 cuadritos, está pintado el 35 % de la figura. Si se pinta toda la cuadrícula, está pintado el 100 %. Si no se pinta ninguno, es 0 %. La mitad de la figura es 50 %, porque 50 de 100 es la mitad.",
        "Si un todo está dividido en 10 partes iguales, cada parte es el 10 %. Si pintas 3 de esas 10 partes, el 30 % está pintado. Las partes que no están pintadas completan el total: pintado más no pintado siempre da 100 %.",
    ],
    vocab=[("porcentaje", "razón entre una cantidad y 100"), ("por ciento", "se lee del símbolo %; significa «de cada 100»"), ("cuadrícula", "figura dividida en cuadritos iguales, aquí de 10 × 10"), ("100 %", "el total, todo"), ("complemento", "lo que falta para completar el total")],
    worked=[
        W("Porcentaje de una cuadrícula", "En una cuadrícula de 100 cuadritos se pintan 27. ¿Qué porcentaje está pintado?", ["Pintados: 27 de 100.", "Razón: 27 : 100, que se escribe 27 %."], "27 %"),
        W("Porcentaje en una tira", "Una tira se divide en 10 partes iguales y se pintan 3. ¿Qué porcentaje está pintado?", ["Cada parte es el 10 % de la tira.", "Tres partes son 3 × 10 % = 30 %."], "30 %"),
    ],
    mistakes=[
        M("Decir que 30 % es 30 de 30.", "Se olvidó que el total siempre es 100.", "30 % significa 30 de cada 100."),
        M("Decir que si se pintan 60 cuadritos de 100 queda 60 % sin pintar.", "Se confundió lo pintado con lo no pintado.", "Lo pintado es 60 % y lo no pintado es 100 % − 60 % = 40 %."),
    ],
    rec=[
        ex("Escribe 45 % como una razón con 100.", "45 : 100", "El porcentaje es la razón entre una cantidad y 100."),
        ex("En una cuadrícula de 100 cuadritos hay 80 pintados. ¿Qué porcentaje está pintado?", "80 %", "80 de 100 es 80 %."),
        ex("Si todo el dibujo está pintado, ¿qué porcentaje es?", "100 %", "Todo el total es 100 %."),
    ],
    und=[
        ex("En una cuadrícula de 100 cuadritos hay 12 sin pintar. ¿Qué porcentaje está pintado?", "88 %", "Pintados: 100 − 12 = 88 de 100."),
        ex("De 100 estudiantes de un colegio, 38 van en bus. ¿Qué porcentaje va en bus?", "38 %", "38 de 100 es 38 %."),
        ex("Una tira de 10 partes iguales tiene 7 partes pintadas. ¿Qué porcentaje está pintado?", "70 %", "Cada parte es 10 %, y 7 × 10 % = 70 %."),
    ],
    app=[
        ex("En una cuadrícula de 100 cuadritos se pintan 25 de rojo y 35 de azul, y el resto queda blanco. ¿Qué porcentaje es blanco?", "40 %", "Blanco: 100 − 25 − 35 = 40 cuadritos de 100."),
        ex("La batería de un teléfono tiene 100 segmentos y se han usado 64. ¿Qué porcentaje de batería queda?", "36 %", "Quedan 100 − 64 = 36 segmentos de 100."),
        ex("Un tablero tiene 100 casillas y 9 tienen una ficha. ¿Qué porcentaje de las casillas no tiene ficha?", "91 %", "Sin ficha: 100 − 9 = 91 casillas de 100."),
    ],
    rea=[
        ex("Pía dice que 30 % significa 30 de 30. ¿De cuánto es realmente el total en un porcentaje?", "100", "Un porcentaje siempre compara con 100."),
        ex("Ben pinta 50 cuadritos en una cuadrícula de 100 y Ana pinta 5 partes de una tira de 10. ¿Pintaron el mismo porcentaje? Responde sí o no.", "Sí", "Ben pintó 50 % y Ana pintó 5 × 10 % = 50 %."),
    ],
    cha=[
        ex("En una cuadrícula de 100 cuadritos, el 30 % es rojo, el doble de eso es azul y el resto es blanco. ¿Qué porcentaje es blanco?", "10 %", "Azul: 2 × 30 % = 60 %. Blanco: 100 % − 30 % − 60 % = 10 %."),
        ex("En una figura, lo no pintado es el triple de lo pintado. ¿Qué porcentaje está pintado?", "25 %", "Hay 4 partes iguales (1 pintada y 3 no) que suman 100 %, y 100 ÷ 4 = 25."),
    ],
    ctx=[ex("En una encuesta ficticia a 100 personas, 56 prefieren la montaña y el resto prefiere la playa. ¿Qué porcentaje prefiere la playa?", "44 %", "100 − 56 = 44 personas de 100.")],
    sc=[
        ex("De 100 cuadritos se pintan 73. ¿Qué porcentaje está pintado?", "73 %", "73 de 100 es 73 %."),
        ex("Si el 17 % de los estudiantes llega tarde, ¿qué porcentaje llega a tiempo?", "83 %", "100 % − 17 % = 83 %."),
        ex("Escribe 9 % como una razón con 100.", "9 : 100", "Un porcentaje es la razón entre un número y 100."),
    ],
    op=task(
        "Dibuja una cuadrícula de 10 × 10 en tu cuaderno. Pinta exactamente 35 cuadritos. Escribe el porcentaje pintado y el no pintado y explica por qué suman 100 %.",
        "En una cuadrícula con 35 pintados: pintado 35 %, no pintado 65 %. Suman 100 % porque los 100 cuadritos son el total.",
        ["dibujo coherente", "porcentajes correctos", "explica que suman 100 %"],
        ["dibujo de la cuadrícula", "dos porcentajes y frase"],
        ["olvidar el complemento", "contar mal los cuadritos"],
        "Pide que cuente los cuadritos pintados y no pintados y que su suma sea 100.",
    ),
    reinforce="En una cuadrícula de 100 cuadritos pinta 20 de rojo, 30 de azul y deja el resto sin pintar. Escribe el porcentaje de cada color y del resto.",
    extend="Explica con tus palabras por qué 25 % es la cuarta parte de un total, usando una cuadrícula de 100 cuadritos.",
)

# ------------------------------------------------------------------ OA 04 clase 2
lesson(
    OA4, 2,
    use="Aprenderé a pasar un porcentaje a fracción y a decimal, y al revés. Sirve para comparar datos escritos de formas distintas.",
    prior=["Sé qué es un porcentaje como razón de 100.", "Sé leer decimales hasta las centésimas y fracciones equivalentes."],
    explain=[
        "Un porcentaje, una fracción y un decimal pueden representar la misma cantidad. 25 % es 25 de cada 100: la fracción 25/100 y el decimal 0,25. Como 25/100 se puede simplificar dividiendo por 25, también es 1/4. Las tres formas son equivalentes.",
        "Para pasar un porcentaje a decimal, escribe la fracción con denominador 100 y léela como centésimas: 7 % es 7/100, que es 0,07. Para pasar una fracción a porcentaje, busca una fracción equivalente con denominador 100. Esto es fácil cuando el denominador es un divisor de 100, como 2, 4, 5, 10, 20, 25 o 50: 3/5 = 60/100 = 60 %.",
        "Algunas equivalencias son muy útiles y conviene recordarlas: 50 % = 1/2, 25 % = 1/4, 75 % = 3/4, 10 % = 1/10 y 20 % = 1/5. Para comparar cantidades escritas de formas distintas, llévalas todas al mismo formato, por ejemplo porcentaje.",
    ],
    vocab=[("fracción equivalente", "fracción que representa la misma cantidad con otros números"), ("centésima", "una parte de las 100 en que se divide una unidad"), ("decimal", "número escrito con coma, como 0,25"), ("amplificar", "multiplicar numerador y denominador por el mismo número"), ("simplificar", "dividir numerador y denominador por un mismo número")],
    worked=[
        W("De fracción a porcentaje", "Escribe 3/5 como porcentaje.", ["El denominador 5 se multiplica por 20 para llegar a 100.", "El numerador también: 3 × 20 = 60, entonces 3/5 = 60/100.", "60/100 es 60 %."], "60 %"),
        W("De decimal a porcentaje", "Escribe 0,35 como porcentaje.", ["0,35 son 35 centésimas, es decir 35/100.", "35/100 es 35 %."], "35 %"),
    ],
    mistakes=[
        M("Escribir 1/5 = 5 %.", "Se usó el denominador como porcentaje.", "1/5 = 20/100 = 20 %."),
        M("Escribir 7 % como 0,7.", "Se confundió centésimas con décimas.", "7 % = 7/100 = 0,07."),
    ],
    rec=[
        ex("¿Qué fracción con denominador 100 es 40 %?", "40/100", "Un porcentaje se lee como centésimas."),
        ex("Escribe 0,75 como porcentaje.", "75 %", "0,75 son 75 centésimas, es decir 75 %."),
        ex("¿Qué porcentaje es 1/2?", "50 %", "1/2 = 50/100."),
    ],
    und=[
        ex("Escribe 1/4 como porcentaje.", "25 %", "1/4 = 25/100."),
        ex("Escribe 7/10 como porcentaje.", "70 %", "7/10 = 70/100."),
        ex("Escribe 0,08 como porcentaje.", "8 %", "0,08 son 8 centésimas."),
    ],
    app=[
        ex("Escribe 3/4 como porcentaje.", "75 %", "3/4 = 75/100 al multiplicar por 25."),
        ex("Escribe 2/5 como porcentaje.", "40 %", "2/5 = 40/100 al multiplicar por 20."),
        ex("Escribe 17/20 como porcentaje.", "85 %", "17/20 = 85/100 al multiplicar por 5."),
    ],
    rea=[
        ex("Luis dice que 1/5 es lo mismo que 5 %. ¿Qué porcentaje es en realidad 1/5?", "20 %", "1/5 = 20/100; el 5 es el denominador, no el porcentaje."),
        ex("¿Qué es mayor, 0,6 o 55 %?", "0,6", "0,6 = 60 %, que es mayor que 55 %."),
    ],
    cha=[
        ex("Ordena de menor a mayor: 1/2, 30 % y 0,45.", "30 % < 0,45 < 1/2", "En porcentajes: 30 %, 45 % y 50 %."),
        ex("Escribe 9/25 como porcentaje.", "36 %", "25 × 4 = 100, así que 9 × 4 = 36."),
    ],
    ctx=[ex("En un curso ficticio de 20 estudiantes, 13 usan mochila azul. ¿Qué porcentaje usa mochila azul?", "65 %", "13/20 = 65/100 al multiplicar por 5.")],
    sc=[
        ex("Escribe 1/10 como porcentaje.", "10 %", "1/10 = 10/100."),
        ex("Escribe 0,4 como porcentaje.", "40 %", "0,4 = 0,40 = 40 centésimas."),
        ex("Escribe 90 % como fracción con denominador 10.", "9/10", "90/100 se simplifica dividiendo por 10."),
    ],
    op=task(
        "Completa en una tabla las tres formas (fracción, decimal y porcentaje) para estos datos: 1/2, 0,2 y 75 %. Después escribe qué valor es el menor y explica cómo lo decidiste.",
        "1/2 = 0,5 = 50 %. 0,2 = 2/10 = 20 %. 75 % = 75/100 = 3/4 = 0,75. El menor es 0,2 = 20 %, porque tiene el menor porcentaje.",
        ["las tres formas son equivalentes", "llega a un mismo formato para comparar", "explica la decisión"],
        ["tabla con tres columnas", "frase de comparación"],
        ["confundir décimas y centésimas", "no llevar a un mismo formato"],
        "Pide que pase todos los valores a porcentaje antes de comparar.",
    ),
    reinforce="Escribe 1/2, 1/4, 3/4, 1/5 y 1/10 como porcentaje y como decimal.",
    extend="Elige una fracción de denominador 20 o 25, escríbela como porcentaje y como decimal, y explica el paso a paso.",
)

# ------------------------------------------------------------------ OA 04 clase 3
lesson(
    OA4, 3,
    use="Aprenderé a calcular el porcentaje de una cantidad con estrategias mentales y con una calculadora. Sirve para calcular descuentos, aumentos y propinas.",
    prior=["Sé que un porcentaje es una razón con 100.", "Sé escribirlo como fracción o decimal."],
    explain=[
        "Para encontrar un porcentaje de una cantidad hay estrategias fáciles. El 50 % es la mitad. El 25 % es la cuarta parte. El 10 % se calcula dividiendo la cantidad por 10. El 1 % se calcula dividiendo por 100. Con estos puedes armar otros: el 20 % es el doble del 10 %, y el 15 % es el 10 % más el 5 %, que es la mitad del 10 %.",
        "Otra estrategia es usar la fracción: 75 % es 3/4, así que 75 % de 24 es 3/4 de 24, es decir 24 ÷ 4 × 3 = 18. La palabra «de» en «30 % de 150» indica multiplicar: 30/100 × 150. En la calculadora puedes hacer 150 ÷ 100 × 30.",
        "En problemas, un descuento se resta del precio y un aumento se suma. Si una chaqueta de $40.000 tiene 20 % de descuento, el 20 % es $8.000 y se paga $40.000 − $8.000 = $32.000. Comprueba siempre que el resultado tenga sentido: un descuento nunca puede ser mayor que el precio.",
    ],
    vocab=[("descuento", "cantidad que se resta al precio"), ("aumento", "cantidad que se suma a un valor"), ("mitad", "la mitad de una cantidad es 50 %"), ("cuarta parte", "25 % de una cantidad"), ("de", "en un porcentaje «de» una cantidad, indica multiplicar")],
    worked=[
        W("Porcentajes sencillos", "Calcula el 25 % de 80.", ["25 % es la cuarta parte.", "80 ÷ 4 = 20."], "20"),
        W("Combinar porcentajes", "Calcula el 15 % de 60.", ["10 % de 60 es 60 ÷ 10 = 6.", "5 % es la mitad del 10 %: 6 ÷ 2 = 3.", "15 % = 6 + 3 = 9."], "9"),
    ],
    mistakes=[
        M("Decir que el 50 % de 10 es 50.", "Se usó el porcentaje como cantidad.", "50 % es la mitad: 10 ÷ 2 = 5."),
        M("Calcular un descuento de 20 % de $40.000 y pagar $8.000.", "Se confundió el descuento con el precio final.", "El descuento es $8.000; se paga $40.000 − $8.000 = $32.000."),
    ],
    rec=[
        ex("Una bolsa tiene 18 galletas y se come la mitad (50 %). ¿Cuántas galletas se comen?", "9", "50 % es la mitad."),
        ex("En un curso de 70 estudiantes, el 10 % tiene cumpleaños en verano. ¿Cuántos estudiantes son?", "7", "Se divide 70 entre 10."),
        ex("¿Cuánto es la cuarta parte (25 %) de $40?", "10", "Es la cuarta parte: 40 ÷ 4."),
    ],
    und=[
        ex("Un tren lleva 90 pasajeros y el 20 % baja en la primera estación. ¿Cuántos bajan?", "18", "10 % de 90 es 9 y el 20 % es el doble: 18."),
        ex("Con 24 lápices en una caja, ¿cuántos son el 75 % de la caja?", "18", "24 ÷ 4 = 6 y 6 × 3 = 18."),
        ex("Se dividen 500 en 100 partes iguales. ¿Cuánto vale 1 parte, es decir el 1 %?", "5", "Se divide 500 entre 100."),
    ],
    app=[
        ex("De 150 estudiantes, el 30 % usa bicicleta. ¿Cuántos estudiantes usan bicicleta?", "45", "10 % de 150 es 15 y el 30 % es el triple: 45."),
        ex("Un libro cuesta $12.000 y tiene 25 % de descuento. ¿Cuánto se paga?", "$9.000", "El descuento es 12.000 ÷ 4 = 3.000 y se paga 12.000 − 3.000."),
        ex("Una piscina de 200 m² tiene el 35 % de su superficie con sombra. ¿Cuántos m² tienen sombra?", "70", "1 % de 200 es 2 y 35 × 2 = 70."),
    ],
    rea=[
        ex("Mara dice que el 50 % de 10 es 50. ¿Cuál es el valor correcto?", "5", "50 % es la mitad de 10."),
        ex("¿El 20 % de 50 es igual al 50 % de 20? Responde sí o no.", "Sí", "Ambos dan 10."),
    ],
    cha=[
        ex("Un celular cuesta $240.000 y su precio sube 15 %. ¿Cuál es el precio nuevo?", "$276.000", "10 % son 24.000, 5 % son 12.000; el aumento es 36.000 y 240.000 + 36.000."),
        ex("El 15 % de un número es 9. ¿Cuánto es el 30 % de ese mismo número?", "18", "30 % es el doble de 15 %, así que es el doble de 9."),
    ],
    ctx=[ex("En una tienda ficticia un abrigo de $50.000 tiene 30 % de descuento. ¿Cuánto se paga?", "$35.000", "10 % de 50.000 es 5.000 y 30 % es 15.000; se resta del precio: 50.000 − 15.000.")],
    sc=[
        ex("Para la propina se deja el 10 % de una cuenta de $250. ¿Cuántos pesos son?", "25", "Se divide entre 10."),
        ex("Calcula el 50 % de 64.", "32", "50 % es la mitad de 64."),
        ex("De 200 personas, el 5 % tiene lentes. ¿Cuántas personas son?", "10", "10 % es 20 y 5 % es su mitad."),
    ],
    op=task(
        "Una mochila ficticia cuesta $24.000 y tiene dos ofertas: A) 25 % de descuento; B) 10 % de descuento y después $2.000 menos. Calcula cuánto se paga en cada oferta y di cuál conviene más.",
        "A) 25 % de 24.000 es 6.000 y se paga 18.000. B) 10 % de 24.000 es 2.400, queda 21.600 y menos 2.000 son 19.600. Conviene A, que cuesta $18.000.",
        ["calcula bien cada descuento", "resta del precio", "compara y decide"],
        ["dos cálculos con pasos", "frase con la decisión"],
        ["pagar el descuento", "no restar al precio"],
        "Pide que compruebe que el precio final es menor que el precio inicial en las dos ofertas.",
    ),
    reinforce="Calcula el 10 %, el 20 % y el 30 % de 120. Observa qué pasa con el resultado cuando el porcentaje aumenta.",
    extend="Explica cómo calcular el 15 % de $8.000 de dos maneras distintas y comprueba que dan lo mismo.",
)

# ------------------------------------------------------------------ OA 04 clase 4
lesson(
    OA4, 4,
    use="Aprenderé a encontrar qué porcentaje es una parte del total y a resolver problemas de comparación con porcentajes. Sirve para entender encuestas y ofertas.",
    prior=["Sé calcular porcentajes sencillos de una cantidad.", "Sé pasar fracciones a porcentaje."],
    explain=[
        "Para saber qué porcentaje es una parte del total, escribe la fracción parte/total y llévala a denominador 100. Si 18 de 24 estudiantes respondieron bien, la fracción es 18/24, que se simplifica a 3/4 y equivale a 75 %. Cuando el total no divide a 100, usa una estrategia con decimales o con simplificación.",
        "Los porcentajes de las partes de un mismo todo suman 100 %. Si 35 % son niños, el resto, 65 %, son niñas. Si te dan el porcentaje de una parte y su cantidad, puedes hallar el total: si 20 % son 40 personas, 10 % son 20 y el 100 % son 200 personas.",
        "Para comparar ofertas con distinto precio y distinto descuento, calcula el precio final de cada una. No te guíes solo por el porcentaje. Un 10 % de descuento sobre un precio alto puede ahorrar más que un 20 % sobre un precio bajo. También cuidado: subir 10 % y bajar 10 % después no vuelve al valor inicial, porque cada porcentaje se calcula sobre un valor distinto.",
    ],
    vocab=[("parte", "cantidad que forma una fracción del total"), ("total", "el todo, que es 100 %"), ("encuesta", "pregunta hecha a varias personas para reunir datos"), ("precio final", "lo que se paga después de aplicar el descuento"), ("comparar", "decidir cuál valor es mayor o menor")],
    worked=[
        W("Qué porcentaje es una parte", "En una prueba, 18 de 24 respuestas fueron correctas. ¿Qué porcentaje fue correcto?", ["Fracción: 18/24, que se simplifica dividiendo por 6 y da 3/4.", "3/4 = 75/100, es decir 75 %."], "75 %"),
        W("Descuento sobre un precio", "Unas zapatillas cuestan $30.000 y tienen 10 % de descuento. ¿Cuánto se paga?", ["10 % de 30.000 es 3.000.", "Precio final: 30.000 − 3.000 = 27.000."], "$27.000"),
    ],
    mistakes=[
        M("Decir que 12 de 50 es 12 %.", "Se usó el número de partes como porcentaje, sin pasar a 100.", "12/50 = 24/100 = 24 %."),
        M("Creer que subir 10 % y luego bajar 10 % deja el precio igual.", "El segundo porcentaje se calcula sobre un valor mayor.", "100 sube a 110 y 10 % de 110 es 11, así que queda 99."),
    ],
    rec=[
        ex("¿Qué porcentaje es 10 de 20?", "50 %", "10/20 es la mitad, 50 %."),
        ex("¿Qué porcentaje es 5 de 50?", "10 %", "5/50 = 10/100."),
        ex("Si 40 % de un grupo lleva lentes, ¿qué porcentaje no lleva lentes?", "60 %", "100 % − 40 % = 60 %."),
    ],
    und=[
        ex("¿Qué porcentaje es 6 de 25?", "24 %", "6/25 = 24/100 al multiplicar por 4."),
        ex("¿Qué porcentaje es 9 de 12?", "75 %", "9/12 = 3/4 = 75 %."),
        ex("En un curso, 35 % son niños y el resto son niñas. ¿Qué porcentaje son niñas?", "65 %", "100 % − 35 % = 65 %."),
    ],
    app=[
        ex("Un equipo jugó 40 partidos y ganó 28. ¿Qué porcentaje ganó?", "70 %", "28/40 = 7/10 = 70 %."),
        ex("En un curso de 32 estudiantes faltaron 8. ¿Qué porcentaje asistió?", "75 %", "Asistieron 24 de 32, que es 3/4 = 75 %."),
        ex("Un pantalón cuesta $25.000 y tiene 20 % de descuento. ¿Cuánto se paga?", "$20.000", "20 % de 25.000 es 5.000 y se resta del precio."),
    ],
    rea=[
        ex("Tienda A: $50.000 con 10 % de descuento. Tienda B: $45.000 con 5 % de descuento. ¿Dónde se paga menos, en A o en B?", "B", "A: 50.000 − 5.000 = 45.000. B: 45.000 − 2.250 = 42.750."),
        ex("Un precio de $200 sube 10 % y luego baja 10 %. ¿Cuánto vale al final?", "$198", "Sube a 220; el 10 % de 220 es 22, así que baja a 198."),
    ],
    cha=[
        ex("En una encuesta, 20 % prefiere A, 35 % prefiere B y 25 % prefiere C. Las 40 personas restantes prefieren D. ¿Cuántas personas respondieron la encuesta?", "200", "Restan 100 % − 80 % = 20 %; si 20 % son 40 personas, el total es 200."),
        ex("En una reserva hay 800 aves. El 15 % son patos y el 35 % son gansos. ¿Cuántas aves son de otras especies?", "400", "Otras: 100 % − 50 % = 50 %, y el 50 % de 800 es 400."),
    ],
    ctx=[ex("En una encuesta ficticia a 250 estudiantes, 100 prefieren un recreo más largo. ¿Qué porcentaje prefiere el recreo más largo?", "40 %", "100/250 se simplifica dividiendo por 50 y da 2/5, que es 40/100.")],
    sc=[
        ex("¿Qué porcentaje es 3 de 12?", "25 %", "3/12 = 1/4 = 25 %."),
        ex("Calcula el 30 % de 90.", "27", "10 % de 90 es 9 y el 30 % es el triple."),
        ex("Si el 72 % de las personas apoya una idea, ¿qué porcentaje no la apoya?", "28 %", "100 % − 72 % = 28 %."),
    ],
    op=task(
        "En un curso ficticio de 40 estudiantes, 14 viajan en bus, 18 caminan y el resto llega en bicicleta. Calcula la cantidad que llega en bicicleta y el porcentaje de cada grupo. Comprueba que los tres porcentajes sumen 100 %.",
        "Bicicleta: 40 − 14 − 18 = 8. Bus: 14/40 = 35 %. Caminan: 18/40 = 45 %. Bicicleta: 8/40 = 20 %. Suman 35 % + 45 % + 20 % = 100 %.",
        ["calcula bien la parte que falta", "convierte cada fracción a porcentaje", "comprueba la suma"],
        ["tabla con cantidades y porcentajes", "suma de comprobación"],
        ["usar la cantidad como porcentaje", "no comprobar la suma"],
        "Pide que sume los tres porcentajes y que explique qué haría si la suma no diera 100 %.",
    ),
    reinforce="De un total de 20 estudiantes, 5 usan lentes. Calcula el porcentaje que usa lentes y el que no.",
    extend="Compara dos ofertas de un mismo producto de $60.000: A) 25 % de descuento; B) $12.000 de descuento. Calcula y explica cuál conviene más.",
)
