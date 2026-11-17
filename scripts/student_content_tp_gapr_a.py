"""Gastronomía TP 4.º medio, mención Pastelería y Repostería: OAM-01 (masas y pastas según la formulación de recetas), OAM-02 (dulces, cremas y glaseados), OAM-03 (tortas, pasteles y postres). Todo en papel, sin recetas ni técnicas de elaboración paso a paso: formulaciones, rendimientos y costos con datos «de ejemplo»."""
from __future__ import annotations

from tp_gapr_common import build

O1 = "TP-GAPR-4-OAM-01"
O2 = "TP-GAPR-4-OAM-02"
O3 = "TP-GAPR-4-OAM-03"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: la práctica en obrador requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); no te habilita para trabajar."

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (obrador de ejemplo, inventado). En pastelería y repostería se elaboran productos dulces, como tortas, pasteles, galletas y postres. Una masa es una mezcla de ingredientes con consistencia firme, que permite darle forma; una pasta es una mezcla más blanda, que se vierte en un molde. "
     "Formulación: lista de ingredientes con sus cantidades, que fija cómo debe ser el producto. Alérgenos frecuentes en pastelería: gluten (harina de trigo), huevo, leche y frutos secos. "
     "Equipos del obrador: batidora, amasadora, horno y balanza. La autoridad sanitaria fiscaliza la higiene y el rotulado según la norma vigente.")
build(
    O1, 1, F,
    use="Aprenderé a situar el trabajo de masas y pastas: qué son, qué es una formulación, qué alérgenos son frecuentes y qué riesgos y normas existen.",
    prior=["Conozco la receta estándar y los alérgenos.", "Sé multiplicar y dividir.", "Conozco el rótulo y el orden por riesgo."],
    explain=[
        "En Pastelería y Repostería se elaboran productos dulces como tortas, pasteles, galletas y postres. Las masas y pastas son las mezclas base de muchos de ellos. Una masa tiene consistencia firme, que permite darle forma; una pasta es más blanda y se vierte en un molde. Lo que define cómo debe ser cada una es su formulación, la lista de ingredientes con sus cantidades.",
        "Seguir la formulación es esencial: en pastelería, un cambio pequeño de cantidad puede alterar mucho el resultado. Por eso los ingredientes se pesan con balanza, no se miden a ojo. Los alérgenos más frecuentes son el gluten de la harina de trigo, el huevo, la leche y los frutos secos, y deben declararse en el rótulo.",
        "El trabajo en un obrador implica riesgos con equipos y calor, y requiere higiene estricta de manos, utensilios y superficies. Aquí solo se estudian conceptos, formulaciones y cálculos en papel; las técnicas se practican con instructor y la norma vigente. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("masa", "mezcla firme que permite darle forma"), ("pasta", "mezcla blanda que se vierte en un molde"), ("formulación", "lista de ingredientes con sus cantidades"), ("obrador", "lugar donde se elaboran productos de pastelería"), ("pesaje", "medición de ingredientes en balanza")],
    worked=[
        ("Clasificar una mezcla", "Una mezcla de ejemplo es tan blanda que se vierte en un molde. ¿Es una masa o una pasta?", ["Una masa es firme y se moldea.", "Una mezcla blanda que se vierte es una pasta."], "Una pasta"),
        ("Calcular unidades de un lote", "Un lote de ejemplo da 24 unidades y se hacen 3 lotes. ¿Cuántas unidades son?", ["Se multiplican los lotes por las unidades de cada uno.", "3 × 24 = 72."], "72 unidades"),
    ],
    mistakes=[("Medir los ingredientes «a ojo» para ir más rápido.", "Un cambio pequeño de cantidad altera mucho el resultado.", "Pesa los ingredientes en balanza, según la formulación."),
              ("Omitir el gluten del rótulo porque «solo es harina».", "La harina de trigo contiene gluten y una persona puede reaccionar.", "Declara los alérgenos presentes en cada producto.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿qué es una formulación?", "La lista de ingredientes con sus cantidades", "El horario de producción del obrador", "El nombre comercial del producto", "La formulación fija cantidades que definen cómo debe ser el producto."),
        ("abc", "{F} ¿Cómo se diferencia una masa de una pasta?", "La masa es firme y se moldea; la pasta es blanda y se vierte en un molde", "La masa es siempre dulce y la pasta salada", "La masa se vende y la pasta no", "La ficha las distingue por su consistencia."),
        ("abc", "{F} ¿Qué alérgeno aporta la harina de trigo?", "Gluten", "Huevo", "Leche", "La ficha asocia el gluten a la harina de trigo."),
        ("=", "Un obrador de ejemplo hace 4 lotes de una masa y cada lote da 30 unidades. ¿Cuántas unidades son?", "4*30", "Se multiplican los lotes por las unidades de cada lote.", " unidades"),
        ("abc", "{F} ¿Con qué equipo se verifica la cantidad de cada ingrediente de la formulación?", "Con una balanza", "Con una batidora", "Con un horno", "La balanza es el equipo de pesaje de los ingredientes."),
        ("abc", "{F} Un ayudante pesa la harina «a ojo» porque «le sale parecido». ¿Qué corresponde?", "Pesarla en balanza según la formulación", "Aceptarlo si la masa se ve bien", "Pesar solo la mitad de los ingredientes", "Una diferencia pequeña de cantidad puede alterar el producto."),
        ("abc", "{F} ¿Cuál de estos es un alérgeno frecuente en pastelería según la ficha?", "Los frutos secos", "El azúcar", "El agua", "La ficha incluye los frutos secos entre los alérgenos frecuentes."),
        ("=", "Un obrador de ejemplo produce 360 unidades por día en 6 lotes iguales. ¿Cuántas unidades tiene cada lote?", "360//6", "Se divide el total de unidades por el número de lotes.", " unidades"),
        ("abc", "{F} Un cliente alérgico al huevo pregunta por una masa que lleva huevo en su formulación. ¿Qué corresponde?", "Informar que contiene huevo según la formulación", "Decir que no tiene huevo para evitar dudas", "Decir que no se sabe", "La respuesta se basa en la formulación, sin suposiciones."),
        ("abc", "Un compañero dice que los equipos de un obrador son seguros porque son de uso común. ¿Qué respuesta es correcta?", "Los equipos tienen riesgos y se usan solo con capacitación y autorización", "Tiene razón, no hay riesgos", "Solo hay riesgo con el horno", "Todo equipo con partes en movimiento o calor requiere capacitación."),
        ("abc", "{F} Una persona del obrador siente un malestar después de manipular un producto. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Darle un remedio casero", "Esperar a que se le pase", "Ante un malestar se pide ayuda de personal capacitado."),
        ("=", "{F} Una formulación de ejemplo rinde 40 unidades de 50 g. ¿Cuántos gramos de masa son en total?", "40*50", "Se multiplican las unidades por el peso de cada una.", " g"),
        ("abc", "{F} ¿Por qué se exige higiene estricta de manos, utensilios y superficies?", "Para evitar la contaminación de los productos y proteger a quienes los consumen", "Para que el obrador se vea más ordenado", "Para reducir el tiempo de pesaje", "Los productos de pastelería, listos para comer, no se cocinan de nuevo y deben protegerse."),
    ],
    ctx=("abc", "{F} La jefa de producción nota que dos ayudantes usan cantidades distintas de azúcar para la misma masa. ¿Qué debe hacer?", "Aclarar que se usa la formulación vigente, pesar en balanza y registrar cualquier cambio con autorización", "Dejar que cada uno use su cantidad", "Elegir la más barata sin avisar", "Una sola formulación asegura un producto constante."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es una masa?", "Una mezcla firme que permite darle forma", "Se distingue de la pasta, que es blanda."),
        ("¿Cómo se miden los ingredientes?", "Pesándolos en balanza", "Una diferencia pequeña puede cambiar el resultado."),
        ("¿Qué alérgenos son frecuentes en pastelería?", "Gluten, huevo, leche y frutos secos", "Son los que más se emplean en estos productos."),
    ],
    op=("Un obrador de ejemplo elabora tres productos: una masa de galletas (con harina de trigo, mantequilla y huevo), una pasta de bizcocho (con harina de trigo, huevo y leche) y una masa de pan dulce (con harina de trigo y leche). Cada producto se produce en lotes de 30 unidades. "
        "Escribe: (a) qué producto es una pasta, (b) los alérgenos que declararías para cada producto, (c) cuántas unidades hay si se producen 2 lotes de cada uno, y (d) una regla de higiene general.",
        "(a) La pasta de bizcocho, que es blanda y se vierte en un molde. (b) Galletas: gluten, huevo y leche (mantequilla). Bizcocho: gluten, huevo y leche. Pan dulce: gluten y leche. (c) 3 productos × 2 lotes × 30 = 180 unidades. (d) Lavarse las manos antes de manipular y mantener limpios los utensilios y las superficies.",
        ["identifica la pasta", "declara alérgenos por producto", "calcula 180 unidades y nombra una regla de higiene"],
        ["hoja con cuatro respuestas"],
        ["olvidar el gluten", "calcular solo un lote", "describir cómo elaborar los productos"],
        "Pregunta: «¿qué alérgenos lleva el pan dulce?». Debe nombrar gluten y leche."),
    reinforce="Escribe tres productos de pastelería inventados y clasifica su mezcla como masa o pasta.",
    extend="Explica por qué pesar los ingredientes ayuda a que un producto sea siempre igual.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (formulación en porcentajes de ejemplo, inventada). «Masa dulce de ejemplo», con la harina como base de 1.000 g (100 %): azúcar 300 g (30 %), mantequilla 400 g (40 %), huevo 200 g (20 %), leudante 20 g (2 %), sal 10 g (1 %) y agua 70 g (7 %). Total: 2.000 g. "
     "Función de los ingredientes: la harina aporta estructura; el azúcar, dulzor; la mantequilla, textura tierna; el huevo, une los ingredientes; el leudante hace que el producto aumente de volumen; la sal, sabor. "
     "Roles: el pastelero elabora; el ayudante apoya y pesa bajo supervisión; la jefa de producción aprueba las formulaciones.")
build(
    O1, 2, F,
    use="Aprenderé a leer una formulación en porcentajes, a reconocer la función de cada ingrediente y a calcular cantidades para distintos lotes.",
    prior=["Conozco la formulación y el pesaje.", "Sé calcular porcentajes.", "Sé multiplicar y dividir."],
    explain=[
        "En pastelería, muchas formulaciones se escriben en porcentajes respecto de la harina: la harina es el 100 % y los demás ingredientes se expresan como una parte de ella. El porcentaje de un ingrediente se calcula con su cantidad multiplicada por 100 y dividida por el peso de la harina. Así es fácil preparar un lote mayor o menor manteniendo las proporciones.",
        "Cada ingrediente tiene una función: la harina aporta estructura; el azúcar, dulzor; la grasa, como la mantequilla, textura tierna; el huevo une los ingredientes; el leudante hace que el producto aumente de volumen; y la sal da sabor. Conocer las funciones ayuda a entender por qué un cambio de cantidad altera el producto.",
        "Los roles son: el pastelero elabora, el ayudante apoya bajo supervisión y la jefa de producción aprueba las formulaciones. Las cantidades de esta ficha son de ejemplo y no describen cómo elaborar el producto." + LIM,
    ],
    vocab=[("formulación en porcentajes", "ingredientes expresados como parte del peso de la harina"), ("estructura", "firmeza que da forma al producto"), ("leudante", "ingrediente que hace aumentar el volumen"), ("textura", "sensación al tocar o comer el producto"), ("proporción", "relación entre las cantidades de los ingredientes")],
    worked=[
        ("Calcular un porcentaje", "En una formulación de ejemplo con 500 g de harina, el azúcar pesa 150 g. ¿Qué porcentaje de la harina es?", ["Se multiplica por 100 y se divide por la harina.", "150 × 100 ÷ 500 = 30."], "30 %"),
        ("Escalar una cantidad", "Si la harina pasa de 500 g a 1.500 g, ¿por cuánto se multiplican los demás ingredientes?", ["Se divide la harina nueva por la anterior.", "1.500 ÷ 500 = 3."], "Por 3"),
    ],
    mistakes=[("Cambiar un ingrediente sin mantener su porcentaje respecto de la harina.", "Las proporciones se alteran y el producto sale distinto.", "Escala todos los ingredientes por el mismo factor."),
              ("Creer que el leudante se puede aumentar para que el producto «suba más».", "Un exceso altera el producto y su estructura.", "Respeta la cantidad de la formulación y consulta a la jefa antes de modificarla.")],
    T=[
        ("abc", "{F} ¿Qué porcentaje de la harina representa la mantequilla?", "40 %", "30 %", "20 %", "400 g sobre 1.000 g de harina equivalen al 40 %."),
        ("abc", "{F} ¿Qué función cumple la harina?", "Aporta estructura", "Aporta dulzor", "Hace aumentar el volumen", "La ficha asigna la estructura a la harina."),
        ("abc", "{F} ¿Qué ingrediente hace que el producto aumente de volumen?", "El leudante", "El huevo", "La sal", "La ficha atribuye ese efecto al leudante."),
        ("=", "{F} ¿Qué porcentaje de la harina representa el azúcar?", "300*100//1000", "Se multiplican los gramos de azúcar por 100 y se dividen por los de la harina.", " %"),
        ("=", "{F} ¿Cuántos gramos suman todos los ingredientes?", "1000+300+400+200+20+10+70", "Se suman las cantidades de los siete ingredientes.", " g"),
        ("=", "{F} Si la harina pasa a 3.000 g, ¿cuántos gramos de mantequilla se necesitan?", "400*3", "Se multiplica la mantequilla por el mismo factor que la harina.", " g"),
        ("=", "{F} Con harina de 2.500 g, ¿cuántos gramos de azúcar corresponden al 30 %?", "2500*30//100", "Se calcula el 30 % de la harina.", " g"),
        ("abc", "{F} ¿Quién aprueba las formulaciones?", "La jefa de producción", "El ayudante", "El pastelero", "La ficha asigna la aprobación a la jefa de producción."),
        ("abc", "{F} Un ayudante agrega más leudante «para que suba más». ¿Qué observación corresponde?", "No se modifica la cantidad sin autorización: un exceso altera el producto", "Está bien, porque suba más es mejor", "Está bien si se agrega la mitad", "Un cambio de cantidad cambia las proporciones y el resultado."),
        ("=", "{F} Si el agua fuera de 7 % y la harina de 4.000 g, ¿cuántos gramos de agua corresponden?", "4000*7//100", "Se calcula el 7 % de la harina.", " g"),
        ("abc", "{F} ¿Qué ingrediente da textura tierna?", "La mantequilla", "La sal", "El agua", "La ficha lo atribuye a la mantequilla."),
        ("abc", "Un compañero dice que, como el porcentaje de sal es solo el 1 %, no importa pesarla. ¿Qué respuesta es correcta?", "Todo ingrediente se pesa según la formulación: una pequeña diferencia afecta el sabor", "Tiene razón, el 1 % no importa", "Solo hay que pesar los ingredientes grandes", "Incluso las cantidades pequeñas influyen en el producto."),
        ("=", "{F} Si el pedido requiere el doble de la formulación, ¿cuántos gramos de masa total se obtienen?", "2000*2", "Se multiplica el peso total por 2.", " g"),
    ],
    ctx=("abc", "{F} Un ayudante nuevo comenta que el huevo «no hace falta» porque la masa «se junta igual». ¿Qué debe responder el pastelero?", "Que el huevo cumple una función de unión y que cada ingrediente de la formulación se mantiene", "Que puede omitirlo si la masa se ve bien", "Que lo cambie por más agua", "Las funciones de los ingredientes explican por qué no se omiten sin autorización."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es el 100 % en una formulación en porcentajes?", "El peso de la harina", "Los demás ingredientes se expresan respecto de ella."),
        ("¿Qué aporta el azúcar?", "Dulzor", "Es su función principal en la formulación."),
        ("¿Quién aprueba una formulación?", "La jefa de producción", "Asegura constancia y calidad en cada producto."),
    ],
    op=("Formulación de ejemplo con harina de 800 g (100 %): azúcar 240 g, mantequilla 320 g, huevo 160 g, leudante 16 g, sal 8 g. "
        "Calcula el porcentaje de cada ingrediente respecto de la harina, el peso total, y cuántos gramos de cada ingrediente se necesitan si la harina pasa a 2.400 g; indica además qué ingrediente da dulzor y cuál hace aumentar el volumen.",
        "Porcentajes: azúcar 30 %, mantequilla 40 %, huevo 20 %, leudante 2 %, sal 1 %. Peso total: 800 + 240 + 320 + 160 + 16 + 8 = 1.544 g. Con harina de 2.400 g el factor es 3: azúcar 720 g, mantequilla 960 g, huevo 480 g, leudante 48 g, sal 24 g. El azúcar da dulzor y el leudante hace aumentar el volumen.",
        ["calcula los cinco porcentajes", "calcula el peso total y el factor 3", "nombra las dos funciones"],
        ["hoja con cálculos y funciones"],
        ["calcular el porcentaje sobre el total y no sobre la harina", "usar 2.400 como factor", "olvidar un ingrediente"],
        "Pregunta: «¿sobre qué peso se calcula cada porcentaje?». Debe responder sobre la harina."),
    reinforce="Inventa una formulación de cinco ingredientes con harina de 600 g y calcula el porcentaje de cada uno.",
    extend="Explica por qué las formulaciones en porcentajes facilitan elaborar lotes de distinto tamaño.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso de producción de ejemplo, inventado). Formulación de la «Masa dulce de ejemplo» para 2.000 g de masa: harina 1.000 g, azúcar 300 g, mantequilla 400 g, huevo 200 g, leudante 20 g, sal 10 g y agua 70 g. Unidad de producto: 50 g de masa. "
     "Pedido: 400 unidades. Existencias en bodega: harina 8.000 g, azúcar 3.500 g, mantequilla 3.600 g, huevo 2.500 g, leudante 300 g, sal 200 g y agua suficiente.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de producción de masas en papel: calcular el factor de escala, las cantidades y los faltantes, y decidir con la jefa de producción.",
    prior=["Conozco la formulación en porcentajes.", "Sé calcular el factor de escala.", "Sé restar cantidades."],
    explain=[
        "Para producir una cantidad de unidades se calcula primero el peso total de masa necesario: unidades por peso de cada unidad. Luego el factor de escala se obtiene dividiendo ese peso por el peso total de la formulación. Cada ingrediente se multiplica por el factor y se compara con las existencias de bodega.",
        "Si algún ingrediente no alcanza, se calcula el faltante y se decide con la jefa de producción: pedir lo que falta, producir menos unidades o reprogramar. Los ingredientes no se sustituyen ni se cambian las cantidades para que alcance, porque se altera el producto.",
        "Un análisis ordenado anota los datos, calcula, compara y deja una decisión. Todas las cantidades son de ejemplo y el cálculo se hace en papel." + LIM,
    ],
    vocab=[("peso total de masa", "unidades por peso de cada unidad"), ("factor de escala", "peso necesario dividido por el peso de la formulación"), ("existencias", "cantidad disponible en bodega"), ("faltante", "cantidad que falta para cubrir lo necesario"), ("reprogramar", "cambiar el momento de producción")],
    worked=[
        ("Calcular el peso total", "Se piden 60 unidades de 80 g de ejemplo. ¿Cuántos gramos de masa se necesitan?", ["Se multiplican las unidades por el peso de cada una.", "60 × 80 = 4.800."], "4.800 g"),
        ("Calcular el factor", "Una formulación de ejemplo pesa 1.200 g y se necesitan 4.800 g. ¿Cuál es el factor?", ["Se divide el peso necesario por el de la formulación.", "4.800 ÷ 1.200 = 4."], "4"),
    ],
    mistakes=[("Calcular el factor usando las unidades pedidas en lugar del peso total.", "Las cantidades resultan muy distintas a las reales.", "Calcula el peso total de masa y divídelo por el peso de la formulación."),
              ("Cambiar la cantidad de mantequilla para que alcance con las existencias.", "Se altera la proporción del producto.", "Calcula el faltante y decide con la jefa de producción.")],
    T=[
        ("=", "{F} ¿Cuántos gramos de masa se necesitan para las 400 unidades?", "400*50", "Se multiplican las unidades por el peso de cada una.", " g"),
        ("=", "{F} ¿Cuál es el factor de escala?", "20000//2000", "Se divide el peso necesario por el peso de la formulación.", ""),
        ("=", "{F} ¿Cuántos gramos de harina se necesitan?", "1000*10", "Se multiplica la harina de la formulación por el factor 10.", " g"),
        ("=", "{F} ¿Cuántos gramos de harina faltan?", "1000*10-8000", "A la harina necesaria se le restan las existencias.", " g"),
        ("=", "{F} ¿Cuántos gramos de mantequilla se necesitan?", "400*10", "Se multiplica la mantequilla de la formulación por el factor 10.", " g"),
        ("=", "{F} ¿Cuántos gramos de mantequilla faltan?", "400*10-3600", "A la mantequilla necesaria se le restan las existencias.", " g"),
        ("abc", "{F} ¿Alcanza el huevo de bodega?", "Sí: se necesitan 2.000 g y hay 2.500 g", "No: se necesitan 3.000 g", "No: se necesitan 2.600 g", "200 g por 10 dan 2.000 g, que es menos que las existencias."),
        ("abc", "{F} ¿Alcanza el azúcar de bodega?", "Sí: se necesitan 3.000 g y hay 3.500 g", "No: se necesitan 4.000 g", "No: se necesitan 3.600 g", "300 g por 10 dan 3.000 g, menos que las existencias."),
        ("=", "{F} ¿Cuántos gramos de sal se necesitan para el pedido?", "10*10", "Se multiplica la sal de la formulación por el factor 10.", " g"),
        ("abc", "{F} ¿Qué ingredientes no alcanzan?", "La harina y la mantequilla", "Solo la mantequilla", "El azúcar y el huevo", "Faltan 2.000 g de harina y 400 g de mantequilla."),
        ("abc", "{F} ¿Qué decisión corresponde ante los faltantes?", "Consultar a la jefa de producción para pedir lo que falta, producir menos unidades o reprogramar", "Reducir la harina y la mantequilla de la formulación", "Producir igual y esperar que alcance", "Se resuelve con más ingredientes, menos unidades o reprogramación, no alterando la formulación."),
        ("=", "{F} Con las existencias de harina, ¿cuántas unidades de 50 g se pueden producir como máximo, considerando solo la harina?", "8000//1000*40", "Se calcula cuántas formulaciones permite la harina y se multiplican por las 40 unidades de cada una.", " unidades"),
        ("abc", "{F} Un compañero propone usar menos mantequilla en todas las unidades «para que alcance». ¿Qué observación corresponde?", "Cambia el producto y requiere autorización; mejor calcular el faltante y decidir con la jefa", "Es válido, porque nadie lo nota", "Es válido si se hace solo en las últimas unidades", "Un cambio de cantidad altera el producto y sus proporciones."),
    ],
    ctx=("abc", "{F} Al día siguiente, el proveedor entrega la harina y la mantequilla faltantes. ¿Qué debe hacer el encargado de bodega antes de usarlas?", "Recibirlas contra la orden, rotularlas y registrar las cantidades en el inventario", "Usarlas de inmediato sin registrar", "Almacenarlas sin revisar la orden", "Toda recepción se compara con el pedido, se rotula y se registra."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calcula el peso total de masa?", "Unidades por el peso de cada una", "Es el peso total que debe producirse."),
        ("¿Cómo se calcula el factor de escala?", "Peso necesario dividido por el peso de la formulación", "Indica por cuánto se multiplica cada ingrediente."),
        ("¿Qué se hace con un faltante?", "Se decide con la jefa de producción", "Nunca se altera la formulación para que alcance."),
    ],
    op=("Formulación de ejemplo de una «Pasta de bizcocho de ejemplo» para 1.500 g: harina 500 g, azúcar 400 g, huevo 450 g, leche 150 g. Pedido: 60 unidades de 150 g. Existencias: harina 4.000 g, azúcar 3.000 g, huevo 4.000 g, leche 1.000 g. "
        "Calcula el peso total, el factor, las cantidades necesarias, los faltantes y propón una decisión con la jefa.",
        "Peso total: 60 × 150 = 9.000 g. Factor: 9.000 ÷ 1.500 = 6. Harina: 3.000 g (alcanza). Azúcar: 2.400 g (alcanza). Huevo: 2.700 g (alcanza). Leche: 900 g (alcanza). No hay faltantes. Decisión: se puede producir todo el pedido con las existencias.",
        ["calcula 9.000 g y el factor 6", "calcula las cuatro cantidades", "verifica que alcanzan y decide"],
        ["hoja con cálculos y decisión"],
        ["usar 60 como factor", "no comparar con las existencias", "inventar un faltante"],
        "Pregunta: «¿cuántos gramos de leche necesitas?». Si no responde 900, repasa el factor."),
    reinforce="Inventa una formulación de cuatro ingredientes y un pedido, y calcula el factor y los faltantes con existencias inventadas.",
    extend="Explica por qué es mejor reprogramar una producción que reducir ingredientes para que alcance.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (costeo de la masa dulce de ejemplo, inventado). Formulación para 2.000 g, que rinde 40 unidades de 50 g. Precios de ejemplo por kilo: harina $1.200; azúcar $1.000; mantequilla $6.000; huevo $3.000; leudante $8.000; sal $2.000 (el agua no tiene costo). "
     "Cantidades: harina 1.000 g, azúcar 300 g, mantequilla 400 g, huevo 200 g, leudante 20 g y sal 10 g. Costo objetivo: 30 % del precio de venta. Pérdida de producción de ejemplo: 5 % de las unidades.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: costear una formulación, calcular el costo y el precio por unidad y considerar la pérdida de producción.",
    prior=["Conozco el costeo y el costo objetivo.", "Sé calcular porcentajes.", "Conozco el rendimiento de una formulación."],
    explain=[
        "Para costear una formulación se calcula el costo de cada ingrediente: gramos multiplicados por el precio por kilo y divididos por 1.000. La suma es el costo total del lote. El costo por unidad es el costo total dividido por las unidades que rinde el lote.",
        "El precio de venta se calcula con el costo objetivo: el costo por unidad se multiplica por 100 y se divide por el porcentaje. La pérdida de producción es el porcentaje de unidades que no se pueden vender, por ejemplo por daños; se calcula como unidades por porcentaje dividido por 100, y las unidades vendibles son las producidas menos la pérdida.",
        "Todos los valores son de ejemplo; en la práctica se usan los precios reales y los registros del obrador. El cálculo se hace en papel, sin elaborar el producto." + LIM,
    ],
    vocab=[("costo del lote", "suma de los costos de los ingredientes de una formulación"), ("costo por unidad", "costo del lote dividido por las unidades"), ("pérdida de producción", "parte de las unidades que no se pueden vender"), ("unidades vendibles", "unidades producidas menos la pérdida"), ("precio de venta", "valor al que se ofrece una unidad")],
    worked=[
        ("Costear un ingrediente", "Una formulación de ejemplo usa 250 g de un ingrediente que cuesta $4.000 el kilo. ¿Cuánto cuesta?", ["Gramos por precio, dividido por 1.000.", "250 × 4.000 ÷ 1.000 = 1.000."], "$1.000"),
        ("Calcular unidades vendibles", "Se producen 50 unidades de ejemplo y la pérdida es del 10 %. ¿Cuántas se pueden vender?", ["Pérdida: 50 × 10 ÷ 100 = 5.", "50 − 5 = 45."], "45 unidades"),
    ],
    mistakes=[("Calcular el costo por unidad sin considerar la pérdida de producción.", "El costo por unidad vendible es mayor que el calculado.", "Divide el costo del lote por las unidades vendibles si quieres el costo real."),
              ("Olvidar convertir los gramos a kilos.", "El costo resulta mil veces mayor o menor.", "Divide por 1.000 después de multiplicar por el precio por kilo.")],
    T=[
        ("=", "{F} ¿Cuánto cuesta la harina de la formulación?", "1000*1200//1000", "Se multiplican los gramos por el precio y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la mantequilla de la formulación?", "400*6000//1000", "Se multiplican los gramos por el precio y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el huevo de la formulación?", "200*3000//1000", "Se multiplican los gramos por el precio y se divide por 1.000.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan el leudante y la sal juntos?", "20*8000//1000+10*2000//1000", "Se calcula el costo de cada uno y se suman.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total del lote?", "1000*1200//1000+300*1000//1000+400*6000//1000+200*3000//1000+20*8000//1000+10*2000//1000", "Se suman los costos de los seis ingredientes.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por unidad producida?", "4680//40", "Se divide el costo total por las unidades del lote.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de una unidad con el costo objetivo?", "117*100//30", "Se multiplica el costo por 100 y se divide por el costo objetivo.", " pesos"),
        ("=", "{F} ¿Cuántas unidades del lote se pierden según la pérdida de ejemplo?", "40*5//100", "Se calcula el 5 % de las unidades del lote.", " unidades"),
        ("=", "{F} ¿Cuántas unidades vendibles tiene el lote?", "40-40*5//100", "A las unidades producidas se les resta la pérdida.", " unidades"),
        ("abc", "{F} ¿Por qué el costo por unidad vendible es mayor que el costo por unidad producida?", "Porque el mismo costo se reparte entre menos unidades", "Porque la pérdida baja el precio de los ingredientes", "Porque se agregan nuevos ingredientes", "Con menos unidades vendibles, cada una debe cubrir más costo."),
        ("=", "{F} Si se venden las 38 unidades al precio calculado de $390, ¿cuánto se obtiene?", "390*38", "Se multiplica el precio por las unidades vendibles.", " pesos"),
        ("abc", "{F} Si el precio de la mantequilla sube a $7.000 el kilo, ¿qué efecto tiene en el costo del lote?", "Sube, porque la mantequilla es uno de sus ingredientes más costosos", "Baja, porque la mantequilla rinde más", "No cambia", "Un aumento de precio en un ingrediente sube el costo total."),
        ("abc", "{F} Una compañera propone vender cada unidad a $117, el costo por unidad, «para ser competitivos». ¿Qué observación corresponde?", "No queda margen para otros gastos ni ganancia; conviene aplicar el costo objetivo", "Es lo mejor, porque se vende más", "Es válido si se baja la pérdida", "Vender al costo no cubre otros gastos."),
    ],
    ctx=("abc", "{F} Una jefa quiere bajar el precio de venta. ¿Qué es lo más razonable revisar primero?", "El costo de los ingredientes más costosos y la pérdida de producción, antes de bajar el precio", "Bajar el precio sin revisar costos", "Eliminar el control de la pérdida", "Reducir costos o pérdidas permite bajar el precio sin perder margen."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calcula el costo por unidad?", "Costo del lote dividido por las unidades", "Reparte el costo del lote entre las unidades."),
        ("¿Qué son las unidades vendibles?", "Las producidas menos la pérdida", "Son las que realmente se pueden vender."),
        ("¿Cómo se calcula el precio de venta?", "Costo por 100, dividido por el costo objetivo", "Aplica el costo objetivo al costo por unidad."),
    ],
    op=("Formulación de ejemplo para 1.000 g que rinde 20 unidades: harina 500 g a $1.200 el kilo; azúcar 200 g a $1.000 el kilo; mantequilla 250 g a $6.000 el kilo; sal 10 g a $4.000 el kilo. Costo objetivo: 30 %. Pérdida de producción: 10 %. "
        "Calcula el costo del lote, el costo por unidad, el precio de venta, las unidades vendibles y los ingresos si se venden todas las vendibles al precio calculado.",
        "Harina: 600. Azúcar: 200. Mantequilla: 1.500. Sal: 40. Costo del lote: 2.340. Costo por unidad: 2.340 ÷ 20 = 117. Precio: 117 × 100 ÷ 30 = 390. Unidades vendibles: 20 − 2 = 18. Ingresos: 390 × 18 = 7.020 pesos.",
        ["calcula los cuatro costos y el total", "calcula costo por unidad y precio", "calcula unidades vendibles e ingresos"],
        ["hoja con cálculos"],
        ["olvidar dividir por 1.000", "no restar la pérdida", "vender al costo"],
        "Pregunta: «¿cuántas unidades se pierden con el 10 %?». Debe responder 2."),
    reinforce="Inventa una formulación de cuatro ingredientes con precios y calcula el costo del lote y por unidad.",
    extend="Explica por qué la pérdida de producción debe considerarse al fijar el precio de venta.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (componentes de pastelería de ejemplo, inventados). Rellenos: van dentro de un producto (crema pastelera de ejemplo, manjar). Coberturas: cubren el producto (glaseado de azúcar de ejemplo, baño de chocolate de ejemplo). Decoraciones: adornos como frutas o confites de ejemplo. "
     "Dulce: preparación en la que predomina el azúcar, como el manjar. Vida útil de ejemplo en refrigeración (valores inventados que no reemplazan la norma vigente): crema pastelera, 2 días; manjar envasado y cerrado, 30 días; glaseado, 3 días. "
     "Alérgenos declarados de ejemplo: crema pastelera, leche y huevo; manjar, leche; glaseado, ninguno declarado; baño de chocolate, leche y soya. Riesgos: las cremas con huevo o lácteos son perecibles y requieren frío; el trabajo con azúcar caliente puede causar quemaduras graves.")
build(
    O2, 1, F,
    use="Aprenderé a situar la elaboración de dulces, cremas y glaseados: cómo se clasifican, qué riesgos tienen y por qué importan la vida útil y los alérgenos.",
    prior=["Conozco la formulación y los alérgenos.", "Conozco la vida útil y la cadena de frío.", "Sé sumar días."],
    explain=[
        "En Pastelería y Repostería, los dulces, las cremas y los glaseados sirven para componer y decorar los productos. Se clasifican por su función: los rellenos van dentro del producto, como una crema pastelera o el manjar; las coberturas lo cubren por fuera, como un glaseado de azúcar; y las decoraciones son adornos, como frutas. Un dulce es una preparación en la que predomina el azúcar.",
        "Las cremas con huevo o lácteos son perecibles: se echan a perder con facilidad y requieren cadena de frío. Cada componente tiene su propia vida útil, el plazo en que puede usarse, y sus propios alérgenos, que se declaran en el rótulo. Por eso cada preparación se rotula con fecha de elaboración y plazo.",
        "El azúcar caliente puede causar quemaduras graves, por lo que su manejo solo se practica con instructor y la norma vigente. Aquí se estudian conceptos y datos en papel; no se describe cómo elaborar ninguna preparación. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("relleno", "preparación que va dentro de un producto"), ("cobertura", "preparación que cubre un producto por fuera"), ("decoración", "adorno que se agrega al producto"), ("dulce", "preparación en que predomina el azúcar"), ("perecible", "que se echa a perder con facilidad"), ("cadena de frío", "mantención continua del frío en productos perecibles")],
    worked=[
        ("Clasificar un componente", "Un baño que cubre una torta de ejemplo por fuera, ¿es relleno, cobertura o decoración?", ["Cubre el producto por fuera.", "Eso es una cobertura."], "Una cobertura"),
        ("Calcular un plazo", "Una crema de ejemplo se elabora el día 4 y su vida útil es de 2 días. ¿Hasta qué día puede usarse?", ["Se suma la vida útil al día de elaboración.", "4 + 2 = 6."], "Hasta el día 6"),
    ],
    mistakes=[("Guardar una crema con huevo o lácteos fuera del frío «solo un rato».", "Los alimentos perecibles se echan a perder con facilidad si se rompe la cadena de frío.", "Mantén el frío continuo de las cremas, según la norma vigente."),
              ("Asumir que un glaseado «solo azúcar» no tiene alérgenos.", "Puede llevar ingredientes que sí los tienen, como leche o soya.", "Revisa los alérgenos de cada componente en su especificación.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿qué es un relleno?", "Una preparación que va dentro de un producto", "Una preparación que cubre el producto por fuera", "Un adorno que se agrega al final", "El relleno está dentro; la cobertura cubre y la decoración adorna."),
        ("abc", "{F} ¿Cuál de estos componentes es una cobertura?", "El glaseado de azúcar", "La crema pastelera", "El manjar", "La ficha ubica el glaseado entre las coberturas."),
        ("abc", "{F} ¿Qué vida útil de ejemplo tiene la crema pastelera?", "2 días", "30 días", "3 días", "La ficha asigna 2 días a la crema pastelera."),
        ("abc", "{F} ¿Qué alérgenos declara la crema pastelera?", "Leche y huevo", "Leche y soya", "Ninguno", "La ficha declara leche y huevo para la crema."),
        ("=", "Una crema de ejemplo se produce en lotes de 6 kg y se usan 2 kg por día. ¿Para cuántos días alcanza un lote?", "6//2", "Se divide el peso del lote por el consumo diario.", " días"),
        ("abc", "{F} Un lote de crema pastelera alcanza para 3 días de uso, pero su vida útil es de 2. ¿Qué corresponde?", "Producir cantidades para 2 días y elaborar otro lote después", "Usarla el tercer día si se ve bien", "Guardarla a temperatura ambiente para conservarla", "Se respeta la vida útil y se programa un lote nuevo."),
        ("abc", "{F} Un ayudante quiere trabajar con azúcar caliente rápido, sin instrucción previa. ¿Qué corresponde?", "No hacerlo sin instructor y norma vigente, por el riesgo de quemaduras graves", "Hacerlo con cuidado", "Hacerlo solo si la cantidad es pequeña", "El azúcar caliente exige instrucción y autorización por su riesgo."),
        ("abc", "{F} ¿Por qué las cremas con huevo o lácteos requieren frío?", "Porque son perecibles y se echan a perder con facilidad", "Para que tengan un sabor más dulce", "Para que se vean más brillantes", "El frío frena el deterioro de los alimentos perecibles."),
        ("=", "{F} Un lote de glaseado se prepara el día 4. Con la vida útil de ejemplo, ¿hasta qué día puede usarse?", "4+3", "Se suma la vida útil al día de elaboración.", ""),
        ("abc", "{F} Un cliente alérgico a la leche pregunta por un pastel con crema pastelera y glaseado. ¿Qué debe revisarse?", "La especificación de cada componente, porque la crema declara leche", "Solo el glaseado, que no declara alérgenos", "Nada, porque es un pastel", "El producto tiene varios componentes y uno de ellos declara leche."),
        ("=", "Un obrador ofrece 3 rellenos y 4 coberturas de ejemplo. ¿Cuántas combinaciones de relleno y cobertura puede ofrecer?", "3*4", "Se multiplica el número de rellenos por el de coberturas.", " combinaciones"),
        ("abc", "{F} ¿Quién fiscaliza el rotulado y la higiene de las preparaciones?", "La autoridad sanitaria", "El proveedor de azúcar", "El cliente", "La norma vigente la asigna a la autoridad sanitaria."),
        ("abc", "{F} Una compañera dice que el manjar cerrado dura 30 días, así que el manjar abierto también. ¿Qué respuesta es correcta?", "El plazo de ejemplo es para el manjar envasado y cerrado; una vez abierto se rige por otro plazo", "Tiene razón, el plazo es el mismo", "El manjar nunca se echa a perder", "La ficha limita los 30 días al manjar cerrado."),
    ],
    ctx=("abc", "{F} Un viernes, la jefa encuentra 2 kg de crema pastelera elaborada el lunes. ¿Qué corresponde?", "Descartarla según el procedimiento y registrar la pérdida, porque superó los 2 días de vida útil", "Usarla si no huele mal", "Mezclarla con crema nueva", "Superó su vida útil; el olor no garantiza la inocuidad."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es una cobertura?", "Una preparación que cubre el producto por fuera", "Se distingue del relleno, que va dentro."),
        ("¿Por qué las cremas con huevo o lácteos requieren frío?", "Porque son perecibles", "Se echan a perder con facilidad si no se conservan."),
        ("¿Qué datos lleva el rótulo de una preparación?", "Fecha de elaboración, plazo y alérgenos", "Permiten usarla a tiempo y con seguridad."),
    ],
    op=("Un obrador de ejemplo elabora un glaseado (vida útil de ejemplo de 4 días), una crema con leche y huevo (vida útil de 2 días) y un dulce de frutas envasado y cerrado (vida útil de 20 días). Hoy es el día 10 y se elaboran los tres. "
        "Escribe: (a) hasta qué día puede usarse cada uno, (b) cuál es relleno y cuál cobertura si la crema va dentro de una torta y el glaseado la cubre, (c) qué alérgenos declararías para la crema y (d) por qué la crema requiere frío.",
        "(a) Glaseado: hasta el día 14. Crema: hasta el día 12. Dulce de frutas cerrado: hasta el día 30. (b) La crema es relleno; el glaseado es cobertura. (c) Leche y huevo. (d) Porque es perecible y se echa a perder con facilidad si se rompe la cadena de frío.",
        ["calcula 14, 12 y 30", "clasifica relleno y cobertura", "declara los alérgenos y explica la necesidad de frío"],
        ["hoja con cuatro respuestas"],
        ["sumar mal los días", "decir que la crema es cobertura", "olvidar el huevo"],
        "Pregunta: «¿hasta qué día vale la crema?». Debe responder el día 12."),
    reinforce="Inventa tres componentes de pastelería con su función, vida útil y un alérgeno, y calcula hasta qué día se pueden usar si se elaboran el día 1.",
    extend="Explica por qué cada componente de una torta debe tener su propio rótulo con plazo y alérgenos.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (producto compuesto de ejemplo). La «Torta de ejemplo» está formada por tres componentes: bizcocho (vida útil de ejemplo en refrigeración, 5 días), crema pastelera (2 días) y glaseado (3 días). La vida útil del producto compuesto es la del componente que vence antes. "
     "Rótulo del componente: nombre, fecha de elaboración, usar antes de y alérgenos. Roles: el pastelero prepara los componentes; el decorador arma y decora; la jefa de producción controla los plazos.")
build(
    O2, 2, F,
    use="Aprenderé el vocabulario de los productos compuestos: componentes, rótulo, vida útil del producto y los roles que preparan y controlan cada parte.",
    prior=["Conozco rellenos, coberturas y decoraciones.", "Sé calcular fechas de vencimiento.", "Conozco el rótulo y los alérgenos."],
    explain=[
        "Un producto compuesto está formado por varios componentes, como un bizcocho, una crema y un glaseado. Cada componente se elabora por separado y tiene su propio rótulo con nombre, fecha de elaboración, plazo máximo de uso y alérgenos. Armar es unir los componentes para formar el producto; decorar es agregar los adornos finales.",
        "La vida útil de un producto compuesto es la del componente que vence antes: si la crema dura 2 días y el bizcocho 5, el producto dura 2 días. Antes de armar, se verifica que todos los componentes estén dentro de su plazo.",
        "Los roles son: el pastelero prepara los componentes, el decorador arma y decora, y la jefa de producción controla los plazos. Las cifras son de ejemplo y no describen cómo elaborar los componentes. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("producto compuesto", "producto formado por varios componentes"), ("componente", "parte de un producto compuesto, como el bizcocho o la crema"), ("armar", "unir los componentes de un producto"), ("decorador", "persona que arma y decora los productos"), ("plazo máximo de uso", "último día en que un componente puede usarse")],
    worked=[
        ("Calcular la vida útil de un compuesto", "Un producto de ejemplo tiene componentes con vida útil de 6, 3 y 4 días. ¿Cuál es la vida útil del producto?", ["Es la del componente que vence antes.", "El menor valor es 3."], "3 días"),
        ("Verificar un componente", "Un componente de ejemplo se elaboró el día 2 y su vida útil es de 4 días. Hoy es el día 5. ¿Está dentro del plazo?", ["El plazo llega hasta el día 6 (2 + 4).", "El día 5 es anterior al día 6."], "Sí, está dentro del plazo"),
    ],
    mistakes=[("Informar para el producto compuesto la vida útil del componente que más dura.", "El producto se echa a perder cuando vence su componente más frágil.", "Usa la vida útil del componente que vence antes."),
              ("Armar el producto sin revisar el rótulo de cada componente.", "Se puede usar un componente vencido.", "Verifica el plazo de cada componente antes de armar.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿cuál es la vida útil de un producto compuesto?", "La del componente que vence antes", "La del componente que dura más", "El promedio de las vidas útiles de los componentes", "El producto es tan perecible como su componente más frágil."),
        ("abc", "{F} ¿Cuál es la vida útil de ejemplo de la torta?", "2 días", "5 días", "3 días", "Es la de la crema pastelera, el componente que vence antes."),
        ("abc", "{F} ¿Qué componente limita la vida útil de la torta?", "La crema pastelera", "El bizcocho", "El glaseado", "La crema tiene el plazo más corto."),
        ("=", "{F} Si la torta se arma el día 10, ¿hasta qué día puede usarse?", "10+2", "Se suma la vida útil del producto al día de armado.", ""),
        ("=", "{F} ¿Cuántos días más dura el bizcocho que la crema pastelera?", "5-2", "A la vida útil del bizcocho se le resta la de la crema.", " días"),
        ("abc", "{F} ¿Quién arma y decora los productos?", "El decorador", "El pastelero", "La jefa de producción", "La ficha asigna el armado y la decoración al decorador."),
        ("abc", "{F} ¿Quién controla los plazos de los componentes?", "La jefa de producción", "El decorador", "El pastelero", "La ficha asigna el control de plazos a la jefa de producción."),
        ("=", "Se arman 12 tortas de ejemplo con 3 componentes cada una. ¿Cuántos componentes se usan en total?", "12*3", "Se multiplican las tortas por los componentes de cada una.", " componentes"),
        ("=", "Un glaseado de ejemplo se elaboró el día 6 y puede usarse hasta el día 9. ¿Cuántos días de vida útil tiene?", "9-6", "Al último día de uso se le resta el día de elaboración.", " días"),
        ("abc", "{F} Un decorador arma una torta con un bizcocho de 4 días de antigüedad, crema de 1 día y glaseado de 2 días. ¿Puede usar los componentes?", "Sí: cada componente está dentro de su plazo", "No: el bizcocho es el más antiguo", "No: los tres tienen distinta antigüedad", "4 ≤ 5, 1 ≤ 2 y 2 ≤ 3: todos están dentro de su plazo."),
        ("abc", "{F} Si la crema tuviera 3 días de antigüedad, ¿qué corresponde?", "No usarla, porque superó los 2 días de su vida útil", "Usarla, porque el bizcocho aún es válido", "Mezclarla con crema nueva", "Cada componente se controla por separado."),
        ("=", "Un lote de crema da 24 porciones y cada torta de ejemplo usa 3 porciones de crema. ¿Para cuántas tortas alcanza el lote?", "24//3", "Se divide el total de porciones por las porciones de cada torta.", " tortas"),
        ("abc", "{F} Un compañero propone no rotular el glaseado porque «todos saben que dura 3 días». ¿Qué respuesta es correcta?", "Todo componente se rotula con fecha, plazo y alérgenos, aunque todos recuerden el plazo", "Tiene razón, el rótulo es innecesario", "Solo se rotulan los rellenos", "La memoria de las personas no reemplaza un registro verificable."),
    ],
    ctx=("abc", "{F} Una cliente quiere recoger la torta tres días después de su armado. ¿Qué debe informar la persona que atiende?", "Que la vida útil de ejemplo es de 2 días y que el producto debe entregarse y consumirse dentro de ese plazo", "Que puede esperar el tiempo que quiera", "Que dura 5 días, como el bizcocho", "El plazo del producto compuesto lo fija el componente que vence antes."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es un producto compuesto?", "Un producto formado por varios componentes", "Cada componente tiene su propio rótulo y plazo."),
        ("¿Cuál es la vida útil de un producto compuesto?", "La del componente que vence antes", "Es el eslabón más frágil del producto."),
        ("¿Qué rol arma y decora?", "El decorador", "Es el rol que une los componentes y los adorna."),
    ],
    op=("Producto compuesto de ejemplo: «Pastel de ejemplo», con bizcocho (vida útil 6 días), crema de frutas (3 días) y baño de cobertura (4 días). Se elaboran todos los componentes el día 1. "
        "Escribe: la vida útil del pastel, hasta qué día puede usarse, qué componente la limita, qué datos tendría el rótulo de la crema y quién controlaría los plazos.",
        "Vida útil: 3 días, la de la crema de frutas. Puede usarse hasta el día 4. La limita la crema. El rótulo de la crema: nombre, fecha de elaboración (día 1), usar hasta el día 4 y alérgenos. Los plazos los controla la jefa de producción.",
        ["identifica 3 días y el día 4", "nombra la crema como componente limitante", "completa el rótulo y nombra el rol"],
        ["hoja con cinco respuestas"],
        ["usar 6 días", "olvidar los alérgenos del rótulo", "no nombrar al rol"],
        "Pregunta: «¿cuál es el componente que vence antes?». Debe responder la crema de frutas."),
    reinforce="Inventa un producto compuesto con tres componentes y sus vidas útiles, y calcula la del producto.",
    extend="Explica por qué un cliente debe conocer la vida útil del producto completo y no la de un solo componente.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Pedido de 6 tortas de ejemplo para el sábado. Por torta: bizcocho 800 g, crema pastelera 600 g, manjar 300 g y glaseado 250 g. Existencias: bizcocho 5.000 g, crema pastelera 3.000 g, manjar 2.000 g y glaseado 1.000 g. "
     "Vida útil de ejemplo: crema pastelera 2 días, glaseado 3 días, bizcocho 5 días y manjar cerrado 30 días. Alérgenos de ejemplo: crema, leche y huevo; manjar, leche; glaseado, ninguno declarado; bizcocho, gluten, huevo y leche.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de componentes: calcular cantidades y faltantes y programar la elaboración de cada componente según su vida útil.",
    prior=["Conozco el producto compuesto y la vida útil.", "Conozco el factor de escala.", "Sé restar cantidades."],
    explain=[
        "Para un pedido de varios productos compuestos se multiplica la cantidad de cada componente por el número de productos y se compara con las existencias. Si falta algo, se calcula el faltante y se decide con la jefa de producción cómo resolverlo.",
        "Además se programa cuándo elaborar cada componente: se hace con el máximo de días de anticipación que permite su vida útil, contados hacia atrás desde la entrega. La crema, que dura menos, se elabora lo más cerca posible de la entrega; el bizcocho y el manjar cerrado pueden prepararse antes.",
        "También se revisan los alérgenos de todos los componentes para informar al cliente, ya que el producto declara la suma de los alérgenos de sus partes. Todo se hace en papel con datos de ejemplo. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("anticipación máxima", "días antes de la entrega en que puede elaborarse un componente sin superar su vida útil"), ("faltante", "cantidad que falta para cubrir lo necesario"), ("programar", "decidir cuándo se hace cada tarea"), ("alérgenos del producto", "suma de los alérgenos de todos sus componentes")],
    worked=[
        ("Calcular una cantidad total", "Cada torta de ejemplo usa 400 g de crema y se piden 5 tortas. ¿Cuántos gramos de crema se necesitan?", ["Se multiplican los gramos por las tortas.", "400 × 5 = 2.000."], "2.000 g"),
        ("Aplicar la anticipación máxima", "Un componente de ejemplo dura 3 días y la entrega es el día 10. ¿Desde qué día puede elaborarse?", ["No puede elaborarse con más de 3 días de anticipación.", "10 − 3 = 7."], "Desde el día 7"),
    ],
    mistakes=[("Elaborar la crema con 5 días de anticipación porque el bizcocho dura 5.", "La crema vence antes y estaría vencida en la entrega.", "Programa cada componente según su propia vida útil."),
              ("Informar solo los alérgenos del bizcocho.", "El producto contiene también los alérgenos de la crema y del manjar.", "Declara la suma de los alérgenos de todos los componentes.")],
    T=[
        ("=", "{F} ¿Cuántos gramos de bizcocho se necesitan para las 6 tortas?", "800*6", "Se multiplican los gramos por torta por el número de tortas.", " g"),
        ("=", "{F} ¿Cuántos gramos de crema pastelera se necesitan para las 6 tortas?", "600*6", "Se multiplican los gramos por torta por el número de tortas.", " g"),
        ("=", "{F} ¿Cuántos gramos de crema pastelera faltan?", "600*6-3000", "A la crema necesaria se le restan las existencias.", " g"),
        ("=", "{F} ¿Cuántos gramos de glaseado se necesitan?", "250*6", "Se multiplican los gramos por torta por el número de tortas.", " g"),
        ("=", "{F} ¿Cuántos gramos de glaseado faltan?", "250*6-1000", "Al glaseado necesario se le restan las existencias.", " g"),
        ("abc", "{F} ¿Alcanza el manjar de bodega para las 6 tortas?", "Sí: se necesitan 1.800 g y hay 2.000 g", "No: se necesitan 2.400 g", "No: se necesitan 1.200 g", "300 g por 6 dan 1.800 g, menos que las existencias."),
        ("abc", "{F} ¿Alcanza el bizcocho de bodega?", "Sí: se necesitan 4.800 g y hay 5.000 g", "No: se necesitan 5.200 g", "No: se necesitan 4.200 g", "800 g por 6 dan 4.800 g, menos que las existencias."),
        ("abc", "{F} Con la entrega el sábado, ¿con cuántos días de anticipación máxima puede elaborarse la crema?", "Con 2 días", "Con 5 días", "Con 3 días", "La anticipación no puede superar su vida útil de 2 días."),
        ("abc", "{F} ¿Con cuántos días de anticipación máxima puede elaborarse el bizcocho?", "Con 5 días", "Con 2 días", "Con 30 días", "La anticipación no puede superar su vida útil de 5 días."),
        ("abc", "{F} ¿Qué componente debe elaborarse más cerca de la entrega?", "La crema pastelera", "El manjar cerrado", "El bizcocho", "La crema tiene la vida útil más corta, junto con la de menor anticipación."),
        ("abc", "{F} ¿Qué alérgenos debe declarar la torta, sumando sus componentes?", "Gluten, huevo y leche", "Solo leche", "Solo gluten", "El bizcocho aporta gluten, huevo y leche, y la crema y el manjar también declaran leche."),
        ("abc", "{F} Un compañero propone usar menos crema por torta para cubrir el faltante. ¿Qué observación corresponde?", "Cambia el producto y requiere autorización; mejor decidir con la jefa cómo conseguir el faltante", "Es válido, porque nadie lo notará", "Es válido solo en las últimas tortas", "Cambiar cantidades altera el producto y su especificación."),
        ("=", "{F} Si el proveedor entrega 600 g de crema y 500 g de glaseado que faltaban, ¿cuántos gramos de crema habrá en total?", "3000+600", "Se suman las existencias y lo entregado.", " g"),
    ],
    ctx=("abc", "{F} El jueves se descubre que la crema pastelera, elaborada el lunes, ya superó su vida útil. ¿Qué corresponde?", "Descartarla según el procedimiento, elaborar crema nueva y registrar lo ocurrido", "Usarla porque aún hay tiempo hasta el sábado", "Mezclarla con crema nueva para no perderla", "La crema vencida no se usa; se registra y se repone según la anticipación permitida."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se programa la elaboración de un componente?", "Según su vida útil, contando hacia atrás desde la entrega", "El componente no debe vencer antes de la entrega."),
        ("¿Qué alérgenos declara un producto compuesto?", "La suma de los de sus componentes", "El cliente debe conocer todos los que contiene."),
        ("¿Qué se hace ante un faltante?", "Se decide con la jefa de producción", "No se alteran las cantidades de la especificación."),
    ],
    op=("Pedido de ejemplo: 4 pasteles para el día 20. Por pastel: bizcocho 500 g, crema 400 g y glaseado 200 g. Existencias: bizcocho 2.500 g, crema 1.400 g, glaseado 900 g. Vida útil de ejemplo: crema, 2 días; glaseado, 3 días; bizcocho, 5 días. "
        "Calcula las cantidades, los faltantes y el primer día en que puede elaborarse cada componente para la entrega del día 20.",
        "Bizcocho: 2.000 g (alcanza). Crema: 1.600 g (hay 1.400, faltan 200 g). Glaseado: 800 g (alcanza). Primer día de elaboración: crema, día 18; glaseado, día 17; bizcocho, día 15.",
        ["calcula tres cantidades", "detecta el faltante de crema", "calcula los tres días de elaboración"],
        ["hoja con cálculos y fechas"],
        ["olvidar el faltante", "restar al revés los días", "usar 5 días para la crema"],
        "Pregunta: «¿desde qué día puede elaborarse la crema?». Debe responder el día 18."),
    reinforce="Inventa un pedido de 5 productos compuestos con tres componentes y calcula cantidades y faltantes.",
    extend="Explica por qué se programa primero el componente que más rápido vence cuando se planifica una entrega.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (costeo de una torta de ejemplo, inventado). Torta de 16 porciones. Costos de ejemplo por torta: bizcocho $3.200; crema pastelera $2.400; manjar $1.200; glaseado $1.000; decoración $600. Costo objetivo: 35 % del precio de venta. "
     "Pedido: 5 tortas. Pérdida de ejemplo por manipulación y transporte: 1 torta de cada 20.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: costear un producto compuesto, calcular el costo por porción y el precio, y considerar las pérdidas.",
    prior=["Conozco el costeo, el costo objetivo y las pérdidas.", "Sé dividir y multiplicar.", "Conozco el producto compuesto."],
    explain=[
        "El costo de un producto compuesto es la suma de los costos de sus componentes y de su decoración. El costo por porción se obtiene dividiéndolo por las porciones de la torta. El precio de venta por porción se calcula con el costo objetivo: se multiplica el costo por 100 y se divide por el porcentaje.",
        "El precio de la torta completa es el precio por porción multiplicado por las porciones. Con el pedido se calculan el costo, las ventas y el margen, que es la diferencia entre ventas y costo. Las pérdidas por manipulación o transporte reducen las tortas vendibles y deben considerarse.",
        "Todos los valores son de ejemplo y se calculan en papel, sin elaborar el producto." + LIM,
    ],
    vocab=[("costo del producto", "suma de los costos de sus componentes y decoración"), ("costo por porción", "costo del producto dividido por sus porciones"), ("precio de la torta", "precio por porción por las porciones"), ("margen", "ventas menos costo"), ("pérdida", "unidades que no se pueden vender por daños u otras causas")],
    worked=[
        ("Calcular el costo por porción", "Una torta de ejemplo cuesta $6.000 y tiene 12 porciones. ¿Cuánto cuesta cada porción?", ["Se divide el costo por las porciones.", "6.000 ÷ 12 = 500."], "$500"),
        ("Calcular el margen", "Se venden 4 tortas de ejemplo a $20.000 cada una y su costo es $8.000 por torta. ¿Cuál es el margen?", ["Ventas: 20.000 × 4 = 80.000. Costo: 8.000 × 4 = 32.000.", "Margen: 80.000 − 32.000 = 48.000."], "$48.000"),
    ],
    mistakes=[("Olvidar la decoración al calcular el costo del producto.", "El costo queda subestimado y el precio, bajo.", "Suma todos los componentes y la decoración."),
              ("No considerar las pérdidas al calcular lo que se venderá.", "Se esperan ingresos que no se obtendrán.", "Resta las pérdidas de las unidades producidas.")],
    T=[
        ("=", "{F} ¿Cuál es el costo de una torta?", "3200+2400+1200+1000+600", "Se suman los costos de los cuatro componentes y de la decoración.", " pesos"),
        ("=", "{F} ¿Cuál es el costo por porción?", "8400//16", "Se divide el costo de la torta por sus porciones.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de venta de una porción con el costo objetivo?", "525*100//35", "Se multiplica el costo por porción por 100 y se divide por el porcentaje.", " pesos"),
        ("=", "{F} ¿Cuál es el precio de una torta completa?", "1500*16", "Se multiplica el precio de una porción por las porciones.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta producir las 5 tortas del pedido?", "8400*5", "Se multiplica el costo de una torta por las tortas.", " pesos"),
        ("=", "{F} ¿Cuánto se obtiene por vender las 5 tortas?", "24000*5", "Se multiplica el precio de una torta por las tortas.", " pesos"),
        ("=", "{F} ¿Cuál es el margen del pedido de 5 tortas?", "24000*5-8400*5", "A las ventas se les resta el costo.", " pesos"),
        ("=", "{F} En una producción de 60 tortas, ¿cuántas se pierden según la pérdida de ejemplo?", "60//20", "Se divide el total de tortas por 20, porque se pierde 1 de cada 20.", " tortas"),
        ("=", "{F} En esa producción de 60 tortas, ¿cuántas tortas vendibles quedan?", "60-60//20", "A las tortas producidas se les resta la pérdida.", " tortas"),
        ("abc", "{F} ¿Por qué el costo de la decoración debe incluirse en el costo del producto?", "Porque forma parte de lo que se gasta para elaborar y vender la torta", "Porque aumenta el número de porciones", "Porque reduce las pérdidas", "El costo total incluye todo lo que se consume en el producto."),
        ("=", "{F} Si el costo del manjar subiera a $1.600 por torta, ¿cuál sería el nuevo costo de la torta?", "3200+2400+1600+1000+600", "Se recalcula la suma con el nuevo costo del manjar.", " pesos"),
        ("abc", "{F} Una compañera propone vender cada porción a $525, el costo por porción. ¿Qué observación corresponde?", "No queda margen para otros gastos ni ganancia; conviene aplicar el costo objetivo", "Es lo más competitivo y recomendable", "Es válido si se vende más", "Vender al costo no cubre ningún otro gasto."),
        ("abc", "{F} Si la pérdida aumenta y quedan menos tortas vendibles, ¿qué ocurre con el margen?", "Disminuye, porque se vende menos con los mismos costos", "Aumenta", "No cambia", "Las unidades perdidas ya tuvieron costo y no generan ingresos."),
    ],
    ctx=("abc", "{F} La jefa quiere bajar el precio de la torta para vender más. ¿Qué debe revisar primero?", "Si el costo por porción y el costo objetivo permiten el nuevo precio sin perder margen", "Nada, porque vender más siempre conviene", "Eliminar la decoración sin revisar el efecto", "Bajar el precio sin revisar el costo puede dejar sin margen."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calcula el costo de una torta?", "Suma de los costos de sus componentes y decoración", "Todo lo que se consume en el producto."),
        ("En pastelería: ¿cómo se calcula el margen?", "Ventas menos costo", "Muestra lo que queda después de cubrir el costo."),
        ("¿Qué efecto tiene la pérdida?", "Reduce las unidades vendibles", "Las unidades perdidas no generan ingresos."),
    ],
    op=("Torta de ejemplo de 12 porciones. Costos: bizcocho $2.400; crema $1.800; glaseado $900; decoración $300. Costo objetivo: 30 %. Pedido: 8 tortas. Pérdida de ejemplo: 1 torta de cada 8. "
        "Calcula el costo de una torta, el costo por porción, el precio de una porción, el precio de una torta, las tortas vendibles del pedido y los ingresos si se venden las vendibles.",
        "Costo de una torta: 2.400 + 1.800 + 900 + 300 = 5.400. Por porción: 5.400 ÷ 12 = 450. Precio de porción: 450 × 100 ÷ 30 = 1.500. Precio de torta: 1.500 × 12 = 18.000. Pérdida: 8 ÷ 8 = 1; vendibles: 7. Ingresos: 18.000 × 7 = 126.000 pesos.",
        ["calcula 5.400 y 450", "calcula 1.500 y 18.000", "calcula 7 tortas vendibles e ingresos de 126.000"],
        ["hoja con cálculos"],
        ["olvidar la decoración", "no restar la pérdida", "vender al costo"],
        "Pregunta: «¿cuántas tortas se pierden en 8?». Debe responder 1."),
    reinforce="Inventa una torta con cuatro costos y 10 porciones, y calcula el costo por porción y el precio con un costo objetivo.",
    extend="Explica por qué las pérdidas deben incluirse en el precio de los productos de pastelería.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (tortas, pasteles y postres de ejemplo). Torta: producto grande que se divide en porciones. Pastel: producto individual. Postre: preparación dulce que se sirve al final de una comida. "
     "Preparaciones tradicionales en Chile (ejemplos de especialidades; las variantes locales se consultan a fuentes culinarias de cada zona): torta mil hojas con manjar, kuchen de frutas y leche asada. Las costumbres y los ingredientes cambian según la zona del país. "
     "Estándares de calidad de ejemplo: especificación de diámetro, peso y porciones; rotulado de alérgenos; transporte protegido. La autoridad sanitaria fiscaliza la higiene y el rotulado según la norma vigente.")
build(
    O3, 1, F,
    use="Aprenderé a situar la preparación y el armado de tortas, pasteles y postres: sus tipos, la influencia de las zonas del país y los estándares de calidad.",
    prior=["Conozco el producto compuesto.", "Conozco la especificación y la vida útil.", "Sé multiplicar."],
    explain=[
        "En Pastelería y Repostería, una torta es un producto grande que se divide en porciones; un pastel es un producto individual; y un postre es una preparación dulce que se sirve al final de una comida. Armar es unir los componentes (bizcocho, rellenos, coberturas y decoraciones) según una especificación.",
        "En Chile hay preparaciones tradicionales conocidas, como la torta mil hojas con manjar, el kuchen de frutas o la leche asada. Las costumbres y los ingredientes cambian según la zona: se usan frutas y productos locales, y cada zona tiene sus gustos. Quien prepara productos de consumo habitual conoce esa diversidad y consulta fuentes de cada lugar.",
        "Los estándares de calidad definen el nivel esperado: diámetro, peso y porciones iguales a los de la especificación, alérgenos rotulados y transporte protegido. La autoridad sanitaria fiscaliza la higiene y el rotulado. Aquí no se describe cómo elaborar los productos. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("torta", "producto grande que se divide en porciones"), ("pastel", "producto individual"), ("postre", "preparación dulce que se sirve al final de una comida"), ("zona del país", "región con ingredientes y costumbres propias"), ("estándar de calidad", "nivel que se espera de un producto"), ("especificación", "documento que describe el producto y su calidad esperada")],
    worked=[
        ("Clasificar un producto", "Un producto individual de ejemplo, de tamaño para una persona, ¿es una torta o un pastel?", ["Una torta se divide en porciones.", "Un producto individual es un pastel."], "Un pastel"),
        ("Contar porciones", "Se preparan 5 tortas de ejemplo de 12 porciones cada una. ¿Cuántas porciones son?", ["Se multiplican las tortas por las porciones.", "5 × 12 = 60."], "60 porciones"),
    ],
    mistakes=[("Hacer cada torta de un tamaño distinto «a ojo».", "El cliente no recibe lo que contrató y se pierde el control del costo.", "Sigue la especificación de diámetro, peso y porciones."),
              ("Suponer que una preparación típica se prepara igual en todas las zonas.", "Cada zona tiene variantes y costumbres propias.", "Consulta la especificación del producto y fuentes culinarias de cada lugar.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿qué es un pastel?", "Un producto individual", "Un producto grande que se divide en porciones", "Un adorno para tortas", "El pastel es de tamaño individual; la torta se divide."),
        ("abc", "{F} ¿Cuál de estas es una preparación tradicional en Chile, según la ficha?", "La torta mil hojas con manjar", "El croissant de almendras", "La tarta de manzana francesa", "La ficha incluye la mil hojas, el kuchen y la leche asada."),
        ("abc", "{F} ¿Por qué cambian las preparaciones de una zona a otra?", "Por los ingredientes locales y las costumbres de cada zona", "Porque cada zona tiene una norma sanitaria distinta", "Porque la autoridad sanitaria lo ordena", "La ficha explica que cambian los ingredientes y las costumbres."),
        ("=", "Un obrador de ejemplo prepara 8 tortas de 16 porciones cada una. ¿Cuántas porciones son?", "8*16", "Se multiplican las tortas por las porciones.", " porciones"),
        ("abc", "{F} ¿Qué incluye la especificación de ejemplo de un producto?", "Diámetro, peso y porciones", "Solo el nombre del producto", "El nombre de quien lo elaboró", "La ficha menciona esos tres datos entre los estándares."),
        ("abc", "{F} ¿Quién fiscaliza la higiene y el rotulado?", "La autoridad sanitaria", "El cliente", "El proveedor", "La ficha lo asigna a la autoridad sanitaria."),
        ("abc", "{F} Un cliente pregunta por el kuchen de frutas y la persona que atiende no conoce la variante local de su zona. ¿Qué corresponde?", "Consultar a la jefatura o a una fuente culinaria antes de afirmar algo", "Inventar una descripción convincente", "Decir que no existe", "No se afirma lo que no se sabe; se consulta para informar bien."),
        ("abc", "{F} Una torta debe transportarse al lugar del evento. ¿Qué estándar se aplica?", "Transporte protegido", "Transporte sin envase", "Transporte con otros productos sueltos", "El estándar de ejemplo incluye transporte protegido."),
        ("=", "Una cocina de ejemplo prepara 3 postres por día y 5 días a la semana, con 20 porciones cada uno. ¿Cuántas porciones por semana?", "3*5*20", "Se multiplican los postres, los días y las porciones.", " porciones"),
        ("abc", "{F} Un compañero dice que, como la leche asada es tradicional, no necesita rotular alérgenos. ¿Qué respuesta es correcta?", "Todo producto debe rotular sus alérgenos, sea o no tradicional", "Tiene razón, lo tradicional no lleva rótulo", "Solo se rotulan los productos importados", "La norma de rotulado aplica a todos los productos."),
        ("abc", "En Pastelería y Repostería: ¿qué es armar un producto?", "Unir sus componentes según la especificación", "Comprar sus ingredientes", "Anotar su precio", "Armar es ensamblar los componentes, sin cambiar la especificación."),
        ("=", "Una torta de ejemplo se divide en 16 porciones y un evento requiere 128. ¿Cuántas tortas se necesitan?", "128//16", "Se dividen las porciones requeridas por las de cada torta.", " tortas"),
        ("abc", "{F} Un cliente pide una torta que lleve el nombre de una preparación típica de su zona, pero el obrador no sabe cómo es. ¿Qué debe hacerse?", "Pedir información al cliente o consultar a la jefatura y registrar la especificación acordada", "Hacerla de cualquier manera", "Rechazar el pedido sin explicar", "La especificación se acuerda con el cliente y se registra."),
    ],
    ctx=("abc", "{F} Una escuela de una zona del sur pide un kuchen de frutas para su aniversario, para 80 personas. ¿Qué debe hacer la jefa de producción?", "Consultar la especificación y las porciones, verificar ingredientes y alérgenos, y planificar el pedido", "Preparar lo que se le ocurra", "Rechazar el pedido por ser local", "Un pedido se gestiona con especificación, porciones, alérgenos y planificación."),
    sc=[
        ("En Pastelería y Repostería: ¿qué es una torta?", "Un producto grande que se divide en porciones", "Se distingue del pastel, que es individual."),
        ("¿Por qué cambian las preparaciones por zona?", "Por ingredientes y costumbres locales", "Cada zona tiene su oferta y tradiciones."),
        ("¿Qué estándares de calidad se esperan?", "Diámetro, peso y porciones, rotulado y transporte", "Son los estándares de calidad que enumera la ficha."),
    ],
    op=("Un obrador de ejemplo recibe tres pedidos: 6 tortas de 16 porciones para un evento, 40 pasteles individuales para una escuela y 3 postres de leche asada de 20 porciones cada uno para un casino. "
        "Calcula las porciones totales de los tres pedidos y escribe tres estándares de calidad que aplicarías a las tortas, y qué harías si un cliente pregunta por un ingrediente que no conoces.",
        "Porciones: tortas, 6 × 16 = 96; pasteles, 40; postres, 3 × 20 = 60; total: 196. Estándares: diámetro, peso y porciones iguales a la especificación; alérgenos rotulados; transporte protegido. Si no conozco un ingrediente, consulto a la jefatura antes de informar.",
        ["calcula 96, 40, 60 y 196", "nombra tres estándares", "indica consultar y no inventar"],
        ["hoja con cálculos y respuestas"],
        ["olvidar un pedido", "inventar una respuesta", "no mencionar los alérgenos"],
        "Pregunta: «¿cuánto suman 96, 40 y 60?». Debe responder 196."),
    reinforce="Inventa tres productos de pastelería (una torta, un pastel y un postre) y escribe sus porciones y un alérgeno de cada uno.",
    extend="Explica por qué conocer las preparaciones de distintas zonas ayuda a atender a una clientela diversa.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (especificación de tortas de ejemplo, inventada). Tabla de tamaños: torta de 18 cm, 8 porciones, 1.200 g; torta de 22 cm, 12 porciones, 1.800 g; torta de 26 cm, 16 porciones, 2.400 g (cada porción pesa 150 g). "
     "Vida útil de ejemplo de la torta armada: 2 días en refrigeración. Datos de la especificación: nombre, diámetro, peso, porciones, componentes, alérgenos y vida útil. Roles: el pastelero prepara; el decorador arma y decora; el encargado de calidad verifica; la vendedora informa al cliente.")
build(
    O3, 2, F,
    use="Aprenderé a leer la especificación de una torta y a reconocer los roles que preparan, arman, verifican y venden.",
    prior=["Conozco la especificación y los estándares de calidad.", "Sé dividir y multiplicar.", "Conozco la vida útil de un producto compuesto."],
    explain=[
        "La especificación de una torta describe el producto: nombre, diámetro, peso, número de porciones, componentes, alérgenos y vida útil. Con la tabla de tamaños se sabe cuántas porciones rinde cada torta y cuánto pesa; el peso de una porción se calcula dividiendo el peso por las porciones.",
        "El armado consiste en unir los componentes según la especificación, y la presentación es la forma final del producto: limpio, centrado y con la decoración acordada. El encargado de calidad verifica que el peso y el diámetro coincidan con lo especificado dentro de un margen aceptable.",
        "Cada persona cumple un rol: el pastelero prepara, el decorador arma y decora, el encargado de calidad verifica y la vendedora informa al cliente sobre porciones, alérgenos y vida útil. Las cifras son de ejemplo. Los alérgenos se estudian solo como concepto y rotulado: ante una reacción de una persona se avisa de inmediato a un adulto responsable y a los servicios de emergencia, sin improvisar remedios." + LIM,
    ],
    vocab=[("diámetro", "ancho de la torta, medido de un borde a otro pasando por el centro"), ("porción", "cantidad de torta que se sirve a una persona"), ("presentación", "forma final y aspecto del producto"), ("margen aceptable", "diferencia máxima permitida respecto de lo especificado"), ("encargado de calidad", "persona que verifica el producto")],
    worked=[
        ("Calcular el peso de una porción", "Una torta de ejemplo pesa 1.500 g y tiene 10 porciones. ¿Cuánto pesa cada porción?", ["Se divide el peso por las porciones.", "1.500 ÷ 10 = 150."], "150 g"),
        ("Elegir un tamaño", "Un cliente de ejemplo necesita 11 porciones y hay tortas de 8, 12 y 16 porciones. ¿Cuál es la menor que alcanza?", ["Debe tener al menos 11 porciones.", "La de 8 no alcanza; la de 12 sí."], "La de 12 porciones"),
    ],
    mistakes=[("Entregar una torta de otro diámetro sin avisar al cliente.", "El cliente no recibe lo que contrató y las porciones no coinciden.", "Respeta la especificación o acuerda el cambio con el cliente."),
              ("Informar los alérgenos de memoria.", "Se puede omitir uno y poner en riesgo a una persona.", "Lee la especificación vigente antes de informar.")],
    T=[
        ("abc", "{F} ¿Cuántas porciones tiene la torta de 22 cm?", "12 porciones", "8 porciones", "16 porciones", "La tabla asigna 12 porciones a la torta de 22 cm."),
        ("=", "{F} ¿Cuántos gramos pesa cada porción de la torta de 18 cm?", "1200//8", "Se divide el peso de la torta por sus porciones.", " g"),
        ("abc", "{F} ¿Qué torta pesa 2.400 g?", "La de 26 cm", "La de 22 cm", "La de 18 cm", "La tabla asigna 2.400 g a la torta de 26 cm."),
        ("abc", "{F} Un cliente necesita 14 porciones. ¿Cuál es la torta de menor tamaño que alcanza?", "La de 26 cm, de 16 porciones", "La de 22 cm, de 12 porciones", "La de 18 cm, de 8 porciones", "La de 22 cm tiene solo 12 porciones; la de 26 cm alcanza."),
        ("abc", "{F} ¿Quién verifica el peso y el diámetro de la torta?", "El encargado de calidad", "El decorador", "La vendedora", "La ficha asigna la verificación al encargado de calidad."),
        ("abc", "{F} ¿Quién informa al cliente sobre porciones, alérgenos y vida útil?", "La vendedora", "El pastelero", "El encargado de calidad", "La ficha asigna esa tarea a la vendedora."),
        ("=", "{F} Para un evento de 100 personas, una porción cada una, ¿cuántas tortas de 16 porciones se necesitan como mínimo?", "(100+15)//16", "Se dividen las porciones requeridas por las de cada torta, redondeando hacia arriba.", " tortas"),
        ("=", "{F} Para un evento de 100 personas se producen 7 tortas de 26 cm. ¿Cuántas porciones sobran?", "7*16-100", "Se restan las porciones requeridas a las porciones producidas.", " porciones"),
        ("abc", "{F} Si el pedido es para recoger tres días después del armado, ¿qué corresponde informar?", "Que la vida útil de ejemplo es de 2 días, por lo que deben ajustarse la fecha de armado o de entrega", "Que no hay problema, porque se refrigera", "Que dura una semana", "El plazo de la especificación manda sobre la comodidad."),
        ("abc", "{F} Una torta de 22 cm salió con diámetro de 24 cm. ¿Qué corresponde?", "El encargado de calidad debe registrar la diferencia y decidir si se acepta, se corrige o se avisa al cliente", "Entregarla igual, porque es más grande", "Cambiar el rótulo a 24 cm sin avisar", "Una diferencia respecto de la especificación se registra y se decide con el responsable."),
        ("=", "{F} Si se producen 3 tortas de 22 cm y 2 de 26 cm, ¿cuántas porciones se obtienen en total?", "3*12+2*16", "Se calculan las porciones de cada tipo y se suman.", " porciones"),
        ("abc", "Un compañero dice que el rótulo de alérgenos de las tortas «solo sirve para los clientes que preguntan». ¿Qué respuesta es correcta?", "El rótulo informa a todos y evita riesgos aunque nadie pregunte", "Tiene razón, es un trámite", "Solo se pone en tortas de chocolate", "El rótulo es una obligación de información que protege a las personas."),
        ("=", "{F} Si la torta de 26 cm se vendiera a $24.000, ¿cuánto cuesta cada porción?", "24000//16", "Se divide el precio de la torta por sus porciones.", " pesos"),
    ],
    ctx=("abc", "{F} Una clienta pide una torta «para todos los invitados», sin decir cuántos son. ¿Qué debe hacer la vendedora?", "Preguntar el número de invitados para elegir el tamaño de la torta según la tabla", "Elegir la torta más grande sin consultar", "Elegir la más barata", "El tamaño depende del número de porciones requeridas."),
    sc=[
        ("En Pastelería y Repostería: ¿cómo se calcula el peso de una porción?", "Peso de la torta dividido por las porciones", "Reparte el peso total entre las porciones."),
        ("¿Quién verifica la torta terminada?", "El encargado de calidad", "Compara el producto con la especificación."),
        ("¿Qué datos tiene la especificación?", "Diámetro, peso, porciones, componentes, alérgenos y vida útil", "Describen el producto y su calidad."),
    ],
    op=("Especificación de ejemplo: torta de 20 cm, 10 porciones, 1.500 g; torta de 24 cm, 14 porciones, 2.100 g. Un cliente pide porciones para 40 personas y quiere recoger la torta 3 días después del armado (vida útil de ejemplo de 2 días). "
        "Calcula el peso de una porción, cuántas tortas de 24 cm se necesitan y cuántas porciones sobran, y escribe qué le informarías sobre la fecha de retiro.",
        "Peso de una porción: 1.500 ÷ 10 = 150 g (y 2.100 ÷ 14 = 150 g). Tortas de 24 cm: 2 tortas dan 28 porciones y no alcanzan; 3 tortas dan 42 porciones, por lo que se necesitan 3 y sobran 2. Fecha de retiro: la vida útil es de 2 días, por lo que la torta debe armarse a más tardar 2 días antes del retiro, o retirarse antes.",
        ["calcula 150 g", "calcula 3 tortas y 2 porciones sobrantes", "informa la vida útil de 2 días"],
        ["hoja con cálculos y una frase para el cliente"],
        ["usar 2 tortas", "ignorar la vida útil", "inventar un plazo"],
        "Pregunta: «¿cuántas porciones dan 3 tortas de 14?». Debe responder 42."),
    reinforce="Inventa una tabla de tres tamaños de torta con porciones y calcula cuántas tortas necesitas para 60 personas.",
    extend="Explica por qué la vendedora debe conocer la especificación completa antes de tomar un pedido.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (caso de pedido de ejemplo, inventado). Un cliente pide 100 porciones de torta para un evento. Tamaños y precios de ejemplo: torta de 18 cm, 8 porciones, $6.000; de 22 cm, 12 porciones, $9.000; de 26 cm, 16 porciones, $12.000. "
     "Opciones: A) 7 tortas de 26 cm; B) 6 tortas de 26 cm y 1 de 18 cm; C) 8 tortas de 22 cm. El cliente avisa que algunos invitados no pueden consumir frutos secos, alérgeno que está en la decoración de las tortas normales. Vida útil de ejemplo: 2 días.")
build(
    O3, 3, F,
    use="Aprenderé a analizar un pedido en papel: comparar opciones por porciones y costo, atender un requerimiento de alérgenos y confirmar los datos con el cliente.",
    prior=["Conozco la especificación y los tamaños de torta.", "Sé calcular porciones y costos.", "Conozco los alérgenos."],
    explain=[
        "Un pedido de tortas se analiza comparando opciones: para cada una se calculan las porciones que da y su costo. Una opción solo es válida si cubre las porciones pedidas. Entre las válidas, conviene la de menor costo o la que mejor responde a las necesidades del cliente, como menos sobrantes.",
        "Si un cliente informa que algunos invitados no pueden consumir un alérgeno, como los frutos secos, se prepara un producto específico sin ese ingrediente, rotulado y separado del resto para evitar la contaminación cruzada. No se retira el alérgeno de un producto ya hecho, porque pueden quedar trazas. Ante una reacción de una persona, se avisa a un adulto responsable y a emergencias.",
        "Antes de aceptar el pedido se confirman la fecha de entrega, la cantidad de invitados, los alérgenos y la forma de retiro o transporte, y se registran en la orden. Los datos de esta ficha son de ejemplo." + LIM,
    ],
    vocab=[("opción válida", "opción que cubre las porciones pedidas"), ("sobrante", "porciones que sobran respecto de lo pedido"), ("contaminación cruzada", "paso de un alérgeno de un producto a otro"), ("trazas", "restos muy pequeños de un ingrediente"), ("orden de pedido", "documento donde se registran los datos acordados con el cliente")],
    worked=[
        ("Verificar una opción", "Un cliente de ejemplo necesita 50 porciones. La opción de 3 tortas de 16 porciones, ¿es válida?", ["Se calculan las porciones: 3 × 16 = 48.", "48 es menor que 50."], "No es válida"),
        ("Comparar costos", "La opción X de ejemplo cuesta $30.000 y la opción Y $27.000, y ambas cubren el pedido. ¿Cuál es más económica?", ["Se comparan los dos costos.", "27.000 es menor que 30.000."], "La opción Y"),
    ],
    mistakes=[("Quitar los frutos secos de una torta ya decorada para atender a un invitado alérgico.", "Pueden quedar trazas y causar una reacción.", "Prepara un producto específico sin ese ingrediente y rotulado."),
              ("Elegir la opción más barata sin comprobar que cubre las porciones.", "El cliente se queda sin porciones para algunos invitados.", "Verifica primero que la opción sea válida.")],
    T=[
        ("=", "{F} ¿Cuántas porciones da la opción A?", "7*16", "Se multiplican las tortas por las porciones de cada una.", " porciones"),
        ("=", "{F} ¿Cuánto cuesta la opción A?", "7*12000", "Se multiplican las tortas por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántas porciones da la opción B?", "6*16+8", "Se suman las porciones de las tortas de 26 cm y de la de 18 cm.", " porciones"),
        ("=", "{F} ¿Cuánto cuesta la opción B?", "6*12000+6000", "Se suman el costo de las tortas de 26 cm y el de la de 18 cm.", " pesos"),
        ("=", "{F} ¿Cuántas porciones da la opción C?", "8*12", "Se multiplican las tortas por las porciones de cada una.", " porciones"),
        ("abc", "{F} ¿Qué opción no cubre las 100 porciones pedidas?", "La opción C", "La opción A", "La opción B", "La opción C da 96 porciones y no alcanza."),
        ("abc", "{F} Entre las opciones que cubren el pedido, ¿cuál es la más económica?", "La opción B", "La opción A", "La opción C", "B cuesta $78.000 y A cuesta $84.000; C no cubre el pedido."),
        ("=", "{F} ¿Cuántas porciones sobran con la opción B?", "104-100", "A las porciones producidas se les restan las pedidas.", " porciones"),
        ("abc", "{F} Algunos invitados no pueden consumir frutos secos. ¿Qué corresponde?", "Preparar una torta específica sin frutos secos, rotulada y separada de las demás", "Retirar los frutos secos de la torta decorada", "Decir que no se puede atender el pedido", "Retirar el alérgeno de un producto ya hecho deja trazas; se prepara uno aparte."),
        ("abc", "{F} El cliente quiere retirar las tortas tres días después de armadas. ¿Qué corresponde informar?", "Que la vida útil de ejemplo es de 2 días, por lo que debe ajustarse la fecha de armado o de retiro", "Que no hay problema", "Que dura una semana", "La fecha de armado se programa según la vida útil."),
        ("=", "{F} Si a la opción B se agrega una torta de 18 cm sin frutos secos, ¿cuánto cuesta en total?", "6*12000+6000+6000", "Se suma el costo de la torta adicional al de la opción B.", " pesos"),
        ("abc", "{F} Un compañero dice que A es la mejor opción porque tiene más porciones. ¿Qué observación corresponde?", "Cubre el pedido, pero cuesta más y deja más sobrantes que B", "Tiene razón, más porciones siempre es mejor", "A no cubre el pedido", "Una opción se evalúa por cobertura, costo y sobrantes, no solo por cantidad."),
        ("=", "{F} Con la opción B, ¿cuál es el costo por porción pedida (100 porciones)?", "78000//100", "Se divide el costo de la opción por las porciones pedidas.", " pesos"),
    ],
    ctx=("abc", "{F} La vendedora debe aceptar el pedido. ¿Qué datos debe confirmar con el cliente?", "La fecha de entrega, el número de invitados, los alérgenos y la forma de retiro o transporte", "Solo el precio", "Solo el sabor de las tortas", "Estos datos aseguran que el pedido se cumpla y se registren las necesidades."),
    sc=[
        ("En Pastelería y Repostería: ¿cuándo es válida una opción de pedido?", "Cuando cubre las porciones pedidas", "Si no cubre, el cliente queda sin porciones."),
        ("¿Qué se hace para un invitado alérgico a los frutos secos?", "Se prepara un producto aparte, rotulado y separado", "Así se evitan trazas y la contaminación cruzada."),
        ("¿Qué datos se confirman al aceptar un pedido?", "Fecha, invitados, alérgenos y retiro", "Se registran en la orden de pedido."),
    ],
    op=("Pedido de ejemplo: 60 porciones de torta. Tamaños y precios de ejemplo: de 18 cm, 8 porciones, $6.000; de 22 cm, 12 porciones, $9.000. Opción A: 5 tortas de 22 cm. Opción B: 7 tortas de 18 cm y 1 de 22 cm. Además, 3 invitados no pueden consumir leche. "
        "Calcula las porciones y el costo de cada opción, di cuál conviene y escribe qué harías con los invitados que no pueden consumir leche.",
        "Opción A: 5 × 12 = 60 porciones; costo 5 × 9.000 = 45.000. Opción B: 7 × 8 + 12 = 68 porciones; costo 7 × 6.000 + 9.000 = 51.000. Conviene la A, que cubre exactamente el pedido con menor costo. Para los invitados: preparar porciones sin leche, rotuladas y separadas, confirmando los ingredientes con la jefatura.",
        ["calcula 60 y 68 porciones", "calcula 45.000 y 51.000", "propone un producto específico rotulado y separado"],
        ["hoja con cálculos y decisión"],
        ["elegir B por tener más porciones", "retirar la leche de un producto ya hecho", "olvidar rotular"],
        "Pregunta: «¿cuántas porciones dan 5 tortas de 12?». Debe responder 60."),
    reinforce="Inventa un pedido de 80 porciones y dos opciones de combinación de tortas con sus costos, y elige la más conveniente.",
    extend="Explica por qué un producto específico para una persona alérgica es más seguro que retirar el alérgeno de un producto ya hecho.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (control de calidad de ejemplo, inventado). Especificación de la torta de 22 cm: peso 1.800 g con tolerancia de ±50 g (entre 1.750 y 1.850 g) y diámetro 22 cm con tolerancia de ±1 cm (entre 21 y 23 cm). Una torta es conforme si cumple las dos condiciones. "
     "Muestra de 5 tortas (peso y diámetro): torta 1, 1.790 g y 22 cm; torta 2, 1.820 g y 21 cm; torta 3, 1.860 g y 22 cm; torta 4, 1.750 g y 23 cm; torta 5, 1.810 g y 24 cm. Meta de ejemplo: al menos 80 % de tortas conformes en la muestra.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos: verificar si un producto cumple su especificación con tolerancias y calcular el porcentaje de conformidad.",
    prior=["Conozco la especificación y el control de calidad.", "Sé calcular porcentajes.", "Sé comparar valores con un rango."],
    explain=[
        "Una tolerancia es la diferencia máxima permitida respecto del valor especificado. Si una torta debe pesar 1.800 g con tolerancia de ±50 g, el peso es aceptable entre 1.750 y 1.850 g, incluyendo los extremos. Lo mismo ocurre con el diámetro. Un producto es conforme si cumple todas las condiciones de su especificación.",
        "En una muestra se cuenta cuántos productos son conformes y se calcula el porcentaje de conformidad: los conformes multiplicados por 100 y divididos por el total de la muestra. Se compara con la meta. Los productos no conformes se separan, se registran y se decide si se corrigen, se rehacen o se informa al cliente.",
        "Si hay muchas variaciones, se busca la causa: por ejemplo, el pesaje de los ingredientes o la calibración de la balanza, que es verificar que mide con exactitud. No se amplía la tolerancia para que los productos cumplan." + LIM,
    ],
    vocab=[("tolerancia", "diferencia máxima permitida respecto del valor especificado"), ("conforme", "que cumple todas las condiciones de la especificación"), ("muestra", "grupo de productos que se revisan"), ("porcentaje de conformidad", "conformes por 100, dividido por el total de la muestra"), ("calibración", "verificación de que un instrumento mide con exactitud")],
    worked=[
        ("Verificar un valor", "Un peso de ejemplo de 500 g tiene tolerancia de ±10 g. ¿Es aceptable 515 g?", ["El rango aceptable va de 490 a 510 g.", "515 está fuera del rango."], "No es aceptable"),
        ("Calcular conformidad", "En una muestra de ejemplo de 10 productos, 8 son conformes. ¿Qué porcentaje es?", ["Se multiplican los conformes por 100 y se divide por el total.", "8 × 100 ÷ 10 = 80."], "80 %"),
    ],
    mistakes=[("Ampliar la tolerancia después de ver los resultados para que más productos cumplan.", "Se pierde el control de calidad y la confianza del cliente.", "Define la tolerancia antes y busca la causa de las variaciones."),
              ("Revisar solo el peso y olvidar el diámetro.", "El producto puede no cumplir una de las condiciones.", "Revisa todas las condiciones de la especificación.")],
    T=[
        ("abc", "En Pastelería y Repostería: ¿qué es la tolerancia?", "La diferencia máxima permitida respecto del valor especificado", "El peso de la torta", "El diámetro de la torta", "La tolerancia define el rango aceptable alrededor de un valor."),
        ("abc", "{F} ¿Cuál es el rango de peso aceptable de la torta de 22 cm?", "De 1.750 a 1.850 g", "De 1.700 a 1.900 g", "De 1.800 a 1.850 g", "La tolerancia de ±50 g marca ese rango."),
        ("abc", "{F} ¿Es conforme la torta 1?", "Sí: su peso y su diámetro están dentro del rango", "No: pesa menos de 1.800 g", "No: su diámetro no es 21 cm", "1.790 g está entre 1.750 y 1.850 g, y 22 cm está entre 21 y 23 cm."),
        ("abc", "{F} ¿Por qué no es conforme la torta 3?", "Su peso supera 1.850 g", "Su diámetro es menor que 21 cm", "Su peso es menor que 1.750 g", "Pesa 1.860 g, por encima del máximo aceptable."),
        ("abc", "{F} ¿Por qué no es conforme la torta 5?", "Su diámetro supera 23 cm", "Su peso supera 1.850 g", "Su peso es menor que 1.750 g", "Mide 24 cm, por encima del máximo de 23 cm."),
        ("abc", "{F} ¿Es conforme la torta 4?", "Sí: su peso y su diámetro están justo en los límites aceptables", "No: pesa 1.750 g, menos que 1.800 g", "No: su diámetro está en el límite", "Los extremos del rango están incluidos."),
        ("=", "{F} Si 3 tortas de la muestra son conformes, ¿qué porcentaje de conformidad tiene la muestra?", "3*100//5", "Se multiplican las conformes por 100 y se dividen por el total.", " %"),
        ("abc", "{F} ¿Se cumple la meta de al menos 80 % de tortas conformes?", "No, porque el 60 % es menor que 80 %", "Sí, porque 3 de 5 es mayoría", "Sí, porque no hay tortas sin peso", "El 60 % no alcanza la meta."),
        ("=", "{F} ¿Cuántas tortas conformes más necesitaría la muestra de 5 para alcanzar el 80 % de conformidad?", "5*80//100-3", "Se calcula cuántas tortas conformes exige el 80 % y se resta las que ya hay.", " torta"),
        ("abc", "{F} Un compañero propone ampliar la tolerancia a ±100 g para que más tortas cumplan. ¿Qué observación corresponde?", "La tolerancia se define antes de revisar; ampliarla después quita objetividad al control", "Es válido, porque así se cumple la meta", "Es válido si la jefa no está", "Cambiar el criterio después de ver los resultados vuelve la decisión arbitraria."),
        ("abc", "{F} ¿Qué se hace con las tortas no conformes?", "Se separan, se registran y se decide si se corrigen, se rehacen o se informa al cliente", "Se entregan igual si el cliente no nota", "Se mezclan con las conformes", "Las no conformes no se entregan sin una decisión registrada."),
        ("=", "{F} Si cada torta conforme se vende a $9.000, ¿cuánto se obtiene por las tortas conformes de la muestra?", "3*9000", "Se multiplica el precio de una torta por las tortas conformes.", " pesos"),
        ("abc", "{F} Para reducir las variaciones de peso, ¿qué acción correctiva corresponde?", "Revisar el pesaje de ingredientes y la calibración de la balanza, y capacitar al personal", "Aumentar la tolerancia", "Pesar las tortas con la mano", "Se busca la causa de las variaciones y se corrige."),
    ],
    ctx=("abc", "{F} El decorador dice que la torta 5 es «solo 1 cm más ancha» y que no importa. ¿Qué debe responder el encargado de calidad?", "Que la especificación fija un máximo de 23 cm y que la diferencia debe registrarse y decidirse", "Que tiene razón, 1 cm no importa", "Que se entregue sin registrar", "La especificación es el criterio; las diferencias se registran y se deciden."),
    sc=[
        ("En Pastelería y Repostería: ¿cuándo es conforme un producto?", "Cuando cumple todas las condiciones de la especificación", "Basta que falle una para no ser conforme."),
        ("¿Cómo se calcula el porcentaje de conformidad?", "Conformes por 100, dividido por el total", "Expresa la parte conforme de la muestra."),
        ("¿Qué es la calibración?", "Verificar que un instrumento mide con exactitud", "Asegura que las mediciones sean confiables y exactas."),
    ],
    op=("Especificación de ejemplo de una torta de 18 cm: peso 1.200 g con tolerancia de ±30 g y diámetro 18 cm con tolerancia de ±1 cm. Muestra de 4 tortas (peso y diámetro): torta 1, 1.210 g y 18 cm; torta 2, 1.240 g y 18 cm; torta 3, 1.185 g y 19 cm; torta 4, 1.165 g y 17 cm. Meta de ejemplo: 75 % de conformidad. "
        "Indica los rangos aceptables, cuáles tortas son conformes, el porcentaje de conformidad y si se cumple la meta, y escribe una acción correctiva.",
        "Rango de peso: 1.170 a 1.230 g; diámetro: 17 a 19 cm. Torta 1: conforme. Torta 2: no (1.240 g). Torta 3: conforme (1.185 g y 19 cm). Torta 4: no (1.165 g, menos de 1.170). Conformes: 2 de 4, es decir, 50 %. No se cumple la meta de 75 %. Acción: revisar el pesaje y la calibración de la balanza y registrar las no conformes.",
        ["calcula los rangos 1.170-1.230 g y 17-19 cm", "identifica las dos tortas conformes y el 50 %", "propone una acción correctiva"],
        ["hoja con rangos, clasificación, porcentaje y acción"],
        ["usar la tolerancia como rango completo", "considerar conforme la torta 4", "ampliar la tolerancia"],
        "Pregunta: «¿cuál es el peso mínimo aceptable?». Debe responder 1.170 g."),
    reinforce="Inventa una especificación con tolerancia y una muestra de 4 productos, y calcula el porcentaje de conformidad.",
    extend="Explica por qué una tolerancia se define antes de revisar la producción.",
)
