"""HGCS EPJA Media N1, módulo 2 (parte 4): OAD-08, analizar distintas fuentes para explicar cómo los conflictos globales y regionales configuraron el territorio y la identidad contemporáneos. Fuentes y datos de ejemplo en papel, descripciones y tablas en lugar de mapas, tono plural."""
from __future__ import annotations

from epja_hgcs_nm1_b_common import K

O = "EPJA-HGCS-NM1-OAD-08"

# ====================================================== clase 1: partir de lo que ya se sabe
F = ("Ficha 1 (caso de ejemplo, inventado, y dato escolar básico). «Río Seco» es un pueblo ficticio a orillas de un río. En 1920, un tratado entre dos países ficticios fijó la frontera por el centro del río. "
     "Antes, la feria de los sábados reunía a familias de ambas orillas. Después del tratado, la feria se redujo, apareció un puesto de control, algunas familias quedaron en países distintos y ambas orillas mantuvieron la misma fiesta patronal y el mismo modo de hablar. "
     "Dato escolar básico: después de la Primera Guerra Mundial, los tratados de paz de 1919 y 1920 cambiaron fronteras en Europa.")
K(O, 1, F,
  "Hoy parto de lo que sé de mi barrio y mi gente para entender qué son el territorio y la identidad y cómo un conflicto puede cambiarlos.",
  ["Todas las personas se sienten parte de algún lugar y de alguna comunidad: un barrio, un pueblo, un país, un oficio, una familia. El territorio es el espacio que una comunidad o un Estado ocupa, usa y organiza. La identidad es el sentimiento de pertenencia a un grupo, con su historia, sus costumbres, su lengua o su forma de ver el mundo.",
   "Los conflictos pueden cambiar el territorio: se trazan o se mueven fronteras, se levantan muros o se fundan nuevos Estados. También pueden cambiar la identidad: algunas personas se ven obligadas a migrar, otras guardan recuerdos distintos del mismo hecho y se crean nuevos símbolos y fechas de recuerdo. Pero hay continuidades: a menudo las comunidades conservan su fiesta, su lengua o sus costumbres.",
   "Para explicar cómo un conflicto configuró un territorio y una identidad usamos fuentes de distintos tipos: tablas con datos, relatos de personas y documentos. Las leemos con empatía y respeto, sabiendo que una misma historia puede recordarse de maneras diferentes y que ninguna persona tiene que contar lo que no quiere."],
  [("territorio", "espacio que una comunidad o un Estado ocupa, usa y organiza"), ("identidad", "sentimiento de pertenencia a un grupo, con su historia, costumbres y lengua"), ("frontera", "línea que separa el territorio de dos Estados"), ("continuidad", "lo que se mantiene a pesar de los cambios"), ("símbolo", "hecho u objeto que representa una idea o una comunidad")],
  [("Ver un cambio territorial", "{F} ¿Qué cambió en Río Seco con el tratado de 1920?", ["Se fijó una frontera por el centro del río.", "Apareció un puesto de control."], "Se fijó una frontera en el río y apareció un puesto de control"),
   ("Ver una continuidad", "{F} ¿Qué se mantuvo en Río Seco después del tratado?", ["La ficha dice que ambas orillas mantuvieron la fiesta patronal.", "También el mismo modo de hablar."], "La fiesta patronal y el modo de hablar")],
  [("Pensar que una frontera cambia toda la identidad de un día para otro.", "La identidad tiene continuidades: costumbres, lengua y fiestas siguen.", "Anota qué cambió y qué se mantuvo."),
   ("Creer que todas las personas de un lugar recuerdan el conflicto igual.", "Cada persona lo vivió desde su situación.", "Escucha varias fuentes antes de generalizar.")],
  [("abc", "{F} ¿Por dónde pasó la frontera, según la ficha?", "Por el centro del río", "Por la plaza del pueblo", "Por un cerro", "La ficha indica que el tratado fijó la frontera por el centro del río."),
   ("ab", "En Geografía: ¿qué es un territorio?", "Un espacio que una comunidad o un Estado ocupa, usa y organiza", "Un tipo de clima", "El territorio es el espacio ocupado y organizado por una comunidad o Estado."),
   ("=", "{F} ¿Cuántos años pasaron entre los tratados de 1919 y el inicio de la Segunda Guerra Mundial en 1939?", "1939-1919", "Se restan los años de ambos hechos para saber el tiempo que pasó.", " años"),
   ("abc", "{F} ¿Qué ocurrió con la feria de los sábados?", "Se redujo", "Se duplicó", "Se trasladó a otra ciudad", "La ficha dice que, después del tratado, la feria se redujo."),
   ("ab", "En Historia: ¿qué es la identidad?", "El sentimiento de pertenencia a un grupo, con su historia y sus costumbres", "El número de cédula de una persona", "La identidad de una comunidad incluye historia, lengua y costumbres."),
   ("{F} ¿En qué año se firmó el tratado que fijó la frontera de Río Seco?", "1920", "La ficha lo indica como el año del tratado."),
   ("abc", "{F} ¿Qué es una continuidad en este caso?", "Que ambas orillas mantuvieron la misma fiesta patronal", "Que apareció un puesto de control", "Que algunas familias quedaron en países distintos", "Una continuidad es lo que se mantiene a pesar del cambio."),
   ("abc", "{F} ¿Cuál es un efecto territorial del tratado en Río Seco?", "Una frontera y un puesto de control", "Una nueva fiesta", "Un cambio de idioma", "La frontera es un cambio de territorio."),
   ("ab", "{F} Una vecina dice: «Antes, una sola feria unía a las dos orillas». ¿Qué fuente de la ficha respalda esa frase?", "La descripción de la feria antes del tratado", "El dato sobre los tratados de 1919", "La ficha dice que antes la feria reunía a familias de ambas orillas."),
   ("abc", "Un estudiante dice: «Tras el tratado, la gente de ambas orillas dejó de sentirse parte de la misma comunidad». ¿Qué falla?", "La ficha muestra continuidades: mantuvieron la fiesta y el modo de hablar", "Nada, es seguro", "La ficha dice que se prohibió la fiesta", "No se puede afirmar un cambio total cuando hay continuidades."),
   ("abc", "{F} ¿Qué dato falta para saber si todas las familias de Río Seco quedaron igual de afectadas?", "Información de cada familia y su situación", "El nombre del río", "El año del tratado", "La ficha solo habla de algunas familias."),
   ("abc", "{F} ¿Qué tienen en común Río Seco y los cambios de fronteras en Europa de 1919 y 1920?", "En ambos, tratados fijaron nuevas fronteras que afectaron a comunidades", "En ambos hubo una guerra civil", "En ambos desapareció el río", "Los dos casos son ejemplos de fronteras redefinidas por tratados."),
   ("abc", "{F} Para explicar un cambio territorial con respeto, ¿qué conviene hacer?", "Usar la ficha, anotar cambios y continuidades y no suponer cómo se sintió cada persona", "Inventar cómo se sentían", "Culpar a un país sin datos", "Describe con evidencia y sin suposiciones.")],
  ("abc", "Un comité de vecinos de ejemplo vive en una calle que, por una obra de la ciudad, quedó cortada en dos barrios con juntas distintas. ¿Cuál es una buena forma de estudiar qué cambió y qué se mantuvo?", "Anotar qué actividades dejaron de hacerse juntos y qué costumbres se mantienen", "Decidir que todo cambió", "Decidir que nada cambió", "Se observa con datos lo que cambió y lo que continúa."),
  [("En Geografía: ¿qué es una frontera?", "Una línea que separa el territorio de dos Estados", "Marca hasta dónde llega cada Estado."),
   ("En un territorio marcado por un conflicto: ¿qué es una continuidad?", "Lo que se mantiene a pesar de los cambios", "Muestra lo que perdura a pesar del cambio."),
   ("¿La identidad cambia de un día para otro por un conflicto?", "No siempre: hay cambios y también continuidades", "En un caso real se observan ambos aspectos.")],
  ("Elige una opción. Opción 1: con la ficha de Río Seco, escribe tres cambios y dos continuidades. Opción 2: piensa en un lugar de tu vida (un barrio, un lugar de trabajo) y anota un cambio y una continuidad, sin datos personales. Usa un tono respetuoso.",
   "Cambios: se fijó una frontera en el río, apareció un puesto de control, la feria se redujo. Continuidades: la fiesta patronal y el modo de hablar se mantuvieron en ambas orillas.",
   ["distingue cambios de continuidades", "usa datos de la ficha o de un caso propio", "no supone sentimientos", "tono respetuoso"],
   ["lista de cambios y continuidades"],
   ["decir que todo cambió", "inventar datos"],
   "Pregunta: «¿Estoy describiendo un cambio o suponiendo lo que sintió alguien?»."),
  "Anota tres cosas de tu barrio que han cambiado y tres que se mantienen.",
  "Explica con un ejemplo por qué una frontera puede cambiar la vida diaria de las personas.")

# ====================================================== clase 2: reconocer la idea y su vocabulario
F = ("Ficha 2 (hechos escolares básicos). 1919 y 1920: tratados de paz que cambian fronteras en Europa. 1945: se crea la ONU. 1947: India y Pakistán se independizan del Imperio británico. "
     "1948: la ONU aprueba la Declaración Universal de Derechos Humanos. Décadas de 1950 y 1960: muchos territorios de África y Asia se independizan de las potencias coloniales. "
     "1949: Alemania queda dividida en dos Estados. 1990: Alemania se reunifica el 3 de octubre. 1973 a 1990: régimen militar en Chile; durante esos años muchas personas salieron del país como exiliadas o migrantes. "
     "1991: una comisión de verdad en Chile entrega un informe sobre violaciones a los derechos humanos durante el régimen militar.")
K(O, 2, F,
  "Hoy aprendo las palabras para explicar cómo los conflictos cambian territorios e identidades: migración, exilio, refugio, descolonización y memoria.",
  ["La migración es el traslado de personas de un lugar a otro para vivir. El refugio es la protección que se busca fuera del país cuando se teme por la vida o la libertad por causa de una guerra o una persecución. El exilio es salir del propio país, forzado o impulsado por una situación política, y a menudo termina en un retorno. En el siglo XX, muchos conflictos produjeron grandes movimientos de personas.",
   "La descolonización fue el proceso por el cual territorios que dependían de potencias coloniales se independizaron, sobre todo después de 1945. Cambió el mapa político del mundo, aunque muchas fronteras se habían trazado antes por decisión de las potencias. La Declaración Universal de Derechos Humanos de 1948 fijó principios comunes de dignidad e igualdad que hoy se usan para mirar estos procesos.",
   "La memoria es lo que una comunidad recuerda de su pasado, y a veces hay recuerdos distintos sobre un mismo hecho. Las comisiones de verdad son organismos que recopilan información sobre violaciones a los derechos humanos para reconocerlas. Para estudiar todo esto sin simplificar, distinguimos hechos con fecha, datos de territorio y relatos personales."],
  [("migración", "traslado de personas de un lugar a otro para vivir"), ("refugio", "protección que se busca fuera del país ante guerra o persecución"), ("exilio", "salida forzada o motivada por razones políticas del propio país"), ("descolonización", "proceso por el que territorios coloniales se independizan"), ("memoria", "lo que una comunidad recuerda de su pasado")],
  [("Relacionar hecho y concepto", "{F} ¿Qué proceso ocurrió en África y Asia en las décadas de 1950 y 1960?", ["La ficha habla de independencias de potencias coloniales.", "Ese proceso se llama descolonización."], "La descolonización"),
   ("Calcular", "{F} ¿Cuántos años pasaron entre la creación de la ONU y la Declaración Universal de Derechos Humanos?", ["Años: 1945 y 1948.", "1948 − 1945 = 3."], "3 años")],
  [("Usar «exilio» y «migración» como si fueran siempre lo mismo.", "El exilio responde a razones políticas y suele ser forzado.", "Pregunta por qué salió la persona y si fue por decisión o por una amenaza."),
   ("Pensar que la descolonización terminó con todos los problemas de los nuevos Estados.", "Las fronteras y las economías heredadas siguieron planteando desafíos.", "Describe cambios y desafíos con fuentes.")],
  [("abc", "En Historia: ¿qué es una migración?", "El traslado de personas de un lugar a otro para vivir", "Un cambio de gobierno", "Una guerra mundial", "Es un movimiento de personas entre lugares."),
   ("ab", "{F} ¿En qué año Alemania se reunificó?", "1990", "1949", "La ficha indica 1990 para la reunificación y 1949 para la división."),
   ("=", "{F} ¿Cuántos años estuvo dividida Alemania, entre 1949 y 1990?", "1990-1949", "Se restan los años de división y reunificación que da la ficha.", " años"),
   ("abc", "En Historia: ¿qué es el exilio?", "La salida del propio país por razones políticas, a menudo forzada", "El regreso al propio país después de una ausencia", "La elección de autoridades por votación", "Se asocia a persecución o amenaza política."),
   ("ab", "{F} ¿Qué aprobó la ONU en 1948?", "La Declaración Universal de Derechos Humanos", "El tratado de Versalles", "La ficha señala esa declaración como hecho de 1948."),
   ("{F} ¿Cuántos años duró el régimen militar en Chile, según la ficha?", "17", "Se resta 1973 de 1990, lo que da 17 años."),
   ("abc", "En Historia: ¿qué fue la descolonización?", "Un proceso por el que territorios coloniales se independizaron", "La creación de nuevas colonias", "La unión de dos países", "Es la independencia de territorios que dependían de potencias."),
   ("abc", "{F} ¿Qué se creó en Chile en 1991, según la ficha?", "Una comisión de verdad entregó un informe sobre violaciones a los derechos humanos", "Un tratado de límites", "Una nueva moneda", "La ficha lo indica como hecho de 1991."),
   ("ab", "En Historia: ¿qué es la memoria de una comunidad?", "Lo que esa comunidad recuerda de su pasado", "Un registro de datos de una oficina pública", "En Ciencias Sociales, memoria es el recuerdo colectivo de una comunidad."),
   ("abc", "{F} ¿Qué dos hechos de la ficha ocurrieron en 1947 y 1949?", "La independencia de India y Pakistán y la división de Alemania", "El golpe de Chile y la Revolución cubana", "La ONU y el Muro", "La ficha los ubica en esos años."),
   ("abc", "Una persona dice: «Si un territorio se independiza, ya no tiene ningún desafío». ¿Cuál es la mejor respuesta?", "Una independencia cambia el gobierno, pero pueden quedar desafíos, como fronteras heredadas", "Tiene razón", "Nunca hay independencia", "Cambiar de Estado no resuelve automáticamente todos los problemas."),
   ("abc", "{F} ¿Qué relación hay entre el régimen militar de Chile y el exilio, según la ficha?", "Durante esos años muchas personas salieron del país como exiliadas o migrantes", "Nadie salió del país", "Todas las personas se quedaron", "La ficha indica que hubo salidas de personas durante ese período."),
   ("abc", "¿Por qué la Declaración Universal de Derechos Humanos de 1948 sirve para mirar estos procesos?", "Porque fija principios comunes de dignidad e igualdad que se usan como referencia", "Porque prohíbe hablar de historia", "Porque solo vale para un país", "Es un marco compartido para evaluar hechos.")],
  ("abc", "Una organización comunitaria de ejemplo apoya a familias recién llegadas de otros países. En una charla debe explicar la diferencia entre migrar y buscar refugio. ¿Cuál es una explicación correcta?", "Migrar es trasladarse para vivir en otro lugar; buscar refugio es pedir protección por guerra o persecución", "Son exactamente lo mismo", "El refugio es siempre un viaje turístico", "El refugio se vincula a una amenaza grave."),
  [("En Historia: ¿qué es un refugio?", "La protección que se busca fuera del país por guerra o persecución", "Responde a un temor grave por la vida o la libertad."),
   ("En Historia: ¿qué es el exilio?", "Salir del país por razones políticas, a menudo de manera forzada", "Suele terminar en un retorno al país de origen."),
   ("¿Qué es una comisión de verdad?", "Un organismo que recopila información sobre violaciones a los derechos humanos", "Su fin es reconocerlas y dejar registro de ellas.")],
  ("Arma una tabla de cinco filas con cinco palabras del vocabulario (migración, refugio, exilio, descolonización, memoria): para cada una escribe con tus palabras qué es y un hecho de la ficha relacionado. Evita agregar datos que no estén en la ficha.",
   "Migración: traslado para vivir en otro lugar; muchas personas salieron de Chile entre 1973 y 1990. Refugio: protección ante guerra o persecución. Exilio: salida por razones políticas. Descolonización: independencias de África y Asia en las décadas de 1950 y 1960. Memoria: recuerdo de la comunidad; la comisión de verdad de 1991 recopiló información sobre violaciones a los derechos humanos.",
   ["define las cinco palabras", "asocia un hecho de la ficha a cada una", "no agrega datos que no están en la ficha", "usa tono respetuoso"],
   ["tabla de cinco filas"],
   ["mezclar exilio y migración", "inventar cifras"],
   "Pregunta: «¿Este hecho está en la ficha?»."),
  "Escribe con tus palabras la diferencia entre exilio y migración.",
  "Explica por qué la memoria de una comunidad puede incluir recuerdos distintos sobre un mismo hecho.")

# ====================================================== clase 3: ver cómo se hace, paso a paso
F = ("Ficha 3 (fuentes de ejemplo, textos inventados, sobre la división de Alemania, hecho histórico básico). "
     "Dato escolar: tras la Segunda Guerra Mundial Alemania quedó dividida; en 1949 se formaron dos Estados, uno en el oeste y otro en el este. En 1961 se levantó un muro que dividió la ciudad de Berlín; en 1989 se abrió y el 3 de octubre de 1990 Alemania se reunificó. "
     "Fuente A (tabla de ejemplo): «cruces autorizados entre las dos partes de Berlín»: 1960, 12 puntos de paso; 1962, 5; 1989, 0 hasta noviembre. "
     "Fuente B (relato de ejemplo, inventado): una mujer ficticia recuerda que su familia quedó separada por el muro y que se volvió a reunir años después. "
     "Fuente C (texto de ejemplo): «Las dos partes siguieron hablando el mismo idioma».")
K(O, 3, F,
  "Hoy sigo cinco pasos para explicar con fuentes cómo un conflicto configuró un territorio y una identidad: pregunta, hecho, territorio, identidad y conclusión.",
  ["Para explicar con fuentes se sigue un método de cinco pasos. Paso 1: escribe la pregunta, por ejemplo, «¿cómo cambió el territorio y la vida de las personas con la división de Alemania?». Paso 2: ubica el hecho con fechas. Paso 3: lee las fuentes sobre el territorio (tablas, descripciones de fronteras). Paso 4: lee las fuentes sobre la identidad (relatos, símbolos, lengua, memorias). Paso 5: concluye con prudencia.",
   "Cada fuente aporta algo distinto. Una tabla muestra el tamaño de un cambio, como cuántos puntos de paso había entre dos zonas. Un relato muestra cómo lo vivió una familia. Un texto sobre el idioma muestra una continuidad. Al combinar, la explicación es más completa. Siempre decimos «según la fuente» y no generalizamos desde un solo caso.",
   "En estos temas hay emociones fuertes. Trabajar con empatía y respeto es leer los relatos con cuidado, evitar juzgar con ideas de hoy y no exigir a nadie que cuente su historia. Para proteger la privacidad usamos casos de ejemplo y cifras totales."],
  [("pregunta de análisis", "lo que quiero explicar, escrito con claridad"), ("hecho", "algo que ocurrió y se puede ubicar en el tiempo"), ("generalizar", "extender lo que vale para un caso a todos los casos"), ("reunificación", "unión de partes que estaban separadas")],
  [("Pasos 1 y 2", "{F} Ubica el hecho con sus fechas.", ["Alemania quedó dividida en dos Estados en 1949.", "Se reunificó el 3 de octubre de 1990."], "División en 1949 y reunificación el 3 de octubre de 1990"),
   ("Paso 3", "{F} Usa la fuente A para describir el cambio territorial.", ["En 1960 había 12 puntos de paso.", "En 1962 había 5 y en 1989 ninguno hasta noviembre."], "Los puntos de paso bajaron de 12 en 1960 a 5 en 1962 y a 0 en 1989")],
  [("Generalizar a toda la población desde un relato personal.", "Un relato muestra una vivencia, no todas.", "Escribe «según un relato de ejemplo…» y compara con otras fuentes."),
   ("Mirar solo el territorio y olvidar la identidad, o al revés.", "El conflicto cambia el espacio y la vida de las personas.", "Usa fuentes de ambos tipos.")],
  [("abc", "{F} ¿Qué dice la fuente A sobre los puntos de paso en 1989, hasta noviembre?", "Que no había ninguno (0)", "Que había 12", "Que había 5", "La fuente A anota 0 puntos de paso en 1989 hasta noviembre."),
   ("ab", "{F} ¿Qué tipo de fuente es la fuente B?", "Un relato personal", "Una tabla de datos", "Es el testimonio de una mujer de ejemplo."),
   ("=", "{F} ¿Cuántos puntos de paso menos había en 1962 que en 1960?", "12-5", "Se restan los puntos de paso de 1962 a los de 1960.", " puntos"),
   ("abc", "{F} ¿Qué paso del método usas al leer la fuente C, sobre el idioma?", "Paso 4: identidad", "Paso 3: territorio", "Paso 2: ubicar el hecho", "El idioma común es parte de la identidad y de las continuidades."),
   ("ab", "{F} ¿Qué continuidad señala la fuente C?", "El idioma común de las dos partes", "El muro", "La fuente C dice que las dos partes siguieron hablando el mismo idioma."),
   ("=", "{F} ¿Cuántos años pasaron entre la construcción del muro y la reunificación?", "1990-1961", "Se restan los años del muro y de la reunificación.", " años"),
   ("abc", "{F} ¿Qué se puede afirmar con la fuente B?", "Que una familia ficticia quedó separada y se reunió años después", "Que todas las familias de Alemania se separaron", "Que nadie volvió a verse", "Un relato personal sirve para ese caso, no para todos."),
   ("abc", "{F} ¿Qué pregunta de análisis tiene sentido para estas fuentes?", "¿Cómo cambió el territorio y la vida de las personas con la división de Alemania?", "¿Cuál es la moneda de Alemania hoy?", "¿Qué países producen más trigo en la actualidad?", "La pregunta debe relacionarse con lo que dicen las fuentes."),
   ("ab", "{F} ¿Qué dato muestra que el cambio fue grande?", "Que los puntos de paso bajaron hasta cero en 1989", "Que el idioma era el mismo", "La tabla muestra una disminución fuerte en los cruces."),
   ("abc", "Una persona dice: «Con la fuente B sé qué sintieron todos los habitantes de Berlín». ¿Cuál es la mejor respuesta?", "No: es un caso de ejemplo y no representa a todos", "Sí, un relato basta", "No existe ningún relato", "Un testimonio muestra una vivencia, no la de toda una población."),
   ("abc", "{F} ¿Qué conclusión prudente se puede escribir?", "La división cambió el territorio y separó a familias, aunque se mantuvo el idioma común", "La división no cambió nada", "Todos pensaban igual", "Combina cambios y continuidad según las tres fuentes."),
   ("abc", "{F} Si apareciera una tabla de ejemplo con más cruces autorizados en 1975, ¿qué haría una persona cuidadosa?", "Revisarla y ajustar lo que se afirma, si corresponde", "Ocultarla", "Cambiar los números", "Nuevos datos pueden matizar la conclusión."),
   ("abc", "{F} ¿Por qué se usan casos de ejemplo y cifras totales en el cuaderno?", "Para proteger la privacidad de las personas", "Para ocultar los hechos", "Para evitar fechas", "Así se evita exponer datos personales de las familias.")],
  ("abc", "Un archivo comunitario de ejemplo recibe tres cosas: una tabla de vecinos por año que vivían en una población, un relato de una vecina y una fotografía descrita de un letrero. ¿Qué paso del método usarías primero?", "Escribir la pregunta que se quiere responder", "Elegir un bando", "Descartar los relatos", "El primer paso es tener clara la pregunta."),
  [("¿Cuál es el primer paso para explicar con fuentes?", "Escribir la pregunta de análisis", "La pregunta orienta toda la búsqueda de fuentes."),
   ("¿Qué aporta una tabla y qué aporta un relato?", "La tabla muestra el tamaño del cambio y el relato cómo lo vivió una persona", "Una tabla y un relato se complementan entre sí."),
   ("¿Por qué no se debe generalizar desde un relato?", "Porque muestra una vivencia, no la de todos", "Hay otras experiencias que el relato no muestra.")],
  ("Con las fuentes A, B y C de la ficha, escribe una explicación de cinco líneas siguiendo los pasos: pregunta, hecho con fechas, cambio del territorio (con un dato), identidad (relato y continuidad) y conclusión prudente.",
   "Pregunta: ¿cómo cambiaron el territorio y la vida con la división de Alemania? Hecho: división en 1949 y reunificación en 1990. Territorio: los puntos de paso en Berlín bajaron de 12 en 1960 a 5 en 1962. Identidad: una familia ficticia quedó separada y las dos partes mantuvieron el idioma. Conclusión: hubo cambios fuertes y continuidades, según estas fuentes.",
   ["escribe los cinco pasos", "usa un dato de cada fuente", "no generaliza", "tono respetuoso"],
   ["cinco líneas numeradas"],
   ["generalizar desde un relato", "olvidar la identidad"],
   "Pregunta: «¿He usado las tres fuentes y dicho de cuál sale cada dato?»."),
  "Escribe una pregunta de análisis sobre cómo un cambio en tu barrio afectó la vida de las personas.",
  "Explica por qué conviene combinar tablas y relatos.")

# ====================================================== clase 4: practicar juntos con apoyo
F = ("Ficha 4 (datos escolares básicos y fuentes de ejemplo sobre la Guerra del Pacífico, 1879 a 1884, conflicto regional entre Chile, Perú y Bolivia; se presentan miradas de los tres países). "
     "Tabla de hechos: 1879, comienza la guerra; 1883, tratado de Ancón entre Chile y Perú; 1884, pacto de tregua entre Chile y Bolivia; 1904, tratado de paz y amistad entre Chile y Bolivia. "
     "Efecto territorial: Chile incorporó territorios que antes pertenecían a Perú y Bolivia, y Bolivia quedó sin costa. Hoy Bolivia plantea una demanda de acceso al mar y Chile sostiene que los tratados vigentes fijaron los límites. "
     "Fuente A (texto de ejemplo, mirada chilena): destaca que el 21 de mayo se recuerda el Combate Naval de Iquique. "
     "Fuente B (texto de ejemplo, mirada boliviana): destaca que el 23 de marzo se recuerda el Día del Mar y la demanda de acceso al mar. "
     "Fuente C (texto de ejemplo, mirada peruana): destaca la memoria de la pérdida de territorio y la defensa de ciudades.")
K(O, 4, F,
  "Hoy practico con apoyo cómo un conflicto regional dejó efectos en el territorio y en la memoria de tres países, con fuentes que miran desde lugares distintos.",
  ["La Guerra del Pacífico (1879 a 1884) fue un conflicto regional entre Chile, Perú y Bolivia. Terminó con tratados: el de Ancón (1883) con Perú, un pacto de tregua con Bolivia (1884) y, más tarde, un tratado de paz y amistad con Bolivia (1904). Cambió el territorio: Chile incorporó zonas del norte y Bolivia quedó sin acceso al mar.",
   "También configuró la identidad y la memoria de cada país. En Chile se recuerdan fechas como el 21 de mayo. En Bolivia el 23 de marzo se recuerda como Día del Mar y existe una demanda de acceso al mar; Chile sostiene que los tratados vigentes ya fijaron los límites. En Perú se recuerda la pérdida de territorio y la defensa de varias ciudades. Estas memorias no son idénticas, y una persona estudiosa las lee con respeto.",
   "Para practicar, comparamos las tres fuentes con una tabla: qué destaca cada una, qué efecto territorial menciona y qué fecha recuerda. Evitamos frases que ofendan a otros pueblos, no tomamos partido simplificando y usamos «según la fuente». La meta es entender por qué las memorias difieren, no decidir quién tiene la razón."],
  [("conflicto regional", "conflicto que afecta sobre todo a una región o a algunos países vecinos"), ("tratado", "acuerdo formal entre Estados"), ("memoria colectiva", "recuerdo compartido por una comunidad"), ("incorporar", "pasar a formar parte de un territorio o Estado")],
  [("Ubicar tratados", "{F} ¿Qué tratado se firmó en 1883 y entre quiénes?", ["Se busca 1883 en la tabla.", "Fue el tratado de Ancón, entre Chile y Perú."], "El tratado de Ancón, entre Chile y Perú"),
   ("Comparar memorias", "{F} ¿Qué fecha destaca la fuente B?", ["La fuente B tiene mirada boliviana.", "Destaca el 23 de marzo, Día del Mar."], "El 23 de marzo, Día del Mar")],
  [("Sostener que hay una sola memoria correcta de la guerra.", "Cada país conserva recuerdos propios.", "Compara las fuentes y explica por qué difieren."),
   ("Usar insultos hacia otro país o pueblo.", "No ayuda a comprender y ofende.", "Usa un lenguaje respetuoso y basado en datos.")],
  [("abc", "{F} ¿En qué año comenzó la Guerra del Pacífico?", "1879", "1883", "1904", "La tabla de hechos indica 1879."),
   ("ab", "{F} ¿Qué efecto territorial menciona la ficha para Bolivia?", "Quedó sin costa", "Ganó territorio en el norte", "La ficha dice que Bolivia quedó sin costa."),
   ("=", "{F} ¿Cuántos años duró la guerra, entre 1879 y 1884?", "1884-1879", "Se restan el año de inicio y el de la tregua con Bolivia.", " años"),
   ("abc", "{F} ¿Qué fecha destaca la fuente A?", "El 21 de mayo, Combate Naval de Iquique", "El 23 de marzo", "El 11 de septiembre", "La fuente A menciona el 21 de mayo."),
   ("ab", "{F} ¿Qué mira destaca la fuente C?", "La memoria de la pérdida de territorio y la defensa de ciudades", "El Día del Mar", "La fuente C tiene mirada peruana y destaca esos hechos."),
   ("=", "{F} ¿Cuántos años pasaron entre el tratado de Ancón y el tratado de paz y amistad con Bolivia?", "1904-1883", "Se restan los años de ambos tratados de la ficha.", " años"),
   ("abc", "{F} ¿Qué conflicto fue la Guerra del Pacífico?", "Un conflicto regional entre Chile, Perú y Bolivia", "Una guerra mundial", "Una revolución industrial", "La ficha lo describe como regional entre tres países."),
   ("abc", "{F} ¿Por qué las tres fuentes destacan cosas distintas?", "Porque cada una mira desde la memoria de su país", "Porque dos son falsas", "Porque no hablan del mismo hecho", "Las memorias pueden ser diferentes sobre un mismo hecho."),
   ("ab", "{F} ¿Qué es un tratado?", "Un acuerdo formal entre Estados", "Una declaración de guerra", "Un tratado fija términos del fin de un conflicto."),
   ("abc", "Una compañera dice: «Solo la fuente A es válida». ¿Qué respuesta es mejor?", "Cada fuente aporta una mirada, y se leen todas con respeto para comprender", "Tiene razón", "Hay que ocultar B y C", "Comparar miradas ayuda a entender el conflicto."),
   ("abc", "{F} ¿Qué se puede afirmar con la tabla sobre el territorio?", "Que cambió el territorio chileno y que Bolivia perdió su acceso al mar", "Que no cambió nada", "Que Perú ganó toda la costa", "La ficha lo indica como efecto territorial."),
   ("abc", "{F} Una persona escribe un insulto a otro país. ¿Qué corresponde?", "Reemplazarlo por una descripción con datos y respeto", "Dejarlo", "Publicarlo", "Un lenguaje respetuoso es parte del método."),
   ("abc", "{F} ¿Qué pregunta de análisis tiene sentido para las tres fuentes?", "¿Cómo configuró la guerra el territorio y las memorias de los tres países?", "¿Cuántos habitantes tiene hoy cada país?", "¿Qué país produce más cobre en la actualidad?", "Relaciona territorio y memoria, como piden las fuentes.")],
  ("abc", "Una escuela de adultos de ejemplo prepara un panel sobre la Guerra del Pacífico para estudiantes de los tres países. ¿Cuál es la mejor forma de presentarlo?", "Mostrar hechos con fechas, las tres miradas por separado y un lenguaje respetuoso", "Mostrar solo una mirada", "Usar burlas para captar atención", "Mostrar hechos y varias miradas con respeto favorece la comprensión."),
  [("¿Qué es un conflicto regional?", "Uno que afecta sobre todo a una región o a países vecinos", "Su alcance no es global sino de una región."),
   ("¿Qué es la memoria colectiva?", "El recuerdo compartido por una comunidad", "Puede variar entre una comunidad y otra."),
   ("¿Por qué se leen varias fuentes sobre un mismo conflicto?", "Porque muestran distintas miradas y completan la comprensión", "Una sola fuente es siempre una mirada incompleta.")],
  ("Con la ficha, completa una tabla de tres filas (fuente A, B, C) con tres columnas: país, fecha o hecho que destaca, y efecto en la memoria. Después escribe dos frases: una sobre el efecto en el territorio y otra sobre por qué las memorias difieren. Usa un tono respetuoso.",
   "A: Chile, 21 de mayo, recuerdo del Combate Naval de Iquique. B: Bolivia, 23 de marzo, Día del Mar y demanda de acceso al mar. C: Perú, memoria de la pérdida de territorio y defensa de ciudades. Territorio: Chile incorporó territorios y Bolivia quedó sin costa. Las memorias difieren porque cada país vivió la guerra desde su situación.",
   ["completa tres filas con datos de la ficha", "explica el efecto en el territorio", "explica por qué las memorias difieren", "usa lenguaje respetuoso"],
   ["tabla de tres filas y dos frases"],
   ["tomar partido con insultos", "inventar datos"],
   "Pregunta: «¿Mi frase respeta a las personas de los tres países?»."),
  "Anota una fecha que tu familia o tu comunidad recuerde de manera especial y por qué.",
  "Explica con un ejemplo por qué dos memorias distintas no siempre se contradicen del todo.")

# ====================================================== clase 5: aplicar a una situación de trabajo, hogar o comunidad
F = ("Ficha 5 (situación de ejemplo con datos inventados). Una junta de vecinos de un barrio ficticio, «La Vega», prepara una exposición llamada «Barrio de llegadas». "
     "Tabla de ejemplo: procedencia de las familias que se instalaron en La Vega según la década. Década de 1960: 20 familias del campo cercano. Década de 1970: 15 familias del campo y 10 de otras ciudades del país. "
     "Década de 1990: 12 familias que volvieron al país después de haber vivido fuera. Década de 2010: 30 familias que llegaron de otros países. "
     "Fuente A (relato de ejemplo): una vecina ficticia cuenta que volvió a Chile en la década de 1990 después de haber vivido fuera y que se sintió acogida por su cuadra. "
     "Fuente B (relato de ejemplo): un vecino ficticio cuenta que llegó de otro país en la década de 2010 y que sigue celebrando una fiesta de su tierra. "
     "Regla de la junta: no se publican nombres ni direcciones.")
K(O, 5, F,
  "Hoy aplico lo aprendido a una situación de comunidad: explicar con una tabla y dos relatos cómo las migraciones y los retornos han configurado la identidad de un barrio.",
  ["Los conflictos del siglo XX y otros procesos han movido a muchas personas: unas migraron del campo a la ciudad, otras salieron del país y algunas volvieron, y hoy llegan personas de otros países. Cada llegada trae costumbres, lenguas y fiestas, y cambia el barrio. Por eso la identidad de un barrio no es fija: se construye con la suma de historias.",
   "Para explicar este proceso en una exposición comunitaria usamos una tabla (cuántas familias llegaron y de dónde) y relatos (cómo lo vivieron). La tabla da el panorama y los relatos humanizan los datos. Pero tenemos cuidados: pedir permiso, no publicar nombres ni direcciones, no suponer lo que siente cada persona y evitar frases que dividan entre «los de aquí» y «los de afuera».",
   "También es una oportunidad de convivencia. Una explicación respetuosa muestra qué se aporta entre todas las personas, qué desafíos hay y qué puede hacer la comunidad para acoger. Y deja claro que los relatos son casos y no representan a todos los grupos."],
  [("procedencia", "lugar de donde viene una persona o una familia"), ("retorno", "vuelta al país o al lugar de origen"), ("convivencia", "vida en común entre personas distintas"), ("acoger", "recibir a una persona con respeto y apoyo"), ("exposición", "muestra pública de información")],
  [("Leer la tabla", "{F} ¿Cuántas familias de otros países llegaron en la década de 2010?", ["Se busca la década de 2010.", "La tabla indica 30 familias."], "30 familias"),
   ("Sumar", "{F} ¿Cuántas familias llegaron en total en las décadas de 1960 y 1970?", ["Década de 1960: 20 familias.", "Década de 1970: 15 + 10 = 25; total 20 + 25 = 45."], "45 familias")],
  [("Escribir «los de afuera» y «los de aquí» como si fueran grupos opuestos.", "Divide a la comunidad y no describe hechos.", "Usa descripciones neutras y datos de procedencia."),
   ("Publicar el relato de una persona con su nombre y dirección.", "Se exponen datos personales.", "Pide permiso y usa casos de ejemplo.")],
  [("abc", "{F} ¿Cuántas familias volvieron al país en la década de 1990?", "12", "20", "30", "La tabla indica 12 familias que volvieron en la década de 1990."),
   ("ab", "{F} ¿Qué regla tiene la junta con los datos personales?", "No se publican nombres ni direcciones", "Se publican todos los datos", "La ficha establece que no se publican nombres ni direcciones."),
   ("=", "{F} ¿Cuántas familias en total llegaron a La Vega en las cuatro décadas de la tabla?", "20+15+10+12+30", "Se suman todas las familias de las cuatro décadas de la tabla.", " familias"),
   ("abc", "{F} ¿Qué dice el relato de la fuente A?", "Que una vecina volvió a Chile y se sintió acogida por su cuadra", "Que un vecino se fue del barrio", "Que se cerró la junta", "La ficha resume el relato de una vecina que volvió."),
   ("ab", "{F} ¿Qué muestra la fuente B?", "Que una persona que llegó de otro país mantiene una fiesta de su tierra", "Que nadie conserva costumbres", "El relato muestra una continuidad cultural."),
   ("=", "{F} ¿Cuántas familias más llegaron en la década de 2010 que en la década de 1990?", "30-12", "Se resta lo de la década de 1990 a lo de la década de 2010.", " familias"),
   ("abc", "{F} ¿Qué patrón de procedencia se ve entre 1960 y 2010?", "Pasó de familias del campo cercano a familias de otros países", "Solo llegaron familias del campo", "Nadie llegó", "La tabla muestra que cambió la procedencia con el tiempo."),
   ("abc", "{F} ¿Cuál es la mejor frase para la exposición sobre la identidad del barrio?", "«La identidad de La Vega se construye con las historias de familias de distinta procedencia»", "«Los de afuera cambiaron el barrio»", "«El barrio nunca cambió»", "Es neutra, está apoyada en la tabla y respeta a todas las personas."),
   ("ab", "{F} ¿Qué cuidado ético corresponde con los relatos?", "Pedir permiso y no exponer datos personales", "Publicarlos sin consultar", "Respeta la privacidad de quienes los cuentan."),
   ("abc", "Un vecino propone titular la exposición «Los extranjeros llegaron a quitarnos el espacio». ¿Qué observación respetuosa corresponde?", "Ese título divide y no se apoya en la tabla; mejor uno que muestre la suma de historias", "Es un excelente título", "Hay que poner un título más fuerte", "El título debe describir con datos y no generar rechazo."),
   ("abc", "{F} ¿Qué dato podría completar la exposición?", "Qué actividades comparten las familias hoy, como una feria o un comité", "La dirección exacta de cada familia", "Los nombres de las familias", "Se complementa con información que no expone a nadie."),
   ("abc", "{F} Una visitante dice: «Esto prueba que todas las personas que llegaron de otros países se sienten igual». ¿Qué falla?", "Es un relato de ejemplo y no representa a todas las personas", "Nada", "Los relatos nunca valen", "Un solo caso no permite generalizar a todos."),
   ("abc", "{F} Si la junta quiere mostrar cómo los conflictos influyeron en el barrio, ¿qué fuente adicional ayudaría?", "Un testimonio, con permiso, sobre por qué salió o llegó una persona", "Un rumor sin fuente conocida", "Una lista con direcciones", "Ayuda a vincular movimientos de personas con procesos más amplios.")],
  ("abc", "Un centro comunitario de ejemplo prepara una muestra con fotos descritas y relatos de socios sobre cómo cambió su barrio. Un socio no quiere que se publique su relato. ¿Qué corresponde?", "Respetar su decisión y no publicarlo", "Publicarlo igual", "Insistir para que acepte", "La participación en estos temas debe ser siempre voluntaria."),
  [("En la exposición del barrio: ¿qué es la procedencia?", "El lugar de donde viene una persona o una familia", "Se usa para describir movimientos de población."),
   ("¿Qué cuidados éticos hay con relatos de personas?", "Pedir permiso y no exponer datos personales", "Estos cuidados protegen la privacidad de las personas."),
   ("¿Por qué evitar «los de afuera» y «los de aquí»?", "Porque divide y no describe con datos", "Una descripción neutra respeta a todas las personas.")],
  ("Prepara el texto de la exposición «Barrio de llegadas» (cinco a siete líneas): usa tres cifras de la tabla, una idea de cada relato, una frase sobre la identidad del barrio y una pregunta final de convivencia. No incluyas nombres ni direcciones.",
   "En La Vega llegaron 20 familias del campo en la década de 1960 y 30 familias de otros países en la década de 2010. Una vecina cuenta que volvió en la década de 1990 y se sintió acogida; un vecino mantiene una fiesta de su tierra. La identidad del barrio se construye con muchas historias. ¿Qué podemos hacer para acoger a quienes llegan?",
   ["usa tres cifras de la tabla", "incluye una idea de cada relato", "no publica datos personales", "usa lenguaje respetuoso"],
   ["texto de cinco a siete líneas"],
   ["dividir entre «los de afuera» y «los de aquí»", "exponer datos personales"],
   "Pregunta: «¿Esta frase suma o divide a la comunidad?»."),
  "Anota una costumbre de otro lugar que hayas conocido en tu barrio y qué aporta.",
  "Explica cómo los movimientos de personas pueden cambiar la identidad de un barrio.")

# ====================================================== clase 6: revisar lo logrado y decidir los pasos siguientes
F = ("Ficha 6 (síntesis y fuentes de ejemplo). Tabla de hechos: 1919 y 1920, tratados cambian fronteras en Europa; 1945, creación de la ONU; 1949 a 1990, Alemania dividida; décadas de 1950 y 1960, descolonización; 1973 a 1990, régimen militar en Chile; 1879 a 1884, Guerra del Pacífico. "
     "Fuente A (tabla de ejemplo): en la década de 1950, 8 territorios se independizaron en cierta región; en la década de 1960, 24. "
     "Fuente B (relato de ejemplo): una persona ficticia cuenta que su ciudad cambió de país tras un tratado y que mantuvo su idioma y su fiesta. "
     "Afirmación de un texto de ejemplo: «Los conflictos solo cambiaron los territorios, nunca la identidad de las personas».")
K(O, 6, F,
  "Hoy reviso lo logrado: explico con fuentes cómo los conflictos configuraron territorios e identidades y decido qué reforzar.",
  ["En este módulo aprendiste a explicar cómo los conflictos globales y regionales cambiaron el territorio (fronteras, Estados nuevos, divisiones) y la identidad (migraciones, exilios, memorias, símbolos y fiestas). También aprendiste que hay continuidades: a pesar de los cambios, muchas comunidades conservan su lengua, sus fiestas y sus costumbres.",
   "Una explicación sólida usa fuentes de distintos tipos y las cita. Una tabla muestra el tamaño de un cambio, un relato muestra una vivencia y un texto de ejemplo puede mostrar una continuidad. Un texto de la ficha dice que los conflictos solo cambiaron los territorios y nunca la identidad. La fuente B muestra una continuidad, pero otros ejemplos del módulo muestran cambios en la identidad, como los exilios y las migraciones. La afirmación es demasiado absoluta.",
   "Para seguir avanzando, anota qué conceptos recuerdas bien, cuáles confundes y qué harás. Puedes explicar un caso a otra persona, hacer tarjetas con fechas y practicar escribir una explicación de cinco líneas con una tabla y un relato. Seguir con respeto estos temas es parte del aprendizaje."],
  [("explicación", "texto que dice cómo y por qué ocurrió algo, con evidencia"), ("afirmación absoluta", "frase que dice «siempre» o «nunca» sin matices"), ("matiz", "detalle que muestra que algo no es totalmente blanco o negro"), ("síntesis", "resumen de lo más importante")],
  [("Evaluar una afirmación", "{F} ¿Es sólida la afirmación del texto de ejemplo?", ["Dice «solo» y «nunca», sin matices.", "Hay ejemplos de cambios en la identidad, como exilios y migraciones."], "No: es demasiado absoluta, porque los conflictos también cambiaron identidades"),
   ("Calcular", "{F} ¿Cuántos territorios más se independizaron en la década de 1960 que en la de 1950 según la fuente A?", ["Valores: 24 y 8.", "24 − 8 = 16."], "16 territorios más")],
  [("Repetir una afirmación de «siempre» o «nunca» sin revisarla.", "Pocas cosas son absolutas.", "Busca ejemplos que la contradigan y matiza."),
   ("Explicar solo con tablas y olvidar a las personas.", "La identidad se ve en vivencias y relatos.", "Combina tablas y relatos.")],
  [("abc", "{F} ¿Qué mide la fuente A?", "La cantidad de territorios que se independizaron por década", "Los habitantes de cada territorio", "El número de tratados firmados", "La fuente A es una tabla de independencias por década."),
   ("ab", "{F} ¿Qué muestra la fuente B?", "Una continuidad: la ciudad cambió de país, pero mantuvo su idioma y su fiesta", "Que la identidad desapareció", "El relato menciona el idioma y la fiesta mantenidos."),
   ("=", "{F} ¿Cuántos territorios se independizaron en total en las décadas de 1950 y 1960, según la fuente A?", "8+24", "Se suman los territorios de las dos décadas de la fuente A.", " territorios"),
   ("abc", "{F} ¿Qué proceso muestran las décadas de 1950 y 1960 en la tabla de hechos?", "La descolonización", "La Guerra del Pacífico", "La división de Alemania", "La ficha lo ubica en esas décadas."),
   ("ab", "{F} ¿Cuál es un efecto en el territorio?", "El cambio de fronteras en Europa tras los tratados de 1919 y 1920", "El recuerdo de una fiesta", "Las fronteras son parte del territorio."),
   ("=", "{F} ¿Cuántos años pasaron entre el término de la Guerra del Pacífico (1884) y la creación de la ONU (1945)?", "1945-1884", "Se restan los años de ambos hechos de la ficha.", " años"),
   ("abc", "{F} ¿En qué década se independizaron más territorios, según la fuente A?", "En la década de 1960, con 24", "En la década de 1950, con 8", "En ambas por igual", "La fuente A anota 24 territorios en 1960 y 8 en 1950."),
   ("abc", "{F} ¿Por qué conviene combinar la fuente A y la fuente B?", "Porque la tabla da el tamaño del cambio y el relato da la vivencia", "Porque son idénticas", "Porque una de las dos es falsa", "Una tabla y un relato se complementan entre sí."),
   ("ab", "{F} ¿Qué palabra de la afirmación la hace demasiado absoluta?", "«Nunca»", "«Los»", "La palabra «nunca» no admite excepciones."),
   ("abc", "Una compañera dice: «Siempre que hay una frontera nueva, la identidad desaparece». ¿Qué corrección es mejor?", "A veces cambia y a veces se mantiene; hay que mirar cada caso con fuentes", "Tiene razón", "Nunca cambia", "Se matiza la frase con evidencia de cada caso."),
   ("abc", "{F} ¿Cuál es una conclusión prudente con A y B?", "Los conflictos cambiaron territorios y hubo comunidades que mantuvieron elementos de su identidad", "Todas las comunidades perdieron su identidad", "Nada cambió en ningún lugar", "Combina cambios y continuidades según las fuentes."),
   ("abc", "{F} Al explicar el efecto del régimen militar en Chile sobre las personas, ¿qué conviene hacer?", "Usar fuentes variadas y mencionar que existen distintas memorias, con respeto", "Imponer una sola memoria", "Insultar a quien piense distinto", "Se respeta la pluralidad y se usan fuentes."),
   ("abc", "Al terminar el módulo, ¿qué muestra mejor que aprendiste?", "Escribir una explicación con una tabla, un relato y una conclusión prudente", "Repetir una frase aprendida", "Decir que no hay nada que explicar", "Aplica el método completo con tabla y relato.")],
  ("abc", "Una biblioteca comunitaria de ejemplo prepara un taller de memoria. Quiere partir con una frase que recoja varias miradas. ¿Cuál es la mejor?", "«Cada persona recuerda estos hechos desde su vivencia, y las fuentes nos ayudan a comprender más»", "«Solo una versión es correcta»", "«Es mejor no recordar»", "Reconoce la pluralidad y el valor de las fuentes."),
  [("¿Qué es una afirmación absoluta?", "Una frase con «siempre» o «nunca» sin matices", "Por eso hay que revisarla con evidencia."),
   ("¿Qué conviene incluir en una explicación sólida?", "Fuentes de distintos tipos, citadas, y una conclusión prudente", "Cada fuente da evidencia que sostiene la explicación."),
   ("¿Qué muestra una continuidad en un conflicto?", "Lo que se mantiene a pesar de los cambios", "Mostrar las continuidades matiza mucho la explicación.")],
  ("Haz tu cierre del módulo en cinco a ocho líneas: (a) escribe una explicación breve de cómo un conflicto de la tabla de hechos cambió el territorio y una identidad, con un dato y una continuidad; (b) corrige la afirmación del texto de ejemplo; (c) anota qué te cuesta más y cómo lo practicarás.",
   "(a) La división de Alemania (1949 a 1990) cambió el territorio con un muro y separó familias; el idioma común se mantuvo. (b) No es cierto que los conflictos nunca cambien la identidad, porque hubo exilios y migraciones, aunque también continuidades. (c) Me cuesta distinguir cambios de continuidades; practicaré con casos de mi barrio.",
   ["explica un caso con dato y continuidad", "corrige la afirmación con matices", "identifica una dificultad y un plan", "usa lenguaje respetuoso"],
   ["texto de cinco a ocho líneas"],
   ["generalizar desde un caso", "no matizar"],
   "Pregunta: «¿Dije cuál fuente respalda cada frase?»."),
  "Repasa con tarjetas cinco hechos de la tabla de la ficha durante tres días.",
  "Explica a otra persona por qué las memorias de una comunidad pueden ser distintas y por qué se escuchan todas con respeto.")
