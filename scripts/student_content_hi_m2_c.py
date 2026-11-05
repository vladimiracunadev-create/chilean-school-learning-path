"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 18 (Constitución de 1980: institucionalidad, cambios y continuidades)."""
from __future__ import annotations

from hi5_lib import build

MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

OA = "HI2M OA 18"

# ---------------------------------------------------------------- Clase 1
F1 = ("Resumen de ejemplo, redactado para este cuaderno: en 1973 una Junta de Gobierno militar, encabezada por Augusto Pinochet, asumió el poder en Chile. "
      "Una comisión de expertos preparó un proyecto de nueva Constitución. El 11 de septiembre de 1980 se votó en un plebiscito, sin competencia libre entre las opciones. "
      "La Constitución comenzó a regir en marzo de 1981 y sus artículos transitorios fijaron cómo se pasaría del gobierno de la Junta al nuevo orden.")
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo la Constitución de 1980 y a reconocer a sus actores y a sus artículos transitorios. Sirve para entender de dónde viene gran parte de nuestras reglas políticas.",
    prior=["Sé qué es una ley y para qué sirve.", "Sé ubicar años en una línea de tiempo.", "Conozco la diferencia entre dictadura y democracia."],
    explain=[
        "Una constitución es la norma más importante de un país: define cómo se organiza el Estado, quién toma las decisiones y qué derechos tienen las personas. Todas las leyes deben respetarla. La institucionalidad es el conjunto de instituciones y reglas que organizan la vida política, como el Congreso, los tribunales y las Fuerzas Armadas.",
        "La Constitución de 1980 se redactó durante la dictadura militar, cuando el Congreso no funcionaba y las decisiones las tomaba la Junta de Gobierno. Sus actores principales fueron la Junta, una comisión de expertos que preparó el proyecto y la ciudadanía, que solo pudo votar sí o no en un plebiscito, es decir, una votación directa sobre una propuesta.",
        "El texto tuvo artículos permanentes y artículos transitorios. Un artículo transitorio es una norma de duración limitada que regula el paso de un régimen a otro. Los transitorios mantuvieron a la Junta con la función de dictar leyes mientras no se instalara el Congreso y fijaron un período de ocho años para el presidente inicial. Distinguir lo permanente de lo transitorio evita confundir lo que sería definitivo con lo que era un puente.",
    ],
    vocab=[("constitución", "norma más importante de un país, que organiza el Estado y protege derechos"), ("institucionalidad", "conjunto de instituciones y reglas que organizan la vida política"), ("plebiscito", "votación en que la ciudadanía responde sí o no a una propuesta"), ("artículo transitorio", "norma de duración limitada que regula el paso de un régimen a otro"), ("Junta de Gobierno", "órgano formado por los comandantes en jefe de las Fuerzas Armadas y el general director de Carabineros, que ejerció el poder desde 1973")],
    worked=[
        ("Ordenar hechos en el tiempo", "El resumen menciona: (1) la Constitución comenzó a regir; (2) se votó el plebiscito; (3) la Junta asumió el poder. ¿En qué orden ocurrieron?",
         ["Busco cada fecha: 1973, septiembre de 1980 y marzo de 1981.", "Ordeno de la más antigua a la más reciente."], "Primero la Junta asumió (1973), luego se votó el plebiscito (1980) y después la Constitución comenzó a regir (1981)"),
        ("Distinguir norma permanente y transitoria", "Un artículo de ejemplo dice: «Durante los dos primeros años, un consejo provisional dirigirá el servicio». ¿Es permanente o transitorio?",
         ["Un artículo transitorio tiene un plazo y regula un paso entre situaciones.", "Este tiene un plazo de dos años y habla de un consejo provisional."], "Transitorio"),
    ],
    mistakes=[
        ("Creer que una constitución es una ley más, igual a las demás.", "Es la norma superior: las leyes deben respetarla y no al revés.", "Pregunta si la norma organiza el Estado y protege derechos; si es así, es de rango constitucional."),
        ("Pensar que todo plebiscito es igual a una votación libre y competitiva.", "Un plebiscito vale según las condiciones en que se realiza, por ejemplo si las opciones compiten con libertad.", "Revisa cuándo, quién convocó y si había competencia entre opciones."),
    ],
    T=[
        ("En Historia: ¿qué es una constitución?", "La norma más importante de un país, que organiza el Estado y protege derechos", "Todas las demás leyes deben respetarla."),
        ("{F} ¿Qué actor tomaba las decisiones políticas principales cuando se redactó la Constitución? A) el Congreso elegido, B) la Junta de Gobierno.", "B", "El Congreso no funcionaba y la Junta ejercía el poder."),
        ("Un artículo transitorio es una norma: A) de duración limitada que regula el paso de un régimen a otro, B) que no puede modificarse nunca.", "A", "Se aplica un tiempo para organizar el cambio."),
        ("{F} ¿En qué fecha comenzó a regir la Constitución, según el resumen? A) en septiembre de 1980, B) en marzo de 1981.", "B", "En septiembre de 1980 solo se votó; comenzó a regir en marzo de 1981."),
        ("{F} ¿Qué limitaba el plebiscito de 1980, según el resumen? A) que no hubo competencia libre entre las opciones, B) que no se realizó votación, C) que votaron solo las Fuerzas Armadas.", "A", "El resumen dice que se votó sin competencia libre entre opciones, pero sí hubo votación."),
        ("Un artículo de ejemplo dice: «Durante los primeros tres años, un comité provisional administrará el servicio». ¿Es permanente o transitorio? A) permanente, B) transitorio.", "B", "Tiene un plazo y regula una etapa provisional."),
        ("¿Cuál de estas normas de ejemplo es transitoria? A) «Mientras no se instale el Congreso, la Junta dictará las leyes», B) «Chile es una república democrática».", "A", "La primera vale solo hasta que ocurra un hecho; la segunda describe el orden permanente."),
        ("{F} ¿Qué ocurrió primero? A) la Constitución comenzó a regir, B) se votó el plebiscito.", "B", "Se votó en septiembre de 1980 y comenzó a regir en marzo de 1981."),
        ("{F} ¿Qué hizo la comisión de expertos? A) preparó el proyecto de Constitución, B) lo aprobó en el plebiscito, C) gobernó el país en lugar de la Junta.", "A", "La ciudadanía votó en el plebiscito y la Junta gobernaba; la comisión redactó el proyecto."),
        ("Una compañera dice: «Como hubo plebiscito, la Constitución de 1980 nació igual que una Constitución elaborada en democracia». ¿Qué le falta considerar? A) que el plebiscito se hizo sin competencia libre de opciones y con el Congreso cerrado, B) cuántos votos obtuvo la opción ganadora.", "A", "Las condiciones del plebiscito importan tanto como su existencia."),
        ("{F} ¿Por qué conviene separar artículos transitorios de permanentes al analizar la Constitución? A) porque los transitorios muestran el paso entre regímenes y los permanentes, el orden de largo plazo, B) porque solo los permanentes obligan.", "A", "Ambos obligan, pero cumplen funciones distintas en el tiempo."),
        ("{F} Un estudiante dice: «La Constitución de 1980 se escribió en democracia». ¿Qué dato del resumen lo contradice? A) la preparó una comisión de expertos mientras gobernaba la Junta, B) comenzó a regir en 1981.", "A", "El resumen indica que la Junta tenía el poder desde 1973 cuando se preparó el proyecto."),
        ("{F} Un estudiante concluye: «La Constitución de 1980 la decidió completamente la ciudadanía». ¿Qué dato del resumen lo debilita? A) la comisión de expertos preparó el proyecto y la ciudadanía solo votó sí o no, B) la Constitución rigió desde 1981.", "A", "La ciudadanía solo respondió a un texto ya redactado."),
    ],
    ctx=("Un liceo prepara un panel sobre los actores de 1980. ¿Qué actores debe incluir como mínimo para explicar cómo nació la Constitución? A) la Junta de Gobierno, la comisión de expertos y la ciudadanía que votó, B) solo la ciudadanía que votó.", "A", "Los tres participaron en distintas etapas del proceso."),
    sc=[("En Historia: ¿qué es un plebiscito?", "Una votación en que la ciudadanía responde sí o no a una propuesta", "Se decide sobre un texto o una propuesta ya definida."),
        ("¿Qué es la institucionalidad?", "El conjunto de instituciones y reglas que organizan la vida política", "Incluye al Congreso, los tribunales y las Fuerzas Armadas."),
        ("¿Cómo reconoces un artículo transitorio?", "Porque regula un plazo o el paso entre regímenes y deja de aplicarse", "Tiene vigencia limitada.")],
    op=("{F} Usa el resumen para escribir una línea de tiempo con tres fechas (1973, 1980 y 1981), una frase por fecha, y nombra qué actor aparece en cada una. Cierra con una frase que explique qué es un artículo transitorio.",
        "1973: la Junta de Gobierno asume el poder. 1980: se vota el plebiscito, con la comisión de expertos y la ciudadanía como actores. 1981: la Constitución comienza a regir. Un artículo transitorio es una norma de duración limitada para pasar de un régimen a otro.",
        ["escribe tres fechas en orden", "nombra un actor por fecha", "define artículo transitorio con sus palabras"], ["una línea de tiempo con cuatro frases"], ["ordenar mal las fechas", "decir que el artículo transitorio no obliga"], "Pide a una persona de tu casa que lea tu línea de tiempo y diga si las fechas están en orden."),
    reinforce="Escribe con tus palabras qué diferencia hay entre una ley y una constitución.",
    extend="Explica por qué las condiciones de una votación importan para juzgar su legitimidad.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Fuente A (resumen de ejemplo, basado en el sentido del texto de 1980): las Fuerzas Armadas existen para la defensa de la patria y son garantes del orden institucional de la República. "
      "Fuente B (declaración de ejemplo, de un vocero del gobierno militar): «La Constitución asegura que las instituciones no caerán en manos de quienes quieren destruirlas». "
      "Fuente C (declaración de ejemplo, de un grupo opositor): «Un orden que pone a las Fuerzas Armadas como garantes limita la soberanía popular, porque los votantes no deciden sobre ellas».")
build(
    OA, 2, F2,
    use="Aprenderé a leer con cuidado la función tutelar de las Fuerzas Armadas, preguntando quién habla, cuándo y con qué interés. Sirve para distinguir un texto oficial de una opinión.",
    prior=["Sé qué es una constitución y quiénes participaron en la de 1980.", "Sé distinguir un hecho de una opinión.", "Sé que una fuente puede ser un texto, un discurso o una declaración."],
    explain=[
        "La Constitución de 1980 no solo asignó a las Fuerzas Armadas la defensa de la patria, sino que las declaró garantes del orden institucional. Tutelar significa proteger o vigilar. Por eso se habla de una función tutelar: las instituciones armadas quedaban como vigilantes del orden político, además de ser defensa externa. Los comandantes en jefe, además, gozaban de inamovilidad: durante su período el Presidente no podía removerlos, salvo en casos excepcionales fijados por la propia Constitución.",
        "Para interpretar esta idea hay que mirar la procedencia de cada fuente, es decir, quién la produjo, cuándo, dónde y con qué propósito. Un texto constitucional es una fuente primaria y oficial: dice lo que la norma establece. Una declaración de un vocero o de un grupo opositor expresa una posición con intereses propios y debe leerse como un juicio, no como un hecho comprobado.",
        "La soberanía popular es la idea de que el poder reside en el pueblo, que lo ejerce mediante el voto. La oposición sostuvo que una función tutelar limitaba esa soberanía; el gobierno de la época sostuvo que protegía las instituciones. Un buen análisis no escoge una voz sin más: separa lo que dice el texto de lo que cada actor opina sobre él.",
    ],
    vocab=[("función tutelar", "papel de proteger o vigilar el orden institucional"), ("garante", "quien asegura que algo se cumpla"), ("procedencia", "quién produjo una fuente, cuándo, dónde y con qué propósito"), ("soberanía popular", "idea de que el poder reside en el pueblo y se ejerce mediante el voto"), ("inamovilidad", "condición de no poder ser removido de un cargo durante un período")],
    worked=[
        ("Leer la procedencia", "Una declaración de ejemplo, firmada en 1981 por un ministro del gobierno militar, elogia la Constitución. ¿Qué dato de procedencia debes considerar antes de usarla como prueba?",
         ["Pregunto quién la escribió y qué interés tiene.", "El autor integra el gobierno que impulsó la Constitución."], "Que el autor tiene interés en defender la Constitución"),
        ("Separar texto y juicio", "De dos frases de ejemplo, ¿cuál es un juicio? (1) «Las Fuerzas Armadas son garantes del orden institucional». (2) «Esta función es injusta».",
         ["La frase (1) repite lo que dice una norma y se puede comprobar en el texto.", "La frase (2) valora la norma como injusta."], "La frase (2)"),
    ],
    mistakes=[
        ("Usar la declaración de un actor como si describiera lo que dice la Constitución.", "Una declaración interpreta y valora; no reemplaza al texto.", "Contrasta la declaración con el texto constitucional."),
        ("Descartar una fuente solo porque su autor tiene una posición.", "Todas las fuentes tienen autor e intereses; sirven si se leen con su procedencia.", "Úsala para conocer la posición del actor, no como prueba neutral."),
    ],
    T=[
        ("En Historia: ¿qué significa que las Fuerzas Armadas tuvieran una función tutelar en la Constitución de 1980?", "Que debían proteger o vigilar el orden institucional, además de defender la patria", "Tutelar significa proteger o vigilar."),
        ("{F} ¿Cuál de las fuentes resume el texto constitucional? A) la fuente A, B) la fuente B, C) la fuente C.", "A", "Las otras dos son declaraciones de actores con posición propia."),
        ("En Historia: ¿qué es la procedencia de una fuente?", "Quién la produjo, cuándo, dónde y con qué propósito", "Permite juzgar el interés del autor."),
        ("{F} ¿Qué interés probable tiene el autor de la fuente B? A) defender la Constitución que impulsó su gobierno, B) criticar la Constitución, C) informar sin tomar posición.", "A", "Es vocero del gobierno militar que impulsó el texto."),
        ("{F} ¿Qué afirmación se puede comprobar en el texto constitucional? A) las Fuerzas Armadas son garantes del orden institucional, B) las Fuerzas Armadas limitan la soberanía popular, C) la Constitución asegura que las instituciones no caerán.", "A", "Las otras dos son valoraciones de sus autores."),
        ("Una estudiante cita la fuente B como prueba de que «todos los chilenos apoyaban la Constitución». ¿Qué error comete? A) usa la declaración de un solo actor interesado para hablar de todos, B) usa una fuente demasiado nueva, C) cita directamente el texto constitucional.", "A", "Una voz interesada no representa a toda la sociedad."),
        ("Para saber qué disponía el texto sobre las Fuerzas Armadas, ¿qué fuente conviene usar primero? A) la fuente A, porque resume la norma, B) la fuente B, porque la emite un vocero.", "A", "El texto constitucional es la fuente primaria sobre la norma."),
        ("{F} Clasifica cada fuente como texto constitucional (T) o declaración de un actor (D): a) fuente A, b) fuente B, c) fuente C. Responde con las tres letras.", "a) T, b) D, c) D", "Solo la fuente A resume la norma."),
        ("Los comandantes en jefe tenían inamovilidad. ¿Qué significa? A) que el Presidente no podía removerlos libremente durante su período, B) que no podían salir del país.", "A", "Inamovilidad es no poder ser removido de un cargo durante un período."),
        ("{F} Las fuentes B y C se contradicen. ¿Qué lo explica mejor? A) los autores tienen intereses y posiciones distintas frente a la Constitución, B) una de las dos miente siempre, C) una pertenece a otro país.", "A", "Cada actor mira la norma desde su posición."),
        ("Un compañero dice: «Como las Fuerzas Armadas eran garantes, nunca respondieron ante autoridades elegidas». ¿Qué necesita para sostenerlo? A) revisar otras partes del texto y estudios sobre cómo se aplicó, B) nada, porque la fuente A lo demuestra.", "A", "La fuente A no dice nada sobre el control de las autoridades."),
        ("=", "En una encuesta de ejemplo (dato inventado para este cuaderno) 200 personas opinaron sobre la función tutelar y 120 dijeron estar de acuerdo. ¿Qué porcentaje de acuerdo hubo?", "120*100//200", "Se divide el acuerdo por el total y se multiplica por 100.", "%"),
        ("{F} Elige la conclusión mejor sostenida por las tres fuentes. A) la función tutelar fue valorada de forma opuesta por actores con intereses distintos, B) todos los actores aceptaban la función tutelar.", "A", "Las fuentes B y C expresan posiciones contrarias."),
    ],
    ctx=("Para un trabajo sobre las Fuerzas Armadas y la Constitución, una estudiante debe elegir su primera fuente. ¿Cuál es la más adecuada para saber qué establecía la norma? A) un artículo de opinión de un diario, B) el texto constitucional.", "B", "Es la fuente primaria y oficial sobre lo que establecía la norma."),
    sc=[("En Historia: ¿qué es la soberanía popular?", "La idea de que el poder reside en el pueblo y se ejerce mediante el voto", "Es el principio que la oposición dijo que se limitaba."),
        ("¿Qué es una función tutelar?", "El papel de proteger o vigilar el orden institucional", "Tutelar significa proteger o vigilar."),
        ("¿Por qué una declaración no reemplaza al texto?", "Porque interpreta y valora desde la posición de su autor", "El texto dice lo que la norma establece.")],
    op=("{F} Elige dos fuentes y completa para cada una: tipo (texto constitucional o declaración), autor, interés probable y qué afirma. Termina con una frase que explique qué ganas al combinar las dos.",
        "Fuente A: texto constitucional; resume la norma; afirma que las Fuerzas Armadas son garantes del orden institucional. Fuente C: declaración de un grupo opositor; busca criticar; afirma que limita la soberanía popular. Juntas muestran la norma y una valoración.",
        ["clasifica las dos fuentes", "nombra autor e interés", "justifica el uso conjunto"], ["dos fuentes analizadas y una conclusión"], ["tratar una declaración como si fuera el texto constitucional", "no nombrar el interés del autor"], "Pide a una persona de tu casa que lea tu conclusión y diga si distingue texto y opinión."),
    reinforce="Elige una noticia reciente y anota quién la escribe y qué interés podría tener.",
    extend="Escribe una pregunta que estas tres fuentes no responden y qué fuente adicional necesitarías.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Datos de ejemplo (Senado ficticio): 47 integrantes, de los cuales 38 son elegidos por votación y 9 son designados por instituciones del Estado. Para aprobar una ley se necesita mayoría absoluta de los integrantes en ejercicio, es decir, más de la mitad. "
      "Voz A (senador elegido de oposición, de ejemplo): «Los designados no representan a los votantes». Voz B (senador designado, de ejemplo): «Aportamos experiencia y estabilidad al Senado». "
      "Descripción de ejemplo del Consejo de Seguridad Nacional: lo integraban autoridades civiles y los comandantes en jefe de las Fuerzas Armadas y el director de Carabineros, y podía hacer presente su opinión sobre hechos que, a su juicio, atentaran contra las bases de la institucionalidad.")
build(
    OA, 3, F3,
    use="Aprenderé a comparar cómo veían los senadores designados y el Consejo de Seguridad Nacional distintos actores, y a notar qué cambia si miro una institución o el sistema político completo. Sirve para evaluar si una regla afecta la representación.",
    prior=["Sé qué es una función tutelar.", "Sé qué es la soberanía popular.", "Sé calcular una mayoría simple con números pequeños."],
    explain=[
        "La Constitución de 1980 incluyó senadores designados: personas que llegaban al Senado no por votación de la ciudadanía, sino por decisión de instituciones del Estado, como la Corte Suprema o el Consejo de Seguridad Nacional. El Consejo de Seguridad Nacional reunía a autoridades civiles y a los comandantes de las Fuerzas Armadas y podía manifestar su opinión sobre hechos que, a su juicio, amenazaran las bases de la institucionalidad.",
        "Una perspectiva es el punto de vista de un actor según sus intereses. Quienes defendían a los senadores designados hablaban de experiencia y estabilidad; quienes los criticaban señalaban que no representaban a los votantes y podían inclinar votaciones. También importa la escala: dentro del Senado, nueve designados parecen pocos, pero en una votación estrecha pueden decidir el resultado.",
        "La representación es la relación por la cual una persona elegida actúa en nombre de quienes la eligieron. Los designados quedaban fuera de esa relación, porque no respondían ante votantes. Al evaluar una regla política conviene preguntar quién gana peso, quién lo pierde y si el efecto aparece solo en casos extremos o todos los días.",
    ],
    vocab=[("senador designado", "senador que llega al cargo por decisión de instituciones y no por votación"), ("Consejo de Seguridad Nacional", "organismo que reunía a autoridades civiles y militares y podía manifestar su opinión sobre la institucionalidad"), ("representación", "relación por la cual quien es elegido actúa en nombre de sus votantes"), ("mayoría absoluta", "más de la mitad de los integrantes en ejercicio"), ("escala", "nivel desde el que se observa un hecho: una institución, el país o el mundo")],
    worked=[
        ("Calcular la mayoría absoluta", "Una cámara de ejemplo tiene 31 integrantes. ¿Cuántos votos bastan para tener mayoría absoluta?",
         ["La mitad de 31 es 15,5.", "Se necesita más de la mitad, o sea 16 votos."], "16 votos"),
        ("Asociar perspectiva y actor", "Una frase de ejemplo dice: «Tengo experiencia y ayudo a estabilizar las decisiones». ¿Qué actor la diría con más probabilidad: un senador designado o uno de oposición elegido?",
         ["Defiende la presencia de los designados.", "El actor más interesado en defenderla es el designado."], "Un senador designado"),
    ],
    mistakes=[
        ("Pensar que nueve de cuarenta y siete es un número demasiado pequeño para importar.", "En votaciones estrechas puede decidir el resultado.", "Calcula cuántos votos faltan para la mayoría y compara con los designados."),
        ("Mezclar la opinión del Consejo de Seguridad Nacional con una orden obligatoria.", "El texto de ejemplo dice que podía manifestar su opinión, no que lo decidiera todo.", "Lee con precisión el verbo que usa la norma."),
    ],
    T=[
        ("En Historia: ¿qué es un senador designado?", "Un senador que llega al cargo por decisión de instituciones y no por votación", "No fue elegido por la ciudadanía."),
        ("{F} En ese Senado ficticio, ¿cuántos integrantes son elegidos por votación?", "38", "Los datos separan 38 elegidos y 9 designados."),
        ("{F} ¿Qué opinaba el senador de oposición sobre los designados? A) que no representaban a los votantes, B) que aportaban experiencia, C) que eran elegidos por votación.", "A", "Es lo que dice la voz A."),
        ("=", "{F} ¿Cuántos votos necesita una ley para obtener mayoría absoluta?", "47//2+1", "La mitad es 23 y se necesita más de la mitad, o sea 24 votos."),
        ("=", "{F} Si los 9 designados votan a favor de una ley, ¿cuántos elegidos faltan para llegar a la mayoría absoluta?", "24-9", "Se resta lo que aportan los designados a los votos necesarios."),
        ("{F} ¿Qué podía hacer el Consejo de Seguridad Nacional, según la descripción? A) manifestar su opinión sobre hechos que atentaran contra las bases de la institucionalidad, B) dictar leyes, C) elegir a los senadores elegidos.", "A", "La descripción solo habla de hacer presente su opinión."),
        ("{F} Una ley recibe 20 votos de elegidos y 9 de designados. ¿Obtiene mayoría absoluta? A) sí, B) no.", "A", "Suma 29 votos y la mayoría necesaria era 24."),
        ("=", "{F} Si 18 elegidos votan en contra y 20 votan a favor, y los 9 designados votan en contra, ¿cuántos votos suma el rechazo?", "18+9", "Se suman los elegidos y los designados que votan en contra."),
        ("{F} ¿Cuál de las dos voces defendería mantener los senadores designados? A) la voz A, B) la voz B.", "B", "La voz B destaca experiencia y estabilidad."),
        ("Un compañero dice: «Nueve designados de cuarenta y siete no pueden cambiar nada». ¿Qué cálculo lo desmiente? A) en una votación estrecha, 9 votos pueden decidir quién llega a los 24 necesarios, B) 9 es casi la mitad de 47.", "A", "El peso depende de lo estrecha que sea la votación."),
        ("{F} ¿Qué cambia al mirar la institución en vez del sistema político completo? A) en el Senado los designados son una minoría, pero en el sistema político afectan la representación de toda la ciudadanía, B) nada cambia nunca.", "A", "Los efectos varían según la escala."),
        ("=", "{F} Si el Senado tuviera 38 elegidos y los designados no existieran, ¿cuántos votos serían la mayoría absoluta?", "38//2+1", "La mitad de 38 es 19 y se necesita más de la mitad, o sea 20."),
        ("{F} Elige la conclusión mejor sostenida. A) los designados eran una minoría, pero podían pesar en votaciones estrechas y no respondían ante votantes, B) los designados eran irrelevantes porque eran pocos.", "A", "Combina el cálculo con el argumento sobre representación."),
    ],
    ctx=("Una profesora de ejemplo debe explicar a su curso por qué algunos críticos decían que los senadores designados afectaban la representación. ¿Qué argumento es el más preciso? A) no habían sido elegidos por los votantes y sus votos contaban igual que los de los elegidos, B) eran mayoría en el Senado.", "A", "En el Senado ficticio eran 9 de 47, no la mayoría, pero sus votos valían igual."),
    sc=[("En Historia: ¿qué es la representación política?", "La relación por la cual quien es elegido actúa en nombre de sus votantes", "Los designados quedaban fuera de esa relación."),
        ("¿Qué es la mayoría absoluta?", "Más de la mitad de los integrantes en ejercicio", "Es la regla del ejemplo."),
        ("¿Qué podía hacer el Consejo de Seguridad Nacional según la descripción?", "Manifestar su opinión sobre hechos que atentaran contra las bases de la institucionalidad", "La descripción usa el verbo manifestar, no decidir.")],
    op=("{F} Escribe un párrafo corto que compare la perspectiva de la voz A y la de la voz B, calcule cuántos votos faltaban a los designados para la mayoría absoluta y diga qué cambia al mirar el Senado o todo el sistema político.",
        "La voz A dice que los designados no representan a los votantes; la voz B dice que aportan experiencia y estabilidad. La mayoría es 24 y con 9 designados faltan 15 votos de elegidos. En el Senado son minoría, pero para el sistema político afectan la representación.",
        ["compara las dos perspectivas", "calcula 24 y 15 correctamente", "distingue dos escalas"], ["un párrafo con tres partes"], ["tomar partido sin comparar", "olvidar el cálculo de la mayoría"], "Lee tu párrafo a una persona de tu casa y pídele que diga cuál es tu tesis."),
    reinforce="Anota quién representa a tu curso y cómo fue elegido.",
    extend="Explica por qué la representación es distinta si alguien es elegido o designado.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Datos de ejemplo (Cámara ficticia de 120 integrantes en ejercicio): una ley simple se aprueba por mayoría de los presentes; una ley de cuórum calificado necesita la mayoría absoluta de los integrantes en ejercicio, o sea, más de la mitad de 120; "
      "una reforma de la Constitución exige tres quintos de los integrantes en ejercicio. "
      "Cronología básica: en 1989 hubo reformas constitucionales acordadas entre el gobierno militar y la oposición; en 2005 una reforma eliminó los senadores designados y la inamovilidad de los comandantes en jefe.")
build(
    OA, 4, F4,
    use="Aprenderé a relacionar el cuórum calificado con la dificultad de cambiar leyes y a explicar por qué la Constitución de 1980 se reformó varias veces. Sirve para entender cambios y continuidades.",
    prior=["Sé qué es una mayoría absoluta.", "Conozco la función tutelar y los senadores designados.", "Sé calcular fracciones de un número entero."],
    explain=[
        "El cuórum es el número mínimo de votos necesarios para aprobar una decisión. El cuórum calificado es más exigente que la mayoría simple: en el ejemplo, requiere la mayoría absoluta de los integrantes en ejercicio, no solo de los presentes. Subir el cuórum dificulta cambiar una norma, por eso se usa para proteger leyes consideradas importantes. También se puede fijar un cuórum muy alto para reformar la Constitución.",
        "Un cuórum alto puede proteger acuerdos de cambios apresurados, pero también puede bloquear cambios que una mayoría quiere. En la Constitución de 1980 esto se combinó con otras reglas, como los senadores designados, y volvió difícil modificarla sin acuerdo con los sectores que la defendían. Por eso importan las reformas de 1989, que fueron negociadas, y la de 2005, que eliminó los designados y la inamovilidad de los comandantes en jefe.",
        "Para explicar un cambio hay que distinguir causas, que lo producen, de coincidencias. Fueron causas de reforma la negociación entre gobierno y oposición en 1989, la presión por completar la democracia y los acuerdos políticos posteriores. También hay continuidades: la Constitución siguió vigente con su estructura general, aunque modificada. Cambio y continuidad pueden convivir en el mismo texto.",
    ],
    vocab=[("cuórum", "número mínimo de votos necesarios para aprobar una decisión"), ("cuórum calificado", "exigencia de votos mayor que la mayoría simple"), ("reforma constitucional", "modificación del texto de la Constitución mediante el procedimiento que ella misma fija"), ("cambio", "aspecto que se modifica entre dos momentos"), ("continuidad", "aspecto que permanece entre dos momentos")],
    worked=[
        ("Calcular un cuórum calificado", "Una cámara de ejemplo tiene 80 integrantes en ejercicio. ¿Cuántos votos exige la mayoría absoluta?",
         ["La mitad de 80 es 40.", "Se necesita más de la mitad: 41 votos."], "41 votos"),
        ("Separar cambio y continuidad", "Un texto de ejemplo cuenta que, tras una reforma, desaparecen los cargos designados, pero se mantienen el Congreso y los tribunales. ¿Qué cambió y qué continuó?",
         ["Los cargos designados desaparecieron.", "El Congreso y los tribunales siguieron existiendo."], "Cambió la designación de cargos; continuaron las instituciones"),
    ],
    mistakes=[
        ("Creer que un cuórum más alto siempre es mejor.", "Protege acuerdos, pero también puede impedir reformas que una mayoría respalda.", "Evalúa qué protege y qué bloquea."),
        ("Pensar que, si hubo reformas, la Constitución dejó de ser la de 1980.", "El texto vigente conserva su estructura con modificaciones, de modo que hay cambio y continuidad.", "Compara artículo por artículo antes de concluir."),
    ],
    T=[
        ("En Historia: ¿qué es un cuórum?", "El número mínimo de votos necesarios para aprobar una decisión", "Es el requisito para que una votación valga."),
        ("{F} ¿Cuántos integrantes en ejercicio tiene esa Cámara?", "120", "El dato está al inicio de la ficha."),
        ("{F} ¿Qué año se produjo la reforma que eliminó los senadores designados? A) 1989, B) 2005.", "B", "La cronología dice que fue en 2005."),
        ("=", "{F} ¿Cuántos votos exige una ley de cuórum calificado (más de la mitad de 120)?", "120//2+1", "La mitad es 60 y se necesita más de la mitad."),
        ("=", "{F} ¿Cuántos votos exige una reforma constitucional (tres quintos de 120)?", "120*3//5", "Se divide 120 por 5 y se multiplica por 3."),
        ("{F} ¿Cuál exigencia es más difícil de alcanzar? A) la ley de cuórum calificado, B) la reforma constitucional.", "B", "Exige más votos que la mayoría absoluta."),
        ("=", "{F} En una votación, 70 integrantes votan a favor de una reforma constitucional. ¿Cuántos votos le faltan para aprobarla?", "120*3//5-70", "Se resta lo obtenido a los votos exigidos."),
        ("{F} Un diputado dice: «Con 70 votos aprobamos una ley de cuórum calificado». ¿Tiene razón? A) sí, porque supera los 61 votos exigidos, B) no, porque necesita 80.", "A", "La mayoría absoluta de 120 es 61."),
        ("En una votación de ejemplo hay 100 presentes, pero 120 integrantes en ejercicio. Una ley de cuórum calificado se aprueba con 55 votos. ¿Qué error comete quien dice que se aprobó? A) olvida que se mide sobre los integrantes en ejercicio y se requieren 61, B) cree que los presentes valen más que los ausentes.", "A", "Con 55 votos no llega a más de la mitad de 120."),
        ("{F} ¿Qué relación hay entre los cuórums altos y los cambios a la Constitución? A) dificultan cambiarla sin acuerdo entre sectores, B) permiten cambiarla con la mayoría simple de los presentes.", "A", "Exigen más votos y, por tanto, más acuerdo."),
        ("{F} ¿Cuál es una causa de las reformas de 1989? A) la negociación entre el gobierno militar y la oposición, B) la creación de los senadores designados.", "A", "Las reformas fueron acordadas entre ambos sectores."),
        ("{F} ¿Qué diferencia hay entre las reformas de 1989 y la de 2005? A) la de 1989 fue acordada entre el gobierno militar y la oposición y la de 2005 eliminó los senadores designados, B) la de 1989 eliminó los senadores designados y la de 2005 fue acordada con el gobierno militar.", "A", "Según la cronología, los designados se eliminaron en 2005."),
        ("{F} Elige la conclusión mejor sostenida. A) la Constitución cambió con reformas, pero conservó su estructura general, B) la Constitución fue reemplazada por una completamente nueva en 1989.", "A", "Hay cambios y continuidades en el mismo texto."),
    ],
    ctx=("Un centro de estudiantes de ejemplo quiere reformar su reglamento y debate el cuórum. Una propuesta exige mayoría simple; otra, tres quintos. ¿Qué ventaja tiene la segunda? A) protege el reglamento de cambios apresurados y obliga a buscar acuerdos, B) permite cambiarlo con menos votos.", "A", "Un cuórum más alto exige más acuerdo."),
    sc=[("En Historia: ¿qué es un cuórum calificado?", "Una exigencia de votos mayor que la mayoría simple", "Se usa para proteger normas importantes."),
        ("¿Qué es una reforma constitucional?", "La modificación del texto de la Constitución mediante el procedimiento que ella misma fija", "Debe seguir las reglas de la propia Constitución."),
        ("¿Qué diferencia hay entre cambio y continuidad?", "El cambio es lo que se modifica entre dos momentos y la continuidad es lo que permanece", "Ambos conviven en un mismo texto.")],
    op=("{F} Escribe un párrafo corto que calcule cuántos votos exigen una ley de cuórum calificado y una reforma constitucional en la Cámara de 120, nombre una causa de reforma, un cambio y una continuidad.",
        "Una ley de cuórum calificado exige 61 votos y una reforma, 72. Una causa de reforma fue la negociación de 1989. Cambió la presencia de senadores designados, que se eliminó en 2005. Continuó la Constitución con su estructura general.",
        ["calcula 61 y 72", "nombra una causa", "distingue cambio y continuidad"], ["un párrafo con tres elementos"], ["calcular sobre los presentes y no sobre los integrantes en ejercicio", "no mencionar ninguna continuidad"], "Pide a una persona de tu casa que verifique tus cálculos."),
    reinforce="Explica con un ejemplo de tu curso qué diferencia hay entre aprobar por mayoría simple y con dos tercios.",
    extend="Escribe una ventaja y un riesgo de exigir cuórums altos para cambiar una constitución.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Tabla de ejemplo, resumen redactado para este cuaderno: "
      "Senadores designados: existían en 1980; fueron eliminados en la reforma de 2005. "
      "Fuerzas Armadas como garantes del orden institucional: figuraba en el texto de 1980; la reforma de 2005 eliminó esa expresión. "
      "Inamovilidad de los comandantes en jefe: existía en 1980; la reforma de 2005 la eliminó. "
      "Consejo de Seguridad Nacional: en 1980 podía hacer presente su opinión sobre hechos que atentaran contra la institucionalidad; tras 2005 pasó a ser un organismo asesor. "
      "Constitución vigente: sigue siendo la de 1980, con modificaciones, y su texto fue ordenado en un texto refundido en 2005.")
build(
    OA, 5, F5,
    use="Aprenderé a construir una interpretación documentada sobre qué cambió y qué continúa de la Constitución de 1980. Sirve para apoyar una conclusión con evidencia y no con impresiones.",
    prior=["Conozco las instituciones de 1980: transitorios, cuórum, senadores designados, función tutelar y Consejo.", "Sé distinguir cambio y continuidad.", "Sé citar un dato como evidencia."],
    explain=[
        "Una interpretación documentada es una explicación que se apoya en evidencia citada. Para construirla se hace una afirmación, se señalan las fuentes y se explica cómo la evidencia sostiene la afirmación. También se indica un límite: lo que la evidencia no permite decir. Por ejemplo, una tabla de cambios muestra qué se modificó, pero no mide cuánto cambió la vida cotidiana.",
        "Al comparar el texto de 1980 con el vigente se ve una mezcla. Cambiaron elementos centrales de la institucionalidad, como los senadores designados, la expresión garantes del orden institucional, la inamovilidad de los comandantes y el carácter del Consejo de Seguridad Nacional. Continuó la Constitución como texto vigente, con su estructura general y su origen en 1980, aunque modificada.",
        "Al redactar una interpretación se evita el anacronismo, que consiste en juzgar el pasado con ideas o hechos posteriores como si ya existieran. Se separa lo que dice el texto de 1980 de lo que dice el vigente. Y se evita la afirmación absoluta: decir que todo cambió o que nada cambió casi nunca tiene sustento.",
    ],
    vocab=[("interpretación documentada", "explicación apoyada en evidencia citada y con sus límites indicados"), ("evidencia", "dato o fuente que sostiene una afirmación"), ("texto refundido", "texto que reúne en un solo documento una norma y sus modificaciones"), ("anacronismo", "error de juzgar el pasado con hechos o ideas que aún no existían"), ("límite", "aquello que la evidencia no permite afirmar")],
    worked=[
        ("Armar una afirmación con evidencia", "Con la tabla, ¿qué afirmación está bien documentada: «En 2005 se eliminaron los senadores designados» o «Todo cambió en 2005»?",
         ["La primera cita un hecho que aparece en la tabla.", "La segunda es absoluta y la tabla muestra continuidades."], "«En 2005 se eliminaron los senadores designados»"),
        ("Detectar un anacronismo", "Un texto de ejemplo dice: «En 1980 los senadores designados ya habían sido eliminados». ¿Qué error contiene?",
         ["La eliminación ocurrió en 2005.", "Atribuye a 1980 un hecho posterior."], "Es un anacronismo: atribuye a 1980 un cambio de 2005"),
    ],
    mistakes=[
        ("Afirmar sin matices que la Constitución actual es una completamente distinta a la de 1980.", "Formalmente sigue siendo el mismo texto con modificaciones y texto refundido en 2005, aunque se debate cuánto cambió.", "Cita qué se mantuvo y qué se modificó."),
        ("Escribir una conclusión sin indicar ninguna evidencia.", "Sin evidencia no se puede comprobar la afirmación.", "Añade el dato de la tabla que la sostiene."),
    ],
    T=[
        ("En Historia: ¿qué es una interpretación documentada?", "Una explicación apoyada en evidencia citada, con sus límites indicados", "Evita afirmar sin pruebas."),
        ("{F} ¿En qué año se eliminaron los senadores designados? A) 1980, B) 2005.", "B", "La tabla lo indica para la reforma de 2005."),
        ("{F} ¿Qué pasó con la inamovilidad de los comandantes en jefe? A) se eliminó en 2005, B) se creó en 2005.", "A", "Existía en 1980 y la reforma la eliminó."),
        ("{F} ¿En qué se convirtió el Consejo de Seguridad Nacional después de 2005? A) en un organismo asesor, B) en un tribunal, C) en un órgano que dicta leyes.", "A", "La tabla indica que pasó a ser asesor."),
        ("{F} ¿Cuál de estos elementos de 1980 sigue igual según la tabla? A) la Constitución como texto vigente, con modificaciones, B) la inamovilidad de los comandantes.", "A", "Lo único que la tabla da como continuidad es el texto vigente; la inamovilidad se eliminó."),
        ("{F} ¿Cuál de estas afirmaciones es una continuidad? A) la Constitución sigue vigente con modificaciones, B) los senadores designados siguen existiendo, C) los comandantes mantienen su inamovilidad.", "A", "La tabla indica que el texto sigue vigente con modificaciones."),
        ("Una estudiante escribe: «En 1980 ya no existían senadores designados». ¿Qué error comete? A) afirma lo contrario de lo que muestra la tabla: existían y se eliminaron en 2005, B) confunde la reforma de 2005 con la de 1989.", "A", "En 1980 sí existían; se eliminaron después."),
        ("{F} Elige la afirmación mejor documentada. A) la reforma de 2005 eliminó los senadores designados y la inamovilidad, B) la reforma de 2005 hizo desaparecer la Constitución de 1980.", "A", "La primera cita hechos de la tabla."),
        ("{F} ¿Cuántos elementos de la institucionalidad aparecen en la tabla como cambiados por la reforma de 2005 (senadores designados, garantes, inamovilidad y Consejo)? A) cuatro, B) dos.", "A", "La tabla cita esos cuatro elementos."),
        ("Un texto de ejemplo dice: «Como los designados ya no existen, la Constitución es completamente nueva». ¿Qué problema tiene? A) exagera, porque el texto sigue siendo el de 1980 con modificaciones, B) subestima las reformas.", "A", "La evidencia muestra cambio y continuidad."),
        ("{F} Para saber cuánto cambió la vida cotidiana de las personas, ¿es suficiente la tabla? A) no, porque muestra cambios institucionales pero no mide efectos en la vida diaria, B) sí, porque cita todas las reformas.", "A", "Es un límite de la fuente."),
        ("{F} Una estudiante afirma: «El Consejo de Seguridad Nacional se eliminó en 2005». ¿Qué dice la tabla? A) pasó a ser un organismo asesor, B) se eliminó, como los senadores designados.", "A", "La tabla distingue lo eliminado de lo que cambió de carácter."),
        ("{F} ¿Qué conclusión está mejor documentada? A) cambiaron elementos centrales de la institucionalidad, pero la Constitución sigue vigente con su estructura general, B) nada cambió.", "A", "Combina cambios y continuidades que cita la tabla."),
    ],
    ctx=("Una estudiante prepara una exposición. Quiere afirmar que la reforma de 2005 cambió la institucionalidad. ¿Qué evidencia cita? A) la eliminación de los senadores designados y de la inamovilidad, B) la edad del Presidente de turno.", "A", "Son hechos de la tabla relacionados con la institucionalidad."),
    sc=[("En Historia: ¿qué es un anacronismo?", "Juzgar el pasado con hechos o ideas que aún no existían", "Atribuye a una época algo que ocurrió después."),
        ("¿Qué es un texto refundido?", "Un texto que reúne en un solo documento una norma y sus modificaciones", "Facilita leer la norma vigente."),
        ("¿Por qué una interpretación debe indicar un límite?", "Porque muestra lo que la evidencia no permite afirmar", "Evita conclusiones exageradas.")],
    op=("{F} Escribe tu interpretación en cuatro frases: una afirmación, una evidencia de la tabla, un cambio con su año y un límite de lo que la tabla no permite decir.",
        "La Constitución de 1980 cambió, pero sigue vigente. Evidencia: la tabla dice que continúa con modificaciones. Un cambio: en 2005 se eliminaron los senadores designados. Límite: la tabla no mide cómo cambió la vida cotidiana.",
        ["incluye una afirmación y una evidencia", "da un cambio con año", "indica un límite"], ["cuatro frases"], ["afirmar que todo cambió", "olvidar el límite"], "Pide a una persona de tu casa que marque la evidencia en tu texto."),
    reinforce="Escribe una afirmación sobre tu comuna y la evidencia que la sostendría.",
    extend="Explica por qué un texto refundido puede inducir a pensar que es una constitución nueva.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 6
F6 = ("Dos posturas de ejemplo, redactadas para este cuaderno. Postura A: «Las reformas posteriores a 1980 eliminaron los elementos más cuestionados, así que la Constitución actual es legítima aunque su origen haya sido en dictadura». "
      "Postura B: «Las reformas no cambian el origen del texto y por eso una constitución elaborada en democracia sería más legítima». "
      "Dato adicional: en 2022 y en 2023 se sometieron a plebiscito dos propuestas de nueva Constitución y en ambos casos fueron rechazadas por la ciudadanía.")
build(
    OA, 6, F6,
    use="Aprenderé a debatir con evidencia si cambió lo suficiente la Constitución de 1980 y a reconocer los límites de cada argumento. Sirve para participar en un debate público sin descalificar.",
    prior=["Conozco los cambios de 1989 y de 2005.", "Sé distinguir cambio y continuidad.", "Sé que un argumento necesita evidencia."],
    explain=[
        "Un debate histórico no busca ganar, sino comprender qué sostiene cada postura. Un argumento tiene una tesis, es decir, una afirmación, y razones o evidencias que la apoyan. Un contraargumento reconoce una razón de la otra postura y la responde. Hay que distinguir el origen de una norma, es decir, cómo y por quién fue creada, de su contenido actual.",
        "Quienes defienden la legitimidad de la Constitución actual destacan las reformas, el uso del procedimiento previsto y que los sectores políticos las aceptaron. Quienes cuestionan su legitimidad destacan que su origen fue en dictadura y que el texto no nació de un proceso democrático. Ambas posturas pueden usar datos ciertos y llegar a conclusiones distintas, porque ponen el peso en criterios diferentes.",
        "Los procesos de 2022 y 2023 muestran que intentar cambiar la Constitución es una decisión compleja: ambas propuestas fueron rechazadas en plebiscito, lo que no dice por sí solo qué razones tuvo cada votante. Un buen debate indica sus límites: no atribuye a todos una misma intención, no usa un dato para probar más de lo que muestra y reconoce que quedan preguntas abiertas.",
    ],
    vocab=[("tesis", "afirmación principal que se sostiene en un argumento"), ("contraargumento", "respuesta que reconoce una razón de otra postura y la rebate"), ("legitimidad", "reconocimiento social de que una autoridad o norma es justa o válida"), ("origen", "cómo y por quién fue creada una norma"), ("criterio", "regla o valor con que se juzga algo")],
    worked=[
        ("Identificar la tesis", "Postura de ejemplo: «El origen en dictadura importa más que las reformas posteriores». ¿Cuál es su tesis?",
         ["La tesis es la afirmación principal.", "Afirma que el origen pesa más que las reformas."], "El origen en dictadura pesa más que las reformas"),
        ("Redactar un contraargumento", "Contra la tesis anterior, ¿qué contraargumento reconoce una razón y la rebate?",
         ["Reconozco la razón: el origen fue en dictadura.", "Rebato: las reformas modificaron elementos centrales y cambiaron el texto actual."], "Reconoce el origen y señala que las reformas cambiaron elementos centrales"),
    ],
    mistakes=[
        ("Dar por seguro por qué rechazaron los votantes de 2022 y 2023 las propuestas.", "El resultado de un plebiscito no explica las razones de cada persona.", "Habla solo de lo que prueba el dato: que fueron rechazadas."),
        ("Descalificar a quien piensa distinto en vez de rebatir su argumento.", "Una descalificación no responde a ninguna razón.", "Responde con evidencia a la razón que presentó."),
    ],
    T=[
        ("En Historia: ¿qué es una tesis?", "La afirmación principal que se sostiene en un argumento", "Se apoya luego con razones y evidencias."),
        ("{F} ¿Qué sostiene la postura A? A) que la Constitución actual es legítima aunque su origen fuera en dictadura, B) que la Constitución actual no tuvo reformas, C) que se rechazó dos veces.", "A", "Es su tesis."),
        ("{F} ¿Qué sostiene la postura B? A) que el origen no cambia con las reformas, B) que las reformas bastan para dar legitimidad.", "A", "Dice que las reformas no cambian el origen del texto."),
        ("{F} ¿Qué dato adicional se menciona en la ficha? A) dos propuestas de nueva Constitución fueron rechazadas en plebiscito, B) la Constitución se aprobó por unanimidad.", "A", "Está en el dato adicional."),
        ("{F} ¿Qué prueba el dato de los plebiscitos de 2022 y 2023? A) que ambas propuestas fueron rechazadas, B) que todos quienes votaron defendían la Constitución de 1980.", "A", "El resultado no dice las razones de cada votante."),
        ("{F} ¿Qué criterio pone la postura B por encima de las reformas? A) el origen del texto, B) el cuórum de reforma.", "A", "Dice que las reformas no cambian el origen."),
        ("{F} ¿Cuál es el mejor contraargumento a la postura B? A) reconoce que el origen fue en dictadura y señala que las reformas cambiaron elementos centrales del texto, B) afirma que quien piensa así no entiende la historia.", "A", "Responde con una razón; la otra opción solo descalifica."),
        ("Un compañero dice: «Como las dos propuestas fueron rechazadas, todos los votantes defendían la Constitución de 1980». ¿Qué error comete? A) atribuye a todos una misma razón, que el resultado no demuestra, B) usa un plebiscito como fuente.", "A", "Un resultado no explica las intenciones individuales."),
        ("{F} Una compañera dice que la reforma de 2005 llegó tarde. ¿Qué necesita para sostenerlo? A) un criterio (por ejemplo, cuánto tiempo se tardó en eliminar elementos cuestionados) y evidencia, B) repetirlo con más seguridad.", "A", "Una opinión se vuelve argumento con criterio y evidencia."),
        ("{F} ¿Qué parte de la postura A reconoce una razón de la postura B? A) acepta que el origen fue en dictadura, B) niega que haya habido reformas.", "A", "Dice «aunque su origen haya sido en dictadura»."),
        ("{F} ¿Por qué ambas posturas pueden usar datos ciertos y concluir distinto? A) porque ponen el peso en criterios diferentes, como el origen o el contenido actual, B) porque una usa datos falsos.", "A", "Cada una da prioridad a un criterio."),
        ("{F} Según la explicación, ¿qué debe indicar un buen debate? A) sus límites: no atribuir a todos la misma intención y no probar más de lo que muestra un dato, B) solo las razones a favor de la propia postura.", "A", "Reconocer límites fortalece el argumento."),
        ("{F} Elige la conclusión con mejor sustento. A) hay acuerdo en que hubo cambios importantes y desacuerdo en cuánto pesan el origen y las reformas, B) todos están de acuerdo en todo.", "A", "Muestra lo que comparten las posturas y dónde se separan."),
    ],
    ctx=("En un debate escolar de ejemplo, una estudiante responde a su compañero sin descalificarlo: «Entiendo que el origen importa. Aun así, las reformas de 2005 eliminaron los senadores designados». ¿Qué hace? A) presenta un contraargumento con evidencia, B) cambia de tema.", "A", "Reconoce una razón y responde con un dato."),
    sc=[("En Historia: ¿qué es un contraargumento?", "Una respuesta que reconoce una razón de otra postura y la rebate", "Combina reconocimiento y respuesta."),
        ("¿Qué es la legitimidad?", "El reconocimiento social de que una autoridad o norma es justa o válida", "No depende solo del texto."),
        ("¿Qué demuestra que dos propuestas fueran rechazadas en plebiscito?", "Solo que fueron rechazadas, no las razones de cada votante", "El resultado no explica las intenciones.")],
    op=("{F} Elige una postura, escribe tu tesis, una razón con evidencia, un contraargumento a la otra postura y un límite de tu argumento.",
        "Tesis: la Constitución actual es legítima por sus reformas. Razón: se eliminaron los senadores designados en 2005. Contraargumento: aunque el origen fue en dictadura, el texto cambió. Límite: no sé las razones de los votantes de 2022 y 2023.",
        ["escribe una tesis clara", "incluye una razón con evidencia", "responde a la otra postura", "indica un límite"], ["cuatro frases"], ["descalificar a la otra postura", "no indicar límite"], "Lee tu argumento a una persona de tu casa y pídele que diga qué opina del contraargumento."),
    reinforce="Escribe con tus palabras qué diferencia hay entre el origen de una norma y su contenido actual.",
    extend="Explica por qué dos personas pueden tener el mismo dato y llegar a conclusiones diferentes.",
    materials=MAT,
)
