"""Mundo global 3.º y 4.º medio FG: OA 07 (propuestas locales frente a problemas globales). Barrio, cifras y voces de ejemplo inventados."""
from __future__ import annotations

from fg_mglo_common import build

O7 = "FG-MGLO-3y4-OAC-07"

# ============================================================ OA 07, clase 1
F = ("Ficha 1 (barrio ficticio El Roble, comuna de Valle Alto). Problema observado: en los veranos hay olas de calor y el barrio casi no tiene sombra. De las 3 plazas, solo 1 tiene árboles. "
     "Viven 400 familias; la escuela, la junta de vecinos, el comercio local y el municipio actúan en el barrio. "
     "Vínculo global: el calor extremo es una de las consecuencias del cambio climático, que se origina en emisiones de todo el mundo.")
build(
    O7, 1, F,
    use="Aprenderé a ubicar un problema local que se relaciona con un tema global, a identificar a los actores del barrio y a empezar un trabajo colaborativo con reglas claras.",
    explain=[
        "Muchos problemas globales, como el cambio climático, las migraciones o los desastres, se viven en lo local: en un barrio, una escuela o una comuna. Por eso se dice que lo global se manifiesta en lo local. Un problema local es una situación concreta del entorno cercano que afecta a personas reales y que se puede observar, medir y trabajar con actores del lugar.",
        "Para empezar se hace un diagnóstico: describir qué ocurre, dónde, desde cuándo, a quiénes afecta y qué datos hay. Luego se identifican los actores (vecinas y vecinos, escuela, organizaciones, comercio, municipio, otros servicios) y sus recursos. Contextualizar también es ubicar la escala: algunas causas son globales y no se pueden resolver desde el barrio, pero sí se pueden reducir sus efectos o preparar a la comunidad.",
        "Trabajar de forma colaborativa significa decidir en conjunto con roles claros, escucha activa, acuerdos por escrito y distribución de tareas. Todos los proyectos escolares se hacen con seguridad: sin entrar a zonas de riesgo, con apoyo de personas adultas, sin manipular materiales peligrosos y sin exponer datos personales.",
    ],
    vocab=[("problema local", "situación concreta del entorno cercano que afecta a personas reales"), ("diagnóstico", "descripción de un problema con sus datos, actores y causas"), ("actor local", "persona u organización que actúa en el territorio"), ("trabajo colaborativo", "trabajo conjunto con roles, acuerdos y tareas compartidas"), ("escala", "nivel en que ocurre un hecho: barrio, comuna, país o mundo")],
    worked=[
        ("Ubicar la escala", "Una sequía grave afecta a todo un país, y un barrio de ejemplo se queda sin agua en verano. ¿Cuál es el problema local y cuál el global?", ["El barrio sin agua es el problema local.", "La sequía del país está ligada a un proceso global."], "Local: falta de agua del barrio. Global: la sequía vinculada al clima"),
        ("Identificar actores", "Una escuela de ejemplo quiere plantar árboles en la plaza. ¿Qué actores deben participar?", ["La escuela y la junta de vecinos.", "El municipio, que autoriza el uso de la plaza."], "Escuela, junta de vecinos y municipio"),
    ],
    mistakes=[("Elegir un problema tan grande que nadie del barrio puede abordarlo.", "El proyecto no podrá ejecutarse ni medirse.", "Escoge un aspecto concreto del problema que se pueda trabajar en el barrio."),
              ("Decidir sin consultar a quienes viven el problema.", "La propuesta puede no responder a sus necesidades.", "Incluye a las personas afectadas desde el diagnóstico.")],
    T=[
        ("{F} ¿Qué problema local describe la ficha?", "La falta de sombra durante las olas de calor del verano", "La falta de agua potable en las casas", "El exceso de ruido de las plazas", "La ficha habla de calor y poca sombra; no menciona agua ni ruido."),
        ("=", "{F} ¿Cuántas plazas del barrio no tienen árboles?", "3-1", "Se resta a las 3 plazas la que sí tiene árboles."),
        ("{F} ¿Qué vínculo global tiene el problema?", "El calor extremo es una consecuencia del cambio climático global", "Las plazas se financian con dinero de otros países", "Las olas de calor se deben a la migración", "La ficha lo une con el cambio climático; la migración y el dinero no se mencionan."),
        ("{F} ¿Cuál de estos es un actor del barrio?", "La junta de vecinos", "Un organismo de otro continente sin presencia local", "Una empresa que no opera en la comuna", "La junta de vecinos actúa en el barrio; los otros no están en el territorio."),
        ("{F} ¿Qué paso corresponde primero en el trabajo colaborativo?", "Hacer un diagnóstico del problema con datos y con los actores del barrio", "Comprar materiales para una obra ya decidida", "Elegir a una sola persona para decidir por todos", "El diagnóstico va antes; sin él se actúa sin conocer el problema."),
        ("{F} ¿Por qué el barrio no puede resolver por sí solo la causa global del calor?", "Porque las emisiones que lo causan provienen de todo el mundo", "Porque los barrios no tienen derecho a opinar", "Porque el calor no depende de ninguna actividad", "La causa es global y compartida; el barrio puede reducir efectos y preparar a la comunidad."),
        ("Un grupo propone «acabar con el cambio climático» como proyecto del curso. ¿Qué problema tiene ese objetivo?", "Es demasiado grande y general para un barrio", "Es muy pequeño para tener efectos en el barrio", "No se relaciona con ningún tema global", "Un objetivo debe ser concreto, medible y posible de ejecutar; ese es demasiado amplio."),
        ("{F} ¿Qué objetivo local es más concreto y posible?", "Dar sombra a dos de las plazas del barrio el próximo verano", "Detener las olas de calor en toda la región del país", "Eliminar las emisiones de todos los países", "El primero puede ejecutarse y medirse en el barrio; los otros exceden su escala."),
        ("Un curso de ejemplo propone una actividad: subir al techo de la escuela para medir la temperatura. ¿Qué respuesta es adecuada?", "Cambiarla por una medición segura con apoyo adulto", "Hacerla igual, porque medir es lo más importante", "Suspender el proyecto completo, porque ninguna actividad es segura", "La seguridad cuenta: se cambia la actividad por una medición segura, sin cancelar todo el proyecto."),
        ("{F} Una vecina dice: «En El Roble nadie se preocupa». ¿Cómo verificarías la afirmación?", "Con una encuesta breve y anónima a vecinos", "Repitiéndola en la reunión hasta que todos coincidan", "Dando por cierta la frase, porque es una opinión de una vecina", "Se verifica consultando a más personas; repetir una frase o aceptarla sin datos no la comprueba."),
        ("{F} Elige la mejor descripción de un diagnóstico.", "Qué ocurre, dónde, desde cuándo, a quiénes afecta y con qué datos", "Una lista de soluciones que ya se decidieron entre pocos", "Una opinión sobre quién tiene la culpa del problema local", "El diagnóstico describe y mide; no propone soluciones ni busca culpables."),
        ("En un equipo de ejemplo, una persona habla la mayor parte del tiempo y otra no se atreve a hablar. ¿Qué regla de trabajo colaborativo ayuda?", "Turnos de palabra y roles definidos", "Que quien habla más decida por todo el equipo", "Evitar las reuniones para que no haya conflictos", "Turnos y roles dan voz a todos; decidir por el que más habla o evitar reunirse empeora la colaboración."),
        ("{F} Alguien afirma: «El calor del barrio se debe solo a los árboles que faltan». ¿Qué precisión falta?", "Que influyen también el clima global y las calles", "Que los árboles no tienen ninguna relación con el calor del barrio", "Que el calor se debe únicamente al cambio climático", "Hay varias causas; ni los árboles son la única ni dejan de influir."),
    ],
    ctx=("Un liceo de ejemplo quiere ayudar a su barrio frente a las inundaciones por lluvias fuertes, un efecto del clima. El equipo discute si hacer primero un diagnóstico o ir a limpiar un canal. ¿Qué paso es más adecuado, considerando la seguridad?", "Hacer un diagnóstico con adultos y no entrar al canal", "Ir a limpiar el canal de inmediato, aunque nadie sepa si es seguro", "Esperar a que haya una inundación para entender el problema", "El diagnóstico va primero y los canales son zonas de riesgo; esperar una inundación es peligroso e innecesario."),
    sc=[
        ("En Mundo global: ¿qué es un problema local?", "Una situación concreta del entorno cercano que afecta a personas reales", "Se puede observar, medir y trabajar con actores del lugar."),
        ("¿Qué es un diagnóstico?", "Una descripción del problema con datos, actores y causas", "Es el primer paso antes de proponer soluciones."),
        ("=", "En un barrio de ejemplo hay 5 plazas y 2 tienen sombra. ¿Cuántas no tienen sombra?", "5-2", "Se resta a las plazas totales las que sí tienen sombra."),
    ],
    op=("Usa la {F} Escribe una ficha de diagnóstico de cinco líneas: qué ocurre, dónde, a quiénes afecta, qué actores hay y qué dato te falta. Agrega un objetivo local concreto y una regla de seguridad para el equipo.",
        "Hay calor sin sombra en El Roble; solo 1 de 3 plazas tiene árboles. Afecta a las 400 familias, sobre todo a personas mayores. Actores: junta de vecinos, escuela, comercio y municipio. Falta el dato de temperatura. Objetivo: dar sombra a dos plazas el próximo verano. Seguridad: trabajar solo con apoyo adulto.",
        ["describe el problema con datos", "identifica actores", "formula un objetivo concreto", "incluye una regla de seguridad"], ["ficha de cinco líneas", "objetivo y regla"], ["objetivo demasiado amplio", "omitir a los actores afectados"],
        "Pide a otra persona que diga si tu objetivo se puede medir."),
    rx=("Explica con tus palabras cómo un problema global se vive en un barrio.", "Anota tres actores de tu entorno que podrían colaborar en un proyecto del barrio."),
)

# ============================================================ OA 07, clase 2
F = ("Ficha 2 (datos de ejemplo de El Roble, inventados). Encuesta anónima a 50 hogares elegidos al azar: 35 dicen que no tienen una plaza con sombra a menos de 5 minutos de su casa; 15 dicen que sí. "
     "Medición de ejemplo en un día de verano a mediodía: en una plaza con árboles, 28 grados; en una plaza sin árboles, 36 grados. "
     "Fuentes: A) la encuesta del curso; B) el registro del municipio, que cuenta árboles plantados en los últimos 5 años (8 en la comuna); C) un comentario en redes sociales que afirma «todo el barrio sufre».")
build(
    O7, 2, F,
    use="Aprenderé a interrogar fuentes e indicadores de un problema local: encuestas, mediciones y registros, y a decidir qué datos faltan antes de proponer una solución.",
    explain=[
        "Antes de proponer una solución se necesita evidencia. Una encuesta recoge opiniones de una muestra de hogares; una medición recoge datos con un instrumento, como un termómetro; un registro oficial entrega información de una institución. Cada fuente tiene un propósito y límites: la encuesta refleja percepciones, la medición depende de cuándo y dónde se hizo, y el registro depende de qué cuenta la institución.",
        "Un indicador es un dato que resume un aspecto del problema. Por ejemplo, el porcentaje de hogares sin sombra cercana se calcula dividiendo los hogares con el problema entre los encuestados y multiplicando por 100. Una línea base es el valor del indicador antes de actuar, y permite comparar después para saber si la propuesta funcionó. Una meta es el valor que se espera lograr.",
        "Para que los datos sean confiables se explican cómo se obtuvieron (muestra, fecha, lugar y método), se protege la privacidad (encuestas anónimas, sin nombres) y se separan los hechos de las opiniones. Un comentario en redes sin datos no es evidencia suficiente. Se declara también qué dato falta.",
    ],
    vocab=[("indicador", "dato que resume un aspecto del problema"), ("línea base", "valor del indicador antes de actuar"), ("meta", "valor que se espera lograr"), ("muestra", "grupo de hogares o personas que representa a un conjunto mayor"), ("percepción", "lo que las personas creen o sienten sobre un hecho")],
    worked=[
        ("Calcular un indicador", "En una encuesta de 20 hogares, 8 no tienen sombra cercana. ¿Qué porcentaje es?", ["Divide 8 entre 20: 0,4.", "Multiplica por 100."], "40 %"),
        ("Fijar una meta", "La línea base es 70 % de hogares sin sombra. Se desea bajar a la mitad. ¿Cuál es la meta?", ["La mitad de 70 es 35.", "La meta es 35 %."], "35 %"),
    ],
    mistakes=[("Usar un comentario de redes como si fuera un dato.", "No tiene método ni muestra.", "Complementa con una encuesta o una medición propia."),
              ("Medir solo después de actuar.", "Sin línea base no se puede saber si hubo cambio.", "Mide antes y después con el mismo método.")],
    T=[
        ("=", "{F} ¿Qué porcentaje de los hogares encuestados no tiene una plaza con sombra a menos de 5 minutos (35 de 50)?", "35*100/50", "Se divide 35 entre 50 y se multiplica por 100."),
        ("=", "{F} ¿Cuántos grados más hace en la plaza sin árboles que en la plaza con árboles?", "36-28", "Se resta la temperatura de la plaza con árboles a la de la plaza sin árboles."),
        ("{F} ¿Cuál es la línea base del indicador de hogares sin plaza con sombra?", "70 %, el valor antes de actuar", "30 %, el porcentaje de hogares que sí tiene sombra cerca", "35 %, porque son 35 los hogares sin sombra", "La línea base es el valor inicial (35 de 50 es 70 %); 35 es el conteo de hogares y 30 % corresponde a quienes sí tienen sombra."),
        ("{F} ¿Qué tipo de fuente es el registro del municipio?", "Un registro oficial", "Una encuesta de percepciones del barrio", "Un comentario de redes sin método", "Es un registro institucional; la encuesta es la fuente A y el comentario es la C."),
        ("{F} ¿Qué límite tiene la medición de temperatura?", "Se hizo un solo día y en dos plazas", "Se hizo en todas las plazas del país durante un año", "No se hizo con ningún instrumento de medición", "La ficha entrega una medición puntual; no sirve para concluir sobre todos los días."),
        ("{F} ¿Por qué el comentario en redes («todo el barrio sufre») no basta como evidencia?", "Porque no dice cuántas personas opinan, cómo se obtuvo la cifra ni cuándo", "Porque los comentarios en redes siempre son falsos", "Porque solo cuenta lo que dice una autoridad del municipio", "Sin método ni datos no se puede verificar; no significa que siempre sea falso."),
        ("{F} El registro muestra solo 8 árboles plantados en 5 años en toda la comuna. ¿Qué conclusión es adecuada?", "Que hubo poca plantación reciente en la comuna, sin datos de los árboles antiguos", "Que el barrio no tiene ningún árbol en sus calles ni plazas", "Que el municipio nunca ha plantado árboles en ninguna comuna", "El dato es acotado a 5 años y a la comuna; no permite concluir sobre el barrio ni sobre el pasado."),
        ("{F} Si el curso quiere reducir a 35 % los hogares sin sombra, ¿qué es 35 %?", "La meta", "La línea base", "La percepción", "La meta es el valor que se desea alcanzar."),
        ("Una encuesta se hizo solo a las personas que asistieron a la reunión de la junta de vecinos. ¿Qué sesgo tiene?", "Deja fuera a quienes no asisten", "Incluye a todos los hogares del barrio por igual", "No tiene ningún sesgo, porque asistieron muchas personas", "Quienes asisten no representan a todo el barrio; la selección es un sesgo."),
        ("{F} Para saber si una propuesta funcionó, ¿qué dato se necesita además de la línea base?", "Una nueva medición con el mismo método y en las mismas plazas", "Un comentario de apoyo en redes sociales del barrio", "La opinión de quien diseñó la propuesta del curso", "Se compara la medición posterior con la línea base usando el mismo método."),
        ("{F} Una encuesta anónima, sin nombres ni direcciones. ¿Qué protege?", "La privacidad de las personas encuestadas, al no tener nombres", "La opinión del curso frente a otras opiniones", "La exactitud de la medición de temperatura", "El anonimato protege los datos personales."),
        ("{F} Elige la conclusión mejor situada.", "Según la encuesta, 70 % no tiene sombra; falta medir", "Todo el barrio sufre calor y basta plantar árboles sin más análisis", "El problema no existe, porque 15 hogares sí tienen sombra cerca", "Una conclusión situada cita los datos y declara lo que falta; las otras generalizan o niegan."),
        ("Una persona del curso propone preguntar a hogares con nombre y dirección, para «ver quién dice qué». ¿Qué respuesta es más adecuada?", "No pedir datos personales y mantener la encuesta anónima", "Pedirlos, porque así se verifica cada respuesta", "Pedirlos solo a los hogares que respondan que sí", "Los datos personales no son necesarios y exponen a las personas."),
    ],
    ctx=("El curso de ejemplo quiere saber si los adultos mayores del barrio tienen más dificultades con el calor. Consulta solo a 3 abuelas vecinas del curso y concluye que sí. ¿Qué mejora al diseño?", "Ampliar la muestra a hogares de distintas calles y de distintas edades", "Dar por válida la conclusión, porque son personas conocidas", "Descartar el tema, porque las encuestas no sirven nunca", "Tres casos conocidos no representan al barrio; hay que ampliar la muestra."),
    sc=[
        ("En Mundo global: ¿qué es una línea base?", "El valor del indicador antes de actuar", "Permite comparar después para saber si hubo cambio."),
        ("=", "En una encuesta de 40 hogares, 10 no tienen sombra. ¿Qué porcentaje es?", "10*100/40", "Se divide 10 entre 40 y se multiplica por 100."),
        ("¿Para qué sirve una meta?", "Para indicar el valor que se espera lograr", "Orienta la propuesta y permite saber si se cumplió."),
    ],
    op=("Usa la {F} Diseña una mini tabla de seguimiento con tres indicadores (uno de la encuesta, uno de temperatura y uno de árboles), su línea base, una meta y cómo medirías de nuevo. Escribe un límite de tus datos.",
        "Hogares sin sombra: base 70 %, meta 35 %, nueva encuesta anónima. Diferencia de temperatura: base 8 grados, meta 4, nueva medición a mediodía en las mismas plazas. Árboles plantados: base sin dato en el barrio (8 en toda la comuna en 5 años), meta 20 en el barrio, conteo con el municipio. Límite: la medición se hizo un solo día.",
        ["propone tres indicadores con línea base y meta", "indica cómo volver a medir", "declara un límite"], ["tabla de tres indicadores", "límite"], ["metas sin línea base", "indicadores que no se pueden medir"],
        "Pide a otra persona que revise si cada indicador se puede medir con el mismo método."),
    rx=("Explica con tus palabras por qué se necesita una línea base.", "Anota qué dato falta en tu entorno para entender un problema que te preocupe."),
)

# ============================================================ OA 07, clase 3
F = ("Ficha 3 (árbol de problemas y voces de ejemplo, El Roble). Efectos: personas mayores con mareos por calor; niñas y niños que no juegan al aire libre; comercio con menos clientes al mediodía. "
     "Causas: pocas áreas verdes, calles de asfalto que acumulan calor, y cambio climático con veranos más cálidos. "
     "Voces: una persona mayor: «Necesito un lugar con sombra donde sentarme»; el comercio: «No queremos que se quiten estacionamientos»; la escuela: «Podemos cuidar árboles pequeños»; el municipio: «Tenemos poco presupuesto».")
build(
    O7, 3, F,
    use="Aprenderé a comparar causas y perspectivas de un problema local, a ordenarlas en un árbol de problemas y a construir acuerdos entre actores que piensan distinto.",
    explain=[
        "El árbol de problemas es una herramienta para ordenar un problema: en el tronco se escribe el problema central; en las raíces, sus causas; y en las ramas, sus efectos. Sirve para ver que un problema tiene varias causas, de distintas escalas (locales y globales), y distintos efectos para distintos grupos. Una buena propuesta actúa sobre causas que se pueden modificar localmente o sobre efectos que se pueden reducir.",
        "Cada actor tiene una perspectiva: una forma de ver el problema según su situación, sus intereses y sus recursos. Comparar perspectivas no significa que todas valgan lo mismo: se pide razones y datos, y se buscan puntos en común. Los acuerdos se pueden construir por consenso (todos aceptan), por votación o por priorización con criterios (por ejemplo, quién se beneficia, costo y rapidez).",
        "Para un trabajo colaborativo sano se escucha sin interrumpir, se respetan los turnos, se distinguen las personas de las ideas y se registran los acuerdos. Si hay desacuerdo, se vuelve a los datos y a los criterios. Si hay conflictos personales o situaciones de riesgo, se informa a una persona adulta de confianza.",
    ],
    vocab=[("árbol de problemas", "esquema con el problema central, sus causas y sus efectos"), ("causa", "factor que contribuye a que el problema exista"), ("efecto", "consecuencia del problema"), ("consenso", "acuerdo aceptado por todas las personas"), ("priorización", "ordenar alternativas según criterios")],
    worked=[
        ("Clasificar causa y efecto", "En el barrio hay poca sombra y las personas mayores se marean por calor. ¿Cuál es causa y cuál efecto?", ["La poca sombra produce más calor.", "Los mareos son una consecuencia."], "Causa: poca sombra. Efecto: mareos"),
        ("Hallar un punto en común", "El comercio quiere conservar estacionamientos y la escuela quiere plantar árboles. ¿Qué punto en común puede haber?", ["Ambos quieren un barrio con vida.", "Se podría plantar árboles en lugares que no quiten estacionamientos."], "Plantar en espacios que no afecten los estacionamientos"),
    ],
    mistakes=[("Culpar a una sola causa o a un solo actor.", "El problema tiene varias causas y actores.", "Completa el árbol con causas locales y globales."),
              ("Decidir por votación sin escuchar las razones.", "Se pierde información y puede quedar un grupo muy afectado.", "Escucha razones y usa criterios antes de votar.")],
    T=[
        ("{F} ¿Cuál de estos es un efecto del problema?", "Mareos de personas mayores", "Calles de asfalto que acumulan calor", "Pocas áreas verdes en el barrio", "Los mareos son una consecuencia; las calles y las áreas verdes son causas."),
        ("{F} ¿Cuál de estas es una causa de escala global?", "El clima global, con veranos cada vez más cálidos en la región", "Las calles de asfalto del barrio de El Roble", "La falta de árboles en las plazas del barrio", "El clima global es la causa de mayor escala; las otras son locales."),
        ("{F} ¿Qué voz expresa una restricción de recursos?", "La del municipio, que tiene poco presupuesto", "La de la escuela, que ofrece cuidar árboles", "La de la persona mayor, que pide un lugar con sombra", "El municipio señala falta de presupuesto; la escuela ofrece apoyo y la persona mayor expresa una necesidad."),
        ("{F} ¿Qué actor ofrece un recurso concreto?", "La escuela, que puede cuidar árboles pequeños", "El comercio, que pide conservar los estacionamientos", "La persona mayor, que ofrece plantar los árboles ella sola", "La escuela ofrece cuidar árboles; el comercio expresa un interés y la persona mayor expresa una necesidad."),
        ("{F} ¿Qué interés tiene el comercio?", "Conservar los estacionamientos", "Quitar todas las plazas para tener más tiendas", "Eliminar los árboles pequeños de la calle", "El comercio dice que no quiere que se quiten estacionamientos."),
        ("{F} ¿Qué causa sobre la que el barrio sí puede actuar aparece en la ficha?", "Las pocas áreas verdes", "El cambio climático global", "El presupuesto nacional del municipio", "Se pueden plantar árboles en el barrio; el clima global y el presupuesto exceden su escala."),
        ("{F} La persona mayor y el comercio parecen oponerse. ¿Qué es lo más productivo?", "Buscar una propuesta que dé sombra y conserve los estacionamientos", "Elegir la voz que habla con más fuerza y dejar a la otra", "Eliminar la propuesta para que nadie se moleste", "Buscar soluciones que atiendan ambos intereses es la vía colaborativa; imponer o cancelar no resuelve."),
        ("{F} ¿Qué criterio ayuda a priorizar entre plantar árboles y poner toldos?", "Beneficiarios, costo y tiempo", "Cuál alternativa suena más moderna y llamativa", "Cuál fue propuesta primero en la reunión del curso", "Los criterios de beneficiarios, costo y tiempo permiten comparar; la moda o el orden de propuesta no."),
        ("Un equipo discute una propuesta. Una persona dice: «Eso es una tontería». ¿Qué conducta colaborativa corresponde?", "Criticar la idea con razones y datos concretos, sin atacar a las personas", "Seguir la discusión sin cambiar el tono del intercambio", "Expulsar a quien critica del equipo de trabajo", "Se distinguen las personas de las ideas y se pide razones; no se permite el ataque personal."),
        ("{F} ¿Por qué el árbol de problemas incluye causas y efectos?", "Porque muestra varias causas y efectos, y ayuda a escoger dónde actuar", "Porque obliga a elegir una única causa del problema", "Porque sirve para decidir quién tiene la culpa del problema", "Mostrar varias causas y efectos ayuda a escoger dónde intervenir; no busca una sola causa ni culpables."),
        ("{F} Un compañero afirma: «Si se plantan árboles, el calor del barrio desaparece». ¿Qué respuesta es más precisa?", "Bajan el calor local, pero no el cambio climático global", "Es exacto, porque los árboles eliminan todo el calor", "Es falso, porque los árboles no cambian la temperatura", "La sombra y la vegetación bajan la temperatura local; no resuelven la causa global."),
        ("Un integrante del equipo de ejemplo cuenta en privado que sufre burlas del grupo y teme asistir. ¿Qué paso corresponde?", "Avisar a una persona adulta de confianza", "Ignorarlo para no afectar el avance del proyecto", "Confrontar al grupo sin apoyo en una reunión del equipo", "Ante conductas de hostigamiento se avisa a una persona adulta de confianza; no se ignora ni se confronta solo."),
        ("{F} Elige la conclusión mejor formulada.", "Hay causas locales y globales; una propuesta puede dar sombra", "La culpa es del municipio, porque tiene poco presupuesto para el barrio", "El comercio es el principal obstáculo y debe ceder en todo", "Una conclusión situada integra causas y voces; culpar a un actor no ayuda a colaborar."),
    ],
    ctx=("En una reunión de ejemplo, el equipo debe escoger entre tres propuestas: plantar árboles, instalar toldos o abrir un patio de sombra en la escuela. Hay tres votos para la primera, dos para la segunda y uno para la tercera, pero varios no explicaron sus razones. ¿Qué es más adecuado?", "Pedir las razones de cada voto y comparar con criterios antes de decidir", "Aceptar la mayoría y cerrar la discusión de inmediato", "Votar otra vez hasta que gane la propuesta que más me gusta", "Escuchar razones y usar criterios mejora la decisión; la mayoría sola o repetir hasta ganar no lo hace."),
    sc=[
        ("En Mundo global: ¿qué es un árbol de problemas?", "Un esquema con el problema central, sus causas y sus efectos", "Ayuda a decidir en qué parte del problema actuar."),
        ("¿Qué es el consenso?", "Un acuerdo aceptado por todas las personas", "Se diferencia de la votación porque nadie queda en desacuerdo."),
        ("{F} ¿Qué voz representa a un grupo vulnerable?", "La persona mayor", "Las personas mayores son más afectadas por el calor extremo."),
    ],
    op=("Usa la {F} Dibuja un árbol de problemas con el problema central, tres causas (una global) y tres efectos. Luego elige dos voces con intereses distintos y propone un acuerdo que atienda a ambas, indicando qué cede cada una.",
        "Problema central: poca sombra en El Roble. Causas: pocas áreas verdes, asfalto, cambio climático. Efectos: mareos, niñez sin juego al aire libre, menos clientes. Voces: persona mayor y comercio. Acuerdo: plantar árboles en plazas, no en estacionamientos; el comercio conserva sus estacionamientos, la persona mayor acepta toldos temporales mientras crecen los árboles y la escuela los cuida.",
        ["incluye problema, tres causas y tres efectos", "identifica una causa global", "propone un acuerdo con cesiones", "usa un lenguaje respetuoso"], ["árbol de problemas", "acuerdo entre dos voces"], ["una sola causa", "acuerdo que ignora a una voz"],
        "Pide a otra persona que revise si tu acuerdo atiende a las dos voces."),
    rx=("Explica con tus palabras la diferencia entre causa y efecto en un árbol de problemas.", "Anota una regla que ayuda a que un equipo trabaje de forma respetuosa."),
)

# ============================================================ OA 07, clase 4
F = ("Ficha 4 (propuesta de ejemplo para El Roble). Objetivo: dar sombra a 2 de las 3 plazas antes del próximo verano. "
     "Actividades: A) plantar 20 árboles pequeños con apoyo del municipio; B) instalar 4 toldos temporales en los lugares más usados; C) taller de cuidado de árboles en la escuela. "
     "Presupuesto de ejemplo (en u.m.): árboles, 20 por 15 cada uno; toldos, 4 por 50 cada uno; taller, 30 en total. Fondos disponibles: 600. "
     "Riesgos: sequía que mate a los árboles; vandalismo; falta de riego.")
build(
    O7, 4, F,
    use="Aprenderé a explicar cómo una propuesta local se relaciona con sus resultados: objetivo, actividades, recursos, responsables, indicadores, riesgos y consecuencias, incluidas las no previstas.",
    explain=[
        "Una propuesta colaborativa bien diseñada tiene partes que se relacionan entre sí. El objetivo dice qué se quiere lograr. Las actividades son las acciones que llevan al objetivo. Los recursos son lo que se necesita (dinero, materiales, tiempo, personas). Los responsables son quienes se encargan de cada actividad. Los indicadores y las metas permiten saber si se avanza. El cronograma ordena las actividades en el tiempo.",
        "Explicar las relaciones significa mostrar cómo cada actividad contribuye al objetivo y qué consecuencias puede tener. Hay consecuencias previstas (más sombra) y no previstas (por ejemplo, necesidad de riego constante). Un riesgo es algo que puede salir mal y afectar el resultado; se prevé con medidas, como un plan de riego. La propuesta se revisa con evidencia después de ejecutarla: se compara con la línea base y se ajusta.",
        "Una propuesta local frente a un problema global no resuelve la causa mundial, pero puede reducir efectos, preparar a la comunidad y mostrar un camino. Se comunica de manera clara a quienes decidirán, con datos, costos, riesgos y la participación de la comunidad. Toda actividad escolar se hace con apoyo de personas adultas y con medidas de seguridad.",
    ],
    vocab=[("objetivo", "lo que se quiere lograr"), ("cronograma", "orden de las actividades en el tiempo"), ("riesgo", "algo que puede salir mal y afectar el resultado"), ("consecuencia no prevista", "efecto que no se había anticipado"), ("evaluación", "revisión de los resultados frente a la línea base y la meta")],
    worked=[
        ("Calcular un presupuesto", "Plantar 10 árboles a 12 u.m. cada uno. ¿Cuánto cuesta?", ["Multiplica la cantidad por el costo de cada uno: 10 por 12.", "El resultado es el costo total de la plantación."], "120 u.m."),
        ("Prever un riesgo", "Los árboles nuevos pueden morir por falta de agua en verano. ¿Qué medida lo previene?", ["Se organiza un turno de riego con la escuela y los vecinos.", "Se registra quién riega y cuándo."], "Un plan de riego con responsables"),
    ],
    mistakes=[("Diseñar actividades que no conducen al objetivo.", "Se gastan recursos sin avanzar en lo que se quiere lograr.", "Revisa que cada actividad aporte al objetivo."),
              ("No considerar los riesgos.", "Los resultados pueden perderse por problemas que se podían prever.", "Anota riesgos y una medida para cada uno.")],
    T=[
        ("=", "{F} ¿Cuántas u.m. cuestan los 20 árboles (20 por 15)?", "20*15", "Se multiplica la cantidad de árboles por el costo de cada uno."),
        ("=", "{F} ¿Cuántas u.m. cuestan los 4 toldos (4 por 50)?", "4*50", "Se multiplica la cantidad de toldos por el costo de cada uno."),
        ("=", "{F} ¿Cuánto cuesta en total la propuesta con las tres actividades (árboles, toldos y taller)?", "20*15+4*50+30", "Se suman 300 de árboles, 200 de toldos y 30 del taller."),
        ("=", "{F} ¿Cuántas u.m. de los fondos disponibles (600) sobrarían tras ejecutar todo?", "600-(20*15+4*50+30)", "Se resta el costo total a los fondos disponibles."),
        ("{F} ¿Qué actividad aporta una solución rápida mientras los árboles crecen?", "B, los toldos temporales, que dan sombra desde el primer día", "A, plantar 20 árboles pequeños", "C, el taller de cuidado de árboles", "Los toldos dan sombra de inmediato; los árboles pequeños tardan en crecer."),
        ("{F} ¿Qué relación tiene el taller C con el objetivo?", "Ayuda a que los árboles sobrevivan", "Reemplaza la necesidad de plantar árboles", "No tiene ninguna relación con la sombra del barrio", "El taller aporta cuidado, lo que protege el resultado; no reemplaza la plantación."),
        ("{F} ¿Cuál es un riesgo de la propuesta?", "Que la falta de riego en verano mate los árboles recién plantados", "Que haya demasiada sombra en las plazas del barrio", "Que los vecinos aprendan a cuidar árboles", "El riesgo es algo que puede salir mal; la falta de riego puede arruinar la plantación."),
        ("{F} ¿Qué medida reduce el riesgo de que los árboles mueran por falta de riego?", "Un turno de riego con responsables definidos y un registro de cuándo se riega", "Plantar solo la mitad de los árboles de la propuesta", "Esperar a que llueva para regar solo una vez al año", "Un plan de riego con responsables ataca la causa; reducir la cantidad o esperar no la garantiza."),
        ("{F} Una consecuencia no prevista podría ser:", "Que los vecinos pidan más riego del que se había programado en el plan", "Que los árboles den sombra, como se esperaba", "Que la propuesta cueste 530 u.m., como indica el presupuesto", "Lo no previsto es lo que no estaba en el plan; la sombra sí estaba prevista."),
        ("{F} Para decidir si la propuesta funcionó, ¿qué compararías?", "Los indicadores nuevos frente a la línea base", "La opinión del equipo sobre cuánto trabajó en el proyecto", "El número de reuniones que se hicieron durante el proyecto", "La evaluación compara resultados con la línea base y la meta; el esfuerzo no mide el efecto."),
        ("{F} Un compañero propone cambiar el objetivo a «eliminar el calor del planeta» para dar más importancia. ¿Qué problema tiene?", "Es inalcanzable desde el barrio y no se puede medir con datos locales", "Es muy pequeño y no se relaciona con el clima global", "Es una actividad del proyecto y no un objetivo", "Un objetivo debe ser alcanzable y medible a escala local."),
        ("{F} Elige la comunicación mejor formulada para el municipio.", "El objetivo, el costo de 530 u.m., los riesgos y los indicadores de avance", "Una petición de dinero para plantar árboles, sin más datos", "Una lista de quejas sobre el municipio, sin propuestas", "La comunicación efectiva muestra objetivo, costo, riesgos e indicadores; las otras no ofrecen información."),
        ("{F} Un vecino pregunta: «¿Esto detendrá el cambio climático?». ¿Cuál es la respuesta más honesta?", "No, pero reduce el calor local y prepara a la comunidad", "Sí, porque cada árbol elimina las emisiones del mundo", "No sirve de nada, porque el problema es global", "La propuesta tiene un alcance local; honestidad es reconocer qué logra y qué no."),
    ],
    ctx=("Un curso de ejemplo propone organizar una jornada de limpieza de un cauce de la comuna como parte de su proyecto de gestión del riesgo. El profesor sugiere cambiar la actividad. ¿Qué alternativa es más adecuada para la seguridad?", "Una campaña informativa y un mapa de riesgo hecho con adultos, sin entrar al cauce", "Entrar igual al cauce con guantes y botas, porque se limpia más rápido", "Eliminar el proyecto completo, porque ninguna actividad escolar es segura", "Una alternativa segura mantiene el aporte sin exponer a nadie; ni se arriesga ni se cancela todo."),
    sc=[
        ("En Mundo global: ¿qué es un riesgo en una propuesta?", "Algo que puede salir mal y afectar el resultado", "Se anticipa con una medida de prevención."),
        ("=", "Una propuesta de ejemplo compra 12 plantas a 8 u.m. cada una. ¿Cuánto cuesta?", "12*8", "Se multiplica la cantidad de plantas por el costo de cada una."),
        ("¿Para qué sirve el cronograma?", "Para ordenar las actividades en el tiempo", "Permite organizar quién hace qué y cuándo."),
    ],
    op=("Usa la {F} Completa una tabla de planificación con cuatro filas (una por actividad más una de evaluación): responsable, recurso, fecha, indicador y un riesgo con su medida. Después escribe en dos líneas una consecuencia prevista y una no prevista.",
        "A, plantar: responsable municipio y vecinos; recurso, 300 u.m.; fecha, otoño; indicador, 20 árboles vivos; riesgo, falta de riego, con turno de riego. B, toldos: responsable junta de vecinos; 200 u.m.; indicador, 4 toldos instalados; riesgo, vandalismo, con vigilancia de vecinos. C, taller: escuela; 30 u.m.; indicador, personas asistentes. Evaluación: nueva encuesta. Prevista: más sombra. No prevista: más demanda de riego.",
        ["completa responsable, recurso, fecha, indicador y riesgo", "los costos coinciden con la ficha", "distingue consecuencia prevista y no prevista"], ["tabla de cuatro filas", "dos líneas de consecuencias"], ["actividades sin indicador", "no considerar riesgos"],
        "Pide a otra persona que revise si el presupuesto coincide con las cifras de la ficha."),
    rx=("Explica con tus palabras por qué una propuesta necesita indicadores y riesgos.", "Anota una propuesta local posible para un problema de tu barrio y cómo la evaluarías."),
)
