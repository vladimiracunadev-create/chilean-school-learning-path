"""Elaboración Industrial de Alimentos TP (3.º y 4.º medio): OAE-07 (rotular y etiquetar materias primas, insumos, productos intermedios y finales; envases y embalajes; registro del proceso) y OAE-08 (manejo de residuos sólidos, líquidos y gaseosos: prevención y emergencia, solo conceptos). Todo en papel: plantas, productos, lotes, cantidades y límites inventados y rotulados «de ejemplo»."""
from __future__ import annotations

from tp_eial_common import build

O7 = "TP-EIAL-3y4-OAE-07"
O8 = "TP-EIAL-3y4-OAE-08"
LIM = " Esto es aprendizaje conceptual en papel, con datos de ejemplo: la práctica en una planta de alimentos requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar."
LIMX = " Las máquinas, los equipos de frío, las atmósferas peligrosas y los productos químicos solo se estudian aquí como concepto: su uso requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria, SEC, etc.); este cuaderno no te habilita para trabajar. Ante un accidente o una intoxicación, avisa a un adulto responsable y a emergencias."

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (línea de rotulado de una planta de ejemplo, inventada). Elementos del rótulo de un producto final de ejemplo (la lista exacta la fija la norma vigente): nombre del alimento, lista de ingredientes, declaración de alérgenos, peso neto, nombre del fabricante, código de lote y fecha de vencimiento. "
     "Las etiquetas se entregan contadas a la línea. El operador de rotulado coloca la etiqueta; el supervisor verifica el primer envase rotulado de cada lote contra la ficha del producto. La planta rotula también las materias primas y los insumos que guarda en bodega. "
     "Producción de ejemplo de la línea de rotulado: 120 envases por hora.")
build(
    O7, 1, F,
    use="Aprenderé a situar el rotulado y etiquetado de una planta: qué es un rótulo, qué contiene, por qué importa que sea verídico y qué riesgos trae un error.",
    prior=["Conozco el flujo de una planta de alimentos.", "Conozco el concepto de lote.", "Sé multiplicar y restar enteros."],
    explain=[
        "El rótulo es toda la información escrita, impresa o gráfica que lleva un producto. La etiqueta es el soporte (por ejemplo, un papel adhesivo) donde se coloca esa información. Un rótulo informa qué es el producto, qué contiene, cuánto contiene, quién lo fabricó, de qué lote es y hasta cuándo se puede consumir. La norma vigente fija qué datos son obligatorios y cómo deben presentarse.",
        "El rótulo debe ser verídico: lo que dice debe coincidir con el producto. Un error puede declarar un producto equivocado, omitir un alérgeno (una sustancia que puede provocar una reacción alérgica en personas sensibles), mostrar un peso neto distinto del real o una fecha equivocada. Por eso el supervisor verifica el primer envase de cada lote contra la ficha del producto antes de seguir.",
        "También se rotulan las materias primas, los insumos y los productos intermedios en la bodega, para identificarlos, rastrear su lote y conocer su vencimiento. La máquina etiquetadora la maneja solo personal autorizado." + LIMX,
    ],
    vocab=[("rótulo", "toda la información escrita, impresa o gráfica que lleva un producto"), ("etiqueta", "soporte donde se coloca el rótulo"), ("código de lote", "identificación del conjunto de producto elaborado en condiciones iguales"), ("fecha de vencimiento", "fecha hasta la cual el producto conserva sus condiciones"), ("peso neto", "peso del producto sin el envase"), ("alérgeno", "sustancia que puede provocar una reacción alérgica en personas sensibles")],
    worked=[
        ("Distinguir rótulo y etiqueta", "Un papel adhesivo lleva impreso el nombre, el lote y la fecha de vencimiento de un producto de ejemplo. ¿Qué es el papel y qué es lo impreso?", ["El papel es el soporte.", "Lo impreso es la información del rótulo."], "El papel es la etiqueta; lo impreso es el rótulo"),
        ("Elegir un dato de rastreo", "¿Qué dato del rótulo permite rastrear el conjunto de producto elaborado junto?", ["Se necesita una identificación del conjunto.", "Eso es el código de lote."], "El código de lote"),
    ],
    mistakes=[("Pensar que rotular es solo pegar una etiqueta.", "La etiqueta debe llevar los datos correctos y verificados; pegarla mal puede engañar al consumidor.", "Verifica los datos del primer envase contra la ficha del producto."),
              ("Dejar sin rótulo los productos de bodega porque «igual se sabe qué son».", "Otra persona no los reconocerá y no se podrá rastrear su lote ni su vencimiento.", "Rotula materias primas, insumos y productos intermedios.")],
    T=[
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es un rótulo?", "Toda la información escrita, impresa o gráfica que lleva un producto", "El papel adhesivo donde se imprime la información", "El envase que contiene el producto", "El rótulo es la información; la etiqueta es el soporte donde se coloca."),
        ("abc", "{F} ¿Qué dato del rótulo permite rastrear el lote de un producto?", "El código de lote", "El nombre del fabricante", "El peso neto", "El código de lote identifica el conjunto elaborado junto."),
        ("abc", "{F} ¿Quién verifica el primer envase rotulado de cada lote?", "El supervisor", "El proveedor", "El cliente", "La ficha asigna esa verificación al supervisor."),
        ("abc", "{F} ¿Por qué se declaran los alérgenos en el rótulo?", "Para advertir a las personas sensibles y que puedan evitar el producto", "Para mejorar el sabor del producto", "Para aumentar el peso neto declarado", "Una persona alérgica depende del rótulo para saber si puede consumirlo."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es el peso neto del rótulo?", "El peso del producto sin el envase", "El peso del producto con el envase", "El peso de la caja de embalaje", "El peso neto es el contenido sin el envase."),
        ("abc", "{F} ¿Por qué se rotulan las materias primas que se guardan en bodega?", "Para identificarlas, rastrear su lote y conocer su vencimiento", "Para aumentar su precio de venta", "Para que el proveedor las reconozca", "Un producto de bodega sin rótulo no se puede identificar ni rastrear."),
        ("=", "Una caja de embalaje de ejemplo contiene 12 envases rotulados y se arman 30 cajas. ¿Cuántos envases rotulados hay en total?", "12*30", "Se multiplican los envases por caja por la cantidad de cajas.", " envases"),
        ("abc", "{F} El rótulo de un envase dice peso neto 500 g, pero la ficha del producto dice 450 g. ¿Qué corresponde?", "Detener el rotulado, retener los envases y avisar al supervisor, porque el rótulo debe ser verídico", "Seguir rotulando, porque 50 g es poco", "Cambiar a mano el 500 por 450", "Un dato falso en el rótulo engaña al consumidor."),
        ("abc", "{F} Aparecen en la línea etiquetas de otro producto mezcladas con las del producto en curso. ¿Qué corresponde?", "Separarlas e informar al supervisor antes de seguir, porque rotular con la etiqueta equivocada declara otro producto", "Usarlas si el formato es parecido", "Usarlas primero para no perderlas", "Mezclar etiquetas puede hacer que un producto lleve el rótulo de otro."),
        ("abc", "Un jefe pide omitir la fecha de vencimiento para que el producto «parezca más fresco». ¿Qué respuesta es correcta?", "No se puede: el rótulo debe ser verídico y la fecha protege al consumidor", "Se puede si el producto es de alta rotación", "Se puede si el cliente no la pide", "La fecha informa el límite de consumo y la norma exige que el rótulo no engañe."),
        ("abc", "Una fecha de vencimiento mal impresa en un lote de ejemplo, ¿por qué es grave?", "El consumidor puede usar un producto vencido o descartar uno bueno, y se debilita el rastreo del lote", "Porque cambia el precio del producto", "Porque aumenta el peso neto", "El error afecta la seguridad del consumidor y la trazabilidad."),
        ("=", "La línea de rotulado de ejemplo trabaja 6 horas a 120 envases por hora y 15 envases se retiran por errores. ¿Cuántos envases quedan bien rotulados?", "120*6-15", "Se calcula lo rotulado y se restan los retirados.", " envases"),
        ("abc", "Un operador nota que el código de lote de la etiqueta sale borroso. ¿Qué corresponde?", "Detener, avisar al supervisor y retener lo rotulado hasta aclarar el problema", "Seguir si el resto se lee bien", "Escribir el código a mano en los envases", "Un código ilegible impide rastrear el lote."),
    ],
    ctx=("abc", "{F} El supervisor verifica el primer envase de un lote y encuentra que falta el código de lote. ¿Qué corresponde?", "Detener el rotulado, corregir la causa y verificar de nuevo antes de seguir", "Seguir rotulando y agregar el código al final", "Anotar el código en la factura", "El primer envase se verifica justamente para evitar errores en todo el lote."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre rótulo y etiqueta?", "El rótulo es la información y la etiqueta es su soporte", "Una cosa es el contenido y la otra el soporte."),
        ("¿Para qué sirve el código de lote?", "Para rastrear el conjunto de producto", "Conecta cada envase con sus registros."),
        ("¿Quién verifica el primer envase rotulado?", "El supervisor", "Así se detectan errores antes de rotular todo el lote."),
    ],
    op=("Una planta de ejemplo prepara el rotulado de un producto final. La ficha del producto dice: peso neto 250 g, código de lote L-77 y declara que contiene almendras. En el primer envase, la etiqueta dice: peso neto 300 g, código de lote L-77 y no declara almendras. "
        "Escribe: (a) qué errores tiene la etiqueta, (b) qué riesgos genera cada uno, (c) qué haría el operador y (d) quién debe decidir qué hacer con lo ya rotulado.",
        "(a) El peso neto es 300 g en lugar de 250 g y falta declarar las almendras. (b) El peso engaña al consumidor y la omisión del alérgeno pone en riesgo a personas sensibles. (c) Detener el rotulado y avisar al supervisor. (d) El supervisor o el jefe de calidad, retiene lo rotulado.",
        ["detecta los dos errores", "explica el riesgo de cada uno", "indica detener y avisar"],
        ["hoja con las cuatro respuestas"],
        ["considerar solo el peso", "seguir rotulando", "corregir a mano"],
        "Pregunta: «¿qué pasaría si una persona alérgica compra el producto?». Debe decir que no sabría que contiene almendras."),
    reinforce="Escribe los siete elementos del rótulo de un producto inventado y marca cuál sirve para rastrear el lote.",
    extend="Explica con un ejemplo inventado por qué un error de rotulado puede ser más grave que un error de envasado.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (registro de rotulado de un lote de ejemplo, inventado). Lote L-410 del producto Q, de 250 g. Envases a rotular: 600. Etiquetas entregadas a la línea: 650. Etiquetas usadas: 600; dañadas: 30; sobrantes devueltas: 20. "
     "Elaboración: mes 3 (marzo); vida útil de ejemplo: 6 meses. Envase primario: la bolsa que contiene el producto; envase secundario o embalaje: la caja de 20 bolsas. La conciliación de etiquetas compara las entregadas con las usadas, dañadas y sobrantes.")
build(
    O7, 2, F,
    use="Aprenderé los documentos y términos del rotulado: código de lote, fecha de elaboración y vencimiento, envase primario y secundario, registro de rotulado y conciliación de etiquetas.",
    prior=["Conozco el rótulo y sus elementos.", "Sé sumar y restar enteros.", "Sé leer una planilla."],
    explain=[
        "El registro de rotulado de un lote anota el producto, el lote, las fechas, cuántos envases se rotularon y cuántas etiquetas se entregaron, usaron, dañaron y devolvieron. La conciliación de etiquetas comprueba que las entregadas sean iguales a las usadas más las dañadas y las sobrantes. Si no cuadra, puede haber etiquetas perdidas o usadas en un producto equivocado y se investiga.",
        "La fecha de vencimiento se calcula a partir de la fecha de elaboración y de la vida útil del producto, que en este cuaderno es de ejemplo. El código de lote debe coincidir en el envase y en el embalaje, para poder rastrear el producto en ambos. El envase primario está en contacto con el producto; el envase secundario o embalaje agrupa varios envases primarios.",
        "Las etiquetas dañadas y sobrantes no se tiran ni se guardan en la línea: se contabilizan y se devuelven o destruyen según el procedimiento, para que no se usen en otro producto." + LIMX,
    ],
    vocab=[("registro de rotulado", "planilla con los envases rotulados y las etiquetas usadas, dañadas y sobrantes"), ("conciliación de etiquetas", "comprobación de que entregadas = usadas + dañadas + sobrantes"), ("envase primario", "el que está en contacto con el producto"), ("envase secundario o embalaje", "el que agrupa varios envases primarios"), ("vida útil", "tiempo durante el cual el producto conserva sus condiciones")],
    worked=[
        ("Conciliar etiquetas", "Se entregan 100 etiquetas de ejemplo; se usan 90, se dañan 6 y sobran 4. ¿Concilian?", ["Se suman usadas, dañadas y sobrantes: 90 + 6 + 4 = 100.", "Coincide con las entregadas."], "Sí, concilian"),
        ("Clasificar un envase", "Una caja de cartón agrupa 12 frascos de ejemplo. ¿Es envase primario o secundario?", ["La caja no toca el producto.", "Agrupa envases primarios."], "Envase secundario o embalaje"),
    ],
    mistakes=[("Tirar las etiquetas dañadas sin contarlas.", "La conciliación no cuadra y no se puede saber si se usaron en otro producto.", "Cuenta y registra las dañadas y las sobrantes."),
              ("Cambiar el código de lote entre el envase y la caja.", "Se pierde la conexión entre ambos y el rastreo falla.", "Usa el mismo código de lote en el envase y en el embalaje.")],
    T=[
        ("abc", "{F} ¿Cuántas etiquetas se usaron en el lote L-410?", "600", "650", "620", "El registro indica 600 etiquetas usadas; 650 son las entregadas."),
        ("=", "{F} ¿Cuántas etiquetas dañadas y sobrantes hubo en total?", "30+20", "Se suman las etiquetas dañadas y las sobrantes.", " etiquetas"),
        ("=", "{F} ¿Cuántas etiquetas se entregaron de más respecto de los envases a rotular?", "650-600", "A las etiquetas entregadas se les resta la cantidad de envases a rotular.", " etiquetas"),
        ("abc", "{F} ¿Concilian las etiquetas del lote L-410?", "Sí, porque 600 + 30 + 20 es igual a las 650 entregadas", "No, porque se usaron menos de las entregadas", "No, porque hubo etiquetas dañadas", "La conciliación cuadra cuando las entregadas son iguales a usadas, dañadas y sobrantes."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es conciliar las etiquetas?", "Comprobar que las entregadas son iguales a las usadas más las dañadas y las sobrantes", "Pegar todas las etiquetas del lote", "Contar solo las etiquetas dañadas", "La conciliación suma todos los destinos de las etiquetas entregadas."),
        ("abc", "¿Para qué sirve conciliar las etiquetas?", "Para detectar etiquetas perdidas o usadas en el producto equivocado", "Para fijar el precio de las etiquetas", "Para reducir la cantidad de envases", "Una diferencia indica que alguna etiqueta no está donde debería."),
        ("=", "{F} El producto se elaboró en el mes 3 y su vida útil de ejemplo es de 6 meses. ¿En qué número de mes vence?", "3+6", "Al mes de elaboración se le suman los meses de vida útil.", " (septiembre)"),
        ("abc", "{F} La bolsa que contiene el producto, ¿qué tipo de envase es?", "Envase primario", "Envase secundario", "Embalaje", "La bolsa está en contacto directo con el producto."),
        ("abc", "{F} La caja de 20 bolsas, ¿qué tipo de envase es?", "Envase secundario o embalaje", "Envase primario", "Materia prima", "La caja agrupa envases primarios y no toca el producto."),
        ("abc", "En otro lote de ejemplo, se usaron 640 etiquetas, se dañaron 10 y sobraron 5, y se habían entregado 650. ¿Qué indica?", "Hay 5 etiquetas de más en el registro, lo que sugiere un error de conteo o etiquetas de otro origen, y se investiga", "Que todo está bien, porque la diferencia es pequeña", "Que se entregaron etiquetas de menos", "640 + 10 + 5 suman 655, que supera las 650 entregadas."),
        ("abc", "¿Por qué el código de lote debe ser el mismo en el envase y en el embalaje?", "Para poder rastrear el producto tanto por el envase como por la caja", "Para que la caja se vea más ordenada", "Para reducir el costo de las etiquetas", "El mismo código conecta ambos niveles con los mismos registros."),
        ("=", "{F} Si hubieran dañado 45 etiquetas en lugar de 30, y todo lo demás igual, ¿cuántas etiquetas habrían sobrado?", "650-600-45", "A las entregadas se les restan las usadas y las dañadas.", " etiquetas"),
        ("abc", "{F} Un operario reemplaza etiquetas dañadas con otras de una caja vecina sin registrarlo. ¿Qué problema hay?", "La conciliación no cuadrará y pueden mezclarse etiquetas de otro producto", "Ninguno, porque son etiquetas del mismo tamaño", "Solo falta firmar el registro", "Las etiquetas sin registro rompen el control de lo entregado y usado."),
    ],
    ctx=("abc", "{F} Un cliente reporta un envase cuyo código de lote es ilegible. Con el registro de rotulado y el código de la caja, ¿qué se puede hacer?", "Identificar el lote por el código del embalaje y revisar sus registros", "Nada, porque sin código en el envase no se puede rastrear", "Suponer que es del último lote producido", "El código de la caja y el registro permiten reconstruir el origen del envase."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cuál es la diferencia entre envase primario y secundario?", "El primario toca el producto y el secundario agrupa envases primarios", "Cada uno cumple una función distinta en la protección del producto."),
        ("¿Cómo se concilian las etiquetas?", "Entregadas = usadas + dañadas + sobrantes", "La suma de destinos debe coincidir con lo entregado."),
        ("¿Qué se hace con las etiquetas sobrantes y dañadas?", "Se contabilizan y se devuelven o destruyen según el procedimiento", "Así no se usan por error en otro producto."),
    ],
    op=("Registro de ejemplo del lote L-520 de un producto de 300 g: envases a rotular, 800; etiquetas entregadas, 850; usadas, 800; dañadas, 35; sobrantes devueltas, 10. Elaboración en el mes 5; vida útil de ejemplo de 4 meses. "
        "Escribe: (a) si las etiquetas concilian, con la cuenta, (b) qué indicaría una diferencia, (c) en qué número de mes vence el lote y (d) qué tipo de envase es una caja que agrupa 10 bolsas.",
        "(a) 800 + 35 + 10 = 845, que es distinto de 850: faltan 5 etiquetas, no concilia. (b) Que alguna etiqueta se perdió o se usó en otro producto y debe investigarse. (c) 5 + 4 = mes 9. (d) Envase secundario o embalaje.",
        ["hace la cuenta y concluye que no concilia", "explica qué indica la diferencia", "calcula el mes 9 e identifica el embalaje"],
        ["hoja con las cuatro respuestas"],
        ["decir que concilia", "olvidar las dañadas", "confundir envase primario con secundario"],
        "Pregunta: «¿qué haría el supervisor con las 5 etiquetas faltantes?». Debe decir que investigaría dónde quedaron."),
    reinforce="Inventa un registro de rotulado con etiquetas entregadas, usadas, dañadas y sobrantes, y comprueba si concilia.",
    extend="Explica con un ejemplo inventado cómo una etiqueta perdida puede terminar en un producto equivocado.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (etiqueta con errores, de ejemplo e inventada). Ficha del producto correcto: nombre, Mezcla de frutas y frutos secos Q; peso neto, 300 g; ingredientes, pasas, almendras y maní; alérgenos, contiene almendras y maní; código de lote, L-520; vencimiento, mes 10; fabricante, Planta de Ejemplo. "
     "Etiqueta encontrada en el primer envase: nombre, Mezcla de frutas y frutos secos Q; peso neto, 350 g; ingredientes, pasas y almendras; alérgenos, contiene almendras; código de lote, en blanco; vencimiento, mes 10; fabricante, Planta de Ejemplo. "
     "Se rotularon 400 envases con esta etiqueta; 150 siguen en la bodega de la planta.")
build(
    O7, 3, F,
    use="Aprenderé a analizar un caso en papel: comparar una etiqueta con la ficha del producto, detectar errores, clasificar su gravedad y decidir qué hacer con lo ya rotulado.",
    prior=["Conozco los elementos del rótulo.", "Sé restar enteros y calcular porcentajes.", "Sé comparar dos textos."],
    explain=[
        "Para verificar un rótulo se compara cada elemento con la ficha del producto: nombre, peso neto, ingredientes, alérgenos, código de lote, vencimiento y fabricante. Cada diferencia es un error. La gravedad depende del efecto: omitir un alérgeno puede poner en riesgo la salud de una persona sensible; un peso neto equivocado engaña al consumidor; un código de lote en blanco impide el rastreo.",
        "Ante un error, quien lo detecta detiene el rotulado y avisa al supervisor. Lo ya rotulado con la etiqueta equivocada se retiene e identifica, tanto en la bodega como, si ya fue despachado, mediante la trazabilidad. Los rótulos no se corrigen a mano ni se tapan: el supervisor y el jefe de calidad deciden cómo se corrige según el procedimiento y la norma vigente.",
        "Después se busca la causa del error, por ejemplo una etiqueta de otra versión del producto, y se define una acción preventiva. Un alérgeno es una sustancia que puede provocar una reacción alérgica; ante una reacción de una persona, se avisa a un adulto responsable y a emergencias." + LIM,
    ],
    vocab=[("error de rotulado", "diferencia entre la etiqueta y la ficha del producto"), ("omisión", "dato que falta en el rótulo"), ("retener", "mantener apartado e identificado hasta decidir"), ("causa raíz", "origen de un error que, si se corrige, evita que se repita"), ("verificación del primer envase", "comparación del primer envase rotulado con la ficha")],
    worked=[
        ("Detectar una diferencia", "La ficha de un producto de ejemplo dice peso neto 200 g y la etiqueta dice 250 g. ¿Es un error?", ["Se compara cada dato con la ficha.", "No coinciden."], "Sí, un error de peso neto"),
        ("Comparar gravedad", "Una etiqueta de ejemplo omite un alérgeno y otra tiene un nombre mal escrito en una letra. ¿Cuál es más grave?", ["Se piensa en el efecto sobre las personas.", "Omitir un alérgeno puede afectar la salud."], "La omisión del alérgeno"),
    ],
    mistakes=[("Corregir a mano el peso en las etiquetas ya pegadas.", "Los rótulos no se alteran por cuenta propia y el cambio no queda verificado ni respaldado.", "Retén lo rotulado y avisa al supervisor para que decida."),
              ("Corregir el error sin averiguar su causa.", "El error puede repetirse en el siguiente lote.", "Busca la causa raíz y define una acción preventiva.")],
    T=[
        ("abc", "{F} ¿Cuántos errores tiene la etiqueta encontrada respecto de la ficha?", "Cuatro", "Dos", "Tres", "Son errores el peso neto, los ingredientes, el alérgeno y el código de lote en blanco."),
        ("=", "{F} La ficha tiene 7 elementos de rótulo. ¿Cuántos elementos de la etiqueta coinciden con la ficha?", "7-4", "Al total de elementos se le restan los que tienen error.", " elementos"),
        ("abc", "{F} ¿Qué error es el más grave desde el punto de vista de la salud?", "La omisión del maní en los alérgenos", "El peso neto de 350 g", "El código de lote en blanco", "Una persona alérgica al maní no sería advertida por el rótulo."),
        ("abc", "{F} ¿Qué dato falta que impide rastrear el lote?", "El código de lote", "El nombre del fabricante", "El vencimiento", "El código de lote está en blanco en la etiqueta."),
        ("=", "{F} ¿Cuántos gramos más de peso neto declara la etiqueta respecto de la ficha?", "350-300", "Al peso de la etiqueta se le resta el peso de la ficha.", " g"),
        ("abc", "{F} ¿Qué debe hacer quien detecta los errores en el primer envase?", "Detener el rotulado y avisar al supervisor", "Seguir rotulando y avisar al terminar", "Corregir los errores a mano en los envases", "Detener evita que más envases salgan con el rótulo equivocado."),
        ("=", "{F} Se rotularon 400 envases con la etiqueta errónea y 150 siguen en la bodega. ¿Cuántos envases ya salieron de la bodega?", "400-150", "Al total rotulado se le restan los que siguen en la bodega.", " envases"),
        ("abc", "{F} ¿Qué se hace con los 150 envases que siguen en la bodega?", "Retenerlos e identificarlos hasta que el supervisor y el jefe de calidad decidan", "Despacharlos si se avisa al cliente por teléfono", "Cambiar las etiquetas a mano sin registrarlo", "Lo rotulado con un error se retiene hasta una decisión formal."),
        ("abc", "{F} ¿A quién perjudica que la etiqueta declare un peso neto mayor que el real?", "Al consumidor, que cree comprar más producto", "A nadie, porque el peso no importa", "Solo al proveedor de etiquetas", "El rótulo debe ser verídico para no engañar a quien compra."),
        ("abc", "{F} Un operario propone tachar el 350 y escribir 300 con lápiz en los envases. ¿Qué respuesta corresponde?", "No: los rótulos no se corrigen a mano; lo decide el supervisor con el jefe de calidad", "Sí, si se hace rápido", "Sí, si se anota en el cuaderno de la línea", "Una corrección a mano no está verificada y puede esconder el error."),
        ("abc", "{F} Se halla que las etiquetas pertenecían a otra versión del producto. ¿Qué acción preventiva es adecuada?", "Verificar el código de versión de la etiqueta al recibirla y al cargar la línea", "Rotular más rápido", "Pedir más etiquetas del mismo tipo", "Controlar la versión de la etiqueta ataca la causa del error."),
        ("=", "Se revisan por muestreo 20 etiquetas de otro lote de ejemplo y 3 tienen errores. ¿Qué porcentaje de las etiquetas revisadas no tiene errores?", "(20-3)*100//20", "Se restan las etiquetas con error del total y se calcula el porcentaje.", " %"),
        ("abc", "¿Por qué se verifica el primer envase de cada lote contra la ficha antes de seguir?", "Para detectar errores antes de rotular todo el lote", "Para aumentar la velocidad de la línea", "Para reducir el peso de las etiquetas", "La verificación temprana evita que el error se repita en miles de envases."),
    ],
    ctx=("abc", "{F} Un cliente que ya recibió algunos de esos envases pregunta si el producto contiene maní. ¿Qué respuesta corresponde?", "Informar que el rótulo tiene un error, que el producto sí contiene maní, y coordinar el retiro con la planta", "Decir que no contiene maní porque no está en el rótulo", "No responder hasta que el cliente reclame", "El rótulo estaba equivocado: lo real es la ficha del producto."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se verifica un rótulo?", "Comparando cada elemento con la ficha del producto", "Cada diferencia se considera un error."),
        ("¿Qué se hace con lo rotulado con error?", "Se retiene e identifica hasta que se decida", "Evita que siga su curso con el rótulo equivocado."),
        ("¿Por qué se busca la causa raíz?", "Para evitar que el error se repita", "Corregir solo el síntoma deja la causa pendiente."),
    ],
    op=("Ficha de un producto de ejemplo: peso neto 400 g, código de lote L-88, vencimiento en el mes 8 y contiene huevo. Etiqueta del primer envase: peso neto 400 g, código L-88, vencimiento en el mes 11 y sin declarar huevo. "
        "Escribe: (a) los errores de la etiqueta, (b) cuál es el más grave y por qué, (c) qué debe hacer el operador y (d) una acción preventiva.",
        "(a) El vencimiento es el mes 11 en lugar del mes 8 y falta declarar el huevo. (b) La omisión del huevo, porque una persona alérgica no sería advertida. (c) Detener el rotulado y avisar al supervisor. (d) Verificar la versión de la etiqueta al cargar la línea y el primer envase contra la ficha.",
        ["encuentra los dos errores", "elige la omisión del alérgeno", "propone detener y una acción preventiva"],
        ["hoja con las cuatro respuestas"],
        ["considerar bueno el vencimiento erróneo", "corregir a mano", "no proponer prevención"],
        "Pregunta: «¿qué pasaría con una persona alérgica al huevo?». Debe decir que no sabría que el producto lo contiene."),
    reinforce="Inventa una ficha de producto y una etiqueta con tres errores, y escríbelos en una tabla.",
    extend="Explica con un ejemplo inventado por qué la verificación del primer envase evita problemas mayores.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (orden de rotulado de ejemplo, inventada). Lote L-630: 2.400 envases; cajas de 24 envases; una etiqueta por envase y una etiqueta por caja; un pallet con 50 cajas. Etiquetas de envase entregadas: 2.500; usadas: 2.400; dañadas: 50; sobrantes devueltas: 50. "
     "La línea rotula 600 envases por hora. Precio de ejemplo: $8 por etiqueta de envase. Límite de ejemplo de etiquetas dañadas: hasta 2 % de las entregadas; sobre ese valor se revisa la causa con el supervisor.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular cajas, pallets y horas de rotulado, conciliar etiquetas, medir el porcentaje de dañadas y estimar costos.",
    prior=["Conozco el registro de rotulado y la conciliación.", "Sé calcular porcentajes con enteros.", "Sé multiplicar y dividir enteros."],
    explain=[
        "Con la cantidad de envases se calculan las cajas dividiendo por los envases por caja, y los pallets dividiendo las cajas por las cajas por pallet. Con la velocidad de la línea se calcula el tiempo: envases a rotular divididos por envases por hora. Todos estos cálculos sirven para planificar etiquetas, embalajes y tiempos.",
        "El porcentaje de etiquetas dañadas se calcula con las dañadas por 100, dividido por las entregadas. Se compara con el límite de la planta: si lo supera, se revisa la causa con el supervisor, por ejemplo el estado del material o el ajuste del equipo, que corresponde a personal autorizado. El costo de las etiquetas dañadas se calcula con su cantidad por el precio de cada una.",
        "La conciliación debe cuadrar: entregadas, usadas, dañadas y sobrantes. Una etiqueta que no se registra puede terminar en otro producto. Las etiquetas sobrantes se devuelven contadas." + LIMX,
    ],
    vocab=[("pallet", "plataforma sobre la que se agrupan cajas para transportarlas"), ("porcentaje de dañadas", "etiquetas dañadas por 100, dividido por las entregadas"), ("límite de dañadas", "máximo de etiquetas dañadas aceptado sin revisar la causa"), ("planificación", "cálculo anticipado de materiales y tiempos")],
    worked=[
        ("Calcular cajas", "Un lote de ejemplo tiene 1.200 envases y cada caja lleva 24. ¿Cuántas cajas se arman?", ["Se divide el total de envases por los que lleva cada caja.", "1.200 ÷ 24 = 50."], "50 cajas"),
        ("Calcular un porcentaje", "De 500 etiquetas de ejemplo entregadas, 10 se dañaron. ¿Qué porcentaje es?", ["Se multiplican las dañadas por 100 y se divide por las entregadas.", "10 × 100 ÷ 500 = 2."], "2 %"),
    ],
    mistakes=[("Calcular el porcentaje de dañadas dividiéndolas por las usadas.", "El límite se mide respecto de las etiquetas entregadas.", "Divide las dañadas por las entregadas y multiplica por 100."),
              ("Tratar una etiqueta dañada como si no costara nada.", "Es dinero perdido y puede indicar un problema en la línea.", "Registra su cantidad y calcula su costo.")],
    T=[
        ("=", "{F} ¿Cuántas cajas se arman con el lote L-630?", "2400//24", "Se divide el total de envases por los envases de cada caja.", " cajas"),
        ("=", "{F} ¿Cuántos pallets se arman con las cajas del lote?", "2400//24//50", "Se divide el número de cajas por las cajas de cada pallet.", " pallets"),
        ("=", "{F} ¿Cuántas horas demora el rotulado del lote?", "2400//600", "Se divide el total de envases por los envases rotulados cada hora.", " horas"),
        ("=", "{F} ¿Cuántas etiquetas se entregaron de más respecto de los envases del lote?", "2500-2400", "A las etiquetas entregadas se les restan los envases a rotular.", " etiquetas"),
        ("=", "{F} ¿Qué porcentaje de las etiquetas entregadas se dañó?", "50*100//2500", "Se multiplican las dañadas por 100 y se divide por las entregadas.", " %"),
        ("abc", "{F} ¿Cumple el lote el límite de dañadas?", "Sí, porque 2 % no supera el límite de 2 %", "No, porque hubo etiquetas dañadas", "No, porque el límite es 0 %", "El valor calculado es igual al límite y no lo supera."),
        ("=", "{F} ¿Cuántos pesos cuestan todas las etiquetas de envase entregadas?", "2500*8", "Se multiplica la cantidad de etiquetas por su precio.", " pesos"),
        ("=", "{F} ¿Cuántos pesos costaron las etiquetas dañadas?", "50*8", "Se multiplica la cantidad de dañadas por el precio de cada una.", " pesos"),
        ("=", "En otro lote de ejemplo se entregaron 2.500 etiquetas y se dañaron 100. ¿Qué porcentaje se dañó?", "100*100//2500", "Se multiplican las dañadas por 100 y se divide por las entregadas.", " %"),
        ("abc", "Con un porcentaje de dañadas de 4 % y un límite de 2 %, ¿qué corresponde?", "Revisar la causa con el supervisor, por ejemplo el material o el ajuste del equipo por personal autorizado", "Aceptarlo, porque la diferencia es de solo 2 puntos", "Esconder las dañadas para que no figuren", "Superar el límite exige investigar la causa y no ocultar el dato."),
        ("abc", "Un operario reemplaza las etiquetas dañadas por otras de la caja de al lado, sin registrar. ¿Qué problema hay?", "La conciliación no cuadrará y se pueden mezclar etiquetas de otro producto", "Ninguno, porque son del mismo tamaño", "Solo falta firmar el registro de al lado", "Las etiquetas sin registro rompen el control de lo entregado y usado."),
        ("=", "Un lote de ejemplo de 3.600 envases se arma en cajas de 24 envases y pallets de 50 cajas. ¿Cuántos pallets completos se arman?", "3600//24//50", "Se calculan las cajas y luego se dividen por las cajas de cada pallet.", " pallets"),
        ("=", "Para 3.600 envases se entregan 3.700 etiquetas y se dañan 60. ¿Cuántas etiquetas sobran?", "3700-3600-60", "A las entregadas se les restan las usadas y las dañadas.", " etiquetas"),
    ],
    ctx=("abc", "{F} El supervisor pide devolver las 50 etiquetas sobrantes a la bodega. ¿Qué forma es la correcta?", "Devolverlas contadas y registradas, sin dejarlas en la línea ni tirarlas", "Dejarlas en la línea para el próximo lote", "Tirarlas a la basura sin contarlas", "Las sobrantes se cuentan y se devuelven para que la conciliación cuadre."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calculan las cajas de un lote?", "Dividiendo los envases por los envases de cada caja", "Cada caja agrupa una cantidad fija de envases."),
        ("¿Cómo se calcula el porcentaje de etiquetas dañadas?", "Dañadas por 100, dividido por las entregadas", "El límite se mide respecto de lo entregado."),
        ("¿Qué se hace si se supera el límite de dañadas?", "Se revisa la causa con el supervisor", "Un valor sobre el límite indica un problema por investigar."),
    ],
    op=("Orden de ejemplo: lote L-700 de 1.800 envases; cajas de 24 envases; pallets de 25 cajas; línea de 300 envases por hora; etiquetas de envase entregadas: 1.900; usadas: 1.800; dañadas: 38; sobrantes devueltas: 62; precio de ejemplo de $6 por etiqueta; límite de dañadas de 2 % de las entregadas. "
        "Escribe: (a) cuántas cajas y pallets completos se arman, (b) cuántas horas dura el rotulado, (c) si las etiquetas concilian y qué porcentaje se dañó, y (d) el costo de las dañadas.",
        "(a) 1.800 ÷ 24 = 75 cajas y 75 ÷ 25 = 3 pallets. (b) 1.800 ÷ 300 = 6 horas. (c) 1.800 + 38 + 62 = 1.900: concilian; 38 × 100 ÷ 1.900 = 2 %, que no supera el límite. (d) 38 × 6 = 228 pesos.",
        ["calcula cajas, pallets y horas", "concilia y calcula el porcentaje", "calcula el costo de las dañadas"],
        ["hoja con las cuatro respuestas"],
        ["no sumar las sobrantes en la conciliación", "dividir por las usadas", "olvidar comparar con el límite"],
        "Pregunta: «¿qué pasaría si las dañadas fueran 100?». Debe decir que el porcentaje superaría el límite y se revisaría la causa."),
    reinforce="Inventa un lote con envases, envases por caja y cajas por pallet, y calcula cajas y pallets.",
    extend="Explica con un ejemplo inventado cómo la planificación de etiquetas evita detener la línea.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 5 (residuos de una planta de ejemplo, inventada). Residuos sólidos: recortes y cáscaras, cartón, plástico y vidrio roto. Residuos líquidos: agua de lavado con restos de producto y aceite usado. Residuos gaseosos: vapores y olores del proceso y gases de equipos de frío, que solo manejan personas autorizadas. "
     "Reglas generales: los residuos se separan en el lugar donde se generan; el aceite usado se guarda aparte y lo retira una empresa autorizada; los contenedores se vacían con la frecuencia que fija el programa. El plan de emergencia tiene vías de evacuación señalizadas y un punto de reunión. "
     "La norma de seguridad y la norma ambiental vigentes, y las autoridades sanitaria y ambiental, regulan y fiscalizan estos temas.")
build(
    O8, 1, F,
    use="Aprenderé a situar el manejo de residuos de una planta de alimentos: qué tipos hay, qué riesgos generan, qué diferencia hay entre prevención y emergencia y qué norma lo regula.",
    prior=["Conozco el flujo de una planta de alimentos.", "Sé sumar y multiplicar enteros.", "Sé leer una ficha con reglas."],
    explain=[
        "Un residuo es un material que la planta ya no usa y debe manejar con seguridad. Se clasifican por su estado: sólidos (recortes, cartón, plástico, vidrio), líquidos (agua de lavado, aceites usados) y gaseosos (vapores, olores y gases de equipos). También se clasifican por su peligrosidad: un residuo peligroso puede dañar a las personas o al ambiente, como un aceite usado o el envase de un producto químico, y requiere almacenamiento aparte y retiro por una empresa autorizada.",
        "Los residuos mal manejados generan riesgos: plagas y olores, contaminación del producto, contaminación del suelo y del agua, incendios y derrames. La prevención reúne las medidas que evitan el problema, como separar los residuos en origen, vaciar los contenedores con frecuencia y rotularlos. La emergencia es la respuesta cuando ocurre algo, como un derrame o un incendio, y sigue el plan de emergencia.",
        "En una emergencia se mantiene la calma, se evacúa por las vías señalizadas hasta el punto de reunión y se avisa a un adulto responsable y a emergencias. Quien no está capacitado no interviene en derrames de productos químicos, fugas de gas ni incendios. Este cuaderno no enseña a hacerlo." + LIMX,
    ],
    vocab=[("residuo", "material que la planta ya no usa y debe manejar con seguridad"), ("residuo peligroso", "residuo que puede dañar a las personas o al ambiente"), ("prevención", "medidas que evitan que ocurra el problema"), ("emergencia", "situación grave que exige una respuesta inmediata"), ("plan de emergencia", "documento con las acciones y las vías de evacuación ante una emergencia"), ("punto de reunión", "lugar seguro donde se juntan las personas al evacuar")],
    worked=[
        ("Clasificar un residuo", "El agua de lavado de un equipo, con restos de producto, ¿es un residuo sólido, líquido o gaseoso?", ["El agua es un líquido.", "Es un residuo líquido."], "Líquido"),
        ("Prevención o emergencia", "Vaciar los contenedores con la frecuencia del programa, ¿es prevención o respuesta a emergencia?", ["Se hace antes de que haya un problema.", "Eso es prevención."], "Prevención"),
    ],
    mistakes=[("Intentar limpiar un derrame de producto químico sin estar capacitado.", "Puede haber vapores o contacto con la piel y se agrava el riesgo.", "Aléjate, avisa a un adulto responsable y a emergencias, y no intervengas."),
              ("Mezclar todos los residuos en el mismo contenedor «para ahorrar tiempo».", "Dificulta su manejo y puede contaminar lo que podría aprovecharse.", "Separa los residuos en el lugar donde se generan.")],
    T=[
        ("abc", "{F} Las cáscaras y los recortes, ¿qué tipo de residuo son?", "Sólido", "Líquido", "Gaseoso", "Son materiales sólidos que quedan de la preparación."),
        ("abc", "{F} El agua de lavado con restos de producto, ¿qué tipo de residuo es?", "Líquido", "Sólido", "Gaseoso", "El agua es un residuo líquido."),
        ("abc", "{F} Los vapores y olores del proceso, ¿qué tipo de residuo son?", "Gaseoso", "Sólido", "Líquido", "Son emisiones que se dispersan en el aire."),
        ("abc", "{F} ¿Qué se hace con el aceite usado según las reglas de la ficha?", "Se guarda aparte y lo retira una empresa autorizada", "Se vierte al desagüe del piso", "Se mezcla con los recortes orgánicos", "La ficha indica almacenamiento aparte y retiro por una empresa autorizada."),
        ("abc", "{F} ¿Qué riesgo genera acumular residuos orgánicos sin vaciar los contenedores?", "Plagas y olores, y posible contaminación del producto", "Disminución del peso de los envases", "Pérdida de las etiquetas de bodega", "Los restos orgánicos atraen plagas y generan olores."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué diferencia hay entre prevención y emergencia?", "La prevención evita el problema y la emergencia es la respuesta cuando ocurre", "Son lo mismo con distinto nombre", "La prevención se hace después de la emergencia", "Prevenir es actuar antes; la emergencia exige responder a lo ocurrido."),
        ("=", "En una planta de ejemplo, cada turno genera 3 contenedores de 40 kg de recortes y trabajan 4 turnos al día. ¿Cuántos kg de recortes se generan por día?", "3*40*4", "Se multiplican los contenedores por su peso y por los turnos.", " kg"),
        ("abc", "{F} Se derrama un producto químico y una persona no capacitada está cerca. ¿Qué corresponde?", "Alejarse, avisar a un adulto responsable y a emergencias, y no intervenir", "Limpiarlo con lo que haya a mano", "Cubrirlo y seguir trabajando", "Intervenir sin capacitación agrava el riesgo."),
        ("abc", "{F} Suena la alarma de emergencia y un compañero quiere terminar antes su tarea. ¿Qué corresponde?", "Evacuar de inmediato por las vías señaladas hasta el punto de reunión", "Terminar la tarea para no perder tiempo", "Volver por sus pertenencias", "Una alarma exige evacuar sin demora siguiendo el plan."),
        ("abc", "Un operario deja cartón mojado junto a los recortes orgánicos «porque igual van en el mismo camión». ¿Qué respuesta corresponde?", "Se separan en el origen: mezclarlos dificulta su manejo y puede contaminarlos", "Es correcto, porque se ahorra espacio", "Es correcto si se hace el último día de la semana", "Separar en origen es la regla base del manejo de residuos."),
        ("abc", "¿Por qué el plan de emergencia debe conocerse antes de que ocurra una emergencia?", "Porque en la emergencia no hay tiempo de leerlo: se actúa con lo aprendido", "Porque las emergencias se anuncian con anticipación", "Porque el plan solo sirve a los visitantes", "La preparación previa permite actuar con rapidez y seguridad."),
        ("=", "{F} En una semana de ejemplo la planta genera 2.000 litros de agua de lavado con restos y 40 litros de aceite usado. ¿Cuántos litros de residuos líquidos son en total?", "2000+40", "Se suman los litros de cada residuo líquido.", " litros"),
        ("abc", "{F} Un jefe pide guardar el aceite usado junto a los envases limpios para ahorrar espacio. ¿Qué respuesta corresponde?", "No: el aceite usado se guarda aparte y lo retira una empresa autorizada", "Sí, si el bidón está bien cerrado", "Sí, si es solo por una semana", "La ficha exige almacenamiento aparte para el aceite usado."),
    ],
    ctx=("abc", "{F} Un vecino de la planta reclama por olores. El encargado dice que se debe a contenedores sin vaciar. ¿Qué medida preventiva es adecuada?", "Revisar el programa de vaciado y cumplir su frecuencia, con una persona responsable", "Vaciar los contenedores solo cuando están completamente llenos", "Cerrar los contenedores con más fuerza sin cambiar el vaciado", "Cumplir la frecuencia evita la acumulación que produce olores y plagas."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se clasifican los residuos por su estado?", "En sólidos, líquidos y gaseosos", "Es la primera clasificación para decidir su manejo."),
        ("¿Qué hace una persona no capacitada ante un derrame químico?", "Se aleja, avisa a un adulto responsable y a emergencias, y no interviene", "Intervenir sin capacitación agrava el riesgo para todos."),
        ("¿Qué se hace con el aceite usado?", "Se guarda aparte y lo retira una empresa autorizada", "Es un residuo peligroso que no se vierte."),
    ],
    op=("Una planta de ejemplo tiene estos residuos en una semana: recortes de verdura, cartón, aceite usado, agua de lavado, olores del proceso y el envase vacío de un producto de limpieza. "
        "Escribe: (a) el estado de cada residuo (sólido, líquido o gaseoso), (b) cuál tratarías como peligroso y por qué, (c) una medida de prevención y (d) qué haría una persona no capacitada si ocurre un derrame de un producto químico.",
        "(a) Recortes, cartón y envase vacío: sólidos; aceite usado y agua de lavado: líquidos; olores: gaseoso. (b) El aceite usado y el envase del producto de limpieza, porque pueden dañar a las personas o al ambiente. (c) Separar los residuos en origen y vaciar los contenedores con la frecuencia del programa. (d) Alejarse, avisar a un adulto responsable y a emergencias, y no intervenir.",
        ["clasifica los seis residuos", "identifica los peligrosos y justifica", "propone una prevención y la acción ante el derrame"],
        ["hoja con las cuatro respuestas"],
        ["clasificar los olores como líquidos", "intervenir en el derrame", "mezclar el aceite con los recortes"],
        "Pregunta: «¿qué pasaría si el aceite usado se vierte al desagüe?». Debe decir que contaminaría el agua y es un residuo peligroso."),
    reinforce="Escribe cinco residuos de una planta inventada y clasifícalos por estado y por peligrosidad.",
    extend="Explica con un ejemplo inventado por qué la prevención es más barata que responder a una emergencia.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 6 (residuos semanales de una planta de ejemplo, inventada). Recortes orgánicos, 800 kg: residuo no peligroso; destino, valorización. Cartón y plástico limpios, 180 kg: no peligrosos; destino, reciclaje. Vidrio roto, 30 kg: no peligroso pero cortante; se guarda en un contenedor rígido señalizado. "
     "Aceite usado, 40 litros: peligroso; se guarda aparte y lo retira una empresa autorizada. Envases vacíos de productos de limpieza: se tratan como residuo peligroso y no se reutilizan. Agua de lavado con restos de producto: residuo industrial líquido que se trata antes de salir de la planta, según la norma vigente. "
     "Cada retiro queda en un registro con la fecha, el tipo y la cantidad de residuo y el nombre de la empresa autorizada.")
build(
    O8, 2, F,
    use="Aprenderé el vocabulario del manejo de residuos: segregación, residuo peligroso, 3R, valorización, disposición final, empresa autorizada y registro de retiro.",
    prior=["Conozco los tipos de residuos y los riesgos.", "Sé sumar y restar enteros.", "Sé leer una tabla breve."],
    explain=[
        "La segregación en origen es separar los residuos en el lugar donde se generan, según su tipo. Las 3R son reducir (generar menos residuos), reutilizar (volver a usar lo que se puede) y reciclar (transformar el residuo en un material nuevo). La valorización es aprovechar el residuo, por ejemplo como material reciclable o para otros usos autorizados. Lo que no se puede valorizar va a disposición final, que es el destino definitivo.",
        "Un residuo peligroso se almacena aparte, rotulado, y lo retira una empresa autorizada. Los residuos industriales líquidos (riles) se tratan antes de salir de la planta, según la norma vigente. Cada retiro queda en un registro con la fecha, el tipo, la cantidad y la empresa. La hoja de datos de seguridad de un producto informa cómo manejar sus envases y residuos.",
        "Un vidrio roto se guarda en un contenedor rígido señalizado para no cortar a quien lo maneja. Los residuos nunca se queman ni se entierran por cuenta de la planta; el manejo lo define la norma vigente." + LIMX,
    ],
    vocab=[("segregación en origen", "separar los residuos en el lugar donde se generan"), ("3R", "reducir, reutilizar y reciclar"), ("valorización", "aprovechar un residuo en lugar de eliminarlo"), ("disposición final", "destino definitivo de lo que no se puede valorizar"), ("empresa autorizada", "empresa habilitada para retirar y tratar un tipo de residuo"), ("registro de retiro", "anotación de fecha, tipo, cantidad y empresa de cada retiro"), ("riles", "residuos industriales líquidos")],
    worked=[
        ("Clasificar una acción 3R", "Diseñar el corte de una materia prima para generar menos recortes, ¿es reducir, reutilizar o reciclar?", ["Se genera menos residuo desde el inicio.", "Eso es reducir."], "Reducir"),
        ("Leer una tabla", "En la tabla de una planta de ejemplo, el cartón limpio va a reciclaje. ¿Se valoriza o va a disposición final?", ["El reciclaje aprovecha el residuo.", "Eso es valorización."], "Se valoriza"),
    ],
    mistakes=[("Verter el aceite usado al desagüe «porque es poco».", "Es un residuo peligroso y contamina el agua aunque sea poco.", "Guárdalo aparte para que lo retire una empresa autorizada."),
              ("Retirar residuos sin dejar registro.", "No se puede probar a quién se entregaron ni cuánto.", "Anota fecha, tipo, cantidad y empresa en el registro de retiro.")],
    T=[
        ("abc", "{F} ¿Cómo se clasifica el aceite usado?", "Como residuo peligroso", "Como residuo no peligroso", "Como residuo gaseoso", "La ficha indica que es peligroso y se guarda aparte."),
        ("abc", "{F} ¿Cuál es el destino de los recortes orgánicos?", "Valorización", "Disposición final", "Reutilización directa en la línea", "La ficha asigna a los recortes el destino de valorización."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué son las 3R?", "Reducir, reutilizar y reciclar", "Recibir, rotular y retirar", "Registrar, revisar y reponer", "Las 3R son tres formas de manejar los residuos para generar menos."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es la segregación en origen?", "Separar los residuos en el lugar donde se generan", "Llevar todos los residuos a un solo contenedor", "Separar los residuos al llegar al vertedero", "Separar en origen evita mezclas que impiden su aprovechamiento."),
        ("abc", "En Elaboración Industrial de Alimentos: ¿qué es la valorización?", "Aprovechar un residuo en lugar de eliminarlo", "Eliminarlo en la disposición final", "Calcular el costo de los residuos", "Valorizar es darle un uso autorizado a lo que sería residuo."),
        ("abc", "{F} ¿Por qué el vidrio roto se guarda en un contenedor rígido y señalizado?", "Para no cortar a quien lo maneja", "Para que ocupe menos espacio en la bodega", "Para que no se mezcle con el aceite", "Es un residuo cortante que requiere un contenedor que lo contenga."),
        ("abc", "{F} ¿Qué se hace con los envases vacíos de productos de limpieza?", "Se tratan como residuo peligroso y no se reutilizan", "Se reutilizan para guardar alimentos", "Se mezclan con el cartón limpio", "El producto que contenían puede dejar residuos peligrosos."),
        ("abc", "{F} ¿Qué datos debe tener el registro de retiro?", "Fecha, tipo y cantidad de residuo, y empresa autorizada", "Solo el nombre del operario", "Solo la fecha", "El registro respalda a quién se entregó cada residuo, cuánto y cuándo."),
        ("abc", "Reutilizar una caja de cartón en buen estado para embalar otra cosa, ¿qué tipo de acción 3R es?", "Reutilizar", "Reciclar", "Reducir", "Volver a usar el objeto tal como está es reutilizar."),
        ("abc", "Un operario vacía aceite usado por el desagüe «porque es poco». ¿Qué respuesta corresponde?", "No: es un residuo peligroso que se guarda aparte y retira una empresa autorizada", "Está bien si es una cantidad pequeña", "Está bien si se diluye con agua", "El aceite contamina el agua aunque sea poco; su manejo es regulado."),
        ("abc", "¿Por qué es importante el registro de retiro?", "Prueba que el residuo se entregó a una empresa autorizada y permite rastrearlo", "Sirve para calcular el sueldo del operario", "Reemplaza el rótulo del residuo", "Sin registro no se puede demostrar el destino de los residuos."),
        ("=", "{F} ¿Cuántos kg de residuos sólidos no peligrosos se generan por semana, sumando recortes, cartón y plástico, y vidrio roto?", "800+180+30", "Se suman los kilos de cada residuo sólido no peligroso.", " kg"),
        ("abc", "{F} Un vecino pregunta qué hace la planta con el agua de lavado. ¿Qué respuesta es correcta según la ficha?", "Se trata antes de salir de la planta, según la norma vigente", "Se vierte directamente a la calle", "Se mezcla con el aceite usado", "La ficha indica que el agua se trata como residuo industrial líquido antes de salir."),
    ],
    ctx=("abc", "{F} El encargado nota que en el registro de retiro de ayer falta el nombre de la empresa. ¿Qué corresponde?", "Completar el dato con la empresa que efectivamente retiró y dejar constancia", "Dejarlo en blanco porque ya se retiró", "Inventar un nombre para completar", "El registro debe reflejar quién retiró el residuo para ser una prueba válida."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es un residuo peligroso?", "Uno que puede dañar a las personas o al ambiente", "Requiere almacenamiento aparte y retiro por empresa autorizada."),
        ("¿Qué significan las 3R?", "Reducir, reutilizar y reciclar", "Son tres formas de generar menos residuos."),
        ("¿Qué se anota en un registro de retiro?", "Fecha, tipo, cantidad y empresa autorizada", "Así se prueba el destino del residuo."),
    ],
    op=("Residuos semanales de ejemplo de otra planta: recortes orgánicos, 600 kg; cartón limpio, 150 kg; vidrio roto, 20 kg; aceite usado, 30 litros; envases vacíos de productos de limpieza, 12 unidades. "
        "Escribe: (a) qué residuos son peligrosos y qué se hace con ellos, (b) cuál va a valorización y cuál a reciclaje, (c) cuántos kg de residuos sólidos no peligrosos hay y (d) qué datos tendría el registro de retiro del aceite.",
        "(a) El aceite usado y los envases vacíos de productos de limpieza; se guardan aparte y los retira una empresa autorizada. (b) Los recortes van a valorización y el cartón limpio a reciclaje. (c) 600 + 150 + 20 = 770 kg. (d) Fecha, tipo (aceite usado), cantidad (30 litros) y nombre de la empresa autorizada.",
        ["identifica los residuos peligrosos y su manejo", "asigna destinos correctos", "calcula 770 kg y completa el registro"],
        ["hoja con las cuatro respuestas"],
        ["tratar los recortes como peligrosos", "olvidar el vidrio en la suma", "no incluir a la empresa autorizada"],
        "Pregunta: «¿qué pasaría si no se anota el retiro del aceite?». Debe decir que no habría prueba de su destino."),
    reinforce="Inventa una tabla de cuatro residuos de una planta con su estado, su peligrosidad y su destino.",
    extend="Explica con un ejemplo inventado cómo reducir un residuo desde el diseño del proceso ahorra costos de disposición.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 7 (revisión semanal de contenedores, de ejemplo e inventada). Ocho contenedores revisados: (1) orgánicos, solo recortes; (2) orgánicos, con bolsas plásticas dentro; (3) cartón y plástico, limpios; (4) cartón y plástico, con restos de producto y grasa; "
     "(5) vidrio, contenedor rígido cerrado; (6) peligrosos, aceite usado en bidón cerrado y rotulado; (7) peligrosos, bidón sin rótulo; (8) residuos no peligrosos generales, con un envase vacío de un producto de limpieza dentro. "
     "Los contenedores 1, 3, 5 y 6 cumplen; los demás no cumplen. Meta de ejemplo: al menos 90 % de contenedores que cumplen.")
build(
    O8, 3, F,
    use="Aprenderé a analizar un caso en papel: revisar contenedores de residuos, detectar errores de segregación, calcular el cumplimiento y proponer acciones correctivas y preventivas.",
    prior=["Conozco segregación, residuos peligrosos y 3R.", "Sé calcular porcentajes con enteros.", "Sé leer una lista de ítems."],
    explain=[
        "La revisión de contenedores comprueba que cada residuo esté en el contenedor que le corresponde. Un contenedor cumple cuando solo contiene lo que debe, está bien rotulado y cerrado si es peligroso. Un error de segregación puede contaminar un residuo aprovechable: por ejemplo, restos de grasa en el cartón impiden reciclarlo, y bolsas plásticas en los orgánicos dificultan su valorización.",
        "Un residuo peligroso en el contenedor equivocado es más grave, porque puede dañar a las personas o al ambiente. Un bidón de peligrosos sin rótulo no permite saber qué contiene ni cómo manejarlo. Para cada incumplimiento se define una acción correctiva (corregir el contenedor) y una acción preventiva (por ejemplo, capacitar y mejorar la señalética).",
        "Quien detecta un error lo informa y registra; no mueve por su cuenta un residuo peligroso desconocido. Si hay un olor extraño, un derrame o un bidón dañado, se aleja y avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("error de segregación", "residuo ubicado en un contenedor que no le corresponde"), ("contaminar un residuo", "mezclarlo con algo que impide aprovecharlo"), ("señalética", "carteles y colores que indican qué va en cada contenedor"), ("acción correctiva", "medida que corrige lo que falló"), ("acción preventiva", "medida que evita que vuelva a ocurrir")],
    worked=[
        ("Detectar un error", "Un contenedor de ejemplo de cartón limpio contiene también un envase vacío de producto químico. ¿Cumple?", ["El contenedor debe tener solo cartón limpio.", "El envase de producto químico está mal ubicado."], "No cumple"),
        ("Calcular el cumplimiento", "De 10 contenedores de ejemplo, 8 cumplen. ¿Qué porcentaje cumple?", ["Se multiplican los que cumplen por 100.", "8 × 100 ÷ 10 = 80."], "80 %"),
    ],
    mistakes=[("Mover por cuenta propia un bidón de peligrosos sin rótulo.", "No se sabe qué contiene ni cómo manejarlo, y puede haber un riesgo.", "No lo muevas, avisa al encargado y registra el hallazgo."),
              ("Corregir solo el contenedor y no capacitar ni mejorar la señalética.", "El error puede repetirse en la siguiente semana.", "Agrega una acción preventiva.")],
    T=[
        ("abc", "{F} ¿Cuántos contenedores no cumplen?", "Cuatro", "Tres", "Cinco", "Los contenedores 2, 4, 7 y 8 no cumplen."),
        ("=", "{F} ¿Qué porcentaje de los contenedores revisados cumple?", "4*100//8", "Se multiplican los contenedores que cumplen por 100 y se divide por el total.", " %"),
        ("abc", "{F} ¿Cumple la revisión la meta de 90 %?", "No, porque llega a 50 %", "Sí, porque la mitad cumple", "Sí, porque 4 es un número alto", "50 % es menor que la meta de 90 %."),
        ("abc", "{F} ¿Qué problema tiene el contenedor 2?", "Contiene bolsas plásticas que dificultan la valorización de los orgánicos", "Contiene un residuo peligroso", "No está cerrado", "Las bolsas plásticas contaminan un residuo orgánico aprovechable."),
        ("abc", "{F} ¿Qué problema tiene el contenedor 4?", "Los restos de producto y grasa impiden reciclar el cartón y el plástico", "Tiene vidrio roto", "Tiene aceite usado", "La grasa y los restos contaminan materiales que podrían reciclarse."),
        ("abc", "{F} ¿Qué problema tiene el contenedor 8?", "Contiene un envase de un producto de limpieza, que debe tratarse como residuo peligroso", "Está demasiado lleno", "Está rotulado con el color equivocado", "Un envase de limpieza no debe estar con residuos no peligrosos."),
        ("abc", "{F} ¿Cuál de los errores es el más grave y por qué?", "El bidón de peligrosos sin rótulo, porque no se sabe qué contiene ni cómo manejarlo", "Las bolsas plásticas en los orgánicos, porque ocupan espacio", "La grasa en el cartón, porque mancha", "Un peligroso sin rótulo expone a las personas y al ambiente."),
        ("abc", "{F} ¿Qué acción correctiva corresponde para el contenedor 4?", "Retirar el material contaminado y dejarlo en el contenedor correcto, informando al encargado", "Tapar el contenedor con una caja", "Esperar a la próxima revisión", "La acción correctiva soluciona lo que está mal ubicado y se informa."),
        ("abc", "{F} ¿Qué acción preventiva es adecuada para evitar los errores de segregación?", "Capacitar al personal y mejorar la señalética de cada contenedor", "Cambiar el color de las bolsas", "Reducir la frecuencia de revisión", "La capacitación y la señalética previenen que se repitan los errores."),
        ("=", "{F} Si se corrigen 2 de los 4 contenedores que no cumplen, ¿qué porcentaje cumpliría?", "(4+2)*100//8", "Se suman los contenedores corregidos a los que ya cumplían.", " %"),
        ("abc", "El encargado encuentra un bidón sin rótulo y con olor extraño. ¿Qué corresponde hacer a un operario no capacitado?", "Alejarse, avisar al encargado y a un adulto responsable, y no moverlo", "Abrirlo para ver qué contiene", "Moverlo al patio para ventilarlo", "Un contenido desconocido con olor extraño puede ser peligroso y no se manipula."),
        ("=", "En otra revisión de ejemplo hay 20 contenedores y 17 cumplen. ¿Qué porcentaje cumple?", "17*100//20", "Se multiplican los contenedores que cumplen por 100 y se divide por el total.", " %"),
        ("abc", "{F} El jefe propone no informar los cuatro incumplimientos porque «bajan la nota de la planta». ¿Qué corresponde?", "Informar los cuatro con sus acciones correctivas, porque ocultarlos impide corregir", "No informar, si se corrigen enseguida", "Informar solo el del bidón sin rótulo", "El informe debe reflejar lo observado para poder mejorar."),
    ],
    ctx=("abc", "{F} Una empresa autorizada llega a retirar el aceite usado, pero el bidón del contenedor 7 no tiene rótulo. ¿Qué corresponde?", "No entregarlo sin identificar su contenido y avisar al encargado, para que el responsable lo identifique y rotule según el procedimiento", "Entregarlo igual para que se lo lleven", "Rotularlo con un nombre cualquiera", "Un residuo peligroso debe estar identificado para su manejo y retiro."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué es un error de segregación?", "Un residuo ubicado en un contenedor que no le corresponde", "Puede contaminar residuos aprovechables o crear un riesgo."),
        ("¿Qué hace quien encuentra un bidón de peligrosos sin rótulo?", "No lo mueve y avisa al encargado", "No se sabe qué contiene ni cómo manejarlo."),
        ("¿Cuál es una acción preventiva para los errores de segregación?", "Capacitar y mejorar la señalética", "Evita que los errores se repitan."),
    ],
    op=("Revisión de ejemplo de 10 contenedores: cumplen 7. Los que no cumplen: (a) orgánicos con vidrio roto dentro, (b) peligrosos con un bidón sin rótulo, (c) cartón mojado con restos de grasa. Meta de ejemplo: 90 %. "
        "Escribe: (a) el porcentaje de cumplimiento, (b) si cumple la meta, (c) el error más grave y por qué, (d) una acción correctiva y una preventiva para el bidón sin rótulo.",
        "(a) 7 × 100 ÷ 10 = 70 %. (b) No cumple la meta de 90 %. (c) El bidón de peligrosos sin rótulo, porque no se sabe qué contiene ni cómo manejarlo. (d) Correctiva: no moverlo y avisar al encargado, para que el responsable lo identifique y rotule según el procedimiento. Preventiva: revisar que todos los bidones se rotulen al llenarse y capacitar al personal.",
        ["calcula el 70 % y compara con la meta", "elige el error más grave y lo justifica", "propone una acción correctiva y una preventiva"],
        ["hoja con las cuatro respuestas"],
        ["decir que cumple la meta", "proponer abrir el bidón", "confundir correctiva con preventiva"],
        "Pregunta: «¿qué se debe hacer primero con el bidón sin rótulo?». Debe decir que no moverlo y avisar al encargado."),
    reinforce="Inventa una revisión de ocho contenedores con tres errores y calcula el porcentaje de cumplimiento.",
    extend="Explica con un ejemplo inventado por qué la señalética clara reduce los errores de segregación.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 8 (indicadores de residuos de una planta de ejemplo, inventada). Semana base: se generaron 1.200 kg de residuos; 780 kg se valorizaron o reciclaron y 420 kg fueron a disposición final. "
     "Costos de ejemplo: valorización, $25 por kg; disposición final, $60 por kg. Meta de ejemplo: al menos 60 % de los residuos valorizados. "
     "Después de mejorar la segregación en origen, una semana siguiente tuvo 1.200 kg de residuos, con 900 kg valorizados y 300 kg a disposición final.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular el porcentaje de valorización, el costo de manejo de residuos y el ahorro de una mejora.",
    prior=["Conozco segregación, valorización y disposición final.", "Sé calcular porcentajes con enteros.", "Sé multiplicar, sumar y restar enteros."],
    explain=[
        "Un indicador de residuos resume cómo va el manejo. El porcentaje de valorización se calcula con los kg valorizados por 100, dividido por los kg totales generados. Se compara con una meta, que aquí es de ejemplo. Mientras más residuo se valoriza, menos va a disposición final.",
        "El costo de manejo se calcula multiplicando los kg de cada destino por su costo por kg y sumando. Una mejora de la segregación en origen suele aumentar la parte valorizada y reducir el costo total, porque la disposición final es más cara que la valorización en este ejemplo. El ahorro es el costo antes menos el costo después.",
        "Mejorar la segregación exige que el personal sepa qué va en cada contenedor y que la señalética sea clara. Los indicadores se registran semana a semana para ver la tendencia. Todo el manejo de residuos se hace conforme a la norma vigente." + LIM,
    ],
    vocab=[("indicador", "dato calculado que resume cómo va un proceso"), ("porcentaje de valorización", "kg valorizados por 100, dividido por los kg generados"), ("costo de manejo", "suma de los kg de cada destino por su costo por kg"), ("ahorro", "costo antes de una mejora menos costo después"), ("tendencia", "dirección en que cambia un indicador con el tiempo")],
    worked=[
        ("Calcular la valorización", "Una planta de ejemplo genera 500 kg de residuos y valoriza 300 kg. ¿Qué porcentaje valoriza?", ["Se multiplican los kg valorizados por 100.", "300 × 100 ÷ 500 = 60."], "60 %"),
        ("Calcular un ahorro", "El costo semanal de ejemplo era de $20.000 y después de una mejora es de $16.000. ¿Cuál es el ahorro?", ["Se resta el costo después al costo antes.", "20.000 − 16.000 = 4.000."], "$4.000 por semana"),
    ],
    mistakes=[("Calcular el porcentaje de valorización dividiendo por los kg valorizados.", "Se debe dividir por el total generado, que es la base.", "Divide por los kg totales y multiplica por 100."),
              ("Medir una sola semana y asegurar que la mejora es permanente.", "Una semana puede ser una excepción.", "Registra varias semanas y mira la tendencia.")],
    T=[
        ("=", "{F} En la semana base, ¿qué porcentaje de los residuos se valorizó?", "780*100//1200", "Se multiplican los kg valorizados por 100 y se divide por el total.", " %"),
        ("abc", "{F} ¿Cumplió la semana base la meta de 60 %?", "Sí, porque 65 % supera el 60 % exigido", "No, porque 65 % es menor que la meta", "No, porque la meta es 100 %", "El 65 % calculado es mayor que el mínimo de 60 %."),
        ("=", "{F} ¿Cuántos pesos costó la valorización de la semana base?", "780*25", "Se multiplican los kg valorizados por el costo por kg.", " pesos"),
        ("=", "{F} ¿Cuántos pesos costó la disposición final de la semana base?", "420*60", "Se multiplican los kg de disposición final por su costo por kg.", " pesos"),
        ("=", "{F} ¿Cuál fue el costo total de manejo de la semana base?", "780*25+420*60", "Se suman los costos de valorización y de disposición final.", " pesos"),
        ("=", "{F} ¿Qué porcentaje se valorizó en la semana posterior a la mejora?", "900*100//1200", "Se multiplican los kg valorizados por 100 y se divide por el total.", " %"),
        ("=", "{F} ¿Cuál fue el costo total de manejo de la semana posterior a la mejora?", "900*25+300*60", "Se suman los costos de valorización y de disposición final.", " pesos"),
        ("=", "{F} ¿Cuántos pesos ahorró la planta en esa semana respecto de la semana base?", "(780*25+420*60)-(900*25+300*60)", "Se resta el costo posterior al costo de la semana base.", " pesos"),
        ("abc", "{F} ¿Por qué la mejora redujo el costo total?", "Porque más kg pasaron a valorización, que cuesta menos que la disposición final", "Porque se generaron menos residuos en total", "Porque la valorización es más cara que la disposición final", "En el ejemplo, la valorización cuesta $25 por kg y la disposición final $60."),
        ("abc", "Un jefe dice que, como una semana mejoró, la mejora es permanente. ¿Qué respuesta es correcta?", "Hay que registrar varias semanas y observar la tendencia antes de concluir", "Tiene razón, una semana basta", "Solo importa el resultado del primer día", "Una sola semana puede ser una excepción."),
        ("abc", "¿Qué acción puede aumentar la valorización sin comprar nada nuevo?", "Capacitar al personal en segregación y mejorar la señalética de los contenedores", "Mezclar todos los residuos en un solo contenedor", "Reducir la frecuencia del retiro", "Separar bien en origen permite aprovechar más residuos."),
        ("=", "En otra semana de ejemplo se generaron 2.000 kg de residuos y se valorizaron 1.400 kg. ¿Qué porcentaje se valorizó?", "1400*100//2000", "Se multiplican los kg valorizados por 100 y se divide por el total.", " %"),
        ("=", "Con costos de ejemplo de $25 por kg valorizado y $60 por kg a disposición final, 600 kg que se desvían de disposición final a valorización, ¿cuántos pesos se ahorran?", "600*(60-25)", "Cada kg desviado ahorra la diferencia entre ambos costos.", " pesos"),
    ],
    ctx=("abc", "{F} El encargado quiere reportar solo la semana posterior a la mejora y no la semana base. ¿Qué corresponde?", "Reportar ambas semanas para que se vea el cambio y su efecto", "Reportar solo la semana mejor", "No reportar ninguna", "Comparar antes y después es lo que permite demostrar el efecto de la mejora."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿cómo se calcula el porcentaje de valorización?", "Kg valorizados por 100, dividido por los kg generados", "Relaciona lo aprovechado con el total."),
        ("¿Cómo se calcula el ahorro de una mejora?", "Costo antes menos costo después", "Mide cuánto menos dinero se gasta después de la mejora."),
        ("¿Por qué se miran varias semanas?", "Para ver la tendencia y no una excepción", "Una sola semana puede no ser representativa."),
    ],
    op=("Datos de ejemplo de otra planta: semana base de 1.000 kg de residuos, con 500 kg valorizados y 500 kg a disposición final; semana posterior de 1.000 kg, con 700 kg valorizados y 300 kg a disposición final. Costos de ejemplo: valorización $20 por kg y disposición final $50 por kg. Meta: al menos 60 % valorizado. "
        "Escribe: (a) el porcentaje valorizado en cada semana, (b) cuál cumple la meta, (c) el costo de manejo de cada semana y (d) el ahorro.",
        "(a) Semana base: 50 %; semana posterior: 70 %. (b) Cumple la semana posterior. (c) Base: 500 × 20 + 500 × 50 = 35.000 pesos; posterior: 700 × 20 + 300 × 50 = 29.000 pesos. (d) 35.000 − 29.000 = 6.000 pesos.",
        ["calcula 50 % y 70 %", "calcula los dos costos", "calcula el ahorro de 6.000 pesos"],
        ["hoja con las cuatro respuestas"],
        ["dividir por los kg valorizados", "usar el mismo costo para ambos destinos", "olvidar restar los costos"],
        "Pregunta: «¿qué pasaría si la semana posterior fuera una excepción?». Debe decir que habría que mirar más semanas."),
    reinforce="Inventa una planta con residuos, valorizados y disposición final, y calcula su porcentaje de valorización.",
    extend="Explica con un ejemplo inventado por qué mejorar la segregación puede ahorrar dinero y reducir el impacto ambiental.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 9 (comparación de alternativas y verificación, de ejemplo e inventada). Se generan 800 kg de residuos orgánicos por semana. Alternativa A: disposición final, $60 por kg. Alternativa B: entrega a valorización, $25 por kg más un cargo fijo de transporte de $6.000 por semana. "
     "Indicador de valorización después de elegir B, en cuatro semanas: 56 %, 60 %, 64 % y 68 %; meta de ejemplo: al menos 60 %. "
     "Simulacro de evacuación de ejemplo: 40 personas en la planta; 38 llegaron al punto de reunión en el tiempo previsto; a las 2 restantes se las buscó con la lista de asistencia.")
build(
    O8, 5, F,
    use="Aprenderé a comparar alternativas de manejo de residuos con costos y beneficios, a verificar con indicadores si una decisión funciona y a evaluar un simulacro de emergencia.",
    prior=["Conozco valorización, disposición final y 3R.", "Sé calcular porcentajes y promedios con enteros.", "Conozco el plan de emergencia."],
    explain=[
        "Para comparar alternativas se calcula el costo de cada una con los mismos datos y se miran también los beneficios ambientales, como los kg que se evitan enviar a disposición final. La alternativa más barata no siempre es la mejor, pero tampoco se elige solo por ser más cara. La decisión se justifica con los datos y con la norma vigente.",
        "Elegir una alternativa no termina el trabajo: se verifica con un indicador durante varias semanas, para comprobar si se logra la meta y cuál es la tendencia. Si no se logra, se revisa la causa y se corrige. El promedio de varias semanas resume el resultado.",
        "Un simulacro es un ejercicio de emergencia planificado. Se evalúa cuántas personas llegaron al punto de reunión, cuánto tardaron y qué falló. Las personas faltantes se buscan con la lista de asistencia, sin que nadie vuelva a las zonas peligrosas. Ante una emergencia real se avisa a un adulto responsable y a emergencias." + LIMX,
    ],
    vocab=[("alternativa", "una de las opciones posibles para resolver un problema"), ("costo-beneficio", "comparación entre lo que cuesta una opción y lo que aporta"), ("verificación", "comprobación posterior de que la decisión funcionó"), ("simulacro", "ejercicio planificado que practica la respuesta a una emergencia"), ("lista de asistencia", "registro de las personas presentes, que sirve para ubicar a quien falta")],
    worked=[
        ("Comparar costos", "La alternativa X de ejemplo cuesta $50 por kg y la alternativa Y cuesta $20 por kg más $4.000 fijos. Para 200 kg, ¿cuál cuesta menos?", ["X cuesta 200 × 50 = 10.000.", "Y cuesta 200 × 20 + 4.000 = 8.000."], "La alternativa Y"),
        ("Calcular un promedio", "Cuatro semanas de ejemplo tuvieron valorización de 50 %, 60 %, 70 % y 80 %. ¿Cuál es el promedio?", ["Se suman: 50 + 60 + 70 + 80 = 260.", "260 ÷ 4 = 65."], "65 %"),
    ],
    mistakes=[("Elegir la alternativa solo por el precio por kg, sin sumar los cargos fijos.", "El costo total puede cambiar al incluir todos los cargos.", "Calcula el costo total de cada alternativa con todos sus componentes."),
              ("Volver a la zona de trabajo durante un simulacro para buscar a alguien.", "Se pone en riesgo a más personas; la búsqueda la organiza la persona responsable.", "Quédate en el punto de reunión y avisa quién falta.")],
    T=[
        ("=", "{F} ¿Cuántos pesos cuesta por semana la alternativa A (disposición final)?", "800*60", "Se multiplican los kg por el costo por kg.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta por semana la alternativa B, con el cargo de transporte incluido?", "800*25+6000", "Se suman el costo por kg total y el cargo fijo.", " pesos"),
        ("abc", "{F} ¿Qué alternativa cuesta menos por semana?", "La alternativa B", "La alternativa A", "Cuestan lo mismo", "B cuesta 26.000 pesos y A cuesta 48.000 pesos."),
        ("=", "{F} ¿Cuántos pesos se ahorran por semana al elegir B en lugar de A?", "800*60-(800*25+6000)", "Se resta el costo de B al costo de A.", " pesos"),
        ("=", "{F} ¿Cuántos pesos se ahorran en 4 semanas al elegir B?", "(800*60-(800*25+6000))*4", "Se multiplica el ahorro semanal por las semanas.", " pesos"),
        ("abc", "{F} ¿Qué beneficio ambiental tiene B respecto de A, además del costo?", "Evita enviar 800 kg semanales a disposición final", "Aumenta la cantidad de residuos generados", "Elimina la necesidad de segregar", "La valorización aprovecha los residuos en lugar de eliminarlos."),
        ("=", "{F} ¿Cuál es el promedio de valorización de las cuatro semanas, en porcentaje?", "(56+60+64+68)//4", "El promedio es la suma de los valores dividida por la cantidad de semanas.", " %"),
        ("abc", "{F} ¿Cuántas de las cuatro semanas cumplieron la meta de 60 %?", "Tres semanas", "Dos semanas", "Cuatro semanas", "Las semanas de 60 %, 64 % y 68 % cumplen; la de 56 % no."),
        ("abc", "{F} ¿Qué tendencia muestra el indicador de valorización?", "Sube semana a semana", "Baja semana a semana", "Se mantiene constante", "Los valores crecen de 56 % a 68 %."),
        ("abc", "{F} Un jefe propone cancelar la verificación porque ya se eligió B. ¿Qué respuesta corresponde?", "La verificación se mantiene para comprobar que se logra la meta y detectar problemas a tiempo", "Tiene razón, porque la decisión ya se tomó", "Se verifica solo si hay reclamos", "La verificación comprueba que la decisión funcione en la práctica."),
        ("abc", "{F} En el simulacro, 38 de 40 personas llegaron al punto de reunión. ¿Qué corresponde hacer con las 2 restantes?", "Buscarlas con la lista de asistencia, organizado por la persona responsable", "Que cada persona vuelva a buscarlas", "Ignorarlas, porque son pocas", "La búsqueda ordenada evita poner en riesgo a más personas."),
        ("=", "{F} ¿Qué porcentaje de las personas llegó al punto de reunión en el tiempo previsto?", "38*100//40", "Se multiplican las personas que llegaron por 100 y se divide por el total.", " %"),
        ("abc", "{F} Si la meta de un simulacro es que todas las personas lleguen al punto de reunión, ¿qué conclusión corresponde?", "No se cumplió: hay que analizar por qué faltaron 2 personas y corregir", "Se cumplió, porque casi todos llegaron", "No importa, porque era un simulacro", "Un simulacro sirve para detectar fallas antes de una emergencia real."),
    ],
    ctx=("abc", "{F} Un compañero propone no registrar los resultados del simulacro «porque no fue una emergencia real». ¿Qué respuesta corresponde?", "Se registra: los resultados permiten corregir fallas del plan antes de una emergencia real", "No se registra, porque un simulacro no cuenta", "Se registra solo si todo salió bien", "El registro del simulacro permite mejorar el plan de emergencia."),
    sc=[
        ("En Elaboración Industrial de Alimentos: ¿qué debe incluir la comparación de costos de dos alternativas?", "Todos los componentes de cada alternativa, incluidos los cargos fijos", "Así se comparan los costos totales."),
        ("¿Para qué se verifica una decisión con un indicador?", "Para comprobar que funciona en la práctica", "Puede que lo planificado no se logre."),
        ("¿Qué se evalúa en un simulacro?", "Cuántos llegaron al punto de reunión, cuánto tardaron y qué falló", "Permite mejorar el plan antes de una emergencia real."),
    ],
    op=("Datos de ejemplo. Se generan 500 kg de residuos orgánicos por semana. Alternativa A: disposición final a $50 por kg. Alternativa B: valorización a $20 por kg más $3.000 fijos de transporte por semana. Indicador de valorización con B en cuatro semanas: 52 %, 58 %, 64 % y 70 %; meta: al menos 60 %. "
        "Escribe: (a) el costo semanal de cada alternativa, (b) cuál eliges y por qué, (c) el promedio de valorización de las cuatro semanas y cuántas cumplieron la meta, y (d) una razón para seguir verificando.",
        "(a) A: 500 × 50 = 25.000 pesos; B: 500 × 20 + 3.000 = 13.000 pesos. (b) B, porque cuesta menos y evita enviar 500 kg a disposición final. (c) (52 + 58 + 64 + 70) ÷ 4 = 61 %; cumplen dos semanas (64 % y 70 %). (d) Para comprobar que se mantiene la tendencia a subir y detectar problemas a tiempo.",
        ["calcula los costos de A y B", "elige con razones de costo y ambiente", "calcula el promedio, cuenta las semanas y justifica la verificación"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el cargo fijo", "contar tres semanas sobre la meta", "no justificar la verificación"],
        "Pregunta: «¿qué pasaría con el costo si el cargo fijo subiera a $15.000?». Debe calcular que B costaría 25.000 pesos, igual que A."),
    reinforce="Inventa dos alternativas de manejo de un residuo con sus costos y calcula cuál cuesta menos por semana.",
    extend="Explica con un ejemplo inventado por qué un simulacro con fallas es útil.",
)
