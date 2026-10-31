"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 04 (aspectos culturales del siglo XIX)."""
from __future__ import annotations

from hi5_lib import build

OA4 = "HI06 OA 04"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 15 (cronología cultural del siglo XIX, hecha para este cuaderno). "
     "1813: se funda el Instituto Nacional en Santiago. "
     "1822: la escritora inglesa María Graham visita Chile y escribe un diario sobre lo que ve. "
     "1830: el naturalista francés Claudio Gay comienza a estudiar la naturaleza de Chile; su obra «Historia física y política de Chile» se publica entre 1844 y 1871. "
     "1834-1835: el científico inglés Charles Darwin visita Chile. "
     "1842: se crean la Universidad de Chile, con Andrés Bello como primer rector, y la Escuela Normal de Preceptores, para formar profesores. "
     "1851: se inaugura el primer ferrocarril de Chile, entre Caldera y Copiapó. "
     "1860: la ley de instrucción primaria establece escuelas gratuitas. "
     "1863: se inaugura el ferrocarril entre Santiago y Valparaíso. "
     "1877: el Decreto Amunátegui permite que las mujeres ingresen a la universidad. "
     "1887: Eloísa Díaz y Ernestina Pérez se titulan de médicas.")
build(
    OA4, 1, F,
    use="Aprenderé a ubicar en el tiempo los avances culturales de Chile en el siglo XIX. Sirve para investigar con orden y no confundir fechas ni personas.",
    prior=["Sé que Chile se organizó como república en el siglo XIX.", "Sé leer una línea de tiempo y restar años.", "Sé que una fuente sirve para investigar."],
    explain=[
        "En el siglo XIX, Chile vivió cambios culturales importantes. La cultura incluye la educación, la ciencia, el arte y las costumbres de una sociedad. Para investigar, primero conviene ubicar los hechos en una línea de tiempo y preguntarse por quién, cuándo y dónde ocurrieron.",
        "La educación avanzó con la fundación del Instituto Nacional en 1813, de la Universidad de Chile y la Escuela Normal de Preceptores en 1842, y con la ley de 1860 que estableció escuelas primarias gratuitas. Intelectuales nacionales y extranjeros aportaron conocimientos: Andrés Bello, Claudio Gay, Charles Darwin y María Graham, entre otros.",
        "También hubo avances tecnológicos y sociales. En 1851 se inauguró el primer ferrocarril y en 1863 el que une Santiago con Valparaíso. En 1877 se permitió que las mujeres entraran a la universidad, y en 1887 las primeras se titularon de médicas. Todos estos hechos se pueden ordenar y comparar para ver cómo cambió la sociedad.",
    ],
    vocab=[("cultura", "conjunto de conocimientos, costumbres y creaciones de una sociedad"), ("intelectual", "persona que se dedica a estudiar, escribir y pensar"), ("naturalista", "científico que estudia la naturaleza"), ("ferrocarril", "tren que circula sobre rieles"), ("titularse", "recibir el título que permite ejercer una profesión")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre la fundación del Instituto Nacional y la de la Universidad de Chile?", ["Busco los años: 1813 y 1842.", "Resto: 1842 − 1813 = 29."], "29 años"),
        ("Ubicar un hecho en el tiempo", "{F} ¿Qué ocurrió primero: la visita de Darwin o el primer ferrocarril?", ["Darwin visitó Chile en 1834-1835.", "El primer ferrocarril es de 1851."], "La visita de Darwin"),
    ],
    mistakes=[("Creer que todo el avance cultural ocurrió al mismo tiempo.", "Se mira el siglo como un bloque.", "Los hechos ocurrieron en distintos años, de 1813 a 1887."),
              ("Mezclar a las personas con sus obras.", "Se recuerdan los nombres, pero no lo que hizo cada persona.", "Bello fue rector; Gay estudió la naturaleza; Darwin visitó Chile; Graham escribió un diario.")],
    T=[
        ("{F} ¿Qué ciudad une el ferrocarril inaugurado en 1863 con Santiago?", "Valparaíso", "La ficha lo indica."),
        ("{F} ¿Quién fue el primer rector de la Universidad de Chile?", "Andrés Bello", "La ficha lo dice."),
        ("{F} ¿Qué decreto de 1877 permitió a las mujeres ingresar a la universidad?", "el Decreto Amunátegui", "La ficha lo nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre el Decreto Amunátegui y el título de las primeras médicas?", "1887-1877", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué escritora inglesa visitó Chile en 1822?", "María Graham", "La ficha lo indica."),
        ("{F} ¿Entre qué ciudades se inauguró el primer ferrocarril de Chile en 1851?", "Caldera y Copiapó", "La ficha lo dice."),
        ("{F} Ordena de más antiguo a más reciente: Decreto Amunátegui, Instituto Nacional, ferrocarril Santiago-Valparaíso, Universidad de Chile.", "Instituto Nacional, Universidad de Chile, ferrocarril Santiago-Valparaíso, Decreto Amunátegui", "Los años son 1813, 1842, 1863 y 1877."),
        ("=", "{F} ¿Cuántos años pasaron entre la primera visita de María Graham y la de Darwin (considera el año 1834)?", "1834-1822", "Se restan los años.", " años"),
        ("{F} Clasifica cada hecho como «educación» o «transporte»: a) Escuela Normal; b) ferrocarril de 1851; c) ley de 1860; d) ferrocarril de 1863.", "educación: a y c; transporte: b y d", "Cada hecho pertenece a un ámbito."),
        ("{F} Un compañero dice: «Darwin fundó la Universidad de Chile». Corrígelo.", "No: Darwin visitó Chile; Andrés Bello fue el primer rector de la Universidad de Chile", "Son personas y hechos distintos."),
        ("{F} Una alumna dice: «Las primeras médicas se titularon antes del Decreto Amunátegui». ¿Por qué se equivoca?", "porque se titularon en 1887, diez años después de 1877", "1887 es posterior a 1877."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1810. ¿A cuántos cm de distancia queda el año 1860?", "5 cm", "(1860 − 1810) ÷ 10 = 5."),
        ("{F} ¿Cuántos hechos de la ficha son anteriores a 1840?", "cuatro", "Instituto Nacional, visita de María Graham, estudios de Claudio Gay en 1830 y visita de Darwin."),
    ],
    ctx=("Un museo prepara una línea de tiempo del siglo XIX y quiere poner juntos los hechos de la década de 1860. ¿Qué dos hechos de la ficha debe incluir?", "la ley de instrucción primaria (1860) y el ferrocarril Santiago-Valparaíso (1863)", "Son los únicos hechos de esa década en la ficha."),
    sc=[("¿Qué incluye la cultura de una sociedad?", "conocimientos, costumbres y creaciones", "La definición de la clase."),
        ("{F} ¿En qué año se fundó el Instituto Nacional?", "1813", "La ficha lo dice."),
        ("¿Para qué sirve ubicar los hechos en una línea de tiempo antes de investigar?", "para ordenar los hechos y no confundir fechas ni personas", "El orden ayuda a investigar.")],
    op=("Dibuja una línea de tiempo desde 1810 hasta 1890. Marca al menos diez hechos de la ficha con su año. Usa un color para los hechos de educación y otro para los de transporte o tecnología. {F}",
        "Puntos en 1813, 1822, 1830, 1834, 1842, 1851, 1860, 1863, 1877 y 1887, con dos colores.",
        ["diez hechos ordenados", "dos colores bien usados", "años correctos"], ["línea de tiempo coloreada"], ["poner el Decreto Amunátegui antes de 1860", "colorear un ferrocarril como educación"],
        "Pide que cuente en voz alta cuántos años hay entre el primer y el último hecho."),
    reinforce="Di en voz alta cinco hechos de la ficha en orden, con su año.",
    extend="Escribe una pregunta sobre qué cambió en la vida diaria de las personas con alguno de los hechos de la ficha.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 16 (fuentes para investigar, inventadas para este cuaderno a partir de hechos conocidos). "
     "Fuente A, fragmento del diario de María Graham, 1822 (texto inventado): «Las mujeres de Santiago tienen una vida muy ligada a la casa y a la iglesia. Pocas saben leer». "
     "Fuente B, nota de un periódico de 1863 (texto inventado): «Hoy llegó el primer tren de Valparaíso a Santiago. Los pasajeros viajaron cómodos y rápidos». "
     "Fuente C, libro de historia de 1995 sobre las primeras médicas: explica que Eloísa Díaz y Ernestina Pérez se titularon en 1887 después del Decreto Amunátegui. "
     "Fuente D, fotografía de la época, sin explicación: muestra una escuela con niños y niñas sentados en bancas, un profesor y un pizarrón.")
build(
    OA4, 2, F,
    use="Aprenderé a investigar con distintas fuentes: diarios, periódicos, libros y fotografías. Sirve para saber qué puede decir cada una y qué no.",
    prior=["Sé qué es una fuente primaria y una secundaria.", "Sé ubicar los hechos culturales del siglo XIX en el tiempo.", "Sé que cada fuente tiene un punto de vista."],
    explain=[
        "Investigar es buscar respuestas a una pregunta usando fuentes. Una buena investigación empieza con una pregunta clara, por ejemplo: ¿cómo cambió la educación en el siglo XIX? Luego se buscan fuentes de distintos tipos y se analiza quién las produjo, cuándo y para qué.",
        "El diario de María Graham es una fuente primaria porque fue escrito en 1822 por una persona que visitó Chile, pero es una mirada de una extranjera. La nota de periódico de 1863 también es primaria y sirve para saber cómo se contó un hecho nuevo. La fotografía muestra una escuela, pero no dice dónde ni cuándo fue tomada; por eso hay que usarla con cuidado.",
        "El libro de 1995 es una fuente secundaria: explica un hecho, pero no lo vivió. Sirve para ordenar la información, siempre que se sepa qué fuentes usó. Cuando se juntan varias fuentes, se pueden confirmar datos y descubrir límites. Por ejemplo, ninguna de estas fuentes entrega la voz de las niñas que asistían a esa escuela.",
    ],
    vocab=[("investigar", "buscar respuestas a una pregunta usando fuentes"), ("fotografía", "imagen tomada con una cámara en un momento determinado"), ("periódico", "publicación que cuenta noticias del momento"), ("fragmento", "parte de un texto más largo"), ("confirmar", "comprobar un dato con otra fuente")],
    worked=[
        ("Clasificar una fuente", "{F} ¿La fuente B es primaria o secundaria?", ["Es una nota de 1863 sobre un hecho de 1863.", "Se creó en la época del hecho."], "Primaria"),
        ("Reconocer un límite", "{F} ¿Qué no dice la fuente D?", ["Solo muestra una escuela con niños, un profesor y un pizarrón.", "No indica dónde ni cuándo fue tomada."], "Dónde y cuándo fue tomada"),
    ],
    mistakes=[("Usar una fotografía como prueba sin saber cuándo se tomó.", "Se olvida preguntar por la procedencia.", "Hay que averiguar dónde, cuándo y quién la tomó antes de usarla."),
              ("Creer que el diario de una viajera cuenta toda la vida de la sociedad.", "Se generaliza desde una mirada.", "Es el punto de vista de una persona extranjera.")],
    T=[
        ("{F} ¿Quién escribió la fuente A?", "María Graham", "La ficha lo indica."),
        ("{F} ¿En qué año se escribió la fuente C?", "1995", "La ficha da ese año."),
        ("{F} ¿Qué hecho cuenta la fuente B?", "la llegada del primer tren de Valparaíso a Santiago", "La nota lo dice."),
        ("{F} ¿Qué fuentes de la ficha son primarias?", "A, B y D", "Se crearon en la época del siglo XIX."),
        ("{F} ¿Por qué la fuente C es secundaria?", "porque se escribió en 1995, mucho después de los hechos", "Su año es posterior."),
        ("=", "{F} ¿Cuántos años pasaron entre la fuente A y la fuente B?", "1863-1822", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué dato de la fuente A habla de la educación de las mujeres?", "que pocas saben leer", "Lo dice el texto."),
        ("{F} Una alumna dice: «La fuente D prueba que todas las escuelas tenían niñas y niños juntos». ¿Qué error comete?", "generaliza desde una sola fotografía", "Una imagen no muestra todas las escuelas."),
        ("{F} Para saber si se mantuvo la educación de las niñas después de 1877, ¿qué fuente de la ficha es más útil?", "la fuente C, porque habla de las primeras médicas después del Decreto Amunátegui", "Es la única que trata de ese período."),
        ("{F} Un compañero dice: «La fuente A es mala porque la escribió una extranjera». ¿Qué respuesta le darías?", "es una fuente con una mirada particular que debe compararse con otras, no una fuente mala", "La procedencia explica el punto de vista."),
        ("{F} ¿Qué pregunta investigaría mejor con las fuentes A y C: A) ¿Cómo cambió la educación de las mujeres? B) ¿Cuántos trenes había en 1863?", "A", "Ambas hablan de educación de mujeres."),
        ("{F} ¿Qué fuente de la ficha cuenta una noticia de la época y qué ventajas del viaje destaca?", "la B, que destaca la comodidad y la rapidez", "Dice que los pasajeros viajaron cómodos y rápidos."),
        ("{F} ¿Qué información puedes confirmar usando juntas las fuentes A y C sobre las mujeres?", "que en 1822 pocas sabían leer y que en 1887 ya había mujeres tituladas", "Muestra un cambio entre dos fechas."),
    ],
    ctx=("Tu curso investiga cómo cambió la vida de las mujeres durante el siglo XIX. Tienes las fuentes A y C. ¿Qué cambio puedes señalar con ellas y qué fuente más buscarías?", "pasó de pocas mujeres que sabían leer en 1822 a mujeres tituladas en 1887; buscaría una fuente escrita por mujeres de esa época", "Las fuentes A y C muestran un cambio."),
    sc=[("¿Qué es investigar?", "buscar respuestas a una pregunta usando fuentes", "Es la definición de la clase."),
        ("{F} ¿La fuente D dice en qué año fue tomada?", "no", "La ficha dice que no tiene explicación."),
        ("¿Para qué sirve combinar fuentes distintas?", "para confirmar datos y descubrir límites", "Cada fuente aporta algo.")],
    op=("Escribe una ficha de investigación con esta pregunta: «¿Cómo cambió la educación en el siglo XIX?». Anota qué dato te da cada fuente de la ficha, si es primaria o secundaria, y qué límite tiene. Termina con una respuesta de dos oraciones. {F}",
        "A: pocas mujeres sabían leer en 1822 (primaria; mirada extranjera). C: primeras médicas en 1887 (secundaria). D: escuela con niños (primaria; sin fecha). Respuesta: la educación se amplió a lo largo del siglo.",
        ["cuatro fuentes analizadas", "tipo de fuente correcto", "límites razonables", "respuesta de dos oraciones"], ["ficha de investigación", "respuesta final"], ["usar la fuente D como si tuviera fecha", "no incluir ningún límite"],
        "Pide que explique qué fuente le fue más útil y por qué."),
    reinforce="Di en voz alta las tres preguntas que haces a una fuente: quién la hizo, cuándo y para qué.",
    extend="Escribe una pregunta de investigación sobre la vida diaria en una ciudad del siglo XIX que se pueda responder con cartas o fotografías.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 17 (el ferrocarril y otros avances, hecha para este cuaderno). "
     "Antes del ferrocarril, las mercancías y las personas viajaban en carretas, mulas o caballos y el viaje entre ciudades podía tomar más de un día. "
     "Con el ferrocarril, el viaje entre Santiago y Valparaíso pasó a tomar unas pocas horas. "
     "El telégrafo (1852) permitió enviar mensajes escritos a otras ciudades en minutos. "
     "Efectos que se conocen: el comercio y la minería movieron más productos; las noticias llegaron más rápido; los pueblos con estación crecieron; algunos arrieros (personas que transportaban carga con mulas) perdieron trabajo; los viajes dejaron de ser tan largos y peligrosos.")
build(
    OA4, 3, F,
    use="Aprenderé a explicar el impacto del ferrocarril y otros avances tecnológicos en la sociedad del siglo XIX. Sirve para distinguir causas, consecuencias y quiénes ganaron o perdieron.",
    prior=["Sé ubicar los avances en el tiempo.", "Sé distinguir causa y consecuencia.", "Sé que un mismo cambio afecta distinto a cada grupo."],
    explain=[
        "Una innovación tecnológica es un invento o mejora que cambia la manera de hacer algo. El ferrocarril fue una de las más importantes del siglo XIX. Antes, mover mercancías y personas era lento y caro. Con el tren, el tiempo de viaje se redujo y se pudo transportar más carga.",
        "El telégrafo también acortó las distancias, porque permitió enviar mensajes en minutos. Estas innovaciones tuvieron consecuencias. El comercio y la minería crecieron, las noticias circularon más rápido y los pueblos con estación se desarrollaron. Una consecuencia es lo que ocurre después de un hecho, y puede ser positiva o negativa.",
        "No todos ganaron. Los arrieros, que transportaban carga con mulas, perdieron trabajo cuando el tren se hizo más usado. Al estudiar un cambio hay que preguntar siempre quién se benefició y quién se perjudicó. Así se evita pensar que el progreso favoreció a todos por igual.",
    ],
    vocab=[("innovación", "invento o mejora que cambia la manera de hacer algo"), ("telégrafo", "aparato que enviaba mensajes escritos a distancia usando señales eléctricas"), ("arriero", "persona que transportaba carga con mulas"), ("mercancía", "producto que se compra y se vende"), ("beneficiar", "ayudar o favorecer a alguien")],
    worked=[
        ("Reconocer una consecuencia", "{F} ¿Cuál fue una consecuencia del ferrocarril para el comercio?", ["Leo los efectos de la ficha.", "El comercio movió más productos."], "El comercio movió más productos"),
        ("Ver quién se perjudicó", "{F} ¿Qué grupo perdió trabajo con el ferrocarril?", ["Busco los grupos afectados negativamente.", "La ficha menciona a los arrieros."], "Algunos arrieros"),
    ],
    mistakes=[("Pensar que el ferrocarril benefició a todos por igual.", "Se miran solo los efectos positivos.", "Algunos arrieros perdieron trabajo; hay ganadores y perdedores."),
              ("Confundir el telégrafo con el teléfono.", "Se mezclan los inventos.", "El telégrafo enviaba mensajes escritos con señales; el teléfono transmite la voz y llegó después.")],
    T=[
        ("{F} ¿En qué año se instaló el telégrafo según la ficha?", "1852", "La ficha lo indica."),
        ("{F} ¿Cómo viajaban las mercancías antes del ferrocarril?", "en carretas, mulas o caballos", "La ficha lo dice."),
        ("{F} ¿Cuánto pasó a tomar el viaje entre Santiago y Valparaíso con el tren?", "unas pocas horas", "La ficha lo indica."),
        ("{F} ¿Qué enviaba el telégrafo?", "mensajes escritos", "La ficha lo dice."),
        ("{F} Clasifica como «ganó» o «perdió» con el ferrocarril: a) comercio; b) arrieros; c) pueblos con estación.", "ganó: a y c; perdió: b", "La ficha describe esos efectos."),
        ("=", "{F} ¿Cuántos años pasaron entre el telégrafo (1852) y el tren Santiago-Valparaíso (1863)?", "1863-1852", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué relación hay entre las estaciones del ferrocarril y el crecimiento de los pueblos?", "los pueblos con estación crecieron", "La ficha lo indica."),
        ("{F} Una persona de 1850 quería avisar algo a otra ciudad. ¿Qué invento de la ficha le servía mejor años después?", "el telégrafo, porque enviaba mensajes en minutos", "El telégrafo acortó el tiempo de aviso."),
        ("{F} Un compañero dice: «Los arrieros se beneficiaron con el tren». Corrígelo.", "No: algunos perdieron trabajo", "La ficha lo dice."),
        ("{F} Una alumna dice: «El telégrafo transportaba mercancías». ¿Qué error comete?", "el telégrafo enviaba mensajes, no mercancías", "Su función era comunicar."),
        ("{F} Elige la mejor razón para decir que el ferrocarril cambió la sociedad: A) tenía rieles de hierro; B) acortó el tiempo de viaje y permitió mover más productos.", "B", "Las consecuencias explican el cambio."),
        ("{F} ¿Qué dos efectos del ferrocarril fueron positivos para las noticias y el comercio?", "las noticias llegaron más rápido y el comercio movió más productos", "La ficha los menciona."),
        ("{F} Un panadero de un pueblo con estación vende más pan porque llegan más viajeros. ¿Qué efecto de la ficha ilustra su caso?", "que los pueblos con estación crecieron", "Más viajeros dinamizan la economía local."),
    ],
    ctx=("Un periodista de 1863 escribe: «El tren trae solo ventajas para todos». ¿Qué dato de la ficha usarías para corregirlo?", "que algunos arrieros perdieron trabajo", "Muestra un grupo perjudicado."),
    sc=[("¿Qué es una innovación tecnológica?", "un invento o mejora que cambia la manera de hacer algo", "La definición de la clase."),
        ("{F} ¿Qué efecto tuvo el ferrocarril en las noticias?", "llegaron más rápido", "La ficha lo dice."),
        ("¿Qué pregunta ayuda a no pensar que el progreso favoreció a todos por igual?", "quién se benefició y quién se perjudicó", "Permite ver ganadores y perdedores.")],
    op=("Dibuja una tabla con dos columnas, «ganaron» y «perdieron», y completa con grupos de la ficha. Después escribe un párrafo de tres oraciones que explique por qué el ferrocarril cambió la vida en el siglo XIX. {F}",
        "Ganaron: comercio, pueblos con estación, quienes querían noticias. Perdieron: algunos arrieros. El ferrocarril acortó el tiempo de viaje y permitió mover más productos.",
        ["al menos dos grupos en cada columna o uno en cada una con explicación", "párrafo de tres oraciones", "dato de la ficha usado"], ["tabla de ganadores y perdedores", "párrafo"], ["decir que todos ganaron", "no mencionar ningún dato"],
        "Pide que explique con un ejemplo por qué una innovación no beneficia a todos."),
    reinforce="Cuenta a alguien de tu casa dos cambios que trajo el ferrocarril en el siglo XIX.",
    extend="Escribe una pregunta sobre cómo cambió la vida de un pueblo con una nueva estación de tren.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 18 (aportes de intelectuales, hecha para este cuaderno). "
     "Andrés Bello, nacido en Venezuela, vivió en Chile desde 1829; fue el primer rector de la Universidad de Chile y escribió un código de leyes civiles y una gramática de la lengua española. "
     "Claudio Gay, nacido en Francia, estudió plantas, animales y territorios de Chile y publicó una obra de varios tomos sobre el país. "
     "Charles Darwin, nacido en Inglaterra, visitó Chile en 1834-1835 y observó la naturaleza y un terremoto en el sur. "
     "María Graham, nacida en Inglaterra, escribió un diario sobre su estadía en Chile en 1822. "
     "Diego Barros Arana, nacido en Chile, fue historiador y rector del Instituto Nacional y escribió una historia general de Chile. "
     "Benjamín Vicuña Mackenna, nacido en Chile, fue historiador y gobernó la ciudad de Santiago, donde impulsó mejoras urbanas. "
     "José Victorino Lastarria, nacido en Chile, fue escritor y político que promovió la libertad de pensamiento.")
build(
    OA4, 4, F,
    use="Aprenderé a comparar los aportes de intelectuales nacionales y extranjeros en el siglo XIX. Sirve para explicar cómo contribuyó cada uno a la cultura de Chile.",
    prior=["Sé ubicar los hechos culturales en el tiempo.", "Sé comparar con un criterio.", "Sé distinguir quién escribe y desde dónde."],
    explain=[
        "Un intelectual es una persona que estudia, escribe y piensa sobre asuntos importantes. En el siglo XIX, intelectuales nacidos en Chile y extranjeros contribuyeron a la cultura del país. Comparar sus aportes significa ver qué hizo cada uno y en qué se diferencian.",
        "Entre los extranjeros, Andrés Bello fue rector y redactó leyes y una gramática; Claudio Gay estudió la naturaleza y publicó una obra sobre Chile; Charles Darwin observó la naturaleza y un terremoto; María Graham dejó un diario con su mirada sobre la sociedad. Entre los nacidos en Chile, Barros Arana y Vicuña Mackenna escribieron historia, y Lastarria impulsó la libertad de pensamiento.",
        "Podemos comparar con criterios: de dónde venían, a qué se dedicaron y qué dejaron. Los extranjeros aportaron miradas externas y estudios de la naturaleza; los chilenos aportaron historia, política y debate. Todos dejaron fuentes que hoy usamos para conocer el pasado, aunque cada uno tenía su propia mirada.",
    ],
    vocab=[("intelectual", "persona que estudia, escribe y piensa sobre asuntos importantes"), ("aporte", "contribución que ayuda a otros"), ("rector", "persona que dirige una universidad"), ("historiador", "persona que estudia y cuenta el pasado"), ("gramática", "libro que explica las reglas de una lengua")],
    worked=[
        ("Reconocer un aporte", "{F} ¿Qué aporte hizo Claudio Gay?", ["Reviso su entrada en la ficha.", "Estudió plantas, animales y territorios de Chile y publicó una obra de varios tomos."], "Estudió la naturaleza de Chile y publicó una obra sobre el país"),
        ("Comparar dos personas", "{F} ¿Qué tienen en común Barros Arana y Vicuña Mackenna?", ["Ambos nacieron en Chile.", "Ambos fueron historiadores."], "Nacieron en Chile y fueron historiadores"),
    ],
    mistakes=[("Atribuir la obra de una persona a otra.", "Se confunden los nombres.", "Bello redactó leyes y una gramática; Gay publicó una obra sobre la naturaleza; Barros Arana escribió historia."),
              ("Creer que solo aportaron los hombres.", "Se recuerdan solo algunos nombres.", "María Graham, una mujer, dejó un diario importante.")],
    T=[
        ("{F} ¿En qué país nació Claudio Gay?", "Francia", "La ficha lo indica."),
        ("{F} ¿Qué escribió María Graham?", "un diario sobre su estadía en Chile", "La ficha lo dice."),
        ("{F} ¿Quién fue historiador y rector del Instituto Nacional?", "Diego Barros Arana", "La ficha lo indica."),
        ("{F} ¿Qué observó Darwin en el sur de Chile?", "un terremoto", "La ficha lo menciona."),
        ("{F} ¿Qué dos extranjeros de la ficha nacieron en Inglaterra?", "Charles Darwin y María Graham", "La ficha lo indica."),
        ("{F} ¿Qué chileno impulsó mejoras urbanas en Santiago?", "Benjamín Vicuña Mackenna", "La ficha lo dice."),
        ("{F} Clasifica como nacional (N) o extranjero (E): a) Bello; b) Lastarria; c) Gay; d) Barros Arana.", "a: E; b: N; c: E; d: N", "Bello nació en Venezuela y Gay en Francia; los otros en Chile."),
        ("=", "{F} ¿Cuántos años pasaron entre la llegada de Bello a Chile (1829) y la visita de Darwin (1834)?", "1834-1829", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué aporte comparten Gay y Darwin?", "ambos estudiaron la naturaleza", "La ficha dice que los dos se dedicaron a la naturaleza."),
        ("{F} Un compañero dice: «Bello nació en Chile». Corrígelo.", "No: nació en Venezuela y vivió en Chile desde 1829", "La ficha lo indica."),
        ("{F} Una alumna dice: «Solo los hombres aportaron a la cultura». Da un contraejemplo de la ficha.", "María Graham", "Es una mujer con un aporte."),
        ("{F} Compara a Bello y Barros Arana: ¿quién redactó leyes y una gramática?", "Bello", "La ficha lo dice."),
        ("{F} ¿Cuál de estos aportes fue sobre la libertad de pensamiento: el de Gay o el de Lastarria?", "el de Lastarria", "La ficha lo indica."),
    ],
    ctx=("Para una exposición, debes elegir una persona de la ficha que sirva para explicar cómo se estudió la naturaleza de Chile. ¿A quién eliges y por qué?", "Claudio Gay, porque estudió plantas, animales y territorios y publicó una obra sobre Chile", "Es el aporte más directo sobre la naturaleza del país."),
    sc=[("¿Qué es un intelectual?", "una persona que estudia, escribe y piensa sobre asuntos importantes", "Es la definición de la clase."),
        ("{F} ¿Qué escribió Barros Arana?", "una historia general de Chile", "La ficha lo dice."),
        ("¿Por qué los aportes de extranjeros y chilenos son distintos?", "porque tenían miradas y ocupaciones distintas", "Su origen y trabajo diferían.")],
    op=("Dibuja una tabla con cuatro columnas: «persona», «país de nacimiento», «a qué se dedicó» y «aporte». Completa con al menos cinco personas de la ficha, incluyendo a una mujer. Al final, escribe una oración que compare a un nacional con un extranjero. {F}",
        "María Graham, Inglaterra, escritora, diario sobre Chile. Barros Arana, Chile, historiador, historia general de Chile. Oración: Gay estudió la naturaleza de Chile mientras Barros Arana escribió su historia.",
        ["cinco personas con datos correctos", "una mujer incluida", "oración comparativa"], ["tabla de aportes", "oración comparativa"], ["atribuir una obra a otra persona", "no incluir a ninguna mujer"],
        "Pide que explique por qué eligió a esas cinco personas."),
    reinforce="Di en voz alta cuatro nombres de la ficha con el aporte de cada uno.",
    extend="Escribe una pregunta que le harías a María Graham sobre cómo era la vida diaria en Chile en 1822.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 19 (educación en el siglo XIX, hecha para este cuaderno). "
     "Antes de 1860, muchas niñas y niños de familias pobres no iban a la escuela. "
     "En 1842 se creó la Escuela Normal de Preceptores para formar profesores. "
     "En 1860 la ley de instrucción primaria estableció escuelas primarias gratuitas, pero no obligatorias. "
     "En 1877, el Decreto Amunátegui permitió que las mujeres ingresaran a la universidad. "
     "Eloísa Díaz y Ernestina Pérez se titularon de médicas en 1887, después de cursar sus estudios. "
     "Aun así, muchos niños y niñas del campo seguían sin asistir a la escuela porque debían trabajar o vivían lejos.")
build(
    OA4, 5, F,
    use="Aprenderé a argumentar cuál avance de la educación del siglo XIX tuvo más impacto, usando evidencia. Sirve para sostener una opinión con datos y reconocer sus límites.",
    prior=["Sé qué hechos de educación hubo en el siglo XIX.", "Sé qué es un argumento: afirmación, evidencia y razón.", "Sé reconocer objeciones."],
    explain=[
        "En el siglo XIX, la educación fue una prioridad para varios gobiernos. Se formaron profesores en la Escuela Normal de Preceptores en 1842. En 1860, la ley de instrucción primaria estableció escuelas gratuitas. En 1877, el Decreto Amunátegui abrió la universidad a las mujeres.",
        "Para argumentar sobre cuál avance fue más importante, necesitamos criterios: a cuántas personas llegó, qué derechos amplió y qué cambió a largo plazo. Podemos defender, por ejemplo, que la ley de 1860 llegó a más niños porque la escuela gratuita no dependía del dinero de la familia. O que el Decreto Amunátegui fue clave para la igualdad entre hombres y mujeres.",
        "Un argumento sólido incluye evidencia y reconoce límites. La ley de 1860 no obligaba a asistir, y muchas familias del campo seguían sin enviar a sus hijos. El Decreto de 1877 beneficiaba a pocas mujeres, pero abrió una puerta que sirvió a muchas después. Reconocer estos límites hace más honesta la conclusión.",
    ],
    vocab=[("gratuito", "que no cuesta dinero"), ("obligatorio", "que todos deben cumplir"), ("preceptor", "profesor de escuela primaria en el siglo XIX"), ("igualdad", "que todas las personas tengan los mismos derechos"), ("criterio", "aspecto que se usa para juzgar o comparar")],
    worked=[
        ("Armar un argumento", "{F} Defiende que la ley de 1860 fue un avance importante.", ["Afirmación: la ley de 1860 fue un avance importante.", "Evidencia: estableció escuelas primarias gratuitas, así más niños pudieron estudiar."], "La ley de 1860 fue importante porque estableció escuelas gratuitas"),
        ("Reconocer un límite", "{F} ¿Qué límite tuvo la ley de 1860?", ["Busco qué no hacía la ley.", "No era obligatoria y muchos niños del campo no asistían."], "No era obligatoria"),
    ],
    mistakes=[("Defender un avance sin usar datos.", "Se confunde opinión con argumento.", "Hay que citar un dato de la ficha."),
              ("Creer que la ley de 1860 hizo que todos los niños fueran a la escuela.", "Se ignora el límite de que no era obligatoria.", "La ficha dice que muchos niños seguían sin asistir.")],
    T=[
        ("{F} ¿Qué estableció la ley de 1860?", "escuelas primarias gratuitas", "La ficha lo dice."),
        ("{F} ¿Qué permitió el Decreto Amunátegui?", "que las mujeres ingresaran a la universidad", "La ficha lo indica."),
        ("{F} ¿Para qué se creó la Escuela Normal de Preceptores?", "para formar profesores", "La ficha lo dice."),
        ("{F} ¿Por qué muchos niños del campo no asistían a la escuela?", "porque debían trabajar o vivían lejos", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la Escuela Normal y la ley de instrucción primaria?", "1860-1842", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Cuál es una objeción válida a decir que la ley de 1860 llevó a todos los niños a la escuela?", "que no era obligatoria y muchos niños del campo no asistían", "Es un dato de la ficha."),
        ("{F} ¿Qué avance de la ficha favoreció directamente la igualdad entre hombres y mujeres?", "el Decreto Amunátegui", "Permitió el ingreso de las mujeres a la universidad."),
        ("{F} Elige el argumento con evidencia. A) El Decreto Amunátegui es lo mejor. B) El Decreto fue importante porque permitió que las mujeres entraran a la universidad.", "B", "B tiene afirmación y evidencia."),
        ("=", "{F} ¿Cuántos años pasaron entre el Decreto Amunátegui y el título de Eloísa Díaz y Ernestina Pérez?", "1887-1877", "Se resta el año menor al mayor.", " años"),
        ("{F} Un alumno dice que la ley de 1860 fue inútil porque no era obligatoria. ¿Qué dato de la ficha contradice la idea de que fue inútil?", "que estableció escuelas gratuitas", "Igual amplió el acceso."),
        ("{F} ¿Qué avance sirvió para que existieran más profesores formados?", "la Escuela Normal de Preceptores", "Su función era formar profesores."),
        ("{F} Una compañera dice que el Decreto de 1877 ayudó al principio a pocas mujeres. ¿Qué dato de la ficha da una pista?", "que la ficha nombra solo a dos mujeres tituladas, en 1887, diez años después del decreto", "Son las dos tituladas que menciona la ficha."),
        ("{F} Si tuvieras que elegir entre la ley de 1860 y el Decreto de 1877 por su alcance en más niños, ¿cuál elegirías?", "la ley de 1860, porque estableció escuelas gratuitas para más niños", "Es un avance que llegó a más personas."),
    ],
    ctx=("Para el aniversario de tu colegio, quieres elegir un avance de educación del siglo XIX para el afiche. Escribe tu elección con una razón.", "la ley de 1860, porque estableció escuelas gratuitas", "Sirve una elección con razón basada en la ficha."),
    sc=[("¿Qué tres criterios sirven para juzgar un avance en educación?", "a cuántas personas llegó, qué derechos amplió y qué cambió a largo plazo", "Son los criterios de la clase."),
        ("{F} ¿La ley de 1860 hacía obligatorio asistir a la escuela?", "no", "La ficha dice que no era obligatoria."),
        ("¿Para qué sirve reconocer un límite?", "para que el argumento sea más honesto", "Ayuda a ser preciso.")],
    op=("Escribe un texto de cinco oraciones: 1) elige un avance de la educación de la ficha; 2) explica qué cambió con un dato; 3) di a quién ayudó; 4) escribe un límite; 5) responde a ese límite. {F}",
        "Elijo la ley de 1860. Estableció escuelas gratuitas. Ayudó a niños de familias pobres. Un límite es que no era obligatoria. Aun así, abrió una puerta para más estudiantes.",
        ["avance elegido de la ficha", "dato correcto", "límite y respuesta"], ["texto de cinco oraciones"], ["no usar dato de la ficha", "no incluir límite"],
        "Pide que explique cuál criterio usó: alcance, derechos o largo plazo."),
    reinforce="Di en voz alta un argumento completo sobre un avance de la educación.",
    extend="Escribe una pregunta sobre qué ocurría en las escuelas rurales en 1860.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 20 (una decisión ciudadana, hecha para este cuaderno). "
     "En 1877, el ministro de Justicia e Instrucción Pública, Miguel Luis Amunátegui, firmó un decreto que permitía que las mujeres rindieran exámenes y estudiaran en la universidad. "
     "Antes de ese decreto, las mujeres que querían estudiar en la universidad no podían hacerlo, aunque tuvieran buenas notas. "
     "Después del decreto, en 1887 se titularon las primeras médicas, Eloísa Díaz y Ernestina Pérez. "
     "Algunas personas de la época pensaban que las mujeres debían dedicarse solo a la casa; otras pensaban que merecían los mismos estudios que los hombres. "
     "Aun después del decreto, hubo pocas mujeres en la universidad durante varios años.")
build(
    OA4, 6, F,
    use="Aprenderé a evaluar una decisión pública del pasado usando criterios y evidencia. Sirve para opinar sobre decisiones con razones, no solo con gustos.",
    prior=["Sé qué fue el Decreto Amunátegui.", "Sé argumentar con evidencia.", "Sé distinguir hecho de opinión."],
    explain=[
        "Evaluar una decisión es juzgar si fue buena o mala usando criterios. Una decisión ciudadana es una decisión que afecta a muchas personas, como un decreto del gobierno. Algunos criterios son: ¿amplió derechos?, ¿a quiénes benefició?, ¿tuvo costos o límites?, ¿qué consecuencias dejó a largo plazo?",
        "El Decreto Amunátegui de 1877 permitió que las mujeres estudiaran en la universidad. Amplió derechos y, diez años después, se titularon las primeras médicas. Tuvo un límite: durante varios años hubo pocas mujeres en la universidad, y algunas personas de la época no estaban de acuerdo con el cambio.",
        "Al evaluar, es importante separar los hechos de las opiniones y entender cómo pensaban las personas de ese tiempo, sin dejar de preguntar si la decisión respetaba la igualdad. Una buena evaluación termina con una conclusión razonada: la decisión fue buena porque amplió derechos y produjo profesionales; y tuvo límites porque no cambió todo de inmediato.",
    ],
    vocab=[("evaluar", "juzgar el valor de algo usando criterios"), ("decreto", "orden oficial firmada por una autoridad del gobierno"), ("derecho", "algo que una persona puede hacer o recibir porque es justo y está reconocido"), ("criterio", "aspecto que se usa para juzgar"), ("consecuencia", "resultado de un hecho")],
    worked=[
        ("Aplicar un criterio", "{F} ¿El decreto amplió derechos? Responde con un dato.", ["Antes no podían estudiar en la universidad.", "Después pudieron: en 1887 se titularon las primeras médicas."], "Sí, porque las mujeres pudieron estudiar y titularse"),
        ("Reconocer un límite", "{F} ¿Qué límite se menciona después del decreto?", ["Leo las consecuencias.", "Hubo pocas mujeres en la universidad durante varios años."], "Hubo pocas mujeres en la universidad"),
    ],
    mistakes=[("Juzgar el pasado solo con las ideas de hoy.", "Se ignora cómo pensaban las personas entonces.", "Hay que explicar el contexto y también preguntar por la igualdad."),
              ("Dar una opinión sin criterios.", "Se confunde evaluación con gusto personal.", "Se necesitan criterios y evidencia.")],
    T=[
        ("{F} ¿Quién firmó el decreto de 1877?", "el ministro Miguel Luis Amunátegui", "La ficha lo indica."),
        ("{F} ¿Qué permitió el decreto?", "que las mujeres estudiaran en la universidad", "La ficha lo dice."),
        ("{F} ¿Qué dos mujeres se titularon en 1887?", "Eloísa Díaz y Ernestina Pérez", "La ficha las nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre el decreto y el título de las primeras médicas?", "1887-1877", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué pensaban algunas personas de la época sobre las mujeres?", "que debían dedicarse solo a la casa", "La ficha lo indica."),
        ("{F} ¿Qué pensaban otras personas?", "que merecían los mismos estudios que los hombres", "La ficha lo dice."),
        ("{F} Clasifica como hecho (H) u opinión (O): a) En 1877 se firmó un decreto; b) las mujeres deben dedicarse solo a la casa; c) en 1887 se titularon dos médicas.", "a: H; b: O; c: H", "Los hechos se comprueban; b es una opinión."),
        ("{F} ¿Qué criterio apoya decir que el decreto fue una buena decisión?", "que amplió derechos de las mujeres", "Permitió el estudio universitario."),
        ("{F} ¿Qué dato muestra un límite del decreto?", "que hubo pocas mujeres en la universidad durante varios años", "La ficha lo dice."),
        ("{F} Un alumno dice: «El decreto fue malo porque pocas mujeres entraron». Responde con un dato.", "aunque hubo pocas, en 1887 se titularon las primeras médicas, lo que muestra su efecto", "El límite no anula su efecto."),
        ("{F} Una compañera dice: «En 1877 todos pensaban igual sobre el decreto». ¿Qué dato lo contradice?", "que algunos pensaban que las mujeres debían dedicarse solo a la casa y otros que merecían los mismos estudios", "Había opiniones distintas."),
        ("{F} Elige la mejor conclusión razonada. A) El decreto fue bueno porque amplió derechos, pero tuvo límites. B) El decreto fue bueno porque sí.", "A", "A tiene criterios y evidencia."),
        ("{F} ¿Qué consecuencia a largo plazo se menciona para el decreto?", "que se titularon las primeras médicas", "Es la consecuencia de la ficha."),
    ],
    ctx=("Tu curso debe votar si recuerda el Decreto Amunátegui en un acto escolar. Escribe un argumento breve con un criterio.", "Sí, porque amplió los derechos de las mujeres a estudiar", "Se acepta cualquier argumento con criterio de la ficha."),
    sc=[("¿Qué es evaluar una decisión?", "juzgar su valor usando criterios", "Es la definición de la clase."),
        ("{F} ¿En qué año se firmó el decreto?", "1877", "La ficha lo dice."),
        ("¿Por qué conviene separar hechos de opiniones?", "porque los hechos se pueden comprobar y las opiniones no", "Evita confundir lo que ocurrió con lo que alguien piensa.")],
    op=("Escribe una evaluación del Decreto Amunátegui con esta pauta: 1) dos criterios; 2) un dato de la ficha para cada criterio; 3) un límite; 4) tu conclusión en dos oraciones. {F}",
        "Criterio 1: amplió derechos; dato: las mujeres pudieron estudiar. Criterio 2: consecuencias; dato: en 1887 se titularon médicas. Límite: pocas mujeres entraron. Conclusión: fue una buena decisión con límites.",
        ["dos criterios con dato", "un límite", "conclusión de dos oraciones"], ["texto de evaluación"], ["usar criterios sin dato", "no incluir límite"],
        "Pide que lea su conclusión y diga qué evidencia la apoya."),
    reinforce="Di en voz alta dos criterios para evaluar una decisión pública.",
    extend="Escribe una pregunta sobre cómo se sintió una de las primeras mujeres que estudió en la universidad.",
)
