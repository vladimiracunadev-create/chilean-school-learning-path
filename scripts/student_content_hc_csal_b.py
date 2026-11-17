"""Ciencias de la salud (electivo 3.º y 4.º medio HC): OAC-03 (estilos de vida y salud integral, clases 1 a 5) y OAC-04 (aire, agua y suelo y salud, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, internet ni medirte a ti ni a nadie. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos, no diagnostica ni da consejos médicos personales, y no incluye procedimientos clínicos ni dosis. "
             "Las cifras de salud y de ambiente son ilustrativas: sirven para practicar el análisis, no para decidir sobre tu alimentación, tu actividad o tu sueño. Para eso consulta a un profesional de salud. "
             "Si un tema te preocupa a ti o a alguien cercano, cuéntaselo a una persona adulta de confianza o a un profesional de salud; si necesitas orientación inmediata, el Fono Niños 147 puede ayudarte.")
build = make_build(MATERIALS)

O3 = "CN-CSAL-3y4-OAC-03"
O4 = "CN-CSAL-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 11 (cadenas de ejemplo para delimitar la pregunta). "
     "Estilo de vida A, actividad física regular. Nivel celular: las células musculares gastan más ATP, la molécula que entrega energía, y producen más ATP a partir de glucosa y oxígeno. Nivel fisiológico: el corazón y los pulmones se adaptan para llevar más oxígeno a los músculos. Nivel de conducta: puede mejorar el ánimo y el sueño. "
     "Estilo de vida B, dormir pocas horas de manera sostenida. Nivel celular y hormonal: cambian señales que regulan el hambre y la saciedad. Nivel fisiológico: baja la capacidad de concentración. Nivel de conducta: aumentan los errores por distracción. "
     "Datos de ejemplo de un curso ficticio de 30 estudiantes: 12 duermen menos de 6 horas por noche.")
build(
    O3, 1, F,
    use="Aprenderé a delimitar una pregunta causal sobre estilos de vida y salud, distinguiendo los niveles celular, fisiológico y de conducta. Sirve para no mezclar hábitos, efectos y explicaciones en una sola frase.",
    prior=["Sé que las células obtienen energía de los nutrientes.", "Sé que el corazón y los pulmones llevan oxígeno al cuerpo.", "Distingo una causa de un efecto."],
    explain=[
        "El estilo de vida es el conjunto de hábitos de una persona: alimentación, actividad física, sueño, consumo de sustancias y manejo del estrés. La salud humana integral incluye lo físico, lo mental y lo social. Los hábitos influyen en la salud a través de varios niveles. En el nivel celular está el metabolismo, es decir, el conjunto de reacciones químicas de las células, y la energética celular, que es cómo las células obtienen energía en forma de ATP.",
        "Del nivel celular se pasa al fisiológico, que es el funcionamiento de órganos y sistemas como el corazón, los pulmones y el sistema hormonal, y de ahí a la conducta, es decir, lo que la persona siente, piensa y hace. Una pregunta causal sobre estilos de vida debe decir qué hábito es la causa (la variable que se compara) y qué efecto se mide, y en qué nivel. Por ejemplo, «¿cambia la atención en clase si se duerme menos de 6 horas?».",
        "Causa y asociación no son lo mismo. Para afirmar que un hábito causa un efecto se pide más que ver que ocurren juntos: que la causa venga antes, que a mayor cantidad del hábito haya mayor efecto, que exista un mecanismo biológico que lo explique y que otros estudios coincidan. Los datos de este cuaderno no sirven para diagnosticar a nadie: si te preocupa tu sueño, tu alimentación o tu ánimo, conversa con una persona adulta de confianza o con un profesional de salud.",
    ],
    vocab=[("estilo de vida", "conjunto de hábitos de una persona, como alimentación, actividad física y sueño"), ("metabolismo", "conjunto de reacciones químicas de las células"), ("ATP", "molécula que entrega energía a las células"), ("fisiología", "funcionamiento de los órganos y sistemas del cuerpo"), ("conducta", "lo que una persona siente, piensa y hace")],
    worked=[
        ("Ubicar en el nivel", "Se observa que quienes hacen actividad física regular tienen un corazón que bombea más sangre por cada latido. ¿En qué nivel está esta observación?",
         ["El corazón es un órgano.", "El funcionamiento de órganos y sistemas es el nivel fisiológico."],
         "Nivel fisiológico"),
        ("Delimitar una pregunta causal", "Quieres estudiar el sueño y la atención en un curso de ejemplo. ¿Qué pregunta está bien delimitada: «¿es bueno dormir?» o «¿baja el puntaje de atención de estudiantes que duermen menos de 6 horas, comparados con quienes duermen más?»",
         ["La primera no dice qué efecto se mide ni con qué comparación.", "La segunda fija la causa (dormir menos de 6 horas), el efecto (puntaje de atención) y una comparación."],
         "La segunda pregunta"),
    ],
    mistakes=[("Afirmar que un hábito causa un efecto solo porque aparecen juntos.", "Se necesita además orden temporal, mecanismo y coincidencia de estudios.", "Escribe «se asocia con» hasta tener más evidencia."),
              ("Explicar todo en un solo nivel, por ejemplo solo con fuerza de voluntad.", "La salud integral se explica por varios niveles que interactúan.", "Nombra el nivel celular, el fisiológico y el de conducta.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es el metabolismo?", "El conjunto de reacciones químicas de las células", "El peso de una persona", "El número de comidas al día", "El metabolismo describe las reacciones químicas que ocurren en las células."),
        ("{F} ¿Qué molécula entrega energía a las células musculares?", "El ATP", "La ficha nombra el ATP como la molécula que entrega energía."),
        ("ab", "{F} En el estilo de vida A, el corazón y los pulmones se adaptan para llevar más oxígeno. ¿En qué nivel está esto?", "Fisiológico", "Celular", "Corazón y pulmones son órganos y sistemas, así que el nivel es el fisiológico."),
        ("abc", "{F} En el estilo de vida B, el aumento de errores por distracción pertenece al nivel:", "De conducta", "Celular", "Fisiológico", "Los errores por distracción son algo que la persona hace, es decir, conducta."),
        ("=", "{F} Si 12 de los 30 estudiantes duermen menos de 6 horas por noche, ¿qué porcentaje del curso es?", "12/30*100", "Son 12 de 30, es decir, 40 %.", " %"),
        ("abc", "{F} ¿Cuál es la mejor pregunta causal sobre el estilo de vida B?", "¿Baja el puntaje de atención de quienes duermen menos de 6 horas comparado con quienes duermen más?", "¿Qué es el sueño?", "¿Por qué hay estudiantes?", "La pregunta fija una causa, un efecto medible y una comparación."),
        ("abc", "Un estudiante dice: «la actividad física causa mejor ánimo porque las dos cosas aparecen juntas en mi curso». ¿Qué falta para afirmar una causa?", "Mostrar que la actividad viene antes, que hay mecanismo y que otros estudios coinciden", "Nada, porque ya aparecen juntas", "Preguntar solo a los amigos", "Para afirmar causa se necesita más que la coincidencia de dos variables."),
        ("ab", "{F} Otro curso de ejemplo tiene 40 estudiantes y 18 de ellos duermen menos de 6 horas. ¿Cuál de los dos cursos tiene el mayor porcentaje de estudiantes que duermen poco?", "El otro curso, con 45 %", "El curso de la ficha, con 40 %", "Se compara 18 de 40, que es 45 %, con 12 de 30, que es 40 %."),
        ("abc", "{F} ¿Qué variable se compara si se quiere estudiar el sueño y la atención?", "Las horas de sueño", "El nombre del curso", "El color de los cuadernos", "La causa propuesta es la cantidad de sueño y por eso es lo que se compara."),
        ("abc", "{F} Una persona dice: «dormir poco solo es falta de voluntad». ¿Qué responde una mirada con varios niveles?", "Que también influyen el nivel hormonal y fisiológico y el entorno, no solo la voluntad", "Que tiene razón, el sueño solo depende de la voluntad", "Que el sueño no afecta nada", "El sueño se relaciona con señales celulares y hormonales, además de la conducta."),
        ("abc", "{F} ¿Por qué es útil nombrar el nivel celular al explicar un efecto del estilo de vida?", "Porque ayuda a proponer un mecanismo, es decir, cómo el hábito produce el efecto", "Porque reemplaza la necesidad de datos", "Porque convierte cualquier hábito en una causa", "El mecanismo celular da una explicación posible, que además debe sostenerse con datos."),
        ("abc", "Un docente de ejemplo escribe: «dormir menos de 6 horas cuatro noches seguidas se asocia con peor atención». ¿Qué tipo de afirmación es?", "Una asociación que se debería evaluar con más evidencia", "Una causa demostrada", "Una opinión sin ninguna relación con la salud", "La frase usa «se asocia con», propia de una relación todavía por evaluar."),
        ("abc", "Un estudiante ficticio duerme poco y se pregunta si «le pasa algo grave». ¿Qué corresponde según este cuaderno?", "Conversar con una persona adulta de confianza o con un profesional de salud", "Diagnosticarse con la ficha", "Ignorar el tema para siempre", "Este cuaderno no diagnostica y recomienda consultar a profesionales."),
    ],
    ctx=("abc", "Contexto: tu curso quiere hacer un afiche sobre sueño y atención. ¿Qué mensaje es más honesto con la evidencia?", "Dormir poco se asocia con peor atención, y hay mecanismos posibles que se siguen estudiando", "Dormir poco siempre causa fracaso escolar", "El sueño no influye en nada", "El mensaje usa «se asocia con» y reconoce lo que aún se estudia."),
    sc=[
        ("En Ciencias de la salud: ¿qué es el ATP?", "La molécula que entrega energía a las células", "El ATP es la energía utilizable de las células."),
        ("ab", "Una pregunta causal bien delimitada incluye:", "Una causa, un efecto medible y una comparación", "Solo una opinión", "Esos tres elementos permiten responder con datos."),
        ("ab", "Si dos variables aparecen juntas, se habla de:", "Una asociación", "Una causa demostrada", "Aparecer juntas es una asociación y no basta para afirmar causa."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) elige uno de los dos estilos de vida y completa una cadena con un hábito, un efecto celular, uno fisiológico y uno de conducta; (2) escribe una pregunta causal bien delimitada; (3) escribe qué evidencia pedirías antes de decir que el hábito causa el efecto.",
        "(1) Estilo A: actividad regular, más ATP producido, corazón y pulmones adaptados, mejor ánimo. (2) «¿Mejora el puntaje de bienestar de estudiantes que hacen actividad regular, comparados con quienes no la hacen?» (3) Pediría que la actividad ocurra antes del cambio, que haya más bienestar con más actividad y que otros estudios coincidan.",
        ["cadena con los tres niveles", "pregunta con causa, efecto y comparación", "pide al menos dos tipos de evidencia", "usa lenguaje de asociación si no hay prueba"],
        ["cadena, pregunta y evidencia numeradas"],
        ["afirmar causa solo por coincidencia", "usar un solo nivel", "hacer una pregunta sin comparación"],
        "Pregunta: «¿qué cambiaría en tu pregunta si quisieras estudiar el efecto a largo plazo?»."),
    reinforce="Escribe tres frases, una por cada nivel (celular, fisiológico y de conducta), sobre cómo un mismo hábito te puede influir.",
    extend="Explica por qué una cadena que parte en el nivel celular no basta para afirmar una causa y qué más hay que mostrar.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 12 (dos estudios de ejemplo sobre sueño y atención). "
     "Estudio 1, observacional: se midió el sueño y un puntaje de atención de 0 a 100 en 500 adolescentes elegidos al azar, sin cambiar sus hábitos. Quienes duermen 8 horas o más tuvieron un promedio de 70 puntos y quienes duermen menos de 6 horas, 58 puntos. "
     "Estudio 2, experimental, aprobado por un comité de ética y con consentimiento informado: 60 adolescentes voluntarios fueron asignados al azar a dormir 9 horas (grupo 1) o 6 horas (grupo 2) durante una semana. El puntaje de atención inicial era 72 en ambos grupos. Al final, el grupo 1 tuvo 74 puntos y el grupo 2, 64 puntos. "
     "Nota: en el Estudio 1, los estudiantes que duermen poco suelen tener también más horas de trabajo y más tiempo en pantallas.")
build(
    O3, 2, F,
    use="Aprenderé a evaluar fuentes y variables en estudios sobre estilos de vida, distinguiendo estudios observacionales de experimentales y reconociendo variables confusoras. Sirve para decidir qué estudios dan más fuerza a una relación causal.",
    prior=["Sé calcular diferencias y promedios.", "Sé qué es una variable confusora.", "Sé que un estudio con personas necesita consentimiento."],
    explain=[
        "Los estudios sobre estilos de vida se dividen en dos grandes tipos. En un estudio observacional se miden los hábitos y los resultados sin cambiar nada; sirve para ver asociaciones, pero puede tener variables confusoras, como en la ficha, donde quienes duermen poco también trabajan más. En un estudio experimental se asigna al azar a las personas a un grupo y otro, y se compara el cambio, lo que permite acercarse mejor a una causa.",
        "La asignación al azar reparte las otras características entre los grupos, de modo que la diferencia final se atribuye con más seguridad al hábito. Pero también tiene límites: un experimento corto no muestra los efectos de largo plazo, y los voluntarios pueden no representar a toda la población. Los estudios con personas deben tener aprobación ética, consentimiento informado y evitar daños; por eso muchas preguntas solo se pueden estudiar con observación.",
        "Al evaluar una fuente se revisa el tamaño de la muestra, la forma de elegir a las personas, cómo se midió el resultado, si hay un grupo de comparación y si los autores tienen intereses. Una buena evidencia causal suele sumar varios estudios de distinto tipo que coinciden y un mecanismo biológico plausible, es decir, una explicación posible de cómo el hábito produce el efecto.",
    ],
    vocab=[("estudio observacional", "estudio que mide hábitos y resultados sin cambiar nada"), ("estudio experimental", "estudio que asigna a las personas a grupos y compara los cambios"), ("asignación al azar", "reparto de las personas a los grupos por sorteo"), ("consentimiento informado", "aceptación libre de participar, después de conocer los riesgos y objetivos"), ("mecanismo plausible", "explicación biológica posible de cómo una causa produce un efecto")],
    worked=[
        ("Calcular un cambio", "En un experimento de ejemplo, un grupo pasa de 60 a 66 puntos y otro de 60 a 54. ¿Cuánto cambió cada grupo?",
         ["Primer grupo: 66 menos 60 son 6 puntos más.", "Segundo grupo: 54 menos 60 son 6 puntos menos."],
         "+6 y −6 puntos"),
        ("Elegir el estudio más fuerte", "Para saber si un hábito causa un efecto, ¿qué ofrece más fuerza: un estudio observacional o uno experimental con asignación al azar?",
         ["El experimental reparte las otras características entre los grupos.", "Por eso la diferencia se atribuye con más seguridad al hábito."],
         "El experimental con asignación al azar"),
    ],
    mistakes=[("Creer que un estudio observacional prueba una causa.", "Puede haber variables confusoras que expliquen la diferencia.", "Habla de asociación y busca estudios que controlen las confusoras."),
              ("Creer que un experimento prueba el efecto a largo plazo.", "Un experimento corto solo muestra efectos de corto plazo.", "Declara el límite de tiempo en la conclusión.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es un estudio observacional?", "Uno que mide hábitos y resultados sin cambiar nada", "Uno que asigna al azar a los grupos", "Uno que no tiene datos", "Observacional significa que solo se observa y se mide."),
        ("{F} ¿Qué estudio (1 o 2) asignó a las personas al azar a un grupo?", "Estudio 2", "El Estudio 2 es el experimental, con asignación al azar."),
        ("ab", "{F} Un estudio con personas, como el Estudio 2, debe tener:", "Consentimiento informado y aprobación ética", "Solo la autorización de la dirección del liceo", "Las personas deben participar de forma libre y protegida, no por obligación."),
        ("=", "{F} En el Estudio 1, ¿cuántos puntos más de atención tuvieron en promedio quienes duermen 8 horas o más que quienes duermen menos de 6?", "70-58", "La diferencia entre 70 y 58 es de 12 puntos.", " puntos"),
        ("=", "{F} En el Estudio 2, ¿cuánto cambió el puntaje del grupo 2 entre el inicio y el final? Escribe el cambio como número positivo.", "72-64", "Pasó de 72 a 64, es decir, bajó 8 puntos.", " puntos"),
        ("=", "{F} En el Estudio 2, ¿cuántos puntos de diferencia hubo al final entre el grupo 1 y el grupo 2?", "74-64", "Al final hubo 74 contra 64, una diferencia de 10 puntos.", " puntos"),
        ("abc", "{F} ¿Qué variable confusora se menciona en la nota del Estudio 1?", "Más horas de trabajo y más tiempo en pantallas", "El color del uniforme", "El número de estudiantes", "Esas variables influyen en el sueño y también en la atención."),
        ("abc", "{F} ¿Por qué el Estudio 2 acerca más a una causa que el Estudio 1?", "Porque la asignación al azar reparte entre los grupos las otras características", "Porque tiene más puntos", "Porque dura menos de una semana", "Con grupos parecidos, la diferencia final se debe con más probabilidad al sueño."),
        ("abc", "{F} Alguien dice: «el Estudio 2 prueba que dormir 6 horas daña la atención para toda la vida». ¿Qué problema tiene?", "El estudio dura una semana y solo muestra efectos de corto plazo", "El estudio no tiene grupo de comparación", "El estudio no midió la atención", "El tiempo del experimento limita lo que se puede concluir."),
        ("abc", "¿Por qué no se hacen experimentos que asignen a las personas a hábitos que probablemente dañen su salud por mucho tiempo?", "Porque sería poco ético dañar a las personas", "Porque no se pueden medir", "Porque los hábitos no influyen", "Los estudios con personas deben evitar daños, por eso muchas preguntas se estudian con observación."),
        ("abc", "{F} Si los resultados del Estudio 1 y del Estudio 2 coinciden en la dirección del efecto, esto:", "Fortalece la idea de que el sueño influye en la atención", "Prueba que no hay otras causas", "Anula los dos estudios", "Estudios de distinto tipo que coinciden dan más confianza."),
        ("abc", "{F} Falta un mecanismo plausible para completar el argumento causal. ¿Cuál sería un buen mecanismo?", "Una explicación biológica de cómo dormir poco altera el funcionamiento del cerebro que sostiene la atención", "Que los estudiantes con peor atención prefieren acostarse tarde", "Que el puntaje de atención va de 0 a 100", "El mecanismo plausible explica cómo el hábito produciría el efecto."),
        ("abc", "{F} Para decidir si cambia la política de horarios de un liceo, ¿qué conviene hacer con estos estudios?", "Tomar la decisión con la evidencia disponible y reconocer sus límites", "Esperar que no quede ninguna duda", "Ignorar los estudios y decidir por costumbre", "Las decisiones de salud pública se toman con la mejor evidencia, declarando los límites."),
    ],
    ctx=("abc", "Contexto: un amigo te muestra un titular: «dormir menos de 6 horas daña a los jóvenes», basado en un estudio observacional. ¿Qué le dices?", "Que el estudio muestra una asociación y que conviene mirar si otros estudios y un mecanismo la apoyan", "Que no sirve porque es observacional", "Que está probado para siempre", "Un estudio observacional es útil, aunque no basta por sí solo para una causa."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la asignación al azar?", "El reparto de las personas a los grupos por sorteo", "El azar iguala los grupos en las demás características."),
        ("ab", "El consentimiento informado significa:", "Participar libremente después de conocer los riesgos y objetivos", "Firmar sin leer", "Una persona informada puede aceptar o rechazar con libertad."),
        ("ab", "Los estudios observacionales sirven para:", "Descubrir asociaciones", "Probar una causa por sí solos", "Observan relaciones, pero no controlan las confusoras."),
    ],
    op=("Con los estudios de la ficha {F} haz lo siguiente: (1) calcula las diferencias de cada estudio; (2) explica qué estudio da más fuerza a una causa y por qué; (3) nombra un límite de cada estudio.",
        "(1) Estudio 1: 12 puntos a favor de quienes duermen más. Estudio 2: diferencia final de 10 puntos entre los grupos. (2) El Estudio 2, porque asignó al azar y repartió las otras características. (3) Estudio 1: variables confusoras como trabajo y pantallas. Estudio 2: dura una semana.",
        ["diferencias correctas", "explica la ventaja de la asignación al azar", "un límite para cada estudio", "no afirma una causa definitiva"],
        ["tres partes numeradas"],
        ["decir que ambos estudios valen lo mismo", "no nombrar confusoras", "olvidar el límite de tiempo"],
        "Pregunta: «¿qué estudio nuevo pedirías para saber si el efecto dura meses?»."),
    reinforce="Anota dos diferencias entre un estudio observacional y uno experimental, y una ventaja de cada uno.",
    extend="Explica por qué hay preguntas de salud que solo pueden responderse con estudios observacionales y cómo se reduce su principal limitación.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 13 (modelos de ejemplo de energía en el cuerpo). "
     "Modelo celular: con oxígeno, la célula usa glucosa para producir CO2, agua y ATP en las mitocondrias, y rinde alrededor de 30 ATP por cada glucosa. Sin oxígeno, solo obtiene 2 ATP por cada glucosa. "
     "Modelo de balance de energía (de ejemplo, para una persona ficticia, en kilocalorías, kcal): ingreso por alimentos 2.400 kcal al día; gasto 2.200 kcal al día. Balance = ingreso menos gasto. "
     "Si la actividad física aumenta el gasto en 300 kcal al día y el ingreso no cambia, el balance cambia. "
     "Límites: el cuerpo regula el hambre y el gasto, y las personas son distintas. Este modelo no sirve para planificar la alimentación de nadie.")
build(
    O3, 3, F,
    use="Aprenderé a interpretar dos modelos, uno de la energética celular y otro del balance de energía, para explicar cómo los hábitos afectan el metabolismo. Sirve para ver por qué un modelo es útil y a la vez limitado.",
    prior=["Sé qué es la glucosa y que las células la usan.", "Sé que respirar entrega oxígeno a las células.", "Sé sumar y restar números grandes."],
    explain=[
        "Las células necesitan energía para funcionar. La obtienen en forma de ATP, que se produce sobre todo en las mitocondrias a partir de la glucosa y el oxígeno: es la respiración celular. Con oxígeno se obtiene alrededor de 30 ATP por glucosa; sin oxígeno solo 2. Por eso la actividad física intensa aumenta la demanda de oxígeno, y el corazón y los pulmones deben responder para llevarlo a los músculos.",
        "El balance de energía compara la energía que entra con los alimentos y la que se gasta en el metabolismo basal, la digestión y la actividad. Si el ingreso supera el gasto, el balance es positivo y el cuerpo almacena la energía sobrante. Si el gasto supera el ingreso, el balance es negativo. El modelo es una simplificación: el cuerpo regula el hambre y el gasto, y cada persona es distinta.",
        "Por eso un buen análisis nombra los límites del modelo y no lo usa para dar consejos individuales. El modelo celular explica por qué hace falta oxígeno, y el de balance explica la relación entre alimentación y actividad en una población. Las decisiones sobre la alimentación o la actividad de una persona concreta las orienta un profesional de salud, no este cuaderno.",
    ],
    vocab=[("respiración celular", "proceso en que las células obtienen ATP de la glucosa, usando oxígeno"), ("mitocondria", "organelo donde se produce la mayor parte del ATP"), ("balance de energía", "diferencia entre la energía que entra y la que se gasta"), ("metabolismo basal", "energía que el cuerpo gasta en reposo para mantenerse funcionando"), ("kilocaloría (kcal)", "unidad en que se mide la energía de los alimentos")],
    worked=[
        ("Calcular un balance", "Una persona ficticia ingiere 2.000 kcal y gasta 2.300 kcal en un día. ¿Cuál es su balance?",
         ["Balance es ingreso menos gasto: 2.000 menos 2.300.", "El resultado es −300 kcal."],
         "−300 kcal, balance negativo"),
        ("Comparar ATP", "Si una célula usa 5 glucosas con oxígeno, ¿cuántos ATP obtiene, si cada glucosa rinde 30 ATP con oxígeno, como dice el modelo de la ficha?",
         ["Se multiplica 5 por 30.", "5 por 30 son 150."],
         "150 ATP"),
    ],
    mistakes=[("Usar el modelo de balance para decidir cuánto debe comer una persona.", "El modelo es una simplificación y no considera la regulación del cuerpo ni las diferencias entre personas.", "Úsalo para entender relaciones generales y consulta a un profesional para decisiones personales."),
              ("Creer que sin oxígeno las células no producen nada de energía.", "Sin oxígeno obtienen una cantidad mucho menor de ATP, no cero.", "Recuerda que sin oxígeno se obtienen 2 ATP por glucosa en el modelo.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la respiración celular?", "El proceso en que las células obtienen ATP de la glucosa, usando oxígeno", "Entrar y sacar aire de los pulmones", "El movimiento de los músculos", "La respiración celular ocurre dentro de las células y produce ATP."),
        ("{F} ¿Cuántos ATP rinde una glucosa con oxígeno, según el modelo celular?", "Alrededor de 30", "El modelo dice que con oxígeno rinde alrededor de 30 ATP."),
        ("ab", "{F} Si el ingreso de energía supera al gasto, el balance es:", "Positivo", "Negativo", "El balance es ingreso menos gasto, y si el ingreso es mayor, el resultado es positivo."),
        ("=", "{F} ¿Cuál es el balance de energía de la persona ficticia, en kcal?", "2400-2200", "Se resta el gasto al ingreso: 2.400 menos 2.200.", " kcal"),
        ("=", "{F} Si el gasto aumenta en 300 kcal por actividad física y el ingreso no cambia, ¿cuál es el nuevo balance?", "2400-(2200+300)", "El nuevo gasto es 2.500 kcal y el balance es 2.400 menos 2.500.", " kcal"),
        ("=", "{F} Una célula usa 4 glucosas sin oxígeno. ¿Cuántos ATP obtiene?", "4*2", "Cada glucosa rinde 2 ATP sin oxígeno, y 4 por 2 son 8.", " ATP"),
        ("=", "{F} Una célula usa 3 glucosas con oxígeno. ¿Cuántos ATP más obtiene que si las usara sin oxígeno?", "3*30-3*2", "Con oxígeno obtiene 90 y sin oxígeno 6, una diferencia de 84.", " ATP"),
        ("abc", "{F} Durante un ejercicio muy intenso aumenta la demanda de oxígeno de los músculos. ¿Qué respuesta fisiológica esperas?", "Que el corazón y los pulmones lleven más oxígeno", "Que el corazón y los pulmones lleven menos oxígeno", "Que los músculos obtengan igual energía sin oxígeno", "Más oxígeno permite producir más ATP en los músculos."),
        ("abc", "{F} ¿Cuál es un límite del modelo de balance de energía?", "No considera que el cuerpo regula el hambre y el gasto", "Usa kilocalorías", "Tiene dos números", "La regulación del cuerpo y las diferencias entre personas no están en el modelo."),
        ("abc", "Alguien dice: «según el modelo, si como 100 kcal menos hoy bajaré de peso exactamente lo que dice la fórmula». ¿Qué respondes?", "Que el modelo es una simplificación y que el cuerpo se regula, por lo que no predice exactamente a una persona", "Que sí, el modelo siempre acierta", "Que el modelo es inútil", "El modelo muestra una tendencia general, no una predicción individual."),
        ("abc", "{F} ¿Qué parte de la ficha explica por qué el ejercicio intenso exige más oxígeno?", "El modelo celular, porque con oxígeno se produce mucho más ATP", "El modelo de balance, porque tiene kilocalorías", "La nota de límites", "El ATP que necesita el músculo se produce sobre todo con oxígeno."),
        ("abc", "Un joven ficticio quiere cambiar su alimentación y actividad usando solo este modelo. ¿Qué es lo más adecuado?", "Consultar a un profesional de salud para una orientación a su medida", "Seguir el modelo al pie de la letra", "Ignorar cualquier consejo", "Las decisiones individuales requieren una orientación profesional personalizada."),
        ("abc", "{F} ¿Qué cambiaría el balance de manera sostenida según el modelo?", "Cambiar el ingreso, el gasto o ambos de forma mantenida", "Mirar el balance una sola vez", "Cambiar el nombre del modelo", "El balance depende de cuánto entra y cuánto se gasta a lo largo del tiempo."),
    ],
    ctx=("abc", "Contexto: en el liceo se presenta un cartel que dice «comer menos siempre es sano». ¿Qué respuesta tiene en cuenta lo aprendido?", "El modelo muestra una relación entre ingreso y gasto, pero las necesidades de cada persona varían y requieren orientación profesional", "Sí, porque el balance negativo es lo mejor", "No, porque los modelos no sirven", "La respuesta reconoce la utilidad y los límites del modelo."),
    sc=[
        ("En Ciencias de la salud: ¿qué es el balance de energía?", "La diferencia entre la energía que entra y la que se gasta", "El balance resta el gasto del ingreso de energía."),
        ("ab", "Con oxígeno, una célula obtiene del mismo nutriente:", "Mucho más ATP", "Menos ATP", "La respiración con oxígeno rinde alrededor de 30 ATP contra 2 sin oxígeno."),
        ("ab", "El modelo de balance de energía sirve para:", "Entender relaciones generales entre alimentación y actividad", "Prescribir cuánto debe comer una persona", "Es un modelo general, no una receta individual."),
    ],
    op=("Con los modelos de la ficha {F} haz lo siguiente: (1) calcula el balance si el ingreso es 2.400 kcal y el gasto sube a 2.600 kcal; (2) explica en dos oraciones por qué la actividad física intensa necesita más oxígeno; (3) nombra dos límites del modelo de balance.",
        "(1) 2.400 menos 2.600 son −200 kcal. (2) El músculo gasta más ATP y el ATP se produce sobre todo con oxígeno en las mitocondrias, por eso el corazón y los pulmones llevan más oxígeno. (3) El cuerpo regula el hambre y el gasto, y las personas son distintas.",
        ["balance calculado con el signo correcto", "explicación que relaciona ATP y oxígeno", "dos límites reales del modelo", "no da consejos personales"],
        ["tres partes numeradas"],
        ["restar al revés", "decir que sin oxígeno no hay energía", "usar el modelo como receta"],
        "Pregunta: «¿qué dato tendrías que agregar al modelo para acercarlo a una persona real?»."),
    reinforce="Con otros números de ejemplo, calcula un balance positivo y uno negativo y explica qué significa cada uno según el modelo.",
    extend="Explica por qué la misma cantidad de glucosa rinde distinto ATP con y sin oxígeno y cómo eso se relaciona con el ejercicio.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 14 (tabla de ejemplo de un estudio observacional con 4.000 adolescentes ficticios). Puntaje de bienestar de 0 a 100, según los minutos de actividad física moderada a la semana: "
     "menos de 60 minutos: 55 puntos; de 60 a 149 minutos: 62 puntos; de 150 a 299 minutos: 68 puntos; 300 minutos o más: 69 puntos. "
     "Nota: el bienestar se midió con un cuestionario anónimo. Es posible que las personas con mejor ánimo hagan más actividad, y no solo al revés.")
build(
    O3, 4, F,
    use="Aprenderé a analizar evidencia sobre actividad física y bienestar, a reconocer cuando una relación se aplana y a considerar que la causalidad puede ir en ambos sentidos. Sirve para leer tablas sobre hábitos sin exagerar.",
    prior=["Sé calcular diferencias.", "Sé leer una tabla con grupos ordenados.", "Sé que una asociación no prueba una causa."],
    explain=[
        "Cuando se analiza evidencia se busca un patrón. En la ficha, el bienestar sube a medida que aumentan los minutos de actividad: 55, 62, 68 y 69. A esto se le llama relación dosis-respuesta: a mayor cantidad del hábito, mayor efecto. Es un indicio a favor de una causa. Pero la relación puede aplanarse: del segundo al tercer grupo el aumento es de 6 puntos, pero del tercero al cuarto solo es de 1 punto.",
        "También hay que preguntar en qué dirección va la causa. Puede ser que la actividad mejore el bienestar, pero también que quienes tienen mejor ánimo hagan más actividad. Esto se llama causalidad inversa. Además, pueden existir variables confusoras, como el ingreso familiar, el tiempo libre o el acceso a espacios deportivos. Un estudio observacional no resuelve esto por sí solo.",
        "Para fortalecer una conclusión se busca coincidencia con otros estudios, un orden temporal claro, un mecanismo plausible (por ejemplo, cambios fisiológicos y celulares con el ejercicio) y datos de personas diversas. La conclusión se redacta con cuidado: «se asocia con», «es compatible con», y con los límites a la vista. Los datos son de ejemplo y no indican cuánto debe hacer cada persona.",
    ],
    vocab=[("relación dosis-respuesta", "patrón en que a mayor cantidad del hábito se observa mayor efecto"), ("causalidad inversa", "situación en que el supuesto efecto es en realidad la causa"), ("aplanamiento", "momento en que el aumento del efecto se hace mucho menor"), ("orden temporal", "la causa ocurre antes que el efecto"), ("bienestar", "estado de ánimo, energía y satisfacción con la vida que una persona declara")],
    worked=[
        ("Calcular el cambio entre grupos", "En una tabla de ejemplo, el bienestar es 50 con 0 minutos y 58 con 100 minutos. ¿Cuánto aumenta?",
         ["Se resta el valor inicial al final: 58 menos 50.", "El aumento es de 8 puntos."],
         "8 puntos"),
        ("Reconocer causalidad inversa", "En una encuesta de ejemplo, las personas con mejor ánimo hacen más deporte. ¿Qué explicación alternativa a «el deporte mejora el ánimo» aparece?",
         ["Puede ser que el buen ánimo lleve a hacer más deporte.", "A eso se le llama causalidad inversa."],
         "Causalidad inversa"),
    ],
    mistakes=[("Concluir que más actividad siempre da más bienestar sin límite.", "La tabla muestra que la relación se aplana, y el estudio no probó que más siempre sea mejor.", "Describe el patrón completo, incluido el aplanamiento."),
              ("Olvidar que la causalidad puede ir al revés.", "Las personas con buen ánimo pueden hacer más actividad.", "Considera ambos sentidos antes de afirmar una causa.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la causalidad inversa?", "Cuando el supuesto efecto es en realidad la causa", "Cuando un estudio se hace dos veces", "Cuando no hay datos", "La causalidad inversa invierte el sentido de la relación que se suponía."),
        ("{F} ¿Cuál es el puntaje de bienestar del grupo que hace menos de 60 minutos a la semana?", "55 puntos", "La tabla de la ficha indica 55 puntos."),
        ("ab", "{F} El patrón de la tabla, en que a más minutos hay más bienestar, es:", "Una relación dosis-respuesta", "Una relación sin orden", "A mayor cantidad del hábito se observa mayor efecto, lo que se llama dosis-respuesta."),
        ("=", "{F} ¿Cuántos puntos más de bienestar tiene el grupo de 150 a 299 minutos que el de menos de 60?", "68-55", "La diferencia entre 68 y 55 es de 13 puntos.", " puntos"),
        ("=", "{F} ¿Cuántos puntos de bienestar aumenta el grupo de 300 minutos o más respecto al de 150 a 299?", "69-68", "La diferencia entre 69 y 68 es de 1 punto.", " punto"),
        ("=", "{F} ¿Cuántos puntos aumenta el bienestar del grupo de 60 a 149 minutos respecto al de menos de 60?", "62-55", "La diferencia entre 62 y 55 es de 7 puntos.", " puntos"),
        ("abc", "{F} ¿Qué se observa al pasar del tercer al cuarto grupo?", "El aumento se aplana", "El bienestar baja mucho", "No hay ningún cambio en los datos", "Solo sube 1 punto, mucho menos que en los tramos anteriores."),
        ("abc", "{F} ¿Qué explicación alternativa menciona la nota de la ficha?", "Que las personas con mejor ánimo hagan más actividad", "Que la tabla tiene errores", "Que el cuestionario es muy largo", "La nota señala la posible causalidad inversa."),
        ("abc", "{F} Un estudiante dice: «la tabla prueba que la actividad física causa el bienestar». ¿Qué respondes?", "Que es una asociación compatible con una causa, pero hay que descartar la causalidad inversa y las confusoras", "Que es una causa demostrada", "Que no tiene ninguna relación", "El estudio es observacional y no resuelve el sentido de la relación."),
        ("abc", "{F} ¿Qué variable confusora posible podría influir en la actividad y en el bienestar?", "El acceso a espacios deportivos y el tiempo libre", "El color de la tabla", "El número de preguntas del cuestionario", "El acceso a espacios y el tiempo libre pueden influir en ambas variables."),
        ("abc", "{F} ¿Qué evidencia fortalecería más una conclusión causal?", "Un experimento con asignación al azar y un mecanismo plausible", "Otra tabla con los mismos datos", "Una opinión de un amigo", "Un experimento controla confusoras, y el mecanismo explica el efecto."),
        ("abc", "{F} Un alcalde de ejemplo propone mejorar canchas y espacios públicos. ¿Con qué parte de la evidencia se relaciona mejor?", "Con la posibilidad de aumentar la actividad de muchas personas, reduciendo barreras de acceso", "Con que nadie necesita actividad", "Con que la tabla prueba que solo importa el dinero", "Mejorar el acceso actúa sobre una confusora y sobre la actividad."),
        ("abc", "{F} Un joven ficticio con dolor o con una condición de salud se pregunta cuánta actividad debe hacer según la tabla. ¿Qué corresponde?", "Consultar a un profesional de salud, porque la tabla describe grupos y no sirve para decisiones personales", "Hacer 300 minutos sin consultar", "No hacer ninguna actividad", "Las decisiones sobre actividad física de una persona con una condición requieren orientación profesional."),
    ],
    ctx=("abc", "Contexto: se discute en tu curso si hay que agregar más clases de educación física. Alguien cita la tabla. ¿Qué argumento es más cuidadoso?", "La tabla es compatible con un beneficio de la actividad, aunque es observacional y habría que mirar más evidencia", "La tabla prueba que más educación física asegura el bienestar", "La tabla no dice nada", "El argumento usa la evidencia y reconoce sus límites."),
    sc=[
        ("En Ciencias de la salud: ¿qué es una relación dosis-respuesta?", "Un patrón en que a mayor cantidad del hábito hay mayor efecto", "Es un indicio a favor de una relación causal, pero no una prueba."),
        ("ab", "Si la relación se aplana, el efecto:", "Aumenta cada vez menos", "Sigue aumentando igual", "Aplanarse significa que cada aumento del hábito suma poco al efecto."),
        ("ab", "Un estudio observacional puede tener:", "Variables confusoras", "Asignación al azar", "Al no asignar al azar, otras variables pueden influir."),
    ],
    op=("Con la tabla de la ficha {F} haz lo siguiente: (1) calcula el aumento de bienestar entre cada grupo y el siguiente; (2) escribe una conclusión de dos oraciones que describa el patrón, incluido el aplanamiento; (3) nombra una explicación alternativa y qué estudio pedirías.",
        "(1) 7, 6 y 1 puntos. (2) El bienestar aumenta con la actividad, pero el aumento se aplana en el último tramo. Es compatible con un beneficio de la actividad, sin probar una causa. (3) Causalidad inversa: quienes están de buen ánimo hacen más actividad. Pediría un experimento con asignación al azar.",
        ["aumentos correctos entre grupos", "conclusión que incluye el aplanamiento", "explicación alternativa distinta de la causa directa", "estudio propuesto con asignación al azar o seguimiento"],
        ["tres partes numeradas"],
        ["decir que más siempre es mejor", "afirmar una causa", "no nombrar explicaciones alternativas"],
        "Pregunta: «¿qué haría cambiar tu conclusión si el último grupo fuera muy pequeño?»."),
    reinforce="Con una tabla de ejemplo de tres grupos, calcula los aumentos entre grupos y describe el patrón con una frase.",
    extend="Explica con un ejemplo propio una situación de causalidad inversa en salud y cómo un estudio podría distinguirla.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 15 (opciones de ejemplo para un liceo ficticio que quiere mejorar el bienestar de sus estudiantes). "
     "Opción A, pausas activas de 10 minutos en la jornada. Opción B, un kiosco con alimentos más saludables. Opción C, horario de entrada una hora más tarde. Opción D, una charla informativa única. "
     "Puntajes de 1 a 3 (3 es mejor) en tres criterios: efecto esperado según la evidencia, alcance (a cuántos estudiantes llega) y costo accesible. "
     "A: efecto 2, alcance 3, costo 3. B: efecto 2, alcance 2, costo 2. C: efecto 3, alcance 3, costo 1. D: efecto 1, alcance 1, costo 3. "
     "Pesos de los criterios en el primer análisis: efecto 3, alcance 2, costo 1.")
build(
    O3, 5, F,
    use="Aprenderé a comparar medidas que promueven estilos de vida saludables con una matriz de criterios y pesos, y a ver cómo cambia la decisión si cambian los pesos. Sirve para tomar decisiones colectivas con razones y no por costumbre.",
    prior=["Sé multiplicar y sumar.", "Sé comparar opciones con criterios.", "Sé qué es una asociación."],
    explain=[
        "Los estilos de vida de una población dependen de las personas, pero también del entorno: los horarios, la oferta de alimentos, los espacios para el movimiento y la información disponible. Por eso las medidas más efectivas suelen actuar sobre el entorno y no solo pedir a cada persona que cambie. Para comparar medidas se usa una matriz con criterios y puntajes.",
        "En una matriz con pesos, cada criterio tiene un peso que dice cuánto importa. Se multiplica el puntaje de cada opción por el peso del criterio y se suman los productos. Con pesos 3, 2 y 1, la opción A suma 2 por 3, más 3 por 2, más 3 por 1, es decir, 15 puntos. El resultado depende de los pesos: otras personas pueden valorar más el costo y el ranking cambiaría.",
        "Por eso se hace un análisis de sensibilidad: se cambian los pesos y se mira si la decisión se mantiene. Una decisión robusta no cambia con pequeños cambios de peso. Además, se miran los efectos no previstos, como una medida que beneficia a unos y deja fuera a otros, y se acuerda cómo evaluar el resultado después. Las medidas colectivas se complementan con la orientación personal de profesionales de salud.",
    ],
    vocab=[("matriz de decisión", "tabla que compara opciones con criterios y puntajes"), ("peso", "número que indica cuánto importa un criterio"), ("análisis de sensibilidad", "revisión de si la decisión cambia al cambiar los pesos o supuestos"), ("entorno", "condiciones del lugar donde vive la gente, como horarios, oferta y espacios"), ("efecto no previsto", "consecuencia que no se había pensado al elegir una medida")],
    worked=[
        ("Calcular un puntaje con pesos", "Una opción de ejemplo tiene puntajes 3, 1 y 2 en tres criterios con pesos 2, 2 y 1. ¿Cuántos puntos suma?",
         ["Se multiplica cada puntaje por su peso: 3 por 2 es 6, 1 por 2 es 2 y 2 por 1 es 2.", "Se suman: 6 más 2 más 2."],
         "10 puntos"),
        ("Cambiar los pesos", "La misma opción con pesos 1, 1 y 3, ¿cuántos puntos suma?",
         ["3 por 1 es 3, 1 por 1 es 1 y 2 por 3 es 6.", "Se suman: 3 más 1 más 6."],
         "10 puntos, la misma cantidad con otros pesos"),
    ],
    mistakes=[("Elegir sin explicar los pesos de los criterios.", "El ranking depende de los pesos, y quienes deciden pueden tener distintos valores.", "Muestra los pesos y prueba cómo cambia el resultado."),
              ("Creer que una charla informativa basta para cambiar hábitos.", "Los hábitos dependen mucho del entorno, además de la información.", "Combina información con cambios del entorno.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es el análisis de sensibilidad?", "Revisar si la decisión cambia al cambiar los pesos o los supuestos", "Medir la sensibilidad de la piel", "Elegir la opción más cara", "Sirve para saber si la decisión es robusta."),
        ("{F} ¿Qué opción tiene el mejor puntaje de efecto esperado?", "Opción C", "La ficha da puntaje 3 en efecto a la opción C."),
        ("ab", "Las medidas que cambian el entorno, como los horarios o la oferta de alimentos:", "Llegan a más personas sin depender de la decisión de cada una", "Solo sirven para una persona", "Un cambio del entorno alcanza a toda la población que lo usa."),
        ("=", "{F} Con los pesos 3, 2 y 1, ¿cuántos puntos suma la opción A?", "2*3+3*2+3*1", "Se multiplica cada puntaje por su peso y se suma: 6, 6 y 3.", " puntos"),
        ("=", "{F} Con los pesos 3, 2 y 1, ¿cuántos puntos suma la opción B?", "2*3+2*2+2*1", "Se suman 6, 4 y 2.", " puntos"),
        ("=", "{F} Con los pesos 3, 2 y 1, ¿cuántos puntos suma la opción C?", "3*3+3*2+1*1", "Se suman 9, 6 y 1.", " puntos"),
        ("=", "{F} Con los pesos 3, 2 y 1, ¿cuántos puntos suma la opción D?", "1*3+1*2+3*1", "Se suman 3, 2 y 3.", " puntos"),
        ("abc", "{F} Con los pesos 3, 2 y 1, ¿qué opción queda primera?", "Opción C", "Opción A", "Opción D", "C suma 16, A suma 15, B suma 12 y D suma 8."),
        ("=", "{F} Si los pesos cambian a efecto 1, alcance 2 y costo 3, ¿cuántos puntos suma la opción A?", "2*1+3*2+3*3", "Se suman 2, 6 y 9.", " puntos"),
        ("abc", "{F} Con los pesos efecto 1, alcance 2 y costo 3, A suma 17, B suma 12, C suma 12 y D suma 12. ¿Qué conclusión sacas?", "Que la decisión depende de los pesos, y la opción A es robusta en ambos análisis", "Que el análisis no sirve", "Que la opción C es siempre mala", "A queda primera o segunda con ambos pesos, lo que la hace robusta."),
        ("abc", "{F} ¿Qué efecto no previsto podría tener la opción C?", "Dificultades para estudiantes que dependen del transporte a esa hora", "Que desaparezca el liceo", "Que nadie duerma", "Un cambio de horario puede afectar a quienes dependen de buses o del trabajo familiar."),
        ("abc", "{F} Una estudiante dice: «con las pausas activas basta, no hay que informar a nadie». ¿Qué respondes?", "Que la información ayuda a entender el porqué de las pausas y puede complementar el cambio del entorno", "Que la información no sirve", "Que las pausas no sirven", "Las medidas del entorno y la información se complementan."),
        ("abc", "{F} Para decidir con una matriz de forma justa, ¿qué conviene hacer?", "Acordar los pesos entre estudiantes, docentes y familias y mostrar cómo cambia el resultado", "Que decida una sola persona", "Esconder los pesos", "Los pesos reflejan valores, y es mejor acordarlos y transparentarlos."),
    ],
    ctx=("abc", "Contexto: el centro de estudiantes debe escoger una medida con un presupuesto pequeño. ¿Qué paso es más adecuado?", "Aplicar la matriz con pesos acordados y revisar cómo cambia el resultado si cambian los pesos", "Elegir lo que más le gusta a la directiva", "Elegir lo más barato siempre", "La matriz con sensibilidad ordena la discusión y la hace transparente."),
    sc=[
        ("En Ciencias de la salud: ¿qué es el peso de un criterio?", "Un número que indica cuánto importa ese criterio", "Los pesos reflejan valores y prioridades."),
        ("ab", "Una decisión robusta:", "Se mantiene aunque cambien un poco los pesos", "Cambia con cualquier peso", "Robusta significa estable ante cambios pequeños de supuestos."),
        ("ab", "Las medidas del entorno suelen:", "Llegar a más personas", "Llegar a nadie", "Cambian las condiciones para todos quienes usan el espacio."),
    ],
    op=("Con la matriz de la ficha {F} haz lo siguiente: (1) calcula el puntaje de cada opción con los pesos 2, 2 y 2 (todos iguales); (2) compara el ranking con el del análisis de pesos 3, 2 y 1; (3) elige una opción y nombra un efecto no previsto y cómo lo vigilarías.",
        "(1) A: 16. B: 12. C: 14. D: 10. (2) Con pesos iguales A queda primera y C segunda, mientras que con 3, 2 y 1 C quedaba primera y A segunda. (3) Elijo A, porque es primera con pesos iguales y segunda con los pesos originales. Efecto no previsto: que algunos estudiantes no participen. Lo vigilaría con una encuesta breve.",
        ["puntajes correctos con pesos iguales", "compara dos rankings", "elige con razones", "nombra un efecto no previsto y cómo vigilarlo"],
        ["tres partes numeradas"],
        ["no multiplicar por los pesos", "no comparar los análisis", "no considerar efectos no previstos"],
        "Pregunta: «¿qué opción combinarías con la que elegiste para cubrir una limitación?»."),
    reinforce="Elige tres criterios propios y puntúa dos opciones de ejemplo para mejorar el bienestar escolar. Calcula los puntajes con pesos que tú definas.",
    extend="Explica por qué dos grupos de personas pueden elegir opciones distintas con la misma matriz y qué se puede hacer para decidir de manera justa.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 16 (caso de ejemplo en una ciudad ficticia, Valle Claro). "
     "En invierno, muchas casas de Valle Claro se calientan con leña, y el humo aumenta la cantidad de material particulado en el aire. Material particulado es el conjunto de partículas muy pequeñas suspendidas en el aire; PM2.5 son las partículas de menos de 2,5 micrómetros de diámetro. "
     "Cadena de exposición: fuente (la combustión de leña) → medio (el aire) → vía de exposición (inhalación) → órgano (las vías respiratorias) → efecto (por ejemplo, más consultas por problemas respiratorios). "
     "Otros medios del caso: el agua del pozo de un sector rural puede tener un metal tóxico natural, que se ingiere al beber; el suelo cercano a una faena minera antigua puede tener metales que se contactan o se ingieren con el polvo. "
     "Concentración: cantidad de una sustancia por volumen, por ejemplo microgramos por metro cúbico (µg/m³) en el aire. Un microgramo es una millonésima de gramo.")
build(
    O4, 1, F,
    use="Aprenderé a delimitar un problema de ambiente y salud usando la cadena de exposición: fuente, medio, vía, órgano y efecto. Sirve para elegir una pregunta que se pueda investigar con datos sobre el aire, el agua o el suelo.",
    prior=["Sé que el aire, el agua y el suelo pueden contener sustancias que dañan.", "Sé leer unidades de medida.", "Sé formular una pregunta con variables."],
    explain=[
        "La calidad del aire, de las aguas y de los suelos influye en la salud humana. Para estudiar esta relación se piensa en una cadena de exposición. Todo parte en una fuente de contaminación, como la combustión de leña, un relave o un vertido. El contaminante pasa a un medio, que puede ser el aire, el agua o el suelo, y llega a las personas por una vía de exposición: inhalación, ingestión o contacto con la piel. Después actúa en un órgano y produce un efecto.",
        "La exposición no depende solo de que el contaminante exista: depende de su concentración, del tiempo que la persona está expuesta y de quién es esa persona. Los niños, las personas mayores y quienes tienen enfermedades previas suelen ser más sensibles. Por eso se habla de poblaciones vulnerables. Si no hay vía de exposición, aunque haya contaminante, no hay riesgo para las personas.",
        "Una pregunta de investigación bien delimitada elige un medio, un contaminante, un grupo y un efecto medible: por ejemplo, «¿aumentan las consultas por problemas respiratorios en días con más PM2.5 en Valle Claro?». Comunicar bien la pregunta ayuda a que la comunidad entienda qué se va a medir y para qué. Los datos de este cuaderno son de ejemplo y no describen ninguna ciudad real.",
    ],
    vocab=[("contaminante", "sustancia que, en cierta concentración, puede dañar la salud o el ambiente"), ("vía de exposición", "camino por el que el contaminante llega al cuerpo: inhalación, ingestión o contacto"), ("concentración", "cantidad de una sustancia por unidad de volumen o de masa"), ("material particulado", "partículas muy pequeñas suspendidas en el aire"), ("población vulnerable", "grupo que sufre más daño por una misma exposición")],
    worked=[
        ("Reconocer la vía", "El agua de un pozo tiene un metal tóxico y una familia la bebe a diario. ¿Cuál es la vía de exposición?",
         ["La sustancia entra al cuerpo con el agua que se bebe.", "Eso se llama ingestión."],
         "Ingestión"),
        ("Cuándo no hay riesgo", "Hay un contaminante en el suelo de un terreno cerrado al que nadie entra ni cultiva. ¿Hay riesgo para las personas?",
         ["Sin vía de exposición, el contaminante no llega al cuerpo.", "El contaminante existe, pero el riesgo para las personas es muy bajo mientras nadie esté en contacto."],
         "Riesgo muy bajo mientras no haya vía de exposición"),
    ],
    mistakes=[("Creer que la presencia de un contaminante basta para que haya daño.", "Se necesita una vía de exposición, una concentración suficiente y tiempo de exposición.", "Revisa la cadena completa: fuente, medio, vía, órgano y efecto."),
              ("Plantear una pregunta sin medio, grupo ni efecto medible.", "Sin esos elementos no se puede responder con datos.", "Incluye un medio, un contaminante, un grupo y un efecto medible.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es una vía de exposición?", "El camino por el que un contaminante llega al cuerpo", "El lugar donde se fabrica el contaminante", "La unidad de medida de un contaminante", "La vía de exposición puede ser inhalación, ingestión o contacto."),
        ("{F} ¿Cuál es la fuente de contaminación en el caso del aire de Valle Claro?", "La combustión de leña", "La ficha indica la leña como fuente del humo."),
        ("ab", "{F} Beber agua de un pozo con un metal tóxico es una exposición por:", "Ingestión", "Inhalación", "La sustancia entra al cuerpo con el agua que se bebe, es decir, por ingestión."),
        ("abc", "{F} En el caso del aire de Valle Claro, ¿cuál es el órgano principal que actúa en la cadena?", "Las vías respiratorias", "El hígado", "La piel de las manos", "La inhalación lleva las partículas a las vías respiratorias."),
        ("=", "{F} En una sala de ejemplo de 100 m³ con una concentración de 40 µg/m³ de PM2.5, ¿cuántos microgramos de PM2.5 hay en el aire de la sala?", "40*100", "Se multiplica la concentración por el volumen: 40 por 100.", " µg"),
        ("=", "Un recipiente de ejemplo de agua de 5 litros tiene una concentración de 10 µg por litro de un metal. ¿Cuántos microgramos hay en total?", "10*5", "Se multiplica la concentración por el volumen: 10 por 5.", " µg"),
        ("abc", "{F} ¿Cuál es una pregunta bien delimitada sobre Valle Claro?", "¿Aumentan las consultas por problemas respiratorios en días con más PM2.5?", "¿Qué es el ambiente?", "¿Cómo se limpia todo el planeta?", "Elige un medio, un contaminante y un efecto medible."),
        ("abc", "{F} Una familia de Valle Claro vive lejos de la faena y nunca contacta el suelo contaminado. ¿Qué se puede decir del suelo para ella?", "Que no hay vía de exposición directa, así que el riesgo por esa vía es bajo", "Que igual está expuesta, porque el contaminante llega solo hasta su casa", "Que ningún suelo contaminado puede causar riesgo en ningún caso", "Sin contacto ni ingestión, el contaminante no llega al cuerpo por esa vía."),
        ("abc", "{F} ¿Por qué un niño podría ser más vulnerable a las partículas del aire?", "Porque respira más aire por cada kilo de peso y sus vías respiratorias aún se desarrollan", "Porque los niños siempre pasan más tiempo cerca de las fuentes de humo", "Porque el aire que respiran los niños tiene menos oxígeno", "Los niños son más vulnerables por su fisiología y su desarrollo."),
        ("abc", "{F} ¿Qué dato necesitas, además de la concentración, para evaluar la exposición?", "El tiempo que las personas están expuestas", "El color del humo", "El nombre del contaminante", "La exposición combina concentración y tiempo."),
        ("abc", "{F} Una vecina dice: «si en el aire de la ciudad hay PM2.5, todos se enferman». ¿Qué le respondes?", "Que depende de la concentración, del tiempo y de quién es la persona", "Que sí, siempre", "Que el PM2.5 es inofensivo", "El riesgo depende de varios factores y no solo de que exista el contaminante."),
        ("abc", "{F} ¿Qué medio y qué vía describe «el polvo del suelo cercano a la faena que se respira o se ingiere»?", "Suelo, por inhalación o ingestión", "Agua, por contacto", "Aire, por ingestión de alimentos", "El polvo del suelo puede entrar por la boca o por las vías respiratorias."),
        ("abc", "{F} Para comunicar la pregunta a la comunidad, ¿qué frase es más clara?", "Queremos saber si en los días con más humo hay más consultas por problemas respiratorios", "Estamos investigando varios temas", "Haremos un estudio de todo el ambiente", "Una frase clara dice qué se mide y para qué."),
    ],
    ctx=("abc", "Contexto: eres parte de un grupo del liceo que investiga la calidad del aire en tu ciudad. ¿Cuál es la mejor pregunta de partida?", "¿Hay más estudiantes con problemas respiratorios en los días con más material particulado?", "¿Es mala la contaminación?", "¿Por qué el humo existe?", "La pregunta nombra un medio, un contaminante, un grupo y un efecto medible."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la concentración de un contaminante?", "La cantidad de contaminante por unidad de volumen o de masa", "La concentración mide cuánto contaminante hay en cierta cantidad de aire, agua o suelo."),
        ("ab", "Sin vía de exposición, el riesgo para las personas es:", "Muy bajo", "El máximo posible", "El contaminante debe llegar al cuerpo para dañar."),
        ("ab", "Las poblaciones vulnerables son:", "Grupos que sufren más daño con la misma exposición", "Grupos que no se exponen", "Vulnerable describe a quienes son más sensibles."),
    ],
    op=("Con el caso de la ficha {F} haz lo siguiente: (1) elige uno de los tres medios (aire, agua o suelo) y escribe su cadena de exposición completa; (2) escribe una pregunta bien delimitada; (3) nombra un grupo vulnerable y por qué.",
        "(1) Aire: fuente leña, medio aire, vía inhalación, órgano vías respiratorias, efecto más consultas respiratorias. (2) «¿Aumentan las consultas por problemas respiratorios en los días con más PM2.5?» (3) Los niños, porque sus vías respiratorias aún se desarrollan.",
        ["cadena con las cinco partes", "pregunta con medio, grupo y efecto", "grupo vulnerable con una razón", "no da un diagnóstico personal"],
        ["tres partes numeradas"],
        ["omitir la vía de exposición", "hacer una pregunta sin efecto medible", "no justificar el grupo vulnerable"],
        "Pregunta: «¿qué dato de ejemplo medirías primero para responder tu pregunta?»."),
    reinforce="Elige otro contaminante de ejemplo y escribe su cadena de exposición con fuente, medio, vía, órgano y efecto.",
    extend="Explica por qué dos personas expuestas al mismo contaminante pueden tener riesgos distintos.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 17 (datos de ejemplo sobre agua y suelo, para evaluar fuentes y variables). "
     "Agua del pozo de un sector rural, contaminante X en µg por litro, tres muestras tomadas en meses distintos: 6, 14 y 10. Valor de referencia de ejemplo: 10 µg por litro. El laboratorio informa un margen de error de ±2. "
     "Suelo cercano a una faena minera antigua, un metal Y en mg por kg, cuatro puntos a distintas distancias de la faena: 100 m: 90; 500 m: 60; 1.000 m: 40; 2.000 m: 30. Valor de referencia de ejemplo: 60 mg por kg. "
     "Dos informes: el Informe 1 es de la municipalidad, con el método y el laboratorio descritos. El Informe 2 es un mensaje anónimo que dice «el agua de todo el valle está envenenada», sin datos.")
build(
    O4, 2, F,
    use="Aprenderé a evaluar datos de calidad de agua y suelo: cuántas muestras hay, cómo varían, qué indican las distancias y si una fuente explica su método. Sirve para no concluir con una sola muestra ni con un mensaje sin datos.",
    prior=["Sé calcular un promedio.", "Sé qué es un valor de referencia.", "Sé comparar un dato con una referencia."],
    explain=[
        "Un dato ambiental depende de cómo se tomó la muestra. Una sola muestra puede ser excepcional, porque la concentración varía con el tiempo y con el lugar. Por eso se toman varias muestras y se calcula un promedio, pero también se mira la variación. En la ficha, el agua del pozo tuvo 6, 14 y 10 µg por litro: el promedio es 10, igual a la referencia, pero una muestra superó el valor.",
        "Todo instrumento tiene un margen de error. Si el laboratorio informa ±2, una medición de 10 podría estar entre 8 y 12. Un valor de referencia es un número que se usa como señal de alerta, definido por organismos de salud; superarlo no significa que alguien se enferme, y no superarlo no garantiza seguridad total. En el suelo, la concentración baja al alejarse de la faena, lo que sugiere que la faena es la fuente.",
        "También se evalúa la fuente de la información: quién tomó las muestras, con qué método, en qué lugares y por qué. Un informe con método y laboratorio descritos se puede revisar. Un mensaje sin datos no. Una buena evaluación declara qué falta: más muestras, otras épocas, otros puntos y datos de salud de la población. Y no culpa a personas ni genera alarma sin respaldo.",
    ],
    vocab=[("muestra", "porción de agua, suelo o aire que se toma para medir"), ("valor de referencia", "número que se usa como señal de alerta definida por organismos de salud"), ("margen de error", "intervalo dentro del cual puede estar el valor real de una medición"), ("gradiente", "cambio gradual de un valor a medida que cambia la distancia"), ("promedio", "suma de los valores dividida por el número de valores")],
    worked=[
        ("Promedio de muestras", "Tres muestras de ejemplo dan 4, 8 y 12. ¿Cuál es el promedio?",
         ["Se suman los valores: 4 más 8 más 12 son 24.", "Se divide entre 3."],
         "8"),
        ("Usar el margen de error", "Una medición de ejemplo es 20 con un margen de ±3 y la referencia es 22. ¿Se puede asegurar que está bajo la referencia?",
         ["El valor real podría estar entre 17 y 23.", "El 23 supera la referencia de 22."],
         "No se puede asegurar"),
    ],
    mistakes=[("Concluir con una sola muestra.", "La concentración varía en el tiempo y en el lugar.", "Toma varias muestras y observa la variación."),
              ("Creer que superar el valor de referencia significa enfermedad.", "La referencia es una señal de alerta y no un diagnóstico.", "Úsalo para priorizar acciones y buscar más datos.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es un valor de referencia?", "Un número que se usa como señal de alerta definida por organismos de salud", "El valor que tiene siempre un contaminante", "La edad de la muestra", "La referencia ayuda a decidir si hay que actuar o investigar más."),
        ("=", "{F} ¿Cuál es el promedio de las tres muestras de agua del pozo?", "(6+14+10)/3", "La suma es 30 y se divide entre 3.", " µg por litro"),
        ("ab", "{F} Una de las tres muestras de agua superó la referencia de 10. ¿Cuál fue?", "La de 14", "La de 6", "Solo 14 es mayor que 10; 6 es menor y 10 es igual."),
        ("abc", "{F} Una muestra de agua dio 10 con un margen de ±2. ¿Entre qué valores puede estar el valor real?", "Entre 8 y 12", "Entre 10 y 12", "Entre 0 y 10", "El margen ±2 se resta y se suma al valor medido."),
        ("=", "{F} En el suelo, ¿cuántos mg por kg baja la concentración desde los 100 m hasta los 2.000 m?", "90-30", "Pasa de 90 a 30, una baja de 60.", " mg por kg"),
        ("abc", "{F} ¿En cuál de los cuatro puntos se supera el valor de referencia de 60 mg por kg?", "Solo en el de 100 m", "En los cuatro puntos", "En ninguno", "El punto a 100 m tiene 90; el de 500 m tiene 60, que es igual a la referencia y no la supera."),
        ("abc", "{F} ¿Qué sugiere que la concentración baje al alejarse de la faena?", "Que la faena es la fuente probable del metal Y", "Que el metal Y no existe", "Que el suelo no se mide", "Un gradiente que baja con la distancia apunta a la fuente."),
        ("abc", "{F} ¿Qué informe (1 o 2) permite revisar el método y repetir las mediciones?", "Informe 1", "Informe 2", "Los dos por igual", "El Informe 1 describe el método y el laboratorio."),
        ("abc", "{F} ¿Qué falta en el Informe 2 para evaluarlo?", "Datos, método y lugares medidos", "Más adjetivos", "Más personas que lo compartan", "Sin datos ni método no se puede revisar."),
        ("abc", "{F} Alguien afirma: «con una muestra de 14 se prueba que el pozo es peligroso». ¿Qué respondes?", "Que hay que mirar las tres muestras y su margen de error, y consultar a la autoridad sanitaria", "Que es peligroso con seguridad", "Que el pozo no tiene ningún riesgo", "Una sola muestra no basta, y las decisiones las toma la autoridad con más datos."),
        ("abc", "{F} Para mejorar el estudio del pozo, ¿qué agregarías?", "Más muestras en distintas épocas y un laboratorio con método descrito", "Una sola muestra más grande", "Quitar el valor de 14", "Más muestras en el tiempo permiten ver la variación."),
        ("abc", "{F} El promedio del agua es igual a la referencia. ¿Qué ocultaría usar solo el promedio?", "Que una de las muestras superó la referencia", "Que hay tres muestras", "Que el agua es transparente", "El promedio esconde la variación entre muestras."),
        ("abc", "{F} Una familia que usa el pozo se preocupa. ¿Qué corresponde según este cuaderno?", "Contactar a la autoridad sanitaria o a un profesional de salud para recibir orientación", "Seguir bebiendo y esperar a ver si alguien se enferma", "Compartir el resultado en redes sin consultar a nadie", "Las decisiones sobre agua de consumo las orienta la autoridad o un profesional, no un ensayo casero."),
    ],
    ctx=("abc", "Contexto: en la radio local alguien dice «el suelo del pueblo está contaminado» y cita un solo punto de medición. ¿Qué pregunta haces?", "¿Cuántos puntos se midieron, con qué método y con qué referencia se comparó?", "¿Quién lo dijo más fuerte?", "¿Cuántas personas lo escucharon?", "Preguntar por puntos, método y referencia permite evaluar el dato."),
    sc=[
        ("En Ciencias de la salud: ¿qué es el margen de error de una medición?", "El intervalo en que puede estar el valor real", "El margen indica la incertidumbre de la medición."),
        ("ab", "Una sola muestra ambiental:", "Puede no representar el lugar ni el tiempo", "Siempre representa todo", "La concentración varía y una muestra no basta."),
        ("ab", "Superar un valor de referencia indica:", "Una señal de alerta para investigar", "Un diagnóstico de enfermedad", "La referencia orienta acciones y no diagnostica a nadie."),
    ],
    op=("Con los datos de la ficha {F} haz lo siguiente: (1) calcula el promedio del agua y di cuántas muestras superan la referencia; (2) describe el patrón del suelo con la distancia y qué sugiere; (3) evalúa los dos informes con una frase cada uno y di qué datos faltan.",
        "(1) Promedio 10 µg por litro y una muestra supera la referencia. (2) La concentración baja de 90 a 30 al alejarse, lo que sugiere que la faena es la fuente. (3) El Informe 1 describe su método, así que es revisable. El Informe 2 no tiene datos. Faltan más muestras en el tiempo y datos de salud.",
        ["promedio y conteo correctos", "describe el gradiente del suelo", "evalúa ambos informes con criterio", "nombra datos que faltan"],
        ["tres partes numeradas"],
        ["usar solo el promedio", "olvidar el margen de error", "creer en un informe sin datos"],
        "Pregunta: «¿qué punto de muestreo agregarías para entender mejor el suelo?»."),
    reinforce="Con tres muestras de ejemplo propias calcula el promedio y escribe si alguna supera una referencia que tú inventes y rotules.",
    extend="Explica por qué es importante tomar muestras en distintas épocas al evaluar la calidad del agua.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 18 (dos modelos de ejemplo de mecanismos biológicos). "
     "Modelo del aire: al respirar, las partículas grandes se quedan en la nariz y las vías altas; las partículas muy finas, como las PM2.5, llegan más profundo, hasta los alvéolos, que son los sacos donde ocurre el intercambio de gases. Las células de defensa responden y producen inflamación, que puede dificultar el paso del oxígeno. "
     "Modelo del agua y el suelo: un metal tóxico del agua entra a las algas; cada nivel de la cadena alimentaria acumula más. En unidades de ejemplo: algas 1; peces pequeños 10; peces grandes 100. A este aumento a lo largo de la cadena se le llama biomagnificación. "
     "A nivel molecular, un metal tóxico puede unirse a proteínas y alterar su función.")
build(
    O4, 3, F,
    use="Aprenderé a interpretar modelos de mecanismos biológicos con los que un contaminante del aire, del agua o del suelo puede dañar el cuerpo. Sirve para dar una explicación posible de por qué ciertas exposiciones se relacionan con efectos en la salud.",
    prior=["Sé que los pulmones intercambian gases en los alvéolos.", "Sé que las proteínas cumplen funciones en las células.", "Sé qué es una cadena alimentaria."],
    explain=[
        "Un mecanismo biológico explica cómo una exposición llega a producir un efecto. En el aire, el tamaño de las partículas importa: las más grandes quedan atrapadas en la nariz y la garganta; las muy finas, como las PM2.5, penetran hasta los alvéolos, donde ocurre el intercambio de gases. Allí las células de defensa reaccionan y producen inflamación, y esa respuesta puede dificultar la respiración, sobre todo en personas con asma u otras enfermedades.",
        "En el agua y el suelo, algunos contaminantes se acumulan en los seres vivos. La bioacumulación es el aumento de la concentración de una sustancia en un organismo a lo largo del tiempo, y la biomagnificación es su aumento a lo largo de la cadena alimentaria: cada nivel contiene más que el anterior. Por eso consumir organismos de niveles altos de la cadena puede significar mayor exposición a algunos metales que beber el agua.",
        "A escala molecular, un metal tóxico puede unirse a proteínas y alterar su función, como cuando una enzima deja de trabajar. Un modelo ayuda a explicar, pero tiene límites: no dice cuánta exposición es necesaria ni cuántas personas se verán afectadas. Para eso hacen falta datos. Cuando un mecanismo y los datos coinciden, la evidencia causal es más fuerte.",
    ],
    vocab=[("alvéolo", "saco pequeño del pulmón donde ocurre el intercambio de gases"), ("inflamación", "respuesta de defensa del cuerpo que enrojece, hincha y puede dificultar una función"), ("bioacumulación", "aumento de una sustancia en un organismo a lo largo del tiempo"), ("biomagnificación", "aumento de una sustancia a lo largo de la cadena alimentaria"), ("mecanismo biológico", "explicación de cómo una exposición produce un efecto en el cuerpo")],
    worked=[
        ("Seguir la cadena de bioacumulación", "En unidades de ejemplo de otro lago, las algas tienen 10 y cada nivel siguiente acumula 5 veces más que el anterior. ¿Cuánto hay en los peces pequeños, que son el nivel siguiente a las algas?",
         ["Los peces pequeños son el nivel que sigue a las algas.", "Se multiplica el valor de las algas por 5: 10 por 5."],
         "50 unidades"),
        ("Tamaño y profundidad", "Si una partícula es muy fina y llega a los alvéolos, ¿en qué parte del cuerpo puede interferir con el intercambio de gases?",
         ["Los alvéolos son los sacos donde ocurre el intercambio de gases.", "La inflamación allí dificulta el paso del oxígeno."],
         "En los pulmones, en los alvéolos"),
    ],
    mistakes=[("Creer que todas las partículas del aire llegan igual de profundo.", "El tamaño determina hasta dónde llegan: las finas llegan más profundo.", "Relaciona el tamaño con la zona del aparato respiratorio a la que llegan."),
              ("Confundir presencia de un metal en el agua con la exposición total de una persona.", "La exposición también depende de la cadena alimentaria y de lo que se consume.", "Revisa todas las vías, incluidos los alimentos.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la bioacumulación?", "El aumento de una sustancia en un organismo a lo largo del tiempo", "La pérdida de una sustancia en el agua", "El crecimiento de una planta", "Bioacumulación es acumular una sustancia en el cuerpo del organismo."),
        ("{F} ¿Dónde ocurre el intercambio de gases en los pulmones?", "En los alvéolos", "La ficha define los alvéolos como los sacos donde ocurre el intercambio de gases."),
        ("ab", "{F} Las partículas más finas, como las PM2.5:", "Llegan más profundo en los pulmones", "Quedan en la nariz", "El tamaño pequeño les permite pasar las vías altas y llegar a los alvéolos."),
        ("abc", "{F} ¿Cuál es el efecto de la inflamación en los alvéolos?", "Puede dificultar el paso del oxígeno", "Aumenta siempre el oxígeno", "Destruye todos los pulmones", "La inflamación puede dificultar el intercambio de gases."),
        ("=", "{F} En el modelo de ejemplo, ¿cuántas veces más hay en los peces grandes que en los peces pequeños?", "100/10", "Los peces grandes tienen 100 y los pequeños 10.", " veces"),
        ("=", "{F} En unidades de ejemplo, si cada nivel multiplica por 10 y los peces grandes tienen 100, ¿cuánto tendría un ave que se alimenta de los peces grandes, un nivel más arriba?", "100*10", "Se multiplica por 10 un nivel más.", " unidades"),
        ("abc", "{F} Una familia come con frecuencia peces grandes de un lago con un metal tóxico en el agua. ¿Qué dice el modelo?", "Que su exposición por alimentos puede ser mayor que por beber el agua", "Que no hay exposición", "Que el metal desaparece al cocinar", "La biomagnificación concentra el metal en los niveles altos de la cadena."),
        ("abc", "{F} ¿Cómo explica el modelo molecular el daño de un metal tóxico?", "Se une a proteínas y altera su función", "Convierte el agua en otra sustancia", "Impide que existan las proteínas", "Si una proteína deja de funcionar bien, la célula se afecta."),
        ("abc", "{F} ¿Qué población podría sentir más el efecto de la inflamación en los alvéolos?", "Personas con asma u otras enfermedades respiratorias", "Todas por igual siempre", "Nadie", "Quienes ya tienen vías respiratorias sensibles tienen más riesgo."),
        ("abc", "{F} ¿Qué no dice el modelo del aire?", "Cuánta exposición produce un efecto ni cuántas personas serán afectadas", "Que las partículas tienen tamaño", "Que existen los alvéolos", "Los modelos de mecanismo no dan cantidades, que hay que medir."),
        ("abc", "{F} Si un estudio muestra más consultas respiratorias en días con más PM2.5, ¿cómo ayuda el modelo?", "Aporta una explicación posible de por qué ocurre la relación", "Demuestra por sí solo la causa", "Anula el estudio", "El mecanismo y los datos que coinciden fortalecen la evidencia causal."),
        ("abc", "{F} Dos lagos tienen la misma concentración del metal en el agua. En uno hay una cadena alimentaria larga y en otro corta. ¿En qué lago habría peces con más metal?", "En el de cadena larga, por la biomagnificación", "En el de cadena corta", "En ambos igual", "Más niveles permiten más aumento acumulado."),
        ("abc", "Una familia de ejemplo que vive cerca de un lago contaminado tiene dudas. ¿Qué corresponde?", "Consultar a la autoridad sanitaria o a un profesional de salud sobre el consumo de los peces", "Decidir por el sabor y el aspecto de los peces", "Ignorar el tema", "Las decisiones sobre consumo de alimentos con contaminantes las orienta la autoridad sanitaria."),
    ],
    ctx=("abc", "Contexto: te piden explicar en un afiche por qué las partículas finas son especialmente dañinas. ¿Qué incluyes?", "Que llegan hasta los alvéolos, donde pueden causar inflamación y dificultar el intercambio de gases", "Que son visibles a simple vista", "Que solo afectan la nariz", "El afiche explica el mecanismo con el tamaño, la zona del pulmón y el efecto."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un mecanismo biológico?", "La explicación de cómo una exposición produce un efecto en el cuerpo", "El mecanismo une la causa y el efecto con pasos biológicos."),
        ("ab", "La biomagnificación ocurre:", "A lo largo de la cadena alimentaria", "En una sola célula", "Cada nivel acumula más que el anterior."),
        ("ab", "Las partículas más finas llegan:", "Más profundo en los pulmones", "Solo a la nariz", "Su tamaño pequeño les permite llegar a los alvéolos."),
    ],
    op=("Con los modelos de la ficha {F} haz lo siguiente: (1) dibuja el mecanismo del aire en cuatro pasos con flechas; (2) calcula cuántas veces más hay en los peces grandes que en las algas; (3) escribe un límite de estos modelos.",
        "(1) Partículas finas → llegan a los alvéolos → las células de defensa producen inflamación → se dificulta el paso del oxígeno. (2) 100 veces más. (3) No dicen cuánta exposición produce un efecto ni cuántas personas se afectarán.",
        ["cuatro pasos en orden", "cálculo correcto", "un límite razonable", "usa el vocabulario de la clase"],
        ["tres partes numeradas"],
        ["omitir el tamaño de la partícula", "confundir bioacumulación con biomagnificación", "no nombrar un límite"],
        "Pregunta: «¿qué dato medirías para saber cuánta exposición produce un efecto?»."),
    reinforce="Escribe con tus palabras la diferencia entre bioacumulación y biomagnificación, con un ejemplo.",
    extend="Explica por qué un mecanismo biológico plausible aumenta la confianza en una relación entre exposición y efecto, pero no basta por sí solo.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 19 (tabla de ejemplo de Valle Claro). Promedio diario de PM2.5 en µg/m³ y consultas diarias por problemas respiratorios en un centro de salud ficticio, durante 120 días de invierno. "
     "PM2.5 menor de 20: 40 consultas al día. De 20 a 39: 55 consultas al día. De 40 a 59: 80 consultas al día. De 60 o más: 120 consultas al día. "
     "Notas: en días muy fríos también hay más virus respiratorios circulando y más gente en espacios cerrados. Las consultas del día suelen subir uno a dos días después de un pico de PM2.5.")
build(
    O4, 4, F,
    use="Aprenderé a analizar evidencia que relaciona la calidad del aire con la salud, reconociendo gradientes, desfases en el tiempo y variables confusoras como el frío. Sirve para decidir qué se puede decir con una tabla y qué no.",
    prior=["Sé calcular diferencias y porcentajes.", "Sé qué es una variable confusora.", "Sé qué es una relación dosis-respuesta."],
    explain=[
        "La tabla de la ficha muestra una relación dosis-respuesta: a medida que sube la concentración de PM2.5, aumentan las consultas por problemas respiratorios, de 40 a 120 al día. Es un indicio a favor de una causa. Para saber cuánto aumentan se compara con un grupo de referencia: pasar de 40 a 80 consultas es un aumento de 40 consultas, es decir, 100 %, el doble.",
        "Pero hay que revisar otras explicaciones. En invierno hace frío, circulan más virus y la gente está más tiempo en espacios cerrados, y todo eso puede aumentar las consultas aunque el aire no cambie. Esas son variables confusoras. Para controlar su efecto, los estudios comparan días con la misma temperatura, o ajustan estadísticamente por el frío y los virus. También importa el orden temporal: si las consultas suben uno a dos días después del pico de PM2.5, eso es coherente con una causa.",
        "Una conclusión sólida suma varios elementos: gradiente, orden en el tiempo, mecanismo biológico plausible, coincidencia con otros estudios y control de confusoras. Una conclusión se redacta con lenguaje cuidadoso, por ejemplo «los datos son compatibles con un aumento de consultas respiratorias en días con más PM2.5». Los números de ejemplo no deben usarse para estimar el riesgo de una persona.",
    ],
    vocab=[("aumento porcentual", "cambio dividido por el valor de partida, multiplicado por 100"), ("desfase", "tiempo que pasa entre la causa y el efecto"), ("ajustar por una variable", "comparar o calcular de modo que esa variable no distorsione el resultado"), ("pico", "valor máximo de una medición en un período"), ("serie temporal", "datos medidos en días o períodos sucesivos")],
    worked=[
        ("Calcular un aumento porcentual", "En un centro de ejemplo, las consultas pasan de 50 a 75 al día. ¿Cuál es el aumento porcentual?",
         ["El cambio es 75 menos 50, es decir, 25.", "Se divide 25 entre 50 y se multiplica por 100."],
         "50 %"),
        ("Reconocer una confusora", "En días muy fríos hay más consultas y también más PM2.5, porque se usa más leña. ¿Qué papel tiene el frío?",
         ["Influye en las consultas por sí mismo y también en la cantidad de PM2.5.", "Eso lo convierte en una variable confusora."],
         "Variable confusora"),
    ],
    mistakes=[("Atribuir todo el aumento de consultas al aire.", "El frío y los virus también aumentan las consultas.", "Controla o menciona las variables confusoras."),
              ("Comparar el mismo día en vez de considerar el desfase.", "El efecto puede aparecer uno o dos días después del pico.", "Revisa también los días siguientes.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es un desfase en una serie temporal?", "El tiempo que pasa entre la causa y el efecto", "Un error de medición", "Un valor máximo", "El desfase es el retraso con que aparece el efecto."),
        ("{F} ¿Cuántas consultas al día hay cuando el PM2.5 es de 60 o más?", "120", "La ficha indica 120 consultas al día en ese tramo."),
        ("ab", "{F} A medida que aumenta el PM2.5 en la tabla, las consultas:", "Aumentan", "Disminuyen", "Los valores de la tabla suben de 40 a 120."),
        ("=", "{F} ¿Cuántas consultas más al día hay en el tramo de 40 a 59 que en el de menos de 20?", "80-40", "La diferencia entre 80 y 40 es de 40 consultas.", " consultas"),
        ("=", "{F} ¿Cuál es el aumento porcentual de consultas al pasar del tramo menor de 20 al tramo de 40 a 59?", "(80-40)/40*100", "El cambio es 40 sobre 40, es decir, 100 %.", " %"),
        ("=", "{F} ¿Cuál es el aumento porcentual de consultas al pasar del tramo de 40 a 59 al tramo de 60 o más?", "(120-80)/80*100", "El cambio es 40 sobre 80, es decir, 50 %.", " %"),
        ("abc", "{F} Un día hay un pico de PM2.5. Según la nota, ¿cuándo esperarías un aumento de consultas?", "Uno a dos días después", "Antes del pico", "Nunca", "La nota de la ficha indica ese desfase de uno a dos días."),
        ("abc", "{F} ¿Qué variable confusora se menciona en la nota?", "El frío y los virus respiratorios", "El color del humo", "El tamaño del centro de salud", "El frío aumenta las consultas y también la leña quemada."),
        ("abc", "{F} Una vecina dice: «la tabla prueba que el humo es la única causa de las consultas». ¿Qué le respondes?", "Que es compatible con una causa, pero hay confusoras como el frío y los virus", "Que sí, es la única causa", "Que la tabla no sirve", "Un estudio observacional no descarta otras explicaciones."),
        ("abc", "{F} ¿Qué evidencia fortalecería la conclusión de que el PM2.5 aumenta las consultas?", "Que otros estudios en otras ciudades muestren lo mismo y exista un mecanismo plausible", "Que la tabla tenga más colores", "Que haya más centros de salud", "Coincidencia entre estudios y mecanismo suman a la evidencia."),
        ("abc", "{F} ¿Qué haría un estudio para controlar el efecto del frío?", "Comparar días con una temperatura parecida", "Ignorar la temperatura", "Medir solo en verano", "Comparar días con igual frío separa el efecto del aire."),
        ("abc", "{F} Una autoridad propone alertas de calidad del aire en los días con PM2.5 de 60 o más. ¿Qué dato de la tabla la respalda?", "Que en esos días hay el triple de consultas que en los de menos de 20", "Que hay 120 días de datos", "Que el centro es ficticio", "120 contra 40 es el triple de consultas."),
        ("abc", "Una estudiante con tos persistente se pregunta si la tabla explica lo suyo. ¿Qué corresponde según este cuaderno?", "Consultar a un profesional de salud, porque la tabla describe una población y no diagnostica", "Usar la tabla para diagnosticarse", "No hacer nada", "Los datos de población no sirven para diagnosticar a una persona."),
    ],
    ctx=("abc", "Contexto: preparas una nota para el diario del liceo sobre la tabla de Valle Claro. ¿Qué titular es más honesto?", "«En días con más humo hay más consultas respiratorias, aunque otros factores también influyen»", "«El humo causa todas las enfermedades del invierno»", "«La tabla prueba que el frío no importa»", "El titular informa el patrón y reconoce otras explicaciones."),
    sc=[
        ("En Ciencias de la salud: ¿qué es el aumento porcentual?", "El cambio dividido por el valor de partida, multiplicado por 100", "Permite comparar cambios respecto del punto de partida."),
        ("ab", "Una variable confusora:", "Puede explicar parte de la relación", "No tiene ningún efecto", "Influye en ambas variables y puede distorsionar."),
        ("ab", "Un gradiente dosis-respuesta es:", "Un indicio a favor de una causa", "Una prueba definitiva", "Fortalece la idea de causa, pero no la demuestra por sí solo."),
    ],
    op=("Con la tabla de la ficha {F} haz lo siguiente: (1) calcula el aumento porcentual entre el primer y el último tramo; (2) escribe una conclusión de dos oraciones con lenguaje prudente; (3) nombra dos confusoras o limitaciones y una evidencia que pedirías.",
        "(1) De 40 a 120 son 80 consultas más, es decir, 200 %. (2) En los días con más PM2.5 hay más consultas respiratorias, lo que es compatible con un efecto del aire. No se puede decir que sea la única causa. (3) El frío y los virus. Pediría un estudio que compare días con la misma temperatura.",
        ["aumento porcentual correcto", "conclusión con lenguaje prudente", "dos confusoras o limitaciones", "evidencia adicional razonable"],
        ["tres partes numeradas"],
        ["decir que el aire es la única causa", "olvidar el frío", "calcular mal el porcentaje"],
        "Pregunta: «¿cómo cambiaría tu conclusión si las consultas subieran el mismo día y no uno o dos días después?»."),
    reinforce="Calcula el aumento porcentual entre otros dos tramos de la tabla y explica si el aumento es mayor o menor que entre los extremos.",
    extend="Explica por qué el orden temporal es importante para afirmar que una exposición causa un efecto.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 20 (opciones de ejemplo para reducir la exposición al humo en Valle Claro). "
     "Opción A, un programa de recambio de calefactores a leña por otros más limpios. Opción B, mejorar la aislación térmica de las viviendas para necesitar menos calefacción. Opción C, alertas de calidad del aire con recomendaciones. Opción D, entregar solo mascarillas. "
     "Puntajes de 1 a 3 (3 es mejor) en tres criterios: reduce la exposición, protege a todos por igual y costo accesible. "
     "A: reduce 3, protege a todos 2, costo 1. B: reduce 3, protege a todos 3, costo 1. C: reduce 1, protege a todos 2, costo 3. D: reduce 1, protege a todos 1, costo 2.")
build(
    O4, 5, F,
    use="Aprenderé a comparar medidas para reducir la exposición a contaminantes y a comunicar la decisión a la comunidad con claridad y con los límites de la evidencia. Sirve para escribir un mensaje que informe sin alarmar.",
    prior=["Sé comparar opciones con criterios.", "Sé sumar puntajes.", "Sé identificar una cadena de exposición."],
    explain=[
        "Reducir la exposición se puede hacer en distintos puntos de la cadena. Lo más efectivo es actuar en la fuente, por ejemplo mejorando los calefactores o evitando la necesidad de calefacción con aislación térmica. Luego se puede actuar en el medio, por ejemplo con normas y control de emisiones, y por último en la persona, con alertas, recomendaciones o mascarillas. Las medidas personales dependen de cada uno y protegen menos que las que actúan en la fuente.",
        "Para decidir se usa una matriz de criterios: cuánto reduce la exposición, si protege a todos por igual (equidad) y el costo. En la ficha, la opción B suma 3 más 3 más 1, es decir, 7 puntos; la A suma 6; la C suma 6; y la D suma 4. Pero el resultado no es una orden: las comunidades con menos recursos pueden necesitar apoyo para aplicar una medida cara.",
        "Después se comunica la decisión. Un buen mensaje a la comunidad dice qué se decide y por qué, qué datos lo sostienen, qué no se sabe, qué puede hacer cada persona y a quién acudir. Usa palabras simples, evita el miedo innecesario y no culpa a nadie. Si alguien se siente mal de salud, el mensaje orienta a consultar a un profesional. Las cifras de este cuaderno son de ejemplo y no describen ninguna ciudad real.",
    ],
    vocab=[("equidad", "que las medidas protejan de manera justa a todos los grupos, incluidos los más vulnerables"), ("emisión", "liberación de contaminantes al ambiente desde una fuente"), ("medida en la fuente", "acción que evita o reduce el contaminante en su origen"), ("comunicación de riesgo", "forma de informar a la comunidad sobre un problema, sus causas y qué hacer"), ("incertidumbre", "aquello que todavía no se sabe con seguridad")],
    worked=[
        ("Sumar puntajes", "Una opción de ejemplo tiene puntajes 2, 3 y 1. ¿Cuántos puntos suma?",
         ["Se suman los tres puntajes.", "2 más 3 más 1."],
         "6 puntos"),
        ("Elegir dónde actuar", "Para reducir la exposición al humo de leña, ¿es más efectivo mejorar el calefactor o entregar mascarillas?",
         ["Mejorar el calefactor actúa en la fuente.", "Las mascarillas actúan en la persona y dependen de que se usen bien siempre."],
         "Mejorar el calefactor"),
    ],
    mistakes=[("Elegir solo la medida más barata.", "Una medida barata puede reducir poco la exposición o dejar fuera a quienes más lo necesitan.", "Compara reducción de exposición, equidad y costo."),
              ("Comunicar con alarma o culpando a las familias.", "El miedo y la culpa no ayudan a actuar y pueden generar rechazo.", "Informa con datos, límites y acciones posibles.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es una medida en la fuente?", "Una acción que evita o reduce el contaminante en su origen", "Una acción que solo protege a una persona", "Una acción que solo informa", "Las medidas en la fuente evitan que el contaminante llegue al ambiente."),
        ("=", "{F} ¿Cuántos puntos suma la opción A?", "3+2+1", "Se suman 3, 2 y 1.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción B?", "3+3+1", "Se suman 3, 3 y 1.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción C?", "1+2+3", "Se suman 1, 2 y 3.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción D?", "1+1+2", "Se suman 1, 1 y 2.", " puntos"),
        ("abc", "{F} ¿Qué opción queda primera?", "Opción B", "Opción A", "Opción D", "B suma 7, A y C suman 6 y D suma 4."),
        ("abc", "{F} ¿Por qué la opción D tiene puntaje bajo en reducir la exposición?", "Porque la mascarilla depende de que cada persona la use bien siempre y no reduce el humo en la fuente", "Porque las mascarillas son muy caras", "Porque eliminan el humo", "La protección personal es menos confiable que actuar en la fuente."),
        ("abc", "{F} ¿Qué criterio de la ficha se relaciona con la equidad?", "Protege a todos por igual", "Costo accesible", "Reduce la exposición", "Equidad es proteger de manera justa a todos los grupos."),
        ("abc", "{F} La opción B tiene costo 1. ¿Qué se podría hacer para que las familias de menos recursos puedan aplicarla?", "Buscar un apoyo o subsidio y priorizar a quienes más lo necesitan", "No aplicarla nunca", "Aplicarla solo en las familias con más recursos", "Un subsidio reduce la barrera del costo y mejora la equidad."),
        ("abc", "{F} Hay un aviso para la comunidad. ¿Cuál es el mejor mensaje?", "En días de alerta de calidad del aire, sigue las indicaciones de la autoridad sanitaria y, si te sientes mal, consulta a un profesional de salud", "Todos se van a enfermar", "No hay nada que hacer", "Un buen mensaje informa y orienta a acciones posibles y a consultar."),
        ("abc", "{F} Un mensaje a la comunidad dice «las familias que usan leña son culpables». ¿Qué problema tiene?", "Culpa a un grupo y no ayuda a actuar", "Es muy técnico", "Tiene demasiados datos", "Un buen mensaje evita culpar y propone soluciones compartidas."),
        ("abc", "{F} ¿Qué incertidumbre convendría comunicar?", "Que los datos son de pocos días y no incluyen todas las causas de las consultas", "Que todo se sabe con certeza", "Que no hay datos", "Declarar lo que falta da credibilidad al mensaje."),
        ("abc", "{F} Una combinación sensata de medidas sería:", "B y C: actuar en la fuente a largo plazo y avisar a la comunidad mientras tanto", "Solo D", "Ninguna", "Las alertas protegen en el corto plazo mientras la medida en la fuente da resultados."),
    ],
    ctx=("abc", "Contexto: te piden escribir una infografía para tu comunidad sobre la calidad del aire en invierno. ¿Qué elementos incluyes?", "Qué se sabe, qué datos lo respaldan, qué no se sabe, qué puede hacer cada persona y cuándo consultar a un profesional", "Solo fotos del humo", "Solo el número más alto", "La infografía informa con claridad y deja la decisión a la persona y a los profesionales."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la equidad en una medida de salud pública?", "Que proteja de manera justa a todos los grupos, incluidos los más vulnerables", "Una medida equitativa no deja atrás a quienes tienen menos recursos."),
        ("ab", "Las medidas en la fuente suelen ser:", "Más efectivas que las medidas personales", "Menos efectivas que las personales", "Actuar en el origen reduce la exposición de todos."),
        ("ab", "Un buen mensaje de riesgo:", "Informa los límites y qué se puede hacer", "Solo asusta", "Honestidad y acción posible hacen un mensaje útil."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) suma los puntajes de las cuatro opciones; (2) elige una combinación de dos opciones y justifica; (3) escribe un mensaje de cuatro oraciones para la comunidad, con un dato, un límite, una acción posible y a quién consultar si hay síntomas.",
        "(1) A: 6. B: 7. C: 6. D: 4. (2) Elijo B y C: B reduce la fuente y es equitativa, y C avisa mientras tanto. (3) En Valle Claro hay más consultas respiratorias en días con más humo. Aún no sabemos cuánto influye el frío. Sigue las indicaciones de la autoridad sanitaria en los días de alerta. Si te sientes mal, consulta a un profesional de salud.",
        ["puntajes correctos", "combinación justificada con criterios", "mensaje con dato, límite, acción y orientación", "lenguaje que no alarma ni culpa"],
        ["tres partes numeradas"],
        ["decidir solo por costo", "comunicar sin límites", "culpar a un grupo"],
        "Pregunta: «¿qué cambiarías del mensaje para que lo entienda una persona mayor?»."),
    reinforce="Escribe dos frases sobre calidad del aire: una alarmista y otra informativa, y marca las palabras que cambian el tono.",
    extend="Explica por qué las medidas en la fuente suelen proteger más y de manera más justa que las medidas personales.",
)
