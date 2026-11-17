"""Ciencias de la salud (electivo 3.º y 4.º medio HC): OAC-01 (perspectiva sistémica de problemas de salud pública, clases 1 a 6) y OAC-02 (genoma y ambiente, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, internet ni medir a nadie. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos, no diagnostica ni da consejos médicos personales, y no incluye procedimientos clínicos ni dosis. "
             "Las cifras de salud son ilustrativas: sirven para practicar el análisis, no para tomar decisiones sobre tu salud. "
             "Si un tema te preocupa a ti o a alguien cercano, cuéntaselo a una persona adulta de confianza o a un profesional de salud; si necesitas orientación inmediata, el Fono Niños 147 puede ayudarte.")
build = make_build(MATERIALS)

O1 = "CN-CSAL-3y4-OAC-01"
O2 = "CN-CSAL-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso de ejemplo en un liceo ficticio). Durante un mes de invierno, 40 de los 800 estudiantes faltaron por una infección respiratoria. "
     "La sala 1 tiene 40 estudiantes y sus ventanas están cerradas todo el día. La sala 2 tiene 25 estudiantes y se ventila en cada recreo. "
     "El liceo tiene un solo comedor para todos. Además, el 30 % del curso A vive en una misma población donde hubo muchos casos. "
     "Elementos de la cadena de transmisión: el agente (el microorganismo), la fuente (la persona que lo tiene), la vía de transmisión (por el aire o por contacto) y el huésped susceptible (la persona que puede enfermar).")
build(
    O1, 1, F,
    use="Aprenderé a mirar un problema de salud pública como un sistema, a delimitar su escala y a formular una pregunta que se pueda responder con evidencia. Sirve para no confundir un problema complejo con una sola causa.",
    prior=["Sé que algunos microorganismos pueden causar enfermedades.", "Distingo una causa de un efecto.", "Sé leer una pequeña tabla de datos."],
    explain=[
        "La salud pública se ocupa de la salud de las poblaciones: cuántas personas enferman, por qué y cómo se puede prevenir. Los problemas que estudia, como las infecciones, el consumo de drogas, las infecciones de transmisión sexual, los desequilibrios alimentarios o las enfermedades del trabajo, son complejos porque tienen varias causas que se influyen entre sí: biológicas, de conducta, sociales y del ambiente.",
        "Una perspectiva sistémica mira el problema como un sistema, es decir, un conjunto de partes que interactúan. En una infección respiratoria las partes son el agente, la fuente, la vía de transmisión, las personas susceptibles y el ambiente donde se juntan, como una sala cerrada o un comedor. Si solo se mira una parte, se puede proponer una solución que arregla poco, porque el resto del sistema sigue funcionando igual.",
        "Para estudiar un problema complejo primero se delimita. Se elige la escala, que puede ser local (un liceo, una comuna) o global (un país o el mundo), se fijan los límites del sistema y se escribe una pregunta concreta. Una pregunta bien delimitada nombra qué se compara y con qué dato se responderá. Delimitar no es esconder el resto: se reconoce lo que queda fuera.",
    ],
    vocab=[("salud pública", "ciencia y práctica que cuidan la salud de poblaciones y previenen problemas colectivos"), ("sistema", "conjunto de partes que interactúan entre sí"), ("variable", "característica que puede cambiar y que se mide o se compara"), ("vía de transmisión", "modo en que un agente pasa de una persona a otra"), ("escala", "tamaño del espacio estudiado, local o global")],
    worked=[
        ("Reconocer las partes de un sistema", "Una persona con resfrío tose en un bus cerrado y otra, sentada cerca, se contagia días después. Identifica la fuente, la vía y el huésped.",
         ["La fuente es la persona que tiene el agente: la que tose.", "La vía de transmisión es el aire del bus, que lleva gotitas con el agente.", "El huésped susceptible es la persona que se contagió."],
         "Fuente: quien tose. Vía: el aire. Huésped: quien se contagió."),
        ("Delimitar una pregunta", "Quieres estudiar las enfermedades profesionales. ¿Cuál pregunta está mejor delimitada: «¿por qué se enferma la gente en el trabajo?» o «¿baja el ruido en un taller si se aísla una máquina?»",
         ["La primera no fija lugar, enfermedad ni dato con el que responder.", "La segunda nombra un taller, una variable que se mide (el ruido) y una acción que se compara.", "Con una medición antes y después se puede responder."],
         "La segunda pregunta"),
    ],
    mistakes=[("Creer que el problema tiene una sola causa y buscar un culpable único.", "En los problemas complejos varias causas interactúan y se refuerzan entre sí.", "Dibuja las partes del sistema y las relaciones entre ellas antes de proponer una solución."),
              ("Plantear una pregunta tan amplia que no se puede contestar con datos.", "Sin escala, límites ni variable concreta no hay evidencia que la responda.", "Fija lugar, grupo, variable y qué se compararía.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué estudia la salud pública?", "La salud de las poblaciones y cómo prevenir los problemas que las afectan", "Solo el tratamiento de una persona enferma en un consultorio", "Solo los medicamentos que se venden en farmacias", "La salud pública mira poblaciones y prevención, no solo la atención de un caso individual."),
        ("{F} ¿Cómo se llama el modo en que el agente pasa de una persona a otra, por ejemplo por el aire?", "Vía de transmisión", "La vía de transmisión es el camino que sigue el agente entre personas."),
        ("ab", "{F} El caso de la ficha ocurre en un solo liceo. ¿A qué escala se estudia?", "Local", "Global", "Un solo liceo es un espacio acotado, es decir, una escala local."),
        ("abc", "{F} ¿Cuál de estas preguntas está mejor delimitada?", "¿Hay menos ausentes por infección respiratoria en la sala que se ventila (sala 2) que en la sala de ventanas cerradas (sala 1)?", "¿Cómo se terminan todas las enfermedades del mundo?", "¿Por qué las personas se enferman?", "La primera nombra lugar, una variable y una comparación que se puede responder con datos."),
        ("abc", "{F} El comedor único del liceo corresponde, en el sistema de la ficha, a:", "Una parte del ambiente donde pueden juntarse fuentes y personas susceptibles", "El agente infeccioso", "El huésped susceptible", "El comedor es un lugar compartido, es decir, ambiente donde hay contacto entre personas."),
        ("=", "En un curso de ejemplo de 40 estudiantes (sala 1) hubo 10 con infección y en otro de 25 (sala 2) hubo 3. ¿Cuántos puntos porcentuales más tuvo la sala 1 que la sala 2?", "10/40*100-3/25*100", "En la sala 1 fue 25 % y en la sala 2 fue 12 %, y la diferencia es de 13 puntos.", " puntos porcentuales"),
        ("abc", "Quieres delimitar el problema «consumo de alcohol entre estudiantes de un liceo». ¿Cuál es el mejor primer paso?", "Fijar la escala (un liceo), el grupo y la pregunta que se quiere responder", "Buscar cualquier cifra mundial y copiarla", "Proponer de inmediato una prohibición", "Delimitar comienza por fijar escala, grupo y pregunta, antes de buscar evidencia o proponer soluciones."),
        ("{F} ¿Qué porcentaje de los 800 estudiantes faltó por infección respiratoria?", "5 %", "Son 40 de 800, es decir, 5 de cada 100 estudiantes."),
        ("abc", "{F} En la ficha se compara la sala 1 con la sala 2. ¿Qué condición es la que cambia entre ambas?", "La ventilación", "El mes de invierno", "El nombre del liceo", "El mes y el liceo son iguales para ambas salas, así que lo que cambia es la ventilación."),
        ("abc", "{F} Alguien dice: «la causa de las ausencias es solo el ambiente cerrado». ¿Qué responde una mirada sistémica?", "Hay varias partes que interactúan: agente, personas susceptibles, ambiente y hogares", "Tiene razón, las personas no influyen", "Tiene razón porque la ventilación lo explica todo", "El sistema incluye varias causas que interactúan, por eso una sola explicación queda incompleta."),
        ("abc", "{F} ¿Qué dato de la ficha sugiere que el problema no se limita al liceo?", "Que el 30 % del curso A vive en una población donde hubo muchos casos", "Que la sala 2 se ventila en cada recreo", "Que la sala 1 tiene 40 estudiantes", "Los casos en un barrio muestran contagio también fuera del liceo, en el hogar o la comunidad."),
        ("abc", "{F} El liceo propone solo ventilar las salas. ¿Qué limitación tiene esa solución?", "No cambia lo que ocurre en el comedor ni en los hogares, así que puede resolver solo una parte", "Ventilar siempre empeora el problema", "Ventilar es imposible en invierno", "Una medida sobre una parte del sistema no resuelve las otras vías de contacto."),
        ("abc", "El liceo cierra el comedor y todos almuerzan en sus salas con ventanas cerradas. ¿Qué riesgo sistémico aparece?", "Se podría aumentar el contacto prolongado en salas cerradas, y el problema se trasladaría", "No hay ningún riesgo, porque el comedor era la única causa", "El riesgo desaparece porque cada curso está separado", "Mover a las personas a otra parte del sistema puede crear un nuevo foco, por eso se piensa en el sistema completo."),
    ],
    ctx=("abc", "Contexto: tu liceo tiene muchas ausencias por resfríos en invierno y el centro de estudiantes quiere hacer algo. ¿Qué propuesta es más sistémica?", "Revisar juntos ventilación de salas, uso del comedor y mensajes a las familias sobre quedarse en casa con síntomas", "Pedir que nadie hable en clases", "Culpar al curso con más ausentes", "Una propuesta sistémica actúa sobre varias partes: el ambiente, las rutinas y la comunidad."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un sistema?", "Un conjunto de partes que interactúan entre sí", "Un sistema se define por las relaciones entre sus partes, no solo por las partes."),
        ("ab", "Una pregunta de investigación bien delimitada:", "Nombra qué se compara y con qué dato se responderá", "Abarca todos los problemas posibles de salud", "Delimitar significa acotar lugar, variable y comparación para poder responder."),
        ("ab", "Una escala global se refiere a:", "Un país o el mundo", "Una sola sala de clases", "La escala global abarca territorios amplios, mientras que una sala es una escala local."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) dibuja un esquema con las partes del sistema (agente, fuente, vía, huésped y ambiente) usando datos de la ficha; (2) escribe una pregunta bien delimitada y su escala; (3) nombra una parte del sistema que tu pregunta deja fuera y por qué.",
        "(1) Fuente: estudiantes con infección. Vía: aire de las salas y contacto en el comedor. Huésped: estudiantes susceptibles. Ambiente: sala 1 cerrada, sala 2 ventilada, comedor y hogares. (2) «¿Tuvo menos ausencias la sala 2 que la sala 1 en un mes de invierno?» Escala local. (3) Deja fuera los hogares, porque no hay datos de ellos.",
        ["esquema con las cinco partes del sistema", "pregunta con lugar, variable y comparación", "indica la escala", "nombra algo que queda fuera con una razón"],
        ["esquema, pregunta y límite numerados"],
        ["dibujar solo una causa", "plantear una pregunta sin comparación", "no reconocer ningún límite"],
        "Pregunta: «¿qué dato de la ficha te permitiría decidir si la ventilación sola basta?»."),
    reinforce="Elige un problema de salud que conozcas por noticias y escribe sus partes: agente o factor, personas, ambiente y una pregunta con escala local.",
    extend="Explica por qué una pregunta puede ser local aunque el problema sea global, y qué ganas y pierdes al delimitar así.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo sobre alimentación de estudiantes). "
     "Fuente 1: una encuesta de un servicio de salud ficticio a 1.000 estudiantes elegidos al azar en 20 liceos; el 35 % declara tomar bebidas azucaradas todos los días y el 42 % declara hacer menos de 30 minutos de actividad física a la semana. Los datos se obtuvieron con un cuestionario anónimo y el método se describe completo. "
     "Fuente 2: una publicación anónima en una red social que dice «el 90 % de los jóvenes come solo comida chatarra», sin explicar cómo se midió. "
     "Fuente 3: un estudio de una empresa que vende un suplemento, realizado con 12 personas elegidas por la propia empresa, que concluye que su producto «mejora la salud de todos».")
build(
    O1, 2, F,
    use="Aprenderé a evaluar si una fuente de datos de salud es confiable y a distinguir las variables que se miden, se comparan o pueden confundir un resultado. Sirve para no creer cifras solo porque suenan fuertes.",
    prior=["Sé qué es un porcentaje.", "Sé que una encuesta pregunta a un grupo de personas.", "Distingo una opinión de un dato."],
    explain=[
        "No todas las fuentes valen lo mismo. Para evaluar una fuente de salud se pregunta quién la produjo, cómo obtuvo los datos, a cuántas personas midió, si sus datos son recientes y si tiene un interés económico en el resultado. Una fuente confiable explica su método, de modo que otra persona podría revisar o repetir el trabajo. Una afirmación sin método, sin autor o con un interés comercial pide más cautela.",
        "También importa la muestra, que es el grupo de personas realmente medido. Una muestra representativa refleja a la población que se quiere conocer, por ejemplo cuando las personas se eligen al azar. Una muestra pequeña o elegida por quien tiene interés puede dar resultados que no sirven para todos. Además, en una encuesta las personas declaran lo que creen o recuerdan, y eso puede no coincidir exactamente con lo que hacen.",
        "Las variables son las características que se miden o se comparan. Cuando se estudia si una conducta se relaciona con un efecto en la salud, puede haber una variable confusora: una tercera característica, como el ingreso familiar, que influye en ambas y puede crear una relación que parece causal. Que dos cosas aparezcan juntas es una asociación; para afirmar causa se necesita más evidencia.",
    ],
    vocab=[("muestra representativa", "grupo medido que refleja a la población que se quiere conocer"), ("conflicto de interés", "situación en que quien informa gana algo con cierto resultado"), ("variable confusora", "tercera característica que influye en dos variables y puede crear una falsa relación entre ellas"), ("asociación", "relación entre dos variables que aparecen juntas, sin probar que una cause la otra"), ("método", "forma en que se obtuvieron los datos")],
    worked=[
        ("Evaluar una fuente", "Una página dice que «el 70 % de las personas mejora con la bebida Z» y no indica a cuántas personas midió ni quién la hizo. ¿Qué haces?",
         ["Pregunta por el autor y el método: no están indicados.", "Pregunta por la muestra: no se sabe cuántas personas fueron.", "Sin método ni muestra no se puede revisar el dato."],
         "Se usa con cautela y se busca otra fuente que explique su método"),
        ("Variable confusora", "En un liceo ficticio, los estudiantes que duermen más tienen mejores notas. Pero también tienen menos horas de trabajo en la tarde. ¿Qué es esto último?",
         ["Es una tercera característica que podría influir en el sueño y en las notas.", "Por eso la relación puede no ser una causa directa."],
         "Una variable confusora"),
    ],
    mistakes=[("Creer una cifra porque es muy alta o aparece en muchas publicaciones.", "Que algo se repita no prueba que se haya medido bien.", "Revisa quién la produjo y cómo la obtuvo."),
              ("Concluir que una conducta causa un efecto solo porque aparecen juntos.", "Puede haber variables confusoras u otras explicaciones.", "Di que hay una asociación y busca más evidencia.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es una muestra representativa?", "Un grupo medido que refleja a la población que se quiere conocer", "El grupo más fácil de encontrar", "El grupo cuyos resultados son más llamativos", "Una muestra es útil cuando se parece a la población, no cuando es cómoda o llamativa."),
        ("{F} ¿Qué fuente (1, 2 o 3) puede tener un conflicto de interés porque quien la publica vende un producto?", "Fuente 3", "La empresa del suplemento gana si el resultado es favorable a su producto."),
        ("ab", "Una fuente de salud es más confiable cuando:", "Explica cómo obtuvo los datos y quién los produjo", "Sus afirmaciones son más contundentes", "Mostrar el método permite que otras personas revisen el dato, y la contundencia no lo prueba."),
        ("=", "{F} Según la Fuente 1, ¿cuántos de los 1.000 estudiantes declaran tomar bebidas azucaradas todos los días?", "1000*35/100", "El 35 % de 1.000 son 350 estudiantes.", " estudiantes"),
        ("abc", "{F} Un amigo dice: «la Fuente 3 prueba que el suplemento sirve para todos». ¿Cuál es el principal problema?", "Son solo 12 personas elegidas por quien vende el producto", "Que la empresa tiene demasiados clientes", "Que usa números", "Doce personas elegidas por la empresa no representan a todos y hay interés comercial."),
        ("abc", "Se compara el consumo de bebidas azucaradas con la actividad física. Los estudiantes más activos tienen en general mayores ingresos familiares. El ingreso familiar sería:", "Una variable confusora que podría explicar parte de la diferencia", "El resultado final que se mide", "Un dato sin ninguna importancia", "El ingreso influye en la alimentación y en la actividad, así que puede confundir la relación."),
        ("=", "{F} Según la Fuente 1, ¿cuántos puntos porcentuales más de estudiantes declaran hacer poca actividad física que los que toman bebidas azucaradas a diario?", "42-35", "Son 42 % y 35 %, y la diferencia es de 7 puntos.", " puntos porcentuales"),
        ("abc", "{F} ¿Qué datos faltan en la Fuente 2 para evaluarla?", "Cómo se midió el 90 % y a quiénes", "El color de la publicación", "El número de personas que la leyó", "Sin método ni muestra no se puede saber si la cifra es válida."),
        ("abc", "En una encuesta anónima, una persona declara cuántas bebidas toma. Una limitación de este tipo de dato es que:", "Lo declarado puede diferir de lo que realmente hace", "Las encuestas nunca sirven", "Siempre se llena con respuestas verdaderas", "Declarar depende de la memoria y de lo que cada persona quiere decir."),
        ("abc", "Un estudio de ejemplo muestra que en meses con más ventas de helados hay más ahogamientos en piscinas. ¿Qué explica mejor la asociación?", "Una tercera variable, el calor del verano, que influye en ambas", "Los helados causan ahogamientos", "Los ahogamientos aumentan las ventas de helados", "El calor lleva a comprar helados y a ir a piscinas, y por eso se asocian sin ser causa uno del otro."),
        ("abc", "¿Qué fortalece más una afirmación de salud?", "Varias fuentes independientes que coinciden y explican cómo midieron", "Una publicación muy compartida en redes", "Una afirmación repetida muchas veces", "La coincidencia de estudios independientes con método claro da más confianza que la popularidad."),
        ("abc", "{F} Debes elegir una fuente como base para un trabajo escolar sobre alimentación. ¿Cuál eliges y con qué cuidado?", "La Fuente 1, reconociendo que los datos son declarados y pueden subestimar", "La Fuente 3, porque es la más optimista", "La Fuente 2, porque es la más corta", "La Fuente 1 es abierta en su método y con muestra al azar; igual conviene anotar la limitación."),
        ("abc", "{F} Para estudiar si las bebidas azucaradas se relacionan con ausencias a clases, ¿qué agregarías a la Fuente 1?", "Medir también las ausencias y variables como actividad física e ingreso familiar en los mismos estudiantes", "Preguntar solo a quien quiera responder", "Repetir la misma pregunta con otras palabras", "Para estudiar la relación hay que medir ambas variables en las mismas personas y controlar posibles confusoras."),
    ],
    ctx=("abc", "Contexto: en tu curso circula un mensaje que dice «el 80 % de los adolescentes tiene problemas por no desayunar», sin autor ni método. ¿Qué haces antes de compartirlo?", "Busco la fuente original y reviso su método y su muestra", "Lo comparto porque la cifra es alta", "Lo comparto con una nota diciendo que es seguro", "Revisar autor, método y muestra evita difundir datos que nadie verificó."),
    sc=[
        ("En Ciencias de la salud: ¿qué es una variable confusora?", "Una tercera característica que influye en dos variables y puede crear una falsa relación", "La confusora explica por qué dos variables parecen conectadas sin que una cause la otra."),
        ("ab", "Una asociación entre dos variables:", "No prueba por sí sola que una cause la otra", "Prueba siempre una causa", "Dos variables pueden aparecer juntas por una tercera o por azar."),
        ("ab", "Una muestra elegida al azar suele ser:", "Más representativa que una elegida por quien tiene interés", "Menos útil que cualquier otra", "Al elegir al azar, quien tiene interés no decide quiénes entran a la muestra."),
    ],
    op=("Con las fuentes de la ficha {F} haz lo siguiente: (1) evalúa cada fuente con tres preguntas (quién, cómo midió, a cuántas personas); (2) elige una fuente para un informe y justifica; (3) nombra una variable confusora posible para la relación entre bebidas azucaradas y ausencias.",
        "(1) F1: servicio de salud, cuestionario anónimo, 1.000 estudiantes al azar. F2: anónima, sin método, sin muestra. F3: empresa que vende, 12 personas elegidas por ella. (2) Elijo F1 porque explica su método y su muestra; su límite es que los datos son declarados. (3) El ingreso familiar.",
        ["evalúa las tres fuentes con las tres preguntas", "elige una fuente con razón basada en método o muestra", "reconoce una limitación de la fuente elegida", "nombra una variable confusora creíble"],
        ["tres fuentes evaluadas, elección y confusora"],
        ["elegir por el resultado que gusta", "no mencionar el método", "confundir asociación con causa"],
        "Pregunta: «¿qué cambiaría tu elección si la Fuente 1 hubiera encuestado solo a un liceo?»."),
    reinforce="Escribe tres preguntas que harías a cualquier fuente de salud antes de creerle, y explica para qué sirve cada una.",
    extend="Explica con un ejemplo propio cómo una variable confusora puede hacer que dos cosas parezcan relacionadas sin que una cause la otra.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (modelo de ejemplo de una infección que pasa de persona a persona). Ronda 0: hay 1 caso. En cada ronda, cada caso nuevo contagia a un número fijo de personas, que llamaremos «contagios por caso». "
     "Escenario A (sin medidas): 2 contagios por caso. Escenario B (con medidas como ventilar, lavarse las manos y quedarse en casa con síntomas): 1 contagio por caso. "
     "Bucle de refuerzo: más casos llevan a más contagios, que llevan a más casos. Bucle de equilibrio: más casos llevan a más aislamiento en casa, que lleva a menos contagios. "
     "Supuestos del modelo: todas las personas tienen el mismo contacto, nadie tiene defensas previas y no se consideran vacunas.")
build(
    O1, 3, F,
    use="Aprenderé a construir e interpretar un modelo simple de cómo se propaga una infección, con sus bucles de refuerzo y de equilibrio, y a declarar los supuestos del modelo. Sirve para entender por qué pequeñas medidas pueden cambiar mucho el resultado.",
    prior=["Sé multiplicar y sumar.", "Sé que una infección puede pasar de una persona a otra.", "Distingo causa de efecto."],
    explain=[
        "Un modelo es una versión simplificada de la realidad que sirve para entender y predecir. En salud pública, un modelo de propagación dice cuántas personas contagia cada caso. Si cada caso contagia a dos personas en cada ronda, los casos nuevos son 1, 2, 4, 8, y así se duplican. Si cada caso contagia solo a una, los casos nuevos se mantienen en 1: el problema deja de crecer.",
        "En un sistema hay bucles. Un bucle de refuerzo amplifica un cambio: más casos producen más contagios y más casos. Un bucle de equilibrio lo frena: más casos llevan a más personas en aislamiento y a menos contagios. El resultado depende de cuál bucle domina. Las medidas de prevención buscan fortalecer el bucle de equilibrio, y por eso un pequeño cambio en los contagios por caso puede cambiar mucho el resultado final.",
        "Todo modelo tiene supuestos y límites. Este modelo supone que todas las personas tienen el mismo contacto, que nadie tiene defensas previas y que el número de contagios por caso no cambia. En la realidad esos supuestos varían. Un buen análisis dice qué supone el modelo y qué no permite concluir: ocultar los supuestos es un error frecuente, porque hace parecer exacto lo que es una simplificación.",
    ],
    vocab=[("modelo", "versión simplificada de la realidad que sirve para explicar y predecir"), ("bucle de refuerzo", "relación en que un cambio se amplifica a sí mismo"), ("bucle de equilibrio", "relación en que un cambio se frena a sí mismo"), ("supuesto", "condición que se da por cierta para que el modelo funcione"), ("ronda", "paso del modelo en que los casos contagian a otras personas")],
    worked=[
        ("Leer el modelo", "Con 2 contagios por caso y 1 caso inicial, ¿cuántos casos nuevos hay en la ronda 3?",
         ["Ronda 0: 1 caso. Ronda 1: 1 por 2 = 2.", "Ronda 2: 2 por 2 = 4.", "Ronda 3: 4 por 2 = 8."],
         "8 casos nuevos"),
        ("Cambiar un parámetro", "En un modelo de ejemplo con 3 contagios por caso y 1 caso inicial, ¿cuántos casos nuevos hay en la ronda 2 y cómo cambia si se reduce a 1 contagio por caso?",
         ["Con 3 contagios: ronda 1 tiene 3 casos y ronda 2 tiene 3 por 3 = 9.", "Con 1 contagio por caso: todas las rondas tienen 1 caso.", "La diferencia en la ronda 2 es de 9 menos 1 = 8 casos."],
         "9 casos con 3 contagios, 1 caso con 1 contagio por caso"),
    ],
    mistakes=[("Presentar el resultado del modelo como una predicción exacta de la realidad.", "El modelo solo es tan bueno como sus supuestos, y la realidad varía.", "Escribe qué supone el modelo y qué no permite concluir."),
              ("Confundir un bucle de refuerzo con uno de equilibrio.", "El de refuerzo amplifica el cambio y el de equilibrio lo frena.", "Pregúntate si el cambio inicial aumenta o disminuye después de recorrer el bucle.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es un bucle de refuerzo?", "Una relación en que un cambio se amplifica a sí mismo", "Una relación en que un cambio se frena a sí mismo", "Una medida de prevención", "Un bucle de refuerzo hace crecer el cambio original, como más casos que producen más contagios."),
        ("=", "{F} En el escenario A, ¿cuántos casos nuevos más hay en la ronda 3 que en la ronda 1?", "8-2", "La ronda 1 tiene 2 casos nuevos y la ronda 3 tiene 8, así que hay 6 más.", " casos"),
        ("ab", "{F} El aislamiento en casa de las personas con síntomas actúa como:", "Un bucle de equilibrio, porque frena los contagios", "Un bucle de refuerzo, porque aumenta los contagios", "Aislarse reduce los contagios, y esa acción que frena el crecimiento es de equilibrio."),
        ("=", "{F} En el escenario A, ¿cuántos casos nuevos hay en la ronda 4?", "2*2*2*2", "Cada ronda duplica los casos: 2, 4, 8 y 16.", " casos"),
        ("=", "{F} En el escenario A, ¿cuántos casos suman en total las rondas 0, 1, 2 y 3?", "1+2+4+8", "Se suman los casos de cada ronda: 1, 2, 4 y 8.", " casos"),
        ("ab", "{F} En el escenario B, los casos nuevos de cada ronda:", "Se mantienen en 1", "Se duplican en cada ronda", "Con un contagio por caso, cada caso es reemplazado por uno solo."),
        ("abc", "{F} ¿Qué supuesto del modelo puede no cumplirse en un liceo real?", "Que todas las personas tienen el mismo contacto", "Que hay una ronda 0", "Que los casos se cuentan con números", "En un liceo unas personas se juntan más que otras, y eso cambia los contagios."),
        ("=", "{F} Si una medida lleva el escenario de 2 a 1 contagio por caso, ¿cuántos casos menos hay en la ronda 4 que en el escenario A?", "2*2*2*2-1", "En A hay 16 casos y en B hay 1 en esa ronda, es decir, 15 casos menos.", " casos"),
        ("abc", "Un modelo de ejemplo con 4 contagios por caso parte con 1 caso. ¿Cuántos casos nuevos hay en la ronda 3?", "64", "12", "16", "Cada ronda se multiplica por 4: 4, 16 y 64."),
        ("abc", "{F} Alguien dice: «el modelo prueba que en el liceo habrá exactamente 16 casos en la ronda 4». ¿Qué respondes?", "Que es una simplificación con supuestos y no una predicción exacta", "Que sí, el modelo siempre acierta", "Que el modelo no sirve para nada", "El modelo muestra una tendencia bajo ciertos supuestos, no una cifra segura."),
        ("abc", "{F} ¿Por qué ventilar y quedarse en casa con síntomas pueden cambiar mucho el resultado final?", "Reducen los contagios por caso, y ese número se multiplica en cada ronda", "Porque eliminan el modelo", "Porque aumentan los casos iniciales", "Un cambio pequeño en el número que se multiplica produce una diferencia grande después de varias rondas."),
        ("abc", "{F} Si cada persona con síntomas se queda en casa, ¿qué parte del sistema fortaleces?", "El bucle de equilibrio, porque disminuye los contactos", "El bucle de refuerzo, porque aumentan los contactos", "Ninguna, porque el aislamiento no cambia nada", "Menos contacto reduce los contagios, que es lo que hace el bucle de equilibrio."),
        ("abc", "{F} ¿Qué dato no incluye el modelo y sería importante para decidir en un liceo real?", "Cuántas personas tienen defensas previas o vacunas", "El nombre del modelo", "El número de rondas del ejemplo", "El modelo supone que nadie tiene defensas, y eso puede cambiar mucho los contagios."),
    ],
    ctx=("abc", "Contexto: en una clase te piden presentar el modelo de contagios a tu curso. ¿Cómo lo presentas de manera honesta?", "Muestro los resultados de los dos escenarios y digo qué supone el modelo y qué no permite concluir", "Digo que los números son lo que ocurrirá en nuestro liceo", "Muestro solo el escenario con más casos para asustar", "Un modelo se presenta con sus escenarios, sus supuestos y sus límites."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un supuesto de un modelo?", "Una condición que se da por cierta para que el modelo funcione", "Los supuestos simplifican la realidad y limitan lo que el modelo permite concluir."),
        ("ab", "Un bucle de equilibrio:", "Frena un cambio", "Amplifica un cambio", "El equilibrio devuelve el sistema hacia valores más estables, frenando el cambio."),
        ("ab", "Con 1 contagio por caso, la infección en el modelo:", "No crece", "Se duplica en cada ronda", "Si cada caso es reemplazado por uno solo, el número de casos nuevos se mantiene."),
    ],
    op=("Con el modelo de la ficha {F} haz lo siguiente: (1) calcula los casos nuevos de las rondas 1 a 3 en el escenario A y en el B; (2) explica en dos oraciones qué bucle domina en cada escenario; (3) escribe un supuesto del modelo y cómo podría cambiar el resultado si no se cumple.",
        "(1) A: 2, 4, 8. B: 1, 1, 1. (2) En A domina el bucle de refuerzo porque los casos se duplican. En B domina el de equilibrio porque las medidas frenan los contagios. (3) Supone que todas las personas tienen el mismo contacto. Si unas personas se juntan mucho más, los casos podrían crecer más rápido en esos grupos.",
        ["calcula bien las tres rondas de A y de B", "explica qué bucle domina en cada escenario", "nombra un supuesto del modelo", "indica un efecto posible si no se cumple"],
        ["tres partes numeradas"],
        ["sumar en vez de multiplicar", "no distinguir los bucles", "presentar el modelo como predicción exacta"],
        "Pregunta: «¿qué cambiarías en el modelo para acercarlo a un liceo real?»."),
    reinforce="Dibuja un esquema con flechas donde se vea un bucle de refuerzo y uno de equilibrio para el contagio en un liceo, y rotula cada uno.",
    extend="Explica por qué pasar de 2 a 1 contagio por caso tiene un efecto mucho mayor después de varias rondas que al inicio.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (tabla de ejemplo de una ciudad ficticia sobre infecciones de transmisión sexual, ITS, en personas jóvenes). "
     "Año 1: 40.000 jóvenes en la ciudad, 2.000 exámenes de detección realizados y 100 casos detectados. "
     "Año 2: 40.000 jóvenes en la ciudad, 4.000 exámenes realizados y 160 casos detectados. "
     "Nota: las ITS son infecciones que se transmiten por contacto sexual; muchas pueden no dar síntomas, por lo que solo se detectan con un examen. Algunas se previenen con vacunas. Las barreras como el preservativo y los exámenes oportunos reducen el riesgo, aunque ninguna medida lo elimina por completo.")
build(
    O1, 4, F,
    use="Aprenderé a analizar evidencia de salud pública, como la diferencia entre casos detectados y personas realmente infectadas, usando datos de ejemplo de infecciones de transmisión sexual. Sirve para no sacar conclusiones apresuradas de una cifra que sube.",
    prior=["Sé calcular un porcentaje.", "Sé que algunas infecciones se transmiten por contacto.", "Sé comparar dos números de una tabla."],
    explain=[
        "Las infecciones de transmisión sexual (ITS) son un problema de salud pública porque muchas no producen síntomas y pueden pasar de una persona a otra sin que se note. Se previenen con información, vacunas contra algunos agentes, barreras como el preservativo y exámenes oportunos, que permiten tratar a tiempo las infecciones que se pueden curar. Hablar de ellas con datos y sin juicios ayuda a que las personas consulten sin miedo a un profesional de salud.",
        "Al analizar evidencia hay que distinguir qué mide realmente un dato. Los casos detectados dependen de cuántos exámenes se hacen: si se examina a más personas, se encuentran más casos aunque la cantidad de infectados no haya subido. Por eso se calcula también la positividad, que es el porcentaje de exámenes con resultado positivo. Si los casos detectados suben pero la positividad baja, el aumento puede deberse en gran parte a más exámenes.",
        "Una tasa compara casos con el tamaño de la población, por ejemplo casos por cada 10.000 personas, y permite comparar ciudades o años distintos. Aun así, una tabla de ejemplo no muestra por qué cambian los números ni dice qué hizo cada persona. La evidencia se usa para tomar decisiones colectivas, no para juzgar a personas, y cualquier duda personal se conversa con un profesional de salud o con una persona adulta de confianza.",
    ],
    vocab=[("ITS", "infección de transmisión sexual, que pasa de una persona a otra por contacto sexual"), ("positividad", "porcentaje de exámenes cuyo resultado es positivo"), ("tasa", "número de casos en relación con el tamaño de la población"), ("detección", "hallazgo de una infección mediante un examen"), ("prevención", "acciones que reducen el riesgo antes de que ocurra el problema")],
    worked=[
        ("Calcular positividad", "En un año de ejemplo se hicieron 500 exámenes y hubo 25 positivos. ¿Cuál es la positividad?",
         ["Positividad es positivos dividido por exámenes: 25 entre 500.", "25 entre 500 es 5 centésimos.", "Como porcentaje es 5 %."],
         "5 %"),
        ("Calcular una tasa", "Una comuna de ejemplo tiene 20.000 jóvenes y 50 casos. ¿Cuál es la tasa por cada 10.000?",
         ["Se divide 50 entre 20.000.", "Se multiplica por 10.000 para expresarlo por cada 10.000 personas.", "50 por 10.000 entre 20.000 es 25."],
         "25 casos por cada 10.000 jóvenes"),
    ],
    mistakes=[("Concluir que hay más infectados solo porque subieron los casos detectados.", "Los casos detectados dependen de cuántos exámenes se hacen.", "Calcula también la positividad antes de sacar conclusiones."),
              ("Usar la evidencia para señalar o juzgar a personas.", "Los datos de salud pública describen poblaciones, no culpan a individuos.", "Habla de tasas y medidas de prevención, y respeta la privacidad.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la positividad de un examen?", "El porcentaje de exámenes cuyo resultado es positivo", "El número total de personas de la ciudad", "El costo de cada examen", "La positividad compara los resultados positivos con todos los exámenes realizados."),
        ("{F} ¿Cuántos casos más se detectaron en el año 2 que en el año 1?", "60", "160 menos 100 son 60 casos más."),
        ("ab", "{F} Según la nota, muchas ITS pueden no dar síntomas. Por eso solo se detectan:", "Con un examen", "Esperando que aparezcan señales", "Si no hay síntomas, solo un examen permite saber si hay infección."),
        ("=", "{F} ¿Cuál fue la positividad del año 1?", "100/2000*100", "Son 100 positivos de 2.000 exámenes, es decir, 5 %.", " %"),
        ("=", "{F} ¿Cuál fue la positividad del año 2?", "160/4000*100", "Son 160 positivos de 4.000 exámenes, es decir, 4 %.", " %"),
        ("abc", "{F} Entre el año 1 y el año 2 los exámenes se duplicaron. ¿Qué efecto puede tener esto en los casos detectados?", "Aumentarlos, aunque la cantidad real de infectados no haya subido", "Disminuirlos siempre", "No tiene ningún efecto posible", "Con más exámenes se encuentran más casos que antes pasaban inadvertidos."),
        ("=", "{F} ¿Cuál es la tasa de casos detectados por cada 10.000 jóvenes en el año 2?", "160*10000/40000", "Se divide 160 entre 40.000 y se multiplica por 10.000.", " casos por cada 10.000"),
        ("abc", "{F} ¿Qué conclusión es más prudente con esta tabla?", "Los casos detectados aumentaron, pero la positividad bajó, así que no se puede afirmar que haya más infecciones", "Hay el doble de infectados", "Las ITS desaparecieron", "La positividad bajó de 5 % a 4 %, y eso indica que el aumento se asocia a más exámenes."),
        ("abc", "{F} Si el año 3 tuviera 6.000 exámenes y 300 casos detectados, ¿cuál sería la positividad?", "5 %", "50 %", "0,5 %", "Son 300 entre 6.000, que es 5 de cada 100."),
        ("abc", "{F} Una autoridad dice: «los casos subieron 60 %, por eso hay una epidemia». ¿Qué le falta analizar?", "Cuántos exámenes se hicieron y la positividad", "El color de la tabla", "Cuántas ciudades hay en el país", "Para interpretar el aumento hay que mirar también la cantidad de exámenes que lo produjo."),
        ("abc", "{F} Se propone vacunar contra los agentes que tienen vacuna, difundir información y facilitar los exámenes. ¿Qué enfoque representa?", "Un enfoque de prevención con varias medidas a la vez", "Una sola medida que lo resuelve todo", "Una medida que juzga a las personas", "Combinar vacunas, información y exámenes actúa sobre varias partes del sistema."),
        ("abc", "{F} Sobre el uso de estos datos, ¿qué práctica es adecuada?", "Presentar tasas de la población sin identificar a ninguna persona", "Publicar nombres de las personas con resultado positivo", "Culpar a un grupo de jóvenes por los casos", "Los datos de salud pública se presentan agregados y se protege la privacidad de las personas."),
        ("abc", "{F} Una persona joven de esta ciudad ficticia se pregunta si tiene una ITS. ¿Cuál es la respuesta adecuada del análisis?", "Que lo consulte con un profesional de salud o una persona adulta de confianza", "Que lo deduzca mirando la tabla", "Que lo ignore porque no tiene síntomas", "La tabla describe una población y no sirve para saber si una persona tiene una infección."),
    ],
    ctx=("abc", "Contexto: en el diario mural del liceo quieres presentar datos de ITS de forma responsable. ¿Qué incluyes?", "Tasas de la población, el cuidado con la positividad y un mensaje para consultar a un profesional de salud", "Los nombres de estudiantes que se hicieron exámenes", "Solo la cifra más alta para llamar la atención", "Un mensaje responsable usa datos agregados, explica sus límites y orienta a consultar."),
    sc=[
        ("En Ciencias de la salud: ¿qué es una tasa?", "Casos en relación con el tamaño de la población, por ejemplo por cada 10.000 personas", "Una tasa permite comparar poblaciones o años de tamaños distintos."),
        ("ab", "Si aumentan los exámenes, los casos detectados:", "Pueden aumentar aunque no suban las infecciones reales", "Siempre bajan", "Examinar a más personas encuentra más casos que antes no se veían."),
        ("ab", "Los datos de ITS en salud pública se usan para:", "Decidir medidas colectivas de prevención", "Señalar a personas", "La evidencia colectiva orienta políticas y no debe estigmatizar a nadie."),
    ],
    op=("Con la tabla de la ficha {F} haz lo siguiente: (1) calcula la tasa por 10.000 jóvenes y la positividad de cada año; (2) escribe una conclusión de dos oraciones que no exagere; (3) propone dos medidas de prevención y una limitación de estos datos.",
        "(1) Año 1: 25 casos por 10.000 y 5 % de positividad. Año 2: 40 casos por 10.000 y 4 %. (2) Los casos detectados aumentaron, pero la positividad bajó, así que parte del aumento se debe a más exámenes. No se puede afirmar que haya más infecciones. (3) Información y vacunas para los agentes que las tienen. Limitación: la tabla no dice quiénes se hacen exámenes ni por qué.",
        ["calcula tasas y positividades correctas", "conclusión prudente sin exagerar", "dos medidas de prevención coherentes con la ficha", "nombra una limitación de los datos"],
        ["cálculos, conclusión y medidas numerados"],
        ["afirmar que hay una epidemia solo por los casos detectados", "olvidar la positividad", "no proteger la privacidad"],
        "Pregunta: «¿qué otro dato pedirías para saber si las infecciones realmente aumentaron?»."),
    reinforce="Con una tabla propia de ejemplo (años, exámenes y casos), calcula la positividad de cada año y escribe qué cambió.",
    extend="Explica por qué mirar solo los casos detectados puede llevar a una conclusión equivocada y cómo la positividad ayuda a corregirlo.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (caso de ejemplo de enfermedad laboral). En un taller ficticio de carpintería, el ruido de una máquina es alto durante la jornada y varias personas trabajadoras han tenido pérdida de audición progresiva. "
     "Jerarquía de controles, de la más a la menos efectiva: 1) eliminar o sustituir la fuente de riesgo; 2) controles de ingeniería, como encerrar o aislar la máquina; 3) controles administrativos, como turnos y descansos; 4) protección personal, como orejeras. "
     "Opciones de ejemplo y su puntaje de 1 a 3 en cada criterio (3 es mejor): Opción A, reemplazar la máquina por una más silenciosa: efectividad 3, no depende de que cada persona la use bien 3, costo accesible 1. "
     "Opción B, encerrar la máquina en una cabina aislante: efectividad 3, no depende 3, costo accesible 2. "
     "Opción C, rotar los turnos para reducir las horas de exposición: efectividad 2, no depende 2, costo accesible 3. "
     "Opción D, entregar solo orejeras: efectividad 1, no depende 1, costo accesible 3.")
build(
    O1, 5, F,
    use="Aprenderé a comparar soluciones frente a un problema de salud laboral con criterios claros, usando la jerarquía de controles. Sirve para elegir una medida con razones y no solo por costo o costumbre.",
    prior=["Sé que el ruido fuerte puede dañar el oído.", "Sé sumar puntajes de una tabla.", "Sé comparar opciones con criterios."],
    explain=[
        "Las enfermedades profesionales o laborales son problemas de salud causados por las condiciones del trabajo, como el ruido, el polvo, las posturas repetidas o el estrés. Aparecen de manera lenta, por eso se pasan por alto. Son un problema de salud pública porque afectan a muchas personas y se pueden prevenir cambiando el ambiente de trabajo, y no solo pidiendo a cada persona que se cuide.",
        "La jerarquía de controles ordena las medidas de más a menos efectivas. Lo mejor es eliminar o sustituir la fuente del riesgo. Luego vienen los controles de ingeniería, que aíslan el riesgo, después los controles administrativos, como turnos y descansos, y por último la protección personal. La protección personal es la menos confiable, porque depende de que cada persona la use bien y todo el tiempo.",
        "Para comparar soluciones se eligen criterios, como efectividad, dependencia de la conducta de cada persona y costo, y se asigna un puntaje a cada opción. Sumar los puntajes ayuda a decidir, pero no reemplaza el juicio: hay que preguntar quién gana o pierde con cada opción y qué efectos no previstos podría haber. Una solución barata que no reduce el riesgo no es una buena solución.",
    ],
    vocab=[("enfermedad profesional", "problema de salud causado por las condiciones del trabajo"), ("jerarquía de controles", "orden de las medidas de prevención de la más a la menos efectiva"), ("control de ingeniería", "cambio físico que aísla o reduce el riesgo en su origen"), ("control administrativo", "cambio en turnos, descansos o reglas de trabajo"), ("criterio", "aspecto con el que se evalúa una opción")],
    worked=[
        ("Ordenar por la jerarquía", "En otro taller de ejemplo hay polvo que irrita las vías respiratorias. ¿Es mejor cambiar el material por uno que no suelte polvo o entregar mascarillas?",
         ["Cambiar el material elimina o sustituye la fuente de riesgo: es el primer nivel.", "Las mascarillas son protección personal: es el último nivel y depende de usarlas bien siempre."],
         "Cambiar el material"),
        ("Sumar puntajes", "En una comparación de ejemplo, la opción X tiene puntajes 3, 2 y 2, y la opción Y tiene 2, 2 y 3. ¿Cuál suma más?",
         ["Opción X: 3 más 2 más 2 es 7.", "Opción Y: 2 más 2 más 3 es 7.", "Hay empate, y el puntaje solo no decide: hay que revisar cuál criterio pesa más."],
         "Empate en 7 puntos"),
    ],
    mistakes=[("Elegir solo la solución más barata sin mirar cuánto reduce el riesgo.", "Una medida barata que no reduce el riesgo deja el problema igual.", "Compara varios criterios, no solo el costo."),
              ("Creer que entregar protección personal basta.", "Depende de que cada persona la use bien siempre y no elimina el riesgo en su origen.", "Revisa primero medidas que actúan sobre la fuente.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es una enfermedad profesional?", "Un problema de salud causado por las condiciones del trabajo", "Una enfermedad que solo tienen los profesionales universitarios", "Una infección que se contagia en cualquier lugar", "El nombre se refiere a la relación con las condiciones del trabajo, no con el título de la persona."),
        ("{F} Según la jerarquía de la ficha, ¿qué tipo de control es el más efectivo?", "Eliminar o sustituir la fuente de riesgo", "La jerarquía parte por quitar el riesgo en su origen."),
        ("ab", "{F} Entregar orejeras es un control de:", "Protección personal", "Ingeniería", "Las orejeras protegen a cada persona y no cambian el ruido de la máquina."),
        ("=", "{F} ¿Cuántos puntos suma la opción A (efectividad, no depende y costo)?", "3+3+1", "Se suman 3, 3 y 1.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción B?", "3+3+2", "Se suman 3, 3 y 2.", " puntos"),
        ("abc", "{F} ¿Por qué la opción D tiene puntaje 1 en no depende de que cada persona la use bien?", "Porque funciona solo si cada persona usa las orejeras bien y siempre", "Porque las orejeras son muy caras", "Porque eliminan el ruido de la máquina", "La protección personal depende de la conducta de cada trabajador."),
        ("=", "{F} ¿Cuántos puntos más suma la opción B que la opción D?", "(3+3+2)-(1+1+3)", "La opción B suma 8 y la D suma 5.", " puntos"),
        ("abc", "{F} Con la suma de puntajes, ¿qué opción queda primera?", "Opción B", "Opción A", "Opción D", "B suma 8, A suma 7, C suma 7 y D suma 5, así que B tiene el mayor puntaje."),
        ("abc", "{F} Si el criterio de costo accesible fuera lo único que importa, ¿qué opciones empatarían en primer lugar?", "C y D", "A y B", "Solo A", "C y D tienen puntaje 3 en costo accesible, el más alto."),
        ("abc", "{F} Alguien propone solo la opción D por ser barata y rápida. ¿Qué le respondes?", "Que es la menos efectiva y la que más depende de las personas, así que no elimina el riesgo", "Que es la mejor porque cuesta poco", "Que es la más efectiva de la jerarquía", "D queda en el último nivel de la jerarquía y depende de la conducta."),
        ("abc", "{F} Después de encerrar la máquina (opción B), ¿qué podría seguir siendo útil como medida complementaria?", "Revisar el ruido con mediciones periódicas y usar orejeras en tareas puntuales", "Quitar toda revisión porque ya no hay riesgo", "Aumentar la jornada", "Ninguna medida elimina todo el riesgo y por eso se mide y se complementa."),
        ("abc", "{F} Un efecto no previsto de la opción C, rotar turnos, podría ser que:", "Más personas queden expuestas, aunque menos horas cada una", "El ruido desaparezca por completo", "Se elimine la máquina", "Rotar reparte la exposición entre más personas y no baja el ruido de la máquina."),
        ("abc", "{F} Si solo hubiera dinero para una opción y se necesita que no dependa de la conducta de las personas, ¿cuál conviene?", "Opción B, que suma el mayor puntaje y no depende de las personas", "Opción D, porque es barata", "Opción C, porque tiene el costo más accesible", "B combina efectividad alta, independencia de la conducta y costo medio."),
    ],
    ctx=("abc", "Contexto: tu tío trabaja en un taller con mucho polvo y quiere proteger su salud. ¿Qué le sugieres, con base en la jerarquía?", "Que converse con quien dirige el taller sobre cambiar o aislar la fuente del polvo, y que consulte a un profesional de salud", "Que se resigne porque es parte del trabajo", "Que use solo una mascarilla y no diga nada", "La prevención más efectiva actúa en el origen del riesgo y se conversa con las personas responsables y con profesionales."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un control de ingeniería?", "Un cambio físico que aísla o reduce el riesgo en su origen", "Aísla el riesgo y no depende de que cada persona se cuide."),
        ("ab", "La protección personal es:", "La medida menos confiable de la jerarquía", "La medida más efectiva", "Depende de que cada persona la use bien siempre."),
        ("ab", "Para comparar soluciones conviene:", "Usar varios criterios, como efectividad y costo", "Mirar solo el costo", "Un solo criterio puede ocultar la baja efectividad de una opción."),
    ],
    op=("Con el caso de la ficha {F} haz lo siguiente: (1) suma los puntos de las cuatro opciones; (2) elige una opción y explica con dos criterios por qué la prefieres; (3) nombra un efecto no previsto de tu opción y cómo lo vigilarías.",
        "(1) A: 7. B: 8. C: 7. D: 5. (2) Elijo B porque suma 8 y porque es efectiva y no depende de que cada persona la use bien. (3) Si la cabina se deja abierta, el ruido vuelve a salir. Lo vigilaría midiendo el ruido de forma periódica.",
        ["suma correcta de las cuatro opciones", "elige una opción con dos criterios", "usa la jerarquía de controles", "nombra un efecto no previsto y cómo vigilarlo"],
        ["tres partes numeradas"],
        ["decidir solo por costo", "sumar mal los puntajes", "no considerar la dependencia de la conducta"],
        "Pregunta: «¿cambiaría tu elección si el costo tuviera el doble de peso que los otros criterios?»."),
    reinforce="Elige un riesgo laboral de ejemplo, como polvo o posturas repetidas, y escribe una medida para cada nivel de la jerarquía de controles.",
    extend="Explica por qué la protección personal debería ser la última opción y no la primera en una empresa que quiere prevenir enfermedades profesionales.",
)

# ============================================================ OAC-01, clase 6
F = ("Ficha 6 (comparación de ejemplo sobre prevención del consumo de alcohol en adolescentes). "
     "Liceo P, ficticio, aplicó durante un año talleres de habilidades sociales y reuniones informativas con las familias. Liceo Q, ficticio, no aplicó ningún programa. "
     "Al final del año, en una encuesta anónima de 600 estudiantes en cada liceo, declararon haber consumido alcohol en el último mes: 90 estudiantes en P y 120 en Q. "
     "Limitaciones: los datos son declarados; los liceos no fueron asignados al azar y pueden diferir en otros aspectos; se observó solo un año.")
build(
    O1, 6, F,
    use="Aprenderé a comunicar una decisión de salud pública diciendo qué muestra la evidencia, qué no permite concluir y qué falta saber. Sirve para escribir recomendaciones honestas sobre temas sensibles, como el consumo de drogas.",
    prior=["Sé calcular porcentajes y diferencias.", "Distingo asociación de causa.", "Sé comparar dos grupos con una tabla."],
    explain=[
        "El consumo de alcohol, tabaco y otras drogas es un problema de salud pública complejo, porque se relaciona con la biología, con la edad, con la familia, con los amigos, con la publicidad y con lo fácil que sea conseguir la sustancia. Por eso los programas de prevención suelen actuar en varios frentes a la vez, como el desarrollo de habilidades sociales, la información para las familias y las normas del entorno.",
        "Para evaluar un programa se compara un grupo que lo recibió con otro que no. Si en P declaró consumo el 15 % y en Q el 20 %, la diferencia es de 5 puntos porcentuales. Parece favorable al programa, pero no prueba que el programa la causó: los liceos pueden diferir en otras cosas, los datos son declarados y se observó solo un año. Se dice que los datos son compatibles con un posible beneficio, no que lo demuestran.",
        "Comunicar una decisión es decir qué se recomienda, con qué evidencia y con qué límites. Se evita el lenguaje alarmista, el juicio a las personas y las certezas exageradas. Si tú o alguien cercano está en riesgo por consumo, lo más seguro es contárselo a una persona adulta de confianza o a un profesional de salud, y el Fono Niños 147 puede orientar. Los textos de este cuaderno no reemplazan ayuda profesional.",
    ],
    vocab=[("programa de prevención", "conjunto de acciones para evitar que aparezca un problema de salud"), ("grupo de comparación", "grupo que no recibe la acción y sirve para comparar"), ("punto porcentual", "diferencia entre dos porcentajes"), ("límite", "aspecto que impide concluir con más fuerza"), ("recomendación", "propuesta de acción apoyada en evidencia y con sus límites declarados")],
    worked=[
        ("Calcular y comparar", "En un par de liceos de ejemplo, el 12 % declara consumo en el que tiene programa y el 18 % en el que no. ¿Cuál es la diferencia y qué se puede decir?",
         ["La diferencia es 18 menos 12, es decir, 6 puntos porcentuales.", "Es compatible con un posible beneficio del programa.", "No prueba que el programa lo causó, porque falta saber si los liceos eran parecidos."],
         "6 puntos porcentuales, compatible con un beneficio posible, sin prueba de causa"),
        ("Redactar con cuidado", "¿Qué frase comunica mejor un resultado: «el programa funciona» o «los datos son compatibles con un efecto favorable, con límites»?",
         ["La primera afirma una certeza que los datos no dan.", "La segunda dice lo que muestran los datos y nombra los límites."],
         "La segunda frase"),
    ],
    mistakes=[("Afirmar que un programa «funciona» solo con una diferencia entre dos liceos.", "Los liceos pueden diferir en otras cosas y los datos son declarados.", "Habla de un resultado compatible y nombra los límites."),
              ("Comunicar con lenguaje alarmista o culpando a los jóvenes.", "Asustar o juzgar no ayuda a prevenir y puede alejar a quien necesita ayuda.", "Usa datos, lenguaje respetuoso y orienta a consultar con adultos y profesionales.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es un grupo de comparación?", "Un grupo que no recibe la acción y sirve para comparar el resultado", "El grupo que más se beneficia", "El grupo que decide el programa", "Sin un grupo de comparación no se sabe qué habría pasado sin el programa."),
        ("=", "{F} ¿Qué porcentaje de los 600 estudiantes del liceo P declaró consumo en el último mes?", "90/600*100", "Son 90 de 600, es decir, 15 %.", " %"),
        ("=", "{F} ¿Qué porcentaje de los 600 estudiantes del liceo Q declaró consumo en el último mes?", "120/600*100", "Son 120 de 600, es decir, 20 %.", " %"),
        ("ab", "{F} La diferencia entre P y Q es de:", "5 puntos porcentuales", "15 puntos porcentuales", "Se resta 20 % menos 15 %, y esa diferencia es de 5 puntos.", ),
        ("abc", "{F} ¿Cuál es una limitación de estos datos?", "Los datos son declarados y los liceos no fueron asignados al azar", "Que hay dos liceos", "Que la encuesta fue anónima", "Lo declarado puede diferir de lo real, y sin azar los liceos pueden diferir en otras cosas."),
        ("abc", "{F} ¿Qué frase refleja mejor lo que muestran los datos?", "Los datos son compatibles con un posible efecto favorable del programa, con límites", "El programa demuestra que el consumo se acaba", "El programa no sirve para nada", "La diferencia favorece a P pero no basta para probar causa."),
        ("=", "{F} ¿Cuántos estudiantes menos declararon consumo en P que en Q?", "120-90", "La diferencia entre 120 y 90 estudiantes es de 30.", " estudiantes"),
        ("abc", "{F} ¿Qué dato adicional ayudaría más a saber si el programa causó la diferencia?", "Cómo era el consumo en ambos liceos antes del programa", "El color del uniforme", "El número de salas de cada liceo", "Comparar la situación inicial muestra si la diferencia ya existía antes."),
        ("abc", "{F} ¿Por qué es importante que la encuesta sea anónima?", "Porque ayuda a que las personas respondan con más sinceridad y protege su privacidad", "Porque permite identificar a quienes consumen", "Porque hace que las respuestas sean siempre verdaderas", "El anonimato protege a las personas y favorece respuestas más honestas, aunque no garantiza que todas sean exactas."),
        ("abc", "Un afiche dice: «¡Los jóvenes están perdidos con las drogas!». ¿Qué problema comunicativo tiene?", "Es alarmista y generaliza sin evidencia", "Es demasiado preciso", "Usa demasiados datos", "Un lenguaje alarmista que generaliza no informa y puede estigmatizar."),
        ("abc", "{F} Una directora quiere extender el programa de P a todos los liceos. ¿Qué decisión es más prudente?", "Aplicarlo en algunos liceos más y evaluarlo con mejor diseño antes de generalizar", "Aplicarlo en todos sin evaluar", "Descartarlo porque la evidencia es incompleta", "Con evidencia limitada conviene ampliar con evaluación, sin certeza exagerada ni descarte."),
        ("abc", "{F} ¿Qué incluye una buena recomendación final?", "Qué se recomienda, qué evidencia la apoya y qué límites tiene", "Solo qué se recomienda", "Solo los datos sin conclusión", "Una recomendación honesta une la decisión, la evidencia y sus límites."),
        ("abc", "Un estudiante de ejemplo cuenta que un compañero consume alcohol con frecuencia y está muy mal. ¿Qué acción es la más adecuada?", "Contarlo a una persona adulta de confianza o a un profesional de salud", "Guardar el secreto para no traicionarlo", "Confrontarlo delante de todo el curso", "Pedir ayuda a una persona adulta o a un profesional protege al compañero y no deja la situación en secreto."),
    ],
    ctx=("abc", "Contexto: te piden un párrafo para el boletín del liceo con los resultados de la ficha. ¿Cuál escribes?", "En el liceo con programa declaró consumo el 15 % y en el sin programa el 20 %. Es compatible con un beneficio, pero faltan datos para probarlo.", "El programa funciona y hay que copiarlo en todos los liceos.", "El 15 % de los jóvenes está en peligro y es culpa de sus familias.", "El párrafo correcto informa los datos, sugiere un posible beneficio y nombra el límite."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un punto porcentual?", "La diferencia entre dos porcentajes", "Se usa para decir cuánto se separa un porcentaje de otro."),
        ("ab", "Una recomendación honesta:", "Declara los límites de la evidencia", "Oculta lo que no se sabe", "Informar los límites evita transmitir una certeza que los datos no dan."),
        ("ab", "Si alguien cercano está en riesgo por consumo, lo más seguro es:", "Avisar a una persona adulta de confianza o a un profesional", "Guardar el secreto", "Una persona adulta o un profesional pueden ayudar de forma segura."),
    ],
    op=("Con los datos de la ficha {F} haz lo siguiente: (1) escribe un párrafo de cuatro oraciones para el diario mural que informe los porcentajes y la diferencia; (2) nombra dos límites de los datos; (3) escribe una recomendación para el liceo que incluya lo que aconsejas y qué evaluarías después.",
        "(1) En el liceo P, con talleres, declaró consumo el 15 % y en el Q, sin programa, el 20 %. La diferencia es de 5 puntos porcentuales. Es compatible con un posible beneficio del programa. No prueba que haya sido la causa. (2) Datos declarados y liceos no asignados al azar. (3) Recomiendo seguir con los talleres y medir el consumo antes y después, también en el liceo Q.",
        ["porcentajes y diferencia correctos", "lenguaje que no exagera ni culpa", "dos límites nombrados", "recomendación con evaluación posterior"],
        ["párrafo, límites y recomendación"],
        ["afirmar que el programa funciona sin reservas", "usar lenguaje alarmista", "no nombrar ningún límite"],
        "Pregunta: «¿qué dato pedirías para saber si el programa fue la causa de la diferencia?»."),
    reinforce="Escribe dos frases sobre un mismo resultado: una exagerada y otra prudente. Subraya qué palabras cambian la certeza.",
    extend="Explica por qué en salud pública es importante comunicar los límites de la evidencia aunque la decisión deba tomarse de todos modos.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 7 (tres condiciones de ejemplo para analizar genoma y ambiente). "
     "Condición X, inspirada en la fenilcetonuria: una persona que hereda dos copias alteradas de un gen no puede procesar bien una sustancia de los alimentos. Si se detecta al nacer y un equipo de salud ajusta la alimentación, se evitan las consecuencias. "
     "Condición Y, inspirada en la intolerancia a la lactosa: hay diferencias genéticas en cuánto tiempo sigue activa la enzima que digiere el azúcar de la leche; los síntomas dependen además de cuánta leche se consume. "
     "Condición Z, inspirada en la diabetes tipo 2: muchos genes con efectos pequeños influyen en el riesgo, junto con la alimentación, la actividad física, el peso y la edad.")
build(
    O2, 1, F,
    use="Aprenderé a distinguir qué parte de una condición de salud se explica por el genoma, cuál por el ambiente y cuál por la interacción entre ambos. Sirve para evitar explicaciones del tipo «es genético» o «es culpa del estilo de vida».",
    prior=["Sé que los genes están en el ADN.", "Sé que cada persona hereda una copia de cada gen de cada progenitor.", "Distingo alelo dominante y recesivo."],
    explain=[
        "El genoma es el conjunto de todo el ADN de una persona. Los genes son segmentos del genoma que contienen instrucciones para fabricar proteínas. El genotipo es la combinación de alelos que una persona tiene en un gen. El fenotipo es lo que se observa o mide: un rasgo, una condición, una concentración de una sustancia en la sangre. El fenotipo depende del genotipo, pero también del ambiente.",
        "El ambiente incluye la alimentación, la actividad física, el sueño, las exposiciones a sustancias, las infecciones y las condiciones sociales. Hay condiciones determinadas sobre todo por un solo gen, como la condición X de la ficha, y otras multifactoriales, como la condición Z, en que muchos genes y muchos factores del ambiente contribuyen. En ambos casos, el ambiente puede cambiar el fenotipo aunque el genotipo no cambie.",
        "Por eso decir «es genético» o «es del ambiente» suele ser una simplificación. Para analizar una condición se delimita qué genotipos y qué ambientes se comparan y se pregunta qué fenotipo se observa en cada combinación. Un examen que se ofrece a toda una población para detectar a tiempo una condición se llama tamizaje. Estos análisis describen poblaciones y no diagnostican a nadie: cualquier duda personal se consulta con un profesional de salud.",
    ],
    vocab=[("genoma", "conjunto de todo el ADN de una persona"), ("genotipo", "combinación de alelos que una persona tiene en un gen"), ("fenotipo", "rasgo o condición que se observa o se mide"), ("condición multifactorial", "condición en que influyen muchos genes y factores del ambiente"), ("tamizaje", "examen que se ofrece a toda una población para detectar a tiempo una condición")],
    worked=[
        ("Genotipo y fenotipo", "Una persona de ejemplo tiene dos alelos distintos en un gen: uno normal y uno alterado. Su condición de salud no se manifiesta. ¿Qué es el genotipo y qué es el fenotipo?",
         ["El genotipo es la combinación de alelos: uno normal y uno alterado.", "El fenotipo es lo que se observa: no hay manifestación de la condición."],
         "Genotipo: un alelo normal y uno alterado. Fenotipo: sin manifestación."),
        ("Clasificar la condición", "Una condición de ejemplo depende de muchos genes con efecto pequeño, de la alimentación y de la actividad física. ¿Se explica solo por la herencia?",
         ["Participan muchos genes y también factores del ambiente.", "Por eso es una condición multifactorial y no solo hereditaria."],
         "No: es multifactorial"),
    ],
    mistakes=[("Decir «es genético, no se puede hacer nada».", "El ambiente puede cambiar el fenotipo aunque el genotipo no cambie, como en la condición X.", "Pregunta qué parte depende del ambiente y qué se puede modificar."),
              ("Decir «es culpa del estilo de vida» en una condición con base genética.", "Muchos genes influyen en el riesgo y no dependen de la voluntad de la persona.", "Habla de factores que interactúan y evita culpar.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es el fenotipo?", "El rasgo o condición que se observa o se mide", "El conjunto de todo el ADN de una persona", "La combinación de alelos de un gen", "El fenotipo es lo observable, que resulta del genotipo y del ambiente."),
        ("{F} ¿Cuál de las tres condiciones es multifactorial, con muchos genes y varios factores del ambiente?", "La condición Z", "La ficha dice que en la condición Z influyen muchos genes con efecto pequeño y varios factores del ambiente."),
        ("ab", "En Ciencias de la salud: el genotipo es:", "La combinación de alelos que una persona tiene en un gen", "El rasgo que se observa", "El genotipo se refiere a los alelos y no a lo observable."),
        ("abc", "{F} En la condición X, ¿qué factor del ambiente puede cambiar el resultado?", "La alimentación, ajustada por un equipo de salud", "El color de los ojos", "La estatura de los padres", "En la ficha, la alimentación ajustada evita las consecuencias aunque el genotipo sea el mismo."),
        ("abc", "{F} En la condición Y, ¿qué cambia los síntomas además de la diferencia genética?", "Cuánta leche se consume", "El número de hermanos", "El día de nacimiento", "La ficha indica que los síntomas dependen también de la cantidad de leche."),
        ("abc", "{F} Un examen que se ofrece a todos los recién nacidos para detectar a tiempo la condición X es un ejemplo de:", "Tamizaje", "Diagnóstico personal en la casa", "Experimento con alimentos", "Un examen ofrecido a toda una población para detectar a tiempo es un tamizaje."),
        ("abc", "{F} Alguien afirma: «la condición Z es solo hereditaria, no depende del estilo de vida». ¿Qué le respondes?", "Que influyen muchos genes y también la alimentación, la actividad física, el peso y la edad", "Que tiene razón porque tiene genes", "Que es solo del ambiente", "La ficha indica que la condición Z es multifactorial."),
        ("abc", "{F} Dos personas con el mismo genotipo en la condición X siguen alimentaciones distintas. ¿Qué es lo más probable?", "Que sus fenotipos sean distintos", "Que sus fenotipos sean idénticos siempre", "Que cambie su genotipo por la dieta", "La alimentación puede cambiar el fenotipo sin cambiar el genotipo."),
        ("abc", "¿Cuál es una pregunta bien delimitada sobre genoma y ambiente?", "¿Cambia el fenotipo de un grupo con el mismo genotipo cuando cambia la alimentación?", "¿Qué es la vida?", "¿Por qué hay enfermedades?", "La primera fija un genotipo, un factor del ambiente y un fenotipo que se compara."),
        ("abc", "Un joven de ejemplo con un familiar con una condición multifactorial pregunta si «es seguro que la tendrá». ¿Qué respuesta es más correcta?", "Que tener familiares puede aumentar el riesgo, pero no determina el resultado y conviene consultar a un profesional de salud", "Que sí, es seguro", "Que no, nunca puede ocurrir", "En una condición multifactorial, los genes cambian el riesgo pero no lo fijan, y una persona concreta debe consultar a un profesional."),
        ("abc", "¿Por qué un examen genético no debe usarse para discriminar a las personas?", "Porque es información de salud sensible que solo indica riesgos, no destinos", "Porque es información pública que cualquiera puede pedir", "Porque solo las personas sanas tienen genoma", "La información genética es sensible y no determina la vida de una persona."),
        ("abc", "{F} En la condición X, la sustancia que no se procesa viene de la alimentación. ¿Qué componente del sistema es la alimentación?", "Un factor del ambiente que interactúa con el genotipo", "El genotipo", "El fenotipo", "La alimentación es parte del ambiente, y la interacción se ve cuando cambia el fenotipo."),
        ("abc", "{F} En la condición Y, una persona de ejemplo tiene síntomas con poca leche y otra no los tiene con la misma cantidad. ¿Qué explica la diferencia?", "Diferencias genéticas en la enzima que digiere el azúcar de la leche", "Que una persona nació en otro día de la semana", "Que no existen diferencias entre personas", "La ficha dice que la actividad de la enzima varía por diferencias genéticas."),
    ],
    ctx=("abc", "Contexto: en una charla del liceo alguien dice que «las enfermedades vienen todas en los genes». ¿Cómo respondes con evidencia?", "Que hay condiciones con base genética, pero el ambiente también influye y a veces cambia el resultado, como en la condición X", "Que los genes no tienen nada que ver con la salud", "Que solo el ambiente importa", "La respuesta reconoce ambos factores y su interacción con un ejemplo."),
    sc=[
        ("En Ciencias de la salud: ¿qué es el genoma?", "El conjunto de todo el ADN de una persona", "El genoma incluye todos los genes y el ADN que está entre ellos."),
        ("ab", "El ambiente puede cambiar el fenotipo:", "Aunque el genotipo no cambie", "Solo si cambia el genotipo", "La alimentación, por ejemplo, puede cambiar un fenotipo sin modificar los genes."),
        ("ab", "Una condición multifactorial depende de:", "Muchos genes y factores del ambiente", "Un solo gen", "Multifactorial quiere decir que hay varios factores que contribuyen."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) completa una tabla con las tres condiciones, el factor genético y el factor del ambiente de cada una; (2) escribe una pregunta bien delimitada sobre genotipo, ambiente y fenotipo; (3) explica por qué «es genético» no basta para describir ninguna de las tres.",
        "(1) X: dos copias alteradas de un gen, alimentación. Y: diferencias en la enzima, cantidad de leche. Z: muchos genes con efecto pequeño, alimentación, actividad física, peso y edad. (2) «¿Cambia el fenotipo de un grupo con el mismo genotipo cuando cambia la alimentación?» (3) En las tres hay factores del ambiente que cambian el resultado.",
        ["tabla con factor genético y de ambiente de las tres condiciones", "pregunta con genotipo, ambiente y fenotipo", "explica con un dato de la ficha", "evita culpar o dar certezas"],
        ["tabla, pregunta y explicación"],
        ["afirmar que todo es genético", "decir que todo es del ambiente", "confundir genotipo con fenotipo"],
        "Pregunta: «¿en cuál de las tres condiciones el ambiente tiene más posibilidades de cambiar el resultado, y por qué?»."),
    reinforce="Escribe una frase con las palabras genotipo, fenotipo y ambiente que explique por qué dos personas con el mismo genotipo pueden ser distintas.",
    extend="Explica qué ventaja tiene detectar a tiempo una condición con un tamizaje y qué cuidados éticos se necesitan con esa información.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 8 (estudio de ejemplo con gemelos sobre una condición W). "
     "Gemelos idénticos, que comparten casi todo su genoma: 100 parejas en las que al menos una persona tiene la condición; en 60 de ellas la tienen ambas. "
     "Mellizos, que comparten en promedio la mitad de las variantes que difieren entre personas: 100 parejas en las que al menos una persona tiene la condición; en 30 de ellas la tienen ambas. "
     "Nota: las parejas de gemelos suelen crecer en la misma casa, así que también comparten gran parte de su ambiente.")
build(
    O2, 2, F,
    use="Aprenderé a evaluar fuentes y variables en estudios de familia y de gemelos, para estimar cuánto aportan los genes y cuánto el ambiente a una condición. Sirve para leer con criterio las noticias sobre «genes de» una enfermedad.",
    prior=["Sé qué es un porcentaje.", "Sé que los gemelos idénticos comparten casi todo su genoma.", "Distingo genotipo de ambiente."],
    explain=[
        "Para saber cuánto influyen los genes y el ambiente en una condición, un diseño clásico compara gemelos idénticos con mellizos. Los idénticos comparten casi todo su genoma, y los mellizos comparten la mitad de las variantes que difieren entre personas, como cualquier hermano. Si ambos tipos de gemelos comparten un ambiente parecido y los idénticos se parecen más en la condición, es una señal de que los genes aportan.",
        "La concordancia es el porcentaje de parejas en que ambas personas tienen la condición, entre las parejas donde al menos una la tiene. Si la concordancia en idénticos es 60 % y en mellizos 30 %, los genes importan. Pero 60 % no es 100 %: aun con el mismo genoma, en 4 de cada 10 parejas solo una persona tiene la condición. Esa diferencia se atribuye al ambiente y al azar.",
        "Todo diseño tiene límites. Los gemelos comparten ambiente familiar, y si los idénticos fueran tratados de manera más parecida, parte de su parecido sería ambiental. Además, un estudio de gemelos describe una población y una condición determinada, y no puede aplicarse a una persona concreta. Por eso las noticias sobre «el gen de» algo deben leerse preguntando cómo se midió, a cuántas parejas y con qué ambiente.",
    ],
    vocab=[("gemelos idénticos", "hermanos nacidos juntos que comparten casi todo su genoma"), ("mellizos", "hermanos nacidos juntos que comparten en promedio la mitad de las variantes que difieren entre personas"), ("concordancia", "porcentaje de parejas en que ambas personas tienen la condición, entre las parejas con al menos un caso"), ("ambiente compartido", "condiciones que viven en común las personas de una familia"), ("estudio de gemelos", "estudio que compara la semejanza de gemelos idénticos y mellizos")],
    worked=[
        ("Calcular la concordancia", "En otro estudio de ejemplo hay 50 parejas de gemelos idénticos con al menos un caso, y en 20 ambas personas tienen la condición. ¿Cuál es la concordancia?",
         ["Concordancia es parejas con ambos casos entre parejas con al menos un caso.", "20 entre 50 es 4 de cada 10.", "Como porcentaje es 40 %."],
         "40 %"),
        ("Interpretar una diferencia", "En una condición de ejemplo la concordancia es 80 % en idénticos y 40 % en mellizos. ¿Qué indica?",
         ["Los idénticos se parecen el doble que los mellizos en la condición.", "Esto sugiere que los genes aportan.", "Pero 80 % no es 100 %, así que el ambiente también interviene."],
         "Los genes aportan, pero no explican todo"),
    ],
    mistakes=[("Concluir que si la concordancia en idénticos es 60 %, el gen causa la condición el 60 % de las veces en una persona.", "La concordancia describe parejas de una población, no el riesgo de una persona concreta.", "Interpreta la concordancia como una señal sobre la población."),
              ("Olvidar que los gemelos comparten ambiente.", "Parte del parecido de los idénticos podría deberse al ambiente compartido.", "Nombra el ambiente compartido como un límite del diseño.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la concordancia en un estudio de gemelos?", "El porcentaje de parejas en que ambas personas tienen la condición, entre las parejas con al menos un caso", "El número total de gemelos del mundo", "El porcentaje de parejas sanas", "La concordancia compara los casos en ambas personas de la pareja."),
        ("=", "{F} ¿Cuál es la concordancia en gemelos idénticos?", "60/100*100", "Son 60 parejas de 100 con ambos casos, es decir, 60 %.", " %"),
        ("=", "{F} ¿Cuál es la concordancia en mellizos?", "30/100*100", "Son 30 parejas de 100 con ambos casos, es decir, 30 %.", " %"),
        ("ab", "{F} Los idénticos tienen una concordancia mayor que los mellizos. Esto sugiere que:", "Los genes aportan a la condición", "El ambiente no influye en nada", "Mayor parecido con mayor semejanza genética apunta a una contribución de los genes.", ),
        ("=", "{F} En las parejas de gemelos idénticos, ¿cuántas tienen la condición en solo una de las dos personas?", "100-60", "De 100 parejas, 60 tienen ambas y las otras 40 tienen solo una.", " parejas"),
        ("abc", "{F} ¿Qué indica el hecho de que haya parejas de idénticos con solo una persona afectada?", "Que el ambiente o el azar también participan", "Que los gemelos no son idénticos", "Que no hay genes involucrados", "Con el mismo genoma, la diferencia solo puede venir del ambiente o del azar."),
        ("abc", "{F} ¿Cuál es un límite de este diseño según la nota de la ficha?", "Los gemelos comparten gran parte de su ambiente", "Que los mellizos no existen", "Que los gemelos no crecen", "Parte del parecido de los idénticos puede ser ambiental."),
        ("=", "En otro estudio de ejemplo, 45 de 90 parejas de idénticos con al menos un caso tienen la condición en ambas personas. ¿Cuál es la concordancia?", "45/90*100", "Son 45 de 90 parejas, es decir, la mitad: 50 %.", " %"),
        ("abc", "Un titular dice: «descubren que un gen causa el 60 % de una enfermedad en cada persona». ¿Qué problema tiene?", "Interpreta un dato de poblaciones como si fuera el riesgo de una persona", "Usa porcentajes", "Cita a los gemelos", "La concordancia no dice cuánto contribuye un gen en una persona concreta."),
        ("abc", "{F} Si los idénticos vivieran separados en ambientes muy distintos y aun así tuvieran 60 % de concordancia, ¿qué se podría concluir?", "Que los genes tienen un aporte más claro, porque el ambiente compartido pesaría menos", "Que el ambiente no importa nunca", "Que los mellizos son idénticos", "Con ambientes distintos, el parecido se atribuye más a los genes."),
        ("abc", "{F} Si la concordancia en mellizos fuera igual a la de idénticos, ¿qué sugeriría?", "Que el ambiente compartido pesa más que la diferencia genética", "Que los genes explican todo", "Que no hay gemelos", "Si el parecido es igual con distinta cercanía genética, el ambiente compartido gana peso."),
        ("abc", "{F} Una persona dice que, según la ficha, ella tendrá la condición W porque su hermano gemelo idéntico la tiene. ¿Qué respuesta corresponde?", "Que los datos describen poblaciones y no predicen lo que ocurrirá en una persona concreta", "Que sí, la tendrá con certeza", "Que el estudio es falso", "La tabla muestra frecuencias en parejas y no define el destino de una persona."),
        ("abc", "{F} Para mejorar el estudio, ¿qué dato convendría agregar?", "Qué ambientes vivieron los gemelos, por ejemplo si crecieron juntos o separados", "El color favorito de cada pareja", "El nombre de los padres", "Conocer el ambiente de cada pareja permite separar mejor su aporte del de los genes."),
    ],
    ctx=("abc", "Contexto: una revista publica «hallan el gen de la timidez». Tú recuerdas lo aprendido sobre estudios de gemelos. ¿Qué preguntas haces?", "¿Cuántas parejas se estudiaron, cómo se midió el rasgo y qué ambiente compartían?", "¿Cuántas personas leyeron la revista?", "¿Es verdad porque suena científico?", "Las preguntas sobre muestra, medición y ambiente permiten evaluar la fuente."),
    sc=[
        ("En Ciencias de la salud: ¿quiénes comparten casi todo su genoma?", "Los gemelos idénticos", "Los idénticos vienen de un mismo cigoto, por eso son casi iguales en su genoma."),
        ("ab", "Una concordancia de 60 % entre idénticos muestra que:", "Los genes aportan, pero no explican todo", "Los genes lo explican todo", "Si fuera 100 % no habría aporte del ambiente, y 60 % deja lugar para él."),
        ("ab", "El ambiente compartido es:", "Un límite de los estudios con gemelos", "Un error de cálculo", "Si los gemelos comparten ambiente, su parecido no es solo genético."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) calcula la concordancia en idénticos y en mellizos; (2) escribe una conclusión de dos oraciones sobre el aporte de genes y ambiente; (3) nombra un límite del diseño y un dato que pedirías para reducirlo.",
        "(1) Idénticos: 60 %. Mellizos: 30 %. (2) Los idénticos se parecen más, lo que sugiere un aporte genético. Como 60 % no es 100 %, el ambiente o el azar también influyen. (3) Los gemelos comparten ambiente. Pediría datos de gemelos que crecieron en ambientes distintos.",
        ["concordancias correctas", "conclusión que combina genes y ambiente", "no aplica los datos a una persona concreta", "nombra un límite y un dato por pedir"],
        ["cálculos, conclusión y límite numerados"],
        ["decir que los genes lo explican todo", "aplicar el porcentaje a una persona", "olvidar el ambiente compartido"],
        "Pregunta: «¿qué diría una concordancia de 100 % en idénticos y qué no diría?»."),
    reinforce="Escribe en tus palabras por qué comparar gemelos idénticos con mellizos ayuda a separar el aporte de los genes y del ambiente.",
    extend="Explica por qué no se puede usar la concordancia de un estudio para decir cuánto riesgo tiene una persona concreta.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 9 (modelo de ejemplo de herencia recesiva con efecto del ambiente). "
     "Un gen tiene dos alelos: N (normal) y n (alterado). La condición X solo se manifiesta con genotipo nn, que es recesivo. Las personas Nn son portadoras: tienen un alelo alterado pero no manifiestan la condición. "
     "Cada progenitor transmite uno de sus dos alelos con la misma probabilidad. "
     "Cuadro de Punnett de ejemplo para dos progenitores Nn: NN, Nn, Nn, nn. "
     "Efecto del ambiente en la condición X (de ejemplo): con alimentación ajustada, el fenotipo con genotipo nn no presenta consecuencias; sin ajuste, sí las presenta.")
build(
    O2, 3, F,
    use="Aprenderé a usar un modelo de herencia con un cuadro de Punnett y a agregarle el efecto del ambiente. Sirve para calcular probabilidades de genotipos y para entender que el genotipo no es lo mismo que el destino.",
    prior=["Sé que cada progenitor transmite un alelo de cada gen.", "Sé multiplicar fracciones sencillas.", "Distingo alelo dominante y recesivo."],
    explain=[
        "Un cuadro de Punnett es un modelo para calcular las combinaciones de alelos de los hijos a partir de los progenitores. Cada progenitor aporta uno de sus dos alelos con la misma probabilidad. Si ambos son Nn, los hijos pueden ser NN, Nn, Nn o nn: la probabilidad de nn es 1 de cada 4, o 25 %; la de Nn, 2 de cada 4, o 50 %; y la de NN, 25 %. Cada hijo tiene esas probabilidades de manera independiente.",
        "Que haya una probabilidad de 25 % no significa que de cuatro hijos uno vaya a tener nn. El azar no tiene memoria: cada hijo tiene de nuevo 25 %. Tampoco significa que las personas Nn estén enfermas. Son portadoras: tienen el alelo alterado, pero el alelo normal alcanza para que la condición no se manifieste, porque la condición es recesiva.",
        "El modelo del cuadro de Punnett predice genotipos, no fenotipos con certeza. Para llegar al fenotipo se agrega el ambiente: en la condición X, con alimentación ajustada bajo control de un equipo de salud, el genotipo nn no presenta consecuencias. Un buen modelo declara su alcance: aquí predice genotipos de un solo gen y no incluye otros genes ni otros factores.",
    ],
    vocab=[("cuadro de Punnett", "modelo que muestra las combinaciones posibles de alelos de los hijos"), ("portador", "persona con un alelo alterado que no manifiesta la condición recesiva"), ("alelo recesivo", "alelo que se manifiesta solo cuando está en dos copias"), ("probabilidad", "medida de qué tan posible es un resultado, de 0 a 100 %"), ("independencia", "cada hijo tiene las mismas probabilidades sin importar los anteriores")],
    worked=[
        ("Hacer un cuadro", "Un progenitor es Nn y el otro NN. ¿Qué genotipos pueden tener los hijos y con qué probabilidad?",
         ["El progenitor NN solo aporta N. El Nn aporta N o n con la misma probabilidad.", "Combinaciones: NN, Nn, NN, Nn.", "Dos de cuatro son NN y dos de cuatro son Nn."],
         "50 % NN y 50 % Nn; ninguno nn"),
        ("Interpretar la independencia", "Dos progenitores Nn tienen un hijo nn. ¿Cuál es la probabilidad de que el segundo hijo sea nn?",
         ["Cada hijo recibe sus alelos de manera independiente.", "El primer hijo no cambia la probabilidad del segundo.", "La probabilidad sigue siendo 1 de cada 4."],
         "25 %"),
    ],
    mistakes=[("Pensar que si el primer hijo es nn, el siguiente tiene menos probabilidad.", "Cada hijo tiene las mismas probabilidades porque el azar no tiene memoria.", "Recuerda que cada hijo es independiente de los anteriores."),
              ("Creer que una persona portadora tiene la condición.", "En una condición recesiva el alelo normal alcanza para que no se manifieste.", "Diferencia genotipo Nn (portadora) de genotipo nn (manifiesta).")],
    T=[
        ("abc", "En Ciencias de la salud: ¿quién es una persona portadora en una condición recesiva?", "Quien tiene un alelo alterado y no manifiesta la condición", "Quien tiene la condición manifiesta", "Quien no tiene ningún alelo alterado", "La persona portadora tiene un alelo alterado y uno normal."),
        ("{F} ¿Cuántos de los cuatro resultados del cuadro de Punnett de dos progenitores Nn son nn?", "1", "Los resultados son NN, Nn, Nn y nn, y solo uno es nn."),
        ("ab", "{F} Una persona Nn en la condición X:", "Es portadora y no manifiesta la condición", "Manifiesta la condición", "La condición es recesiva, así que se necesitan dos copias del alelo alterado."),
        ("=", "{F} Con dos progenitores Nn, ¿qué porcentaje de los hijos es en promedio portador (Nn)?", "2/4*100", "Dos de los cuatro resultados son Nn, es decir, 50 %.", " %"),
        ("=", "Dos progenitores Nn tienen hijos. ¿Qué porcentaje de ellos, en promedio, no tiene ningún alelo alterado (NN)?", "1/4*100", "Uno de los cuatro resultados del cuadro, NN, no tiene alelo alterado.", " %"),
        ("abc", "Un progenitor es NN y el otro nn. ¿Qué genotipo tienen todos sus hijos?", "Nn", "NN", "nn", "El progenitor NN aporta N y el nn aporta n, así que todos son Nn."),
        ("abc", "{F} Dos progenitores Nn tienen tres hijos sin la condición. ¿Qué probabilidad tiene el cuarto de ser nn?", "25 %, igual que antes", "100 %, porque ya le toca", "0 %, porque ya hubo tres sin la condición", "Cada hijo recibe sus alelos de manera independiente."),
        ("=", "En un conjunto de ejemplo de 8 hijos de progenitores Nn, si se cumpliera exactamente la proporción esperada, ¿cuántos serían nn?", "8*25/100", "El 25 % de 8 es 2, aunque en una familia real puede variar por azar.", " hijos"),
        ("abc", "{F} Un hijo nn se alimenta con ajuste bajo control de un equipo de salud. ¿Qué dice el modelo sobre su fenotipo?", "No presenta las consecuencias de la condición", "Presenta las consecuencias con seguridad", "Cambia su genotipo a NN", "En el modelo, el ambiente cambia el fenotipo sin cambiar el genotipo."),
        ("abc", "{F} ¿Por qué se dice que el genotipo nn no es un destino?", "Porque el ambiente, como la alimentación, puede modificar el fenotipo", "Porque el genotipo cambia con la edad", "Porque los cuadros de Punnett no funcionan", "El fenotipo resulta de genotipo y ambiente."),
        ("abc", "Un amigo dice: «si mis padres son portadores, yo estoy enfermo». ¿Qué le explicas?", "Que podría ser portador, tener nn o no tener el alelo alterado, y que un profesional puede orientarlo", "Que seguro está enfermo", "Que los portadores nunca tienen hijos con la condición", "Con padres portadores, cada hijo puede ser NN, Nn o nn."),
        ("abc", "{F} ¿Qué limitación tiene este modelo?", "Considera un solo gen y no incluye otros genes ni otros factores", "No usa letras", "Solo sirve para animales", "El modelo es simple y no representa condiciones multifactoriales."),
        ("abc", "{F} Si una pareja portadora se pregunta por su riesgo, ¿cuál es la mejor acción?", "Conversar con un profesional de salud o un servicio de orientación genética", "Decidir solo con el cuadro de este cuaderno", "Evitar hablar del tema", "Una orientación profesional considera la situación completa y respeta a las personas."),
    ],
    ctx=("abc", "Contexto: en el liceo te piden explicar en un afiche por qué «ser portador no es estar enfermo». ¿Qué mensaje central eliges?", "Una persona portadora tiene un alelo alterado, pero el normal evita que la condición se manifieste", "Los portadores deben ser aislados", "Los portadores siempre transmiten la condición", "El mensaje aclara el significado de portador sin estigmatizar."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un alelo recesivo?", "Un alelo que se manifiesta solo cuando está en dos copias", "El alelo recesivo queda oculto si hay un alelo dominante."),
        ("ab", "Con progenitores Nn y Nn, la probabilidad de nn en cada hijo es:", "25 %", "50 %", "Uno de los cuatro resultados del cuadro de Punnett es nn."),
        ("ab", "Un cuadro de Punnett predice:", "Genotipos probables", "Con certeza el fenotipo de cada hijo", "Predice combinaciones de alelos y no el fenotipo sin conocer el ambiente."),
    ],
    op=("Con el modelo de la ficha {F} haz lo siguiente: (1) arma el cuadro de Punnett para un progenitor Nn y otro nn; (2) calcula el porcentaje de cada genotipo; (3) explica en dos oraciones qué cambia en el fenotipo de un hijo nn según el ambiente.",
        "(1) Resultados: Nn, Nn, nn, nn. (2) 50 % Nn y 50 % nn, y 0 % NN. (3) Con alimentación ajustada por un equipo de salud, el hijo nn no presenta consecuencias. Sin ajuste, sí las presenta, aunque su genotipo es el mismo.",
        ["cuadro con cuatro combinaciones correctas", "porcentajes correctos", "explica el efecto del ambiente", "no da consejos médicos personales"],
        ["cuadro, porcentajes y explicación"],
        ["no incluir los cuatro resultados", "creer que portador es estar enfermo", "pensar que el genotipo fija el fenotipo"],
        "Pregunta: «¿qué más tendría que incluir el modelo para describir una condición multifactorial?»."),
    reinforce="Haz el cuadro de Punnett para un progenitor NN y otro Nn, y escribe qué porcentaje de hijos será portador.",
    extend="Explica por qué una probabilidad de 25 % no garantiza que uno de cada cuatro hijos sea nn en una familia concreta.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 10 (tabla de ejemplo de una condición multifactorial). Casos nuevos en 10 años por cada 1.000 personas adultas, según una variante genética de riesgo y el hábito de actividad física. "
     "Sin variante y activas: 20 casos. Sin variante y sedentarias: 40 casos. Con variante y activas: 40 casos. Con variante y sedentarias: 120 casos. "
     "Nota: «activas» significa que cumplen la recomendación general de actividad física de su edad; «sedentarias», que no la cumplen. Los números son de ejemplo y no sirven para calcular el riesgo de una persona.")
build(
    O2, 4, F,
    use="Aprenderé a analizar una tabla de riesgo para ver el efecto de un gen, del ambiente y de su interacción. Sirve para reconocer que la actividad física y otros hábitos pueden cambiar el riesgo incluso en quienes tienen una variante genética.",
    prior=["Sé calcular una razón entre dos números.", "Sé leer una tabla de doble entrada.", "Sé qué es una condición multifactorial."],
    explain=[
        "En una condición multifactorial, el riesgo depende de la variante genética y del ambiente, y además de cómo se combinan. Para analizarlo se compara una tabla de doble entrada. La razón de riesgo divide el riesgo de un grupo por el de otro grupo de referencia. Si es 2, el grupo tiene el doble de riesgo. Si es 1, no hay diferencia.",
        "Hay interacción cuando el efecto de un factor cambia según el otro. En la ficha, la variante duplica el riesgo en personas activas (de 20 a 40) y lo triplica en sedentarias (de 40 a 120). Es decir, el ambiente importa más en quienes tienen la variante. Y lo contrario también: en personas con variante, ser activa baja el riesgo de 120 a 40.",
        "La epigenética estudia cambios químicos que encienden o apagan genes sin cambiar la secuencia del ADN, y que pueden verse influidos por el ambiente. Es otro modo de interacción entre genoma y ambiente. Estos datos son de poblaciones y sirven para decidir medidas de prevención. La información genética es privada y no debe usarse para discriminar. Las dudas personales se conversan con un profesional de salud.",
    ],
    vocab=[("razón de riesgo", "riesgo de un grupo dividido por el riesgo de un grupo de referencia"), ("interacción", "situación en que el efecto de un factor depende del otro"), ("variante genética de riesgo", "forma de un gen que se asocia a mayor probabilidad de una condición"), ("epigenética", "cambios que activan o silencian genes sin alterar la secuencia del ADN"), ("grupo de referencia", "grupo con el que se compara")],
    worked=[
        ("Calcular una razón de riesgo", "En una tabla de ejemplo, el riesgo del grupo A es 30 casos y el del grupo B, de referencia, es 10 casos. ¿Cuál es la razón de riesgo?",
         ["Se divide el riesgo del grupo A por el del grupo de referencia.", "30 dividido por 10 es 3."],
         "3: el grupo A tiene el triple de riesgo"),
        ("Detectar interacción", "En otra tabla de ejemplo, un factor duplica el riesgo en un grupo y lo multiplica por cinco en otro. ¿Hay interacción?",
         ["Hay interacción si el efecto de un factor cambia según el otro.", "Aquí el efecto cambia de dos veces a cinco veces según el grupo."],
         "Sí, hay interacción"),
    ],
    mistakes=[("Concluir que la variante genética «hace» que la persona enferme.", "La variante cambia la probabilidad, y el ambiente la modifica.", "Habla de riesgo y no de destino."),
              ("Ignorar que el ambiente es más importante en quienes tienen la variante.", "En la tabla, la razón de riesgo del ambiente es mayor con variante que sin ella.", "Compara los efectos del ambiente en cada grupo genético.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué indica una razón de riesgo de 2?", "Que el grupo tiene el doble de riesgo que el de referencia", "Que el grupo no tiene riesgo", "Que el grupo tiene la mitad del riesgo", "Una razón de 2 significa dos veces el riesgo del grupo de referencia."),
        ("{F} ¿Cuántos casos hay en el grupo sin variante y activo?", "20", "La ficha indica 20 casos por cada 1.000 en ese grupo."),
        ("=", "{F} ¿Cuál es la razón de riesgo de las personas con variante y activas, respecto a sin variante y activas?", "40/20", "Se divide 40 entre 20, que es 2.", " veces"),
        ("=", "{F} ¿Cuál es la razón de riesgo de las personas con variante y sedentarias, respecto a sin variante y sedentarias?", "120/40", "Se divide 120 entre 40, que es 3.", " veces"),
        ("=", "{F} ¿Cuántos casos menos por 1.000 hay entre las personas con variante si son activas en vez de sedentarias?", "120-40", "Pasar de 120 a 40 casos es una diferencia de 80 casos.", " casos por 1.000"),
        ("abc", "{F} Según la tabla, ¿qué ocurre con el riesgo de las personas sin variante que pasan de sedentarias a activas?", "Disminuye de 40 a 20", "Aumenta de 20 a 40", "No cambia", "La tabla muestra 40 casos en sedentarias y 20 en activas."),
        ("abc", "{F} ¿Se observa interacción entre la variante y la actividad física?", "Sí, porque el efecto de la variante es mayor en las personas sedentarias", "No, porque el efecto es igual en todos los grupos", "No, porque solo importan los genes", "La razón de riesgo pasa de 2 a 3, así que el efecto de la variante cambia según el hábito."),
        ("=", "{F} ¿Cuántas veces más riesgo tiene el grupo con variante y sedentario que el grupo sin variante y activo?", "120/20", "Se divide 120 entre 20, que es 6.", " veces"),
        ("abc", "{F} Alguien dice: «con la variante da lo mismo ser activo o sedentario». ¿Qué responde la tabla?", "Con variante, pasar de sedentario a activo baja el riesgo de 120 a 40", "Tiene razón, porque en ambos casos hay riesgo", "No hay datos para esa comparación", "La tabla muestra que el hábito cambia mucho el riesgo, incluso con la variante."),
        ("abc", "{F} ¿Por qué es incorrecto decir que quien tiene la variante «tendrá» la condición?", "Porque la variante cambia la probabilidad y el riesgo depende también del ambiente", "Porque las variantes no existen", "Porque la tabla no tiene números", "La tabla muestra riesgos, no destinos, y con actividad el riesgo baja."),
        ("abc", "{F} Un equipo de salud pública quiere priorizar acciones. Según la tabla, ¿dónde un programa de actividad física baja más los casos por 1.000?", "En las personas con variante, donde baja 80 casos", "En las personas sin variante, donde baja 20 casos", "En ningún grupo", "Con variante, el cambio de sedentario a activo reduce 80 casos, más que los 20 de quienes no la tienen."),
        ("abc", "{F} ¿Por qué estos datos no sirven para calcular el riesgo de una persona concreta?", "Porque son promedios de poblaciones y ejemplos", "Porque la tabla tiene un error de ortografía", "Porque todos tienen el mismo riesgo", "Los datos describen grupos, y el riesgo individual depende de más factores."),
        ("abc", "Una empresa de ejemplo pide a sus empleados los resultados de sus pruebas genéticas para decidir contrataciones. ¿Qué problema ético hay?", "Se podría discriminar con información privada que solo indica riesgos", "Ninguno, porque es información pública", "Que los empleados ya no tienen genes", "La información genética es privada y no debe usarse para discriminar."),
    ],
    ctx=("abc", "Contexto: una persona joven de ejemplo se entera de que un familiar tiene una condición multifactorial y le preocupa su riesgo. ¿Qué mensaje basado en esta clase le darías?", "Que el riesgo depende de genes y del ambiente, que hábitos saludables ayudan, y que puede conversar con un profesional de salud", "Que está condenada a tener la condición", "Que no tiene ningún riesgo", "El mensaje es esperanzador y realista, y orienta a la consulta profesional."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la interacción entre gen y ambiente?", "Cuando el efecto de un factor depende del otro", "En la interacción, el efecto del ambiente cambia según el genotipo."),
        ("ab", "La epigenética estudia:", "Cambios que activan o silencian genes sin cambiar la secuencia del ADN", "Solo cambios en el orden de las letras del ADN", "La epigenética no altera la secuencia, solo la actividad de los genes."),
        ("ab", "La información genética de una persona debe:", "Mantenerse privada y no usarse para discriminar", "Publicarse para todos", "Los datos genéticos son sensibles y requieren protección."),
    ],
    op=("Con la tabla de la ficha {F} haz lo siguiente: (1) calcula la razón de riesgo de la variante en activas y en sedentarias; (2) escribe una conclusión de dos oraciones sobre interacción; (3) propone una medida de salud pública y una precaución ética sobre la información genética.",
        "(1) Activas: 40 entre 20 es 2. Sedentarias: 120 entre 40 es 3. (2) La variante aumenta el riesgo, más en sedentarias que en activas, así que hay interacción. Con variante, ser activa baja el riesgo de 120 a 40. (3) Fomentar programas de actividad física para toda la población. La información genética de cada persona debe ser privada.",
        ["razones de riesgo correctas", "conclusión que reconoce la interacción", "medida de salud pública coherente", "precaución ética explícita"],
        ["cálculos, conclusión y medida numerados"],
        ["hablar de destino en vez de riesgo", "no usar los datos de la tabla", "olvidar la privacidad"],
        "Pregunta: «¿qué ocurriría con la conclusión si la variante fuera muy poco frecuente en la población?»."),
    reinforce="Escribe una frase que explique por qué una variante genética cambia el riesgo pero no determina el resultado.",
    extend="Explica qué es la epigenética con tus palabras y por qué es una forma de interacción entre genoma y ambiente.",
)
