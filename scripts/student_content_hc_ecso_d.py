"""Economía y sociedad (electivo HC, 3.º y 4.º medio): OAC-06 (comercio internacional) y OAC-08 (desafíos actuales de las economías), clases 1 a 6 de cada uno. Países, empresas, cifras y fuentes de ejemplo, ficticios."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma, papel o cuaderno y, si quieres, una calculadora simple. No se necesita computador ni internet: cada caso, tabla y dato está escrito en el enunciado. "
             "Los países, empresas, productos y cifras son ficticios o «de ejemplo» y sirven para practicar el razonamiento económico; no representan a ningún país real ni son datos oficiales. "
             "Las posturas sobre comercio, ambiente y equidad se presentan con sus argumentos, sin tomar partido: tu tarea es analizarlas y evaluarlas con criterios. "
             "Este cuaderno no entrega asesoría financiera ni recomienda inversiones. El dinero está en pesos chilenos cuando no se indica otra cosa.")
build = make_build(MATERIALS)

O6 = "HI-ECSO-3y4-OAC-06"
O8 = "HI-ECSO-3y4-OAC-08"

# ============================================================ OAC-06, clase 1
F = ("Ficha 31 (país de ejemplo, ficticio). El País Alfa exporta frutas y vino, e importa maquinaria y combustible. Datos de ejemplo (en miles de millones de unidades monetarias, u.m.): "
     "año 1, exportaciones 120 e importaciones 100; año 2, exportaciones 110 e importaciones 130.")
build(
    O6, 1, F,
    use="Aprenderé por qué comercian los países, qué son las exportaciones, las importaciones y la balanza comercial, y qué beneficios y desafíos trae la apertura al comercio.",
    prior=["Conozco el PIB y el costo de oportunidad.", "Sé restar cantidades y calcular porcentajes.", "Sé qué es un mercado y qué es la oferta y la demanda."],
    explain=[
        "El comercio internacional es el intercambio de bienes y servicios entre países. Una exportación es un bien o servicio que un país vende a otro. Una importación es un bien o servicio que un país compra a otro. La balanza comercial es la diferencia entre las exportaciones y las importaciones: si es positiva hay superávit comercial, y si es negativa, déficit comercial.",
        "Los países comercian por varias razones. Tienen recursos, clima y tierras distintos, por lo que a cada uno le resulta más barato producir ciertos bienes. Tienen tecnologías y habilidades diferentes. Producir en gran cantidad baja el costo por unidad, lo que se llama economías de escala, y exige vender a un mercado más grande que el propio. Y los consumidores quieren más variedad que la que un solo país produce.",
        "El comercio tiene beneficios, como más variedad, precios menores y acceso a mercados más grandes, y también desafíos, como la competencia para algunas empresas locales y la dependencia de lo que ocurra en otros países. Un déficit o un superávit comercial no es bueno ni malo por sí solo: depende de qué se importa (por ejemplo, maquinaria que aumenta la producción futura) y de cómo se financia. Chile es una economía muy abierta al comercio, pero los datos de esta clase son de ejemplo.",
    ],
    vocab=[("comercio internacional", "intercambio de bienes y servicios entre países"), ("exportación", "bien o servicio que un país vende a otro"), ("importación", "bien o servicio que un país compra a otro"), ("balanza comercial", "exportaciones menos importaciones"), ("apertura comercial", "grado en que un país permite y participa en el comercio exterior"), ("economías de escala", "costo por unidad que baja al producir más")],
    worked=[
        ("Calcular la balanza", "Un país de ejemplo exportó 80 e importó 95. ¿Cuál es su balanza comercial y qué indica?",
         ["Exportaciones menos importaciones: 80 menos 95 da menos 15.", "El resultado es negativo: déficit comercial."],
         "Menos 15: déficit comercial"),
        ("Identificar la razón del comercio", "Un país de ejemplo de clima cálido produce plátanos baratos y los vende a países fríos. ¿Qué razón del comercio ilustra?",
         ["El clima es un recurso natural distinto entre países.", "Por el clima, le resulta más barato producir plátanos."],
         "Diferencias de recursos y clima"),
    ],
    mistakes=[("Creer que un superávit comercial siempre es bueno y un déficit siempre malo.", "Se simplifica sin mirar qué se importa ni cómo se financia.", "Analiza el contenido de las importaciones y el financiamiento antes de juzgar."),
              ("Pensar que el comercio solo beneficia a quien exporta.", "Se olvida a quienes consumen e importan.", "Ambos lados del intercambio pueden ganar variedad, precio y acceso.")],
    T=[
        ("abc", "{F} ¿Cuál de estos bienes importa País Alfa?", "Maquinaria", "Frutas", "Vino", "La ficha dice que exporta frutas y vino e importa maquinaria y combustible."),
        ("=", "{F} ¿Cuál fue la balanza comercial del año 1 (en miles de millones de u.m.)?", "120-100", "Se restan las importaciones a las exportaciones."),
        ("abc", "En Economía y sociedad: ¿qué es una exportación?", "Un bien o servicio que un país vende a otro", "Un bien que un país compra a otro", "Un impuesto al comercio", "Exportar significa vender bienes o servicios al exterior."),
        ("=", "{F} ¿Cuál fue la balanza comercial del año 2? (un número negativo indica déficit)", "110-130", "Se restan las importaciones a las exportaciones."),
        ("abc", "En Economía y sociedad: ¿qué es una importación?", "Un bien o servicio que un país compra a otro", "Un bien que un país vende a otro", "Un subsidio", "Importar significa comprar bienes o servicios al exterior."),
        ("abc", "{F} En el año 2, ¿hubo superávit o déficit comercial?", "Déficit, porque las importaciones superaron a las exportaciones", "Superávit, porque exportó mucho", "Equilibrio exacto", "Las importaciones de 130 son mayores que las exportaciones de 110."),
        ("abc", "Un país con mucho sol produce uvas muy baratas y exporta vino. ¿Qué razón del comercio ilustra?", "Diferencias de clima y recursos", "Economías de escala", "Mayor variedad de gustos", "El clima favorece cierta producción y la hace más barata."),
        ("abc", "Un país pequeño compra autos al exterior porque fabricarlos solo para sus pocos habitantes saldría carísimo. ¿Qué razón ilustra?", "Economías de escala", "Diferencias de clima", "Un precio máximo", "Producir en gran cantidad baja el costo por unidad, y un mercado pequeño no lo permite."),
        ("{F} Si el año 3 País Alfa exporta 130 e importa 130, ¿cuál es su balanza comercial?", "0", "Cuando exportaciones e importaciones son iguales, la diferencia es cero."),
        ("{F} Un diputado dice: «Un déficit comercial es siempre malo». ¿Qué matiz harías?", "No es bueno ni malo por sí solo: depende de qué se importa y cómo se financia", "Por ejemplo, importar maquinaria puede aumentar la producción futura."),
        ("{F} El comercio da más variedad a los consumidores y más competencia a las empresas locales. ¿Cuál es un beneficio y cuál un posible costo?", "La variedad es un beneficio; la competencia puede ser un costo para algunas empresas locales", "Los efectos recaen de distinta forma en consumidores y empresas."),
        ("=", "{F} Las exportaciones del año 1 suben 10%. ¿Cuánto serían?", "120*110/100", "Subir 10% equivale a multiplicar por 110 y dividir por 100."),
        ("=", "{F} Con esas exportaciones y las importaciones del año 1 sin cambio, ¿cuál sería la nueva balanza?", "132-100", "Se restan las importaciones a las nuevas exportaciones."),
    ],
    ctx=("abc", "Una familia de ejemplo compra un teléfono fabricado en otro país porque en su país nadie lo produce a un precio similar. ¿Qué beneficio del comercio ilustra?", "Acceso a más variedad y a mejores precios", "Un superávit comercial siempre bueno", "Un impuesto a la importación", "Importar permite acceder a bienes que el país no produce o produce más caro."),
    sc=[
        ("¿Cómo se calcula la balanza comercial?", "Exportaciones menos importaciones", "Un resultado negativo de la balanza es un déficit comercial."),
        ("Nombra dos razones por las que comercian los países.", "Diferencias de recursos o clima, tecnología, economías de escala o variedad", "Son motivos que explican el intercambio."),
        ("¿Es un déficit comercial siempre malo?", "No: depende de qué se importa y cómo se financia", "Debe analizarse con más datos sobre qué se importa."),
    ],
    op=("Elige un producto de tu casa que haya sido importado (por ejemplo, un teléfono, una prenda o una fruta) y completa una ficha: (1) por qué crees que el país de origen lo produce más barato, usando una de las razones del comercio; "
        "(2) quién gana con esa importación y quién podría perder; (3) un dato de ejemplo con una balanza comercial de dos años (inventa cifras rotuladas «de ejemplo») y cuál fue su resultado.",
        "Teléfono. (1) Economías de escala: se fabrica en cantidades enormes. (2) Gana el consumidor con variedad; pierden fabricantes locales si hubiera. (3) Año 1, exportaciones 90 e importaciones 80 (de ejemplo): superávit de 10.",
        ["usa una razón del comercio de manera adecuada", "identifica ganadores y posibles perdedores", "calcula una balanza con cifras rotuladas como de ejemplo"],
        ["ficha de tres partes"],
        ["decir que el comercio solo beneficia al exportador", "inventar cifras sin rotular", "calcular la balanza al revés"],
        "Pregunta: «¿qué exporta y qué importa tu país en este ejemplo?». Con eso verifica el signo de la balanza."),
    reinforce="Escribe tres productos que se exporten y tres que se importen en un país de ejemplo de tu elección.",
    extend="Explica por qué importar maquinaria puede producir efectos distintos en la balanza hoy y en la producción futura.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 32 (países de ejemplo, ficticios). Horas de trabajo necesarias para producir una unidad: País Alfa, 2 horas por vino y 4 horas por tela. País Beta, 6 horas por vino y 6 horas por tela. "
     "Cada país dispone de 120 horas de trabajo y, si no comercian, dedican la mitad a cada bien.")
build(
    O6, 2, F,
    use="Aprenderé la diferencia entre ventaja absoluta y ventaja comparativa, a calcularlas con costos de oportunidad y a explicar por qué el comercio puede convenir incluso a un país que produce mejor todos los bienes.",
    prior=["Sé qué es el costo de oportunidad.", "Sé qué son las exportaciones e importaciones.", "Sé dividir y comparar razones."],
    explain=[
        "Un país tiene ventaja absoluta en un bien cuando lo produce usando menos recursos (por ejemplo, menos horas de trabajo) que otro país. Un país tiene ventaja comparativa en un bien cuando su costo de oportunidad de producirlo es menor que el del otro país. El costo de oportunidad se calcula con una razón: para el bien X, es la cantidad del otro bien a la que se renuncia por cada unidad de X.",
        "Con horas por unidad: si un país tarda 2 horas por vino y 4 horas por tela, en las 4 horas que le toma una tela podría hacer 2 vinos; entonces el costo de oportunidad de una tela es 2 vinos, y el de un vino es 2 dividido por 4, o sea 0,5 telas. Se compara ese número entre países: el que tiene menor costo de oportunidad en un bien tiene ventaja comparativa en él.",
        "La idea de David Ricardo, economista clásico, es que ambos países pueden ganar si cada uno se especializa en el bien en que tiene ventaja comparativa y luego intercambian, incluso si uno de ellos tiene ventaja absoluta en todo. El modelo supone cosas simples (dos países, dos bienes, sin costos de transporte), y en la práctica los resultados dependen de otros factores. Quienes critican el modelo señalan que ignora a los trabajadores que pierden su empleo al cambiar la estructura productiva.",
    ],
    vocab=[("ventaja absoluta", "producir un bien con menos recursos que otro país"), ("ventaja comparativa", "producir un bien con menor costo de oportunidad que otro país"), ("especialización", "dedicarse a producir el bien en que se tiene ventaja comparativa"), ("costo de oportunidad", "lo que se deja de producir por producir una unidad más de otro bien"), ("términos de intercambio", "relación entre precios de exportaciones e importaciones"), ("David Ricardo", "economista clásico asociado a la teoría de la ventaja comparativa")],
    worked=[
        ("Calcular un costo de oportunidad", "En un país de ejemplo, un pan toma 1 hora y un pastel toma 3 horas. ¿Cuál es el costo de oportunidad de un pastel, en panes?",
         ["En las 3 horas de un pastel se podrían hacer 3 panes.", "Costo de oportunidad de un pastel: 3 panes."],
         "3 panes"),
        ("Identificar la ventaja comparativa", "País X: costo de oportunidad de un queso, 2 jamones. País Y: costo de oportunidad de un queso, 3 jamones. ¿Quién tiene ventaja comparativa en queso?",
         ["Compara los costos de oportunidad: 2 y 3.", "El menor es el de X, por lo que X tiene ventaja comparativa en queso."],
         "País X"),
    ],
    mistakes=[("Confundir ventaja absoluta con ventaja comparativa.", "Se mira solo quién produce con menos horas.", "La comparativa se define por el costo de oportunidad."),
              ("Creer que un país que produce todo mejor no necesita comerciar.", "Se ignora el costo de oportunidad.", "Le conviene especializarse donde su costo de oportunidad es menor.")],
    T=[
        ("=", "{F} ¿Cuál es el costo de oportunidad de un vino en País Alfa, medido en telas?", "2/4", "Dos horas del vino entre cuatro horas de una tela."),
        ("=", "{F} ¿Cuál es el costo de oportunidad de una tela en País Alfa, medido en vinos?", "4/2", "Cuatro horas de la tela entre dos horas de un vino."),
        ("=", "{F} ¿Cuál es el costo de oportunidad de un vino en País Beta, medido en telas?", "6/6", "Seis horas del vino entre seis horas de una tela."),
        ("abc", "{F} ¿Qué país tiene ventaja absoluta en vino?", "País Alfa, porque usa menos horas", "País Beta", "Ninguno", "Alfa necesita 2 horas y Beta 6."),
        ("abc", "{F} ¿Qué país tiene ventaja comparativa en vino?", "País Alfa, con costo de oportunidad 0,5 telas frente a 1", "País Beta", "Ninguno", "El menor costo de oportunidad en vino es el de Alfa."),
        ("abc", "{F} ¿Qué país tiene ventaja comparativa en tela?", "País Beta, con costo de oportunidad de 1 vino frente a 2", "País Alfa", "Ninguno", "El costo de oportunidad de una tela es 1 vino en Beta y 2 vinos en Alfa."),
        ("abc", "En Economía y sociedad: ¿qué es la ventaja comparativa?", "Producir un bien con menor costo de oportunidad que otro país", "Producir un bien con menos horas de trabajo", "Vender un bien más caro", "Se define por el costo de oportunidad, no por las horas."),
        ("=", "{F} Si Alfa dedicara sus 120 horas solo al vino, ¿cuántos vinos produciría?", "120/2", "Se dividen las horas disponibles por las horas por vino."),
        ("=", "{F} Si Beta dedicara sus 120 horas solo a la tela, ¿cuántas telas produciría?", "120/6", "Se dividen las horas disponibles por las horas por tela."),
        ("{F} Alfa produce vino y tela con menos horas que Beta (2 contra 6 y 4 contra 6). ¿Por qué igual le conviene especializarse en vino y comprar tela?", "Porque su costo de oportunidad de la tela (2 vinos) es mayor que el de Beta (1 vino)", "Conviene especializarse donde el costo de oportunidad es menor."),
        ("abc", "{F} Se intercambian a 1 vino por 0,75 telas. Alfa renuncia a 0,5 telas por cada vino que produce. ¿Le conviene vender vino a ese precio?", "Sí, porque recibe 0,75 telas por un vino que le cuesta 0,5 telas", "No, porque recibe menos de lo que le costó", "Es indiferente", "Recibe más de lo que renuncia."),
        ("abc", "{F} Con ese mismo intercambio, Beta puede obtener un vino pagando 0,75 telas, aunque producirlo le cuesta 1 tela. ¿Le conviene comprarlo?", "Sí, porque paga menos de lo que le costaría producirlo", "No, porque paga más", "Es indiferente", "Producirlo le cuesta 1 tela y comprarlo, 0,75."),
        ("abc", "Alguien dice: «Alfa no debería comerciar con Beta porque ya es mejor en vino». ¿Qué respuesta usa lo aprendido?", "Importa el costo de oportunidad y no solo quién produce con menos horas", "Tiene razón, quien produce con menos horas no necesita comerciar", "El costo de oportunidad solo importa dentro de un país", "La ventaja comparativa justifica el intercambio."),
    ],
    ctx=("abc", "Un panadero hace un pan en 1 hora o un pastel en 2 horas. Su ayudante hace un pan en 2 horas o un pastel en 3 horas. El costo de oportunidad de un pastel es 2 panes para el panadero y 1,5 panes para el ayudante. ¿En qué debería especializarse el ayudante?", "En pasteles, porque su costo de oportunidad es menor", "En panes, porque tarda más", "En ninguno", "Menor costo de oportunidad (1,5 contra 2) indica ventaja comparativa en pasteles."),
    sc=[
        ("En Economía y sociedad: ¿qué es la ventaja absoluta?", "Producir un bien con menos recursos que otro país", "Se mide por horas o recursos usados."),
        ("¿Cómo se compara la ventaja comparativa entre países?", "Con los costos de oportunidad", "El menor costo de oportunidad gana."),
        ("¿Qué crítica se hace al modelo de Ricardo?", "Ignora a los trabajadores que pierden su empleo y supone cosas simples", "Es un modelo con supuestos fuertes."),
    ],
    op=("Resuelve un caso de ejemplo. País Luna: 3 horas por fruta y 6 horas por zapato. País Sol: 4 horas por fruta y 4 horas por zapato. "
        "Calcula el costo de oportunidad de una fruta y de un zapato en cada país, indica en qué tiene ventaja comparativa cada uno, y escribe una frase que explique en qué debería especializarse cada país. "
        "Luego escribe un límite del modelo (por ejemplo, qué supone).",
        "Luna: fruta = 0,5 zapato; zapato = 2 frutas. Sol: fruta = 1 zapato; zapato = 1 fruta. Luna: fruta. Sol: zapato. Límite: supone solo dos países y dos bienes.",
        ["calcula bien los cuatro costos de oportunidad", "asigna la ventaja comparativa a cada país", "justifica la especialización", "nombra un límite del modelo"],
        ["cuadro con cuatro cálculos y dos frases"],
        ["comparar horas en lugar de costos de oportunidad", "invertir las razones", "no declarar ningún límite"],
        "Pregunta: «a cuánto renuncia cada país por cada unidad?». Con eso verifica los cálculos."),
    reinforce="Rehace los costos de oportunidad de la Ficha 32 con una calculadora y escribe una frase que explique cada resultado.",
    extend="Explica por qué la especialización puede traer beneficios y también costos para ciertos trabajadores.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 33 (país de ejemplo, ficticio). País Alfa exporta vino e importa maquinaria. Año 1: un lote de vino se vende a $100 y una máquina cuesta $50. Año 2: el lote de vino se vende a $90 y la máquina cuesta $60. "
     "Índices de precios de ejemplo (año 1 = 100): año 2, precios de exportación 90 y de importación 120. Año 3: precios de exportación 130 y de importación 100.")
build(
    O6, 3, F,
    use="Aprenderé qué son los términos de intercambio, cómo se calculan, qué efectos tienen en un país que exporta pocos productos y cómo se discuten las perspectivas sobre la especialización.",
    prior=["Sé qué son exportaciones e importaciones.", "Conozco la ventaja comparativa.", "Sé dividir y calcular índices."],
    explain=[
        "Los términos de intercambio son la relación entre los precios de lo que un país exporta y los precios de lo que importa. Se pueden expresar de dos maneras: cuántas unidades importadas se pueden comprar con una unidad exportada (si un lote de vino a $100 compra máquinas de $50, compra 2), o como un índice: (índice de precios de exportación dividido por el índice de precios de importación) por 100.",
        "Si el índice sube, los términos de intercambio mejoran: con la misma cantidad exportada se compra más. Si baja, empeoran o se deterioran. Cuando los términos de intercambio mejoran, el país puede comprar más con lo que vende; cuando empeoran, necesita exportar más para importar lo mismo. Estos precios cambian, y para países que exportan pocos productos, como materias primas, las variaciones pueden ser grandes.",
        "Hay perspectivas distintas. Algunas personas sostienen que la especialización en pocos productos expone al país a precios volátiles y que conviene diversificar. Otras sostienen que la especialización en el bien con ventaja comparativa es eficiente y que se puede reducir el riesgo con ahorro y política económica. Ambas presentan argumentos; un análisis serio usa datos de varios años y reconoce los límites de cada indicador.",
    ],
    vocab=[("términos de intercambio", "relación entre los precios de exportación y de importación"), ("índice de precios de exportación", "número que muestra cómo cambian los precios de lo que se exporta"), ("deterioro de los términos de intercambio", "baja de ese índice"), ("diversificar", "producir y exportar productos más variados"), ("volatilidad", "variaciones grandes y repentinas"), ("materia prima", "recurso natural poco procesado")],
    worked=[
        ("Calcular cuánto se compra", "Un lote de un producto de ejemplo se vende a $200 y una máquina cuesta $40. ¿Cuántas máquinas compra un lote?",
         ["Divide el precio del lote por el precio de la máquina.", "200 dividido por 40."],
         "5 máquinas"),
        ("Calcular el índice", "Precios de exportación 150 y de importación 100, ambos con base 100. ¿Cuál es el índice de términos de intercambio y qué indica?",
         ["Índice = 150 dividido por 100, por 100.", "Es 150: los términos de intercambio mejoraron."],
         "150: mejoraron"),
    ],
    mistakes=[("Creer que si suben los precios de exportación siempre mejoran los términos de intercambio.", "Se olvida de mirar los precios de importación.", "Compara ambos: lo que importa es su relación."),
              ("Pensar que un deterioro significa que el país exporta menos.", "Se confunde precios con cantidades.", "Se refiere a la relación de precios, no a las cantidades.")],
    T=[
        ("=", "{F} Año 1: ¿cuántas máquinas compraba un lote de vino? (precio del lote entre precio de la máquina)", "100/50", "Se divide el precio del lote por el de la máquina."),
        ("=", "{F} Año 2: ¿cuántas máquinas compra un lote de vino?", "90/60", "Se divide el precio del lote por el de la máquina."),
        ("abc", "{F} Entre el año 1 y el año 2, ¿cómo cambiaron los términos de intercambio de Alfa?", "Empeoraron, porque un lote compra menos máquinas", "Mejoraron", "Quedaron igual", "Se pasó de comprar 2 a comprar 1,5 máquinas."),
        ("=", "{F} Año 2: ¿cuál es el índice de términos de intercambio?", "90/120*100", "Se divide el índice de exportación por el de importación y se multiplica por 100."),
        ("=", "{F} Año 3: ¿cuál es el índice de términos de intercambio?", "130/100*100", "Se divide el índice de exportación por el de importación y se multiplica por 100."),
        ("abc", "{F} Entre el año 2 y el año 3, ¿cómo cambiaron los términos de intercambio?", "Mejoraron, porque el índice subió de 75 a 130", "Empeoraron", "Quedaron igual", "Subieron los precios de exportación y bajaron los de importación."),
        ("abc", "En Economía y sociedad: ¿qué son los términos de intercambio?", "La relación entre los precios de lo que un país exporta y de lo que importa", "El total de exportaciones", "Un impuesto al comercio", "Comparan los precios de exportación e importación."),
        ("abc", "Si los términos de intercambio empeoran, ¿qué sucede con la capacidad de compra del país?", "Con lo mismo que exporta, compra menos importaciones", "Compra más importaciones", "No cambia", "Es el significado de un deterioro."),
        ("{F} Un economista dice: «Si el precio del vino baja, el país necesita exportar más vino para comprar las mismas máquinas». ¿Se cumple con el cambio del año 1 al año 2?", "Sí: antes un lote compraba 2 máquinas y ahora 1,5", "Para comprar las mismas máquinas hay que vender más lotes."),
        ("abc", "{F} Un país que exporta casi solo un producto, ¿qué riesgo enfrenta con los términos de intercambio?", "Que el precio de ese producto cambie bruscamente y afecte todo su ingreso", "Que las máquinas dejen de existir", "Que el comercio sea ilegal", "Depende de un solo precio, lo que lo hace volátil."),
        ("abc", "Un defensor de diversificar dice: «Con más productos exportados, el país depende menos de un solo precio». ¿Qué tipo de argumento es?", "Un argumento sobre reducir el riesgo", "Un argumento sobre la inflación", "Un argumento sobre el monopolio", "Más productos reducen la dependencia de un solo precio."),
        ("abc", "Un defensor de la especialización dice: «Producir el bien con ventaja comparativa es más eficiente». ¿Qué información de varios años ayudaría a evaluarlo?", "La evolución del precio del bien y de los ingresos del país", "El número de empresas exportadoras", "El número de habitantes del país", "Se necesita ver precios y resultados en el tiempo."),
        ("En Chile, por ejemplo, el precio del cobre influye en los ingresos de exportación. ¿Qué concepto de la clase se relaciona con eso?", "Términos de intercambio y volatilidad", "Los precios de materias primas pueden variar mucho y modifican lo que el país puede comprar."),
    ],
    ctx=("abc", "Un país de ejemplo exporta cobre y su precio sube mucho, mientras el precio de lo que importa casi no cambia. ¿Qué ocurre con sus términos de intercambio?", "Mejoran", "Empeoran", "Quedan igual", "El índice de exportación sube más que el de importación."),
    sc=[
        ("¿Cómo se calcula el índice de términos de intercambio?", "Índice de exportación entre índice de importación, por 100", "El índice resume la relación entre precios de exportación e importación."),
        ("¿Qué significa que los términos de intercambio mejoren?", "Que con lo mismo que se exporta se compra más", "Aumenta el poder de compra externo del país."),
        ("En Economía y sociedad: ¿qué es la volatilidad?", "Variaciones grandes y repentinas", "Afecta a quienes dependen de pocos precios."),
    ],
    op=("Analiza este caso de ejemplo. País Colina exporta frutos secos e importa tractores. Año 1: lote de frutos secos $300 y tractor $100. Año 2: lote $240 y tractor $120. Año 3: lote $360 y tractor $90. "
        "Calcula cuántos tractores compra un lote cada año, señala en qué años mejoraron o empeoraron los términos de intercambio, y escribe un argumento a favor de diversificar y uno a favor de mantener la especialización, sin elegir.",
        "Año 1: 3; año 2: 2; año 3: 4. Empeoraron del año 1 al 2; mejoraron del 2 al 3. A favor de diversificar: reduce la dependencia de un solo precio. A favor de especializarse: usa su ventaja comparativa.",
        ["calcula los tres años", "identifica mejoras y empeoramientos", "presenta dos argumentos equilibrados"],
        ["tres cálculos y dos argumentos"],
        ["dividir al revés", "confundir precios y cantidades", "tomar partido sin argumentos"],
        "Pregunta: «¿cuántos tractores compra un lote?». Con eso compara años."),
    reinforce="Calcula los términos de intercambio como índice (exportación entre importación por 100) para los tres años del caso.",
    extend="Explica cómo la volatilidad de los precios puede afectar la planificación del presupuesto de un país que exporta un solo producto.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 34 (mercado de ejemplo, ficticio). Zapatos en el País Alfa, por mes. El precio mundial es $20.000 el par. Con ese precio, los consumidores compran 800 pares y los productores locales ofrecen 200. "
     "Si el Estado fija un arancel (impuesto a las importaciones) de 25%, el precio local pasa a $25.000: se compran 600 pares y la producción local sube a 300. Sin comercio, el precio local sería $30.000, con 400 pares comprados y producidos.")
build(
    O6, 4, F,
    use="Aprenderé qué son los aranceles, las cuotas y los tratados de libre comercio, cómo afectan a precios y cantidades, y qué argumentos usan quienes defienden más o menos protección.",
    prior=["Sé qué son importaciones y exportaciones.", "Conozco el efecto de un impuesto sobre un precio.", "Sé calcular porcentajes."],
    explain=[
        "Un arancel es un impuesto a las importaciones. Encarece el bien importado, así que el precio local sube, los consumidores compran menos, los productores locales venden más y el Estado recauda. Una cuota es un límite a la cantidad que se puede importar. El proteccionismo es la política que protege a los productores locales con aranceles, cuotas u otras barreras. El libre comercio, en cambio, busca reducir esas barreras.",
        "Un tratado de libre comercio es un acuerdo entre países para reducir o eliminar aranceles y otras barreras entre ellos. Algunas alianzas van más allá: un bloque comercial coordina reglas y aranceles comunes. Chile ha firmado numerosos tratados comerciales con distintos países y bloques, por lo que sus productos pagan menos aranceles en varios mercados.",
        "Las posturas difieren. Quienes defienden el libre comercio destacan precios menores, más variedad y eficiencia. Quienes defienden alguna protección destacan el empleo local, el desarrollo de industrias nuevas y la seguridad de abastecimiento. Ambas posturas tienen argumentos, y los efectos dependen del producto, del tamaño de la economía y de cómo se compensa a quienes pierden. La decisión incluye valores, no solo cálculos.",
    ],
    vocab=[("arancel", "impuesto a las importaciones"), ("cuota", "límite a la cantidad que se puede importar"), ("proteccionismo", "política que protege a los productores locales de la competencia externa"), ("libre comercio", "comercio con pocas barreras"), ("tratado de libre comercio", "acuerdo para reducir o eliminar aranceles entre países"), ("bloque comercial", "grupo de países con reglas y aranceles coordinados")],
    worked=[
        ("Calcular el precio con arancel", "El precio mundial de un bien de ejemplo es $1.000 y el Estado fija un arancel de 20%. ¿Cuál es el nuevo precio local?",
         ["El arancel es 20% de 1.000, es decir 200.", "El precio pasa a 1.200."],
         "$1.200"),
        ("Calcular las importaciones", "A un precio de ejemplo, los consumidores compran 500 unidades y los productores locales ofrecen 150. ¿Cuántas se importan?",
         ["Lo que no ofrece el productor local se importa.", "500 menos 150."],
         "350 unidades"),
    ],
    mistakes=[("Creer que un arancel lo paga el país exportador.", "Se olvida que sube el precio en el mercado local.", "En general el arancel encarece el bien para los compradores del país que lo aplica."),
              ("Pensar que el proteccionismo no tiene costos.", "Se miran solo los productores protegidos.", "Los consumidores pagan más y puede haber represalias.")],
    T=[
        ("=", "{F} Con libre comercio, ¿cuántos pares se importan al mes (consumo menos producción local)?", "800-200", "Se restan los pares producidos localmente a los comprados."),
        ("=", "{F} Con el arancel de 25%, ¿cuántos pares se importan al mes?", "600-300", "Se restan los pares producidos localmente a los comprados."),
        ("abc", "{F} ¿En cuánto sube el precio local con el arancel respecto del precio mundial?", "$5.000", "$10.000", "$25.000", "El precio pasa de 20.000 a 25.000, es decir 5.000 más."),
        ("=", "{F} Con el arancel de 25%, ¿cuánto recauda el Estado por mes en pesos? (importaciones por arancel de $5.000 por par)", "300*5000", "Se multiplican los pares importados por el arancel por par."),
        ("abc", "En Economía y sociedad: ¿qué es un arancel?", "Un impuesto a las importaciones", "Un impuesto a las exportaciones", "Un subsidio a los productores locales", "Encarece el bien que viene del exterior."),
        ("abc", "{F} ¿Quiénes ganan con el arancel?", "Los productores locales, que venden más, y el Estado, que recauda", "Los consumidores, que pagan menos", "Los exportadores del país extranjero", "La producción local sube de 200 a 300 y el Estado recauda."),
        ("abc", "{F} ¿Quiénes pierden con el arancel?", "Los consumidores, que pagan más y compran menos", "Los productores locales", "El Estado", "El precio sube y la cantidad comprada baja de 800 a 600."),
        ("abc", "En Economía y sociedad: ¿qué es una cuota de importación?", "Un límite a la cantidad que se puede importar", "Un impuesto a la exportación", "Una ayuda al consumidor", "Restringe la cantidad en vez de encarecer."),
        ("abc", "En Economía y sociedad: ¿qué es un tratado de libre comercio?", "Un acuerdo para reducir o eliminar aranceles entre países", "Un acuerdo para subir los aranceles", "Una ley interna sin otros países", "Busca facilitar el comercio entre las partes."),
        ("{F} Sin comercio el precio sería $30.000 con 400 pares. ¿Cuántos pares más compran los consumidores con libre comercio?", "400 pares más", "Con libre comercio compran 800, frente a 400."),
        ("abc", "{F} Un defensor de proteger la industria local dice que el arancel conserva empleos. ¿Qué dato de la ficha lo respalda?", "La producción local sube de 200 a 300 pares", "El precio mundial es $20.000", "Los consumidores compran 800 pares", "Más producción local sostiene más empleo."),
        ("abc", "{F} Un defensor del libre comercio dice que el arancel encarece la vida de las familias. ¿Qué dato lo respalda?", "El precio local pasa de $20.000 a $25.000", "La producción local sube", "El Estado recauda", "El precio más alto lo pagan los consumidores."),
        ("abc", "«El país debería eliminar todos los aranceles» es una afirmación…", "Normativa, porque dice qué debería hacerse según valores", "Positiva, porque se verifica con datos", "Falsa", "Contiene un deber, no un hecho."),
    ],
    ctx=("abc", "Un país de ejemplo firma un tratado con otro y ambos eliminan aranceles a las frutas. Los productores de fruta exportan más y los consumidores compran fruta importada más barata. ¿Qué tipo de política es?", "Libre comercio mediante un tratado", "Proteccionismo", "Una cuota", "Ambos países reducen barreras entre las partes del tratado."),
    sc=[
        ("¿Qué efecto tiene un arancel sobre el precio local?", "Lo sube", "El arancel encarece el bien que viene del exterior."),
        ("En Economía y sociedad: ¿qué es el proteccionismo?", "La política que protege a los productores locales de la competencia externa", "Usa aranceles, cuotas u otras barreras."),
        ("Nombra un argumento del libre comercio y uno de la protección.", "Libre comercio: precios menores y variedad; protección: empleo local o industrias nuevas", "Ambas posturas tienen argumentos que se evalúan con datos."),
    ],
    op=("Analiza esta propuesta de ejemplo. El País Alfa evalúa un arancel de 30% a las bicicletas importadas, cuyo precio mundial es $100.000. Datos de ejemplo: con libre comercio se compran 5.000 bicicletas y la producción local es 1.000; con el arancel, el precio local sube a $130.000, se compran 4.000 y la producción local es 2.000. "
        "Calcula el precio local con el arancel, las importaciones en cada caso, lo que recauda el Estado y escribe un argumento a favor y uno en contra del arancel, sin tomar partido.",
        "Precio: 130.000. Importaciones: 4.000 con libre comercio y 2.000 con arancel. Recaudación: 2.000 por 30.000 son 60.000.000. A favor: la producción local sube de 1.000 a 2.000. En contra: el precio sube 30.000 para las familias.",
        ["calcula el precio con el arancel", "calcula las importaciones en ambos casos", "calcula la recaudación", "presenta argumentos de ambas posturas"],
        ["cálculos y dos argumentos"],
        ["calcular el arancel sobre el precio equivocado", "olvidar restar la producción local", "tomar partido sin argumentos"],
        "Pregunta: «¿cuántas se importan?». Pide restar la producción local de lo comprado."),
    reinforce="Con la Ficha 34, escribe tres cifras que cambian al pasar del libre comercio al arancel y qué indican.",
    extend="Compara los argumentos para proteger una industria nueva y los argumentos para dejarla competir desde el inicio.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 35 (caso de ejemplo, ficticio). Valle Seco es una ciudad de 900 empleos, de los cuales 300 están en una fábrica de calzado. El país abre su mercado a zapatos importados y el precio baja de $30.000 a $20.000 el par. "
     "Los consumidores del país ahorran en conjunto $400 millones al mes. La fábrica reduce su producción y despide a 200 trabajadores, que ganaban $500.000 al mes cada uno. Se discute un programa de reconversión laboral que cuesta $60 millones al mes.")
build(
    O6, 5, F,
    use="Aprenderé a analizar el impacto del comercio en economías locales y nacionales: quiénes ganan y quiénes pierden, cómo medirlo y qué políticas se discuten para compensar.",
    prior=["Conozco aranceles, ventajas comparativas y términos de intercambio.", "Sé calcular costos y beneficios.", "Sé distinguir lo positivo de lo normativo."],
    explain=[
        "El comercio internacional produce ganancias para el conjunto del país, pero no se reparten por igual. Los consumidores suelen ganar con precios menores y más variedad; los productores que compiten con importaciones pueden perder ventas y empleos; los exportadores ganan acceso a mercados más grandes. Por eso se habla de ganadores y perdedores, y se distinguen el impacto nacional (el balance total) y el impacto local (lo que ocurre en una ciudad que depende de una industria).",
        "Un ejercicio útil es comparar el beneficio total con el costo total, y luego mirar cómo se distribuyen. Aunque el balance sea positivo, hay familias que enfrentan pérdidas concentradas y difíciles, y comunidades enteras que se resienten. Las políticas de compensación y reconversión, como la capacitación, el apoyo a la reubicación y los seguros de cesantía, buscan que quienes pierden puedan adaptarse. Su costo y eficacia se discuten.",
        "Las posturas difieren. Algunas personas ponen el acento en las ganancias totales y en la eficiencia; otras, en proteger a las comunidades afectadas y en la justicia con quienes pierden. Estas posturas se basan en valores distintos, y un análisis serio presenta los números y también el modo en que se reparten, sin esconder a los afectados ni exagerar los beneficios.",
    ],
    vocab=[("ganadores y perdedores", "grupos que se benefician y grupos que se perjudican por un cambio"), ("impacto local", "efecto en una ciudad o región"), ("impacto nacional", "balance total para el país"), ("reconversión laboral", "capacitación y apoyo para cambiar de oficio o sector"), ("compensación", "ayuda a quienes pierden con un cambio"), ("cesantía", "situación de quien perdió su empleo")],
    worked=[
        ("Calcular una pérdida de ingresos", "Una fábrica de ejemplo despide a 50 trabajadores que ganaban $400.000 al mes. ¿Cuánto ingreso mensual se pierde en total?",
         ["Multiplica trabajadores por sueldo.", "50 por 400.000."],
         "$20.000.000 al mes"),
        ("Distinguir lo nacional y lo local", "La ciudad de ejemplo X pierde 100 empleos en una fábrica, pero el país gana 5.000 empleos en otras actividades. ¿Qué diferencia de impacto se observa?",
         ["En lo nacional, hay un balance positivo.", "En lo local, la ciudad X enfrenta una pérdida concentrada."],
         "Balance nacional positivo; pérdida local concentrada"),
    ],
    mistakes=[("Decir que el comercio perjudica a todos por los despidos.", "Se mira solo a un grupo.", "Hay ganadores y perdedores, y hay que mirar a ambos."),
              ("Decir que si el balance nacional es positivo no hay problema.", "Se ignora cómo se reparten los costos.", "Los costos pueden concentrarse en comunidades y requerir compensación.")],
    T=[
        ("=", "{F} ¿Cuánto ingreso mensual pierden en total los 200 trabajadores despedidos, en pesos?", "200*500000", "Se multiplican los trabajadores por su sueldo."),
        ("abc", "{F} ¿Quiénes ganan con la baja del precio de los zapatos?", "Los consumidores, que ahorran", "Los trabajadores despedidos", "La fábrica local", "El ahorro de los consumidores es de 400 millones al mes."),
        ("=", "{F} Los despedidos pierden en conjunto 100 millones de pesos al mes. ¿Cuántos millones al mes es el saldo entre el ahorro de los consumidores y esa pérdida?", "400-100", "Se resta la pérdida de ingresos al ahorro de los consumidores."),
        ("{F} ¿Cuántos empleos de los 900 de Valle Seco se pierden con los despidos?", "200", "La ficha dice que la fábrica despide a 200 trabajadores."),
        ("=", "{F} ¿Qué porcentaje de los 900 empleos de Valle Seco son los 200 despedidos? (resultado aproximado)", "200/900*100", "Se divide 200 entre 900 y se multiplica por 100."),
        ("abc", "En Economía y sociedad: ¿qué es una reconversión laboral?", "Capacitación y apoyo para cambiar de oficio o de sector", "Un impuesto al empleo", "Un subsidio a las importaciones", "Ayuda a quienes pierden su empleo a encontrar otro."),
        ("{F} El programa de reconversión cuesta $60 millones al mes. Si se financia con el ahorro de los consumidores, ¿cuánto de ese ahorro queda disponible?", "340 millones", "Se resta 60 a los 400 millones de ahorro."),
        ("abc", "{F} Una vecina de Valle Seco dice: «El comercio nos perjudicó a todos». ¿Qué corrección harías con los datos?", "No a todos: los consumidores ahorran; el costo se concentra en los trabajadores despedidos", "Tiene toda la razón", "Los consumidores también perdieron", "Los efectos no se reparten por igual."),
        ("abc", "{F} Un economista dice: «Como el balance total es positivo, no hace falta ayudar a nadie». ¿Qué falta en esa afirmación?", "Mirar cómo se reparten los costos y la justicia con quienes pierden", "Nada, es completa", "Los números del ahorro", "El balance positivo no elimina las pérdidas concentradas."),
        ("abc", "{F} Una concejala propone el programa de reconversión. Otra propone un arancel para proteger la fábrica. ¿Qué diferencia de enfoque hay?", "La primera ayuda a adaptarse y la segunda evita la competencia", "Ambas hacen lo mismo", "Ninguna tiene costos", "Una compensa y la otra protege."),
        ("abc", "{F} Una crítica a proteger la fábrica con aranceles es que…", "Los consumidores pagarían precios más altos", "Los consumidores pagarían precios menores", "Los productores locales perderían ventas", "Los aranceles encarecen el bien para quienes lo compran."),
        ("{F} ¿Qué dato adicional ayudaría a decidir si el programa de reconversión es efectivo?", "Cuántos de los despedidos consiguen un empleo comparable tras el programa", "Medir el resultado permite evaluar si vale su costo."),
        ("abc", "«Es justo compensar a quienes pierden por el comercio» es una afirmación…", "Normativa, porque expresa un juicio de justicia", "Positiva, porque tiene un dato", "Falsa", "Contiene un juicio de justicia que depende de valores."),
    ],
    ctx=("abc", "Una región agrícola de ejemplo exporta paltas gracias a un tratado de libre comercio y crecen los ingresos de sus productores, mientras una industria de conservas de otra región cierra por la competencia de productos importados. ¿Qué conclusión es adecuada?", "El tratado tiene ganadores y perdedores en distintas regiones", "El tratado perjudica a todos", "El tratado beneficia a todos por igual", "Los efectos locales difieren entre regiones."),
    sc=[
        ("¿Qué diferencia hay entre impacto nacional y local?", "El nacional es el balance total y el local lo que pasa en una ciudad o región", "Ambos impactos pueden ser muy distintos entre sí."),
        ("¿Para qué sirve una política de reconversión?", "Para que quienes pierden empleo puedan adaptarse a otra actividad", "Busca compensar a quienes pierden con el cambio."),
        ("¿Por qué no basta que el balance total sea positivo?", "Porque los costos pueden concentrarse en comunidades específicas", "La forma en que se reparte el costo también importa."),
    ],
    op=("Analiza este caso de ejemplo. Ciudad Lago tiene 600 empleos, 150 de ellos en una fábrica de muebles. Un tratado reduce el precio de los muebles de $200.000 a $150.000 y la fábrica despide a 100 trabajadores que ganaban $450.000 al mes cada uno; los consumidores del país ahorran $300 millones al mes. "
        "Calcula la pérdida mensual de ingresos de los despedidos, el balance con el ahorro de los consumidores, el porcentaje de empleos de Ciudad Lago que se pierde, y escribe un argumento a favor de compensar y otro que cuestione cómo hacerlo.",
        "Pérdida: 100 por 450.000, 45 millones. Balance: 300 menos 45, 255 millones a favor. Empleos perdidos: 100 de 600, cerca de 16,7%. A favor de compensar: los costos están concentrados. Cuestionamiento: no se sabe si el programa es efectivo ni quién lo paga.",
        ["calcula la pérdida de ingresos", "calcula el balance y el porcentaje de empleos", "presenta argumentos sobre compensar y sobre su costo"],
        ["cálculos y dos argumentos"],
        ["olvidar que los ingresos son mensuales", "concluir que no hay problema por el balance positivo", "tomar partido sin argumentos"],
        "Pregunta: «¿quién gana y quién pierde en este caso?». Pide que lo diga con cifras."),
    reinforce="Con la Ficha 35, escribe una frase con el impacto nacional y otra con el impacto local.",
    extend="Compara dos formas de ayudar a trabajadores afectados por el comercio (capacitación y seguro de cesantía) y qué valor prioriza cada una.",
)

# ============================================================ OAC-06, clase 6
F = ("Ficha 36 (país de ejemplo, ficticio). El País Sur obtiene el 80% del valor de sus exportaciones de un solo mineral. Índice del precio del mineral (año 1 = 100): año 2, 140; año 3, 70. "
     "Cada año exporta 10 unidades del mineral. El país exporta el mineral sin procesar a un valor de 100 por unidad; una empresa extranjera lo procesa y vende el producto elaborado a 250 por unidad.")
build(
    O6, 6, F,
    use="Aprenderé a analizar los desafíos de un país al insertarse en el mercado global (dependencia de pocos productos, volatilidad, valor agregado) y a comunicar una conclusión situada.",
    prior=["Conozco términos de intercambio y ventaja comparativa.", "Sé qué es la volatilidad.", "Sé escribir una conclusión situada con evidencia y límites."],
    explain=[
        "Insertarse en el mercado global significa participar en el comercio y en las cadenas de producción internacionales. Un primer desafío es la concentración exportadora: cuando un país exporta pocos productos, su ingreso depende de pocos precios, y si uno cae, el efecto es grande. La diversificación productiva intenta repartir ese riesgo agregando nuevos productos y mercados.",
        "Un segundo desafío es el valor agregado, que es el valor que se suma a un bien cuando se transforma. Exportar un mineral sin procesar deja el mayor valor en quien lo procesa; procesarlo en el país puede retener parte de ese valor, aunque exige inversión, tecnología y trabajadores capacitados. Otros desafíos son la innovación, la educación, la infraestructura y la capacidad de negociar reglas del comercio.",
        "Las posturas sobre cómo enfrentar estos desafíos difieren. Algunas ponen el acento en políticas activas para diversificar y agregar valor; otras, en mantener la apertura y que el mercado asigne los recursos, con reglas estables. Una conclusión situada sobre este tema indica el caso, la evidencia, los límites (por ejemplo, que los datos son de ejemplo) y una mirada alternativa, sin dar una receta universal.",
    ],
    vocab=[("concentración exportadora", "dependencia de pocos productos de exportación"), ("diversificación productiva", "ampliar la variedad de productos y mercados"), ("valor agregado", "valor que se suma a un bien al transformarlo"), ("cadena de valor", "secuencia de etapas para producir un bien"), ("inserción global", "participación de un país en el mercado mundial"), ("producto elaborado", "bien procesado con mayor valor")],
    worked=[
        ("Calcular el ingreso por exportación", "Un país de ejemplo exporta 20 unidades de un producto a un precio de 30. ¿Cuánto ingresa?",
         ["Multiplica cantidad por precio.", "20 por 30."],
         "600"),
        ("Calcular el valor agregado", "Una materia prima de ejemplo se vende a 50 y el producto elaborado a 120. ¿Cuánto valor se agrega al procesarla?",
         ["Resta el valor de la materia prima al del producto elaborado.", "120 menos 50."],
         "70"),
    ],
    mistakes=[("Creer que procesar un producto es fácil y siempre rentable.", "Se olvida la inversión y la tecnología.", "Agregar valor exige capacidades que hay que construir."),
              ("Creer que diversificar elimina todo el riesgo.", "Se supone una solución perfecta.", "Reduce la dependencia, pero tiene costos y plazos.")],
    T=[
        ("=", "{F} Año 1 (precio del mineral = 100): ¿cuánto vale la exportación del mineral con 10 unidades a 100 cada una?", "10*100", "Se multiplica cantidad por precio."),
        ("=", "{F} Año 2, con el índice del precio en 140: ¿cuánto vale la exportación de 10 unidades si el precio base es 100?", "10*140", "El precio pasa a 140 por unidad."),
        ("=", "{F} Año 3, con el índice del precio en 70: ¿cuánto vale la exportación de 10 unidades si el precio base es 100?", "10*70", "El precio pasa a 70 por unidad."),
        ("abc", "{F} Entre los años 2 y 3, ¿cómo cambió el ingreso de exportación del mineral?", "Bajó de 1.400 a 700", "Subió de 700 a 1.400", "Se mantuvo igual", "El precio cayó a la mitad con la misma cantidad."),
        ("abc", "En Economía y sociedad: ¿qué es la concentración exportadora?", "Depender de pocos productos de exportación", "Exportar a un solo país", "Tener muchas empresas", "Una caída del precio de ese producto afecta todo el ingreso."),
        ("=", "{F} ¿Cuánto valor agregado se genera al procesar una unidad de mineral? (producto elaborado menos mineral sin procesar)", "250-100", "Se resta el valor sin procesar al valor elaborado."),
        ("=", "{F} Si el país procesara las 10 unidades, ¿cuánto valor agregado total retendría?", "10*150", "Se multiplica el valor agregado por unidad por las unidades."),
        ("abc", "En Economía y sociedad: ¿qué es el valor agregado?", "El valor que se suma a un bien al transformarlo", "El impuesto al consumo", "El precio del mineral", "Es la diferencia entre el valor del producto elaborado y los insumos."),
        ("abc", "{F} ¿Qué política busca reducir el riesgo de depender de un solo precio?", "La diversificación productiva", "Un precio máximo", "Un arancel a las importaciones", "Esta política agrega productos y mercados nuevos."),
        ("{F} Explica por qué procesar el mineral en el país no es una solución automática.", "Porque exige inversión, tecnología y trabajadores capacitados", "Agregar valor requiere capacidades que hay que construir."),
        ("abc", "{F} Una economista dice: «Hay que mantener la apertura y dejar que el mercado asigne los recursos». Otra dice: «Hay que impulsar activamente el procesamiento». ¿Qué ocurre aquí?", "Hay dos posturas con argumentos y valores distintos", "Solo una tiene argumentos", "Las dos son iguales", "Cada una destaca un riesgo diferente."),
        ("abc", "{F} ¿Qué límite tiene usar solo tres años de precios?", "No permite concluir sobre tendencias de largo plazo", "Que los precios no se pueden comparar", "Que tres años no tienen valor alguno", "Tres años son pocos para afirmar patrones."),
        ("abc", "{F} ¿Cuál de estas frases es una conclusión situada?", "En este país de ejemplo, el ingreso por el mineral cayó de 1.400 a 700 entre el año 2 y el 3, aunque son datos de ejemplo de solo tres años", "Los minerales siempre bajan de precio y ningún país debe exportarlos", "El mineral es lo único que el país debe exportar", "Indica el caso, la evidencia con cifras y el límite de los datos."),
    ],
    ctx=("abc", "Una cooperativa de ejemplo vende duraznos frescos a 40 el kilo y, tras instalar una planta de conservas, vende las conservas hechas con un kilo de duraznos a 100. ¿Cuánto valor agregado obtiene por kilo?", "60", "40", "140", "Son 100 de la conserva menos 40 de los duraznos frescos."),
    sc=[
        ("¿Qué riesgo tiene depender de pocos productos de exportación?", "Que la caída del precio de uno de ellos afecte todo el ingreso", "El ingreso depende de pocos precios."),
        ("En Economía y sociedad: ¿qué es el valor agregado?", "El valor que se suma a un bien al transformarlo", "Se mide como valor elaborado menos insumos."),
        ("¿Por qué la diversificación no elimina todo el riesgo?", "Porque tiene costos, plazos y nuevos riesgos", "Es una estrategia gradual y parcial."),
    ],
    op=("Escribe una conclusión situada (cuatro a seis líneas) sobre los desafíos de País Sur con la Ficha 36. Debe incluir: una afirmación con cifras, una opción para enfrentar el problema (diversificar o agregar valor), un riesgo o costo de esa opción, un límite de los datos y una mirada alternativa. "
        "Evita recetas universales.",
        "En este país de ejemplo, el ingreso por el mineral bajó de 1.400 a 700 entre el año 2 y el año 3 con las mismas 10 unidades, y el 80% de las exportaciones depende de él. Procesarlo retendría 150 por unidad, pero exige inversión. Los datos son de ejemplo y de tres años. Otra mirada: priorizar la apertura y la estabilidad de reglas.",
        ["usa cifras de la ficha", "propone una opción con su costo o riesgo", "declara un límite", "presenta una mirada alternativa"],
        ["párrafo de cuatro a seis líneas"],
        ["afirmar como cierto lo que depende de supuestos", "no declarar ningún límite", "recetas universales"],
        "Pregunta: «¿qué opción de política elegirías y qué costo tendría?». Pide que no omita el costo."),
    reinforce="Con la Ficha 36, calcula el ingreso por exportación del mineral en los tres años y escribe una frase que los compare.",
    extend="Compara el procesamiento local y la diversificación hacia otros productos, indicando una ventaja y una dificultad de cada uno.",
)

# ============================================================ OAC-08, clase 1
F = ("Ficha 37 (países de ejemplo, ficticios). País Pinar crece 5% al año y País Roble crece 2% al año. En Pinar, la producción por habitante sube, pero la mitad de los hogares dice que su ingreso casi no ha cambiado y el aire de la capital empeora. "
     "En Roble, el crecimiento es más lento, la educación mejora y las jornadas de trabajo se acortan.")
build(
    O8, 1, F,
    use="Aprenderé a analizar la relación entre crecimiento económico y bienestar: qué puede aportar el crecimiento, qué no mide y qué dilemas plantea.",
    prior=["Sé calcular el crecimiento del PIB y el PIB per cápita.", "Distingo crecimiento y desarrollo.", "Sé calcular porcentajes."],
    explain=[
        "El crecimiento económico puede mejorar el bienestar: más producción permite más ingresos, más empleo, mayor recaudación para financiar educación y salud, y más opciones para las personas. Por eso muchos países lo ven como un objetivo central. Una forma simple de entender su velocidad es la regla del 70, una aproximación: el tiempo en que se duplica una cantidad es 70 dividido por la tasa de crecimiento porcentual.",
        "Pero el crecimiento no equivale al bienestar. Puede ir acompañado de desigualdad, de contaminación o de jornadas muy largas; y los promedios, como el PIB per cápita, no muestran cómo se reparte el ingreso. Por eso se usan indicadores complementarios, como la distribución del ingreso, la esperanza de vida, la educación, la calidad del ambiente y encuestas de satisfacción con la vida.",
        "Los países desarrollados y en vías de desarrollo enfrentan el dilema de manera distinta. Un país con bajos ingresos puede priorizar el crecimiento para reducir carencias urgentes, mientras uno con ingresos altos puede preguntarse qué tipo de crecimiento conviene y cuánto crecimiento adicional mejora la vida. Hay posturas distintas, que se presentan con sus argumentos, y la decisión involucra valores sobre qué es una buena vida.",
    ],
    vocab=[("bienestar", "calidad de vida de las personas: salud, educación, ingreso, ambiente y tiempo libre"), ("regla del 70", "aproximación: años para duplicar = 70 dividido por la tasa de crecimiento"), ("indicador complementario", "medida que agrega aspectos que el PIB no mide"), ("jornada de trabajo", "horas que se trabaja en un período"), ("satisfacción con la vida", "valoración subjetiva que las personas hacen de su vida"), ("dilema", "situación en que hay que elegir entre valores o beneficios que compiten")],
    worked=[
        ("Aplicar la regla del 70", "Una economía de ejemplo crece 10% al año. Según la regla del 70, ¿en cuánto tiempo duplica su producción?",
         ["Divide 70 por la tasa de crecimiento.", "70 dividido por 10."],
         "7 años"),
        ("Distinguir crecimiento y bienestar", "Un país de ejemplo duplica su PIB, pero las enfermedades respiratorias aumentan por la contaminación. ¿Qué muestra?",
         ["El PIB creció, pero el ambiente empeoró.", "El crecimiento no garantiza una mejora del bienestar."],
         "Que crecimiento y bienestar no son lo mismo"),
    ],
    mistakes=[("Creer que si el PIB sube, todos viven mejor.", "Se confunde promedio con distribución.", "Revisa cómo se reparte el ingreso y otros indicadores."),
              ("Creer que crecer siempre daña el ambiente o que nunca lo daña.", "Se generaliza.", "El efecto depende de cómo se crece y de las políticas que se aplican.")],
    T=[
        ("=", "{F} Según la regla del 70, ¿en cuántos años duplica su producción País Pinar?", "70/5", "Se divide 70 por la tasa de crecimiento."),
        ("=", "{F} Según la regla del 70, ¿en cuántos años duplica su producción País Roble?", "70/2", "Se divide 70 por la tasa de crecimiento."),
        ("abc", "En Economía y sociedad: ¿qué es el bienestar?", "La calidad de vida: salud, educación, ingreso, ambiente y tiempo libre", "Solo el ingreso", "Solo el PIB", "El bienestar incluye más aspectos que el ingreso."),
        ("abc", "{F} ¿Qué muestra que la mitad de los hogares de Pinar diga que su ingreso casi no ha cambiado?", "Que el promedio no refleja cómo se reparte el beneficio del crecimiento", "Que el PIB per cápita es siempre exacto", "Que el crecimiento es negativo", "El promedio puede esconder la desigualdad entre hogares."),
        ("abc", "{F} ¿Qué aspecto del bienestar empeora en Pinar según la ficha?", "La calidad del aire", "La educación", "Las jornadas de trabajo", "La ficha menciona el aire de la capital."),
        ("abc", "{F} ¿Qué aspectos del bienestar mejoran en Roble según la ficha?", "La educación y la reducción de jornadas", "La calidad del aire", "El ingreso de la mitad de los hogares", "La ficha menciona educación y jornadas más cortas."),
        ("=", "{F} Si Pinar parte con 100 de producción y pasan 28 años, es decir dos duplicaciones, ¿cuánto produce?", "100*2*2", "Cada duplicación multiplica por dos, y son dos duplicaciones."),
        ("abc", "{F} Una periodista dice: «Pinar es mejor porque crece más». ¿Qué corrección harías?", "Hay que mirar más indicadores que el crecimiento, como el ambiente y la distribución", "Es correcto, el crecimiento resume todo", "El crecimiento no existe", "El bienestar es más que crecer."),
        ("abc", "{F} Una economista dice: «Roble debería crecer más rápido para reducir carencias». Otra dice: «Roble ya tiene una vida mejor en lo que importa». ¿Qué ocurre?", "Valoran distinto el crecimiento y el bienestar", "Una de las dos miente", "Ambas hablan de inflación", "Entre ambas hay una diferencia de valores sobre qué priorizar."),
        ("{F} ¿Por qué un país de ingresos bajos y uno de ingresos altos pueden valorar distinto el crecimiento adicional?", "Porque el país pobre tiene carencias urgentes que el crecimiento puede ayudar a cubrir", "El efecto de un ingreso extra es mayor donde hay más carencias."),
        ("abc", "Dos países de ejemplo crecen 3% al año, pero uno reparte el ingreso de forma más pareja. ¿Qué indicador permitiría verlo?", "Un indicador de distribución del ingreso", "El número de habitantes", "El número de ciudades del país", "Muestra cómo se reparte el beneficio."),
        ("abc", "«El gobierno debería priorizar el crecimiento por sobre el ambiente» es una afirmación…", "Normativa, porque expresa una prioridad", "Positiva, porque se verifica con datos", "Falsa", "Dice qué debería hacerse según valores."),
        ("=", "Un país de ejemplo crece 7% al año. Según la regla del 70, ¿en cuántos años duplica su producción?", "70/7", "Se divide 70 entre la tasa de crecimiento."),
    ],
    ctx=("abc", "Una ciudad de ejemplo atrae una gran fábrica que aumenta el empleo y los ingresos locales, pero aumenta el ruido y el tráfico. ¿Qué dilema plantea?", "Entre más ingresos y empleo, y peor calidad de vida en el barrio", "Entre dos precios iguales", "Entre dos monedas", "Hay beneficios y costos que se reparten distinto."),
    sc=[
        ("¿Qué indica la regla del 70?", "Los años que tarda en duplicarse una cantidad: 70 dividido por la tasa", "La regla del 70 es solo una aproximación útil."),
        ("En Economía y sociedad: ¿por qué el PIB per cápita no basta para medir el bienestar?", "Porque es un promedio y no incluye ambiente, distribución ni tiempo libre", "Hay aspectos del bienestar que no mide."),
        ("¿Qué es un indicador complementario?", "Una medida que agrega aspectos que el PIB no mide", "Ayuda a ver el bienestar de forma más completa."),
    ],
    op=("Compara dos países de ejemplo. País Cerro crece 4% al año, tiene mucha contaminación y el 20% más rico recibe 55% del ingreso. País Bosque crece 2% al año, tiene aire limpio y el 20% más rico recibe 38%. "
        "Calcula en cuántos años se duplica la producción de cada uno (regla del 70) y escribe: dos indicadores a favor de cada país, un dilema que enfrentan y una pregunta que le harías a una persona de cada país.",
        "Cerro: 70/4 son 17,5 años. Bosque: 70/2 son 35 años. A favor de Cerro: crecimiento más alto. A favor de Bosque: aire limpio y mejor reparto. Dilema: crecer rápido frente a cuidar ambiente e igualdad. Pregunta: ¿cómo vive el 20% más pobre en cada país?",
        ["aplica la regla del 70", "nombra indicadores a favor de cada país", "describe un dilema", "formula preguntas pertinentes"],
        ["cálculos, listas y dos preguntas"],
        ["calcular la duplicación al revés", "ignorar los indicadores no económicos", "tomar partido sin argumentos"],
        "Pregunta: «¿qué mide el crecimiento y qué no mide?». Con eso revisa los indicadores."),
    reinforce="Elige cinco indicadores que usarías para decir si una persona de tu comuna vive mejor que hace diez años.",
    extend="Explica por qué dos personas pueden preferir políticas distintas con los mismos datos de crecimiento.",
)

# ============================================================ OAC-08, clase 2
F = ("Ficha 38 (cadena de valor de ejemplo, ficticia). Una bicicleta se produce así: el marco se fabrica en el País A, las ruedas en el País B, y el ensamble final en el País C. Costos por bicicleta, en u.m.: marco 40, ruedas 30, ensamble 20 y transporte 10; total 100. "
     "Además, las bicicletas que el País C vende al País X son el 40% de sus exportaciones totales, que suman 200 (u.m.).")
build(
    O8, 2, F,
    use="Aprenderé qué es la interdependencia entre economías: cadenas globales de producción, efectos de shocks externos y los desafíos de depender de otros países.",
    prior=["Conozco comercio internacional y términos de intercambio.", "Sé calcular porcentajes.", "Sé qué es una cadena de valor."],
    explain=[
        "La interdependencia es la situación en que las economías de distintos países se influyen mutuamente. Hoy muchos bienes se producen en cadenas globales de valor: cada etapa ocurre en un país distinto, según dónde resulta más barata o mejor. Esto reduce costos y permite especializarse, pero también conecta a los países: un problema en una etapa puede afectar a todas.",
        "Un shock externo es un cambio brusco que viene de fuera, como un alza de precios de un insumo, una crisis financiera en otro país o una caída de la demanda de un mercado importante. Sus efectos se transmiten por varios canales: precios de insumos importados, exportaciones, tasas de interés y expectativas. Los países pequeños y muy abiertos suelen sentir esos efectos más intensamente.",
        "Frente a la interdependencia hay desafíos: la concentración en pocos proveedores o mercados, la dificultad de coordinar reglas entre países y la distribución de beneficios dentro de cada uno. Hay posturas que ponen el acento en la cooperación y las cadenas globales, y otras que destacan la necesidad de mayor autonomía en bienes estratégicos. Ambas se basan en argumentos que se evalúan con datos.",
    ],
    vocab=[("interdependencia", "influencia mutua entre las economías de distintos países"), ("cadena global de valor", "producción repartida en etapas realizadas en distintos países"), ("shock externo", "cambio brusco que viene de fuera de la economía"), ("canal de transmisión", "camino por el que un shock afecta a una economía"), ("proveedor", "quien entrega un bien o insumo a otro"), ("bien estratégico", "bien considerado esencial para la seguridad o el abastecimiento")],
    worked=[
        ("Calcular el efecto de un alza", "En un producto de ejemplo, el insumo importado cuesta 50 de un total de 200. Si ese insumo sube 10%, ¿cuánto aumenta el costo total?",
         ["10% de 50 es 5.", "El costo total pasa de 200 a 205."],
         "5 unidades más"),
        ("Identificar la concentración", "Un país de ejemplo exporta el 70% de sus productos a un solo país. ¿Qué riesgo tiene?",
         ["Depende de un solo mercado.", "Si ese mercado reduce sus compras, el efecto es grande."],
         "Dependencia de un solo mercado"),
    ],
    mistakes=[("Creer que la interdependencia solo trae beneficios o solo trae riesgos.", "Se simplifica.", "Reduce costos y aumenta la exposición a shocks."),
              ("Pensar que los shocks externos afectan igual a todos los países.", "Se olvida la estructura de cada economía.", "Dependen del tamaño, la apertura y la diversificación.")],
    T=[
        ("=", "{F} ¿Cuánto cuesta producir una bicicleta sin el transporte?", "40+30+20", "Se suman marco, ruedas y ensamble."),
        ("=", "{F} El precio de las ruedas sube 20%. ¿Cuánto aumenta el costo de las ruedas en u.m.?", "30*20/100", "Se calcula el 20% de 30."),
        ("=", "{F} Con ese aumento, ¿cuál es el nuevo costo total de la bicicleta?", "100+6", "Al costo total se le suma el aumento de las ruedas."),
        ("abc", "{F} ¿Qué porcentaje aumenta el costo total de la bicicleta?", "6%", "20%", "30%", "El aumento de 6 sobre 100 es 6%."),
        ("abc", "En Economía y sociedad: ¿qué es una cadena global de valor?", "Una producción repartida en etapas realizadas en distintos países", "Una cadena de tiendas", "Un tipo de impuesto", "Cada etapa ocurre donde resulta más conveniente."),
        ("abc", "{F} ¿Qué país produce el componente más caro de la bicicleta?", "País A, con el marco de 40", "País B", "País C", "El marco cuesta 40, más que las ruedas (30) y el ensamble (20)."),
        ("=", "{F} ¿Cuántas u.m. exporta el País C al País X?", "200*40/100", "Se calcula el 40% de 200."),
        ("=", "{F} Si el País X reduce sus compras en 10%, ¿cuántas u.m. dejan de ingresar al País C?", "80*10/100", "Se calcula el 10% de las exportaciones a X."),
        ("abc", "{F} ¿Qué porcentaje de las exportaciones totales del País C representa esa caída?", "4%", "10%", "40%", "8 u.m. sobre 200 es 4%."),
        ("abc", "En Economía y sociedad: ¿qué es un shock externo?", "Un cambio brusco que viene de fuera de la economía", "Un impuesto interno", "Una política del banco central", "Un shock externo se origina fuera del propio país."),
        ("{F} Una crisis detiene la producción de ruedas en el País B. ¿Qué ocurre con la producción de bicicletas del País C?", "Se ve afectada, porque depende de las ruedas de B", "Es el efecto de la interdependencia en una cadena."),
        ("abc", "{F} Un defensor de la autonomía dice que conviene producir ruedas también en el País C. Un defensor de las cadenas globales dice que eso subiría los costos. ¿Qué ocurre aquí?", "Cada postura destaca un valor distinto: seguridad de abastecimiento o menor costo", "Solo una tiene argumentos", "Ninguna usa datos", "Se comparan dos valores: seguridad y costo."),
        ("abc", "¿Qué tipo de país suele sentir con más fuerza los shocks externos?", "Uno pequeño y muy abierto, con pocos socios", "Uno que no comercia con nadie", "Uno con muchas actividades y socios variados", "Depende más de lo que ocurre afuera."),
    ],
    ctx=("abc", "Un puerto de ejemplo se cierra una semana por una crisis en otro país, y varias fábricas dejan de recibir componentes. ¿Qué concepto ilustra?", "Interdependencia a través de una cadena global de valor", "Un arancel", "Un monopolio", "Los problemas en una etapa afectan a las otras."),
    sc=[
        ("¿Qué beneficio y qué riesgo tienen las cadenas globales de valor?", "Menores costos y mayor exposición a shocks", "Estas cadenas conectan a los países entre sí."),
        ("Nombra un canal por el que un shock externo afecta a una economía.", "Precios de insumos, exportaciones, tasas de interés o expectativas", "Son los caminos por los que se transmite el shock."),
        ("En Economía y sociedad: ¿qué es un bien estratégico?", "Un bien considerado esencial para la seguridad o el abastecimiento", "Se discute si debe producirse con mayor autonomía."),
    ],
    op=("Analiza una cadena de ejemplo. Un celular se produce con pantalla del País P (35), batería del País Q (25), ensamble del País R (30) y transporte (10). Un conflicto sube 20% el costo de las baterías. "
        "Calcula el costo total, el aumento del costo total y su porcentaje; escribe un riesgo de depender de un solo proveedor de baterías y una medida para reducirlo, con un costo de esa medida.",
        "Total 100. Baterías: 25 por 20% son 5. Nuevo total 105, aumento de 5%. Riesgo: si el proveedor falla se detiene la producción. Medida: buscar un segundo proveedor, con un costo de negociar nuevos contratos.",
        ["calcula bien el costo total y el aumento", "calcula el porcentaje", "nombra un riesgo y una medida con su costo"],
        ["cálculos y dos frases"],
        ["aplicar el porcentaje al total en vez de al componente", "no incluir un costo de la medida", "olvidar el riesgo"],
        "Pregunta: «¿qué costo sube y cuánto del total representa?». Pide que lo calcule sobre el componente."),
    reinforce="Con la Ficha 38, calcula cuánto aumentaría el costo total si el marco sube 10%.",
    extend="Explica ventajas y riesgos de tener varios proveedores de un mismo componente.",
)

# ============================================================ OAC-08, clase 3
F = ("Ficha 39 (datos de ejemplo, ficticios). Economía Costa Verde: año 1, producción 100 y emisiones de gases contaminantes 60; año 2, producción 120 y emisiones 66. "
     "Una pesquería de ejemplo tiene 1.000 toneladas de peces; cada año la población se repone en 100 toneladas y se pescan 150 toneladas (en este modelo simple, supón que esas cifras no cambian).")
build(
    O8, 3, F,
    use="Aprenderé qué es una economía sustentable, cómo se relaciona el crecimiento con el ambiente, qué diferencia hay entre recursos renovables y no renovables y qué opciones se discuten.",
    prior=["Conozco externalidades negativas.", "Sé calcular porcentajes y razones.", "Distingo costos privados y sociales."],
    explain=[
        "Una economía sustentable busca satisfacer las necesidades actuales sin comprometer la capacidad de las generaciones futuras de satisfacer las suyas. Eso exige cuidar el ambiente y los recursos. Un recurso renovable es el que se repone de forma natural (peces, bosques, agua) si no se usa más rápido de lo que se repone; un recurso no renovable se agota con el uso (como los minerales y el petróleo).",
        "Para ver la relación entre producción y ambiente se usa la intensidad de emisiones, que es la cantidad de emisiones por unidad de producción. Si la producción crece más que las emisiones, la intensidad baja, y se habla de desacople parcial. Pero lo que importa para el ambiente es el total de emisiones, no solo su intensidad. La economía circular propone reducir residuos reutilizando, reparando y reciclando materiales.",
        "Hay posturas distintas. Algunas sostienen que con tecnología, regulación e incentivos es posible crecer reduciendo el impacto ambiental. Otras sostienen que existen límites ambientales y que en los países de mayores ingresos habría que moderar el consumo. También se discute quién paga los costos de la transición. Aquí se presentan los argumentos y los cálculos, sin elegir una postura.",
    ],
    vocab=[("economía sustentable", "economía que satisface necesidades actuales sin comprometer las futuras"), ("recurso renovable", "recurso que se repone naturalmente si no se sobreexplota"), ("recurso no renovable", "recurso que se agota con el uso"), ("intensidad de emisiones", "emisiones por unidad de producción"), ("economía circular", "modelo que reduce residuos reutilizando y reciclando"), ("sobreexplotación", "usar un recurso más rápido de lo que se repone")],
    worked=[
        ("Calcular una intensidad", "Una economía de ejemplo produce 200 y emite 100. ¿Cuál es su intensidad de emisiones?",
         ["Divide las emisiones por la producción.", "100 dividido por 200."],
         "0,5"),
        ("Detectar sobreexplotación", "Un bosque de ejemplo crece 50 árboles al año y se talan 80 al año. ¿Cuántos árboles se pierden cada año?",
         ["Compara lo que se repone con lo que se extrae.", "80 menos 50."],
         "30 árboles al año"),
    ],
    mistakes=[("Creer que si baja la intensidad de emisiones el ambiente mejora siempre.", "Se olvida el total.", "Si la producción crece mucho, el total de emisiones puede subir igual."),
              ("Creer que un recurso renovable no se puede agotar.", "Se ignora la sobreexplotación.", "Se repone solo si no se usa más rápido de lo que se repone.")],
    T=[
        ("=", "{F} ¿Cuál es la intensidad de emisiones en el año 1 (emisiones por unidad de producción)?", "60/100", "Se dividen las emisiones por la producción."),
        ("=", "{F} ¿Cuál es la intensidad de emisiones en el año 2?", "66/120", "Se dividen las emisiones por la producción."),
        ("abc", "{F} Entre el año 1 y el año 2, ¿qué ocurrió con la intensidad de emisiones?", "Bajó", "Subió", "Se mantuvo", "La intensidad pasó de 0,6 a 0,55, es decir, bajó."),
        ("abc", "{F} Entre el año 1 y el año 2, ¿qué ocurrió con el total de emisiones?", "Subió, de 60 a 66", "Bajó", "Se mantuvo", "El total de 66 es mayor que el de 60."),
        ("=", "{F} ¿Cuántas toneladas netas pierde la pesquería cada año (pesca menos reposición)?", "150-100", "Se resta la reposición a lo pescado."),
        ("=", "{F} Si se mantiene la pesca, ¿cuántas toneladas quedarán después de 4 años?", "1000-4*50", "Cada año se pierden 50 toneladas netas."),
        ("abc", "En Economía y sociedad: ¿qué es un recurso renovable?", "Uno que se repone naturalmente si no se usa más rápido de lo que se repone", "Uno que solo se encuentra en los océanos", "Uno que se importa", "Un recurso renovable puede agotarse si se sobreexplota."),
        ("abc", "{F} ¿Qué cantidad máxima anual de pesca mantendría estable la población de peces?", "100 toneladas", "150 toneladas", "50 toneladas", "Es lo que se repone cada año."),
        ("abc", "{F} Un empresario dice: «Como bajó la intensidad de emisiones, el ambiente no empeoró». ¿Qué corrección harías?", "El total de emisiones subió; la intensidad no basta", "Tiene razón en todo", "Las emisiones bajaron", "Lo que importa es el total."),
        ("abc", "{F} Una defensora de la regulación dice que se necesita una norma que limite las emisiones totales. Un defensor del crecimiento dice que la tecnología bajará la intensidad. ¿Qué ocurre?", "Proponen caminos distintos con argumentos distintos", "Solo uno tiene argumentos", "Los dos dicen lo mismo", "Una postura discute límites y la otra confía en la tecnología."),
        ("abc", "En Economía y sociedad: ¿qué es la economía circular?", "Un modelo que reduce residuos reutilizando, reparando y reciclando", "Una economía sin comercio", "Una economía sin Estado", "Busca que los materiales se mantengan en uso."),
        ("{F} ¿Por qué un impuesto a las emisiones puede ser una política para esta economía, y qué costo podría tener?", "Hace que quien contamina pague el costo y cambia incentivos, pero puede encarecer productos y afectar el empleo", "Internaliza la externalidad con efectos distributivos."),
        ("abc", "«Los países ricos deben consumir menos» es una afirmación…", "Normativa, porque expresa lo que se debe hacer según valores", "Positiva, porque se mide con datos", "Falsa", "Contiene un deber que depende de valores."),
    ],
    ctx=("abc", "Un lago de ejemplo se repone con 80 toneladas de peces al año y los pescadores capturan 120. ¿Qué sucede a largo plazo si nada cambia?", "La población de peces disminuye cada año", "La población aumenta", "Se mantiene estable", "Se extraen 40 más de lo que se repone."),
    sc=[
        ("¿Qué es la intensidad de emisiones?", "Emisiones por unidad de producción", "Se calcula dividiendo emisiones entre producción."),
        ("¿Por qué no basta mirar la intensidad?", "Porque el total de emisiones puede subir si la producción crece mucho", "Lo que afecta al ambiente es el total."),
        ("En Economía y sociedad: ¿qué es la sobreexplotación?", "Usar un recurso más rápido de lo que se repone", "La sobreexplotación puede agotar un recurso renovable."),
    ],
    op=("Analiza este caso de ejemplo. Una economía produce 150 y emite 90; después produce 180 y emite 99. Un bosque de ejemplo con 2.000 árboles crece 100 árboles al año y se talan 160 al año. "
        "Calcula la intensidad en ambos años, di si el total de emisiones subió o bajó, calcula cuántos árboles quedan después de 5 años y escribe una política posible con una ventaja y un costo, sin elegir una postura.",
        "Intensidad: 0,6 y 0,55. El total sube de 90 a 99. Árboles: 2.000 menos 5 por 60, 1.700. Política: impuesto a la tala, con ventaja de reducir pérdida y costo de encarecer la madera.",
        ["calcula las intensidades", "compara total y relación", "calcula la pérdida de recurso", "propone una política con ventaja y costo"],
        ["tres cálculos y una política"],
        ["confundir intensidad con total", "olvidar la reposición", "no declarar ningún costo de la política"],
        "Pregunta: «¿baja la intensidad pero sube el total?». Pide que lo verifique con cifras."),
    reinforce="Con la Ficha 39, calcula cuántos años aguantaría la pesquería si pescan 150 toneladas al año y se reponen 100, hasta agotar 1.000 toneladas.",
    extend="Compara las posturas de crecer reduciendo el impacto ambiental y de moderar el consumo, mencionando un argumento de cada una.",
)

# ============================================================ OAC-08, clase 4
F = ("Ficha 40 (distribución de ejemplo, ficticia). País Lomas dividido en cinco grupos iguales de población, de menor a mayor ingreso. Parte del ingreso total que recibe cada grupo: primer quinto 5%, segundo 10%, tercero 15%, cuarto 25% y quinto 45%. "
     "Sistema de impuesto de ejemplo: 0% hasta $1.000.000 de ingreso mensual; 10% sobre lo que excede $1.000.000 hasta $3.000.000; 20% sobre lo que excede $3.000.000.")
build(
    O8, 4, F,
    use="Aprenderé a analizar la equidad y la desigualdad con indicadores, a distinguir igualdad y equidad y a evaluar políticas de redistribución con sus argumentos a favor y en contra.",
    prior=["Sé leer una distribución en porcentajes.", "Conozco impuestos y transferencias.", "Distingo afirmaciones positivas y normativas."],
    explain=[
        "La desigualdad económica describe diferencias en ingreso o riqueza entre personas o grupos. Una forma de medirla es dividir la población en cinco grupos iguales, llamados quintiles, y ver qué parte del ingreso recibe cada uno. La razón entre el quinto y el primer quintil dice cuántas veces recibe más el grupo de mayores ingresos que el de menores. Otro indicador usado es el coeficiente de Gini, que va de 0 (igualdad total) a 1 (desigualdad máxima).",
        "Igualdad y equidad no son sinónimos: la igualdad pide tratar a todos igual; la equidad pide tratar de modo justo según las circunstancias, lo que a veces significa dar más apoyo a quien tiene menos. La pobreza es una situación de carencia de ingresos o recursos para cubrir necesidades básicas. La movilidad social es la posibilidad de mejorar la posición económica a lo largo de la vida o entre generaciones.",
        "La redistribución se hace con impuestos y transferencias. Un impuesto progresivo cobra una tasa mayor a quienes tienen más ingresos, y uno regresivo pesa más, en proporción, sobre quienes tienen menos. Se discute cuánta redistribución es conveniente: quienes la defienden destacan la justicia y las oportunidades; quienes la cuestionan advierten sobre los efectos en los incentivos al trabajo y la inversión. Los datos informan, y las conclusiones dependen de valores.",
    ],
    vocab=[("desigualdad", "diferencias de ingreso o riqueza entre personas o grupos"), ("quintil", "uno de cinco grupos iguales de población ordenados por ingreso"), ("coeficiente de Gini", "indicador de desigualdad entre 0 y 1"), ("equidad", "trato justo según las circunstancias"), ("movilidad social", "posibilidad de mejorar la posición económica"), ("impuesto progresivo", "impuesto con tasa mayor para quienes tienen más ingresos")],
    worked=[
        ("Calcular una razón", "En un país de ejemplo el quinto quintil recibe 40% del ingreso y el primero 8%. ¿Cuántas veces recibe más el quinto que el primero?",
         ["Divide 40 por 8.", "El resultado es 5."],
         "5 veces"),
        ("Calcular un impuesto progresivo", "Con una regla de ejemplo: 0% hasta 500.000 y 10% sobre lo que exceda de 500.000, una persona con ingreso de 800.000. ¿Cuánto paga?",
         ["Lo que excede es 800.000 menos 500.000, igual a 300.000.", "El 10% de 300.000 es 30.000."],
         "$30.000"),
    ],
    mistakes=[("Creer que equidad es lo mismo que igualdad.", "Se confunde tratar igual con tratar justo.", "La equidad atiende circunstancias distintas."),
              ("Creer que un impuesto progresivo cobra la misma tasa a todos.", "Se confunde con un impuesto plano.", "La tasa aumenta con el ingreso.")],
    T=[
        ("=", "{F} ¿Cuántas veces recibe más ingreso el quinto quintil que el primero?", "45/5", "Se divide la parte del quinto por la del primero."),
        ("=", "{F} ¿Qué porcentaje del ingreso recibe en conjunto el 40% de menores ingresos (primer y segundo quintil)?", "5+10", "Se suman los dos primeros quintiles."),
        ("abc", "{F} ¿Qué quintil recibe la mayor parte del ingreso?", "El quinto", "El primero", "El tercero", "El quinto quintil recibe 45%, la mayor parte."),
        ("abc", "En Economía y sociedad: ¿qué es un quintil?", "Uno de cinco grupos iguales de población ordenados por ingreso", "Un tipo de impuesto", "Un indicador de inflación", "Divide a la población en cinco grupos."),
        ("=", "{F} Una persona con ingreso mensual de $2.000.000, ¿cuánto impuesto paga? (10% sobre lo que excede $1.000.000)", "(2000000-1000000)*10/100", "Se calcula el 10% del exceso sobre $1.000.000."),
        ("=", "{F} Una persona con ingreso mensual de $4.000.000, ¿cuánto paga en el tramo de 10% (sobre $2.000.000 entre 1.000.000 y 3.000.000)?", "2000000*10/100", "El tramo del 10% abarca $2.000.000."),
        ("=", "{F} La misma persona de $4.000.000, ¿cuánto paga en el tramo de 20% (sobre lo que excede $3.000.000)?", "(4000000-3000000)*20/100", "Se calcula el 20% del exceso sobre $3.000.000."),
        ("abc", "{F} ¿Qué tipo de impuesto es el de la ficha?", "Progresivo, porque la tasa aumenta con el ingreso", "Regresivo", "Plano, con la misma tasa", "Las tasas suben de 0% a 10% y a 20%."),
        ("abc", "En Economía y sociedad: ¿cuál es la diferencia entre igualdad y equidad?", "La igualdad trata a todos igual; la equidad trata de modo justo según las circunstancias", "No hay diferencia", "La equidad es un impuesto", "La equidad puede dar más apoyo a quien tiene menos."),
        ("{F} Una persona dice: «El quinto quintil recibe 45%, así que hay desigualdad». Otra dice: «La desigualdad es injusta». ¿Cuál es positiva y cuál normativa?", "La primera es positiva y la segunda normativa", "Una describe un dato y la otra expresa un juicio de valor."),
        ("abc", "{F} Un defensor de la redistribución dice que mejora las oportunidades. Un crítico dice que puede reducir los incentivos al trabajo. ¿Qué tipo de desacuerdo es?", "Una diferencia de valores y de evidencia sobre efectos", "Un error de cálculo", "Una confusión de unidades", "Ambas posturas se apoyan en argumentos distintos."),
        ("abc", "Un impuesto de ejemplo del 19% al consumo pesa igual en pesos sobre una compra de $10.000 para cualquier persona. ¿Por qué se discute que puede ser regresivo?", "Porque pesa más, en proporción, sobre quienes tienen menos ingresos", "Porque cobra más a los ricos", "Porque no cobra a nadie", "Los hogares de menores ingresos destinan una parte mayor de su ingreso a consumir."),
        ("abc", "Dos países de ejemplo tienen el mismo coeficiente de Gini. ¿Significa que tienen la misma movilidad social?", "No, son conceptos distintos", "Sí, porque ambos miden lo mismo", "Solo si tienen la misma población", "El Gini mide desigualdad en un momento, no la movilidad."),
    ],
    ctx=("abc", "Un municipio de ejemplo reparte útiles escolares solo a las familias del 40% de menores ingresos. ¿Qué principio ilustra?", "Equidad: dar más apoyo a quien tiene menos", "Igualdad estricta", "Monopolio", "Se considera la circunstancia de cada hogar."),
    sc=[
        ("¿Cómo se interpreta la razón entre el quinto y el primer quintil?", "Cuántas veces recibe más ingreso el grupo más alto que el más bajo", "La razón muestra la brecha entre ambos grupos."),
        ("En Economía y sociedad: ¿qué es un impuesto progresivo?", "Un impuesto con tasa mayor para quienes tienen más ingresos", "La tasa aumenta con el ingreso."),
        ("¿Qué argumento usan quienes cuestionan la redistribución?", "Que puede afectar los incentivos al trabajo y la inversión", "Es un argumento sobre los posibles efectos."),
    ],
    op=("Analiza un país de ejemplo con quintiles: 6%, 11%, 16%, 24%, 43%. Calcula cuántas veces recibe más el quinto que el primero. Con la regla de impuesto de la Ficha 40, calcula el impuesto de una persona con ingreso de $1.500.000 y otra de $3.500.000 (10% sobre lo que excede $1.000.000 hasta $3.000.000; 20% sobre lo que excede $3.000.000). "
        "Luego escribe un argumento a favor de aumentar la redistribución y uno en contra, y una pregunta que te harías antes de decidir.",
        "Razón: 43/6, un poco más de 7. Persona de $1.500.000: 50.000. Persona de $3.500.000: 200.000 más 100.000, o 300.000. A favor: mejora oportunidades. En contra: puede reducir incentivos. Pregunta: ¿cuánto cambia el esfuerzo de las personas con el impuesto?",
        ["calcula la razón entre quintiles", "calcula los impuestos con el sistema de la ficha", "presenta dos argumentos", "formula una pregunta pertinente"],
        ["tres cálculos y dos argumentos"],
        ["aplicar la tasa sobre todo el ingreso", "olvidar los tramos", "tomar partido sin argumentos"],
        "Pregunta: «¿sobre qué parte del ingreso se paga cada tasa?». Pide que lo escriba por tramos."),
    reinforce="Con la Ficha 40, calcula cuánto paga una persona con ingreso de $3.000.000 según el sistema de impuesto.",
    extend="Explica por qué la movilidad social y la desigualdad son conceptos distintos con un ejemplo.",
)

# ============================================================ OAC-08, clase 5
F = ("Ficha 41 (países de ejemplo, ficticios). País Norte (economía desarrollada) y País Sur (en vías de desarrollo). Datos de ejemplo: producción por habitante, Norte 200 y Sur 40 (miles de u.m.). Personas mayores de 65 años: Norte 22% de la población, Sur 8%. "
     "Trabajo informal (sin contrato): Norte 10% de los ocupados, Sur 45%. Gasto en investigación y desarrollo: Norte 2,5% de la producción, Sur 0,4%. Deuda pública: Norte 90% de la producción, Sur 50%.")
build(
    O8, 5, F,
    use="Aprenderé a comparar los desafíos de economías desarrolladas y en vías de desarrollo con indicadores, a evitar generalizaciones y a reconocer cómo se influyen mutuamente.",
    prior=["Conozco crecimiento, bienestar, equidad y sustentabilidad.", "Sé calcular razones y porcentajes.", "Sé interpretar una tabla de indicadores."],
    explain=[
        "Las economías suelen clasificarse como desarrolladas o en vías de desarrollo según su nivel de ingreso, su estructura productiva y otros indicadores. Esa clasificación es una simplificación: dentro de cada grupo hay países muy distintos, y un mismo país puede avanzar en unas áreas y quedar rezagado en otras. Por eso se comparan con indicadores concretos y no solo con la etiqueta.",
        "Los desafíos pueden diferir. Una economía desarrollada puede enfrentar el envejecimiento de la población y el financiamiento de pensiones y salud, el cuidado del ambiente y la desigualdad, además del desafío de seguir innovando. Una economía en vías de desarrollo puede enfrentar la informalidad laboral, la falta de infraestructura, la baja inversión en conocimiento, la dependencia de pocos productos y la necesidad de elevar los ingresos. Muchos desafíos se comparten: ambiente, desigualdad y estabilidad económica.",
        "Los países se influyen mutuamente: el crecimiento de uno afecta la demanda por los productos de otro, y los problemas ambientales y financieros cruzan las fronteras. Por eso se habla de cooperación, pero también hay desacuerdos sobre cómo repartir costos y responsabilidades. Una comparación honesta evita pensar que un grupo tiene «los problemas» y el otro «las soluciones», usa datos y reconoce los límites de los indicadores.",
    ],
    vocab=[("economía desarrollada", "economía de ingresos altos y estructura productiva avanzada"), ("economía en vías de desarrollo", "economía que busca elevar ingresos y mejorar su estructura productiva"), ("envejecimiento de la población", "aumento de la proporción de personas mayores"), ("informalidad laboral", "trabajo sin contrato ni protección legal"), ("investigación y desarrollo", "gasto en crear conocimiento y tecnología nueva"), ("deuda pública", "dinero que debe el Estado")],
    worked=[
        ("Comparar con una razón", "En dos países de ejemplo, uno gasta 3% de su producción en investigación y otro 0,5%. ¿Cuántas veces mayor es el primero?",
         ["Divide 3 por 0,5.", "El resultado es 6."],
         "6 veces"),
        ("Evitar una generalización", "Un periodista de ejemplo dice: «Todos los países en vías de desarrollo tienen un 45% de informalidad». ¿Qué problema tiene?",
         ["Generaliza a todo un grupo desde un caso.", "Los países de ese grupo son muy distintos."],
         "Generaliza a todo un grupo desde un caso"),
    ],
    mistakes=[("Creer que las etiquetas «desarrollado» y «en desarrollo» describen a todos por igual.", "Se simplifica.", "Compara con indicadores concretos."),
              ("Creer que un grupo solo tiene problemas y el otro soluciones.", "Se ignoran desafíos compartidos.", "Ambos grupos enfrentan desafíos, a veces distintos y a veces comunes.")],
    T=[
        ("=", "{F} ¿Cuántas veces es mayor la producción por habitante de Norte que la de Sur?", "200/40", "Se divide el valor de Norte por el de Sur."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de personas mayores de 65 años tiene Norte que Sur?", "22-8", "Se restan los porcentajes."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de trabajo informal tiene Sur que Norte?", "45-10", "Se restan los porcentajes."),
        ("abc", "{F} ¿Qué desafío es más probable que preocupe a Norte por su estructura de edades?", "El financiamiento de pensiones y salud por el envejecimiento", "La escasez de personas mayores", "La falta de energía", "La proporción de mayores es mayor."),
        ("abc", "{F} ¿Qué desafío muestra el dato de informalidad de Sur?", "Muchos trabajadores sin contrato ni protección legal", "Deuda pública alta", "Baja inversión en investigación", "45% de trabajo informal indica ese desafío."),
        ("abc", "En Economía y sociedad: ¿qué es la informalidad laboral?", "Trabajo sin contrato ni protección legal", "Trabajo en una empresa grande", "Trabajo de domingo", "Es una carencia de protección legal."),
        ("=", "{F} ¿Cuántas veces mayor es el gasto en investigación de Norte que el de Sur? (2,5 dividido por 0,4)", "2.5/0.4", "Se divide el gasto de Norte por el de Sur."),
        ("abc", "{F} ¿Qué país tiene mayor deuda pública en proporción a su producción?", "Norte", "Sur", "Iguales", "Norte tiene 90% y Sur 50%."),
        ("{F} Un analista dice: «Sur solo tiene problemas y Norte ninguno». ¿Qué dato de la ficha muestra que es una simplificación?", "Norte tiene una deuda pública alta y un envejecimiento importante", "También Norte enfrenta desafíos importantes y no es perfecto."),
        ("abc", "{F} Una política propone aumentar el gasto en investigación de Sur de 0,4% a 1%. ¿Qué indicador de la ficha cambiaría?", "El gasto en investigación y desarrollo", "La proporción de personas mayores", "El trabajo informal", "La política modifica directamente ese gasto."),
        ("abc", "{F} ¿Qué desafío comparten Norte y Sur aunque en distinta intensidad?", "La desigualdad y el cuidado del ambiente", "Ninguno", "El mismo nivel de ingreso", "Son desafíos comunes de muchas economías."),
        ("abc", "Un periodista afirma: «Cuando Norte crece, Sur no se ve afectado». ¿Qué corrección harías?", "Pueden influirse mediante el comercio y las finanzas", "Es correcto, porque cada país vive aislado", "Solo se influyen si comparten idioma", "Hay interdependencia entre las economías de ambos países."),
        ("abc", "«Los países desarrollados deberían pagar más del costo de la transición ambiental» es una afirmación…", "Normativa, porque expresa un juicio sobre responsabilidades", "Positiva, porque se verifica con datos", "Falsa", "La frase propone un deber según ciertos valores."),
    ],
    ctx=("abc", "Un país de ejemplo de ingresos medios tiene alto trabajo informal, pero también un buen desempeño en educación. ¿Qué conclusión es adecuada?", "Tiene fortalezas y desafíos, y no cabe en una sola etiqueta", "Es un país desarrollado en todo", "No tiene desafíos", "Los países combinan avances y rezagos."),
    sc=[
        ("¿Por qué es una simplificación hablar de países «desarrollados» y «en desarrollo»?", "Porque dentro de cada grupo hay países muy distintos", "Se compara mejor con indicadores concretos."),
        ("Nombra un desafío de una economía desarrollada y uno de una en vías de desarrollo.", "Envejecimiento y financiamiento de pensiones; informalidad o infraestructura", "Los desafíos pueden diferir entre tipos de economía."),
        ("En Economía y sociedad: ¿qué es la deuda pública?", "El dinero que debe el Estado", "Se compara con el tamaño de la economía."),
    ],
    op=("Compara dos países de ejemplo con estos datos. País Alto: producción por habitante 150, mayores de 65 años 20%, informalidad 12%, gasto en investigación 2,2%. País Medio: producción por habitante 50, mayores de 65 años 9%, informalidad 40%, gasto en investigación 0,5%. "
        "Calcula cuántas veces mayor es la producción por habitante de Alto y su gasto en investigación (en razón), identifica un desafío probable de cada país y uno compartido, y escribe una frase que evite generalizar.",
        "Producción por habitante: 150/50 son 3 veces. Investigación: 2,2/0,5 son 4,4 veces. Alto: envejecimiento. Medio: informalidad. Compartido: ambiente. Frase: con estos datos de ejemplo, Medio enfrenta más informalidad, pero esto no vale para todos los países en vías de desarrollo.",
        ["calcula las razones", "relaciona indicadores con desafíos", "nombra un desafío compartido", "evita generalizar"],
        ["dos cálculos y tres frases"],
        ["dividir al revés", "atribuir un desafío sin dato", "generalizar a todos los países"],
        "Pregunta: «¿esta frase vale solo para estos dos países o para todos?». Pide que la reescriba."),
    reinforce="Con la Ficha 41, escribe dos desafíos distintos para cada país, apoyados en un dato.",
    extend="Explica cómo la economía de un país puede afectar a otro a través del comercio y las finanzas, con un ejemplo.",
)

# ============================================================ OAC-08, clase 6
F = ("Ficha 42 (opciones de ejemplo, ficticias). País Árbol quiere reducir emisiones. Opciones y efectos estimados de ejemplo: "
     "Opción 1, impuesto a las emisiones: reduce 10% las emisiones, cuesta 0,5 puntos de la producción y pesa más en hogares de menores ingresos. "
     "Opción 2, subsidio a energía renovable: reduce 6% las emisiones y cuesta 0,3 puntos de la producción. "
     "Opción 3, norma de eficiencia para los equipos: reduce 8% las emisiones y cuesta 0,2 puntos de la producción, con menos efecto en los hogares.")
build(
    O8, 6, F,
    use="Aprenderé a comunicar una conclusión situada sobre un desafío actual (crecimiento, interdependencia, sustentabilidad o equidad), con evidencia, costos, límites y una mirada alternativa.",
    prior=["Conozco los desafíos de crecimiento, interdependencia, sustentabilidad y equidad.", "Sé evaluar alternativas con criterios.", "Sé escribir una conclusión situada."],
    explain=[
        "Los desafíos actuales de las economías, como el crecimiento, la interdependencia, la sustentabilidad y la equidad, suelen entrar en tensión: una medida puede ayudar a uno y complicar otro. Por eso la evaluación de una política debe considerar varios criterios a la vez, como el efecto buscado, el costo, a quién afecta más y qué riesgos tiene.",
        "Una forma de comparar es calcular el costo por unidad de resultado, por ejemplo cuántos puntos de la producción cuesta cada punto de reducción de emisiones. Ese número ayuda, pero no decide solo: una política más barata puede tener un efecto pequeño o recaer sobre grupos con menos recursos. Entonces se combinan cálculos con juicios de valor, y se explica cuáles se priorizan.",
        "Comunicar una conclusión situada consiste en decir qué se concluye, con qué evidencia, bajo qué condiciones, con qué límites y qué otra mirada razonable existe. Se evita decir «la mejor política es X» sin más. En cambio, se escribe, por ejemplo: «con estos datos de ejemplo, la opción 3 tiene el menor costo por punto de reducción, pero reduce menos que la opción 1; quien priorice reducir más podría preferir otra».",
    ],
    vocab=[("costo por unidad de resultado", "costo dividido por el resultado logrado"), ("tensión entre objetivos", "situación en que lograr uno dificulta otro"), ("criterio múltiple", "evaluar con varios criterios a la vez"), ("efecto distributivo", "forma en que una política reparte costos y beneficios"), ("conclusión situada", "afirmación con evidencia, condiciones y límites"), ("mirada alternativa", "otra interpretación razonable")],
    worked=[
        ("Calcular el costo por punto", "Una política de ejemplo reduce 5% las emisiones y cuesta 0,5 puntos de la producción. ¿Cuánto cuesta cada punto de reducción?",
         ["Divide el costo por la reducción.", "0,5 dividido por 5."],
         "0,1 puntos de la producción"),
        ("Escribir una conclusión situada", "Con datos de ejemplo: la política A reduce 4% y la B reduce 8%, y la B cuesta el doble. Escribe una conclusión prudente.",
         ["Afirma lo que muestran los datos y declara el alcance.", "Incluye la mirada alternativa."],
         "Con estos datos de ejemplo, B reduce más, pero cuesta el doble; quien priorice el costo podría preferir A"),
    ],
    mistakes=[("Elegir la política con el menor costo por punto sin mirar cuánto reduce ni a quién afecta.", "Se usa un solo criterio.", "Combina costo, efecto total y efecto distributivo."),
              ("Presentar una conclusión como universal.", "Se omiten condiciones y límites.", "Indica el caso, la evidencia, los límites y otra mirada.")],
    T=[
        ("=", "{F} ¿Cuántos puntos de la producción cuesta cada punto de reducción con la Opción 1?", "0.5/10", "Se divide el costo por la reducción."),
        ("=", "{F} ¿Cuántos puntos de la producción cuesta cada punto de reducción con la Opción 2?", "0.3/6", "Se divide el costo por la reducción."),
        ("=", "{F} ¿Cuántos puntos de la producción cuesta cada punto de reducción con la Opción 3?", "0.2/8", "Se divide el costo por la reducción."),
        ("abc", "{F} ¿Qué opción tiene el menor costo por punto de reducción?", "La Opción 3", "La Opción 1", "La Opción 2", "Cuesta 0,025 frente a 0,05 de las otras dos."),
        ("abc", "{F} ¿Qué opción reduce más las emisiones?", "La Opción 1", "La Opción 2", "La Opción 3", "La opción 1 reduce 10%, la mayor reducción."),
        ("abc", "En Economía y sociedad: ¿qué es un efecto distributivo?", "La forma en que una política reparte costos y beneficios", "El tamaño del presupuesto", "Una tasa de interés", "Indica quién gana y quién paga."),
        ("abc", "{F} ¿Qué opción pesa más en hogares de menores ingresos?", "La Opción 1", "La Opción 2", "La Opción 3", "La ficha lo indica para el impuesto."),
        ("=", "{F} Si se aplicaran las Opciones 2 y 3 juntas y sus efectos se sumaran, ¿cuántos puntos de reducción lograrían?", "6+8", "Se suman las reducciones."),
        ("=", "{F} Con las Opciones 2 y 3 juntas, ¿cuántos puntos de la producción costarían en total?", "0.3+0.2", "Se suman los costos."),
        ("abc", "{F} Una concejala dice: «La Opción 3 es la mejor porque es la más barata por punto». ¿Qué le falta considerar?", "Que reduce menos que la Opción 1 y no se sabe si alcanza la meta", "Nada, es perfecta", "Que no reduce nada", "Un solo criterio no basta para decidir."),
        ("abc", "{F} Otro concejal dice: «La Opción 1 es la mejor porque reduce más». ¿Qué le falta considerar?", "Su costo y su efecto en hogares de menores ingresos", "Nada, es la mejor", "Que no tiene costos", "También importan el costo y quién paga."),
        ("abc", "{F} ¿Cuál de estas frases es una conclusión situada con los datos de la ficha?", "Con estos datos de ejemplo, la Opción 3 tiene el menor costo por punto de reducción, pero reduce menos que la 1; quien priorice reducir más podría preferir la 1", "La Opción 3 es la mejor política para cualquier país", "La Opción 1 es la peor porque pesa más en algunos hogares", "Incluye evidencia, alcance y mirada alternativa, y no generaliza."),
        ("abc", "«El Estado debería priorizar la equidad antes que la reducción de emisiones» es una afirmación…", "Normativa, porque expresa una prioridad según valores", "Positiva, porque se verifica con datos", "Falsa", "La frase dice qué debería hacerse según valores."),
    ],
    ctx=("abc", "Un municipio de ejemplo compara dos medidas para disminuir los residuos: la A reduce 20% y cuesta $40 millones; la B reduce 10% y cuesta $15 millones. ¿Cuál tiene menor costo por punto de reducción?", "La B, con $1,5 millones por punto", "La A, con $2 millones por punto", "Ambas igual", "A cuesta 2 por punto y B cuesta 1,5."),
    sc=[
        ("¿Cómo se calcula el costo por unidad de resultado?", "Dividiendo el costo por el resultado", "Este cálculo permite comparar políticas distintas."),
        ("¿Qué partes tiene una conclusión situada?", "Afirmación, evidencia, condiciones, límites y mirada alternativa", "Evita decir que algo vale para todos los casos."),
        ("En Economía y sociedad: ¿por qué los desafíos actuales entran en tensión?", "Porque lograr un objetivo puede dificultar otro", "Por ejemplo, reducir emisiones puede afectar el costo de vida."),
    ],
    op=("Escribe una conclusión situada de cinco a seis líneas sobre una de estas dos decisiones de ejemplo. Decisión 1: elegir entre las tres opciones de la Ficha 42. Decisión 2: reducir la desigualdad con un impuesto progresivo o con transferencias a las familias de menores ingresos, usando datos que inventes y rotules como «de ejemplo». "
        "Incluye: qué opción te parece mejor y por qué, la evidencia (con cifras), el costo o efecto distributivo, un límite de los datos y la mejor objeción.",
        "Decisión 1. Con estos datos de ejemplo elijo la Opción 3 porque cuesta 0,025 puntos por punto de reducción y pesa menos en los hogares. Reduce 8%, menos que la Opción 1 (10%). Los datos son de ejemplo y no incluyen efectos en el empleo. Objeción: quien quiera reducir más preferirá la Opción 1.",
        ["justifica la elección con cifras", "menciona costo o efecto distributivo", "declara un límite", "presenta la mejor objeción"],
        ["párrafo de cinco a seis líneas"],
        ["decir que la elección es la única razonable", "no declarar límites", "usar cifras sin rotular como de ejemplo"],
        "Pregunta: «¿qué diría una persona que prioriza otro valor?». Pide que escriba su objeción."),
    reinforce="Calcula el costo por punto de reducción de las tres opciones y escribe cuál elegirías si el criterio fuera solo el costo, y cuál si fuera solo el efecto total.",
    extend="Elige dos desafíos de las clases anteriores que entren en tensión y explica por qué una medida para uno puede complicar al otro.",
)
