"""Student material for 5.º básico Matemática, OA 26 (leer, interpretar y completar tablas, gráficos de barra simple y de línea; comunicar conclusiones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA26 = "MA05 OA 26"

TABLA_LIB = "Tabla «Libros prestados en la biblioteca»: lunes 24, martes 18, miércoles 30, jueves 12 y viernes 36."
BARRAS_DEP = "Gráfico de barras «Deporte favorito del curso». Eje vertical: cantidad de estudiantes, con marcas de 5 en 5 desde 0 hasta 30. Fútbol llega a la marca 25, natación a la 15, tenis a la 10 y básquetbol a la 20."
LINEA_T = "Gráfico de línea «Temperatura de un día de otoño». Eje horizontal: las horas 9, 11, 13, 15 y 17. Eje vertical: grados Celsius, con marcas de 5 en 5 desde 0 hasta 30. Los puntos están en la marca 10 a las 9 h, en la 15 a las 11 h, en la 25 a las 13 h, en la 20 a las 15 h y en la 15 a las 17 h. Los puntos se unen con segmentos."
LINEA_V = "Gráfico de línea «Visitas a la biblioteca por mes». Eje horizontal: marzo, abril, mayo, junio y julio. Eje vertical: cantidad de visitas, con marcas de 20 en 20 desde 0 hasta 100. Los puntos están en la marca 40 en marzo, en la 60 en abril, en la 100 en mayo, en la 80 en junio y en la 20 en julio. Los puntos se unen con segmentos."
AGUA = "Gráfico de barras «Agua usada para regar la huerta del colegio». Eje vertical: litros, con marcas de 20 en 20 desde 0 hasta 120. Lunes llega a la marca 80. Martes llega justo a la mitad entre las marcas 60 y 80. Miércoles llega a la marca 100. Jueves llega justo a la mitad entre las marcas 80 y 100. Viernes llega a la marca 40."
LECTURA = "Tabla «Minutos de lectura por semana»: semana 1: 5.º A 60 y 5.º B 80; semana 2: 5.º A 90 y 5.º B 70; semana 3: 5.º A 120 y 5.º B 90; semana 4: 5.º A 150 y 5.º B 100."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA26, 1,
    materials="Lápiz, regla y papel, mejor si es cuadriculado. Las tablas y los gráficos están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a leer tablas y gráficos de barras: dónde está cada dato y qué dice la escala. Sirve para sacar datos exactos y no equivocarse al interpretar.",
    prior=["Sé contar de 5 en 5, de 10 en 10 y de 20 en 20.", "Sé sumar y restar números hasta 200."],
    explain=[
        "Una tabla ordena datos en filas y columnas. Cada fila o columna tiene un encabezado que dice qué es cada dato. En la tabla «Libros prestados» el encabezado dice el día, y al lado está la cantidad de libros de ese día.",
        "Un gráfico de barras muestra la misma información con barras. Tiene un título, que dice de qué trata; un eje horizontal con las categorías, como los días o los deportes; y un eje vertical con la escala. La escala dice cuánto vale cada marca: si sube de 5 en 5, la quinta marca después del 0 vale 25.",
        "Para leer una barra, mira hasta qué marca llega y lee su valor en la escala. Para completar una tabla desde un gráfico, copia el valor de cada barra en su fila. Para ordenar o comparar, usa los números. Siempre escribe la unidad: libros, estudiantes o litros.",
    ],
    vocab=[("tabla", "datos ordenados en filas y columnas"), ("encabezado", "palabra que dice qué son los datos de una fila o columna"), ("escala", "números del eje vertical que dicen cuánto vale cada marca"), ("categoría", "cada grupo que se compara, como un día o un deporte")],
    worked=[
        {"title": "Leer una tabla", "problem": TABLA_LIB + " ¿Cuántos libros se prestaron el lunes y el martes juntos?", "steps": ["Lunes son 24 libros y martes son 18 libros.", "Los sumo: 24 + 18 = 42."], "answer": "Se prestaron 42 libros"},
        {"title": "Leer una barra", "problem": BARRAS_DEP + " ¿Cuántos estudiantes prefieren natación?", "steps": ["Busco la barra de natación y miro hasta qué marca llega.", "Llega a la marca 15 y la escala sube de 5 en 5."], "answer": "Prefieren natación 15 estudiantes"},
    ],
    mistakes=[
        {"wrong": "Leer una barra que llega a la quinta marca de una escala de 5 en 5 como 5.", "why": "Se cuenta cuántas marcas hay y no se mira su valor.", "fix": "Mira el número escrito en la marca: la quinta marca vale 25."},
        {"wrong": "Sumar solo algunas filas de la tabla para obtener el total.", "why": "Se olvida alguna categoría.", "fix": "Para el total, suma todas las filas, una por una."},
    ],
    tiers={
        "recovery": [
            ex(TABLA_LIB + " ¿Cuántos libros se prestaron el miércoles?", "30", "Está en la fila del miércoles."),
            ex(TABLA_LIB + " ¿Qué día se prestaron menos libros?", "Jueves", "Tiene 12, el número más pequeño."),
            ex(BARRAS_DEP + " ¿De cuánto en cuánto sube la escala del eje vertical?", "De 5 en 5", "Las marcas son 0, 5, 10, 15, 20, 25 y 30."),
        ],
        "understand": [
            ex(BARRAS_DEP + " ¿Cuántos estudiantes prefieren natación?", "15", "La barra llega a la marca 15."),
            ex(BARRAS_DEP + " ¿Qué deporte prefieren 10 estudiantes?", "Tenis", "Su barra llega a la marca 10."),
            arith(TABLA_LIB + " ¿Cuántos libros se prestaron el lunes y el martes juntos?", "24+18", "Se suman los dos días.", " libros"),
        ],
        "apply": [
            arith(TABLA_LIB + " ¿Cuántos libros se prestaron en toda la semana?", "24+18+30+12+36", "Se suman los cinco días.", " libros"),
            arith(BARRAS_DEP + " ¿Cuántos estudiantes más prefieren fútbol que básquetbol?", "25-20", "Se resta el valor menor al mayor.", " estudiantes"),
            arith(BARRAS_DEP + " Se agrega a la tabla del gráfico la fila «Total». ¿Qué número va en ella?", "25+15+10+20", "Se suman las cuatro barras.", " estudiantes"),
        ],
        "reason": [
            ex(BARRAS_DEP + " Mía dice que la barra de fútbol llega a la quinta marca después del 0, así que vale 5. ¿Qué error hay y cuánto vale?", "Contó marcas y no leyó su valor; vale 25", "5 marcas de 5 en 5 valen 25.", calc="5*5"),
            ex("Leo dice que un gráfico de barras sin título está bien porque se entiende por los números. ¿Qué problema tiene?", "No se sabe de qué trata", "El título dice qué se está contando."),
        ],
        "challenge": [
            ex(TABLA_LIB + " Si el jueves se hubieran prestado 6 libros más, ¿cuántos libros se habrían prestado ese día?", "18", "12 + 6 = 18.", calc="12+6"),
            ex(TABLA_LIB + " ¿Qué día tiene exactamente el doble de libros que el jueves?", "Lunes", "El doble de 12 es 24, y el lunes tiene 24."),
        ],
    },
    context=[ex("Una tabla anotó cuántas botellas recicló cada curso: 5.º A 45, 5.º B 60 y 5.º C 35. ¿Cuántas botellas más recicló 5.º B que 5.º C?", "25", "60 − 35 = 25.", calc="60-35")],
    selfcheck=[
        ex(TABLA_LIB + " ¿Qué día se prestaron más libros?", "Viernes", "Tiene 36, el número más grande."),
        ex(BARRAS_DEP + " ¿Cuántos estudiantes prefieren básquetbol?", "20", "Su barra llega a la marca 20."),
        ex("¿Qué dice el título de un gráfico?", "De qué trata", "Es la frase que describe lo que se cuenta."),
    ],
    open_task=task(
        "Con la tabla de libros prestados, dibuja un gráfico de barras en papel cuadriculado: escribe un título, dibuja los dos ejes, elige una escala de 5 en 5 hasta 40 y dibuja las cinco barras. Debajo escribe dos cosas que descubres con tu gráfico. Datos: lunes 24, martes 18, miércoles 30, jueves 12 y viernes 36.",
        "Título: Libros prestados en la biblioteca. Escala de 5 en 5. Descubrí que el viernes se prestaron más libros y que el jueves se prestaron menos.",
        ["título y dos ejes", "escala de 5 en 5 hasta 40", "cinco barras que llegan al valor correcto", "dos conclusiones con números"],
        ["gráfico", "dos conclusiones"],
        ["dibujar barras que no llegan al valor", "olvidar el título o la escala"],
        "Pide leer cada barra en voz alta con su valor. Reconoce que la escala esté completa.",
    ),
    reinforce="Busca una tabla o un gráfico en un diario y di qué dice su título y de cuánto en cuánto sube su escala.",
    extend="Escribe una tabla de 4 filas con tus datos de la semana, por ejemplo minutos de lectura, y dibuja su gráfico de barras.",
)

register(
    OA26, 2,
    materials="Lápiz y papel. Los gráficos están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a pasar de una tabla a un gráfico de línea y al revés, y a leer en él cuánto sube o baja un dato. Sirve para ver cómo cambia algo a lo largo del tiempo.",
    prior=["Sé leer tablas y gráficos de barras.", "Sé restar para calcular una diferencia."],
    explain=[
        "Un gráfico de línea muestra cómo cambia algo en el tiempo, como la temperatura durante el día. En el eje horizontal van los momentos, por ejemplo las horas. En el eje vertical va la escala. Cada dato es un punto, y los puntos se unen con segmentos.",
        "Una tabla y un gráfico de línea muestran los mismos datos. Si la tabla dice que a las 13 h hubo 25 grados, en el gráfico el punto de las 13 h está en la marca 25. Para pasar de uno al otro, ubica el momento en el eje horizontal y el valor en el vertical.",
        "Un segmento que sube significa que el valor aumentó; uno que baja significa que disminuyó. Para saber cuánto cambió, resta el valor menor al mayor entre los dos puntos. Un segmento horizontal, que ni sube ni baja, significa que el valor se mantuvo igual.",
    ],
    vocab=[("gráfico de línea", "gráfico de puntos unidos con segmentos que muestra cambios en el tiempo"), ("punto", "marca que muestra el valor de un dato"), ("segmento", "línea recta entre dos puntos"), ("aumentar y disminuir", "subir o bajar un valor")],
    worked=[
        {"title": "De la tabla al gráfico", "problem": LINEA_T + " La tabla dice: hora 9, 11, 13, 15, 17 y temperatura 10, 15, ?, 20, 15. ¿Qué número falta?", "steps": ["Falta el valor de las 13 h.", "En el gráfico, el punto de las 13 h está en la marca 25."], "answer": "Falta el 25"},
        {"title": "Cuánto cambió", "problem": LINEA_T + " ¿Cuántos grados subió la temperatura entre las 9 y las 13 h?", "steps": ["A las 9 h son 10 grados y a las 13 h son 25 grados.", "Resto: 25 − 10 = 15."], "answer": "Subió 15 grados"},
    ],
    mistakes=[
        {"wrong": "Decir que un punto más a la derecha tiene un valor menor.", "why": "Se confunde la posición horizontal con el valor.", "fix": "El valor se lee en el eje vertical; la derecha solo indica un momento más tarde."},
        {"wrong": "Unir los puntos de un gráfico de línea sin ver la escala.", "why": "Se dibuja sin ubicar cada valor en su marca.", "fix": "Ubica cada punto en su hora y su marca, y luego los une."},
    ],
    tiers={
        "recovery": [
            ex(LINEA_T + " ¿Qué temperatura hubo a las 13 h?", "25 grados", "El punto de las 13 h está en la marca 25."),
            ex(LINEA_T + " ¿Qué se muestra en el eje horizontal?", "Las horas", "Los números 9, 11, 13, 15 y 17 son horas."),
            ex("¿Qué se une con segmentos en un gráfico de línea?", "Los puntos", "Cada punto es un dato."),
        ],
        "understand": [
            ex(LINEA_T + " ¿A qué hora hubo 10 grados?", "A las 9 h", "El punto de las 9 h está en la marca 10."),
            ex(LINEA_T + " ¿A qué hora hizo más calor?", "A las 13 h", "Tiene la temperatura mayor, 25 grados."),
            ex(LINEA_T + " La tabla de este gráfico dice: hora 9, 11, 13, 15, 17 y temperatura 10, 15, ?, 20, 15. ¿Qué número falta?", "25", "Es el valor de las 13 h."),
        ],
        "apply": [
            arith(LINEA_T + " ¿Cuántos grados subió la temperatura entre las 9 h y las 13 h?", "25-10", "Se resta el valor menor al mayor.", " grados"),
            arith(LINEA_T + " ¿Cuántos grados bajó la temperatura entre las 13 h y las 17 h?", "25-15", "Se resta el valor menor al mayor.", " grados"),
            ex(LINEA_T + " Se agrega el dato: a las 19 h hubo 10 grados. ¿En qué marca del eje vertical va el punto?", "En la marca 10", "El valor del dato es 10."),
        ],
        "reason": [
            ex(LINEA_T + " Marta dice que a las 15 h hizo menos calor que a las 11 h porque su punto está más a la derecha. ¿Qué error tiene?", "Mira la posición horizontal; a las 15 h son 20 grados y a las 11 h son 15", "El valor se lee en el eje vertical."),
            ex(LINEA_T + " ¿La línea entre las 9 h y las 11 h sube o baja? ¿Qué significa?", "Sube; la temperatura aumentó", "Pasa de 10 a 15 grados."),
        ],
        "challenge": [
            ex(LINEA_T + " ¿Cuántos tramos seguidos, de una hora medida a la siguiente, bajó la temperatura?", "2", "Bajó de las 13 h a las 15 h y de las 15 h a las 17 h."),
            arith(LINEA_T + " ¿Cuál es la diferencia entre la temperatura mayor y la menor del día?", "25-10", "Se resta la menor a la mayor.", " grados"),
        ],
    },
    context=[ex("Una tabla anotó la altura de una planta de poroto al final de cada semana: semana 1, 4 cm; semana 2, 9 cm; semana 3, 15 cm; semana 4, 20 cm. ¿Cuántos centímetros creció entre la semana 2 y la semana 4?", "11", "20 − 9 = 11.", calc="20-9")],
    selfcheck=[
        ex(LINEA_T + " ¿Qué temperatura hubo a las 15 h?", "20 grados", "El punto de las 15 h está en la marca 20."),
        ex("Si un segmento baja de izquierda a derecha, ¿el valor aumentó o disminuyó?", "Disminuyó", "Baja significa que el valor es menor."),
        ex(LINEA_T + " ¿A qué hora hubo 15 grados por primera vez?", "A las 11 h", "Las 9 h tienen 10 y las 11 h tienen 15."),
    ],
    open_task=task(
        "Con estos datos de una planta, dibuja un gráfico de línea: semana 1, 4 cm; semana 2, 9 cm; semana 3, 15 cm; semana 4, 20 cm. Elige una escala de 5 en 5 hasta 25, ubica los cuatro puntos y únelos. Escribe entre qué dos semanas la planta creció más.",
        "Título: Altura de una planta. La planta creció 5, 6 y 5 cm entre semanas; creció más entre la semana 2 y la 3, con 6 cm.",
        ["ejes y escala de 5 en 5", "cuatro puntos bien ubicados", "los puntos unidos con segmentos", "calcula el cambio entre semanas"],
        ["gráfico", "mayor cambio"],
        ["ubicar mal los puntos", "calcular el cambio sin restar"],
        "Pide mostrar cómo calculó cada cambio. Reconoce el cuidado con la escala.",
    ),
    reinforce="Anota la temperatura que marca un termómetro a tres horas del día durante dos días y dibuja un gráfico de línea.",
    extend="Escribe una tabla de 5 datos de algo que cambia con el tiempo y dibuja su gráfico de línea.",
)

register(
    OA26, 3,
    materials="Lápiz y papel. Los gráficos están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a elegir si conviene un gráfico de barras o uno de línea, y a justificar mi elección. Sirve para mostrar los datos de la forma más clara.",
    prior=["Sé leer gráficos de barras y de línea.", "Sé calcular diferencias entre dos puntos."],
    explain=[
        "Un gráfico de barras sirve para comparar categorías distintas, como deportes favoritos, cursos o colores. Cada barra es una categoría y no hay un orden en el tiempo. Se puede cambiar el orden de las barras sin que los datos pierdan sentido.",
        "Un gráfico de línea sirve para mostrar cómo cambia un dato en el tiempo, como la temperatura por hora, el peso de un gatito por mes o las visitas por mes. Los puntos van en orden y el segmento muestra si sube, baja o se mantiene.",
        "Para decidir, pregúntate: ¿comparo categorías o miro un cambio en el tiempo? Para encontrar el mayor aumento, resta los valores de cada par de puntos seguidos y compara los resultados. Para justificar, escribe la pregunta que te hiciste y los números que usaste.",
    ],
    vocab=[("categoría", "grupo que se compara, como un deporte o un curso"), ("tiempo", "horas, días, meses o años en orden"), ("aumento", "cuánto sube un dato de un punto al siguiente"), ("justificar", "explicar una elección con razones y números")],
    worked=[
        {"title": "Elegir el gráfico", "problem": "Se quiere mostrar cuánto pesó un gatito cada mes durante 5 meses. ¿Conviene un gráfico de barras o uno de línea?", "steps": ["Los datos cambian mes a mes, en orden.", "Un gráfico de línea muestra ese cambio en el tiempo."], "answer": "Conviene un gráfico de línea"},
        {"title": "Buscar el mayor aumento", "problem": LINEA_V + " ¿Entre qué meses seguidos subieron más las visitas?", "steps": ["De marzo a abril: 60 − 40 = 20. De abril a mayo: 100 − 60 = 40.", "El mayor es 40."], "answer": "Entre abril y mayo"},
    ],
    mistakes=[
        {"wrong": "Usar un gráfico de línea para colores favoritos.", "why": "Los colores no tienen orden en el tiempo.", "fix": "Para categorías, usa barras."},
        {"wrong": "Buscar el mayor aumento mirando solo el punto más alto.", "why": "El mayor aumento es entre dos puntos seguidos, no el valor más alto.", "fix": "Resta los valores de cada par de puntos seguidos y compara."},
    ],
    tiers={
        "recovery": [
            ex("Se quiere comparar los sabores de helado favoritos de un curso. ¿Qué gráfico conviene: barras o línea?", "Barras", "Los sabores son categorías."),
            ex("Se quiere mostrar cómo cambió la temperatura cada hora. ¿Qué gráfico conviene: barras o línea?", "Línea", "La temperatura cambia con el tiempo."),
            ex("¿Un gráfico de línea muestra categorías sin orden o cambios en el tiempo?", "Cambios en el tiempo", "Sus puntos están en orden y se unen."),
        ],
        "understand": [
            ex("Se quiere mostrar cuántos goles hizo cada jugador de un equipo. ¿Qué gráfico conviene?", "Barras", "Cada jugador es una categoría."),
            ex("Se quiere mostrar cuánto pesó un gatito cada mes durante 5 meses. ¿Qué gráfico conviene?", "Línea", "Los meses van en orden."),
            ex("Se quiere mostrar cuántos libros prestó cada curso durante una semana: 5.º A, 5.º B y 5.º C. ¿Qué gráfico conviene?", "Barras", "Los cursos son categorías."),
        ],
        "apply": [
            arith(LINEA_V + " ¿Cuántas visitas más hubo en mayo que en abril?", "100-60", "Se resta el valor menor al mayor.", " visitas"),
            arith(LINEA_V + " ¿Cuántas visitas menos hubo en julio que en junio?", "80-20", "Se resta el valor menor al mayor.", " visitas"),
            arith(LINEA_V + " ¿Cuántas visitas hubo en total en los cinco meses?", "40+60+100+80+20", "Se suman los cinco puntos.", " visitas"),
        ],
        "reason": [
            ex("Gabriel dice que usará un gráfico de línea para mostrar cuántos goles hizo cada jugador. ¿Es buena idea? Explica.", "No; los jugadores son categorías y conviene un gráfico de barras", "La línea sugiere un orden en el tiempo que no existe."),
            ex("Sofía unió con una línea las barras de rojo, azul y verde en un gráfico de colores favoritos. ¿Por qué no tiene sentido?", "Porque una línea muestra cambio en el tiempo y los colores no tienen orden", "Los colores son categorías separadas."),
        ],
        "challenge": [
            ex("Una tabla muestra la altura de una planta al final de cada semana: semana 1, 3 cm; semana 2, 8 cm; semana 3, 14 cm; semana 4, 15 cm. ¿Entre cuáles semanas seguidas creció menos?", "Entre la semana 3 y la 4", "Creció 5, 6 y 1 cm entre semanas."),
            ex(LINEA_V + " ¿En qué mes hubo el doble de visitas que en julio?", "Marzo", "El doble de 20 es 40, y marzo tuvo 40."),
        ],
    },
    context=[ex("Un colegio quiere mostrar cuántos estudiantes llegan en bus, a pie o en auto. ¿Qué gráfico conviene?", "Barras", "Bus, a pie y auto son categorías.")],
    selfcheck=[
        ex(LINEA_V + " ¿En qué mes hubo más visitas?", "Mayo", "Llegó a la marca 100."),
        ex("Se quiere mostrar cómo cambiaron, mes a mes durante un año, los minutos que corre una niña en sus entrenamientos. ¿Qué gráfico conviene?", "Línea", "Los meses van en orden y se mira cómo cambia."),
        arith(LINEA_V + " ¿Cuántas visitas más hubo en abril que en marzo?", "60-40", "Se resta el valor menor al mayor.", " visitas"),
    ],
    open_task=task(
        "Se quiere mostrar estos dos conjuntos de datos: A) mascotas favoritas del curso: perro 14, gato 9, pez 5 y ave 2; B) temperatura al mediodía durante 5 días: 14, 16, 15, 19 y 21 grados. Escribe qué gráfico usarías para cada uno y justifica con una frase. Dibuja uno de los dos con su escala.",
        "A) Barras, porque las mascotas son categorías. B) Línea, porque la temperatura cambia día a día. Dibujé B con escala de 5 en 5 hasta 25.",
        ["elige barras para A y línea para B", "justifica cada elección", "dibuja uno con escala y ejes", "ubica bien los valores"],
        ["dos elecciones", "gráfico dibujado"],
        ["usar línea para categorías", "justificar sin hablar del tipo de datos"],
        "Pide decir si los datos son categorías o cambios en el tiempo. Reconoce la justificación.",
    ),
    reinforce="Mira dos gráficos de un diario y di por qué el autor eligió barras o línea.",
    extend="Escribe tres datos que mostrarías con barras y tres que mostrarías con línea, y explica la diferencia.",
)

register(
    OA26, 4,
    materials="Lápiz y papel. Los gráficos están descritos con palabras y números dentro de cada ejercicio.",
    use="Aprenderé a resolver casos nuevos: barras entre dos marcas, datos que se agregan, datos que faltan y cambios en la escala. Sirve para leer y completar gráficos aunque el caso sea distinto.",
    prior=["Sé leer gráficos de barras y de línea.", "Sé hallar la mitad entre dos números."],
    explain=[
        "A veces una barra queda justo en la mitad entre dos marcas. Si las marcas suben de 20 en 20 y la barra queda entre la 60 y la 80, su valor está en el medio: 60 + 10 = 70. La mitad de 20 es 10. Así se lee un valor exacto cuando no coincide con una marca.",
        "Si se agrega un dato nuevo que es mayor que el último número de la escala, hay que alargar el eje. Por ejemplo, con un dato de 110 y una escala que llega a 100, hay que agregar la marca 120. Cuando los datos son grandes, se elige una escala que suba de a más, como de 20 en 20.",
        "Si falta un dato en una tabla y se conoce el total, se resta al total los datos conocidos. Si el total es 180 y los datos conocidos suman 125, falta 180 − 125 = 55. Siempre comprueba sumando de nuevo todos los datos.",
    ],
    vocab=[("mitad entre dos marcas", "valor que queda justo en el medio de dos marcas de la escala"), ("alargar el eje", "agregar más marcas para que quepan los datos"), ("dato faltante", "valor que no está en la tabla o el gráfico"), ("total", "suma de todos los datos")],
    worked=[
        {"title": "Una barra entre dos marcas", "problem": AGUA + " ¿Cuántos litros se usaron el martes?", "steps": ["La barra queda justo a la mitad entre 60 y 80.", "La mitad de 20 es 10, y 60 + 10 = 70."], "answer": "Se usaron 70 litros"},
        {"title": "Un dato faltante", "problem": "Tabla «Libros leídos»: marzo 30, abril ?, mayo 50, junio 45. El total es 180. ¿Cuántos libros se leyeron en abril?", "steps": ["Sumo los datos conocidos: 30 + 50 + 45 = 125.", "Resto al total: 180 − 125 = 55."], "answer": "Se leyeron 55 libros en abril"},
    ],
    mistakes=[
        {"wrong": "Leer una barra que queda entre 60 y 80 como 80.", "why": "Se elige la marca más cercana sin calcular.", "fix": "Si queda justo a la mitad, el valor es 70."},
        {"wrong": "Dibujar una barra de 110 en un eje que llega a 100.", "why": "No se alarga el eje cuando el dato es mayor.", "fix": "Agrega la marca 120 al eje antes de dibujar la barra."},
    ],
    tiers={
        "recovery": [
            ex(AGUA + " ¿Cuántos litros se usaron el lunes?", "80", "La barra llega a la marca 80."),
            ex(AGUA + " ¿Cuántos litros se usaron el miércoles?", "100", "La barra llega a la marca 100."),
            ex(AGUA + " ¿De cuánto en cuánto sube la escala?", "De 20 en 20", "Las marcas son 0, 20, 40, 60, 80, 100 y 120."),
        ],
        "understand": [
            ex(AGUA + " ¿Cuántos litros se usaron el martes?", "70", "Queda a la mitad entre 60 y 80."),
            ex(AGUA + " ¿Cuántos litros se usaron el jueves?", "90", "Queda a la mitad entre 80 y 100."),
            ex(AGUA + " ¿Qué día se usó menos agua?", "Viernes", "Su barra llega solo a 40."),
        ],
        "apply": [
            ex(AGUA + " El sábado se usaron 110 litros. ¿Dónde queda la barra del sábado?", "A la mitad entre las marcas 100 y 120", "110 está en el medio de 100 y 120."),
            ex(AGUA + " Si el eje vertical solo llegara hasta 100, ¿cabría la barra del sábado, que vale 110 litros?", "No", "110 es mayor que 100."),
            arith(AGUA + " ¿Cuántos litros se usaron de lunes a viernes?", "80+70+100+90+40", "Se suman los cinco días.", " litros"),
        ],
        "reason": [
            ex("Con una escala de 20 en 20, una barra llega a la cuarta marca después del 0 y vale 80. Si la escala cambia a 10 en 10, ¿a qué marca después del 0 llega esa barra?", "A la octava marca", "80 dividido en marcas de 10 son 8 marcas."),
            ex(AGUA + " Pedro dice que el martes vale 60 porque la barra no alcanzó la marca 80. ¿Qué error tiene?", "Olvidó que queda a la mitad entre 60 y 80; vale 70", "La barra pasó la marca 60."),
        ],
        "challenge": [
            arith("Tabla «Libros leídos»: marzo 30, abril ?, mayo 50, junio 45. El total es 180. ¿Cuántos libros se leyeron en abril?", "180-30-50-45", "Se restan al total los datos conocidos.", " libros"),
            arith("Un eje vertical va de 10 en 10 hasta 130. ¿Cuántas marcas tiene sin contar el 0?", "130//10", "Se divide 130 por lo que sube cada marca.", " marcas"),
        ],
    },
    context=[ex("Un curso recicló botellas: lunes 120, martes 90 y miércoles 150. Para un gráfico de barras con marcas de 50 en 50, ¿hasta qué marca debe llegar el eje como mínimo?", "150", "La barra mayor llega a 150.")],
    selfcheck=[
        ex("Una barra queda justo a la mitad entre las marcas 40 y 60. ¿Cuánto vale?", "50", "40 + 10 = 50.", calc="40+10"),
        ex("Un total es 100 y se conocen dos datos: 35 y 40. ¿Cuánto vale el dato que falta?", "25", "100 − 35 − 40 = 25.", calc="100-35-40"),
        ex(AGUA + " ¿Qué día se usó más agua?", "Miércoles", "Su barra llega a 100."),
    ],
    open_task=task(
        "Usa este caso: gráfico de barras con escala de 20 en 20 hasta 120. Hay 4 datos: A llega a 40, B queda justo a la mitad entre 80 y 100, C llega a 120 y D queda justo a la mitad entre 20 y 40. Escribe los cuatro valores. Después agrega un quinto dato E de 70 y explica entre qué marcas queda su barra.",
        "A 40, B 90, C 120, D 30. E de 70 queda a la mitad entre las marcas 60 y 80.",
        ["los cuatro valores son 40, 90, 120 y 30", "explica el cálculo de la mitad", "ubica E entre 60 y 80"],
        ["cuatro valores", "ubicación de E"],
        ["aproximar a la marca más cercana", "olvidar calcular la mitad"],
        "Pide decir cuánto es la mitad entre las marcas. Reconoce el cálculo exacto.",
    ),
    reinforce="Mira una regla y di a qué número llega un lápiz que termina justo a la mitad entre el 10 y el 20.",
    extend="Inventa una tabla con un dato faltante y un total, y escribe cómo se calcula el dato que falta.",
)

register(
    OA26, 5,
    materials="Lápiz y papel. La tabla está escrita en cada ejercicio.",
    use="Aprenderé a comprobar mis lecturas, a comparar dos conjuntos de datos y a escribir conclusiones que los datos sí apoyan. Sirve para comunicar lo que dice un gráfico sin inventar.",
    prior=["Sé leer tablas y gráficos de barras y de línea.", "Sé sumar y restar para comparar datos."],
    explain=[
        "Para comparar dos conjuntos de datos, mira cada fila con la misma pregunta: ¿cuál es mayor?, ¿cuánto más?, ¿cuánto suman? Primero lee todos los datos y luego calcula. Así evitas decir algo que solo es cierto en una parte de la tabla.",
        "Una conclusión es una frase que dice lo que descubres, apoyada en los números. «5.º A leyó 80 minutos más que 5.º B en total» es una conclusión que se puede comprobar. «5.º A es el mejor curso» no se puede comprobar con la tabla, porque nada en ella dice cuál curso es mejor.",
        "También hay que separar los datos de las predicciones. Un dato está en la tabla o el gráfico. Una predicción es una suposición sobre lo que pasará, y puede fallar. Si no hay un punto medido entre dos puntos, el valor entre ellos es solo una estimación. Siempre comprueba tu lectura volviendo a mirar los números.",
    ],
    vocab=[("conclusión", "frase que dice lo que descubres y se apoya en los datos"), ("comprobar", "revisar los números para ver si lo que dije es verdad"), ("predicción", "suposición sobre lo que pasará, no un dato"), ("estimación", "valor aproximado que no fue medido")],
    worked=[
        {"title": "Comparar totales", "problem": LECTURA + " ¿Qué curso leyó más minutos en total?", "steps": ["5.º A: 60 + 90 + 120 + 150 = 420.", "5.º B: 80 + 70 + 90 + 100 = 340."], "answer": "5.º A leyó más: 420 contra 340 minutos"},
        {"title": "Revisar una conclusión", "problem": LECTURA + " Un compañero dice: «5.º A siempre leyó más que 5.º B». ¿Los datos lo apoyan?", "steps": ["En la semana 1, 5.º A leyó 60 y 5.º B leyó 80.", "Entonces hay una semana en que 5.º B leyó más."], "answer": "No lo apoyan, porque en la semana 1 leyó más 5.º B"},
    ],
    mistakes=[
        {"wrong": "Afirmar que 5.º A leerá 180 minutos la semana 5 como si fuera un dato.", "why": "Se confunde una predicción con un dato.", "fix": "Di que es una predicción y que no está en la tabla."},
        {"wrong": "Escribir una conclusión sin ningún número.", "why": "No se puede comprobar con los datos.", "fix": "Apoya la conclusión con los números de la tabla."},
    ],
    tiers={
        "recovery": [
            ex(LECTURA + " ¿Cuántos minutos leyó 5.º B en la semana 3?", "90", "Está en la fila de la semana 3."),
            ex(LECTURA + " ¿Qué curso leyó más en la semana 1?", "5.º B", "Leyó 80 y 5.º A leyó 60."),
            arith(LECTURA + " ¿Cuántos minutos leyó 5.º A en las 4 semanas?", "60+90+120+150", "Se suman las cuatro semanas.", " minutos"),
        ],
        "understand": [
            arith(LECTURA + " ¿Cuántos minutos leyó 5.º B en las 4 semanas?", "80+70+90+100", "Se suman las cuatro semanas.", " minutos"),
            ex(LECTURA + " ¿Qué curso leyó más en total?", "5.º A", "Leyó 420 y 5.º B leyó 340."),
            ex(LECTURA + " ¿En cuántas semanas leyó más 5.º A que 5.º B?", "3", "En las semanas 2, 3 y 4."),
        ],
        "apply": [
            arith(LECTURA + " ¿Cuántos minutos más leyó 5.º A que 5.º B en total?", "420-340", "Se resta el total menor al mayor.", " minutos"),
            arith(LECTURA + " ¿Cuántos minutos aumentó 5.º A entre la semana 1 y la semana 4?", "150-60", "Se resta el valor menor al mayor.", " minutos"),
            ex(LECTURA + " ¿Es verdadero o falso: «5.º B leyó más cada semana que la anterior»?", "Falso", "Bajó de 80 a 70 en la semana 2."),
        ],
        "reason": [
            ex(LECTURA + " Una conclusión dice: «5.º A siempre leyó más que 5.º B». ¿Los datos la apoyan?", "No; en la semana 1 leyó más 5.º B", "Hay una semana en que ocurre lo contrario."),
            ex(LECTURA + " Lía dice que 5.º A leerá 180 minutos la semana 5 porque cada semana aumenta 30. ¿Es un dato de la tabla?", "No; es una predicción", "La semana 5 no está en la tabla."),
        ],
        "challenge": [
            ex("En un gráfico de línea, el punto de las 12 h está en 18 grados y el de las 14 h en 24 grados. Un compañero dice que a las 13 h hubo exactamente 21 grados. ¿Los datos lo prueban?", "No; es solo una estimación, no se midió", "El gráfico no tiene un punto para las 13 h."),
            ex(LECTURA + " ¿Qué conclusión apoya la tabla? A) 5.º A lee más porque es mejor curso. B) De la semana 1 a la 4, 5.º A aumentó 90 minutos y 5.º B aumentó 20. C) 5.º B no lee.", "B", "5.º A: 150 − 60 = 90. 5.º B: 100 − 80 = 20."),
        ],
    },
    context=[ex("En una feria se vendieron 40 jugos el sábado y 25 el domingo. ¿Qué conclusión apoyan los datos? A) El sábado se vendieron 15 jugos más que el domingo. B) El lunes se venderán 10 jugos.", "A", "40 − 25 = 15; B es una predicción.")],
    selfcheck=[
        ex("Una conclusión sin números, ¿se puede comprobar con la tabla?", "No", "No hay datos con los que revisarla."),
        ex(LECTURA + " ¿Cuántos minutos leyó 5.º B en la semana 4?", "100", "Está en la fila de la semana 4."),
        ex("¿Un valor que no fue medido es un dato o una estimación?", "Una estimación", "Un dato se mide o se anota."),
    ],
    open_task=task(
        "Usa la tabla: " + LECTURA + " Escribe un párrafo de tres frases con tus conclusiones: una que compare los totales, una que compare el crecimiento entre la semana 1 y la 4, y una que sea una predicción claramente señalada como predicción. Calcula los números antes de escribir.",
        "5.º A leyó 420 minutos y 5.º B leyó 340, 80 minutos menos. De la semana 1 a la 4, 5.º A subió 90 minutos y 5.º B subió 20. Predicción: si sigue igual, 5.º A podría leer más de 150 minutos en la semana 5.",
        ["compara los totales con números", "compara el aumento con números", "señala la predicción como predicción", "los cálculos son correctos"],
        ["tres frases", "cálculos"],
        ["presentar una predicción como dato", "conclusiones sin números"],
        "Pide mostrar los cálculos de cada número del párrafo. Reconoce que separe datos de predicciones.",
    ),
    reinforce="Elige un gráfico de un diario y escribe dos conclusiones que los datos apoyen.",
    extend="Escribe una conclusión que los datos no apoyen y otra que sí, a partir de la misma tabla, y explica la diferencia.",
)
