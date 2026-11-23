"""Matemática EPJA Nivel 1 básico, módulo 4: OAD-13 clases 1 a 4 (del gráfico de cuadros al gráfico de barras). Datos de ejemplo, inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Hoja, lápiz de mina y regla. Si quieres, lápices de colores. Todo se hace en papel; los gráficos de este cuaderno se dibujan con cuadros ■ y tablas. Todos los datos son de ejemplo, inventados."
build = make_build(MATERIALS)

O13 = "EPJA-MATE-NB1-OAD-13"

# ===================================================== OAD-13 clase 1
F = ("Datos de ejemplo. Una cuadrilla de 20 trabajadores anotó cómo llega al trabajo. Cada ■ es una persona. "
     "Bus: ■■■■■■■■. Metro: ■■■■■■. A pie: ■■■■. Bicicleta: ■■.")
build(
    O13, 1, F,
    use="Voy a leer un gráfico de cuadros de colores y a contar cuántas personas hay en cada fila.",
    prior=["Sé contar objetos.", "Sé sumar números pequeños.", "Sé que una lista puede tener nombres y cantidades."],
    explain=[
        "Un gráfico de cuadros muestra cantidades con dibujos iguales. En esta ficha cada cuadro ■ es una persona. Para leerlo, mira el nombre de cada fila y cuenta los cuadros de esa fila. Más cuadros significa más personas.",
        "Los cuadros deben tener el mismo tamaño y estar pegados, sin espacios. Así comparas las filas con solo mirar cuál es más larga. La fila más larga es la categoría que más se repite en el grupo.",
        "Contar el vuelto, los turnos o las cajas es una tarea de todos los días. Este gráfico es otra forma de contar y de mostrar ese conteo a otras personas. Antes de leer, siempre busca qué vale cada cuadro: en este cuaderno, vale uno.",
    ],
    vocab=[("gráfico", "dibujo que muestra datos para leerlos rápido"), ("fila", "línea de cuadros hacia el lado"), ("categoría", "grupo con nombre, como «bus» o «metro»"), ("cuadro", "unidad del gráfico; aquí vale una persona"), ("dato", "información anotada, como un número o un nombre"), ("total", "resultado de juntar todas las cantidades")],
    worked=[
        ("Contar una fila", "En la ficha, ¿cuántas personas llegan en metro?", ["Busca la fila que dice «Metro».", "Cuenta sus cuadros: ■■■■■■ son 6."], "6 personas"),
        ("Hallar el total", "En la ficha, ¿cuántas personas anotó la cuadrilla en total?", ["Cuenta cada fila: 8, 6, 4 y 2.", "Suma: 8 + 6 = 14; 14 + 4 = 18; 18 + 2 = 20."], "20 personas"),
    ],
    mistakes=[("Contar los espacios y no los cuadros de la fila.", "Se mira el largo de la fila sin fijarse en que cada cuadro es una persona.", "Toca cada cuadro con el lápiz y di el número en voz baja."),
              ("Decir que «bicicleta» es la más usada porque aparece al final.", "Se confunde el orden de la lista con la cantidad.", "Compara el largo de las filas, no su lugar.")],
    T=[
        ("abc", "{F} ¿Qué representa cada cuadro?", "Una persona", "Un bus", "Un día de trabajo", "La ficha dice que cada cuadro es una persona de la cuadrilla."),
        ("{F} ¿Cuántas personas llegan a pie?", "4 personas", "La fila «A pie» tiene cuatro cuadros, uno por cada persona."),
        ("abc", "{F} ¿Qué medio usan menos personas?", "Bicicleta", "Bus", "Metro", "Bicicleta tiene la fila más corta, solo dos cuadros."),
        ("=", "{F} ¿Cuántas personas hay en total en la cuadrilla?", "8+6+4+2", "Se suman los cuadros de las cuatro filas.", " personas"),
        ("abc", "{F} ¿Cuál es el medio más usado?", "Bus", "Metro", "A pie", "La fila del bus es la más larga, con ocho cuadros."),
        ("=", "{F} ¿Cuántas personas más van en bus que a pie?", "8-4", "Se resta la fila más corta de la más larga.", " personas"),
        ("ab", "{F} Comparado con el bus, la fila del metro tiene", "menos cuadros", "más cuadros", "El metro tiene 6 cuadros y el bus tiene 8, por eso tiene menos."),
        ("=", "{F} Dos personas que van en bus pasan al metro. ¿Cuántas irán en metro?", "6+2", "Se suman las dos personas a la fila del metro.", " personas"),
        ("abc", "Una compañera dice: «la fila del bus es más larga, así que hay más gente en bus». ¿Es correcto?", "Sí, más cuadros quiere decir más personas", "No, todas las filas tienen la misma gente", "No, la fila más corta tiene más gente", "Con cuadros iguales, una fila más larga representa más personas."),
        ("=", "{F} Si 7 personas más empiezan a ir a pie, ¿cuántas irán a pie?", "4+7", "Se suman las nuevas personas a la fila A pie.", " personas"),
        ("=", "{F} ¿Cuántas personas NO van en bus?", "6+4+2", "Se suman las filas que no son bus.", " personas"),
        ("ab", "{F} Alguien dice: «la mitad de la cuadrilla va en bus». ¿Es cierto?", "No: la mitad de 20 es 10 y en bus van 8", "Sí: el bus es la fila más larga", "La mitad de 20 es 10; como en bus van 8, no llegan a la mitad."),
        ("abc", "{F} ¿Cuántas filas tiene el gráfico?", "4", "20", "8", "Hay una fila por cada medio de transporte: bus, metro, a pie y bicicleta."),
    ],
    ctx=("=", "Una jefa de turno anotó con cuadros cuántos de sus 20 trabajadores llegan en cada medio: 8 en bus, 6 en metro, 4 a pie y 2 en bicicleta. Si el bus se atrasa y 8 personas llegan tarde, ¿cuántas llegan a tiempo?", "20-8", "Se resta del total las personas que van en bus.", " personas"),
    sc=[("En un gráfico de cuadros, ¿cómo sabes qué categoría es la más grande?", "Es la fila con más cuadros", "Más cuadros representa más cantidad de personas o cosas."),
        ("¿Qué debes buscar antes de leer un gráfico de cuadros?", "Cuánto vale cada cuadro", "Sin ese valor no sabes qué cantidad representa cada cuadro."),
        ("Una fila tiene 5 cuadros y otra 3. ¿Cuántos cuadros más tiene la primera?", "2 cuadros más", "Se restan 5 − 3 para comparar las dos filas.")],
    op=("Anota con cuadros ■ cómo llegan al trabajo 12 personas de ejemplo: 5 en bus, 4 en metro y 3 a pie. Haz una fila por medio y escribe una frase que diga cuál es el más usado.",
        "Bus: ■■■■■. Metro: ■■■■. A pie: ■■■. Frase: «El bus es el más usado, con 5 personas».",
        ["dibuja una fila por categoría", "usa la cantidad correcta de cuadros", "escribe una frase correcta"],
        ["hoja con las tres filas y la frase"],
        ["dejar espacios entre los cuadros", "cambiar la cantidad de cuadros de una fila"],
        "Pregunta: «¿cuántas personas hay en total en tu gráfico?». Si la suma no da 12, pídele que cuente otra vez."),
    reinforce="Haz un gráfico de cuadros con tres cosas de tu casa (por ejemplo, 4 sillas, 2 mesas y 3 camas).",
    extend="Explica por qué es importante que todos los cuadros tengan el mismo tamaño.",
)

# ===================================================== OAD-13 clase 2
F = ("Datos de ejemplo. Una feria vecinal contó cuántos puestos vende cada producto. Cada ■ es un puesto. "
     "Verduras: ■■■■■■■. Frutas: ■■■■■. Ropa: ■■■■. Panes: ■■■.")
build(
    O13, 2, F,
    use="Voy a pasar un gráfico de cuadros a un gráfico de barras y a ver qué cambia.",
    prior=["Sé leer un gráfico de cuadros.", "Sé contar hasta 20.", "Sé que más cuadros es más cantidad."],
    explain=[
        "Un gráfico de barras dibuja cada categoría como una barra. La barra reemplaza a los cuadros pegados: si una fila tenía 7 cuadros, la barra llega hasta la marca 7. Con muchos datos, dibujar una barra es más rápido que dibujar cada cuadro.",
        "En el gráfico de barras que usamos, las barras se paran sobre una línea horizontal y suben. A un lado hay una línea con números, que se llama escala. La altura de la barra se lee en la escala: eso te dice la cantidad.",
        "Pasar de cuadros a barras no cambia los datos; cambia la forma de mostrarlos. Por eso, una fila de 7 cuadros y una barra de altura 7 dicen lo mismo. Si no coinciden, hay un error que debes buscar.",
    ],
    vocab=[("barra", "rectángulo cuya altura muestra una cantidad"), ("escala", "línea con números para leer la altura de las barras"), ("altura", "qué tan alta llega la barra"), ("eje horizontal", "línea de abajo, donde van los nombres"), ("eje vertical", "línea del lado, donde van los números"), ("equivale", "vale lo mismo")],
    worked=[
        ("De cuadros a barra", "En la ficha, Frutas tiene ■■■■■. ¿Hasta qué número sube su barra?", ["Cuenta los cuadros de Frutas: son 5.", "La barra llega hasta la marca 5 de la escala."], "Hasta 5"),
        ("De barra a cuadros", "Una barra de Ropa llega hasta 4. ¿Cuántos cuadros tenía su fila?", ["La altura de la barra es la cantidad: 4.", "La fila tenía cuatro cuadros: ■■■■."], "4 cuadros"),
    ],
    mistakes=[("Dibujar la barra hasta un número distinto del conteo.", "Se cuenta bien, pero se marca en un número equivocado de la escala.", "Después de dibujar, compara la altura con el número de cuadros."),
              ("Pensar que una barra más ancha vale más.", "Se mira el ancho en vez de la altura.", "La cantidad se lee solo en la altura; todas las barras deben tener el mismo ancho.")],
    T=[
        ("abc", "{F} ¿Hasta qué número sube la barra de Verduras?", "7", "5", "4", "Verduras tiene siete cuadros, así que su barra llega a 7."),
        ("{F} ¿Hasta qué número sube la barra de Panes?", "3", "Panes tiene tres cuadros, por eso su barra llega hasta 3."),
        ("abc", "¿Qué parte del gráfico de barras sirve para leer las cantidades?", "La escala", "El color", "El ancho", "La escala es la línea con números donde se lee la altura."),
        ("ab", "Una barra llega a 6 en la escala. ¿Cuántos cuadros tenía su fila?", "6 cuadros", "3 cuadros", "La altura de la barra es la cantidad, y 6 equivale a seis cuadros."),
        ("abc", "{F} ¿Qué producto tendrá la barra más alta?", "Verduras", "Frutas", "Panes", "La barra más alta es la del producto con más puestos: verduras."),
        ("=", "{F} Se dibujan las barras de Verduras y de Panes. ¿Cuántas marcas de altura las separan?", "7-3", "La diferencia entre alturas es una resta.", " marcas"),
        ("=", "{F} ¿Cuántos puestos hay en total en la feria?", "7+5+4+3", "Se suman las alturas de las cuatro barras.", " puestos"),
        ("abc", "Una barra de Ropa llega a 5, pero su fila tiene 4 cuadros. ¿Qué pasó?", "Hay un error al dibujar la barra", "Los datos cambiaron solos", "Está bien, las barras no coinciden con los cuadros", "La barra debe llegar exactamente a la cantidad de cuadros; hay que corregirla."),
        ("=", "{F} Llegan 2 puestos más de panes. ¿Hasta qué altura sube la barra de Panes?", "3+2", "Se suman los puestos nuevos a la cantidad anterior.", " marcas"),
        ("abc", "Una persona dibujó la barra de Frutas más ancha que las demás. ¿Cambia la cantidad?", "No, la cantidad se lee en la altura", "Sí, más ancha vale más", "Sí, vale el doble", "El ancho es solo forma; la cantidad la da la altura de la barra."),
        ("ab", "{F} ¿Qué dos barras quedan de la misma altura si Panes sube 1 puesto?", "Panes y Ropa", "Panes y Verduras", "Panes pasa a 4 y Ropa tiene 4, por lo tanto igualan altura."),
        ("=", "{F} ¿Cuántos puestos más tiene Verduras que Frutas?", "7-5", "Se compara restando la cantidad menor de la mayor.", " puestos"),
        ("abc", "{F} ¿Cuántas barras tendrá el gráfico?", "4", "7", "19", "Se dibuja una barra por cada producto: verduras, frutas, ropa y panes."),
    ],
    ctx=("=", "La dirigente de una feria vecinal pasó a barras los datos de 4 productos: 7, 5, 4 y 3 puestos. Para el cartel necesita saber cuántos puestos hay en total. ¿Cuántos son?", "7+5+4+3", "Se suman las alturas de todas las barras.", " puestos"),
    sc=[("¿Qué se lee en la altura de una barra?", "La cantidad de esa categoría", "La altura sobre la escala indica cuánto hay."),
        ("Una fila de 6 cuadros, ¿hasta dónde sube su barra?", "Hasta 6", "La barra llega al mismo número que el conteo."),
        ("¿Qué línea del gráfico de barras tiene números?", "La escala del eje vertical", "Allí se leen las alturas de las barras.")],
    op=("Pasa a barras estos datos de ejemplo: Lunes: ■■■■■■ (6 clientes). Martes: ■■■■ (4). Miércoles: ■■■■■ (5). Dibuja una línea con números del 0 al 7 y una barra por día.",
        "Barras con alturas 6, 4 y 5, todas del mismo ancho, paradas sobre una línea y con los nombres de los días debajo.",
        ["alturas correctas: 6, 4 y 5", "barras del mismo ancho", "nombres escritos bajo cada barra"],
        ["hoja con las tres barras y la escala"],
        ["alturas distintas al conteo", "barras de ancho distinto"],
        "Pregunta: «¿qué día tuvo más clientes y cómo lo ves?». Si responde por el color, vuelve a mirar la altura."),
    reinforce="Dibuja de nuevo la fila de cuadros de Verduras y su barra, una al lado de la otra, y compáralas.",
    extend="Explica una ventaja de la barra sobre los cuadros cuando hay 30 elementos.",
)

# ===================================================== OAD-13 clase 3
F = ("Datos de ejemplo. Gráfico de barras: «Clientes por día de la semana en un local de lavandería». "
     "Eje horizontal: Lunes, Martes, Miércoles, Jueves, Viernes. Eje vertical (escala de 1 en 1): clientes. "
     "Alturas: Lunes 6, Martes 4, Miércoles 5, Jueves 8, Viernes 9.")
build(
    O13, 3, F,
    use="Voy a reconocer las partes de un gráfico de barras: título, ejes, escala y barras.",
    prior=["Sé que una barra muestra una cantidad.", "Sé leer números hasta 20.", "Sé comparar dos números."],
    explain=[
        "Un gráfico de barras tiene partes que siempre debes buscar. El título dice de qué trata. El eje horizontal, el de abajo, muestra las categorías, por ejemplo los días. El eje vertical, el del lado, muestra la escala con números.",
        "Las barras salen del eje horizontal hacia arriba. Su altura se compara con la escala para saber la cantidad. Si la barra termina justo en una marca, lees ese número. Cada eje debe tener un rótulo, que es una palabra que explica qué mide: días, clientes.",
        "Antes de sacar conclusiones, lee el título y los rótulos. Un gráfico sin título o sin rótulos puede confundir. Con boletas, listas o carteles el hábito es el mismo: primero ubica de qué habla el gráfico, después lee los números.",
    ],
    vocab=[("título", "frase que dice de qué trata el gráfico"), ("eje horizontal", "línea de abajo, con las categorías"), ("eje vertical", "línea del lado, con la escala"), ("rótulo", "palabra que explica qué mide cada eje"), ("escala", "números para leer la altura"), ("marca", "rayita de la escala con su número")],
    worked=[
        ("Leer una barra", "En la ficha, ¿cuántos clientes hubo el jueves?", ["Busca la barra de Jueves en el eje de abajo.", "Su altura llega a la marca 8."], "8 clientes"),
        ("Hallar el día con más clientes", "¿Qué día tuvo más clientes?", ["Compara las alturas: 6, 4, 5, 8 y 9.", "La más alta es 9, que corresponde al viernes."], "Viernes"),
    ],
    mistakes=[("Leer una barra sin mirar la escala.", "Se mira solo el dibujo y se adivina el número.", "Baja desde la punta de la barra hasta la escala y lee la marca."),
              ("Confundir el eje de las categorías con el de la escala.", "No se leyeron los rótulos de los ejes.", "Los nombres van abajo; los números, al lado.")],
    T=[
        ("abc", "{F} ¿Qué dice el título del gráfico?", "Clientes por día de la semana en un local de lavandería", "Alturas de las barras", "Viernes con 9 clientes", "El título es la frase que describe de qué trata el gráfico."),
        ("abc", "{F} ¿Qué se muestra en el eje horizontal?", "Los días de la semana", "Los números de la escala", "El título", "El eje de abajo tiene las categorías, aquí los días."),
        ("{F} ¿Cuántos clientes hubo el martes?", "4 clientes", "La barra del martes llega a la marca 4 de la escala."),
        ("abc", "{F} ¿Qué día tuvo menos clientes?", "Martes", "Lunes", "Viernes", "La barra más baja es la del martes, con 4 clientes."),
        ("=", "{F} ¿Cuántos clientes más hubo el viernes que el lunes?", "9-6", "Se resta la altura del lunes a la del viernes.", " clientes"),
        ("ab", "{F} ¿Qué mide el eje vertical?", "Los clientes", "Los días", "En el eje del lado está la escala, y cada número es una cantidad de clientes."),
        ("=", "{F} ¿Cuántos clientes hubo entre lunes y miércoles juntos?", "6+4+5", "Se suman las alturas de las tres barras.", " clientes"),
        ("abc", "{F} ¿Cuántas barras tiene el gráfico?", "5", "9", "8", "Hay una barra por cada día, y son cinco días."),
        ("=", "{F} ¿Cuántos clientes hubo en la semana completa?", "6+4+5+8+9", "Se suman las cinco alturas.", " clientes"),
        ("abc", "Un gráfico no tiene título ni rótulos. ¿Qué problema tiene?", "No se sabe de qué trata ni qué mide", "Las barras no pueden leerse nunca", "Tiene demasiados números", "Sin título ni rótulos no se entiende qué datos se muestran."),
        ("ab", "{F} ¿Qué días superan los 7 clientes?", "Jueves y viernes", "Lunes y martes", "Solo Jueves (8) y Viernes (9) pasan de 7; las otras barras son más bajas."),
        ("=", "{F} Si el miércoles llegaran 3 clientes más, ¿cuántos habría ese día?", "5+3", "Se suman los clientes nuevos a la altura del miércoles.", " clientes"),
        ("abc", "{F} ¿En qué marca de la escala termina la barra del lunes?", "6", "4", "9", "La barra del lunes llega a la marca 6."),
    ],
    ctx=("=", "La dueña de una lavandería de ejemplo mira su gráfico: lunes 6 y martes 4 clientes. Quiere saber cuántos clientes hubo esos dos días juntos para pedir más detergente. ¿Cuántos fueron?", "6+4", "Se suman las alturas de las dos barras.", " clientes"),
    sc=[("¿Dónde ves de qué trata un gráfico?", "En el título", "El título resume el tema del gráfico."),
        ("¿Qué eje muestra la escala numérica?", "El eje vertical", "Allí están los números que se comparan con la altura."),
        ("¿Qué es un rótulo?", "Una palabra que explica qué mide un eje", "El rótulo evita confundir categorías con cantidades.")],
    op=("Haz un gráfico de barras con estos datos de ejemplo: Panadería abierta Lunes 5 horas, Martes 6, Miércoles 4. Escribe título, rótulos de ambos ejes y la escala del 0 al 7.",
        "Título: «Horas de atención por día». Eje de abajo rotulado «Días»; eje del lado rotulado «Horas». Barras con alturas 5, 6 y 4.",
        ["escribe un título", "rotula los dos ejes", "dibuja alturas correctas"],
        ["hoja con el gráfico completo"],
        ["olvidar el título", "olvidar el rótulo de un eje"],
        "Pregunta: «¿qué día se atiende más horas?». Si no lo ve, pídele señalar la barra más alta."),
    reinforce="Busca un gráfico en un diario o afiche y nombra su título y sus dos ejes.",
    extend="Explica qué pasaría si dos gráficos tuvieran los mismos datos pero uno no tuviera rótulos.",
)

# ===================================================== OAD-13 clase 4
F = ("Datos de ejemplo. Tabla: «Paquetes entregados por un repartidor en 5 jornadas». Escala de 1 en 1. "
     "Jornada 1: 7 paquetes. Jornada 2: 10. Jornada 3: 9. Jornada 4: 12. Jornada 5: 6.")
build(
    O13, 4, F,
    use="Voy a construir un gráfico de barras desde una tabla y leer la altura de cada barra.",
    prior=["Sé las partes del gráfico de barras.", "Sé contar hasta 20.", "Sé comparar números."],
    explain=[
        "Para construir un gráfico de barras sigue pasos fijos. Primero escribe el título. Después dibuja el eje de abajo con las categorías y el eje del lado con la escala. La escala parte en cero y sube de uno en uno hasta un número un poco mayor que el dato más grande.",
        "Luego dibuja cada barra. La barra de una categoría sube hasta el número de su dato. Todas las barras tienen el mismo ancho y no se tocan. Al final rotula los ejes: abajo «Jornadas» y al lado «Paquetes».",
        "En esta ficha el dato mayor es 12, por eso la escala debe llegar al menos hasta 12. Si la escala llega solo hasta 10, la barra de 12 no cabe. Comprueba siempre que cada barra coincida con su número de la tabla.",
    ],
    vocab=[("tabla", "lista ordenada de categorías y sus cantidades"), ("escala", "números del eje vertical"), ("cero", "punto donde parten las barras"), ("construir", "dibujar el gráfico paso a paso"), ("jornada", "día o turno de trabajo"), ("coincidir", "ser iguales los datos y el dibujo")],
    worked=[
        ("Elegir la escala", "En la ficha, el dato mayor es 12. ¿Hasta qué número debe llegar la escala?", ["Busca el dato más grande: 12.", "La escala debe llegar al menos a 12; sirve hasta 13 o 14."], "Al menos hasta 12"),
        ("Dibujar una barra", "¿Hasta dónde sube la barra de la jornada 5?", ["La tabla dice 6 paquetes.", "Se dibuja una barra que sube desde 0 hasta la marca 6."], "Hasta la marca 6"),
    ],
    mistakes=[("Empezar la escala en un número distinto de cero.", "Se parte del primer dato y la barra no se ve completa.", "Escribe 0 al inicio de la escala y avanza de uno en uno."),
              ("Hacer barras de anchos distintos.", "Se dibuja a mano y sin cuidado.", "Marca el mismo ancho para todas con la regla.")],
    T=[
        ("abc", "{F} ¿Dónde parten todas las barras?", "En el cero de la escala", "En el título", "En el dato mayor", "Las barras parten del cero y suben hasta su dato."),
        ("{F} ¿Hasta qué número sube la barra de la jornada 2?", "10", "La tabla dice que la jornada 2 tuvo diez paquetes."),
        ("abc", "{F} ¿Cuál es el dato mayor de la tabla?", "12", "7", "10", "El dato más grande es 12, de la jornada 4."),
        ("=", "{F} ¿Cuántos paquetes entregó el repartidor en las jornadas 1 y 2 juntas?", "7+10", "Se suman las alturas de las dos barras.", " paquetes"),
        ("ab", "{F} Para que quepa toda la información, la escala debe llegar al menos a", "12", "9", "La barra más alta mide 12; si la escala termina antes, esa barra no cabe."),
        ("abc", "{F} ¿Qué jornada tendrá la barra más baja?", "Jornada 5", "Jornada 1", "Jornada 3", "Seis paquetes es el dato menor, de la jornada 5."),
        ("=", "{F} ¿Cuántos paquetes más se entregaron en la jornada 4 que en la jornada 5?", "12-6", "Se resta el dato menor del mayor.", " paquetes"),
        ("=", "{F} ¿Cuántos paquetes entregó en total en las cinco jornadas?", "7+10+9+12+6", "Se suman los cinco datos de las barras.", " paquetes"),
        ("abc", "Una persona dibujó la barra de la jornada 3 hasta 10. ¿Está bien?", "No, debe llegar hasta 9", "Sí, 10 está cerca de 9", "Sí, porque 10 es el dato de otra jornada", "Cada barra debe coincidir con su dato exacto; la jornada 3 tuvo 9."),
        ("=", "{F} Si en la jornada 1 se hubieran entregado 5 paquetes más, ¿cuántos habría?", "7+5", "Se suma el aumento a la altura de la jornada 1.", " paquetes"),
        ("abc", "¿Qué se escribe primero al construir un gráfico de barras?", "El título", "El total", "La conclusión", "El título dice de qué trata y se escribe antes de dibujar."),
        ("=", "{F} ¿Cuántos paquetes más que la jornada 1 se entregaron en las jornadas 2 y 3 juntas?", "10+9-7", "Se suman las dos jornadas y luego se resta la jornada 1.", " paquetes"),
        ("ab", "{F} ¿Las barras de las jornadas 2 y 3 tienen la misma altura?", "No: 10 y 9 son alturas distintas", "Sí, ambas son muy altas", "Una llega a 10 y la otra a 9, por eso no son iguales."),
    ],
    ctx=("=", "Un repartidor de ejemplo anotó 7, 10, 9, 12 y 6 paquetes en cinco jornadas. Su jefa quiere el total de paquetes de la semana para el informe. ¿Cuántos son?", "7+10+9+12+6", "Se suman todos los datos de la tabla.", " paquetes"),
    sc=[("¿En qué número parte la escala?", "En cero", "Las barras parten desde cero para mostrar la cantidad completa."),
        ("¿Cómo eliges hasta dónde llega la escala?", "Debe llegar al menos al dato mayor", "Si no llega, la barra más alta no cabe."),
        ("¿Cómo comprobar tu gráfico terminado?", "Comparar cada barra con su dato de la tabla", "Esa comparación detecta errores de altura.")],
    op=("Construye un gráfico de barras con estos datos de ejemplo: kilos de pan vendidos Lunes 8, Martes 11, Miércoles 6, Jueves 9. Escala del 0 al 12, título y rótulos.",
        "Título: «Kilos de pan vendidos por día». Barras de altura 8, 11, 6 y 9, mismo ancho, ejes rotulados «Días» y «Kilos».",
        ["escala correcta del 0 al 12", "barras con alturas exactas", "título y rótulos presentes"],
        ["hoja con el gráfico y la tabla al lado"],
        ["escala que no parte en cero", "alturas distintas a los datos"],
        "Pregunta: «¿cómo sabes que tu gráfico está bien?». Que compare cada barra con la tabla."),
    reinforce="Haz una tabla de cuatro datos tuyos de la semana (por ejemplo, vasos de agua por día) y dibuja sus barras.",
    extend="Explica por qué una escala que parte en 5 puede engañar a quien lee el gráfico.",
)
