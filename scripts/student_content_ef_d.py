"""Student material for 1.º básico Educación Física y Salud, OA 09 (higiene, postura y vida saludable) y OA 10 (trabajo en equipo y roles)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


OA9, OA10 = "EF01 OA 09", "EF01 OA 10"

# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Agua limpia, jabón, una toalla limpia, un reloj con segundos y 6 tarjetas de papel con los pasos del lavado (se escriben en la clase). Un adulto cerca del lavamanos.",
    use="Aprenderé a lavarme las manos y la cara después de hacer ejercicio. Sirve para sacar la suciedad y los gérmenes y sentirme limpio y cómodo.",
    prior=["Sé abrir y cerrar una llave de agua con cuidado.", "Sé contar hasta 20."],
    explain=[
        "Cuando juegas o haces ejercicio, tus manos se ensucian y tu cara suda. Después de la clase conviene lavarse las manos y la cara. El agua y el jabón sacan la suciedad y los gérmenes, que son seres muy pequeños que pueden enfermarnos.",
        "El lavado de manos tiene 6 pasos en este orden: 1) mojar las manos, 2) poner jabón, 3) frotar las palmas y el dorso (la parte de atrás), 4) frotar entre los dedos, las uñas y los pulgares, 5) enjuagar con agua, 6) secar con una toalla limpia. Frotar debe durar al menos 20 segundos, el tiempo de contar despacio hasta 20.",
        "Para la cara, usa agua y, si la tienes sucia, un poco de jabón suave; luego sécala con una toalla limpia. Si tu polera quedó sudada, cámbiala por una seca. Nunca compartas tu toalla. Y recuerda cerrar la llave al terminar para no gastar agua.",
    ],
    vocab=[("gérmenes", "seres muy pequeños que pueden enfermar"), ("frotar", "restregar las manos entre sí"), ("dorso", "la parte de atrás de la mano"), ("enjuagar", "sacar el jabón con agua"), ("higiene", "cuidar la limpieza del cuerpo")],
    worked=[
        W("Ordenar los pasos", "Tienes estos pasos desordenados: secar, enjuagar, frotar, mojar, poner jabón. ¿Cuál es el orden?", ["Primero mojo las manos.", "Después pongo jabón y froto.", "Luego enjuago y por último seco."], "Mojar, jabón, frotar, enjuagar, secar."),
        W("Tiempo de frotado", "Debes frotar 20 segundos. Ya llevas 12. ¿Cuántos segundos faltan?", ["La meta es 20.", "Llevo 12.", "20 − 12 = 8."], "8 segundos."),
    ],
    mistakes=[M("Frotar solo 3 segundos.", "Se tiene prisa.", "Cuenta despacio hasta 20 mientras frotas."),
              M("Olvidar el dorso y las uñas.", "Se piensa que solo importan las palmas.", "Frota palmas, dorso, entre los dedos, uñas y pulgares.")],
    tiers={
        "recovery": [
            ex("Para lavarte las manos usas agua y...", "Jabón", "Ayuda a sacar la suciedad."),
            ex("Después del ejercicio, ¿te lavas las manos y la cara o no hace falta?", "Te las lavas", "Se ensucian y suda la cara."),
            ex("¿Cuántos segundos mínimo frotas?", "20", "Es el tiempo recomendado."),
        ],
        "understand": [
            ex("¿Qué son los gérmenes?", "Seres muy pequeños que pueden enfermar", "No se ven a simple vista."),
            ex("¿Con qué te secas las manos: con una toalla limpia o con la ropa sucia?", "Con una toalla limpia", "Una toalla sucia las ensucia."),
            ex("¿Es buena idea compartir la toalla?", "No", "Se pasan gérmenes."),
        ],
        "apply": [
            ex("Ordena: A) enjuagar, B) mojar, C) frotar con jabón. ¿Cuál es el orden?", "B, C, A", "Mojar, frotar con jabón y enjuagar."),
            arith("Debes frotar 20 segundos y llevas 14. ¿Cuántos faltan?", "20-14", "Se resta lo frotado.", " segundos"),
            ex("El lavado tiene 6 pasos. Ya hiciste mojar, poner jabón y frotar palmas y dorso. ¿Cuántos pasos faltan?", "3", "Faltan frotar entre los dedos, enjuagar y secar: 6 menos 3 son 3."),
        ],
        "reason": [
            ex("Beto se enjuaga sin jabón porque «el agua basta». ¿Qué le dices?", "Que el jabón saca la suciedad y los gérmenes", "El jabón ayuda a limpiar mejor."),
            ex("Ana se lava solo las palmas. ¿Qué partes olvida?", "Dorso, entre los dedos, uñas y pulgares", "Esas partes también se ensucian."),
        ],
        "challenge": [
            arith("Te lavas las manos 3 veces en el día y cada vez frotas 20 segundos. ¿Cuántos segundos frotaste?", "3*20", "Se multiplican veces por segundos.", " segundos"),
            ex("Al terminar el lavado cierras la llave. ¿Para qué?", "Para no gastar agua", "El agua es un recurso valioso."),
        ],
    },
    context=[ex("Terminó la clase de Educación Física. Tienes las manos con tierra y sudor en la cara. ¿Qué haces primero: A) tomar colación sin lavarte, B) lavarte las manos con agua y jabón, C) jugar más?", "B", "Se lava antes de comer.")],
    selfcheck=[
        ex("¿Cuántos pasos tiene el lavado de manos?", "6", "Mojar, jabón, frotar, entre dedos, enjuagar y secar."),
        ex("¿Cuánto tiempo mínimo frotas?", "20 segundos", "Es lo recomendado."),
        ex("¿Qué haces con la polera sudada?", "La cambias por una seca", "Evita el frío y la humedad."),
    ],
    open_task=task("Escribe en 6 papelitos los pasos del lavado: mojar, jabón, frotar palmas y dorso, frotar entre dedos y uñas, enjuagar, secar. Desordénalos y ordénalos de nuevo. Luego lávate las manos con un adulto cerca, cuenta hasta 20 mientras frotas y anota los 6 pasos que hiciste. Marca con una palomita cada uno.",
                   "Ordené los 6 papelitos bien. Me lavé con agua y jabón, froté 20 segundos y me sequé con toalla limpia. Hice los 6 pasos.",
                   ["ordena los 6 pasos", "frota al menos 20 segundos", "se seca con toalla limpia"],
                   ["papelitos ordenados", "lista con palomitas", "observación de un adulto"],
                   ["frotar menos de 20 segundos", "olvidar el dorso", "no secar"],
                   "Reconoce los pasos hechos y pide repetir el que olvidó."),
    reinforce="Cuenta hasta 20 en voz baja mientras te frotas las manos con jabón.",
    extend="Explica a un hermano o amigo por qué se lava con jabón y no solo con agua.",
)

register(
    OA9, 2,
    materials="Una mochila liviana con un cuaderno y una botella de agua, una silla, un adulto y un espejo si hay. Los datos de peso están escritos en esta clase.",
    use="Aprenderé a mantener una postura cómoda y a llevar la mochila sin dañar mi espalda. Sirve para que no me duela el cuerpo al estudiar y moverme.",
    prior=["Sé nombrar espalda, hombros y pies.", "Sé sentarme en una silla."],
    explain=[
        "Postura es la forma en que colocas tu cuerpo al estar de pie, sentado o caminando. Una buena postura es cómoda, no rígida: cabeza alineada con el cuerpo, hombros relajados, espalda larga y pies apoyados en el suelo. Si te cansas, cambia de posición con calma.",
        "Al sentarte, apoya la espalda en el respaldo, los pies planos en el suelo y las rodillas dobladas. Al llevar la mochila, usa las dos correas sobre los hombros, ajustadas para que quede pegada a la espalda, no colgando. Se recomienda que la mochila no pese más de una décima parte (10 %) del peso del niño.",
        "Para calcular una décima parte, divide el peso entre 10. Si pesas 20 kilos, la mochila debe pesar 2 kilos o menos. Si pesa más, saca lo que no necesitas. Nunca cargues la mochila en un solo hombro y no te inclines hacia adelante por el peso.",
    ],
    vocab=[("postura", "cómo coloco mi cuerpo"), ("alinear", "poner derecho, uno sobre otro"), ("correa", "tira que sostiene la mochila"), ("décima parte", "una de diez partes iguales"), ("relajado", "sin tensión")],
    worked=[
        W("Peso de la mochila", "Pesas 20 kilos. ¿Cuánto debe pesar como máximo tu mochila (una décima parte)?", ["Divido 20 entre 10.", "20 ÷ 10 = 2.", "La mochila debe pesar 2 kilos o menos."], "2 kilos como máximo."),
        W("Sentarse bien", "Te sientas a estudiar. ¿Cómo colocas tu cuerpo?", ["Apoyo la espalda en el respaldo.", "Pongo los pies planos en el suelo.", "Mantengo hombros relajados y cabeza alineada."], "Espalda apoyada, pies en el suelo, hombros relajados."),
    ],
    mistakes=[M("Llevar la mochila en un solo hombro.", "Se ve más cómodo al principio.", "Usa las dos correas, bien ajustadas."),
              M("Sentarse con la espalda muy curvada hacia adelante.", "Se mira muy de cerca el cuaderno.", "Apoya la espalda y acerca el cuaderno.")],
    tiers={
        "recovery": [
            ex("La mochila se lleva ¿en un hombro o en los dos?", "En los dos", "Reparte el peso."),
            ex("Al sentarte, los pies van ¿colgando o planos en el suelo?", "Planos en el suelo", "Los pies planos dan estabilidad al cuerpo."),
            ex("Una buena postura es ¿cómoda o muy rígida?", "Cómoda", "No es tensión."),
        ],
        "understand": [
            ex("¿Qué es la postura?", "Cómo coloco mi cuerpo", "Está de pie, sentado o caminando."),
            ex("¿Por qué conviene cambiar de posición si te cansas?", "Porque estar quieto mucho rato cansa", "El cuerpo necesita moverse."),
            ex("La mochila, ¿debe quedar pegada a la espalda o colgando?", "Pegada a la espalda", "Pesa menos y es más estable."),
        ],
        "apply": [
            arith("Pesas 30 kilos. ¿Cuánto debe pesar como máximo tu mochila (una décima parte)?", "30//10", "Se divide el peso entre 10.", " kilos"),
            arith("Pesas 20 kilos y tu mochila pesa 3 kilos. ¿Cuántos kilos sobran sobre el máximo de 2?", "3-2", "Se resta el máximo del peso real.", " kilo"),
            ex("Tu mochila tiene: cuaderno, botella de agua, un libro grande, juguetes y tres cuadernos más. Si pesa de más, ¿qué sacas primero?", "Los juguetes", "No son necesarios para la clase."),
        ],
        "reason": [
            ex("Dani dice «llevo la mochila en un hombro porque es más rápido». ¿Qué problema tiene?", "Carga el peso solo de un lado", "Puede doler la espalda."),
            ex("Una mochila de 4 kilos para un niño de 25 kilos, ¿está dentro del máximo?", "No", "El máximo es 2,5 kilos."),
        ],
        "challenge": [
            arith("Eres 40 kilos de peso. ¿Cuál es el máximo de la mochila (décima parte)?", "40//10", "Se divide el peso entre 10.", " kilos"),
            ex("Tu mochila tiene un cuaderno de 1 kilo, un libro de 1 kilo y una botella de 1 kilo. Pesas 25 kilos. ¿Está dentro de la décima parte (2,5 kg)?", "No", "Pesa 3 kilos, más de 2,5."),
        ],
    },
    context=[ex("Al salir del colegio, tu amigo lleva la mochila colgando de un solo hombro y se inclina hacia un lado. ¿Qué le sugieres: A) que use las dos correas ajustadas, B) que la arrastre, C) que corra?", "A", "Repartir el peso protege la espalda.")],
    selfcheck=[
        ex("¿Cuántas correas usas?", "Las dos", "El peso se reparte."),
        ex("Si pesas 20 kilos, ¿cuánto pesa como máximo tu mochila?", "2 kilos", "Es una décima parte."),
        ex("¿Dónde van los pies al sentarte?", "Planos en el suelo", "Los pies planos dan estabilidad al cuerpo."),
    ],
    open_task=task("Con un adulto, sigue estos pasos: 1) ponte una mochila con un cuaderno y una botella; 2) ajusta las dos correas hasta que quede pegada a la espalda; 3) siéntate con la espalda apoyada y los pies planos; 4) levántate, camina 10 pasos derecho con hombros relajados. Después calcula: si un niño pesa 30 kilos, ¿cuánto pesa como máximo su mochila? Anota cuántos de los 4 pasos hiciste bien.",
                   "Hice bien 4 de 4 pasos. Con las correas ajustadas la mochila queda pegada. Para un niño de 30 kilos el máximo es 3 kilos.",
                   ["usa las dos correas", "se sienta con espalda apoyada y pies planos", "calcula el máximo correctamente"],
                   ["lista de 4 pasos", "cálculo escrito", "observación de un adulto"],
                   ["mochila en un hombro", "postura rígida", "calcular mal"],
                   "Reconoce la postura cómoda y pide ajustar una correa si queda suelta."),
    reinforce="Siéntate con la espalda apoyada y los pies planos durante 10 segundos; relaja los hombros.",
    extend="Pesa tu mochila en casa con ayuda de un adulto y compara con una décima parte de tu peso.",
)

register(
    OA9, 3,
    materials="Una botella de agua, 8 tarjetas de comida dibujadas o escritas con los nombres de la lista, y una hoja para clasificar. Todos los alimentos están escritos en esta clase.",
    use="Aprenderé a elegir agua y colaciones que me ayudan a moverme antes y después de hacer ejercicio. Sirve para tener energía y recuperarme.",
    prior=["Sé qué es una fruta.", "Sé qué es tener sed."],
    explain=[
        "El cuerpo necesita agua, sobre todo cuando sudas. Antes de hacer ejercicio puedes beber unos sorbos de agua, durante las pausas también, y después para reponer lo que perdiste. El agua es la mejor bebida para hidratarte; las bebidas muy dulces no son lo mejor para tomar a diario.",
        "Una colación saludable es una comida pequeña que da energía y nutre, como una fruta (manzana, plátano), un yogur sin mucha azúcar, un pan con queso o palta, o un vaso de leche. Antes de hacer ejercicio, conviene algo liviano, unos 30 a 60 minutos antes. Después de jugar, algo que te ayude a recuperarte, junto con agua.",
        "Escoger bien no significa nunca comer golosinas, sino que no sean la colación de todos los días. Tampoco hay que juzgar la colación de otros: cada familia come con lo que tiene. Si no tienes algo, una fruta, un pan o agua de la llave ya son opciones válidas.",
    ],
    vocab=[("hidratarse", "beber agua para reponer lo que se pierde"), ("colación", "comida pequeña entre comidas"), ("liviano", "que no pesa en el estómago"), ("energía", "fuerza para moverse"), ("recuperarse", "volver a estar bien después del esfuerzo")],
    worked=[
        W("Clasificar colaciones", "Tienes: manzana, galletas con mucha azúcar, plátano, yogur, papas fritas, pan con queso. ¿Cuáles son saludables para antes o después de hacer ejercicio?", ["Fruta (manzana, plátano): sí.", "Yogur y pan con queso: sí.", "Galletas muy dulces y papas fritas: son para ocasiones, no diarias."], "Manzana, plátano, yogur y pan con queso."),
        W("Cuánta agua", "Bebes 3 sorbos antes, 2 en la pausa y 4 al final. ¿Cuántos sorbos bebiste?", ["3 + 2 = 5.", "5 + 4 = 9.", "Son 9 sorbos."], "9 sorbos."),
    ],
    mistakes=[M("Beber solo bebida dulce al hacer ejercicio.", "Se piensa que da más energía.", "Bebe agua; las bebidas dulces tómalas pocas veces."),
              M("Comer mucho justo antes de jugar.", "Se tiene hambre.", "Elige algo liviano y espera un rato.")],
    tiers={
        "recovery": [
            ex("La mejor bebida para hidratarte es ¿agua o bebida dulce?", "Agua", "Hidrata sin azúcar."),
            ex("Una manzana, ¿es una colación saludable?", "Sí", "La manzana es una fruta saludable."),
            ex("Cuando sudas, ¿tu cuerpo pierde agua?", "Sí", "El sudor es agua."),
        ],
        "understand": [
            ex("¿Para qué sirve beber agua después de hacer ejercicio?", "Para reponer el agua que perdiste", "El sudor saca agua del cuerpo."),
            ex("¿Es malo comer una golosina una vez?", "No, pero no para todos los días", "Se trata de equilibrio."),
            ex("¿Hay que burlarse de la colación de otro?", "No", "Cada familia come con lo que tiene."),
        ],
        "apply": [
            ex("Lista: plátano, yogur, bebida muy dulce, pan con queso, papas fritas. ¿Cuántas son saludables para la colación diaria?", "3", "Plátano, yogur y pan con queso."),
            arith("Bebes 4 sorbos antes, 3 durante y 5 después. ¿Cuántos sorbos son?", "4+3+5", "Se suman.", " sorbos"),
            arith("Una colación liviana se come 30 minutos antes y el ejercicio dura 40. ¿Cuántos minutos pasan entre empezar la colación y terminar el ejercicio?", "30+40", "Se suman los dos tiempos.", " minutos"),
        ],
        "reason": [
            ex("Ema no tiene yogur pero sí un pan y agua. ¿Su colación sirve?", "Sí", "Pan y agua son opciones válidas."),
            ex("Beto tomó solo bebida dulce y se siente con sed de nuevo. ¿Qué debe tomar?", "Agua", "El agua hidrata mejor."),
        ],
        "challenge": [
            ex("Escribe una colación antes del ejercicio y otra después con alimentos de la lista (plátano, yogur, pan con queso, manzana). Respuesta modelo: plátano antes y pan con queso después. ¿Cuántas colaciones son?", "2", "Una antes y otra después."),
            arith("Un niño bebe 8 sorbos de agua en una clase; otro, 6. ¿Cuántos sorbos más bebe el primero?", "8-6", "Se resta.", " sorbos"),
        ],
    },
    context=[ex("Después de jugar en el patio tienes sed. Tu mochila tiene una botella de agua y un paquete de golosinas. ¿Qué eliges primero: A) las golosinas, B) beber agua, C) nada?", "B", "El agua repone lo que perdiste.")],
    selfcheck=[
        ex("¿Qué bebida hidrata mejor?", "Agua", "Hidrata sin azúcar."),
        ex("Da dos ejemplos de colación saludable.", "Fruta y pan con queso", "Son opciones de la lista."),
        ex("¿Se juzga la colación de otro?", "No", "Se respeta a todos."),
    ],
    open_task=task("Con las tarjetas de esta clase (manzana, plátano, yogur, pan con queso, galletas con mucha azúcar, papas fritas, bebida muy dulce y agua), arma dos colaciones para un día de ejercicio: una para antes (liviana) y otra para después. Escribe por qué las elegiste y cuántos sorbos de agua beberás en total (por ejemplo, 3 antes y 5 después).",
                   "Antes: plátano y 3 sorbos de agua. Después: pan con queso, yogur y 5 sorbos de agua. Elegí alimentos que dan energía y me ayudan a recuperarme. En total 8 sorbos.",
                   ["elige alimentos saludables", "incluye agua", "justifica su elección"],
                   ["hoja con las dos colaciones", "suma de sorbos", "relato oral"],
                   ["elegir solo dulces", "olvidar el agua", "criticar la colación de otros"],
                   "Pide que explique cómo cada alimento ayuda y respeta lo que cada familia tiene."),
    reinforce="Bebe unos sorbos de agua y dibuja tu colación favorita saludable.",
    extend="Compara dos colaciones y elige la mejor para antes de correr; explica por qué.",
)

register(
    OA9, 4,
    materials="12 tarjetas de papel con las acciones de abajo, un reloj y un lápiz. Las acciones están escritas en esta clase.",
    use="Aprenderé a ordenar lo que hago antes y después de hacer ejercicio. Sirve para cuidar mi cuerpo y estar listo para seguir con mi día.",
    prior=["Sé qué es antes y después.", "Sé lavarme las manos."],
    explain=[
        "Una rutina es una secuencia de acciones que repites siempre. Antes de la actividad física: ir al baño si hace falta, amarrar bien las zapatillas, beber unos sorbos de agua y calentar el cuerpo con movimientos suaves. Esto te prepara y evita lesiones.",
        "Después de la actividad física: caminar despacio para recuperarte, beber agua, lavarte las manos y la cara, cambiarte la polera si está sudada y comer una colación saludable si corresponde. Esto te ayuda a recuperarte y a mantener la higiene.",
        "Para ordenar una rutina, piensa qué va primero y qué va después. Por ejemplo, no tiene sentido lavarte las manos antes de jugar si luego te volverás a ensuciar. Y no se come con las manos sucias. Un buen orden hace que cuides tu cuerpo sin olvidar nada.",
    ],
    vocab=[("rutina", "acciones que repito siempre en orden"), ("antes", "lo que se hace primero"), ("después", "lo que se hace al terminar"), ("calentar", "preparar el cuerpo con movimientos suaves"), ("secuencia", "acciones en orden")],
    worked=[
        W("Antes de jugar", "Tienes estas acciones: beber agua, calentar, amarrar zapatillas. ¿En qué orden las haces antes de jugar?", ["Amarro las zapatillas primero para estar seguro.", "Bebo unos sorbos de agua.", "Termino calentando el cuerpo con movimientos suaves."], "Zapatillas, agua, calentar."),
        W("Después de jugar", "Acciones: lavarme las manos, caminar despacio, comer colación. ¿Cuál es el orden?", ["Primero camino despacio para recuperarme.", "Luego me lavo las manos.", "Por último como mi colación."], "Caminar, lavar las manos, comer."),
    ],
    mistakes=[M("Comer la colación antes de lavarse las manos.", "Se tiene hambre.", "Lávate las manos antes de comer."),
              M("Sentarse de golpe al terminar.", "Se quiere descansar ya.", "Camina despacio un minuto primero.")],
    tiers={
        "recovery": [
            ex("Amarrar las zapatillas, ¿se hace antes o después de jugar?", "Antes", "Zapatillas amarradas evitan caídas al jugar."),
            ex("Lavarte las manos y la cara, ¿se hace antes o después del ejercicio?", "Después", "Se ensucian al jugar."),
            ex("Calentar el cuerpo, ¿se hace antes o después de jugar?", "Antes", "Prepara los músculos."),
        ],
        "understand": [
            ex("En Educación Física, ¿qué es una rutina?", "Acciones que repito siempre en orden", "Siempre se hacen igual."),
            ex("¿Por qué se camina despacio al terminar?", "Para recuperarse de a poco", "El cuerpo baja el ritmo."),
            ex("¿Por qué no se come con las manos sucias?", "Porque pasan gérmenes", "El lavado evita enfermedades."),
        ],
        "apply": [
            ex("Ordena las acciones de después: A) comer colación, B) lavarse las manos, C) caminar despacio. ¿Cuál es el orden?", "C, B, A", "Primero te recuperas, luego te lavas y al final comes."),
            arith("Antes haces 3 acciones y después 5. ¿Cuántas acciones tiene tu rutina completa?", "3+5", "Se suman.", " acciones"),
            arith("Calientas 3 minutos y juegas 12. ¿Cuántos minutos son antes de la recuperación?", "3+12", "Se suman.", " minutos"),
        ],
        "reason": [
            ex("Beto se lava las manos antes de jugar y no después. ¿Qué falla?", "Después de jugar están sucias", "Se debe lavar al terminar."),
            ex("Ana dice «mi rutina empieza con comer, luego correr». ¿Qué le recomiendas?", "Esperar un poco y comer algo liviano", "Comer mucho antes de correr cae pesado."),
        ],
        "challenge": [
            ex("Cuenta cuántas acciones de antes hay: ir al baño, amarrar zapatillas, beber agua, calentar.", "4", "Se cuentan cuatro acciones en la lista."),
            ex("Cuenta cuántas acciones de después hay: caminar, beber agua, lavar manos y cara, cambiar polera, colación.", "5", "Se cuentan cinco acciones en la lista."),
        ],
    },
    context=[ex("Terminaste la clase de Educación Física y el timbre suena. Estás sudado y con las manos sucias. ¿Qué haces: A) correr a comer, B) caminar, beber agua, lavarte las manos y la cara, y cambiarte la polera, C) acostarte en el piso?", "B", "Es la rutina de después.")],
    selfcheck=[
        ex("¿Qué se hace antes de calentar?", "Amarrar las zapatillas", "Unas zapatillas bien amarradas dan seguridad."),
        ex("¿Qué se hace después de caminar despacio?", "Beber agua y lavarse las manos", "Es parte de la rutina."),
        ex("¿Cuántas acciones de antes hay en esta clase?", "4", "Baño, zapatillas, agua y calentar."),
    ],
    open_task=task("Escribe en tarjetas las acciones: ir al baño, amarrar zapatillas, beber agua, calentar, caminar despacio, beber agua, lavar manos y cara, cambiar polera, comer colación. Divídelas en «antes» y «después» y ordénalas. Luego pide a un adulto que mire mientras haces la rutina completa, y cuenta cuántas acciones hiciste.",
                   "Antes (4): baño, zapatillas, agua, calentar. Después (5): caminar, agua, lavar manos y cara, polera, colación. En total 9 acciones, todas en orden.",
                   ["separa antes y después", "ordena las acciones", "hace la rutina completa"],
                   ["tarjetas ordenadas", "observación de un adulto", "relato oral"],
                   ["comer sin lavarse", "no calentar", "sentarse de golpe"],
                   "Pide que explique por qué cada acción va en ese lugar."),
    reinforce="Ordena tres tarjetas de antes de jugar: agua, zapatillas, calentar.",
    extend="Crea una rutina de después para un día de mucho calor en la playa y explícala.",
)

register(
    OA9, 5,
    materials="Tres situaciones escritas en esta clase, una hoja y lápiz. No se necesita ningún material especial.",
    use="Aprenderé a elegir una buena alternativa cuando no tengo todo lo que necesito, respetando a los demás. Sirve para cuidarme en cualquier lugar.",
    prior=["Sé las rutinas de antes y después.", "Sé que cada familia es distinta."],
    explain=[
        "A veces no tenemos todo: no hay jabón, no tenemos fruta, falta agua o no hay toalla. Decidir con contexto es pensar qué puedo hacer con lo que tengo. Una buena alternativa cuida mi salud y respeta a los demás.",
        "Por ejemplo, si no hay jabón, pide ayuda a un adulto para conseguirlo; mientras tanto, usa agua y frota las manos. Si no tienes fruta, un pan o agua también sirven. Si falta una toalla, usa un paño limpio propio. Si no hay agua para tomar, avisa a un adulto: nunca tomes agua de una fuente que no sea segura.",
        "Respetar significa no burlarte de lo que otro trae ni de lo que otro no tiene. Todos tenemos situaciones distintas. Cuando propongas algo, dilo con amabilidad: «¿te sirve esto?». Una buena alternativa es posible y segura.",
    ],
    vocab=[("alternativa", "otra opción posible"), ("contexto", "la situación en que estoy"), ("posible", "que se puede hacer"), ("respetuoso", "que cuida a los demás"), ("seguro", "que no daña")],
    worked=[
        W("Sin jabón", "En el baño del patio no hay jabón después de la clase. ¿Qué alternativa propones?", ["Pienso en lo posible y seguro.", "Aviso a un adulto para que consiga jabón.", "Mientras tanto, me froto las manos con agua y luego las lavo con jabón cuando haya."], "Avisar a un adulto, lavar con agua y completar con jabón después."),
        W("Colación distinta", "Tu amigo trae solo pan y tú traes fruta. ¿Cómo lo tratas?", ["Pienso que su colación sirve.", "No me burlo.", "Si quiero, comparto con amabilidad."], "Con respeto: su colación vale igual."),
    ],
    mistakes=[M("Burlarse de la colación de otro.", "Se compara con lo propio.", "Cada familia come con lo que tiene."),
              M("Tomar agua de cualquier lugar.", "Se tiene mucha sed.", "Pide agua segura a un adulto.")],
    tiers={
        "recovery": [
            ex("Si no hay jabón, ¿avisas a un adulto o lo ignoras?", "Avisas a un adulto", "Él puede conseguirlo."),
            ex("Un pan, ¿es una colación posible?", "Sí", "Es un alimento válido."),
            ex("¿Te burlas de lo que trae otro?", "No", "Burlarse no respeta a la otra persona."),
        ],
        "understand": [
            ex("¿Qué es una alternativa?", "Otra opción posible", "Reemplaza lo que falta."),
            ex("¿Por qué la alternativa debe ser segura?", "Para no dañar a nadie", "Cuidarse es lo primero."),
            ex("¿Una buena alternativa cuida la salud y respeta a los demás?", "Sí", "Son los dos criterios."),
        ],
        "apply": [
            ex("No tienes fruta para la colación pero hay pan y agua. ¿Qué haces?", "Comes el pan y bebes agua", "Es una opción válida."),
            ex("No hay toalla. Tienes un paño limpio propio. ¿Lo usas?", "Sí", "Está limpio y es tuyo."),
            ex("Tienes mucha sed y solo hay una fuente de agua que no sabes si es segura. ¿Qué haces?", "Pides ayuda a un adulto", "Debes asegurarte de que el agua sea segura."),
        ],
        "reason": [
            ex("Dani dice «tu colación es fea». ¿Qué le dices?", "Que cada uno trae lo que puede", "Se respeta lo que cada familia puede traer."),
            ex("Ema propone no lavarse las manos «porque no hay jabón». ¿Es buena alternativa?", "No", "Debe buscar una opción."),
        ],
        "challenge": [
            ex("Tres situaciones: sin jabón, sin fruta, sin toalla. Si propones una alternativa para cada una, ¿cuántas alternativas escribes?", "3", "Una por situación."),
            ex("Haces tu propia alternativa: sin agua para tomar en la plaza. Respuesta posible: avisar a un adulto y pedir agua segura. ¿A quién avisas?", "A un adulto", "Es quien puede conseguirla."),
        ],
    },
    context=[ex("En la plaza se acaba tu agua. Hay una pileta de decoración. ¿Qué haces: A) tomas de la pileta, B) pides ayuda a un adulto, C) corres?", "B", "El agua de una pileta puede no ser segura.")],
    selfcheck=[
        ex("¿Qué haces si no hay jabón?", "Avisas a un adulto", "Un adulto puede conseguirlo para todos."),
        ex("¿Qué es contexto?", "La situación en que estoy", "Depende de lo que tengo."),
        ex("¿Qué tiene que cumplir una buena alternativa?", "Ser posible, segura y respetuosa", "Son sus criterios."),
    ],
    open_task=task("Resuelve estas tres situaciones con una alternativa posible, segura y respetuosa: 1) después de la clase no hay jabón, 2) olvidaste tu colación, 3) un compañero se burla de lo que trae otro niño. Escribe una oración para cada una y cuántas de las tres alternativas cuidan la salud.",
                   "1) Aviso a un adulto y froto con agua hasta tener jabón. 2) Pido a un adulto una fruta o tomo agua. 3) Le digo que cada uno trae lo que puede. Las 3 cuidan la salud y respetan.",
                   ["propone alternativas posibles y seguras", "respeta a los demás", "usa lo que tiene"],
                   ["hoja con tres respuestas", "explicación oral", "dibujo"],
                   ["no pedir ayuda", "burlarse", "tomar agua insegura"],
                   "Elogia la amabilidad y pide un ejemplo de su propia vida."),
    reinforce="Escribe una alternativa cuando falta una toalla.",
    extend="Inventa una situación nueva en que falte algo y propón una alternativa segura.",
)

# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="Un grupo de 3 o 4 personas, un aro, una pelota blanda, un reloj y una hoja. Un adulto como guía.",
    use="Aprenderé a ponernos de acuerdo en una meta y a escuchar a todos. Sirve para jugar en equipo sin peleas.",
    prior=["Sé esperar mi turno.", "Sé escuchar cuando otro habla."],
    explain=[
        "Un equipo es un grupo de personas que trabajan juntas para lograr una meta. Antes de jugar, el equipo necesita acuerdos. Un acuerdo es una decisión que todos entienden y aceptan, como «pasamos la pelota a todos» o «esperamos el turno».",
        "Para definir una meta, el equipo responde: ¿qué queremos lograr? y ¿cómo sabemos que lo logramos? Por ejemplo: «hacer 10 pases sin que caiga la pelota». Escuchar es mirar a quien habla, esperar a que termine y luego decir lo tuyo.",
        "Si alguien no está de acuerdo, se vuelve a conversar con calma. No se grita ni se impone. Todos pueden dar una idea. Al final, se repite el acuerdo en voz alta para que nadie dude.",
    ],
    vocab=[("equipo", "grupo que trabaja junto"), ("meta", "lo que quieren lograr"), ("acuerdo", "decisión que todos aceptan"), ("escuchar", "mirar y esperar mientras otro habla"), ("turno", "momento de cada uno")],
    worked=[
        W("Definir una meta", "Tu equipo tiene una pelota y 4 jugadores. ¿Qué meta clara pueden fijar?", ["Piensan qué se puede medir.", "Dicen: «hacer 10 pases sin que caiga».", "Todos repiten la meta en voz alta."], "Hacer 10 pases sin que caiga la pelota."),
        W("Escuchar", "Ana tiene una idea y Beto habla al mismo tiempo. ¿Qué hace Beto?", ["Se calla un momento.", "Mira a Ana y escucha hasta que termine.", "Después dice su idea."], "Esperar, escuchar y luego hablar."),
    ],
    mistakes=[M("Hablar todos a la vez.", "Todos quieren dar su idea.", "Hablen por turno y escuchen."),
              M("Imponer la idea propia gritando.", "Se piensa que la propia es mejor.", "Propón y escucha; decidan juntos.")],
    tiers={
        "recovery": [
            ex("Un equipo es un grupo que trabaja ¿junto o solo?", "Junto", "La meta es compartida."),
            ex("Un acuerdo lo aceptan ¿todos o uno solo?", "Todos", "Es una decisión del grupo."),
            ex("Para escuchar, ¿miras a quien habla o miras para otro lado?", "Miras a quien habla", "Mirar a quien habla muestra respeto."),
        ],
        "understand": [
            ex("¿Por qué se necesitan acuerdos antes de jugar?", "Para evitar peleas y confusiones", "Todos saben qué hacer."),
            ex("Si alguien no está de acuerdo, ¿se grita o se conversa con calma?", "Se conversa con calma", "Todos pueden opinar."),
            ex("¿Qué hace el equipo al final del acuerdo?", "Lo repite en voz alta", "Para que nadie dude."),
        ],
        "apply": [
            arith("La meta es 10 pases y llevan 7. ¿Cuántos faltan?", "10-7", "Se resta.", " pases"),
            ex("Los acuerdos son: pasar a todos, esperar turno y no gritar. ¿Cuántos acuerdos hay?", "3", "Se cuentan los elementos de la lista."),
            arith("Un equipo de 4 y otro de 3 se juntan. ¿Cuántos jugadores hay?", "4+3", "Se suman.", " jugadores"),
        ],
        "reason": [
            ex("Dani dice «mi idea es la mejor, no escucho a nadie». ¿Qué le dices?", "Que todos pueden dar ideas", "Un equipo escucha."),
            ex("Fito y Gaby discuten fuerte por quién parte. ¿Qué pueden hacer?", "Hablar con calma y turnarse", "Es una solución respetuosa."),
        ],
        "challenge": [
            ex("Escribe una meta con un número para un equipo de 3 que lanza una pelota a un aro. Ejemplo válido: «lograr 6 aciertos entre todos». ¿Cuántos aciertos propone?", "6", "Está en la meta."),
            arith("Tres integrantes hacen 4 lanzamientos cada uno. ¿Cuántos lanzamientos hace el equipo?", "3*4", "Se multiplican.", " lanzamientos"),
        ],
    },
    context=[ex("En el recreo tu grupo discute qué jugar. Cada uno quiere algo distinto. ¿Qué proponen: A) votar o turnarse, B) pelear, C) cada uno se va?", "A", "Resuelven con acuerdo.")],
    selfcheck=[
        ex("¿Qué es una meta?", "Lo que quieren lograr", "Es el objetivo."),
        ex("¿Qué es escuchar?", "Mirar y esperar mientras otro habla", "Escuchar así muestra respeto por el otro."),
        ex("¿Qué es un acuerdo?", "Una decisión que todos aceptan", "Todos la entienden."),
    ],
    open_task=task("Con 3 o 4 personas, elijan una meta de este juego: lanzar una pelota blanda a un aro desde 3 pasos, cada uno 4 veces. Propongan metas posibles (por ejemplo, 6, 8 o 10 aciertos entre todos). Escriban tres acuerdos de convivencia y la meta. Jueguen y anoten cuántos aciertos lograron y si cumplieron los acuerdos.",
                   "Meta: 8 aciertos entre todos. Acuerdos: esperar turno, escuchar y animar. Lograron 9 aciertos y cumplieron los 3 acuerdos.",
                   ["define una meta clara", "escribe acuerdos", "los cumple durante el juego"],
                   ["hoja con meta y acuerdos", "registro de aciertos", "observación de un adulto"],
                   ["gritar o imponer", "no escuchar", "no cumplir acuerdos"],
                   "Reconoce un acuerdo cumplido y pregunta cuál costó más."),
    reinforce="Escribe dos acuerdos para jugar en equipo.",
    extend="Propón una meta más desafiante para el mismo juego y explica cómo la lograrían.",
)

register(
    OA10, 2,
    materials="Cuatro tarjetas de roles escritas aquí (capitán, ayudante de materiales, árbitro amable, animador), 8 conos o botellas, una pelota blanda y un reloj. Para 4 personas.",
    use="Aprenderé a cumplir un rol en el equipo y a rotar los roles sin sentirme mejor ni peor que otros. Sirve para que todos aprendan y aporten.",
    prior=["Sé qué es un equipo.", "Sé esperar mi turno."],
    explain=[
        "Un rol es una responsabilidad que tienes en el juego. Hoy los roles son: capitán, que da las instrucciones del juego con voz clara; ayudante de materiales, que reparte y recoge los conos y la pelota; árbitro amable, que dice si se cumplen las reglas sin retar; y animador, que anima a todos con palabras de apoyo.",
        "Los roles rotan: en cada ronda cada persona cambia de rol. Así todos prueban todo y nadie es más importante. Ningún rol es mejor que otro: todos son necesarios para que el equipo funcione. El rol de ayudante es tan importante como el de capitán.",
        "Para cumplir un rol, escucha las reglas, haz bien tu parte y respeta al otro. Recoger los materiales al final es parte del juego. Si te toca liderar, lo haces con amabilidad y escuchando.",
    ],
    vocab=[("rol", "responsabilidad en el juego"), ("rotar", "cambiar por turnos"), ("capitán", "quien da las instrucciones"), ("árbitro amable", "quien cuida las reglas sin retar"), ("animador", "quien da ánimo")],
    worked=[
        W("Rotar roles", "Hay 4 personas y 4 roles. Después de la ronda 1, cada uno cambia de rol. ¿Cuántas rondas se necesitan para que todos prueben los 4 roles?", ["Cada ronda, cada persona tiene un rol distinto.", "Para probar los 4 roles se necesitan 4 rondas.", "Todos pasan por todos."], "4 rondas."),
        W("Cumplir mi rol", "Eres ayudante de materiales. ¿Qué haces al terminar?", ["Junto los conos y la pelota.", "Los guardo en su lugar.", "Reviso que no quede nada en el suelo."], "Recojo y guardo los materiales."),
    ],
    mistakes=[M("Querer ser siempre el capitán.", "Se piensa que ese rol es el mejor.", "Todos los roles son importantes; rota."),
              M("Retar al compañero como árbitro.", "No se sabe cómo corregir.", "Corrige con amabilidad: «recuerda la regla».")],
    tiers={
        "recovery": [
            ex("Un rol es una...", "Responsabilidad", "Es lo que hago en el equipo."),
            ex("Rotar significa que los roles ¿cambian o se quedan?", "Cambian", "Pasan de uno a otro."),
            ex("El ayudante de materiales recoge los materiales ¿al final o nunca?", "Al final", "Es su tarea."),
        ],
        "understand": [
            ex("¿Por qué rotan los roles?", "Para que todos prueben y aporten", "Así nadie es más importante."),
            ex("¿Hay un rol mejor que los demás?", "No", "Todos son necesarios."),
            ex("¿Cómo corrige un árbitro amable?", "Con amabilidad, sin retar", "Se cuida a los demás."),
        ],
        "apply": [
            ex("Los roles son capitán, ayudante, árbitro y animador. ¿Cuántos roles hay?", "4", "Se cuentan los elementos de la lista."),
            arith("En 4 rondas, cada una dura 20 segundos de acción. ¿Cuántos segundos de acción son?", "4*20", "Se multiplican.", " segundos"),
            ex("Ema fue capitán en la ronda 1. ¿Puede repetir capitán en la ronda 2 si hay rotación?", "No", "Debe cambiar de rol."),
        ],
        "reason": [
            ex("Beto dice «yo siempre soy capitán porque soy el mejor». ¿Qué le dices?", "Que los roles rotan y todos son importantes", "Nadie es más que otro."),
            ex("Caro es animadora y dice a un compañero que falló «¡buen intento!». ¿Cumple su rol?", "Sí", "Anima con palabras de apoyo."),
        ],
        "challenge": [
            arith("El equipo recoge 8 conos entre 4 personas, cada una la misma cantidad. ¿Cuántos conos recoge cada una?", "8//4", "Se reparte en partes iguales.", " conos"),
            ex("Si 4 personas rotan por 4 roles en 4 rondas, ¿cuántos turnos de rol hay en total?", "16", "4 personas por 4 rondas son 16."),
        ],
    },
    context=[ex("En tu casa juegan 4 primos a lanzar calcetines a un cesto. Uno quiere mandar siempre. ¿Qué proponen: A) rotar roles, B) que se vaya, C) pelear?", "A", "Rotar da oportunidad a todos.")],
    selfcheck=[
        ex("¿Qué hace el animador?", "Anima a todos", "Es su rol."),
        ex("¿Rotan los roles?", "Sí", "Para que todos aprendan."),
        ex("¿Quién recoge los materiales?", "El ayudante, con todos", "Es parte del juego."),
    ],
    open_task=task("Con 4 personas, jueguen 4 rondas de 20 segundos de acción con 20 de pausa: lanzar la pelota a un aro desde 3 pasos. Roles: capitán, ayudante de materiales, árbitro amable y animador. Al final de cada ronda, roten. Anoten quién tuvo cada rol en cada ronda y cuántos aciertos lograron.",
                   "Ronda 1: yo capitán, Ana ayudante, Beto árbitro, Caro animadora. Rotamos cada ronda. Lograron 5, 6, 7 y 7 aciertos. Todos probamos los 4 roles.",
                   ["cumple el rol asignado", "rota sin discutir", "respeta a todos"],
                   ["tabla de roles por ronda", "registro de aciertos", "observación de un adulto"],
                   ["no rotar", "retar al árbitro", "no recoger materiales"],
                   "Reconoce los cuatro roles y pide decir cuál disfrutó más."),
    reinforce="Escribe los 4 roles y una tarea de cada uno.",
    extend="Agrega un quinto rol, como cronometrador, y define su tarea.",
)

register(
    OA10, 3,
    materials="Una pelota blanda, 4 conos, un aro y una hoja con tres frases de ejemplo (en esta clase). Para 3 o 4 personas.",
    use="Aprenderé a dar y recibir consejos amables y concretos. Sirve para mejorar juntos en vez de criticar.",
    prior=["Sé qué es un equipo.", "Sé escuchar."],
    explain=[
        "Un consejo útil es amable, concreto y se puede aplicar. Tiene tres partes: «Me gustó que…», «Podrías…» y «Así…». Por ejemplo: «Me gustó que miraste a tu compañero; podrías lanzar más suave; así llegará más fácil». Un consejo no dice «lo haces mal» ni se burla.",
        "Para dar un consejo, observa algo específico, como la mirada, la fuerza o la posición. Habla con voz suave y mira a la persona. Para recibirlo, escucha hasta el final, di «gracias» y prueba el cambio. Si no entiendes, puedes preguntar «¿cómo?».",
        "Los consejos son para ayudar, no para ganar. Se dan uno a la vez, y mejor si son pocos y claros. Después de probar el cambio, se conversa si ayudó. Todos damos y recibimos consejos.",
    ],
    vocab=[("consejo", "idea para mejorar"), ("concreto", "claro y específico"), ("amable", "con buen trato"), ("recibir", "escuchar y aceptar"), ("probar", "intentar de nuevo con el cambio")],
    worked=[
        W("Dar un consejo", "Ana lanza muy fuerte y la pelota se va lejos. ¿Cómo le das un consejo con las tres partes?", ["«Me gustó que miras el aro.»", "«Podrías lanzar más suave.»", "«Así la pelota llegará al aro.»"], "Me gustó que miras el aro; podrías lanzar más suave; así llegará al aro."),
        W("Recibir un consejo", "Un compañero te dice: «podrías doblar las rodillas al saltar». ¿Qué haces?", ["Escucho hasta el final.", "Digo «gracias».", "Pruebo doblar las rodillas."], "Escucho, agradezco y pruebo."),
    ],
    mistakes=[M("Decir «lo haces mal».", "Se critica sin ayudar.", "Di qué podrías cambiar y para qué."),
              M("Dar muchos consejos a la vez.", "Se quiere ayudar mucho.", "Da uno o dos, claros.")],
    tiers={
        "recovery": [
            ex("Un consejo útil es ¿amable o burlón?", "Amable", "Ayuda a mejorar."),
            ex("La primera parte del consejo es «Me gustó que...». ¿Dice algo bueno o malo?", "Algo bueno", "Parte reconociendo algo."),
            ex("Cuando recibes un consejo, dices...", "Gracias", "Agradecer es una forma respetuosa de recibir."),
        ],
        "understand": [
            ex("¿Cuáles son las tres partes del consejo?", "Me gustó que, podrías y así", "Son las partes de la clase."),
            ex("¿Qué es un consejo concreto?", "Claro y específico", "Dice qué cambiar."),
            ex("¿Para qué se da un consejo?", "Para ayudar a mejorar", "No es para ganar."),
        ],
        "apply": [
            ex("Dani saltó con las piernas rectas. ¿Cuál es el consejo concreto: A) «salta mal», B) «podrías doblar las rodillas, así caerás más suave»?", "B", "Dice qué cambiar y para qué."),
            ex("Completa: «Me gustó que ____ ; podrías ____ ; así ____». ¿Cuántas partes tiene?", "3", "Las tres partes del consejo son tres."),
            arith("Das 2 consejos a cada uno de 3 compañeros. ¿Cuántos consejos das?", "2*3", "Se multiplican.", " consejos"),
        ],
        "reason": [
            ex("Beto dice «lo haces horrible». ¿Es un consejo útil?", "No", "No es concreto ni amable."),
            ex("Ema recibe un consejo, dice «gracias» y lo prueba. ¿Qué hizo bien?", "Escuchar, agradecer y probar", "Esos son los tres pasos."),
        ],
        "challenge": [
            ex("Escribe un consejo con las tres partes para alguien que lanza a un aro y falla por fuerza. Ejemplo: «Me gustó que miras al aro; podrías lanzar más suave; así acertarás». ¿Cuántas partes tiene?", "3", "Las tres partes del consejo son tres."),
            arith("En 4 rondas de 50 segundos de acción, ¿cuántos segundos de acción hay?", "4*50", "Se multiplican.", " segundos"),
        ],
    },
    context=[ex("Un amigo se frustra porque la pelota no entra al aro. ¿Qué le dices: A) «eres malo», B) «me gustó que lo intentaste; podrías lanzar más suave; así entrará», C) nada?", "B", "Es amable, concreto y útil.")],
    selfcheck=[
        ex("¿Qué dices después de recibir un consejo?", "Gracias", "Agradecer es una forma respetuosa de recibir."),
        ex("¿Cuántas partes tiene el consejo?", "3", "Me gustó, podrías, así."),
        ex("¿Se puede burlar al dar un consejo?", "No", "Debe ser amable."),
    ],
    open_task=task("Con un compañero, lancen una pelota blanda a un aro desde 3 pasos, 5 veces cada uno. Después de los 5 lanzamientos, cada uno da un consejo al otro con las tres partes («Me gustó que…», «Podrías…», «Así…»). Prueben el consejo en 5 lanzamientos más y anoten si hubo más aciertos.",
                   "Ana me dijo: «Me gustó que miras al aro; podrías lanzar más suave; así acertarás». Primero hice 2 aciertos; después del consejo hice 4.",
                   ["da un consejo amable y concreto", "recibe con respeto", "prueba el cambio"],
                   ["consejos escritos", "registro de aciertos", "observación de un adulto"],
                   ["criticar sin ayudar", "no escuchar", "burlarse"],
                   "Reconoce el consejo concreto y pide explicar qué cambió."),
    reinforce="Escribe un consejo con las tres partes para alguien que salta.",
    extend="Da un consejo a un adulto sobre cómo lanzar suave y pídele uno a cambio.",
)

register(
    OA10, 4,
    materials="8 conos, una pelota blanda, un aro, una cuerda, un reloj y una hoja con una tabla de roles. Para 4 personas.",
    use="Aprenderé a completar un desafío entre todos y a evaluar cómo aportó cada rol. Sirve para reconocer lo que cada uno hace por el equipo.",
    prior=["Sé los roles del equipo.", "Sé dar un consejo amable."],
    explain=[
        "Un desafío cooperativo es una tarea que solo se logra si todos colaboran. Hoy el desafío es: llevar 8 conos de un lado al otro del cuadrado de 4 × 4 m y formar una torre de 4 conos y otra de 4 conos, en 80 segundos. Solo se puede llevar un cono por persona y se camina.",
        "Cada rol aporta: el capitán da las instrucciones; el ayudante organiza los conos; el árbitro amable cuida las reglas; el animador da ánimo. Si un rol falla, el equipo lo nota. Pero ningún rol es más importante que otro.",
        "Al terminar, evalúan con tres preguntas: ¿cumplimos la meta?, ¿qué hizo cada rol?, ¿qué haremos mejor la próxima vez? Se responde con ejemplos concretos y se agradece a cada persona.",
    ],
    vocab=[("desafío cooperativo", "tarea que se logra entre todos"), ("evaluar", "mirar cómo resultó"), ("aportar", "dar algo al equipo"), ("torre", "conos puestos uno sobre otro"), ("agradecer", "decir gracias")],
    worked=[
        W("Repartir los conos", "Hay 8 conos y 4 personas. Si cada persona lleva la misma cantidad, ¿cuántos lleva cada una?", ["Divido 8 entre 4.", "8 ÷ 4 = 2.", "Cada persona lleva 2 conos."], "2 conos cada una."),
        W("Evaluar un rol", "El animador dijo «¡vamos, tú puedes!» cuando se cayó una torre. ¿Qué aportó?", ["Dio ánimo.", "Ayudó a que el equipo intentara otra vez.", "Cumplió su rol."], "Dio ánimo para seguir intentando."),
    ],
    mistakes=[M("Culpar a un compañero cuando la torre cae.", "Se siente frustración.", "Pregunten qué pueden mejorar entre todos."),
              M("Hacer todo uno solo.", "Se quiere terminar rápido.", "El desafío es del equipo: cada uno hace su parte.")],
    tiers={
        "recovery": [
            ex("Un desafío cooperativo se logra ¿entre todos o uno solo?", "Entre todos", "Todos colaboran para lograr la tarea."),
            ex("El animador ¿anima o critica?", "Anima", "Es su rol."),
            ex("Al terminar, ¿se agradece a los compañeros o no?", "Se agradece", "Escuchar así muestra respeto por el otro."),
        ],
        "understand": [
            ex("¿Para qué se evalúa el desafío?", "Para ver qué mejorar", "Así se aprende para la próxima vez."),
            ex("Si la torre cae, ¿se culpa a alguien o se piensa cómo mejorar?", "Se piensa cómo mejorar", "El equipo aprende."),
            ex("¿Hay un rol más importante?", "No", "Todos los roles aportan al equipo."),
        ],
        "apply": [
            arith("Hay 8 conos y 4 personas. ¿Cuántos lleva cada una?", "8//4", "Se divide en partes iguales.", " conos"),
            arith("Hacen 2 torres de 4 conos. ¿Cuántos conos usaron?", "2*4", "Se multiplican.", " conos"),
            arith("Tienen 80 segundos y ya pasaron 50. ¿Cuántos faltan?", "80-50", "Se resta.", " segundos"),
        ],
        "reason": [
            ex("Beto dice «Dani tiró la torre, es su culpa». ¿Qué respondes?", "Que lo arreglen juntos", "El desafío es del equipo."),
            ex("Ema armó todas las torres sola. ¿Cumple el desafío cooperativo?", "No", "Debe participar todo el equipo."),
        ],
        "challenge": [
            ex("Cuatro personas, cuatro roles, un desafío de 80 segundos. ¿Cuántas preguntas tiene la evaluación?", "3", "Son tres preguntas."),
            arith("Repiten el desafío 3 veces con 80 segundos de acción cada una. ¿Cuántos segundos de acción son?", "3*80", "Se multiplican.", " segundos"),
        ],
    },
    context=[ex("En casa tus primos y tú arman una torre de vasos de plástico entre todos. La torre se cae. ¿Qué haces: A) culpas a alguien, B) dicen «otra vez» y piensan cómo hacerlo mejor, C) se van?", "B", "El equipo intenta de nuevo.")],
    selfcheck=[
        ex("¿Cuántos conos hay en el desafío?", "8", "Dos torres de 4."),
        ex("¿Qué se pregunta al evaluar?", "Si cumplimos la meta, qué hizo cada rol y qué mejorar", "Son las tres preguntas."),
        ex("¿Se culpa a alguien?", "No", "Se mejora entre todos."),
    ],
    open_task=task("Con 4 personas, hagan el desafío: llevar 8 conos al otro lado del cuadrado de 4 × 4 m y armar dos torres de 4 conos en 80 segundos. Roles: capitán, ayudante, árbitro amable y animador. Al final respondan: ¿cumplimos la meta?, ¿qué hizo cada rol?, ¿qué haremos mejor? Escriban una frase de agradecimiento para cada persona.",
                   "Lo logramos en 75 segundos. El capitán dio instrucciones, el ayudante organizó los conos, el árbitro cuidó que se caminara y la animadora dio ánimo. La próxima vez hablaremos más claro. Gracias a todos.",
                   ["cumple su rol", "evalúa con las tres preguntas", "agradece al equipo"],
                   ["hoja con preguntas respondidas", "observación de un adulto", "frases de agradecimiento"],
                   ["culpar", "hacer todo solo", "no evaluar"],
                   "Pide un ejemplo de aporte de cada rol y celebra el esfuerzo del equipo."),
    reinforce="Reparte 8 objetos pequeños entre 4 personas, en partes iguales.",
    extend="Aumenta el desafío a 12 conos con 3 torres de 4 conos y 120 segundos; ¿cuántos conos lleva cada persona de 4?",
)
