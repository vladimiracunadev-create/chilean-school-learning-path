"""Cuaderno del estudiante, 7.º básico Tecnología: OA 04 (comunicación de procesos mediante herramientas TIC), clases 1 a 4.

Seguridad y privacidad: no se publican datos personales ni fotos de otras personas; todo tiene alternativa en papel; las herramientas se nombran por tipo (procesador de texto, presentación, planilla) y no por marca.
Cifras enteras. Los casos y los datos son inventados para practicar.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te7_a import reg
from student_lessons import arith

OA4 = "TE07 OA 04"

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Todo se puede resolver en papel.",
    use="Aprenderé a decidir qué quiero lograr al comunicar un proceso de diseño y a quién se lo voy a explicar. Sirve para elegir el formato, el lenguaje y la extensión adecuados.",
    prior=["Sé qué es una necesidad y un criterio.", "Sé que un proceso tiene pasos en orden.", "Sé que una audiencia es quien recibe un mensaje."],
    explain=[
        "Comunicar un proceso de diseño es contar a otras personas qué problema había, cómo se planificó, qué se construyó y qué resultados se obtuvieron. Antes de crear el mensaje, define el objetivo, es decir, qué quieres lograr: informar (que entiendan lo que hiciste), instruir (que puedan repetir los pasos) o convencer (que apoyen tu solución).",
        "También define la audiencia, que son las personas que recibirán el mensaje: tu curso, una profesora, estudiantes de cursos menores, una familia o un vecindario. La audiencia cambia el lenguaje, la cantidad de detalle y el formato. A estudiantes menores les conviene un lenguaje simple y muchas imágenes; a un adulto que decide si apoyar tu proyecto le sirven datos, costos y resultados.",
        "El formato puede ser un informe escrito, una presentación, un afiche, un video corto o una infografía. Se elige según el objetivo, la audiencia y el tiempo disponible. Un buen mensaje es claro y breve: una idea por diapositiva o por párrafo. Y sus datos son verdaderos: nunca se exageran los resultados.",
    ],
    vocab=[("objetivo", "lo que quieres lograr con tu mensaje"), ("audiencia", "personas que reciben el mensaje"), ("informar", "hacer que otras personas entiendan lo que hiciste"), ("instruir", "enseñar los pasos para repetir un trabajo"), ("formato", "forma en que se presenta el mensaje, como informe, afiche o video")],
    worked=[
        ("Elegir objetivo y audiencia", "Un grupo repara bancas del patio y quiere que la dirección apruebe comprar pintura. ¿Cuál es el objetivo y quién es la audiencia?", ["Quiere que la dirección apoye su idea: el objetivo es convencer.", "La audiencia es la dirección del colegio."], "Objetivo: convencer. Audiencia: la dirección"),
        ("Elegir el formato adecuado", "Se quiere explicar a estudiantes de 1.º básico cómo guardar los útiles. ¿Conviene un informe de 3 páginas o un afiche con dibujos y 3 frases cortas?", ["La audiencia es de 6 años: necesita imágenes y frases cortas.", "Un informe largo no lo entenderían."], "Un afiche con dibujos y 3 frases cortas"),
    ],
    mistakes=[
        ("Preparar un mensaje sin pensar quién lo va a recibir.", "El lenguaje o el detalle pueden no servirle a esa audiencia.", "Escribe primero el objetivo y la audiencia."),
        ("Exagerar un resultado para convencer más.", "Quien se entera del dato real pierde la confianza.", "Informa los datos verdaderos, incluso los que no salieron perfectos."),
    ],
    R=[
        ("Si quieres que otras personas puedan repetir tus pasos, ¿tu objetivo es informar, instruir o convencer?", "Instruir", "Se enseña cómo hacer algo."),
        ("Las personas que reciben tu mensaje, ¿cómo se llaman?", "Audiencia", "Es la definición del término."),
        ("Para estudiantes de 1.º básico, ¿conviene lenguaje simple o lenguaje técnico?", "Simple", "Así lo entienden."),
    ],
    C=[
        ("¿Cuál objetivo es convencer? A «mostrar los pasos de armado», B «lograr que el curso vote a favor de tu proyecto».", "B", "Convencer es lograr apoyo."),
        ("¿Qué cambia al pasar de hablarle a tu curso a hablarle a la dirección? A el lenguaje y los datos importantes, B el tema del que se trata.", "A", "La audiencia cambia la forma, no el proceso."),
        ("Un grupo dice: «No importa quién nos escuche, usamos el mismo mensaje». ¿Es buena idea?", "No", "Cada audiencia necesita un lenguaje y un detalle distintos."),
    ],
    A=[
        arith("Una presentación dura 8 minutos y se dedican 2 minutos a cada diapositiva. ¿Cuántas diapositivas conviene hacer?", "8//2", "Se divide el tiempo total entre el tiempo por diapositiva.", " diapositivas"),
        arith("Un afiche tiene 5 frases de 10 palabras cada una. ¿Cuántas palabras tiene en total?", "5*10", "Se multiplica la cantidad de frases por las palabras de cada una.", " palabras"),
        ("Para explicar a vecinos mayores cómo se reparó una banca, ¿qué formato sirve más? A una hoja con letra grande y 4 pasos, B un archivo de 40 páginas.", "A", "Es corta, clara y legible."),
    ],
    Z=[
        ("Un grupo tiene dos audiencias: estudiantes de 3.º básico y un profesor de Tecnología. ¿Qué parte del mensaje cambia?", "El lenguaje y el nivel de detalle", "La audiencia determina cómo se explica, no qué proceso se hizo."),
        ("Mateo dice: «Mi mensaje es mejor si tiene mil palabras». Elena dice: «Es mejor si es claro y corto». ¿Quién tiene razón?", "Elena", "Un mensaje claro y breve se entiende mejor."),
    ],
    D=[
        arith("Un video de 3 minutos tiene 180 segundos. Se quiere mostrar 6 pasos con la misma duración cada uno. ¿Cuántos segundos dura cada paso?", "180//6", "Se divide la duración total entre los pasos.", " segundos"),
        ("Se debe presentar a la directora en 4 minutos un proyecto con 8 diapositivas. Si cada diapositiva dura lo mismo, ¿cuántos segundos hay por diapositiva?", "30 segundos", "4 minutos son 240 segundos y 240 ÷ 8 = 30."),
    ],
    ctx=("Reparaste el cierre de una mochila y quieres contarlo a tu curso para que otros hagan lo mismo. Escribe tu objetivo, tu audiencia, un formato adecuado y un dato verdadero para incluir.", "Objetivo: instruir. Audiencia: mi curso. Formato: un afiche con 4 pasos y fotos o dibujos. Dato: la reparación tomó 20 minutos", "Une objetivo, audiencia, formato y un dato verificable."),
    sc=[
        ("¿Qué tres objetivos puede tener un mensaje de la clase?", "Informar, instruir o convencer", "Son los que se estudian en la clase."),
        ("¿Qué cambia según la audiencia?", "El lenguaje, el detalle y el formato", "Se adapta a quien recibe el mensaje."),
        ("¿Se pueden exagerar los resultados para convencer?", "No", "Los datos deben ser verdaderos."),
    ],
    open_task=(
        "Escoge un proceso. Proceso 1: reparación de una banca del patio que se terminó en 2 sesiones de 45 minutos. Proceso 2: adaptación de un estante de la sala a una altura que alcance todo el curso, con costo de $3.000. Proceso 3: mejora de un portalápices que subió de 6 a 12 lápices. Escribe tu objetivo, tu audiencia, el formato que usarías, una razón y un dato verdadero para mostrar.",
        "Proceso 3: objetivo: informar. Audiencia: mi curso. Formato: presentación corta. Razón: son pocos minutos y se ven imágenes. Dato: el portalápices pasó de 6 a 12 lápices",
        ["objetivo claro", "audiencia definida", "formato con una razón", "dato verdadero del proceso"],
        ["hoja con objetivo, audiencia, formato y dato"],
        ["no definir la audiencia", "exagerar los resultados"],
        "Pregunta: «¿qué entendería esta audiencia con tu mensaje?». Si no está claro, pídele simplificarlo.",
    ),
    reinforce="Cuenta a una persona de tu casa algo que reparaste, en 1 minuto y con lenguaje simple.",
    extend="Explica cómo cambiarías un mismo mensaje si lo tuvieras que presentar a estudiantes de 1.º básico y a un adulto que decide el presupuesto.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja, lápiz y los datos escritos en este cuaderno. Si tienes computador, puedes probar un procesador de texto, una presentación y una planilla; si no, todo se hace en papel.",
    use="Aprenderé a elegir la herramienta TIC adecuada para cada parte de un proceso de diseño, a presentar datos en tablas y gráficos claros y a armar diapositivas legibles. Sirve para comunicar con orden y sin engañar.",
    prior=["Sé qué es una tabla de datos.", "Sé calcular un promedio.", "Sé que un mensaje tiene objetivo y audiencia."],
    explain=[
        "Las herramientas TIC son programas y aparatos para crear, guardar y compartir información. Un procesador de texto sirve para escribir informes y listas de pasos. Una presentación sirve para mostrar ideas con pocas palabras e imágenes. Una planilla de cálculo sirve para ordenar datos en tablas, hacer cálculos y crear gráficos. Un programa de dibujo sirve para planos y esquemas, y una cámara o grabadora sirve para evidencias.",
        "Los gráficos deben ser honestos. En un gráfico de barras, el eje vertical debe empezar en cero; si empieza más arriba, las diferencias parecen enormes aunque sean pequeñas. Cada gráfico lleva título, nombres en los ejes y unidades. Elige el gráfico según el dato: barras para comparar valores, líneas para ver cambios en el tiempo.",
        "Una diapositiva legible tiene una idea principal, pocas líneas (como máximo 6), letra grande (24 puntos o más), buen contraste entre texto y fondo y una imagen que ayude a entender. No pongas texto largo copiado. En una planilla, una fórmula como «=SUMA(B2:B4)» suma las casillas de B2 a B4, que son 3 casillas. Revisa siempre que el resultado tenga sentido.",
    ],
    vocab=[("TIC", "tecnologías de la información y la comunicación"), ("planilla de cálculo", "programa que ordena datos en filas y columnas y hace cálculos"), ("gráfico de barras", "gráfico que compara valores con barras"), ("eje", "línea de un gráfico donde se escriben valores o nombres"), ("contraste", "diferencia de color entre texto y fondo que permite leer")],
    worked=[
        ("Elegir la herramienta", "Quieres mostrar a tu curso 5 resultados de pruebas de un puente y su promedio. ¿Qué herramienta usas para calcular y graficar?", ["Necesito ordenar números, calcular y graficar.", "Eso lo hace una planilla de cálculo."], "Una planilla de cálculo"),
        ("Leer una fórmula", "En una planilla, las casillas B2, B3 y B4 tienen 300, 400 y 500. ¿Qué resultado da «=SUMA(B2:B4)»?", ["La fórmula suma desde B2 hasta B4, es decir, 3 casillas.", "300 + 400 + 500 = 1.200."], "1.200"),
    ],
    mistakes=[
        ("Poner en una diapositiva todo el informe copiado.", "Nadie alcanza a leerlo y se pierde la idea principal.", "Deja una idea, pocas líneas y una imagen; el resto lo cuentas hablando."),
        ("Empezar el eje de un gráfico de barras en un número mayor que cero.", "Hace que las diferencias parezcan enormes y engaña.", "Empieza el eje vertical en cero."),
    ],
    R=[
        ("¿Qué herramienta sirve para hacer un gráfico a partir de una tabla: un procesador de texto o una planilla?", "Una planilla", "Está hecha para tablas, cálculos y gráficos."),
        ("En una diapositiva, ¿cuántas líneas de texto se recomiendan como máximo?", "Seis", "Es la regla de la clase."),
        ("¿Dónde debe empezar el eje vertical de un gráfico de barras?", "En cero", "Así las barras se comparan con justicia."),
    ],
    C=[
        ("¿Qué gráfico sirve para ver cómo cambió la altura de una planta cada semana? A de líneas, B de barras apiladas por color.", "A", "Las líneas muestran cambios en el tiempo."),
        ("Una diapositiva tiene letra gris clara sobre fondo blanco. ¿Qué problema tiene?", "Poco contraste", "Cuesta leer el texto."),
        ("¿Por qué un gráfico debe tener título y unidades? A para que se entienda qué mide, B para que sea más grande.", "A", "Sin título ni unidades, el gráfico no se interpreta."),
    ],
    A=[
        arith("Una planilla tiene los datos 12, 18 y 15. ¿Qué resultado da la suma de las tres casillas?", "12+18+15", "Se suman los tres valores.", ""),
        arith("Tres pruebas de un puente dieron 400 g, 450 g y 500 g. ¿Cuál es el promedio que mostraría la planilla?", "(400+450+500)//3", "Se suman y se divide entre 3.", " g"),
        ("Una barra mide el doble de alto que otra. Si el eje empieza en cero, ¿el valor real también es el doble?", "Sí", "Con el eje en cero, la altura es proporcional al valor."),
    ],
    Z=[
        ("Un gráfico muestra dos barras: 98 y 100, pero su eje empieza en 96 y la segunda barra parece el doble de alta. ¿Es honesto?", "No", "Empezar en 96 exagera la diferencia entre 98 y 100."),
        ("Una compañera quiere pegar 3 párrafos largos en una diapositiva. Otro propone dejar tres frases cortas y una foto. ¿Cuál propuesta se lee mejor?", "La del segundo", "Tiene pocas palabras y una imagen de apoyo."),
    ],
    D=[
        arith("Los valores de una columna son 30, 30, 40 y 20. ¿Cuál es el promedio?", "(30+30+40+20)//4", "Se suman y se divide entre 4.", ""),
        ("La fórmula «=SUMA(C2:C6)» ¿cuántas casillas suma?", "5", "Va de C2 a C6: C2, C3, C4, C5 y C6."),
    ],
    ctx=("Quieres mostrar a tu curso cuánto sostuvo tu estante en tres pruebas: 300 g, 360 g y 420 g. Escribe qué herramienta usarías para ordenar los datos y graficar, qué tipo de gráfico, desde qué número empieza el eje vertical y el promedio.", "Planilla de cálculo; gráfico de barras; el eje empieza en 0; promedio 360 g", "Se suma 300 + 360 + 420 = 1.080 y se divide entre 3."),
    sc=[
        ("¿Para qué sirve una planilla?", "Para ordenar datos, hacer cálculos y graficar", "Es su uso principal."),
        ("¿Cuántas líneas como máximo en una diapositiva?", "Seis", "Es la regla de legibilidad."),
        ("¿Qué debe tener todo gráfico?", "Título, ejes con nombre y unidades", "Así se entiende qué muestra."),
    ],
    open_task=(
        "Escoge un conjunto de datos. Datos 1: sostuvo 200 g, 250 g y 300 g en tres pruebas. Datos 2: un cierre se abrió 20, 22 y 24 veces antes de fallar. Dibuja a mano una tabla y un gráfico de barras con título y ejes (el eje debe empezar en cero), calcula el promedio y diseña una diapositiva con una idea principal, tres líneas como máximo y una imagen.",
        "Datos 1: promedio 250 g; gráfico de tres barras con eje desde 0; diapositiva: «Mi estante sostiene 250 g en promedio» con un dibujo del estante",
        ["tabla y gráfico con título y ejes", "eje que empieza en cero", "promedio correcto", "diapositiva legible"],
        ["hoja con tabla, gráfico y diapositiva"],
        ["eje que no empieza en cero", "demasiado texto en la diapositiva"],
        "Pregunta: «¿se ve claro desde lejos?». Si no, pídele acortar el texto.",
    ),
    reinforce="Dibuja un gráfico de barras con tus horas de sueño de los últimos 3 días, con título y unidades.",
    extend="Explica cuándo usarías un gráfico de líneas y cuándo uno de barras, con un ejemplo de cada uno.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja, lápiz y los guiones escritos en este cuaderno. Todo se puede hacer en papel.",
    use="Aprenderé a planificar un mensaje con guion y esquema de diapositivas, a repartir el tiempo y a revisar la accesibilidad. Sirve para presentar un proceso en el tiempo que tienes y para que todas las personas puedan entenderlo.",
    prior=["Sé definir objetivo y audiencia.", "Sé elegir la herramienta TIC.", "Sé dividir tiempos."],
    explain=[
        "Un guion ordena lo que dirás. Conviene tener tres partes: inicio, desarrollo y cierre. En el inicio presentas la necesidad y el usuario. En el desarrollo cuentas la planificación, la construcción y las pruebas con sus datos. En el cierre dices qué resultado obtuviste, qué aprendiste y qué mejorarías. Cada parte lleva una o más diapositivas.",
        "Se reparte el tiempo antes de ensayar. Si tienes 5 minutos y cada diapositiva dura 1 minuto, preparas 5 diapositivas. Una regla útil es no usar más de 1 idea por diapositiva y practicar una vez en voz alta con un reloj. Si pasas del tiempo, se acorta; no se habla más rápido. Es mejor contar menos y bien.",
        "La accesibilidad significa que todas las personas puedan entender tu mensaje. Usa letra grande y buen contraste, describe las imágenes con una frase (texto alternativo) y no uses solo el color para dar un dato: agrega una etiqueta. Si alguien no puede ver una pantalla, debe poder recibir lo esencial por escrito o por voz. Pide opinión a una persona antes de la presentación.",
    ],
    vocab=[("guion", "texto que ordena lo que se dirá"), ("texto alternativo", "frase que describe una imagen para quien no la ve"), ("accesibilidad", "posibilidad de que todas las personas entiendan un mensaje"), ("ensayo", "práctica de la presentación antes de hacerla"), ("cierre", "parte final con el resultado y lo aprendido")],
    worked=[
        ("Repartir el tiempo", "Tienes 6 minutos y el guion tiene inicio, desarrollo y cierre. Decides 1 minuto de inicio y 1 de cierre. ¿Cuántos minutos le quedan al desarrollo?", ["Sumo inicio y cierre: 1 + 1 = 2 minutos.", "Resto del total: 6 − 2."], "4 minutos"),
        ("Escribir un texto alternativo", "Una diapositiva muestra la foto de un portalápices con 12 lápices. ¿Qué texto alternativo escribes?", ["Debe decir qué se ve, en una frase corta.", "«Portalápices de cartón con 12 lápices en pie»."], "«Portalápices de cartón con 12 lápices en pie»"),
    ],
    mistakes=[
        ("Preparar tantas diapositivas que no alcanzas a explicar ninguna.", "El tiempo se reparte mal y se habla rápido.", "Calcula cuántas diapositivas caben en tu tiempo."),
        ("Usar solo colores para distinguir datos en un gráfico.", "Quien no distingue colores pierde la información.", "Agrega etiquetas o formas distintas."),
    ],
    R=[
        ("Un guion, ¿tiene dos o tres partes?", "Tres", "Inicio, desarrollo y cierre."),
        ("En el inicio de un guion, ¿se presenta la necesidad o los resultados?", "La necesidad", "Se parte contando el problema."),
        ("Una frase que describe una imagen para quien no puede verla, ¿cómo se llama?", "Texto alternativo", "Es la forma de hacer accesible una imagen."),
    ],
    C=[
        ("¿Qué haces si tu presentación pasa del tiempo? A acorto el contenido, B hablo más rápido.", "A", "Acortar mantiene la claridad."),
        ("¿Para qué ensayar con un reloj?", "Para comprobar que el tiempo alcanza", "El ensayo permite ajustar antes de la presentación."),
        ("Un gráfico distingue dos barras solo por color rojo y verde. ¿Qué agregas para que sea accesible?", "Etiquetas con los nombres", "No todas las personas distinguen esos colores."),
    ],
    A=[
        arith("Tu presentación dura 5 minutos y cada diapositiva usa 1 minuto. Dedicas 1 diapositiva al inicio y 1 al cierre. ¿Cuántas diapositivas quedan para el desarrollo?", "5-1-1", "Se restan inicio y cierre del total.", " diapositivas"),
        arith("Un guion tiene 150 palabras para decir en 1 minuto. ¿Cuántas palabras necesitas para una presentación de 4 minutos?", "150*4", "Se multiplica por los minutos.", " palabras"),
        ("Ordena las partes: (a) cierre con aprendizajes, (b) necesidad y usuario, (c) pruebas con datos. ¿Cuál es el orden correcto?", "b, c, a", "Primero la necesidad, luego el desarrollo con datos y al final el cierre."),
    ],
    Z=[
        ("Un grupo tiene 4 minutos y 10 diapositivas. Dani dice: «Hablamos rápido». Elena dice: «Dejamos 4 diapositivas». ¿Quién propone una solución mejor?", "Elena", "Ajusta el contenido al tiempo sin perder claridad."),
        ("Una diapositiva tiene una foto sin descripción y un texto con 12 líneas. Nombra dos cambios para mejorarla.", "Agregar texto alternativo y reducir el texto a 6 líneas o menos", "Mejora la accesibilidad y la legibilidad."),
    ],
    D=[
        arith("Un video de 4 minutos tiene 1 diapositiva de inicio de 30 segundos, 1 de cierre de 30 segundos y el resto del tiempo se reparte en 6 diapositivas iguales. ¿Cuántos segundos dura cada una de las 6?", "(240-30-30)//6", "Se resta lo del inicio y el cierre del total y se divide entre 6.", " segundos"),
        arith("Guion de 5 minutos: 1 de inicio, 3 de desarrollo y 1 de cierre. El grupo se entusiasma y el inicio dura 2 minutos. ¿Cuántos minutos se pasan del total?", "2+3+1-5", "Se suman las tres partes y se resta el tiempo permitido.", " minuto"),
    ],
    ctx=("Debes contar en 5 minutos cómo repararon un cierre. Escribe qué dirías en el inicio, el desarrollo y el cierre (una frase para cada parte) y un texto alternativo para la foto del cierre ya reparado.", "Inicio: el cierre de una mochila no cerraba. Desarrollo: lo reparamos en 20 minutos y lo probamos 10 veces. Cierre: ahora funciona y aprendimos a medir. Texto alternativo: «Cierre de mochila totalmente cerrado»", "Tres partes con una frase y una descripción breve de la imagen."),
    sc=[
        ("¿Cuáles son las tres partes de un guion?", "Inicio, desarrollo y cierre", "Es la estructura de la clase."),
        ("¿Qué haces si pasas del tiempo?", "Acorto el contenido", "No se habla más rápido."),
        ("¿Para qué sirve el texto alternativo?", "Para describir una imagen a quien no puede verla", "Hace el mensaje accesible."),
    ],
    open_task=(
        "Escoge un proceso. Proceso 1: una banca reparada con 2 sesiones de trabajo; tienes 5 minutos. Proceso 2: un estante adaptado a una altura de 80 cm; tienes 4 minutos. Escribe un guion con inicio, desarrollo y cierre (una frase por parte), el reparto de minutos, el número de diapositivas y un texto alternativo para una imagen.",
        "Proceso 2: Inicio: algunos compañeros no alcanzaban el estante (1 minuto). Desarrollo: bajamos el estante a 80 cm y probamos (2 minutos). Cierre: ahora todos alcanzan (1 minuto). 4 diapositivas. Texto alternativo: «Estante de cartón a 80 cm de altura con libros»",
        ["tres partes en orden", "reparte los minutos sin pasarse", "diapositivas acordes al tiempo", "texto alternativo claro"],
        ["hoja con guion, tiempos y texto alternativo"],
        ["pasarse del tiempo", "no describir la imagen"],
        "Pregunta: «¿cuánto dura cada parte?». Si suma más del tiempo, pídele acortar.",
    ),
    reinforce="Ensaya en voz alta durante 1 minuto cómo cuentas la reparación de un objeto, con un reloj o un cronómetro.",
    extend="Explica por qué es mejor mostrar menos cosas bien explicadas que muchas cosas rápidamente.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno. Todo se resuelve en papel.",
    use="Aprenderé a comunicar con ética: citar las fuentes, respetar el trabajo ajeno, cuidar la privacidad y presentar los datos con honestidad. Sirve para que tu trabajo sea confiable y no perjudique a nadie.",
    prior=["Sé que un mensaje tiene objetivo y audiencia.", "Sé que los gráficos deben ser honestos.", "Sé que hay información personal que se protege."],
    explain=[
        "Comunicar con ética significa actuar con honestidad y respeto cuando compartes un proceso. Primero, la honestidad con los datos: se muestran los resultados reales, incluso los que no salieron bien, y los gráficos no se manipulan. Segundo, el respeto al trabajo ajeno: si usas una imagen, un texto, una idea o un dato de otra persona, se anota la fuente, que es de dónde viene. Copiar y presentarlo como propio es plagio.",
        "Muchas obras tienen derechos de autor, es decir, su autora o autor decide cómo se pueden usar. Algunas permiten usarlas si se da crédito; otras no se pueden copiar. Cuando no sabes si puedes usar algo, no lo uses: dibuja tu propia imagen, saca tu propia foto o pide permiso a quien corresponda. Los datos de apoyo se citan con el nombre de la fuente y de qué se trata.",
        "Tercero, la privacidad: no publiques nombres completos, direcciones ni fotos de otras personas sin su permiso y el de su familia, sobre todo si son menores. En vez de fotos de rostros, muestra manos, objetos o dibujos. Si alguien te presiona para compartir algo que te incomoda, o ves algo que te preocupa en línea, avisa a una persona adulta de confianza. Y comenta siempre con respeto, hablando de la solución y no de las personas.",
    ],
    vocab=[("fuente", "origen de una imagen, dato o idea"), ("plagio", "presentar como propio el trabajo de otra persona"), ("derechos de autor", "derechos de quien creó una obra a decidir cómo se usa"), ("privacidad", "derecho a que no se difundan tus datos o los de otras personas sin permiso"), ("crédito", "mención de quién creó algo")],
    worked=[
        ("Detectar un plagio", "Un grupo copia un texto de un sitio sobre puentes y lo presenta sin decir de dónde es. ¿Qué falta?", ["Se usa el trabajo de otra persona sin reconocerlo.", "Falta citar la fuente o escribir el texto con palabras propias y citar igual."], "Citar la fuente del texto"),
        ("Cuidar la privacidad", "Un grupo quiere publicar la foto de un compañero armando un puente, con su nombre completo. ¿Qué hace?", ["Pide permiso al compañero y a su familia antes de publicar.", "Mejor aún: usa una foto solo de las manos y el puente, sin nombre."], "Pedir permiso, o mostrar solo manos y puente sin el nombre"),
    ],
    mistakes=[
        ("Pensar que si algo está en internet se puede usar libremente.", "Muchas obras tienen derechos de autor.", "Pregunta si se puede usar; si no sabes, crea la tuya o pide permiso."),
        ("Publicar una foto de otra persona sin preguntarle.", "No se respeta su privacidad.", "Pide permiso y, si es menor, también a su familia."),
    ],
    R=[
        ("Presentar el trabajo de otra persona como propio, ¿cómo se llama?", "Plagio", "Es la definición del término."),
        ("El origen de una imagen o dato, ¿cómo se llama?", "Fuente", "Se anota para dar crédito."),
        ("Si algo en línea te incomoda, ¿avisas a una persona adulta de confianza o lo guardas en secreto?", "Aviso a una persona adulta de confianza", "Pedir ayuda protege."),
    ],
    C=[
        ("Usaste el gráfico de un libro en tu presentación. ¿Qué haces? A anoto de qué libro lo saqué, B lo presento como mío.", "A", "La fuente se reconoce."),
        ("¿Por qué no se exageran los datos de un proyecto? A porque quien se entera del dato real pierde la confianza, B porque los resultados malos no importan en un informe.", "A", "La honestidad sostiene la confianza."),
        ("¿Cuál foto cuida mejor la privacidad? A manos armando el modelo, B el rostro de un compañero con su nombre y curso.", "A", "A no identifica a nadie."),
    ],
    A=[
        arith("Una presentación tiene 12 datos y 5 de ellos vienen de otras fuentes. ¿Cuántos datos son propios?", "12-5", "Se restan los datos de otras fuentes del total.", " datos"),
        arith("Un grupo cita 3 fuentes por cada uno de 4 temas. ¿Cuántas fuentes anota en total?", "3*4", "Se multiplica por los temas.", " fuentes"),
        ("Un compañero te envía su foto con una amiga y te pide que no la compartas, pero tu informe necesita una foto de personas. ¿Qué haces?", "Uso otra foto o dibujo que no identifique a nadie", "Respetas su privacidad."),
    ],
    Z=[
        ("Una compañera dice: «Si lo copio y cambio dos palabras, ya es mío». ¿Tiene razón?", "No", "Sigue siendo el trabajo de otra persona; hay que citar la fuente."),
        ("Un gráfico muestra tu proyecto con una barra más alta de lo real para que se vea mejor. Otro compañero te pide corregirlo. ¿Quién actúa con ética?", "El compañero que pide corregirlo", "Los datos deben ser verdaderos."),
    ],
    D=[
        arith("El informe tiene 20 imágenes: 8 son fotos propias, 6 son dibujos propios y las demás vienen de otras fuentes. ¿Cuántas fuentes hay que citar?", "20-8-6", "Se restan las propias del total.", " imágenes"),
        ("Un proyecto tiene 6 fotos: 2 con rostros de compañeros, 3 de objetos y 1 de manos. Si no hay permiso, ¿cuántas se pueden publicar sin pedir permiso a nadie?", "4", "Se pueden publicar las 3 de objetos y la de manos; las de rostros necesitan permiso."),
    ],
    ctx=("Terminaste el informe de la reparación de una banca. Usaste una imagen de un libro de Tecnología y una foto de un compañero armando la banca, con su rostro. Escribe qué anotas sobre la imagen del libro y qué haces con la foto del compañero.", "Anoto el nombre del libro y su autora o autor como fuente. Con la foto, pido permiso al compañero y a su familia, o la cambio por una de las manos y la banca", "Se cita la fuente y se protege la privacidad."),
    sc=[
        ("En Tecnología: ¿Qué es el plagio?", "Presentar como propio el trabajo de otra persona", "No se reconoce a quien lo hizo."),
        ("¿Qué haces si algo en línea te preocupa?", "Aviso a una persona adulta de confianza", "Se busca ayuda."),
        ("¿Cómo comentas el trabajo de otras personas?", "Con respeto, hablando de la solución", "No se ataca a las personas."),
    ],
    open_task=(
        "Escoge un informe. Informe 1: una presentación sobre una banca reparada, con 1 texto copiado de un libro, 1 foto de un compañero y un gráfico con eje que empieza en 50. Informe 2: un afiche sobre un estante adaptado, con 1 dibujo copiado de una revista, 1 foto de un vecino y un dato que nadie midió. Escribe tres cambios éticos, uno por cada problema, y una frase respetuosa para comentar el trabajo de otra persona.",
        "Informe 1: citar el libro; pedir permiso o cambiar la foto por una de manos; corregir el eje a cero. Comentario: «el gráfico se entiende mejor si el eje parte en cero»",
        ["tres cambios, uno por problema", "cita la fuente", "cuida la privacidad", "comentario respetuoso sobre la solución"],
        ["hoja con cambios y comentario"],
        ["no citar fuentes", "criticar a la persona y no a la solución"],
        "Pregunta: «¿de dónde viene este dato o imagen?». Si no se sabe, pídele no usarlo.",
    ),
    reinforce="Haz una lista de tres cosas que debes anotar si usas la imagen de otra persona en un trabajo.",
    extend="Explica por qué es mejor usar tus propios dibujos o fotos cuando no sabes si puedes usar los de otras personas.",
)
