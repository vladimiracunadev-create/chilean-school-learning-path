"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 11 (opinión pública, educación y construcción de nación)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 11"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1827, aparece El Mercurio de Valparaíso; 1830, comienza a circular El Araucano, periódico del gobierno; 1842, se funda la Universidad de Chile, con Andrés Bello como primer rector, y la Escuela Normal de Preceptores; 1850, nace la Sociedad de la Igualdad; 1860, Ley de Instrucción Primaria; 1877, el decreto Amunátegui permite el ingreso de mujeres a la universidad."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo la prensa, la universidad, las escuelas y las organizaciones políticas del siglo XIX y a explicar cómo ayudaron a formar la idea de nación. Sirve para entender de dónde viene la identidad nacional y quiénes quedaron fuera.",
    prior=["Sé qué fue la Independencia y qué es una república.", "Sé leer una línea de tiempo.", "Sé que una fuente tiene autor y fecha."],
    explain=[
        "La nación es una comunidad de personas que se siente unida por una historia, un territorio, una lengua y símbolos comunes, y que se reconoce como parte de un mismo país. En el siglo XIX, después de la Independencia, las élites chilenas trabajaron para crear y difundir esa idea. No bastaba con tener Estado: había que lograr que las personas sintieran que pertenecían a Chile.",
        "Para eso se desarrollaron espacios de opinión pública, es decir, lugares donde las personas discuten asuntos de interés común. Entre ellos, la prensa (periódicos como El Araucano y El Mercurio de Valparaíso), la historiografía (escritura de la historia), la literatura y la movilización política (organizaciones como la Sociedad de la Igualdad en 1850). También creció el sistema educacional: la Universidad de Chile, la Escuela Normal que formaba profesores y escuelas primarias.",
        "Estos espacios difundieron relatos, símbolos y saberes comunes. Pero la nación imaginada no incluyó a todos por igual: muchas personas no sabían leer ni escribir, y las mujeres, los pobres y los pueblos originarios tuvieron un acceso desigual. Por eso decimos que las instituciones ayudaron a expandir y profundizar la idea de nación, no que la volvieron igual para todos.",
    ],
    vocab=[("nación", "comunidad que se siente unida por historia, territorio, lengua y símbolos comunes"), ("opinión pública", "discusión de asuntos de interés común en espacios abiertos como la prensa"), ("historiografía", "escritura de la historia por parte de historiadores"), ("movilización política", "organización de personas para influir en decisiones públicas"), ("sistema educacional", "conjunto de escuelas, liceos y universidades de un país")],
    worked=[
        ("Ubicar hechos en la línea", "Con la línea de tiempo, ¿cuántos años pasaron entre el inicio de El Araucano y la fundación de la Universidad de Chile?",
         ["Busco ambas fechas: 1830 y 1842.", "Resto: 1842 - 1830."], "12 años"),
        ("Distinguir tipos de espacio", "Clasifica la Sociedad de la Igualdad (1850) y la Escuela Normal de Preceptores (1842): ¿cuál es movilización política y cuál sistema educacional?",
         ["La Sociedad de la Igualdad era una organización para influir en la vida pública: movilización política.", "La Escuela Normal formaba profesores: sistema educacional."], "Sociedad de la Igualdad: movilización política; Escuela Normal: sistema educacional"),
    ],
    mistakes=[
        ("Creer que la nación chilena existía igual para todos desde la Independencia.", "Fue una idea que se construyó con instituciones y con exclusiones.", "Pregunta quién participaba y quién quedaba fuera."),
        ("Confundir Estado con nación.", "El Estado es la organización con leyes e instituciones; la nación es la comunidad que se reconoce como tal.", "Usa «Estado» para instituciones y «nación» para identidad."),
    ],
    T=[
        ("En Historia: ¿qué es la opinión pública?", "La discusión de asuntos de interés común en espacios abiertos como la prensa", "Define el concepto central de la clase."),
        ("{F} ¿En qué año se fundó la Universidad de Chile?", "1842", "La línea de tiempo lo indica."),
        ("{F} ¿Qué periódico era del gobierno según la línea de tiempo?", "El Araucano", "La línea lo describe como periódico del gobierno."),
        ("{F} ¿Qué decreto de 1877 abrió la universidad a las mujeres?", "El decreto Amunátegui", "La línea lo menciona con ese nombre."),
        ("En Historia: ¿qué diferencia hay entre Estado y nación? A) el Estado es la organización con leyes e instituciones y la nación es la comunidad que se reconoce unida, B) son lo mismo, C) el Estado es la comunidad que se siente unida y la nación es el conjunto de leyes e instituciones.", "A", "Son conceptos distintos y complementarios."),
        ("Una compañera dice: «Como se fundó una universidad, todos los chilenos pudieron estudiar en ella». ¿Qué corrección haces según la explicación?", "El acceso fue desigual: muchas personas no sabían leer y las mujeres entraron recién en 1877", "La educación creció, pero con exclusiones."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley de instrucción primaria y el decreto que permitió a las mujeres entrar a la universidad?", "1877-1860", "Se restan las dos fechas de la línea."),
        ("=", "{F} ¿Cuántos años pasaron entre la aparición de El Mercurio de Valparaíso y la Sociedad de la Igualdad?", "1850-1827", "Se restan las fechas de ambos hitos."),
        ("Clasifica estos dos espacios: A) un periódico que discute leyes, B) una escuela que enseña a leer. ¿Cuál es de opinión pública?", "A", "El periódico discute asuntos comunes; la escuela forma."),
        ("{F} ¿Qué hecho de la línea muestra que el Estado se interesaba en formar profesores? Justifica.", "La Escuela Normal de Preceptores en 1842, porque preparaba a quienes enseñarían en las escuelas", "Su función es formar docentes."),
        ("Explica por qué la nación imaginada del siglo XIX no incluyó a todos por igual.", "Porque muchas personas no sabían leer ni escribir y mujeres, pobres y pueblos originarios tenían menos acceso a esos espacios", "Los espacios de opinión y educación eran desiguales."),
        ("Evalúa la afirmación «la prensa y la educación ayudaron a expandir la idea de nación». A) es razonable porque difundieron relatos y saberes comunes, B) es falsa porque la prensa y la educación llegaron a todos los chilenos por igual, C) es falsa porque la idea de nación ya estaba completa desde la Independencia.", "A", "Es una afirmación acotada y sustentada."),
        ("Una persona dice: «La nación chilena fue idea de un solo grupo y todos la aceptaron sin debate». ¿Qué sugiere la existencia de organizaciones como la Sociedad de la Igualdad?", "Que había grupos que discutían y proponían ideas distintas sobre el país", "La movilización política muestra debate."),
    ],
    ctx=("Un afiche escolar dice: «En 1842 todos los chilenos empezaron a sentirse parte de una misma nación gracias a la universidad». Escribe una frase que mejore el afiche con lo aprendido.", "La universidad y otras instituciones ayudaron a difundir la idea de nación, pero el acceso fue desigual", "Se debe matizar el efecto de una sola institución."),
    sc=[("En Historia: ¿qué es la historiografía?", "La escritura de la historia por parte de historiadores", "Es uno de los espacios que ayudaron a formar la idea de nación."),
        ("Nombra dos espacios de opinión pública del siglo XIX.", "Por ejemplo: la prensa y la movilización política", "Son espacios de discusión de asuntos comunes."),
        ("{F} ¿Quién fue el primer rector de la Universidad de Chile?", "Andrés Bello", "La línea de tiempo lo señala.")],
    op=("{F} Con la línea de tiempo de arriba, escribe un párrafo de cinco líneas que responda: «¿Qué espacios ayudaron a formar la idea de nación en el siglo XIX y quiénes tuvieron menos acceso?». Nombra al menos un periódico, una institución educativa y un grupo con menos acceso.",
        "El Araucano y El Mercurio de Valparaíso difundían información. La Universidad de Chile y la Escuela Normal formaban saberes comunes. Sin embargo, las mujeres solo pudieron entrar a la universidad desde 1877 y muchas personas no sabían leer.",
        ["nombra un periódico y una institución", "identifica un grupo con menos acceso", "usa una fecha"], ["párrafo de cinco líneas"], ["decir que todos tuvieron igual acceso", "no usar fechas"], "Léele tu párrafo a una persona de tu casa y pídele que diga qué grupo quedó con menos acceso."),
    reinforce="Escribe en tu cuaderno las seis fechas de la línea de tiempo y, al lado de cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué la Escuela Normal es importante para expandir la educación.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (editorial de un periódico, texto de ejemplo): «Quien sabe leer participa en los asuntos de la República; abramos escuelas para que ninguna familia quede sin el beneficio de las letras.» Fuente B (registro de una escuela rural, texto de ejemplo): «De 40 niños inscritos asisten 22 en invierno; los caminos están cortados por la lluvia.» Fuente C (tabla de ejemplo): en una ciudad de ejemplo saben leer 45 de cada 100 habitantes; en una zona rural de ejemplo, 12 de cada 100. Fuente D (historiadora actual, texto de ejemplo): «La expansión escolar fue real, pero desigual según territorio y género.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer fuentes de prensa, de escuelas y de estadísticas del siglo XIX y a detectar qué dicen, quién las produce y qué no muestran. Sirve para no tomar como cierto todo lo que dice un periódico o una tabla.",
    prior=["Distingo fuentes primarias y secundarias.", "Sé qué es la opinión pública.", "Sé leer porcentajes sencillos."],
    explain=[
        "Los espacios de opinión pública producen fuentes muy distintas. Un editorial de prensa expresa la postura de un periódico y busca convencer: tiene un propósito. Un registro escolar anota datos prácticos, como cuántos niños asistían. Una tabla estadística resume información en números. Cada una responde preguntas diferentes.",
        "Al leer una fuente conviene separar tres cosas: qué dice (su contenido), quién y para qué lo dijo (procedencia e intención) y qué deja fuera (su límite). El editorial de ejemplo defiende abrir escuelas, pero no prueba que se abrieran. El registro de una escuela rural muestra la asistencia, no el aprendizaje de los niños. La tabla de alfabetización cuenta quién sabe leer, no cómo se usó esa habilidad.",
        "Contrastar fuentes permite ver mejor. Si el editorial dice que se abren escuelas y el registro muestra baja asistencia en invierno, aparece una distancia entre lo que se declara y lo que sucede. La tabla ayuda a comparar territorios: cuando una ciudad y una zona rural tienen cifras muy distintas, vemos desigualdad territorial.",
    ],
    vocab=[("editorial", "texto de un periódico que expresa su postura"), ("alfabetización", "capacidad de leer y escribir"), ("contenido de una fuente", "lo que la fuente dice explícitamente"), ("desigualdad territorial", "diferencia entre lugares en el acceso a algo, como la escuela"), ("contrastar", "comparar fuentes para ver coincidencias y diferencias")],
    worked=[
        ("Separar contenido y límite", "Con la Fuente B (registro de escuela rural), ¿qué dice y qué no permite saber?",
         ["Dice que de 40 inscritos asisten 22 en invierno y que los caminos están cortados.", "No dice cuánto aprenden los niños ni qué pasa en verano."], "Muestra baja asistencia en invierno; no muestra aprendizaje"),
        ("Contrastar dos fuentes", "La Fuente A pide abrir escuelas y la Fuente B muestra asistencia baja en invierno. ¿Qué se puede concluir con cuidado?",
         ["El editorial expresa un deseo de ampliar la educación.", "El registro muestra que asistir no era fácil en una zona rural.", "Entonces las escuelas existían pero su alcance estaba limitado por el territorio."], "Hay interés en educar, pero el acceso era desigual por territorio"),
    ],
    mistakes=[
        ("Tomar un editorial como descripción exacta de la realidad.", "Un editorial busca convencer y expresa una postura.", "Pregunta qué quiere lograr el periódico."),
        ("Concluir con una tabla más de lo que dice.", "La tabla cuenta alfabetización, no calidad ni uso.", "Escribe solo lo que las cifras permiten."),
    ],
    T=[
        ("En Historia: ¿qué es un editorial?", "Un texto de un periódico que expresa su postura", "Busca convencer, no solo informar."),
        ("{F} ¿Cuántos niños inscritos hay en la escuela rural de la Fuente B?", "40", "El registro lo indica."),
        ("{F} ¿La Fuente D es primaria o secundaria?", "Secundaria", "La escribe una historiadora actual."),
        ("{F} ¿Qué pide la Fuente A? A) abrir escuelas para que ninguna familia quede sin letras, B) cerrar las escuelas, C) prohibir la prensa.", "A", "El editorial defiende ampliar la educación."),
        ("{F} ¿Qué razón entrega la Fuente B para la baja asistencia en invierno?", "Los caminos están cortados por la lluvia", "El registro lo indica."),
        ("{F} Una compañera afirma que la Fuente A prueba que en todo el país se abrieron escuelas. ¿Por qué se equivoca?", "Porque un editorial expresa una petición o postura y no prueba que se cumpliera", "El editorial tiene intención, no es registro de hechos."),
        ("=", "{F} ¿Cuántos niños inscritos en la escuela de la Fuente B no asisten en invierno?", "40-22", "Se restan los que asisten de los inscritos."),
        ("=", "{F} ¿Cuántos puntos de diferencia hay entre la alfabetización de la ciudad (45 por cada 100) y la zona rural (12 por cada 100)?", "45-12", "Se restan las dos cifras de la tabla."),
        ("{F} Según la Fuente C, ¿en cuál de los dos territorios sabe leer una proporción menor de habitantes?", "En la zona rural", "Su cifra es 12 de cada 100."),
        ("{F} Explica por qué conviene contrastar la Fuente A con la Fuente B.", "Porque el editorial muestra lo que se pedía y el registro muestra lo que sucedía en una escuela rural", "Contrastar revela la distancia entre lo declarado y lo ocurrido."),
        ("{F} Con las Fuentes C y D, redacta una conclusión de una frase sobre la expansión escolar.", "La expansión escolar fue real, pero desigual entre ciudad y campo", "Une el dato y la interpretación."),
        ("{F} Evalúa la conclusión «La Fuente C demuestra que en el campo nadie quería aprender». A) es correcta, B) es excesiva porque la tabla mide alfabetización, no motivación, C) es correcta porque 12 es poco.", "B", "La tabla no explica las razones."),
        ("¿Qué otra fuente sumarías para saber cuántas niñas asistían a la escuela, comparadas con los niños? Escribe una y para qué.", "Por ejemplo: un registro de matrícula por género, para comparar cuántas niñas y cuántos niños asistían", "Una fuente nueva debe cerrar un vacío."),
    ],
    ctx=("{F} Un compañero prepara un afiche y copia solo la Fuente A con el título «Así era la escuela chilena en el siglo XIX». ¿Qué fuente agregarías para evitar una imagen exagerada y por qué?", "La Fuente B, porque muestra baja asistencia por los caminos cortados en invierno", "Contrastar corrige una imagen idealizada."),
    sc=[("En Historia: ¿qué es alfabetización?", "La capacidad de leer y escribir", "Es lo que mide la Fuente C."),
        ("¿Qué significa contrastar fuentes?", "Compararlas para ver coincidencias y diferencias", "Permite una conclusión más sólida."),
        ("¿Una tabla de alfabetización muestra la calidad de la enseñanza? Responde sí o no y por qué.", "No, porque solo cuenta quién sabe leer", "Es un límite de la fuente.")],
    op=("{F} Escribe una respuesta de seis líneas que use las Fuentes A, B y C de arriba para responder: «¿Cuán extendida estaba la educación a mediados del siglo XIX?». Señala qué dice cada fuente, una diferencia entre ciudad y campo y un límite.",
        "La Fuente A pide abrir escuelas. La Fuente B muestra que en una escuela rural asisten 22 de 40 inscritos en invierno. La Fuente C muestra que 45 de cada 100 saben leer en la ciudad y 12 en el campo. Hay desigualdad territorial. Límite: no muestran la calidad del aprendizaje.",
        ["usa tres fuentes", "marca desigualdad", "anota un límite"], ["texto de seis líneas"], ["citar solo la fuente A", "no mencionar límites"], "Pide a una persona de tu casa que verifique que usaste las cifras exactas."),
    reinforce="Haz una tabla con las Fuentes A, B y C: autor probable, qué dice y un límite.",
    extend="Escribe una pregunta que la Fuente C no permite responder.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: antes de 1842 no había universidad nacional; luego se fundó la Universidad de Chile, se abrieron más escuelas y circularon más periódicos. Continuidad: en el campo muchas familias seguían sin escuela cercana y gran parte de la población no sabía leer; las mujeres no podían entrar a la universidad hasta 1877; los pueblos originarios tenían poco lugar en el relato nacional."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué se mantuvo en la educación y la opinión pública y a ubicar esas diferencias en el territorio. Sirve para evitar la idea de que ampliar la educación eliminó todas las exclusiones.",
    prior=["Conozco los espacios de opinión pública del siglo XIX.", "Sé leer fuentes y tablas.", "Distingo cambio y continuidad."],
    explain=[
        "En el siglo XIX cambiaron varias cosas. Se fundó la Universidad de Chile en 1842; se creó la Escuela Normal para formar profesores; la Ley de Instrucción Primaria de 1860 estableció que el Estado financiaría escuelas primarias gratuitas; y creció la cantidad de periódicos y de lectores en las ciudades. Esto amplió el acceso a ideas y a saberes comunes, sobre todo en zonas urbanas.",
        "Pero muchas cosas continuaron. En el campo faltaban escuelas cercanas, la asistencia dependía del clima y del trabajo de las familias, y muchas personas no sabían leer. La Ley de 1860 dispuso escuelas gratuitas, pero no obligatorias: la obligatoriedad llegó recién con una ley de 1920. Las mujeres obtuvieron el derecho a ingresar a la universidad en 1877, y los pueblos originarios casi no aparecían en el relato nacional que se enseñaba.",
        "Por eso decimos que la educación expandió la idea de nación, pero no eliminó exclusiones. Para analizarlo se usa un cuadro de cambio y continuidad y se agrega el territorio: no era lo mismo vivir en Santiago o Valparaíso que en una zona rural. El territorio explica por qué una misma ley tuvo efectos distintos.",
    ],
    vocab=[("instrucción primaria", "enseñanza básica inicial que entregaban las escuelas"), ("obligatoria", "que todas las familias deben cumplir por ley"), ("gratuita", "que no se paga"), ("exclusión", "dejar fuera a ciertas personas o grupos de un derecho o de un espacio"), ("zona urbana / rural", "ciudad / campo")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «se fundó la Universidad de Chile» y «las mujeres no podían entrar a la universidad hasta 1877». ¿Cuál es cambio y cuál continuidad dentro del periodo?",
         ["La universidad es una institución nueva en 1842: cambio.", "La exclusión de mujeres se mantuvo hasta 1877: continuidad."], "La fundación es cambio; la exclusión de mujeres, continuidad hasta 1877"),
        ("Territorio", "¿Por qué una ley de escuelas gratuitas pudo llegar menos a una zona rural que a una ciudad?",
         ["La ley decía que las escuelas serían gratuitas, pero había que construirlas y mantenerlas.", "En el campo las distancias, el clima y el trabajo de las familias dificultaban asistir."], "Porque faltaban escuelas cercanas y el acceso dependía de distancia, clima y trabajo"),
    ],
    mistakes=[
        ("Decir que, con la Ley de 1860, todos los niños iban a la escuela.", "La ley la hizo gratuita, no obligatoria, y faltaban escuelas.", "Distingue ley, aplicación y asistencia."),
        ("Pensar que la expansión escolar fue igual en todo el país.", "El territorio marcó diferencias entre ciudad y campo.", "Siempre pregunta en qué zona ocurre el hecho."),
    ],
    T=[
        ("En Historia: ¿qué significa que una escuela sea gratuita?", "Que no se paga por asistir", "Es el sentido de la palabra."),
        ("{F} ¿Cuántos años pasaron entre la fundación de la Universidad de Chile y el ingreso de mujeres a la universidad según el cuadro?", "35 años", "1877 menos 1842 son 35 años."),
        ("En Historia: ¿qué es una exclusión?", "Dejar fuera a ciertas personas o grupos de un derecho o espacio", "Es lo contrario de incluir."),
        ("{F} Clasifica como cambio o continuidad: «circularon más periódicos».", "Cambio", "El cuadro lo presenta como novedad."),
        ("{F} Clasifica como cambio o continuidad: «en el campo muchas familias seguían sin escuela cercana».", "Continuidad", "El cuadro lo lista como lo que se mantuvo."),
        ("La Ley de 1860 dispuso escuelas gratuitas pero no obligatorias. ¿Qué significa eso? A) que el Estado ofrecía escuelas sin costo y no obligaba a asistir, B) que todos debían asistir, C) que las escuelas cobraban.", "A", "Gratuita no es lo mismo que obligatoria."),
        ("=", "Una zona rural de ejemplo tiene 5 escuelas para 1.200 niños en edad escolar. ¿Cuántos niños hay en promedio por escuela?", "1200//5", "Se reparte el total entre las escuelas."),
        ("=", "En una ciudad de ejemplo hay 12 escuelas para 1.200 niños. ¿Cuántos niños hay en promedio por escuela?", "1200//12", "Se reparte el total entre las escuelas."),
        ("Explica por qué la misma ley de 1860 pudo tener efectos distintos en ciudad y campo.", "Porque en las ciudades había más escuelas y en el campo la distancia, el clima y el trabajo dificultaban asistir", "El territorio condiciona la aplicación de una ley."),
        ("{F} Con el cuadro, ¿qué muestra la fecha 1877 sobre la expansión de la educación?", "Que las mujeres tardaron décadas en acceder a la universidad, pese a la expansión", "La exclusión de género continuó."),
        ("Una compañera dice: «Como se fundó la Universidad en 1842, desde entonces no hubo exclusiones en la educación». Corrige con un dato.", "Las mujeres solo pudieron ingresar en 1877 y muchas personas del campo no sabían leer", "Hay datos de continuidad de la exclusión."),
        ("Evalúa la afirmación «la educación amplió el acceso al saber pero mantuvo desigualdades de género y territorio». A) es exacta, B) es falsa porque no hubo cambios, C) es falsa porque todos tenían el mismo acceso.", "A", "Sostiene cambio y continuidad a la vez."),
        ("Propón una pregunta de territorio sobre la escuela del siglo XIX.", "Por ejemplo: ¿cuántas escuelas había por habitante en la ciudad y en el campo?", "La pregunta compara territorios."),
    ],
    ctx=("Un compañero escribe: «Desde 1860 todos los niños chilenos iban a la escuela». Con lo aprendido, corrige su frase en una oración.", "La ley de 1860 creó escuelas gratuitas, pero no obligatorias, y muchas zonas rurales no tenían escuela cercana", "La corrección distingue gratuita de obligatoria y señala el territorio."),
    sc=[("En Historia: ¿qué es la instrucción primaria?", "La enseñanza básica inicial que entregaban las escuelas", "Es el nivel regulado por la ley de 1860."),
        ("¿Qué significa «obligatoria»?", "Que todas las familias deben cumplirla por ley", "Es distinto de gratuita."),
        ("Nombra una exclusión que continuó en el siglo XIX.", "Por ejemplo: la de las mujeres en la universidad hasta 1877", "Es una exclusión del cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, elabora una tabla de dos columnas (cambio y continuidad) con tres filas. Luego escribe una frase que explique por qué las zonas rurales cambiaron más despacio que las ciudades.",
        "Cambio: universidad 1842; cambio: más periódicos; cambio: ley de 1860. Continuidad: poca escuela en el campo; continuidad: mujeres excluidas hasta 1877; continuidad: pueblos originarios poco presentes. En el campo cambiaron más despacio porque faltaban escuelas cercanas.",
        ["dos columnas", "tres filas", "frase sobre territorio"], ["tabla y frase"], ["poner solo cambios", "no hablar de territorio"], "Pide a alguien de tu casa que revise que cada dato está en su columna."),
    reinforce="Escribe tres datos del cuadro y clasifícalos con las letras C (cambio) o K (continuidad).",
    extend="Escribe una pregunta sobre qué grupos no aparecen en el cuadro y por qué.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Ministro de educación: «Las escuelas formarán ciudadanos que conozcan las leyes de la República.» Maestra de una escuela primaria: «Mis alumnos aprenden a leer, pero faltan libros y bancas.» Escritor de la Sociedad Literaria: «Necesitamos una literatura que hable de Chile y de su gente.» Artesano de la Sociedad de la Igualdad: «Queremos que los trabajadores también participen en la vida pública.» Mujer que desea estudiar: «Pido poder rendir los exámenes de la universidad.»"
build(
    OA, 4, F4,
    use="Aprenderé a reconocer los actores que impulsaron la educación y la opinión pública, sus intereses y las causas de su expansión. Sirve para explicar que la idea de nación fue construida por varios grupos con intereses distintos y a veces opuestos.",
    prior=["Conozco la expansión de la prensa y las escuelas.", "Sé qué es la multicausalidad.", "Sé que una fuente refleja la perspectiva de su autor."],
    explain=[
        "Los espacios de opinión pública y de educación no se crearon solos. El Estado impulsó la Universidad de Chile, la Escuela Normal y la ley de instrucción primaria para formar ciudadanos y profesores. Intelectuales como Andrés Bello, Domingo Faustino Sarmiento y José Victorino Lastarria participaron en la universidad, en la escuela normal y en la Sociedad Literaria; los historiadores escribieron relatos del pasado nacional.",
        "También actuaron grupos de la sociedad. Artesanos y trabajadores formaron organizaciones, como la Sociedad de la Igualdad, para participar en la vida pública. Hubo debates sobre quién debía dirigir la educación: el Estado, la Iglesia o ambos. Las mujeres pidieron poder estudiar y obtuvieron el decreto Amunátegui en 1877. Cada actor tenía intereses distintos: formar ciudadanos, difundir una cultura, ganar participación o abrir derechos.",
        "Las causas de la expansión educacional fueron varias: el deseo del Estado de organizar la nación, la demanda de personas que querían leer y participar, el crecimiento de las ciudades y los recursos fiscales. Por eso hablamos de multicausalidad. Y como los actores tenían intereses y poderes distintos, la idea de nación no fue la misma para todos: algunos la definían como unidad cultural, otros pedían más derechos.",
    ],
    vocab=[("ciudadano", "persona que tiene derechos y deberes políticos"), ("intelectual", "persona que se dedica a pensar, escribir y enseñar sobre asuntos públicos"), ("interés", "aquello que un actor busca lograr"), ("debate", "discusión en que se defienden posturas distintas"), ("participación", "intervención de las personas en la vida pública")],
    worked=[
        ("Emparejar actor e interés", "En las voces de ejemplo, ¿qué busca el ministro de educación y qué busca el artesano de la Sociedad de la Igualdad?",
         ["El ministro quiere formar ciudadanos que conozcan las leyes.", "El artesano quiere que los trabajadores participen en la vida pública."], "El ministro busca formar ciudadanos; el artesano, participación de los trabajadores"),
        ("Contrastar perspectivas", "La maestra dice que faltan libros y bancas. ¿En qué se diferencia su perspectiva de la del ministro?",
         ["El ministro habla de lo que se espera de las escuelas.", "La maestra habla de las condiciones concretas del aula.", "Así se ve la distancia entre el proyecto y la práctica."], "El ministro habla del proyecto; la maestra, de las condiciones reales"),
    ],
    mistakes=[
        ("Creer que la nación fue construida solo por el Estado.", "También actuaron intelectuales, maestras, artesanos y mujeres.", "Haz una lista de actores y de sus intereses."),
        ("Suponer que todos los actores entendían la nación de la misma manera.", "Cada grupo la definía según sus intereses.", "Pregunta qué derechos o lugares buscaba cada actor."),
    ],
    T=[
        ("En Historia: ¿qué es un ciudadano?", "Una persona que tiene derechos y deberes políticos", "Es el sujeto que la educación buscaba formar."),
        ("{F} ¿Qué busca el escritor de la Sociedad Literaria?", "Una literatura que hable de Chile y de su gente", "Su voz lo dice."),
        ("{F} ¿Qué pide la mujer que desea estudiar?", "Poder rendir los exámenes de la universidad", "Su voz lo dice."),
        ("{F} ¿Qué problema concreto señala la maestra? A) faltan libros y bancas, B) sobra dinero, C) hay demasiados maestros.", "A", "Describe una limitación material de la escuela."),
        ("Une cada actor con su interés: 1) ministro, 2) artesano, 3) mujer que desea estudiar. a) participar en la vida pública, b) formar ciudadanos, c) estudiar en la universidad. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada voz expresa un interés distinto."),
        ("{F} Elige el actor cuyo interés se relaciona con un decreto de 1877. A) la mujer que desea estudiar, B) el ministro, C) el escritor.", "A", "El decreto Amunátegui abrió la universidad a las mujeres."),
        ("=", "En una escuela de ejemplo hay 60 alumnos y 20 libros de lectura. ¿Cuántos alumnos hay por cada libro?", "60//20", "Se divide el número de alumnos entre los libros."),
        ("=", "Una sociedad de artesanos de ejemplo tiene 90 socios; 35 saben leer y el resto no. ¿Cuántos socios no saben leer?", "90-35", "Se resta los que saben leer del total."),
        ("{F} Explica por qué la nación no era la misma idea para el ministro y para el artesano.", "El ministro pensaba en formar ciudadanos desde el Estado y el artesano pedía participación de los trabajadores", "Sus intereses y poderes eran distintos."),
        ("Una compañera dice que la expansión de la educación se debió solo a la voluntad del Estado. Menciona otra causa.", "La demanda de personas que querían leer y participar o el crecimiento de las ciudades", "La multicausalidad incluye demanda social."),
        ("{F} ¿Qué diferencia de poder hay entre el ministro y la maestra en las voces de ejemplo?", "El ministro decide el proyecto y la maestra lo aplica con pocos recursos", "Sus posiciones en el sistema son distintas."),
        ("Evalúa la afirmación «la nación fue construida por un solo actor con una idea única». A) es falsa porque participaron varios actores con intereses distintos, B) es verdadera porque solo el Estado actuaba, C) es verdadera porque nadie discutía.", "A", "Hubo varios actores y debates."),
        ("Redacta una pregunta que contraste la perspectiva de la mujer que desea estudiar con la del ministro.", "Por ejemplo: ¿qué derechos buscaba cada uno al hablar de educación?", "La pregunta compara intereses."),
    ],
    ctx=("{F} En una obra escolar sobre 1850, un compañero hace que el ministro, la maestra y el artesano digan lo mismo sobre la educación. ¿Cómo ayudarías a que cada personaje exprese su perspectiva?", "Hacer que el ministro hable de formar ciudadanos, la maestra de la falta de libros y el artesano de participar", "Cada personaje debe hablar desde su interés."),
    sc=[("En Historia: ¿qué es un debate?", "Una discusión en que se defienden posturas distintas", "Muestra que hay perspectivas diversas."),
        ("Nombra dos actores que impulsaron la educación.", "Por ejemplo: el Estado y los intelectuales", "Ambos participaron en las instituciones."),
        ("¿Qué decreto de 1877 permitió a las mujeres ingresar a la universidad?", "El decreto Amunátegui", "Es el hecho citado en la clase.")],
    op=("{F} Elige dos voces de ejemplo de arriba y escribe cinco líneas: qué busca cada una, una diferencia de poder entre ambas y una causa de la expansión de la educación distinta de la voluntad del Estado.",
        "El ministro busca formar ciudadanos y la maestra enseñar con pocos libros. El ministro tiene más poder de decisión y la maestra trabaja con pocos recursos. Otra causa fue la demanda de personas que querían aprender a leer.",
        ["dos voces", "diferencia de poder", "otra causa"], ["texto de cinco líneas"], ["no marcar diferencia de poder", "usar una sola voz"], "Lee tu texto a alguien de tu casa y comprueba que entiende el contraste."),
    reinforce="Haz una tabla con cuatro actores del tema y escribe un interés para cada uno.",
    extend="Explica por qué los debates sobre quién debe dirigir la educación son parte de la historia de la nación.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Dossier de ejemplo. Dato 1: se fundó la Universidad de Chile (1842) y la Escuela Normal de Preceptores (1842). Dato 2: la Ley de Instrucción Primaria de 1860 fijó escuelas gratuitas. Dato 3: la prensa y la historiografía difundieron relatos comunes sobre el pasado de Chile. Dato 4: en el campo había menos escuelas y las mujeres solo ingresaron a la universidad en 1877."
build(
    OA, 5, F5,
    use="Aprenderé a escribir un argumento con tesis, evidencia y límite sobre si la prensa y la educación expandieron la idea de nación y qué exclusiones persistieron. Sirve para responder preguntas históricas complejas con datos.",
    prior=["Conozco los espacios de opinión pública y de educación.", "Sé contextualizar y contrastar fuentes.", "Sé distinguir cambio y continuidad."],
    explain=[
        "Para argumentar en historia hay que partir de una pregunta y responderla con una tesis, es decir, una afirmación defendible. Ante la pregunta «¿Cómo contribuyeron la opinión pública y la educación a expandir y profundizar la idea de nación?», una tesis posible es que ayudaron a difundir relatos, saberes y símbolos comunes, pero con exclusiones persistentes.",
        "Luego se eligen evidencias pertinentes. Para esta tesis sirven el dato de que se fundaron la universidad y la escuela normal, el de que la ley de 1860 fijó escuelas gratuitas, el de que la prensa y la historiografía difundieron relatos comunes, y el de que las mujeres y el campo tuvieron menos acceso. Cada evidencia debe explicarse: no basta con citarla, hay que decir qué demuestra.",
        "Por último, el límite. Con estos datos no podemos afirmar que todos los chilenos compartieran la misma idea de nación ni medir cuánto influyó cada institución. Un buen argumento reconoce que hubo difusión y exclusión a la vez, y evita frases absolutas como «todos» o «nadie».",
    ],
    vocab=[("tesis", "afirmación principal que se defiende"), ("evidencia pertinente", "dato relacionado directamente con la tesis"), ("explicar la evidencia", "decir qué demuestra un dato respecto de la tesis"), ("límite", "aquello que la evidencia no permite afirmar"), ("afirmación absoluta", "frase con «todos», «nadie» o «siempre» que rara vez se sostiene")],
    worked=[
        ("Armar tesis y evidencia", "Con el dossier, ¿qué dos datos sostienen la tesis «la educación amplió el acceso al saber, aunque con exclusiones»?",
         ["El dato 1 y el dato 2 muestran la expansión institucional.", "El dato 4 muestra las exclusiones."], "Datos 1 y 2 para la ampliación, y dato 4 para la exclusión"),
        ("Detectar exageración", "¿Por qué la frase «todos los chilenos compartían la misma idea de nación» excede el dossier?",
         ["El dossier solo muestra instituciones y exclusiones.", "No prueba qué pensaba cada persona.", "«Todos» es una afirmación absoluta."], "Porque usa «todos» y el dossier no prueba lo que pensaba cada persona"),
    ],
    mistakes=[
        ("Citar un dato y no explicarlo.", "El lector no sabe qué demuestra.", "Después de cada dato escribe «esto muestra que…»."),
        ("Usar solo evidencia de un lado.", "El argumento queda parcial.", "Incluye datos de expansión y de exclusión."),
    ],
    T=[
        ("En Historia: ¿qué es una afirmación absoluta?", "Una frase con «todos», «nadie» o «siempre» que rara vez se sostiene", "Suele exceder la evidencia."),
        ("{F} ¿Qué dato muestra una exclusión? A) dato 1, B) dato 3, C) dato 4.", "C", "El dato 4 habla de menos escuelas rurales y de mujeres en la universidad desde 1877."),
        ("{F} ¿Qué dato menciona la ley de 1860?", "El dato 2", "Habla de escuelas gratuitas."),
        ("{F} ¿Qué dato muestra espacios de opinión pública y de relatos comunes?", "El dato 3", "Menciona prensa e historiografía."),
        ("Elige la tesis mejor formulada. A) La educación fue un invento sin importancia, B) La prensa y la educación ayudaron a difundir una idea común de nación, aunque con exclusiones, C) Todos pensaban igual.", "B", "Es defendible con datos y reconoce un límite."),
        ("Una compañera usa solo el dato 1 para decir que «la educación llegó a todos». ¿Qué le falta?", "El dato 4, que muestra que el campo y las mujeres tenían menos acceso", "La evidencia es parcial."),
        ("=", "{F} Si el dossier tiene 4 datos y 2 muestran expansión (1 y 2), ¿cuántos datos quedan para otros temas?", "4-2", "Se restan los datos usados."),
        ("=", "Un grupo de ejemplo escribe un texto de 12 líneas: 2 de tesis, 6 de evidencia y el resto de límite. ¿Cuántas líneas son de límite?", "12-2-6", "Se restan tesis y evidencias del total."),
        ("{F} Con los datos 2 y 4, redacta una conclusión proporcional.", "La ley de 1860 fijó escuelas gratuitas, pero el acceso fue menor en el campo y las mujeres tardaron en llegar a la universidad", "Une expansión y exclusión sin exagerar."),
        ("Explica por qué una tesis necesita un límite.", "Porque evita afirmar más de lo que los datos permiten", "El límite protege de la exageración."),
        ("Un compañero escribe: «La educación en el siglo XIX eliminó todas las desigualdades». Señala la exageración y corrígela.", "Afirma «todas» sin evidencia; el dato 4 muestra desigualdades que continuaron", "Hay datos contrarios."),
        ("Evalúa este argumento: «La prensa y la universidad difundieron relatos comunes (datos 1 y 3), pero las mujeres y el campo tuvieron menos acceso (dato 4)». A) es sólido porque usa evidencia de ambos lados, B) es débil porque solo presenta datos de expansión y ninguno de exclusión, C) es falso porque la prensa no tuvo ninguna influencia en la idea de nación.", "A", "Tiene tesis y evidencias de ambos lados."),
        ("Escribe una pregunta que exigiría otra fuente para completar el argumento.", "Por ejemplo: ¿qué pensaban las familias del campo sobre mandar a sus hijos a la escuela?", "La pregunta indica un vacío del dossier."),
    ],
    ctx=("{F} En un foro del colegio, alguien dice que «la historia nacional enseñada en el siglo XIX incluía a todos los grupos del país». Con el dossier, escribe en dos frases tu respuesta y una evidencia.", "No necesariamente: el dato 4 muestra exclusiones de mujeres y del campo, y el dossier no menciona a los pueblos originarios", "La respuesta debe apoyarse en un dato."),
    sc=[("En Historia: ¿qué es explicar una evidencia?", "Decir qué demuestra un dato respecto de la tesis", "No basta con citarlo."),
        ("Nombra un dato de expansión educativa.", "Por ejemplo: la fundación de la Universidad de Chile en 1842", "Es un hecho del dossier."),
        ("¿Qué exclusión mantuvo la educación según el dossier?", "Las mujeres solo ingresaron a la universidad en 1877 y el campo tuvo menos escuelas", "Es el dato 4.")],
    op=("{F} Con el dossier de ejemplo de arriba, escribe un párrafo de siete líneas que responda: «¿Cómo ayudaron la prensa y la educación a construir la nación y qué exclusiones persistieron?». Incluye una tesis, dos evidencias explicadas y un límite.",
        "La prensa, la historiografía y las instituciones educativas difundieron una idea común de nación. La universidad y la escuela normal de 1842 y la ley de 1860 ampliaron el acceso al saber. Sin embargo, las mujeres solo ingresaron en 1877 y en el campo había menos escuelas. Límite: el dossier no muestra lo que pensaba cada persona.",
        ["tesis clara", "dos evidencias explicadas", "límite"], ["párrafo de siete líneas"], ["omitir exclusiones", "no explicar los datos"], "Pide a una persona de tu casa que marque tu tesis en el texto."),
    reinforce="Reescribe tu tesis en una frase y anota debajo las dos evidencias que la apoyan.",
    extend="Escribe una segunda tesis posible, centrada en las exclusiones, y un dato nuevo que necesitarías.",
    materials=MAT,
)
