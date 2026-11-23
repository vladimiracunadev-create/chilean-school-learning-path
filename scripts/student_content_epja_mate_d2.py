"""Matemática EPJA Nivel 1 básico, módulo 4: OAD-13 clases 5 a 8 (escalas, describir una población, explicar y revisar). Datos de ejemplo, inventados; todo en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Hoja, lápiz de mina y regla. Todo se hace en papel; los gráficos de este cuaderno se dibujan con cuadros ■ y tablas. Todos los datos son de ejemplo, inventados."
build = make_build(MATERIALS)

O13 = "EPJA-MATE-NB1-OAD-13"

# ===================================================== OAD-13 clase 5
F = ("Datos de ejemplo. Gráfico de barras: «Cajas de verdura vendidas por semana en una feria». La escala sube de 5 en 5: 0, 5, 10, 15… "
     "Semana 1: 20 cajas. Semana 2: 35. Semana 3: 30. Semana 4: 45.")
build(
    O13, 5, F,
    use="Voy a leer gráficos de barras con escala de 2 en 2, de 5 en 5 y de 10 en 10.",
    prior=["Sé leer un gráfico de barras con escala de 1 en 1.", "Sé contar de 5 en 5.", "Sé multiplicar por 5 y por 10 contando de a saltos."],
    explain=[
        "No siempre la escala sube de uno en uno. Cuando los datos son grandes, la escala puede subir de 2 en 2, de 5 en 5 o de 10 en 10. Así el gráfico cabe en la hoja. Lo primero es mirar de cuánto en cuánto sube la escala.",
        "Para saber de cuánto sube, mira dos marcas seguidas y resta. Si ves 0, 5, 10, 15, sube de 5 en 5. Para leer una barra, cuenta las marcas con saltos: 5, 10, 15, 20. También puedes multiplicar el número de marcas por el valor del salto.",
        "Si la barra queda justo en una marca, lees ese número. Esto es parecido a contar billetes de a $5.000 o a $10.000: no cuentas de uno en uno, cuentas por saltos. Leer la escala con cuidado evita errores grandes.",
    ],
    vocab=[("escala", "números que sirven para leer las barras"), ("salto", "lo que sube la escala entre una marca y la siguiente"), ("marca", "rayita de la escala"), ("de 5 en 5", "5, 10, 15, 20, así sigue"), ("multiplicar", "repetir una cantidad varias veces"), ("leer", "hallar el número de una barra")],
    worked=[
        ("Hallar el salto", "La escala dice 0, 5, 10, 15. ¿De cuánto en cuánto sube?", ["Resta dos marcas seguidas: 10 − 5 = 5.", "Revisa con otra pareja: 15 − 10 = 5."], "De 5 en 5"),
        ("Leer una barra", "En la ficha, la barra de la semana 3 termina en la sexta marca contada desde el cero. ¿Cuántas cajas son?", ["Cada marca vale 5.", "Cuenta de 5 en 5 seis veces: 5, 10, 15, 20, 25, 30."], "30 cajas"),
    ],
    mistakes=[("Leer 6 cuando la barra llega a la sexta marca de una escala de 5 en 5.", "Se cuentan las marcas como si valieran uno.", "Multiplica el número de marcas por el salto: 6 × 5 = 30."),
              ("Suponer que toda escala sube de uno en uno.", "No se mira cómo cambian los números de la escala.", "Siempre resta dos marcas seguidas antes de leer.")],
    T=[
        ("abc", "{F} ¿De cuánto en cuánto sube la escala?", "De 5 en 5", "De 1 en 1", "De 10 en 10", "Los números 0, 5, 10, 15 suben de a cinco."),
        ("{F} ¿Cuántas cajas se vendieron la semana 2?", "35 cajas", "La ficha dice que la barra de la semana 2 llega a la marca 35."),
        ("abc", "La escala dice 0, 5, 10, 15. ¿Qué número viene después?", "20", "16", "25", "Se suman cinco al 15 y da 20, siguiendo el salto."),
        ("=", "{F} ¿Cuántas cajas se vendieron en las cuatro semanas?", "20+35+30+45", "Se suman las alturas de las cuatro barras.", " cajas"),
        ("abc", "{F} ¿Qué semana vendió más cajas?", "Semana 4", "Semana 1", "Semana 3", "La barra más alta es la de 45 cajas, que corresponde a la semana 4."),
        ("=", "{F} ¿Cuántas cajas más se vendieron en la semana 4 que en la semana 1?", "45-20", "Se resta la barra menor de la mayor.", " cajas"),
        ("ab", "{F} La barra de la semana 3 llega a la marca", "30", "6", "Cada marca vale cinco y la barra llega a la sexta marca, por eso 30."),
        ("=", "{F} ¿Cuántas cajas más se vendieron la semana 4 que la semana 3?", "45-30", "Se comparan dos barras restando sus datos.", " cajas"),
        ("abc", "Una persona cuenta 6 marcas en una escala de 5 en 5 y dice «6 cajas». ¿Qué corrige?", "Cada marca vale 5, así que son 30", "Hay que sumar 6 más 5, son 11", "Nada, 6 está bien", "Con saltos de cinco, seis marcas valen 6 × 5, es decir 30."),
        ("=", "Una barra llega a la sexta marca en una escala que sube de 5 en 5. ¿Cuántas unidades representa?", "6*5", "Se multiplica el número de marcas por el salto.", " unidades"),
        ("=", "{F} Si la semana 1 aumenta 10 cajas más, ¿cuántas cajas habría?", "20+10", "Se suma el aumento al dato de la semana 1.", " cajas"),
        ("=", "Una escala sube de 2 en 2 y una barra llega a la quinta marca. ¿Qué valor tiene?", "5*2", "Cinco marcas de dos en dos son diez.", ""),
        ("ab", "Una escala sube de 10 en 10 y una barra llega a 50. ¿Cuántas marcas hay desde el cero?", "5 marcas", "50 marcas", "Cada marca vale diez, así que 50 corresponde a cinco marcas."),
    ],
    ctx=("=", "Un feriante de ejemplo mira su gráfico, de 5 en 5: vendió 35 cajas la semana 2 y 30 la semana 3. Necesita el total de esas dos semanas para pagar al proveedor. ¿Cuántas cajas son?", "35+30", "Se suman las dos barras.", " cajas"),
    sc=[("¿Cómo averiguas de cuánto en cuánto sube la escala?", "Resto dos marcas seguidas", "La diferencia entre dos marcas seguidas es el salto de la escala."),
        ("En una escala de 5 en 5, ¿qué número va después de 25?", "30", "Se suman cinco al 25 y resulta 30."),
        ("En una escala de 10 en 10, ¿qué valor tiene la tercera marca?", "30", "Tres marcas de diez en diez dan treinta.")],
    op=("Dibuja las barras para estos datos de ejemplo, con escala de 10 en 10 del 0 al 60: Enero 30 pedidos, Febrero 50 pedidos, Marzo 40 pedidos. Escribe título y rótulos.",
        "Título «Pedidos por mes»; barras de alturas 30, 50 y 40 sobre una escala 0, 10, 20, 30, 40, 50, 60; ejes rotulados «Meses» y «Pedidos».",
        ["escala de 10 en 10 bien escrita", "alturas 30, 50 y 40", "título y rótulos"],
        ["hoja con el gráfico"],
        ["escribir la escala de 1 en 1", "alturas que no coinciden con los datos"],
        "Pregunta: «¿cuántas marcas sube la barra de febrero?». Debe responder cinco marcas, de diez en diez."),
    reinforce="Escribe la escala de 5 en 5 hasta 50 y la escala de 2 en 2 hasta 20.",
    extend="Explica cuándo conviene usar una escala de 10 en 10 en vez de una de 1 en 1.",
)

# ===================================================== OAD-13 clase 6
F = ("Datos de ejemplo. Una junta de vecinos preguntó por el tipo de vivienda a las 40 familias de un pasaje (población: las 40 familias). "
     "Gráfico de barras, escala de 2 en 2: Casa 18, Departamento 12, Pieza arrendada 6, Otra 4.")
build(
    O13, 6, F,
    use="Voy a describir un grupo de personas, llamado población, usando un gráfico de barras.",
    prior=["Sé leer un gráfico de barras.", "Sé comparar cantidades.", "Sé sumar y restar números de dos cifras."],
    explain=[
        "Una población es el grupo completo del que hablan los datos: las 40 familias de un pasaje, los 20 trabajadores de una cuadrilla. Un gráfico de barras sirve para describir sus características, por ejemplo qué tipo de vivienda tiene cada familia.",
        "Para describir una población con un gráfico, di cuántos elementos hay en total, cuál categoría es la mayor, cuál es la menor y cuánto suman algunas categorías juntas. Usa siempre números: «18 de 40 familias viven en casa». Evita opiniones que el gráfico no muestra.",
        "El total de la población es la suma de todas las barras. Si la suma no da el total que dice la ficha, hay un error. El conocimiento que tienes de tu barrio es útil. El gráfico pone ese saber en números.",
    ],
    vocab=[("población", "grupo completo del que hablan los datos"), ("característica", "rasgo que se puede observar, como el tipo de vivienda"), ("mayoría", "la categoría con más elementos"), ("total", "suma de todas las barras"), ("describir", "decir cómo es algo, con números"), ("junta de vecinos", "grupo que organiza la vida de un barrio")],
    worked=[
        ("Verificar el total", "En la ficha, ¿suman las barras las 40 familias?", ["Suma: 18 + 12 = 30; 30 + 6 = 36; 36 + 4 = 40.", "El total coincide con las 40 familias."], "Sí, suman 40"),
        ("Describir con números", "Escribe una frase sobre la categoría mayor.", ["La barra más alta es Casa, con 18.", "Frase: «18 de las 40 familias viven en casa»."], "18 de 40 familias viven en casa"),
    ],
    mistakes=[("Escribir «a todos les gusta vivir en casa».", "Se agrega una opinión que el gráfico no muestra.", "Describe solo lo que muestran las barras: cuántas familias viven en casa."),
              ("Describir solo la barra más alta y olvidar el total.", "Se piensa que con una barra basta.", "Menciona también el total de la población y la categoría menor.")],
    T=[
        ("{F} ¿Cuántas familias viven en casa?", "18 familias", "La barra de Casa llega a 18 en la escala."),
        ("abc", "{F} ¿Qué tipo de vivienda es el más frecuente?", "Casa", "Departamento", "Otra", "La barra de Casa es la más alta de las cuatro."),
        ("abc", "{F} ¿Qué tipo de vivienda es el menos frecuente?", "Otra", "Pieza arrendada", "Casa", "La barra más baja es la de Otra, con 4 familias."),
        ("=", "{F} ¿Cuántas familias hay en total en la población?", "18+12+6+4", "Se suman todas las barras.", " familias"),
        ("=", "{F} ¿Cuántas familias más viven en casa que en departamento?", "18-12", "Se resta el dato menor del mayor.", " familias"),
        ("abc", "{F} ¿Cuántos tipos de vivienda se compararon?", "4", "40", "18", "El gráfico tiene cuatro barras, una por cada tipo de vivienda."),
        ("=", "{F} ¿Cuántas familias viven en casa o en departamento?", "18+12", "Se suman las dos barras pedidas.", " familias"),
        ("ab", "{F} ¿Vive más de la mitad de las familias en casa?", "No: la mitad de 40 es 20 y en casa viven 18", "Sí: casa es la barra más alta", "La mitad de 40 es 20, y 18 no alcanza esa cantidad."),
        ("=", "{F} ¿Cuántas familias NO viven en casa?", "12+6+4", "Se suman todas las barras menos la de casa.", " familias"),
        ("abc", "{F} ¿Qué frase describe bien el gráfico?", "Casi la mitad de las familias vive en casa: 18 de 40", "Todas las familias viven en casa", "Muy pocas familias viven en casa", "Dieciocho de cuarenta es casi la mitad, y es lo que muestra la barra."),
        ("=", "{F} ¿Cuántas familias más viven en departamento que en pieza arrendada?", "12-6", "Se comparan dos barras restando.", " familias"),
        ("=", "{F} Llegan 3 familias nuevas que arriendan pieza. ¿Cuántas habrá en esa barra?", "6+3", "Se suman las familias nuevas a la barra.", " familias"),
        ("ab", "{F} ¿Qué frase es verdadera?", "Hay el triple de familias en casa que en pieza arrendada", "Hay el doble de familias en casa que en pieza arrendada", "Seis multiplicado por tres es dieciocho, así que casa es el triple."),
    ],
    ctx=("=", "La presidenta de una junta de vecinos de ejemplo quiere pedir material para 40 familias. Si 18 viven en casa y 12 en departamento, ¿para cuántas familias pedirá un tipo de material de casas o de departamentos?", "18+12", "Se suman las barras de casas y departamentos.", " familias"),
    sc=[("¿Qué es la población en un gráfico?", "El grupo completo del que hablan los datos", "La población es el conjunto de personas o cosas medidas."),
        ("¿Cómo compruebas que no falta ninguna familia en el gráfico?", "Sumo las barras y comparo con el total", "Si la suma coincide con el total, no falta ningún dato."),
        ("Di una frase correcta sobre la barra más baja de la ficha.", "Solo 4 de las 40 familias tienen otro tipo de vivienda", "Se usa el dato exacto de la barra.")],
    op=("Describe esta población de ejemplo con tres frases: 30 personas de un curso nocturno. Edad en tramos: 18 a 25 años: 12 personas; 26 a 40 años: 10; 41 años o más: 8. Dibuja las barras, escala de 2 en 2.",
        "«El grupo tiene 30 personas. El tramo más frecuente es de 18 a 25 años, con 12. El menos frecuente es de 41 años o más, con 8.» Barras de alturas 12, 10 y 8.",
        ["dibuja las barras con alturas 12, 10 y 8", "menciona el total 30", "nombra el mayor y el menor con sus números"],
        ["hoja con el gráfico y tres frases"],
        ["no decir el total", "agregar opiniones que el gráfico no muestra"],
        "Pregunta: «¿cuánto suman las tres barras?». Si no da 30, pídele revisar."),
    reinforce="Describe con tres frases el gráfico de la ficha, sin usar la palabra «casa».",
    extend="Explica por qué un gráfico de una población pequeña no sirve para hablar de todo un país.",
)

# ===================================================== OAD-13 clase 7
F = ("Datos de ejemplo. Gráfico de barras, escala de 2 en 2: «Personas inscritas en un taller de oficios». Costura 14, Panadería 18, Electricidad 10, Soldadura 8. "
     "Una persona debe explicarlo a otra con sus palabras.")
build(
    O13, 7, F,
    use="Voy a explicar con mis palabras qué muestra un gráfico de barras a otra persona.",
    prior=["Sé las partes de un gráfico de barras.", "Sé comparar datos.", "Sé decir un número en voz alta."],
    explain=[
        "Explicar un gráfico es contarle a otra persona qué dice, sin mostrar solo el dibujo. Sigue tres pasos. Primero, di de qué trata: lee el título. Segundo, di el dato mayor y el menor con sus números. Tercero, di algo que se saca de comparar, por ejemplo cuántos más hay en una barra que en otra.",
        "Usa frases cortas y números exactos: «En Panadería hay 18 personas, 4 más que en Costura». No digas «hay muchos» si puedes decir cuántos. También conviene decir qué muestra el eje de abajo y qué mide el de arriba, para que la otra persona no se pierda.",
        "Una buena explicación solo dice lo que está en el gráfico. Si piensas por qué hay más gente en un taller, es una idea tuya y debes decirla como idea, no como dato. Explicar con claridad también ayuda cuando muestras información en una reunión o un trámite.",
    ],
    vocab=[("explicar", "contar algo para que otra persona lo entienda"), ("conclusión", "idea que se saca de comparar los datos"), ("dato", "número o hecho que muestra el gráfico"), ("comparar", "ver cuál es mayor o menor"), ("oficio", "trabajo que se aprende y se practica con las manos"), ("inscrito", "anotado para participar")],
    worked=[
        ("Armar la explicación", "Explica en dos frases la ficha, sin repetir el título.", ["Di el mayor con su número: Panadería, 18.", "Di el menor con su número: Soldadura, 8."], "«Panadería tiene más personas, 18. Soldadura tiene menos, 8»."),
        ("Agregar una comparación", "¿Cuántas personas más hay en Panadería que en Soldadura?", ["Resta 18 − 8.", "Escribe la frase con el resultado."], "10 personas más"),
    ],
    mistakes=[("Decir «hay muchos en Panadería» sin dar el número.", "Se piensa que con eso se entiende.", "Agrega siempre el número que muestra la barra: 18."),
              ("Mezclar lo que dice el gráfico con una opinión, como «Panadería es el mejor taller».", "El gráfico muestra cantidad de inscritos, no calidad.", "Di la opinión aparte y marcada como tuya.")],
    T=[
        ("abc", "¿Qué se dice primero al explicar un gráfico?", "De qué trata, leyendo el título", "Cuál es mi taller favorito", "Cuántos colores tiene", "Primero se ubica el tema para que la otra persona se oriente."),
        ("{F} ¿Qué taller tiene más personas?", "Panadería, con 18 personas", "La barra más alta es la de Panadería, que llega a 18."),
        ("=", "{F} ¿Cuántas personas hay inscritas en total en los cuatro talleres?", "14+18+10+8", "Se suman las cuatro barras.", " personas"),
        ("abc", "{F} ¿Qué frase explica bien el gráfico?", "Panadería tiene 18 personas, la barra más alta", "Soldadura es la barra más alta", "Costura tiene 10 personas", "La frase correcta nombra el taller y su número exacto."),
        ("=", "{F} ¿Cuántas personas más hay en Panadería que en Soldadura?", "18-8", "Se resta el dato menor del mayor.", " personas"),
        ("ab", "{F} ¿Cuál es una explicación basada en los datos?", "Hay más personas en Panadería que en Costura: 18 y 14", "Panadería es mejor taller que Costura", "El gráfico muestra cantidades de personas, no si un taller es mejor."),
        ("=", "{F} ¿Cuántas personas hay entre Costura y Electricidad juntas?", "14+10", "Se suman las dos barras nombradas.", " personas"),
        ("abc", "Alguien dice: «Panadería es la más alta». ¿Qué le agregas para explicar mejor?", "El valor: 18 personas", "Mi opinión sobre el pan", "El color de la barra", "Una explicación completa incluye el número exacto de la barra."),
        ("=", "{F} ¿Cuántas personas más hay en Panadería que en Costura?", "18-14", "Se comparan dos barras restando.", " personas"),
        ("abc", "{F} Una persona dice: «Electricidad tiene más inscritos que Costura». ¿Es correcto?", "No: Electricidad tiene 10 y Costura 14", "Sí: tiene la barra más alta", "Sí: están igual de altas", "Diez es menor que catorce, así que Electricidad tiene menos."),
        ("=", "{F} Si Soldadura duplicara sus inscritos, ¿cuántos tendría?", "8*2", "Duplicar es multiplicar por dos.", " personas"),
        ("=", "{F} ¿Cuántas personas NO están en Panadería?", "14+10+8", "Se suman todas las barras menos la de Panadería.", " personas"),
        ("ab", "{F} ¿Qué conclusión se puede sacar de los datos?", "Costura tiene más inscritos que Electricidad", "A todas las personas les gusta el pan", "Solo se puede afirmar lo que muestran las barras: 14 es mayor que 10."),
    ],
    ctx=("=", "Una encargada de un taller de ejemplo debe explicar a su jefa cuántas personas hay en Costura y Soldadura juntas, para ordenar sillas. Costura tiene 14 y Soldadura 8. ¿Cuántas sillas necesita?", "14+8", "Se suman las dos barras para saber el total de sillas.", " sillas"),
    sc=[("¿Qué tres cosas dices al explicar un gráfico?", "De qué trata, el mayor y el menor, y una comparación con números", "Esos pasos ordenan la explicación y la hacen clara."),
        ("¿Por qué conviene decir el número exacto?", "Porque evita decir «muchos» o «pocos», que no son claros", "El número deja la información precisa y comprobable."),
        ("¿Se puede decir por qué un taller tiene más gente si el gráfico no lo muestra?", "No como dato; solo como una idea aparte", "El gráfico solo muestra cantidades, no las razones.")],
    op=("Explica en voz alta, o por escrito, este gráfico de ejemplo a otra persona: Reciclaje semanal en un edificio, en kilos: Vidrio 12, Cartón 18, Plástico 14, Latas 6. Usa los tres pasos: de qué trata, mayor y menor, una comparación.",
        "«El gráfico muestra kilos reciclados por semana. Cartón es lo que más se recicla, 18 kilos, y Latas lo que menos, 6. Hay 12 kilos más de cartón que de latas.»",
        ["dice de qué trata", "nombra el mayor y el menor con sus números", "hace una comparación correcta"],
        ["frases escritas o explicación oral escuchada por otra persona"],
        ["omitir los números", "agregar opiniones como si fueran datos"],
        "Pregunta a quien escucha: «¿entendiste de qué trata y cuál es el mayor?». Si no, pide repetir los pasos."),
    reinforce="Escribe dos frases con números sobre cualquier gráfico de la ficha de esta clase.",
    extend="Explica la diferencia entre un dato y una opinión con un ejemplo de tu barrio.",
)

# ===================================================== OAD-13 clase 8
F = ("Datos de ejemplo. Un centro vecinal registró las atenciones de su oficina de trámites. Cada ■ vale 2 atenciones. "
     "Lunes: ■■■■■■. Martes: ■■■■. Miércoles: ■■■■■. Jueves: ■■■■■■■. Para el gráfico de barras se usa una escala de 2 en 2.")
build(
    O13, 8, F,
    use="Voy a repasar todo el módulo de gráficos de barras: pasar de cuadros a barras, leer, construir y describir.",
    prior=["Sé leer cuadros y barras.", "Sé leer escalas de 2 en 2 y de 5 en 5.", "Sé describir con números."],
    explain=[
        "Hoy repasas lo aprendido. Un gráfico de cuadros usa cuadros iguales; cada cuadro puede valer 1, 2 u otro número, y eso siempre se dice. Para pasar a barras, multiplica el número de cuadros por lo que vale cada uno y dibuja la barra hasta esa altura.",
        "Un gráfico de barras completo tiene título, eje de las categorías, eje con la escala y rótulos. La escala parte en cero y sube con saltos iguales. Para leer una barra, baja desde su punta hasta la escala. Para describir una población, di el total, el mayor, el menor y una comparación con números.",
        "Revisa tu trabajo con tres preguntas: ¿cada barra coincide con su dato?, ¿la escala parte en cero y sube parejo?, ¿escribí título y rótulos? Si algo falla, corrige. Reconocer qué ya dominas y qué quieres repasar es parte del aprendizaje.",
    ],
    vocab=[("valor del cuadro", "cantidad que representa cada cuadro"), ("barra", "rectángulo cuya altura muestra una cantidad"), ("escala", "números para leer la altura"), ("rótulo", "palabra que explica qué mide cada eje"), ("población", "grupo del que hablan los datos"), ("revisar", "comprobar que algo está bien")],
    worked=[
        ("Cuadros con valor 2", "En la ficha, el lunes tiene 6 cuadros y cada uno vale 2. ¿Cuántas atenciones hubo?", ["Multiplica 6 × 2.", "Eso da 12 atenciones, y la barra del lunes sube a 12."], "12 atenciones"),
        ("Elegir la escala", "El jueves tiene 7 cuadros de valor 2. ¿Hasta dónde debe llegar la escala?", ["Calcula 7 × 2 = 14.", "La escala debe llegar al menos a 14."], "Al menos hasta 14"),
    ],
    mistakes=[("Dibujar la barra del martes hasta 4, que es el número de cuadros.", "Se olvida que cada cuadro vale 2.", "Multiplica los cuadros por su valor: 4 × 2 = 8."),
              ("Dejar el gráfico sin título ni rótulos.", "Se piensa que las barras hablan solas.", "Antes de entregar, revisa título y rótulos de los dos ejes.")],
    T=[
        ("abc", "{F} ¿Cuánto vale cada cuadro?", "2 atenciones", "1 atención", "7 atenciones", "La ficha dice que cada cuadro vale dos atenciones."),
        ("=", "{F} ¿Cuántas atenciones hubo el lunes?", "6*2", "Se multiplica el número de cuadros por su valor.", " atenciones"),
        ("=", "{F} ¿Cuántas atenciones hubo el martes?", "4*2", "Cuatro cuadros de valor dos son ocho.", " atenciones"),
        ("abc", "{F} ¿Qué día tuvo la barra más alta?", "Jueves", "Martes", "Lunes", "El jueves tiene siete cuadros, el mayor número, y llega a 14."),
        ("=", "{F} ¿Cuántas atenciones hubo en total en los cuatro días?", "12+8+10+14", "Se suman las alturas de las cuatro barras.", " atenciones"),
        ("=", "{F} ¿Cuántas atenciones más hubo el jueves que el martes?", "14-8", "Se resta el dato menor del mayor.", " atenciones"),
        ("abc", "{F} ¿Hasta qué número sube la barra del miércoles?", "10", "5", "14", "Cinco cuadros de valor dos hacen diez, y la barra llega a 10."),
        ("{F} ¿Qué día tuvo menos atenciones?", "Martes, con 8 atenciones", "La barra más baja es la del martes, con cuatro cuadros de valor dos."),
        ("=", "{F} ¿Cuántos cuadros hay en total en el gráfico de cuadros?", "6+4+5+7", "Se suman los cuadros de las cuatro filas.", " cuadros"),
        ("ab", "Si cada cuadro valiera 3, el lunes con 6 cuadros tendría", "18 atenciones", "12 atenciones", "Seis cuadros de valor tres son 6 × 3, es decir 18."),
        ("=", "{F} ¿Cuántas atenciones hubo el miércoles y el jueves juntos?", "10+14", "Se suman las dos barras.", " atenciones"),
        ("abc", "Alguien dibuja la barra del martes en 4. ¿Qué error cometió?", "Contó los cuadros sin multiplicar por 2", "Usó la escala de 5 en 5", "Olvidó el título", "El valor del cuadro es 2, así que la barra debe llegar a 8."),
        ("ab", "{F} Para dibujar todas las barras, la escala debe llegar al menos a", "14", "7", "La barra más alta es la del jueves, que mide 14 atenciones."),
    ],
    ctx=("=", "La coordinadora de un centro vecinal de ejemplo quiere saber cuántas atenciones hubo de lunes a miércoles para un informe. Lunes 12, martes 8 y miércoles 10. ¿Cuántas fueron?", "12+8+10", "Se suman las tres barras de la semana.", " atenciones"),
    sc=[("¿Qué haces si cada cuadro vale 2?", "Multiplico los cuadros por 2 para hallar la cantidad", "El valor del cuadro cambia la cantidad que representa cada fila."),
        ("¿Qué partes debe tener un gráfico de barras completo?", "Título, dos ejes con rótulos, escala y barras", "Esas partes permiten leerlo sin confundirse."),
        ("¿Cómo revisas que una barra está bien dibujada?", "Comparo su altura con el dato de la tabla", "Si no coinciden, hay un error por corregir.")],
    op=("Haz un gráfico de barras con estos datos de ejemplo de una panadería: Pan corriente 16 kilos, Pan integral 8, Pan de molde 12. Cada ■ vale 4 kilos: primero dibuja los cuadros y luego las barras con escala de 4 en 4.",
        "Cuadros: ■■■■ (16), ■■ (8), ■■■ (12). Barras de alturas 16, 8 y 12 sobre una escala 0, 4, 8, 12, 16, 20; título «Kilos de pan vendidos por tipo»; ejes rotulados.",
        ["cuadros bien contados con su valor", "barras con las alturas correctas", "título, rótulos y escala completos"],
        ["hoja con cuadros, barras y escala"],
        ["no usar el valor del cuadro", "olvidar rótulos"],
        "Pregunta: «¿qué parte de este módulo dominas y cuál quieres repasar?». Anotarla ayuda a decidir qué practicar."),
    reinforce="Rehace la barra del jueves de la ficha, escribiendo cuántos cuadros y cuánto vale cada uno.",
    extend="Explica cómo cambiaría la escala si cada cuadro valiera 10 y el mayor tuviera 7 cuadros.",
)
