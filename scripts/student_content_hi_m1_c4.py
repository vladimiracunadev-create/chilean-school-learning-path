"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 24 (conflicto, convivencia y diversidad de los pueblos indígenas)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 24"
MAT = ("Lápiz y papel. Las fuentes y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet. "
       "No tienes que hablar de tu propia familia ni representar a ningún pueblo: trabajas con los casos escritos.")

# ---------------------------------------------------------------- Clase 1
F1 = ("Mapa en palabras, de ejemplo y a grandes rasgos. Norte de Chile (altiplano, valles y desierto): aymara, quechua, atacameño (también llamado lickanantay), colla y diaguita. "
      "Zona centro-sur: mapuche, en el campo y también en ciudades. "
      "Océano Pacífico: rapa nui, en la Isla de Pascua (Rapa Nui). "
      "Sur austral (canales y fiordos): kawéskar (también se escribe kawésqar) y yagán (también llamado yámana).")
build(
    OA, 1, F1,
    use="Aprenderé a ubicar a los nueve pueblos indígenas que nombra el OA y a plantear el problema de cómo han sido las relaciones entre ellos y el Estado. Sirve para no hablar de «los indígenas» como si fueran una sola cultura.",
    prior=["Sé leer un mapa descrito con palabras.", "Sé qué es una fuente y una perspectiva.", "Sé que Chile tiene zonas geográficas muy distintas."],
    explain=[
        "Un pueblo indígena es un conjunto de personas que descienden de quienes habitaban un territorio antes de que se formara el Estado actual y que mantienen rasgos culturales propios, como lengua, historia y formas de organización. En Chile se reconocen, entre otros, los pueblos aymara, quechua, atacameño o lickanantay, colla, diaguita, mapuche, rapa nui, kawéskar y yagán. Cada uno tiene su propia historia, lengua y territorio; no son una sola cultura.",
        "El territorio es el espacio que un pueblo habita, usa y al que da significado. Algunos pueblos se ubican en el norte, otros en la zona central y sur, otros en el Pacífico y otros en los canales del sur. Hoy muchas personas indígenas viven también en ciudades, de modo que cultura y territorio no siempre coinciden con el lugar donde alguien vive.",
        "Las relaciones entre los pueblos indígenas y el Estado han incluido conflicto, cuando hubo disputas por tierras, derechos o reconocimiento, y convivencia, cuando hubo acuerdos, intercambios y trabajo conjunto. El problema que estudiaremos es cómo evaluar esas relaciones con fuentes, sin generalizar y valorando la diversidad cultural, es decir, la existencia de muchas culturas que enriquecen a la sociedad.",
    ],
    vocab=[("pueblo indígena", "conjunto de personas descendientes de los primeros habitantes de un territorio, con rasgos culturales propios"), ("territorio", "espacio que un pueblo habita, usa y al que da significado"), ("diversidad cultural", "existencia de muchas culturas en una sociedad"), ("conflicto", "disputa entre grupos por tierras, derechos o reconocimiento"), ("convivencia", "vida en común basada en el respeto y los acuerdos")],
    worked=[
        ("Contar pueblos por zona", "En un mapa en palabras de ejemplo hay 3 pueblos en el norte, 2 en el sur y 1 en una isla. ¿Cuántos pueblos hay en total?",
         ["Sumo los pueblos de cada zona.", "3 + 2 + 1 = 6."], "6 pueblos"),
        ("Evitar una generalización", "Un texto de ejemplo dice: «Todos los pueblos indígenas hablan la misma lengua». ¿Qué error tiene?",
         ["Cada pueblo tiene lengua, historia y cultura propias.", "Decir «todos» borra esas diferencias."], "Generaliza como si fueran una sola cultura"),
    ],
    mistakes=[
        ("Hablar de «los indígenas» como si fueran una sola cultura.", "Cada pueblo tiene lengua, historia, territorio y formas de organización propias.", "Nombra el pueblo del que hablas."),
        ("Creer que los pueblos indígenas solo viven en el campo.", "Muchas personas indígenas viven hoy en ciudades.", "Distingue territorio de origen y lugar de residencia."),
    ],
    T=[
        ("En Historia: ¿qué es un pueblo indígena?", "Un conjunto de personas descendientes de los primeros habitantes de un territorio, con rasgos culturales propios", "Tiene lengua, historia y organización propias."),
        ("{F} ¿En qué zona se ubica el pueblo rapa nui?", "En el océano Pacífico, en la Isla de Pascua", "El mapa lo ubica en esa isla."),
        ("{F} ¿Qué pueblos se ubican en el sur austral? A) kawéskar y yagán, B) aymara y quechua.", "A", "Los canales y fiordos del sur son su zona."),
        ("=", "{F} ¿Cuántos pueblos se nombran en el norte?", "5", "Son aymara, quechua, atacameño, colla y diaguita."),
        ("{F} ¿Cuántos pueblos aparecen en total en el mapa en palabras?", "9", "Son 5 del norte, 1 mapuche, 1 rapa nui y 2 del sur austral."),
        ("En Historia: ¿qué es la diversidad cultural? A) la existencia de muchas culturas en una sociedad, B) que todas las personas piensen igual.", "A", "Es la existencia de varias culturas."),
        ("=", "{F} Una exposición escolar dedica 2 carteles a cada uno de los pueblos nombrados en el mapa. ¿Cuántos carteles necesita?", "9*2", "Se multiplica el número de pueblos por los carteles de cada uno."),
        ("=", "{F} En una gira escolar de ejemplo se visitan los pueblos del norte. ¿Cuántos de los pueblos nombrados en el mapa no se visitan?", "9-5", "Se resta el número de pueblos del norte al total."),
        ("{F} Una persona dice: «Los pueblos indígenas solo viven en el campo». ¿Qué dato del mapa la contradice? A) que el pueblo mapuche vive también en ciudades, B) que el pueblo rapa nui vive en una isla.", "A", "El mapa dice que los mapuche viven también en ciudades."),
        ("{F} Un compañero escribe: «Los pueblos del norte y del sur austral son la misma cultura». ¿Qué debería hacer para corregirlo? A) nombrar cada pueblo y sus rasgos propios, B) usar la palabra «todos».", "A", "Cada pueblo tiene rasgos distintos."),
        ("{F} ¿Por qué ayuda ubicar a los pueblos en el mapa antes de estudiar sus relaciones con el Estado? Responde con una frase.", "Porque cada pueblo tiene un territorio y una historia distinta, y no se pueden mezclar", "Así se evita generalizar a todos los pueblos."),
        ("En una ciudad de ejemplo, 2.000 de 10.000 personas tienen ascendencia de un pueblo indígena. ¿Qué parte del total son? A) una quinta parte, B) la mitad.", "A", "2.000 es la quinta parte de 10.000."),
        ("{F} Un panel escolar dice «Los pueblos originarios: una sola cultura». ¿Qué título lo corrige mejor? A) «Pueblos originarios: nueve culturas distintas», B) «Pueblos originarios: todos iguales».", "A", "Reconoce la diversidad."),
    ],
    ctx=("Un colegio de ejemplo prepara una muestra con carteles de los nueve pueblos. Una estudiante propone mezclar todos los datos en un solo cartel «Pueblos indígenas». ¿Qué conviene hacer? A) un cartel por pueblo, con su lugar y rasgos, B) un solo cartel con todos los datos mezclados.", "A", "Así se respeta la diversidad."),
    sc=[("En Historia: ¿por qué no se debe hablar de una sola cultura indígena?", "Porque cada pueblo tiene lengua, historia y territorio propios", "La diversidad se pierde al generalizar."),
        ("En Historia: ¿Qué es el territorio?", "El espacio que un pueblo habita, usa y al que da significado", "No es solo el lugar donde se vive hoy."),
        ("Nombra dos zonas de Chile donde viven pueblos indígenas.", "Por ejemplo: el norte y los canales del sur austral", "Están en el mapa en palabras.")],
    op=("{F} Elige tres pueblos del mapa y escribe para cada uno: en qué zona se ubica y una pregunta que harías para conocer mejor su relación con el Estado. Termina con una frase que explique por qué no se puede hablar de «los indígenas» como una sola cultura. No tienes que hablar de ninguna persona real.",
        "Mapuche: zona central y sur, campo y ciudades; ¿qué conflictos hubo por tierras? Rapa nui: Isla de Pascua; ¿cómo se incorporó a Chile? Aymara: norte; ¿cómo vive hoy la frontera? No son una sola cultura porque cada pueblo tiene lengua y territorio propios.",
        ["ubica tres pueblos", "formula tres preguntas", "explica la diversidad"], ["tres pueblos, tres preguntas y una frase"], ["mezclar pueblos distintos", "hablar de personas reales"], "Pide a una persona de tu casa que lea tus preguntas y diga cuál le pareció más interesante."),
    reinforce="Escribe los nueve pueblos en una lista y, al lado de cada uno, la zona donde se ubica.",
    extend="Explica por qué un pueblo puede tener personas que viven lejos de su territorio de origen.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Fuente A (de ejemplo, resumen actual de una ley de 1993): la ley chilena de 1993 establece normas de protección, fomento y desarrollo de los indígenas y crea un organismo del Estado para apoyarlos. "
      "Fuente B (de ejemplo, testimonio actual escrito para este ejercicio, sin nombre real): «En mi comunidad enseñamos nuestra lengua a niños y niñas, y queremos que también se enseñe en la escuela del pueblo.» "
      "Fuente C (de ejemplo, columna de un periódico ficticio de fines del siglo XIX): «El gobierno debe extender su autoridad y poblar con colonos los territorios del sur.» "
      "Fuente D (de ejemplo, texto escolar actual): «Las relaciones entre el Estado y los pueblos indígenas han tenido momentos de conflicto y de convivencia, y varían según el pueblo y la época.»")
build(
    OA, 2, F2,
    use="Aprenderé a leer fuentes de distinto tipo sobre pueblos indígenas y a reconocer de quién es la voz y qué parte de la historia muestra. Sirve para evaluar las relaciones entre pueblos indígenas y Estado sin quedarme con una sola mirada.",
    prior=["Sé distinguir fuente primaria de secundaria.", "Sé qué es una perspectiva.", "Conozco los pueblos indígenas de Chile."],
    explain=[
        "Para estudiar las relaciones entre los pueblos indígenas y el Estado se usan fuentes variadas: leyes y documentos oficiales, testimonios de personas de comunidades, periódicos de una época y textos escolares. Cada una responde a preguntas distintas. Una ley muestra lo que el Estado decidió; un testimonio muestra una experiencia; un periódico antiguo muestra la mirada de quienes lo escribían en su época; un texto escolar interpreta y resume.",
        "Una fuente primaria nace en la época o situación estudiada, como una ley o una columna de periódico de esa época. Una fuente secundaria se escribe después y explica lo ocurrido. Es importante preguntar quién habla y quién no habla. Si solo leemos fuentes del Estado, falta la voz de los pueblos; si solo leemos un testimonio, falta una mirada general. Un testimonio habla por una persona o comunidad, no por todo un pueblo.",
        "Al contrastar fuentes busco coincidencias y diferencias, y reviso si alguna usa expresiones que hoy resultarían discriminatorias o que presentan una sola mirada. Una conclusión sólida se limita a lo que las fuentes permiten afirmar y dice qué voces faltan.",
    ],
    vocab=[("fuente oficial", "documento escrito por el Estado o una institución pública"), ("testimonio", "relato de una persona sobre lo que vivió o piensa"), ("voz", "persona o grupo cuyo punto de vista aparece en una fuente"), ("generalizar", "afirmar de todo un grupo lo que se observó en una parte"), ("discriminatorio", "que trata a una persona o grupo de manera injusta por su origen o cultura")],
    worked=[
        ("Clasificar una fuente", "Una carta de 1890 escrita por un funcionario del gobierno sobre los territorios del sur, ¿es primaria o secundaria?",
         ["Se escribió en la época que se estudia.", "Eso la hace una fuente primaria."], "Primaria"),
        ("Identificar la voz ausente", "Un texto del Estado sobre un pueblo indígena no cita a ninguna persona de ese pueblo. ¿Qué voz falta?",
         ["El texto presenta solo la mirada del Estado.", "Falta la voz del pueblo mismo."], "La voz del pueblo indígena"),
    ],
    mistakes=[
        ("Usar un testimonio como si hablara por todo un pueblo.", "Un testimonio expresa la experiencia de una persona o comunidad.", "Di quién habla y no generalices."),
        ("Usar solo fuentes del Estado.", "Faltaría la voz de las comunidades.", "Combina fuentes oficiales y testimonios."),
    ],
    T=[
        ("En Historia: ¿qué es un testimonio?", "El relato de una persona sobre lo que vivió o piensa", "Muestra una experiencia concreta."),
        ("{F} ¿Qué fuente es un texto escolar actual?", "La fuente D", "Resume e interpreta las relaciones."),
        ("{F} ¿Qué fuente muestra la mirada de quienes querían extender la autoridad del Estado? A) la fuente C, B) la fuente B.", "A", "Pide poblar con colonos el sur."),
        ("{F} ¿Qué fuente es un testimonio de una comunidad? A) la fuente B, B) la fuente A.", "A", "Habla de «mi comunidad»."),
        ("{F} ¿Qué fuente muestra lo que el Estado decidió por ley? A) la fuente A, B) la fuente D.", "A", "Resume una ley."),
        ("{F} ¿Cuál de estas dos fuentes es secundaria, es decir, escrita después para explicar lo ocurrido? A) la fuente D, B) la fuente C.", "A", "Interpreta lo ocurrido después."),
        ("{F} ¿Qué voz falta en la fuente C? A) la voz de los pueblos del sur, B) la voz del gobierno.", "A", "Solo habla la mirada de quien escribe sobre ellos."),
        ("{F} Un compañero afirma: «La fuente B muestra lo que piensan todos los pueblos indígenas». ¿Qué error comete? Responde con una frase.", "Generaliza: un testimonio habla de una comunidad, no de todos los pueblos", "Un testimonio no representa a todo un grupo."),
        ("{F} Para saber qué decidió el Estado en 1993, ¿qué fuente conviene? A) la fuente A, B) la fuente B.", "A", "Resume la ley."),
        ("{F} Para saber qué le interesa hoy a una comunidad sobre su lengua, ¿qué fuente conviene? A) la fuente B, B) la fuente C.", "A", "Es un testimonio actual sobre lengua."),
        ("{F} Una frase de la fuente C se refiere a «poblar» los territorios del sur. ¿Qué mirada deja de lado? A) la de las comunidades que ya vivían allí, B) la de los colonos.", "A", "Habla como si el territorio estuviera vacío."),
        ("=", "{F} Si la columna de la fuente C se escribió en 1890 (año de ejemplo), ¿cuántos años pasaron hasta la ley de 1993?", "1993-1890", "Se resta el año menor al mayor."),
        ("{F} Elige la conclusión mejor sostenida. A) las fuentes muestran distintas voces y falta incluir más testimonios, B) las fuentes prueban lo que piensan todos los pueblos.", "A", "Las fuentes son pocas y de voces distintas."),
    ],
    ctx=("Un curso de ejemplo prepara un trabajo sobre la relación del Estado con un pueblo indígena. Tiene tres fuentes oficiales y ninguna con voz de la comunidad. ¿Qué debe agregar? A) un testimonio de la comunidad, B) otra fuente oficial igual.", "A", "Falta la voz del pueblo."),
    sc=[("En Historia: ¿qué es una fuente oficial?", "Un documento escrito por el Estado o una institución pública", "Muestra su mirada."),
        ("¿Por qué un testimonio no habla por todo un pueblo?", "Porque expresa la experiencia de una persona o comunidad", "No se puede generalizar."),
        ("¿Qué pregunta ayuda a leer una fuente?", "¿Quién habla y quién no habla?", "Revela las voces ausentes.")],
    op=("{F} Elige dos fuentes distintas y escribe para cada una: tipo (primaria o secundaria), quién habla y qué voz falta. Termina con una frase que explique qué ganas al usarlas juntas y qué fuente adicional pedirías.",
        "Fuente A: secundaria (resumen de una ley); habla el Estado; falta la voz de las comunidades. Fuente B: testimonio actual; habla una comunidad; falta la mirada general. Juntas muestran decisión y experiencia. Pediría un testimonio de otro pueblo.",
        ["clasifica dos fuentes", "indica quién habla y quién no", "justifica el uso conjunto"], ["dos fuentes analizadas y una conclusión"], ["tomar un testimonio como voz de todo un pueblo", "no indicar la voz que falta"], "Léele tu respuesta a una persona de tu casa y pídele que diga qué voz le parece que falta."),
    reinforce="Escribe tres preguntas para hacerle a cualquier fuente histórica.",
    extend="Explica por qué las palabras con que se describe a un pueblo en una fuente antigua pueden mostrar prejuicios de su época.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Resumen de ejemplo, a grandes rasgos y con algunos hechos reales. "
      "Pueblo mapuche: hasta mediados del siglo XIX, amplias zonas al sur del río Biobío estaban fuera del control del Estado chileno; en la segunda mitad del siglo XIX el Estado ocupó esa zona y se instalaron colonos; hoy hay comunidades en el campo y también muchas personas mapuche viven en ciudades. "
      "Pueblo rapa nui: en 1888 la isla fue anexada a Chile; hoy forma parte de la Región de Valparaíso y su lengua se sigue hablando y enseñando. "
      "Pueblo aymara: tras la Guerra del Pacífico (iniciada en 1879), territorios del norte pasaron a Chile y se aplicaron políticas de chilenización, es decir, de imposición de la identidad nacional chilena; hoy existen programas de educación intercultural bilingüe en algunas escuelas del norte. "
      "Ley de 1993: reconoce a los pueblos indígenas y crea un organismo del Estado para apoyarlos.")
build(
    OA, 3, F3,
    use="Aprenderé a describir qué cambió y qué continuó en la historia de algunos pueblos indígenas desde el siglo XIX hasta hoy, y cómo el territorio influyó. Sirve para evaluar conflicto y convivencia con evidencia.",
    prior=["Conozco los pueblos indígenas de Chile y su ubicación.", "Sé distinguir cambio y continuidad.", "Sé calcular años entre dos fechas."],
    explain=[
        "El territorio es una clave para entender las relaciones entre los pueblos indígenas y el Estado. En el siglo XIX el Estado chileno extendió su autoridad sobre territorios que antes no controlaba: al sur del Biobío, en la isla de Rapa Nui (anexada en 1888) y, después de la Guerra del Pacífico, en el norte. Estos procesos incluyeron ocupación de tierras, llegada de colonos y políticas de chilenización, y generaron conflictos y pérdida de territorios.",
        "Ha habido cambios importantes. Muchas comunidades perdieron tierras, parte de la población migró a las ciudades y, en 1993, una ley reconoció a los pueblos indígenas y creó un organismo estatal para apoyarlos. También surgieron programas de educación intercultural bilingüe, que enseñan en dos lenguas. Estos cambios muestran un avance en el reconocimiento, aunque las demandas siguen abiertas.",
        "Pero también hay continuidades: las lenguas se siguen hablando y enseñando, las comunidades mantienen formas de organización propias y los pueblos siguen reclamando derechos sobre sus territorios. Una descripción equilibrada no dice que todo cambió ni que nada cambió: separa lo que se perdió, lo que se transformó y lo que sigue vivo, y lo ubica en cada territorio.",
    ],
    vocab=[("anexar", "incorporar un territorio al control de otro Estado"), ("colono", "persona que se instala en un territorio para vivir y trabajar en él"), ("chilenización", "política que buscó imponer la identidad nacional chilena"), ("educación intercultural bilingüe", "enseñanza que usa dos lenguas y valora la cultura de los pueblos indígenas"), ("demanda", "petición que un grupo hace a las autoridades")],
    worked=[
        ("Calcular años entre dos hechos", "Si un hecho ocurrió en 1861 y otro en 1888, ¿cuántos años pasaron entre ambos?",
         ["Resto el año menor al mayor.", "1888 - 1861 = 27."], "27 años"),
        ("Separar cambio y continuidad", "Una comunidad de ejemplo perdió parte de sus tierras en el siglo XIX, pero su lengua se sigue hablando hoy. ¿Qué cambió y qué continuó?",
         ["Cambió la extensión de las tierras.", "Continuó la lengua."], "Cambió el territorio; continuó la lengua"),
    ],
    mistakes=[
        ("Decir que, tras la ocupación, los pueblos indígenas desaparecieron.", "Los pueblos siguen existiendo, con lenguas, organización y demandas.", "Busca qué continuó además de lo que cambió."),
        ("Mezclar la historia de pueblos distintos como si fuera la misma.", "El mapuche, el rapa nui y el aymara tuvieron procesos distintos en lugares distintos.", "Cuenta la historia de cada pueblo por separado."),
    ],
    T=[
        ("En Historia: ¿qué significa anexar un territorio?", "Incorporarlo al control de otro Estado", "El Estado lo incorporó a su territorio."),
        ("{F} ¿En qué año fue anexada la isla Rapa Nui a Chile?", "1888", "El resumen lo informa."),
        ("{F} ¿Qué pueblo vivió políticas de chilenización tras la Guerra del Pacífico? A) el aymara, B) el rapa nui.", "A", "El resumen lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre la anexación de Rapa Nui y la ley de 1993?", "1993-1888", "Se resta el año menor al mayor."),
        ("=", "{F} ¿Cuántos años pasaron entre el inicio de la Guerra del Pacífico y la anexación de Rapa Nui?", "1888-1879", "Se resta el año menor al mayor."),
        ("{F} ¿Qué cambió para el pueblo mapuche en el siglo XIX? A) el Estado ocupó la zona al sur del Biobío, B) la lengua mapuche desapareció.", "A", "El resumen habla de ocupación y colonos."),
        ("{F} ¿Qué continuó para el pueblo rapa nui? A) su lengua se sigue hablando y enseñando, B) la gente rapa nui dejó de vivir en la isla.", "A", "El resumen lo señala."),
        ("{F} ¿Qué novedad de 1993 muestra un cambio en el reconocimiento? A) una ley que reconoce a los pueblos indígenas, B) el fin de todos los conflictos.", "A", "Hubo reconocimiento legal."),
        ("{F} ¿Qué territorio explica una política de chilenización? A) el norte, tras la Guerra del Pacífico, B) la Isla de Pascua en 1993.", "A", "El resumen asocia la chilenización a esa guerra."),
        ("{F} Una persona dice: «Con la ley de 1993 terminaron las demandas de los pueblos indígenas». ¿Qué respuesta es mejor? A) la ley fue un avance, pero las demandas siguen abiertas, B) es correcto.", "A", "El reconocimiento no cierra todos los reclamos."),
        ("{F} Un compañero escribe: «Los pueblos mapuche, rapa nui y aymara tuvieron la misma historia». ¿Qué dato lo contradice? Responde con una frase.", "Que cada uno vivió procesos distintos en lugares distintos, como la ocupación al sur del Biobío, la anexación de Rapa Nui y la chilenización en el norte", "Los procesos fueron diferentes."),
        ("{F} ¿Qué dato muestra una continuidad cultural en varios pueblos? Responde con una frase.", "Que las lenguas se siguen hablando y enseñando y que hay programas de educación intercultural bilingüe", "Las lenguas siguen vivas."),
        ("=", "{F} Si el organismo se creó junto con la ley de 1993, ¿en qué año cumple 30 años de existencia?", "1993+30", "Se suman los 30 años al año de la ley."),
    ],
    ctx=("Un periódico escolar de ejemplo titula: «Los pueblos indígenas ya no existen en Chile». ¿Qué dato del resumen contradice el titular? A) las lenguas se siguen hablando y hay comunidades y programas de educación intercultural, B) la ley de 1993 desapareció.", "A", "Muestra que los pueblos continúan."),
    sc=[("En Historia: ¿qué significa chilenización?", "Una política que buscó imponer la identidad nacional chilena", "Se aplicó en el norte tras la Guerra del Pacífico."),
        ("¿Qué es la educación intercultural bilingüe?", "Una enseñanza que usa dos lenguas y valora la cultura de los pueblos indígenas", "Es un cambio reciente."),
        ("¿Por qué conviene separar la historia de cada pueblo?", "Porque cada uno vivió procesos distintos en lugares distintos", "Evita mezclar situaciones diferentes.")],
    op=("{F} Elige un pueblo y escribe un párrafo con: un cambio, una continuidad, el territorio donde ocurrió y un cálculo de años entre dos hechos del resumen. No tienes que hablar de ninguna persona real.",
        "Pueblo rapa nui: cambió su situación al ser anexada la isla en 1888; continuó el uso de su lengua. Territorio: Isla de Pascua. Entre 1888 y 1993 pasaron 105 años.",
        ["nombra un cambio y una continuidad", "ubica el territorio", "calcula años"], ["un párrafo con un cálculo"], ["mezclar pueblos", "decir que el pueblo desapareció"], "Pide a una persona de tu casa que compruebe tu resta."),
    reinforce="Anota tres hechos del resumen con su año y el pueblo al que corresponden.",
    extend="Explica por qué la pérdida de tierras puede afectar la continuidad de una cultura.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Caso de ejemplo, valle ficticio «Valle Claro» en el norte. Un río lleva 100 litros de agua por segundo. Hoy lo usan: una comunidad indígena ficticia, 30 litros por segundo; el pueblo, 20; una empresa agrícola, 20. "
      "La empresa pide 40 litros por segundo más para regar nuevos cultivos. "
      "Voz de la empresa (de ejemplo): «Daremos 200 empleos y exportaremos fruta.» "
      "Voz de la comunidad (de ejemplo): «Si usan toda el agua, se secan nuestros cultivos y la vida ligada al río; pedimos ser consultados.» "
      "Voz del municipio (de ejemplo): «Necesitamos empleo, pero también cuidar el valle.» "
      "Voz del Estado (de ejemplo): «Debemos revisar los datos del agua y consultar a todas las partes antes de decidir.»")
build(
    OA, 4, F4,
    use="Aprenderé a contrastar actores, causas y perspectivas en un conflicto por recursos donde participa una comunidad indígena. Sirve para ver cómo se buscan acuerdos sin caricaturizar a nadie.",
    prior=["Sé que cada actor tiene una perspectiva.", "Conozco la diferencia entre conflicto y convivencia.", "Sé hacer sumas y restas con cantidades."],
    explain=[
        "En muchos conflictos por recursos como el agua o la tierra participan comunidades indígenas, empresas, municipios y el Estado. Cada actor tiene intereses y una perspectiva distinta: la empresa busca producir y dar empleo; la comunidad busca conservar el agua para sus cultivos y su forma de vida; el municipio busca equilibrar empleo y cuidado del valle; el Estado debe decidir con información y con reglas.",
        "Las causas de estos conflictos son varias, es decir, hay multicausalidad: el agua es limitada, hay usos que compiten, hay intereses económicos y hay derechos de las comunidades. Un mecanismo de convivencia es la consulta, que consiste en preguntar a las comunidades afectadas, con información clara y a tiempo, antes de tomar una decisión que las afecte. La consulta no significa que todos obtengan lo que piden, sino que su voz se escuche de verdad.",
        "Para evaluar un caso conviene calcular los datos, por ejemplo si el agua alcanza, y pedir más información. También hay que evitar caricaturas: ni todas las empresas dañan, ni todas las comunidades se oponen al desarrollo. Un buen análisis busca acuerdos que consideren el recurso, el empleo, los derechos y la sostenibilidad del valle.",
    ],
    vocab=[("consulta", "proceso de preguntar a las comunidades afectadas, con información clara, antes de decidir"), ("recurso", "elemento natural que se usa para producir o vivir, como el agua"), ("caudal", "cantidad de agua que lleva un río en un tiempo dado"), ("sostenible", "que se puede mantener en el tiempo sin agotar el recurso"), ("acuerdo", "decisión aceptada por todas las partes")],
    worked=[
        ("Calcular si alcanza el recurso", "Un río de ejemplo lleva 50 litros por segundo. Hoy se usan 35 y alguien pide 20 más. ¿Alcanza el agua?",
         ["Sumo el uso actual y la petición: 35 + 20 = 55.", "Comparo con el caudal: 55 es mayor que 50."], "No alcanza; faltan 5 litros por segundo"),
        ("Asociar una voz con un interés", "Una voz de ejemplo dice: «Pedimos ser consultados antes de que se decida». ¿Qué interés tiene?",
         ["Pide participar en la decisión.", "Su interés es que se escuche a la comunidad."], "Que se escuche a la comunidad"),
    ],
    mistakes=[
        ("Presentar a la empresa o a la comunidad como un villano.", "Cada actor tiene intereses y razones; una caricatura no explica el conflicto.", "Describe los intereses y los datos de cada uno."),
        ("Confundir consulta con tener siempre la razón.", "La consulta busca escuchar y considerar la voz de las comunidades; no garantiza que se acepte todo lo que piden.", "Distingue ser escuchado de obtener todo."),
    ],
    T=[
        ("En Historia: ¿qué es una consulta a una comunidad?", "Un proceso de preguntar a las comunidades afectadas, con información clara, antes de decidir", "Busca que su voz se escuche."),
        ("{F} ¿Cuántos litros por segundo lleva el río de Valle Claro?", "100", "El caso lo informa."),
        ("{F} ¿Qué actor pide ser consultado? A) la comunidad, B) la empresa.", "A", "Lo dice su voz."),
        ("=", "{F} ¿Cuántos litros por segundo se usan hoy en total?", "30+20+20", "Se suman los tres usos."),
        ("=", "{F} Con el uso actual, ¿cuántos litros por segundo quedan libres?", "100-(30+20+20)", "Se resta el uso actual al caudal."),
        ("=", "{F} Si se agrega lo que pide la empresa, ¿cuánto sería el uso total (en litros por segundo)?", "30+20+20+40", "Se suma la petición al uso actual."),
        ("=", "{F} ¿Cuánta agua faltaría si se aceptara la petición de la empresa (en litros por segundo)?", "30+20+20+40-100", "Se resta el caudal al uso total."),
        ("{F} ¿Alcanza el río para la petición? A) no, B) sí.", "A", "El uso total supera el caudal."),
        ("{F} ¿Qué voz equilibra empleo y cuidado del valle? A) la del municipio, B) la de la empresa.", "A", "Dice necesitar empleo y cuidar el valle."),
        ("{F} ¿Qué dato necesita el Estado antes de decidir? A) los datos del agua y la consulta a las partes, B) solo la opinión de la empresa.", "A", "Su voz lo dice."),
        ("{F} Un comentarista dice: «La comunidad se opone al desarrollo». Usando las voces, ¿qué le responderías? Responde con una frase.", "Que la comunidad pide ser consultada y cuidar el agua para sus cultivos, no oponerse al desarrollo en general", "Su voz expresa una preocupación concreta."),
        ("{F} ¿Qué solución podría considerar el recurso y el empleo? A) pedir una cantidad de agua menor a la empresa o usar riego que gaste menos, B) quitarle toda el agua a la comunidad.", "A", "Reduce el conflicto por el recurso."),
        ("=", "{F} Si la empresa aceptara pedir solo 10 litros por segundo más, ¿cuánta agua quedaría libre (en litros por segundo)?", "100-(30+20+20)-10", "Se resta la nueva petición al agua libre actual."),
    ],
    ctx=("Un municipio de ejemplo debe decidir sobre una nueva carretera que pasa por tierras de una comunidad indígena ficticia. ¿Qué paso es adecuado antes de decidir? A) consultar a la comunidad con información clara, B) informar a la comunidad después de empezar la obra.", "A", "La consulta debe hacerse antes de decidir."),
    sc=[("En Historia: ¿qué significa que un recurso sea limitado?", "Que hay una cantidad fija que no alcanza para todos los usos que se piden", "Genera competencia por su uso."),
        ("¿Para qué sirve una consulta?", "Para escuchar a las comunidades afectadas antes de decidir", "Permite considerar su voz."),
        ("¿Por qué conviene evitar caricaturas de empresas y comunidades?", "Porque cada actor tiene intereses y razones, y las caricaturas impiden entender el conflicto", "Se necesita un análisis con datos.")],
    op=("{F} Elige dos voces y escribe para cada una: qué actor es, qué interés tiene y qué dato del caso apoya o debilita su posición. Termina proponiendo una solución que considere el agua disponible, el empleo y la voz de la comunidad.",
        "Empresa: busca empleo y exportación; pide 40 litros, pero el río solo tiene 30 libres. Comunidad: busca conservar sus cultivos y ser consultada; ya usa 30 litros. Solución: pedirle a la empresa 30 litros o menos y usar riego eficiente, con consulta previa.",
        ["describe dos actores", "usa un dato del caso", "propone una solución"], ["dos voces y una solución"], ["culpar a un solo actor", "ignorar el caudal"], "Pide a una persona de tu casa que opine si tu solución escucha a todas las partes."),
    reinforce="Escribe tres preguntas que harías a una empresa y tres que harías a una comunidad antes de decidir un proyecto.",
    extend="Explica por qué la consulta no garantiza un acuerdo, pero sí mejora la calidad de la decisión.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Dossier de ejemplo, «¿Qué valor tiene la diversidad cultural?» en una escuela ficticia. "
      "Dato 1: la escuela tiene 120 estudiantes; 40 de ellos hablan en su casa una lengua indígena además del castellano. "
      "Dato 2: el programa intercultural dedica 2 horas semanales a enseñar lengua y saberes de pueblos indígenas, de un total de 40 horas de clases a la semana. "
      "Dato 3 (de ejemplo): un estudio pequeño encontró que la asistencia fue de 92 % con el programa y de 88 % antes de él. "
      "Dato 4 (de ejemplo): un vecino dice que ese tiempo restaría horas a matemática y a lenguaje.")
build(
    OA, 5, F5,
    use="Aprenderé a argumentar sobre el valor de la diversidad cultural con datos, una objeción y un límite. Sirve para participar en debates sobre educación y convivencia con respeto.",
    prior=["Conozco los pueblos indígenas y la diferencia entre conflicto y convivencia.", "Sé armar un argumento con tesis, evidencia, objeción y límite.", "Sé calcular porcentajes sencillos."],
    explain=[
        "La diversidad cultural es la existencia de varias culturas que conviven en una misma sociedad. Se considera un valor porque aporta lenguas, conocimientos, formas de vivir y maneras de ver el mundo, y porque el respeto mutuo mejora la convivencia. Valorar la diversidad no significa que todas las personas piensen igual ni que se oculten los conflictos, sino que se reconoce a cada pueblo y se busca el diálogo.",
        "Para argumentar con datos se pueden usar cifras, como el número de estudiantes que hablan una lengua indígena o el tiempo que ocupa un programa. También se pueden usar razones: que una lengua que se enseña tiene más posibilidades de mantenerse, que conocer otras culturas amplía la comprensión y que todos tienen derecho a su identidad. Pero las cifras y las razones deben ser proporcionales: un estudio pequeño no prueba un efecto general.",
        "Una objeción frecuente es que estos programas quitan tiempo a otras asignaturas. Una respuesta basada en datos compara cuánto tiempo ocupan realmente. El límite de un argumento es lo que los datos no permiten afirmar. Un argumento honesto lo dice y propone qué otra información haría falta.",
    ],
    vocab=[("diversidad cultural", "existencia de varias culturas que conviven en una sociedad"), ("identidad", "conjunto de rasgos con que una persona o grupo se reconoce a sí mismo"), ("diálogo", "conversación en que las partes se escuchan para entenderse"), ("proporcional", "que corresponde al tamaño de la evidencia disponible"), ("asistencia", "porcentaje de días de clases a los que van los estudiantes")],
    worked=[
        ("Calcular qué parte es un programa", "Un programa de ejemplo ocupa 3 horas semanales de un total de 30. ¿Qué porcentaje del tiempo es?",
         ["Divido 3 por 30.", "3 ÷ 30 × 100 = 10."], "10 % del tiempo"),
        ("Identificar un límite", "Un estudio de ejemplo con 20 estudiantes mostró mejoras. ¿Qué límite tiene para afirmar que ocurre en todo el país?",
         ["Son muy pocos estudiantes.", "No representa a todos los colegios."], "Que la muestra es pequeña para generalizar"),
    ],
    mistakes=[
        ("Afirmar que un programa mejora todo sin datos suficientes.", "Un estudio pequeño no prueba un efecto general.", "Indica el límite de los datos."),
        ("Pensar que valorar la diversidad es negar los conflictos.", "El diálogo y el reconocimiento exigen reconocer también los conflictos.", "Considera conflicto y convivencia."),
    ],
    T=[
        ("En Historia: ¿qué es la diversidad cultural?", "La existencia de varias culturas que conviven en una sociedad", "Es la idea central de la clase."),
        ("{F} ¿Cuántos estudiantes tiene la escuela?", "120", "El dato 1 lo informa."),
        ("{F} ¿Qué proporción de estudiantes habla una lengua indígena en su casa? A) un tercio, B) la mitad.", "A", "40 de 120 es un tercio."),
        ("=", "{F} ¿Qué porcentaje del tiempo de clases ocupa el programa intercultural?", "2*100//40", "Se divide las horas del programa por las horas totales y se multiplica por 100.", "%"),
        ("=", "{F} ¿Cuántos puntos porcentuales aumentó la asistencia con el programa?", "92-88", "Se resta la asistencia anterior a la nueva."),
        ("=", "{F} Si el programa durara 3 horas en vez de 2, ¿cuántas horas de otras asignaturas quedarían de las 40?", "40-3", "Se resta el tiempo del programa al total."),
        ("{F} ¿Qué dato responde a la objeción del vecino? A) el dato 2, porque muestra que el programa ocupa solo 2 de 40 horas, B) el dato 1, porque cuenta estudiantes.", "A", "Permite calcular el tiempo real que ocupa."),
        ("{F} ¿Prueba el dato 3 que el programa causa la mejora de asistencia? A) no, porque es un estudio pequeño y pueden influir otros factores, B) sí, siempre.", "A", "Una coincidencia no prueba la causa."),
        ("=", "{F} Si los 40 estudiantes del dato 1 formaran 4 grupos iguales para un taller de saberes, ¿cuántos estudiantes habría por grupo?", "40//4", "Se divide el total entre los grupos."),
        ("{F} Una tesis dice: «La diversidad cultural enriquece a la escuela». ¿Qué dato apoya la tesis? A) el dato 1, porque hay estudiantes con lengua indígena en la escuela, B) el dato 4.", "A", "Muestra que la diversidad está presente."),
        ("{F} ¿Cuál es el límite más importante de este dossier? A) que no hay datos sobre notas ni sobre otras escuelas, B) que la escuela es ficticia.", "A", "Falta información para generalizar."),
        ("{F} Un compañero concluye: «El programa mejora la asistencia en todo el país». ¿Qué respuesta es mejor? A) solo se puede afirmar que, en esta escuela de ejemplo, la asistencia fue mayor, B) es correcto.", "A", "La conclusión debe ser proporcional."),
        ("{F} Elige un enunciado que valore la diversidad sin caricaturizar. A) respetar las lenguas de cada pueblo enriquece la convivencia, B) las culturas indígenas deben desaparecer.", "A", "Reconoce el valor de la diversidad."),
    ],
    ctx=("Un centro de estudiantes de ejemplo debate si dedicar 1 de 38 horas de clases semanales a conocer lenguas y saberes de pueblos indígenas. ¿Qué información ayuda a responder a quienes dicen que quita tiempo? A) calcular el porcentaje del tiempo total, B) preguntar a cada estudiante qué asignatura prefiere.", "A", "Muestra la proporción real."),
    sc=[("En Historia: ¿por qué se dice que la diversidad cultural es un valor?", "Porque aporta lenguas, conocimientos y formas de vida y mejora la convivencia", "Enriquece a la sociedad."),
        ("En Historia: ¿Qué es una objeción?", "Una razón que va en contra de una tesis", "Hay que reconocerla y responderla."),
        ("¿Qué es un límite en un argumento?", "Lo que los datos no permiten afirmar", "Así se evita exagerar los resultados.")],
    op=("{F} Escribe un argumento de cinco a siete líneas sobre el valor de la diversidad cultural en la escuela del dossier. Incluye una tesis, dos datos, una objeción con su respuesta y un límite. No tienes que hablar de tu propia familia.",
        "Tesis: la diversidad cultural enriquece a la escuela. Datos: 40 de 120 estudiantes hablan una lengua indígena y el programa ocupa solo 2 de 40 horas. Objeción: quita tiempo a otras asignaturas; se responde con que ocupa 5 % del tiempo. Límite: falta información sobre notas.",
        ["declara una tesis", "usa dos datos", "responde una objeción", "indica un límite"], ["un argumento de cinco a siete líneas"], ["afirmar un efecto general sin datos", "no incluir objeción"], "Léele tu argumento a una persona de tu casa y pídele que diga si respeta a todas las posturas."),
    reinforce="Escribe una razón por la que conocer otras culturas mejora la convivencia.",
    extend="Explica cómo cambiaría tu argumento si el programa ocupara 10 horas de las 40.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = ("Propuestas de ejemplo para mejorar la convivencia entre los pueblos indígenas y el resto de la sociedad. "
      "Propuesta 1: ampliar la educación intercultural bilingüe en 25 escuelas, con un costo de ejemplo de 12 millones de pesos por escuela. "
      "Propuesta 2: consultar a las comunidades antes de proyectos que afecten sus territorios, con información clara y a tiempo. "
      "Propuesta 3: incluir saberes de pueblos indígenas en todos los colegios del país. "
      "Límites de las fuentes: un testimonio no habla por todo un pueblo; los datos del dossier son de ejemplo; ningún estudiante debe representar a un pueblo.")
build(
    OA, 6, F6,
    use="Aprenderé a evaluar propuestas para mejorar la convivencia, a proyectar sus efectos y a reconocer los límites de las fuentes. Sirve para cerrar el estudio de conflicto y convivencia con una mirada crítica y respetuosa.",
    prior=["Conozco conflicto y convivencia en las relaciones con los pueblos indígenas.", "Sé armar un argumento con tesis, evidencia, objeción y límite.", "Sé calcular multiplicaciones de dinero."],
    explain=[
        "Evaluar una propuesta significa preguntar qué problema busca resolver, a quiénes beneficia, cuánto cuesta, qué efectos puede tener y qué riesgos tiene. Proyectar es imaginar, con base en datos, cómo podría cambiar una situación en el futuro si se aplica una medida. Una proyección no es una predicción segura: depende de supuestos, es decir, de condiciones que se dan por ciertas.",
        "Para proponer medidas sobre pueblos indígenas es clave incluir su voz. Una propuesta hecha solo desde fuera, sin consultar, tiene más riesgo de no funcionar. También hay límites de las fuentes: los testimonios y los datos disponibles son parciales, y nadie puede hablar en nombre de un pueblo completo. Por eso las conclusiones deben ser prudentes y decir qué voces y datos faltan.",
        "Una evaluación equilibrada compara costos y beneficios, reconoce los intereses de distintos actores y evita caricaturas. Al terminar, se puede decir qué medida parece más prometedora con la evidencia disponible, qué dudas quedan y qué nueva información se necesitaría para decidir mejor.",
    ],
    vocab=[("proyectar", "imaginar con base en datos cómo podría cambiar una situación en el futuro"), ("supuesto", "condición que se da por cierta para hacer un cálculo o una proyección"), ("prudente", "que no afirma más de lo que la evidencia permite"), ("beneficio", "ventaja que se espera obtener de una medida"), ("costo", "recursos que hay que gastar para aplicar una medida")],
    worked=[
        ("Calcular el costo de una medida", "Una medida de ejemplo cuesta 8 millones por escuela y se aplicaría en 10 escuelas. ¿Cuánto costaría en total?",
         ["Multiplico el costo por el número de escuelas.", "8 × 10 = 80."], "80 millones de pesos"),
        ("Reconocer un supuesto", "Una proyección de ejemplo dice: «Si se aplica el programa, mejorará la convivencia». ¿Qué se está dando por cierto?",
         ["Se supone que el programa funciona como se espera.", "Ese es el supuesto de la proyección."], "Que el programa funcionará como se espera"),
    ],
    mistakes=[
        ("Tratar una proyección como una predicción segura.", "Depende de supuestos que pueden no cumplirse.", "Indica los supuestos y los riesgos."),
        ("Proponer medidas sin incluir la voz de los pueblos.", "Aumenta el riesgo de que la medida no responda a lo que necesitan.", "Incluye una instancia de consulta."),
    ],
    T=[
        ("En Historia: ¿qué es proyectar?", "Imaginar con base en datos cómo podría cambiar una situación en el futuro", "No es una predicción segura."),
        ("{F} ¿Cuántas escuelas incluye la propuesta 1?", "25", "El texto lo informa."),
        ("{F} ¿Qué propuesta se centra en preguntar a las comunidades antes de decidir? A) la propuesta 2, B) la propuesta 3.", "A", "Habla de consultar."),
        ("=", "{F} ¿Cuánto costaría la propuesta 1 en total (en millones de pesos)?", "25*12", "Se multiplica el costo por escuela por 25."),
        ("=", "{F} Si la propuesta 1 se aplicara solo en 12 escuelas, ¿cuánto costaría (en millones)?", "12*12", "Se multiplica el costo por escuela por 12."),
        ("=", "{F} Si el costo por escuela subiera de 12 a 15 millones, ¿cuánto costarían las 25 escuelas (en millones)?", "25*15", "Se multiplica el nuevo costo por 25."),
        ("{F} ¿Qué supuesto tiene la propuesta 1? A) que la educación intercultural mejora la convivencia, B) que cuesta 12 millones.", "A", "Es lo que se da por cierto."),
        ("{F} ¿Qué límite señala el dossier sobre los testimonios? A) que un testimonio no habla por todo un pueblo, B) que los testimonios son falsos.", "A", "El dossier lo dice."),
        ("{F} ¿Qué riesgo tiene la propuesta 3 si se aplica sin consultar a los pueblos? A) que no refleje bien sus saberes, B) que el costo sea de 12 millones por escuela.", "A", "No incluye su voz."),
        ("{F} ¿Qué dato necesitarías para comparar la propuesta 1 y la 3? A) el costo y los beneficios de cada una, B) cuántos pueblos aparecen en el mapa.", "A", "Permite comparar ambas propuestas."),
        ("{F} Un compañero afirma: «La propuesta 2 resolverá todos los conflictos». ¿Qué respuesta es mejor? A) puede mejorar las decisiones, pero no garantiza acuerdos totales, B) es correcto.", "A", "La consulta escucha, pero no asegura consenso."),
        ("{F} ¿Qué conclusión es más prudente? A) la propuesta 2 parece útil, pero faltan datos y voces para decidir, B) hay que aplicar las tres sin evaluar.", "A", "Reconoce los límites de la evidencia."),
        ("{F} Un estudiante de un curso de ejemplo dice: «Yo represento a todo un pueblo indígena en este debate». ¿Qué le responderías? A) nadie puede hablar por todo un pueblo; se pueden estudiar las fuentes, B) tiene razón.", "A", "Se respeta la diversidad interna."),
    ],
    ctx=("Un municipio de ejemplo tiene 60 millones de pesos y debe elegir entre aplicar la propuesta 1 en 5 escuelas (12 millones cada una) o hacer 3 consultas a comunidades (cada una cuesta 15 millones). ¿Cuánto costaría cada opción? A) la primera 60 millones y la segunda 45 millones, B) la primera 45 millones y la segunda 60 millones.", "A", "5 por 12 son 60 y 3 por 15 son 45."),
    sc=[("En Historia: ¿qué es un supuesto?", "Una condición que se da por cierta para hacer una proyección", "Si falla, cambia el resultado."),
        ("¿Por qué una conclusión debe ser prudente?", "Porque debe afirmar solo lo que la evidencia permite", "Las fuentes son parciales."),
        ("¿Por qué incluir la voz de los pueblos en una propuesta?", "Porque la medida los afecta y así responde mejor a sus necesidades", "Mejora la calidad de la decisión.")],
    op=("{F} Elige una propuesta y escribe una evaluación de cinco a siete líneas que incluya: el problema que busca resolver, su costo (con una cifra del dossier), un beneficio posible, un supuesto y un límite de las fuentes. No tienes que hablar de ninguna persona real.",
        "Propuesta 1: busca mejorar la educación intercultural. Cuesta 25 × 12 = 300 millones. Beneficio: más estudiantes con su lengua enseñada. Supuesto: que la medida mejora la convivencia. Límite: los datos son de ejemplo y faltan testimonios de otros pueblos.",
        ["nombra el problema", "calcula el costo", "indica un supuesto", "señala un límite"], ["una evaluación de cinco a siete líneas"], ["afirmar que resolverá todo", "no mencionar ningún límite"], "Pide a una persona de tu casa que identifique cuál es tu supuesto."),
    reinforce="Escribe tres supuestos que tendría una medida para mejorar la convivencia en tu curso.",
    extend="Explica por qué una buena propuesta incluye una forma de evaluar si funcionó.",
    materials=MAT,
)
