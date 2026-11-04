"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 02 (cultura burguesa, trabajo, familia y género)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 02"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (siglo XIX: años 1801 a 1900). "
     "Burguesía: grupo urbano de comerciantes, industriales, banqueros y profesionales (abogados, médicos) que vive de su trabajo y de su capital; no es nobleza ni campesinado. "
     "Valores burgueses: trabajo, ahorro, educación, orden, puntualidad y vida privada. "
     "Familia burguesa ideal: padre, madre e hijos viviendo juntos (familia nuclear); el hombre trabaja fuera y mantiene el hogar; la mujer cuida el hogar y educa a los hijos. "
     "Hitos: Revolución Francesa, 1789; Código Civil de Chile, 1855.")
build(
    OA, 1, F,
    use="Aprenderé a situar a la burguesía del siglo XIX y a plantear la pregunta que guía este tema: ¿qué ideal de vida y qué valores tenía este grupo y cómo cambió la sociedad?",
    prior=["Sé qué es el liberalismo y qué es el libre mercado.", "Sé ubicar un año en su siglo.", "Sé que las fuentes expresan el punto de vista de alguien."],
    explain=[
        "La burguesía es un grupo social urbano que se enriquece con el comercio, la industria, los bancos o profesiones como la abogacía y la medicina. No nació en la nobleza ni vive de la tierra como el campesino. Su poder viene del trabajo y del capital, es decir, del dinero que se invierte para ganar más. Por eso apoyó ideas liberales, como la propiedad privada y el libre mercado.",
        "La cultura burguesa es el conjunto de valores y costumbres de este grupo. Valoraba el trabajo como virtud, el ahorro, la educación, el orden y la puntualidad. También defendía la vida privada: el hogar era un espacio de intimidad y de respeto. En el ideal de familia, el hombre era el proveedor que trabajaba fuera y la mujer se ocupaba del hogar y de la crianza. Esto se llama separación de roles de género.",
        "Este ideal fue un modelo, no la realidad de todas las familias. Muchas mujeres trabajaban por necesidad, sobre todo las de familias pobres, y no todos los burgueses seguían esas costumbres. Por eso es importante preguntar quién tenía ese ideal, dónde y cuándo, y no suponer que toda la sociedad pensaba igual.",
    ],
    vocab=[("burguesía", "grupo urbano que vive del comercio, la industria, los bancos o profesiones"), ("capital", "dinero o bienes que se invierten para producir más riqueza"), ("familia nuclear", "padre, madre e hijos que viven juntos"), ("rol de género", "tareas y conductas que una sociedad espera de hombres y de mujeres"), ("ética del trabajo", "idea de que trabajar es una virtud moral")],
    worked=[
        ("Calcular una distancia en el tiempo", "¿Cuántos años pasaron entre la Revolución Francesa (1789) y el Código Civil de Chile (1855)?", ["Tomo los dos años de la ficha.", "Resto: 1855 − 1789 = 66."], "66 años"),
        ("Distinguir ideal de realidad", "La ficha dice que la mujer burguesa cuida el hogar. ¿Eso prueba que ninguna mujer trabajaba fuera de casa?", ["La ficha habla de un ideal de familia burguesa.", "No dice nada sobre las mujeres de otros grupos."], "No: es un ideal de un grupo, no de toda la sociedad"),
    ],
    mistakes=[("Decir que toda la sociedad del siglo XIX vivía según el ideal burgués.", "Se confunde un modelo de un grupo con la realidad de todos.", "Escribe «el ideal burgués» y pregunta quiénes no lo vivían."),
              ("Confundir burguesía con nobleza.", "Se olvida que la burguesía vive de su trabajo y capital, no de títulos heredados.", "Define cada grupo por la fuente de su riqueza.")],
    T=[
        ("{F} ¿De qué vive la burguesía según la ficha?", "De su trabajo y de su capital", "La ficha la define así."),
        ("{F} ¿Cómo se llama la familia formada por padre, madre e hijos?", "Familia nuclear", "La ficha usa ese nombre."),
        ("{F} Según el ideal burgués, ¿quién cuida el hogar?", "La mujer", "La ficha asigna ese rol a la mujer."),
        ("=", "{F} ¿Cuántos años pasaron entre el Código Civil de Chile y el final del siglo XIX (1900)?", "1900-1855", "Se resta el año del Código al 1900.", " años"),
        ("{F} ¿En qué siglo ocurre la Revolución Francesa, 1789? A) Siglo XVIII B) Siglo XIX", "A) Siglo XVIII", "El siglo XVIII va de 1701 a 1800."),
        ("{F} ¿Qué es la ética del trabajo? A) Considerar el trabajo como una virtud B) Creer que el éxito depende solo de la herencia", "A) Considerar el trabajo como una virtud", "La explicación la define como idea de que trabajar es una virtud moral."),
        ("{F} Una familia ahorra una parte de su sueldo cada mes y estudia por las noches para progresar. ¿Qué valores burgueses muestra? A) Ahorro y educación B) Herencia y títulos de nobleza", "A) Ahorro y educación", "Guardar dinero y estudiar son valores de la ficha."),
        ("{F} Una persona vive de un título heredado y de las rentas de sus tierras. ¿Es burguesa? A) No, vive de la nobleza y de la tierra B) Sí, porque tiene dinero", "A) No, vive de la nobleza y de la tierra", "La burguesía vive de su trabajo y capital, no de títulos heredados."),
        ("{F} Un médico de ciudad atiende en su consulta y ahorra para educar a sus hijos. ¿A qué grupo social de la ficha corresponde? A) Burguesía B) Campesinado", "A) Burguesía", "La ficha menciona a los profesionales urbanos como parte de la burguesía."),
        ("{F} Un compañero dice: «En el siglo XIX todas las mujeres se quedaban en el hogar». Corrígelo.", "Era el ideal de la familia burguesa; muchas mujeres de familias pobres trabajaban por necesidad", "La ficha habla de un ideal de un grupo, no de toda la sociedad."),
        ("{F} ¿Por qué la burguesía apoyó la propiedad privada y el libre mercado?", "Porque su riqueza venía del comercio, la industria y el capital", "Esas ideas protegían la fuente de su riqueza."),
        ("{F} Dos afirmaciones: (1) «La burguesía valoraba el ahorro». (2) «Todos los habitantes de Europa eran burgueses». ¿Cuál se apoya en la ficha? A) La (1) B) La (2)", "A) La (1)", "La ficha nombra el ahorro como valor burgués y define a la burguesía como un grupo particular."),
        ("¿Cuál es la mejor pregunta histórica para este tema? A) ¿Qué ideal de vida y qué valores tenía la burguesía y cómo participó en las transformaciones del siglo XIX? B) ¿Era buena o mala la burguesía?", "A) ¿Qué ideal de vida y qué valores tenía la burguesía y cómo participó en las transformaciones del siglo XIX?", "La pregunta A se responde con evidencia; la B es un juicio sin criterio."),
    ],
    ctx=("Una exposición dice: «En 1850, todas las familias de Chile vivían como en la ficha 1». ¿Cuál es el problema? A) Generaliza el ideal de un grupo urbano a toda la sociedad B) Usa una fecha del siglo XIX", "A) Generaliza el ideal de un grupo urbano a toda la sociedad", "La ficha describe un ideal de la burguesía, no de todos."),
    sc=[("¿Qué grupo social vive de comercio, industria, bancos o profesiones?", "La burguesía", "Así se define en la ficha."),
        ("¿Qué valor burgués consiste en guardar dinero?", "El ahorro", "Está entre los valores de la ficha."),
        ("=", "¿Cuántos años pasaron entre 1789 y 1860?", "1860-1789", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1780 a 1900 con escala 1 cm = 20 años y marca la Revolución Francesa (1789) y el Código Civil de Chile (1855). Debajo escribe dos frases: una sobre los valores burgueses y otra sobre cómo era el ideal de familia. Termina con una frase que diga qué no podemos afirmar solo con la ficha. {F}",
        "Posiciones desde 1780: 0,45 cm y 3,75 cm. Frases: «La burguesía valoraba el trabajo, el ahorro y la educación»; «El ideal era una familia nuclear con el hombre proveedor y la mujer a cargo del hogar»; «No podemos afirmar que todas las familias vivieran así».",
        ["respeta la escala", "las frases usan datos de la ficha", "señala un límite"], ["línea de tiempo", "tres frases"], ["no medir con la escala", "decir que toda la sociedad era burguesa"],
        "Pide que explique por qué un ideal no es lo mismo que la vida cotidiana."),
    reinforce="Explica a una persona de tu casa qué es la burguesía y da dos valores que defendía.",
    extend="Anota dos hábitos de tu vida diaria (como el ahorro o la puntualidad) y di si se parecen a los valores de la ficha.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, manual de buenas costumbres, 1860: «El padre trabaja y ahorra. La madre cuida el hogar y enseña buenas costumbres. Los hijos estudian y obedecen. Una familia ordenada es la base de una nación próspera.» "
     "Fuente B, cuaderno de gastos de una familia, 1860, en pesos de ejemplo, un mes: ingresos del padre 500; arriendo 150; comida 120; educación de los hijos 80; sirvienta 60; ropa 50; ahorro 40.")
build(
    OA, 2, F,
    use="Aprenderé a leer fuentes sobre la vida burguesa: un manual de costumbres y un registro de gastos, para ver qué dicen del ideal de vida y de la ética del trabajo.",
    prior=["Sé contextualizar una fuente.", "Sé que un ideal no es toda la realidad.", "Sé separar descripción de interpretación."],
    explain=[
        "Un manual de buenas costumbres no describe cómo vivían todos, sino cómo algunos querían que se viviera. Sirve como evidencia del ideal burgués: un orden de roles, deberes y valores. Para saber qué hacía de verdad una familia hay que mirar otras fuentes, como un cuaderno de gastos, que muestra en qué se usaba el dinero.",
        "El cuaderno de gastos permite hacer cálculos. Sumando los gastos y el ahorro se comprueba si coinciden con los ingresos. También se puede calcular qué parte del ingreso se dedicaba a educación o a ahorro. Esa información sirve para interpretar qué valoraba la familia, pero no prueba lo que pensaban todas las familias de la época.",
        "Al contrastar las dos fuentes aparece una pregunta útil: ¿lo que dice el manual coincide con lo que muestra el cuaderno? El manual dice que el padre ahorra y que los hijos estudian; el cuaderno muestra partidas de ahorro y educación. Aun así, es una sola familia de ejemplo y una sola fecha, por lo que la conclusión debe ser prudente.",
    ],
    vocab=[("manual de conducta", "libro que dice cómo comportarse en la sociedad"), ("ingreso", "dinero que entra a una familia"), ("gasto", "dinero que se paga por algo"), ("partida", "cada rubro de un registro de gastos"), ("prudente", "que no afirma más de lo que prueban los datos")],
    worked=[
        ("Comprobar un registro", "En la Fuente B, ¿los gastos y el ahorro suman los ingresos del mes?", ["Sumo: 150 + 120 + 80 + 60 + 50 + 40 = 500.", "Comparo con el ingreso de 500."], "Sí, suman 500"),
        ("Calcular una parte", "¿Qué porcentaje del ingreso se destina al ahorro?", ["Ahorro: 40 de 500.", "40 dividido entre 500 es 0,08, es decir, 8 por ciento."], "8 por ciento"),
    ],
    mistakes=[("Concluir que todas las familias del país gastaban igual que la del cuaderno.", "El cuaderno es de una sola familia y una sola fecha.", "Escribe «esta familia de ejemplo» y compara con otras fuentes."),
              ("Tomar el manual como descripción de la realidad.", "Un manual expresa un deber ser, no lo que ocurría siempre.", "Contrasta el manual con una fuente de datos.")],
    T=[
        ("{F} ¿Qué tipo de fuente es la Fuente A?", "Un manual de buenas costumbres", "La ficha la presenta así."),
        ("{F} ¿Qué hace la madre según la Fuente A?", "Cuida el hogar y enseña buenas costumbres", "El manual asigna ese papel a la madre."),
        ("{F} ¿Cuánto dinero ingresa al mes en la Fuente B?", "500 pesos de ejemplo", "Es el ingreso del padre en la ficha."),
        ("=", "{F} ¿Cuánto se gasta en total en comida y educación de los hijos?", "120+80", "Se suman las dos partidas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se gastan en arriendo y sirvienta juntos?", "150+60", "Se suman las dos partidas.", " pesos"),
        ("{F} ¿Qué partida es mayor? A) Arriendo B) Comida", "A) Arriendo", "El arriendo es 150 y la comida 120."),
        ("=", "{F} Si la familia no tuviera sirvienta, ¿cuánto dinero le sobraría de esos 500 para otros usos?", "500-(150+120+80+50+40)", "Al total de ingresos se le restan los gastos que sí se mantienen.", " pesos"),
        ("{F} ¿Qué partida del cuaderno coincide con el valor del ahorro del manual? A) El ahorro de 40 pesos B) La ropa de 50 pesos", "A) El ahorro de 40 pesos", "El manual dice que el padre ahorra; el cuaderno tiene la partida de ahorro."),
        ("{F} ¿Qué partida del cuaderno coincide con «los hijos estudian»? A) Educación de los hijos B) Arriendo", "A) Educación de los hijos", "Esa partida muestra dinero destinado a estudios."),
        ("{F} ¿Por qué el manual no prueba lo que hacían todas las familias?", "Porque dice cómo se quería que vivieran, no cómo vivían todas", "Un manual expresa un deber ser."),
        ("{F} Un compañero concluye: «En 1860 todas las familias ahorraban 8 por ciento». ¿Qué falla tiene?", "Generaliza los datos de una sola familia de ejemplo a todas", "El cuaderno solo muestra una familia."),
        ("{F} ¿Qué otra fuente ayudaría a saber si el manual describe la realidad? A) Cuadernos de gastos de otras familias de la época B) Una foto actual de una ciudad", "A) Cuadernos de gastos de otras familias de la época", "Comparar varias familias permite ver si el patrón se repite."),
        ("{F} Alguien escribe: «La Fuente B demuestra que la mujer no trabajaba». ¿Qué corrección haces? A) La fuente no dice nada sobre el trabajo de la mujer B) Es correcto porque no aparece su ingreso", "A) La fuente no dice nada sobre el trabajo de la mujer", "Que no aparezca no prueba que no existiera; solo registra el ingreso del padre."),
    ],
    ctx=("Para un trabajo escolar quieres explicar cómo vivía la burguesía. ¿Qué combinación de fuentes es más sólida? A) El manual y el cuaderno de gastos, comparando lo que dicen B) Solo el manual, porque es el más claro", "A) El manual y el cuaderno de gastos, comparando lo que dicen", "Una fuente de ideal y otra de práctica permiten contrastar."),
    sc=[("¿Qué muestra un manual de buenas costumbres?", "El ideal de cómo debían vivir", "Expresa un deber ser."),
        ("¿Qué muestra un cuaderno de gastos?", "En qué se usaba el dinero", "Registra ingresos y gastos."),
        ("=", "Una familia de ejemplo gasta 150 en arriendo, 120 en comida y 40 en ahorro. ¿Cuánto suman esas tres partidas?", "150+120+40", "Se suman las tres partidas nombradas.", " pesos")],
    op=("Con los datos de la ficha, haz una tabla con las seis partidas (cinco gastos y el ahorro) y anota cuántos pesos de los 500 de ejemplo van a cada una. Luego escribe una frase que explique qué valor burgués se ve en una de esas partidas y otra frase que diga qué no podemos concluir. {F}",
        "Arriendo 150; comida 120; educación 80; sirvienta 60; ropa 50; ahorro 40. Frase: «La partida de educación muestra que la familia valoraba estudiar». Límite: «No podemos concluir que todas las familias gastaban igual».",
        ["suma correcta de las partidas", "relaciona una partida con un valor", "señala un límite"], ["tabla completa", "dos frases"], ["no incluir todas las partidas", "generalizar a todas las familias"],
        "Pide que diga qué partida le parece más reveladora y por qué."),
    reinforce="Explica en voz alta por qué un manual y un cuaderno de gastos informan cosas distintas.",
    extend="Anota los gastos de una semana de una persona de tu casa (si te dan permiso) y escribe una frase sobre qué valor muestran.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de cambio y continuidad en el siglo XIX). "
     "Antes: la posición social dependía sobre todo del nacimiento (nobleza). Durante el siglo XIX: el dinero, el trabajo, los estudios y la propiedad ganaron peso como medida de éxito social. "
     "Código Civil de Chile, 1855: la mujer casada quedaba bajo la autoridad del marido. "
     "Mujeres de familias pobres: trabajaban en talleres, fábricas, servicio doméstico y comercio por necesidad. "
     "Ciudades: en muchas ciudades, las familias burguesas se concentraban en los barrios céntricos; los trabajadores vivían en barrios populares.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar el cambio y la continuidad en la cultura burguesa y a ver cómo el territorio, en este caso la ciudad, muestra desigualdades sociales.",
    prior=["Sé qué es la burguesía y su ideal de familia.", "Sé leer un cuadro de datos.", "Sé que un ideal no es toda la realidad."],
    explain=[
        "Un cambio importante del siglo XIX es la forma de medir el éxito. Antes, la posición social dependía sobre todo de haber nacido en una familia noble. Con el avance de la burguesía, ganaron peso el trabajo, el dinero ahorrado, los estudios y la propiedad. Es decir, la sociedad empezó a valorar el mérito y la riqueza producida, aunque el origen familiar seguía importando.",
        "También hay continuidades. Las leyes siguieron limitando a las mujeres: en el Código Civil de Chile de 1855 la mujer casada quedaba bajo la autoridad del marido. Y aunque el ideal burgués decía que la mujer debía estar en el hogar, las mujeres pobres trabajaban por necesidad. Había, entonces, una distancia entre el ideal y la vida de gran parte de la sociedad.",
        "El territorio muestra esas diferencias. En las ciudades, las familias burguesas vivían en barrios céntricos con mejores servicios y los trabajadores en barrios populares. Mirar un mapa o un plano de la ciudad ayuda a ver cómo la desigualdad social se refleja en el espacio. El concepto que ordena este análisis es la segregación espacial.",
    ],
    vocab=[("mérito", "valor que se reconoce por el esfuerzo y las capacidades de una persona"), ("continuidad", "lo que sigue igual a lo largo del tiempo"), ("Código Civil", "conjunto de leyes sobre personas, familia, propiedad y contratos"), ("segregación espacial", "separación de grupos sociales en barrios distintos de una ciudad"), ("servicio doméstico", "trabajo en casas ajenas, como cocinar o limpiar")],
    worked=[
        ("Reconocer un cambio", "Según la ficha, ¿qué cambió en la medida del éxito social?", ["Antes dependía sobre todo del nacimiento.", "Después ganaron peso el dinero, el trabajo, los estudios y la propiedad."], "Pasó del nacimiento al dinero, trabajo y estudios"),
        ("Reconocer una continuidad", "¿Qué siguió igual para las mujeres casadas según el Código Civil de 1855?", ["La ficha dice que quedaban bajo la autoridad del marido.", "Eso limita su autonomía legal."], "Siguieron bajo la autoridad del marido"),
    ],
    mistakes=[("Decir que con la burguesía desapareció toda desigualdad.", "Se ignoran las continuidades en leyes y en barrios.", "Busca qué cambió y qué siguió igual."),
              ("Creer que todas las mujeres se quedaban en el hogar.", "Se toma el ideal por la realidad.", "Recuerda que las mujeres pobres trabajaban por necesidad.")],
    T=[
        ("{F} ¿Qué dependía sobre todo del nacimiento antes del siglo XIX?", "La posición social", "La ficha lo indica en la columna «Antes»."),
        ("{F} ¿Dónde se concentraban las familias burguesas en las ciudades?", "En los barrios céntricos", "La ficha lo dice para las ciudades."),
        ("{F} ¿En qué año se promulgó el Código Civil de Chile mencionado?", "1855", "La ficha lo fecha."),
        ("=", "{F} ¿Cuántos años pasaron entre 1855 y el cierre del siglo XIX (1900)?", "1900-1855", "Se resta el año del Código al año de cierre.", " años"),
        ("{F} ¿Qué es un cambio? A) El dinero y los estudios ganaron peso como medida de éxito B) La mujer casada quedaba bajo la autoridad del marido", "A) El dinero y los estudios ganaron peso como medida de éxito", "Es lo que se transformó respecto de «Antes»; la B es una continuidad."),
        ("{F} ¿Qué es una continuidad? A) Las leyes seguían limitando a la mujer casada B) Se valoraba más el trabajo", "A) Las leyes seguían limitando a la mujer casada", "Es algo que se mantuvo; la B es un cambio."),
        ("{F} Clasifica: «las trabajadoras de los talleres eran mujeres pobres». ¿Qué ideal burgués contradice? A) Que la mujer debía estar en el hogar B) Que el padre debía ahorrar", "A) Que la mujer debía estar en el hogar", "La ficha muestra mujeres que trabajaban fuera por necesidad."),
        ("{F} ¿Qué mostraría un plano de una ciudad con barrios céntricos y populares? A) Segregación espacial B) Igualdad de servicios", "A) Segregación espacial", "La ficha describe grupos sociales en barrios distintos."),
        ("{F} Una niña de familia pobre cose en un taller desde los doce años. ¿Qué ocurre con el ideal de la familia burguesa? A) No se cumple en su caso B) Se cumple igual", "A) No se cumple en su caso", "Su trabajo desmiente la imagen de la mujer solo en el hogar."),
        ("{F} ¿Por qué se puede decir que hubo cambio y continuidad a la vez?", "Porque cambió la medida del éxito, pero las leyes y las desigualdades siguieron", "La ficha muestra avances con permanencias."),
        ("{F} Un compañero dice: «El mérito reemplazó por completo al nacimiento». ¿Qué datos de la ficha lo contradicen?", "La ficha dice que el nacimiento seguía pesando y que las leyes limitaban a la mujer", "El nacimiento perdió peso, pero no desapareció."),
        ("{F} ¿Qué consecuencia tiene para la ciudad que burgueses y trabajadores vivan separados? A) Los servicios y oportunidades se reparten de forma desigual B) Todos tienen la misma vivienda", "A) Los servicios y oportunidades se reparten de forma desigual", "La ficha asocia los barrios céntricos a mejores condiciones."),
        ("{F} ¿Qué conclusión es más proporcional? A) La sociedad valoró más el dinero y el mérito, pero siguieron desigualdades de nacimiento, género y barrio B) La sociedad se volvió igualitaria", "A) La sociedad valoró más el dinero y el mérito, pero siguieron desigualdades de nacimiento, género y barrio", "Reúne cambios y continuidades de la ficha."),
    ],
    ctx=("Un museo de la ciudad cuelga un plano con barrios céntricos y populares. ¿Qué título explica mejor lo que muestra? A) La ciudad del siglo XIX reflejaba diferencias sociales en el espacio B) Todas las familias vivían en la misma zona", "A) La ciudad del siglo XIX reflejaba diferencias sociales en el espacio", "La ficha describe barrios distintos para grupos distintos."),
    sc=[("En el análisis de la cultura burguesa, ¿qué es una continuidad?", "Algo que siguió igual a pesar de los cambios, como las leyes que limitaban a la mujer casada", "Así se aplica el término a la ficha."),
        ("¿Qué ganó peso como medida de éxito en el siglo XIX?", "El dinero, el trabajo, los estudios y la propiedad", "Lo dice la ficha."),
        ("=", "¿Cuántos años pasaron entre 1789 y 1855?", "1855-1789", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», y escribe tres datos en cada una usando solo la ficha. Después escribe una frase que explique qué grupo social ganó más con los cambios y cuál se quedó con menos derechos. {F}",
        "Cambió: más peso del dinero, del trabajo y de los estudios; valoración del mérito; ahorro y educación. Continuó: leyes que limitaban a la mujer casada; desigualdad de barrios; mujeres pobres que trabajaban por necesidad. Frase: «Ganó más la burguesía; las mujeres y los trabajadores se quedaron con menos derechos».",
        ["usa datos de la ficha", "separa cambio y continuidad", "justifica con evidencia"], ["tabla de seis datos", "una frase"], ["repetir el mismo dato en ambas columnas", "afirmar sin apoyarse en la ficha"],
        "Pide que explique por qué la ciudad ayuda a ver las desigualdades."),
    reinforce="Explica en voz alta un cambio y una continuidad de la cultura burguesa.",
    extend="Observa el plano de un barrio de tu ciudad y anota una diferencia que veas entre dos sectores (calles, áreas verdes).",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Empresario, 1870: «Trabajo catorce horas y ahorro cada mes. Mis hijos estudiarán y mi esposa cuidará la casa. Así se construye una nación.» "
     "Obrera de una fábrica textil, 1870: «Trabajo doce horas para que mis hijos coman. No tengo tiempo para estudiar ni para cuidar la casa como quisiera.» "
     "Mujer burguesa, 1870: «Me enseñan que mi lugar es el hogar. Yo quisiera estudiar y opinar en los asuntos públicos.» "
     "Cronista crítico, 1870: «Los ricos hablan del valor del trabajo, pero viven del trabajo de otros.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar las perspectivas de distintos actores sobre el trabajo, la familia y los roles de género, y a explicar el protagonismo de la burguesía.",
    prior=["Sé qué es el ideal burgués.", "Sé que cada actor tiene intereses.", "Sé separar el ideal de la realidad."],
    explain=[
        "En una misma sociedad conviven perspectivas distintas. El empresario defiende la ética del trabajo porque su éxito depende de que se trabaje mucho. La obrera trabaja para sobrevivir y no tiene tiempo para el estudio. La mujer burguesa vive el ideal de la familia como una limitación a sus deseos. El cronista critica que el valor del trabajo no sea el mismo para todos.",
        "Estas voces ayudan a entender el protagonismo de la burguesía. La burguesía impulsó las transformaciones políticas, sociales y económicas del siglo XIX: apoyó revoluciones y constituciones, fundó empresas y bancos, creó periódicos y escuelas. Pero ese protagonismo no benefició a todos por igual, y por eso hubo reclamos de obreros y de mujeres.",
        "Contrastar significa buscar acuerdos y desacuerdos. Aquí, el empresario y el cronista hablan del mismo valor, el trabajo, pero lo interpretan distinto. Una buena explicación no elige un bando sin evidencia: cita qué dice cada voz y explica por qué sus intereses son diferentes.",
    ],
    vocab=[("protagonismo", "papel principal que tiene un grupo en un proceso"), ("jornada", "horas que se trabajan en un día"), ("reclamo", "petición de cambio por considerar injusta una situación"), ("opinar en lo público", "participar en decisiones o debates de la sociedad"), ("contraste", "comparación que muestra diferencias entre perspectivas")],
    worked=[
        ("Comparar jornadas", "Según la ficha, ¿cuántas horas más trabaja el empresario que la obrera?", ["Empresario: 14 horas.", "Obrera: 12 horas. Resto: 14 − 12 = 2."], "2 horas más"),
        ("Identificar un desacuerdo", "El empresario y el cronista hablan del trabajo. ¿En qué difieren?", ["El empresario lo ve como base de la nación.", "El cronista dice que los ricos viven del trabajo de otros."], "Difieren en quién se beneficia del trabajo"),
    ],
    mistakes=[("Quedarse con una sola voz, la del empresario, para explicar toda la sociedad.", "Se ignoran las perspectivas de quienes trabajaban para él.", "Incluye al menos dos voces con intereses opuestos."),
              ("Decir que la burguesía impulsó los cambios en beneficio de todos.", "Los cambios favorecieron más a unos grupos que a otros.", "Pregunta quién ganó y quién quedó con menos.")],
    T=[
        ("{F} ¿Cuántas horas trabaja el empresario según su voz?", "14 horas", "La ficha lo dice directamente."),
        ("{F} ¿Para qué trabaja la obrera?", "Para que sus hijos coman", "Es lo que dice su voz."),
        ("{F} ¿Qué quisiera hacer la mujer burguesa además de cuidar el hogar?", "Estudiar y opinar en los asuntos públicos", "Lo dice su voz."),
        ("=", "{F} Si la obrera duerme 8 horas y trabaja 12, ¿cuántas horas del día le quedan para todo lo demás?", "24-8-12", "Al día de 24 horas se le restan las horas de sueño y de trabajo.", " horas"),
        ("{F} ¿Quién se beneficia más de la ética del trabajo según el cronista? A) Los ricos, que viven del trabajo de otros B) Los obreros que trabajan doce horas", "A) Los ricos, que viven del trabajo de otros", "El cronista critica a los ricos."),
        ("{F} ¿Qué voz muestra una limitación del ideal burgués? A) La mujer burguesa B) El empresario", "A) La mujer burguesa", "Ella siente el ideal del hogar como una restricción."),
        ("{F} ¿Qué voz dice que su lugar en el hogar es algo que le enseñan y no algo que ella eligió? A) La mujer burguesa B) El empresario", "A) La mujer burguesa", "Ella dice «me enseñan que mi lugar es el hogar» y expresa que quisiera otra cosa."),
        ("=", "{F} Si una obrera trabaja seis días a la semana, doce horas al día, ¿cuántas horas trabaja por semana?", "12*6", "Se multiplica la jornada por los días trabajados.", " horas"),
        ("{F} ¿Qué voz explica mejor el protagonismo de la burguesía en el trabajo y los negocios? A) El empresario B) La obrera", "A) El empresario", "Él es el burgués que invierte y dirige."),
        ("{F} ¿Qué voz critica que el valor del trabajo no beneficie a todos por igual? A) El cronista crítico B) El empresario", "A) El cronista crítico", "El cronista dice que los ricos viven del trabajo de otros."),
        ("{F} Un compañero dice: «Todos los grupos de la sociedad estaban contentos con el nuevo orden». ¿Qué voz lo contradice?", "La obrera, la mujer burguesa y el cronista muestran descontento o crítica", "Hay reclamos de varios grupos."),
        ("{F} ¿Por qué el cronista y el empresario discrepan sobre la ética del trabajo?", "Porque uno la usa para defender su éxito y el otro critica quién se beneficia", "Sus intereses y posición son distintos."),
        ("{F} ¿Qué conclusión es más equilibrada? A) La burguesía fue protagonista de los cambios, pero otros grupos pagaron costos y pidieron cambios B) La burguesía hizo cambios que todos celebraron", "A) La burguesía fue protagonista de los cambios, pero otros grupos pagaron costos y pidieron cambios", "Considera las cuatro voces de la ficha."),
    ],
    ctx=("Una revista escolar quiere publicar una entrevista sobre el trabajo en 1870. ¿A quiénes deberían entrevistar para mostrar distintas perspectivas? A) A un empresario y a una obrera B) A dos empresarios", "A) A un empresario y a una obrera", "Dos voces con posición distinta permiten un contraste."),
    sc=[("¿Qué grupo dirige empresas y bancos en el siglo XIX?", "La burguesía", "Es su rasgo central."),
        ("¿Qué es contrastar?", "Comparar para ver diferencias entre perspectivas", "Así se explica en la clase."),
        ("=", "¿Cuántas horas trabaja en una semana una persona que trabaja 12 horas al día durante 5 días?", "12*5", "Se multiplica por los días.", " horas")],
    op=("Elige dos de las cuatro voces de la ficha y haz una tabla con: qué dice cada una, qué valor defiende o cuestiona y qué le conviene. Después redacta tres líneas que expliquen por qué la burguesía fue protagonista pero no benefició a todos por igual. {F}",
        "Empresario: dice que trabaja y ahorra; defiende la ética del trabajo; le conviene que se trabaje mucho. Obrera: trabaja doce horas; cuestiona la falta de tiempo; le conviene una jornada más corta. Texto: «La burguesía dirigió empresas y política, pero los obreros y las mujeres tuvieron menos derechos».",
        ["usa dos voces", "completa dice, valor y conviene", "explica con evidencia"], ["tabla completa", "tres líneas"], ["mezclar las voces", "afirmar sin citar la ficha"],
        "Pide que cuente qué voz le parece más cercana a la vida actual y por qué."),
    reinforce="Elige una voz y explica en voz alta qué quiere y qué teme.",
    extend="Pregunta a una persona de tu casa qué opina del trabajo y compara su respuesta con una voz de la ficha.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento). "
     "Pregunta: ¿por qué se dice que la burguesía fue protagonista de las transformaciones del siglo XIX? "
     "Dato 1: en la Revolución Francesa (1789), abogados, comerciantes y otros burgueses ocuparon cargos importantes. "
     "Dato 2: la burguesía fundó empresas, bancos, periódicos y escuelas. "
     "Dato 3: en muchos países el voto era censitario, es decir, votaban quienes tenían renta o propiedad. "
     "Dato 4: la burguesía era una minoría de la población; muchas mujeres y trabajadores no participaban en esas decisiones.")
build(
    OA, 5, F,
    use="Aprenderé a escribir un argumento sobre el protagonismo de la burguesía, con afirmación, evidencia, razonamiento y una conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé que una conclusión debe ser proporcional a la evidencia.", "Conozco los valores y el ideal burgués."],
    explain=[
        "Un argumento sobre la burguesía parte de una pregunta como «¿por qué fue protagonista?». La afirmación puede ser: «la burguesía fue protagonista porque tuvo poder político, económico y cultural». La evidencia son los datos: cargos en la Revolución Francesa, empresas y bancos, voto censitario. El razonamiento explica cómo cada dato muestra una forma de poder.",
        "Para que sea proporcional, el argumento debe reconocer límites. Aunque la burguesía fue protagonista, era una minoría. Muchas personas, como mujeres y trabajadores, no participaban en las decisiones. Una conclusión como «la burguesía hizo todos los cambios» exagera. Es mejor decir «lideró muchos cambios, junto a otros grupos que también presionaron».",
        "Un buen argumento anticipa un contraargumento: un dato que podría contradecir la afirmación. Por ejemplo, el dato 4 recuerda que la burguesía no representaba a toda la sociedad. Responder al contraargumento fortalece el texto, porque muestra que la conclusión se ajusta a todos los datos.",
    ],
    vocab=[("protagonista", "grupo que lidera un proceso"), ("afirmación", "respuesta que defiendes a una pregunta"), ("razonamiento", "explicación que une evidencia y afirmación"), ("minoría", "grupo menos numeroso dentro de una población"), ("contraargumento", "idea o dato que podría contradecir tu afirmación")],
    worked=[
        ("Elegir evidencia de poder económico", "¿Qué dato de la ficha muestra poder económico?", ["Busco un dato sobre dinero o negocios.", "El dato 2 menciona empresas y bancos."], "Dato 2"),
        ("Encontrar un límite", "¿Qué dato limita la idea de que la burguesía representaba a toda la sociedad?", ["La afirmación dice «toda la sociedad».", "El dato 4 dice que era una minoría."], "Dato 4"),
    ],
    mistakes=[("Escribir que la burguesía hizo todos los cambios.", "Se ignoran otros grupos que también presionaron.", "Usa expresiones como «lideró muchos cambios»."),
              ("Citar un dato sin explicar qué muestra.", "Falta el razonamiento que conecta dato y afirmación.", "Agrega una frase que empiece con «Esto muestra que…».")],
    T=[
        ("{F} ¿Qué dato muestra poder político?", "El dato 1, cargos importantes en la Revolución Francesa", "Ocupar cargos importantes es poder político."),
        ("{F} ¿Qué dato muestra poder cultural?", "El dato 2, porque funda periódicos y escuelas", "Los periódicos y las escuelas difunden ideas y valores."),
        ("{F} ¿Qué dato muestra que votar dependía de la riqueza?", "El dato 3, el voto censitario", "El dato 3 habla de renta o propiedad."),
        ("{F} ¿Qué parte de un argumento es el dato? A) La evidencia B) El razonamiento", "A) La evidencia", "La evidencia son los datos de las fuentes."),
        ("{F} ¿Qué afirmación responde la pregunta? A) La burguesía fue protagonista porque tuvo poder político, económico y cultural B) La burguesía no tuvo ninguna influencia", "A) La burguesía fue protagonista porque tuvo poder político, económico y cultural", "Se apoya en los datos 1, 2 y 3."),
        ("{F} ¿Qué dato sirve de contraargumento? A) El dato 4 B) El dato 2", "A) El dato 4", "Muestra que era una minoría y que otros no participaban."),
        ("{F} Completa el razonamiento: «El dato 3 muestra que la burguesía…» A) tenía más poder para decidir porque podía votar B) no podía votar", "A) tenía más poder para decidir porque podía votar", "El voto censitario beneficiaba a quienes tenían renta o propiedad."),
        ("{F} Un compañero escribe: «La burguesía hizo todos los cambios». ¿Cómo lo reformulas?", "La burguesía lideró muchos cambios, pero otros grupos también presionaron y no participaban de las decisiones", "El dato 4 impide decir «todos»."),
        ("{F} ¿Por qué el dato 2 refuerza la afirmación de poder económico y cultural?", "Porque muestra que fundó empresas, bancos, periódicos y escuelas", "Son instituciones que dan poder económico y cultural."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «lideró» B) «hizo todo»", "A) «lideró»", "No dice que fuera el único actor."),
        ("{F} Ordena las partes de un buen argumento: contraargumento y respuesta, afirmación, evidencia, razonamiento.", "Afirmación, evidencia, razonamiento, contraargumento y respuesta", "Primero se responde, luego se prueba, se explica y se responde a la objeción."),
        ("{F} ¿Qué dato falta en la ficha para completar el argumento sobre el trabajo de las mujeres? A) Un dato sobre el trabajo de mujeres pobres B) Otro dato del dato 1", "A) Un dato sobre el trabajo de mujeres pobres", "Ayuda a evaluar el protagonismo y sus límites."),
        ("{F} ¿Qué conclusión se ajusta mejor a los cuatro datos? A) La burguesía fue protagonista de los cambios, pero siendo minoría dejó fuera a mujeres y trabajadores B) La burguesía representó a toda la sociedad", "A) La burguesía fue protagonista de los cambios, pero siendo minoría dejó fuera a mujeres y trabajadores", "Reúne el liderazgo y su límite."),
    ],
    ctx=("Un diario escolar publica: «La burguesía hizo todo el progreso del siglo XIX». ¿Qué evidencia de la ficha usarías para matizar? A) El dato 4, que muestra que era minoría y que otros grupos no participaban B) El dato 2 solo", "A) El dato 4, que muestra que era minoría y que otros grupos no participaban", "Permite corregir la generalización."),
    sc=[("¿Qué parte de un argumento sobre la burguesía explica cómo un dato apoya la afirmación?", "El razonamiento", "Es la parte que une el dato con la afirmación."),
        ("En el argumento sobre la burguesía, ¿qué dato de la ficha funciona como contraargumento?", "El dato 4, que era una minoría", "Contradice la idea de que representaba a toda la sociedad."),
        ("=", "¿Cuántos años pasaron entre la Revolución Francesa (1789) y 1900?", "1900-1789", "Se resta el año menor al mayor.", " años")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Por qué se dice que la burguesía fue protagonista de las transformaciones del siglo XIX?». Usa al menos tres datos de la ficha, incluye el dato 4 como límite y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«La burguesía fue protagonista porque tuvo poder político, económico y cultural. En 1789 ocupó cargos en la Revolución Francesa. Además fundó empresas, bancos, periódicos y escuelas, y el voto censitario le daba más peso. Sin embargo, era una minoría y dejó fuera a mujeres y trabajadores, por lo que no representó a toda la sociedad».",
        ["responde la pregunta", "usa tres datos y el límite", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["usar «todos» sin evidencia", "no explicar cómo el dato apoya la idea"],
        "Pide que diga qué grupo habría opinado distinto y qué diría."),
    reinforce="Explica en voz alta por qué la burguesía fue protagonista y qué límite tuvo su protagonismo.",
    extend="Escribe un contraargumento en dos líneas y responde con el dato 4.",
)
