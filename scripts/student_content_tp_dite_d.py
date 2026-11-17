"""Dibujo Técnico TP 3.º y 4.º medio: OAE-07 (representación 3D, como concepto y cálculo) y OAE-08 (impresión y reproducción de planos). Papel; sin software; datos de ejemplo."""
from __future__ import annotations

from tp_dite_common import build

O7 = "TP-DITE-3y4-OAE-07"
O8 = "TP-DITE-3y4-OAE-08"

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (pedido de ejemplo, inventado). El «Estudio Cordillera» necesita una representación tridimensional (con largo, ancho y alto) de una caseta de 4 m de largo, 3 m de ancho y 2,5 m de alto, "
     "para mostrársela a la mandante antes de construir. Entregables: imágenes generadas por el computador a partir del modelo (renders) y un video corto. "
     "Las texturas (imágenes que imitan materiales) se bajaron de un sitio cuya licencia permite solo uso personal. En el video aparecen, por casualidad, dos vecinos del barrio.")
build(
    O7, 1, F,
    use="Aprenderé para qué sirve un modelo 3D, qué etapas tiene su trabajo y qué cuidados de derechos de autor, privacidad y salud hay que tener.",
    prior=["Sé qué es una planta, una fachada y una sección.", "Sé calcular volúmenes de cajas.", "Sé qué es una escala."],
    explain=[
        "Un modelo 3D representa un objeto o una obra con sus tres dimensiones: largo, ancho y alto. Sirve para mostrar un proyecto antes de construirlo, revisar cómo se unen las partes y preparar maquetas. Un modelo digital no reemplaza a los planos: los planos siguen siendo los documentos con las medidas oficiales, y el modelo debe coincidir con ellos. Este cuaderno trabaja solo los conceptos y los cálculos en papel, sin software de modelado.",
        "El trabajo tiene etapas: modelar la forma, asignar materiales y texturas, configurar la iluminación y la cámara, generar imágenes o render (la imagen final calculada por el computador) y, si se pide, hacer una animación, que es una secuencia de imágenes que simula movimiento. Cada etapa puede tardar horas, y se avisa a la mandante el plazo real.",
        "Hay tres cuidados. Primero, los derechos de autor: texturas, modelos e imágenes descargadas tienen licencia, y se usan solo dentro de lo permitido. Segundo, la privacidad: no se publican imágenes donde se pueda reconocer a personas sin su permiso. Tercero, la salud: mirar pantallas muchas horas cansa los ojos y el cuello, por lo que se hacen pausas breves y se cuida la postura.",
    ],
    vocab=[("modelo 3D", "representación de un objeto con largo, ancho y alto"), ("render", "imagen final calculada por el computador a partir del modelo"), ("textura", "imagen que imita un material"), ("animación", "secuencia de imágenes que simula movimiento"), ("licencia", "permiso que fija cómo se puede usar una obra ajena"), ("privacidad", "derecho a que no se difundan datos o imágenes personales")],
    worked=[
        ("Calcular un volumen", "Un contenedor de ejemplo mide 6 m de largo, 2 m de ancho y 2 m de alto. ¿Cuántos m³ tiene?", ["Volumen = largo × ancho × alto.", "6 × 2 × 2 = 24 m³."], "24 m³"),
        ("Revisar una licencia", "Una textura de ejemplo dice «uso personal, no comercial». ¿Se puede usar en un render que se entrega a una mandante que pagará por el proyecto?", ["Entregar un trabajo pagado es un uso comercial.", "La licencia no lo permite."], "No: se necesita otra textura o autorización"),
    ],
    mistakes=[("Usar una imagen bajada de internet porque «todo el mundo lo hace».", "Las imágenes tienen autor y licencia; usarlas fuera de lo permitido infringe sus derechos.", "Revisa la licencia o crea la textura tú mismo."),
              ("Mostrar en un video el rostro de personas reales sin pedirles permiso.", "La imagen de una persona es un dato personal y requiere su autorización.", "Evita incluirlas o pídeles permiso.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un modelo 3D?", "Una representación de un objeto con largo, ancho y alto", "Una lista de materiales de la obra", "Un plano impreso en tres hojas", "El modelo 3D muestra las tres dimensiones del objeto."),
        ("abc", "¿Qué es un render?", "La imagen final que calcula el computador a partir del modelo", "El plano de planta", "La lista de precios", "El render es la imagen generada a partir del modelo, con luces y materiales."),
        ("abc", "En Dibujo Técnico: ¿qué es una textura?", "Una imagen que imita un material", "La forma básica de un objeto", "La luz de la escena", "La textura da apariencia de madera, ladrillo u otro material."),
        ("=", "{F} Expresado en metros, ¿cuántos m³ tiene la caseta?", "4*3*2.5", "El volumen es largo por ancho por alto.", " m³"),
        ("=", "{F} ¿Cuántos m² de superficie de piso tiene la caseta?", "4*3", "La superficie del piso es largo por ancho.", " m²"),
        ("abc", "{F} ¿Qué problema tiene el uso de las texturas descargadas?", "La licencia permite solo uso personal, y este es un trabajo para una mandante", "Ninguno, porque son solo imágenes", "Que pesan demasiado para el video", "El uso en un trabajo pagado excede el uso personal."),
        ("abc", "{F} ¿Qué haces con los dos vecinos que aparecen en el video?", "Los saco del video o pido su permiso antes de mostrarlo", "Los dejo, porque salieron por casualidad", "Les cambio el color de ropa", "La imagen de una persona reconocible requiere su permiso."),
        ("abc", "{F} Un modelo y el plano tienen medidas distintas. ¿Qué documento manda como oficial?", "El plano, y el modelo se corrige para que coincida", "El modelo, porque se ve mejor", "Ninguno: se promedian", "El modelo debe coincidir con los planos oficiales."),
        ("=", "{F} En una maqueta física de la caseta a escala 1:50, ¿cuántos centímetros mide el largo de 4 m?", "400//50", "El largo de 4 m son 400 cm y se dividen por 50.", " cm"),
        ("abc", "{F} El trabajo exige seis horas seguidas frente a la pantalla. ¿Cuál es la mejor práctica?", "Hacer pausas breves, ajustar la pantalla y la postura", "Seguir sin pausas para terminar antes", "Acercarse más a la pantalla para ver mejor", "Las pausas y la postura previenen cansancio visual y molestias."),
        ("abc", "{F} La mandante quiere compartir el video en redes sociales. ¿Qué verificas antes?", "Que las texturas tengan licencia y que no se vean personas sin permiso", "Que el video dure menos de un minuto", "Que el modelo tenga muchos colores", "Antes de publicar se verifican derechos de autor y privacidad."),
        ("=", "{F} Si la caseta tuviera una pared de 4 m de largo y 2,5 m de alto con una puerta de 1 m por 2 m, ¿cuántos m² de pared quedan sin contar la puerta?", "4*2.5-1*2", "Se resta la superficie de la puerta a la de la pared.", " m²"),
        ("abc", "{F} Un compañero propone entregar solo el video y no los planos, «porque el modelo es mejor». ¿Qué respondes?", "Que el modelo complementa los planos, pero no los reemplaza", "Que tiene razón, porque el video muestra todo", "Que los planos solo se entregan si los piden dos veces", "Los planos contienen las medidas oficiales y se entregan."),
    ],
    ctx=("abc", "Te piden terminar el render para mañana, pero el cálculo dice que se necesitan tres días. ¿Qué haces?", "Informo el plazo real y propongo alternativas", "Prometo entregar mañana y trabajo toda la noche", "Entrego un render incompleto sin avisar", "Se informa el plazo real, porque forzar el cumplimiento perjudica la calidad y la salud."),
    sc=[
        ("En Dibujo Técnico: ¿para qué sirve un render?", "Para mostrar una imagen realista del modelo", "Permite ver el proyecto antes de construirlo."),
        ("¿Qué pasa si una textura tiene licencia de uso personal?", "No se puede usar en un trabajo comercial", "Hay que respetar el permiso del autor."),
        ("¿Qué haces ante imágenes de personas reconocibles?", "Pido permiso o las evito", "Es un dato personal protegido por la privacidad de cada persona."),
    ],
    op=("Una oficina de ejemplo prepara el modelo 3D de una bodega de 10 m de largo, 6 m de ancho y 4 m de alto para una mandante. Calcula su volumen y la superficie del piso, y escribe tres cuidados que tendrías con las texturas, con las personas que aparezcan y con tu salud, y un aviso a la mandante sobre el plazo.",
        "Volumen: 10 × 6 × 4 = 240 m³. Piso: 10 × 6 = 60 m². Cuidados: revisar la licencia de cada textura; no mostrar personas reconocibles sin permiso; hacer pausas y cuidar la postura. Aviso: «El render final requiere X horas; propongo entregar el miércoles».",
        ["calcula volumen y superficie", "nombra los tres cuidados", "redacta un aviso de plazo claro"],
        ["hoja con cálculos y tres líneas"],
        ["olvidar la licencia", "no mencionar la privacidad", "prometer un plazo irreal"],
        "Pregunta: «¿por qué no usas esa textura gratis?». Si no responde, repasa la licencia."),
    reinforce="Elige un objeto de tu casa, mide su largo, ancho y alto y calcula su volumen aproximado.",
    extend="Explica con un ejemplo inventado por qué un modelo 3D no reemplaza a los planos.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (modelo de ejemplo). Un cubo tiene 8 vértices (puntos de esquina), 12 aristas (líneas entre vértices) y 6 caras (superficies planas). "
     "Mesa de ejemplo modelada con formas básicas llamadas primitivas: un tablero (caja de 120 cm de largo, 60 cm de ancho y 4 cm de espesor) y 4 patas (cajas de 5 cm por 5 cm por 70 cm). "
     "Ejes: x = largo, y = ancho, z = alto. El vértice inferior izquierdo del tablero está en (0, 0, 70). Una animación de ejemplo muestra la mesa girando 360 grados en 10 segundos.")
build(
    O7, 2, F,
    use="Aprenderé los elementos de un modelo 3D (vértices, aristas, caras, primitivas, coordenadas), la diferencia entre vistas y los conceptos de textura, luz, cámara y animación.",
    prior=["Sé calcular volúmenes de cajas.", "Sé qué es un render.", "Sé usar coordenadas simples."],
    explain=[
        "Un modelo 3D se construye con puntos y superficies. Un vértice es un punto de esquina; una arista es la línea entre dos vértices; una cara es una superficie plana limitada por aristas. Las primitivas son formas básicas, como cajas, cilindros y esferas, que se combinan para formar objetos más complejos. Un cubo tiene 8 vértices, 12 aristas y 6 caras.",
        "Cada punto se ubica con tres coordenadas (x, y, z), por ejemplo largo, ancho y alto. A la forma se le asignan material y textura, se agregan luces, que crean zonas iluminadas y sombras, y se ubica una cámara que define desde dónde se mira. Dos tipos de vista son la isométrica, que no achica los objetos lejanos y conserva las medidas en los ejes, y la perspectiva, que los achica como la vista humana y se parece a una fotografía.",
        "Una animación es una secuencia de imágenes llamadas fotogramas, mostradas rápido. La cantidad de fotogramas por segundo se abrevia fps. Para calcular los fotogramas se multiplican los segundos por los fps. Los datos de ejemplo de esta ficha no pretenden ser normas.",
    ],
    vocab=[("vértice", "punto de esquina"), ("arista", "línea entre dos vértices"), ("cara", "superficie plana limitada por aristas"), ("primitiva", "forma básica como caja, cilindro o esfera"), ("coordenadas", "tres números que ubican un punto en el espacio"), ("fotograma", "cada imagen de una animación"), ("fps", "fotogramas por segundo")],
    worked=[
        ("Volumen de una caja", "Una caja de ejemplo mide 30 cm por 20 cm por 10 cm. ¿Cuántos cm³ tiene?", ["Volumen = largo × ancho × alto.", "30 × 20 × 10 = 6.000 cm³."], "6.000 cm³"),
        ("Contar fotogramas", "Una animación de ejemplo dura 5 segundos a 24 fps. ¿Cuántos fotogramas tiene?", ["Fotogramas = segundos × fps.", "5 × 24 = 120."], "120 fotogramas"),
    ],
    mistakes=[("Creer que la perspectiva conserva las medidas en todas partes.", "En la perspectiva los objetos lejanos se ven más pequeños; la vista isométrica sí conserva las medidas sobre los ejes.", "Usa isométrica para medir y perspectiva para mostrar."),
              ("Confundir una arista con una cara.", "La arista es una línea; la cara es una superficie.", "Cuenta líneas para las aristas y superficies para las caras.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un vértice?", "Un punto de esquina del modelo", "Una superficie plana", "Una imagen de la animación", "El vértice es el punto donde se unen las aristas."),
        ("abc", "¿Cuántas caras tiene un cubo?", "6", "8", "12", "El cubo tiene 6 caras; 8 son los vértices y 12 las aristas."),
        ("abc", "¿Qué es una primitiva?", "Una forma básica como una caja o un cilindro", "Una textura de madera", "Un plano de fachada", "Las primitivas se combinan para formar objetos."),
        ("=", "{F} ¿Cuántos cm³ tiene el tablero de la mesa?", "120*60*4", "El volumen es largo por ancho por espesor.", " cm³"),
        ("=", "{F} ¿Cuántos cm³ tienen las 4 patas juntas?", "4*5*5*70", "Se calcula una pata y se multiplica por 4.", " cm³"),
        ("=", "{F} ¿Cuántos cm³ tiene la mesa en total?", "120*60*4+4*5*5*70", "Se suman los volúmenes del tablero y de las patas.", " cm³"),
        ("abc", "{F} Si el vértice inferior izquierdo del tablero está en (0, 0, 70), ¿qué dice la tercera coordenada?", "Que el tablero está a 70 cm de altura", "Que el tablero mide 70 cm de largo", "Que el tablero tiene 70 vértices", "z es la altura y 70 coincide con el alto de las patas."),
        ("=", "{F} ¿Cuántos fotogramas tiene la animación de 10 segundos si se mostrara a 24 fps?", "10*24", "Se multiplican los segundos por los fps.", " fotogramas"),
        ("abc", "{F} Para comprobar sobre un dibujo que el tablero mide 120 cm, ¿qué vista conviene?", "La isométrica, porque conserva las medidas sobre los ejes", "La perspectiva, porque se parece a una foto", "Ninguna, porque no se puede medir", "La isométrica conserva medidas sobre los ejes."),
        ("abc", "{F} Para mostrar la mesa a la mandante con una imagen parecida a una fotografía, ¿qué vista conviene?", "La perspectiva", "La isométrica", "Una lista de vértices", "La perspectiva imita la visión humana."),
        ("=", "{F} Si cada pata tuviera 6 cm por 6 cm por 70 cm, ¿cuántos cm³ tendrían las 4 patas?", "4*6*6*70", "Se multiplica la cantidad por el volumen de una pata.", " cm³"),
        ("abc", "{F} Un compañero dice que la mesa de la ficha tiene 4 aristas porque tiene 4 patas. ¿Qué error comete?", "Confunde piezas con aristas: cada caja tiene 12 aristas", "Ninguno, porque cada pata tiene una arista", "Olvida el tablero", "Cada caja tiene 12 aristas; las patas son piezas, no aristas."),
        ("abc", "{F} La luz del modelo se coloca delante de la mesa. ¿Qué produce?", "Zonas iluminadas y sombras", "Una nueva cara", "Un cambio en las medidas", "Las luces generan iluminación y sombras en el render."),
    ],
    ctx=("abc", "Un dibujante ve que el modelo tiene el tablero a 75 cm de altura y las patas de 70 cm. ¿Qué detecta?", "Una incoherencia entre piezas: el tablero queda separado de las patas", "Ningún problema", "Un error de textura", "El tablero debe apoyarse en las patas; la diferencia indica un error."),
    sc=[
        ("En Dibujo Técnico: ¿qué son los fps?", "Los fotogramas por segundo de una animación", "Indican cuántas imágenes se muestran cada segundo."),
        ("¿Qué vista conserva las medidas sobre los ejes?", "La isométrica", "La perspectiva achica los objetos lejanos y no conserva medidas."),
        ("¿Cuántos fotogramas hay en 4 segundos a 25 fps?", "100", "Se multiplican los segundos por los fps."),
    ],
    op=("Un modelo de ejemplo representa un banco con un asiento (caja de 100 cm por 30 cm por 5 cm) y 2 apoyos (cajas de 5 cm por 30 cm por 40 cm). Calcula el volumen total, cuántos fotogramas tendría una animación de 8 segundos a 24 fps y escribe qué vista usarías para medir y cuál para mostrar el banco a una mandante.",
        "Asiento: 100 × 30 × 5 = 15.000 cm³. Apoyos: 2 × 5 × 30 × 40 = 12.000 cm³. Total: 27.000 cm³. Fotogramas: 8 × 24 = 192. Para medir, la vista isométrica; para mostrar, la perspectiva.",
        ["calcula los volúmenes", "calcula los fotogramas", "elige bien las vistas"],
        ["hoja con cálculos y dos vistas elegidas"],
        ["olvidar un apoyo", "confundir fps con segundos", "invertir las vistas"],
        "Pregunta: «¿qué vista te sirve para medir?». Si dice perspectiva, repasa la diferencia."),
    reinforce="Cuenta los vértices, aristas y caras de una caja de cartón que tengas en casa.",
    extend="Explica con un ejemplo inventado cómo se combinan primitivas para formar un objeto.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (caso de ejemplo). Plano de un edificio pequeño: 20 m de largo, 12 m de ancho y 9 m de alto. Modelo 3D recibido: 20 m de largo, 12 m de ancho y 7,5 m de alto. "
     "Maqueta física que se quiere construir a escala 1:100. Textura de ejemplo: una pared de ladrillo que se repite sin cortes visibles. Una vista del modelo muestra la altura de la puerta mayor que la altura de la pared.")
build(
    O7, 3, F,
    use="Aprenderé a comparar un modelo 3D con los planos, a calcular las medidas de una maqueta y a detectar errores antes de generar las imágenes finales.",
    prior=["Sé usar escalas.", "Sé calcular volúmenes.", "Sé qué es un modelo 3D."],
    explain=[
        "Antes de generar imágenes finales se comprueba el modelo contra los planos. Se comparan largo, ancho y alto, la ubicación de puertas y ventanas y la altura de los niveles. Si el modelo tiene medidas distintas, el error se registra con el lugar, el valor del plano y el valor del modelo. No se corrige a ojo, porque puede estar mal el plano o el modelo, y quien firma el proyecto lo confirma.",
        "Una maqueta es una reproducción a escala reducida de un objeto o de un lugar. Cada medida de la maqueta es la medida real dividida por el número de la escala. Con la escala 1:100, 20 m (2.000 cm) se transforman en 20 cm. Si la escala se aplica a un área, el área se reduce con el cuadrado del número y el volumen, con el cubo; en esta clase solo se calculan largos.",
        "También se revisan problemas de imagen: elementos que se cruzan (una puerta más alta que la pared), texturas que se repiten de forma visible y escalas de textura equivocadas, como ladrillos del tamaño de una puerta. Estos defectos se corrigen antes de gastar horas en el render final.",
    ],
    vocab=[("maqueta", "reproducción a escala reducida de un objeto o lugar"), ("coincidencia", "que modelo y plano tengan las mismas medidas"), ("repetición de textura", "patrón que se nota porque la imagen se repite"), ("escala de textura", "tamaño con que se ve la textura sobre el objeto")],
    worked=[
        ("Medida de una maqueta", "Un edificio de ejemplo mide 30 m de largo y la maqueta se construye a escala 1:200. ¿Cuántos centímetros mide el largo de la maqueta?", ["30 m son 3.000 cm.", "3.000 ÷ 200 = 15 cm."], "15 cm"),
        ("Comparar modelo y plano", "El plano de ejemplo dice altura 6 m y el modelo 5 m. ¿Qué diferencia hay?", ["6 − 5 = 1 m.", "Se registra y se consulta a quien firmó el proyecto."], "1 m de diferencia"),
    ],
    mistakes=[("Corregir el modelo sin avisar porque «seguro el error es del modelo».", "El plano también puede estar mal y el error se quedaría escondido.", "Registra la diferencia y consulta antes de corregir."),
              ("Medir la maqueta con la escala al revés, multiplicando por 100.", "La maqueta es más pequeña que el edificio real, por lo que se divide.", "Divide la medida real por el número de la escala.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una maqueta?", "Una reproducción a escala reducida de un objeto o lugar", "Una lista de materiales", "Un video de un recorrido", "La maqueta reproduce el objeto en tamaño reducido."),
        ("abc", "¿Qué se compara entre el modelo y el plano?", "Medidas, ubicación de puertas y ventanas, y alturas", "Solo los colores", "Solo la textura", "La coincidencia con el plano es la base del control."),
        ("abc", "¿Qué haces con una diferencia entre modelo y plano?", "La registro y la consulto con quien firmó el proyecto", "Corrijo el modelo sin avisar", "La ignoro", "No se sabe si el error está en el plano o en el modelo."),
        ("=", "{F} ¿Cuántos centímetros mide el largo de la maqueta a escala 1:100?", "2000//100", "20 m son 2.000 cm, y se dividen por 100.", " cm"),
        ("=", "{F} ¿Cuántos centímetros mide el ancho de la maqueta a escala 1:100?", "1200//100", "12 m son 1.200 cm, y se dividen por 100.", " cm"),
        ("=", "{F} ¿Cuántos centímetros mide la altura de la maqueta a escala 1:100 según el plano?", "900//100", "9 m son 900 cm, y se dividen por 100.", " cm"),
        ("=", "{F} ¿Cuántos centímetros reales de diferencia hay entre la altura del plano y la del modelo?", "(9-7.5)*100", "La diferencia de 1,5 m se pasa a centímetros multiplicando por 100.", " cm"),
        ("abc", "{F} ¿Quién debe confirmar cuál altura es la correcta?", "Quien firmó el proyecto", "El dibujante del modelo", "El que hace la maqueta", "Solo el responsable del proyecto puede confirmarlo."),
        ("abc", "{F} Una vista muestra una puerta más alta que la pared. ¿Qué tipo de problema es?", "Una incoherencia geométrica del modelo", "Un problema de licencia", "Un problema de plazo", "Los elementos no pueden sobresalir de la pared que los contiene."),
        ("abc", "{F} Ves que la textura de ladrillo se repite en un patrón evidente. ¿Qué haces antes del render final?", "Ajusto la textura o la escala de textura para disimular la repetición", "Dejo el patrón: nadie lo notará", "Agrando todo el modelo", "Los defectos se corrigen antes de gastar tiempo en el render."),
        ("=", "{F} Si una maqueta se hiciera a escala 1:50, ¿cuántos centímetros mediría el largo de 20 m?", "2000//50", "20 m son 2.000 cm, y se dividen por 50.", " cm"),
        ("abc", "{F} ¿Cuál escala daría una maqueta más grande, 1:50 o 1:100?", "1:50", "1:100", "Son iguales", "A menor número de la derecha, mayor tamaño de la maqueta."),
        ("abc", "{F} Con la escala 1:100, ¿cuál de estas afirmaciones sobre el volumen es correcta?", "El volumen de la maqueta es mucho menor que 1/100 del real", "El volumen de la maqueta es 1/100 del real", "El volumen es igual al real", "El volumen se reduce con el cubo de la escala, es decir, un millonésimo."),
    ],
    ctx=("abc", "Tu jefa te pide enviar hoy el render y ves la altura distinta de la del plano. ¿Qué haces?", "Aviso de la diferencia por escrito y espero la confirmación antes de generar el render final", "Genero el render igual", "Cambio el plano para que coincida", "Un render con medidas equivocadas es trabajo perdido."),
    sc=[
        ("En Dibujo Técnico: ¿cómo se obtiene la medida de la maqueta?", "Se divide la medida real por el número de la escala", "La maqueta es más pequeña que el objeto real."),
        ("¿Qué haces con una diferencia modelo y plano?", "La registro y la consulto", "No se corrige a ojo sin confirmar el dato."),
        ("¿Qué defecto de textura conviene corregir antes del render?", "La repetición visible", "Es un defecto que se nota en la imagen final."),
    ],
    op=("Un plano de ejemplo dice que un galpón mide 30 m de largo, 15 m de ancho y 6 m de alto. El modelo 3D tiene 30 m de largo, 15 m de ancho y 5 m de alto. Calcula la diferencia, la maqueta a escala 1:100 con las medidas del plano, y escribe el registro de la diferencia y a quién se la consultas.",
        "Diferencia de altura: 1 m. Maqueta: 30 cm × 15 cm × 6 cm. Registro: «Galpón, altura: plano 6 m, modelo 5 m; se consulta a quien firmó el proyecto antes de generar el render».",
        ["calcula la diferencia", "calcula las medidas de la maqueta", "escribe el registro con lugar y valores"],
        ["hoja con cálculos y registro"],
        ["multiplicar por 100", "corregir sin consultar", "olvidar las unidades"],
        "Pregunta: «¿cuánto mide el alto de la maqueta?». Si no responde, repasa la división por la escala."),
    reinforce="Mide un objeto de tu pieza y calcula su tamaño en una maqueta a escala 1:10.",
    extend="Explica con un ejemplo inventado por qué conviene revisar el modelo antes de generar las imágenes finales.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (encargo de animación de ejemplo). Recorrido virtual de una casa de 20 segundos a 24 fotogramas por segundo (fps). Resolución de cada imagen: 1920 píxeles de ancho por 1080 de alto. "
     "Tiempo de cálculo de ejemplo: 3 minutos por fotograma. El computador de la oficina está disponible 8 horas al día y el plazo de la mandante es de 3 días. Todos los valores son de ejemplo.")
build(
    O7, 4, F,
    use="Aprenderé a calcular fotogramas, píxeles y tiempos de cálculo de un render y a decidir si un plazo es posible.",
    prior=["Sé multiplicar y dividir.", "Sé qué son fotogramas y fps.", "Sé convertir minutos en horas."],
    explain=[
        "Una imagen digital está formada por píxeles, puntos de color ordenados en filas y columnas. La resolución es la cantidad de píxeles de ancho por la de alto: 1920 por 1080 da 2.073.600 píxeles. Más píxeles significan más detalle y también más tiempo de cálculo y más espacio de almacenamiento.",
        "Una animación se compone de fotogramas. Los fotogramas totales son los segundos por los fps. Si cada fotograma tarda un tiempo en calcularse, el tiempo total es los fotogramas por ese tiempo. Para saber si se llega al plazo se compara el tiempo total con las horas disponibles: horas disponibles = horas por día × días. Una hora son 60 minutos.",
        "Un buen plan considera imprevistos: el computador puede fallar, una corrección puede obligar a repetir fotogramas y un archivo puede perderse. Por eso se hacen copias de seguridad, se prueba con pocos fotogramas antes del render completo y se informa el avance. El trabajo de pantalla prolongado requiere pausas.",
    ],
    vocab=[("píxel", "punto de color de una imagen digital"), ("resolución", "cantidad de píxeles de ancho por alto"), ("tiempo de cálculo", "tiempo que tarda el computador en generar un fotograma"), ("plazo", "fecha o tiempo límite para entregar"), ("prueba", "render de pocos fotogramas para verificar antes del completo")],
    worked=[
        ("Fotogramas y tiempo", "Una animación de ejemplo dura 10 segundos a 25 fps y cada fotograma tarda 2 minutos. ¿Cuántos minutos tarda en total?", ["Fotogramas: 10 × 25 = 250.", "Tiempo: 250 × 2 = 500 minutos."], "500 minutos"),
        ("Horas disponibles", "Un computador de ejemplo se usa 6 horas al día durante 2 días. ¿Cuántas horas dispone?", ["Horas = 6 × 2.", "El total es 12 horas."], "12 horas"),
    ],
    mistakes=[("Calcular el tiempo en minutos y compararlo con las horas disponibles sin convertir.", "Compara cantidades en unidades distintas y da una conclusión falsa.", "Convierte todo a minutos o a horas antes de comparar."),
              ("Prometer el plazo calculado sin considerar imprevistos.", "Un fallo o una corrección pueden retrasar el trabajo.", "Considera un margen y avisa si el plazo es justo.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un píxel?", "Un punto de color de una imagen digital", "Un fotograma", "Una unidad de peso", "Las imágenes digitales están formadas por píxeles."),
        ("abc", "¿Qué es la resolución de una imagen?", "La cantidad de píxeles de ancho por alto", "El tiempo que dura el video", "El número de colores del modelo", "La resolución describe el tamaño de la imagen en píxeles."),
        ("abc", "¿Cómo se calcula el total de fotogramas de una animación?", "Segundos por fps", "Segundos más fps", "Fps menos segundos", "Los fps indican fotogramas por segundo."),
        ("=", "{F} ¿Cuántos fotogramas tiene el recorrido virtual?", "20*24", "Se multiplican los segundos por los fps.", " fotogramas"),
        ("=", "{F} ¿Cuántos píxeles tiene cada imagen?", "1920*1080", "Se multiplica el ancho por el alto.", " píxeles"),
        ("=", "{F} ¿Cuántos minutos tarda el cálculo de todos los fotogramas?", "20*24*3", "Se multiplican los fotogramas por los minutos de cada uno.", " minutos"),
        ("=", "{F} ¿Cuántas horas son esos minutos?", "20*24*3//60", "Se divide el total de minutos por 60.", " horas"),
        ("=", "{F} ¿Cuántas horas tiene disponibles la oficina en el plazo de 3 días?", "8*3", "Se multiplican las horas por día por los días.", " horas"),
        ("abc", "{F} ¿Alcanza el tiempo disponible para el cálculo?", "Justo: 24 horas necesarias y 24 horas disponibles, sin margen", "Sobran 8 horas", "Faltan 10 horas", "Ambas cantidades son 24 horas, así que no queda margen para imprevistos."),
        ("abc", "{F} Dado que no hay margen, ¿qué conviene hacer?", "Hacer una prueba corta, hacer copias y avisar que el plazo es justo", "No avisar y trabajar en secreto", "Entregar menos fotogramas sin decirlo", "Informar y prevenir imprevistos es parte de un buen plan."),
        ("=", "{F} Si el tiempo por fotograma bajara a 2 minutos, ¿cuántas horas tardaría el cálculo?", "20*24*2//60", "Se recalcula con 2 minutos por fotograma.", " horas"),
        ("=", "{F} En ese caso, ¿cuántas horas de margen quedarían del tiempo disponible?", "8*3-20*24*2//60", "Se resta el tiempo necesario al disponible.", " horas"),
        ("abc", "{F} Un compañero propone subir la resolución al doble en ancho y en alto. ¿Qué pasa con el tiempo de cálculo?", "Aumenta, porque hay cuatro veces más píxeles", "Disminuye", "No cambia", "Doblar ancho y alto multiplica por cuatro los píxeles y el trabajo."),
    ],
    ctx=("abc", "Faltan 2 horas para entregar y el render sigue en el fotograma 400 de 480. El computador tardaría 4 horas más. ¿Qué corresponde?", "Avisar que habrá retraso y acordar un nuevo plazo", "Entregar el video incompleto sin decir nada", "Reducir la resolución sin avisar", "Se informa el retraso con transparencia y se acuerda una solución."),
    sc=[
        ("En Dibujo Técnico: ¿cómo se calcula la cantidad de píxeles?", "Ancho por alto", "Es el producto de ambas dimensiones."),
        ("¿Para qué sirve una prueba corta?", "Para verificar el resultado antes del render completo", "Así se detectan errores a tiempo."),
        ("¿Cuántos minutos son 3 horas?", "180", "Una hora son 60 minutos, y por eso se divide."),
    ],
    op=("Una animación de ejemplo dura 15 segundos a 24 fps y cada fotograma tarda 4 minutos. El computador está disponible 6 horas diarias y la mandante da 3 días. Calcula los fotogramas, las horas necesarias, las horas disponibles y decide si se llega al plazo; escribe qué le dirías a la mandante.",
        "Fotogramas: 15 × 24 = 360. Minutos: 360 × 4 = 1.440, es decir, 24 horas. Disponibles: 6 × 3 = 18 horas. No se llega: faltan 6 horas. Aviso: «Con los equipos disponibles se necesitan 4 días; propongo un nuevo plazo o menor resolución».",
        ["calcula fotogramas y horas", "compara con las horas disponibles", "redacta un aviso claro"],
        ["hoja con cálculos y un mensaje"],
        ["no convertir minutos a horas", "prometer un plazo imposible", "no proponer alternativas"],
        "Pregunta: «¿cuántas horas necesitas y cuántas tienes?». Si no sabe, pide que reordene los pasos."),
    reinforce="Calcula cuántos fotogramas tendría un video de 30 segundos a 30 fps.",
    extend="Explica con un ejemplo inventado por qué se avisa un retraso antes de la fecha de entrega.",
)

# ============================================================ OAE-07, clase 5
F = ("Ficha 5 (alternativas de render de ejemplo). La animación tiene 480 fotogramas. Calidad media: 3 minutos por fotograma. Calidad alta: 6 minutos por fotograma. "
     "Horas disponibles para el cálculo: 36. Lista de control de la entrega: (1) medidas del modelo iguales a los planos; (2) texturas con licencia vigente; (3) sin personas reconocibles sin permiso; "
     "(4) imágenes con la resolución pedida; (5) copia de seguridad hecha; (6) nombre de archivo con la revisión.")
build(
    O7, 5, F,
    use="Aprenderé a comparar alternativas de calidad y tiempo de un render y a verificar la entrega con una lista de control.",
    prior=["Sé calcular tiempos de render.", "Sé qué es una lista de control.", "Sé comparar horas disponibles y necesarias."],
    explain=[
        "Elegir entre calidad media y alta es una decisión con costos y beneficios. La calidad alta tiene más detalle y ocupa más tiempo de cálculo; la media es más rápida y puede ser suficiente si el objetivo es una revisión del proyecto. Se comparan con criterios medibles: tiempo total, horas disponibles y margen restante. La decisión final la toma el responsable del proyecto con la mandante.",
        "Una alternativa mixta es renderizar la animación en calidad media y unas pocas imágenes fijas importantes en calidad alta. Así se cumple el plazo y se dan imágenes de alto detalle donde más importan. Se anota la decisión y su razón.",
        "La entrega se verifica con una lista de control: medidas iguales a los planos, texturas con licencia, sin personas reconocibles sin permiso, resolución pedida, copia de seguridad y nombre con la revisión. Un solo punto en rojo impide entregar. La propiedad intelectual del modelo se aclara con la mandante: quién puede usarlo después.",
    ],
    vocab=[("alternativa mixta", "combinar dos calidades según la importancia"), ("margen", "tiempo que sobra después de calcular"), ("lista de control", "lista de puntos que se revisan antes de entregar"), ("propiedad intelectual", "derecho del autor sobre su obra")],
    worked=[
        ("Calcular horas", "Una animación de ejemplo tiene 120 fotogramas y cada uno tarda 3 minutos. ¿Cuántas horas son?", ["120 × 3 = 360 minutos.", "360 ÷ 60 = 6 horas."], "6 horas"),
        ("Aplicar la lista de control", "Una entrega de ejemplo cumple todo, pero no tiene copia de seguridad. ¿Se entrega?", ["Un punto de la lista no se cumple.", "No se entrega hasta hacer la copia."], "No, primero se hace la copia de seguridad"),
    ],
    mistakes=[("Elegir siempre la calidad más alta «por si acaso».", "Puede no alcanzar el tiempo y la mandante quizá solo necesita una revisión.", "Compara con las horas disponibles y el objetivo."),
              ("Dejar el modelo en un solo disco sin copia.", "Si falla el disco, se pierde el trabajo.", "Haz copias en lugares distintos.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una alternativa mixta de render?", "Combinar calidad media para el video y alta para pocas imágenes fijas", "Hacer todo en calidad baja", "Cambiar el modelo por otro", "La mixta combina calidades según la importancia."),
        ("abc", "¿Quién decide la calidad final del render?", "El responsable del proyecto con la mandante", "El dibujante solo", "El computador", "El dibujante entrega la comparación; la decisión es del responsable."),
        ("abc", "¿Qué es el margen de tiempo?", "El tiempo que sobra después del cálculo", "El tiempo que dura el video", "La resolución", "Es la diferencia entre horas disponibles y necesarias."),
        ("=", "{F} ¿Cuántas horas tarda el render de calidad media?", "480*3//60", "Se multiplican los fotogramas por los minutos y se divide por 60.", " horas"),
        ("=", "{F} ¿Cuántas horas tarda el render de calidad alta?", "480*6//60", "Se multiplican los fotogramas por los minutos y se divide por 60.", " horas"),
        ("abc", "{F} ¿Qué alternativa cabe en las horas disponibles?", "La media, con 24 horas, y sobran 12", "La alta, con 48 horas", "Ambas caben", "La alta necesita 48 horas y solo hay 36."),
        ("=", "{F} ¿Cuántas horas de margen quedan con calidad media?", "36-480*3//60", "Se resta el tiempo necesario al disponible.", " horas"),
        ("=", "{F} ¿Cuántas horas faltarían con calidad alta?", "480*6//60-36", "Se resta lo disponible a lo necesario.", " horas"),
        ("=", "{F} Con las 12 horas de margen, ¿cuántas imágenes fijas de 20 minutos cada una en calidad alta se podrían hacer?", "(36-480*3//60)*60//20", "Se pasan las horas a minutos y se dividen por 20.", " imágenes"),
        ("abc", "{F} ¿Qué punto de la lista de control falla si el nombre del archivo no dice la revisión?", "El punto (6)", "El punto (2)", "El punto (4)", "El punto (6) pide el nombre con la revisión."),
        ("abc", "{F} Descubres que una textura tiene licencia vencida. ¿Qué haces?", "Cambio la textura o consigo una licencia vigente antes de entregar", "La dejo, porque nadie lo notará", "Le cambio el nombre", "Una licencia vencida no autoriza el uso."),
        ("abc", "{F} La mandante pide quedarse con los archivos del modelo. ¿Qué aclaras?", "Qué derechos de uso tendrá cada parte, por escrito", "Nada, porque es suyo siempre", "Que no se pueden entregar", "La propiedad intelectual se acuerda por escrito."),
        ("=", "{F} Si se agregaran 60 fotogramas más en calidad media, ¿cuántas horas tardaría en total?", "(480+60)*3//60", "Se recalculan los fotogramas totales y se divide por 60.", " horas"),
    ],
    ctx=("abc", "El jefe pide calidad alta, pero los cálculos indican que no se llega al plazo. ¿Qué haces?", "Presento los números y propongo calidad media o una alternativa mixta", "Acepto y entrego tarde sin avisar", "Reduzco la calidad sin decir nada", "Se informa con datos y se proponen alternativas."),
    sc=[
        ("En Dibujo Técnico: ¿para qué sirve una lista de control?", "Para verificar la calidad antes de entregar", "Todos los puntos de la lista deben cumplirse."),
        ("¿Cómo se calcula el margen?", "Horas disponibles menos horas necesarias", "Un margen negativo indica que faltan horas."),
        ("¿Qué acuerdas sobre los archivos del modelo?", "Quién puede usarlos después, por escrito", "Es parte de la propiedad intelectual."),
    ],
    op=("Un render de ejemplo tiene 300 fotogramas. En calidad media cada uno tarda 4 minutos y en alta 8 minutos. Hay 30 horas disponibles. Calcula las horas de cada alternativa, el margen o el déficit, y propón una alternativa mixta con 3 imágenes fijas en alta calidad de 30 minutos cada una. Escribe tres puntos de tu lista de control.",
        "Media: 300 × 4 = 1.200 min = 20 horas, margen 10 horas. Alta: 300 × 8 = 2.400 min = 40 horas, faltan 10. Mixta: media más 3 imágenes de 30 minutos = 1,5 horas; total 21,5 horas, cabe. Lista: licencias vigentes; medidas iguales al plano; copia de seguridad.",
        ["calcula las horas de cada calidad", "compara con las 30 horas", "propone una mixta y tres puntos de control"],
        ["tabla de tiempos y decisión"],
        ["no convertir a horas", "elegir calidad alta sin cálculo", "omitir la lista de control"],
        "Pregunta: «¿por qué no eliges la alta?». Si no responde, pídele que muestre las horas."),
    reinforce="Calcula cuánto tardaría un render de 100 fotogramas si cada uno tarda 90 segundos.",
    extend="Explica con un ejemplo inventado por qué una alternativa mixta puede ser mejor que elegir solo una calidad.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (encargo de ejemplo, inventado). El taller de copias «Copias Central» recibe de un estudio el archivo de un plano para imprimir 4 copias en papel formato A1 (594 mm por 841 mm) a escala 1:50. "
     "Instrucción escrita del estudio: «el plano es confidencial; entregarlo solo a quien presente la orden de retiro». Equipo: una impresora de gran formato, llamada plotter. Los rollos de papel son pesados y los cartuchos de tinta manchan.")
build(
    O8, 1, F,
    use="Aprenderé qué es imprimir y reproducir planos, qué parámetros influyen en la calidad y qué cuidados de seguridad y confidencialidad hay que tener.",
    prior=["Sé qué es una escala.", "Sé que la hoja A4 mide 210 mm por 297 mm.", "Sé multiplicar cantidades."],
    explain=[
        "Imprimir un plano es llevar el archivo digital al papel; reproducir es sacar copias del plano ya impreso o del archivo. Un plano debe salir con la escala exacta, las líneas legibles y todos sus datos. Los parámetros de impresión son el formato del papel, la escala o porcentaje de impresión, la orientación (horizontal o vertical), la resolución, el grosor de las líneas, el color o blanco y negro, y la cantidad de copias.",
        "Si la escala de impresión no es 100 %, el plano sale reducido o ampliado y la escala escrita en el rótulo deja de ser verdadera. Por eso se imprime a 100 % y se verifica con la escala gráfica, una regla dibujada en el plano. Las copias que no sirven se rompen o se devuelven, no se dejan a la vista, porque el plano es confidencial.",
        "Hay cuidados de seguridad y salud: los rollos de papel son pesados y se mueven entre dos personas o con ayuda; la tinta puede manchar la piel y la ropa; no se meten las manos en las partes móviles del equipo ni se abre un equipo encendido; y quien trabaja mucho de pie o frente a pantalla debe hacer pausas. Esto es aprendizaje conceptual en papel y no te habilita para operar equipos de impresión sin capacitación.",
    ],
    vocab=[("imprimir", "llevar un archivo digital al papel"), ("reproducir", "sacar copias de un plano"), ("plotter", "impresora de gran formato"), ("escala de impresión", "porcentaje con que se imprime un archivo"), ("escala gráfica", "regla dibujada en el plano"), ("confidencial", "que solo puede conocer quien está autorizado")],
    worked=[
        ("Calcular cantidades", "Un taller de ejemplo imprime 6 copias de un plano en 3 formatos distintos. ¿Cuántas hojas son?", ["Se multiplican las copias por los formatos: 6 × 3.", "Resultado: 18 hojas."], "18 hojas"),
        ("Actuar ante una copia fallida", "Una copia de un plano confidencial sale con una mancha. ¿Qué haces con ella?", ["La copia no sirve, pero tiene información reservada.", "Se rompe o se devuelve al estudio, no se tira a la basura a la vista."], "Se rompe o se devuelve, no se deja a la vista"),
    ],
    mistakes=[("Imprimir con la opción «ajustar a la página» sin revisar la escala.", "El plano sale a otra escala y las medidas leídas con regla serán falsas.", "Imprime a 100 % y verifica la escala gráfica."),
              ("Entregar las copias a la primera persona que las pide.", "El plano es confidencial y solo debe recibirlo quien presente la orden.", "Pide la orden de retiro antes de entregar.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un plotter?", "Una impresora de gran formato", "Un programa de dibujo", "Un tipo de plano", "El plotter imprime planos en formatos grandes."),
        ("abc", "¿Qué pasa si se imprime con «ajustar a la página» sin controlar?", "La escala del plano puede cambiar", "El plano sale siempre perfecto", "Se cambia el rótulo", "El ajuste automático altera el tamaño y por lo tanto la escala."),
        ("abc", "¿Qué se hace con una copia fallida de un plano confidencial?", "Se rompe o se devuelve al estudio", "Se deja a la vista para quien la quiera", "Se vende como papel reciclado sin romperla", "La copia aún contiene información reservada."),
        ("=", "{F} ¿Cuántos milímetros cuadrados tiene una hoja A1?", "594*841", "La superficie es ancho por alto.", " mm²"),
        ("=", "{F} Un rollo de ejemplo alcanza para 12 impresiones A1 y ya se hicieron las 4 del encargo. ¿Cuántas impresiones A1 quedan en el rollo?", "12-4", "Se resta al total del rollo lo ya impreso.", " impresiones"),
        ("abc", "{F} ¿Con qué porcentaje de escala de impresión se debe imprimir para respetar la escala 1:50?", "100 %", "50 %", "200 %", "Con 100 % el plano mantiene su escala; otro valor la altera."),
        ("abc", "{F} Una persona llega y pide las copias sin orden de retiro. ¿Qué haces?", "No las entrego hasta que presente la orden, porque el plano es confidencial", "Se las entrego porque parece de confianza", "Se las entrego si da su nombre", "La instrucción pide entregar solo con orden de retiro."),
        ("abc", "{F} El rollo de papel pesa mucho. ¿Cuál es la conducta segura?", "Moverlo entre dos personas o con ayuda", "Levantarlo solo y rápido", "Arrastrarlo por el suelo", "Los rollos pesados pueden dañar la espalda; se mueven con ayuda."),
        ("abc", "{F} El plotter se atasca. ¿Qué haces?", "Aviso al responsable del equipo, sin meter las manos en partes móviles", "Meto la mano para sacar el papel con el equipo encendido", "Golpeo el equipo", "Las partes móviles son un riesgo y el equipo lo revisa personal capacitado."),
        ("abc", "{F} Una hoja A4 mide 210 por 297 mm. Por su tamaño, ¿cuál es el uso más probable de una hoja A1?", "Un plano grande para una mesa de trabajo", "Una carta personal", "Una tarjeta de presentación", "El A1 mide 594 por 841 mm, un tamaño de plano grande."),
        ("abc", "{F} Un empleado quiere llevarse una copia sobrante «para aprender». ¿Qué corresponde?", "Pedir autorización al estudio, porque el plano es confidencial", "Llevársela, porque sobró", "Fotografiar la copia", "Una copia de un plano ajeno no se lleva sin permiso."),
        ("abc", "{F} Se imprime a las 17 h y se descubre que el archivo era la revisión B y no la C. ¿Qué haces?", "Aviso al estudio y reimprimo con la revisión vigente", "Entrego igual", "Cambio la letra B por C con lápiz", "Las copias deben ser de la revisión vigente."),
        ("=", "{F} Si el estudio pidiera 4 copias de 3 planos distintos, ¿cuántas hojas A1 serían?", "4*3", "Se multiplican las copias por los planos.", " hojas"),
    ],
    ctx=("abc", "Estás solo en el taller y llega un cliente pidiendo ver un plano que otro cliente dejó impreso. ¿Qué haces?", "No lo muestro, porque pertenece a otro cliente y es confidencial", "Se lo muestro un minuto", "Lo presto si promete no copiarlo", "Un plano de otro cliente no se muestra sin autorización."),
    sc=[
        ("En Dibujo Técnico: ¿por qué se imprime a 100 %?", "Para mantener la escala del plano", "Con otro porcentaje la escala escrita deja de ser verdadera."),
        ("¿Para qué sirve la escala gráfica?", "Para verificar la escala en la copia impresa", "Se mide con regla en el papel."),
        ("¿Qué haces con un rollo pesado?", "Lo muevo con ayuda", "Cuidar la espalda previene lesiones por levantar peso."),
    ],
    op=("Un taller de ejemplo debe imprimir 3 copias de un plano A1 y 5 copias de otro plano A3, ambos a 100 %. Calcula cuántas hojas se usan en total, escribe dos parámetros que revisarías antes de imprimir y dos cuidados de confidencialidad y seguridad.",
        "Hojas: 3 + 5 = 8 (3 A1 y 5 A3). Parámetros: formato y escala de impresión al 100 %. Cuidados: entregar solo con orden de retiro y romper las copias fallidas; mover los rollos pesados con ayuda.",
        ["calcula las hojas", "nombra dos parámetros", "nombra dos cuidados"],
        ["hoja con la suma y cuatro líneas"],
        ["olvidar la escala de impresión", "no mencionar la confidencialidad", "mezclar formatos al sumar"],
        "Pregunta: «¿qué haces con la copia que sale con mancha?». Si no responde, repasa la confidencialidad."),
    reinforce="Mide una hoja de tu cuaderno y compara con las medidas de una A4 (210 por 297 mm).",
    extend="Explica con un ejemplo inventado por qué se imprime a 100 % cuando el plano tiene una escala.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (formatos y datos de ejemplo). Formatos de la serie A en milímetros: A0, 841 por 1189; A1, 594 por 841; A2, 420 por 594; A3, 297 por 420; A4, 210 por 297. Cada formato tiene la mitad de superficie que el anterior. "
     "Un píxel es un punto de la imagen; la resolución se mide en puntos por pulgada (ppp). Una pulgada son 25,4 mm. Plano de ejemplo en PDF (archivo que conserva el diseño) que se debe imprimir en A3.")
build(
    O8, 2, F,
    use="Aprenderé los formatos de papel, la resolución, los tipos de archivo y las reglas de plegado para reproducir planos.",
    prior=["Sé multiplicar y dividir.", "Sé qué es un píxel.", "Sé convertir mm a pulgadas con 25,4 mm."],
    explain=[
        "Los planos usan los formatos de la serie A: A0, A1, A2, A3, A4. Cada uno se obtiene doblando el anterior por la mitad del lado largo, así que tiene la mitad de superficie. Un A1 equivale a dos A2, cuatro A3 y ocho A4. Las medidas en milímetros están en la ficha. Las dimensiones se leen siempre como ancho por alto.",
        "La resolución indica cuántos puntos caben en una pulgada, que son 25,4 mm: a más ppp, más detalle y más tamaño de archivo. Un archivo vectorial guarda líneas como fórmulas y se puede ampliar sin perder calidad; una imagen de píxeles pierde nitidez si se amplía demasiado. El PDF conserva el diseño y es un formato común para enviar a imprimir.",
        "Al reproducir, las copias grandes se pliegan en formato A4 con el rótulo visible, para archivarlas en carpetas. Se verifica que la revisión sea la vigente antes de imprimir. Esto es aprendizaje conceptual en papel y no te habilita para operar equipos sin capacitación.",
    ],
    vocab=[("formato", "tamaño del papel, como A1 o A3"), ("ppp", "puntos por pulgada, medida de resolución"), ("vectorial", "archivo que guarda líneas como fórmulas"), ("PDF", "archivo que conserva el diseño de un documento"), ("plegado", "doblar un plano a un tamaño menor"), ("pulgada", "unidad de longitud de 25,4 mm")],
    worked=[
        ("Pasar de formato", "¿Cuántas hojas A3 equivalen a una A1?", ["Una A1 equivale a dos A2.", "Cada A2 equivale a dos A3: en total son 4 A3."], "4 hojas A3"),
        ("Calcular píxeles", "Un lado de 2 pulgadas con una resolución de 150 ppp, ¿cuántos píxeles tiene?", ["Píxeles = pulgadas × ppp.", "2 × 150 = 300 píxeles."], "300 píxeles"),
    ],
    mistakes=[("Creer que A4 es más grande que A3 porque el número es mayor.", "En la serie A, a mayor número, menor tamaño.", "Recuerda: A0 es el más grande y A4 el más pequeño."),
              ("Ampliar una imagen de píxeles pequeña para un plano A1 «porque se verá igual».", "Se pierde nitidez y las líneas se ven borrosas.", "Usa archivos vectoriales o imágenes con resolución suficiente.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿cuál es el formato más grande de la serie A?", "A0", "A4", "A2", "En la serie A, el número menor es el formato mayor."),
        ("abc", "¿Qué indica ppp?", "Puntos por pulgada, una medida de resolución", "Páginas por plano", "Pulgadas por pliegue", "ppp mide cuántos puntos caben en una pulgada."),
        ("abc", "¿Qué ventaja tiene un archivo vectorial?", "Se puede ampliar sin perder calidad", "Es siempre más pequeño", "No necesita escala", "Las líneas se guardan como fórmulas y se redibujan nítidas."),
        ("=", "{F} ¿Cuántas hojas A4 equivalen a una A2?", "2*2", "Una A2 son dos A3 y cada A3 son dos A4.", " hojas"),
        ("=", "{F} ¿Cuántas hojas A3 equivalen a una A0?", "2*2*2", "A0 son dos A1, cada A1 dos A2 y cada A2 dos A3.", " hojas"),
        ("abc", "{F} ¿Cuántos milímetros mide el lado largo de una A3?", "420", "297", "594", "En la ficha, A3 mide 297 por 420 mm."),
        ("=", "{F} ¿Cuántos píxeles de ancho tiene una imagen de 10 pulgadas a 300 ppp?", "10*300", "Se multiplican las pulgadas por los ppp.", " píxeles"),
        ("=", "{F} ¿Cuántos mm son 10 pulgadas?", "10*25.4", "Una pulgada son 25,4 mm y se multiplica por 10.", " mm"),
        ("abc", "{F} Un plano A1 se imprime en A3. ¿Qué ocurre con el tamaño?", "Se reduce a cerca de la mitad en cada lado", "Se duplica", "No cambia", "A1 es cuatro veces la superficie de A3: cada lado es aproximadamente la mitad."),
        ("abc", "{F} Una imagen de 600 píxeles de ancho se amplía para ocupar 10 pulgadas. ¿Cuántos ppp tendrá?", "60 ppp", "600 ppp", "6 ppp", "600 dividido por 10 da 60 puntos por pulgada, resolución baja."),
        ("=", "{F} ¿Cuántos ppp tiene una imagen de 3000 píxeles en 10 pulgadas?", "3000//10", "Se dividen los píxeles por las pulgadas.", " ppp"),
        ("abc", "{F} ¿Cuál archivo conviene para un plano con muchas líneas finas?", "Un archivo vectorial o un PDF con líneas vectoriales", "Una imagen pequeña de píxeles", "Una foto del plano en un celular", "Los archivos vectoriales mantienen la calidad de las líneas."),
        ("abc", "{F} Al plegar un plano A1 hasta A4, ¿qué debe quedar visible?", "El rótulo", "La parte en blanco", "La parte trasera", "El rótulo permite identificar el plano sin abrirlo."),
    ],
    ctx=("abc", "El estudio envía una foto del plano, tomada con celular, y pide imprimirlo en A1. ¿Qué haces?", "Aviso que la foto no tiene la calidad ni la escala de un plano y pido el archivo original", "Imprimo la foto en A1", "Aumento el contraste hasta que parezca nítida", "La foto no es un archivo de plano fiable."),
    sc=[
        ("En Dibujo Técnico: ¿cuántas A4 forman una A1?", "8", "Cada formato tiene la mitad de superficie."),
        ("¿Cómo se calculan los píxeles de un lado?", "Pulgadas por ppp", "Es una multiplicación sencilla de ancho por ppp."),
        ("¿Qué debe verse al plegar un plano?", "El rótulo", "Para identificarlo en la carpeta sin abrirlo."),
    ],
    op=("Un plano de ejemplo se debe imprimir en A2 (420 por 594 mm). Calcula cuántas hojas A4 equivalen a una A2, cuántos píxeles de ancho tiene un lado de 12 pulgadas a 200 ppp, y escribe qué tipo de archivo prefieres para un plano de líneas finas y qué debe quedar visible al plegarlo.",
        "A2 = 4 hojas A4. 12 × 200 = 2.400 píxeles. Prefiero un archivo vectorial o PDF vectorial, y al plegarlo debe quedar visible el rótulo.",
        ["calcula la equivalencia y los píxeles", "elige el tipo de archivo", "indica qué debe quedar visible"],
        ["hoja con cálculos y dos frases"],
        ["pensar que A4 es mayor", "elegir una foto pequeña", "olvidar el rótulo"],
        "Pregunta: «¿cuántas A4 caben en una A2?». Si no responde, pide que dibuje los dobleces."),
    reinforce="Dobla una hoja A4 por la mitad y cuenta cuántas veces cabe en una hoja A3 imaginaria.",
    extend="Explica con un ejemplo inventado por qué un archivo vectorial es mejor que una imagen pequeña para un plano.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (control de copia de ejemplo). Plano original a escala 1:50, impreso a 100 %, con una escala gráfica que mide 100 mm. En la copia reproducida, la escala gráfica mide 96 mm. "
     "En ambos documentos un muro está dibujado con 100 mm de largo. Una persona calcula medidas reales multiplicando por 50 lo que mide con regla.")
build(
    O8, 3, F,
    use="Aprenderé a comprobar la escala de una copia con la escala gráfica y a calcular el error de lectura que produce una copia reducida.",
    prior=["Sé qué es una escala.", "Sé calcular porcentajes.", "Sé qué es una escala gráfica."],
    explain=[
        "Una copia puede salir reducida o ampliada sin que se note a simple vista. Para comprobarlo se mide con regla la escala gráfica de la copia y se compara con su valor original. El porcentaje de la copia es la medida de la copia dividida por la medida original, por 100. Si la escala gráfica de 100 mm mide 96 mm, la copia sale al 96 %, es decir, está reducida.",
        "Una copia reducida da lecturas falsas: un muro dibujado con 100 mm en el original se lee como 5.000 mm reales con la escala 1:50 (100 × 50). Si en la copia mide 96 mm, la lectura de 96 × 50 da 4.800 mm. La diferencia, 200 mm, es un error de lectura que puede producir problemas al construir o fabricar, así que la copia no se puede usar para medir.",
        "Cuando una copia no cumple, se explica el problema, se corrige la causa (por ejemplo, la configuración de escala) y se reimprime. La copia defectuosa se rompe o se devuelve, porque el plano es confidencial. Se anota el control: fecha, plano, medida de la escala gráfica y resultado.",
    ],
    vocab=[("escala gráfica", "regla dibujada en el plano"), ("reducida", "más pequeña que el original"), ("ampliada", "más grande que el original"), ("error de lectura", "diferencia entre la medida real y la leída en la copia"), ("control", "comprobación registrada de una copia")],
    worked=[
        ("Calcular el porcentaje", "La escala gráfica de un original mide 50 mm y en la copia mide 45 mm. ¿Qué porcentaje es la copia?", ["45 ÷ 50 = 0,9, es decir, 90 %.", "La copia está reducida."], "90 %, copia reducida"),
        ("Calcular el error de lectura", "Un muro de ejemplo dibujado a escala 1:100 mide 20 mm en el original y 18 mm en una copia reducida. ¿Cuál es la diferencia de lectura real?", ["Original: 20 × 100 = 2.000 mm. Copia: 18 × 100 = 1.800 mm.", "Diferencia: 200 mm."], "200 mm"),
    ],
    mistakes=[("Medir con regla sobre la copia sin comprobar antes la escala gráfica.", "Si la copia está reducida, la medida real calculada será incorrecta.", "Comprueba primero la escala gráfica."),
              ("Dar por buena una copia porque «se ve bien».", "Una reducción pequeña no se nota a simple vista pero produce errores.", "Mide la escala gráfica y registra el control.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿para qué sirve la escala gráfica en una copia?", "Para comprobar con regla que la copia mantiene la escala", "Para decorar el plano", "Para indicar el formato", "La escala gráfica permite verificar la copia."),
        ("abc", "Una copia mide menos que el original. ¿Cómo está?", "Reducida", "Ampliada", "Exacta", "Mide menos, por lo tanto está reducida."),
        ("abc", "¿Qué se hace con una copia que no cumple?", "Se corrige la causa y se reimprime; la defectuosa se rompe o devuelve", "Se entrega con una nota", "Se usa para medir", "La copia defectuosa produce errores de lectura."),
        ("abc", "{F} ¿Qué porcentaje del original es la copia?", "96 %, porque 96 mm es el 96 % de 100 mm", "104 %, porque difieren en 4 mm", "4 %, que es la diferencia", "Se divide la medida de la copia por la del original: 96 de 100."),
        ("=", "{F} ¿Cuántos milímetros reales se leerían del muro del original?", "100*50", "Se multiplican los milímetros del dibujo por 50.", " mm"),
        ("=", "{F} Si la copia reduce el muro a 96 mm, ¿cuántos milímetros reales se leerían?", "96*50", "Se multiplican los milímetros de la copia por 50.", " mm"),
        ("=", "{F} ¿Cuál es el error de lectura en milímetros?", "100*50-96*50", "Se resta la lectura de la copia a la del original.", " mm"),
        ("=", "{F} Expresado en centímetros, ¿cuál es el error de lectura?", "(100*50-96*50)//10", "Se pasa el error de milímetros a centímetros dividiendo por 10.", " cm"),
        ("abc", "{F} ¿Qué haces con esa copia?", "No la uso para medir; corrijo la causa y reimprimo a 100 %", "La uso, porque solo falta un poco", "Corrijo la escala del rótulo a 1:52", "La copia reducida entrega lecturas falsas."),
        ("abc", "{F} ¿Qué causa probable tiene una reducción del 96 %?", "Una configuración de «ajustar a la página» en vez de 100 %", "Que el plano tenga rótulo", "Que el papel sea blanco", "El ajuste automático reduce el plano para que entre en el papel."),
        ("abc", "{F} Cambiar «1:50» por «1:52» en el rótulo de la copia, ¿es correcto?", "No: es una forma de ocultar el problema y no soluciona nada", "Sí, porque así queda exacta", "Sí, siempre que se anote a lápiz", "La solución es imprimir a 100 %."),
        ("=", "{F} Si el original se hubiera reproducido al 90 %, ¿cuántos milímetros mediría una escala gráfica de 100 mm?", "100*90//100", "Se aplica el 90 % a los 100 mm.", " mm"),
        ("abc", "{F} Una copia de 90 % y una escala 1:50, ¿cómo se debe interpretar el rótulo?", "La escala escrita ya no es válida para esa copia", "Es válida porque está impresa", "Ahora es 1:45", "El rótulo conserva el 1:50 del original; la copia reducida lo incumple."),
    ],
    ctx=("abc", "El cliente acepta una copia al 96 % y dice: «no importa, yo mido con regla». ¿Qué haces?", "Le explico que las lecturas serán falsas y ofrezco reimprimir a 100 %", "Se la entrego sin explicar", "Escribo en el rótulo que es una copia reducida y listo", "Es mejor reimprimir que arriesgar lecturas falsas."),
    sc=[
        ("En Dibujo Técnico: ¿cómo se detecta una copia reducida?", "Midiendo la escala gráfica con regla", "Se compara con su valor original."),
        ("¿Qué porcentaje es una copia de 45 mm cuando el original mide 50 mm?", "90 %", "45 dividido por 50 es 0,9."),
        ("¿Qué se anota en el control de una copia?", "Fecha, plano, medida de la escala gráfica y resultado", "Permite repetir y verificar el control."),
    ],
    op=("El original de un plano a escala 1:100 tiene una escala gráfica de 80 mm. En la copia mide 76 mm. Un muro mide 30 mm en el original. Calcula el porcentaje de la copia, la medida real del muro con el original y con la copia y el error en centímetros; escribe qué harías y la línea del control.",
        "Porcentaje: 76 ÷ 80 = 95 %. Muro original: 30 × 100 = 3.000 mm. Copia: el muro mide 28,5 mm, y 28,5 × 100 = 2.850 mm; error 150 mm = 15 cm. Acción: reimprimir a 100 %. Control: «plano X, escala gráfica 76 mm de 80; resultado: reducida, reimprimir».",
        ["calcula el porcentaje", "calcula el error", "escribe acción y control"],
        ["hoja con cálculos y una línea de control"],
        ["no usar la escala gráfica", "ignorar el error", "cambiar el rótulo"],
        "Pregunta: «¿por qué no sirve la copia reducida para medir?». Si no responde, repasa el error de lectura."),
    reinforce="Mide con una regla una línea de 100 mm dibujada en tu cuaderno y compara con otra regla distinta.",
    extend="Explica con un ejemplo inventado por qué una copia reducida puede causar un error en una obra o en una pieza.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (encargo de ejemplo). Un plano en formato A1 a escala 1:50 debe reducirse a formato A3 para una reunión. Medidas del plano: A1, 594 por 841 mm; A3, 297 por 420 mm. "
     "Texto del plano: alto de 5 mm. Altura mínima legible de ejemplo: 3 mm. Precios de ejemplo: copia A1, $1.800; copia A3, $450. Se necesitan 2 copias A1 y 10 copias A3.")
build(
    O8, 4, F,
    use="Aprenderé a calcular la escala resultante al cambiar de formato, a comprobar si los textos siguen siendo legibles y a estimar el costo de una reproducción.",
    prior=["Sé qué son los formatos A.", "Sé calcular porcentajes.", "Sé qué es una escala."],
    explain=[
        "Al reducir un plano de un formato a otro, todas las medidas del dibujo se reducen en la misma proporción. Pasar de A1 a A3 reduce cada lado aproximadamente a la mitad, es decir, a 50 %. La escala del dibujo cambia: si el original está a 1:50 y la copia mide la mitad, la copia queda a 1:100, porque 1 mm del papel representa el doble de la realidad. Por eso se anota una escala gráfica nueva o se aclara en la copia la nueva escala.",
        "Los textos y las líneas también se reducen. Un texto de 5 mm de alto queda en 2,5 mm al 50 %, por debajo de un mínimo de ejemplo de 3 mm, y se vuelve difícil de leer. Si los textos no son legibles, se elige un formato mayor, se rehacen los textos o se imprimen solo las partes importantes.",
        "El costo de una reproducción es el precio por copia por la cantidad, sumado por cada formato. Se compara con el presupuesto y se informa antes de imprimir. Esto es un cálculo en papel y no te habilita para operar equipos sin capacitación.",
    ],
    vocab=[("reducir", "hacer más pequeño en una proporción"), ("proporción", "relación constante entre dos tamaños"), ("legible", "que se puede leer con claridad"), ("escala resultante", "escala que queda al cambiar el tamaño"), ("presupuesto", "dinero disponible para un trabajo")],
    worked=[
        ("Escala al reducir", "Un plano de ejemplo está a escala 1:100 y se reduce a la mitad. ¿A qué escala queda?", ["Cada medida mide la mitad en el papel.", "La escala pasa a 1:200."], "1:200"),
        ("Revisar legibilidad", "Un texto de 6 mm se reduce al 50 %, y el mínimo legible de ejemplo es 2 mm. ¿Sigue legible?", ["50 % de 6 mm es 3 mm.", "3 mm es mayor que 2 mm: sí es legible."], "Sí, mide 3 mm y es legible"),
    ],
    mistakes=[("Dejar escrita la escala 1:50 en una copia reducida a la mitad.", "La escala escrita ya no es verdadera y las lecturas serían falsas.", "Anota la nueva escala o la escala gráfica."),
              ("Reducir sin revisar el texto pequeño.", "Los textos pueden quedar ilegibles.", "Calcula el tamaño reducido y compara con el mínimo legible.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué ocurre con la escala al reducir un plano a la mitad?", "El número de la derecha se duplica", "El número de la derecha se divide por dos", "La escala no cambia", "La escala pasa de 1:50 a 1:100."),
        ("abc", "¿Qué es una medida legible?", "Una que se puede leer con claridad", "Una medida muy pequeña", "Una medida en milímetros", "Legible significa que se puede leer sin dificultad."),
        ("abc", "¿Qué se debe informar antes de imprimir?", "El costo y las condiciones", "Solo el color del papel", "Nada", "El cliente debe conocer el costo antes de aprobar."),
        ("=", "{F} A escala 1:50, ¿a qué número de la derecha queda la escala al reducir a la mitad?", "50*2", "La escala se duplica cuando el plano se reduce a la mitad.", ""),
        ("abc", "{F} Con la reducción al 50 %, ¿cuánto mide el texto de 5 mm de alto?", "2,5 mm", "5 mm", "10 mm", "El 50 % de 5 mm es la mitad: 2,5 mm."),
        ("abc", "{F} El texto reducido mide 2,5 mm y el mínimo legible es 3 mm. ¿Qué conclusión se saca?", "El texto no es legible", "El texto es legible", "El texto es el doble de lo necesario", "2,5 mm es menor que 3 mm."),
        ("abc", "{F} ¿Qué solución conviene si los textos no son legibles?", "Elegir un formato mayor o rehacer los textos", "Imprimir con una tinta más oscura", "Cambiar la escala escrita", "El tamaño real del texto es lo que importa."),
        ("=", "{F} ¿Cuánto cuestan las copias A1?", "2*1800", "Se multiplica la cantidad por el precio de cada copia.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan las copias A3?", "10*450", "Se multiplica la cantidad por el precio de cada copia.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el encargo completo?", "2*1800+10*450", "Se suman los costos de ambos formatos.", " pesos"),
        ("abc", "{F} El presupuesto es de $7.500. ¿Alcanza?", "No: el costo es $8.100 y supera el presupuesto", "Sí: el costo es exactamente $7.500", "Sí, porque la copia A3 es barata", "El costo de $8.100 es mayor que $7.500."),
        ("=", "{F} ¿Cuántos pesos faltan para cubrir el costo con el presupuesto de $7.500?", "2*1800+10*450-7500", "Se resta el presupuesto al costo.", " pesos"),
        ("abc", "{F} ¿Qué alternativa podría reducir el costo sin perder legibilidad?", "Pedir menos copias A3 o menos copias A1", "Imprimir con peor calidad sin avisar", "Quitar el rótulo", "Reducir cantidades, informando, baja el costo."),
    ],
    ctx=("abc", "El cliente quiere las copias A3 con la escala 1:50 impresa, pero fueron reducidas. ¿Qué respondes?", "Que la escala escrita debe corregirse a 1:100 o usarse la escala gráfica", "Que se deja 1:50", "Que se borra la escala", "La escala escrita debe ser verdadera."),
    sc=[
        ("En Dibujo Técnico: ¿a qué escala queda 1:50 reducido a la mitad?", "1:100", "La escala se duplica cuando el plano se reduce a la mitad."),
        ("¿Qué se revisa tras reducir un plano?", "Que los textos sigan legibles", "Los textos se reducen igual que el dibujo."),
        ("¿Cómo se calcula el costo de una reproducción?", "Precio por cantidad en cada formato, sumado", "Se multiplican y se suman los formatos."),
    ],
    op=("Un plano A1 a escala 1:100 se reduce al 50 % para A3. El texto del plano es de 4 mm y el mínimo legible de ejemplo es 3 mm. Se piden 3 copias A1 a $1.800 y 8 copias A3 a $450. Calcula la escala resultante, el texto reducido, si es legible, el costo total y escribe una alternativa si no es legible.",
        "Escala resultante: 1:200. Texto reducido: 2 mm, menor que 3 mm: no es legible. Costo: 3 × 1.800 + 8 × 450 = 5.400 + 3.600 = $9.000. Alternativa: usar A2 o rehacer los textos con mayor tamaño.",
        ["calcula la escala y el texto reducido", "calcula el costo", "propone una alternativa"],
        ["hoja con cálculos y una frase"],
        ["dejar 1:100", "no revisar la legibilidad", "olvidar un formato en el costo"],
        "Pregunta: «¿se lee el texto a esa escala?». Si no responde, revisa los cálculos."),
    reinforce="Dibuja una línea de 8 cm, escribe un texto de 5 mm y calcula su tamaño si se reduce al 50 %.",
    extend="Explica con un ejemplo inventado cómo una reducción puede hacer ilegible un plano.",
)

# ============================================================ OAE-08, clase 5
F = ("Ficha 5 (alternativas de ejemplo). Se deben reproducir 20 copias de un plano A3. Alternativa 1: imprimir en el plotter, $450 por copia, 3 minutos por copia. "
     "Alternativa 2: imprimir una y fotocopiar 19 veces, $200 por copia fotocopiada, 1 minuto por copia, con riesgo de pequeñas diferencias de escala. Plazo: 30 minutos. "
     "Lista de control de calidad: (1) revisión vigente; (2) escala gráfica verificada; (3) textos legibles; (4) líneas completas y sin manchas; (5) cantidad exacta; (6) plegado con rótulo visible; (7) confidencialidad cumplida.")
build(
    O8, 5, F,
    use="Aprenderé a comparar alternativas de reproducción por costo, tiempo y calidad, y a verificar un lote de copias con una lista de control.",
    prior=["Sé calcular costos y tiempos.", "Sé comprobar una escala gráfica.", "Sé que una copia puede salir reducida."],
    explain=[
        "Para reproducir muchas copias hay varias formas, cada una con costos, tiempos y riesgos distintos. Imprimir cada copia en el plotter es lo más fiel, pero cuesta más y tarda más; fotocopiar es más barato y rápido, pero cada fotocopia puede reducir o ampliar un poco el plano. Se comparan con criterios medibles: costo total, tiempo total y riesgo de error de escala.",
        "El tiempo total es los minutos por copia por la cantidad, y el costo total es el precio por la cantidad. Si una alternativa no cabe en el plazo o presupuesto, se descarta o se propone otra. En cualquier alternativa, cada copia o una muestra se controla con la escala gráfica y la lista de control.",
        "La lista de control se aplica a todo el lote: revisión vigente, escala gráfica verificada, textos legibles, líneas completas, cantidad exacta, plegado con rótulo visible y confidencialidad. Una sola falla impide la entrega. Los sobrantes y las copias defectuosas se rompen o se devuelven, no se dejan a la vista.",
    ],
    vocab=[("lote", "conjunto de copias del mismo trabajo"), ("muestra", "algunas copias elegidas para controlar"), ("riesgo", "posibilidad de que algo salga mal"), ("fiel", "que reproduce el original sin cambios"), ("descartar", "dejar de considerar una alternativa")],
    worked=[
        ("Calcular tiempo y costo", "Se necesitan 10 copias y cada una tarda 2 minutos y cuesta $300. ¿Cuánto tiempo y dinero se necesitan?", ["Tiempo: 10 × 2 = 20 minutos.", "Costo: 10 × 300 = $3.000."], "20 minutos y $3.000"),
        ("Controlar una muestra", "Se revisan 3 copias de un lote de 30 y todas cumplen. ¿Se puede asegurar que las 30 cumplen?", ["Una muestra da una idea, pero no garantiza el lote.", "Si el riesgo es alto, se controlan todas."], "No: la muestra no garantiza todas las copias"),
    ],
    mistakes=[("Elegir la alternativa más barata sin revisar el riesgo de escala.", "Una copia mal escalada puede dar medidas falsas.", "Compara costo, tiempo y riesgo."),
              ("Controlar solo la primera copia de un lote de fotocopias.", "Cada fotocopia puede salir distinta.", "Controla todas o al menos una muestra mayor.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un lote de copias?", "El conjunto de copias del mismo trabajo", "Una sola copia", "El papel que sobra", "Un lote reúne las copias del mismo encargo."),
        ("abc", "¿Qué riesgo tiene fotocopiar muchas veces un plano?", "Pequeñas diferencias de escala en cada copia", "Que el plano se vuelva más grande para siempre", "Ninguno", "Cada fotocopia puede reducir o ampliar levemente."),
        ("abc", "¿Qué se hace con las copias defectuosas?", "Se rompen o se devuelven", "Se dejan a la vista", "Se entregan igual", "El plano es confidencial y no debe quedar a la vista."),
        ("=", "{F} ¿Cuánto cuesta la Alternativa 1?", "20*450", "Se multiplican las copias por el precio de cada una.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta la Alternativa 2? (una impresión más 19 fotocopias)", "450+19*200", "Se suma la impresión al costo de las fotocopias.", " pesos"),
        ("=", "{F} ¿Cuántos minutos tarda la Alternativa 1?", "20*3", "Se multiplican las copias por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Cuántos minutos tarda la Alternativa 2? (3 minutos de impresión más 19 fotocopias)", "3+19*1", "Se suma la impresión a las fotocopias.", " minutos"),
        ("abc", "{F} ¿Cuál alternativa cumple el plazo de 30 minutos?", "Solo la Alternativa 2", "Solo la Alternativa 1", "Ambas", "La 1 tarda 60 minutos y la 2 tarda 22."),
        ("=", "{F} ¿Cuántos pesos más cuesta la Alternativa 1 que la 2?", "20*450-(450+19*200)", "Se resta el costo de la 2 al de la 1.", " pesos"),
        ("abc", "{F} La Alternativa 2 cumple el plazo y es más barata, pero tiene riesgo de escala. ¿Qué agregas?", "Control de cada fotocopia con la escala gráfica", "Ningún control", "Cambiar la escala escrita", "El riesgo se maneja con controles."),
        ("abc", "{F} Si el estudio exige exactitud de escala en todas las copias, ¿qué alternativa conviene?", "La 1, y pedir ampliar el plazo", "La 2 sin controles", "La que sea más rápida", "La exactitud exige lo más fiel, aunque cueste más."),
        ("abc", "{F} Al revisar el lote falta una copia (hay 19 de 20). ¿Qué punto de la lista falla?", "El punto (5), cantidad exacta", "El punto (2)", "El punto (7)", "El punto (5) pide la cantidad exacta."),
        ("abc", "{F} Una copia sale plegada con el rótulo hacia adentro. ¿Qué punto falla?", "El punto (6), plegado con rótulo visible", "El punto (1)", "El punto (3)", "El punto (6) pide el rótulo visible."),
    ],
    ctx=("abc", "Faltan 5 minutos para el plazo y la lista de control tiene un punto en rojo. ¿Qué haces?", "Aviso el retraso y corrijo el punto antes de entregar", "Entrego igual para cumplir", "Marco el punto como cumplido", "Una falla conocida no se entrega."),
    sc=[
        ("En Dibujo Técnico: ¿qué criterios comparas entre alternativas de reproducción?", "Costo, tiempo y riesgo de error de escala", "Son criterios medibles que permiten comparar con números."),
        ("¿Qué pasa si un punto de la lista no cumple?", "No se entrega hasta corregirlo", "La lista exige todos los puntos."),
        ("¿Qué se hace con los sobrantes de un plano confidencial?", "Se rompen o se devuelven", "Evita que otras personas los vean."),
    ],
    op=("Se necesitan 15 copias de un plano A3. Alternativa 1: plotter, $500 por copia y 4 minutos por copia. Alternativa 2: una impresión más 14 fotocopias, $200 por fotocopia y 1 minuto por fotocopia (la impresión cuesta $500 y tarda 4 minutos). Plazo: 30 minutos. Calcula costo y tiempo de cada una, indica cuál cumple el plazo, el riesgo de la 2 y tres puntos de control.",
        "Alt. 1: costo 15 × 500 = $7.500, tiempo 15 × 4 = 60 minutos, no cumple. Alt. 2: costo 500 + 14 × 200 = $3.300, tiempo 4 + 14 = 18 minutos, cumple. Riesgo: diferencias de escala. Control: escala gráfica en cada copia; revisión vigente; cantidad exacta.",
        ["calcula costo y tiempo de ambas", "elige la que cumple y nombra el riesgo", "propone tres controles"],
        ["hoja con tabla de costos y tiempos"],
        ["no sumar la impresión", "ignorar el riesgo de escala", "omitir un control"],
        "Pregunta: «¿cuál cumple el plazo y por qué?». Si no responde, pide que muestre los minutos."),
    reinforce="Compara el costo de hacer 12 copias a $250 cada una con 1 impresión de $400 y 11 fotocopias de $100.",
    extend="Explica con un ejemplo inventado por qué una lista de control evita entregar copias con errores.",
)
