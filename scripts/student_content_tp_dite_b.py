"""Dibujo Técnico TP 3.º y 4.º medio: OAE-03 (planos de arquitectura y expediente municipal, como concepto) y OAE-04 (lectura de planos de redes interiores). Papel; sin software; datos de ejemplo."""
from __future__ import annotations

from tp_dite_common import build

O3 = "TP-DITE-3y4-OAE-03"
O4 = "TP-DITE-3y4-OAE-04"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). «Casa Pehuén»: vivienda de dos pisos en un terreno de 200 m². Para pedir el permiso de edificación se arma un expediente de obras, "
     "que se presenta a la Dirección de Obras Municipales (DOM) de la comuna. Contenido de ejemplo: planta del primer piso, planta del segundo piso, fachadas, secciones, cuadro de superficies "
     "y la firma de la arquitecta responsable. Superficie construida: primer piso 80 m²; segundo piso 60 m². Los dibujos se guardan en archivos digitales organizados en capas.")
build(
    O3, 1, F,
    use="Aprenderé qué es un expediente de obras, qué papel cumplen la reglamentación y la firma profesional, y cómo se cuidan los archivos digitales de un proyecto.",
    prior=["Sé calcular superficies de rectángulos.", "Sé calcular porcentajes sencillos.", "Sé qué son planta, fachada y corte."],
    explain=[
        "Un proyecto de arquitectura de una vivienda se representa con plantas, fachadas y secciones. El urbanismo se ocupa de cómo se organizan calles, terrenos y espacios de una ciudad, y también tiene planos. Para construir, el proyecto se presenta a la Dirección de Obras Municipales (DOM) en un expediente de obras: el conjunto de planos y documentos que la municipalidad revisa antes de dar el permiso. La reglamentación vigente y el instrumento de planificación de la comuna fijan qué se puede construir en cada terreno.",
        "Dos medidas de uso común son la ocupación del suelo, que es la superficie construida en el primer piso dividida por la superficie del terreno, y la constructibilidad, que es la superficie construida total dividida por la del terreno. Aquí se expresan como porcentaje. Los límites los fija la norma vigente de cada lugar; en este cuaderno los valores límite son siempre «de ejemplo». La arquitecta responsable firma el proyecto y responde de su cumplimiento; el dibujante no decide si cumple.",
        "En el dibujo digital los elementos se organizan en capas, como hojas transparentes superpuestas: muros, puertas, cotas, textos. Cada capa se puede mostrar u ocultar por separado. Los archivos se guardan con nombre y revisión claros y con copias de seguridad en lugares distintos. Los símbolos o bloques descargados pueden tener licencia: se usa solo lo permitido. Dibujar frente a pantalla exige ergonomía y pausas breves.",
    ],
    vocab=[("expediente de obras", "conjunto de planos y documentos presentado a la municipalidad"), ("DOM", "Dirección de Obras Municipales, que revisa los proyectos de la comuna"), ("capa", "grupo de elementos de un dibujo digital que se muestra u oculta por separado"), ("ocupación del suelo", "superficie construida en el primer piso dividida por la del terreno"), ("constructibilidad", "superficie construida total dividida por la del terreno"), ("urbanismo", "organización de calles, terrenos y espacios de una ciudad"), ("licencia", "permiso que fija cómo se puede usar una obra ajena")],
    worked=[
        ("Calcular la ocupación del suelo", "Un terreno de ejemplo mide 300 m² y el primer piso construido mide 90 m². ¿Qué porcentaje de ocupación del suelo tiene?", ["Se divide la superficie del primer piso por la del terreno: 90 ÷ 300.", "El resultado es 0,3, que expresado como porcentaje es 30 %."], "30 %"),
        ("Elegir qué capa ocultar", "Para imprimir un dibujo de ejemplo solo con muros y puertas, sin cotas ni textos, ¿qué se hace con las capas?", ["Las capas se muestran u ocultan por separado.", "Se ocultan las capas de cotas y de textos y se dejan visibles las de muros y puertas."], "Ocultar las capas de cotas y de textos"),
    ],
    mistakes=[("Creer que el dibujante decide si el proyecto cumple la reglamentación.", "El cumplimiento lo responde el profesional que firma; el dibujante representa lo proyectado.", "Si ves un dato que parece superar un límite, avísale a la arquitecta."),
              ("Guardar el único archivo del proyecto en un solo pendrive.", "Si se daña o se pierde, se pierde el trabajo y las versiones.", "Guarda copias de seguridad en lugares distintos y con la revisión en el nombre.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un expediente de obras?", "El conjunto de planos y documentos que se presenta a la municipalidad para obtener un permiso", "Un archivo con las fotos de la obra terminada", "Una lista de precios de materiales", "El expediente reúne planos y documentos para que la municipalidad revise el proyecto."),
        ("abc", "En un dibujo digital, ¿qué es una capa?", "Un grupo de elementos que se puede mostrar u ocultar por separado", "Una copia de seguridad del archivo", "El material de un muro", "Las capas ordenan el dibujo, por ejemplo muros en una y cotas en otra."),
        ("abc", "¿Quién responde por que el proyecto cumpla la reglamentación?", "El profesional responsable que firma el proyecto", "El dibujante, porque dibujó los planos", "El programa con que se dibujó", "La firma de un profesional responsabiliza; el dibujante representa lo que se proyectó."),
        ("=", "{F} ¿Cuántos m² suman el primer y el segundo piso de la Casa Pehuén?", "80+60", "La superficie total construida es la suma de los dos pisos.", " m²"),
        ("=", "{F} ¿Qué porcentaje de ocupación del suelo tiene la Casa Pehuén?", "80*100//200", "Se divide la superficie del primer piso por la del terreno y se pasa a porcentaje.", " %"),
        ("abc", "{F} ¿A quién se presenta el expediente de obras de la Casa Pehuén?", "A la Dirección de Obras Municipales de la comuna", "A la empresa que venderá los materiales", "Al vecino colindante, que debe aprobarlo", "La revisión de los expedientes la hace la DOM; los otros actores no otorgan el permiso."),
        ("=", "{F} Si el límite de ocupación de ejemplo fuera 50 %, ¿cuántos puntos porcentuales de margen quedan?", "50-80*100//200", "Se resta al límite el porcentaje de ocupación calculado.", " puntos"),
        ("abc", "{F} Un compañero guarda el proyecto en un solo pendrive. ¿Cuál es el riesgo?", "Perder el trabajo si se daña o se extravía; conviene tener copias en lugares distintos", "Ninguno, porque los archivos digitales no se pierden", "Que el pendrive sea demasiado liviano", "Un solo respaldo no protege contra daño o pérdida."),
        ("ab", "Una dibujante descarga de internet un símbolo cuya licencia prohíbe el uso comercial y lo pone en un plano de un cliente. ¿Qué corresponde?", "Revisar la licencia y usar solo lo permitido o pedir autorización", "Usarlo igual, porque está en internet", "Estar en internet no significa que el uso sea libre; la licencia dice qué se permite."),
        ("abc", "{F} El cuadro de superficies del expediente dice 130 m² en total, pero los pisos suman otra cifra. ¿Qué haces?", "Aviso a la arquitecta de la diferencia, porque 80 + 60 son 140 m²", "Cambio el cuadro a 140 sin avisar", "Dejo 130 porque el cuadro tiene firma", "Una diferencia entre cuadro y pisos es un error que revisa y corrige la arquitecta."),
        ("abc", "{F} Si el segundo piso se amplía a 80 m², ¿qué pasa con la superficie total?", "Sube a 160 m² y se debe recalcular la constructibilidad", "Sigue en 140 m²", "Baja a 120 m²", "La suma 80 + 80 es 160; el cambio obliga a recalcular los porcentajes."),
        ("=", "{F} Con la ampliación del segundo piso a 80 m², ¿qué porcentaje de constructibilidad tendría la casa?", "(80+80)*100//200", "Se divide la superficie total construida por la del terreno.", " %"),
        ("abc", "{F} Con la ampliación a 80 m² y un límite de ejemplo de constructibilidad de 75 %, ¿qué corresponde?", "Informar a la arquitecta que supera el límite de ejemplo para que ella decida", "Dibujarla igual, porque lo revisa la municipalidad", "Reducir yo el segundo piso a 60 m²", "El dibujante avisa; la decisión de cambiar el proyecto es de la arquitecta."),
    ],
    ctx=("abc", "La mandante pide entregar el expediente sin la firma de la arquitecta para ahorrar tiempo. ¿Qué respondes?", "Que el expediente necesita la firma del profesional responsable y no puede presentarse sin ella", "Que se presenta igual y la firma se agrega después sin avisar", "Que firme el dibujante en su lugar", "Quien responde por el cumplimiento es el profesional; no se reemplaza su firma."),
    sc=[
        ("En Dibujo Técnico: ¿qué es un expediente de obras?", "Conjunto de planos y documentos que se presenta a la DOM", "Sirve para que la municipalidad revise el proyecto."),
        ("¿Cómo se calcula la ocupación del suelo?", "Superficie del primer piso dividida por la superficie del terreno", "Se expresa como porcentaje para compararla con los límites."),
        ("¿Qué haces con las licencias de símbolos descargados?", "Reviso que el uso esté permitido", "No todo lo que está en internet es de uso libre."),
    ],
    op=("Un terreno de ejemplo mide 250 m². El proyecto tiene un primer piso de 100 m² y un segundo de 75 m². Calcula la ocupación del suelo y la constructibilidad en porcentaje, compáralas con los límites de ejemplo de 50 % y 80 %, y escribe qué avisarías a la arquitecta y qué copias de seguridad harías.",
        "Ocupación: 100 ÷ 250 = 40 %, menor que 50 %. Constructibilidad: (100 + 75) ÷ 250 = 70 %, menor que 80 %. Ambas cumplen los límites de ejemplo, y se lo confirmo a la arquitecta. Copias: en dos lugares distintos, con la revisión en el nombre del archivo.",
        ["calcula los dos porcentajes", "compara con los límites de ejemplo", "propone una copia de seguridad y dice a quién informa"],
        ["hoja con los cálculos y tres líneas de comunicación"],
        ["dividir por la superficie del primer piso en vez de la del terreno", "olvidar el segundo piso en la constructibilidad", "no informar a la arquitecta"],
        "Pregunta: «¿qué piso cuentas en la ocupación y cuáles en la constructibilidad?». Si no responde, repasa las dos definiciones."),
    reinforce="Elige un terreno de 400 m² imaginario, inventa un primer piso y calcula su ocupación del suelo.",
    extend="Explica con un ejemplo inventado por qué un mismo archivo con muchas capas ordena el trabajo de un equipo.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (vivienda de ejemplo, descrita por escrito). Casa de un piso. Planta: living-comedor de 5 m por 4 m; dormitorio de 3 m por 3 m; baño de 2 m por 2 m; muros dibujados con dos líneas continuas gruesas paralelas; "
     "la puerta se dibuja como una abertura con un arco que muestra hacia dónde abre; la ventana, como una abertura con tres líneas finas. "
     "Fachada principal (vista de frente): ancho 9 m, altura del muro 2,5 m, una puerta y dos ventanas. Plano general a escala 1:100; detalle del encuentro de muro y puerta a escala 1:20.")
build(
    O3, 2, F,
    use="Aprenderé a distinguir planta, fachada y sección, a leer sus símbolos y a elegir el nivel de detalle y la escala.",
    prior=["Sé calcular superficies.", "Sé usar escalas.", "Sé qué es un expediente de obras."],
    explain=[
        "La planta es la vista desde arriba, como si se cortara la casa a la altura de las ventanas: muestra muros, puertas, ventanas y la forma de cada ambiente. La fachada, o elevación, es la vista de frente de un lado exterior y muestra altura, puertas y ventanas. La sección es la vista de un corte vertical que permite leer alturas interiores, techo y niveles. Las tres se complementan y deben coincidir.",
        "Los símbolos se explican en una leyenda. En esta ficha, de ejemplo, el muro son dos líneas gruesas paralelas, la puerta tiene un arco y la ventana tres líneas finas; según la norma de dibujo vigente, cada oficina puede definir símbolos adicionales y los debe explicar. El nivel de detalle indica cuánto se muestra: un plano general (escala menor, como 1:100) muestra la casa completa; un plano de detalle (escala mayor, como 1:20) muestra un encuentro entre elementos.",
        "Cada plano debe tener rótulo, escala, norte (en las plantas, una flecha que indica la orientación) y cotas con unidad. El dibujo digital permite ampliar y reproducir sin perder medidas, pero no corrige errores de lectura por sí solo.",
    ],
    vocab=[("planta", "vista del objeto desde arriba"), ("fachada", "vista de frente de un lado exterior"), ("sección", "vista de un corte vertical"), ("leyenda", "lista que explica los símbolos del plano"), ("nivel de detalle", "cuánto se muestra de un elemento"), ("norte", "flecha que indica la orientación de la planta")],
    worked=[
        ("Elegir la vista", "Quieres mostrar cuánto mide la altura del muro y el techo de una casa de ejemplo. ¿Qué vista eliges?", ["La altura se lee en vistas verticales.", "Para mostrar interior y techo se usa la sección."], "La sección"),
        ("Elegir la escala", "Un detalle de una ventana de ejemplo debe verse con mucho detalle y un plano general de una casa debe caber en una hoja. ¿Escala mayor o menor para cada uno?", ["El detalle necesita ampliarse: escala mayor (por ejemplo, 1:10).", "El plano general abarca más: escala menor (por ejemplo, 1:100)."], "Detalle: escala mayor; plano general: escala menor"),
    ],
    mistakes=[("Pensar que una escala 1:100 es mayor que una 1:20 porque 100 es un número más grande.", "En 1:20 el dibujo es menos reducido, es decir, de mayor escala.", "Compara: cuanto menor es el número de la derecha, mayor es la escala."),
              ("Usar símbolos inventados sin leyenda.", "Quien lea el plano no podrá interpretarlos.", "Incluye una leyenda con cada símbolo no habitual.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué muestra una sección?", "Un corte vertical que permite leer alturas interiores", "El objeto visto desde arriba", "Solo el rótulo con la escala", "La sección corta el objeto verticalmente; la planta lo ve desde arriba."),
        ("abc", "¿Para qué sirve la leyenda de un plano?", "Para explicar los símbolos usados", "Para indicar el nombre de la mandante", "Para decir en qué fecha se imprimió", "La leyenda hace legibles los símbolos del plano."),
        ("abc", "¿Qué escala es mayor?", "1:20", "1:100", "Son iguales", "Cuanto menor es el número de la derecha, menos se reduce el dibujo."),
        ("=", "{F} ¿Cuántos m² tiene el living-comedor?", "5*4", "La superficie es largo por ancho.", " m²"),
        ("=", "{F} Entre dormitorio y baño, ¿cuántos m² de superficie hay en total?", "3*3+2*2", "Se calcula cada superficie y se suman.", " m²"),
        ("abc", "{F} ¿Con qué símbolo se dibuja la puerta en la planta?", "Una abertura con un arco que muestra hacia dónde abre", "Dos líneas gruesas paralelas", "Una abertura con tres líneas finas", "En la ficha las dos líneas gruesas son muros y las tres líneas finas, ventanas."),
        ("=", "{F} A escala 1:100, ¿cuántos centímetros ocupa en el papel el ancho de 9 m de la fachada?", "900//100", "9 m son 900 cm, y se dividen por la escala 100.", " cm"),
        ("=", "{F} A escala 1:20, ¿cuántos centímetros ocupa en el papel una puerta de 2 m de alto?", "200//20", "2 m son 200 cm, y se dividen por 20 para pasar al papel.", " cm"),
        ("abc", "{F} Se quiere mostrar el interior del dormitorio con el alto del cielo. ¿Qué vista corresponde?", "La sección", "La fachada principal", "La planta", "La altura interior se lee en un corte vertical."),
        ("abc", "{F} En la planta aparece una puerta de 1 m, pero en la fachada la puerta mide 80 cm de ancho. ¿Qué corresponde?", "Marcar la diferencia y consultar a la proyectista antes de dibujar", "Dejar ambas medidas, porque son vistas distintas", "Usar 90 cm, que queda en el medio", "El ancho de la puerta debe coincidir en todas las vistas; la diferencia es un error."),
        ("abc", "{F} Una compañera dibuja un símbolo propio para un enchufe y no lo explica. ¿Qué falta?", "Una leyenda que explique el símbolo", "Una escala más pequeña", "Una cota adicional del ancho de la hoja", "Un símbolo no habitual necesita leyenda."),
        ("=", "{F} Si el muro de 2,5 m se dibuja a escala 1:50, ¿cuántos milímetros ocupa en el papel?", "250//50*10", "250 cm se dividen por 50 y los centímetros se pasan a milímetros.", " mm"),
        ("=", "{F} A escala 1:100, ¿cuántos centímetros ocupa en el papel el largo de 5 m del living-comedor?", "500//100", "5 m son 500 cm, y se dividen por la escala 100.", " cm"),
    ],
    ctx=("abc", "Una dibujante olvida indicar el norte en la planta. ¿Por qué es un problema?", "Porque no se podrá saber la orientación de la casa respecto del sol y del terreno", "Porque la planta no tendrá muros", "Porque se pierde la escala", "El norte permite leer la orientación de la planta."),
    sc=[
        ("En Dibujo Técnico: ¿qué es una fachada?", "La vista de frente de un lado exterior", "También se llama elevación y muestra un lado exterior."),
        ("¿Qué escala es menor, 1:50 o 1:200?", "1:200", "Mientras mayor es el número de la derecha, más se reduce el dibujo."),
        ("¿Para qué sirve un plano de detalle?", "Para mostrar con precisión un encuentro entre elementos, a escala mayor", "Se amplía solo la parte que necesita más precisión."),
    ],
    op=("Una vivienda de ejemplo tiene un dormitorio de 4 m por 3 m, un baño de 2 m por 2 m y una fachada de 8 m de ancho. Calcula las superficies, calcula cuántos centímetros ocupan 8 m a escala 1:100 y 1:50, y escribe qué vista usarías para mostrar la altura interior y qué símbolo necesita leyenda.",
        "Dormitorio: 12 m²; baño: 4 m². Fachada: 800 cm; a 1:100 son 8 cm y a 1:50 son 16 cm. Para la altura interior: la sección. Un símbolo no habitual, como el de un enchufe, necesita leyenda.",
        ["calcula superficies y medidas en el papel", "elige la vista correcta", "indica un símbolo que requiere leyenda"],
        ["hoja con cálculos y tres respuestas"],
        ["multiplicar en vez de dividir por la escala", "elegir la planta para ver alturas", "no justificar la leyenda"],
        "Pregunta: «¿qué vista usarías para leer la altura del techo y por qué?». Si dice planta, repasa las tres vistas."),
    reinforce="Dibuja en tu cuaderno la planta de un cuarto con una puerta y una ventana usando la simbología de la ficha.",
    extend="Explica con un ejemplo inventado cuándo conviene un plano de detalle además del plano general.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (planta de ejemplo del primer piso, descrita por escrito). Medidas interiores en metros: cocina 3 por 3; living 5 por 4; dormitorio 1 de 4 por 3; dormitorio 2 de 3 por 3; baño 2 por 2; pasillo 4 por 1. "
     "El cuadro de superficies del expediente dice: «Superficie útil del primer piso: 72 m²». La superficie útil es la suma de las superficies de los ambientes, sin contar muros.")
build(
    O3, 3, F,
    use="Aprenderé a revisar una planta descrita y su cuadro de superficies, a detectar diferencias y a escribir una observación clara para el profesional responsable.",
    prior=["Sé calcular áreas de rectángulos.", "Sé qué es un cuadro de superficies.", "Sé qué son planta, fachada y sección."],
    explain=[
        "Un cuadro de superficies es la tabla del expediente donde se anota la superficie de cada ambiente y el total. Para revisarlo se calcula la superficie de cada ambiente (largo por ancho), se suman y se compara el resultado con el total anotado. Esa diferencia se anota con claridad: ambiente, valor leído y valor calculado. La superficie útil suma ambientes sin muros; la superficie construida los incluye y siempre es mayor.",
        "Si una diferencia no se explica con una definición distinta, se trata como posible error y se informa a quien firma el proyecto. No se corrige el cuadro por cuenta propia, porque el dibujante no puede adivinar si el error está en el cuadro o en las medidas de la planta. Tampoco se deja pasar un error pequeño con la idea de que la municipalidad lo revisará.",
        "En el dibujo digital, las superficies pueden calcularse con herramientas del programa, pero siempre se comprueban a mano en este tipo de cuadros: un error de captura de un ambiente (un número equivocado) se detecta con una suma. Las observaciones se escriben de forma breve y respetuosa y quedan registradas con la revisión del plano.",
    ],
    vocab=[("cuadro de superficies", "tabla de superficies de los ambientes y su total"), ("superficie útil", "suma de las superficies de los ambientes, sin muros"), ("superficie construida", "superficie que incluye los muros"), ("observación", "nota breve que describe un posible error"), ("ambiente", "sala o recinto de una vivienda")],
    worked=[
        ("Revisar un total", "Un cuadro de ejemplo anota dos dormitorios de 12 m² y 9 m², y una cocina de 6 m², con un total de 30 m². ¿Es correcto?", ["Se suman los ambientes: 12 + 9 + 6 = 27 m².", "27 m² es distinto de 30 m²: el total tiene una diferencia de 3 m²."], "No: la suma da 27 m², no 30 m²"),
        ("Redactar una observación", "En el ejemplo anterior, ¿cómo escribirías la observación?", ["Se indica el lugar, el valor leído y el valor calculado.", "Se dirige a quien firma el proyecto, sin corregir por cuenta propia."], "«Cuadro de superficies: total leído 30 m²; suma de ambientes 27 m². Se consulta a la arquitecta.»"),
    ],
    mistakes=[("Cambiar el total del cuadro por la suma calculada sin avisar.", "El error podría estar en una medida de la planta y no en el total.", "Anota la diferencia y consulta antes de cambiar."),
              ("Mezclar superficie útil con superficie construida al comparar totales.", "Una incluye muros y la otra no; no se pueden comparar directamente.", "Antes de comparar, confirma qué superficie dice el cuadro.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la superficie útil?", "La suma de las superficies de los ambientes, sin contar muros", "La superficie del terreno completo", "La superficie que incluye los muros", "La superficie útil excluye muros; la construida los incluye."),
        ("abc", "¿Qué tipo de superficie suele ser mayor, la útil o la construida?", "La construida, porque incluye los muros", "La útil, porque suma más ambientes", "Siempre son iguales", "Los muros agregan superficie a la construida."),
        ("abc", "¿Qué debe llevar una observación?", "Ambiente, valor leído y valor calculado", "Solo la palabra «error»", "El nombre de quien cometió el error", "La observación tiene datos que permiten verificar el error."),
        ("=", "{F} ¿Cuántos m² tiene la cocina?", "3*3", "La superficie es largo por ancho.", " m²"),
        ("=", "{F} ¿Cuántos m² tiene el living?", "5*4", "Se multiplica el largo por el ancho.", " m²"),
        ("=", "{F} ¿Cuántos m² suman el dormitorio 1 y el dormitorio 2?", "4*3+3*3", "Se calcula la superficie de cada dormitorio y se suman.", " m²"),
        ("=", "{F} ¿Cuántos m² suman todos los ambientes?", "3*3+5*4+4*3+3*3+2*2+4*1", "Se suman las superficies de los seis ambientes.", " m²"),
        ("abc", "{F} Un compañero suma 3+3+5+4+4+3+3+3+2+2+4+1 (todos los lados) y obtiene 37. ¿Qué error comete?", "Suma los lados en vez de multiplicar largo por ancho en cada ambiente", "Olvida descontar los muros", "Usa metros en vez de centímetros", "La superficie de cada ambiente es largo por ancho; sumar lados no da m²."),
        ("=", "{F} ¿Cuántos m² de diferencia hay entre el cuadro de superficies y la suma de los ambientes?", "72-(3*3+5*4+4*3+3*3+2*2+4*1)", "Se resta la suma de los ambientes a lo que dice el cuadro.", " m²"),
        ("abc", "{F} ¿Qué haces con esa diferencia?", "La anoto y se la informo a la arquitecta antes de corregir", "Cambio el cuadro a 58 y sigo", "Sumo 14 m² al pasillo para que cuadre", "La arquitecta decide si el error está en el cuadro o en las medidas."),
        ("ab", "{F} Un compañero dice que el cuadro puede ser correcto porque incluye los muros. ¿Es válido?", "No: el cuadro dice «superficie útil» y esa excluye los muros", "Sí: todos los cuadros incluyen los muros", "La ficha define la superficie útil como suma de ambientes sin muros; el argumento no corresponde."),
        ("abc", "{F} Si se agregara un baño de 2 m por 3 m, ¿cuánto sumaría el total de ambientes?", "64 m², porque se agregan 6 m² a los 58 m²", "74 m², porque se agregan 2 m²", "60 m², porque se agregan 2 m²", "6 m² más 58 m² dan 64 m²; no se suman los lados, se multiplican."),
        ("abc", "{F} Un compañero propone no avisar de la diferencia: «la municipalidad lo revisará». ¿Qué le respondes?", "Que un error conocido se informa antes de entregar, no se deja para que otro lo encuentre", "Que tiene razón, porque la municipalidad revisa todo", "Que lo importante es entregar rápido", "El equipo debe entregar documentos sin errores conocidos."),
    ],
    ctx=("abc", "Al revisar descubres que escribiste «5 por 4» para un ambiente que en la planta mide 5 por 3. ¿Qué haces?", "Corrijo mi propio error de captura y dejo registrado el cambio con la revisión", "Lo dejo, porque nadie se dará cuenta", "Cambio la planta para que coincida con el cuadro", "Un error propio de captura se corrige y se registra; no se modifica el dato original."),
    sc=[
        ("En Dibujo Técnico: ¿qué diferencia hay entre superficie útil y construida?", "La construida incluye los muros", "La útil suma solo los ambientes."),
        ("¿Cómo se revisa un cuadro de superficies?", "Calculando cada ambiente, sumando y comparando con el total", "Así se detectan las diferencias antes de entregar."),
        ("¿A quién se informa una diferencia no explicada?", "A quien firma el proyecto", "Esa persona decide dónde está el error."),
    ],
    op=("Un cuadro de ejemplo anota: dormitorio 4 m por 3 m; baño 2 m por 2 m; living 6 m por 4 m; total de superficie útil 42 m². Calcula la suma de los ambientes, compárala con el total y escribe la observación que enviarías a la arquitecta.",
        "Dormitorio: 12 m²; baño: 4 m²; living: 24 m². Suma: 40 m². El total dice 42 m²: diferencia de 2 m². Observación: «Cuadro de superficies, total leído 42 m²; suma de ambientes 40 m²; se consulta si falta un ambiente o hay un error de cifra».",
        ["calcula las tres superficies y la suma", "detecta la diferencia", "redacta la observación con lugar, valor leído y valor calculado"],
        ["hoja con cálculos y la observación"],
        ["no sumar los tres ambientes", "corregir el total sin consultar", "escribir una observación sin datos"],
        "Pregunta: «¿por qué no corriges tú el total?». Si no responde, repasa quién decide dónde está el error."),
    reinforce="Calcula la superficie útil de tu casa sumando tres ambientes que midas o estimes.",
    extend="Explica con un ejemplo inventado por qué un error pequeño en un cuadro puede producir otros errores en un expediente.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (sección de ejemplo, descrita por escrito) de una casa de dos pisos. Niveles medidos desde el piso terminado del primer piso, que vale 0 cm: cielo del primer piso, +250 cm; piso del segundo piso, +270 cm; "
     "cielo del segundo piso, +520 cm; punto más alto del techo, +700 cm. Ventana del primer piso: alféizar +100 cm, alto 120 cm. Escala de la sección: 1:50.")
build(
    O3, 4, F,
    use="Aprenderé a leer cotas de nivel en una sección y a calcular alturas libres, espesores de losa y medidas en el papel.",
    prior=["Sé qué es una sección.", "Sé usar escalas.", "Sé restar medidas."],
    explain=[
        "En una sección las alturas se anotan como cotas de nivel: la medida vertical desde un nivel de referencia, que se fija en 0. El piso terminado del primer piso suele ser ese nivel. Un valor con signo más, como +250, está a 250 cm sobre el nivel 0. La altura libre de un recinto es la distancia entre su piso y su cielo, es decir, lo que se puede usar para moverse. La losa es el elemento que separa un piso del siguiente y su espesor es la diferencia entre el nivel del cielo de abajo y el piso de arriba.",
        "Con las cotas de nivel se calculan: altura libre del primer piso = cielo − piso; espesor de losa = piso del segundo piso − cielo del primer piso; altura libre del segundo piso = cielo del segundo − piso del segundo. Las alturas mínimas que exige la reglamentación las fija la norma vigente: en este cuaderno no se usan valores normativos.",
        "Para dibujar la sección a escala, cada cota de nivel se divide por el número de la escala. Antes de entregar se compara con la fachada y con la planta: una ventana, por ejemplo, debe tener el mismo alféizar en la sección y en la fachada. Esa coherencia entre vistas es parte de la calidad del expediente.",
    ],
    vocab=[("cota de nivel", "medida vertical desde un nivel de referencia"), ("nivel 0", "nivel de referencia, normalmente el piso terminado del primer piso"), ("altura libre", "distancia entre el piso y el cielo de un recinto"), ("losa", "elemento que separa un piso del siguiente"), ("espesor", "grosor de un elemento"), ("cielo", "superficie superior de un recinto")],
    worked=[
        ("Calcular la altura libre", "Un recinto de ejemplo tiene el piso en +0 cm y el cielo en +240 cm. ¿Cuál es su altura libre?", ["Altura libre = cielo − piso.", "240 − 0 = 240 cm."], "240 cm"),
        ("Calcular el espesor de una losa", "En otro edificio de ejemplo, el cielo del primer piso está en +260 cm y el piso del segundo en +285 cm. ¿Cuál es el espesor de la losa?", ["Espesor = piso de arriba − cielo de abajo.", "285 − 260 = 25 cm."], "25 cm"),
    ],
    mistakes=[("Calcular la altura libre del segundo piso como 520 − 0.", "Se olvida que el segundo piso empieza en +270 cm, no en 0.", "Resta el nivel del piso de ese recinto al nivel de su cielo."),
              ("Dibujar la sección con una escala distinta de la de la fachada sin avisarlo.", "Las medidas se leerían mal si no se indica cada escala.", "Escribe la escala de cada vista en su título.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una cota de nivel?", "Una medida vertical desde un nivel de referencia", "Una medida horizontal de un muro", "La escala del plano", "Las cotas de nivel dan alturas respecto del nivel 0."),
        ("abc", "¿Qué es la altura libre?", "La distancia entre el piso y el cielo de un recinto", "El espesor de la losa", "La altura total del edificio", "La altura libre es el espacio utilizable entre piso y cielo."),
        ("abc", "¿Qué indica el signo + en +250?", "Que el nivel está sobre el nivel 0", "Que la medida está en milímetros", "Que la medida es un espesor", "El signo más indica un nivel por sobre el de referencia."),
        ("=", "{F} ¿Cuál es la altura libre del primer piso?", "250-0", "Altura libre es cielo menos piso.", " cm"),
        ("=", "{F} ¿Cuál es el espesor de la losa entre los dos pisos?", "270-250", "Es el piso de arriba menos el cielo de abajo.", " cm"),
        ("=", "{F} ¿Cuál es la altura libre del segundo piso?", "520-270", "Se resta el piso del segundo al cielo del segundo.", " cm"),
        ("=", "{F} ¿Cuántos centímetros hay entre el cielo del segundo piso y el punto más alto del techo?", "700-520", "Se resta el cielo al punto más alto.", " cm"),
        ("=", "{F} A escala 1:50, ¿cuántos milímetros ocupa en el papel la altura total hasta el punto más alto?", "700//50*10", "Se divide 700 por 50 y los centímetros se pasan a milímetros.", " mm"),
        ("abc", "{F} ¿A qué nivel está el borde superior de la ventana del primer piso?", "+220 cm, porque 100 + 120 son 220", "+120 cm, porque ese es su alto", "+100 cm, porque ese es su alféizar", "El borde superior es alféizar más alto de ventana."),
        ("abc", "{F} ¿Cabe la ventana bajo el cielo del primer piso?", "Sí: su borde superior está a +220 cm y el cielo a +250 cm", "No: 120 cm es mayor que 100 cm", "No: el alféizar está sobre el cielo", "Se compara el borde superior de la ventana con el nivel del cielo."),
        ("abc", "{F} En la fachada, el alféizar de la misma ventana se dibuja a +110 cm. ¿Qué haces?", "Marco la diferencia con la sección y consulto cuál valor corresponde", "Dejo los dos valores", "Cambio el de la fachada sin avisar", "Una cota que cambia entre vistas es una incoherencia que se consulta."),
        ("=", "{F} Si la losa tuviera 30 cm de espesor y el cielo del primer piso se mantuviera en +250 cm, ¿a qué nivel quedaría el piso del segundo piso?", "250+30", "Se suma el espesor al nivel del cielo de abajo.", " cm"),
        ("abc", "{F} Con esa losa de 30 cm y el cielo del segundo piso en +520 cm, ¿cuál sería su altura libre?", "Cambia: 520 − 280 = 240 cm", "Sigue siendo 250 cm", "Aumenta a 270 cm", "Si el piso del segundo piso sube a +280, su altura libre disminuye."),
    ],
    ctx=("abc", "El mandante pide más altura libre en el primer piso sin cambiar la altura total. ¿Qué respondes?", "Que eso cambia otras cotas y debe decidirlo la arquitecta", "Que se hace de inmediato cambiando el cielo en el dibujo", "Que no se puede, porque las alturas nunca cambian", "Un cambio de alturas afecta a las demás cotas y lo decide quien proyecta."),
    sc=[
        ("En Dibujo Técnico: ¿qué es la altura libre?", "La distancia entre el piso y el cielo", "Se calcula restando el nivel del piso al del cielo."),
        ("¿Cómo se calcula el espesor de una losa?", "Piso de arriba menos cielo de abajo", "Es la diferencia entre ambos niveles."),
        ("¿Qué escala se usa para dibujar cada cota en el papel?", "Se divide la medida real por el número de la escala", "Es la misma regla de siempre."),
    ],
    op=("Una sección de ejemplo anota: piso del primer piso +0 cm; cielo del primer piso +240 cm; piso del segundo +265 cm; cielo del segundo +505 cm; escala 1:50. Calcula las alturas libres, el espesor de la losa y la altura total del cielo del segundo piso en el papel, en milímetros.",
        "Altura libre del primero: 240 cm; espesor de losa: 265 − 240 = 25 cm; altura libre del segundo: 505 − 265 = 240 cm; cielo del segundo en el papel: 505 ÷ 50 = 10,1 cm, es decir, 101 mm.",
        ["calcula las dos alturas libres y el espesor", "convierte la altura a milímetros del papel", "usa las cotas con unidad"],
        ["hoja con cuatro cálculos"],
        ["calcular la altura del segundo piso desde 0", "dividir en vez de multiplicar para pasar a milímetros", "omitir unidades"],
        "Pregunta: «¿desde dónde empieza el segundo piso?». Si no responde, pídele que dibuje una columna con los niveles."),
    reinforce="Mide la altura de una puerta de tu casa en centímetros y calcula cuánto ocuparía en una sección a escala 1:20.",
    extend="Explica con un ejemplo inventado por qué una cota de nivel con error afecta a la fachada y a la sección.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (alternativas de ejemplo). Terreno de 200 m². Alternativa A: casa de dos pisos, primer piso 80 m² y segundo piso 60 m². Alternativa B: casa de un piso, 130 m². "
     "Límites de ejemplo del lugar (rotulados, no son valores reales): ocupación del suelo máxima 50 %; constructibilidad máxima 80 %. "
     "Lista de verificación del expediente de ejemplo: (1) rótulo completo con revisión; (2) escala escrita; (3) cotas con unidad; (4) norte en las plantas; (5) medidas iguales en planta, fachada y sección; (6) firma del profesional.")
build(
    O3, 5, F,
    use="Aprenderé a comparar alternativas de un proyecto con criterios medibles y a verificar la calidad de un expediente con una lista de control.",
    prior=["Sé calcular ocupación y constructibilidad.", "Sé qué es la coherencia entre vistas.", "Sé comparar porcentajes."],
    explain=[
        "Comparar alternativas es medir cada una con los mismos criterios y ordenar los resultados. En un proyecto de vivienda, dos criterios medibles son la ocupación del suelo y la constructibilidad. Se calculan para cada alternativa, se comparan con los límites fijados por la norma vigente de cada lugar y se anota cuál cumple. En este cuaderno los límites son siempre «de ejemplo». El dibujante entrega los cálculos; la decisión entre alternativas la toma la arquitecta con la mandante.",
        "La verificación de calidad usa una lista de control: se revisa cada punto y se anota si cumple, no cumple o no aplica. La lista del expediente incluye el rótulo con la revisión, la escala, las cotas con unidad, el norte, la coincidencia de medidas entre planta, fachada y sección, y la firma del profesional. Un solo punto en rojo impide entregar.",
        "Para dejar trazabilidad, el archivo digital lleva en el nombre la revisión y la fecha, y los cambios se anotan en una tabla de revisiones. Los datos y planos de una mandante son confidenciales y no se comparten con otras personas sin su autorización.",
    ],
    vocab=[("alternativa", "una de las opciones posibles para un mismo proyecto"), ("criterio", "regla medible para comparar opciones"), ("lista de control", "lista de puntos que se revisan antes de entregar"), ("trazabilidad", "posibilidad de seguir qué cambió, cuándo y quién lo hizo"), ("tabla de revisiones", "tabla que registra los cambios de cada versión")],
    worked=[
        ("Comparar con un límite", "Una alternativa de ejemplo tiene 45 m² en el primer piso sobre un terreno de 100 m². El límite de ocupación de ejemplo es 50 %. ¿Cumple?", ["45 ÷ 100 es 45 %.", "45 % es menor que 50 %: cumple."], "Sí, cumple: 45 % es menor que 50 %"),
        ("Usar la lista de control", "Un expediente de ejemplo tiene rótulo completo, escala y firma, pero las cotas no llevan unidad. ¿Se puede entregar?", ["Un punto de la lista no cumple: cotas con unidad.", "Se corrige antes de entregar."], "No, hay que corregir las cotas"),
    ],
    mistakes=[("Elegir la alternativa solo porque es la más grande.", "Hay que cumplir los límites del lugar y los criterios de la mandante.", "Calcula los criterios de cada alternativa y compáralos."),
              ("Marcar «cumple» en un punto de la lista sin haberlo revisado.", "Un punto sin revisar puede ocultar un error que llegue al expediente.", "Revisa cada punto en el dibujo antes de marcarlo.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una lista de control?", "Una lista de puntos que se revisan antes de entregar", "Una lista de precios de los materiales", "Una lista de los dibujantes del equipo", "La lista de control ordena la verificación de calidad."),
        ("abc", "¿Qué es un criterio de comparación?", "Una regla medible para comparar opciones", "La opinión del dibujante", "El color de las líneas", "Un criterio permite comparar con números."),
        ("abc", "¿Quién decide entre dos alternativas de un proyecto?", "La arquitecta con la mandante", "El dibujante, por su cuenta", "El programa de dibujo", "El dibujante entrega cálculos; la decisión es del profesional y la mandante."),
        ("=", "{F} ¿Qué porcentaje de ocupación del suelo tiene la Alternativa A?", "80*100//200", "Primer piso dividido por terreno.", " %"),
        ("=", "{F} ¿Qué porcentaje de constructibilidad tiene la Alternativa A?", "(80+60)*100//200", "Superficie total construida dividida por terreno.", " %"),
        ("=", "{F} ¿Qué porcentaje de ocupación del suelo tiene la Alternativa B?", "130*100//200", "Como es de un piso, toda su superficie es del primer piso.", " %"),
        ("abc", "{F} ¿Cuál alternativa cumple los dos límites de ejemplo?", "La Alternativa A", "La Alternativa B", "Ninguna", "A tiene 40 % y 70 %; B tiene 65 % de ocupación, que supera el 50 %."),
        ("=", "{F} ¿En cuántos puntos porcentuales la Alternativa B supera el límite de ocupación?", "130*100//200-50", "Se resta el límite al porcentaje de B.", " puntos"),
        ("abc", "{F} Si el expediente tiene los puntos (1) a (5) en regla, pero no la firma (6), ¿qué corresponde?", "No entregarlo hasta tener la firma", "Entregarlo, porque cinco de seis es suficiente", "Firmar en nombre del profesional", "La lista exige todos los puntos."),
        ("abc", "{F} En la lista, el punto (5) falla porque la altura del muro es 250 cm en la sección y 260 cm en la fachada. ¿Cuál es la acción correcta?", "Informar la incoherencia para que se confirme cuál es la altura vigente", "Dejar los dos valores", "Poner 255 cm en ambas", "Una incoherencia entre vistas se consulta; no se promedia."),
        ("ab", "{F} La mandante prefiere la Alternativa B. ¿Qué corresponde informar?", "Que B supera el límite de ocupación de ejemplo y qué se podría ajustar", "Nada: la mandante manda y no se discute", "La mandante decide con información completa; el dibujante informa el resultado de los cálculos."),
        ("=", "{F} Para que B cumpla el límite de ocupación de 50 % en un terreno de 200 m², ¿cuántos m² como máximo podría tener en el primer piso?", "200*50//100", "Se aplica el 50 % a la superficie del terreno.", " m²"),
        ("abc", "{F} ¿Qué anotarías en la tabla de revisiones al cambiar el segundo piso de 60 a 70 m²?", "La fecha, el cambio y quién lo pidió o aprobó", "Solo la palabra «cambio»", "Nada, porque es un detalle", "La trazabilidad necesita fecha, descripción y responsable."),
    ],
    ctx=("abc", "La mandante te pide la Alternativa B de la Casa Pehuén para mostrarla a un vecino. ¿Qué corresponde?", "Pedir a la mandante que lo autorice por escrito o que lo haga ella misma", "Enviarlo, porque es su casa", "Enviarlo sin la escala para que no se pueda usar", "Los planos del encargo son confidenciales y la autorización debe ser clara."),
    sc=[
        ("En Dibujo Técnico: ¿para qué sirve una lista de control?", "Para verificar la calidad antes de entregar", "Todo punto de la lista debe cumplir para entregar."),
        ("¿Cómo se comparan dos alternativas?", "Con los mismos criterios medibles", "Así la comparación entre opciones es justa y verificable."),
        ("¿Qué es la trazabilidad?", "Poder seguir qué cambió, cuándo y quién lo hizo", "Se apoya en la tabla de revisiones."),
    ],
    op=("Un terreno de ejemplo mide 300 m². La Alternativa 1 es una casa de un piso de 140 m². La Alternativa 2 es una casa de dos pisos de 90 m² y 70 m². Límites de ejemplo: ocupación 50 %, constructibilidad 60 %. Calcula ambos porcentajes en cada alternativa, indica cuál cumple y escribe tres puntos de una lista de control que revisarías.",
        "Alternativa 1: ocupación 140 ÷ 300 ≈ 47 %, constructibilidad 47 %: cumple los dos. Alternativa 2: ocupación 90 ÷ 300 = 30 %, constructibilidad 160 ÷ 300 ≈ 53 %: cumple los dos. Ambas cumplen. Lista: rótulo con revisión; cotas con unidad; coincidencia de medidas entre vistas. La decisión es de la arquitecta con la mandante.",
        ["calcula los cuatro porcentajes", "compara con los límites de ejemplo", "propone tres puntos de control"],
        ["tabla con los resultados y la lista"],
        ["usar la superficie total en la ocupación", "no compararlos con el límite", "decidir en nombre de la mandante"],
        "Pregunta: «¿qué le informas a la mandante y qué no decides tú?». Si no responde, repasa los roles."),
    reinforce="Calcula la ocupación y la constructibilidad de una casa imaginaria de dos pisos en un terreno de 150 m².",
    extend="Explica con un ejemplo inventado cómo una lista de control evita entregar un plano con errores.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (vivienda de ejemplo, inventada). Plano de redes de una vivienda con un baño y una cocina. Redes: agua potable (fría y caliente), alcantarillado (aguas servidas), electricidad y gas. "
     "Artefactos: 1 lavamanos, 1 inodoro, 1 ducha, 1 lavaplatos y 1 cocina a gas. El rótulo de ejemplo dice: «Proyecto firmado por instalador autorizado; revisar con la norma vigente».")
build(
    O4, 1, F,
    use="Aprenderé qué son las redes interiores de una vivienda, qué riesgos tiene cada una y cuál es el rol de quien dibuja y de quien instala.",
    prior=["Sé leer un plano de planta.", "Sé contar elementos en una lista.", "Sé qué es una leyenda."],
    explain=[
        "Las redes interiores de una vivienda son las instalaciones que van dentro de ella: el agua potable, que lleva agua fría y caliente a los artefactos; el alcantarillado, que lleva las aguas servidas hacia afuera; la electricidad, que alimenta enchufes y luces; y el gas, que alimenta artefactos como la cocina. Un artefacto es un aparato conectado a una red, como un lavamanos o una ducha.",
        "Cada red tiene riesgos distintos. La electricidad puede causar electrocución e incendio. El gas puede causar incendio, explosión o intoxicación si hay una fuga. El agua y el alcantarillado pueden causar daños en la construcción y problemas de salubridad. Por eso, los proyectos y las instalaciones los hacen profesionales e instaladores autorizados, según la norma vigente, y su fiscalización corresponde a las entidades competentes de cada red; en electricidad y gas, la Superintendencia de Electricidad y Combustibles (SEC).",
        "Quien dibuja los planos no instala ni modifica nada en terreno. Su trabajo es representar lo proyectado con claridad y detectar datos que falten o que se contradigan. Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente (por ejemplo, la entidad fiscalizadora de tu sector) y elementos de protección; este cuaderno no te habilita para trabajar.",
    ],
    vocab=[("red interior", "instalación que va dentro de una vivienda"), ("artefacto", "aparato conectado a una red, como un lavamanos"), ("aguas servidas", "agua usada que se evacúa por el alcantarillado"), ("instalador autorizado", "persona habilitada por la entidad competente para instalar"), ("fuga", "salida no controlada de un fluido"), ("SEC", "Superintendencia de Electricidad y Combustibles")],
    worked=[
        ("Asociar red y artefacto", "En una vivienda de ejemplo hay una cocina a gas, un lavamanos y un enchufe. ¿A qué red pertenece cada uno?", ["La cocina a gas usa la red de gas.", "El lavamanos usa agua potable y alcantarillado; el enchufe usa electricidad."], "Cocina: gas; lavamanos: agua potable y alcantarillado; enchufe: electricidad"),
        ("Asociar riesgo y red", "¿Qué riesgo grave tiene una fuga de gas?", ["El gas es combustible.", "Una fuga puede producir incendio, explosión o intoxicación."], "Incendio, explosión o intoxicación"),
    ],
    mistakes=[("Creer que quien dibuja puede corregir en terreno una instalación que le parece mal hecha.", "Modificar instalaciones es trabajo de profesionales e instaladores autorizados.", "Si ves un error en un plano o en una obra, avisa por escrito a la persona responsable."),
              ("Pensar que el alcantarillado y el agua potable son la misma red porque se usan juntos.", "Una lleva agua limpia a los artefactos y la otra evacúa el agua usada.", "Nómbralas y dibújalas por separado.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una red interior?", "Una instalación que va dentro de la vivienda, como agua o gas", "Una calle de la ciudad", "El rótulo de un plano", "Las redes interiores son las instalaciones domiciliarias."),
        ("abc", "¿Qué hace el alcantarillado?", "Evacúa las aguas servidas", "Lleva agua limpia a los artefactos", "Alimenta los enchufes", "El agua limpia la lleva la red de agua potable."),
        ("abc", "¿Qué riesgo principal tiene la electricidad?", "Electrocución e incendio", "Solo mojarse", "Intoxicación por gas", "La electricidad puede causar descargas y fuego."),
        ("=", "{F} Si se agrega una segunda ducha, ¿cuántos artefactos tendrá la vivienda en total?", "5+1", "Se suma el artefacto nuevo a los cinco de la ficha.", " artefactos"),
        ("abc", "{F} ¿A qué red pertenece la cocina a gas?", "A la red de gas", "A la red de alcantarillado", "A la red de electricidad", "La cocina a gas se conecta a la red de gas."),
        ("abc", "{F} ¿Qué redes usa el inodoro?", "Agua potable y alcantarillado", "Solo gas", "Electricidad y gas", "El inodoro recibe agua y evacúa aguas servidas."),
        ("=", "{F} Cuatro artefactos de la ficha usan agua fría y tres usan agua caliente. Si cada uno necesita una conexión por tipo de agua, ¿cuántas conexiones de agua hay?", "4+3", "Se suman las conexiones de agua fría y las de agua caliente.", " conexiones"),
        ("abc", "{F} ¿Cuál artefacto de la ficha no usa agua?", "La cocina a gas", "El lavaplatos", "El inodoro", "La cocina usa gas; el lavaplatos y el inodoro reciben agua potable."),
        ("abc", "{F} Un estudiante quiere revisar el empalme eléctrico para «comprobar el plano». ¿Qué corresponde?", "No tocar instalaciones: la revisión en terreno la hace personal autorizado", "Hacerlo con cuidado, porque es solo mirar", "Hacerlo si usa guantes", "Tocar instalaciones energizadas es un riesgo; lo hace personal autorizado."),
        ("abc", "{F} ¿Quién firma el proyecto, según el rótulo de ejemplo?", "Un instalador autorizado", "El dibujante", "La mandante", "El rótulo de la ficha indica la firma de un instalador autorizado."),
        ("ab", "Una dibujante nota que el plano no dibuja la red de gas, aunque el cuadro de artefactos incluye una cocina a gas. ¿Qué hace?", "Lo informa a la persona responsable del proyecto", "Dibuja una red de gas por su cuenta", "Si falta una red dibujada, no se inventa su trazado: se consulta al responsable."),
        ("abc", "{F} ¿Qué entidad fiscaliza las instalaciones de gas y electricidad?", "La Superintendencia de Electricidad y Combustibles (SEC)", "La junta de vecinos", "El Registro Civil", "La SEC es la entidad fiscalizadora de electricidad y combustibles."),
        ("abc", "{F} Una compañera propone reparar con cinta una fuga de gas que ve en una vivienda para que «no se note». ¿Qué corresponde?", "Avisar de inmediato a una persona adulta responsable y a personal autorizado, sin tocar nada", "Taparla con cinta", "Esperar a ver si crece", "Una fuga de gas es una emergencia; la atiende personal autorizado."),
    ],
    ctx=("abc", "En un plano de ejemplo, el cuadro de artefactos anota una estufa a gas que el dibujo no muestra. ¿Qué haces?", "Registro la omisión y la consulto a quien firmó el proyecto", "Dibujo la estufa donde me parezca", "Lo borro del cuadro para que coincida", "Una omisión se consulta; el dibujante no inventa ni borra datos."),
    sc=[
        ("En Dibujo Técnico: ¿qué es un artefacto?", "Un aparato conectado a una red", "Por ejemplo, un lavamanos o una ducha de la vivienda."),
        ("¿Qué hace quien dibuja redes?", "Representa lo proyectado y detecta datos que faltan o se contradicen", "No instala ni modifica en terreno."),
        ("¿Qué riesgo tiene una fuga de gas?", "Incendio, explosión o intoxicación", "Por eso se avisa a personal autorizado."),
    ],
    op=("Una vivienda de ejemplo tiene: 1 lavamanos, 1 ducha, 1 inodoro, 1 lavaplatos, 1 cocina a gas y 3 enchufes. Escribe una tabla con cada artefacto y las redes que usa (agua fría, agua caliente, alcantarillado, gas, electricidad). Luego cuenta cuántos artefactos usan agua fría y escribe una frase sobre qué harías si el plano no dibujara la red de gas.",
        "Lavamanos: agua fría, agua caliente, alcantarillado. Ducha: agua fría, agua caliente, alcantarillado. Inodoro: agua fría, alcantarillado. Lavaplatos: agua fría, agua caliente, alcantarillado. Cocina: gas. Enchufes: electricidad. Agua fría: 4 artefactos (lavamanos, ducha, inodoro y lavaplatos). Frase: «Informo a la persona responsable que falta la red de gas; no la dibujo por mi cuenta».",
        ["asocia bien artefactos y redes", "cuenta los artefactos con agua fría", "describe la acción correcta ante una omisión"],
        ["tabla de dos columnas y dos frases"],
        ["asociar el inodoro a gas", "inventar la red faltante", "no incluir el alcantarillado"],
        "Pregunta: «¿qué redes usa el lavaplatos?». Si olvida el alcantarillado, repasa para qué sirve."),
    reinforce="Escribe una lista de cuatro artefactos de tu casa y la red a la que pertenece cada uno.",
    extend="Explica con un ejemplo inventado por qué el dibujante no debe modificar una instalación en terreno.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (leyenda de ejemplo del estudio, no oficial). Colores de líneas: azul = agua fría; rojo = agua caliente; marrón = alcantarillado; amarillo = gas; negro = electricidad. "
     "Símbolos de ejemplo: círculo = artefacto; triángulo = llave de paso (válvula que corta el paso); T = derivación. "
     "Un tramo de agua fría de ejemplo: diámetro nominal 20 mm y 300 cm de largo; alcantarillado con pendiente de ejemplo de 2 % (2 cm de bajada por cada 100 cm de largo). "
     "Documentos: plano de planta con el trazado, isométrico (dibujo de la red en perspectiva simplificada), cuadro de artefactos y cuadro de materiales.")
build(
    O4, 2, F,
    use="Aprenderé a leer la leyenda y los documentos de un proyecto de redes, y qué rol cumple cada persona del equipo.",
    prior=["Sé qué es una red interior.", "Sé usar porcentajes sencillos.", "Sé leer cuadros."],
    explain=[
        "Un proyecto de redes interiores se lee con su leyenda, que dice qué significa cada color y símbolo. Los colores y símbolos de esta ficha son de ejemplo de un estudio y no son oficiales: la norma de dibujo vigente y las normas de cada red fijan lo que corresponde. Los documentos son: el plano de planta, que muestra el trazado; el isométrico, un dibujo en perspectiva simplificada que muestra la red como un esquema en tres dimensiones; el cuadro de artefactos; y el cuadro de materiales con tramos y piezas.",
        "El diámetro nominal es el tamaño de referencia de un tubo, indicado en milímetros. La pendiente es la inclinación de un tubo, necesaria en el alcantarillado para que el agua baje; se expresa en porcentaje: 2 % significa 2 cm de bajada por cada 100 cm de largo. La llave de paso es una válvula que corta el paso del fluido. Las derivaciones son los puntos donde un tramo se divide en dos.",
        "Los roles son: el proyectista o instalador autorizado, que diseña y firma; el dibujante, que representa; el revisor, que comprueba que el plano sea coherente; y el instalador, que ejecuta con autorización. Esto es aprendizaje conceptual en papel y no te habilita para instalar nada.",
    ],
    vocab=[("leyenda", "lista que explica colores y símbolos"), ("isométrico", "dibujo de una red en perspectiva simplificada"), ("diámetro nominal", "tamaño de referencia de un tubo, en milímetros"), ("pendiente", "inclinación de un tubo, en porcentaje"), ("llave de paso", "válvula que corta el paso del fluido"), ("derivación", "punto donde un tramo se divide")],
    worked=[
        ("Calcular una bajada", "Un tubo de alcantarillado de ejemplo mide 500 cm y tiene una pendiente de 2 %. ¿Cuántos centímetros baja?", ["2 % son 2 cm por cada 100 cm.", "500 cm tienen 5 grupos de 100 cm: 5 × 2 = 10 cm."], "10 cm"),
        ("Leer la leyenda", "Una línea roja en un plano con la leyenda de la ficha, ¿qué red representa?", ["Se busca el color en la leyenda.", "Rojo = agua caliente."], "Agua caliente"),
    ],
    mistakes=[("Creer que los colores de una leyenda son iguales en todos los planos del mundo.", "Cada estudio o norma puede usar su propia convención, y por eso existe la leyenda.", "Lee siempre la leyenda antes de interpretar el plano."),
              ("Dibujar el alcantarillado sin pendiente porque «se ve más ordenado».", "Sin pendiente el agua no avanza por gravedad.", "Respeta la pendiente indicada en el proyecto y consulta si falta.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿para qué sirve la leyenda de un plano de redes?", "Para explicar el significado de colores y símbolos", "Para indicar el precio de los materiales", "Para indicar quién instaló", "La leyenda hace legibles los símbolos."),
        ("abc", "¿Qué es la pendiente de un tubo de alcantarillado?", "Su inclinación, para que el agua baje", "Su color", "Su largo total", "La pendiente es la inclinación expresada en porcentaje."),
        ("abc", "¿Qué es un isométrico?", "Un dibujo de la red en perspectiva simplificada", "Una tabla de materiales", "El rótulo del plano", "El isométrico muestra la red como un esquema en tres dimensiones."),
        ("abc", "{F} Según la leyenda de ejemplo, ¿qué representa una línea amarilla?", "Gas", "Agua fría", "Electricidad", "En la leyenda de la ficha, amarillo = gas."),
        ("abc", "{F} Según la leyenda de ejemplo, ¿qué representa un triángulo?", "Una llave de paso", "Una derivación", "Un artefacto", "El triángulo es la llave de paso; la T es una derivación y el círculo es un artefacto."),
        ("=", "{F} Un tramo de alcantarillado mide 300 cm con una pendiente de 2 %. ¿Cuántos centímetros baja?", "300*2//100", "Se aplica 2 cm por cada 100 cm.", " cm"),
        ("=", "{F} Otro tramo de alcantarillado mide 450 cm con pendiente de 2 %. ¿Cuántos centímetros baja?", "450*2//100", "Se calcula la bajada con el mismo porcentaje.", " cm"),
        ("abc", "{F} ¿Qué dato indica el tamaño de referencia del tubo de agua fría?", "El diámetro nominal de 20 mm", "El largo de 300 cm", "El color azul", "El diámetro nominal es el tamaño de referencia."),
        ("abc", "{F} Un tramo de la planta se dibuja en azul y el isométrico lo muestra en rojo. ¿Qué haces?", "Consulto cuál es la red correcta y marco la contradicción", "Dejo los dos", "Lo pinto del color que prefiera", "Si dos documentos dan red distinta para el mismo tramo, es incoherencia."),
        ("abc", "{F} Un revisor encuentra un tramo marrón sin pendiente anotada. ¿Qué hace?", "Lo registra como omisión y lo consulta con el proyectista", "Anota una pendiente que le parece buena", "Lo borra del plano", "El revisor informa; no inventa datos que no le corresponde definir."),
        ("ab", "El dibujante duda si un tubo debe tener 20 mm o 25 mm de diámetro nominal. ¿Qué corresponde?", "Consultar al proyectista que firmó el proyecto", "Elegir 25 mm, porque es más seguro", "Elegir el diámetro es una decisión técnica que corresponde al proyectista."),
        ("=", "{F} Si el tramo de agua fría de 300 cm se dibuja en un plano a escala 1:50, ¿cuántos centímetros ocupa en el papel?", "300//50", "Se divide por el número de la escala.", " cm"),
        ("=", "{F} Si una pendiente de ejemplo de 2 % se aplica a un tramo de 1000 cm, ¿cuántos centímetros baja de un extremo al otro?", "1000*2//100", "La bajada es el largo por el porcentaje.", " cm"),
    ],
    ctx=("abc", "Te entregan un plano de gas sin leyenda y con colores que no conoces. ¿Qué haces?", "Pido la leyenda a quien lo entregó antes de interpretarlo", "Supongo que los colores son los habituales", "Pinto de nuevo el plano con mis colores", "Sin leyenda, interpretar los colores sería adivinar su significado."),
    sc=[
        ("En Dibujo Técnico: ¿qué es una derivación?", "Un punto donde un tramo se divide en dos", "Se dibuja con un símbolo en la leyenda."),
        ("¿Para qué sirve la pendiente en el alcantarillado?", "Para que el agua baje por gravedad", "Sin inclinación el agua no avanza."),
        ("¿Quién decide el diámetro de un tubo?", "El proyectista que firma el proyecto", "El dibujante solo lo representa en el plano."),
    ],
    op=("Un plano de ejemplo (leyenda de la ficha) muestra una línea azul de 400 cm hasta un lavamanos, una línea roja de 250 cm al mismo lavamanos y una línea marrón de 350 cm con pendiente de 2 %. Escribe qué red representa cada línea, cuántos centímetros baja la línea marrón y cuántos centímetros de papel ocupa la línea azul a escala 1:50.",
        "Azul: agua fría; roja: agua caliente; marrón: alcantarillado. La línea marrón baja 350 × 2 ÷ 100 = 7 cm. La azul en el papel: 400 ÷ 50 = 8 cm.",
        ["lee bien la leyenda", "calcula la bajada con la pendiente", "convierte a escala"],
        ["tabla y cálculos"],
        ["confundir azul con agua caliente", "calcular la bajada con un porcentaje equivocado", "no dividir por la escala"],
        "Pregunta: «¿cómo lees el color de una línea?». Si no responde, repasa la leyenda."),
    reinforce="Inventa tu propia leyenda de cinco colores para redes y anota qué representa cada uno.",
    extend="Explica con un ejemplo inventado por qué un isométrico ayuda a entender una red que en planta se ve confusa.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (cuadro de metraje de agua fría, de ejemplo). Tramo A–B: 300 cm, diámetro 20 mm. Tramo B–C: 150 cm, diámetro 20 mm. Tramo C–D: 250 cm, diámetro sin anotar. Tramo D–E: 100 cm, diámetro 25 mm. "
     "El cuadro de artefactos de ejemplo dice: «4 artefactos de agua fría». El plano dibuja 5 derivaciones hacia artefactos.")
build(
    O4, 3, F,
    use="Aprenderé a revisar un cuadro de metraje de una red, a sumar longitudes y a detectar datos que faltan o que se contradicen.",
    prior=["Sé sumar longitudes.", "Sé qué es una derivación.", "Sé que no se inventan datos faltantes."],
    explain=[
        "El cuadro de metraje es la tabla que lista cada tramo de una red con su longitud y su diámetro. Sirve para calcular la cantidad de material que se necesita. El metraje total se obtiene sumando las longitudes de todos los tramos, expresadas en la misma unidad. Si un dato falta, por ejemplo el diámetro de un tramo, es una omisión y se pide a quien firma el proyecto.",
        "Para revisar, se hacen tres controles: completitud (todos los tramos tienen longitud y diámetro), coherencia con el cuadro de artefactos (la cantidad de derivaciones coincide con la cantidad de artefactos) y suma (el metraje total coincide con lo que dice el cuadro de materiales). Cada hallazgo se anota con su lugar, el dato leído y el dato esperado.",
        "El material se pide en piezas de largo comercial. Si un tubo comercial de ejemplo mide 600 cm y se necesitan 800 cm, se piden 2 tubos, porque no se pueden pedir fracciones: se redondea hacia arriba. Esta es una tarea de lectura y cálculo; no es un procedimiento de instalación. Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado y norma vigente, y este cuaderno no te habilita para trabajar.",
    ],
    vocab=[("metraje", "longitud de tubo o cable que se necesita"), ("tramo", "parte de una red entre dos puntos"), ("completitud", "que no falte ningún dato"), ("omisión", "dato que falta"), ("redondear hacia arriba", "subir al número entero siguiente cuando sobra una fracción")],
    worked=[
        ("Sumar el metraje", "Una red de ejemplo tiene tramos de 200 cm, 180 cm y 120 cm. ¿Cuál es el metraje total?", ["Se suman: 200 + 180 + 120.", "El total es 500 cm."], "500 cm"),
        ("Calcular tubos comerciales", "Se necesitan 1.300 cm de tubo y cada tubo comercial de ejemplo mide 600 cm. ¿Cuántos tubos se piden?", ["1.300 ÷ 600 da 2 y sobran 100 cm.", "Como sobra, se pide un tubo más: 3 tubos."], "3 tubos"),
    ],
    mistakes=[("Pedir 2 tubos para 1.300 cm con tubos de 600 cm «porque 2 × 600 es casi 1.300».", "2 tubos son 1.200 cm y faltarían 100 cm.", "Divide y, si sobra, redondea hacia arriba."),
              ("Completar el diámetro faltante con el del tramo vecino.", "Pueden ser distintos y un error de diámetro afecta el funcionamiento.", "Anota la omisión y pide el dato.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es el metraje?", "La longitud de tubo o cable que se necesita", "El color de la red", "El precio total", "El metraje se calcula sumando las longitudes de los tramos."),
        ("abc", "¿Qué es una omisión en un cuadro?", "Un dato necesario que falta", "Un dato repetido", "Un dato escrito en metros", "La omisión es un dato ausente."),
        ("abc", "¿Qué haces con un diámetro que falta?", "Pido el dato a quien firma el proyecto", "Pongo el del tramo vecino", "Lo calculo a ojo midiendo el dibujo", "No se inventa el diámetro; se pide al responsable."),
        ("=", "{F} ¿Cuántos centímetros suman todos los tramos?", "300+150+250+100", "Se suman los cuatro tramos, que están en centímetros.", " cm"),
        ("=", "{F} ¿Cuántos centímetros suman los tramos con diámetro de 20 mm anotado?", "300+150", "Solo los tramos A–B y B–C tienen 20 mm anotado.", " cm"),
        ("abc", "{F} ¿Qué tramo tiene una omisión?", "C–D, porque no tiene diámetro anotado", "A–B, porque mide 300 cm", "D–E, porque tiene 25 mm", "Solo el tramo C–D no trae diámetro anotado."),
        ("abc", "{F} El cuadro de artefactos dice 4 y el plano dibuja 5 derivaciones. ¿Qué pasa?", "Hay una incoherencia que debe revisar el proyectista", "Todo está correcto", "Hay una derivación de más que se borra sin consultar", "La cantidad de derivaciones debe coincidir con la de artefactos."),
        ("=", "{F} ¿Cuántas derivaciones sobran respecto del cuadro de artefactos?", "5-4", "Se resta lo esperado a lo dibujado.", " derivación"),
        ("=", "{F} Con tubos comerciales de ejemplo de 600 cm, ¿cuántos tubos se piden para el metraje total?", "(800+599)//600", "Se divide y se redondea hacia arriba.", " tubos"),
        ("abc", "{F} Un compañero escribe «faltan 3 cm de largo en C–D» sin ningún dato más. ¿Qué le falta a su observación?", "Lugar, valor leído y valor esperado", "El nombre del dibujante", "Una fotografía", "Una observación completa da ubicación y valores."),
        ("abc", "{F} El plano muestra el tramo D–E en 25 mm y el isométrico en 20 mm. ¿Qué haces?", "Registro la contradicción y la consulto con el proyectista", "Uso el menor", "Uso el mayor", "Dos documentos con datos distintos se consultan."),
        ("=", "{F} Si se agrega un tramo E–F de 90 cm, ¿cuántos centímetros suman ahora los cinco tramos?", "300+150+250+100+90", "Se suma el tramo nuevo al total.", " cm"),
        ("abc", "{F} Con la suma de los cinco tramos y tubos de 600 cm, ¿cuántos tubos se piden?", "2, porque 890 cm requieren más de 1 tubo", "1, porque 890 es casi 600", "3, para tener repuestos siempre", "890 ÷ 600 da 1 y sobran 290; se redondea a 2."),
    ],
    ctx=("abc", "Una compañera propone pedir 5 tubos «por si acaso» en vez de calcular. ¿Qué respondes?", "Que se calcula con el metraje y se agrega solo la pérdida definida por el proyectista", "Que sí, porque es mejor que sobre mucho", "Que no se pide nada hasta la obra", "El material se cuantifica con el metraje y el criterio del proyecto."),
    sc=[
        ("¿Cómo se obtiene el metraje total?", "Sumando las longitudes en la misma unidad", "Con ese total se calcula el material necesario."),
        ("¿Qué hallazgos revisas en un cuadro de metraje?", "Datos faltantes, coherencia con el cuadro de artefactos y suma", "Son los tres controles que se hacen al revisar."),
        ("¿Qué haces si sobra una fracción de tubo?", "Redondeo hacia arriba", "No se pueden pedir fracciones de tubo entero."),
    ],
    op=("Un cuadro de ejemplo de agua fría anota los tramos 1: 220 cm, diámetro 20 mm; 2: 180 cm, diámetro 20 mm; 3: 300 cm, sin diámetro; 4: 140 cm, 25 mm. El cuadro de artefactos dice 3 artefactos y el plano dibuja 3 derivaciones. Calcula el metraje, los tubos de 600 cm que se piden y escribe las observaciones.",
        "Metraje: 220 + 180 + 300 + 140 = 840 cm. Tubos: 840 ÷ 600 = 1 y sobran 240, por lo tanto 2 tubos. Observaciones: tramo 3, falta el diámetro; las derivaciones coinciden con los artefactos.",
        ["suma el metraje", "redondea hacia arriba", "registra la omisión sin inventar"],
        ["hoja con cálculos y dos observaciones"],
        ["pedir 1 tubo", "completar el diámetro faltante", "no revisar las derivaciones"],
        "Pregunta: «¿por qué 2 tubos y no 1,4?». Si no responde, repasa el redondeo hacia arriba."),
    reinforce="Mide tres tramos de una cinta o cordel y suma su metraje; calcula cuántos tramos de 100 cm necesitarías.",
    extend="Explica con un ejemplo inventado por qué un cuadro de metraje con un diámetro faltante no debe entregarse.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (plano de ejemplo a escala 1:100). Trazado de agua fría medido sobre el plano, en centímetros de papel: tramo 1, 6 cm; tramo 2, 3 cm; tramo 3, 5 cm; tramo 4, 2 cm. "
     "Piezas contadas en el plano: 5 codos y 2 derivaciones. Tubo comercial de ejemplo: 600 cm. Pérdida de ejemplo definida por el proyecto: 10 % sobre el metraje.")
build(
    O4, 4, F,
    use="Aprenderé a calcular el metraje real desde un plano a escala y a obtener la lista de materiales con la pérdida definida por el proyecto.",
    prior=["Sé multiplicar por la escala.", "Sé calcular porcentajes.", "Sé redondear hacia arriba."],
    explain=[
        "Cuando el metraje no está en una tabla, se calcula desde el plano: cada medida del papel se multiplica por el número de la escala para obtener la longitud real. Con la escala 1:100, 6 cm del papel son 600 cm reales. El metraje total es la suma de todos los tramos reales.",
        "Al metraje se le suma una pérdida: el material que se descarta por cortes y ajustes. La pérdida la define el proyecto, y en este cuaderno es siempre un valor de ejemplo. Con una pérdida del 10 %, a 1.000 cm se suman 100 cm. El metraje con pérdida se divide por el largo del tubo comercial y se redondea hacia arriba.",
        "La lista de materiales también cuenta las piezas: codos, derivaciones y otras piezas dibujadas en el plano, una por una. Esa lista la revisa el proyectista. Es un cálculo de papel y no una instrucción de montaje. Esto es aprendizaje conceptual: practicar esta tarea exige instructor autorizado y norma vigente, y este cuaderno no te habilita para trabajar.",
    ],
    vocab=[("metraje real", "longitud real calculada con la escala"), ("pérdida", "material que se descarta por cortes y ajustes"), ("pieza", "elemento suelto como un codo o una derivación"), ("lista de materiales", "tabla con cantidades de cada material")],
    worked=[
        ("Del plano a la realidad", "En un plano de ejemplo a escala 1:50, un tramo mide 8 cm. ¿Cuánto mide en la realidad?", ["Se multiplica por 50: 8 × 50 = 400 cm.", "400 cm son 4 m."], "400 cm"),
        ("Agregar la pérdida", "Un metraje de ejemplo de 2.000 cm con una pérdida de 5 %. ¿Cuánto es el metraje con pérdida?", ["5 % de 2.000 es 100.", "2.000 + 100 = 2.100 cm."], "2.100 cm"),
    ],
    mistakes=[("Olvidar convertir los centímetros del papel a centímetros reales con la escala.", "Se calcularían metrajes cien veces menores que los reales.", "Multiplica siempre cada tramo del plano por el número de la escala."),
              ("Aplicar la pérdida y no redondear hacia arriba al pedir tubos.", "Faltaría material si sobra una fracción de tubo.", "Divide, y si hay resto, pide un tubo más.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la pérdida de material?", "El material que se descarta por cortes y ajustes", "El material que se vende", "El dinero que pierde la empresa", "La pérdida se agrega al metraje."),
        ("abc", "¿Quién define el porcentaje de pérdida?", "El proyecto, es decir, el proyectista", "El dibujante, según su gusto", "El fabricante del plano", "La pérdida es un criterio de proyecto."),
        ("abc", "¿Cómo se pasa una medida del plano a la realidad?", "Multiplicando por el número de la escala", "Dividiendo por el número de la escala", "Restando el número de la escala", "En el plano el tramo está reducido, por lo tanto se multiplica."),
        ("=", "{F} A escala 1:100, ¿cuántos centímetros reales mide el tramo 1?", "6*100", "Se multiplica el tramo del papel por 100.", " cm"),
        ("=", "{F} ¿Cuántos centímetros reales suman los cuatro tramos?", "(6+3+5+2)*100", "Se suman los tramos del papel y se multiplican por 100.", " cm"),
        ("abc", "{F} ¿Cuántos codos se cuentan en el plano?", "5", "2", "7", "La ficha dice 5 codos y 2 derivaciones; 7 sería la suma de ambas piezas."),
        ("=", "{F} ¿Cuántas piezas hay en total entre codos y derivaciones?", "5+2", "Se suman las piezas contadas.", " piezas"),
        ("=", "{F} ¿Cuántos centímetros de pérdida corresponden al 10 % del metraje total?", "1600*10//100", "Se calcula el 10 % del metraje de 1.600 cm.", " cm"),
        ("=", "{F} ¿Cuántos centímetros de metraje con pérdida se necesitan?", "1600+1600*10//100", "Se suma la pérdida al metraje total.", " cm"),
        ("=", "{F} Con tubos de 600 cm, ¿cuántos tubos se piden para el metraje con pérdida?", "(1760+599)//600", "Se divide y se redondea hacia arriba.", " tubos"),
        ("abc", "{F} Un compañero pide 2 tubos porque «1760 ÷ 600 es casi 3». ¿Qué le respondes?", "Que 2 tubos son 1.200 cm y no alcanzan; se piden 3", "Que 2 es correcto", "Que se piden 4, para tener más", "1.760 supera 1.200 y se redondea hacia arriba a 3."),
        ("abc", "{F} En la ficha, ¿cuál de los datos es un valor de ejemplo y no una regla oficial?", "La pérdida de 10 %", "La escala 1:100", "El número de tramos", "La ficha rotula la pérdida como valor de ejemplo definido por el proyecto."),
        ("=", "{F} Si el proyecto cambiara la pérdida a 20 % sobre los 1.600 cm, ¿cuántos centímetros de metraje con pérdida serían?", "1600+1600*20//100", "Se suma el 20 % al metraje total.", " cm"),
    ],
    ctx=("abc", "Calculas los tubos con una pérdida del 10 %, pero el proyectista dice que es 15 %. ¿Qué haces?", "Recalculo con 15 % y dejo anotada la versión del cálculo", "Mantengo el 10 % porque ya lo calculé", "Elijo el promedio, 12,5 %", "La pérdida la fija el proyecto; se recalcula y se registra."),
    sc=[
        ("¿Cómo se calcula el metraje real?", "Se multiplica cada tramo del plano por la escala", "Luego se suman todos los tramos obtenidos."),
        ("¿Qué se hace con una pérdida de 10 %?", "Se suma el 10 % al metraje", "Es material adicional por cortes y ajustes."),
        ("¿Por qué se redondea hacia arriba al pedir tubos?", "Porque no se pueden pedir fracciones y faltaría material", "Siempre se pide un tubo entero."),
    ],
    op=("En un plano de ejemplo a escala 1:50, los tramos de una red miden 10 cm, 8 cm y 6 cm. Hay 3 codos. El proyecto define una pérdida de ejemplo de 10 % y el tubo comercial mide 600 cm. Calcula el metraje real, el metraje con pérdida, los tubos que se piden y escribe la lista de materiales.",
        "Metraje real: (10 + 8 + 6) × 50 = 1.200 cm. Pérdida: 120 cm; con pérdida: 1.320 cm. Tubos: 1.320 ÷ 600 da 2 y sobran 120, por lo tanto 3 tubos. Lista: 3 tubos de 600 cm y 3 codos.",
        ["calcula el metraje real", "agrega la pérdida y redondea hacia arriba", "arma la lista de materiales"],
        ["hoja con cálculos y la lista"],
        ["no multiplicar por la escala", "olvidar la pérdida", "contar los codos mal"],
        "Pregunta: «¿por qué 3 tubos?». Si no responde, repasa el redondeo hacia arriba."),
    reinforce="Elige un recorrido de tu casa, mídelo en pasos y calcula cuántos tramos de 100 cm de cordel necesitarías.",
    extend="Explica con un ejemplo inventado qué pasa si se olvida la pérdida al pedir material.",
)
