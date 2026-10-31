"""Cuaderno del estudiante, 5.º básico Tecnología: OA 02 (planificar la elaboración de un objeto), clases 1 a 5, y OA 03 (elaborar con dominio técnico), clases 1 a 5.

Seguridad: papel, cartón, cinta, cordel, cola fría escolar, témpera y tijeras de punta roma. Serrar, perforar madera y lijar solo con una persona adulta;
los cuadernos describen las técnicas, pero nunca piden usar cortadores, fuego, vidrio, pistola de silicona caliente ni herramientas con filo.
Medidas enteras en centímetros, milímetros, gramos y minutos. Precios inventados, múltiplos de 100 pesos.
Simplificación declarada: el plan de la ficha oficial es genérico; cada clase sigue el contenido del OA. Cerámicos y metales se tratan solo como materiales
(propiedades y precauciones), sin trabajarlos en las tareas abiertas.
"""
from __future__ import annotations

from student_content_te5_a import reg
from student_lessons import arith

OA2 = "TE05 OA 02"
OA3 = "TE05 OA 03"

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja y lápiz. Todas las secuencias están escritas en este cuaderno.",
    use="Aprenderé a ordenar las acciones para elaborar un objeto y a estimar cuánto demora cada una. Sirve para no perder tiempo ni cometer errores de orden.",
    prior=["Sé que un diseño tiene criterios.", "Sé que un dibujo técnico lleva medidas.", "Sé sumar y restar minutos."],
    explain=[
        "Planificar la elaboración es decidir qué vas a hacer, en qué orden y cuánto tiempo necesitas. La secuencia de acciones es la lista de pasos ordenada. Cada paso empieza con un verbo en infinitivo, como medir, cortar, unir o pintar. Un paso claro se puede hacer sin adivinar.",
        "El orden importa porque unos pasos dependen de otros. No puedes pintar antes de que el pegamento seque, ni cortar antes de medir y marcar. Para revisar el orden pregúntate: «¿Qué necesito tener terminado antes de este paso?». Esa pregunta ayuda a detectar errores antes de empezar a trabajar.",
        "A cada paso se le pone un tiempo estimado en minutos. La suma de todos los tiempos es lo que demora el trabajo. Si dos pasos no dependen uno del otro, dos personas pueden hacerlos al mismo tiempo, y así el trabajo es más corto. Un plan se puede dibujar como una fila de cajas con flechas.",
    ],
    vocab=[("secuencia", "lista de pasos en orden"), ("dependencia", "cuando un paso necesita que otro esté terminado"), ("tiempo estimado", "cálculo de cuánto demora un paso"), ("verbo en infinitivo", "palabra de acción terminada en ar, er o ir"), ("plan", "la secuencia con materiales y tiempos")],
    worked=[
        ("Ordenar los pasos", "Ordena estos pasos para hacer una caja de cartón: pintar, medir, cortar, pegar, marcar.", ["Primero medir y marcar, porque se necesita saber el tamaño.", "Luego cortar y pegar. La pintura va al final, cuando todo está seco."], "Medir, marcar, cortar, pegar y pintar"),
        ("Sumar los tiempos", "Medir y marcar 10 min, cortar 15 min, pegar 20 min, secar 30 min. ¿Cuánto demora todo?", ["Los tiempos son 10, 15, 20 y 30 minutos.", "Se suman: 10 + 15 + 20 + 30."], "75 minutos"),
    ],
    mistakes=[
        ("Escribir los pasos como «la caja» o «el pegamento».", "No son acciones, porque no dicen qué hacer.", "Empieza cada paso con un verbo: pegar las caras."),
        ("Poner «pintar» antes de «secar el pegamento».", "La pintura se corre cuando la pieza está húmeda.", "Pregunta qué debe estar terminado antes de cada paso."),
    ],
    R=[
        ("¿Cuál va primero al hacer una caja de cartón: cortar o medir?", "Medir", "Se necesita saber el tamaño antes de cortar."),
        ("¿Cuál de estas frases es una acción? A «base de cartón», B «cortar la base».", "B", "Una acción empieza con un verbo."),
        ("En un plan de trabajo, ¿qué es la secuencia de acciones?", "Los pasos en el orden en que se hacen", "Es la lista de pasos ordenada."),
    ],
    C=[
        ("Ana pegó las piezas y pintó enseguida, y la pintura se corrió. ¿Qué paso faltó entre pegar y pintar?", "Esperar a que seque", "La pieza estaba húmeda."),
        ("Plan: medir → marcar → cortar → unir → pintar. ¿Qué paso va justo después de marcar?", "Cortar", "Así lo indica la fila de pasos."),
        ("¿Por qué se mide antes de cortar?", "Porque se necesita el tamaño para cortar bien", "Cortar sin medir produce piezas de tamaño equivocado."),
    ],
    A=[
        arith("Un plan tiene medir 10 min, cortar 15 min, unir 20 min y secar 30 min. La clase dura 90 minutos. ¿Cuántos minutos sobran?", "90-10-15-20-30", "Se restan los cuatro tiempos de los 90 minutos."),
        ("Ordena: A pintar, B medir, C cortar, D pegar. ¿Cuál es el orden correcto?", "B, C, D, A", "Medir, cortar, pegar y al final pintar."),
        ("¿Cuál paso empieza con verbo? A «tijera», B «marcar las líneas», C «cartón grueso».", "B", "Solo B dice qué hacer."),
    ],
    Z=[
        ("Medir demora 20 min y preparar la pintura 10 min. Si dos personas hacen ambas tareas al mismo tiempo, ¿cuánto demoran?", "20 minutos", "Demoran lo que dura la tarea más larga."),
        ("Un plan dice: cortar, medir, pegar. ¿Qué error tiene?", "Corta antes de medir", "Para cortar se necesita haber medido y marcado."),
    ],
    D=[
        arith("Los pasos de un plan demoran 12, 18, 25 y 15 minutos. ¿Cuántos minutos demora el plan completo?", "12+18+25+15", "Se suman los cuatro tiempos."),
        arith("Un plan dura 70 minutos y tienes 90 minutos para hacerlo. Si necesitas dejar 10 minutos para ordenar, ¿cuántos minutos libres quedan?", "90-70-10", "Se restan el plan y el orden de los 90 minutos."),
    ],
    ctx=("Quieres hacer un porta-lápices de cartón. Los pasos son: pegar, medir 5 min, cortar 15 min, pintar 15 min, marcar 5 min, secar 20 min. Escribe la secuencia ordenada y el tiempo total, suponiendo que pegar demora 15 min.", "Medir, marcar, cortar, pegar, secar y pintar. Tiempo: 5 + 5 + 15 + 15 + 20 + 15 = 75 minutos", "Orden correcto y suma de todos los tiempos."),
    sc=[
        ("¿Con qué clase de palabra empieza cada paso?", "Con un verbo", "Dice la acción."),
        ("¿Qué pregunta ayuda a revisar el orden?", "Qué necesito tener terminado antes de este paso", "Muestra las dependencias."),
        ("¿Dos pasos que no dependen uno del otro pueden hacerse a la vez?", "Sí", "Así el trabajo se acorta."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un portalápices de cartón con base cuadrada y pintado. Objeto 2: un marco de cartón para un dibujo, pintado. Escribe la secuencia de al menos 6 pasos con verbos, un tiempo en minutos para cada uno y el total.",
        "Objeto 2: medir (5), marcar (5), cortar (15), pegar (15), secar (20), pintar (15). Total: 75 minutos.",
        ["pasos con verbo", "el orden respeta las dependencias", "cada paso tiene un tiempo en minutos", "el total está bien sumado"],
        ["lista de pasos con tiempos y total"],
        ["pintar antes de secar", "pasos sin verbo"],
        "Pregunta: «¿qué necesitas terminado antes de este paso?». Si no lo está, pídele cambiar el orden.",
    ),
    reinforce="Escribe en orden los pasos para preparar tu mochila antes de dormir y anota cuánto demora cada uno.",
    extend="Elige un plan de 5 pasos y marca cuáles dos podrían hacerse al mismo tiempo entre dos personas.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja, lápiz y los datos escritos en este cuaderno.",
    use="Aprenderé a hacer la lista de materiales con cantidades y a calcular su costo. Sirve para reunir todo antes de empezar y no quedarse sin materiales a mitad del trabajo.",
    prior=["Sé hacer la secuencia de acciones.", "Sé medir en centímetros.", "Sé sumar, restar y multiplicar con números hasta 10.000."],
    explain=[
        "La lista de materiales dice qué materiales necesitas, cuánto de cada uno y para qué sirve. Se escribe mirando el dibujo técnico y la secuencia de acciones. Una lista útil incluye cantidades con unidades: «3 cartones de 30 cm por 20 cm» o «240 cm de cinta». Una lista que solo dice «cartón y cinta» no alcanza.",
        "Las cantidades se calculan. Si cada unión necesita 40 cm de cinta y hay 6 uniones, necesitas 240 cm, porque 6 × 40 = 240. También conviene pensar en el desperdicio, que es el material que sobra y no sirve. Una hoja de 30 cm de ancho permite cortar 3 piezas de 8 cm y sobran 6 cm.",
        "Después se calcula el presupuesto, que es el costo total. Se multiplica el precio de cada material por su cantidad y se suman los resultados. Los materiales reutilizados, como cajas o tapas, cuestan $0. Si el presupuesto es mayor que la plata disponible, hay que buscar materiales más baratos o reutilizar más.",
    ],
    vocab=[("lista de materiales", "lista con cada material, su cantidad y su uso"), ("desperdicio", "material que sobra y no sirve"), ("presupuesto", "costo total de los materiales"), ("cantidad", "cuánto se necesita de un material"), ("reutilizar", "volver a usar un material en vez de botarlo")],
    worked=[
        ("Calcular una cantidad", "Un estante tiene 6 uniones y cada una necesita 40 cm de cinta. ¿Cuánta cinta se necesita?", ["Cantidad por unión: 40 cm. Uniones: 6.", "Se multiplica 6 × 40."], "240 cm de cinta"),
        ("Calcular un presupuesto", "Cartón reutilizado $0, cinta $600, témpera $1.200. Tienes $2.000. ¿Alcanza y cuánto sobra?", ["Total: 0 + 600 + 1.200 = 1.800.", "Resto: 2.000 − 1.800 = 200."], "Sí alcanza y sobran $200"),
    ],
    mistakes=[
        ("Escribir «cartón» sin cantidad ni medida.", "No se sabe cuánto reunir.", "Escribe cantidad y unidad: 3 cartones de 30 por 20 cm."),
        ("Olvidar el desperdicio al calcular el material.", "Falta material si sobran trozos que no sirven.", "Calcula cuántas piezas caben y cuánto sobra."),
    ],
    R=[
        ("¿Cuánto cuesta un material reutilizado que ya tenías en casa?", "$0", "No se compra, así que no suma costo."),
        ("¿Qué le falta a la lista «cartón y cinta»?", "Las cantidades con unidades", "No dice cuánto reunir."),
        ("¿Cómo se llama el material que sobra y no sirve?", "Desperdicio", "Es la parte sobrante inútil."),
    ],
    C=[
        ("¿Por qué conviene calcular el presupuesto antes de comprar?", "Para saber si alcanza la plata", "Evita comprar de más o quedarse corto."),
        ("Una hoja mide 30 cm de ancho y cortas piezas de 8 cm. ¿Cuántas piezas enteras caben?", "3", "Caben 3, porque 3 por 8 es 24 y 4 por 8 es 32, que pasa de 30."),
        ("Una tapa de botella reutilizada vale $0. Para el presupuesto, ¿se cuenta como material?", "Sí, con costo $0", "Se escribe en la lista aunque no cueste."),
    ],
    A=[
        arith("Cada unión necesita 25 cm de cinta y hay 8 uniones. ¿Cuántos centímetros de cinta se necesitan?", "8*25", "Se multiplican las uniones por la cinta de cada una."),
        arith("Hoja de 30 cm de ancho, piezas de 8 cm. ¿Cuántos centímetros sobran después de cortar 3 piezas?", "30-3*8", "Se restan los 24 cm usados de los 30 cm."),
        arith("Cinta $600 y témpera $1.200, cartón $0. ¿Cuánto cuesta todo?", "600+1200+0", "Se suman los tres costos."),
    ],
    Z=[
        ("Ana tiene $1.500 y los materiales cuestan $1.800. ¿Qué le sirve para que alcance sin cambiar el diseño? A comprar un material más caro, B reutilizar materiales que ya tiene, C agregar más piezas.", "B", "Reutilizar baja el costo sin cambiar el objeto."),
        ("Beto dice que 12 cm de ancho de una pieza permiten 4 piezas de 3 cm sin sobra. Cecilia dice que sobran 3 cm. ¿Quién tiene razón?", "Beto", "4 por 3 es 12, así que no sobra."),
    ],
    D=[
        arith("Una caja necesita 4 paredes de 24 cm de largo cada una. ¿Cuántos centímetros de cartón largo se necesitan en total?", "4*24", "Se multiplican las paredes por el largo de cada una."),
        arith("Compras 3 pinceles de $800 cada uno y un pegamento de $1.500. Pagas con $5.000. ¿Cuánto vuelto recibes?", "5000-3*800-1500", "Se resta el costo total de los $5.000."),
    ],
    ctx=("Para un estante necesitas: 4 paneles de cartón reutilizado ($0), 160 cm de cinta a $5 el cm y 1 témpera de $1.200. Calcula el costo de la cinta y el total, y di si alcanzan $2.500.", "Cinta: 160 × 5 = 800. Total: 0 + 800 + 1.200 = 2.000. Sí alcanzan y sobran $500", "Calcula costo de cinta, total y compara."),
    sc=[
        ("¿Qué datos lleva cada material de la lista?", "Cantidad, unidad y uso", "Así se reúne todo antes de empezar."),
        ("¿Cómo se calcula el presupuesto?", "Multiplicando precio por cantidad y sumando", "Así se obtiene el costo total."),
        ("¿Qué es el desperdicio?", "El material que sobra y no sirve", "Hay que contarlo al calcular."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un estante de 4 paneles de cartón con 6 uniones de 30 cm de cinta cada una. Objeto 2: una caja de 5 caras con 8 uniones de 25 cm de cinta cada una. Haz la lista de materiales con cantidades y calcula la cinta; suponiendo cartón $0, cinta a $4 el cm y témpera $1.200, calcula el presupuesto.",
        "Objeto 2: 5 caras de cartón, 8 × 25 = 200 cm de cinta (200 × 4 = $800), 1 témpera ($1.200). Total: $2.000.",
        ["lista con cantidades y unidades", "calcula bien la cantidad de cinta", "calcula el presupuesto", "indica el costo de cada material"],
        ["lista y cálculo de presupuesto"],
        ["lista sin cantidades", "olvidar materiales reutilizados"],
        "Pregunta: «¿cuánto necesitas de cada material?». Si falta un número, pídele calcularlo.",
    ),
    reinforce="Haz la lista de materiales de un trabajo de tu casa con cantidades y unidades.",
    extend="Escribe cómo bajarías $500 el presupuesto de tu objeto sin cambiar el diseño.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja y lápiz. Las situaciones están escritas en este cuaderno.",
    use="Aprenderé a elegir herramientas y técnicas adecuadas para cada acción del plan y a anotar las medidas de seguridad. Sirve para trabajar sin accidentes.",
    prior=["Sé hacer la secuencia de acciones.", "Sé hacer una lista de materiales.", "Sé que algunas herramientas requieren a una persona adulta."],
    explain=[
        "Cada acción del plan se hace con una técnica y una herramienta. Medir y marcar se hace con regla y lápiz. Cortar papel y cartón delgado se hace con tijeras de punta roma. Perforar papel se hace con un perforador. Pegar se hace con cola fría o cinta. Pintar se hace con pincel y témpera. Cada herramienta sirve para algo concreto.",
        "Para cada paso hay medidas de seguridad. Trabaja en una mesa ordenada y despejada, con el pelo largo amarrado. Corta alejando tus dedos de la línea de corte. Para pintar, cubre la mesa y ventila el lugar. Después de trabajar, lava tus manos y guarda las herramientas. Una persona adulta debe estar cerca cuando uses algo que pueda herir.",
        "Algunos trabajos usan herramientas más peligrosas, como el serrucho para serrar madera o el taladro para perforar. Esas herramientas solo las usa una persona adulta. Si el plan las necesita y no hay adulto disponible, se cambia por una alternativa más segura, como usar cartón grueso en lugar de madera. La seguridad es un criterio más del plan.",
    ],
    vocab=[("técnica", "manera de hacer una acción"), ("herramienta", "objeto que ayuda a hacer una acción"), ("medida de seguridad", "cuidado para evitar accidentes"), ("punta roma", "punta sin filo"), ("ventilar", "dejar entrar aire fresco al lugar")],
    worked=[
        ("Elegir la herramienta", "Debes dividir una hoja en tiras de 5 cm, marcarlas y cortarlas. ¿Qué herramientas usas en cada acción?", ["Para medir y marcar: regla y lápiz.", "Para cortar el papel: tijeras de punta roma."], "Regla y lápiz para medir y marcar, tijeras de punta roma para cortar"),
        ("Escribir la seguridad", "Vas a pintar un portalápices de cartón con témpera. ¿Qué medidas de seguridad escribes?", ["Cubro la mesa para no manchar.", "Ventilo el lugar y me lavo las manos al terminar."], "Cubrir la mesa, ventilar y lavarse las manos"),
    ],
    mistakes=[
        ("Usar las tijeras para cortar una madera delgada.", "No sirven para madera y pueden herir.", "La madera se sierra con serrucho, siempre con una persona adulta."),
        ("Cortar mientras otra persona sostiene la hoja cerca de la tijera.", "Los dedos quedan en la línea de corte.", "Corta alejando las manos y sostén el material lejos del filo."),
    ],
    R=[
        ("¿Qué herramienta sirve para medir y marcar un cartón?", "Regla y lápiz", "Se mide con la regla y se marca con el lápiz."),
        ("¿Quién puede usar un serrucho en esta clase?", "Una persona adulta", "Serrar es una tarea peligrosa."),
        ("¿Con qué se perfora una hoja de papel?", "Con un perforador", "Es la herramienta indicada para papel."),
    ],
    C=[
        ("Antes de pintar con témpera, ¿qué se hace con la mesa?", "Cubrirla", "Así no se mancha."),
        ("¿Por qué se cortan las piezas alejando los dedos de la línea de corte?", "Para no herirse", "Los dedos lejos de la tijera evitan cortes."),
        ("Una técnica es la manera de hacer una acción. ¿Cuál es una técnica? A «cortar sobre la línea marcada», B «tijera».", "A", "Una técnica es una manera de hacer; la tijera es una herramienta."),
    ],
    A=[
        ("Une cada acción con la herramienta: medir, cortar papel, pintar, perforar papel. Respuestas: A perforador, B pincel, C regla, D tijeras. ¿En qué orden se escriben las letras?", "C, D, B, A", "Medir regla, cortar tijeras, pintar pincel, perforar perforador."),
        ("Un plan necesita perforar una tabla de madera con un taladro. ¿Qué cambias si no hay adulto?", "Usar cartón grueso en vez de madera", "Se elige un material más seguro."),
        arith("Para pintar, cada una de 4 personas necesita 1 pincel y 1 trapo para limpiar. ¿Cuántos elementos hay que reunir en total?", "4*2", "Cada persona necesita 2 cosas."),
    ],
    Z=[
        ("Rita usa tijeras de punta roma para cortar cartón grueso y se le dobla. Su compañero dice: «Sigue cortando, con fuerza». ¿Qué debe hacer ella?", "Pedir ayuda a una persona adulta o cambiar a cartón más delgado", "Forzar la tijera aumenta el riesgo de herirse."),
        ("Dos planes: A pinta dentro de la sala cerrada sin ventilar, B abre la ventana antes. ¿Cuál cuida mejor la seguridad?", "B", "Ventilar es una medida de seguridad al pintar."),
    ],
    D=[
        arith("El trabajo tiene 5 pasos y cada paso necesita 2 medidas de seguridad. ¿Cuántas medidas hay que anotar en total?", "5*2", "Se multiplican los pasos por las medidas de cada uno."),
        ("Un plan dice: cortar con cortador. ¿Qué haces con ese paso?", "Cambiarlo por tijeras de punta roma o hacerlo una persona adulta", "El cortador tiene filo y no se usa en estas clases."),
    ],
    ctx=("Plan: medir una base de cartón de 20 cm, cortarla, perforarla con un perforador y pintarla. Escribe la herramienta de cada acción y una medida de seguridad para cortar y otra para pintar.", "Medir con regla y lápiz; cortar con tijeras de punta roma; perforar con perforador; pintar con pincel. Seguridad: alejar los dedos al cortar; cubrir la mesa y ventilar al pintar", "Une cada acción con su herramienta y agrega seguridad."),
    sc=[
        ("¿Qué herramienta se usa para cortar cartón delgado?", "Tijeras de punta roma", "Son seguras y cortan cartón delgado."),
        ("¿Qué se hace con el pelo largo al trabajar?", "Se amarra", "Así no estorba."),
        ("Si el plan pide serrar madera, ¿quién lo hace?", "Una persona adulta", "Serrar es peligroso."),
    ],
    open_task=(
        "Escoge un plan. Plan 1: hacer un estante de cartón con 3 paneles, pegar y pintar. Plan 2: hacer una caja con tapa de cartón, perforarla con perforador y pintarla. Para cada acción escribe la herramienta, la técnica y una medida de seguridad.",
        "Plan 2: perforar: perforador, uno a la vez. Seguridad: dedos lejos del perforador.",
        ["cada acción tiene herramienta", "cada acción tiene técnica", "cada acción tiene una medida de seguridad", "no usa herramientas con filo"],
        ["tabla de acción, herramienta, técnica y seguridad"],
        ["herramienta equivocada para la acción", "olvidar la seguridad"],
        "Pregunta: «¿qué podría herirte en este paso?». Si no sabe responder, repasen la seguridad.",
    ),
    reinforce="Mira las herramientas que hay en tu casa y anota para qué sirve cada una y quién debe usarla.",
    extend="Escribe qué cambiarías en un plan si no tienes un perforador ni adulto cerca.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja y lápiz. Las tablas con puntajes están escritas en este cuaderno.",
    use="Aprenderé a buscar materiales, herramientas o técnicas alternativas y a elegir la mejor con criterios. Sirve para seguir adelante cuando falta algo o cuando hay una opción mejor.",
    prior=["Sé hacer la lista de materiales.", "Sé elegir herramientas y medidas de seguridad.", "Sé sumar puntajes."],
    explain=[
        "A veces falta un material o una herramienta, o aparece una opción mejor. Entonces se busca una alternativa, que es otra forma de lograr el mismo resultado. Si no hay cinta, se puede unir con cola fría y pestañas de cartón. Si no hay témpera, se puede usar papel de color pegado. Cada alternativa debe cumplir los criterios del diseño.",
        "Para decidir, se comparan las opciones con una tabla de criterios. Se da un puntaje a cada opción en cada criterio: por ejemplo, 3 es lo mejor y 1 es lo más débil. Los criterios pueden ser resistencia, costo, seguridad y cuidado del ambiente. Se suman los puntajes y gana la opción con el total mayor. En costo, 3 significa el más barato.",
        "Un puntaje no reemplaza al pensamiento. Una opción puede tener el puntaje más alto y aun así quedar descartada si rompe una restricción, como el límite de dinero o de seguridad. Primero se descartan las opciones que no cumplen las restricciones y después se comparan las restantes. La decisión final se explica con los datos de la tabla.",
    ],
    vocab=[("alternativa", "otra forma de lograr el mismo resultado"), ("tabla de criterios", "tabla que compara opciones con puntajes"), ("puntaje", "número que muestra qué tan bien cumple una opción"), ("restricción", "límite que no se puede pasar"), ("descartar", "dejar fuera una opción")],
    worked=[
        ("Elegir con tabla", "Opción A, cinta: resistencia 2, costo 3, seguridad 3. Opción B, cola fría: resistencia 3, costo 2, seguridad 3. ¿Cuál tiene mayor puntaje?", ["A: 2 + 3 + 3 = 8.", "B: 3 + 2 + 3 = 8.", "Empatan, así que se desempata por el criterio más importante para el uso."], "Empatan con 8 puntos y se desempata por el criterio más importante"),
        ("Descartar por restricción", "Una opción tiene 9 puntos pero cuesta $3.000 y solo tienes $2.000. ¿Qué haces?", ["Primero reviso la restricción de dinero.", "La opción no cabe en el presupuesto."], "La descarto aunque tenga mayor puntaje"),
    ],
    mistakes=[
        ("Elegir la opción con mayor puntaje aunque rompa una restricción.", "Una restricción no se puede pasar.", "Descarta primero las que no cumplen las restricciones."),
        ("Cambiar a una alternativa sin revisar los criterios del diseño.", "La alternativa puede no resolver el problema.", "Compara la alternativa con los criterios antes de decidir."),
    ],
    R=[
        ("Si no hay cinta, ¿se puede unir con cola fría y pestañas de cartón?", "Sí", "Es otra forma de lograr la unión."),
        ("En una tabla, 3 es lo mejor y 1 es lo más débil. Una opción tiene 1 en seguridad. ¿Es fuerte o débil en seguridad?", "Débil", "El puntaje 1 es el más débil."),
        ("En Tecnología: ¿Qué es una alternativa?", "Otra forma de lograr el mismo resultado", "Reemplaza una opción que no se puede usar."),
    ],
    C=[
        ("¿Por qué se descartan primero las opciones que rompen una restricción?", "Porque una restricción no se puede pasar", "No se pueden aceptar aunque tengan buen puntaje."),
        ("Opción A suma 9 puntos y opción B suma 7. Ninguna rompe restricciones. ¿Cuál se prefiere?", "A", "Tiene el mayor total."),
        ("Una alternativa más barata baja la seguridad del diseño. ¿Se acepta?", "No", "La seguridad es un criterio que debe cumplirse."),
    ],
    A=[
        arith("Una opción tiene resistencia 3, costo 2 y seguridad 3. ¿Cuántos puntos suma?", "3+2+3", "Se suman los tres puntajes."),
        arith("Opción A suma 8 puntos y opción B suma 5. ¿Cuántos puntos más tiene A?", "8-5", "Se resta el total de B del total de A."),
        ("Falta pintura. ¿Cuál alternativa mantiene el criterio «tiene color»? A usar papel de color pegado, B dejar el cartón sin pintar.", "A", "El papel de color cumple el criterio de color."),
    ],
    Z=[
        ("Tabla: opción A suma 9 y cuesta $2.800; opción B suma 7 y cuesta $1.500. Tienes $2.000. ¿Cuál eliges?", "B", "A pasa tu presupuesto y B lo cumple."),
        ("Dos opciones empatan con 8 puntos. El criterio más importante es la seguridad. A tiene 3 en seguridad y B tiene 2. ¿Cuál eliges?", "A", "Se desempata por el criterio más importante."),
    ],
    D=[
        arith("Tres opciones suman 6, 8 y 7 puntos. ¿Cuántos puntos más tiene la mejor que la peor?", "8-6", "Se resta el total menor del mayor."),
        ("Opción A: resistencia 3, costo 1, seguridad 3, ambiente 2. Opción B: resistencia 2, costo 3, seguridad 2, ambiente 3. ¿Cuál suma más?", "B", "A suma 3+1+3+2=9 y B suma 2+3+2+3=10."),
    ],
    ctx=("Para unir un estante de cartón tienes dos alternativas. Cinta: resistencia 2, costo 3, seguridad 3, ambiente 1. Cola fría: resistencia 3, costo 2, seguridad 3, ambiente 2. Calcula el total de cada una y elige.", "Cinta: 2 + 3 + 3 + 1 = 9. Cola fría: 3 + 2 + 3 + 2 = 10. Elijo cola fría", "Suma bien y elige la mayor."),
    sc=[
        ("¿Qué se descarta primero?", "Las opciones que rompen una restricción", "Una restricción no se puede pasar."),
        ("¿Qué se hace con los puntajes de una opción?", "Se suman", "El total permite comparar."),
        ("¿Una alternativa debe cumplir los criterios del diseño?", "Sí", "Si no los cumple, no resuelve el problema."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: no tienes cinta para unir un estante y puedes usar cola fría (resistencia 3, costo 2, seguridad 3) o cordel (resistencia 2, costo 3, seguridad 3); el criterio más importante es la resistencia. Caso 2: no tienes pincel y puedes usar una esponja (resistencia 2, costo 3, seguridad 3) o un trozo de tela (resistencia 3, costo 2, seguridad 3); el criterio más importante es el costo. Calcula el total de cada opción, desempata con el criterio más importante y explica tu elección.",
        "Caso 1: cola fría 8 y cordel 8. Empatan; elijo cola fría porque el estante necesita más resistencia.",
        ["suma bien los puntajes", "compara las opciones", "desempata con el criterio más importante", "explica la elección con datos"],
        ["tabla de puntajes con elección y explicación"],
        ["elegir sin calcular", "no desempatar con el criterio más importante"],
        "Pregunta: «¿qué dato de la tabla respalda tu decisión?». Si no tiene, pídele volver a la tabla.",
    ),
    reinforce="Piensa en una alternativa para un material de la lista que no tengas en casa.",
    extend="Agrega un cuarto criterio a la tabla y vuelve a calcular los totales para elegir.",
)

# ------------------------------------------------------------------ OA 02, clase 5
reg(
    OA2, 5,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a discutir qué efectos ambientales y sociales tienen los recursos que se usan. Sirve para elegir materiales de manera responsable y justa.",
    prior=["Sé hacer la lista de materiales.", "Sé elegir alternativas con criterios.", "Sé que reutilizar baja el costo."],
    explain=[
        "Los recursos que usamos en un trabajo vienen de algún lugar y terminan en otro. Eso tiene implicancias, que son efectos o consecuencias. Las implicancias ambientales son los efectos en la naturaleza. Por ejemplo, la madera viene de árboles y el plástico se demora mucho en descomponerse. Las implicancias sociales son los efectos en las personas: quién fabrica el material, cuánto cuesta y quién puede conseguirlo.",
        "Hay tres acciones para cuidar el ambiente. Reducir es usar menos material. Reutilizar es volver a usar lo que ya existe. Reciclar es transformar un desecho en material nuevo. Reducir y reutilizar suelen ser mejores que reciclar, porque usan menos energía y menos recursos. También conviene que el objeto dure mucho y se pueda reparar.",
        "Para discutir con respeto, da tu opinión con una razón y escucha las razones de los demás. Una razón dice qué efecto tiene el recurso. «Usar cajas del colegio evita comprar cartón y evita botar las cajas» es una razón. «Me gusta más» no es una razón sobre el recurso. En una discusión se puede cambiar de opinión si aparece un dato mejor.",
    ],
    vocab=[("implicancia", "efecto o consecuencia de una decisión"), ("reducir", "usar menos material"), ("reutilizar", "volver a usar lo que ya existe"), ("reciclar", "transformar un desecho en material nuevo"), ("durabilidad", "capacidad de un objeto de durar mucho")],
    worked=[
        ("Reconocer el tipo de implicancia", "«Usar cajas del colegio evita comprar cartón nuevo». ¿Es una implicancia ambiental o social?", ["Habla de evitar comprar cartón nuevo, es decir, usar menos recursos.", "Se refiere al efecto sobre la naturaleza."], "Ambiental"),
        ("Aplicar las tres acciones", "El curso tiene 60 botellas plásticas. Reutiliza 45 como maceteros y recicla el resto. ¿Cuántas recicla?", ["Total: 60. Reutilizadas: 45.", "Se resta 60 − 45."], "15 botellas"),
    ],
    mistakes=[
        ("Creer que reciclar es siempre lo mejor.", "Reducir y reutilizar usan menos recursos y energía.", "Primero reduce, luego reutiliza y al final recicla."),
        ("Opinar «me gusta más» como razón para elegir un material.", "No habla del efecto del recurso.", "Da una razón sobre el ambiente o las personas."),
    ],
    R=[
        ("Usar menos material, ¿es reducir, reutilizar o reciclar?", "Reducir", "Reducir es usar menos."),
        ("Volver a usar una caja de cartón para guardar cosas, ¿es reducir, reutilizar o reciclar?", "Reutilizar", "Se usa otra vez sin transformarla."),
        ("Si un material es muy caro, ¿es más fácil o más difícil que todos puedan conseguirlo?", "Más difícil", "El precio limita el acceso; es una implicancia social."),
    ],
    C=[
        ("«Un material barato permite que más personas hagan el objeto». ¿Es una implicancia ambiental o social?", "Social", "Habla del acceso de las personas."),
        ("¿Por qué reducir suele ser mejor que reciclar?", "Porque se usan menos recursos y menos energía", "Reciclar también gasta recursos y energía."),
        ("Un objeto que dura mucho y se puede reparar, ¿es mejor o peor para el ambiente?", "Mejor", "Se compra y se bota menos."),
    ],
    A=[
        arith("El curso junta 80 tapas. Reutiliza 50 para un juego. ¿Cuántas tapas quedan para otra actividad?", "80-50", "Se restan las tapas reutilizadas del total."),
        ("¿Cuál es una razón sobre el ambiente? A «Me gusta más», B «Las cajas del colegio ya existen y no se botan».", "B", "B dice el efecto sobre el recurso."),
        arith("Cada grupo de 4 estudiantes usa 3 cajas reutilizadas. Hay 6 grupos. ¿Cuántas cajas se reutilizan?", "6*3", "Se multiplica el número de grupos por las cajas de cada grupo."),
    ],
    Z=[
        ("Dos grupos fabrican el mismo estante. G1 usa cartón nuevo y G2 usa cajas del colegio. ¿Cuál tiene menor impacto ambiental y por qué?", "G2, porque reutiliza y evita cartón nuevo", "Reutilizar usa menos recursos."),
        ("Un material cuesta $5.000 por estudiante y el curso solo tiene dinero para que 2 de 30 lo reciban. ¿Qué implicancia social tiene elegirlo?", "Que la mayoría del curso no podría usarlo", "El costo deja a muchas personas fuera."),
    ],
    D=[
        arith("Un curso de 30 estudiantes bota 90 hojas por mes. Si cada estudiante reduce 1 hoja por mes, ¿cuántas hojas se botan ahora?", "90-30", "Se restan las hojas que reduce cada estudiante."),
        ("Un compañero dice: «Reciclemos todo, así no hace falta reducir». ¿Qué le respondes?", "Que reducir y reutilizar usan menos recursos", "Reciclar también gasta energía."),
    ],
    ctx=("Tu grupo puede hacer un porta-lápices con cartón nuevo ($1.200) o con cajas del colegio ($0). Escribe una implicancia ambiental y una implicancia social de elegir las cajas del colegio.", "Ambiental: se reutilizan las cajas y se compra menos cartón. Social: todo el curso puede conseguirlas sin pagar", "Una ambiental y una social con razón."),
    sc=[
        ("¿Cuáles son las tres acciones para cuidar el ambiente?", "Reducir, reutilizar y reciclar", "Son las acciones de la clase."),
        ("¿Una implicancia social habla de personas o de naturaleza?", "De personas", "Se refiere a quién fabrica, paga o consigue."),
        ("¿Qué debe tener una opinión en una discusión?", "Una razón", "Así se puede conversar con datos."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: tu grupo puede hacer un estante con cartón nuevo ($2.000) o con 12 cajas que el colegio iba a botar ($0). Caso 2: tu grupo puede hacer un macetero con una botella plástica que el curso ya tiene o con un macetero nuevo de plástico ($1.500). Escribe una implicancia ambiental y una social de cada opción, y tu elección con dos razones.",
        "Caso 1: cajas. Ambiental: se reutilizan 12 cajas. Social: no cuesta y todo el curso lo puede hacer. Elijo cajas.",
        ["una implicancia ambiental por opción", "una implicancia social por opción", "elige una opción", "da dos razones"],
        ["tabla de implicancias y elección razonada"],
        ["razones sin relación con el recurso", "no escuchar otras razones"],
        "Pregunta: «¿qué efecto tiene tu elección en la naturaleza y en las personas?». Si responde solo gusto, pídele una razón.",
    ),
    reinforce="Mira qué objeto desechable se usa mucho en tu casa y piensa cómo reutilizarlo.",
    extend="Escribe un acuerdo de 3 frases para que tu curso reutilice más materiales.",
)

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja y lápiz. Si quieres, mira objetos de papel, cartón, madera, tela, plástico y metal en tu casa, sin forzarlos.",
    use="Aprenderé a reconocer las propiedades de los materiales y a elegir el adecuado para cada pieza. Sirve para que el objeto funcione y resista.",
    prior=["Sé que los objetos están hechos de materiales.", "Sé hacer una lista de materiales.", "Sé que algunos materiales son peligrosos."],
    explain=[
        "Los materiales tienen propiedades, que son sus características. Un material puede ser rígido, que no se dobla, o flexible, que se dobla. Puede ser liviano o pesado. Puede ser resistente, que aguanta fuerza, o frágil, que se quiebra. Puede ser impermeable, que no deja pasar el agua, o absorbente, que la absorbe.",
        "Los grupos de materiales son: papeles y cartones, maderas, fibras como lana o cordel, plásticos, cerámicos como la loza, metales y desechos como cajas o tapas. El papel es liviano y flexible. El cartón es más rígido. La madera es rígida y resistente. Las fibras son flexibles. El plástico suele ser impermeable. La cerámica es dura pero frágil. El metal es resistente.",
        "Elegir un material es relacionar la propiedad con lo que se necesita. Un portalápices necesita paredes rígidas, así que sirve cartón. Un cordón para colgar necesita flexibilidad y resistencia, así que sirve una fibra. Los cerámicos y los metales pueden quebrarse o tener bordes que cortan. En estas clases no se trabajan; solo se estudian. Los desechos limpios se pueden usar.",
    ],
    vocab=[("propiedad", "característica de un material"), ("rígido", "que no se dobla"), ("flexible", "que se dobla sin romperse"), ("frágil", "que se quiebra con facilidad"), ("impermeable", "que no deja pasar el agua")],
    worked=[
        ("Relacionar propiedad y necesidad", "Necesitas el cuerpo de un portalápices que no se doble. ¿Qué propiedad buscas y qué material sirve?", ["Busco rigidez, porque no debe doblarse.", "El cartón y la madera son rígidos; el cartón es seguro para esta clase."], "Material rígido, como el cartón"),
        ("Elegir para colgar", "Necesitas un cordón para colgar un cartel liviano. ¿Qué propiedades pide?", ["Debe doblarse para atarse y resistir el tirón.", "Una fibra como el cordel tiene ambas propiedades."], "Flexible y resistente, por ejemplo un cordel"),
    ],
    mistakes=[
        ("Elegir un material porque «se ve lindo» sin mirar su propiedad.", "El objeto puede no funcionar.", "Primero escribe qué propiedad necesitas y luego elige."),
        ("Usar una lata o loza rota para hacer el objeto.", "Los bordes cortan.", "No uses cerámicos ni metales rotos; usa desechos limpios y seguros."),
    ],
    R=[
        ("Un material que no se dobla, ¿es rígido o flexible?", "Rígido", "Rígido significa que no se dobla."),
        ("El cordel, ¿es una fibra o un metal?", "Una fibra", "El cordel está hecho de fibras."),
        ("Un material que no deja pasar el agua, ¿es impermeable o absorbente?", "Impermeable", "Impermeable significa que el agua no lo atraviesa."),
    ],
    C=[
        ("Necesitas la base de un estante que aguante peso. ¿Qué propiedad buscas?", "Resistencia", "La base debe aguantar fuerza."),
        ("¿Por qué una taza de loza es frágil?", "Porque se quiebra con facilidad", "La cerámica es dura pero se rompe con un golpe."),
        ("Una caja limpia de cereal sin uso, ¿es un desecho útil para un trabajo?", "Sí", "Es cartón limpio que se puede reutilizar."),
    ],
    A=[
        ("Quieres un envoltorio liviano y flexible para un regalo. ¿Sirve mejor papel o madera?", "Papel", "El papel es liviano y flexible."),
        ("Quieres un vaso que guarde agua. ¿Qué propiedad necesita el material?", "Ser impermeable", "El agua no debe atravesarlo."),
        arith("Una pieza de madera pesa 300 gramos y una de cartón pesa 80 gramos. ¿Cuántos gramos más pesa la de madera?", "300-80", "Se resta el peso del cartón del peso de la madera."),
    ],
    Z=[
        ("Dos estudiantes eligen material para sostener libros en un estante. Una elige papel y otro elige madera. ¿Quién acierta y por qué?", "El que elige madera, porque es rígida y resistente", "El papel se dobla con el peso."),
        ("Un grupo quiere usar una lata cortada para un portalápices. ¿Qué riesgo tiene y qué alternativa propones?", "Los bordes cortan; usar cartón", "El cartón es seguro y rígido."),
    ],
    D=[
        arith("Una caja de cartón pesa 120 gramos y lleva 3 piezas de madera de 90 gramos cada una. ¿Cuántos gramos pesa todo?", "120+3*90", "Se suma la caja y el peso de las tres piezas."),
        ("Una tapa debe ser impermeable y liviana. ¿Cuál cumple las dos: papel, plástico o madera maciza?", "Plástico", "El plástico es impermeable y liviano; el papel no es impermeable y la madera maciza es más pesada."),
    ],
    ctx=("Debes elegir material para un portalápices que quedará en tu mesa. Necesita paredes rígidas, que no sean pesadas y que sean seguras en el colegio. Elige entre cartón limpio, loza rota y madera maciza, y explica.", "Cartón limpio, porque es rígido, liviano y seguro. La loza rota corta y la madera maciza es pesada", "Elige según propiedades y seguridad."),
    sc=[
        ("En Tecnología: ¿Qué es una propiedad de un material?", "Una característica del material", "Describe cómo es el material."),
        ("¿Qué material sirve para un cordón para colgar?", "Una fibra", "Es flexible y resistente."),
        ("¿Se usan cerámicos y metales rotos en las tareas?", "No", "Sus bordes pueden cortar."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un portalápices. Objeto 2: un colgador para un cartel liviano. Anota la propiedad que necesitas, escribe dos materiales posibles y elige uno con una razón que mencione la propiedad.",
        "Objeto 2: flexible y resistente; materiales: cordel y papel; elijo el cordel porque es resistente.",
        ["dice la propiedad que necesita", "nombra dos materiales", "elige uno", "da una razón con la propiedad", "no elige materiales peligrosos"],
        ["tabla de propiedad, materiales y elección"],
        ["elegir por apariencia", "materiales peligrosos"],
        "Pregunta: «¿qué propiedad necesita este objeto?». Si no responde, vuelvan a la propiedad.",
    ),
    reinforce="Toca con cuidado tres objetos de tu casa y di si son rígidos o flexibles.",
    extend="Elige un objeto y explica por qué se hizo de su material y no de otro.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Regla de 30 cm, lápiz y una hoja. Las medidas están escritas en este cuaderno.",
    use="Aprenderé a medir con precisión y a marcar líneas de corte y de doblez. Sirve para que las piezas encajen y el objeto quede bien armado.",
    prior=["Sé medir con regla en centímetros.", "Sé leer vistas con cotas.", "Sé que 1 cm tiene 10 mm."],
    explain=[
        "Medir es comparar una longitud con una unidad. En la regla, cada raya grande es 1 centímetro y cada raya pequeña es 1 milímetro. Un centímetro tiene 10 milímetros. Para medir, coloca el cero de la regla al comienzo de lo que mides y lee dónde termina. Si la regla tiene el borde gastado, empieza en el 1 y resta 1 al resultado.",
        "Marcar es dejar señales en el material. Marca con lápiz grafito y haz puntos pequeños en los extremos de la medida. Después une los puntos con la regla para trazar la línea de corte. La línea de doblez se marca con puntos o trazos cortos para distinguirla. Una escuadra ayuda a trazar ángulos rectos, es decir, esquinas cuadradas.",
        "Un buen consejo es «medir dos veces y cortar una». Comprobar la medida antes de cortar evita perder material. También conviene revisar la tolerancia, que es cuánto se acepta que una pieza se aleje de la medida. Una pieza de 25 cm que mide 24 cm tiene 1 cm de diferencia, que puede ser demasiado si debe encajar.",
    ],
    vocab=[("milímetro", "la décima parte de un centímetro"), ("marcar", "dejar señales en el material"), ("línea de corte", "línea donde se corta"), ("escuadra", "regla en forma de ángulo recto"), ("tolerancia", "diferencia aceptada respecto de la medida")],
    worked=[
        ("Medir con borde gastado", "Una regla tiene el borde gastado. Pones una pieza desde la raya del 1 y termina en la raya del 13. ¿Cuánto mide?", ["Empecé en el 1, no en el 0.", "Resto: 13 − 1."], "12 cm"),
        ("Pasar de centímetros a milímetros", "Una línea mide 4 cm y 5 mm. ¿Cuántos milímetros son?", ["4 cm son 4 × 10 = 40 mm.", "Agrego 5 mm."], "45 mm"),
    ],
    mistakes=[
        ("Marcar con un trazo grueso y a ojo.", "La medida real queda imprecisa.", "Haz un punto pequeño en el extremo y une con regla."),
        ("Cortar sin comprobar la medida.", "No se puede corregir un corte equivocado.", "Mide dos veces y corta una."),
    ],
    R=[
        ("¿Cuántos milímetros tiene 1 centímetro?", "10", "Un centímetro tiene 10 milímetros."),
        ("Para medir con regla, ¿dónde se coloca el cero?", "Al comienzo de lo que se mide", "Así se lee la longitud completa."),
        ("¿Con qué se marca una línea de corte sobre cartón?", "Con lápiz y regla", "El grafito deja una línea fina."),
    ],
    C=[
        ("¿Por qué se mide dos veces antes de cortar?", "Para evitar errores que no se pueden corregir", "Un corte no se puede deshacer."),
        ("Una pieza debe medir 25 cm y mide 24 cm. ¿Cuál es la diferencia?", "1 cm", "25 menos 24 es 1."),
        ("¿Cómo se marca una línea de doblez para distinguirla de la de corte?", "Con puntos o trazos cortos", "Así se ve que no se corta."),
    ],
    A=[
        arith("Una línea mide 7 cm y 3 mm. ¿Cuántos milímetros mide?", "7*10+3", "Se pasan los centímetros a milímetros y se suman los 3 mm."),
        arith("Una pieza empieza en la raya 1 y termina en la raya 15 de una regla con el borde gastado. ¿Cuántos centímetros mide?", "15-1", "Se resta 1, porque empezó en el 1."),
        arith("Debes marcar 3 tiras de 12 cm una a continuación de la otra. ¿Cuántos centímetros de largo necesitas en total?", "3*12", "Se multiplican las tiras por su largo."),
    ],
    Z=[
        ("Dos piezas de 20 cm miden 20 cm y 19 cm. Deben encajar en una ranura de 20 cm. ¿Cuál no debe usarse sin corregir?", "La de 19 cm", "Queda 1 cm suelta."),
        ("Ana marcó con puntos pequeños y unió con regla; Beto marcó a ojo con trazo grueso. ¿Quién tiene una línea de corte más confiable?", "Ana", "Los puntos y la regla dan una línea precisa."),
    ],
    D=[
        arith("Una hoja mide 297 mm de largo. ¿Cuántos centímetros enteros mide, sin contar los milímetros que sobran?", "297//10", "Se divide entre 10."),
        arith("Una pieza debe medir 250 mm. Se corta con 247 mm. ¿Cuántos milímetros le faltan?", "250-247", "Se resta la medida del corte de la medida pedida."),
    ],
    ctx=("Necesitas cortar 4 tiras de cartón de 15 cm para las paredes de una caja. Escribe cuántos centímetros de largo de cartón necesitas, cómo las marcarías y qué harías antes de cortar.", "60 cm. Marcaría puntos en 15 cm y los uniría con regla. Mediría de nuevo antes de cortar", "Cálculo, marcado y comprobación."),
    sc=[
        ("¿Cuántos mm tiene 1 cm?", "10", "Una raya grande tiene 10 milímetros."),
        ("¿Qué consejo evita cortes equivocados?", "Medir dos veces y cortar una", "Se comprueba antes de cortar."),
        ("¿Qué es la tolerancia?", "La diferencia aceptada respecto de la medida", "Dice cuánto se puede alejar la pieza."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: marcar en cartón 4 tiras de 18 cm de largo y 3 cm de ancho. Trabajo 2: marcar en cartón una base de 14 cm por 10 cm con una línea de doblez a 2 cm de cada borde. Dibuja las marcas con regla, anota las medidas y comprueba dos veces.",
        "Trabajo 2: rectángulo de 14 por 10 con líneas punteadas a 2 cm de cada borde, medidas anotadas.",
        ["usa puntos y regla", "las medidas son correctas", "distingue corte y doblez", "comprueba dos veces"],
        ["pieza marcada con medidas y comprobación"],
        ["marcar a ojo", "no distinguir corte y doblez"],
        "Pregunta: «¿desde dónde mediste y cómo comprobaste?». Si no comprobó, pídele medir de nuevo.",
    ),
    reinforce="Mide con regla el largo de tu cuaderno en centímetros y en milímetros.",
    extend="Explica por qué una pieza de 26 cm no entra en una ranura de 25 cm.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja y lápiz. La técnica se describe en este cuaderno; practica con papel y tijeras de punta roma solo si tienes y con cuidado.",
    use="Aprenderé técnicas seguras para cortar y perforar, y sabré cuándo una tarea es solo para una persona adulta. Sirve para cortar piezas limpias sin lastimarse.",
    prior=["Sé medir y marcar.", "Sé que algunas herramientas son solo para adultos.", "Sé elegir materiales por sus propiedades."],
    explain=[
        "Cortar es separar una pieza de un material. Para papel y cartón delgado se usan tijeras de punta roma. El material se pone entre las dos hojas abiertas de la tijera y se corta sobre la línea marcada. Se mueve el papel con la otra mano y no la tijera, y los dedos se mantienen lejos de la línea de corte. Los cortes se hacen de a poco.",
        "Perforar es hacer un agujero. En papel se usa un perforador. La madera se perfora con taladro, y la madera se sierra con serrucho. Ambas herramientas las usa solo una persona adulta, porque pueden causar heridas graves. Un estudiante puede marcar dónde va el agujero o el corte, pero no hacerlo.",
        "Antes de cortar o perforar, sujeta bien el material y revisa que la línea esté marcada. Trabaja sentado, con la mesa despejada. Los recortes se guardan para reutilizar o se botan en el basurero. Nunca camines con las tijeras abiertas; ciérralas y entrégalas con el mango hacia la otra persona. Si algo se atasca, pide ayuda y no fuerces la herramienta.",
    ],
    vocab=[("cortar", "separar una pieza de un material"), ("perforar", "hacer un agujero"), ("taladro", "herramienta eléctrica para perforar, solo para adultos"), ("serrucho", "herramienta con dientes para serrar madera, solo para adultos"), ("recorte", "trozo que sobra al cortar")],
    worked=[
        ("Elegir el modo de cortar", "Debes cortar una tira de cartón delgado y otra de madera de 2 cm de grosor. ¿Qué herramienta y quién la usa en cada caso?", ["El cartón delgado se corta con tijeras de punta roma por el estudiante.", "La madera se sierra con serrucho y solo la persona adulta lo usa."], "Tijeras para el cartón; serrucho de una persona adulta para la madera"),
        ("Pasar la tijera", "Vas a entregar unas tijeras a una compañera. ¿Cómo lo haces?", ["Las cierro.", "Las entrego con el mango hacia ella."], "Cerradas y con el mango hacia la otra persona"),
    ],
    mistakes=[
        ("Mover la tijera mientras el papel queda quieto.", "El corte se desvía y los dedos se acercan al filo.", "Mueve el papel con la otra mano y corta de a poco."),
        ("Tratar de perforar madera con un lápiz o punzón sin adulto.", "Puede resbalar y causar heridas.", "Marca el punto y pide a una persona adulta que perfore."),
    ],
    R=[
        ("¿Con qué herramienta se corta papel o cartón delgado?", "Con tijeras de punta roma", "Son seguras para estas tareas."),
        ("¿Quién usa el taladro?", "Una persona adulta", "Es una herramienta peligrosa."),
        ("¿Con qué se perfora una hoja de papel?", "Con un perforador", "Es la herramienta indicada."),
    ],
    C=[
        ("¿Por qué se mueve el papel y no la tijera?", "Porque el corte queda más recto y seguro", "Así los dedos no se acercan al filo."),
        ("Para entregar unas tijeras a otra persona, ¿cómo se hace?", "Cerradas y con el mango hacia ella", "Así no hay punta apuntando."),
        ("¿Qué puede hacer un estudiante en una tarea de serrar madera?", "Marcar la línea", "Marcar es seguro; serrar lo hace un adulto."),
    ],
    A=[
        arith("Debes cortar 3 tiras de 25 cm de cartón. ¿Cuántos centímetros de corte son en total?", "3*25", "Se multiplican las tiras por su largo."),
        ("Debes hacer 2 agujeros en el borde de una tira de cartulina para pasar un cordel. ¿Qué herramienta usas?", "Un perforador", "Sirve para agujerear papel y cartulina delgada."),
        ("Una tabla de madera debe cortarse en 2 partes. ¿Qué haces tú?", "Marcar la línea y pedir a una persona adulta que serruche", "Serrar solo lo hace un adulto."),
    ],
    Z=[
        ("Dos estudiantes cortan una tira. Ana mueve el papel y Beto mueve la tijera con el papel quieto. ¿Cuál tiene una técnica más segura y por qué?", "Ana, porque mantiene los dedos lejos del filo", "Mover el papel da un corte más recto y seguro."),
        ("La tijera se atasca con un cartón grueso. Un compañero dice que fuerces. ¿Qué haces?", "No forzar y pedir ayuda a un adulto", "Forzar puede hacer que la tijera resbale."),
    ],
    D=[
        arith("Cortas 4 tiras de 12 cm y 2 tiras de 20 cm. ¿Cuántos centímetros de corte son?", "4*12+2*20", "Se suman los cortes de cada grupo de tiras."),
        ("Un plan dice: cortar un tubo de metal con sierra. ¿Qué haces con ese paso?", "Cambiarlo por otro material seguro o pedir a un adulto", "El metal y la sierra no se usan en las tareas de estudiantes."),
    ],
    ctx=("Debes preparar una tarjeta colgante de cartulina. Tienes que cortar 4 tiras de 20 cm de largo y perforar 2 agujeros en el borde de una de ellas con perforador, para pasar un cordel. Escribe qué herramienta usas y dos medidas de seguridad.", "Tijeras de punta roma y perforador. Seguridad: dedos lejos de la línea de corte y mesa despejada", "Dice herramientas y dos medidas."),
    sc=[
        ("¿Qué se mueve al cortar: el papel o la tijera?", "El papel", "Así el corte es seguro."),
        ("¿Quién usa el serrucho?", "Una persona adulta", "Es una herramienta peligrosa."),
        ("¿Cómo se camina con unas tijeras?", "No se camina con tijeras abiertas", "Las tijeras abiertas pueden herir."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: cortar 4 tiras de 20 cm de cartón delgado. Trabajo 2: cortar una base de 15 cm por 10 cm y hacer 2 agujeros en su borde con perforador. Escribe la técnica paso a paso, la herramienta, dónde van las manos y una medida de seguridad.",
        "Trabajo 1: marco con regla, sostengo el cartón, muevo el cartón sobre la tijera cerrando de a poco, dedos lejos de la línea.",
        ["pasos en orden", "herramienta correcta", "ubica bien las manos", "una medida de seguridad"],
        ["lista de pasos de corte con seguridad"],
        ["mover la tijera en vez del papel", "usar herramientas de adulto"],
        "Pregunta: «¿dónde están tus dedos al cortar?». Si están cerca de la línea, pídele cambiar la posición.",
    ),
    reinforce="Muestra a una persona de tu casa cómo se entregan unas tijeras y cómo se corta papel con cuidado.",
    extend="Explica por qué la madera se sierra solo con un adulto y cómo ayudas tú en esa tarea.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja y lápiz. Las situaciones están escritas en este cuaderno; si quieres practicar usa papel, cartón, cola fría y cordel.",
    use="Aprenderé distintas formas de unir y pegar piezas y a elegir la mejor según el material. Sirve para que las uniones resistan y el objeto no se desarme.",
    prior=["Sé elegir materiales por sus propiedades.", "Sé cortar con seguridad.", "Sé que algunas uniones se pueden deshacer."],
    explain=[
        "Unir es juntar dos piezas. Hay uniones permanentes, que no se pueden deshacer sin dañar las piezas, y uniones temporales, que sí se pueden deshacer. Pegar con cola fría es permanente. Amarrar con cordel o encajar una pieza en una ranura son uniones temporales, porque se pueden volver a abrir. Una cinta adhesiva puede ser temporal o semipermanente.",
        "La mejor unión depende del material. Papel con papel se une con pegamento en barra. Cartón con cartón se une con cola fría o con cinta. La madera se une con cola fría y presión mientras seca. Las fibras se unen con nudos o amarras. El plástico liso se une mejor con cinta fuerte que con cola fría. La pistola de silicona caliente la usa solo una persona adulta.",
        "Para una buena unión: limpia las piezas, pon una capa fina de pegamento, junta las piezas y presiona. Espera el tiempo de secado que dice la etiqueta antes de mover o pintar. Una unión con pestañas aumenta la superficie que se pega y aguanta más. Las uniones también se prueban: un objeto bien armado resiste una prueba suave sin soltarse.",
    ],
    vocab=[("unión permanente", "unión que no se puede deshacer sin dañar las piezas"), ("unión temporal", "unión que se puede deshacer"), ("pestaña", "tira doblada que da más superficie para pegar"), ("secado", "tiempo que tarda un pegamento en endurecer"), ("presionar", "apretar las piezas mientras el pegamento seca")],
    worked=[
        ("Elegir la unión", "Quieres unir dos paredes de cartón y que no se separen. ¿Qué usas y cómo mejoras la unión?", ["Cola fría, porque es una unión permanente.", "Agrego una pestaña doblada para tener más superficie de pegado."], "Cola fría con una pestaña"),
        ("Distinguir tipos de unión", "Una caja se cierra con un cordel amarrado que se puede abrir. ¿Es una unión permanente o temporal?", ["El cordel se puede desamarrar sin dañar la caja.", "Eso la hace temporal."], "Temporal"),
    ],
    mistakes=[
        ("Mover la pieza antes de que seque la cola.", "La unión se debilita o se despega.", "Espera el tiempo de secado y presiona suavemente."),
        ("Poner mucha cola creyendo que pega más.", "El exceso chorrea y tarda más en secar.", "Usa una capa fina y pareja."),
    ],
    R=[
        ("Una unión con cola fría, ¿es permanente o temporal?", "Permanente", "No se puede deshacer sin dañar las piezas."),
        ("Un cordel amarrado que se puede desamarrar, ¿es unión permanente o temporal?", "Temporal", "Se puede deshacer."),
        ("¿Qué se hace con las piezas pegadas mientras seca la cola?", "Se presionan y se dejan quietas", "Así la unión queda firme."),
    ],
    C=[
        ("¿Por qué una pestaña ayuda a pegar?", "Porque da más superficie para pegar", "Más superficie pegada resiste más."),
        ("Quieres unir una hoja de papel con otra hoja de papel. ¿Cuál sirve mejor: A pegamento en barra, B amarra con cordel?", "A", "El pegamento en barra es adecuado para papel con papel."),
        ("¿Quién usa una pistola de silicona caliente?", "Una persona adulta", "Quema y es peligrosa."),
    ],
    A=[
        arith("La cola fría tarda 30 minutos en secar. La clase dura 90 minutos. Después de esperar el secado, ¿cuántos minutos quedan de clase?", "90-30", "Se restan los 30 minutos de secado de los 90 minutos."),
        ("Debes unir un cordel con un cartón para colgarlo. ¿Qué unión usas: amarra por un agujero o cola fría sola?", "Amarra por un agujero", "Una amarra sujeta mejor una fibra a un cartón."),
        ("Quieres que una tapa se pueda abrir y cerrar muchas veces. ¿Unión permanente o temporal?", "Temporal", "Debe poder deshacerse."),
    ],
    Z=[
        ("Dos estudiantes pegan paredes de cartón. Uno agrega pestañas y el otro no. Al empujar, el que no tiene pestañas se despega. ¿Por qué?", "Porque tenía menos superficie de pegado", "Las pestañas aumentan la superficie."),
        ("Una cinta fuerte y una cola fría se prueban para unir plástico liso. ¿Cuál es probable que resulte mejor y por qué?", "La cinta fuerte", "La cola fría no se adhiere bien al plástico liso."),
    ],
    D=[
        arith("Cada unión lleva 2 pestañas y hay 7 uniones. ¿Cuántas pestañas hacen falta?", "2*7", "Se multiplican las pestañas por las uniones."),
        ("Un plan junta dos piezas de madera con cola fría y las deja secando solo 5 minutos aunque la etiqueta dice 30. ¿Qué pasa?", "La unión queda débil", "No se respetó el tiempo de secado."),
    ],
    ctx=("Armas un portalápices de cartón con 4 paredes unidas por pestañas de 2 cm y cola fría. La etiqueta dice que seca en 30 minutos. Escribe cómo pegas, cuánto esperas y qué haces mientras seca.", "Pongo una capa fina de cola en las pestañas, junto las paredes y presiono. Espero 30 minutos sin mover. Mientras seca preparo la pintura", "Describe técnica, tiempo y espera."),
    sc=[
        ("¿Una unión que se puede deshacer es permanente o temporal?", "Temporal", "Se puede abrir sin dañar."),
        ("¿Cuánto pegamento se pone?", "Una capa fina", "El exceso chorrea."),
        ("¿Por qué se espera el secado?", "Para que la unión quede firme", "Si se mueve antes se debilita."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: unir las 4 paredes de una caja de cartón con pestañas y cola fría. Caso 2: unir un cartel de cartón con un cordel para colgarlo, usando un agujero hecho con perforador. Escribe el material, la unión, los pasos y cuánto esperas antes de mover.",
        "Caso 1: cartón y cola fría; pestañas de 2 cm; capa fina; junto y presiono; espero 30 minutos.",
        ["nombra la unión elegida", "explica los pasos", "dice cuánto espera", "la elección coincide con el material"],
        ["pasos de unión con tiempos"],
        ["mover antes de secar", "unión equivocada para el material"],
        "Pregunta: «¿esta unión se puede deshacer? ¿por qué la elegiste?». Si no coincide con el uso, pídele revisar.",
    ),
    reinforce="Busca tres cosas armadas en tu casa y di si sus uniones son permanentes o temporales.",
    extend="Explica por qué los muebles de madera se arman a veces con cola y a veces con tornillos.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja y lápiz. La tarea está descrita en este cuaderno. Si pintas, usa témpera lavable, papel de diario sobre la mesa y un lugar ventilado.",
    use="Aprenderé a mezclar colores y materiales, a lijar con seguridad y a pintar con buen acabado. Sirve para dejar un producto limpio, resistente y bien presentado.",
    prior=["Sé que la pintura se usa al final del plan.", "Sé cubrir la mesa y ventilar.", "Sé que algunas tareas son solo para adultos."],
    explain=[
        "Mezclar es unir dos o más cosas para obtener una nueva. Con témpera se mezclan colores por partes: 2 partes de amarillo y 1 parte de azul dan verde; rojo con blanco da rosado; amarillo con rojo da naranja. Para que el color se repita, siempre se usa la misma cantidad de cada parte, por ejemplo cucharadas.",
        "Lijar es desgastar una superficie con una lija para dejarla lisa. Se hace con una lija suave, siempre con una persona adulta cerca, en la dirección de las fibras de la madera. Se evita soplar el polvo; se limpia con un paño húmedo. Pintar viene después: cubre la mesa con diarios, aplica capas finas y espera a que cada una seque antes de poner la siguiente.",
        "El acabado es el aspecto final del producto. Un buen acabado no tiene grumos ni goteos, cubre las esquinas y no deja manchas fuera de la pieza. Se revisa con una lista: ¿está lisa?, ¿cubrió todo?, ¿seca? Después de trabajar se lavan los pinceles con agua y las manos con jabón. Así se demuestra dominio de la técnica.",
    ],
    vocab=[("mezclar", "unir dos o más cosas para obtener una nueva"), ("lijar", "desgastar una superficie para dejarla lisa"), ("acabado", "aspecto final de la superficie"), ("capa fina", "pintura aplicada en poca cantidad"), ("dirección de la fibra", "sentido en que corren las líneas de la madera")],
    worked=[
        ("Mezclar por partes", "Quieres un verde que se pueda repetir. Usas 2 cucharadas de amarillo y 1 de azul. ¿Cuántas cucharadas de verde obtienes?", ["Las partes son 2 cucharadas de amarillo y 1 de azul.", "Se suman las partes: 2 + 1."], "3 cucharadas de verde"),
        ("Revisar el acabado", "Una pieza pintada tiene un goteo en una esquina y una zona sin cubrir. ¿Qué dos problemas de acabado tiene y qué haces?", ["Tiene goteo y falta de cobertura.", "Espero a que seque, aplico una capa fina y repaso la zona."], "Goteo y zona sin cubrir; se corrige con una capa fina después de secar"),
    ],
    mistakes=[
        ("Poner una capa gruesa para terminar rápido.", "Gotea y tarda mucho en secar.", "Aplica capas finas y espera el secado."),
        ("Lijar sin adulto y soplar el polvo.", "El polvo irrita la nariz y los ojos.", "Pide a una persona adulta que lije y limpia con paño húmedo."),
    ],
    R=[
        ("Amarillo con azul, ¿qué color da?", "Verde", "Es una mezcla conocida de colores."),
        ("¿Quién lija madera en estas clases?", "Una persona adulta", "El polvo y la herramienta requieren cuidado."),
        ("¿Con qué se limpia el polvo del lijado?", "Con un paño húmedo", "Soplar lo esparce por el aire."),
    ],
    C=[
        ("¿Por qué se usan capas finas de pintura?", "Para evitar goteos y que seque mejor", "Una capa fina seca parejo."),
        ("Quieres repetir un color después. ¿Qué haces al mezclar?", "Anotar las partes que usaste", "Así se obtiene el mismo color otra vez."),
        ("Una pieza pintada tiene la pintura corrida en una esquina. ¿Qué problema de acabado es?", "Goteo", "La pintura se corrió hacia abajo."),
    ],
    A=[
        arith("Mezclas 2 cucharadas de amarillo y 1 de azul para un verde. Necesitas 3 veces esa cantidad. ¿Cuántas cucharadas de amarillo usas?", "2*3", "Se multiplica la cantidad de amarillo por 3."),
        arith("Mezclas 3 cucharadas de rojo con 2 de blanco para un rosado. ¿Cuántas cucharadas hay en total?", "3+2", "Se suman las dos partes."),
        ("Necesitas un anaranjado. ¿Qué dos colores de témpera mezclas?", "Amarillo y rojo", "Amarillo y rojo dan naranja."),
    ],
    Z=[
        ("Dos estudiantes pintan una caja. Uno aplica una capa gruesa y la otra dos capas finas esperando que seque cada una. ¿Cuál tendrá mejor acabado y por qué?", "La segunda, porque no hay goteos", "Las capas finas secan parejas."),
        ("Una madera se lija contra la dirección de la fibra y queda rayada. ¿Qué se debe hacer?", "Lijar en la dirección de la fibra con adulto", "Así el desgaste es parejo."),
    ],
    D=[
        arith("Cada capa seca en 20 minutos y aplicarás 2 capas, esperando el secado de cada una. ¿Cuántos minutos de secado necesitas en total?", "2*20", "Se multiplican las capas por el secado."),
        ("Una pintura se vierte sobre la mesa sin diarios. ¿Qué medida de seguridad y orden faltó?", "Cubrir la mesa", "La mesa debe protegerse antes de pintar."),
    ],
    ctx=("Pintas un portalápices con rosado. La receta es 3 cucharadas de rojo y 2 de blanco. Haces 2 capas finas y cada una seca 20 minutos. Escribe cuántas cucharadas de rojo usas para 2 recetas y cuánto demora el secado total.", "Rojo: 3 × 2 = 6 cucharadas. Secado: 20 + 20 = 40 minutos", "Calcula la mezcla y el secado."),
    sc=[
        ("¿Qué hay que repetir para obtener el mismo color otra vez?", "Las mismas cantidades de cada parte", "Así el color se repite."),
        ("¿Qué se revisa en el acabado?", "Que esté liso, cubierto y seco", "Son los tres puntos de la lista."),
        ("¿Quién lija madera?", "Una persona adulta", "Lijar requiere mucho cuidado."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: mezclar un verde con 2 cucharadas de amarillo y 1 de azul para pintar un portalápices de cartón. Trabajo 2: mezclar un rosado con 3 cucharadas de rojo y 2 de blanco para pintar una caja de cartón. Escribe la mezcla, cómo pintas en 2 capas finas y la lista de acabado con tres revisiones.",
        "Trabajo 1: 3 cucharadas de verde; dos capas finas; reviso liso, cubierto y seco.",
        ["escribe las partes de la mezcla", "usa capas finas con secado", "lista de acabado de tres puntos", "incluye cubrir la mesa y ventilar"],
        ["mezcla y lista de acabado"],
        ["capas gruesas", "olvidar el secado"],
        "Pregunta: «¿cómo sabes que la capa está seca antes de la siguiente?». Si no sabe, repasen el tiempo de secado.",
    ),
    reinforce="Mezcla dos colores de tus lápices de colores sobre un papel y anota el resultado.",
    extend="Escribe cómo reconocerías un buen acabado en un objeto pintado de tu casa.",
)
