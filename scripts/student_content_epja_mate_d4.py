"""Matemática EPJA Nivel 1 básico, módulo 4: OAD-14 clases 5 a 8 (del gráfico a la tabla, sorteos con moneda y dado, y repaso). Datos de ejemplo, inventados; los resultados de los sorteos vienen escritos en cada ficha; sin apuestas."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Hoja, lápiz de mina y regla. Todo se hace en papel; los resultados de cada sorteo vienen escritos en la ficha, no hace falta moneda ni dado. Todos los datos son de ejemplo, inventados."
build = make_build(MATERIALS)

O14 = "EPJA-MATE-NB1-OAD-14"

# ===================================================== OAD-14 clase 5
F = ("Datos de ejemplo. Gráfico de barras, escala de 1 en 1: «Libros prestados por día en una biblioteca vecinal». "
     "Lunes 6, Martes 9, Miércoles 4, Jueves 7, Viernes 10.")
build(
    O14, 5, F,
    use="Voy a pasar un gráfico de barras a una tabla de frecuencia leyendo la altura de cada barra.",
    prior=["Sé leer un gráfico de barras.", "Sé qué es una tabla de frecuencia.", "Sé sumar cinco números pequeños."],
    explain=[
        "Así como de una tabla sale un gráfico, de un gráfico de barras sale una tabla. Haz una fila por cada barra: en la primera columna escribe el nombre de la categoría y en la segunda la altura de la barra, que es su frecuencia.",
        "Para leer cada altura, baja desde la punta de la barra hasta la escala. Después suma todas las frecuencias y escribe el total al final. Ese total es la cantidad de datos que había: aquí, la cantidad de libros prestados en la semana.",
        "La tabla y el gráfico cuentan lo mismo. Pasar de uno a otro es como convertir una receta escrita en una lista de compras: cambia la forma, no la información. Si el total te parece raro, vuelve a leer las barras.",
    ],
    vocab=[("gráfico de barras", "dibujo con barras que muestra cantidades"), ("tabla de frecuencia", "tabla con categorías y cuántas veces aparece cada una"), ("préstamo", "entrega de un libro por un tiempo"), ("altura", "qué tan alta llega la barra"), ("total", "suma de todas las frecuencias"), ("convertir", "cambiar la forma de mostrar algo")],
    worked=[
        ("Leer una barra", "En la ficha, ¿qué frecuencia anotas para el martes?", ["Busca la barra del martes.", "Baja hasta la escala: llega a 9."], "9"),
        ("Total de la tabla", "¿Cuántos libros se prestaron en la semana?", ["Suma 6 + 9 + 4 + 7 + 10.", "El resultado es 36."], "36 libros"),
    ],
    mistakes=[("Escribir en la tabla el nombre del día pero no su frecuencia.", "Se copia el eje de abajo y se olvida la altura.", "Cada fila lleva dos datos: la categoría y su altura."),
              ("Leer una barra en un número vecino de la escala.", "Se mira rápido y no se baja hasta la escala.", "Apoya la regla sobre la punta de la barra y lee la marca exacta.")],
    T=[
        ("abc", "¿Qué escribes en la tabla por cada barra?", "El nombre de la categoría y su altura", "Solo el color", "Solo el título", "Cada fila de la tabla reúne la categoría y su frecuencia."),
        ("{F} ¿Cuántos libros se prestaron el martes?", "9 libros", "La barra del martes llega a la marca nueve."),
        ("=", "{F} ¿Cuántos libros se prestaron en toda la semana?", "6+9+4+7+10", "Se suman las cinco frecuencias.", " libros"),
        ("abc", "{F} ¿Qué día tuvo la menor frecuencia?", "Miércoles", "Lunes", "Viernes", "La barra más baja es la del miércoles, con cuatro libros."),
        ("=", "{F} ¿Cuántos libros más se prestaron el viernes que el miércoles?", "10-4", "Se resta la frecuencia menor de la mayor.", " libros"),
        ("ab", "{F} ¿Cuántas filas tendrá la tabla?", "5", "36", "Se hace una fila por cada barra y hay una para cada día."),
        ("=", "{F} ¿Cuántos libros se prestaron entre lunes y martes?", "6+9", "Se suman las dos frecuencias.", " libros"),
        ("abc", "{F} ¿Cuál tabla representa bien el gráfico?", "Lunes 6, Martes 9, Miércoles 4, Jueves 7, Viernes 10", "Lunes 9, Martes 6, Miércoles 7, Jueves 4, Viernes 10", "Lunes 6, Martes 9, Miércoles 7, Jueves 4, Viernes 10", "La tabla correcta copia cada altura en su día."),
        ("=", "{F} ¿Cuántos libros se prestaron de miércoles a viernes?", "4+7+10", "Se suman las tres frecuencias pedidas.", " libros"),
        ("=", "{F} Si se quita el viernes, ¿cuántos libros suman los otros cuatro días?", "36-10", "Se resta del total la frecuencia del viernes.", " libros"),
        ("ab", "Una tabla de este gráfico da un total de 35. ¿Qué haces?", "Vuelvo a leer las barras", "Dejo la tabla así", "El total correcto es 36, por lo tanto debe haber un error de lectura."),
        ("=", "{F} Si el jueves se prestan 3 libros más, ¿cuántos serán?", "7+3", "Se suman los libros nuevos a la frecuencia.", " libros"),
        ("abc", "{F} ¿Cuántos días tuvieron al menos 7 préstamos?", "3", "5", "2", "Martes con 9, jueves con 7 y viernes con 10 llegan a siete o más."),
    ],
    ctx=("=", "La encargada de una biblioteca vecinal de ejemplo debe informar cuántos libros prestó de lunes a miércoles. Lunes 6, martes 9 y miércoles 4. ¿Cuántos fueron?", "6+9+4", "Se suman las tres frecuencias de la tabla.", " libros"),
    sc=[("¿Cómo lees la frecuencia de una barra?", "Bajo desde su punta hasta la escala", "La escala da el número exacto de esa barra."),
        ("¿Qué debe dar la suma de las frecuencias de la tabla?", "El total de datos del gráfico", "El total refleja todos los elementos contados."),
        ("¿Cuántas filas tiene una tabla de un gráfico con 4 barras?", "4", "Cada barra se convierte en una fila de la tabla.")],
    op=("Pasa a una tabla de frecuencia este gráfico de ejemplo: «Postres vendidos» (escala de 1 en 1): Helado 8, Flan 5, Torta 11. Escribe el total y una frase.",
        "Helado 8, Flan 5, Torta 11. Total: 24. Frase: «La torta fue lo más vendido, con 11 postres».",
        ["una fila por barra", "frecuencias 8, 5 y 11", "total 24 y una frase correcta"],
        ["hoja con la tabla y la frase"],
        ["mezclar las alturas entre categorías", "no sumar el total"],
        "Pregunta: «¿qué postre vendió menos y cuántos menos que la torta?». Debe responder flan, 6 menos."),
    reinforce="Dibuja un gráfico de barras con tres datos de ejemplo y pásalo a tabla.",
    extend="Explica qué información de la tabla no se ve a simple vista en el gráfico, y al revés.",
)

# ===================================================== OAD-14 clase 6
F = ("Datos de ejemplo. Dos personas de un mismo turno sortean quién abre el local lanzando una moneda 20 veces; el sorteo es solo para decidir turnos, sin apuestas. "
     "C = cara, S = sello. Resultados en orden: C S S C C S C S C C S S C S C C S C S C.")
build(
    O14, 6, F,
    use="Voy a anotar y contar los resultados de un sorteo con moneda y a entender qué es un experimento aleatorio.",
    prior=["Sé contar con marcas de recuento.", "Sé armar una tabla de frecuencia.", "Sé que un sorteo sirve para decidir."],
    explain=[
        "Un experimento aleatorio es uno en que no puedes saber de antemano qué va a pasar. Lanzar una moneda es un ejemplo: puede salir cara o sello. Se usa para sortear turnos o decidir quién empieza, porque nadie controla el resultado.",
        "Cuando repites el experimento muchas veces, puedes anotar cada resultado con marcas de recuento y armar una tabla de frecuencia. Cada resultado posible es una categoría, y su frecuencia es las veces que salió. Aquí los resultados posibles son dos: cara y sello.",
        "Que las frecuencias no queden idénticas no significa que la moneda esté mala. Con pocos lanzamientos es normal que un lado salga algunas veces más. Usamos la moneda solo para sortear; en este curso no se juega dinero ni se hacen apuestas.",
    ],
    vocab=[("experimento aleatorio", "situación en que no se sabe de antemano qué resultado saldrá"), ("resultado posible", "cada cosa que puede salir"), ("cara y sello", "los dos lados de una moneda"), ("sorteo", "forma de decidir sin elegir a propósito"), ("lanzamiento", "cada vez que se tira la moneda"), ("frecuencia", "cuántas veces salió un resultado")],
    worked=[
        ("Contar caras", "En la ficha, ¿cuántas caras (C) salieron?", ["Recorre la lista y marca cada C.", "Salen 11 marcas: IIIII IIIII I."], "11 caras"),
        ("Contar sellos", "Si hubo 20 lanzamientos y 11 caras, ¿cuántos sellos hubo?", ["Cada lanzamiento es cara o sello.", "Resta: 20 − 11 = 9."], "9 sellos"),
    ],
    mistakes=[("Pensar que después de 3 caras seguidas el siguiente es seguro un sello.", "Se cree que la moneda «compensa».", "Cada lanzamiento es independiente: nadie puede saber cuál saldrá."),
              ("Creer que la moneda está mala porque no salieron 10 caras y 10 sellos.", "Se espera un resultado exacto.", "Con pocos lanzamientos es normal una pequeña diferencia.")],
    T=[
        ("abc", "¿Qué significa que un experimento sea aleatorio?", "No se sabe de antemano qué va a salir", "Siempre sale lo mismo", "Se puede predecir con seguridad", "En un experimento aleatorio el resultado depende del azar."),
        ("{F} ¿Cuántas caras salieron en los 20 lanzamientos?", "11 caras", "Al recorrer la lista aparecen once caras."),
        ("=", "{F} ¿Cuántos lanzamientos se hicieron en total sumando caras y sellos?", "11+9", "Se suman las frecuencias de los dos resultados.", " lanzamientos"),
        ("abc", "{F} ¿Qué resultados posibles tiene cada lanzamiento?", "Cara o sello", "Solo cara", "Cara, sello o canto, siempre igual", "Una moneda cae mostrando uno de sus dos lados."),
        ("=", "{F} ¿Cuántas caras más que sellos salieron?", "11-9", "Se resta la frecuencia menor de la mayor.", " caras"),
        ("ab", "{F} ¿Se puede saber antes del primer lanzamiento si saldrá cara?", "No, porque es un experimento aleatorio", "Sí, siempre sale cara primero", "El resultado depende del azar, por lo tanto no se puede asegurar."),
        ("{F} ¿Cuántos sellos hubo en los primeros 10 lanzamientos?", "4 sellos", "Los primeros diez son C S S C C S C S C C, con cuatro sellos."),
        ("=", "{F} Si se lanzan 15 veces más, ¿cuántos lanzamientos habrá en total?", "20+15", "Se suman los lanzamientos nuevos a los anteriores.", " lanzamientos"),
        ("abc", "Salieron 11 caras y 9 sellos. ¿Qué significa?", "Es una diferencia normal en un sorteo", "La moneda está trucada seguro", "Hay un error en el conteo", "Con pocos lanzamientos las frecuencias casi nunca quedan iguales."),
        ("abc", "¿Por qué sirve una moneda para sortear quién abre el local?", "Porque ninguna persona controla el resultado", "Porque siempre sale cara", "Porque es más rápido elegir al que cae mejor", "El azar da igual oportunidad a las dos personas."),
        ("=", "{F} Si salieron 11 caras en 20 lanzamientos, ¿cuántos NO fueron caras?", "20-11", "Se resta del total la frecuencia de caras.", " lanzamientos"),
        ("ab", "Salieron 3 caras seguidas. ¿Qué se puede decir del próximo lanzamiento?", "No se sabe: puede ser cara o sello", "Seguro sale sello", "El lanzamiento siguiente no depende de los anteriores."),
        ("=", "{F} En los primeros 10 lanzamientos salieron 6 caras. ¿Cuántos sellos salieron en esos 10?", "10-6", "Se resta de diez las caras de ese tramo.", " sellos"),
    ],
    ctx=("=", "Dos vendedoras de una feria de ejemplo sortean con una moneda quién ocupa el puesto de la esquina durante 20 días. Ganó la cara 11 veces. ¿Cuántos días ganó el sello?", "20-11", "Se resta del total lo que ganó la cara.", " días"),
    sc=[("¿Qué es un experimento aleatorio?", "Uno en que no se sabe de antemano el resultado", "El azar decide cuál de los resultados posibles sale."),
        ("En un sorteo de turnos, ¿cuántos resultados posibles tiene lanzar una moneda?", "Dos: cara y sello", "La moneda tiene solo dos lados."),
        ("¿Qué haces con los resultados de varios lanzamientos?", "Los cuento y los anoto en una tabla de frecuencia", "La tabla ordena cuántas veces salió cada resultado.")],
    op=("Estos son 10 lanzamientos de ejemplo: C S C C S S C S C C. Anota los resultados con marcas, arma la tabla de frecuencia y escribe una frase sobre lo que viste.",
        "Cara: IIIII I (6). Sello: IIII (4). Total 10. Frase: «Salió cara 6 veces y sello 4; no se podía saber antes».",
        ["cuenta bien las frecuencias 6 y 4", "total igual a 10", "frase que no promete lo que pasará después"],
        ["hoja con las marcas, la tabla y la frase"],
        ["decir que el próximo resultado es seguro", "no sumar el total"],
        "Pregunta: «¿podías saber el primer resultado antes de lanzar?». Debe responder que no."),
    reinforce="Escribe tres situaciones de tu vida en que se use un sorteo para decidir turnos.",
    extend="Explica por qué no hace falta que salgan igual número de caras y de sellos para que la moneda sea justa.",
)

# ===================================================== OAD-14 clase 7
F = ("Datos de ejemplo. Un equipo de aseo sortea el orden de limpieza lanzando un dado de seis caras 30 veces (solo para sortear; sin apuestas). "
     "Tabla de frecuencia: resultado 1: 4 veces. 2: 6. 3: 5. 4: 7. 5: 3. 6: 5. Gráfico de barras con escala de 1 en 1, del 0 al 8.")
build(
    O14, 7, F,
    use="Voy a leer la tabla y el gráfico de un sorteo con dado y a decir qué se puede afirmar y qué no.",
    prior=["Sé leer tablas de frecuencia.", "Sé leer gráficos de barras.", "Sé qué es un experimento aleatorio."],
    explain=[
        "Un dado común tiene seis caras con los números 1, 2, 3, 4, 5 y 6. Al lanzarlo puede salir cualquiera de esos seis resultados. Es otro experimento aleatorio: no puedes saber de antemano cuál va a salir.",
        "Si lo lanzas muchas veces, anotas cuántas veces salió cada número. Eso es una tabla de frecuencia absoluta con seis filas. Con el gráfico de barras ves cuál número salió más y cuál menos. Pero las frecuencias cambian cada vez que repites el experimento.",
        "Por eso, de una tabla de dado solo puedes afirmar lo que ya pasó: «el 4 salió 7 veces». No puedes asegurar lo que pasará en los próximos lanzamientos. Esta diferencia entre lo que ocurrió y lo que no se puede prometer es una idea importante.",
    ],
    vocab=[("dado", "cubo con seis caras numeradas del 1 al 6"), ("cara del dado", "cada lado con un número"), ("resultado", "número que sale al lanzar"), ("tabla de seis filas", "una fila por cada resultado posible"), ("par", "número que se puede repartir en dos grupos iguales: 2, 4 y 6"), ("sortear", "decidir con ayuda del azar")],
    worked=[
        ("Leer la tabla", "En la ficha, ¿cuántas veces salió el 4?", ["Busca la fila del 4.", "La frecuencia es 7."], "7 veces"),
        ("Verificar el total", "¿Suman 30 las frecuencias?", ["Suma 4 + 6 + 5 + 7 + 3 + 5.", "4 + 6 = 10; 10 + 5 = 15; 15 + 7 = 22; 22 + 3 = 25; 25 + 5 = 30."], "Sí, suman 30"),
    ],
    mistakes=[("Decir «el 5 casi no sale, así que en los próximos 30 saldrá poco».", "Se toma lo que pasó como si fuera una regla.", "Di solo lo que pasó: el 5 salió 3 veces en estos 30 lanzamientos."),
              ("Olvidar el número 6 al armar la tabla porque no salió seguido.", "Se arma la tabla solo con lo que se recuerda.", "Escribe siempre una fila por cada resultado posible, uno al seis.")],
    T=[
        ("abc", "¿Cuántos resultados posibles tiene un dado de seis caras?", "6", "3", "30", "El dado muestra uno de los números del uno al seis."),
        ("{F} ¿Cuántas veces salió el 4?", "7 veces", "La fila del 4 de la tabla dice siete."),
        ("=", "{F} ¿Cuántos lanzamientos se hicieron en total?", "4+6+5+7+3+5", "Se suman las seis frecuencias.", " lanzamientos"),
        ("abc", "{F} ¿Qué número salió menos veces?", "5", "1", "4", "El cinco tiene la frecuencia menor, tres veces."),
        ("=", "{F} ¿Cuántas veces más salió el 4 que el 5?", "7-3", "Se resta la frecuencia menor de la mayor.", " veces"),
        ("ab", "{F} ¿Salió el 2 más veces que el 1?", "Sí: 6 veces contra 4", "No: salió menos", "Seis es mayor que cuatro, por eso el dos salió más."),
        ("=", "{F} ¿Cuántas veces salió el 1 o el 2?", "4+6", "Se suman las dos frecuencias pedidas.", " veces"),
        ("=", "{F} ¿Cuántos lanzamientos NO fueron un 4?", "30-7", "Se resta del total la frecuencia del cuatro.", " lanzamientos"),
        ("abc", "Un compañero dice: «en los próximos 30 lanzamientos el 5 saldrá otra vez 3 veces». ¿Es seguro?", "No, el resultado depende del azar", "Sí, siempre sale igual", "Sí, porque ya pasó", "Una repetición nueva del experimento puede dar frecuencias distintas."),
        ("=", "{F} ¿Cuántas veces salió el 5 o el 6?", "3+5", "Se suman las dos frecuencias pedidas.", " veces"),
        ("ab", "{F} Los lanzamientos de la tabla suman", "30", "6", "Las seis frecuencias suman treinta, igual que los lanzamientos."),
        ("=", "{F} ¿Cuántas veces salió un número par (2, 4 o 6)?", "6+7+5", "Se suman las frecuencias de los números pares.", " veces"),
        ("abc", "{F} ¿Qué barra del gráfico es la más alta?", "La del 4", "La del 5", "La del 1", "El cuatro tiene la mayor frecuencia, por eso su barra es la más alta."),
    ],
    ctx=("=", "Un equipo de aseo de ejemplo usa 30 lanzamientos de dado para repartir turnos. Los turnos del 1 y del 2 se hacen en la mañana. Si el 1 salió 4 veces y el 2 salió 6 veces, ¿cuántos turnos de mañana se asignaron?", "4+6", "Se suman las frecuencias de los dos números.", " turnos"),
    sc=[("¿Cuántas filas tiene la tabla de un dado de seis caras?", "Seis", "Cada resultado posible tiene su fila."),
        ("¿Qué puedes afirmar con la tabla?", "Lo que ya ocurrió en esos lanzamientos", "Los datos muestran lo pasado, no lo que ocurrirá."),
        ("¿Qué tienen en común un dado y una moneda?", "Ambos dan resultados que dependen del azar", "En los dos no se sabe de antemano qué saldrá.")],
    op=("Un grupo anotó 12 lanzamientos de ejemplo de un dado: 3, 5, 1, 6, 3, 2, 3, 4, 6, 3, 1, 5. Arma la tabla de frecuencia con las seis filas y dibuja las barras con escala de 1 en 1 del 0 al 5.",
        "1: 2, 2: 1, 3: 4, 4: 1, 5: 2, 6: 2. Total 12. Barras de alturas 2, 1, 4, 1, 2 y 2; el 3 tiene la barra más alta.",
        ["una fila para cada número del 1 al 6", "frecuencias correctas", "total 12 y barras con esas alturas"],
        ["hoja con la tabla y el gráfico"],
        ["olvidar un número que no salió", "total distinto de 12"],
        "Pregunta: «¿cuál número salió más y cuántas veces?». Debe responder el tres, cuatro veces."),
    reinforce="Escribe una lista de 10 resultados de dado de ejemplo y arma su tabla.",
    extend="Explica por qué dos grupos que lanzan el mismo dado 30 veces pueden obtener tablas distintas.",
)

# ===================================================== OAD-14 clase 8
F = ("Datos de ejemplo. Un puesto de feria anotó con marcas la cantidad de clientes por hora: "
     "16:00 → IIIII IIII. 17:00 → IIIII IIIII IIII. 18:00 → IIIII IIIII II. 19:00 → IIIII. "
     "El gráfico de barras tiene escala de 2 en 2, del 0 al 16.")
build(
    O14, 8, F,
    use="Voy a repasar cómo ir de las marcas a la tabla y al gráfico, y a explicar cada paso con mis palabras.",
    prior=["Sé contar con marcas.", "Sé armar tablas de frecuencia.", "Sé dibujar y leer gráficos de barras."],
    explain=[
        "Hoy conectas todo lo aprendido. Se parte de los datos o de las marcas de recuento. Se cuenta cada categoría y se arma la tabla de frecuencia. Luego, cada fila de la tabla se dibuja como una barra cuya altura es la frecuencia.",
        "Se puede volver atrás: del gráfico se lee la altura de cada barra y se arma la tabla, y de la tabla se puede escribir de nuevo en marcas. Los tres modos muestran la misma información. Lo que debe coincidir siempre es el total de datos.",
        "Para explicarlo a otra persona, di qué se contó, cuál categoría tuvo más y menos, y cuánto suman todas. Si usaste un sorteo con moneda o dado, di solo lo que pasó, no lo que pasará. Revisa qué parte ya dominas y cuál quieres practicar.",
    ],
    vocab=[("marcas de recuento", "rayitas agrupadas de cinco que cuentan datos"), ("tabla de frecuencia", "tabla de categorías y sus frecuencias"), ("gráfico de barras", "dibujo de barras con alturas de frecuencia"), ("total", "suma de todas las frecuencias"), ("sorteo", "decisión con ayuda del azar"), ("revisar", "comprobar que todo esté correcto")],
    worked=[
        ("De marcas a número", "En la ficha, ¿cuántos clientes hubo a las 17:00?", ["Hay dos grupos de cinco y cuatro sueltas.", "Suma: 5 + 5 + 4 = 14."], "14 clientes"),
        ("Escribir de nuevo en marcas", "Anota 12 con marcas.", ["Dibuja dos grupos de cinco: IIIII IIIII.", "Agrega dos sueltas: II."], "IIIII IIIII II")
    ],
    mistakes=[("Hacer la barra de las 19:00 más alta que la de las 18:00.", "Se mira el orden de las horas y no la frecuencia.", "Compara las frecuencias: 5 contra 12."),
              ("Decir que un sorteo con dado repetido dará siempre lo mismo.", "Se confunde lo que pasó con lo que pasará.", "Di que las frecuencias pueden cambiar en cada repetición.")],
    T=[
        ("=", "{F} ¿Cuántos clientes hubo a las 16:00?", "5+4", "Un grupo de cinco más cuatro sueltas.", " clientes"),
        ("=", "{F} ¿Cuántos clientes hubo a las 17:00?", "5+5+4", "Dos grupos de cinco más cuatro sueltas.", " clientes"),
        ("=", "{F} ¿Cuántos clientes hubo a las 18:00?", "5+5+2", "Dos grupos de cinco más dos sueltas.", " clientes"),
        ("=", "{F} ¿Cuántos clientes hubo en total entre las 16:00 y las 19:00?", "9+14+12+5", "Se suman las frecuencias de las cuatro horas.", " clientes"),
        ("abc", "{F} ¿A qué hora hubo más clientes?", "17:00", "16:00", "19:00", "Catorce clientes es la mayor frecuencia."),
        ("=", "{F} ¿Cuántos clientes más hubo a las 17:00 que a las 19:00?", "14-5", "Se resta la frecuencia menor de la mayor.", " clientes"),
        ("ab", "{F} La barra de las 19:00 (5 clientes) queda", "entre las marcas 4 y 6, a mitad de camino", "sobre la marca 6", "Cinco está justo entre cuatro y seis."),
        ("=", "{F} ¿Cuántos clientes hubo a las 18:00 y a las 19:00?", "12+5", "Se suman las dos frecuencias.", " clientes"),
        ("abc", "¿Qué marcas anotan el número 12?", "IIIII IIIII II", "IIIII IIIII I", "IIII IIII IIII", "Dos grupos de cinco y dos sueltas dan doce."),
        ("abc", "¿Qué debe ser igual en las marcas, en la tabla y en el gráfico?", "El total de datos", "El color", "El ancho de las barras", "Los tres modos muestran la misma información, con el mismo total."),
        ("=", "{F} ¿Cuántos clientes NO llegaron a las 17:00?", "40-14", "Se resta del total la frecuencia de las 17:00.", " clientes"),
        ("ab", "Una persona lanzó una moneda 10 veces y salieron 7 caras. ¿Cuántos sellos salieron?", "3 sellos", "7 sellos", "Diez lanzamientos menos siete caras da tres sellos."),
        ("abc", "{F} ¿Qué parte del dato 19:00 → IIIII muestra que hubo cinco clientes?", "El grupo cerrado de cinco rayitas", "La hora 19:00", "Las dos rayitas sueltas", "Un grupo cerrado equivale a cinco datos."),
    ],
    ctx=("=", "El dueño de un puesto de feria de ejemplo sabe que a las 16:00 hubo 9 clientes y a las 17:00 hubo 14. Quiere pedir cajas para el total de esas dos horas. ¿Para cuántos clientes calcula?", "9+14", "Se suman las dos frecuencias.", " clientes"),
    sc=[("¿Cuál es el camino de los datos al gráfico?", "Marcas, tabla y barras", "Primero se cuenta, luego se ordena y al final se dibuja."),
        ("¿Qué se puede afirmar de un sorteo ya hecho?", "Lo que pasó, no lo que pasará", "Los datos solo muestran los resultados observados."),
        ("¿Cómo compruebas que no te falta ningún dato?", "Sumo las frecuencias y comparo con el total", "Si coincide, no falta ni sobra ningún dato.")],
    op=("Recorre el camino completo con estos datos de ejemplo de un reparto de volantes: Lunes 8, Martes 13, Miércoles 10. Escribe las marcas, la tabla y el gráfico de barras con escala de 2 en 2, y explica en dos frases qué viste.",
        "Marcas: IIIII III; IIIII IIIII III; IIIII IIIII. Tabla: 8, 13, 10; total 31. Barras de alturas 8, 13 (entre 12 y 14) y 10. Frase: «El martes se repartieron más volantes, 13, y el lunes menos, 8».",
        ["marcas correctas", "tabla con total 31", "gráfico coherente y frase correcta"],
        ["hoja con marcas, tabla, gráfico y frases"],
        ["datos que cambian entre marcas, tabla y gráfico", "total mal sumado"],
        "Pregunta: «¿qué parte te resultó más fácil y cuál quieres repasar?». Anotarlo ayuda a elegir qué practicar."),
    reinforce="Escribe 9 con marcas, tabla de una fila y una barra, y explica que dicen lo mismo.",
    extend="Explica con tus palabras qué se puede decir y qué no de un dado que se lanzó muchas veces.",
)
