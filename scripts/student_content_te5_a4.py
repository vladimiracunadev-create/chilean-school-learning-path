"""Cuaderno del estudiante, 5.º básico Tecnología: OA 05 (presentaciones y hojas de cálculo), clases 2 a 5, y OA 06 (procesador de textos), clases 1 a 5.

Las pantallas se describen con texto y son EJEMPLOS FICTICIOS: cada programa real se ve distinto y aquí no se nombra ninguna marca.
Todas las clases tienen alternativa en papel. No se usan datos personales. Los atajos de teclado no se enseñan como obligatorios.
Simplificación declarada: no se verifica el manejo de un programa real; se enseñan conceptos y lectura de resultados. De las hojas de cálculo solo
se usan tablas de doble entrada, celdas con nombre (B3), sumas simples y gráficos de barras y de líneas con datos enteros.
"""
from __future__ import annotations

from student_content_te5_a import reg
from student_lessons import arith

OA5 = "TE05 OA 05"
OA6 = "TE05 OA 06"

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja y lápiz. Los ejemplos de diapositivas están descritos en este cuaderno; si quieres practicar, usa un programa de presentaciones o una hoja de papel por diapositiva.",
    use="Aprenderé a armar diapositivas legibles con texto, imágenes y diagramas. Sirve para que la audiencia entienda tu mensaje a primera vista.",
    prior=["Sé planificar una presentación con un guion.", "Sé que cada diapositiva lleva una idea.", "Sé anotar la fuente de una información."],
    explain=[
        "Una diapositiva se lee en pocos segundos. Por eso lleva un título corto, que dice la idea, y pocas líneas de texto, no más de cinco. El texto debe tener letra grande, de al menos 24 puntos, y buen contraste: letra oscura sobre fondo claro, o al revés. Un texto largo se pasa a la voz de quien presenta, no a la diapositiva.",
        "Las imágenes muestran lo que el texto no alcanza a decir. Una imagen sirve si se relaciona con la idea de la diapositiva y se ve nítida. Se ubica sin tapar el texto. Si no es tuya, anota la fuente en la diapositiva de fuentes y usa solo imágenes que tengas permiso de usar. Una imagen decorativa sin relación distrae a la audiencia.",
        "Un diagrama organiza información con formas y flechas. El diagrama de flujo muestra pasos en orden. El diagrama de ciclo muestra algo que se repite, como las estaciones del año. El mapa de ideas muestra un tema central con sus partes. Elegir el diagrama correcto depende de cómo se relacionan las ideas.",
    ],
    vocab=[("contraste", "diferencia clara entre el color de la letra y el del fondo"), ("legible", "que se puede leer con facilidad"), ("diagrama de flujo", "diagrama con pasos en orden y flechas"), ("diagrama de ciclo", "diagrama de algo que se repite"), ("mapa de ideas", "diagrama con un tema central y sus partes")],
    worked=[
        ("Revisar una diapositiva", "Una diapositiva tiene 9 líneas de texto, letra de 14 puntos y letra gris clara sobre fondo blanco. ¿Qué tres problemas tiene?", ["Tiene más de 5 líneas.", "La letra es menor de 24 puntos.", "El contraste es débil."], "Mucho texto, letra pequeña y poco contraste"),
        ("Elegir el diagrama", "Quieres mostrar los pasos para reciclar una botella: separar, enjuagar, llevar al contenedor. ¿Qué diagrama sirve?", ["Los pasos van en orden.", "El diagrama de flujo muestra pasos con flechas."], "Un diagrama de flujo"),
    ],
    mistakes=[
        ("Copiar un párrafo largo en la diapositiva.", "La audiencia lee en vez de escuchar.", "Deja la idea clave y explica el resto hablando."),
        ("Poner una imagen sin relación para que se vea lindo.", "Distrae del mensaje.", "Usa solo imágenes que apoyen la idea y anota la fuente."),
    ],
    R=[
        ("¿Cuántas líneas de texto, como máximo, lleva una diapositiva de esta clase?", "Cinco", "Un texto corto se lee a primera vista."),
        ("Letra gris clara sobre fondo blanco, ¿tiene buen o mal contraste?", "Mal contraste", "Casi no se distingue."),
        ("Algo que se repite, como las estaciones, ¿se muestra con un diagrama de flujo o de ciclo?", "De ciclo", "El ciclo muestra lo que vuelve a empezar."),
    ],
    C=[
        ("¿Por qué una imagen sin relación con la idea es un problema?", "Porque distrae a la audiencia", "No apoya el mensaje."),
        ("Quieres mostrar un tema central con cuatro partes. ¿Qué diagrama sirve?", "Un mapa de ideas", "Muestra un centro y sus partes."),
        ("¿Dónde se anota la fuente de una imagen ajena?", "En la diapositiva de fuentes", "Así se reconoce su origen."),
    ],
    A=[
        arith("Una diapositiva tiene 9 líneas de texto y el máximo es 5. ¿Cuántas líneas sobran?", "9-5", "Se resta el máximo del total."),
        arith("Una letra mide 14 puntos y se necesitan 24. ¿Cuántos puntos hay que aumentar?", "24-14", "Se resta lo que tiene de lo que necesita."),
        ("Quieres mostrar que el día y la noche se repiten. ¿Diagrama de flujo, de ciclo o mapa de ideas?", "De ciclo", "Se repite sin fin."),
    ],
    Z=[
        ("Dos diapositivas explican lo mismo: una con 80 palabras y otra con un título, 3 líneas y una imagen relacionada. ¿Cuál comunica mejor y por qué?", "La segunda, porque es más fácil de leer", "Pocas líneas y una imagen apoyan la idea."),
        ("Un compañero pone una foto tomada de internet sin anotar de dónde viene. ¿Qué falta?", "La fuente y el permiso de uso", "Hay que reconocer el origen de lo ajeno."),
    ],
    D=[
        arith("Un diagrama de flujo tiene 5 pasos y cada paso se une con una flecha al siguiente. ¿Cuántas flechas necesita?", "5-1", "Entre 5 pasos hay 4 uniones."),
        ("Una diapositiva de ciclo tiene 4 etapas. ¿Cuántas flechas necesita para que el ciclo vuelva al comienzo?", "4", "Cada etapa se une con la siguiente y la última con la primera."),
    ],
    ctx=("Armas una diapositiva con tres consejos para ahorrar agua: cerrar la llave al enjabonarse, usar un vaso para lavarse los dientes y avisar si una llave gotea. Los consejos no van en orden. Escribe el título, elige el diagrama y di dónde irá la fuente de una imagen de una llave.", "Título: Ahorra agua: 3 consejos. Mapa de ideas, porque los consejos salen de un tema central y no van en orden. La fuente irá en la diapositiva de fuentes", "Título corto, diagrama adecuado y fuente."),
    sc=[
        ("¿Cuántas ideas lleva una diapositiva?", "Una", "Así se lee en pocos segundos."),
        ("¿Qué se hace con las imágenes ajenas?", "Anotar la fuente", "Se reconoce el origen."),
        ("¿Para qué sirve un diagrama de ciclo?", "Para mostrar algo que se repite", "Vuelve al comienzo."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: los pasos para ahorrar electricidad en la sala. Tema 2: las estaciones del año. Diseña una diapositiva en papel con título, hasta 5 líneas de texto, una imagen dibujada y un diagrama elegido según el tema. Anota qué diagrama elegiste y por qué.",
        "Tema 2: título: Las estaciones; diagrama de ciclo con 4 etapas; una imagen de un árbol.",
        ["título corto", "hasta cinco líneas", "diagrama adecuado al tema", "imagen relacionada"],
        ["diapositiva dibujada con explicación"],
        ["demasiado texto", "diagrama que no corresponde al tema"],
        "Pregunta: «¿cómo se relacionan las ideas: en orden, se repiten o salen de un centro?». Con eso elegirás el diagrama.",
    ),
    reinforce="Mira un afiche de tu barrio y cuenta cuántas líneas de texto tiene.",
    extend="Explica por qué el contraste de la letra importa más cuando se proyecta en una pared.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja cuadriculada y lápiz. Las tablas y los datos están escritos en este cuaderno. Si tienes computador, un programa de hoja de cálculo; si no, dibuja la tabla en papel.",
    use="Aprenderé a organizar datos en una tabla de doble entrada de una hoja de cálculo y a usar el nombre de las celdas. Sirve para ordenar resultados y hacer sumas sin errores.",
    prior=["Sé leer tablas simples.", "Sé sumar y restar.", "Sé que una investigación entrega datos."],
    explain=[
        "Una hoja de cálculo es un programa con una cuadrícula. Las columnas se nombran con letras (A, B, C) y las filas con números (1, 2, 3). Cada casillero se llama celda y su nombre une la letra de la columna y el número de la fila. La celda B3 está en la columna B, fila 3. Cada celda guarda un texto o un número.",
        "Una tabla de doble entrada muestra los datos de dos criterios a la vez. Un criterio va en las filas y otro en las columnas. Por ejemplo, los cursos van en las filas y los juegos preferidos en las columnas. Se cruzan para dar la cantidad de votos de un curso por un juego. Los encabezados son los títulos de filas y columnas; deben estar claros.",
        "La hoja de cálculo suma por ti. Una fórmula empieza con el signo igual (=). La fórmula =B2+B3 suma los valores de las celdas B2 y B3. Si cambias un número, el resultado se actualiza. Así se calculan totales por fila o por columna. Siempre conviene revisar a mano un total para comprobar que está bien.",
    ],
    vocab=[("celda", "casillero donde se cruzan una columna y una fila"), ("columna", "línea vertical de celdas, nombrada con letra"), ("fila", "línea horizontal de celdas, nombrada con número"), ("tabla de doble entrada", "tabla con dos criterios, uno en filas y otro en columnas"), ("fórmula", "cálculo que empieza con el signo =")],
    worked=[
        ("Nombrar una celda", "La tabla guarda el 9 en la columna B, fila 3. ¿Cómo se llama esa celda?", ["La columna es B.", "La fila es 3."], "B3"),
        ("Leer una tabla de doble entrada", "Fila 2: 5.º A, con B2 = 8 (fútbol), C2 = 5 (cuerdas) y D2 = 7 (elástico). ¿Cuántos votos de 5.º A tiene la cuerda?", ["Busco la fila de 5.º A.", "La cuerda está en la columna C: C2 = 5."], "5 votos"),
    ],
    mistakes=[
        ("Llamar a una celda con el número primero, como «3B».", "El nombre lleva primero la letra de la columna.", "Escríbelo como B3."),
        ("Confiar en un total sin revisarlo.", "Un número mal escrito da un total equivocado.", "Revisa a mano al menos un total."),
    ],
    R=[
        ("Una celda está en la columna C, fila 4. ¿Cómo se llama?", "C4", "Primero la letra y luego el número."),
        ("¿Las filas se nombran con letras o con números?", "Con números", "Las columnas usan letras."),
        ("¿Con qué signo empieza una fórmula?", "Con el signo =", "El igual indica un cálculo."),
    ],
    C=[
        ("En una tabla de doble entrada, ¿cuántos criterios se muestran a la vez?", "Dos", "Uno en las filas y otro en las columnas."),
        ("¿Qué hace la fórmula =B2+B3?", "Suma los valores de B2 y B3", "El signo + junta las dos celdas."),
        ("Si cambias un número de una celda, ¿qué pasa con el total que la usa?", "Se actualiza", "La hoja recalcula las fórmulas."),
    ],
    A=[
        ("Tabla: B2 = 8, C2 = 5, D2 = 7 (5.º A); B3 = 9, C3 = 6, D3 = 4 (5.º B), con columnas fútbol, cuerdas y elástico. ¿Cuántos votos tiene el elástico en 5.º B? Responde con la celda y el número.", "D3 = 4", "El elástico está en la columna D y 5.º B en la fila 3."),
        arith("Tabla: B2 = 8, C2 = 5, D2 = 7 son los votos de 5.º A. ¿Cuánto suma la fórmula =B2+C2+D2?", "8+5+7", "Se suman las tres celdas."),
        arith("Tabla: B2 = 8 de 5.º A y B3 = 9 de 5.º B votaron fútbol. ¿Cuánto suma la fórmula =B2+B3?", "8+9", "Se suman los votos de fútbol de ambos cursos."),
    ],
    Z=[
        ("Ana escribió el total de 5.º B (B3 = 9, C3 = 6, D3 = 4) como 18. ¿Qué debe hacer?", "Revisarlo a mano; la suma correcta es 19", "9 más 6 más 4 es 19."),
        ("Dos estudiantes llenan una tabla de doble entrada. Una pone cursos en las filas y juegos en las columnas; el otro pone todo en una sola columna. ¿Cuál es una tabla de doble entrada?", "La primera", "La doble entrada cruza dos criterios."),
    ],
    D=[
        arith("En la tabla, fútbol tiene B2 = 8 y B3 = 9; cuerdas, C2 = 5 y C3 = 6. ¿Cuántos votos suman fútbol y cuerdas entre los dos cursos?", "8+9+5+6", "Se suman los cuatro valores."),
        arith("En una tabla, un curso tiene 7 votos de elástico (D2) y el otro 4 (D3). ¿Cuántos votos más tiene el primero?", "7-4", "Se resta el menor del mayor."),
    ],
    ctx=("Anotas los juegos preferidos del recreo. 5.º A: fútbol 8, cuerdas 5, elástico 7. 5.º B: fútbol 9, cuerdas 6, elástico 4. Escribe la tabla de doble entrada con encabezados, la celda donde está el 6 y el total de 5.º A.", "Filas: 5.º A y 5.º B. Columnas: fútbol, cuerdas y elástico. El 6 está en C3. Total de 5.º A: 20", "Tabla clara, celda correcta y suma."),
    sc=[
        ("¿Cómo se nombra una celda?", "Letra de la columna y número de la fila", "Por ejemplo B3."),
        ("¿Para qué sirve el signo = al comienzo?", "Para indicar una fórmula", "La hoja calcula."),
        ("¿Qué se hace con los totales?", "Revisarlos a mano", "Así se evitan errores."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: 5.º A: leen 9 libros de cuentos, 7 de ciencia, 4 de historia; 5.º B: 6, 8, 5. Caso 2: 5.º A: 12 estudiantes van a pie, 8 en bus, 4 en auto; 5.º B: 10, 11, 3. Dibuja la tabla de doble entrada con encabezados, escribe el nombre de la celda de un dato, y calcula los totales de cada fila con una fórmula.",
        "Caso 2: filas 5.º A y 5.º B; columnas pie, bus y auto. B2 = 12. Total de 5.º A: =B2+C2+D2 = 24.",
        ["tabla con filas y columnas rotuladas", "nombra bien una celda", "escribe la fórmula de suma", "el total es correcto"],
        ["tabla con celdas, fórmula y totales"],
        ["nombrar mal la celda", "no revisar el total"],
        "Pregunta: «¿qué celda cruza este curso con este dato?». Si se confunde, pídele ubicarla con el dedo.",
    ),
    reinforce="Dibuja una tabla de 3 por 3 y nombra todas las celdas con letra y número.",
    extend="Explica por qué una tabla de doble entrada ordena mejor que una lista larga.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja cuadriculada y lápiz. Los datos están escritos en este cuaderno.",
    use="Aprenderé a convertir una tabla en un gráfico de barras con título, ejes y escala. Sirve para comparar cantidades de un vistazo.",
    prior=["Sé leer una tabla de doble entrada.", "Sé nombrar celdas.", "Sé sumar y restar."],
    explain=[
        "Un gráfico de barras compara cantidades de categorías. Cada categoría tiene una barra. Mientras más alta la barra, mayor la cantidad. Se usa cuando se quieren comparar valores, por ejemplo cuántos votos tiene cada juego. Un buen gráfico tiene título, nombre de cada eje, escala y barras del mismo ancho con un espacio igual entre ellas.",
        "El eje horizontal muestra las categorías. El eje vertical muestra la cantidad y lleva una escala, que son los números de las marcas. Si cada cuadro de la hoja vale 2 votos, una barra de 8 votos mide 4 cuadros. La escala empieza en 0 y sube de a pasos iguales. Si no empieza en 0, las diferencias se ven más grandes de lo que son.",
        "En una hoja de cálculo se selecciona la tabla y se elige el gráfico de barras. El programa lo dibuja, pero tú revisas el título, los ejes y las etiquetas. Un gráfico se lee de abajo hacia arriba: busca la barra, sigue su altura hasta el eje y lee el valor. Ordenar las barras de mayor a menor ayuda a comparar.",
    ],
    vocab=[("gráfico de barras", "gráfico que compara cantidades con barras"), ("eje", "línea del gráfico que muestra categorías o cantidades"), ("escala", "números de las marcas del eje"), ("título", "frase que dice de qué trata el gráfico"), ("categoría", "grupo que se compara")],
    worked=[
        ("Calcular la altura de una barra", "Cada cuadro vale 2 votos. ¿Cuántos cuadros mide la barra de 8 votos?", ["Cada cuadro son 2 votos.", "Divido 8 entre 2."], "4 cuadros"),
        ("Leer un gráfico", "En un gráfico de votos, la barra de cuerdas llega a la marca 6 y la de elástico a la marca 10. ¿Cuántos votos más tiene el elástico?", ["Cuerdas: 6. Elástico: 10.", "Resto 10 − 6."], "4 votos más"),
    ],
    mistakes=[
        ("Empezar la escala en un número mayor que 0.", "Las diferencias parecen más grandes de lo que son.", "Empieza la escala en 0."),
        ("Olvidar el título y los nombres de los ejes.", "Nadie sabe qué muestra el gráfico.", "Escribe el título y rotula los ejes."),
    ],
    R=[
        ("¿Qué muestra el eje horizontal de este gráfico: las categorías o la cantidad?", "Las categorías", "El eje vertical muestra la cantidad."),
        ("Una barra más alta, ¿es mayor o menor cantidad?", "Mayor cantidad", "La altura representa la cantidad."),
        ("¿Dónde empieza una escala bien hecha?", "En 0", "Así no se exageran las diferencias."),
    ],
    C=[
        ("¿Para qué se usa un gráfico de barras?", "Para comparar cantidades de categorías", "Cada barra es una categoría."),
        ("¿Por qué ayuda ordenar las barras de mayor a menor?", "Porque se compara más fácil", "La altura baja de forma ordenada."),
        ("Si la escala no empieza en 0, ¿qué pasa con las diferencias?", "Parecen más grandes de lo que son", "Se exagera la diferencia entre barras."),
    ],
    A=[
        arith("Cada cuadro vale 2 votos. ¿Cuántos cuadros mide una barra de 14 votos?", "14//2", "Se divide entre el valor de cada cuadro."),
        arith("La barra de fútbol mide 9 cuadros y cada cuadro vale 2 votos. ¿Cuántos votos tiene fútbol?", "9*2", "Se multiplican los cuadros por su valor."),
        ("Votos: fútbol 17, cuerdas 11, elástico 11. ¿Qué categoría tiene la barra más alta?", "Fútbol", "17 es el valor mayor."),
    ],
    Z=[
        ("Dos gráficos muestran 9 y 11 votos. En uno la escala empieza en 0 y en el otro empieza en 8. ¿Cuál exagera la diferencia?", "El que empieza en 8", "La barra de 9 queda muy baja y la de 11 muy alta."),
        ("Un gráfico no tiene título ni nombres de ejes. ¿Qué se puede decir de él?", "No se entiende qué muestra", "Faltan los rótulos que explican los datos."),
    ],
    D=[
        arith("Votos de tres juegos: 17, 11 y 11. ¿Cuántos votos hay en total?", "17+11+11", "Se suman las tres cantidades."),
        arith("La barra de fútbol llega a 17 votos y la de cuerdas a 11 votos. ¿Cuántos votos más tiene fútbol?", "17-11", "Se resta lo de cuerdas de lo de fútbol."),
    ],
    ctx=("Tienes la tabla de votos totales: fútbol 16, cuerdas 12 y elástico 10. Cada cuadro vale 2 votos. Calcula cuántos cuadros mide la barra de fútbol y escribe un título para el gráfico.", "La barra de fútbol mide 8 cuadros. Título: Juegos preferidos del recreo", "Calcula la altura y escribe un título claro."),
    sc=[
        ("¿Qué lleva un buen gráfico de barras?", "Título, ejes rotulados y escala desde 0", "Son sus partes necesarias."),
        ("¿Qué se compara con un gráfico de barras?", "Cantidades de categorías", "Cada barra es una categoría."),
        ("¿Qué mide el eje vertical?", "La cantidad", "Lleva la escala."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: botellas juntadas: lunes 12, martes 9, miércoles 15, jueves 8, viernes 11. Caso 2: libros leídos: cuentos 16, ciencia 10, historia 12, poesía 6. Dibuja en papel cuadriculado el gráfico de barras con título y nombres de ejes. Elige la escala: cada cuadro vale 2 si todos los datos son pares, y vale 1 si hay datos impares. Luego escribe dos cosas que el gráfico muestra.",
        "Caso 2: barras de 8, 5, 6 y 3 cuadros. Muestra que se leen más cuentos y menos poesía.",
        ["título", "ejes rotulados", "escala desde 0 con pasos iguales", "las barras coinciden con los datos", "dos conclusiones"],
        ["gráfico de barras con conclusiones"],
        ["escala que no empieza en 0", "olvidar rótulos"],
        "Pregunta: «¿cuántos votos vale cada cuadro y cuántos cuadros mide esta barra?». Si no coincide con el dato, pídele recalcular.",
    ),
    reinforce="Busca un gráfico de barras en un diario o revista y lee dos valores.",
    extend="Explica por qué un gráfico con la escala truncada puede engañar.",
)

# ------------------------------------------------------------------ OA 05, clase 5
reg(
    OA5, 5,
    materials="Hoja cuadriculada y lápiz. Los datos y la lista de revisión están escritos en este cuaderno.",
    use="Aprenderé a hacer un gráfico de líneas, a elegir el gráfico correcto y a revisar una presentación completa antes de mostrarla. Sirve para comunicar tus datos sin errores.",
    prior=["Sé hacer un gráfico de barras.", "Sé planificar una presentación y armar diapositivas.", "Sé leer tablas."],
    explain=[
        "Un gráfico de líneas muestra cómo cambia algo en el tiempo. Cada punto es un valor en un momento, y los puntos se unen con una línea. Si la línea sube, el valor aumenta; si baja, disminuye; si es plana, no cambia. Se usa para mostrar el crecimiento de una planta semana a semana o la temperatura a lo largo de un día.",
        "Para elegir el gráfico, mira la pregunta. Si quieres comparar categorías, como juegos, cursos o libros, usa un gráfico de barras. Si quieres ver el cambio en el tiempo, como semanas o meses, usa un gráfico de líneas. Un gráfico de líneas también lleva título, ejes rotulados y escala desde 0 con pasos iguales.",
        "Antes de presentar, revisa con una lista: ¿cada diapositiva tiene una idea?, ¿la letra es legible?, ¿los gráficos tienen título y ejes?, ¿hay fuentes?, ¿el tiempo alcanza? Ensaya con una persona de tu casa y anota qué no entendió. Mejora la diapositiva que causó confusión. Presentar es también escuchar preguntas e intercambiar ideas.",
    ],
    vocab=[("gráfico de líneas", "gráfico que muestra cambios en el tiempo"), ("tendencia", "forma en que sube, baja o se mantiene un valor"), ("lista de revisión", "lista de puntos para comprobar antes de presentar"), ("ensayo", "práctica de la presentación antes de mostrarla"), ("intercambiar ideas", "escuchar y responder a las demás personas")],
    worked=[
        ("Leer un gráfico de líneas", "Una planta midió 3 cm la semana 1, 5 cm la 2, 8 cm la 3 y 12 cm la 4. ¿Entre qué semanas creció más?", ["Cambios: 2, 3 y 4 cm.", "El mayor es 4 cm, entre la semana 3 y la 4."], "Entre las semanas 3 y 4"),
        ("Elegir el gráfico", "Quieres mostrar cuántos libros leyó cada curso. ¿Barras o líneas?", ["Los cursos son categorías, no tiempo.", "Para comparar categorías se usan barras."], "Gráfico de barras"),
    ],
    mistakes=[
        ("Usar un gráfico de líneas para comparar cursos.", "La línea sugiere un orden en el tiempo que no existe.", "Para categorías usa barras."),
        ("Presentar sin ensayar.", "No se descubren las partes confusas.", "Ensaya con alguien y mejora lo que no entendió."),
    ],
    R=[
        ("Si la línea de un gráfico sube, ¿el valor aumenta o disminuye?", "Aumenta", "Subir indica que el valor crece."),
        ("¿Qué gráfico muestra el cambio en el tiempo: barras o líneas?", "Líneas", "La línea une puntos de distintos momentos."),
        ("¿Qué se hace antes de presentar con una persona de tu casa?", "Ensayar", "El ensayo muestra qué se entiende y qué no."),
    ],
    C=[
        ("Quieres comparar los votos de tres juegos. ¿Barras o líneas?", "Barras", "Los juegos son categorías."),
        ("Quieres mostrar cómo cambió la temperatura durante un día. ¿Barras o líneas?", "Líneas", "Muestra cambio en el tiempo."),
        ("Una línea plana en un gráfico, ¿qué significa?", "Que el valor no cambia", "Los puntos están a la misma altura."),
    ],
    A=[
        arith("La planta midió 5 cm en la semana 2 y 12 cm en la semana 4. ¿Cuántos centímetros creció entre esas semanas?", "12-5", "Se resta la medida inicial de la final."),
        arith("La planta midió 3 cm, 5 cm, 8 cm y 12 cm en cuatro semanas. ¿Cuántos centímetros creció desde la semana 1 hasta la 4?", "12-3", "Se resta la primera medida de la última."),
        ("Quieres mostrar cuánto subió el precio de un cuaderno cada mes. ¿Barras o líneas?", "Líneas", "Es un cambio mes a mes."),
    ],
    Z=[
        ("Dos grupos presentan el mismo dato de temperatura en el día. Uno con barras y otro con líneas. ¿Cuál muestra mejor la tendencia y por qué?", "El de líneas, porque une los puntos en el tiempo", "La línea muestra subida y bajada."),
        ("Un estudiante dice: «Ya revisé, no hace falta ensayar». Otro ensayó y descubrió que una diapositiva confundía. ¿Qué lección sacas?", "Que el ensayo descubre problemas que la revisión no ve", "El ensayo muestra lo que la audiencia entiende."),
    ],
    D=[
        arith("Cada semana la planta crece 1 cm más que la anterior: 2 cm, luego 3 cm, luego 4 cm. ¿Cuántos centímetros creció en total en las tres semanas?", "2+3+4", "Se suman los crecimientos."),
        arith("Tu presentación tiene 6 diapositivas y cada una dura 2 minutos. Tienes 15 minutos. ¿Cuántos minutos sobran?", "15-6*2", "Se restan los 12 minutos de presentación de los 15."),
    ],
    ctx=("Mediste una planta durante 4 semanas: 3 cm, 5 cm, 8 cm y 12 cm. Escribe qué gráfico usarías, el título, entre qué semanas creció más y la tendencia general.", "Gráfico de líneas. Título: Crecimiento de la planta por semana. Creció más entre las semanas 3 y 4 (4 cm). La tendencia sube", "Elige gráfico, título y lee los datos."),
    sc=[
        ("¿Qué gráfico muestra cambios en el tiempo?", "El de líneas", "Une puntos de distintos momentos."),
        ("¿Qué gráfico compara categorías?", "El de barras", "Cada barra es una categoría."),
        ("En Tecnología: ¿Para qué se ensaya?", "Para descubrir qué no se entiende", "Se mejora antes de mostrar."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: temperatura de un día: 8 h: 10 grados, 12 h: 18 grados, 16 h: 22 grados, 20 h: 15 grados. Caso 2: libros leídos por el curso: semana 1: 14, semana 2: 18, semana 3: 11, semana 4: 17. Dibuja un gráfico de líneas con título, ejes y escala; escribe cuándo sube y baja, y arma una lista de revisión de tres puntos para tu presentación.",
        "Caso 2: sube de la semana 1 a la 2, baja en la 3 y vuelve a subir en la 4. Revisión: una idea por diapositiva; gráfico con título; fuentes.",
        ["gráfico de líneas correcto", "título y ejes", "describe cuándo sube y baja", "lista de revisión de tres puntos"],
        ["gráfico y lista de revisión"],
        ["usar barras para tiempo", "no revisar la presentación"],
        "Pregunta: «¿el dato cambia en el tiempo o compara grupos?». Con esa respuesta decide el gráfico.",
    ),
    reinforce="Anota durante 4 días cuántos vasos de agua tomas y haz un gráfico de líneas.",
    extend="Escribe dos preguntas que te podrían hacer al presentar tu gráfico y cómo las responderías.",
)

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja y lápiz. Si tienes computador, un procesador de textos; si no, escribe a mano en una hoja y usa las instrucciones como guía.",
    use="Aprenderé a crear un documento con un propósito: escribir un texto con título, párrafos y buena ortografía. Sirve para producir cartas, afiches e informes limpios y ordenados.",
    prior=["Sé escribir oraciones y párrafos.", "Sé abrir y cerrar un programa.", "Sé que un archivo se guarda con un nombre."],
    explain=[
        "Un procesador de textos es un programa para escribir y dar forma a documentos. Todo documento nace de un propósito: una carta para contar algo, un afiche para invitar, un informe para explicar. El propósito decide el título, el tamaño y el tono. Antes de escribir, anota para qué es y quién lo leerá.",
        "Al crear un documento nuevo, aparece una página en blanco con un cursor que parpadea. El texto se escribe donde está el cursor. Al llegar al final de la línea, el texto baja solo. La tecla Enter se presiona solo cuando termina un párrafo, no en cada línea. Un documento claro tiene un título, párrafos con una idea cada uno y un cierre.",
        "El programa marca con una línea las palabras que podría tener mal escritas. Es una ayuda, no una autoridad: puede marcar nombres propios correctos y pasar por alto errores. Tú revisas la ortografía y las tildes. Cada documento se guarda con un nombre que diga su contenido. Cada programa se ve distinto; busca el equivalente en el que uses.",
    ],
    vocab=[("procesador de textos", "programa para escribir y dar forma a documentos"), ("cursor", "raya que parpadea y marca dónde se escribe"), ("párrafo", "bloque de texto que desarrolla una idea"), ("propósito", "para qué se crea el documento"), ("corrector", "ayuda del programa que marca posibles errores")],
    worked=[
        ("Decidir cuándo usar Enter", "Escribes: «Mi curso hará una feria. Será el viernes. Invitaremos a las familias.» ¿Cuándo presionas Enter?", ["Las tres oraciones desarrollan una sola idea.", "Enter solo se usa al terminar el párrafo."], "Solo al terminar el párrafo, no entre oraciones"),
        ("Plantear el documento", "Debes escribir una invitación a una feria del curso. Escribe propósito, lector y título.", ["Propósito: invitar a una feria.", "Lector: las familias del curso.", "Título corto: Feria del curso."], "Propósito: invitar. Lector: las familias. Título: Feria del curso"),
    ],
    mistakes=[
        ("Presionar Enter al final de cada línea.", "El texto queda cortado y se desordena al cambiar el tamaño.", "Presiona Enter solo al terminar un párrafo."),
        ("Aceptar todo lo que marca el corrector sin pensar.", "Puede marcar nombres propios correctos.", "Revisa tú cada marca."),
    ],
    R=[
        ("¿Cuándo se presiona Enter al escribir?", "Al terminar un párrafo", "Enter no se usa en cada línea."),
        ("La raya que parpadea y marca dónde se escribe, ¿cómo se llama?", "Cursor", "Marca la posición del texto."),
        ("Quieres explicar cómo funciona el reciclaje del colegio. ¿Qué documento sirve mejor: un informe o un afiche de invitación?", "Un informe", "Un informe explica; una invitación pide que alguien vaya."),
    ],
    C=[
        ("¿Por qué conviene saber el propósito antes de escribir?", "Porque decide el título, el tamaño y el tono", "El propósito guía las decisiones."),
        ("El corrector marca el nombre «Antofagasta» como error. ¿Qué haces?", "Reviso y dejo el nombre si está bien escrito", "El corrector puede equivocarse con nombres propios."),
        ("Un documento tiene una sola idea larga en un párrafo y otra idea distinta sin separar. ¿Qué falta?", "Separar en dos párrafos", "Un párrafo desarrolla una idea."),
    ],
    A=[
        ("Quieres invitar a todo el colegio a una feria y pegar el aviso en el patio. ¿Qué documento escribes: afiche o informe?", "Afiche", "Es un aviso corto que se pega a la vista."),
        arith("Un documento tiene 3 párrafos y cada uno tiene 4 oraciones. ¿Cuántas oraciones hay en total?", "3*4", "Se multiplican los párrafos por las oraciones de cada uno."),
        ("Un título dice «Ahorremos agua en la sala». ¿Es mejor ese título o «Texto 1»?", "Ahorremos agua en la sala", "Dice de qué trata el documento."),
    ],
    Z=[
        ("Dos estudiantes escriben una carta. Uno presiona Enter en cada línea; el otro solo al final del párrafo. Se cambia el tamaño de letra. ¿A quién se le desordena el texto?", "Al que presionó Enter en cada línea", "Las líneas cortadas no se acomodan al nuevo tamaño."),
        ("Ana cree que el corrector siempre tiene razón. ¿Qué le explicarías?", "Que puede marcar palabras correctas y no ver errores", "Debe revisarlo ella."),
    ],
    D=[
        arith("Escribes un informe de 5 párrafos y agregas 2 más. ¿Cuántos párrafos tiene ahora?", "5+2", "Se suman los párrafos nuevos."),
        ("Un afiche debe invitar a la feria del viernes. ¿Cuál es un título mejor: «Feria del viernes: ¡te esperamos!» o «Aviso»?", "Feria del viernes: ¡te esperamos!", "Dice el tema y el día."),
    ],
    ctx=("Debes escribir una carta corta a una persona de tu casa para contarle algo que aprendiste en Tecnología. Escribe el propósito, el título de la carta y cuántos párrafos tendrá.", "Propósito: contar lo que aprendí. Título: Lo que aprendí en Tecnología. Dos o tres párrafos", "Responde propósito, título y párrafos."),
    sc=[
        ("¿Qué se hace antes de escribir un documento?", "Anotar el propósito y el lector", "Guía las decisiones."),
        ("En Tecnología: ¿Para qué sirve el corrector?", "Para marcar posibles errores", "Es una ayuda, no una autoridad."),
        ("¿Qué lleva el nombre del archivo?", "El contenido del documento", "Así se encuentra después."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: una invitación a una feria del curso el viernes a las 15:00 en el patio. Documento 2: una carta para pedir más papeleros en el colegio. Escribe en una hoja o en el programa el propósito, el título, dos párrafos con una idea cada uno, y revisa la ortografía.",
        "Documento 1: propósito: invitar. Título: Feria del curso. Párrafo 1: qué es y cuándo. Párrafo 2: quiénes pueden venir.",
        ["anota propósito y lector", "título claro", "dos párrafos con una idea", "ortografía revisada"],
        ["documento escrito con título y dos párrafos"],
        ["Enter en cada línea", "título genérico"],
        "Pregunta: «¿qué idea desarrolla cada párrafo?». Si hay dos ideas juntas, pídele separarlas.",
    ),
    reinforce="Escribe una nota corta para una persona de tu casa con título y un párrafo.",
    extend="Explica por qué un afiche y un informe no se escriben igual.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja y lápiz. Las instrucciones son para cualquier procesador; si no tienes computador, practica con un texto escrito en papel y tachas.",
    use="Aprenderé a editar un documento: seleccionar, copiar, cortar, pegar, deshacer y buscar y reemplazar. Sirve para corregir y reorganizar un texto sin volver a escribirlo.",
    prior=["Sé crear un documento con título y párrafos.", "Sé que el corrector ayuda.", "Sé guardar un archivo."],
    explain=[
        "Editar es cambiar un texto ya escrito. Para cambiar algo, primero se selecciona: se marca con el cursor la parte que quieres tratar y queda resaltada. Después puedes borrarla, copiarla o cortarla. Copiar deja el texto en su lugar y hace una copia. Cortar quita el texto de su lugar y lo guarda. Pegar pone esa copia donde está el cursor.",
        "Para mover una oración se hace en orden: seleccionar, cortar, ubicar el cursor en el nuevo lugar y pegar. Si te equivocas, la opción deshacer devuelve el documento al paso anterior. Buscar y reemplazar encuentra una palabra y la cambia por otra en todo el texto; sirve cuando una palabra se repite mucho o se escribió mal varias veces.",
        "Antes de reemplazar, mira si todas las veces que aparece la palabra deben cambiar. Si reemplazas «sol» por «luna», también cambiarías «solo» por «lunao», que está mal. Revisa cada cambio y usa deshacer si algo sale mal. Edita de a poco y guarda con frecuencia, para no perder el trabajo. Los atajos de teclado pueden variar según el programa.",
    ],
    vocab=[("seleccionar", "marcar una parte del texto para trabajarla"), ("copiar", "hacer una copia sin quitar el texto"), ("cortar", "quitar el texto de su lugar y guardarlo"), ("pegar", "poner el texto copiado o cortado en el lugar del cursor"), ("deshacer", "volver al paso anterior")],
    worked=[
        ("Mover una oración", "Quieres mover la oración «Te esperamos a las 15:00.» del final al principio. Ordena los pasos.", ["Primero selecciono la oración.", "Luego la corto, ubico el cursor al principio y la pego."], "Seleccionar, cortar, ubicar el cursor y pegar"),
        ("Cuidar el reemplazo", "Quieres cambiar «niño» por «niña» en un texto con «niños» y «niño». ¿Qué problema puedes tener?", ["El reemplazo también cambiaría «niños» por «niñas».", "Antes de aceptar cada cambio debo revisar."], "Cambiaría palabras que no corresponde; hay que revisar cada cambio"),
    ],
    mistakes=[
        ("Cortar un texto y olvidar pegarlo.", "El texto queda guardado pero no aparece en el documento.", "Ubica el cursor y pega enseguida."),
        ("Reemplazar todas las palabras sin revisar.", "Puede cambiar palabras que no corresponden.", "Revisa cada cambio o usa deshacer."),
    ],
    R=[
        ("¿Qué se hace primero para cambiar una parte del texto: seleccionar o pegar?", "Seleccionar", "Hay que marcar lo que se quiere tratar."),
        ("Quitar el texto de su lugar y guardarlo, ¿es copiar o cortar?", "Cortar", "Copiar deja el texto donde está."),
        ("¿Qué opción devuelve el documento al paso anterior?", "Deshacer", "Anula el último cambio."),
    ],
    C=[
        ("¿Qué diferencia hay entre copiar y cortar?", "Copiar deja el texto y cortar lo quita", "Cortar mueve el texto."),
        ("¿Para qué sirve buscar y reemplazar?", "Para cambiar una palabra en todo el texto", "Encuentra y cambia cada vez que aparece."),
        ("Pegaste el texto en el lugar equivocado. ¿Qué haces?", "Deshacer", "Devuelve el documento al paso anterior."),
    ],
    A=[
        ("Quieres repetir un título en la última página sin borrarlo de la primera. ¿Copiar o cortar?", "Copiar", "Copiar deja el original."),
        ("Ordena: A pegar, B seleccionar, C cortar, D ubicar el cursor. ¿Cuál es el orden para mover un texto?", "B, C, D, A", "Seleccionar, cortar, ubicar y pegar."),
        arith("Una palabra aparece 12 veces y cambias 9 de ellas. ¿Cuántas quedan sin cambiar?", "12-9", "Se resta lo cambiado del total."),
    ],
    Z=[
        ("Pedro reemplazó «sol» por «luna» en todo el texto y apareció «lunao». ¿Qué error cometió?", "No revisó cada cambio", "El reemplazo cambió también partes de otras palabras."),
        ("Luisa selecciona una oración, la copia y la pega al final, y ahora aparece dos veces. ¿Qué debió usar para moverla?", "Cortar", "Cortar quita el texto de su lugar."),
    ],
    D=[
        arith("Un documento tiene 4 párrafos y copias 2 completos al final. ¿Cuántos párrafos tiene ahora?", "4+2", "Se suman los párrafos copiados."),
        arith("Copias una oración y la pegas dos veces. ¿Cuántas veces aparece la oración en total, contando la original?", "1+2", "Se suma la original y las dos copias."),
    ],
    ctx=("Tu texto dice: «La feria será el sábado. Te esperamos.» Quieres que diga «Te esperamos» primero, y cambiar «sábado» por «viernes». Escribe los pasos y el texto final.", "Selecciono «Te esperamos.», lo corto, ubico el cursor al inicio y lo pego; luego reemplazo «sábado» por «viernes». Texto final: «Te esperamos. La feria será el viernes.»", "Pasos correctos y texto final."),
    sc=[
        ("¿Qué se hace antes de copiar?", "Seleccionar", "Hay que marcar el texto."),
        ("¿Qué hace deshacer?", "Vuelve al paso anterior", "Sirve para corregir errores."),
        ("¿Por qué se revisa un reemplazo?", "Porque puede cambiar palabras que no corresponden", "Hay palabras parecidas."),
    ],
    open_task=(
        "Escoge un texto. Texto 1: «Te esperamos. La feria será el sábado.» (queda: «La feria será el sábado. Te esperamos.»). Texto 2: «Gracias por venir. Hola a todos. Hoy contamos lo que aprendimos.» (queda: «Hola a todos. Hoy contamos lo que aprendimos. Gracias por venir.»). Escribe los pasos de edición para ordenar el texto y revisa el resultado.",
        "Texto 2: selecciono «Gracias por venir.», la corto, ubico el cursor al final y la pego.",
        ["usa seleccionar, cortar y pegar en orden", "el texto final queda correcto", "revisa el resultado", "menciona deshacer si hay error"],
        ["pasos de edición y texto final"],
        ["olvidar seleccionar", "no revisar el resultado"],
        "Pregunta: «¿qué debió quedar seleccionado?». Si no sabe, repasen el primer paso.",
    ),
    reinforce="Escribe cinco oraciones en desorden en una hoja y numera el orden correcto.",
    extend="Explica cuándo usarías buscar y reemplazar y cuándo cambiarías las palabras a mano.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja y lápiz. Los ejemplos de texto están en este cuaderno; practica el formato en papel o en un programa.",
    use="Aprenderé a dar formato a un texto: letra, tamaño, énfasis, alineación, interlineado y listas. Sirve para que un documento sea claro y fácil de leer.",
    prior=["Sé crear y editar un documento.", "Sé que un título dice de qué trata el texto.", "Sé que el contraste ayuda a leer."],
    explain=[
        "Dar formato es cambiar el aspecto del texto sin cambiar lo que dice. El tipo de letra debe ser claro; el tamaño del texto normal suele ser 12 puntos y el del título es mayor, por ejemplo 18. La negrita resalta lo importante y la cursiva sirve para títulos de obras o palabras especiales. No conviene mezclar muchos tipos de letra.",
        "La alineación es cómo se acomoda el texto en la página: a la izquierda, centrado, a la derecha o justificado. El texto largo se lee mejor alineado a la izquierda. El título se suele centrar. El interlineado es el espacio entre las líneas; un espacio algo amplio hace el texto más fácil de leer. Los márgenes son el espacio en blanco en los bordes de la página.",
        "Las listas con viñetas muestran elementos que no tienen orden. Las listas numeradas muestran pasos en orden. Usa el formato con un propósito: si todo está en negrita, nada se destaca. Revisa el documento completo antes de guardarlo: debe verse ordenado, con pocos formatos y con el mismo estilo en las partes iguales.",
    ],
    vocab=[("formato", "aspecto del texto: letra, tamaño, alineación"), ("negrita", "letra más gruesa para resaltar"), ("alineación", "forma de acomodar el texto en la página"), ("interlineado", "espacio entre líneas"), ("viñeta", "marca que encabeza cada elemento de una lista")],
    worked=[
        ("Elegir el tipo de lista", "Quieres escribir los pasos para armar una caja: 1 medir, 2 cortar, 3 pegar. ¿Lista con viñetas o numerada?", ["Los pasos van en orden.", "La numerada muestra el orden."], "Lista numerada"),
        ("Corregir exceso de formato", "Un afiche tiene cada palabra en un color y tipo de letra distintos. ¿Qué problema tiene?", ["Muchos formatos distraen.", "No se destaca lo importante."], "Demasiados formatos; se pierde lo importante"),
    ],
    mistakes=[
        ("Poner todo el texto en negrita.", "Si todo está resaltado, nada se destaca.", "Usa negrita solo para lo más importante."),
        ("Usar letra de 8 puntos para que quepa más.", "Se lee con dificultad.", "Usa 12 puntos para el texto y ajusta el contenido."),
    ],
    R=[
        ("Lista con pasos en orden: ¿viñetas o numerada?", "Numerada", "El número muestra el orden."),
        ("¿Para qué sirve la negrita?", "Para resaltar lo importante", "Hace destacar una palabra."),
        ("El espacio blanco en los bordes de la página, ¿cómo se llama?", "Márgenes", "Es el espacio de los bordes."),
    ],
    C=[
        ("¿Por qué no conviene mezclar muchos tipos de letra?", "Porque distrae y desordena", "Menos formatos se leen mejor."),
        ("¿Cómo se alinea normalmente un texto largo para leerlo mejor?", "A la izquierda", "Los ojos vuelven al mismo punto."),
        ("¿Qué es el interlineado?", "El espacio entre las líneas", "Se ajusta para leer mejor."),
    ],
    A=[
        ("Quieres una lista de materiales sin orden: cartón, cinta y tijeras. ¿Viñetas o numerada?", "Con viñetas", "Los materiales no tienen orden."),
        arith("El título tiene letra de 18 puntos y el texto de 12 puntos. ¿Cuántos puntos más grande es el título?", "18-12", "Se resta el tamaño del texto del tamaño del título."),
        ("Un título de una invitación, ¿suele ir alineado a la izquierda o centrado?", "Centrado", "Así llama la atención en la parte superior."),
    ],
    Z=[
        ("Dos documentos: uno con título de 18 puntos, texto de 12 y negrita en tres palabras clave; otro con todo en negrita y 8 puntos. ¿Cuál se lee mejor y por qué?", "El primero, porque destaca lo importante", "Pocos formatos con propósito ayudan a leer."),
        ("Una lista de pasos usa viñetas. Un compañero propone numerarla. ¿Por qué tiene razón?", "Porque los pasos van en orden", "El número muestra la secuencia."),
    ],
    D=[
        arith("Un texto tiene 24 líneas con interlineado normal. Si se aumenta el espacio y cada página admite 20 líneas, ¿cuántas líneas pasan a la segunda página?", "24-20", "Se restan las que caben en la primera página."),
        ("Un texto de 12 puntos se imprime en un cartel para leer a 5 metros. ¿Conviene mantener 12 puntos?", "No, conviene una letra mucho mayor", "A distancia se necesita letra grande."),
    ],
    ctx=("Escribes una invitación con título, fecha, lugar y una lista de lo que se ofrecerá en la feria: juegos, comida y música. Elige tamaño del título, alineación, formato de la fecha y tipo de lista.", "Título de 18 puntos centrado; fecha en negrita; lista con viñetas porque no tiene orden", "Cuatro decisiones justificadas."),
    sc=[
        ("¿Qué tamaño es el habitual del texto normal?", "12 puntos", "Se lee bien."),
        ("¿Qué se hace con los pasos en orden?", "Se numeran", "El número muestra el orden."),
        ("¿Se usa negrita en todo el texto?", "No", "Solo para lo importante."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: una invitación a una feria con título, fecha, lugar y una lista de tres atracciones. Documento 2: instrucciones de 4 pasos para armar una caja de cartón. Escribe el documento y anota qué formato usas para el título, el texto, lo importante y la lista, con una razón.",
        "Documento 2: título 18 puntos centrado; texto 12; lista numerada porque son pasos en orden.",
        ["usa pocos formatos", "tamaños distintos para título y texto", "tipo de lista adecuado", "razón para cada decisión"],
        ["documento formateado con lista de decisiones"],
        ["demasiados formatos", "lista con tipo equivocado"],
        "Pregunta: «¿qué quieres destacar y qué formato usaste para eso?». Si todo está destacado, pídele elegir.",
    ),
    reinforce="Mira un afiche y anota qué formatos usa para título y texto.",
    extend="Explica por qué el formato debe ayudar a leer y no solo a decorar.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja y lápiz. Los ejemplos y las medidas están escritos en este cuaderno.",
    use="Aprenderé a incorporar elementos de diseño: imágenes, tablas, formas, columnas, encabezado y pie de página. Sirve para que un documento sea más atractivo y comunique mejor.",
    prior=["Sé dar formato a un texto.", "Sé que las imágenes ajenas llevan fuente.", "Sé leer tablas y proporciones simples."],
    explain=[
        "Los elementos de diseño ayudan a comunicar mejor, no solo a decorar. Una imagen explica algo que el texto no dice y debe relacionarse con él. Al cambiarle el tamaño, se hace desde una esquina para mantener la proporción; si se estira de un lado, se deforma. Se acompaña con un pie de imagen, que es una frase corta debajo que explica qué muestra, y con la fuente.",
        "Una tabla ordena datos en filas y columnas dentro del documento. Las formas, como cuadros y flechas, ayudan a hacer diagramas. Las columnas dividen el texto en dos o más franjas, como en un diario. El encabezado es el texto que se repite arriba de cada página y el pie de página, el que se repite abajo. Allí van el título del documento y el número de página.",
        "También se decide cómo se acomoda el texto alrededor de una imagen: puede quedar arriba y abajo, o rodearla. Deja espacio en blanco para que no se vea apretado. Alinea imágenes y títulos con los márgenes. Si usas una imagen ajena, anota la fuente y usa solo la que tienes permiso de usar. Revisa que cada elemento tenga un propósito.",
    ],
    vocab=[("proporción", "relación entre el ancho y el alto de una imagen"), ("pie de imagen", "frase corta debajo de la imagen que explica qué muestra"), ("encabezado", "texto que se repite arriba de cada página"), ("pie de página", "texto que se repite abajo de cada página"), ("columna", "franja vertical en que se divide el texto")],
    worked=[
        ("Mantener la proporción", "Una imagen mide 12 cm de ancho y 8 cm de alto. La reduces a 6 cm de ancho manteniendo la proporción. ¿Cuánto mide de alto?", ["Pasa de 12 a 6: es la mitad.", "El alto también queda a la mitad: 8 dividido en 2."], "4 cm"),
        ("Elegir el elemento", "Quieres mostrar los materiales con sus cantidades de forma ordenada. ¿Usas una tabla o una forma de flecha?", ["Son datos en dos grupos: material y cantidad.", "Una tabla ordena datos en filas y columnas."], "Una tabla"),
    ],
    mistakes=[
        ("Estirar una imagen de un solo lado para que quepa.", "Se deforma y se ve mal.", "Cambia el tamaño desde una esquina para mantener la proporción."),
        ("Poner una imagen sin pie y sin fuente.", "No se sabe qué muestra ni de dónde viene.", "Escribe un pie de imagen y anota la fuente."),
    ],
    R=[
        ("Una imagen estirada de un solo lado, ¿se deforma?", "Sí", "Cambia su proporción."),
        ("El texto que se repite arriba de cada página, ¿es encabezado o pie de página?", "Encabezado", "Está en la parte superior."),
        ("Una frase corta debajo de la imagen que explica qué muestra, ¿cómo se llama?", "Pie de imagen", "Describe la imagen."),
    ],
    C=[
        ("¿Por qué una imagen debe relacionarse con el texto?", "Porque debe ayudar a comunicar", "Una imagen sin relación distrae."),
        ("¿Para qué sirve una tabla en un documento?", "Para ordenar datos en filas y columnas", "Hace fácil comparar datos."),
        ("¿Dónde suele ir el número de página?", "En el encabezado o en el pie de página", "Se repite en cada página."),
    ],
    A=[
        arith("Una imagen mide 12 cm de ancho y 8 cm de alto. Si el ancho pasa a 6 cm manteniendo la proporción, ¿cuántos cm de alto mide?", "8//2", "El alto queda a la mitad."),
        arith("Una imagen de 10 cm de ancho y 6 cm de alto se amplía al doble manteniendo la proporción. ¿Cuántos cm de ancho mide ahora?", "10*2", "El ancho se duplica."),
        ("Quieres que el título del documento aparezca arriba en todas las páginas. ¿Dónde lo pones?", "En el encabezado", "El encabezado se repite arriba."),
    ],
    Z=[
        ("Dos estudiantes reducen la misma imagen. Una la reduce desde una esquina y la otra solo de un lado. ¿Cuál se deforma?", "La que la redujo de un lado", "Cambió solo una medida."),
        ("Un documento usa una imagen decorativa que no tiene relación con el texto. ¿Qué problema tiene?", "Distrae al lector", "Debe apoyar el mensaje."),
    ],
    D=[
        arith("Un texto con 3 columnas iguales tiene 90 palabras en total. ¿Cuántas palabras hay en cada columna?", "90//3", "Se divide el total entre las columnas."),
        arith("Una página mide 21 cm de ancho y tiene un margen de 2 cm a cada lado. ¿Cuántos cm de ancho quedan para el texto y las imágenes?", "21-2-2", "Se restan los márgenes de ambos lados."),
    ],
    ctx=("Haces un informe con una foto de una planta de 12 cm por 8 cm. Quieres que mida 6 cm de ancho, ponerle un pie de imagen y que el título del informe aparezca en todas las páginas. Escribe el alto nuevo, el pie y dónde irá el título.", "Alto: 4 cm. Pie: «Planta de la sala en la semana 3». Título en el encabezado", "Cálculo, pie y ubicación."),
    sc=[
        ("¿Cómo se cambia el tamaño de una imagen sin deformarla?", "Desde una esquina", "Mantiene la proporción."),
        ("¿Qué lleva una imagen ajena?", "Pie de imagen y fuente", "Dice qué muestra y de dónde viene."),
        ("¿Qué hace un pie de página?", "Se repite abajo en cada página", "Allí va, por ejemplo, el número de página."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: una invitación con una imagen de 12 cm por 8 cm, que quieres reducir a 6 cm de ancho, con pie de imagen. Documento 2: un informe de 3 páginas con título repetido arriba y número de página abajo, y una tabla de materiales. Describe qué elementos usas, su tamaño y dónde van, y por qué.",
        "Documento 2: título en el encabezado, número en el pie, tabla de 3 filas con material y cantidad.",
        ["usa elementos con propósito", "calcula bien el tamaño", "incluye pie y fuente de imagen", "ubica encabezado y pie correctamente"],
        ["descripción del diseño del documento"],
        ["imagen deformada", "elementos sin propósito"],
        "Pregunta: «¿qué aporta este elemento al mensaje?». Si no aporta, pídele sacarlo.",
    ),
    reinforce="Mira un diario o revista y señala su encabezado, sus columnas y el pie de una imagen.",
    extend="Explica por qué demasiados elementos de diseño pueden empeorar un documento.",
)

# ------------------------------------------------------------------ OA 06, clase 5
reg(
    OA6, 5,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno; si tienes computador, practica con un documento tuyo.",
    use="Aprenderé a guardar un documento con un buen nombre y formato, a revisarlo con una lista de cotejo y a cuidar mis archivos. Sirve para no perder el trabajo y para compartirlo bien.",
    prior=["Sé crear, editar y dar formato a un documento.", "Sé agregar imágenes, tablas y encabezados.", "Sé que los archivos se guardan en carpetas."],
    explain=[
        "Guardar un documento es grabarlo para poder abrirlo después. La primera vez se elige un nombre y una carpeta. «Guardar» actualiza el mismo archivo con los cambios. «Guardar como» crea un archivo nuevo con otro nombre o formato, útil para hacer una versión. Conviene guardar cada pocos minutos, porque un corte de luz puede hacer perder lo escrito.",
        "El nombre del archivo debe decir su contenido y la versión: afiche_feria_v2. Evita tildes, espacios y signos raros, porque a veces no se leen bien en otros equipos. Usa una carpeta ordenada, como «tecnologia/feria». El formato editable permite seguir cambiando el documento. El formato PDF sirve para compartir un documento que no debe cambiar, y se ve igual en cualquier equipo.",
        "Antes de compartir, revisa el documento con una lista de cotejo: ¿tiene título?, ¿la ortografía está revisada?, ¿el formato es parejo?, ¿las imágenes tienen fuente?, ¿el nombre del archivo es claro? Mira la vista previa para ver cómo quedará impreso. Haz una copia de seguridad en otro lugar, porque un archivo guardado en un solo sitio se puede perder.",
    ],
    vocab=[("guardar", "grabar el archivo con los cambios"), ("guardar como", "crear un archivo nuevo con otro nombre o formato"), ("versión", "estado del documento en un momento"), ("PDF", "formato para compartir un documento sin que cambie"), ("copia de seguridad", "copia guardada en otro lugar por precaución")],
    worked=[
        ("Elegir el nombre", "Tienes la segunda versión de un afiche de la feria. ¿Qué nombre es mejor: «nuevo2» o «afiche_feria_v2»?", ["El primero no dice el contenido.", "El segundo dice qué es y la versión."], "afiche_feria_v2"),
        ("Elegir el formato", "Quieres enviar la invitación a las familias sin que nadie cambie su texto. ¿Formato editable o PDF?", ["Se necesita que no cambie.", "El PDF mantiene el documento igual."], "PDF"),
    ],
    mistakes=[
        ("Guardar solo al final de todo el trabajo.", "Un corte de luz puede hacer perder todo.", "Guarda cada pocos minutos."),
        ("Guardar el archivo con el nombre «nuevo» o «documento1».", "No se sabe qué contiene.", "Usa un nombre que diga el contenido y la versión."),
    ],
    R=[
        ("¿Cada cuánto conviene guardar un documento?", "Cada pocos minutos", "Así se evita perder el trabajo."),
        ("Para compartir un documento que no debe cambiar, ¿formato editable o PDF?", "PDF", "Se ve igual y no se modifica fácilmente."),
        ("¿Qué es una copia de seguridad?", "Una copia guardada en otro lugar", "Protege contra pérdidas."),
    ],
    C=[
        ("¿Qué hace «guardar como»?", "Crea un archivo nuevo con otro nombre o formato", "Permite tener varias versiones."),
        ("¿Por qué evitar tildes y espacios en el nombre del archivo?", "Porque a veces no se leen bien en otros equipos", "Pueden aparecer como signos raros."),
        ("¿Para qué sirve la vista previa?", "Para ver cómo quedará el documento impreso", "Permite detectar errores antes."),
    ],
    A=[
        ("¿Cuál es el mejor nombre para la tercera versión de un informe de ciencias? A «informe», B «informe_ciencias_v3».", "B", "B dice el contenido y la versión."),
        arith("Guardas cada 5 minutos durante una hora de trabajo (60 minutos). ¿Cuántas veces guardas?", "60//5", "Se divide el tiempo entre el intervalo."),
        ("Quieres seguir cambiando el documento mañana. ¿Lo guardas en formato editable o solo en PDF?", "En formato editable", "El PDF no se edita con facilidad."),
    ],
    Z=[
        ("A dos estudiantes se les corta la luz. Una había guardado hace 5 minutos y el otro hace 1 hora. ¿Cuál pierde menos trabajo?", "La que guardó hace 5 minutos", "Perdió solo los últimos 5 minutos."),
        ("Un documento está en un solo pendrive y se pierde. ¿Qué precaución faltó?", "Una copia de seguridad en otro lugar", "Toda información importante debe tener copia."),
    ],
    D=[
        arith("Tienes 3 versiones de un afiche y guardas 2 versiones más. ¿Cuántos archivos hay?", "3+2", "Se suman los archivos nuevos."),
        ("La lista de cotejo tiene 6 puntos y el documento cumple 5. ¿Está listo para compartir?", "No, falta corregir el punto que no cumple", "Debe cumplir todos antes de compartirse."),
    ],
    ctx=("Terminaste una invitación. Debes guardarla para editar mañana, enviar una copia que no cambie y hacer una copia de seguridad. Escribe el nombre del archivo, el formato de cada copia y dónde guardas la copia de seguridad.", "Nombre: invitacion_feria_v1. Editable para mañana; PDF para enviar. Copia de seguridad en otro lugar distinto", "Nombre, formatos y copia de seguridad."),
    sc=[
        ("¿Qué debe decir el nombre del archivo?", "El contenido y la versión", "Se encuentra fácil."),
        ("¿Para qué sirve el formato PDF?", "Para compartir un documento que no cambie", "Se ve igual en cualquier equipo."),
        ("¿Dónde se guarda la copia de seguridad?", "En otro lugar distinto", "Así no se pierde con el original."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: terminaste una invitación a la feria y la debes enviar a las familias sin que cambie. Caso 2: terminaste un informe de ciencias y lo seguirás editando mañana. Escribe el nombre del archivo, el formato elegido, la carpeta y la copia de seguridad, y completa una lista de cotejo de 5 puntos.",
        "Caso 1: invitacion_feria_v1; PDF; carpeta Tecnologia/Feria; copia en otro lugar. Lista: título, ortografía, formato parejo, fuentes y nombre claro.",
        ["nombre claro con versión", "formato adecuado", "carpeta ordenada", "copia de seguridad", "lista de cotejo de cinco puntos"],
        ["plan de guardado y lista de cotejo"],
        ["nombres sin significado", "olvidar la copia de seguridad"],
        "Pregunta: «¿cómo encontrarías este archivo en un mes?». Si no sabe, pídele mejorar el nombre y la carpeta.",
    ),
    reinforce="Escribe en una hoja la lista de cotejo de cinco puntos para revisar tus documentos.",
    extend="Explica por qué guardar versiones permite volver atrás si algo sale mal.",
)
