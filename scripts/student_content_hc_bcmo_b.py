"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-02 (estructura y organización de la célula, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, microscopio ni internet. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos: los resultados que se analizan se entregan ya escritos. Si quieres ver células reales, pide a tu docente una demostración con muestras preparadas, bajo su supervisión. "
             "Los esquemas se dibujan a mano con lápiz y papel; las cifras biológicas se limitan a las bien establecidas y los demás datos son inventados y rotulados «de ejemplo».")
build = make_build(MATERIALS)

O2 = "CN-BCMO-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (descripciones de ejemplo de cuatro moléculas de una célula). Molécula P: formada por cadenas de unidades llamadas aminoácidos; algunas aceleran reacciones y otras dan forma a la célula. "
     "Molécula Q: formada por unidades llamadas nucleótidos; guarda y transmite información. "
     "Molécula R: un azúcar simple, la glucosa, que se puede unir en cadenas largas; entrega energía. "
     "Molécula S: formada por ácidos grasos; no se disuelve en agua y forma parte de las membranas y de las reservas de energía.")
build(
    O2, 1, F,
    use="Aprenderé a distinguir las cuatro grandes biomoléculas, de qué unidades están hechas y qué función cumplen en la célula. Sirve para entender por qué la estructura química explica el funcionamiento celular.",
    prior=["Sé que la célula está formada por moléculas.", "Conozco los nombres de algunos nutrientes.", "Sé qué es una cadena de elementos repetidos."],
    explain=[
        "Las biomoléculas son las moléculas propias de los seres vivos. Las cuatro grandes familias son los carbohidratos, los lípidos, las proteínas y los ácidos nucleicos. Además, el agua es la molécula más abundante de la célula y es el medio donde ocurren muchas reacciones. Cada familia cumple funciones distintas y su forma química explica lo que hace.",
        "Muchas biomoléculas son polímeros, es decir, cadenas formadas por unidades repetidas llamadas monómeros. Las proteínas son cadenas de aminoácidos, de los cuales hay veinte tipos; los ácidos nucleicos, ADN y ARN, son cadenas de nucleótidos; los carbohidratos complejos, como el almidón, son cadenas de azúcares simples. Los lípidos no forman cadenas largas de la misma manera, pero se agrupan por no disolverse en agua.",
        "Las funciones principales son: carbohidratos, energía rápida y algunas estructuras; lípidos, membranas y reserva de energía; proteínas, enzimas, transporte y estructura; ácidos nucleicos, información genética. Estas funciones se complementan: por ejemplo, el ADN dirige qué proteínas se fabrican, y las proteínas, como las enzimas, permiten que ocurran las reacciones de la célula.",
    ],
    vocab=[("biomolécula", "molécula propia de los seres vivos"), ("monómero", "unidad que se repite para formar una cadena"), ("polímero", "cadena formada por muchas unidades repetidas"), ("aminoácido", "unidad que forma las proteínas"), ("nucleótido", "unidad que forma los ácidos nucleicos")],
    worked=[
        ("Clasificar una molécula", "Una molécula de ejemplo está formada por una cadena de aminoácidos y acelera una reacción. ¿A qué familia pertenece?",
         ["Una cadena de aminoácidos es una proteína.", "Las proteínas que aceleran reacciones se llaman enzimas."],
         "Es una proteína, de tipo enzima"),
        ("Contar enlaces", "Una cadena de ejemplo tiene 10 aminoácidos unidos de forma consecutiva. ¿Cuántas uniones hay entre aminoácidos?",
         ["Cada unión conecta dos aminoácidos vecinos.", "Entre 10 aminoácidos en fila hay 10 − 1 = 9 uniones."],
         "9 uniones"),
    ],
    mistakes=[("Decir que todos los lípidos son «grasas malas» que hay que evitar.", "Los lípidos forman las membranas de todas las células y guardan energía; su rol es esencial.", "Describe su función y deja las recomendaciones de salud para el profesional de la salud."),
              ("Creer que los ácidos nucleicos solo existen en el núcleo.", "El ARN también actúa en el citoplasma, por ejemplo al fabricar proteínas.", "Distingue ADN (guarda información) y ARN (la copia y la usa).")],
    T=[
        ("abc", "En Biología celular y molecular: ¿cuál es la unidad que forma las proteínas?", "El aminoácido", "El nucleótido", "La glucosa", "Las proteínas son cadenas de aminoácidos."),
        ("{F} ¿A qué familia de biomoléculas pertenece la molécula Q?", "Ácidos nucleicos", "La molécula Q está hecha de nucleótidos y guarda información: es un ácido nucleico."),
        ("{F} ¿Qué molécula (P, Q, R o S) no se disuelve en agua?", "S", "La descripción de S indica que no se disuelve en agua, rasgo de los lípidos."),
        ("abc", "{F} La molécula R es la glucosa. ¿Cuál es su función principal?", "Entregar energía", "Guardar información genética", "Formar la membrana", "La glucosa es una fuente de energía de la célula."),
        ("ab", "{F} La molécula P es una cadena de aminoácidos. ¿Cómo se llama una cadena de unidades repetidas?", "Un polímero", "Un monómero", "El monómero es la unidad; la cadena completa es el polímero."),
        ("{F} ¿Qué molécula (P, Q, R o S) incluye a las enzimas?", "P", "Las enzimas son proteínas, es decir, cadenas de aminoácidos como la molécula P."),
        ("=", "Una cadena de ejemplo tiene 120 aminoácidos unidos de forma consecutiva. ¿Cuántas uniones hay entre ellos?", "120-1", "Entre 120 unidades en fila hay una unión menos que unidades."),
        ("=", "Una proteína de ejemplo tiene 49 uniones entre aminoácidos vecinos, todos en una sola fila. ¿Cuántos aminoácidos tiene?", "49+1", "En una fila hay un aminoácido más que uniones.", " aminoácidos"),
        ("abc", "Una célula de ejemplo necesita fabricar su membrana. ¿Qué familia de biomoléculas usa como material principal?", "Lípidos", "Carbohidratos simples", "Ácidos nucleicos", "La membrana está formada principalmente por lípidos y proteínas."),
        ("abc", "Alguien afirma: «los lípidos son malos y las células no los necesitan». ¿Qué corriges?", "Las células los necesitan para formar membranas y guardar energía", "Tiene razón: las células no los usan", "Solo los usan los animales", "Todas las células tienen membrana, y esta contiene lípidos."),
        ("ab", "{F} Si el ADN dirige qué proteínas se fabrican y las proteínas permiten las reacciones, ¿qué relación hay entre moléculas Q y P?", "La molécula Q contiene la información para fabricar la P", "La molécula P contiene la información para fabricar la Q", "El ADN, un ácido nucleico, guarda la información y las proteínas ejecutan funciones."),
        ("abc", "{F} Una enzima de ejemplo pierde su función cuando se cambia un aminoácido clave. ¿Qué explica esto?", "La función depende de la secuencia y la forma de la proteína", "Las enzimas no son proteínas", "Los aminoácidos no influyen en nada", "Cambiar un aminoácido puede cambiar la forma, y de la forma depende la función."),
        ("abc", "Una dieta de ejemplo reduce mucho los azúcares, pero la persona mantiene energía por otras fuentes. ¿Qué conclusión sobre biomoléculas es correcta?", "Hay más de una molécula que puede entregar energía", "Solo los azúcares entregan energía", "Las proteínas no tienen ninguna función", "Los carbohidratos son una fuente de energía, pero los lípidos también la entregan y la guardan."),
    ],
    ctx=("abc", "Contexto: en el kiosco del liceo hay un cartel que dice «las proteínas son solo para el músculo». Quieres corregirlo con una frase breve. ¿Cuál eliges?", "Las proteínas también forman enzimas, transportan sustancias y dan estructura a muchas células", "Las proteínas no sirven para nada más", "Las proteínas son lo mismo que los lípidos", "La frase correcta amplía las funciones de las proteínas con lo visto en la clase."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un polímero?", "Una cadena formada por muchas unidades repetidas", "El polímero es la cadena formada por monómeros."),
        ("ab", "El ADN es un:", "Ácido nucleico", "Lípido", "El ADN está formado por nucleótidos, así que es un ácido nucleico."),
        ("ab", "Las enzimas son:", "Proteínas", "Azúcares", "Las enzimas son un tipo de proteína."),
    ],
    op=("Con la ficha {F}: (1) escribe en una tabla las moléculas P, Q, R y S con su familia, su unidad (si la tienen) y su función; (2) escribe una oración que relacione dos de ellas, por ejemplo cómo una depende de otra.",
        "(1) P: proteínas, aminoácidos, acelerar reacciones y dar forma; Q: ácidos nucleicos, nucleótidos, guardar información; R: carbohidrato, glucosa, entregar energía; S: lípidos, ácidos grasos, membranas y reserva. (2) La molécula Q guarda la información para fabricar las proteínas P.",
        ["tabla con las cuatro moléculas", "familia correcta de cada una", "función correcta de cada una", "relación entre dos moléculas bien explicada"],
        ["una tabla y una oración"],
        ["confundir monómero con polímero", "asignar a una familia la función de otra", "relación sin explicar el vínculo"],
        "Pregunta: «¿qué pasaría en la célula si faltara una de las cuatro familias?»."),
    reinforce="Escribe una tarjeta para cada familia de biomoléculas con su unidad y una función.",
    extend="Explica por qué la secuencia de aminoácidos de una proteína afecta su función, usando un ejemplo inventado.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (datos de ejemplo). La membrana celular es una doble capa de fosfolípidos: cada fosfolípido tiene una cabeza que se lleva bien con el agua y dos colas que la rechazan; las cabezas miran hacia el agua y las colas quedan en el interior. En esa doble capa hay proteínas. "
     "Tabla de ejemplo de cómo cruzan sustancias: oxígeno, molécula pequeña y sin carga: cruza directamente por la bicapa, a favor de su concentración; glucosa: cruza con ayuda de una proteína transportadora, a favor de su concentración; iones, partículas con carga: cruzan por canales o por bombas; "
     "las bombas gastan ATP, la molécula que entrega energía a la célula, y mueven iones en contra de su concentración. Concentración de ejemplo de un ion: afuera 10 unidades, adentro 2 unidades.")
build(
    O2, 2, F,
    use="Aprenderé cómo la estructura de la membrana celular explica qué sustancias pasan y cuáles no, y cómo se mueven. Sirve para entender el equilibrio entre la célula y su entorno.",
    prior=["Sé que la célula está rodeada por una membrana.", "Conozco las biomoléculas.", "Sé qué es una concentración."],
    explain=[
        "La membrana celular está formada por una bicapa de fosfolípidos con proteínas insertas. Cada fosfolípido tiene una cabeza hidrofílica, que se lleva bien con el agua, y colas hidrofóbicas, que la rechazan. Por eso se ordenan en dos capas con las colas hacia adentro. El interior de la bicapa no deja pasar fácilmente partículas con carga ni moléculas grandes.",
        "El modelo del mosaico fluido dice que los lípidos y las proteínas de la membrana se mueven y se acomodan como piezas de un mosaico que fluye. Las proteínas cumplen funciones: transportar sustancias, actuar como canales, reconocer señales y anclar la célula a su entorno.",
        "El transporte pasivo no gasta energía de la célula: las sustancias se mueven a favor de su concentración, de donde hay más hacia donde hay menos. Puede ser directo (oxígeno) o ayudado por proteínas (glucosa, canales). El agua se mueve por ósmosis. El transporte activo mueve sustancias en contra de su concentración y necesita energía, que entrega el ATP; por ejemplo, las bombas de iones.",
    ],
    vocab=[("fosfolípido", "lípido con cabeza que se lleva bien con el agua y colas que la rechazan"), ("mosaico fluido", "modelo en que lípidos y proteínas de la membrana se mueven"), ("transporte pasivo", "paso a favor de la concentración sin gasto de energía celular"), ("transporte activo", "paso en contra de la concentración con gasto de ATP"), ("ósmosis", "paso de agua a través de una membrana")],
    worked=[
        ("Dirección de la difusión", "Un ion de ejemplo tiene 10 unidades afuera y 2 adentro, y el canal está abierto. ¿Hacia dónde tiende a moverse por transporte pasivo?",
         ["El transporte pasivo va de donde hay más hacia donde hay menos.", "Hay más afuera (10) que adentro (2)."],
         "Hacia adentro de la célula"),
        ("Distinguir pasivo y activo", "Una sustancia sube de 2 a 10 unidades dentro de la célula, y la célula gasta ATP. ¿Qué transporte es?",
         ["Pasa de menos a más concentración: va en contra.", "Gasta ATP: necesita energía."],
         "Transporte activo"),
    ],
    mistakes=[("Pensar que la membrana es una pared rígida e impermeable.", "Es una estructura fluida y selectiva que deja pasar sustancias según su tamaño, carga y las proteínas disponibles.", "Describe la membrana como selectivamente permeable."),
              ("Decir que el transporte pasivo no necesita nada, ni siquiera proteínas.", "No gasta ATP, pero a veces usa proteínas transportadoras o canales.", "Separa «no gasta energía de la célula» de «no usa proteínas».")],
    T=[
        ("abc", "En Biología celular y molecular: ¿de qué está formada principalmente la membrana celular?", "Una bicapa de fosfolípidos con proteínas", "Una sola capa de azúcares", "Una pared rígida de proteínas", "La membrana es una bicapa de fosfolípidos con proteínas insertas."),
        ("{F} ¿Hacia dónde miran las colas de los fosfolípidos que rechazan el agua?", "Hacia el interior de la bicapa", "Las colas rechazan el agua y quedan entre las dos capas, lejos del agua."),
        ("{F} ¿Qué molécula entrega energía en el transporte activo?", "ATP", "La ficha indica que las bombas gastan ATP, que entrega energía a la célula."),
        ("abc", "{F} El oxígeno cruza directamente la bicapa. ¿Por qué puede hacerlo?", "Es pequeño y no tiene carga", "Es un ion con carga", "Usa una bomba que gasta ATP", "La bicapa deja pasar moléculas pequeñas sin carga."),
        ("ab", "{F} La glucosa cruza con ayuda de una proteína transportadora a favor de su concentración. ¿Qué transporte es?", "Transporte pasivo con ayuda de una proteína", "Transporte activo", "No gasta ATP y va a favor de la concentración, por lo que es pasivo."),
        ("{F} ¿Qué tipo de partículas cruzan por canales o por bombas? Responde en una palabra.", "Iones", "Las partículas con carga necesitan canales o bombas porque no cruzan por la bicapa."),
        ("=", "{F} ¿Cuántas unidades más hay afuera que adentro de la célula?", "10-2", "La diferencia de concentración se calcula restando lo de adentro a lo de afuera.", " unidades"),
        ("abc", "Otro ion de ejemplo tiene 3 unidades afuera y 9 adentro, y su canal se abre. ¿Qué esperas que pase por transporte pasivo?", "Sale de la célula, porque adentro hay más", "Entra a la célula, porque afuera hay más", "No se mueve nunca, porque tiene carga", "El transporte pasivo va de mayor a menor concentración, es decir, hacia afuera en este caso."),
        ("abc", "Una célula de ejemplo bombea un ion hacia afuera, donde ya hay más concentración, y gasta ATP. ¿Qué transporte realiza?", "Transporte activo", "Transporte pasivo", "Ósmosis", "Moverse en contra de la concentración exige energía y es transporte activo."),
        ("abc", "Alguien dice: «la membrana es una pared que no deja pasar nada». ¿Qué corriges?", "Es selectiva: deja pasar algunas sustancias, directamente o con proteínas", "Tiene razón y por eso las células no intercambian nada", "Deja pasar todo sin excepción", "La membrana es selectivamente permeable, no una pared cerrada."),
        ("ab", "{F} ¿Por qué un ion no cruza fácilmente el interior de la bicapa?", "Porque tiene carga y el interior de la bicapa es poco afín a las cargas", "Porque es demasiado grande para cualquier membrana", "El interior de la bicapa son colas de lípidos, que rechazan partículas con carga."),
        ("abc", "Una célula de ejemplo tiene muchas bombas. ¿Qué necesita esa célula en abundancia para que funcionen?", "ATP", "Almidón", "ADN adicional", "Las bombas gastan ATP para mover iones en contra de su concentración."),
        ("abc", "{F} Una proteína de membrana defectuosa deja de transportar la glucosa. ¿Qué pasará con el ingreso de glucosa si no tiene otra vía?", "Disminuirá, porque la glucosa depende de esa proteína", "Aumentará por la bicapa directamente", "No cambiará nada", "La glucosa no cruza bien la bicapa y requiere proteína transportadora."),
    ],
    ctx=("abc", "Contexto: en una feria del liceo debes explicar con una maqueta de cartulina cómo funciona la membrana. ¿Qué incluyes?", "Dos capas de fosfolípidos con colas hacia adentro y proteínas que atraviesan la bicapa", "Una sola capa lisa sin proteínas", "Una pared gruesa sin aberturas", "La maqueta debe mostrar bicapa y proteínas, que explican el paso selectivo."),
    sc=[
        ("En Biología celular y molecular: ¿qué es el transporte pasivo?", "Paso de sustancias a favor de su concentración sin gasto de energía celular", "El transporte pasivo va de más a menos concentración."),
        ("ab", "El transporte activo necesita:", "ATP", "Que haya igual concentración a ambos lados", "El transporte activo gasta ATP porque va en contra de la concentración."),
        ("ab", "La membrana celular es:", "Selectiva", "Impermeable a todo", "Deja pasar algunas sustancias y otras no."),
    ],
    op=("Con la tabla de la ficha {F}: (1) clasifica el paso del oxígeno, de la glucosa y de los iones por bomba como pasivo o activo; (2) dibuja un esquema simple de la bicapa con una proteína de canal y rotula cabeza, cola y canal; (3) explica con una frase por qué la membrana es selectiva.",
        "(1) Oxígeno: pasivo directo; glucosa: pasivo con transportadora; iones por bomba: activo. (2) Dos capas con cabezas hacia afuera y colas hacia adentro, y un canal que las atraviesa. (3) Porque deja pasar algunas sustancias según su tamaño y carga, y otras solo con proteínas.",
        ["clasificación correcta de tres pasos", "esquema con cabeza, cola y canal rotulados", "explicación de la selectividad"],
        ["tabla o lista, un esquema y una frase"],
        ["confundir cabeza con cola", "decir que el transporte activo va a favor de la concentración", "no rotular el canal"],
        "Pregunta: «¿qué pasaría si la bicapa tuviera solo lípidos y ninguna proteína?»."),
    reinforce="Haz una tabla con tres sustancias de la ficha, la vía por donde cruzan y si gastan ATP.",
    extend="Explica por qué la ósmosis es un tipo de transporte pasivo y qué ocurriría con una célula animal si el agua entrara sin control.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (tabla de ejemplo de organelos). Núcleo: guarda el ADN. Ribosoma: fabrica proteínas. Retículo endoplasmático rugoso: tiene ribosomas y ayuda a fabricar y plegar proteínas. Aparato de Golgi: modifica, empaqueta y envía sustancias. "
     "Mitocondria: obtiene ATP de los nutrientes y tiene su propio ADN. Lisosoma: digiere sustancias. Cloroplasto: realiza la fotosíntesis, está en plantas y algas y tiene su propio ADN. "
     "Dos tipos de célula de ejemplo: la célula 1 no tiene núcleo ni organelos con membrana; la célula 2 tiene núcleo y organelos con membrana.")
build(
    O2, 3, F,
    use="Aprenderé la organización de la célula en organelos y cómo trabajan juntos. Sirve para explicar cómo una célula fabrica, transporta y recicla lo que necesita.",
    prior=["Conozco las biomoléculas.", "Sé que la membrana separa la célula de su entorno.", "Sé que hay células sin núcleo."],
    explain=[
        "Las células eucariontes, como las de animales, plantas, hongos y protistas, tienen un núcleo con ADN y organelos rodeados de membrana. Las células procariontes, como las bacterias, no tienen núcleo ni organelos con membrana, pero sí ADN, ribosomas y membrana celular. Los organelos permiten dividir el trabajo: cada uno realiza reacciones propias en un espacio separado.",
        "Los organelos cooperan. Una proteína que la célula va a exportar se fabrica en ribosomas del retículo rugoso, pasa al aparato de Golgi, donde se modifica y se empaqueta en una vesícula, y la vesícula la lleva a la membrana para liberarla. Las mitocondrias aportan el ATP que mueve todo ese trabajo, y los lisosomas reciclan lo que sobra.",
        "Mitocondrias y cloroplastos tienen su propio ADN y ribosomas parecidos a los de las bacterias. La teoría endosimbiótica propone que se originaron cuando una célula antigua incorporó bacterias que terminaron viviendo dentro de ella. Esta idea explica un rasgo de la continuidad y la evolución de la célula, y se apoya en esas evidencias.",
    ],
    vocab=[("eucarionte", "célula con núcleo y organelos con membrana"), ("procarionte", "célula sin núcleo ni organelos con membrana"), ("vesícula", "bolsa de membrana que transporta sustancias"), ("fotosíntesis", "proceso en que se obtiene alimento a partir de luz, agua y dióxido de carbono"), ("endosimbiosis", "relación en que un organismo vive dentro de otro")],
    worked=[
        ("Ruta de una proteína exportada", "Ordena el camino de una proteína que sale de la célula: Golgi, ribosoma del retículo, membrana.",
         ["Se fabrica en el ribosoma del retículo.", "Pasa al Golgi, donde se modifica y se empaqueta.", "La vesícula la lleva a la membrana para liberarla."],
         "Ribosoma del retículo, Golgi, membrana"),
        ("Clasificar una célula", "La célula 1 de la ficha no tiene núcleo. ¿Es eucarionte o procarionte?",
         ["Una célula sin núcleo ni organelos con membrana es procarionte.", "Un ejemplo de este tipo son las bacterias."],
         "Es procarionte"),
    ],
    mistakes=[("Decir que la mitocondria «fabrica energía».", "La energía no se fabrica: la mitocondria transforma la energía de los nutrientes en ATP.", "Escribe «obtiene ATP a partir de los nutrientes»."),
              ("Pensar que los ribosomas tienen membrana.", "Los ribosomas no tienen membrana y están en procariontes y eucariontes.", "Usa «organelos con membrana» solo para los que corresponden.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué organelo guarda el ADN en una célula eucarionte?", "El núcleo", "El lisosoma", "El ribosoma", "El núcleo contiene el ADN de la célula eucarionte."),
        ("{F} ¿Qué organelo obtiene ATP de los nutrientes?", "La mitocondria", "La ficha indica que la mitocondria obtiene ATP de los nutrientes."),
        ("{F} ¿Qué organelo realiza la fotosíntesis?", "El cloroplasto", "El cloroplasto es el organelo de plantas y algas que realiza la fotosíntesis."),
        ("abc", "{F} ¿Qué función cumple el aparato de Golgi?", "Modificar, empaquetar y enviar sustancias", "Digerir sustancias", "Guardar el ADN", "El Golgi trabaja como centro de empaque y envío."),
        ("ab", "{F} La célula 2 tiene núcleo y organelos con membrana. ¿Qué tipo de célula es?", "Eucarionte", "Procarionte", "El núcleo y los organelos con membrana son propios de las células eucariontes."),
        ("{F} ¿Qué organelo digiere sustancias?", "El lisosoma", "La ficha atribuye la digestión de sustancias al lisosoma."),
        ("abc", "{F} ¿Qué organelo recibe una proteína ya fabricada para modificarla y empaquetarla en una vesícula?", "El aparato de Golgi", "El lisosoma", "La mitocondria", "El Golgi modifica y empaqueta; el lisosoma digiere y la mitocondria obtiene ATP."),
        ("abc", "{F} Dos células de ejemplo: una de músculo, que gasta mucha energía, y una de piel, que gasta menos. ¿Cuál esperas que tenga más mitocondrias?", "La de músculo, porque necesita más ATP", "La de piel, porque está en la superficie", "Ninguna, porque no dependen del ATP", "Una célula que gasta más energía necesita más mitocondrias para obtener ATP."),
        ("=", "Una célula de ejemplo tiene 250 mitocondrias y otra tiene 40. ¿Cuántas mitocondrias más tiene la primera?", "250-40", "La diferencia se obtiene restando la cantidad menor a la mayor.", " mitocondrias"),
        ("abc", "{F} Un cloroplasto y una mitocondria tienen su propio ADN y ribosomas parecidos a los de bacterias. ¿Qué idea apoyan?", "La teoría endosimbiótica", "Que no tienen ninguna función", "Que son procariontes completos hoy", "Tener ADN propio y ribosomas de tipo bacteriano apoya que provienen de bacterias incorporadas."),
        ("abc", "Un compañero dice: «los ribosomas son organelos con membrana porque están en el núcleo». ¿Qué corriges?", "Los ribosomas no tienen membrana y están también fuera del núcleo", "Tiene razón en todo", "Los ribosomas no existen en bacterias", "Los ribosomas son estructuras sin membrana presentes en procariontes y eucariontes."),
        ("ab", "{F} Una enfermedad de ejemplo impide que los lisosomas funcionen y se acumulan restos dentro de la célula. ¿Qué proceso falla?", "El reciclaje y la digestión de sustancias", "La fotosíntesis", "El lisosoma digiere sustancias, por eso su falla deja restos acumulados."),
        ("abc", "{F} ¿Qué evidencia de la ficha apoya que mitocondrias y cloroplastos tienen un origen independiente del resto de la célula?", "Que ambos tienen su propio ADN", "Que ambos están rodeados de agua", "Que ambos fabrican lípidos", "El ADN propio es un indicio de un origen independiente, distinto del resto de la célula."),
    ],
    ctx=("abc", "Contexto: para un cartel del laboratorio escolar debes mostrar cómo una célula del páncreas, que produce una hormona proteica, usa sus organelos. ¿Qué esquema eliges?", "Ribosomas del retículo, Golgi, vesícula y membrana, con mitocondrias aportando ATP", "Solo el núcleo con una flecha", "Solo cloroplastos con una flecha", "El esquema correcto sigue el camino de la proteína y muestra de dónde viene la energía."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una célula eucarionte?", "Una célula con núcleo y organelos con membrana", "La eucarionte tiene núcleo y organelos membranosos."),
        ("ab", "Las bacterias son:", "Procariontes", "Eucariontes", "Las bacterias no tienen núcleo ni organelos con membrana."),
        ("ab", "La mitocondria obtiene:", "ATP a partir de nutrientes", "ADN a partir de luz", "La mitocondria transforma la energía de los nutrientes en ATP."),
    ],
    op=("Con la tabla de la ficha {F}: (1) escribe una tabla de cinco organelos con su función; (2) dibuja un esquema con flechas del camino de una proteína que sale de la célula; (3) explica en una frase por qué se piensa que mitocondrias y cloroplastos provienen de bacterias.",
        "(1) Núcleo guarda ADN; ribosoma fabrica proteínas; Golgi empaqueta; mitocondria obtiene ATP; lisosoma digiere. (2) Ribosoma del retículo, Golgi, vesícula, membrana. (3) Porque tienen su propio ADN y ribosomas parecidos a los de bacterias.",
        ["cinco organelos con su función", "esquema en el orden correcto", "explicación con evidencia del ADN propio"],
        ["una tabla, un esquema y una frase"],
        ["atribuir al núcleo la fabricación de proteínas", "invertir el orden de la ruta", "no mencionar la evidencia"],
        "Pregunta: «¿qué organelo sería más importante para una célula muy activa?»."),
    reinforce="Escribe una oración que una dos organelos, por ejemplo mitocondria con ribosoma, explicando su cooperación.",
    extend="Explica qué otras evidencias podrían apoyar la teoría endosimbiótica y qué dato la debilitaría.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (datos de ejemplo). Ciclo celular: interfase (G1, S y G2) y fase M, que incluye la mitosis y la división del citoplasma. En la fase S se copia el ADN. "
     "Conteo de ejemplo de 100 células de una raíz de planta observadas en una lámina preparada: interfase 90, profase 4, metafase 2, anafase 2, telofase 2. "
     "Especie de ejemplo, inventada: sus células del cuerpo tienen 8 cromosomas. Cantidad de ADN de ejemplo (unidades arbitrarias): una célula en G1 tiene 2 unidades.")
build(
    O2, 4, F,
    use="Aprenderé cómo se reproduce la célula: ciclo celular, mitosis y meiosis, y qué significa que el ADN se copie y se reparta. Sirve para entender el crecimiento, la reparación y la continuidad de la vida.",
    prior=["Sé que el ADN está en los cromosomas.", "Conozco la teoría celular.", "Sé leer porcentajes y conteos."],
    explain=[
        "Toda célula proviene de otra célula, y eso ocurre por división celular. En las eucariontes, el ciclo celular alterna dos grandes etapas. La interfase incluye G1 (crecimiento), S (copia del ADN) y G2 (preparación). La fase M incluye la mitosis, que reparte los cromosomas, y la citocinesis, que divide el citoplasma. En los procariontes, el equivalente más simple es la fisión binaria.",
        "La mitosis tiene cuatro fases: profase (los cromosomas se hacen visibles), metafase (se alinean en el centro), anafase (se separan las copias hacia polos opuestos) y telofase (se forman los dos núcleos). El resultado son dos células hijas con la misma información que la célula madre. La mitosis permite crecer, reponer células y reparar tejidos.",
        "La meiosis es otro tipo de división: ocurre solo en las células que forman gametos, como óvulos y espermatozoides, y reduce a la mitad el número de cromosomas. Gracias a eso, cuando dos gametos se unen en la fecundación, se recupera el número normal. La meiosis, además, mezcla la información genética y por eso favorece la variación entre individuos.",
    ],
    vocab=[("ciclo celular", "secuencia de etapas por las que pasa una célula desde que nace hasta que se divide"), ("mitosis", "división que reparte copias iguales de los cromosomas entre dos células hijas"), ("meiosis", "división que reduce a la mitad los cromosomas para formar gametos"), ("gameto", "célula sexual, como el óvulo o el espermatozoide"), ("cromosoma", "estructura que contiene ADN y proteínas")],
    worked=[
        ("Leer un conteo", "En el conteo de ejemplo, ¿qué porcentaje de células está en mitosis?",
         ["Mitosis incluye profase, metafase, anafase y telofase.", "Suman 4 + 2 + 2 + 2 = 10 células de 100.", "10 de 100 es 10 %."],
         "10 %"),
        ("Cromosomas en mitosis y en meiosis", "En la especie de ejemplo, las células del cuerpo tienen 8 cromosomas. ¿Cuántos tendrán las células hijas por mitosis y los gametos por meiosis?",
         ["Mitosis: las hijas tienen el mismo número que la madre: 8.", "Meiosis: se reduce a la mitad: 8 ÷ 2 = 4."],
         "8 por mitosis y 4 por meiosis"),
    ],
    mistakes=[("Decir que la mitosis y la meiosis son lo mismo.", "La mitosis da dos células iguales a la madre; la meiosis da gametos con la mitad de cromosomas.", "Compara el resultado de cada una: número de células y de cromosomas."),
              ("Pensar que el ADN se copia durante la mitosis.", "El ADN se copia en la fase S de la interfase, antes de la mitosis.", "Ubica la copia del ADN en la interfase.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿en qué fase del ciclo celular se copia el ADN?", "En la fase S de la interfase", "En la anafase", "En la citocinesis", "El ADN se duplica en la fase S, antes de la mitosis."),
        ("{F} ¿Cuántas células de las 100 del conteo de ejemplo están en interfase?", "90", "La ficha indica que 90 de las 100 células están en interfase."),
        ("{F} ¿Qué fase de la mitosis tiene los cromosomas alineados en el centro?", "Metafase", "En metafase los cromosomas se alinean en el centro de la célula."),
        ("abc", "{F} ¿Qué resultado tiene una mitosis?", "Dos células hijas con la misma información que la madre", "Cuatro gametos con la mitad de cromosomas", "Una célula sin ADN", "La mitosis produce dos células iguales entre sí y a la madre."),
        ("ab", "{F} ¿Qué etapa del ciclo dura más según el conteo de ejemplo?", "La interfase", "La metafase", "El 90 % de las células está en interfase, lo que indica que es la etapa más larga."),
        ("{F} ¿Cuál es el nombre de la división que forma gametos?", "Meiosis", "La meiosis produce gametos con la mitad de cromosomas."),
        ("=", "{F} Con el conteo de ejemplo, ¿cuántas de las 100 células no están ni en anafase ni en telofase?", "100-2-2", "Al total se le restan las células en anafase y en telofase.", " células"),
        ("{F} Una célula en G1 tiene 2 unidades de ADN. ¿Cuántas unidades tendrá al terminar la fase S, antes de la mitosis?", "4", "En la fase S se copia el ADN, así que la cantidad se duplica."),
        ("abc", "Una especie de ejemplo inventada tiene 12 cromosomas en las células del cuerpo. ¿Cuántos cromosomas tiene un gameto de esa especie?", "6", "12", "24", "La meiosis reduce a la mitad los 12 cromosomas, quedando 6 en cada gameto."),
        ("abc", "Dos gametos de la especie de ejemplo con 12 cromosomas en el cuerpo se unen en la fecundación. ¿Cuántos cromosomas tiene la célula resultante?", "12", "6", "24", "6 más 6 recuperan el número normal de la especie."),
        ("ab", "Un compañero dice: «el ADN se copia durante la anafase». ¿Qué corriges?", "El ADN se copia antes, en la fase S de la interfase", "Tiene razón: la anafase copia el ADN", "En anafase se separan las copias ya hechas hacia polos opuestos."),
        ("abc", "{F} Si en un tejido de ejemplo el porcentaje de células en mitosis aumenta de 10 % a 25 %, ¿qué podría estar ocurriendo?", "El tejido está creciendo o reparándose, con más divisiones", "Las células dejaron de dividirse", "Las células pasaron a ser gametos", "Más células en mitosis indica más divisiones, como en crecimiento o reparación."),
        ("abc", "¿Por qué la meiosis favorece la variación entre individuos?", "Porque mezcla la información genética de los gametos", "Porque copia el ADN dos veces", "Porque produce células idénticas a la madre", "La mezcla de información en la meiosis hace que cada gameto sea distinto."),
    ],
    ctx=("abc", "Contexto: una herida de ejemplo en la piel cierra en pocos días. Para explicarlo en un afiche del liceo, ¿qué proceso celular destacas?", "Mitosis: las células vecinas se dividen y reponen las perdidas", "Meiosis: se forman gametos nuevos en la piel", "Fotosíntesis: la piel hace su propio alimento", "La reparación de tejidos se explica por la mitosis, que repone células."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la mitosis?", "Una división que reparte copias iguales de los cromosomas entre dos células hijas", "La mitosis conserva el número de cromosomas."),
        ("ab", "Los gametos se forman por:", "Meiosis", "Mitosis", "La meiosis reduce a la mitad el número de cromosomas."),
        ("ab", "La interfase incluye:", "G1, S y G2", "Profase, metafase y anafase", "La interfase tiene tres etapas, y en S se copia el ADN."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula el porcentaje de células en mitosis; (2) dibuja un esquema de una célula de la especie de ejemplo con 8 cromosomas dividiéndose por mitosis, mostrando las dos hijas; (3) compara en una tabla el resultado de la mitosis y el de la meiosis.",
        "(1) 4 + 2 + 2 + 2 = 10 células de 100, es decir, 10 %. (2) Una célula con 8 cromosomas que da dos hijas con 8 cada una. (3) Mitosis: 2 células, 8 cromosomas, crecimiento y reparación; meiosis: gametos con 4 cromosomas, reproducción sexual.",
        ["porcentaje bien calculado", "esquema con el número correcto de cromosomas", "tabla comparativa coherente"],
        ["un cálculo, un esquema y una tabla"],
        ["no sumar las cuatro fases", "dibujar hijas con 4 cromosomas en mitosis", "mezclar los resultados de ambas divisiones"],
        "Pregunta: «¿cómo cambiaría el conteo si el tejido estuviera creciendo muy rápido?»."),
    reinforce="Ordena los pasos del ciclo celular desde G1 hasta la citocinesis y rotula en cuál se copia el ADN.",
    extend="Explica por qué un error en el reparto de cromosomas durante la mitosis puede afectar a las células hijas.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (cuatro situaciones de ejemplo en células). Situación 1: una célula usa glucosa y oxígeno para obtener ATP. Situación 2: una célula degrada un organelo dañado y reutiliza sus componentes. "
     "Situación 3: una célula se desplaza emitiendo extensiones que se apoyan en filamentos de actina, parte del citoesqueleto. Situación 4: una molécula señal, una hormona, se une a un receptor de la membrana de otra célula y cambia lo que esta célula hace. "
     "Dato de ejemplo: una célula tiene 60 proteínas de un tipo y cada hora se degradan 6 y se fabrican 6 nuevas.")
build(
    O2, 5, F,
    use="Aprenderé cómo la célula se mantiene y se renueva: metabolismo, recambio de moléculas, movimiento y comunicación, y cómo todo eso se conecta con la continuidad de la vida y su evolución. Sirve para comparar explicaciones sobre cómo la célula funciona como un sistema.",
    prior=["Conozco las biomoléculas y los organelos.", "Sé qué es el ATP.", "Sé qué es la membrana celular."],
    explain=[
        "El metabolismo es el conjunto de reacciones químicas de la célula. El catabolismo rompe moléculas para obtener energía en forma de ATP, y el anabolismo construye moléculas más complejas usando esa energía. Ambos son procesos acoplados: el ATP que se obtiene en uno se gasta en el otro. La célula también reemplaza sus propias moléculas: las proteínas se degradan y se fabrican de nuevo, y los organelos dañados se reciclan por un proceso llamado autofagia.",
        "La motilidad es el movimiento de la célula o de sus partes. Se apoya en el citoesqueleto, una red de filamentos de proteínas, entre ellos los de actina y los microtúbulos. Gracias a ellos la célula cambia de forma, transporta vesículas y se divide. La comunicación ocurre cuando una molécula señal se une a un receptor y provoca una respuesta en la célula.",
        "Estas funciones comparten una base común en todos los seres vivos: el ADN, el ATP y los mismos tipos de biomoléculas, lo que apoya el origen común de la vida. La reproducción celular, que copia el ADN con mucha fidelidad, asegura la continuidad, y los pequeños cambios que ocurren de vez en cuando dan la variación sobre la que actúa la evolución.",
    ],
    vocab=[("metabolismo", "conjunto de reacciones químicas de la célula"), ("catabolismo", "reacciones que rompen moléculas para obtener energía"), ("anabolismo", "reacciones que construyen moléculas usando energía"), ("citoesqueleto", "red de filamentos de proteínas que da forma y permite el movimiento"), ("receptor", "proteína que se une a una molécula señal y desencadena una respuesta")],
    worked=[
        ("Clasificar una situación", "La situación 1 usa glucosa y oxígeno para obtener ATP. ¿Es catabolismo o anabolismo?",
         ["Rompe glucosa para obtener energía.", "Romper moléculas para obtener ATP es catabolismo."],
         "Catabolismo"),
        ("Recambio constante", "La célula de la ficha tiene 60 proteínas de un tipo, degrada 6 por hora y fabrica 6 por hora. ¿Cambia la cantidad total?",
         ["Se pierden 6 y se ganan 6 cada hora.", "La cantidad se mantiene en 60, aunque las proteínas son renovadas."],
         "No cambia, aunque las proteínas se renuevan"),
    ],
    mistakes=[("Creer que si la cantidad de una molécula no cambia, entonces la molécula no se renueva.", "Puede mantenerse constante porque se degrada y se fabrica al mismo ritmo.", "Distingue cantidad total y ritmo de recambio."),
              ("Confundir receptor con molécula señal.", "La señal es la molécula que viene de afuera; el receptor es la proteína que la reconoce.", "Dibuja la llave (señal) y la cerradura (receptor).")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es el metabolismo?", "El conjunto de reacciones químicas de la célula", "La división celular", "La forma de la membrana", "El metabolismo reúne las reacciones que obtienen y usan energía y materia."),
        ("{F} ¿Qué situación (1, 2, 3 o 4) describe comunicación celular?", "Situación 4", "En la situación 4 una hormona se une a un receptor y cambia lo que hace la célula."),
        ("{F} ¿Qué parte del citoesqueleto se menciona en la situación 3?", "Los filamentos de actina", "La situación 3 señala que las extensiones se apoyan en filamentos de actina."),
        ("abc", "{F} ¿Qué proceso describe la situación 2?", "Autofagia o reciclaje de un organelo dañado", "Fotosíntesis", "Mitosis", "Degradar un organelo dañado y reutilizar sus componentes es reciclaje celular."),
        ("ab", "Una célula de ejemplo une aminoácidos para fabricar una proteína nueva y gasta ATP. ¿Qué tipo de reacciones realiza?", "Anabólicas, porque construyen moléculas usando energía", "Catabólicas, porque rompen moléculas para obtener energía", "Construir una molécula con gasto de ATP es anabolismo."),
        ("{F} ¿Qué molécula de la situación 4 se une al receptor? Responde en una palabra.", "Hormona", "La molécula señal de la situación 4 es una hormona."),
        ("=", "{F} Si la célula con 60 proteínas degrada 6 por hora y no fabrica ninguna, ¿cuántas quedan tras 3 horas?", "60-6*3", "Cada hora se pierden 6 proteínas, así que en tres horas se pierden 18.", " proteínas"),
        ("=", "{F} Si degrada 6 por hora y fabrica 10 por hora, ¿cuántas proteínas habrá tras 2 horas?", "60+(10-6)*2", "Cada hora la ganancia neta es 4 proteínas, es decir, 8 en dos horas.", " proteínas"),
        ("abc", "{F} Una célula de ejemplo ya no se desplaza porque sus filamentos de actina no funcionan. ¿Qué situación se ve afectada?", "La situación 3, de movimiento", "La situación 4, de comunicación", "La situación 1, de obtención de ATP", "Sin filamentos de actina la célula no emite las extensiones para desplazarse."),
        ("abc", "{F} Una célula no tiene el receptor de la hormona. ¿Qué esperas?", "Que no responda a la hormona", "Que responda igual", "Que se divida de inmediato", "Sin receptor, la señal no se reconoce y no hay respuesta."),
        ("ab", "Un estudiante dice: «si el número de proteínas no cambia, es que no se renuevan». ¿Qué corriges?", "Puede mantenerse el número porque se degradan y se fabrican al mismo ritmo", "Tiene razón: no cambia nada si el número es el mismo", "Se pueden renovar todas y mantener constante la cantidad."),
        ("abc", "{F} ¿Qué relación hay entre las situaciones 1 y 2?", "La 1 aporta el ATP que se usa en procesos como el reciclaje de la 2", "Son procesos que no tienen ninguna relación", "La 2 produce glucosa para la 1", "El ATP obtenido sostiene el trabajo de la célula, incluido el reciclaje."),
        ("abc", "Todos los seres vivos de ejemplo usan ADN y ATP. ¿Qué apoya esto?", "Que la vida tiene un origen común", "Que los seres vivos no cambian", "Que cada especie surgió sin relación con las demás", "Compartir moléculas básicas es consistente con un origen común."),
    ],
    ctx=("abc", "Contexto: en el cartel de un laboratorio escolar debes explicar por qué una célula nerviosa necesita muchas mitocondrias y mucho recambio de proteínas. ¿Qué mensaje eliges?", "Es muy activa: gasta mucho ATP y renueva constantemente sus proteínas", "Es una célula inactiva que casi no gasta energía", "Es una célula sin metabolismo", "El mensaje refleja actividad alta, ATP y recambio constante."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un receptor?", "Una proteína que se une a una molécula señal y desencadena una respuesta", "El receptor reconoce la señal y activa la respuesta."),
        ("ab", "El anabolismo:", "Construye moléculas usando energía", "Rompe moléculas para obtener energía", "Anabolismo es construir; catabolismo es romper."),
        ("ab", "El citoesqueleto permite:", "Dar forma y mover la célula y sus partes", "Guardar el ADN", "Está formado por filamentos de proteínas que sostienen y mueven."),
    ],
    op=("Con las cuatro situaciones de la ficha {F}: (1) rotula cada una como metabolismo, recambio, motilidad o comunicación; (2) elige una y explica qué molécula o estructura interviene; (3) escribe cómo esa función contribuye a la continuidad de la vida de la célula.",
        "(1) Situación 1 metabolismo; 2 recambio; 3 motilidad; 4 comunicación. (2) La situación 4: la hormona se une al receptor de la membrana. (3) Permite que la célula responda a su ambiente, se ajuste y siga viva.",
        ["cuatro rótulos correctos", "molécula o estructura bien identificada", "relación con la continuidad explicada"],
        ["una lista y dos oraciones"],
        ["confundir recambio con metabolismo", "no nombrar la molécula o estructura", "no relacionar con la continuidad"],
        "Pregunta: «¿qué pasaría si fallara la función que elegiste?»."),
    reinforce="Escribe tres frases, una para metabolismo, una para motilidad y una para comunicación, cada una con una molécula o estructura.",
    extend="Explica cómo la fidelidad en la copia del ADN y los pequeños cambios ocasionales permiten a la vez continuidad y evolución.",
)
