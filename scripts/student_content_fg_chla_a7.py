"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 04 clases 4 a 6 (pueblos indígenas: relaciones y consecuencias, evaluación de alternativas, conclusión situada). Casos y datos de ejemplo inventados; la cultura de cada pueblo se remite al educador/a tradicional."""
from __future__ import annotations

from fg_chla_common import build

O4 = "FG-CHLA-3y4-OAC-04"

# ============================================================ OA 04, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado; no representa a ningún pueblo real). Una empresa ficticia propone sacar agua de un río para riego cerca del territorio de la comunidad de Lomas Verdes. "
     "Situación 1: el Estado organiza una consulta previa; la comunidad recibe información, propone cambios y se acuerdan controles de la calidad del agua. "
     "Situación 2 (otro caso de ejemplo): no hay consulta, la comunidad se entera por la prensa, pierde la confianza y presenta un reclamo ante un tribunal. "
     "Aparte: en la escuela de Lomas Verdes, al contratar a un educador tradicional, los estudiantes que participan en el taller de lengua pasaron de 10 a 40.")
build(
    O4, 4, F,
    use="Aprenderé a explicar relaciones y consecuencias entre territorio, consulta previa, lengua, educación y participación en la vida de los pueblos indígenas y su relación con los Estados.",
    explain=[
        'Los procesos que afectan a los pueblos indígenas se conectan entre sí. El territorio no es solo un lugar físico: puede ser clave para la economía, la identidad y las prácticas de una comunidad. Por eso, los proyectos que cambian un territorio pueden tener consecuencias económicas, ambientales y culturales. La consulta previa busca que la comunidad sea informada y escuchada antes de la decisión; cuando se hace bien, suele aumentar la información y la confianza, aunque no garantiza que todos queden de acuerdo.',
        'La lengua también se relaciona con otros procesos. Si la escuela solo enseña en una lengua, puede disminuir la transmisión entre generaciones; si incluye a educadores tradicionales y participa la comunidad, puede aumentar el uso de la lengua. La discriminación y las desigualdades de ingreso o de acceso a servicios influyen en las oportunidades. Al explicar, hay que decir qué es un hecho comprobado y qué es una hipótesis, y no atribuir una causa única a procesos que tienen muchas.',
    ],
    vocab=[("consecuencia", "efecto que resulta de un hecho o decisión"), ("hipótesis", "explicación posible que todavía debe comprobarse"), ("confianza", "creencia en que otra persona o institución actuará de forma justa"), ("transmisión de la lengua", "paso de la lengua de una generación a la siguiente"), ("reclamo", "petición formal para que se revise una decisión")],
    worked=[
        ("Explicar una consecuencia", "En un caso de ejemplo, una comunidad es informada y consultada antes de un proyecto. ¿Qué consecuencia es probable?", ["La comunidad recibe información y propone cambios.", "Eso suele aumentar la confianza, aunque no asegura acuerdo total."], "Más información y confianza"),
        ("Distinguir hecho e hipótesis", "En un caso de ejemplo, el taller de lengua pasó de 10 a 40 estudiantes tras contratar a un educador tradicional. ¿Qué es hecho y qué es hipótesis?", ["El aumento es un dato: es hecho.", "Que el educador sea la causa es una hipótesis que debe comprobarse."], "Hecho: el aumento. Hipótesis: la causa"),
    ],
    mistakes=[("Afirmar que la consulta previa garantiza que todos queden de acuerdo.", "Informa y abre diálogo, pero no asegura un acuerdo.", "Habla de «probable» o «puede» al explicar consecuencias."),
              ("Atribuir una sola causa a un cambio en el uso de la lengua.", "Intervienen escuela, familia, migración y discriminación.", "Enumera varios factores y busca evidencia para cada uno.")],
    T=[
        ('¿Qué busca la consulta previa?', 'Que la comunidad sea informada y escuchada antes de decidir', 'Que la comunidad apruebe siempre el proyecto de la empresa', 'Que la comunidad participe solo después de que empiece la obra', 'La consulta es previa a la decisión y busca información y diálogo; no es una aprobación obligatoria.'),
        ('¿Qué es una hipótesis?', 'Una explicación posible que todavía debe comprobarse con datos', 'Un dato ya comprobado por una institución del Estado', 'Una opinión que no necesita evidencia', 'La hipótesis se plantea y luego se somete a prueba con datos.'),
        ('¿Qué significa «transmisión de la lengua»?', 'El paso de la lengua de una generación a la siguiente', 'La traducción de un texto escrito a otro idioma', 'El envío de mensajes por medios de comunicación masiva', 'Transmitir la lengua es enseñarla y usarla entre generaciones.'),
        ('=', '{F} ¿Cuántos estudiantes más participan hoy en el taller de lengua que antes?', '40-10', 'Se resta el número inicial al actual.', ' estudiantes'),
        ('=', '{F} ¿Cuántas veces mayor es hoy la cantidad de estudiantes del taller que antes?', '40//10', 'Se divide el número actual por el inicial.', ' veces'),
        ('{F} En la Situación 1, ¿qué ocurre antes de decidir el proyecto?', 'La comunidad recibe información y propone cambios', 'La comunidad se entera por la prensa', 'La comunidad presenta un reclamo ante un tribunal', 'La ficha describe la información y la propuesta de cambios como parte de la consulta.'),
        ('{F} En la Situación 2, ¿cómo se entera la comunidad del proyecto?', 'Por la prensa, sin aviso previo', 'Por una consulta previa del Estado', 'Por una carta de la empresa', 'La ficha dice que la comunidad se entera por la prensa.'),
        ('{F} ¿Qué diferencia hay entre las dos situaciones en cuanto a confianza?', 'En la 1 se acuerdan controles; en la 2 se pierde la confianza', 'En la 1 se pierde la confianza; en la 2 se acuerdan controles', 'En ambas situaciones se acuerdan controles de la calidad del agua', 'La Situación 1 incluye acuerdos y la Situación 2 pérdida de confianza y reclamo.'),
        ('{F} Un estudiante escribe: «La consulta previa asegura que todos estén de acuerdo». ¿Qué corrección corresponde?', 'Puede aumentar la confianza, pero no asegura el acuerdo de todos', 'Tiene razón, porque una consulta siempre termina en acuerdo', 'La consulta no tiene efecto sobre la información', 'La consulta abre diálogo y puede mejorar las decisiones, pero no garantiza unanimidad.'),
        ('{F} El taller de lengua pasó de 10 a 40 estudiantes. ¿Qué afirmación es una hipótesis y no un hecho?', 'El aumento se debe a la contratación del educador tradicional', 'El taller tiene 40 estudiantes ahora, según la ficha', 'Antes del educador el taller tenía 10 estudiantes', 'Los números son datos; atribuir la causa al educador requiere comprobarlo con más evidencia.'),
        ('{F} ¿Qué dato adicional ayudaría a comprobar esa hipótesis?', 'Testimonios de estudiantes sobre por qué se inscribieron', 'La cantidad total de ciudades que hay en la región completa', 'El nombre de la empresa que planea el proyecto de riego', 'Preguntar a quienes participan ayuda a ver las razones; los otros datos no se relacionan.'),
        ('{F} Si el Estado ignora las propuestas de la comunidad en la consulta, ¿qué consecuencia es posible?', 'Que baje la confianza y aumenten los reclamos de la comunidad', 'Que el proyecto se vuelva siempre más rápido y barato', 'Que la comunidad deje de tener interés en su territorio', 'Una consulta solo formal puede producir desconfianza y reclamos.'),
        ('{F} En la Situación 2, ¿qué podría hacerse para reconstruir la confianza?', 'Abrir un diálogo con información y atender las propuestas', 'Cerrar todo diálogo hasta que termine el reclamo ante el tribunal', 'Dar por terminado el tema porque ya se presentó el proyecto de la empresa', 'Reconstruir confianza exige información y escucha; cerrar el diálogo no la mejora.'),
    ],
    ctx=('En una localidad de ejemplo, al cerrar la escuela rural muchas familias se trasladan a la ciudad y los niños dejan de usar su lengua en la casa. ¿Qué relación entre procesos se observa?', 'La migración a la ciudad puede disminuir el uso de la lengua', 'La migración a la ciudad aumenta siempre el uso de la lengua', 'La lengua se mantiene igual aunque cambien los lugares de vida', 'Al cambiar el entorno y perder la escuela local, hay menos espacios para usar la lengua.'),
    sc=[
        ('En Chile y la región, ¿para qué sirve la consulta previa?', 'Para informar y escuchar a la comunidad antes de decidir', 'Es un mecanismo de diálogo previo a decisiones que afectan a la comunidad.'),
        ('Nombra una consecuencia posible de un proyecto que cambia el uso de un río.', 'Puede cambiar el acceso al agua de la comunidad', 'Un cambio en el territorio afecta a la economía, el ambiente y la cultura.'),
        ('¿Por qué es mejor hablar de «probable» que de «seguro» al explicar consecuencias?', 'Porque los procesos sociales tienen varios factores y no son automáticos', 'La prudencia evita afirmar más de lo que muestran los datos.'),
    ],
    op=("Usa la {F} Escribe una cadena de cuatro pasos para cada situación (1 y 2), desde la forma de decidir hasta una consecuencia posible. Indica qué es hecho y qué es hipótesis en cada una. No agregues datos que la ficha no trae.",
        "Situación 1: consulta previa → información y propuestas de cambio → acuerdo de controles del agua → mayor confianza (probable). Hecho: se acordaron controles. Hipótesis: la confianza aumenta. Situación 2: sin consulta → la comunidad se entera por la prensa → pierde la confianza → presenta un reclamo. Hecho: presentó un reclamo. Hipótesis: la falta de consulta explica la pérdida de confianza.",
        ["dos cadenas de cuatro pasos", "separa hecho de hipótesis", "no agrega datos inventados"], ["dos cadenas"], ["afirmar certezas sin evidencia", "inventar datos"],
        "Pregunta qué dato nuevo cambiaría una de tus hipótesis."),
    rx=("Explica con un ejemplo la diferencia entre un hecho y una hipótesis.", "Averigua con apoyo del educador o educadora tradicional, si existe, o de tu docente, qué actividades de lengua se hacen en tu zona."),
)

# ============================================================ OA 04, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). La comuna ficticia de Cerro Claro, donde vive la comunidad de Lomas Verdes, evalúa tres alternativas para mejorar la relación con las comunidades indígenas. "
     "Alternativa A: una mesa permanente de diálogo entre comunidades, municipio y empresas. Alternativa B: contratar educadores tradicionales en las escuelas con programa intercultural. "
     "Alternativa C: una campaña de información pública sobre derechos de los pueblos. Criterios (1 punto si se cumple, 0 si no): respeta el derecho a ser consultados; "
     "las comunidades participan en su diseño; se puede hacer con el presupuesto disponible; sus efectos duran más de un año. "
     "A cumple los cuatro criterios menos el presupuesto. B cumple participación, presupuesto y duración, pero no consulta. C cumple solo presupuesto y duración.")
build(
    O4, 5, F,
    use="Aprenderé a evaluar alternativas para mejorar la relación entre Estado, municipios, empresas y pueblos indígenas con criterios que incluyen consulta y participación.",
    explain=[
        'Evaluar alternativas es compararlas con criterios claros. En temas que afectan a pueblos indígenas son especialmente relevantes dos: si la alternativa respeta el derecho a ser consultados y si las propias comunidades participan en su diseño. Otros criterios habituales son la factibilidad (si se puede hacer con el presupuesto y los plazos), la duración de los efectos y los efectos no deseados, como dejar fuera a ciertas comunidades o a las personas que viven en la ciudad.',
        'Una forma simple de comparar es una lista de verificación: se asigna 1 punto si la alternativa cumple un criterio y 0 si no, y se suman los puntos. Esta lista ordena la discusión, pero no decide por sí sola: los criterios pueden pesar distinto y las comunidades pueden tener prioridades propias. Por eso se recomienda mostrar los puntajes, explicar los criterios y conversar con las comunidades antes de decidir.',
    ],
    vocab=[("criterio", "regla con que se compara una alternativa"), ("lista de verificación", "tabla en que se marca si cada alternativa cumple o no cada criterio"), ("efecto no deseado", "consecuencia negativa que no se buscaba"), ("participación", "intervención de las comunidades en las decisiones que las afectan"), ("factibilidad", "posibilidad real de hacer algo con los recursos disponibles")],
    worked=[
        ("Sumar una lista", "Una alternativa de ejemplo cumple 3 de 4 criterios. ¿Cuántos puntos tiene?", ["Cada criterio cumplido vale 1 punto.", "3 cumplidos dan 3 puntos."], "3 puntos"),
        ("Revisar un efecto no deseado", "Un programa de ejemplo solo beneficia a quienes viven en el campo. ¿Qué efecto no deseado puede tener?", ["Deja fuera a las personas que viven en la ciudad.", "Eso puede aumentar la desigualdad entre miembros de una misma comunidad."], "Excluir a quienes viven en la ciudad"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar si respeta la consulta.", "En estos temas el derecho a ser consultados es un criterio central.", "Incluye siempre consulta y participación entre los criterios."),
              ("Tomar el puntaje más alto como decisión final.", "Los puntajes ordenan la discusión, pero no reemplazan el diálogo.", "Explica los criterios y conversa con las comunidades.")],
    T=[
        ('¿Qué es un criterio?', 'Una regla con que se compara una alternativa', 'Una orden del Estado que no admite discusión', 'Un resultado final que ya se alcanzó en el pasado', 'Un criterio es una pauta de comparación, no una orden ni un resultado.'),
        ('¿Qué es una lista de verificación?', 'Una tabla donde se marca si cada alternativa cumple o no', 'Una lista de personas que deben aprobar un proyecto', 'Una lista de precios de los productos del programa', 'Sirve para marcar el cumplimiento de criterios y sumar puntos.'),
        ('¿Qué es un efecto no deseado?', 'Una consecuencia negativa que no se buscaba', 'Una consecuencia positiva que se planificó antes', 'Un objetivo que se alcanza antes de lo previsto', 'No deseado significa no buscado y perjudicial para alguien.'),
        ('=', '{F} ¿Cuántos puntos suma la Alternativa A?', '1+1+0+1', 'Cumple consulta, participación y duración, pero no el presupuesto.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma la Alternativa B?', '0+1+1+1', 'No cumple consulta, pero sí participación, presupuesto y duración.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma la Alternativa C?', '0+0+1+1', 'Solo cumple presupuesto y duración.', ' puntos'),
        ('{F} Según la lista, ¿qué alternativas empatan en el primer lugar?', 'A y B, con 3 puntos cada una, y la C con 2', 'A y C, con 3 puntos cada una', 'B y C, con 2 puntos cada una', 'La A suma 3, la B suma 3 y la C suma 2; por eso empatan A y B.'),
        ('{F} Si A y B empatan con 3 puntos, ¿qué criterio puede usarse para desempatar en este tema?', 'Que respete el derecho a ser consultados', 'Que su nombre sea más corto y fácil de recordar', 'Que sea la primera que alguien propuso en la mesa', 'En asuntos que afectan a comunidades indígenas, la consulta es un criterio central.'),
        ('{F} ¿Qué criterio incumple la Alternativa B?', 'El derecho a ser consultados', 'La participación de las comunidades', 'La duración de los efectos', 'La ficha dice que B no cumple consulta.'),
        ('{F} Alguien dice: «La Alternativa C es mejor, porque es barata y sus efectos duran». ¿Qué objeción es más sólida?', 'No respeta la consulta ni la participación de las comunidades', 'Su costo es más alto que el de todas las demás alternativas en la ficha', 'Sus efectos duran menos de un año, según los datos de la ficha de trabajo', 'C cumple presupuesto y duración, pero no consulta ni participación.'),
        ('{F} ¿Qué efecto no deseado podría tener la Alternativa B?', 'Que comunidades sin escuela intercultural queden fuera', 'Que todas las escuelas pierdan estudiantes', 'Que la lengua desaparezca por contratar educadores', 'Un programa en escuelas puntuales puede dejar fuera a comunidades sin esa escuela.'),
        ('{F} ¿Cómo podrían combinarse A y B para mejorar el resultado?', 'Usar la mesa de diálogo para diseñar el programa de educadores', 'Reemplazar la mesa de diálogo por una decisión tomada sin consulta previa', 'Cancelar el programa de educadores para ahorrar presupuesto municipal', 'Una mesa de diálogo permite que las comunidades participen en el diseño de B y subsane su falta de consulta.'),
        ('{F} Antes de decidir entre A, B o C, ¿qué paso es recomendable?', 'Conversar con las comunidades sobre sus prioridades', 'Elegir la de más puntos sin mirar nada más', 'Esperar que una empresa proponga una cuarta', 'Los puntajes no reemplazan el diálogo con quienes serán afectados.'),
    ],
    ctx=('Una alternativa de ejemplo cumple consulta, participación y duración, pero no presupuesto; otra cumple solo presupuesto y duración. ¿Cuál suma más y cuántos puntos de diferencia hay?', 'La primera, por 1 punto', 'La segunda, por 1 punto', 'La primera, por 2 puntos', 'La primera suma 3 y la segunda 2; la diferencia es 1 punto.'),
    sc=[
        ('Nombra dos criterios importantes al evaluar propuestas que afectan a pueblos indígenas.', 'Por ejemplo, la consulta previa y la participación de las comunidades', 'Son criterios que garantizan voz a quienes serán afectados.'),
        ('=', 'Una alternativa de ejemplo cumple 2 de 4 criterios y otra cumple 3. ¿Cuántos puntos suman entre las dos?', '2+3', 'Se suman los puntos de ambas.', ' puntos'),
        ('¿Por qué un puntaje alto no basta para decidir?', 'Porque los criterios pueden pesar distinto y las comunidades tienen prioridades propias', 'El puntaje ordena, pero la decisión requiere diálogo.'),
    ],
    op=("Usa la {F} Redacta una recomendación de cinco líneas: qué alternativa o combinación elegirías, sus puntajes, qué criterio pesó más, un efecto no deseado posible y cómo conversarías con las comunidades antes de decidir.",
        "Recomiendo combinar A y B. A suma 3 y B suma 3. Pesó el derecho a ser consultados y la participación. Un efecto no deseado: que comunidades sin escuela intercultural queden fuera. Antes de decidir conversaría con las comunidades, en la mesa de diálogo, sobre sus prioridades y la forma de elegir a los educadores tradicionales.",
        ["usa los puntajes de la ficha", "incluye consulta y participación", "reconoce un efecto no deseado"], ["recomendación de cinco líneas"], ["decidir solo por puntaje", "ignorar a las comunidades"],
        "Pregunta cómo cambia tu recomendación si las comunidades priorizan otra cosa."),
    rx=("Suma una lista de verificación inventada con cinco criterios y tres alternativas.", "Conversa con tu docente sobre qué instancias de participación existen en tu comuna para las comunidades."),
)

# ============================================================ OA 04, clase 6
F = ("Ficha 6 (caso de ejemplo, inventado). Dos borradores de un informe escolar sobre la comunidad ficticia de Lomas Verdes. "
     "Borrador 1: «Los indígenas viven en el campo, hablan todos su lengua y están en contra de cualquier proyecto». "
     "Borrador 2: «Según una dirigente de Lomas Verdes (entrevista de ejemplo), la comunidad pide ser consultada antes de proyectos en su territorio. "
     "En la encuesta de ejemplo, 70 % de las personas que se identificaron como indígenas vive en ciudades. Faltan datos para saber cuántas personas hablan la lengua. "
     "Esta redacción debe ser revisada por la comunidad y por su educador o educadora tradicional».")
build(
    O4, 6, F,
    use="Aprenderé a comunicar una conclusión situada y respetuosa sobre pueblos indígenas: atribuyendo voces, usando datos con sus límites y pidiendo revisión a las comunidades.",
    explain=[
        'Comunicar sobre pueblos indígenas exige cuidado. Una conclusión situada dice de qué comunidad, lugar, tiempo y fuente habla, y no extiende lo que ocurre en un caso a todos los pueblos. Conviene usar el nombre del pueblo o la comunidad cuando se conoce, atribuir cada afirmación a quien la dijo («según una dirigente…»), usar datos con su año y su límite, y diferenciar el hecho de la interpretación. Se debe evitar el lenguaje que presenta a los pueblos como un grupo único, como «los indígenas piensan…».',
        'También es parte de comunicar con respeto reconocer qué no sabemos: si no hay datos, se dice. Cuando un texto trata de la cultura, la lengua o las creencias de un pueblo, lo adecuado es consultar a la propia comunidad o a su educador o educadora tradicional, y pedir que revise lo escrito. Una conclusión puede terminar con una pregunta para la comunidad o una propuesta que esa comunidad pueda discutir, sin hablar en su nombre.',
    ],
    vocab=[("atribuir", "indicar quién dijo una idea o de qué fuente proviene"), ("conclusión situada", "conclusión que indica el lugar, el tiempo y la fuente a los que se refiere"), ("generalización", "extender lo observado en un caso a todos los casos"), ("revisión de la comunidad", "lectura de un texto por parte de la comunidad de la que habla"), ("lenguaje respetuoso", "uso de palabras que no estereotipan ni borran la diversidad")],
    worked=[
        ("Reescribir una generalización", "Un texto de ejemplo dice: «Los indígenas no quieren desarrollo». ¿Cómo se reescribe con atribución?", ["Se identifica quién habla.", "Se cita la fuente y se evita generalizar."], "Según un dirigente de ejemplo de esta comunidad, la comunidad pide ser consultada antes de los proyectos"),
        ("Decir lo que no se sabe", "En un caso de ejemplo no hay datos de cuántas personas hablan la lengua. ¿Qué se escribe?", ["No se inventa una cifra.", "Se declara que faltan datos."], "Faltan datos sobre el uso de la lengua"),
    ],
    mistakes=[("Escribir «los indígenas» para referirse a todos los pueblos.", "Hay pueblos distintos con voces propias.", "Nombra la comunidad o el pueblo y atribuye cada idea."),
              ("Escribir sobre la cultura de una comunidad sin que ella lo revise.", "Se pueden cometer errores y faltar a su derecho a hablar por sí misma.", "Pide la revisión de la comunidad o de su educador o educadora tradicional.")],
    T=[
        ('¿Qué significa atribuir una afirmación?', 'Indicar quién la dijo o de qué fuente proviene, para evaluarla', 'Aceptarla sin pensar porque la dijo alguien conocido', 'Cambiarla para que suene más fuerte y convincente', 'Atribuir es decir de quién es una idea para que el lector la pueda evaluar.'),
        ('¿Qué hace situada a una conclusión sobre un pueblo indígena?', 'Una conclusión que indica lugar, tiempo y fuente', 'Una conclusión que vale para todo lugar y tiempo', 'Una conclusión que no necesita datos ni fuentes', 'Situar es decir a qué caso se refiere y con qué datos.'),
        ('¿Por qué conviene nombrar el pueblo o la comunidad cuando se conoce?', 'Porque evita tratar a muchos pueblos distintos como uno solo', 'Porque es obligatorio nombrar a todos los pueblos', 'Porque así se evita citar la fuente del dato', 'Nombrar evita borrar la diversidad entre pueblos.'),
        ('{F} ¿Qué falla tiene el Borrador 1 en la frase «Los indígenas viven en el campo»?', 'Generaliza y deja fuera a quienes viven en ciudades', 'Cita la fuente y el año de los datos con precisión', 'Atribuye la afirmación a una dirigente de la comunidad', 'El Borrador 2 muestra que 70 % vive en ciudades en la encuesta de ejemplo.'),
        ('{F} ¿Qué falla tiene la frase «hablan todos su lengua»?', 'Da un dato sin fuente, y la ficha dice que faltan datos', 'Está bien redactada porque es breve y sencilla', 'Es un dato comprobado porque aparece en el borrador', 'No se sabe cuántos hablan la lengua; el Borrador 2 indica que faltan datos.'),
        ('{F} ¿Qué mejora incluye el Borrador 2 en cuanto a las voces?', 'Cita a una dirigente de la comunidad', 'Habla en nombre de todos los pueblos indígenas de la región', 'No menciona ninguna fuente de las afirmaciones que presenta', 'Dice «según una dirigente» y especifica que es una entrevista de ejemplo.'),
        ('{F} ¿Qué dato presenta el Borrador 2 con su límite?', 'El 70 % que vive en ciudades, según una encuesta', 'El número exacto de hablantes de la comunidad', 'La opinión de todos los pueblos sobre los proyectos', 'Cita el porcentaje con su fuente; sobre los hablantes, dice que faltan datos.'),
        ('{F} ¿Qué hace bien el Borrador 2 respecto de lo que no se sabe?', 'Reconoce abiertamente que faltan datos sobre el uso de la lengua', 'Inventa una cifra para que la conclusión parezca completa', 'Evita mencionar el tema para que nadie note la falta', 'Declarar lo que falta es honestidad intelectual.'),
        ('{F} ¿Por qué el Borrador 2 pide revisión de la comunidad y de su educador o educadora tradicional?', 'Porque la comunidad conoce su cultura y puede corregir', 'Porque la comunidad debe aprobar todos los trabajos escolares', 'Porque así se evita citar fuentes', 'La revisión respeta el derecho de la comunidad a hablar por sí misma.'),
        ('{F} Alguien dice: «El Borrador 1 es mejor porque es corto y claro». ¿Qué respuesta es más completa?', 'Es corto, pero generaliza y no cita ninguna fuente', 'Es mejor, porque un texto breve no necesita citar fuentes', 'Es peor solo porque usa palabras más sencillas', 'La brevedad no compensa generalizar ni omitir fuentes.'),
        ('{F} Reescribe mejor «están en contra de cualquier proyecto»: ¿cuál opción es más fiel a la ficha?', 'Según una dirigente, la comunidad pide ser consultada antes', 'La comunidad rechaza todos los proyectos de las empresas', 'La comunidad acepta todo proyecto que cree empleo', 'La ficha dice que se pide consulta, no que se rechacen todos los proyectos.'),
        ('Un estudiante quiere describir una ceremonia de un pueblo con lo que vio en una película. ¿Qué es lo más adecuado?', 'Pedir a la comunidad o a su educador o educadora que oriente el texto', 'Describirla con detalle, porque una película es fuente suficiente y completa', 'Inventar los detalles que falten para que el texto quede completo y atractivo', 'La cultura la explican quienes la viven; una película puede ser incompleta o inexacta.'),
        ('{F} ¿Cuál es una buena pregunta final para el informe?', '¿Cómo quieren las familias de Lomas Verdes que se haga la consulta?', '¿Por qué los pueblos indígenas se oponen siempre al desarrollo del país entero?', '¿Qué opina la mayoría de la población del país sobre la comunidad de Lomas Verdes?', 'La pregunta debe dirigirse a la comunidad y no sugerir una respuesta ni un prejuicio.'),
    ],
    ctx=('Un estudiante de ejemplo prepara una exposición sobre una comunidad y duda si incluir una costumbre que leyó en un blog. ¿Qué es lo más responsable?', 'Verificarla con la comunidad o su educador o educadora tradicional', 'Incluirla porque un blog publicado en internet es siempre una fuente confiable', 'Cambiar algunos detalles de la costumbre para que no se note la fuente', 'Las costumbres las explica la comunidad; un blog puede contener errores.'),
    sc=[
        ('Nombra dos prácticas para comunicar con respeto sobre un pueblo.', 'Por ejemplo, atribuir las voces y pedir revisión a la comunidad', 'También sirve nombrar el pueblo y declarar lo que falta.'),
        ('¿Por qué no se inventa una cifra cuando faltan datos?', 'Porque engañaría a quien lee y no se podría verificar', 'Es más honesto decir que faltan datos.'),
        ('¿Por qué evitar la frase «los indígenas piensan…»?', 'Porque presenta a muchos pueblos y personas como un solo grupo', 'Cada pueblo y persona tiene voz propia.'),
    ],
    op=("Usa la {F} Escribe una versión mejorada de un párrafo de cuatro oraciones sobre la comunidad de Lomas Verdes con estas cuatro partes: una afirmación atribuida, un dato con su límite, algo que no se sabe y una pregunta para la comunidad. Incluye al final la frase de revisión por la comunidad.",
        "Según una dirigente de Lomas Verdes (entrevista de ejemplo), la comunidad pide ser consultada antes de proyectos en su territorio. En una encuesta de ejemplo, 70 % de las personas que se identificaron como indígenas vive en ciudades. Faltan datos sobre cuántas personas hablan la lengua. Pregunta para la comunidad: ¿cómo les gustaría participar en la consulta? Esta redacción debe ser revisada por la comunidad y por su educador o educadora tradicional.",
        ["atribuye una afirmación", "da un dato con límite", "declara lo que falta y pide revisión"], ["párrafo de cuatro oraciones", "frase de revisión"], ["generalizar a «los indígenas»", "inventar datos"],
        "Revisa que ninguna oración hable por la comunidad sin atribuir."),
    rx=("Reescribe una frase que generalice sobre un grupo para hacerla más precisa.", "Si hay un educador o educadora tradicional en tu escuela, pregúntale cómo prefiere que se escriba sobre su pueblo."),
)
