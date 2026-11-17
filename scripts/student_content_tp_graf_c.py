"""Gráfica TP 3.º y 4.º medio: OAE-06 (postimpresión: corte, plegado, encuadernación y terminaciones, solo conceptos y cálculos en papel) y OAE-07 (mantenimiento básico de equipos de preimpresión, impresión y postimpresión, solo conceptos, planes y registros). Sin procedimientos operativos; datos inventados."""
from __future__ import annotations

from tp_graf_common import build

O6 = "TP-GRAF-3y4-OAE-06"
O7 = "TP-GRAF-3y4-OAE-07"
MAQ = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). Trabajo: 3.000 catálogos de 32 páginas, tapa blanda. Operaciones de postimpresión: corte, plegado, alzado (ordenar los cuadernillos de un mismo ejemplar), encuadernación y empaque. "
     "Equipos: guillotina (máquina de corte de papel), plegadora y encuadernadora. Un cuadernillo es un pliego plegado que forma un grupo de páginas; en este trabajo, cada cuadernillo tiene 16 páginas. "
     "Reglas de ejemplo: solo personal autorizado opera máquinas de corte; las cuchillas y los resguardos no se tocan; los recortes de papel se separan para reciclaje; las cajas se mueven con ayuda o con carro. Documentos: la OT, el manual del fabricante y la hoja de control de postimpresión.")
build(
    O6, 1, F,
    use="Aprenderé qué operaciones forman la postimpresión, qué documentos las guían y qué riesgos, ergonomía y cuidados ambientales las rodean, sin operar ninguna máquina.",
    prior=["Conozco la OT y las fases del proceso gráfico.", "Sé calcular divisiones y multiplicaciones.", "Sé qué son los resguardos."],
    explain=[
        "La postimpresión es la fase en que el material impreso se transforma en el producto final: se corta, se pliega, se ordena, se encuaderna y se empaca. Las máquinas de corte de papel, como la guillotina, tienen cuchillas muy filosas, por lo que existe el riesgo de cortes graves. Por eso solo las opera personal autorizado y capacitado, siempre con los resguardos en su lugar.",
        "Una hoja de control de postimpresión registra las cantidades, las medidas y los problemas detectados. El alzado ordena los cuadernillos de cada ejemplar en la secuencia correcta. En el área de terminación también importan la ergonomía (mover cajas con ayuda o con carro, hacer pausas) y el ambiente (separar los recortes de papel para reciclaje y mantener el orden).",
        "Este cuaderno describe conceptos y documentos de la postimpresión y no enseña a manejar las máquinas." + MAQ,
    ],
    vocab=[("postimpresión", "fase en que el impreso se corta, pliega, ordena y encuaderna"), ("guillotina", "máquina de corte de papel con cuchilla"), ("cuadernillo", "pliego plegado que forma un grupo de páginas"), ("alzado", "orden de los cuadernillos de un mismo ejemplar"), ("encuadernación", "unión de las hojas o cuadernillos para formar un libro o catálogo"), ("hoja de control", "registro de cantidades, medidas y problemas")],
    worked=[
        ("Cuadernillos de un catálogo", "Un catálogo de ejemplo tiene 48 páginas y cada cuadernillo 16. ¿Cuántos cuadernillos tiene?", ["Se divide el total de páginas por las de cada cuadernillo.", "48 ÷ 16 = 3."], "3 cuadernillos"),
        ("Cajas necesarias", "Un pedido de ejemplo de 900 folletos se entrega en cajas de 100. ¿Cuántas cajas se necesitan?", ["Se divide la cantidad por las que caben en una caja.", "900 ÷ 100 = 9."], "9 cajas"),
    ],
    mistakes=[("Acercar la mano a la cuchilla de una máquina de corte «solo para ver cómo está».", "Las cuchillas pueden causar cortes graves y solo se intervienen con personal autorizado y la máquina asegurada.", "Mantén distancia y avisa a la persona responsable."),
              ("Botar los recortes de papel en la basura común.", "El papel limpio puede reciclarse si se separa de otros residuos.", "Sepáralo en el contenedor indicado para reciclaje.")],
    T=[
        ("abc", "En Gráfica: ¿qué es la postimpresión?", "La fase en que el impreso se corta, pliega, ordena y encuaderna", "La fase en que se prepara el archivo", "La fase en que se mezclan las tintas", "La postimpresión termina el producto después de imprimir."),
        ("abc", "{F} ¿Cuántas páginas tiene cada catálogo?", "32 páginas", "16 páginas", "3.000 páginas", "El pedido es de catálogos de 32 páginas; 16 es el tamaño de un cuadernillo."),
        ("abc", "{F} ¿Qué operación ordena los cuadernillos de un mismo ejemplar?", "El alzado", "El empaque", "El corte", "Según la ficha, el alzado ordena los cuadernillos de cada ejemplar."),
        ("=", "{F} Los catálogos se entregan en cajas de 50. ¿Cuántas cajas se necesitan para los 3.000 catálogos?", "3000//50", "Se divide el pedido por los catálogos que caben en cada caja.", " cajas"),
        ("abc", "¿Qué riesgo general tienen las máquinas de corte de papel?", "Cortes graves por las cuchillas", "Que el papel cambie de color", "Que se acabe la tinta", "Las cuchillas son filosas y pueden provocar lesiones serias."),
        ("abc", "{F} ¿Dónde se ponen los recortes de papel?", "Separados, para reciclaje", "Mezclados con residuos químicos", "En el desagüe", "Los recortes de papel limpio pueden reciclarse si se separan."),
        ("=", "{F} Cada catálogo tiene 2 cuadernillos. ¿Cuántos cuadernillos se necesitan para 3.000 catálogos?", "3000*2", "Se multiplican los catálogos por los cuadernillos de cada uno.", " cuadernillos"),
        ("abc", "Un ayudante quiere revisar la cuchilla de una guillotina con las manos mientras está encendida. ¿Qué corresponde?", "No hacerlo: las cuchillas solo las interviene personal autorizado con la máquina asegurada", "Hacerlo con cuidado", "Hacerlo si usa guantes", "Acercar las manos a una cuchilla es un riesgo grave y se prohíbe."),
        ("abc", "¿Qué práctica ergonómica corresponde al mover cajas de catálogos?", "Pedir ayuda o usar un carro, según la norma vigente", "Levantarlas rápido con la espalda", "Arrastrarlas por el piso", "Mover cargas sin apoyo puede lesionar la espalda."),
        ("abc", "{F} Un compañero dice: «la guillotina es una máquina como cualquier otra, la puede usar quien quiera». ¿Qué respondes?", "La ficha exige personal autorizado y capacitado, por el riesgo de las cuchillas", "Tiene razón: no tiene riesgo", "Solo aplica en la mañana", "Las reglas de ejemplo del taller limitan su uso a personal autorizado."),
        ("abc", "Terminada la jornada hay recortes de papel en el piso, cerca de la máquina de corte. ¿Qué corresponde?", "Dejar la máquina detenida y asegurada y retirar los recortes para reciclaje", "Pisarlos y seguir", "Taparlos con un trapo", "El orden evita tropiezos y el papel se separa para reciclar."),
        ("abc", "{F} ¿Para qué sirve la hoja de control de postimpresión?", "Para registrar cantidades, medidas y problemas del trabajo", "Para cobrar al cliente", "Para guardar las cuchillas", "La hoja de control deja constancia de lo hecho y lo detectado."),
        ("=", "{F} Armar y cerrar cada caja demora 3 minutos. ¿Cuántos minutos se necesitan para las cajas del pedido, trabajando una sola persona?", "3000//50*3", "Se calculan las cajas del pedido y se multiplican por los minutos de cada una.", " minutos"),
    ],
    ctx=("abc", "Un conocido de ejemplo te ofrece dejarte «probar» su cortadora de papel en su imprenta sin instructor. ¿Qué respondes?", "Que solo trabajarás con instructor autorizado, porque este aprendizaje es conceptual", "Que aceptas si no hay nadie más", "Que aceptas si tienes cuidado", "Las máquinas de corte exigen autorización y capacitación."),
    sc=[
        ("En Gráfica: ¿qué máquina corta papel con una cuchilla?", "La guillotina", "Es la máquina de corte de papel de la ficha."),
        ("¿Quién opera las máquinas de corte?", "Personal autorizado y capacitado", "El riesgo de las cuchillas exige capacitación."),
        ("¿Qué haces con los recortes de papel?", "Los separo para reciclaje", "El papel limpio se recicla si no se mezcla."),
    ],
    op=("Un taller de ejemplo debe entregar 2.400 revistas de 48 páginas con cuadernillos de 16 páginas, en cajas de 40. Calcula cuántos cuadernillos se necesitan en total y cuántas cajas. Además, escribe tres cuidados de seguridad, ergonomía o ambiente que respetarías en la zona de postimpresión.",
        "Cuadernillos por revista: 48 ÷ 16 = 3; en total 2.400 × 3 = 7.200. Cajas: 2.400 ÷ 40 = 60. Cuidados: no acercarse a las cuchillas y dejar las máquinas de corte a personal autorizado; mover cajas con ayuda o carro; separar los recortes de papel para reciclaje.",
        ["calcula cuadernillos y cajas", "nombra tres cuidados distintos", "no describe cómo operar una máquina"],
        ["hoja con los cálculos y los tres cuidados"],
        ["multiplicar mal los cuadernillos", "olvidar las cajas", "escribir pasos para cortar"],
        "Pregunta: «¿por qué solo personal autorizado opera la guillotina?». Si responde 'es difícil', recuerda el riesgo de cortes graves."),
    reinforce="Haz una lista de cinco operaciones de postimpresión y escribe, para cada una, un cuidado de seguridad u orden.",
    extend="Explica por qué separar los recortes de papel para reciclaje es parte del trabajo en un taller gráfico.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (glosario de ejemplo, inventado). Refilado: corte de los bordes del impreso para dejarlo al tamaño final. Díptico: hoja con 1 pliegue y 2 paneles por cara. Tríptico: hoja con 2 pliegues y 3 paneles por cara. "
     "Laminado: cubrir el impreso con una película plástica. Barniz: capa transparente que protege o da brillo. Troquelado: corte con forma, hecho con un molde llamado troquel. "
     "Encuadernación rústica: las hojas se pegan en el lomo; espiral: un alambre o plástico en espiral pasa por perforaciones y el cuaderno se abre plano; corchete: grapas en el lomo. Lomo: borde por donde se unen las hojas.")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario de las terminaciones: refilado, plegado, laminado, barniz, troquelado y tipos de encuadernación, y para qué sirve cada una.",
    prior=["Conozco la postimpresión y los cuadernillos.", "Sé multiplicar y dividir.", "Sé leer una OT."],
    explain=[
        "Las terminaciones dan al impreso su forma y su protección. El refilado corta los bordes para dejar el tamaño final. El plegado dobla la hoja: un díptico tiene un pliegue y dos paneles por cara, y un tríptico tiene dos pliegues y tres paneles por cara. El troquelado corta una forma, como una estrella, con un molde llamado troquel.",
        "El laminado cubre el impreso con una película plástica y el barniz es una capa transparente que protege o da brillo; no son lo mismo. La encuadernación une las hojas: en la rústica van pegadas en el lomo, en la espiral un alambre o plástico en espiral atraviesa perforaciones y permite abrir plano el cuaderno, y en el corchete se usan grapas en el lomo.",
        "Conocer estos términos sirve para leer una OT y conversar con el equipo. Estos conceptos no enseñan a operar las máquinas de terminación." + MAQ,
    ],
    vocab=[("refilado", "corte de los bordes para dejar el tamaño final"), ("díptico", "hoja con un pliegue y dos paneles por cara"), ("tríptico", "hoja con dos pliegues y tres paneles por cara"), ("laminado", "cubierta de película plástica sobre el impreso"), ("troquelado", "corte con forma hecho con un molde"), ("lomo", "borde por donde se unen las hojas de un libro o cuaderno")],
    worked=[
        ("Paneles de un díptico", "Un díptico de ejemplo se imprime por las dos caras. ¿Cuántos paneles tiene en total?", ["Cada cara tiene 2 paneles.", "2 × 2 = 4."], "4 paneles"),
        ("Elegir la encuadernación", "Un folleto de ejemplo de pocas hojas se une con grapas en el lomo. ¿Qué encuadernación de la ficha es?", ["La ficha describe el corchete como grapas en el lomo.", "La rústica usa pegamento y la espiral un alambre o plástico en espiral."], "Corchete"),
    ],
    mistakes=[("Decir que laminar y barnizar son lo mismo.", "El laminado cubre con una película plástica y el barniz es una capa transparente líquida.", "Recuerda: película para el laminado, capa para el barniz."),
              ("Pensar que un tríptico tiene tres pliegues.", "Un tríptico tiene dos pliegues y tres paneles por cara.", "Cuenta los pliegues, no los paneles.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el refilado?", "El corte de los bordes del impreso para dejarlo al tamaño final", "El plegado de la hoja en tres partes", "La capa transparente de brillo", "El refilado deja el tamaño final al cortar los bordes."),
        ("abc", "En Gráfica: ¿qué es laminar un impreso?", "Cubrirlo con una película plástica", "Cortarlo con un molde", "Pegarlo en el lomo", "El laminado agrega una película plástica de protección."),
        ("abc", "En Gráfica: ¿qué es troquelar?", "Cortar una forma con un molde llamado troquel", "Doblar la hoja en dos", "Unir hojas con grapas", "El troquelado corta formas, como una estrella."),
        ("abc", "{F} ¿Cuántos paneles por cara tiene un tríptico?", "3 paneles", "2 paneles", "4 paneles", "El tríptico tiene dos pliegues y por eso tres paneles por cara."),
        ("=", "{F} Se pliegan 800 trípticos. ¿Cuántos pliegues se hacen en total?", "800*2", "Se multiplican los trípticos por los pliegues de cada uno.", " pliegues"),
        ("abc", "{F} ¿Qué encuadernación une las hojas con pegamento en el lomo?", "La rústica", "La espiral", "El corchete", "La rústica pega las hojas en el lomo."),
        ("abc", "{F} Un cliente quiere un cuaderno que se abra plano para escribir. ¿Qué encuadernación conviene?", "La espiral", "La rústica", "El corchete", "En la espiral el cuaderno se abre plano."),
        ("=", "{F} Un tríptico se imprime por las dos caras. ¿Cuántos paneles tiene en total?", "3*2", "Se multiplican los paneles por cara por las dos caras.", " paneles"),
        ("abc", "{F} Un cliente quiere tarjetas con forma de estrella. ¿Qué operación necesita?", "Troquelado", "Laminado", "Refilado", "Cortar una forma exige un molde llamado troquel."),
        ("abc", "{F} Un compañero dice: «laminar y barnizar son lo mismo». ¿Qué respondes?", "El laminado es una película plástica y el barniz es una capa transparente", "Tiene razón: son lo mismo", "El barniz es un tipo de corte", "Son terminaciones distintas con materiales y efectos distintos."),
        ("abc", "{F} ¿Cómo se llama un folleto de dos pliegues?", "Tríptico", "Díptico", "Troquelado", "Dos pliegues dan tres paneles por cara, es decir, un tríptico."),
        ("abc", "Alguien propone cortar a mano unas pocas hojas con una cuchilla suelta «para ahorrar tiempo». ¿Qué corresponde?", "Dejar el corte a las máquinas y al personal autorizado", "Hacerlo si son pocas hojas", "Hacerlo si usa regla", "Las cuchillas sueltas pueden causar cortes graves."),
        ("=", "{F} Se laminan 250 tarjetas por las dos caras. ¿Cuántas caras laminadas hay?", "250*2", "Se multiplican las tarjetas por las dos caras de cada una.", " caras"),
    ],
    ctx=("abc", "Una escuela de ejemplo pide 500 invitaciones con esquinas en forma de arco y protección contra roces. ¿Qué dos terminaciones de la ficha sugieres?", "Troquelado para las esquinas y laminado para proteger", "Espiral y corchete", "Díptico y tríptico", "El troquel da la forma y la película plástica protege el impreso."),
    sc=[
        ("En Gráfica: ¿cuántos pliegues tiene un tríptico?", "Dos", "Dos pliegues dan tres paneles por cara."),
        ("¿Qué encuadernación abre plano?", "La espiral", "Un alambre o plástico en espiral atraviesa las perforaciones."),
        ("¿Qué operación corta los bordes?", "El refilado", "Deja el impreso al tamaño final."),
    ],
    op=("Un cliente de ejemplo pide 600 folletos tipo tríptico, 40 tarjetas con forma de corazón y 100 cuadernos que se abran planos. Para cada pedido, indica la operación o encuadernación de la ficha que usarías y por qué, y calcula cuántos pliegues habrá en total en los trípticos.",
        "Trípticos: pliegues de 2 por folleto, 600 × 2 = 1.200. Tarjetas en forma de corazón: troquelado, porque corta una forma con un molde. Cuadernos que se abren planos: encuadernación en espiral, porque el alambre o plástico en espiral permite abrir plano.",
        ["asigna la operación correcta a cada pedido", "da una razón basada en la ficha", "calcula bien los pliegues"],
        ["hoja con tres elecciones, razones y el cálculo"],
        ["confundir tríptico con tres pliegues", "elegir la rústica para abrir plano", "no dar razón"],
        "Pregunta: «¿cuántos pliegues tiene un tríptico?». Si responde 3, dibuja una hoja con 3 paneles y cuenta los pliegues."),
    reinforce="Dibuja un díptico y un tríptico y marca en cada uno los pliegues y los paneles de una cara.",
    extend="Explica con un ejemplo inventado cuándo conviene laminar y cuándo barnizar.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (libros de ejemplo, inventados). Libro A: 160 páginas. Libro B: 100 páginas. Los cuadernillos tienen 16 páginas. Cada hoja tiene 2 páginas (una por cada cara). "
     "Espesor de ejemplo: 10 hojas miden 1 mm. El lomo mide lo mismo que el bloque de hojas.")
build(
    O6, 3, F,
    use="Aprenderé a calcular cuadernillos, hojas y grosor del lomo de un libro, y a decidir cómo completar los cuadernillos cuando las páginas no calzan.",
    prior=["Conozco el cuadernillo y la encuadernación.", "Sé dividir y multiplicar.", "Sé qué es el lomo."],
    explain=[
        "Un libro se arma con cuadernillos de un mismo número de páginas, por ejemplo 16. El número de cuadernillos es las páginas divididas por las de cada cuadernillo. Si el total no es múltiplo del tamaño del cuadernillo, se completan páginas en blanco hasta llegar al siguiente múltiplo, pero eso se hace con acuerdo del cliente, porque se cambia el libro.",
        "Una hoja tiene dos páginas, una por cada cara. Las hojas de un libro son las páginas divididas por 2. El grosor del bloque, y por tanto el lomo, se calcula con el espesor de las hojas: aquí, 10 hojas miden 1 mm. El lomo es un dato clave para diseñar la tapa, porque si es distinto de lo previsto, el texto del lomo no calza.",
        "Los cálculos de esta clase son de ejemplo y se hacen en papel, antes de cualquier trabajo de máquina." + MAQ,
    ],
    vocab=[("cuadernillo", "pliego plegado que forma un grupo de páginas"), ("múltiplo", "número que resulta de multiplicar otro por un número entero"), ("página en blanco", "página sin contenido que se agrega para completar un cuadernillo"), ("lomo", "grosor del bloque de hojas de un libro"), ("bloque", "conjunto de hojas del libro sin tapa")],
    worked=[
        ("Cuadernillos de un libro", "Un libro de ejemplo de 64 páginas con cuadernillos de 16. ¿Cuántos cuadernillos tiene?", ["Se dividen las páginas por las del cuadernillo.", "64 ÷ 16 = 4."], "4 cuadernillos"),
        ("Hojas de un libro", "Un libro de ejemplo de 48 páginas. ¿Cuántas hojas tiene?", ["Cada hoja tiene 2 páginas.", "48 ÷ 2 = 24."], "24 hojas"),
    ],
    mistakes=[("Cortar texto del cliente «para que calce» en los cuadernillos.", "Cambiar el contenido sin autorización altera el trabajo del cliente.", "Propone páginas en blanco o ajustes y espera la aprobación del cliente."),
              ("Diseñar la tapa con un lomo supuesto sin calcularlo.", "Un lomo distinto al real deja el texto desalineado.", "Calcula el lomo con las hojas y el espesor antes de diseñar la tapa.")],
    T=[
        ("abc", "En Gráfica: ¿qué es un cuadernillo?", "Un pliego plegado que forma un grupo de páginas", "Un tipo de tinta", "Una máquina de corte", "Los cuadernillos agrupan páginas y se encuadernan juntos."),
        ("abc", "{F} ¿Cuántas páginas tiene cada hoja?", "2 páginas", "1 página", "16 páginas", "Cada hoja tiene una página por cara."),
        ("=", "{F} ¿Cuántos cuadernillos tiene el libro A?", "160//16", "Se dividen las páginas del libro por las del cuadernillo.", " cuadernillos"),
        ("=", "{F} ¿Cuántas hojas tiene el libro A?", "160//2", "Se dividen las páginas por 2.", " hojas"),
        ("=", "{F} ¿Cuánto mide el lomo del libro A, en mm?", "(160//2)//10", "Las hojas se dividen por 10, porque 10 hojas miden 1 mm.", " mm"),
        ("abc", "{F} ¿El libro B de 100 páginas se completa exactamente con cuadernillos de 16?", "No, porque 100 no es múltiplo de 16", "Sí, porque 100 es mayor que 16", "Sí, porque 100 es par", "100 ÷ 16 no es un número entero."),
        ("=", "{F} ¿Cuántas páginas en blanco hay que agregar al libro B para completar cuadernillos de 16?", "7*16-100", "Se calcula el siguiente múltiplo de 16 y se resta el total de páginas.", " páginas"),
        ("=", "{F} Con las páginas en blanco, ¿cuántos cuadernillos tendrá el libro B?", "(7*16)//16", "Las páginas completas se dividen por las del cuadernillo.", " cuadernillos"),
        ("abc", "{F} Un compañero propone cortar 4 páginas del texto del libro B «para que calce». ¿Qué respondes?", "No se cambia el contenido sin autorización; se propone completar con páginas en blanco y se consulta al cliente", "Tiene razón: se corta lo que sobra", "Se corta y no se avisa", "El contenido es del cliente y los cambios se acuerdan."),
        ("=", "{F} ¿Cuántas hojas tiene el libro B ya completado a 112 páginas?", "112//2", "Se dividen las páginas completas por 2.", " hojas"),
        ("abc", "{F} La tapa del libro A se diseñó para un lomo de 6 mm. ¿Qué pasa?", "El lomo real es de 8 mm y el texto del lomo no calzará", "Calzará perfectamente", "El libro tendrá menos hojas", "El lomo real es mayor que el previsto, por lo que la tapa no coincide."),
        ("=", "{F} Si el libro A se hiciera con cuadernillos de 8 páginas, ¿cuántos cuadernillos tendría?", "160//8", "Se dividen las páginas por las del nuevo cuadernillo.", " cuadernillos"),
        ("abc", "{F} Un cliente pide ver cuánto crecería el lomo del libro A si se agregan 40 páginas. ¿Cuánto mediría?", "10 mm", "8 mm", "12 mm", "Con 200 páginas hay 100 hojas, que miden 10 mm."),
    ],
    ctx=("abc", "Un cliente de ejemplo te entrega un libro de 90 páginas para cuadernillos de 16 y te dice «no importa si sobran páginas, hazlo como puedas». ¿Qué haces?", "Calculo cuántas páginas en blanco se necesitan y se lo confirmo por escrito antes de seguir", "Corto el texto por mi cuenta", "Imprimo más cuadernillos de los que pide sin avisar", "Cualquier cambio a un libro se acuerda con el cliente y queda registrado."),
    sc=[
        ("En Gráfica: ¿cuántas hojas tiene un libro de 64 páginas?", "32 hojas", "Cada hoja tiene dos páginas, una por cada cara."),
        ("¿Cómo se completa un cuadernillo cuando faltan páginas?", "Con páginas en blanco acordadas con el cliente", "No se altera el contenido sin autorización."),
        ("¿Qué dato necesita la tapa de un libro?", "El lomo", "El lomo define el ancho del espacio entre portada y contraportada."),
    ],
    op=("Un libro de ejemplo tiene 70 páginas, con cuadernillos de 16 páginas. Usa el espesor de ejemplo de la ficha (10 hojas miden 1 mm). "
        "Calcula cuántas páginas en blanco hacen falta para completar cuadernillos, cuántos cuadernillos tendrá, cuántas hojas tendrá el libro completado y cuánto medirá su lomo.",
        "70 ÷ 16 no es entero; el siguiente múltiplo es 80 (5 × 16), así que hacen falta 10 páginas en blanco. Cuadernillos: 80 ÷ 16 = 5. Hojas: 80 ÷ 2 = 40. Lomo: 40 ÷ 10 = 4 mm.",
        ["calcula el siguiente múltiplo de 16", "calcula cuadernillos y hojas", "calcula el lomo con la regla de ejemplo"],
        ["hoja con los cuatro cálculos y una nota para el cliente"],
        ["no completar el cuadernillo", "contar mal las hojas", "olvidar dividir por 10"],
        "Pregunta: «¿por qué 80 y no 75?». Si no responde, recuerda que el siguiente múltiplo de 16 es 80."),
    reinforce="Elige un libro de 80 páginas y calcula cuadernillos de 16, hojas y lomo con la regla de la ficha.",
    extend="Explica por qué agregar páginas en blanco requiere avisar al cliente.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (aprovechamiento de papel y control de corte, de ejemplo). Pliego de 320 × 450 mm. Producto 1: tarjetas A5 de 148 × 210 mm; caben 2 en el ancho y 2 en el alto. Producto 2: tarjetas A6 de 105 × 148 mm; caben 3 en el ancho y 3 en el alto. "
     "Control de corte: el ancho objetivo de la tarjeta A5 es 148 mm con una tolerancia de ± 1 mm. Medidas de 4 tarjetas cortadas: 148, 149, 150 y 147 mm.")
build(
    O6, 4, F,
    use="Aprenderé a calcular cuántos productos salen de un pliego y cuánto papel sobra, y a revisar medidas de corte contra una tolerancia.",
    prior=["Conozco el refilado y la tolerancia.", "Sé multiplicar y restar.", "Sé calcular el área de un rectángulo."],
    explain=[
        "El aprovechamiento de papel indica cuánto del pliego queda convertido en producto. El área de un rectángulo es el largo por el ancho, en milímetros cuadrados (mm²). Si de un pliego salen varios productos, el área usada es el área de un producto por la cantidad. El sobrante es el área del pliego menos el área usada, y esos recortes se separan para reciclaje.",
        "La cantidad de productos por pliego se calcula contando cuántos caben en el ancho y cuántos en el alto, y multiplicando ambos números. Elegir bien cómo disponer los productos reduce el sobrante y el costo.",
        "El control de corte compara la medida de cada pieza con la medida objetivo y la tolerancia. Una pieza fuera de tolerancia se separa, se registra y se avisa a la persona responsable. Estos cálculos se hacen en papel, sin operar ninguna máquina." + MAQ,
    ],
    vocab=[("aprovechamiento", "parte del pliego que queda convertida en producto"), ("área", "medida de la superficie: largo por ancho"), ("sobrante", "papel que queda sin usar después de cortar"), ("tolerancia", "diferencia máxima aceptada"), ("medida objetivo", "medida que debería tener la pieza")],
    worked=[
        ("Productos por pliego", "En un pliego de ejemplo caben 3 tarjetas a lo ancho y 4 a lo alto. ¿Cuántas salen?", ["Se multiplican las que caben en el ancho por las del alto.", "3 × 4 = 12."], "12 tarjetas"),
        ("Medida dentro de tolerancia", "Una pieza de ejemplo debe medir 100 mm con tolerancia de ± 2 mm y mide 102 mm. ¿Cumple?", ["La diferencia es 2 mm.", "2 es igual a la tolerancia."], "Sí, cumple"),
    ],
    mistakes=[("Contar los productos por pliego dividiendo el área del pliego por el área del producto.", "Los productos no se pueden partir: hay que contar cuántos caben enteros en cada lado.", "Cuenta cuántos caben a lo ancho y a lo alto y multiplica."),
              ("Aceptar una pieza que mide 150 mm cuando el objetivo es 148 ± 1 «porque es casi igual».", "La tolerancia se cumple o no se cumple.", "Compara la diferencia con la tolerancia y registra.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el sobrante de un pliego?", "El papel que queda sin usar después de cortar", "El papel que se vende", "La tinta restante", "El sobrante es la diferencia entre el pliego y lo usado."),
        ("abc", "{F} ¿Cuántas tarjetas A5 caben en un pliego?", "4", "9", "2", "Caben 2 en el ancho y 2 en el alto, es decir, 4."),
        ("=", "{F} ¿Cuántas tarjetas A6 caben en un pliego?", "3*3", "Se multiplican las que caben en el ancho por las que caben en el alto.", " tarjetas"),
        ("=", "{F} ¿Cuántas tarjetas A6 más que A5 salen de cada pliego?", "9-4", "Se restan las tarjetas A5 a las tarjetas A6.", " tarjetas"),
        ("=", "{F} ¿Cuál es el área del pliego, en mm²?", "320*450", "El área es el largo por el ancho.", " mm²"),
        ("=", "{F} ¿Cuál es el área usada por las tarjetas A5 de un pliego?", "4*148*210", "Se multiplica la cantidad de tarjetas por el área de cada una.", " mm²"),
        ("=", "{F} ¿Cuántos mm² sobran por pliego al cortar tarjetas A5?", "320*450-4*148*210", "Al área del pliego se le resta el área usada.", " mm²"),
        ("=", "{F} ¿Cuántos mm² sobran por pliego al cortar tarjetas A6?", "320*450-9*105*148", "Al área del pliego se le resta el área usada por las nueve tarjetas.", " mm²"),
        ("abc", "{F} ¿Qué formato aprovecha mejor el pliego de la ficha?", "El A6, porque deja menos sobrante", "El A5, porque es más grande", "Ninguno, porque dejan igual sobrante", "El sobrante del A6 es menor que el del A5."),
        ("abc", "{F} Un compañero dice: «mientras más tarjetas por pliego, siempre se aprovecha mejor». ¿Qué respondes?", "Hay que comparar el sobrante de cada disposición, no solo la cantidad", "Tiene razón: solo importa la cantidad", "El sobrante no cuenta nunca", "Una disposición con más tarjetas puede dejar más o menos sobrante; se compara con el área."),
        ("=", "{F} ¿Cuántas de las 4 medidas cumplen la tolerancia de ± 1 mm?", "4-1", "Solo la de 150 mm difiere en 2 mm del objetivo; las otras difieren 0, 1 y 1.", " medidas"),
        ("abc", "{F} ¿Qué corresponde con la tarjeta de 150 mm?", "Separarla, registrar la medida y avisar a la persona responsable", "Aceptarla porque es casi igual", "Cambiar el valor medido a 149", "Una pieza fuera de tolerancia se separa y se informa."),
        ("=", "{F} Se necesitan 2.000 tarjetas A6. ¿Cuántos pliegos completos hacen falta?", "(2000+8)//9", "Se divide por las tarjetas de cada pliego y se redondea hacia arriba.", " pliegos"),
    ],
    ctx=("abc", "El cliente de ejemplo dice que quiere 1.000 tarjetas A5 y pregunta cuántos pliegos de 320 × 450 mm se necesitan con la disposición de la ficha. ¿Qué respondes?", "250 pliegos completos, porque salen 4 tarjetas por pliego", "100 pliegos, porque salen 10 por pliego", "1.000 pliegos, porque sale una por pliego", "Con 4 tarjetas por pliego se necesitan 1.000 ÷ 4 = 250 pliegos."),
    sc=[
        ("En Gráfica: ¿cómo se calcula cuántos productos caben en un pliego?", "Multiplicando los que caben a lo ancho por los que caben a lo alto", "Los productos deben caber enteros en cada lado."),
        ("¿Cómo se calcula el área de un rectángulo?", "Largo por ancho", "El área mide la superficie de la pieza."),
        ("En el control de calidad de una imprenta, ¿qué haces con un pliego fuera de tolerancia?", "La separo y registro", "Una pieza fuera de tolerancia no se aprueba."),
    ],
    op=("Un pliego de ejemplo mide 320 × 450 mm. Se quieren cortar tarjetas de 100 × 150 mm. Calcula cuántas caben a lo ancho, cuántas a lo alto, cuántas salen por pliego y cuántos mm² sobran. Luego revisa estas medidas de ancho (objetivo 100 mm, tolerancia ± 1 mm): 100, 101, 102. Indica cuántas están fuera.",
        "A lo ancho: 3 (3 × 100 = 300 ≤ 320). A lo alto: 3 (3 × 150 = 450 ≤ 450). Por pliego: 9. Área usada: 9 × 100 × 150 = 135.000. Área del pliego: 320 × 450 = 144.000. Sobran 9.000 mm². Medidas: 102 está fuera (diferencia 2 mm).",
        ["calcula productos por pliego", "calcula el sobrante", "revisa las medidas contra la tolerancia"],
        ["hoja con los cálculos y el control de medidas"],
        ["dividir áreas para contar tarjetas", "olvidar el sobrante", "aceptar 102 mm"],
        "Pregunta: «¿por qué caben 3 a lo alto si 3 × 150 es justo 450?». Si dice que no cabe, aclara que cabe cuando es menor o igual."),
    reinforce="Dibuja un rectángulo de 12 × 8 cuadritos y reparte tarjetas de 4 × 4; cuenta cuántas caben y cuántos cuadritos sobran.",
    extend="Explica por qué un cliente puede ahorrar dinero al elegir un formato que aproveche mejor el pliego.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (taller de ejemplo, inventado). Equipos: un computador de preimpresión, una impresora digital, una prensa offset y una guillotina. Mantenimiento básico: limpieza, lubricación (poner aceite o grasa en las piezas que lo requieren) y reemplazo de fungibles "
     "(piezas o insumos que se gastan con el uso, como filtros o cuchillas), siempre según el manual del fabricante. Reglas de ejemplo: solo personal autorizado interviene un equipo; antes de intervenirlo se aplica el bloqueo y etiquetado "
     "(método para asegurar que el equipo no pueda partir mientras alguien trabaja en él), según la norma vigente; toda intervención se anota en la bitácora; los aceites, solventes y trapos con restos van a contenedores rotulados.")
build(
    O7, 1, F,
    use="Aprenderé qué es el mantenimiento básico de equipos gráficos, quién puede hacerlo, qué normas lo rodean y por qué se registra, sin hacer ninguna intervención.",
    prior=["Conozco los resguardos y las normas de seguridad del taller.", "Sé leer un manual o una ficha.", "Sé multiplicar y sumar."],
    explain=[
        "El mantenimiento básico reúne las tareas que mantienen un equipo en buen estado: limpieza, lubricación (poner aceite o grasa donde el fabricante lo indica) y reemplazo de fungibles, que son piezas o insumos que se gastan con el uso, como filtros o cuchillas. Se aplica a equipos de preimpresión, impresión y postimpresión, y siempre se hace según el manual del fabricante.",
        "Intervenir un equipo es un riesgo: puede partir inesperadamente, tener partes en movimiento, corriente eléctrica o productos químicos. Por eso solo lo hace personal autorizado y se usa el bloqueo y etiquetado, un método para asegurar que el equipo no pueda partir mientras alguien trabaja en él, según la norma vigente. Toda intervención se anota en la bitácora, que es el registro cronológico del mantenimiento.",
        "Los aceites, solventes y trapos con restos se guardan en contenedores rotulados; no se vierten al desagüe. Este cuaderno solo enseña conceptos y no habilita para intervenir equipos." + MAQ,
    ],
    vocab=[("mantenimiento básico", "limpieza, lubricación y reemplazo de fungibles según el manual"), ("fungible", "pieza o insumo que se gasta con el uso"), ("lubricación", "poner aceite o grasa en las piezas que lo requieren"), ("bloqueo y etiquetado", "método para asegurar que un equipo no parta mientras se interviene"), ("bitácora", "registro cronológico de las intervenciones"), ("autorizado", "persona que la empresa habilitó para intervenir un equipo")],
    worked=[
        ("Limpiezas al mes", "Un taller de ejemplo tiene 3 equipos y limpia cada uno 2 veces al mes. ¿Cuántas limpiezas hay al mes?", ["Se multiplican los equipos por las limpiezas de cada uno.", "3 × 2 = 6."], "6 limpiezas"),
        ("Qué documento consultar", "Quieres saber qué lubricante usa una máquina de ejemplo. ¿Qué documento consultas?", ["El fabricante indica los lubricantes adecuados.", "Está en el manual del fabricante."], "El manual del fabricante"),
    ],
    mistakes=[("Intervenir un equipo «un momento» sin bloqueo y etiquetado porque la tarea es corta.", "Una tarea corta puede ser peligrosa si el equipo parte mientras alguien trabaja en él.", "Solo personal autorizado interviene, con el bloqueo y etiquetado de la norma vigente."),
              ("No anotar una limpieza porque «ya es de rutina».", "Sin registro no se sabe cuándo se hizo ni quién la hizo.", "Anota cada intervención en la bitácora con fecha y responsable.")],
    T=[
        ("abc", "En Gráfica: ¿qué es un fungible?", "Una pieza o insumo que se gasta con el uso, como un filtro o una cuchilla", "Una máquina completa", "Un tipo de tinta", "Los fungibles se reemplazan cuando se desgastan."),
        ("abc", "En Gráfica: ¿para qué sirve el bloqueo y etiquetado?", "Para asegurar que el equipo no parta mientras alguien trabaja en él", "Para etiquetar los precios de los repuestos", "Para pintar las máquinas", "Es una medida de seguridad que evita arranques inesperados."),
        ("abc", "{F} ¿Dónde se anotan las intervenciones de mantenimiento?", "En la bitácora", "En la factura de la tinta", "En el plano de planta", "La bitácora es el registro cronológico del mantenimiento."),
        ("=", "{F} Cada uno de los 4 equipos se limpia 2 veces al mes. ¿Cuántas limpiezas hay al mes en el taller?", "4*2", "Se multiplican los equipos por las limpiezas de cada uno.", " limpiezas"),
        ("abc", "{F} ¿Quién puede intervenir un equipo según las reglas del taller?", "Solo personal autorizado", "Cualquier ayudante del turno", "Quien lleve más años en el taller", "La regla de ejemplo limita las intervenciones a personal autorizado."),
        ("abc", "¿Qué documento manda cómo hacer una lubricación?", "El manual del fabricante", "La costumbre del taller", "El catálogo de papel", "El fabricante conoce su equipo y fija cómo mantenerlo."),
        ("=", "{F} Con 8 limpiezas al mes en total, ¿cuántas limpiezas hay en 6 meses?", "8*6", "Se multiplican las limpiezas mensuales por los meses.", " limpiezas"),
        ("abc", "Un ayudante quiere lubricar una pieza que «se oye seca» mientras el equipo está funcionando. ¿Qué corresponde?", "No hacerlo y avisar a personal autorizado, que interviene con bloqueo y etiquetado", "Hacerlo rápido con cuidado", "Hacerlo si el equipo va lento", "Intervenir un equipo en marcha es un riesgo grave."),
        ("abc", "{F} ¿Dónde se guardan los trapos con restos de aceite o solvente?", "En contenedores rotulados", "En la basura común", "En el desagüe", "Son residuos que se manejan según la norma vigente."),
        ("abc", "{F} Un compañero dice: «el bloqueo y etiquetado es una pérdida de tiempo en tareas cortas». ¿Qué respondes?", "Es una medida de seguridad que evita arranques inesperados, incluso en tareas cortas", "Tiene razón: solo sirve para tareas largas", "Solo se usa si hay inspección", "Un arranque inesperado puede causar lesiones graves aunque la tarea sea corta."),
        ("abc", "Una persona de ejemplo ve que nadie anotó la última limpieza de una máquina. ¿Qué riesgo produce?", "No se sabe cuándo se hizo y se puede repetir o saltar la siguiente", "Ninguno, porque se hizo", "La máquina ya no necesita limpieza", "Sin registro se pierde el control del plan de mantenimiento."),
        ("abc", "{F} Un estudiante en visita pregunta si puede cambiar una cuchilla «solo para aprender». ¿Qué respondes?", "No: este aprendizaje es conceptual y la intervención exige personal autorizado e instructor", "Sí, si usa guantes", "Sí, si hay poco ruido", "Practicar una intervención exige instructor autorizado, norma vigente y elementos de protección."),
        ("=", "{F} El taller anota cada intervención en la bitácora. Si ocurrieron 12 limpiezas y 3 lubricaciones en un mes, ¿cuántas anotaciones hay?", "12+3", "Se suman las intervenciones de cada tipo.", " anotaciones"),
    ],
    ctx=("abc", "El jefe de turno de ejemplo no está y una máquina hace un ruido raro. Un compañero propone abrir una tapa y mirar adentro. ¿Qué haces?", "Detengo la máquina de forma segura si estoy autorizado, no abro nada y aviso a personal autorizado", "Abro la tapa para mirar", "Sigo trabajando para no perder tiempo", "Ante un ruido anormal se detiene y se avisa; la revisión la hace personal autorizado con bloqueo."),
    sc=[
        ("En Gráfica: ¿qué tareas forman el mantenimiento básico?", "Limpieza, lubricación y reemplazo de fungibles", "Son las tareas básicas que menciona la ficha."),
        ("¿Qué se anota en la bitácora?", "Cada intervención, con fecha y responsable", "El registro permite controlar el plan de mantenimiento."),
        ("¿Quién interviene un equipo?", "Solo personal autorizado", "La intervención tiene riesgos y exige capacitación."),
    ],
    op=("Un taller de ejemplo tiene 5 equipos y limpia cada uno 3 veces al mes. Calcula cuántas limpiezas hay al mes y cuántas en 4 meses. "
        "Escribe también tres reglas de seguridad o de registro que cumplirías en el mantenimiento (por ejemplo sobre bloqueo y etiquetado, bitácora y residuos), con una razón cada una.",
        "Al mes: 5 × 3 = 15 limpiezas. En 4 meses: 15 × 4 = 60. Reglas: solo personal autorizado interviene, porque hay riesgo de arranques y partes en movimiento; se anota cada intervención en la bitácora, porque sin registro se pierde el control; los trapos con aceite van a contenedores rotulados, porque son residuos.",
        ["calcula bien las limpiezas", "escribe tres reglas con razón", "no describe cómo intervenir un equipo"],
        ["hoja con los cálculos y las tres reglas"],
        ["escribir pasos de una intervención", "olvidar el registro", "no dar razones"],
        "Pregunta: «¿para qué sirve la bitácora?». Si responde 'para tener papeles', recuerda el control de las fechas del plan."),
    reinforce="Haz una lista de cuatro fungibles de un taller gráfico (de ejemplo) y para cada uno escribe qué documento consultarías.",
    extend="Explica por qué las intervenciones las hace personal autorizado aunque la tarea parezca simple.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (plan de mantenimiento de ejemplo, inventado, para una máquina). Limpieza general: cada 40 horas de uso. Lubricación: cada 200 horas de uso. Reemplazo de filtro: cada 500 horas de uso. Reemplazo de cuchilla: cada 1.000 horas de uso. "
     "Mantenimiento preventivo: tareas programadas antes de que ocurra una falla. Mantenimiento correctivo: reparación después de una falla. Vida útil: horas de uso que dura una pieza antes de desgastarse. Las horas de uso se registran en la bitácora.")
build(
    O7, 2, F,
    use="Aprenderé la diferencia entre mantenimiento preventivo y correctivo, a leer un plan con intervalos de horas y a calcular cuándo corresponde cada tarea.",
    prior=["Conozco el mantenimiento básico y la bitácora.", "Sé sumar, multiplicar y dividir.", "Sé qué es un fungible."],
    explain=[
        "El mantenimiento preventivo son las tareas programadas antes de que ocurra una falla; el correctivo es la reparación que se hace después de una falla. El preventivo busca evitar paradas inesperadas y suele costar menos. Un plan de mantenimiento fija cada tarea con un intervalo de horas de uso, que se mide con el contador de horas del equipo y se anota en la bitácora.",
        "La próxima fecha de una tarea se calcula sumando el intervalo a las horas de uso de la última vez que se hizo. La vida útil de una pieza es el número de horas que dura antes de desgastarse; el fungible se reemplaza antes de llegar al final de su vida útil, según el manual del fabricante. Si se cumple todo el plan, hay menos fallas, pero igual se revisa la bitácora.",
        "Los intervalos de esta ficha son de ejemplo; los reales los fija el manual del fabricante." + MAQ,
    ],
    vocab=[("mantenimiento preventivo", "tareas programadas antes de que ocurra una falla"), ("mantenimiento correctivo", "reparación hecha después de una falla"), ("intervalo", "horas de uso entre una tarea y la siguiente"), ("vida útil", "horas que dura una pieza antes de desgastarse"), ("plan de mantenimiento", "lista de tareas con sus intervalos")],
    worked=[
        ("Próxima tarea", "Una tarea de ejemplo se hizo a las 300 horas y se repite cada 100 horas. ¿A qué hora corresponde la siguiente?", ["Se suma el intervalo a la hora de la última vez.", "300 + 100 = 400."], "A las 400 horas"),
        ("Preventivo o correctivo", "Una máquina de ejemplo se detiene porque se rompió una correa y se repara. ¿Qué tipo de mantenimiento es?", ["La reparación ocurre después de la falla.", "Eso es mantenimiento correctivo."], "Correctivo"),
    ],
    mistakes=[("Esperar a que algo falle para recién mantenerlo.", "Eso es mantenimiento correctivo, que suele costar más y detener el trabajo.", "Sigue el plan preventivo."),
              ("Calcular la próxima tarea desde la fecha de hoy en vez de desde la última vez que se hizo.", "El intervalo se cuenta desde la última intervención anotada en la bitácora.", "Suma el intervalo a las horas de la última vez.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el mantenimiento preventivo?", "Tareas programadas antes de que ocurra una falla", "Reparar después de una falla", "Comprar equipos nuevos", "Lo preventivo busca evitar la falla."),
        ("abc", "En Gráfica: ¿qué es el mantenimiento correctivo?", "La reparación que se hace después de una falla", "Las tareas programadas con anticipación", "El cambio de turno", "Lo correctivo corrige un problema que ya ocurrió."),
        ("abc", "{F} ¿Cada cuántas horas de uso se hace la limpieza general?", "Cada 40 horas", "Cada 200 horas", "Cada 1.000 horas", "La ficha fija la limpieza general cada 40 horas."),
        ("abc", "{F} ¿Qué tarea tiene el intervalo más largo?", "El reemplazo de cuchilla, cada 1.000 horas", "La limpieza general, cada 40 horas", "La lubricación, cada 200 horas", "El mayor intervalo es el de la cuchilla."),
        ("=", "{F} La última limpieza general fue a las 120 horas de uso. ¿A qué hora corresponde la siguiente?", "120+40", "Se suma el intervalo a la hora de la última vez.", " horas"),
        ("=", "{F} La última lubricación fue a las 400 horas. ¿A qué hora corresponde la siguiente?", "400+200", "Se suma el intervalo a la hora de la última lubricación.", " horas"),
        ("=", "{F} En 1.000 horas de uso, ¿cuántas limpiezas generales corresponden?", "1000//40", "Se divide el período por el intervalo.", " limpiezas"),
        ("=", "{F} En 1.000 horas de uso, ¿cuántas lubricaciones corresponden?", "1000//200", "Se divide el período por el intervalo.", " lubricaciones"),
        ("=", "{F} En 1.000 horas de uso, ¿cuántas tareas en total corresponden entre limpiezas, lubricaciones, reemplazos de filtro y de cuchilla?", "1000//40+1000//200+1000//500+1000//1000", "Se suman las veces que corresponde cada tarea en ese período.", " tareas"),
        ("abc", "{F} Una máquina se detiene por una falla y se repara. ¿Qué tipo de mantenimiento es?", "Correctivo", "Preventivo", "Ninguno", "La reparación posterior a una falla es correctiva."),
        ("abc", "{F} Un compañero dice: «mejor esperar a que falle para gastar solo cuando haga falta». ¿Qué respondes?", "Lo correctivo suele detener el trabajo de golpe y costar más que lo preventivo", "Tiene razón: lo correctivo siempre es más barato", "Las máquinas no fallan nunca", "Esperar a la falla provoca paradas inesperadas y costos mayores."),
        ("abc", "{F} Si la lubricación se hizo a las 600 horas, un compañero calcula la siguiente a las 700. ¿Cuál es el error?", "Sumó 100 horas en vez de las 200 horas del intervalo", "Ninguno", "Debió restar el intervalo", "El intervalo de lubricación es de 200 horas, así que corresponde a las 800."),
        ("=", "{F} Una cuchilla se reemplazó a las 750 horas. ¿A qué hora corresponde el siguiente reemplazo?", "750+1000", "Se suma el intervalo a la hora del último reemplazo.", " horas"),
    ],
    ctx=("abc", "El plan de ejemplo dice limpieza cada 40 horas y la bitácora muestra que la última fue a las 80 horas, con la máquina ya en 130 horas. ¿Qué haces?", "Aviso que la limpieza venció a las 120 horas y propongo programarla, dejando constancia", "Espero a que llegue a 200 horas", "Anoto que se hizo a las 130 sin hacerla", "Se detecta el atraso con la bitácora, se avisa y se programa; no se falsea el registro."),
    sc=[
        ("En Gráfica: ¿qué es el mantenimiento preventivo?", "Tareas programadas antes de la falla", "Busca evitar paradas inesperadas del equipo antes de que ocurra la falla."),
        ("¿Cómo se calcula la próxima tarea?", "Sumando el intervalo a las horas de la última vez", "El intervalo se cuenta desde la última intervención."),
        ("¿Qué documento fija los intervalos reales?", "El manual del fabricante", "Los valores de esta ficha son de ejemplo."),
    ],
    op=("Plan de ejemplo: limpieza cada 50 horas; lubricación cada 250 horas; filtro cada 500 horas. La máquina tiene 1.000 horas de uso. Calcula cuántas veces corresponde cada tarea en 1.000 horas, el total de tareas, y a qué hora corresponde el próximo filtro si el último se cambió a las 700 horas. "
        "Escribe además una razón para preferir lo preventivo a lo correctivo.",
        "Limpiezas: 1.000 ÷ 50 = 20. Lubricaciones: 1.000 ÷ 250 = 4. Filtros: 1.000 ÷ 500 = 2. Total: 26 tareas. Próximo filtro: 700 + 500 = 1.200 horas. Razón: lo preventivo evita paradas inesperadas y costos mayores.",
        ["calcula las tres cantidades y el total", "calcula la hora del próximo filtro", "da una razón para lo preventivo"],
        ["hoja con los cálculos y la razón"],
        ["sumar mal el total", "calcular el filtro desde hoy en vez de desde la última vez", "no dar razón"],
        "Pregunta: «¿desde cuándo se cuenta el intervalo?». Si responde 'desde cero', recuerda que se cuenta desde la última vez anotada."),
    reinforce="Inventa un plan con tres tareas y sus intervalos, y calcula cuántas veces se hacen cada una en 600 horas.",
    extend="Explica por qué un registro de horas en la bitácora es la base del mantenimiento preventivo.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (equipo y bitácora de ejemplo, inventados). La máquina tiene 1.250 horas de uso. Plan: limpieza cada 40 horas; lubricación cada 200 horas; filtro cada 500 horas; cuchilla cada 1.000 horas. "
     "Bitácora, última vez que se hizo cada tarea: limpieza a las 1.230 horas; lubricación a las 1.000 horas; filtro a las 800 horas; cuchilla a las 400 horas. Una tarea está vencida si las horas desde la última vez superan el intervalo.")
build(
    O7, 3, F,
    use="Aprenderé a leer una bitácora, detectar qué tareas del plan están vencidas y proponer qué se programa, sin hacer ninguna intervención.",
    prior=["Conozco el mantenimiento preventivo y los intervalos.", "Sé restar y comparar números.", "Sé leer una tabla."],
    explain=[
        "Para saber si una tarea está al día se calcula cuántas horas pasaron desde la última vez que se hizo: horas de uso actuales menos las horas anotadas en la bitácora. Si el resultado supera el intervalo del plan, la tarea está vencida; si es igual o menor, está al día. La próxima fecha se obtiene sumando el intervalo a la hora de la última vez.",
        "Una tarea vencida se informa a la persona responsable y se programa; no se hace por cuenta propia ni con el equipo en marcha. La bitácora debe reflejar lo que realmente ocurrió: anotar una tarea que no se hizo es una falta grave.",
        "Los datos de esta ficha son de ejemplo y el análisis se hace en papel." + MAQ,
    ],
    vocab=[("vencida", "tarea cuyo intervalo ya se superó"), ("al día", "tarea que no ha superado su intervalo"), ("horas desde la última vez", "horas de uso actuales menos las horas anotadas"), ("programar", "fijar cuándo se hará una tarea y quién la hará")],
    worked=[
        ("Horas desde la última vez", "Una máquina de ejemplo tiene 900 horas de uso y la última limpieza fue a las 880. ¿Cuántas horas pasaron?", ["Se restan las horas de la última vez a las actuales.", "900 − 880 = 20."], "20 horas"),
        ("Tarea vencida", "Una tarea de ejemplo tiene un intervalo de 100 horas y pasaron 130. ¿Está vencida?", ["Se compara 130 con 100.", "130 supera el intervalo."], "Sí, está vencida"),
    ],
    mistakes=[("Anotar en la bitácora una tarea que no se hizo «para ponerse al día».", "Falsear un registro quita confianza y puede causar fallas o accidentes.", "Anota solo lo realizado y avisa de lo vencido."),
              ("Calcular las horas desde el inicio de la máquina y no desde la última vez.", "Lo que importa es el tiempo transcurrido desde la última intervención.", "Resta las horas de la bitácora a las horas actuales.")],
    T=[
        ("abc", "En Gráfica: ¿cuándo está vencida una tarea de mantenimiento?", "Cuando las horas desde la última vez superan el intervalo del plan", "Cuando tiene muchas horas de uso", "Cuando se hizo hace poco", "Una tarea vencida pasó su intervalo sin hacerse."),
        ("abc", "{F} ¿A cuántas horas de uso está la máquina?", "A 1.250 horas", "A 1.230 horas", "A 1.000 horas", "La ficha indica 1.250 horas de uso."),
        ("=", "{F} ¿Cuántas horas pasaron desde la última limpieza?", "1250-1230", "Se restan las horas de la última limpieza a las horas actuales.", " horas"),
        ("=", "{F} ¿Cuántas horas pasaron desde la última lubricación?", "1250-1000", "Se restan las horas de la última lubricación a las actuales.", " horas"),
        ("abc", "{F} ¿Está vencida la limpieza?", "No: pasaron 20 horas y el intervalo es de 40", "Sí: pasaron 20 horas", "Sí: pasaron 40 horas", "20 horas no superan el intervalo de 40."),
        ("abc", "{F} ¿Está vencida la lubricación?", "Sí: pasaron 250 horas y el intervalo es de 200", "No: pasaron 250 horas", "No: el intervalo es de 250", "250 horas superan el intervalo de 200."),
        ("=", "{F} ¿Cuántas horas pasaron desde el último reemplazo del filtro?", "1250-800", "Se restan las horas del último cambio a las actuales.", " horas"),
        ("abc", "{F} ¿Está vencido el reemplazo del filtro?", "No: pasaron 450 horas y el intervalo es de 500", "Sí: pasaron 450 horas", "Sí: el intervalo es de 450", "450 horas no superan el intervalo de 500."),
        ("=", "{F} ¿A qué hora corresponde el próximo reemplazo del filtro?", "800+500", "Se suma el intervalo a la hora del último reemplazo.", " horas"),
        ("abc", "{F} ¿Está vencido el reemplazo de la cuchilla?", "No: pasaron 850 horas y el intervalo es de 1.000", "Sí: pasaron 850 horas", "Sí: ya llegó a 1.000", "850 horas no superan el intervalo de 1.000 horas."),
        ("abc", "{F} Un compañero dice: «anotemos que la lubricación se hizo hoy, así el plan queda al día». ¿Qué respondes?", "No: la bitácora debe reflejar lo realizado; hay que informar y programar la lubricación", "Tiene razón, queda ordenado", "Anótalo, pero con lápiz", "Falsear la bitácora quita confianza y puede causar fallas."),
        ("abc", "{F} ¿Qué tarea debe informarse como vencida?", "La lubricación", "La limpieza", "El reemplazo del filtro", "Solo la lubricación superó su intervalo."),
        ("=", "{F} ¿A qué hora de uso corresponde la próxima limpieza?", "1230+40", "Se suma el intervalo a la hora de la última limpieza.", " horas"),
    ],
    ctx=("abc", "Una inspección de ejemplo llega mañana y la bitácora muestra la lubricación vencida. Un compañero sugiere cambiar la fecha anotada. ¿Qué haces?", "Informo que está vencida y propongo programarla, sin alterar el registro", "Cambio la fecha para evitar un problema", "Pido que se esconda la bitácora", "La bitácora debe ser veraz; lo correcto es informar y programar."),
    sc=[
        ("En Gráfica: ¿cómo se calculan las horas desde la última vez?", "Restando las horas anotadas a las horas actuales", "Mide el tiempo transcurrido desde la última intervención."),
        ("¿Qué haces con una tarea vencida?", "La informo y la programo", "La intervención la hace personal autorizado."),
        ("¿Se puede anotar una tarea que no se hizo?", "No", "El registro debe reflejar lo realizado."),
    ],
    op=("Bitácora de ejemplo: la máquina tiene 2.100 horas de uso. Plan: limpieza cada 50 horas; lubricación cada 300 horas; filtro cada 600 horas. Última vez: limpieza a las 2.070; lubricación a las 1.700; filtro a las 1.600. "
        "Calcula las horas desde la última vez de cada tarea, indica cuáles están vencidas y escribe qué harías y qué anotarías en la bitácora.",
        "Limpieza: 30 horas, al día. Lubricación: 400 horas, supera 300, vencida. Filtro: 500 horas, no supera 600, al día. Acción: informar la lubricación vencida a la persona responsable y programarla, sin anotar que se hizo; en la bitácora anotaría la revisión del plan y el aviso.",
        ["calcula las tres diferencias", "identifica la tarea vencida", "propone informar y programar sin alterar el registro"],
        ["tabla con horas, intervalo y estado, más la acción"],
        ["calcular desde cero", "declarar vencida una tarea al día", "proponer alterar la bitácora"],
        "Pregunta: «¿por qué el filtro está al día si pasaron 500 horas?». Si responde que no, repasa que el intervalo es de 600."),
    reinforce="Inventa una bitácora de cuatro tareas con horas y calcula cuáles están vencidas con un plan que fijes.",
    extend="Explica por qué una bitácora falsa puede ser más peligrosa que una tarea atrasada.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (costos de ejemplo, inventados). Filtro de una máquina: $15.000 cada uno, se reemplaza cada 500 horas de uso. Si el filtro no se reemplaza y la máquina falla, la reparación cuesta $600.000 y el taller queda 3 días parado; cada día parado cuesta $200.000. "
     "Stock de filtros en bodega: 2. El mantenimiento está previsto por 2.000 horas de uso.")
build(
    O7, 4, F,
    use="Aprenderé a comparar el costo del mantenimiento preventivo con el de una falla y a planificar los repuestos que se necesitan, con datos y registro.",
    prior=["Conozco el plan y la bitácora.", "Sé calcular costos con multiplicaciones.", "Sé calcular cuántas veces cabe un intervalo en un período."],
    explain=[
        "Comparar el costo del mantenimiento preventivo con el de una falla ayuda a decidir con datos. El costo preventivo es el de los repuestos que se cambian según el plan. El costo de una falla es la reparación más lo que se pierde por el taller parado: los días parados por el costo de cada día.",
        "Para planificar repuestos se calcula cuántos se necesitan en el período y se compara con el stock: lo que falta se compra con anticipación para no detener el trabajo. El número de repuestos que se necesitan es el período dividido por el intervalo de reemplazo.",
        "Los costos son de ejemplo. En la realidad, la decisión la toma la persona responsable con el manual del fabricante y la norma vigente." + MAQ,
    ],
    vocab=[("costo preventivo", "costo de los repuestos y tareas programadas del plan"), ("costo de una falla", "reparación más lo que se pierde por el taller parado"), ("stock", "cantidad de repuestos que ya hay en bodega"), ("período", "tiempo o cantidad de horas que se planifica")],
    worked=[
        ("Repuestos necesarios", "Un repuesto de ejemplo se cambia cada 400 horas. ¿Cuántos se necesitan en 1.200 horas?", ["Se divide el período por el intervalo.", "1.200 ÷ 400 = 3."], "3 repuestos"),
        ("Costo de parada", "Un taller de ejemplo queda parado 2 días y cada día cuesta $100.000. ¿Cuánto cuesta la parada?", ["Se multiplican los días por el costo de cada uno.", "2 × 100.000 = 200.000."], "$200.000"),
    ],
    mistakes=[("Elegir no cambiar el repuesto «para ahorrar» sin sumar el costo de una falla.", "El ahorro de corto plazo puede ser mucho menor que el costo de una parada.", "Compara ambos costos con datos."),
              ("Planificar los repuestos sin mirar el stock.", "Se puede comprar de más o quedarse sin repuestos.", "Resta el stock a lo que se necesita.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el costo de una falla?", "La reparación más lo que se pierde por el taller parado", "Solo el precio del repuesto", "Solo el costo de la reparación, sin contar los días parados", "La falla cuesta reparar y también detener el trabajo."),
        ("abc", "{F} ¿Cada cuántas horas se reemplaza el filtro?", "Cada 500 horas", "Cada 50 horas", "Cada 1.000 horas", "La ficha fija 500 horas de intervalo."),
        ("=", "{F} ¿Cuántos filtros se necesitan en las 2.000 horas previstas?", "2000//500", "Se divide el período por el intervalo.", " filtros"),
        ("=", "{F} ¿Cuánto cuestan los filtros del período?", "2000//500*15000", "Se multiplican los filtros necesarios por su precio.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los 3 días de parada si el filtro falla?", "3*200000", "Se multiplican los días por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta en total una falla, sumando reparación y parada?", "600000+3*200000", "Se suman la reparación y el costo de la parada.", " pesos"),
        ("=", "{F} ¿Cuántos filtros faltan comprar para el período, considerando el stock?", "2000//500-2", "Al total necesario se le resta el stock.", " filtros"),
        ("=", "{F} ¿Cuántas veces es mayor el costo de una falla que el de todos los filtros del período?", "(600000+3*200000)//(2000//500*15000)", "Se divide el costo de la falla por el costo de los filtros.", " veces"),
        ("abc", "{F} ¿Qué conviene según los costos de la ficha?", "Seguir el plan, porque los filtros cuestan mucho menos que una falla", "No cambiar los filtros para ahorrar", "Esperar la falla", "Los filtros del período cuestan 60.000 y una falla 1.200.000."),
        ("abc", "{F} Un compañero dice: «cambiar el filtro no vale la pena, $15.000 es mucho». ¿Qué respondes?", "Una falla cuesta 1.200.000, así que el cambio preventivo es mucho más barato", "Tiene razón: $15.000 es mucho", "La falla nunca ocurre", "Comparar costos muestra que el filtro es un gasto pequeño frente al riesgo."),
        ("abc", "{F} El stock es de 2 filtros y se necesitan 4. ¿Qué corresponde?", "Comprar los 2 que faltan con anticipación", "Esperar a que se acaben", "Usar un filtro vencido", "Se compra con tiempo para no detener el trabajo."),
        ("=", "{F} Si se prevén 3.000 horas en vez de 2.000, ¿cuántos filtros se necesitarían?", "3000//500", "Se divide el nuevo período por el intervalo.", " filtros"),
        ("abc", "El jefe pide ahorrar y propone alargar el intervalo del filtro sin consultar el manual. ¿Qué haces?", "Explico que el intervalo lo fija el fabricante y propongo consultarlo antes de cambiarlo", "Lo alargo sin avisar", "Lo acorto sin avisar", "Los intervalos del plan se basan en el manual y se cambian con respaldo."),
    ],
    ctx=("abc", "El presupuesto de ejemplo del taller se recortó y el jefe sugiere no comprar los filtros del plan. ¿Qué le muestras?", "Que los filtros del período cuestan 60.000 y una falla puede costar 1.200.000", "Que los filtros no son importantes", "Que un taller parado no cuesta nada", "Los datos muestran que el gasto preventivo es mucho menor que el costo de una falla."),
    sc=[
        ("En Gráfica: ¿cuántos repuestos se necesitan en un período?", "El período dividido por el intervalo", "El intervalo dice cada cuántas horas se cambia."),
        ("¿Qué se resta para saber cuántos repuestos comprar?", "El stock", "Lo que ya hay en bodega no se vuelve a comprar."),
        ("¿Qué costos suma una falla?", "La reparación y los días parados", "Ambos forman el costo total de la falla."),
    ],
    op=("Costos de ejemplo: un filtro cuesta $20.000 y se cambia cada 400 horas. Una falla cuesta reparación de $500.000 más 2 días parados a $150.000 cada uno. El período es de 1.600 horas y hay 1 filtro en stock. "
        "Calcula cuántos filtros se necesitan, cuántos faltan comprar, el costo de los filtros del período, el costo de una falla y cuántas veces mayor es.",
        "Filtros necesarios: 1.600 ÷ 400 = 4. Faltan 4 − 1 = 3. Costo de los 4 filtros: 4 × 20.000 = 80.000. Falla: 500.000 + 2 × 150.000 = 800.000. La falla es 800.000 ÷ 80.000 = 10 veces mayor.",
        ["calcula filtros necesarios y faltantes", "calcula costo preventivo y de la falla", "compara con una división"],
        ["hoja con los cinco cálculos"],
        ["olvidar el stock", "no sumar los días parados", "dividir al revés"],
        "Pregunta: «¿por qué restas el stock?». Si no puede explicarlo, recuerda que lo que ya hay no se compra otra vez."),
    reinforce="Inventa un repuesto con su precio e intervalo y calcula cuántos necesitas en 1.000 horas y cuánto cuestan.",
    extend="Explica por qué una parada también cuesta aunque nadie se haya lesionado.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (decisión de ejemplo, inventada). Hay 10 tareas de mantenimiento programadas este mes; 8 se hicieron a tiempo y quedaron registradas. Meta del taller: al menos 90 % de las tareas a tiempo. "
     "Un pedido urgente llega y el jefe propone postergar por 100 horas de uso la lubricación vencida de una máquina. Alternativa A: lubricar ahora, con una parada de 2 horas; la máquina cuesta $30.000 por hora parada. "
     "Alternativa B: postergar; riesgo de falla con costo de $900.000 (reparación y parada), según el historial de ejemplo.")
build(
    O7, 5, F,
    use="Aprenderé a comparar alternativas ante un mantenimiento vencido, a calcular el cumplimiento del plan y a verificar que la bitácora respalde lo que se hizo.",
    prior=["Conozco el plan, la bitácora y los costos de falla.", "Sé calcular porcentajes.", "Sé comparar costos."],
    explain=[
        "Cuando un mantenimiento está vencido y llega un pedido urgente, se comparan alternativas con datos: hacerlo ahora tiene un costo de parada conocido; postergarlo tiene un riesgo de falla con un costo mayor. La decisión la toma la persona responsable con la información del manual, la bitácora y la norma vigente; nadie decide en secreto.",
        "El cumplimiento del plan es el porcentaje de tareas hechas a tiempo: tareas a tiempo por 100 dividido por las tareas programadas. Se compara con la meta del taller. Para verificar, se revisa que cada tarea realizada esté anotada en la bitácora con fecha y responsable.",
        "Un pedido urgente no justifica saltarse una medida de seguridad ni falsear un registro. Si hay dudas, se informa." + MAQ,
    ],
    vocab=[("cumplimiento del plan", "porcentaje de tareas hechas a tiempo"), ("meta", "valor mínimo que el taller se propone alcanzar"), ("postergar", "dejar para después una tarea programada"), ("verificar", "comprobar con datos que algo se hizo y está registrado")],
    worked=[
        ("Porcentaje de cumplimiento", "En un mes de ejemplo se hicieron 9 de 12 tareas a tiempo. ¿Qué porcentaje es?", ["Se multiplica por 100 y se divide por las programadas.", "9 × 100 ÷ 12 = 75."], "75 %"),
        ("Costo de una parada", "Una parada de ejemplo dura 3 horas y la máquina cuesta $20.000 por hora. ¿Cuánto cuesta?", ["Se multiplican las horas por el costo por hora.", "3 × 20.000 = 60.000."], "$60.000")],
    mistakes=[("Postergar un mantenimiento por un pedido urgente sin informar el riesgo.", "Si la máquina falla, se pierde el pedido y se paga más.", "Informa a la persona responsable y compara costos."),
              ("Dar por cumplido el plan sin revisar la bitácora.", "Sin registro no hay prueba de que las tareas se hicieron.", "Comprueba cada tarea con su anotación.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el cumplimiento del plan?", "El porcentaje de tareas hechas a tiempo", "El número de máquinas del taller", "El precio de los repuestos", "Mide cuántas de las tareas programadas se hicieron a tiempo."),
        ("abc", "{F} ¿Cuál es la meta del taller?", "Al menos 90 % de las tareas a tiempo", "Al menos 50 %", "100 % exacto siempre", "La ficha fija una meta de 90 %."),
        ("=", "{F} ¿Qué porcentaje de las tareas del mes se hicieron a tiempo?", "8*100//10", "Se multiplican las tareas a tiempo por 100 y se dividen por las programadas.", " %"),
        ("abc", "{F} ¿Se cumple la meta del taller?", "No, porque 80 % es menor que 90 %", "Sí, porque 8 de 10 es más de la mitad", "Sí, porque se hicieron 8 tareas", "80 % no alcanza el 90 % de la meta."),
        ("=", "{F} ¿Cuántas tareas de las 10 debían hacerse a tiempo para llegar justo a la meta?", "10*90//100", "Se calcula el 90 % de las tareas programadas.", " tareas"),
        ("=", "{F} ¿Cuánto cuesta la parada de la alternativa A?", "2*30000", "Se multiplican las horas de parada por el costo por hora.", " pesos"),
        ("abc", "{F} ¿Qué alternativa tiene menor costo seguro?", "La A, con $60.000", "La B, con $0", "Ninguna cuesta", "La B puede costar $900.000 si ocurre la falla; la A tiene un costo conocido."),
        ("=", "{F} ¿Cuántas veces es mayor el costo de la falla de la alternativa B que el de la parada de la A?", "900000//(2*30000)", "Se divide el costo de la falla por el costo de la parada.", " veces"),
        ("abc", "{F} El jefe dice: «postergamos para cumplir el pedido». ¿Qué conviene responder?", "Mostrarle los costos y el riesgo con datos y dejar que decida con esa información", "Aceptar sin decir nada", "Anotar que se lubricó sin hacerlo", "La decisión se toma con datos y sin falsear registros."),
        ("abc", "{F} Un compañero propone anotar la lubricación como hecha «para cumplir la meta». ¿Qué respondes?", "No: anotar lo que no se hizo es una falta grave y quita confianza", "Sí, queda mejor el porcentaje", "Sí, pero solo por un mes", "El registro debe ser veraz aunque no se cumpla la meta."),
        ("abc", "{F} Antes de afirmar que el plan se cumplió, ¿qué se verifica?", "Que cada tarea hecha esté anotada en la bitácora con fecha y responsable", "Que el taller esté limpio", "Que el jefe lo diga", "La bitácora es la evidencia de lo realizado."),
        ("=", "{F} Si las 2 tareas restantes también se hubieran hecho a tiempo, ¿qué porcentaje de cumplimiento tendría el taller?", "(8+2)*100//10", "Se suman las tareas y se calcula el porcentaje sobre las programadas.", " %"),
        ("abc", "{F} Si ocurre la falla del escenario B, ¿qué se pierde además de la reparación?", "Los días de producción por la máquina parada", "Nada más", "La bitácora", "La falla también detiene el trabajo y cuesta por cada día parado."),
    ],
    ctx=("abc", "El cliente de un pedido urgente de ejemplo te pregunta si se puede entregar antes si se salta el mantenimiento. ¿Qué respondes?", "Que no se salta una medida de seguridad ni un mantenimiento sin evaluar el riesgo y que la decisión la toma la persona responsable", "Que sí, porque lo importante es el plazo", "Que se hace y no se anota", "El plazo no justifica omitir seguridad ni falsear registros."),
    sc=[
        ("En Gráfica: ¿cómo se calcula el cumplimiento del plan?", "Tareas a tiempo por 100 dividido por tareas programadas", "Es un porcentaje sobre el total programado."),
        ("¿Dónde se verifica que una tarea se hizo?", "En la bitácora", "La bitácora guarda fecha y responsable."),
        ("¿Qué haces si un mantenimiento está vencido y hay presión por el plazo?", "Informo y comparo costos", "La decisión se toma con datos y con la persona responsable."),
    ],
    op=("Caso de ejemplo. Hay 20 tareas programadas y 16 hechas a tiempo, con meta de 90 %. Una máquina tiene una lubricación vencida y llega un pedido urgente. Alternativa A: lubricar con 3 horas de parada a $25.000 por hora. Alternativa B: postergar con riesgo de falla de $600.000. "
        "Calcula el cumplimiento y si cumple la meta, el costo de A, cuántas veces mayor es el riesgo de B, y escribe qué recomendarías y qué dejarías anotado en la bitácora.",
        "Cumplimiento: 16 × 100 ÷ 20 = 80 %, no cumple el 90 %. Costo de A: 3 × 25.000 = 75.000. B arriesga 600.000, es 8 veces mayor. Recomiendo informar a la persona responsable y proponer A. En la bitácora se anota la tarea vencida, la decisión tomada, quién la tomó y la fecha, sin falsear nada.",
        ["calcula el cumplimiento y lo compara con la meta", "calcula costos y la comparación", "recomienda con registro veraz"],
        ["hoja con los cálculos, la recomendación y la anotación"],
        ["proponer anotar lo no hecho", "no comparar con la meta", "olvidar informar a la persona responsable"],
        "Pregunta: «¿por qué no puedes anotar la lubricación como hecha?». Si dice 'por reglas', pide que explique el riesgo de una bitácora falsa."),
    reinforce="Inventa un mes con 12 tareas y calcula el cumplimiento del plan para 9 y 11 tareas a tiempo.",
    extend="Explica por qué una buena bitácora ayuda a tomar mejores decisiones sobre qué mantener primero.",
)
