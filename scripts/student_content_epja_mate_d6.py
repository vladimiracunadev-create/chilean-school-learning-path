"""Matemática EPJA Nivel 1 básico, módulo 4: OAD-16 (explicar el razonamiento para elaborar gráficos de barras y de línea y compartir la información). Datos de ejemplo, inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Hoja, lápiz de mina y regla. Todo se hace en papel; las tablas y los datos vienen escritos en cada ficha y los gráficos se dibujan a mano. Todos los datos son de ejemplo, inventados."
build = make_build(MATERIALS)

O16 = "EPJA-MATE-NB1-OAD-16"

# ===================================================== OAD-16 clase 1
F = ("Datos de ejemplo. Tabla de consultas recibidas en un punto de atención durante una semana: "
     "Trámite 32, Reclamo 12, Información 24, Pago 20. Para el gráfico de barras se usará una escala de 4 en 4, del 0 al 36.")
build(
    O16, 1, F,
    use="Voy a explicar los pasos para elaborar un gráfico de barras desde una tabla, y por qué se hace cada uno.",
    prior=["Sé leer tablas de frecuencia.", "Sé las partes de un gráfico de barras.", "Sé contar de 4 en 4."],
    explain=[
        "Elaborar un gráfico de barras tiene cuatro pasos. Uno: ordenar los datos en una tabla con categorías y números. Dos: decidir la escala, que parte en cero y llega al menos al dato mayor. Tres: dibujar una barra por categoría con su altura. Cuatro: escribir título y rótulos de los ejes.",
        "Cada paso tiene una razón. La tabla evita olvidar datos. La escala pareja permite comparar. Las barras del mismo ancho evitan engañar al ojo. El título y los rótulos permiten que otra persona entienda sin que tú estés. Si puedes explicar la razón de cada paso, ya lo entiendes de verdad.",
        "En la ficha la escala sube de 4 en 4 porque todos los datos son múltiplos de 4. Así cada barra llega justo a una marca. Cuando explicas a otra persona, usa tus palabras y los números de la tabla: «Trámite llega a la marca 32 porque tuvo 32 consultas».",
    ],
    vocab=[("elaborar", "construir paso a paso"), ("escala", "números parejos que sirven para leer"), ("múltiplo de 4", "número que aparece al contar de 4 en 4"), ("rótulo", "palabra que explica qué mide un eje"), ("consulta", "pregunta que una persona hace en un punto de atención"), ("razón", "motivo de un paso")],
    worked=[
        ("Elegir hasta dónde llega la escala", "En la ficha, ¿hasta qué número debe llegar la escala?", ["El dato mayor es 32.", "Con saltos de 4 se llega a 36, que es el siguiente a 32."], "Hasta 36, o al menos hasta 32"),
        ("Dibujar una barra", "¿Cuántas marcas sube la barra de Reclamo?", ["Reclamo tiene 12 consultas.", "12 ÷ 4 = 3, así que sube hasta la tercera marca."], "3 marcas")
    ],
    mistakes=[("Dibujar las barras antes de decidir la escala.", "Se empieza por lo que se ve más rápido.", "Primero ordena la tabla y decide la escala; después dibuja."),
              ("Olvidar el título y los rótulos al terminar.", "Se cree que el dibujo se explica solo.", "Escríbelos antes de entregar y revisa que digan qué mide cada eje.")],
    T=[
        ("abc", "{F} ¿Cuál es el primer paso para elaborar el gráfico?", "Ordenar los datos en una tabla", "Pintar las barras", "Escribir las conclusiones", "Con los datos ordenados se decide la escala y se dibuja."),
        ("=", "{F} ¿Cuántas consultas hubo en total en la semana?", "32+12+24+20", "Se suman los cuatro datos de la tabla.", " consultas"),
        ("{F} ¿Hasta qué número sube la barra de Reclamo?", "12", "El dato de Reclamo en la tabla es doce consultas."),
        ("=", "{F} ¿Cuántas marcas sube la barra de Trámite si cada marca vale 4?", "32//4", "Se divide el dato por el valor de cada marca.", " marcas"),
        ("abc", "{F} ¿Hasta dónde debe llegar la escala como mínimo?", "32", "12", "20", "La escala debe cubrir el dato mayor, treinta y dos."),
        ("ab", "{F} ¿Por qué conviene la escala de 4 en 4 para estos datos?", "Porque todos los datos son múltiplos de 4 y las barras llegan justo a una marca", "Porque 4 es el número más grande", "Los datos 32, 12, 24 y 20 se alcanzan contando de cuatro en cuatro."),
        ("=", "{F} ¿Cuántas consultas más hubo de Trámite que de Reclamo?", "32-12", "Se resta el dato menor del mayor.", " consultas"),
        ("=", "{F} ¿Cuántas marcas sube la barra de Información?", "24//4", "Se divide el dato por el valor de cada marca.", " marcas"),
        ("=", "{F} ¿Cuántas consultas hubo de Reclamo y Pago juntas?", "12+20", "Se suman los dos datos pedidos.", " consultas"),
        ("abc", "Alguien dibujó una barra de Pago más angosta que las demás. ¿Cuál es el problema?", "Las barras deben tener el mismo ancho para no engañar", "Ninguno, el ancho no importa", "Cambia el dato de Pago", "Con anchos distintos la vista compara áreas y no alturas."),
        ("=", "{F} Si Reclamo subiera 8 consultas, ¿cuántas tendría?", "12+8", "Se suman las nuevas consultas al dato.", " consultas"),
        ("ab", "{F} La barra de Pago (20) llega a la marca número", "5", "20", "Con saltos de cuatro, veinte es la quinta marca."),
        ("abc", "¿Qué orden de pasos es correcto?", "Tabla, escala, barras, título y rótulos", "Barras, título, tabla, escala", "Título, barras, escala, tabla", "Los datos y la escala se deciden antes de dibujar."),
    ],
    ctx=("=", "Una funcionaria de un punto de atención de ejemplo debe explicar a su jefa cuántas consultas de Trámite y de Pago hubo en total para organizar a los turnos. ¿Cuántas fueron?", "32+20", "Se suman las consultas de las dos categorías.", " consultas"),
    sc=[("¿Cuáles son los cuatro pasos para elaborar un gráfico de barras?", "Tabla, escala, barras, título y rótulos", "Ese orden evita errores y deja el gráfico claro."),
        ("¿Por qué las barras tienen el mismo ancho?", "Para que solo cuente la altura al comparar", "Con el mismo ancho la altura muestra la diferencia real."),
        ("¿Qué explicas de cada paso al compartir tu gráfico?", "La razón de por qué lo hiciste así", "Explicar el motivo muestra que comprendiste el procedimiento.")],
    op=("Elabora el gráfico de barras de esta tabla de ejemplo: Llamadas recibidas en un call center vecinal: Lunes 8, Martes 16, Miércoles 12, Jueves 20. Usa escala de 4 en 4 y explica en cuatro frases los pasos que seguiste.",
        "Tabla ordenada; escala 0, 4, 8, 12, 16, 20; barras de alturas 8, 16, 12 y 20; título «Llamadas por día»; rótulos «Día» y «Llamadas». Explicación: «Primero ordené, después elegí la escala, dibujé las barras y escribí título y rótulos».",
        ["barras con alturas correctas", "escala de 4 en 4 bien escrita", "explica los pasos con razones"],
        ["hoja con el gráfico y las cuatro frases"],
        ["dibujar sin elegir la escala", "no escribir rótulos"],
        "Pregunta: «¿por qué elegiste esa escala?». Debe explicar que los datos son múltiplos de cuatro."),
    reinforce="Elabora un gráfico de barras con una tabla de tres datos tuyos y escribe sus pasos.",
    extend="Explica cómo cambiarías la escala si los datos fueran 60, 40 y 100.",
)

# ===================================================== OAD-16 clase 2
F = ("Datos de ejemplo. Kilos de papas vendidos por cuatro locales de una feria: Local A 120, Local B 180, Local C 90, Local D 150. "
     "Se comparan tres escalas posibles: de 1 en 1, de 10 en 10 y de 30 en 30, todas hasta 180.")
build(
    O16, 2, F,
    use="Voy a elegir una escala adecuada para un gráfico de barras y a explicar por qué la elegí.",
    prior=["Sé contar de 10 en 10 y de 30 en 30.", "Sé dividir por 10 y por 30.", "Sé qué es una escala."],
    explain=[
        "La escala es la parte del gráfico que decide cuántas marcas tendrá y cuánto vale cada una. Una buena escala parte en cero, sube de manera pareja y llega al menos al dato mayor. Además debe ser cómoda: ni demasiadas marcas, ni tan pocas que no se pueda leer.",
        "Con datos grandes, como 120, 180 o 90, una escala de uno en uno tendría 180 marcas: imposible de dibujar. Una de 10 en 10 tiene 18 marcas, que es largo. Una de 30 en 30 tiene solo 6 marcas y todos los datos caen justo en una marca. Esa es la mejor elección aquí.",
        "Elegir la escala es una decisión que puedes explicar: «usé 30 en 30 porque todos los datos son múltiplos de 30 y así el gráfico cabe en la hoja». Si los datos fueran pequeños, como 8 y 12, serviría una escala de uno en uno o de dos en dos.",
    ],
    vocab=[("escala", "números parejos con los que se lee el gráfico"), ("marca", "rayita de la escala con su número"), ("salto", "lo que sube la escala entre una marca y la siguiente"), ("cómoda", "fácil de dibujar y de leer"), ("múltiplo de 30", "número que sale al contar de 30 en 30"), ("justificar", "explicar por qué elegiste algo")],
    worked=[
        ("Contar marcas", "En la ficha, ¿cuántas marcas tiene una escala de 30 en 30 hasta 180?", ["Divide 180 por 30.", "180 ÷ 30 = 6."], "6 marcas"),
        ("Ubicar una barra", "¿En qué marca termina la barra del Local C (90) con escala de 30 en 30?", ["Divide 90 por 30.", "90 ÷ 30 = 3, la tercera marca."], "En la tercera marca")
    ],
    mistakes=[("Elegir la escala de uno en uno porque «es la más exacta».", "Se piensa que más marcas es mejor.", "Elige una escala que quepa en la hoja y que haga caer los datos en una marca."),
              ("Dejar la escala sin llegar al dato mayor.", "No se revisa la tabla antes de dibujar.", "Comprueba que la última marca sea mayor o igual al dato mayor.")],
    T=[
        ("abc", "{F} ¿Qué escala conviene a estos datos?", "De 30 en 30", "De 1 en 1", "De 7 en 7", "Treinta divide a todos los datos y deja pocas marcas."),
        ("=", "{F} ¿Cuántas marcas tendría una escala de 10 en 10 hasta 180?", "180//10", "Se divide el máximo de la escala por el salto.", " marcas"),
        ("=", "{F} ¿Cuántas marcas tendría una escala de 30 en 30 hasta 180?", "180//30", "Se divide el máximo de la escala por el salto.", " marcas"),
        ("abc", "{F} ¿Hasta qué número debe llegar la escala como mínimo?", "180", "90", "120", "La escala debe cubrir el dato mayor, que es ciento ochenta."),
        ("=", "{F} ¿Cuántos kilos se vendieron en total en los cuatro locales?", "120+180+90+150", "Se suman los cuatro datos.", " kilos"),
        ("=", "{F} ¿En qué marca termina la barra del Local C con escala de 30 en 30?", "90//30", "Se divide el dato por el valor de cada marca.", ""),
        ("ab", "{F} Con escala de 30 en 30, la marca que sigue a 120 es", "150", "121", "Se suma treinta a ciento veinte."),
        ("=", "{F} ¿Cuántos kilos más vendió el Local B que el Local C?", "180-90", "Se resta el dato menor del mayor.", " kilos"),
        ("abc", "¿Por qué no sirve una escala de 1 en 1 hasta 180?", "Tendría 180 marcas y no cabría en la hoja", "Porque el uno no es un número válido", "Porque cambia los datos", "Una escala demasiado larga es impráctica de dibujar y de leer."),
        ("=", "{F} ¿Cuántos kilos vendieron los locales A y D juntos?", "120+150", "Se suman los dos datos pedidos.", " kilos"),
        ("ab", "{F} La barra del Local D llega a la marca número", "5", "150", "Ciento cincuenta dividido en treinta da cinco."),
        ("=", "{F} ¿Cuántas marcas separan la barra del Local B y la del Local C?", "(180-90)//30", "Se resta la diferencia y se divide por el salto.", " marcas"),
        ("abc", "Para los datos 8, 12, 5 y 10 kilos, ¿qué escala conviene?", "De 1 en 1 o de 2 en 2", "De 100 en 100", "De 50 en 50", "Con datos pequeños, una escala de saltos pequeños los muestra bien."),
    ],
    ctx=("=", "Una feriante de ejemplo prepara un cartel con los kilos de papas de dos locales: A 120 y D 150. Quiere indicar cuántos kilos vendieron juntos. ¿Cuántos kilos son?", "120+150", "Se suman los datos de los dos locales.", " kilos"),
    sc=[("¿Cómo debe partir una escala?", "En cero", "Las barras parten en cero para mostrar la cantidad completa."),
        ("¿Qué revisas para elegir el salto de la escala?", "Que los datos caigan en una marca y que no haya demasiadas marcas", "Así el gráfico es claro y cabe en la hoja."),
        ("¿Qué escala usarías para datos 20, 40 y 60?", "De 20 en 20 o de 10 en 10", "Los tres datos son múltiplos de veinte.")],
    op=("Para estos datos de ejemplo de una panadería (kilos de harina usados por semana: S1 50, S2 100, S3 75, S4 150), elige una escala, escribe cuántas marcas tendrá y explica en dos frases por qué la elegiste. Dibuja las barras.",
        "Escala de 25 en 25 hasta 150: 6 marcas. Explicación: «Elegí 25 en 25 porque todos los datos son múltiplos de 25 y así hay pocas marcas». Barras de 50, 100, 75 y 150.",
        ["la escala parte en cero y cubre el dato mayor", "las barras coinciden con los datos", "la explicación da una razón"],
        ["hoja con el gráfico y las dos frases"],
        ["escala que no llega al dato mayor", "no justificar la elección"],
        "Pregunta: «¿qué otra escala podrías usar y qué cambiaría?». Debe comparar el número de marcas."),
    reinforce="Elige una escala para los datos 6, 9, 3 y 12 y explica tu elección.",
    extend="Explica por qué una escala de 50 en 50 no sirve para los datos 120 y 130 del mismo gráfico.",
)

# ===================================================== OAD-16 clase 3
F = ("Datos de ejemplo. Un local registra los pedidos de dos sucursales: Norte 60 y Sur 64. "
     "Gráfico 1: la escala parte en 0 y sube de 10 en 10. Gráfico 2: la escala parte en 56 y sube de 2 en 2, con la barra Norte hasta 60 y la barra Sur hasta 64. "
     "Gráfico 3: tiene las barras, pero no tiene título ni rótulos.")
build(
    O16, 3, F,
    use="Voy a revisar si un gráfico está completo y si su escala es honesta, y a escribir conclusiones que se puedan comprobar.",
    prior=["Sé las partes de un gráfico de barras.", "Sé qué es una escala.", "Sé calcular una diferencia."],
    explain=[
        "Un gráfico bien hecho tiene título, ejes con rótulos y una escala que parte en cero. Si falta el título o los rótulos, quien lo lee no sabe de qué trata. Si la escala no parte en cero, las barras pueden mostrar diferencias que parecen enormes aunque sean pequeñas.",
        "En la ficha, 60 y 64 se diferencian en solo 4. En el gráfico 1, con escala desde cero, las barras casi no se distinguen. En el gráfico 2, con escala desde 56, la barra Sur parece el doble de alta que la Norte. Es un engaño del dibujo: el dato no cambió.",
        "Una conclusión honesta dice lo que los números muestran: «Sur tuvo 4 pedidos más que Norte». No dice «Sur vende mucho más», si no es cierto. Antes de compartir un gráfico, revisa que sea claro y que no exagere las diferencias.",
    ],
    vocab=[("honesto", "que no engaña con lo que muestra"), ("conclusión", "idea que se saca de comparar los datos"), ("rótulo", "palabra que dice qué mide un eje"), ("escala que parte en cero", "escala que empieza en 0"), ("engañar", "hacer creer algo que no es"), ("sucursal", "local de una misma empresa en otro lugar")],
    worked=[
        ("Diferencia real", "En la ficha, ¿cuál es la diferencia real entre Sur y Norte?", ["Los datos son 64 y 60.", "Resta: 64 − 60 = 4."], "4 pedidos"),
        ("Barras con escala desde 56", "En el gráfico 2, ¿cuánto sobresale la barra Norte de la base de 56?", ["Norte es 60 y la escala parte en 56.", "60 − 56 = 4; mientras que Sur sobresale 64 − 56 = 8."], "Norte sobresale 4 y Sur 8")
    ],
    mistakes=[("Concluir que Sur vende el doble que Norte porque su barra se ve más alta en el gráfico 2.", "Se mira el dibujo y no los números.", "Compara siempre los datos: 64 no es el doble de 60."),
              ("Entregar un gráfico sin título ni rótulos.", "Se supone que quien lo mira sabrá de qué trata.", "Agrega título y rótulos antes de compartirlo.")],
    T=[
        ("abc", "{F} ¿Cuál gráfico muestra con más honestidad la diferencia entre las sucursales?", "El gráfico 1, porque su escala parte en cero", "El gráfico 2, porque se ve más grande la diferencia", "El gráfico 3, porque tiene más barras", "Con escala desde cero las alturas son proporcionales a los datos."),
        ("=", "{F} ¿Cuál es la diferencia real de pedidos entre Sur y Norte?", "64-60", "Se resta el dato menor del mayor.", " pedidos"),
        ("ab", "{F} En el gráfico 2, la barra Sur parece mucho más alta porque", "la escala no parte en cero", "Sur vendió el doble", "Parte en 56, así que se exagera una diferencia pequeña."),
        ("=", "{F} ¿Cuánto sobresale la barra Norte de la base 56 en el gráfico 2?", "60-56", "Se resta la base de la escala al dato.", " pedidos"),
        ("=", "{F} ¿Cuánto sobresale la barra Sur de la base 56 en el gráfico 2?", "64-56", "Se resta la base de la escala al dato.", " pedidos"),
        ("abc", "{F} Un titular dice: «Sur vende el doble que Norte». ¿Es honesto?", "No: 64 no es el doble de 60", "Sí: su barra se ve el doble", "Sí: Sur vende más", "El doble de sesenta sería ciento veinte."),
        ("=", "{F} ¿Cuánto sería el doble de los pedidos de Norte?", "60*2", "El doble se calcula multiplicando por dos.", " pedidos"),
        ("abc", "{F} ¿Qué le falta al gráfico 3?", "Título y rótulos de los ejes", "Más barras", "Otro color", "Sin título ni rótulos no se sabe de qué trata ni qué mide."),
        ("=", "{F} ¿Cuántos pedidos tuvieron las dos sucursales juntas?", "60+64", "Se suman los dos datos.", " pedidos"),
        ("abc", "{F} ¿Qué conclusión es honesta?", "Sur tuvo 4 pedidos más que Norte", "Sur es mucho mejor que Norte", "Norte casi no vende", "La conclusión honesta usa los números exactos de la tabla."),
        ("ab", "{F} ¿Qué corriges en el gráfico 2 para que sea honesto?", "Hacer que la escala parta en 0", "Pintar más oscura la barra Sur", "Una escala desde cero muestra la diferencia con su tamaño real."),
        ("=", "{F} Si Norte subiera 10 pedidos, ¿cuántos tendría?", "60+10", "Se suma el aumento al dato.", " pedidos"),
        ("abc", "Alguien dice: «da lo mismo que la escala parta en cero o en 56». ¿Qué respondes?", "Sí da diferencia: puede exagerar las diferencias", "Tiene razón, es igual", "Solo importa el color", "Al cambiar el punto de partida cambia lo que se ve del dibujo."),
    ],
    ctx=("=", "Una jefa de zona de ejemplo va a mostrar a su equipo el gráfico de las sucursales. Quiere decir cuántos pedidos tuvo Sur más que Norte, sin exagerar. ¿Cuántos pedidos más tuvo Sur?", "64-60", "Se resta el dato de Norte al de Sur.", " pedidos"),
    sc=[("¿Qué partes debe tener un gráfico completo?", "Título, rótulos, escala y barras", "Con ellas otra persona puede entenderlo sola."),
        ("¿Por qué conviene que la escala parta en cero?", "Para que la altura de las barras muestre las diferencias reales", "La altura proporcional evita exagerar o esconder diferencias."),
        ("¿Cómo escribes una conclusión honesta?", "Con los números exactos que muestra la tabla", "Los datos exactos dicen solo lo que de verdad ocurrió.")],
    op=("Revisa estos tres gráficos de ejemplo del mismo dato (Taller A 40 personas y Taller B 42): uno parte en 0, otro parte en 38 y otro no tiene título. Escribe qué problema tiene cada uno y una conclusión honesta de una frase.",
        "El primero es honesto; el segundo exagera la diferencia porque parte en 38; el tercero no dice de qué trata. Conclusión: «El taller B tuvo 2 personas más que el taller A».",
        ["identifica el problema de cada gráfico", "calcula la diferencia 2", "escribe una conclusión honesta"],
        ["hoja con tres observaciones y una frase"],
        ["no ver que la escala no parte en cero", "exagerar la diferencia en la frase"],
        "Pregunta: «¿cuál gráfico elegirías para compartir y por qué?». Debe justificar con la escala."),
    reinforce="Revisa un gráfico de un diario o de internet y anota si tiene título, rótulos y escala desde cero.",
    extend="Explica por qué a veces se exagera una diferencia sin querer.",
)

# ===================================================== OAD-16 clase 4
F = ("Datos de ejemplo. Temperatura en grados de una bodega, medida cada dos horas: 8:00 → 12. 10:00 → 15. 12:00 → 19. 14:00 → 21. 16:00 → 18. "
     "Gráfico de línea: en el eje horizontal van las horas y en el vertical los grados, con escala de 3 en 3.")
build(
    O16, 4, F,
    use="Voy a elaborar un gráfico de línea para mostrar cómo cambia una cosa a lo largo del tiempo.",
    prior=["Sé leer tablas de datos.", "Sé las partes de un gráfico de barras.", "Sé contar de 3 en 3."],
    explain=[
        "Un gráfico de línea muestra cómo cambia algo a lo largo del tiempo: la temperatura durante un día, las ventas semana a semana. En el eje de abajo van los momentos, en orden. En el eje del lado va la medida, con una escala que parte en cero.",
        "Para elaborarlo: primero ubica en la tabla cada momento y su dato. Después marca un punto donde se cruzan el momento y el dato. Por último une los puntos con una línea, de izquierda a derecha, en orden. Escribe título y rótulos como en las barras.",
        "Elige barras cuando comparas categorías distintas, como tipos de transporte. Elige línea cuando los datos van en orden de tiempo y quieres ver si suben, bajan o se mantienen. La línea ayuda a ver una tendencia, es decir, hacia dónde van los datos.",
    ],
    vocab=[("gráfico de línea", "gráfico con puntos unidos para mostrar cambios en el tiempo"), ("punto", "marca donde se cruzan el momento y el dato"), ("tendencia", "hacia dónde van los datos: suben, bajan o se mantienen"), ("bodega", "lugar donde se guardan productos"), ("grado", "unidad con que se mide la temperatura"), ("tiempo", "horas, días o meses en orden")],
    worked=[
        ("Ubicar un punto", "En la ficha, ¿dónde va el punto de las 12:00?", ["Busca la hora 12:00 en el eje de abajo.", "Sube hasta la altura 19 de la escala y marca el punto."], "En el cruce de 12:00 con 19 grados"),
        ("Leer una subida", "¿Cuántos grados subió la temperatura entre las 8:00 y las 14:00?", ["A las 8:00 había 12 y a las 14:00 había 21.", "Resta: 21 − 12 = 9."], "9 grados")
    ],
    mistakes=[("Unir los puntos en cualquier orden.", "Se ven los puntos como si fueran independientes.", "Une de izquierda a derecha, siguiendo el orden del tiempo."),
              ("Usar barras para mostrar la temperatura a lo largo del día.", "Se aplica un gráfico que no muestra bien el cambio.", "Con datos en el tiempo, usa una línea para ver cómo cambian.")],
    T=[
        ("abc", "{F} ¿Qué va en el eje horizontal del gráfico de línea?", "Las horas, en orden", "Los grados", "El título", "El eje de abajo muestra el tiempo, en este caso las horas."),
        ("{F} ¿Qué temperatura hubo a las 12:00?", "19 grados", "Según la tabla, el dato de las doce es diecinueve grados."),
        ("=", "{F} ¿Cuántos grados subió la temperatura entre las 8:00 y las 14:00?", "21-12", "Se resta el dato inicial al dato final.", " grados"),
        ("abc", "{F} ¿A qué hora hubo la temperatura más alta?", "14:00", "8:00", "16:00", "Veintiún grados es el dato mayor, medido a las catorce horas."),
        ("=", "{F} ¿Cuántos grados bajó la temperatura entre las 14:00 y las 16:00?", "21-18", "Se resta el dato final al dato inicial.", " grados"),
        ("ab", "{F} Entre las 8:00 y las 10:00, la línea", "sube", "baja", "Pasa de doce a quince grados, por eso la línea sube."),
        ("=", "{F} ¿Cuál es la diferencia entre la temperatura mayor y la menor?", "21-12", "Se resta el dato menor al mayor.", " grados"),
        ("abc", "¿Cuándo conviene un gráfico de línea?", "Cuando los datos cambian en el tiempo", "Cuando se comparan tipos de transporte", "Cuando hay una sola categoría", "La línea muestra cómo cambia algo a lo largo del tiempo."),
        ("=", "{F} ¿Cuántos grados subió entre las 10:00 y las 12:00?", "19-15", "Se resta el dato inicial al dato final.", " grados"),
        ("abc", "{F} ¿Cuántos puntos tiene el gráfico de línea?", "5", "4", "21", "Hay un punto por cada hora anotada en la tabla."),
        ("=", "{F} Si a las 18:00 la temperatura bajara 4 grados desde las 16:00, ¿cuántos grados habría?", "18-4", "Se resta la baja a la temperatura anterior.", " grados"),
        ("ab", "{F} ¿Cómo se unen los puntos del gráfico de línea?", "De izquierda a derecha, en el orden de las horas", "En cualquier orden", "El tiempo avanza hacia la derecha, por eso se unen en ese orden."),
        ("abc", "Alguien dibujó los datos del día como barras separadas. ¿Qué podría mejorar?", "Usar una línea para ver el cambio", "Quitar los números", "Cambiar las horas", "La línea muestra la subida y la bajada con claridad."),
    ],
    ctx=("=", "Un bodeguero de ejemplo revisa su registro: a las 12:00 la bodega estaba a 19 grados y a las 14:00 a 21. ¿Cuántos grados subió en esas dos horas?", "21-19", "Se resta el dato inicial al final.", " grados"),
    sc=[("En Matemática, ¿qué muestra un gráfico de línea de datos en el tiempo?", "Cómo cambia algo a lo largo del tiempo", "Une los datos medidos en distintos momentos."),
        ("¿Qué pasos sigues para elaborarlo?", "Ubicar puntos, unirlos en orden y escribir título y rótulos", "Esos pasos lo dejan correcto y claro."),
        ("¿En qué eje van los momentos del tiempo?", "En el horizontal", "El tiempo se escribe abajo, de izquierda a derecha.")],
    op=("Elabora el gráfico de línea de estos datos de ejemplo del número de personas que llegan a una oficina: 9:00 → 6, 10:00 → 12, 11:00 → 18, 12:00 → 9, 13:00 → 3. Usa escala de 3 en 3. Escribe título, rótulos y dos frases sobre cómo cambia.",
        "Puntos en (9:00, 6), (10:00, 12), (11:00, 18), (12:00, 9) y (13:00, 3), unidos en orden. Frases: «Llegó más gente a las 11:00, 18 personas. Después bajó hasta 3 a las 13:00».",
        ["ubica bien los cinco puntos", "los une en orden", "escribe título, rótulos y frases correctas"],
        ["hoja con el gráfico y dos frases"],
        ["unir en desorden", "no escribir rótulos"],
        "Pregunta: «¿entre qué horas subió la cantidad de personas?». Debe responder entre 9:00 y 11:00."),
    reinforce="Anota durante tres días, a la misma hora, un dato tuyo (por ejemplo, los minutos que demoras en una fila o un trámite) y haz un gráfico de línea.",
    extend="Explica por qué unir puntos con una línea no significa que sepamos qué pasó entre dos mediciones.",
)

# ===================================================== OAD-16 clase 5
F = ("Datos de ejemplo. Gráfico de línea de las ventas semanales de un puesto, en unidades: Semana 1 → 40. Semana 2 → 55. Semana 3 → 55. Semana 4 → 75. Semana 5 → 60. "
     "Escala de 5 en 5.")
build(
    O16, 5, F,
    use="Voy a leer un gráfico de línea y a describir si sube, baja o se mantiene, con números.",
    prior=["Sé elaborar un gráfico de línea.", "Sé restar números de dos cifras.", "Sé leer una escala de 5 en 5."],
    explain=[
        "Para leer un gráfico de línea, mira los tramos, que son las partes de la línea entre dos puntos. Si el segundo punto está más alto, la línea sube. Si está más bajo, baja. Si están a la misma altura, la línea se mantiene.",
        "Con los números puedes decir cuánto cambió: resta el dato del primer punto al dato del segundo. Entre la semana 1 y la 2 subió 15 unidades. Entre la 2 y la 3 se mantuvo. Entre la 4 y la 5 bajó 15. Siempre di entre qué momentos ocurre el cambio.",
        "También puedes encontrar el punto más alto, el más bajo y el tramo de mayor subida. La línea no dice por qué cambió; solo dice cómo cambió. Si quieres explicar las razones, necesitas más información. Usa palabras claras y los números exactos.",
    ],
    vocab=[("tramo", "parte de la línea entre dos puntos"), ("subir", "pasar a un dato mayor"), ("bajar", "pasar a un dato menor"), ("mantenerse", "quedar igual"), ("punto más alto", "dato mayor del gráfico"), ("cambio", "cuánto sube o baja entre dos momentos")],
    worked=[
        ("Leer un tramo", "En la ficha, ¿qué ocurre entre la semana 2 y la semana 3?", ["Los dos puntos están a la misma altura: 55 y 55.", "Por lo tanto la línea se mantiene."], "Se mantiene en 55"),
        ("Mayor subida", "¿Cuánto subió entre la semana 3 y la 4?", ["Semana 3: 55. Semana 4: 75.", "Resta 75 − 55 = 20."], "20 unidades")
    ],
    mistakes=[("Decir que la línea sube siempre porque termina más alta que como empezó.", "Se mira solo el inicio y el fin.", "Revisa cada tramo entre dos puntos seguidos."),
              ("Explicar por qué subió, como «porque llegó más gente».", "El gráfico no da razones.", "Describe el cambio con números y di que las razones necesitan más información.")],
    T=[
        ("{F} ¿Cuántas unidades se vendieron en la semana 3?", "55 unidades", "El punto de la semana tres está en el cincuenta y cinco."),
        ("abc", "{F} ¿Qué ocurre entre la semana 2 y la semana 3?", "Se mantiene", "Sube", "Baja", "Los dos puntos tienen el mismo valor."),
        ("=", "{F} ¿Cuántas unidades subió entre la semana 1 y la semana 2?", "55-40", "Se resta el dato inicial al final.", " unidades"),
        ("abc", "{F} ¿En qué semana hubo más ventas?", "Semana 4", "Semana 2", "Semana 5", "El punto más alto es el de setenta y cinco, en la semana cuatro."),
        ("=", "{F} ¿Cuánto subió entre la semana 3 y la semana 4?", "75-55", "Se resta el dato inicial al final.", " unidades"),
        ("=", "{F} ¿Cuántas unidades bajó entre la semana 4 y la semana 5?", "75-60", "Se resta el dato final al inicial.", " unidades"),
        ("ab", "{F} ¿En qué tramo baja la línea?", "Entre la semana 4 y la 5", "Entre la semana 1 y la 2", "Solo ese tramo termina en un dato menor que el inicial."),
        ("=", "{F} ¿Cuántas unidades se vendieron en total en las cinco semanas?", "40+55+55+75+60", "Se suman los cinco puntos.", " unidades"),
        ("abc", "{F} ¿Cuántos tramos tiene la línea?", "4", "5", "3", "Cinco puntos forman cuatro tramos entre ellos."),
        ("=", "{F} ¿Cuántas unidades más se vendieron en la semana 4 que en la semana 1?", "75-40", "Se resta el dato menor del mayor.", " unidades"),
        ("abc", "Alguien dice: «subió porque llegó más gente». ¿Qué respondes?", "El gráfico muestra cuánto subió, no por qué", "Es seguro que fue por eso", "No subió", "La línea solo entrega datos, no razones."),
        ("=", "{F} ¿Cuántas unidades se vendieron en las semanas 2 y 3 juntas?", "55+55", "Se suman los dos puntos pedidos.", " unidades"),
        ("abc", "{F} ¿Qué frase describe bien la línea?", "Sube, se mantiene, sube y luego baja", "Sube siempre", "Baja siempre", "La descripción sigue cada tramo: sube, igual, sube y baja."),
    ],
    ctx=("=", "La dueña de un puesto de ejemplo ve que en la semana 4 vendió 75 unidades y en la semana 5, 60. Para pedir mercadería quiere saber cuántas unidades bajó. ¿Cuántas fueron?", "75-60", "Se resta el dato final al dato inicial.", " unidades"),
    sc=[("¿Cómo sabes si la línea sube en un tramo?", "El segundo punto está más alto que el primero", "El valor mayor al final indica una subida."),
        ("¿Qué operación usas para saber cuánto cambió?", "Una resta", "Restar los datos de dos puntos da el cambio."),
        ("¿Qué no dice un gráfico de línea?", "Las razones del cambio", "Muestra datos, no explica por qué ocurren.")],
    op=("Describe este gráfico de línea de ejemplo, de personas atendidas por mes en un consultorio vecinal (datos inventados): Marzo 30, Abril 45, Mayo 45, Junio 35, Julio 50. Escribe tres frases sobre cómo cambia y calcula el total.",
        "«Entre marzo y abril sube 15. Entre abril y mayo se mantiene. Entre mayo y junio baja 10 y luego sube 15 hasta julio.» Total: 30 + 45 + 45 + 35 + 50 = 205.",
        ["describe tramos con subir, bajar o mantenerse", "calcula cambios correctos", "total correcto"],
        ["hoja con tres frases y el total"],
        ["decir que sube siempre", "dar razones que los datos no muestran"],
        "Pregunta: «¿entre qué meses bajó y cuánto?». Debe responder entre mayo y junio, 10."),
    reinforce="Escribe una frase con números que describa el tramo de la semana 1 a la semana 3.",
    extend="Explica por qué dos gráficos de línea con la misma forma pueden tener números muy distintos.",
)

# ===================================================== OAD-16 clase 6
F = ("Datos de ejemplo. Caso 1: transporte que usan 30 personas de un taller: Bus 14, Metro 10, A pie 6. "
     "Caso 2: kilos de pan vendidos en un local por mes: Enero 80, Febrero 90, Marzo 85, Abril 100.")
build(
    O16, 6, F,
    use="Voy a elegir entre barras y línea, y a explicar a otra persona cómo elaboré mi gráfico y qué concluyo.",
    prior=["Sé elaborar barras y líneas.", "Sé que una conclusión honesta usa números.", "Sé calcular diferencias."],
    explain=[
        "Al compartir información, primero decide qué gráfico usar. Si comparas categorías distintas, como tipos de transporte, usa barras. Si los datos van en orden de tiempo, como las ventas de cada mes, usa una línea. La elección depende de lo que quieres mostrar.",
        "Luego explica a otra persona los pasos: qué datos usaste, qué escala elegiste, cómo dibujaste y qué muestra el gráfico. Termina con una conclusión honesta, con números exactos, sin exagerar. Por ejemplo: «el bus es el medio más usado: 14 de 30 personas».",
        "Compartir bien es respetar a quien te escucha. Usa palabras simples, muestra el gráfico completo, con título y rótulos, y responde preguntas. Si alguien te pide una razón que los datos no muestran, di con honestidad que no lo sabes. Eso también es explicar con claridad.",
    ],
    vocab=[("compartir", "mostrar información a otras personas"), ("conclusión honesta", "idea que usa números exactos y no exagera"), ("barras", "gráfico para comparar categorías"), ("línea", "gráfico para ver cambios en el tiempo"), ("explicar los pasos", "contar qué hiciste y por qué"), ("exagerar", "hacer parecer algo mayor de lo que es")],
    worked=[
        ("Elegir el gráfico", "Para el caso 1, ¿barras o línea?", ["Bus, metro y a pie son categorías, no momentos del tiempo.", "Para comparar categorías conviene un gráfico de barras."], "Barras"),
        ("Conclusión honesta", "Escribe una conclusión para el caso 2.", ["Enero 80, abril 100: la diferencia es 20.", "Frase: «Entre enero y abril se vendieron 20 kilos más de pan»."], "20 kilos más entre enero y abril")
    ],
    mistakes=[("Elegir línea para comparar bus, metro y a pie.", "Se une con una línea algo que no sigue un orden de tiempo.", "Para categorías, usa barras."),
              ("Concluir «las ventas siempre suben» con cuatro meses.", "Se saca una regla de pocos datos.", "Di solo lo que ocurrió entre enero y abril.")],
    T=[
        ("abc", "{F} ¿Qué gráfico conviene para el caso 1?", "Barras", "Línea", "Ninguno", "El caso uno compara categorías, y para eso se usan barras."),
        ("abc", "{F} ¿Qué gráfico conviene para el caso 2?", "Línea", "Barras separadas sin orden", "Ninguno", "Los meses están en orden de tiempo, y la línea muestra su cambio."),
        ("=", "{F} ¿Cuántas personas hay en total en el caso 1?", "14+10+6", "Se suman las tres categorías.", " personas"),
        ("=", "{F} ¿Cuántos kilos de pan se vendieron en total en el caso 2?", "80+90+85+100", "Se suman los cuatro meses.", " kilos"),
        ("abc", "{F} ¿Qué conclusión es honesta para el caso 1?", "El bus es el más usado: 14 de 30 personas", "Todas las personas prefieren el bus", "Nadie va a pie", "La conclusión honesta usa el dato exacto de la tabla."),
        ("=", "{F} ¿Cuántos kilos más se vendieron en abril que en enero?", "100-80", "Se resta el dato inicial al final.", " kilos"),
        ("ab", "{F} ¿Por qué se usa una línea en el caso 2?", "Porque muestra cómo cambian las ventas mes a mes", "Porque tiene menos datos", "Las ventas siguen el orden de los meses y la línea muestra ese cambio."),
        ("=", "{F} ¿Cuántas personas más van en bus que a pie?", "14-6", "Se resta el dato menor del mayor.", " personas"),
        ("abc", "¿Qué debes hacer al explicar tu gráfico a otra persona?", "Contar los pasos y dar una conclusión con números", "Mostrarlo sin hablar", "Explicar solo el color", "Explicar con pasos y números ayuda a que otra persona lo entienda."),
        ("=", "{F} ¿Cuántos kilos bajó el pan de febrero a marzo?", "90-85", "Se resta el dato final al inicial.", " kilos"),
        ("ab", "Alguien dice: «las ventas siempre suben». Con estos datos, ¿es honesto?", "No: bajaron entre febrero y marzo", "Sí: terminaron más altas", "Entre febrero y marzo las ventas pasaron de 90 a 85, es decir bajaron."),
        ("=", "{F} ¿Cuántas personas NO usan el metro?", "14+6", "Se suman las otras dos categorías.", " personas"),
        ("abc", "Si te preguntan por qué subió el pan y el dato no lo dice, ¿qué contestas?", "Que el gráfico no muestra las razones", "Invento una razón", "Digo que fue por el clima", "Ser honesto es decir que los datos no lo muestran."),
    ],
    ctx=("=", "Una instructora de un taller de ejemplo presenta su gráfico de transporte a la directora. Si 14 personas van en bus y 10 en metro, ¿cuántas personas usan transporte público?", "14+10", "Se suman las dos categorías de transporte público.", " personas"),
    sc=[("¿Cuándo usas barras y cuándo línea?", "Barras para comparar categorías y línea para cambios en el tiempo", "Cada gráfico responde a una necesidad distinta."),
        ("¿Qué incluye una buena explicación de un gráfico?", "Los pasos, la escala y una conclusión con números", "Eso permite que otra persona lo comprenda y lo compruebe."),
        ("¿Qué haces si no sabes la razón de un cambio?", "Digo que el gráfico no la muestra", "Ser honesto evita inventar explicaciones que no existen.")],
    op=("Elige el gráfico adecuado para estos datos de ejemplo y explícalo a otra persona en cinco frases: Personas atendidas en una oficina de trámites por mes: Enero 40, Febrero 48, Marzo 48, Abril 36. Incluye una conclusión honesta.",
        "Línea, porque son meses en orden. Escala de 4 en 4 hasta 48. «Subió 8 de enero a febrero, se mantuvo en marzo y bajó 12 en abril». Conclusión: «Abril fue el mes con menos atenciones, 36».",
        ["elige línea y da la razón", "calcula bien los cambios", "conclusión honesta con números"],
        ["hoja con el gráfico y cinco frases"],
        ["elegir barras sin justificar", "exagerar o dar razones inventadas"],
        "Pregunta: «¿cómo le explicarías a una vecina por qué elegiste esa escala?». Debe dar la razón."),
    reinforce="Explica a una persona de tu casa uno de los gráficos de este módulo en tres frases.",
    extend="Escribe una situación de la vida diaria en que convenga una línea y otra en que convengan barras.",
)

# ===================================================== OAD-16 clase 7
F = ("Datos de ejemplo. Ventas por trimestre de una librería: Trimestre 1 → 30, Trimestre 2 → 45, Trimestre 3 → 40, Trimestre 4 → 60. "
     "Escala de 5 en 5 hasta 60. También: preferencia de lectura de 20 personas (categorías): Novela 8, Poesía 4, Cuento 6, Ensayo 2.")
build(
    O16, 7, F,
    use="Voy a repasar cómo se elabora y se explica un gráfico de barras o de línea y a decidir qué quiero practicar.",
    prior=["Sé hacer barras y líneas.", "Sé elegir una escala.", "Sé escribir una conclusión honesta."],
    explain=[
        "Hoy repasas todo el módulo de datos. Para elaborar un gráfico: ordena la tabla, elige una escala que parta en cero y llegue al dato mayor, dibuja barras o puntos unidos, y escribe título y rótulos. Para elegir tipo de gráfico: barras para categorías, línea para cambios en el tiempo.",
        "Para leer un gráfico: mira el título y los ejes, ubica los datos que necesitas, resta para comparar y suma para totales. Para compartirlo: explica los pasos con tus palabras, usa números exactos y escribe una conclusión honesta, sin exagerar ni inventar razones.",
        "Revisa tu trabajo con una lista: ¿la escala parte en cero?, ¿las barras tienen el mismo ancho?, ¿la línea une los puntos en orden?, ¿puse título y rótulos?, ¿mi conclusión usa números del gráfico? Decide qué parte quieres practicar más para el próximo módulo.",
    ],
    vocab=[("elaborar", "construir paso a paso"), ("escala", "números del eje vertical"), ("rótulo", "palabra que explica qué mide un eje"), ("conclusión", "idea que sale de los datos"), ("trimestre", "período de tres meses"), ("revisar", "comprobar que algo esté bien")],
    worked=[
        ("Elegir el gráfico", "En la ficha, ¿qué gráfico conviene para las ventas por trimestre?", ["Los trimestres son momentos del tiempo, en orden.", "Conviene un gráfico de línea."], "Línea"),
        ("Cambio entre trimestres", "¿Cuánto cambió entre el trimestre 2 y el 3?", ["Trimestre 2: 45. Trimestre 3: 40.", "Como el dato baja, se resta al revés: 45 − 40 = 5."], "Bajó 5 unidades")
    ],
    mistakes=[("Usar barras para ver el cambio de las ventas en el tiempo.", "Se elige el gráfico sin pensar en lo que se quiere mostrar.", "Para ver cambios en el tiempo, usa una línea."),
              ("Entregar el gráfico sin revisar la escala.", "Se confía en que quedó bien.", "Revisa que la escala parta en cero y llegue al dato mayor.")],
    T=[
        ("abc", "{F} ¿Qué gráfico conviene para las ventas por trimestre?", "Línea", "Barras de colores sin orden", "Ninguno", "Los trimestres van en orden de tiempo y la línea muestra el cambio."),
        ("abc", "{F} ¿Qué gráfico conviene para la preferencia de lectura?", "Barras", "Línea", "Ninguno", "Novela, poesía, cuento y ensayo son categorías, que se comparan con barras."),
        ("=", "{F} ¿Cuántas ventas hubo en total en el año?", "30+45+40+60", "Se suman los cuatro trimestres.", " ventas"),
        ("=", "{F} ¿Cuánto subieron las ventas entre el trimestre 1 y el 2?", "45-30", "Se resta el dato inicial al final.", " ventas"),
        ("=", "{F} ¿Cuánto bajaron entre el trimestre 2 y el 3?", "45-40", "Se resta el dato final al inicial.", " ventas"),
        ("abc", "{F} ¿En qué trimestre fue mayor la venta?", "Trimestre 4", "Trimestre 2", "Trimestre 3", "El dato mayor es sesenta, del cuarto trimestre."),
        ("=", "{F} ¿Cuántas personas hay en total en la preferencia de lectura?", "8+4+6+2", "Se suman las cuatro categorías.", " personas"),
        ("=", "{F} ¿Cuántas personas más prefieren novela que ensayo?", "8-2", "Se resta el dato menor del mayor.", " personas"),
        ("ab", "{F} ¿Cuántas marcas sube la barra de Cuento si la escala sube de 2 en 2?", "3", "6", "Seis dividido en dos da tres marcas."),
        ("abc", "{F} ¿Qué conclusión honesta se puede escribir sobre la lectura?", "La novela es la preferida de 8 de las 20 personas", "A todos les gusta la novela", "Nadie lee ensayo", "La conclusión honesta usa el dato exacto de la tabla."),
        ("=", "{F} ¿Cuántas ventas hubo en el trimestre 3 y en el 4 juntos?", "40+60", "Se suman los dos datos pedidos.", " ventas"),
        ("ab", "Una persona dibujó una escala que parte en 30 para las ventas. ¿Qué problema tiene?", "Exagera las diferencias porque no parte en cero", "Ninguno", "Una escala que no parte en cero cambia lo que parece la diferencia."),
        ("abc", "¿Qué tres cosas revisas antes de compartir un gráfico?", "Escala, título y rótulos", "Solo el color", "Solo el tamaño de la hoja", "Con esos elementos el gráfico se entiende y no engaña."),
    ],
    ctx=("=", "La encargada de una librería de ejemplo presenta sus ventas al dueño. Si en el trimestre 1 vendió 30 y en el trimestre 4 vendió 60, ¿cuántas ventas más hubo en el trimestre 4?", "60-30", "Se resta el dato inicial al final.", " ventas"),
    sc=[("¿Qué haces primero para elaborar un gráfico?", "Ordeno los datos en una tabla", "La tabla ordena los datos antes de dibujar."),
        ("¿Cómo eliges entre barras y línea?", "Según si comparo categorías o veo cambios en el tiempo", "Cada tipo de gráfico responde a una pregunta distinta."),
        ("¿Qué lista de revisión usas antes de compartir un gráfico?", "Escala desde cero, título, rótulos y conclusión con números", "Esa lista permite que el gráfico se entienda y no exagere diferencias.")],
    op=("Con estos datos de ejemplo de una feria (kilos de verdura vendidos por semana: S1 24, S2 36, S3 30, S4 42), elabora el gráfico de línea con escala de 6 en 6, escribe título y rótulos, y explica a otra persona en tres frases con una conclusión honesta.",
        "Puntos en 24, 36, 30 y 42, unidos en orden, escala 0, 6, 12, … 42. Frases: «La venta sube 12, baja 6 y vuelve a subir 12. La semana 4 fue la mejor, con 42 kilos. Los datos no explican el motivo».",
        ["gráfico correcto con escala de 6 en 6", "título y rótulos", "tres frases con números y conclusión honesta"],
        ["hoja con el gráfico y las tres frases"],
        ["escala que no parte en cero", "dar razones que los datos no muestran"],
        "Pregunta: «¿qué parte de este módulo dominas y qué quieres repasar?». Anotarla ayuda a elegir qué practicar."),
    reinforce="Haz el gráfico de barras de la preferencia de lectura de la ficha, con escala de 2 en 2.",
    extend="Explica con tus palabras cuándo un gráfico puede engañar sin querer y cómo evitarlo.",
)
