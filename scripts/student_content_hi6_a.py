"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (antecedentes de la independencia americana y su carácter continental)."""
from __future__ import annotations

from hi5_lib import build

OA1 = "HI06 OA 01"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología, hecha para este cuaderno). 1776: las trece colonias británicas de América del Norte declaran su independencia y nace Estados Unidos. "
     "1789: comienza la Revolución Francesa en Francia. 1804: Haití, colonia francesa en América, se declara independiente. "
     "1808: tropas de Napoleón invaden España y el rey Fernando VII deja el trono. "
     "1810: se forman juntas de gobierno en Caracas (19 de abril), en Buenos Aires (25 de mayo) y en Santiago de Chile (18 de septiembre). "
     "1818: Chile proclama su independencia. 1824: en la batalla de Ayacucho, en Perú, el ejército del rey es derrotado de manera final en Sudamérica.")
build(
    OA1, 1, F,
    use="Aprenderé a ubicar la independencia de Chile dentro de una línea de tiempo de hechos del mundo y de América. Sirve para ver que no fue un hecho aislado.",
    prior=["Sé leer una línea de tiempo y restar años.", "Sé que Chile fue una colonia del rey de España hasta 1810.", "Sé reconocer países y ciudades de América en un mapa."],
    explain=[
        "Una colonia es un territorio gobernado por otro país. Hasta comienzos del siglo XIX, casi toda América del Sur dependía del rey de España. La independencia fue el proceso por el cual esos territorios dejaron de obedecer al rey y formaron países con gobierno propio.",
        "Para entenderlo, ubicamos los hechos en el tiempo y en el espacio. Primero ocurrieron cambios en otras partes del mundo: la independencia de Estados Unidos en 1776 y la Revolución Francesa en 1789. Después, en 1808, Napoleón invadió España y el rey dejó el trono. Eso dejó al imperio español sin su autoridad más importante.",
        "En 1810 varias ciudades de América, como Caracas, Buenos Aires y Santiago, formaron juntas de gobierno. Estas son grupos de personas que gobiernan en lugar de una autoridad ausente. Por eso decimos que la independencia de Chile fue parte de un proceso continental: ocurrió en muchos lugares de América, en años cercanos, con hechos conectados.",
    ],
    vocab=[("colonia", "territorio gobernado por otro país lejano"), ("independencia", "proceso por el cual un territorio deja de depender de otro y se gobierna solo"), ("junta de gobierno", "grupo de personas que gobierna mientras falta la autoridad"), ("proceso continental", "hechos conectados que ocurren en muchos lugares de un continente"), ("cronología", "orden de los hechos según el año en que ocurrieron")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre la Revolución Francesa y la independencia de Haití?", ["Busco los años en la ficha: 1789 y 1804.", "Resto el menor al mayor: 1804 − 1789 = 15."], "15 años"),
        ("Ubicar un hecho en el espacio", "{F} ¿Dónde ocurrió la batalla de Ayacucho y qué resultado tuvo?", ["La ficha dice que fue en Perú.", "Agrega que allí el ejército del rey fue derrotado de manera final en Sudamérica."], "En Perú; el ejército del rey fue derrotado"),
    ],
    mistakes=[("Decir que Chile fue el primer territorio americano en independizarse.", "Se mira solo la historia de Chile y no el contexto de América.", "Antes de 1818 ya se habían declarado independientes Estados Unidos (1776) y Haití (1804)."),
              ("Creer que las juntas de 1810 se formaron todas el mismo día.", "Se mira el año y no el mes.", "Caracas formó su junta en abril, Buenos Aires en mayo y Santiago en septiembre de 1810.")],
    T=[
        ("{F} ¿En qué fecha se formó la junta de gobierno de Santiago de Chile?", "18 de septiembre de 1810", "La ficha da esa fecha para Santiago."),
        ("=", "{F} Estados Unidos se declaró independiente en 1776 y Chile proclamó su independencia en 1818. ¿Cuántos años pasaron entre ambos hechos?", "1818-1776", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué ocurrió primero: la Revolución Francesa o la invasión de Napoleón a España?", "la Revolución Francesa", "Comenzó en 1789; la invasión fue en 1808."),
        ("=", "{F} ¿Cuántos años pasaron entre la invasión de Napoleón a España y la proclamación de la independencia de Chile?", "1818-1808", "Se restan los años de la ficha.", " años"),
        ("{F} ¿Qué tres ciudades de América formaron juntas de gobierno en 1810 según la ficha?", "Caracas, Buenos Aires y Santiago de Chile", "La ficha las nombra con su fecha."),
        ("{F} ¿Cuál fue la primera colonia de la ficha en declararse independiente y en qué año?", "las trece colonias británicas (Estados Unidos), en 1776", "1776 es el año más antiguo de la ficha."),
        ("{F} Ordena de más antiguo a más reciente: batalla de Ayacucho, independencia de Haití, junta de Santiago, Revolución Francesa.", "Revolución Francesa, independencia de Haití, junta de Santiago, batalla de Ayacucho", "Los años son 1789, 1804, 1810 y 1824."),
        ("=", "{F} ¿Cuántos años pasaron entre la proclamación de la independencia de Chile y la batalla de Ayacucho?", "1824-1818", "Se resta el año de 1818 al de 1824.", " años"),
        ("{F} Clasifica cada hecho en «ocurrió en América» o «ocurrió fuera de América»: a) Revolución Francesa; b) independencia de Haití; c) invasión de Napoleón a España; d) junta de Buenos Aires.", "en América: b y d; fuera de América: a y c", "Haití y Buenos Aires están en América; Francia y España en Europa."),
        ("{F} Camila dice: «Chile fue el primer territorio de América en independizarse». Corrígela con datos de la ficha.", "No: Estados Unidos (1776) y Haití (1804) se declararon independientes antes que Chile (1818)", "Hay fechas anteriores a 1818 en la ficha."),
        ("{F} Tomás dice: «Las juntas de 1810 se formaron en el mismo mes en todas las ciudades». ¿Es correcto? Usa las fechas.", "No: Caracas en abril, Buenos Aires en mayo y Santiago en septiembre", "Los meses de la ficha son distintos."),
        ("=", "{F} Una línea de tiempo parte en 1770 y usa la escala 1 cm = 10 años. ¿A cuántos centímetros del inicio debe ir el año 1810? (Calcula (1810 − 1770) ÷ 10).", "(1810-1770)//10", "Cada 10 años equivalen a 1 cm; hay 40 años de diferencia.", " cm"),
        ("{F} Un compañero dice que la independencia de Chile fue «un hecho aislado». Nombra dos hechos de la ficha, anteriores a 1818, que muestren que no lo fue.", "dos cualesquiera de: independencia de Estados Unidos (1776), Revolución Francesa (1789), independencia de Haití (1804), invasión de Napoleón (1808), juntas de Caracas o Buenos Aires (1810)", "Todos esos hechos son anteriores y se relacionan con el proceso."),
    ],
    ctx=("Un panel de museo muestra tres fechas del año 1810: junta de Caracas, junta de Buenos Aires y junta de Santiago. ¿Qué idea de esta clase apoya el panel?", "que la independencia fue un proceso continental: varias ciudades actuaron en años cercanos", "Tres lugares distintos actúan en el mismo año."),
    sc=[("En una línea de tiempo, ¿qué va primero: 1808 o 1810?", "1808", "El año menor va más a la izquierda."),
        ("¿Para qué sirve ubicar un hecho en la cronología y en el mapa?", "para ver con qué otros hechos se conecta y no estudiarlo aislado", "Ubicar permite relacionar tiempos y lugares."),
        ("{F} ¿En qué país de Sudamérica se libró la batalla de Ayacucho?", "Perú", "La ficha dice que fue en Perú.")],
    op=("Dibuja una línea de tiempo que parta en 1770 y termine en 1830. Marca con un punto cada año de esta ficha y escribe una frase corta junto a cada punto. Pinta de otro color los hechos que ocurrieron en América. {F}",
        "Puntos en 1776, 1789, 1804, 1808, 1810, 1818 y 1824, en ese orden, con una frase breve y los hechos americanos de otro color.",
        ["los siete años están en orden", "cada punto tiene una frase correcta", "los hechos de América se distinguen por color"], ["línea de tiempo dibujada", "colores aplicados"], ["poner 1810 antes de 1808", "olvidar pintar Haití o las juntas como hechos de América"],
        "Pide que explique por qué la junta de Santiago no está sola en la línea de tiempo."),
    reinforce="Di en voz alta los siete años de la ficha en orden, con un hecho para cada uno.",
    extend="Escribe una pregunta sobre qué relación puede haber entre los hechos de 1776 y 1789 y las juntas de 1810.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes inventadas para este cuaderno, a partir de situaciones reales de la época). "
     "Fuente A, carta de un comerciante criollo de Santiago, 1809: «El trigo se pierde en el puerto porque solo podemos vender a los lugares que el rey autoriza. Comerciantes de otros países pagarían mejor». "
     "Fuente B, informe de un funcionario nacido en España, enviado por el rey, 1809: «Los criollos son leales, pero algunos olvidan que es el rey quien decide quién gobierna». "
     "Fuente C, página de un libro de historia escrito en 1950 por un historiador: «La crisis de España en 1808 abrió el camino a las juntas de 1810». "
     "Fuente D, proclama de una junta, 1810: «Gobernaremos en nombre del rey Fernando VII mientras él esté preso».")
build(
    OA1, 2, F,
    use="Aprenderé a preguntar quién escribió una fuente, cuándo y desde qué punto de vista. Sirve para no creer que una sola fuente cuenta toda la historia de la independencia.",
    prior=["Sé que una fuente es una pista sobre el pasado.", "Sé que en 1808 el rey de España dejó el trono.", "Sé qué es una colonia."],
    explain=[
        "Los historiadores estudian el pasado con fuentes. Una fuente primaria se creó en la época que se estudia, como una carta de 1809. Una fuente secundaria se escribió después, como un libro de 1950 que cuenta lo ocurrido. Para usar una fuente hay que preguntar quién la hizo, cuándo, para quién y con qué propósito.",
        "Dos personas pueden ver el mismo hecho de manera distinta. Un comerciante nacido en América (criollo) puede quejarse del comercio limitado. Un funcionario nacido en España (peninsular) y enviado por el rey puede defender que la autoridad es del rey. Cada fuente muestra una perspectiva: el punto de vista de quien la escribe.",
        "Ninguna fuente sola basta. La carta del comerciante no dice qué pensaban las mujeres ni los pueblos indígenas. La proclama de 1810 muestra que esa junta dijo gobernar en nombre del rey preso. Por eso una conclusión debe apoyarse en varias fuentes, y hay que reconocer lo que ellas no permiten saber.",
    ],
    vocab=[("fuente primaria", "documento creado en la época que se estudia"), ("fuente secundaria", "texto escrito después, a partir de otras fuentes"), ("criollo", "persona de familia española nacida en América"), ("peninsular", "persona nacida en España que vivía en América"), ("perspectiva", "punto de vista de quien escribe")],
    worked=[
        ("Clasificar una fuente", "{F} ¿La fuente C es primaria o secundaria? Explica.", ["Veo que se escribió en 1950.", "Los hechos que cuenta son de 1808 y 1810, es decir, mucho antes."], "Secundaria: se escribió después de los hechos"),
        ("Reconocer una perspectiva", "{F} ¿Desde qué punto de vista habla la fuente B?", ["La escribe un funcionario nacido en España y enviado por el rey.", "Defiende que el rey decide quién gobierna."], "Desde el de un funcionario del rey"),
    ],
    mistakes=[("Creer que una fuente primaria siempre dice toda la verdad.", "Se olvida que quien escribe tiene un punto de vista.", "Se pregunta quién escribe y para qué, y se compara con otras fuentes."),
              ("Usar una sola carta para decir lo que pensaba toda la sociedad.", "Se generaliza más allá de la evidencia.", "Una carta muestra la opinión de una persona; hay que sumar otras fuentes.")],
    T=[
        ("{F} ¿Quién escribió la fuente A?", "un comerciante criollo de Santiago", "El encabezado de la fuente A lo dice."),
        ("{F} ¿En qué año se escribió la fuente C?", "1950", "La ficha indica 1950 como año del libro."),
        ("{F} ¿Qué dijo la junta en la fuente D sobre en nombre de quién gobernaría?", "en nombre del rey Fernando VII", "La proclama lo declara con esas palabras."),
        ("{F} ¿Cuáles fuentes son primarias? Nombra las tres letras.", "A, B y D", "Se crearon en 1809 y 1810, durante los hechos."),
        ("{F} ¿Por qué la fuente C es secundaria?", "porque la escribió un historiador en 1950, mucho después de los hechos", "Su año es posterior a lo que cuenta."),
        ("{F} ¿Qué queja de comercio aparece en la fuente A?", "que solo pueden vender a los lugares que el rey autoriza", "La carta lo dice sobre el trigo."),
        ("=", "{F} ¿Cuántos años pasaron entre la fuente D (1810) y la fuente C (1950)?", "1950-1810", "Se resta el año menor al mayor.", " años"),
        ("{F} Compara A y B: ¿quién critica el comercio limitado y quién defiende la autoridad del rey?", "A critica el comercio limitado; B defiende la autoridad del rey", "Cada autor habla desde su situación."),
        ("{F} Una compañera dice: «La fuente A prueba que todos los chilenos pensaban lo mismo». ¿Qué error comete?", "generaliza: una carta solo muestra la opinión de un comerciante", "Una persona no habla por toda la sociedad."),
        ("{F} ¿Qué no permite saber ninguna de las cuatro fuentes sobre los pueblos indígenas y las mujeres?", "lo que pensaban, porque ninguna fuente los menciona", "Ninguna cita a esos grupos."),
        ("{F} Para saber si la fuente D es una buena prueba de que esa junta quería la independencia en 1810, ¿qué dato de ella debes considerar?", "que dice gobernar en nombre del rey, no que quiera independencia", "La proclama no habla de independencia."),
        ("{F} Elige la mejor pregunta para investigar la fuente B: A) ¿Es bonita la letra? B) ¿Qué intereses tenía quien escribió? C) ¿Cuántas hojas tiene?", "B", "Los intereses ayudan a entender la perspectiva."),
        ("{F} Ordena las cuatro fuentes de la más antigua a la más reciente. Si dos son del mismo año, ponlas en orden alfabético de su letra.", "A, B, D, C", "A y B son de 1809, D de 1810 y C de 1950."),
    ],
    ctx=("Para una exposición, un compañero tiene solo la fuente C y quiere explicar cómo vivía la gente común en 1809. ¿Qué le aconsejas?", "buscar fuentes de la época, como cartas, porque C es posterior y habla de política", "C es secundaria y no describe la vida diaria."),
    sc=[("¿Qué se pregunta primero a una fuente: quién la escribió, o cuántas hojas tiene?", "quién la escribió", "El autor ayuda a entender el punto de vista."),
        ("{F} ¿Qué diferencia hay entre una fuente primaria y una secundaria?", "la primaria se creó en la época estudiada y la secundaria después", "La diferencia es el momento de creación."),
        ("¿Por qué conviene usar más de una fuente?", "porque cada una muestra una perspectiva y deja cosas sin decir", "Una sola fuente es parcial.")],
    op=("Escribe en tu cuaderno una ficha de análisis con cuatro filas, una por cada fuente de la ficha (A, B, C y D). En cada fila anota: quién escribe, en qué año, si es primaria o secundaria y una cosa que no permite saber. {F}",
        "Fila A: comerciante criollo, 1809, primaria, no dice qué pensaban los pueblos indígenas. Fila C: historiador, 1950, secundaria, no es testigo de los hechos.",
        ["cuatro filas completas", "primaria o secundaria bien indicada", "un límite razonable por fuente"], ["ficha de análisis de cuatro filas"], ["marcar C como primaria", "no anotar límites"],
        "Pide que explique por qué su límite para la fuente D es verdadero."),
    reinforce="Repite en voz alta las tres preguntas para una fuente: ¿quién la escribió?, ¿cuándo?, ¿qué punto de vista tiene?",
    extend="Imagina otra fuente de 1810 escrita por una persona distinta. Escribe quién sería y qué crees que diría, marcando que es una suposición.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (causas y consecuencias, hecha para este cuaderno). Antecedentes que ayudan a explicar la independencia: "
     "1) Ideas de la Ilustración, como la libertad y que el poder viene del pueblo, que circularon entre personas instruidas. "
     "2) Ejemplos de Estados Unidos (1776) y Francia (1789). "
     "3) La crisis de España en 1808, cuando el rey dejó el trono. "
     "4) El descontento de muchos criollos, porque los cargos más altos solían darse a peninsulares y el comercio estaba limitado por el rey. "
     "Consecuencias: formación de juntas de gobierno, guerras entre patriotas (que querían gobierno propio) y realistas (leales al rey), y nacimiento de nuevos países en América.")
build(
    OA1, 3, F,
    use="Aprenderé a distinguir causas de consecuencias y a ver quiénes actuaron en la independencia. Sirve para explicar por qué ocurrió y qué cambió.",
    prior=["Sé qué fue la crisis de España de 1808.", "Sé la diferencia entre criollo y peninsular.", "Sé leer fuentes y reconocer su punto de vista."],
    explain=[
        "Un acontecimiento histórico rara vez tiene una sola causa. Una causa es lo que ayuda a que algo ocurra; una consecuencia es lo que ocurre después. Para la independencia hubo varios antecedentes, es decir, hechos y situaciones anteriores que prepararon el proceso.",
        "Algunos antecedentes fueron ideas, como las de la Ilustración. Otros fueron ejemplos, como la independencia de Estados Unidos y la Revolución Francesa. Otros fueron hechos de España, como la crisis de 1808. Otros fueron descontentos de los criollos: querían ocupar cargos importantes y comerciar con más libertad.",
        "Los actores, o personas que participaron, tenían intereses distintos. Los patriotas querían gobierno propio; los realistas defendían al rey. Había criollos, peninsulares, mestizos, indígenas y personas esclavizadas, y no todos pensaban igual. Como consecuencia, surgieron juntas, hubo guerras y aparecieron nuevos países en América.",
    ],
    vocab=[("antecedente", "hecho o idea anterior que ayuda a explicar algo posterior"), ("causa", "razón que ayuda a que algo ocurra"), ("consecuencia", "resultado que viene después de un hecho"), ("patriota", "persona que quería gobierno propio para su territorio"), ("realista", "persona leal al rey de España")],
    worked=[
        ("Clasificar causa y consecuencia", "{F} ¿La formación de juntas de gobierno es causa o consecuencia?", ["Busco la lista: aparece entre las consecuencias.", "Las juntas se forman después de la crisis de 1808."], "Es una consecuencia"),
        ("Identificar un actor", "{F} ¿Quiénes querían gobierno propio y quiénes defendían al rey?", ["Leo la definición de cada bando.", "Patriotas: gobierno propio. Realistas: leales al rey."], "Los patriotas querían gobierno propio y los realistas defendían al rey"),
    ],
    mistakes=[("Explicar la independencia con una sola causa.", "Se simplifica un proceso complejo.", "Se nombran varios antecedentes: ideas, ejemplos, crisis de España y descontento criollo."),
              ("Pensar que todos los habitantes eran patriotas.", "Se ignora que había realistas y personas indiferentes.", "Había bandos con intereses distintos.")],
    T=[
        ("{F} ¿Qué causa de la ficha tiene relación con lo que ocurrió en España en 1808?", "la crisis de España cuando el rey dejó el trono", "La ficha la nombra como causa 3."),
        ("{F} ¿Cómo se llaman las personas que querían gobierno propio?", "patriotas", "La ficha define a los patriotas así."),
        ("{F} ¿Cuál aparece primero en la lista de consecuencias: juntas de gobierno o guerras?", "juntas de gobierno", "Las juntas aparecen primero entre las consecuencias."),
        ("{F} Clasifica en «causa» o «consecuencia»: a) ideas de la Ilustración; b) guerras entre patriotas y realistas; c) descontento de los criollos; d) nuevos países.", "causa: a y c; consecuencia: b y d", "Las ideas y el descontento son anteriores; las guerras y nuevos países, posteriores."),
        ("{F} Un criollo reclama que los altos cargos van a peninsulares. ¿A qué antecedente de la ficha corresponde?", "al descontento de los criollos", "Es el antecedente número 4."),
        ("{F} ¿Qué dos ejemplos de otros lugares conocieron los criollos según la ficha?", "Estados Unidos (1776) y Francia (1789)", "La ficha los nombra como antecedente 2."),
        ("{F} Un comerciante criollo dice: «Quiero vender mi trigo a otros países». ¿Qué antecedente muestra?", "que el comercio estaba limitado por el rey", "El antecedente 4 menciona esa limitación."),
        ("{F} Un funcionario enviado por el rey ordena castigar a quien forme una junta sin permiso. ¿Era patriota o realista?", "realista", "Defiende la autoridad del rey."),
        ("{F} Un criollo lee un libro que dice que todas las personas tienen derecho a la libertad y que el poder viene del pueblo. ¿A qué antecedente corresponde?", "a las ideas de la Ilustración", "Esa idea figura en el antecedente 1."),
        ("{F} Lucas dice: «La independencia ocurrió solo porque los criollos querían cargos». ¿Qué le falta considerar?", "otros antecedentes: ideas, ejemplos externos y la crisis de España", "La ficha lista cuatro antecedentes, no uno."),
        ("{F} Sofía dice: «Todas las personas de América querían la independencia». ¿Qué dato de la ficha lo contradice?", "que existían realistas, leales al rey", "Hubo bandos con intereses distintos."),
        ("{F} Si el rey no hubiera dejado el trono en 1808, ¿cuál antecedente de la ficha no habría ocurrido?", "la crisis de España de 1808", "Esa causa depende de ese hecho."),
        ("{F} Ordena en cadena: guerras entre patriotas y realistas, crisis de España de 1808, formación de juntas.", "crisis de España de 1808, formación de juntas, guerras entre patriotas y realistas", "Cada hecho lleva al siguiente según la ficha."),
    ],
    ctx=("Un afiche escolar dice: «La independencia de América se debió solo a las ideas de la Ilustración». Usa la ficha para decir por qué la explicación es incompleta.", "porque también influyeron los ejemplos externos, la crisis de España y el descontento de los criollos", "La ficha enumera cuatro antecedentes."),
    sc=[("¿Qué es una causa y qué es una consecuencia?", "causa: lo que ayuda a que algo ocurra; consecuencia: lo que ocurre después", "Se distinguen por el momento en que ocurren."),
        ("{F} ¿Qué querían los patriotas?", "gobierno propio", "La ficha lo define."),
        ("{F} Nombra un antecedente de la ficha que sea una idea.", "las ideas de la Ilustración, como la libertad", "Es el antecedente 1.")],
    op=("En tu cuaderno dibuja una tabla de tres columnas: «antecedentes», «hecho central» y «consecuencias». Escribe en cada columna al menos dos elementos de la ficha. Después, escribe una frase que explique cómo se conectan. {F}",
        "Antecedentes: ideas de la Ilustración y descontento de los criollos. Hecho central: la crisis de España de 1808. Consecuencias: juntas y guerras. Frase: la crisis dio la oportunidad para que las juntas gobernaran.",
        ["tres columnas con al menos dos elementos cada una", "elementos en la columna correcta", "frase que conecta causa y consecuencia"], ["tabla de tres columnas", "frase de conexión"], ["poner las guerras como antecedente", "dejar la columna central vacía"],
        "Pide que cambie un elemento de columna y explique por qué su cambio produce un error."),
    reinforce="Con tus palabras, di dos antecedentes y dos consecuencias de la independencia sin mirar la ficha.",
    extend="Escribe cómo habría sido distinto el proceso si el rey de España no hubiera dejado el trono en 1808, marcando que es una suposición.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación de territorios, hecha para este cuaderno). "
     "Venezuela: junta en Caracas en abril de 1810; independencia declarada en 1811; guerras largas con el ejército del rey; Simón Bolívar fue un jefe patriota. "
     "Río de la Plata (hoy Argentina): junta en Buenos Aires en mayo de 1810; independencia declarada en 1816 en Tucumán; José de San Martín organizó un ejército que cruzó los Andes hacia Chile en 1817. "
     "México: en septiembre de 1810 el sacerdote Miguel Hidalgo llamó a levantarse contra el gobierno colonial; la independencia se consiguió en 1821. "
     "Chile: junta en septiembre de 1810; independencia proclamada en 1818, con ayuda del ejército de San Martín y de Bernardo O'Higgins. "
     "Perú: San Martín proclamó la independencia en Lima en 1821.")
build(
    OA1, 4, F,
    use="Aprenderé a comparar cómo ocurrió la independencia en distintos territorios. Sirve para ver qué compartieron y en qué se diferenciaron, y entender que Chile fue parte de un proceso continental.",
    prior=["Sé ubicar los hechos de la independencia en una línea de tiempo.", "Sé distinguir causas y consecuencias.", "Sé qué es una junta de gobierno."],
    explain=[
        "Comparar es buscar semejanzas y diferencias con un criterio claro. Para comparar la independencia de varios territorios usamos criterios como el año de la junta, el año de la declaración de independencia, los jefes y la forma en que se logró.",
        "Hubo semejanzas. En Caracas, Buenos Aires y Santiago se formaron juntas en 1810. En todos los territorios hubo bandos que se enfrentaron, y los jefes patriotas coordinaron fuerzas. También hubo diferencias: Venezuela declaró su independencia en 1811, el Río de la Plata en 1816 y Chile en 1818. México tuvo un levantamiento liderado por un sacerdote.",
        "San Martín muestra por qué hablamos de un proceso continental: un ejército nacido en el Río de la Plata cruzó los Andes en 1817, ayudó a liberar Chile y luego siguió a Perú. Así, la independencia de Chile estuvo ligada a la de sus vecinos. Sin embargo, cada territorio tuvo su propio ritmo y sus propios protagonistas.",
    ],
    vocab=[("comparar", "buscar semejanzas y diferencias usando un criterio"), ("criterio", "aspecto que usamos para comparar, como el año o el jefe"), ("declaración de independencia", "documento o acto oficial en que un territorio dice que ya no depende de otro"), ("ejército libertador", "fuerza armada patriota que luchaba por la independencia"), ("territorio", "espacio gobernado por una autoridad")],
    worked=[
        ("Comparar con un criterio", "{F} Compara el año de la declaración de independencia de Venezuela y de Chile.", ["Venezuela declaró en 1811 y Chile en 1818.", "Resto: 1818 − 1811 = 7."], "Chile declaró 7 años después que Venezuela"),
        ("Hallar una semejanza", "{F} ¿Qué tuvieron en común Caracas, Buenos Aires y Santiago en 1810?", ["Reviso las tres entradas de la ficha.", "En las tres se formó una junta de gobierno."], "Formaron una junta de gobierno en 1810"),
    ],
    mistakes=[("Decir que la independencia fue idéntica en todos los territorios.", "Se confunde proceso continental con proceso igual en todas partes.", "Hubo hechos compartidos, pero distintos años, jefes y formas."),
              ("Comparar sin criterio, mezclando años con jefes.", "No se fija qué se compara.", "Primero se elige un criterio y luego se comparan los territorios con él.")],
    T=[
        ("{F} ¿En qué año declaró su independencia el Río de la Plata y dónde?", "1816, en Tucumán", "La ficha lo indica."),
        ("{F} ¿Quién fue el jefe patriota que se menciona para Venezuela?", "Simón Bolívar", "La ficha lo nombra en la entrada de Venezuela."),
        ("{F} ¿Qué sacerdote llamó a levantarse en México en 1810?", "Miguel Hidalgo", "La ficha lo nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la declaración de independencia del Río de la Plata y la de Chile?", "1818-1816", "Se restan los años de la ficha.", " años"),
        ("{F} ¿En qué año cruzó los Andes el ejército de San Martín hacia Chile?", "1817", "La ficha da ese año."),
        ("{F} ¿Qué territorio de la ficha empezó su proceso con un llamado a levantarse y no con una junta?", "México", "Solo la entrada de México habla de un llamado de un sacerdote."),
        ("{F} Con el criterio «año de la declaración de independencia», ordena de la más antigua a la más reciente: Chile, Venezuela, Río de la Plata.", "Venezuela (1811), Río de la Plata (1816), Chile (1818)", "El orden depende de los años de la ficha."),
        ("=", "{F} ¿Cuántos años pasaron entre el llamado de Hidalgo en México y la independencia de México?", "1821-1810", "Se resta el año de inicio al año final.", " años"),
        ("{F} ¿Qué tres territorios de la ficha aparecen unidos por la acción de San Martín?", "el Río de la Plata, Chile y Perú", "San Martín organizó el ejército y proclamó la independencia en Lima."),
        ("{F} Marta dice: «Chile se independizó antes que Venezuela». Usa los años de la ficha para corregirla.", "No: Venezuela declaró en 1811 y Chile en 1818", "1811 es anterior a 1818."),
        ("{F} Pablo dice: «México y Chile tuvieron el mismo comienzo». ¿Qué diferencia de la ficha lo contradice?", "en México el comienzo fue un levantamiento llamado por un sacerdote; en Chile, una junta", "Los comienzos son distintos."),
        ("{F} Da una razón de la ficha que muestre que la independencia de Chile fue parte de un proceso continental.", "San Martín organizó en el Río de la Plata un ejército que cruzó los Andes hacia Chile", "Muestra la conexión entre territorios."),
        ("{F} Si el criterio es «año en que se formó una junta», ¿qué territorio quedaría primero en el orden de la ficha?", "Venezuela, en abril de 1810", "Caracas formó su junta antes que Buenos Aires y Santiago."),
    ],
    ctx=("Un cartel de la sala de historia dice: «Cada país tuvo su independencia: no hay nada en común». Usa la ficha para responder.", "no es cierto: hubo juntas parecidas, jefes que cooperaron y un ejército que cruzó los Andes", "La ficha muestra semejanzas y conexiones."),
    sc=[("¿Qué se necesita antes de comparar dos territorios?", "un criterio, como el año o el jefe", "Sin criterio la comparación se mezcla."),
        ("{F} ¿Quién proclamó la independencia de Perú en Lima en 1821?", "José de San Martín", "La ficha lo dice."),
        ("¿Por qué decimos que la independencia fue un proceso continental?", "porque ocurrió en muchos lugares de América con hechos conectados", "Los territorios actuaron en años cercanos y se ayudaron.")],
    op=("Dibuja una tabla con cuatro filas (Venezuela, Río de la Plata, Chile y México) y tres columnas: «año de la declaración o logro de la independencia», «jefe o líder de la ficha» y «un rasgo distinto». Completa con la ficha y escribe una frase final que diga una semejanza y una diferencia. {F}",
        "Chile: 1818; San Martín y O'Higgins; independencia con ayuda de un ejército que cruzó los Andes. Frase: Todos tuvieron bandos que se enfrentaron, pero declararon la independencia en años distintos.",
        ["cuatro filas completas con datos de la ficha", "un criterio por columna", "frase con semejanza y diferencia"], ["tabla comparativa", "frase de cierre"], ["poner 1810 como declaración de Chile", "no escribir ninguna diferencia"],
        "Pide que explique qué columna le sirvió más para encontrar una diferencia."),
    reinforce="Elige dos territorios de la ficha y di en voz alta una semejanza y una diferencia entre ellos.",
    extend="Escribe una pregunta que la ficha no responde sobre cómo participaron las mujeres en las independencias de estos territorios.",
)
