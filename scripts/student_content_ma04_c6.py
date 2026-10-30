"""Student material for 4.º básico Matemática, OA 27 (pictogramas y gráficos de barra simple con escala)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA27 = "MA04 OA 27"

LIBROS = "Gráfico de barras «Libros leídos en octubre». Eje horizontal: Ana, Beto, Carla y Dani. Eje vertical: cantidad de libros, con marcas de 5 en 5 desde 0 hasta 25. La barra de Ana llega a la marca 15, la de Beto a la 10, la de Carla a la 25 y la de Dani a la 20."
PELOTAS = "Pictograma «Pelotas prestadas en el recreo». Cada ● vale 2 pelotas. Lunes ●●●; martes ●●●●●; miércoles ●●; jueves ●●●●."
FRUTAS = "Gráfico de barras «Frutas vendidas en una feria». Eje vertical: cantidad de kilos, con marcas de 10 en 10 desde 0 hasta 50. Manzana: la barra llega a la marca 40. Pera: llega justo a la mitad entre la marca 20 y la 30. Naranja: llega justo a la mitad entre la marca 30 y la 40. Plátano: llega a la marca 50. Uva: llega justo a la mitad entre la marca 10 y la 20."
PAN = "Pictograma «Panes vendidos». Cada ● vale 10 panes y cada ◐ vale 5 panes. Lunes ●●●◐; martes ●●; miércoles ●●●●; jueves ●◐."
DEPORTES = "Gráfico de barras «Deporte favorito del curso». Eje vertical: cantidad de estudiantes, con marcas de 3 en 3 desde 0 hasta 18. Fútbol llega a la marca 18, natación a la 12, básquetbol a la 15 y tenis a la 9."
MASC = "Gráfico de barras «Mascota favorita de un curso». Eje vertical: cantidad de estudiantes, con marcas de 2 en 2 desde 0 hasta 12. Perro llega a la marca 12, gato a la 8, pez a la 4 y ave a la 2."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA27, 1,
    materials="Lápiz y papel. Los gráficos están descritos con palabras y números dentro de cada ejercicio; con papel cuadriculado puedes dibujarlos.",
    use="Aprenderé a leer el título, los ejes y la escala de un gráfico de barras y de un pictograma. Sirve para entender qué cuenta el gráfico antes de sacar datos.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10.", "Sé qué es una tabla de conteo."],
    explain=[
        "Un gráfico de barras muestra datos con barras de distinta altura. Lo primero que se lee es el título, que dice de qué trata. Luego se leen los ejes: en el eje horizontal suelen ir las categorías, como nombres, y en el vertical la cantidad.",
        "La escala dice cuánto vale cada marca del eje vertical. Si las marcas suben de 5 en 5, una barra que llega a la marca 15 vale 15. Siempre hay que mirar de cuánto en cuánto sube la escala, porque cambia de gráfico a gráfico.",
        "Un pictograma usa símbolos en vez de barras. Un recuadro dice cuánto vale cada símbolo. Si cada ● vale 2 pelotas, cuatro ● valen 4 × 2 = 8 pelotas. Sin la clave del símbolo no se puede saber el valor.",
    ],
    vocab=[("título", "frase que dice de qué trata el gráfico"), ("eje", "línea del gráfico: horizontal para las categorías y vertical para las cantidades"), ("escala", "números del eje vertical que dicen cuánto vale cada marca"), ("pictograma", "gráfico con símbolos que representan una cantidad")],
    worked=[
        {"title": "Leer una barra con escala", "problem": LIBROS + " ¿Cuántos libros leyó Beto?", "steps": ["Miro la marca del eje vertical a la que llega la barra de Beto.", "Llega a la marca 10 y la escala es de 5 en 5."], "answer": "Beto leyó 10 libros"},
        {"title": "Leer un pictograma", "problem": PELOTAS + " ¿Cuántas pelotas se prestaron el martes?", "steps": ["El martes tiene 5 símbolos.", "Cada símbolo vale 2: 5 × 2 = 10."], "answer": "Se prestaron 10 pelotas"},
    ],
    mistakes=[
        {"wrong": "Leer una barra que llega a la tercera marca como 3, sin ver la escala.", "why": "Se cuenta la marca en vez de leer su valor.", "fix": "Si las marcas suben de 5 en 5, la tercera marca vale 15."},
        {"wrong": "Contar los símbolos de un pictograma como si cada uno valiera 1.", "why": "No se lee la clave que dice cuánto vale cada símbolo.", "fix": "Multiplica los símbolos por su valor: 5 × 2 = 10."},
    ],
    tiers={
        "recovery": [
            ex(LIBROS + " ¿Qué dice el título del gráfico?", "Libros leídos en octubre", "El título está entre comillas."),
            ex(LIBROS + " ¿De cuánto en cuánto sube la escala del eje vertical?", "De 5 en 5", "Las marcas son 0, 5, 10, 15, 20 y 25."),
            ex(PELOTAS + " ¿Cuánto vale cada ●?", "2 pelotas", "Está escrito en la clave del pictograma."),
        ],
        "understand": [
            ex(LIBROS + " ¿Qué se muestra en el eje horizontal?", "Los nombres Ana, Beto, Carla y Dani", "Son las categorías del gráfico."),
            ex(LIBROS + " ¿Cuántos libros leyó Carla?", "25", "Su barra llega a la marca 25."),
            ex(PELOTAS + " ¿Cuántos ● tiene el lunes?", "3", "Se cuentan tres símbolos."),
        ],
        "apply": [
            arith(PELOTAS + " ¿Cuántas pelotas se prestaron el lunes?", "3*2", "Se multiplican los símbolos por 2.", " pelotas"),
            arith(PELOTAS + " ¿Cuántas pelotas se prestaron el jueves?", "4*2", "Se multiplican los símbolos por 2.", " pelotas"),
            ex(LIBROS + " ¿Cuántos libros leyó Dani?", "20", "Su barra llega a la marca 20."),
        ],
        "reason": [
            ex("En un gráfico, la barra de Eva llega a la tercera marca y la escala sube de 10 en 10. Pía dice que Eva tiene 3. ¿Qué error hay y cuánto tiene?", "Contó la marca y no su valor; tiene 30", "3 × 10 = 30.", calc="3*10"),
            ex("En un pictograma sin clave, ¿se puede saber cuánto vale un símbolo? Explica.", "No; la clave dice el valor de cada símbolo", "Sin clave no hay manera de saber su valor."),
        ],
        "challenge": [
            ex(PELOTAS + " ¿Cuántas pelotas más se prestaron el martes que el miércoles?", "6", "Martes 10 y miércoles 4; 10 − 4 = 6.", calc="10-4"),
            ex(LIBROS + " ¿Cuántos libros leyeron Ana y Beto juntos?", "25", "15 + 10 = 25.", calc="15+10"),
        ],
    },
    context=[ex("En el colegio hicieron un pictograma «Botellas recicladas» donde cada ● vale 5 botellas. El curso A tiene 6 ● y el curso B tiene 4 ●. ¿Cuántas botellas recicló el curso A?", "30", "6 × 5 = 30.", calc="6*5")],
    selfcheck=[
        ex("¿Qué dice la escala de un gráfico?", "Cuánto vale cada marca del eje vertical", "Permite leer la cantidad de cada barra."),
        ex(LIBROS + " ¿Quién leyó menos libros?", "Beto", "Su barra es la más baja, con 10."),
        ex("En un pictograma donde cada ● vale 4, ¿cuánto valen 3 ●?", "12", "3 × 4 = 12.", calc="3*4"),
    ],
    open_task=task(
        "Usa este gráfico: " + LIBROS + " Escribe: el título, qué hay en cada eje, de cuánto en cuánto sube la escala y el valor de las cuatro barras. Después explica cómo leíste una barra.",
        "Título: Libros leídos en octubre. Eje horizontal: nombres. Eje vertical: libros, de 5 en 5. Ana 15, Beto 10, Carla 25 y Dani 20.",
        ["lee el título", "dice qué hay en los dos ejes", "dice la escala", "da el valor de las cuatro barras"],
        ["título", "ejes y escala", "cuatro valores"],
        ["leer marcas sin su valor", "olvidar la escala"],
        "Pide señalar con el dedo la marca a la que llega cada barra. Reconoce que use la escala.",
    ),
    reinforce="Busca un gráfico en un diario, libro o revista y lee su título y su escala.",
    extend="Dibuja un pictograma con 3 categorías y escribe la clave que dice cuánto vale cada símbolo.",
)

register(
    OA27, 2,
    materials="Lápiz y papel. Los gráficos están descritos con palabras y números en cada ejercicio.",
    use="Aprenderé a leer valores exactos aunque la barra quede entre dos marcas o el símbolo esté partido. Sirve para no leer números aproximados cuando se pide el dato exacto.",
    prior=["Sé leer el título, los ejes y la escala.", "Sé que la mitad de un número es dividirlo por 2."],
    explain=[
        "A veces una barra no llega justo a una marca, sino a la mitad entre dos marcas. Si las marcas suben de 10 en 10 y la barra llega a la mitad entre 20 y 30, su valor es 25. Se calcula la mitad de la distancia: 10 ÷ 2 = 5, y 20 + 5 = 25.",
        "En un pictograma, un símbolo partido vale la mitad. Si cada ● vale 10 y cada ◐ vale 5, entonces ●●● ◐ vale 3 × 10 + 5 = 35. Primero cuentas los símbolos enteros, y luego sumas los medios.",
        "Para leer un valor exacto, mira dónde termina la barra y compara con las marcas de la escala. Escribe el número con su unidad, por ejemplo 25 kilos. Cuando una barra está entre marcas, nunca respondas con una marca cualquiera.",
    ],
    vocab=[("valor exacto", "número preciso al que llega una barra"), ("mitad", "una de las dos partes iguales de algo"), ("símbolo partido", "símbolo que vale la mitad de uno completo"), ("unidad", "palabra que dice qué se cuenta, como kilos o panes")],
    worked=[
        {"title": "Barra entre dos marcas", "problem": FRUTAS + " ¿Cuántos kilos de pera se vendieron?", "steps": ["La barra de pera llega a la mitad entre 20 y 30.", "La mitad de 10 es 5, y 20 + 5 = 25."], "answer": "Se vendieron 25 kilos de pera"},
        {"title": "Símbolos partidos", "problem": PAN + " ¿Cuántos panes se vendieron el lunes?", "steps": ["Tres ● valen 3 × 10 = 30.", "Un ◐ vale 5; 30 + 5 = 35."], "answer": "Se vendieron 35 panes"},
    ],
    mistakes=[
        {"wrong": "Leer una barra que queda entre 20 y 30 como 30.", "why": "Se elige la marca más cercana sin calcular el valor.", "fix": "Calcula la mitad de la distancia entre las marcas: 25."},
        {"wrong": "Contar un símbolo partido como uno entero.", "why": "No se lee que un ◐ vale la mitad.", "fix": "Un ◐ vale 5 cuando el ● vale 10."},
    ],
    tiers={
        "recovery": [
            ex(FRUTAS + " ¿Cuántos kilos de manzana se vendieron?", "40", "Su barra llega a la marca 40."),
            ex(FRUTAS + " ¿Cuántos kilos de plátano se vendieron?", "50", "Su barra llega a la marca 50."),
            ex(PAN + " ¿Cuánto vale un ◐?", "5 panes", "La clave dice que un ◐ vale 5 panes."),
        ],
        "understand": [
            ex(FRUTAS + " ¿Cuántos kilos de naranja se vendieron?", "35", "Está a la mitad entre 30 y 40."),
            ex(FRUTAS + " ¿Cuántos kilos de uva se vendieron?", "15", "Está a la mitad entre 10 y 20."),
            ex(PAN + " ¿Cuántos panes se vendieron el martes?", "20", "Dos ● valen 2 × 10 = 20.", calc="2*10"),
        ],
        "apply": [
            ex(PAN + " ¿Cuántos panes se vendieron el miércoles?", "40", "Cuatro ● valen 4 × 10 = 40.", calc="4*10"),
            ex(PAN + " ¿Cuántos panes se vendieron el jueves?", "15", "10 + 5 = 15.", calc="10+5"),
            arith(FRUTAS + " ¿Cuántos kilos de pera y de uva se vendieron en total?", "25+15", "Pera 25 y uva 15 se suman.", " kilos"),
        ],
        "reason": [
            ex("Una barra llega a la mitad entre la marca 40 y la 50. Rosa responde 50. ¿Qué error hay y cuál es el valor?", "Eligió una marca; el valor es 45", "Hay que calcular la mitad entre 40 y 50.", calc="40+5"),
            ex("Un pictograma tiene ●●● ◐ con ● = 10 y ◐ = 5. Tomás dice que son 40. ¿Qué hizo mal?", "Contó el ◐ como entero; son 35", "3 × 10 + 5 = 35.", calc="3*10+5"),
        ],
        "challenge": [
            ex(FRUTAS + " ¿Cuántos kilos más de manzana que de pera se vendieron?", "15", "40 − 25 = 15.", calc="40-25"),
            ex(PAN + " ¿Cuántos panes se vendieron en total el lunes y el jueves?", "50", "35 + 15 = 50.", calc="35+15"),
        ],
    },
    context=[ex("En una verdulería, un gráfico con escala de 10 en 10 muestra que la barra de las zanahorias llega justo a la mitad entre 30 y 40. ¿Cuántos kilos de zanahoria se vendieron?", "35", "La mitad entre 30 y 40 es 35.")],
    selfcheck=[
        ex(FRUTAS + " ¿Cuál fruta se vendió menos?", "Uva", "Uva llega solo a 15."),
        ex(PAN + " ¿Qué día se vendieron 20 panes?", "El martes", "Dos ● valen 20."),
        ex("Una barra llega a la mitad entre 0 y 10 en una escala de 10 en 10. ¿Cuál es su valor?", "5", "La mitad de 10 es 5.", calc="10//2"),
    ],
    open_task=task(
        "Usa el gráfico de frutas de esta clase: " + FRUTAS + " Escribe el valor exacto de cada fruta con su unidad, ordena las frutas de la que más se vendió a la que menos y explica cómo leíste la barra de la pera.",
        "Plátano 50, manzana 40, naranja 35, pera 25, uva 15. En la pera la barra queda a la mitad entre 20 y 30, así que vale 25.",
        ["da los cinco valores con unidad", "ordena de mayor a menor", "explica cómo leyó una barra entre marcas", "no aproxima a la marca más cercana"],
        ["cinco valores", "orden", "explicación"],
        ["aproximar a la marca más cercana", "olvidar la unidad"],
        "Pide mostrar con el dedo la mitad entre las dos marcas. Reconoce el cálculo de la mitad.",
    ),
    reinforce="Mira una regla y di a qué número llega un lápiz que termina justo a la mitad entre el 10 y el 20.",
    extend="Inventa un pictograma con símbolos enteros y partidos, escribe su clave y calcula el total.",
)

register(
    OA27, 3,
    materials="Lápiz y papel. El gráfico está descrito en cada ejercicio; puedes dibujarlo en papel cuadriculado.",
    use="Aprenderé a comparar categorías de un gráfico y a calcular diferencias y totales. Sirve para saber cuánto más o cuánto menos hay.",
    prior=["Sé leer valores exactos.", "Sé sumar y restar números hasta 100."],
    explain=[
        "Para comparar categorías, primero lee el valor de cada barra. Luego decide cuál es la mayor y cuál es la menor. La mayor es la barra más alta, o el pictograma con más valor, y la menor es la más baja.",
        "La diferencia entre dos categorías se calcula restando: el valor mayor menos el valor menor. Si fútbol tiene 18 y tenis tiene 9, la diferencia es 18 − 9 = 9 estudiantes más en fútbol que en tenis.",
        "El total se calcula sumando todas las categorías. Si fútbol 18, natación 12, básquetbol 15 y tenis 9, el total es 18 + 12 + 15 + 9 = 54 estudiantes. Siempre escribe la unidad en la respuesta.",
    ],
    vocab=[("mayor", "la categoría con el valor más alto"), ("menor", "la categoría con el valor más bajo"), ("diferencia", "resultado de restar el valor menor al mayor"), ("total", "suma de todas las categorías")],
    worked=[
        {"title": "Calcular una diferencia", "problem": DEPORTES + " ¿Cuántos estudiantes más prefieren fútbol que natación?", "steps": ["Fútbol tiene 18 y natación 12.", "Resto: 18 − 12 = 6."], "answer": "6 estudiantes más prefieren fútbol"},
        {"title": "Calcular el total", "problem": DEPORTES + " ¿Cuántos estudiantes respondieron en total?", "steps": ["Sumo las cuatro barras: 18 + 12 + 15 + 9.", "18 + 12 = 30; 30 + 15 = 45; 45 + 9 = 54."], "answer": "Respondieron 54 estudiantes"},
    ],
    mistakes=[
        {"wrong": "Calcular la diferencia sumando los dos valores.", "why": "Se confunde cuánto más con cuánto en total.", "fix": "Resta el valor menor al mayor."},
        {"wrong": "Decir que la categoría con más letras en el nombre es la mayor.", "why": "Se mira el nombre y no la barra.", "fix": "Compara los valores de las barras."},
    ],
    tiers={
        "recovery": [
            ex(DEPORTES + " ¿Cuál es el deporte favorito de más estudiantes?", "Fútbol", "Su barra es la más alta, con 18."),
            ex(DEPORTES + " ¿Cuál es el deporte favorito de menos estudiantes?", "Tenis", "Su barra es la más baja, con 9."),
            ex(DEPORTES + " ¿Cuántos estudiantes prefieren básquetbol?", "15", "Su barra llega a la marca 15."),
        ],
        "understand": [
            arith(DEPORTES + " ¿Cuántos estudiantes más prefieren fútbol que tenis?", "18-9", "Se resta el valor menor al mayor.", " estudiantes"),
            arith(DEPORTES + " ¿Cuántos estudiantes más prefieren básquetbol que natación?", "15-12", "Se resta el valor menor al mayor.", " estudiantes"),
            ex("¿Qué operación se usa para saber cuántos más hay en una categoría que en otra?", "Una resta", "La diferencia es mayor menos menor."),
        ],
        "apply": [
            arith(DEPORTES + " ¿Cuántos estudiantes prefieren natación o tenis?", "12+9", "Se suman las dos barras.", " estudiantes"),
            arith(DEPORTES + " ¿Cuántos estudiantes respondieron en total?", "18+12+15+9", "Se suman las cuatro barras.", " estudiantes"),
            arith(DEPORTES + " ¿Cuántos estudiantes más hay entre fútbol y básquetbol juntos que entre natación y tenis juntos?", "(18+15)-(12+9)", "Se suma cada par y se restan los totales.", " estudiantes"),
        ],
        "reason": [
            ex("Pía dice que la diferencia entre 18 y 9 es 27. ¿Qué operación usó mal y cuál es la diferencia?", "Sumó en vez de restar; es 9", "18 − 9 = 9.", calc="18-9"),
            ex(DEPORTES + " ¿Es verdad que natación tiene exactamente la mitad de estudiantes que fútbol? Explica con los valores.", "No; natación tiene 12 y la mitad de 18 es 9", "18 ÷ 2 = 9, que no es 12.", calc="18//2"),
        ],
        "challenge": [
            ex(DEPORTES + " Si se suma 1 estudiante a tenis, ¿tiene tenis más que natación?", "No", "Tenis pasaría a 10, menos que 12."),
            ex(DEPORTES + " ¿Cuántos estudiantes tendría que sumar tenis para igualar a básquetbol?", "6", "15 − 9 = 6.", calc="15-9"),
        ],
    },
    context=[ex(MASC + " ¿Cuántos estudiantes más prefieren perro que gato?", "4", "12 − 8 = 4.", calc="12-8")],
    selfcheck=[
        ex(MASC + " ¿Qué mascota prefieren menos estudiantes?", "Ave", "Su barra llega solo a 2."),
        ex(MASC + " ¿Cuántos estudiantes respondieron en total?", "26", "12 + 8 + 4 + 2 = 26.", calc="12+8+4+2"),
        ex(MASC + " ¿Cuántos estudiantes más prefieren pez que ave?", "2", "4 − 2 = 2.", calc="4-2"),
    ],
    open_task=task(
        "Usa el gráfico de deportes de esta clase: " + DEPORTES + " Escribe cuál es el mayor y el menor, calcula una diferencia entre dos deportes que elijas y calcula el total de estudiantes. Muestra las operaciones.",
        "Mayor: fútbol, 18. Menor: tenis, 9. Diferencia fútbol y tenis: 18 − 9 = 9. Total: 18 + 12 + 15 + 9 = 54.",
        ["dice mayor y menor", "calcula una diferencia con resta", "calcula el total con suma", "escribe las unidades"],
        ["mayor y menor", "diferencia", "total"],
        ["sumar en vez de restar", "olvidar una barra en el total"],
        "Pide mostrar de dónde sacó cada número. Reconoce que use la operación correcta.",
    ),
    reinforce="Con una tabla de datos de tu casa (por ejemplo, frutas que comió cada persona), calcula el total y una diferencia.",
    extend="Inventa una pregunta que se responda con una suma y otra que se responda con una resta, usando el gráfico de mascotas de esta clase.",
)

register(
    OA27, 4,
    materials="Lápiz y papel. El gráfico está descrito con palabras en cada ejercicio.",
    use="Aprenderé a escribir conclusiones claras que se apoyen en los datos de un gráfico. Sirve para explicar lo que muestran los datos sin inventar.",
    prior=["Sé leer valores, hacer diferencias y calcular totales.", "Sé qué es un título y una escala."],
    explain=[
        "Una conclusión es una frase que dice lo que muestran los datos. Una buena conclusión usa números del gráfico como evidencia. Por ejemplo: «El perro es la mascota más elegida, con 12 votos, y el ave la menos elegida, con 2 votos».",
        "Una conclusión debe poder comprobarse mirando el gráfico. No debe agregar cosas que el gráfico no dice, como las razones por las que las personas eligieron algo. Tampoco debe hablar de personas que no fueron encuestadas.",
        "Para escribir una buena conclusión, sigue tres pasos: nombra la categoría o las categorías, di los valores, y compara con una palabra como más, menos o igual. Termina con la unidad, por ejemplo estudiantes o libros.",
    ],
    vocab=[("conclusión", "frase que dice lo que muestran los datos"), ("evidencia", "datos del gráfico que apoyan lo que afirmo"), ("comparar", "decir qué es mayor, menor o igual"), ("afirmación sin apoyo", "frase que no se puede comprobar con el gráfico")],
    worked=[
        {"title": "Escribir una conclusión con evidencia", "problem": MASC + " Escribe una conclusión con números.", "steps": ["Nombro la mayor y la menor: perro 12 y ave 2.", "Comparo con una resta: 12 − 2 = 10."], "answer": "El perro fue elegido por 12 estudiantes y el ave por 2: 10 estudiantes más eligieron perro"},
        {"title": "Revisar una afirmación", "problem": MASC + " Un estudiante dice: «Los gatos son mejores que los peces porque son más suaves». ¿Está apoyada en el gráfico?", "steps": ["El gráfico muestra cuántos prefirieron cada mascota.", "No dice nada sobre lo suave que son."], "answer": "No está apoyada; solo se puede decir que 8 prefieren gato y 4 prefieren pez"},
    ],
    mistakes=[
        {"wrong": "Escribir una conclusión sin números, como «Gustan los perros».", "why": "No hay evidencia que se pueda comprobar.", "fix": "Agrega los valores del gráfico: 12 estudiantes."},
        {"wrong": "Agregar razones que el gráfico no muestra.", "why": "Se inventa información.", "fix": "Dilo solo con lo que el gráfico entrega."},
    ],
    tiers={
        "recovery": [
            ex(MASC + " ¿Cuántos estudiantes prefieren perro?", "12", "Su barra llega a la marca 12."),
            ex(MASC + " ¿Cuántos estudiantes prefieren gato?", "8", "Su barra llega a la marca 8."),
            ex("Una buena conclusión, ¿debe usar números del gráfico o puede no usarlos?", "Debe usar números del gráfico", "Los números son la evidencia."),
        ],
        "understand": [
            ex(MASC + " ¿La frase «El perro es la mascota más elegida» está apoyada en el gráfico?", "Sí", "La barra del perro es la más alta."),
            ex(MASC + " ¿La frase «Los gatos son más tiernos» está apoyada en el gráfico?", "No", "El gráfico no muestra ternura."),
            ex(MASC + " ¿Cuál es la diferencia entre perro y ave?", "10", "12 − 2 = 10.", calc="12-2"),
        ],
        "apply": [
            ex(MASC + " Completa la conclusión: «Perro y gato juntos suman … estudiantes».", "20", "12 + 8 = 20.", calc="12+8"),
            ex(MASC + " Completa la conclusión: «Ave tiene … estudiantes menos que pez».", "2", "4 − 2 = 2.", calc="4-2"),
            ex(MASC + " Completa: «En total respondieron … estudiantes».", "26", "12 + 8 + 4 + 2 = 26.", calc="12+8+4+2"),
        ],
        "reason": [
            ex(MASC + " Ana escribe: «Nadie quiere peces». ¿Está bien apoyada? Explica con el gráfico.", "No; 4 estudiantes prefirieron pez", "La barra de pez llega a 4."),
            ex(MASC + " Beto escribe: «Perro tiene más votos que todas las otras mascotas juntas». ¿Es verdad?", "No; las otras suman 14 y perro 12", "8 + 4 + 2 = 14, que es mayor que 12.", calc="8+4+2"),
        ],
        "challenge": [
            ex(MASC + " ¿Cuál de estas conclusiones está apoyada: «Gato tiene el doble que pez» o «Perro es el favorito de todos los estudiantes»?", "«Gato tiene el doble que pez»", "Gato 8 es el doble de pez 4; perro tiene 12 de 26, no todos."),
            ex(MASC + " Escribe cuántos estudiantes no eligieron perro.", "14", "26 − 12 = 14.", calc="26-12"),
        ],
    },
    context=[ex("Una escuela encuestó a 40 estudiantes y el gráfico muestra: fútbol 18, natación 12, básquetbol 6 y tenis 4. Una conclusión dice «Fútbol es el deporte más elegido, con 18 estudiantes». ¿Está apoyada?", "Sí", "La barra más alta es la de fútbol, con 18.")],
    selfcheck=[
        ex("¿Qué es una conclusión?", "Una frase que dice lo que muestran los datos", "Se apoya en el gráfico."),
        ex(MASC + " ¿Qué suma más estudiantes: perro y gato juntos, o ave y pez juntos?", "Perro y gato juntos", "Perro y gato suman 20 y ave y pez suman 6."),
        ex("¿Una conclusión puede decir por qué las personas eligieron algo, si el gráfico no lo dice?", "No", "No hay evidencia en el gráfico."),
    ],
    open_task=task(
        "Usa el gráfico de mascotas de esta clase: " + MASC + " Escribe tres conclusiones con números: una de mayor y menor, una con una diferencia y una con un total. Después escribe una frase que NO se puede apoyar con este gráfico.",
        "Perro es la mascota más elegida con 12 y ave la menos elegida con 2. Perro tiene 4 más que gato. Respondieron 26 estudiantes en total. No se puede apoyar: «Los perros son más cariñosos».",
        ["escribe tres conclusiones con números", "una compara mayor y menor", "una usa diferencia y una total", "da un ejemplo de frase sin apoyo"],
        ["tres conclusiones", "ejemplo de frase sin apoyo"],
        ["conclusiones sin números", "agregar razones que el gráfico no da"],
        "Pide mostrar en el gráfico dónde está cada número. Reconoce la frase sin apoyo bien identificada.",
    ),
    reinforce="Lee una conclusión de una noticia con un gráfico y revisa si se apoya en números.",
    extend="Usa este gráfico: " + LIBROS + " Escribe una conclusión con números y una frase que no se pueda apoyar con ese gráfico.",
)

register(
    OA27, 5,
    materials="Lápiz y papel. Los gráficos con errores están descritos con palabras y números.",
    use="Aprenderé a detectar gráficos que pueden engañar. Sirve para no creer una conclusión solo por cómo se ve el dibujo.",
    prior=["Sé leer título, ejes y escala.", "Sé comparar valores de un gráfico."],
    explain=[
        "Un gráfico puede dar una idea equivocada aunque los números sean verdaderos. Por ejemplo, si el eje vertical no parte de 0, dos barras que valen 52 y 56 pueden verse como si una fuera mucho más alta que la otra, y la diferencia real es solo 4.",
        "También engañan las escalas con saltos desiguales, como 0, 10, 20, 50, 60. Y en un pictograma, si los símbolos tienen distinto tamaño, no se pueden comparar solo por cuántos se ven. Cada símbolo debe valer lo mismo y tener el mismo tamaño.",
        "Para revisar un gráfico, mira cinco cosas: si tiene título, si los ejes tienen nombre, si la escala parte de 0, si las marcas están a igual distancia y si los símbolos son iguales. Si algo falla, no confíes en lo que parece: usa los números.",
    ],
    vocab=[("engañoso", "que hace creer algo que no es verdad"), ("eje que no parte de 0", "eje cuya escala empieza en otro número"), ("escala irregular", "escala con saltos distintos entre marcas"), ("revisar", "mirar con cuidado para encontrar errores")],
    worked=[
        {"title": "Eje que no parte de cero", "problem": "Un gráfico tiene la escala desde 50: marcas 50, 55, 60. La barra de A llega a 52 y la de B llega a 56. ¿B vale el doble de A?", "steps": ["Leo los valores: A vale 52 y B vale 56.", "El doble de 52 sería 104, no 56."], "answer": "No; B vale 56, un poco más que A"},
        {"title": "Símbolos de distinto tamaño", "problem": "En un pictograma, 2 símbolos grandes y 3 símbolos pequeños valen cada uno 5 libros. ¿Se pueden comparar solo por tamaño?", "steps": ["Cada símbolo vale lo mismo, 5 libros.", "Los 3 pequeños valen más que los 2 grandes: 15 y 10."], "answer": "No; hay que contar cuántos símbolos hay, no mirar su tamaño"},
    ],
    mistakes=[
        {"wrong": "Decidir solo mirando qué barra se ve más alta.", "why": "Si la escala no parte de 0, la altura engaña.", "fix": "Lee el valor numérico de cada barra."},
        {"wrong": "Comparar símbolos de un pictograma por su tamaño.", "why": "Cada símbolo debería valer lo mismo.", "fix": "Cuenta los símbolos y multiplica por su valor."},
    ],
    tiers={
        "recovery": [
            ex("¿En qué número debería partir la escala de un gráfico de barras para no engañar?", "En 0", "Así la altura es proporcional al valor."),
            ex("Un gráfico sin título, ¿se entiende bien?", "No", "No dice de qué trata."),
            ex("En un pictograma, ¿todos los símbolos deben valer lo mismo?", "Sí", "Si no, no se puede comparar."),
        ],
        "understand": [
            ex("Dos barras valen 52 y 56. En un gráfico que parte desde 50 se ven muy distintas. ¿Cuál es la diferencia real?", "4", "56 − 52 = 4.", calc="56-52"),
            ex("Una escala marca 0, 10, 20, 50, 60. ¿Qué problema tiene?", "Los saltos no son iguales", "De 20 a 50 hay un salto mayor."),
            ex("¿Qué se debe hacer para no engañarse con un gráfico?", "Leer los valores numéricos", "Los números dicen lo que de verdad hay."),
        ],
        "apply": [
            ex("Un gráfico parte desde 20. La barra de Luis llega a 24 y la de Marta a 28. ¿Cuánto más vale la de Marta?", "4", "28 − 24 = 4.", calc="28-24"),
            ex("Un pictograma: ● vale 4 galletas. Lunes tiene 3 ● y martes 5 ●, pero los del lunes son más grandes. ¿Qué día se vendieron más galletas?", "El martes", "5 × 4 = 20 es mayor que 3 × 4 = 12."),
            ex("Una escala va 0, 5, 10, 15, 20. ¿Está bien hecha?", "Sí", "Todos los saltos son de 5."),
        ],
        "reason": [
            ex("Teo dice que una barra de 56 es el doble de una barra de 52 porque se ve mucho más alta. ¿Qué error hay?", "El eje no parte de 0; el doble de 52 sería 104", "56 es solo un poco más que 52.", calc="52*2"),
            ex("Una empresa dibuja ● grandes para sus ventas y ● chicos para las de su competencia, con la misma clave. ¿Es justo? Explica.", "No; el tamaño hace parecer mayor su cantidad", "Cada símbolo debe tener el mismo tamaño."),
        ],
        "challenge": [
            ex("Un gráfico parte en 100. Las barras llegan a 102 y 108. Alguien dice «la segunda es mucho más grande». ¿Cuál es la diferencia real?", "6", "108 − 102 = 6.", calc="108-102"),
            ex("Un pictograma tiene ● = 5 y cuatro ●: ¿cuántos hay en total, aunque se vean pequeños?", "20", "4 × 5 = 20.", calc="4*5"),
        ],
    },
    context=[ex("Un aviso muestra dos barras de ventas con la escala partiendo de 1.000: una llega a 1.020 y la otra a 1.050, y se ven muy distintas. ¿Cuánto es la diferencia real entre las ventas?", "30", "1.050 − 1.020 = 30.", calc="1050-1020")],
    selfcheck=[
        ex("¿Qué cinco cosas conviene revisar en un gráfico? Nombra una de ellas.", "Título, nombres de ejes, escala desde 0, marcas iguales o símbolos iguales", "Cualquiera de esas sirve para revisar."),
        ex("Si dos barras valen 30 y 33 en un eje que parte desde 30, ¿una es mucho mayor que la otra?", "No; la diferencia es 3", "33 − 30 = 3.", calc="33-30"),
        ex("¿Qué indica que un gráfico puede engañar: escala desde 0 o escala desde 50 para valores como 52 y 56?", "Escala desde 50", "No parte de 0."),
    ],
    open_task=task(
        "Observa estos dos gráficos descritos. Gráfico A: eje vertical desde 0 con marcas de 10 en 10; barras de 52 y 56 que se ven casi iguales. Gráfico B: eje vertical desde 50 con marcas de 2 en 2; barras de 52 y 56 que se ven como si una fuera mucho más alta que la otra. Explica cuál puede engañar, por qué, y qué haces para saber la verdad.",
        "El B puede engañar porque el eje parte de 50 y no de 0. Leo los valores: 52 y 56, la diferencia es 4. Uso los números y no el dibujo.",
        ["elige el gráfico que engaña", "explica por qué con el eje", "calcula la diferencia real", "dice que se leen los valores"],
        ["gráfico elegido", "explicación", "diferencia"],
        ["fiarse solo del dibujo", "no calcular la diferencia"],
        "Pide mostrar cómo leyó los valores. Reconoce que use los números y no la altura.",
    ),
    reinforce="Busca un gráfico en un diario o en internet con ayuda de un adulto y revisa si la escala parte de 0.",
    extend="Dibuja dos gráficos con los mismos datos: uno que no engañe y otro con la escala cortada. Explica la diferencia.",
)
