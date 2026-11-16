"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 07 clases 2 a 4 (diagnóstico con fuentes e indicadores, causas y perspectivas con acuerdos, diseño de la propuesta con sus relaciones y consecuencias). Casos y datos de ejemplo inventados."""
from __future__ import annotations

from fg_chla_common import build

O7 = "FG-CHLA-3y4-OAC-07"

# ============================================================ OA 07, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados; barrio ficticio Villa Esperanza). El equipo del liceo hizo una encuesta breve y anónima a 60 personas del barrio, todas a la salida del liceo. "
     "Resultados: 45 dicen que la plaza está sucia; 30 dicen que no la usan porque tiene poca luz; 18 participarían en una actividad comunitaria. "
     "Conteo de personas en la plaza (observación en grupo, de día, con aviso al liceo): 5 en la mañana, 12 a mediodía y 3 en la tarde. "
     "Dato de la municipalidad: la basura de la plaza se retira 2 veces por semana. Una pregunta de la encuesta fue: «¿No cree que es vergonzoso lo sucia que está la plaza?».")
build(
    O7, 2, F,
    use="Aprenderé a hacer un diagnóstico local con fuentes e indicadores sencillos, revisando su calidad y sus límites antes de proponer.",
    explain=[
        'Un diagnóstico es el conocimiento del problema antes de proponer una solución. Se puede construir con varias fuentes: la observación en terreno (por ejemplo, contar cuántas personas usan un lugar a distintas horas, siempre en grupo, de día y con aviso a una persona adulta), encuestas breves, entrevistas con consentimiento, y datos de instituciones como la municipalidad. Los indicadores sencillos son porcentajes y conteos: un porcentaje se calcula dividiendo la parte por el total y multiplicando por 100.',
        'Las fuentes se interrogan: ¿a quiénes se preguntó?, ¿cómo se preguntó?, ¿qué falta? Una muestra muy pequeña o tomada en un solo lugar puede no representar a todo el barrio (sesgo de muestra). Una pregunta que sugiere la respuesta, como «¿no cree que es vergonzoso…?», es una pregunta inductiva y distorsiona los resultados. También se cuida la privacidad: las encuestas pueden ser anónimas y no se anotan nombres ni datos personales. Y si una persona cuenta que está en riesgo o sufre violencia, se le sugiere hablar con una persona adulta de confianza.',
    ],
    vocab=[("diagnóstico", "conocimiento del problema antes de proponer una solución"), ("muestra", "grupo de personas a quienes se pregunta"), ("sesgo", "distorsión que hace que los resultados no representen bien a todos"), ("pregunta inductiva", "pregunta que sugiere la respuesta"), ("anónimo", "sin nombre ni datos que identifiquen a la persona")],
    worked=[
        ("Calcular un porcentaje", "En una encuesta de ejemplo a 40 personas, 10 dicen que usan la plaza. ¿Qué porcentaje es?", ["Se divide 10 por 40.", "Se multiplica por 100."], "25 %"),
        ("Detectar una pregunta inductiva", "Una pregunta de ejemplo dice: «¿No le parece horrible que no haya luz?». ¿Qué problema tiene?", ["Sugiere cuál debe ser la respuesta.", "Una versión neutral es: ¿cómo evalúa la iluminación de la plaza?"], "Es inductiva; conviene una versión neutral"),
    ],
    mistakes=[("Encuestar solo a personas de un mismo lugar y generalizar al barrio completo.", "La muestra puede no representar a todas las personas.", "Busca distintos lugares y grupos de edad, o declara el límite."),
              ("Escribir preguntas que sugieren la respuesta.", "Los resultados quedan distorsionados.", "Redacta preguntas neutrales y prueba con una persona antes.")],
    T=[
        ('¿Qué es un diagnóstico?', 'Conocer bien el problema antes de proponer una solución', 'La solución que el equipo propone a la municipalidad', 'La evaluación final de todo el trabajo del equipo', 'El diagnóstico viene antes de proponer; no es la solución ni la evaluación final.'),
        ('¿Qué es una pregunta inductiva?', 'Una pregunta que sugiere cuál debe ser la respuesta', 'Una pregunta que se responde con números exactos', 'Una pregunta que se hace dos veces a la misma persona', 'Induce porque orienta la respuesta.'),
        ('¿Qué significa que una encuesta sea anónima?', 'Que no se anotan nombres ni datos personales de quien responde', 'Que solo responden personas que no viven en el barrio', 'Que las respuestas se publican con nombre', 'Anónimo protege la privacidad de quien responde.'),
        ('=', '{F} ¿Qué porcentaje de las 60 personas dice que la plaza está sucia?', '45*100//60', 'Se divide quienes lo dicen por el total y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje de las 60 personas no usa la plaza por la poca luz?', '30*100//60', 'Se divide quienes lo dicen por el total y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje de las 60 personas participaría en una actividad comunitaria?', '18*100//60', 'Se divide quienes lo dicen por el total y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Cuántas personas se contaron en total en la plaza en los tres momentos?', '5+12+3', 'Se suman los tres conteos.', ' personas'),
        ('{F} ¿Qué limitación tiene la muestra de la encuesta?', 'Se encuestó solo a la salida del liceo, en un único lugar', 'Se encuestó a demasiadas personas para un barrio pequeño', 'Se preguntó solo a quienes no viven cerca de la plaza', 'La ficha dice que fue a la salida del liceo, por lo que puede no representar a todo el barrio.'),
        ('{F} ¿Qué problema tiene la pregunta «¿No cree que es vergonzoso lo sucia que está la plaza?»?', 'Es inductiva: sugiere la respuesta', 'Es neutral: no orienta la respuesta', 'Es anónima: no pide el nombre', 'La frase orienta hacia el «sí»; una versión neutral es ¿cómo evalúa el aseo de la plaza?'),
        ('{F} Un integrante afirma: «El 75 % de todo el barrio dice que la plaza está sucia». ¿Qué corrección corresponde?', 'Es el 75 % de las 60 personas encuestadas, no de todo el barrio', 'Es correcto, porque la encuesta cubrió todo el barrio', 'Es incorrecto, porque el porcentaje real es 45 %', 'Se puede afirmar para la muestra; para el barrio se necesita una muestra más representativa.'),
        ('{F} Con el dato de que la basura se retira 2 veces por semana, ¿qué hipótesis se puede plantear?', 'Tal vez falten contenedores o más frecuencia de retiro', 'Que la municipalidad no retira nunca la basura de la plaza', 'Que las personas del barrio no generan nada de basura', 'Es una hipótesis que se debe comprobar; el dato muestra una frecuencia, no la causa.'),
        ('{F} Para mejorar el diagnóstico, ¿qué conviene hacer?', 'Encuestar a varios lugares y edades con preguntas neutrales', 'Repetir la encuesta a la salida del liceo con una mayor cantidad de preguntas', 'Agregar preguntas que sugieran a las personas qué deben responder en cada caso', 'Ampliar la muestra y neutralizar las preguntas mejora la calidad.'),
        ('{F} Durante una entrevista, una persona cuenta que sufre violencia en su casa. ¿Qué corresponde hacer?', 'Escucharla y sugerirle hablar con una persona adulta de confianza', 'Anotar su nombre y publicar su caso en el informe final del equipo escolar', 'Prometerle guardar el secreto y no contarlo a nadie más del liceo o del barrio', 'No se guarda un secreto de riesgo: se orienta a hablar con una persona adulta de confianza.'),
    ],
    ctx=('Un equipo de ejemplo encuesta a 50 personas y 35 dicen que no usan una cancha por falta de luz. ¿Qué porcentaje es y qué advertencia corresponde?', '70 %; vale para las 50 personas encuestadas, no para todo el barrio', '35 %; vale para todo el barrio sin necesidad de agregar ninguna advertencia', '85 %; vale para toda la comuna sin necesidad de agregar ninguna advertencia más', 'Se calcula 35 ÷ 50 × 100 = 70; el resultado describe a la muestra.'),
    sc=[
        ('Nombra dos fuentes que puede usar un equipo escolar para un diagnóstico local.', 'Por ejemplo, observación en grupo y una encuesta anónima', 'También sirven entrevistas con consentimiento y datos de la municipalidad.'),
        ('=', 'En una encuesta de ejemplo a 80 personas, 20 dicen que usan la plaza. ¿Qué porcentaje es?', '20*100//80', 'Se divide por el total y se multiplica por 100.', ' %'),
        ('¿Por qué las encuestas deben ser anónimas?', 'Para proteger la privacidad de las personas', 'No se necesitan nombres para describir al barrio.'),
    ],
    op=("Usa la {F} Escribe un diagnóstico de seis líneas: tres porcentajes de la encuesta, el conteo en la plaza, un límite de la muestra, una pregunta que corregirías (en versión neutral) y qué fuente nueva sumarías.",
        "El 75 % de las 60 personas dice que la plaza está sucia, el 50 % no la usa por la poca luz y el 30 % participaría en una actividad. En la observación se contaron 20 personas en total, con solo 3 en la tarde. La muestra se tomó en un solo lugar, a la salida del liceo. La pregunta «¿No cree que es vergonzoso…?» sería «¿Cómo evalúa el aseo de la plaza?». Sumaría una entrevista con la junta de vecinos, con consentimiento.",
        ["calcula los porcentajes", "reconoce un límite de la muestra", "corrige una pregunta inductiva"], ["diagnóstico de seis líneas"], ["generalizar a todo el barrio", "no corregir la pregunta"],
        "Pregunta si tu diagnóstico permite saber cuál es la causa del problema."),
    rx=("Redacta tres preguntas neutrales para una encuesta sobre un problema de tu barrio.", "Pide a una persona adulta de tu casa que responda tu encuesta en forma anónima y anota si alguna pregunta le pareció confusa."),
)

# ============================================================ OA 07, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado; Villa Esperanza). El equipo conversó con cuatro actores sobre la plaza. "
     "Junta de vecinos: faltan contenedores y actividades para que las familias se junten. Comerciante de la esquina: la basura atrae plagas y espanta a los clientes; ofrece ayudar con letreros. "
     "Adulto mayor: no sale en la tarde porque hay poca luz y teme caerse. Joven de una familia llegada hace poco: le gustaría un lugar para reunirse con otras personas del barrio, pero se siente poco invitado a las actividades. "
     "El equipo hizo una votación para elegir qué problema priorizar: poca luz, 5 votos; basura, 8 votos; falta de actividades de encuentro, 7 votos.")
build(
    O7, 3, F,
    use="Aprenderé a comparar causas y perspectivas de distintos actores locales, a priorizar un problema con criterios y a tomar acuerdos de forma colaborativa.",
    explain=[
        'Un problema local tiene varias causas. Una herramienta útil es el árbol de problemas: en el tronco se escribe el problema, en las raíces sus causas y en las ramas sus consecuencias. Para hallar causas, se pregunta «¿por qué?» varias veces y se revisan los datos. Las causas pueden ser de infraestructura (pocos contenedores, poca luz), de organización (falta de coordinación entre vecinos y municipalidad) y de convivencia (por ejemplo, que ciertas personas se sientan poco invitadas).',
        'Cada actor ve el problema desde su lugar: la junta de vecinos, los comerciantes, las personas mayores, los jóvenes, las familias que llegaron hace poco. Escuchar sus perspectivas permite proponer algo que responda a necesidades reales. Para priorizar un problema se usan criterios (importancia, urgencia, factibilidad, impacto en más personas) y una forma clara de decidir, como una votación o un consenso. Un acuerdo colaborativo se logra escuchando sin interrumpir, resumiendo lo que dijo el otro y buscando soluciones que beneficien a más de un actor.',
    ],
    vocab=[("árbol de problemas", "esquema con el problema, sus causas y sus consecuencias"), ("priorizar", "elegir qué atender primero según criterios"), ("consenso", "acuerdo al que se llega conversando hasta que todas las personas lo aceptan"), ("votación", "forma de decidir contando los votos de cada alternativa"), ("convivencia", "forma en que las personas viven y se relacionan en un lugar")],
    worked=[
        ("Armar un árbol", "Problema de ejemplo: una cancha está vacía. Causas: poca luz y falta de equipos. Consecuencia: los jóvenes no tienen dónde reunirse. ¿Qué va en las raíces?", ["Las raíces son las causas.", "Poca luz y falta de equipos."], "Raíces: poca luz y falta de equipos"),
        ("Contar votos", "En una votación de ejemplo, A tiene 6 votos, B tiene 4 y C tiene 5. ¿Cuántos votos hubo?", ["Se suman los votos.", "6 + 4 + 5."], "15 votos"),
    ],
    mistakes=[("Elegir el problema que más le gusta a quien coordina.", "Priorizar requiere criterios y una forma de decidir acordada.", "Define criterios antes de votar y registra el resultado."),
              ("Tomar solo la voz de los actores más fuertes.", "Se pierden necesidades de personas con menos voz.", "Busca activamente la perspectiva de quienes participan menos.")],
    T=[
        ('¿Qué es un árbol de problemas?', 'Un esquema que ordena el problema, sus causas y sus consecuencias', 'Un listado de los árboles que hay en una plaza', 'Un plan de trabajo con fechas y responsables', 'El árbol de problemas organiza causas y consecuencias.'),
        ('¿Qué significa priorizar?', 'Elegir qué atender primero según criterios', 'Resolver todos los problemas al mismo tiempo', 'Dejar que cada persona haga lo que quiera', 'Priorizar es ordenar según importancia, urgencia u otros criterios.'),
        ('¿Qué es un consenso?', 'Un acuerdo al que todas las personas llegan conversando', 'Una votación en que gana la opción con más votos', 'Una decisión tomada solo por quien coordina', 'El consenso busca acuerdo amplio; la votación cuenta votos.'),
        ('=', '{F} ¿Cuántos votos hubo en total?', '5+8+7', 'Se suman los votos de las tres alternativas.', ' votos'),
        ('{F} ¿Qué problema obtuvo más votos?', 'La basura', 'La poca luz', 'La falta de actividades de encuentro', 'La basura obtuvo 8 votos, más que los otros.'),
        ('=', '{F} ¿Cuántos votos más tuvo la basura que la poca luz?', '8-5', 'Se resta los votos de la poca luz a los de la basura.', ' votos'),
        ('{F} ¿Qué causa de infraestructura señala la Junta de vecinos?', 'La falta de contenedores', 'La falta de comerciantes', 'La falta de personas mayores', 'La Junta menciona contenedores y actividades.'),
        ('{F} ¿Qué consecuencia señala el comerciante?', 'La basura atrae plagas y aleja a los clientes', 'La poca luz hace caer a las personas mayores', 'La falta de actividades aumenta las burlas', 'El comerciante habla de plagas y clientes.'),
        ('{F} ¿Qué perspectiva aporta el adulto mayor?', 'Que la poca luz lo inseguriza en la tarde', 'Que la plaza debería tener más tiendas', 'Que no hace falta cambiar nada', 'Sale poco en la tarde por la poca luz.'),
        ('{F} ¿Qué aspecto de convivencia aparece en la voz del joven?', 'Sentirse poco invitado a las actividades', 'Que hay actividades todos los días', 'Que no vive nadie nuevo en el barrio', 'Habla de sentirse poco invitado.'),
        ('{F} Un integrante dice: «Como la basura ganó la votación, la poca luz y la convivencia no importan». ¿Qué respuesta es más adecuada?', 'La votación prioriza, pero los otros problemas siguen existiendo', 'Tiene razón, porque lo que no gana la votación deja de existir en el barrio', 'Hay que repetir la votación varias veces hasta que gane la poca luz', 'Priorizar no elimina los otros problemas; algunos pueden combinarse con la propuesta.'),
        ('{F} ¿Cómo podría una propuesta responder a más de un actor a la vez?', 'Con contenedores y una jornada abierta a todas las familias', 'Con contenedores colocados solo cerca de los comercios', 'Con una actividad abierta solo para los vecinos antiguos', 'Una jornada que invite a todos atiende la basura, la convivencia y la participación.'),
        ('{F} Dos integrantes discrepan sobre cuál es la causa principal de la basura. ¿Qué paso colaborativo es el mejor?', 'Revisar datos y escuchar a ambos antes de decidir', 'Decidir según quién tenga más años de experiencia en el equipo', 'Ignorar el tema y pasar sin discutir al siguiente punto de la reunión', 'Los desacuerdos se resuelven con datos, escucha y síntesis.'),
    ],
    ctx=('Un equipo de ejemplo escucha que los comerciantes quieren más letreros, los adultos mayores más luz y los jóvenes más actividades. ¿Qué es lo más colaborativo?', 'Buscar una propuesta que combine las necesidades', 'Elegir solo la necesidad del actor más influyente del barrio', 'Descartar las necesidades que tengan menos votos en la reunión', 'Una propuesta integrada reconoce a más actores.'),
    sc=[
        ('¿Qué se escribe en las raíces de un árbol de problemas?', 'Las causas', 'Las raíces muestran por qué ocurre el problema.'),
        ('Nombra un criterio para priorizar un problema local.', 'Por ejemplo, la urgencia o a cuántas personas afecta', 'También sirven la importancia y la factibilidad.'),
        ('¿Por qué conviene resumir lo que dijo otra persona antes de responder?', 'Para asegurar que se entendió y mostrar respeto', 'El resumen ayuda a evitar malentendidos.'),
    ],
    op=("Usa la {F} Dibuja en texto un árbol de problemas: el problema en el tronco, tres causas en las raíces (una de infraestructura, una de organización y una de convivencia) y dos consecuencias en las ramas. Luego escribe una oración que indique qué actor aportó cada causa.",
        "Tronco: la plaza está sucia, poco iluminada y con pocas actividades. Raíces: faltan contenedores (infraestructura; Junta de vecinos), poca coordinación entre vecinos y municipalidad (organización), algunas personas se sienten poco invitadas (convivencia; joven). Ramas: plagas y menos clientes (comerciante); personas mayores no salen en la tarde (adulto mayor).",
        ["ubica causas en las raíces", "ubica consecuencias en las ramas", "atribuye cada aporte a un actor"], ["árbol de problemas en texto", "una oración"], ["mezclar causas y consecuencias", "no atribuir aportes"],
        "Revisa que cada causa se sostenga con un dato o con la voz de un actor."),
    rx=("Haz un árbol de problemas de un tema de tu liceo con una causa y una consecuencia.", "Conversa con alguien de tu casa sobre qué haría para que más vecinos participen en una actividad del barrio."),
)

# ============================================================ OA 07, clase 4
F = ("Ficha 4 (propuesta de ejemplo, inventada; Villa Esperanza). Objetivo: durante el primer semestre, reducir la basura de la plaza y aumentar el uso de la plaza por parte de familias de distintos orígenes. "
     "Actividades: (1) instalar 4 contenedores, con permiso de la municipalidad, a $20.000 cada uno; (2) hacer 3 letreros de cuidado de la plaza con la ayuda del comerciante, a $5.000 cada uno; "
     "(3) organizar una jornada de limpieza y de encuentro, con guantes y bolsas, bajo supervisión de adultos, con materiales por $10.000; (4) pedir a la municipalidad una revisión del alumbrado. "
     "Línea base: antes se juntaban 12 bolsas de basura en la plaza cada semana; la meta es 4 bolsas. Riesgos: que no haya permiso; que pocas personas asistan.")
build(
    O7, 4, F,
    use="Aprenderé a explicar las relaciones entre actividades, resultados y consecuencias de una propuesta local, a calcular su presupuesto, a definir indicadores y a prever riesgos.",
    explain=[
        'Una propuesta local necesita un objetivo claro, actividades concretas, responsables, un cronograma y un presupuesto. Cada actividad debe estar vinculada con una causa del problema: si la causa es la falta de contenedores, una actividad es instalarlos. Esta relación entre causa, actividad y resultado se llama lógica de la propuesta. Un presupuesto suma el costo de cada actividad: cantidad por precio unitario, y luego el total.',
        'Para saber si funcionó se definen indicadores, que son datos comparables antes y después, como las bolsas de basura por semana o el número de personas que asisten a una actividad. Una línea base es el valor antes de comenzar y una meta es el valor que se espera lograr. También se prevén riesgos, es decir, hechos que pueden dificultar el plan, y se piensa cómo reducirlos. Las actividades deben ser seguras (sin alturas ni herramientas peligrosas, con supervisión de personas adultas) y respetuosas de todos los actores. La propuesta se presenta a los actores que pueden decidir o apoyar.',
    ],
    vocab=[("objetivo", "lo que se quiere lograr con la propuesta"), ("presupuesto", "suma de los costos de las actividades"), ("indicador", "dato comparable antes y después para evaluar un resultado"), ("línea base", "valor del indicador antes de comenzar"), ("meta", "valor que se espera lograr"), ("riesgo", "hecho que puede dificultar el plan")],
    worked=[
        ("Calcular un costo", "Una actividad de ejemplo requiere 5 carteles a $2.000 cada uno. ¿Cuánto cuesta?", ["Se multiplica la cantidad por el precio.", "5 × $2.000."], "$10.000"),
        ("Medir un resultado", "Una propuesta de ejemplo baja la basura de 10 a 4 bolsas por semana. ¿Cuánto se redujo?", ["Se resta: 10 − 4.", "El resultado es 6 bolsas."], "6 bolsas"),
    ],
    mistakes=[("Proponer actividades que no se relacionan con ninguna causa.", "No resuelven el problema.", "Vincula cada actividad con una causa del árbol de problemas."),
              ("Evaluar sin una línea base.", "No se puede comparar el antes y el después.", "Mide el indicador antes de comenzar.")],
    T=[
        ('¿Qué es una línea base?', 'El valor del indicador antes de comenzar', 'La meta que se espera lograr al final', 'El nombre del primer actor que apoya la propuesta', 'Es el punto de partida para comparar.'),
        ('¿Para qué sirve un indicador en una propuesta local?', 'Para comparar un dato antes y después del trabajo y medir el cambio', 'Para dar la opinión del equipo sobre si fue un éxito', 'Para listar todas las actividades que se realizaron', 'Los indicadores permiten medir cambios.'),
        ('¿Qué es un riesgo en una propuesta?', 'Un hecho que puede dificultar que el plan se cumpla', 'Un beneficio seguro que traerá la propuesta', 'Una actividad que el equipo ya terminó', 'El riesgo es algo que podría salir mal.'),
        ('=', '{F} ¿Cuánto cuestan los 4 contenedores?', '4*20000', 'Se multiplica la cantidad por el precio de cada uno.', ' pesos'),
        ('=', '{F} ¿Cuánto cuestan los 3 letreros?', '3*5000', 'Se multiplica la cantidad por el precio de cada uno.', ' pesos'),
        ('=', '{F} ¿Cuál es el costo total de las actividades (1), (2) y (3)?', '4*20000+3*5000+10000', 'Se suman los tres costos: contenedores, letreros y materiales.', ' pesos'),
        ('=', '{F} ¿Cuántas bolsas por semana se espera reducir según la meta?', '12-4', 'Se resta la meta a la línea base.', ' bolsas'),
        ('{F} ¿Qué actividad se vincula con la causa «faltan contenedores»?', 'La actividad (1), instalar contenedores', 'La actividad (2), hacer los letreros', 'La actividad (4), pedir la revisión del alumbrado', 'Los contenedores responden directamente a esa causa.'),
        ('{F} ¿Qué actividad atiende el aspecto de convivencia?', 'La actividad (3), la jornada de encuentro', 'La actividad (1), instalar contenedores', 'La actividad (4), pedir la revisión del alumbrado', 'Una jornada de encuentro invita a las familias a conocerse.'),
        ('{F} Si al terminar el semestre se juntan 6 bolsas por semana, ¿qué se puede decir?', 'Mejoró de 12 a 6, pero no alcanzó la meta de 4', 'Se alcanzó la meta, porque 6 es menor que 12', 'Empeoró, porque 6 es mayor que la meta de 4', 'Pasó de 12 a 6, una mejora, pero la meta era 4.'),
        ('{F} ¿Qué riesgo de la ficha se puede reducir con una gestión anticipada?', 'Falta de permiso: pedirlo antes a la municipalidad', 'Que llueva más de lo esperado', 'Que suban los precios del transporte', 'Solicitar el permiso con anticipación reduce ese riesgo.'),
        ('{F} Para que asistan más personas a la jornada, ¿qué conviene hacer?', 'Invitar directamente a las familias y a la junta de vecinos', 'Anunciar la actividad solo entre los estudiantes del curso y sus amigos', 'Anunciarla solo por las redes sociales del liceo, sin invitar a vecinos', 'La invitación abierta aumenta la participación y la convivencia.'),
        ('{F} Un integrante propone subir a postes para instalar focos. ¿Qué corresponde?', 'Descartarlo por seguridad y pedir la revisión a la municipalidad', 'Hacerlo en la tarde con una escalera que preste un vecino del barrio', 'Hacerlo sin avisar a ningún adulto para ganar tiempo en el semestre', 'Las actividades en altura son riesgosas; el alumbrado lo revisa la municipalidad.'),
    ],
    ctx=('Un equipo de ejemplo calcula: 2 contenedores a $20.000 y 2 letreros a $5.000. ¿Cuál es el total?', '$50.000', '$40.000', '$25.000', 'Se calcula 2 × 20.000 + 2 × 5.000 = 40.000 + 10.000.'),
    sc=[
        ('En Chile y la región, ¿por qué cada actividad debe vincularse con una causa del problema?', 'Porque así la propuesta ataca el origen y no solo el síntoma', 'La lógica de la propuesta une causa, actividad y resultado.'),
        ('=', 'Un equipo de ejemplo compra 3 carteles a $5.000 cada uno. ¿Cuánto gasta?', '3*5000', 'Se multiplica la cantidad por el precio.', ' pesos'),
        ('¿Para qué sirve definir una meta?', 'Para saber qué valor se espera lograr y evaluar el resultado', 'Sin meta no se puede decir si la propuesta funcionó.'),
    ],
    op=("Usa la {F} Escribe un resumen de la propuesta de seis líneas: objetivo, dos actividades con la causa que atacan, presupuesto total de esas dos actividades, indicador con línea base y meta, un riesgo y cómo lo reducirías. No agregues actividades peligrosas.",
        "Objetivo: reducir la basura y aumentar el uso de la plaza. Actividad 1: instalar 4 contenedores, que atacan la falta de contenedores ($80.000). Actividad 3: jornada de limpieza y encuentro, que ataca la convivencia ($10.000). Presupuesto de ambas: $90.000. Indicador: bolsas por semana, de 12 a una meta de 4. Riesgo: falta de permiso; lo reduciría solicitándolo con anticipación a la municipalidad.",
        ["vincula actividades y causas", "calcula el presupuesto", "define indicador, línea base y meta"], ["resumen de seis líneas"], ["actividades sin relación con causas", "no definir línea base"],
        "Pregunta quién evaluaría el resultado y con qué dato."),
    rx=("Calcula el presupuesto de una actividad inventada con tres materiales.", "Presenta tu propuesta a una persona adulta de confianza del liceo y anota una pregunta que te haya hecho."),
)
