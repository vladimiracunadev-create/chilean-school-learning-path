"""Matemática EPJA Nivel 1 básico, módulo 4: OAD-14 clases 1 a 4 (marcas de recuento, tablas de frecuencia absoluta y paso de la tabla al gráfico de barras). Datos de ejemplo, inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Hoja, lápiz de mina y regla. Todo se hace en papel; las listas, las marcas de recuento y las tablas están escritas en cada ficha. Todos los datos son de ejemplo, inventados."
build = make_build(MATERIALS)

O14 = "EPJA-MATE-NB1-OAD-14"

# ===================================================== OAD-14 clase 1
F = ("Datos de ejemplo. Un guardia anotó con marcas de recuento cuántas personas entraron a un edificio cada hora. "
     "Cada IIIII es un grupo cerrado de 5. 8:00 → IIIII II. 9:00 → IIIII IIIII I. 10:00 → IIIII III. 11:00 → IIII.")
build(
    O14, 1, F,
    use="Voy a contar con marcas de recuento, agrupando de a cinco, y a leer cuántas veces ocurre algo.",
    prior=["Sé contar hasta 30.", "Sé contar de 5 en 5.", "Sé sumar números pequeños."],
    explain=[
        "Las marcas de recuento sirven para contar mientras algo ocurre: personas que entran, llamadas, pedidos. Cada vez que ocurre algo, se anota una rayita I. Contar rayitas sueltas es lento, por eso se agrupan de a cinco: IIII y una quinta que cierra el grupo.",
        "Para leer las marcas, cuenta los grupos de cinco de a 5, 10, 15, y luego suma las rayitas sueltas. Por ejemplo, IIIII IIIII II son dos grupos de 5 y 2 sueltas: 5 + 5 + 2 = 12. Así no pierdes la cuenta.",
        "Contar de a cinco es común cuando se agrupan billetes o cajas. Las marcas de recuento ponen ese hábito en papel. El resultado de contar cuántas veces ocurre algo se llama frecuencia, y lo vas a usar para armar tablas y gráficos.",
    ],
    vocab=[("marca de recuento", "rayita que se anota cada vez que ocurre algo"), ("grupo de cinco", "cinco rayitas agrupadas para contar rápido"), ("recuento", "conteo de cuántas veces ocurre algo"), ("frecuencia", "cuántas veces aparece un dato"), ("suelta", "marca que no completa un grupo de cinco"), ("dato", "cada cosa anotada")],
    worked=[
        ("Leer marcas", "En la ficha, ¿cuántas personas entraron a las 8:00?", ["Hay un grupo de 5 y dos sueltas.", "Suma: 5 + 2 = 7."], "7 personas"),
        ("Anotar con marcas", "Anota 13 con marcas de recuento.", ["Dibuja dos grupos de cinco: IIIII IIIII.", "Agrega tres sueltas: III."], "IIIII IIIII III"),
    ],
    mistakes=[("Contar cada grupo cerrado como una sola marca.", "Se olvida que un grupo vale cinco.", "Cuenta los grupos de a cinco: 5, 10, 15."),
              ("Anotar 10 rayitas seguidas sin agrupar.", "Se pierde la cuenta al contar después.", "Cierra cada grupo en la quinta marca antes de empezar otro.")],
    T=[
        ("abc", "¿Cuántas rayitas tiene un grupo cerrado?", "5", "4", "10", "Un grupo cerrado completa cinco rayitas para contar rápido."),
        ("{F} ¿Cuántas personas entraron a las 8:00?", "7 personas", "Un grupo de cinco más dos sueltas son siete."),
        ("=", "¿Cuántas personas representan IIIII IIIII III?", "5+5+3", "Se suman dos grupos de cinco y tres sueltas.", " personas"),
        ("{F} ¿Cuántas personas entraron a las 9:00?", "11 personas", "Dos grupos de cinco y una suelta suman once."),
        ("=", "{F} ¿Cuántas personas entraron en total entre las 8:00 y las 11:00?", "7+11+8+4", "Se suman los recuentos de las cuatro horas.", " personas"),
        ("abc", "{F} ¿A qué hora entró más gente?", "A las 9:00", "A las 8:00", "A las 11:00", "La hora con más marcas fue las 9:00, con once personas."),
        ("=", "{F} ¿Cuántas personas más entraron a las 9:00 que a las 11:00?", "11-4", "Se resta la menor cantidad de la mayor.", " personas"),
        ("abc", "¿Por qué las marcas se agrupan de cinco?", "Para contar más rápido y no perder la cuenta", "Para que se vean más bonitas", "Porque siempre hay cinco personas", "Agrupar de a cinco permite contar de cinco en cinco."),
        ("ab", "¿Cómo se anotan 12 con marcas de recuento?", "IIIII IIIII II", "IIIII IIII", "Dos grupos de cinco y dos sueltas suman 12."),
        ("=", "Hay 3 grupos cerrados de cinco y 4 sueltas. ¿Cuántos datos son?", "3*5+4", "Se multiplican los grupos por cinco y se suman las sueltas.", " datos"),
        ("=", "{F} Entran 6 personas más a las 11:00. ¿Cuántas habrá en esa hora?", "4+6", "Se suman las nuevas entradas al recuento.", " personas"),
        ("abc", "Alguien anotó 9 personas como IIIII IIIII. ¿Qué error hay?", "Esas marcas son 10, no 9", "Está bien porque son dos grupos", "Faltan cinco marcas más", "Dos grupos cerrados valen diez; nueve sería IIIII IIII."),
        ("ab", "¿Cuántos son IIIII IIIII IIIII I?", "16", "6", "Tres grupos de cinco son 15 y una suelta hace 16."),
    ],
    ctx=("=", "El guardia de un edificio de oficinas anotó 7, 11, 8 y 4 personas en cuatro horas. La administradora quiere saber cuántas personas entraron en total para pedir más tarjetas de visita. ¿Cuántas fueron?", "7+11+8+4", "Se suman las entradas de las cuatro horas.", " personas"),
    sc=[("¿Para qué sirven las marcas de recuento?", "Para contar cuántas veces ocurre algo mientras ocurre", "Permiten anotar cada hecho sin perder la cuenta."),
        ("¿Cuántos son dos grupos de cinco y una marca suelta?", "11", "Dos grupos suman diez y la suelta hace once."),
        ("¿Qué es la frecuencia de un dato?", "Cuántas veces aparece", "La frecuencia es el resultado de contar un dato.")],
    op=("Anota con marcas de recuento estas llamadas a una oficina de ejemplo en una mañana: Consulta 9, Reclamo 4, Trámite 12. Escribe cuántas llamadas hubo en total.",
        "Consulta: IIIII IIII. Reclamo: IIII. Trámite: IIIII IIIII II. Total: 9 + 4 + 12 = 25 llamadas.",
        ["agrupa las marcas de cinco", "las marcas coinciden con los números", "suma correctamente el total"],
        ["hoja con las marcas y la suma"],
        ["no cerrar los grupos de cinco", "sumar mal el total"],
        "Pregunta: «¿cuántas marcas tiene tu fila de Trámite?». Si no da 12, pídele contar por grupos."),
    reinforce="Anota con marcas cuántas veces suena tu teléfono en un día de ejemplo: 14 veces.",
    extend="Explica por qué contar por grupos reduce los errores respecto de contar rayitas sueltas.",
)

# ===================================================== OAD-14 clase 2
F = ("Datos de ejemplo. Una pastelería anotó el sabor que pidió cada uno de 20 clientes: "
     "Ch, V, Ch, F, V, Ch, Ch, V, F, Ch, V, V, Ch, F, Ch, V, Ch, F, V, Ch. (Ch = chocolate, V = vainilla, F = frutilla).")
build(
    O14, 2, F,
    use="Voy a pasar una lista de datos a una tabla de frecuencia absoluta.",
    prior=["Sé contar con marcas de recuento.", "Sé sumar números de dos cifras.", "Sé qué es un dato."],
    explain=[
        "Una lista de datos desordenada es difícil de leer. Una tabla de frecuencia la ordena: en una columna van las categorías, como los sabores, y en otra cuántas veces aparece cada una. Ese número se llama frecuencia absoluta.",
        "Para armarla, haz una fila por cada categoría sin repetir. Recorre la lista y marca cada dato con una rayita en su fila, o táchalo de la lista para no contarlo dos veces. Al final, cuenta las marcas de cada fila y escribe el número.",
        "El total de la tabla debe ser igual al número de datos de la lista. Si no coincide, faltó un dato o se contó uno dos veces. Esta comprobación te cuida de errores, igual que cuando revisas el vuelto de una compra.",
    ],
    vocab=[("tabla de frecuencia", "tabla que dice cuántas veces aparece cada dato"), ("frecuencia absoluta", "cantidad de veces que aparece un dato"), ("categoría", "grupo con nombre, como un sabor"), ("total", "suma de todas las frecuencias"), ("lista", "datos anotados uno tras otro"), ("comprobar", "revisar que algo esté correcto")],
    worked=[
        ("Contar una categoría", "En la ficha, ¿cuántas veces aparece Ch?", ["Recorre la lista y marca cada Ch.", "Hay 9 marcas."], "9 veces"),
        ("Comprobar el total", "La tabla dice Ch 9, V 7, F 4. ¿Coincide con los 20 clientes?", ["Suma: 9 + 7 + 4 = 20.", "El total coincide con la cantidad de datos."], "Sí, 20"),
    ],
    mistakes=[("Contar un dato dos veces.", "No se tachan ni se marcan los datos ya contados.", "Táchalos al contarlos."),
              ("Escribir una fila repetida, como dos filas de chocolate.", "No se revisa que las categorías sean distintas.", "Haz una sola fila por categoría.")],
    T=[
        ("abc", "En Matemática: ¿qué es la frecuencia absoluta?", "Cuántas veces aparece un dato", "El dato que aparece primero", "La suma de dos categorías", "Es el conteo de veces que aparece cada dato."),
        ("{F} ¿Cuántas veces aparece F en la lista?", "4 veces", "Recorriendo la lista aparecen cuatro frutillas."),
        ("=", "{F} ¿Cuántos clientes hay en total en la lista?", "9+7+4", "Se suman las frecuencias de los tres sabores.", " clientes"),
        ("abc", "{F} ¿Qué sabor fue el más pedido?", "Chocolate", "Vainilla", "Frutilla", "Chocolate tiene la frecuencia mayor, con nueve pedidos."),
        ("=", "{F} ¿Cuántos pedidos más tuvo chocolate que vainilla?", "9-7", "Se resta la frecuencia menor de la mayor.", " pedidos"),
        ("ab", "{F} La suma de las tres frecuencias debe dar", "20", "9", "Cada cliente pidió un sabor, así que el total es 20."),
        ("=", "{F} ¿Cuántos clientes pidieron vainilla o frutilla?", "7+4", "Se suman las dos frecuencias pedidas.", " clientes"),
        ("=", "Una tabla tiene Ch 9, F 4 y V sin completar. El total es 20. ¿Cuántos pidieron V?", "20-9-4", "Se resta del total lo que ya se contó.", " clientes"),
        ("abc", "Una tabla suma 19 pero había 20 datos. ¿Qué haces?", "Vuelvo a contar la lista, porque falta un dato", "Dejo la tabla así", "Borro el total", "Si el total no coincide con los datos, se recuenta."),
        ("=", "{F} Si 3 clientes más piden chocolate, ¿cuántas veces aparecerá?", "9+3", "Se suman los pedidos nuevos a la frecuencia.", " veces"),
        ("ab", "{F} ¿Cuál es la frecuencia de limón en esta lista?", "0", "9", "El limón no aparece en la lista, así que su frecuencia es cero."),
        ("=", "{F} ¿Cuántos clientes NO pidieron chocolate?", "20-9", "Se resta del total la frecuencia de chocolate.", " clientes"),
        ("abc", "{F} ¿Cuántas filas tiene la tabla de frecuencia?", "3", "20", "9", "Se hace una fila por cada sabor distinto: chocolate, vainilla y frutilla."),
    ],
    ctx=("=", "La dueña de una pastelería de ejemplo hornea 20 queques según los pedidos: 9 de chocolate, 7 de vainilla y 4 de frutilla. Si ya vendió 6 de chocolate, ¿cuántos de chocolate le quedan por entregar?", "9-6", "Se resta lo ya entregado a la frecuencia de chocolate.", " queques"),
    sc=[("¿Qué debe coincidir en una tabla de frecuencia?", "La suma de las frecuencias con el número de datos", "Esa comparación revela datos olvidados o repetidos."),
        ("¿Cuántas filas se hacen por cada categoría?", "Una", "Cada categoría distinta aparece una sola vez en la tabla."),
        ("¿Qué escribes en la tabla para una categoría que no aparece?", "El número cero", "Cero indica que ese dato no ocurrió ninguna vez.")],
    op=("Arma una tabla de frecuencia con esta lista de ejemplo, que muestra el medio de transporte de 15 personas: Bus, Metro, Bus, A pie, Bus, Metro, Bus, A pie, Bus, Metro, Bus, Bus, A pie, Metro, Bus. Escribe el total.",
        "Bus 8, Metro 4, A pie 3. Total: 8 + 4 + 3 = 15.",
        ["una fila por categoría", "frecuencias correctas 8, 4 y 3", "total igual a 15"],
        ["hoja con la tabla y el total"],
        ["repetir una categoría", "olvidar una fila"],
        "Pregunta: «¿cómo sabes que contaste todos los datos?». Debe decir que el total da 15."),
    reinforce="Cuenta las vocales de la frase «hoy me toca turno en la mañana» y arma una tabla.",
    extend="Explica por qué dos listas distintas pueden dar la misma tabla de frecuencia.",
)

# ===================================================== OAD-14 clase 3
F = ("Datos de ejemplo. Una oficina municipal anotó el motivo de las 18 llamadas del día: "
     "P, Pg, C, C, P, Pg, Pg, C, P, Pg, C, Pg, P, C, C, Pg, P, C. (P = permiso, Pg = pago, C = consulta).")
build(
    O14, 3, F,
    use="Voy a contar datos sin repetir ni olvidar y a escribir la tabla con marcas y frecuencias.",
    prior=["Sé qué es una tabla de frecuencia.", "Sé contar con marcas de recuento.", "Sé sumar tres números."],
    explain=[
        "Cuando la lista es larga, hay un método para no equivocarse. Lee la lista de principio a fin y anota una marca de recuento en la fila de cada dato. Mientras lees, puedes tachar el dato de la lista, así sabes por dónde vas.",
        "Al terminar, cuenta las marcas de cada fila y escribe el número en la columna de frecuencia. La tabla queda con tres columnas: categoría, marcas y frecuencia. Con ella puedes ver rápido cuál categoría es la mayor y cuál la menor.",
        "Suma todas las frecuencias. El total debe ser igual al número de datos de la lista, aquí 18. Si no coincide, repite el conteo de la categoría que dudas. Este método también sirve para contar llamadas, pedidos o boletas.",
    ],
    vocab=[("marcas", "rayitas que se anotan por cada dato"), ("frecuencia", "número de veces que aparece un dato"), ("tachar", "hacer una línea sobre un dato ya contado"), ("recorrer", "leer la lista de principio a fin"), ("municipalidad", "oficina del gobierno local"), ("motivo", "razón de la llamada")],
    worked=[
        ("Contar permisos", "En la ficha, ¿cuántas llamadas fueron por permiso (P)?", ["Recorre la lista y marca cada P: IIIII.", "Son cinco."], "5 llamadas"),
        ("Revisar el total", "La tabla dice P 5, Pg 6 y C 7. ¿Cuadra con las 18 llamadas?", ["Suma 5 + 6 + 7 = 18.", "Cuadra con la cantidad de datos."], "Sí, 18"),
    ],
    mistakes=[("Marcar un dato en dos filas distintas.", "Se lee rápido y se pierde por dónde se va.", "Tacha cada dato apenas lo cuentas."),
              ("Hacer un grupo de cinco con cuatro rayitas.", "Se cierra el grupo antes de tiempo.", "Cierra el grupo solo en la quinta marca.")],
    T=[
        ("abc", "¿Para qué sirve tachar cada dato mientras se cuenta?", "Para no contarlo dos veces", "Para borrar la lista", "Para cambiar el dato", "Tachar muestra qué datos ya se contaron."),
        ("{F} ¿Cuántas llamadas fueron por consulta (C)?", "7 llamadas", "Recorriendo la lista aparecen siete consultas."),
        ("=", "{F} ¿Cuántas llamadas recibió la oficina en total?", "5+6+7", "Se suman las frecuencias de las tres categorías.", " llamadas"),
        ("abc", "{F} ¿Cuántas llamadas fueron por pago (Pg)?", "6", "5", "7", "En la lista aparecen seis llamadas por pago."),
        ("=", "{F} ¿Cuántas llamadas más fueron consultas que permisos?", "7-5", "Se resta la frecuencia menor de la mayor.", " llamadas"),
        ("abc", "¿Cómo se escribe 7 con marcas de recuento?", "IIIII II", "IIIII I", "IIII III", "Siete es un grupo de cinco y dos sueltas."),
        ("ab", "{F} La suma de las frecuencias debe ser igual a", "18, el número de datos de la lista", "7, la frecuencia mayor", "Cada llamada se cuenta una vez, así que el total es 18."),
        ("=", "{F} ¿Cuántas llamadas fueron por permiso o por pago?", "5+6", "Se suman las dos frecuencias pedidas.", " llamadas"),
        ("abc", "Una persona contó 7 pagos porque anotó un dato dos veces. ¿Qué pasó con su total?", "Daría 19, más que los 18 datos", "Daría 17", "No cambiaría", "Un dato contado dos veces suma de más y el total supera los datos."),
        ("=", "{F} ¿Cuántas llamadas NO fueron consultas?", "18-7", "Se resta del total la frecuencia de consultas.", " llamadas"),
        ("ab", "{F} ¿Qué categoría tiene la mayor frecuencia?", "Consulta", "Permiso", "La consulta tiene siete llamadas, más que pago y permiso."),
        ("=", "{F} Si entran 4 llamadas más por permiso, ¿cuántas serán?", "5+4", "Se suman las llamadas nuevas a la frecuencia.", " llamadas"),
        ("abc", "{F} Si se ordena la tabla de mayor a menor frecuencia, ¿qué categoría va primero?", "Consulta", "Pago", "Permiso", "La mayor frecuencia, siete, es la de consulta."),
    ],
    ctx=("=", "Una funcionaria municipal de ejemplo recibió 7 llamadas de consulta, 6 de pago y 5 de permiso. Debe anotar en su informe cuántas llamadas atendió ese día. ¿Cuántas fueron?", "7+6+5", "Se suman las frecuencias de las tres categorías.", " llamadas"),
    sc=[("¿Qué haces mientras recorres la lista?", "Marco cada dato y lo tacho", "Así no se cuenta dos veces ni se olvida ninguno."),
        ("¿Cómo compruebas el conteo?", "Sumo las frecuencias y comparo con los datos", "Si el total coincide, el conteo es correcto."),
        ("¿Qué número escribes cuando hay IIIII III?", "8", "Un grupo de cinco más tres sueltas suman ocho.")],
    op=("Haz una tabla con marcas y frecuencias de esta lista de ejemplo de 16 pedidos de una ferretería: Clavos, Pintura, Clavos, Tornillos, Pintura, Clavos, Tornillos, Clavos, Pintura, Clavos, Tornillos, Clavos, Pintura, Clavos, Tornillos, Clavos.",
        "Clavos 8 (IIIII III), Pintura 4 (IIII), Tornillos 4 (IIII). Total: 8 + 4 + 4 = 16.",
        ["una fila por categoría", "marcas agrupadas de cinco", "total igual a 16"],
        ["hoja con la tabla de tres columnas"],
        ["contar un dato dos veces", "no revisar el total"],
        "Pregunta: «¿qué producto se pidió más y cuántas veces?». Debe responder clavos, ocho veces."),
    reinforce="Cuenta los colores de ropa que ves colgada en una tienda o foto y arma una tabla con marcas.",
    extend="Explica cómo harías el conteo si la lista tuviera 100 datos y 5 categorías.",
)

# ===================================================== OAD-14 clase 4
F = ("Datos de ejemplo. Tabla de frecuencia: medio de pago usado en 25 compras de un almacén de barrio. "
     "Efectivo 12. Tarjeta de débito 8. Transferencia 5. El gráfico de barras tiene escala de 2 en 2: 0, 2, 4, 6, 8, 10, 12, 14.")
build(
    O14, 4, F,
    use="Voy a dibujar un gráfico de barras a partir de una tabla de frecuencia.",
    prior=["Sé las partes de un gráfico de barras.", "Sé leer escalas de 2 en 2.", "Sé qué es una frecuencia."],
    explain=[
        "Una tabla de frecuencia se puede dibujar como gráfico de barras. Cada categoría de la tabla será una barra y su frecuencia será la altura. Primero escribe el título, después dibuja los ejes y la escala, y luego cada barra hasta su frecuencia.",
        "La escala debe llegar al menos a la frecuencia mayor. Si usas una escala de 2 en 2 y un dato es impar, como 5, la barra queda justo entre las marcas 4 y 6. Eso es correcto: la mitad entre dos marcas vale el número del medio.",
        "El gráfico y la tabla dicen lo mismo. Por eso, cuando termines, compara: cada barra debe coincidir con su fila de la tabla. Este paso de tabla a gráfico sirve para mostrar información a otras personas de manera rápida y visual.",
    ],
    vocab=[("tabla de frecuencia", "lista de categorías con cuántas veces aparece cada una"), ("barra", "rectángulo cuya altura es la frecuencia"), ("escala", "números del eje vertical"), ("mitad entre dos marcas", "lugar justo en el centro entre dos marcas"), ("efectivo", "dinero en billetes y monedas"), ("transferencia", "pago de una cuenta a otra")],
    worked=[
        ("Altura de una barra", "En la ficha, ¿hasta dónde sube la barra de Tarjeta de débito?", ["La tabla dice 8.", "La barra llega a la marca 8 de la escala."], "Hasta 8"),
        ("Valor entre marcas", "La barra de Transferencia (5) queda entre dos marcas. ¿Cuáles?", ["La escala sube de 2 en 2: ..., 4, 6.", "El 5 queda justo en el medio entre 4 y 6."], "Entre 4 y 6"),
    ],
    mistakes=[("Dibujar la barra de 5 sobre la marca 6.", "Se redondea a la marca más cercana.", "Deja la barra en el punto medio entre 4 y 6."),
              ("Usar una escala que llega solo hasta 10 para una frecuencia de 12.", "No se mira el dato mayor.", "Haz que la escala llegue al menos a 12.")],
    T=[
        ("abc", "{F} ¿Cuántas barras tiene el gráfico?", "3", "25", "12", "Cada medio de pago de la tabla se dibuja como una barra."),
        ("{F} ¿Hasta qué número sube la barra de Efectivo?", "12", "La tabla dice que Efectivo tiene doce compras."),
        ("=", "{F} ¿Cuántas compras suman las tres barras?", "12+8+5", "Se suman las frecuencias de la tabla.", " compras"),
        ("abc", "{F} ¿Hasta dónde debe llegar la escala como mínimo?", "12", "8", "5", "La escala debe cubrir la frecuencia mayor, que es doce."),
        ("ab", "{F} La barra de Transferencia (5) queda", "justo en el medio entre las marcas 4 y 6", "sobre la marca 6", "Cinco está a igual distancia de 4 y de 6, es decir a mitad de camino."),
        ("=", "{F} ¿Cuántas compras más se pagaron en efectivo que por transferencia?", "12-5", "Se resta la frecuencia menor de la mayor.", " compras"),
        ("=", "{F} ¿Cuántas compras se pagaron con tarjeta o transferencia?", "8+5", "Se suman las dos frecuencias pedidas.", " compras"),
        ("abc", "{F} ¿Qué barra es la más baja?", "Transferencia", "Efectivo", "Tarjeta de débito", "La barra de Transferencia llega solo a cinco, la menor frecuencia."),
        ("abc", "Una barra llega justo en el medio entre las marcas 8 y 10. ¿Qué valor tiene?", "9", "8", "10", "El punto medio entre ocho y diez es nueve."),
        ("=", "{F} ¿Cuántas compras NO se pagaron en efectivo?", "25-12", "Se resta del total la frecuencia de efectivo.", " compras"),
        ("ab", "{F} Una persona dibujó la barra de Tarjeta de débito hasta 10. ¿Está bien?", "No, debe llegar a 8", "Sí, 10 es cercano a 8", "La tabla dice 8, así que la barra debe llegar exactamente a 8."),
        ("=", "{F} Si hubiera 4 compras más por transferencia, ¿cuántas serían?", "5+4", "Se suman las compras nuevas a la frecuencia.", " compras"),
        ("abc", "{F} ¿Cuál es un buen título para el gráfico?", "Medios de pago en 25 compras de un almacén", "Barras", "Doce, ocho y cinco", "Un buen título dice de qué datos trata el gráfico."),
    ],
    ctx=("=", "El dueño de un almacén de ejemplo ve su gráfico: efectivo 12 y tarjeta de débito 8. Para guardar dinero en caja necesita saber cuántas compras se pagaron en efectivo o con tarjeta. ¿Cuántas fueron?", "12+8", "Se suman las dos barras.", " compras"),
    sc=[("¿Qué se lee en la altura de cada barra?", "La frecuencia de esa categoría", "La altura muestra cuántas veces aparece el dato."),
        ("¿Cómo compruebas que el gráfico está bien hecho?", "Comparo cada barra con su fila de la tabla", "Así se detectan alturas equivocadas antes de mostrarlo."),
        ("¿Qué valor está justo entre las marcas 6 y 8 de una escala de 2 en 2?", "7", "El punto medio entre seis y ocho es siete.")],
    op=("Dibuja el gráfico de barras de esta tabla de ejemplo: Turnos de una panadería: Mañana 9, Tarde 7, Noche 3. Escala de 1 en 1 del 0 al 10, título y rótulos.",
        "Título «Personas por turno»; barras de alturas 9, 7 y 3; ejes rotulados «Turno» y «Personas».",
        ["alturas 9, 7 y 3", "escala bien escrita", "título y rótulos"],
        ["hoja con el gráfico y la tabla al lado"],
        ["barras que no coinciden con la tabla", "olvidar los rótulos"],
        "Pregunta: «¿qué turno tiene más personas y cuántas más que el de noche?». Debe responder mañana, 6 más."),
    reinforce="Pasa la tabla de la clase anterior (sabores de pastelería) a un gráfico de barras.",
    extend="Explica qué ventaja tiene el gráfico sobre la tabla cuando se muestra a mucha gente.",
)
