"""Cuaderno del estudiante, 6.º básico Tecnología: OA 05 (software para organizar y comunicar resultados), clases 1 a 6.

Clase 1 estructura de una presentación, 2 diseño de diapositivas con imágenes y diagramas, 3 hoja de cálculo y tablas de doble entrada,
4 gráficos de barra simple y doble, 5 gráficos circulares y de línea, 6 comunicar los resultados de una investigación.
Simplificación declarada: no se verifica el manejo de un programa real (cada programa se ve distinto); se enseñan conceptos, elección del recurso
y lectura de resultados. Todas las actividades tienen alternativa en papel. Datos ficticios, sin datos personales ni marcas.
"""
from __future__ import annotations

from student_content_te6_a import reg
from student_lessons import arith

OA5 = "TE06 OA 05"

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja y lápiz. Si tienes computador, un programa de presentación; si no, hojas dobladas como diapositivas.",
    use="Aprenderé a organizar los resultados de una investigación en una presentación con diapositivas. Sirve para comunicar ideas de forma ordenada y clara.",
    prior=["Sé qué es un título y una idea principal.", "Sé que una fuente es el origen de un dato.", "Sé ordenar información en una secuencia."],
    explain=[
        "Un programa de presentación permite mostrar imágenes, diagramas y textos en diapositivas, que son páginas que se proyectan una tras otra. Se usa para comunicar los resultados de una investigación o para intercambiar ideas con un propósito: informar, explicar, proponer o pedir opiniones.",
        "Una presentación se organiza en partes: una diapositiva de portada con el título y los autores, una de introducción con la pregunta de la investigación, varias de resultados, una de conclusión y una de fuentes. Cada diapositiva tiene una sola idea principal, que se escribe en el título y se apoya con una imagen, un diagrama o una lista corta.",
        "Antes de abrir el programa, planifica en papel: escribe la pregunta, los datos y la conclusión y decide cuántas diapositivas necesitas. Un buen orden es: de lo general a lo particular. Al final, revisa que cada diapositiva responda a la pregunta y que los datos sean verdaderos y tengan fuente.",
    ],
    vocab=[("diapositiva", "página de una presentación que se proyecta"), ("idea principal", "lo más importante que dice una diapositiva"), ("portada", "primera diapositiva con título y autores"), ("conclusión", "respuesta final a la pregunta de la investigación"), ("propósito", "para qué se comunica algo")],
    worked=[
        ("Ordenar las diapositivas", "Ordena: conclusión, portada, resultados, fuentes, introducción.", ["La portada es primero y la introducción presenta la pregunta.", "Luego los resultados, la conclusión y al final las fuentes."], "Portada, introducción, resultados, conclusión y fuentes"),
        ("Una idea por diapositiva", "Una diapositiva dice: «El reciclaje, la basura, el agua y la energía». ¿Qué problema tiene y cómo se arregla?", ["Mezcla cuatro ideas en una sola diapositiva.", "Se separa en una diapositiva por idea."], "Mezcla varias ideas; se separa una idea por diapositiva"),
    ],
    mistakes=[
        ("Poner mucho texto en una diapositiva.", "Nadie alcanza a leerlo.", "Usa una idea principal y pocas palabras."),
        ("Empezar a hacer diapositivas sin planificar.", "Se desordenan las ideas.", "Planifica en papel: pregunta, datos y conclusión."),
    ],
    R=[
        ("¿Qué diapositiva va primero en una presentación?", "La portada", "Presenta el título y los autores."),
        ("¿Cuántas ideas principales lleva cada diapositiva?", "Una", "Así es clara."),
        ("¿Qué diapositiva responde la pregunta de la investigación?", "La conclusión", "Resume la respuesta."),
    ],
    C=[
        ("¿Para qué se planifica en papel antes de abrir el programa?", "Para ordenar las ideas y decidir cuántas diapositivas hacer", "Así las ideas no se desordenan."),
        ("¿Qué propósito tiene presentar los resultados de una encuesta a tu curso?", "Informar los resultados", "Se comunica lo encontrado."),
        ("¿Dónde se escribe la idea principal de la diapositiva?", "En el título", "Así se entiende rápido."),
    ],
    A=[
        ("Ordena estas diapositivas de una investigación sobre el uso de agua: fuentes, resultados con datos, portada, pregunta de investigación, conclusión.", "Portada, pregunta de investigación, resultados con datos, conclusión y fuentes", "Sigue el orden general a particular."),
        arith("Una presentación tiene 1 portada, 1 introducción, 5 diapositivas de resultados, 1 conclusión y 1 de fuentes. ¿Cuántas diapositivas tiene?", "1+1+5+1+1", "Se suman todas las partes.", " diapositivas"),
        ("Una diapositiva tiene 3 gráficos, 8 líneas de texto y 2 ideas distintas. ¿Qué conviene hacer? A dividirla en dos diapositivas, B agregar más texto.", "A", "Hay dos ideas; cada una va en su diapositiva."),
    ],
    Z=[
        ("Dos equipos presentan la misma encuesta. El equipo A muestra una diapositiva con todo el texto; el equipo B muestra una idea por diapositiva con un gráfico. ¿Cuál comunica mejor y por qué?", "El equipo B, porque es más claro", "Una idea por diapositiva facilita entender."),
        ("Un equipo no pone fuentes porque «los datos son verdaderos». ¿Qué falta?", "Indicar de dónde salen los datos", "Las fuentes permiten comprobar."),
    ],
    D=[
        arith("Una presentación de 12 minutos dedica 1 minuto a cada diapositiva. Si tiene portada, introducción, conclusión y fuentes, ¿cuántas diapositivas de resultados cabe?", "12-4", "Se restan las 4 diapositivas fijas del total.", " diapositivas"),
        ("La pregunta es «¿Cuántos libros leyó el curso en 4 meses?». ¿Qué debe mostrar la conclusión? A un chiste, B la respuesta con el dato.", "B", "La conclusión responde la pregunta."),
    ],
    ctx=("Tu curso encuestó a 30 estudiantes sobre qué hacen en el recreo. Resultados: 12 juegan fútbol, 10 conversan y 8 leen. Planifica 5 diapositivas: escribe el título de cada una y la idea principal.", "1 Portada: Qué hacemos en el recreo. 2 Pregunta: ¿Qué hace el curso en el recreo? 3 Resultados: 12 fútbol, 10 conversan, 8 leen. 4 Conclusión: el fútbol es lo más elegido. 5 Fuentes: encuesta del curso", "Se planifica con portada, pregunta, resultados, conclusión y fuentes."),
    sc=[
        ("¿Qué lleva la diapositiva de portada?", "El título y los autores", "Presenta el tema."),
        ("¿Cuántas ideas por diapositiva?", "Una", "Se entiende mejor."),
        ("¿Qué se planifica antes de usar el programa?", "La pregunta, los datos y la conclusión", "Ordena el trabajo."),
    ],
    open_task=(
        "Escoge una investigación. Investigación 1: 28 estudiantes dijeron su fruta favorita: 11 manzana, 9 plátano y 8 naranja. Investigación 2: durante 5 días se anotó cuántos vasos de agua tomó un curso: 40, 38, 45, 50 y 47. Planifica en papel una presentación de 5 diapositivas con título, idea principal y qué imagen o diagrama pondrías en cada una.",
        "Investigación 1: 1 Portada. 2 Pregunta. 3 Resultados con gráfico de barras. 4 Conclusión: la manzana es la preferida. 5 Fuentes: encuesta del curso",
        ["cinco diapositivas ordenadas", "una idea por diapositiva", "propone imagen o gráfico", "incluye fuentes"],
        ["plan escrito de cinco diapositivas"],
        ["mezclar ideas", "omitir fuentes"],
        "Pregunta: «¿cuál es la idea principal de esta diapositiva?». Si hay dos, pídele separarlas.",
    ),
    reinforce="Escribe en un papel el plan de tres diapositivas para contar a tu familia qué hiciste el fin de semana.",
    extend="Explica por qué una presentación para convencer y una para informar pueden tener el mismo orden pero distinto propósito.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja y lápiz. Los ejemplos de diapositivas están descritos con texto en este cuaderno.",
    use="Aprenderé a diseñar diapositivas legibles con texto breve, imágenes y diagramas y a citar las fuentes. Sirve para que la audiencia entienda tus resultados.",
    prior=["Sé organizar una presentación.", "Sé que las fuentes se anotan.", "Sé qué es un diagrama."],
    explain=[
        "Una diapositiva legible tiene poco texto: entre 3 y 5 líneas cortas, con letra grande que se lea desde el fondo de la sala (al menos 24 puntos, una medida del tamaño de la letra). El texto debe contrastar con el fondo: letra oscura sobre fondo claro, o al revés. Se usa un mismo tipo de letra y pocos colores.",
        "Las imágenes y los diagramas ayudan a entender. Una imagen debe tener relación con la idea, ser nítida y tener fuente. Un diagrama muestra relaciones: un diagrama de flujo muestra pasos con flechas; un diagrama de ciclo muestra pasos que se repiten, como el ciclo del agua; un esquema muestra las partes de algo.",
        "Respeta los derechos de autor: usa imágenes propias, fotografías que tomaste o imágenes con permiso de uso, y anota la fuente en la diapositiva final. Elige elementos útiles y evita los que solo adornan, como animaciones que distraen. Antes de presentar, revisa la ortografía y practica.",
    ],
    vocab=[("legible", "que se puede leer con facilidad"), ("contraste", "diferencia clara entre el color del texto y el del fondo"), ("diagrama de flujo", "esquema con pasos unidos por flechas"), ("diagrama de ciclo", "esquema de pasos que se repiten"), ("derechos de autor", "derechos de quien creó una obra")],
    worked=[
        ("Revisar la legibilidad", "Una diapositiva tiene 12 líneas de texto en letra pequeña, amarilla sobre fondo blanco. ¿Qué problemas tiene?", ["Tiene mucho texto: debería ser de 3 a 5 líneas.", "El amarillo sobre blanco no tiene contraste."], "Demasiado texto y poco contraste"),
        ("Elegir un diagrama", "Quieres mostrar los pasos para lavar un trapo, de uno en uno y en orden. ¿Qué diagrama eliges: de flujo o de ciclo?", ["Los pasos van de uno al siguiente y terminan.", "Eso lo muestra un diagrama de flujo."], "Diagrama de flujo"),
    ],
    mistakes=[
        ("Poner letra clara sobre fondo claro.", "No se ve.", "Usa texto oscuro sobre fondo claro, o al revés."),
        ("Usar una imagen de internet sin fuente.", "No se respeta al autor.", "Usa imágenes propias o con permiso y anota la fuente."),
    ],
    R=[
        ("¿Cuántas líneas de texto lleva una diapositiva legible?", "Entre 3 y 5", "Más texto no se lee."),
        ("Letra negra sobre fondo blanco, ¿tiene buen o mal contraste?", "Buen contraste", "Se distingue con claridad."),
        ("¿Qué se anota cuando usas una imagen que no es tuya?", "La fuente", "Reconoce al autor."),
    ],
    C=[
        ("¿Para qué sirve un diagrama de ciclo?", "Para mostrar pasos que se repiten", "Termina donde empezó."),
        ("¿Por qué es mejor una imagen propia o con permiso?", "Porque respeta los derechos de autor", "El autor decide cómo se usa."),
        ("¿Por qué evitar animaciones que solo adornan?", "Porque distraen de la idea principal", "La atención debe estar en los datos."),
    ],
    A=[
        ("Quieres mostrar el ciclo del agua: evaporación, condensación, precipitación y escurrimiento, que se repiten. ¿Qué diagrama eliges?", "Diagrama de ciclo", "Los pasos se repiten."),
        arith("Una diapositiva tenía 10 líneas y se reduce a 4. ¿Cuántas líneas se quitaron?", "10-4", "Se resta lo que queda de lo que había.", " líneas"),
        ("Fondo azul oscuro. ¿Qué color de letra tiene mejor contraste? A blanca, B azul marino.", "A", "La letra clara destaca sobre un fondo oscuro."),
    ],
    Z=[
        ("Un equipo usa 5 tipos de letra, 6 colores y una animación que gira. ¿Qué cambio mejora más la presentación?", "Usar un solo tipo de letra y pocos colores", "Se evita distraer y el texto se lee mejor."),
        ("Una compañera usa la fotografía de otra persona sin permiso. ¿Qué debe hacer?", "Usar una imagen propia o con permiso y anotar la fuente", "Se respetan los derechos de autor."),
    ],
    D=[
        arith("Una presentación tiene 15 diapositivas y cada una usa un diagrama o una imagen. 6 usan diagramas. ¿Cuántas usan imágenes?", "15-6", "Se resta de las 15 las que usan diagramas.", " diapositivas"),
        ("La letra debe ser de 24 puntos como mínimo. Un equipo usa 18 puntos. ¿Cuántos puntos debe aumentar?", "6 puntos", "24 − 18 = 6."),
    ],
    ctx=("Preparas una diapositiva sobre la regla de las tres erres: reducir, reutilizar y reciclar. Escribe el título, 3 líneas cortas, el diagrama que usarías (flujo, ciclo o esquema) y el color de texto y de fondo.", "Título: Las tres erres. Líneas: reducir, reutilizar, reciclar. Esquema con las tres partes. Texto oscuro sobre fondo claro", "Las tres erres son partes de una idea y no pasos que se repiten, por eso sirve un esquema."),
    sc=[
        ("¿Qué mide el tamaño de letra de una diapositiva?", "Cuán grande se ve el texto", "Debe leerse a distancia."),
        ("¿Qué diagrama muestra pasos con flechas que terminan?", "El diagrama de flujo", "Va de un paso a otro hasta el final."),
        ("¿Qué se hace con una imagen ajena?", "Pedir permiso y citar la fuente", "Se respeta al autor."),
    ],
    open_task=(
        "Escoge una diapositiva. Diapositiva 1: los pasos para hacer una caja de cartón (medir, cortar, pegar, pintar). Diapositiva 2: el ciclo de vida de una botella reutilizada (usar, lavar, rellenar, volver a usar). Escribe el título, el texto breve en 3 a 5 líneas, qué diagrama usas y los colores del texto y del fondo. Indica una imagen propia que podrías incluir.",
        "Diapositiva 2: título «Reutilizar una botella». Diagrama de ciclo. Texto oscuro sobre fondo claro. Imagen: dibujo propio",
        ["texto breve de 3 a 5 líneas", "diagrama adecuado", "buen contraste", "imagen propia o con fuente"],
        ["boceto en papel de la diapositiva"],
        ["demasiado texto", "mal contraste"],
        "Pregunta: «¿se lee desde el fondo de la sala?». Si no, pídele reducir texto o aumentar la letra.",
    ),
    reinforce="Dibuja una diapositiva de un tema que te guste con título y 3 líneas.",
    extend="Explica cuándo conviene un diagrama de flujo y cuándo uno de ciclo, con un ejemplo de cada uno.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja cuadriculada y lápiz. Las tablas están escritas en este cuaderno. Si tienes computador, una hoja de cálculo.",
    use="Aprenderé a organizar datos en una tabla de doble entrada en una hoja de cálculo y a calcular totales. Sirve para ordenar los resultados antes de graficarlos.",
    prior=["Sé qué es una fila y una columna.", "Sé sumar varias cifras.", "Sé calcular un promedio."],
    explain=[
        "Una hoja de cálculo es un programa con filas y columnas. Cada cuadro se llama celda. Las columnas se nombran con letras (A, B, C) y las filas con números (1, 2, 3). Así, la celda B3 está en la columna B y la fila 3. En una celda se puede escribir un número, un texto o un cálculo.",
        "Una tabla de doble entrada organiza datos con dos criterios: uno va en las filas y otro en las columnas. Por ejemplo, las filas pueden ser los cursos y las columnas, las frutas. Cada celda del interior cruza una fila y una columna, y muestra un dato, como cuántos estudiantes del curso A eligieron manzana.",
        "Para calcular, se escribe un signo igual y la operación. Por ejemplo, «=B2+C2+D2» suma tres celdas y «=SUMA(B2:B4)» suma las celdas de B2 a B4. Los totales por fila y por columna ayudan a revisar los datos: la suma de todos los totales por fila debe coincidir con la suma de todos los totales por columna.",
    ],
    vocab=[("celda", "cuadro donde se cruza una fila con una columna"), ("tabla de doble entrada", "tabla que organiza datos con dos criterios, uno en filas y otro en columnas"), ("fila", "línea horizontal de celdas"), ("columna", "línea vertical de celdas"), ("total", "resultado de sumar varios datos")],
    worked=[
        ("Leer una tabla de doble entrada", "Tabla. Columnas: Manzana, Plátano, Naranja. Sala A: 8, 5, 7. Sala B: 6, 9, 4. ¿Cuántos estudiantes de la sala B eligieron plátano?", ["Busco la fila Sala B.", "Busco la columna Plátano: el cruce dice 9."], "9 estudiantes"),
        ("Calcular totales", "Con la tabla anterior, ¿cuál es el total de la sala A y el total de la columna Manzana?", ["Sala A: 8 + 5 + 7 = 20.", "Manzana: 8 + 6 = 14."], "Sala A: 20; Manzana: 14"),
    ],
    mistakes=[
        ("Confundir fila con columna.", "Se lee un dato de otro lugar.", "Recuerda: fila es horizontal y columna es vertical."),
        ("Escribir la suma sin el signo igual.", "El programa lo toma como texto.", "Empieza el cálculo con un signo igual."),
    ],
    R=[
        ("¿La celda B3 está en la columna B o en la fila B?", "En la columna B", "Las letras son columnas."),
        ("¿Una fila es horizontal o vertical?", "Horizontal", "Va de lado a lado."),
        ("¿Con qué signo empieza un cálculo en una hoja de cálculo?", "Con un signo igual", "Indica que es un cálculo."),
    ],
    C=[
        ("¿Qué cruza cada celda de una tabla de doble entrada?", "Una fila y una columna", "Muestra el dato de ambos criterios."),
        ("¿Para qué sirve un total por columna?", "Para saber cuánto suma cada categoría", "Resume la columna."),
        ("¿Qué hace «=B2+C2+D2»?", "Suma las celdas B2, C2 y D2", "Es un cálculo."),
    ],
    A=[
        ("Tabla de reciclaje. Columna A: semana; B: papel; C: plástico; D: latas. Fila 2: Semana 1 = 12, 8, 5. Fila 3: Semana 2 = 15, 6, 9. Fila 4: Semana 3 = 10, 11, 4. ¿Qué valor tiene la celda C3?", "6", "C3 es plástico en la semana 2."),
        arith("Con la tabla de reciclaje anterior, ¿cuál es el total de papel de las 3 semanas?", "12+15+10", "Se suman las tres celdas de la columna B.", " unidades"),
        arith("En esa tabla, ¿cuántas unidades recicló el curso en la Semana 3 sumando papel, plástico y latas?", "10+11+4", "Se suma la fila de la semana 3.", " unidades"),
    ],
    Z=[
        ("Un equipo sumó los totales por fila y obtuvo 100, y sumó los totales por columna y obtuvo 98. ¿Qué indica?", "Que hay un error en los datos o en una suma", "Ambos totales deberían ser iguales."),
        ("Tienes datos de 3 cursos y 4 deportes. ¿Cuántas celdas de datos tendrá la tabla de doble entrada, sin contar los títulos?", "12", "3 filas por 4 columnas dan 12."),
    ],
    D=[
        arith("En una hoja de cálculo se suman las celdas de B2 a B6. ¿Cuántas celdas se suman?", "6-2+1", "Se cuentan las filas 2, 3, 4, 5 y 6.", " celdas"),
        arith("Tabla de 4 filas y 5 columnas de datos. Si cada celda tiene el valor 3, ¿cuánto suman todas las celdas?", "4*5*3", "Hay 20 celdas de valor 3.", ""),
    ],
    ctx=("Anotas cuántas veces fueron a la biblioteca tres cursos en tres meses. Abril: A=10, B=8, C=12. Mayo: A=14, B=9, C=11. Junio: A=7, B=13, C=15. Escribe los totales por curso y por mes y comprueba que ambos suman lo mismo.", "Totales por curso: A 31, B 30, C 38. Por mes: abril 30, mayo 34, junio 35. Ambos suman 99", "Se suman filas y columnas y se comparan los totales."),
    sc=[
        ("¿Cómo se nombra una celda?", "Con la letra de la columna y el número de la fila", "Por ejemplo, B3."),
        ("¿Qué es una tabla de doble entrada?", "Una tabla con un criterio en filas y otro en columnas", "Cruza dos criterios."),
        ("¿Para qué se suman los totales?", "Para revisar que los datos estén bien", "Los totales deben coincidir."),
    ],
    open_task=(
        "Escoge una encuesta. Encuesta 1: sala A: fútbol 9, vóleibol 6, básquetbol 5; sala B: fútbol 7, vóleibol 8, básquetbol 4. Encuesta 2: lunes: leche 12, jugo 8, agua 5; martes: leche 10, jugo 9, agua 6; miércoles: leche 11, jugo 7, agua 7. Dibuja la tabla de doble entrada con encabezados, escribe los totales por fila y por columna y comprueba que ambos suman lo mismo.",
        "Encuesta 1: totales por sala 20 y 19; por deporte 16, 14 y 9. Ambos suman 39",
        ["tabla con encabezados", "totales por fila y por columna", "comprueba la suma total", "usa los datos dados"],
        ["tabla de doble entrada con totales"],
        ["confundir filas y columnas", "no verificar los totales"],
        "Pregunta: «¿qué suman las filas y qué suman las columnas?». Si no coinciden, pídele revisar.",
    ),
    reinforce="Haz una tabla de doble entrada con los días de lunes a viernes en las filas y tres asignaturas en las columnas, y marca con un 1 las asignaturas en que tienes tarea cada día.",
    extend="Explica qué diferencia hay entre una tabla simple y una de doble entrada, con un ejemplo.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja cuadriculada y lápiz. Los datos están escritos en este cuaderno.",
    use="Aprenderé a diseñar y leer gráficos de barra simple y de barra doble a partir de una tabla. Sirve para comparar categorías con una imagen clara.",
    prior=["Sé organizar datos en una tabla.", "Sé qué es un eje.", "Sé comparar números."],
    explain=[
        "Un gráfico de barras muestra cantidades con barras de distinta altura. El eje horizontal indica las categorías, como los cursos o los meses, y el eje vertical indica la cantidad con una escala, por ejemplo de 0 a 20 de 5 en 5. Todo gráfico lleva título, nombre de los ejes y las unidades.",
        "El gráfico de barra simple compara una cantidad entre categorías, como cuántos estudiantes eligieron cada fruta. El gráfico de barra doble compara dos grupos a la vez, con dos barras por categoría y una leyenda que dice qué color es cada grupo. Sirve, por ejemplo, para comparar dos cursos mes a mes.",
        "Para hacer un gráfico en una hoja de cálculo, se selecciona la tabla con sus encabezados, se elige el tipo de gráfico y se revisan el título, los ejes y la leyenda. La escala debe empezar en cero; si no, las diferencias parecen mayores de lo que son. Leer un gráfico es comparar la altura de las barras con la escala.",
    ],
    vocab=[("eje", "línea del gráfico donde se ubican categorías o cantidades"), ("escala", "valores marcados en el eje, a igual distancia"), ("barra simple", "gráfico con una barra por categoría"), ("barra doble", "gráfico con dos barras por categoría para comparar dos grupos"), ("leyenda", "recuadro que explica qué representa cada color")],
    worked=[
        ("Leer una barra simple", "Un gráfico de barras muestra frutas elegidas: manzana 12, plátano 9, naranja 6. ¿Cuántos estudiantes más eligieron manzana que naranja?", ["Manzana tiene 12.", "Naranja tiene 6. Resto 12 − 6."], "6 estudiantes más"),
        ("Leer una barra doble", "Barras dobles por mes. Abril: 6.ºA 10, 6.ºB 8. Mayo: 6.ºA 12, 6.ºB 15. ¿En qué mes ganó 6.ºB y por cuánto?", ["En abril 6.ºB tiene 8, menos que 6.ºA.", "En mayo 6.ºB tiene 15 y 6.ºA 12, o sea 3 más."], "En mayo, por 3"),
    ],
    mistakes=[
        ("Empezar la escala en un número distinto de cero.", "Las diferencias parecen mayores.", "Empieza la escala en cero."),
        ("Dibujar barras dobles sin leyenda.", "No se sabe qué color es cada grupo.", "Agrega una leyenda."),
    ],
    R=[
        ("¿Qué indica el eje vertical de un gráfico de barras?", "La cantidad", "Tiene la escala de valores."),
        ("¿Qué compara una barra doble: uno o dos grupos?", "Dos grupos", "Hay dos barras por categoría."),
        ("¿Qué lleva todo gráfico?", "Título, ejes y unidades", "Permiten entender lo que se muestra."),
    ],
    C=[
        ("¿Para qué sirve la leyenda en un gráfico de barra doble?", "Para decir qué color representa cada grupo", "Sin leyenda no se distinguen."),
        ("¿Por qué la escala empieza en cero?", "Para que las diferencias no parezcan exageradas", "Así no se distorsionan los datos."),
        ("Quieres comparar solo cuántos estudiantes eligen cada deporte. ¿Qué gráfico usas: barra simple o doble?", "Barra simple", "Es una sola cantidad por categoría."),
    ],
    A=[
        arith("Un gráfico de barras muestra mascotas: perro 14, gato 9, ave 4. ¿Cuántos estudiantes tienen perro o gato?", "14+9", "Se suman las barras de perro y gato.", " estudiantes"),
        arith("Barras de lluvia en milímetros: enero 18 y febrero 6. ¿Cuántos milímetros más llovió en enero?", "18-6", "Se resta la barra más baja de la más alta.", " mm"),
        ("En un gráfico de barra doble con 3 cursos, ¿cuántas barras hay en total?", "6", "Hay 2 barras por cada uno de los 3 cursos."),
    ],
    Z=[
        ("Un gráfico tiene la escala desde 90 hasta 100 y dos barras de 92 y 98. Parece que una es muchísimo más alta. ¿Qué problema tiene?", "La escala no empieza en cero", "Exagera la diferencia."),
        ("Quieres comparar la lectura de dos cursos en tres meses. ¿Qué gráfico eliges?", "Barra doble", "Compara dos grupos por mes."),
    ],
    D=[
        arith("Barra doble. Curso A: 12, 15, 9. Curso B: 10, 14, 13. ¿Cuántos libros leyó A en total?", "12+15+9", "Se suman las tres barras de A.", " libros"),
        arith("Con los mismos datos (A: 12, 15, 9 y B: 10, 14, 13), ¿cuántos libros más leyó B que A en total?", "(10+14+13)-(12+15+9)", "Se comparan los totales de B y de A.", " libro"),
    ],
    ctx=("Tienes los datos de bebidas del recreo: lunes: jugo 10, agua 15; martes: jugo 12, agua 9; miércoles: jugo 7, agua 14. Escribe qué tipo de gráfico usarías, qué va en cada eje, la escala sugerida y qué día ganó el agua por más.", "Barra doble; eje horizontal: días; eje vertical: cantidad de 0 a 15; el miércoles el agua ganó por 7", "El miércoles 14 − 7 = 7, más que el lunes (5)."),
    sc=[
        ("¿Qué va en el eje horizontal?", "Las categorías", "Por ejemplo, días o cursos."),
        ("¿Cuándo se usa una barra doble?", "Cuando se comparan dos grupos", "Cada categoría tiene dos barras."),
        ("¿Dónde empieza la escala?", "En cero", "Así no se distorsiona."),
    ],
    open_task=(
        "Escoge un conjunto de datos. Datos 1: estudiantes que usan bicicleta: lunes 5, martes 8, miércoles 6, jueves 9. Datos 2: lectura de dos grupos en tres semanas: grupo azul 8, 11, 9; grupo rojo 6, 10, 13. Decide qué gráfico usar, dibuja el gráfico con título, ejes, escala desde cero y leyenda si corresponde, y escribe dos conclusiones con números.",
        "Datos 2: barra doble con leyenda. Conclusiones: en la semana 3 el grupo rojo leyó 4 más que el azul; el grupo rojo ganó solo en la semana 3",
        ["elige el tipo de gráfico", "título, ejes y escala desde cero", "leyenda si es doble", "dos conclusiones con números"],
        ["gráfico dibujado con conclusiones"],
        ["escala que no empieza en cero", "olvidar la leyenda"],
        "Pregunta: «¿qué compara este gráfico?». Revisa el tipo elegido.",
    ),
    reinforce="Haz un gráfico de barras con los colores de 10 lápices o plumones que tengas a mano.",
    extend="Explica por qué una escala que no empieza en cero puede engañar a quien lee el gráfico.",
)

# ------------------------------------------------------------------ OA 05, clase 5
reg(
    OA5, 5,
    materials="Hoja cuadriculada y lápiz. Los datos están escritos en este cuaderno.",
    use="Aprenderé a diseñar y leer gráficos circulares y de línea y a elegir el gráfico adecuado. Sirve para mostrar partes de un total y cambios en el tiempo.",
    prior=["Sé hacer gráficos de barras.", "Sé calcular porcentajes sencillos.", "Sé qué es un eje."],
    explain=[
        "Un gráfico circular, o de torta, muestra cómo se reparte un total en partes. Todo el círculo es el 100 % y cada parte es un sector. Sirve cuando las partes son un total, como cómo se reparten 40 estudiantes entre tres deportes. Si 20 de 40 eligen fútbol, su sector es la mitad del círculo (50 %).",
        "Un gráfico de línea muestra cómo cambia un dato en el tiempo, como la altura de una planta cada semana. En el eje horizontal va el tiempo y en el vertical, la cantidad. Los puntos se unen con una línea: si sube, la cantidad aumenta; si baja, disminuye; si queda plana, no cambia.",
        "Para elegir un gráfico se piensa en el propósito. Para comparar cantidades entre categorías, barras. Para mostrar partes de un total, círculo. Para mostrar cambio en el tiempo, línea. En la hoja de cálculo se elige el tipo de gráfico y se revisa el título y las etiquetas. El gráfico circular no sirve para más de 5 o 6 partes.",
    ],
    vocab=[("sector", "parte de un gráfico circular"), ("gráfico circular", "gráfico que muestra cómo se reparte un total"), ("gráfico de línea", "gráfico que muestra cómo cambia un dato en el tiempo"), ("tendencia", "dirección en que cambia un dato"), ("porcentaje", "cantidad de cada 100")],
    worked=[
        ("Calcular un sector", "En un curso de 40 estudiantes, 10 prefieren básquetbol. ¿Qué porcentaje del círculo ocupa ese sector?", ["Multiplico 10 por 100: 1.000.", "Divido 1.000 entre 40."], "25 %"),
        ("Leer un gráfico de línea", "Altura de una planta: semana 1: 3 cm, semana 2: 7 cm, semana 3: 12 cm, semana 4: 18 cm. ¿En qué semana creció más la planta respecto de la semana anterior y cuánto?", ["Aumentos: 4 (de 3 a 7), 5 (de 7 a 12), 6 (de 12 a 18).", "El mayor aumento es en la semana 4: 6 cm."], "En la semana 4, 6 cm"),
    ],
    mistakes=[
        ("Usar un gráfico circular para comparar muchos grupos.", "Los sectores pequeños no se distinguen.", "Usa barras si hay más de 5 o 6 categorías."),
        ("Usar gráfico de barras para mostrar cambios diarios en el tiempo.", "No muestra la tendencia con claridad.", "Usa un gráfico de línea."),
    ],
    R=[
        ("¿Cuánto es todo el círculo de un gráfico circular?", "El 100 %", "Representa el total."),
        ("¿Qué gráfico muestra cómo cambia un dato en el tiempo?", "El gráfico de línea", "Une puntos en el tiempo."),
        ("Si la línea sube, ¿la cantidad aumenta o disminuye?", "Aumenta", "Sube con el tiempo."),
    ],
    C=[
        ("¿Qué gráfico eliges para mostrar cómo se reparte el tiempo de un día (dormir, estudiar, jugar, comer)?", "Circular", "Muestra partes de un total."),
        ("¿Qué gráfico eliges para mostrar la temperatura de cada día de una semana?", "De línea", "Muestra el cambio en el tiempo."),
        ("¿Por qué no se usa un gráfico circular con 12 categorías?", "Porque los sectores serían muy pequeños", "No se distinguirían."),
    ],
    A=[
        arith("En un curso de 50 estudiantes, 25 prefieren fútbol. ¿Qué porcentaje es?", "25*100//50", "Se multiplica por 100 y se divide entre el total.", " %"),
        arith("En un curso de 20 estudiantes, 6 prefieren vóleibol. ¿Qué porcentaje es?", "6*100//20", "Se multiplica por 100 y se divide entre el total.", " %"),
        arith("Una planta mide 6 cm la semana 1 y 15 cm la semana 4. ¿Cuántos centímetros creció en ese tiempo?", "15-6", "Se resta la altura inicial de la final.", " cm"),
    ],
    Z=[
        ("Ana dice que un gráfico circular con los sectores 50 %, 30 % y 30 % está bien hecho. ¿Qué error tiene?", "Los sectores suman 110 %, no 100 %", "Un círculo completo debe sumar 100 %."),
        ("Para mostrar cuántas horas durmió una persona cada noche durante 7 noches, ¿qué gráfico elige Rosa y por qué?", "De línea, porque muestra el cambio día a día", "Son datos que cambian en el tiempo."),
    ],
    D=[
        arith("En una encuesta de 80 estudiantes, 20 eligen jugo, 40 eligen agua y el resto leche. ¿Qué porcentaje elige leche?", "(80-20-40)*100//80", "Primero se halla cuántos eligen leche y luego se calcula el porcentaje.", " %"),
        ("Datos de lluvia en milímetros por mes: enero 2, febrero 4, marzo 9, abril 20, mayo 40. ¿Entre qué meses hubo el mayor aumento?", "Entre abril y mayo", "Subió 20 mm, más que en los otros meses."),
    ],
    ctx=("En tu curso de 30 estudiantes, 15 viajan en bus, 9 caminan y 6 vienen en auto. Calcula el porcentaje de cada grupo, di qué gráfico usarías y cómo se vería el sector de bus.", "Bus 50 %, caminan 30 %, auto 20 %. Circular. El bus ocupa la mitad del círculo", "15 de 30 es la mitad; 9 de 30 es 30; 6 de 30 es 20."),
    sc=[
        ("¿Cuánto suman todos los sectores?", "100 %", "Son el total."),
        ("¿Qué muestra un gráfico de línea?", "Cambios en el tiempo", "Une puntos de distintos momentos."),
        ("¿Qué gráfico compara cantidades entre categorías?", "El de barras", "Muestra alturas comparables."),
    ],
    open_task=(
        "Escoge un conjunto de datos. Datos 1: 60 estudiantes eligen un animal: 30 perro, 15 gato, 15 conejo. Datos 2: altura de una planta al final de cada mes: marzo 8 cm, abril 10 cm, mayo 13 cm, junio 18 cm. Decide el tipo de gráfico, calcula los porcentajes si es circular o la tendencia si es de línea, explica tu decisión y escribe dos conclusiones con números.",
        "Datos 1: circular; perro 50 %, gato 25 %, conejo 25 %. Conclusión: el perro ocupa la mitad del círculo",
        ["elige el gráfico y lo explica", "cálculos correctos", "dos conclusiones con números", "título y etiquetas"],
        ["gráfico dibujado con cálculos"],
        ["gráfico circular que no suma 100 %", "usar barras para cambio en el tiempo"],
        "Pregunta: «¿es un total repartido o un cambio en el tiempo?». Revisa el gráfico elegido.",
    ),
    reinforce="Anota durante 4 días cuántas horas ves la tele o juegas y haz un gráfico de línea.",
    extend="Explica por qué dos gráficos pueden mostrar los mismos datos pero uno comunica mejor la idea.",
)

# ------------------------------------------------------------------ OA 05, clase 6
reg(
    OA5, 6,
    materials="Hoja y lápiz. Los datos y los casos están escritos en este cuaderno.",
    use="Aprenderé a combinar tabla, gráfico y presentación para comunicar los resultados de una investigación y a intercambiar ideas con distintos propósitos. Sirve para explicar tus hallazgos con claridad.",
    prior=["Sé hacer presentaciones.", "Sé hacer tablas de doble entrada.", "Sé elegir un gráfico."],
    explain=[
        "Los resultados de una investigación se comunican mejor cuando se combinan recursos: una tabla de doble entrada que organiza los datos, un gráfico que muestra lo importante y una diapositiva que cuenta la conclusión con pocas palabras. Cada recurso cumple un papel: la tabla ordena, el gráfico compara y la presentación explica.",
        "El propósito cambia lo que se comunica. Para informar, se muestran los datos con claridad. Para convencer, se usan datos y razones que apoyen una propuesta. Para intercambiar ideas, se muestra un resultado y se pide opinión o sugerencias. Siempre se indica la fuente y se evita exagerar con gráficos engañosos.",
        "Para trabajar con otras personas, se pueden compartir archivos, comentar las diapositivas y acordar quién completa cada parte. Se revisan los datos antes de presentar. Después de la presentación, se escuchan las preguntas, se responde con evidencia y se anotan las ideas de mejora.",
    ],
    vocab=[("hallazgo", "resultado importante de una investigación"), ("propósito", "para qué se comunica algo"), ("intercambiar ideas", "compartir opiniones y escuchar las de otras personas"), ("evidencia", "datos que apoyan una conclusión"), ("trabajo colaborativo", "trabajo en que varias personas aportan")],
    worked=[
        ("Elegir el recurso", "Quieres mostrar a tu curso cuántos libros leyeron 4 cursos en 3 meses. ¿Qué recursos combinas?", ["Una tabla de doble entrada organiza cursos y meses.", "Un gráfico de barras compara los cursos y la diapositiva cuenta la conclusión."], "Tabla de doble entrada, gráfico de barras y una diapositiva de conclusión"),
        ("Ajustar al propósito", "Quieres que la dirección compre más papeleros porque el patio tiene 3 y se llenan en una hora. ¿Qué propósito tiene y qué dato muestras?", ["El propósito es convencer.", "Muestras el dato: 3 papeleros se llenan en 1 hora."], "Convencer; muestro que 3 papeleros se llenan en 1 hora"),
    ],
    mistakes=[
        ("Poner todos los datos en la presentación.", "La audiencia se pierde.", "Incluye solo los datos que responden la pregunta."),
        ("Usar un gráfico que exagera las diferencias.", "Engaña a quien lee.", "Usa escala desde cero y rotula los ejes."),
    ],
    R=[
        ("¿Qué recurso ordena los datos: la tabla o el gráfico?", "La tabla", "Organiza filas y columnas."),
        ("Pedir opiniones sobre un resultado, ¿es informar o intercambiar ideas?", "Intercambiar ideas", "Se escucha a las demás personas."),
        ("¿Qué recurso compara cantidades de un vistazo?", "El gráfico", "Las alturas se ven rápido."),
    ],
    C=[
        ("¿Por qué conviene revisar los datos antes de presentar?", "Para evitar errores en los resultados", "Los errores quitan credibilidad."),
        ("¿Qué se hace con las preguntas de la audiencia?", "Se responden con evidencia y se anotan las ideas", "Mejora el trabajo."),
        ("Quieres convencer a tu curso de ahorrar agua. ¿Qué incluyes? A datos que apoyen la propuesta, B chistes sin relación.", "A", "Convencer necesita razones y datos."),
    ],
    A=[
        arith("Una presentación tiene 4 gráficos y cada gráfico se explica en 2 diapositivas. ¿Cuántas diapositivas ocupan los gráficos?", "4*2", "Se multiplican los gráficos por las diapositivas de cada uno.", " diapositivas"),
        arith("La presentación dura 10 minutos. Se usan 3 para la introducción y 2 para las preguntas. ¿Cuántos minutos quedan para los resultados?", "10-3-2", "Se restan las otras partes del total.", " minutos"),
        ("Tu pregunta es cuánto cambió la altura de una planta en 5 semanas. ¿Qué gráfico eliges?", "De línea", "Muestra el cambio en el tiempo."),
    ],
    Z=[
        ("Un equipo muestra la misma tabla en cuatro diapositivas seguidas. ¿Qué debería hacer para comunicar mejor?", "Mostrar un gráfico y la conclusión", "La tabla ordena; el gráfico y la conclusión comunican."),
        ("Dos equipos concluyen cosas distintas con los mismos datos. ¿Qué hacen al intercambiar ideas?", "Revisar juntos los datos y la evidencia", "Así se llega a una conclusión justificada."),
    ],
    D=[
        arith("Un equipo recibe 3 sugerencias por cada una de sus 5 diapositivas. ¿Cuántas sugerencias recibe en total?", "3*5", "Se multiplican las diapositivas por las sugerencias.", " sugerencias"),
        ("Una conclusión dice «todos los cursos mejoraron». Los datos muestran que 2 de 4 cursos mejoraron. ¿Es correcta?", "No", "Solo la mitad de los cursos mejoró."),
    ],
    ctx=("Tu curso midió cuántos kilogramos de papel reciclaron en 4 semanas: 5, 8, 12 y 15 kg. Quieres convencer a la dirección de comprar un contenedor más grande. Escribe qué tabla, gráfico y diapositivas usarías, y la conclusión.", "Tabla de semana y kilogramos; gráfico de línea; 3 diapositivas: datos, gráfico y conclusión: el reciclaje se triplicó en 4 semanas", "15 es el triple de 5, y la línea muestra el aumento."),
    sc=[
        ("¿Qué papel cumple cada recurso?", "La tabla ordena, el gráfico compara y la presentación explica", "Cada uno ayuda a comunicar."),
        ("¿Qué cambia con el propósito?", "Lo que se comunica y cómo", "Informar, convencer e intercambiar son distintos."),
        ("¿Qué se hace tras la presentación?", "Escuchar preguntas y anotar mejoras", "Permite mejorar el trabajo."),
    ],
    open_task=(
        "Escoge una investigación. Investigación 1: se midió cuántos minutos de lectura hizo un curso cada día de una semana: lunes 15, martes 20, miércoles 18, jueves 25, viernes 30. Investigación 2: 40 estudiantes eligieron su juego favorito: 20 pillarse, 10 saltar la cuerda y 10 pelota. Elige un propósito, un gráfico y una tabla, planifica 4 diapositivas y escribe una pregunta para la audiencia.",
        "Investigación 2: propósito informar; gráfico circular; 4 diapositivas: portada, tabla, gráfico, conclusión. Pregunta: ¿qué otro juego añadirían?",
        ["elige propósito", "elige gráfico y tabla adecuados", "planifica cuatro diapositivas", "pregunta para la audiencia"],
        ["plan escrito con diapositivas y gráfico"],
        ["usar el gráfico equivocado", "no indicar la fuente"],
        "Pregunta: «¿qué quieres que entienda la audiencia?». Revisa que el gráfico respalde esa idea.",
    ),
    reinforce="Elige un tema que te guste, anota cuatro datos y decide qué gráfico los muestra mejor.",
    extend="Explica cómo cambiarías tu presentación si en vez de informar quisieras convencer a otras personas.",
)
