"""Material del estudiante de 1.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (personas que contribuyen) y OA 08 (mapas y planos)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA7, OA8 = "HI01 OA 07", "HI01 OA 08"

HURTADO = ("Alberto Hurtado nació el 22 de enero de 1901 en Viña del Mar. Fue sacerdote jesuita. En 1944 fundó el Hogar de Cristo para ayudar a niños y a personas que no tenían casa. "
           "Murió el 18 de agosto de 1952.")
MISTRAL = ("Gabriela Mistral se llamaba Lucila Godoy Alcayaga. Nació el 7 de abril de 1889 en Vicuña, en el valle de Elqui. Fue maestra. Publicó el libro «Ternura» en 1924, con poemas y rondas para niños. "
           "En 1945 recibió el Premio Nobel de Literatura. Murió el 10 de enero de 1957.")
DIAZ = ("Eloísa Díaz nació el 25 de junio de 1866 en Santiago. Estudió medicina y se recibió de médica en 1887. Fue la primera mujer en recibirse de médica en Chile. Cuidó la salud de niñas y niños de las escuelas.")
PARRA = ("Violeta Parra nació el 4 de octubre de 1917 en la zona de Ñuble. Recorrió Chile para recoger canciones que cantaba la gente del campo. Compuso canciones, bordó arpilleras y pintó. "
         "Murió el 5 de febrero de 1967.")
AHRENS = ("Marlene Ahrens nació el 27 de enero de 1933 en Santiago. Lanzaba la jabalina. En los Juegos Olímpicos de Melbourne, en 1956, ganó la medalla de plata, la primera medalla olímpica de una mujer chilena.")
VALDIVIA = ("Pedro de Valdivia llegó a Chile desde España. El 12 de febrero de 1541 fundó la ciudad de Santiago, junto al cerro Huelén, que hoy se llama Santa Lucía. En ese valle ya vivían pueblos originarios.")
CAFFARENA = ("Elena Caffarena nació en 1903 y fue abogada. En 1935 fundó con otras mujeres el MEMCh, un movimiento para defender los derechos de las mujeres. "
             "Ayudó a conseguir que las mujeres pudieran votar en todas las elecciones, lo que ocurrió en 1949. Murió en 2003.")

# ---------------------------------------------------------------- OA 07
register(
    OA7, 1,
    materials="Lápiz y papel. La biografía breve de Alberto Hurtado está escrita en los ejercicios.",
    use="Aprenderé qué significa contribuir a la sociedad y reconoceré que una acción puede ayudar a muchas personas. Sirve para valorar a quienes hacen cosas buenas por otros.",
    prior=["Sé qué es ayudar a alguien.", "Sé leer fechas con año."],
    explain=[
        "Contribuir es hacer algo que ayuda a otras personas o mejora la vida de muchos. Una persona contribuye cuando cuida a otros, enseña, descubre algo útil, crea arte o ayuda a quien lo necesita. No hace falta ser famoso para contribuir: un vecino que cuida la plaza también contribuye.",
        "Alberto Hurtado es un ejemplo. Nació en Viña del Mar en 1901. En 1944 fundó el Hogar de Cristo para ayudar a niños y a personas que no tenían casa. Murió en 1952. Su acción de ayudar benefició a muchas personas durante muchos años.",
        "Para saber si alguien contribuyó, hazte dos preguntas: ¿qué hizo? y ¿a quiénes ayudó o benefició? Si puedes responder las dos, ya tienes la idea de su aporte. También sirve poner la historia en una línea de tiempo con los años.",
    ],
    vocab=[("contribuir", "hacer algo que ayuda a otros o a la sociedad"), ("aporte", "lo que una persona da o hace por los demás"), ("sociedad", "todas las personas que vivimos juntas"), ("fundar", "crear algo por primera vez"), ("beneficiar", "dar algo bueno a alguien")],
    worked=[
        {"title": "Qué hizo y a quién ayudó", "problem": f"{HURTADO} ¿Qué hizo y a quiénes ayudó?", "steps": ["Busco la acción: fundó el Hogar de Cristo.", "Busco a quiénes ayudó: niños y personas sin casa."], "answer": "Fundó el Hogar de Cristo y ayudó a niños y a personas sin casa"},
        {"title": "Años de la historia", "problem": f"{HURTADO} ¿Cuántos años pasaron entre su nacimiento y la fundación del Hogar de Cristo?", "steps": ["Nació en 1901 y fundó el Hogar en 1944.", "1944 − 1901 = 43."], "answer": "43 años"},
    ],
    mistakes=[
        {"wrong": "Creer que contribuir es solo para personas famosas.", "why": "Se recuerda más a quienes están en los libros.", "fix": "También contribuyen los vecinos y las personas comunes."},
        {"wrong": "Decir lo que hizo una persona sin decir a quién ayudó.", "why": "Se olvida el beneficio.", "fix": "Responde siempre: ¿qué hizo? y ¿a quién ayudó?"},
    ],
    tiers={
        "recovery": [
            ex(f"{HURTADO} ¿En qué ciudad nació Alberto Hurtado?", "Viña del Mar", "Así lo dice la biografía."),
            ex(f"{HURTADO} ¿En qué año fundó el Hogar de Cristo?", "1944", "Es el año que dice el texto."),
            ex(f"{HURTADO} ¿Qué mes murió Alberto Hurtado?", "agosto", "Murió el 18 de agosto de 1952."),
        ],
        "understand": [
            ex("¿Qué significa contribuir?", "Hacer algo que ayuda a otros o a la sociedad", "Es dar un aporte."),
            ex("¿Hay que ser famoso para contribuir?", "No", "Un vecino que cuida la plaza también contribuye."),
            ex(f"{HURTADO} ¿A quiénes ayudó el Hogar de Cristo?", "A niños y a personas sin casa", "Lo dice la biografía."),
        ],
        "apply": [
            arith(f"{HURTADO} ¿Cuántos años pasaron entre la fundación del Hogar de Cristo (1944) y la muerte de Hurtado (1952)?", "1952-1944", "Se resta el año de la fundación al año de su muerte."),
            ex("Una vecina reparte sopa caliente a quienes no tienen comida. ¿Contribuye a la sociedad?", "Sí", "Ayuda a otras personas."),
            ex(f"{HURTADO} Ordena: murió, fundó el Hogar de Cristo, nació.", "nació, fundó el Hogar de Cristo, murió", "Se ordenan por año: 1901, 1944 y 1952."),
        ],
        "reason": [
            ex("Un niño dice: «Hurtado contribuyó porque era sacerdote». ¿Cuál es la razón verdadera?", "Porque con su acción ayudó a muchas personas", "Contribuir se define por lo que se hace."),
            ex("Dos acciones: A) Lola se queda con todos los dulces. B) Lola reparte los dulces con su curso. ¿Cuál contribuye al bienestar del curso?", "B", "Compartir ayuda a todos."),
        ],
        "challenge": [
            arith(f"{HURTADO} ¿Cuántos años vivió Alberto Hurtado, entre 1901 y 1952?", "1952-1901", "Se resta el año de nacimiento al de su muerte."),
            ex("Una escuela junta ropa de abrigo para familias que lo necesitan. ¿Qué hizo (acción) y a quiénes ayudó?", "Juntó ropa; ayudó a familias que la necesitan", "Se responde qué hizo y a quién ayudó."),
        ],
    },
    context=[ex("En tu barrio, un grupo de vecinos limpia la plaza cada sábado. ¿A quiénes beneficia?", "A todos los vecinos", "Una plaza limpia sirve a todos.")],
    selfcheck=[
        ex("¿Qué es fundar?", "Crear algo por primera vez", "Hurtado fundó el Hogar de Cristo."),
        ex(f"{HURTADO} ¿Cuántos años tenía en 1944? Nació en 1901.", "43", "1944 − 1901 = 43."),
        ex("¿Qué dos preguntas ayudan a ver el aporte de una persona?", "¿Qué hizo? y ¿a quién ayudó?", "Son la acción y el beneficio."),
    ],
    open_task=task("Piensa en una persona de tu familia o barrio que ayude a otros. Escribe dos frases: una que diga qué hace y otra que diga a quién ayuda. Si no se te ocurre una, usa una de estas: una vecina que cuida la plaza, un bombero voluntario, una profesora que enseña a leer.", "Mi vecina limpia la plaza los sábados. Con eso ayuda a todos los niños que juegan allí.", ["dos frases", "dice qué hace y a quién ayuda", "persona real o de la lista"], ["dos frases escritas"], ["decir solo el nombre", "no mencionar el beneficio"], "Pide que explique por qué esa acción es un aporte."),
    reinforce="Cuenta a alguien de tu casa qué hizo Alberto Hurtado.",
    extend="Dibuja una línea de tiempo con 1901, 1944 y 1952 y escribe un hecho en cada año.",
)

register(
    OA7, 2,
    materials="Lápiz y papel. Las biografías breves de Eloísa Díaz, Violeta Parra, Marlene Ahrens y Alberto Hurtado están escritas en los ejercicios.",
    use="Aprenderé que se puede contribuir de muchas maneras: con la ciencia, el arte, el deporte y la solidaridad. Sirve para ver que hay muchos caminos para ayudar.",
    prior=["Sé qué es contribuir.", "Sé ordenar años en una línea de tiempo."],
    explain=[
        "Las personas contribuyen en distintos ámbitos, que son campos de la vida. Algunos ámbitos son: la ciencia, que busca conocer y cuidar; el arte, que crea belleza y expresa sentimientos; el deporte, que desarrolla el cuerpo y el esfuerzo; y la solidaridad, que ayuda a quien lo necesita.",
        "Eloísa Díaz, médica, aportó con la ciencia y la salud. Violeta Parra, artista, aportó con la música y la poesía. Marlene Ahrens, deportista, aportó con el deporte. Alberto Hurtado, sacerdote, aportó con la solidaridad. Todos viven en tiempos distintos, pero cada uno ayudó a su manera.",
        "Comparar ámbitos no es decir cuál es el mejor. Es ver que todos son necesarios. Para comparar, usa una tabla con la persona, el ámbito y lo que hizo.",
    ],
    vocab=[("ámbito", "campo de la vida, como ciencia, arte o deporte"), ("ciencia", "forma de conocer y cuidar el mundo con preguntas y pruebas"), ("arte", "creaciones como música, pintura o poesía"), ("deporte", "actividad física con reglas"), ("solidaridad", "ayudar a quien lo necesita")],
    worked=[
        {"title": "Unir persona y ámbito", "problem": f"{DIAZ} ¿En qué ámbito contribuyó Eloísa Díaz?", "steps": ["Era médica y cuidó la salud de escolares.", "Eso es ciencia y salud."], "answer": "En la ciencia y la salud"},
        {"title": "Ordenar por nacimiento", "problem": "Nacieron: Eloísa Díaz en 1866 y Alberto Hurtado en 1901. ¿Quién nació primero?", "steps": ["Comparo los años: 1866 y 1901.", "El menor nació primero."], "answer": "Eloísa Díaz"},
    ],
    mistakes=[
        {"wrong": "Decir que un ámbito es mejor que otro.", "why": "Se piensa que unos aportes valen más.", "fix": "Todos los ámbitos son necesarios."},
        {"wrong": "Confundir artista con deportista.", "why": "Los dos se presentan frente a otros.", "fix": "Mira qué hacen: crear obras es arte; competir con reglas es deporte."},
    ],
    tiers={
        "recovery": [
            ex(f"{PARRA} ¿En qué ámbito contribuyó Violeta Parra: arte o deporte?", "arte", "Compuso canciones y pintó."),
            ex(f"{AHRENS} ¿En qué deporte participó Marlene Ahrens?", "lanzamiento de jabalina", "Lanzaba la jabalina."),
            ex(f"{DIAZ} ¿Qué estudió Eloísa Díaz?", "medicina", "Así lo dice el texto."),
        ],
        "understand": [
            ex("¿Qué es un ámbito?", "Un campo de la vida, como ciencia, arte o deporte", "Agrupa tipos de aportes."),
            ex("¿Qué ámbito ayuda a quien lo necesita?", "la solidaridad", "Eso es ser solidario."),
            ex("¿Es un ámbito mejor que otro?", "No", "Todos son necesarios."),
        ],
        "apply": [
            ex("Une cada persona con su ámbito: Alberto Hurtado, Marlene Ahrens. Rmbitos: deporte, solidaridad.", "Hurtado: solidaridad; Ahrens: deporte", "Hurtado fundó el Hogar de Cristo y Ahrens lanzaba la jabalina."),
            ex("Años de nacimiento: Díaz 1866, Hurtado 1901, Parra 1917, Ahrens 1933. Ordénalos de la persona que nació antes a la que nació después.", "Díaz, Hurtado, Parra, Ahrens", "Se ordenan por el año de nacimiento."),
            arith(f"{AHRENS} Marlene Ahrens nació en 1933 y ganó su medalla en 1956. ¿Cuántos años tenía al ganarla?", "1956-1933", "Se resta el año de nacimiento al año de la medalla."),
        ],
        "reason": [
            ex("Un niño dice que el deporte es mejor que el arte. ¿Qué respondes?", "Todos los ámbitos son necesarios", "Cada uno aporta algo distinto."),
            ex(f"{PARRA} Violeta Parra viajó por Chile recogiendo canciones. ¿Qué cuidó con eso?", "La música tradicional de la gente del campo", "Guardó canciones que podían perderse."),
        ],
        "challenge": [
            ex("Cuatro personas: Díaz (ciencia), Parra (arte), Ahrens (deporte), Hurtado (solidaridad). ¿Cuántos ámbitos distintos hay?", "4", "Cada persona es de un ámbito distinto."),
            arith(f"{PARRA} Violeta Parra nació en 1917 y murió en 1967. ¿Cuántos años vivió?", "1967-1917", "Se resta el año de nacimiento al año de su muerte."),
        ],
    },
    context=[ex("En un concurso de la escuela, Ema dibuja un mural, Teo corre una carrera y Lola ayuda a limpiar la sala. ¿En qué ámbitos contribuyen?", "arte, deporte y solidaridad", "Dibujar es arte, correr es deporte y ayudar es solidaridad.")],
    selfcheck=[
        ex("¿La música es parte del arte o de la ciencia?", "del arte", "Crea belleza y expresa sentimientos."),
        ex("Si ayudas a un compañero que se cayó, ¿en qué ámbito estás contribuyendo?", "la solidaridad", "Ayudar a quien lo necesita es solidaridad."),
        ex(f"{DIAZ} ¿En qué ciudad nació Eloísa Díaz?", "Santiago", "Así lo dice el texto."),
    ],
    open_task=task("Haz una tabla de cuatro filas con persona, ámbito y qué hizo. Usa estas personas: Eloísa Díaz (cuidó la salud de las niñas y niños de las escuelas), Violeta Parra (recogió canciones), Marlene Ahrens (ganó una medalla olímpica), Alberto Hurtado (fundó el Hogar de Cristo). Completa la columna del ámbito: ciencia, arte, deporte o solidaridad.", "Díaz: ciencia, cuidó la salud. Parra: arte, recogió canciones. Ahrens: deporte, ganó medalla. Hurtado: solidaridad, fundó el Hogar de Cristo.", ["cuatro filas", "ámbito correcto para cada persona", "lo que hizo en una frase"], ["tabla con tres columnas"], ["poner dos personas en el mismo ámbito sin razón", "dejar la columna vacía"], "Pide que cuente qué ámbito le gustaría que fuera el suyo."),
    reinforce="Elige un ámbito y di tres cosas de la vida diaria que pertenecen a él.",
    extend="Escribe cuál es tu ámbito favorito para contribuir y por qué.",
)

register(
    OA7, 3,
    materials="Lápiz y papel. La biografía breve de Gabriela Mistral está escrita en los ejercicios.",
    use="Aprenderé a sacar información explícita de la biografía de una persona. Sirve para contar su vida con datos exactos.",
    prior=["Sé leer fechas.", "Sé qué es contribuir."],
    explain=[
        "Una biografía cuenta la vida de una persona. Para leerla, busca datos explícitos, es decir, que están escritos con claridad: cuándo nació, dónde, qué hizo y cuándo murió. Esos datos se pueden comprobar en la fuente.",
        "La vida de Gabriela Mistral, poeta chilena, se puede ordenar en una línea de tiempo: 1889, nació en Vicuña; 1924, publicó el libro «Ternura»; 1945, recibió el Premio Nobel de Literatura; 1957, murió. Fue la primera persona de América Latina en recibir ese premio de literatura.",
        "Cuando leas, separa lo que dice la fuente de lo que tú piensas. «Nació en Vicuña» es explícito. «Era muy simpática» no está en el texto. Por eso, cuando uses un dato, di dónde lo leíste.",
    ],
    vocab=[("biografía", "texto que cuenta la vida de una persona"), ("dato explícito", "dato escrito con claridad en el texto"), ("poeta", "persona que escribe poemas"), ("maestra", "persona que enseña en una escuela"), ("Premio Nobel", "premio internacional muy importante")],
    worked=[
        {"title": "Dato explícito", "problem": f"{MISTRAL} ¿En qué lugar nació Gabriela Mistral?", "steps": ["Busco la frase del nacimiento.", "Dice Vicuña, en el valle de Elqui."], "answer": "En Vicuña, en el valle de Elqui"},
        {"title": "Calcular años", "problem": f"{MISTRAL} ¿Cuántos años pasaron entre su nacimiento y el Premio Nobel?", "steps": ["Nació en 1889 y recibió el premio en 1945.", "1945 − 1889 = 56."], "answer": "56 años"},
    ],
    mistakes=[
        {"wrong": "Contestar con algo que no está en el texto.", "why": "Se responde con lo que ya se sabía.", "fix": "Busca la frase en la biografía y subráyala."},
        {"wrong": "Confundir el año de nacimiento con el año del premio.", "why": "Todos los años son números parecidos.", "fix": "Mira qué hecho acompaña a cada año."},
    ],
    tiers={
        "recovery": [
            ex(f"{MISTRAL} ¿Cómo se llamaba Gabriela Mistral antes de ser conocida por ese nombre?", "Lucila Godoy Alcayaga", "Es el nombre que da la biografía."),
            ex(f"{MISTRAL} ¿En qué año publicó el libro «Ternura»?", "1924", "Aparece en el texto."),
            ex(f"{MISTRAL} ¿A qué se dedicó como trabajo: maestra o médica?", "maestra", "Dice que fue maestra."),
        ],
        "understand": [
            ex("¿Qué es una biografía?", "Un texto que cuenta la vida de una persona", "Habla de lo que hizo y cuándo."),
            ex("¿Qué es un dato explícito?", "Un dato escrito con claridad en el texto", "No se inventa."),
            ex(f"{MISTRAL} ¿Para quiénes eran los poemas de «Ternura»?", "Para niños", "La biografía dice poemas y rondas para niños."),
        ],
        "apply": [
            arith(f"{MISTRAL} ¿Cuántos años pasaron entre «Ternura» (1924) y el Premio Nobel (1945)?", "1945-1924", "Se resta un año al otro."),
            arith(f"{MISTRAL} ¿Cuántos años pasaron entre el Premio Nobel (1945) y la muerte (1957)?", "1957-1945", "Se restan los años."),
            ex(f"{MISTRAL} Ordena los hechos: murió, nació, recibió el Premio Nobel, publicó «Ternura».", "nació, publicó «Ternura», recibió el Premio Nobel, murió", "Los años son 1889, 1924, 1945 y 1957."),
        ],
        "reason": [
            ex(f"{MISTRAL} Un niño dice: «Gabriela Mistral nació en Santiago». ¿Qué texto lo corrige?", "La biografía dice que nació en Vicuña", "La fuente da el lugar exacto."),
            ex(f"{MISTRAL} Un niño dice: «Era muy simpática». ¿Está en la biografía?", "No", "Es una opinión que no aparece en el texto."),
        ],
        "challenge": [
            arith(f"{MISTRAL} ¿Cuántos años vivió Gabriela Mistral, entre 1889 y 1957?", "1957-1889", "Se resta el año de nacimiento al año de su muerte."),
            ex(f"{MISTRAL} Escribe una frase con dos datos de su vida usando años.", "Gabriela Mistral nació en 1889 y recibió el Premio Nobel en 1945", "Incluye dos datos del texto."),
        ],
    },
    context=[ex("Una compañera lee en voz alta: «Gabriela Mistral fue maestra». Otro compañero dice «y también cantante». La profesora pide que muestre dónde dice eso. ¿Por qué?", "Para ver si el dato está en la fuente", "Un dato debe estar en el texto.")],
    selfcheck=[
        ex(f"{MISTRAL} ¿En qué año murió Gabriela Mistral?", "1957", "Murió el 10 de enero de 1957."),
        ex(f"{MISTRAL} ¿Qué premio recibió en 1945?", "el Premio Nobel de Literatura", "Está en la biografía."),
        ex("¿Dónde conviene buscar un dato: en el texto o en lo que creo?", "en el texto", "La fuente es lo que se puede comprobar."),
    ],
    open_task=task("Con la biografía de Gabriela Mistral que está en los ejercicios, escribe tres datos de su vida con su año, por ejemplo qué pasó en 1889, 1924 y 1945. Debajo escribe una frase que empiece con «Según la biografía…» y que diga cómo ayudó a los niños.", "1889: nació en Vicuña. 1924: publicó «Ternura». 1945: recibió el Premio Nobel de Literatura. Según la biografía, escribió poemas y rondas para niños.", ["tres datos con año", "frase con «Según la biografía…»", "datos correctos"], ["hoja con tres datos y una frase"], ["inventar datos", "años equivocados"], "Pide que muestre en el texto la frase de donde sacó cada dato."),
    reinforce="Lee en voz alta la biografía y subraya con lápiz los tres años.",
    extend="Escribe una pregunta que la biografía no responde y dónde la buscarías.",
)

register(
    OA7, 4,
    materials="Lápiz y papel. Las biografías breves de Eloísa Díaz, Elena Caffarena y un breve texto sobre Lautaro están escritas en los ejercicios.",
    use="Aprenderé que muchas mujeres y comunidades hicieron aportes que antes se nombraban poco. Sirve para conocer mejor la historia de todos.",
    prior=["Sé qué es contribuir.", "Sé sacar datos de una biografía."],
    explain=[
        "En muchos libros antiguos se nombraba más a unos hombres famosos y menos a mujeres y a comunidades. Por eso decimos que algunas personas fueron invisibilizadas: hicieron cosas importantes, pero casi no se contaban.",
        "Eloísa Díaz fue la primera mujer en recibirse de médica en Chile, en 1887. Elena Caffarena fundó en 1935 el MEMCh y luchó por el derecho de las mujeres a votar. En 1934 las mujeres pudieron votar en elecciones de la municipalidad y en 1949 en todas las elecciones. Lautaro fue un líder mapuche del siglo XVI que defendió a su pueblo y murió en 1557.",
        "Cuando leas una historia, pregúntate: ¿quiénes aparecen? ¿Quiénes faltan? Buscar a las personas que faltan es una forma de justicia y de conocer más.",
    ],
    vocab=[("invisibilizado", "persona cuyo aporte casi no se cuenta"), ("derecho", "algo que una persona puede hacer o tener por justicia"), ("votar", "elegir a una autoridad"), ("liderar", "guiar a un grupo"), ("comunidad", "grupo de personas con algo en común")],
    worked=[
        {"title": "Un derecho", "problem": f"{CAFFARENA} ¿En qué año pudieron votar las mujeres en todas las elecciones?", "steps": ["Busco el voto en el texto.", "Dice 1949."], "answer": "1949"},
        {"title": "Pensar quién falta", "problem": "Un libro habla de cinco hombres que fundaron una ciudad y no habla de ninguna mujer. ¿Qué pregunta conviene hacer?", "steps": ["Pregunto quiénes no aparecen.", "Busco si hubo mujeres que participaron."], "answer": "¿Qué mujeres participaron y no se nombraron?"},
    ],
    mistakes=[
        {"wrong": "Creer que si no aparece en el libro, no participó.", "why": "Se confía solo en lo escrito.", "fix": "Pregunta quién faltó y busca otras fuentes."},
        {"wrong": "Pensar que los derechos siempre existieron.", "why": "Se vive el presente sin mirar el pasado.", "fix": "Mira las fechas: el voto de las mujeres se logró en 1934 y en 1949."},
    ],
    tiers={
        "recovery": [
            ex(f"{DIAZ} ¿En qué año se recibió de médica Eloísa Díaz?", "1887", "Lo dice el texto."),
            ex(f"{CAFFARENA} ¿En qué año nació Elena Caffarena?", "1903", "Aparece en la primera frase."),
            ex("Lautaro fue un líder mapuche del siglo XVI y murió en 1557. ¿En qué año murió?", "1557", "Es el año dado."),
        ],
        "understand": [
            ex("¿Qué significa que una persona fue invisibilizada?", "Que su aporte casi no se contaba", "Casi no se la nombraba."),
            ex("¿Qué es un derecho?", "Algo que una persona puede hacer o tener por justicia", "Por ejemplo, votar."),
            ex(f"{CAFFARENA} ¿Qué defendía el MEMCh?", "Los derechos de las mujeres", "Así lo dice el texto."),
        ],
        "apply": [
            arith(f"{CAFFARENA} ¿Cuántos años pasaron entre la fundación del MEMCh (1935) y el voto de las mujeres en todas las elecciones (1949)?", "1949-1935", "Se resta un año al otro."),
            ex("Años: Díaz se recibió en 1887, el MEMCh se fundó en 1935, las mujeres votaron en todas las elecciones en 1949. Ordena de más antiguo a más nuevo.", "se recibió Díaz, se fundó el MEMCh, votaron las mujeres", "Se ordenan por año: 1887, 1935 y 1949."),
            ex("Hubo mujeres que votaron en elecciones de municipalidades en 1934. ¿Es antes o después del voto en todas las elecciones de 1949?", "antes", "1934 es menor que 1949."),
        ],
        "reason": [
            ex("Un libro de historia nombra solo a hombres. ¿Qué pregunta ayuda a encontrar a las personas que faltan?", "¿Qué mujeres y comunidades participaron?", "La pregunta busca a los ausentes."),
            ex(f"{DIAZ} Eloísa Díaz cuidó a niñas y niños en las escuelas. ¿Por qué ese aporte merece ser recordado?", "Porque mejoró la salud de muchos niños", "Ayudó a mucha gente."),
        ],
        "challenge": [
            arith(f"{DIAZ} Si Eloísa Díaz nació en 1866 y se recibió de médica en 1887, ¿cuántos años tenía al recibirse?", "1887-1866", "Se resta el año de nacimiento al año en que se recibió."),
            ex("Lautaro vivió en el siglo XVI y murió en 1557. Eloísa Díaz se recibió en 1887. ¿Cuál es más antiguo?", "Lautaro", "1557 es menor que 1887."),
        ],
    },
    context=[ex("La profesora lee un cuento sobre la fundación de una ciudad y no menciona a las mujeres. Un niño pregunta: «¿Y las mujeres no ayudaron?». ¿Qué hizo bien el niño?", "Preguntó quién faltaba", "Buscó a quienes no aparecían.")],
    selfcheck=[
        ex("¿Qué es votar?", "Elegir a una autoridad", "Es decidir con otros."),
        ex(f"{CAFFARENA} ¿En qué año se fundó el MEMCh?", "1935", "Aparece en la biografía."),
        ex("¿Qué pregunta sirve para buscar a quienes faltan en una historia?", "¿Quiénes no aparecen?", "Es la pregunta clave."),
    ],
    open_task=task("Elige a una de estas personas: Eloísa Díaz, Elena Caffarena o Lautaro. Escribe tres frases: quién fue, qué hizo y por qué su aporte importa. Usa los datos de las biografías de esta clase. Empieza con «Quiero contar que…».", "Quiero contar que Eloísa Díaz fue la primera mujer en recibirse de médica en Chile en 1887. Cuidó la salud de niñas y niños de las escuelas. Su aporte importa porque ayudó a muchos niños.", ["tres frases", "quién fue, qué hizo y por qué importa", "datos correctos de la biografía"], ["tres frases escritas"], ["inventar datos", "no explicar por qué importa"], "Pide que explique por qué esa persona casi no se nombraba."),
    reinforce="Pregunta a un adulto qué mujer admira y por qué.",
    extend="Escribe una pregunta para saber de otra mujer o comunidad que falte en un libro.",
)

register(
    OA7, 5,
    materials="Lápiz y papel. Las fichas de personas están escritas en los ejercicios y en la tarea.",
    use="Aprenderé a escribir un aporte con evidencia. Sirve para explicar por qué una persona ayudó a la sociedad y usar datos de una fuente.",
    prior=["Sé sacar información de una biografía.", "Sé qué es contribuir."],
    explain=[
        "Una biografía argumentada cuenta quién fue una persona, qué hizo y por qué su aporte importa, y lo prueba con datos. Un argumento tiene una idea y una prueba: «Alberto Hurtado ayudó a niños sin casa, porque fundó el Hogar de Cristo en 1944».",
        "La estructura es simple: primero el nombre y cuándo vivió; después qué hizo con un dato exacto; al final por qué ayudó a otros. Y siempre indica tu fuente: «Según la biografía».",
        "Aquí tienes tres fichas para practicar. Alberto Hurtado: fundó el Hogar de Cristo en 1944. Gabriela Mistral: recibió el Premio Nobel de Literatura en 1945. Pedro de Valdivia: fundó Santiago el 12 de febrero de 1541, en un valle donde ya vivían pueblos originarios. Una historia puede tener varias miradas: Valdivia es recordado como fundador, pero también hubo pueblos que ya vivían en el valle.",
    ],
    vocab=[("argumentar", "dar razones con pruebas"), ("evidencia", "dato o prueba que apoya una idea"), ("aporte", "lo que una persona da a la sociedad"), ("fundador", "persona que crea una ciudad o una institución"), ("pueblos originarios", "pueblos que ya vivían en este territorio antes de que llegaran los europeos")],
    worked=[
        {"title": "Idea y prueba", "problem": f"{HURTADO} Escribe una frase con idea y prueba sobre su aporte.", "steps": ["Idea: ayudó a personas sin casa.", "Prueba: fundó el Hogar de Cristo en 1944."], "answer": "Alberto Hurtado ayudó a personas sin casa, porque fundó el Hogar de Cristo en 1944"},
        {"title": "Dos miradas", "problem": f"{VALDIVIA} ¿Qué dos cosas dice el texto sobre el valle de Santiago?", "steps": ["Valdivia fundó la ciudad en 1541.", "Ya vivían pueblos originarios."], "answer": "Que Valdivia fundó Santiago y que ya vivían pueblos originarios"},
    ],
    mistakes=[
        {"wrong": "Decir «fue importante» sin dar un dato.", "why": "Se cree que basta con decirlo.", "fix": "Agrega una prueba: un año, un lugar o una acción."},
        {"wrong": "Contar solo la parte que me parece buena y olvidar otras miradas.", "why": "Se quiere admirar sin preguntar.", "fix": "Pregunta quiénes más estaban y qué opinaban."},
    ],
    tiers={
        "recovery": [
            ex(f"{HURTADO} ¿Qué fundó Alberto Hurtado en 1944?", "el Hogar de Cristo", "Es el hecho que dice la biografía."),
            ex(f"{VALDIVIA} ¿En qué fecha fundó Pedro de Valdivia la ciudad de Santiago?", "12 de febrero de 1541", "Es la fecha escrita."),
            ex(f"{MISTRAL} ¿Qué premio recibió Gabriela Mistral en 1945?", "el Premio Nobel de Literatura", "Está en la biografía."),
        ],
        "understand": [
            ex("¿Qué es argumentar?", "Dar razones con pruebas", "Una idea necesita una prueba."),
            ex("En Historia, ¿qué es una evidencia?", "Un dato o prueba que apoya una idea", "Por ejemplo, un año."),
            ex("¿Para qué decimos «según la biografía»?", "Para indicar de dónde viene el dato", "Se cita la fuente."),
        ],
        "apply": [
            ex(f"{MISTRAL} Completa: «Gabriela Mistral contribuyó a la cultura, porque en 1945 ___».", "recibió el Premio Nobel de Literatura", "Es la prueba del aporte."),
            ex(f"{HURTADO} Completa: «Alberto Hurtado ayudó a personas sin casa, porque en ___ fundó el Hogar de Cristo».", "1944", "Es el año de la biografía."),
            arith(f"{VALDIVIA} Valdivia fundó Santiago en 1541. ¿Cuántos años pasaron hasta 1810? (año de la Primera Junta)", "1810-1541", "Se resta un año al otro."),
        ],
        "reason": [
            ex("Un niño escribió: «Mistral fue muy importante». ¿Qué le falta a su frase?", "Una prueba o dato", "Una idea necesita evidencia."),
            ex(f"{VALDIVIA} ¿Por qué no basta decir «Valdivia fundó Santiago» sin mencionar a los pueblos que ya vivían ahí?", "Porque falta otra mirada de la historia", "Hay más personas en el relato."),
        ],
        "challenge": [
            ex(f"{AHRENS} Escribe una frase con idea y prueba sobre Marlene Ahrens.", "Marlene Ahrens contribuyó al deporte chileno, porque ganó la medalla de plata en 1956", "Incluye la idea y el dato del año."),
            ex("Ordena las partes de una biografía: A) por qué ayudó a otros, B) quién fue, C) qué hizo con un dato exacto.", "B, C, A", "Primero quién fue, luego qué hizo y al final por qué ayudó."),
        ],
    },
    context=[ex("Camila quiere presentar a Violeta Parra en el curso. Tiene tres datos: nació en 1917, recogió canciones del campo y murió en 1967. ¿Cuál de ellos prueba su aporte a la música?", "Recogió canciones del campo", "Es lo que hizo por la música.")],
    selfcheck=[
        ex("¿Qué dos partes tiene un argumento?", "Una idea y una prueba", "La prueba apoya la idea."),
        ex("¿Se debe indicar la fuente?", "Sí", "Para saber de dónde sale el dato."),
        ex(f"{HURTADO} ¿En qué año murió Hurtado?", "1952", "Está en la biografía."),
    ],
    open_task=task("Elige a una de estas personas y escribe tres frases con la forma quién fue, qué hizo y por qué importa. Fichas: (a) Alberto Hurtado: fundó el Hogar de Cristo en 1944; (b) Gabriela Mistral: publicó «Ternura» en 1924 y recibió el Premio Nobel en 1945; (c) Marlene Ahrens: ganó la medalla de plata en 1956. Termina con «Fuente: la ficha de la clase».", "Alberto Hurtado fue un sacerdote chileno. En 1944 fundó el Hogar de Cristo para ayudar a niños y a personas sin casa. Su aporte importa porque ayudó a muchas personas. Fuente: la ficha de la clase.", ["tres frases", "idea y prueba", "fuente al final"], ["biografía de tres frases con fuente"], ["inventar datos", "no dar prueba"], "Pide que explique cuál es el dato que prueba el aporte."),
    reinforce="Cuenta a alguien de tu casa por qué esa persona ayudó a la sociedad.",
    extend="Agrega una cuarta frase con una pregunta sobre la persona que todavía no sabes responder.",
)

# ---------------------------------------------------------------- OA 08
register(
    OA8, 1,
    materials="Lápiz y papel. Los dibujos están descritos con palabras en cada ejercicio; puedes mirar tu sala o tu pieza.",
    use="Aprenderé la diferencia entre un lugar real y su dibujo, y que un plano o un mapa es una forma de representarlo. Sirve para entender dónde estamos.",
    prior=["Sé dibujar objetos.", "Sé nombrar lugares de mi casa."],
    explain=[
        "Un lugar es un espacio real donde estamos, como tu sala. Una representación es un dibujo, un plano o un mapa que muestra ese lugar. La representación no es el lugar: es una forma de mostrarlo.",
        "Un plano muestra un lugar pequeño, como una sala, una casa o una escuela, visto desde arriba. Un mapa muestra un lugar más grande, como Chile o el mundo. Los dos usan dibujos pequeños y símbolos en lugar de cosas reales.",
        "En una representación todo se hace más chico y se deja solo lo importante. Por ejemplo, un plano de tu sala puede mostrar la puerta, la pizarra y las mesas, pero no los lápices. Por eso un plano ayuda a ubicarse, pero no muestra todo.",
    ],
    vocab=[("lugar", "espacio donde estamos"), ("plano", "dibujo de un lugar pequeño visto desde arriba"), ("mapa", "dibujo de un lugar grande visto desde arriba"), ("representar", "mostrar algo con un dibujo o un símbolo"), ("símbolo", "dibujo simple que representa algo")],
    worked=[
        {"title": "Plano o mapa", "problem": "Un dibujo muestra tu casa con sus piezas vistas desde arriba. ¿Es un plano o un mapa?", "steps": ["Una casa es un lugar pequeño.", "Un dibujo de un lugar pequeño visto desde arriba es un plano."], "answer": "Un plano"},
        {"title": "Real o dibujo", "problem": "La mesa de tu sala y el dibujo de la mesa en el plano, ¿son lo mismo?", "steps": ["La mesa real se toca y tiene tamaño grande.", "El dibujo es chico y solo la representa."], "answer": "No; el dibujo representa la mesa real"},
    ],
    mistakes=[
        {"wrong": "Pensar que el dibujo es igual de grande que el lugar.", "why": "Se mira el dibujo como si fuera el lugar.", "fix": "Recuerda: una representación hace todo más pequeño."},
        {"wrong": "Esperar que el plano muestre absolutamente todo.", "why": "Se piensa que dibujar es copiar todo.", "fix": "Un plano deja solo lo importante."},
    ],
    tiers={
        "recovery": [
            ex("Un dibujo que muestra tu sala vista desde arriba, ¿es un plano o un mapa del mundo?", "un plano", "Una sala es un lugar pequeño."),
            ex("¿Un mapa de Chile muestra un lugar pequeño o uno grande?", "uno grande", "Chile es un país."),
            ex("¿El dibujo de una mesa es la mesa real?", "No", "Solo la representa."),
        ],
        "understand": [
            ex("¿Qué es un plano?", "Un dibujo de un lugar pequeño visto desde arriba", "Sirve para ubicarse."),
            ex("¿Qué es un símbolo?", "Un dibujo simple que representa algo", "Reemplaza a la cosa real."),
            ex("¿Por qué un plano no muestra todos los lápices de la sala?", "Porque deja solo lo importante", "Mostrar todo lo haría confuso."),
        ],
        "apply": [
            ex("Plano de una sala: puerta abajo, pizarra arriba, tres mesas en el medio. ¿Qué hay arriba del plano?", "la pizarra", "Así está en la descripción."),
            ex("Plano de una sala: puerta abajo, pizarra arriba, tres mesas en el medio. ¿Cuántas mesas hay?", "3", "El plano dice tres mesas."),
            ex("Plano de una casa: cocina a la izquierda, dormitorio a la derecha, baño arriba. ¿Dónde está el dormitorio?", "a la derecha", "Así lo muestra el plano."),
        ],
        "reason": [
            ex("Un niño dice que el plano de su sala mide lo mismo que su sala. ¿Es cierto?", "No; el plano es mucho más chico", "Representar es mostrar en pequeño."),
            ex("Una niña dice que el mapa de Chile y el plano de su pieza sirven para lo mismo. ¿Es correcto?", "No; el mapa muestra un lugar grande y el plano uno pequeño", "Cambia el tamaño del lugar."),
        ],
        "challenge": [
            ex("Tres dibujos: A) vista desde arriba de una pieza, B) vista de frente de una casa, C) vista desde arriba de Chile. ¿Cuáles son representaciones desde arriba?", "A y C", "El dibujo B es de frente."),
            ex("De las tres representaciones anteriores, ¿cuál es un plano?", "A", "Muestra un lugar pequeño desde arriba."),
        ],
    },
    context=[ex("Para llegar al baño de una escuela nueva, una niña ve un dibujo con la entrada, el patio y el baño a la derecha del patio. ¿Qué tipo de representación usa?", "un plano", "Muestra un lugar pequeño.")],
    selfcheck=[
        ex("¿Qué es representar?", "Mostrar algo con un dibujo o un símbolo", "Se usa en planos y mapas."),
        ex("¿Un mapa es el lugar real?", "No", "Solo lo representa."),
        ex("¿Un plano muestra un lugar grande o pequeño?", "pequeño", "Por ejemplo, una sala."),
    ],
    open_task=task("Dibuja un plano muy simple de tu pieza o de tu sala visto desde arriba. Usa un rectángulo para el lugar y dibuja cuatro objetos con símbolos simples. Elige entre: cama, mesa, silla, puerta, ventana, pizarra. Escribe el nombre de cada objeto.", "Rectángulo grande. Dentro: cama (rectángulo), mesa (cuadrado), puerta (línea) y ventana (línea doble). Cada uno con su nombre.", ["rectángulo del lugar", "cuatro objetos con símbolos", "nombres escritos"], ["plano dibujado"], ["dibujar los objetos de frente", "no escribir los nombres"], "Pide que cuente qué objeto es lo más importante en su plano."),
    reinforce="Mira tu pieza y señala dónde quedaría la puerta en un dibujo desde arriba.",
    extend="Dibuja el plano de otra habitación de tu casa.",
)

register(
    OA8, 2,
    materials="Lápiz y papel. Los objetos y su vista desde arriba están descritos en cada ejercicio; puedes mirar un vaso, un libro y una pelota.",
    use="Aprenderé a imaginar cómo se ven los objetos desde arriba y a dibujarlos en un plano. Sirve para construir mis propios planos.",
    prior=["Sé qué es un plano.", "Sé reconocer círculos, cuadrados y rectángulos."],
    explain=[
        "Un plano muestra los lugares vistos desde arriba, como si fueras un pájaro mirando hacia abajo. Por eso los objetos cambian de forma. Un vaso redondo visto desde arriba se ve como un círculo. Un libro se ve como un rectángulo.",
        "Una mesa rectangular se ve como un rectángulo. Una mesa redonda se ve como un círculo. Una pelota desde cualquier lado se ve como un círculo. Una silla vista desde arriba se ve como un cuadrado, con el respaldo en un borde.",
        "Para dibujar un plano, primero marca los bordes del lugar. Luego dibuja cada objeto desde arriba, en su posición: lo que está cerca de la puerta, cerca de la puerta; lo que está en el fondo, en el fondo. Mantén los objetos en el mismo orden que en el lugar real.",
    ],
    vocab=[("vista desde arriba", "forma de mirar como un pájaro que vuela"), ("círculo", "figura redonda"), ("rectángulo", "figura con cuatro lados, dos largos y dos cortos"), ("posición", "lugar donde está un objeto"), ("borde", "límite de un lugar o un objeto")],
    worked=[
        {"title": "Forma desde arriba", "problem": "¿Cómo se ve un vaso redondo desde arriba?", "steps": ["Miro la boca del vaso desde arriba.", "Es redonda."], "answer": "Como un círculo"},
        {"title": "Ubicar un objeto", "problem": "La pizarra está al fondo de la sala y la puerta está abajo. En el plano, ¿dónde va la pizarra?", "steps": ["La puerta está abajo.", "El fondo es lo contrario: arriba."], "answer": "Arriba en el plano"},
    ],
    mistakes=[
        {"wrong": "Dibujar los objetos de frente, como un dibujo de una casa.", "why": "Se dibuja como se ve normalmente.", "fix": "Imagina que miras desde el techo hacia abajo."},
        {"wrong": "Poner los objetos en lugares distintos a los reales.", "why": "No se mira cómo está el lugar.", "fix": "Revisa cada posición: ¿cerca de la puerta o en el fondo?"},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se ve una pelota desde arriba: círculo o rectángulo?", "círculo", "Una pelota es redonda por todos lados."),
            ex("¿Cómo se ve un libro cerrado desde arriba?", "un rectángulo", "Tiene cuatro lados."),
            ex("¿Cómo se ve la boca de un vaso desde arriba?", "un círculo", "La boca del vaso es redonda."),
        ],
        "understand": [
            ex("¿Qué es la vista desde arriba?", "Mirar como un pájaro que vuela", "Se ve el lugar hacia abajo."),
            ex("¿Por qué cambian las formas al mirar desde arriba?", "Porque se ve la parte de arriba", "Se pierde el frente."),
            ex("¿Cómo se ve una mesa redonda desde arriba?", "un círculo", "Una mesa redonda tiene forma de círculo."),
        ],
        "apply": [
            ex("En una sala, la puerta está abajo y la pizarra arriba. ¿Dónde pones la pizarra en el plano?", "arriba", "Es el lado opuesto a la puerta."),
            ex("En una pieza, la cama está a la izquierda y la ventana a la derecha. ¿Dónde dibujas la cama en el plano?", "a la izquierda", "Se respeta la posición real."),
            ex("En una cocina, la mesa redonda está al centro. ¿Qué figura dibujas y dónde?", "un círculo al centro", "Mesa redonda: círculo; centro: al medio."),
        ],
        "reason": [
            ex("Una niña dibujó una mesa de frente en su plano. ¿Qué debe cambiar?", "Dibujarla como se ve desde arriba", "El plano usa la vista desde arriba."),
            ex("En el plano de una sala la puerta está a la derecha, pero en la sala real está a la izquierda. ¿Qué pasó?", "El plano está mal hecho", "No respeta la posición real."),
        ],
        "challenge": [
            ex("Una sala tiene: 4 mesas rectangulares, 1 mesa redonda y 1 pizarra. En el plano, ¿cuántos rectángulos hay si la pizarra también se dibuja como rectángulo?", "5", "4 mesas + 1 pizarra = 5 rectángulos."),
            ex("Un objeto visto desde arriba es un círculo pequeño y está al lado de un rectángulo grande con el título «mesa». ¿Qué objeto podría ser el círculo?", "un vaso o un plato sobre la mesa", "Son objetos redondos."),
        ],
    },
    context=[ex("Beto está sentado en su pieza. Ve su cama a la izquierda, la ventana al frente y la puerta a la derecha. Para su plano, la ventana la pone arriba. ¿Dónde pone la puerta?", "a la derecha", "Se mantiene la posición real.")],
    selfcheck=[
        ex("¿Qué forma tiene una pelota desde arriba?", "un círculo", "Una pelota es redonda por todos lados."),
        ex("¿Dibujamos de frente o desde arriba en un plano?", "desde arriba", "Así se hace un plano."),
        ex("Si la puerta está a la derecha en la sala real, ¿dónde va en el plano?", "a la derecha", "Se respeta la posición."),
    ],
    open_task=task("Dibuja un plano de esta sala imaginaria: un rectángulo grande; la puerta abajo a la derecha; la pizarra arriba al centro; dos mesas rectangulares en el medio; una mesa redonda a la izquierda. Escribe el nombre de cada objeto.", "Rectángulo grande. Puerta abajo a la derecha. Pizarra rectángulo arriba al centro. Dos rectángulos en el medio (mesas). Un círculo a la izquierda (mesa redonda).", ["lugar y cinco objetos", "figuras vistas desde arriba", "posiciones correctas"], ["plano dibujado con nombres"], ["dibujar de frente", "cambiar la posición de la puerta"], "Pide que señale con el dedo dónde está cada objeto."),
    reinforce="Mira tu mesa desde arriba y dibuja su forma.",
    extend="Dibuja el plano de tu cuarto con cuatro objetos reales y su posición.",
)

register(
    OA8, 3,
    materials="Lápiz y papel. Los mapas y la leyenda están escritos con palabras y letras en cada ejercicio.",
    use="Aprenderé a interpretar símbolos y una leyenda en un plano o mapa. Sirve para leer cualquier plano, como el de un parque o una ciudad.",
    prior=["Sé qué es un plano.", "Sé qué es un símbolo."],
    explain=[
        "Un plano o mapa usa símbolos. Cada símbolo es un dibujo o una letra que representa algo real. La leyenda es una lista que explica qué significa cada símbolo. Sin leyenda no podemos estar seguros de qué quiere decir.",
        "Ejemplo de un plano de parque en cuadrícula (filas 1, 2 y 3; columnas A, B, C y D). Leyenda: R es árbol, B es banca, J es juegos, F es fuente. Fila 1: A1 = R, C1 = J. Fila 2: B2 = B, D2 = F. Fila 3: A3 = R, D3 = R.",
        "Para leer, busca el símbolo en la leyenda y luego ubica la casilla. Una casilla es un cuadro formado por la letra de la columna y el número de la fila. Así podemos decir: «La fuente está en D2».",
    ],
    vocab=[("leyenda", "lista que explica los símbolos de un mapa o plano"), ("cuadrícula", "red de cuadros con letras y números"), ("casilla", "cada cuadro de la cuadrícula"), ("fila", "línea horizontal de casillas"), ("columna", "línea vertical de casillas")],
    worked=[
        {"title": "Buscar en la leyenda", "problem": "Leyenda: R es árbol, B es banca, J es juegos, F es fuente. ¿Qué es la letra J?", "steps": ["Busco J en la leyenda.", "Dice juegos."], "answer": "Juegos"},
        {"title": "Ubicar una casilla", "problem": "Plano: A1 = R, C1 = J, B2 = B, D2 = F, A3 = R, D3 = R. ¿Dónde está la fuente?", "steps": ["La fuente es F.", "F está en D2."], "answer": "En D2"},
    ],
    mistakes=[
        {"wrong": "Adivinar qué significa un símbolo sin mirar la leyenda.", "why": "Se piensa que se entiende solo.", "fix": "Busca siempre el símbolo en la leyenda."},
        {"wrong": "Confundir columna y fila.", "why": "Las dos son líneas del plano.", "fix": "La letra va con la columna (vertical) y el número con la fila (horizontal)."},
    ],
    tiers={
        "recovery": [
            ex("Leyenda: R es árbol, B es banca, J es juegos, F es fuente. ¿Qué significa B?", "banca", "La leyenda lo dice."),
            ex("Plano del parque: A1 = R, C1 = J, B2 = B, D2 = F, A3 = R, D3 = R. ¿Qué hay en C1?", "juegos", "J significa juegos."),
            ex("¿Qué es una leyenda?", "Una lista que explica los símbolos", "Dice qué significa cada uno."),
        ],
        "understand": [
            ex("Plano: A1 = R, C1 = J, B2 = B, D2 = F, A3 = R, D3 = R. ¿Cuántos árboles hay si R significa árbol?", "3", "Hay R en A1, A3 y D3."),
            ex("¿Por qué sirve la leyenda?", "Porque explica los símbolos", "Sin ella no se sabe qué son."),
            ex("En la casilla D2, ¿la D es columna o fila?", "columna", "Las letras indican columna."),
        ],
        "apply": [
            ex("Plano: A1 = R, C1 = J, B2 = B, D2 = F, A3 = R, D3 = R. ¿En qué casilla está la banca?", "B2", "La B está en esa casilla."),
            ex("Mismo plano. ¿En qué casilla están los juegos?", "C1", "La J está en C1."),
            ex("Mismo plano. ¿Cuál casilla tiene un árbol: A1 o B2?", "A1", "R está en A1."),
        ],
        "reason": [
            ex("Un niño dice que la F es una fuente porque suena parecido, pero no mira la leyenda. ¿Es una buena forma de leer?", "No; debe mirar la leyenda", "La leyenda es la prueba."),
            ex("Mismo plano. Lola dice que la fuente está en la fila 3. ¿Tiene razón?", "No; está en la fila 2", "F está en D2."),
        ],
        "challenge": [
            ex("Mismo plano. Si caminas desde A1 hasta D3, ¿qué dos columnas distintas cruzas, aparte de A y D?", "B y C", "Las columnas entre A y D son B y C."),
            ex("Mismo plano. ¿Cuántos símbolos distintos hay: R, J, B, F?", "4", "Cada letra es un símbolo distinto."),
        ],
    },
    context=[ex("Una familia mira el plano de un parque: R es árbol, B es banca, J es juegos y F es fuente. Quieren sentarse. ¿Qué símbolo deben buscar?", "B", "Una banca sirve para sentarse.")],
    selfcheck=[
        ex("¿Qué es una casilla?", "Un cuadro de la cuadrícula", "Se nombra con letra y número."),
        ex("¿Qué símbolo representa una fuente en la leyenda del parque?", "F", "La leyenda dice F es fuente."),
        ex("¿La letra de una casilla indica columna o fila?", "columna", "Así lo vimos en la clase."),
    ],
    open_task=task("Dibuja una cuadrícula de 3 filas y 4 columnas (A, B, C y D). Pon estos símbolos: R (árbol) en A1, B (banca) en B2, J (juegos) en C1 y F (fuente) en D2. Escribe la leyenda debajo. Luego escribe en qué casilla está la fuente.", "Cuadrícula con R en A1, B en B2, J en C1, F en D2. Leyenda: R árbol, B banca, J juegos, F fuente. La fuente está en D2.", ["cuadrícula completa", "símbolos en las casillas", "leyenda y ubicación de la fuente"], ["cuadrícula dibujada y leyenda"], ["poner símbolos en casillas equivocadas", "olvidar la leyenda"], "Pide que explique cómo se llama cada casilla."),
    reinforce="Inventa un símbolo para una piscina y agrégalo a la leyenda.",
    extend="Haz un plano de tu escuela con una leyenda de cinco símbolos.",
)

register(
    OA8, 4,
    materials="Lápiz y papel. El plano de la escuela está descrito con casillas en cada ejercicio.",
    use="Aprenderé a representar y seguir un recorrido en un plano y a explicar sus límites. Sirve para llegar a un lugar y para saber qué no muestra un plano.",
    prior=["Sé leer una cuadrícula con letras y números.", "Sé usar derecha, izquierda, arriba y abajo."],
    explain=[
        "Un recorrido es el camino de un lugar a otro. En un plano en cuadrícula, se escribe con pasos: «avanza 2 casillas a la derecha» o «baja 1 casilla». Así otra persona puede seguir tu recorrido sin verte.",
        "Plano de una escuela: columnas A, B, C y D; filas 1, 2 y 3. Puerta de entrada en A3, patio en B2, sala en C1 y baño en D3. Para ir de la entrada (A3) a la sala (C1): sube 2 casillas hasta A1 y avanza 2 casillas a la derecha hasta C1.",
        "Un plano ayuda mucho, pero tiene límites. No muestra el tamaño real, ni quién está en cada lugar, ni si hay ruido o barro. Para llegar bien, el plano y mirar el lugar real se completan.",
    ],
    vocab=[("recorrido", "camino de un lugar a otro"), ("casilla", "cada cuadro de la cuadrícula"), ("límite", "lo que algo no puede mostrar o hacer"), ("instrucción", "paso que dice qué hacer"), ("entrada", "lugar por donde se entra")],
    worked=[
        {"title": "Seguir un recorrido", "problem": "Estás en A3. Sube 2 casillas y avanza 2 a la derecha. ¿A qué casilla llegas?", "steps": ["Subir 2 desde A3 es llegar a A1.", "Avanzar 2 a la derecha desde A1 es llegar a C1."], "answer": "C1"},
        {"title": "Un límite del plano", "problem": "El plano muestra el patio en B2. ¿Muestra si hoy hay mucho barro?", "steps": ["Un plano muestra posiciones fijas.", "No muestra cómo está el lugar hoy."], "answer": "No lo muestra"},
    ],
    mistakes=[
        {"wrong": "Dar un recorrido sin decir cuántas casillas.", "why": "Se da por sabido el número.", "fix": "Escribe cuántas casillas y hacia dónde."},
        {"wrong": "Creer que el plano muestra todo lo que hay en el lugar.", "why": "Se piensa que dibuja todo.", "fix": "Un plano deja solo lo importante."},
    ],
    tiers={
        "recovery": [
            ex("Plano de la escuela: entrada A3, patio B2, sala C1, baño D3. ¿En qué casilla está la sala?", "C1", "Así lo dice el plano."),
            ex("Plano de la escuela: entrada A3, patio B2, sala C1, baño D3. ¿Dónde está el baño?", "D3", "Así lo dice el plano."),
            ex("¿Qué es un recorrido?", "El camino de un lugar a otro", "Se hace paso a paso."),
        ],
        "understand": [
            ex("¿Por qué se escriben los recorridos con pasos?", "Para que otro pueda seguirlos", "Cada paso dice qué hacer."),
            ex("¿Un plano muestra si hay ruido en el lugar?", "No", "Es un límite del plano."),
            ex("¿Para qué sirve mirar también el lugar real, además del plano?", "Para ver lo que el plano no muestra", "Los dos se completan entre sí."),
        ],
        "apply": [
            ex("Plano: entrada A3, patio B2, sala C1, baño D3. Estás en A3. Avanza 1 a la derecha y sube 1. ¿A qué casilla llegas?", "B2", "A3 a la derecha es B3; subir 1 es B2."),
            ex("Mismo plano. Estás en B2. Avanza 2 a la derecha y baja 1. ¿A qué casilla llegas?", "D3", "B2 a la derecha 2 es D2; bajar 1 es D3."),
            ex("Mismo plano. Estás en C1. Baja 2 casillas. ¿A qué casilla llegas?", "C3", "C1 hacia abajo 2 es C3."),
        ],
        "reason": [
            ex("Un niño dice que con el plano no hace falta mirar el patio. ¿Tiene razón?", "No; el plano no muestra todo", "Hay cosas que solo se ven en el lugar."),
            ex("El plano muestra que el baño está en D3, pero está cerrado hoy. ¿Lo muestra el plano?", "No", "El plano no cambia con el día."),
        ],
        "challenge": [
            ex("Escribe un recorrido para ir de la entrada (A3) al baño (D3).", "Avanza 3 casillas a la derecha", "A3, B3, C3 y D3 están en la fila 3."),
            ex("Mismo plano. Escribe un recorrido de la sala (C1) al patio (B2).", "Baja 1 casilla y avanza 1 a la izquierda", "C1 a C2 y luego B2."),
        ],
    },
    context=[ex("Un niño nuevo llega a la entrada (A3) y debe llegar a la sala (C1). La profesora le da un papel con el plano. ¿Qué recorrido escribe ella?", "Sube 2 casillas y avanza 2 a la derecha", "A3 a A1 y luego C1.")],
    selfcheck=[
        ex("¿Qué es una instrucción de un recorrido?", "Un paso que dice qué hacer", "Por ejemplo: avanza 2 casillas."),
        ex("Plano de la escuela: entrada A3, patio B2, sala C1, baño D3. ¿Dónde está el patio?", "B2", "Así lo dice el plano."),
        ex("¿Un plano muestra todo lo que hay en un lugar?", "No", "Deja solo lo importante."),
    ],
    open_task=task("Con el plano de la escuela que está en la clase (entrada A3, patio B2, sala C1, baño D3), escribe un recorrido de la entrada (A3) al baño (D3) en una frase. Luego escribe un límite del plano: algo que el plano no te dice del lugar real. Opciones de límite: si hay ruido, si el piso está mojado, cuántos niños hay.", "Recorrido: avanza 3 casillas a la derecha. Límite: el plano no dice si el piso está mojado.", ["recorrido con pasos y números", "una casilla de llegada correcta", "un límite del plano"], ["frase de recorrido y frase de límite"], ["no decir cuántas casillas", "no escribir ningún límite"], "Pide que dibuje el recorrido con una flecha sobre el plano."),
    reinforce="Escribe cómo llegar de tu cama a la puerta de tu pieza en tres pasos.",
    extend="Dibuja un plano de tu cuadra con cinco lugares y una leyenda.",
)
