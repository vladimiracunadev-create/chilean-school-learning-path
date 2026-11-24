"""Ciencias Naturales EPJA Básica N2, módulo 3 (parte 2): OAD-10, explicar cambios del agua por energía térmica con temperatura y calor, a partir de tablas y gráficos. Todo en papel; los datos son inventados y rotulados «de ejemplo»; no se hacen experimentos."""
from __future__ import annotations

from hc_common import make_build


MATERIALS = ("Papel, lápiz y goma. Todas las tablas, gráficos descritos y observaciones están escritos en cada ejercicio y son datos de ejemplo, inventados para este cuaderno. "
             "No se calienta nada ni se hace ningún experimento: solo se leen y se analizan datos. Si algo te cuesta leer, pide apoyo a quien te acompañe.")
build = make_build(MATERIALS)

O = "EPJA-CNAT-NB2-OAD-10"
PRIOR = ["Ya veo cómo el agua se hace vapor en una olla y se vuelve hielo en el congelador.", "Sé leer tablas sencillas y sumar y restar."]

# ============================================================ clase 1
F = ("Ficha 1 (observaciones de ejemplo). A) Un cubo de hielo en un plato sobre la mesa se convierte en agua. B) La ropa mojada en el cordel se seca. "
     "C) De una olla con agua hirviendo sale vapor. D) En la tapa de la olla aparecen gotas de agua. E) El agua de una bandeja en el congelador se vuelve hielo.")
build(
    O, 1, F,
    use="Hoy reconozco los cambios del agua que veo a diario y los relaciono con el calor que gana o pierde.",
    prior=PRIOR,
    explain=[
        "El agua se encuentra en tres estados: sólido (hielo), líquido (agua) y gaseoso (vapor de agua). Tú ya ves esos cambios todos los días: el hielo que se derrite, la ropa que se seca, el vapor de la olla y las gotas en una tapa.",
        "Cuando el agua gana energía térmica, o sea calor, sus partículas se mueven más y el agua cambia hacia un estado más caliente. El hielo se derrite (fusión) y el agua líquida se evapora (evaporación). Cuando el agua pierde calor, ocurre lo contrario: el vapor se condensa (condensación) y el agua líquida se congela (solidificación).",
        "Para describir un cambio conviene nombrar tres cosas: el estado inicial, el estado final y si el agua ganó o perdió calor. Así otra persona entiende el proceso sin haberlo visto.",
    ],
    vocab=[("estado del agua", "sólido, líquido o gaseoso"), ("fusión", "paso de sólido a líquido"), ("evaporación", "paso de líquido a gas"), ("condensación", "paso de gas a líquido"), ("solidificación", "paso de líquido a sólido")],
    worked=[
        ("Nombrar un cambio", F, ["Miro la observación A: hielo pasa a agua.", "De sólido a líquido se llama fusión, y el hielo gana calor del ambiente."], "A) es fusión: el hielo gana calor y se derrite"),
        ("Cambio con pérdida de calor", "Una botella con agua se deja en el congelador y después de unas horas hay hielo.", ["El estado inicial es líquido y el final es sólido.", "Para eso el agua tuvo que perder calor."], "Es solidificación y el agua pierde calor"),
    ],
    mistakes=[("Decir que el vapor es el humo que se ve en una olla.", "El vapor de agua es un gas invisible; lo que se ve son gotas diminutas que ya se condensaron.", "Piensa que el vapor se forma antes y las gotas después."),
              ("Confundir fusión con evaporación.", "La fusión es sólido a líquido; la evaporación es líquido a gas.", "Pregunta cuál es el estado inicial y cuál el final.")],
    T=[
        ("abc", "{F} ¿Qué cambio ocurre en la observación A?", "El hielo se derrite", "El vapor se condensa", "El agua se congela", "La observación A dice que el hielo se convierte en agua."),
        ("ab", "¿Cuál es el estado del hielo?", "Sólido", "Gaseoso", "El hielo es agua en estado sólido."),
        ("abc", "{F} ¿En cuál observación el agua líquida pasa a gas?", "En la C, el agua hirviendo que da vapor", "En la E, la bandeja del congelador", "En la A, el cubo de hielo", "En la olla el agua líquida se vuelve vapor, un gas."),
        ("abc", "¿Cómo se llama el paso de líquido a gas?", "Evaporación", "Condensación", "Fusión", "La evaporación es el cambio de líquido a gas."),
        ("ab", "{F} La observación D muestra gotas en la tapa. ¿Qué cambio ocurrió?", "Condensación", "Fusión", "El vapor se enfrió al tocar la tapa más fría y pasó a líquido."),
        ("abc", "{F} ¿Qué observación muestra una solidificación?", "La E", "La B", "La C", "En la bandeja del congelador el agua líquida pasa a hielo, que es sólido."),
        ("abc", "{F} El agua de la bandeja de la observación E, ¿gana o pierde calor para volverse hielo?", "Pierde calor", "Gana calor", "No cambia su calor", "Para volverse sólida el agua debe perder energía térmica."),
        ("ab", "Una persona dice: «El hielo se derrite porque pierde calor». ¿Qué corrección es correcta?", "El hielo se derrite porque gana calor del ambiente", "Está correcto", "Para derretirse hace falta recibir energía térmica."),
        ("=", "{F} En la ficha hay 5 observaciones. Tres muestran cambios hacia un estado con más energía térmica (A, B y C). ¿Cuántas muestran cambios hacia menos energía?", "5-3", "Se resta del total las que ganan calor.", " observaciones"),
        ("abc", "Una piscina de ejemplo pierde agua porque el sol la calienta y parte pasa a vapor. ¿Qué cambio explica la pérdida?", "Evaporación", "Solidificación", "Condensación", "El agua líquida gana calor del sol y pasa a gas."),
        ("abc", "Un vaso con agua fría deja gotas por fuera en un día cálido. ¿Qué explicación es correcta?", "El vapor del aire se enfría al tocar el vaso y se condensa", "El agua pasa a través del vidrio", "El vaso produce agua", "El vapor del aire pierde calor al tocar el vaso frío y pasa a líquido."),
        ("abc", "{F} Se ordenan los cambios A, C y E según si el agua gana o pierde calor. ¿Cuál orden es correcto?", "A gana, C gana, E pierde", "A pierde, C gana, E gana", "A gana, C pierde, E pierde", "El hielo se derrite ganando calor, la olla gana calor y el congelador quita calor."),
        ("ab", "Para describir un cambio del agua, ¿qué dato es más completo?", "Estado inicial, estado final y si ganó o perdió calor", "Solo el color del agua", "Con esos tres datos otra persona entiende el cambio sin verlo."),
    ],
    ctx=("abc", "En una cocina comunitaria, una persona dice que el vapor de una olla es «humo». Otra le explica que el vapor es agua. ¿Qué explicación corresponde?", "El agua líquida ganó calor y pasó a gas; lo que se ve son gotas que ya se enfriaron", "Es el humo de la olla", "Es el aire que se quema", "El agua se evapora al calentarse y se vuelve a condensar al enfriarse."),
    sc=[("En Ciencias: ¿qué es la condensación?", "El paso de gas a líquido", "Ocurre cuando el vapor pierde calor."),
        ("¿Qué le pasa al agua cuando se derrite el hielo?", "Gana calor y pasa de sólido a líquido", "La fusión necesita recibir energía térmica."),
        ("¿Qué tres estados tiene el agua?", "Sólido, líquido y gaseoso", "Son hielo, agua y vapor de agua.")],
    op=("Describe en tres frases tres cambios del agua que veas esta semana en tu casa o en la calle (por ejemplo: ropa secándose, un charco que desaparece o un vidrio empañado). En cada una anota estado inicial, estado final y si el agua ganó o perdió calor.",
        "Un charco desaparece en la tarde: pasa de líquido a gas (evaporación) porque gana calor del sol.",
        ["las tres frases nombran estado inicial y final", "indican si gana o pierde calor", "usan al menos un nombre del cambio"],
        ["tres frases escritas"],
        ["confundir fusión con evaporación", "olvidar decir si gana o pierde calor"],
        "Pregunta: «¿De qué estado a cuál pasó y qué le ocurrió al calor?»."),
    reinforce="Observa hoy un cambio del agua y anota su estado inicial y final.",
    extend="Explica por qué un espejo de baño se empaña cuando alguien se ducha.",
)

# ============================================================ clase 2
F = ("Ficha 2 (datos de ejemplo). Taza A: 200 mL de té a 80 °C. Taza B: 200 mL de té a 40 °C. "
     "Vaso C: 200 mL de agua a 60 °C. Olla D: 2.000 mL de agua a 60 °C. Un termómetro mide la temperatura en grados Celsius (°C). "
     "Para este cuaderno, el agua pura al nivel del mar se congela a 0 °C y hierve a 100 °C.")
build(
    O, 2, F,
    use="Hoy distingo entre temperatura y calor y los uso para explicar cambios del agua.",
    prior=PRIOR + ["Conozco los estados del agua y sus cambios."],
    explain=[
        "La temperatura dice qué tan caliente o fría está algo. Se mide con un termómetro y en Chile usamos grados Celsius (°C). Una taza de té a 80 °C está más caliente que otra a 40 °C.",
        "El calor es la energía térmica que pasa de un cuerpo con más temperatura a otro con menos. Si dejas una taza de té caliente sobre la mesa, el calor pasa del té al aire hasta que ambos quedan a una temperatura parecida.",
        "Temperatura y calor no son lo mismo. Un vaso y una olla pueden estar a 60 °C, pero la olla tiene más agua y, por eso, más energía térmica. Con estos dos conceptos podemos explicar por qué el hielo se derrite o el agua hierve.",
    ],
    vocab=[("temperatura", "qué tan caliente o fría está algo"), ("termómetro", "instrumento que mide la temperatura"), ("grado Celsius (°C)", "unidad con que medimos la temperatura"), ("calor", "energía térmica que pasa de un cuerpo más caliente a uno más frío")],
    worked=[
        ("Dirección del calor", F, ["La taza A está a 80 °C y la B a 40 °C.", "El calor pasa del cuerpo más caliente al más frío."], "Si se juntan, el calor pasa de la taza A a la taza B"),
        ("Temperatura igual, calor distinto", "Se comparan el vaso C y la olla D de la ficha.", ["Los dos están a 60 °C.", "La olla tiene diez veces más agua, así que tiene más energía térmica."], "La temperatura es igual, pero la olla tiene más energía térmica"),
    ],
    mistakes=[("Decir que temperatura y calor son lo mismo.", "La temperatura dice qué tan caliente está algo; el calor es la energía que pasa de un cuerpo a otro.", "Pregunta si hablas de «qué tan caliente» o de «energía que pasa»."),
              ("Pensar que el frío pasa de un cuerpo a otro.", "Lo que pasa es el calor, siempre desde lo más caliente hacia lo más frío.", "Explica un enfriamiento como «pierde calor»." )],
    T=[
        ("abc", "{F} ¿Qué taza tiene mayor temperatura?", "La A", "La B", "Las dos tienen igual", "La taza A está a 80 °C y la B a 40 °C."),
        ("ab", "¿Con qué instrumento se mide la temperatura?", "Con un termómetro", "Con una regla", "El termómetro es el instrumento de medida de temperatura."),
        ("=", "{F} ¿Cuántos grados más caliente está la taza A que la taza B?", "80-40", "Se resta la temperatura menor a la mayor.", " °C"),
        ("abc", "{F} Si se juntan la taza A y la taza B, ¿hacia dónde pasa el calor?", "De la A a la B", "De la B a la A", "No pasa calor", "El calor va del cuerpo más caliente al más frío."),
        ("ab", "¿Qué es el calor?", "Energía térmica que pasa de un cuerpo más caliente a uno más frío", "La temperatura medida con termómetro", "La temperatura es una medida; el calor es energía que se transfiere."),
        ("abc", "{F} ¿Qué se puede decir del vaso C y la olla D?", "Tienen la misma temperatura, pero la olla tiene más energía térmica", "La olla está más caliente", "El vaso tiene más energía térmica", "Con igual temperatura, más cantidad de agua contiene más energía térmica."),
        ("abc", "Una persona deja una cuchara metálica en una olla caliente y el mango se calienta. ¿Qué ocurrió?", "El calor pasó del agua a la cuchara", "El frío pasó de la cuchara al agua", "No pasó nada", "El calor viaja de lo caliente a lo frío, y la cuchara se entibia."),
        ("=", "{F} Si la taza B se enfría 15 °C más, ¿a qué temperatura queda?", "40-15", "Se resta el descenso a la temperatura inicial de la taza B.", " °C"),
        ("ab", "Un termómetro marca 100 °C en una olla con agua pura al nivel del mar. ¿Qué se espera?", "Que el agua esté hirviendo", "Que el agua esté congelada", "Esa es la temperatura de ebullición del agua pura al nivel del mar."),
        ("abc", "{F} Una amiga dice: «La olla D está más caliente porque es más grande». ¿Qué respuesta corrige mejor?", "Están a la misma temperatura; la olla solo tiene más agua y más energía térmica", "Tiene razón: más grande, más temperatura", "La olla está más fría", "La temperatura no depende del tamaño, la cantidad de energía sí."),
        ("abc", "Un hielo a 0 °C se pone sobre una mano a 30 °C. ¿Qué ocurre con el calor?", "Pasa de la mano al hielo", "Pasa del hielo a la mano", "No pasa", "La mano está más caliente y entrega calor al hielo."),
        ("abc", "{F} ¿Por qué un vaso de agua a 60 °C se enfría antes que la olla D con la misma temperatura?", "Porque tiene menos energía térmica para perder", "Porque la olla está más fría", "Porque el vaso no tiene calor", "La olla tiene más agua y almacena más energía térmica."),
        ("ab", "Para una conclusión científica, ¿qué dato se necesita?", "Temperatura con su unidad, por ejemplo 80 °C", "Solo «está tibio»", "Medir con termómetro y anotar la unidad permite comparar."),
    ],
    ctx=("abc", "En un comedor comunitario se deja una olla grande de sopa a 70 °C y un tazón a 70 °C. Una persona pregunta cuál se enfriará primero. ¿Qué respondes?", "El tazón, porque tiene menos energía térmica", "La olla, porque tiene menos energía", "Los dos igual de rápido", "A igual temperatura, el que tiene menos cantidad pierde antes su calor."),
    sc=[("En Ciencias: ¿qué mide la temperatura?", "Qué tan caliente o fría está algo", "Se mide con termómetro en °C."),
        ("Entre una taza de té caliente y otra fría, ¿hacia dónde pasa el calor?", "Del cuerpo más caliente al más frío", "Siempre en ese sentido hasta igualar temperaturas."),
        ("¿Puede haber igual temperatura y distinta cantidad de energía térmica?", "Sí, si hay distinta cantidad de agua", "Una olla y un vaso a 60 °C tienen distinta energía térmica.")],
    op=("Con estos datos de ejemplo: una olla con 3 litros de agua a 50 °C y un vaso con 100 mL de agua a 50 °C. Escribe tres frases: cuál está más caliente, cuál tiene más energía térmica y cuál se enfriaría antes. Explica por qué.",
        "Están igual de calientes (50 °C). La olla tiene más energía térmica. El vaso se enfría antes porque tiene menos.",
        ["usa «temperatura» para qué tan caliente", "usa «energía térmica» para la cantidad", "explica con la cantidad de agua"],
        ["tres frases y una explicación"],
        ["confundir temperatura con calor", "decir que la olla está más caliente"],
        "Pregunta: «¿Hablas de qué tan caliente o de cuánta energía?»."),
    reinforce="Compara dos tazas de tu casa con agua tibia y di cuál se enfría antes y por qué.",
    extend="Explica por qué la mano siente frío al tocar un hielo.",
)

# ============================================================ clase 3
F = ("Ficha 3 (tabla de ejemplo; agua pura calentada en una olla, al nivel del mar). Tiempo (min) | Temperatura (°C): "
     "0 | 20; 2 | 38; 4 | 56; 6 | 74; 8 | 92; 10 | 100; 12 | 100; 14 | 100.")
build(
    O, 3, F,
    use="Hoy leo una tabla de temperaturas paso a paso y explico qué le pasa al agua cuando se calienta.",
    prior=PRIOR + ["Distingo temperatura y calor."],
    explain=[
        "Una tabla ordena datos en filas y columnas. Para leerla sigue tres pasos. Paso 1: lee el título y las unidades, por ejemplo minutos y grados Celsius. Paso 2: busca la fila que necesitas. Paso 3: compara los valores y describe cómo cambian.",
        "En el calentamiento de agua, la temperatura sube mientras el agua recibe calor. Cuando el agua pura llega a 100 °C al nivel del mar, empieza a hervir. Mientras hierve, la temperatura se mantiene en 100 °C aunque siga recibiendo calor, porque esa energía se usa en pasar el agua de líquido a gas.",
        "Con una tabla puedes formular una explicación: «el agua subió su temperatura porque recibió calor, y al hervir mantuvo 100 °C mientras cambiaba a vapor». Esa explicación se apoya en los datos.",
    ],
    vocab=[("tabla de datos", "datos ordenados en filas y columnas"), ("variable", "algo que cambia, como el tiempo o la temperatura"), ("hervir", "pasar de líquido a gas en todo el líquido"), ("se mantiene", "no cambia")],
    worked=[
        ("Leer un valor", F, ["Paso 1: minutos y °C.", "Paso 2: busco la fila del minuto 6.", "Paso 3: leo 74."], "A los 6 minutos el agua estaba a 74 °C"),
        ("Describir un cambio", "Entre los minutos 0 y 4 de la tabla, ¿cuánto subió la temperatura?", ["Al minuto 0 estaba en 20 °C y al minuto 4 en 56 °C.", "Se resta 56 menos 20."], "Subió 36 °C"),
    ],
    mistakes=[("Decir que la temperatura sigue subiendo mientras el agua hierve.", "En la tabla, de los 10 a los 14 minutos se mantiene en 100 °C.", "Compara los valores de varias filas antes de concluir."),
              ("Leer el valor de la fila equivocada.", "Se mira el tiempo y se confunde con la temperatura.", "Sigue la fila con el dedo y revisa las unidades.")],
    T=[
        ("abc", "{F} ¿Qué temperatura marca el minuto 4?", "56 °C", "38 °C", "74 °C", "En la fila del minuto 4 aparece 56."),
        ("ab", "{F} ¿En qué unidad está la temperatura?", "Grados Celsius", "Minutos", "La columna de temperatura está en °C y el tiempo en minutos."),
        ("=", "{F} ¿Cuántos grados subió la temperatura entre el minuto 0 y el minuto 2?", "38-20", "Se resta la temperatura inicial a la del minuto 2.", " °C"),
        ("abc", "{F} ¿Cuándo llega el agua a 100 °C?", "Al minuto 10", "Al minuto 8", "Al minuto 14", "La tabla marca 100 °C por primera vez en el minuto 10."),
        ("ab", "{F} ¿Qué pasa con la temperatura entre el minuto 10 y el 14?", "Se mantiene en 100 °C", "Sigue subiendo 18 grados cada dos minutos", "Los tres valores de esos minutos son iguales."),
        ("=", "{F} ¿Cuántos grados subió la temperatura entre el minuto 0 y el minuto 8?", "92-20", "Se resta la temperatura del minuto 0 a la del minuto 8.", " °C"),
        ("abc", "{F} Entre los minutos 0 y 8 el agua sube la misma cantidad cada dos minutos. ¿Cuánto es?", "18 °C", "20 °C", "8 °C", "Cada fila sube de 18 en 18: 38-20, 56-38, 74-56 y 92-74."),
        ("abc", "{F} ¿Cuál de estas es una explicación apoyada en los datos?", "El agua recibió calor y subió su temperatura hasta llegar a 100 °C", "El agua se calentó porque era de noche", "El agua se enfrió", "La explicación se apoya en el aumento de 20 a 100 °C."),
        ("ab", "¿Por qué la temperatura se mantiene en 100 °C mientras hierve?", "Porque la energía que recibe se usa en pasar el agua de líquido a gas", "Porque el termómetro se descompone", "Esa energía se usa en el cambio de estado, no en subir la temperatura."),
        ("=", "{F} ¿Cuántos minutos pasaron desde que el agua llegó a 100 °C (minuto 10) hasta el minuto 14?", "14-10", "Se resta el minuto en que llegó a 100 °C al minuto final.", " minutos"),
        ("abc", "{F} Una persona afirma: «El agua siguió calentándose hasta 120 °C». ¿Qué dato la contradice?", "La tabla muestra 100 °C en los minutos 10, 12 y 14", "La tabla muestra 20 °C", "La tabla no tiene minutos", "Los datos no superan los 100 °C."),
        ("abc", "{F} Se quiere repetir la medición en otra olla igual con el mismo fuego. ¿Qué dato esperas en el minuto 6?", "Un valor cercano a 74 °C", "0 °C", "200 °C", "Si todo es igual, el resultado debe ser similar."),
        ("ab", "Una buena conclusión sobre la tabla es:", "El agua recibió calor, subió hasta 100 °C y después se mantuvo en 100 °C mientras hervía", "El agua se calentó", "Debe usar datos y describir los cambios con valores."),
    ],
    ctx=("abc", "Un grupo anota la temperatura del agua de una olla cada 2 minutos y obtiene 25, 45, 65, 85, 100, 100 (datos de ejemplo). Una persona pregunta si el agua dejó de recibir calor al llegar a 100. ¿Qué respondes?", "No, sigue recibiendo calor, pero se usa en pasar a vapor y la temperatura se mantiene", "Sí, dejó de recibir calor", "El termómetro falló", "La temperatura se estabiliza en 100 °C porque el calor se usa en el cambio a vapor."),
    sc=[("En Ciencias: ¿qué es una variable?", "Algo que cambia, como el tiempo o la temperatura", "Las tablas relacionan dos variables, como el tiempo y la temperatura."),
        ("¿Qué pasa con la temperatura de agua pura que hierve al nivel del mar?", "Se mantiene en 100 °C", "La energía se usa en el cambio de estado."),
        ("¿Qué tres pasos se siguen para leer una tabla?", "Título y unidades, fila buscada y comparación", "Así se evita leer mal los datos.")],
    op=("Con esta tabla de ejemplo de un hielo que se calienta: minuto 0: -5 °C; minuto 2: 0 °C; minuto 4: 0 °C; minuto 6: 8 °C. Escribe tres observaciones y una explicación: qué pasó con la temperatura y qué hizo el hielo entre los minutos 2 y 4.",
        "La temperatura subió de -5 a 0 °C, se mantuvo en 0 °C durante dos minutos y luego subió. Entre 2 y 4 el hielo se derritió: recibía calor, pero la temperatura no cambiaba.",
        ["lee valores de la tabla", "describe los cambios con números", "relaciona la temperatura estable con el cambio de estado"],
        ["tres observaciones y una explicación"],
        ["leer mal las filas", "afirmar algo que la tabla no muestra"],
        "Pregunta: «¿Qué fila de la tabla apoya lo que dices?»."),
    reinforce="Inventa una tabla de tres filas con tiempo y temperatura y descríbela.",
    extend="Explica por qué mientras el agua hierve la temperatura no sube aunque la cocina siga encendida.",
)

# ============================================================ clase 4
F = ("Ficha 4 (gráfico de líneas de ejemplo, descrito con sus puntos). Un trozo de hielo se calienta de forma constante. "
     "Eje horizontal: tiempo en minutos. Eje vertical: temperatura en °C. Puntos unidos con líneas: (0, -10), (3, 0), (9, 0), (12, 5), (15, 10).")
build(
    O, 4, F,
    use="Hoy practico, con apoyo, la lectura de un gráfico de temperatura para explicar un cambio de estado.",
    prior=PRIOR + ["Sé leer una tabla de temperaturas."],
    explain=[
        "Un gráfico de líneas muestra cómo cambia una cantidad con el tiempo. Cada punto tiene dos datos: el tiempo en el eje horizontal y la temperatura en el eje vertical. Si la línea sube, la temperatura aumenta; si es horizontal, se mantiene.",
        "En el calentamiento de un hielo vemos tres partes. Primero la línea sube hasta 0 °C. Luego queda plana mientras el hielo se derrite, porque la energía se usa en pasar de sólido a líquido. Después vuelve a subir cuando solo hay agua líquida.",
        "Para explicar un gráfico, junta tres pasos: describe la forma de la línea, di qué ocurre con el agua en cada parte y apoya tu explicación en los valores del gráfico.",
    ],
    vocab=[("eje", "línea de un gráfico donde se marca una variable"), ("punto", "par de datos: un tiempo y una temperatura"), ("tramo plano", "parte de la línea que no sube ni baja"), ("describir un gráfico", "contar cómo cambia la línea y qué significa")],
    worked=[
        ("Leer un punto", F, ["El punto (12, 5) tiene tiempo 12 y temperatura 5.", "Lo leo como: a los 12 minutos, 5 °C."], "A los 12 minutos la temperatura es 5 °C"),
        ("Explicar el tramo plano", F, ["Entre los minutos 3 y 9 la temperatura se mantiene en 0 °C.", "En ese tramo el hielo se derrite."], "El tramo plano muestra la fusión: se recibe calor pero la temperatura no cambia"),
    ],
    mistakes=[("Pensar que en el tramo plano el hielo no recibe calor.", "Sigue recibiendo calor; esa energía se usa en la fusión y no en subir la temperatura.", "Explica el tramo plano como un cambio de estado."),
              ("Invertir los ejes y leer la temperatura como si fuera el tiempo.", "En el punto (3, 0) el primer número es el tiempo.", "Lee siempre primero el tiempo y luego la temperatura.")],
    T=[
        ("abc", "{F} ¿Cuál era la temperatura inicial del hielo?", "-10 °C", "0 °C", "10 °C", "El primer punto es (0, -10): a los 0 minutos, -10 °C."),
        ("ab", "{F} ¿Qué muestra el eje vertical?", "La temperatura en °C", "El tiempo en minutos", "El eje vertical es la temperatura y el horizontal es el tiempo."),
        ("abc", "{F} ¿Qué temperatura marca el punto (9, 0)?", "0 °C a los 9 minutos", "9 °C a los 0 minutos", "0 minutos a los 9 °C", "En cada punto, el primer número es el tiempo."),
        ("=", "{F} ¿Cuántos minutos dura el tramo plano, entre el minuto 3 y el minuto 9?", "9-3", "Se resta el tiempo inicial al tiempo final del tramo.", " minutos"),
        ("abc", "{F} ¿Qué ocurre con el hielo durante el tramo plano?", "Se derrite", "Se evapora por completo", "Se congela más", "A 0 °C, mientras recibe calor, se produce la fusión."),
        ("ab", "{F} ¿En qué momento deja de haber hielo y solo queda agua líquida?", "Hacia el minuto 9, cuando la línea vuelve a subir", "En el minuto 0", "La línea sube después del tramo plano porque ya no hay hielo."),
        ("=", "{F} ¿Cuántos grados sube la temperatura entre el minuto 9 y el minuto 15?", "10-0", "Se resta la temperatura del minuto 9 a la del minuto 15.", " °C"),
        ("abc", "{F} Una persona dice que a los 6 minutos la temperatura del agua es 6 °C. ¿Qué corrección corresponde?", "A los 6 minutos está en el tramo plano, a 0 °C", "Tiene razón", "A los 6 minutos hace 20 °C", "Entre los minutos 3 y 9 la línea está en 0 °C."),
        ("abc", "{F} ¿Cuál descripción del gráfico es mejor?", "Sube hasta 0 °C, se mantiene mientras se derrite y luego sube", "Sube siempre sin cambios", "Baja y sube", "La descripción debe incluir la forma y lo que ocurre con el hielo."),
        ("ab", "Si se calentara más fuerte, ¿cómo cambiaría el gráfico?", "Llegaría a 0 °C antes y la línea subiría más rápido", "La línea quedaría igual", "Con más calor por minuto, la temperatura cambia más rápido."),
        ("abc", "{F} Se quiere comparar con otro hielo de igual tamaño calentado igual. ¿Qué se espera del tramo plano?", "Una duración parecida y a 0 °C", "Que ocurra a 50 °C", "Que no exista", "Si todo es igual, también debería haber un tramo a 0 °C."),
        ("abc", "{F} Una afirmación segura según el gráfico es:", "Entre el minuto 3 y el 9 la temperatura no cambia", "El hielo se derritió a 10 °C", "El agua hirvió", "Esa afirmación se lee directamente del tramo plano."),
        ("ab", "Para evaluar una explicación sobre un gráfico, ¿qué conviene preguntar?", "¿Qué valores del gráfico la apoyan?", "¿Quién la dijo más fuerte?", "Una explicación científica se apoya en datos."),
    ],
    ctx=("abc", "En una charla de ejemplo muestran un gráfico de una olla con agua: la línea sube y llega a una zona horizontal a 100 °C. Una persona pregunta qué significa esa zona. ¿Qué respondes?", "El agua está hirviendo y su energía se usa en pasar a vapor", "El agua dejó de recibir calor", "El termómetro se apagó", "La zona horizontal indica cambio de estado con temperatura constante."),
    sc=[("En un gráfico de líneas, ¿qué indica un tramo plano?", "Que la temperatura se mantiene", "No sube ni baja en ese tiempo."),
        ("¿Qué muestra cada punto (tiempo, temperatura)?", "Un par de datos: cuándo y a qué temperatura", "El primer número es el tiempo."),
        ("¿Por qué hay un tramo plano al derretirse el hielo?", "Porque la energía se usa en la fusión", "No sube la temperatura mientras cambia de estado.")],
    op=("Con estos puntos de ejemplo de agua que se calienta: (0, 20), (4, 60), (8, 100), (14, 100). Dibuja el gráfico en tu cuaderno y escribe tres frases que lo expliquen: qué pasó entre 0 y 8 minutos, qué pasó entre 8 y 14 y por qué.",
        "Entre 0 y 8 minutos la temperatura subió de 20 a 100 °C. Entre 8 y 14 se mantuvo en 100 °C porque el agua hervía y pasaba a vapor.",
        ["dibuja los ejes con unidades", "marca los cuatro puntos", "explica los dos tramos"],
        ["un gráfico dibujado y tres frases"],
        ["invertir los ejes", "no explicar el tramo plano"],
        "Pregunta: «¿Qué tramo muestra el cambio de estado?»."),
    reinforce="Dibuja un gráfico de ejemplo con cuatro puntos y descríbelo en voz alta.",
    extend="Explica qué cambiaría en el gráfico si se tuviera el doble de agua con el mismo fuego.",
)

# ============================================================ clase 5
F = ("Ficha 5 (situaciones de ejemplo). A) Ropa mojada en un cordel seca más rápido en una tarde de sol que en una tarde fría y sin viento. "
     "B) Un vaso con agua fría deja gotas por fuera en un día cálido. C) Una hielera con hielo, dejada al sol, pierde el hielo antes que otra igual dejada a la sombra. "
     "D) Una olla con tapa tiene gotas en la parte interior de la tapa.")
build(
    O, 5, F,
    use="Hoy aplico lo aprendido para explicar cambios del agua en situaciones de la casa y de la comunidad.",
    prior=PRIOR + ["Distingo temperatura y calor y leo tablas y gráficos."],
    explain=[
        "Para formular una explicación en ciencias usa esta estructura: «Ocurre X porque el agua gana (o pierde) calor y cambia de un estado a otro». Una buena explicación nombra el cambio, la dirección del calor y las condiciones que influyen.",
        "La evaporación ocurre en la superficie del agua y se acelera con más temperatura, más viento y más superficie expuesta. Por eso la ropa extendida y al sol se seca más rápido que la ropa arrugada y a la sombra. En cambio, la ebullición ocurre en todo el líquido cuando alcanza su temperatura de ebullición.",
        "La condensación aparece cuando el vapor del aire toca una superficie más fría y pierde calor. Por eso se empaña un vaso frío en un día cálido o se mojan los vidrios de una cocina.",
    ],
    vocab=[("superficie expuesta", "parte del agua que está en contacto con el aire"), ("ebullición", "evaporación en todo el líquido a su temperatura de ebullición"), ("explicación", "razón basada en datos de por qué ocurre algo"), ("condiciones", "factores que influyen en un cambio")],
    worked=[
        ("Explicar una situación", F, ["La situación A habla de ropa que se seca: el agua líquida pasa a gas.", "Con sol, el agua gana más calor y se evapora antes."], "La ropa se seca antes con sol porque el agua gana más calor y se evapora más rápido"),
        ("Explicar gotas en un vaso", "En la situación B, un vaso frío muestra gotas por fuera.", ["El vapor de agua del aire toca el vaso frío.", "Pierde calor y pasa a líquido."], "Es condensación del vapor del aire; el agua no atravesó el vaso"),
    ],
    mistakes=[("Decir que el agua de las gotas «salió del vaso a través del vidrio».", "El agua viene del vapor del aire que se condensa en la superficie fría.", "Pregunta de dónde viene el vapor y por qué pierde calor."),
              ("Dar una explicación sin decir si el agua gana o pierde calor.", "Sin eso no se explica el cambio de estado.", "Siempre indica la dirección del calor.")],
    T=[
        ("abc", "{F} ¿Qué cambio ocurre en la situación A?", "Evaporación", "Condensación", "Solidificación", "La ropa mojada pierde agua líquida que pasa a gas."),
        ("ab", "{F} ¿En qué situación el agua gana calor del sol?", "En la A y en la C", "En la B y en la D", "Al sol, la ropa y el hielo reciben más calor."),
        ("=", "{F} Hay 4 situaciones en la ficha. Dos muestran condensación (B y D). ¿Cuántas no la muestran?", "4-2", "Se resta del total las situaciones con condensación.", " situaciones"),
        ("abc", "{F} ¿Por qué la ropa se seca más rápido en una tarde de sol?", "Porque el agua gana más calor y se evapora antes", "Porque el sol pesa más", "Porque la ropa produce calor", "Más calor acelera el paso del agua líquida a gas."),
        ("ab", "{F} En la situación C, ¿en cuál hielera se derrite antes el hielo?", "En la del sol, porque recibe más calor", "En la de la sombra", "Más calor significa fusión más rápida."),
        ("abc", "{F} ¿Qué explica las gotas de la tapa de la olla (D)?", "El vapor toca la tapa más fría, pierde calor y se condensa", "La tapa produce agua", "El agua salta", "Al perder calor el vapor vuelve a líquido."),
        ("abc", "Dos prendas iguales y mojadas: una extendida, otra hecha un bollo. ¿Cuál se seca antes?", "La extendida, porque tiene más superficie expuesta", "La del bollo", "Las dos igual", "La evaporación ocurre en la superficie."),
        ("ab", "Un día con viento seca más rápido la ropa. ¿Por qué?", "El viento se lleva el vapor que se forma, y se evapora más agua", "El viento calienta el agua", "El vapor que rodea la ropa se renueva y la evaporación continúa."),
        ("=", "En una tarde de ejemplo, una prenda mojada tiene 200 g de agua y pierde 50 g por hora. ¿Cuántos gramos pierde en 3 horas?", "50*3", "Se multiplica lo perdido por hora por las horas.", " g"),
        ("abc", "{F} Una persona explica C diciendo «el hielo del sol se derrite antes porque el sol lo ataca». ¿Cuál explicación es mejor?", "Recibe más calor del sol y por eso se derrite más rápido", "El sol lo ataca", "El hielo quiere ser agua", "La explicación nombra la causa con energía térmica."),
        ("abc", "{F} Para comprobar que el sol influye en C, ¿qué condición debe mantenerse igual?", "El tamaño de las hieleras y la cantidad de hielo", "El color de la ropa", "La hora de almuerzo", "Solo cambia la exposición al sol; lo demás se controla."),
        ("abc", "Una persona dice que el agua de la olla hirviendo y la de un charco se evaporan de la misma manera. ¿Qué es correcto?", "La ebullición ocurre en todo el líquido y la evaporación del charco en su superficie", "No hay diferencia", "El charco hierve", "Hay diferencias: dónde ocurre el cambio y cuánta energía necesita."),
        ("ab", "¿Qué estructura tiene una buena explicación?", "Cambio observado, dirección del calor y condiciones que influyen", "Solo una opinión", "La explicación científica describe causa y evidencia."),
    ],
    ctx=("abc", "En una feria venden hielo en bolsas. Un vendedor dice que dejar las bolsas bajo un toldo las mantiene más tiempo. ¿Qué explicación científica corresponde?", "A la sombra el hielo recibe menos calor y se derrite más despacio", "El toldo pone hielo nuevo", "El sol enfría el hielo", "Menos calor recibido hace más lenta la fusión."),
    sc=[("En Ciencias: ¿qué hace que la ropa se seque más rápido?", "Más calor, más viento y más superficie expuesta", "Esos factores aceleran la evaporación del agua de la ropa."),
        ("¿Qué cambio explica las gotas en un vaso frío?", "La condensación del vapor del aire", "El vapor pierde calor al tocar el vaso."),
        ("¿Qué debe decir una buena explicación?", "El cambio, el calor que gana o pierde y las condiciones", "Así se apoya en causa y evidencia.")],
    op=("Elige una situación de la ficha o una propia (secar ropa, un charco, hielo en una hielera, vidrios empañados). Escribe una explicación de cuatro líneas con esta estructura: qué observas, qué cambio del agua ocurre, si gana o pierde calor y qué condiciones influyen.",
        "Observo vidrios empañados en la cocina. El vapor se condensa al tocar el vidrio frío. Pierde calor. Influye la diferencia de temperatura.",
        ["nombra el cambio de estado", "dice si gana o pierde calor", "menciona una condición"],
        ["cuatro líneas escritas"],
        ["omitir la dirección del calor", "dar una opinión sin causa"],
        "Pregunta: «¿Qué dato apoya tu explicación?»."),
    reinforce="Elige una situación de tu casa con agua y escribe una explicación en dos líneas.",
    extend="Explica por qué se seca antes la ropa extendida que la doblada.",
)

# ============================================================ clase 6
F = ("Ficha 6 (informe de ejemplo). Pregunta: ¿el agua de un vaso al sol se evapora más rápido que la de un vaso a la sombra? "
     "Predicción: el vaso al sol perderá más agua. Condiciones iguales: vasos idénticos, 30 mm de agua en cada uno, mismo día. "
     "Resultados al final del día: vaso al sol, 24 mm de agua; vaso a la sombra, 28 mm de agua.")
build(
    O, 6, F,
    use="Hoy reviso mi explicación comparando predicciones y resultados, y decido qué mejorar.",
    prior=PRIOR + ["Sé explicar cambios del agua con temperatura y calor."],
    explain=[
        "Una predicción es lo que esperas que ocurra antes de mirar los resultados. Cuando tienes los datos, los comparas con la predicción: si coinciden, la explicación se apoya; si no, hay que revisar la explicación o el procedimiento.",
        "Para que la comparación sea justa, solo debe cambiar una condición a la vez. En la ficha, solo cambia el lugar: sol o sombra. Si además cambiaran el tamaño de los vasos o la cantidad de agua, no se sabría cuál condición produjo la diferencia.",
        "Una conclusión se escribe con tres partes: lo que se midió, si se cumplió la predicción y qué explicación se propone. Si hay dudas, se nombra qué mejorar: repetir la medición, usar más vasos o anotar la hora.",
    ],
    vocab=[("predicción", "lo que esperas que ocurra antes de medir"), ("resultado", "dato obtenido al medir"), ("condición controlada", "algo que se mantiene igual para comparar bien"), ("conclusión", "lo que se puede afirmar con los datos")],
    worked=[
        ("Comparar predicción y resultado", F, ["La predicción dice que el vaso al sol pierde más agua.", "Al sol quedaron 24 mm de 30 y a la sombra 28 mm de 30."], "Al sol perdió 6 mm y a la sombra 2 mm: la predicción se cumplió"),
        ("Detectar un problema", "Otro informe compara un vaso ancho al sol con un vaso angosto a la sombra.", ["Cambian el lugar y el tamaño del vaso.", "No se sabe cuál condición causó la diferencia."], "La comparación no es justa: cambió más de una condición"),
    ],
    mistakes=[("Cambiar varias condiciones a la vez y concluir igual.", "Así no se sabe cuál produjo el resultado.", "Cambia una sola condición y controla las demás."),
              ("Decir que la predicción se cumplió sin mirar los números.", "La comparación debe apoyarse en los datos medidos.", "Calcula cuánto cambió cada medición y compara.")],
    T=[
        ("abc", "{F} ¿Qué predijo el informe?", "Que el vaso al sol perdería más agua", "Que el vaso a la sombra perdería más agua", "Que los dos perderían igual", "La predicción está escrita después de la pregunta."),
        ("ab", "{F} ¿Qué condición cambia en el informe?", "El lugar: sol o sombra", "La cantidad de agua", "Los vasos y el agua son iguales; solo cambia dónde están."),
        ("=", "{F} ¿Cuántos milímetros perdió el vaso al sol?", "30-24", "Se resta el nivel final al nivel inicial.", " mm"),
        ("=", "{F} ¿Cuántos milímetros perdió el vaso a la sombra?", "30-28", "Se resta el nivel final al inicial.", " mm"),
        ("abc", "{F} ¿Se cumplió la predicción?", "Sí, porque el vaso al sol perdió más", "No, porque el de la sombra perdió más", "No se puede saber", "Perdió 6 mm contra 2 mm."),
        ("ab", "¿Por qué el vaso al sol pierde más agua?", "Porque gana más calor y se evapora más rápido", "Porque el sol lo llena", "Más calor acelera la evaporación del agua."),
        ("=", "{F} ¿Cuántos milímetros más perdió el vaso al sol que el de la sombra?", "6-2", "Se compara lo perdido en cada vaso.", " mm"),
        ("abc", "{F} Si el vaso al sol fuera más ancho que el de la sombra, ¿qué problema habría?", "No se sabría si la diferencia viene del sol o del ancho", "Ninguno", "Se perdería menos agua", "Cambiarían dos condiciones a la vez."),
        ("abc", "{F} ¿Cuál es una conclusión apoyada en los datos?", "El vaso al sol perdió más agua, lo que coincide con la predicción", "El sol siempre hace evaporar todo", "Los vasos no sirven", "La conclusión se limita a lo que muestran los datos."),
        ("ab", "Un informe dice que «siempre» pasa lo mismo con un solo día de datos. ¿Qué corresponde?", "Aclarar que con un día no se puede asegurar y repetir la medición", "Aceptarlo", "Con pocos datos no se puede asegurar que ocurra siempre."),
        ("abc", "{F} Una persona propone mejorar el informe. ¿Qué mejora es adecuada?", "Repetir el día siguiente y anotar la hora de cada medición", "Cambiar el vaso cada vez", "Quitar el vaso de la sombra", "Repetir y registrar la hora permite comprobar."),
        ("abc", "Se obtuvo un resultado distinto de la predicción. ¿Qué se debe hacer?", "Revisar el procedimiento y la explicación, sin ocultar el resultado", "Cambiar los datos", "Olvidar el informe", "Un resultado distinto ayuda a mejorar la explicación."),
        ("ab", "¿Qué debe tener una conclusión?", "Lo medido, si se cumplió la predicción y una explicación", "Solo una opinión", "Los tres elementos hacen clara la conclusión."),
    ],
    ctx=("abc", "Un grupo de vecinos de ejemplo quiere saber si la ropa se seca antes con viento. Cuelgan una polera al viento y otra, de otra tela, dentro de una pieza sin corriente. ¿Qué problema tiene el plan?", "Cambian el viento y la tela: no se sabe cuál influye", "No tiene ningún problema", "El viento no existe", "Para comparar bien debe cambiar solo una condición a la vez."),
    sc=[("En Ciencias: ¿qué es una predicción?", "Lo que esperas que ocurra antes de medir", "Se compara después con los resultados."),
        ("¿Por qué cambiar una sola condición a la vez?", "Para saber cuál produjo el resultado", "Si cambian varias, no se puede concluir."),
        ("¿Qué hago si el resultado no coincide con la predicción?", "Revisar la explicación y el procedimiento", "Un resultado distinto sirve para aprender y mejorar la explicación.")],
    op=("Plantea un informe breve de ejemplo con esta pregunta: ¿se derrite antes un cubo de hielo en agua tibia o en agua fría? Escribe tu predicción, qué condiciones mantendrías iguales, qué resultados esperas y cómo los usarías para concluir.",
        "Predicción: se derrite antes en agua tibia. Igual: tamaño del cubo y cantidad de agua. Resultado esperado: menos minutos en agua tibia. Conclusión: la tibia entrega más calor.",
        ["hace una predicción", "controla las demás condiciones", "explica con calor y temperatura"],
        ["cuatro líneas escritas"],
        ["cambiar dos condiciones a la vez", "no explicar con calor"],
        "Pregunta: «¿Qué dato te haría cambiar de opinión?»."),
    reinforce="Elige una situación del hogar con agua y escribe una predicción y cómo la comprobarías en papel.",
    extend="Explica cómo aclararías con más datos una conclusión hecha con un solo día de medición.",
)
