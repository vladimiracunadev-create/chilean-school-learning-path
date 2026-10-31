"""Cuaderno del estudiante de 7.º básico Matemática: OA 08 (proporcionalidad directa e inversa)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, lesson, task

OA8 = "MA07 OA 08"

# ------------------------------------------------------------------ OA 08 clase 1
lesson(
    OA8, 1,
    use="Aprenderé a distinguir cuándo dos cantidades están en proporción directa, en proporción inversa o en ninguna de las dos. Sirve para decidir cómo calcular precios, tiempos y repartos.",
    prior=["Sé multiplicar y dividir números naturales.", "Sé leer datos en una tabla."],
    explain=[
        "Dos cantidades que cambian juntas pueden estar relacionadas de distintas formas. En una proporción directa, si una cantidad se multiplica por un número, la otra se multiplica por el mismo número. Si 1 kg cuesta $1.500, entonces 2 kg cuestan $3.000 y 3 kg cuestan $4.500. El cociente precio ÷ kilos es siempre 1.500: esa es la constante de proporcionalidad.",
        "En una proporción inversa, si una cantidad se multiplica por un número, la otra se divide por ese número. Si 2 obreros hacen un trabajo en 12 días, 4 obreros lo hacen en 6 días y 6 obreros en 4 días. Aquí lo constante es el producto: 2 · 12 = 4 · 6 = 6 · 4 = 24. Cuando una cantidad sube, la otra baja.",
        "No toda relación es proporcional. Que dos cantidades crezcan juntas no basta para que sea directa: en la tabla x = 1, 2, 3 e y = 5, 7, 9 las dos suben, pero 5 ÷ 1, 7 ÷ 2 y 9 ÷ 3 no son iguales. Tampoco toda relación en que una sube y la otra baja es inversa; hay que revisar si el producto es constante. Calcula siempre el cociente y el producto de cada pareja.",
    ],
    vocab=[("proporción directa", "relación en que el cociente entre las dos cantidades es constante"), ("proporción inversa", "relación en que el producto entre las dos cantidades es constante"), ("constante de proporcionalidad", "valor fijo del cociente (en la directa) o del producto (en la inversa)"), ("razón", "comparación de dos cantidades mediante una división"), ("magnitud", "cantidad que se puede medir, como el tiempo o el peso")],
    worked=[
        W("Reconocer una directa", "Tabla de ejemplo: x = 1, 2, 3, 4 e y = 3, 6, 9, 12. ¿Qué relación es?", ["Calculo y ÷ x: 3, 3, 3, 3.", "El cociente es constante."], "Directa, con constante 3"),
        W("Reconocer una inversa", "Tabla de ejemplo: obreros = 2, 3, 4, 6 y días = 12, 8, 6, 4. ¿Qué relación es?", ["Calculo el producto de cada pareja: 24, 24, 24, 24.", "El producto es constante."], "Inversa, con constante 24"),
    ],
    mistakes=[
        M("Decir que (1, 2), (2, 3), (3, 4) es proporcional porque ambas cantidades crecen.", "Se miró solo que las dos suben.", "Los cocientes son 2, 1,5 y 1,33…: no son iguales, no es directa."),
        M("Decir que si x se triplica en una inversa, y también se triplica.", "Se confundió con la directa.", "En una inversa, si x se triplica, y se divide por 3."),
    ],
    rec=[
        ex("Si 1 kg de manzanas de ejemplo cuesta $1.500, 2 kg cuestan $3.000 y 3 kg cuestan $4.500, ¿la relación entre kilos y precio es directa o inversa?", "Directa", "Al multiplicar los kilos por 2 o por 3, el precio se multiplica igual."),
        ex("Al duplicar la cantidad de obreros que hacen un mismo trabajo, el tiempo baja a la mitad. ¿La relación es directa o inversa?", "Inversa", "Una cantidad se multiplica por 2 y la otra se divide por 2."),
        ex("En la tabla x = 1, 2, 3 e y = 5, 10, 15, ¿cuánto vale y ÷ x en cada pareja?", "5", "5 ÷ 1, 10 ÷ 2 y 15 ÷ 3 dan 5."),
    ],
    und=[
        ex("Tabla de ejemplo: x = 1, 2, 3, 4 e y = 4, 8, 12, 16. ¿Es directa, inversa o ninguna?", "Directa", "y ÷ x vale siempre 4."),
        ex("Tabla de ejemplo: x = 1, 2, 3, 4 e y = 12, 6, 4, 3. ¿Es directa, inversa o ninguna?", "Inversa", "Los productos 12, 12, 12 y 12 son iguales."),
        ex("Tabla de ejemplo: x = 1, 2, 3 e y = 5, 7, 9. ¿Es directa, inversa o ninguna?", "Ninguna", "Los cocientes son 5, 3,5 y 3, y los productos 5, 14 y 27."),
    ],
    app=[
        ex("Una máquina de ejemplo llena 4 botellas por minuto. ¿La relación entre minutos y botellas llenadas es directa, inversa o ninguna?", "Directa", "Botellas ÷ minutos es siempre 4."),
        ex("Para recorrer 120 km, a 40 km/h se demora 3 h; a 60 km/h, 2 h; a 80 km/h, 1,5 h. ¿La relación entre velocidad y tiempo es directa, inversa o ninguna?", "Inversa", "40 · 3 = 60 · 2 = 80 · 1,5 = 120."),
        ex("Una niña de ejemplo mide 115 cm a los 6 años, 128 cm a los 8 años y 138 cm a los 10 años. ¿La relación entre edad y altura es directa?", "No", "Los cocientes 115 ÷ 6, 128 ÷ 8 y 138 ÷ 10 no son iguales."),
    ],
    rea=[
        ex("Pablo dice que (1, 2), (2, 3), (3, 4) es directa porque ambas crecen. ¿Tiene razón?", "No", "Los cocientes son 2, 1,5 y 1,33…, que no son iguales."),
        ex("Marta dice que «en una inversa, si x se triplica, y también se triplica». ¿Es correcto?", "No", "En una inversa y se divide entre 3."),
    ],
    cha=[
        ex("Tabla directa de ejemplo: x = 2, 4, 6 e y = 10, ?, 30. ¿Qué número falta?", "20", "La constante es 10 ÷ 2 = 5 y 5 · 4 = 20."),
        ex("Tabla inversa de ejemplo: x = 2, 4, 8 e y = 24, ?, 6. ¿Qué número falta?", "12", "El producto es 2 · 24 = 48 y 48 ÷ 4 = 12."),
    ],
    ctx=[ex("En un taller de ejemplo, 3 llaves iguales llenan un estanque en 8 horas, 6 llaves lo llenan en 4 horas y 12 llaves lo llenan en 2 horas. ¿La relación entre llaves y horas es directa o inversa?", "Inversa", "3 · 8 = 6 · 4 = 12 · 2 = 24.")],
    sc=[
        ex("Si 5 cuadernos cuestan $4.000 y 10 cuadernos cuestan $8.000, ¿la relación es directa o inversa?", "Directa", "Al duplicar los cuadernos se duplica el precio."),
        ex("Si 4 personas comen un queque en 6 minutos y 8 personas lo comen en 3 minutos, ¿la relación es directa o inversa?", "Inversa", "Al duplicar las personas, el tiempo baja a la mitad."),
        ex("¿Qué se mantiene constante en una proporción inversa: el cociente o el producto?", "El producto", "x · y no cambia."),
    ],
    op=task(
        "Mira estas dos tablas de ejemplo. Tabla A (kg de naranjas y precio en pesos): 1 kg → 1.200, 2 kg → 2.400, 3 kg → 3.600, 5 kg → 6.000. Tabla B (cantidad de personas y minutos para pintar una pared): 2 → 60, 3 → 40, 4 → 30, 6 → 20. (a) Calcula el cociente de cada pareja de la tabla A y el producto de cada pareja de la tabla B. (b) Escribe cuál es directa y cuál es inversa y el valor de su constante. (c) Explica con una frase cómo lo supiste.",
        "Tabla A: 1.200 en todas, directa con constante 1.200. Tabla B: productos 120 en todas, inversa con constante 120. Lo supe porque en A el cociente es constante y en B el producto es constante.",
        ["calcula cociente y producto de cada pareja", "clasifica cada tabla", "explica con la constante"],
        ["cálculos por pareja", "clasificación y frase"],
        ["decidir solo por si crecen o decrecen", "calcular el producto en la tabla directa"],
        "Pide que pruebe la otra operación en cada tabla y vea que no da un valor constante.",
    ),
    reinforce="Con la tabla x = 1, 2, 3, 4 e y = 7, 14, 21, 28, calcula el cociente de cada pareja y decide qué tipo de relación es.",
    extend="Inventa una tabla de cuatro parejas que no sea ni directa ni inversa, pero donde ambas cantidades crezcan, y demuestra por qué.",
)

# ------------------------------------------------------------------ OA 08 clase 2
lesson(
    OA8, 2,
    use="Aprenderé a construir tablas de proporcionalidad directa usando la constante o el valor unitario. Sirve para calcular precios, ingredientes y distancias para cualquier cantidad.",
    prior=["Sé distinguir una relación directa de una inversa.", "Sé multiplicar y dividir con números naturales y decimales."],
    explain=[
        "En una relación directa, el cociente y ÷ x es siempre el mismo número k, que se llama constante de proporcionalidad. Entonces y = k · x. Si 3 kg cuestan $4.500, k = 4.500 ÷ 3 = 1.500: es el precio de 1 kg, el valor unitario. Con k puedes completar toda la tabla: para 5 kg el precio es 5 · 1.500 = 7.500.",
        "Para armar una tabla, escribe los valores de x en una fila y calcula cada y con y = kx. También puedes usar la regla de tres: si 3 kg cuestan 4.500, 5 kg cuestan 4.500 ÷ 3 · 5. Cualquier camino sirve mientras la relación sea directa. Los valores nuevos se pueden obtener sumando valores de la tabla: el precio de 5 kg es el de 2 kg más el de 3 kg.",
        "Revisa siempre la constante. Si una tabla supuestamente directa tiene un cociente distinto, la relación no es directa. Por ejemplo, si 5 pasajes cuestan $4.000 pero 10 pasajes cuestan $8.500, no es proporcional, porque el doble de pasajes debería costar $8.000. Escribe la unidad de k: pesos por kilo, kilómetros por litro, galletas por taza.",
    ],
    vocab=[("constante de proporcionalidad", "número k tal que y = k · x"), ("valor unitario", "valor correspondiente a una unidad; es el valor de k"), ("regla de tres", "método para hallar un valor usando una pareja conocida"), ("tabla de valores", "lista de parejas (x, y) de una relación"), ("fórmula", "regla escrita con letras, como y = 4x")],
    worked=[
        W("Hallar la constante y completar", "3 kg de arroz de ejemplo cuestan $4.500. Completa la tabla para 1, 2, 5 y 8 kg.", ["k = 4.500 ÷ 3 = 1.500 pesos por kg.", "1 kg: 1.500; 2 kg: 3.000; 5 kg: 7.500; 8 kg: 12.000."], "1.500; 3.000; 7.500; 12.000"),
        W("Regla de tres", "Una receta de ejemplo usa 2 tazas de harina para 8 panes. ¿Cuántas tazas para 20 panes?", ["k = 8 ÷ 2 = 4 panes por taza, así que tazas = panes ÷ 4.", "20 ÷ 4 = 5."], "5 tazas"),
    ],
    mistakes=[
        M("Calcular k dividiendo x ÷ y en lugar de y ÷ x y luego mezclar los valores.", "No se cuidó qué cantidad va arriba.", "Define antes qué es k (pesos por kilo) y divide siempre en ese orden."),
        M("Completar la tabla sumando una cantidad fija en vez de multiplicar.", "Se confundió con un patrón de suma.", "En una directa, al duplicar x se duplica y: se multiplica por la constante."),
    ],
    rec=[
        ex("En la pareja (2, 8) de una relación directa, ¿cuánto vale la constante k = y ÷ x?", "4", "8 ÷ 2 = 4."),
        ex("Si y = 6x y x = 5, ¿cuánto vale y?", "30", "6 · 5 = 30."),
        ex("Un lápiz de ejemplo cuesta $250. ¿Cuánto cuestan 4 lápices?", "$1.000", "4 · 250 = 1.000."),
    ],
    und=[
        ex("Completa la tabla directa: x = 1, 2, 3, 4 e y = 7, 14, ?, 28.", "21", "La constante es 7 y 7 · 3 = 21."),
        ex("En una relación directa, la pareja (3, 12) está en la tabla. ¿Cuál es el valor unitario (y cuando x = 1)?", "4", "12 ÷ 3 = 4."),
        ex("5 pasajes de ejemplo cuestan $4.000. ¿Cuánto cuestan 8 pasajes?", "$6.400", "Un pasaje cuesta 800 y 8 · 800 = 6.400."),
    ],
    app=[
        ex("Una receta de ejemplo usa 3 tazas de harina para 12 galletas. ¿Cuántas tazas se necesitan para 28 galletas?", "7", "Son 4 galletas por taza y 28 ÷ 4 = 7."),
        ex("Una impresora de ejemplo imprime 90 páginas en 6 minutos. ¿Cuántas páginas imprime en 10 minutos al mismo ritmo?", "150", "Son 15 páginas por minuto y 15 · 10 = 150."),
        ex("Un auto de ejemplo recorre 240 km con 20 L de bencina. ¿Cuántos km recorre con 35 L?", "420 km", "Son 12 km por litro y 12 · 35 = 420."),
    ],
    rea=[
        ex("Eva dice que si 5 pasajes cuestan $4.000 y 10 pasajes cuestan $8.500, la relación es directa. ¿Tiene razón?", "No", "El doble de pasajes debería costar el doble: 8.000, no 8.500."),
        ex("Tabla de ejemplo: x = 2, 5, 10 e y = 6, 15, 30. Escribe la regla y = k · x.", "y = 3x", "6 ÷ 2 = 15 ÷ 5 = 30 ÷ 10 = 3."),
    ],
    cha=[
        ex("En una relación directa, la pareja (4, 10) pertenece a la tabla. ¿Cuánto vale y cuando x = 14?", "35", "k = 10 ÷ 4 = 2,5 y 2,5 · 14 = 35."),
        ex("En un mapa de ejemplo, 2 cm representan 5 km. ¿Cuántos km representan 7 cm?", "17,5 km", "Cada centímetro son 2,5 km y 7 · 2,5 = 17,5."),
    ],
    ctx=[ex("Una panadería de ejemplo vende 6 panes por $2.400. ¿Cuánto cuestan 15 panes al mismo precio por pan?", "$6.000", "Un pan cuesta 400 y 15 · 400 = 6.000.")],
    sc=[
        ex("Si y = 7x, ¿cuánto vale y cuando x = 6?", "42", "7 · 6."),
        ex("Si 4 manzanas cuestan $1.600, ¿cuánto cuesta 1 manzana?", "$400", "1.600 ÷ 4."),
        ex("Completa la tabla directa: x = 1, 2, 5 e y = 9, 18, ?.", "45", "9 · 5."),
    ],
    op=task(
        "Una pastelería de ejemplo usa 600 g de harina para 4 tortas. (a) Calcula cuántos gramos de harina se usan para 1 torta (valor unitario). (b) Completa una tabla para 1, 2, 3, 6 y 10 tortas. (c) Escribe la regla y = k · x indicando qué es cada letra. (d) Responde cuántas tortas se pueden hacer con 2.400 g de harina.",
        "(a) 150 g por torta. (b) 150, 300, 450, 900 y 1.500 g. (c) g = 150 · t, donde t son las tortas. (d) 2.400 ÷ 150 = 16 tortas.",
        ["calcula el valor unitario", "completa bien la tabla", "escribe la regla con significado", "usa la relación al revés"],
        ["tabla completa", "regla escrita", "respuesta con unidad"],
        ["sumar en lugar de multiplicar", "no verificar con una pareja conocida"],
        "Pide que compruebe que 4 tortas dan 600 g con la regla.",
    ),
    reinforce="Si 3 cuadernos cuestan $2.700, completa una tabla para 1, 2, 5 y 7 cuadernos.",
    extend="Escribe la regla y = k · x para el precio de x cuadernos que cuestan $900 cada uno y úsala para decidir cuántos se pueden comprar con $8.000.",
)

# ------------------------------------------------------------------ OA 08 clase 3
lesson(
    OA8, 3,
    use="Aprenderé a construir tablas de proporcionalidad inversa usando el producto constante. Sirve para calcular tiempos, velocidades y repartos cuando más de una cosa significa menos de la otra.",
    prior=["Sé distinguir una proporción directa de una inversa.", "Sé multiplicar y dividir con números naturales."],
    explain=[
        "En una relación inversa, el producto x · y es siempre el mismo número k. Entonces y = k ÷ x. Si 4 obreros terminan un trabajo en 15 días, el trabajo total vale 4 · 15 = 60 obrero-días. Con 6 obreros, los días son 60 ÷ 6 = 10. Más obreros significa menos días, pero el trabajo total sigue siendo el mismo.",
        "Para construir una tabla, calcula k con una pareja conocida y luego divide k entre cada valor de x. Si k = 120 y x = 8, entonces y = 15. También sirve razonar con factores: si x se multiplica por 3, y se divide por 3. Otros ejemplos son velocidad y tiempo para una misma distancia, y número de niños y caramelos para un mismo reparto.",
        "Revisa cada tabla con el producto. Si x = 2, 4, 6 e y = 12, 6, 3, los productos son 24, 24 y 18: no es una relación inversa. Cuando completes una tabla, comprueba que todas las parejas tengan el mismo producto. Escribe la unidad de k: obrero-días, kilómetros, caramelos.",
    ],
    vocab=[("producto constante", "valor fijo de x · y en una relación inversa"), ("obrero-día", "trabajo que hace una persona en un día"), ("reparto", "división de una cantidad entre varias personas"), ("proporción inversa", "relación en que el producto de las dos cantidades es constante"), ("distancia", "cantidad de camino recorrido")],
    worked=[
        W("Obreros y días", "4 obreros de ejemplo terminan un trabajo en 15 días. ¿Cuántos días demoran 6 obreros al mismo ritmo?", ["k = 4 · 15 = 60 obrero-días.", "Días = 60 ÷ 6 = 10."], "10 días"),
        W("Completar una tabla inversa", "x = 1, 2, 3, 6 e y = 36, ?, 12, ?. Complétala.", ["k = 1 · 36 = 36. Para x = 2: 36 ÷ 2 = 18.", "Para x = 6: 36 ÷ 6 = 6. Compruebo 3 · 12 = 36."], "18 y 6"),
    ],
    mistakes=[
        M("Calcular los días con 6 obreros como 15 · 6 / 4 (relación directa).", "Se usó la regla de la directa.", "Con más obreros bajan los días: 60 ÷ 6 = 10."),
        M("Creer que (2, 12), (4, 6) y (6, 3) es inversa.", "Se revisó solo hasta la segunda pareja.", "Los productos son 24, 24 y 18: no es constante, no es inversa."),
    ],
    rec=[
        ex("En la pareja (3, 8) de una relación inversa, ¿cuánto vale el producto constante?", "24", "3 · 8 = 24."),
        ex("6 obreros demoran 4 días en un trabajo. ¿Cuántos obrero-días tiene el trabajo?", "24", "6 · 4 = 24."),
        ex("En una relación inversa, cuando x aumenta, ¿y aumenta o disminuye?", "Disminuye", "El producto se mantiene constante."),
    ],
    und=[
        ex("Completa la tabla inversa: x = 1, 2, 4, 8 e y = 16, 8, ?, 2.", "4", "El producto es 16 y 16 ÷ 4 = 4."),
        ex("La pareja (5, 12) pertenece a una relación inversa. ¿Cuál es el producto constante?", "60", "5 · 12 = 60."),
        ex("En una relación inversa con producto 36, ¿cuánto vale y cuando x = 9?", "4", "36 ÷ 9 = 4."),
    ],
    app=[
        ex("A 50 km/h un viaje de ejemplo demora 6 horas. ¿Cuántas horas demora a 75 km/h?", "4 horas", "La distancia es 50 · 6 = 300 km y 300 ÷ 75 = 4."),
        ex("Se reparten 120 caramelos en partes iguales. Con 8 niños tocan 15 a cada uno. ¿Cuántos caramelos recibe cada uno si se reparten entre 12 niños?", "10", "120 ÷ 12 = 10."),
        ex("Un piso de ejemplo se cubre con 36 baldosas pequeñas. Si cada baldosa nueva cubre el cuádruple de superficie que una pequeña, ¿cuántas baldosas nuevas se necesitan para cubrir el mismo piso?", "9", "Con baldosas 4 veces más grandes se necesitan 4 veces menos: 36 ÷ 4 = 9."),
    ],
    rea=[
        ex("Pedro dice que (3, 20), (5, 12) y (6, 8) es inversa porque y baja al subir x. Calcula los productos y responde si tiene razón.", "No; los productos son 60, 60 y 48", "El producto no es constante."),
        ex("En una relación inversa, si x se reduce a la mitad, ¿qué pasa con y?", "Se duplica", "El producto se mantiene constante."),
    ],
    cha=[
        ex("6 máquinas iguales hacen un pedido en 10 horas. Si dos se averían y quedan 4 funcionando, ¿cuántas horas demoran?", "15 horas", "Hay 6 · 10 = 60 máquina-horas y 60 ÷ 4 = 15."),
        ex("12 personas pintan una muralla en 20 días. ¿Cuántas personas harían falta para pintarla en 8 días?", "30", "El trabajo es 12 · 20 = 240 y 240 ÷ 8 = 30."),
    ],
    ctx=[ex("Un grupo de 9 estudiantes de ejemplo debe armar 72 sobres en total y cada uno arma la misma cantidad. ¿Cuántos sobres arma cada uno? ¿Y si fueran 12 estudiantes?", "8 y 6", "72 ÷ 9 = 8 y 72 ÷ 12 = 6.")],
    sc=[
        ex("Si x · y = 40 y x = 5, ¿cuánto vale y?", "8", "40 ÷ 5."),
        ex("3 grifos llenan un estanque en 8 horas. ¿Cuántas horas demoran 6 grifos iguales?", "4 horas", "24 grifo-horas ÷ 6."),
        ex("¿La tabla x = 2, 4, 8 e y = 20, 10, 5 es inversa? Responde sí o no.", "Sí", "Los productos 40, 40 y 40 son iguales."),
    ],
    op=task(
        "Una familia de ejemplo planea un viaje de 240 km. (a) Completa una tabla con velocidad (km/h) y tiempo (horas): 40, 60, 80, 120 y 30 km/h. (b) Calcula el producto de cada pareja y comprueba que es constante. (c) Responde cuánto demora a 48 km/h y explica con una frase por qué más velocidad significa menos tiempo.",
        "(a) 40 km/h: 6 h; 60: 4 h; 80: 3 h; 120: 2 h; 30: 8 h. (b) El producto es 240 en todas. (c) A 48 km/h: 240 ÷ 48 = 5 h. Con más velocidad se recorren más kilómetros por hora, así que se necesita menos tiempo para la misma distancia.",
        ["calcula k con la distancia", "completa la tabla con divisiones", "explica la relación inversa"],
        ["tabla completa", "productos comprobados", "frase de explicación"],
        ["multiplicar en vez de dividir", "olvidar comprobar con el producto"],
        "Pide que verifique que las parejas dan siempre 240.",
    ),
    reinforce="Si 5 obreros terminan un trabajo en 12 días, completa una tabla para 1, 2, 3, 4 y 6 obreros.",
    extend="Explica con un ejemplo por qué la relación entre número de personas y días para pintar una muralla no es inversa si algunas personas trabajan más rápido que otras.",
)

# ------------------------------------------------------------------ OA 08 clase 4
lesson(
    OA8, 4,
    use="Aprenderé a graficar tablas de proporcionalidad y a explicar las características de cada gráfica. Sirve para reconocer una relación directa o inversa con solo mirar un dibujo.",
    prior=["Sé armar tablas de proporcionalidad directa e inversa.", "Sé ubicar puntos en un plano con ejes."],
    explain=[
        "Para graficar, cada pareja (x, y) de la tabla se marca como un punto en un plano. El eje horizontal muestra x y el vertical muestra y. El punto (3, 12) está 3 lugares a la derecha del origen y 12 hacia arriba. Después se observa cómo quedan los puntos.",
        "En una proporción directa los puntos quedan alineados sobre una recta que pasa por el origen (0, 0). Si k es mayor, la recta sube más rápido. Por ejemplo, con y = 2x los puntos son (1, 2), (2, 4), (3, 6). Con y = 5x la recta sube más. La gráfica va creciendo: cuando x aumenta, y también.",
        "En una proporción inversa los puntos no quedan sobre una recta, sino sobre una curva que baja. Para x · y = 12, los puntos son (1, 12), (2, 6), (3, 4), (4, 3) y (6, 2). La curva nunca toca los ejes, porque x e y nunca valen 0 (su producto sería 0). Al aumentar x, y disminuye. Si k es mayor, la curva queda más lejos del origen.",
    ],
    vocab=[("plano cartesiano", "plano con dos ejes numéricos perpendiculares"), ("punto", "pareja (x, y) marcada en el plano"), ("origen", "punto (0, 0), donde se cruzan los ejes"), ("recta", "línea sin curvas; la gráfica de una proporción directa"), ("curva", "línea que se dobla; la gráfica de una proporción inversa")],
    worked=[
        W("Gráfica de una directa", "Tabla de ejemplo: (1, 2), (2, 4), (3, 6). ¿Cómo es su gráfica?", ["Los puntos suben 2 cada vez que x sube 1: están alineados.", "Si sigo la línea hacia atrás llego a (0, 0)."], "Una recta que pasa por el origen"),
        W("Gráfica de una inversa", "Tabla de ejemplo: (1, 12), (2, 6), (3, 4), (4, 3). ¿Cómo es su gráfica?", ["Los productos son 12, 12, 12 y 12: relación inversa.", "Los puntos bajan cada vez más lento y no están en una recta."], "Una curva que baja y no toca los ejes"),
    ],
    mistakes=[
        M("Pensar que la gráfica de una proporción inversa pasa por el origen.", "Se confundió con la gráfica de la directa.", "La directa pasa por (0, 0); la inversa nunca toca los ejes."),
        M("Unir los puntos de una inversa con una recta.", "Se supuso que siempre se unen con rectas.", "Los puntos de una inversa quedan sobre una curva."),
    ],
    rec=[
        ex("En el punto (3, 12), ¿cuál es el valor de y?", "12", "El segundo número es el vertical."),
        ex("La gráfica de una proporción directa pasa por un punto especial. ¿Cuál es?", "(0, 0)", "El origen del plano."),
        ex("En una proporción inversa, ¿la gráfica toca los ejes? Responde sí o no.", "No", "Si x o y valieran 0, el producto sería 0."),
    ],
    und=[
        ex("Los puntos (1, 3), (2, 6) y (3, 9) están en una gráfica. ¿La gráfica es una recta por el origen o una curva que baja?", "Una recta por el origen", "y ÷ x es siempre 3: es directa."),
        ex("Los puntos (1, 12), (2, 6), (3, 4) y (4, 3) están en una gráfica. ¿Qué tipo de relación es y cuánto vale el producto constante?", "Inversa; 12", "1 · 12 = 2 · 6 = 3 · 4 = 4 · 3 = 12."),
        ex("Una gráfica directa pasa por (4, 8). ¿Por cuál punto pasa cuando x = 5?", "(5, 10)", "k = 8 ÷ 4 = 2 y 2 · 5 = 10."),
    ],
    app=[
        ex("La recta A pasa por (1, 2) y la recta B pasa por (1, 5). Ambas son de proporcionalidad directa. ¿Cuál sube más rápido?", "La B", "k = 5 es mayor que k = 2."),
        ex("En una gráfica directa de precio de bencina de ejemplo, el punto (10, 15.000) indica 10 litros por $15.000. ¿Cuánto indica el punto cuando x = 4?", "(4, 6.000)", "k = 1.500 y 1.500 · 4 = 6.000."),
        ex("En una gráfica inversa de ejemplo (personas, días) pasa por (4, 15). ¿Qué valor de días indica cuando hay 6 personas?", "10", "El producto es 60 y 60 ÷ 6 = 10."),
    ],
    rea=[
        ex("Los puntos (1, 3), (2, 5) y (3, 7) están alineados, pero la recta no pasa por (0, 0). ¿Es una relación directa?", "No", "Los cocientes 3, 2,5 y 2,33… no son iguales."),
        ex("Una persona une los puntos (1, 12), (2, 6), (3, 4) con una recta. ¿Está bien? Responde sí o no.", "No", "En una inversa los puntos están sobre una curva."),
    ],
    cha=[
        ex("Dos gráficas de relaciones directas pasan por (4, 8) y por (4, 20). ¿Cuáles son sus constantes?", "2 y 5", "8 ÷ 4 = 2 y 20 ÷ 4 = 5."),
        ex("En una gráfica inversa, ¿cuál punto de esta lista pertenece a la curva de (2, 24): (3, 16), (4, 10) o (8, 4)?", "(3, 16)", "El producto es 48 y solo 3 · 16 da 48."),
    ],
    ctx=[ex("Una tabla de ejemplo de tiempo (minutos) y litros que sale de una llave es (1, 4), (2, 8), (3, 12). ¿La gráfica es una recta por el origen? Responde sí o no.", "Sí", "Los litros por minuto son siempre 4.")],
    sc=[
        ex("¿Cómo es la gráfica de una proporción inversa: recta o curva?", "Curva", "Los puntos bajan sin formar una línea recta."),
        ex("Si una recta directa pasa por (2, 6), ¿cuánto vale k?", "3", "6 ÷ 2."),
        ex("¿Qué hay que ubicar primero en el plano: el valor de x o el de y?", "El valor de x", "La pareja (x, y) se ubica primero en el eje horizontal."),
    ],
    op=task(
        "En papel cuadriculado dibuja un plano con ejes de 0 a 12. Marca los puntos de la tabla A: (1, 2), (2, 4), (3, 6), (4, 8) y los de la tabla B: (1, 12), (2, 6), (3, 4), (4, 3), (6, 2). (a) Une los puntos de A con una regla. (b) Une los de B con una curva suave. (c) Escribe cuál es directa y cuál inversa y una característica de cada gráfica.",
        "A es directa, con constante 2: los puntos forman una recta que pasa por el origen. B es inversa, con producto constante 12: los puntos forman una curva que baja y no toca los ejes.",
        ["ubica bien todos los puntos", "une A con recta y B con curva", "describe las gráficas con las características"],
        ["dibujo en papel cuadriculado", "frases con las características"],
        ["marcar los valores de x e y al revés", "unir B con una recta"],
        "Pide que compruebe que cada punto se ubica contando primero a la derecha y luego hacia arriba.",
    ),
    reinforce="Marca en un plano los puntos de la tabla x = 1, 2, 3, 4 e y = 5, 10, 15, 20 y descríbelos.",
    extend="Explica con la tabla por qué la gráfica de los puntos (1, 6), (2, 3), (3, 2) y (6, 1) no puede pasar por el punto (0, 0).",
)

# ------------------------------------------------------------------ OA 08 clase 5
lesson(
    OA8, 5,
    use="Aprenderé a elegir el modelo correcto (directo o inverso) para resolver un problema y a justificar mi elección. Sirve para resolver problemas de la vida diaria y de otras asignaturas.",
    prior=["Sé armar tablas y graficar relaciones directas e inversas.", "Sé usar la constante de proporcionalidad."],
    explain=[
        "Para resolver un problema de proporcionalidad, sigue estos pasos. Primero identifica las dos cantidades. Segundo, decide qué pasa al aumentar una: si la otra aumenta en la misma razón es directa; si disminuye en la misma razón es inversa. Tercero, calcula la constante (cociente o producto). Cuarto, úsala para hallar el valor pedido y comprueba con una pareja conocida.",
        "Justificar el modelo es explicar por qué elegiste directa o inversa. Ejemplo: «más kilos cuestan más, y el precio por kilo no cambia: es directa». Otro: «más obreros terminan en menos días, y el trabajo total no cambia: es inversa». También sirve una pregunta de prueba: ¿qué pasa si duplico la primera cantidad?, ¿la otra se duplica o se reduce a la mitad?",
        "No todo problema es proporcional. Si una tarifa tiene un cargo fijo más un valor por kilómetro, el cociente no es constante. Revisa siempre con dos parejas. Los problemas de otras asignaturas, como escala de un mapa, densidad, rapidez o recetas de laboratorio, usan estos mismos modelos. Escribe la respuesta con unidad.",
    ],
    vocab=[("modelo", "relación matemática que representa una situación"), ("justificar", "explicar con razones por qué una decisión es correcta"), ("tarifa fija", "cobro que no depende de la cantidad"), ("escala", "razón entre una medida del dibujo y la medida real"), ("rapidez", "distancia recorrida por unidad de tiempo")],
    worked=[
        W("Elegir y justificar un modelo directo", "Un ciclista de ejemplo recorre 36 km en 3 horas a ritmo constante. ¿Cuántos km recorre en 5 horas?", ["Si duplica el tiempo, duplica la distancia: es directa. k = 36 ÷ 3 = 12 km/h.", "Distancia = 12 · 5 = 60."], "60 km"),
        W("Elegir y justificar un modelo inverso", "8 obreros de ejemplo terminan un camino en 9 días. ¿En cuántos días lo terminan 12 obreros?", ["Más obreros, menos días y el trabajo no cambia: es inversa. k = 8 · 9 = 72.", "Días = 72 ÷ 12 = 6."], "6 días"),
    ],
    mistakes=[
        M("Usar una regla de tres directa para el problema de obreros y días.", "No se analizó el sentido de la relación.", "Más obreros significa menos días: se usa el producto constante."),
        M("Suponer que una tarifa con cargo fijo es proporcional.", "No se comprobó con dos parejas.", "Si 2 km cuestan $2.200 y 4 km cuestan $3.400 (con $1.000 fijos), el cociente cambia: no es directa."),
    ],
    rec=[
        ex("Si 2 kg de papas de ejemplo cuestan $1.600, ¿cuánto cuestan 3 kg?", "$2.400", "800 · 3 = 2.400."),
        ex("Si 3 pintores demoran 10 días, ¿cuántos pintores-día tiene el trabajo?", "30", "3 · 10."),
        ex("Si a más personas se demora menos tiempo en un mismo trabajo, ¿qué modelo conviene: directo o inverso?", "Inverso", "Cuando una sube, la otra baja y el trabajo total no cambia."),
    ],
    und=[
        ex("Un auto de ejemplo gasta 8 L cada 100 km. ¿Cuántos litros gasta en 250 km?", "20 L", "Es directa: 8 ÷ 100 · 250 = 20."),
        ex("Un grupo de 6 jardineros termina de podar un parque en 8 días. ¿En cuántos días terminan 4 jardineros al mismo ritmo?", "12 días", "Trabajo: 6 · 8 = 48; 48 ÷ 4 = 12."),
        ex("En un mapa de ejemplo, 1 cm representa 4 km. ¿Cuántos km son 6,5 cm?", "26 km", "4 · 6,5 = 26."),
    ],
    app=[
        ex("Una receta de ejemplo para 4 personas usa 600 g de arroz. ¿Cuántos gramos se necesitan para 10 personas?", "1.500 g", "150 g por persona y 150 · 10 = 1.500."),
        ex("Si 5 amigos comparten el costo de un regalo de ejemplo, cada uno paga $6.000. Si fueran 6 amigos, ¿cuánto pagaría cada uno?", "$5.000", "El costo total es 30.000 y 30.000 ÷ 6 = 5.000."),
        ex("En un laboratorio de ejemplo, 50 mL de solución pesan 60 g. ¿Cuántos g pesan 200 mL de la misma solución?", "240 g", "Es directa: 60 ÷ 50 = 1,2 g por mL y 1,2 · 200 = 240."),
    ],
    rea=[
        ex("Un taxi de ejemplo cobra $1.000 fijos más $300 por km. Si 2 km cuestan $1.600, ¿4 km cuestan el doble, $3.200? Responde sí o no.", "No", "4 km cuestan 1.000 + 1.200 = 2.200: hay un cobro fijo y no es directa."),
        ex("Juana dice que 3 obreros construyen un muro en 12 días, así que 6 obreros lo construyen en 24 días. ¿Tiene razón?", "No", "Es inversa: con el doble de obreros, la mitad de días, o sea 6."),
    ],
    cha=[
        ex("Una llave de ejemplo llena un balde de 12 L en 3 minutos. Con la misma llave, ¿cuántos litros hay después de 5 minutos? ¿Y si dos llaves iguales llenan el balde, cuántos minutos demoran?", "20 L; 1,5 minutos", "Directa: 4 L por minuto y 4 · 5 = 20. Inversa: 12 L con 2 llaves van el doble de rápido, 3 ÷ 2 = 1,5."),
        ex("Una piscina de ejemplo se llena con 4 mangueras iguales en 6 horas. Si se usan 3 mangueras iguales, ¿en cuántas horas se llena?", "8 horas", "Producto: 4 · 6 = 24 y 24 ÷ 3 = 8."),
    ],
    ctx=[ex("Se necesitan 18 L de pintura de ejemplo para pintar 90 m² de pared. ¿Cuántos litros se necesitan para 150 m² al mismo rendimiento?", "30 L", "Un litro rinde 5 m² y 150 ÷ 5 = 30.")],
    sc=[
        ex("Si 3 cuadernos cuestan $2.700, ¿cuánto cuestan 5 cuadernos?", "$4.500", "900 · 5."),
        ex("Si 4 pintores demoran 6 días, ¿cuánto demoran 8 pintores?", "3 días", "24 pintor-días ÷ 8."),
        ex("¿La relación entre el número de personas que comparten un pastel y el trozo que recibe cada una es directa o inversa?", "Inversa", "A más personas, trozos más pequeños."),
    ],
    op=task(
        "Resuelve estos dos problemas de ejemplo y justifica el modelo de cada uno. (1) Una máquina corta 45 metros de tela en 5 minutos. ¿Cuántos metros corta en 12 minutos? (2) Con 6 trabajadores, un galpón se limpia en 10 horas. ¿Cuánto demoran 15 trabajadores? Para cada uno escribe: tipo de relación, constante, cálculo, respuesta con unidad y una prueba de la regla (por ejemplo, qué pasa si duplicas una cantidad).",
        "(1) Directa, k = 9 m/min, 9 · 12 = 108 m. Si duplico los minutos, se duplican los metros. (2) Inversa, k = 60 trabajador-horas, 60 ÷ 15 = 4 horas. Si duplico los trabajadores, se reduce a la mitad el tiempo.",
        ["elige y justifica el modelo", "calcula correctamente la constante y el resultado", "comprueba con una prueba de duplicar"],
        ["procedimiento escrito", "respuestas con unidad", "justificación"],
        ["elegir el modelo directo en todos los problemas", "no incluir las unidades"],
        "Pide que verifique que la respuesta tiene sentido: más trabajadores deben demorar menos.",
    ),
    reinforce="Resuelve: 4 kg de carne de ejemplo cuestan $20.000. ¿Cuánto cuestan 7 kg? Escribe si es directa o inversa.",
    extend="Escribe un problema de tu propia invención que use proporcionalidad inversa y resuélvelo con una tabla y con una gráfica.",
)
