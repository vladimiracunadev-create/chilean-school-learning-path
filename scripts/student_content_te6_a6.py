"""Cuaderno del estudiante, 6.º básico Tecnología: OA 06 (procesador de textos), clases 1 a 5.

Clase 1 crear y guardar, 2 editar, 3 dar formato, 4 elementos de diseño, 5 revisar y guardar versiones.
Simplificación declarada: no se verifica el manejo de un programa real (cada programa se ve distinto); se enseñan conceptos, decisiones y resultados que se
describen con texto y tienen alternativa en papel. No se nombra ninguna marca. Los textos y datos son ficticios y sin datos personales.
"""
from __future__ import annotations

from student_content_te6_a import reg
from student_lessons import arith

OA6 = "TE06 OA 06"

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja y lápiz. Si tienes computador, un procesador de textos; si no, escribe en papel todo lo que se pide.",
    use="Aprenderé a crear un documento nuevo, escribir con orden y guardarlo con un nombre claro en una carpeta. Sirve para encontrar tu trabajo después y compartirlo.",
    prior=["Sé escribir un texto con párrafos.", "Sé usar mayúsculas, tildes y puntuación.", "Sé qué es una carpeta."],
    explain=[
        "Un procesador de textos es un programa para escribir, editar y dar formato a documentos. Para empezar se crea un documento nuevo, que aparece como una hoja en blanco con un cursor parpadeante. El cursor marca dónde se escribirá la próxima letra. Se escribe con el teclado, la tecla Mayúscula para las mayúsculas y la tecla Enter para pasar a un párrafo nuevo.",
        "Un documento ordenado tiene un título, párrafos separados y un solo espacio entre las palabras. No se usa Enter al final de cada línea: el programa pasa solo a la línea siguiente. Se escribe con tildes, mayúsculas y puntuación correctas. Al comenzar, escribe el contenido y deja el diseño para después.",
        "Guardar es almacenar el documento para no perderlo. Se elige una carpeta y un nombre claro que diga qué es, como «informe_reciclaje_curso6». Se evita usar nombres como «documento1» o con tildes y espacios raros. Guarda al comenzar y cada pocos minutos. Un documento que no se guardó se pierde si se corta la energía.",
    ],
    vocab=[("procesador de textos", "programa para escribir y dar formato a documentos"), ("cursor", "marca que indica dónde se escribe"), ("párrafo", "bloque de texto que termina con Enter"), ("archivo", "documento guardado con un nombre"), ("carpeta", "lugar donde se ordenan los archivos")],
    worked=[
        ("Elegir un nombre de archivo", "Escribiste un informe sobre el reciclaje de papel del curso 6. ¿Cuál nombre es mejor: A «documento1» o B «informe_reciclaje_papel_curso6»?", ["Un nombre claro dice qué es el archivo.", "El nombre B dice el tema y el curso."], "B"),
        ("Arreglar el uso de Enter", "Un estudiante pulsa Enter al final de cada línea y el párrafo queda cortado cuando cambia el tamaño de la página. ¿Qué hace mal?", ["Enter crea un párrafo nuevo y no es para cambiar de línea.", "El programa pasa solo a la línea siguiente."], "Usa Enter en cada línea; debe usarlo solo para terminar un párrafo"),
    ],
    mistakes=[
        ("Escribir sin guardar hasta el final.", "Si se corta la energía, se pierde todo.", "Guarda al empezar y cada pocos minutos."),
        ("Dejar dos espacios entre palabras.", "El texto se ve desparejo.", "Deja un solo espacio."),
    ],
    R=[
        ("¿Qué marca indica dónde se escribirá la próxima letra?", "El cursor", "Parpadea en el lugar de escritura."),
        ("¿Qué tecla se usa para empezar un párrafo nuevo?", "Enter", "Crea una línea nueva de párrafo."),
        ("¿Qué se hace para no perder un documento?", "Guardarlo", "Lo almacena en el computador."),
    ],
    C=[
        ("¿Por qué conviene darle un nombre claro a un archivo?", "Para encontrarlo después", "El nombre dice qué es."),
        ("¿Se usa Enter al final de cada línea?", "No, solo al terminar un párrafo", "El programa cambia de línea solo."),
        ("¿Cuándo conviene guardar un documento?", "Al empezar y cada pocos minutos", "Evita perder el trabajo."),
    ],
    A=[
        ("Elige el mejor nombre para una carta al director: A «sin_titulo», B «carta_director_6A».", "B", "Dice el contenido y el curso."),
        arith("Escribes 360 palabras y quieres saber cuántas páginas ocupan si caben 120 palabras por página. ¿Cuántas páginas son?", "360//120", "Se divide el total de palabras entre las que caben por página.", " páginas"),
        ("Un párrafo tiene dos espacios entre «la» y «casa» y falta la tilde en «mamá». ¿Cuántos errores de escritura tiene?", "2", "Hay un espacio de más y una tilde faltante."),
    ],
    Z=[
        ("Dos compañeros guardan su trabajo como «tarea». Al final del día no encuentran cuál es de cada uno. ¿Qué error cometieron?", "Usaron un nombre poco claro", "Un buen nombre dice qué es y de quién."),
        ("Rocío trabajó 40 minutos sin guardar y se cortó la luz. ¿Qué debió hacer?", "Guardar al empezar y cada pocos minutos", "Así se pierde poco."),
    ],
    D=[
        arith("Escribes a razón de 20 palabras por minuto. ¿Cuántas palabras escribes en 15 minutos?", "20*15", "Se multiplica el ritmo por los minutos.", " palabras"),
        arith("Tu informe tiene 450 palabras y escribes 30 palabras por minuto. ¿Cuántos minutos necesitas?", "450//30", "Se divide el total de palabras entre las palabras por minuto.", " minutos"),
    ],
    ctx=("Escribirás un informe de una página sobre las plantas de tu casa. Escribe el nombre del archivo que usarías, cuándo lo guardas la primera vez y cómo ordenas tu escritura (título y párrafos).", "Nombre: informe_plantas_casa_6. Guardo al comenzar. Título, introducción, tres plantas en párrafos separados y conclusión", "El nombre es claro, se guarda al comienzo y los párrafos están ordenados."),
    sc=[
        ("¿Qué es un procesador de textos?", "Un programa para escribir y dar formato a documentos", "Es la herramienta de la clase."),
        ("¿Cómo debe ser un nombre de archivo?", "Claro y que diga qué es", "Ayuda a encontrarlo."),
        ("¿Qué se hace con Enter?", "Empezar un párrafo nuevo", "Enter separa un párrafo de otro."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: una carta al curso para invitar a una exposición de trabajos, con fecha, saludo, dos párrafos y despedida. Documento 2: un informe de media página sobre un cuidado del ambiente. Escribe el texto completo con título, párrafos, tildes y puntuación; escribe el nombre del archivo y la carpeta donde lo guardarías. Si no tienes computador, hazlo en papel.",
        "Documento 2: título «Cuidar el agua en casa». Dos párrafos. Archivo: informe_agua_casa_6, carpeta Tecnología",
        ["texto con título y párrafos", "tildes y puntuación correctas", "nombre de archivo claro", "carpeta indicada"],
        ["texto escrito con nombre de archivo"],
        ["nombre poco claro", "uso de Enter en cada línea"],
        "Pregunta: «¿tu nombre dice qué es el archivo?». Si no, pídele reescribirlo.",
    ),
    reinforce="Escribe un párrafo de cuatro líneas sobre tu día, con título, y escribe el nombre del archivo.",
    extend="Explica por qué nombres como «documento1» pueden causar problemas cuando hay muchos archivos.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja y lápiz. Los textos están escritos en este cuaderno.",
    use="Aprenderé a editar un texto: seleccionar, copiar, cortar, pegar, deshacer y buscar y reemplazar. Sirve para corregir y reorganizar sin escribir todo de nuevo.",
    prior=["Sé crear y guardar un documento.", "Sé que un cursor marca dónde se escribe.", "Sé leer instrucciones paso a paso."],
    explain=[
        "Editar es cambiar un texto ya escrito. Para cambiar una parte, primero se selecciona: se arrastra el cursor sobre el texto o se hace doble clic en una palabra. Lo seleccionado se ve marcado. Luego se puede copiar, que deja el texto y guarda una copia; cortar, que lo saca y lo guarda; y pegar, que pone lo guardado donde está el cursor.",
        "Para mover un párrafo, se corta y se pega en el nuevo lugar. Para repetir un texto, se copia y se pega. Si te equivocas, usas deshacer, que anula la última acción, y rehacer, que la repite. Los atajos del teclado son más rápidos: copiar, cortar, pegar y deshacer tienen combinaciones de tecla Control con una letra.",
        "Buscar y reemplazar encuentra una palabra en todo el documento y la cambia por otra. Sirve para corregir un nombre que escribiste mal muchas veces. Antes de reemplazar todo, revisa dónde aparece, porque una palabra puede estar dentro de otra. Siempre guarda tu trabajo antes de hacer cambios grandes.",
    ],
    vocab=[("seleccionar", "marcar una parte del texto para trabajar con ella"), ("copiar", "guardar una copia sin sacar el texto"), ("cortar", "sacar el texto y guardarlo"), ("pegar", "poner el texto guardado donde está el cursor"), ("reemplazar", "cambiar una palabra por otra")],
    worked=[
        ("Mover un párrafo", "Escribiste: «1. Conclusión. 2. Introducción. 3. Desarrollo». Quieres el orden: introducción, desarrollo, conclusión. ¿Qué haces?", ["Selecciono «Conclusión» y la corto.", "Pego después de «Desarrollo»."], "Cortar «Conclusión» y pegarla al final"),
        ("Buscar y reemplazar", "El texto dice: «El gato duerme. El gato come. El gato juega». Reemplazas «gato» por «perro». ¿Cómo queda y cuántos cambios se hacen?", ["Aparece «gato» tres veces.", "Cada una pasa a «perro»."], "«El perro duerme. El perro come. El perro juega», 3 cambios"),
    ],
    mistakes=[
        ("Reemplazar todo sin revisar.", "Una palabra puede estar dentro de otra.", "Revisa dónde aparece antes de reemplazar todo."),
        ("Borrar un texto equivocado y no deshacer.", "Se pierde trabajo.", "Usa deshacer de inmediato."),
    ],
    R=[
        ("¿Qué se hace primero para cambiar una parte del texto?", "Seleccionarla", "Hay que marcar lo que se cambia."),
        ("¿Qué acción anula la última acción?", "Deshacer", "Devuelve el texto al paso anterior."),
        ("¿Cortar deja el texto en su lugar o lo saca?", "Lo saca", "Se guarda para pegarlo."),
    ],
    C=[
        ("¿Qué diferencia hay entre copiar y cortar?", "Copiar deja el texto y cortar lo saca", "Ambos guardan una copia."),
        ("¿Para qué sirve buscar y reemplazar?", "Para cambiar una palabra en todo el documento", "Ahorra tiempo y evita repetir cambios."),
        ("¿Para qué se guarda el trabajo antes de cambios grandes?", "Para poder volver si algo sale mal", "Evita perder lo hecho."),
    ],
    A=[
        ("Texto: «La casa es grande. La casa es azul». Reemplazas «casa» por «escuela». ¿Cómo queda?", "«La escuela es grande. La escuela es azul»", "Se cambian las dos veces."),
        arith("En un texto la palabra «hoja» aparece 7 veces. Reemplazas «hoja» por «página». ¿Cuántos cambios se hacen?", "7", "Cada aparición se cambia.", " cambios"),
        ("Quieres repetir la frase «Cuidemos el agua» al final de dos párrafos. ¿Qué haces: copiar y pegar o cortar y pegar?", "Copiar y pegar", "La frase debe quedar en el lugar original."),
    ],
    Z=[
        ("Reemplazas «sol» por «luna» en «solución al problema del sol». ¿Qué problema aparece?", "Cambia también «solución» por «lunaución»", "La palabra está dentro de otra."),
        ("Beto pegó un párrafo dos veces por error. ¿Cuál es la mejor acción? A borrar uno, B deshacer la última acción.", "B", "Deshacer lo anula de inmediato."),
    ],
    D=[
        arith("Copias dos párrafos de 50 palabras cada uno y los pegas 3 veces. ¿Cuántas palabras agregaste?", "2*50*3", "Son 100 palabras copiadas, pegadas 3 veces.", " palabras"),
        arith("Copias una frase de 12 palabras y la pegas 4 veces. ¿Cuántas palabras agregaste?", "12*4", "Se multiplica la frase por las veces que se pega.", " palabras"),
    ],
    ctx=("Escribes: «Los patos nadan. Los patos vuelan. Los patos comen». Quieres cambiar «patos» por «gansos» y mover la tercera oración al comienzo. Escribe cómo queda el texto y qué acciones usaste.", "«Los gansos comen. Los gansos nadan. Los gansos vuelan». Usé reemplazar y cortar y pegar", "Se reemplaza y se mueve la tercera oración al comienzo."),
    sc=[
        ("¿Qué se hace para mover un texto?", "Cortarlo y pegarlo", "Cambia su lugar."),
        ("¿Qué hace deshacer?", "Anula la última acción", "Sirve para corregir."),
        ("¿Qué se revisa antes de reemplazar todo?", "Dónde aparece la palabra", "Puede estar dentro de otra."),
    ],
    open_task=(
        "Escoge un texto. Texto 1: «El perro corre. El perro salta. El perro duerme». Texto 2: «Pintamos la caja. Cortamos el cartón. Medimos el cartón». Para el texto 1, reemplaza «perro» por «gato». Para el texto 2, ordena las oraciones con cortar y pegar para que la secuencia sea lógica (medir, cortar, pintar). Escribe el resultado y los pasos.",
        "Texto 2: «Medimos el cartón. Cortamos el cartón. Pintamos la caja». Pasos: cortar y pegar oraciones",
        ["resultado correcto", "pasos de edición nombrados", "secuencia lógica si corresponde", "sin perder texto"],
        ["texto final con pasos"],
        ["reemplazar todo sin revisar", "perder texto al mover"],
        "Pregunta: «¿qué acción usaste para mover y qué para repetir?». Revisa copiar y cortar.",
    ),
    reinforce="Escribe una frase de tres palabras y haz tres versiones cambiando una palabra cada vez.",
    extend="Explica por qué deshacer es una herramienta importante cuando editas un documento.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja y lápiz. Los textos están escritos en este cuaderno.",
    use="Aprenderé a dar formato a un texto con fuente, tamaño, negrita, alineación, interlineado y listas. Sirve para que el documento sea claro y fácil de leer.",
    prior=["Sé editar un texto.", "Sé qué es un título y un párrafo.", "Sé medir en centímetros."],
    explain=[
        "Dar formato es cambiar cómo se ve el texto sin cambiar lo que dice. La fuente es el tipo de letra; el tamaño se mide en puntos y para un texto normal se usan entre 11 y 12 puntos. El título puede ser más grande. La negrita destaca palabras importantes; la cursiva se usa para títulos de obras y palabras extranjeras; el subrayado casi no se usa.",
        "La alineación indica cómo se acomoda el texto: a la izquierda (la más fácil de leer), centrada (para títulos), a la derecha o justificada (ambos lados parejos). El interlineado es el espacio entre líneas; 1,5 facilita la lectura. La sangría es el espacio al comienzo de un párrafo. Se usa solo un tipo de letra y pocos colores.",
        "Las listas con viñetas se usan cuando el orden no importa, y las listas numeradas cuando importa, como los pasos de una receta. Los títulos y subtítulos con estilos distintos ayudan a ordenar el documento. Un formato se aplica seleccionando antes el texto. Se usa el mismo formato para elementos del mismo tipo.",
    ],
    vocab=[("fuente", "tipo de letra"), ("tamaño", "medida de la letra en puntos"), ("interlineado", "espacio entre las líneas"), ("alineación", "forma de acomodar el texto en la hoja"), ("viñeta", "símbolo que marca cada elemento de una lista")],
    worked=[
        ("Elegir la lista adecuada", "Escribirás los pasos para armar un puente, uno tras otro. ¿Lista con viñetas o numerada?", ["El orden de los pasos importa.", "Se usa la numerada."], "Numerada"),
        ("Elegir el tamaño", "Un texto largo se imprimirá y tiene letra de 6 puntos. ¿Qué tamaño conviene?", ["Una letra de 6 puntos es muy pequeña.", "Un texto normal usa entre 11 y 12 puntos."], "Entre 11 y 12 puntos"),
    ],
    mistakes=[
        ("Usar cinco tipos de letra en una página.", "Distrae y se ve desordenado.", "Usa un tipo de letra y destaca con negrita."),
        ("Poner todo el texto en negrita.", "Si todo se destaca, nada se destaca.", "Usa negrita solo para palabras clave."),
    ],
    R=[
        ("¿En qué se mide el tamaño de la letra?", "En puntos", "Es la unidad de las fuentes."),
        ("¿Qué alineación se usa en los títulos?", "Centrada", "Se destaca en el centro."),
        ("¿Para qué se usa la negrita?", "Para destacar palabras importantes", "Hace que resalten."),
    ],
    C=[
        ("¿Cuándo se usa una lista numerada?", "Cuando importa el orden", "Por ejemplo, los pasos de una receta."),
        ("¿Por qué el interlineado de 1,5 ayuda?", "Porque facilita leer las líneas", "Hay más espacio entre ellas."),
        ("¿Para qué se selecciona el texto antes de dar formato?", "Para que el formato se aplique a esa parte", "El formato afecta lo seleccionado."),
    ],
    A=[
        ("Escribirás los ingredientes de una receta sin importar el orden. ¿Lista con viñetas o numerada?", "Con viñetas", "El orden no importa."),
        ("¿Cuál tamaño es más adecuado para un texto normal impreso? A 8 puntos, B 12 puntos, C 30 puntos.", "B", "12 puntos se lee bien."),
        arith("Un título tiene tamaño de 18 puntos y el texto de 12. ¿Cuántos puntos es más grande el título?", "18-12", "Se resta el tamaño del texto del título.", " puntos"),
    ],
    Z=[
        ("Dos documentos tienen el mismo texto. Uno tiene 5 fuentes, 6 colores y todo en negrita; el otro tiene una fuente, 2 colores y títulos en negrita. ¿Cuál se lee mejor y por qué?", "El segundo, porque es ordenado y destaca lo importante", "Un formato sencillo ayuda a leer."),
        ("Un título largo está alineado a la derecha. ¿Qué alineación cambia mejor su aspecto?", "Centrada", "Es la alineación habitual de los títulos."),
    ],
    D=[
        arith("Una lista numerada empieza en el número 3 y tiene 6 elementos. ¿Con qué número termina?", "3+6-1", "Se suman los elementos al primer número y se resta 1 porque el primero ya cuenta.", ""),
        arith("Un título de 28 puntos se reduce a la mitad de su tamaño. ¿Cuántos puntos tiene ahora?", "28//2", "La mitad se obtiene dividiendo entre 2.", " puntos"),
    ],
    ctx=("Preparas un afiche de aviso para una exposición de trabajos de Tecnología con título, fecha, hora y tres cosas que se mostrarán. Escribe el formato de cada parte: fuente, tamaño, alineación y tipo de lista.", "Título: negrita, 28 puntos, centrado. Fecha y hora: 16 puntos, centrado. Lista con viñetas de lo que se mostrará, 14 puntos, alineada a la izquierda", "Se elige el formato según el uso de cada parte."),
    sc=[
        ("¿Qué es el formato?", "Cómo se ve el texto sin cambiar lo que dice", "No cambia el contenido."),
        ("¿Qué lista se usa si el orden importa?", "Numerada", "Muestra la secuencia."),
        ("¿Qué alineación se lee más fácil?", "A la izquierda", "Es la más usada en textos."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: instrucciones de 5 pasos para plantar una semilla en un vaso de papel. Documento 2: un cartel de «Biblioteca de aula» con el título, el horario (lunes y jueves de 10:00 a 10:30) y tres normas. Escribe cómo formatearías cada parte (fuente, tamaño, alineación, lista, negrita) y por qué.",
        "Documento 2: título 24 puntos centrado en negrita. Horario 14 puntos. Normas con viñetas, alineadas a la izquierda",
        ["formato por parte", "usa lista adecuada", "tamaños razonables", "explica por qué"],
        ["tabla con formato elegido y razón"],
        ["demasiados estilos", "negrita en todo"],
        "Pregunta: «¿qué tipo de lista necesita este contenido?». Revisa orden y destaque.",
    ),
    reinforce="Escribe una lista de cinco cosas que usas en la escuela y decide si va con viñetas o numerada.",
    extend="Explica por qué un formato sencillo suele comunicar mejor que uno muy recargado.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja y lápiz. Los ejemplos están descritos con texto en este cuaderno.",
    use="Aprenderé a incorporar imágenes, tablas, encabezados y columnas en un documento y a respetar los derechos de autor. Sirve para que el documento sea más claro y atractivo.",
    prior=["Sé dar formato a un texto.", "Sé que una fuente se anota.", "Sé qué es una tabla."],
    explain=[
        "Los elementos de diseño son recursos que ayudan a comunicar: imágenes, tablas, encabezado y pie de página, columnas, bordes y cuadros de texto. Cada uno debe tener un propósito: una imagen ilustra una idea, una tabla ordena datos y el encabezado repite el título del documento en cada página.",
        "Al insertar una imagen, se ajusta el tamaño sin deformarla: se cambia el ancho y el alto al mismo tiempo, en la misma proporción. Si una imagen mide 8 cm de ancho por 6 cm de alto y reduces el ancho a la mitad, el alto debe reducirse también a la mitad. Se agrega un texto alternativo que describe la imagen para quienes no pueden verla, y una fuente que indica su origen.",
        "Respeta los derechos de autor: usa imágenes propias o con permiso, y siempre indica la fuente. Para organizar, el texto puede ir en dos o tres columnas, como un diario. Los elementos se alinean y se dejan márgenes parejos. Pocas imágenes bien elegidas valen más que muchas sin sentido.",
    ],
    vocab=[("encabezado", "texto que se repite en la parte superior de cada página"), ("pie de página", "texto que se repite en la parte inferior de cada página"), ("proporción", "relación entre ancho y alto de una imagen"), ("texto alternativo", "descripción de una imagen para quienes no la ven"), ("columna", "franja vertical de texto en una página")],
    worked=[
        ("Reducir una imagen sin deformarla", "Una imagen mide 8 cm de ancho y 6 cm de alto. Reduces el ancho a 4 cm. ¿Cuánto debe medir el alto para no deformarla?", ["El ancho pasó de 8 a 4: se redujo a la mitad.", "El alto también se reduce a la mitad: 6 ÷ 2."], "3 cm"),
        ("Escribir texto alternativo", "Insertas la foto de un curso plantando un árbol. Escribe un texto alternativo.", ["Describo qué se ve.", "Debe ser breve y claro."], "«Un curso planta un árbol en el patio de la escuela»"),
    ],
    mistakes=[
        ("Estirar una imagen solo a lo ancho.", "Se deforma.", "Cambia el ancho y el alto en la misma proporción."),
        ("Usar una imagen de internet sin fuente ni permiso.", "No se respeta al autor.", "Usa imágenes propias o con permiso y anota la fuente."),
    ],
    R=[
        ("¿Qué texto se repite en la parte superior de cada página?", "El encabezado", "Se pone arriba."),
        ("¿Qué recurso ordena datos en filas y columnas?", "La tabla", "Organiza los datos en celdas."),
        ("¿Qué se anota para una imagen ajena?", "La fuente", "Reconoce al autor."),
    ],
    C=[
        ("¿Para qué sirve el texto alternativo?", "Para describir la imagen a quienes no la ven", "Es un aporte de accesibilidad."),
        ("¿Por qué no se estira una imagen solo a lo ancho?", "Porque se deforma", "Hay que mantener la proporción."),
        ("¿Por qué cada elemento debe tener un propósito?", "Para que ayude a comunicar y no solo adorne", "Evita recargar el documento."),
    ],
    A=[
        arith("Una imagen mide 12 cm de ancho y 8 cm de alto. Reduces el ancho a 6 cm. ¿Cuánto debe medir el alto?", "8//2", "El ancho se redujo a la mitad; el alto también.", " cm"),
        arith("Un documento tiene 15 páginas y el encabezado aparece en todas. ¿Cuántas veces se repite el encabezado?", "15", "Aparece una vez por página.", " veces"),
        ("¿Qué elemento usarías para ordenar los precios de cinco materiales? A una imagen, B una tabla.", "B", "La tabla organiza datos en filas y columnas."),
    ],
    Z=[
        ("Una imagen de 10 cm de ancho y 5 cm de alto se aumenta a 20 cm de ancho y 8 cm de alto. ¿Se deformó?", "Sí", "El alto debía ser 10 cm para mantener la proporción."),
        ("Una compañera usa una fotografía de un sitio web en su informe y no anota la fuente. ¿Qué debe hacer?", "Pedir permiso o buscar una imagen con permiso de uso y anotar la fuente, o usar una propia", "Debe respetar el derecho de autor."),
    ],
    D=[
        arith("Una imagen de 18 cm de ancho y 12 cm de alto se reduce a un tercio del ancho. ¿Cuánto mide de alto?", "12//3", "El alto también se reduce a un tercio.", " cm"),
        arith("Un texto de 600 palabras se acomoda en 3 columnas parejas. ¿Cuántas palabras tiene cada columna?", "600//3", "Se divide el total entre las columnas.", " palabras"),
    ],
    ctx=("Haces un informe sobre aves con una foto de una paloma que sacaste tú, de 15 cm de ancho y 10 cm de alto, que quieres poner a 9 cm de ancho. Calcula el alto, escribe el texto alternativo y la fuente.", "Alto: 6 cm (15 a 9 es × 3/5; 10 × 3/5 = 6). Texto alternativo: «Una paloma sobre una baranda». Fuente: foto propia", "Se mantiene la proporción y se cita la fuente."),
    sc=[
        ("¿Qué se hace para no deformar una imagen?", "Cambiar ancho y alto en la misma proporción", "Mantiene su forma."),
        ("¿Qué debe tener cada elemento de diseño?", "Un propósito", "Debe ayudar a comunicar."),
        ("¿Qué se anota de una imagen ajena?", "La fuente", "Reconoce al autor."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: un informe sobre plantas con una imagen de 16 cm por 12 cm que quieres poner a 8 cm de ancho, una tabla de 3 plantas y su altura, y un encabezado. Documento 2: un boletín del curso con dos columnas, una imagen de 10 cm por 6 cm a 5 cm de ancho y un pie de página con el nombre del curso. Calcula el alto de la imagen, describe la tabla o las columnas, escribe el texto alternativo y la fuente.",
        "Documento 2: la imagen queda de 5 cm por 3 cm. Texto alternativo: «Cuatro estudiantes presentan un trabajo». Fuente: foto del curso. Dos columnas y pie con el nombre del curso",
        ["calcula el alto sin deformar", "describe la tabla o las columnas", "texto alternativo", "fuente indicada"],
        ["boceto del documento con cálculos"],
        ["deformar la imagen", "olvidar la fuente"],
        "Pregunta: «¿cambiaste el ancho y el alto en la misma proporción?». Revisa el cálculo.",
    ),
    reinforce="Dibuja una página con una imagen, un título y dos columnas de texto.",
    extend="Explica cuándo una tabla comunica mejor que un párrafo, con un ejemplo.",
)

# ------------------------------------------------------------------ OA 06, clase 5
reg(
    OA6, 5,
    materials="Hoja y lápiz. Los textos con errores están escritos en este cuaderno.",
    use="Aprenderé a revisar un documento, a corregir errores que el programa no detecta y a guardar versiones y copias. Sirve para entregar un trabajo correcto y no perderlo.",
    prior=["Sé editar y dar formato.", "Sé usar tildes y puntuación.", "Sé guardar un archivo con nombre claro."],
    explain=[
        "Revisar es leer el documento para encontrar y corregir errores. El revisor de ortografía subraya las palabras que no existen, pero no detecta todo. Por ejemplo, no marca error en «hecho» cuando debía ser «echo», ni en «a ver» cuando debía ser «haber». Por eso, además del revisor, se lee el texto en voz alta y se pide a otra persona que lo lea.",
        "Una buena revisión sigue una lista: ortografía y tildes, puntuación, orden de las ideas, formato parejo, imágenes con fuente y nombre del archivo. Se revisa primero el contenido y después el formato. La vista previa de impresión muestra cómo se verá en papel antes de gastar hojas. Si se imprime, se puede usar ambos lados de la hoja.",
        "Guardar versiones es conservar copias del documento en distintos momentos, con nombres como «informe_v1» e «informe_v2». Así puedes volver a una anterior si algo sale mal. También se guarda una copia de seguridad en otro lugar. Para compartir, se puede guardar el documento como PDF, que mantiene el formato en cualquier computador.",
    ],
    vocab=[("revisar", "leer un documento para encontrar y corregir errores"), ("revisor ortográfico", "herramienta que marca palabras mal escritas"), ("versión", "copia del documento en un momento determinado"), ("copia de seguridad", "copia guardada en otro lugar por si se pierde el original"), ("PDF", "formato que mantiene el aspecto del documento en cualquier computador")],
    worked=[
        ("Errores que el revisor no marca", "La oración «Voy a haber si llegó mi amiga» no tiene palabras inexistentes. ¿Está correcta?", ["Todas las palabras existen, así que el revisor no marca nada.", "Debe decir «a ver»."], "No; debe decir «a ver», y el revisor no lo detecta"),
        ("Nombrar versiones", "Tienes la primera versión del informe y haces cambios importantes. ¿Cómo nombras la segunda: A «informe_v2» o B «informe»?", ["Si uso el mismo nombre, borro la primera versión.", "Con v2 conservo ambas."], "A"),
    ],
    mistakes=[
        ("Confiar solo en el revisor ortográfico.", "No detecta todos los errores.", "Lee en voz alta y pide a otra persona que lea."),
        ("Guardar siempre con el mismo nombre.", "Se pierde la versión anterior.", "Guarda versiones con nombres distintos."),
    ],
    R=[
        ("¿El revisor ortográfico detecta todos los errores?", "No", "No marca palabras existentes mal usadas."),
        ("¿Qué formato mantiene el aspecto del documento en cualquier computador?", "PDF", "No cambia el formato."),
        ("¿Dónde se guarda una copia de seguridad?", "En otro lugar", "Así no se pierde si falla el original."),
    ],
    C=[
        ("¿Por qué pedir a otra persona que lea tu texto?", "Porque ve errores que tú no ves", "Otra mirada ayuda."),
        ("¿Para qué sirve la vista previa de impresión?", "Para ver cómo se verá en papel antes de imprimir", "Así se evita gastar hojas."),
        ("¿Para qué sirven las versiones?", "Para volver a una versión anterior", "Se conserva el trabajo."),
    ],
    A=[
        ("Corrige la oración: «Mañana iremos a haber el museo». ¿Qué palabra se cambia?", "«haber» por «a ver»", "El verbo es «ver» con la preposición «a»."),
        ("Elige la oración correcta. A «Ayer hize la tarea», B «Ayer hice la tarea».", "B", "El verbo hacer se escribe «hice»."),
        arith("Un informe de 12 páginas se imprime por ambos lados de la hoja. ¿Cuántas hojas se usan?", "12//2", "Cada hoja tiene dos páginas.", " hojas"),
    ],
    Z=[
        ("Un compañero guardó su informe como «informe» tres veces seguidas con cambios distintos. ¿Qué problema tiene?", "Perdió las versiones anteriores", "Cada guardado reemplazó al anterior."),
        ("Dos estudiantes dicen que «el revisor no marcó nada, así que mi texto está perfecto». ¿Es seguro?", "No", "Hay errores que el revisor no marca."),
    ],
    D=[
        arith("Guardas una versión cada 10 minutos durante 1 hora. ¿Cuántas versiones guardas?", "60//10", "Se divide el tiempo entre el intervalo.", " versiones"),
        arith("Un informe de 20 páginas se imprime por ambos lados. Si cada hoja se usa una vez, ¿cuántas hojas se ahorran frente a imprimir una página por hoja?", "20-20//2", "Una página por hoja usa 20 hojas y por ambos lados, 10.", " hojas"),
    ],
    ctx=("Revisas esta frase de un informe: «Ayer vimos como el agua se evaporo en el vaso». Escribe cómo debe quedar y qué dos errores corriges.", "«Ayer vimos cómo el agua se evaporó en el vaso». Errores: falta la tilde de «cómo» y de «evaporó»", "«Cómo» exclamativo o interrogativo lleva tilde y «evaporó» es verbo en pasado."),
    sc=[
        ("¿Qué errores no detecta el revisor?", "Palabras que existen pero están mal usadas", "El programa solo marca palabras inexistentes."),
        ("¿Qué se guarda con nombres como v1 y v2?", "Versiones del documento", "Conservan el trabajo."),
        ("¿Qué formato se usa para compartir manteniendo el aspecto?", "PDF", "No cambia en otros computadores."),
    ],
    open_task=(
        "Escoge un texto para revisar. Texto 1: «El curso aprobecho la tarde para ver como se hace una cometa. Hecha en cartulina, la cometa vuela mui bien». Texto 2: «Ayer el profesor nos dijo que hiba a traer un mapa para ver donde queda el rio». Corrige los errores de ortografía y tildes, escribe el texto final y cuántos errores corregiste. Escribe también cómo guardarías la versión corregida.",
        "Texto 1: «El curso aprovechó la tarde para ver cómo se hace una cometa. Hecha en cartulina, la cometa vuela muy bien». 3 palabras corregidas. Archivo: cometa_v2",
        ["encuentra los errores", "escribe el texto corregido", "cuenta los errores", "nombra una versión"],
        ["texto corregido con conteo de errores"],
        ["dejar errores sin ver", "guardar sin versión"],
        "Pregunta: «¿lo leíste en voz alta?». Revisa los errores que el revisor no marca.",
    ),
    reinforce="Lee en voz alta una página de un texto tuyo y anota tres errores o mejoras.",
    extend="Explica por qué guardar versiones es útil cuando varias personas trabajan en un mismo documento.",
)
