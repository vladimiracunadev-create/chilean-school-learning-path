"""Material del estudiante de 2.º medio, Historia, Geografía y Ciencias Sociales: OA 05 (crisis parlamentaria y Constitución de 1925) y OA 06 (Gran Depresión, industrialización y Estado social en Chile)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 05"

# ================================================================ OA 05, clase 1
F = ("Ficha 1 (el período parlamentario). "
     "Hechos: tras la guerra civil de 1891 comienza el período parlamentario, que dura hasta la Constitución de 1925. "
     "En esos años el Congreso tiene mucho poder: puede censurar a los ministros, es decir, votar contra ellos, y los ministros suelen renunciar; por eso los gabinetes (equipos de ministros) duran poco. "
     "En 1907 ocurre la matanza de trabajadores del salitre en Iquique. En 1920 es elegido presidente Arturo Alessandri. En 1925 se aprueba una nueva Constitución. "
     "Actores: presidente, Congreso, partidos políticos, trabajadores, clase media y Fuerzas Armadas. Dato de ejemplo: en un año se formaron 6 gabinetes.")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo la crisis del período parlamentario y a reconocer quiénes eran sus actores y qué poder tenía cada uno.",
    prior=["Sé ubicar un año en su siglo y calcular diferencias entre años.", "Sé que una constitución es la ley principal de un país.", "Conozco la diferencia entre presidente y Congreso."],
    explain=[
        "El período parlamentario es la etapa de la historia de Chile que va desde la guerra civil de 1891 hasta la Constitución de 1925. Su rasgo central es que el Congreso, formado por diputados y senadores, tenía más poder que el presidente. El Congreso podía censurar a los ministros, es decir, votar en su contra, y entonces estos solían renunciar.",
        "Como los ministros caían con facilidad, los gabinetes duraban poco y los gobiernos tenían dificultades para cumplir sus planes. Mientras tanto, los problemas sociales crecían: los trabajadores del salitre y de las ciudades protestaban por sus condiciones de vida, y en 1907 una protesta terminó en la matanza de Iquique. A esto se le llama la crisis del sistema político.",
        "Para estudiar el tema conviene separar a los actores: el presidente, el Congreso, los partidos, los trabajadores, la clase media y las Fuerzas Armadas. Cada uno tenía intereses distintos. Una buena pregunta histórica une tiempo y problema: ¿por qué un sistema que dio poder al Congreso terminó en crisis y fue reemplazado en 1925?",
    ],
    vocab=[("período parlamentario", "etapa chilena de 1891 a 1925 en que el Congreso tenía más poder que el presidente"), ("censurar", "votar en contra de un ministro, de modo que suele renunciar"), ("gabinete", "equipo de ministros que acompaña al presidente"), ("Constitución", "ley principal de un país, que organiza el poder y reconoce derechos"), ("actor", "persona o grupo que participa e influye en un proceso histórico")],
    worked=[
        ("Ubicar un hecho en el período", "La matanza de trabajadores en Iquique ocurrió en 1907. ¿Cae dentro del período parlamentario?", ["El período va de 1891 a 1925.", "El año 1907 está entre esos dos años."], "Sí, 1907 está dentro del período"),
        ("Reconocer un rasgo", "Un ministro renuncia después de que la mayoría del Congreso vota contra él. ¿Qué rasgo del período muestra?", ["El Congreso censura al ministro.", "Eso indica que el Congreso controla al gobierno."], "El poder del Congreso sobre el gobierno"),
    ],
    mistakes=[("Decir que el período parlamentario comenzó en 1925.", "Se confunde el final del período con su comienzo.", "Recuerda: comienza en 1891 y la Constitución de 1925 lo cierra."),
              ("Creer que en el período parlamentario el presidente mandaba sin control.", "Se mezcla con otras etapas en que el presidente tenía más poder.", "Pregunta quién podía censurar a los ministros: el Congreso.")],
    T=[
        ("{F} ¿Qué años delimitan el período parlamentario según la ficha?", "1891 y 1925", "La ficha lo sitúa entre la guerra civil de 1891 y la Constitución de 1925."),
        ("{F} ¿Qué podía hacer el Congreso con los ministros?", "Censurarlos, es decir, votar en su contra", "La ficha lo dice como rasgo central del período."),
        ("{F} ¿Qué año fue elegido presidente Arturo Alessandri?", "1920", "La ficha lo indica entre los hechos."),
        ("=", "{F} ¿Cuántos años duró el período parlamentario?", "1925-1891", "Se resta el año de inicio al año de término.", " años"),
        ("{F} ¿Qué consecuencia tenía la facilidad para censurar ministros? A) Gabinetes de corta duración B) Presidentes que gobernaban sin Congreso", "A) Gabinetes de corta duración", "Si los ministros renuncian con facilidad, los gabinetes duran poco."),
        ("{F} ¿Qué actor representa mejor a quienes protestan por sus condiciones de trabajo? A) Los trabajadores B) El Congreso", "A) Los trabajadores", "Las protestas del salitre las hicieron trabajadores."),
        ("=", "{F} Con el dato de ejemplo de la ficha, ¿cuántos meses duró en promedio cada gabinete de ese año?", "12/6", "Se reparten los 12 meses entre los 6 gabinetes.", " meses"),
        ("{F} En una línea de tiempo de 1891 a 1925, ¿dónde queda 1920? A) Cerca del final, a cinco años de 1925 B) A la mitad del período, en torno a 1908", "A) Cerca del final, a cinco años de 1925", "De 1920 a 1925 pasan cinco años; la mitad del período sería 1908."),
        ("{F} Alguien dice: «En el período parlamentario Chile era una dictadura». ¿Qué corrección corresponde? A) El Congreso tenía mucho poder y podía censurar a los ministros, así que no gobernaba una sola persona B) Es correcto porque había un presidente", "A) El Congreso tenía mucho poder y podía censurar a los ministros, así que no gobernaba una sola persona", "La ficha describe un Congreso fuerte, no un gobierno de una sola persona."),
        ("{F} ¿Por qué es un error decir que el período parlamentario comenzó con la Constitución de 1925?", "Porque en 1925 el período terminó; había comenzado en 1891", "La ficha ubica la Constitución al final del período."),
        ("{F} Un compañero afirma: «En 1907 el Congreso aprobó la Constitución». ¿Se puede sostener con la ficha? A) No, en 1907 ocurrió la matanza de Iquique y la Constitución es de 1925 B) Sí, porque 1907 está dentro del período", "A) No, en 1907 ocurrió la matanza de Iquique y la Constitución es de 1925", "Estar dentro del período no prueba que ese hecho haya ocurrido en ese año."),
        ("{F} ¿Qué información de la ficha apoya mejor la idea de que el sistema tenía problemas? A) Gabinetes que duraban poco y una matanza de trabajadores en 1907 B) La existencia de partidos políticos", "A) Gabinetes que duraban poco y una matanza de trabajadores en 1907", "Muestran inestabilidad y un conflicto social grave; tener partidos no es un problema."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Por qué el sistema político de 1891 a 1925 entró en crisis y se reemplazó? B) ¿Quién fue el político más simpático del período?", "A) ¿Por qué el sistema político de 1891 a 1925 entró en crisis y se reemplazó?", "La primera pregunta se responde con hechos y tiempo; la segunda es una opinión."),
    ],
    ctx=("Un panel escolar dice: «En el período parlamentario ningún grupo social protestó». ¿Qué dato de la ficha lo contradice? A) La matanza de trabajadores de 1907 B) La elección de 1920", "A) La matanza de trabajadores de 1907", "Esa matanza ocurrió tras una protesta de trabajadores."),
    sc=[("¿Qué es censurar a un ministro?", "Votar en su contra, de modo que suele renunciar", "Así se define en el vocabulario."),
        ("¿Qué es un gabinete?", "El equipo de ministros que acompaña al presidente", "Así se define en la clase."),
        ("En Historia: ¿qué es un actor?", "Una persona o grupo que participa e influye en un proceso histórico", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo con la escala 1 cm = 5 años, de 1891 a 1925. Marca con una raya y su nombre: guerra civil (1891), matanza de Iquique (1907), elección de Alessandri (1920) y Constitución (1925). Debajo escribe una frase que explique por qué los gabinetes duraban poco. {F}",
        "Posiciones desde 1891: 0 cm; 3,2 cm; 5,8 cm; 6,8 cm. Frase: «Los gabinetes duraban poco porque el Congreso podía censurar a los ministros y estos renunciaban».",
        ["respeta la escala", "ubica los cuatro hitos", "la frase usa la censura de ministros"], ["línea de tiempo dibujada", "frase escrita"], ["poner los hitos sin medir", "explicar la corta duración sin nombrar la censura"],
        "Pide que explique por qué la matanza de 1907 se considera parte de la crisis y no solo un hecho aislado."),
    reinforce="Explica en voz alta qué era el período parlamentario y por qué los gabinetes duraban poco.",
    extend="Averigua en tu casa qué cargo tiene hoy el jefe del gobierno de Chile y si el Congreso puede hacerlo renunciar.",
)

# ================================================================ OA 05, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
     "Fuente A, discurso de un senador, 1913: «El Congreso vigila al gobierno; si un ministro falla, debe caer. Así se evita el abuso de un presidente.» "
     "Fuente B, carta de un empleado público a un diario, 1921: «Los gabinetes cambian cada pocas semanas y la ley sobre los sueldos nunca se vota.» "
     "Fuente C, manifiesto de jóvenes oficiales del ejército, 1924: «Exigimos que se aprueben leyes sociales y que cesen las discusiones sin resultados.» "
     "Hecho real: en septiembre de 1924 oficiales presionaron al Congreso para que votara leyes sociales; se conoce como «ruido de sables».")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre la crisis parlamentaria: quién las escribe, cuándo, para qué, y qué conclusión permiten y cuál no.",
    prior=["Sé situar el período parlamentario entre 1891 y 1925.", "Sé que una fuente es una huella del pasado.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Interrogar una fuente es hacerle preguntas antes de creerle. La procedencia es el conjunto de datos de su origen: quién la escribió, en qué fecha, para quién y con qué propósito. Un senador que defiende al Congreso no mira el sistema igual que un empleado público que sufre la falta de leyes o que un oficial que quiere presionar. Todos hablan desde su lugar.",
        "También hay que separar lo que la fuente describe de lo que interpreta. Describir es decir qué ocurre: «los gabinetes cambian cada pocas semanas». Interpretar es dar una explicación u opinión: «el Congreso abusa». Una sola fuente no basta para probar un proceso entero, porque muestra solo una parte. Por eso se compara con otras.",
        "Finalmente, la conclusión debe ser proporcional a la evidencia. Si una carta dice que los gabinetes cambian rápido, no prueba por sí sola cuántos cambiaron ni por qué. Se puede concluir que a su autor le preocupaba la inestabilidad y que otras fuentes deberían confirmar el dato. Así se evita decir más de lo que la fuente permite.",
    ],
    vocab=[("procedencia", "datos del origen de una fuente: autor, fecha, destinatario y propósito"), ("propósito", "lo que el autor busca lograr con su texto"), ("describir", "decir qué ocurre sin dar opinión"), ("interpretar", "dar una explicación u opinión sobre lo ocurrido"), ("conclusión proporcional", "conclusión que no dice más de lo que la evidencia permite")],
    worked=[
        ("Identificar procedencia y propósito", "Fuente de ejemplo: discurso de un ministro, 1910: «Pido al Congreso más tiempo para cumplir mi programa». ¿Quién habla y qué busca?", ["Habla un ministro, autoridad del gobierno.", "Pide más tiempo al Congreso, así que busca que no lo censuren."], "Un ministro que busca no ser censurado"),
        ("Separar descripción e interpretación", "Frase de ejemplo: «Hoy cayó otro gabinete, lo que demuestra que los políticos son incapaces». ¿Qué parte describe?", ["«Hoy cayó otro gabinete» dice qué ocurrió.", "«Los políticos son incapaces» es una opinión."], "Describe: cayó otro gabinete"),
    ],
    mistakes=[("Creer una fuente solo porque es antigua.", "Se confunde antigüedad con verdad.", "Pregunta quién la escribió, para qué y qué otras fuentes la confirman."),
              ("Concluir que una carta prueba lo que ocurrió en todo el país.", "Se generaliza desde un solo testimonio.", "Presenta la carta como evidencia de lo que una persona vivió y busca otras fuentes.")],
    T=[
        ("{F} ¿Quién escribe la Fuente B?", "Un empleado público", "La ficha lo indica en su procedencia."),
        ("{F} ¿En qué año está fechada la Fuente C?", "1924", "La fecha aparece junto a la fuente."),
        ("{F} ¿Qué pide la Fuente C?", "Que se aprueben leyes sociales y que cesen las discusiones sin resultados", "El manifiesto lo exige en su texto."),
        ("{F} ¿Qué defiende el senador de la Fuente A? A) Que el Congreso vigile y pueda hacer caer a los ministros B) Que el presidente mande sin control", "A) Que el Congreso vigile y pueda hacer caer a los ministros", "El discurso dice que el Congreso vigila para evitar abusos."),
        ("{F} En la Fuente B, ¿qué frase describe un hecho? A) «Los gabinetes cambian cada pocas semanas» B) Ninguna, toda la carta es opinión", "A) «Los gabinetes cambian cada pocas semanas»", "Dice qué ocurre; el autor además opina, pero esa frase es descriptiva."),
        ("{F} ¿Qué fuente muestra la mirada de quien quiere que el Congreso cambie su forma de trabajar? A) Fuente C B) Fuente A", "A) Fuente C", "Los oficiales exigen que cesen las discusiones sin resultados; el senador defiende al Congreso."),
        ("{F} ¿Qué hecho real de septiembre de 1924 menciona la ficha? A) El «ruido de sables» B) La matanza de Iquique", "A) El «ruido de sables»", "La ficha lo presenta como presión de oficiales al Congreso; la matanza de Iquique es de 1907."),
        ("{F} Un compañero dice: «La Fuente B prueba que en todo Chile los gabinetes duraban semanas». ¿Qué responde? A) Solo muestra lo que vio un empleado y hay que buscar más fuentes B) Tiene razón porque es una carta publicada", "A) Solo muestra lo que vio un empleado y hay que buscar más fuentes", "Un testimonio no prueba por sí solo un proceso nacional."),
        ("{F} Un aviso de ejemplo de 1913 dice: «Compre sombreros a buen precio». ¿Sirve para saber si el Congreso vigilaba al gobierno? A) No, su propósito es vender sombreros B) Sí, porque es de 1913", "A) No, su propósito es vender sombreros", "La procedencia y el propósito del aviso no se relacionan con la pregunta."),
        ("{F} ¿Por qué la Fuente A y la Fuente C llegan a ideas distintas sobre el Congreso?", "Porque sus autores tienen lugares e intereses distintos: uno es senador y otros son oficiales que quieren leyes", "La procedencia explica el punto de vista de cada autor."),
        ("{F} ¿Qué conclusión proporcional permite la Fuente C? A) Que en 1924 hubo oficiales que exigían leyes sociales B) Que todo el ejército pensaba igual", "A) Que en 1924 hubo oficiales que exigían leyes sociales", "El manifiesto es de jóvenes oficiales, no de todo el ejército."),
        ("{F} ¿Qué otra fuente ayudaría a comprobar el dato de la Fuente B? A) Un registro oficial con las fechas de cambio de gabinete B) Otra carta del mismo empleado", "A) Un registro oficial con las fechas de cambio de gabinete", "Un registro de fechas permite contrastar el dato de la carta; otra carta del mismo autor solo lo repetiría."),
        ("{F} ¿Cuál es la mejor síntesis? A) Las tres fuentes muestran puntos de vista distintos sobre cómo debía gobernarse el país B) Las tres fuentes prueban que el Congreso fue el culpable de todo", "A) Las tres fuentes muestran puntos de vista distintos sobre cómo debía gobernarse el país", "Una síntesis respeta la diferencia de procedencias y no culpa a un solo actor."),
    ],
    ctx=("Para una exposición eliges un fragmento de diario de 1921 que critica al Congreso. ¿Qué debes anotar al lado para usarlo bien? A) Quién lo publicó, la fecha y su propósito B) Solo el nombre del diario", "A) Quién lo publicó, la fecha y su propósito", "Esos datos son la procedencia, base para interpretar la fuente."),
    sc=[("¿Qué es la procedencia de una fuente?", "Los datos de su origen: autor, fecha, destinatario y propósito", "Así se define en el vocabulario."),
        ("¿Qué diferencia hay entre describir e interpretar?", "Describir dice qué ocurre; interpretar da una explicación u opinión", "Esa distinción está en la explicación."),
        ("{F} ¿Qué fuente critica que las leyes no se voten?", "Fuente B", "La carta se queja de que la ley de sueldos nunca se vota.")],
    op=("Elige una de las tres fuentes de la ficha y completa una tabla con cuatro filas: autor, fecha, propósito y conclusión que sí permite. Agrega una quinta fila con lo que la fuente no permite concluir. {F}",
        "Fuente B: autor, un empleado público; fecha, 1921; propósito, criticar la inestabilidad de los gabinetes; permite concluir que a su autor le preocupaba el cambio constante de gabinetes; no permite concluir cuántos gabinetes cayeron en todo el país.",
        ["identifica autor, fecha y propósito", "la conclusión se apoya en el texto", "indica un límite de la fuente"], ["tabla de cinco filas"], ["no indicar el propósito", "concluir algo sobre todo el país con una sola fuente"],
        "Pide que explique qué otra fuente buscaría para comprobar su conclusión."),
    reinforce="Elige un mensaje que hayas recibido y di quién lo envió, para qué y qué no puedes concluir solo con él.",
    extend="Busca en tu casa un documento con fecha y autor (una boleta, una carta) y explica para qué se escribió.",
)

# ================================================================ OA 05, clase 3
F = ("Ficha 3 (cuatro perspectivas de ejemplo sobre el sistema político de 1920, escritas para este cuaderno). "
     "Perspectiva 1, un diputado: «El Congreso debe controlar al gobierno; un presidente fuerte puede abusar del poder.» "
     "Perspectiva 2, un candidato reformista: «Necesitamos un presidente elegido por el pueblo, con poder para aprobar leyes sociales.» "
     "Perspectiva 3, una dirigente obrera: «Nos prometen leyes y no llegan; queremos jornadas justas y derecho a organizarnos.» "
     "Perspectiva 4, una profesora de una escuela rural: «Aquí no hay escuela cerca; lo que se discute en Santiago no llega a mi pueblo.» "
     "Escalas: la perspectiva 4 es local; las perspectivas 1, 2 y 3 son nacionales (hablan del país y de los trabajadores en general).")
build(
    OA, 3, F,
    use="Aprenderé a comparar cómo distintos actores veían la crisis del sistema parlamentario y a distinguir la escala local, regional y nacional de un problema.",
    prior=["Sé interrogar una fuente por su procedencia.", "Sé que cada actor tiene intereses propios.", "Sé qué eran el Congreso y el presidente en 1920."],
    explain=[
        "Una perspectiva es el punto de vista desde el cual alguien observa un hecho. En la crisis del período parlamentario, un diputado, un candidato reformista, una dirigente obrera y una profesora rural veían el mismo sistema, pero sus experiencias eran distintas. Comparar perspectivas significa buscar qué coincide, qué se contradice y por qué.",
        "Los intereses explican parte de las diferencias. El diputado quería conservar el control del Congreso sobre el gobierno. El candidato reformista quería un presidente con más fuerza para aprobar leyes sociales. La dirigente obrera pedía derechos laborales concretos. Los tres criticaban el sistema, pero proponían soluciones diferentes, y por eso no se puede decir que todos pensaban igual.",
        "La escala es el tamaño del espacio desde el cual se mira: local, regional, nacional o mundial. La profesora rural habla de su pueblo, y su fuente muestra que los debates nacionales no siempre llegaban a todo el país. Una buena comparación indica la escala de cada perspectiva y evita tratar la voz de una persona como si fuera la de todos.",
    ],
    vocab=[("perspectiva", "punto de vista desde el cual alguien observa y valora un hecho"), ("escala", "tamaño del espacio al que se refiere un hecho: local, regional, nacional o mundial"), ("interés", "aquello que un actor busca lograr o proteger"), ("reformista", "persona que propone cambios dentro del sistema, sin destruirlo"), ("jornada laboral", "horas que una persona trabaja en un día")],
    worked=[
        ("Comparar dos perspectivas", "En la ficha, ¿en qué coinciden la perspectiva 2 y la 3?", ["La perspectiva 2 quiere aprobar leyes sociales.", "La perspectiva 3 reclama leyes que no llegan."], "Ambas valoran las leyes sociales"),
        ("Determinar la escala", "Una carta de ejemplo cuenta que en una caleta no hay médico. ¿Qué escala tiene?", ["Habla de un lugar pequeño.", "No describe el país entero."], "Escala local"),
    ],
    mistakes=[("Pensar que quienes critican el sistema piensan lo mismo.", "Se ignora que cada actor propone soluciones distintas.", "Compara qué critica y qué propone cada uno."),
              ("Tomar la voz de una persona como la de todo un grupo.", "Se confunde un testimonio con la totalidad.", "Indica que es una perspectiva y su escala.")],
    T=[
        ("{F} ¿Qué actor propone un presidente elegido por el pueblo?", "El candidato reformista (perspectiva 2)", "Está en su cita de la ficha."),
        ("{F} ¿Qué escala tiene la perspectiva 4?", "Local", "La ficha lo indica y habla de su pueblo."),
        ("{F} ¿Quién pide derecho a organizarse?", "La dirigente obrera (perspectiva 3)", "La cita de la ficha incluye ese reclamo."),
        ("{F} ¿Qué teme el diputado de la perspectiva 1? A) Que un presidente fuerte abuse del poder B) Que falten escuelas rurales", "A) Que un presidente fuerte abuse del poder", "Así lo dice en la ficha; las escuelas rurales las menciona la profesora."),
        ("{F} ¿En qué se diferencian las perspectivas 1 y 2? A) En quién debe tener más poder, el Congreso o el presidente B) En el año en que ocurren", "A) En quién debe tener más poder, el Congreso o el presidente", "Una defiende al Congreso y otra al presidente."),
        ("{F} ¿Qué perspectiva muestra que la discusión nacional no llegaba a todos los lugares? A) La 4 B) La 1", "A) La 4", "La profesora rural dice que lo debatido en Santiago no llega a su pueblo."),
        ("{F} Un lector concluye: «Todos los chilenos de 1920 querían un presidente fuerte». ¿Qué corrección corresponde? A) Solo una de las perspectivas lo pide; el diputado piensa lo contrario B) Está bien, porque la perspectiva 2 es nacional", "A) Solo una de las perspectivas lo pide; el diputado piensa lo contrario", "Una voz no representa a todos y el diputado propone otra cosa."),
        ("{F} Un habitante de ejemplo dice: «En mi pueblo no hay médico». ¿Qué escala tiene su testimonio? A) Local B) Mundial", "A) Local", "Habla de su pueblo, un lugar concreto."),
        ("{F} ¿Qué perspectiva coincide con la 2 en pedir leyes sociales? A) La 3 B) La 1", "A) La 3", "La dirigente obrera también reclama leyes; el diputado defiende el control del Congreso."),
        ("{F} ¿Por qué no se pueden juntar las cuatro perspectivas en una sola opinión?", "Porque cada actor tiene intereses y experiencias distintas y propone soluciones diferentes", "Las citas de la ficha muestran demandas diferentes."),
        ("{F} ¿Qué ventaja tiene incluir una perspectiva local en un estudio nacional? A) Muestra cómo el problema se vivía lejos de la capital B) Permite saber el resultado de todas las votaciones", "A) Muestra cómo el problema se vivía lejos de la capital", "La escala local aporta una experiencia que las voces nacionales no dicen."),
        ("{F} ¿Cuál es la mejor síntesis? A) Hubo críticas al sistema desde distintos lugares, pero con soluciones distintas B) Todos los actores querían volver a 1891", "A) Hubo críticas al sistema desde distintos lugares, pero con soluciones distintas", "Resume coincidencias y diferencias de las citas."),
        ("{F} Quien estudia estas perspectivas quiere conocer la voz de campesinos de varias zonas. ¿Qué conviene hacer? A) Buscar cartas o testimonios de campesinos de la época B) Suponer que piensan como el diputado", "A) Buscar cartas o testimonios de campesinos de la época", "Una perspectiva se conoce con fuentes de ese grupo."),
    ],
    ctx=("Un compañero prepara una exposición solo con la voz de un parlamentario de la capital. ¿Qué le sugieres? A) Agregar una perspectiva obrera y una local para ver otras escalas B) Agregar otra cita de un parlamentario de la capital", "A) Agregar una perspectiva obrera y una local para ver otras escalas", "Comparar perspectivas exige incluir actores y escalas distintos."),
    sc=[("¿Qué es una perspectiva?", "El punto de vista desde el cual alguien observa y valora un hecho", "Así se define en el vocabulario."),
        ("{F} ¿Qué perspectiva defiende el control del Congreso sobre el gobierno?", "La del diputado (perspectiva 1)", "Su cita lo dice en la ficha."),
        ("¿Qué es la escala de un hecho?", "El tamaño del espacio al que se refiere: local, regional, nacional o mundial", "Así se define en la clase.")],
    op=("Haz una tabla con dos columnas, perspectiva 1 y perspectiva 3 de la ficha, y tres filas: qué critican, qué proponen y qué escala tienen. Al final escribe una frase que diga en qué coinciden y en qué se diferencian. {F}",
        "Perspectiva 1: critica abusos de un presidente fuerte; propone control del Congreso; escala nacional. Perspectiva 3: critica que las leyes no llegan; propone jornadas justas y derecho a organizarse; escala nacional, porque habla de los trabajadores en general. Coinciden en criticar el sistema; difieren en las soluciones.",
        ["compara en las tres filas", "indica coincidencia y diferencia", "usa solo lo que dice la ficha"], ["tabla de tres filas", "frase final"], ["inventar propuestas que la ficha no menciona", "decir que ambos piensan lo mismo"],
        "Pide que explique qué fuente adicional agregaría para entender mejor a la clase media."),
    reinforce="Explica en voz alta por qué una misma crisis puede verse distinta desde un pueblo pequeño y desde la capital.",
    extend="Pregunta a una persona de tu casa cómo ve un problema de tu barrio y compara con lo que opinas tú.",
)

# ================================================================ OA 05, clase 4
F = ("Ficha 4 (causas, cambios y continuidades de la crisis parlamentaria). "
     "Causas de largo plazo: la cuestión social, es decir, los problemas de las condiciones de vida y de trabajo de obreros y empleados, que el Congreso trataba con lentitud; el cohecho, que es comprar votos en las elecciones; y la crisis de la industria del salitre después de la Primera Guerra Mundial. "
     "Detonante: en septiembre de 1924 oficiales presionan al Congreso («ruido de sables»), que aprueba leyes sociales. "
     "Cambios de 1925: nueva Constitución que fortalece al presidente, elegido directamente por seis años; los ministros dejan de caer por la censura del Congreso; se separan la Iglesia y el Estado; se crea un tribunal para calificar las elecciones. "
     "Continuidades: persisten la desigualdad social y las mujeres no votan en elecciones nacionales.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la crisis parlamentaria con los cambios de 1925 y a reconocer lo que siguió igual.",
    prior=["Sé situar el período 1891-1925 y sus actores.", "Sé separar causas de largo plazo y detonante.", "Sé comparar perspectivas."],
    explain=[
        "La crisis del período parlamentario tuvo varias causas que se acumularon. La cuestión social era la más profunda: trabajadores y empleados vivían con salarios bajos y poca protección, y el Congreso resolvía esos problemas con lentitud. El cohecho, o compra de votos, hacía que muchas elecciones no reflejaran la voluntad de la gente. Además, la industria del salitre perdió fuerza tras la Primera Guerra Mundial.",
        "El detonante fue el «ruido de sables» de 1924: oficiales presionaron al Congreso, que aprobó leyes sociales. La presencia militar en la política mostró que el sistema había perdido apoyo. La reconstrucción llegó con la Constitución de 1925, que fortaleció el régimen presidencial: el presidente es elegido directamente por seis años y los ministros ya no caen por votos de censura del Congreso.",
        "También hubo continuidades. Muchas desigualdades sociales siguieron y las mujeres no votaron en elecciones nacionales hasta años después. Un cambio institucional no resuelve de inmediato todos los problemas. Al relacionar causas y consecuencias hay que decir qué cambió, qué continuó y qué parte de cada cambio se puede explicar con la evidencia.",
    ],
    vocab=[("cuestión social", "conjunto de problemas de vida y trabajo de obreros y empleados en la época"), ("cohecho", "compra de votos u otros favores en una elección"), ("régimen presidencial", "sistema donde el presidente, elegido directamente, dirige el gobierno sin depender del voto de censura del Congreso"), ("detonante", "hecho que desencadena una crisis con causas previas"), ("continuidad", "aspecto que sigue igual después de un cambio")],
    worked=[
        ("Clasificar una causa", "¿El cohecho es una causa de largo plazo o un detonante?", ["Era una práctica repetida durante años.", "No fue un hecho puntual que desatara la crisis."], "Causa de largo plazo"),
        ("Distinguir cambio y continuidad", "Después de 1925 los ministros dejan de caer por la censura del Congreso, y persiste la desigualdad. ¿Qué es cada cosa?", ["Los ministros sin censura son una modificación del sistema: un cambio.", "La desigualdad sigue igual: una continuidad."], "Cambio: ministros sin censura; continuidad: desigualdad"),
    ],
    mistakes=[("Decir que el «ruido de sables» fue la única causa de la Constitución de 1925.", "Se ignoran la cuestión social, el cohecho y la crisis del salitre.", "Ubica el ruido de sables como detonante, no como causa única."),
              ("Creer que con la nueva Constitución desaparecieron todos los problemas.", "Se confunde un cambio institucional con la solución de la desigualdad.", "Revisa qué continuó después de 1925.")],
    T=[
        ("{F} ¿Qué es el cohecho según la ficha?", "Comprar votos en las elecciones", "La ficha lo define así."),
        ("{F} ¿Cuántos años dura el mandato presidencial en la Constitución de 1925?", "Seis años", "La ficha dice que se elige directamente por seis años."),
        ("{F} ¿Qué hecho de 1924 se presenta como detonante?", "El «ruido de sables»", "La ficha lo describe como presión de oficiales al Congreso."),
        ("{F} ¿Cuál de estas es una causa de largo plazo? A) La cuestión social B) El ruido de sables de 1924", "A) La cuestión social", "La cuestión social se acumuló durante años; el ruido de sables es el hecho que desencadena."),
        ("{F} ¿Qué cambio de 1925 afecta a los ministros? A) Dejan de caer por la censura del Congreso B) Son elegidos por los obreros", "A) Dejan de caer por la censura del Congreso", "Así lo dice la ficha; los obreros no los elegían."),
        ("{F} ¿Qué continuidad señala la ficha? A) Las mujeres no votan en elecciones nacionales B) El presidente es elegido directamente", "A) Las mujeres no votan en elecciones nacionales", "Lo segundo es un cambio de 1925."),
        ("{F} Una persona dice: «Mi voto fue comprado con un saco de harina». ¿A qué problema corresponde? A) Cohecho B) Detonante", "A) Cohecho", "Comprar un voto a cambio de un bien es cohecho."),
        ("{F} Un decreto de ejemplo crea un tribunal para revisar los resultados de las elecciones. ¿Qué parte de la ficha lo refleja? A) El tribunal que califica las elecciones B) La separación de la Iglesia y el Estado", "A) El tribunal que califica las elecciones", "Ese tribunal revisa elecciones, lo que responde al problema del cohecho."),
        ("{F} Imagina un país donde el Congreso censura a ministros cada mes y otro donde no puede hacerlo. ¿En cuál se parece más al sistema que crea 1925? A) El segundo B) El primero", "A) El segundo", "En 1925 los ministros dejan de caer por la censura."),
        ("{F} ¿Por qué se dice que el ruido de sables no explica por sí solo la crisis?", "Porque antes ya existían la cuestión social, el cohecho y la crisis del salitre", "La ficha lo presenta como detonante de causas previas."),
        ("{F} ¿Qué enunciado distingue bien un cambio y una continuidad? A) Cambió el modo de elegir al presidente y siguió la desigualdad B) Cambió todo y no continuó nada", "A) Cambió el modo de elegir al presidente y siguió la desigualdad", "La ficha muestra cambios y también continuidades."),
        ("{F} Un compañero escribe: «La Constitución de 1925 solucionó la cuestión social». ¿Qué corrección corresponde? A) Fortaleció al presidente, pero la desigualdad social continuó B) Es correcto porque fue una ley importante", "A) Fortaleció al presidente, pero la desigualdad social continuó", "La ficha señala la persistencia de la desigualdad."),
        ("{F} ¿Cuál es la mejor síntesis? A) Causas de largo plazo y un detonante llevaron a una reconstrucción institucional con cambios y continuidades B) Un solo hecho de 1924 cambió el país", "A) Causas de largo plazo y un detonante llevaron a una reconstrucción institucional con cambios y continuidades", "Reúne causas, detonante, cambios y continuidades."),
    ],
    ctx=("Un afiche dice: «Desde 1925 todo es distinto en Chile». ¿Qué le falta? A) Mencionar las continuidades, como la desigualdad B) Agregar una fecha más exacta", "A) Mencionar las continuidades, como la desigualdad", "La ficha enumera hechos que siguieron igual."),
    sc=[("¿Qué es la cuestión social?", "El conjunto de problemas de vida y trabajo de obreros y empleados", "Así se define en el vocabulario."),
        ("¿Qué es un detonante?", "Un hecho que desencadena una crisis con causas previas", "Así se define en la clase."),
        ("En Historia: ¿qué es el régimen presidencial?", "Un sistema donde el presidente, elegido directamente, dirige el gobierno sin depender del voto de censura del Congreso", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja un esquema con «crisis del período parlamentario» al centro. A un lado escribe tres causas de largo plazo, arriba el detonante y al otro lado dos cambios de 1925 y una continuidad. Debajo escribe una frase que empiece con «contribuyó a…». {F}",
        "Causas: cuestión social, cohecho, crisis del salitre. Detonante: ruido de sables (1924). Cambios: presidente elegido directamente por seis años; ministros sin censura. Continuidad: desigualdad social. Frase: «La cuestión social contribuyó a la pérdida de apoyo del sistema».",
        ["distingue causas, detonante y consecuencias", "incluye cambios y una continuidad", "usa «contribuyó a…» sin decir causa única"], ["esquema", "frase con «contribuyó a…»"], ["poner el detonante entre las causas de largo plazo", "decir que una sola causa explica todo"],
        "Pide que explique por qué un cambio de reglas políticas no basta para resolver la desigualdad."),
    reinforce="Explica a alguien de tu casa la diferencia entre una causa de largo plazo y un detonante usando este tema.",
    extend="Piensa en un cambio de normas en tu colegio y di una cosa que cambió y otra que siguió igual.",
)

# ================================================================ OA 05, clase 5
F = ("Ficha 5 (construir una interpretación sobre la Constitución de 1925). "
     "Pregunta de investigación: ¿ayudó la Constitución de 1925 a reconstruir la institucionalidad política de Chile? "
     "Hechos: la Constitución se aprueba en 1925 y fortalece el régimen presidencial, con un presidente elegido directamente por seis años; se separan la Iglesia y el Estado; se crea un tribunal calificador de elecciones; en 1922 se funda el Partido Comunista de Chile y en 1933 el Partido Socialista de Chile. "
     "Evidencia 1, discurso de ejemplo de un presidente, 1926: «Hoy el gobierno puede trabajar sin vivir bajo la amenaza de censura.» "
     "Evidencia 2, editorial de ejemplo de un diario, 1927: «Se necesitan elecciones sin compra de votos para que el Congreso represente de verdad.» "
     "Evidencia 3, carta de ejemplo de una obrera, 1927: «El salario sigue igual de bajo, aunque haya nueva Constitución.»")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada de la Constitución de 1925: una afirmación apoyada en evidencias y con límites claros.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé distinguir causas, cambios y continuidades.", "Sé que una afirmación necesita evidencia."],
    explain=[
        "Una interpretación documentada es una respuesta a una pregunta histórica que se apoya en evidencias y reconoce sus límites. Se puede escribir en tres partes: afirmación (lo que sostengo), evidencia (las fuentes o hechos que la apoyan) y límite (lo que no puedo concluir con esa evidencia). Si falta una de las tres, la interpretación queda incompleta.",
        "Sobre la Constitución de 1925, una afirmación posible es que ayudó a reconstruir la institucionalidad porque fortaleció al presidente, separó la Iglesia del Estado y creó un tribunal para calificar elecciones. La evidencia 1 respalda el primer punto y la evidencia 2 muestra que aún se esperaban elecciones más limpias. Además, en esos años surgieron partidos nuevos, como el Partido Comunista (1922) y el Partido Socialista (1933), lo que cambió el sistema de partidos.",
        "El límite aparece en la evidencia 3: una obrera señala que su salario seguía bajo. Eso no prueba que la Constitución fracasara, pero muestra que no resolvió por sí sola la cuestión social. Una buena interpretación usa expresiones como «ayudó a» o «permitió», y no «solucionó todo». Así separa lo que se puede afirmar de lo que habría que investigar más.",
    ],
    vocab=[("interpretación documentada", "respuesta a una pregunta histórica apoyada en evidencias"), ("afirmación", "idea que se sostiene como respuesta"), ("evidencia", "dato o fuente que apoya o contradice una afirmación"), ("límite", "aquello que la evidencia no permite concluir"), ("sistema de partidos", "conjunto de partidos políticos de un país y la forma en que compiten")],
    worked=[
        ("Evaluar una evidencia", "Afirmación: «En 1925 el presidente quedó con más poder». ¿Apoya la evidencia 1 esta afirmación?", ["El presidente dice que ya no vive bajo la amenaza de censura.", "Eso muestra más libertad para gobernar."], "Sí, la apoya"),
        ("Formular un límite", "Con la carta de la obrera, ¿qué no se puede concluir?", ["Es un testimonio de una persona en 1927.", "No dice nada sobre todos los trabajadores del país."], "Que la situación fuera igual para todos los trabajadores"),
    ],
    mistakes=[("Escribir una afirmación sin ninguna evidencia.", "Se confunde opinión con interpretación.", "Cita al menos una fuente o hecho que la apoye."),
              ("Usar «solucionó todo» o «fracasó por completo».", "Se ignoran los límites de la evidencia.", "Usa verbos como «ayudó a» o «no resolvió por sí sola».")],
    T=[
        ("{F} ¿En qué año se funda el Partido Comunista de Chile según la ficha?", "1922", "Está entre los hechos de la ficha."),
        ("{F} ¿Qué dice la evidencia 3 sobre el salario?", "Que sigue igual de bajo", "La carta lo dice."),
        ("{F} ¿Cuáles son las tres partes de una interpretación documentada?", "Afirmación, evidencia y límite", "La explicación las presenta como las tres partes."),
        ("{F} ¿Qué evidencia respalda que el presidente gobernó con menos amenaza de censura? A) La evidencia 1 B) La evidencia 3", "A) La evidencia 1", "El discurso presidencial lo dice; la carta habla de salario."),
        ("{F} ¿Qué muestra la evidencia 2? A) Que aún se esperaban elecciones sin compra de votos B) Que el cohecho ya había desaparecido", "A) Que aún se esperaban elecciones sin compra de votos", "El editorial pide elecciones limpias, por tanto el problema seguía."),
        ("{F} ¿Qué hecho de la ficha es parte de la reforma del sistema de partidos? A) Surgen el Partido Comunista y el Partido Socialista B) Se separan la Iglesia y el Estado", "A) Surgen el Partido Comunista y el Partido Socialista", "Son nuevos partidos; lo otro es una reforma institucional."),
        ("{F} ¿Qué hecho de la ficha responde mejor al problema del cohecho? A) La creación de un tribunal calificador de elecciones B) La separación de la Iglesia y el Estado", "A) La creación de un tribunal calificador de elecciones", "El tribunal revisa los resultados de las elecciones; la separación de la Iglesia y el Estado trata de otro tema."),
        ("{F} Afirmación de ejemplo: «La Constitución de 1925 no resolvió por sí sola la cuestión social». ¿Qué evidencia la apoya? A) La evidencia 3 B) La evidencia 1", "A) La evidencia 3", "La obrera señala que el salario sigue bajo."),
        ("{F} Un estudiante escribe: «La Constitución de 1925 solucionó todos los problemas». ¿Qué corrección propones? A) «Ayudó a reconstruir la institucionalidad, pero hubo problemas pendientes» B) «Fracasó totalmente»", "A) «Ayudó a reconstruir la institucionalidad, pero hubo problemas pendientes»", "Recoge los cambios y los límites que muestra la evidencia."),
        ("{F} ¿Por qué la evidencia 3 sirve como límite y no como prueba general?", "Porque es el testimonio de una persona y no representa a todos los trabajadores", "Un solo testimonio no prueba una situación nacional."),
        ("{F} ¿Qué evidencia adicional fortalecería la interpretación sobre la reconstrucción de la institucionalidad? A) Un registro oficial de elecciones posteriores a 1925 B) Otro discurso del mismo presidente de 1926", "A) Un registro oficial de elecciones posteriores a 1925", "Mostraría si las reglas nuevas se aplicaron; otro discurso solo repetiría la versión del presidente."),
        ("{F} ¿Cuál enunciado incluye un límite? A) «Fortaleció al presidente, pero no resolvió por sí sola la desigualdad» B) «Fortaleció al presidente y eso es todo»", "A) «Fortaleció al presidente, pero no resolvió por sí sola la desigualdad»", "Reconoce lo que la evidencia no permite concluir."),
        ("{F} ¿Qué respuesta a la pregunta es más honesta con la evidencia? A) Ayudó a reconstruir la institucionalidad, aunque no resolvió la cuestión social B) Fue un fracaso porque los salarios seguían bajos", "A) Ayudó a reconstruir la institucionalidad, aunque no resolvió la cuestión social", "Equilibra evidencias a favor y límites."),
    ],
    ctx=("Para un trabajo escolar, escribes: «La Constitución de 1925 fortaleció al presidente». ¿Qué debes agregar para que sea una interpretación documentada? A) Una evidencia y un límite B) Solo una opinión sobre la Constitución", "A) Una evidencia y un límite", "Una interpretación necesita afirmación, evidencia y límite."),
    sc=[("¿Qué es un límite en una interpretación?", "Lo que la evidencia no permite concluir", "Así se define en el vocabulario."),
        ("{F} ¿Qué pregunta de investigación plantea la ficha?", "Si la Constitución de 1925 ayudó a reconstruir la institucionalidad política de Chile", "Es la pregunta escrita al inicio de la ficha."),
        ("¿Qué verbo es más prudente en una interpretación, «solucionó» o «ayudó a»?", "«Ayudó a»", "Evita decir más de lo que la evidencia permite.")],
    op=("Escribe un párrafo de cuatro a seis líneas que responda la pregunta de la ficha. Debe tener una afirmación, al menos dos evidencias citadas (indica su número) y un límite. {F}",
        "«La Constitución de 1925 ayudó a reconstruir la institucionalidad: fortaleció al presidente (evidencia 1) y se esperaban elecciones más limpias (evidencia 2). Sin embargo, la evidencia 3 muestra que no resolvió por sí sola la cuestión social, así que no se puede decir que cambió la vida de todos.»",
        ["tiene afirmación, evidencia y límite", "cita dos evidencias de la ficha", "no usa verbos absolutos"], ["párrafo escrito"], ["no citar las evidencias", "decir que solucionó todo"],
        "Pide que explique qué otra fuente buscaría para estudiar el límite señalado."),
    reinforce="Explica en voz alta qué es una afirmación, una evidencia y un límite con un ejemplo de tu vida escolar.",
    extend="Elige un tema de tu colegio, escribe una afirmación y busca una evidencia que la apoye.",
)

# ================================================================ OA 06
OA = "HI2M OA 06"

# ================================================================ OA 06, clase 1
F = ("Ficha 1 (Chile y la Gran Depresión). "
     "Hasta 1929 la economía chilena crecía hacia afuera: vendía al exterior materias primas, sobre todo salitre y cobre, y compraba afuera casi todos los productos manufacturados. "
     "Después de la Primera Guerra Mundial el salitre natural chileno perdió mercado frente al salitre sintético, hecho en fábricas de otros países. "
     "En 1929 comienza la Gran Depresión, una crisis económica mundial en la que cae el comercio. Para Chile bajan las exportaciones y muchas oficinas salitreras cierran. "
     "Hitos: en 1938 es elegido presidente Pedro Aguirre Cerda; en 1939 se crea la Corporación de Fomento de la Producción (CORFO); en 1943 se crea la empresa eléctrica estatal ENDESA. "
     "Dato de ejemplo: el valor de las exportaciones de un año es 100 y dos años después baja a 35.")
build(
    OA, 1, F,
    use="Aprenderé a situar el fin de la riqueza del salitre y el golpe de la Gran Depresión en Chile, y a reconocer quiénes eran los actores del cambio de modelo económico.",
    prior=["Sé qué es una materia prima y qué es exportar.", "Sé calcular diferencias entre años y restas simples.", "Conozco la Gran Depresión de 1929 como crisis mundial."],
    explain=[
        "Hasta 1929 Chile tenía un modelo de crecimiento hacia afuera: su economía dependía de vender materias primas al exterior, principalmente salitre y cobre, y de comprar afuera las manufacturas, es decir, productos fabricados como telas, máquinas o herramientas. El Estado se financiaba en buena parte con los impuestos a esas exportaciones. Mientras los precios y la demanda se mantuvieron altos, el sistema funcionó.",
        "Después de la Primera Guerra Mundial el salitre chileno perdió mercado porque se fabricó salitre sintético en otros países. Luego, la Gran Depresión de 1929 redujo el comercio mundial y las exportaciones chilenas cayeron con fuerza. Muchas oficinas salitreras cerraron y miles de personas quedaron sin trabajo. Se llama fin de la riqueza del salitre a este derrumbe de un negocio que había sostenido al país.",
        "Frente a esa crisis, el Estado tomó un papel nuevo. Con el gobierno de Pedro Aguirre Cerda se creó la CORFO en 1939 para promover la industria, y en 1943 se creó ENDESA para producir electricidad. Los actores fueron el Estado, los trabajadores sin empleo, los empresarios que querían fabricar en Chile y las empresas extranjeras. La pregunta guía es cómo cambió el rol del Estado a partir de esta crisis.",
    ],
    vocab=[("crecimiento hacia afuera", "modelo en que un país crece vendiendo materias primas al exterior"), ("materia prima", "producto natural que se usa para fabricar otras cosas, como el cobre"), ("manufactura", "producto fabricado, como una tela o una máquina"), ("salitre sintético", "salitre fabricado en fábricas de otros países, que reemplazó al natural"), ("CORFO", "Corporación de Fomento de la Producción, creada en 1939 para promover la industria")],
    worked=[
        ("Calcular un tiempo", "La CORFO se creó en 1939 y la Gran Depresión comenzó en 1929. ¿Cuántos años pasaron?", ["Tomo los dos años.", "1939 − 1929 = 10."], "10 años"),
        ("Clasificar un producto", "El cobre sin refinar se vende al exterior. ¿Es materia prima o manufactura?", ["No es un producto terminado para el consumo.", "Es un material natural para fabricar otras cosas."], "Materia prima"),
    ],
    mistakes=[("Decir que la Gran Depresión fue el único motivo del fin del salitre.", "Se olvida que el salitre sintético ya le quitaba mercado después de la Primera Guerra.", "Separa lo que ocurrió antes y después de 1929."),
              ("Creer que el Estado no intervenía antes de 1929 en nada.", "Se simplifica el cambio de rol.", "Di que desde 1939 el Estado asumió un papel más activo en la industria.")],
    T=[
        ("{F} ¿Qué productos vendía Chile al exterior según la ficha?", "Materias primas, sobre todo salitre y cobre", "La ficha describe así el crecimiento hacia afuera."),
        ("{F} ¿Qué año se crea la CORFO?", "1939", "Está entre los hitos de la ficha."),
        ("{F} ¿Qué empresa estatal se crea en 1943?", "ENDESA", "Aparece entre los hitos."),
        ("{F} ¿Qué hito de la ficha ocurre antes de la elección de Aguirre Cerda? A) El comienzo de la Gran Depresión en 1929 B) La creación de ENDESA en 1943", "A) El comienzo de la Gran Depresión en 1929", "Aguirre Cerda fue elegido en 1938; ENDESA se crea en 1943."),
        ("{F} ¿Por qué perdió mercado el salitre natural después de la Primera Guerra? A) Porque se fabricó salitre sintético en otros países B) Porque dejó de existir en el norte", "A) Porque se fabricó salitre sintético en otros países", "Así lo dice la ficha."),
        ("{F} El cobre vendido en bruto al extranjero, ¿qué es? A) Materia prima B) Manufactura", "A) Materia prima", "Es un material natural que otros usan para fabricar."),
        ("=", "{F} Con el dato de ejemplo, ¿cuántos puntos bajó el valor de las exportaciones?", "100-35", "Se resta el valor final al inicial.", " puntos"),
        ("{F} Un país de ejemplo vende solo trigo y compra todas sus máquinas afuera. ¿Qué modelo sigue? A) Crecimiento hacia afuera B) Crecimiento con industria propia", "A) Crecimiento hacia afuera", "Vende materias primas y compra manufacturas, como el modelo de la ficha."),
        ("{F} Una oficina salitrera cierra en 1931 y sus trabajadores se van a una ciudad a buscar empleo. ¿Qué proceso muestra? A) Efecto de la crisis en la vida de las personas B) Un efecto de la CORFO", "A) Efecto de la crisis en la vida de las personas", "La CORFO se crea después, en 1939."),
        ("{F} ¿Por qué la caída de las exportaciones afectaba también al Estado?", "Porque parte de sus ingresos venía de los impuestos a esas exportaciones", "La explicación vincula las finanzas del Estado con las exportaciones."),
        ("{F} Alguien afirma: «La CORFO se creó en 1929». ¿Qué corriges? A) Se creó en 1939; en 1929 comenzó la Gran Depresión B) Está bien, porque ambos son del siglo XX", "A) Se creó en 1939; en 1929 comenzó la Gran Depresión", "Los hitos de la ficha tienen fechas distintas."),
        ("{F} Un compañero dice: «El salitre dejó de venderse del todo en 1929». ¿Se sostiene con la ficha? A) No, la ficha dice que perdió mercado y que las exportaciones cayeron B) Sí, porque la ficha dice 1929", "A) No, la ficha dice que perdió mercado y que las exportaciones cayeron", "Perder mercado no es dejar de vender por completo."),
        ("¿Cuál es la mejor pregunta para este tema? A) ¿Cómo cambió el rol del Estado en Chile después del fin de la riqueza del salitre y de la Gran Depresión? B) ¿Cuál era el producto más bonito de la época?", "A) ¿Cómo cambió el rol del Estado en Chile después del fin de la riqueza del salitre y de la Gran Depresión?", "La primera se responde con hechos y tiempo; la segunda es una opinión."),
    ],
    ctx=("Un afiche escolar dice: «Chile fue siempre un país industrial». ¿Qué dato de la ficha lo contradice? A) Hasta 1929 vendía materias primas y compraba manufacturas B) La CORFO se creó en 1939", "A) Hasta 1929 vendía materias primas y compraba manufacturas", "Eso describe un modelo de crecimiento hacia afuera, no industrial."),
    sc=[("¿Qué es el crecimiento hacia afuera?", "Un modelo en que un país crece vendiendo materias primas al exterior", "Así se define en el vocabulario."),
        ("¿Qué es una manufactura?", "Un producto fabricado, como una tela o una máquina", "Así se define en la clase."),
        ("En Historia: ¿qué es una manufactura?", "Un producto fabricado, como una tela o una máquina", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo de 1925 a 1945 con la escala 1 cm = 5 años. Marca la Gran Depresión (1929), la elección de Aguirre Cerda (1938), la CORFO (1939) y ENDESA (1943). Debajo escribe dos frases: una sobre el modelo hacia afuera y otra sobre el nuevo papel del Estado. {F}",
        "Posiciones desde 1925: 0,8 cm; 2,6 cm; 2,8 cm; 3,6 cm. Frases: «Hasta 1929 Chile vendía salitre y cobre al exterior»; «Desde 1939 el Estado promueve la industria con la CORFO».",
        ["respeta la escala", "ubica los cuatro hitos", "las frases describen los dos modelos"], ["línea de tiempo", "dos frases"], ["poner los hitos sin medir", "mezclar el modelo antiguo con el nuevo"],
        "Pide que explique por qué la caída del salitre y la Depresión de 1929 no son lo mismo."),
    reinforce="Explica en voz alta qué significaba que Chile creciera hacia afuera y qué problema trajo la Gran Depresión.",
    extend="Mira la etiqueta de un objeto de tu casa y anota dónde fue fabricado; piensa si podría haberse fabricado en Chile.",
)

# ================================================================ OA 06, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
     "Fuente A, informe de un ingeniero al gobierno, 1936: «Importamos telas, zapatos y herramientas que podríamos fabricar aquí; si el Estado presta dinero a las fábricas, habrá empleo.» "
     "Fuente B, aviso del Estado, 1941: «La CORFO ofrece créditos a quienes instalen nuevas industrias en el país.» "
     "Fuente C, carta de una familia salitrera a un diario, 1932: «Cerró la oficina y nos vinimos a la ciudad. Mi esposo busca trabajo y no hay.» "
     "Hecho real: la CORFO se creó en 1939.")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes sobre la crisis y la industrialización: quién las escribe, para qué y qué se puede concluir de cada una.",
    prior=["Sé interrogar una fuente por su procedencia.", "Sé qué fue la CORFO y cuándo se creó.", "Sé separar descripción de interpretación."],
    explain=[
        "Para estudiar cómo cambió la economía chilena después de la Gran Depresión se usan fuentes de distintos autores. Cada una tiene una procedencia: quién escribe, cuándo y con qué propósito. Un informe de un ingeniero propone una idea al gobierno. Un aviso estatal busca que las personas pidan un crédito. Una carta de una familia cuenta una experiencia personal de la crisis.",
        "Es importante no tratar a todas las fuentes igual. El aviso de la CORFO tiene un propósito de difusión: invita a participar, y por eso no dice si los créditos tuvieron éxito. La carta de la familia describe un hecho vivido, pero muestra solo un caso. El informe del ingeniero interpreta: afirma que se podrían fabricar productos aquí, pero no prueba que ya se fabricaran.",
        "Una conclusión sólida combina fuentes. La carta muestra el efecto de la crisis en una familia, el informe muestra una propuesta y el aviso muestra una política que ya existía en 1941. Aun así, ninguna prueba cuántas industrias se crearon. Esa respuesta necesitaría datos, como registros oficiales de fábricas. Por eso se dice que la conclusión debe ser proporcional a la evidencia.",
    ],
    vocab=[("procedencia", "datos de origen de una fuente: autor, fecha y propósito"), ("crédito", "dinero que se presta para devolverlo más adelante"), ("política pública", "conjunto de acciones del Estado para resolver un problema"), ("difusión", "acción de dar a conocer algo a mucha gente"), ("testimonio", "relato de una persona sobre lo que vivió")],
    worked=[
        ("Reconocer el propósito", "Aviso de ejemplo de 1942: «Pida su crédito en la CORFO y construya su taller». ¿Cuál es su propósito?", ["Invita a pedir un crédito.", "Quiere que más personas usen el programa."], "Difundir un programa y atraer solicitantes"),
        ("Medir el alcance de una fuente", "Carta de ejemplo de un comerciante de una ciudad del sur: «Aquí abrieron dos talleres nuevos». ¿Permite decir cuántos talleres se abrieron en Chile?", ["Habla de una ciudad.", "No entrega datos de todo el país."], "No, solo muestra lo ocurrido en esa ciudad"),
    ],
    mistakes=[("Creer que un aviso del Estado prueba que el programa funcionó.", "Se confunde propaganda con resultados.", "Pregunta cuántos créditos se pidieron y qué ocurrió después."),
              ("Usar una carta como prueba de lo que vivió todo el país.", "Se generaliza desde un caso.", "Presenta la carta como un testimonio y busca otras fuentes.")],
    T=[
        ("{F} ¿Quién escribe la Fuente A?", "Un ingeniero, en un informe al gobierno", "La ficha indica su procedencia."),
        ("{F} ¿En qué año se publica la Fuente B?", "1941", "La ficha lo indica."),
        ("{F} ¿Qué cuenta la familia de la Fuente C?", "Que cerró la oficina, se fueron a la ciudad y no encuentran trabajo", "La carta lo relata."),
        ("{F} ¿Cuál es el propósito de la Fuente B? A) Invitar a instalar nuevas industrias con créditos B) Contar la experiencia de una familia", "A) Invitar a instalar nuevas industrias con créditos", "Es un aviso estatal que ofrece créditos."),
        ("{F} ¿Qué fuente es un testimonio personal? A) La Fuente C B) La Fuente A", "A) La Fuente C", "Una familia cuenta su experiencia personal; la Fuente A es un informe de un ingeniero."),
        ("{F} En la Fuente A, ¿qué parte es una propuesta del autor? A) Que el Estado preste dinero a las fábricas B) Que se importan telas y zapatos", "A) Que el Estado preste dinero a las fábricas", "Es lo que el ingeniero propone; lo otro es una descripción."),
        ("{F} ¿Qué fuente es posterior a la creación de la CORFO? A) La Fuente B, de 1941 B) La Fuente A, de 1936", "A) La Fuente B, de 1941", "La CORFO se creó en 1939; el aviso es de 1941 y el informe de 1936."),
        ("{F} Un compañero dice: «El aviso de la Fuente B prueba que se crearon muchas industrias». ¿Qué respondes? A) Solo prueba que existían créditos, no cuántas industrias se crearon B) Tiene razón porque el aviso es del Estado", "A) Solo prueba que existían créditos, no cuántas industrias se crearon", "Un aviso no informa resultados."),
        ("{F} ¿Qué fuente servirá mejor para conocer cuántas fábricas existían en 1945? A) Un registro oficial de fábricas de ese año B) Una carta personal de 1932", "A) Un registro oficial de fábricas de ese año", "Cuenta datos del año pedido; la carta es anterior y personal."),
        ("{F} ¿Por qué la Fuente C no sirve para decir cuánta gente quedó sin trabajo en todo Chile?", "Porque cuenta solo el caso de una familia", "Un testimonio no mide a todo el país."),
        ("{F} ¿Qué conclusión proporcional permite la Fuente A? A) Que un ingeniero propuso en 1936 apoyar a las fábricas con préstamos del Estado B) Que en 1936 todas las fábricas ya recibían préstamos", "A) Que un ingeniero propuso en 1936 apoyar a las fábricas con préstamos del Estado", "El informe propone; no demuestra que ya se aplicara."),
        ("{F} ¿Qué combinación permite entender mejor el proceso? A) La carta de la crisis, el informe con una propuesta y el aviso de una política ya vigente B) Tres cartas personales sin fecha", "A) La carta de la crisis, el informe con una propuesta y el aviso de una política ya vigente", "Reúne distintas procedencias y momentos."),
        ("{F} ¿Cuál es la mejor síntesis? A) Las fuentes muestran el efecto de la crisis, una propuesta y una política estatal, pero no miden sus resultados B) Las fuentes demuestran que la industrialización fue un éxito", "A) Las fuentes muestran el efecto de la crisis, una propuesta y una política estatal, pero no miden sus resultados", "La conclusión respeta los límites de las fuentes."),
    ],
    ctx=("Para una exposición encuentras un afiche de 1941 que dice «Chile produce más cada día». ¿Qué debes hacer antes de usarlo como prueba? A) Preguntar quién lo hizo, para qué y buscar datos que lo confirmen B) Copiarlo tal cual", "A) Preguntar quién lo hizo, para qué y buscar datos que lo confirmen", "Un afiche puede tener propósito de propaganda."),
    sc=[("¿Qué es un crédito?", "Dinero que se presta para devolverlo más adelante", "Así se define en el vocabulario."),
        ("¿Qué es un testimonio?", "El relato de una persona sobre lo que vivió", "Así se define en la clase."),
        ("En Historia: ¿qué es una política pública?", "Un conjunto de acciones del Estado para resolver un problema", "Así se define en el vocabulario de la clase.")],
    op=("Elige las fuentes A y C de la ficha y completa una tabla con las filas: autor, fecha, propósito, qué se puede concluir y qué no se puede concluir. Cierra con una frase que combine las dos fuentes. {F}",
        "Fuente A: ingeniero; 1936; proponer apoyo del Estado a las fábricas; se puede concluir que existía esa propuesta; no se puede concluir que ya se aplicara. Fuente C: una familia salitrera; 1932; contar su caso; se puede concluir que el cierre de una oficina dejó a una familia sin empleo; no se puede concluir lo que vivió todo el país.",
        ["completa las cinco filas", "las conclusiones se apoyan en el texto", "la frase combina ambas fuentes"], ["tabla", "frase final"], ["no indicar el propósito", "generalizar desde la carta"],
        "Pide que explique qué dato adicional buscaría para medir los resultados de la política."),
    reinforce="Explica en voz alta por qué un aviso del Estado no basta para saber si un programa funcionó.",
    extend="Busca un aviso o folleto en tu casa y anota qué quiere lograr con quien lo lee.",
)

# ================================================================ OA 06, clase 3
F = ("Ficha 3 (perspectivas y escalas de ejemplo, escritas para este cuaderno). "
     "Perspectiva 1, un industrial: «Si el Estado ayuda a las fábricas nacionales, podremos producir lo que hoy se compra afuera.» "
     "Perspectiva 2, un importador: «Si se protege a las fábricas, los productos serán más caros y habrá menos variedad.» "
     "Perspectiva 3, una dirigente de obreros: «Queremos empleo estable y salarios que alcancen; si las fábricas del país dan trabajo, serán bienvenidas.» "
     "Perspectiva 4, un campesino: «En el campo seguimos trabajando para el patrón y nada de esto llega a nosotros.» "
     "Escalas: la Gran Depresión es un hecho mundial; la CORFO es una política nacional; el cierre de una oficina salitrera es un hecho local.")
build(
    OA, 3, F,
    use="Aprenderé a comparar cómo distintos actores veían el nuevo papel del Estado en la economía y a distinguir las escalas mundial, nacional y local.",
    prior=["Sé qué fue la CORFO y por qué se creó.", "Sé interrogar fuentes por su procedencia.", "Sé que una perspectiva es un punto de vista."],
    explain=[
        "Cuando el Estado empezó a promover la industria, no todos estuvieron de acuerdo ni se beneficiaron igual. Un industrial quería ayuda para fabricar en Chile. Un importador temía que los productos subieran de precio y hubiera menos variedad. Una dirigente de obreros pedía empleo estable y salarios suficientes. Un campesino sentía que los cambios no llegaban al campo.",
        "Comparar perspectivas significa buscar coincidencias y diferencias. El industrial y la dirigente obrera quieren más fábricas, pero por razones distintas: él por negocios y ella por empleo. El importador discrepa de ambos. El campesino muestra que la industrialización se concentró en las ciudades y que no todos los grupos la sintieron igual. Cada perspectiva corresponde a un interés.",
        "También hay que ordenar los hechos por escala. La Gran Depresión es mundial porque afectó el comercio de muchos países. La creación de la CORFO es nacional porque es una decisión del Estado chileno. El cierre de una oficina salitrera es local porque ocurrió en un lugar concreto. Una buena explicación conecta las tres escalas y evita atribuir a una sola persona lo que depende de varios niveles.",
    ],
    vocab=[("perspectiva", "punto de vista desde el cual alguien valora un hecho"), ("importador", "persona o empresa que compra productos en el extranjero para venderlos en el país"), ("industrial", "dueño de una fábrica o empresario de la industria"), ("escala", "tamaño del espacio al que se refiere un hecho: local, nacional o mundial"), ("salario", "pago que recibe una persona por su trabajo")],
    worked=[
        ("Comparar intereses", "En la ficha, ¿qué diferencia hay entre lo que pide el industrial y lo que pide el importador?", ["El industrial quiere ayuda estatal para producir en Chile.", "El importador teme productos más caros."], "El industrial pide protección; el importador teme precios más altos"),
        ("Asignar una escala", "Una noticia de ejemplo dice que el precio del cobre cayó en los mercados de muchos países. ¿Qué escala tiene?", ["Se refiere a varios países.", "No describe solo a Chile."], "Escala mundial"),
    ],
    mistakes=[("Pensar que todos los grupos sociales apoyaban la industrialización por las mismas razones.", "Se ignoran los distintos intereses.", "Pregunta qué buscaba cada actor."),
              ("Atribuir un hecho mundial a una decisión nacional.", "Se confunden escalas.", "Ubica cada hecho en su escala antes de explicarlo.")],
    T=[
        ("{F} ¿Qué actor teme que los productos sean más caros?", "El importador (perspectiva 2)", "Su cita lo dice."),
        ("{F} ¿Qué pide la dirigente de obreros?", "Empleo estable y salarios que alcancen", "Su cita lo señala."),
        ("{F} ¿Qué escala tiene la creación de la CORFO?", "Nacional", "La ficha la presenta como política nacional."),
        ("{F} ¿En qué coinciden el industrial y la dirigente obrera? A) En querer que haya más fábricas y trabajo en el país B) En querer importar todo", "A) En querer que haya más fábricas y trabajo en el país", "Ambos esperan beneficios de la industria; el importador es quien discrepa."),
        ("{F} ¿Qué perspectiva muestra que los cambios no llegaban al campo? A) La del campesino B) La del industrial", "A) La del campesino", "Su cita lo dice de forma directa."),
        ("{F} El cierre de una oficina salitrera, ¿de qué escala es? A) Local B) Mundial", "A) Local", "Ocurre en un lugar concreto."),
        ("{F} Un dueño de zapatería importa zapatos y los vende en su tienda. ¿Con qué perspectiva coincide más? A) Con el importador B) Con la dirigente obrera", "A) Con el importador", "Su negocio depende de traer productos de afuera."),
        ("{F} Una fábrica de textiles contrata a 300 trabajadores. ¿Qué actor se ve favorecido, según la ficha? A) Los obreros que buscan empleo B) El campesino que sigue en el campo", "A) Los obreros que buscan empleo", "El empleo fabril responde a lo que pide la dirigente."),
        ("{F} Sobre la caída del comercio mundial en 1929, un compañero dice que fue culpa del presidente de Chile. ¿Qué escala olvidó? A) La mundial B) La local", "A) La mundial", "La Depresión afectó el comercio de muchos países."),
        ("{F} ¿Por qué la perspectiva del campesino ayuda a evaluar la industrialización?", "Porque muestra que no todos los grupos sintieron sus beneficios", "Su cita revela un grupo que se sintió fuera del cambio."),
        ("{F} ¿Qué conclusión es prudente? A) Hubo apoyos y críticas según los intereses de cada actor B) Todos apoyaron la política del Estado", "A) Hubo apoyos y críticas según los intereses de cada actor", "Las citas muestran acuerdos y desacuerdos."),
        ("{F} Un trabajo dice: «Los obreros, los industriales y los importadores querían lo mismo». ¿Qué evidencia de la ficha lo contradice? A) La cita del importador, que teme productos más caros B) La fecha de la CORFO", "A) La cita del importador, que teme productos más caros", "Muestra un interés opuesto al del industrial."),
        ("{F} ¿Cuál es la mejor síntesis? A) La industrialización tuvo apoyos, críticas y beneficios desiguales, y se explica en escalas mundial, nacional y local B) Fue una decisión de un solo actor", "A) La industrialización tuvo apoyos, críticas y beneficios desiguales, y se explica en escalas mundial, nacional y local", "Resume las perspectivas y las escalas."),
    ],
    ctx=("Para opinar sobre un proyecto de fábrica en tu ciudad conviene escuchar a obreros, comerciantes y vecinos. ¿Por qué? A) Porque cada grupo tiene intereses y perspectivas distintas B) Porque todos piensan igual", "A) Porque cada grupo tiene intereses y perspectivas distintas", "Comparar perspectivas exige oír actores diversos."),
    sc=[("¿Qué es un importador?", "Una persona o empresa que compra productos en el extranjero para venderlos en el país", "Así se define en el vocabulario."),
        ("¿Qué es una escala?", "El tamaño del espacio al que se refiere un hecho: local, nacional o mundial", "Así se define en la clase."),
        ("{F} ¿Qué actor dice que nada llega al campo?", "El campesino (perspectiva 4)", "Su cita lo afirma.")],
    op=("Haz una tabla con las perspectivas 1, 2 y 3 de la ficha. Para cada una escribe qué quiere, qué teme y cuál es su interés. Debajo escribe una frase que explique por qué el campesino de la perspectiva 4 ve el cambio de otra forma. {F}",
        "Industrial: quiere ayuda estatal; teme seguir comprando afuera; interés, producir en Chile. Importador: quiere comerciar sin trabas; teme productos caros; interés, importar. Dirigente: quiere empleo estable; teme salarios insuficientes; interés, trabajo. Frase: el campesino trabaja en el campo, donde la industria no llega.",
        ["completa las tres perspectivas", "usa solo lo que dice la ficha", "explica la perspectiva del campesino"], ["tabla", "frase final"], ["inventar datos que no están en la ficha", "tratar a todos los actores como iguales"],
        "Pide que explique qué otra perspectiva agregaría para ver mejor el período."),
    reinforce="Explica en voz alta por qué dos personas pueden valorar distinto una misma política económica.",
    extend="Pregunta a alguien de tu casa si prefiere productos fabricados en Chile o importados y por qué.",
)

# ================================================================ OA 06, clase 4
F = ("Ficha 4 (causas, cambios y continuidades de la industrialización estatal). "
     "Causas: con la Gran Depresión bajaron las exportaciones y entraron menos divisas, es decir, monedas extranjeras como el dólar que sirven para pagar importaciones; por eso comprar productos de afuera se hizo difícil. "
     "Idea: la industrialización por sustitución de importaciones (ISI) consiste en fabricar en el país lo que antes se importaba. "
     "Detonante: el terremoto de Chillán, en enero de 1939, destruyó ciudades del sur y dio impulso a una reconstrucción y a la creación de la CORFO ese año. "
     "Cambios: el Estado se convierte en promotor de la industria con la CORFO (1939) y ENDESA (1943), crecen las ciudades y los empleos en fábricas. "
     "Continuidades: el cobre sigue siendo un producto de exportación muy importante y en el campo sigue habiendo desigualdad. "
     "Dato de ejemplo: un país importaba 500 máquinas al año y ahora fabrica 200 de ellas.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la industrialización estatal con sus cambios y continuidades, y a explicar qué es la sustitución de importaciones.",
    prior=["Sé que Chile dependía de exportar materias primas hasta 1929.", "Sé distinguir causas de largo plazo y detonante.", "Sé calcular restas y porcentajes sencillos."],
    explain=[
        "La caída de las exportaciones tuvo una consecuencia directa: entraron menos divisas. Las divisas son monedas extranjeras, como el dólar, que un país necesita para comprar productos en el exterior. Con pocas divisas, importar máquinas, telas o herramientas se volvió muy difícil. Esa dificultad llevó a pensar en fabricar dentro del país lo que antes se compraba afuera.",
        "A esa idea se le llama industrialización por sustitución de importaciones, o ISI: se sustituye un producto importado por uno hecho en Chile. Para lograrlo el Estado creó la CORFO en 1939, tras el terremoto de Chillán, y más tarde ENDESA, en 1943. Así pasó a ser un promotor de la industria, no solo un cobrador de impuestos. Las ciudades crecieron porque había empleos en las fábricas.",
        "Aun con esos cambios hubo continuidades. El cobre siguió siendo un producto de exportación muy importante, de modo que la economía no dejó de depender de lo que ocurría afuera. Y en el campo se mantuvo la desigualdad. Al explicar, conviene decir que la crisis fue una causa, no la única, y que un nuevo modelo no cambia todo de golpe.",
    ],
    vocab=[("divisas", "monedas extranjeras, como el dólar, que sirven para pagar importaciones"), ("ISI", "industrialización por sustitución de importaciones: fabricar en el país lo que antes se importaba"), ("promotor", "quien impulsa y apoya una actividad"), ("detonante", "hecho que desencadena un cambio con causas previas"), ("continuidad", "aspecto que sigue igual después de un cambio")],
    worked=[
        ("Aplicar la ISI", "Un país importaba zapatos y ahora los fabrica. ¿Es un caso de sustitución de importaciones?", ["Antes compraba el producto afuera.", "Ahora lo produce dentro del país."], "Sí, es sustitución de importaciones"),
        ("Calcular un efecto", "Un país de ejemplo importaba 90 televisores al año y reemplaza 30 con producción propia. ¿Cuántos siguen importándose?", ["Parto de lo que importaba.", "90 − 30 = 60."], "60 televisores"),
    ],
    mistakes=[("Decir que la ISI significa dejar de comerciar con otros países.", "Se confunde sustituir algunas importaciones con aislarse.", "Aclara que se reemplazan ciertos productos, no todo el comercio."),
              ("Creer que después de la CORFO el país dejó de depender del cobre.", "Se ignoran las continuidades.", "Revisa qué siguió igual.")],
    T=[
        ("{F} ¿Qué son las divisas?", "Monedas extranjeras, como el dólar, que sirven para pagar importaciones", "La ficha las define así."),
        ("{F} ¿Qué significa ISI?", "Industrialización por sustitución de importaciones", "La ficha lo explica."),
        ("{F} ¿Qué hecho de 1939 dio impulso a la reconstrucción y a la CORFO?", "El terremoto de Chillán", "La ficha lo presenta como detonante."),
        ("{F} ¿Cuál de estos casos es sustitución de importaciones? A) Una fábrica de zapatos que antes llegaban desde afuera B) La venta de cobre al exterior", "A) Una fábrica de zapatos que antes llegaban desde afuera", "Fabricar en el país lo que se importaba es ISI; vender cobre al exterior es exportar."),
        ("{F} ¿Por qué se hizo difícil importar tras la Depresión? A) Porque entraron menos divisas B) Porque el Estado prohibió toda compra", "A) Porque entraron menos divisas", "Con exportaciones bajas faltaban monedas extranjeras."),
        ("{F} ¿Cuál es un cambio en el rol del Estado? A) Se convierte en promotor de la industria B) El cobre sigue exportándose", "A) Se convierte en promotor de la industria", "Lo segundo es una continuidad."),
        ("=", "{F} En el país de ejemplo, ¿qué porcentaje de las máquinas importadas antes pasó a fabricarse allí?", "200/500*100", "Se divide lo fabricado por lo importado antes y se multiplica por 100.", " %"),
        ("{F} Un taller empieza a fabricar camisas que antes llegaban de otro continente. ¿Qué proceso muestra? A) Sustitución de importaciones B) Crecimiento hacia afuera", "A) Sustitución de importaciones", "Fabrica lo que se compraba afuera."),
        ("{F} Una persona de ejemplo se muda del campo a una ciudad para trabajar en una fábrica. ¿Qué cambio de la ficha ilustra? A) El crecimiento de ciudades y empleos fabriles B) La desigualdad rural", "A) El crecimiento de ciudades y empleos fabriles", "Se menciona entre los cambios de la ficha."),
        ("{F} ¿Por qué el cobre es una continuidad aun con la industrialización?", "Porque siguió siendo un producto de exportación muy importante, y la economía seguía dependiendo de afuera", "La ficha lo presenta como lo que siguió igual."),
        ("{F} ¿Por qué la crisis explica el origen de la ISI pero no es su única causa? A) Porque también influyeron ideas sobre el papel del Estado y la reconstrucción tras el terremoto B) Porque la crisis ocurrió después de la CORFO", "A) Porque también influyeron ideas sobre el papel del Estado y la reconstrucción tras el terremoto", "La explicación combina varias causas."),
        ("{F} Un estudiante escribe: «Después de 1939 el campo se volvió igual de próspero que las ciudades». ¿Qué corriges? A) La ficha señala que en el campo seguía la desigualdad B) Nada, está bien", "A) La ficha señala que en el campo seguía la desigualdad", "Es una continuidad señalada en la ficha."),
        ("{F} ¿Cuál es la mejor síntesis? A) La crisis llevó a sustituir importaciones con ayuda del Estado, con cambios en las ciudades y continuidades en el cobre y el campo B) Todo cambió en 1939", "A) La crisis llevó a sustituir importaciones con ayuda del Estado, con cambios en las ciudades y continuidades en el cobre y el campo", "Reúne causas, cambios y continuidades."),
    ],
    ctx=("Un afiche dice: «La ISI hizo que Chile no comprara nada del extranjero». ¿Qué problema tiene? A) Confunde sustituir algunas importaciones con dejar de importar todo B) Menciona el cobre", "A) Confunde sustituir algunas importaciones con dejar de importar todo", "La ISI reemplaza ciertos productos, no el comercio completo."),
    sc=[("¿Qué es la ISI?", "Fabricar en el país lo que antes se importaba", "Así se define en el vocabulario."),
        ("¿Qué son las divisas?", "Monedas extranjeras que sirven para pagar importaciones", "Así se define en la clase."),
        ("En Historia: ¿qué es una divisa?", "Una moneda extranjera, como el dólar, que sirve para pagar importaciones", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja un esquema con «industrialización por sustitución de importaciones» al centro. Escribe tres causas a la izquierda, el detonante arriba, y a la derecha dos cambios y dos continuidades. Debajo escribe una frase con «contribuyó a…». {F}",
        "Causas: caída de exportaciones, falta de divisas, ideas de un Estado promotor. Detonante: terremoto de Chillán y creación de CORFO en 1939. Cambios: CORFO y ENDESA; crecimiento de ciudades. Continuidades: cobre exportador; desigualdad en el campo. Frase: la falta de divisas contribuyó a que se buscara producir en Chile.",
        ["distingue causas, detonante, cambios y continuidades", "usa «contribuyó a…»", "usa solo datos de la ficha"], ["esquema", "frase"], ["tomar el detonante como causa de largo plazo", "decir que cambió todo"],
        "Pide que explique por qué un modelo nuevo puede mantener rasgos del anterior."),
    reinforce="Explica a alguien de tu casa qué es la sustitución de importaciones con un ejemplo de producto.",
    extend="Mira un objeto de tu casa y piensa si podría fabricarse en tu región o hay que traerlo de lejos.",
)

# ================================================================ OA 06, clase 5
F = ("Ficha 5 (construir una interpretación sobre Estados Unidos y la economía chilena). "
     "Pregunta de investigación: ¿qué peso tuvo Estados Unidos en la economía chilena y qué efectos tuvo? "
     "Hechos: empresas de Estados Unidos controlaban la gran minería del cobre en Chile, con yacimientos como Chuquicamata y El Teniente; el cobre era un producto de exportación muy importante; el Estado chileno cobraba impuestos a esas empresas. "
     "Evidencia 1, informe de ejemplo de un economista, 1940: «Las grandes minas del cobre pertenecen a empresas extranjeras; las utilidades salen del país.» "
     "Evidencia 2, discurso de ejemplo de un ministro, 1941: «Los impuestos al cobre financian escuelas, caminos y fábricas del Estado.» "
     "Evidencia 3, carta de ejemplo de un industrial, 1942: «Para instalar mi fábrica necesito máquinas que solo se consiguen en el extranjero.»")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre el peso de Estados Unidos en la economía chilena: una afirmación, evidencias y límites.",
    prior=["Sé que el cobre era una exportación importante.", "Sé estructurar afirmación, evidencia y límite.", "Sé que una fuente tiene procedencia y propósito."],
    explain=[
        "En el siglo XX, empresas de Estados Unidos tuvieron una gran presencia en la economía chilena, sobre todo en la gran minería del cobre. Eso significa que parte importante de los yacimientos, como Chuquicamata y El Teniente, estaba en manos de empresas extranjeras. El cobre era un producto de exportación muy importante, y el Estado chileno cobraba impuestos a esas empresas.",
        "Para interpretar este hecho se necesita una afirmación apoyada en evidencias. Por ejemplo: «La economía chilena dependía de empresas estadounidenses, aunque el Estado obtenía recursos de ellas». La evidencia 1 muestra que las utilidades salían del país. La evidencia 2 muestra que los impuestos financiaban gasto estatal. La evidencia 3 muestra otra dependencia: la tecnología importada que necesitaban las fábricas.",
        "El límite está en que estas fuentes de ejemplo no miden cuánto dinero salía ni cuánto se recaudaba. Por eso no se puede decir «Estados Unidos controlaba toda la economía» ni «las empresas solo beneficiaban a Chile». Una conclusión prudente dice que su participación fue grande y tuvo efectos mixtos, y que se necesitan cifras para precisarlos. Dependencia significa necesitar de otro país para producir o financiarse.",
    ],
    vocab=[("dependencia", "situación en que un país necesita de otro para producir o financiarse"), ("utilidades", "ganancias que obtiene una empresa"), ("gran minería", "explotación de yacimientos de gran tamaño con mucha inversión"), ("inversión extranjera", "dinero de empresas de otro país que se pone en negocios locales"), ("recaudar", "reunir dinero, por ejemplo mediante impuestos")],
    worked=[
        ("Evaluar una evidencia", "Afirmación: «Las utilidades del cobre salían del país». ¿Apoya la evidencia 1?", ["La evidencia 1 dice que las utilidades salen del país.", "Coincide con la afirmación."], "Sí, la apoya"),
        ("Formular un límite", "Con la evidencia 2, ¿qué no se puede concluir?", ["Dice que los impuestos financian escuelas, caminos y fábricas.", "No dice cuánto dinero se recaudaba."], "Cuánto dinero se recaudaba"),
    ],
    mistakes=[("Afirmar que las empresas extranjeras controlaban toda la economía.", "La ficha solo menciona la gran minería del cobre.", "Limita la afirmación a lo que la evidencia muestra."),
              ("Dejar de lado la evidencia que contradice mi idea.", "Se escoge solo lo que conviene.", "Incluye las evidencias a favor y en contra.")],
    T=[
        ("{F} ¿Qué yacimientos nombra la ficha?", "Chuquicamata y El Teniente", "Aparecen como ejemplos de gran minería."),
        ("{F} ¿Qué cobraba el Estado chileno a las empresas del cobre?", "Impuestos", "La ficha lo dice."),
        ("{F} ¿Qué necesitaba el industrial de la evidencia 3?", "Máquinas que solo se consiguen en el extranjero", "La carta lo dice."),
        ("{F} ¿Qué evidencia muestra que las utilidades salían del país? A) La evidencia 1 B) La evidencia 2", "A) La evidencia 1", "El economista lo afirma."),
        ("{F} ¿Qué muestra la evidencia 2? A) Que el Estado usaba impuestos del cobre en gasto público B) Que el cobre no se exportaba", "A) Que el Estado usaba impuestos del cobre en gasto público", "El ministro nombra escuelas, caminos y fábricas del Estado."),
        ("{F} ¿Qué es la dependencia? A) Necesitar de otro país para producir o financiarse B) Producir todo dentro del país", "A) Necesitar de otro país para producir o financiarse", "Así se define en la explicación."),
        ("{F} Afirmación: «El Estado obtenía recursos de las empresas del cobre». ¿Qué evidencia la apoya? A) La evidencia 2 B) La evidencia 3", "A) La evidencia 2", "El ministro afirma que los impuestos al cobre financian obras."),
        ("{F} Afirmación: «Las fábricas chilenas dependían de tecnología extranjera». ¿Qué evidencia la apoya? A) La evidencia 3 B) La evidencia 1", "A) La evidencia 3", "El industrial necesita máquinas del extranjero."),
        ("{F} ¿Qué empresas controlaban la gran minería del cobre en Chile según la ficha? A) Empresas de Estados Unidos B) Empresas del Reino Unido", "A) Empresas de Estados Unidos", "La ficha lo dice de forma directa."),
        ("{F} ¿Por qué la evidencia 1 y la evidencia 2 no se contradicen del todo?", "Porque una habla de utilidades que salen y otra de impuestos que se quedan, y ambas pueden ocurrir a la vez", "Hablan de dinero distinto: ganancias y recaudación."),
        ("{F} Un estudiante escribe: «Estados Unidos controlaba toda la economía chilena». ¿Qué corrección propones? A) La ficha solo muestra su fuerte presencia en la gran minería del cobre B) Está correcto porque había empresas estadounidenses", "A) La ficha solo muestra su fuerte presencia en la gran minería del cobre", "La conclusión no debe ir más allá de la evidencia."),
        ("{F} ¿Qué dato permitiría precisar el efecto de las empresas? A) Cifras de utilidades que salían y de impuestos recaudados B) La cantidad de caminos construidos", "A) Cifras de utilidades que salían y de impuestos recaudados", "Permitiría comparar lo que salía con lo que se recaudaba."),
        ("{F} ¿Cuál es la afirmación mejor formulada? A) La participación de Estados Unidos en el cobre tuvo efectos mixtos: dependencia externa y recursos fiscales B) Estados Unidos solo perjudicó a Chile", "A) La participación de Estados Unidos en el cobre tuvo efectos mixtos: dependencia externa y recursos fiscales", "Toma en cuenta evidencias de signos distintos."),
    ],
    ctx=("Un compañero sostiene que la presencia de empresas extranjeras fue solo positiva porque pagaban impuestos. ¿Qué evidencia de la ficha debería considerar? A) La evidencia 1, sobre utilidades que salen del país B) La evidencia 3, sobre las máquinas del extranjero", "A) La evidencia 1, sobre utilidades que salen del país", "Muestra un efecto negativo que contradice una visión solo positiva; la evidencia 3 habla de tecnología, no de utilidades."),
    sc=[("¿Qué es la dependencia económica?", "Necesitar de otro país para producir o financiarse", "Así se define en el vocabulario."),
        ("¿Qué son las utilidades?", "Las ganancias que obtiene una empresa", "Así se define en la clase."),
        ("{F} ¿Qué dice la evidencia 2 sobre los impuestos?", "Que financian escuelas, caminos y fábricas del Estado", "El discurso lo afirma.")],
    op=("Escribe un párrafo de cuatro a seis líneas que responda la pregunta de la ficha. Debe tener una afirmación, al menos dos evidencias citadas con su número y un límite. {F}",
        "«La participación de empresas de Estados Unidos fue fuerte en la gran minería del cobre y tuvo efectos mixtos. La evidencia 1 muestra que las utilidades salían del país y la evidencia 2 que los impuestos financiaban obras. No se puede medir con estas fuentes cuánto salía ni cuánto se recaudaba.»",
        ["tiene afirmación, evidencia y límite", "cita dos evidencias", "no generaliza a toda la economía"], ["párrafo escrito"], ["no citar evidencias", "decir que controlaban todo"],
        "Pide que explique qué cifras buscaría para precisar el efecto."),
    reinforce="Explica en voz alta qué significa que una economía dependa de empresas de otro país.",
    extend="Busca en tu casa un producto de una empresa extranjera y piensa qué parte de su valor queda en Chile.",
)

# ================================================================ OA 06, clase 6
F = ("Ficha 6 (debate: Estado industrializador y Estado de bienestar). "
     "Hechos: en 1920 se aprueba la ley de instrucción primaria obligatoria; en 1924 se crea el seguro obligatorio de trabajadores; en 1952 se crea el Servicio Nacional de Salud; en 1953 se crea la Corporación de la Vivienda (CORVI). "
     "Bienestar social: acciones del Estado para mejorar educación, salud, vivienda y previsión (ayudas para vejez, enfermedad o invalidez). "
     "Posición A, de ejemplo: «El Estado debe priorizar fábricas y empleo, porque sin producción no hay recursos para el bienestar.» "
     "Posición B, de ejemplo: «El Estado debe priorizar escuelas, salud y vivienda, porque son derechos que no pueden esperar.» "
     "Límites a considerar: no todos los grupos accedieron por igual a esos servicios; los recursos del Estado son limitados; muchas obras se concentraron en las ciudades.")
build(
    OA, 6, F,
    use="Aprenderé a debatir las consecuencias y los límites del Estado industrializador y del bienestar social en Chile, con argumentos basados en evidencia.",
    prior=["Sé qué fue la CORFO y la ISI.", "Sé distinguir afirmación, evidencia y límite.", "Sé que los recursos del Estado son limitados."],
    explain=[
        "Desde las primeras décadas del siglo XX el Estado chileno asumió tareas de bienestar social: educación, salud, vivienda y previsión. Previsión significa ayudas económicas por vejez, enfermedad o invalidez. Hechos de la ficha son la ley de instrucción primaria obligatoria de 1920, el seguro obligatorio de 1924, el Servicio Nacional de Salud de 1952 y la CORVI en 1953.",
        "Un debate histórico no consiste en gritar opiniones, sino en dar razones. La posición A sostiene que primero hay que industrializar para tener recursos. La posición B sostiene que escuelas, salud y vivienda son derechos urgentes. Un buen argumento tiene una tesis, una razón, una evidencia y reconoce qué dice la otra posición. También reconoce límites: servicios que no llegaban a todos y recursos que se concentraban en las ciudades.",
        "Evaluar consecuencias exige comparar a corto y largo plazo. Más escuelas aumentan la cantidad de personas que saben leer, pero ese efecto se ve con los años. Una fábrica da empleo pronto, pero puede depender de maquinaria importada. Quien debate debe decir qué efecto mide, cuándo ocurre y para quién. Así se evitan frases como «todo salió bien» o «todo salió mal».",
    ],
    vocab=[("bienestar social", "acciones del Estado para mejorar educación, salud, vivienda y previsión"), ("previsión", "ayudas económicas por vejez, enfermedad o invalidez"), ("tesis", "idea central que se defiende en un debate"), ("argumento", "razón que apoya una tesis, con evidencia"), ("contraargumento", "razón que responde a la posición contraria")],
    worked=[
        ("Armar un argumento", "Tesis de ejemplo: «El Estado debe construir escuelas». ¿Qué razón la apoya?", ["Busco una razón relacionada con el derecho a estudiar.", "La ley de 1920 hizo obligatoria la educación primaria."], "La educación primaria obligatoria exige escuelas para todos"),
        ("Reconocer un límite", "Un servicio de salud se instala en las ciudades pero no llega a una aldea rural. ¿Qué límite muestra?", ["El servicio existe, pero no llega a todos.", "Es un problema de cobertura."], "Que no todos los grupos accedieron por igual"),
    ],
    mistakes=[("Defender una posición diciendo solo «porque sí».", "Falta una razón y una evidencia.", "Agrega por qué y qué hecho lo respalda."),
              ("Ignorar lo que dice la posición contraria.", "Se debilita el argumento.", "Incluye un contraargumento y respóndelo.")],
    T=[
        ("{F} ¿Qué se crea en 1952?", "El Servicio Nacional de Salud", "Está en la lista de hechos."),
        ("{F} ¿Qué es la previsión?", "Ayudas económicas por vejez, enfermedad o invalidez", "La ficha la define así."),
        ("{F} ¿Qué posición prioriza las fábricas y el empleo?", "La posición A", "Su cita lo dice."),
        ("{F} ¿Qué hecho hizo obligatoria la educación primaria? A) La ley de 1920 B) La CORVI de 1953", "A) La ley de 1920", "Así lo señala la ficha; la CORVI se refiere a vivienda."),
        ("{F} ¿Qué área atiende la CORVI? A) Vivienda B) Salud", "A) Vivienda", "Se creó para vivienda, según la ficha."),
        ("{F} ¿Qué razón da la posición B? A) Que son derechos que no pueden esperar B) Que sin fábricas no hay recursos", "A) Que son derechos que no pueden esperar", "La segunda razón es de la posición A."),
        ("{F} ¿Qué hecho de la ficha se relaciona más con la previsión? A) El seguro obligatorio de trabajadores de 1924 B) La CORVI de 1953", "A) El seguro obligatorio de trabajadores de 1924", "Un seguro de trabajadores ofrece ayudas ante enfermedad o invalidez; la CORVI atiende vivienda."),
        ("{F} Un debatiente dice: «El Estado debe construir viviendas porque hay familias sin casa». ¿Qué posición apoya? A) La posición B B) La posición A", "A) La posición B", "Prioriza vivienda como derecho urgente."),
        ("{F} Un debatiente responde a la posición A diciendo: «Las fábricas dan empleo, pero no enseñan a leer a los niños». ¿Qué hace? A) Un contraargumento B) Una tesis nueva sin relación", "A) Un contraargumento", "Responde a una razón de la posición contraria."),
        ("{F} ¿Por qué se dice que una escuela y una fábrica tienen efectos en plazos distintos?", "Porque la fábrica da empleo pronto y la educación muestra resultados con los años", "La explicación compara corto y largo plazo."),
        ("{F} Un compañero dice: «Con las leyes de bienestar, todos los chilenos tuvieron los mismos servicios». ¿Qué corriges? A) La ficha señala que no todos los grupos accedieron por igual B) Nada, es correcto", "A) La ficha señala que no todos los grupos accedieron por igual", "Es uno de los límites mencionados."),
        ("{F} ¿Qué argumento está mejor formulado? A) «Debe priorizarse la salud porque el Servicio Nacional de Salud de 1952 buscaba llegar a más personas, aunque los recursos eran limitados» B) «Debe priorizarse la salud porque sí»", "A) «Debe priorizarse la salud porque el Servicio Nacional de Salud de 1952 buscaba llegar a más personas, aunque los recursos eran limitados»", "Tiene razón, evidencia y límite."),
        ("{F} ¿Cuál es la mejor síntesis del debate? A) Ambas posiciones tienen razones válidas y los recursos limitados obligan a decidir prioridades B) Una posición está siempre equivocada", "A) Ambas posiciones tienen razones válidas y los recursos limitados obligan a decidir prioridades", "Reconoce valor y límite de las dos posiciones."),
    ],
    ctx=("En tu curso discuten si el gasto del Estado debe ir primero a industrias o a hospitales. ¿Qué haces para argumentar bien? A) Dar una tesis con razones, evidencias y responder al otro lado B) Repetir tu opinión sin dar razones", "A) Dar una tesis con razones, evidencias y responder al otro lado", "Un debate histórico se basa en razones y evidencias."),
    sc=[("¿Qué es el bienestar social?", "Acciones del Estado para mejorar educación, salud, vivienda y previsión", "Así se define en el vocabulario."),
        ("¿Qué es un contraargumento?", "Una razón que responde a la posición contraria", "Así se define en la clase."),
        ("En Historia: ¿qué es una tesis en un debate?", "La idea central que se defiende", "Así se define en el vocabulario de la clase.")],
    op=("Escribe un mini debate de seis líneas. Elige la posición A o la B de la ficha. Escribe tu tesis, dos razones con evidencia de la ficha, un contraargumento a la posición contraria y un límite que reconozcas. {F}",
        "Posición B: «El Estado debe priorizar escuelas y salud. Razón 1: la ley de 1920 hizo obligatoria la primaria. Razón 2: en 1952 se creó el Servicio Nacional de Salud. Contraargumento: la posición A tiene razón en que se necesitan recursos, pero ellos no deben retrasar derechos. Límite: no todos los grupos accedieron por igual».",
        ["tiene tesis y dos razones con evidencia", "responde a la otra posición", "reconoce un límite"], ["mini debate escrito"], ["argumentar sin evidencia", "ignorar la posición contraria"],
        "Pide que explique qué hecho adicional buscaría para fortalecer su argumento."),
    reinforce="Explica en voz alta una tesis con una razón y una evidencia sobre qué debe priorizar el Estado.",
    extend="Pregunta a una persona de tu casa qué servicio del Estado considera más urgente y por qué; anota su razón.",
)
