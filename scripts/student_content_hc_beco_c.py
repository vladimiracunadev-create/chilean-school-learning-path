"""Biología de los ecosistemas (electivo 3.º y 4.º medio HC): OAC-05 (integración de la biología con otras ciencias y sus implicancias éticas, sociales y ambientales, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas salida a terreno, laboratorio ni internet. "
             "Este cuaderno no propone tomar muestras de agua, usar fertilizantes ni intervenir en cuerpos de agua reales: el caso del lago es ficticio y todas las mediciones se entregan ya escritas. Si quieres estudiar un cuerpo de agua real, hazlo con una persona docente y una institución autorizada, desde la orilla y sin tocar el agua. "
             "Las cifras son inventadas para practicar el razonamiento y no describen un lugar real.")
build = make_build(MATERIALS)

O5 = "CN-BECO-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 19 (caso ficticio del lago Claro). Un lago rodeado de campos agrícolas y de un pueblo. En verano aparecen manchas verdes de algas, el agua se enturbia y se encuentran peces muertos. "
     "Datos de ejemplo: en los últimos 10 años el fósforo y el nitrógeno disueltos en el agua han aumentado, y el oxígeno disuelto en el fondo ha disminuido. "
     "Disciplinas que podrían aportar: biología (organismos), química (nutrientes y oxígeno), física (temperatura y luz), geografía (cuenca y uso del suelo), matemática (modelos y estadística) y ciencias sociales (economía y hábitos de la comunidad).")
build(
    O5, 1, F,
    use="Aprenderé a delimitar un problema de un sistema natural y a identificar qué aportan la biología y otras ciencias para entenderlo. Sirve para valorar por qué los problemas ambientales no se resuelven desde una sola disciplina.",
    prior=["Sé qué es un ecosistema y una cadena trófica.", "Sé que las plantas necesitan nutrientes.", "Sé distinguir una observación de una explicación."],
    explain=[
        "Los problemas actuales de los sistemas naturales, como la contaminación de un lago o la pérdida de un humedal, son complejos: tienen muchas causas y afectan a muchas personas. La biología explica cómo responden los organismos y los ecosistemas, pero por sí sola no basta. La química mide sustancias como los nutrientes y el oxígeno disuelto; la física estudia la temperatura, la luz y el movimiento del agua; la geografía analiza la cuenca y el uso del suelo; la matemática construye modelos y analiza datos; y las ciencias sociales estudian cómo la economía y las costumbres de las personas influyen.",
        "Integrar conocimientos significa combinar lo que aporta cada disciplina para formar una explicación más completa. Por ejemplo, para entender por qué un lago se llena de algas hay que saber cómo crecen las algas (biología), qué nutrientes necesitan y de dónde llegan (química y geografía), cómo cambia la temperatura del agua (física), y cómo se puede predecir su evolución (matemática). Con eso se pueden proponer soluciones que tengan en cuenta a las personas.",
        "Para empezar, se delimita el sistema, es decir, la parte de la realidad que se estudia: aquí, el lago y su cuenca, que es el territorio cuyas aguas llegan a él. Luego se formula una pregunta que se pueda responder con datos y se decide qué disciplinas hacen falta. Una pregunta como «¿qué pasa con la naturaleza?» no sirve; una como «¿de dónde viene el fósforo que llega al lago y cómo cambió en diez años?» sí.",
    ],
    vocab=[("integración de saberes", "combinación de lo que aportan varias disciplinas para explicar un problema"), ("cuenca", "territorio cuyas aguas llegan a un mismo río o lago"), ("nutriente", "sustancia que los organismos necesitan para crecer, como el nitrógeno y el fósforo"), ("oxígeno disuelto", "oxígeno presente en el agua que respiran los organismos acuáticos"), ("problema complejo", "problema con muchas causas y muchas personas afectadas")],
    worked=[
        ("Asignar una disciplina", "Quieres medir cuántos microgramos de fósforo hay en un litro de agua del lago de ejemplo. ¿Qué disciplina aporta principalmente ese método?",
         ["Medir cantidades de sustancias en el agua es parte de la química.", "La biología usa luego esos datos para explicar a los organismos."],
         "La química"),
        ("Delimitar el sistema", "¿Cuál sistema está mejor delimitado: «toda el agua del planeta» o «el lago y su cuenca durante los últimos diez años»?",
         ["El primero es demasiado amplio y no tiene período.", "El segundo nombra el lugar, la cuenca y el período."],
         "El lago y su cuenca durante los últimos diez años"),
    ],
    mistakes=[("Creer que un problema ambiental se explica solo con biología.", "Intervienen sustancias químicas, la geografía del lugar, la física del agua y las decisiones de las personas.", "Lista qué aporta cada disciplina antes de explicar."),
              ("Mezclar el sistema con la solución: «el sistema es construir una planta de tratamiento».", "El sistema es lo que se estudia (el lago y su cuenca); la solución es una acción posible.", "Primero delimita el sistema y la pregunta; luego propone soluciones.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es una cuenca?", "Un territorio cuyas aguas llegan a un mismo río o lago", "El fondo de un lago", "Un tipo de alga", "La cuenca reúne el territorio que aporta agua al lago, por eso su uso del suelo importa."),
        ("{F} ¿Qué dato de la ficha ha disminuido en el fondo del lago?", "El oxígeno disuelto", "La ficha indica que el oxígeno disuelto en el fondo ha disminuido."),
        ("{F} ¿Qué dos nutrientes han aumentado en el agua?", "El fósforo y el nitrógeno", "La ficha nombra el fósforo y el nitrógeno como nutrientes que aumentaron."),
        ("abc", "{F} ¿Qué disciplina estudia el uso del suelo de la cuenca que rodea al lago?", "La geografía", "La matemática", "La química", "La geografía analiza cuencas y uso del suelo."),
        ("abc", "{F} ¿Qué disciplina aporta el método para predecir cómo cambiarán las algas con distintos escenarios?", "La matemática, con modelos y análisis de datos", "La física, midiendo la luz", "La biología sola, sin cálculo", "Un modelo numérico permite probar escenarios y predecir."),
        ("ab", "{F} ¿Por qué el estudio del lago necesita más de una disciplina?", "Porque el problema tiene causas químicas, físicas, geográficas, biológicas y sociales", "Porque cada disciplina mide lo mismo con palabras distintas", "Un problema complejo no se explica completo desde un solo punto de vista."),
        ("abc", "{F} Una compañera dice que el problema del lago es solo «de plantas». ¿Qué respondes?", "Es más amplio: involucra nutrientes, oxígeno, uso del suelo y decisiones de las personas", "Tiene razón: solo la biología importa", "Tiene razón porque las algas son plantas", "Las algas son parte del problema, pero también lo son sus causas y consecuencias."),
        ("abc", "¿Cuál es una pregunta bien delimitada para el caso?", "¿De dónde viene el fósforo que llega al lago y cómo cambió su cantidad en diez años?", "¿Qué pasa con la naturaleza?", "¿Es malo el verano?", "La primera nombra una sustancia, un lugar y un período."),
        ("abc", "{F} ¿Qué disciplina estudia cómo los hábitos y la economía de la comunidad influyen en el uso del fertilizante?", "Las ciencias sociales", "La física", "La química del agua", "Las ciencias sociales analizan decisiones y costumbres humanas."),
        ("abc", "{F} Se propone estudiar solo el lago, sin su cuenca. ¿Qué se pierde?", "Saber de dónde llegan los nutrientes al lago", "Nada importante", "Saber cuántas algas hay", "Los nutrientes llegan desde la cuenca, así que sin ella falta una causa."),
        ("ab", "Un equipo propone estudiar «el agua del mundo» para entender el lago. ¿Qué falla?", "El sistema es demasiado amplio y no permite responder con datos del lago", "Nada, mientras más grande mejor", "Delimitar significa acotar para poder responder con datos concretos."),
        ("Ordena de lo más específico a lo más general: (a) el lago Claro, (b) la cuenca del lago Claro, (c) todos los lagos del país. Escribe las letras separadas por comas.", "a, b, c", "Un lago está dentro de su cuenca, y esta dentro del conjunto de todos los lagos del país."),
        ("{F} Escribe la sigla de la disciplina que mediría el oxígeno disuelto (B = biología, Q = química, F = física, G = geografía). Responde con una letra.", "Q", "Medir la concentración de una sustancia en el agua es un método propio de la química."),
    ],
    ctx=("abc", "Contexto: tu liceo de ejemplo está junto a una laguna que se tiñó de verde en verano. Debes proponer cómo empezar a estudiarla. ¿Qué plan es mejor?", "Delimitar la laguna y su cuenca, formular una pregunta con datos y reunir a quienes aportan desde química, geografía, biología y ciencias sociales", "Opinar sin datos", "Estudiar solo las algas", "Un plan integrado delimita el sistema, formula una pregunta y suma disciplinas."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un nutriente?", "Una sustancia que los organismos necesitan para crecer", "Los nutrientes, como el nitrógeno y el fósforo, sostienen el crecimiento."),
        ("ab", "Integrar saberes significa:", "Combinar lo que aportan varias disciplinas", "Usar solo la mejor disciplina", "Un problema complejo exige explicaciones que reúnan varios puntos de vista."),
        ("ab", "Una pregunta bien delimitada:", "Se puede responder con datos concretos", "Es tan amplia que sirve para todo", "Acotar el sistema permite medir y comparar con datos."),
    ],
    op=("Con la ficha {F}: (1) escribe una pregunta bien delimitada sobre el lago; (2) elige tres disciplinas y escribe qué aportaría cada una; (3) explica en dos oraciones por qué una sola disciplina no basta.",
        "(1) ¿De dónde viene el fósforo que llega al lago y cómo cambió su cantidad en diez años? (2) Química: mide fósforo y oxígeno; geografía: identifica campos y pueblo de la cuenca; biología: explica el crecimiento de algas y el efecto en peces. (3) El problema tiene causas en la cuenca y efectos en los organismos; ninguna disciplina ve todo.",
        ["pregunta con sistema y período", "tres aportes diferentes y precisos", "explicación de por qué una sola disciplina no basta"],
        ["tres respuestas numeradas"],
        ["hacer una pregunta demasiado amplia", "repetir el mismo aporte en distintas disciplinas", "no justificar la integración"],
        "Pregunta: «¿qué disciplina agregarías para tener en cuenta a las personas?»."),
    reinforce="Elige un problema de tu entorno (por ejemplo, la basura en un río) y escribe tres disciplinas que ayudarían a entenderlo, con un aporte cada una.",
    extend="Explica por qué delimitar el sistema, incluyendo la cuenca, es un paso previo a proponer soluciones.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 20 (datos de ejemplo del lago Claro, rodeado de campos y de un pueblo). Fósforo en el agua, en microgramos por litro: año 1: 20; año 5: 35; año 10: 50. Oxígeno disuelto en el fondo, en miligramos por litro: año 1: 8; año 5: 5; año 10: 2. "
     "Fertilizante aplicado en los campos de la cuenca, en kilogramos por hectárea: año 1: 100; año 10: 160. "
     "Fuente A: informe de una universidad con método y datos publicados. Fuente B: encuesta de un vecino a 5 personas, sin método descrito. Fuente C: registro de ventas de una cooperativa agrícola de la zona.")
build(
    O5, 2, F,
    use="Aprenderé a evaluar fuentes de distintas disciplinas y a trabajar con variables en unidades distintas. Sirve para decidir qué evidencia es confiable y qué conclusiones permite en un problema complejo.",
    prior=["Sé qué es una variable y una unidad.", "Sé calcular cambios porcentuales.", "Sé que la asociación no prueba por sí sola una causa."],
    explain=[
        "En un problema complejo se usan fuentes de distintos tipos: informes de universidades, registros de empresas, encuestas, mapas y observaciones de la comunidad. Cada una tiene fortalezas y límites. Un informe con método y datos publicados se puede revisar; una encuesta a pocas personas sin método describe opiniones pero no mide el fenómeno; un registro de ventas informa sobre el uso de un producto, pero quien lo produce puede tener intereses económicos.",
        "Cada disciplina mide variables con sus propias unidades: microgramos por litro para el fósforo, miligramos por litro para el oxígeno, kilogramos por hectárea para el fertilizante. Para comparar cambios entre variables de unidades distintas se usa el cambio relativo, es decir, el cambio dividido por el valor inicial y multiplicado por cien. Así se ve cuál variable cambió más en proporción.",
        "Cuando varias variables cambian en el mismo período, como el fertilizante, el fósforo y el oxígeno, hay una asociación entre ellas. Para atribuir una causa se necesita además un mecanismo plausible, como que el fósforo es un nutriente que favorece el crecimiento de algas, y comparaciones que descarten otras explicaciones. Una conclusión sólida es la que se apoya en varias fuentes independientes.",
    ],
    vocab=[("cambio relativo", "cambio dividido por el valor inicial y expresado en porcentaje"), ("unidad", "patrón con que se expresa una medida, como microgramos por litro"), ("fuente independiente", "fuente que obtuvo sus datos por un camino distinto de otra"), ("mecanismo plausible", "explicación creíble de cómo una causa produce un efecto"), ("muestra", "parte de un conjunto sobre la que se mide o se pregunta")],
    worked=[
        ("Calcular un cambio relativo", "En un río de ejemplo, el nitrato pasó de 10 a 15 miligramos por litro. ¿Cuál fue el cambio relativo?",
         ["Cambio = 15 − 10 = 5.", "5 ÷ 10 × 100 = 50."],
         "50 % de aumento"),
        ("Evaluar una fuente", "Una encuesta de ejemplo a 5 vecinos dice que «el lago está peor que antes». ¿Qué tipo de evidencia es?",
         ["Recoge percepciones.", "No describe un método de medición ni usa una muestra grande."],
         "Evidencia de percepción, útil como pista pero insuficiente por sí sola"),
    ],
    mistakes=[("Comparar directamente 50 microgramos por litro con 160 kilogramos por hectárea como si fueran la misma magnitud.", "Las unidades y las magnitudes son distintas y no se pueden restar ni comparar tal cual.", "Compara los cambios relativos de cada variable."),
              ("Descartar toda fuente que viene de una empresa.", "Hay que revisar método y datos y contrastar con otras fuentes; el origen exige cuidado, no descarte automático.", "Pide el método y compara con una fuente independiente.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es el cambio relativo?", "El cambio dividido por el valor inicial y expresado en porcentaje", "La diferencia entre dos valores en cualquier unidad", "El valor más grande de una serie", "Permite comparar variables con unidades distintas porque se expresa en porcentaje."),
        ("{F} ¿Cuántos microgramos por litro de fósforo había en el año 10?", "50", "La ficha indica 50 microgramos por litro de fósforo en el año 10."),
        ("=", "{F} ¿Cuántos microgramos por litro aumentó el fósforo entre el año 1 y el año 10?", "50-20", "Se resta el valor del año 1 al del año 10.", " microgramos por litro"),
        ("=", "{F} ¿Qué porcentaje aumentó el fósforo entre el año 1 y el año 10?", "(50-20)/20*100", "El cambio relativo es el aumento dividido por el valor inicial.", " %"),
        ("=", "{F} ¿Qué porcentaje bajó el oxígeno disuelto entre el año 1 y el año 10?", "(8-2)/8*100", "El cambio relativo es la baja dividida por el valor inicial.", " %"),
        ("=", "{F} ¿Qué porcentaje aumentó el fertilizante aplicado entre el año 1 y el año 10?", "(160-100)/100*100", "El cambio relativo es el aumento dividido por el valor inicial.", " %"),
        ("abc", "{F} ¿Qué fuente muestra su método y datos publicados?", "La Fuente A", "La Fuente B", "La Fuente C", "Solo el informe universitario publica método y datos que se pueden revisar."),
        ("abc", "{F} ¿Por qué la Fuente B es una evidencia débil para medir el fenómeno?", "Tiene una muestra muy pequeña y no describe método", "Porque la escribió un vecino", "Porque pregunta por el lago", "Una muestra pequeña sin método solo recoge percepciones."),
        ("abc", "{F} ¿Qué limita el uso de la Fuente C como evidencia sobre el lago?", "Mide ventas de la cooperativa y no lo que llega al lago, y quien la produce tiene intereses económicos", "Que no tiene números", "Que está escrita en español", "Su registro es indirecto y debe contrastarse."),
        ("ab", "{F} El fertilizante, el fósforo y el oxígeno cambian en el mismo período. ¿Qué se puede decir con la ficha?", "Que están asociados y que se necesita un mecanismo y comparaciones para atribuir causa", "Que el fertilizante es la única causa del problema", "Los datos muestran asociación; la causa necesita más evidencia."),
        ("abc", "{F} ¿Qué mecanismo plausible une el fósforo con las algas?", "El fósforo es un nutriente que favorece el crecimiento de algas", "Las algas producen fósforo para el agua", "El fósforo enfría el agua", "Un mecanismo es una explicación de cómo una causa produce un efecto."),
        ("abc", "¿Qué haría más sólida la conclusión sobre el origen del fósforo?", "Comparar con otra fuente independiente, como el análisis de un laboratorio externo", "Repetir lo mismo con la misma fuente", "Eliminar los datos del año 1", "Fuentes independientes que coinciden fortalecen la conclusión."),
        ("abc", "{F} Una persona dice: «los datos prueban que el fertilizante es la única causa». ¿Qué respondes?", "No: hay asociación, pero pueden existir otras fuentes de fósforo, como las aguas del pueblo", "Sí, porque ambos suben", "Sí, porque la cooperativa lo informó", "Atribuir una causa única exige descartar otras explicaciones."),
    ],
    ctx=("abc", "Contexto: en una asamblea, una vecina del lago de ejemplo dice que «con 5 personas que opinan lo mismo ya está probado». ¿Qué respuesta es más adecuada?", "Que las opiniones sirven de pista, pero hace falta medir con método para probarlo", "Que tiene toda la razón", "Que las opiniones no valen nada", "Las percepciones orientan la investigación; la prueba exige mediciones con método."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es una fuente independiente?", "Una fuente que obtuvo sus datos por un camino distinto de otra", "Si dos fuentes independientes coinciden, la conclusión es más sólida."),
        ("ab", "Para comparar variables con unidades distintas se usa:", "El cambio relativo", "La suma de los valores", "El porcentaje permite comparar proporciones, no unidades."),
        ("ab", "Una asociación entre variables:", "No prueba por sí sola una causa", "Siempre prueba una causa", "Se necesita mecanismo y comparación además de la asociación."),
    ],
    op=("Con la ficha {F}: (1) calcula el cambio relativo del fósforo, del oxígeno y del fertilizante; (2) evalúa las Fuentes A, B y C con un criterio para cada una; (3) escribe una conclusión prudente y una limitación.",
        "(1) Fósforo +150 %, oxígeno −75 %, fertilizante +60 %. (2) A muestra método y datos; B es una muestra pequeña sin método; C mide ventas y tiene interés económico. (3) El fósforo aumentó mientras bajó el oxígeno y subió el fertilizante; con estos datos no se descartan otras fuentes de fósforo.",
        ["tres cambios relativos correctos", "criterio por fuente", "conclusión con limitación"],
        ["tres respuestas numeradas"],
        ["dividir por el valor final", "tratar las tres fuentes como iguales", "afirmar una causa única"],
        "Pregunta: «¿qué otra fuente independiente buscarías?»."),
    reinforce="Elige tres variables de un problema ambiental de tu entorno, escribe sus unidades y qué disciplina las mediría.",
    extend="Explica por qué un cambio de 50 % en una variable no es comparable con un aumento de 50 unidades en otra.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 21 (modelo integrado de ejemplo para el lago Claro). Cadena de efectos propuesta: más fertilizante y aguas del pueblo → más fósforo y nitrógeno en el lago → más algas → al morir, las algas son descompuestas por bacterias, que consumen oxígeno → menos oxígeno en el fondo → mueren peces. "
     "Datos de ejemplo del modelo, en unidades de ejemplo. Escenario actual: fósforo 50, algas 80, oxígeno 2. Escenario con la mitad del fertilizante y aguas del pueblo tratadas: fósforo 25, algas 40, oxígeno 5. "
     "Supuesto del modelo: el fósforo acumulado en el sedimento del fondo no se libera.")
build(
    O5, 3, F,
    use="Aprenderé a interpretar un modelo que integra biología, química, física y factores sociales para predecir el efecto de una decisión. Sirve para evaluar escenarios y reconocer los supuestos y límites de un modelo.",
    prior=["Sé qué es un modelo y para qué sirve.", "Sé calcular porcentajes.", "Sé leer una cadena de causas y efectos."],
    explain=[
        "Un modelo integrado reúne conocimientos de varias disciplinas en una cadena de causas y efectos. En el caso del lago, la actividad humana aporta nutrientes; la química explica que el fósforo y el nitrógeno limitan el crecimiento de las algas; la biología explica que, al morir, las algas son descompuestas por bacterias que consumen oxígeno; y la física explica que, en verano, el agua más cálida y tranquila se mezcla menos, lo que deja el fondo con poco oxígeno.",
        "Un modelo sirve para comparar escenarios: qué pasaría si se reduce el fertilizante o se trata el agua del pueblo. Se cambian los datos de entrada y se observa el resultado. Esto permite elegir medidas con más fundamento antes de gastar recursos. Pero todo modelo tiene supuestos, que son las condiciones que da por ciertas, y límites, que son lo que deja fuera. Si un supuesto falla, el resultado puede ser distinto.",
        "En este caso el modelo supone que el fósforo ya acumulado en el sedimento no se libera. En la realidad, el sedimento puede devolver fósforo al agua cuando hay poco oxígeno, y eso retrasa la recuperación aunque se reduzcan los aportes nuevos. Valorar la integración de saberes es también valorar la honestidad de decir qué predice el modelo y qué no.",
    ],
    vocab=[("modelo integrado", "modelo que combina conocimientos de varias disciplinas"), ("escenario", "situación hipotética con ciertos valores de entrada"), ("supuesto", "condición que el modelo da por cierta"), ("sedimento", "material que se deposita en el fondo de un cuerpo de agua"), ("recuperación", "vuelta de un sistema a un estado más sano")],
    worked=[
        ("Comparar escenarios", "En un modelo de ejemplo, el escenario A tiene algas 60 y el B tiene algas 30. ¿Cuántas algas menos hay en B?",
         ["Se resta el valor de B al de A.", "60 − 30 = 30."],
         "30 unidades menos"),
        ("Reconocer un supuesto que falla", "Un modelo supone que el sedimento no libera fósforo. Si lo libera, ¿qué pasará con la recuperación del lago?",
         ["El fósforo del sedimento vuelve al agua.", "Aunque se reduzcan los aportes nuevos, seguirá habiendo fósforo disponible para las algas.", "La recuperación será más lenta."],
         "Será más lenta"),
    ],
    mistakes=[("Creer que si se detiene el aporte de nutrientes, el lago se recupera de inmediato.", "El fósforo ya acumulado en el sedimento puede seguir alimentando a las algas por años.", "Declara el tiempo de recuperación como una incertidumbre del modelo."),
              ("Tomar los números del modelo como predicciones exactas.", "Son valores de ejemplo y dependen de supuestos que pueden fallar.", "Presenta el resultado como una tendencia con supuestos declarados.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un supuesto de un modelo?", "Una condición que el modelo da por cierta", "El resultado final del modelo", "Un dato medido en terreno", "Los supuestos son condiciones aceptadas para que el modelo funcione."),
        ("abc", "{F} Según el modelo, ¿qué provoca el aumento de las algas?", "El mayor aporte de fósforo y nitrógeno", "Menos oxígeno en el fondo", "La muerte de peces", "La cadena del modelo comienza con nutrientes que estimulan el crecimiento de algas."),
        ("{F} ¿Qué organismos consumen oxígeno al descomponer las algas muertas?", "Las bacterias", "En la ficha, las bacterias descomponedoras consumen oxígeno al descomponer las algas."),
        ("=", "{F} ¿Cuántas unidades menos de algas tiene el escenario con medidas respecto del escenario actual?", "80-40", "Se resta el valor del escenario con medidas al del escenario actual.", " unidades"),
        ("=", "{F} ¿Cuántas unidades más de oxígeno hay en el escenario con medidas?", "5-2", "Se resta el oxígeno del escenario actual al del escenario con medidas.", " unidades"),
        ("=", "{F} ¿Qué porcentaje del fósforo actual queda en el escenario con medidas?", "25/50*100", "Se divide el fósforo del escenario con medidas por el actual y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Qué disciplina explica por qué el fondo del lago tiene poco oxígeno en verano si el agua está cálida y tranquila?", "La física, que estudia temperatura y mezcla del agua", "La geografía", "La economía", "La mezcla y la temperatura del agua son fenómenos físicos."),
        ("abc", "{F} ¿Qué disciplina aporta el método para medir cuánto fósforo y nitrógeno hay disueltos en el agua?", "La química, que mide sustancias", "La física, que mide la temperatura", "La geografía, que describe el uso del suelo", "Medir la cantidad de nutrientes disueltos es un método de la química."),
        ("ab", "{F} ¿Qué puede ocurrir si el sedimento sí libera fósforo?", "La recuperación del lago será más lenta de lo que predice el modelo", "La recuperación será más rápida que en el modelo", "El fósforo del sedimento mantiene alimentadas a las algas."),
        ("abc", "{F} Alguien dice que, con la mitad del fertilizante, el lago estará sano al instante. ¿Qué advertencia hace falta?", "El modelo supone que el sedimento no libera fósforo y la recuperación puede tardar", "Ninguna: el modelo es perfecto", "El oxígeno nunca cambia", "Hay que considerar el tiempo de recuperación y los supuestos."),
        ("abc", "{F} Además del fertilizante, ¿qué otra fuente de nutrientes se reduce en el escenario con medidas?", "Las aguas del pueblo, que pasan a ser tratadas", "El sedimento del fondo", "La luz del Sol", "El escenario con medidas incluye aguas del pueblo tratadas, que aportan menos nutrientes al lago."),
        ("abc", "¿Qué tipo de decisión permite probar un modelo antes de gastar recursos?", "Comparar escenarios con distintos valores de entrada", "Elegir sin comparar", "Esperar a que el lago empeore", "Los escenarios permiten evaluar medidas antes de aplicarlas."),
        ("abc", "{F} Un estudiante cambia el modelo y supone que los peces no necesitan oxígeno. ¿Qué problema tiene el cambio?", "Contradice la biología, porque los peces respiran oxígeno disuelto", "Ninguno", "Mejora el modelo", "Un supuesto debe ser coherente con el conocimiento disciplinar."),
    ],
    ctx=("abc", "Contexto: el municipio de ejemplo duda entre reducir el fertilizante, tratar las aguas del pueblo o ambas medidas. ¿Cómo ayuda el modelo?", "Permite comparar los tres escenarios con valores de entrada distintos, declarando sus supuestos", "Decide por sí solo cuál es la mejor", "Reemplaza la medición en el lago", "Un modelo orienta la decisión, pero no la reemplaza."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un escenario?", "Una situación hipotética con ciertos valores de entrada", "Los escenarios permiten comparar qué pasaría con distintas decisiones."),
        ("ab", "El sedimento puede:", "Devolver fósforo al agua cuando hay poco oxígeno", "Absorber todo el fósforo sin liberarlo jamás", "Esa liberación retrasa la recuperación del lago."),
        ("ab", "Un modelo integrado:", "Combina conocimientos de varias disciplinas", "Usa solo biología", "Integrar disciplinas da una explicación más completa."),
    ],
    op=("Con la ficha {F}: (1) explica la cadena de efectos en tres oraciones indicando qué disciplina aporta cada eslabón; (2) calcula cuánto cambian las algas y el oxígeno entre el escenario actual y el escenario con medidas; (3) escribe un supuesto del modelo, por qué podría fallar y qué efecto tendría.",
        "(1) Los campos y el pueblo aportan nutrientes (ciencias sociales y geografía); el fósforo y el nitrógeno alimentan algas (química y biología); al morir, las bacterias consumen oxígeno y el fondo queda con poco, por el agua cálida y quieta (biología y física). (2) Algas bajan 40 unidades (50 %) y el oxígeno sube 3 unidades. (3) Supone que el sedimento no libera fósforo; si lo libera, la recuperación sería más lenta.",
        ["cadena ordenada con disciplinas", "dos cálculos correctos", "supuesto con consecuencia"],
        ["tres respuestas numeradas"],
        ["invertir la cadena de efectos", "dar solo números sin explicar", "no declarar ningún supuesto"],
        "Pregunta: «¿qué dato real necesitarías para comprobar el supuesto?»."),
    reinforce="Dibuja con palabras la cadena de efectos del modelo y marca en cada flecha qué disciplina la explica.",
    extend="Explica por qué un modelo útil debe incluir, además de cifras, una lista de sus supuestos y de lo que no considera.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 22 (decisión de ejemplo sobre el lago Claro). Cuatro grupos afectados: la cooperativa agrícola, los pescadores artesanales, el municipio que toma agua potable del lago y un grupo de turismo de la orilla. "
     "Medidas posibles, con datos de ejemplo. Medida 1, limitar el fertilizante en la cuenca: costo 40 unidades, reduce el fósforo en 40 %; lo paga sobre todo la cooperativa. "
     "Medida 2, tratar las aguas del pueblo: costo 60 unidades, reduce el fósforo en 30 %; lo paga el municipio. Medida 3, franjas de vegetación nativa en las orillas: costo 20 unidades, reduce el fósforo en 20 %; la pagan en partes iguales cooperativa y municipio. "
     "Un lago con menos fósforo beneficia a los cuatro grupos. Supuesto de ejemplo: las reducciones se suman cuando se aplican varias medidas.")
build(
    O5, 4, F,
    use="Aprenderé a analizar una decisión sobre un sistema natural considerando sus implicancias éticas, sociales y ambientales, y a valorar la integración de la biología con otras ciencias. Sirve para justificar una propuesta sin olvidar a las personas ni al ecosistema.",
    prior=["Sé qué es un criterio y una matriz de decisión.", "Sé calcular razones y porcentajes.", "Sé distinguir un dato de una opinión."],
    explain=[
        "Una decisión sobre un sistema natural afecta a personas con intereses distintos. La ciencia aporta evidencia sobre qué medidas funcionan, pero decidir qué hacer también implica valores. Las implicancias éticas son las preguntas de lo que es justo o correcto, como quién paga, quién se beneficia y quién queda en riesgo. Las implicancias sociales se refieren a las personas y comunidades, y las ambientales, al ecosistema y a las generaciones futuras.",
        "Algunos principios ayudan a razonar. La equidad pide repartir de forma justa los costos y beneficios. La precaución pide actuar para evitar daños graves aunque haya incertidumbre científica. La participación pide que las personas afectadas puedan opinar y decidir, con información clara. La transparencia pide mostrar los datos, los supuestos y los intereses detrás de cada propuesta. Estos principios no reemplazan a los datos: se usan junto con ellos.",
        "Un análisis integrado compara las medidas por su eficacia, su costo, quién las paga y a quién benefician. Un indicador simple es el costo por punto de reducción: costo ÷ porcentaje de reducción. Pero el número solo no decide: una medida barata puede cargar todo el costo a un solo grupo. Valorar la integración de saberes es reconocer que la mejor propuesta combina evidencia científica, criterios éticos y participación de la comunidad.",
    ],
    vocab=[("implicancia ética", "pregunta de justicia o de lo correcto que plantea una decisión"), ("equidad", "reparto justo de costos y beneficios"), ("principio de precaución", "actuar para evitar daños graves aunque haya incertidumbre científica"), ("participación", "derecho de las personas afectadas a opinar y decidir con información"), ("transparencia", "mostrar los datos, los supuestos y los intereses detrás de una propuesta")],
    worked=[
        ("Calcular el costo por punto", "Una medida de ejemplo cuesta 50 unidades y reduce 25 % del contaminante. ¿Cuál es el costo por punto de reducción?",
         ["Costo por punto = 50 ÷ 25.", "50 ÷ 25 = 2."],
         "2 unidades por punto"),
        ("Relacionar un principio con un caso", "Una medida de ejemplo le carga todo el costo a un solo grupo, aunque benefician a todos. ¿Qué principio se cuestiona?",
         ["Se evalúa quién paga y quién se beneficia.", "El reparto no es justo entre los grupos."],
         "La equidad"),
    ],
    mistakes=[("Elegir la medida más barata sin mirar quién la paga.", "El costo total no dice cómo se reparte; puede cargar a un grupo con una carga injusta.", "Analiza quién paga y quién se beneficia con cada medida."),
              ("Creer que la ciencia por sí sola decide qué es lo mejor.", "La ciencia informa sobre efectos, pero la decisión involucra valores y participación de las personas.", "Usa la evidencia junto con criterios éticos y consulta a los afectados.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué pide el principio de equidad?", "Repartir de forma justa los costos y beneficios", "Que todos paguen exactamente lo mismo siempre", "Que decida solo quien más sabe", "La equidad se refiere a un reparto justo, no necesariamente igual."),
        ("{F} ¿Qué porcentaje de reducción del fósforo logra la Medida 1?", "40 %", "La ficha indica que la Medida 1 reduce el fósforo en 40 %."),
        ("=", "{F} ¿Cuál es el costo por punto de reducción de la Medida 1?", "40/40", "Se divide el costo de 40 unidades entre los 40 puntos de reducción.", " unidades por punto"),
        ("=", "{F} ¿Cuál es el costo por punto de reducción de la Medida 2?", "60/30", "Se divide el costo de 60 unidades entre los 30 puntos de reducción.", " unidades por punto"),
        ("abc", "{F} ¿Qué medida tiene el mayor costo por punto de reducción?", "La Medida 2", "La Medida 1", "La Medida 3", "La Medida 2 cuesta 2 por punto, y las medidas 1 y 3 cuestan 1."),
        ("=", "{F} Si se aplican las medidas 1 y 3, ¿qué reducción total del fósforo se logra?", "40+20", "Según el supuesto, las reducciones se suman.", " %"),
        ("=", "{F} ¿Cuál es el costo total de aplicar las medidas 1 y 3 juntas?", "40+20", "El costo total suma los costos de las dos medidas.", " unidades"),
        ("abc", "{F} ¿Qué grupo carga principalmente con el costo de la Medida 1?", "La cooperativa agrícola", "Los pescadores artesanales", "El grupo de turismo", "La ficha indica que lo paga sobre todo la cooperativa."),
        ("abc", "{F} ¿Qué pregunta ética plantea la Medida 1?", "Si es justo que la cooperativa pague casi todo, aunque los beneficios sean para varios grupos", "Si el fósforo es un nutriente", "Si el lago es grande", "Plantea cómo se reparten costos y beneficios."),
        ("ab", "{F} Un vecino dice: «aún no hay certeza total de que el fósforo cause las algas, así que no se haga nada». ¿Qué principio se invoca en contra?", "El principio de precaución, que pide actuar ante daños graves aunque haya incertidumbre", "La equidad, que pide que todos paguen exactamente lo mismo", "La precaución no exige certeza absoluta cuando el daño puede ser grave."),
        ("abc", "{F} ¿Qué haría más participativa la decisión del municipio?", "Informar con claridad y escuchar a los cuatro grupos afectados antes de decidir", "Decidir sin consultar", "Consultar solo a quienes ya están de acuerdo", "La participación supone información clara y voz para los afectados."),
        ("abc", "{F} Una empresa propone una medida y no muestra sus datos ni sus intereses. ¿Qué principio se incumple?", "La transparencia", "La equidad en el reparto de costos", "La precaución", "Mostrar datos e intereses es lo que pide la transparencia."),
        ("abc", "{F} ¿Qué recomendación integra mejor evidencia, equidad y participación?", "Combinar medidas de costos repartidos entre varios grupos y consultar a la comunidad", "Elegir solo la medida más barata", "No hacer nada para no generar conflictos", "Integrar significa considerar datos, justicia y participación a la vez."),
    ],
    ctx=("abc", "Contexto: en una asamblea de ejemplo, un grupo pide que se aplique la Medida 1 y otro dice que la Medida 2 es más justa. ¿Cómo conviene ordenar la discusión?", "Comparar eficacia, costo y quién paga de cada medida con los datos de la ficha y escuchar a todos los grupos", "Votar sin mostrar datos", "Aceptar lo que diga la persona con más cargo", "Una discusión informada usa datos y criterios éticos compartidos."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es el principio de precaución?", "Actuar para evitar daños graves aunque haya incertidumbre científica", "La precaución se invoca cuando el daño posible es grave."),
        ("ab", "La transparencia consiste en:", "Mostrar datos, supuestos e intereses", "Ocultar los intereses", "Mostrar lo que hay detrás permite evaluar una propuesta."),
        ("ab", "La ciencia en una decisión ambiental:", "Informa los efectos, y se suma a criterios éticos", "Decide sola sin considerar a las personas", "La decisión también involucra valores y participación."),
    ],
    op=("Con la ficha {F}: (1) calcula el costo por punto de reducción de las tres medidas; (2) escribe qué grupo se beneficia y qué grupo paga en la medida que prefieras; (3) redacta una propuesta de tres oraciones que combine evidencia, un principio ético (equidad, precaución, participación o transparencia) y una valoración de por qué importó integrar la biología con otras ciencias.",
        "(1) 1, 2 y 1 unidades por punto. (2) La Medida 3 beneficia a los cuatro grupos y la pagan por partes iguales la cooperativa y el municipio. (3) Propongo las medidas 1 y 3, que reducen el fósforo 60 % a un costo de 60; reparto el costo entre cooperativa y municipio por equidad y consulto a los cuatro grupos. Sin química, biología, matemática y ciencias sociales no habría visto el problema completo.",
        ["tres costos por punto correctos", "grupo beneficiado y grupo que paga", "propuesta con evidencia, principio y valoración de la integración"],
        ["tres respuestas numeradas"],
        ["olvidar quién paga", "no nombrar un principio ético", "no explicar por qué importó integrar disciplinas"],
        "Pregunta: «¿qué grupo faltó considerar en tu propuesta?»."),
    reinforce="Elige un problema de tu entorno y escribe qué grupos afecta, qué medida propones y qué principio ético aplicarías.",
    extend="Explica por qué la ciencia necesita criterios éticos y participación para decidir qué hacer con un ecosistema.",
)
