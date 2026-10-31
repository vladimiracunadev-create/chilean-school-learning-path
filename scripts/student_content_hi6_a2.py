"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 02 (desarrollo del proceso de independencia de Chile)."""
from __future__ import annotations

from hi5_lib import build

OA2 = "HI06 OA 02"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 5 (cronología de la independencia de Chile, hecha para este cuaderno). "
     "18 de septiembre de 1810: en un cabildo abierto en Santiago se forma la Primera Junta Nacional de Gobierno, presidida por Mateo de Toro y Zambrano; la junta dice gobernar en nombre del rey Fernando VII. "
     "1811: se elige el primer Congreso Nacional, que se instala en julio. "
     "1-2 de octubre de 1814: batalla de Rancagua, victoria de las fuerzas del rey; comienza la Reconquista española (1814-1817). "
     "12 de febrero de 1817: batalla de Chacabuco, victoria patriota del ejército de los Andes. "
     "12 de febrero de 1818: se proclama la independencia de Chile. "
     "5 de abril de 1818: batalla de Maipú, victoria patriota que asegura la independencia.")
build(
    OA2, 1, F,
    use="Aprenderé a ordenar los hechos principales de la independencia de Chile en una línea de tiempo. Sirve para no confundir cuándo ocurrió cada uno.",
    prior=["Sé que Chile fue colonia de España y que en 1808 el rey dejó el trono.", "Sé leer fechas y restar años.", "Sé la diferencia entre patriotas y realistas."],
    explain=[
        "La independencia de Chile no fue un solo día, sino un proceso que duró varios años. Comenzó el 18 de septiembre de 1810, cuando un cabildo abierto reunió en Santiago a vecinos importantes y formó la Primera Junta Nacional de Gobierno. Un cabildo abierto es una reunión de los vecinos principales para tomar decisiones.",
        "En 1811 se eligió el primer Congreso Nacional. Después vinieron las guerras. En la batalla de Rancagua, en 1814, ganaron las fuerzas del rey y comenzó la Reconquista, un período en que el gobierno español volvió a mandar en Chile hasta 1817.",
        "En 1817 el ejército de los Andes, organizado por San Martín, cruzó la cordillera y ganó en Chacabuco. El 12 de febrero de 1818 se proclamó la independencia, y el 5 de abril de 1818 la victoria de Maipú la aseguró. Los historiadores dividen este proceso en tres etapas: Patria Vieja (1810-1814), Reconquista (1814-1817) y Patria Nueva (1817-1823).",
    ],
    vocab=[("cabildo abierto", "reunión de los vecinos importantes de una ciudad para tomar decisiones"), ("junta", "grupo de personas que gobierna"), ("Reconquista", "período en que los españoles volvieron a gobernar Chile (1814-1817)"), ("proclamar", "anunciar algo oficialmente"), ("Congreso Nacional", "reunión de representantes elegidos para hacer leyes")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuánto duró la Reconquista según los años de la ficha?", ["La ficha indica que fue de 1814 a 1817.", "Resto: 1817 − 1814 = 3."], "3 años"),
        ("Ordenar dos hechos", "{F} ¿Qué ocurrió primero: la batalla de Chacabuco o la proclamación de la independencia?", ["Chacabuco fue el 12 de febrero de 1817.", "La proclamación fue el 12 de febrero de 1818, un año después."], "Chacabuco"),
    ],
    mistakes=[("Creer que la independencia se logró el 18 de septiembre de 1810.", "Se confunde la formación de la Primera Junta con la proclamación de la independencia.", "El 18 de septiembre de 1810 se formó la junta; la independencia se proclamó el 12 de febrero de 1818."),
              ("Pensar que Rancagua fue una victoria patriota.", "Se mezcla con Chacabuco o Maipú.", "En Rancagua (1814) ganaron las fuerzas del rey; Chacabuco y Maipú fueron victorias patriotas.")],
    T=[
        ("{F} ¿Quién presidió la Primera Junta Nacional de Gobierno?", "Mateo de Toro y Zambrano", "La ficha lo indica."),
        ("{F} ¿En nombre de qué rey dijo gobernar la junta de 1810?", "Fernando VII", "La ficha lo dice."),
        ("{F} ¿Quién ganó la batalla de Rancagua?", "las fuerzas del rey", "La ficha habla de una victoria de las fuerzas del rey."),
        ("=", "{F} ¿Cuántos años pasaron entre la formación de la Primera Junta y la proclamación de la independencia?", "1818-1810", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué batalla ocurrió primero: Chacabuco o Maipú?", "Chacabuco", "Fue en 1817; Maipú, en 1818."),
        ("{F} ¿Cómo se llama el período 1814-1817 en que gobernaron nuevamente los españoles?", "la Reconquista", "La ficha lo define."),
        ("{F} Ordena de más antiguo a más reciente: Chacabuco, Rancagua, Primera Junta, proclamación de la independencia.", "Primera Junta, Rancagua, Chacabuco, proclamación de la independencia", "Los años son 1810, 1814, 1817 y 1818."),
        ("=", "{F} ¿Cuántos años pasaron entre la batalla de Rancagua y la batalla de Maipú?", "1818-1814", "Se restan los años de ambas batallas.", " años"),
        ("{F} Clasifica cada hecho como «victoria patriota» o «victoria del rey»: a) Rancagua; b) Chacabuco; c) Maipú.", "victoria del rey: a; victoria patriota: b y c", "La ficha las describe así."),
        ("{F} Un compañero dice: «Chile se declaró independiente en 1810». Corrígelo con la ficha.", "En 1810 se formó la junta; la independencia se proclamó el 12 de febrero de 1818", "Son dos hechos distintos."),
        ("{F} Una alumna dice: «Rancagua fue una victoria patriota que inició la independencia». ¿Qué error hay?", "Rancagua fue victoria del rey y dio inicio a la Reconquista", "La ficha lo indica."),
        ("{F} La Patria Vieja va de 1810 a 1814. ¿Qué hecho de la ficha marca su final?", "la batalla de Rancagua", "Después de ella empezó la Reconquista."),
        ("=", "{F} ¿Cuántos años pasaron entre la batalla de Chacabuco y la batalla de Maipú?", "1818-1817", "Se resta el año de Chacabuco al de Maipú.", " año"),
    ],
    ctx=("En una plaza hay una placa que dice «12 de febrero». ¿Qué dos hechos de la ficha ocurrieron en esa fecha y en qué años?", "la batalla de Chacabuco (1817) y la proclamación de la independencia (1818)", "La ficha da ambos hechos con ese día."),
    sc=[("¿Cómo se llaman las tres etapas de la independencia de Chile? Escribe sus nombres en orden.", "Patria Vieja, Reconquista y Patria Nueva", "Siguen el orden de los años."),
        ("{F} ¿En qué mes y año fue la batalla de Maipú?", "abril de 1818", "La ficha da 5 de abril de 1818."),
        ("{F} ¿Qué es un cabildo abierto?", "una reunión de los vecinos importantes de una ciudad para tomar decisiones", "La ficha lo muestra y la clase lo define.")],
    op=("Dibuja una línea de tiempo de 1810 a 1818. Marca los seis hechos de la ficha con su fecha y pinta de verde los hechos favorables a los patriotas y de rojo los favorables al rey. Pinta de azul las fechas de formación de gobierno o de proclamación. {F}",
        "Junta (azul, 1810), Congreso (azul, 1811), Rancagua (rojo, 1814), Chacabuco (verde, 1817), proclamación (azul, 1818), Maipú (verde, 1818).",
        ["seis hechos ordenados", "colores bien usados", "fechas completas"], ["línea de tiempo coloreada"], ["pintar Rancagua de verde", "poner Maipú antes que Chacabuco"],
        "Pide que cuente en voz alta cuántos años hubo entre la junta y la proclamación."),
    reinforce="Repite en voz alta las tres etapas de la independencia y un hecho de cada una.",
    extend="Escribe una pregunta sobre qué pasó en Chile entre la batalla de Rancagua y la batalla de Chacabuco.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 6 (fuentes inventadas para este cuaderno, basadas en hechos conocidos). "
     "Fuente A, proclama de la Primera Junta, 1810: «Gobernamos en nombre del rey Fernando VII mientras él no pueda hacerlo». "
     "Fuente B, número del periódico «Aurora de Chile», 1812: el fraile Camilo Henríquez escribe que el pueblo tiene derecho a gobernarse. "
     "Fuente C, carta de un oficial del ejército del rey, 1814, desde Rancagua: cuenta cómo avanzaron sus tropas contra los patriotas. "
     "Fuente D, relato escrito en 1900 por un historiador sobre la batalla de Maipú, a partir de documentos de la época.")
build(
    OA2, 2, F,
    use="Aprenderé a leer fuentes de la independencia de Chile preguntando quién las escribió, cuándo y para qué. Sirve para saber qué podemos concluir de cada una.",
    prior=["Sé la diferencia entre fuente primaria y secundaria.", "Sé qué fueron la Patria Vieja y la Reconquista.", "Sé que cada autor tiene un punto de vista."],
    explain=[
        "En la independencia de Chile hubo muchos tipos de fuentes: proclamas, periódicos, cartas y relatos de historiadores. Una proclama es un anuncio público de un gobierno. Un periódico informa y también defiende ideas. Una carta cuenta lo que vio una persona. Cada una se creó con un propósito diferente.",
        "La fuente A es primaria y muestra que en 1810 la junta no pidió independencia: dijo gobernar en nombre del rey. La fuente B es primaria y defiende una idea, que el pueblo puede gobernarse, por eso sirve para conocer opiniones de los patriotas. La fuente C es primaria, pero la escribe un oficial del rey, así que cuenta la batalla desde su lado.",
        "La fuente D es secundaria porque se escribió mucho después, usando documentos. Sirve para tener una visión ordenada, pero hay que preguntar en qué documentos se apoya. Ninguna de estas fuentes cuenta lo que pensaron los pueblos indígenas ni la gente sin poder político. Por eso una conclusión necesita varias fuentes y debe ser prudente.",
    ],
    vocab=[("proclama", "anuncio público hecho por un gobierno o jefe"), ("periódico", "publicación que informa y opina sobre hechos del momento"), ("testigo", "persona que vio un hecho"), ("propósito", "razón por la que alguien crea una fuente"), ("conclusión", "idea final que se apoya en evidencia")],
    worked=[
        ("Reconocer el propósito", "{F} ¿Para qué crees que se escribió la fuente B?", ["Es un periódico, que informa y defiende ideas.", "El texto dice que el pueblo tiene derecho a gobernarse."], "Para defender la idea de que el pueblo puede gobernarse"),
        ("Usar una fuente como prueba", "{F} ¿Qué prueba muestra la fuente A sobre lo que la junta pedía en 1810?", ["La proclama dice que gobierna en nombre del rey Fernando VII.", "No habla de independencia."], "Que dijo gobernar en nombre del rey, no pidió independencia"),
    ],
    mistakes=[("Creer que la proclama de 1810 pedía independencia.", "Se lee la historia de 1818 en un texto de 1810.", "La fuente A muestra lealtad al rey en 1810."),
              ("Tratar la carta de un oficial del rey como si fuera neutral.", "No se pregunta desde qué lado habla.", "El oficial cuenta la batalla desde el lado del rey.")],
    T=[
        ("{F} ¿Quién escribe la fuente B?", "el fraile Camilo Henríquez", "La ficha lo indica."),
        ("{F} ¿En qué año se publicó la fuente B?", "1812", "La ficha da ese año."),
        ("{F} ¿A qué batalla se refiere la fuente C?", "a la de Rancagua", "La ficha dice que la carta es desde Rancagua."),
        ("{F} ¿Cuál de las fuentes de la ficha es secundaria?", "la fuente D", "La escribió un historiador en 1900."),
        ("{F} ¿Qué fuente muestra el punto de vista de un oficial del rey?", "la fuente C", "El autor es un oficial del ejército del rey."),
        ("=", "{F} ¿Cuántos años pasaron entre la fuente A y la fuente B?", "1812-1810", "Se resta el año menor al mayor.", " años"),
        ("{F} Una alumna usa la fuente A para decir que en 1810 los chilenos pidieron independencia. ¿Qué dato de la fuente la contradice?", "que la junta dice gobernar en nombre del rey Fernando VII", "La fuente muestra lealtad al rey."),
        ("{F} ¿Qué puede decir la fuente B sobre las ideas de los patriotas y qué no puede decir sobre los realistas?", "muestra ideas de patriotas; no muestra lo que pensaban los realistas", "Es un periódico patriota."),
        ("{F} Explica por qué la fuente C y la fuente D pueden contar distinto una misma etapa.", "C la escribió un oficial del rey que estuvo presente; D la escribió un historiador después, con documentos", "Cambia el autor, el momento y el propósito."),
        ("{F} Un compañero afirma: «La fuente D es mejor que la C porque es más reciente». ¿Qué error hay?", "ninguna es mejor en todo: C es testigo directo y D ordena documentos, y hay que usar ambas", "La antigüedad no define la calidad."),
        ("{F} La explicación de la clase nombra un grupo cuya voz no aparece en ninguna de las cuatro fuentes. ¿Cuál es?", "los pueblos indígenas", "Ninguna fuente de la ficha los menciona."),
        ("{F} Si quieres saber lo que pensaban los patriotas en 1812, ¿qué fuente es la más útil y por qué?", "la fuente B, porque es de ese año y defiende ideas patriotas", "El año y el autor coinciden con lo que se pregunta."),
        ("{F} Ordena de la más antigua a la más reciente las fuentes A, B, C y D.", "A, B, C, D", "Los años son 1810, 1812, 1814 y 1900."),
    ],
    ctx=("Para un trabajo escolar, un grupo quiere saber qué pensaba la Primera Junta en 1810. Tiene las cuatro fuentes de la ficha. ¿Cuál debe usar primero y por qué?", "la fuente A, porque es la proclama de la junta en 1810", "Es una fuente primaria del año y autor buscados."),
    sc=[("¿Qué dos preguntas haces a toda fuente?", "quién la escribió y para qué", "Autor y propósito ayudan a entender su punto de vista."),
        ("{F} ¿Es primaria o secundaria la fuente A?", "primaria", "Se creó en 1810, durante los hechos."),
        ("¿Por qué una conclusión necesita varias fuentes?", "porque cada fuente tiene un punto de vista y deja cosas sin decir", "Una sola fuente es parcial.")],
    op=("Escribe una ficha de análisis para tres de las cuatro fuentes (elige las que quieras entre A, B, C y D). En cada ficha anota: quién escribe, año, primaria o secundaria, qué prueba y qué no permite saber. Al final escribe una conclusión de dos oraciones. {F}",
        "Ficha de A: Primera Junta, 1810, primaria; prueba lealtad al rey; no permite saber qué pensaba el pueblo. Conclusión: en 1810 la junta no pidió independencia, pero ya empezó a gobernar.",
        ["tres fichas completas", "primaria o secundaria correcta", "un límite razonable para cada fuente", "conclusión prudente"], ["tres fichas de análisis", "conclusión de dos oraciones"], ["afirmar que A pide independencia", "no incluir ningún límite"],
        "Pide que explique en voz alta por qué su conclusión no afirma más de lo que dicen las fuentes."),
    reinforce="Con tus palabras, di qué fuente de la ficha usarías para conocer a los patriotas y cuál para conocer al ejército del rey.",
    extend="Escribe qué fuente nueva te gustaría encontrar para conocer cómo vivía una familia común durante la Reconquista.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 7 (actores de la independencia, hecha para este cuaderno). "
     "Patriotas: querían gobierno propio. Bernardo O'Higgins, nacido en Chile, fue jefe militar patriota y, desde 1817, Director Supremo. "
     "José Miguel Carrera fue otro jefe patriota. Su hermana, Javiera Carrera, apoyó con decisión la causa patriota. "
     "Manuel Rodríguez organizó acciones contra las fuerzas del rey durante la Reconquista. "
     "Camilo Henríquez, fraile, escribió en el periódico «Aurora de Chile» a favor de las ideas patriotas. "
     "José de San Martín, jefe del ejército de los Andes, llegó desde el Río de la Plata. "
     "Realistas: leales al rey. Mariano Osorio y Casimiro Marcó del Pont fueron jefes de las fuerzas del rey. "
     "Avances patriotas: libre comercio (1811), primer Congreso (1811), un periódico (1812) y el Instituto Nacional (1813). "
     "Retrocesos patriotas: derrota de Rancagua (1814) y derrota de Cancha Rayada (marzo de 1818).")
build(
    OA2, 3, F,
    use="Aprenderé a reconocer a los actores de la independencia de Chile, hombres y mujeres, y a distinguir avances y retrocesos de la causa patriota. Sirve para explicar quiénes actuaron y qué consecuencias tuvo cada hecho.",
    prior=["Sé la diferencia entre patriotas y realistas.", "Sé ordenar los hechos de la independencia en el tiempo.", "Sé distinguir causas y consecuencias."],
    explain=[
        "Un actor histórico es una persona o grupo que participa en un hecho. En la independencia de Chile hubo actores de los dos bandos. Entre los patriotas estuvieron Bernardo O'Higgins, José Miguel Carrera, Javiera Carrera, Manuel Rodríguez, Camilo Henríquez y José de San Martín. Entre los realistas, jefes como Mariano Osorio y Casimiro Marcó del Pont.",
        "También hubo mujeres destacadas. Javiera Carrera apoyó la causa patriota con decisión, y su familia tuvo gran influencia política. Las mujeres no tenían los mismos derechos políticos que los hombres en esa época, por lo que hay menos fuentes sobre ellas, pero participaron en la sociedad y en la guerra de distintas maneras.",
        "La causa patriota tuvo avances y retrocesos. Un avance es un hecho que la fortaleció, como el libre comercio de 1811 o el Instituto Nacional de 1813. Un retroceso es un hecho que la debilitó, como la derrota de Rancagua en 1814 o la de Cancha Rayada en 1818. Estos cambios muestran que la independencia no fue un camino recto.",
    ],
    vocab=[("actor histórico", "persona o grupo que participa en un hecho del pasado"), ("avance", "hecho que fortalece una causa"), ("retroceso", "hecho que debilita una causa"), ("Director Supremo", "cargo de gobierno de Chile desde 1817 que ocupó O'Higgins"), ("libre comercio", "permiso para vender y comprar con otros países sin tantas limitaciones")],
    worked=[
        ("Reconocer el bando", "{F} ¿A qué bando pertenecía Mariano Osorio?", ["Reviso la parte de los realistas en la ficha.", "Allí aparece como jefe de las fuerzas del rey."], "Era realista"),
        ("Clasificar un hecho", "{F} ¿La derrota de Cancha Rayada fue un avance o un retroceso patriota?", ["La ficha la lista entre los retrocesos.", "Debilitó a la causa patriota."], "Un retroceso"),
    ],
    mistakes=[("Pensar que solo hubo hombres en la independencia.", "Se estudian solo los nombres más repetidos.", "Hubo mujeres destacadas, como Javiera Carrera, aunque hay menos fuentes sobre ellas."),
              ("Creer que la causa patriota siempre avanzó.", "Se mira solo el resultado final.", "Hubo retrocesos como Rancagua y Cancha Rayada.")],
    T=[
        ("{F} ¿Qué cargo ocupó O'Higgins desde 1817?", "Director Supremo", "La ficha lo dice."),
        ("{F} ¿Qué mujer de la ficha apoyó la causa patriota?", "Javiera Carrera", "La ficha la menciona."),
        ("{F} ¿Quién llegó desde el Río de la Plata como jefe del ejército de los Andes?", "José de San Martín", "La ficha lo dice."),
        ("{F} ¿Qué dos jefes realistas nombra la ficha?", "Mariano Osorio y Casimiro Marcó del Pont", "Aparecen en la parte de los realistas."),
        ("{F} ¿En qué periódico escribió Camilo Henríquez?", "Aurora de Chile", "La ficha lo menciona."),
        ("=", "{F} ¿Cuántos años pasaron entre el libre comercio y el Instituto Nacional?", "1813-1811", "Se resta el año menor al mayor.", " años"),
        ("{F} Clasifica en «avance» o «retroceso patriota»: a) Instituto Nacional; b) Rancagua; c) periódico de 1812; d) Cancha Rayada.", "avance: a y c; retroceso: b y d", "La ficha enumera esos hechos así."),
        ("{F} ¿Qué actor organizó acciones contra las fuerzas del rey durante la Reconquista?", "Manuel Rodríguez", "La ficha lo indica."),
        ("{F} ¿Qué actores patriotas de la ficha eran hermanos?", "José Miguel Carrera y Javiera Carrera", "La ficha los presenta como hermanos."),
        ("{F} Elena dice: «Todos los jefes de la ficha eran patriotas». Corrígela con un ejemplo.", "No: Mariano Osorio y Marcó del Pont eran realistas", "La ficha los clasifica como realistas."),
        ("{F} Un compañero dice que el periódico de 1812 fue un retroceso. ¿Por qué se equivoca?", "porque fue un avance: difundió ideas patriotas", "La ficha lo lista entre los avances."),
        ("{F} ¿Qué hecho entre los retrocesos tiene fecha en marzo de 1818?", "la derrota de Cancha Rayada", "La ficha le da esa fecha."),
        ("{F} Explica con la ficha por qué la independencia no fue un camino recto.", "porque hubo avances (como el libre comercio) y retrocesos (como Rancagua)", "Ambos aparecen en la ficha."),
    ],
    ctx=("Una profesora dice: «Solo los hombres participaron en la independencia». Usa la ficha para dar una respuesta con dos datos.", "no: la ficha cita a Javiera Carrera, que apoyó la causa patriota, y la sociedad incluía a mujeres de ambos bandos", "El ejemplo de Javiera Carrera contradice la idea."),
    sc=[("¿Qué es un actor histórico?", "una persona o grupo que participa en un hecho del pasado", "La definición de la clase."),
        ("{F} ¿Qué cargo tuvo José de San Martín en Chile: jefe del ejército de los Andes o presidente de la junta?", "jefe del ejército de los Andes", "La ficha lo dice."),
        ("¿Qué diferencia hay entre un avance y un retroceso?", "el avance fortalece una causa y el retroceso la debilita", "Es la definición de ambos términos.")],
    op=("Dibuja una tabla con tres columnas: «actor», «bando» y «qué hizo». Completa al menos cinco filas con actores de la ficha, incluyendo a una mujer. Debajo, escribe dos avances y dos retrocesos de la causa patriota. {F}",
        "Javiera Carrera, patriota, apoyó con decisión la causa. Avances: libre comercio, Instituto Nacional. Retrocesos: Rancagua, Cancha Rayada.",
        ["cinco actores con su bando correcto", "una mujer incluida", "dos avances y dos retrocesos bien clasificados"], ["tabla de actores", "lista de avances y retrocesos"], ["poner a Osorio como patriota", "poner Rancagua como avance"],
        "Pide que explique por qué eligió a esos actores y no a otros."),
    reinforce="Di en voz alta tres actores patriotas y dos realistas de la ficha, con lo que hizo cada uno.",
    extend="Escribe una pregunta sobre qué rol pudieron tener las mujeres comunes durante la guerra, marcando que no tienes fuentes en la ficha.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 8 (perspectivas, hecha para este cuaderno). "
     "Perspectiva patriota (texto inventado, 1818): «Hoy Chile deja de depender del rey. Tenemos derecho a gobernarnos y a comerciar con quien queramos». "
     "Perspectiva realista (texto inventado, 1815): «El rey es la autoridad legítima. Quienes se levantaron contra él faltaron a su juramento de lealtad». "
     "Perspectiva de una mujer de campo (texto inventado, 1817): «Los soldados de ambos bandos pasaron por nuestra casa y se llevaron animales y comida; nos preocupa cómo alimentar a los niños». "
     "Hecho conocido: durante las guerras de independencia, el campo y las ciudades de Chile sufrieron pérdidas, y las familias fueron afectadas por la guerra.")
build(
    OA2, 4, F,
    use="Aprenderé a comparar cómo veían la independencia los patriotas, los realistas y las personas comunes. Sirve para entender que un mismo hecho se vive y se cuenta de distintas formas.",
    prior=["Sé quiénes eran patriotas y realistas.", "Sé que cada fuente tiene un punto de vista.", "Sé hacer una tabla comparativa."],
    explain=[
        "Una perspectiva es la manera en que una persona o grupo ve un hecho, según su situación y sus intereses. En la independencia de Chile, los patriotas, los realistas y las personas comunes vivieron los hechos de modos diferentes. Comparar perspectivas es identificar qué dice cada una, por qué lo dice y en qué se parecen o se diferencian.",
        "Los patriotas defendían el derecho a gobernarse. Los realistas defendían la autoridad del rey y la lealtad jurada. Una familia de campo veía sobre todo el efecto de la guerra: la pérdida de animales y comida. Las tres perspectivas son reales, pero ninguna cuenta toda la historia.",
        "Para comparar bien se usan criterios: qué se defiende, qué se teme y quién habla. También se separa el hecho de la opinión. Es un hecho que hubo guerra y afectó a las familias. Es una opinión decir que el rey era la autoridad legítima o que había derecho a gobernarse. Comprender las perspectivas no es estar de acuerdo con todas, sino entender por qué cada grupo pensaba así.",
    ],
    vocab=[("perspectiva", "manera de ver un hecho según la situación de quien lo vive"), ("legítimo", "que se considera justo y con derecho a mandar"), ("lealtad", "fidelidad a una persona o a una autoridad"), ("hecho", "algo que ocurrió y se puede comprobar"), ("opinión", "juicio de una persona que no se puede comprobar como un hecho")],
    worked=[
        ("Identificar una perspectiva", "{F} ¿Qué defiende la perspectiva realista?", ["Leo el texto del realista.", "Dice que el rey es autoridad legítima y que se faltó a la lealtad."], "La autoridad legítima del rey y la lealtad a él"),
        ("Separar hecho de opinión", "{F} ¿«Hubo guerra en Chile» es un hecho o una opinión?", ["Se puede comprobar con fuentes que hubo guerra.", "No depende del bando de quien lo dice."], "Un hecho"),
    ],
    mistakes=[("Pensar que hay una sola perspectiva verdadera sobre un hecho.", "Se confunde comprender con aceptar.", "Hay varias perspectivas; se estudian con evidencia sin perder de vista los hechos."),
              ("Mezclar hecho y opinión.", "No se pregunta si se puede comprobar.", "Los hechos se comprueban; las opiniones expresan lo que alguien piensa.")],
    T=[
        ("{F} ¿Qué perspectiva habla de preocupación por alimentar a los niños?", "la de la mujer de campo", "El texto lo dice."),
        ("{F} ¿Qué derecho afirma la perspectiva patriota?", "el derecho a gobernarse y comerciar con quien quieran", "El texto lo dice."),
        ("{F} ¿Qué idea de lealtad aparece en la perspectiva realista?", "que quienes se levantaron faltaron a su juramento de lealtad al rey", "Lo afirma el texto realista."),
        ("{F} ¿Cuál de las tres perspectivas es la más antigua (año menor)?", "la realista (1815)", "Los años son 1818, 1815 y 1817."),
        ("=", "{F} ¿Cuántos años separan la perspectiva realista de la patriota?", "1818-1815", "Se resta el año menor al mayor.", " años"),
        ("{F} Clasifica como hecho (H) u opinión (O): a) Hubo guerra en Chile durante la independencia; b) el rey es autoridad legítima; c) Chile tiene derecho a gobernarse.", "a: H; b: O; c: O", "La guerra se comprueba con fuentes; b y c expresan convicciones."),
        ("{F} ¿Qué tienen en común la perspectiva patriota y la realista?", "ambas defienden con razones lo que consideran justo", "Cada una defiende lo que considera legítimo."),
        ("{F} ¿En qué se diferencia la perspectiva de la mujer de campo de las otras dos?", "habla de las consecuencias de la guerra en su familia, no de quién debe gobernar", "Su foco es la vida cotidiana."),
        ("{F} Un compañero dice: «El texto patriota es mentira porque no es del rey». ¿Qué error comete?", "confunde perspectiva con falsedad: todas son puntos de vista que hay que analizar", "Un punto de vista no es una mentira."),
        ("{F} Elige la mejor pregunta para analizar la perspectiva realista: A) ¿qué defendía ese grupo y por qué?; B) ¿cuántas palabras tiene?; C) ¿quién tiene mejor letra?", "A", "Pregunta por intereses y razones."),
        ("{F} ¿Qué perspectiva falta en la ficha y que debería investigarse para tener una visión más completa?", "la de los pueblos indígenas o las personas esclavizadas, por ejemplo", "Ninguno de los tres textos la incluye."),
        ("{F} Si un trabajo escolar dice «todos los chilenos celebraron la independencia», ¿qué dato de la ficha lo cuestiona?", "que hubo realistas y familias afectadas por la guerra", "No todos vivieron igual los hechos."),
        ("{F} ¿Cuál oración compara bien dos perspectivas? A) Mientras que los patriotas defendían gobernarse, los realistas defendían la lealtad al rey. B) Todos defendían exactamente lo mismo.", "A", "Compara lo que defiende cada grupo con un criterio."),
    ],
    ctx=("Una compañera dice: «No sirve estudiar a los realistas porque perdieron». Con la ficha, da una razón para estudiarlos.", "porque sin su perspectiva no entendemos por qué hubo guerra ni qué defendían", "Comprender la guerra exige conocer ambos lados."),
    sc=[("¿Qué es una perspectiva?", "la manera en que un grupo ve un hecho según su situación", "La definición de la clase."),
        ("{F} ¿«El rey es autoridad legítima» es un hecho o una opinión?", "una opinión", "No se puede comprobar como un hecho."),
        ("¿Comprender una perspectiva significa estar de acuerdo con ella?", "no, significa entender por qué ese grupo pensaba así", "Comprender no es aprobar.")],
    op=("Elige dos perspectivas de la ficha y escribe un cuadro con tres filas: «qué defiende», «qué teme» y «por qué lo piensa». Después escribe una oración que compare ambas y otra que diga qué perspectiva falta. {F}",
        "Patriota: defiende gobernarse; teme seguir dependiendo del rey. Realista: defiende la lealtad; teme que se rompa el juramento al rey. Oración: Mientras los patriotas querían gobernarse, los realistas defendían la lealtad al rey.",
        ["dos perspectivas con tres filas", "una oración comparativa", "una perspectiva faltante nombrada"], ["cuadro de comparación", "oración comparativa"], ["decir que una perspectiva es la verdadera", "copiar la ficha sin comparar"],
        "Pide que diga qué parte de su cuadro es hecho y qué parte es opinión."),
    reinforce="Cuenta a alguien de tu casa dos perspectivas de la ficha sin decir cuál prefieres.",
    extend="Escribe una pregunta que la ficha no responde sobre cómo vivieron la guerra las personas del sur de Chile.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 9 (hitos de la independencia, hecha para este cuaderno). "
     "Hito 1: cabildo abierto de septiembre de 1810 y Primera Junta, porque por primera vez un gobierno propio decide en Chile. "
     "Hito 2: primer Congreso Nacional de 1811, porque reúne a representantes elegidos para decidir. "
     "Hito 3: batalla de Rancagua de 1814, porque termina la Patria Vieja y da paso a la Reconquista. "
     "Hito 4: batalla de Chacabuco de 1817, porque permite recuperar Santiago y formar un nuevo gobierno patriota. "
     "Hito 5: Declaración de la Independencia de 1818, porque anuncia oficialmente que Chile deja de depender del rey. "
     "Hito 6: batalla de Maipú de 1818, porque asegura la independencia frente al ejército del rey.")
build(
    OA2, 5, F,
    use="Aprenderé a elegir un hito de la independencia de Chile y a defender mi elección con evidencia. Sirve para argumentar con razones y no solo con opiniones.",
    prior=["Sé ubicar los hechos de la independencia en el tiempo.", "Sé quiénes fueron los actores principales.", "Sé distinguir hecho de opinión."],
    explain=[
        "Argumentar es defender una idea con razones y evidencia. Un argumento tiene tres partes: una afirmación, que es lo que defiendes; una evidencia, que es el dato que la apoya; y una razón, que explica cómo la evidencia sostiene la afirmación. Por ejemplo: «La Declaración de 1818 fue un hito, porque anunció oficialmente que Chile dejaba de depender del rey».",
        "Un hito es un hecho importante que marca un antes y un después. En la independencia de Chile hay varios: la Primera Junta, el primer Congreso, Rancagua, Chacabuco, la Declaración y Maipú. No hay un solo hito correcto: se puede elegir cualquiera, siempre que la razón sea válida y use evidencia de las fuentes.",
        "Un buen argumento también reconoce un límite o una objeción. Por ejemplo, alguien podría decir que Maipú fue más importante que la Declaración, porque aseguró la independencia en el campo de batalla. Responder a esa objeción hace el argumento más sólido. Así se evita repetir lo que dice el libro y se piensa con evidencia.",
    ],
    vocab=[("hito", "hecho importante que marca un antes y un después"), ("argumento", "idea defendida con una razón y una evidencia"), ("evidencia", "dato o fuente que apoya una afirmación"), ("objeción", "razón que se opone a una idea"), ("afirmación", "idea que alguien defiende")],
    worked=[
        ("Armar un argumento", "{F} Defiende que el hito 4 fue importante.", ["Afirmación: Chacabuco fue un hito importante.", "Evidencia y razón: permitió recuperar Santiago y formar un nuevo gobierno patriota."], "Chacabuco fue un hito porque permitió recuperar Santiago y formar un nuevo gobierno patriota"),
        ("Distinguir evidencia de opinión", "{F} ¿«Maipú es el hito más lindo» es un argumento con evidencia?", ["«Lindo» es un gusto personal.", "No hay dato de la ficha que lo apoye."], "No: es una opinión sin evidencia"),
    ],
    mistakes=[("Elegir un hito y decir solo «porque sí».", "Falta la razón y la evidencia.", "Cada afirmación necesita un dato de la ficha y una razón."),
              ("Creer que existe un único hito correcto.", "Se confunde argumento con respuesta única.", "Varios hitos pueden defenderse si hay razón y evidencia.")],
    T=[
        ("{F} ¿Qué hito termina la Patria Vieja?", "la batalla de Rancagua de 1814", "El hito 3 lo dice."),
        ("{F} ¿Qué hito anuncia oficialmente que Chile deja de depender del rey?", "la Declaración de la Independencia de 1818", "El hito 5 lo dice."),
        ("{F} ¿Qué hito reunió a representantes elegidos?", "el primer Congreso Nacional de 1811", "El hito 2 lo dice."),
        ("{F} Completa: «Afirmo que Maipú fue un hito, porque ______». Usa un dato de la ficha.", "asegura la independencia frente al ejército del rey", "Es el dato del hito 6."),
        ("{F} ¿Cuál de estas frases es un argumento con evidencia? A) Rancagua es importante porque sí. B) Rancagua fue un hito porque terminó la Patria Vieja y dio paso a la Reconquista.", "B", "Tiene afirmación, razón y dato."),
        ("{F} ¿Qué dato de la ficha apoya decir que la Primera Junta fue un hito?", "que por primera vez un gobierno propio decide en Chile", "Es la razón del hito 1."),
        ("{F} ¿Qué parte de este argumento es la evidencia? «Chacabuco fue importante porque permitió recuperar Santiago».", "permitió recuperar Santiago", "Es el dato que apoya la afirmación."),
        ("{F} Un compañero dice que la Declaración de 1818 fue el hito más importante. ¿Cuál es una objeción? A) La Declaración fue en 1818. B) Maipú aseguró la independencia frente al ejército del rey. C) Hubo seis hitos.", "B", "Defiende otro hito con una razón de la ficha."),
        ("{F} Ordena los hitos 3, 4 y 6 de más antiguo a más reciente.", "3 (1814), 4 (1817), 6 (1818)", "Ordenados por año."),
        ("=", "{F} ¿Cuántos años pasaron entre el primer hito y la Declaración de la Independencia?", "1818-1810", "Se resta el año menor al mayor.", " años"),
        ("{F} Una alumna defiende el hito 1 así: «Fue importante porque estaba en Santiago». ¿Qué le falta a su argumento?", "una razón con evidencia: que por primera vez un gobierno propio decide en Chile", "Estar en Santiago no explica su importancia."),
        ("{F} ¿Cuál es un argumento completo sobre el hito 2? A) El Congreso fue importante. B) El Congreso fue un hito porque reunió a representantes elegidos para decidir.", "B", "Solo B tiene afirmación, razón y evidencia."),
        ("{F} Elige la razón que corresponde a Chacabuco: A) dio paso a la Reconquista; B) permitió recuperar Santiago y formar un nuevo gobierno patriota.", "B", "La razón A corresponde a Rancagua."),
    ],
    ctx=("En un concurso de historia debes recomendar qué hito destacar en una exposición de tu colegio sobre la independencia. Escribe tu recomendación en una oración con razón y evidencia.", "Recomiendo la Declaración de 1818, porque anunció oficialmente que Chile dejaba de depender del rey", "Cualquier hito sirve si tiene razón y evidencia de la ficha."),
    sc=[("¿Cuáles son las tres partes de un argumento?", "afirmación, evidencia y razón", "Así se organiza un argumento."),
        ("{F} ¿Qué hito terminó la Patria Vieja?", "la batalla de Rancagua", "La ficha lo dice."),
        ("¿Para qué sirve responder a una objeción?", "para que el argumento sea más sólido", "Reconoce razones contrarias y las responde.")],
    op=("Escribe un texto corto de cuatro oraciones: 1) elige un hito de la ficha; 2) di por qué fue importante con un dato; 3) escribe una objeción que podría hacer otro compañero; 4) responde a la objeción. {F}",
        "Elijo la Declaración de 1818. Fue un hito porque anunció oficialmente que Chile dejaba de depender del rey. Otro podría decir que Maipú fue más importante. Pero sin la Declaración no habría un acto oficial que fundara el nuevo país.",
        ["hito elegido de la ficha", "razón con dato", "objeción y respuesta"], ["texto de cuatro oraciones"], ["no incluir dato", "copiar la ficha sin razonar"],
        "Pide que explique por qué su respuesta a la objeción es válida."),
    reinforce="Di en voz alta un argumento con afirmación, evidencia y razón sobre un hito de la independencia.",
    extend="Escribe una segunda objeción posible y piensa cómo la responderías con los hitos de la ficha.",
)
