"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 18 (conceptos políticos clásicos, medievales y actuales)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 18"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a contextualizar y comparar los conceptos de ciudadanía y democracia en el mundo clásico y en la actualidad. Sirve para no creer que una palabra significa siempre lo mismo.",
    ["Sé que en Atenas y Roma había ciudadanos con derechos.", "Sé que hoy se vota en elecciones."],
    [
        "Una misma palabra puede significar cosas distintas según la época. La ciudadanía es la condición de la persona que tiene derechos y deberes políticos en una comunidad. En Atenas, la ciudadanía era de los varones adultos nacidos de padres atenienses, y se ejercía participando en la Asamblea. En Roma, ser ciudadano daba derechos legales y, para quienes tenían el voto, derechos políticos. En ambos casos quedaban fuera mujeres y esclavos.",
        "En Chile hoy, la ciudadanía incluye a las personas de nacionalidad chilena de 18 años o más, sin distinción de sexo. Pueden votar, ser elegidas y participar en la vida pública. La democracia es el sistema en que el pueblo decide, ahora principalmente por medio de representantes elegidos en votaciones periódicas. Existen también formas de participación directa, como los plebiscitos.",
        "La comparación muestra continuidades y cambios. Se mantiene la idea de que los ciudadanos tienen derechos y participan en las decisiones. Cambiaron quién cuenta como ciudadano y cómo se decide: de la Asamblea directa de pocos a las elecciones de representantes para una gran mayoría. Antes de comparar hay que definir la palabra en cada época.",
    ],
    [("ciudadanía", "condición de quien tiene derechos y deberes políticos en una comunidad"), ("democracia", "sistema en que el pueblo decide, directamente o por medio de representantes"), ("representante", "persona elegida para decidir en nombre de otros"), ("plebiscito", "votación en que la ciudadanía decide directamente una pregunta"), ("sufragio", "derecho a votar"), ("elección", "votación para escoger personas para un cargo")],
    [
        ("Contextualizar el concepto", "En Atenas, una mujer libre nacida de padres atenienses, ¿tenía ciudadanía política con voto?", ["Las mujeres estaban excluidas.", "No tenía voto."], "No"),
        ("Contextualizar hoy", "En Chile, un joven chileno de 19 años, ¿es ciudadano con derecho a voto?", ["Tiene más de 18 años.", "Es chileno.", "Sí tiene derecho."], "Sí"),
    ],
    [
        ("Pensar que «ciudadano» significa lo mismo en todas las épocas.", "En Atenas era una minoría de varones; hoy incluye a casi toda la población adulta nacional.", "Define el concepto antes de comparar."),
        ("Creer que la democracia actual es igual a la ateniense.", "Hoy es sobre todo representativa y con sufragio amplio; en Atenas era directa y excluyente.", "Nombra una continuidad y un cambio."),
    ],
    [
        ("¿A qué edad tienen hoy los chilenos ciudadanía para votar?", "18 años", "Así lo dice la explicación."),
        ("¿Cómo se llama el sistema en que el pueblo decide?", "Democracia", "Es la definición del vocabulario."),
        ("En la unidad de conceptos políticos, ¿qué es una elección?", "Una votación para escoger personas para un cargo", "Es la definición del vocabulario."),
    ],
    [
        ("En la unidad de conceptos políticos, ¿qué es un plebiscito?", "Una votación en que la ciudadanía decide directamente una pregunta", "Es la definición del vocabulario."),
        ("Nombra un grupo excluido de la ciudadanía ateniense.", "Mujeres, esclavos o metecos (cualquiera)", "La clase nombra grupos excluidos."),
        ("Nombra una continuidad en el concepto de ciudadanía.", "La idea de que los ciudadanos tienen derechos y participan en las decisiones", "La explicación la señala."),
    ],
    [
        ("Una ficha de ejemplo describe: «Todos los ciudadanos se reúnen en una plaza a votar una ley». ¿Es democracia directa o representativa?", "Directa", "Los ciudadanos deciden por sí mismos."),
        ("Una ficha de ejemplo describe: «Los ciudadanos eligen a sus diputados cada cuatro años». ¿Es democracia directa o representativa?", "Representativa", "Se eligen representantes."),
        ("Una ciudad de ejemplo tiene 1.000 habitantes adultos, pero solo 300 son ciudadanos con derecho a voto. ¿Cuántos quedan excluidos?", "700", "1.000 menos 300 son 700."),
    ],
    [
        ("Pedro dice: «En Atenas todos decidían las leyes». ¿Qué corrección haces con lo aprendido?", "Solo decidían los varones adultos nacidos de padres atenienses", "Muchos grupos estaban excluidos."),
        ("Marta dice: «Hoy la democracia es perfecta porque todos pueden votar». ¿Qué matiz agregas?", "Votar es un derecho amplio, pero la participación depende de muchos factores y siempre puede mejorar", "Evita idealizar el presente."),
    ],
    [
        ("Ordena de menor a mayor inclusión de la ciudadanía: A) Atenas clásica, B) Chile actual.", "A, B", "En Atenas la ciudadanía era una minoría; hoy incluye a casi todos los adultos nacionales."),
        ("Un estudiante escribe: «La palabra ciudadanía es la misma, así que su significado no cambió». ¿Qué error lógico comete?", "Confunde la palabra con su significado, que cambió", "Una palabra puede mantenerse con otro sentido."),
    ],
    [("Un estudiante lee dos frases: 1) «Los ciudadanos de Atenas votan en la Asamblea.» 2) «Los chilenos eligen a un presidente.» ¿Cuál es democracia directa y cuál representativa?", "1 directa; 2 representativa", "En la Asamblea se vota personalmente; el presidente representa a los votantes.")],
    [("En la unidad de conceptos políticos, ¿qué es la ciudadanía?", "La condición de quien tiene derechos y deberes políticos en una comunidad", "Es la definición del vocabulario."), ("En la unidad de conceptos políticos, ¿qué es un representante?", "Una persona elegida para decidir en nombre de otros", "Es la definición del vocabulario."), ("¿Qué hay que hacer antes de comparar un concepto?", "Definirlo en cada época", "Así no se confunden significados.")],
    (
        "Haz una tabla de dos columnas (Atenas y Chile hoy) con tres filas: quién es ciudadano, cómo se decide, qué derecho principal tiene. Usa solo datos de la clase. Escribe después tres líneas con una continuidad y un cambio.",
        "Atenas: varones adultos de padres atenienses; Asamblea directa; votar. Chile: nacionales de 18 años o más; elecciones y plebiscitos; votar.",
        ["completa seis casillas", "usa datos correctos", "escribe una continuidad y un cambio", "no idealiza"],
        ["tabla de seis casillas y tres líneas"],
        ["decir que ciudadano significa lo mismo", "idealizar la democracia actual"],
        "Muestra tu tabla a una persona de tu casa y pídele que explique la diferencia más grande.",
    ),
    "Anota qué derechos y deberes crees que tiene una persona ciudadana en tu comuna.",
    "Averigua qué es el padrón electoral y quién lo administra en Chile.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a comparar los conceptos de derecho y república en el mundo clásico y medieval con la actualidad. Sirve para entender de dónde vienen las ideas de ley y de república.",
    ["Sé qué es la ley y qué es un cargo temporal.", "Sé que Roma fue una república."],
    [
        "El derecho es el conjunto de normas que regulan la vida en sociedad y que una autoridad puede hacer cumplir. Los romanos desarrollaron un derecho muy elaborado: leyes escritas como las Doce Tablas, y después juristas que explicaban cómo aplicarlas. En el siglo VI, el emperador bizantino Justiniano hizo reunir ese derecho en un gran código, que se estudió en universidades medievales como Bolonia.",
        "En la Edad Media europea convivían varios derechos: el derecho romano estudiado en las universidades, las costumbres locales y el derecho de la Iglesia, llamado canónico. Hoy el derecho de Chile se basa en una Constitución, leyes escritas y tribunales independientes. Muchas ideas, como la igualdad ante la ley, se apoyan en esa herencia romana, aunque con cambios.",
        "La república, palabra que viene del latín «res publica» (cosa pública), designa un sistema en que el poder pertenece a la comunidad y los cargos son elegidos y, en general, temporales. En Roma, la república duró desde el 509 a.C. hasta el siglo I a.C. En la Edad Media hubo ciudades-república, como Venecia y Génova, gobernadas por consejos de ciudadanos ricos y un jefe llamado dux, elegido por ellos aunque en Venecia ocupaba el cargo de por vida; cada república tenía rasgos propios. Hoy Chile es una república: el presidente es elegido y gobierna por un tiempo limitado.",
    ],
    [("derecho", "conjunto de normas que regulan la vida en sociedad"), ("jurista", "persona que estudia y explica las leyes"), ("Constitución", "ley fundamental de un país"), ("república", "sistema donde el poder pertenece a la comunidad y los cargos son elegidos, del latín «cosa pública»"), ("derecho canónico", "leyes de la Iglesia"), ("dux", "jefe de la república de Venecia")],
    [
        ("Rastrear una palabra", "La palabra «república» viene del latín «res publica». ¿Qué significa «cosa pública»?", ["«Res» es cosa y «publica» es pública.", "Es lo que pertenece a la comunidad."], "Lo que pertenece a la comunidad"),
        ("Aplicar el concepto", "Un jefe elegido por un consejo para cinco años, en una ciudad gobernada por ciudadanos ricos. ¿Qué tipo de sistema es?", ["El cargo es temporal.", "Lo eligen ciudadanos.", "Es una república."], "Una república"),
    ],
    [
        ("Creer que el derecho nació en Chile.", "Muchas ideas del derecho chileno vienen del derecho romano a través de la tradición europea.", "Rastrea el origen de la idea."),
        ("Pensar que república significa lo mismo que ausencia de rey.", "Es un sistema de cargos temporales y poder de la comunidad; no solo la ausencia de rey.", "Define el concepto con rasgos."),
    ],
    [
        ("¿Cómo se llama la ley fundamental de un país?", "Constitución", "Es la definición del vocabulario."),
        ("¿Qué emperador bizantino hizo reunir el derecho romano en un código?", "Justiniano", "La explicación lo dice."),
        ("¿Cómo se llamaba el jefe de la república de Venecia?", "Dux", "Está en el vocabulario."),
    ],
    [
        ("¿Qué son las leyes de la Iglesia?", "El derecho canónico", "Es la definición del vocabulario."),
        ("¿Dónde se estudiaba el derecho romano en la Edad Media?", "En universidades como Bolonia", "La clase lo menciona."),
        ("Nombra dos repúblicas medievales.", "Venecia y Génova", "Son los ejemplos de la explicación."),
    ],
    [
        ("En una ciudad de ejemplo la ley escrita se aplica igual a ricos y pobres. ¿Qué idea del derecho muestra?", "La igualdad ante la ley", "La ley no distingue por riqueza."),
        ("Una ciudad medieval de ejemplo tiene un dux elegido por un consejo. ¿Qué tipo de gobierno es?", "Una ciudad-república", "Es gobernada por consejos de ciudadanos."),
        arith("El emperador Justiniano reunió el derecho romano en el siglo VI. ¿Cuántos siglos pasaron desde ese siglo hasta el siglo XXI?", "21-6", "Se restan los números de los siglos.", " siglos"),
    ],
    [
        ("Julia dice: «En la Edad Media solo existía un derecho». ¿Qué corrección haces?", "Convivían el derecho romano, las costumbres locales y el derecho canónico", "Había varios sistemas."),
        ("Pedro dice: «Venecia era una república solo porque no tenía rey». ¿Qué otro rasgo de la clase cumplía el dux?", "Era elegido por un consejo y no heredaba el cargo", "Ser república depende de cómo se elige el cargo, no solo de que no haya rey."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A) Constitución chilena, B) Doce Tablas, C) código de Justiniano.", "B, C, A", "Doce Tablas (450 a.C.), código de Justiniano (siglo VI) y Constitución chilena (siglo XX)."),
        ("Una afirmación dice: «Chile es una república porque tiene presidente». ¿Qué rasgo completa la definición de la clase?", "Que el presidente es elegido y su cargo es temporal", "No basta con tener presidente."),
    ],
    [("Un estudiante lee que en Chile todos deben cumplir las mismas leyes, el presidente dura cuatro años y hay tribunales. ¿Qué dos conceptos de la clase muestra?", "Derecho y república", "Normas iguales y cargos temporales.")],
    [("En la unidad de conceptos políticos, ¿qué es el derecho?", "El conjunto de normas que regulan la vida en sociedad", "Es la definición del vocabulario."), ("¿Qué significa «res publica»?", "Cosa pública", "Es la raíz de república."), ("¿Qué ejemplo de ciudad-república medieval da la clase?", "Venecia", "Se cita junto a Génova.")],
    (
        "Elige derecho o república y escribe un texto de seis líneas con: una definición, un ejemplo romano, un ejemplo medieval, un ejemplo actual y una continuidad con un cambio. Usa solo datos de la clase.",
        "Derecho: normas para la vida en sociedad. Romano: Doce Tablas. Medieval: derecho canónico. Actual: Constitución. Continuidad: igualdad ante la ley; cambio: tribunales independientes.",
        ["define el concepto", "da tres ejemplos de épocas distintas", "nombra una continuidad", "nombra un cambio"],
        ["texto de seis líneas con los cinco elementos"],
        ["mezclar ejemplos de épocas", "olvidar la definición"],
        "Lee tu texto a una persona de tu casa y pídele que diga en qué época está cada ejemplo.",
    ),
    "Escribe una norma de tu curso y explica por qué es una forma de derecho.",
    "Averigua cuántas constituciones ha tenido Chile y cuál es la vigente.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a examinar los conceptos de municipio y gremio en el mundo romano, medieval y actual. Sirve para entender cómo se organizaban las comunidades locales y los oficios.",
    ["Sé qué es un gremio medieval.", "Sé que una comuna es un territorio local."],
    [
        "El municipio, en Roma, era una ciudad incorporada al Estado romano que conservaba un gobierno local con magistrados y consejo, y cuyos habitantes tenían ciertos derechos romanos. En la Edad Media, muchas ciudades obtuvieron cartas que les permitían gobernarse mediante consejos y alcaldes. Hoy, en Chile, el municipio o municipalidad es el gobierno local de una comuna, dirigido por un alcalde y un concejo municipal, elegidos por votación cada cuatro años.",
        "El gremio, como ya vimos, era la asociación de artesanos de un mismo oficio en una ciudad medieval, con maestros, oficiales y aprendices, y reglas de calidad y precios. Hoy la palabra «gremio» se usa para organizaciones de personas de una misma actividad, como asociaciones de comerciantes o colegios profesionales, que defienden intereses y fijan estándares. A diferencia del gremio medieval, hoy la pertenencia no suele pasar de padres a hijos ni controla quién puede trabajar con tanta fuerza.",
        "Estas comparaciones muestran continuidades, como el gobierno local y la organización por oficio, y cambios, como la elección por voto, la igualdad de derechos y el control del Estado. Al comparar, se debe evitar pensar que el municipio actual es una copia del romano o que el gremio actual es igual al medieval.",
    ],
    [("municipio", "gobierno local de una ciudad o comuna"), ("alcalde", "autoridad que dirige el municipio"), ("concejo municipal", "grupo de personas elegidas que acompañan y controlan al alcalde"), ("comuna", "unidad territorial en que se divide el país en Chile"), ("gremio", "asociación de personas de un mismo oficio"), ("estándar", "regla o nivel mínimo de calidad que se acuerda")],
    [
        ("Identificar el concepto", "Una ficha de ejemplo dice: «Ciudad incorporada a Roma que conserva magistrados y consejo propios». ¿Qué concepto es?", ["Hay gobierno local.", "Es un municipio romano."], "Municipio"),
        ("Aplicar a hoy", "En Chile, el gobierno local de una comuna lo dirige un alcalde junto a un concejo. ¿Cómo se llama esa institución?", ["Está en el vocabulario.", "Se llama municipalidad."], "Municipalidad o municipio"),
    ],
    [
        ("Creer que el municipio actual es igual al romano.", "Se parecen en el gobierno local, pero hoy hay elecciones periódicas y derechos para todos.", "Compara continuidad y cambio."),
        ("Pensar que los gremios actuales son iguales a los medievales.", "Hoy no controlan tan fuertemente quién puede trabajar ni la pertenencia pasa de padres a hijos.", "Compara con criterios."),
    ],
    [
        ("¿Quién dirige el municipio en Chile?", "El alcalde", "Es el cargo del vocabulario."),
        ("¿Cada cuántos años se eligen alcalde y concejo en Chile, según la clase?", "Cada cuatro años", "La explicación lo dice."),
        ("En la unidad de conceptos políticos, ¿qué es una comuna?", "La unidad territorial en que se divide el país en Chile", "Es la definición del vocabulario."),
    ],
    [
        ("¿Qué conservaba un municipio romano?", "Un gobierno local con magistrados y consejo", "La clase lo explica."),
        ("En la unidad de conceptos políticos, ¿qué es un estándar?", "Una regla o nivel mínimo de calidad que se acuerda", "Es la definición del vocabulario."),
        ("Nombra un ejemplo actual de gremio.", "Una asociación de comerciantes o un colegio profesional", "Son los ejemplos de la clase."),
    ],
    [
        ("Una ficha de ejemplo dice: «La asociación de panaderos de una ciudad fija un precio mínimo del pan y la calidad». ¿Qué concepto es y de qué época se parece?", "Gremio; se parece a la época medieval", "Fija reglas de precio y calidad."),
        ("Un concejo municipal de ejemplo tiene 8 concejales y cada uno recibe 1.250 votos. ¿Cuántos votos suman?", "10.000", "Se multiplican concejales por votos."),
        ("En una comuna de ejemplo, el alcalde decide cerrar una calle sin consultar al concejo. ¿Qué institución debería controlarlo?", "El concejo municipal", "El concejo acompaña y controla al alcalde."),
    ],
    [
        ("Ana dice: «El gremio medieval y una asociación de comerciantes actual son lo mismo». ¿Qué diferencia puedes dar?", "El gremio medieval controlaba quién ejercía el oficio y la pertenencia solía heredarse; hoy no", "Cambió el control y la herencia."),
        ("Pedro dice: «En el municipio romano el alcalde era elegido por todas las personas como hoy». ¿Qué error comete?", "En Roma no votaban mujeres ni esclavos; hoy el voto es amplio", "Las condiciones eran distintas."),
    ],
    [
        ("Ordena de lo más local a lo más general: A) país, B) comuna, C) región.", "B, C, A", "La comuna es parte de la región y la región es parte del país."),
        ("¿Cuál de estos dos conceptos se organiza en torno a un mismo oficio: el municipio o el gremio?", "El gremio", "El municipio es gobierno local; el gremio reúne a personas del mismo oficio."),
    ],
    [("Un estudiante lee: «Cada cuatro años los vecinos eligen a su alcalde y a su concejo». ¿Qué concepto de la clase es y qué cambio con el municipio romano muestra?", "Municipio; el voto se extendió y hay elecciones periódicas", "Hoy el voto es amplio.")],
    [("En la unidad de conceptos políticos, ¿qué es un municipio?", "El gobierno local de una ciudad o comuna", "Es la definición del vocabulario."), ("En la unidad de conceptos políticos, ¿qué es un gremio?", "Una asociación de personas de un mismo oficio", "Es la definición del vocabulario."), ("¿Qué institución controla al alcalde?", "El concejo municipal", "Lo acompaña y lo controla.")],
    (
        "Escribe una comparación de seis líneas entre el municipio romano o medieval y el municipio de tu comuna, y entre el gremio medieval y una asociación actual de un oficio que conozcas. Incluye una continuidad y un cambio en cada comparación.",
        "Municipio: gobierno local con consejo; hoy hay alcalde y concejo elegidos. Gremio: reglas de oficio; hoy no se hereda.",
        ["compara municipio", "compara gremio", "incluye continuidad y cambio en cada uno", "usa datos de la clase"],
        ["texto de seis líneas con dos comparaciones"],
        ["decir que son idénticos", "no incluir cambios"],
        "Pide a una persona de tu casa que diga si en tu comuna conoce a algún concejal o alcalde y para qué sirve.",
    ),
    "Anota el nombre de tu comuna y cómo se llama la autoridad que la dirige (sin escribir datos personales).",
    "Averigua cuántos concejales tiene tu comuna y cómo se eligen.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a relacionar las continuidades y los cambios de los conceptos políticos desde el mundo clásico hasta hoy. Sirve para cerrar la unidad con una comparación bien fundada.",
    ["Conozco ciudadanía, democracia, derecho, república, municipio y gremio.", "Sé que una palabra puede cambiar de sentido."],
    [
        "Para comparar conceptos políticos, conviene hacer una tabla con tres columnas: mundo clásico, mundo medieval y actualidad. En cada fila se pone un concepto y se anota su significado, quiénes participaban y cómo se aplicaba. Luego se marcan continuidades (lo que se mantiene) y cambios (lo que se transforma).",
        "Algunos ejemplos: la ciudadanía pasó de ser un privilegio de pocos varones a un derecho amplio. La democracia pasó de la Asamblea directa a las elecciones de representantes. El derecho pasó de leyes y juristas romanos a una Constitución y tribunales independientes. La república pasó de cargos temporales en Roma y de jefes elegidos por consejos en repúblicas medievales a presidentes elegidos hoy. El municipio pasó de ser un gobierno local romano a la municipalidad con alcalde y concejo. El gremio pasó de controlar un oficio a ser una asociación que representa intereses.",
        "Un buen análisis explica por qué cambió cada concepto: el crecimiento de la población, las ideas de igualdad, los derechos humanos y las nuevas instituciones. También evita ideas falsas: ni «todo igual desde siempre» ni «el pasado no tiene relación con el presente». La conclusión debe nombrar ambas cosas.",
    ],
    [("continuidad", "rasgo que se mantiene en el tiempo"), ("cambio", "rasgo que se transforma"), ("tabla comparativa", "cuadro que ordena datos de varios casos para compararlos"), ("evolución", "transformación gradual de algo a lo largo del tiempo"), ("igualdad", "principio por el que todas las personas tienen los mismos derechos"), ("fundamentar", "apoyar una idea con datos o razones")],
    [
        ("Clasificar", "«La ciudadanía incluye hoy a casi todos los adultos nacionales, antes a una minoría.» ¿Es continuidad o cambio?", ["Cambió quién es ciudadano.", "Es cambio."], "Cambio"),
        ("Clasificar otra afirmación", "«Un cargo de república dura un tiempo limitado en la antigua Roma y hoy en Chile.» ¿Es continuidad o cambio?", ["Se mantiene la temporalidad.", "Es continuidad."], "Continuidad"),
    ],
    [
        ("Decir que nada cambió.", "Cambiaron quién participa, cómo se decide y qué derechos hay.", "Nombra al menos un cambio."),
        ("Decir que el pasado no tiene relación con el presente.", "Muchas palabras e ideas vienen del mundo clásico y medieval.", "Nombra al menos una continuidad."),
    ],
    [
        ("¿Cuántas columnas tiene la tabla comparativa de la clase?", "Tres", "Mundo clásico, mundo medieval y actualidad."),
        ("¿Qué concepto pasó de la Asamblea directa a las elecciones de representantes?", "La democracia", "Así lo dice la explicación."),
        ("¿Qué significa «fundamentar»?", "Apoyar una idea con datos o razones", "Es la definición del vocabulario."),
    ],
    [
        ("¿Qué concepto pasó de ser un privilegio de pocos a un derecho amplio?", "La ciudadanía", "Así lo dice la explicación."),
        ("¿Qué institución local actual se parece al municipio romano en ser gobierno local?", "La municipalidad", "Ambos son gobiernos locales."),
        ("Nombra dos razones que explican los cambios de los conceptos.", "Dos de estas: crecimiento de la población, ideas de igualdad, derechos humanos, nuevas instituciones", "Son las razones de la clase."),
    ],
    [
        ("Completa con una continuidad: «En la Roma republicana y en Chile hoy, los cargos republicanos son…».", "Temporales", "Es el rasgo común de la república."),
        ("Completa con un cambio: «En Atenas votaban pocos; hoy…».", "Votan casi todas las personas adultas nacionales", "Cambió la amplitud de la ciudadanía."),
        ("Una tabla de ejemplo tiene tres filas y tres columnas completas. ¿Cuántas casillas hay?", "9", "3 por 3 son 9 casillas."),
    ],
    [
        ("Luis dice: «El gremio medieval y la asociación actual son idénticos». ¿Qué cambio de la clase puedes citar?", "Hoy no controlan tan fuertemente quién trabaja ni la pertenencia se hereda", "Cambió el control del oficio."),
        ("¿Por qué una conclusión debe nombrar continuidades y cambios a la vez?", "Porque el pasado tiene relación con el presente pero no es igual", "Evita dos errores."),
    ],
    [
        ("Ordena los pasos de una buena comparación: A) marcar continuidades y cambios, B) hacer la tabla, C) explicar por qué cambió, D) concluir.", "B, A, C, D", "Primero la tabla, luego se marcan, se explican las causas y se concluye."),
        ("Según la comparación de la clase, ¿de qué forma a qué forma cambió la democracia?", "De la Asamblea directa a las elecciones de representantes", "Es el cambio señalado en la explicación."),
    ],
    [("Un estudiante concluye: «Los conceptos políticos clásicos no sirven hoy». ¿Qué evidencia de la clase usa un compañero para corregirlo?", "Que conceptos como república, derecho y democracia vienen del mundo clásico y siguen usándose", "Esa permanencia muestra continuidad.")],
    [("En la unidad de conceptos políticos, ¿qué es una continuidad?", "Un rasgo que se mantiene en el tiempo", "Es la definición del vocabulario."), ("En la unidad de conceptos políticos, ¿qué es un cambio?", "Un rasgo que se transforma", "Es la definición del vocabulario."), ("¿Qué debe hacer una buena conclusión?", "Nombrar continuidades y cambios con razones", "Así se fundamenta.")],
    (
        "Completa una tabla con las columnas mundo clásico, mundo medieval y actualidad para tres conceptos a tu elección entre ciudadanía, democracia, derecho, república, municipio y gremio. Anota en una frase por casilla. Luego escribe una conclusión de cuatro líneas con una continuidad, un cambio y una razón del cambio.",
        "República: Roma, cargos temporales; Venecia, dux y consejo; Chile, presidente elegido. Continuidad: cargos temporales. Cambio: elección por voto amplio.",
        ["completa nueve casillas", "usa datos correctos", "nombra continuidad, cambio y razón", "evita anacronismos"],
        ["tabla de nueve casillas y conclusión de cuatro líneas"],
        ["mezclar épocas", "olvidar la razón del cambio"],
        "Muestra tu tabla a una persona de tu casa y pídele que diga qué concepto le parece que más cambió.",
    ),
    "Escribe qué concepto político te parece más importante hoy y por qué.",
    "Averigua cómo se llama el órgano que hace las leyes en Chile y cómo se elige.",
)
