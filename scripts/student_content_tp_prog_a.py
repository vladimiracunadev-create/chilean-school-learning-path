"""Programación TP 3.º y 4.º medio: OAE-01 (programas y rutinas con estructuras y bases de datos), OAE-02 (sistemas de información manufacturados) y OAE-03 (mantenimiento de bases de datos). Código breve y datos inventados; todo se razona a mano."""
from __future__ import annotations

from tp_prog_common import build

O1 = "TP-PROG-3y4-OAE-01"
O2 = "TP-PROG-3y4-OAE-02"
O3 = "TP-PROG-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (requerimiento de ejemplo, inventado). La «Librería Los Boldos» pide un programa que calcule el total de una venta. Programa de ejemplo (Python): "
     "precio = 1500 ; cantidad = 4 ; total = precio * cantidad ; print(total). La librería también guarda una tabla de clientes con nombre y teléfono (datos de ejemplo).")
build(
    O1, 1, F,
    use="Aprenderé qué es un requerimiento, qué piezas básicas tiene un programa (variables y estructuras) y qué cuidados exige trabajar con datos de una empresa.",
    prior=["Sé multiplicar y sumar números.", "Sé leer una tabla simple.", "Sé que una empresa tiene clientes y vende productos."],
    explain=[
        "Un programa es una secuencia de instrucciones que el computador sigue para resolver una tarea. Antes de escribirlo se aclara el requerimiento: lo que la empresa necesita que el programa haga. Un buen requerimiento es concreto y se puede comprobar, por ejemplo: «calcular el total de una venta como precio por cantidad».",
        "Un programa guarda valores en variables, que son nombres con un valor dentro (precio = 1500). Ordena las instrucciones con tres estructuras: la secuencia (una tras otra), el condicional (if: decide según una condición) y la repetición (for o while: repite instrucciones). Cuando hay muchos datos, se guardan en una base de datos, que organiza la información en tablas de registros.",
        "Programar en una empresa trae responsabilidades. Las tablas de clientes tienen datos personales (nombre, teléfono) y la norma vigente de protección de datos exige usarlos solo con permiso y para un fin claro. Además, un resultado no se da por bueno sin probarlo con datos de ejemplo y dejar un registro de quién lo hizo y qué cambió.",
    ],
    vocab=[("programa", "secuencia de instrucciones que resuelve una tarea"), ("requerimiento", "lo que la empresa necesita que el programa haga"), ("variable", "nombre que guarda un valor que el programa usa"), ("condicional", "estructura que decide según una condición (if)"), ("repetición", "estructura que repite instrucciones (for o while)"), ("base de datos", "conjunto organizado de tablas de registros"), ("dato personal", "dato que identifica a una persona, como su nombre o teléfono")],
    worked=[
        ("Leer un programa a mano", "Programa de ejemplo: precio = 2000 ; cantidad = 3 ; total = precio * cantidad. ¿Qué valor queda en total?", ["Se reemplazan las variables: total = 2000 * 3.", "Se multiplica: 2000 por 3."], "6000"),
        ("Reconocer un dato personal", "Una tabla de ejemplo tiene las columnas: nombre de la clienta, teléfono y precio del producto. ¿Cuáles columnas son datos personales?", ["El nombre y el teléfono identifican a una persona.", "El precio del producto no identifica a nadie."], "Nombre y teléfono"),
    ],
    mistakes=[("Escribir el programa sin preguntar qué necesita la empresa y adivinar el requerimiento.", "Un programa que no responde al requerimiento no sirve aunque funcione sin errores.", "Escribe el requerimiento con una frase comprobable y pídele a la jefatura que lo confirme."),
              ("Pasarle a un compañero la tabla de clientes completa «para probar».", "Los datos personales no se comparten sin permiso ni fin claro.", "Usa datos de ejemplo inventados para probar.")],
    T=[
        ("abc", "En Programación: ¿qué es un requerimiento?", "Lo que la empresa necesita que el programa haga", "Una instrucción escrita en Python", "El computador donde se ejecuta el programa", "El requerimiento describe la necesidad; el código y el equipo son la solución."),
        ("abc", "En Programación: ¿qué es una variable?", "Un nombre que guarda un valor que el programa usa", "Una tabla completa de la base de datos", "Un error que detiene el programa", "Una variable es un nombre con un valor dentro; no es una tabla ni un error."),
        ("abc", "¿Qué estructura repite instrucciones varias veces?", "La repetición (for o while)", "El condicional (if)", "La secuencia", "La repetición ejecuta de nuevo un bloque; el condicional decide y la secuencia solo ordena."),
        ("=", "{F} ¿Qué valor muestra el programa de la ficha?", "1500*4", "total es el precio multiplicado por la cantidad.", ""),
        ("abc", "{F} ¿Qué columna de la tabla de clientes es un dato personal?", "El nombre", "El precio de un cuaderno", "La cantidad de cuadernos en bodega", "El nombre identifica a una persona; el precio y las existencias no."),
        ("abc", "Programa de ejemplo: cantidad = 12 ; if cantidad >= 10: mensaje = «mayorista» ; else: mensaje = «detalle». ¿Qué texto queda en mensaje?", "mayorista", "detalle", "cantidad", "12 es mayor o igual que 10, entonces se cumple la condición del if."),
        ("=", "Programa de ejemplo: precio = 1500 ; cantidad = 7 ; total = precio * cantidad. ¿Qué valor queda en total?", "1500*7", "Se multiplica el precio por la cantidad vendida.", ""),
        ("abc", "¿Cuál es un requerimiento bien escrito para la librería?", "El programa debe calcular el total de una venta como precio por cantidad", "Hacer algo útil con las ventas", "Usar muchos bucles y muchas variables", "Un requerimiento claro dice qué debe hacer el programa y se puede comprobar."),
        ("ab", "{F} ¿Qué muestra el programa de la ficha si la cantidad vale 0?", "0, porque el precio multiplicado por cero da cero", "Un error, porque no se puede multiplicar por cero", "Multiplicar por cero es válido y el resultado es cero, por eso no hay error."),
        ("abc", "Una compañera propone copiar la tabla de clientes del ejemplo al celular para «trabajar en la casa», sin avisar a la jefa. ¿Qué corresponde?", "Pedir permiso y trabajar con datos de ejemplo inventados", "Copiarla igual porque es solo para trabajar", "Publicarla en una red social para pedir ayuda", "Los datos personales solo se llevan o comparten con permiso y un fin claro; para practicar sirven datos inventados."),
        ("abc", "Un programador entrega el programa sin probarlo con datos de ejemplo ni dejar registro de su cambio. ¿Qué riesgo crea?", "Dar por bueno un resultado sin verificación ni responsable", "Que el programa tenga demasiadas variables", "Que la empresa venda menos cuadernos", "Sin prueba ni registro nadie puede comprobar el resultado ni sabe quién lo cambió."),
        ("=", "Programa de ejemplo: precio = 2000 ; cantidad = 5 ; descuento = 500 ; total = precio * cantidad - descuento. ¿Qué valor queda en total?", "2000*5-500", "Primero se multiplica y después se resta el descuento.", ""),
        ("abc", "Programa de ejemplo: suma = 0 ; for v in [3, 5, 2]: suma = suma + v. Antes de repetir con el último valor, suma vale 8. ¿Qué valor tendrá suma al terminar el for?", "10", "8", "5", "Con el último valor 2 se hace 8 + 2, y eso da 10."),
    ],
    ctx=("abc", "La dueña de una librería de ejemplo dice: «Quiero saber cuánto vendí hoy». La programadora empieza a escribir código de inmediato. ¿Qué paso falta?", "Aclarar con la dueña el requerimiento: qué datos usar y qué resultado mostrar", "Cambiar el lenguaje de programación", "Borrar la tabla de clientes", "Primero se acuerda qué se necesita; solo después se programa."),
    sc=[
        ("En Programación: ¿qué es un requerimiento?", "Lo que la empresa necesita que el programa haga", "Se escribe antes de programar y se puede comprobar."),
        ("Nombra las tres estructuras básicas de un programa.", "Secuencia, condicional y repetición", "Ordenan las instrucciones: una tras otra, decidir o repetir."),
        ("¿Qué datos usas para practicar con una tabla de clientes?", "Datos de ejemplo inventados", "Los datos personales reales no se usan sin permiso y fin claro."),
    ],
    op=("Una panadería de ejemplo pide un programa que calcule el total de una venta de pan: precio de un kilo $1.800 y cantidad de kilos 3. Escribe (a) el requerimiento en una frase, (b) tres líneas de Python con precio, cantidad y total, (c) el valor que queda en total y (d) una frase sobre qué datos personales no pondrías en la prueba.",
        "(a) El programa debe calcular el total de una venta como precio por cantidad. (b) precio = 1800 ; cantidad = 3 ; total = precio * cantidad. (c) 5400. (d) No usaría nombres ni teléfonos reales de clientes; probaría con datos inventados.",
        ["escribe un requerimiento comprobable", "escribe el código con variables y calcula bien el total", "nombra datos personales que no se usan"],
        ["hoja con el requerimiento, el código y el valor calculado"],
        ["sumar en vez de multiplicar", "escribir un requerimiento vago", "usar datos reales en la prueba"],
        "Pregunta: «¿cómo sabes que tu programa responde a lo que pidió la panadería?». Si no responde, pídele que relea el requerimiento."),
    reinforce="Escribe una frase de requerimiento para un programa que sume los pesos de tres compras inventadas.",
    extend="Explica con un ejemplo inventado por qué un programa puede funcionar sin errores y aun así no cumplir el requerimiento.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (diseño de ejemplo, inventado). Requerimiento: «registrar productos con código, nombre y stock». Tabla «productos» (datos de ejemplo): "
     "código 1, cuaderno, stock 20; código 2, lápiz, stock 50; código 3, regla, stock 8. La columna «código» es la clave primaria. Roles: analista (aclara el requerimiento), "
     "programador (escribe el código), tester (prueba) y jefatura de proyecto (aprueba).")
build(
    O1, 2, F,
    use="Aprenderé los conceptos de bases de datos y estructuras de datos, los documentos del trabajo de programar y los roles de un equipo.",
    prior=["Sé qué es un programa, una variable y un requerimiento.", "Sé leer una tabla.", "Sé qué es una lista de valores."],
    explain=[
        "Una tabla de una base de datos tiene columnas (campos, como nombre o stock) y filas (registros, cada producto). La clave primaria es el campo que identifica un registro de forma única: dos productos nunca tienen el mismo código. En el programa, una lista guarda varios valores en orden (el primero está en la posición 0) y un diccionario guarda pares clave-valor, como {«código»: 1, «nombre»: «cuaderno»}.",
        "El trabajo de programar deja documentos: la especificación de requisitos (lo que se pide), el diagrama de flujo o el pseudocódigo (el plan del programa), el diccionario de datos (qué campos tiene cada tabla y de qué tipo) y la bitácora de cambios (quién modificó qué y cuándo). Esos documentos permiten que otra persona entienda y revise el trabajo.",
        "Cada rol tiene su responsabilidad. El analista aclara el requerimiento, el programador escribe el código, el tester prueba con datos de ejemplo y la jefatura de proyecto aprueba. Nadie se aprueba a sí mismo su propio trabajo: la revisión por otra persona detecta errores a tiempo. Además, solo se accede a los datos que el rol necesita.",
    ],
    vocab=[("tabla", "conjunto de filas y columnas de una base de datos"), ("registro", "fila de una tabla: un caso completo"), ("campo", "columna de una tabla: un dato de cada registro"), ("clave primaria", "campo que identifica un registro de forma única"), ("lista", "estructura que guarda varios valores en orden"), ("diccionario de datos", "documento que describe los campos de cada tabla"), ("bitácora", "registro de quién cambió qué y cuándo")],
    worked=[
        ("Leer un registro", "Tabla de ejemplo «alumnos»: id 1, Ana; id 2, Luis; id 3, Marta. ¿Cuál es el campo clave primaria y cuántos registros hay?", ["La clave primaria es el campo que no se repite: id.", "Cada fila es un registro: hay tres filas."], "Clave primaria: id; hay 3 registros"),
        ("Posición en una lista", "Lista de ejemplo: nombres = [«Ana», «Luis», «Marta»]. ¿Qué valor está en la posición 1?", ["Las posiciones parten desde 0: Ana es 0.", "La posición 1 es la segunda: Luis."], "Luis"),
    ],
    mistakes=[("Contar las posiciones de una lista desde 1 y decir que nombres[1] es «Ana».", "En Python las posiciones parten desde 0: la posición 1 es el segundo valor.", "Cuenta 0, 1, 2… al leer posiciones."),
              ("Usar el nombre del producto como clave primaria.", "Dos productos pueden llamarse igual; la clave primaria debe ser única.", "Usa un código que no se repita.")],
    T=[
        ("abc", "En Programación: ¿qué es un registro de una tabla?", "Una fila: un caso completo, como un producto", "Una columna con un solo tipo de dato", "El documento donde se anotan los cambios", "El registro es una fila de la tabla; la columna es un campo y el documento de cambios es la bitácora."),
        ("abc", "En Programación: ¿qué es la clave primaria?", "El campo que identifica cada registro de forma única", "La contraseña de la base de datos", "El campo con el valor más alto", "La clave primaria no se repite en la tabla; no es una contraseña."),
        ("abc", "¿Qué rol aclara el requerimiento antes de programar?", "El analista", "El tester", "La jefatura de proyecto al final", "El analista traduce la necesidad de la empresa en requisitos; el tester prueba."),
        ("=", "{F} ¿Cuántas unidades de stock suman los tres productos de la tabla?", "20+50+8", "Se suman los valores del campo stock de cada registro.", " unidades"),
        ("abc", "{F} ¿Cuál es el campo clave primaria de la tabla «productos»?", "código", "nombre", "stock", "El código no se repite y por eso identifica cada producto."),
        ("abc", "Lista de ejemplo: colores = [«rojo», «azul», «verde»]. ¿Qué valor está en la posición 2?", "verde", "azul", "rojo", "Las posiciones parten desde 0, así que la posición 2 es el tercer valor."),
        ("abc", "{F} Se quiere anotar qué campos tiene la tabla «productos» y de qué tipo es cada uno. ¿Qué documento corresponde?", "El diccionario de datos", "La bitácora de cambios", "El diagrama de flujo", "El diccionario de datos describe los campos y sus tipos."),
        ("=", "{F} Se agregan 15 unidades al stock de las reglas. ¿Cuál es el nuevo stock de las reglas?", "8+15", "Se suma lo que entra al stock anterior.", " unidades"),
        ("abc", "Lista de ejemplo: n = [4, 9, 2, 7]. ¿Cuántos valores tiene la lista y en qué posición está el 2?", "Tiene 4 valores y el 2 está en la posición 2", "Tiene 4 valores y el 2 está en la posición 3", "Tiene 3 valores y el 2 está en la posición 2", "Los valores 4, 9, 2 y 7 son cuatro; el 2 es el tercero, que está en la posición 2."),
        ("abc", "{F} El programador termina el código y dice: «yo mismo lo apruebo, no necesita prueba». ¿Qué principio se rompe?", "Nadie se aprueba a sí mismo su trabajo: lo revisa otra persona", "El diccionario de datos debe estar en inglés", "La tabla debe tener más columnas", "La revisión por otra persona, como el tester, permite detectar errores a tiempo."),
        ("abc", "{F} El tester necesita probar el programa con la tabla «productos». ¿Qué datos corresponde usar?", "Los datos de ejemplo de la ficha", "Una copia de la tabla de clientes reales", "Datos de familiares y amigos", "Se prueba con datos de ejemplo que no identifican a personas reales."),
        ("=", "{F} Se venden 12 cuadernos y 30 lápices. ¿Cuántas unidades quedan en stock entre cuadernos y lápices juntos?", "(20-12)+(50-30)", "A cada stock se le resta lo vendido y se suman los restantes.", " unidades"),
        ("abc", "Diccionario de ejemplo: p = {«código»: 2, «nombre»: «lápiz»}. ¿Qué valor devuelve p[«nombre»]?", "lápiz", "2", "nombre", "Un diccionario entrega el valor asociado a la clave consultada."),
    ],
    ctx=("abc", "En una empresa de ejemplo, una persona nueva del equipo de programación pide acceso a toda la base de datos «por si acaso». ¿Cuál es la respuesta responsable de la jefatura?", "Darle solo el acceso que su rol necesita y dejarlo anotado", "Darle acceso a todo para que no pregunte", "Negarle todo acceso aunque deba trabajar", "Cada rol accede solo a los datos que necesita y el acceso se registra."),
    sc=[
        ("En Programación: ¿para qué sirve la clave primaria?", "Para identificar cada registro de forma única", "Evita que dos registros se confundan."),
        ("¿En qué posición está el primer valor de una lista en Python?", "En la posición 0", "Las posiciones se cuentan desde 0."),
        ("¿Quién prueba el programa con datos de ejemplo?", "El tester, no quien lo escribió", "Una segunda persona detecta errores que el autor no ve."),
    ],
    op=("Una veterinaria de ejemplo quiere una tabla «mascotas» con los campos id, nombre de la mascota, especie y fecha de la última vacuna (datos inventados). Dibuja la tabla con tres registros de ejemplo, indica la clave primaria y explica en dos líneas qué dato personal del dueño no incluirías y quién del equipo revisaría tu diseño.",
        "Tabla: id 1, Luna, gato; id 2, Toby, perro; id 3, Kiwi, ave (con fecha de ejemplo). Clave primaria: id. No incluiría el nombre, teléfono ni dirección del dueño sin permiso. Lo revisaría el tester o la jefatura de proyecto, no yo mismo.",
        ["dibuja la tabla con campos y registros", "elige una clave primaria única", "nombra un dato personal que se evita y un revisor"],
        ["hoja con la tabla de tres registros y las dos líneas"],
        ["usar el nombre como clave primaria", "mezclar campos con registros", "revisar su propio diseño"],
        "Pregunta: «¿por qué el id y no el nombre es la clave primaria?». Si no responde, pídele que busque dos mascotas con el mismo nombre."),
    reinforce="Dibuja una tabla de tres libros inventados con id, título y año, y marca la clave primaria.",
    extend="Explica con un ejemplo inventado qué problema aparece si dos registros tienen la misma clave primaria.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Tabla «ventas» de la Librería Los Boldos: venta 1, importe 4000; venta 2, importe 1500; venta 3, importe 6500; venta 4, importe 3000. "
     "Rutina (Python): total = 0 ; mayores = 0 ; for v in [4000, 1500, 6500, 3000]: total = total + v ; if v > 3500: mayores = mayores + 1. "
     "Requerimiento: calcular el total vendido y contar cuántas ventas superan 3500.")
build(
    O1, 3, F,
    use="Aprenderé a seguir una rutina con repetición y condicional a mano (traza) y a comprobar si cumple el requerimiento.",
    prior=["Sé qué es una variable, una lista y una repetición.", "Sé qué es un condicional.", "Sé sumar y comparar números."],
    explain=[
        "La traza es seguir un programa a mano, instrucción por instrucción, anotando en una tabla el valor de cada variable. Es la forma más simple de comprobar que una rutina hace lo que se pidió antes de ejecutarla en un computador. Se anota una fila por cada vuelta de la repetición.",
        "Una rutina que recorre una lista usa for v in lista: en cada vuelta, v toma el siguiente valor. Un acumulador es una variable que parte en 0 y va sumando (total = total + v). Un contador es una variable que sube de uno en uno cuando se cumple una condición (mayores = mayores + 1). Los operadores de comparación son > (mayor), < (menor), >= (mayor o igual) y == (igual).",
        "Al terminar, se compara el resultado con el requerimiento y con un cálculo hecho por otra vía, como una suma directa. Si no coinciden, se busca el error en la traza y se deja anotado en la bitácora. Un resultado que nadie verificó no se entrega a la empresa.",
    ],
    vocab=[("traza", "seguimiento a mano de un programa anotando sus variables"), ("acumulador", "variable que suma valores en cada vuelta"), ("contador", "variable que sube cuando se cumple una condición"), ("comparación", "operación que da verdadero o falso (>, <, >=, ==)"), ("vuelta", "una pasada de la repetición por un valor"), ("verificación", "comprobar un resultado por otra vía")],
    worked=[
        ("Traza de un acumulador", "Rutina de ejemplo: s = 0 ; for v in [2, 4, 6]: s = s + v. ¿Cuánto vale s al final?", ["Vuelta 1: s = 0 + 2 = 2. Vuelta 2: s = 2 + 4 = 6.", "Vuelta 3: s = 6 + 6 = 12."], "12"),
        ("Traza de un contador", "Rutina de ejemplo: c = 0 ; for v in [5, 1, 8, 9]: if v > 6: c = c + 1. ¿Cuánto vale c?", ["Solo se cuentan los valores mayores que 6.", "Cumplen 8 y 9: c = 2."], "2"),
    ],
    mistakes=[("Contar un valor igual al límite cuando la condición dice «mayor que».", "Con v > 3500 el valor 3500 no cuenta, porque no es mayor, solo igual.", "Lee el operador con cuidado: > no incluye el límite, >= sí."),
              ("Dar por bueno el total sin hacer la suma directa.", "Un resultado sin verificación por otra vía puede traer un error escondido.", "Compara siempre con un cálculo hecho de otra forma.")],
    T=[
        ("abc", "En Programación: ¿qué es una traza?", "Seguir un programa a mano anotando los valores de sus variables", "Escribir el programa sin comentarios", "Borrar los errores del programa", "La traza permite comprobar la lógica antes de ejecutar el programa."),
        ("abc", "¿Qué hace un acumulador?", "Suma valores en cada vuelta de la repetición", "Cuenta solo cuando se cumple una condición", "Borra el valor anterior de la lista", "Un acumulador parte en 0 y suma en cada vuelta; el contador sube solo si se cumple una condición."),
        ("abc", "¿Qué significa v > 3500?", "v es mayor que 3500", "v es igual a 3500", "v es menor que 3500", "El símbolo > se lee «mayor que»."),
        ("=", "{F} ¿Cuánto vale total al terminar la rutina?", "4000+1500+6500+3000", "El acumulador suma los cuatro importes de la lista.", ""),
        ("abc", "{F} ¿Cuánto vale mayores al terminar la rutina?", "2", "3", "1", "Superan 3500 los valores 4000 y 6500; 3000 y 1500 no."),
        ("abc", "Rutina de ejemplo: c = 0 ; for v in [10, 20, 30]: if v >= 20: c = c + 1. ¿Cuánto vale c?", "2", "1", "3", "Con >= cuentan el 20 y el 30; el 10 no."),
        ("=", "Rutina de ejemplo: s = 0 ; for v in [7, 3, 9, 1]: s = s + v. ¿Cuánto vale s al final?", "7+3+9+1", "El acumulador suma uno por uno los valores de la lista.", ""),
        ("abc", "{F} En la vuelta del valor 6500, ¿qué ocurre con las variables?", "total sube a 12000 y mayores sube a 2", "total sube a 6500 y mayores se queda en 0", "total sube a 12000 y mayores se queda en 1", "Antes de 6500 el total era 5500 y mayores valía 1; el 6500 suma y también cuenta."),
        ("=", "{F} ¿Cuánto vale total justo después de la vuelta del valor 1500?", "4000+1500", "Va acumulado el primer valor más el segundo.", ""),
        ("abc", "Rutina de ejemplo: c = 0 ; for v in [3500, 4000, 3600]: if v > 3500: c = c + 1. Una persona dice que c vale 3. ¿Cuál es su error?", "Contó el 3500, que es igual al límite y no es mayor", "Sumó los valores en vez de contarlos", "Olvidó que la lista parte en la posición 0", "Con > solo cuentan 4000 y 3600, así que c vale 2."),
        ("abc", "{F} Un tester suma directamente 4000 + 1500 + 6500 + 3000 y obtiene el mismo total que la rutina. ¿Qué logró?", "Verificó el resultado por otra vía", "Cambió el requerimiento", "Eliminó la repetición del programa", "Una suma directa es un cálculo independiente que confirma el resultado."),
        ("=", "Rutina de ejemplo: p = 1 ; for v in [2, 3, 4]: p = p * v. ¿Cuánto vale p al final?", "2*3*4", "Es un acumulador que multiplica en cada vuelta, partiendo de 1.", ""),
        ("abc", "{F} Se quiere contar las ventas de 3500 o más. ¿Qué cambio hace falta en la condición de la rutina?", "Cambiar > por >=", "Cambiar total por mayores", "Cambiar el 0 inicial por 1", "Para incluir el límite se usa >=; con 3500 o más seguiría contando 2 ventas en este caso."),
    ],
    ctx=("abc", "Una rutina de ejemplo da 12.000 como total, pero la suma directa hecha por otra persona da 11.000. ¿Qué hace el equipo?", "Revisa la traza, encuentra el error y lo anota en la bitácora antes de entregar", "Entrega 12.000 porque lo calculó el computador", "Entrega 11.000 sin investigar por qué hubo diferencia", "Una diferencia entre dos vías de cálculo exige encontrar la causa y dejar registro."),
    sc=[
        ("En Programación: ¿para qué sirve una traza?", "Para comprobar a mano lo que hace un programa", "Anota cómo cambia cada variable en cada vuelta."),
        ("¿Con qué valor parte un acumulador de suma?", "Con 0", "Así el primer valor sumado queda tal cual."),
        ("¿Qué comparación incluye el límite: > o >=?", ">=", "El signo >= acepta el valor igual al límite."),
    ],
    op=("Una tienda de ejemplo tiene estas ventas: 2500, 4200, 3800, 1000. Rutina: total = 0 ; mayores = 0 ; for v in [2500, 4200, 3800, 1000]: total = total + v ; if v > 3000: mayores = mayores + 1. Haz la traza en una tabla (vuelta, v, total, mayores), escribe el resultado final y verifícalo con una suma directa.",
        "Vuelta 1: v 2500, total 2500, mayores 0. Vuelta 2: v 4200, total 6700, mayores 1. Vuelta 3: v 3800, total 10500, mayores 2. Vuelta 4: v 1000, total 11500, mayores 2. Resultado: total 11500 y mayores 2. Suma directa: 2500 + 4200 + 3800 + 1000 = 11500, coincide.",
        ["hace la traza con una fila por vuelta", "obtiene total y mayores correctos", "verifica con una suma directa"],
        ["tabla de traza con cuatro filas y la verificación"],
        ["saltarse una vuelta", "contar el valor 3000 como mayor que 3000", "no verificar por otra vía"],
        "Pregunta: «¿cómo confirmas que tu total es correcto?». Si no responde, pídele que lo calcule por otra vía."),
    reinforce="Haz la traza de s = 0 ; for v in [5, 5, 10]: s = s + v y anota el valor de s en cada vuelta.",
    extend="Explica con un ejemplo inventado qué cambia en la traza si el límite del condicional pasa de > a >=.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado). Tabla «clientes» de la Librería Los Boldos: id 1, Ana, ciudad Osorno; id 2, Beto, ciudad Puerto Montt; id 3, Carla, ciudad Osorno; id 4, Dani, ciudad Valdivia (nombres y datos de ejemplo). "
     "Consulta de ejemplo (SQL): SELECT nombre FROM clientes WHERE ciudad = «Osorno». Requerimiento: «listar los clientes de Osorno para un aviso de promoción, solo con quienes dieron su permiso».")
build(
    O1, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: elegir la estructura adecuada, leer una consulta a una base de datos y cuidar los datos personales.",
    prior=["Sé qué es una tabla, un registro y una clave primaria.", "Sé hacer una traza con una lista.", "Sé qué es un dato personal."],
    explain=[
        "Una consulta pide datos a una base de datos. En el lenguaje de consultas SQL, SELECT indica qué campos mostrar, FROM indica la tabla y WHERE filtra los registros que cumplen una condición. Por ejemplo, SELECT nombre FROM clientes WHERE ciudad = «Osorno» muestra solo los nombres de los clientes de esa ciudad. Con AND se exigen dos condiciones a la vez. Se lee a mano revisando fila por fila.",
        "El criterio técnico elige la estructura según la necesidad: una lista guarda valores en orden, un diccionario busca un valor por su clave y una tabla guarda muchos registros con los mismos campos. También valida las entradas: antes de usar un dato se comprueba que existe y que tiene el tipo esperado, por ejemplo que una cantidad no sea negativa.",
        "El criterio ético y legal pesa tanto como el técnico. Un aviso de promoción se manda solo a quienes dieron su permiso y se usa solo el dato que hace falta (el nombre, no toda la ficha). Las contraseñas nunca se guardan escritas tal cual: se guardan transformadas con una función de resumen (hash), y jamás se piden ni se escriben contraseñas reales en un ejercicio.",
    ],
    vocab=[("consulta", "pedido de datos a una base de datos"), ("SELECT", "parte de la consulta que indica qué campos mostrar"), ("FROM", "parte de la consulta que indica la tabla"), ("WHERE", "parte de la consulta que filtra registros por una condición"), ("validar", "comprobar que un dato es correcto antes de usarlo"), ("permiso", "autorización de la persona para usar sus datos"), ("hash", "resumen que se guarda en vez de la contraseña escrita")],
    worked=[
        ("Leer una consulta", "Tabla de ejemplo «autos»: id 1, rojo; id 2, azul; id 3, rojo. Consulta: SELECT id FROM autos WHERE color = «rojo». ¿Qué id muestra?", ["WHERE filtra: solo los autos de color rojo.", "Los rojos son id 1 e id 3."], "1 y 3"),
        ("Validar una entrada", "Un programa de ejemplo recibe una cantidad de cuadernos. ¿Qué se valida antes de calcular el total?", ["La cantidad debe ser un número.", "Además, no puede ser negativa."], "Que sea un número y que no sea negativo"),
    ],
    mistakes=[("Olvidar el WHERE y creer que la consulta muestra solo una ciudad.", "Sin WHERE la consulta muestra todos los registros de la tabla.", "Revisa que la condición del filtro esté escrita."),
              ("Guardar las contraseñas escritas tal cual en la tabla de usuarios.", "Si alguien accede a la tabla, ve todas las contraseñas.", "Guarda solo el hash de la contraseña y nunca la escribas en ejercicios.")],
    T=[
        ("abc", "En Programación: ¿qué hace WHERE en una consulta?", "Filtra los registros que cumplen una condición", "Elige la tabla de donde salen los datos", "Borra los registros de la tabla", "WHERE deja pasar solo los registros que cumplen la condición."),
        ("abc", "En Programación: ¿qué es validar un dato?", "Comprobar que es correcto antes de usarlo", "Guardarlo en dos tablas distintas", "Cambiar su tipo sin avisar", "Validar evita usar datos erróneos, como una cantidad negativa."),
        ("abc", "¿Cómo se guarda de forma segura la contraseña de un usuario?", "Transformada con un hash, nunca escrita tal cual", "Escrita tal cual en la tabla", "Pegada en una nota junto al computador", "El hash impide que quien vea la tabla lea la contraseña real."),
        ("abc", "{F} ¿Qué nombres muestra la consulta de la ficha?", "Ana y Carla", "Ana, Beto y Carla", "Beto y Dani", "Solo Ana y Carla tienen ciudad Osorno en la tabla."),
        ("=", "{F} ¿Cuántos clientes de la tabla viven en Osorno?", "1+1", "Se cuentan las filas que cumplen la condición del WHERE: Ana y Carla.", " clientes"),
        ("abc", "Tabla de ejemplo «autos»: id 1, rojo; id 2, azul; id 3, rojo; id 4, verde. ¿Qué id muestra SELECT id FROM autos WHERE color = «azul»?", "2", "1 y 3", "4", "Solo el auto con id 2 es azul."),
        ("abc", "{F} Solo Ana dio permiso para el aviso. ¿A quiénes se puede enviar?", "Solo a Ana", "A Ana y Carla porque viven en Osorno", "A los cuatro clientes de la tabla", "El criterio es el permiso; vivir en la ciudad no basta."),
        ("abc", "Un programa de ejemplo recibe la cantidad -4 de cuadernos. ¿Qué debe hacer?", "Rechazar el dato y pedir uno válido", "Calcular el total con -4", "Cambiarlo a 4 sin avisar", "Una cantidad negativa no es válida; se rechaza antes de calcular."),
        ("ab", "{F} Para el aviso solo hace falta el nombre. ¿Qué campos debe pedir la consulta?", "Solo nombre", "Nombre, ciudad y todos los datos de la ficha", "Se usa el mínimo de datos necesarios para el fin del aviso, es decir, solo el nombre."),
        ("abc", "{F} Una persona escribe SELECT nombre FROM clientes, sin WHERE. ¿Qué muestra?", "Los nombres de los cuatro clientes", "Solo los nombres de Osorno", "Solo el nombre del primer cliente", "Sin filtro se muestran todos los registros de la tabla."),
        ("abc", "Una compañera quiere probar el inicio de sesión con la contraseña real de su correo personal. ¿Qué corresponde?", "Usar una contraseña inventada de ejemplo y nunca la real", "Usar la real porque es solo una prueba", "Compartirla con el tester para que la compruebe", "Las contraseñas reales no se escriben ni comparten; en pruebas se usan datos inventados."),
        ("=", "Una lista de ejemplo tiene los stocks [12, 0, 7, 0, 5]. Se cuentan los productos sin stock (iguales a 0). ¿Cuántos son?", "1+1", "Hay dos valores iguales a 0 en la lista.", " productos"),
        ("abc", "Se necesita buscar el teléfono de un cliente por su id, sin recorrer todo. ¿Qué estructura conviene usar?", "Un diccionario con el id como clave", "Una lista sin orden", "Una variable por cada cliente", "El diccionario entrega el valor directo a partir de su clave."),
    ],
    ctx=("abc", "La jefa pide enviar el aviso de promoción a todos los clientes de la tabla, pero solo algunos dieron permiso. ¿Qué responde la programadora?", "Propone filtrar solo a quienes dieron permiso y deja el filtro anotado", "Envía a todos para cumplir con la jefa", "Se niega a trabajar sin dar explicaciones", "Se usan los datos solo con permiso; se explica y se deja constancia."),
    sc=[
        ("En Programación: ¿qué indica FROM en una consulta?", "La tabla de donde se sacan los datos", "FROM nombra la tabla; SELECT los campos."),
        ("¿Cómo se guarda una contraseña?", "Como hash, nunca escrita tal cual", "Así nadie que vea la tabla puede leerla."),
        ("¿A quién se le envía un aviso de promoción?", "Solo a quienes dieron su permiso", "Los datos personales se usan solo con autorización."),
    ],
    op=("Una peluquería de ejemplo tiene la tabla «clientas»: id 1, Eva, comuna Rengo, permiso sí; id 2, Fran, comuna Talca, permiso no; id 3, Gina, comuna Rengo, permiso sí (datos inventados). Escribe una consulta SQL que liste el nombre de las clientas de Rengo con permiso (campo permiso = «sí»), indica qué nombres muestra y explica en dos líneas qué dato no pedirías en la consulta.",
        "SELECT nombre FROM clientas WHERE comuna = «Rengo» AND permiso = «sí». Muestra Eva y Gina. No pediría el teléfono ni otros datos que no hacen falta para el aviso, y no usaría a Fran porque no dio permiso.",
        ["escribe SELECT, FROM y WHERE con las dos condiciones", "indica los nombres correctos", "justifica el mínimo de datos y el permiso"],
        ["hoja con la consulta, el resultado y las dos líneas"],
        ["olvidar la condición de permiso", "pedir todos los campos de la ficha", "incluir a una persona sin permiso"],
        "Pregunta: «¿por qué Fran queda fuera aunque podría vivir en Rengo?». Si no responde, pídele que relea la condición del permiso."),
    reinforce="Escribe una consulta que muestre los títulos de una tabla de libros inventados cuyo año sea posterior al 2010.",
    extend="Explica con un ejemplo inventado por qué pedir solo los campos necesarios reduce el riesgo con datos personales.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 5 (caso de ejemplo, inventado). «Distribuidora Mar Azul Ltda.» quiere instalar el sistema de información «StockFácil» (nombre de ejemplo), un programa de inventario ya elaborado por un proveedor, "
     "para controlar el stock de sus bodegas. Tiene 6 computadores. El proveedor de ejemplo cobra una licencia de $9.000 al mes por cada usuario (valor de ejemplo). Hoy el inventario está en una planilla compartida.")
build(
    O2, 1, F,
    use="Aprenderé qué es un sistema de información manufacturado, qué riesgos hay al instalarlo y qué cuidados hay que tener antes de empezar.",
    prior=["Sé qué es un programa y qué es un requerimiento.", "Sé qué es una base de datos.", "Sé multiplicar cifras en pesos."],
    explain=[
        "Un sistema de información reúne datos, programas y personas para entregar a la empresa la información que necesita, como un inventario o las ventas. Un sistema manufacturado es un software ya elaborado por un proveedor (un «paquete») que la empresa instala y configura, a diferencia del software a medida, que se programa desde cero para una empresa. Instalarlo bien es parte del trabajo del técnico.",
        "Antes de instalar se revisa la licencia: el permiso de uso que da el proveedor, que fija cuántos usuarios y equipos puede tener. Usar un programa sin licencia o con más usuarios de los permitidos es un riesgo legal y de seguridad. También se hace un respaldo (copia de los datos), se prueba en un ambiente de pruebas separado y se pide la autorización escrita de la jefatura.",
        "Los riesgos más comunes son perder datos por instalar sin respaldo, dejar usuarios con permisos de más y descargar el programa desde un sitio que no es del proveedor. Los datos personales de clientes y trabajadores se protegen según la norma vigente. Todo se anota en una bitácora: qué se instaló, quién lo hizo y con qué autorización.",
    ],
    vocab=[("sistema de información", "datos, programas y personas que entregan información a la empresa"), ("sistema manufacturado", "software ya elaborado por un proveedor, que se instala y configura"), ("software a medida", "software programado desde cero para una empresa"), ("licencia", "permiso de uso que fija usuarios y equipos"), ("respaldo", "copia de los datos para recuperarlos si algo falla"), ("ambiente de pruebas", "entorno separado para probar sin afectar el trabajo real"), ("autorización", "permiso escrito de quien decide")],
    worked=[
        ("Costo mensual de licencias", "Una empresa de ejemplo necesita licencias para 4 usuarios a $7.000 mensuales por usuario (valores de ejemplo). ¿Cuánto paga al mes?", ["Se multiplica el costo por cada usuario por la cantidad de usuarios.", "4 por 7.000."], "$28.000"),
        ("Manufacturado o a medida", "Una empresa de ejemplo compra un programa de facturas listo, lo instala y lo configura. ¿Es manufacturado o a medida?", ["El programa ya fue elaborado por un proveedor.", "La empresa solo lo instala y configura."], "Manufacturado"),
    ],
    mistakes=[("Instalar el programa directamente en el computador de trabajo para «ahorrar tiempo», sin respaldo.", "Si la instalación falla se pueden perder los datos reales.", "Haz el respaldo y prueba primero en un ambiente de pruebas."),
              ("Descargar el instalador desde un enlace que llegó por mensaje porque «dice ser del proveedor».", "Un instalador de origen dudoso puede traer programas maliciosos.", "Descarga solo desde el canal oficial indicado por el proveedor y confirma con la jefatura.")],
    T=[
        ("abc", "En Programación: ¿qué es un sistema manufacturado?", "Un software ya elaborado por un proveedor que la empresa instala y configura", "Un programa que se escribe desde cero para una sola empresa", "Una máquina de una fábrica", "El sistema manufacturado es un paquete ya hecho; el software a medida se programa desde cero."),
        ("abc", "En Programación: ¿qué es una licencia de software?", "El permiso de uso que fija cuántos usuarios y equipos pueden usarlo", "Una copia de los datos de la empresa", "Un manual con fotos de la pantalla", "La licencia es el permiso del proveedor; la copia de datos es el respaldo."),
        ("abc", "¿Para qué sirve un ambiente de pruebas?", "Para probar la instalación sin afectar el trabajo real", "Para guardar los respaldos por un año", "Para aumentar el número de usuarios", "Un entorno separado permite equivocarse sin perder datos reales."),
        ("=", "{F} ¿Cuántos pesos al mes cuestan las licencias si usan el sistema los 6 computadores, un usuario por computador?", "6*9000", "Se multiplica el costo mensual por usuario por la cantidad de usuarios.", " pesos"),
        ("abc", "{F} ¿Qué debe hacer el técnico antes de instalar StockFácil en la bodega?", "Respaldar los datos de la planilla y pedir autorización escrita", "Instalarlo en todos los computadores y avisar después", "Borrar la planilla para empezar de cero", "El respaldo protege los datos y la autorización asegura que la jefatura lo aprobó."),
        ("abc", "{F} La empresa tiene 6 computadores, pero se compraron solo 4 licencias. ¿Qué ocurre si instalan en los 6?", "Usan más usuarios de los permitidos, lo que es un riesgo legal", "No pasa nada porque el programa funciona igual", "Se pierden los datos de la planilla", "La licencia fija un máximo de usuarios; excederlo incumple el permiso."),
        ("=", "{F} Si el proveedor ofrece un 10 % menos solo en 2 de las licencias, que cuestan $9.000 cada una, ¿cuántos pesos se ahorran en total?", "2*9000//10", "El 10 % de 9.000 se multiplica por las dos licencias.", " pesos"),
        ("abc", "Un compañero dice: «instalemos el programa desde este enlace que llegó por mensaje, dice que es del proveedor». ¿Qué corresponde?", "Pedir el canal oficial al proveedor y confirmar con la jefatura", "Instalarlo porque el mensaje menciona al proveedor", "Reenviar el enlace a todos los trabajadores", "Un instalador de origen dudoso puede traer programas maliciosos."),
        ("abc", "{F} ¿Cuál de estos datos de StockFácil exige más cuidado según la norma vigente de protección de datos?", "Los nombres y teléfonos de clientes que guarde el sistema", "El nombre del producto «cuaderno»", "La cantidad de cajas en bodega", "Los datos personales identifican personas y se protegen; los datos de stock no."),
        ("abc", "El técnico instala un programa y no anota nada. Una semana después falla y nadie sabe qué versión se instaló ni con qué permiso. ¿Qué faltó?", "La bitácora con lo instalado, quién lo hizo y con qué autorización", "Más usuarios con permisos de administrador", "Un nombre más corto para el programa", "La bitácora deja constancia y permite encontrar la causa."),
        ("abc", "{F} En el ambiente de pruebas, ¿qué datos conviene usar con StockFácil?", "Datos de ejemplo inventados de productos", "La lista real de clientes con sus teléfonos", "Los datos personales de los trabajadores", "En pruebas se evita exponer datos reales."),
        ("=", "{F} La empresa de la ficha tiene 3 bodegas y quiere 2 usuarios por bodega con licencia. ¿Cuántos pesos al mes pagaría?", "3*2*9000", "Primero se calculan los usuarios y luego se multiplica por el valor de la licencia.", " pesos"),
        ("ab", "{F} Hoy el inventario está en una planilla compartida. ¿Qué sistema es StockFácil respecto de la empresa?", "Manufacturado, porque el proveedor ya lo elaboró", "A medida, porque la empresa lo usa", "El proveedor lo elaboró antes y la empresa solo lo instala, por eso es manufacturado."),
    ],
    ctx=("abc", "La jefa de una empresa de ejemplo quiere que el sistema funcione «para mañana» y pide saltarse el respaldo y la prueba. ¿Qué responde el técnico?", "Explicar el riesgo de perder datos y proponer un plan breve con respaldo y prueba", "Aceptar sin decir nada para evitar problemas", "Negarse a instalar el sistema sin dar razones", "El técnico informa el riesgo y propone una alternativa; la decisión queda registrada."),
    sc=[
        ("En Programación: ¿qué diferencia hay entre software manufacturado y a medida?", "El manufacturado ya está elaborado por un proveedor; el a medida se programa para una empresa", "Cambia quién lo elaboró y para quién."),
        ("¿Qué se hace antes de instalar un sistema?", "Respaldo, prueba y autorización escrita", "Estos tres pasos reducen el riesgo de perder datos."),
        ("¿Desde dónde se descarga un instalador?", "Del canal oficial del proveedor", "Un sitio dudoso puede traer programas maliciosos."),
    ],
    op=("Una clínica dental de ejemplo quiere instalar un sistema de agenda de citas manufacturado en 5 computadores; la licencia cuesta $6.000 al mes por usuario (valor de ejemplo). Calcula el costo mensual y escribe un plan de cuatro líneas con lo que harías antes de instalar, qué datos personales debes proteger y quién debe autorizar.",
        "Costo: 5 por 6.000 = 30.000 pesos al mes. Plan: 1) pedir autorización escrita a la jefatura; 2) hacer respaldo de la agenda actual; 3) probar en un ambiente de pruebas con pacientes inventados; 4) anotar en la bitácora. Datos personales: nombres y teléfonos de pacientes, que se usan solo con permiso y fin claro.",
        ["calcula bien el costo mensual", "incluye respaldo, prueba, autorización y bitácora", "nombra los datos personales que se protegen"],
        ["hoja con el cálculo y el plan de cuatro líneas"],
        ["instalar sin respaldo", "probar con datos reales de pacientes", "olvidar la autorización"],
        "Pregunta: «¿qué pasa si la instalación falla y no hiciste el respaldo?». Si no sabe, pídele que ordene sus pasos otra vez."),
    reinforce="Escribe tres riesgos de instalar un programa descargado de un sitio no oficial y una forma de evitar cada uno.",
    extend="Explica con un ejemplo inventado cuándo convendría un software a medida en vez de uno manufacturado.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 6 (documentos de ejemplo, inventados). Para instalar «StockFácil» el técnico recibe: (1) la ficha de requisitos mínimos del proveedor (memoria 8 GB, espacio libre 40 GB, sistema operativo compatible); "
     "(2) el acuerdo de licencia; (3) el manual de instalación; (4) un acta de aceptación que firma la jefatura al final. Roles: usuario clave (conoce el trabajo diario), administrador del sistema (configura cuentas y permisos), "
     "técnico (instala) y proveedor (da soporte). Computador de ejemplo: memoria 8 GB, espacio libre 25 GB.")
build(
    O2, 2, F,
    use="Aprenderé los conceptos y documentos de una instalación de software y los roles de quienes participan.",
    prior=["Sé qué es un sistema manufacturado y una licencia.", "Sé qué es un respaldo.", "Sé comparar cifras."],
    explain=[
        "Los requisitos mínimos son las condiciones que debe cumplir un equipo para que el programa funcione: memoria, espacio libre en disco, sistema operativo y a veces conexión. La memoria (RAM) es el espacio donde el equipo trabaja mientras el programa está abierto, y se mide en gigabytes (GB). El espacio libre en disco es donde se guarda el programa y sus datos. Si el equipo no cumple, no se instala.",
        "La instalación se apoya en documentos. El acuerdo de licencia dice qué se puede y qué no se puede hacer con el programa. El manual de instalación entrega los pasos del proveedor: se sigue tal cual y no se improvisa. La bitácora anota lo realizado y el acta de aceptación deja constancia de que el sistema quedó funcionando y fue recibido por la jefatura.",
        "Cada rol tiene límites. El usuario clave explica cómo se trabaja a diario y prueba que el sistema sirva, el administrador del sistema crea cuentas con el mínimo de permisos necesarios, el técnico instala y el proveedor da soporte según el acuerdo. Una cuenta de administrador compartida entre varias personas es un riesgo: no se sabe quién hizo cada cambio.",
    ],
    vocab=[("requisitos mínimos", "condiciones que debe cumplir un equipo para ejecutar el programa"), ("memoria (RAM)", "espacio de trabajo del equipo mientras el programa está abierto"), ("gigabyte (GB)", "unidad para medir memoria o espacio de almacenamiento"), ("acuerdo de licencia", "documento que fija qué se puede hacer con el programa"), ("acta de aceptación", "documento que firma la jefatura al recibir el sistema"), ("administrador del sistema", "persona que configura cuentas y permisos"), ("usuario clave", "persona que conoce el trabajo diario y prueba el sistema")],
    worked=[
        ("Cumplir requisitos", "Un programa de ejemplo pide memoria de 4 GB y 20 GB libres. Un equipo tiene 8 GB de memoria y 15 GB libres. ¿Cumple?", ["La memoria cumple: 8 es mayor o igual que 4.", "El espacio no cumple: 15 es menor que 20."], "No cumple, falta espacio libre"),
        ("Elegir el documento", "El técnico duda cómo seguir un paso de la instalación. ¿Qué documento consulta?", ["Los pasos del proveedor están escritos en un documento.", "Ese documento es el manual de instalación."], "El manual de instalación"),
    ],
    mistakes=[("Instalar aunque el equipo no cumpla los requisitos mínimos, «a ver si funciona».", "El programa puede quedar lento o fallar y dañar el trabajo diario.", "Compara el equipo con la ficha de requisitos antes de instalar."),
              ("Usar la misma cuenta de administrador para todo el equipo.", "No se puede saber quién hizo cada cambio y se amplía el daño si se filtra.", "Crea cuentas individuales con los permisos mínimos necesarios.")],
    T=[
        ("abc", "En Programación: ¿qué son los requisitos mínimos de un programa?", "Las condiciones que debe cumplir un equipo para ejecutarlo", "El precio mínimo de la licencia", "Los datos personales del usuario", "Los requisitos mínimos son técnicos y se comparan con el equipo."),
        ("abc", "En Programación: ¿para qué sirve un acta de aceptación?", "Para dejar constancia de que la jefatura recibió el sistema funcionando", "Para listar los pasos de instalación", "Para respaldar los datos del sistema", "El acta la firma quien recibe el trabajo, al final."),
        ("abc", "¿Qué rol crea cuentas de usuario con permisos mínimos?", "El administrador del sistema", "El proveedor desde su oficina sin avisar", "El cliente que usa el sistema", "El administrador del sistema configura cuentas y permisos."),
        ("abc", "{F} ¿Cumple el computador de ejemplo los requisitos mínimos?", "No, porque el espacio libre de 25 GB es menor que 40 GB", "Sí, porque la memoria es de 8 GB", "Sí, porque el manual de instalación está completo", "Aunque la memoria cumple, el espacio libre de 25 GB no llega a los 40 GB pedidos."),
        ("=", "{F} ¿Cuántos GB de espacio libre faltan al computador de ejemplo para cumplir el requisito?", "40-25", "Se resta el espacio libre al espacio pedido.", " GB"),
        ("abc", "{F} ¿Qué documento dice si se puede usar el programa en más de 6 computadores?", "El acuerdo de licencia", "El acta de aceptación", "La ficha de requisitos mínimos", "La licencia fija los usos permitidos del programa."),
        ("abc", "{F} Una usuaria clave propone dejar a todos los trabajadores con cuenta de administrador. ¿Qué corresponde?", "Dar a cada persona solo los permisos que su trabajo necesita", "Aceptar para evitar pedir permisos cada vez", "Compartir una sola cuenta de administrador", "El permiso mínimo reduce el daño por errores o filtraciones."),
        ("=", "{F} Un computador de ejemplo tiene 60 GB libres y el programa ocupa 40 GB. ¿Cuántos GB libres quedan después de instalar?", "60-40", "Se resta lo que ocupa el programa al espacio libre.", " GB"),
        ("abc", "{F} Si un paso del manual de instalación dice algo distinto de lo que el técnico acostumbra hacer, ¿qué corresponde?", "Seguir el manual y consultar al proveedor si hay duda", "Hacerlo como siempre, sin leer", "Saltarse el paso", "El manual entrega los pasos que el proveedor garantiza."),
        ("abc", "Una empresa de ejemplo tiene computadores con 4 GB, 8 GB y 16 GB de memoria. El programa pide 8 GB como mínimo. ¿Cuántos computadores cumplen la memoria?", "2", "1", "3", "Cumplen el de 8 GB y el de 16 GB; el de 4 GB no."),
        ("abc", "El proveedor entrega por correo una clave y pide a la empresa publicarla en un grupo abierto de mensajería. ¿Qué corresponde?", "No publicarla: la clave de licencia se comparte solo con quien corresponde", "Publicarla para que todos instalen", "Imprimirla y pegarla en la puerta", "Una clave de licencia es reservada y se comparte solo con el personal autorizado."),
        ("=", "{F} El proveedor de ejemplo tarda 3 horas en dar soporte por cada falla y hay 4 fallas en el mes. ¿Cuántas horas de soporte son?", "3*4", "Se multiplican las horas por la cantidad de fallas.", " horas"),
        ("ab", "{F} Al terminar, la jefatura firma el acta de aceptación. ¿Qué indica esa firma?", "Que recibió el sistema funcionando", "Que el proveedor debe pagar la licencia", "Con la firma la jefatura deja constancia de haber recibido el trabajo y no del pago del proveedor."),
    ],
    ctx=("abc", "El técnico de una empresa de ejemplo descubre que el computador de la contadora no cumple el requisito de memoria. ¿Qué hace?", "Informa a la jefatura, propone ampliar la memoria o usar otro equipo y espera la decisión", "Instala igual y espera que funcione", "Cambia los requisitos escritos para que parezcan cumplidos", "No se alteran los documentos; se informa y se decide con la jefatura."),
    sc=[
        ("En Programación: ¿qué dicen los requisitos mínimos?", "Qué condiciones debe cumplir un equipo para ejecutar el programa", "Se comparan con el equipo antes de instalar."),
        ("¿Quién firma el acta de aceptación?", "La jefatura", "Deja constancia de que recibió el sistema funcionando."),
        ("¿Por qué no se comparte una cuenta de administrador?", "Porque no se sabría quién hizo cada cambio", "Las cuentas individuales permiten rastrear quién hizo cada cambio."),
    ],
    op=("Un colegio de ejemplo quiere instalar un programa de biblioteca. Requisitos mínimos: memoria 4 GB y 30 GB libres. Equipos: A (4 GB, 50 GB libres), B (8 GB, 20 GB libres), C (2 GB, 80 GB libres). Indica cuál equipo cumple, cuál documento consultarías para seguir la instalación, quién firma el acta y cómo darías permisos a la bibliotecaria.",
        "Cumple el equipo A (4 GB y 50 GB). B no cumple por espacio y C no cumple por memoria. Para instalar se sigue el manual de instalación. El acta la firma la jefatura. A la bibliotecaria se le crea una cuenta personal con los permisos mínimos que necesita para su trabajo.",
        ["compara cada equipo con ambos requisitos", "nombra el documento y la persona que firma", "propone permisos mínimos y cuenta individual"],
        ["tabla con los tres equipos y el cumplimiento"],
        ["mirar solo la memoria", "aceptar el equipo B", "dar cuenta de administrador a la bibliotecaria"],
        "Pregunta: «¿qué condición falla en los equipos B y C?». Si no responde, pídele que revise cada requisito por separado."),
    reinforce="Escribe los requisitos mínimos de un programa de ejemplo y compáralos con las cifras de un equipo inventado.",
    extend="Explica con un ejemplo inventado por qué el acta de aceptación protege tanto a la empresa como al técnico.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 7 (caso de ejemplo, inventado). La «Constructora Cerro Verde Ltda.» necesita un sistema para controlar materiales. Requerimientos: (R1) al menos 5 usuarios a la vez; (R2) funcionar sin internet; "
     "(R3) generar un informe de stock; (R4) costo máximo de $60.000 al mes. Opciones de ejemplo: Paquete A: 10 usuarios, requiere internet, informe de stock, $45.000 al mes. "
     "Paquete B: 8 usuarios, funciona sin internet, informe de stock, $55.000 al mes. Paquete C: 4 usuarios, funciona sin internet, informe de stock, $30.000 al mes.")
build(
    O2, 3, F,
    use="Aprenderé a analizar en papel qué sistema manufacturado cumple los requerimientos de una empresa y a justificar la elección.",
    prior=["Sé qué son los requisitos de un sistema y una licencia.", "Sé comparar valores con un máximo o un mínimo.", "Sé calcular costos mensuales."],
    explain=[
        "Elegir un sistema manufacturado es comparar lo que la empresa necesita con lo que ofrece cada paquete. Se escribe una tabla con los requerimientos en las filas y los paquetes en las columnas, y se marca si cada uno cumple. Un requerimiento obligatorio debe cumplirse sí o sí; si no se cumple, el paquete queda descartado. Un requerimiento deseable suma puntos pero no descarta.",
        "Al analizar se revisan también los límites: cuántos usuarios simultáneos tolera (usuarios a la vez), si exige conexión a internet, cuánto cuesta al mes y qué soporte entrega el proveedor. El costo se calcula con la licencia por usuario o con un valor fijo, según lo diga el acuerdo, sin inventar descuentos que no están escritos.",
        "La decisión se escribe con dos evidencias y se revisa si cambia una condición. Por ejemplo, si el presupuesto bajara, ¿sigue siendo válida la elección? Quien decide es la jefatura; el técnico entrega el análisis, deja constancia de los datos usados y no esconde un requisito que no se cumple.",
    ],
    vocab=[("requerimiento obligatorio", "condición que el sistema debe cumplir sí o sí"), ("requerimiento deseable", "condición que suma valor pero no descarta"), ("usuarios simultáneos", "personas que usan el sistema a la vez"), ("presupuesto", "monto máximo que la empresa puede gastar"), ("descartar", "dejar fuera una opción que no cumple un requisito obligatorio"), ("evidencia", "dato del caso que respalda la decisión")],
    worked=[
        ("Descartar por un requisito", "Una empresa de ejemplo necesita 5 usuarios a la vez. El paquete X permite 3 usuarios y el paquete Y permite 6. ¿Qué paquete se descarta?", ["El requisito es obligatorio: 5 usuarios.", "El paquete X permite 3, que son menos de 5."], "Se descarta el paquete X"),
        ("Costo con presupuesto", "El presupuesto de ejemplo es $50.000 al mes. El paquete Y cuesta $42.000. ¿Cumple el presupuesto?", ["Se compara 42.000 con el máximo 50.000.", "42.000 es menor o igual que 50.000."], "Sí, cumple"),
    ],
    mistakes=[("Elegir el paquete más barato sin revisar si cumple los requerimientos obligatorios.", "Un paquete barato que no cumple un obligatorio no resuelve el problema de la empresa.", "Descarta primero lo que no cumple y compara después entre los que quedan."),
              ("Anotar que un paquete «cumple» un requisito sin tener el dato en la ficha.", "Una afirmación sin evidencia puede llevar a una elección equivocada.", "Cita el dato de la ficha o pide al proveedor que lo confirme por escrito.")],
    T=[
        ("abc", "En Programación: ¿qué es un requerimiento obligatorio?", "Una condición que el sistema debe cumplir sí o sí", "Una condición que da puntos extra si se cumple", "Una condición que solo importa al proveedor", "Si no se cumple un obligatorio, la opción se descarta."),
        ("abc", "¿Qué significa «usuarios simultáneos»?", "Personas que usan el sistema al mismo tiempo", "Personas que tienen cuenta aunque no se conecten", "Personas que pagan la licencia", "Los simultáneos son los que están conectados a la vez."),
        ("abc", "{F} ¿Qué paquete se descarta por exigir internet, si el requerimiento R2 es obligatorio?", "El paquete A", "El paquete B", "El paquete C", "Solo el paquete A requiere internet y R2 pide funcionar sin internet."),
        ("abc", "{F} ¿Qué paquete se descarta por no tener los 5 usuarios a la vez de R1?", "El paquete C", "El paquete A", "El paquete B", "El paquete C solo permite 4 usuarios, que son menos que 5."),
        ("abc", "{F} Si R1 a R4 son obligatorios, ¿qué paquete cumple todo?", "El paquete B", "El paquete A", "El paquete C", "El paquete B tiene 8 usuarios, funciona sin internet, informe de stock y cuesta menos de 60.000."),
        ("=", "{F} ¿Cuántos pesos al mes sobran del presupuesto con el paquete B?", "60000-55000", "Se resta el costo del paquete al presupuesto máximo.", " pesos"),
        ("abc", "{F} Una compañera dice: «elijamos el paquete C porque es el más barato». ¿Cuál es el error?", "No cumple el requerimiento de 5 usuarios a la vez", "El paquete C no tiene informe de stock", "El paquete C requiere internet", "El paquete C permite 4 usuarios; es más barato, pero no cumple R1."),
        ("=", "{F} Si la empresa contrata el paquete B durante 6 meses, ¿cuántos pesos paga en total?", "55000*6", "Se multiplica el costo mensual por la cantidad de meses.", " pesos"),
        ("abc", "{F} El presupuesto baja a $50.000 al mes. ¿Qué pasa con la elección del paquete B?", "Ya no cumple R4 y habría que revisar la decisión", "Sigue cumpliendo todo sin cambios", "El paquete A pasa a cumplir R2", "55.000 supera el nuevo máximo de 50.000."),
        ("abc", "{F} El proveedor del paquete B dice de palabra que puede rebajar el costo, pero no lo deja escrito. ¿Qué se usa para decidir?", "El costo escrito de $55.000", "El costo de la rebaja dicha de palabra", "El costo del paquete A", "Se decide con evidencia escrita; las promesas verbales no cuentan."),
        ("=", "{F} Suponte que el paquete B cobrara $9.000 al mes por usuario (valor de ejemplo, en lugar del precio fijo) y se necesitan 5 usuarios. ¿Cuántos pesos al mes serían?", "5*9000", "Se multiplica el valor por usuario por la cantidad de usuarios.", " pesos"),
        ("abc", "El jefe de la constructora de ejemplo decide contratar otro paquete que no cumple un obligatorio. ¿Qué debe hacer el técnico?", "Dejar por escrito el análisis y el requisito que no se cumple", "Ocultar el requisito para evitar discusiones", "Cambiar el requerimiento sin avisar", "El técnico informa con evidencia; la decisión es de la jefatura y queda registrada."),
        ("ab", "{F} Si el requisito R2 (sin internet) pasara a ser solo deseable, ¿podría considerarse el paquete A?", "Sí, aunque con menor puntaje", "No, el paquete A se descarta siempre", "Un deseable no descarta; el paquete A cumple R1, R3 y R4, y solo le falta R2."),
    ],
    ctx=("abc", "Una empresa de ejemplo tiene en la mesa dos paquetes que cumplen todo. ¿Cómo se desempata de forma responsable?", "Con un criterio escrito, como el soporte del proveedor y el costo total, anotado en el informe", "Con la opinión del técnico sin dejar registro", "Escogiendo el nombre más conocido", "El criterio debe ser comprobable y quedar escrito."),
    sc=[
        ("En Programación: ¿qué pasa si un paquete no cumple un requerimiento obligatorio?", "Se descarta", "El obligatorio es una condición que no puede faltar."),
        ("¿Con qué se respalda una decisión?", "Con evidencia: datos de la ficha o por escrito", "Las afirmaciones sin dato no sirven."),
        ("¿Quién toma la decisión final de qué sistema contratar?", "La jefatura", "El técnico entrega el análisis, pero decide la jefatura."),
    ],
    op=("Una clínica de ejemplo necesita un sistema con: (R1) 3 usuarios a la vez, obligatorio; (R2) funcionar sin internet, obligatorio; (R3) costo máximo $40.000 al mes, obligatorio. Paquete P: 5 usuarios, sin internet, $38.000. Paquete Q: 3 usuarios, requiere internet, $20.000. Paquete R: 2 usuarios, sin internet, $25.000. Haz la tabla de cumplimiento, elige uno con dos evidencias y explica qué cambiaría si el costo máximo bajara a $35.000.",
        "P cumple R1, R2 y R3 (5 usuarios, sin internet, 38.000). Q falla R2. R falla R1. Elijo P: tiene 5 usuarios (más de 3) y cuesta 38.000, menos que 40.000. Si el máximo bajara a 35.000, P ya no cumpliría R3 y ninguno cumpliría todo: habría que revisar los requisitos con la jefatura.",
        ["hace la tabla de cumplimiento", "elige con dos evidencias", "revisa la decisión al cambiar el presupuesto"],
        ["tabla de tres paquetes y tres requisitos, y la conclusión"],
        ["elegir por precio sin mirar obligatorios", "no citar evidencias", "no revisar el cambio de presupuesto"],
        "Pregunta: «¿qué dato de la ficha respalda tu elección?». Si no responde, pídele que marque las evidencias en el enunciado."),
    reinforce="Inventa tres paquetes de software con usuarios y costo, y descarta uno por un requisito obligatorio.",
    extend="Explica con un ejemplo inventado cuándo un requerimiento deseable podría convertirse en obligatorio.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 8 (plan de instalación de ejemplo, inventado). Tareas de «Distribuidora Mar Azul Ltda.» para instalar StockFácil, desordenadas: (a) firmar el acta de aceptación; (b) pedir autorización escrita; "
     "(c) instalar y configurar en el ambiente de pruebas; (d) hacer el respaldo de los datos actuales; (e) capacitar a los usuarios; (f) instalar en los computadores de trabajo; (g) probar con datos de ejemplo. "
     "Espacio: el programa ocupa 40 GB, los datos 15 GB y se guardan 2 copias de respaldo de los datos (15 GB cada una). Ventana de instalación de ejemplo: sábado de 9:00 a 12:00.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: ordenar un plan de instalación, calcular el espacio necesario y decidir con registro.",
    prior=["Sé qué es un respaldo, un ambiente de pruebas y un acta.", "Sé sumar y restar espacio en GB.", "Sé calcular horas."],
    explain=[
        "Un plan de instalación ordena las tareas para reducir el riesgo. El orden lógico es: pedir autorización, hacer el respaldo, instalar en el ambiente de pruebas, probar con datos de ejemplo, instalar en los equipos de trabajo, capacitar a los usuarios y, al final, firmar el acta de aceptación. Cada paso se anota en la bitácora con fecha y responsable.",
        "El plan incluye un plan de reversa: qué se hace si algo sale mal, por ejemplo volver a la versión anterior y restaurar el respaldo. Además, se calcula el espacio necesario sumando el programa, los datos y las copias de respaldo, y se compara con el espacio libre del equipo. También se planifica la ventana de instalación: un horario en que se interrumpe lo menos posible el trabajo.",
        "La seguridad forma parte del plan: cuentas con permisos mínimos, claves de licencia y contraseñas guardadas por quien corresponde (nunca en mensajes abiertos) y datos de prueba inventados. Si el plan no se puede cumplir en el tiempo o el espacio disponible, el técnico informa antes y no recorta pasos para llegar a la hora.",
    ],
    vocab=[("plan de instalación", "lista ordenada de tareas para instalar un sistema"), ("plan de reversa", "pasos para volver atrás si algo sale mal"), ("ventana de instalación", "horario acordado para instalar con menos interrupciones"), ("restaurar", "recuperar los datos desde un respaldo"), ("capacitación", "enseñanza a los usuarios para usar el sistema"), ("responsable", "persona a cargo de una tarea")],
    worked=[
        ("Ordenar tareas", "Tareas de ejemplo: (a) instalar en equipos de trabajo; (b) respaldar datos; (c) pedir autorización. ¿Cuál es el orden correcto?", ["Primero se pide la autorización.", "Luego se respalda y recién después se instala."], "c, b, a"),
        ("Espacio total", "Un sistema de ejemplo ocupa 30 GB, sus datos 10 GB y se guarda un respaldo de 10 GB. ¿Cuántos GB se necesitan en total?", ["Se suman programa, datos y respaldo.", "30 + 10 + 10."], "50 GB"),
    ],
    mistakes=[("Instalar en los equipos de trabajo antes de probar en el ambiente de pruebas.", "Si falla, se interrumpe el trabajo real y se pueden perder datos.", "Prueba primero con datos de ejemplo y recién después instala en los equipos."),
              ("Recortar la capacitación y la bitácora para llegar a la hora.", "Los usuarios cometen errores y nadie puede revisar lo hecho.", "Informa que el plan no cabe en el tiempo y pide más tiempo.")],
    T=[
        ("abc", "En Programación: ¿qué es un plan de reversa?", "Los pasos para volver atrás si la instalación sale mal", "La lista de usuarios con permiso de administrador", "El listado de precios de las licencias", "El plan de reversa permite recuperar la situación anterior."),
        ("abc", "{F} ¿Cuál es la primera tarea del plan?", "(b) pedir autorización escrita", "(f) instalar en los computadores de trabajo", "(a) firmar el acta de aceptación", "Sin autorización no se parte; el acta se firma al final."),
        ("abc", "{F} ¿Qué tarea va inmediatamente después de pedir la autorización?", "(d) hacer el respaldo de los datos actuales", "(e) capacitar a los usuarios", "(f) instalar en los equipos de trabajo", "El respaldo protege los datos antes de tocar nada."),
        ("=", "{F} ¿Cuántos GB se necesitan en total para el programa, los datos y las dos copias de respaldo?", "40+15+15+15", "Se suman el programa, los datos y cada copia de respaldo.", " GB"),
        ("abc", "{F} ¿Qué tarea va inmediatamente antes de (f) instalar en los computadores de trabajo?", "(g) probar con datos de ejemplo", "(a) firmar el acta de aceptación", "(e) capacitar a los usuarios", "Se prueba antes de pasar al trabajo real."),
        ("abc", "{F} ¿Cuál es la última tarea del plan?", "(a) firmar el acta de aceptación", "(d) hacer el respaldo", "(c) instalar en el ambiente de pruebas", "El acta cierra el trabajo recibido y funcionando."),
        ("=", "{F} Un computador de ejemplo tiene 100 GB libres. ¿Cuántos GB quedan libres después de ocupar el espacio total que calculaste (40 + 15 + 15 + 15)?", "100-85", "Se resta el espacio total al espacio libre.", " GB"),
        ("=", "{F} ¿Cuántas horas dura la ventana de instalación del sábado?", "12-9", "Se restan la hora de inicio a la hora de término.", " horas"),
        ("abc", "{F} La instalación en los equipos de trabajo falla a mitad de la ventana. ¿Qué hace el técnico según el plan de reversa?", "Vuelve a la versión anterior, restaura el respaldo si hace falta y lo anota en la bitácora", "Sigue sin informar para no perder tiempo", "Borra los datos y empieza de cero", "El plan de reversa recupera el estado anterior y la bitácora deja constancia."),
        ("abc", "{F} Falta tiempo y alguien propone saltarse la capacitación. ¿Qué corresponde?", "Informar que no cabe y pedir más tiempo", "Saltarla sin avisar", "Capacitar solo a la jefatura y registrar que se hizo con todos", "Recortar pasos aumenta los errores; se informa y se pide más tiempo."),
        ("abc", "Para dar acceso al sistema, la administradora envía por un mensaje abierto la contraseña inicial de cada trabajador. ¿Cuál es el problema?", "Cualquiera que vea el mensaje podría usar la contraseña", "La contraseña inicial es demasiado corta", "Los trabajadores no necesitan acceso", "Las contraseñas no se envían en mensajes abiertos; se entregan de forma segura y se cambian al primer ingreso."),
        ("=", "{F} Un computador de ejemplo ya usa 70 GB de su disco de 120 GB. ¿Cuántos GB libres tiene?", "120-70", "El espacio libre es el total menos lo usado.", " GB"),
        ("abc", "{F} Con ese computador (50 GB libres), ¿alcanza el espacio para el programa y los datos, 55 GB en total?", "No, faltan 5 GB", "Sí, sobran 5 GB", "Sí, justo alcanza", "50 GB libres son menos que los 55 GB necesarios."),
    ],
    ctx=("abc", "Dos días antes de la ventana, el técnico ve que el respaldo no cabe en el disco previsto. ¿Qué hace?", "Avisa a la jefatura, propone otro disco o mover la fecha y deja constancia", "Instala sin respaldo para llegar a tiempo", "No dice nada y espera que alcance", "Informar a tiempo permite resolver sin riesgo."),
    sc=[
        ("En Programación: ¿qué tarea va primero en un plan de instalación?", "La autorización escrita", "Sin autorización no se toca ningún equipo."),
        ("¿Qué se hace si la instalación falla?", "Aplicar el plan de reversa y anotarlo", "Vuelve al estado anterior y deja registro."),
        ("¿Cómo se calcula el espacio necesario?", "Se suman programa, datos y respaldos", "Se compara el total con el espacio libre."),
    ],
    op=("Una escuela de ejemplo instalará un programa de notas. Ocupa 20 GB, los datos 5 GB y se guardan 2 respaldos de 5 GB. El computador tiene 40 GB libres. Calcula el espacio total y si alcanza, ordena estas tareas: probar con datos de ejemplo, pedir autorización, respaldar, firmar el acta, instalar en el computador de trabajo; y escribe qué incluirías en el plan de reversa.",
        "Espacio: 20 + 5 + 5 + 5 = 35 GB; hay 40 GB libres, alcanza y sobran 5 GB. Orden: pedir autorización, respaldar, probar con datos de ejemplo, instalar en el computador de trabajo, firmar el acta. Plan de reversa: volver a la versión anterior, restaurar el respaldo y anotar lo ocurrido en la bitácora.",
        ["calcula el espacio y lo compara", "ordena las cinco tareas", "describe un plan de reversa con bitácora"],
        ["hoja con el cálculo, el orden y el plan de reversa"],
        ["olvidar un respaldo en la suma", "instalar antes de probar", "no registrar en bitácora"],
        "Pregunta: «¿qué haces si la instalación falla?». Si no responde, pídele que escriba los pasos de reversa."),
    reinforce="Escribe en orden los pasos de un plan de instalación que tú diseñes para un programa de ejemplo, con quién es responsable de cada uno.",
    extend="Explica con un ejemplo inventado por qué la bitácora ayuda a encontrar la causa de una falla semanas después.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 9 (caso de ejemplo, inventado). El «Club Deportivo Las Araucarias» (nombre de ejemplo) guarda en una base de datos la tabla «socios»: id 1, Hugo, cuota al día; id 2, Inés, cuota atrasada; id 3, Jorge, cuota al día; "
     "id 4, Karen, cuota atrasada (datos de ejemplo). Mantenimiento es el trabajo periódico de cuidar la base de datos: respaldar, actualizar datos, corregir errores y revisar permisos. "
     "Instrucción de ejemplo (SQL): UPDATE socios SET cuota = «al día» WHERE id = 2.")
build(
    O3, 1, F,
    use="Aprenderé qué es el mantenimiento de una base de datos, por qué hay que actualizarla con cuidado y qué normas de privacidad y seguridad se respetan.",
    prior=["Sé qué es una tabla, un registro y una clave primaria.", "Sé leer una consulta con SELECT y WHERE.", "Sé qué es un respaldo."],
    explain=[
        "El mantenimiento de una base de datos es el cuidado periódico para que los datos sigan correctos, disponibles y seguros. Incluye respaldar, actualizar y corregir registros, eliminar datos que ya no se necesitan y revisar quién tiene permiso de modificar. Una base de datos descuidada llena de duplicados, datos vacíos y errores entrega información equivocada a la empresa.",
        "Para cambiar datos se usan instrucciones: INSERT agrega un registro nuevo, UPDATE modifica registros existentes y DELETE elimina registros. UPDATE y DELETE actúan sobre todos los registros de la tabla si falta el WHERE, que los limita. Un UPDATE o un DELETE sin WHERE es uno de los errores más peligrosos, porque cambia o borra todo.",
        "Por eso se trabaja con cuidado: se hace un respaldo antes de cambiar, se prueba en una copia, solo cambia datos quien tiene permiso y cada cambio se anota en la bitácora. Los datos personales de los socios se guardan según la norma vigente de protección de datos y solo mientras se necesiten.",
    ],
    vocab=[("mantenimiento", "cuidado periódico de la base de datos"), ("INSERT", "instrucción que agrega un registro nuevo"), ("UPDATE", "instrucción que modifica registros existentes"), ("DELETE", "instrucción que elimina registros"), ("duplicado", "registro repetido que no debería estar"), ("copia de prueba", "copia de la base de datos para ensayar cambios sin riesgo")],
    worked=[
        ("Leer un UPDATE", "Tabla de ejemplo: id 1, cuota atrasada; id 2, cuota atrasada. Instrucción: UPDATE socios SET cuota = «al día» WHERE id = 1. ¿Qué cambia?", ["WHERE limita el cambio al registro con id 1.", "El id 2 queda igual."], "Solo el id 1 pasa a «al día»"),
        ("UPDATE sin WHERE", "La misma tabla de ejemplo con 2 registros y la instrucción UPDATE socios SET cuota = «al día». ¿Cuántos registros cambian?", ["Sin WHERE, la instrucción actúa sobre toda la tabla.", "Cambian los dos registros."], "2 registros"),
    ],
    mistakes=[("Ejecutar un DELETE sin WHERE para «limpiar» un registro.", "Sin WHERE se borran todos los registros de la tabla.", "Escribe siempre el WHERE y comprueba con un SELECT qué registros afectará."),
              ("Cambiar datos directamente en la base real sin respaldo ni autorización.", "Un error puede perder datos sin forma de recuperarlos.", "Haz el respaldo, prueba en una copia y pide autorización.")],
    T=[
        ("abc", "En Programación: ¿qué hace la instrucción UPDATE?", "Modifica registros que ya existen", "Agrega un registro nuevo", "Muestra los datos sin cambiarlos", "UPDATE modifica; INSERT agrega y SELECT muestra."),
        ("abc", "En Programación: ¿qué hace la instrucción DELETE?", "Elimina registros", "Respalda la tabla", "Cambia el nombre de un campo", "DELETE quita registros de la tabla."),
        ("abc", "¿Qué se debe hacer antes de modificar datos de la base real?", "Hacer un respaldo", "Apagar el computador", "Cambiar el nombre de la tabla", "El respaldo permite recuperar los datos si el cambio sale mal."),
        ("abc", "{F} ¿Qué registro cambia la instrucción UPDATE de la ficha?", "El socio con id 2, Inés", "Todos los socios de la tabla", "El socio con id 1, Hugo", "WHERE id = 2 limita el cambio al registro de Inés."),
        ("=", "{F} ¿Cuántos socios quedan con cuota atrasada después del UPDATE de la ficha?", "2-1", "De los dos socios atrasados, uno (Inés) pasó a estar al día.", " socio"),
        ("=", "{F} Si faltara el WHERE y el UPDATE actuara sobre toda la tabla, ¿cuántos socios quedarían con cuota «al día»?", "4", "Sin WHERE se cambian los cuatro registros de la tabla.", " socios"),
        ("abc", "Un compañero escribe DELETE FROM socios para quitar al socio con id 3. ¿Qué ocurre?", "Se borran todos los registros de la tabla", "Se borra solo el registro con id 3", "No se borra nada", "Falta el WHERE id = 3; sin filtro se borran todos."),
        ("abc", "{F} ¿Qué parte debería añadirse a DELETE FROM socios para borrar solo a Jorge?", "WHERE id = 3", "SET id = 3", "FROM id = 3", "WHERE limita la instrucción al registro con id 3."),
        ("abc", "Dos registros de socios son exactamente iguales (mismo nombre y mismos datos). ¿Qué problema es?", "Un duplicado que ensucia la base de datos", "Una clave primaria bien usada", "Un respaldo", "Los duplicados distorsionan conteos y se corrigen en el mantenimiento."),
        ("abc", "{F} Una ayudante del club pide a la encargada la tabla completa de socios con sus datos «para revisarla en su casa». ¿Qué corresponde?", "Pedir autorización y usar solo los datos necesarios, en un equipo seguro", "Enviársela por un mensaje abierto", "Subirla a una red social para que otros ayuden", "Los datos personales se comparten con permiso, fin claro y por un canal seguro."),
        ("abc", "El administrador cambia datos en la base real un viernes sin respaldo ni registro del cambio, y el lunes faltan registros. ¿Qué dos medidas habrían ayudado?", "El respaldo previo y la bitácora de cambios", "Más duplicados y más columnas", "Dar permiso de modificar a todos", "El respaldo permite restaurar y la bitácora muestra qué se cambió."),
        ("=", "La tabla de ejemplo tiene 120 registros y se eliminan 8 duplicados con un DELETE bien filtrado. ¿Cuántos registros quedan?", "120-8", "Se restan los registros eliminados.", " registros"),
        ("abc", "{F} Se agregó un socio nuevo con INSERT. ¿Cuántos registros tiene ahora la tabla?", "5", "4", "6", "Los 4 registros de la ficha más el nuevo suman 5."),
    ],
    ctx=("abc", "La encargada del club de ejemplo pide cambiar la cuota de todos los socios a «al día» porque «ya pagaron», pero no hay lista de pagos. ¿Qué responde el técnico?", "Pide la lista de pagos, respalda y cambia solo los registros que corresponden, anotándolo", "Ejecuta el UPDATE sin WHERE para terminar rápido", "Se niega y borra la tabla", "Se cambia solo lo respaldado por evidencia y todo queda registrado."),
    sc=[
        ("En Programación: ¿qué pasa con un UPDATE sin WHERE?", "Cambia todos los registros de la tabla", "WHERE limita a los registros que cumplen la condición."),
        ("¿Qué haces antes de cambiar datos reales?", "Hago un respaldo y pido autorización", "Así puedo recuperar los datos si algo falla."),
        ("¿Para qué sirve la bitácora de cambios?", "Para saber quién cambió qué y cuándo", "Permite revisar lo hecho y corregir errores después."),
    ],
    op=("Un taller de ejemplo tiene la tabla «pedidos»: id 1, estado «pendiente»; id 2, «pendiente»; id 3, «listo» (datos inventados). Quieren marcar como «listo» solo el pedido 1. Escribe la instrucción UPDATE correcta, indica cómo quedaría la tabla, explica qué pasaría si olvidas el WHERE y escribe qué harías antes de ejecutarla.",
        "UPDATE pedidos SET estado = «listo» WHERE id = 1. La tabla queda: id 1 listo, id 2 pendiente, id 3 listo. Sin WHERE, los tres pedidos quedarían «listo», lo que sería un error. Antes haría un respaldo, probaría en una copia y anotaría el cambio en la bitácora.",
        ["escribe el UPDATE con WHERE", "indica el resultado correcto de la tabla", "explica el riesgo y la medida previa"],
        ["hoja con la instrucción, la tabla final y la explicación"],
        ["olvidar el WHERE", "cambiar el pedido equivocado", "no hacer respaldo"],
        "Pregunta: «¿qué registros cambiaría tu instrucción?». Si no responde, pídele que simule la instrucción fila por fila."),
    reinforce="Escribe un DELETE con WHERE para eliminar un registro de una tabla de libros inventados.",
    extend="Explica con un ejemplo inventado cómo un UPDATE sin WHERE podría afectar una decisión de la empresa.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 10 (documentos y roles de ejemplo, inventados). Base de datos «Biblioteca Escolar» con tablas «libros» (id, título, copias) y «préstamos» (id, id_libro, alumno). El campo «id_libro» de «préstamos» apunta al «id» de «libros»: es una clave foránea. "
     "Documentos: plan de mantención (qué se hace y cada cuánto), solicitud de cambio autorizada, bitácora y registro de respaldos. Roles: administrador de la base de datos (DBA, cuida la base), "
     "desarrollador (escribe las rutinas), usuario (usa los datos) y jefatura (autoriza). Datos de ejemplo: libro 1, «Cuentos del sur», copias 3; libro 2, «Ciencia fácil», copias 2.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos de la integridad de los datos, los documentos de mantención y los roles de quienes cuidan una base de datos.",
    prior=["Sé qué hacen INSERT, UPDATE y DELETE.", "Sé qué es una clave primaria.", "Sé qué es un respaldo."],
    explain=[
        "La integridad de los datos significa que están completos, sin contradicciones y relacionados correctamente. Una clave foránea es un campo de una tabla que apunta a la clave primaria de otra: así, cada préstamo señala a qué libro corresponde. Si se borra un libro que tiene préstamos, los préstamos quedan apuntando a algo que no existe y se rompe la integridad.",
        "El respaldo completo copia todos los datos de la base, y restaurar consiste en devolver los datos desde esa copia cuando algo falla. Los respaldos se guardan en un lugar distinto del equipo original y se prueban de vez en cuando, porque un respaldo que nunca se ha restaurado puede no servir. Los documentos del trabajo son el plan de mantención, la solicitud de cambio autorizada, la bitácora y el registro de respaldos.",
        "Los roles se reparten responsabilidades: el administrador de la base de datos (DBA) cuida el respaldo, los permisos y el rendimiento; el desarrollador escribe las rutinas; el usuario solo ve y modifica lo que necesita; y la jefatura autoriza los cambios. El principio del menor privilegio dice que cada persona recibe solo los permisos mínimos para su trabajo.",
    ],
    vocab=[("integridad", "datos completos, sin contradicciones y bien relacionados"), ("clave foránea", "campo que apunta a la clave primaria de otra tabla"), ("respaldo completo", "copia de todos los datos de la base"), ("restaurar", "devolver los datos desde una copia"), ("plan de mantención", "documento que dice qué se hace y cada cuánto"), ("DBA", "administrador de la base de datos"), ("menor privilegio", "dar solo los permisos mínimos necesarios")],
    worked=[
        ("Reconocer la clave foránea", "Tablas de ejemplo: «pedidos» (id, id_cliente) y «clientes» (id, nombre). ¿Qué campo es clave foránea?", ["La clave foránea apunta a otra tabla.", "id_cliente apunta al id de clientes."], "id_cliente"),
        ("Integridad rota", "Se borra el cliente 5 de «clientes», pero «pedidos» tiene un pedido con id_cliente = 5. ¿Qué pasa con la integridad?", ["El pedido apunta a un cliente que ya no existe.", "Eso es una contradicción entre las tablas."], "Se rompe la integridad: el pedido queda sin cliente"),
    ],
    mistakes=[("Guardar los respaldos en el mismo equipo donde está la base de datos.", "Si el equipo se daña, se pierden los datos y las copias a la vez.", "Guarda los respaldos en un lugar distinto y compruébalos."),
              ("Dar permisos de DBA a todos los desarrolladores «para que no pidan ayuda».", "Se viola el menor privilegio y un error afecta toda la base.", "Da a cada rol solo los permisos mínimos necesarios.")],
    T=[
        ("abc", "En Programación: ¿qué es una clave foránea?", "Un campo que apunta a la clave primaria de otra tabla", "El campo que identifica un registro dentro de su propia tabla", "Una copia de seguridad de la tabla", "La clave foránea relaciona dos tablas; la primaria identifica dentro de una tabla."),
        ("abc", "En Programación: ¿qué es restaurar una base de datos?", "Devolver los datos desde una copia de respaldo", "Borrar los datos antiguos", "Cambiar el nombre de la base", "Restaurar recupera los datos a partir del respaldo."),
        ("abc", "¿Qué dice el principio del menor privilegio?", "Cada persona recibe solo los permisos mínimos para su trabajo", "Todos reciben los mismos permisos", "Solo el desarrollador puede ver los datos", "Menos permisos reduce el daño de un error o una filtración."),
        ("abc", "{F} ¿Qué campo de «préstamos» es la clave foránea?", "id_libro", "alumno", "id de la tabla préstamos", "id_libro apunta al id de la tabla libros."),
        ("abc", "{F} Se borra el libro 2 de «libros», pero «préstamos» tiene un préstamo con id_libro = 2. ¿Qué problema aparece?", "Se rompe la integridad: el préstamo apunta a un libro que no existe", "Se duplica el libro 2", "Se cambia el nombre del alumno", "La clave foránea queda apuntando a un registro borrado."),
        ("abc", "{F} Quien aprueba una modificación a las tablas es...", "La jefatura, con una solicitud de cambio autorizada", "El usuario que la pidió, sin papel", "El proveedor de internet", "La jefatura autoriza y el cambio queda documentado."),
        ("=", "{F} Entre los dos libros de ejemplo, ¿cuántas copias hay en total?", "3+2", "Se suman las copias de cada libro.", " copias"),
        ("abc", "{F} Una persona de la biblioteca solo debe consultar los libros. ¿Qué permiso conviene darle?", "Solo lectura de la tabla libros", "Permiso para borrar tablas", "Permiso de DBA", "El menor privilegio da solo lo necesario para consultar."),
        ("=", "{F} Se prestan 2 copias del libro 1. ¿Cuántas copias quedan disponibles de ese libro?", "3-2", "Se restan las copias prestadas a las copias totales.", " copias"),
        ("abc", "El respaldo se guarda en el mismo computador de la base y ese equipo se daña. ¿Qué ocurre?", "Se pierden los datos y la copia a la vez", "Solo se pierde la copia", "No pasa nada porque el respaldo está completo", "Una copia en el mismo equipo no protege de la falla del equipo."),
        ("abc", "Un respaldo se hizo hace un año y nunca se probó. ¿Qué riesgo tiene?", "Puede no funcionar al restaurarlo cuando haga falta", "Es siempre perfecto", "Ocupa menos espacio", "Solo probar la restauración demuestra que el respaldo sirve."),
        ("=", "El plan de mantención de ejemplo dice: respaldo completo cada 7 días. En 28 días, ¿cuántos respaldos se hacen?", "28//7", "Se divide el período por la frecuencia del respaldo.", " respaldos"),
        ("ab", "{F} El DBA quiere borrar un libro con préstamos pendientes. ¿Qué corresponde?", "Revisar primero los préstamos y registrar la solicitud autorizada", "Borrarlo ya, para ordenar la tabla", "Borrar el libro dejaría préstamos apuntando a un registro inexistente; se revisa y se registra."),
    ],
    ctx=("abc", "Una desarrolladora nueva pide acceso total a la base de datos de producción «para trabajar más rápido». ¿Cuál es la respuesta correcta de la jefatura?", "Darle una copia de prueba y permisos mínimos sobre la base real", "Darle acceso total como al resto", "No darle acceso a nada", "El menor privilegio y la copia de prueba protegen los datos reales."),
    sc=[
        ("En Programación: ¿para qué sirve una clave foránea?", "Para relacionar una tabla con otra", "Apunta a la clave primaria de la otra tabla."),
        ("¿Dónde se guarda un respaldo?", "En un lugar distinto del equipo original", "Así sobrevive si el equipo falla."),
        ("¿Qué es el menor privilegio?", "Dar solo los permisos mínimos necesarios", "Reduce el daño que puede causar un error."),
    ],
    op=("Una ferretería de ejemplo tiene las tablas «productos» (id, nombre) y «ventas» (id, id_producto, cantidad). Indica cuál campo es clave foránea, qué problema ocurriría si se borra un producto vendido, qué permisos darías a la cajera y dónde guardarías los respaldos.",
        "La clave foránea es id_producto de ventas. Si se borra un producto vendido, las ventas quedarían apuntando a un producto que no existe y se rompería la integridad. A la cajera le daría permisos mínimos, por ejemplo registrar ventas y consultar productos. Los respaldos irían en un lugar distinto del equipo original, probando de vez en cuando la restauración.",
        ["identifica la clave foránea", "explica el problema de integridad", "propone permisos mínimos y respaldo en otro lugar"],
        ["hoja con las cuatro respuestas"],
        ["llamar clave foránea al id de la propia tabla", "dar permisos de administrador a la cajera", "guardar el respaldo en el mismo equipo"],
        "Pregunta: «¿qué pasaría con las ventas si borraras un producto?». Si no responde, pídele que dibuje la flecha entre las dos tablas."),
    reinforce="Dibuja dos tablas inventadas relacionadas por una clave foránea y marca el campo que las une.",
    extend="Explica con un ejemplo inventado por qué se prueba la restauración de un respaldo y no basta con crearlo.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 11 (caso de ejemplo, inventado). Tabla «inventario» de la «Ferretería El Roble» (nombre de ejemplo): id 1, tornillos, stock 40, activo sí; id 2, clavos, stock 5, activo sí; id 3, martillos, stock 0, activo sí; id 4, serruchos, stock 12, activo sí. "
     "Rutina de mantención (Python): alertas = [] ; for p in productos: if p[«stock»] < 10: alertas.append(p[«nombre»]). Instrucciones SQL: (1) UPDATE inventario SET stock = stock + 20 WHERE id = 2 ; (2) UPDATE inventario SET activo = «no» WHERE stock = 0.")
build(
    O3, 3, F,
    use="Aprenderé a analizar en papel qué efecto tiene una rutina o una instrucción de mantenimiento sobre una tabla y a verificar el resultado.",
    prior=["Sé hacer la traza de una repetición con condicional.", "Sé leer UPDATE con WHERE.", "Sé qué es una lista de diccionarios."],
    explain=[
        "Analizar un caso de mantenimiento es predecir en papel el estado de la tabla después de una rutina, antes de ejecutarla de verdad. Se copia la tabla, se aplica cada instrucción en orden y se escribe cómo queda. Así se descubren errores como afectar registros de más o dejar datos incoherentes.",
        "Una rutina de mantención suele recorrer una lista de registros: for p in productos: toma un registro por vuelta, p[«stock»] lee el campo stock y alertas.append(nombre) agrega un nombre a la lista alertas. Con SQL, UPDATE inventario SET stock = stock + 20 aumenta en 20 el valor que ya tenía el campo, solo en los registros que cumplen el WHERE.",
        "Después de aplicar los cambios se verifica: se cuenta cuántos registros quedaron, se compara con lo esperado y se anota en la bitácora. Si el resultado no coincide, no se entrega; se corrige y se vuelve a probar en la copia. Nunca se prueba una rutina de cambio directamente en la base real.",
    ],
    vocab=[("alertas", "lista de productos que requieren atención"), ("append", "instrucción que agrega un valor al final de una lista"), ("stock", "cantidad de unidades disponibles"), ("estado de la tabla", "datos que tiene la tabla en un momento"), ("verificar", "comprobar que el resultado es el esperado")],
    worked=[
        ("Aplicar un UPDATE aritmético", "Tabla de ejemplo: id 1, stock 6. Instrucción: UPDATE tabla SET stock = stock + 4 WHERE id = 1. ¿Cuál es el stock final?", ["El nuevo valor es el valor anterior más 4.", "6 + 4."], "10"),
        ("Rutina con condición", "Rutina de ejemplo: alertas = [] ; for v in [3, 15, 8]: if v < 10: alertas.append(v). ¿Qué contiene alertas?", ["Entran los valores menores que 10.", "Cumplen 3 y 8."], "[3, 8]"),
    ],
    mistakes=[("Marcar como no activos a los clavos porque tienen poco stock.", "La instrucción (2) solo mira stock = 0, no un stock bajo.", "Lee la condición exacta del WHERE y aplícala registro por registro."),
              ("Dar por bueno el resultado sin contar los registros afectados.", "Un cambio en más registros de los esperados pasa inadvertido.", "Cuenta cuántos registros cambian y compara con lo esperado.")],
    T=[
        ("abc", "En Programación: ¿qué hace alertas.append(x)?", "Agrega el valor x al final de la lista alertas", "Borra la lista alertas", "Cambia el stock de x", "append significa agregar al final de una lista."),
        ("abc", "{F} ¿Qué productos agrega la rutina de la ficha a la lista alertas?", "clavos y martillos", "tornillos y serruchos", "solo martillos", "Tienen stock menor que 10 los clavos (5) y los martillos (0)."),
        ("=", "{F} ¿Cuál es el stock de los clavos después de la instrucción (1)?", "5+20", "El UPDATE suma 20 al stock anterior de 5.", " unidades"),
        ("abc", "{F} ¿Qué registro marca como no activo la instrucción (2)?", "El de martillos, que tiene stock 0", "El de clavos", "Todos los productos", "Solo los martillos cumplen stock = 0."),
        ("=", "{F} Después de las dos instrucciones, ¿cuántos productos quedan con activo = «sí»?", "4-1", "De los cuatro productos, uno (martillos) pasa a no activo.", " productos"),
        ("abc", "{F} Después de la instrucción (1), si se vuelve a ejecutar la rutina, ¿qué productos entran a alertas?", "Solo martillos", "Clavos y martillos", "Ninguno", "Los clavos suben a 25 y ya no son menores que 10; los martillos tienen 0."),
        ("=", "{F} ¿Cuántas unidades en total tiene el inventario después de la instrucción (1)?", "40+25+0+12", "Los clavos subieron a 25 y los otros stocks no cambian.", " unidades"),
        ("abc", "{F} Una persona ejecuta la instrucción (1) sin el WHERE. ¿Cuál sería el error?", "Los cuatro productos subirían 20 unidades", "Solo los clavos subirían 20 unidades", "No subiría ninguno", "Sin WHERE el UPDATE afecta todos los registros."),
        ("abc", "Rutina de ejemplo: n = 0 ; for v in [1, 4, 6, 9]: if v > 5: n = n + 1. ¿Cuánto vale n?", "2", "1", "3", "Superan 5 el 6 y el 9."),
        ("abc", "{F} Un técnico asegura que el stock total después de (1) es 77. ¿Es correcto?", "Sí: 40 + 25 + 0 + 12 = 77", "No: el total es 82", "No: el total es 57", "Los clavos tienen 25 después de sumar 20 al stock de 5."),
        ("abc", "{F} El técnico quiere probar la instrucción (2) en la base real un viernes por la tarde para «ahorrar tiempo». ¿Qué corresponde?", "Probarla antes en una copia y respaldar la base real", "Probarla directamente porque es corta", "Pedir a un cliente que la pruebe", "Los cambios se ensayan en una copia y la base real se respalda antes."),
        ("=", "Rutina de ejemplo: s = 0 ; for v in [4, 0, 7, 0, 2]: if v == 0: s = s + 1. ¿Cuánto vale s?", "1+1", "Cuenta los valores iguales a 0, que son dos.", ""),
        ("abc", "{F} Tras el mantenimiento, el técnico anota en la bitácora: «ajustado stock de clavos a 25 y desactivado martillos por stock 0». ¿Qué falta para que el registro sea completo?", "La fecha, quién lo hizo y quién lo autorizó", "El nombre de todos los clientes", "La contraseña del administrador", "Una bitácora útil dice cuándo, quién y con qué autorización."),
    ],
    ctx=("abc", "Al aplicar un UPDATE en la copia de prueba, el técnico ve que cambiaron 4 registros cuando esperaba 1. ¿Qué hace?", "No lo aplica a la base real, corrige el WHERE y vuelve a probar", "Lo aplica a la base real de todos modos", "Borra la copia de prueba y no avisa", "Una diferencia con lo esperado se corrige antes de tocar la base real."),
    sc=[
        ("En Programación: ¿qué hace SET stock = stock + 20?", "Suma 20 al valor que ya tenía el campo", "El campo se calcula a partir de su valor anterior."),
        ("¿Dónde se prueba un cambio antes de aplicarlo?", "En una copia de la base de datos", "Se evita dañar los datos reales."),
        ("¿Qué se verifica al terminar?", "Que los registros afectados sean los esperados", "Se cuenta y se compara con lo previsto."),
    ],
    op=("Una papelería de ejemplo tiene la tabla «stock»: id 1, lápices, 30; id 2, cuadernos, 4; id 3, gomas, 0 (datos inventados). Instrucciones: (1) UPDATE stock SET cantidad = cantidad + 10 WHERE id = 2 ; (2) rutina que agrega a «alertas» los productos con cantidad menor que 5. Escribe la tabla después de (1), el contenido de alertas y el total de unidades.",
        "Tras (1): lápices 30, cuadernos 14, gomas 0. Alertas: solo gomas (0 es menor que 5; cuadernos ya tiene 14). Total de unidades: 30 + 14 + 0 = 44.",
        ["aplica bien el UPDATE al registro correcto", "obtiene el contenido de alertas", "calcula el total y lo verifica"],
        ["tabla antes y después, lista de alertas y total"],
        ["aplicar el UPDATE a todos los registros", "incluir cuadernos en alertas", "olvidar sumar las gomas con 0"],
        "Pregunta: «¿por qué cuadernos ya no está en alertas?». Si no responde, pídele que relea el stock después del UPDATE."),
    reinforce="Escribe una tabla de tres productos inventados, aplica un UPDATE con WHERE a uno y escribe la tabla final.",
    extend="Explica con un ejemplo inventado qué cambia en el resultado si dos instrucciones se aplican en distinto orden.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 12 (caso de ejemplo, inventado). Tabla «contactos» de la «Agrupación Vecinal Los Álamos» (nombre de ejemplo): id 1, Lía, correo lia@ejemplo.cl, permiso sí; id 2, Marcos, correo (vacío), permiso sí; "
     "id 3, Lía, correo lia@ejemplo.cl, permiso sí; id 4, Nora, correo nora@ejemplo.cl, permiso no; id 5, Omar, correo omar@ejemplo.cl, permiso sí (datos inventados). "
     "Plan de mantención de ejemplo: depurar duplicados y vacíos cada mes, respaldo completo cada 7 días y borrar datos de quienes retiran su permiso.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: depurar una base, decidir con el menor riesgo y respetar el permiso de las personas.",
    prior=["Sé qué es un duplicado, un respaldo y un UPDATE con WHERE.", "Sé qué es un dato personal.", "Sé contar registros."],
    explain=[
        "La depuración es limpiar la base de datos: se buscan duplicados (registros repetidos), campos vacíos que deberían tener valor, datos en formatos distintos y registros que ya no se necesitan. Se detecta con consultas, por ejemplo SELECT con WHERE, y se corrige con UPDATE o DELETE filtrados, siempre sobre una copia y con respaldo previo.",
        "El orden seguro de una modificación es: pedir autorización, respaldar, probar en una copia, aplicar con WHERE, verificar el resultado y anotar en la bitácora. Si el resultado no es el esperado, se restaura el respaldo. Un cambio masivo hecho sin estos pasos es una causa frecuente de pérdida de datos.",
        "La privacidad también guía la decisión. Una persona puede retirar su permiso, y entonces sus datos personales se eliminan o se dejan de usar según la norma vigente. Se conservan solo los datos necesarios para el fin informado, y los avisos se mandan solo a quienes dieron permiso. Las contraseñas no se guardan escritas y nunca se piden ni se escriben reales en un ejercicio.",
    ],
    vocab=[("depuración", "limpieza de duplicados, vacíos y errores de una base"), ("campo vacío", "campo sin valor que debería tenerlo"), ("retirar el permiso", "la persona deja de autorizar el uso de sus datos"), ("cambio masivo", "modificación que afecta muchos registros a la vez"), ("conservar solo lo necesario", "guardar únicamente los datos que hacen falta para el fin informado")],
    worked=[
        ("Detectar un duplicado", "Tabla de ejemplo: id 1, Raúl, raul@ejemplo.cl; id 2, Sara, sara@ejemplo.cl; id 3, Raúl, raul@ejemplo.cl. ¿Cuál registro es un duplicado y cuál se conserva?", ["Los registros 1 y 3 tienen los mismos datos.", "Se conserva el primero (id 1) y se elimina el id 3 con DELETE ... WHERE id = 3."], "Duplicado: id 3; se conserva el id 1"),
        ("Respetar el permiso", "Una persona de ejemplo con id 7 retira su permiso. ¿Cómo debe tratarse su dato de contacto?", ["Ya no se le pueden mandar avisos.", "Se elimina o se deja de usar el dato según la norma vigente."], "Se deja de usar y se elimina según la norma"),
    ],
    mistakes=[("Eliminar los duplicados ejecutando un DELETE sin revisar cuál registro se conserva.", "Se puede borrar el registro más completo o el que otras tablas usan.", "Decide cuál se conserva, elimina con WHERE y comprueba las relaciones."),
              ("Seguir mandando avisos a una persona que retiró su permiso porque «ya estaba en la lista».", "Se incumple su decisión y la norma de protección de datos.", "Marca el retiro del permiso y no la incluyas en ningún aviso.")],
    T=[
        ("abc", "En Programación: ¿qué es depurar una base de datos?", "Limpiar duplicados, vacíos y errores de los datos", "Aumentar el número de tablas", "Cambiar la contraseña del administrador", "La depuración mejora la calidad de los datos."),
        ("abc", "{F} ¿Qué registros de la ficha son duplicados entre sí?", "id 1 y id 3, ambos de Lía con el mismo correo", "id 2 y id 4", "id 4 y id 5", "Los registros 1 y 3 tienen el mismo nombre y correo."),
        ("abc", "{F} ¿Qué registro tiene un campo vacío que debería tener valor?", "id 2, Marcos, sin correo", "id 4, Nora", "id 5, Omar", "Solo Marcos tiene el correo vacío."),
        ("=", "{F} ¿Cuántos registros quedan en la tabla después de eliminar el duplicado?", "5-1", "Se elimina uno de los dos registros repetidos.", " registros"),
        ("abc", "{F} ¿A quiénes puede enviarse un aviso por correo si se conservan solo registros con correo y permiso sí?", "Lía y Omar", "Lía, Marcos y Omar", "Lía, Nora y Omar", "Marcos no tiene correo y Nora no dio permiso."),
        ("abc", "{F} Nora retira su permiso. ¿Qué corresponde con su registro?", "Dejar de usar su dato y eliminarlo según la norma vigente", "Seguir enviándole avisos", "Cambiar su nombre por otro", "El retiro del permiso obliga a dejar de usar sus datos."),
        ("=", "{F} Con el plan de mantención, ¿cuántos respaldos completos se hacen en 21 días?", "21//7", "Se divide el período por los días entre respaldos.", " respaldos"),
        ("abc", "{F} ¿Cuál es el orden seguro para eliminar el duplicado de Lía?", "Autorización, respaldo, prueba en copia, DELETE con WHERE, verificación y bitácora", "DELETE, respaldo, autorización y verificación", "Verificación, DELETE y respaldo", "Primero se protege y se prueba; recién después se aplica y se anota."),
        ("abc", "{F} Para eliminar el registro duplicado id 3, ¿qué instrucción es correcta?", "DELETE FROM contactos WHERE id = 3", "DELETE FROM contactos", "UPDATE contactos SET id = 3", "Con WHERE id = 3 se elimina solo el duplicado."),
        ("abc", "El técnico, para ahorrar espacio, guarda también la fecha de nacimiento y la dirección de cada vecino, aunque el aviso solo necesita el correo. ¿Qué principio se rompe?", "Conservar solo los datos necesarios para el fin informado", "El menor privilegio", "La clave primaria única", "Se recogen datos personales que el fin del aviso no necesita."),
        ("abc", "{F} Tras la depuración quedan los registros 1, 2, 4 y 5. El técnico anota «5 registros» en la bitácora. ¿Qué error cometió?", "Anotó una cifra que no coincide con el resultado verificado de 4 registros", "No incluyó la fecha de nacimiento", "Contó dos veces a Omar", "La bitácora debe reflejar lo verificado: 4 registros."),
        ("=", "{F} Una tabla de ejemplo tiene 200 registros, 14 duplicados y 6 vacíos que se eliminan. ¿Cuántos quedan?", "200-14-6", "Se restan los duplicados y los vacíos eliminados.", " registros"),
        ("ab", "{F} Un vecino pide ver qué datos suyos guarda la agrupación. ¿Qué corresponde?", "Atender la solicitud por el canal que la jefatura indique", "Ignorar el pedido porque la tabla es interna", "Según la norma vigente las personas pueden consultar sus datos, y la respuesta pasa por quien corresponde."),
    ],
    ctx=("abc", "La presidenta pide eliminar a todos los contactos de la tabla «para empezar de cero», sin respaldo. ¿Qué responde el técnico?", "Propone respaldar primero, aclarar qué contactos se eliminan y dejar autorización escrita", "Ejecuta DELETE sin WHERE de inmediato", "Se niega sin explicar", "Los borrados masivos exigen respaldo, alcance claro y autorización."),
    sc=[
        ("En Programación: ¿qué se hace con los datos de quien retira su permiso?", "Se deja de usar y se elimina según la norma vigente", "La persona decide sobre sus datos personales."),
        ("¿Cuál es el primer paso de un cambio masivo?", "Pedir autorización y respaldar", "Protege los datos antes de modificar."),
        ("¿Qué se hace con un registro duplicado?", "Se decide cuál se conserva y se elimina el otro con WHERE", "No se borra ningún registro sin revisar antes cuál conservar."),
    ],
    op=("Una escuela de ejemplo tiene la tabla «apoderados»: id 1, Pía, pia@ejemplo.cl, permiso sí; id 2, Raúl, (vacío), permiso sí; id 3, Pía, pia@ejemplo.cl, permiso sí; id 4, Sol, sol@ejemplo.cl, permiso no. Indica el duplicado, el campo vacío, los apoderados a quienes se puede mandar un aviso por correo y escribe el orden de seis pasos seguros para eliminar el duplicado.",
        "Duplicado: id 3 (igual al id 1). Campo vacío: el correo de Raúl. Se puede avisar solo a Pía (tiene correo y permiso). Pasos: 1) autorización; 2) respaldo; 3) prueba en copia; 4) DELETE FROM apoderados WHERE id = 3; 5) verificar que quedan 3 registros; 6) anotar en la bitácora.",
        ["identifica duplicado y campo vacío", "selecciona correctamente a quién avisar", "escribe el orden seguro de seis pasos"],
        ["hoja con las respuestas y los seis pasos"],
        ["avisar a Sol", "eliminar sin respaldo", "borrar el registro equivocado"],
        "Pregunta: «¿por qué Raúl no recibe el aviso por correo aunque dio permiso?». Si no responde, pídele que revise el campo del correo."),
    reinforce="Inventa una tabla de cinco contactos con un duplicado y un campo vacío, y señálalos.",
    extend="Explica con un ejemplo inventado por qué conservar solo los datos necesarios reduce riesgos para la organización y para las personas.",
)
