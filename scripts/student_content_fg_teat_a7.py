"""Teatro 3.º y 4.º medio FG: OAC-04 (propósitos expresivos y contexto de obras teatrales), clases 4 y 5. Obras y textos originales e inventados; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O4 = "FG-TEAT-3y4-OAC-04"

# ============================================================ OAC-04, clase 4
F = ("Ficha 4 (tres obras de ejemplo, inventadas, sin autoría ni fecha real). Obra 1, «El pozo de la plaza»: comedia representada en una plaza por vecinos de un pueblo agrícola, con el público de pie alrededor; usa exageraciones y música tocada en vivo. "
     "Obra 2, «Los turnos»: drama representado en una sala cerrada por una compañía profesional; cuenta la vida de obreros de una fábrica durante una huelga de ejemplo, con poco movimiento y diálogo directo. "
     "Obra 3, «La sombra del río»: teatro de títeres con figuras de cartón manipuladas, creado por un grupo de una ciudad costera para niños; cuenta una leyenda inventada sobre un río.")
build(
    O4, 4, F,
    use="Aprenderé a considerar la época, el entorno y el contexto de producción, además del género y el origen de una obra, para inferir su propósito expresivo sin apoyarme en estereotipos.",
    prior=["Sé inferir el propósito con rasgos y pistas.", "Sé analizar con rasgo, efecto y propósito.", "Sé separar hechos de opiniones."],
    explain=[
        "El contexto de una obra reúne las circunstancias en que se creó y se presenta. La época es el momento histórico con sus valores, problemas y formas de vivir. El entorno es el lugar físico y social: un pueblo, una ciudad, una plaza, una sala cerrada. El contexto de producción dice quién la hizo, para quién y dónde. Estos datos ayudan a entender por qué una obra se parece a lo que es y qué quería expresar.",
        "Las obras también se agrupan por género, que es el tipo de obra según su tono y su manera de contar. La comedia busca provocar risa y mostrar situaciones con humor; el drama trata conflictos serios con un tono más grave. Tragedia y comedia son géneros que nacen en el teatro de la antigua Grecia. Hay además formas como el teatro de títeres, en que figuras manipuladas hacen de personajes, el teatro de calle y el teatro comunitario, hecho por vecinos. Las obras tienen orígenes diversos, nacionales y extranjeros, populares y profesionales.",
        "El contexto ayuda, pero no reemplaza la evidencia de la obra: se combinan rasgos y contexto. Hay que evitar estereotipos, por ejemplo suponer que todas las obras de un lugar son de un mismo tipo. Tampoco se juzga una obra de otra época solo con las costumbres de hoy; primero se entiende qué valores y problemas había y luego se discute. Las obras de esta clase son descripciones inventadas, sin fechas ni autores reales.",
    ],
    vocab=[("época", "momento histórico con sus valores, problemas y formas de vivir"), ("entorno", "lugar físico y social donde se crea o se presenta la obra"), ("contexto de producción", "quién hizo la obra, para quién y dónde"), ("género", "tipo de obra según su tono y su manera de contar, como comedia o drama"), ("teatro de títeres", "forma teatral en que figuras manipuladas hacen de personajes"), ("estereotipo", "idea fija y simplificada sobre un grupo o lugar")],
    worked=[
        ("Usar el contexto", "Una obra se presenta en una plaza, de pie y con música en vivo, para toda una comunidad. ¿Qué dice el contexto sobre su propósito?", ["Un espacio abierto y colectivo sugiere una obra pensada para reunir a muchas personas.", "La música en vivo y la exageración sugieren que busca divertir y animar."], "Divertir y reunir a la comunidad"),
        ("Evitar un estereotipo", "Alguien dice: «Las obras de ese país son todas dramas». ¿Qué conviene responder?", ["Esa afirmación generaliza a partir de pocos casos.", "Hay que revisar obras concretas y su contexto, y no suponer."], "No generalizar: revisar obras concretas"),
    ],
    mistakes=[("Suponer que todas las obras de un lugar o de una época son iguales.", "Es un estereotipo; cada obra tiene su propio contexto y rasgos.", "Analiza obras concretas y cita sus rasgos."),
              ("Juzgar una obra de otra época solo con las costumbres actuales.", "Se pierde lo que quiso expresar para su público de entonces.", "Primero entiende su contexto; luego discútela con respeto.")],
    T=[
        ('abc', '¿Qué es el contexto de una obra?', 'Las circunstancias de época, entorno y producción en que se creó y se presenta', 'La lista de personajes y la duración de la función, tal como figuran en el programa de mano', 'El comentario del público al terminar la presentación', 'El contexto reúne datos sobre cuándo, dónde y para quién se hizo la obra.'),
        ('abc', '{F} ¿Qué rasgo del entorno de la obra 1 influye en cómo se presenta?', 'Se presenta en una plaza con público de pie, por eso usa exageraciones y música en vivo', 'Se presenta en una sala cerrada por una compañía profesional, con poco movimiento y diálogo directo entre obreros', 'Se presenta con figuras manipuladas para un público de niños', 'El espacio abierto y el público alrededor explican sus recursos; las otras opciones describen otras obras.'),
        ('abc', '¿Qué distingue a un drama de una comedia?', 'El drama trata conflictos serios con tono grave; la comedia busca la risa y el humor', 'El drama siempre es más largo que la comedia y se presenta en salas cerradas', 'La comedia no tiene conflicto y el drama sí', 'Se distinguen por el tono y el modo de contar; ambos tienen conflicto.'),
        ('abc', '{F} ¿Qué propósito se infiere de la obra 1 con apoyo en su contexto?', 'Divertir y reunir a la comunidad en un espacio público', 'Denunciar las condiciones de trabajo en una fábrica', 'Transmitir una leyenda a niños de una ciudad costera', 'Plaza, vecinos, música en vivo y comedia apuntan a reunir y divertir.'),
        ('abc', '{F} ¿Qué dato del contexto ayuda a entender el propósito de la obra 2?', 'Cuenta la vida de obreros de una fábrica durante una huelga de ejemplo', 'Se presenta en una plaza con música en vivo y con el público de pie alrededor de los vecinos', 'Está hecha con figuras de cartón para niños', 'El tema, los obreros y la huelga, orienta el propósito hacia el mundo del trabajo.'),
        ('abc', '¿Qué es el teatro de títeres?', 'Una forma teatral en la que figuras manipuladas hacen de personajes', 'Un género que solo se hace en plazas, con público de pie y música tocada en vivo', 'Una obra con música en vivo hecha por vecinos', 'Se define por las figuras manipuladas, no por el lugar ni por la música.'),
        ('=', 'En una plaza hay 120 personas de público y el 25 % son niños. ¿Cuántos niños hay?', '120*25//100', 'Se calcula la cuarta parte del público.', ' niños'),
        ('abc', '{F} Un grupo analiza la obra 2 y dice: «los obreros hablan tan directo porque no saben actuar». ¿Qué le falta?', 'Considerar que el diálogo directo puede ser una elección de estilo ligada al contexto', 'Aceptar que el diálogo directo es una falla de la compañía, que no supo darle más recursos a la escena', 'Cambiar el género de la obra a comedia', 'El diálogo directo puede ser una decisión para mostrar la vida del trabajo sin adornos.'),
        ('abc', 'Un grupo descarta una obra de otra época porque «tenía costumbres anticuadas». ¿Qué conviene hacer?', 'Comprender primero los valores y problemas de esa época y luego discutirlos', 'Descartarla, porque una obra debe coincidir con las costumbres actuales', 'Cambiar sus costumbres antes de analizar el propósito, para que se parezca a lo que hoy se espera de una obra', 'Entender el contexto permite analizar con justicia y luego discutir con respeto.'),
        ('abc', 'Dos obras tratan sobre el trabajo: una comedia de plaza y un drama de sala. ¿Qué cambia entre ellas?', 'El género, el tono y el modo de presentar, y con ello el propósito percibido', 'Nada, porque tratan el mismo tema del trabajo y por eso comunican exactamente lo mismo', 'Solo el número de intérpretes que participan', 'El mismo tema puede tener propósitos distintos según el género y el espacio.'),
        ('abc', 'Un estudiante dice: «Todas las obras de los pueblos agrícolas son comedias simples». ¿Qué error comete?', 'Generaliza a partir de pocos casos y cae en un estereotipo', 'Confunde la comedia con el drama en una obra concreta', 'Olvida mencionar el nombre de la compañía', 'Una generalización ignora la variedad de obras y contextos.'),
        ('=', 'Una compañía presenta «Los turnos» en 4 funciones. En cada una asisten 85 personas y 35 son estudiantes. ¿Cuántas personas que no son estudiantes asisten entre todas las funciones?', '(85-35)*4', 'Se resta el número de estudiantes de cada función y se multiplica por las funciones.', ' personas'),
        ('abc', 'Un grupo quiere inferir el propósito de una obra extranjera cuyo contexto desconoce. ¿Qué conviene?', 'Buscar información del contexto en fuentes confiables y contrastarla con los rasgos de la obra', 'Suponer que el contexto es igual al de las obras de su entorno y analizar solo según lo que ya conoce', 'Inferir solo con lo que le gustó de la obra', 'El contexto se averigua, y se contrasta con la evidencia de la propia obra.'),
    ],
    ctx=('ab', 'Vas a analizar una obra de otro país. ¿Qué haces antes de inferir su propósito?', 'Investigar su contexto y leerla con ese dato junto a sus rasgos', 'Suponer que es igual a las obras de tu entorno', 'El contexto cambia lo que la obra comunica y se averigua sin suponer.'),
    sc=[
        ("En Teatro: ¿qué es el contexto de producción?", "Quién hizo la obra, para quién y dónde", "Explica por qué la obra se presenta de cierta manera."),
        ("En Teatro: ¿Qué es un estereotipo?", "Una idea fija y simplificada sobre un grupo o lugar", "Los estereotipos ignoran la variedad de cada obra."),
        ("¿Se puede juzgar una obra de otra época solo con las costumbres de hoy?", "No, primero se comprende su época y luego se discute", "Así se analiza con justicia y respeto."),
    ],
    op=("Escoge una de las tres obras de ejemplo de la ficha. Escribe: su género, su entorno, un dato de su contexto de producción, un rasgo observable y el propósito que infieres combinando rasgo y contexto. Evita estereotipos.",
        "Obra 3: teatro de títeres; entorno, una ciudad costera; contexto, grupo que crea para niños; rasgo, figuras de cartón manipuladas; propósito, transmitir una leyenda de manera cercana a niños, usando un río como elemento de su entorno.",
        ["identifica género y entorno", "incluye un dato de contexto de producción", "cita un rasgo observable", "propone un propósito sin estereotipos"],
        ["hoja con las cinco respuestas"],
        ["generalizar sobre un lugar o época", "olvidar el rasgo observable"],
        "Pregunta: «¿qué rasgo de la obra respalda tu idea además del contexto?». Debe citarlo."),
    reinforce="Escribe tres datos de contexto que te gustaría averiguar de una obra extranjera antes de inferir su propósito.",
    extend="Explica por qué el contexto ayuda a inferir un propósito, pero no reemplaza lo que muestra la obra.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 5 (cuatro inferencias de ejemplo sobre el texto «La caja», inventadas). Inferencia 1: «Es una obra triste porque a mí me dio pena.» "
     "Inferencia 2: «Muestra un adiós contenido; lo sostienen las pausas y la llave que se deja (evidencia) y la oficina vacía de noche (entorno).» "
     "Inferencia 3: «Es una comedia porque tiene personajes.» Inferencia 4: «Habla de la distancia entre dos personas; lo sostiene que Elena no mira a David y habla de la caja.»")
build(
    O4, 5, F,
    use="Aprenderé a revisar y a fundamentar mis inferencias sobre el propósito de una obra: afirmación, evidencia observable, criterio estético y contexto, y a ajustarlas cuando aparece información nueva.",
    prior=["Sé inferir el propósito con rasgos y pistas.", "Sé usar el contexto de época y entorno.", "Sé separar opinión de evidencia."],
    explain=[
        "Una inferencia sólida tiene cuatro partes. La afirmación dice cuál es el propósito que se propone. La evidencia son los rasgos observables que la sostienen, como pausas, gestos o un objeto. El criterio estético explica cómo se ve ese rasgo en el lenguaje teatral, por ejemplo el uso de la voz o de la luz. El contexto aporta datos de época o entorno que ayudan a entender el sentido. Si falta la evidencia, es solo una opinión.",
        "Revisar una inferencia es comprobarla. Se pregunta: ¿cada afirmación tiene un rasgo que la respalde?, ¿otra persona puede comprobar ese rasgo?, ¿hay algo en la obra que la contradiga? Una buena inferencia reconoce sus límites: si se desconoce el contexto de producción, se dice que la lectura es provisional. Si aparece un dato nuevo, se ajusta la inferencia en vez de defenderla a toda costa.",
        "Dos personas pueden proponer lecturas distintas de la misma obra. Se comparan según cuánta evidencia reúnen y cuántos rasgos explican, no según quién habla más fuerte. La conversación se hace con respeto: se escucha, se pregunta por la evidencia y se acepta cambiar de idea cuando hay buenas razones.",
    ],
    vocab=[("afirmación", "idea que se propone sobre el propósito de la obra"), ("evidencia", "rasgo observable que respalda la afirmación"), ("provisional", "que puede cambiar si aparece nueva información"), ("contradicción", "dato que va en contra de lo que se afirma"), ("fundamentar", "apoyar una idea con razones y evidencia")],
    worked=[
        ("Revisar una inferencia", "«La obra muestra amistad porque los dos personajes están en escena». ¿Qué falla?", ["Estar en escena no prueba amistad; no hay un rasgo que sostenga la afirmación.", "Habría que citar gestos, tono o acciones que muestren cuidado entre ellos."], "Falta evidencia observable específica"),
        ("Ajustar con información nueva", "Tu inferencia dice que una obra es una comedia, pero el programa informa que es un drama con momentos de humor. ¿Qué haces?", ["Revisas los rasgos: ¿hay humor en toda la obra o en algunos momentos?", "Ajustas la inferencia reconociendo el drama con humor."], "Se ajusta la inferencia con el dato nuevo"),
    ],
    mistakes=[("Defender una inferencia aunque aparezca un dato que la contradice.", "Una inferencia debe poder cambiar con nueva información.", "Revisa y ajusta tu lectura."),
              ("Dar por cierta una lectura sin decir qué evidencia la sostiene.", "Sin evidencia es una opinión.", "Cita el rasgo y explica su efecto.")],
    T=[
        ('abc', '¿Qué partes tiene una inferencia sólida?', 'Afirmación, evidencia observable, criterio estético y contexto', 'Solo una opinión y una emoción personal sobre lo que le pareció a quien mira la obra', 'Un resumen de la historia y el nombre de quienes actuaron', 'La inferencia se compone de una idea sostenida por evidencia, criterio y contexto.'),
        ('abc', '{F} ¿Qué inferencia se basa solo en una reacción personal?', 'La inferencia 1, que solo dice que dio pena', 'La inferencia 2, que cita pausas y la llave', 'La inferencia 4, que cita que Elena no mira a David', 'La primera no cita ningún rasgo de la obra, solo lo que sintió quien la escribió.'),
        ('abc', '{F} ¿Por qué es débil la inferencia 3?', 'Tener personajes no prueba que sea comedia, porque todas las obras los tienen', 'Porque una comedia no puede ocurrir en una oficina ni tener personajes que hablen de trabajo', 'Porque habla de una caja y no de personas', 'El rasgo que cita es común a todas las obras y no sostiene el género.'),
        ('abc', '{F} ¿Qué parte de la inferencia 2 corresponde al contexto o entorno?', 'La oficina vacía de noche', 'Las pausas', 'La llave que se deja', 'La oficina vacía de noche describe el lugar; pausas y llave son evidencias de la puesta.'),
        ('abc', 'Aparece un dato nuevo que contradice tu inferencia. ¿Qué haces?', 'La revisas y, si hace falta, la ajustas', 'La mantienes igual para no confundir a nadie', 'La descartas sin volver a mirar la obra', 'Una inferencia puede cambiar con nueva información; se revisa con la obra.'),
        ('abc', '¿Qué diferencia hay entre una inferencia y una opinión?', 'La inferencia cita evidencia observable; la opinión puede no hacerlo', 'La opinión siempre es más correcta que la inferencia porque nace de lo que cada persona siente de verdad', 'No hay diferencia, porque ambas son lo mismo', 'La evidencia observable es lo que hace comprobable a una inferencia.'),
        ('=', 'Una pauta de 4 criterios vale 2 puntos cada uno. La inferencia 2 cumple tres criterios completos y el cuarto a medias (1 punto). ¿Cuántos puntos suma?', '3*2+1', 'Se suman los criterios completos y el medio puntaje del cuarto.', ' puntos'),
        ('abc', '{F} ¿Cuál reescritura mejora la inferencia 1?', 'Muestra un adiós contenido: las pausas y el silencio al despedirse sostienen esa lectura', 'Es una obra triste porque a todos les da pena ver cómo se despiden dos personas', 'Es una obra triste porque la escribió alguien serio', 'Cita rasgos observables en vez de apoyarse en una reacción personal.'),
        ('abc', 'Un compañero no está de acuerdo con tu inferencia. ¿Qué haces?', 'Escuchar su lectura, comparar evidencias y ajustar la tuya si hay buenas razones', 'Repetir tu idea cada vez más fuerte hasta que el compañero la acepte y termine la discusión', 'Evitar hablar del tema para no discutir', 'La conversación respetuosa compara evidencias y permite cambiar de idea.'),
        ('abc', 'Dos inferencias distintas sobre la misma obra citan buena evidencia. ¿Cómo se comparan?', 'Se revisa cuál explica más rasgos de la obra, sin exigir que haya una única lectura', 'Se elige la que defiende la persona que habla primero, para ahorrar tiempo y no discutir más', 'Se descartan ambas por no coincidir', 'Se comparan por evidencia y alcance; varias lecturas pueden ser razonables.'),
        ('abc', 'Alguien dice: «No se puede inferir nada porque no conozco a quien escribió la obra». ¿Qué respuesta es adecuada?', 'El texto y su puesta ya dan pistas; conocer el contexto ayuda, pero no es la única fuente', 'Tiene razón, porque sin conocer al autor ni su vida no se entiende nada de lo que la obra muestra', 'Debe inventar un autor para poder analizar la obra', 'La obra misma ofrece evidencia, y el contexto la complementa.'),
        ('=', 'Ocho estudiantes escribieron inferencias y seis citaron evidencia. ¿Qué porcentaje citó evidencia?', '6*100//8', 'Se divide quienes citaron evidencia entre el total y se pasa a porcentaje.', ' %'),
        ('abc', 'Un grupo escribe: «el propósito parece ser X, con tres evidencias, aunque desconocemos el contexto de producción, por lo que es una lectura provisional». ¿Qué valor tiene la última parte?', 'Reconoce los límites de la inferencia y la deja abierta a revisión', 'Muestra que el grupo no sabe analizar la obra y por eso deja su inferencia sin terminar', 'Resta valor a la evidencia ya presentada', 'Señalar límites es parte de una buena inferencia y permite ajustarla después.'),
    ],
    ctx=('ab', 'Terminaste de escribir tu inferencia. ¿Qué revisas antes de entregarla?', 'Que cada afirmación tenga una evidencia que otra persona pueda comprobar', 'Que la redacción tenga muchos adjetivos para que suene mejor', 'Cada afirmación necesita evidencia comprobable para ser una inferencia.'),
    sc=[
        ("En Teatro: ¿qué es la evidencia en una inferencia?", "Un rasgo observable de la obra que respalda la afirmación", "Es lo que permite comprobar la inferencia."),
        ("¿Qué significa que una inferencia es provisional?", "Que puede cambiar si aparece información nueva", "Reconoce los límites de lo que se sabe."),
        ("¿Cómo se compara una lectura con otra distinta de la misma obra?", "Se revisa cuál tiene más evidencia y explica más rasgos", "No se decide por quién habla más fuerte."),
    ],
    op=("Usa esta descripción original: en una oficina vacía de noche, una persona recoge sus cosas en una caja, deja una llave sobre el escritorio y otra persona la mira en silencio hasta que se cierra la puerta. Escribe una inferencia completa con afirmación, dos evidencias, un criterio estético y un dato de contexto. Termina con una frase que reconozca un límite de tu lectura.",
        "Afirmación, muestra un adiós contenido. Evidencias: la llave que se deja y la mirada en silencio. Criterio: uso del silencio y de los objetos. Contexto: oficina vacía de noche. Límite: no conocemos cómo la presentó cada compañía, así que la lectura es provisional.",
        ["afirmación clara", "dos evidencias observables", "criterio estético", "contexto y límite reconocido"],
        ["inferencia completa de cuatro o cinco oraciones"],
        ["dar solo opiniones", "no reconocer límites"],
        "Pregunta: «¿qué pasaría con tu inferencia si aparece un dato nuevo?». Debe poder ajustarla."),
    reinforce="Revisa una inferencia tuya anterior y marca cuáles afirmaciones tienen evidencia y cuáles no.",
    extend="Explica por qué reconocer los límites de una inferencia la hace más confiable y no más débil.",
)
