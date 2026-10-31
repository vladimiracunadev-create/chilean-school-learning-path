"""Cuaderno del estudiante de 7.º básico Matemática: OA 04 (porcentajes) y OA 05 (potencias de base diez y notación científica)."""
from __future__ import annotations

from student_lessons import ex
from student_content_ma07_a import M, W, cx, lesson, task

OA4 = "MA07 OA 04"
OA5 = "MA07 OA 05"

# ------------------------------------------------------------------ OA 04 clase 1
lesson(
    OA4, 1,
    use="Aprenderé qué es un porcentaje y cómo se representa con una cuadrícula de cien cuadritos. Sirve para entender datos como «el 30 % de las personas» o «un 20 % de descuento».",
    prior=["Sé que una fracción es una parte de un todo.", "Sé contar y sumar hasta 100."],
    explain=[
        "Un porcentaje es una comparación de una parte con 100. El signo % significa «por cada cien». Si pintas 35 cuadritos de una cuadrícula de 100, pintaste el 35 % y se lee «treinta y cinco por ciento». En una cuadrícula de 10 por 10, cada cuadrito vale 1 %, y cada fila o columna completa vale 10 %.",
        "El total que se compara se llama cantidad de referencia y siempre vale el 100 %. Cuando el total no es 100, se imagina cuántos serían si hubiera 100. Si de 200 cuadritos pintas 50, pintaste la cuarta parte; en 100 cuadritos serían 25, así que es el 25 %. Antes de dar un porcentaje, pregúntate: ¿porcentaje de qué total?",
        "Lo pintado y lo no pintado siempre suman 100 %. Si 82 de 100 cuadritos están pintados, el 18 % no lo está. El 100 % es el total completo y el 0 % es nada. Algunos porcentajes se reconocen rápido: 50 % es la mitad, 25 % es un cuarto y 10 % es una décima parte. El porcentaje sirve para comparar grupos de distinto tamaño.",
    ],
    vocab=[("porcentaje", "parte de una cantidad comparada con 100"), ("%", "símbolo que significa «por cada cien»"), ("cantidad de referencia", "total con el que se compara; vale el 100 %"), ("cuadrícula de cien", "cuadrado de 10 por 10 con 100 cuadritos iguales"), ("parte", "porción del total que se considera")],
    worked=[
        W("Leer un porcentaje en la cuadrícula", "En una cuadrícula de 100 cuadritos hay 37 pintados. ¿Qué porcentaje está pintado y cuál no?", ["Hay 37 de 100 pintados: 37 %.", "Lo no pintado es 100 − 37 = 63 cuadritos: 63 %."], "37 % pintado y 63 % sin pintar"),
        W("Pintar un porcentaje", "¿Cómo se representa el 20 % en una cuadrícula de 10 por 10?", ["Cada columna completa vale 10 cuadritos, o sea 10 %.", "Para 20 % se pintan 2 columnas completas, es decir, 20 cuadritos."], "Se pintan 20 cuadritos"),
    ],
    mistakes=[
        M("Decir que 50 cuadritos pintados de 200 es el 50 %.", "Se usó el número pintado como si fuera el porcentaje.", "Se compara con el total: 50 de 200 es la cuarta parte, o sea 25 de cada 100: 25 %."),
        M("Pensar que el 100 % es siempre 100 personas.", "Se confundió el porcentaje con la cantidad.", "El 100 % es el total completo, sea 20, 100 o 500 personas."),
    ],
    rec=[
        ex("Una cuadrícula de 100 cuadritos tiene 45 pintados. ¿Qué porcentaje está pintado?", "45 %", "Hay 45 de cada 100."),
        ex("¿Cuántos cuadritos hay que pintar en una cuadrícula de 100 para representar el 60 %?", "60", "Cada cuadrito vale 1 %."),
        ex("En una cuadrícula de 10 columnas iguales hay 3 columnas completas pintadas. ¿Qué porcentaje es?", "30 %", "Cada columna es 10 % y 3 × 10 = 30."),
    ],
    und=[
        ex("Cada fila de 10 cuadritos vale 10 %. ¿Cuántas filas completas hay que pintar para representar el 70 %?", "7", "7 × 10 % = 70 %."),
        ex("Una cuadrícula de 100 cuadritos tiene 82 pintados. ¿Qué porcentaje queda sin pintar?", "18 %", "100 − 82 = 18 cuadritos."),
        ex("¿Qué porcentaje de una cuadrícula representa la mitad pintada?", "50 %", "La mitad de 100 cuadritos son 50."),
    ],
    app=[
        ex("En un curso de ejemplo con 100 estudiantes, 28 usan lentes. ¿Qué porcentaje usa lentes?", "28 %", "Hay 28 de cada 100."),
        ex("Una barra de carga de ejemplo tiene 100 partes iguales y se han llenado 64. ¿Qué porcentaje falta por llenar?", "36 %", "100 − 64 = 36 partes."),
        ex("Un jardín de ejemplo tiene 100 parcelas iguales: 15 tienen flores rojas y 25 flores amarillas. ¿Qué porcentaje de las parcelas tiene flores rojas o amarillas?", "40 %", "15 + 25 = 40 parcelas de 100."),
    ],
    rea=[
        ex("Valentina pintó 50 cuadritos de una cuadrícula de 200 y dice que pintó el 50 %. ¿Está bien?", "No; es el 25 %", "Pintó 50 de 200, que es la cuarta parte: en 100 cuadritos serían 25."),
        ex("¿Qué es mayor: 30 % de una cuadrícula de 100 cuadritos o 30 cuadritos pintados de una cuadrícula de 200?", "El 30 % de la cuadrícula de 100", "30 de 100 es 30 %, pero 30 de 200 es solo 15 %."),
    ],
    cha=[
        ex("En una cuadrícula de 200 cuadritos hay 90 pintados. ¿Qué porcentaje es?", "45 %", "Dividiendo por 2: 90 de 200 equivale a 45 de 100."),
        ex("Una cuadrícula de 50 cuadritos tiene 18 pintados. ¿Qué porcentaje es?", "36 %", "Duplicando todo: 18 de 50 equivale a 36 de 100."),
    ],
    ctx=[ex("Una bolsa de ejemplo tiene 100 fichas: 23 rojas, 41 azules y las demás verdes. ¿Qué porcentaje de las fichas es verde?", "36 %", "23 + 41 = 64 y 100 − 64 = 36.")],
    sc=[
        ex("Si pintas 25 cuadritos de 100, ¿qué porcentaje pintaste?", "25 %", "Son 25 de cada 100."),
        ex("¿Cuántas filas completas de 10 cuadritos hay que pintar para el 100 %?", "10", "10 filas de 10 cuadritos forman la cuadrícula entera."),
        ex("Si el 45 % de una cuadrícula está pintada, ¿qué porcentaje no lo está?", "55 %", "100 − 45 = 55."),
    ],
    op=task(
        "Dibuja tres cuadrículas de 10 por 10. En la primera pinta el 35 %, en la segunda pinta el 60 % y en la tercera pinta el 8 %. Debajo de cada una escribe cuántos cuadritos pintaste y qué porcentaje queda sin pintar. Después explica con una frase por qué el 100 % es el total.",
        "35 %: 35 cuadritos pintados y 65 % sin pintar. 60 %: 60 cuadritos y 40 % sin pintar. 8 %: 8 cuadritos y 92 % sin pintar. El 100 % es el total porque es todo lo que se está comparando.",
        ["pinta la cantidad correcta de cuadritos", "calcula bien el porcentaje que queda sin pintar", "explica que el 100 % es el total"],
        ["tres cuadrículas dibujadas", "cálculos escritos", "frase de explicación"],
        ["pintar menos o más cuadritos de los pedidos", "restar mal de 100"],
        "Pide que cuente de nuevo los cuadritos pintados y que sume pintados más no pintados.",
    ),
    reinforce="En una cuadrícula de 100 pinta el 12 %. Escribe cuántos cuadritos pintaste y qué porcentaje quedó sin pintar.",
    extend="En una cuadrícula de 20 cuadritos pinta 5. Explica qué porcentaje es y cómo lo supiste.",
)

# ------------------------------------------------------------------ OA 04 clase 2
lesson(
    OA4, 2,
    use="Aprenderé a escribir un mismo valor como porcentaje, como fracción y como decimal. Sirve para comparar descuentos, notas y resultados de encuestas escritos de distintas formas.",
    prior=["Sé que un porcentaje es una parte de 100.", "Sé simplificar fracciones y escribir fracciones como decimales."],
    explain=[
        "Un porcentaje se puede escribir como fracción con denominador 100: 25 % = 25/100. Esa fracción se simplifica: 25/100 = 1/4. Como decimal, 25/100 = 0,25. Para pasar un porcentaje a decimal, divide por 100 (corre la coma dos lugares a la izquierda): 40 % = 0,40 = 0,4 y 7 % = 0,07. Para pasar un decimal a porcentaje, multiplica por 100.",
        "Para pasar una fracción a porcentaje, busca una fracción equivalente con denominador 100. Por ejemplo, 3/5 = 60/100 porque 5 × 20 = 100 y 3 × 20 = 60; entonces 3/5 es el 60 %. Otra manera es dividir: 3 ÷ 5 = 0,6 y 0,6 × 100 = 60 %. Con ambas maneras se llega al mismo resultado.",
        "Conviene memorizar las equivalencias más usadas: 50 % = 1/2 = 0,5; 25 % = 1/4 = 0,25; 75 % = 3/4 = 0,75; 10 % = 1/10 = 0,1; 20 % = 1/5 = 0,2; 5 % = 1/20 = 0,05. Para comparar, lleva todo a la misma forma, por ejemplo, todo a porcentaje o todo a decimal.",
    ],
    vocab=[("equivalente", "que vale lo mismo aunque se escriba distinto"), ("fracción decimal", "fracción con denominador 100, como 35/100"), ("decimal", "número con coma, como 0,35"), ("simplificar", "dividir numerador y denominador por el mismo número"), ("amplificar", "multiplicar numerador y denominador por el mismo número")],
    worked=[
        W("De porcentaje a fracción y decimal", "Escribe 40 % como fracción simplificada y como decimal.", ["40 % = 40/100. Divido arriba y abajo por 20: 2/5.", "Como decimal: 40 ÷ 100 = 0,4."], "2/5 y 0,4"),
        W("De fracción a porcentaje", "Escribe 3/20 como porcentaje.", ["Amplifico para llegar a denominador 100: 20 × 5 = 100, entonces 3 × 5 = 15 y queda 15/100.", "15/100 es el 15 %."], "15 % (0,15)"),
    ],
    mistakes=[
        M("Escribir 5 % = 0,5.", "Se dividió por 10 en vez de por 100.", "5 % = 5/100 = 0,05."),
        M("Escribir 1/4 = 14 %.", "Se juntaron los dos números del 1/4.", "1/4 = 25/100 = 25 %."),
    ],
    rec=[
        ex("Escribe 50 % como fracción simplificada.", "1/2", "50/100 se simplifica dividiendo por 50."),
        ex("Escribe 0,25 como porcentaje.", "25 %", "0,25 × 100 = 25."),
        ex("Escribe 3/10 como porcentaje.", "30 %", "3/10 = 30/100."),
    ],
    und=[
        ex("Escribe 60 % como fracción simplificada y como decimal.", "3/5 y 0,6", "60/100 = 3/5 y 60 ÷ 100 = 0,6."),
        ex("Escribe 7/20 como porcentaje.", "35 %", "7/20 = 35/100 porque 20 × 5 = 100 y 7 × 5 = 35."),
        ex("Expresa el decimal 0,08 como porcentaje.", "8 %", "0,08 × 100 = 8."),
    ],
    app=[
        ex("Una tienda de ejemplo anuncia «1/5 de descuento». ¿Qué porcentaje de descuento es?", "20 %", "1/5 = 20/100."),
        ex("En una encuesta de ejemplo, 0,35 de los estudiantes eligió el deporte. ¿Qué porcentaje es?", "35 %", "0,35 × 100 = 35."),
        ex("El 45 % de los asistentes a un taller de ejemplo son menores de edad. ¿Qué fracción simplificada es?", "9/20", "45/100 se divide por 5 arriba y abajo."),
    ],
    rea=[
        ex("Ana dice que 5 % es igual a 0,5. ¿Tiene razón?", "No; 5 % = 0,05", "5 % = 5/100 = 0,05."),
        ex("¿Qué es mayor, 2/5 o 35 %?", "2/5", "2/5 = 40 %, que es mayor que 35 %."),
    ],
    cha=[
        ex("Ordena de menor a mayor: 0,3; 1/4; 35 %; 2/5.", "1/4, 0,3, 35 %, 2/5", "Como porcentajes: 25 %, 30 %, 35 % y 40 %."),
        ex("Un número se escribe 45/100. Escríbelo como porcentaje, decimal y fracción simplificada.", "45 %, 0,45 y 9/20", "45/100 es 45 %, 0,45 y simplificando por 5 queda 9/20."),
    ],
    ctx=[ex("En un curso de ejemplo, 3/4 de los estudiantes entregó el trabajo. ¿Qué porcentaje entregó?", "75 %", "3/4 = 75/100.")],
    sc=[
        ex("Escribe 10 % como decimal.", "0,1", "10 ÷ 100 = 0,1."),
        ex("Escribe 1/2 como porcentaje.", "50 %", "1/2 = 50/100."),
        ex("Escribe 0,6 como porcentaje.", "60 %", "0,6 = 0,60 y 0,60 × 100 = 60."),
    ],
    op=task(
        "Completa esta tabla de ejemplo con las tres formas de cada valor (porcentaje, fracción simplificada y decimal): fila 1: 80 %; fila 2: 3/4; fila 3: 0,05; fila 4: 12 %. Después ordena los cuatro valores de menor a mayor.",
        "80 % = 4/5 = 0,8. 3/4 = 75 % = 0,75. 0,05 = 5 % = 1/20. 12 % = 3/25 = 0,12. Orden: 0,05 < 12 % < 3/4 < 80 %.",
        ["completa bien las tres formas de cada fila", "simplifica las fracciones", "ordena usando una misma forma"],
        ["tabla completa", "lista ordenada"],
        ["dividir por 10 en vez de por 100", "ordenar comparando formas distintas sin convertir"],
        "Pide que lleve los cuatro valores a porcentaje antes de ordenarlos.",
    ),
    reinforce="Escribe 25 %, 90 % y 4 % como fracción simplificada y como decimal.",
    extend="Busca una fracción que equivalga a un porcentaje entero con denominador distinto de 100 y explica cómo la encontraste.",
)

# ------------------------------------------------------------------ OA 04 clase 3
lesson(
    OA4, 3,
    use="Aprenderé varias estrategias para calcular un porcentaje de una cantidad. Sirve para saber cuánto es el descuento, la propina o la parte de un grupo sin usar siempre calculadora.",
    prior=["Sé escribir porcentajes como fracciones y decimales.", "Sé dividir por 10 y por 100."],
    explain=[
        "Hay varias formas de calcular el porcentaje de una cantidad. Con el 10 %: divide la cantidad por 10 y multiplica según corresponda. El 10 % de 240 es 24, así que el 30 % es 3 × 24 = 72. Con las mitades: el 50 % es la mitad y el 25 % es la mitad de la mitad. El 1 % se calcula dividiendo por 100.",
        "Otra forma es usar el decimal: el 35 % de 200 es 0,35 × 200 = 70. También puedes usar la fracción: 25 % de 360 es 1/4 de 360, o sea 360 ÷ 4 = 90. Y puedes combinar: el 15 % es el 10 % más la mitad del 10 %. Siempre debes tener claro de qué cantidad se calcula el porcentaje.",
        "Elige la estrategia más cómoda según los números. Para 50 %, 25 % o 10 % usa la mitad, el cuarto o la décima. Para 35 %, usa 10 % tres veces más la mitad de 10 %. Si necesitas la cantidad total sabiendo una parte, divide la parte por su porcentaje y multiplica por 100. Comprueba con una estimación: el 30 % de 240 debe ser menos que la mitad de 240 (120) y más que su cuarta parte (60).",
    ],
    vocab=[("estrategia", "manera de resolver un problema"), ("décima parte", "una de diez partes iguales; es el 10 %"), ("mitad de la mitad", "forma de calcular el 25 %"), ("factor decimal", "porcentaje escrito como decimal para multiplicar, como 0,35"), ("cantidad total", "número del cual se calcula el porcentaje")],
    worked=[
        W("Estrategia del 10 %", "Calcula el 30 % de 240.", ["El 10 % de 240 es 24 (240 ÷ 10).", "El 30 % son tres veces el 10 %: 3 × 24 = 72. Con el decimal: 0,3 × 240 = 72."], "72"),
        W("Mitad de la mitad", "Calcula el 25 % de 360.", ["El 50 % es la mitad: 180.", "El 25 % es la mitad de eso: 90."], "90"),
    ],
    mistakes=[
        M("Calcular el 20 % de 90 como 20 × 90 = 1.800.", "Se multiplicó por 20 sin pasar el porcentaje a decimal.", "El 20 % de 90 es 0,2 × 90 = 18."),
        M("Creer que el 25 % de 80 es 25.", "Se confundió el número del porcentaje con el resultado.", "El 25 % es un cuarto: 80 ÷ 4 = 20."),
    ],
    rec=[
        ex("¿Cuánto es el 10 % de 80?", "8", "80 ÷ 10 = 8."),
        ex("¿Cuánto es el 50 % de 46?", "23", "El 50 % es la mitad."),
        ex("¿Cuánto es el 1 % de 700?", "7", "700 ÷ 100 = 7."),
    ],
    und=[
        ex("Calcula el 20 % de 150.", "30", "El 10 % es 15 y el 20 % es 2 × 15."),
        ex("Calcula el 25 % de 120.", "30", "La mitad de 120 es 60 y la mitad de 60 es 30."),
        ex("Calcula el 75 % de 80.", "60", "El 25 % de 80 es 20 y el 75 % es 3 × 20."),
    ],
    app=[
        ex("Una polera de ejemplo cuesta $12.000 y tiene un 25 % de descuento. ¿Cuántos pesos se descuentan?", "$3.000", "12.000 ÷ 4 = 3.000."),
        ex("En un curso de 40 estudiantes, el 35 % faltó un día. ¿Cuántos estudiantes faltaron?", "14", "El 10 % de 40 es 4; 3 × 4 = 12 y el 5 % es 2; 12 + 2 = 14."),
        ex("Un libro de ejemplo tiene 320 páginas y ya se leyó el 15 %. ¿Cuántas páginas se leyeron?", "48", "El 10 % es 32 y el 5 % es 16; 32 + 16 = 48."),
    ],
    rea=[
        ex("Dani calculó el 20 % de 90 como 1.800. ¿Cuál es el resultado correcto?", "18", "El 20 % de 90 es 0,2 × 90 = 18."),
        ex("¿Verdadero o falso? «Para hallar el 5 % de una cantidad se puede calcular el 10 % y dividirlo por 2».", "Verdadero", "5 es la mitad de 10, así que el 5 % es la mitad del 10 %."),
    ],
    cha=[
        ex("El 15 % de una cantidad es 45. ¿Cuál es la cantidad total?", "300", "Si 15 % son 45, 1 % son 3 y el 100 % son 300."),
        ex("El 10 % de una cantidad es 24. ¿Cuánto es el 35 % de esa misma cantidad?", "84", "El 100 % es 240 y el 35 % es 0,35 × 240 = 84."),
    ],
    ctx=[ex("En un grupo de ejemplo de 60 personas, el 40 % son niños. ¿Cuántos niños hay?", "24", "El 10 % de 60 es 6 y 4 × 6 = 24.")],
    sc=[
        ex("¿Cuánto es el 50 % de 90?", "45", "Es la mitad de 90."),
        ex("¿Cuánto es el 30 % de 50?", "15", "El 10 % es 5 y 3 × 5 = 15."),
        ex("¿Cuánto es el 25 % de 200?", "50", "200 ÷ 4 = 50."),
    ],
    op=task(
        "Una librería de ejemplo ofrece un cuaderno a $6.000, una mochila a $18.000 y un estuche a $4.000. Aplica el descuento indicado a cada uno y escribe cuántos pesos se descuentan y cuánto se paga: cuaderno 50 %, mochila 15 %, estuche 25 %. Calcula cada porcentaje con una estrategia distinta y escribe cuál usaste.",
        "Cuaderno: 50 % es la mitad, se descuentan $3.000 y se pagan $3.000. Mochila: 10 % = 1.800 y 5 % = 900, así que se descuentan 2.700 y se pagan 15.300. Estuche: 25 % es la mitad de la mitad, se descuentan 1.000 y se pagan 3.000.",
        ["calcula bien cada descuento", "usa estrategias distintas y las nombra", "calcula el precio final"],
        ["tres cálculos", "frase con la estrategia"],
        ["usar el porcentaje como si fuera pesos", "no restar el descuento al precio"],
        "Pide que compruebe cada descuento con una estimación, por ejemplo que el 15 % es menos de la mitad de la mitad.",
    ),
    reinforce="Calcula el 10 %, el 20 % y el 5 % de 360. Escribe cómo calculaste cada uno.",
    extend="Explica dos formas distintas de calcular el 35 % de 80 y comprueba que dan el mismo resultado.",
)

# ------------------------------------------------------------------ OA 04 clase 4
lesson(
    OA4, 4,
    use="Aprenderé a resolver y evaluar situaciones sencillas con porcentajes, como descuentos, aumentos y encuestas, y a decidir de qué total se habla. Sirve para elegir mejor ofertas y entender datos.",
    prior=["Sé calcular un porcentaje de una cantidad.", "Sé escribir porcentajes como fracción y decimal."],
    explain=[
        "En una situación con porcentajes, lo primero es identificar el total de referencia: ¿el porcentaje es de qué cantidad? En una encuesta de 240 respuestas, el 30 % que eligió la opción A es el 30 % de 240, o sea 72 respuestas. Los que no eligieron A son el 70 % restante: 240 − 72 = 168 respuestas.",
        "En un descuento, el precio final es el precio original menos el descuento. Si un producto cuesta $30.000 y tiene 20 % de descuento, se descuentan $6.000 y se paga $24.000. En un aumento, se suma: un 10 % de aumento sobre $40.000 deja el precio en $44.000. También se puede calcular el precio final directo: con 20 % de descuento se paga el 80 %.",
        "Para comparar grupos de distinto tamaño, usa porcentajes, no cantidades. Si en el grupo A son 12 de 40 y en el grupo B son 15 de 60, mira 12/40 = 30 % y 15/60 = 25 %. Aunque B tenga más personas, en A el porcentaje es mayor. Evalúa siempre si el resultado es razonable: un descuento nunca puede ser más que el precio.",
    ],
    vocab=[("descuento", "rebaja que se hace a un precio"), ("aumento", "alza que se agrega a un precio"), ("precio final", "lo que se paga después del descuento o aumento"), ("encuesta", "preguntas hechas a un grupo para conocer sus respuestas"), ("comparar", "mirar dos valores para ver cuál es mayor, menor o igual")],
    worked=[
        W("Encuesta", "En una encuesta de 240 respuestas, el 30 % eligió A. ¿Cuántas respuestas no eligieron A?", ["30 % de 240 = 0,3 × 240 = 72 eligieron A.", "Las demás son 240 − 72 = 168."], "168 respuestas"),
        W("Descuento", "Unas zapatillas de ejemplo cuestan $30.000 y tienen 20 % de descuento. ¿Cuánto se paga?", ["20 % de 30.000 = 6.000 de descuento.", "Precio final: 30.000 − 6.000 = 24.000."], "$24.000"),
    ],
    mistakes=[
        M("Decir que 15 personas de un grupo de 60 son un porcentaje mayor que 12 de 40 «porque 15 es más que 12».", "Se compararon las cantidades en vez de los porcentajes.", "15 de 60 es el 25 % y 12 de 40 es el 30 %: es mayor 12 de 40."),
        M("Calcular un aumento de 10 % sobre $40.000 y responder $4.000.", "Se entregó solo el aumento y no el nuevo precio.", "El precio final es 40.000 + 4.000 = 44.000."),
    ],
    rec=[
        ex("Un pantalón de ejemplo cuesta $20.000 y tiene 10 % de descuento. ¿Cuántos pesos se descuentan?", "$2.000", "El 10 % de 20.000 es 2.000."),
        ex("Si se descuenta el 10 % de un precio, ¿qué porcentaje del precio se paga?", "90 %", "100 % − 10 % = 90 %."),
        ex("¿Cuánto es el 40 % de 50?", "20", "El 10 % de 50 es 5 y 4 × 5 = 20."),
    ],
    und=[
        ex("Una chaqueta de ejemplo cuesta $15.000 y tiene 20 % de descuento. ¿Cuánto se paga?", "$12.000", "Descuento: 3.000. Precio final: 15.000 − 3.000 = 12.000."),
        ex("Un equipo de ejemplo ganó 18 de 20 partidos. ¿Qué porcentaje ganó?", "90 %", "18/20 = 90/100."),
        ex("De 50 estudiantes, 30 viajan en bus. ¿Qué porcentaje viaja en bus?", "60 %", "30/50 = 60/100."),
    ],
    app=[
        ex("En el taller A hay 9 de 30 estudiantes inscritos y en el taller B hay 20 de 80. ¿En cuál es mayor el porcentaje de inscritos?", "En el taller A", "A tiene 9/30 = 30 % y B tiene 20/80 = 25 %."),
        ex("El precio de un televisor de ejemplo es $200.000 y sube un 10 %. ¿Cuál es el nuevo precio?", "$220.000", "El aumento es 20.000 y 200.000 + 20.000 = 220.000."),
        ex("En una encuesta de 80 respuestas, el 25 % dijo sí, el 45 % dijo no y el resto no sabe. ¿Cuántas respuestas son de «no sabe»?", "24", "25 % + 45 % = 70 %, queda 30 % de 80 = 24."),
    ],
    rea=[
        ex("Ema dice: «el 20 % de 50 es mayor que el 10 % de 200 porque 20 es mayor que 10». ¿Tiene razón?", "No", "El 20 % de 50 es 10 y el 10 % de 200 es 20."),
        ex("Una tienda ofrece 50 % de descuento a un abrigo de $18.000. Otra ofrece un descuento de $8.000 al mismo abrigo. ¿Qué descuento conviene más?", "El 50 %", "El 50 % de 18.000 son 9.000, que es más que 8.000."),
    ],
    cha=[
        ex("Un precio de ejemplo de 100 pesos sube un 10 % y luego baja un 10 % del nuevo precio. ¿Queda igual que al inicio?", "No; queda en 99 pesos", "Sube a 110. El 10 % de 110 es 11 y 110 − 11 = 99."),
        ex("En un curso de ejemplo de 25 estudiantes, el 40 % son niñas. Llegan 5 niñas más. ¿Qué porcentaje del nuevo curso son niñas?", "50 %", "Antes eran 10 niñas. Ahora hay 15 niñas de 30 estudiantes, que es la mitad."),
    ],
    ctx=[ex("Una encuesta de ejemplo tiene 200 respuestas. El 45 % prefiere el recreo largo. ¿Cuántas personas lo prefieren?", "90", "El 10 % de 200 es 20; 4 × 20 = 80 y el 5 % es 10; 80 + 10 = 90.")],
    sc=[
        ex("¿Cuánto es el 60 % de 150?", "90", "El 10 % es 15 y 6 × 15 = 90."),
        ex("Un pan cuesta $1.000 y sube 10 %. ¿Cuál es el nuevo precio?", "$1.100", "El aumento es 100."),
        ex("De 25 estudiantes, 5 usan bicicleta. ¿Qué porcentaje es?", "20 %", "5/25 = 1/5 = 20 %."),
    ],
    op=task(
        "Una tienda de ejemplo tiene estas ofertas. Mochila: $25.000 con 20 % de descuento. Zapatillas: $40.000 con 15 % de descuento. Chaleco: $30.000 con 25 % de descuento. (a) Calcula cuánto se descuenta y cuánto se paga por cada producto. (b) Indica en cuál producto el descuento en pesos es mayor. (c) Explica si el producto con mayor porcentaje es el que más pesos descuenta.",
        "Mochila: 5.000 de descuento, se paga 20.000. Zapatillas: 6.000, se paga 34.000. Chaleco: 7.500, se paga 22.500. El mayor descuento en pesos es el chaleco. Aquí el mayor porcentaje también coincide, pero en general depende del precio.",
        ["calcula los tres descuentos y precios finales", "compara descuentos en pesos", "explica la relación entre porcentaje y precio"],
        ["tabla de resultados", "frase de explicación"],
        ["comparar porcentajes sin considerar el precio", "olvidar restar el descuento"],
        "Pide que compruebe que descuento + precio final = precio original.",
    ),
    reinforce="Calcula el precio final de un producto de $12.000 con 15 % de descuento.",
    extend="Explica por qué subir un 20 % y luego bajar un 20 % no deja un precio igual al inicial. Usa un ejemplo con números.",
)

# ------------------------------------------------------------------ OA 05 clase 1
lesson(
    OA5, 1,
    use="Aprenderé qué es una potencia de base diez y cómo se lee. Sirve para escribir números muy grandes, como mil, un millón o mil millones, de forma corta.",
    prior=["Sé multiplicar por 10, 100 y 1.000.", "Sé leer y escribir números grandes."],
    explain=[
        "Una potencia es una multiplicación repetida del mismo número. En 10³ el 10 es la base, el 3 es el exponente y se lee «diez elevado a tres». El exponente dice cuántas veces se escribe la base como factor: 10³ = 10 × 10 × 10 = 1.000. Cuidado: 10³ no es 10 × 3.",
        "Con base 10 hay un patrón fácil: el exponente es la cantidad de ceros que tiene el resultado. 10² = 100 (dos ceros), 10⁴ = 10.000 (cuatro ceros) y 10⁶ = 1.000.000 (seis ceros). Por eso 10³ es mil, 10⁶ es un millón y 10⁹ es mil millones. Así, un 1 seguido de siete ceros se escribe como 10⁷.",
        "Para multiplicar por una potencia de 10, escribe a la derecha del número tantos ceros como indica el exponente: 7 × 10³ = 7.000. Para leer una potencia, nombra primero la base y luego el exponente. Siempre revisa la posición: el exponente es pequeño y va arriba a la derecha de la base.",
    ],
    vocab=[("potencia", "multiplicación repetida del mismo número"), ("base", "número que se multiplica por sí mismo"), ("exponente", "número pequeño que dice cuántas veces se escribe la base"), ("elevado a", "forma de leer una potencia: «diez elevado a cinco»"), ("factor", "número que se multiplica")],
    worked=[
        W("Calcular una potencia", "Calcula 10⁵.", ["10⁵ = 10 × 10 × 10 × 10 × 10.", "El exponente 5 indica cinco ceros: 100.000."], "100.000"),
        W("Escribir como potencia", "Escribe 10.000.000 como potencia de 10.", ["Cuento los ceros: 7.", "Entonces es 10⁷."], "10⁷"),
    ],
    mistakes=[
        M("Escribir 10³ = 30.", "Se multiplicó la base por el exponente.", "El exponente indica cuántas veces se multiplica la base: 10 × 10 × 10 = 1.000."),
        M("Escribir 10⁴ = 1.000.", "Se contó un cero de menos.", "El exponente 4 indica cuatro ceros: 10.000."),
    ],
    rec=[
        ex("10⁴ es 10 × 10 × 10 × 10. ¿Qué número es?", "10.000", "El resultado tiene cuatro ceros."),
        ex("En la potencia 10⁸, ¿cuál es el exponente?", "8", "El exponente es el número pequeño de arriba."),
        ex("En la potencia 10⁵, ¿cuál es la base?", "10", "La base es el número que se multiplica."),
    ],
    und=[
        ex("¿Cuántos ceros tiene el número 10⁷?", "7", "El exponente indica la cantidad de ceros."),
        ex("Escribe 1.000.000 como potencia de 10.", "10⁶", "El número tiene seis ceros."),
        ex("Escribe 1.000.000.000 (mil millones) como potencia de 10.", "10⁹", "El número tiene nueve ceros."),
    ],
    app=[
        ex("Una biblioteca de ejemplo tiene 10³ libros y cada libro tiene unas 100 páginas. ¿Cuántas páginas hay en total?", "100.000", "1.000 × 100 = 100.000."),
        ex("Un tren recorre 10³ metros en un minuto. Si mantiene el mismo ritmo, ¿cuántos metros recorre en 10 minutos?", "10.000", "1.000 × 10 = 10.000, que es 10⁴."),
        ex("Escribe 10⁵ con todos sus ceros y di cómo se lee.", "100.000, cien mil", "El exponente 5 indica cinco ceros."),
    ],
    rea=[
        ex("Un estudiante escribió 10³ = 30. ¿Cuál es el valor correcto?", "1.000", "10³ = 10 × 10 × 10, no 10 × 3."),
        ex("¿Es 10² igual a 2 × 10? Responde sí o no.", "No", "10² = 100 y 2 × 10 = 20."),
    ],
    cha=[
        ex("¿Qué es mayor, 10⁴ o 9.999?", "10⁴", "10⁴ = 10.000, que es mayor que 9.999."),
        ex("¿Cuántas veces cabe 10³ en 10⁶? Escribe el número.", "1.000", "1.000.000 ÷ 1.000 = 1.000."),
    ],
    ctx=[ex("Un estadio de ejemplo tiene capacidad para 10⁴ personas. Si se llenan 10 estadios iguales, ¿cuántas personas caben en total?", "100.000", "10.000 × 10 = 100.000.")],
    sc=[
        ex("Escribe 10² como número.", "100", "10 × 10."),
        ex("¿Cuántos ceros tiene 10¹⁰? ", "10", "El exponente es la cantidad de ceros."),
        ex("Escribe 100.000 como potencia de 10.", "10⁵", "Tiene cinco ceros."),
    ],
    op=task(
        "Completa esta tabla de ejemplo con una regla. Fila 1: 10² = ___. Fila 2: 10⁵ = ___. Fila 3: ___ = 1.000.000. Fila 4: 10⁹ = ___. Para cada fila escribe la multiplicación repetida cuando el exponente sea menor que 5, y cómo se lee en voz alta. Después explica con una frase cómo se relaciona el exponente con los ceros.",
        "10² = 10 × 10 = 100 (diez al cuadrado). 10⁵ = 100.000 (diez elevado a cinco). 1.000.000 = 10⁶. 10⁹ = 1.000.000.000 (mil millones). El exponente es la cantidad de ceros.",
        ["completa las cuatro filas", "escribe la multiplicación repetida cuando corresponde", "explica la relación exponente-ceros"],
        ["tabla completa", "frase de explicación"],
        ["contar mal los ceros", "multiplicar base por exponente"],
        "Pide que cuente los ceros de su respuesta y los compare con el exponente.",
    ),
    reinforce="Escribe 10³, 10⁴ y 10⁷ como números con todos sus ceros.",
    extend="Escribe un número con seis ceros y otro con ocho ceros usando potencias de 10. Lee cada uno en voz alta.",
)

# ------------------------------------------------------------------ OA 05 clase 2
lesson(
    OA5, 2,
    use="Aprenderé por qué 10⁰ vale 1 y cómo se relaciona con el valor posicional. Sirve para escribir cualquier número como suma de potencias de 10.",
    prior=["Sé qué es una potencia de base 10.", "Sé dividir por 10."],
    explain=[
        "Mira el patrón: 10³ = 1.000, 10² = 100, 10¹ = 10. Cada vez que el exponente baja en 1, el número se divide por 10: 1.000 ÷ 10 = 100 y 100 ÷ 10 = 10. Si seguimos el patrón, el siguiente es 10 ÷ 10 = 1. Por eso se define 10⁰ = 1. No es 0 ni 10: es 1.",
        "El exponente 1 deja la base igual: 10¹ = 10. El exponente 0 siempre da 1 cuando se usa en el sistema decimal. Esto es importante en el valor posicional: la posición de las unidades vale 10⁰ = 1, la de las decenas vale 10¹ = 10, la de las centenas vale 10² = 100, y así sucesivamente.",
        "Con esto, cualquier cifra se multiplica por la potencia de su posición. En 3.405, el 5 está en las unidades y vale 5 × 10⁰ = 5. Cuando una potencia con exponente 0 se multiplica por una cifra, el valor no cambia: 8 × 10⁰ = 8. Usa el patrón de dividir por 10 siempre que dudes.",
    ],
    vocab=[("exponente cero", "exponente 0; con base 10 da siempre 1"), ("valor posicional", "valor que tiene una cifra según el lugar que ocupa"), ("unidades", "posición de la derecha, que vale 10⁰"), ("patrón", "regla que se repite y permite seguir una secuencia"), ("potencia de 10", "número de la forma 10 elevado a un exponente")],
    worked=[
        W("Seguir el patrón", "Completa: 10³ = 1.000, 10² = 100, 10¹ = 10, 10⁰ = ?", ["Cada paso se divide por 10: 1.000 → 100 → 10.", "El siguiente es 10 ÷ 10 = 1."], "10⁰ = 1"),
        W("Valor de una cifra en las unidades", "En el número 7.206, ¿cuánto vale el 6 con su potencia de 10?", ["El 6 está en las unidades, que valen 10⁰ = 1.", "Entonces vale 6 × 10⁰ = 6."], "6 × 10⁰ = 6"),
    ],
    mistakes=[
        M("Decir que 10⁰ = 0.", "Se asoció el exponente 0 con el resultado 0.", "Por el patrón de dividir por 10, 10⁰ = 1."),
        M("Decir que 10⁰ = 10.", "Se confundió con el exponente 1.", "10¹ = 10, pero 10⁰ = 1."),
    ],
    rec=[
        ex("¿Cuánto es 10¹?", "10", "Exponente 1 deja la base igual."),
        ex("¿Cuánto es 10⁰?", "1", "Por el patrón 1.000, 100, 10, 1."),
        ex("En el patrón 100.000, 10.000, 1.000, 100, 10, ¿qué número sigue y qué potencia de 10 es?", "1, que es 10⁰", "Cada término se divide por 10: 10 ÷ 10 = 1."),
    ],
    und=[
        ex("Calcula 5 × 10⁰.", "5", "5 × 1 = 5."),
        ex("¿Qué exponente falta? 10___ = 10.", "1", "10¹ = 10."),
        ex("Calcula 10⁰ + 10¹ + 10².", "111", "1 + 10 + 100 = 111."),
    ],
    app=[
        ex("Escribe como número: 4 × 10¹ + 6 × 10⁰.", "46", "40 + 6."),
        ex("Escribe como número: 2 × 10² + 0 × 10¹ + 9 × 10⁰.", "209", "200 + 0 + 9."),
        ex("En el número 3.405, ¿qué potencia de 10 multiplica a la cifra 5?", "10⁰", "El 5 está en las unidades."),
    ],
    rea=[
        ex("Marta dice que 10⁰ = 0 porque el exponente es 0. ¿Cuál es el valor correcto?", "1", "El patrón 10 ÷ 10 = 1 define 10⁰ = 1."),
        ex("¿Verdadero o falso? «10⁰ es igual a 10¹ dividido por 10».", "Verdadero", "10 ÷ 10 = 1 = 10⁰."),
    ],
    cha=[
        ex("Ordena de menor a mayor: 10², 10⁰, 10³, 10¹.", "10⁰, 10¹, 10², 10³", "Valen 1, 10, 100 y 1.000."),
        ex("¿Qué exponente n cumple 10ⁿ ÷ 10 = 10⁰?", "1", "10¹ ÷ 10 = 1 = 10⁰."),
    ],
    ctx=[ex("En un código de ejemplo cada posición vale una potencia de 10 desde la derecha: unidades 10⁰, decenas 10¹, etc. ¿Qué potencia vale la posición de las centenas?", "10²", "Centenas: 100 = 10².")],
    sc=[
        ex("Calcula 9 × 10⁰.", "9", "9 × 1."),
        ex("¿Cuánto es 10⁰ + 10⁰?", "2", "1 + 1."),
        ex("¿Qué potencia de 10 vale la posición de las decenas?", "10¹", "Las decenas valen 10."),
    ],
    op=task(
        "Completa el patrón que baja de a un exponente: 10⁴ = 10.000, 10³ = ___, 10² = ___, 10¹ = ___, 10⁰ = ___. Escribe qué operación pasas de una fila a la siguiente. Después explica con una frase por qué 10⁰ no puede ser 0.",
        "10³ = 1.000, 10² = 100, 10¹ = 10, 10⁰ = 1. De una fila a la siguiente se divide por 10. Si 10⁰ fuera 0, el patrón se rompería, porque 10 ÷ 10 = 1.",
        ["completa el patrón", "indica la operación entre filas", "explica por qué 10⁰ = 1"],
        ["patrón completo", "frase de explicación"],
        ["afirmar que 10⁰ = 0 o 10", "no justificar con el patrón"],
        "Pide que compruebe que cada resultado es el anterior dividido por 10.",
    ),
    reinforce="Escribe 10⁰, 10¹, 10² y 10³ como números, y suma los cuatro.",
    extend="Escribe el número 1.111 como suma de potencias de 10 de exponente 0 a 3.",
)

# ------------------------------------------------------------------ OA 05 clase 3
lesson(
    OA5, 3,
    use="Aprenderé a descomponer un número usando potencias de 10 según el valor posicional de sus cifras. Sirve para entender cómo se arma un número y para preparar la notación científica.",
    prior=["Sé qué es 10⁰, 10¹, 10², 10³… ", "Sé el valor posicional de las cifras."],
    explain=[
        "Cada cifra de un número vale según su posición. En 4.256, el 4 está en las unidades de mil, el 2 en las centenas, el 5 en las decenas y el 6 en las unidades. Con potencias de 10 se escribe: 4.256 = 4 × 10³ + 2 × 10² + 5 × 10¹ + 6 × 10⁰. Cada cifra se multiplica por la potencia de su posición.",
        "Si una cifra es 0, ese término puede no escribirse. Así, 3.040 = 3 × 10³ + 0 × 10² + 4 × 10¹ + 0 × 10⁰ = 3 × 10³ + 4 × 10¹. El exponente de cada término es la posición de la cifra contando desde la derecha, con la posición de las unidades como 0. Un número con 5 cifras tiene como mayor exponente 4.",
        "Para armar un número desde su descomposición, calcula cada término y suma. 6 × 10³ + 2 × 10² + 9 × 10⁰ = 6.000 + 200 + 9 = 6.209. Fíjate en que falta la potencia 10¹: en las decenas hay un cero. Revisa siempre que cada posición aparezca una sola vez y que ninguna esté de más.",
    ],
    vocab=[("descomposición", "escritura de un número como suma de partes"), ("posición", "lugar de una cifra, contando desde la derecha"), ("término", "cada parte de una suma"), ("cifra", "cada dígito de un número"), ("unidad de mil", "posición que vale 10³ = 1.000")],
    worked=[
        W("Descomponer", "Descompón 4.256 con potencias de 10.", ["4 está en la posición de exponente 3, 2 en la de exponente 2, 5 en la de exponente 1 y 6 en la de exponente 0.", "Escribo cada cifra por su potencia y sumo."], "4 × 10³ + 2 × 10² + 5 × 10¹ + 6 × 10⁰"),
        W("Armar el número", "¿Qué número es 3 × 10⁴ + 7 × 10²?", ["3 × 10⁴ = 30.000 y 7 × 10² = 700.", "30.000 + 700 = 30.700."], "30.700"),
    ],
    mistakes=[
        M("Escribir 3.050 = 3 × 10³ + 5 × 10².", "Se asignó mal la posición del 5.", "El 5 está en las decenas: 3.050 = 3 × 10³ + 5 × 10¹."),
        M("Escribir 507 = 5 × 10¹ + 7 × 10⁰.", "Se olvidó que el 5 está en las centenas.", "507 = 5 × 10² + 0 × 10¹ + 7 × 10⁰."),
    ],
    rec=[
        ex("Completa: 52 = 5 × 10___ + 2 × 10⁰.", "1", "El 5 está en las decenas, que valen 10¹."),
        ex("¿Cuánto es 3 × 10²?", "300", "3 × 100."),
        ex("En 8.903, ¿qué cifra está en la posición de 10²?", "9", "10² es la posición de las centenas."),
    ],
    und=[
        ex("Escribe como número: 6 × 10³ + 2 × 10² + 9 × 10⁰.", "6.209", "6.000 + 200 + 9."),
        ex("En 80.452, ¿por qué potencia de 10 se multiplica la cifra 8?", "10⁴", "El 8 está en la quinta posición desde la derecha: exponente 4."),
        ex("Descompón 7.305 con potencias de 10 (puedes omitir el término con cero).", "7 × 10³ + 3 × 10² + 5 × 10⁰", "El 0 está en las decenas, por eso no hay término con 10¹."),
    ],
    app=[
        ex("Una tienda de ejemplo tiene 2 × 10³ + 5 × 10² + 4 × 10¹ productos. ¿Cuántos productos tiene?", "2.540", "2.000 + 500 + 40."),
        ex("En el número 9.017, ¿qué cifra se multiplica por 10¹?", "1", "La cifra de las decenas es 1."),
        ex("Un código de ejemplo es 4 × 10⁵ + 3 × 10² + 8 × 10⁰. ¿Qué número es?", "400.308", "400.000 + 300 + 8."),
    ],
    rea=[
        ex("Pedro escribió 3.050 = 3 × 10³ + 5 × 10². ¿Cuál es la descomposición correcta?", "3 × 10³ + 5 × 10¹", "El 5 está en las decenas."),
        ex("¿Cuántas cifras tiene el número 6 × 10⁵ + 2 × 10³ + 7 × 10⁰?", "6", "Es 602.007: seis cifras."),
    ],
    cha=[
        ex("Escribe 100.000 + 3.000 + 20 como suma de potencias de 10 con su cifra.", "1 × 10⁵ + 3 × 10³ + 2 × 10¹", "Cada sumando es una cifra por su potencia."),
        ex("Calcula 9 × 10³ + 9 × 10² + 9 × 10¹ + 9 × 10⁰ + 1 y escribe el resultado como potencia de 10.", "10.000 = 10⁴", "9.999 + 1 = 10.000."),
    ],
    ctx=[ex("El marcador de visitas de un museo de ejemplo muestra 5 × 10⁴ + 6 × 10³ + 1 × 10¹ visitas. ¿Cuántas visitas son?", "56.010", "50.000 + 6.000 + 10.")],
    sc=[
        ex("¿Cuánto es 4 × 10³?", "4.000", "4 × 1.000."),
        ex("Descompón 83 con potencias de 10.", "8 × 10¹ + 3 × 10⁰", "80 + 3."),
        ex("¿Qué número es 7 × 10² + 1 × 10⁰?", "701", "700 + 1."),
    ],
    op=task(
        "Descompón estos números con potencias de 10: 5.208, 30.060 y 700.401. Después arma el número que corresponde a 8 × 10⁴ + 6 × 10² + 3 × 10¹. En una frase explica por qué en algunos números no aparece algún exponente.",
        "5.208 = 5 × 10³ + 2 × 10² + 8 × 10⁰. 30.060 = 3 × 10⁴ + 6 × 10¹. 700.401 = 7 × 10⁵ + 4 × 10² + 1 × 10⁰. 8 × 10⁴ + 6 × 10² + 3 × 10¹ = 80.630. Algunos exponentes no aparecen porque esa posición tiene un cero.",
        ["descompone bien los tres números", "arma correctamente el número final", "explica el rol del cero"],
        ["tres descomposiciones", "número armado", "frase de explicación"],
        ["asignar mal los exponentes", "olvidar el cero en el número armado"],
        "Pide que compruebe cada descomposición sumando los términos.",
    ),
    reinforce="Descompón 4.371 y 90.508 con potencias de 10.",
    extend="Explica cómo se relaciona la cantidad de cifras de un número con el mayor exponente de su descomposición.",
)

# ------------------------------------------------------------------ OA 05 clase 4
lesson(
    OA5, 4,
    use="Aprenderé a escribir números naturales grandes en notación científica. Sirve para ahorrar ceros, comparar tamaños y leer datos de ciencias y tecnología.",
    prior=["Sé qué es una potencia de 10.", "Sé descomponer números con potencias de 10."],
    explain=[
        "La notación científica escribe un número como a × 10ⁿ, donde a es un número mayor o igual que 1 y menor que 10, y n es un número natural. Por ejemplo, 3.000 = 3 × 10³. Si el número no es redondo, a lleva coma: 45.000 = 4,5 × 10⁴, porque 4,5 × 10.000 = 45.000.",
        "Para escribir un número en notación científica, sigue estos pasos. Primero, ubica la coma después de la primera cifra: 45.000 pasa a 4,5. Segundo, cuenta cuántos lugares corriste la coma: fueron 4. Tercero, escribe 4,5 × 10⁴. Una forma rápida: el exponente es la cantidad de cifras del número menos 1. Por ejemplo, 8.450.000 tiene 7 cifras, el exponente es 6 y se escribe 8,45 × 10⁶.",
        "Para volver al número, multiplica por la potencia de 10, es decir, corre la coma hacia la derecha tantos lugares como indique el exponente: 2,5 × 10³ = 2.500. Revisa que a esté entre 1 y 10: 45 × 10³ no está en notación científica, porque 45 es mayor que 10; se escribe 4,5 × 10⁴.",
    ],
    vocab=[("notación científica", "forma de escribir un número como a × 10ⁿ con a entre 1 y 10"), ("coeficiente", "número a que multiplica la potencia de 10"), ("orden de magnitud", "exponente n de la potencia de 10 en la notación científica"), ("exponente", "número pequeño de arriba; dice cuántos lugares se corre la coma"), ("correr la coma", "mover la coma a la izquierda o a la derecha")],
    worked=[
        W("Escribir en notación científica", "Escribe 72.000 en notación científica.", ["Ubico la coma tras la primera cifra: 7,2.", "La coma se corrió 4 lugares, así que el exponente es 4."], "7,2 × 10⁴"),
        W("Volver al número", "Escribe 6,3 × 10⁵ como número.", ["Corro la coma 5 lugares a la derecha: 6,3 → 630.000.", "Compruebo: 6,3 × 100.000 = 630.000."], "630.000"),
    ],
    mistakes=[
        M("Escribir 8.450.000 = 84,5 × 10⁵ como notación científica.", "El coeficiente 84,5 es mayor que 10.", "8.450.000 = 8,45 × 10⁶."),
        M("Escribir 3.000 = 3 × 10⁴.", "Se contó un cero de más.", "3.000 = 3 × 10³ porque hay 3 ceros."),
    ],
    rec=[
        ex("Escribe 3.000 en notación científica.", "3 × 10³", "3.000 = 3 × 1.000."),
        ex("¿Cuál está bien escrito en notación científica: 12 × 10³ o 1,2 × 10⁴?", "1,2 × 10⁴", "El coeficiente debe estar entre 1 y 10."),
        ex("Escribe 6 × 10⁵ como número.", "600.000", "6 seguido de cinco ceros."),
    ],
    und=[
        ex("Escribe 45.000 en notación científica.", "4,5 × 10⁴", "La coma se corre 4 lugares."),
        ex("Escribe 700.000 en notación científica.", "7 × 10⁵", "El número tiene 6 cifras: exponente 5."),
        ex("Escribe 2,5 × 10³ como número.", "2.500", "Se corre la coma 3 lugares."),
    ],
    app=[
        ex("Un estadio de ejemplo tiene capacidad para 62.000 personas. Escribe esa cantidad en notación científica.", "6,2 × 10⁴", "La coma se corre 4 lugares."),
        ex("Una distancia de ejemplo es 84.000.000 m. Escríbela en notación científica.", "8,4 × 10⁷", "El número tiene 8 cifras: exponente 7."),
        ex("Un pueblo de ejemplo tiene 3,6 × 10³ habitantes. ¿Cuántos habitantes son?", "3.600", "Se corre la coma 3 lugares."),
    ],
    rea=[
        ex("Ana escribió 450 = 45 × 10¹ en notación científica. ¿Cuál es la forma correcta?", "4,5 × 10²", "El coeficiente debe ser menor que 10."),
        ex("Un número tiene 9 cifras. ¿Qué exponente tiene su notación científica?", "8", "El exponente es la cantidad de cifras menos 1."),
    ],
    cha=[
        ex("Escribe 2.340.000.000 en notación científica.", "2,34 × 10⁹", "Tiene 10 cifras: exponente 9."),
        ex("¿Cuál es mayor, 5 × 10⁴ o 4,9 × 10⁵?", "4,9 × 10⁵", "Valen 50.000 y 490.000."),
    ],
    ctx=[ex("Una pila de ejemplo de papel tiene 7.200.000 hojas. Escribe esa cantidad en notación científica.", "7,2 × 10⁶", "Tiene 7 cifras: exponente 6.")],
    sc=[
        ex("Escribe 9.000 en notación científica.", "9 × 10³", "Tiene tres ceros."),
        ex("Escribe 1,5 × 10⁴ como número.", "15.000", "Se corre la coma 4 lugares."),
        ex("Escribe 380.000 en notación científica.", "3,8 × 10⁵", "Tiene 6 cifras: exponente 5."),
    ],
    op=task(
        "Convierte a notación científica estos datos de ejemplo: una ciudad con 540.000 habitantes, un recorrido de 1.200.000 m y una biblioteca con 8.000 libros. Luego convierte a número normal: 3,7 × 10⁶ y 9 × 10². Crea un error plausible (por ejemplo, un coeficiente mayor que 10) y corrígelo.",
        "540.000 = 5,4 × 10⁵. 1.200.000 = 1,2 × 10⁶. 8.000 = 8 × 10³. 3,7 × 10⁶ = 3.700.000. 9 × 10² = 900. Error: 54 × 10⁴; corrección: 5,4 × 10⁵.",
        ["convierte bien los tres datos", "convierte bien los dos números de vuelta", "crea y corrige un error"],
        ["cinco conversiones", "error corregido"],
        ["coeficiente fuera del rango 1 a 10", "contar mal los lugares de la coma"],
        "Pide que compruebe cada resultado multiplicando el coeficiente por la potencia.",
    ),
    reinforce="Escribe 6.000.000, 250.000 y 90.000 en notación científica.",
    extend="Explica por qué el exponente en notación científica es la cantidad de cifras menos 1. Usa dos ejemplos.",
)

# ------------------------------------------------------------------ OA 05 clase 5
lesson(
    OA5, 5,
    use="Aprenderé a resolver problemas con notación científica y a comparar números por su orden de magnitud. Sirve para dimensionar cantidades muy grandes sin contar ceros.",
    prior=["Sé escribir números en notación científica.", "Sé comparar números naturales."],
    explain=[
        "Para comparar dos números en notación científica, mira primero el exponente: el que tiene el exponente mayor es el número mayor. Si los exponentes son iguales, compara los coeficientes. Así, 7 × 10⁴ es menor que 3 × 10⁵ aunque 7 sea mayor que 3, porque 70.000 < 300.000. El exponente de la notación científica se llama orden de magnitud.",
        "Multiplicar por 10 sube el exponente en 1: 3 × 10⁴ × 10 = 3 × 10⁵. Multiplicar por 1.000 = 10³ sube el exponente en 3. Para saber cuántas veces mayor es un número que otro con el mismo coeficiente, resta los exponentes y escribe la potencia: 5 × 10⁶ es 100 veces mayor que 5 × 10⁴, porque 10⁶ ÷ 10⁴ = 100.",
        "Si el resultado de una operación pasa de 10, vuelve a ajustar el coeficiente. Por ejemplo, 4 × 10² por 3 × 10² da 12 × 10⁴, que en notación científica es 1,2 × 10⁵. Siempre revisa que el coeficiente esté entre 1 y 10 y que el resultado tenga sentido en el problema.",
    ],
    vocab=[("orden de magnitud", "exponente de la notación científica; indica qué tan grande es el número"), ("comparar", "decidir cuál de dos valores es mayor o menor"), ("coeficiente", "número entre 1 y 10 que multiplica la potencia de 10"), ("ajustar", "volver a escribir un número en notación científica correcta"), ("veces mayor", "cociente entre dos cantidades")],
    worked=[
        W("Comparar", "¿Cuál es mayor, 8 × 10⁴ o 2 × 10⁵?", ["Comparo los exponentes: 5 es mayor que 4.", "Compruebo: 80.000 < 200.000."], "2 × 10⁵"),
        W("Multiplicar y ajustar", "Una caja de ejemplo tiene 4 × 10² clips. ¿Cuántos clips hay en 30 cajas iguales? Escribe en notación científica.", ["4 × 10² = 400 clips por caja; 400 × 30 = 12.000.", "12.000 = 1,2 × 10⁴ en notación científica."], "1,2 × 10⁴ clips"),
    ],
    mistakes=[
        M("Decir que 2 × 10⁴ es mayor que 1 × 10⁵ porque 2 > 1.", "Se comparó solo el coeficiente.", "Primero se compara el exponente: 10⁵ > 10⁴, entonces 1 × 10⁵ es mayor."),
        M("Sumar 2 × 10³ + 3 × 10³ y obtener 5 × 10⁶.", "Se sumaron también los exponentes.", "Con la misma potencia solo se suman los coeficientes: 2 × 10³ + 3 × 10³ = 5 × 10³."),
    ],
    rec=[
        ex("Multiplica 3 × 10⁴ por 10 y escribe el resultado en notación científica.", "3 × 10⁵", "Multiplicar por 10 sube el exponente en 1."),
        ex("¿Cuál es mayor, 2 × 10⁵ o 9 × 10⁴?", "2 × 10⁵", "200.000 > 90.000."),
        ex("¿Qué orden de magnitud tiene 5,3 × 10⁷?", "7", "Es el exponente de la potencia de 10."),
    ],
    und=[
        ex("¿Cuántas veces mayor es 5 × 10⁶ que 5 × 10⁴?", "100", "10⁶ ÷ 10⁴ = 100."),
        ex("Ordena de menor a mayor: 4 × 10³, 2 × 10⁵, 9 × 10⁴.", "4 × 10³, 9 × 10⁴, 2 × 10⁵", "Valen 4.000, 90.000 y 200.000."),
        ex("Multiplica 3 × 10⁴ por 1.000 y escribe el resultado en notación científica.", "3 × 10⁷", "Multiplicar por 10³ sube el exponente en 3."),
    ],
    app=[
        ex("Un colegio de ejemplo recicla 2 × 10² kg de papel al mes. ¿Cuántos kg recicla en 10 meses? Escribe en notación científica.", "2 × 10³ kg", "200 × 10 = 2.000."),
        ex("Una caja de ejemplo tiene 5 × 10³ clips. ¿Cuántos clips hay en 20 cajas? Escribe el resultado en notación científica.", "1 × 10⁵ clips", "5.000 × 20 = 100.000 = 1 × 10⁵."),
        ex("Una sala de ejemplo registra 7,5 × 10⁴ visitas en un año. Escribe ese número con todas sus cifras.", "75.000", "7,5 × 10.000."),
    ],
    rea=[
        ex("Sofía dice que 7 × 10⁴ es mayor que 3 × 10⁵ porque 7 es mayor que 3. ¿Tiene razón?", "No", "7 × 10⁴ = 70.000 y 3 × 10⁵ = 300.000."),
        ex("Rodrigo suma 6 × 10⁵ + 6 × 10⁵ y obtiene 6 × 10¹⁰. ¿Cuál es el resultado correcto en notación científica?", "1,2 × 10⁶", "600.000 + 600.000 = 1.200.000."),
    ],
    cha=[
        ex("Un número x vale 9,9 × 10⁴. ¿Es mayor que 10⁵?", "No", "x = 99.000 y 10⁵ = 100.000."),
        ex("Cada estudiante de un colegio de ejemplo escribe 4 × 10² palabras en un trabajo, y hay 3 × 10² estudiantes. ¿Cuántas palabras escriben en total? Respóndelo en notación científica.", "1,2 × 10⁵", "400 × 300 = 120.000."),
    ],
    ctx=[ex("Una impresora de ejemplo imprime 6 × 10³ hojas por día. ¿Cuántas hojas imprime en 5 días? Escribe en notación científica.", "3 × 10⁴", "6.000 × 5 = 30.000.")],
    sc=[
        ex("¿Cuál es mayor, 9 × 10² o 1 × 10³?", "1 × 10³", "900 < 1.000."),
        ex("Multiplica 8 × 10² por 10.", "8 × 10³", "El exponente sube en 1."),
        ex("¿Cuántas veces mayor es 1 × 10⁵ que 1 × 10²?", "1.000", "10⁵ ÷ 10² = 1.000."),
    ],
    op=task(
        "Esta tabla de ejemplo muestra el número de visitas de tres sitios en un año: sitio A: 4,5 × 10⁴; sitio B: 9 × 10⁵; sitio C: 6 × 10⁴. (a) Ordénalos de menor a mayor. (b) Calcula cuántas visitas tienen entre los tres y escribe el resultado en notación científica. (c) Escribe cuántas veces mayor es B que C.",
        "(a) A (45.000) < C (60.000) < B (900.000). (b) 45.000 + 900.000 + 60.000 = 1.005.000 = 1,005 × 10⁶. (c) 900.000 ÷ 60.000 = 15 veces.",
        ["ordena comparando exponentes y coeficientes", "suma convirtiendo a números normales", "calcula correctamente cuántas veces mayor"],
        ["lista ordenada", "suma en notación científica", "cociente"],
        ["comparar solo coeficientes", "sumar exponentes"],
        "Pide que escriba los tres números sin notación científica antes de operar.",
    ),
    reinforce="Compara 5 × 10³ con 4 × 10⁴, y calcula 2 × 10⁴ × 100. Escribe cada respuesta en notación científica.",
    extend="Inventa un problema donde el resultado sea 2,4 × 10⁶ y resuélvelo mostrando los pasos.",
)
