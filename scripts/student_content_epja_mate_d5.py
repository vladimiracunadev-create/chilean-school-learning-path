"""Matemática EPJA Nivel 1 básico, módulo 4: OAD-15 (identificar datos de una tabla o un gráfico para resolver problemas y generar información nueva). Datos de ejemplo, inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Hoja, lápiz de mina y regla. Todo se hace en papel; las tablas y los gráficos vienen escritos en cada ficha. Todos los datos, precios y cifras son de ejemplo, inventados."
build = make_build(MATERIALS)

O15 = "EPJA-MATE-NB1-OAD-15"

# ===================================================== OAD-15 clase 1
F = ("Datos de ejemplo. Tabla de asistentes a los talleres de un centro comunitario: "
     "Marzo 24, Abril 30, Mayo 27, Junio 21, Julio 33.")
build(
    O15, 1, F,
    use="Voy a buscar datos exactos en una tabla y a usarlos para responder preguntas.",
    prior=["Sé leer una tabla de dos columnas.", "Sé sumar y restar números de dos cifras.", "Sé qué es un dato."],
    explain=[
        "Una tabla ordena la información en filas y columnas. Cada fila tiene una categoría, como un mes, y su dato, como la cantidad de asistentes. Para buscar un dato, ubica primero la fila de la categoría y luego lee el número de la columna.",
        "Antes de resolver un problema, identifica qué te piden y qué datos necesitas. A veces basta un solo dato: «¿cuántos asistieron en mayo?». Otras veces necesitas varios y una operación: «¿cuántos asistieron en total?». Subraya los datos que usarás.",
        "Leer boletas, horarios y listas ya es una práctica que sirve aquí. Una tabla es una lista bien ordenada. Después de resolver, comprueba que tu respuesta tenga sentido: que sea parecida a los números de la tabla y tenga la unidad correcta.",
    ],
    vocab=[("tabla", "datos ordenados en filas y columnas"), ("fila", "línea de datos que va hacia el lado"), ("columna", "línea de datos que va hacia abajo"), ("dato", "número o palabra que da información"), ("asistente", "persona que está presente en una actividad"), ("identificar", "reconocer y señalar algo")],
    worked=[
        ("Buscar un dato", "En la ficha, ¿cuántos asistieron en mayo?", ["Busca la fila «Mayo».", "Lee su número: 27."], "27 asistentes"),
        ("Usar dos datos", "¿Cuántos asistieron entre abril y mayo?", ["Identifica los dos datos: 30 y 27.", "Suma 30 + 27 = 57."], "57 asistentes"),
    ],
    mistakes=[("Leer el dato del mes vecino.", "Se mira rápido y se cambia de fila.", "Pasa un dedo o una regla por la fila del mes."),
              ("Resolver sin saber qué se pregunta.", "Se suman todos los datos aunque no hagan falta.", "Subraya la pregunta y escribe qué datos necesitas.")],
    T=[
        ("abc", "{F} ¿Qué se busca primero para hallar un dato en una tabla?", "La fila de la categoría", "El número mayor", "El total", "Cada dato pertenece a una fila, que se ubica por su nombre."),
        ("{F} ¿Cuántos asistentes hubo en junio?", "21 asistentes", "La fila de junio indica veintiún asistentes."),
        ("=", "{F} ¿Cuántos asistentes hubo en total en los cinco meses?", "24+30+27+21+33", "Se suman todos los datos de la columna.", " asistentes"),
        ("abc", "{F} ¿En qué mes hubo más asistentes?", "Julio", "Abril", "Marzo", "Treinta y tres es el número mayor de la tabla, de julio."),
        ("=", "{F} ¿Cuántos asistentes hubo entre abril y mayo?", "30+27", "Se suman los dos datos pedidos.", " asistentes"),
        ("ab", "{F} ¿Hubo más asistentes en abril o en junio?", "En abril", "En junio", "Treinta es mayor que veintiuno, por lo tanto abril tuvo más."),
        ("=", "{F} ¿Cuántos asistentes más hubo en julio que en junio?", "33-21", "Se resta el dato menor del mayor.", " asistentes"),
        ("abc", "{F} ¿Qué dato NO está en la tabla?", "Los asistentes de agosto", "Los asistentes de marzo", "Los asistentes de julio", "La tabla llega hasta julio y no incluye agosto."),
        ("=", "{F} ¿Cuántos asistentes hubo de marzo a mayo?", "24+30+27", "Se suman las tres filas pedidas.", " asistentes"),
        ("=", "{F} Si en junio hubieran asistido 9 personas más, ¿cuántas habría?", "21+9", "Se suman las personas nuevas al dato de junio.", " asistentes"),
        ("ab", "{F} ¿En cuántos meses hubo más de 25 asistentes?", "3", "5", "Abril con 30, mayo con 27 y julio con 33 superan 25."),
        ("=", "{F} ¿Cuántos asistentes NO hubo en julio, de los cinco meses?", "24+30+27+21", "Se suman todos los meses menos julio.", " asistentes"),
        ("abc", "¿Qué pregunta se responde mirando una sola fila?", "¿Cuántos asistieron en abril?", "¿Cuántos asistieron en total?", "¿Cuántos más asistieron en julio que en marzo?", "Una pregunta puntual usa un solo dato; las otras piden operar con varios."),
    ],
    ctx=("=", "La coordinadora de un centro comunitario debe preparar sillas para el mes con más asistentes de la tabla. ¿Para cuántas personas prepara sillas si el mes mayor fue julio, con 33, y quiere dejar 5 sillas más por si acaso?", "33+5", "Se suman las sillas extra al dato mayor.", " sillas"),
    sc=[("¿Qué haces antes de resolver un problema de una tabla?", "Identifico qué me preguntan y qué datos necesito", "Así uso solo los datos útiles y no me confundo."),
        ("¿Cómo compruebas que tu respuesta tiene sentido?", "Veo si se parece a los números de la tabla y tiene su unidad", "Una respuesta absurda indica un error de cálculo."),
        ("¿Qué operación usas para saber cuántos más hay en una fila que en otra?", "Una resta", "Restar el dato menor al mayor da la diferencia.")],
    op=("Con esta tabla de ejemplo de una verdulería, escribe tres preguntas y respóndelas: Tomates 18 kilos, Paltas 12 kilos, Cebollas 25 kilos, Zapallos 9 kilos.",
        "«¿Cuántos kilos de paltas? 12.» «¿Cuál se vendió más? Cebollas, 25.» «¿Cuántos kilos en total? 18 + 12 + 25 + 9 = 64.»",
        ["las preguntas se responden con la tabla", "las respuestas son correctas", "indica qué datos usó"],
        ["hoja con tres preguntas y respuestas"],
        ["usar un dato de otra fila", "preguntas que la tabla no puede responder"],
        "Pregunta: «¿de qué fila sacaste ese número?». Debe señalar la fila."),
    reinforce="Busca en una boleta tres datos y escríbelos en una tabla de dos columnas.",
    extend="Explica por qué una tabla ordenada ayuda más que una lista suelta de datos.",
)

# ===================================================== OAD-15 clase 2
F = ("Datos de ejemplo. Gráfico de barras, escala de 5 en 5: «Empanadas vendidas por día en un puesto». "
     "Lunes 40, Martes 55, Miércoles 35, Jueves 60, Viernes 85.")
build(
    O15, 2, F,
    use="Voy a hallar el mayor, el menor y la diferencia entre datos de un gráfico para resolver problemas.",
    prior=["Sé leer un gráfico de barras con escala de 5 en 5.", "Sé restar de a dos cifras.", "Sé comparar números."],
    explain=[
        "Con un gráfico puedes responder preguntas. El dato mayor es el de la barra más alta y el menor el de la barra más baja. La diferencia entre dos datos es cuánto le falta al menor para llegar al mayor, y se calcula con una resta.",
        "Para encontrar la diferencia entre el mayor y el menor, resta el menor al mayor. Aquí el mayor es 85 y el menor es 35: 85 − 35 = 50. Esa información nueva no estaba escrita en el gráfico; la calculaste tú con los datos.",
        "Generar información nueva es parte del trabajo con datos. Puedes sumar, restar, comparar o buscar cuántos faltan para igualar. Siempre di la unidad: aquí, empanadas. Y comprueba que el resultado tenga sentido frente al gráfico.",
    ],
    vocab=[("mayor", "el dato más grande"), ("menor", "el dato más pequeño"), ("diferencia", "resultado de restar dos datos"), ("información nueva", "dato calculado a partir de los datos del gráfico"), ("igualar", "hacer que dos cantidades sean iguales"), ("unidad", "palabra que dice qué se cuenta, como empanadas")],
    worked=[
        ("Diferencia mayor y menor", "En la ficha, ¿cuál es la diferencia entre el día de más ventas y el de menos?", ["Mayor: viernes, 85. Menor: miércoles, 35.", "Resta: 85 − 35 = 50."], "50 empanadas"),
        ("Cuánto falta para igualar", "¿Cuántas empanadas más debió vender el miércoles para igualar al jueves?", ["Jueves vendió 60 y miércoles 35.", "Resta: 60 − 35 = 25."], "25 empanadas"),
    ],
    mistakes=[("Restar el mayor al menor y dar un resultado confuso.", "Se resta en el orden en que aparecen los datos.", "Pon primero el dato mayor y resta el menor."),
              ("Olvidar la unidad en la respuesta.", "Se piensa que el número basta.", "Escribe siempre qué cuentas: empanadas.")],
    T=[
        ("abc", "{F} ¿Qué día se vendió más?", "Viernes", "Martes", "Lunes", "La barra más alta es la del viernes, con ochenta y cinco."),
        ("abc", "{F} ¿Qué día se vendió menos?", "Miércoles", "Lunes", "Jueves", "La barra más baja es la del miércoles, con treinta y cinco."),
        ("=", "{F} ¿Cuál es la diferencia entre el día de más ventas y el de menos?", "85-35", "Se resta el dato menor al mayor.", " empanadas"),
        ("=", "{F} ¿Cuántas empanadas más se vendieron el martes que el lunes?", "55-40", "Se comparan dos barras restando.", " empanadas"),
        ("=", "{F} ¿Cuántas empanadas más se vendieron el jueves que el martes?", "60-55", "Es una resta entre dos datos del gráfico.", " empanadas"),
        ("ab", "{F} La diferencia entre dos datos se calcula con", "una resta", "una suma", "Cuánto más es un dato que otro se halla restando."),
        ("=", "{F} ¿Cuántas empanadas se vendieron en la semana?", "40+55+35+60+85", "Se suman los cinco datos.", " empanadas"),
        ("=", "{F} Si el miércoles se hubieran vendido 20 empanadas más, ¿cuántas habría?", "35+20", "Se suman las nuevas ventas al dato del miércoles.", " empanadas"),
        ("=", "{F} ¿Cuántas empanadas más debió vender el miércoles para igualar al jueves?", "60-35", "Se resta el dato menor al mayor.", " empanadas"),
        ("abc", "{F} ¿Qué día se parece más al lunes en ventas?", "Miércoles", "Viernes", "Jueves", "El miércoles difiere en cinco del lunes, menos que los demás días."),
        ("=", "{F} ¿Cuántas empanadas más se vendieron el viernes que el jueves?", "85-60", "Se resta el dato menor del mayor.", " empanadas"),
        ("ab", "{F} ¿Vendió más el lunes o el miércoles?", "El lunes", "El miércoles", "Cuarenta es mayor que treinta y cinco, así que el lunes vendió más."),
        ("abc", "Una persona calculó 35 − 85 y no pudo. ¿Qué debe hacer?", "Restar 85 − 35", "Sumar 35 + 85", "Dejar el cálculo sin resolver", "Para la diferencia se resta el dato menor al mayor."),
    ],
    ctx=("=", "El dueño de un puesto de empanadas de ejemplo quiere saber cuántas empanadas más vendió el viernes que el lunes para decidir cuántas masas comprar. ¿Cuántas más fueron?", "85-40", "Se resta la barra del lunes a la del viernes.", " empanadas"),
    sc=[("¿Cómo hallas la diferencia entre dos datos?", "Resto el menor al mayor", "La resta muestra cuánto más es uno que otro."),
        ("¿Cómo reconoces el dato mayor en un gráfico?", "Es la barra más alta", "La altura de la barra indica la cantidad de cada categoría."),
        ("¿Qué información nueva puedes calcular de un gráfico?", "Totales, diferencias y comparaciones", "Con los datos se pueden hacer cálculos nuevos.")],
    op=("Con este gráfico de ejemplo de un taller mecánico (autos atendidos por día: Lunes 12, Martes 9, Miércoles 15, Jueves 11), escribe: el día mayor, el menor, su diferencia y el total de la semana.",
        "Mayor: miércoles, 15. Menor: martes, 9. Diferencia: 15 − 9 = 6. Total: 12 + 9 + 15 + 11 = 47 autos.",
        ["identifica mayor y menor", "calcula bien la diferencia y el total", "usa la unidad"],
        ["hoja con cuatro respuestas y sus cálculos"],
        ["restar en orden inverso", "olvidar un día en el total"],
        "Pregunta: «¿cómo sabes que el miércoles es el mayor?». Debe decir que su barra es la más alta."),
    reinforce="Escribe dos preguntas de comparación sobre la ficha y respóndelas.",
    extend="Explica una situación de la vida diaria en que necesites saber cuánto falta para igualar dos cantidades.",
)

# ===================================================== OAD-15 clase 3
F = ("Datos de ejemplo. Tabla de entradas vendidas para una función comunitaria; la meta es vender 300 entradas: "
     "Adulto 120, Estudiante 80, Adulto mayor 45. Precio de ejemplo: la entrada de adulto mayor cuesta $2.000.")
build(
    O15, 3, F,
    use="Voy a calcular totales y cuánto falta para llegar a una meta usando una tabla.",
    prior=["Sé sumar números de tres cifras.", "Sé restar números de tres cifras.", "Sé multiplicar por 2.000 contando de a miles."],
    explain=[
        "Un total se calcula sumando todos los datos de una tabla. Si hay una meta, es decir, una cantidad que se quiere lograr, puedes saber cuánto falta restando el total a la meta. Aquí la meta es 300 entradas.",
        "Los pasos son: primero sumar para hallar el total vendido, y luego restar. Por ejemplo, 120 + 80 + 45 = 245, y 300 − 245 = 55. Faltan 55 entradas. Si además hay un precio, puedes multiplicar la cantidad por el precio para saber cuánto dinero se junta.",
        "Las metas aparecen en muchas situaciones: lo que se quiere reunir, vender o producir. Calcular cuánto falta ayuda a decidir qué hacer. Los precios de este cuaderno son inventados; para dinero real, mira siempre los valores vigentes.",
    ],
    vocab=[("meta", "cantidad que se quiere lograr"), ("total", "resultado de sumar todos los datos"), ("faltar", "ser necesario para llegar a la meta"), ("precio", "dinero que cuesta una cosa"), ("entrada", "boleto para asistir a un evento"), ("recaudar", "juntar dinero")],
    worked=[
        ("Hallar lo vendido", "En la ficha, ¿cuántas entradas se vendieron en total?", ["Suma 120 + 80 + 45.", "120 + 80 = 200; 200 + 45 = 245."], "245 entradas"),
        ("Cuánto falta", "¿Cuántas entradas faltan para la meta de 300?", ["El total vendido es 245.", "Resta: 300 − 245 = 55."], "55 entradas"),
    ],
    mistakes=[("Restar a la meta solo una fila de la tabla.", "No se suma antes el total vendido.", "Primero suma todas las filas y luego resta a la meta."),
              ("Sumar la meta al total vendido.", "Se confunde «falta» con «agregar».", "Falta es una resta: meta menos lo que ya se tiene.")],
    T=[
        ("=", "{F} ¿Cuántas entradas se vendieron en total?", "120+80+45", "Se suman las tres filas de la tabla.", " entradas"),
        ("=", "{F} ¿Cuántas entradas faltan para llegar a la meta?", "300-245", "Se resta lo vendido a la meta.", " entradas"),
        ("abc", "{F} ¿Qué operación sirve para saber cuánto falta para la meta?", "Restar el total vendido a la meta", "Sumar la meta al total", "Multiplicar la meta por el total", "Falta es lo que queda entre lo logrado y la meta, una resta."),
        ("=", "{F} ¿Cuántas entradas de estudiante y de adulto mayor se vendieron juntas?", "80+45", "Se suman las dos filas pedidas.", " entradas"),
        ("=", "{F} ¿Cuántas entradas más de adulto que de adulto mayor se vendieron?", "120-45", "Se resta el dato menor del mayor.", " entradas"),
        ("abc", "{F} ¿Qué tipo de entrada se vendió más?", "Adulto", "Estudiante", "Adulto mayor", "Ciento veinte es el número mayor de la tabla."),
        ("ab", "{F} ¿Se alcanzó la meta de 300 entradas?", "No, porque se vendieron 245", "Sí, porque se vendieron más de 200", "Doscientas cuarenta y cinco es menor que trescientas."),
        ("=", "{F} Si se venden 55 entradas más, ¿cuántas habrá vendidas en total?", "245+55", "Se suman las nuevas entradas al total vendido.", " entradas"),
        ("=", "{F} ¿Cuántos pesos se juntaron con las entradas de adulto mayor?", "45*2000", "Se multiplica la cantidad por el precio de cada entrada.", " pesos"),
        ("=", "{F} ¿Cuántas entradas NO son de adulto?", "80+45", "Se suman las dos filas que no son de adulto.", " entradas"),
        ("abc", "Una persona calculó 300 + 245 = 545 para saber cuánto falta. ¿Qué error cometió?", "Sumó en vez de restar", "Restó en vez de sumar", "Usó una meta equivocada", "Para saber cuánto falta se resta lo logrado a la meta."),
        ("=", "{F} Si se vendieran 20 entradas más de estudiante, ¿cuántas serían de estudiante?", "80+20", "Se suman las entradas nuevas a la fila de estudiante.", " entradas"),
        ("ab", "{F} Si faltan 55 entradas y se venden 60 más, ¿se supera la meta?", "Sí, por 5 entradas", "No, faltarían 5", "Sesenta es mayor que cincuenta y cinco, así que sobran cinco."),
    ],
    ctx=("=", "Una organizadora de un evento barrial de ejemplo vendió entradas de adulto, estudiante y adulto mayor: 120, 80 y 45. Si la meta es 300, ¿cuántas entradas más debe vender?", "300-245", "Se resta lo vendido a la meta de entradas.", " entradas"),
    sc=[("¿Cómo calculas cuánto falta para una meta?", "Resto el total logrado a la meta", "Falta es la diferencia entre la meta y lo logrado."),
        ("¿Qué haces antes de restar a la meta?", "Sumo todos los datos para hallar el total", "Sin el total no se sabe cuánto se logró."),
        ("¿Cómo calculas el dinero juntado si cada entrada tiene el mismo precio?", "Multiplico la cantidad por el precio", "Repetir un precio varias veces es multiplicar.")],
    op=("Un grupo quiere reunir 100 kilos de alimentos. Reunió: Arroz 35 kilos, Fideos 28 kilos, Legumbres 22 kilos (datos de ejemplo). Calcula el total reunido y cuántos kilos faltan para la meta. Escribe una frase.",
        "Total: 35 + 28 + 22 = 85 kilos. Faltan 100 − 85 = 15 kilos. Frase: «Faltan 15 kilos para llegar a la meta».",
        ["suma bien el total", "resta bien lo que falta", "escribe una frase con la unidad"],
        ["hoja con los cálculos y la frase"],
        ["sumar la meta en vez de restar", "olvidar una fila"],
        "Pregunta: «¿cómo sabes que faltan 15?». Debe mostrar la resta 100 − 85."),
    reinforce="Inventa una meta de ahorro semanal y una tabla de lo ahorrado en cuatro días, y calcula cuánto falta.",
    extend="Explica cómo cambia lo que falta si la meta sube de 300 a 350 entradas.",
)

# ===================================================== OAD-15 clase 4
F = ("Datos de ejemplo. Gráfico de barras, escala de 5 en 5: «Kilos reciclados en un mes por un condominio». "
     "Cartón 60, Vidrio 30, Plástico 45, Latas 15.")
build(
    O15, 4, F,
    use="Voy a comparar datos con «el doble», «la mitad» y «el triple», y a juntar categorías en un gráfico.",
    prior=["Sé multiplicar por 2 y por 3.", "Sé dividir por 2.", "Sé leer un gráfico de barras con escala de 5 en 5."],
    explain=[
        "Para comparar datos hay otras formas además de restar. El doble de un dato es ese dato multiplicado por 2. La mitad se halla dividiendo por 2. El triple es multiplicar por 3. El cuádruple es multiplicar por 4. Estas comparaciones dicen cuántas veces cabe un dato en otro.",
        "En la ficha, Cartón (60) es el doble de Vidrio (30), porque 30 × 2 = 60. Latas (15) es la mitad de Vidrio, porque 30 dividido en 2 es 15. Plástico (45) es el triple de Latas, porque 15 × 3 = 45. Comprueba siempre con la operación.",
        "También puedes juntar categorías sumando sus barras. Por ejemplo, Vidrio y Latas juntos suman 45, lo mismo que Plástico. Estas comparaciones sirven para decidir cuántas bolsas, cajas o camiones necesitas, y las usas aunque no las hayas escrito antes.",
    ],
    vocab=[("doble", "dos veces una cantidad"), ("mitad", "una de las dos partes iguales"), ("triple", "tres veces una cantidad"), ("comparar", "decir cuánto más o cuánto menos, o cuántas veces"), ("juntar", "sumar dos o más categorías"), ("reciclar", "volver a usar un material")],
    worked=[
        ("El doble", "En la ficha, ¿es Cartón el doble de Vidrio?", ["Calcula el doble de Vidrio: 30 × 2 = 60.", "Cartón es 60, así que sí lo es."], "Sí, 60 es el doble de 30"),
        ("La mitad", "¿Cuántos kilos es la mitad de los kilos de Vidrio?", ["Divide 30 en 2.", "30 ÷ 2 = 15, que coincide con Latas."], "15 kilos")
    ],
    mistakes=[("Decir que 45 es el doble de 15.", "Se compara sin calcular.", "Calcula 15 × 2 = 30; como 45 no es 30, no es el doble: es el triple."),
              ("Restar para saber «cuántas veces».", "Se confunden «cuánto más» y «cuántas veces».", "Para «cuántas veces» usa multiplicación o división.")],
    T=[
        ("abc", "{F} ¿Qué material pesa el doble que Vidrio?", "Cartón", "Plástico", "Latas", "Treinta por dos es sesenta, que es el dato de cartón."),
        ("=", "{F} ¿Cuántos kilos es el doble de Vidrio?", "30*2", "El doble se calcula multiplicando por dos.", " kilos"),
        ("=", "{F} ¿Cuántos kilos es la mitad de Cartón?", "60//2", "La mitad se calcula dividiendo por dos.", " kilos"),
        ("abc", "{F} ¿Qué material es la mitad de Vidrio?", "Latas", "Plástico", "Cartón", "La mitad de treinta es quince, que es el dato de latas."),
        ("=", "{F} ¿Cuántos kilos se reciclaron en total?", "60+30+45+15", "Se suman las cuatro barras.", " kilos"),
        ("=", "{F} ¿Cuántos kilos más de cartón que de plástico se reciclaron?", "60-45", "Se resta el dato menor del mayor.", " kilos"),
        ("ab", "{F} ¿Es Plástico el doble de Latas?", "No, es el triple", "Sí, es el doble", "Quince por dos es treinta, y plástico es 45, que es quince por tres."),
        ("=", "{F} ¿Cuántos kilos es el triple de Latas?", "15*3", "El triple se calcula multiplicando por tres.", " kilos"),
        ("abc", "{F} ¿Qué dos materiales juntos pesan lo mismo que Plástico?", "Vidrio y Latas", "Cartón y Latas", "Cartón y Vidrio", "Treinta más quince da cuarenta y cinco, igual que plástico."),
        ("=", "{F} ¿Cuántos kilos NO son cartón?", "30+45+15", "Se suman las otras tres barras.", " kilos"),
        ("=", "{F} Si el mes siguiente se recicla el doble de latas, ¿cuántos kilos serían?", "15*2", "Duplicar es multiplicar por dos.", " kilos"),
        ("ab", "{F} Latas es la mitad de", "Vidrio", "Cartón", "Quince es la mitad de treinta, que es lo que reciclaron en vidrio."),
        ("abc", "{F} ¿Qué operación usas para saber cuántas veces cabe Latas en Plástico?", "Dividir 45 por 15", "Restar 45 menos 15", "Sumar 45 más 15", "Para saber cuántas veces cabe un dato en otro se divide."),
    ],
    ctx=("=", "La administradora de un condominio de ejemplo calcula cuántos kilos de vidrio y de latas retirará el camión juntos: vidrio 30 y latas 15. ¿Cuántos kilos son?", "30+15", "Se suman las dos categorías que se retiran juntas.", " kilos"),
    sc=[("¿Cómo hallas el doble de un dato?", "Lo multiplico por 2", "Dos veces un dato es ese dato por dos."),
        ("¿Cómo hallas la mitad de un dato?", "Lo divido por 2", "Dividir en dos partes iguales da la mitad."),
        ("¿Cómo juntas dos categorías de un gráfico?", "Sumo sus barras", "El total de dos categorías es la suma de sus datos.")],
    op=("Con este gráfico de ejemplo de pan (kilos vendidos en un día: Corriente 40, Integral 20, Molde 10), escribe tres comparaciones usando «el doble», «la mitad» o «el cuádruple» y comprueba cada una con una operación.",
        "«Corriente es el doble de Integral: 20 × 2 = 40.» «Molde es la mitad de Integral: 20 ÷ 2 = 10.» «Corriente es el cuádruple de Molde: 10 × 4 = 40.»",
        ["comparaciones correctas", "comprueba con una operación", "usa los datos del gráfico"],
        ["hoja con tres frases y operaciones"],
        ["afirmar sin comprobar", "confundir doble con triple"],
        "Pregunta: «¿cómo sabes que es el doble?». Debe mostrar la multiplicación."),
    reinforce="Escribe una comparación de «el doble» con tus propias cifras de compras.",
    extend="Explica por qué «el doble» y «dos más» no son lo mismo, usando 30 como ejemplo.",
)

# ===================================================== OAD-15 clase 5
F = ("Datos de ejemplo. Tabla de gastos del mes en un hogar (pesos): Luz $30.000. Agua $15.000. Gas $25.000. Internet $20.000. "
     "El presupuesto del hogar para estas cuentas es $100.000.")
build(
    O15, 5, F,
    use="Voy a usar una tabla de gastos del hogar para sumar, restar y decidir si alcanza el dinero.",
    prior=["Sé sumar y restar con miles.", "Sé qué es un presupuesto.", "Sé leer una tabla."],
    explain=[
        "Las cuentas del hogar se pueden ordenar en una tabla: una fila por cada gasto y una columna con su valor. Con ella puedes sumar para saber el total del mes y restar al presupuesto para saber cuánto sobra o cuánto falta.",
        "Un presupuesto es el dinero que se tiene para gastar en algo. Si el total de los gastos es menor que el presupuesto, sobra dinero. Si es mayor, falta. En esta ficha el total es 90.000 y el presupuesto 100.000, por eso sobran 10.000.",
        "Al sumar miles, suma primero las cifras como si fueran números chicos y agrega los miles: 30 + 15 + 25 + 20 = 90, es decir 90.000. Los valores de esta ficha son inventados; en tu vida real mira tus cuentas vigentes. Aquí no se da consejo financiero personal.",
    ],
    vocab=[("presupuesto", "dinero disponible para gastar en algo"), ("gasto", "dinero que se paga"), ("sobrar", "quedar dinero después de pagar"), ("faltar", "no alcanzar el dinero"), ("mensual", "que ocurre cada mes"), ("total", "suma de todos los gastos")],
    worked=[
        ("Total del mes", "En la ficha, ¿cuánto suman los cuatro gastos?", ["Suma los números sin los miles: 30 + 15 + 25 + 20 = 90.", "Agrega los miles: 90.000."], "$90.000"),
        ("Cuánto sobra", "Si el presupuesto es $100.000, ¿cuánto sobra?", ["Resta: 100.000 − 90.000.", "Eso da 10.000."], "$10.000")
    ],
    mistakes=[("Olvidar un gasto al sumar.", "Se suma sin recorrer todas las filas.", "Marca cada fila al sumarla."),
              ("Restar el presupuesto al total en vez del total al presupuesto.", "Se resta en el orden en que aparecen.", "Resta lo gastado al presupuesto: presupuesto menos gastos.")],
    T=[
        ("=", "{F} ¿Cuánto suman los cuatro gastos del mes?", "30000+15000+25000+20000", "Se suman todas las filas de la tabla.", " pesos"),
        ("=", "{F} ¿Cuánto dinero sobra del presupuesto?", "100000-90000", "Se resta el total de gastos al presupuesto.", " pesos"),
        ("abc", "{F} ¿Cuál es el gasto mayor?", "Luz", "Agua", "Internet", "Treinta mil pesos es el valor mayor de la tabla."),
        ("=", "{F} ¿Cuánto más cuesta la luz que el agua?", "30000-15000", "Se resta el gasto menor al mayor.", " pesos"),
        ("=", "{F} ¿Cuánto suman el gas y el internet?", "25000+20000", "Se suman las dos filas pedidas.", " pesos"),
        ("ab", "{F} ¿Es el agua la mitad de la luz?", "Sí: 15.000 es la mitad de 30.000", "No: es el doble", "Quince mil por dos da treinta mil, así que el agua es la mitad."),
        ("=", "{F} ¿Cuánto se gasta en tres meses si los gastos son iguales?", "90000*3", "Se multiplica el total mensual por tres meses.", " pesos"),
        ("=", "{F} ¿Cuánto suman todos los gastos menos la luz?", "15000+25000+20000", "Se suman las tres filas que no son luz.", " pesos"),
        ("abc", "{F} Si la luz sube a $35.000, ¿alcanza el presupuesto de $100.000?", "Sí, el total sería $95.000", "No, faltarían $5.000", "No, sobrarían $10.000", "Noventa mil más cinco mil son noventa y cinco mil, menor que cien mil."),
        ("=", "{F} Si el presupuesto bajara a $80.000, ¿cuánto faltaría?", "90000-80000", "Se resta el presupuesto al total gastado.", " pesos"),
        ("ab", "{F} Con $50.000, ¿se pueden pagar luz y gas?", "No: suman $55.000", "Sí: suman $45.000", "Treinta mil más veinticinco mil son cincuenta y cinco mil."),
        ("=", "{F} ¿Cuánto suman agua, gas e internet?", "15000+25000+20000", "Se suman tres filas de la tabla.", " pesos"),
        ("abc", "{F} ¿Qué tabla nueva sirve para saber cuánto cuesta cada cuenta en seis meses?", "Una con cada gasto multiplicado por 6", "Una con cada gasto dividido por 6", "Una con cada gasto más 6", "Seis meses de un gasto igual son ese gasto por seis."),
    ],
    ctx=("=", "Una persona de ejemplo revisa las cuentas del hogar: luz $30.000 y gas $25.000. Quiere saber cuánto suman antes de apartar ese dinero. ¿Cuánto es?", "30000+25000", "Se suman las dos cuentas.", " pesos"),
    sc=[("¿Cómo sabes cuánto sobra de un presupuesto?", "Resto los gastos al presupuesto", "Lo que queda tras pagar es presupuesto menos gastos."),
        ("¿Cómo sumas valores en miles con facilidad?", "Sumo las cifras chicas y agrego los miles", "30 + 15 es más fácil que 30.000 + 15.000 y se agregan los miles al final."),
        ("¿Qué haces si los gastos superan el presupuesto?", "Calculo cuánto falta con una resta", "La diferencia dice cuánto falta para alcanzar.")],
    op=("Con esta tabla de ejemplo de un comercio pequeño (pesos): Arriendo $200.000, Sueldos $300.000, Insumos $150.000. El presupuesto es $700.000. Calcula el total de gastos y lo que sobra. Escribe una frase sin dar consejos.",
        "Total: 200.000 + 300.000 + 150.000 = 650.000. Sobra 700.000 − 650.000 = 50.000. Frase: «Los gastos suman $650.000 y sobran $50.000 del presupuesto».",
        ["suma bien el total", "resta bien lo que sobra", "frase clara con unidades"],
        ["hoja con los cálculos y la frase"],
        ["olvidar un gasto", "restar al revés"],
        "Pregunta: «¿qué gasto es el mayor y cuánto más que el menor?». Debe responder sueldos, $150.000 más."),
    reinforce="Anota tres cuentas inventadas de tu hogar y suma el total.",
    extend="Explica cómo cambia el total del mes si un gasto sube $5.000 y otro baja $5.000.",
)

# ===================================================== OAD-15 clase 6
F = ("Datos de ejemplo. Tabla de ventas de un almacén en dos meses (unidades): Pan: mes 1 → 50, mes 2 → 60. "
     "Leche: 40 → 35. Huevos: 30 → 45. Arroz: 25 → 25.")
build(
    O15, 6, F,
    use="Voy a comparar dos meses en una tabla y a explicar a otra persona qué subió, qué bajó y qué no cambió.",
    prior=["Sé restar números de dos cifras.", "Sé sumar columnas de una tabla.", "Sé qué es una diferencia."],
    explain=[
        "Una tabla puede tener dos columnas de datos para comparar, por ejemplo dos meses. Para saber cuánto cambió un producto, resta el dato menor al mayor. Si el segundo mes es mayor, subió; si es menor, bajó; si son iguales, no cambió.",
        "Con esos cálculos puedes armar una tabla nueva que diga cuánto subió o bajó cada producto: Pan sube 10, Leche baja 5, Huevos sube 15, Arroz no cambia. Esa tabla es información nueva que sale de los datos.",
        "Para explicarlo, empieza por lo más importante. Por ejemplo: «Subieron las ventas de pan y huevos, bajaron las de leche, y el arroz quedó igual». Luego agrega los números. Habla solo de lo que muestran los datos, sin inventar razones.",
    ],
    vocab=[("subir", "aumentar el dato de un mes a otro"), ("bajar", "disminuir el dato"), ("no cambiar", "quedar igual"), ("variación", "cuánto cambió un dato"), ("columna", "datos hacia abajo"), ("explicar", "contar con claridad qué muestran los datos")],
    worked=[
        ("Cuánto cambió", "En la ficha, ¿cuánto subió el pan?", ["Compara 50 y 60.", "Resta: 60 − 50 = 10."], "Subió 10 unidades"),
        ("Total de un mes", "¿Cuántas unidades se vendieron en el mes 1?", ["Suma la columna del mes 1: 50 + 40 + 30 + 25.", "El resultado es 145."], "145 unidades")
    ],
    mistakes=[("Decir que la leche subió porque 40 es un número grande.", "Se mira el valor y no la comparación.", "Compara los dos meses: 35 es menor que 40, por eso bajó."),
              ("Explicar con razones que el dato no muestra, como «la gente prefiere huevos».", "Se agrega una idea sin datos.", "Di solo lo que muestran los números.")],
    T=[
        ("=", "{F} ¿Cuánto subió el pan del mes 1 al mes 2?", "60-50", "Se resta el dato menor al mayor.", " unidades"),
        ("=", "{F} ¿Cuánto bajó la leche del mes 1 al mes 2?", "40-35", "Se resta el dato menor al mayor.", " unidades"),
        ("abc", "{F} ¿Qué producto no cambió?", "Arroz", "Pan", "Huevos", "El arroz tiene veinticinco en los dos meses."),
        ("=", "{F} ¿Cuántas unidades se vendieron en total en el mes 1?", "50+40+30+25", "Se suman los datos de la columna del mes uno.", " unidades"),
        ("=", "{F} ¿Cuántas unidades se vendieron en total en el mes 2?", "60+35+45+25", "Se suman los datos de la columna del mes dos.", " unidades"),
        ("=", "{F} ¿Cuántas unidades más se vendieron en el mes 2 que en el mes 1, en total?", "165-145", "Se restan los totales de los dos meses.", " unidades"),
        ("abc", "{F} ¿Qué producto tuvo el mayor aumento?", "Huevos", "Pan", "Leche", "Los huevos subieron quince unidades, más que el pan."),
        ("=", "{F} ¿Cuánto subieron los huevos?", "45-30", "Se resta el dato del primer mes al del segundo.", " unidades"),
        ("ab", "{F} ¿Subieron más los huevos o el pan?", "Los huevos, 15 contra 10", "El pan, 10 contra 15", "Quince unidades es mayor que diez, por eso los huevos subieron más."),
        ("=", "{F} ¿Cuántas unidades de leche y arroz se vendieron juntas en el mes 2?", "35+25", "Se suman las dos filas del mes dos.", " unidades"),
        ("abc", "{F} ¿Qué fila de una tabla de cambios es correcta?", "Leche: baja 5", "Leche: sube 5", "Leche: baja 40", "Cuarenta menos treinta y cinco es cinco, y es una baja."),
        ("=", "{F} Si el pan sube otras 10 unidades en el mes 3, ¿cuántas se venderían?", "60+10", "Se suma el aumento al dato del mes dos.", " unidades"),
        ("ab", "{F} ¿Qué frase explica mejor los datos?", "Subieron el pan y los huevos, bajó la leche y el arroz quedó igual", "La gente prefiere huevos porque es más rico", "La tabla solo muestra cantidades vendidas, no las razones de la gente."),
    ],
    ctx=("=", "El encargado de un almacén de ejemplo debe decidir cuántas bandejas de huevos pedir. Vendió 30 en el mes 1 y 45 en el mes 2. ¿Cuántas unidades más vendió en el mes 2?", "45-30", "Se resta el primer mes del segundo.", " unidades"),
    sc=[("¿Cómo sabes si un producto subió, bajó o quedó igual?", "Comparo el dato del mes 2 con el del mes 1", "La comparación de los dos datos define el cambio."),
        ("¿Qué operación da cuánto cambió?", "Una resta", "Restar el dato menor al mayor da la variación."),
        ("¿Se pueden explicar las razones de un cambio con la tabla?", "No, la tabla solo muestra cantidades", "Las razones de un cambio requieren otra información distinta.")],
    op=("Con esta tabla de ejemplo de una panadería (unidades vendidas, semana 1 → semana 2): Marraquetas 120 → 140, Hallullas 90 → 80, Pan de molde 30 → 30. Escribe una tabla de cambios y una explicación de dos frases para otra persona.",
        "Marraquetas sube 20; Hallullas baja 10; Pan de molde no cambia. Explicación: «Subieron las marraquetas y bajaron las hallullas; el pan de molde quedó igual. Se vendieron 240 en la semana 1 y 250 en la semana 2».",
        ["calcula bien los cambios", "dice subió, bajó o igual", "explica sin inventar razones"],
        ["hoja con la tabla de cambios y las dos frases"],
        ["restar al revés", "dar razones que los datos no muestran"],
        "Pregunta: «¿cómo sabes que bajaron las hallullas?». Debe comparar 90 con 80."),
    reinforce="Escribe una tabla de dos semanas de tus propios gastos de ejemplo y di qué subió y qué bajó.",
    extend="Explica por qué dos productos pueden tener el mismo cambio aunque vendan cantidades distintas.",
)

# ===================================================== OAD-15 clase 7
F = ("Datos de ejemplo. Gráfico de barras, escala de 5 en 5: «Asistentes a charlas vecinales por mes». "
     "Enero 15, Febrero 25, Marzo 20, Abril 35, Mayo 30. Meta del semestre: 150 asistentes.")
build(
    O15, 7, F,
    use="Voy a revisar lo aprendido: leer datos, comparar, calcular totales y cuánto falta para una meta.",
    prior=["Sé leer tablas y gráficos.", "Sé sumar y restar.", "Sé comparar con doble y mitad."],
    explain=[
        "Repasa el camino para resolver un problema con datos. Primero lee el título y mira qué mide cada eje. Segundo, identifica qué te preguntan y qué datos necesitas. Tercero, elige una operación: suma para totales, resta para diferencias y faltantes, multiplicación o división para doble y mitad.",
        "Después resuelve con cuidado y escribe la respuesta con su unidad. Por último, comprueba: ¿el resultado se parece a los números del gráfico?, ¿tiene sentido? En esta ficha el total es 125 y la meta es 150, por eso faltan 25 asistentes.",
        "Explicar tu razonamiento a otra persona te ayuda a notar errores. Puedes decir: «sumé las cinco barras y le resté el total a la meta». Reconocer qué parte te resulta fácil y cuál quieres repasar es una forma de aprender mejor.",
    ],
    vocab=[("meta", "cantidad que se quiere lograr"), ("total", "suma de los datos"), ("diferencia", "resultado de restar dos datos"), ("razonamiento", "los pasos con que llegaste a una respuesta"), ("comprobar", "revisar que el resultado tenga sentido"), ("faltante", "lo que falta para llegar a la meta")],
    worked=[
        ("Total y faltante", "En la ficha, ¿cuántos asistentes faltan para la meta?", ["Suma 15 + 25 + 20 + 35 + 30 = 125.", "Resta 150 − 125 = 25."], "25 asistentes"),
        ("Comparar dos meses", "¿Cuántos asistentes más hubo en abril que en enero?", ["Abril 35 y enero 15.", "Resta: 35 − 15 = 20."], "20 asistentes")
    ],
    mistakes=[("Sumar la meta al total para hallar lo que falta.", "Se confunde faltar con sumar.", "Resta el total a la meta."),
              ("No comprobar si el resultado tiene sentido.", "Se confía en el primer cálculo.", "Compara el resultado con los números del gráfico.")],
    T=[
        ("abc", "{F} ¿Cuál es el título del gráfico?", "Asistentes a charlas vecinales por mes", "Meta del semestre", "Barras de 5 en 5", "El título está entre comillas al inicio de la ficha."),
        ("{F} ¿Cuántos asistentes hubo en marzo?", "20 asistentes", "La barra de marzo llega a la marca veinte."),
        ("=", "{F} ¿Cuántos asistentes hubo en total?", "15+25+20+35+30", "Se suman las cinco barras.", " asistentes"),
        ("=", "{F} ¿Cuántos asistentes faltan para la meta del semestre?", "150-125", "Se resta el total a la meta.", " asistentes"),
        ("abc", "{F} ¿Qué mes tuvo más asistentes?", "Abril", "Febrero", "Mayo", "La barra más alta es la de abril, con treinta y cinco."),
        ("=", "{F} ¿Cuántos asistentes más hubo en abril que en enero?", "35-15", "Se resta el dato menor al mayor.", " asistentes"),
        ("ab", "{F} ¿Es Enero la mitad de Mayo?", "Sí: 15 es la mitad de 30", "No: es el triple", "Treinta dividido en dos es quince, que es el dato de enero."),
        ("=", "{F} ¿Cuántos asistentes hubo entre febrero y marzo?", "25+20", "Se suman las dos barras pedidas.", " asistentes"),
        ("=", "{F} ¿Cuántos asistentes NO hubo en abril?", "15+25+20+30", "Se suman todos los meses menos abril.", " asistentes"),
        ("abc", "{F} ¿Se alcanzó la meta de 150 asistentes?", "No, faltaron 25", "Sí, se superó por 25", "Sí, se alcanzó justo", "El total fue ciento veinticinco, menor que ciento cincuenta."),
        ("=", "{F} Si en junio asistieran 25, ¿cuántos asistentes habría en total en los seis meses?", "125+25", "Se suma el nuevo mes al total anterior.", " asistentes"),
        ("ab", "{F} Un compañero dice que febrero tuvo más asistentes que abril. ¿Es correcto?", "No: abril tuvo 35 y febrero 25", "Sí: febrero tuvo más", "Treinta y cinco es mayor que veinticinco, por eso abril tuvo más."),
        ("abc", "¿Qué haces al terminar de resolver un problema con datos?", "Compruebo que el resultado tenga sentido", "Borro los datos", "Cambio el título", "Revisar evita errores de cálculo y de lectura."),
    ],
    ctx=("=", "La organizadora de las charlas de ejemplo quiere saber cuántos asistentes hubo entre marzo y mayo para pedir material. Marzo 20, abril 35 y mayo 30. ¿Cuántos fueron?", "20+35+30", "Se suman las tres barras de esos meses.", " asistentes"),
    sc=[("¿Qué haces primero ante un gráfico?", "Leo el título y los ejes", "Así sé qué mide y cómo se lee."),
        ("¿Qué operación usas para un total?", "Suma", "El total junta todos los datos."),
        ("¿Qué haces si tu respuesta no se parece a los números del gráfico?", "Reviso la lectura y la cuenta", "Una respuesta muy distinta de los datos avisa que hay un error de lectura o de cálculo.")],
    op=("Con este gráfico de ejemplo de un huerto comunitario (kilos de verdura cosechados: Semana 1 20, Semana 2 25, Semana 3 40, Semana 4 35), escribe un total, una diferencia, cuánto falta para una meta de 150 kilos y una frase para explicarlo.",
        "Total: 20 + 25 + 40 + 35 = 120 kilos. Diferencia mayor y menor: 40 − 20 = 20. Faltan 150 − 120 = 30 kilos. Frase: «Se cosecharon 120 kilos y faltan 30 para la meta».",
        ["total correcto", "diferencia y faltante correctos", "frase clara con unidades"],
        ["hoja con cálculos y una frase"],
        ["sumar la meta", "olvidar una semana"],
        "Pregunta: «¿qué pasos usaste para llegar a la meta?». Debe contar sumar y luego restar."),
    reinforce="Haz un problema propio con la ficha de esta clase y resuélvelo.",
    extend="Explica por qué cambiar la meta cambia lo que falta, pero no el total.",
)
