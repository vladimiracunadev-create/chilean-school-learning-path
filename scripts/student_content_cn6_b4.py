"""Cuaderno del estudiante, 6.º básico Ciencias Naturales: OA 18 (erosión, sus agentes y sus consecuencias)."""
from __future__ import annotations

from student_content_cn6_b import task
from student_lessons import arith, ex, register

OA18 = "CN06 OA 18"

# ================================================================ OA 18, clase 1
register(
    OA18, 1,
    materials="Papel y lápiz. Los casos están escritos en el cuaderno. Si quieres, observa una cuesta de tierra o un canal de agua de lluvia cerca de tu casa, sin acercarte a bordes ni a corrientes.",
    use="Aprenderé a reconocer la erosión y a separar lo que veo de la explicación que doy sobre qué la causó. Sirve para entender por qué cambia el paisaje y se pierde el suelo.",
    prior=["Sé que el suelo se forma muy lento a partir de la roca.", "Sé que el viento y el agua pueden mover materiales."],
    explain=[
        "La erosión es el desgaste de la superficie de la Tierra y el traslado de sus materiales, como tierra, arena y trozos de roca, de un lugar a otro. Los agentes que la provocan son el agua (lluvia, ríos, olas), el viento, el hielo de los glaciares y las actividades humanas, como cortar árboles sin cuidar el suelo.",
        "Veamos cuatro casos. Caso 1: en un cerro sin plantas, después de una lluvia fuerte aparecen surcos profundos en la tierra. Caso 2: en una playa, el viento mueve la arena y forma dunas. Caso 3: un río lleva agua turbia, de color café, después de llover. Caso 4: en una ladera donde se cortaron árboles, la tierra se desliza hacia abajo.",
        "Una observación es lo que vemos: «aparecen surcos». Una interpretación es la explicación: «el agua de lluvia arrastró la tierra». Para separar ambas, pregúntate qué parte se puede ver o medir y qué parte es la causa que imaginamos. Ambas son útiles, pero son cosas distintas.",
    ],
    vocab=[("erosión", "desgaste de la superficie de la Tierra y traslado de sus materiales"), ("agente de erosión", "lo que provoca la erosión, como el agua, el viento o las personas"), ("sedimento", "material suelto arrastrado, como arena o barro"), ("duna", "montículo de arena formado por el viento"), ("ladera", "pendiente de un cerro")],
    worked=[
        {"title": "Reconocer el agente", "problem": "Caso 2: el viento mueve la arena de una playa y forma dunas. ¿Cuál es el agente de la erosión?", "steps": ["Lo que mueve la arena es el viento.", "Por lo tanto, el agente es el viento."], "answer": "El viento"},
        {"title": "Observación o interpretación", "problem": "Frase A: «Aparecen surcos en el cerro después de la lluvia». Frase B: «Los surcos se formaron porque no había plantas». ¿Cuál es la observación?", "steps": ["La frase A describe lo que se ve.", "La frase B explica la causa, que no se ve directamente."], "answer": "La frase A es observación; la B es interpretación"},
    ],
    mistakes=[
        {"wrong": "Pensar que la erosión solo ocurre en los desiertos.", "why": "Se piensa que solo el viento erosiona.", "fix": "El agua también la provoca, en cualquier cerro sin protección."},
        {"wrong": "Decir que la erosión siempre es culpa de las personas.", "why": "Se ignoran los agentes naturales.", "fix": "El agua, el viento y el hielo erosionan por sí solos; las personas pueden acelerarla."},
    ],
    tiers={
        "recovery": [
            ex("Un río lleva barro y arena después de una lluvia. ¿Qué agente de erosión es: el agua o el viento?", "El agua", "El río arrastra los materiales."),
            ex("El viento mueve la arena y forma dunas. ¿Qué agente de erosión es?", "El viento", "Es el que traslada la arena."),
            ex("Se cortan todos los árboles de una ladera y la tierra se deslava. ¿Qué agente de erosión actuó, además del agua?", "Las actividades humanas", "La tala dejó sin protección al suelo."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es la erosión?", "El desgaste de la superficie y el traslado de sus materiales", "Los materiales se mueven de un lugar a otro."),
            ex("Frase: «El agua del río se ve café después de llover». ¿Observación o interpretación?", "Observación", "Se ve directamente."),
            ex("Frase: «El río está turbio porque arrastra tierra del cerro». ¿Observación o interpretación?", "Interpretación", "Explica una causa que no se ve."),
        ],
        "apply": [
            ex("Clasifica el agente de cada caso, en orden: surcos tras la lluvia en un cerro; dunas en una playa; glaciar que arrastra rocas.", "Agua, viento, hielo", "Cada caso tiene un agente distinto."),
            arith("Un cerro tiene 12 surcos antes de una lluvia y 30 surcos después. ¿Cuántos surcos nuevos aparecieron?", "30-12", "Se resta el dato inicial al final.", " surcos"),
            arith("Una duna avanza 3 metros cada año por el viento. ¿Cuántos metros avanza en 5 años si el avance es parejo?", "3*5", "Se multiplica el avance anual por los años.", " metros"),
        ],
        "reason": [
            ex("Tomás dice: «El viento formó los surcos del cerro». El cerro estaba en una zona sin viento, pero con lluvia fuerte. ¿Qué agente explica mejor los surcos?", "El agua de lluvia", "Los surcos se forman por agua que corre cuesta abajo."),
            ex("Una compañera afirma que la erosión solo la causan las personas. ¿Qué caso de la clase la contradice?", "Las dunas que forma el viento", "El viento erosiona sin intervención humana."),
        ],
        "challenge": [
            ex("Dos laderas: una con árboles y otra sin ellos. Después de la misma lluvia, la ladera sin árboles tiene más surcos. ¿Qué actividad humana pudo causar la diferencia?", "Cortar los árboles", "Sin árboles el suelo queda desprotegido."),
            arith("En una ladera sin plantas se perdieron 6 mm de suelo en 3 años por lluvias. Si la pérdida es pareja, ¿cuántos mm se pierden por año?", "6//3", "Se reparte la pérdida total en los años.", " mm"),
        ],
    },
    context=[ex("Una persona de tu casa te cuenta que después de cada lluvia el agua baja barro por la calle de un cerro cercano. ¿Qué agente de erosión es el principal en esa observación?", "El agua de lluvia", "Es el agua la que arrastra el barro.")],
    selfcheck=[
        ex("¿Qué agente de erosión forma dunas?", "El viento", "Mueve la arena."),
        ex("Una interpretación, ¿es lo que veo o la causa que explico?", "La causa que explico", "No se ve directamente."),
        ex("¿Una ladera sin plantas se erosiona más o menos que una con plantas?", "Más", "No tiene protección."),
    ],
    open_task=task(
        "Con los cuatro casos de esta clase (surcos en un cerro sin plantas, dunas por el viento, río turbio tras la lluvia, ladera deforestada), haz una tabla con tres columnas: caso, qué observo y agente que interpreto. Marca con O las observaciones y con I las interpretaciones.",
        "Caso 1: O, surcos tras la lluvia. I, el agua arrastró la tierra. Caso 2: O, dunas. I, el viento movió la arena. Caso 3: O, río café. I, arrastra tierra. Caso 4: O, la tierra se desliza. I, la tala dejó el suelo sin protección.",
        ["los cuatro casos", "observación e interpretación separadas", "agente identificado en cada caso"],
        ["tabla completa"],
        ["escribir la causa como observación", "no marcar O e I"],
        "Pregunta cuál de los casos tiene más de un agente.",
    ),
    reinforce="Observa un lugar cerca de tu casa donde haya tierra suelta y escribe una observación y una interpretación sin acercarte a bordes ni corrientes.",
    extend="Averigua con una persona de tu casa si recuerdan un lugar de tu comuna donde el agua o el viento haya cambiado el paisaje.",
)

# ================================================================ OA 18, clase 2
register(
    OA18, 2,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno. Para la tarea abierta puedes usar una bandeja con tierra y una regadera, al aire libre.",
    use="Aprenderé a formular preguntas comprobables y predicciones sobre cómo la lluvia erosiona una cuesta con distinta cobertura. Sirve para anticipar dónde habrá más erosión.",
    prior=["Conozco los agentes de la erosión.", "Sé qué es una prueba justa."],
    explain=[
        "Se puede estudiar la erosión con un modelo pequeño: una bandeja inclinada con tierra, a la que se le echa agua con una regadera, como si fuera lluvia. Se recoge en un recipiente la tierra que baja y se pesa. Esa tierra recogida, en gramos, mide la erosión.",
        "Una pregunta comprobable es: «¿una bandeja con pasto pierde menos tierra que una bandeja sin plantas?». Una prueba justa usa la misma cantidad de tierra, la misma cantidad de agua (por ejemplo, 1 litro), la misma inclinación y el mismo tiempo. Solo cambia si hay pasto o no.",
        "La predicción usa lo que sabemos: las raíces sujetan la tierra y las hojas frenan las gotas. Entonces: «Si la bandeja tiene pasto, entonces se perderá menos tierra que en la bandeja sin plantas». También podemos predecir con la inclinación: «Si la cuesta es más empinada, entonces el agua correrá más rápido y arrastrará más tierra». Si los datos contradicen la predicción, se corrige la predicción.",
    ],
    vocab=[("cobertura vegetal", "plantas que cubren el suelo"), ("inclinación", "qué tan empinada es una cuesta"), ("sedimento recogido", "tierra que bajó y se pesó"), ("prueba justa", "prueba en que cambia solo una condición"), ("regadera", "recipiente con agujeros para regar")],
    worked=[
        {"title": "Predecir con la cobertura", "problem": "Una bandeja sin plantas pierde 80 g de tierra con 1 litro de agua. ¿Qué predices para una bandeja igual, pero con pasto?", "steps": ["El pasto sujeta la tierra con raíces y frena las gotas.", "Entonces se espera una pérdida menor a 80 g."], "answer": "Perderá menos de 80 g"},
        {"title": "Reconocer lo constante", "problem": "Se comparan una bandeja con pasto y otra sin plantas, con la misma tierra, 1 litro de agua y la misma inclinación. ¿Qué cambia?", "steps": ["Los datos iguales son tierra, agua e inclinación.", "Lo que cambia es el pasto."], "answer": "Solo cambia si hay pasto o no"},
    ],
    mistakes=[
        {"wrong": "Comparar una bandeja inclinada con pasto y otra plana sin plantas.", "why": "Cambian dos condiciones.", "fix": "Deja igual la inclinación y cambia solo la cobertura."},
        {"wrong": "Predecir sin decir en qué idea te apoyas.", "why": "Se parece a adivinar.", "fix": "Usa «Si… entonces…» y nombra la idea, como que las raíces sujetan la tierra."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué se pesa en la bandeja para medir la erosión: la tierra que bajó o el agua que se echó?", "La tierra que bajó", "Esa tierra es la que se erosionó."),
            ex("¿Qué sujeta la tierra: las raíces de las plantas o el agua?", "Las raíces", "Evitan que la tierra se mueva."),
            ex("En una prueba justa, ¿cuántas condiciones cambian?", "Una", "Así se sabe la causa."),
        ],
        "understand": [
            ex("¿Cuál es una pregunta comprobable: «¿Qué bandeja es más linda?» o «¿Cuántos gramos de tierra pierde cada bandeja con 1 litro de agua?»?", "¿Cuántos gramos de tierra pierde cada bandeja con 1 litro de agua?", "Se responde pesando."),
            ex("Predicción: «Si la cuesta es más empinada, entonces se perderá más tierra». ¿En qué idea se apoya?", "En que el agua corre más rápido y arrastra más tierra", "La velocidad del agua influye en lo que arrastra."),
            ex("Una bandeja perdió 25 g y tu predicción decía 60 g. ¿Qué número es la evidencia y se queda igual?", "25 g", "El dato medido no se cambia; lo que se corrige es la predicción."),
        ],
        "apply": [
            arith("La bandeja sin plantas perdió 80 g y la bandeja con pasto perdió 20 g. ¿Cuántos gramos menos perdió la bandeja con pasto?", "80-20", "Se resta el menor al mayor.", " g"),
            arith("Una bandeja con cuesta suave perdió 30 g y otra más empinada perdió 55 g. ¿Cuántos gramos más perdió la empinada?", "55-30", "Se resta el menor al mayor.", " g"),
            ex("Una prueba compara tierra con pasto y sin pasto, pero una bandeja recibe 1 litro de agua y la otra 2 litros. ¿Qué condición no es constante?", "La cantidad de agua", "Debe ser igual en las dos bandejas."),
        ],
        "reason": [
            ex("Inés predijo que la bandeja con pasto perdería más tierra que la desnuda, pero perdió 20 g contra 80 g. ¿Qué debe corregir?", "La predicción", "La medición es la evidencia."),
            ex("Beto dice que probó con pasto, pero también usó una cuesta más suave en esa bandeja. ¿Por qué su prueba no es justa?", "Cambió dos condiciones: cobertura e inclinación", "No se sabe cuál causó la diferencia."),
        ],
        "challenge": [
            arith("Tres repeticiones de la bandeja desnuda perdieron 78, 80 y 82 g. ¿Cuál es el promedio? Suma y divide por 3.", "(78+80+82)//3", "El promedio resume pruebas repetidas.", " g"),
            ex("Una compañera predice que una bandeja cubierta con hojas secas perderá menos tierra que la desnuda. ¿Qué idea apoya su predicción?", "Que las hojas frenan las gotas de lluvia", "Las gotas golpean menos la tierra."),
        ],
    },
    context=[ex("Una persona de tu casa quiere evitar que la tierra de una ladera se vaya con la lluvia. ¿Qué predicción puedes hacer si planta pasto o arbustos en la pendiente?", "Se perderá menos tierra", "Las raíces sujetan el suelo y las hojas frenan el agua.")],
    selfcheck=[
        ex("¿Qué mide la erosión en el modelo de la bandeja?", "Los gramos de tierra que bajan", "Es lo que se erosiona."),
        ex("¿Qué predices para una cuesta más empinada?", "Más erosión", "El agua corre más rápido."),
        ex("En una prueba justa, ¿cuántas variables cambian?", "Una", "Así se identifica la causa."),
    ],
    open_task=task(
        "Diseña una prueba justa en papel para ver cuánta tierra pierde una bandeja cubierta con hojas secas frente a una bandeja sin cobertura. Escribe la pregunta comprobable, la variable que cambia, la variable que mides, tres constantes y una predicción con «Si…, entonces…». Si puedes, hazla al aire libre con una regadera y 1 litro de agua.",
        "Pregunta: ¿qué bandeja pierde menos tierra con 1 litro de agua? Cambia: la cobertura. Mido: gramos de tierra. Constantes: tierra, agua e inclinación. Predicción: si hay hojas secas, entonces se perderá menos tierra.",
        ["pregunta comprobable", "variable que cambia y la que se mide", "tres constantes y una predicción"],
        ["diseño escrito"],
        ["cambiar dos condiciones", "olvidar una constante"],
        "Pregunta qué cambiaría en su diseño si no tuviera una balanza.",
    ),
    reinforce="Escribe una predicción sobre qué pasa si llueve el doble de agua en la misma bandeja sin cobertura.",
    extend="Averigua con una persona de tu casa si en las laderas de tu barrio hay plantas o muros y para qué sirven.",
)

# ================================================================ OA 18, clase 3
register(
    OA18, 3,
    materials="Papel y lápiz. Dibuja el modelo con flechas.",
    use="Aprenderé el modelo de cómo ocurre la erosión (desprendimiento, transporte y depósito) y cómo se conectan sus agentes y consecuencias. Sirve para explicar el recorrido de la tierra desde un cerro hasta un río.",
    prior=["Conozco los agentes de la erosión.", "Sé que el suelo se forma muy lento."],
    explain=[
        "La erosión ocurre en tres pasos. Primero, el material se desprende: el agua, el viento o el hielo sueltan trozos de roca o partículas de suelo. Segundo, se transporta: el agua en un río, el viento o un glaciar lo lleva a otro lugar. Tercero, se deposita: cuando el agua o el viento pierden fuerza, el material se acumula y se llama sedimento.",
        "Las consecuencias de la erosión son varias. En el lugar de origen se pierde suelo fértil y bajan los cultivos. En el camino, el agua se pone turbia. En el lugar de destino, los sedimentos pueden tapar un río o una represa. Las actividades humanas, como cortar árboles, arar en pendientes sin cuidado o dejar demasiados animales comiendo el pasto, aceleran la erosión. Cuando una zona seca pierde su suelo fértil y se vuelve desierto, se llama desertificación.",
        "Este modelo de tres pasos tiene límites. Simplifica un proceso que a veces ocurre muy lento, durante miles de años, y a veces rápido, en una tormenta. Tampoco muestra todas las causas que se mezclan: lluvia, pendiente, plantas, personas.",
    ],
    vocab=[("desprendimiento", "paso en que el material se suelta"), ("transporte", "paso en que el material se traslada"), ("depósito", "paso en que el material se acumula"), ("sedimentación", "acumulación de sedimentos"), ("desertificación", "pérdida de suelo fértil que convierte una zona en desierto")],
    worked=[
        {"title": "Ordenar los pasos", "problem": "Ordena: (1) el material se acumula, (2) la lluvia suelta partículas del suelo, (3) el río lleva las partículas. ¿En qué orden ocurren?", "steps": ["Primero se sueltan las partículas.", "Luego se transportan.", "Finalmente se depositan."], "answer": "2, 3, 1"},
        {"title": "Seguir una consecuencia", "problem": "Una ladera sin árboles pierde tierra y el río cercano se pone café. ¿Qué paso del modelo explica el río café?", "steps": ["La tierra arrastrada llega al río.", "Eso es transporte."], "answer": "Transporte"},
    ],
    mistakes=[
        {"wrong": "Creer que la erosión termina cuando el material cae al suelo.", "why": "Se olvida el depósito.", "fix": "El material se mueve y luego se acumula en otro lugar."},
        {"wrong": "Pensar que todas las consecuencias ocurren en el mismo lugar.", "why": "No se sigue el recorrido.", "fix": "Distingue lo que pasa donde se origina, en el camino y donde se deposita."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama el paso en que el material se suelta?", "Desprendimiento", "Es el primer paso."),
            ex("¿Cómo se llama el paso en que el material se acumula?", "Depósito", "Es el último paso."),
            ex("¿Qué paso ocurre cuando el río lleva tierra?", "Transporte", "El agua traslada el material."),
        ],
        "understand": [
            ex("En Ciencias, ¿qué es un sedimento?", "Material suelto, como arena o barro, que fue arrastrado y se acumula", "Es lo que se deposita."),
            ex("¿Cuál es una consecuencia de la erosión en el lugar de origen: pérdida de suelo fértil o aumento de las lluvias?", "Pérdida de suelo fértil", "Es el efecto donde el suelo se suelta."),
            ex("¿Cuál es una limitación del modelo de tres pasos: (a) que no muestra cuánto tiempo demora cada paso o (b) que tiene tres pasos?", "(a)", "El modelo no muestra el tiempo."),
        ],
        "apply": [
            ex("Un cerro sin plantas pierde tierra con la lluvia, el río la lleva y se acumula frente a una represa. Escribe los tres pasos en orden.", "Desprendimiento, transporte, depósito", "Son los pasos del modelo."),
            arith("Un río deposita 4 cm de sedimento por año en el fondo de una represa. ¿Cuántos cm se acumulan en 6 años si la tasa es pareja?", "4*6", "Se multiplica la tasa por los años.", " cm"),
            arith("Una ladera perdió 9 mm de suelo. De ese material, 5 mm fueron transportados lejos por el río y el resto se depositó cerca. ¿Cuántos mm se depositaron cerca?", "9-5", "Se resta lo transportado lejos del total perdido.", " mm"),
        ],
        "reason": [
            ex("Rosa dice que la tala de árboles no cambia el sedimento del río. Con el modelo, ¿qué conexión la contradice?", "Sin árboles el suelo se suelta más y el río lo transporta", "La cadena conecta desprendimiento y transporte."),
            ex("Un compañero dice que el modelo muestra cuánto demora la erosión. ¿Qué respondes?", "Que no lo muestra y es una limitación", "El modelo no incluye el tiempo."),
        ],
        "challenge": [
            ex("Una zona seca con poco pasto y animales que comen todo el pasto pierde suelo por el viento y se vuelve más árida. ¿Cómo se llama ese proceso?", "Desertificación", "Es la pérdida de suelo fértil que convierte una zona en desierto."),
            ex("En un modelo, se quiere mostrar el viento como agente. ¿Qué paso del modelo representa el viento que mueve arena de una duna a otra zona?", "Transporte", "El viento traslada la arena."),
        ],
    },
    context=[ex("Después de un temporal, en una ladera sin plantas, el camino quedó cubierto de barro. ¿Qué paso del modelo explica que el barro llegara al camino?", "Transporte y depósito", "El agua lo trasladó y luego se acumuló.")],
    selfcheck=[
        ex("¿Cuáles son los tres pasos del modelo, en orden?", "Desprendimiento, transporte y depósito", "Es el recorrido del material."),
        ex("¿Qué consecuencia de la erosión baja los cultivos?", "La pérdida de suelo fértil", "Las plantas necesitan ese suelo."),
        ex("¿Qué actividad humana acelera la erosión?", "Cortar árboles", "Sin raíces el suelo se suelta más."),
    ],
    open_task=task(
        "Dibuja un cerro con un río al pie y una represa más abajo. Con flechas, muestra los tres pasos (desprendimiento, transporte y depósito) y escribe en cada lugar una consecuencia (pérdida de suelo, río turbio, sedimentos en la represa). Agrega una actividad humana que acelere el proceso y una limitación de tu modelo.",
        "Cerro: desprendimiento, se pierde suelo. Río: transporte, agua turbia. Represa: depósito, se llena de sedimento. Actividad humana: cortar árboles. Limitación: no muestra cuánto tiempo demora.",
        ["tres pasos en orden", "una consecuencia por lugar", "una actividad humana y una limitación"],
        ["dibujo", "rótulos"],
        ["poner los pasos en desorden", "olvidar la limitación"],
        "Pregunta qué cambiaría en su dibujo si el cerro tuviera árboles.",
    ),
    reinforce="Explica con los tres pasos cómo llega barro a una calle después de una lluvia fuerte.",
    extend="Averigua con una persona de tu casa si hay una represa, un tranque o un canal cerca de tu comuna y qué problema causan los sedimentos.",
)

# ================================================================ OA 18, clase 4
register(
    OA18, 4,
    materials="Papel y lápiz. Los datos están escritos en el cuaderno; son datos de ejemplo.",
    use="Aprenderé a comparar con un criterio cuánta tierra pierde una cuesta con distintas protecciones y a concluir con evidencia. Sirve para recomendar medidas contra la erosión.",
    prior=["Sé que la erosión se mide por los gramos de tierra perdidos.", "Sé qué es una prueba justa."],
    explain=[
        "Se hizo una prueba justa con cuatro bandejas inclinadas, con la misma tierra, 1 litro de agua y la misma inclinación. Datos de ejemplo de la tierra perdida: sin cobertura, 80 g; con pasto, 20 g; con hojas secas, 16 g; con piedras pequeñas, 40 g.",
        "El criterio de comparación es la tierra perdida: menos gramos significa mejor protección. Con el criterio, el orden de mejor a peor es hojas secas (16 g), pasto (20 g), piedras (40 g) y sin cobertura (80 g). Para comparar mejor se puede ver cuántas veces menos pierde cada cobertura que la bandeja sin cobertura: con pasto pierde 4 veces menos (80 ÷ 20) y con piedras 2 veces menos (80 ÷ 40).",
        "Una conclusión con evidencia: «Cualquier cobertura redujo la pérdida de tierra; la mejor fue la de hojas secas con 16 g contra 80 g». Una limitación: los datos son de ejemplo, hubo una sola prueba por bandeja y una bandeja pequeña no representa un cerro entero. Para un cerro real habría que considerar otras medidas, como terrazas o plantar árboles.",
    ],
    vocab=[("cobertura", "material que cubre el suelo"), ("terraza", "escalón en una pendiente para frenar el agua"), ("criterio de comparación", "regla para decidir qué es mejor"), ("conclusión", "idea final apoyada en datos"), ("limitación", "aspecto que reduce la confianza en los resultados")],
    worked=[
        {"title": "Comparar con el criterio", "problem": "La bandeja con pasto perdió 20 g y la bandeja con piedras perdió 40 g. ¿Cuál protegió mejor?", "steps": ["Menos gramos perdidos es mejor.", "20 es menor que 40."], "answer": "La bandeja con pasto"},
        {"title": "Cuántas veces menos", "problem": "La bandeja sin cobertura perdió 80 g y la bandeja con hojas secas 16 g. ¿Cuántas veces menos perdió la de hojas secas?", "steps": ["Se divide la pérdida mayor por la menor.", "80 ÷ 16 = 5."], "answer": "5 veces menos"},
    ],
    mistakes=[
        {"wrong": "Decir que la mejor cobertura es la que perdió más tierra.", "why": "Se invierte el criterio.", "fix": "Menos gramos perdidos es mejor protección."},
        {"wrong": "Afirmar que una bandeja pequeña muestra exactamente lo que pasa en un cerro entero.", "why": "Se olvida que es un modelo.", "fix": "Dilo como limitación del modelo."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué bandeja protegió mejor: la que perdió 16 g o la que perdió 40 g?", "La que perdió 16 g", "Menos tierra perdida es mejor."),
            ex("En el criterio de la clase, ¿qué dato se compara?", "Los gramos de tierra perdidos", "Mide la erosión."),
            ex("¿Cuál es la peor cobertura según los datos de la clase?", "Sin cobertura", "Perdió 80 g."),
        ],
        "understand": [
            ex("¿Por qué la prueba de las cuatro bandejas es justa?", "Porque solo cambia la cobertura y lo demás es igual", "Así se sabe qué causó la diferencia."),
            ex("¿Cuál es una conclusión con evidencia: (a) «Las hojas son mejores» o (b) «Con hojas secas se perdieron 16 g y sin cobertura 80 g»?", "(b)", "Cita datos medidos."),
            ex("¿Qué es una limitación de usar una bandeja pequeña para estudiar un cerro?", "Que un modelo pequeño no representa todo lo que pasa en un cerro", "El tamaño y las condiciones son distintas."),
        ],
        "apply": [
            arith("Una bandeja sin cobertura perdió 80 g y otra con piedras perdió 40 g. ¿Cuántos gramos menos perdió la de piedras?", "80-40", "Se resta el menor al mayor.", " g"),
            arith("La bandeja sin cobertura perdió 90 g y otra con pasto perdió 30 g. ¿Cuántas veces menos perdió la del pasto?", "90//30", "Se divide el mayor por el menor.", " veces"),
            ex("Ordena de mayor a menor protección: con pasto 20 g, con piedras 40 g, con hojas 16 g, sin cobertura 80 g.", "Con hojas, con pasto, con piedras, sin cobertura", "Se ordena por menos gramos perdidos."),
        ],
        "reason": [
            ex("Teo dice que las piedras son mejores que el pasto porque perdieron más tierra. ¿Qué error comete?", "Invierte el criterio: menos tierra perdida es mejor", "Las piedras perdieron más que el pasto."),
            ex("Un grupo midió 20 g y otro 21 g con el mismo pasto. ¿Los resultados son parecidos o muy distintos?", "Parecidos", "Solo difieren en 1 g."),
        ],
        "challenge": [
            arith("Se repitieron tres veces las piedras: 38, 40 y 42 g. ¿Cuál es el promedio? Suma y divide por 3.", "(38+40+42)//3", "El promedio resume pruebas repetidas.", " g"),
            ex("En un cerro real, plantar árboles protege el suelo, pero tarda años. Para una medida más rápida, ¿qué cobertura de la clase se puede poner de inmediato: hojas secas o árboles grandes?", "Hojas secas", "Se pueden poner de inmediato."),
        ],
    },
    context=[ex("Una persona de tu casa quiere proteger la tierra de una ladera de la lluvia. Con los datos de la clase, ¿qué cobertura entre hojas secas y piedras pequeñas perdió menos tierra?", "Las hojas secas", "Perdieron 16 g contra 40 g.")],
    selfcheck=[
        ex("¿Qué cobertura perdió menos tierra en los datos de la clase?", "Las hojas secas", "Perdieron 16 g."),
        ex("Una conclusión con evidencia, ¿cita datos?", "Sí", "La evidencia son los datos."),
        ex("¿Qué es mejor protección: más o menos gramos perdidos?", "Menos gramos perdidos", "Significa menos erosión."),
    ],
    open_task=task(
        "Con los datos de ejemplo (sin cobertura 90 g, pasto 18 g, hojas secas 15 g, piedras 45 g), haz una tabla ordenada de mejor a peor, calcula cuántas veces menos tierra perdió cada cobertura que la bandeja sin cobertura, y escribe una conclusión con dos datos, una limitación y una recomendación para una ladera.",
        "Orden: hojas (15 g), pasto (18 g), piedras (45 g), sin cobertura (90 g). Veces menos: hojas 6, pasto 5, piedras 2. Conclusión: toda cobertura redujo la pérdida; con hojas 15 g contra 90 g. Limitación: una sola prueba. Recomendación: plantar pasto o arbustos porque se mantiene en el tiempo.",
        ["tabla ordenada", "cálculos de veces menos correctos", "conclusión con dos datos, limitación y recomendación"],
        ["tabla", "conclusión"],
        ["ordenar al revés", "olvidar la limitación"],
        "Pregunta qué otra prueba haría para elegir entre el pasto y las hojas secas.",
    ),
    reinforce="Escribe dónde ubicarías en el orden de protección una cobertura que perdió 25 g, y explica por qué.",
    extend="Averigua con una persona de tu casa qué plantas usan en el jardín para que la tierra no se vaya con el agua o el viento.",
)
