"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 1 (parte 2): OAD-02, datos e información geográfica (demografía y economía) del siglo XIX. Todo se trabaja con tablas inventadas («de ejemplo») descritas en papel, sin mapas."""
from __future__ import annotations

from epja_hgcs_nm1_a_common import build, PRIOR_BASE

O = "EPJA-HGCS-NM1-OAD-02"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Tabla de habitantes de tres ciudades ficticias. Fuente: censos de ejemplo de cada fecha. "
      "Puerto Alba: 8.000 habitantes en 1800, 12.000 en 1850 y 40.000 en 1900. "
      "Villa Cobre: 2.000 habitantes en 1800, 3.000 en 1850 y 15.000 en 1900. "
      "Valle Verde: 10.000 habitantes en 1800, 11.000 en 1850 y 12.000 en 1900.")
build(
    O, 1, F1,
    use="Hoy aprendo a leer una tabla de datos geográficos y a reconocer sus variables, empezando por tablas parecidas a las que ya ves en una boleta o en un informe.",
    prior=PRIOR_BASE + ["Sé sumar, restar y leer números con punto de mil, como 12.000."],
    explain=[
        "Ya lees tablas todos los días: la boleta de luz muestra el mes y el consumo, y una lista de turnos muestra el día y la hora. En Geografía y en Historia se usan tablas para guardar datos sobre los lugares y las personas. Cada dato es un valor concreto, como «12.000 habitantes».",
        "Una variable es una característica que puede cambiar de un caso a otro. En la tabla de la ficha hay tres variables: la ciudad (un nombre), el año (un momento) y los habitantes (una cantidad que se mide en personas). Una variable de cantidad se llama cuantitativa; una de nombre o categoría se llama cualitativa.",
        "Antes de interpretar una tabla se lee su título, sus unidades y su fuente. La fuente dice de dónde vienen los datos y permite juzgar si son confiables. La demografía es el estudio de la población: cuántas personas hay, dónde viven y cómo cambia su número.",
    ],
    vocab=[("dato", "valor concreto que entrega una tabla, como 12.000 habitantes"), ("variable", "característica que puede cambiar de un caso a otro: ciudad, año, habitantes"), ("variable cuantitativa", "variable que se mide con una cantidad"), ("demografía", "estudio de cuántas personas hay y cómo cambia su número"), ("fuente de los datos", "origen de la información: un censo, un registro")],
    worked=[
        ("Reconocer variables", "{F} ¿Qué variables tiene la tabla y cuál es cuantitativa?", ["Reviso las columnas y filas: hay ciudad, año y habitantes.", "La ciudad es un nombre (cualitativa) y el año un momento; los habitantes se miden con una cantidad."], "Ciudad, año y habitantes; la cuantitativa es habitantes"),
        ("Leer un dato y su cambio", "{F} ¿Cuántos habitantes más tenía Puerto Alba en 1900 que en 1850?", ["Leo los datos: 40.000 en 1900 y 12.000 en 1850.", "Resto: 40.000 menos 12.000 es 28.000."], "28.000 habitantes más"),
    ],
    mistakes=[("Leer solo la última columna y olvidar los años anteriores.", "Se mira el dato más reciente y se pierde el cambio en el tiempo.", "Lee cada fila completa y compara sus valores."),
              ("Dejar fuera la unidad de medida.", "Se piensa que el número «habla solo».", "Anota siempre la unidad, aquí «habitantes».")],
    T=[
        ("abc", "{F} ¿Cuál es una variable cuantitativa de la tabla?", "Los habitantes", "El nombre de la ciudad", "El título de la tabla", "Los habitantes se miden con una cantidad; el nombre de la ciudad es una categoría."),
        ("ab", "{F} ¿Qué variable indica el momento del dato?", "El año", "La ciudad", "El año ubica cada dato en el tiempo."),
        ("{F} ¿Cuántos habitantes tenía Puerto Alba en 1850?", "12.000", "El dato de Puerto Alba en la columna 1850 es 12.000."),
        ("=", "{F} ¿Cuántos habitantes más tenía Villa Cobre en 1900 que en 1850?", "15000-3000", "Se restan los habitantes de 1900 y de 1850 para ver el aumento.", " habitantes"),
        ("=", "{F} ¿Cuántos habitantes sumaban las tres ciudades en 1800?", "8000+2000+10000", "Se suman los habitantes de las tres ciudades en el mismo año.", " habitantes"),
        ("abc", "{F} ¿Qué ciudad aumentó más su número de habitantes entre 1850 y 1900?", "Puerto Alba", "Villa Cobre", "Valle Verde", "Puerto Alba aumentó 28.000, más que Villa Cobre (12.000) y Valle Verde (1.000)."),
        ("ab", "En Geografía: ¿en qué unidad se mide la población de una ciudad?", "En habitantes", "En kilómetros", "La población se cuenta en personas, es decir, habitantes."),
        ("=", "{F} ¿Cuántos habitantes más tenía Valle Verde en 1900 que en 1800?", "12000-10000", "La diferencia entre el dato final y el inicial muestra el aumento.", " habitantes"),
        ("abc", "{F} ¿Qué se observa en Valle Verde a lo largo de los tres años?", "Casi no crece", "Crece muchísimo", "Disminuye cada año", "Pasa de 10.000 a 11.000 y a 12.000, un aumento muy pequeño."),
        ("abc", "{F} ¿Qué pregunta de investigación sugiere que Puerto Alba y Villa Cobre crecieron mucho?", "¿Qué actividad atrajo a más personas a esas ciudades?", "¿Qué nombre tenían las calles en 1800?", "¿Cuántas calles tiene Valle Verde?", "Un crecimiento tan grande invita a preguntar por sus posibles causas económicas."),
        ("ab", "{F} Un vecino afirma: «Valle Verde es la ciudad más poblada en 1900». ¿Qué dice la tabla?", "Que no, pues Puerto Alba tiene 40.000", "Que sí, pues tiene 12.000", "En 1900 Puerto Alba (40.000) supera a Valle Verde (12.000), por eso la afirmación es falsa."),
        ("abc", "{F} ¿Qué se puede afirmar con seguridad con esta tabla?", "Que Puerto Alba y Villa Cobre crecieron más que Valle Verde", "La razón por la que crecieron", "Que Valle Verde tiene menos terreno", "La tabla solo muestra cuántos habitantes había; no explica causas ni extensión de terreno."),
        ("abc", "{F} ¿Cómo se sabe de dónde vienen los datos de la tabla?", "Por la fuente: censos de ejemplo de cada fecha", "Por el nombre de las ciudades", "Por el número de habitantes", "La ficha anota la fuente de los datos y eso permite juzgar su origen."),
    ],
    ctx=("abc", "Una dirigente de la junta de vecinos de ejemplo revisa una tabla de la boleta de luz: «Enero: 120 kWh; febrero: 100 kWh; marzo: 140 kWh». ¿Cuál es la variable cuantitativa?", "El consumo en kWh", "El nombre del mes", "El título de la boleta", "El consumo se mide con una cantidad en kWh; el mes es solo la categoría de tiempo."),
    sc=[("En Geografía: ¿qué es una variable?", "Una característica que puede cambiar de un caso a otro", "Las variables son lo que se mide o se registra en una tabla."),
        ("¿Qué estudia la demografía?", "Cuántas personas hay y cómo cambia su número", "La población es el centro de la demografía."),
        ("¿Para qué sirve anotar la fuente de los datos?", "Para saber de dónde vienen y si son confiables", "La fuente permite juzgar la calidad de la información.")],
    op=("Lee esta tabla de ejemplo (fuente: registro municipal de ejemplo): «Pueblo Seco: 1.000 habitantes en 1850 y 3.000 en 1900. Pueblo Lluvia: 2.000 habitantes en 1850 y 2.500 en 1900». "
        "Escribe las variables, di cuál es cuantitativa, calcula cuántos habitantes aumentó cada pueblo y anota una pregunta que te gustaría investigar.",
        "Variables: pueblo, año y habitantes; la cuantitativa es habitantes. Pueblo Seco aumentó 2.000 y Pueblo Lluvia 500. Pregunta: ¿qué actividad pudo hacer crecer más a Pueblo Seco?",
        ["identifica las tres variables", "calcula bien las diferencias", "plantea una pregunta sin dar una causa como cierta"],
        ["una lista de variables, dos cálculos y una pregunta"], ["olvidar la unidad", "afirmar una causa sin evidencia"],
        "Pregunta: «¿Qué dato de la tabla respalda tu frase?»."),
    reinforce="Mira una tabla de tu casa (una cuenta, un horario) y anota sus variables y cuál es cuantitativa.",
    extend="Explica con un ejemplo por qué una tabla muestra datos, pero no explica por qué ocurrieron.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Tabla de una región ficticia de 500 kilómetros cuadrados (km²). Fuente: censos de ejemplo. "
      "Año 1850: población urbana (vive en ciudades) 20.000 habitantes; población rural (vive en el campo) 80.000 habitantes. "
      "Año 1900: población urbana 90.000 habitantes; población rural 110.000 habitantes. "
      "Dato adicional: densidad de población = habitantes divididos por la superficie en km².")
build(
    O, 2, F2,
    use="Hoy aprendo palabras para describir datos de población (urbano, rural, densidad, porcentaje, tendencia, patrón) y las uso con una tabla.",
    prior=PRIOR_BASE + ["Sé leer una tabla, identificar sus variables y restar para ver un aumento."],
    explain=[
        "La población urbana es la que vive en ciudades y la rural la que vive en el campo. La suma de ambas es la población total. La densidad de población muestra cuántos habitantes hay por cada kilómetro cuadrado y se calcula dividiendo la población total por la superficie.",
        "Un porcentaje es una parte de cada cien. Si 20.000 de 100.000 personas viven en ciudades, son 20 de cada 100, es decir, el 20 %. El porcentaje permite comparar cosas de distinto tamaño, como una región pequeña con una grande, porque lleva todo a una misma base de cien.",
        "Una tendencia es la dirección en que van los datos: si crecen, decrecen o se mantienen. Un patrón es una regularidad que se repite, como «las ciudades con puerto crecen más». Durante el siglo XIX, por la industrialización, muchas personas migraron del campo a la ciudad, y por eso crecieron las poblaciones urbanas.",
    ],
    vocab=[("población urbana", "personas que viven en ciudades"), ("población rural", "personas que viven en el campo"), ("densidad de población", "habitantes por kilómetro cuadrado"), ("porcentaje", "parte de cada cien"), ("tendencia", "dirección en que van los datos: crece, decrece o se mantiene")],
    worked=[
        ("Calcular una densidad", "{F} ¿Cuál era la densidad de población en 1850?", ["Sumo la población total de 1850: 20.000 más 80.000, que da 100.000 habitantes.", "Divido por la superficie: 100.000 entre 500."], "200 habitantes por km²"),
        ("Calcular un porcentaje", "{F} ¿Qué porcentaje de la población vivía en ciudades en 1850?", ["La población urbana era 20.000 y el total, 100.000.", "20.000 entre 100.000 es 0,2, es decir, 20 de cada 100."], "20 %"),
    ],
    mistakes=[("Comparar solo cantidades de población sin tener en cuenta el tamaño del territorio.", "Dos lugares con la misma cantidad de habitantes pueden tener densidades muy distintas.", "Calcula la densidad para comparar territorios de distinto tamaño."),
              ("Confundir el aumento de la población urbana con el aumento del porcentaje urbano.", "Una cantidad puede subir mientras el porcentaje se mantiene o baja.", "Calcula siempre las dos cosas.")],
    T=[
        ("abc", "{F} ¿Cómo se llama la población que vive en ciudades?", "Urbana", "Rural", "Total", "La población urbana es la que vive en ciudades; la rural vive en el campo."),
        ("ab", "En Geografía: ¿qué es la densidad de población?", "Habitantes por kilómetro cuadrado", "Total de habitantes de una ciudad", "La densidad relaciona la población con el espacio que ocupa."),
        ("{F} ¿Cuál era la población rural en 1900?", "110.000 habitantes", "La ficha indica 110.000 habitantes rurales en 1900."),
        ("=", "{F} ¿Cuál era la población total de la región en 1900?", "90000+110000", "La población total es la suma de la urbana y la rural.", " habitantes"),
        ("=", "{F} ¿Cuál era la densidad de población en 1900, en habitantes por km²?", "200000//500", "Se divide la población total por la superficie de 500 km².", " habitantes por km²"),
        ("abc", "{F} ¿Qué tendencia muestra la población urbana entre 1850 y 1900?", "Crece", "Decrece", "Se mantiene", "Pasa de 20.000 a 90.000, es decir, aumenta."),
        ("=", "{F} ¿Qué porcentaje de la población vivía en ciudades en 1900?", "90000*100//200000", "Se divide la población urbana por el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué cambio muestra el porcentaje urbano entre 1850 (20 %) y 1900 (45 %)?", "Una parte mayor de la población vivía en ciudades", "Una parte menor vivía en ciudades", "No cambió el porcentaje", "Pasar de 20 % a 45 % significa que más de cada cien personas vivían en ciudades."),
        ("abc", "{F} Un vecino dice: «La población rural disminuyó entre 1850 y 1900». ¿Qué dice la tabla?", "Que aumentó de 80.000 a 110.000", "Que disminuyó a 20.000", "Que desapareció", "La población rural pasó de 80.000 a 110.000, así que la afirmación es falsa."),
        ("abc", "{F} ¿Qué patrón se observa en el crecimiento de la población?", "La urbana crece más rápido que la rural", "La rural crece más rápido que la urbana", "Ambas decrecen", "La urbana se multiplicó por 4,5 y la rural por menos de 2; por eso crece más rápido."),
        ("ab", "{F} ¿Qué proceso del siglo XIX ayuda a explicar el patrón urbano?", "La industrialización, que atrajo gente del campo a la ciudad", "La Conferencia de Berlín, que reunió a potencias europeas", "La industrialización atrajo trabajadores a las ciudades; el dato de la tabla coincide con ese proceso."),
        ("abc", "Una región A tiene 1.000 habitantes en 10 km² y una región B tiene 1.000 habitantes en 100 km². ¿Cuál tiene mayor densidad?", "La región A, con 100 habitantes por km²", "La región B, con 10 habitantes por km²", "Tienen la misma densidad", "A: 1.000 entre 10 es 100; B: 1.000 entre 100 es 10; por eso A tiene mayor densidad."),
        ("abc", "{F} ¿Qué falta para saber por qué creció tanto la población urbana?", "Más información sobre las causas, como fuentes sobre empleo y migración", "Nada, la tabla ya explica la causa", "Más datos sobre el número de calles de cada ciudad", "La tabla describe un cambio, pero no dice por qué ocurrió."),
    ],
    ctx=("abc", "Un equipo municipal de ejemplo compara dos poblaciones: la comuna A tiene 10.000 habitantes en 50 km² y la comuna B, 10.000 habitantes en 25 km². ¿Cuál tiene mayor densidad?", "La comuna B, con 400 habitantes por km²", "La comuna A, con 200 habitantes por km²", "Tienen la misma densidad", "B: 10.000 entre 25 es 400; A: 10.000 entre 50 es 200; B es más densa."),
    sc=[("En datos geográficos: ¿cómo se define un porcentaje?", "Una parte de cada cien", "El porcentaje lleva una cantidad a una base de cien."),
        ("En demografía histórica: ¿cómo se obtiene la densidad de una región?", "Dividiendo los habitantes por la superficie", "Esa división da habitantes por km²."),
        ("Al leer una tabla de población: ¿qué es una tendencia?", "La dirección en que van los datos", "La tendencia dice si crecen, decrecen o se mantienen.")],
    op=("Lee estos datos de ejemplo (fuente: registro municipal de ejemplo). Comuna Lomas, superficie 100 km²: 1850, 5.000 habitantes (1.000 urbanos y 4.000 rurales); 1900, 15.000 habitantes (9.000 urbanos y 6.000 rurales). "
        "Calcula la densidad de 1850 y 1900, el porcentaje urbano de 1850 y 1900, y escribe una frase que describa la tendencia.",
        "Densidad 1850: 5.000 entre 100 es 50 habitantes por km²; 1900: 15.000 entre 100 es 150. Porcentaje urbano 1850: 1.000 de 5.000 es 20 %; 1900: 9.000 de 15.000 es 60 %. Tendencia: la población total y la urbana crecieron, y la ciudad pasó a reunir más de la mitad de los habitantes.",
        ["calcula bien las densidades", "calcula bien los porcentajes", "describe la tendencia sin inventar causas"],
        ["cuatro cálculos y una frase"], ["dividir por un número equivocado", "confundir cantidad y porcentaje"],
        "Pregunta: «¿Dividiste el dato correcto por la superficie o por el total?»."),
    reinforce="Calcula la densidad de una comuna de ejemplo con 6.000 habitantes y 20 km², y escribe qué significa el resultado.",
    extend="Explica con un ejemplo por qué el porcentaje urbano puede subir aunque la población rural también crezca.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Tabla de un país ficticio, fuente: informe económico de ejemplo. "
      "Año 1860: 100 km de ferrocarril; 50 mil toneladas exportadas. "
      "Año 1870: 300 km de ferrocarril; 100 mil toneladas exportadas. "
      "Año 1880: 600 km de ferrocarril; 150 mil toneladas exportadas. "
      "Año 1890: 900 km de ferrocarril; 300 mil toneladas exportadas.")
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a describir una tabla de datos: leer título y fuente, calcular el cambio y el porcentaje, y nombrar un patrón.",
    prior=PRIOR_BASE + ["Sé calcular una diferencia, una densidad y un porcentaje simple."],
    explain=[
        "Para analizar datos hay un camino de cinco pasos. Paso 1: lee el título, las unidades y la fuente. Paso 2: identifica las variables. Paso 3: calcula el cambio entre dos momentos restando el valor inicial al final. Paso 4: calcula el porcentaje de cambio. Paso 5: describe el patrón con una frase.",
        "El porcentaje de cambio se calcula dividiendo el aumento por el valor inicial y multiplicando por 100. Por ejemplo, si el ferrocarril pasó de 100 a 300 km, aumentó 200 km, y 200 entre 100 es 2, es decir, un 200 %. Este número permite comparar dos variables que se miden en unidades distintas, como kilómetros y toneladas.",
        "Un patrón puede ser que dos variables suban juntas. Pero atención: que suban juntas no prueba que una cause la otra. Para afirmar una causa se necesitan fuentes que expliquen la relación, como cartas, informes o relatos de la época. Por eso un buen análisis termina con una pregunta pendiente.",
    ],
    vocab=[("diferencia", "resultado de restar el valor inicial al valor final"), ("porcentaje de cambio", "aumento dividido por el valor inicial, por 100"), ("patrón", "regularidad que se repite en los datos"), ("relación", "forma en que dos datos suben o bajan juntos"), ("causa", "razón que produce un hecho y que se prueba con evidencia")],
    worked=[
        ("Calcular una diferencia", "{F} ¿Cuántos kilómetros de ferrocarril se agregaron entre 1860 y 1890?", ["Leo el valor final, 900, y el inicial, 100.", "Resto 900 menos 100."], "800 km"),
        ("Calcular un porcentaje de cambio", "{F} ¿Cuánto aumentaron las toneladas exportadas entre 1860 y 1870, en porcentaje?", ["El aumento es 100 menos 50, es decir, 50 mil toneladas.", "Divido 50 entre 50, que es 1, y multiplico por 100."], "100 %"),
    ],
    mistakes=[("Calcular el porcentaje dividiendo por el valor final.", "Se toma el dato que se ve más grande.", "Divide siempre por el valor inicial."),
              ("Afirmar que el ferrocarril causó las exportaciones porque ambos crecieron.", "Se confunde relación con causa.", "Escribe que están relacionadas y busca fuentes que expliquen el vínculo.")],
    T=[
        ("abc", "{F} ¿Cuál es el primer paso para analizar datos?", "Leer el título, las unidades y la fuente", "Calcular el porcentaje", "Escribir la conclusión", "Se parte por saber qué miden los datos y de dónde vienen."),
        ("ab", "{F} ¿Qué variable mide la tabla en kilómetros?", "El ferrocarril", "Las exportaciones", "El ferrocarril se mide en km y las exportaciones, en toneladas."),
        ("{F} ¿Cuántas toneladas se exportaron en 1880?", "150 mil", "La ficha indica 150 mil toneladas en 1880."),
        ("=", "{F} ¿Cuántos kilómetros de ferrocarril se agregaron entre 1870 y 1880?", "600-300", "Se resta el valor inicial al final para obtener el aumento.", " km"),
        ("=", "{F} ¿Cuántas mil toneladas más se exportaron en 1890 que en 1860?", "300-50", "La diferencia entre el valor de 1890 y el de 1860 muestra el aumento.", " mil toneladas"),
        ("=", "{F} ¿En qué porcentaje aumentó el ferrocarril entre 1870 y 1880?", "(600-300)*100//300", "Se divide el aumento por el valor inicial y se multiplica por 100.", " %"),
        ("=", "{F} ¿En qué porcentaje aumentaron las toneladas exportadas entre 1880 y 1890?", "(300-150)*100//150", "El aumento de 150 sobre un valor inicial de 150 es un 100 %.", " %"),
        ("abc", "{F} ¿Qué patrón se observa en las dos variables entre 1860 y 1890?", "Ambas aumentan en todos los años", "Ambas disminuyen", "El ferrocarril sube y las exportaciones bajan", "Los kilómetros y las toneladas crecen en cada fecha de la tabla."),
        ("abc", "{F} Una persona dice: «Entre 1870 y 1880 las toneladas crecieron un 100 %». ¿Qué dice la tabla?", "Que crecieron un 50 %, porque pasaron de 100 a 150", "Que crecieron un 100 % como dice", "Que no crecieron", "El aumento es 50 sobre 100 inicial, un 50 %; el 100 % corresponde a otro periodo."),
        ("abc", "{F} ¿Qué se puede afirmar con seguridad sobre la relación entre ferrocarril y exportaciones?", "Ambos aumentaron en los mismos años", "El ferrocarril causó el aumento de exportaciones", "Las exportaciones causaron el aumento del ferrocarril", "Con una tabla se ve que suben juntos, pero no se prueba una causa."),
        ("ab", "{F} Para afirmar que el ferrocarril permitió exportar más, ¿qué se necesita?", "Fuentes de la época que expliquen la relación", "Solo mirar de nuevo la tabla", "La tabla muestra que ambos suben, pero la causa se prueba con otras fuentes."),
        ("abc", "{F} Si se agrega el dato «1890: 5 puertos habilitados», ¿qué pregunta nueva surge?", "¿Cómo se relacionan los puertos con el ferrocarril y las exportaciones?", "¿Cuántos pasajeros cabían en cada vagón?", "¿Qué nombre tenía cada locomotora?", "Los puertos son otro elemento del sistema de exportación y se pueden relacionar con los otros dos datos."),
        ("abc", "{F} ¿Cuál es una frase que describe bien el patrón sin inventar causas?", "El ferrocarril y las exportaciones crecieron juntos entre 1860 y 1890", "Las exportaciones crecieron porque el ferrocarril lo permitió", "El ferrocarril fue lo único que importó", "Es la única frase que se apoya solo en los datos de la tabla."),
    ],
    ctx=("abc", "El comité de una cooperativa de ejemplo compara dos años: en 2010 vendían 400 kilos de miel y en 2020, 800 kilos. ¿En qué porcentaje aumentaron las ventas?", "En un 100 %", "En un 50 %", "En un 200 %", "El aumento es 400 sobre un valor inicial de 400; eso es un 100 %."),
    sc=[("¿Cómo se calcula el porcentaje de cambio?", "Aumento dividido por el valor inicial, por 100", "Se divide por el valor inicial para tener una base."),
        ("¿Que dos datos suban juntos prueba una causa?", "No, solo muestra una relación", "La causa se prueba con fuentes que expliquen el vínculo."),
        ("¿Cuál es el último paso del análisis?", "Describir el patrón y dejar una pregunta pendiente", "Un buen análisis termina con una conclusión y una pregunta.")],
    op=("Analiza esta tabla de ejemplo (fuente: informe de una compañía de ejemplo): «Puerto Mar: 1880, 2 muelles y 1.000 personas empleadas; 1890, 4 muelles y 3.000 personas empleadas; 1900, 8 muelles y 6.000 personas empleadas». "
        "Calcula la diferencia de muelles entre 1880 y 1900, el porcentaje de aumento de las personas empleadas entre 1880 y 1890, describe el patrón y escribe una pregunta pendiente.",
        "Muelles: 8 menos 2 son 6 más. Empleo 1880 a 1890: aumento de 2.000 sobre 1.000 es 200 %. Patrón: los muelles y el empleo aumentaron en todos los años. Pregunta: ¿qué tipo de mercaderías explicaba tanto trabajo en el puerto?",
        ["usa bien la diferencia y el porcentaje", "describe el patrón con los datos", "no afirma causas sin fuente"],
        ["dos cálculos, una frase de patrón y una pregunta"], ["dividir por el valor final", "afirmar una causa"],
        "Pregunta: «¿Esta frase muestra una relación o afirma una causa?»."),
    reinforce="Calcula el porcentaje de aumento si una cuenta pasó de $20.000 a $30.000 y escribe qué significa.",
    extend="Explica con un ejemplo de la vida diaria dos cosas que suben juntas sin que una cause la otra.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Tabla de cuatro ciudades ficticias, años 1850 y 1900. Fuente: censos de ejemplo. "
      "Puerto Alba (en la costa, con estación de ferrocarril): 12.000 habitantes en 1850 y 40.000 en 1900. "
      "Villa Cobre (en el interior, con estación de ferrocarril): 3.000 en 1850 y 15.000 en 1900. "
      "Valle Verde (en el interior, sin ferrocarril): 11.000 en 1850 y 12.000 en 1900. "
      "Lomas Altas (en la costa, sin ferrocarril): 5.000 en 1850 y 6.000 en 1900.")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo comparar grupos de datos geográficos para encontrar un patrón y cuidar que mis conclusiones no digan más que la tabla.",
    prior=PRIOR_BASE + ["Sé calcular diferencias y porcentajes de cambio y distinguir relación de causa."],
    explain=[
        "Comparar grupos es una forma de buscar patrones. En la ficha hay dos variables que pueden influir en el crecimiento de una ciudad: la ubicación (costa o interior) y la existencia de ferrocarril. Se agrupan las ciudades según una característica y se compara cómo cambió cada grupo.",
        "Por ejemplo, se suman los habitantes de las ciudades con ferrocarril en cada año y se hace lo mismo con las que no tienen. Si el grupo con ferrocarril creció mucho más, aparece un patrón. Pero se debe probar cada variable: si la ubicación fuera la clave, las dos ciudades de la costa crecerían parecido, y eso no ocurre.",
        "Un patrón geográfico no se confirma con una sola variable ni con pocos casos. Con cuatro ciudades ficticias solo puedes decir que «en esta tabla» ocurre algo; para generalizar necesitas más casos y fuentes que expliquen el porqué. También conviene decir qué dato falta.",
    ],
    vocab=[("grupo de comparación", "casos que se juntan porque comparten una característica"), ("variable que influye", "variable que podría explicar parte de un cambio"), ("generalizar", "decir que algo vale para muchos casos, no solo para los de la tabla"), ("evidencia", "datos o fuentes que apoyan una afirmación"), ("hipótesis", "explicación posible que se debe comprobar")],
    worked=[
        ("Sumar un grupo", "{F} ¿Cuántos habitantes sumaban en 1900 las ciudades con ferrocarril?", ["Identifico las ciudades con ferrocarril: Puerto Alba y Villa Cobre.", "Sumo sus habitantes de 1900: 40.000 más 15.000."], "55.000 habitantes"),
        ("Descartar una variable", "{F} ¿La ubicación en la costa explica el crecimiento?", ["Las dos ciudades de la costa son Puerto Alba (creció mucho) y Lomas Altas (creció poco).", "Si la costa explicara el crecimiento, ambas habrían crecido parecido."], "No: la ubicación sola no explica el crecimiento"),
    ],
    mistakes=[("Generalizar con muy pocos casos, por ejemplo «todas las ciudades con tren crecen».", "Se toman cuatro casos como si fueran todos los casos.", "Di «en esta tabla» y pide más casos."),
              ("Probar solo una variable e ignorar las otras.", "Se piensa que la primera idea que aparece es la causa.", "Revisa cada variable posible, como la ubicación y el ferrocarril.")],
    T=[
        ("abc", "{F} ¿Cuáles ciudades tienen ferrocarril?", "Puerto Alba y Villa Cobre", "Valle Verde y Lomas Altas", "Solo Puerto Alba", "La ficha indica estación de ferrocarril en Puerto Alba y Villa Cobre."),
        ("ab", "{F} ¿Qué ciudad está en el interior y no tiene ferrocarril?", "Valle Verde", "Lomas Altas", "Valle Verde es del interior y sin ferrocarril; Lomas Altas está en la costa."),
        ("{F} ¿Cuántos habitantes tenía Lomas Altas en 1900?", "6.000", "El dato de Lomas Altas en 1900 es 6.000 habitantes."),
        ("=", "{F} ¿Cuántos habitantes sumaban en 1850 las dos ciudades con ferrocarril?", "12000+3000", "Se suman los habitantes de 1850 de Puerto Alba y de Villa Cobre.", " habitantes"),
        ("=", "{F} ¿Cuántos habitantes sumaban en 1900 las dos ciudades sin ferrocarril?", "12000+6000", "Se suman los habitantes de 1900 de Valle Verde y de Lomas Altas.", " habitantes"),
        ("=", "{F} Las ciudades con ferrocarril sumaban 15.000 en 1850 y 55.000 en 1900. ¿Cuánto aumentó el grupo?", "55000-15000", "La diferencia entre el total de 1900 y el de 1850 es el aumento del grupo.", " habitantes"),
        ("=", "{F} Las ciudades sin ferrocarril sumaban 16.000 en 1850 y 18.000 en 1900. ¿Cuánto aumentó el grupo?", "18000-16000", "Se resta el total de 1850 al de 1900 en el grupo sin ferrocarril.", " habitantes"),
        ("abc", "{F} ¿Qué patrón aparece al comparar los dos grupos?", "El grupo con ferrocarril creció mucho más", "El grupo sin ferrocarril creció más", "Ambos crecieron igual", "El grupo con ferrocarril aumentó 40.000 y el otro 2.000."),
        ("abc", "{F} Una persona dice: «Lomas Altas está en la costa, por eso debía crecer como Puerto Alba». ¿Qué dicen los datos?", "Lomas Altas creció poco, aunque está en la costa", "Lomas Altas creció igual que Puerto Alba", "Lomas Altas dejó de existir", "La costa sola no basta: Lomas Altas pasó de 5.000 a 6.000."),
        ("abc", "{F} ¿Qué hipótesis se puede plantear con esta tabla?", "El ferrocarril pudo favorecer el crecimiento de las ciudades", "El ferrocarril fue lo único que importó", "La costa causó todo el crecimiento", "Una hipótesis es una explicación posible que luego se comprueba con fuentes."),
        ("ab", "{F} ¿Qué se puede afirmar con seguridad con estos cuatro casos?", "Que en esta tabla las ciudades con ferrocarril crecieron más", "Que todas las ciudades con ferrocarril del mundo crecieron más", "Con cuatro casos solo se afirma lo que ocurre en la tabla."),
        ("abc", "{F} Para comprobar la hipótesis del ferrocarril, ¿qué fuente ayudaría más?", "Un informe de la época sobre quiénes llegaron en tren y para qué", "Un dibujo de una locomotora", "Una lista de nombres de calles", "Un informe sobre quiénes llegaban y por qué da evidencia de la relación."),
        ("abc", "{F} ¿Qué dato falta para un análisis más completo?", "Qué actividad económica tenía cada ciudad", "La cantidad de bancas de cada plaza", "El nombre del alcalde actual", "La actividad económica podría explicar por qué algunas ciudades atraían más gente."),
    ],
    ctx=("abc", "Una organización de transportistas de ejemplo registra: «Ruta con paradero techado: 120 pasajeros por semana en 2015 y 180 en 2020. Ruta sin paradero techado: 100 pasajeros en 2015 y 105 en 2020». ¿Qué patrón puede describir?", "La ruta con paradero techado aumentó más pasajeros", "La ruta sin paradero aumentó más", "Ambas aumentaron igual", "La primera aumentó 60 y la segunda 5; eso es un patrón, aunque no prueba la causa."),
    sc=[("¿Qué es agrupar casos para comparar?", "Juntar casos con una característica común", "Agrupar permite ver si un grupo cambia distinto de otro."),
        ("¿Basta una variable para explicar un patrón?", "No, hay que probar otras posibles", "Probar otras variables evita explicaciones apresuradas."),
        ("Al analizar datos de ciudades: ¿qué es una hipótesis?", "Una explicación posible que se debe comprobar", "Se apoya en datos pero necesita más evidencia.")],
    op=("Analiza esta tabla de ejemplo (fuente: registro de una región ficticia): «Pueblo Sur (con puerto): 4.000 habitantes en 1850 y 10.000 en 1900. Pueblo Este (con puerto): 3.000 y 9.000. Pueblo Norte (sin puerto): 4.000 y 5.000. Pueblo Oeste (sin puerto): 3.000 y 4.000». "
        "Suma cada grupo en 1850 y 1900, calcula cuánto aumentó cada uno, escribe el patrón y una hipótesis que dejes como pendiente.",
        "Con puerto: 7.000 en 1850 y 19.000 en 1900, aumento de 12.000. Sin puerto: 7.000 y 9.000, aumento de 2.000. Patrón: en esta tabla los pueblos con puerto crecieron mucho más. Hipótesis pendiente: el puerto pudo atraer trabajo y personas.",
        ["suma y compara los grupos", "describe el patrón con datos", "formula una hipótesis sin afirmarla como cierta"],
        ["una tabla de cuatro números, una frase de patrón y una hipótesis"], ["generalizar con cuatro casos", "afirmar la causa"],
        "Pregunta: «¿Qué fuente comprobaría tu hipótesis?»."),
    reinforce="Elige dos grupos de casos de tu barrio (por ejemplo, calles con y sin transporte) y di qué datos compararías.",
    extend="Explica por qué cuatro casos no bastan para decir que algo ocurre en todos los casos.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). Datos de una ciudad ficticia, Puerto Alba, hacia 1900. Fuente: registro municipal de ejemplo. "
      "Tabla 1, origen de 400 trabajadores de una fábrica: 100 nacieron en la ciudad, 240 llegaron del campo y 60 llegaron de otras ciudades. "
      "Tabla 2, vivienda: en 1860 había 4.000 personas y 800 viviendas; en 1900 había 24.000 personas y 2.000 viviendas. "
      "Dato adicional: la migración es el traslado de personas de un lugar a otro para vivir.")
build(
    O, 5, F5,
    use="Hoy uso datos geográficos para analizar un caso de ciudad en crecimiento (trabajo y vivienda) y lo relaciono con la industrialización.",
    prior=PRIOR_BASE + ["Sé comparar grupos de datos, calcular porcentajes y plantear una hipótesis."],
    explain=[
        "Las tablas permiten estudiar problemas reales de una comunidad. En una ciudad que crece por la industrialización aparecen preguntas sobre el trabajo, la vivienda y el origen de las personas. La migración del campo a la ciudad fue una de las grandes transformaciones del siglo XIX.",
        "Con los datos de la ficha se pueden calcular porcentajes: de 400 trabajadores, 240 llegaron del campo, y 240 entre 400 es el 60 %. También se puede calcular cuántas personas había por vivienda, dividiendo las personas por el número de viviendas. Ese número muestra si el crecimiento de la ciudad se acompañó de más casas o de hacinamiento.",
        "Un análisis útil termina conectando los datos con un proceso: el crecimiento rápido, por la llegada de trabajadores, pudo dejar menos viviendas por persona. Pero cuando hablamos de causas, usamos la palabra «pudo», porque la tabla describe lo que pasó y no prueba el porqué. Una investigación más amplia agregaría fuentes escritas de la época.",
    ],
    vocab=[("migración", "traslado de personas de un lugar a otro para vivir"), ("hacinamiento", "muchas personas en poco espacio para vivir"), ("personas por vivienda", "población dividida por el número de viviendas"), ("origen", "lugar del que viene una persona o un dato"), ("crecimiento urbano", "aumento de la población y del tamaño de una ciudad")],
    worked=[
        ("Calcular el porcentaje de trabajadores del campo", "{F} ¿Qué porcentaje de los 400 trabajadores llegó del campo?", ["Leo los datos: 240 llegaron del campo, de un total de 400.", "Divido 240 entre 400 y multiplico por 100."], "60 %"),
        ("Calcular personas por vivienda", "{F} ¿Cuántas personas había por vivienda en 1860?", ["Leo los datos: 4.000 personas y 800 viviendas.", "Divido 4.000 entre 800."], "5 personas por vivienda"),
    ],
    mistakes=[("Decir que la migración «causó» el hacinamiento solo porque ambos aparecen en las tablas.", "Se pasa de una relación a una causa sin evidencia.", "Escribe «pudo contribuir» y busca fuentes que expliquen la relación."),
              ("Comparar las cifras de personas y de viviendas por separado y no por vivienda.", "Se piensa que si aumentan las dos, todo mejora.", "Calcula las personas por vivienda en cada año.")],
    T=[
        ("abc", "{F} ¿Cuántos trabajadores nacieron en la ciudad?", "100", "240", "60", "La ficha indica que 100 nacieron en la ciudad."),
        ("ab", "En Historia y Geografía: ¿qué es la migración?", "El traslado de personas de un lugar a otro para vivir", "El aumento del precio de las viviendas", "La migración es el cambio de lugar de residencia de las personas."),
        ("{F} ¿Cuántas viviendas había en 1900?", "2.000", "La Tabla 2 indica 2.000 viviendas en 1900."),
        ("=", "{F} ¿Cuántos trabajadores no llegaron del campo?", "400-240", "Se restan los que llegaron del campo al total de trabajadores.", " trabajadores"),
        ("=", "{F} ¿Qué porcentaje de los trabajadores llegó de otras ciudades?", "60*100//400", "Se divide 60 entre 400 y se multiplica por 100 para sacar el porcentaje.", " %"),
        ("=", "{F} ¿Cuántas personas había por vivienda en 1900?", "24000//2000", "Se divide la población total por el número de viviendas.", " personas por vivienda"),
        ("abc", "{F} ¿Qué cambió entre 1860 y 1900 en las personas por vivienda?", "Pasó de 5 a 12", "Pasó de 12 a 5", "No cambió", "En 1860 había 5 personas por vivienda y en 1900 había 12."),
        ("abc", "{F} ¿Qué se puede afirmar con los datos de la Tabla 1?", "La mayoría de los trabajadores llegó del campo", "La mayoría nació en la ciudad", "Todos llegaron de otras ciudades", "Los que llegaron del campo son 240 de 400, es decir, más de la mitad."),
        ("abc", "{F} ¿Qué relación con la industrialización se puede plantear?", "La fábrica pudo atraer a trabajadores del campo", "La fábrica impidió que llegaran trabajadores del campo", "La fábrica hizo que casi todos nacieran en la ciudad", "Una hipótesis razonable conecta fábrica y llegada de trabajadores, usando «pudo»."),
        ("ab", "{F} Una autoridad dice que el hacinamiento fue causado por la migración. ¿Qué responde un análisis cuidadoso?", "Que los datos muestran una relación y que se necesitan más fuentes para probar la causa", "Que la autoridad tiene toda la razón y no hace falta más", "Las tablas muestran relación y no prueban por sí solas una causa."),
        ("abc", "{F} Para proponer ideas de mejora, ¿qué información faltaría?", "Cuántas viviendas se podían construir y con qué recursos", "La fecha de fundación de la ciudad", "El nombre de la calle principal", "Los recursos y la capacidad de construcción permiten juzgar qué soluciones eran posibles."),
        ("abc", "{F} Se agrega un dato de ejemplo: «en 1900, de cada 100 viviendas, 70 no tenían agua potable». ¿Qué problema pudo afectar a las personas?", "La salud por falta de agua potable", "El precio de los pasajes del tren", "La cantidad de ferias del barrio", "La falta de agua potable pudo afectar la salud de la población."),
        ("abc", "{F} ¿Cuál es una conclusión bien apoyada en los datos?", "Entre 1860 y 1900 la ciudad creció más rápido que sus viviendas", "La ciudad creció solo por culpa de la fábrica", "Todos los trabajadores vivían bien", "Las personas aumentaron 6 veces y las viviendas 2,5 veces, por eso las personas por vivienda subieron."),
    ],
    ctx=("abc", "Una junta de vecinos de ejemplo registra: «Villa Nueva tenía 500 personas y 100 viviendas hace 20 años; hoy tiene 1.200 personas y 200 viviendas». ¿Cuántas personas hay hoy por vivienda?", "6 personas por vivienda", "5 personas por vivienda", "12 personas por vivienda", "1.200 entre 200 es 6; hace 20 años eran 5."),
    sc=[("En demografía: ¿cómo se define la migración?", "El traslado de personas de un lugar a otro para vivir", "La migración cambia el número de habitantes de un lugar."),
        ("¿Cómo se calculan las personas por vivienda?", "Dividiendo las personas por las viviendas", "Esa división muestra qué tan llena está una vivienda."),
        ("¿Qué palabra conviene usar para una explicación posible?", "«Pudo»", "El condicional deja claro que falta evidencia.")],
    op=("Analiza esta tabla de ejemplo (fuente: registro municipal de ejemplo) de la ciudad ficticia Villa Textil, 1900: «De 300 trabajadores de una fábrica, 180 llegaron del campo, 90 nacieron en la ciudad y 30 llegaron de otras ciudades. En 1880 la ciudad tenía 6.000 personas y 1.200 viviendas; en 1900 tenía 18.000 personas y 2.000 viviendas». "
        "Calcula el porcentaje de trabajadores que llegó del campo, las personas por vivienda de 1880 y de 1900, y escribe una hipótesis y una pregunta pendiente.",
        "Del campo: 180 entre 300 es 60 %. Personas por vivienda: en 1880, 6.000 entre 1.200 son 5; en 1900, 18.000 entre 2.000 son 9. Hipótesis: la llegada de trabajadores pudo contribuir a que cada vivienda tuviera más personas. Pregunta pendiente: ¿qué dicen las fuentes de la época sobre la vivienda de las familias obreras?",
        ["calcula bien porcentaje y personas por vivienda", "formula una hipótesis con «pudo»", "propone una pregunta o fuente nueva"],
        ["tres cálculos, una hipótesis y una pregunta"], ["afirmar causa sin evidencia", "olvidar las unidades"],
        "Pregunta: «¿Qué dato respalda tu hipótesis y qué falta para probarla?»."),
    reinforce="Calcula las personas por vivienda de un lugar de ejemplo con 90 personas y 30 viviendas y explica qué significa.",
    extend="Explica con un ejemplo por qué el crecimiento de una ciudad exige también más servicios, además de más viviendas.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Tres usos de un mismo conjunto de datos. Datos de exportación de un puerto ficticio, fuente: informe portuario de ejemplo: "
      "1890: 1.000 toneladas; 1891: 1.200; 1892: 900; 1893: 800; 1894: 850. "
      "Informe A (de un comerciante): «Las exportaciones subieron de 1.000 a 1.200 toneladas». "
      "Informe B (de un periodista): «Entre 1890 y 1894 las exportaciones bajaron de 1.000 a 850 toneladas». "
      "Informe C (de una oficina): «Tabla con nombre completo y dirección de cada trabajador del puerto, para que el público consulte».")
build(
    O, 6, F6,
    use="Hoy aprendo a comunicar datos geográficos con ética: citar la fuente, no recortar datos para engañar y proteger los datos personales.",
    prior=PRIOR_BASE + ["Sé analizar una tabla, calcular cambios y plantear hipótesis."],
    explain=[
        "Comunicar datos con ética significa cuidar tres cosas. Primero, citar la fuente: decir de dónde vienen los datos, de qué año y quién los publicó. Segundo, no manipular la información: mostrar todos los datos relevantes y no solo los que apoyan lo que yo quiero decir. Tercero, proteger a las personas: no publicar datos personales como nombres o direcciones sin permiso.",
        "Un recorte engañoso ocurre cuando se muestran solo algunos años de una serie. En la ficha, el informe A muestra solo 1890 y 1891, y el B muestra solo el principio y el final. Ambos dicen cosas verdaderas, pero cada uno entrega una imagen parcial. Una buena comunicación muestra la serie completa y explica la tendencia.",
        "Las herramientas digitales, como una planilla de cálculo, ayudan a ordenar los datos y a calcular, pero no revisan por ti si los datos son confiables ni si el uso es ético. Antes de compartir una tabla, pregúntate quién puede verla, qué daño podría causar y si cité la fuente.",
    ],
    vocab=[("citar la fuente", "decir de dónde vienen los datos"), ("recorte engañoso", "mostrar solo parte de los datos para apoyar una idea"), ("serie completa", "todos los datos del periodo, en orden"), ("dato personal", "información que identifica a una persona, como nombre o dirección"), ("ética de la información", "uso honesto y respetuoso de los datos")],
    worked=[
        ("Ver un recorte engañoso", "{F} ¿Qué problema tiene el informe A?", ["Muestra solo 1890 y 1891, cuando la serie llega hasta 1894.", "La subida inicial se presenta como si fuera la tendencia de todo el periodo."], "Es un recorte engañoso: no muestra toda la serie"),
        ("Proteger datos personales", "{F} ¿Qué problema tiene el informe C?", ["Publica nombre completo y dirección de cada trabajador.", "Esos son datos personales y se necesita permiso o anonimizar."], "Expone datos personales sin permiso"),
    ],
    mistakes=[("Elegir solo los datos que apoyan mi idea.", "Es más fácil convencer mostrando solo una parte.", "Muestra la serie completa y explica los matices."),
              ("Creer que publicar datos de personas es inocuo si «ya son públicos» en alguna parte.", "Se confunde acceso con permiso.", "Pregunta si las personas dieron su permiso y si es necesario mostrar el dato.")],
    T=[
        ("abc", "{F} ¿Cuál es la fuente de los datos de exportación?", "Un informe portuario de ejemplo", "Un periodista", "Un comerciante", "La ficha dice que los datos vienen de un informe portuario de ejemplo."),
        ("ab", "En ética de la información: ¿qué significa citar la fuente?", "Decir de dónde vienen los datos", "Copiar la tabla sin cambios", "Citar es indicar el origen para que otros puedan revisarlo."),
        ("{F} ¿Cuántas toneladas se exportaron en 1893?", "800", "La serie indica 800 toneladas en 1893."),
        ("=", "{F} ¿Cuántas toneladas más se exportaron en 1891 que en 1890?", "1200-1000", "Se resta el dato de 1890 al de 1891 para ver la subida.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas menos se exportaron en 1894 que en 1890?", "1000-850", "Se resta el dato de 1894 al de 1890 para ver cuánto bajó.", " toneladas"),
        ("=", "{F} ¿En qué porcentaje subieron las exportaciones entre 1890 y 1891?", "(1200-1000)*100//1000", "El aumento de 200 sobre un valor inicial de 1.000 es un 20 %.", " %"),
        ("abc", "{F} ¿Qué muestra la serie completa de 1890 a 1894?", "Subió en 1891 y luego bajó hasta 1893, con una leve alza en 1894", "Subió todos los años", "Bajó todos los años", "La serie sube a 1.200, cae a 800 y repunta a 850, algo que ni A ni B muestran solos."),
        ("abc", "{F} ¿Qué recorte hace el informe B?", "Muestra solo 1890 y 1894 y omite el alza de 1891", "Muestra todos los años", "Usa un dato inventado", "B dice una verdad parcial, pues omite los años intermedios."),
        ("abc", "{F} ¿Qué texto comunica mejor la tendencia?", "Entre 1890 y 1894 subió en 1891, bajó hasta 800 en 1893 y llegó a 850 en 1894", "Las exportaciones solo subieron", "Las exportaciones solo bajaron", "Es el único que usa la serie completa."),
        ("abc", "{F} ¿Qué se debería hacer con el informe C antes de publicarlo?", "Quitar nombres y direcciones o pedir permiso", "Dejarlo igual porque es útil", "Agregar los teléfonos", "Proteger los datos personales es parte del uso ético de la información."),
        ("ab", "{F} Un periodista dice: «No tengo que citar la fuente porque los números son verdaderos». ¿Qué falla?", "Sin fuente nadie puede comprobar los datos", "Nada, porque son verdaderos", "Citar la fuente permite que otros revisen la información."),
        ("abc", "Usas una planilla de cálculo para ordenar los datos y te da un promedio. ¿Qué sigue siendo tu responsabilidad?", "Revisar si los datos son confiables y si el uso es ético", "Nada: la planilla lo revisa todo", "Borrar la fuente", "La herramienta calcula, pero no juzga la calidad ni la ética."),
        ("abc", "{F} Una compañera dice: «Para convencer a mi comunidad solo mostraré el año en que subió». ¿Qué le aconsejarías?", "Mostrar toda la serie y explicar los matices", "Esconder los años que bajaron", "Inventar un año más", "Una comunicación honesta muestra toda la serie."),
    ],
    ctx=("abc", "La directiva de un club de ejemplo quiere publicar en un afiche la lista de socios con nombre y dirección para mostrar que el club creció. ¿Qué es lo más adecuado?", "Publicar solo el número total de socios y su evolución por año", "Publicar los nombres y direcciones de todos", "No decir nada del crecimiento", "El número total muestra el crecimiento sin exponer datos personales."),
    sc=[("Al comunicar datos geográficos: ¿qué significa citar la fuente?", "Decir de dónde vienen los datos", "Citar permite que otros comprueben la información."),
        ("¿Qué es un recorte engañoso?", "Mostrar solo parte de los datos para apoyar una idea", "El recorte da una imagen incompleta o falsa."),
        ("¿Qué datos conviene proteger?", "Los datos personales, como nombre y dirección", "Los datos personales identifican a las personas.")],
    op=("Revisa esta comunicación de ejemplo. Datos de la ficha de ejemplo (fuente: registro de una feria de ejemplo): «visitantes por año: 2018, 1.000; 2019, 1.500; 2020, 600; 2021, 800; 2022, 1.200». Un cartel dice: «¡La feria creció de 600 a 1.200 visitantes!». "
        "Escribe qué problema tiene el cartel, una versión mejorada de dos frases que cite la fuente y una frase sobre qué datos no publicarías si el registro incluyera nombres.",
        "Problema: el cartel muestra solo 2020 y 2022 y deja fuera 2018 y 2019, cuando hubo más visitantes. Versión mejorada: «Según el registro de la feria, los visitantes fueron 1.000 en 2018 y 1.500 en 2019; bajaron a 600 en 2020 y subieron a 1.200 en 2022». No publicaría nombres ni direcciones de visitantes.",
        ["identifica el recorte", "reescribe con la serie completa y la fuente", "protege los datos personales"],
        ["un texto corto con tres partes"], ["omitir la fuente", "mantener el recorte"],
        "Pregunta: «¿Lo que muestras es toda la serie y de dónde viene?»."),
    reinforce="Elige un dato que hayas visto en las noticias o en redes y anota quién lo publicó y si mostró todos los años.",
    extend="Explica con un ejemplo por qué proteger datos personales es parte del respeto hacia la comunidad.",
)
