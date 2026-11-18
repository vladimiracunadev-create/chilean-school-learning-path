"""Forestal TP 3.º y 4.º medio: OAE-01 (manejos culturales en vivero), clases 4 a 6. Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_fore_common import AVISO, EMER, build

O1 = "TP-FORE-3y4-OAE-01"

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (pedido de ejemplo, inventado). Vivero Demo debe entregar 900 plantas de «especie A». Porcentaje de germinación de ejemplo de las semillas: 75 % (de cada 100 semillas sembradas, 75 germinan). "
     "Una bandeja tiene 50 cavidades, una planta por cavidad. Una bolsa de semillas trae 400 semillas y cuesta $12.000 (precio de ejemplo). De cada 10 plantas producidas, 1 se descarta por débil (dato de ejemplo).")
build(
    O1, 4, F,
    use="Aprenderé a planificar en papel cuántas semillas, bolsas y bandejas se necesitan para un pedido, usando el porcentaje de germinación y el descarte.",
    prior=["Sé qué es un lote y qué es una cavidad.", "Sé multiplicar y dividir números enteros.", "Sé qué es un porcentaje."],
    explain=[
        "El porcentaje de germinación indica cuántas semillas de cada 100 logran germinar, es decir, dar origen a una planta. Si el porcentaje fuera 50 %, de 100 semillas germinarían 50, y para conseguir 60 plantas habría que sembrar 120 semillas. Por eso las semillas necesarias se calculan así: plantas buscadas por 100 y dividido por el porcentaje de germinación. Ese porcentaje se obtiene de un ensayo del lote de semillas y debe quedar anotado en su ficha.",
        "El descarte son las plantas que no cumplen la calidad y se retiran. Si se descarta una parte, hay que producir más plantas que las pedidas. Después se calculan los recursos: bolsas de semillas, bandejas y costos. Un buen cálculo se hace por pasos, cada paso con su unidad y sus datos, y se revisa si el resultado tiene sentido. Los valores usados aquí son de ejemplo; en un vivero real los entregan el ensayo del lote y el plan de producción.",
        f"Planificar en papel es una tarea de oficina; sembrar y manejar las plantas lo hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("germinación", "proceso en que una semilla da origen a una planta"), ("porcentaje de germinación", "cuántas semillas de cada 100 logran germinar"), ("ensayo de germinación", "prueba del lote de semillas que estima su porcentaje de germinación"), ("descarte", "plantas que no cumplen la calidad y se retiran"), ("pedido", "cantidad de plantas que debe entregarse")],
    worked=[
        ("Semillas necesarias", "Un pedido de ejemplo pide 300 plantas y la germinación es de 60 %. ¿Cuántas semillas hay que sembrar?", ["Con 60 % germinan 60 de cada 100.", "300 × 100 ÷ 60 = 500."], "500 semillas"),
        ("Plantas a producir", "Se quieren entregar 270 plantas buenas y de cada 10 producidas 1 se descarta, o sea, solo 9 de cada 10 sirven. ¿Cuántas hay que producir?", ["Se entrega 9 de cada 10 plantas producidas.", "270 × 10 ÷ 9 = 300."], "300 plantas"),
    ],
    mistakes=[("Sembrar solo la cantidad de semillas igual al pedido.", "No todas las semillas germinan, así que faltarían plantas.", "Divide por el porcentaje de germinación para calcular las semillas necesarias."),
              ("Usar un porcentaje de germinación de memoria o de otro lote.", "Cada lote de semillas tiene su propio ensayo.", "Usa el dato de la ficha del lote o del ensayo, y anótalo.")],
    T=[
        ("abc", "En Forestal: ¿qué es el porcentaje de germinación de un lote de semillas?", "Cuántas semillas de cada 100 logran germinar", "Cuántas semillas caben en una bandeja", "Cuántos días demora el lote en llegar al vivero", "El porcentaje de germinación mide las semillas que logran dar planta."),
        ("abc", "En Forestal: ¿qué es el descarte de un lote de plantas?", "Las plantas que no cumplen la calidad y se retiran", "Las semillas que no se llegaron a sembrar", "Las bandejas dañadas del vivero", "El descarte se refiere a plantas que no alcanzan la calidad exigida."),
        ("abc", "En Forestal: ¿por qué se siembran más semillas que plantas pedidas?", "Porque no todas las semillas germinan", "Porque la norma exige sembrar siempre el doble", "Porque las semillas pequeñas se pierden al guardarse", "El porcentaje de germinación es menor que 100 %, por eso se siembra de más."),
        ("=", "{F} ¿Cuántas semillas hay que sembrar para obtener 900 plantas con la germinación de la ficha?", "900*100//75", "Se multiplica el pedido por 100 y se divide por el porcentaje de germinación.", " semillas"),
        ("=", "{F} ¿Cuántas bandejas se necesitan para las 900 plantas?", "900//50", "Se divide el total de plantas entre las cavidades de cada bandeja.", " bandejas"),
        ("=", "{F} Una bolsa de semillas se siembra completa. ¿Cuántas plantas se esperan de esa bolsa?", "400*75//100", "Se calcula el 75 % de las 400 semillas de la bolsa.", " plantas"),
        ("=", "{F} ¿Cuántas bolsas de semillas se necesitan para sembrar lo calculado para el pedido?", "(900*100//75)//400", "Se calculan las semillas necesarias y se dividen entre las que trae cada bolsa.", " bolsas"),
        ("=", "{F} Si la germinación real fuera solo de 50 % y se sembraran las semillas calculadas con 75 %, ¿cuántas plantas faltarían para el pedido?", "900-(900*100//75)*50//100", "Se calculan las plantas que realmente germinan y se restan al pedido.", " plantas"),
        ("abc", "{F} Un compañero propone suponer 100 % de germinación para ahorrar semillas. ¿Qué respuesta es correcta?", "Es riesgoso: probablemente no se cumpla el pedido porque no todas germinan", "Es correcto: las semillas siempre germinan todas", "Es correcto: se ahorra y el pedido igual se cumple", "Con una germinación menor que 100 %, sembrar solo el pedido deja plantas faltantes."),
        ("abc", "{F} Antes de calcular las semillas del pedido, ¿qué dato conviene verificar primero?", "El ensayo de germinación del lote de semillas", "La cantidad de bandejas disponibles", "El horario de riego del sector", "El cálculo de semillas depende del porcentaje de germinación del lote."),
        ("=", "{F} Considerando que 1 de cada 10 plantas producidas se descarta, ¿cuántas plantas hay que producir para entregar 900 buenas?", "900*10//9", "Solo 9 de cada 10 plantas producidas sirven, por eso se multiplica por 10 y se divide por 9.", " plantas"),
        ("abc", "El proveedor X vende bolsas de 400 semillas con germinación de 75 % a $12.000, y el proveedor Y bolsas de 450 semillas con germinación de 50 % a $8.000 (precios de ejemplo). Para un pedido de 900 plantas, X necesita 3 bolsas e Y necesita 4. ¿Cuál cuesta menos en semillas?", "El proveedor Y, con $32.000 frente a $36.000", "El proveedor X, porque tiene mejor germinación", "Cuestan lo mismo, porque ambos entregan 900 plantas", "Se compara el costo total: 4 × 8.000 = 32.000 contra 3 × 12.000 = 36.000; la germinación no decide sola."),
        ("=", "{F} Con las bolsas necesarias para sembrar las semillas del pedido, ¿cuánto cuesta el material de semillas por cada planta pedida?", "((900*100//75)//400*12000)//900", "Se calcula el costo total de las bolsas y se divide entre las plantas pedidas.", " pesos"),
    ],
    ctx=("abc", "Un conocido te ofrece semillas «muy buenas» sin etiqueta, sin origen y sin ensayo de germinación para ahorrar en el vivero. ¿Qué corresponde?", "No usarlas sin esa información y consultar al encargado, porque sin origen y germinación no hay trazabilidad ni cálculo posible", "Sembrarlas igual y suponer una germinación alta", "Sembrarlas y anotar datos inventados en la ficha", "Sin ensayo ni origen no se puede planificar ni trazar; inventar datos es una falta grave."),
    sc=[
        ("En Forestal: ¿qué indica el porcentaje de germinación?", "Cuántas semillas de cada 100 logran germinar", "Mide cuántas semillas dan realmente una planta."),
        ("¿Cómo se calculan las semillas necesarias?", "Plantas buscadas por 100 y divididas por el porcentaje de germinación", "Así se compensa la proporción de semillas que no germina."),
        ("¿Por qué se produce más de lo que se entrega?", "Porque parte de las plantas se descarta por calidad", "El descarte reduce la cantidad de plantas buenas disponibles."),
    ],
    op=("Pedido de ejemplo: 600 plantas de «especie B». Germinación de ejemplo de las semillas: 80 %. Cada bandeja tiene 40 cavidades. Cada bolsa trae 250 semillas. Escribe (a) cuántas semillas hay que sembrar, (b) cuántas bolsas se necesitan, (c) cuántas bandejas ocupa el pedido, (d) qué dato verificarías en la ficha del lote antes de calcular.",
        "(a) 600 × 100 ÷ 80 = 750 semillas. (b) 750 ÷ 250 = 3 bolsas. (c) 600 ÷ 40 = 15 bandejas. (d) El ensayo de germinación del lote de semillas y su origen. La siembra la hace personal autorizado.",
        ["calcula bien las semillas", "calcula bolsas y bandejas", "nombra el dato que debe verificarse", "mantiene el cálculo por pasos"],
        ["hoja con los cálculos y respuestas"],
        ["no dividir por el porcentaje de germinación", "olvidar la unidad", "usar un porcentaje sin respaldo"],
        "Pregunta: «¿qué pasa si la germinación real es menor?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un pedido de 200 plantas con germinación de 50 % y calcula las semillas necesarias.",
    extend="Explica con un ejemplo por qué dos lotes de semillas con distinto porcentaje de germinación exigen cálculos diferentes.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas; todos los precios son de ejemplo). Se producirán 1.000 plantas durante 4 semanas. Una bolsa de sustrato llena 25 cavidades. "
     "Sustrato A: $500 por bolsa; exige 3 riegos por semana. Sustrato B: $350 por bolsa; exige 6 riegos por semana. Cada riego tiene un costo de $1.000 (agua y trabajo, dato de ejemplo). "
     "Criterio de calidad de ejemplo: una planta cumple si tiene tallo recto, sin daños visibles y raíz bien formada; un lote se acepta si al menos 85 de cada 100 plantas revisadas cumplen. "
     "Muestra del lote P: 20 plantas revisadas, 17 cumplen. Muestra del lote Q: 20 plantas revisadas, 16 cumplen.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas con criterios de costo y ambiente, y a verificar la calidad de un lote con una muestra y una regla de aceptación.",
    prior=["Sé calcular costos con multiplicaciones y sumas.", "Sé calcular un porcentaje simple.", "Sé qué es un lote."],
    explain=[
        "Comparar alternativas significa decidir con criterios definidos de antemano, para elegir con las mismas reglas y no por preferencia. Los criterios pueden ser el costo total, el consumo de agua o el riesgo para las personas. Mirar solo el precio de un insumo engaña: hay que sumar todo lo que cada alternativa obliga a gastar durante el trabajo, y revisar además su efecto en el ambiente, como el agua que consume.",
        "Para verificar la calidad de un lote se revisa una muestra, que es una parte del lote que se examina para estimar el conjunto. Cada planta de la muestra se compara con un criterio de calidad. El porcentaje de plantas que cumple se compara con la regla de aceptación del lote. Si no cumple, se registra la decisión, se separan las plantas que no cumplen y se informa al encargado; no se cambia la muestra hasta que salga bien, porque eso falsea el resultado. Por ejemplo, si en una muestra de 10 plantas cumplen 9, el porcentaje es 90 %.",
        f"Estas decisiones las toma el encargado técnico con los datos del registro; tú practicas el razonamiento en papel. {EMER} {AVISO}",
    ],
    vocab=[("criterio", "regla definida de antemano para comparar o decidir"), ("alternativa", "una de las opciones entre las que se elige"), ("muestra", "parte del lote que se revisa para estimar el conjunto"), ("regla de aceptación", "porcentaje mínimo que debe cumplir un lote para aprobarse"), ("costo total", "suma de todos los gastos que implica una alternativa")],
    worked=[
        ("Costo total de una alternativa", "Una opción de ejemplo cuesta $300 por bolsa, se usan 10 bolsas y exige 5 riegos de $200 cada uno. ¿Cuál es su costo total?", ["Las bolsas cuestan 10 × 300 = 3.000.", "Los riegos cuestan 5 × 200 = 1.000; el total es 3.000 + 1.000."], "$4.000"),
        ("Aceptar o no un lote", "La regla de ejemplo pide al menos 90 % de plantas que cumplen. En una muestra de 20 plantas cumplen 19. ¿Se acepta?", ["19 de 20 es 95 de cada 100.", "95 es mayor que 90."], "Sí, se acepta"),
    ],
    mistakes=[("Elegir la alternativa con el insumo más barato sin sumar el resto de los costos.", "Los costos de uso, como los riegos, pueden volverla más cara.", "Calcula el costo total de cada alternativa antes de decidir."),
              ("Repetir la revisión de una muestra hasta que el resultado cumpla la regla.", "Es falsear la verificación: el resultado ya no refleja el lote.", "Se registra el resultado real y se decide sobre él.")],
    T=[
        ("abc", "En Forestal: ¿qué es un criterio de calidad de una planta de vivero?", "Una regla definida de antemano para decidir si la planta es aceptable", "El precio final que se cobra por la planta", "La cantidad de agua que se usó en un día", "El criterio fija con qué se compara cada planta; precio y agua son otros datos."),
        ("abc", "En Forestal: ¿qué es una muestra de un lote de plantas?", "Una parte del lote que se revisa para estimar el conjunto", "La planta más grande del lote", "El total de plantas del lote sin excepción", "La muestra es una parte representativa que se examina."),
        ("abc", "En Forestal: ¿por qué conviene definir los criterios antes de comparar alternativas?", "Para decidir con las mismas reglas y no por preferencia", "Para elegir siempre la alternativa más barata", "Para no tener que registrar la decisión", "Los criterios previos evitan sesgos; el costo es solo uno de ellos."),
        ("=", "{F} ¿Cuántos pesos cuestan las bolsas de sustrato A para las 1.000 plantas?", "(1000//25)*500", "Se calculan las bolsas necesarias y se multiplican por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan los riegos del sustrato B durante las 4 semanas?", "6*4*1000", "Se multiplican los riegos por semana, las semanas y el costo de cada riego.", " pesos"),
        ("=", "{F} ¿Qué porcentaje de plantas cumple en la muestra del lote P?", "17*100//20", "Se multiplica por 100 la cantidad que cumple y se divide por la muestra.", " %"),
        ("abc", "{F} Según la regla de aceptación de la ficha, ¿qué lotes se aceptan?", "Solo el lote P, porque llega justo al 85 % exigido", "Solo el lote Q, porque tiene menos plantas que no cumplen", "Ninguno, porque 85 % no supera 85 %", "La regla pide al menos 85 %, así que P con 85 % se acepta y Q con 80 % no."),
        ("=", "{F} ¿Cuál es el costo total con el sustrato A, sumando bolsas y riegos?", "(1000//25)*500+3*4*1000", "Se suma el costo de las bolsas con el de los riegos de 4 semanas.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total con el sustrato B, sumando bolsas y riegos?", "(1000//25)*350+6*4*1000", "Se suma el costo de las bolsas con el de los riegos de 4 semanas.", " pesos"),
        ("abc", "{F} Considerando el costo total, ¿qué sustrato resulta más económico?", "El sustrato A, por $6.000 menos", "El sustrato B, porque su bolsa es más barata", "Ninguno, porque cuestan lo mismo", "El costo total de A es 32.000 y el de B es 38.000; el precio de la bolsa no decide solo."),
        ("abc", "{F} Además del costo, ¿qué diferencia ambiental aparece entre las alternativas?", "B requiere más riegos y por lo tanto usa más agua", "A requiere más riegos y por lo tanto usa más agua", "No hay ninguna diferencia ambiental", "B exige 6 riegos por semana frente a 3 de A, así que consume más agua."),
        ("abc", "{F} El lote Q no cumple la regla. ¿Qué corresponde?", "Registrar el resultado, separar las plantas que no cumplen e informar al encargado", "Despacharlo igual porque ya está listo", "Repetir la muestra hasta que dé 85 %", "El resultado real se registra y se informa; repetir hasta aprobar falsea la verificación."),
        ("=", "{F} Si el lote Q tiene 400 plantas en total y la muestra lo representa, ¿cuántas plantas se espera que cumplan?", "400*16//20", "Se aplica a todo el lote la proporción de la muestra, 16 de 20.", " plantas"),
    ],
    ctx=("abc", "Un comprador de ejemplo ofrece pagar más si le entregan hoy el lote Q sin registrar que no cumplió la regla. ¿Qué corresponde?", "No entregar sin registrar el resultado y avisar al encargado y a un adulto responsable", "Entregarlo y registrar después un resultado mejor", "Entregarlo si el comprador firma que lo acepta", "La decisión se basa en el resultado real; la presión comercial o una firma no lo cambian."),
    sc=[
        ("En Forestal: ¿qué es una muestra?", "Una parte del lote que se revisa para estimar el conjunto", "La muestra permite estimar la calidad de todo el lote."),
        ("¿Qué hay que sumar para comparar el costo de dos alternativas?", "Todos los gastos que cada una obliga a hacer", "El costo total incluye los insumos y también su uso."),
        ("¿Se puede repetir la revisión hasta que el lote cumpla?", "No, porque se falsea el resultado", "La verificación debe reflejar la realidad del lote revisado."),
    ],
    op=("Ficha de ejemplo (precios de ejemplo): se producirán 500 plantas durante 2 semanas; una bolsa de sustrato llena 25 cavidades. Sustrato C: $600 por bolsa y 2 riegos por semana. Sustrato D: $400 por bolsa y 5 riegos por semana. Cada riego cuesta $1.000. Regla de aceptación de ejemplo: al menos 80 de cada 100 plantas revisadas deben cumplir; una muestra de 25 plantas tiene 21 que cumplen. Escribe (a) el costo total de C y de D, (b) cuál es más económico, (c) el porcentaje que cumple en la muestra y si el lote se acepta, (d) una diferencia ambiental entre C y D.",
        "(a) C: 20 bolsas × 600 = 12.000 y 4 riegos × 1.000 = 4.000, total 16.000. D: 20 × 400 = 8.000 y 10 riegos × 1.000 = 10.000, total 18.000. (b) C es más económico por 2.000. (c) 21 × 100 ÷ 25 = 84 %, mayor que 80 %: se acepta. (d) D usa más agua porque exige más riegos.",
        ["calcula los costos totales", "elige con el costo total", "calcula el porcentaje y decide", "nombra una diferencia ambiental"],
        ["hoja con los cálculos y la decisión"],
        ["comparar solo el precio de la bolsa", "olvidar los riegos", "dejar de comparar con la regla de aceptación"],
        "Pregunta: «¿qué otros costos tiene cada alternativa además de la bolsa?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Elige dos objetos que podrías comprar y compara su costo total incluyendo cuánto durarán o cuánto cuesta usarlos.",
    extend="Explica por qué repetir una muestra hasta aprobar es una falta de ética en un registro de calidad.",
)

# ============================================================ OAE-01, clase 6
F = ("Ficha 6 (parte semanal de ejemplo, inventado). Vivero Demo, semana 12, responsable: encargado técnico (nombre de ejemplo). "
     "Lote L-21, «especie A»: 480 plantas al inicio, 24 descartadas, 456 entregadas. Lote L-22, «especie B»: 300 plantas al inicio, 18 descartadas, 282 entregadas. "
     "Observaciones: el miércoles una lectura de temperatura quedó fuera de rango en el sector 2; el jueves una persona resbaló en el pasillo mojado y no se lastimó. "
     "Las plantas descartadas se separan en un contenedor rotulado para su disposición según el plan de manejo ambiental del vivero.")
build(
    O1, 6, F,
    use="Aprenderé a registrar y comunicar el resultado de una semana de trabajo en un vivero: totales, porcentajes, incidentes, residuos y quién informa a quién.",
    prior=["Sé sumar y calcular porcentajes sencillos.", "Sé qué es un registro y un lote.", "Sé qué es un peligro y un riesgo."],
    explain=[
        "Un parte o informe resume lo ocurrido en un periodo para que otras personas puedan decidir. Debe decir qué se hizo, cuánto, cuándo y quién lo anota, con unidades claras y totales que cuadren: las plantas entregadas son las iniciales menos las descartadas. Por ejemplo, un lote de 200 plantas con 10 descartes entrega 190. El porcentaje de descarte se calcula dividiendo los descartes por las plantas iniciales y multiplicando por 100.",
        "También se registran los incidentes, que son hechos no deseados que ocurrieron y pudieron causar daño aunque nadie se lastimara. Informarlos sirve para corregir sus causas antes de que haya un accidente con lesionados, no para castigar a nadie. Los residuos, como plantas descartadas o envases vacíos, se separan y se disponen según el plan de manejo ambiental, porque la normativa ambiental exige un manejo ordenado y trazable.",
        f"Comunicar bien significa usar palabras claras y avisar a quien corresponde, por ejemplo al encargado técnico por un dato de cultivo y al prevencionista por un riesgo. {EMER} {AVISO}",
    ],
    vocab=[("parte", "informe breve de lo ocurrido en un periodo"), ("incidente", "hecho no deseado que ocurrió y pudo causar daño, aunque no lo causó"), ("porcentaje de descarte", "descartes divididos por las plantas iniciales, por 100"), ("residuo", "material que se desecha, como plantas descartadas o envases vacíos"), ("plan de manejo ambiental", "documento que dice cómo cuidar el ambiente y manejar los residuos")],
    worked=[
        ("Cuadrar un parte", "Un lote de ejemplo empezó con 200 plantas, tuvo 10 descartes y el parte dice que entregó 192. ¿Cuadra?", ["Las entregadas deben ser 200 menos 10, es decir, 190.", "192 no es 190."], "No cuadra: deberían ser 190"),
        ("Porcentaje de descarte", "Un lote de ejemplo de 250 plantas tuvo 25 descartes. ¿Cuál es su porcentaje de descarte?", ["25 ÷ 250 son 10 de cada 100.", "El porcentaje es 10 %."], "10 %"),
    ],
    mistakes=[("Callar un incidente porque nadie se lastimó.", "Sin informarlo, las causas siguen y puede haber un accidente después.", "Se registra y se informa al encargado y al prevencionista."),
              ("Informar un total sin revisar que cuadre con los datos del parte.", "Un total equivocado resta credibilidad y lleva a malas decisiones.", "Revisa que iniciales menos descartes den las entregadas.")],
    T=[
        ("abc", "En Forestal: ¿qué debe tener un buen parte de vivero?", "Qué se hizo, cuánto, cuándo y quién lo anota", "Solo el resultado final, sin fechas", "Solo la firma del jefe", "Un parte útil identifica hechos, cantidades, fecha y responsable."),
        ("abc", "En Forestal: ¿qué es un incidente?", "Un hecho no deseado que ocurrió y pudo causar daño aunque no lo causó", "Solo un accidente con lesionados", "Una orden de trabajo del jefe", "Un incidente es un casi accidente; informarlo permite corregir causas."),
        ("abc", "En Forestal: ¿por qué se informa un incidente en que nadie se lastimó?", "Para corregir sus causas antes de que cause daño", "Para sancionar a quien estaba cerca", "No se informa si no hubo lesionados", "Informar un incidente permite prevenir un accidente futuro."),
        ("=", "{F} ¿Cuántas plantas entregaron entre los dos lotes de la ficha?", "456+282", "Se suman las plantas entregadas de L-21 y de L-22.", " plantas"),
        ("=", "{F} ¿Cuántas plantas descartadas hubo en total entre los dos lotes?", "24+18", "Se suman los descartes de ambos lotes.", " plantas"),
        ("=", "{F} ¿Cuál es el porcentaje de descarte del lote L-22?", "18*100//300", "Se multiplican los descartes por 100 y se dividen por las plantas iniciales.", " %"),
        ("abc", "{F} ¿Qué lote tuvo mayor porcentaje de descarte?", "L-22, con 6 % frente a 5 % del otro lote", "L-21, porque tuvo más plantas descartadas", "Ninguno, porque los dos tienen el mismo porcentaje", "El porcentaje de L-21 es 24 ÷ 480 = 5 %; más descartes en número no significa mayor porcentaje."),
        ("abc", "{F} ¿Qué forma de comunicar la lectura fuera de rango es la adecuada?", "Anotar en el parte la lectura, la fecha y el sector, y avisar al encargado", "Comentarlo de pasada sin anotarlo", "Anotar solo «hubo un problema»", "Una comunicación completa deja datos precisos y llega a quien decide."),
        ("abc", "{F} Un borrador dice que L-22 entregó 285 plantas. ¿Es coherente con los datos?", "No: debería ser 282, que son las iniciales menos las descartadas", "Sí: los lotes siempre entregan más de lo que dice el parte", "Sí: el borrador debe ser el que manda", "300 menos 18 son 282, por lo que 285 no cuadra."),
        ("abc", "{F} ¿Qué corresponde hacer con las plantas descartadas?", "Dejarlas registradas y dispuestas según el plan de manejo ambiental del vivero", "Botarlas en el cauce más cercano", "Enterrarlas en cualquier terreno vecino", "Los residuos se manejan según el plan y la normativa ambiental, no donde sea."),
        ("abc", "{F} Una persona resbaló en el pasillo mojado y no se lastimó. ¿A quién conviene informar principalmente por el riesgo del pasillo?", "Al prevencionista y al encargado, para que se corrija la causa", "A nadie, porque no hubo lesiones", "Solo a quien resbaló, para que tenga más cuidado", "El riesgo se corrige informando a quienes pueden tomar medidas."),
        ("=", "{F} Si el próximo parte repite el porcentaje de descarte de L-22 y se inician 500 plantas, ¿cuántas se entregarán?", "500-500*6//100", "Se calcula el 6 % de descartes de 500 y se resta al inicio.", " plantas"),
        ("abc", "{F} ¿Cuál es el mejor orden para cerrar el parte semanal?", "Verificar que los totales cuadren, anotar fecha y responsable, comunicar las observaciones y archivar", "Archivar y después revisar los totales", "Comunicar las observaciones antes de anotarlas", "Primero se revisa lo que se va a informar, luego se informa y al final se archiva."),
    ],
    ctx=("abc", "Una compañera de práctica te cuenta que casi se cae por el piso mojado, pero no pasó nada, y propone no avisar para evitar problemas. ¿Qué le dices?", "Que conviene avisar al encargado o a un adulto responsable, porque informar permite corregir la causa", "Que no avise, porque nadie se lastimó", "Que avise solo si vuelve a ocurrir", "Un casi accidente es una oportunidad de corregir causas antes de que haya lesionados."),
    sc=[
        ("En Forestal: ¿cómo se calcula el porcentaje de descarte?", "Descartes divididos por plantas iniciales, por 100", "Relaciona los descartes con el total inicial del lote."),
        ("¿Qué es un incidente?", "Un hecho no deseado que pudo causar daño aunque no lo causó", "Los incidentes también se informan para corregir sus causas."),
        ("¿Cuántas plantas entrega un lote?", "Las iniciales menos las descartadas", "Así los totales del parte quedan coherentes entre sí."),
    ],
    op=("Ficha de ejemplo (parte de la semana 13): lote L-31, «especie A», 500 plantas al inicio y 20 descartadas; lote L-32, «especie B», 400 plantas al inicio y 40 descartadas. Observación: un envase vacío de un producto quedó fuera de la bodega. Escribe (a) las plantas entregadas de cada lote, (b) el porcentaje de descarte de cada lote, (c) cuál tuvo mayor porcentaje, (d) cómo informarías la observación y a quién.",
        "(a) L-31: 480; L-32: 360. (b) L-31: 20 ÷ 500 = 4 %; L-32: 40 ÷ 400 = 10 %. (c) L-32. (d) Se anota en el parte con fecha y lugar, y se avisa al prevencionista y al encargado; el envase lo gestiona personal autorizado según el plan ambiental.",
        ["calcula bien las entregadas", "calcula los porcentajes", "compara con el porcentaje y no con el número de descartes", "informa la observación a las personas adecuadas"],
        ["hoja con las respuestas"],
        ["comparar solo la cantidad de descartes", "no informar la observación", "dejar un total que no cuadra"],
        "Pregunta: «¿quién puede corregir la causa de la observación?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un parte de tres líneas con un lote, sus iniciales, descartes y entregadas, y comprueba que cuadre.",
    extend="Explica por qué se debe informar un incidente aunque nadie se haya lastimado.",
)
