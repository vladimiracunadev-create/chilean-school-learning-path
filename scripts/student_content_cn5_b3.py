"""Cuaderno del estudiante, 5.º básico Ciencias Naturales: OA 14 (actividad humana y protección de reservas hídricas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA14 = "CN05 OA 14"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 14, clase 1
register(
    OA14, 1,
    materials="Papel y lápiz. Los casos están escritos en el cuaderno; no hace falta salir de tu casa.",
    use="Aprenderé a reconocer efectos positivos y negativos de la actividad humana sobre océanos, ríos, lagos y glaciares, separando lo que se observa de lo que se supone. Sirve para opinar con evidencia sobre el cuidado del agua.",
    prior=["Sé que el agua dulce es escasa en comparación con el total.", "Sé distinguir observación e interpretación."],
    explain=[
        "Las reservas hídricas son los lugares donde se guarda el agua dulce: glaciares, ríos, lagos y aguas subterráneas. Las personas usamos esa agua y también afectamos a los océanos, lagos, ríos y glaciares. Esos efectos pueden ser negativos o positivos.",
        "Algunos efectos negativos son botar basura y plásticos al mar o a un río, verter aguas servidas o residuos sin tratar, pescar más de lo que las especies pueden reponer y gastar agua subterránea más rápido de lo que se renueva. Además, el calentamiento del planeta por actividades humanas hace que muchos glaciares pierdan hielo.",
        "Algunos efectos positivos son tratar las aguas servidas antes de devolverlas, crear parques y áreas marinas protegidas, limpiar playas y orillas de ríos, y regar con goteo para gastar menos agua. Para clasificar un caso, primero anoto lo que se observa y después digo si el efecto es positivo o negativo para el agua y los seres vivos.",
    ],
    vocab=[("reserva hídrica", "lugar donde se guarda agua dulce, como un glaciar, un lago o las aguas subterráneas"), ("contaminación", "presencia en el agua de sustancias o basura que la dañan"), ("aguas servidas", "agua usada en casas y fábricas que arrastra residuos"), ("área protegida", "zona donde se limita la actividad humana para cuidar la naturaleza"), ("efecto", "cambio que produce una acción")],
    worked=[
        {"title": "Clasificar un efecto", "problem": "Una comunidad limpia la orilla de un río y recoge 45 kg de basura. ¿El efecto es positivo o negativo?", "steps": ["Se sacó basura del río y de su orilla.", "Hay menos basura que pueda dañar el agua y a los seres vivos."], "answer": "Positivo"},
        {"title": "Observación o interpretación", "problem": "Frases: (A) «En la orilla del río se contaron 35 botellas plásticas.» (B) «A la gente no le importa el río.» ¿Cuál es observación?", "steps": ["La frase A se puede contar y comprobar.", "La frase B es una idea que no se prueba con ese dato."], "answer": "La A es observación; la B es interpretación"},
    ],
    mistakes=[
        {"wrong": "Decir que toda actividad humana daña el agua.", "why": "Se olvidan las acciones de cuidado.", "fix": "Busca efectos positivos, como tratar el agua o proteger una zona."},
        {"wrong": "Culpar a una persona sin ninguna evidencia.", "why": "Se salta de lo que se ve a una explicación inventada.", "fix": "Anota solo lo que se observa y busca datos para explicarlo."},
    ],
    tiers={
        "recovery": [
            ex("Botar basura a un río, ¿es un efecto positivo o negativo para el agua?", "Negativo", "La basura daña el agua y a los seres vivos."),
            ex("Tratar las aguas servidas antes de devolverlas a un río, ¿es un efecto positivo o negativo?", "Positivo", "Se devuelve agua con menos residuos."),
            ex("Un área marina protegida limita la pesca para cuidar especies. ¿El efecto es positivo o negativo?", "Positivo", "Protege a los seres vivos y su ambiente."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una reserva hídrica?", "Un lugar donde se guarda agua dulce, como un glaciar, un lago, un río o las aguas subterráneas", "Son las reservas que usamos para obtener agua dulce."),
            ex("Lee: «En la orilla de un río se contaron 35 botellas plásticas». ¿Es una observación o una interpretación?", "Observación", "Se puede contar y comprobar."),
            ex("Lee: «Las personas no cuidan el río». ¿Es una observación o una interpretación?", "Interpretación", "Es una idea sobre las personas que ese dato no prueba."),
        ],
        "apply": [
            arith("Tres grupos limpian una playa y recogen 12 kg, 15 kg y 18 kg de basura. ¿Cuántos kg recogen en total?", "12+15+18", "Se suman las tres cantidades.", " kg"),
            ex("Lista de acciones: (A) echar aceite usado al desagüe, (B) regar con goteo, (C) dejar basura en la playa, (D) reciclar botellas, (E) pescar más allá de la cuota permitida. ¿Cuántas son efectos negativos?", "3 (A, C y E)", "Dañan el agua o a sus especies; B y D cuidan el agua o el ambiente."),
            ex("Un municipio instala una planta que limpia las aguas servidas antes de que lleguen al mar. ¿Qué efecto positivo se espera en el agua?", "Llega menos contaminación al mar", "Se retiran residuos antes de devolver el agua."),
        ],
        "reason": [
            ex("Pedro dice: «el glaciar se achicó porque alguien lo pisó». ¿Qué evidencia permitiría afirmar que un glaciar perdió hielo?", "Fotografías o mediciones del glaciar en años distintos", "Para ver un cambio hay que comparar datos de épocas distintas."),
            ex("Un embalse guarda agua para regar, pero cambia el curso del río y a los peces. ¿Es una acción solo positiva?", "No, tiene efectos positivos y negativos", "Una misma acción puede tener ventajas y daños."),
        ],
        "challenge": [
            ex("¿Cuál frase es una observación: (a) «hay peces muertos en la orilla del río» o (b) «los mató una fábrica»?", "(a)", "La (a) se ve; la (b) es una explicación sin evidencia."),
            arith("Una brigada recoge 120 botellas el lunes y 85 el martes. ¿Cuántas botellas recoge en los dos días?", "120+85", "Se suman las dos cantidades.", " botellas"),
        ],
    },
    context=[ex("En tu barrio hay un canal con basura. Una vecina propone limpiarlo cada mes. ¿Es una acción de cuidado del agua o de daño?", "De cuidado", "Retirar basura reduce la contaminación.")],
    selfcheck=[
        ex("¿Verter residuos sin tratar a un río tiene efecto positivo o negativo?", "Negativo", "Contamina el agua."),
        ex("Nombra una acción humana que protege el agua.", "Tratar aguas servidas, limpiar orillas, regar con goteo o crear áreas protegidas", "Cualquiera de esas reduce el daño o cuida el agua."),
        ex("Una observación, ¿se puede comprobar con un dato?", "Sí", "Por eso se separa de la interpretación."),
    ],
    open_task=task(
        "Copia esta lista: (A) una empresa trata sus aguas antes de devolverlas al río; (B) un grupo deja basura en la orilla de un lago; (C) se crea un parque marino para cuidar especies; (D) se riega un campo con manguera abierta todo el día. Clasifica cada caso como efecto positivo o negativo y escribe una observación y una interpretación sobre uno de ellos.",
        "A positivo; B negativo; C positivo; D negativo. Observación: hay basura en la orilla del lago. Interpretación: nadie la limpia porque no le importa.",
        ["clasifica los cuatro casos", "escribe una observación y una interpretación", "las distingue bien"],
        ["lista clasificada", "dos frases rotuladas"],
        ["decir que todo es negativo", "mezclar observación e interpretación"],
        "Pregunta qué dato necesitaría para comprobar su interpretación.",
    ),
    reinforce="Escribe dos efectos positivos y dos negativos de la actividad humana sobre el agua.",
    extend="Averigua con una persona de tu casa qué se hace en tu comuna para cuidar el agua de ríos o del mar.",
)

# ---------------------------------------------------------------- OA 14, clase 2
register(
    OA14, 2,
    materials="Dos o tres vasos plásticos transparentes iguales, agua de la llave, tierra de maceta, una cucharita y una hoja con una cruz dibujada. Hazlo con una persona de tu casa y no bebas el agua usada. Si no puedes, usa los datos escritos.",
    use="Aprenderé a formular una pregunta y una predicción sobre cómo una actividad humana puede cambiar el agua. Sirve para investigar un problema antes de proponer una solución.",
    prior=["Sé que la basura y los residuos pueden contaminar el agua.", "Sé que una variable es algo que puede cambiar."],
    explain=[
        "Una investigación empieza con una pregunta que se puede comprobar. Por ejemplo: «¿Cuánto cambia la transparencia del agua si le agrego más tierra?». Los ríos se enturbian cuando les llegan tierra o residuos, y esa agua deja pasar menos luz.",
        "En un experimento hay tres tipos de variables. La que yo cambio: la cantidad de tierra. La que observo: si veo o no una cruz dibujada bajo el vaso. Las que mantengo iguales: el vaso, la cantidad de agua y el lugar. Mantener iguales las otras variables hace que el resultado sea justo.",
        "La predicción se escribe con «Si…, entonces…»: si agrego más tierra, entonces la cruz se verá menos. Luego se compara con lo observado. Este vaso es un modelo muy pequeño de un río, por eso no se puede concluir que así se contaminan todos los ríos. Otro ejemplo: si llegan muchos nutrientes de fertilizantes a un lago, las algas crecen demasiado, y al descomponerse gastan el oxígeno del agua.",
    ],
    vocab=[("variable", "algo que puede cambiar en un experimento"), ("variable que cambio", "lo único que modifico a propósito"), ("variable que mido u observo", "lo que anoto para ver el resultado"), ("turbia", "agua que no es transparente porque tiene partículas"), ("fertilizante", "producto que se echa a la tierra para ayudar a crecer a las plantas")],
    worked=[
        {"title": "Identificar variables", "problem": "Tres vasos iguales tienen 200 mL de agua. Al vaso A no le agrego tierra; al B, 1 cucharadita; al C, 3 cucharaditas. ¿Cuál es la variable que cambio?", "steps": ["Lo que se modifica a propósito es la cantidad de tierra.", "Los vasos y los 200 mL de agua se mantienen iguales."], "answer": "La cantidad de tierra"},
        {"title": "Escribir una predicción", "problem": "Escribe una predicción para ese experimento.", "steps": ["Uso «Si…, entonces…».", "Relaciono la tierra con la transparencia."], "answer": "Si agrego más tierra al agua, entonces la cruz del fondo se verá menos."},
    ],
    mistakes=[
        {"wrong": "Cambiar la cantidad de tierra y también el tamaño del vaso.", "why": "Se cree que más cambios dan más información.", "fix": "Cambia una sola cosa a la vez y mantén lo demás igual."},
        {"wrong": "Concluir que todos los ríos del mundo se contaminan igual que el vaso.", "why": "Se generaliza desde un modelo muy pequeño.", "fix": "Di que el vaso es un modelo y tiene límites."},
    ],
    tiers={
        "recovery": [
            ex("En el experimento de los vasos con tierra, ¿qué cambia entre el vaso A y el vaso B?", "La cantidad de tierra", "Es lo que se modifica a propósito."),
            ex("En ese experimento, ¿qué debe mantenerse igual: la cantidad de agua o la cantidad de tierra?", "La cantidad de agua", "Solo se debe cambiar una variable."),
            ex("¿Está bien escrita esta predicción: «Si agrego tierra, entonces el agua se verá más turbia»?", "Sí", "Usa «Si…, entonces…» y relaciona dos variables."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una variable?", "Algo que puede cambiar en un experimento", "Se identifican las que cambian y las que se mantienen."),
            ex("¿Qué observas para saber si el agua está más turbia en el experimento?", "Si se ve o no la cruz del fondo", "Es el resultado que se registra."),
            ex("¿Cuál es una pregunta comprobable: (a) «¿Qué río es más lindo?» o (b) «¿Cuánto cambia la transparencia si agrego más tierra al agua?»?", "(b)", "Se responde con datos observados."),
        ],
        "apply": [
            arith("Para tres vasos con 200 mL de agua cada uno, ¿cuántos mL de agua necesitas en total?", "3*200", "Se multiplica la cantidad de vasos por el volumen de cada uno.", " mL"),
            arith("Al vaso B se le agrega 1 cucharadita de tierra y al vaso C, 3 cucharaditas. ¿Cuántas cucharaditas más tiene el vaso C?", "3-1", "Se resta la cantidad menor a la mayor.", " cucharaditas"),
            ex("Los vasos A, B y C tienen 0, 1 y 3 cucharaditas de tierra. ¿En cuál esperas que la cruz se vea menos?", "En el vaso C", "Es el que tiene más tierra."),
        ],
        "reason": [
            ex("Clara usó un vaso grande con tierra y un vaso pequeño sin tierra. ¿Por qué su comparación no es justa?", "Cambió dos cosas a la vez: el tamaño del vaso y la tierra", "No se sabe cuál causó la diferencia."),
            ex("Clara vio que el agua con tierra se enturbió y dice: «así se contaminan todos los ríos». ¿Qué limitación tiene su conclusión?", "El vaso es un modelo pequeño y no representa todos los ríos", "Una conclusión no puede ir más allá de los datos."),
        ],
        "challenge": [
            ex("Dato: cuando las algas de un lago mueren y se descomponen, gastan oxígeno del agua. Si por exceso de fertilizante crecen muchas algas, ¿qué predices para los peces del lago?", "Tendrán menos oxígeno y podrían morir", "Las algas que se descomponen quitan oxígeno al agua."),
            arith("Un grupo prueba 4 cantidades distintas de tierra y repite cada una en 3 vasos. ¿Cuántos vasos usa?", "4*3", "Se multiplican las cantidades por las repeticiones.", " vasos"),
        ],
    },
    context=[ex("Después de una lluvia fuerte, un río cerca de la ciudad se ve café. Una investigadora quiere saber por qué. ¿Qué pregunta comprobable puede hacer?", "¿Cuánta tierra lleva el agua del río después de la lluvia?", "Se puede responder midiendo qué tan turbia está el agua.")],
    selfcheck=[
        ex("¿Qué se debe mantener igual en un experimento justo?", "Las variables que no estoy probando", "Así se sabe qué causó el cambio."),
        ex("¿Con qué palabras se escribe una predicción?", "Si…, entonces…", "Es una forma para relacionar causa y efecto."),
        ex("¿Qué es un modelo en Ciencias?", "Una representación simple de algo", "El vaso representa a un río."),
    ],
    open_task=task(
        "Con una persona de tu casa, prepara dos vasos iguales con 200 mL de agua. A uno agrégale 1 cucharadita de tierra y mézclalo. Pon una hoja con una cruz bajo cada vaso y mira desde arriba. Si no puedes, usa estos datos: vaso sin tierra, la cruz se ve claro; vaso con tierra, la cruz casi no se ve. Escribe la pregunta, la predicción, las variables y una limitación.",
        "Pregunta: ¿cambia la transparencia si agrego tierra? Predicción: si agrego tierra, la cruz se verá menos. Variable que cambio: tierra. Mantengo: vasos y agua. Limitación: es un modelo pequeño.",
        ["pregunta comprobable", "predicción con «Si…, entonces…»", "variables bien identificadas", "una limitación"],
        ["texto de cuatro partes", "dibujo del montaje"],
        ["cambiar dos variables a la vez", "olvidar la limitación"],
        "Pregunta qué cambiaría para comprobar si el tipo de tierra importa.",
    ),
    reinforce="Escribe una pregunta comprobable sobre cómo la basura puede afectar a un río.",
    extend="Averigua por qué después de una lluvia fuerte algunos ríos se ven de color café.",
)

# ---------------------------------------------------------------- OA 14, clase 3
register(
    OA14, 3,
    materials="Un colador, un trozo de tela limpia, dos vasos, agua de la llave, un poco de tierra, hojas y una cucharadita de sal, con una persona de tu casa. No bebas el agua del experimento. Si no puedes, usa los datos escritos.",
    use="Aprenderé a usar un filtro como modelo de una planta de tratamiento de agua y a reconocer lo que logra y lo que no. Sirve para entender por qué no basta con mirar el agua para saber si está limpia.",
    prior=["Sé que el agua puede arrastrar tierra y basura.", "Sé qué es un modelo."],
    explain=[
        "Una planta de tratamiento es un lugar donde se limpia el agua usada antes de devolverla a un río o al mar, o antes de que llegue a las casas. Para estudiarla puedo usar un modelo: un colador o una tela que filtra agua con tierra y hojas.",
        "En el modelo, el colador detiene las hojas grandes y la tela detiene la tierra fina. El agua que pasa queda más clara. Pero si la sal está disuelta en el agua, atraviesa el filtro y el agua sigue salada. Una sustancia disuelta es una que se mezcló con el agua y no se ve.",
        "Por eso el agua transparente no siempre es limpia o segura para beber: puede llevar sustancias disueltas o microbios que no se ven. Las plantas de tratamiento reales usan varias etapas y controles, no solo un filtro. El modelo muestra solo una etapa. No bebas nunca el agua de un experimento.",
    ],
    vocab=[("filtro", "material que deja pasar el agua y retiene partículas"), ("planta de tratamiento", "lugar donde se limpia el agua usada o el agua para beber"), ("disuelto", "mezclado con el agua de modo que no se ve"), ("partículas", "trocitos muy pequeños, como tierra"), ("etapa", "paso de un proceso")],
    worked=[
        {"title": "Agua recuperada", "problem": "Pasas por la tela 200 mL de agua con tierra y recuperas 190 mL de agua más clara. ¿Cuántos mL quedaron en la tela?", "steps": ["Entraron 200 mL.", "Salieron 190 mL.", "Resto: 200 − 190 = 10."], "answer": "10 mL"},
        {"title": "Qué retiene el filtro", "problem": "Filtras agua con sal disuelta y el agua sigue salada. ¿Qué indica?", "steps": ["La sal disuelta pasó a través de la tela.", "Un filtro de tela no retiene lo disuelto."], "answer": "Que el filtro no retira sustancias disueltas"},
    ],
    mistakes=[
        {"wrong": "Pensar que si el agua se ve transparente, ya se puede beber.", "why": "Lo disuelto o los microbios no se ven.", "fix": "Recuerda que se necesitan análisis y varias etapas de tratamiento."},
        {"wrong": "Beber el agua del experimento porque quedó clara.", "why": "Se cree que el filtro de casa la limpió por completo.", "fix": "Nunca bebas el agua de un experimento."},
    ],
    tiers={
        "recovery": [
            ex("En el modelo, ¿el colador detiene las hojas grandes o la sal disuelta?", "Las hojas grandes", "Lo disuelto pasa por el colador."),
            ex("La sal disuelta en el agua, ¿pasa por la tela del filtro o queda atrapada en ella?", "Pasa por la tela", "Lo disuelto atraviesa el filtro."),
            ex("¿Se puede beber el agua de un experimento de filtrado casero?", "No", "Puede tener sustancias o microbios que no se ven."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es una planta de tratamiento de agua?", "Un lugar donde se limpia el agua usada o el agua para beber", "Trata el agua para reducir contaminantes."),
            ex("En el modelo, ¿qué representa el agua con tierra y hojas?", "El agua contaminada de un río", "Es el agua que se quiere limpiar."),
            ex("En el modelo, ¿qué representa la tela?", "Una etapa de filtrado de la planta de tratamiento", "Es el filtro del modelo."),
        ],
        "apply": [
            arith("Pasas por la tela 200 mL de agua con tierra y recuperas 190 mL. ¿Cuántos mL quedaron en la tela?", "200-190", "Se resta lo que salió a lo que entró.", " mL"),
            arith("Una planta de ejemplo trata 300 litros de agua por minuto. ¿Cuántos litros trata en 10 minutos?", "300*10", "Se multiplica la cantidad por minuto por los minutos.", " litros"),
            ex("Después de filtrar agua con sal disuelta, el agua sigue salada. ¿Qué te dice esto del filtro?", "Que no retira lo disuelto", "La sal pasó a través de él."),
        ],
        "reason": [
            ex("Lucas dice: «si el agua quedó transparente, ya es potable». ¿Por qué se equivoca?", "Porque pueden quedar sustancias disueltas o microbios que no se ven", "La transparencia no prueba que sea segura."),
            ex("¿Qué limitación tiene este modelo si lo comparas con una planta real?", "Muestra una sola etapa y una planta usa varias etapas y controles", "El modelo simplifica el proceso."),
        ],
        "challenge": [
            arith("La tela de un filtro de ejemplo retiene 40 g de los 50 g de tierra que llevaba el agua. ¿Cuántos g de tierra pasaron?", "50-40", "Se resta la tierra retenida a la que entró.", " g"),
            ex("Para filtrar agua con hojas grandes y tierra fina, ¿qué va primero: el colador de hojas o la tela fina?", "El colador de hojas", "Si no, las hojas taparían la tela fina."),
        ],
    },
    context=[ex("Una comunidad rural tiene un pozo con agua que se ve clara. Un técnico dice que aun así hay que analizarla. ¿Por qué?", "Porque pueden haber sustancias disueltas o microbios que no se ven", "La claridad no basta para saber si es segura.")],
    selfcheck=[
        ex("¿Qué retiene un filtro: partículas o sustancias disueltas?", "Partículas", "Lo disuelto atraviesa."),
        ex("¿Un modelo muestra todo el proceso real?", "No", "Un modelo tiene limitaciones."),
        ex("¿Es seguro beber agua de un experimento?", "No", "Puede tener cosas que no se ven."),
    ],
    open_task=task(
        "Con una persona de tu casa, pasa agua con tierra y hojas por un colador y luego por una tela. En otro vaso pasa agua con una cucharadita de sal. Si no puedes, usa estos datos: el agua con tierra queda clara; el agua con sal sigue salada. Escribe qué retiene el filtro, qué no retiene y una limitación del modelo.",
        "Retiene hojas y tierra. No retiene la sal disuelta. Limitación: una planta real tiene varias etapas y controles; no bebas el agua.",
        ["distingue partículas y disueltos", "describe lo que retiene y lo que no", "nombra una limitación"],
        ["tabla con dos columnas", "frase de limitación"],
        ["decir que el filtro limpia todo", "olvidar la advertencia de no beberla"],
        "Pregunta qué otra etapa agregaría una planta real.",
    ),
    reinforce="Dibuja un filtro con tres capas y rotula qué retiene cada una.",
    extend="Averigua con una persona de tu casa si su comuna trata las aguas servidas y qué hace con el agua tratada.",
)

# ---------------------------------------------------------------- OA 14, clase 4
register(
    OA14, 4,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a comparar acciones para cuidar el agua usando un mismo criterio, los litros ahorrados. Sirve para escoger acciones que realmente ayuden a proteger las reservas de agua.",
    prior=["Sé multiplicar y restar con números naturales.", "Sé que el agua dulce es escasa."],
    explain=[
        "Para proteger las reservas hídricas, como glaciares, ríos, lagos y aguas subterráneas, se pueden tomar acciones. Unas reducen el gasto de agua y otras evitan la contaminación. Para escoger cuál conviene más, hay que compararlas con un criterio común.",
        "Un criterio común sirve cuando todas las acciones se miden con la misma unidad. Si quiero comparar acciones de ahorro, puedo usar «litros ahorrados por semana». Con datos de ejemplo: una ducha gasta 10 litros por minuto; una llave abierta gasta 8 litros por minuto. Acortar una ducha de 10 a 5 minutos ahorra 50 litros cada vez.",
        "Un ahorro pequeño suma si lo hacen muchas personas. Si 100 personas ahorran 20 litros por día, ahorran 2.000 litros cada día. Para decidir también hay que mirar los límites: los datos son de ejemplo y cada casa gasta distinto.",
    ],
    vocab=[("acción de protección", "algo que hago para cuidar el agua"), ("criterio común", "regla igual para comparar todas las opciones"), ("ahorro", "cantidad de agua que se deja de gastar"), ("litro (L)", "unidad de volumen; 1 litro son 1.000 mL"), ("reserva hídrica", "lugar donde se guarda agua dulce")],
    worked=[
        {"title": "Ahorro de una ducha", "problem": "Una ducha gasta 10 litros por minuto. ¿Cuántos litros se ahorran al bajar de 10 a 5 minutos?", "steps": ["10 minutos gastan 10 × 10 = 100 litros.", "5 minutos gastan 5 × 10 = 50 litros.", "Ahorro: 100 − 50 = 50."], "answer": "50 litros"},
        {"title": "Llave cerrada al cepillarse", "problem": "Una llave abierta gasta 8 litros por minuto. Con la llave abierta 3 minutos se gastan 24 litros. Si la cierras y usas 2 litros en un vaso, ¿cuántos litros ahorras?", "steps": ["Gasto con llave abierta: 24 litros.", "Gasto con vaso: 2 litros.", "Resto: 24 − 2 = 22."], "answer": "22 litros"},
    ],
    mistakes=[
        {"wrong": "Comparar un ahorro por día con otro por semana sin convertirlos.", "why": "No se usó un criterio común.", "fix": "Pasa todos los datos a litros por semana."},
        {"wrong": "Pensar que un ahorro pequeño no sirve.", "why": "Se mira solo a una persona.", "fix": "Multiplica por la cantidad de personas y días."},
    ],
    tiers={
        "recovery": [
            ex("Para comparar acciones de ahorro de agua, ¿qué unidad común puedes usar?", "Litros ahorrados", "Permite comparar todas las acciones con la misma unidad."),
            arith("Una ducha gasta 10 litros por minuto. ¿Cuántos litros gasta en 5 minutos?", "10*5", "Se multiplica el gasto por minuto por los minutos.", " litros"),
            ex("¿Cuál ahorra más agua: una ducha de 5 minutos o una de 10 minutos?", "La de 5 minutos", "Gasta menos litros."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es un criterio común de comparación?", "Una regla o unidad igual para todas las opciones que se comparan", "Así la comparación es justa."),
            ex("¿Cuál es una acción que protege las reservas de agua: (a) botar aceite al desagüe o (b) recoger la basura de la orilla de un río?", "(b)", "La basura retirada no contamina el agua."),
            ex("Ahorrar agua dulce, ¿ayuda a proteger las reservas hídricas?", "Sí", "Se usa menos agua de ríos, lagos y aguas subterráneas."),
        ],
        "apply": [
            arith("Una ducha gasta 10 litros por minuto. ¿Cuántos litros se ahorran al acortar la ducha de 8 a 6 minutos?", "10*8-10*6", "Se restan los gastos de ambas duchas.", " litros"),
            arith("Una ducha de 5 minutos gasta 50 litros. Si te duchas 7 veces en la semana, ¿cuántos litros gastas?", "50*7", "Se multiplica el gasto de una ducha por los días.", " litros"),
            arith("Una llave abierta gasta 8 litros por minuto. En un cepillado de 2 minutos con la llave abierta se gastan 16 litros. Si la cierras y usas 2 litros en un vaso, ¿cuántos litros ahorras?", "8*2-2", "Se resta el gasto del vaso al de la llave abierta.", " litros"),
        ],
        "reason": [
            ex("La acción A ahorra 30 litros por día y la acción B ahorra 150 litros por semana. ¿Cuál ahorra más en una semana?", "La A, que ahorra 210 litros", "30 × 7 = 210, que es más que 150."),
            ex("Un compañero compara una acción medida en minutos con otra medida en litros. ¿Por qué no es una buena comparación?", "Usa unidades distintas; hay que pasar todo a litros", "Se necesita un criterio común."),
        ],
        "challenge": [
            arith("Una familia de 4 personas ahorra 20 litros cada una por día al acortar la ducha. ¿Cuántos litros ahorran en 7 días?", "4*20*7", "Se multiplica por las personas y por los días.", " litros"),
            arith("Un vecino dice: «mi ahorro de 20 litros por día es muy poco». Si 150 personas ahorran 20 litros cada día, ¿cuántos litros ahorran juntas en un día?", "150*20", "Se multiplica el ahorro individual por las personas.", " litros"),
        ],
    },
    context=[ex("En el colegio quieren elegir entre dos acciones: poner cierres en las llaves o regar el patio solo de noche. ¿Qué criterio común pueden usar para decidir?", "Los litros ahorrados por semana", "Permite comparar con la misma unidad.")],
    selfcheck=[
        ex("¿Qué se necesita para comparar acciones con justicia?", "Un criterio común", "Debe haber una misma unidad."),
        ex("¿Cuántos mL tiene 1 litro?", "1.000 mL", "Es la equivalencia entre litro y mililitro."),
        ex("¿Un ahorro pequeño de muchas personas puede ser grande?", "Sí", "Se suman los ahorros individuales."),
    ],
    open_task=task(
        "Compara dos acciones con estos datos de ejemplo: A, acortar la ducha de 10 a 5 minutos (10 L por minuto, 7 veces por semana); B, cerrar la llave al cepillarse (24 L abierta contra 2 L con vaso, 14 veces por semana). Calcula los litros ahorrados por semana de cada una, elige la que ahorra más y escribe una limitación.",
        "A: 50 L × 7 = 350 L. B: 22 L × 14 = 308 L. A ahorra más. Limitación: son datos de ejemplo y cada casa gasta distinto.",
        ["calcula litros por semana de ambas", "elige con el dato", "nombra una limitación"],
        ["dos cálculos", "elección escrita"],
        ["comparar unidades distintas", "no hacer los cálculos semanales"],
        "Pregunta qué cambiaría si hubiera más personas en la casa.",
    ),
    reinforce="Escribe una acción de ahorro de agua para tu casa y calcula cuántos litros ahorrarías en una semana.",
    extend="Averigua con una persona de tu casa cuántos litros de agua aparecen en la cuenta del agua en un mes.",
)

# ---------------------------------------------------------------- OA 14, clase 5
register(
    OA14, 5,
    materials="Papel y lápiz. Los datos son de ejemplo y están escritos en el cuaderno.",
    use="Aprenderé a explicar con evidencia el efecto de la actividad humana en el agua, a proponer acciones de protección y a comunicar mis resultados. Sirve para convencer a otras personas con datos y no solo con opiniones.",
    prior=["Sé clasificar efectos humanos como positivos o negativos.", "Sé comparar acciones con un criterio común."],
    explain=[
        "Chile tiene reservas de agua muy variadas: glaciares en la cordillera de los Andes y en la Patagonia, muchos ríos y lagos en el sur, y una costa muy larga. El norte es muy seco, y en la zona central ha habido varios años con poca lluvia. Por eso proteger el agua en Chile es importante.",
        "Una buena propuesta de protección sigue estos pasos: describir el problema con un dato, proponer una acción posible, explicar por qué ayudaría y decir cuáles son sus límites. Las acciones pueden ser personales, como ahorrar agua o no botar basura, o colectivas, como limpiar orillas, tratar las aguas servidas, regar con goteo o crear áreas protegidas.",
        "Para comunicar los resultados se usa un cartel, un informe o una exposición. Debe tener una pregunta, los datos, la conclusión, la acción que se propone y una limitación. Si el dato no alcanza, se dice «con estos datos no se puede asegurar». Así se evita exagerar.",
    ],
    vocab=[("propuesta", "acción que se sugiere para resolver un problema"), ("acción personal", "algo que hace una persona, como cerrar la llave"), ("acción colectiva", "algo que hace un grupo, como limpiar una orilla"), ("comunicar", "contar los resultados a otras personas de forma clara"), ("limitación", "aspecto que los datos no permiten asegurar")],
    worked=[
        {"title": "Evaluar una propuesta", "problem": "Un curso propone: «Cada persona del colegio cerrará la llave al lavarse las manos». Calculan que ahorran 3 litros por persona al día entre 200 personas. ¿Cuántos litros ahorran por día?", "steps": ["Son 200 personas.", "Cada una ahorra 3 litros: 200 × 3 = 600."], "answer": "600 litros por día"},
        {"title": "Partes de un mensaje", "problem": "¿Qué partes debe tener un cartel sobre una propuesta de cuidado del agua?", "steps": ["Una pregunta y los datos.", "Una conclusión y la acción propuesta.", "Una limitación."], "answer": "Pregunta, datos, conclusión, acción propuesta y limitación"},
    ],
    mistakes=[
        {"wrong": "Proponer algo imposible, como dejar de usar agua.", "why": "Se piensa que cuidar es dejar de usar.", "fix": "Propón acciones realistas, como reducir el gasto o evitar la contaminación."},
        {"wrong": "Presentar un cartel solo con opiniones.", "why": "Se cree que basta con convencer.", "fix": "Incluye al menos un dato y una limitación."},
    ],
    tiers={
        "recovery": [
            ex("Los glaciares de Chile, ¿son una reserva de agua dulce?", "Sí", "Son hielo de agua dulce."),
            ex("¿Cuál es una acción de protección que puedes hacer en casa: cerrar la llave al cepillarte los dientes o dejarla abierta?", "Cerrar la llave", "Se gasta menos agua."),
            ex("¿Cuál gasta menos agua: regar con goteo o regar con la manguera abierta todo el día?", "Regar con goteo", "Entrega solo el agua que la planta necesita."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué debe incluir un mensaje científico sobre el cuidado del agua?", "Datos, una conclusión, una acción propuesta y una limitación", "Así se apoya en evidencia."),
            ex("Lee: «Con estos datos de un solo día no se puede asegurar que el río esté siempre sucio». ¿Es una afirmación o una limitación?", "Una limitación", "Dice hasta dónde llegan los datos."),
            ex("Limpiar la orilla de un río con un grupo, ¿es una acción personal o colectiva?", "Colectiva", "La hace un grupo de personas."),
        ],
        "apply": [
            arith("Tres cursos de un colegio recogen 25 botellas cada uno en una jornada de limpieza. ¿Cuántas botellas recogen en total?", "3*25", "Se multiplica la cantidad de cursos por lo que recoge cada uno.", " botellas"),
            arith("Un colegio ahorra 3 litros por persona al día. Hay 200 personas y la campaña dura 5 días. ¿Cuántos litros ahorran?", "3*200*5", "Se multiplica por las personas y por los días.", " litros"),
            ex("Un curso instala basureros en la orilla de un lago del sur de Chile. ¿Qué dato sirve mejor para saber si la medida funcionó: (a) los kg de basura recogidos de la orilla antes y después, o (b) cuántas personas dicen que les gusta el lago?", "(a)", "Es un dato que se mide y se puede comparar; la opinión no muestra el efecto."),
        ],
        "reason": [
            ex("Un compañero propone «prohibir el uso de agua en el colegio». ¿Es una propuesta realista?", "No, porque las personas necesitan agua; conviene proponer reducir el gasto o evitar la contaminación", "Una propuesta debe poder cumplirse."),
            ex("Un curso ahorró 600 litros en un día y escribe: «así salvamos el río». ¿Qué le falta a esa conclusión?", "Un dato que muestre que ese ahorro llegó al río; los datos solo muestran litros ahorrados en el colegio", "Una conclusión no puede ir más allá de los datos."),
        ],
        "challenge": [
            ex("¿Cuál cartel es mejor: (a) «Cierra la llave y ahorra 22 litros por cepillado; es un cálculo de ejemplo» o (b) «Todos deben cuidar el agua, es obvio»?", "(a)", "Incluye un dato y reconoce el límite."),
            arith("Una brigada limpia una playa 4 veces en el año y recoge 80 kg de basura cada vez. ¿Cuántos kg recoge en el año?", "4*80", "Se multiplican las veces por lo recogido cada vez.", " kg"),
        ],
    },
    context=[ex("Para el Día del Agua, tu curso quiere hacer un cartel. ¿Cuál de estos datos pondrías primero para mostrar el problema: «el agua dulce es 3 de cada 100 partes» o «el agua es linda»?", "El agua dulce es 3 de cada 100 partes", "Es un dato que respalda el problema.")],
    selfcheck=[
        ex("¿Qué debe tener una propuesta de protección del agua?", "Un problema con dato, una acción posible, una razón y una limitación", "Así se apoya en evidencia."),
        ex("¿Un mensaje científico puede decir «con estos datos no se puede asegurar»?", "Sí", "Reconocer límites evita exagerar."),
        ex("Nombra una reserva de agua dulce de Chile.", "Glaciares, ríos, lagos o aguas subterráneas", "Todas son reservas hídricas."),
    ],
    open_task=task(
        "Prepara un cartel o un mensaje de un minuto para tu curso. Elige una acción: acortar la ducha (ahorra 50 litros cada vez, dato de ejemplo), cerrar la llave al cepillarse (22 litros) o limpiar la orilla de un río. Incluye: el problema con un dato, la acción, un cálculo de lo que lograría tu curso en una semana (litros ahorrados o kg de basura recogidos, según tu acción) y una limitación.",
        "Problema: el agua dulce es 3 de cada 100 partes. Acción: acortar la ducha, 50 L. Si 20 estudiantes lo hacen 5 veces por semana, ahorran 5.000 L. Limitación: son datos de ejemplo.",
        ["problema con un dato", "una acción realista", "un cálculo", "una limitación"],
        ["cartel o texto", "cálculo escrito"],
        ["proponer acciones imposibles", "no incluir ningún dato"],
        "Pregunta qué evidencia agregaría para convencer a otro curso.",
    ),
    reinforce="Escribe dos acciones de cuidado del agua, una personal y una colectiva.",
    extend="Averigua qué zonas de Chile cuentan con parques o áreas marinas protegidas y qué cuidan.",
)
