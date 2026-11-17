"""Comprensión histórica del presente (electivo HC, 3.º y 4.º medio): OAC-01 (perspectivas historiográficas sobre cambios recientes en la sociedad chilena), clases 1 a 6. Comuna, fuentes y datos ficticios o de ejemplo."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada fuente, tabla o texto está escrito en el enunciado. "
             "Las fuentes, los autores y los datos son ficticios o de ejemplo (la comuna «Lomas del Sur» no existe) y sirven para practicar el método de la historia, no para aprender cifras. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es analizar y evaluar, no adivinar cuál es «la correcta». "
             "Cuando un tema toque derechos humanos o hechos dolorosos, se trata con sobriedad; si algo te afecta, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O1 = "HI-CHDP-3y4-OAC-01"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (fuentes de ejemplo, ficticias). Dos resúmenes sobre cómo cambió la participación en la comuna de Lomas del Sur desde el retorno a la democracia, en 1990, hasta 2020. "
     "Autora A (historiadora local): «En Lomas del Sur la vida cívica se reconstruyó desde los barrios: una junta de vecinos, un club de adultos mayores y un colectivo de mujeres abrieron espacios de conversación donde antes había silencio.» "
     "Autor B (historiador nacional): «Los cambios en comunas como Lomas del Sur responden sobre todo a decisiones del Estado central: nuevas leyes y programas obligaron a crear instancias de participación.»")
build(
    O1, 1, F,
    use="Aprenderé a contextualizar un cambio reciente de la sociedad chilena (actores, tiempo y espacio) y a reconocer qué perspectiva historiográfica adopta cada autor, para no confundir una interpretación con «lo que pasó».",
    prior=["Sé que la historia se construye a partir de fuentes.", "Distingo un hecho de una interpretación.", "He estudiado el retorno a la democracia como proceso general."],
    explain=[
        "La historiografía es el conjunto de estudios e interpretaciones que historiadoras e historiadores escriben sobre el pasado. Una perspectiva historiográfica es el modo de mirar un proceso: qué actores destaca, a qué escala lo estudia y qué fuentes prefiere. Dos autores pueden hablar del mismo período y contar historias distintas sin que uno de ellos mienta.",
        "Contextualizar es situar un hecho o un texto en su tiempo (cuándo y en qué período), su espacio (dónde y a qué escala: barrio, comuna, región o país) y entre sus actores (quiénes actúan: personas, grupos, instituciones). Los cambios recientes de la sociedad chilena que estudia este electivo tienen cuatro ejes: el fortalecimiento de la sociedad civil, el respeto a los derechos humanos, la búsqueda de menos desigualdad y la inclusión de nuevos grupos y movimientos sociales.",
        "La sociedad civil es el conjunto de organizaciones ciudadanas que no son parte del Estado ni son empresas, como las juntas de vecinos, los clubes, los colectivos y los sindicatos. La democratización es el proceso por el cual aumentan la participación, los derechos y el control ciudadano del poder. Estudiar su impacto a nivel local significa preguntar cómo se vivió ese cambio en una comuna o un barrio concretos, sin suponer que fue igual en todas partes.",
    ],
    vocab=[("historiografía", "estudios e interpretaciones que se escriben sobre el pasado"), ("perspectiva historiográfica", "modo de mirar un proceso: actores, escala y fuentes que destaca"), ("contextualizar", "situar algo en su tiempo, su espacio y sus actores"), ("escala", "nivel de estudio: barrio, comuna, región o país"), ("sociedad civil", "organizaciones ciudadanas que no son Estado ni empresas"), ("democratización", "proceso en que crecen la participación, los derechos y el control ciudadano del poder")],
    worked=[
        ("Contextualizar una frase de archivo", "Un archivo de ejemplo dice: «En 2012, la agrupación de jóvenes de Lomas del Sur pidió una plaza con rampas de acceso.» Contextualiza la frase.",
         ["Actor: la agrupación de jóvenes, que pertenece a la sociedad civil.", "Tiempo: el año 2012. Espacio: Lomas del Sur, es decir, escala local."],
         "Actor: agrupación de jóvenes; tiempo: 2012; espacio: la comuna (escala local)"),
        ("Reconocer una perspectiva", "Un texto de ejemplo afirma: «La democratización llegó a Lomas del Sur porque el Estado ofreció fondos para proyectos.» ¿Qué perspectiva adopta?",
         ["Pregunta quién es el actor principal: el Estado, que ofrece los fondos.", "Pregunta desde dónde se mira: desde las decisiones del Estado hacia la comuna."],
         "Una perspectiva que destaca al Estado como actor principal"),
    ],
    mistakes=[("Creer que una perspectiva historiográfica es solo una opinión personal del autor.", "Se confunde mirar desde un lugar con opinar sin evidencia.", "Una perspectiva se reconoce por los actores, la escala y las fuentes que elige, y se evalúa con evidencia."),
              ("Generalizar desde un caso: decir que lo ocurrido en una comuna ocurrió igual en todo el país.", "Se olvida que cada territorio tiene su propio contexto.", "Indica la escala del estudio y evita extender sus conclusiones sin más evidencia.")],
    T=[
        ("abc", "{F} ¿A qué escala estudia principalmente el cambio la Autora A?", "Local: parte de los barrios y la comuna", "Nacional: parte de las leyes del país", "Internacional: parte de acuerdos entre países", "Habla de la junta de vecinos, el club y el colectivo de la comuna, que son actores de escala local."),
        ("abc", "{F} ¿Qué actor destaca el Autor B para explicar los cambios?", "El Estado central, con leyes y programas", "Las juntas de vecinos y los colectivos", "Las empresas privadas de la comuna", "Dice que las decisiones del Estado central obligaron a crear instancias de participación."),
        ("En Comprensión histórica: ¿cómo se llama el conjunto de estudios e interpretaciones que se escriben sobre el pasado?", "Historiografía", "Es el término que designa lo que historiadoras e historiadores escriben sobre el pasado."),
        ("abc", "Según la explicación, ¿qué es una perspectiva historiográfica?", "Un modo de mirar un proceso: qué actores, escala y fuentes destaca", "La opinión política que el historiador tiene del gobierno", "Una fuente escrita en la misma época del hecho", "No es una opinión suelta: se reconoce por los actores, la escala y las fuentes que el autor elige."),
        ("abc", "{F} Según la definición de la explicación, ¿cuál de estos grupos de la ficha pertenece a la sociedad civil?", "El colectivo de mujeres", "Un ministerio del Estado central", "Una empresa de transporte privada", "El colectivo es una organización ciudadana, mientras un ministerio es Estado y una empresa no es sociedad civil."),
        ("ab", "¿Qué significa contextualizar un proceso?", "Situarlo en su tiempo, su espacio y entre sus actores", "Juzgarlo con las ideas y valores de hoy", "Contextualizar es ubicar el proceso en su propia época y lugar, no juzgarlo desde el presente."),
        ("Un archivo de ejemplo dice: «En 2008, el club de adultos mayores de Lomas del Sur ganó un proyecto para reparar su sede.» Indica el actor, el tiempo y el espacio.", "Actor: el club de adultos mayores; tiempo: 2008; espacio: Lomas del Sur (escala local)", "Se contextualiza respondiendo quién actúa, cuándo ocurre y dónde, como en la frase."),
        ("abc", "{F} Un tercer texto dice: «En todo Chile la participación creció por igual en todas las comunas.» ¿Qué problema tiene usarlo para explicar Lomas del Sur?", "Usa una escala nacional y no distingue lo particular de cada comuna", "Habla de una época demasiado lejana", "Solo nombra al Estado y no a la sociedad civil", "Una afirmación para todo el país no prueba lo ocurrido en una comuna concreta."),
        ("abc", "¿Cuál de estas preguntas contextualiza mejor un estudio local?", "¿Qué organizaciones surgieron en Lomas del Sur entre 1990 y 2020 y quiénes las integraron?", "¿Fue buena la democracia?", "¿Qué pasó en el mundo en esos años?", "Fija un lugar, un período y unos actores, lo que permite buscar evidencia concreta."),
        ("{F} La Autora A y el Autor B no se contradicen necesariamente. ¿Por qué ambas lecturas pueden ser válidas a la vez?", "Porque miran escalas y actores distintos: ella desde los barrios y él desde el Estado", "Cada texto responde a una pregunta distinta, y el cambio pudo tener causas locales y nacionales."),
        ("abc", "{F} Una estudiante concluye: «B tiene la razón, porque las leyes son más importantes que los vecinos.» ¿Qué falla en ese razonamiento?", "Da por hecho que un actor pesa más, sin comparar la evidencia de cada lectura", "Usa una fuente que no existe", "Confunde el año del retorno a la democracia", "Una conclusión histórica debe apoyarse en evidencia comparada y no en una jerarquía supuesta."),
        ("abc", "Si quisieras estudiar cómo llegó la inclusión de nuevos grupos a Lomas del Sur, ¿qué combinación de escalas sería más completa?", "La local (qué hicieron los grupos) y la nacional (qué normas lo permitieron)", "Solo la nacional, porque la local no deja huellas", "Solo la internacional", "Combinar escalas permite ver tanto la acción de los grupos como el marco que la hizo posible."),
        ("Ordena de la escala mayor a la menor: barrio, país, comuna.", "País, comuna, barrio", "Un país contiene a las comunas y cada comuna contiene a sus barrios."),
    ],
    ctx=("abc", "El centro cultural de Lomas del Sur prepara una exposición sobre la historia reciente de la comuna. Una joven propone partir con fotos de la junta de vecinos; un vecino, con las leyes del período. ¿Qué conviene para contextualizar mejor?", "Combinar ambas: los vecinos como actores y las leyes como marco", "Usar solo las leyes, porque son documentos oficiales", "Usar solo las fotos, porque son más atractivas", "Las fotos muestran la acción local y las leyes el contexto nacional, y juntas permiten una exposición más completa."),
    sc=[
        ("En Comprensión histórica: ¿qué es la sociedad civil?", "El conjunto de organizaciones ciudadanas que no son Estado ni empresas", "Incluye juntas de vecinos, clubes, colectivos y sindicatos."),
        ("¿Qué tres elementos permiten contextualizar un proceso?", "Tiempo, espacio y actores", "Situar un proceso exige saber cuándo, dónde y quiénes intervienen."),
        ("¿Por qué no se debe extender sin más lo ocurrido en una comuna a todo el país?", "Porque cada territorio tiene su propio contexto y eso sería generalizar desde un caso", "Un solo caso no prueba que lo mismo ocurriera en otros lugares."),
    ],
    op=("Elige una de estas dos fuentes de ejemplo y contextualízala. Fuente 1: «En 2016, el colectivo de mujeres de Lomas del Sur abrió una biblioteca en la sede vecinal.» "
        "Fuente 2: «En 2019, un consejo comunal de Lomas del Sur incorporó dos cupos para organizaciones de jóvenes.» Escribe actor, tiempo, espacio y escala; una frase que explique qué cambio reciente muestra "
        "(sociedad civil, derechos, desigualdad o inclusión) y una pregunta que te gustaría hacerle a un historiador local.",
        "Fuente 1. Actor: colectivo de mujeres; tiempo: 2016; espacio: sede vecinal de Lomas del Sur (local). Muestra fortalecimiento de la sociedad civil. Pregunta: ¿qué otras organizaciones usaron esa sede?",
        ["identifica correctamente actor, tiempo y espacio", "indica la escala y no la generaliza a todo el país", "relaciona la fuente con uno de los cuatro ejes del cambio", "formula una pregunta que se puede investigar"],
        ["ficha con actor, tiempo, espacio, escala, eje del cambio y pregunta"],
        ["confundir el actor con el lugar", "generalizar a todo Chile desde un solo caso", "escribir una pregunta que se responde con sí o no"],
        "Pregunta: «¿en qué parte de tu ficha dices quién, cuándo y dónde?». Si falta algo, pídele que lo subraye en la fuente."),
    reinforce="Elige una noticia o una foto de tu barrio (descríbela en tres líneas) y escribe quién actúa, cuándo ocurre, dónde y a qué escala la estudiarías.",
    extend="Compara por escrito cómo contaría un mismo cambio de tu comuna una persona de la junta de vecinos y una funcionaria municipal, y qué actores destacaría cada una.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (datos y fuentes de ejemplo, ficticios). Registro municipal de Lomas del Sur con las organizaciones comunitarias inscritas: año 1995, 12 organizaciones; año 2005, 30; año 2015, 54. "
     "Fuente P (acta de 2005): «Se aprueba la creación del comité de adelanto del sector norte, con 18 firmas de vecinos.» "
     "Fuente S (libro de 2018): «La participación comunitaria de Lomas del Sur creció con fuerza en las últimas décadas.»")
build(
    O1, 2, F,
    use="Aprenderé a interrogar fuentes (quién, cuándo, para qué) y a leer un indicador con sus límites, para apoyar una interpretación sobre un cambio reciente sin sobrevalorar un solo dato.",
    prior=["Sé qué es una fuente histórica.", "Sé leer una tabla simple y restar cantidades.", "Distingo un dato de una interpretación."],
    explain=[
        "Una fuente primaria es un documento o testimonio producido en la época que se estudia, como un acta, una foto o una entrevista a quien vivió el hecho. Una fuente secundaria es un texto que interpreta esa época desde después, como un libro de historia. Ambas sirven, pero se leen distinto: la primaria muestra lo que alguien registró entonces, y la secundaria ofrece una interpretación que hay que revisar.",
        "Interrogar una fuente es preguntarle quién la produjo, cuándo, para qué y para quién, qué dice y qué calla. Un acta municipal sirve para saber qué se decidió, pero no cuenta los desacuerdos de la reunión. Un testimonio sirve para entender cómo se vivió algo, pero depende de la memoria y del punto de vista de quien habla.",
        "Un indicador es un dato que mide un aspecto de un proceso, como el número de organizaciones inscritas para hablar de participación. Un buen uso del indicador exige decir qué mide y qué no mide: las organizaciones inscritas no cuentan las informales ni cuántas personas participan en cada una. Por eso un indicador apoya una interpretación, pero no la demuestra por sí solo.",
    ],
    vocab=[("fuente primaria", "documento o testimonio producido en la época estudiada"), ("fuente secundaria", "texto que interpreta una época desde después"), ("interrogar una fuente", "preguntarle quién, cuándo, para qué, qué dice y qué calla"), ("indicador", "dato que mide un aspecto de un proceso"), ("límite de un indicador", "aquello que el dato no mide"), ("evidencia", "información de una fuente que apoya una afirmación")],
    worked=[
        ("Clasificar y interrogar", "Un diario de ejemplo de 2003 informa: «La junta de vecinos del sector sur reunió a 40 personas para pedir iluminación.» ¿Es fuente primaria o secundaria? ¿Qué puedes preguntarle?",
         ["Se produjo en 2003, durante el hecho que cuenta: es fuente primaria.", "Se le puede preguntar quién la escribió, para qué público y si pudo omitir otras opiniones."],
         "Fuente primaria; hay que preguntar autoría, propósito y qué omite"),
        ("Leer un indicador con sus límites", "Un registro de ejemplo indica que en 2010 había 20 clubes deportivos inscritos y en 2020, 26. ¿Qué mide y qué no mide?",
         ["Mide la cantidad de clubes inscritos; el aumento fue de 26 menos 20, es decir, 6.", "No mide cuántas personas participan, ni la actividad real de cada club, ni los clubes no inscritos."],
         "Mide clubes inscritos (6 más); no mide personas ni clubes informales"),
    ],
    mistakes=[("Tratar un libro de historia como si fuera una fuente primaria de la época.", "Se confunde la fecha de publicación con la del hecho.", "Pregunta cuándo se escribió y si su autor vivió lo que cuenta."),
              ("Creer que un indicador demuestra todo el proceso.", "Se olvida que cada dato mide solo un aspecto.", "Escribe siempre qué mide el indicador y qué queda fuera.")],
    T=[
        ("abc", "{F} ¿Cuál de las dos fuentes escritas de la ficha es primaria?", "La Fuente P, un acta producida en 2005", "La Fuente S, un libro de 2018", "Ninguna, porque las dos están escritas", "El acta se produjo en la época del hecho y el libro lo interpreta después."),
        ("abc", "{F} ¿Cuántas organizaciones inscritas había en 2005 según el registro?", "30", "12", "54", "El registro indica 30 para el año 2005."),
        ("abc", "En Comprensión histórica, ¿qué es un indicador?", "Un dato que mide un aspecto de un proceso", "Una conclusión que cierra una discusión", "Un documento escrito por testigos", "El indicador es un dato medible, no una conclusión ni un documento."),
        ("abc", "{F} ¿Qué preguntaría un historiador al acta de la Fuente P?", "Quién la redactó, para qué y qué desacuerdos no registra", "Cuántos años de vida tenía cada firmante", "Cuál es la mejor decisión que podía tomar el comité", "Interrogar una fuente es preguntar por autoría, propósito y silencios."),
        ("abc", "{F} ¿Qué mide el registro municipal de la ficha?", "El número de organizaciones comunitarias inscritas", "El número total de personas que participan", "El grado de satisfacción de los vecinos", "El registro cuenta organizaciones inscritas, no personas ni opiniones."),
        ("ab", "{F} ¿Qué es la Fuente S respecto de la participación en Lomas del Sur?", "Una fuente secundaria que interpreta el período desde después", "Una fuente primaria porque habla de la comuna", "Se publicó en 2018, años después de los hechos que interpreta, por lo que es secundaria."),
        ("=", "{F} ¿Cuántas organizaciones más había inscritas en 2015 que en 1995?", "54-12", "Se resta lo inscrito en 1995 a lo inscrito en 2015."),
        ("abc", "{F} ¿En cuál tramo de diez años aumentó más el número de organizaciones inscritas?", "Entre 2005 y 2015, con 24 más", "Entre 1995 y 2005, con 18 más", "Aumentó lo mismo en ambos tramos", "De 30 a 54 hay 24 más y de 12 a 30 hay 18 más, por lo que el segundo tramo es mayor."),
        ("abc", "{F} Una compañera dice: «El registro prueba que en 2015 participaba más gente que en 1995.» ¿Qué le responderías?", "El registro cuenta organizaciones, no personas: no lo prueba por sí solo", "Tiene razón, porque hay más organizaciones", "No es válido porque es un registro municipal", "Más organizaciones no implican necesariamente más personas participando."),
        ("{F} La Fuente S dice que la participación «creció con fuerza». ¿Qué dato de la ficha podría apoyar esa frase y cuál es su límite?", "El registro: de 12 a 54 organizaciones; no mide cuánta gente participa", "El indicador muestra una tendencia, pero la frase habla de participación en general y el dato cubre solo organizaciones inscritas."),
        ("abc", "{F} Un estudiante cita la Fuente P para afirmar que «todos los vecinos del sector norte querían el comité». ¿Qué falla?", "Solo hay 18 firmas, y el acta no dice cuántos vecinos había ni qué opinaban los demás", "El acta no tiene fecha", "Las actas nunca sirven como fuente", "Una fuente solo permite afirmar lo que registra, y 18 firmas no representan a todo un sector."),
        ("abc", "Para estudiar la inclusión de jóvenes en la vida cívica de una comuna, ¿qué indicador sería más pertinente?", "Cantidad de jóvenes que integran las directivas de organizaciones inscritas", "Cantidad de calles pavimentadas de la comuna", "Cantidad de buses que pasan por la plaza", "El indicador debe medir el aspecto que se estudia, aquí la presencia de jóvenes en cargos."),
        ("abc", "¿Qué conviene hacer para apoyar mejor una interpretación sobre la participación?", "Combinar un indicador, un testimonio y un documento oficial", "Usar solo el indicador, porque los números no se equivocan", "Usar solo el libro más reciente", "Fuentes distintas se corrigen entre sí y reducen el riesgo de un sesgo."),
    ],
    ctx=("abc", "Una estudiante de Lomas del Sur investiga el club de adultos mayores. Encuentra la lista de socios de 2012, una entrevista a la presidenta del club y un folleto municipal de 2020 que elogia al club. ¿Cuál de estas fuentes necesita más cuidado por su propósito?", "El folleto municipal, porque busca mostrar una buena imagen", "La lista de socios, porque tiene nombres", "Ninguna, porque todas son verdaderas", "Toda fuente tiene un propósito, y un folleto institucional suele destacar lo positivo."),
    sc=[
        ("En Comprensión histórica: ¿qué diferencia hay entre una fuente primaria y una secundaria?", "La primaria se produce en la época estudiada y la secundaria la interpreta después", "La fecha de producción respecto del hecho separa a ambas."),
        ("¿Qué dos preguntas básicas se hacen a una fuente para interrogarla?", "Quién la produjo y para qué", "Entender autoría y propósito ayuda a evaluar su punto de vista."),
        ("¿Por qué un indicador no demuestra por sí solo una interpretación?", "Porque mide solo un aspecto y no dice lo que queda fuera", "Cada indicador tiene límites que deben declararse."),
    ],
    op=("Elige un indicador de ejemplo para estudiar una de estas dos preguntas: (1) ¿creció la inclusión de personas migrantes en las organizaciones de Lomas del Sur? (2) ¿mejoró el acceso de las familias a la educación superior? "
        "Datos de ejemplo para (1): organizaciones con al menos una persona migrante en su directiva: 3 en 2005 y 11 en 2020. Para (2): jóvenes de la comuna en la educación superior: 90 en 2005 y 210 en 2020. "
        "Escribe qué mide el indicador, una conclusión que sí puedes sostener, tres cosas que el dato no mide y qué otra fuente agregarías.",
        "Pregunta 1. Mide cuántas organizaciones incluyen migrantes en su directiva: de 3 a 11, 8 más. No mide cuántas personas migrantes viven en la comuna, ni su participación fuera de las directivas. Agregaría entrevistas a dirigentes.",
        ["explica qué mide el indicador", "formula una conclusión que los datos sostienen", "nombra al menos tres límites del dato", "propone una fuente complementaria pertinente"],
        ["texto breve con indicador, conclusión, límites y fuente complementaria"],
        ["concluir más de lo que el dato permite", "no declarar ningún límite", "elegir una fuente complementaria que repite el mismo tipo de dato"],
        "Pregunta: «¿esa conclusión podría ser falsa aunque el dato sea correcto?». Si responde que sí, pídele que escriba por qué."),
    reinforce="Con la tabla de la ficha, escribe una conclusión que el indicador sí permita y otra que no permita, y explica la diferencia.",
    extend="Busca en tu casa o en tu liceo un documento (por ejemplo, un reglamento o una foto de aniversario) y escribe quién lo produjo, para qué y qué calla.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (interpretaciones de ejemplo, ficticias). Pregunta: ¿por qué el consejo comunal de Lomas del Sur incorporó cupos para jóvenes, mujeres, migrantes y adultos mayores? "
     "Interpretación 1: «Fue el resultado de años de demandas de organizaciones de la comuna, que presionaron al municipio.» "
     "Interpretación 2: «Fue consecuencia de una ley nacional que obligó a los municipios a crear instancias de participación.» "
     "Interpretación 3: «Influyó el cambio en la composición de la población: había más personas jóvenes y migrantes que antes y querían ser escuchadas.»")
build(
    O1, 3, F,
    use="Aprenderé a distinguir causas de distinto tipo y a comparar perspectivas que explican un mismo cambio, para decidir qué evidencia haría falta para evaluarlas.",
    prior=["Sé que un hecho puede tener varias causas.", "Reconozco actores y escalas en una fuente.", "Sé leer un indicador con sus límites."],
    explain=[
        "Una causa es un factor que ayuda a explicar por qué ocurrió algo. En historia casi nunca hay una sola: se habla de multicausalidad. Algunas causas son estructurales, es decir, de fondo y de larga duración, como un cambio en la población o en la economía. Otras son coyunturales, o sea, detonantes cercanos en el tiempo, como una ley nueva o una movilización puntual.",
        "Comparar perspectivas significa poner lado a lado dos interpretaciones y preguntar qué causas priorizan, qué actores destacan y qué evidencia usan. Una interpretación que destaca el papel de los movimientos sociales no necesariamente excluye a otra que destaca las leyes. A veces se complementan y a veces compiten; para saberlo hay que mirar qué evidencia respalda a cada una.",
        "Hay que cuidar tres errores: confundir una causa con una consecuencia, confundir una coincidencia en el tiempo con una causa, y reducir un proceso complejo a una sola explicación. Para evitarlos conviene ordenar los hechos en una línea de tiempo y preguntarse si lo que se llama causa ocurrió antes que el efecto.",
    ],
    vocab=[("causa", "factor que ayuda a explicar por qué ocurrió algo"), ("multicausalidad", "idea de que un hecho tiene varias causas"), ("causa estructural", "causa de fondo y de larga duración"), ("causa coyuntural", "detonante cercano en el tiempo"), ("coincidencia", "hechos que ocurren en el mismo período sin que uno cause al otro"), ("comparar perspectivas", "poner dos interpretaciones lado a lado para ver causas, actores y evidencia")],
    worked=[
        ("Clasificar causas", "En una comuna de ejemplo, el número de estudiantes universitarios se duplicó en diez años; en el mismo período, una ley nueva creó becas. Clasifica ambos hechos como causas posibles de un mayor interés por la participación cívica.",
         ["La duplicación ocurrió durante diez años: es un cambio de fondo, o estructural.", "La ley nueva es un hecho puntual y cercano al efecto: es coyuntural."],
         "El aumento de estudiantes es estructural; la ley es coyuntural"),
        ("Distinguir causa de coincidencia", "En una comuna de ejemplo, la tasa de organizaciones juveniles subió el mismo año en que se inauguró un centro comercial. ¿Se puede decir que el centro causó el aumento?",
         ["Los dos hechos ocurrieron en el mismo período, pero eso es solo coincidencia.", "Falta evidencia de que el centro influyera, como testimonios o actas que lo mencionen."],
         "No: solo hay coincidencia; falta evidencia de una relación causal"),
    ],
    mistakes=[("Elegir una sola causa y descartar todas las demás.", "Se prefiere una explicación simple a una completa.", "Pregunta qué otras causas pueden haber actuado y qué evidencia hay de cada una."),
              ("Pensar que si dos hechos ocurren en el mismo año, uno causó el otro.", "Se confunde coincidencia con causalidad.", "Busca una fuente que muestre cómo un hecho influyó en el otro.")],
    T=[
        ("abc", "{F} ¿Qué actor principal destaca la Interpretación 1?", "Las organizaciones de la comuna", "El Estado central", "La población joven y migrante, sin acción propia", "Dice que las demandas de organizaciones presionaron al municipio."),
        ("abc", "{F} ¿Qué causa destaca la Interpretación 2?", "Una ley nacional", "Una movilización de vecinos", "Un cambio de alcalde", "Menciona una ley nacional que obligó a los municipios."),
        ("En Comprensión histórica: ¿cómo se llama la idea de que un hecho histórico tiene varias causas?", "Multicausalidad", "Es el término para explicaciones que consideran más de una causa."),
        ("abc", "{F} La Interpretación 3 menciona el cambio en la composición de la población. ¿De qué tipo de causa se trata?", "Estructural, porque es un cambio de fondo y de larga duración", "Coyuntural, porque es un detonante inmediato", "No es una causa, sino una consecuencia", "Un cambio demográfico se produce lentamente y actúa como causa de fondo."),
        ("abc", "{F} ¿Qué interpretación pone el énfasis en una causa coyuntural?", "La Interpretación 2, la ley que obligó a crear instancias", "La Interpretación 3, el cambio de la población", "Ninguna de las tres", "Una ley es un hecho puntual cercano al efecto, es decir, coyuntural."),
        ("ab", "Dos hechos ocurren en el mismo año, pero no hay ninguna fuente que los relacione. ¿Qué corresponde afirmar?", "Que hay una coincidencia y falta evidencia de causalidad", "Que uno causó el otro porque ocurrieron juntos", "Sin una fuente que muestre cómo se influyeron, solo puede hablarse de coincidencia."),
        ("abc", "{F} ¿Cuál de estas afirmaciones relaciona bien las interpretaciones 1 y 2?", "Pueden complementarse: la ley dio el marco y las demandas lo hicieron efectivo en la comuna", "Se contradicen siempre y solo una puede ser cierta", "Hablan de períodos distintos, por lo que no se relacionan", "Una ley nacional y la presión local pueden actuar juntas, de modo que no se excluyen."),
        ("abc", "{F} Una estudiante dice que, como la ley es nacional, la Interpretación 2 explica todo y las demás sobran. ¿Qué error comete?", "Reduce un proceso complejo a una sola causa", "Confunde causa con consecuencia", "Usa un indicador que no mide nada", "Descartar explicaciones sin evidencia contraria olvida la multicausalidad."),
        ("abc", "{F} Para decidir entre las interpretaciones 1 y 2, ¿qué fuente de la comuna sería más útil?", "Las actas de las reuniones donde se discutió la creación del consejo", "Un mapa con las calles de la comuna", "Una lista de los nombres de los integrantes actuales", "Las actas muestran quién planteó la propuesta, si fue una demanda de organizaciones o una exigencia legal."),
        ("abc", "{F} Si las actas muestran que las organizaciones pidieron el consejo cinco años antes de que existiera la ley, ¿qué se refuerza?", "La Interpretación 1, porque las demandas precedieron a la ley", "La Interpretación 2, porque la ley siempre es la causa", "La Interpretación 3, porque ya no hay causas estructurales", "Una causa debe ocurrir antes que el efecto, y las demandas fueron anteriores."),
        ("abc", "{F} Si en la comuna hubo poca presión de organizaciones y el consejo se creó justo después de la ley, ¿qué interpretación gana apoyo?", "La Interpretación 2, la de la ley nacional", "La Interpretación 1, la de las demandas", "Ninguna puede tener apoyo", "La evidencia ahora favorece una causa coyuntural nacional más que una presión local previa."),
        ("abc", "Un autor escribe: «Como aumentó la participación, la desigualdad disminuyó.» ¿Qué hace falta para sostenerlo?", "Evidencia de que la participación influyó en la desigualdad, no solo de que ambas cosas ocurrieron", "Nada más: se explica solo", "Cambiar la palabra participación por movilización", "Que dos cambios coincidan no basta para afirmar que uno produjo el otro."),
        ("abc", "¿Cuál es la mejor formulación de una explicación completa de un cambio social?", "Varias causas actuaron juntas, unas de fondo y otras detonantes, y cada una tiene distinta evidencia", "Hubo una única causa evidente que todos reconocen", "No se puede explicar ningún cambio histórico", "La explicación más sólida reconoce varias causas y sus evidencias."),
    ],
    ctx=("abc", "Un grupo del Liceo Los Alerces (ficticio) investiga por qué en su comuna aumentaron las organizaciones de jóvenes. Una compañera propone que fue por una ley; otro, por redes sociales; otra, por un cambio en la población. ¿Cuál es el mejor plan de trabajo?", "Buscar evidencia para cada explicación y ver cómo se combinan", "Elegir la que más gusta al grupo", "Descartar las que no se pueden medir con un número", "Evaluar las explicaciones exige revisar la evidencia de cada una, sin descartarlas por intuición."),
    sc=[
        ("En Comprensión histórica: ¿qué es una causa estructural?", "Una causa de fondo y de larga duración", "Actúa lentamente, como un cambio demográfico o económico."),
        ("¿Qué diferencia hay entre una coincidencia y una causa?", "En la coincidencia los hechos solo ocurren en el mismo período; en la causa uno ayuda a producir el otro", "La causalidad exige evidencia de la relación."),
        ("¿Por qué dos interpretaciones distintas pueden no excluirse?", "Porque pueden destacar causas diferentes que actuaron juntas", "La multicausalidad permite que varias explicaciones sean parcialmente válidas."),
    ],
    op=("Pregunta: ¿por qué aumentaron las organizaciones de mujeres en una comuna de ejemplo? Tres explicaciones: (1) las mujeres tenían más años de estudio; (2) una ley creó fondos para proyectos de organizaciones; (3) un colectivo de mujeres lideró campañas en los barrios. "
        "Clasifica cada explicación como estructural o coyuntural, indica qué actores aparecen, propón una fuente que usarías para comprobar cada una y escribe una conclusión que combine al menos dos.",
        "(1) estructural, actores: mujeres estudiantes; fuente: datos de educación. (2) coyuntural, actor: Estado; fuente: texto de la ley. (3) coyuntural (campañas puntuales), actor: colectivo; fuente: entrevistas. Conclusión: el mayor estudio dio una base y la ley y las campañas las impulsaron.",
        ["clasifica las causas con una razón", "identifica actores en cada explicación", "propone una fuente pertinente para cada una", "formula una conclusión que combina causas sin cerrar el debate"],
        ["tabla con clasificación, actores y fuentes, y un párrafo de conclusión"],
        ["clasificar como estructural lo que es un detonante", "proponer fuentes que no sirven para comprobar la causa", "elegir una sola causa sin justificar"],
        "Pregunta: «¿qué evidencia haría que cambiaras de opinión?». Si no encuentra ninguna, la explicación está demasiado cerrada."),
    reinforce="Escribe tres posibles causas de un cambio de tu comuna (por ejemplo, la apertura de una biblioteca) y marca cuál es estructural y cuál coyuntural.",
    extend="Busca dos explicaciones que se den en tu familia o liceo sobre un cambio reciente y escribe qué evidencia faltaría para decidir entre ellas.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (cadena de hechos de ejemplo, ficticia). En Lomas del Sur, una agrupación de vecinas y vecinos pide que se reconozca con sobriedad a las personas de la comuna cuyos derechos humanos fueron vulnerados en el pasado. "
     "Hecho 1: la agrupación reúne testimonios y los presenta al municipio. Hecho 2: el municipio instala una placa en la plaza. "
     "Hecho 3: los liceos de la comuna incorporan actividades de educación en derechos humanos. Hecho 4: más estudiantes se integran a los centros de estudiantes y a organizaciones de la comuna.")
build(
    O1, 4, F,
    use="Aprenderé a explicar relaciones entre hechos de un proceso de democratización (derechos humanos, desigualdad, inclusión) y a distinguir consecuencias de corto y de largo plazo, directas e indirectas.",
    prior=["Sé qué es una causa y una consecuencia.", "Distingo coincidencia de causalidad.", "Sé que los derechos humanos protegen la dignidad de todas las personas."],
    explain=[
        "Los derechos humanos son derechos que corresponden a toda persona por el hecho de serlo, como la vida, la integridad, la libertad y la igualdad ante la ley. Su respeto es una condición de la democracia: sin él, la participación y el control ciudadano del poder pierden sentido. En la historia reciente de Chile, el respeto a los derechos humanos se vincula con el trabajo de organizaciones de la sociedad civil, con la memoria y con la educación.",
        "Explicar relaciones es describir cómo un hecho conduce a otro. Una consecuencia directa ocurre como efecto inmediato de un hecho, y una indirecta se produce a través de otros cambios. También se distingue la corta duración (efectos visibles en meses o pocos años) de la larga duración (efectos que tardan décadas). Una buena explicación indica el orden de los hechos, el mecanismo que los une y la evidencia disponible.",
        "La búsqueda de menos desigualdad y la inclusión de nuevos grupos, como mujeres, jóvenes, migrantes, personas mayores o personas con discapacidad, también se explican por cadenas de hechos: una demanda, una norma, un programa, un cambio en las prácticas. Estos temas se tratan con sobriedad y sin detalles gráficos; lo importante es comprender las relaciones entre hechos y cómo cambian las condiciones de vida.",
    ],
    vocab=[("derechos humanos", "derechos de toda persona por el hecho de serlo"), ("consecuencia directa", "efecto inmediato de un hecho"), ("consecuencia indirecta", "efecto que se produce a través de otros cambios"), ("corta duración", "efectos visibles en meses o pocos años"), ("larga duración", "efectos que tardan décadas en verse"), ("mecanismo", "modo en que un hecho conduce a otro")],
    worked=[
        ("Ordenar una cadena causal", "En una comuna de ejemplo: (a) se aprueba una norma de acceso para personas con discapacidad; (b) una organización de personas con discapacidad pide rampas en la plaza; (c) se construyen rampas en la plaza. Ordena los hechos y explica la relación.",
         ["La petición de la organización es previa a la obra: ocurre primero.", "La norma da el marco y la obra de las rampas es su efecto concreto."],
         "Petición, norma y rampas: la norma da el marco y las rampas son su consecuencia"),
        ("Corto y largo plazo", "En una comuna de ejemplo se crea una beca para estudiantes de familias de menores ingresos. ¿Qué es un efecto de corto plazo y cuál de largo plazo?",
         ["Corto plazo: más jóvenes de esas familias ingresan a la educación superior en los años siguientes.", "Largo plazo: cambia, con las décadas, la composición de las profesiones y de la dirigencia local."],
         "Corto plazo: más ingresos a estudiar; largo plazo: cambios en la composición de profesiones y dirigencias"),
    ],
    mistakes=[("Contar cualquier hecho posterior como consecuencia.", "Se confunde el orden temporal con la relación causal.", "Pregunta cuál es el mecanismo que une los dos hechos y qué fuente lo muestra."),
              ("Explicar el proceso como una línea recta sin tensiones ni retrocesos.", "Se supone que el avance es continuo.", "Considera dificultades, desacuerdos y límites de cada cambio.")],
    T=[
        ("abc", "{F} ¿Cuál es el primer hecho de la cadena?", "La agrupación reúne testimonios y los presenta al municipio", "El municipio instala una placa", "Los liceos incorporan actividades de educación en derechos humanos", "Los hechos están numerados en orden y el primero es la acción de la agrupación."),
        ("abc", "{F} ¿Qué actor impulsa el primer hecho?", "Una agrupación de la sociedad civil", "Un ministerio del Estado central", "Una empresa privada", "Es una agrupación de vecinas y vecinos, que forma parte de la sociedad civil."),
        ("abc", "En Comprensión histórica, ¿qué son los derechos humanos?", "Derechos de toda persona por el hecho de serlo", "Derechos que solo tienen las personas mayores de edad", "Beneficios que entrega cada gobierno", "Pertenecen a toda persona y no dependen de un gobierno ni de la edad."),
        ("abc", "{F} El hecho 2 es la instalación de una placa en la plaza. ¿Qué relación tiene con el hecho 1?", "Es una consecuencia de la acción de la agrupación", "Es una causa del hecho 1", "No tienen relación", "La placa responde a la petición que presentó la agrupación."),
        ("abc", "{F} ¿Cuál es una consecuencia indirecta de la placa?", "Que más estudiantes se involucren en organizaciones tras conocer la historia local", "Que se coloque la placa en la plaza", "Que la agrupación reúna testimonios", "Es un efecto que llega a través de otros cambios, como la educación y la conciencia cívica."),
        ("abc", "{F} ¿Cuál de estos efectos es de larga duración?", "Que una generación crezca con formación en derechos humanos", "Que se publique una nota en el diario local", "Que se inaugure la placa un sábado", "La formación de una generación tarda años en mostrar sus efectos."),
        ("abc", "{F} ¿Qué mecanismo posible une el hecho 2 con el hecho 3?", "El reconocimiento público instaló el tema y los liceos lo llevaron a sus clases", "La placa es una ley que obliga a los liceos a enseñar el tema", "El hecho 3 ocurrió antes que el hecho 2", "Un mecanismo creíble explica cómo uno llevó al otro sin suponer datos que la ficha no entrega."),
        ("abc", "{F} Una estudiante dice: «El hecho 4 ocurrió después del 3; por lo tanto lo causó.» ¿Qué le falta a su razonamiento?", "Evidencia de un mecanismo, como testimonios de estudiantes que se motivaron", "Nada, el orden temporal basta", "Cambiar el orden de los hechos", "El orden en el tiempo es necesario pero no suficiente para afirmar una causa."),
        ("abc", "{F} ¿Qué puede decirse con seguridad usando solo esta ficha?", "Que los hechos ocurrieron en ese orden, pero no cuánto influyó cada uno", "Que cada hecho causó exactamente el siguiente", "Que el proceso fue igual en todo Chile", "La ficha entrega el orden, no mide la influencia ni generaliza."),
        ("abc", "Una comuna de ejemplo crea un programa de apoyo para que más mujeres dirijan organizaciones. ¿Qué efecto indirecto es plausible a largo plazo?", "Más mujeres participando en decisiones de la comuna", "Que todas las mujeres de la comuna pasen a dirigir organizaciones", "Que los hombres dejen de participar en las organizaciones", "Es un efecto vinculado a la inclusión que puede aparecer años después, sin exagerarlo."),
        ("abc", "{F} ¿Qué contraargumento le pondrías a quien diga que la placa «resolvió» el tema de los derechos humanos en la comuna?", "Una placa es un reconocimiento, pero el respeto a los derechos depende de prácticas sostenidas en el tiempo", "Una placa no puede tener ninguna consecuencia", "El tema no es de interés de la comuna", "Un símbolo importa, pero no reemplaza prácticas e instituciones permanentes."),
        ("abc", "Una comuna de ejemplo registró que los jóvenes de familias de menores ingresos en la educación superior pasaron de 90 a 210. ¿Qué indica esto sobre la desigualdad?", "Que se amplió el acceso, pero no basta para afirmar que la desigualdad desapareció", "Que la desigualdad ya no existe", "Que el número no mide nada", "Un indicador de acceso muestra un avance parcial, no una conclusión total."),
        ("=", "Una comuna de ejemplo se propuso llegar a 250 jóvenes de familias de menores ingresos en la educación superior y llegó a 210. ¿Cuántos faltaron para la meta?", "250-210", "Lo que falta se calcula restando lo logrado a la meta."),
    ],
    ctx=("abc", "En un liceo ficticio se pregunta por qué hoy hay más estudiantes migrantes en el centro de estudiantes. Una profesora propone buscar actas del centro, entrevistas a exdirigentes y la norma de convivencia del liceo. ¿Por qué ese plan sirve?", "Porque combina fuentes que muestran decisiones, experiencias y reglas", "Porque todas son de la misma época y tipo", "Porque evita preguntar a los estudiantes", "Las actas, los testimonios y la norma permiten reconstruir cómo y por qué se produjo el cambio."),
    sc=[
        ("En Comprensión histórica: ¿qué diferencia hay entre una consecuencia directa y una indirecta?", "La directa es un efecto inmediato; la indirecta ocurre a través de otros cambios", "La indirecta necesita pasos intermedios para producirse."),
        ("¿Por qué el orden en el tiempo no basta para afirmar una causa?", "Porque que algo ocurra después no prueba que lo provocó", "Se necesita evidencia del mecanismo entre ambos hechos."),
        ("¿Por qué el respeto a los derechos humanos se vincula con la democracia?", "Porque sin respeto a los derechos la participación y el control ciudadano del poder pierden sentido", "Una democracia necesita que todas las personas puedan participar con seguridad."),
    ],
    op=("Elige una cadena de ejemplo. Cadena 1: una organización de personas mayores pide transporte más accesible; el municipio cambia el recorrido de dos buses; más personas mayores llegan al consultorio y a las reuniones vecinales. "
        "Cadena 2: un colectivo de estudiantes pide un baño accesible; el liceo lo construye; aumenta la asistencia de estudiantes con discapacidad. Ordena los hechos, escribe un mecanismo para cada paso, una consecuencia de corto y una de largo plazo, y una duda sobre la evidencia.",
        "Cadena 1. Orden: petición, cambio de recorrido, más llegadas. Mecanismo: el municipio responde a la demanda. Corto plazo: mayor asistencia; largo plazo: más presencia en decisiones. Duda: ¿hay registros de asistencia antes y después?",
        ["ordena correctamente los hechos", "explica un mecanismo en cada paso", "distingue una consecuencia de corto y otra de largo plazo", "formula una duda sobre la evidencia"],
        ["esquema con hechos, mecanismos, consecuencias y duda"],
        ["tomar el orden temporal como prueba de causa", "no distinguir plazos", "presentar el proceso sin dificultades"],
        "Pregunta: «¿cómo sabes que el paso 2 se debe al paso 1?». Si la respuesta es «porque vino después», pide un mecanismo o una fuente."),
    reinforce="Elige un cambio reciente de tu comuna (por ejemplo, una ciclovía o una biblioteca) y escribe una cadena de tres hechos con su orden y sus consecuencias.",
    extend="Imagina una cadena que se interrumpe (la norma no se cumple) y escribe cómo cambiaría la explicación del proceso.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (interpretaciones y datos de ejemplo, ficticios). El consejo comunal de Lomas del Sur tiene 20 integrantes; 8 representan a organizaciones de jóvenes, mujeres, migrantes y personas mayores. En dos años, el municipio tomó 15 decisiones sobre el presupuesto; el consejo fue consultado en 3 de ellas. "
     "Interpretación X: «El consejo muestra una inclusión real: dos de cada cinco integrantes representan a grupos antes ausentes.» "
     "Interpretación Y: «La inclusión es simbólica: los grupos están presentes, pero casi no influyen en las decisiones.»")
build(
    O1, 5, F,
    use="Aprenderé a evaluar interpretaciones sobre un cambio reciente con criterios claros (evidencia, alcance, coherencia, sesgo y omisiones), para elegir la más sólida sin declararla única verdad.",
    prior=["Sé comparar causas y perspectivas.", "Sé leer un indicador con sus límites.", "Conozco los ejes del cambio: sociedad civil, derechos, desigualdad e inclusión."],
    explain=[
        "Evaluar una interpretación es juzgar qué tan bien está respaldada, no si coincide con lo que uno piensa. Cuatro criterios útiles son la evidencia (qué datos y fuentes usa), el alcance (hasta dónde generaliza), la coherencia (si sus partes se contradicen) y el sesgo (qué interés o punto de vista pudo orientar la selección de evidencia). También se revisa qué omite: un silencio puede ser tan importante como lo que se dice.",
        "Una interpretación puede ser sólida en un aspecto y débil en otro. Por ejemplo, una que se apoye en un número sin declarar sus límites tiene buena evidencia aparente pero mal alcance. Cuando dos interpretaciones usan evidencia distinta para responder preguntas distintas, no se pueden comparar directamente, y lo más honesto es decir qué parte de la realidad ilumina cada una.",
        "Una conclusión matizada reconoce lo que la evidencia permite y lo que deja abierto. Si el desacuerdo persiste, no es un fracaso: es información sobre qué falta investigar. Evaluar alternativas en este electivo no significa elegir un bando político, sino decidir con razones qué lectura está mejor respaldada y cuál es su límite.",
    ],
    vocab=[("evaluar una interpretación", "juzgar qué tan bien está respaldada"), ("alcance", "hasta dónde puede generalizarse una conclusión"), ("coherencia", "ausencia de contradicciones internas"), ("sesgo", "punto de vista o interés que orienta la selección de evidencia"), ("omisión", "aquello que una interpretación no menciona"), ("conclusión matizada", "conclusión que reconoce lo que la evidencia permite y lo que deja abierto")],
    worked=[
        ("Aplicar criterios", "Una interpretación de ejemplo afirma: «Las organizaciones de la comuna participan más que nunca», y cita un solo dato: que se inscribieron 5 organizaciones nuevas este año. Evalúa su evidencia y su alcance.",
         ["Evidencia: un solo dato sobre inscripciones, que mide creación y no participación.", "Alcance: generaliza («más que nunca») más de lo que el dato permite."],
         "Evidencia limitada y alcance excesivo"),
        ("Detectar una omisión", "Un informe municipal de ejemplo dice que «el 100 % de las reuniones tuvo asistentes de todos los grupos». No dice cuántas personas fueron ni si pudieron hablar. ¿Qué omite?",
         ["Omite la cantidad de asistentes y su capacidad de intervenir.", "Un dato de presencia no equivale a influencia."],
         "Omite cuántos asistieron y si influyeron"),
    ],
    mistakes=[("Elegir la interpretación que coincide con la propia opinión.", "Se confunde evaluar con estar de acuerdo.", "Aplica los mismos criterios de evidencia, alcance, coherencia, sesgo y omisión a todas."),
              ("Creer que si dos interpretaciones discrepan, una debe ser falsa por completo.", "Se piensa que solo hay una respuesta correcta.", "Revisa qué parte de la realidad ilumina cada una y qué evidencia las separa.")],
    T=[
        ("abc", "{F} ¿Cuántos integrantes del consejo representan a los grupos nombrados en la ficha?", "8", "20", "15", "La ficha dice que 8 de los 20 integrantes representan a esos grupos."),
        ("abc", "{F} ¿En cuántas de las 15 decisiones fue consultado el consejo?", "3", "8", "12", "La ficha indica que el consejo fue consultado en 3 decisiones."),
        ("abc", "En Comprensión histórica, ¿qué significa evaluar una interpretación?", "Juzgar qué tan bien está respaldada", "Decidir si coincide con mi opinión", "Contar cuántos autores la repiten", "Se evalúa por evidencia y razones, no por acuerdo personal."),
        ("abc", "{F} ¿Qué dato usa la Interpretación X como evidencia principal?", "La composición del consejo: 8 de 20 integrantes", "La cantidad de decisiones en que fue consultado", "La opinión de los vecinos", "Habla de que dos de cada cinco integrantes representan a grupos antes ausentes, que es la composición."),
        ("abc", "{F} ¿Qué dato usa la Interpretación Y como evidencia principal?", "La baja influencia del consejo en las decisiones", "La cantidad de organizaciones inscritas", "La edad de los integrantes", "Su afirmación se apoya en que casi no influyen en las decisiones."),
        ("=", "{F} ¿En cuántas de las 15 decisiones el consejo no fue consultado?", "15-3", "Se resta a 15 las decisiones en que sí fue consultado."),
        ("abc", "{F} ¿Cuál es el límite del dato «8 de 20 integrantes»?", "Muestra presencia, no capacidad de influir en las decisiones", "No sirve porque es un número", "Muestra influencia total del consejo", "Cuántas personas hay en un órgano no dice cuánto pesan sus opiniones."),
        ("abc", "{F} ¿Cuál es el límite del dato «consultado en 3 de 15»?", "No dice si fueron decisiones importantes ni si la consulta cambió algo", "Muestra que el consejo es inútil", "No tiene ningún límite", "Que se consulte no implica que la opinión se tome en cuenta, ni cuánto importaba la decisión."),
        ("abc", "{F} ¿Pueden ser ciertas a la vez la Interpretación X y la Y?", "Sí: describen aspectos distintos, la presencia y la influencia", "No: si una es verdadera, la otra es falsa", "No: usan datos de años distintos", "Una habla de la composición del consejo y la otra de su incidencia en decisiones, por lo que no se excluyen."),
        ("abc", "{F} ¿Qué conclusión matizada es mejor?", "Hay presencia de grupos antes ausentes, pero su influencia es todavía limitada según estos datos", "El consejo es un éxito total", "El consejo es un fracaso total", "Reconoce lo que ambos datos permiten sin exagerar."),
        ("abc", "{F} ¿Qué dato adicional ayudaría más a decidir entre X e Y?", "Cuántas veces las opiniones del consejo cambiaron decisiones del municipio", "La edad del alcalde", "El nombre del consejo", "Mide directamente la influencia, que es lo que discuten ambas interpretaciones."),
        ("abc", "Un autor de ejemplo defiende una lectura optimista solo con testimonios de dirigentes satisfechos. ¿Qué criterio revisarías primero?", "El sesgo, por la selección de testimonios favorables", "La ortografía del texto", "El tamaño de la letra", "Si solo se eligen testimonios favorables, el punto de vista orienta la evidencia."),
        ("abc", "Dos informes llegan a conclusiones opuestas, pero uno midió asistencia y el otro, influencia. ¿Qué corresponde?", "Reconocer que responden preguntas distintas y combinarlas", "Descartar a ambos", "Elegir el informe más largo", "Evidencia distinta para preguntas distintas no genera una contradicción real."),
    ],
    ctx=("abc", "Un centro de estudiantes ficticio debe decidir si publica un informe que dice: «La inclusión en nuestro liceo ya está lograda, porque el 40 % de las directivas son mujeres». ¿Qué le sugerirías?", "Agregar otros indicadores (influencia, permanencia) y señalar los límites del dato", "Publicar el informe sin cambios", "Eliminar el dato por incómodo", "Un solo indicador de presencia no basta para afirmar que la inclusión está lograda."),
    sc=[
        ("En Comprensión histórica: ¿cuáles son cuatro criterios para evaluar una interpretación?", "Evidencia, alcance, coherencia y sesgo", "Permiten juzgar el respaldo de una interpretación sin depender de la opinión propia."),
        ("¿Por qué es importante revisar lo que una interpretación omite?", "Porque un silencio puede cambiar el sentido de la conclusión", "Lo que no se dice puede ser tan importante como lo que se dice."),
        ("¿Qué es una conclusión matizada?", "La que reconoce lo que la evidencia permite y lo que deja abierto", "Evita exagerar y declara sus límites."),
    ],
    op=("Evalúa estas dos interpretaciones de ejemplo sobre un programa comunal de becas. Interpretación P: «El programa redujo la desigualdad, porque 60 jóvenes de familias de menores ingresos entraron a estudiar.» "
        "Interpretación Q: «El programa no redujo la desigualdad, porque 25 de esos 60 abandonaron a los dos años.» Escribe, para cada una, qué evidencia usa, qué omite y qué alcance tiene; luego redacta una conclusión matizada de tres frases.",
        "P usa el ingreso (60), omite la permanencia y generaliza «redujo la desigualdad». Q usa el abandono (25 de 60), omite quiénes continuaron (35) y generaliza «no redujo». Conclusión: hubo acceso, 35 continúan, y no se puede decir aún cuánto redujo la desigualdad.",
        ["identifica la evidencia de cada interpretación", "reconoce al menos una omisión en cada una", "evalúa el alcance de cada conclusión", "redacta una conclusión matizada coherente con los datos"],
        ["cuadro con evidencia, omisión y alcance, y una conclusión de tres frases"],
        ["tomar partido sin aplicar criterios", "olvidar que 35 estudiantes sí continuaron", "escribir una conclusión que ignora uno de los datos"],
        "Pregunta: «¿qué dato de P y de Q usas en tu conclusión?». Si solo usa uno, pídele incorporar el otro."),
    reinforce="Elige un titular de ejemplo sobre un cambio social y escribe dos preguntas que le harías para evaluarlo (evidencia y omisiones).",
    extend="Redacta dos conclusiones sobre el mismo dato: una exagerada y otra matizada, y explica en qué se diferencian.",
)

# ============================================================ OAC-01, clase 6
F = ("Ficha 6 (borrador de ejemplo). Un estudiante prepara una conclusión sobre el impacto local de la democratización en Lomas del Sur y escribe: "
     "«La democratización cambió totalmente la comuna: ahora todos participan y no queda desigualdad.» Cuenta con tres evidencias de ejemplo: "
     "(1) las organizaciones inscritas pasaron de 12 a 54 entre 1995 y 2015; (2) el consejo comunal tiene 8 de 20 integrantes de grupos antes ausentes, pero fue consultado en 3 de 15 decisiones; "
     "(3) un testimonio de una dirigenta afirma que «hoy se escucha más, aunque falta mucho».")
build(
    O1, 6, F,
    use="Aprenderé a comunicar una conclusión situada sobre un cambio reciente: una tesis con evidencia de fuentes distintas, un matiz, un límite y la indicación de su tiempo, lugar y escala.",
    prior=["Sé contextualizar, interrogar fuentes y comparar perspectivas.", "Sé evaluar una interpretación con criterios.", "Sé que una conclusión debe declarar sus límites."],
    explain=[
        "Una conclusión situada dice desde dónde se habla: en qué tiempo, en qué lugar y a qué escala vale lo que afirma. En vez de decir «la democratización cambió todo», dice «en Lomas del Sur, entre 1995 y 2015, el número de organizaciones inscritas aumentó, aunque no sabemos cuánta gente participa». Esa precisión la hace más verdadera y más fácil de revisar.",
        "Un párrafo de conclusión historiográfica tiene cuatro partes: una tesis (lo que se afirma), evidencia de al menos dos fuentes o tipos de fuente que la apoyan, un matiz o contrapunto (algo que complica o limita la tesis) y un límite (lo que no se puede afirmar con lo que se tiene). La tesis debe ser lo bastante concreta para poder ser discutida.",
        "Al comunicar, conviene usar verbos que indiquen grado de certeza, como «los datos sugieren», «es probable» o «se confirma», en lugar de absolutos como «siempre» o «todos». También conviene nombrar la perspectiva con que se trabajó y reconocer qué otras lecturas existen. Una buena conclusión invita a continuar la investigación en vez de cerrar la conversación.",
    ],
    vocab=[("conclusión situada", "conclusión que declara su tiempo, lugar y escala de validez"), ("tesis", "afirmación central que se defiende con evidencia"), ("contrapunto", "dato o idea que complica o limita la tesis"), ("límite", "aquello que no puede afirmarse con la evidencia disponible"), ("absoluto", "palabra como «siempre», «nunca» o «todos» que no admite excepciones"), ("grado de certeza", "qué tan segura es una afirmación según su evidencia")],
    worked=[
        ("Reescribir un absoluto", "Un borrador de ejemplo dice: «En todas las comunas la participación aumentó siempre.» Reescríbelo como conclusión situada, usando solo la evidencia: en Lomas del Sur, las organizaciones inscritas pasaron de 12 a 54 entre 1995 y 2015.",
         ["Se acota el lugar y el período: Lomas del Sur, entre 1995 y 2015.", "Se limita a lo que mide el dato: organizaciones inscritas, y se usa un verbo de certeza moderada."],
         "En Lomas del Sur, entre 1995 y 2015, el número de organizaciones inscritas aumentó de 12 a 54, lo que sugiere mayor participación organizada"),
        ("Identificar partes del párrafo", "Un párrafo de ejemplo dice: «Los datos sugieren que en la comuna creció la inclusión de jóvenes. Las actas muestran 5 jóvenes en directivas y un testimonio lo confirma. Sin embargo, solo 1 llegó a presidir. Falta saber si el cambio se mantiene.» Identifica las partes.",
         ["Tesis: creció la inclusión de jóvenes; evidencia: actas y testimonio.", "Contrapunto: solo 1 llegó a presidir; límite: falta saber si se mantiene."],
         "Tesis, evidencia en dos fuentes, contrapunto y límite"),
    ],
    mistakes=[("Escribir una conclusión que suena rotunda para parecer más fuerte.", "Se cree que la seguridad equivale a calidad.", "Usa verbos de certeza moderada y declara los límites."),
              ("Incluir evidencia de un solo tipo de fuente.", "Se confía en el dato más a mano.", "Combina al menos dos tipos de fuente que se corrijan entre sí.")],
    T=[
        ("abc", "{F} ¿Qué problema tiene la frase del estudiante «ya no queda desigualdad»?", "Es un absoluto que ninguna de las evidencias respalda", "Es demasiado corta", "Está bien porque la evidencia (1) la prueba", "Ninguna evidencia mide toda la desigualdad, de modo que la afirmación excede los datos."),
        ("abc", "{F} ¿Cuántas evidencias de ejemplo tiene el estudiante?", "Tres", "Dos", "Cuatro", "La ficha enumera tres evidencias numeradas."),
        ("abc", "En Comprensión histórica, ¿qué es una tesis?", "La afirmación central que se defiende con evidencia", "Una lista de fuentes", "Una opinión sin pruebas", "La tesis es lo que el texto sostiene y respalda con evidencia."),
        ("abc", "{F} ¿Cuál de las evidencias aporta un matiz que complica la tesis del estudiante?", "La evidencia (2): el consejo fue consultado en 3 de 15 decisiones", "La evidencia (1): 12 a 54 organizaciones", "Ninguna", "Muestra que la presencia de grupos no equivale a mucha influencia."),
        ("abc", "{F} ¿Qué tipo de fuente es la evidencia (3)?", "Un testimonio", "Un registro municipal", "Un libro de historia", "Es la opinión de una dirigenta que vivió el período."),
        ("abc", "¿Qué declara una conclusión situada?", "El tiempo, el lugar y la escala en que vale", "Solo la opinión del autor", "Que sirve para todo Chile", "Situada significa acotada a un lugar, un período y una escala."),
        ("ab", "¿Qué formulación usa un verbo de certeza adecuado para un dato de 12 a 54 organizaciones?", "Los datos sugieren un aumento de la participación organizada", "Está probado que todos participan", "Un aumento de organizaciones inscritas apoya, pero no prueba, una mayor participación."),
        ("abc", "{F} ¿Cuál es la mejor reescritura del borrador del estudiante usando la evidencia (1)?", "En Lomas del Sur, entre 1995 y 2015, las organizaciones inscritas pasaron de 12 a 54, lo que sugiere mayor participación organizada", "Con 54 organizaciones inscritas, todos los vecinos participan hoy", "Entre 1995 y 2015 aumentó la participación en todo Chile", "Incluye lugar, período, dato y un verbo de certeza moderada, a diferencia de las otras."),
        ("abc", "{F} Para ser una buena conclusión, además de la tesis y la evidencia, al estudiante le falta principalmente", "Un contrapunto y un límite", "Más adjetivos", "Una opinión política", "Una conclusión sólida declara qué complica la tesis y qué no se puede afirmar."),
        ("abc", "{F} ¿Cuál es el mejor contrapunto para su conclusión usando las evidencias?", "El consejo tiene presencia de grupos, pero fue consultado solo en 3 de 15 decisiones", "El testimonio es de una persona", "Las organizaciones son 54", "Complica la tesis con un dato de la propia ficha."),
        ("abc", "{F} ¿Cuál es un límite honesto de su estudio?", "Los datos corresponden a una comuna y no permiten hablar de todo Chile", "Que la comuna tiene nombre ficticio", "Que fue escrito por un estudiante", "El caso local no autoriza a generalizar al país."),
        ("abc", "¿Cuál es la mejor conclusión situada?", "En Lomas del Sur, entre 1995 y 2015, los datos sugieren más participación organizada, aunque falta saber cuánta gente participa y cuánto influye", "En Chile todos participan hoy más que nunca", "La democratización fue buena y no hay más que decir", "Acota el lugar y el período, usa un verbo moderado y declara límites."),
        ("abc", "Un compañero dice que declarar límites «debilita» la conclusión. ¿Cómo respondes?", "Al contrario: la hace más confiable porque muestra hasta dónde llega la evidencia", "Tiene razón, es mejor ocultarlos", "Los límites solo se escriben en las introducciones", "Declarar límites permite que otros revisen y mejoren la conclusión."),
    ],
    ctx=("abc", "Una alumna debe presentar en un seminario escolar su conclusión sobre el cambio reciente en su comuna. Tiene un dato, un testimonio y un acta. ¿Cómo debería comenzar?", "Con una tesis acotada a su comuna y a un período, apoyada en las tres fuentes", "Con una frase sobre todo Chile", "Con una opinión sin fuentes", "Una tesis situada con evidencia variada es el inicio más sólido."),
    sc=[
        ("En Comprensión histórica: ¿cuáles son las cuatro partes de un párrafo de conclusión?", "Tesis, evidencia, contrapunto y límite", "Combinadas, hacen que la conclusión sea sólida y revisable."),
        ("¿Por qué conviene evitar palabras como «siempre» o «todos»?", "Porque son absolutos que casi nunca puede sostener la evidencia", "Exageran el alcance de la conclusión."),
        ("¿Qué quiere decir que una conclusión sea situada?", "Que declara el tiempo, el lugar y la escala en que vale", "Evita generalizar más allá de la evidencia."),
    ],
    op=("Escribe un párrafo de cuatro a seis líneas con una conclusión situada sobre este caso de ejemplo. Evidencias: (1) en Lomas del Sur, los cargos de dirigencia ocupados por mujeres pasaron de 4 a 15 entre 2000 y 2020; "
        "(2) en una entrevista, una vecina dice: «Hoy nos escuchan, pero las decisiones grandes las siguen tomando otros»; (3) un acta de 2020 muestra que 2 de las 6 decisiones del año fueron consultadas a las organizaciones. "
        "Incluye tesis, dos evidencias, un contrapunto y un límite, y usa al menos un verbo de certeza moderada.",
        "En Lomas del Sur, entre 2000 y 2020, los datos sugieren mayor presencia de mujeres en la dirigencia (4 a 15). Una vecina lo confirma, pero dice que las decisiones grandes las toman otros, y el acta muestra consultas en 2 de 6 decisiones. No sabemos si esto se repite en otras comunas.",
        ["formula una tesis acotada en lugar, período y escala", "usa al menos dos evidencias de tipos distintos", "incluye un contrapunto y un límite", "usa verbos de certeza moderada y evita absolutos"],
        ["párrafo de cuatro a seis líneas"],
        ["usar absolutos", "citar solo el dato que favorece la tesis", "no declarar ningún límite"],
        "Pregunta: «¿qué parte de tu párrafo es el límite y cómo sabes que lo es?». Pídele que lo subraye."),
    reinforce="Toma una afirmación absoluta de una conversación o noticia y reescríbela como conclusión situada con lugar, período y un límite.",
    extend="Escribe una conclusión situada sobre la misma evidencia desde dos perspectivas distintas (una local y una nacional) y explica qué cambia.",
)
