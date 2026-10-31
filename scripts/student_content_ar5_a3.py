"""Cuaderno del estudiante de 5.º básico Artes Visuales: AR05 OA 03 (dominio de materiales, herramientas y medios digitales)."""
from __future__ import annotations

from student_content_ar5_a import lesson, m, task, w
from student_lessons import ex

OA3 = "AR05 OA 03"

# ---------------------------------------------------------------- Clase 1
lesson(
    OA3, 1,
    "Hoja, lápiz y los materiales que tengas en casa: papeles, cartones, retazos de tela, lana, hojas secas, envases limpios, témpera, lápices, cola fría. Las listas de materiales están escritas aquí, así que no necesitas tenerlos todos.",
    "Aprenderé a reconocer los materiales y las herramientas del arte, para qué sirve cada uno, y a elegirlos según la intención de mi obra. Sirve para trabajar con seguridad y con una razón detrás de cada elección.",
    ["Sé que una obra tiene una intención propia.", "Sé usar lápices, pinceles y tijeras con cuidado."],
    [
        "Un material es aquello con lo que se hace una obra. Hay varios grupos. Los materiales de modelado se pueden moldear: arcilla, plasticina y masa. Los de reciclaje son objetos que ya se usaron, como cajas y envases limpios. Los naturales vienen de la naturaleza, como hojas secas o piedras. También hay papeles, cartones, pegamentos, lápices, pinturas y textiles, que son telas, lanas e hilos. Las imágenes digitales son fotos o dibujos que están en una pantalla.",
        "Una herramienta es lo que uso para trabajar el material. Para dibujar sirven los lápices; para pintar, las brochas y los pinceles; para cortar, las tijeras de punta redonda; para unir, el pegamento; para modelar, las manos y la esteca, que es una herramienta con puntas o bordes para marcar detalles en arcilla o plasticina. Las herramientas tecnológicas son la cámara de video y el proyector multimedia, que muestra imágenes grandes en una pared. La sierra de calar corta madera y la usa solo un adulto con formación.",
        "Cada material tiene propiedades: puede ser blando o duro, liso o rugoso, liviano o pesado, transparente o no. Una intención se logra mejor con el material adecuado. Para mostrar un cerro rugoso, sirve el cartón arrugado; para mostrar suavidad, sirve la lana o el algodón. Antes de empezar, escribo qué material y qué herramienta usaré, y por qué. Si una herramienta es peligrosa, pido ayuda a un adulto.",
    ],
    [("material", "aquello con lo que se hace una obra"), ("herramienta", "objeto que uso para trabajar un material"), ("esteca", "herramienta con puntas o bordes para marcar detalles en arcilla o plasticina"), ("textil", "material hecho de tela, lana o hilo"), ("procedimiento", "la manera de hacer una obra con los materiales y herramientas")],
    [
        w("Material según la intención", "Quieres hacer un cerro con textura rugosa y de relieve. ¿Qué material eliges?", ["Pienso en una propiedad: rugoso.", "El cartón arrugado y pegado hace relieve rugoso.", "El papel liso daría una superficie suave."], "Cartón arrugado"),
        w("Herramienta según la acción", "Necesitas marcar líneas finas de pelo en un animal de plasticina. ¿Qué herramienta usas?", ["La acción es marcar detalles en un material de modelado.", "La esteca sirve para eso.", "Las tijeras no sirven para marcar."], "La esteca"),
    ],
    [
        m("Usar un material solo porque lo tengo a mano, sin pensar en la intención.", "El material cambia lo que la obra comunica.", "Pregunta qué propiedad del material ayuda a mi idea."),
        m("Usar una herramienta peligrosa sin un adulto, como la sierra de calar.", "Puede causar un accidente grave.", "Las herramientas eléctricas o de corte difícil las usa un adulto con formación."),
    ],
    [
        ex("La plasticina, ¿es un material de modelado o un material textil?", "De modelado", "La plasticina se moldea con las manos."),
        ex("Una caja de cartón limpia que ya se usó, ¿es un material de reciclaje o un material natural?", "De reciclaje", "Ya tuvo un uso antes y se reutiliza."),
        ex("¿Qué herramienta sirve para marcar detalles en arcilla: la esteca o el proyector multimedia?", "La esteca", "La esteca tiene puntas o bordes para marcar detalles."),
    ],
    [
        ex("Una hoja seca y una piedra pequeña, ¿son materiales naturales o de reciclaje?", "Naturales", "Vienen de la naturaleza."),
        ex("La lana y un retazo de tela, ¿son materiales textiles o pinturas?", "Textiles", "Los textiles están hechos de tela, lana o hilo."),
        ex("¿Qué hace el proyector multimedia: muestra una imagen grande en una pared o corta madera?", "Muestra una imagen grande en una pared", "Es una herramienta tecnológica para proyectar imágenes."),
    ],
    [
        ex("Quieres mostrar la suavidad de una nube en un trabajo con relieve. ¿Qué material eliges: algodón o piedra?", "Algodón", "El algodón es blando y suave."),
        ex("Necesitas cortar papel para una obra. ¿Qué usas: tijeras de punta redonda o sierra de calar?", "Tijeras de punta redonda", "La sierra de calar no se usa para papel y es peligrosa para estudiantes."),
        ex("Quieres unir dos cartones. ¿Qué usas: cola fría o un lápiz de mina?", "Cola fría", "La cola fría es un pegamento."),
    ],
    [
        ex("Quieres que un árbol de tu maqueta parezca liviano y que se mueva con el viento. ¿Qué eliges para las hojas: papel de seda o piedras?", "Papel de seda", "El papel de seda es liviano y se mueve con facilidad."),
        ex("Una compañera dice: «Usé una sierra de calar para mi obra porque era la más rápida». ¿Hizo bien?", "No", "La sierra de calar solo la usa un adulto con formación."),
    ],
    [
        ex("Quieres hacer una escultura pesada y firme. ¿Qué material elegirías: arcilla o papel de seda?", "Arcilla", "La arcilla es pesada y firme cuando se seca."),
        ex("Quieres mostrar una playa de arena en una obra. ¿Qué material natural ayuda: arena limpia o plasticina azul?", "Arena limpia", "La arena es un material natural y tiene textura de playa."),
    ],
    ex("En tu colegio piden una obra sobre el bosque con materiales reciclados o naturales. ¿Qué eliges: cajas de cartón limpias y hojas secas, o pinturas nuevas compradas?", "Cajas de cartón limpias y hojas secas", "Son materiales de reciclaje y naturales, como pide la consigna."),
    [
        ex("Verdadero o falso: la esteca es una herramienta para modelar.", "Verdadero", "Sirve para marcar detalles en arcilla o plasticina."),
        ex("¿Qué es un material textil?", "Un material hecho de tela, lana o hilo", "Textil se refiere a tejidos y fibras."),
        ex("Verdadero o falso: puedo usar cualquier herramienta sin pedir ayuda a un adulto.", "Falso", "Las herramientas peligrosas las usa un adulto."),
    ],
    task(
        "Elige UNA intención: A) mostrar un cerro rugoso y alto; B) mostrar una nube suave y liviana; C) mostrar un río que se mueve. Elige dos materiales de las listas de la clase y una herramienta segura. Escribe una frase: «Usaré… y… porque…». Haz un boceto de cómo quedaría.",
        "Elegí la intención A. Usaré cartón arrugado y cola fría para el relieve rugoso. Herramienta: tijeras de punta redonda. Usaré cartón arrugado porque es rugoso y hace relieve, como una roca. Mi boceto muestra un cerro de tres picos.",
        ["elige materiales con una propiedad relacionada", "elige herramientas seguras", "escribe la razón", "hace un boceto"],
        ["frase de elección", "boceto", "lista de materiales y herramienta"],
        ["elegir sin razón", "usar herramientas peligrosas"],
        "Destaca la razón que usa una propiedad del material y pregunta qué otro material podría lograr lo mismo.",
    ),
    "Mira tres objetos de tu casa y di si son lisos o rugosos, livianos o pesados.",
    "Compara dos materiales distintos para la misma intención y anota cuál lo logra mejor.",
)

# ---------------------------------------------------------------- Clase 2
lesson(
    OA3, 2,
    "Témpera, un pincel grueso y uno fino (o una brocha pequeña), agua en un recipiente irrompible y papel grueso. Cubre la mesa con papel de diario.",
    "Aprenderé a pintar con témpera y a cambiar variables: cantidad de agua, presión y tipo de pincel. Sirve para ver cómo cada decisión cambia el efecto y elegir la que mejor muestra mi idea.",
    ["Sé que los materiales tienen propiedades.", "Sé usar un pincel con cuidado y limpiarlo."],
    [
        "La pintura es un procedimiento: aplico color con un pincel o una brocha sobre una superficie. Con témpera, que se disuelve en agua, hay varias variables. La primera es la cantidad de agua. Con poca agua, el color es cubriente y fuerte. Con mucha agua, el color es transparente y deja ver el papel. La segunda es la presión del pincel: apretar deja una huella gruesa; rozar, una fina.",
        "La tercera variable es la herramienta. Una brocha ancha sirve para cubrir fondos grandes. Un pincel fino sirve para detalles. Un pincel seco con poca pintura deja una textura áspera, con rayas. También importa el orden: se pinta de fondo a detalle y de claro a oscuro, esperando que cada capa se seque para que los colores no se ensucien. Para limpiar, enjuago el pincel en agua y lo seco; no lo dejo mojado de punta.",
        "Para decidir, hago pruebas pequeñas en una esquina del papel o en una hoja aparte. Pruebo el mismo color con poca y con mucha agua, con presión fuerte y suave. Después comparo con mi intención. Si quiero mostrar bruma, elijo agua en abundancia. Si quiero un cerro sólido, elijo poca agua y una brocha ancha. Dejo escrito qué cambié y qué efecto tuvo.",
    ],
    [("témpera", "pintura que se mezcla con agua y se aplica con pincel"), ("cubriente", "pintura que tapa lo que hay debajo"), ("transparente", "que deja ver lo que hay debajo"), ("capa", "una pasada de pintura sobre una superficie"), ("brocha", "herramienta con cerdas anchas para cubrir áreas grandes")],
    [
        w("Efecto de la cantidad de agua", "Quieres pintar bruma suave sobre un cerro. ¿Usas poca o mucha agua con la témpera?", ["La bruma es transparente.", "Con mucha agua el color es transparente.", "Dejo ver el cerro debajo."], "Mucha agua"),
        w("Elegir la herramienta", "Quieres pintar las ramas finas de un árbol. ¿Usas una brocha ancha o un pincel fino?", ["Las ramas finas son un detalle.", "El pincel fino permite trazos delgados.", "La brocha ancha taparía el detalle."], "Un pincel fino"),
    ],
    [
        m("Pintar encima sin esperar que la capa anterior se seque.", "Los colores se mezclan y se ensucian.", "Espera que seque cada capa."),
        m("Dejar el pincel dentro del agua con las cerdas hacia abajo.", "Se doblan y se estropean.", "Enjuaga, seca y guarda el pincel con las cerdas hacia arriba."),
    ],
    [
        ex("Con mucha agua, ¿la témpera queda cubriente o transparente?", "Transparente", "El agua diluye el color y deja ver el papel."),
        ex("¿Qué pincel sirve para cubrir un fondo grande: una brocha ancha o un pincel fino?", "Una brocha ancha", "Cubre más superficie con cada pasada."),
        ex("Antes de pintar sobre una capa, ¿esperas que esté seca o la pintas de inmediato?", "Esperas que esté seca", "Así los colores no se ensucian."),
    ],
    [
        ex("Un pincel casi seco, con poca pintura, ¿deja una textura áspera con rayas o una superficie lisa y mojada?", "Una textura áspera con rayas", "Con poca pintura se ve el papel entre las rayas."),
        ex("Apretar mucho el pincel, ¿deja una huella gruesa o una fina?", "Gruesa", "La presión abre las cerdas y marca más."),
        ex("¿En qué orden se suele pintar: de detalle a fondo o de fondo a detalle?", "De fondo a detalle", "Primero se cubren las zonas grandes."),
    ],
    [
        ex("Quieres pintar un cerro sólido y fuerte. ¿Usas poca agua con una brocha ancha o mucha agua con un pincel fino?", "Poca agua con una brocha ancha", "El color cubriente y la pasada ancha dan solidez."),
        ex("Quieres pintar la espuma delgada de una ola sobre un mar oscuro. ¿Qué haces: un pincel casi seco con blanco o una pasada con mucha agua y blanco?", "Un pincel casi seco con blanco", "El pincel seco deja rayas finas que parecen espuma."),
        ex("Debes pintar un cielo claro y un cerro oscuro delante de él. ¿Qué pintas primero: el cielo o el cerro?", "El cielo", "Se pinta de fondo a primer plano y el cerro va delante."),
    ],
    [
        ex("Dos pruebas de una bruma: la A con poca agua y la B con mucha agua. Quieres que la bruma deje ver el cerro. ¿Cuál sirve?", "La B", "La mucha agua da transparencia."),
        ex("Una compañera pintó un cielo azul y encima el sol amarillo, sin esperar a que secara. El sol amarillo quedó verdoso. ¿Qué pasó?", "Los colores se mezclaron", "La capa mojada de abajo se mezcló con el amarillo."),
    ],
    [
        ex("Tu intención es mostrar un lago con bruma y un árbol firme al frente. ¿Qué haces con el árbol: poca agua y color fuerte, o mucha agua y color suave?", "Poca agua y color fuerte", "El árbol firme necesita color cubriente."),
        ex("Tienes un pincel grueso y uno fino. Tienes que pintar un fondo grande y luego unas líneas de pasto. ¿En qué orden usas los pinceles?", "Grueso y luego fino", "El fondo grande va primero y el detalle después."),
    ],
    ex("Cuando termines de pintar en clases, tienes que ordenar. ¿Qué haces con el pincel: lo enjuagas y lo secas, o lo dejas con pintura en un vaso con agua?", "Lo enjuagas y lo secas", "Así se cuida y dura más."),
    [
        ex("Verdadero o falso: con poca agua, la témpera es más cubriente.", "Verdadero", "Con poca agua el color es más denso."),
        ex("¿Para qué sirve un pincel fino?", "Para pintar detalles", "Hace trazos delgados."),
        ex("Verdadero o falso: se pinta primero el detalle y luego el fondo.", "Falso", "Se parte por el fondo."),
    ],
    task(
        "Elige UNA intención: A) mostrar bruma sobre un cerro; B) mostrar un cerro sólido; C) mostrar espuma de olas. Haz tres pruebas pequeñas con témpera cambiando UNA variable: cantidad de agua, presión o tipo de pincel. Elige la prueba que mejor muestra tu intención, haz la obra y anota qué variable cambiaste y qué efecto tuvo.",
        "Elegí la A. Probé tres cantidades de agua con el mismo azul. Con mucha agua se vio transparente, como bruma. Elegí esa prueba y pinté el cerro con bruma. Cambié la cantidad de agua; el efecto fue que se ve el cerro a través de la pintura.",
        ["cambia una sola variable", "compara las tres pruebas", "elige la que muestra la intención", "anota la variable y el efecto"],
        ["tres pruebas", "obra", "una frase de variable y efecto"],
        ["cambiar varias variables a la vez", "no esperar el secado"],
        "Reconoce la prueba mejor comparada y pregunta qué otra variable cambiaría el efecto.",
    ),
    "Moja un dedo y toca un papel: observa cómo el agua cambia el papel. Di qué pasaría con una pintura muy diluida.",
    "Haz una escala de cinco cuadros pintando el mismo color con cada vez más agua y ordénalos de más fuerte a más suave.",
)

# ---------------------------------------------------------------- Clase 3
lesson(
    OA3, 3,
    "Arcilla de modelar, plasticina o masa de sal (harina, sal y agua), cartón, cola fría, tijeras de punta redonda, retazos de tela y una esteca o un palito de helado.",
    "Aprenderé a elegir procedimientos de escultura y construcción (modelar, armar con cartón, unir con textiles) según lo que quiero lograr. Sirve para hacer objetos en tres dimensiones que se sostengan y comuniquen mi idea.",
    ["Sé reconocer materiales y herramientas.", "Sé que cada material tiene propiedades distintas."],
    [
        "La escultura es una obra en tres dimensiones: tiene alto, ancho y fondo. Se puede hacer con tres procedimientos. Modelar es dar forma con las manos a un material blando, como arcilla o masa. Armar o construir es unir piezas, por ejemplo cartones, con pegamento. Ensamblar textiles es unir telas o lanas, pegándolas o anudándolas.",
        "Con arcilla hay formas de trabajar. Se pueden hacer bolitas, rollos largos y planchas. Para unir dos piezas, se rayan las dos superficies y se humedece un poco antes de pegarlas; así no se despegan al secar. La esteca sirve para marcar detalles. Un trabajo en arcilla necesita secarse en un lugar tranquilo. Con cartón, se pueden cortar y doblar las piezas; los dobleces y los tubos hacen que se sostenga. Para unir cartón uso cola fría y espero que seque. El cartón se corta con tijeras de punta redonda, y madera o placas gruesas las corta un adulto con herramientas adecuadas.",
        "Elijo el procedimiento según mi intención. Si quiero una figura estable y pesada, modelo con arcilla o masa. Si quiero una estructura liviana y grande, construyo con cartón. Si quiero suavidad y color, uso textiles. También pienso en la base: una escultura necesita una base que la haga estable. Al final reviso si se sostiene y si el procedimiento ayudó a mi idea.",
    ],
    [("escultura", "obra en tres dimensiones, con alto, ancho y fondo"), ("modelar", "dar forma con las manos a un material blando"), ("construir", "unir piezas para armar una forma"), ("base", "parte que sostiene la escultura para que no se caiga"), ("ensamblar", "unir piezas o telas entre sí")],
    [
        w("Unir arcilla", "Quieres pegar una oreja de arcilla a un animal. ¿Cómo evitas que se despegue al secar?", ["Rayo las dos superficies.", "Humedezco un poco con agua.", "Las presiono juntas y alizo el borde."], "Rayar las dos superficies, humedecer y presionar"),
        w("Elegir el procedimiento", "Quieres construir una torre grande y liviana para una maqueta. ¿Modelas con arcilla o construyes con cartón?", ["La torre debe ser grande y liviana.", "El cartón es liviano y se arma con piezas.", "La arcilla sería muy pesada."], "Construir con cartón"),
    ],
    [
        m("Pegar dos piezas de arcilla secas con agua y esperar que queden firmes.", "Las piezas secas no se unen bien.", "Une las piezas cuando la arcilla aún está blanda, rayando y humedeciendo."),
        m("Hacer una escultura alta sin base.", "Se cae porque no tiene dónde apoyarse.", "Agrega una base ancha que la sostenga."),
    ],
    [
        ex("Una escultura, ¿es una obra en tres dimensiones o en dos dimensiones?", "En tres dimensiones", "Tiene alto, ancho y fondo."),
        ex("Dar forma con las manos a un material blando, como la arcilla, ¿se llama modelar o construir?", "Modelar", "Modelar es moldear con las manos."),
        ex("Para unir dos piezas de arcilla blanda, ¿rayas y humedeces las superficies o las pegas sin hacer nada?", "Rayas y humedeces las superficies", "Así quedan bien unidas."),
    ],
    [
        ex("Unir piezas de cartón con cola fría para armar una forma, ¿es modelar o construir?", "Construir", "Se unen piezas para armar una forma."),
        ex("Un tubo de cartón y un doblez, ¿hacen que la pieza se sostenga mejor o peor?", "Mejor", "Los dobleces y tubos le dan rigidez."),
        ex("La arcilla se hace con bolitas, rollos y planchas. ¿Un rollo largo es una forma delgada y alargada o una plancha plana?", "Una forma delgada y alargada", "Un rollo es largo y delgado."),
    ],
    [
        ex("Quieres una figura estable, pesada y firme. ¿Eliges arcilla o papel de seda?", "Arcilla", "La arcilla es pesada y se endurece."),
        ex("Quieres hacer un muñeco blando con un abrigo de lana. ¿Qué procedimiento usas: ensamblar textiles o modelar arcilla?", "Ensamblar textiles", "La lana y las telas se unen para dar suavidad."),
        ex("Tu escultura de cartón es alta y delgada, y se cae. ¿Qué agregas: una base ancha o más altura?", "Una base ancha", "La base da estabilidad."),
    ],
    [
        ex("Tu intención es mostrar un animal fuerte y pesado. Prueba A: figura en arcilla con patas gruesas. Prueba B: figura de papel de seda con patas finas. ¿Cuál cumple mejor?", "La prueba A", "La arcilla y las patas gruesas dan sensación de peso y fuerza."),
        ex("Un compañero quiere cortar una tabla gruesa de madera para su escultura con una sierra de calar. ¿Qué debe hacer?", "Pedir que un adulto la corte", "La sierra de calar la usa un adulto con formación."),
    ],
    [
        ex("Acabas de pegar dos cartones con cola fría. ¿Qué haces: los presionas y esperas que sequen o los mueves enseguida?", "Los presionas y esperas que sequen", "El pegamento necesita tiempo para agarrar."),
        ex("Necesitas una base para una escultura de cartón. ¿Qué es mejor: una base ancha y plana o una base redonda y pequeña como una canica?", "Una base ancha y plana", "La base ancha apoya mejor y evita que se vuelque."),
    ],
    ex("En el colegio hay una exposición de esculturas livianas para colgar del techo con hilo. ¿Qué material eliges: cartón y papel o arcilla maciza?", "Cartón y papel", "Son livianos y pueden colgarse."),
    [
        ex("Verdadero o falso: para unir arcilla se rayan y humedecen las superficies.", "Verdadero", "Eso ayuda a que no se despeguen."),
        ex("¿Para qué sirve la base de una escultura?", "Para que se sostenga", "Evita que se caiga."),
        ex("Verdadero o falso: un estudiante puede cortar madera gruesa con sierra de calar sin ayuda.", "Falso", "Debe hacerlo un adulto con formación."),
    ],
    task(
        "Elige UN encargo: A) un animal fuerte de arcilla o masa; B) una torre liviana de cartón; C) un muñeco de tela y lana. Escribe el procedimiento que usarás (modelar, construir o ensamblar), los pasos y qué harás para que se sostenga. Haz el trabajo. Anota si se sostuvo y por qué.",
        "Elegí la A. Modelaré con masa de sal: un cuerpo con bolitas y rollos para las patas. Rayaré y humedeceré donde pegue las patas. Haré una base ancha. Se sostuvo porque las patas son gruesas y tiene base. El procedimiento ayudó a mostrar fuerza.",
        ["elige el procedimiento según la intención", "escribe pasos claros", "considera la base o la estabilidad", "explica si funcionó"],
        ["pasos escritos", "escultura", "una frase de revisión"],
        ["no pensar en la base", "usar herramientas peligrosas"],
        "Destaca el procedimiento mejor explicado y pregunta qué cambiaría si el trabajo fuera más grande.",
    ),
    "Mira un objeto de tu casa y di si está hecho modelando, construyendo o ensamblando.",
    "Haz la misma figura con dos materiales distintos y anota cuál se sostiene mejor.",
)

# ---------------------------------------------------------------- Clase 4
lesson(
    OA3, 4,
    "Un celular o una cámara de un adulto (con permiso), o un visor de cartón: un cartón con una ventana rectangular cortada. Para el video, lápiz y hojas para un guion de imágenes. No fotografíes a personas sin su permiso.",
    "Aprenderé a crear con fotografía y video, eligiendo el encuadre, el plano y el ángulo según mi intención. Sirve para contar una idea con imágenes y para usar la cámara con cuidado y respeto.",
    ["Sé que un material y una herramienta cambian el efecto.", "Sé que la luz cambia lo que se ve."],
    [
        "La fotografía es un procedimiento que guarda una imagen con una cámara. El video guarda una secuencia de imágenes en movimiento. Para decidir cómo fotografiar, uso tres decisiones. El encuadre es lo que entra y lo que queda afuera de la imagen. El plano es qué tan cerca o lejos estoy: el plano general muestra todo el lugar, el plano medio muestra una parte, y el primer plano muestra un detalle muy cerca.",
        "La tercera decisión es el ángulo, que es desde dónde miro. Si miro desde arriba hacia abajo, es un ángulo picado y el objeto se ve más pequeño. Si miro desde abajo hacia arriba, es un ángulo contrapicado y el objeto se ve más grande e importante. Si miro a la altura de los ojos, es un ángulo normal. La luz también cuenta: una foto a contraluz, con la luz detrás del objeto, muestra una silueta oscura. Con el visor de cartón puedo practicar el encuadre sin cámara.",
        "En el video organizo una secuencia: primero un plano general, luego uno medio y al final un primer plano. Un guion de imágenes, llamado storyboard, dibuja cada plano antes de grabar. Si grabo personas, pido permiso y no publico sus imágenes sin autorización de ellas y de sus familias. Si no hay cámara, la clase se puede hacer con el visor y dibujos. Muestro mi trabajo en una pantalla o con un proyector, sin mirar directamente a su luz.",
    ],
    [("encuadre", "lo que entra y lo que queda fuera de una imagen"), ("plano", "qué tan cerca o lejos está lo que se muestra"), ("ángulo", "desde dónde se mira lo que se fotografía"), ("storyboard", "dibujos que muestran los planos de un video antes de grabar"), ("silueta", "forma oscura de un objeto que se ve a contraluz")],
    [
        w("Elegir el plano", "Quieres mostrar la textura de la corteza de un árbol. ¿Usas plano general o primer plano?", ["Quiero un detalle de la textura.", "El primer plano muestra un detalle muy cerca.", "El plano general mostraría todo el árbol."], "Primer plano"),
        w("Elegir el ángulo", "Quieres que un edificio se vea grande e importante. ¿Usas ángulo picado o contrapicado?", ["Contrapicado es mirar desde abajo hacia arriba.", "Eso hace que el objeto se vea más grande.", "Lo elijo para mi intención."], "Contrapicado"),
    ],
    [
        m("Fotografiar a una persona sin pedirle permiso.", "Se invade su privacidad.", "Pide permiso antes y no la publiques sin autorización."),
        m("Grabar un video sin pensar en la secuencia de planos.", "Las imágenes no cuentan una idea.", "Dibuja un storyboard antes de grabar."),
    ],
    [
        ex("¿Qué plano muestra un detalle muy cerca: el plano general o el primer plano?", "El primer plano", "Muestra un detalle de cerca."),
        ex("Mirar desde arriba hacia abajo, ¿es un ángulo picado o contrapicado?", "Picado", "El ángulo picado mira desde arriba."),
        ex("¿Qué es el encuadre: lo que entra y queda fuera de la imagen o el color de la imagen?", "Lo que entra y queda fuera de la imagen", "El encuadre es el recorte de lo que se ve."),
    ],
    [
        ex("Un ángulo contrapicado, ¿hace que un objeto se vea más grande o más pequeño?", "Más grande", "Mirar desde abajo hacia arriba da importancia."),
        ex("Un plano general, ¿muestra todo el lugar o solo un detalle?", "Todo el lugar", "Es el plano más abierto."),
        ex("¿Para qué sirve un storyboard: para dibujar los planos antes de grabar o para pintar una pared?", "Para dibujar los planos antes de grabar", "Sirve para planificar el video."),
    ],
    [
        ex("Quieres mostrar un cerro enorme y majestuoso. ¿Qué ángulo eliges: contrapicado o picado?", "Contrapicado", "Mirar desde abajo hace que el cerro se vea grande."),
        ex("Quieres un video con la secuencia: plano general, plano medio y primer plano. ¿Con qué comienzas: el primer plano o el plano general?", "El plano general", "Primero se muestra todo el lugar y luego se acerca."),
        ex("Quieres una foto de una silueta oscura de un árbol con el atardecer detrás. ¿Dónde está la luz: detrás del árbol o delante?", "Detrás del árbol", "La silueta oscura se produce con la luz detrás."),
    ],
    [
        ex("Quieres sacar una foto a una persona de tu casa para tu obra. ¿Qué haces primero: pedirle permiso o sacar la foto sin que se dé cuenta?", "Pedirle permiso", "Hay que respetar la privacidad de las personas."),
        ex("Dos fotos del mismo perro. En la A, la cámara está arriba y se ve pequeño. En la B, la cámara está abajo y se ve grande. Quieres mostrar a un perro valiente e importante. ¿Cuál eliges?", "La B", "El ángulo contrapicado lo hace ver más grande."),
    ],
    [
        ex("Quieres mostrar que un niño está solo en una plaza enorme. ¿Qué plano sirve más: el general o el primer plano?", "El general", "El plano general muestra todo el espacio vacío alrededor del niño."),
        ex("No tienes cámara. ¿Qué puedes usar para practicar el encuadre: un visor de cartón con una ventana o un lápiz de mina?", "Un visor de cartón con una ventana", "La ventana recorta la escena."),
    ],
    ex("En el colegio piden presentar un video de 3 planos sobre el patio. Tienes la cámara de un adulto. Ves a un compañero que pasa por el patio. ¿Qué haces: le pides permiso o lo grabas rápido?", "Le pides permiso", "Se debe respetar su imagen."),
    [
        ex("Verdadero o falso: el primer plano muestra un detalle muy cerca.", "Verdadero", "Es el plano más cercano."),
        ex("¿Qué ángulo hace que algo se vea más pequeño?", "El picado", "Se mira desde arriba."),
        ex("Verdadero o falso: se puede publicar el video de una persona sin pedirle permiso.", "Falso", "Hay que tener su autorización."),
    ],
    task(
        "Elige UNA idea: A) un día de lluvia en el patio; B) una hoja que cae de un árbol; C) un objeto de tu pieza que cambia de lugar. Dibuja un storyboard de tres planos (general, medio y primer plano), con el ángulo de cada uno. Si tienes cámara y permiso, graba o fotografía; si no, usa el visor de cartón. Escribe qué quieres comunicar.",
        "Elegí la B. Plano 1, general: el árbol y el patio, ángulo picado. Plano 2, medio: la hoja cayendo, ángulo normal. Plano 3, primer plano: la hoja sobre el suelo, ángulo picado. Quiero comunicar la calma del otoño.",
        ["dibuja tres planos distintos", "indica el ángulo de cada uno", "escribe lo que quiere comunicar", "respeta la privacidad"],
        ["storyboard", "fotos o video si hay cámara", "una frase de intención"],
        ["repetir el mismo plano tres veces", "grabar personas sin permiso"],
        "Destaca el plano con mayor intención y pregunta qué cambiaría si cambiara el ángulo.",
    ),
    "Haz un marco con tus dedos y encuadra algo de tu pieza. Di qué dejas fuera del marco.",
    "Haz el mismo storyboard cambiando el ángulo de los tres planos y anota cómo cambia el mensaje.",
)

# ---------------------------------------------------------------- Clase 5
lesson(
    OA3, 5,
    "Un computador, tableta o celular con un programa de dibujo o diseño, con ayuda de un adulto. Si no tienes, usa una hoja cuadriculada y lápices: el trabajo se hace igual como boceto.",
    "Aprenderé a usar imágenes digitales y diseño gráfico: capas, tipografía, tamaño de imagen y contraste. Sirve para hacer un afiche digital que se lea bien y comunique mi idea.",
    ["Sé que el diseño tiene función, usuario y forma.", "Sé que el contraste hace que algo se lea mejor."],
    [
        "Una imagen digital está formada por muchos puntos pequeños llamados píxeles. Si agrando mucho una imagen pequeña, los píxeles se notan y se ve borrosa o con cuadritos. Por eso conviene empezar con una imagen del tamaño adecuado. En el diseño gráfico digital se combinan imágenes y textos en un archivo. Un programa de diseño suele tener capas, que son como láminas transparentes apiladas: puedo mover un texto sin dañar la imagen de abajo.",
        "La tipografía es el tipo de letra. Para un afiche conviene una letra clara y grande en el título, y letras más pequeñas para los detalles. No conviene usar muchos tipos de letra distintos. El contraste entre el color de la letra y el fondo debe ser fuerte: letras oscuras sobre fondo claro, o al revés. Guardo siempre una copia del trabajo antes de cambiarlo mucho, para poder volver atrás.",
        "Al crear con imágenes digitales, cuido los derechos de autor. Una imagen que sacó otra persona es de su autor, y no puedo usarla sin permiso o sin la licencia que lo permita. Lo más seguro es usar mis propias fotos o dibujos. Nunca pongo datos personales en un afiche. Si no tengo computador, hago el diseño en una hoja cuadriculada: cada cuadrito representa un espacio para una imagen o un texto.",
    ],
    [("píxel", "punto pequeño de color que forma una imagen digital"), ("capa", "lámina transparente en un programa de diseño donde se coloca una imagen o un texto"), ("tipografía", "tipo de letra"), ("derechos de autor", "derechos de quien creó una obra, que decide cómo se puede usar"), ("diseño gráfico", "combinación de imágenes y textos para comunicar un mensaje")],
    [
        w("Imagen borrosa", "Tienes una foto pequeña y la agrandas para ocupar todo el afiche. Se ve con cuadritos. ¿Por qué ocurre?", ["La imagen está formada por píxeles.", "Al agrandarla mucho, los píxeles se ven.", "Necesito una imagen más grande desde el inicio."], "Por los píxeles que se hacen visibles al agrandar"),
        w("Elegir el color de la letra", "El fondo del afiche es azul oscuro. ¿Qué color de letra se lee mejor: amarillo claro o azul medio?", ["Busco contraste fuerte con el fondo.", "El amarillo claro contrasta con el azul oscuro.", "El azul medio se parece al fondo."], "Amarillo claro"),
    ],
    [
        m("Usar la foto de otra persona porque está en internet.", "Esa foto tiene un autor con derechos.", "Usa tus propias fotos o dibujos, o pide permiso."),
        m("Usar cinco tipos de letra distintos en un afiche.", "El afiche se ve desordenado y cuesta leerlo.", "Usa una o dos tipografías claras."),
    ],
    [
        ex("¿Cómo se llaman los puntos pequeños que forman una imagen digital?", "Píxeles", "Una imagen digital está formada por píxeles."),
        ex("Una letra clara y grande en un título, ¿ayuda a leer o dificulta la lectura?", "Ayuda a leer", "El título debe verse rápido."),
        ex("Las capas en un programa de diseño, ¿son como láminas transparentes apiladas o como una sola hoja pegada?", "Como láminas transparentes apiladas", "Permiten mover un elemento sin dañar los otros."),
    ],
    [
        ex("Si agrandas mucho una imagen pequeña, ¿se ve más nítida o con cuadritos?", "Con cuadritos", "Se notan los píxeles."),
        ex("¿Qué es la tipografía: el tipo de letra o el tamaño del archivo?", "El tipo de letra", "Tipografía es la forma de las letras."),
        ex("Una foto sacada por otra persona, ¿pertenece a su autor o es de quien la encuentra primero?", "A su autor", "Los derechos de autor protegen a quien creó la obra."),
    ],
    [
        ex("El fondo de tu afiche es blanco. ¿Qué color de letra elegirías: negro o amarillo muy claro?", "Negro", "El negro contrasta con el blanco."),
        ex("Quieres mover un título en un afiche digital sin cambiar la foto. ¿Qué te ayuda: una capa separada para el título o pegar todo en una sola?", "Una capa separada para el título", "Las capas permiten mover un elemento sin dañar los otros."),
        ex("Vas a hacer un afiche con tus datos personales: teléfono y dirección. ¿Lo haces o evitas poner esos datos?", "Evitas poner esos datos", "Los datos personales no deben ponerse en un afiche público."),
    ],
    [
        ex("Dos afiches del mismo festival. El A usa tres tipografías distintas, muy pequeñas. El B usa una sola, con título grande. ¿Cuál se lee mejor?", "El B", "Una tipografía clara con título grande es más legible."),
        ex("Un compañero usó una foto sacada de un sitio web sin permiso y puso su nombre como autor. ¿Está bien?", "No", "Debe pedir permiso, usar sus propias fotos o indicar la fuente permitida."),
    ],
    [
        ex("Tu afiche tiene letras blancas sobre un fondo amarillo claro y casi no se leen. ¿Qué cambias: el fondo a un color oscuro o el título a un tamaño más pequeño?", "El fondo a un color oscuro", "El blanco contrasta con un fondo oscuro, no con uno claro."),
        ex("No tienes computador. ¿Cómo puedes diseñar el afiche: en una hoja cuadriculada con un espacio para cada texto e imagen o esperando a tener uno?", "En una hoja cuadriculada con un espacio para cada texto e imagen", "El boceto en papel sirve igual para planificar."),
    ],
    ex("Debes hacer un afiche digital para la feria del colegio. Tienes tu propio dibujo de una manzana, de tamaño pequeño. Quieres usarlo como imagen principal. ¿Qué es mejor: usarlo en tamaño moderado o agrandarlo hasta ocupar toda la hoja?", "Usarlo en tamaño moderado", "Agrandarlo mucho haría que se vea con cuadritos."),
    [
        ex("Verdadero o falso: una imagen pequeña agrandada mucho se ve borrosa.", "Verdadero", "Los píxeles se hacen visibles."),
        ex("¿Qué es un píxel?", "Un punto pequeño de color de una imagen digital", "Muchos píxeles forman la imagen."),
        ex("Verdadero o falso: es seguro usar cualquier imagen de internet en mi afiche.", "Falso", "Las imágenes tienen derechos de autor."),
    ],
    task(
        "Elige UN encargo: A) un afiche para una feria de libros del colegio; B) un afiche para cuidar el agua; C) una invitación a una exposición de arte. Escribe el texto: un título, una fecha inventada (por ejemplo, viernes 12) y un lugar (el colegio). Diseña el afiche en el computador o en una hoja cuadriculada. Indica la tipografía, el color de la letra y del fondo, y la imagen (tuya, no de internet).",
        "Elegí la B. Título: «Cuidemos el agua», grande y en amarillo sobre fondo azul oscuro. Fecha: viernes 12. Lugar: el colegio. Una sola tipografía clara. Imagen: un dibujo mío de una gota. Elegí amarillo y azul oscuro por el contraste.",
        ["incluye título, fecha y lugar", "usa una o dos tipografías claras", "hay buen contraste", "usa imágenes propias"],
        ["afiche digital o boceto en hoja cuadriculada", "texto escrito", "lista de decisiones"],
        ["usar imágenes de otros", "poco contraste", "demasiadas tipografías"],
        "Destaca el afiche que se lee mejor y pregunta qué decisión de contraste ayudó.",
    ),
    "Mira un afiche de tu barrio o de internet y di en voz alta qué tipografía y qué colores usa.",
    "Haz el mismo afiche con otra tipografía y otros colores y anota cuál se lee mejor.",
)

# ---------------------------------------------------------------- Clase 6
lesson(
    OA3, 6,
    "Tu trabajo de la clase anterior o uno en proceso, una hoja para anotar, y tu mesa de trabajo con los materiales usados.",
    "Aprenderé a revisar mis trabajos para mejorar la técnica sin perder mi idea: orden, cuidado de herramientas, seguridad y respeto a los derechos de autor. Sirve para que mi obra se vea bien hecha y se pueda explicar cómo la hice.",
    ["Sé elegir materiales, herramientas y procedimientos según mi intención.", "Sé que las imágenes de otros tienen derechos de autor."],
    [
        "Dominar un material es saber usarlo para lograr lo que quiero. No significa hacerlo perfecto, sino hacerlo con control, cuidado y razón. Al revisar mi trabajo, miro la técnica: ¿hay exceso de pegamento?, ¿la pintura chorrea?, ¿los cortes quedaron parejos?, ¿la escultura se sostiene? Cada problema técnico tiene una causa, y puedo buscarla y mejorarla.",
        "Para mejorar sin perder mi idea, reviso mi intención primero. Luego busco qué técnica fallé y la corrijo. Si el pegamento se ve, uso menos cantidad. Si la pintura chorrea, uso menos agua. Si un corte quedó chueco, trazo una línea guía con regla. Mi idea no cambia, solo hago mejor su ejecución. También cuido mis herramientas: lavo los pinceles, guardo las tijeras cerradas y con las puntas cubiertas o hacia abajo, y dejo el lugar ordenado.",
        "La seguridad es parte de la técnica: no pruebo herramientas peligrosas sin ayuda, no pongo materiales pequeños en la boca y me lavo las manos al terminar. En el trabajo digital, guardo una copia, cito la fuente de una imagen si uso una ajena con permiso y no publico imágenes de otras personas sin autorización. Al final, escribo en mi hoja de proceso qué técnica mejoré y qué efecto tuvo en mi obra.",
    ],
    [("dominio", "saber usar un material o una herramienta con control y razón"), ("técnica", "forma de usar un material o una herramienta para lograr un efecto"), ("hoja de proceso", "hoja donde anoto qué hice, qué cambié y por qué"), ("ejecución", "cómo se realiza una idea en el trabajo"), ("fuente", "persona o lugar de donde viene una imagen o información")],
    [
        w("Mejorar la técnica", "Tu cartel tiene mucho pegamento visible y se arrugó el papel. ¿Qué mejoras?", ["Reviso la causa: demasiado pegamento.", "Uso menos pegamento y lo reparto parejo.", "Espero que seque antes de seguir."], "Menos pegamento, repartido parejo, y esperar el secado"),
        w("Cuidar la idea", "Al mejorar un corte chueco, ¿cambias la idea de la obra o solo la ejecución?", ["La intención sigue igual.", "Solo corrijo cómo se hizo el corte.", "Uso una línea guía con regla."], "Solo la ejecución"),
    ],
    [
        m("Pensar que dominar una técnica es no cometer nunca errores.", "Los errores son parte de aprender y se pueden corregir.", "Revisa la causa del error y mejora la técnica."),
        m("Dejar las tijeras abiertas y con las puntas hacia arriba sobre la mesa.", "Puede lastimar a otra persona.", "Guarda las tijeras cerradas y con las puntas cubiertas o hacia abajo."),
    ],
    [
        ex("Si la pintura chorrea, ¿usas más agua o menos agua?", "Menos agua", "Mucha agua hace que la pintura corra."),
        ex("Para trazar un corte derecho, ¿usas una línea guía con regla o cortas a ojo?", "Una línea guía con regla", "La regla ayuda a cortar derecho."),
        ex("Al terminar de trabajar, ¿lavas los pinceles o los dejas con pintura?", "Los lavas", "Así se cuidan para usarlos otra vez."),
    ],
    [
        ex("Corregir un corte chueco, ¿cambia la intención de la obra o solo la ejecución?", "Solo la ejecución", "La idea se mantiene."),
        ex("¿Qué se anota en la hoja de proceso: qué técnica mejoré y qué efecto tuvo o el nombre de mi curso?", "Qué técnica mejoré y qué efecto tuvo", "La hoja de proceso explica cómo se hizo la obra."),
        ex("Si usas una imagen ajena con permiso, ¿citas la fuente o dices que la hiciste tú?", "Citas la fuente", "Es honesto y respeta al autor."),
    ],
    [
        ex("Tu escultura de cartón se cae porque no tiene base. ¿Qué técnica mejoras: agregar una base ancha o cambiar el tema de la obra?", "Agregar una base ancha", "El problema es de ejecución y no de la idea."),
        ex("Pegaste papel con mucho pegamento y quedó arrugado. La próxima vez, ¿qué haces: usar una capa fina de pegamento o más cantidad?", "Una capa fina de pegamento", "Mucho pegamento moja y arruga el papel."),
        ex("Vas a terminar tu trabajo digital. ¿Qué haces antes de hacer cambios grandes: guardar una copia o borrar el original?", "Guardar una copia", "Así puedes volver atrás si algo sale mal."),
    ],
    [
        ex("Dos compañeros mejoraron el mismo cartel con letras mal cortadas. Ana corta de nuevo con regla y mantiene su diseño. Luis cambia el diseño completo. ¿Quién mejoró solo la ejecución?", "Ana", "Ella cambió cómo corta, no su idea."),
        ex("Un compañero dice: «Mi técnica es perfecta porque nunca me equivoco». ¿Es una buena forma de dominar un material?", "No", "Se mejora la técnica reconociendo errores y corrigiéndolos."),
    ],
    [
        ex("Tu témpera se llenó de grumos secos porque dejaste el pote abierto. La próxima vez, ¿lo tapas al terminar o lo dejas abierto?", "Lo tapas al terminar", "Tapado, el pote no se seca."),
        ex("Un material pequeño se cayó al suelo en la clase. ¿Qué haces: lo recoges de inmediato para evitar accidentes o lo dejas?", "Lo recoges de inmediato", "Los objetos en el suelo pueden provocar caídas."),
    ],
    ex("Te piden presentar tu trabajo y explicar cómo lo mejoraste. ¿Qué respuesta es mejor: «Usé menos agua para que la pintura no chorreara» o «lo hice mejor»?", "Usé menos agua para que la pintura no chorreara", "Dice la técnica y el efecto."),
    [
        ex("Verdadero o falso: al mejorar la técnica puedo conservar mi idea.", "Verdadero", "Se mejora la ejecución, no la intención."),
        ex("¿Cómo guardas las tijeras con seguridad?", "Cerradas y con las puntas cubiertas", "Así no lastiman a nadie."),
        ex("Verdadero o falso: se puede publicar una foto de otra persona sin su permiso.", "Falso", "Se necesita su autorización."),
    ],
    task(
        "Elige UN trabajo para revisar: A) uno de tus trabajos de las clases anteriores; B) este caso: «un afiche de cartón con letras recortadas chuecas, mucho pegamento visible y una imagen sacada de internet sin autor». Haz una lista de problemas técnicos, escribe cómo los corrigiría (sin cambiar la idea) y qué cuidados de seguridad y derechos aplicarías. Mejora el trabajo y completa una hoja de proceso.",
        "Elegí el caso B. Problemas: letras chuecas, mucho pegamento, imagen sin permiso. Mejoras: cortar con regla, usar una capa fina de pegamento, reemplazar la imagen por un dibujo propio. Mi idea del afiche no cambió. En mi hoja de proceso anoté: usé menos pegamento y quedó plano.",
        ["identifica problemas técnicos", "propone mejoras sin cambiar la idea", "considera seguridad y derechos", "completa la hoja de proceso"],
        ["lista de problemas", "trabajo mejorado", "hoja de proceso"],
        ["cambiar la idea completa", "usar una imagen ajena sin permiso"],
        "Destaca la mejora técnica más clara y pregunta qué efecto tuvo en la obra.",
    ),
    "Mira tu mesa de trabajo y di tres cosas que ordenarías al terminar.",
    "Compara dos trabajos tuyos y anota qué técnica mejoró entre uno y otro.",
)
