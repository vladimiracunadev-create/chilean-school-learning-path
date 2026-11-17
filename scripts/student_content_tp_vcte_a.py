"""Vestuario y Confección Textil TP (3.º y 4.º medio): OAE-01 (diseños básicos de artículos textiles y vestuario) y OAE-02 (moldes manuales y digitales según ficha técnica). Todo en papel: talleres, prendas, telas, medidas y precios inventados y rotulados «de ejemplo»; solo conceptos y cálculos."""
from __future__ import annotations

from tp_vcte_common import build

O1 = "TP-VCTE-3y4-OAE-01"
O2 = "TP-VCTE-3y4-OAE-02"
LIM = " Esto es aprendizaje conceptual en papel, con datos de ejemplo: la práctica en un taller de confección requiere instructor/docente de la especialidad y norma vigente; este cuaderno no te habilita para trabajar. Ante un accidente, avisa a un adulto responsable y a emergencias."

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (taller de confección de ejemplo, inventado). El Taller Aguja de Ejemplo diseña y confecciona poleras y buzos escolares. Etapas: diseño, moldería, corte, confección, terminación y control de calidad. "
     "La diseñadora crea el figurín (dibujo de la prenda sobre una figura humana estilizada) y la ficha técnica; el patronista traza los moldes; el jefe de producción programa la producción; el encargado de calidad revisa el resultado. "
     "Reglas generales: toda prenda se produce según una ficha técnica aprobada; no se copian logos ni diseños de marcas ajenas; el trabajo con computador y mesa de dibujo exige pausas y buena postura; la norma vigente regula el etiquetado de los productos.")
build(
    O1, 1, F,
    use="Aprenderé a situar el trabajo de diseño en un taller de confección: qué se diseña, qué etapas vienen después, qué riesgos hay y qué norma lo regula.",
    prior=["Sé leer una ficha con datos.", "Sé multiplicar y sumar cantidades.", "Sé que una prenda se fabrica en varias etapas antes de llegar a una tienda."],
    explain=[
        "En Vestuario y Confección Textil se diseñan y fabrican prendas de vestir y artículos textiles, como bolsos, cortinas o ropa de cama. El diseño básico parte de una idea y termina en dos documentos: el figurín, que es el dibujo de la prenda sobre una figura humana estilizada, y la ficha técnica, que es el documento con las medidas, la tela, el color y los insumos. Un insumo es todo material que se usa además de la tela, como hilo, botones, cierres o etiquetas.",
        "Para dibujar el figurín se usa un canon de figura, que es la regla de proporciones del cuerpo; se expresa en cabezas de altura, es decir, cuántas veces cabe la cabeza en la altura total. El canon cambia según la edad y el sexo: en niños la cabeza es proporcionalmente más grande, así que su figurín tiene menos cabezas de altura que el de un adulto. Además se consideran las tendencias, que son los estilos y colores que se usan en una temporada, y las innovaciones, como telas o insumos nuevos. Se puede dibujar con herramientas manuales, como lápiz y regla, o informáticas, como un programa de diseño.",
        "Los riesgos del diseño son la mala postura y la fatiga visual por horas frente al papel o la pantalla, por lo que se hacen pausas; el copiar el diseño o el logo de una marca ajena, que es una falta ética; y las omisiones en la ficha, que obligan a rehacer trabajo en etapas posteriores. Un error se corrige más barato antes de cortar la tela, cuando solo existen dibujos y moldes en papel." + LIM,
    ],
    vocab=[("figurín", "dibujo de la prenda sobre una figura humana estilizada"), ("ficha técnica", "documento con medidas, tela, color e insumos de una prenda"), ("insumo", "material que se usa además de la tela, como hilo, botones o etiquetas"), ("canon de figura", "regla de proporciones del cuerpo, medida en cabezas de altura"), ("tendencia", "estilo o color que se usa en una temporada"), ("patronista", "persona que traza los moldes de una prenda")],
    worked=[
        ("Clasificar un material", "En el taller de ejemplo se compra un cierre metálico para unas chaquetas. ¿Es tela o insumo?", ["El cierre se usa además de la tela.", "Eso lo define como insumo."], "Insumo"),
        ("Ubicar al responsable", "Una prenda necesita un dibujo con sus medidas antes de trazar los moldes. ¿Quién crea el documento de la prenda al inicio?", ["La ficha asigna a la diseñadora el figurín y la ficha técnica.", "El patronista actúa después, con ese documento."], "La diseñadora"),
    ],
    mistakes=[("Dibujar un logo parecido al de una marca famosa, cambiando solo el color, para que «se venda mejor».", "Parecerse a una marca ajena puede ser copia y una falta ética.", "Crea un diseño propio y distinto."),
              ("Dejar los botones fuera de la ficha porque «el patronista los agrega».", "Si no están en la ficha, puede faltar el insumo o comprarse uno distinto.", "Anota todos los insumos en la ficha técnica.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué es un figurín?", "Un dibujo de la prenda sobre una figura humana estilizada", "Un molde de papel para cortar la tela", "Una lista de lo que hay en bodega", "El figurín es el dibujo del diseño; el molde es la pieza de papel que se traza después."),
        ("abc", "{F} ¿Quién traza los moldes según la ficha?", "El patronista", "La diseñadora", "El encargado de calidad", "La ficha asigna los moldes al patronista; la diseñadora crea el figurín y el de calidad revisa."),
        ("abc", "{F} ¿Qué dice la ficha sobre los logos de otras marcas?", "No se copian logos ni diseños de marcas ajenas", "Se pueden copiar si se cambia el color", "Se pueden copiar si la prenda es para un colegio", "La regla general es no copiar; cambiar el color o el destino no la elimina."),
        ("abc", "En Vestuario y Confección Textil: ¿cuál de estos materiales es un insumo?", "Un botón para una camisa", "La tela principal de la camisa", "El figurín de la camisa", "El botón se usa además de la tela; la tela es el material principal y el figurín es un dibujo."),
        ("abc", "En Vestuario y Confección Textil: ¿para qué se usa un canon de figura al dibujar el figurín?", "Para mantener proporciones del cuerpo según la edad y el sexo", "Para elegir el color de moda de la temporada", "Para calcular cuánta tela se compra", "El canon fija proporciones; el color depende de las tendencias y la tela se calcula con el consumo."),
        ("abc", "{F} Se detecta que la ficha omitió el largo de la manga. ¿Cuándo es más barato corregirlo?", "Antes de cortar, cuando solo hay dibujos y moldes en papel", "Al final, cuando la prenda ya está terminada", "Durante el empaque, porque ahí se ve el resultado completo", "Antes del corte basta corregir el papel; después hay tela cortada y confección perdidas."),
        ("=", "Un figurín de ejemplo mide 9 cabezas de altura y cada cabeza mide 3 cm. ¿Cuántos cm mide de alto?", "9*3", "La altura es el número de cabezas por el tamaño de una cabeza.", " cm"),
        ("abc", "{F} La diseñadora olvidó anotar el cierre en la ficha. ¿Cuál es la consecuencia más probable?", "En producción puede faltar el cierre o comprarse uno distinto", "Nada, porque el patronista lo define al trazar moldes", "La prenda cambia de talla sola", "Sin el insumo en la ficha, nadie queda obligado a comprarlo con las características correctas."),
        ("abc", "Una diseñadora lleva seis horas seguidas frente a la pantalla sin levantarse. ¿Qué recomendación general corresponde?", "Hacer pausas regulares y cuidar la postura y la distancia a la pantalla", "Seguir hasta terminar para no perder la concentración", "Cambiar solo el brillo de la pantalla", "Las pausas y la postura previenen la fatiga; el brillo solo no basta."),
        ("abc", "Un compañero dice: «si cambio el color del logo de una marca famosa, el diseño ya es mío». ¿Qué corresponde pensar?", "Seguir pareciéndose a una marca ajena puede ser copia; hay que crear un diseño propio", "Es válido, porque cualquier cambio de color crea un diseño nuevo", "Es válido siempre que la prenda no se venda", "Un parecido evidente con una marca ajena sigue siendo copia aunque cambie el color."),
        ("abc", "{F} El encargado de calidad rechaza una polera porque no coincide con lo aprobado. ¿En qué documento se apoya para justificarlo?", "En la ficha técnica aprobada", "En la opinión del jefe de producción", "En el figurín sin medidas", "La ficha aprobada es el respaldo escrito; una opinión o un dibujo sin medidas no basta."),
        ("=", "En una colección de ejemplo hay 4 modelos. Cada modelo necesita 1 hoja de figurín y 2 hojas de ficha técnica. ¿Cuántas hojas se necesitan en total?", "4*(1+2)", "Se suman las hojas de un modelo y se multiplican por los modelos.", " hojas"),
        ("abc", "Un jefe decide cambiar a una tela más barata y avisa solo de palabra al corte. ¿Qué es lo correcto?", "Actualizar la ficha técnica y avisar a moldería, corte y calidad", "Dejar la ficha como está, porque el aviso oral basta", "Cambiar la tela solo en la bodega", "Si la ficha no cambia, otras etapas siguen trabajando con datos que ya no valen."),
    ],
    ctx=("abc", "{F} Un colegio de ejemplo pide buzos para niños de 10 años. ¿Qué debe considerar primero la diseñadora para dibujar el figurín?", "El canon de figura de un niño de esa edad, que tiene menos cabezas de altura que un adulto", "Solo los colores de moda de la temporada", "El precio al que el colegio quiere vender el buzo", "El canon asegura proporciones correctas; los colores y el precio son decisiones posteriores."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué dos documentos produce el diseño básico?", "El figurín y la ficha técnica", "El diseño termina en el dibujo y en el documento con medidas, tela e insumos."),
        ("¿Por qué conviene corregir los errores antes de cortar la tela?", "Porque en esa etapa solo hay dibujos y moldes en papel", "Después del corte hay tela cortada y trabajo hecho que se pierde."),
        ("¿Qué se debe hacer con los logos de otras marcas?", "No copiarlos y crear un diseño propio", "Copiar un logo ajeno es una falta ética aunque se cambie el color."),
    ],
    op=("Un colegio de ejemplo pide una polera de uso diario para estudiantes de 14 años. Escribe una mini ficha con: (a) el nombre de la prenda y la tela que elegirías entre algodón de punto (suave y elástico) y poliéster (liviano y resistente), (b) dos insumos, "
        "(c) una tendencia o color que usarías y (d) una regla de ética o de salud que respetarías mientras diseñas.",
        "(a) Polera escolar de algodón de punto, por ser suave y elástica para el uso diario. (b) Etiqueta de talla y etiqueta de composición y cuidado. (c) Azul marino, un color sobrio y común en uniformes. (d) No copiar logos de marcas ajenas y hacer pausas con buena postura al dibujar.",
        ["nombra la prenda y justifica la tela", "lista dos insumos reales", "indica un color o tendencia", "enuncia una regla de ética o salud"],
        ["mini ficha escrita en el cuaderno"],
        ["no incluir insumos", "copiar el logo de una marca ajena", "no justificar la elección de la tela"],
        "Pregunta: «¿qué pasa si la ficha no dice qué insumos lleva?». Debe responder que podría faltar un material o comprarse uno equivocado."),
    reinforce="Escribe cinco materiales de una polera y clasifica cada uno como tela o insumo.",
    extend="Explica con un ejemplo inventado por qué es más barato corregir un error en la ficha que en la prenda ya cortada.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo, inventada). Modelo: polera escolar PE-14, talla M, versión 2, aprobada por el jefe de producción; responsable de la ficha: la diseñadora. "
     "Tela: algodón de punto (tejido de punto, elástico), color azul marino. Medidas de la prenda terminada: ancho de pecho 52 cm (medido plano, de costura a costura), largo total 66 cm, largo de manga 20 cm. "
     "Insumos: 1 etiqueta de talla y 1 etiqueta de composición y cuidado. Documentos de apoyo: carta de colores (tarjeta con los tonos disponibles) y muestrario de telas (trozos de tela con su nombre y composición).")
build(
    O1, 2, F,
    use="Aprenderé los documentos del diseño (figurín, dibujo plano, ficha técnica, carta de colores y muestrario) y qué rol responde por cada uno.",
    prior=["Conozco las etapas de un taller de confección.", "Sé multiplicar y sumar medidas.", "Sé que el figurín es un dibujo de la prenda."],
    explain=[
        "La ficha técnica reúne los datos de una prenda: modelo, talla, tela, color, medidas de la prenda terminada, insumos, versión y responsable (suele anotarse también la fecha). La versión sirve para saber cuál ficha está vigente cuando se hacen cambios. El dibujo plano es el dibujo de la prenda de frente y de espalda, sin figura humana, que muestra las costuras y los detalles; complementa al figurín, que muestra cómo se ve puesta.",
        "La tela puede ser de tejido plano, formado por hilos que se cruzan en ángulo recto y que casi no se estira, o de tejido de punto, formado por lazadas y más elástico. La carta de colores muestra los tonos disponibles y el muestrario de telas reúne trozos de tela con su nombre y composición; con ambos el cliente elige. Una medida «plana» se toma con la prenda extendida; el contorno de la prenda es el doble del ancho plano.",
        "Cada documento tiene un responsable: la diseñadora redacta la ficha, el jefe de producción la aprueba y el resto de las etapas la usan sin modificarla. Si hay un cambio, se actualiza la ficha con una nueva versión y se avisa a todos; producir con una versión antigua genera errores. Si falta un dato, se pide a la diseñadora y no se inventa." + LIM,
    ],
    vocab=[("dibujo plano", "dibujo de la prenda de frente y espalda, sin figura, con costuras y detalles"), ("versión", "número que indica cuál ficha está vigente"), ("tejido plano", "tela de hilos cruzados en ángulo recto, que casi no se estira"), ("tejido de punto", "tela formada por lazadas, más elástica"), ("carta de colores", "tarjeta con los tonos disponibles"), ("muestrario de telas", "trozos de tela con su nombre y composición"), ("contorno", "medida alrededor de la prenda, el doble del ancho plano")],
    worked=[
        ("Calcular un contorno", "Una prenda de ejemplo mide 48 cm de ancho plano de pecho. ¿Cuál es el contorno de pecho?", ["El contorno es el doble del ancho plano.", "48 × 2 = 96."], "96 cm"),
        ("Elegir el documento", "Se necesita mostrar la prenda de frente y de espalda con sus costuras, sin figura humana. ¿Qué documento corresponde?", ["Es un dibujo sin figura que muestra costuras.", "Eso es el dibujo plano."], "El dibujo plano"),
    ],
    mistakes=[("Producir con la versión 1 de la ficha porque «es la que se tenía impresa».", "La versión 2 puede traer cambios de medidas o insumos.", "Antes de producir, confirma que usas la versión vigente."),
              ("Medir el ancho de pecho de la prenda sin extenderla, siguiendo la curva del cuerpo.", "La ficha define el ancho como medida plana, y otra forma de medir da valores distintos.", "Mide como indica la ficha: plano, de costura a costura.")],
    T=[
        ("abc", "{F} ¿Qué tipo de tela especifica la ficha?", "De tejido de punto", "De tejido plano", "De tejido plano mezclado con punto", "La ficha dice algodón de punto, un tejido de punto y elástico."),
        ("abc", "En Vestuario y Confección Textil: ¿para qué sirve el dibujo plano?", "Para mostrar la prenda de frente y espalda con sus costuras, sin figura humana", "Para mostrar cómo se ve la prenda puesta en una figura", "Para listar las telas disponibles", "El dibujo plano muestra costuras y detalles; el figurín muestra la prenda puesta."),
        ("abc", "{F} ¿Quién es el responsable de redactar la ficha?", "La diseñadora", "El jefe de producción", "El encargado de calidad", "La ficha dice que la diseñadora es la responsable; el jefe de producción solo la aprueba."),
        ("=", "{F} ¿Cuál es el contorno de pecho de la polera?", "52*2", "El contorno es el doble del ancho plano.", " cm"),
        ("abc", "En Vestuario y Confección Textil: ¿qué diferencia hay entre tejido plano y tejido de punto?", "El de punto está formado por lazadas y es más elástico; el plano tiene hilos cruzados y casi no se estira", "El plano está formado por lazadas y es más elástico; el de punto casi no se estira", "Solo se diferencian en el color", "El punto se hace con lazadas elásticas; el plano cruza hilos en ángulo recto."),
        ("abc", "{F} ¿Para qué sirve anotar versión y fecha en la ficha?", "Para saber cuál ficha está vigente cuando hay cambios", "Para calcular el precio de la prenda", "Para decidir la talla del cliente", "La versión identifica la ficha vigente; evita producir con datos antiguos."),
        ("=", "En una tabla de tallas de ejemplo, el ancho plano de pecho sube 4 cm entre una talla y la siguiente (S, M, L, XL). Si la talla M mide 52 cm, ¿cuánto mide la talla XL?", "52+4*2", "De M a XL hay dos tallas, así que se suman dos incrementos.", " cm"),
        ("abc", "{F} Llega la ficha con el campo de medidas vacío. ¿Qué corresponde?", "Pedir a la diseñadora que complete las medidas antes de producir", "Usar las medidas de otra prenda parecida", "Producir y medir después", "Si falta un dato, se pide al responsable y no se inventa."),
        ("abc", "{F} La diseñadora cambia el color de azul marino a verde, pero no actualiza la ficha ni avisa. ¿Qué puede pasar?", "El corte puede comprar tela azul marino porque sigue la versión antigua", "Las etiquetas de composición cambiarán solas", "El patronista cambiará la talla", "Sin ficha actualizada ni aviso, las etapas siguientes trabajan con el dato antiguo."),
        ("abc", "{F} ¿Por qué la ficha aclara que el ancho de pecho se mide «plano, de costura a costura»?", "Para que todas las personas midan de la misma forma y obtengan el mismo valor", "Para que la prenda sea más elástica", "Para ahorrar tela en el corte", "Una forma de medir única evita diferencias entre quien produce y quien revisa."),
        ("abc", "El jefe de producción pide empezar a producir antes de aprobar la ficha, «porque hay apuro». ¿Qué corresponde?", "No producir hasta que la ficha esté aprobada; el apuro no reemplaza el documento", "Producir y aprobar la ficha al terminar", "Producir con la versión anterior", "Producir sin ficha aprobada no deja respaldo si hay errores."),
        ("=", "Para 150 poleras de ejemplo se necesitan 2 etiquetas por polera, y las etiquetas vienen en paquetes de 100. ¿Cuántos paquetes hay que pedir?", "150*2//100", "Se calcula el total de etiquetas y se divide por el contenido de cada paquete.", " paquetes"),
        ("abc", "Dos talleres leen la misma ficha y entregan poleras con distinto ancho de pecho. ¿Cuál es una causa que la ficha ayudaría a evitar?", "Medir de distinta forma por no precisar cómo se mide", "Usar distinto color de hilo", "Tener etiquetas de distinto tamaño", "Si no se indica cómo medir, cada taller aplica su propio criterio."),
    ],
    ctx=("abc", "{F} Una clienta pide «una polera como la PE-14, pero con manga larga». ¿Qué corresponde hacer en los documentos?", "Actualizar la ficha con el nuevo largo de manga y una nueva versión", "Dejar la ficha igual y avisar de palabra", "Crear un figurín nuevo sin cambiar la ficha", "El cambio de medidas debe quedar en la ficha con una versión nueva."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se obtiene el contorno desde el ancho plano?", "Multiplicando el ancho plano por 2", "La prenda tiene una cara delantera y una trasera, así que el contorno es el doble."),
        ("¿Qué indica la versión de una ficha?", "Cuál ficha está vigente", "Así se evita producir con datos antiguos de la ficha."),
        ("¿Quién aprueba la ficha según la ficha 2?", "El jefe de producción", "La ficha lo declara como quien aprueba."),
    ],
    op=("Ficha incompleta de ejemplo. Modelo DE-10 (delantal escolar). Tela: tejido plano de algodón, color beige. Medida: largo total 70 cm. Insumos: 4 botones. "
        "Escribe: (a) cuatro datos que faltan según lo que contiene una ficha técnica, (b) quién debería completarlos y (c) una consecuencia de producir con la ficha así.",
        "(a) Faltan: talla, ancho de pecho, versión y fecha, responsable de la ficha, composición y cuidado de la etiqueta. (b) La diseñadora, que es la responsable de la ficha. (c) Cada etapa podría usar su propio criterio y salir prendas de distinta medida.",
        ["nombra cuatro datos que corresponden a una ficha", "indica a la diseñadora como responsable", "explica una consecuencia concreta"],
        ["hoja con las tres respuestas"],
        ["decir que el patronista inventa las medidas", "no dar ninguna consecuencia", "repetir los datos que ya están"],
        "Pregunta: «¿quién responde si la ficha no se completa?». Debe responder que la diseñadora, y que no se produce hasta tenerla."),
    reinforce="Escribe una ficha técnica de ejemplo de un delantal con los ocho campos: modelo, talla, tela, color, medidas, insumos, versión y responsable.",
    extend="Explica con un ejemplo inventado qué sucede cuando dos personas miden el ancho de una prenda de formas distintas.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (encargo de ejemplo, inventado). Un club deportivo infantil pide 40 camisetas para niños de 8 a 10 años, en rojo y blanco. Presupuesto máximo para tela: $200.000. Cada camiseta usa 1 metro de tela. El club pide que la tela se seque rápido. "
     "Opción A: algodón de punto grueso, $3.500 el metro; absorbente, fresco y se seca lento. Opción B: poliéster deportivo, $4.800 el metro; liviano y se seca rápido. Opción C: lana gruesa, $9.000 el metro; abrigada, requiere lavado delicado y se seca lento. "
     "Cada camiseta lleva una etiqueta de talla y una de composición y cuidado.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un encargo de diseño en papel: comparar opciones de tela con las condiciones del cliente y justificar una decisión.",
    prior=["Conozco la ficha técnica y sus insumos.", "Sé multiplicar y restar.", "Sé comparar un costo con un presupuesto."],
    explain=[
        "Un encargo de diseño trae condiciones: la cantidad de prendas, la edad de quienes la usan, los colores, el uso y el presupuesto. Al analizar un caso se lee primero las condiciones y recién después se comparan las opciones de tela, color e insumos. Una opción solo se puede elegir si cumple todas las condiciones obligatorias; entre las que las cumplen se elige la que mejor responde al uso.",
        "El costo de la tela de un pedido se calcula multiplicando el precio por metro por los metros que se usan. Si el costo supera el presupuesto, la opción se descarta aunque otras características sean buenas. También se consideran las propiedades de la tela, como si absorbe, si se seca rápido o si es abrigada, porque determinan si sirve para el uso pedido.",
        "Si cambia una condición, como el presupuesto o el uso, la decisión debe revisarse: lo que era correcto puede dejar de serlo. Por eso se deja anotado qué criterio decidió y qué evidencia lo respalda. Además, la ética de diseño exige no copiar escudos ni logos ajenos: un club debe tener su propio emblema." + LIM,
    ],
    vocab=[("presupuesto", "cantidad máxima de dinero disponible para un gasto"), ("condición obligatoria", "requisito del cliente que toda opción debe cumplir"), ("propiedad de la tela", "característica como absorber, secarse rápido o abrigar"), ("emblema", "escudo o logo propio de una institución"), ("descartar", "dejar fuera una opción por no cumplir una condición")],
    worked=[
        ("Aplicar una condición obligatoria", "Un cliente de ejemplo pide 20 delantales con un máximo de $50.000 para tela y cada delantal usa 2 metros. Una tela cuesta $1.500 el metro. ¿Cumple el presupuesto?", ["Se calculan los metros: 20 × 2 = 40.", "El costo es 40 × 1.500 = 60.000, que supera 50.000."], "No cumple: cuesta $60.000"),
        ("Revisar al cambiar la condición", "Un cliente de ejemplo pidió una tela fresca y luego cambia: ahora quiere una tela abrigada. ¿Se mantiene la elección anterior?", ["La condición del uso cambió.", "Hay que volver a comparar las opciones con el nuevo criterio."], "No, se revisa la decisión"),
    ],
    mistakes=[("Elegir la opción más barata sin revisar si cumple el uso pedido.", "El precio es solo una condición; el uso también es obligatorio.", "Descarta las que incumplen el presupuesto o el uso y elige entre las restantes."),
              ("Copiar el escudo de un equipo famoso porque «a los niños les gusta».", "Es copia de un emblema ajeno.", "Diseña un emblema propio para el club.")],
    T=[
        ("abc", "{F} ¿Qué opción cumple el presupuesto y el secado rápido que pide el club?", "La opción B", "La opción A", "La opción C", "B cuesta 40 × 4.800 = 192.000 y se seca rápido; A se seca lento y C supera el presupuesto."),
        ("abc", "{F} ¿Qué condición descarta primero la opción C?", "Supera el presupuesto: costaría $360.000", "Es demasiado liviana para el deporte", "No existe en color rojo", "C cuesta 40 × 9.000 = 360.000, más que los $200.000 disponibles."),
        ("=", "{F} ¿Cuánto cuesta la tela para las 40 camisetas con la opción A?", "40*3500", "Se multiplica el precio por metro por los metros necesarios.", " pesos"),
        ("abc", "{F} La opción A cumple el presupuesto. ¿Por qué no se elige?", "Porque se seca lento y el club pidió secado rápido", "Porque es más cara que B", "Porque no se puede teñir de rojo", "A cuesta menos, pero incumple la condición del secado rápido."),
        ("=", "{F} Con la opción B, ¿cuánto dinero sobra del presupuesto?", "200000-40*4800", "Se resta el costo de la tela al presupuesto.", " pesos"),
        ("abc", "{F} El club cambia su pedido: ya no pide secado rápido, sino abrigo para entrenar en invierno, y sube el presupuesto a $400.000. ¿Qué opción conviene ahora?", "La opción C, porque es abrigada y su costo de $360.000 cabe en el presupuesto", "La opción A, porque es más barata", "La opción B, porque sigue siendo liviana", "Con el nuevo uso se busca abrigo, y C es la abrigada que cumple el presupuesto."),
        ("=", "{F} Para las 40 camisetas se piden las dos etiquetas de cada camiseta más 4 etiquetas de repuesto. ¿Cuántas etiquetas se necesitan en total?", "40*2+4", "Se multiplican las etiquetas por camiseta por las camisetas y se suman los repuestos.", " etiquetas"),
        ("abc", "{F} Falta un dato en el encargo: no dice dónde va el emblema del club. ¿Qué corresponde antes de cerrar la ficha?", "Pedir al club que indique la ubicación y el tamaño del emblema", "Poner el emblema donde el patronista prefiera", "Omitir el emblema para no perder tiempo", "La ficha debe llevar la ubicación y el tamaño; no se inventan datos del cliente."),
        ("=", "{F} El club agrega 5 camisetas y pide 45 en total con la opción B. ¿Cuánto costaría la tela?", "45*4800", "Se multiplica el precio por metro por las 45 camisetas de un metro.", " pesos"),
        ("abc", "{F} Con las 45 camisetas de la opción B, ¿qué corresponde si el presupuesto sigue siendo de $200.000?", "Informar al club que se supera el presupuesto y proponer ajustar la cantidad o el presupuesto", "Usar la opción C para compensar", "Reducir el metro de tela por camiseta sin avisar", "Se debe informar y acordar con el cliente; no se cambia en silencio lo pedido."),
        ("abc", "El club pide copiar el escudo de un equipo profesional «para que se parezca». ¿Qué debe responder el taller?", "Proponer un emblema propio, porque copiar un escudo ajeno no es correcto", "Copiarlo, porque el club lo pidió", "Copiarlo cambiando solo el color", "El pedido del cliente no autoriza copiar un emblema ajeno."),
        ("=", "{F} Con la opción B y un presupuesto de $200.000, ¿cuál es el máximo de camisetas completas de 1 metro que se pueden hacer?", "200000//4800", "Se divide el presupuesto por el costo de una camiseta y se toma el número entero.", " camisetas"),
        ("abc", "{F} Un compañero afirma: «B es la mejor porque siempre es la mejor tela para el deporte». ¿Qué falla en esa afirmación?", "No se apoya en las condiciones del encargo ni en datos de costo y secado", "Que B es más cara que C", "Que el poliéster no se usa en camisetas", "Una buena decisión muestra la evidencia del encargo; una afirmación general no la reemplaza."),
    ],
    ctx=("=", "{F} El club decide encargar 38 camisetas con la opción B. ¿Cuántos pesos sobran del presupuesto de $200.000?", "200000-38*4800", "Se calcula el costo de la tela y se resta del presupuesto.", " pesos"),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué se hace primero al analizar un encargo?", "Leer las condiciones del cliente", "Las condiciones determinan qué opciones se pueden elegir."),
        ("¿Qué pasa con una opción que supera el presupuesto?", "Se descarta", "El presupuesto es una condición obligatoria."),
        ("¿Qué se debe hacer si cambia una condición del encargo?", "Revisar la decisión con el nuevo criterio", "La mejor opción puede dejar de serlo."),
    ],
    op=("Encargo de ejemplo: un colegio pide 30 delantales para niños de 6 años, de color amarillo, con un presupuesto de $90.000 para tela; cada delantal usa 2 metros y la tela debe lavarse con facilidad. "
        "Opción 1: algodón liso, $1.400 el metro, fácil de lavar. Opción 2: lino, $2.500 el metro, requiere planchado cuidadoso. "
        "Escribe: (a) el costo de tela de cada opción, (b) cuál eliges y por qué, (c) qué cambiaría tu decisión.",
        "(a) Opción 1: 30 × 2 × 1.400 = 84.000. Opción 2: 30 × 2 × 2.500 = 150.000. (b) La opción 1, porque cumple el presupuesto y el lavado fácil; la 2 supera los $90.000. (c) Si el presupuesto subiera a $150.000 o más y el colegio aceptara el planchado cuidadoso, la opción 2 se podría considerar.",
        ["calcula bien los costos", "elige la opción que cumple las condiciones", "indica qué condición cambiaría la decisión"],
        ["hoja con los tres puntos"],
        ["olvidar que cada delantal usa 2 metros", "elegir solo por el precio sin revisar el uso", "no justificar"],
        "Pregunta: «¿qué pasa si el presupuesto cambia?». Debe responder que se vuelven a comparar las opciones."),
    reinforce="Inventa un encargo de 10 bolsos con un presupuesto y dos telas con precio por metro. Calcula cuál cumple y justifica.",
    extend="Explica con un ejemplo inventado por qué no basta elegir la tela más barata.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (datos de diseño de ejemplo, inventados). Figurín A (adulto): 9 cabezas de altura, cada cabeza de 3 cm. Figurín B (niño de 8 años): 6 cabezas de altura, cada cabeza de 4 cm. "
     "Costos del modelo PE-14 por prenda: tela 1 metro a $3.600; hilo $200; 2 etiquetas a $120 cada una; mano de obra $2.500. Costo de materiales es la suma de la tela y los insumos (hilo y etiquetas); costo total es el costo de materiales más la mano de obra.")
build(
    O1, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos: calcular la altura de un figurín según su canon y el costo de materiales y total de una prenda.",
    prior=["Conozco el figurín y el canon de figura.", "Sé multiplicar y sumar con enteros.", "Sé leer una ficha de costos."],
    explain=[
        "La altura de un figurín se calcula multiplicando el número de cabezas del canon por lo que mide una cabeza. En el canon de un adulto de ejemplo hay más cabezas de altura que en el de un niño; por eso, aunque la cabeza dibujada sea más grande en el niño, su figurín puede quedar más bajo. Las proporciones cambian según edad y sexo, y el diseñador usa el canon que corresponde a quien usará la prenda.",
        "El costo de una prenda se calcula por partes. El costo de materiales es la suma de la tela y los insumos, como hilo, etiquetas, botones o cierres. El costo total agrega la mano de obra, que es el pago por el trabajo de confección. Si el taller quiere ganar una cantidad por prenda, la suma al costo total para obtener el precio de venta.",
        "Para un pedido se multiplica el costo por prenda por la cantidad de prendas. Si cambia un precio o se agrega un insumo, hay que recalcular. Los cálculos se anotan en la ficha o en una planilla, de modo que otra persona pueda revisarlos. Una prenda no se produce hasta que el costo esté calculado y aprobado." + LIM,
    ],
    vocab=[("cabeza de altura", "unidad de medida del canon: cuántas veces cabe la cabeza en la altura"), ("costo de materiales", "suma del costo de la tela y los insumos"), ("mano de obra", "pago por el trabajo de confección"), ("costo total", "costo de materiales más mano de obra"), ("precio de venta", "costo total más la ganancia que busca el taller")],
    worked=[
        ("Altura de un figurín", "Un figurín de ejemplo tiene 8 cabezas de altura y cada cabeza mide 2 cm. ¿Cuánto mide de alto?", ["Se multiplica el número de cabezas por el tamaño de una cabeza.", "8 × 2 = 16."], "16 cm"),
        ("Costo de una bolsa", "Una bolsa de ejemplo usa 2 metros de tela a $2.000 y un cierre de $500. ¿Cuánto cuestan los materiales?", ["Se calcula la tela: 2 × 2.000 = 4.000.", "Se suma el cierre: 4.000 + 500 = 4.500."], "$4.500"),
    ],
    mistakes=[("Calcular el costo de un pedido de 50 poleras multiplicando 50 solo por el precio de la tela.", "Quedan fuera los insumos y la mano de obra.", "Multiplica por el costo total de una prenda."),
              ("Creer que un canon con más cabezas siempre da una cabeza más grande.", "Las cabezas son una unidad de proporción y cada figurín fija el tamaño de su cabeza.", "Calcula la altura multiplicando cabezas por el tamaño de una cabeza.")],
    T=[
        ("=", "{F} ¿Cuántos cm de alto mide el figurín A?", "9*3", "La altura es el número de cabezas por el tamaño de cada cabeza.", " cm"),
        ("=", "{F} ¿Cuántos cm de alto mide el figurín B?", "6*4", "Se multiplican las cabezas de altura por el tamaño de una cabeza.", " cm"),
        ("abc", "{F} ¿Cuál figurín tiene la cabeza proporcionalmente más grande respecto de su altura?", "El figurín B, porque su altura es de solo 6 cabezas", "El figurín A, porque tiene más cabezas", "Ninguno, porque ambos miden cabezas", "Con menos cabezas de altura, cada cabeza es una parte mayor del total."),
        ("=", "{F} ¿Cuál es el costo de materiales de una polera PE-14?", "3600+200+2*120", "Se suman la tela y los insumos: hilo y dos etiquetas.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de una polera PE-14?", "3600+200+2*120+2500", "Al costo de materiales se le suma la mano de obra.", " pesos"),
        ("=", "{F} Si el precio de la tela sube a $4.200 el metro, ¿cuál sería el nuevo costo de materiales?", "4200+200+2*120", "Se reemplaza el precio de la tela y se suman los insumos.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuestan los materiales de un pedido de 50 poleras PE-14?", "50*(3600+200+2*120)", "Se calcula el costo de materiales de una polera y se multiplica por 50.", " pesos"),
        ("=", "{F} El cliente pide agregar un cierre de $350 por prenda. ¿Cuál es el nuevo costo total de una polera?", "3600+200+2*120+2500+350", "Se suma el insumo nuevo al costo total anterior.", " pesos"),
        ("=", "{F} El taller quiere ganar $1.800 por polera. ¿Cuál es el precio de venta?", "3600+200+2*120+2500+1800", "El precio de venta es el costo total más la ganancia buscada.", " pesos"),
        ("abc", "Un diseñador rebaja la mano de obra quitando un bolsillo que el cliente había pedido en la ficha. ¿Qué corresponde hacer?", "Consultar al cliente y actualizar la ficha antes de producir sin el bolsillo", "Quitarlo sin avisar, porque ahorra dinero", "Mantener el bolsillo y no registrar nada", "Un cambio de diseño exige acuerdo con el cliente y una ficha actualizada."),
        ("abc", "{F} Un compañero calcula el costo de 50 poleras solo con el precio de la tela. ¿Qué omite?", "El hilo, las etiquetas y la mano de obra", "El figurín y su canon", "La talla del cliente", "El costo total de una prenda incluye insumos y mano de obra además de la tela."),
        ("=", "{F} El taller tiene $300.000 solo para materiales. ¿Cuántas poleras completas puede hacer?", "300000//(3600+200+2*120)", "Se divide el presupuesto por el costo de materiales de una polera y se toma el número entero.", " poleras"),
        ("=", "Un figurín de 9 cabezas con cabeza de 2 cm se dibuja en una hoja de 20 cm de alto. ¿Cuántos cm sobran de la hoja?", "20-9*2", "Se calcula la altura del figurín y se resta del alto de la hoja.", " cm"),
    ],
    ctx=("=", "Un colegio de ejemplo pide 80 buzos. Los materiales de cada buzo cuestan $6.100 y el colegio dispone de $450.000 para materiales. ¿Cuántos buzos completos alcanzan?", "450000//6100", "Se divide lo disponible por el costo de materiales de un buzo y se toma el número entero.", " buzos"),
    sc=[
        ("En Vestuario y Confección Textil: ¿cómo se calcula la altura de un figurín?", "Multiplicando las cabezas de altura por lo que mide una cabeza", "El canon expresa la altura en cabezas."),
        ("¿Qué incluye el costo total de una prenda?", "Los materiales y la mano de obra", "El costo total suma lo que se gasta en materiales y en el trabajo."),
        ("¿Qué se debe hacer cuando sube el precio de la tela?", "Recalcular el costo", "Un precio nuevo cambia el costo de materiales y el total."),
    ],
    op=("Datos de ejemplo de una mochila escolar: tela 3 metros a $2.500; dos cierres a $450 cada uno; una etiqueta de $100; mano de obra $4.000. El taller quiere ganar $2.000 por mochila. "
        "Escribe: (a) el costo de materiales, (b) el costo total, (c) el precio de venta y (d) cuánto costarían los materiales de 20 mochilas.",
        "(a) 3 × 2.500 + 2 × 450 + 100 = 7.500 + 900 + 100 = 8.500. (b) 8.500 + 4.000 = 12.500. (c) 12.500 + 2.000 = 14.500. (d) 20 × 8.500 = 170.000.",
        ["calcula la tela con los metros", "separa costo de materiales y mano de obra", "suma la ganancia para el precio", "multiplica por la cantidad"],
        ["hoja con los cuatro cálculos"],
        ["olvidar el segundo cierre", "incluir la ganancia dentro del costo total", "usar el costo total para los 20 materiales"],
        "Pregunta: «¿qué suma entra en el costo de materiales?». Debe responder tela e insumos, no mano de obra."),
    reinforce="Calcula el costo de materiales de una prenda inventada con tres insumos y una tela, con precios de ejemplo.",
    extend="Explica por qué el precio de venta no puede ser igual al costo total.",
)

# ============================================================ OAE-01, clase 5
F = ("Ficha 5 (comparación de dos diseños de delantal infantil, de ejemplo). Una ficha técnica completa tiene 8 campos: modelo, talla, tela, color, medidas, insumos, versión y responsable. Mano de obra de ejemplo: $50 por minuto. "
     "Diseño 1: materiales $5.400; tiempo de confección 30 minutos; ficha con los 8 campos; lleva 5 botones. Diseño 2: materiales $4.600; tiempo de confección 24 minutos; ficha con 6 campos (faltan medidas y responsable); no lleva botones. "
     "Costo total por delantal: materiales más mano de obra (minutos por $50). Encargo: 40 delantales para niños de 3 años. Presupuesto máximo de $6.000 por delantal.")
build(
    O1, 5, F,
    use="Aprenderé a comparar alternativas de diseño con criterios de costo, seguridad y calidad de la ficha, y a verificar que la decisión quede respaldada.",
    prior=["Sé calcular costo de materiales y costo total.", "Sé qué campos tiene una ficha técnica.", "Sé comparar un costo con un presupuesto."],
    explain=[
        "Para comparar dos diseños se usan criterios que se pueden verificar: el costo total, el cumplimiento del presupuesto, la seguridad del producto para quien lo usa y la calidad de la ficha técnica. Una ficha completa tiene los campos de modelo, talla, tela, color, medidas, insumos, versión y responsable; si falta alguno, la ficha no está lista para producir y el diseño no puede aprobarse aún.",
        "En prendas para niños pequeños, las piezas que pueden soltarse, como botones o adornos, son un riesgo porque pueden llevarse a la boca. Por eso el diseño evita piezas pequeñas sueltas y respeta la norma vigente de seguridad de productos infantiles. El costo no justifica incumplir la seguridad. Esta es una regla general, no una cifra legal.",
        "Verificar significa comprobar con evidencia: los tiempos se respaldan con mediciones registradas, los costos con la ficha y la decisión con un criterio escrito. Si el diseño más conveniente tiene la ficha incompleta, se pide completarla antes de producir. Quien decide registra los cálculos, la alternativa descartada y el motivo." + LIM,
    ],
    vocab=[("ficha completa", "ficha con los ocho campos escritos"), ("pieza pequeña suelta", "botón o adorno que puede desprenderse y es riesgo para niños pequeños"), ("verificar", "comprobar con evidencia que un dato o resultado es correcto"), ("criterio", "regla que se usa para comparar y decidir"), ("alternativa descartada", "opción que no se elige y cuyo motivo se registra")],
    worked=[
        ("Comparar dos costos", "Un diseño de ejemplo X cuesta en materiales $2.000 y 10 minutos de mano de obra a $40 el minuto. ¿Cuál es su costo total?", ["La mano de obra es 10 × 40 = 400.", "El costo total es 2.000 + 400 = 2.400."], "$2.400"),
        ("Revisar una ficha", "Una ficha de ejemplo tiene escritos 7 de los 8 campos. ¿Está lista para producir?", ["Una ficha completa necesita los 8 campos.", "Falta uno, así que no está lista."], "No está lista"),
    ],
    mistakes=[("Elegir un diseño solo por ser más barato aunque su ficha esté incompleta.", "Sin ficha completa no se puede producir de forma confiable.", "Pide completar la ficha antes de aprobar el diseño."),
              ("Aceptar un tiempo de confección «porque lo dijo el taller» sin ningún registro.", "Un dato sin respaldo no se puede verificar.", "Usa tiempos registrados con su fuente.")],
    T=[
        ("abc", "{F} ¿Qué diseño tiene la ficha completa?", "El diseño 1, que tiene los 8 campos", "El diseño 2, que tiene 6 campos", "Los dos, porque ambos tienen modelo", "Una ficha completa requiere los 8 campos; el diseño 2 no tiene medidas ni responsable."),
        ("=", "{F} ¿Cuántos pesos cuesta la mano de obra de un delantal del diseño 1?", "30*50", "Se multiplican los minutos por el costo de cada minuto.", " pesos"),
        ("abc", "En Vestuario y Confección Textil: ¿qué significa verificar un dato de la ficha?", "Comprobarlo con evidencia, como un registro o una medición", "Aceptarlo porque lo dijo una persona de confianza", "Copiarlo de otra ficha parecida", "Verificar exige evidencia comprobable y no solo confianza."),
        ("=", "{F} ¿Cuál es el costo total de un delantal del diseño 1?", "5400+30*50", "El costo total es el costo de materiales más la mano de obra.", " pesos"),
        ("=", "{F} ¿Cuál es el costo total de un delantal del diseño 2?", "4600+24*50", "Se suman los materiales y la mano de obra del diseño 2.", " pesos"),
        ("abc", "{F} ¿Por qué no basta elegir el diseño 2 solo por ser más barato?", "Porque su ficha está incompleta y no se puede producir de forma confiable", "Porque no lleva botones y eso lo hace menos seguro", "Porque tiene menos minutos de confección", "El costo es un criterio, pero producir con la ficha incompleta genera errores."),
        ("=", "{F} ¿Cuánto costarían los 40 delantales del diseño 1?", "40*(5400+30*50)", "Se multiplica el costo total de un delantal por la cantidad de delantales.", " pesos"),
        ("abc", "{F} Falta el largo total del diseño 2. ¿A quién corresponde completarlo?", "A la diseñadora, que es quien redacta la ficha", "Al encargado de calidad", "Al cliente, que usará el delantal", "La responsable de redactar la ficha técnica es la diseñadora."),
        ("=", "{F} ¿Cuántos pesos se ahorran en los 40 delantales si se eligiera el diseño 2 en lugar del diseño 1?", "40*((5400+30*50)-(4600+24*50))", "Se calcula la diferencia de costo por delantal y se multiplica por 40.", " pesos"),
        ("abc", "{F} Como los delantales son para niños de 3 años, ¿qué criterio de seguridad conviene comparar además del costo?", "Que no lleve piezas pequeñas sueltas como botones", "Que tenga el color más oscuro", "Que se confeccione en menos minutos", "Las piezas pequeñas pueden llevarse a la boca; es un riesgo en niños pequeños."),
        ("abc", "El taller elige el diseño 2 y anota 20 minutos de confección, sin ninguna medición registrada. ¿Qué falla?", "El tiempo no tiene respaldo y no se puede verificar", "El diseño 2 no tiene botones", "El tiempo es mayor que en el diseño 1", "Un dato sin registro ni fuente no permite comprobar el cálculo del costo."),
        ("=", "{F} Con $250.000, ¿cuántos delantales completos del diseño 2 se pueden hacer?", "250000//(4600+24*50)", "Se divide el dinero disponible por el costo total de un delantal y se toma el número entero.", " delantales"),
        ("abc", "{F} Considerando el presupuesto máximo, la seguridad para niños de 3 años y la ficha, ¿qué recomendación es más completa?", "Elegir el diseño 2, porque cuesta menos que $6.000 y no lleva botones, pero completar su ficha antes de producir", "Elegir el diseño 1, porque es el único con ficha completa, aunque supere el presupuesto", "Elegir el diseño 2 y producir ya, porque la ficha se completa después", "El diseño 1 cuesta 6.900 y supera 6.000; el 2 cumple presupuesto y seguridad, pero su ficha debe completarse."),
    ],
    ctx=("abc", "{F} Una profesora pregunta por qué se eligió el diseño 2 y no el 1. ¿Qué respuesta deja mejor respaldada la decisión?", "Los costos calculados por delantal, el presupuesto de $6.000, la ausencia de botones y el compromiso de completar la ficha", "Que al taller le pareció más bonito", "Que el diseño 2 es el más rápido de coser, sin dar más datos", "Una decisión respaldada cita cálculos, criterios de seguridad y el estado de la ficha."),
    sc=[
        ("En Vestuario y Confección Textil: ¿cuántos campos tiene una ficha técnica completa?", "Ocho", "Son modelo, talla, tela, color, medidas, insumos, versión y responsable."),
        ("¿Por qué se evitan los botones en prendas para niños pequeños?", "Porque pueden soltarse y llevarse a la boca", "Una pieza pequeña suelta es un riesgo."),
        ("¿Qué debe quedar registrado al elegir una alternativa?", "Los cálculos y el motivo de la alternativa descartada", "Así otra persona puede revisar la decisión."),
    ],
    op=("Comparación de ejemplo para un bolso. Diseño P: materiales $3.000; 20 minutos a $50 el minuto; ficha con 8 campos; cierre metálico pequeño. Diseño Q: materiales $2.600; 18 minutos a $50 el minuto; ficha con 7 campos; cierre metálico pequeño. Presupuesto máximo: $4.200 por bolso. "
        "Escribe: (a) el costo total de cada diseño, (b) cuál cumple el presupuesto, (c) qué falta antes de producir el diseño elegido y (d) cómo dejarías registrada la decisión.",
        "(a) P: 3.000 + 20 × 50 = 4.000. Q: 2.600 + 18 × 50 = 3.500. (b) Los dos cumplen $4.200. (c) Si se elige Q, falta completar un campo de la ficha; P ya está completa. (d) Anotando los costos, el presupuesto, el estado de la ficha, el diseño elegido y el motivo de descartar el otro.",
        ["calcula los costos totales", "compara con el presupuesto", "reconoce el campo que falta", "propone un registro de la decisión"],
        ["hoja con los cuatro puntos"],
        ["comparar solo los materiales", "olvidar la mano de obra", "no registrar el motivo"],
        "Pregunta: «¿puede producirse el diseño Q ya?». Debe responder que no, hasta completar el campo faltante."),
    reinforce="Inventa dos diseños de una prenda con costos y campos de ficha, y decide cuál se puede producir primero.",
    extend="Explica con un ejemplo inventado por qué un tiempo de confección debe tener un registro.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 6 (sala de moldería de ejemplo, inventada). La moldería transforma la ficha técnica en moldes: piezas de papel, de cartulina o archivos digitales con la forma y las medidas de cada parte de la prenda. "
     "El patronista traza el molde base (molde de una talla de referencia, sin detalles de diseño) y lo transforma según el modelo. Cada molde lleva: nombre de la pieza, talla, cantidad de piezas, sentido del hilo (flecha que indica la dirección de los hilos de la tela), "
     "margen de costura (ancho adicional para unir piezas) y piquetes (marcas de referencia). Reglas generales: el molde se trabaja con la ficha técnica a la vista; se guarda identificado con modelo, talla y versión; se trabaja sentado con buena postura y pausas; las tijeras y los cortes son de personal capacitado.")
build(
    O2, 1, F,
    use="Aprenderé a situar la moldería en el taller: qué es un molde, qué datos lleva, quién lo traza y qué riesgos y reglas hay.",
    prior=["Conozco la ficha técnica y sus medidas.", "Sé sumar y multiplicar medidas.", "Sé que cada talla tiene medidas distintas."],
    explain=[
        "En Vestuario y Confección Textil, un molde es una pieza de papel, cartulina o un archivo digital que reproduce la forma y las medidas de una parte de la prenda, como la espalda, la manga o el cuello. Los moldes se hacen a partir de la ficha técnica, de forma manual con lápiz y regla, o digital con un programa de moldería. El molde base es el de una talla de referencia sin detalles de diseño; de él se obtienen los moldes del modelo.",
        "Cada molde lleva datos obligatorios: el nombre de la pieza, la talla, cuántas piezas se necesitan, el sentido del hilo, el margen de costura y los piquetes. El sentido del hilo es una flecha que indica la dirección de los hilos de la tela; el margen de costura es el ancho adicional alrededor de la pieza para poder unirla a otra; los piquetes son marcas de referencia que ayudan a emparejar las piezas.",
        "Los riesgos de esta etapa son identificar mal los moldes y usar uno de otra talla o versión, y la fatiga por trabajar inclinado; para eso se rotulan los moldes, se ajusta la altura de la mesa y se hacen pausas. Las tijeras y cualquier herramienta de corte son solo para personal capacitado." + LIM,
    ],
    vocab=[("molde", "pieza de papel, cartulina o archivo digital con la forma y medidas de una parte de la prenda"), ("molde base", "molde de una talla de referencia sin detalles de diseño"), ("sentido del hilo", "flecha que indica la dirección de los hilos de la tela"), ("margen de costura", "ancho adicional alrededor de la pieza para unirla a otra"), ("piquete", "marca de referencia para emparejar piezas")],
    worked=[
        ("Ancho con margen", "Una pieza de ejemplo mide 25 cm de ancho sin margen y lleva 2 cm de margen de costura a cada lado. ¿Cuánto mide el molde?", ["Hay margen en los dos lados: 2 × 2 = 4.", "25 + 4 = 29."], "29 cm"),
        ("Identificar un dato", "Un molde tiene una flecha larga dibujada en la pieza. ¿Qué indica?", ["Es una flecha que sigue la dirección de los hilos de la tela.", "Eso es el sentido del hilo."], "El sentido del hilo"),
    ],
    mistakes=[("Guardar un molde sin escribir su talla ni su versión.", "Después nadie sabe a qué modelo pertenece y se puede usar el equivocado.", "Rotula cada molde con modelo, talla y versión."),
              ("Trabajar horas inclinado sobre una mesa demasiado baja.", "Esa postura produce dolor de espalda y fatiga.", "Ajusta la altura de la mesa y haz pausas.")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué es un molde?", "Una pieza de papel o archivo digital con la forma y medidas de una parte de la prenda", "Un dibujo de la prenda sobre una figura humana", "Una lista de los insumos que hay en bodega", "El molde reproduce una parte de la prenda; el figurín es el dibujo del diseño."),
        ("abc", "{F} ¿Qué indica la flecha que lleva el molde?", "La dirección de los hilos de la tela", "La talla de la pieza", "La cantidad de piezas que se necesitan", "La flecha es el sentido del hilo; la talla y la cantidad se anotan aparte."),
        ("abc", "{F} ¿Qué es el margen de costura?", "El ancho adicional alrededor de la pieza para poder unirla a otra", "La medida final de la prenda terminada", "La marca que ayuda a emparejar piezas", "El margen es un ancho extra; la marca de referencia es el piquete."),
        ("abc", "{F} ¿Quién traza el molde base?", "El patronista", "El jefe de producción", "El encargado de calidad", "La ficha asigna el molde base al patronista."),
        ("abc", "En Vestuario y Confección Textil: ¿por qué se guardan los moldes con modelo, talla y versión?", "Para evitar usar un molde equivocado", "Para que ocupen menos espacio", "Para que el cliente los pueda ver", "Un molde rotulado se reconoce y no se confunde con otro."),
        ("abc", "{F} ¿Qué es el molde base?", "El molde de una talla de referencia, sin detalles de diseño", "El molde de la talla más grande", "El molde de la prenda ya terminada", "Es la base de la que se obtienen los moldes de cada modelo."),
        ("=", "Un modelo de ejemplo tiene 6 piezas de molde y se produce en 4 tallas; cada talla tiene su juego completo. ¿Cuántos moldes hay que guardar?", "6*4", "Se multiplican las piezas de un juego por la cantidad de tallas.", " moldes"),
        ("abc", "{F} Aparece un molde sin talla ni versión escritas. ¿Qué corresponde?", "No usarlo hasta consultar al patronista y rotularlo", "Usarlo, porque la forma se reconoce a simple vista", "Escribir la talla que parece más probable", "Un molde sin identificar puede ser de otra talla o versión."),
        ("abc", "El taller guarda sus moldes digitales siempre con el nombre «final», sobrescribiendo el anterior. ¿Cuál es el riesgo principal?", "Se pierde la versión anterior y no se sabe cuál es la vigente", "El archivo ocupa menos memoria", "La ficha técnica cambia sola", "Sin nombres con modelo, talla y versión no se puede distinguir cuál archivo vale."),
        ("abc", "Un compañero dice que el margen de costura no importa porque «da lo mismo». ¿Qué consecuencia tendría ignorarlo?", "La prenda terminada podría quedar más chica que lo pedido en la ficha", "La prenda quedaría de otro color", "La etiqueta cambiaría de talla", "El margen se pierde al unir las piezas; sin considerarlo, la prenda sale menor."),
        ("abc", "La patronista pasa horas inclinada sobre una mesa baja y siente dolor de espalda. ¿Qué medida general corresponde?", "Ajustar la altura de la mesa y hacer pausas", "Trabajar más rápido para terminar antes", "Trazar los moldes en el suelo", "La postura y las pausas previenen la fatiga y el dolor."),
        ("=", "Una pieza de ejemplo mide 40 cm de ancho sin margen y lleva 1 cm de margen de costura a cada lado. ¿Cuánto mide el molde de ancho?", "40+1*2", "Hay margen a ambos lados, así que se suma dos veces.", " cm"),
        ("abc", "Existen los archivos «PE-14_M_v1» y «PE-14_M_v2», y la ficha vigente es la versión 2. El corte usa la versión 1 por costumbre. ¿Qué debería hacer el taller?", "Marcar la v1 como obsoleta y avisar que debe usarse la v2", "Dejar ambos archivos sin cambios, porque se reconocen", "Borrar la v2, porque la v1 ya se probó", "Dos versiones activas generan errores; hay que retirar la antigua y comunicar la vigente."),
    ],
    ctx=("abc", "{F} La ficha de un modelo cambia de versión y el patronista debe actualizar los moldes. ¿Qué es lo más seguro respecto de los moldes antiguos?", "Rotularlos como obsoletos y guardar solo los vigentes a la mano", "Dejarlos mezclados con los nuevos para consultarlos", "Usarlos igual mientras no se acaben", "Marcar lo obsoleto evita que se use por error."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué indica el sentido del hilo?", "La dirección de los hilos de la tela", "Es la flecha del molde y orienta cómo se ubica la pieza."),
        ("¿Para qué sirve el margen de costura?", "Para unir las piezas", "Es el ancho adicional que permite coser una pieza con otra."),
        ("¿Qué datos debe llevar rotulado cada molde?", "Modelo, talla y versión", "Así se identifica y no se confunde con otro."),
    ],
    op=("Un taller de ejemplo recibe un molde sin rótulo, con la forma de una manga y un margen de costura de 1 cm. Escribe: (a) tres datos que deberían estar escritos en el molde, (b) a quién consultarías para identificarlo y (c) una regla para evitar que se repita el problema.",
        "(a) Nombre de la pieza, talla, versión del modelo (también la cantidad de piezas). (b) Al patronista. (c) Rotular cada molde con modelo, talla y versión al guardarlo.",
        ["nombra tres datos del molde", "indica al patronista", "propone una regla de orden"],
        ["hoja con las tres respuestas"],
        ["decir que la forma basta para identificarlo", "usar el molde sin consultar", "no proponer ninguna regla"],
        "Pregunta: «¿qué puede pasar si se usa un molde de otra talla?». Debe responder que la prenda sale con medidas distintas a la ficha."),
    reinforce="Haz una lista de seis datos que lleva un molde y explica con una frase qué indica cada uno.",
    extend="Explica con un ejemplo inventado cómo se puede confundir un molde si no está rotulado.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 7 (tabla de medidas de ejemplo, inventada), en cm. Tabla de medidas corporales de un maniquí de ejemplo: talla S: busto 88, cintura 70, cadera 94; talla M: busto 92, cintura 74, cadera 98; talla L: busto 96, cintura 78, cadera 102. "
     "Holgura de ejemplo para una blusa: 8 cm en el busto (espacio extra para que la prenda quede cómoda y permita moverse). Gradación: obtener el molde de otra talla a partir del molde de una talla, aplicando aumentos o disminuciones fijos entre tallas. "
     "La ficha técnica indica las medidas de la prenda terminada; la tabla de medidas corporales indica las del cuerpo.")
build(
    O2, 2, F,
    use="Aprenderé los documentos y conceptos de la moldería: tabla de medidas, holgura, gradación y transformación del molde, y qué documento usa cada rol.",
    prior=["Conozco el molde y sus datos.", "Sé sumar y restar medidas.", "Sé diferenciar medida del cuerpo y medida de la prenda."],
    explain=[
        "La tabla de medidas corporales reúne las medidas del cuerpo por talla, como busto, cintura y cadera. La ficha técnica, en cambio, indica las medidas de la prenda terminada. La holgura es la diferencia entre la medida del cuerpo y la de la prenda: es el espacio extra que permite moverse y se suma a la medida corporal. Por ejemplo, el contorno de busto de una blusa es la medida corporal más la holgura.",
        "La gradación consiste en obtener el molde de otra talla a partir del molde de una talla de referencia, aplicando aumentos o disminuciones fijos entre tallas. Esos incrementos están en una tabla de gradación y pueden ser distintos para cada medida. La transformación del molde es otra operación: se modifica el molde base para obtener un modelo nuevo, por ejemplo cambiando el cuello o añadiendo un bolsillo.",
        "El patronista trabaja con la ficha técnica, la tabla de medidas y la tabla de gradación, ya sea en papel o en un programa. Cuando dos documentos entregan valores distintos, se consulta cuál es el vigente y aprobado; no se escoge uno al azar. Todo queda registrado con su versión." + LIM,
    ],
    vocab=[("tabla de medidas corporales", "medidas del cuerpo por talla"), ("holgura", "espacio extra entre el cuerpo y la prenda, que permite moverse"), ("gradación", "obtener el molde de otra talla aplicando aumentos o disminuciones fijos"), ("transformación del molde", "modificar el molde base para obtener un modelo nuevo"), ("contorno de prenda", "medida alrededor de la prenda terminada")],
    worked=[
        ("Contorno con holgura", "El busto de una talla de ejemplo mide 90 cm y la holgura de una blusa es de 6 cm. ¿Cuánto mide el contorno de busto de la blusa?", ["La holgura se suma a la medida del cuerpo.", "90 + 6 = 96."], "96 cm"),
        ("Elegir el documento", "El patronista quiere saber cuánto mide el pecho del cuerpo de la talla de referencia. ¿Qué documento mira?", ["Pregunta por una medida del cuerpo, no de la prenda.", "Eso está en la tabla de medidas corporales."], "La tabla de medidas corporales"),
    ],
    mistakes=[("Usar como medida de la prenda directamente la medida del cuerpo, sin holgura.", "La prenda quedaría pegada al cuerpo y sin permitir moverse.", "Suma la holgura que indica la ficha."),
              ("Confundir la gradación con la transformación del molde.", "La gradación cambia de talla; la transformación cambia el modelo.", "Pregunta qué cambia: ¿la talla o el diseño?")],
    T=[
        ("abc", "En Vestuario y Confección Textil: ¿qué es la holgura?", "El espacio extra entre el cuerpo y la prenda que permite moverse", "La marca de referencia que empareja piezas", "El aumento de un molde entre tallas", "La holgura se suma a la medida del cuerpo; la gradación es el cambio de talla."),
        ("abc", "{F} ¿Qué talla tiene una cintura de 74 cm?", "La talla M", "La talla S", "La talla L", "La tabla asigna 74 cm de cintura a la talla M."),
        ("=", "{F} ¿Cuántos cm más de cadera tiene la talla L que la talla S?", "102-94", "Se resta la cadera de S a la de L.", " cm"),
        ("=", "{F} ¿Cuánto mide el contorno de busto de una blusa talla M, con la holgura de la ficha?", "92+8", "A la medida del cuerpo se le suma la holgura.", " cm"),
        ("abc", "En Vestuario y Confección Textil: ¿qué es la gradación?", "Obtener el molde de otra talla aplicando aumentos o disminuciones fijos", "Cambiar el cuello del molde para hacer un modelo nuevo", "Pasar el molde de papel a un archivo digital", "La gradación cambia de talla; transformar el molde cambia el modelo."),
        ("abc", "En Vestuario y Confección Textil: ¿qué es transformar un molde?", "Modificar el molde base para obtener un modelo nuevo, como cambiar el cuello", "Obtener el molde de la talla siguiente", "Escribir la talla en el molde", "Transformar cambia el diseño; cambiar de talla es gradación."),
        ("=", "{F} En la tabla, el busto aumenta lo mismo entre tallas consecutivas. Si sigue igual, ¿cuánto mediría el busto de una talla XL?", "96+(96-92)", "El aumento entre tallas es 4 cm, y se suma al busto de la talla L.", " cm"),
        ("abc", "{F} El patronista necesita las medidas finales de la prenda terminada. ¿Qué documento usa?", "La ficha técnica", "La tabla de medidas corporales", "La tabla de tallas del cliente", "La ficha indica la prenda terminada; la tabla corporal indica el cuerpo."),
        ("abc", "{F} El diseñador pide una blusa con otro cuello, pero con las mismas medidas y la misma talla. ¿Qué operación del patronista corresponde?", "Transformar el molde base", "Graduar el molde a otra talla", "Cambiar la tabla de medidas corporales", "Se cambia el diseño del molde, no la talla."),
        ("abc", "Dos patronistas aplican holguras distintas de 6 y 10 cm a la misma blusa. ¿Cómo se evita esa diferencia?", "Registrando la holgura en la ficha técnica", "Dejando que cada patronista decida", "Usando siempre la mayor", "Si la ficha trae la holgura, ambos aplican el mismo valor."),
        ("abc", "Una blusa se diseña con una holgura demasiado pequeña. ¿Cuál es la consecuencia más probable?", "La prenda queda incómoda y limita el movimiento", "La prenda cambia de color", "La ficha cambia de versión", "Poco espacio extra impide moverse con comodidad."),
        ("=", "Tabla de ejemplo: la cintura de la talla S es 70 cm, la de M es 74 y la de L es 78. Una falda holgada lleva 10 cm de holgura en la cintura. ¿Cuánto mide el contorno de cintura de la falda talla L?", "78+10", "A la cintura corporal de L se le suma la holgura.", " cm"),
        ("abc", "En un archivo digital, el busto de la talla M dice 92, y en la tabla impresa dice 94. ¿Qué corresponde?", "Consultar cuál versión está vigente y aprobada antes de trazar", "Usar el valor mayor para estar seguro", "Promediar los dos valores", "Cuando los documentos difieren, se confirma el vigente y no se elige al azar."),
    ],
    ctx=("=", "{F} Una blusa talla S lleva la holgura de busto de la ficha. ¿Cuánto mide el contorno de busto de la prenda?", "88+8", "A la medida corporal de S se le suma la holgura.", " cm"),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué diferencia hay entre gradación y transformación?", "La gradación cambia la talla y la transformación cambia el modelo", "Una actúa sobre la talla y la otra sobre el diseño."),
        ("¿Cómo se obtiene el contorno de una prenda holgada?", "Sumando la holgura a la medida del cuerpo", "La holgura es espacio extra que se suma al cuerpo."),
        ("¿Qué se hace si dos documentos dan medidas distintas?", "Confirmar cuál es el vigente y aprobado", "No se escoge uno al azar."),
    ],
    op=("Tabla de ejemplo (cm): talla S: busto 84, cintura 66; talla M: busto 88, cintura 70. Una blusa lleva 7 cm de holgura en el busto y una falda lleva 6 cm de holgura en la cintura. "
        "Escribe: (a) el contorno de busto de la blusa en talla M, (b) el contorno de cintura de la falda en talla S y (c) qué documento usarías para saber las medidas finales de una prenda terminada.",
        "(a) 88 + 7 = 95 cm. (b) 66 + 6 = 72 cm. (c) La ficha técnica de la prenda.",
        ["suma la holgura a la medida correcta", "escoge la talla indicada", "nombra la ficha técnica"],
        ["hoja con los tres puntos"],
        ["usar la talla equivocada", "olvidar sumar la holgura", "indicar la tabla corporal para la prenda terminada"],
        "Pregunta: «¿la holgura va en la tabla corporal o en la prenda?». Debe responder que se suma en la prenda."),
    reinforce="Con una tabla inventada de tres tallas, calcula el contorno de una prenda para cada talla con una holgura dada.",
    extend="Explica con un ejemplo inventado por qué una prenda necesita holgura.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 8 (revisión de moldes de ejemplo, inventada). Blusa BL-3, talla M. Tolerancia de ejemplo para moldes: diferencia máxima permitida de 1 cm entre la ficha y el molde. Margen de costura: 1 cm en la ficha y en los moldes. "
     "Medida | Ficha (prenda terminada) | Molde entregado, sin margen: ancho plano de pecho | 56 | 54; largo total | 62 | 62; largo de manga | 18 | 20; ancho de hombros | 40 | 40. "
     "La revisión compara las medidas del molde sin margen con las de la ficha, que son de la prenda terminada.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso en papel: comparar los moldes entregados con la ficha técnica, usar una tolerancia y decidir qué se devuelve al patronista.",
    prior=["Conozco el molde y el margen de costura.", "Sé restar medidas.", "Sé comparar una diferencia con un máximo."],
    explain=[
        "Revisar un molde consiste en comparar sus medidas con las de la ficha técnica. La ficha da las medidas de la prenda terminada, por eso se comparan con las del molde sin el margen de costura, porque el margen se pierde al unir las piezas y no forma parte de la medida terminada. Si se comparara con el margen incluido, un molde chico podría parecer correcto.",
        "La tolerancia es la diferencia máxima permitida entre la medida pedida y la medida real. Si la diferencia es igual o menor que la tolerancia, la medida cumple; si es mayor, no cumple. Los valores de tolerancia los fija el taller según la ficha y la norma o el cliente; en este cuaderno son de ejemplo.",
        "Cuando un molde no cumple, no lo corrige quien lo revisa: se devuelve al patronista con la medida que falla, la diferencia y la versión. Cambiar una medida de la ficha por considerarla mejor exige la aprobación de la diseñadora y una nueva versión. La revisión se registra con las medidas, las diferencias, la decisión y quién la hizo." + LIM,
    ],
    vocab=[("tolerancia", "diferencia máxima permitida entre la medida pedida y la real"), ("cumple", "la diferencia es igual o menor que la tolerancia"), ("devolver al patronista", "enviar el molde con la medida que falla para que lo corrija"), ("revisión de moldes", "comparación de las medidas del molde con las de la ficha"), ("medida terminada", "medida de la prenda ya unida, sin el margen de costura")],
    worked=[
        ("Aplicar la tolerancia", "En una revisión de ejemplo la ficha pide 30 cm y el molde mide 31 cm, con tolerancia de 1 cm. ¿Cumple?", ["La diferencia es 31 − 30 = 1 cm.", "1 es igual a la tolerancia, así que cumple."], "Cumple"),
        ("Por qué no se suma el margen", "Un molde sin margen mide 20 cm de largo, la ficha pide 22 y el margen es de 1 cm por lado. Un compañero suma el margen (22) y dice que cumple. ¿Es correcto?", ["La ficha mide la prenda terminada, donde el margen ya no existe.", "El molde sin margen es de 20 cm y falta 2 cm."], "No, el molde no cumple"),
    ],
    mistakes=[("Sumar el margen de costura para que la medida del molde parezca coincidir con la ficha.", "La medida terminada no incluye el margen.", "Compara el molde sin margen con la ficha."),
              ("Corregir el molde con lápiz uno mismo, sin avisar al patronista.", "Se pierde el registro del cambio y de la versión.", "Devuelve el molde con la medida que falla.")],
    T=[
        ("abc", "{F} ¿Cuáles medidas del molde no coinciden con la ficha?", "El ancho de pecho y el largo de manga", "El largo total y el ancho de hombros", "El ancho de pecho y el largo total", "Pecho: 54 contra 56 y manga: 20 contra 18; las otras dos medidas coinciden."),
        ("=", "{F} ¿Cuántos cm menos que lo pedido mide el ancho de pecho del molde?", "56-54", "Se resta la medida del molde a la medida de la ficha.", " cm"),
        ("abc", "{F} El largo de manga del molde, ¿es más largo o más corto que la ficha?", "Es más largo, por 2 cm", "Es más corto, por 2 cm", "Es igual", "El molde mide 20 y la ficha pide 18."),
        ("=", "{F} Si al ancho de pecho del molde se le suma el margen de ambos lados, ¿qué valor resulta?", "54+1*2", "Se suma el margen de 1 cm dos veces al ancho del molde.", " cm"),
        ("abc", "{F} ¿Qué medida del molde se compara con la ficha técnica?", "La medida sin el margen de costura", "La medida con el margen de costura", "La mitad de la medida", "La ficha mide la prenda terminada, donde ya no está el margen."),
        ("abc", "{F} El molde de pecho, con la tolerancia indicada, ¿cumple?", "No cumple, porque la diferencia de 2 cm supera la tolerancia de 1 cm", "Cumple, porque la diferencia es pequeña", "Cumple, porque se acerca a lo pedido", "La diferencia 2 es mayor que la tolerancia 1, así que no cumple."),
        ("abc", "{F} Si el largo total del molde midiera 63 cm en lugar de 62, ¿cumpliría?", "Cumpliría, porque la diferencia de 1 cm no supera la tolerancia", "No cumpliría, porque no es igual a 62", "No cumpliría, porque la tolerancia solo vale para el pecho", "Una diferencia igual a la tolerancia todavía cumple."),
        ("=", "{F} ¿Cuál es el ancho de pecho mínimo del molde que todavía cumple con la tolerancia?", "56-1", "Se resta la tolerancia a la medida que pide la ficha.", " cm"),
        ("abc", "{F} Tras la revisión, ¿qué debe hacerse con este molde?", "Devolverlo al patronista indicando las medidas que fallan", "Aprobarlo porque dos medidas coinciden", "Corregirlo quien lo revisó", "Un molde con medidas fuera de tolerancia se devuelve a quien lo trazó."),
        ("abc", "{F} Un compañero suma el margen al pecho (54 + 2 = 56) y dice que coincide con la ficha. ¿Por qué se equivoca?", "Porque la ficha mide la prenda terminada y el margen no forma parte de ella", "Porque el margen es de 2 cm y no de 1", "Porque el pecho del molde mide 56", "Con el margen incluido, un molde chico parece correcto sin serlo."),
        ("abc", "El patronista dice: «la manga de 20 cm queda mejor que la de 18 de la ficha, así que la dejo». ¿Qué corresponde?", "Pedir a la diseñadora que cambie la ficha con una nueva versión, o devolver el molde para corregirlo", "Dejar la manga como está", "Cambiar la ficha sin avisar", "La ficha solo cambia con la aprobación de la diseñadora y una versión nueva."),
        ("abc", "Se corrige el molde de pecho para que mida 56, pero no se actualiza la versión del archivo. ¿Cuál es el riesgo?", "Que se siga usando el archivo anterior sin darse cuenta", "Que cambie la ficha técnica", "Que la tolerancia aumente", "Sin versión nueva no se distingue el molde corregido del anterior."),
        ("abc", "Se revisan tres moldes de una falda de ejemplo. La ficha pide largo 58 cm con tolerancia de 1 cm; los moldes miden 57, 60 y 58 cm. ¿Cuántos cumplen?", "Dos, los de 57 y 58 cm", "Solo uno, el de 58 cm", "Los tres", "57 difiere en 1 y 58 en 0, ambos dentro de la tolerancia; 60 difiere en 2."),
    ],
    ctx=("abc", "{F} El patronista pide revisar de nuevo después de corregir el molde y entrega el pecho en 55 cm. ¿Qué decisión corresponde con la tolerancia de la ficha?", "Cumple, porque difiere en 1 cm de la ficha", "No cumple, porque no mide 56", "No se puede decidir sin el margen", "La diferencia de 1 cm es igual a la tolerancia."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué es la tolerancia?", "La diferencia máxima permitida entre la medida pedida y la real", "Define hasta dónde una medida todavía cumple."),
        ("¿Qué se compara con la ficha, el molde con margen o sin margen?", "Sin margen", "La ficha mide la prenda terminada."),
        ("¿Qué se hace con un molde que no cumple?", "Se devuelve al patronista", "Quien lo trazó lo corrige y actualiza la versión."),
    ],
    op=("Revisión de ejemplo de una falda: tolerancia de 1 cm. Ficha: cintura 72, largo 58, ancho de bajo 100. Molde sin margen: cintura 70, largo 59, ancho de bajo 100. "
        "Escribe: (a) la diferencia de cada medida, (b) cuáles cumplen y cuáles no, (c) qué harías con el molde y (d) qué anotarías en el registro de revisión.",
        "(a) Cintura 2, largo 1, ancho de bajo 0. (b) Cumplen largo y ancho de bajo; la cintura no cumple. (c) Devolver el molde al patronista para corregir la cintura. (d) Las tres medidas, las diferencias, la decisión, la versión y quién revisó.",
        ["calcula las tres diferencias", "decide con la tolerancia", "devuelve el molde", "propone un registro completo"],
        ["hoja con las cuatro respuestas"],
        ["sumar el margen a la medida", "aprobar la cintura por estar cerca", "corregir el molde sin avisar"],
        "Pregunta: «¿la diferencia de 1 cm cumple o no?». Debe responder que sí, porque es igual a la tolerancia."),
    reinforce="Inventa una tabla con tres medidas de ficha y de molde, y decide con una tolerancia de 1 cm cuáles cumplen.",
    extend="Explica con un ejemplo inventado por qué comparar con el margen incluido lleva a errores.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 9 (tabla de gradación de ejemplo, inventada). Polera PE-20, talla base M, medidas del molde sin margen, en cm: ancho plano de pecho 50, largo total 64, largo de manga 19, ancho de hombros 38. "
     "Incrementos de ejemplo entre tallas consecutivas (S, M, L, XL): ancho plano +2, largo total +2, largo de manga +1, ancho de hombros +1. Hacia la talla menor, las mismas medidas disminuyen. Tolerancia de ejemplo: 1 cm.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar una tabla de gradación para obtener las medidas de otras tallas y a verificar si un molde cumple con la tolerancia.",
    prior=["Conozco la gradación y la tolerancia.", "Sé sumar y restar medidas.", "Sé que cada medida cambia distinto entre tallas."],
    explain=[
        "Para graduar se parte de la talla base, que es la talla de referencia, y se aplican los incrementos de la tabla de gradación por cada talla que se avanza. Hacia una talla mayor se suma el incremento y hacia una talla menor se resta. Por ejemplo, si el ancho plano sube 2 cm por talla, dos tallas más arriba el ancho sube 4 cm. Cada medida tiene su propio incremento, porque el cuerpo no crece igual en todas partes.",
        "Por eso no se escala todo con el mismo porcentaje: se usan incrementos distintos para cada medida. Tampoco se usa la misma tabla para niños y adultos, porque sus proporciones son distintas; hay tablas por grupo de edad. Un programa digital puede graduar automáticamente, pero debe verificarse comparando sus resultados con la tabla.",
        "Después de graduar, cada molde se revisa con la tolerancia: la diferencia entre la medida calculada y la del molde no debe superarla. Los resultados se registran por talla, y un juego de moldes graduado se identifica con modelo, talla y versión." + LIM,
    ],
    vocab=[("talla base", "talla de referencia desde la que se grada"), ("incremento", "aumento o disminución fijo de una medida entre tallas"), ("tabla de gradación", "lista de incrementos por medida entre tallas"), ("graduar", "obtener el molde de otra talla aplicando los incrementos"), ("medida calculada", "medida que resulta de aplicar los incrementos")],
    worked=[
        ("Graduar una medida", "En una tabla de ejemplo, la talla base M tiene un largo de 60 cm y el incremento es de +3 por talla. ¿Cuánto mide el largo de la talla L?", ["L está una talla sobre M.", "60 + 3 = 63."], "63 cm"),
        ("Graduar hacia abajo", "Con los mismos datos, ¿cuánto mide el largo de la talla S?", ["S está una talla bajo M, así que se resta.", "60 − 3 = 57."], "57 cm"),
    ],
    mistakes=[("Aumentar todas las medidas con el mismo número porque «es más fácil».", "Cada medida tiene un incremento propio según la tabla.", "Aplica el incremento de cada medida."),
              ("Aceptar el resultado de un programa sin compararlo con la tabla.", "Un error de configuración se reproduce en todas las tallas.", "Verifica los resultados contra la tabla de gradación.")],
    T=[
        ("=", "{F} ¿Cuánto mide el ancho plano de pecho de la talla L?", "50+2", "La talla L está una talla sobre la base y se suma el incremento.", " cm"),
        ("=", "{F} ¿Cuánto mide el largo total de la talla S?", "64-2", "S está una talla bajo la base y se resta el incremento.", " cm"),
        ("abc", "En Vestuario y Confección Textil: ¿qué es un incremento de gradación?", "El aumento o disminución fijo de una medida entre tallas consecutivas", "El margen de costura de la pieza", "La diferencia entre el cuerpo y la prenda", "El incremento es el cambio entre tallas; la diferencia con el cuerpo es la holgura."),
        ("=", "{F} ¿Cuánto mide el largo de manga de la talla XL?", "19+1*2", "De M a XL hay dos tallas, así que se suman dos incrementos.", " cm"),
        ("=", "{F} ¿Cuánto mide el ancho de hombros de la talla S?", "38-1", "Hacia la talla menor se resta el incremento.", " cm"),
        ("abc", "{F} ¿Por qué no se escalan todas las medidas con el mismo porcentaje?", "Porque cada medida tiene un incremento propio en la tabla de gradación", "Porque la ficha técnica lo prohíbe", "Porque el margen de costura cambia", "Las medidas del cuerpo no crecen igual, por eso cada una tiene su incremento."),
        ("=", "{F} ¿Cuántos cm más ancho es el pecho de la talla XL que el de la talla S?", "(50+2*2)-(50-2)", "Se resta el ancho de S al ancho de XL.", " cm"),
        ("abc", "{F} Un molde talla L tiene largo total de 67 cm. Con la tolerancia indicada, ¿cumple?", "Sí, porque el largo calculado es 66 y la diferencia es 1 cm", "No, porque debía medir 64", "No, porque la tolerancia no se aplica al largo", "El largo de L es 64 + 2 = 66; 67 difiere en 1, igual a la tolerancia."),
        ("abc", "{F} Un molde talla L tiene largo de manga de 22 cm. ¿Cumple con la tolerancia indicada?", "No, porque debería medir 20 y la diferencia de 2 cm supera la tolerancia", "Sí, porque se acerca a 19", "Sí, porque la manga no tiene tolerancia", "El largo de manga de L es 19 + 1 = 20; 22 difiere en 2."),
        ("abc", "El archivo digital graduado da una manga de 21 cm en la talla L, y la tabla indica otro valor. ¿Por qué es importante verificar aunque lo haya hecho un programa?", "Porque un error en la configuración del programa se repite en todas las tallas", "Porque el programa siempre graduó bien y solo hay que firmar", "Porque la tabla de gradación se ignora en los archivos digitales", "El software aplica lo que se configura; si el incremento está mal, todos los moldes salen mal."),
        ("abc", "Un taller usa la misma tabla de gradación para tallas infantiles y para adultos. ¿Cuál es el problema?", "Las proporciones de niños y adultos son distintas y requieren tablas por grupo", "Que la talla base de los niños no admite incrementos", "Que la tabla de adultos no tiene tolerancia", "Cada grupo de edad tiene proporciones propias y su propia tabla."),
        ("=", "Un revisor mide 3 moldes por talla, y cada molde en 4 medidas, en las 4 tallas del pedido. ¿Cuántas mediciones hace en total?", "4*3*4", "Se multiplican tallas, moldes por talla y medidas por molde.", " mediciones"),
        ("abc", "Un cliente pide una polera cuyo ancho plano sea 52 cm. Con la tabla de la ficha y su talla base, ¿qué talla le corresponde?", "La talla L", "La talla M", "La talla XL", "L tiene 50 + 2 = 52 cm de ancho plano."),
    ],
    ctx=("abc", "{F} Un colegio pide poleras en tallas S, M, L y XL, y el taller solo tiene el molde de la talla M. ¿Qué documento permite obtener los otros moldes?", "La tabla de gradación", "La carta de colores", "El muestrario de telas", "La tabla de gradación indica los incrementos para pasar de una talla a otra."),
    sc=[
        ("En Vestuario y Confección Textil: ¿qué se hace hacia una talla menor con un incremento?", "Se resta", "Hacia la talla menor las medidas disminuyen."),
        ("¿Por qué cada medida tiene su incremento?", "Porque el cuerpo no crece igual en todas las medidas", "Por eso no se usa el mismo porcentaje."),
        ("¿Qué se verifica después de graduar?", "Que la medida cumpla con la tolerancia", "La tolerancia permite decidir si el molde cumple."),
    ],
    op=("Datos de ejemplo: talla base M de una camisa con ancho plano de pecho 54 cm y largo de manga 62 cm. Incrementos entre tallas: ancho plano +2 y largo de manga +1. Escribe: (a) el ancho plano y el largo de manga de la talla L, (b) los de la talla S, (c) los de la talla XL y (d) qué harías para comprobar que un programa digital graduó bien.",
        "(a) L: 56 y 63. (b) S: 52 y 61. (c) XL: 58 y 64. (d) Comparar sus resultados con la tabla de gradación y con la tolerancia, antes de aprobar los moldes.",
        ["suma el incremento hacia arriba", "resta hacia abajo", "aplica dos incrementos para XL", "propone verificar con la tabla"],
        ["hoja con los cuatro puntos"],
        ["usar el mismo incremento para ambas medidas", "sumar en vez de restar para S", "aceptar el programa sin comprobar"],
        "Pregunta: «¿cuántos incrementos hay de M a XL?». Debe responder que dos."),
    reinforce="Con una tabla inventada de tres medidas y la talla base, calcula las medidas de las otras tallas.",
    extend="Explica con un ejemplo inventado por qué una tabla de gradación infantil no sirve para adultos.",
)
