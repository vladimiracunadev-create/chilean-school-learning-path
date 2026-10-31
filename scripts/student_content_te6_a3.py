"""Cuaderno del estudiante, 6.º básico Tecnología: OA 03 (elaborar un producto con técnicas y herramientas), clases 1 a 5.

Clase 1 materiales y propiedades, 2 medir y marcar, 3 cortar, perforar y serrar, 4 unir y pegar, 5 mezclar, lijar y pintar con lista de dominio.
Seguridad: los estudiantes cortan solo papel y cartón delgado con tijeras de punta roma. Serrar, perforar madera, plástico grueso o metal, y lijar con herramienta,
los hace una persona adulta con protección. No hay fuego, vidrio, cortadores ni productos químicos; la pintura es al agua (témpera) y la mezcla es de harina y agua sin calor.
Simplificación declarada: se enseña a elegir la técnica y la herramienta y a cuidarse; la práctica con herramientas de taller queda para el docente.
"""
from __future__ import annotations

from student_content_te6_a import reg
from student_lessons import arith

OA3 = "TE06 OA 03"

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja y lápiz. Todos los materiales se describen en este cuaderno; si quieres, mira un papel, un cartón, una cuerda y una tapa de plástico de tu casa.",
    use="Aprenderé a reconocer papeles, cartones, maderas, fibras, plásticos, cerámicos, metales y desechos, y a elegir el material según lo que el objeto necesita. Sirve para que el producto dure y sea seguro.",
    prior=["Sé que un criterio se puede comprobar.", "Sé reutilizar materiales.", "Sé medir en centímetros."],
    explain=[
        "Los materiales son lo que se usa para elaborar un producto. Los papeles y cartones son livianos y se cortan con tijeras. Las maderas son duras y resistentes. Las fibras son hilos, como la lana, el algodón o el cordel, y sirven para amarrar o tejer. Los plásticos no dejan pasar el agua. Los cerámicos, como la loza, son duros pero se quiebran. Los metales son resistentes y se doblan solo con fuerza.",
        "Cada material tiene propiedades: resistencia, que es cuánto aguanta sin romperse; flexibilidad, que es cuánto se dobla; peso; impermeabilidad, que es no dejar pasar el agua; y dureza. Para elegir un material, primero escribes qué necesita el objeto, como aguantar peso o mojarse, y luego eliges el material cuyas propiedades lo cumplen.",
        "Los desechos, como cajas, tapas y envases limpios, también son materiales. Usarlos reduce la basura y baja el costo. Antes de reutilizarlos, revisa que estén limpios, secos y sin bordes peligrosos. Un objeto puede combinar varios materiales: por ejemplo, un cuaderno usa papel, cartón y una espiral de metal.",
    ],
    vocab=[("propiedad", "característica de un material, como la resistencia"), ("resistencia", "cuánto aguanta un material sin romperse"), ("flexible", "que se dobla sin romperse"), ("impermeable", "que no deja pasar el agua"), ("desecho", "material que ya no se usa y se podría reutilizar")],
    worked=[
        ("Elegir según una necesidad", "Un portalápices de escritorio debe aguantar peso y no mojarse si se derrama agua. Entre cartón común, plástico grueso y papel, ¿cuál eliges?", ["El objeto necesita resistencia e impermeabilidad.", "El plástico grueso no deja pasar el agua y es resistente."], "El plástico grueso"),
        ("Revisar un desecho", "Quieres reutilizar un frasco de plástico de yogur. ¿Qué revisas antes de usarlo?", ["Debe estar limpio y seco.", "Debe tener los bordes lisos y sin partes sueltas."], "Que esté limpio, seco y sin bordes peligrosos"),
    ],
    mistakes=[
        ("Elegir un material solo porque es bonito.", "Puede no cumplir lo que el objeto necesita.", "Escribe primero qué necesita el objeto y luego compara propiedades."),
        ("Pensar que los desechos sirven sin revisarlos.", "Pueden estar sucios o con bordes peligrosos.", "Revisa que estén limpios, secos y seguros."),
    ],
    R=[
        ("La lana y el cordel, ¿son fibras o metales?", "Fibras", "Son hilos que sirven para amarrar o tejer."),
        ("¿Qué material no deja pasar el agua: el plástico o el papel?", "El plástico", "El plástico es impermeable."),
        ("¿El papel o la madera es más resistente?", "La madera", "La madera es más dura y aguanta más."),
    ],
    C=[
        ("¿Qué significa que un material sea flexible?", "Que se dobla sin romperse", "Es la definición de flexibilidad."),
        ("Una taza de loza cae al suelo y se quiebra. ¿Qué propiedad muestra los cerámicos?", "Son duros pero frágiles", "Se quiebran con un golpe."),
        ("¿Por qué una tapa de botella limpia es un material útil?", "Porque es un desecho que se puede reutilizar", "Reduce la basura y no cuesta."),
    ],
    A=[
        ("Necesitas un cordón para amarrar dos tubos de cartón. ¿Qué material eliges? A cordel, B hoja de papel.", "A", "El cordel es una fibra resistente que amarra."),
        ("Un objeto debe doblarse sin romperse. ¿Qué material cumple? A una lámina de cartulina, B una taza de loza.", "A", "La cartulina es flexible; la loza se quiebra."),
        arith("Para un trabajo hay 40 tapas de botella. Cada pieza usa 8 tapas. ¿Cuántas piezas completas se pueden hacer?", "40//8", "Se divide el total de tapas entre las que usa cada pieza.", " piezas"),
    ],
    Z=[
        ("Ana propone hacer un soporte para libros con papel de seda. Beto, con cartón grueso. Si el soporte debe aguantar 5 libros, ¿quién elige mejor y por qué?", "Beto, porque el cartón grueso es más resistente", "El papel de seda no aguanta peso."),
        ("Un grupo usa una caja de pescado sin lavar para reutilizar. ¿Es correcto?", "No", "Un desecho debe estar limpio y seguro."),
    ],
    D=[
        arith("Una repisa lleva 3 tablitas de madera de 30 cm y 2 de 15 cm. ¿Cuántos centímetros de madera se necesitan?", "3*30+2*15", "Se calcula cada grupo de tablitas y se suman.", " cm"),
        ("Un portalápices debe ser impermeable, resistente y reutilizar un desecho. ¿Qué material cumple los tres? A un envase de plástico grueso limpio, B una hoja de periódico.", "A", "El plástico grueso es impermeable y resistente, y es un desecho."),
    ],
    ctx=("Para una maceta pequeña del curso necesitas un recipiente que no se moje, que aguante tierra húmeda y que sea un desecho. Entre una caja de zapatos de cartón, un envase de helado de plástico limpio y una hoja de papel, elige uno y escribe las propiedades que justifican tu decisión.", "El envase de helado de plástico limpio: es impermeable, resistente y es un desecho", "Se eligen propiedades que cumplen la necesidad."),
    sc=[
        ("¿Qué es la impermeabilidad?", "No dejar pasar el agua", "Es una propiedad de materiales como el plástico."),
        ("¿Qué se revisa en un desecho antes de reutilizarlo?", "Que esté limpio, seco y sin bordes peligrosos", "Así es seguro."),
        ("¿Cómo se elige un material?", "Según lo que el objeto necesita", "Se comparan las propiedades con la necesidad."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: un organizador de escritorio que debe aguantar el peso de 10 lápices y estar hecho con desechos. Objeto 2: un posavasos que no se moje y se pueda lavar. Escribe qué necesita el objeto, dos materiales que podrías usar, las propiedades de cada uno y cuál eliges.",
        "Objeto 2: necesita ser impermeable y lavable. Materiales: plástico grueso o tapa de frasco. Elijo la tapa porque es un desecho impermeable",
        ["escribe la necesidad del objeto", "nombra dos materiales", "dice sus propiedades", "elige y justifica"],
        ["tabla con necesidad, materiales y decisión"],
        ["elegir por apariencia", "usar un desecho sucio"],
        "Pregunta: «¿qué propiedad necesita el objeto?». Si no la nombra, pídele volver a la necesidad.",
    ),
    reinforce="Nombra cinco objetos de tu casa y el material principal de cada uno.",
    extend="Explica por qué un objeto puede estar hecho con más de un material, con un ejemplo.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Hoja, lápiz y regla. Las medidas están escritas en este cuaderno.",
    use="Aprenderé a medir y marcar con exactitud usando regla y escuadra. Sirve para que las piezas coincidan al armar el producto.",
    prior=["Sé usar una regla en centímetros.", "Sé que 1 cm son 10 mm.", "Sé leer cotas en un dibujo técnico."],
    explain=[
        "Medir es comparar una longitud con una unidad. Para medir con regla, haz coincidir el cero de la regla con el borde de la pieza y lee el número donde termina. Mira la regla de frente y no de lado, porque si miras de lado la lectura cambia. Una huincha sirve para medidas más largas o curvas.",
        "Marcar es dejar señales en el material para saber dónde cortar o doblar. Se marca con lápiz de punta fina: un punto en el lugar y una línea recta con la regla. Para marcar un ángulo recto se usa una escuadra o la esquina de una hoja. Un ángulo recto mide 90 grados y forma una esquina como la de un libro.",
        "La regla de oro es medir dos veces y cortar una. Si dibujas una línea gruesa, el error aumenta. Cuando necesitas varias piezas iguales, mide la primera y úsala como patrón para marcar las demás, así todas quedan iguales. También conviene dejar un margen para unir y para el grosor del material.",
    ],
    vocab=[("medir", "comparar una longitud con una unidad"), ("marcar", "dejar señales para cortar o doblar"), ("escuadra", "instrumento que forma un ángulo recto"), ("ángulo recto", "esquina de 90 grados"), ("patrón", "pieza que se usa de modelo para marcar otras iguales")],
    worked=[
        ("Leer una medida con regla", "Una tira empieza en el cero de la regla y termina en la marca 14 y 3 rayitas más (cada rayita es 1 mm). ¿Cuánto mide?", ["14 cm son 140 mm.", "Sumo 3 mm."], "143 mm"),
        ("Sacar tiras de una pieza larga", "De una cinta de papel de 60 cm quieres tiras de 15 cm. ¿Cuántas tiras salen y cuántos cortes haces?", ["Divido 60 entre 15: salen 4 tiras.", "Para 4 tiras se hacen 3 cortes."], "4 tiras con 3 cortes"),
    ],
    mistakes=[
        ("Poner el 1 de la regla en el borde de la pieza.", "Se pierde 1 cm de longitud.", "Haz coincidir el 0 con el borde de la pieza."),
        ("Mirar la regla desde un costado.", "La lectura cambia.", "Mira la regla de frente."),
    ],
    R=[
        ("¿Dónde se pone el cero de la regla al medir una pieza?", "En el borde de la pieza", "Desde ahí se mide la longitud."),
        ("En Tecnología: ¿Cuántos grados mide un ángulo recto?", "90", "Es la esquina de un libro o de una hoja."),
        ("¿Cuántos milímetros son 7 cm?", "70", "Cada centímetro tiene 10 mm."),
    ],
    C=[
        ("¿Para qué sirve una escuadra?", "Para marcar ángulos rectos", "Forma una esquina de 90 grados."),
        ("¿Por qué se mira la regla de frente?", "Porque de lado la lectura cambia", "Evita errores de lectura."),
        ("¿Para qué sirve un patrón?", "Para marcar varias piezas iguales", "Se copia la medida de una pieza."),
    ],
    A=[
        arith("Una pieza termina en la marca de 12 cm y empieza en la marca de 4 cm porque no se alineó con el cero. ¿Cuántos centímetros mide?", "12-4", "Se resta la marca inicial de la final.", " cm"),
        arith("De una cinta de 90 cm se cortan tiras de 18 cm. ¿Cuántas tiras salen?", "90//18", "Se divide el largo total entre el largo de cada tira.", " tiras"),
        arith("Una pieza mide 9 cm y 5 mm. ¿Cuántos milímetros son?", "9*10+5", "Se convierten los centímetros y se suman los milímetros.", " mm"),
    ],
    Z=[
        ("Diego puso la regla con el 2 en el borde y leyó 11 en el otro extremo. Dice que mide 11 cm. ¿Qué error cometió?", "No restó el 2 inicial; mide 9 cm", "La pieza va de 2 a 11, o sea 9 cm."),
        ("Para marcar 6 piezas iguales, Rosa mide cada una con la regla; Pablo mide una y la usa de patrón. ¿Cuál método asegura piezas más parecidas?", "El de Pablo", "El patrón copia siempre la misma medida."),
    ],
    D=[
        arith("De un cartón de 100 cm se sacan tiras de 20 cm. ¿Cuántos cortes se necesitan para obtener todas las tiras?", "100//20-1", "Las tiras son 5 y para 5 tiras se hacen 4 cortes.", " cortes"),
        arith("Una caja lleva 4 paredes de 15 cm de largo cada una, con 1 cm de margen para unir en cada pared. ¿Cuántos centímetros de cartón se marcan en total?", "4*(15+1)", "Cada pared mide 15 cm más 1 cm de margen.", " cm"),
    ],
    ctx=("Necesitas marcar en una cartulina una tira de 24 cm y otra de 35 cm para un marcador de libros. Si tienes 60 cm de cartulina, calcula si alcanzan ambas tiras y cuántos centímetros sobran.", "24 + 35 = 59; alcanzan; sobra 1 cm", "Se suman las tiras y se restan de 60."),
    sc=[
        ("¿Dónde se pone el cero de la regla?", "En el borde de la pieza", "Así se mide la longitud completa."),
        ("¿Qué regla ayuda a evitar errores de corte?", "Medir dos veces y cortar una", "Se verifica antes de cortar."),
        ("¿Qué se usa para marcar un ángulo recto?", "Una escuadra o la esquina de una hoja", "Ambas forman 90 grados."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: marcar 4 tiras de 12 cm, para un marco de 12 cm por 12 cm, en una tira de cartulina de 60 cm. Trabajo 2: marcar 3 tiras de 25 cm de una cinta de papel de 80 cm. Escribe cada medida con su unidad, cuánto material sobra, cómo te aseguras de que las piezas queden iguales y cómo marcas los ángulos rectos.",
        "Trabajo 1: 4 × 12 = 48 cm; sobran 12 cm. Trabajo 2: 3 × 25 = 75 cm; sobran 5 cm. Mido una tira, la uso de patrón y marco con lápiz fino. Para ángulos rectos uso la esquina de una hoja",
        ["medidas con unidad", "calcula lo que sobra", "usa un patrón", "marca ángulos rectos con una escuadra o la esquina de una hoja"],
        ["hoja con medidas, cálculo y método de marcado"],
        ["no alinear con el cero", "no revisar la medida dos veces"],
        "Pregunta: «¿cómo sabes que las piezas serán iguales?». Si no menciona el patrón, pídele explicarlo.",
    ),
    reinforce="Mide con una regla el largo de tres objetos de tu escritorio y anótalos en centímetros y milímetros.",
    extend="Explica cómo marcarías un cuadrado de 10 cm de lado usando solo una regla y la esquina de una hoja.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno. No necesitas herramientas: aquí se trata de elegir y de cuidarse.",
    use="Aprenderé a elegir la técnica para cortar, perforar y serrar según el material, y a trabajar seguro. Sirve para cortar bien y evitar accidentes.",
    prior=["Sé medir y marcar con exactitud.", "Sé que algunas herramientas las usa una persona adulta.", "Conozco las propiedades de los materiales."],
    explain=[
        "Cortar es separar un material en partes. Las tijeras de punta roma cortan papel y cartón delgado. Para cartón grueso, madera, plástico duro o metal se necesitan otras herramientas, que solo usa una persona adulta, por ejemplo un serrucho o una sierra. Serrar es cortar con una sierra, moviéndola de ida y vuelta.",
        "Perforar es hacer un agujero. En papel se usa una perforadora de papel. Para perforar madera, plástico grueso o metal se usa un taladro o una lezna, y lo hace una persona adulta. Un estudiante nunca sostiene la pieza que otra persona perfora o sierra; la pieza se sujeta con una prensa o una mesa firme.",
        "Para trabajar seguro: despeja la mesa, usa lentes de protección si algo puede saltar, junta el pelo largo, corta alejando la tijera del cuerpo y deja las herramientas con el filo hacia abajo o guardadas. Si un corte es muy riesgoso, se cambia por otra técnica: por ejemplo, doblar y rasgar sobre una línea marcada, o comprar la pieza ya cortada.",
    ],
    vocab=[("serrar", "cortar con una sierra, moviéndola de ida y vuelta"), ("perforar", "hacer un agujero en un material"), ("tijeras de punta roma", "tijeras sin punta afilada, más seguras"), ("prensa", "herramienta que sujeta una pieza firme"), ("lentes de protección", "anteojos que protegen los ojos")],
    worked=[
        ("Elegir la técnica", "Debes hacer un agujero en una hoja de cartulina y otro en una tabla de madera. ¿Qué técnica y quién la usa en cada caso?", ["Cartulina: perforadora de papel; la puedes usar tú.", "Madera: taladro; lo usa una persona adulta."], "Cartulina con perforadora, tú; madera con taladro, una persona adulta"),
        ("Contar cortes", "De una tira de 90 cm quieres piezas de 30 cm. ¿Cuántas piezas salen y cuántos cortes?", ["90 dividido en 30 da 3 piezas.", "Para 3 piezas se necesitan 2 cortes."], "3 piezas con 2 cortes"),
    ],
    mistakes=[
        ("Sujetar con la mano la pieza que otra persona sierra.", "Puede resultar herida.", "La pieza va sujeta con una prensa o sobre una mesa firme."),
        ("Cortar acercando la tijera al cuerpo.", "Si se resbala, se corta.", "Corta alejando la tijera del cuerpo."),
    ],
    R=[
        ("¿Quién usa un serrucho en la escuela?", "Una persona adulta", "Es una herramienta riesgosa."),
        ("¿Con qué se hace un agujero en una hoja?", "Con una perforadora de papel", "Es la herramienta segura para papel."),
        ("¿Las tijeras de punta roma cortan papel o madera?", "Papel", "Sirven para materiales delgados."),
    ],
    C=[
        ("¿Para qué sirven los lentes de protección?", "Para proteger los ojos", "Evitan que algo salte a los ojos."),
        ("¿Cómo debe estar una pieza que se serrucha?", "Sujeta con una prensa o sobre una mesa firme", "No debe sostenerse con la mano."),
        ("¿Qué haces si un corte es muy riesgoso?", "Cambio la técnica o pido ayuda", "Se evita el peligro."),
    ],
    A=[
        arith("De una tira de 120 cm se quieren piezas de 30 cm. ¿Cuántos cortes se necesitan para obtener todas las piezas?", "120//30-1", "Hay 4 piezas y se necesitan 3 cortes.", " cortes"),
        ("Necesitas un agujero para pasar un cordel en una hoja de cartón delgado. ¿Qué técnica usas? A tijera con la punta hacia ti, B perforadora de papel.", "B", "La perforadora es segura en material delgado."),
        ("¿Cuál es una posición segura para cortar cartón delgado? A tijera alejándola del cuerpo, B tijera hacia el pecho.", "A", "Si se resbala, no te lastima."),
    ],
    Z=[
        ("Un grupo quiere cortar una tabla de madera de 1 cm de grosor con tijeras de punta roma. ¿Es posible y seguro?", "No", "Las tijeras no cortan madera y forzarlas es peligroso."),
        ("Para un cartón muy grueso, Valentina propone usar un cortador con filo. ¿Qué haces?", "Cambiar la técnica o pedir ayuda a una persona adulta", "El cortador es riesgoso para estudiantes."),
    ],
    D=[
        arith("Una tira de 150 cm se corta en piezas de 25 cm. ¿Cuántas piezas salen?", "150//25", "Se divide el largo total entre el largo de cada pieza.", " piezas"),
        ("Una estudiante de pelo largo observa cómo una persona adulta perfora una tabla y mantiene el pelo suelto cerca de la herramienta. ¿Es seguro?", "No, debe juntarse el pelo", "El pelo suelto puede enredarse en una herramienta."),
    ],
    ctx=("Tu grupo hará un portalápices con cartón delgado y debe hacer dos agujeros para pasar un cordel en una tabla de madera. Escribe cómo se cortan y perforan las dos partes, quién usa cada herramienta y una medida de seguridad.", "Cartón: tijera de punta roma, yo. Agujeros en la madera: taladro, una persona adulta. Seguridad: la tabla va sujeta con una prensa", "Se separa lo que hace el estudiante de lo que hace el adulto."),
    sc=[
        ("¿Qué herramienta usa un estudiante para cortar cartón delgado?", "Tijeras de punta roma", "Son seguras para materiales delgados."),
        ("¿Quién perfora madera?", "Una persona adulta", "El taladro es riesgoso."),
        ("¿Qué se hace con el pelo largo?", "Se junta", "Evita que se enrede."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: una caja con 5 paredes de cartón delgado y 2 agujeros para cordel. Trabajo 2: un soporte de madera con una tabla que se corta en 3 partes y 1 agujero. Escribe qué técnica usas para cada parte, quién la realiza, el orden y dos medidas de seguridad.",
        "Trabajo 1: paredes con tijeras de punta roma, yo; agujeros con perforadora de papel, yo. Seguridad: tijera alejada del cuerpo; mesa despejada",
        ["técnica por cada parte", "quién la realiza", "orden de los pasos", "dos medidas de seguridad"],
        ["tabla con técnica, responsable y seguridad"],
        ["proponer herramientas riesgosas a estudiantes", "olvidar la sujeción de la pieza"],
        "Pregunta: «¿quién usa esta herramienta?». Si dice «yo» para madera, repasa la regla de seguridad.",
    ),
    reinforce="Escribe tres reglas de seguridad para cortar papel con tijeras en tu casa.",
    extend="Explica por qué sujetar la pieza con una prensa es más seguro que sostenerla con la mano.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a elegir cómo unir y pegar según los materiales y el uso del objeto. Sirve para que el producto no se desarme.",
    prior=["Conozco materiales y sus propiedades.", "Sé medir y marcar.", "Sé que algunos productos necesitan tiempo de secado."],
    explain=[
        "Unir es juntar dos piezas. Hay uniones que se pegan, como las de papel con pegamento en barra o de cartón con cola fría, que es un pegamento blanco al agua. Hay uniones que se amarran, con cordel o cinta, y uniones que se encajan, con ranuras en las piezas. Cada una tiene ventajas: pegar es fijo, amarrar se puede deshacer y encajar sirve para armar y desarmar.",
        "Para elegir la unión, mira los materiales y el uso. Papel y cartón fino se pegan bien con pegamento. Piezas pesadas necesitan una unión más fuerte, como encaje con pegamento. Si el objeto debe guardarse desarmado, conviene encajar o amarrar. Si estará al aire libre o con humedad, la cinta y el pegamento al agua se despegan.",
        "Para pegar bien: usa poco pegamento, extiéndelo con una tira de cartón, junta las piezas, presiona y espera el tiempo de secado antes de seguir. Si pintas antes de que seque, la pieza se corre. Protege la mesa con papel de diario. Los pegamentos fuertes con olor o con químicos no son para estudiantes.",
    ],
    vocab=[("unir", "juntar dos piezas"), ("cola fría", "pegamento blanco que se limpia con agua"), ("encajar", "unir piezas con ranuras que calzan"), ("amarrar", "unir con cordel, cinta u otro hilo"), ("secado", "tiempo para que el pegamento quede firme")],
    worked=[
        ("Elegir la unión", "Armas una caja de cartón que debe guardarse desarmada en una mochila. ¿Qué unión eliges: pegar o encajar?", ["La caja debe poder desarmarse.", "Pegar es fijo; encajar permite armar y desarmar."], "Encajar"),
        ("Calcular tiempo de espera", "Pegas dos piezas a las 10:00 y la cola fría necesita 45 minutos para quedar firme. ¿A qué hora puedes seguir?", ["Sumo 45 minutos a las 10:00.", "10:00 más 45 minutos es 10:45."], "A las 10:45"),
    ],
    mistakes=[
        ("Poner mucho pegamento.", "Chorrea, tarda en secar y mancha.", "Usa poco y extiéndelo con una tira de cartón."),
        ("Seguir trabajando antes de que seque.", "Las piezas se mueven y se despegan.", "Espera el tiempo de secado indicado."),
    ],
    R=[
        ("La cola fría, ¿se limpia con agua o necesita químicos?", "Con agua", "Es un pegamento blanco al agua."),
        ("Unir piezas con cordel, ¿es pegar, amarrar o encajar?", "Amarrar", "Se junta con un hilo."),
        ("Ranuras que calzan entre piezas, ¿es pegar o encajar?", "Encajar", "Las piezas se calzan sin pegamento."),
    ],
    C=[
        ("¿Por qué conviene encajar un objeto que se guarda desarmado?", "Porque se puede armar y desarmar", "El encaje no es fijo."),
        ("¿Qué pasa si pintas antes de que seque el pegamento?", "La pieza se corre o se despega", "Se mueve mientras está húmeda."),
        ("¿Quién usa pegamentos fuertes con olor químico?", "Una persona adulta", "No son para estudiantes."),
    ],
    A=[
        arith("Pegas una pieza a las 11:15 y la cola necesita 30 minutos para secar. ¿Cuántos minutos pasan entre que termina de secar y las 12:00?", "45-30", "De 11:15 a 12:00 hay 45 minutos; se resta la espera.", " minutos"),
        ("Unirás tarjetas de cartulina que se guardarán en un cuaderno. ¿Qué unión eliges? A pegamento en barra, B cordel grueso.", "A", "El pegamento en barra es plano y limpio."),
        ("Quieres unir un tubo de cartón a una base de forma que se pueda sacar. ¿Qué unión eliges? A pegar, B encajar.", "B", "El encaje permite sacar el tubo."),
    ],
    Z=[
        ("Un grupo pegó una repisa de cartón y la cargó con libros a los 5 minutos. Se despegó. ¿Qué falló?", "No esperaron el tiempo de secado", "El pegamento aún estaba húmedo."),
        ("Hans dice: «A mayor cantidad de pegamento, más firme la unión». ¿Es correcto?", "No", "El exceso chorrea y tarda más en secar."),
    ],
    D=[
        arith("Pegas 3 pares de piezas, uno tras otro, y cada par necesita 15 minutos de secado antes del siguiente. ¿Cuántos minutos de espera hay en total?", "3*15", "Cada par espera 15 minutos.", " minutos"),
        ("Una caja pegada debe guardarse en una mochila y luego abrirse en una mesa. ¿Conviene pegar o encajar sus tapas?", "Encajar", "El encaje se puede armar y desarmar."),
    ],
    ctx=("Armarás un puente de cartón con 6 tiras. Dos tiras se unen con cola fría y una tira se amarra al borde con cordel para poder cambiarla. Describe qué unión usas en cada caso y cuánto esperas antes de probar si la cola necesita 40 minutos.", "Cola para las fijas, cordel para la que se cambia; espero 40 minutos antes de probar", "Se eligen uniones según el uso y se respeta el secado."),
    sc=[
        ("¿Qué tipos de unión hay?", "Pegar, amarrar y encajar", "Son las tres formas de este tema."),
        ("¿Cuánto pegamento se usa?", "Poco, bien extendido", "El exceso chorrea."),
        ("¿Qué se hace tras pegar?", "Esperar el secado", "Así la pieza queda firme."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: una caja de cartón que se guarda plana en un cajón. Objeto 2: un banderín de papel colgado con cordel. Escribe qué uniones usarías para cada parte, por qué y cuánto esperarías antes de usarlo si la cola necesita 30 minutos.",
        "Objeto 1: encajar las paredes para poder aplanarla; pegar solo la base. Espero 30 minutos",
        ["elige una unión por cada parte", "da una razón", "considera el secado", "cuida la seguridad"],
        ["tabla con parte, unión y razón"],
        ["usar demasiado pegamento", "no esperar el secado"],
        "Pregunta: «¿el objeto se guarda desarmado o fijo?». Revisa que la unión se ajuste al uso.",
    ),
    reinforce="Une dos tiras de papel con pegamento en barra, espera 5 minutos y prueba si se separan.",
    extend="Explica una situación en que conviene amarrar en vez de pegar.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja y lápiz. Los casos están escritos en este cuaderno.",
    use="Aprenderé a mezclar, lijar y pintar con seguridad y a revisar si dominé las técnicas con una lista de verificación. Sirve para terminar el producto bien y reconocer qué puedo mejorar.",
    prior=["Sé unir y pegar.", "Sé cortar y marcar con seguridad.", "Sé que algunas tareas las hace una persona adulta."],
    explain=[
        "Mezclar es juntar dos o más cosas para obtener otra. Con pintura al agua, rojo y amarillo dan naranja; azul y amarillo dan verde; rojo y azul dan morado. Para papel maché se mezcla harina y agua en una proporción, como 1 parte de harina y 2 partes de agua. Mezclar se hace sin calor y se revuelve hasta que no queden grumos.",
        "Lijar es desgastar una superficie con papel de lija para que quede lisa. Se lija con un taco, siguiendo la dirección de las vetas, y se usa mascarilla porque el polvo molesta. En madera y plástico duro lo hace una persona adulta; un estudiante solo alisa bordes de cartón con lija fina, en un lugar ventilado y con supervisión.",
        "Pintar es cubrir con pintura al agua. Protege la mesa con diario, usa delantal, aplica capas delgadas y espera que seque cada capa. Al terminar lava el pincel con agua. Al final, revisa si dominaste las técnicas con una lista: las medidas son correctas, los cortes son limpios, las uniones están firmes, la superficie es lisa y la pintura es pareja.",
    ],
    vocab=[("mezclar", "juntar cosas para obtener otra"), ("proporción", "relación entre cantidades, como 1 de harina por 2 de agua"), ("lijar", "desgastar una superficie para dejarla lisa"), ("veta", "línea natural de la madera"), ("capa", "una pasada de pintura sobre una superficie")],
    worked=[
        ("Proporción de una mezcla", "Para papel maché se mezcla 1 taza de harina con 2 tazas de agua. ¿Cuánta agua necesitas con 3 tazas de harina?", ["La proporción es 1 de harina por 2 de agua.", "Con 3 tazas de harina, el agua es 3 × 2."], "6 tazas de agua"),
        ("Mezclar colores", "Quieres pintura verde pero solo tienes azul y amarillo. ¿Qué haces?", ["El verde se obtiene mezclando azul y amarillo.", "Mezcla partes parecidas y prueba el color en un papel."], "Mezclar azul y amarillo"),
    ],
    mistakes=[
        ("Aplicar una capa gruesa de pintura de una vez.", "Chorrea y tarda en secar.", "Aplica capas delgadas y espera que sequen."),
        ("Lijar sin mascarilla.", "El polvo irrita la nariz y los pulmones.", "Usa mascarilla en un lugar ventilado."),
    ],
    R=[
        ("Rojo mezclado con amarillo, ¿qué color da?", "Naranja", "Es una mezcla de pintura básica."),
        ("¿Para qué se usa el papel de lija?", "Para dejar una superficie lisa", "Desgasta pequeñas irregularidades."),
        ("¿Cómo se limpia un pincel con pintura al agua?", "Con agua", "La pintura al agua se lava con agua."),
    ],
    C=[
        ("¿Por qué se usa mascarilla al lijar?", "Porque el polvo molesta", "Evita respirar el polvo."),
        ("¿Por qué conviene aplicar capas delgadas de pintura?", "Porque secan mejor y no chorrean", "Una capa gruesa se corre."),
        ("¿En qué dirección se lija la madera?", "En la dirección de las vetas", "Así no se rayan las fibras."),
    ],
    A=[
        arith("Para papel maché se usa 1 taza de harina por 2 de agua. ¿Cuántas tazas de agua se necesitan con 4 tazas de harina?", "4*2", "Se multiplican las tazas de harina por 2.", " tazas"),
        ("Quieres pintura morada con rojo y azul. ¿Cuántos colores básicos mezclas?", "Dos", "El morado se logra con rojo y azul."),
        arith("Una mezcla lleva 5 partes de agua por 1 de pintura. Si usas 3 partes de pintura, ¿cuántas partes de agua necesitas?", "3*5", "Se multiplica por 5 cada parte de pintura.", " partes"),
    ],
    Z=[
        ("Clara pintó su caja de cartón dos veces seguidas con una capa gruesa y quedó con grumos. ¿Qué debió hacer?", "Pintar capas delgadas y esperar a que sequen", "Las capas gruesas se secan mal."),
        ("Un grupo quiere lijar una tabla de madera con una lijadora eléctrica. ¿Quién lo hace?", "Una persona adulta", "Una herramienta con motor no es para estudiantes."),
    ],
    D=[
        arith("Una pared de cartón pintada necesita 2 capas y cada capa seca 20 minutos. ¿Cuántos minutos de secado hay en total?", "2*20", "Se multiplican las capas por el tiempo de secado de cada una.", " minutos"),
        ("Lista de dominio con 5 criterios. Un trabajo cumple 4. ¿Cuántos criterios le faltan?", "1", "5 menos 4 es 1."),
    ],
    ctx=("Terminas un organizador de cartón. Lo lijas en los bordes con lija fina, lo pintas con 2 capas y revisas con la lista: medidas correctas, cortes limpios, uniones firmes, superficie lisa y pintura pareja. Cumples 4 de 5, y los cortes tienen bordes desparejos. Escribe qué falta y cómo lo mejorarías.", "Falta el criterio de cortes limpios; lijaría los bordes desparejos con lija fina o recortaría con tijera de punta roma", "Se identifica el criterio no cumplido y se propone una mejora."),
    sc=[
        ("¿Qué se mezcla para papel maché?", "Harina y agua", "Es una mezcla segura sin calor."),
        ("¿Qué se usa al lijar?", "Mascarilla y lija fina, en un lugar ventilado", "Protege de respirar el polvo."),
        ("¿Para qué sirve la lista de dominio?", "Para revisar qué técnicas hice bien y qué debo mejorar", "Permite saber qué mejorar."),
    ],
    open_task=(
        "Escoge un producto terminado. Producto 1: una caja de cartón de 5 piezas, con medidas correctas, un corte desparejo, uniones firmes, superficie lisa y pintura que se corrió. Producto 2: un portalápices de cartón con medidas correctas, cortes limpios, una unión suelta, superficie lisa y pintura pareja. Completa la lista de verificación (medidas, cortes, uniones, superficie lisa y pintura), cuenta cuántos criterios cumple, nombra el que falla y explica cómo lo corregirías.",
        "Producto 2: cumple 4 de 5; falla la unión suelta. La corregiría con un poco de cola fría y esperando el secado",
        ["marca los criterios que cumple", "cuenta cuántos cumple", "nombra el que falla", "propone una corrección segura"],
        ["lista de verificación completada"],
        ["no revisar cada criterio", "proponer una corrección riesgosa"],
        "Pregunta: «¿cuál criterio no se cumple y qué técnica lo arregla?». Revisa que no proponga herramientas riesgosas.",
    ),
    reinforce="Mezcla en un papel dos colores que tengas y anota qué color obtuviste.",
    extend="Explica por qué la lista de verificación ayuda a mejorar más que decir «quedó bien».",
)
