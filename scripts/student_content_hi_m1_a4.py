"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 04 (idea de progreso, ciencia y dominio de la naturaleza)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 04"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (siglo XIX: años 1801 a 1900). "
     "Idea de progreso indefinido: creencia en que la humanidad mejora sin límite gracias a la ciencia, la técnica y la razón. "
     "Positivismo: corriente de pensamiento que sostiene que el conocimiento verdadero viene de la observación y la ciencia; su lema asociado es «orden y progreso». "
     "Optimismo histórico: confianza en que el futuro será mejor que el pasado. "
     "Hitos: primer ferrocarril público de vapor de Inglaterra (Stockton–Darlington), 1825; Universidad de Chile, 1842; Exposición Universal de Londres, 1851; primer ferrocarril de Chile (Caldera–Copiapó), 1851; libro «El origen de las especies» de Darwin, 1859; Canal de Suez, 1869.")
build(
    OA, 1, F,
    use="Aprenderé a situar la idea de progreso del siglo XIX en el tiempo y en el espacio, y a plantear la pregunta que guía este tema: ¿cómo la ciencia y la técnica cambiaron la visión del mundo?",
    prior=["Sé qué es la industrialización de manera general.", "Sé calcular diferencias entre años.", "Sé que las ideas se expresan en hechos."],
    explain=[
        "En el siglo XIX muchas personas de Europa y de América Latina creyeron que la humanidad avanzaba sin límite. Esa creencia se llama idea de progreso indefinido. Se apoyaba en los avances de la ciencia y la técnica: los ferrocarriles, el telégrafo, las máquinas y los nuevos descubrimientos científicos. Hoy sabemos que el progreso tuvo costos, pero en esa época se vivía con entusiasmo.",
        "El positivismo es una corriente que afirma que el conocimiento verdadero viene de la observación y de la ciencia, no de la tradición ni de la religión. Su lema asociado es «orden y progreso». El optimismo histórico es la confianza en que el futuro será mejor. Estas ideas influyeron en gobiernos, escuelas y universidades de América Latina, como la Universidad de Chile fundada en 1842.",
        "Otra idea del siglo fue el dominio de la naturaleza: la humanidad podía transformar ríos, montañas y bosques con la técnica. El Canal de Suez, abierto en 1869, unió el mar Mediterráneo con el mar Rojo. Al situar estos hitos hay que evitar un error: pensar que todo el mundo compartía el optimismo. Hubo también críticas y personas que no se beneficiaron.",
    ],
    vocab=[("progreso indefinido", "creencia en que la humanidad mejora sin límite gracias a la ciencia y la técnica"), ("positivismo", "corriente que sostiene que el conocimiento verdadero viene de la observación y la ciencia"), ("optimismo histórico", "confianza en que el futuro será mejor que el pasado"), ("técnica", "conjunto de procedimientos y herramientas para producir o construir algo"), ("dominio de la naturaleza", "idea de que se puede transformar la naturaleza con la técnica")],
    worked=[
        ("Calcular una diferencia", "¿Cuántos años pasaron entre el primer ferrocarril público de vapor de Inglaterra (1825) y el de Chile (1851)?", ["Tomo los dos años de la ficha.", "Resto: 1851 − 1825 = 26."], "26 años"),
        ("Ubicar un hito en su siglo", "¿A qué siglo pertenece el Canal de Suez, 1869?", ["El siglo XIX va de 1801 a 1900.", "El año 1869 está en ese tramo."], "Siglo XIX"),
    ],
    mistakes=[("Decir que todas las personas del siglo XIX creían en el progreso.", "Hubo críticos y personas que no se beneficiaron.", "Escribe «muchos» o «una parte de la sociedad»."),
              ("Confundir positivismo con optimismo histórico.", "El positivismo es una corriente sobre el conocimiento; el optimismo es una actitud ante el futuro.", "Define cada término por separado.")],
    T=[
        ("{F} ¿Qué es la idea de progreso indefinido según la ficha?", "La creencia en que la humanidad mejora sin límite gracias a la ciencia y la técnica", "La ficha la define así."),
        ("{F} ¿Cuál es el lema asociado al positivismo?", "Orden y progreso", "La ficha lo indica."),
        ("{F} ¿En qué año se publicó «El origen de las especies» de Darwin?", "1859", "La ficha lo fecha."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación de la Universidad de Chile y el Canal de Suez?", "1869-1842", "Se resta el año de la Universidad al del Canal.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Exposición Universal de Londres y el Canal de Suez?", "1869-1851", "Se resta el año de la Exposición al del Canal.", " años"),
        ("{F} ¿Qué hito pertenece primero? A) Primer ferrocarril de Inglaterra B) Canal de Suez", "A) Primer ferrocarril de Inglaterra", "1825 es anterior a 1869."),
        ("{F} Una persona dice: «El conocimiento verdadero viene de la observación y la ciencia, no de la tradición». ¿Qué corriente expresa? A) Positivismo B) Optimismo histórico", "A) Positivismo", "Es la definición de positivismo de la ficha."),
        ("{F} Un ingeniero de 1860 dice: «Dentro de cincuenta años todo será mejor». ¿Qué actitud muestra? A) Optimismo histórico B) Crítica al progreso", "A) Optimismo histórico", "Confía en que el futuro será mejor."),
        ("{F} ¿Cuál es un ejemplo de dominio de la naturaleza? A) Abrir un canal que une dos mares B) Esperar la lluvia", "A) Abrir un canal que une dos mares", "Es una transformación del territorio con técnica."),
        ("{F} ¿Por qué el Canal de Suez se relaciona con la idea de progreso?", "Porque muestra que la técnica podía transformar la naturaleza y acortar rutas", "Une dos mares con técnica."),
        ("{F} Un compañero dice: «Todos en el siglo XIX eran optimistas». Corrígelo.", "Muchas personas lo eran, pero hubo críticas y grupos que no se beneficiaron", "La explicación señala que no todos compartían el optimismo."),
        ("{F} ¿Cuál es la mejor pregunta histórica para este tema? A) ¿Cómo la ciencia y la técnica cambiaron la visión del mundo en el siglo XIX? B) ¿Qué invento era el más bonito?", "A) ¿Cómo la ciencia y la técnica cambiaron la visión del mundo en el siglo XIX?", "La A se responde con hechos; la B es preferencia."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y va de 1820 a 1870. ¿Cuántos centímetros mide?", "5 cm", "Se divide el tramo de 50 años por 10."),
    ],
    ctx=("Un museo de ciencia titula una vitrina «El progreso del siglo XIX fue bueno para todos». ¿Qué problema tiene? A) Generaliza sin considerar costos ni grupos perjudicados B) Usa un siglo equivocado", "A) Generaliza sin considerar costos ni grupos perjudicados", "La ficha habla de optimismo, pero la explicación recuerda críticas y costos."),
    sc=[("¿Qué es el positivismo?", "Una corriente que sostiene que el conocimiento viene de la observación y la ciencia", "Así se define."),
        ("¿Qué es el optimismo histórico?", "La confianza en que el futuro será mejor que el pasado", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1842 y 1859?", "1859-1842", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1820 a 1870 con escala 1 cm = 10 años y marca estos hitos: ferrocarril de Inglaterra (1825), Universidad de Chile (1842), Exposición de Londres (1851), Darwin (1859) y Canal de Suez (1869). Debajo escribe una frase que explique qué es la idea de progreso indefinido. {F}",
        "Posiciones desde 1820: 0,5; 2,2; 3,1; 3,9; 4,9 cm. Frase: «Es la creencia en que la humanidad mejora sin límite gracias a la ciencia y la técnica».",
        ["respeta la escala", "los cinco hitos están bien ubicados", "la definición es correcta"], ["línea de tiempo", "frase escrita"], ["no medir con la escala", "confundir progreso con positivismo"],
        "Pide que cuente un invento actual que muestre la idea de progreso y una crítica posible."),
    reinforce="Explica en voz alta qué es el positivismo y qué es el optimismo histórico.",
    extend="Busca en tu casa un aparato técnico y di si sirve para dominar o transformar la naturaleza.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, discurso en la inauguración de un ferrocarril, 1860, de un ingeniero: «Hoy las montañas dejan de ser un muro. Con la ciencia y las máquinas, el hombre domina la naturaleza y avanza hacia un futuro de riqueza y paz.» "
     "Fuente B, carta de un campesino, 1862: «Los rieles pasaron por mi campo. Hubo accidentes y el ruido asusta a mis animales. No sé qué ganamos los que vivimos aquí.»")
build(
    OA, 2, F,
    use="Aprenderé a leer fuentes sobre el progreso: quién habla, cuándo, para qué, y qué voz falta.",
    prior=["Sé qué es la idea de progreso.", "Sé contextualizar una fuente.", "Sé separar descripción de interpretación."],
    explain=[
        "Un discurso de inauguración tiene un propósito claro: celebrar una obra y convencer de que fue buena. El ingeniero de la Fuente A usa palabras como «domina», «riqueza» y «paz». Son palabras de optimismo histórico. Como fuente, sirve para entender cómo pensaban quienes impulsaban las obras, pero no prueba que la obra beneficiara a todos.",
        "La carta de un campesino, en cambio, es privada y muestra una vivencia distinta: los rieles pasaron por su campo, hubo accidentes y los animales se asustan. Es una fuente que muestra costos de la técnica. También tiene límites: expresa la opinión de una persona y no de todos los campesinos.",
        "Para analizar, contextualiza cada fuente (autor, fecha, propósito) y compara. Pregunta: ¿qué voz falta? Aquí no aparecen quienes trabajaron en la obra ni los dueños de los trenes. Una conclusión sólida dice qué muestran las fuentes y reconoce qué no pueden probar.",
    ],
    vocab=[("discurso", "texto que se dice en público para informar o convencer"), ("propósito", "intención con la que se escribe una fuente"), ("costos del progreso", "daños o pérdidas que acompañan a una transformación"), ("voz ausente", "grupo que no aparece en las fuentes"), ("inauguración", "acto de abrir una obra al público")],
    worked=[
        ("Contextualizar", "¿Quién escribe la Fuente A, cuándo y para qué?", ["Autor: un ingeniero.", "Fecha: 1860. Propósito: celebrar la obra y convencer de sus beneficios."], "Un ingeniero, en 1860, para celebrar la obra"),
        ("Descripción o interpretación", "(1) «El ingeniero dice que el hombre domina la naturaleza». (2) «El ingeniero no se preocupaba de nadie». ¿Cuál es descripción?", ["La (1) repite el texto.", "La (2) agrega un juicio que el texto no dice."], "La (1) describe; la (2) interpreta de más"),
    ],
    mistakes=[("Tomar el discurso como prueba de que la obra benefició a todos.", "Un discurso busca convencer y celebra la obra.", "Pregunta qué voces faltan."),
              ("Concluir con una sola carta que todos los campesinos sufrieron.", "La carta muestra una experiencia individual.", "Escribe «este campesino cuenta» y busca otra fuente.")],
    T=[
        ("{F} ¿Qué tipo de texto es la Fuente A?", "Un discurso de inauguración de un ferrocarril", "La ficha lo presenta así."),
        ("{F} ¿Qué dice el campesino que ocurrió en su campo?", "Pasaron los rieles, hubo accidentes y el ruido asusta a sus animales", "La Fuente B lo detalla."),
        ("{F} ¿Qué palabras de optimismo usa el ingeniero?", "Domina, riqueza y paz", "El texto las usa."),
        ("=", "{F} ¿Cuántos años separan la Fuente A de la Fuente B?", "1862-1860", "Se resta el año del discurso al de la carta.", " años"),
        ("{F} ¿Qué fuente muestra costos del progreso? A) La Fuente B B) La Fuente A", "A) La Fuente B", "El campesino cuenta accidentes y ruido."),
        ("{F} ¿Qué fuente busca convencer a muchas personas? A) La Fuente A B) La Fuente B", "A) La Fuente A", "Un discurso se dice en público."),
        ("{F} ¿Cuál frase describe la Fuente B? A) El campesino dice que no sabe qué ganan los que viven allí B) El campesino quería destruir el tren", "A) El campesino dice que no sabe qué ganan los que viven allí", "La frase B agrega una intención que no está en el texto."),
        ("{F} ¿Qué idea del ingeniero se relaciona con el dominio de la naturaleza? A) Las montañas dejan de ser un muro B) La paz llegará pronto", "A) Las montañas dejan de ser un muro", "Habla de transformar el territorio con técnica."),
        ("{F} ¿Qué voz falta en las dos fuentes? A) Las personas que trabajaron en la obra B) El ingeniero", "A) Las personas que trabajaron en la obra", "Ni el discurso ni la carta las dan a conocer."),
        ("{F} ¿Por qué el discurso del ingeniero no prueba que la obra benefició a todos?", "Porque su propósito era celebrar la obra y no considera a quienes perdieron", "El discurso defiende una visión."),
        ("{F} Un compañero concluye: «Todos los campesinos sufrieron por los trenes». ¿Qué corrección haces?", "La carta muestra la experiencia de un solo campesino", "Una carta no prueba lo que vivieron todos."),
        ("{F} ¿Qué fuente nueva serviría para saber si la obra tuvo beneficios para el comercio? A) Un registro de precios y cargas transportadas B) Un poema sobre el campo", "A) Un registro de precios y cargas transportadas", "Aporta datos sobre efectos económicos."),
        ("{F} ¿Qué conclusión es más proporcional? A) Las fuentes muestran entusiasmo en quienes impulsaron la obra y costos para algunos habitantes B) Las fuentes prueban que el progreso fue bueno para todos", "A) Las fuentes muestran entusiasmo en quienes impulsaron la obra y costos para algunos habitantes", "No dice más de lo que muestran las dos fuentes."),
    ],
    ctx=("Para una exposición sobre el ferrocarril en el siglo XIX, un grupo quiere usar solo discursos de inauguración. ¿Qué recomiendas? A) Sumar cartas o testimonios de quienes vivieron cerca de las obras B) Usar solo discursos porque son oficiales", "A) Sumar cartas o testimonios de quienes vivieron cerca de las obras", "Las voces de los afectados completan la visión."),
    sc=[("¿Qué es el propósito de una fuente?", "La intención con la que se escribe", "Así se define."),
        ("¿Qué es una voz ausente?", "Un grupo que no aparece en las fuentes", "Así se define."),
        ("¿Quién escribe la Fuente B?", "Un campesino", "La ficha lo indica.")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (una frase); qué interpretas (una frase que empiece con «Esto sugiere que…»). Cierra con una frase que diga qué no puedes concluir y qué voz falta. {F}",
        "Fuente A. Autor y fecha: un ingeniero, 1860. Dice: las montañas dejan de ser un muro por la técnica. Interpretación: esto sugiere que quienes impulsaban las obras confiaban en dominar la naturaleza. No puedo concluir que la obra beneficiara a todos; falta la voz de quienes la construyeron.",
        ["contextualiza", "separa descripción e interpretación", "señala límite y voz ausente"], ["tabla de tres filas", "frase de cierre"], ["usar un juicio como descripción", "generalizar con una sola fuente"],
        "Pide que cuente cómo habría narrado la obra un trabajador."),
    reinforce="Explica por qué un discurso y una carta personal sirven para cosas distintas.",
    extend="Imagina el discurso de inauguración de una obra de tu ciudad y escribe una frase optimista y otra crítica.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de cambio, continuidad y territorio; los tiempos de viaje son de ejemplo). "
     "Canal de Suez, 1869: une el mar Mediterráneo con el mar Rojo; permite a los barcos ir de Europa a Asia sin rodear África. "
     "Viaje de ejemplo entre dos puertos: por el sur de África, 60 días; por el Canal de Suez, 35 días. "
     "Ferrocarril Caldera–Copiapó, 1851: lleva minerales de la zona minera a un puerto del norte de Chile. "
     "Continuidades: la mayoría de la población seguía viviendo en el campo y trabajando con herramientas manuales; las condiciones de vida de los trabajadores eran duras.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio en el siglo XIX: cómo la técnica transformó espacios y qué siguió igual.",
    prior=["Sé qué es la idea de progreso.", "Sé que las fuentes expresan intereses.", "Sé calcular diferencias y porcentajes simples."],
    explain=[
        "La técnica del siglo XIX transformó el territorio. El Canal de Suez permitió ir de Europa a Asia sin rodear África y acortó el tiempo de viaje. El ferrocarril Caldera–Copiapó conectó una zona minera con un puerto y facilitó sacar minerales para venderlos. Así, la naturaleza se transformó y los espacios quedaron mejor conectados.",
        "Al mismo tiempo hubo continuidades. La mayoría de la población siguió viviendo en el campo y trabajando con herramientas manuales. Las obras no mejoraron de inmediato la vida de los trabajadores, que a veces enfrentaban jornadas duras. Por eso el progreso técnico no fue lo mismo que mejora general de la vida.",
        "El territorio muestra quién se beneficia. Un canal o un ferrocarril conectan puntos, pero no todos los lugares. Las zonas que quedaron fuera de las rutas se quedaron con menos acceso. Para analizarlo se compara el antes y el después, se calcula cuánto cambió y se pregunta quién ganó y quién perdió.",
    ],
    vocab=[("canal", "vía de agua construida por las personas para unir mares o ríos"), ("conectividad", "facilidad para ir de un lugar a otro"), ("mineral", "sustancia sacada de una mina para ser usada o vendida"), ("puerto", "lugar donde los barcos cargan y descargan"), ("continuidad", "lo que sigue igual a lo largo del tiempo")],
    worked=[
        ("Calcular ahorro de tiempo", "¿Cuántos días se ahorran en el viaje de ejemplo al usar el Canal de Suez?", ["Por el sur de África: 60 días. Por Suez: 35 días.", "Resto: 60 − 35 = 25."], "25 días"),
        ("Calcular el porcentaje del ahorro", "¿Qué porcentaje aproximado del viaje original se ahorra?", ["Se ahorran 25 de 60 días.", "25 ÷ 60 es menos de la mitad; es aproximadamente 42 %."], "Aproximadamente 42 %"),
    ],
    mistakes=[("Creer que el progreso técnico mejoró de inmediato la vida de todos.", "La ficha muestra continuidades de trabajo manual y condiciones duras.", "Pregunta qué cambió y qué siguió igual."),
              ("Olvidar que un canal o ferrocarril conecta solo algunos lugares.", "Los territorios fuera de la ruta no se beneficiaron igual.", "Pregunta qué zonas quedaron conectadas y cuáles no.")],
    T=[
        ("{F} ¿Qué dos mares une el Canal de Suez?", "El mar Mediterráneo y el mar Rojo", "La ficha lo dice."),
        ("{F} ¿Qué transportaba el ferrocarril Caldera–Copiapó?", "Minerales", "La ficha lo indica."),
        ("{F} ¿En qué año se inauguró el Canal de Suez?", "1869", "La ficha lo fecha."),
        ("=", "{F} En otro viaje de ejemplo, por el sur de África se tardan 72 días y por Suez 41 días. ¿Cuántos días se ahorran?", "72-41", "Se resta el viaje por Suez al viaje por África.", " días"),
        ("=", "{F} Una carga viaja 3 días en tren hasta el puerto y luego 35 días en barco por Suez (datos de ejemplo). ¿Cuántos días dura el traslado completo?", "3+35", "Se suman el tramo en tren y el tramo en barco.", " días"),
        ("{F} ¿Qué es un cambio? A) El tiempo de viaje entre Europa y Asia se redujo B) La mayoría de la población siguió viviendo en el campo", "A) El tiempo de viaje entre Europa y Asia se redujo", "Es algo que se transformó; la B es una continuidad."),
        ("{F} ¿Qué es una continuidad? A) Se siguió trabajando con herramientas manuales B) Se abrió un canal", "A) Se siguió trabajando con herramientas manuales", "Es algo que se mantuvo."),
        ("{F} ¿Qué territorio se benefició con el ferrocarril Caldera–Copiapó? A) La zona minera y el puerto B) Un pueblo alejado sin rieles", "A) La zona minera y el puerto", "Quedaron conectados por la vía."),
        ("{F} Un pueblo de campo no está en la ruta del ferrocarril. ¿Qué es probable? A) Quedó con menos acceso a mercados B) Quedó mejor conectado que la ciudad", "A) Quedó con menos acceso a mercados", "Las rutas conectan solo algunos lugares."),
        ("{F} ¿Por qué el Canal de Suez es un ejemplo de dominio de la naturaleza?", "Porque se construyó con técnica para unir dos mares y acortar una ruta", "La técnica transformó el territorio."),
        ("{F} Un compañero dice: «Con los canales y los trenes cambió toda la vida de la población». ¿Qué continuidad de la ficha lo contradice?", "La mayoría seguía en el campo y trabajaba con herramientas manuales", "La mayoría de la población no cambió de inmediato."),
        ("{F} ¿Qué conclusión es más ajustada? A) La técnica acortó rutas y conectó zonas, pero muchas condiciones de vida continuaron B) La técnica cambió todo en el siglo XIX", "A) La técnica acortó rutas y conectó zonas, pero muchas condiciones de vida continuaron", "Reúne cambio y continuidad."),
        ("{F} ¿Qué pregunta ayuda a evaluar a quién benefició una obra? A) ¿Qué lugares y grupos quedaron conectados y cuáles no? B) ¿Qué color tenían los vagones?", "A) ¿Qué lugares y grupos quedaron conectados y cuáles no?", "Orienta el análisis del territorio y de los actores."),
    ],
    ctx=("Un periódico escolar quiere mostrar el cambio que provocó un canal con solo el dato «ahorro de 25 días». ¿Qué otro dato daría una visión más completa? A) Qué grupos quedaron fuera de la ruta o cuánto costó la obra B) El nombre del ingeniero", "A) Qué grupos quedaron fuera de la ruta o cuánto costó la obra", "Permite ver beneficios y costos."),
    sc=[("¿Qué es un canal?", "Una vía de agua construida para unir mares o ríos", "Así se define."),
        ("En el estudio del territorio del siglo XIX, ¿qué es una continuidad?", "Lo que siguió igual aunque cambiaron las obras, como el trabajo manual y la vida en el campo", "Así se aplica el término a la ficha."),
        ("=", "Un barco tarda 35 días por Suez y luego pasa 5 días descargando (datos de ejemplo). ¿Cuántos días pasan desde que zarpa hasta terminar de descargar?", "35+5", "Se suman el viaje y la descarga.", " días")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», y escribe tres datos en cada una con la ficha. Luego dibuja un esquema simple del viaje de ejemplo: una flecha larga rotulada «60 días» y una flecha corta rotulada «35 días», y escribe cuántos días se ahorran. {F}",
        "Cambió: viaje de 60 a 35 días; unión de Mediterráneo y Rojo; conexión entre mina y puerto. Continuó: población en el campo; trabajo manual; condiciones duras. Ahorro: 25 días.",
        ["usa datos de la ficha", "separa cambio y continuidad", "calcula el ahorro"], ["tabla completa", "esquema con flechas"], ["mezclar cambio y continuidad", "calcular mal el ahorro"],
        "Pide que diga qué zona crees que no se benefició de la obra."),
    reinforce="Explica en voz alta un cambio y una continuidad en el territorio del siglo XIX.",
    extend="Mira el mapa de rutas de tu región y anota un lugar que esté bien conectado y otro que no.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Ingeniero positivista, 1865: «La ciencia nos permite medir, predecir y construir. Cada obra nos acerca a una sociedad más ordenada y próspera.» "
     "Obrero del ferrocarril, 1865: «Trabajo desde el amanecer. La obra avanza, pero los accidentes son frecuentes y el salario es bajo.» "
     "Poeta romántico, 1865: «Los hombres quieren domar los ríos y las montañas, pero la naturaleza tiene un valor propio que no se mide en dinero.» "
     "Comunidad campesina, 1865: «Las nuevas obras cambiaron nuestro paisaje y el agua que usábamos para regar.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar las perspectivas de distintos actores sobre el progreso y el dominio de la naturaleza: quién lo impulsaba, quién lo vivía y quién lo criticaba.",
    prior=["Sé qué es el positivismo y el optimismo histórico.", "Sé contextualizar fuentes.", "Sé que cada actor tiene intereses."],
    explain=[
        "La idea de progreso no fue vista igual por todos. El ingeniero positivista confía en la ciencia para ordenar y mejorar la sociedad. El obrero vive las obras desde dentro: avanzan, pero con accidentes y salarios bajos. El poeta romántico critica la idea de dominar la naturaleza y afirma que tiene valor propio. La comunidad campesina vive cambios en su paisaje y en el agua.",
        "El Romanticismo fue un movimiento cultural que valoró los sentimientos, la naturaleza y la libertad individual. Muchos románticos desconfiaban de pensar solo con números. Así que dentro del mismo siglo conviven el optimismo del progreso y la crítica a sus costos. Esto muestra que el siglo XIX no se puede resumir en una sola idea.",
        "Para contrastar, pregunta qué quiere cada actor, qué le conviene y qué teme. Una explicación buena reconoce a quienes ganaron y a quienes cargaron los costos. Y no las usa para decidir quién tenía razón, sino para entender por qué pensaban distinto.",
    ],
    vocab=[("Romanticismo", "movimiento cultural que valoró los sentimientos y la naturaleza"), ("salario", "pago que recibe una persona por su trabajo"), ("riego", "aporte de agua a los cultivos"), ("costo social", "daño que sufre un grupo por una obra o decisión"), ("crítica", "análisis que señala problemas o límites")],
    worked=[
        ("Quién critica", "¿Qué actor critica la idea de dominar la naturaleza?", ["Busco una voz que defienda su valor propio.", "El poeta romántico dice que la naturaleza no se mide en dinero."], "El poeta romántico"),
        ("Quién carga costos", "¿Qué actor cuenta los costos humanos directos de una obra?", ["El obrero habla de accidentes y salario bajo.", "Los accidentes son un costo humano directo."], "El obrero del ferrocarril"),
    ],
    mistakes=[("Explicar el siglo XIX solo con la voz del ingeniero.", "Se ignoran quienes vivieron los costos y las críticas.", "Incluye al menos una voz crítica."),
              ("Pensar que el poeta romántico estaba en contra de toda técnica.", "Su crítica es contra la idea de dominar todo con dinero y técnica.", "Cita sus palabras y no más de lo que dicen.")],
    T=[
        ("{F} ¿Qué confía el ingeniero positivista que permite la ciencia?", "Medir, predecir y construir", "Su voz lo dice."),
        ("{F} ¿Qué problemas cuenta el obrero?", "Accidentes frecuentes y salario bajo", "Su voz lo señala."),
        ("{F} ¿Qué afirma el poeta romántico sobre la naturaleza?", "Que tiene un valor propio que no se mide en dinero", "Su voz lo dice."),
        ("{F} ¿Qué cambió para la comunidad campesina?", "El paisaje y el agua que usaban para regar", "Su voz lo cuenta."),
        ("{F} ¿Qué actor representa mejor el optimismo histórico? A) El ingeniero positivista B) El poeta romántico", "A) El ingeniero positivista", "Cree que cada obra acerca a una sociedad próspera."),
        ("{F} ¿Qué actor cuestiona la idea de progreso? A) El poeta romántico B) El ingeniero positivista", "A) El poeta romántico", "Critica el deseo de domar la naturaleza."),
        ("{F} ¿Qué actor vive las obras desde el trabajo físico? A) El obrero B) El ingeniero", "A) El obrero", "Trabaja desde el amanecer en la obra."),
        ("{F} ¿Qué dos actores comparten una preocupación por el costo de las obras? A) El obrero y la comunidad campesina B) El ingeniero y el poeta", "A) El obrero y la comunidad campesina", "Ambos cuentan efectos negativos en su vida."),
        ("{F} ¿Por qué el ingeniero y el obrero ven la misma obra de forma distinta?", "Porque uno ve el plan y los beneficios y el otro vive los accidentes y el bajo salario", "Sus posiciones son distintas."),
        ("{F} Un compañero dice: «Todos celebraban las obras». Refútalo con la ficha.", "El obrero, el poeta y la comunidad campesina muestran costos y críticas", "Hay voces distintas."),
        ("{F} ¿Qué voz falta para comparar la visión de quienes dirigían las empresas? A) La de un empresario dueño de la obra B) La de otro obrero", "A) La de un empresario dueño de la obra", "Completaría la perspectiva de quienes invertían."),
        ("{F} ¿Qué conclusión es más equilibrada? A) El progreso fue impulsado con optimismo, pero trabajadores, comunidades y críticos señalaron costos B) El progreso fue aceptado por todos sin crítica", "A) El progreso fue impulsado con optimismo, pero trabajadores, comunidades y críticos señalaron costos", "Reúne las cuatro voces."),
        ("{F} ¿Qué pregunta ayuda a contrastar a los actores? A) ¿Qué quiere, qué le conviene y qué teme cada uno? B) ¿Quién habló más fuerte?", "A) ¿Qué quiere, qué le conviene y qué teme cada uno?", "Es el método de contraste."),
    ],
    ctx=("Para un debate escolar sobre la construcción de un canal, el grupo A defiende la obra y el grupo B la critica. ¿Qué voz de la ficha usaría el grupo B? A) La de la comunidad campesina, por el cambio del agua B) La del ingeniero, por la ciencia", "A) La de la comunidad campesina, por el cambio del agua", "Muestra un costo de la obra."),
    sc=[("¿Qué fue el Romanticismo?", "Un movimiento cultural que valoró los sentimientos y la naturaleza", "Así se define."),
        ("¿Qué actor critica el dominio de la naturaleza?", "El poeta romántico", "Su voz lo muestra."),
        ("¿Qué es un costo social?", "El daño que sufre un grupo por una obra o decisión", "Así se define.")],
    op=("Elige dos actores de la ficha y haz una tabla con: qué quiere, qué le conviene y qué teme. Después escribe tres líneas que expliquen por qué sus perspectivas sobre el progreso chocan. {F}",
        "Ingeniero: quiere construir; le conviene la ciencia; teme el desorden. Obrero: quiere seguridad; le conviene mejor salario; teme los accidentes. Texto: «El ingeniero ve beneficios y el obrero ve riesgos, por eso su visión del progreso es distinta».",
        ["elige dos actores", "completa las tres columnas", "explica el choque con evidencia"], ["tabla completa", "tres líneas"], ["escribir lo mismo para ambos", "opinar sin base"],
        "Pide que diga cómo se podrían reducir los costos de una obra."),
    reinforce="Elige un actor y explica en voz alta qué piensa del progreso.",
    extend="Averigua si cerca de tu casa hay una obra grande y anota quién gana y quién podría perder.",
)
