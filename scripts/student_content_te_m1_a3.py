"""Cuaderno del estudiante, 1.º medio Tecnología: OA 05 (evolución de productos tecnológicos y entornos, clases 1 a 5) y OA 06 (efectos sociales de la evolución tecnológica, clases 1 a 4).

Seguridad: las tareas son de lectura, cálculo y escritura; no se manipulan herramientas ni materiales.
Cifras enteras. Los datos de tablas, ventas, pesos, precios y encuestas son inventados («de ejemplo») para practicar; no se usan fechas ni años exactos. Los productos se nombran por tipo (celular, ampolleta, lámpara), sin marcas.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te_m1_a import reg
from student_lessons import arith, ex

OA5 = "TE1M OA 05"
OA6 = "TE1M OA 06"

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a describir cómo evoluciona un producto tecnológico con una línea de tiempo, a distinguir lo que se conserva de lo que cambia y a reconocer cambios graduales y cambios de fondo. Sirve para entender de dónde vienen los objetos que usamos.",
    prior=["Sé que un producto tecnológico resuelve una necesidad.", "Sé calcular porcentajes.", "Sé leer una tabla sencilla."],
    explain=[
        "Un producto tecnológico evoluciona cuando sus versiones sucesivas cambian en forma, materiales, tamaño, energía, costo o manera de usarse. A menudo sigue cumpliendo la misma función. Por ejemplo, la lámpara de aceite, la ampolleta incandescente y la luz LED sirven para iluminar, pero cambiaron la energía que usan y cuánto duran.",
        "La evolución se estudia con una línea de tiempo, que ordena las versiones de la más antigua a la más reciente e indica qué cambió en cada paso. Se distingue lo que se conserva (la necesidad y la función) de lo que cambia (las características). Un cambio gradual mejora una versión anterior: la hace más liviana, más barata o más duradera. Un cambio de fondo es una forma nueva de resolver la necesidad, como pasar de la carta en papel al mensaje digital.",
        "Cada versión se apoya en los conocimientos y materiales de las anteriores, por eso el orden importa. Lo nuevo no siempre reemplaza del todo a lo antiguo: a veces conviven. Para describir una evolución se nombra el producto y su necesidad, se ordenan las versiones, se anotan tres características que cambian y se escribe una conclusión.",
    ],
    vocab=[("evolución", "cambio de un producto a través de versiones sucesivas"), ("versión", "forma que tiene un producto en un momento"), ("función", "para qué sirve un producto"), ("característica", "rasgo de un producto, como su peso, su energía o su costo"), ("cambio gradual", "mejora de una versión anterior"), ("cambio de fondo", "forma nueva de resolver la misma necesidad"), ("línea de tiempo", "orden de las versiones en el tiempo")],
    worked=[
        ("Ordenar una evolución", "Ordena de la más antigua a la más reciente: luz LED, lámpara de aceite, ampolleta incandescente.", ["La lámpara de aceite es la más antigua.", "La ampolleta incandescente la reemplazó, y la luz LED llegó después."], "Lámpara de aceite, ampolleta incandescente, luz LED"),
        ("Qué se conserva y qué cambia", "Del teléfono fijo al teléfono celular, ¿qué se conserva y qué cambia?", ["Se conserva la necesidad: hablar con alguien a distancia.", "Cambia la conexión: ya no depende de un cable ni de un lugar fijo."], "Se conserva la función de comunicarse a distancia; cambia que ya no depende de un cable"),
    ],
    mistakes=[
        ("Ordenar las versiones por precio o por tamaño.", "Eso no dice cuándo apareció cada versión.", "Ordena por época y anota después las características."),
        ("Creer que un producto nuevo no tiene relación con los anteriores.", "Cada versión se apoya en conocimientos y materiales previos.", "Busca qué heredó la versión nueva de la anterior."),
    ],
    R=[
        ("Una línea de tiempo muestra A) las versiones de un producto en orden B) cuánto cuesta cada versión", "A", "Su función es ordenar en el tiempo."),
        ("Pasar de la carta en papel al mensaje digital, ¿es un cambio gradual o un cambio de fondo?", "Un cambio de fondo", "Cambia la forma de resolver la necesidad de comunicarse por escrito."),
        ("En la evolución de la lámpara de aceite a la luz LED, ¿qué función se conserva? A) iluminar B) calentar", "A", "Todas sirven para dar luz."),
    ],
    C=[
        ("Una nueva linterna es más liviana y gasta menos pilas, pero sigue sirviendo para alumbrar. ¿Es un cambio gradual o de fondo?", "Gradual", "Mejora lo anterior sin cambiar la forma de resolver la necesidad."),
        ("Del casete al archivo de música digital cambia la forma de guardar y escuchar música. ¿Qué se conserva? A) la necesidad de escuchar música B) el material de la cinta", "A", "La necesidad es la misma aunque cambie la tecnología."),
        ("Ordena por época: reproductor de archivos digitales, disco de vinilo y casete.", "Disco de vinilo, casete, reproductor de archivos digitales", "Cada formato apareció después del anterior."),
    ],
    A=[
        arith("Versiones de un teléfono (datos de ejemplo): la versión 1 pesa 2.000 gramos y la versión 3 pesa 150 gramos. ¿Cuántos gramos bajó el peso?", "2000-150", "Se resta el peso de la versión 3 al de la versión 1.", " gramos"),
        arith("Un teléfono de ejemplo pasó de 500 gramos en su versión 2 a 150 gramos en su versión 3. ¿Qué porcentaje bajó su peso?", "(500-150)*100//500", "La diferencia se calcula sobre el peso antiguo.", " %"),
        ("Una radio cambia de pilas a batería recargable y de 800 g a 300 g, pero sigue teniendo un solo parlante. ¿Cuántas de estas tres características cambiaron: energía, peso y número de parlantes?", "2", "Cambiaron la energía y el peso; el número de parlantes se mantuvo."),
    ],
    Z=[
        ("Un grupo afirma: «El celular reemplazó por completo al teléfono fijo, así que ya no se parecen en nada». ¿Qué error tiene? A) ambos resuelven la misma necesidad de comunicarse a distancia B) los dos usan cables", "A", "Aunque cambió la tecnología, la función se conserva."),
        ("Alguien ordena las versiones de una cámara por precio y no por época. ¿Por qué eso no sirve para una línea de tiempo?", "El precio no indica cuándo apareció cada versión", "La línea de tiempo se ordena por época."),
    ],
    D=[
        arith("Un producto de ejemplo tuvo 4 versiones y en cada una pesó 100 gramos menos que en la anterior. La versión 1 pesaba 700 gramos. ¿Cuánto pesa la versión 4?", "700-3*100", "Hubo 3 cambios de 100 gramos entre la versión 1 y la 4.", " gramos"),
        ex("Costos de fabricar tres versiones de un producto (datos de ejemplo): $80.000, $60.000 y $54.000. ¿Entre cuáles versiones bajó más el costo, en porcentaje, y cuánto?", "Entre la 1 y la 2, 25 %", "De 80.000 a 60.000 bajó 25 %; de 60.000 a 54.000 bajó 10 %.", calc="(80000-60000)*100//80000"),
    ],
    ctx=arith("Un reproductor de música de ejemplo pesaba 400 gramos en su primera versión y pesa 100 gramos en la tercera. ¿Cuántas veces cabe el peso actual en el peso de la primera versión?", "400//100", "Se divide 400 entre 100.", " veces"),
    sc=[
        ("En Tecnología: ¿Qué es una línea de tiempo?", "Un orden de las versiones desde la más antigua a la más reciente", "Muestra cómo cambia un producto."),
        ("¿Qué es un cambio de fondo?", "Una forma nueva de resolver la misma necesidad", "Cambia el modo de resolverla, no solo mejora una versión."),
        ("¿Qué se conserva en la evolución de un producto?", "La necesidad y la función", "Aunque cambien las características."),
    ],
    open_task=(
        "Escoge un producto con estas etapas de ejemplo. A) Iluminación: lámpara de aceite, ampolleta incandescente, ampolleta fluorescente compacta, luz LED. B) Registro de imágenes: cámara de película, cámara digital, cámara del celular. C) Comunicación escrita: carta en papel, mensaje digital, mensaje con imágenes y voz. Escribe la línea de tiempo con una característica que cambia entre cada paso (por ejemplo energía, tamaño, costo o forma de uso), la función que se conserva y cuál paso consideras un cambio de fondo, con una razón.",
        "A: lámpara de aceite (luz con llama, se agota el combustible), ampolleta incandescente (usa electricidad), fluorescente compacta (gasta menos energía), LED (gasta menos energía y dura más). Se conserva la función de iluminar. Cambio de fondo: de la llama a la electricidad, porque cambia la forma de producir la luz",
        ["ordena las etapas", "anota una característica que cambia entre pasos", "indica la función que se conserva", "señala un cambio de fondo y lo justifica"],
        ["línea de tiempo escrita con conclusión"],
        ["ordenar por precio", "no distinguir lo que se conserva de lo que cambia"],
        "Pregunta: «¿para qué sirve el producto en todas las etapas?». La respuesta es la función que se conserva.",
    ),
    reinforce="Elige un objeto de tu casa y pregunta a una persona mayor cómo era antes; anota tres características que cambiaron.",
    extend="Explica por qué conviven a veces un producto nuevo y uno antiguo que cumplen la misma función.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a identificar los factores que influyen en el cambio de los productos tecnológicos: científicos y técnicos, económicos, sociales y culturales, ambientales y legales. Sirve para explicar por qué un producto cambia y no solo cómo.",
    prior=["Sé ordenar una evolución en una línea de tiempo.", "Sé distinguir cambio gradual de cambio de fondo.", "Sé calcular porcentajes."],
    explain=[
        "Los productos no cambian por azar: influyen factores, que son las condiciones que empujan o frenan un cambio. Los factores científicos y técnicos son los nuevos conocimientos, materiales y máquinas, como baterías más pequeñas o plásticos más resistentes. Los factores económicos son los costos de producir, los precios, la competencia entre fabricantes y los ingresos de las personas.",
        "Los factores sociales y culturales son las necesidades, costumbres y modas de las personas: si más gente trabaja lejos de casa, crece el comercio a domicilio. Los factores ambientales son la escasez de recursos, los residuos y el cambio climático, que impulsan productos que gastan menos. Los factores políticos y legales son las leyes, normas y políticas públicas, que pueden exigir, prohibir o fomentar un producto.",
        "Casi siempre actúan varios factores a la vez y se refuerzan. Para analizar un cambio se pregunta: ¿qué lo hizo posible (técnico)?, ¿qué lo hizo rentable o accesible (económico)?, ¿quién lo quería (social)?, ¿qué lo permitió o lo exigió (legal)? y ¿qué problema ambiental lo empujó? Un factor puede acelerar un cambio o frenarlo.",
    ],
    vocab=[("factor", "condición que empuja o frena un cambio"), ("factor técnico", "nuevo conocimiento, material o máquina"), ("factor económico", "costo, precio, competencia o ingresos"), ("factor social y cultural", "necesidades, costumbres y modas de las personas"), ("factor ambiental", "escasez de recursos, residuos o clima"), ("factor legal", "ley o norma que exige, prohíbe o fomenta")],
    worked=[
        ("Clasificar factores", "Clasifica: (a) aparece un material más liviano que permite fabricar bicicletas más livianas, (b) una norma exige que los electrodomésticos indiquen cuánta energía gastan.", ["(a) es un nuevo material: factor técnico.", "(b) es una norma que obliga: factor legal."], "(a) técnico, (b) legal"),
        ("Reconocer varios factores", "Los celulares con cámara se hicieron comunes porque (a) las cámaras se volvieron pequeñas y baratas y (b) la gente quería compartir fotos al instante. ¿Qué factores hay?", ["(a) habla de tecnología y de costo: técnico y económico.", "(b) habla de lo que quieren las personas: social y cultural."], "Técnico, económico y social y cultural"),
    ],
    mistakes=[
        ("Atribuir un cambio a un solo factor.", "Los cambios suelen tener varias causas que actúan juntas.", "Revisa los cinco tipos de factor antes de concluir."),
        ("Confundir factor con efecto.", "El factor empuja el cambio; el efecto es lo que ocurre después.", "Pregunta: ¿esto causó el cambio o es una consecuencia?"),
    ],
    R=[
        ("Un nuevo material resistente permite fabricar cascos más livianos. ¿Qué factor es? A) técnico B) legal", "A", "Es un avance en materiales."),
        ("Una norma de ejemplo exige cinturón de seguridad en todos los asientos de un bus. ¿Qué tipo de factor es?", "Político y legal", "Una norma obliga a incorporar el cinturón."),
        ("Cuando baja el costo de fabricar un producto, ¿qué tipo de factor actúa?", "Económico", "El costo es un factor económico."),
    ],
    C=[
        ("Una persona compra por celular porque termina de trabajar tarde. ¿Qué factor explica mejor su hábito? A) social y cultural B) ambiental", "A", "Depende de su forma de vivir."),
        ("Se agotan ciertos recursos y las empresas diseñan productos que gastan menos materiales. ¿Qué factor actúa?", "Ambiental", "El problema que empuja el cambio son los recursos."),
        ("Un celular con cámara se volvió común porque las cámaras bajaron de precio y la gente quería compartir fotos. ¿Cuántos tipos de factor aparecen?", "2", "Uno económico y uno social y cultural."),
    ],
    A=[
        ("Clasifica cada hecho como técnico, económico, social, ambiental o legal: (1) baterías más pequeñas y duraderas, (2) un precio más bajo por la competencia entre fabricantes, (3) una ley que exige que los juguetes cumplan una norma de seguridad, (4) la costumbre de ver videos en el celular.", "1 técnico, 2 económico, 3 legal, 4 social", "Cada hecho corresponde a una de las categorías de la explicación."),
        arith("El costo de fabricar un producto de ejemplo bajó de $50.000 a $30.000. ¿Qué porcentaje bajó?", "(50000-30000)*100//50000", "La diferencia se calcula sobre el costo antiguo.", " %"),
        ex("En una encuesta de ejemplo a 50 personas, 35 dicen que compran por celular porque no tienen tiempo de ir a la tienda. ¿Qué porcentaje es y qué tipo de factor muestra?", "70 %; social y cultural", "35 × 100 ÷ 50 = 70, y habla de hábitos y de tiempo disponible.", calc="35*100//50"),
    ],
    Z=[
        ("Una tecnología nueva ya es posible pero tan cara que casi nadie la compra. ¿Qué factor frena su difusión? A) económico B) ambiental", "A", "El alto costo limita las compras."),
        ("Dos explicaciones de por qué se difundió el correo electrónico. Explicación 1: solo porque alguien lo inventó. Explicación 2: porque era técnicamente posible, barato y la gente necesitaba comunicarse rápido. ¿Cuál es mejor?", "La 2", "Reúne varios factores y no depende de una sola causa."),
    ],
    D=[
        arith("Cuando bajó el costo de un producto de ejemplo, sus ventas subieron de 800 a 1.200 unidades al mes. ¿Qué porcentaje aumentaron?", "(1200-800)*100//800", "Aumentaron 400 unidades sobre las 800 iniciales.", " %"),
        ("Una innovación se difunde si hay al menos 3 factores a favor. Hay precio bajo, tecnología disponible y moda a favor, y una norma que prohíbe parte de su uso. ¿Se difunde?", "Sí", "Hay 3 factores a favor, que alcanzan el mínimo."),
    ],
    ctx=ex("En un barrio de ejemplo, las bicicletas eléctricas subieron de 40 a 100 cuando bajó su precio. ¿Cuántas más hay y qué tipo de factor explica el aumento?", "60 más; económico", "100 − 40 = 60, y lo que cambió fue el precio.", calc="100-40"),
    sc=[
        ("¿Qué es un factor?", "Una condición que empuja o frena un cambio", "Ayuda a explicar por qué cambia un producto."),
        ("¿Una ley que prohíbe un producto es un factor técnico o legal?", "Legal", "Las leyes son factores políticos y legales."),
        ("¿Suele haber un solo factor detrás de un cambio?", "No, suelen actuar varios", "Se refuerzan entre sí."),
    ],
    open_task=(
        "Escoge un cambio. A) Las bolsas plásticas se reemplazaron en el comercio por bolsas de tela o papel (norma de ejemplo). B) Los celulares pasaron de tener teclas a tener pantalla táctil. C) Los repartos a domicilio aumentaron. Escribe al menos un factor de tres tipos distintos que ayudan a explicar el cambio, con una frase para cada uno, y señala cuál crees que pesó más y por qué.",
        "A: legal, una norma prohíbe entregar bolsas plásticas; ambiental, se acumulan residuos; social, las personas se acostumbran a llevar su propia bolsa. Pesó más la norma porque obligó al cambio",
        ["identifica tres tipos de factor", "los explica con una frase cada uno", "elige el de más peso y lo justifica"],
        ["lista de factores con su justificación"],
        ["usar un solo factor", "confundir un efecto con un factor"],
        "Pregunta: «¿esto causó el cambio o vino después?». Si vino después, es un efecto.",
    ),
    reinforce="Elige un producto que usas y anota un factor técnico y uno económico que crees que lo hizo cambiar.",
    extend="Explica cómo un factor legal puede frenar un producto que es técnica y económicamente posible.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir los entornos natural, construido y digital, y a ver cómo los productos y los entornos se influyen. Sirve para entender que la tecnología cambia los lugares donde vivimos.",
    prior=["Sé qué es un factor de cambio.", "Sé calcular porcentajes.", "Sé leer datos simples."],
    explain=[
        "Un entorno es el espacio en que las personas viven y usan la tecnología. El entorno natural es el paisaje, el agua, el aire y los seres vivos. El entorno construido es lo que las personas edifican: casas, calles, edificios, puentes y redes de transporte. El entorno digital son las redes, plataformas y servicios en línea donde se comunica, se compra y se estudia.",
        "Los entornos también evolucionan. La ciudad agrega ciclovías y semáforos, el campo incorpora riego más eficiente y el entorno digital suma más servicios cada año. Productos y entornos se influyen entre sí. El automóvil cambió el diseño de las calles. Internet creó servicios que antes solo existían en oficinas. Y un cambio del entorno exige productos nuevos: al construirse ciclovías aparecieron luces y cascos para bicicletas.",
        "Para analizar la relación se nombra el entorno, el producto y quién influye en quién: el producto puede cambiar el entorno, o el entorno puede exigir un producto. Los entornos tienen límites, como el espacio, la energía y el acceso, y esos límites orientan la evolución de los productos.",
    ],
    vocab=[("entorno", "espacio en que las personas viven y usan la tecnología"), ("entorno natural", "paisaje, agua, aire y seres vivos"), ("entorno construido", "casas, calles, edificios y redes de transporte"), ("entorno digital", "redes, plataformas y servicios en línea"), ("influir", "producir un cambio en otra cosa")],
    worked=[
        ("Clasificar entornos", "Clasifica: (a) una ciclovía, (b) un sitio de trámites en línea.", ["(a) es una obra que las personas construyeron: entorno construido.", "(b) es un servicio en una red: entorno digital."], "(a) construido, (b) digital"),
        ("Quién influye en quién", "Se construyen ciclovías en una comuna y aparecen tiendas que arriendan bicicletas. ¿Quién influyó en quién?", ["Primero cambió el entorno: se construyeron las ciclovías.", "Después apareció un servicio que antes no hacía falta."], "El cambio del entorno construido impulsó un servicio nuevo"),
    ],
    mistakes=[
        ("Pensar que el entorno es solo la naturaleza.", "También hay un entorno construido y uno digital.", "Revisa los tres tipos antes de clasificar."),
        ("Creer que un producto nuevo no cambia el lugar donde se usa.", "Muchos productos cambian calles, casas, hábitos y servicios.", "Pregunta qué cambió en el lugar después del producto."),
    ],
    R=[
        ("Un bosque nativo, ¿es entorno natural, construido o digital?", "Natural", "Lo formó la naturaleza."),
        ("Una plataforma en línea para pedir horas médicas es parte del A) entorno digital B) entorno natural", "A", "Es un servicio en una red."),
        ("Un puente sobre un río, ¿es entorno natural o construido?", "Construido", "Las personas lo edificaron."),
    ],
    C=[
        ("Aparece un servicio en línea para pedir transporte y cambia cómo se mueven las personas en la ciudad. ¿Qué influyó en qué?", "Un producto digital cambió la movilidad en la ciudad", "El servicio digital modificó el entorno construido."),
        ("Cuando una ciudad crece, hacen falta más buses. ¿Quién exige a quién? A) el entorno exige nuevos productos B) los productos nuevos aparecen sin relación con el entorno", "A", "El crecimiento genera la necesidad."),
        ("¿Cuál es un cambio del entorno digital? A) más servicios que se pueden hacer desde casa B) un camino pavimentado", "A", "Los servicios en línea pertenecen al entorno digital."),
    ],
    A=[
        ("Clasifica cada elemento como natural, construido o digital: (1) un humedal, (2) una aplicación de mapas, (3) una calle con semáforos.", "1 natural, 2 digital, 3 construido", "Cada uno pertenece a un entorno distinto."),
        arith("Una comuna de ejemplo tenía 8 km de ciclovías y hoy tiene 20 km. ¿Qué porcentaje aumentaron?", "(20-8)*100//8", "Aumentó 12 km sobre los 8 km iniciales.", " %"),
        ex("En un barrio de ejemplo, 60 de 80 trámites se hacen ahora en línea. ¿Qué porcentaje es y qué entorno ha crecido?", "75 %; el entorno digital", "60 × 100 ÷ 80 = 75, y los trámites en línea son parte del entorno digital.", calc="60*100//80"),
    ],
    Z=[
        ("Alguien dice: «El entorno digital no afecta a la ciudad porque no se puede tocar». ¿Qué respondes? A) los servicios en línea cambian cómo se mueven y compran las personas en la ciudad B) tiene razón", "A", "Aunque no se toque, modifica la vida en el entorno construido."),
        ("«Los autos cambiaron el diseño de las calles». ¿Qué relación muestra? A) un producto cambió el entorno construido B) un entorno natural cambió un producto", "A", "El automóvil modificó las calles."),
    ],
    D=[
        arith("Una ciudad de ejemplo tenía 2 rutas de bus y agrega 1 ruta cada 3 meses. ¿Cuántas rutas tendrá en 2 años?", "2+24//3", "En 24 meses se agregan 8 rutas a las 2 iniciales.", " rutas"),
        arith("El entorno digital de un colegio de ejemplo ofrece 5 trámites en línea y se agregan 3 por año. ¿En cuántos años tendrá 20 trámites?", "(20-5)//3", "Faltan 15 trámites y se agregan 3 por año.", " años"),
    ],
    ctx=ex("En un pueblo de ejemplo, 96 de 120 familias usan un servicio de pago en línea que antes se hacía en una oficina. ¿Qué porcentaje es y qué entorno creció?", "80 %; el entorno digital", "96 × 100 ÷ 120 = 80, y es un servicio en línea.", calc="96*100//120"),
    sc=[
        ("¿Cuáles son los tres entornos de esta clase?", "Natural, construido y digital", "Son los espacios donde se usa la tecnología."),
        ("¿Una carretera es entorno natural o construido?", "Construido", "La hicieron las personas."),
        ("¿Pueden los productos cambiar los entornos?", "Sí", "Por ejemplo, el automóvil cambió el diseño de las calles."),
    ],
    open_task=(
        "Escoge un caso. A) Una comuna construye ciclovías. B) Un colegio pasa todos los trámites a un sitio en línea. C) Un pueblo instala riego por goteo en sus huertas. Para tu caso escribe el entorno que cambia, el producto que influye, quién influye en quién, un efecto que podría aparecer después y un nuevo producto o servicio que el cambio podría exigir.",
        "A: entorno construido; producto: la ciclovía; el entorno cambia por una obra y puede exigir luces y estacionamientos para bicicletas; efecto: menos autos en esas calles",
        ["identifica el entorno", "explica quién influye en quién", "anticipa un efecto", "propone un producto o servicio que se podría exigir"],
        ["párrafo de cuatro oraciones"],
        ["mezclar el producto con el entorno", "no indicar quién influye en quién"],
        "Pregunta: «¿qué cambió primero, el lugar o el producto?». Sirve para ordenar la relación.",
    ),
    reinforce="Anota tres cosas de tu barrio que no existían cuando tus abuelos eran jóvenes y a qué entorno pertenecen.",
    extend="Explica por qué crecer el entorno digital no elimina el entorno construido.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y la tabla escrita en este cuaderno.",
    use="Aprenderé a analizar la evolución de un producto con una tabla de características, a calcular cuánto cambió cada una y a leer tendencias. Sirve para sostener con números lo que afirmo sobre una evolución.",
    prior=["Sé calcular variación porcentual.", "Sé qué son los factores de cambio.", "Sé leer una tabla."],
    explain=[
        "Para analizar con datos cómo evolucionó un producto se arma una tabla de características con una fila por cada versión. Después se calcula cuánto cambió cada característica. La diferencia es valor nuevo menos valor antiguo. La variación porcentual es diferencia × 100 ÷ valor antiguo, y siempre se calcula sobre el valor antiguo. Si un valor pasa de 4 a 8 se duplicó; si pasa de 4 a 12 se triplicó; si pasa de 4 a 16 se cuadruplicó.",
        "A veces se calcula una razón, que compara dos cantidades: el precio por hora de duración es el precio dividido entre las horas que dura. Una razón permite comparar productos distintos con justicia. Una tendencia es la dirección en que cambia una característica de una versión a otra: sube, baja o se mantiene.",
        "Una tendencia describe lo que ocurrió, pero no asegura lo que ocurrirá. Con solo dos versiones no se puede hablar de una tendencia firme. Por último, los números se relacionan con los factores: si el peso baja y la duración sube, se puede preguntar qué factor técnico o económico lo explica.",
    ],
    vocab=[("diferencia", "valor nuevo menos valor antiguo"), ("variación porcentual", "diferencia × 100 ÷ valor antiguo"), ("duplicar y triplicar", "pasar a 2 veces o a 3 veces el valor"), ("razón", "comparación de dos cantidades, como precio por hora"), ("tendencia", "dirección en que cambia una característica")],
    worked=[
        ("Variación del peso", "Tabla de ejemplo de un producto: versión 1 pesa 400 g, dura 4 h y cuesta $200.000; versión 3 pesa 200 g, dura 12 h y cuesta $150.000. ¿Qué porcentaje bajó el peso de la versión 1 a la 3?", ["Diferencia: 400 − 200 = 200 g.", "Variación sobre el valor antiguo: 200 × 100 ÷ 400 = 50."], "Bajó 50 %"),
        ("Duplicar o triplicar", "Con la misma tabla, ¿cómo cambió la duración de la versión 1 a la 3 y qué porcentaje bajó el precio?", ["La duración pasó de 4 a 12 h: 12 ÷ 4 = 3, o sea, se triplicó.", "El precio bajó 50.000 sobre 200.000: 50.000 × 100 ÷ 200.000 = 25."], "La duración se triplicó y el precio bajó 25 %"),
    ],
    mistakes=[
        ("Calcular el porcentaje sobre el valor nuevo.", "El cambio se mide respecto de donde se partió.", "Divide siempre entre el valor antiguo."),
        ("Afirmar una tendencia con solo dos versiones.", "Dos datos no alcanzan para saber hacia dónde va.", "Reúne al menos tres versiones antes de hablar de tendencia."),
    ],
    R=[
        arith("La duración de una lámpara pasó de 5 horas a 10 horas. ¿Cuántas veces mayor es?", "10//5", "Se divide el valor nuevo entre el antiguo.", " veces"),
        ("La variación porcentual se calcula sobre A) el valor antiguo B) el valor nuevo", "A", "Se mide el cambio respecto del punto de partida."),
        ("Un peso que pasa de 500 g a 400 g, ¿subió o bajó?", "Bajó", "400 es menor que 500."),
    ],
    C=[
        ("Tabla de ejemplo de una lámpara: la versión 1 dura 5 h, pesa 500 g y cuesta $20.000; la versión 3 dura 20 h, pesa 250 g y cuesta $12.000. ¿Cuál característica aumentó?", "La duración", "El peso y el precio bajaron."),
        ("La duración pasó de 5 h en la versión 1 a 20 h en la versión 3. ¿Se duplicó, se triplicó o se cuadruplicó?", "Se cuadruplicó", "20 ÷ 5 = 4."),
        ("Una lámpara dura más y pesa menos en sus versiones nuevas. ¿Qué factor técnico podría explicarlo? A) baterías y materiales mejores B) que el envase de la lámpara cambió de color", "A", "Es un avance en baterías y materiales."),
    ],
    A=[
        arith("En la tabla de la lámpara, la versión 1 pesa 500 g y la versión 3 pesa 250 g. ¿Qué porcentaje bajó el peso?", "(500-250)*100//500", "La diferencia se calcula sobre el peso antiguo.", " %"),
        arith("La versión 2 de la lámpara cuesta $16.000 y la versión 3 cuesta $12.000. ¿Qué porcentaje bajó el precio?", "(16000-12000)*100//16000", "Bajó 4.000 sobre 16.000.", " %"),
        arith("La versión 3 de la lámpara cuesta $12.000 y dura 20 horas. ¿Cuánto cuesta cada hora de duración?", "12000//20", "Se divide el precio entre las horas.", " pesos"),
    ],
    Z=[
        ("La duración de una lámpara fue de 5 h, 10 h y 20 h en tres versiones. Un grupo afirma que la siguiente durará exactamente 40 h. ¿Qué error tiene? A) una tendencia no asegura lo que ocurrirá B) la duración nunca puede superar las 20 h", "A", "Los factores pueden cambiar y la tendencia no se repite necesariamente."),
        ("Una lámpara dura 4 h en la versión 1 y 8 h en la versión 2. ¿Conviene afirmar una tendencia firme? A) no, hacen falta más versiones B) sí, porque se duplicó", "A", "Con solo dos datos no se puede hablar de tendencia."),
    ],
    D=[
        arith("Un producto de ejemplo bajó su peso de 800 a 600 g y su precio de $50.000 a $40.000. ¿Cuántos puntos porcentuales más bajó el peso que el precio?", "(800-600)*100//800-(50000-40000)*100//50000", "El peso bajó 25 % y el precio 20 %.", " puntos"),
        ex("Una versión nueva P pesa 20 % menos que una versión de 500 g. Una versión nueva Q pesa 120 g menos que la misma versión de 500 g. ¿Cuál es más liviana y cuánto pesa?", "Q, con 380 g", "P pesa 500 − 100 = 400 g y Q pesa 500 − 120 = 380 g.", calc="500-120"),
    ],
    ctx=arith("Un reproductor de ejemplo guardaba 10 canciones en su primera versión y 40 en la segunda. ¿Cuántas veces más guarda?", "40//10", "Se divide el valor nuevo entre el antiguo.", " veces"),
    sc=[
        ("¿Sobre qué valor se calcula la variación porcentual?", "Sobre el valor antiguo", "Es el punto de partida."),
        ("Si un valor pasa de 3 a 9, ¿cómo cambió?", "Se triplicó", "9 ÷ 3 = 3."),
        ("En Tecnología: ¿Qué es una tendencia?", "La dirección en que cambia una característica de versión en versión", "Puede subir, bajar o mantenerse."),
    ],
    open_task=(
        "Tabla de ejemplo de un radio portátil: versión 1 pesa 900 g, tiene 10 horas de batería y cuesta $40.000; versión 2 pesa 600 g, 20 horas y $36.000; versión 3 pesa 450 g, 30 horas y $27.000. Calcula el porcentaje que bajó el peso de la versión 1 a la 3, cuántas veces creció la batería, el porcentaje que bajó el precio de la 2 a la 3, y escribe una conclusión con un factor que explique los cambios y una advertencia sobre las tendencias.",
        "Peso: (900 − 450) × 100 ÷ 900 = 50 %. Batería: 30 ÷ 10 = 3 veces. Precio: 9.000 × 100 ÷ 36.000 = 25 %. Conclusión: el radio se volvió más liviano, duradero y barato, probablemente por baterías y materiales mejores; con tres versiones hay una tendencia, pero no asegura el futuro",
        ["calcula las tres variaciones", "usa el valor antiguo como base", "explica con un factor", "incluye una advertencia sobre las tendencias"],
        ["hoja con cálculos y conclusión"],
        ["calcular sobre el valor nuevo", "afirmar que la tendencia seguirá siempre"],
        "Pregunta: «¿entre qué valor dividiste?». Debe ser el valor antiguo.",
    ),
    reinforce="Anota el peso o el precio de dos versiones de un objeto que conozcas y calcula cuánto cambió.",
    extend="Explica por qué la razón «precio por hora de duración» permite comparar mejor dos baterías distintas.",
)

# ------------------------------------------------------------------ OA 05, clase 5
reg(
    OA5, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir hechos, inferencias y opiniones, a evaluar la solidez de la evidencia y a proyectar una tendencia con cuidado. Sirve para sostener con pruebas lo que digo sobre la evolución de los productos.",
    prior=["Sé analizar una tabla de características.", "Sé qué es una tendencia.", "Sé calcular enteros."],
    explain=[
        "Para analizar la evolución con evidencia se separan tres tipos de afirmación. Un hecho se puede comprobar con datos o registros: «la batería pasó de 4 a 8 horas». Una inferencia es una conclusión razonada a partir de hechos: «probablemente se usaron mejores baterías». Una opinión es lo que alguien piensa o prefiere: «los modelos antiguos eran más bonitos». Las inferencias se apoyan en hechos; las opiniones no son evidencia.",
        "Una evidencia es más sólida cuando viene de varias fuentes confiables, usa datos medidos y tiene un orden temporal claro. Que dos cosas ocurran a la vez no prueba que una cause la otra: puede haber una causa común. Por ejemplo, en verano suben las ventas de helados y de bloqueador solar porque hace calor, no porque una cause la otra.",
        "Una proyección estima un valor futuro si la tendencia continúa. Se escribe siempre con «si la tendencia continúa» porque los factores pueden cambiar. Cuanto más lejos del último dato, más incierta es la proyección. Un buen análisis describe el cambio con datos, lo explica con factores y estima el futuro marcando lo que es incierto.",
    ],
    vocab=[("hecho", "afirmación que se puede comprobar"), ("inferencia", "conclusión razonada a partir de hechos"), ("opinión", "lo que alguien piensa o prefiere"), ("evidencia sólida", "la que viene de varias fuentes confiables con datos medidos"), ("causa común", "algo que produce dos hechos a la vez"), ("proyección", "estimación de un valor futuro si la tendencia continúa")],
    worked=[
        ("Clasificar afirmaciones", "Clasifica: (a) «la batería pasó de 4 a 12 horas», (b) «probablemente se usaron baterías mejores», (c) «los modelos nuevos son feos».", ["(a) se puede comprobar con datos: hecho.", "(b) es una conclusión razonada: inferencia. (c) es un gusto: opinión."], "(a) hecho, (b) inferencia, (c) opinión"),
        ("Proyectar una tendencia", "La duración de tres versiones fue 4 h, 8 h y 12 h. Si la tendencia continúa, ¿cuánto durará la cuarta versión?", ["Cada versión dura 4 horas más que la anterior.", "Calculo 12 + 4 = 16."], "16 horas, si la tendencia continúa"),
    ],
    mistakes=[
        ("Tomar una opinión como evidencia.", "Una opinión no se puede comprobar con datos.", "Busca un dato que la respalde."),
        ("Afirmar una causa porque dos cosas ocurrieron a la vez.", "Puede existir una causa común o solo una coincidencia.", "Busca más pruebas antes de afirmar una causa."),
    ],
    R=[
        ("«El peso pasó de 400 a 300 gramos» es A) un hecho B) una opinión", "A", "Se puede comprobar con una medición."),
        ("«Los modelos antiguos eran más bonitos», ¿es un hecho, una inferencia o una opinión?", "Una opinión", "Depende del gusto de cada persona."),
        ("«Probablemente bajó el peso porque se usaron materiales más livianos», ¿es un hecho, una inferencia o una opinión?", "Una inferencia", "Es una conclusión razonada a partir de datos."),
    ],
    C=[
        ("Una proyección se escribe con «si la tendencia continúa» porque A) los factores pueden cambiar B) los datos siempre son falsos", "A", "Una tendencia no asegura el futuro."),
        ("Suben a la vez las ventas de helados y las de bloqueador solar. ¿Una causa la otra? A) no necesariamente; puede haber una causa común, el calor B) sí, siempre", "A", "Dos hechos simultáneos no prueban que uno cause el otro."),
        ("¿Cuál es una evidencia más sólida? A) tres informes de instituciones con datos medidos B) la opinión de un amigo", "A", "Hay varias fuentes confiables y datos medidos."),
    ],
    A=[
        ("Clasifica cada frase como hecho, inferencia u opinión: (1) «la duración subió de 5 a 20 horas», (2) «seguramente mejoraron las baterías», (3) «esas lámparas son las mejores».", "1 hecho, 2 inferencia, 3 opinión", "Se puede medir, se concluye con razones y depende del gusto, respectivamente."),
        arith("La duración de tres versiones fue de 6 h, 9 h y 12 h. Si la tendencia continúa, ¿cuánto durará la cuarta?", "12+(12-9)", "Cada versión dura 3 horas más.", " horas"),
        arith("El peso de tres versiones fue de 1.000 g, 900 g y 800 g. Si la tendencia continúa, ¿cuánto pesará la versión 6?", "800-3*100", "De la versión 3 a la 6 hay 3 pasos de 100 g.", " gramos"),
    ],
    Z=[
        ("Un equipo afirma que «la moda hizo que mejoraran las baterías» solo porque ambas cosas ocurrieron en los mismos años. ¿Qué le falta? A) más evidencia que muestre una relación causal B) nada, porque ocurrir en los mismos años ya es una prueba", "A", "La coincidencia en el tiempo no prueba la causa."),
        ("La duración fue de 4 h, 8 h y 12 h en tres versiones. Alguien proyecta que la versión 10 durará 40 h. ¿Qué tan confiable es esa proyección?", "Poco confiable: está lejos de los datos y los factores pueden cambiar", "Cuanto más lejos del último dato, más incierta es la proyección."),
    ],
    D=[
        arith("Las ventas de un producto de ejemplo fueron 100, 150, 200 y 250 unidades en cuatro años seguidos. Si la tendencia continúa, ¿cuántas unidades se venderían el sexto año?", "250+2*50", "Cada año aumentó 50 unidades y faltan dos años.", " unidades"),
        ("Regla del grupo: una conclusión es sólida si tiene al menos 2 hechos que la respaldan. Conclusión: «bajó el costo por mayor competencia». Respaldos: el precio bajó de $100 a $80 (hecho), los fabricantes pasaron de 2 a 5 (hecho) y «a mí me parece que sí» (opinión). ¿Es sólida?", "Sí", "Tiene dos hechos; la opinión no cuenta como evidencia."),
    ],
    ctx=arith("Los pesos de tres versiones de un producto de ejemplo fueron 600 g, 500 g y 400 g. Si la tendencia continúa, ¿cuánto pesará la siguiente?", "400-(500-400)", "Cada versión pesa 100 g menos que la anterior.", " gramos"),
    sc=[
        ("En Tecnología: ¿Qué diferencia hay entre un hecho y una opinión?", "El hecho se puede comprobar y la opinión depende del gusto", "Solo el hecho sirve como evidencia."),
        ("¿Qué frase acompaña a una proyección?", "«Si la tendencia continúa»", "Marca que el resultado es incierto."),
        ("Dos cosas ocurren a la vez, ¿prueba eso que una causa la otra?", "No", "Puede haber una causa común."),
    ],
    open_task=(
        "Datos de ejemplo de un reproductor portátil: versión 1 guarda 20 canciones, pesa 300 g y cuesta $30.000; versión 2 guarda 40, pesa 200 g y cuesta $25.000; versión 3 guarda 60, pesa 100 g y cuesta $20.000. Escribe dos hechos, dos inferencias (con una razón) y una opinión; luego haz una proyección de la versión 4 con la frase «si la tendencia continúa» y escribe una razón por la que podría no cumplirse.",
        "Hechos: la capacidad pasó de 20 a 60 canciones; el precio bajó de $30.000 a $20.000. Inferencias: probablemente hubo mejores memorias; probablemente más fabricantes redujeron los costos. Opinión: la versión 3 es la más bonita. Proyección: si la tendencia continúa, la versión 4 guardaría 80 canciones y pesaría 0 g, lo que no es posible; la tendencia tiene un límite físico",
        ["dos hechos con datos", "dos inferencias con razón", "una opinión", "una proyección con la frase obligatoria", "una razón por la que podría no cumplirse"],
        ["hoja con las cinco afirmaciones y la proyección"],
        ["presentar una inferencia como hecho", "proyectar sin considerar límites"],
        "Pregunta: «¿esto se puede comprobar con un dato?». Si no, no es un hecho.",
    ),
    reinforce="Mira una noticia o publicación sobre tecnología y subraya una frase que sea un hecho y una que sea opinión.",
    extend="Explica por qué una proyección se vuelve menos confiable cuanto más lejos está del último dato.",
)

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir efectos positivos y negativos, directos e indirectos, previstos y no previstos, y de corto y largo plazo, preguntando siempre para quién. Sirve para analizar con equilibrio lo que cambia la tecnología.",
    prior=["Sé qué es la evolución de un producto.", "Sé calcular porcentajes.", "Sé qué es un impacto."],
    explain=[
        "La tecnología cambia la vida de las personas, y esos cambios se llaman efectos. Un efecto positivo mejora las condiciones de las personas: más acceso, seguridad, tiempo o salud. Un efecto negativo trae daño, pérdida, riesgo o exclusión. Muchos productos tienen efectos de los dos tipos a la vez. La automatización, que es hacer con máquinas o programas tareas que antes hacían personas, es un ejemplo: aumenta la producción y puede reducir puestos de trabajo.",
        "Los efectos pueden ser directos, si recaen en quien usa el producto, o indirectos, si llegan a otras personas o a la sociedad. Pueden ser previstos, cuando se buscaban, o no previstos, cuando nadie los esperaba. Y pueden ocurrir a corto plazo, que es pronto, o a largo plazo, que es mucho después.",
        "Para clasificar un efecto se pregunta: ¿qué cambió?, ¿a quién afecta?, ¿es una mejora o un daño para esa persona? y ¿cuándo ocurre? Lo que es positivo para un grupo puede ser negativo para otro. Por eso la pregunta clave es siempre «¿para quién?». Si se cuentan personas de dos grupos que se cruzan, se suman los grupos y se resta una vez a quienes están en ambos.",
    ],
    vocab=[("efecto", "cambio que produce un producto en las personas o en la sociedad"), ("efecto directo", "el que recae en quien usa el producto"), ("efecto indirecto", "el que llega a otras personas o a la sociedad"), ("efecto no previsto", "el que nadie esperaba al crear el producto"), ("corto y largo plazo", "pronto o mucho después"), ("automatización", "hacer con máquinas o programas tareas que hacían personas")],
    worked=[
        ("Clasificar según para quién", "Una tienda instala cajas de autoservicio: (a) los clientes esperan menos en la fila, (b) hay menos puestos de cajero. Clasifica cada efecto.", ["(a) mejora la situación de los clientes: positivo para ellos.", "(b) disminuye el trabajo de los cajeros: negativo para ellos."], "(a) positivo para los clientes, (b) negativo para los cajeros"),
        ("Reconocer un efecto no previsto", "Se crean las bolsas plásticas para cargar cosas con facilidad y, con los años, se acumulan como residuos. ¿Qué tipo de efecto es el de los residuos?", ["Al crearlas, nadie buscaba producir residuos.", "El daño apareció mucho después."], "No previsto, negativo y de largo plazo"),
    ],
    mistakes=[
        ("Decir que un producto es solo bueno o solo malo.", "La mayoría tiene efectos de ambos tipos.", "Anota efectos positivos y negativos."),
        ("Olvidar preguntar «¿para quién?».", "Lo que ayuda a unos puede perjudicar a otros.", "Nombra a quién afecta cada efecto."),
    ],
    R=[
        ("Un efecto que mejora las condiciones de las personas es A) positivo B) negativo", "A", "Mejorar condiciones es lo propio de lo positivo."),
        ("Un efecto que llega a otras personas después, y no al usuario inmediato, ¿es directo o indirecto?", "Indirecto", "No recae en quien usa el producto."),
        ("Las bolsas plásticas acumuladas como residuos, ¿son un efecto positivo o negativo?", "Negativo", "Dañan el ambiente."),
    ],
    C=[
        ("Un juego educativo ayuda a practicar matemática y a algunos les quita horas de sueño. ¿Qué muestra? A) que un mismo producto puede tener efectos positivos y negativos B) que los productos solo tienen efectos negativos", "A", "Los efectos dependen de cómo y quién lo usa."),
        ("Un efecto no previsto es A) uno que nadie buscaba al crear el producto B) uno que ocurre siempre", "A", "Se llama así porque no fue planeado."),
        ("Para decidir si un efecto es positivo o negativo conviene preguntar A) ¿para quién? B) ¿cuánto costó fabricarlo?", "A", "Un mismo efecto puede ser positivo para unos y negativo para otros."),
    ],
    A=[
        ("Clasifica cada efecto como positivo o negativo: (1) más personas pueden hacer trámites desde casa, (2) algunas personas sin internet no pueden hacer el trámite, (3) las filas son más cortas.", "1 positivo, 2 negativo, 3 positivo", "Los dos primeros se refieren a ganar y a perder acceso, y el tercero ahorra tiempo."),
        arith("En un barrio de ejemplo hay 400 locales. El comercio en línea hizo que 120 vendieran también en línea y que 40 cerraran. Ningún local está en los dos grupos. ¿Cuántos siguieron sin cambios?", "400-120-40", "Se restan los locales de los dos grupos.", " locales"),
        ("Efecto 1: hoy la gente llega más rápido a su destino. Efecto 2: dentro de 20 años hay más autos en las calles y más contaminación. ¿Cuál es de corto plazo y cuál de largo plazo?", "El 1 de corto plazo y el 2 de largo plazo", "El primero ocurre pronto y el segundo mucho después."),
    ],
    Z=[
        ("Una persona dice: «Este producto es malo porque a mi vecino le trajo problemas». ¿Qué le falta a su razonamiento?", "Considerar los efectos en otras personas y los positivos", "Un solo caso no muestra el balance de todos los efectos."),
        ("Dos efectos de un servicio de reparto: (a) más ingresos para los repartidores, (b) más bolsas desechables. ¿Cuántos efectos positivos y cuántos negativos hay?", "1 positivo y 1 negativo", "El primero beneficia y el segundo daña."),
    ],
    D=[
        arith("En una encuesta de ejemplo a 80 personas, 60 dicen que la mensajería instantánea les ahorra tiempo y 24 que les molesta el exceso de mensajes; 12 dijeron ambas cosas. ¿Cuántas personas dijeron al menos una de las dos?", "60+24-12", "Se suman los dos grupos y se resta una vez a quienes están en ambos.", " personas"),
        ex("Un taller automatiza una tarea: la producción sube de 40 a 60 piezas diarias, pero de 5 trabajadores en esa tarea se necesitan 2 menos. ¿Qué porcentaje aumentó la producción y cuántos trabajadores quedan en la tarea?", "50 %; 3 trabajadores", "(60 − 40) × 100 ÷ 40 = 50, y 5 − 2 = 3.", calc="(60-40)*100//40"),
    ],
    ctx=ex("Una aplicación de ejemplo permite a 84 de 120 vecinos pagar sus cuentas desde casa. ¿Qué porcentaje es y qué tipo de efecto es para ellos?", "70 %; positivo", "84 × 100 ÷ 120 = 70, y ahorran tiempo y traslados.", calc="84*100//120"),
    sc=[
        ("En Tecnología: ¿Qué es un efecto indirecto?", "Uno que llega a otras personas o a la sociedad", "No recae en quien usa el producto."),
        ("¿Qué pregunta ayuda a clasificar un efecto como positivo o negativo?", "¿Para quién?", "Cambia según el grupo."),
        ("¿Qué es la automatización?", "Hacer con máquinas o programas tareas que hacían personas", "Puede aumentar la producción y reducir puestos."),
    ],
    open_task=(
        "Escoge un producto. A) El comercio en línea. B) La mensajería instantánea. C) Las cajas de autoservicio en tiendas. Escribe al menos dos efectos positivos y dos negativos; marca cuáles son directos o indirectos, cuál es no previsto y cuál de corto o largo plazo, y para quién es cada uno.",
        "B: positivo directo, se comunica rápido y barato, para quienes tienen celular; positivo indirecto, los grupos se organizan con facilidad; negativo directo, exceso de mensajes que distrae; negativo no previsto, circulan rumores sin verificar. Corto plazo: rapidez; largo plazo: cambia cómo se conversa",
        ["dos efectos positivos y dos negativos", "marca directo o indirecto", "marca un efecto no previsto", "indica para quién es cada uno"],
        ["tabla de efectos con su clasificación"],
        ["solo efectos positivos", "no indicar para quién"],
        "Pregunta: «¿a quién le pasa esto?». Si no puede decirlo, el efecto no está bien descrito.",
    ),
    reinforce="Elige un producto que uses a diario y anota un efecto positivo y uno negativo, indicando para quién.",
    extend="Explica por qué un efecto no previsto puede aparecer mucho tiempo después de crear un producto.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los datos escritos en este cuaderno.",
    use="Aprenderé a inferir efectos sociales a partir de datos de la evolución de un producto, escribiendo la inferencia con su razón y comprobando si el dato alcanza. Sirve para razonar con cuidado en lugar de adivinar.",
    prior=["Sé distinguir hechos, inferencias y opiniones.", "Sé clasificar efectos.", "Sé calcular porcentajes."],
    explain=[
        "Inferir es llegar a una conclusión razonada a partir de datos o hechos, sin que nadie la diga directamente. Para inferir los efectos de la evolución de un producto se revisan los cambios (más barato, más pequeño, más conectado) y se pregunta: si esto cambió, ¿qué probablemente cambió en la vida de las personas?",
        "Un método sencillo tiene cuatro pasos: describir el cambio con un dato, pensar a quién afecta, escribir la inferencia con la palabra «probablemente» y una razón, y buscar un dato que la apoye o la contradiga. Comparar el antes y el después ayuda: cómo se hacía una actividad antes y cómo se hace ahora, en tiempo, costo y personas que participan. Una inferencia no es una certeza.",
        "Por ejemplo, si los celulares con cámara se hicieron baratos y comunes, probablemente más personas pueden registrar lo que ocurre a su alrededor. Eso tiene un efecto positivo (más testimonios) y uno negativo (riesgo para la privacidad). Cuando el dato no alcanza para concluir algo, lo correcto es decir «con este dato no se puede concluir».",
    ],
    vocab=[("inferir", "llegar a una conclusión razonada a partir de datos"), ("antes y después", "comparación de cómo se hacía algo y cómo se hace ahora"), ("dato insuficiente", "el que no alcanza para concluir"), ("probablemente", "palabra que marca que una inferencia no es certeza")],
    worked=[
        ("Inferir desde un dato", "Datos de ejemplo: los hogares con computador pasaron de 20 de cada 100 a 80 de cada 100. Infiere un efecto positivo y uno negativo.", ["Más hogares pueden estudiar y hacer trámites en línea: efecto positivo.", "Quedan 20 de cada 100 hogares sin computador: efecto negativo, podrían quedar fuera."], "Positivo: más acceso a estudio y trámites. Negativo: 20 de cada 100 hogares podrían quedar fuera"),
        ("Reconocer un dato insuficiente", "Dato de ejemplo: las ventas de lectores digitales subieron 50 %. ¿Se puede inferir que las bibliotecas cerraron?", ["El dato habla de ventas de un aparato, no de bibliotecas.", "No dice nada sobre el cierre de ningún lugar."], "No, el dato no alcanza"),
    ],
    mistakes=[
        ("Presentar una inferencia como si fuera un hecho.", "No tiene la seguridad de un dato comprobado.", "Escribe «probablemente» y la razón."),
        ("Inferir solo efectos positivos.", "Se pierde de vista quién resulta perjudicado.", "Pregunta también quién queda fuera o pierde."),
    ],
    R=[
        ("Inferir es A) llegar a una conclusión razonada a partir de datos B) copiar un dato", "A", "Implica razonar y no solo repetir."),
        ("¿Una inferencia es tan segura como un hecho comprobado?", "No", "Por eso se escribe con «probablemente»."),
        ("El comercio en línea se hizo común. ¿Qué inferencia es razonable? A) probablemente más personas compran sin ir a la tienda B) probablemente nadie usa tiendas", "A", "Es coherente con el cambio y no exagera."),
    ],
    C=[
        ("En un pueblo de ejemplo, las visitas a la biblioteca bajaron de 500 a 200 por mes y las consultas en línea a su catálogo subieron de 100 a 600. ¿Qué inferencia está mejor apoyada? A) probablemente muchas personas consultan en línea en vez de ir B) probablemente a nadie le interesan los libros", "A", "Los datos muestran un traslado hacia lo digital."),
        ("¿Qué dato apoyaría la inferencia «el teletrabajo reduce los viajes»? A) el número de viajes en hora punta bajó B) el sueldo promedio subió", "A", "Se relaciona directamente con los viajes."),
        ("Se sabe solo que un producto se hizo más barato. ¿Qué no se puede concluir con ese dato? A) que mejoró la salud de la población B) que más personas pueden comprarlo", "A", "El precio no dice nada de la salud."),
    ],
    A=[
        arith("Datos de ejemplo: los hogares con internet pasaron de 30 de cada 100 a 80 de cada 100. ¿Cuántos puntos porcentuales aumentaron?", "80-30", "Se resta el valor antiguo al nuevo.", " puntos"),
        ex("Dato de ejemplo: 80 de cada 100 hogares tienen internet. ¿Cuántos no tienen y qué efecto negativo podría inferirse?", "20 hogares; podrían quedar fuera de los servicios en línea", "100 − 80 = 20, y sin internet no se accede a esos servicios.", calc="100-80"),
        ("Dato de ejemplo: la mensajería instantánea es gratuita y casi todas las personas tienen celular. ¿Cuáles son inferencias razonables? (1) probablemente se envían más mensajes que cartas, (2) todas las personas se comunican mejor, (3) probablemente baja el uso de mensajes de texto de pago.", "1 y 3", "Son coherentes con el dato; la 2 exagera y no puede comprobarse."),
    ],
    Z=[
        ("Dato: hace diez años había 5 locales de fotocopias y hoy hay 2. Juan infiere: «probablemente muchas tareas se envían ahora en formato digital». ¿Qué le falta para estar más seguro? A) un dato que lo apoye, como cuántas tareas se envían en digital B) nada, porque ya es un hecho", "A", "Una inferencia necesita un dato que la respalde."),
        ("Alguien concluye: «Como subió el uso de bicicletas, la contaminación bajó». ¿Qué problema tiene esa inferencia?", "Usa un solo dato; falta evidencia de la contaminación", "Que más gente use bicicleta no demuestra por sí solo que haya menos contaminación."),
    ],
    D=[
        ex("En una comuna de ejemplo, las compras en línea pasaron de 200 a 500 por semana y las compras en tienda bajaron de 800 a 600. ¿Cuántas compras más hay en total ahora que antes?", "100 más", "Antes eran 200 + 800 = 1.000 y ahora son 500 + 600 = 1.100.", calc="(500+600)-(200+800)"),
        ex("Datos de ejemplo: antes había 5.000 pasajeros diarios en bus. Ahora hay 4.000 en bus y 1.000 viajes en un servicio de transporte en línea. ¿Cuántos viajes hay ahora en total y cuántos más que antes?", "5.000 viajes; ninguno más", "4.000 + 1.000 = 5.000, igual que antes: parte de los pasajeros cambió de servicio.", calc="4000+1000"),
    ],
    ctx=ex("Datos de ejemplo: de cada 100 estudiantes, 40 usaban libros digitales hace un tiempo y hoy los usan 70. ¿Cuántos más hay por cada 100 y qué se podría inferir?", "30 más; probablemente más estudiantes acceden a lectura digital", "70 − 40 = 30, lo que apunta a mayor acceso a la lectura digital.", calc="70-40"),
    sc=[
        ("¿Qué palabra marca que una inferencia no es una certeza?", "Probablemente", "Indica que falta comprobarla."),
        ("¿Qué se hace cuando el dato no alcanza?", "Se dice que no se puede concluir", "Es más honesto que adivinar."),
        ("¿Qué comparación ayuda a inferir efectos?", "El antes y el después", "Muestra qué cambió en tiempo, costo y personas."),
    ],
    open_task=(
        "Datos de ejemplo del comercio en línea de una comuna: antes, de 100 compras semanales, 10 eran en línea y 90 en tienda; hoy, 40 en línea y 60 en tienda. Escribe (a) el cambio con números, (b) dos inferencias con «probablemente» y una razón cada una (una positiva y una negativa), (c) un dato adicional que buscarías para comprobar una de ellas y (d) una cosa que estos datos no permiten concluir.",
        "(a) Las compras en línea pasaron de 10 a 40 de cada 100, 30 más. (b) Probablemente más personas ahorran traslados; probablemente algunos locales pierden clientes. (c) Cuántos locales cerraron o bajaron sus ventas. (d) No permiten concluir que las personas se sienten más felices",
        ["describe el cambio con números", "dos inferencias con «probablemente» y razón", "una positiva y una negativa", "dato para comprobar", "una conclusión que no se puede sacar"],
        ["hoja con las cuatro partes"],
        ["inferencias sin razón", "concluir más de lo que dicen los datos"],
        "Pregunta: «¿qué dato apoya esta inferencia?». Si no hay ninguno, hay que decir que no se puede concluir.",
    ),
    reinforce="Pregunta a una persona mayor cómo hacía antes un trámite o una compra y compara con hoy en tiempo y costo.",
    extend="Explica por qué es más honesto decir «con este dato no se puede concluir» que arriesgar una inferencia sin apoyo.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a ver cómo la evolución tecnológica afecta a distintos grupos y ámbitos (trabajo, educación, comunicación, ambiente y bienestar) y a reconocer la brecha digital. Sirve para evaluar quién gana y quién queda fuera.",
    prior=["Sé clasificar efectos como positivos y negativos.", "Sé inferir con datos.", "Sé calcular porcentajes."],
    explain=[
        "Los efectos de la tecnología se reparten de manera distinta según el ámbito y el grupo. En el trabajo, la automatización cambia tareas y empleos, y el teletrabajo, que es trabajar a distancia usando internet, ahorra viajes. En la educación, los recursos en línea amplían el aprendizaje. En la comunicación, la información circula rápido, pero también los rumores. En el ambiente, los productos más eficientes gastan menos, pero los aparatos viejos generan residuos electrónicos. En la salud, la telemedicina, que es atender consultas por videollamada, acerca a los médicos; el exceso de pantallas puede afectar el sueño y el ánimo.",
        "La brecha digital es la diferencia entre las personas que tienen acceso a internet y habilidades para usarlo, y las que no. Depende de la edad, del lugar donde se vive y de los ingresos. Cuando un trámite o una clase pasan a ser solo en línea, quienes están en el lado de la brecha sin acceso quedan fuera.",
        "Para evaluar el balance se anotan los efectos por grupo y se pregunta quién gana, quién pierde y quién queda fuera. Si una persona nota que el uso del celular le quita el sueño o la hace sentir mal, lo mejor es contarlo a una persona adulta de confianza y acordar horarios de uso.",
    ],
    vocab=[("teletrabajo", "trabajar a distancia usando internet"), ("telemedicina", "consultas de salud por videollamada"), ("brecha digital", "diferencia entre quienes tienen acceso y habilidades digitales y quienes no"), ("residuos electrónicos", "aparatos que se desechan"), ("balance", "suma de positivos menos suma de negativos")],
    worked=[
        ("Quién gana y quién queda fuera", "La telemedicina evita viajes largos a adultos mayores del campo, pero requiere internet. ¿Quién gana y quién queda fuera?", ["Gana quien vive lejos y tiene conexión: ahorra tiempo y dinero.", "Queda fuera quien no tiene internet o no sabe usarlo: es la brecha digital."], "Gana quien tiene conexión; queda fuera quien no la tiene"),
        ("Calcular un balance", "Un servicio en línea tiene efectos positivos de 5 y 2 puntos y un efecto negativo de 4 puntos (puntajes de ejemplo). ¿Cuál es el balance?", ["Suma de positivos: 5 + 2 = 7.", "Balance: 7 − 4 = 3."], "Balance de 3 puntos"),
    ],
    mistakes=[
        ("Pensar que los efectos son iguales para todos.", "Dependen de la edad, el lugar y el acceso.", "Anota los efectos grupo por grupo."),
        ("Ignorar la brecha digital.", "Un servicio solo en línea deja fuera a parte de la población.", "Pregunta quién no tiene acceso y qué alternativa tiene."),
    ],
    R=[
        ("La brecha digital es la diferencia entre A) quienes tienen acceso y habilidades digitales y quienes no B) dos marcas de celular", "A", "Habla de acceso y de habilidades."),
        ("Las clases en línea sirven a una estudiante con internet pero no a otra sin conexión. ¿Qué efecto aparece?", "La brecha digital", "Una queda fuera por no tener acceso."),
        ("La automatización de una tarea en una fábrica, ¿tiene su efecto principal en el trabajo o en el clima?", "En el trabajo", "Cambia las tareas de las personas."),
    ],
    C=[
        ("Los aparatos viejos que se desechan acumulan residuos electrónicos. ¿En qué ámbito está el efecto? A) el ambiente B) la educación", "A", "Los residuos afectan el entorno natural."),
        ("¿Quién gana con el teletrabajo? A) quienes ahorran tiempo de viaje B) quienes no tienen conexión a internet", "A", "Trabajar a distancia evita traslados."),
        ("Una persona duerme poco por mirar el celular de noche y se siente ansiosa. ¿Qué es lo más recomendable? A) contarlo a una persona adulta de confianza y acordar horarios B) esconder el celular para no preocupar a nadie", "A", "Pedir apoyo ayuda a cuidar el bienestar."),
    ],
    A=[
        ("Asocia cada efecto con su ámbito (trabajo, educación o ambiente): (1) cursos gratuitos en línea para aprender, (2) nuevos desechos de aparatos viejos, (3) tareas que hace una máquina en lugar de personas.", "1 educación, 2 ambiente, 3 trabajo", "Cada efecto afecta a un ámbito distinto."),
        arith("Balance de ejemplo: los efectos positivos tienen puntajes 4 y 3, y los negativos 2 y 3. ¿Cuál es el balance?", "4+3-2-3", "Positivos menos negativos.", " puntos"),
        arith("En un pueblo de ejemplo, 60 de 100 hogares tienen internet estable. Si un trámite pasa a ser solo en línea, ¿cuántos hogares quedan sin poder hacerlo?", "100-60", "Son los hogares sin internet estable.", " hogares"),
    ],
    Z=[
        ("Un colegio exige todas las tareas en línea y 6 de 30 estudiantes no tienen internet en casa. ¿Qué efecto negativo hay y qué medida podría reducirlo?", "Brecha digital; permitir entrega en papel o acceso en el colegio", "Así quienes no tienen conexión también cumplen."),
        ("Alguien dice: «La tecnología mejora la vida de todos por igual». ¿Qué respondes? A) los efectos dependen del acceso, la edad y el lugar B) tiene razón", "A", "No todos tienen las mismas condiciones."),
    ],
    D=[
        arith("En un colegio de ejemplo, 24 de 30 estudiantes mejoraron su nota con recursos en línea y 6 no pudieron usarlos. ¿Qué porcentaje no pudo usarlos?", "6*100//30", "Se calcula sobre el total de 30 estudiantes.", " %"),
        arith("Un centro de salud de ejemplo atiende 50 consultas al mes y el 40 % pasa a ser por videollamada. Cada consulta en línea ahorra 2 horas de viaje a la persona. ¿Cuántas horas se ahorran al mes?", "50*40//100*2", "El 40 % de 50 son 20 consultas y cada una ahorra 2 horas.", " horas"),
    ],
    ctx=ex("En un barrio de ejemplo, 70 de cada 100 personas mayores usan videollamadas para hablar con su familia. ¿Cuántas de cada 100 no las usan y qué podría pasarles?", "30; podrían sentirse más aisladas", "100 − 70 = 30, y sin ese medio dependen de otras formas de contacto.", calc="100-70"),
    sc=[
        ("¿Qué es el teletrabajo?", "Trabajar a distancia usando internet", "Ahorra viajes de ida y vuelta."),
        ("¿Qué es la brecha digital?", "La diferencia entre quienes tienen acceso y habilidades digitales y quienes no", "Deja fuera a parte de la población."),
        ("Si el celular te quita el sueño, ¿a quién se lo cuentas?", "A una persona adulta de confianza", "Así puedes acordar horarios y cuidar tu bienestar."),
    ],
    open_task=(
        "Escoge un caso. A) Un municipio pasa todos los trámites a un sitio en línea. B) Una empresa ofrece teletrabajo. C) Un colegio entrega materiales solo digitales. Para tu caso escribe tres grupos de personas (por ejemplo adultos mayores, estudiantes, trabajadores), un efecto positivo y uno negativo para cada grupo, la brecha digital que aparece y una medida para reducirla.",
        "A: adultos mayores, positivo si tienen apoyo (ahorran filas), negativo si no saben usar el sitio; trabajadores, positivo (hacen el trámite fuera del horario), negativo si no tienen conexión; familias sin internet, negativo (quedan fuera). Medida: mantener atención presencial y ofrecer talleres",
        ["tres grupos", "un efecto positivo y uno negativo por grupo", "identifica la brecha digital", "propone una medida"],
        ["tabla de grupos y efectos con una medida"],
        ["describir un solo grupo", "olvidar a quienes no tienen acceso"],
        "Pregunta: «¿quién no puede usar esto y qué hace entonces?». Debe haber una medida para esa persona.",
    ),
    reinforce="Anota qué trámites o servicios de tu familia ya se hacen en línea y cuáles aún exigen ir en persona.",
    extend="Explica por qué ofrecer una alternativa presencial no significa rechazar el avance tecnológico.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a argumentar sobre los efectos de la tecnología con afirmación, evidencia, razonamiento y contraargumento, y a proponer medidas para potenciar lo positivo y reducir lo negativo. Sirve para participar con razones en un debate sobre tecnología.",
    prior=["Sé inferir efectos con datos.", "Sé distinguir hechos de opiniones.", "Sé calcular porcentajes."],
    explain=[
        "Argumentar es defender una postura con razones. Un argumento tiene una afirmación (lo que sostengo), una evidencia (un dato que la apoya), un razonamiento (por qué esa evidencia apoya la afirmación) y un contraargumento (lo que diría quien piensa distinto y cómo respondo). Una postura equilibrada reconoce efectos positivos y negativos y no exagera.",
        "Para potenciar lo positivo y reducir lo negativo hay tres tipos de medidas. Las medidas personales son hábitos, como dejar el celular fuera del dormitorio a cierta hora. Las medidas sociales o de diseño son, por ejemplo, alternativas sin conexión, accesibilidad y talleres para aprender. Las normas son reglas o leyes que obligan o prohíben algo. Una buena medida es concreta, se puede realizar y se hace cargo de un efecto específico.",
        "Argumentar también exige ética: no ocultar datos que contradicen mi postura, reconocer lo que no sé y respetar a quien piensa distinto. Para elegir entre medidas se pueden comparar con criterios como efectividad y viabilidad, dando más peso al criterio más importante.",
    ],
    vocab=[("afirmación", "lo que se sostiene en un argumento"), ("evidencia", "dato que apoya la afirmación"), ("razonamiento", "explicación de por qué la evidencia apoya la afirmación"), ("contraargumento", "lo que diría quien piensa distinto"), ("medida", "acción para potenciar lo positivo o reducir lo negativo"), ("norma", "regla o ley que obliga o prohíbe algo")],
    worked=[
        ("Partes de un argumento", "Identifica las partes: «Conviene ofrecer también tareas en papel (1), porque 6 de 30 estudiantes no tienen internet (2). Sin esa alternativa, ellos no podrían entregar (3)».", ["(1) es lo que se sostiene: afirmación.", "(2) es un dato: evidencia. (3) explica por qué el dato apoya la idea: razonamiento."], "(1) afirmación, (2) evidencia, (3) razonamiento"),
        ("Elegir una medida", "Efecto negativo: «el exceso de pantallas a la hora de dormir». ¿Qué medida personal puedes proponer?", ["Debe ser un hábito concreto que dependa de mí.", "Por ejemplo, acordar con una persona adulta de la casa una hora a partir de la cual el celular queda fuera del dormitorio."], "Dejar el celular fuera del dormitorio desde una hora acordada"),
    ],
    mistakes=[
        ("Defender una postura sin evidencia.", "Una afirmación sin dato es solo una opinión.", "Agrega un dato que la apoye."),
        ("Proponer medidas vagas como «que todos se porten bien».", "No dicen qué hacer ni cómo se comprueba.", "Escribe una acción concreta y viable."),
    ],
    R=[
        ("En un argumento, ¿qué es la evidencia? A) un dato que apoya la afirmación B) la opinión de quien argumenta", "A", "La evidencia respalda con hechos."),
        ("Un contraargumento es A) lo que diría quien piensa distinto B) la conclusión final", "A", "Reconoce la postura contraria."),
        ("«Dejar el celular fuera del dormitorio a cierta hora», ¿es una medida personal o una norma legal?", "Una medida personal", "Es un hábito de cada persona."),
    ],
    C=[
        ("¿Cuál es una medida concreta? A) «ofrecer los trámites también por teléfono y en papel» B) «hay que cuidar a la gente»", "A", "Dice qué hacer."),
        ("¿Qué medida social reduce la brecha digital? A) talleres para aprender a usar servicios en línea B) pedir que todos los trámites sean solo en línea", "A", "Enseña a quienes no saben usarlos."),
        ("Una postura equilibrada A) reconoce efectos positivos y negativos B) solo menciona los positivos", "A", "No oculta información."),
    ],
    A=[
        ("Une cada frase con su parte del argumento (afirmación, evidencia o razonamiento): (1) «Sin esa enseñanza, no podrían hacer sus trámites sin ir a la sucursal.», (2) «20 de 50 personas mayores del barrio dicen no saber usar la banca en línea.», (3) «Conviene enseñar a las personas mayores a usar la banca en línea.»", "1 razonamiento, 2 evidencia, 3 afirmación", "El 3 sostiene, el 2 es un dato y el 1 explica el vínculo."),
        arith("Una medida de ejemplo reduce de 40 a 10 los hogares sin acceso a un trámite. ¿Qué porcentaje de los hogares sin acceso consiguió acceso?", "(40-10)*100//40", "30 de los 40 hogares consiguieron acceso.", " %"),
        ("Medidas: (1) taller de uso para personas mayores, (2) ley que obliga a ofrecer atención presencial, (3) hábito personal de apagar notificaciones. ¿Cuál es una norma?", "La 2", "Una ley obliga a ofrecer algo."),
    ],
    Z=[
        ("Argumento: «La tecnología es mala porque mi primo se distrajo con el celular». ¿Qué falla? A) una sola anécdota no basta como evidencia B) usa demasiados datos", "A", "Un caso no representa a todos."),
        ("Para reducir el efecto negativo del exceso de pantallas, un grupo propone prohibir todo uso de celulares en el país. ¿Qué problema tiene la medida? A) elimina también usos positivos y es poco viable B) es una medida personal y no una norma", "A", "Una buena medida es viable y no destruye lo positivo."),
    ],
    D=[
        ex("Pesos: efectividad 3 y viabilidad 2. Medida X: puntajes 3 y 1. Medida Y: puntajes 2 y 3. Medida Z: puntajes 1 y 3. ¿Cuál es la mejor y cuántos puntos tiene?", "Y, con 12", "X suma 9 + 2 = 11; Y suma 6 + 6 = 12; Z suma 3 + 6 = 9.", calc="3*2+2*3"),
        arith("Una campaña de ejemplo busca que el 30 % de 200 personas mayores aprenda a usar un trámite en línea. Hasta ahora aprendieron 45. ¿Cuántas personas faltan para llegar a la meta?", "200*30//100-45", "La meta es 60 personas y ya hay 45.", " personas"),
    ],
    ctx=arith("En un barrio de ejemplo, 50 de 200 personas mayores no usan servicios en línea. Un taller logra que 30 de ellas aprendan. ¿Cuántas siguen sin usarlos?", "50-30", "Se restan las que aprendieron.", " personas"),
    sc=[
        ("¿Cuáles son las cuatro partes de un argumento?", "Afirmación, evidencia, razonamiento y contraargumento", "Son las partes que se piden en esta clase."),
        ("En Tecnología: ¿Qué es una norma?", "Una regla o ley que obliga o prohíbe algo", "Es un tipo de medida."),
        ("¿Qué debe cumplir una buena medida?", "Ser concreta, viable y hacerse cargo de un efecto", "Así se puede aplicar y comprobar."),
    ],
    open_task=(
        "Escribe un argumento de cuatro oraciones sobre este tema de ejemplo: «Los servicios en línea del municipio». Datos de ejemplo: 70 de 100 hogares usan los servicios en línea; 30 de 100 no tienen acceso estable; los trámites en línea ahorran filas. Incluye afirmación, evidencia con un dato, razonamiento y contraargumento con tu respuesta, y propone una medida personal o social y una norma para reducir un efecto negativo.",
        "Afirmación: conviene mantener los servicios en línea y además atención presencial. Evidencia: 70 de 100 hogares los usan, pero 30 no tienen acceso estable. Razonamiento: así se aprovecha el ahorro de filas sin dejar fuera a nadie. Contraargumento: algunos dirán que cuesta más mantener ambos; respondo que evita que 30 de cada 100 hogares queden sin trámite. Medida social: talleres. Norma: obligar a ofrecer una alternativa presencial",
        ["afirmación clara", "evidencia con dato", "razonamiento", "contraargumento con respuesta", "una medida y una norma"],
        ["texto argumentativo de cuatro oraciones y dos propuestas"],
        ["afirmación sin dato", "medidas vagas"],
        "Pregunta: «¿qué dato apoya tu afirmación y qué diría quien piensa distinto?».",
    ),
    reinforce="Elige una opinión que hayas escuchado sobre tecnología y anota qué dato la apoyaría o la contradiría.",
    extend="Explica por qué reconocer un efecto negativo hace más creíble una postura a favor de una tecnología.",
)
