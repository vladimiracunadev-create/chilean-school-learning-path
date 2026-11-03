"""Cuaderno del estudiante, 8.º básico Tecnología: OA 04 (comunicación ética del proceso tecnológico con herramientas TIC), clases 1 a 4.

Seguridad y privacidad: no se publican datos personales, rostros ni nombres reales; toda tarea tiene alternativa en papel; las herramientas se nombran por tipo (procesador de texto, presentación, planilla, diagrama), no por marca.
Cifras enteras. Los casos, las referencias y los datos son inventados («de ejemplo»). Las cifras de ritmo de habla y de tamaño de letra son reglas de ejemplo, no normas.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA. No se enseña derecho de autor con detalle legal: queda para el docente.
"""
from __future__ import annotations

from student_content_te8_a import reg
from student_lessons import arith, ex

OA4 = "TE08 OA 04"

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a decidir qué quiero lograr al comunicar un proceso tecnológico y a quién se lo explico, y a adaptar formato, lenguaje y tiempo. Sirve para que tu mensaje sea entendido por quien lo recibe.",
    prior=["Sé qué etapas tiene un proceso de diseño.", "Sé calcular tiempos simples.", "Sé que los datos no se cambian al comunicarlos."],
    explain=[
        "Comunicar un proceso tecnológico es contar cómo se pasó de una necesidad a un producto. Antes de elegir el formato se definen dos cosas. La primera es el objetivo: informar (explicar qué se hizo), instruir (enseñar los pasos para hacerlo), persuadir (convencer de apoyar o decidir algo) o documentar (dejar un registro para quien evalúa). La segunda es la audiencia, es decir, las personas que recibirán el mensaje.",
        "De la audiencia importan su edad, lo que ya sabe, lo que le interesa, el tiempo que tiene y sus necesidades de acceso: algunas personas necesitan letra grande, otras escuchan mejor que leen. Con eso se decide el formato (afiche, informe, presentación, video corto), el lenguaje (técnico o cotidiano), el nivel de detalle y la duración. Se define también el mensaje central: la idea que la audiencia debe recordar, en una frase.",
        "Al adaptar un mensaje a otra audiencia cambian la forma y el lenguaje, pero nunca los hechos ni los datos. Dos versiones del mismo proceso deben decir lo mismo en lo esencial. Un ritmo de habla de ejemplo es de unas 120 palabras por minuto; sirve para calcular cuánto texto cabe en el tiempo.",
    ],
    vocab=[("audiencia", "personas a quienes se dirige el mensaje"), ("objetivo comunicativo", "lo que se quiere lograr con el mensaje"), ("mensaje central", "idea que la audiencia debe recordar"), ("formato", "forma del mensaje: afiche, informe, presentación, video"), ("persuadir", "convencer a alguien de apoyar o decidir algo")],
    worked=[
        ("Reconocer el objetivo", "Un afiche dice «¡Firma hoy para tener luz en nuestro pasaje!». ¿Qué objetivo tiene?", ["Pide una acción a las personas: firmar.", "Busca convencer, no solo contar."], "Persuadir"),
        ("Adaptar a dos audiencias", "El equipo probó 3 soportes de libros: A soportó 12 libros, B 15 y C 18. Explícalo a un curso de 8.º y a los vecinos de una sede.", ["Al curso: tabla con los datos y comparación en 5 minutos.", "A los vecinos: un afiche con una foto y la frase «el soporte C aguanta 18 libros». Los datos son los mismos."], "Cambian el formato y el lenguaje; los datos no cambian"),
    ],
    mistakes=[
        ("Usar el mismo mensaje y formato para cualquier audiencia.", "Lo que entiende un curso técnico puede no entenderlo quien no conoce el tema.", "Define primero quién te escucha y qué necesita."),
        ("Cambiar los datos para que suenen mejor ante otra audiencia.", "Adaptar es cambiar la forma, no la verdad.", "Mantén los hechos y adapta el lenguaje y el formato."),
    ],
    R=[
        ("Un manual con los pasos para armar un soporte, ¿informa, instruye o persuade?", "Instruye", "Enseña paso a paso cómo hacer algo."),
        ("La audiencia, ¿son las personas a quienes va dirigido el mensaje o quienes lo escribieron?", "Las personas a quienes va dirigido", "Es quien recibe el mensaje."),
        ("El mensaje central, ¿es una frase que la audiencia debe recordar o el título más largo?", "Una frase que la audiencia debe recordar", "Resume la idea principal."),
    ],
    C=[
        ("Un grupo quiere que una junta de vecinos apruebe $30.000 para luminarias. ¿Cuál es su objetivo? A) persuadir B) instruir", "A", "Busca convencer para que se tome una decisión."),
        ("Se explica una maqueta a niños de 1.º básico. ¿Qué conviene? A) imágenes y palabras simples B) tablas con porcentajes", "A", "La audiencia es pequeña y entiende mejor con imágenes y palabras conocidas."),
        ("Al adaptar el mensaje para otra audiencia, ¿qué no se debe cambiar? A) los datos y los hechos B) el lenguaje", "A", "El lenguaje se adapta; los hechos se mantienen."),
    ],
    A=[
        arith("Una presentación dura 10 minutos: 2 de introducción y 1 de cierre; el resto es desarrollo con una diapositiva por minuto. ¿Cuántas diapositivas de desarrollo hay?", "10-2-1", "Se restan la introducción y el cierre del tiempo total.", " diapositivas"),
        arith("Una charla de 5 minutos se habla a unas 120 palabras por minuto (cifra de ejemplo). ¿Cuántas palabras tiene el guion?", "5*120", "Se multiplica el ritmo por los minutos.", " palabras"),
        ("Asigna el objetivo (I informar, T instruir, P persuadir): (1) «Primero marca la línea; segundo, dobla el cartón», (2) «¡Firma hoy para tener luz en nuestro pasaje!», (3) «Probamos 3 prototipos y el mejor soportó 40 monedas».", "1 T, 2 P, 3 I", "El primero da pasos, el segundo pide una acción y el tercero cuenta lo que se hizo."),
    ],
    Z=[
        ("El resultado es «el prototipo B soporta 25 % más que el A». Para vecinos sin conocimientos técnicos, ¿qué versión conviene? A) «el soporte nuevo aguanta un cuarto más de peso que el anterior» B) «el prototipo B presenta una mejora de 25 % en resistencia a la carga»", "A", "La primera usa un lenguaje cotidiano y dice lo mismo."),
        ("Un grupo presenta ante personas con baja visión solo gráficos, sin explicarlos con palabras. ¿Qué falló? A) no consideró las necesidades de acceso de su audiencia B) usó demasiados colores", "A", "Debía describir los datos en voz alta o en un texto accesible."),
    ],
    D=[
        arith("En un panel, 4 equipos tienen 22 minutos en total y hay 3 cambios de equipo de 2 minutos cada uno. ¿Cuántos minutos puede hablar cada equipo?", "(22-3*2)//4", "Se restan los cambios y se reparte el resto entre los equipos.", " minutos"),
        ("Hay 60 vecinos reunidos en una plaza sin proyector y 3 minutos para persuadirlos. ¿Qué formato conviene? A) un afiche grande con un mensaje y una cifra B) una presentación de 20 diapositivas C) un informe de 10 páginas", "A", "Sin proyector y con poco tiempo se necesita un formato visible y breve."),
    ],
    ctx=ex("Para un video corto de 3 minutos sobre tu soporte, hablarás a 120 palabras por minuto (cifra de ejemplo). ¿Cuántas palabras debe tener tu guion?", "360 palabras", "Se multiplica 3 × 120 = 360.", calc="3*120"),
    sc=[
        ("¿Cuáles son los cuatro objetivos comunicativos de la clase?", "Informar, instruir, persuadir y documentar", "Son los propósitos posibles de un mensaje."),
        ("¿Qué se adapta al cambiar de audiencia?", "El formato, el lenguaje y el detalle", "Los hechos y los datos no cambian."),
        ("¿Qué es el mensaje central?", "La idea que la audiencia debe recordar", "Se resume en una frase."),
    ],
    open_task=(
        "Usa este proceso de ejemplo: un equipo probó tres cobertores de cartón para proteger las esquinas de una mesa de jardín infantil; el cobertor A resistió 10 golpes de prueba con una bolita de papel antes de aplastarse, el B resistió 14 y el C resistió 18; C cuesta $2.000 y A $1.200. Escribe el mensaje central y el plan para dos audiencias: (1) los compañeros de curso (informar, 5 minutos) y (2) las educadoras del jardín (persuadir, un afiche). Para cada una indica objetivo, formato, lenguaje y tiempo.",
        "Mensaje central: el cobertor C protege mejor, con un costo razonable. Curso: informar, presentación de 5 minutos con tabla de datos. Educadoras: persuadir, afiche con foto y la frase «el cobertor C resiste 18 golpes»",
        ["define el mensaje central", "indica objetivo y formato para cada audiencia", "adapta el lenguaje", "mantiene los mismos datos"],
        ["plan escrito para dos audiencias"],
        ["usar el mismo formato para ambas audiencias", "cambiar los datos entre versiones"],
        "Pregunta: «¿qué datos aparecen en las dos versiones?». Deben ser los mismos.",
    ),
    reinforce="Explica en dos frases a una persona de tu casa qué hace tu objeto favorito, y luego en dos frases distintas para un niño pequeño.",
    extend="Explica por qué cambiar los datos para convencer mejor deja de ser comunicar con ética.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y las tablas escritas en este cuaderno.",
    use="Aprenderé a elegir la herramienta TIC y el gráfico adecuados para comunicar datos de un proceso, y a armar diapositivas legibles. Sirve para mostrar tus datos con claridad y sin confundir.",
    prior=["Sé calcular porcentajes.", "Sé leer una tabla.", "Sé que cada herramienta TIC sirve para algo distinto."],
    explain=[
        "Cada formato tiene una herramienta. Un procesador de texto sirve para informes e instructivos; una presentación, para mostrar un tema a un grupo; una planilla, para ordenar datos, calcular y hacer gráficos; un programa de diagramas, para dibujar los pasos de un proceso con flechas. Para trabajar en equipo conviene un documento compartido, con permisos de ver, comentar o editar, y guardar versiones.",
        "El gráfico se elige según lo que se quiere mostrar. El gráfico de barras compara categorías. El de líneas muestra cómo cambia algo en el tiempo. El circular muestra las partes de un todo, y sus porcentajes deben sumar 100 %. Todo gráfico lleva un título, ejes con sus unidades y una leyenda si tiene varias series.",
        "Una diapositiva legible tiene una sola idea principal, pocas líneas (la regla de ejemplo es hasta 6), letra grande (24 puntos o más) y buen contraste entre el texto y el fondo. Las diapositivas son apoyo: el detalle va en la voz o en el informe, no en un párrafo largo.",
    ],
    vocab=[("planilla de cálculo", "herramienta que ordena datos, calcula y grafica"), ("gráfico de barras", "compara categorías"), ("gráfico de líneas", "muestra cambios en el tiempo"), ("gráfico circular", "muestra las partes de un todo"), ("leyenda", "explicación de los colores o series de un gráfico")],
    worked=[
        ("Elegir el gráfico", "Se quiere mostrar cómo bajó el tiempo de armado en 5 semanas. ¿Qué gráfico sirve?", ["Se trata de un cambio a lo largo del tiempo.", "El gráfico de líneas une los puntos semana a semana."], "Gráfico de líneas"),
        ("Calcular los porcentajes de un gráfico circular", "En 40 fallas de ejemplo hubo 20 por pegado, 10 por corte, 6 por medidas y 4 por uso. ¿Qué porcentajes lleva el gráfico circular?", ["Cada porcentaje es la parte × 100 ÷ 40.", "20 → 50 %, 10 → 25 %, 6 → 15 %, 4 → 10 %. La suma es 100 %."], "50 %, 25 %, 15 % y 10 %"),
    ],
    mistakes=[
        ("Poner un párrafo largo en una diapositiva.", "Nadie lo alcanza a leer y se pierde la idea principal.", "Una idea por diapositiva y el detalle en la voz."),
        ("Usar un gráfico circular cuando los datos no forman un total.", "El gráfico circular solo muestra partes de un todo.", "Usa barras para comparar categorías independientes."),
    ],
    R=[
        ("Para mostrar cómo cambió el tiempo de armado semana a semana, ¿qué gráfico conviene: de líneas o circular?", "De líneas", "Muestra un cambio a lo largo del tiempo."),
        ("Para mostrar qué parte del total de fallas corresponde a cada causa, ¿conviene un gráfico circular o de líneas?", "Circular", "Muestra las partes de un todo."),
        ("En una diapositiva, ¿cuántas ideas principales conviene poner: una o diez?", "Una", "Así la audiencia recuerda lo principal."),
    ],
    C=[
        ("Un gráfico de barras no tiene título, ni unidades en el eje, ni leyenda. ¿Qué problema tiene? A) no se entiende qué mide ni en qué unidad B) usa demasiadas barras", "A", "Sin título ni unidades, el lector no sabe qué se está mostrando."),
        ("Varias personas deben escribir juntas un informe. ¿Qué conviene? A) un documento compartido con permisos B) enviar copias por separado y juntarlas al final", "A", "Todas editan el mismo archivo y se evitan versiones distintas."),
        ("Un gráfico circular muestra 40 %, 35 % y 15 %. ¿Está bien armado?", "No", "Los porcentajes suman 90 %, no 100 %."),
    ],
    A=[
        arith("Fallas de ejemplo: pegado 9, corte 6, medidas 3 y uso 2. ¿Qué porcentaje del total son las de corte, para el gráfico circular?", "6*100//(9+6+3+2)", "Se divide la parte entre el total de 20 fallas y se multiplica por 100.", " %"),
        arith("Una planilla muestra los tiempos de armado de 5 semanas: 50, 46, 43, 41 y 40 minutos. ¿Cuánto bajó el tiempo entre la primera y la última semana?", "50-40", "Se resta el último valor del primero.", " minutos"),
        ("Asigna la herramienta (Pl planilla, Pr presentación, Di diagrama de flujo): (1) calcular promedios y graficarlos, (2) mostrar el resultado al curso, (3) dibujar los pasos del proceso con flechas.", "1 Pl, 2 Pr, 3 Di", "Cada herramienta resuelve mejor una de las tareas."),
    ],
    Z=[
        ("Un gráfico de líneas une las fallas de tres causas distintas (pegado, corte y uso) como si fueran semanas. ¿Qué error tiene? A) la línea sugiere un cambio en el tiempo entre categorías que no tienen orden B) tiene pocos datos", "A", "Las categorías no forman una secuencia, por lo que conviene un gráfico de barras."),
        ("Una diapositiva tiene un párrafo de 14 líneas con letra pequeña, para 30 personas en una sala. ¿Cuál es la mejor corrección? A) dividirla en tres diapositivas con una idea cada una y letra grande B) leer el párrafo más rápido", "A", "Una idea por diapositiva y letra grande hacen el mensaje legible."),
    ],
    D=[
        ("Presupuesto de $20.000: material $9.000, transporte $5.000 e imprevistos $6.000. ¿Qué porcentajes lleva el gráfico circular, en ese orden?", "45 %, 25 % y 30 %", "9.000 ÷ 20.000 es 45 %, 5.000 ÷ 20.000 es 25 % y 6.000 ÷ 20.000 es 30 %."),
        ("Tiempo de armado del equipo A en 4 semanas: 50, 45, 40, 35 minutos. Equipo B: 48, 46, 44, 42. ¿Qué equipo bajó más entre la primera y la cuarta semana y cuánto?", "El equipo A, 15 minutos contra 6", "A bajó 50 − 35 = 15 minutos y B bajó 48 − 42 = 6 minutos."),
    ],
    ctx=ex("En una encuesta de ejemplo a 40 personas sobre qué mejorar en la plaza, 20 pidieron más señalética, 12 más sombra y 8 más bancas. ¿Qué porcentaje pidió sombra para el gráfico?", "30 %", "Se calcula 12 × 100 ÷ 40 = 30.", calc="12*100//40"),
    sc=[
        ("¿Qué gráfico muestra las partes de un todo?", "El circular", "Sus porcentajes suman 100 %."),
        ("¿Qué debe llevar todo gráfico?", "Título, ejes con unidades y leyenda si tiene varias series", "Así se entiende lo que mide."),
        ("¿Para qué sirve un documento compartido?", "Para que varias personas trabajen en el mismo archivo", "Evita tener versiones distintas."),
    ],
    open_task=(
        "Con estos datos de ejemplo prepara la comunicación de un proceso. Tiempo de armado en 4 semanas: 52, 47, 44 y 40 minutos. Fallas por causa en 40 pruebas: pegado 16, corte 12, medidas 8, uso 4. Elige el gráfico adecuado para cada dato y justifícalo, calcula los porcentajes del gráfico circular, y escribe cómo sería una diapositiva con título, una idea principal y una descripción para quien no puede ver el gráfico.",
        "Tiempo: gráfico de líneas porque cambia en el tiempo (bajó 12 minutos). Fallas: circular, con 40 %, 30 %, 20 % y 10 %. Diapositiva: título «El tiempo de armado bajó 12 minutos», idea principal, y descripción en voz alta de los valores",
        ["elige y justifica los gráficos", "calcula los porcentajes y suman 100 %", "diseña una diapositiva con una idea", "agrega una descripción accesible"],
        ["tabla de decisiones y boceto de diapositiva"],
        ["usar un circular para datos en el tiempo", "olvidar el título y las unidades"],
        "Pregunta: «¿qué quieres que vea la audiencia en este gráfico?». Debe coincidir con el tipo de gráfico.",
    ),
    reinforce="Anota durante 4 días cuántas veces usas tu celular o tu computador por tareas, y elige el gráfico que mejor muestre el cambio día a día.",
    extend="Explica por qué un gráfico sin unidades en el eje puede llevar a conclusiones equivocadas.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a planificar un mensaje con mensaje central, esquema de diapositivas, guion y reparto del tiempo, y a revisar que sea accesible. Sirve para presentar un proceso en el tiempo que tienes y para que todas las personas puedan entenderlo.",
    prior=["Sé definir objetivo y audiencia.", "Sé elegir un gráfico adecuado.", "Sé calcular tiempos."],
    explain=[
        "Un mensaje se planifica en orden: primero se define la audiencia y el mensaje central; luego se hace el esquema de diapositivas, con un título, una idea y una imagen por diapositiva; después se escribe el guion, que es el texto de lo que se dirá; se ensaya cronometrando; y por último se revisa la accesibilidad y se piden comentarios a dos personas.",
        "La estructura tiene una introducción (saludo, problema y objetivo), un desarrollo (necesidad, diseño, pruebas y resultados) y un cierre (conclusión y qué sigue). El tiempo se reparte entre las partes antes de escribir. Con un ritmo de ejemplo de 120 palabras por minuto se calcula cuántas palabras caben.",
        "La accesibilidad significa que personas distintas puedan entender el mensaje. Se usa un buen contraste entre el texto y el fondo, no se transmite información solo con color, las imágenes y los gráficos llevan un texto alternativo que los describe, los videos tienen subtítulos o transcripción, y siempre existe una versión en papel.",
    ],
    vocab=[("guion", "texto de lo que se va a decir"), ("esquema de diapositivas", "plan con título, idea e imagen de cada diapositiva"), ("texto alternativo", "descripción escrita de una imagen o gráfico"), ("accesibilidad", "posibilidad de que todas las personas entiendan el mensaje"), ("cronometrar", "medir con reloj cuánto dura un ensayo")],
    worked=[
        ("Repartir el tiempo", "Una exposición de 10 minutos tiene introducción de 1, necesidad de 2, diseño de 2, pruebas de 3 y cierre. ¿Cuánto dura el cierre?", ["Sumo lo asignado: 1 + 2 + 2 + 3 = 8.", "Resto del total: 10 − 8."], "2 minutos"),
        ("Escribir un texto alternativo", "Un gráfico de barras muestra que el prototipo A sostiene 12 monedas y el B, 18. Escribe un texto alternativo.", ["Debe decir qué tipo de gráfico es y qué compara.", "Debe incluir los datos principales."], "Gráfico de barras que compara dos prototipos: A sostiene 12 monedas y B sostiene 18"),
    ],
    mistakes=[
        ("Dejar la accesibilidad para el final y no revisarla.", "Si falla, hay que rehacer diapositivas.", "Revisa contraste, texto alternativo y alternativa en papel mientras planificas."),
        ("Escribir el guion sin calcular cuánto cabe en el tiempo.", "La exposición queda demasiado larga o corta.", "Calcula las palabras con el ritmo de habla y cronometra un ensayo."),
    ],
    R=[
        ("La introducción, ¿presenta el problema y el objetivo o muestra las conclusiones finales?", "Presenta el problema y el objetivo", "Prepara a la audiencia para lo que sigue."),
        ("El texto alternativo de un gráfico, ¿describe lo que muestra o solo lo decora?", "Describe lo que muestra", "Permite entenderlo a quien no lo ve."),
        ("Un guion, ¿contiene lo que se va a decir o solo los dibujos?", "Lo que se va a decir", "Es el texto de la exposición."),
    ],
    C=[
        ("Un gráfico distingue dos series solo con rojo y verde. ¿Qué problema tiene para algunas personas con daltonismo? A) no pueden distinguir las series B) el gráfico queda muy grande", "A", "No se debe transmitir información solo con color."),
        ("Un video sin subtítulos, ¿para quién es menos accesible? A) personas sordas o que no pueden oír bien B) personas con vista normal", "A", "No reciben la información hablada."),
        ("¿Qué debe hacer el cierre? A) resumir el resultado y decir qué sigue B) presentar un tema completamente nuevo", "A", "El cierre refuerza el mensaje central."),
    ],
    A=[
        arith("En una charla de 12 minutos: introducción 1, necesidad 2, diseño 3 y pruebas 3. ¿Cuántos minutos quedan para el cierre?", "12-1-2-3-3", "Se restan los tiempos asignados del total.", " minutos"),
        arith("Un guion tiene 720 palabras y se habla a 120 palabras por minuto (cifra de ejemplo). ¿Cuántos minutos dura?", "720//120", "Se divide el total de palabras entre el ritmo.", " minutos"),
        arith("Cada diapositiva de una presentación toma 90 segundos y hay 6 diapositivas. ¿Cuántos minutos dura?", "90*6//60", "Se calculan los segundos totales y se pasan a minutos.", " minutos"),
    ],
    Z=[
        ("Un guion de 900 palabras debe caber en 6 minutos a 120 palabras por minuto (cifra de ejemplo). ¿Cabe y cuántas palabras sobran o faltan?", "No cabe: sobran 180 palabras", "En 6 minutos caben 720 palabras y 900 − 720 = 180."),
        ("Una diapositiva dice «en rojo lo malo, en verde lo bueno» y no tiene otra marca. ¿Cómo se corrige? A) agregar etiquetas de texto o símbolos además del color B) cambiar a colores más fuertes", "A", "La información no debe depender solo del color."),
    ],
    D=[
        arith("Un equipo de 4 expone durante 14 minutos: 2 minutos de introducción y cierre en conjunto, y el resto se reparte en partes iguales. ¿Cuántos minutos habla cada uno en el desarrollo?", "(14-2)//4", "Se restan los minutos conjuntos y se reparte el resto.", " minutos"),
        ("Según el orden de la clase, ordena estos pasos: (a) ensayar y cronometrar, (b) escribir el guion, (c) definir audiencia y mensaje central, (d) hacer el esquema de diapositivas.", "c, d, b, a", "Primero se define el mensaje, luego se esquematiza, después se escribe y al final se ensaya."),
    ],
    ctx=ex("Preparas una exposición de 5 minutos, a 120 palabras por minuto (cifra de ejemplo), y tu guion tiene 540 palabras. ¿Cabe y cuántas palabras de margen quedan?", "Sí cabe, con 60 palabras de margen", "En 5 minutos caben 600 palabras y 600 − 540 = 60.", calc="5*120-540"),
    sc=[
        ("En Tecnología: ¿Qué es un guion?", "El texto de lo que se va a decir", "Se escribe después del esquema."),
        ("¿Qué es el texto alternativo?", "Una descripción escrita de una imagen o gráfico", "Sirve a quien no puede ver la imagen."),
        ("¿Por qué se cronometra un ensayo?", "Para comprobar que cabe en el tiempo", "Se ajusta el guion si es necesario."),
    ],
    open_task=(
        "Planifica una exposición de 8 minutos para estudiantes de 6.º básico sobre este proceso de ejemplo: un soporte de cartón para libros que mejoró de 12 a 18 libros sostenidos tras reforzar la base. Escribe el mensaje central, el reparto de tiempo (introducción, necesidad, diseño, pruebas y cierre, sumando 8 minutos), el esquema de 5 diapositivas (título e idea), el texto alternativo de un gráfico de barras con los datos 12 y 18, y las primeras dos oraciones del guion.",
        "Mensaje: reforzar la base hizo que el soporte sostuviera 6 libros más. Tiempo: 1 + 1 + 2 + 3 + 1 = 8. Texto alternativo: gráfico de barras que compara la base original (12 libros) con la base reforzada (18 libros)",
        ["define el mensaje central", "reparte el tiempo y suma 8 minutos", "arma un esquema de 5 diapositivas", "escribe un texto alternativo con los datos", "redacta un inicio de guion claro"],
        ["plan de la exposición"],
        ["repartir un tiempo que no suma el total", "texto alternativo sin datos"],
        "Pregunta: «¿cuánto suma tu reparto de tiempo?». Debe dar 8 minutos.",
    ),
    reinforce="Cronometra cuánto demoras en explicar en voz alta cómo se arma un objeto sencillo de tu casa y ajusta tu explicación a 1 minuto.",
    extend="Explica por qué la accesibilidad conviene planificarla desde el comienzo y no al final.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a comunicar con ética: citar fuentes y respetar la autoría, cuidar la privacidad de las personas, mostrar los datos con honestidad y reconocer el trabajo de todos. Sirve para que tu trabajo sea confiable y no perjudique a nadie.",
    prior=["Sé comunicar un proceso con un objetivo y una audiencia.", "Sé elegir un gráfico adecuado.", "Sé calcular porcentajes."],
    explain=[
        "Comunicar con ética tiene tres partes. La autoría: lo que otra persona creó, como un texto, una imagen o un dato, se cita con su autor, título, año y lugar donde lo consultaste; copiarlo sin citar se llama plagio. Para usar una obra se pide permiso o se elige material cuya licencia lo permita, respetando sus condiciones, por ejemplo nombrar al autor. También se declara si se usaron plantillas o herramientas automáticas, y se revisa lo que producen.",
        "La privacidad: no se muestran rostros, nombres, voces, direcciones ni datos de otras personas sin su permiso, y en el caso de menores, sin el permiso de su persona adulta responsable. Se muestra solo lo necesario. Si alguien te incomoda o publica algo tuyo sin tu permiso, avisa a una persona adulta de confianza.",
        "La honestidad: se muestran todos los datos relevantes, también los desfavorables, y no se inventan resultados. Un gráfico engaña si cambia el comienzo del eje para exagerar una diferencia: dos barras de 80 y 100 parecen una el triple de la otra si el eje parte de 70, aunque en realidad la segunda es solo 25 % mayor. Además se reconoce el trabajo de cada integrante del equipo.",
    ],
    vocab=[("plagio", "presentar como propio algo que creó otra persona"), ("cita", "mención de autor, título, año y lugar de una fuente"), ("licencia", "condiciones con que el autor permite usar su obra"), ("consentimiento", "permiso de la persona para mostrar algo suyo"), ("eje truncado", "eje que no parte de cero y exagera diferencias")],
    worked=[
        ("Detectar un gráfico engañoso", "Dos barras valen 80 y 100, pero el eje parte de 70 y se dibujan con alturas 10 y 30. ¿Qué parece y qué es en realidad?", ["Parece que la segunda es el triple de la primera: 30 ÷ 10 = 3.", "En realidad la diferencia es 20 sobre 80, o sea 25 %."], "Parece el triple, pero solo es 25 % mayor"),
        ("Citar una fuente", "Usaste un texto de ejemplo de Marta Rojas, titulado «Cartones resistentes», del año 2022, que leíste en la biblioteca del colegio. ¿Cómo lo citas?", ["Reúno autor, año, título y lugar.", "Los escribo en una línea."], "Rojas, M. (2022). Cartones resistentes. Biblioteca del colegio"),
    ],
    mistakes=[
        ("Pensar que lo que está en internet se puede usar sin citar.", "Cada obra tiene un autor y condiciones de uso.", "Cita siempre y usa solo material con permiso o licencia."),
        ("Mostrar solo los resultados favorables.", "Esconde información relevante y engaña a quien lee.", "Muestra todos los resultados y explica los desfavorables."),
    ],
    R=[
        ("Copiar un párrafo de un sitio y presentarlo como propio, ¿es citar o plagiar?", "Plagiar", "Se presenta como propio algo que creó otra persona."),
        ("Antes de usar la foto de un compañero en una presentación pública, ¿qué debes hacer: pedir su permiso o suponer que no le molestará?", "Pedir su permiso", "Se necesita su consentimiento; si es menor, también el de su persona adulta responsable."),
        ("Mostrar solo los resultados favorables y esconder los desfavorables, ¿es honesto o engañoso?", "Engañoso", "Se oculta información relevante."),
    ],
    C=[
        ("¿Cuál referencia tiene autor, año, título y lugar? A) Rojas, M. (2022). Cartones resistentes. Biblioteca del colegio B) un libro sobre cartón que vi", "A", "La primera tiene los cuatro datos; la segunda no permite encontrar la fuente."),
        ("Un afiche usa una imagen creada con una herramienta automática y no lo dice. ¿Qué falta? A) indicar que la imagen fue generada con una herramienta automática B) hacerla más grande", "A", "Se declara qué herramientas se usaron."),
        ("Un video va a mostrar la fachada de una casa con el número visible y el nombre del buzón. ¿Qué conviene? A) evitar mostrar o difuminar esos datos B) subirlo igual porque es una casa", "A", "Esos datos permiten identificar a quienes viven ahí."),
    ],
    A=[
        arith("Dos barras valen 60 y 90, pero el eje parte de 50 y se dibujan con alturas 10 y 40. ¿Cuántas veces más alta se ve la segunda?", "(90-50)//(60-50)", "Se dividen las alturas dibujadas: 40 ÷ 10.", " veces"),
        arith("Con las mismas barras de 60 y 90, ¿qué porcentaje mayor es realmente la segunda?", "(90-60)*100//60", "Se calcula la diferencia real sobre el valor menor.", " %"),
        ("Clasifica la falta (A autoría, P privacidad, H honestidad de datos): (1) copiar un texto sin citar, (2) mostrar rostros sin permiso, (3) cortar el eje de un gráfico para exagerar.", "1 A, 2 P, 3 H", "Cada una daña un aspecto distinto de la comunicación ética."),
    ],
    Z=[
        ("Un prototipo tuvo 7 aciertos en 10 pruebas, pero el informe dice «el prototipo funcionó siempre». ¿Es honesto?", "No", "Afirma algo que los datos contradicen."),
        ("Una imagen tiene una licencia que permite usarla si se nombra al autor. Un grupo la usa sin nombrarlo. ¿Respetó la licencia?", "No", "La condición era nombrar al autor."),
    ],
    D=[
        ("Dos barras valen 100 y 125, y el eje parte de 75. ¿Cuántas veces más alta se ve la segunda y qué porcentaje mayor es realmente?", "Se ve el doble, pero es 25 % mayor", "Las alturas son 25 y 50, y la diferencia real es 25 sobre 100."),
        arith("Un trabajo usó 5 fuentes y citó solo 2. Además usó un gráfico con el eje cortado sin avisar. Se descuenta 1 punto por cada fuente no citada y 1 por el gráfico. ¿Cuántos puntos se descuentan?", "(5-2)+1", "Se suman las tres fuentes sin citar y el gráfico.", " puntos"),
    ],
    ctx=ex("Una compañera ve su foto en tu diapositiva y te dice que no quiere que se muestre. ¿Qué debes hacer?", "Quitar la foto de inmediato y confirmarle que ya no está", "Se respeta su decisión sobre su imagen."),
    sc=[
        ("¿Qué datos lleva una cita sencilla?", "Autor, título, año y lugar donde se consultó", "Permiten encontrar la fuente."),
        ("¿Qué se debe tener para mostrar a una persona en un trabajo?", "Su consentimiento", "Es su imagen y sus datos."),
        ("¿Qué es un eje truncado?", "Un eje que no parte de cero y exagera diferencias", "Puede engañar a quien mira el gráfico."),
    ],
    open_task=(
        "Revisa este borrador de ejemplo y escribe cada problema ético con su corrección. Borrador: un texto copiado de un sitio sin indicar autor; la foto de Daniela, de 11 años, con su nombre completo y su colegio; un gráfico con el eje que parte de 90 para comparar 95 y 100; la frase «todos los prototipos funcionaron», aunque 2 de 10 fallaron; y una imagen sacada de un sitio sin saber si se puede usar.",
        "Texto copiado: citar autor, título, año y lugar; foto de Daniela: pedir permiso a su persona adulta responsable y no mostrar nombre ni colegio; gráfico: partir el eje en cero; frase: decir que 8 de 10 funcionaron; imagen: pedir permiso o usar material con licencia y citar",
        ["identifica los cinco problemas", "propone una corrección para cada uno", "distingue autoría, privacidad y honestidad", "usa los datos del ejemplo"],
        ["lista de problemas y correcciones"],
        ["omitir algún problema", "proponer correcciones sin explicar"],
        "Pregunta: «¿a quién podría perjudicar o engañar esto?». Ayuda a ver el problema ético.",
    ),
    reinforce="Revisa un trabajo propio de otra asignatura y anota si citaste todas las fuentes que usaste.",
    extend="Explica por qué respetar la privacidad en un trabajo escolar también cuida la seguridad de las personas.",
)
