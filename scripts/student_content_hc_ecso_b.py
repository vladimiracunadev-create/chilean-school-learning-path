"""Economía y sociedad (electivo HC, 3.º y 4.º medio): OAC-03 (mercado: oferta, demanda, elasticidad, inflación, precios y rol del Estado) y OAC-05 (imperfecciones del mercado), clases 1 a 5 de cada uno. Cifras de ejemplo, ficticias."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel o cuaderno y, si quieres, una calculadora simple. No se necesita computador ni internet: cada tabla, caso y dato está escrito en el enunciado. "
             "Los mercados, empresas, precios y cantidades son ficticios o «de ejemplo»: sirven para practicar el razonamiento económico, no para aprender cifras reales. "
             "Este cuaderno no entrega asesoría financiera ni recomienda inversiones; presenta modelos y posturas con sus argumentos para que los analices. "
             "El dinero está en pesos chilenos.")
build = make_build(MATERIALS)

O3 = "HI-ECSO-3y4-OAC-03"
O5 = "HI-ECSO-3y4-OAC-05"

# ============================================================ OAC-03, clase 1
F = ("Ficha 11 (mercado de ejemplo, ficticio). Empanadas en una feria de barrio, por día. Precio en pesos → cantidad demandada / cantidad ofrecida: "
     "$1.000 → 100 / 20; $1.500 → 80 / 40; $2.000 → 60 / 60; $2.500 → 40 / 80; $3.000 → 20 / 100.")
build(
    O3, 1, F,
    use="Aprenderé qué son la demanda y la oferta, qué dicen sus leyes y cómo se distingue un cambio de precio de un cambio en los factores que desplazan una curva.",
    prior=["Sé qué es un incentivo y cómo reacciona un agente al precio.", "Sé leer una tabla de precios y cantidades.", "Conozco los agentes económicos: familias, empresas y Estado."],
    explain=[
        "Un mercado es el lugar, físico o virtual, donde se encuentran quienes compran y quienes venden. La demanda muestra las cantidades que los consumidores están dispuestos a comprar a cada precio. La ley de la demanda dice que, si lo demás no cambia, cuando sube el precio baja la cantidad demandada, y cuando baja el precio sube la cantidad demandada.",
        "La oferta muestra las cantidades que los productores están dispuestos a vender a cada precio. La ley de la oferta dice que, si lo demás no cambia, cuando sube el precio sube la cantidad ofrecida, porque vender más resulta más rentable. En una tabla estas cantidades se leen por fila; en un gráfico forman la curva de demanda (con pendiente hacia abajo) y la curva de oferta (con pendiente hacia arriba).",
        "Hay que distinguir dos cosas. Si cambia el precio del propio bien, hay un movimiento a lo largo de la curva: cambia la cantidad demandada u ofrecida. Si cambia otro factor, toda la curva se desplaza. En la demanda influyen el ingreso de las personas, los gustos, el número de compradores y el precio de bienes sustitutos (los que cumplen una función parecida, como el pan y las tortillas). En la oferta influyen el costo de los insumos, la tecnología y el número de productores.",
    ],
    vocab=[("mercado", "lugar donde se encuentran compradores y vendedores"), ("demanda", "cantidades que los consumidores quieren comprar a cada precio"), ("oferta", "cantidades que los productores quieren vender a cada precio"), ("bien sustituto", "bien que cumple una función parecida a otro"), ("desplazamiento de la curva", "cambio de toda la demanda u oferta por un factor distinto al precio"), ("insumo", "material o servicio que se usa para producir")],
    worked=[
        ("Leer la ley de la demanda", "En un kiosco de ejemplo, a $800 se demandan 50 bebidas, a $1.000 se demandan 40 y a $1.200 se demandan 30. ¿Se cumple la ley de la demanda?",
         ["Observa cómo cambia la cantidad cuando sube el precio: 50, 40, 30.", "La cantidad demandada baja al subir el precio, que es lo que dice la ley."],
         "Sí, se cumple"),
        ("Movimiento o desplazamiento", "En un barrio llegan muchas familias nuevas y se compra más pan a todos los precios. ¿Es un movimiento a lo largo de la curva o un desplazamiento?",
         ["Cambió el número de compradores, no el precio del pan.", "Cuando cambia un factor distinto al precio, toda la curva se desplaza: aumenta la demanda."],
         "Desplazamiento de la demanda hacia la derecha (aumenta)"),
    ],
    mistakes=[("Confundir «cantidad demandada» con «demanda».", "Se mezcla un punto de la tabla con la tabla completa.", "La cantidad cambia con el precio; la demanda cambia cuando se mueve otro factor."),
              ("Pensar que la oferta sube cuando sube la demanda.", "Se mezclan los dos lados del mercado.", "Cada lado tiene sus propios factores, aunque se afecten por el precio.")],
    T=[
        ("{F} ¿Cuántas empanadas se demandan al precio de $1.500?", "80", "Se lee la fila de $1.500 en la columna de cantidad demandada."),
        ("{F} ¿Cuántas empanadas se ofrecen al precio de $2.500?", "80", "Se lee la fila de $2.500 en la columna de cantidad ofrecida."),
        ("abc", "En Economía y sociedad: ¿qué dice la ley de la demanda?", "Si sube el precio, baja la cantidad demandada, lo demás constante", "Si sube el precio, sube la cantidad demandada", "El precio no afecta la cantidad demandada", "La relación entre precio y cantidad demandada es inversa, con lo demás constante."),
        ("abc", "{F} ¿Cómo cambia la cantidad ofrecida al subir el precio de $1.000 a $3.000?", "Aumenta de 20 a 100", "Disminuye de 100 a 20", "No cambia", "Con precios más altos los productores quieren vender más."),
        ("En Economía y sociedad: ¿qué es la oferta?", "Las cantidades que los productores quieren vender a cada precio", "La oferta es la relación entre el precio y lo que los productores están dispuestos a vender."),
        ("=", "{F} ¿Cuántas empanadas más se demandan a $1.000 que a $3.000?", "100-20", "Se restan las cantidades demandadas de las dos filas."),
        ("{F} Al precio de $1.000, ¿hay más cantidad demandada o más ofrecida y por cuánto?", "Más demandada, por 80", "Se demandan 100 y se ofrecen 20, así que la diferencia es 80."),
        ("abc", "Las familias de un barrio reciben más ingresos y compran más empanadas a cualquier precio. ¿Qué ocurre en el mercado de empanadas?", "La demanda se desplaza hacia la derecha (aumenta)", "Hay un movimiento a lo largo de la curva de demanda", "La oferta disminuye", "El ingreso es un factor distinto al precio y desplaza toda la curva de demanda."),
        ("abc", "El aceite para freír sube de precio y cada empanada cuesta más producir. ¿Qué ocurre con la oferta de empanadas?", "Disminuye (se desplaza hacia la izquierda)", "Aumenta", "No se ve afectada", "Un insumo más caro eleva el costo y se ofrece menos a cada precio."),
        ("{F} Un estudiante dice: «Al subir el precio de $2.000 a $2.500, la demanda bajó de 60 a 40». ¿Qué término correcto corregiría?", "Bajó la cantidad demandada, no la demanda", "Solo cambió el precio, por lo que hay un movimiento a lo largo de la curva y no un desplazamiento."),
        ("abc", "Sube el precio de las sopaipillas, que son sustitutas de las empanadas. Ceteris paribus, ¿qué ocurre con la demanda de empanadas?", "Aumenta, porque algunos compradores cambian de bien", "Disminuye, porque suben todos los precios", "Disminuye, porque las empanadas se vuelven más baratas que las sopaipillas", "Si un sustituto se encarece, parte de los consumidores se pasa al otro bien."),
        ("=", "{F} Llegan turistas y la demanda aumenta en 40 empanadas a cada precio. ¿Cuántas se demandarían ahora a $2.000?", "60+40", "A la cantidad original de $2.000 se le suma el aumento."),
        ("abc", "{F} Con ese aumento de 40 a cada precio, ¿a qué precio de la tabla coinciden la cantidad demandada y la ofrecida?", "$2.500", "$2.000", "$1.500", "Con el aumento se demandan 80 a $2.500, igual a las 80 ofrecidas."),
    ],
    ctx=("abc", "Una panadería de ejemplo incorpora una máquina que le permite hacer más pan con el mismo costo. ¿Qué ocurre con la oferta de pan de esa panadería?", "Aumenta, es decir, se desplaza hacia la derecha", "Disminuye", "Se mantiene igual, porque el precio no cambió", "La tecnología es un factor que desplaza la oferta cuando permite producir más con el mismo costo."),
    sc=[
        ("En Economía y sociedad: ¿qué dice la ley de la oferta?", "Si sube el precio, sube la cantidad ofrecida, lo demás constante", "Vender más a mejor precio resulta más rentable."),
        ("¿Qué diferencia hay entre un movimiento a lo largo de la curva y un desplazamiento?", "El movimiento lo causa el precio del bien y el desplazamiento otro factor", "Distinguirlos evita confundir cantidad con demanda."),
        ("Nombra dos factores que desplazan la demanda.", "Ingreso, gustos, número de compradores o precio de un sustituto", "Son factores distintos al precio del propio bien."),
    ],
    op=("Elige uno de estos mercados de ejemplo y describe qué ocurre. Mercado 1: entradas a un concierto local, donde la banda se hace muy popular. Mercado 2: tomates, donde una lluvia fuerte daña parte de las cosechas. "
        "Escribe: (1) si cambia la demanda o la oferta; (2) hacia dónde se desplaza; (3) el factor que lo causa; (4) qué pasa con la cantidad demandada u ofrecida si, además, cambiara el precio.",
        "Mercado 2. Cambia la oferta; se desplaza hacia la izquierda (disminuye); factor: la lluvia daña la cosecha y baja la cantidad producida. Si además sube el precio, la cantidad demandada baja por la ley de la demanda.",
        ["identifica correctamente demanda u oferta", "indica el sentido del desplazamiento", "nombra el factor causal", "distingue cantidad de curva"],
        ["cuatro frases numeradas"],
        ["decir que sube la oferta cuando sube la demanda", "confundir cantidad ofrecida con oferta", "usar un factor que no desplaza la curva"],
        "Pregunta: «¿cambió el precio del propio bien o cambió otro factor?». Con eso decide movimiento o desplazamiento."),
    reinforce="Con la Ficha 11, escribe cuántas empanadas se demandan y se ofrecen a $3.000 y a $1.500, y una frase que resuma lo que ves.",
    extend="Explica con un ejemplo de tu barrio cómo un cambio en los gustos desplaza la demanda de un producto.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 12 (mercado de ejemplo, ficticio). Tomates en una feria, kilos por día. Precio por kilo → cantidad demandada / cantidad ofrecida: "
     "$600 → 90 / 10; $800 → 70 / 30; $1.000 → 50 / 50; $1.200 → 30 / 70; $1.400 → 10 / 90.")
build(
    O3, 2, F,
    use="Aprenderé a hallar el equilibrio de un mercado, a distinguir excedentes y faltantes y a analizar cómo cambia el equilibrio cuando se desplaza la oferta o la demanda.",
    prior=["Conozco la ley de la demanda y de la oferta.", "Distingo movimiento y desplazamiento de curva.", "Sé leer una tabla de demanda y oferta."],
    explain=[
        "El equilibrio de mercado es la situación en que la cantidad demandada es igual a la cantidad ofrecida. El precio en que ocurre se llama precio de equilibrio, y la cantidad correspondiente, cantidad de equilibrio. A ese precio, todo lo que los compradores quieren comprar coincide con lo que los productores quieren vender.",
        "Si el precio está por encima del de equilibrio, se ofrece más de lo que se demanda: hay un excedente, y los vendedores tienden a bajar el precio para vender. Si el precio está por debajo del de equilibrio, se demanda más de lo que se ofrece: hay un faltante, y los compradores compiten, por lo que el precio tiende a subir. Así el mercado se ajusta, aunque a veces lo hace lentamente.",
        "Cuando se desplaza la demanda o la oferta cambia el equilibrio. Si aumenta la demanda y la oferta no cambia, suben el precio y la cantidad de equilibrio. Si disminuye la oferta y la demanda no cambia, sube el precio y baja la cantidad. Es importante entender que el precio de equilibrio no es «el precio justo»: describe dónde coinciden las decisiones de compradores y vendedores, no si ese resultado es bueno o equitativo.",
    ],
    vocab=[("equilibrio de mercado", "situación en que cantidad demandada y ofrecida coinciden"), ("precio de equilibrio", "precio en que coinciden demanda y oferta"), ("excedente", "cantidad ofrecida mayor que la demandada"), ("faltante", "cantidad demandada mayor que la ofrecida"), ("ajuste del mercado", "movimiento del precio hacia el equilibrio"), ("shock", "cambio brusco que desplaza la oferta o la demanda")],
    worked=[
        ("Encontrar el equilibrio", "Mercado de ejemplo: a $300 se demandan 80 y se ofrecen 20; a $400, 60 y 40; a $500, 50 y 50; a $600, 30 y 70. ¿Cuál es el precio de equilibrio?",
         ["Busca la fila donde la cantidad demandada es igual a la ofrecida.", "Eso ocurre a $500, con 50 unidades."],
         "$500 y 50 unidades"),
        ("Distinguir faltante y excedente", "En el mismo mercado, el precio está en $300. ¿Hay excedente o faltante y de cuánto?",
         ["A $300 se demandan 80 y se ofrecen 20.", "Se demanda más de lo que se ofrece: es un faltante de 60 unidades."],
         "Faltante de 60 unidades"),
    ],
    mistakes=[("Pensar que el precio de equilibrio es el precio justo.", "Se mezcla un resultado del mercado con un juicio de valor.", "El equilibrio describe dónde coinciden las decisiones, no si es justo."),
              ("Confundir excedente con faltante.", "Se invierte qué cantidad es mayor.", "Excedente: se ofrece más de lo demandado. Faltante: se demanda más de lo ofrecido.")],
    T=[
        ("abc", "{F} ¿Cuál es el precio de equilibrio del mercado de tomates?", "$1.000", "$600", "$1.400", "A $1.000 se demandan y se ofrecen 50 kilos."),
        ("=", "{F} A $1.400, ¿cuántos kilos de excedente hay?", "90-10", "Se resta la cantidad demandada a la ofrecida."),
        ("abc", "En Economía y sociedad: ¿qué es el precio de equilibrio?", "El precio en que coinciden la cantidad demandada y la ofrecida", "El precio más bajo posible", "El precio que fija el Estado", "El equilibrio es el punto donde las decisiones de compradores y vendedores coinciden."),
        ("abc", "{F} A $600, ¿hay excedente o faltante?", "Faltante, porque se demandan 90 y se ofrecen 10", "Excedente, porque se ofrecen 90", "Ninguno, porque está en equilibrio", "La cantidad demandada es mayor que la ofrecida."),
        ("=", "{F} A $600, ¿cuántos kilos faltan?", "90-10", "Se resta la cantidad ofrecida a la demandada."),
        ("abc", "{F} A $1.200 hay excedente de 40 kilos. ¿Qué tiende a ocurrir con el precio?", "Tiende a bajar", "Tiende a subir", "Se mantiene fijo", "Los vendedores con exceso bajan el precio para vender."),
        ("{F} La demanda aumenta en 40 kilos a cada precio. ¿Cuál es el nuevo precio de equilibrio?", "$1.200", "La demanda pasa a 130, 110, 90, 70 y 50, y a $1.200 coincide con los 70 ofrecidos."),
        ("{F} Con ese aumento de la demanda, ¿cuál es la nueva cantidad de equilibrio?", "70 kilos", "A $1.200 la cantidad demandada y la ofrecida son 70."),
        ("abc", "{F} Con el aumento de la demanda en 40 kilos, ¿qué ocurre con el precio de equilibrio respecto de $1.000?", "Sube", "Baja", "No cambia", "Con más demanda, el faltante empuja el precio hacia arriba."),
        ("{F} Un productor dice: «Si fijo $1.400 por kilo, venderé más porque gano más por kilo». Con la tabla, ¿qué ocurre?", "Vende solo 10 kilos, porque la demanda a ese precio es muy baja", "A $1.400 se demandan 10 kilos y se ofrecen 90, de modo que queda un excedente."),
        ("abc", "{F} Una helada reduce en 40 kilos la oferta a cada precio (a $600 y $800 no se ofrece nada). ¿Cuál es el nuevo precio de equilibrio?", "$1.200", "$1.000", "$1.400", "La oferta queda en 0, 0, 10, 30 y 50, y a $1.200 coincide con los 30 demandados."),
        ("{F} Ocurren a la vez el aumento de demanda de 40 kilos y la helada que reduce la oferta en 40 kilos. ¿Cuál es el nuevo precio de equilibrio?", "$1.400", "La demanda será 130, 110, 90, 70 y 50 y la oferta 0, 0, 10, 30 y 50: coinciden a $1.400 con 50 kilos."),
        ("{F} La demanda y la oferta aumentan a la vez en 40 kilos a cada precio. ¿Qué ocurre con el precio y la cantidad de equilibrio?", "El precio sigue en $1.000 y la cantidad sube a 90", "Ambos desplazamientos coinciden a $1.000, donde se demandan y ofrecen 90."),
    ],
    ctx=("abc", "Al final del día, un puesto de lechugas de ejemplo tiene muchas lechugas sin vender al precio de $500. Una feriante nota que otros puestos las venden a $400 y se acaban. ¿Qué es lo más probable que ocurra?", "Bajará el precio para eliminar el excedente", "Subirá el precio para ganar más", "No cambiará nada, porque el precio es fijo", "El excedente presiona los precios hacia abajo en un mercado competitivo."),
    sc=[
        ("En Economía y sociedad: ¿qué es un excedente?", "Que se ofrece más cantidad de la que se demanda", "Ocurre cuando el precio está sobre el de equilibrio."),
        ("¿Qué es un faltante?", "Que se demanda más cantidad de la que se ofrece", "Ocurre cuando el precio está bajo el de equilibrio."),
        ("¿Es el precio de equilibrio un «precio justo»?", "No: describe la coincidencia de decisiones, sin juzgarla", "Su valoración como justo o no es un juicio normativo."),
    ],
    op=("Analiza este mercado de ejemplo de bicicletas usadas en una comuna: precio $60.000 → demanda 100 / oferta 20; $80.000 → 80 / 40; $100.000 → 60 / 60; $120.000 → 40 / 80; $140.000 → 20 / 100. "
        "Escribe: (1) el precio y cantidad de equilibrio; (2) si hay excedente o faltante a $80.000 y de cuánto; (3) el nuevo equilibrio si la demanda aumenta en 40 a cada precio (la oferta no cambia); (4) una frase sobre por qué no se puede decir que el equilibrio es justo.",
        "(1) $100.000 y 60 bicicletas. (2) A $80.000 hay faltante de 40 (80 menos 40). (3) Con +40 la demanda es 140, 120, 100, 80 y 60: coincide con la oferta a $120.000 con 80. (4) El equilibrio describe coincidencia de decisiones, no si es justo.",
        ["calcula correctamente excedente o faltante", "identifica filas donde coinciden cantidades", "explica el cambio del equilibrio con un desplazamiento"],
        ["respuestas numeradas con cálculos"],
        ["confundir excedente y faltante", "olvidar sumar el aumento a cada fila", "decir que el equilibrio es justo"],
        "Pregunta: «¿en qué fila se igualan las dos columnas?». Si no hay ninguna, explica que el precio estaría entre dos filas."),
    reinforce="Con la tabla de tomates, escribe el excedente o faltante a cada uno de los cinco precios.",
    extend="Explica por qué dos personas pueden aceptar que el equilibrio es $1.000 y discrepar sobre si ese precio es justo para los consumidores de menores ingresos.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 13 (casos de ejemplo, ficticios). Caso 1, entradas de cine: el precio sube de $4.000 a $4.400 y la cantidad vendida baja de 200 a 150 por semana. "
     "Caso 2, pan: el precio sube de $2.000 a $2.200 el kilo y la cantidad vendida baja de 1.000 a 980 kilos por día. "
     "Caso 3, un producto de aseo: el precio sube de $1.000 a $1.100 y la cantidad baja de 500 a 450 unidades.")
build(
    O3, 3, F,
    use="Aprenderé a calcular y a interpretar la elasticidad precio de la demanda, para anticipar cómo reaccionan los consumidores a un cambio de precio y qué pasa con el gasto total.",
    prior=["Conozco la ley de la demanda.", "Sé calcular un cambio porcentual.", "Sé multiplicar precio por cantidad."],
    explain=[
        "La elasticidad precio de la demanda mide qué tan sensible es la cantidad demandada frente a un cambio en el precio. Se calcula dividiendo el cambio porcentual de la cantidad por el cambio porcentual del precio, y se usa el valor positivo. Para el cambio porcentual se hace (valor nuevo menos valor antiguo) dividido por el valor antiguo y multiplicado por 100.",
        "Si la elasticidad es mayor que 1, la demanda es elástica: la cantidad cambia proporcionalmente más que el precio. Si es menor que 1, es inelástica: la cantidad cambia poco. Si es igual a 1, es de elasticidad unitaria. Los bienes con muchos sustitutos cercanos o que no son necesarios suelen tener demanda más elástica; los necesarios o sin sustitutos, más inelástica.",
        "La elasticidad sirve para anticipar el gasto total de los consumidores (precio por cantidad). Con demanda elástica, subir el precio reduce el gasto total, porque la cantidad cae más de lo que sube el precio. Con demanda inelástica, subir el precio aumenta el gasto total. Estas son regularidades de un modelo con datos acotados, no leyes exactas: el resultado depende de cada mercado y del período considerado.",
    ],
    vocab=[("elasticidad precio de la demanda", "sensibilidad de la cantidad demandada frente al precio"), ("demanda elástica", "elasticidad mayor que 1"), ("demanda inelástica", "elasticidad menor que 1"), ("elasticidad unitaria", "elasticidad igual a 1"), ("cambio porcentual", "variación dividida por el valor antiguo y multiplicada por 100"), ("gasto total", "precio multiplicado por cantidad")],
    worked=[
        ("Calcular una elasticidad", "Un helado de ejemplo sube de $1.000 a $1.200 (20%) y la cantidad baja de 300 a 270 unidades (10%). ¿Cuál es la elasticidad y cómo es la demanda?",
         ["Elasticidad = 10 dividido por 20, que da 0,5.", "Como 0,5 es menor que 1, la demanda es inelástica."],
         "0,5; demanda inelástica"),
        ("Gasto total", "Un jugo de ejemplo sube de $500 a $600 y se venden 400 unidades antes y 300 después. ¿Qué pasó con el gasto total?",
         ["Antes: 500 por 400 son 200.000. Después: 600 por 300 son 180.000.", "El gasto total bajó, lo que es consistente con una demanda elástica."],
         "Bajó de 200.000 a 180.000"),
    ],
    mistakes=[("Calcular el cambio porcentual dividiendo por el valor nuevo.", "Se olvida que el cambio se mide respecto del valor antiguo.", "Divide siempre por el valor de partida."),
              ("Creer que «inelástica» significa que la cantidad no cambia nada.", "Se confunde poco con nada.", "Inelástica significa que la cantidad cambia proporcionalmente menos que el precio.")],
    T=[
        ("=", "{F} Caso 1: ¿cuál es el cambio porcentual del precio de la entrada?", "(4400-4000)/4000*100", "Se divide el aumento por el precio antiguo y se multiplica por 100."),
        ("=", "{F} Caso 1: ¿en qué porcentaje bajó la cantidad de entradas vendidas?", "(200-150)/200*100", "Se divide la baja por la cantidad antigua y se multiplica por 100."),
        ("abc", "En Economía y sociedad: ¿qué mide la elasticidad precio de la demanda?", "Qué tan sensible es la cantidad demandada a un cambio de precio", "Qué tan alto es un precio", "Cuánto cuesta producir una unidad", "Compara el cambio de la cantidad con el cambio del precio."),
        ("=", "{F} Caso 1: ¿cuál es la elasticidad (cambio porcentual de la cantidad dividido por el del precio)?", "25/10", "Se divide 25 por 10."),
        ("abc", "{F} Caso 1: ¿cómo es la demanda de entradas?", "Elástica, porque la elasticidad es mayor que 1", "Inelástica, porque es menor que 1", "Unitaria, porque es igual a 1", "Con 2,5 la cantidad cambia más que el precio."),
        ("abc", "{F} Caso 2: el precio subió 10% y la cantidad bajó 2%. ¿Cómo es la demanda de pan?", "Inelástica", "Elástica", "Unitaria", "La elasticidad es 0,2, que es menor que 1."),
        ("=", "{F} Caso 2: ¿cuál es la elasticidad del pan?", "2/10", "Se divide el cambio porcentual de la cantidad por el del precio."),
        ("=", "{F} Caso 1: ¿cuánto es el gasto total semanal en entradas después de subir el precio?", "4400*150", "El gasto total es el precio por la cantidad."),
        ("abc", "{F} Caso 2: ¿qué pasó con el gasto total en pan?", "Aumentó, porque con demanda inelástica subir el precio sube el gasto", "Disminuyó, porque la cantidad bajó", "Se mantuvo exactamente igual", "Antes era 2.000.000 y después 2.156.000."),
        ("abc", "{F} Caso 3: ¿cuál es la elasticidad del producto de aseo?", "1", "0,1", "10", "El precio sube 10% y la cantidad baja 10%."),
        ("abc", "Un empresario de ejemplo dice: «Subiré el precio del pan y ganaré más dinero». ¿Cuándo es más probable que tenga razón?", "Cuando la demanda del pan es inelástica", "Cuando la demanda del pan es muy elástica", "Cuando la demanda tiene elasticidad unitaria", "Con demanda inelástica la cantidad cae poco y el gasto total sube."),
        ("abc", "¿Cuál de estos factores haría más elástica la demanda de una marca de bebida?", "Que existan muchas marcas parecidas a menor precio", "Que sea el único producto disponible", "Que sea un bien necesario sin reemplazo", "Con sustitutos cercanos, los consumidores cambian fácilmente de marca."),
        ("{F} Un municipio propone subir el precio de las entradas de un cine municipal para aumentar lo que recibe. Con la elasticidad del Caso 1, ¿qué advertencia haría un economista?", "Como la demanda es elástica, la cantidad cae más que el precio sube y el gasto total podría bajar", "Con elasticidad mayor que 1 el efecto sobre el gasto es contrario al esperado."),
    ],
    ctx=("abc", "Un servicio de colectivos de ejemplo sube la tarifa de $600 a $660 y los pasajeros bajan de 100 a 98 por viaje. Muchos no tienen otra forma de llegar al trabajo. ¿Qué conclusión es correcta?", "La demanda es inelástica: el precio sube 10% y la cantidad solo 2%", "La demanda es elástica porque la cantidad bajó", "La demanda es unitaria", "La elasticidad es 2 dividido por 10, o sea 0,2."),
    sc=[
        ("¿Cómo se calcula un cambio porcentual?", "Se divide la variación por el valor antiguo y se multiplica por 100", "Mide el cambio relativo al punto de partida."),
        ("¿Qué indica una elasticidad menor que 1?", "Que la demanda es inelástica", "La cantidad cambia proporcionalmente menos que el precio."),
        ("Con demanda inelástica, ¿qué pasa con el gasto total si sube el precio?", "Aumenta", "La cantidad cae poco, de modo que el mayor precio domina."),
    ],
    op=("Resuelve uno de estos casos de ejemplo. Caso 1: el precio de un pasaje sube de $800 a $880 y los viajes bajan de 1.000 a 800 por día. Caso 2: el precio de un cuaderno sube de $2.000 a $2.200 y las ventas bajan de 500 a 490 por semana. "
        "Calcula los dos cambios porcentuales, la elasticidad, clasifica la demanda, calcula el gasto total antes y después, y escribe una conclusión que no recomiende ninguna política.",
        "Caso 2. Precio +10%; cantidad -2%; elasticidad 0,2: inelástica. Gasto antes 2.000 por 500 = 1.000.000; después 2.200 por 490 = 1.078.000. Subió. Conclusión: con esta demanda inelástica, el aumento de precio aumenta el gasto total.",
        ["calcula los cambios porcentuales con el valor antiguo en el denominador", "obtiene y clasifica la elasticidad", "calcula el gasto total antes y después", "formula una conclusión sin recomendar una política"],
        ["tabla de cálculos y una conclusión de dos oraciones"],
        ["dividir por el valor nuevo", "invertir el cociente de la elasticidad", "recomendar una política en lugar de describir el efecto"],
        "Pregunta: «¿respecto de qué valor mides el cambio?». Si responde con el valor nuevo, pídele rehacerlo."),
    reinforce="Con el Caso 3 de la ficha, calcula el gasto total antes y después y compara.",
    extend="Explica por qué el mismo producto puede ser más elástico para una familia con poco ingreso que para una con mucho.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 14 (canasta de ejemplo, ficticia). Una canasta con 10 kg de pan, 20 pasajes de bus y 5 docenas de huevos. Precios en el período 1: pan $2.000 el kg, pasaje $700, huevos $3.200 la docena. "
     "Precios en el período 2: pan $2.200 el kg, pasaje $750, huevos $3.600 la docena.")
build(
    O3, 4, F,
    use="Aprenderé qué es la inflación, cómo se mide con una canasta y un índice de precios y por qué importa distinguir ingresos nominales y reales.",
    prior=["Sé calcular un cambio porcentual.", "Sé multiplicar precios por cantidades.", "Conozco la ley de la demanda y de la oferta."],
    explain=[
        "La inflación es el aumento sostenido y generalizado del nivel de precios. «Sostenido» quiere decir que se mantiene en el tiempo, y «generalizado», que afecta a muchos productos, no a uno solo. Se mide con un índice de precios, como el Índice de Precios al Consumidor (IPC), que en Chile calcula el Instituto Nacional de Estadísticas. Compara en el tiempo el costo de una canasta de bienes y servicios que consumen los hogares.",
        "Para medir la inflación se calcula el costo de la canasta en dos períodos y luego el cambio porcentual: (costo nuevo menos costo antiguo) dividido por el costo antiguo, por 100. Un índice con base 100 expresa el costo del período en relación con el período base: si la canasta cuesta 10% más, el índice vale 110. Las canastas son promedios, y cada hogar consume una canasta distinta, por lo que la inflación que siente cada hogar puede diferir.",
        "El ingreso nominal es el que se recibe en pesos de cada período. El ingreso real indica cuánto se puede comprar con él, es decir, el poder adquisitivo. Si el sueldo nominal sube menos que los precios, el poder adquisitivo cae. La inflación tiene costos y quienes la analizan discrepan en sus causas, por ejemplo exceso de demanda, alza de costos o expectativas; aquí se aprende a medirla y a interpretarla, no a elegir una explicación.",
    ],
    vocab=[("inflación", "aumento sostenido y generalizado de los precios"), ("canasta", "conjunto de bienes y servicios que se usa para medir precios"), ("índice de precios", "número que compara el costo de una canasta en el tiempo"), ("ingreso nominal", "ingreso medido en pesos de cada período"), ("ingreso real", "lo que se puede comprar con el ingreso"), ("poder adquisitivo", "capacidad de compra del dinero")],
    worked=[
        ("Costo de una canasta", "Una canasta de ejemplo tiene 4 kg de arroz a $1.500 el kg y 2 litros de aceite a $2.500 el litro. ¿Cuánto cuesta?",
         ["Arroz: 4 por 1.500 son 6.000. Aceite: 2 por 2.500 son 5.000.", "Se suman: 6.000 más 5.000."],
         "$11.000"),
        ("Interpretar ingreso real", "El sueldo de una persona de ejemplo sube 3% y los precios de su canasta suben 6%. ¿Qué pasa con su poder adquisitivo?",
         ["El sueldo nominal sube 3%, pero los precios suben más.", "Puede comprar menos que antes."],
         "Disminuye"),
    ],
    mistakes=[("Llamar inflación a la subida de un solo producto.", "Se olvida que debe ser generalizada y sostenida.", "Mira una canasta amplia y varios períodos."),
              ("Creer que si los precios suben el ingreso real también sube.", "Se confunde nominal con real.", "Compara el aumento del ingreso con el aumento de los precios.")],
    T=[
        ("=", "{F} ¿Cuánto cuesta la canasta en el período 1?", "10*2000+20*700+5*3200", "Se multiplican cantidades por precios y se suman los tres productos."),
        ("=", "{F} ¿Cuánto cuesta la canasta en el período 2?", "10*2200+20*750+5*3600", "Se calcula con los precios del segundo período."),
        ("abc", "En Economía y sociedad: ¿qué es la inflación?", "Un aumento sostenido y generalizado de los precios", "La subida del precio de un producto", "La baja de los precios por una semana", "Debe afectar a muchos productos y mantenerse en el tiempo."),
        ("=", "{F} ¿En qué porcentaje subió el costo de la canasta entre los dos períodos?", "(55000-50000)/50000*100", "Se divide el aumento por el costo antiguo y se multiplica por 100."),
        ("=", "{F} Si el período 1 es la base 100, ¿cuánto vale el índice del período 2?", "55000/50000*100", "El costo nuevo se compara con el costo base."),
        ("abc", "Un índice de precios con base 100 vale 108 un año después. ¿Qué significa?", "Que la canasta cuesta 8% más que en el período base", "Que la canasta cuesta 108 pesos", "Que los precios subieron 100%", "El índice compara el costo de la canasta con el del período base, que vale 100."),
        ("=", "{F} ¿En qué porcentaje subió el precio de los huevos?", "(3600-3200)/3200*100", "Se divide el aumento por el precio antiguo."),
        ("abc", "El sueldo de una persona sube 4% y la inflación es 10%. ¿Qué pasa con su poder adquisitivo?", "Disminuye", "Aumenta", "Se mantiene", "Los precios suben más que su ingreso nominal."),
        ("abc", "Solo suben los precios de las paltas durante una semana. ¿Hay inflación?", "No, porque no es un aumento generalizado ni sostenido", "Sí, porque subió un precio", "Sí, porque es el IPC", "La inflación exige alza de muchos precios mantenida en el tiempo."),
        ("=", "{F} Una persona gana $500.000 y su sueldo sube 10%. ¿Cuánto gana ahora?", "500000*110/100", "Subir 10% equivale a multiplicar por 110 y dividir por 100."),
        ("abc", "Dos hogares: uno gasta casi todo su ingreso en pan y huevos y otro gasta mucho en viajes. Si suben más los alimentos, ¿qué hogar siente más la inflación?", "El que gasta casi todo en alimentos", "El que gasta en viajes", "Los dos lo sienten igual porque pagan los mismos precios", "Cada hogar consume una canasta distinta, y el peso del alimento es mayor en el primero."),
        ("=", "Una canasta de ejemplo cuesta $80.000 y la inflación del período siguiente es 5%. ¿Cuánto costará?", "80000*105/100", "Se aumenta 5% multiplicando por 105 y dividiendo por 100."),
        ("abc", "Un sueldo nominal sube 5% y la inflación es 8%. ¿Qué ocurre con el sueldo real?", "Disminuye", "Aumenta", "No cambia", "El poder de compra cae porque los precios suben más."),
    ],
    ctx=("abc", "Una familia de ejemplo paga $300.000 de arriendo, reajustado cada año según la inflación de 5%. ¿Cuánto pagará el próximo año?", "$315.000", "$305.000", "$350.000", "Se multiplica 300.000 por 105 y se divide por 100."),
    sc=[
        ("En Economía y sociedad: ¿qué es el poder adquisitivo?", "La capacidad de compra del dinero", "Indica cuánto se puede comprar con un ingreso."),
        ("¿Qué diferencia hay entre ingreso nominal y real?", "El nominal está en pesos del período y el real mide lo que se puede comprar", "Se compara el ingreso con los precios."),
        ("¿Por qué la inflación puede sentirse distinta en cada hogar?", "Porque cada hogar consume una canasta distinta", "El IPC es un promedio de una canasta general."),
    ],
    op=("Resuelve un caso de ejemplo. Una canasta con 5 kg de arroz, 10 litros de leche y 4 pasajes. Período 1: arroz $1.200 el kg, leche $1.000 el litro, pasaje $800. Período 2: arroz $1.320, leche $1.050, pasaje $880. "
        "Calcula el costo en cada período, el cambio porcentual, el índice con base 100 y explica qué le pasa a una persona cuyo sueldo sube 5% en ese período. Luego escribe una limitación del IPC.",
        "Costo 1: 6.000 + 10.000 + 3.200 = 19.200. Costo 2: 6.600 + 10.500 + 3.520 = 20.620. Cambio: 1.420 sobre 19.200, cerca de 7,4%. Su sueldo sube 5%, menos que 7,4%, así que su poder adquisitivo cae. Limitación: el IPC es un promedio.",
        ["calcula bien el costo de la canasta", "obtiene el cambio porcentual", "interpreta el ingreso real", "nombra una limitación del índice"],
        ["tabla con cálculos y tres frases"],
        ["calcular el porcentaje sobre el valor nuevo", "confundir nominal con real", "afirmar que el IPC refleja a todos los hogares por igual"],
        "Pregunta: «¿respecto de qué costo calculaste el cambio?». Si usa el nuevo, pídele rehacerlo."),
    reinforce="Elige tres productos de tu casa, anota precios de ejemplo en dos períodos y calcula el cambio porcentual de cada uno.",
    extend="Explica por qué un aumento del salario puede igual dejarte con menos poder de compra, y qué dato necesitarías para saberlo.",
)

# ============================================================ OAC-03, clase 5
F = ("Ficha 15 (mercados de ejemplo, ficticios). Arriendo de piezas para estudiantes en una ciudad universitaria, por mes. Precio → piezas demandadas / ofrecidas: "
     "$200.000 → 500 / 100; $250.000 → 400 / 200; $300.000 → 300 / 300; $350.000 → 200 / 400; $400.000 → 100 / 500. "
     "Mercado de trigo: el precio de equilibrio es $400 el kilo, con 50 toneladas demandadas y ofrecidas; a $500 el kilo se demandan 40 toneladas y se ofrecen 60.")
build(
    O3, 5, F,
    use="Aprenderé cómo el Estado puede intervenir en los precios (máximos y mínimos), qué efectos tienen según el equilibrio y qué argumentos usan quienes los defienden y quienes los critican.",
    prior=["Sé hallar el equilibrio de un mercado.", "Distingo excedente y faltante.", "Distingo afirmaciones positivas y normativas."],
    explain=[
        "El Estado puede intervenir en los mercados de varias formas. Una es fijar un precio máximo, es decir, un tope legal que impide cobrar más. Otra es fijar un precio mínimo, un piso legal que impide cobrar menos. También puede aplicar impuestos, que encarecen un bien, o entregar subsidios, que abaratan su costo para quien compra o produce.",
        "El efecto de un precio fijado depende de dónde se ubique respecto del equilibrio. Un precio máximo por debajo del de equilibrio genera un faltante, porque se demanda más de lo que se ofrece. Un precio mínimo por encima del de equilibrio genera un excedente. Si el máximo está sobre el equilibrio, o el mínimo bajo él, no tiene efecto, porque el mercado ya opera dentro del límite.",
        "Estas medidas se discuten con argumentos distintos. Quienes defienden un tope destacan que protege a quienes compran de precios que consideran abusivos. Quienes lo critican señalan que reduce la cantidad ofrecida y puede generar faltantes o mercados informales. Con un piso, sus defensores destacan la protección de quienes producen, y sus críticos, los excedentes y el costo fiscal (lo que le cuesta al Estado, por ejemplo, comprar lo que sobra). Qué postura es preferible depende de datos y también de valores.",
    ],
    vocab=[("precio máximo", "tope legal para el precio de un bien"), ("precio mínimo", "piso legal para el precio de un bien"), ("impuesto", "pago obligatorio al Estado que encarece un bien"), ("subsidio", "ayuda del Estado que abarata un bien o su producción"), ("regulación", "reglas del Estado que orientan un mercado"), ("mercado informal", "intercambio fuera de las reglas legales")],
    worked=[
        ("Efecto de un precio máximo", "Mercado de ejemplo: a $100 se demandan 60 y se ofrecen 20; a $150, 40 y 40; a $200, 20 y 60. El Estado fija un máximo de $100. ¿Qué ocurre?",
         ["El equilibrio es $150. El máximo de $100 está por debajo.", "A $100 se demandan 60 y se ofrecen 20: hay un faltante de 40."],
         "Faltante de 40 unidades"),
        ("Un tope que no tiene efecto", "En el mismo mercado, el Estado fija un máximo de $250. ¿Qué efecto tiene?",
         ["El equilibrio es $150, que está bajo el tope.", "Como el mercado ya funciona bajo el límite, el tope no cambia nada."],
         "Ningún efecto"),
    ],
    mistakes=[("Creer que un precio máximo siempre baja los precios y beneficia a todos.", "Se ignora el faltante que genera si está bajo el equilibrio.", "Compara el tope con el precio de equilibrio y revisa los efectos en la cantidad."),
              ("Decir que el análisis del tope es solo positivo.", "Se olvida que decidir aplicarlo también depende de valores.", "Los efectos se describen con datos y la decisión incluye juicios de valor.")],
    T=[
        ("abc", "{F} En el mercado de arriendos, ¿cuál es el precio de equilibrio?", "$300.000", "$250.000", "$350.000", "A $300.000 se demandan y se ofrecen 300 piezas."),
        ("=", "{F} Se fija un tope de $250.000. ¿Cuántas piezas faltan?", "400-200", "Se resta la cantidad ofrecida a la cantidad demandada a $250.000."),
        ("abc", "En Economía y sociedad: ¿qué es un precio máximo?", "Un tope legal para el precio de un bien", "Un piso legal para el precio de un bien", "El precio más alto del mercado libre", "Impide cobrar más que cierto valor."),
        ("abc", "{F} Un tope de $250.000 está por debajo del equilibrio. ¿Qué genera?", "Un faltante de piezas", "Un excedente de piezas", "Nada", "Se demanda más de lo que se ofrece."),
        ("=", "{F} Mercado de trigo: con un precio mínimo de $500 el kilo, ¿cuántas toneladas de excedente hay?", "60-40", "Se resta la cantidad demandada a la ofrecida."),
        ("abc", "En Economía y sociedad: ¿qué es un subsidio?", "Una ayuda del Estado que abarata un bien o su producción", "Un impuesto sobre un bien", "Una multa por incumplir una norma", "El subsidio reduce el costo para quien compra o produce."),
        ("{F} Si se fijara un precio mínimo de $350.000 en el arriendo, ¿qué ocurriría con las piezas?", "Habría un excedente de 200 piezas", "A $350.000 se ofrecen 400 y se demandan 200."),
        ("abc", "{F} Si el Estado fijara un tope de $350.000, ¿qué efecto tendría?", "Ninguno, porque el equilibrio de $300.000 está bajo el tope", "Un faltante grande", "Un excedente grande", "Un tope sobre el equilibrio no limita lo que ya se cobra."),
        ("abc", "El Estado entrega un subsidio a estudiantes para pagar parte del arriendo. ¿Qué ocurre con la demanda de piezas?", "Aumenta, porque pueden pagar más", "Disminuye", "Se desplaza la oferta hacia la izquierda", "Con más recursos para pagar, más estudiantes demandan piezas."),
        ("abc", "{F} Los críticos del tope dicen que reduce las piezas disponibles. ¿Qué dato de la ficha respalda ese argumento?", "Con el tope se ofrecen 200 piezas, menos que las 300 de equilibrio", "Con el tope se ofrecen 500 piezas", "El tope sube el precio a $350.000", "Las piezas ofrecidas bajan de 300 a 200."),
        ("=", "{F} Con el tope de $250.000, las 200 piezas que sí se arriendan ahorran $50.000 cada una respecto del equilibrio. ¿Cuánto ahorran en total al mes?", "200*50000", "Se multiplica el ahorro por pieza por el número de piezas."),
        ("abc", "«El Estado debe fijar un tope a los arriendos» es una afirmación…", "Normativa, porque dice qué debe hacerse", "Positiva, porque se verifica con datos", "Ni normativa ni positiva", "Expresa un deber que depende de valores."),
        ("abc", "{F} Sin fijar un tope, ¿qué alternativa podría reducir el faltante de piezas en el mediano plazo?", "Facilitar que se ofrezcan más piezas", "Prohibir arrendar piezas", "Aumentar el tope", "Más oferta acerca la cantidad ofrecida a la demandada."),
    ],
    ctx=("abc", "El Estado de un país de ejemplo fija un precio máximo del pan de $1.500 el kilo cuando el equilibrio es $2.000. Algunas panaderías reducen la producción y otras venden menos calidad por el mismo precio. ¿Qué efecto de un tope bajo el equilibrio ilustra esto?", "Que se ofrece menos o con menor calidad al haber un faltante", "Que el pan aumenta de precio", "Que el tope no tiene efecto", "Un tope bajo el equilibrio reduce la cantidad ofrecida y puede afectar la calidad."),
    sc=[
        ("¿Qué genera un precio mínimo por encima del equilibrio?", "Un excedente", "Se ofrece más de lo que se demanda."),
        ("¿Por qué un tope sobre el equilibrio no tiene efecto?", "Porque el mercado ya opera con un precio menor", "Nadie cobra más que el tope."),
        ("¿Es la decisión de aplicar un tope solo un asunto de datos?", "No: también depende de valores como la protección de quienes compran", "Los datos informan efectos y el juicio decide qué priorizar."),
    ],
    op=("Elige una de estas medidas de ejemplo y analiza. Medida 1: tope de $250.000 al arriendo de la Ficha 15. Medida 2: precio mínimo de $500 el kilo de trigo. "
        "Escribe qué efecto tiene (con cifras de la ficha), quiénes ganan y quiénes pierden, un argumento de quienes la defienden y uno de quienes la critican, y qué parte del debate es positiva y cuál normativa.",
        "Medida 1. Faltante de 200 piezas. Ganan quienes consiguen pieza a menor precio; pierden quienes quedan sin pieza y los dueños. Defensores: protege a quienes arriendan. Críticos: reduce la oferta. Positivo: el faltante. Normativo: si debe aplicarse.",
        ["calcula el efecto con cifras de la ficha", "nombra ganadores y perdedores", "presenta argumentos de ambas posturas", "separa lo positivo de lo normativo"],
        ["cuadro con cinco filas"],
        ["decir que el tope siempre es bueno o malo", "no usar las cifras", "tomar partido sin argumentos"],
        "Pregunta: «¿qué postura elegirías y qué valor la sostiene?». Pide que lo diga sin descalificar la otra."),
    reinforce="Con la tabla de arriendos, calcula el faltante o excedente a cada uno de los cinco precios.",
    extend="Compara los argumentos a favor y en contra de un precio mínimo para productos agrícolas, sin elegir una postura.",
)

# ============================================================ OAC-05, clase 1
F = ("Ficha 16 (casos de ejemplo, ficticios). En el pueblo de Lomas del Sur una sola empresa, «Transportes Único», presta el servicio de bus y no hay otro medio equivalente. "
     "Datos de ejemplo: si hubiera muchas empresas compitiendo, el pasaje sería $400 (igual al costo por pasajero) y viajarían 1.000 personas al día. "
     "Como monopolio, Transportes Único cobra $700 y viajan 600 personas al día. Costo por pasajero para la empresa: $400.")
build(
    O5, 1, F,
    use="Aprenderé qué es un monopolio, qué barreras de entrada le permiten existir y cómo se compara su resultado con el de un mercado de competencia perfecta, incluyendo la dimensión ética.",
    prior=["Sé qué es un mercado y el precio de equilibrio.", "Sé qué es una externalidad.", "Distingo afirmaciones positivas y normativas."],
    explain=[
        "En un mercado de competencia perfecta hay muchas empresas pequeñas que venden un producto igual, cualquiera puede entrar o salir, y ninguna puede cambiar el precio por sí sola. En ese caso el precio tiende a igualar el costo de producir una unidad más. Es un modelo ideal: sirve de referencia, aunque casi ningún mercado lo cumple del todo.",
        "Un monopolio es un mercado donde una sola empresa vende un producto sin sustitutos cercanos. Puede existir por barreras de entrada, que son obstáculos que impiden o dificultan que otras empresas entren: leyes que dan exclusividad, control de un recurso clave, patentes o costos de inversión tan altos que nadie los asume. Una empresa con poder de mercado puede elegir el precio, en vez de aceptarlo.",
        "Un monopolio suele cobrar más y producir menos que un mercado competitivo. Eso transfiere dinero de los consumidores a la empresa y deja a algunos sin comprar aunque estarían dispuestos a pagar el costo de producción. Existe además el monopolio natural, donde un solo proveedor sale más barato porque los costos fijos son enormes, como una red de tuberías. Qué hacer ante un monopolio incluye debates éticos: ¿es justo aprovechar un poder así?, ¿cómo se protege a quienes dependen del servicio?",
    ],
    vocab=[("competencia perfecta", "mercado con muchas empresas, producto igual y libre entrada"), ("monopolio", "mercado con un solo vendedor sin sustitutos cercanos"), ("barrera de entrada", "obstáculo que impide la entrada de nuevas empresas"), ("poder de mercado", "capacidad de una empresa de influir en el precio"), ("monopolio natural", "mercado donde un solo proveedor resulta más barato"), ("patente", "derecho exclusivo temporal sobre una invención")],
    worked=[
        ("Identificar una barrera", "En una ciudad de ejemplo la ley da a una sola empresa el derecho de operar un teleférico urbano. ¿Qué barrera de entrada es?",
         ["Otras empresas no pueden entrar porque la ley lo impide.", "Es una barrera legal."],
         "Una barrera legal"),
        ("Comparar monopolio y competencia", "Mercado de ejemplo: competitivo, precio $200 y 90 unidades; monopolio, precio $350 y 60 unidades. ¿Cuántas unidades menos se venden con el monopolio?",
         ["Compara las cantidades: 90 y 60.", "Resta: 90 menos 60."],
         "30 unidades menos"),
    ],
    mistakes=[("Creer que toda empresa grande es un monopolio.", "Se confunde tamaño con ausencia de rivales.", "Monopolio es ser el único vendedor sin sustitutos cercanos."),
              ("Pensar que el monopolista no puede equivocarse al fijar el precio.", "Se supone poder absoluto.", "Si sube mucho el precio, los consumidores compran menos, y su ganancia depende de esa respuesta.")],
    T=[
        ("abc", "{F} ¿Por qué Transportes Único es un monopolio?", "Porque es la única empresa y no hay un medio equivalente", "Porque es una empresa grande", "Porque cobra un precio bajo", "Un monopolio es un solo vendedor sin sustitutos cercanos."),
        ("=", "{F} ¿Cuántos pesos más cuesta el pasaje en el monopolio que en la competencia?", "700-400", "Se resta el precio competitivo al del monopolio."),
        ("=", "{F} ¿Cuántas personas menos viajan por día en el monopolio que en la competencia?", "1000-600", "Se resta la cantidad del monopolio a la de la competencia."),
        ("abc", "En Economía y sociedad: ¿qué es un monopolio?", "Un mercado con un solo vendedor sin sustitutos cercanos", "Un mercado con muchos vendedores", "Una empresa muy grande", "Se define por la existencia de un solo vendedor."),
        ("abc", "En Economía y sociedad: ¿qué es una barrera de entrada?", "Un obstáculo que dificulta que nuevas empresas entren a un mercado", "Una norma que protege a los consumidores", "El precio de venta de una empresa", "Las barreras explican la permanencia del monopolio."),
        ("=", "{F} ¿Cuánta ganancia total (en pesos al día) obtiene Transportes Único como monopolio? Ganancia por pasajero por pasajeros.", "(700-400)*600", "Se multiplica la ganancia por pasajero por el número de pasajeros."),
        ("abc", "{F} En competencia perfecta, ¿por qué una empresa no puede subir sola el precio?", "Porque los consumidores comprarían a otras empresas", "Porque su producto es más caro de producir", "Porque no le conviene ganar más", "Con muchas empresas y producto igual, quien sube el precio pierde ventas."),
        ("=", "{F} ¿Cuánto pagan en total los pasajeros por día en el monopolio?", "700*600", "El gasto total es el precio por los pasajeros."),
        ("abc", "Una panadería de barrio tiene dos panaderías vecinas que venden pan parecido. ¿Es monopolio?", "No, porque hay sustitutos cercanos", "Sí, porque es la panadería del barrio", "Sí, porque cobra un precio alto", "Con otras panaderías cercanas, los clientes pueden cambiar."),
        ("{F} La empresa dice: «Con mi precio gano y todos tienen transporte». Con los datos, ¿qué se le puede responder?", "400 personas menos viajan que en un mercado competitivo", "La cantidad que viaja baja de 1.000 a 600."),
        ("abc", "Para instalar una segunda red de agua potable por todo el pueblo se necesitaría una inversión enorme. ¿Qué barrera ilustra?", "Costos de inversión muy altos, típicos de un monopolio natural", "Una ley de exclusividad", "Un precio máximo", "Los altos costos fijos hacen que un solo proveedor sea más barato."),
        ("{F} Si entrara una segunda empresa a competir, ¿qué se esperaría que ocurriera con el precio?", "Que bajara hacia el costo de $400", "La competencia presiona los precios hacia el costo de producir."),
        ("abc", "Un defensor de un monopolio dice: «Sus ganancias financian innovación». ¿Qué evidencia necesitarías para evaluar ese argumento?", "Cuánto de la ganancia se invierte realmente en innovación", "El número de clientes del monopolio", "El precio que cobra hoy", "El argumento puede evaluarse mirando el destino real de las ganancias."),
    ],
    ctx=("abc", "En un pueblo de ejemplo hay un único supermercado a 80 km de otro, y los vecinos no tienen cómo viajar. El supermercado sube el precio de varios productos un 15% en un mes. ¿Qué elemento del monopolio aparece?", "Poder de mercado ejercido por falta de sustitutos cercanos", "Competencia perfecta", "Un precio máximo", "Sin alternativas cercanas, el vendedor puede fijar precios más altos."),
    sc=[
        ("En Economía y sociedad: ¿qué es el poder de mercado?", "La capacidad de una empresa de influir en el precio", "En competencia perfecta una empresa no tiene este poder."),
        ("Nombra dos barreras de entrada.", "Leyes de exclusividad, patentes, control de un recurso o costos muy altos", "Son obstáculos que impiden nuevas empresas."),
        ("¿Qué ocurre con precio y cantidad en un monopolio respecto de la competencia?", "El precio es mayor y la cantidad menor", "El monopolista restringe la cantidad para cobrar más."),
    ],
    op=("Analiza un monopolio de ejemplo. Elige: (1) una empresa que es la única en entregar agua en una ciudad, o (2) una empresa con una patente que fabrica un repuesto único. Datos de ejemplo para ambos: competencia → precio $1.000 y 100 unidades; monopolio → precio $1.600 y 70 unidades; costo por unidad $1.000. "
        "Escribe la barrera de entrada, cuánto más pagan los consumidores por unidad, cuántas unidades menos se venden, la ganancia del monopolista (precio menos costo, por unidades), y una pregunta ética que plantea el caso.",
        "(1) Barrera: costo de la red (monopolio natural). 600 más por unidad. 30 unidades menos. Ganancia: (1.600 menos 1.000) por 70 son 42.000. Pregunta: ¿cómo se protege a las familias que dependen del agua?",
        ["nombra una barrera de entrada pertinente", "calcula correctamente las diferencias", "calcula la ganancia", "plantea una pregunta ética"],
        ["cuatro cálculos y una pregunta"],
        ["confundir precio con ganancia", "no restar el costo", "plantear una pregunta que no se relaciona con el caso"],
        "Pregunta: «¿qué ganaría la empresa por unidad?». Si no resta el costo, pídele repetir."),
    reinforce="Escribe tres mercados de tu comuna con muchos vendedores y uno con muy pocos, y explica la diferencia.",
    extend="Describe la diferencia entre una barrera legal y una barrera por costos, con un ejemplo de cada una.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 17 (mercados de ejemplo, ficticios). Mercado de telefonía móvil de un país de ejemplo: la empresa Alfa tiene el 40% de los clientes, Beta el 35%, Gamma el 15% y otras tres empresas pequeñas, juntas, el 10%. "
     "Mercado de pizzerías de un barrio: 12 pizzerías; cada una ofrece algo distinto (masa fina o gruesa, ingredientes, local, nombre) y cobra entre $7.000 y $9.000.")
build(
    O5, 2, F,
    use="Aprenderé a reconocer el oligopolio y la competencia monopolística, a medir qué tan concentrado está un mercado y a explicar cómo afectan el precio, la variedad y a los consumidores.",
    prior=["Sé qué es un monopolio y una barrera de entrada.", "Sé calcular un porcentaje.", "Conozco la competencia perfecta como modelo de referencia."],
    explain=[
        "Entre la competencia perfecta y el monopolio hay otras estructuras de mercado. Un oligopolio es un mercado dominado por pocas empresas grandes, como puede ocurrir en la telefonía móvil o en la venta de combustibles. Como son pocas, cada empresa debe considerar qué harán sus rivales cuando decide su precio o su producción: a eso se le llama interdependencia.",
        "La concentración de un mercado se puede medir sumando las participaciones de mercado (porcentaje de clientes o ventas) de las empresas más grandes. Si las tres mayores suman casi todo el mercado, está muy concentrado. Un mercado concentrado tiene mayor riesgo de precios altos o de acuerdos entre empresas, aunque no siempre ocurre.",
        "La competencia monopolística es un mercado con muchas empresas que venden productos diferenciados, es decir, parecidos pero no iguales (por marca, calidad, ubicación o estilo). La diferenciación le da a cada empresa algo de poder para fijar el precio, pero la entrada libre limita sus ganancias. Es común en restaurantes, peluquerías o ropa, y la publicidad cumple un papel: informa, pero también busca diferenciar.",
    ],
    vocab=[("oligopolio", "mercado dominado por pocas empresas grandes"), ("interdependencia", "cada empresa debe considerar las reacciones de sus rivales"), ("participación de mercado", "porcentaje del mercado que tiene una empresa"), ("concentración", "grado en que pocas empresas dominan un mercado"), ("competencia monopolística", "muchas empresas con productos diferenciados"), ("diferenciación", "características que hacen distinto un producto")],
    worked=[
        ("Medir concentración", "En un mercado de ejemplo, tres empresas tienen 30%, 25% y 20% de las ventas. ¿Qué participación suman?",
         ["Suma 30 más 25 más 20.", "Las tres mayores suman 75%, un mercado concentrado."],
         "75%"),
        ("Clasificar una estructura", "En una ciudad de ejemplo hay dos empresas de energía eléctrica que concentran casi todo el mercado y vigilan mucho los precios de la otra. ¿Qué estructura es?",
         ["Pocas empresas grandes dominan el mercado.", "Se observan interdependencia y concentración: es un oligopolio."],
         "Oligopolio"),
    ],
    mistakes=[("Confundir oligopolio con monopolio.", "Se piensa que «pocas» significa «una».", "Monopolio es una; oligopolio son pocas empresas grandes."),
              ("Pensar que diferenciar un producto siempre es engañar.", "Se mezcla diferenciación con publicidad engañosa.", "La diferenciación también refleja variedad y preferencias reales.")],
    T=[
        ("=", "{F} ¿Qué participación suman las tres mayores empresas de telefonía?", "40+35+15", "Se suman las tres participaciones más altas."),
        ("abc", "{F} ¿Qué tipo de estructura es el mercado de telefonía móvil de la ficha?", "Oligopolio", "Monopolio", "Competencia perfecta", "Tres empresas concentran el 90% del mercado."),
        ("abc", "{F} ¿Qué tipo de estructura es el mercado de pizzerías?", "Competencia monopolística", "Oligopolio", "Monopolio", "Hay muchas empresas con productos diferenciados."),
        ("abc", "En Economía y sociedad: ¿qué es un oligopolio?", "Un mercado dominado por pocas empresas grandes", "Un mercado con un solo vendedor", "Un mercado con cientos de vendedores iguales", "Hay pocas empresas que dominan y se observan entre sí."),
        ("En Economía y sociedad: ¿qué significa interdependencia entre empresas?", "Que cada una debe considerar cómo reaccionarán las rivales", "Es característica del oligopolio porque pocas decisiones influyen en las demás."),
        ("=", "{F} Si Gamma y las tres empresas pequeñas se fusionaran, ¿qué porcentaje del mercado tendrían juntas?", "15+10", "Se suman la participación de Gamma y la del conjunto de pequeñas."),
        ("abc", "{F} ¿Qué característica de las pizzerías muestra la diferenciación?", "Cada una ofrece algo distinto, como masa, ingredientes o local", "Todas cobran lo mismo", "Todas tienen el mismo dueño", "La diferenciación hace que no sean sustitutos perfectos."),
        ("abc", "{F} Si Alfa y Beta se fusionaran, ¿qué participación tendrían juntas?", "75%", "40%", "90%", "Juntas suman 40 más 35, es decir, 75 por ciento."),
        ("abc", "Una pizzería sube el precio de $8.000 a $8.500 y no pierde a todos sus clientes. ¿Por qué puede hacerlo?", "Porque su producto diferenciado le da algo de poder de mercado", "Porque es un monopolio", "Porque no tiene competencia", "La diferenciación hace que algunos clientes la prefieran aunque cueste más."),
        ("{F} ¿Por qué en el mercado de telefonía es más probable que una empresa piense en cómo reaccionarán sus rivales que en el de pizzerías?", "Porque son pocas empresas grandes y sus decisiones se afectan entre sí", "En una pizzería, el efecto de un rival individual es pequeño, y en un oligopolio es grande."),
        ("abc", "{F} Una compañera dice: «Con tres empresas que suman 90%, hay colusión seguro». ¿Qué corrección harías?", "Alta concentración aumenta el riesgo, pero no prueba que haya acuerdos", "Tiene razón, la concentración prueba colusión", "Esa cifra es ilegal por sí sola", "Concentrar no equivale a colusionar: faltan pruebas de acuerdos."),
        ("abc", "Una marca de ropa gasta en publicidad para mostrar que sus polerones son distintos. ¿Qué función cumple en competencia monopolística?", "Diferenciar su producto y dar información a los clientes", "Fijar un precio máximo", "Impedir que otros vendan", "La publicidad ayuda a distinguir el producto, aunque también puede persuadir."),
        ("abc", "{F} Si entraran cinco pizzerías nuevas con ideas distintas, ¿qué se esperaría?", "Más variedad y presión a la baja sobre los precios", "Menos variedad", "Precios fijados por el Estado", "La entrada libre aumenta la competencia."),
    ],
    ctx=("abc", "En una región de ejemplo hay tres cadenas de farmacias que reúnen casi todas las ventas, y cuando una baja el precio de un producto las otras lo bajan al día siguiente. ¿Qué característica ilustra?", "Interdependencia en un oligopolio", "Competencia perfecta", "Monopolio natural", "Las empresas reaccionan a las decisiones de las rivales."),
    sc=[
        ("En Economía y sociedad: ¿qué es la competencia monopolística?", "Muchas empresas que venden productos diferenciados", "Cada una tiene algo de poder sobre su precio."),
        ("¿Cómo se mide la concentración con participaciones de mercado?", "Sumando las participaciones de las empresas más grandes", "Si pocas suman casi todo, el mercado está concentrado."),
        ("¿Prueba la alta concentración que hay acuerdos entre empresas?", "No: solo aumenta el riesgo", "Para afirmar colusión faltan pruebas de acuerdos entre empresas."),
    ],
    op=("Clasifica estos tres mercados de ejemplo y justifica. Mercado A: una sola empresa de agua en una ciudad. Mercado B: cuatro empresas de cemento que suman 85% de las ventas y vigilan sus precios. Mercado C: 30 cafeterías de un barrio, cada una con su estilo y precios entre $2.000 y $3.500. "
        "Para cada uno escribe la estructura, la característica que lo muestra y qué podría preocupar o favorecer a los consumidores.",
        "A. Monopolio (natural), un solo vendedor sin sustitutos; preocupa el precio y el acceso. B. Oligopolio; cuatro empresas suman 85% e interdependencia; preocupa la colusión. C. Competencia monopolística; muchas y diferenciadas; favorece la variedad.",
        ["clasifica correctamente los tres mercados", "justifica con una característica", "nombra un efecto en los consumidores"],
        ["tabla de tres filas"],
        ["confundir oligopolio con monopolio", "justificar solo por el tamaño", "no relacionar con los consumidores"],
        "Pregunta: «¿cuántas empresas dominan y qué tan parecidos son sus productos?». Con eso clasifica."),
    reinforce="Escribe un ejemplo de tu comuna para oligopolio y otro para competencia monopolística, y por qué.",
    extend="Explica por qué la diferenciación puede ser buena para los consumidores y también una forma de ganar poder sobre el precio.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 18 (juego de ejemplo, ficticio). Dos estaciones de servicio, Alfa y Beta, son las únicas de un pueblo. Cada una elige cada mes entre precio alto o precio bajo. Ganancias de ejemplo (en millones de pesos por mes): "
     "ambas precio alto: Alfa 100 y Beta 100. Alfa precio bajo y Beta alto: Alfa 150 y Beta 40. Alfa alto y Beta bajo: Alfa 40 y Beta 150. Ambas precio bajo: Alfa 70 y Beta 70.")
build(
    O5, 3, F,
    use="Aprenderé qué es la colusión, por qué tienta a las empresas, cómo daña a los consumidores y cómo se aborda desde la ética y la regulación.",
    prior=["Sé qué es un oligopolio e interdependencia.", "Sé leer una tabla de ganancias.", "Distingo costo privado y social."],
    explain=[
        "La colusión es un acuerdo entre empresas competidoras, explícito o tácito y casi siempre secreto, para no competir: fijar precios, repartirse clientes o limitar la producción. Cuando un grupo de empresas se pone de acuerdo para actuar como si fueran una sola, se llama cartel. En muchos países la colusión es ilegal. En Chile, la Fiscalía Nacional Económica investiga estos casos y el Tribunal de Defensa de la Libre Competencia resuelve.",
        "Una tabla de ganancias permite ver por qué tienta. Si ambas empresas mantienen el precio alto, cada una gana más que si ambas compiten con precio bajo. Pero cada una, individualmente, gana más si baja su precio mientras la otra lo mantiene. Eso empuja a competir, salvo que se pongan de acuerdo, y además cada una tiene incentivo a romper el acuerdo en secreto.",
        "La colusión daña a los consumidores, que pagan más, y a las empresas que no participan y quedan fuera. También tiene una dimensión ética: implica engañar al mercado y quebrar la confianza. Los países discuten cómo detectar y sancionar estos acuerdos (multas, delaciones, otras sanciones). Esta clase estudia el mecanismo, y no recomienda a nadie coludirse.",
    ],
    vocab=[("colusión", "acuerdo entre competidores para no competir"), ("cartel", "grupo de empresas que actúa de común acuerdo"), ("tabla de ganancias", "cuadro que muestra el resultado según lo que elija cada empresa"), ("precio alto", "opción de cobrar más por el producto"), ("sanción", "castigo por incumplir una norma"), ("tácito", "acuerdo no dicho claramente pero entendido")],
    worked=[
        ("Leer una tabla de ganancias", "En una tabla de ejemplo: si ambas empresas cobran precio alto, cada una gana 80; si ambas cobran bajo, cada una gana 50. ¿Cuál es la mejor situación conjunta para ellas?",
         ["Compara 80 y 50 para cada empresa.", "Les conviene a ambas que los dos cobren alto."],
         "Que ambas cobren precio alto"),
        ("Reconocer colusión", "Dos empresas de ejemplo se reúnen y acuerdan subir el precio al mismo valor el mismo día. ¿Es colusión?",
         ["Hay un acuerdo entre competidores para no competir.", "Fijar precios en conjunto es colusión."],
         "Sí, es colusión"),
    ],
    mistakes=[("Pensar que todos los acuerdos entre empresas son colusión.", "Se olvida que algunos acuerdos no afectan la competencia.", "Colusión es un acuerdo entre competidores para no competir."),
              ("Creer que la colusión solo afecta a las empresas.", "Se ignora a los consumidores.", "Los consumidores pagan más y tienen menos opciones.")],
    T=[
        ("abc", "{F} Si ambas estaciones cobran precio alto, ¿cuántos millones gana cada una?", "100", "70", "150", "La tabla dice 100 para cada una."),
        ("abc", "{F} Si ambas bajan el precio, ¿cuántos millones gana cada una?", "70", "100", "40", "Con ambas con precio bajo, cada una gana 70."),
        ("abc", "En Economía y sociedad: ¿qué es la colusión?", "Un acuerdo entre competidores para no competir", "Una fusión legal entre dos empresas", "Una oferta de precios bajos", "La colusión implica acordar precios, repartirse clientes o limitar la producción."),
        ("=", "{F} Si Beta mantiene precio alto y Alfa baja el suyo, ¿cuánto más gana Alfa que si ambas mantuvieran precio alto?", "150-100", "Se resta la ganancia con ambos altos a la ganancia al bajar solo ella."),
        ("{F} Si Beta cobra precio bajo, ¿qué le conviene hacer a Alfa: precio alto o bajo?", "Precio bajo, porque gana 70 en vez de 40", "Al bajar, Alfa gana 70 frente a 40 con precio alto."),
        ("{F} Si Beta cobra precio alto, ¿qué le conviene a Alfa: precio alto o bajo?", "Precio bajo, porque gana 150 en vez de 100", "Al bajar, gana 150 frente a 100 con precio alto."),
        ("abc", "{F} Si cada estación decide por separado, buscando lo mejor para sí misma, ¿qué ocurre?", "Ambas bajan el precio y cada una gana 70", "Ambas mantienen precio alto y ganan 100", "Alfa gana 150 y Beta 40", "Bajar es mejor para cada una, sea cual sea lo que haga la otra."),
        ("=", "{F} Si logran coludirse y cobrar ambas precio alto, ¿cuántos millones más gana cada una que sin acuerdo?", "100-70", "Se resta lo que ganan compitiendo a lo que ganan coludidas."),
        ("abc", "{F} ¿Por qué un acuerdo secreto de precio alto es inestable?", "Porque cada una gana más si rompe el acuerdo y baja su precio", "Porque la tabla prohíbe el acuerdo", "Porque ambas ganan menos con precio alto", "Rompiendo, la que baja gana 150 frente a 100."),
        ("abc", "{F} ¿Quién sale perjudicado con un acuerdo de precio alto?", "Los clientes del pueblo, que pagan más", "Las propias estaciones, que ganan menos", "Las empresas que no participan en el acuerdo", "La colusión eleva el precio que pagan los consumidores."),
        ("abc", "Un grupo de empresas de ejemplo acuerda repartirse las ciudades: cada una vende solo en una. ¿Es colusión?", "Sí, aunque no fijen precios, porque se reparten el mercado para no competir", "No, porque no hablan de precios", "No, porque venden en ciudades distintas", "Repartirse mercados es una forma de no competir."),
        ("abc", "«Las empresas deberían ser castigadas con cárcel por coludirse» es una afirmación…", "Normativa, porque expresa cómo debería sancionarse", "Positiva, porque describe un hecho comprobable", "Falsa", "Opina sobre lo que debería hacerse."),
        ("{F} ¿Qué pregunta ética plantea la colusión de las dos estaciones respecto de los vecinos del pueblo?", "Si es justo que paguen más por un acuerdo que ellos no conocen", "Hay engaño y se quiebra la confianza del mercado."),
    ],
    ctx=("abc", "Una investigación de ejemplo descubre que tres empresas de ejemplo que venden pintura intercambiaban mensajes para fijar el precio mínimo de venta al supermercado. ¿Qué institución chilena investiga casos de colusión según la clase?", "La Fiscalía Nacional Económica", "El municipio", "El colegio profesional", "La explicación señala a la Fiscalía Nacional Económica y al Tribunal de Defensa de la Libre Competencia."),
    sc=[
        ("En Economía y sociedad: ¿qué es un cartel?", "Un grupo de empresas que actúa de común acuerdo para no competir", "Es el resultado de una colusión."),
        ("¿Por qué tienta a las empresas coludirse?", "Porque ambas ganan más que compitiendo", "Pero cada una gana más si rompe el acuerdo."),
        ("¿Quiénes pierden con una colusión?", "Los consumidores, que pagan más, y las empresas competidoras fuera del acuerdo", "Se distorsiona el mercado y se dañan las opciones de compra."),
    ],
    op=("Analiza una tabla nueva de ejemplo. Dos panaderías de un pueblo eligen entre precio alto o bajo. Ambas altas: cada una gana 60. Una baja y la otra alta: la que baja gana 90 y la otra 20. Ambas bajas: cada una gana 40. "
        "Escribe qué elegiría cada panadería si decide sola, qué resultado obtienen, qué ganarían si se coludieran, por qué ese acuerdo es inestable, quiénes pierden y una pregunta ética.",
        "Sola, cada una baja (90 frente a 60 si la otra mantiene alto; 40 frente a 20 si la otra baja), y ambas ganan 40. Coludidas ganarían 60. Es inestable porque romper da 90. Pierden los vecinos que pagan más. Pregunta: ¿es justo ocultar el acuerdo?",
        ["determina la decisión individual con la tabla", "compara el resultado con el acuerdo", "explica la inestabilidad del acuerdo", "nombra a los perjudicados"],
        ["respuesta de cinco partes"],
        ["leer mal la tabla", "olvidar a los consumidores", "recomendar coludirse"],
        "Pregunta: «¿qué conviene a una panadería si la otra mantiene alto, y si baja?». Pide que haga los dos casos."),
    reinforce="Con la Ficha 18, escribe la mejor decisión de Alfa para cada decisión posible de Beta.",
    extend="Explica por qué se discute cómo sancionar la colusión (multas, delaciones, otras medidas) sin decidir cuál es la mejor.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 19 (caso de ejemplo, ficticio). Una lavandería industrial de ejemplo lava ropa de hoteles y vierte parte del agua con detergente a un estero cercano. Cada lote de ropa le deja un ingreso de $100.000 y le cuesta $60.000. "
     "El agua sucia obliga a los vecinos del estero a gastar en total $50.000 por lote en tratar el agua que usan. Opciones de política que se discuten: un impuesto de $50.000 por lote, una norma que exige una planta de tratamiento, o no hacer nada.")
build(
    O5, 4, F,
    use="Aprenderé cómo las externalidades negativas hacen que el mercado produzca más de lo conveniente para la sociedad y qué herramientas se discuten para corregirlas, con sus ventajas, costos y dilemas éticos.",
    prior=["Sé qué es una externalidad y calcular costo social.", "Sé que un impuesto encarece una actividad.", "Distingo análisis positivo y normativo."],
    explain=[
        "Una externalidad negativa es un costo que una actividad impone a terceros que no participan en ella, como la contaminación. Como quien produce no paga ese costo, lo ignora al decidir cuánto producir, y el mercado entrega una cantidad mayor que la conveniente para la sociedad. Esto es una falla de mercado, una situación en que el mercado por sí solo no logra el mejor resultado.",
        "Hay varias formas de corregirla. Un impuesto sobre la actividad hace que quien contamina pague el costo que traspasaba, y se dice que internaliza la externalidad. Una norma o regulación obliga a cumplir una conducta, como instalar una planta de tratamiento. Otras herramientas son los permisos de contaminación que se pueden comprar y vender, o la negociación directa entre las partes cuando es posible.",
        "Cada herramienta tiene ventajas y costos. Un impuesto es flexible, pero puede trasladarse a los precios; una norma da certeza sobre el resultado, pero puede ser más cara para quien cumple; no hacer nada ahorra costos de fiscalización, pero deja el daño en quienes no deciden. La elección involucra datos y valores, como proteger el medio ambiente, el empleo, o a las personas que viven cerca. Aquí se compara sin imponer una postura.",
    ],
    vocab=[("externalidad negativa", "costo que una actividad impone a terceros"), ("falla de mercado", "situación en que el mercado solo no logra un buen resultado"), ("internalizar", "hacer que quien produce el daño pague su costo"), ("norma", "regla que obliga a una conducta"), ("permiso transable", "derecho a contaminar que se compra y se vende"), ("fiscalización", "control de que se cumplan las reglas")],
    worked=[
        ("Calcular el costo social", "Un lote de pintura de ejemplo tiene costo privado de $30.000 y causa un daño a terceros de $20.000. ¿Cuál es el costo social?",
         ["El costo social suma el privado y el daño a terceros.", "Suma 30.000 y 20.000."],
         "$50.000"),
        ("Efecto de un impuesto", "Una empresa de ejemplo gana $25.000 por lote y su daño a terceros es de $15.000 por lote. Se aplica un impuesto de $15.000. ¿Cómo queda su ganancia?",
         ["Ganancia antes: 25.000. Impuesto: 15.000.", "Ganancia después: 25.000 menos 15.000 son 10.000."],
         "$10.000 por lote"),
    ],
    mistakes=[("Creer que el impuesto elimina siempre la contaminación.", "Se supone que quien paga deja de contaminar.", "El impuesto reduce la actividad si la hace menos rentable, pero depende de su monto."),
              ("Pensar que hay una única solución correcta.", "Se ignoran los costos y valores distintos.", "Compara las herramientas con criterios y declara los valores que priorizas.")],
    T=[
        ("=", "{F} ¿Cuál es el costo social de un lote de ropa lavada?", "60000+50000", "Se suman el costo privado y el costo para los vecinos."),
        ("=", "{F} ¿Cuánto gana la lavandería por lote considerando solo su costo privado?", "100000-60000", "Se resta el costo privado al ingreso."),
        ("abc", "En Economía y sociedad: ¿qué es una externalidad negativa?", "Un costo que una actividad impone a terceros", "Un beneficio que se reparte entre las empresas", "Un impuesto sobre el consumo", "Es un efecto sobre quienes no participan en la decisión."),
        ("abc", "{F} Con el costo social, ¿conviene el lote a la sociedad?", "No, porque el costo social de 110.000 supera el ingreso de 100.000", "Sí, porque la empresa gana 40.000", "Sí, porque los vecinos pueden pagar", "El costo para toda la sociedad es mayor que el ingreso."),
        ("abc", "{F} ¿Por qué la lavandería produce aunque el lote no convenga a la sociedad?", "Porque no paga el costo que impone a los vecinos", "Porque desconoce su ingreso", "Porque el Estado se lo exige", "Decide con su costo privado y no incluye el daño."),
        ("=", "{F} Con un impuesto de $50.000 por lote, ¿cuánto queda de ganancia por lote?", "100000-60000-50000", "Se restan el costo privado y el impuesto al ingreso."),
        ("abc", "{F} Con ese impuesto, ¿qué decisión le conviene a la lavandería?", "Dejar de producir ese lote, porque su ganancia sería negativa", "Producir más lotes", "Subir el impuesto", "Con -10.000 por lote, no le conviene producirlo."),
        ("abc", "En Economía y sociedad: ¿qué significa internalizar una externalidad?", "Que quien causa el daño pague su costo", "Que los vecinos paguen el daño", "Que el Estado oculte el daño", "Internalizar es incorporar el costo externo en la decisión de quien lo causa."),
        ("abc", "{F} La norma que exige una planta de tratamiento cuesta $30.000 por lote a la lavandería. ¿Cuál es su ganancia por lote si cumple y elimina el daño?", "$10.000", "$40.000", "-$20.000", "Son 100.000 menos 60.000 menos 30.000, y los vecinos ya no pagan."),
        ("{F} Compara la norma de la planta (costo 30.000 por lote) con el impuesto (50.000 por lote) desde la perspectiva de la empresa.", "La norma le cuesta menos por lote que el impuesto", "Cumplir la norma cuesta 30.000, menos que los 50.000 del impuesto."),
        ("abc", "{F} Un defensor del impuesto dice que es flexible. Un crítico dice que podría trasladarse a los precios. ¿Qué tipo de desacuerdo es?", "Hay argumentos con ventajas y costos de la misma herramienta", "Es un desacuerdo solo sobre valores, sin efectos que discutir", "Solo uno de los dos habla de dinero", "Ambas posturas señalan aspectos distintos del mismo instrumento."),
        ("abc", "{F} Un vecino dice: «Lo único justo es prohibir la lavandería». ¿Qué tipo de enunciado es?", "Normativo", "Positivo", "Un dato", "Expresa lo que debería hacerse según un valor."),
        ("{F} Imagina que la lavandería cierra y 40 personas pierden su empleo. ¿Qué dilema ético se presenta?", "Proteger el estero y la salud de los vecinos frente a proteger los empleos", "Hay que ponderar valores distintos, como empleo y salud."),
    ],
    ctx=("abc", "Una ciudad de ejemplo permite a las empresas comprar y vender permisos para emitir cierta cantidad de humo, con un total limitado. ¿Qué herramienta es?", "Permisos transables", "Un precio máximo", "Un subsidio", "Los permisos limitan el total y se pueden comprar y vender."),
    sc=[
        ("En Economía y sociedad: ¿qué es una falla de mercado?", "Cuando el mercado solo no logra un buen resultado para la sociedad", "Una externalidad negativa es un ejemplo de falla de mercado."),
        ("Nombra dos herramientas para corregir una externalidad negativa.", "Impuestos, normas, permisos transables o negociación", "Cada una tiene ventajas y costos."),
        ("¿Por qué el impuesto «internaliza» la externalidad?", "Porque quien contamina paga el costo que traspasaba", "El costo entra en su decisión."),
    ],
    op=("Elige un caso de ejemplo y evalúa. Caso 1: un criadero de cerdos cuyos malos olores afectan a un pueblo. Caso 2: una empresa de buses que genera humo en un barrio. Define: quién genera el costo, quiénes son los terceros, "
        "una herramienta para corregirlo (impuesto, norma o permisos), una ventaja y un costo de esa herramienta, y una pregunta ética. Rotula con «de ejemplo» cualquier cifra que uses.",
        "Caso 2. Genera el costo: la empresa de buses. Terceros: vecinos. Herramienta: norma de buses con filtro. Ventaja: certeza del resultado. Costo: caro para la empresa. Pregunta: ¿quién debe pagar el filtro, la empresa o los pasajeros?",
        ["identifica generador y terceros", "elige una herramienta pertinente", "nombra una ventaja y un costo", "plantea una pregunta ética"],
        ["texto de cinco partes"],
        ["no distinguir quién genera el costo", "presentar la herramienta como perfecta", "dar cifras sin rotularlas"],
        "Pregunta: «¿quién paga hoy el daño?». Con eso identifica a los terceros."),
    reinforce="Describe una externalidad negativa que conozcas de tu barrio y una forma de corregirla.",
    extend="Explica por qué un impuesto puede terminar pagándolo en parte los consumidores y qué discusión ética genera.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 20 (caso de ejemplo, ficticio). La ciudad de Puerto Claro tiene una única empresa de agua potable porque instalar redes paralelas sería carísimo (monopolio natural). Se discuten cuatro opciones, con datos de ejemplo: "
     "Opción 1, dejar a la empresa fijar sus tarifas libremente: tarifa $900 el metro cúbico, ganancia alta, algunas familias reducen su consumo por el costo. "
     "Opción 2, un regulador que fija la tarifa máxima en $600: la empresa gana menos, pero hay agua para todos a menor precio, aunque debe fiscalizarse la calidad. "
     "Opción 3, una empresa pública sin fines de lucro: tarifa $500, pero depende del presupuesto estatal. "
     "Opción 4, una concesión por 20 años a la empresa que ofrezca la tarifa más baja en una licitación.")
build(
    O5, 5, F,
    use="Aprenderé a evaluar el rol del Estado como regulador ante fallas de mercado, comparando opciones con criterios, considerando la dimensión ética y reconociendo los riesgos de regular.",
    prior=["Sé qué es un monopolio natural y una externalidad.", "Sé qué es un precio máximo.", "Distingo análisis positivo y normativo."],
    explain=[
        "El Estado puede actuar como regulador cuando el mercado falla: fija reglas, controla que se cumplan y sanciona a quien no las cumple. Ejemplos son los topes a las tarifas de servicios de agua o electricidad, las normas ambientales, la defensa de la libre competencia y la protección de los consumidores. Regular no es lo mismo que producir: el Estado puede regular sin ser dueño de las empresas.",
        "Regular también tiene riesgos y costos. La información es difícil de obtener: el regulador puede no conocer los costos reales de la empresa. La captura regulatoria ocurre cuando el regulador termina favoreciendo a las empresas que debería vigilar. Y una regulación excesiva puede desincentivar la inversión o la innovación. Por eso se discute no solo si regular, sino cómo y cuánto, y con qué transparencia.",
        "Para evaluar opciones se usan criterios: acceso (¿llega a todos?), precio, calidad, eficiencia, sostenibilidad financiera y equidad. También hay dimensión ética: transparencia, honestidad, trato justo a quienes tienen menos poder y rendición de cuentas. Las posturas difieren porque priorizan valores distintos, y un análisis sólido las presenta con sus argumentos y evidencia, sin dar por cerrado el debate.",
    ],
    vocab=[("regulador", "organismo que fija y vigila reglas de un mercado"), ("captura regulatoria", "cuando el regulador favorece a quienes debería vigilar"), ("concesión", "derecho temporal para prestar un servicio público"), ("licitación", "proceso en que varias empresas compiten por un contrato"), ("rendición de cuentas", "deber de explicar y justificar lo que se hace"), ("sostenibilidad financiera", "capacidad de cubrir los costos en el tiempo")],
    worked=[
        ("Aplicar un criterio", "Dos opciones de ejemplo para un servicio: A cobra $700 y llega al 95% de las familias; B cobra $500 y llega al 70%. Según el criterio de acceso, ¿cuál es mejor?",
         ["El acceso se mide por el porcentaje de familias a las que llega.", "A llega al 95% y B al 70%."],
         "A es mejor en acceso"),
        ("Identificar un riesgo", "Un regulador de ejemplo recibe información de costos solo de la empresa que regula y fija una tarifa según esos datos. ¿Qué riesgo aparece?",
         ["Depende de la información de la empresa vigilada.", "Existe riesgo de información incompleta y de captura regulatoria."],
         "Información insuficiente y posible captura"),
    ],
    mistakes=[("Creer que regular es lo mismo que estatizar.", "Se confunde regular con ser dueño.", "El Estado puede fijar reglas sin producir el servicio."),
              ("Pensar que la mejor opción es la de menor tarifa.", "Se usa un solo criterio.", "Compara acceso, calidad, financiamiento y equidad, además del precio.")],
    T=[
        ("abc", "{F} ¿Por qué hay una sola empresa de agua en Puerto Claro?", "Porque instalar redes paralelas sería carísimo", "Porque la ley prohíbe otras", "Porque las personas no quieren agua", "La ficha describe un monopolio natural por los altos costos de las redes."),
        ("=", "{F} ¿Cuánto más barata es la tarifa de la Opción 2 que la de la Opción 1, en pesos por metro cúbico?", "900-600", "Se resta la tarifa regulada a la libre."),
        ("abc", "En Economía y sociedad: ¿qué hace un regulador?", "Fija y vigila reglas de un mercado", "Produce todos los bienes", "Fija el sueldo de todos los trabajadores", "Un regulador vela por reglas y su cumplimiento."),
        ("abc", "{F} ¿Qué opción depende del presupuesto estatal?", "La Opción 3", "La Opción 1", "La Opción 4", "La empresa pública sin fines de lucro necesita presupuesto del Estado."),
        ("En Economía y sociedad: ¿qué es una licitación?", "Un proceso en que varias empresas compiten por un contrato", "Se elige la mejor oferta según los criterios definidos."),
        ("abc", "{F} ¿Qué opción deja a la empresa fijar libremente sus tarifas?", "La Opción 1", "La Opción 2", "La Opción 3", "La primera deja la tarifa a decisión de la empresa."),
        ("{F} Con el criterio de menor tarifa, ¿qué opción es la mejor de las cuatro de la ficha con tarifa dada?", "La Opción 3, con $500", "Las tarifas dadas son 900, 600 y 500, y la menor es 500."),
        ("abc", "{F} La Opción 2 exige fiscalizar la calidad. ¿Qué riesgo apunta?", "Que una tarifa baja lleve a reducir la calidad si no se controla", "Que el agua suba de precio", "Que no haya regulador", "Una tarifa tope puede incentivar a ahorrar costos con menor calidad."),
        ("abc", "{F} Si el regulador fija la tarifa solo con datos entregados por la empresa, ¿qué riesgo aparece?", "Información incompleta y posible captura regulatoria", "Que el agua se vuelva gratuita para todos", "Que bajen los impuestos", "El regulador depende de quien vigila."),
        ("{F} Una vecina dice: «La Opción 3 es la mejor porque es más barata». ¿Qué criterio adicional revisarías?", "La sostenibilidad financiera, porque depende del presupuesto estatal", "El precio bajo no basta si el servicio no se puede financiar en el tiempo."),
        ("abc", "{F} Un defensor de la Opción 1 dice: «Con ganancias altas la empresa invierte en la red». Un crítico dice: «Las familias reducen su consumo por el costo». ¿Qué ocurre aquí?", "Ambos señalan efectos distintos con valores distintos: inversión y acceso", "Solo uno tiene argumentos", "Ambos hablan de la Opción 2", "Cada postura destaca un criterio diferente."),
        ("abc", "{F} ¿Qué pregunta ética es más pertinente al decidir sobre un servicio esencial como el agua?", "¿Cómo se asegura que lleguen a todos, incluidas las familias de menores ingresos?", "¿Cuántos clientes puede tener la empresa el próximo año?", "¿Cuánto ganan los dueños de la empresa?", "Se refiere al acceso justo a un servicio esencial."),
        ("¿Por qué una concesión por licitación debe incluir rendición de cuentas y fiscalización?", "Porque quien gana el contrato podría incumplir calidad o tarifas una vez adjudicado", "La competencia ocurre antes del contrato y el control debe continuar después."),
    ],
    ctx=("abc", "El Estado de un país de ejemplo exige a las empresas de energía publicar sus tarifas y sus costos cada año. ¿Qué dimensión ética refuerza principalmente?", "La transparencia", "El secreto comercial absoluto", "La competencia perfecta", "Publicar información permite que otros controlen y comparen."),
    sc=[
        ("¿Es lo mismo regular que estatizar?", "No: regular es fijar y vigilar reglas, sin ser dueño del servicio", "El Estado puede regular a empresas privadas."),
        ("En Economía y sociedad: ¿qué es la captura regulatoria?", "Cuando el regulador favorece a las empresas que debería vigilar", "Es uno de los riesgos de la regulación."),
        ("Nombra tres criterios para evaluar una regulación.", "Acceso, precio, calidad, eficiencia, sostenibilidad o equidad", "Son criterios de comparación entre opciones."),
    ],
    op=("Evalúa las cuatro opciones de la Ficha 20. Haz una tabla con los criterios acceso, tarifa, calidad y sostenibilidad financiera (marca con alto, medio o bajo a partir de los datos de la ficha y señala cuando no hay datos). "
        "Elige una opción, explica el valor que priorizas, presenta el argumento más fuerte contra tu elección y declara qué dato falta para decidir mejor.",
        "Elijo la Opción 2 priorizando el acceso a un servicio esencial. En contra: la ganancia baja podría reducir la inversión. Falta saber los costos reales de la empresa para saber si $600 es sostenible.",
        ["completa la tabla sin inventar datos", "justifica la elección con un valor", "presenta el argumento contrario con fuerza", "declara un dato que falta"],
        ["tabla de comparación y cuatro frases"],
        ["inventar datos que la ficha no entrega", "no presentar el mejor argumento contrario", "decir que su elección es la única posible"],
        "Pregunta: «¿qué le diría alguien que prioriza otro valor?». Pide que escriba su mejor objeción."),
    reinforce="Elige un servicio esencial de tu comuna y escribe qué podría regularse y qué riesgo tendría esa regulación.",
    extend="Compara dos posturas sobre regular menos y regular más un mercado, presentando el argumento más fuerte de cada una sin elegir.",
)
