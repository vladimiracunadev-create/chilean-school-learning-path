"""Cuaderno del estudiante, 7.º básico Tecnología: OA 02 (diseño e implementación eficiente de soluciones), clases 1 a 5.

Seguridad: solo papel, cartón, cinta, cordel, pegamento en barra y tijeras de punta roma. En la clase de energía solo se leen etiquetas y se calcula: no se abren ni se reparan aparatos conectados a la red eléctrica.
Cifras enteras. La tarifa de energía y los tamaños de archivos son de ejemplo, para practicar.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te7_a import reg
from student_lessons import arith

OA2 = "TE07 OA 02"

# ------------------------------------------------------------------ OA 02, clase 1
reg(
    OA2, 1,
    materials="Hoja, lápiz, regla y las medidas escritas en este cuaderno. Si quieres practicar, una hoja cuadriculada o papel reutilizable.",
    use="Aprenderé a usar los materiales de forma eficiente: calcular cuántas piezas salen de una plancha, medir el desperdicio y elegir materiales reutilizados. Sirve para gastar menos y botar menos.",
    prior=["Sé calcular áreas de rectángulos.", "Sé que una restricción es un límite del problema.", "Sé que reutilizar ayuda a botar menos residuos."],
    explain=[
        "Un recurso material es todo lo que se usa para construir: cartón, papel, cordel, cinta o pegamento. Usarlos de forma eficiente significa lograr el mismo resultado gastando menos o desperdiciando menos. Un buen diseño empieza por saber cuánto material hay y cuántas piezas se necesitan.",
        "Para planificar los cortes se dibuja la plancha a escala y se reparten las piezas. Por ejemplo, de una plancha de 60 cm por 40 cm salen 3 piezas de 20 cm a lo largo y 4 piezas de 10 cm a lo ancho. Lo que no se usa es el desperdicio. El porcentaje de aprovechamiento se calcula así: área usada dividida entre área total, por 100.",
        "Hay otras maneras de ser eficiente. Reutilizar es darle un nuevo uso a un material que ya se usó, como una caja de embalaje. Reducir es gastar menos, por ejemplo uniendo con cordel en lugar de cortar piezas extra. Reciclar es convertir un material desechado en materia prima para otro producto. Reutilizar y reducir se prefieren porque gastan menos energía que reciclar.",
    ],
    vocab=[("recurso material", "material que se usa para construir"), ("eficiente", "que logra el resultado gastando menos recursos"), ("desperdicio", "material que sobra y no se usa"), ("aprovechamiento", "porcentaje del material que sí se usa"), ("reutilizar", "darle un nuevo uso a algo ya usado")],
    worked=[
        ("Repartir piezas en una plancha", "Una plancha de cartón mide 60 cm por 40 cm. Cada pieza mide 25 cm por 10 cm. Si las pones todas en el mismo sentido, ¿cuántas piezas salen y cuánto cartón sobra?", ["A lo largo caben 2 piezas de 25 cm (50 cm) y sobran 10 cm. A lo ancho caben 4 piezas de 10 cm (40 cm).", "Salen 2 × 4 = 8 piezas, que usan 8 × 250 = 2.000 cm². La plancha tiene 60 × 40 = 2.400 cm²."], "Salen 8 piezas y sobran 400 cm²"),
        ("Calcular el aprovechamiento", "En una plancha de 2.400 cm² se usaron 2.000 cm². ¿Qué porcentaje del material se aprovechó?", ["Divido el área usada entre el área total: 2.000 ÷ 2.400.", "2.000 ÷ 2.400 es lo mismo que 5 de cada 6, y 5 de cada 6 son cerca de 83 de cada 100."], "Cerca de 83 %"),
    ],
    mistakes=[
        ("Dibujar piezas sin mirar el tamaño de la plancha y descubrir después que no caben.", "No se planificó el reparto de los cortes.", "Dibuja la plancha a escala y reparte las piezas antes de cortar."),
        ("Botar los trozos que sobran sin pensar en otros usos.", "Esos retazos pueden servir como refuerzos o piezas pequeñas.", "Guarda los retazos y revisa si alguna pieza del diseño sale de ellos."),
    ],
    R=[
        ("El cartón de una caja de embalaje que se usa de nuevo para armar un organizador, ¿es reutilizar o reciclar?", "Reutilizar", "Se usa otra vez sin transformarlo."),
        ("El material que sobra de una plancha y no se usa, ¿cómo se llama?", "Desperdicio", "Es lo que no se aprovecha."),
        ("Para que una plancha sirva bien, ¿conviene repartir las piezas antes o después de cortar?", "Antes", "Si no se planifica, pueden sobrar o faltar piezas."),
    ],
    C=[
        ("¿Cuál es un uso eficiente del cartón? A planificar el reparto de las piezas antes de cortar, B cortar primero las piezas más grandes y ver cuántas caben de las otras.", "A", "A reduce el desperdicio; B lo aumenta."),
        ("Un compañero dice: «Todo lo que sobra se bota». ¿Qué le sugieres?", "Guardar los retazos y buscar un uso", "Un retazo puede servir para refuerzos u otras piezas."),
        ("¿Qué se prefiere para gastar menos energía y menos material? A reutilizar y reducir, B reciclar siempre.", "A", "Reciclar exige transformar el material; reutilizar y reducir gastan menos."),
    ],
    A=[
        arith("Una plancha mide 60 cm por 40 cm. ¿Cuántos centímetros cuadrados de cartón tiene?", "60*40", "El área de un rectángulo es largo por ancho.", " cm²"),
        arith("De una plancha de 60 cm por 40 cm se sacan piezas de 20 cm por 10 cm. A lo largo caben 3 y a lo ancho 4. ¿Cuántas piezas salen en total?", "3*4", "Se multiplican las piezas por fila por el número de filas.", " piezas"),
        arith("Para un organizador se necesitan 18 piezas, pero cada plancha da 12. ¿Cuántas piezas faltan si usas una sola plancha?", "18-12", "Se resta lo que da una plancha de lo que se necesita.", " piezas"),
    ],
    Z=[
        ("Plan A: usa 3 planchas nuevas. Plan B: usa 1 plancha nueva y 2 cajas de embalaje reutilizadas. Ambos logran el mismo organizador. ¿Cuál es más eficiente en materiales y por qué?", "El plan B, porque gasta menos material nuevo", "Reutiliza cajas en vez de consumir planchas nuevas."),
        ("Piezas de 30 cm por 10 cm en una plancha de 60 cm por 40 cm. Mateo dice que salen 8. Elena dice que salen 10. ¿Quién tiene razón?", "Mateo", "Caben 2 a lo largo y 4 a lo ancho: 2 × 4 = 8."),
    ],
    D=[
        arith("Una plancha de 100 cm por 50 cm tiene 5.000 cm². Con ella se arman 4 cajas que usan 1.000 cm² cada una. ¿Cuántos centímetros cuadrados sobran?", "100*50-4*1000", "Se calcula el área total y se restan las áreas usadas.", " cm²"),
        ("Un grupo necesita 20 piezas de 10 cm por 10 cm. Una plancha de 40 cm por 30 cm da 12 piezas de ese tamaño (4 por 3). ¿Cuántas planchas debe tener como mínimo?", "2", "Una plancha da 12 y no alcanza para 20; con 2 hay 24."),
    ],
    ctx=("Quieres hacer un portalápices con 4 paredes de 12 cm por 10 cm. Tienes una caja de embalaje reutilizada que mide 48 cm por 20 cm. Si pones las piezas todas en el mismo sentido, ¿cuántas paredes caben en total y alcanzan para las 4 que necesitas?", "Caben 8 paredes (4 a lo largo y 2 a lo ancho), así que alcanzan y sobran 4 paredes", "A lo largo caben 48 ÷ 12 = 4 y a lo ancho 20 ÷ 10 = 2; 4 × 2 = 8 es más que 4."),
    sc=[
        ("¿Qué significa usar un material de forma eficiente?", "Lograr el mismo resultado gastando menos o desperdiciando menos", "Es el sentido de eficiencia."),
        ("¿Qué es el desperdicio?", "El material que sobra y no se usa", "Se mide para saber cuánto se aprovechó."),
        ("¿Por qué se prefiere reutilizar antes que reciclar?", "Porque gasta menos energía y material", "Reutilizar no transforma el material."),
    ],
    open_task=(
        "Escoge un reparto. Reparto 1: una plancha de 60 cm por 40 cm para piezas de 15 cm por 12 cm. Reparto 2: una plancha de 80 cm por 30 cm para piezas de 25 cm por 14 cm. En ambos, pon las piezas todas en el mismo sentido, con el lado más largo a lo largo de la plancha. Dibuja la plancha, reparte las piezas, cuenta cuántas salen, calcula el área que sobra y propone un uso para los retazos.",
        "Reparto 1: a lo largo caben 4 piezas de 15 cm y a lo ancho 3 de 12 cm, en total 12. Plancha 2.400 cm², usada 12 × 180 = 2.160 cm², sobran 240 cm². Reparto 2: 3 × 2 = 6 piezas, usada 6 × 350 = 2.100 cm², sobran 300 cm². Los retazos sirven para refuerzos",
        ["dibuja la plancha con las piezas", "cuenta bien las piezas", "calcula el área que sobra", "propone un uso para los retazos"],
        ["hoja con dibujo y cálculos"],
        ["no revisar si las piezas caben en ambos sentidos", "olvidar las unidades"],
        "Pregunta: «¿cuántas piezas caben a lo largo y cuántas a lo ancho?». Si falla, pídele rehacer el dibujo.",
    ),
    reinforce="Mide una hoja de tu cuaderno, calcula cuántos cuadrados de 5 cm por 5 cm saldrían de ella y dibújalos.",
    extend="Explica por qué guardar los retazos de cartón puede ahorrar dinero y material en un proyecto.",
)

# ------------------------------------------------------------------ OA 02, clase 2
reg(
    OA2, 2,
    materials="Hoja, lápiz y los datos de etiquetas escritos en este cuaderno. No abras ni toques por dentro ningún aparato conectado a la red eléctrica.",
    use="Aprenderé a calcular cuánta energía gasta un objeto y a diseñar soluciones que gasten menos. Sirve para ahorrar energía y dinero sin perder la función.",
    prior=["Sé multiplicar y dividir.", "Sé que eficiente es lograr lo mismo gastando menos.", "Sé que hay energía eléctrica y energía del cuerpo."],
    explain=[
        "La energía es lo que permite que un objeto funcione. Un aparato eléctrico lleva en su etiqueta la potencia, que es cuánta energía usa cada hora; se mide en watts (W). Para saber cuánta energía gasta en un tiempo, se multiplica la potencia por las horas de uso: así sale la energía en watt-hora (Wh). Mil Wh son un kilowatt-hora (kWh), que es la unidad con que se cobra la electricidad. El costo sale de multiplicar los kWh por la tarifa, que es el precio de cada kWh; aquí usamos tarifas de ejemplo, no las reales.",
        "Un diseño eficiente en energía logra la misma tarea con menos Wh. Se puede lograr de varias maneras: elegir un aparato de menor potencia, usarlo menos horas, apagar lo que no se usa (algunos aparatos gastan un poco aunque estén en espera) o aprovechar la luz natural. También existen fuentes que no usan la red, como la energía del cuerpo (un molino manual) o la solar.",
        "Para comparar dos soluciones se calcula la energía de cada una en el mismo tiempo. Ejemplo: una lámpara de 10 W encendida 5 horas gasta 10 × 5 = 50 Wh; otra de 4 W gasta 4 × 5 = 20 Wh. La segunda ahorra 30 Wh. Por seguridad, estudiantes solo leen etiquetas y calculan: nunca abren aparatos conectados a la red.",
    ],
    vocab=[("potencia", "energía que un aparato usa cada hora; se mide en watts (W)"), ("watt-hora (Wh)", "unidad de energía: potencia por horas de uso"), ("kilowatt-hora (kWh)", "1.000 Wh; unidad con que se cobra la electricidad"), ("energía solar", "energía que viene de la luz del Sol"), ("modo en espera", "estado en que un aparato apagado sigue gastando un poco de energía")],
    worked=[
        ("Calcular la energía de un aparato", "Una lámpara de 8 W se usa 5 horas al día. ¿Cuántos Wh gasta en un día?", ["La energía es potencia por horas.", "Multiplico 8 × 5."], "40 Wh"),
        ("Comparar dos soluciones de energía", "Para iluminar un rincón de lectura 4 horas, la solución A usa una lámpara de 12 W y la solución B una de 5 W. ¿Cuánta energía ahorra B?", ["A gasta 12 × 4 = 48 Wh.", "B gasta 5 × 4 = 20 Wh. La diferencia es 48 − 20."], "B ahorra 28 Wh"),
    ],
    mistakes=[
        ("Creer que apagar un aparato con el botón de la pantalla ya no gasta nada.", "Algunos aparatos siguen gastando energía en espera.", "Si no se usa, desconéctalo con ayuda de una persona adulta o usa una regleta con interruptor."),
        ("Comparar dos aparatos usando un número distinto de horas para cada uno.", "No es justo, porque la energía depende de la potencia y del tiempo.", "Calcula con el mismo número de horas."),
    ],
    R=[
        ("La energía en Wh, ¿es potencia por horas o potencia entre horas?", "Potencia por horas", "Wh = W × h."),
        ("¿Cuántos Wh tiene 1 kWh?", "1.000", "El prefijo kilo significa mil."),
        ("¿Quién abre un aparato conectado a la red eléctrica para repararlo: un estudiante o una persona técnica adulta?", "Una persona técnica adulta", "Es peligroso y no corresponde a estudiantes."),
    ],
    C=[
        ("¿Cuál es una forma de ahorrar energía? A abrir las cortinas para usar la luz del día, B comprar una lámpara más potente para ver mejor.", "A", "Aprovechar la luz natural evita gastar electricidad."),
        ("Una solución dice: «Un molino manual no usa la red eléctrica». ¿Es verdad?", "Sí", "Usa la energía del cuerpo y no electricidad de la red."),
        ("¿Por qué conviene comparar dos soluciones con las mismas horas de uso?", "Para que la comparación sea justa", "La energía cambia con el tiempo."),
    ],
    A=[
        arith("Una lámpara de 10 W se usa 6 horas. ¿Cuántos Wh gasta?", "10*6", "Se multiplica la potencia por las horas.", " Wh"),
        arith("Un ventilador de 30 W funciona 8 horas. ¿Cuántos Wh gasta?", "30*8", "Se multiplica la potencia por las horas de uso.", " Wh"),
        arith("Un cargador gasta 280 Wh en una semana. ¿Cuántos Wh gasta por día, si lo usas los 7 días?", "280//7", "Se reparte la energía de la semana entre los 7 días.", " Wh"),
    ],
    Z=[
        ("Aparato 1: 15 W, 4 horas. Aparato 2: 6 W, 8 horas. ¿Cuál gasta más energía?", "El aparato 1", "El primero gasta 60 Wh y el segundo 48 Wh."),
        ("Dani dice: «Si apago la luz una hora menos al día, ahorro lo mismo con una lámpara de 4 W que con una de 20 W». ¿Tiene razón?", "No", "Con la de 20 W se ahorran 20 Wh y con la de 4 W solo 4 Wh."),
    ],
    D=[
        arith("Una lámpara de 12 W se reemplaza por otra de 4 W en un pasillo que se ilumina 5 horas al día. ¿Cuántos Wh se ahorran en un día?", "12*5-4*5", "Se calcula la energía de cada lámpara y se restan.", " Wh"),
        arith("Con una tarifa de ejemplo de $200 por kWh, se gastan 5.000 Wh en un mes. ¿Cuánto cuesta, en pesos?", "5000//1000*200", "Se pasan los Wh a kWh y se multiplica por la tarifa.", " pesos"),
    ],
    ctx=("Para leer 3 horas cada noche tienes dos opciones: una lámpara de escritorio de 9 W o una luz de 3 W. Calcula cuántos Wh gasta cada opción en una noche y di cuál ahorra más y cuántos Wh.", "La de 9 W gasta 27 Wh y la de 3 W gasta 9 Wh; ahorra 18 Wh", "Se calcula 9 × 3 = 27, 3 × 3 = 9 y la diferencia 18."),
    sc=[
        ("¿Cómo se calcula la energía en Wh?", "Potencia en W por horas de uso", "Es la fórmula de la clase."),
        ("¿Cuántos Wh son 2 kWh?", "2.000", "Cada kWh equivale a 1.000 Wh."),
        ("¿Quién repara aparatos conectados a la red?", "Una persona técnica adulta", "Por seguridad los estudiantes no los abren."),
    ],
    open_task=(
        "Escoge un problema. Problema 1: iluminar tu escritorio 4 horas por noche, comparando una lámpara de 12 W con otra de 6 W. Problema 2: mantener fresca una habitación comparando un ventilador de 40 W usado 5 horas con otro de 25 W usado 5 horas. Calcula los Wh de cada opción, el ahorro, y propone una forma de ahorrar sin comprar nada nuevo.",
        "Problema 1: 12 × 4 = 48 Wh y 6 × 4 = 24 Wh; ahorra 24 Wh. Sin comprar: abrir la cortina de día y usar la lámpara solo de noche",
        ["calcula la energía de cada opción", "calcula bien el ahorro", "propone una forma de ahorro sin comprar", "no manipula aparatos conectados"],
        ["hoja con cálculos y propuesta"],
        ["comparar con horas distintas", "sugerir abrir un aparato eléctrico"],
        "Pregunta: «¿usaste las mismas horas en las dos opciones?». Si no, pídele recalcular.",
    ),
    reinforce="Pide a una persona de tu casa que te lea la potencia que dice la etiqueta de una lámpara y calcula cuántos Wh gasta en 3 horas.",
    extend="Explica por qué la luz natural es un recurso energético que se puede aprovechar en el diseño de una sala.",
)

# ------------------------------------------------------------------ OA 02, clase 3
reg(
    OA2, 3,
    materials="Hoja, lápiz y los datos de archivos escritos en este cuaderno. Si tienes computador, una carpeta con fotos; si no, todo se resuelve en papel.",
    use="Aprenderé a usar de forma eficiente los recursos digitales: archivos, almacenamiento, batería y conexión. Sirve para guardar lo importante sin llenar los dispositivos ni perder el trabajo.",
    prior=["Sé que un archivo digital ocupa espacio.", "Sé que hay programas de dibujo, texto y planilla.", "Sé multiplicar y restar."],
    explain=[
        "Los recursos digitales son los archivos, el espacio para guardarlos, la batería del dispositivo, la conexión a internet y el tiempo de uso. Se miden: los archivos en megabytes (MB) o gigabytes (GB). En este cuaderno usamos 1 GB igual a 1.000 MB. Una foto de 3 MB ocupa menos que un video de 90 MB.",
        "Un buen diseño digital usa los recursos con eficiencia. Se reduce el tamaño de las fotos antes de enviarlas, se borran las copias repetidas, se nombra cada archivo con orden (por ejemplo «plano_repisa_v2») y se guardan las versiones importantes. También se cuida la batería, bajando el brillo y cerrando lo que no se usa, y se evita imprimir cuando basta con compartir el archivo.",
        "Además, lo valioso se respalda: se guarda al menos una segunda copia en otro lugar, porque un dispositivo puede fallar o perderse. Una buena regla es dos copias del trabajo final en lugares distintos. Respalda solo tus propios archivos y no incluyas datos personales en nombres de archivo ni en imágenes.",
    ],
    vocab=[("megabyte (MB)", "unidad para medir el tamaño de un archivo"), ("gigabyte (GB)", "1.000 MB en este cuaderno"), ("respaldo", "copia de un archivo en otro lugar para no perderlo"), ("versión", "estado guardado de un archivo en un momento"), ("comprimir", "reducir el tamaño de un archivo")],
    worked=[
        ("Calcular el espacio de varios archivos", "Un plano se documenta con 12 fotos de 3 MB cada una. ¿Cuántos MB ocupan?", ["Son 12 archivos del mismo tamaño.", "Multiplico 12 × 3."], "36 MB"),
        ("Decidir qué conviene reducir", "Un grupo debe enviar por correo 6 fotos de 8 MB y el correo acepta como máximo 25 MB. ¿Cómo lo resuelve?", ["Las 6 fotos suman 6 × 8 = 48 MB, que supera 25 MB.", "Reduce cada foto a 4 MB: 6 × 4 = 24 MB, que sí cabe."], "Reducir cada foto a 4 MB, con lo que suman 24 MB"),
    ],
    mistakes=[
        ("Guardar un único ejemplar del trabajo final en el dispositivo.", "Si falla o se pierde, se pierde todo el trabajo.", "Guarda al menos dos copias en lugares distintos."),
        ("Nombrar los archivos «foto1», «foto2» o «nuevo final final».", "Después nadie sabe cuál es cuál.", "Usa nombres con contenido y versión, como «planos_banco_v3»."),
    ],
    R=[
        ("El tamaño de un archivo, ¿se mide en MB o en cm?", "En MB", "Los megabytes miden datos digitales."),
        ("Una copia de un archivo en otro lugar para no perderlo, ¿cómo se llama?", "Respaldo", "Protege el trabajo ante fallas."),
        ("En este cuaderno, ¿cuántos MB son 1 GB?", "1.000", "Es la equivalencia usada en la clase."),
    ],
    C=[
        ("¿Qué nombre de archivo es más claro? A «foto_final_final2», B «plano_organizador_v2».", "B", "B dice qué es y qué versión es."),
        ("Para mandar una foto por un mensaje con límite de 5 MB y tu foto pesa 12 MB, ¿qué conviene hacer?", "Reducir su tamaño antes de enviarla", "Así cabe en el límite."),
        ("¿Por qué conviene bajar el brillo de la pantalla? A porque la pantalla gasta menos energía de la batería, B porque libera espacio de almacenamiento del dispositivo.", "A", "Una pantalla menos brillante gasta menos energía de la batería."),
    ],
    A=[
        arith("Un video ocupa 90 MB y cada foto 3 MB. ¿Cuántas fotos ocupan lo mismo que el video?", "90//3", "Se divide el tamaño del video entre el de una foto.", " fotos"),
        arith("Un dispositivo tiene 2 GB libres, es decir 2.000 MB. Se guardan 15 fotos de 4 MB. ¿Cuántos MB quedan libres?", "2000-15*4", "Se calcula el espacio usado y se resta del total.", " MB"),
        arith("Un grupo guarda 3 versiones de un plano de 5 MB cada una y 2 copias de respaldo de la versión final. ¿Cuántos MB ocupa todo?", "3*5+2*5", "Se suman las versiones y las dos copias del mismo tamaño.", " MB"),
    ],
    Z=[
        ("Mateo manda sus 10 fotos de 6 MB a un grupo y el límite del mensaje es 30 MB. Ana propone reducirlas a 2 MB cada una. ¿Así cumplen el límite?", "Sí", "Con 10 fotos de 2 MB suman 20 MB, menos de 30 MB."),
        ("Dani dice: «Imprimir todo es más seguro porque así no ocupa MB». Elena dice: «Imprimir gasta papel, y compartir el archivo no». ¿Quién propone un uso más eficiente de recursos para un documento que otros pueden leer en pantalla?", "Elena", "Compartir el archivo evita gastar papel y tinta."),
    ],
    D=[
        arith("Un archivo de 48 MB se comprime y queda en 12 MB. ¿Cuántos MB se ahorran?", "48-12", "Se resta el tamaño final del inicial.", " MB"),
        ("Una carpeta tiene 6 fotos de 5 MB, 3 de ellas repetidas, y 2 videos de 40 MB. Si se borran las repetidas, ¿cuántos MB quedan?", "95 MB", "Quedan 3 fotos de 5 MB (15 MB) y 2 videos de 40 MB (80 MB); suman 95 MB."),
    ],
    ctx=("Para tu proyecto sacaste 8 fotos de 5 MB y el correo acepta como máximo 24 MB. Calcula cuántos MB ocupan y a cuántos MB debe quedar cada foto, como máximo, para que quepan todas.", "Ocupan 40 MB. Cada foto debe quedar en 3 MB o menos, porque 8 × 3 = 24 MB", "Se calcula 8 × 5 = 40, que supera 24, y 24 ÷ 8 = 3."),
    sc=[
        ("¿Cuántas copias de respaldo conviene hacer del trabajo final?", "Al menos una más, en otro lugar", "Así el trabajo no depende de un solo lugar."),
        ("¿Qué significa comprimir un archivo?", "Reducir su tamaño", "Ocupa menos espacio."),
        ("¿Qué datos no deben ir en el nombre de un archivo?", "Datos personales", "Se protege la privacidad."),
    ],
    open_task=(
        "Escoge un proyecto digital. Proyecto 1: documentar una reparación con 10 fotos de 4 MB y un plano de 6 MB, con un correo que acepta 30 MB. Proyecto 2: preparar una presentación con 5 fotos de 8 MB y 2 videos de 20 MB, con un espacio de 60 MB. Calcula el tamaño total, decide qué reducir y a cuánto, nombra tres archivos con orden y explica dónde harías el respaldo.",
        "Proyecto 1: total 46 MB; reducir las fotos a 2 MB (20 MB) más el plano de 6 MB suman 26 MB. Archivos: reparacion_foto01, reparacion_plano_v1, reparacion_foto02. Respaldo en una segunda carpeta o dispositivo",
        ["calcula el total", "decide qué reducir con números", "nombres de archivo claros", "indica dónde respalda"],
        ["hoja con cálculo y plan de archivos"],
        ["no calcular el total", "nombres de archivo con datos personales"],
        "Pregunta: «¿cuánto ocupa todo si se cumple tu plan?». Si no suma, pídele hacer el cálculo.",
    ),
    reinforce="Inventa y escribe en tu cuaderno cuatro nombres ordenados para las 4 fotos de un proyecto, sin datos personales.",
    extend="Explica por qué guardar solo una copia de un trabajo importante es un uso poco eficiente del tiempo, aunque ahorre espacio.",
)

# ------------------------------------------------------------------ OA 02, clase 4
reg(
    OA2, 4,
    materials="Hoja, lápiz y los datos de tareas escritos en este cuaderno.",
    use="Aprenderé a planificar un trabajo con su plano, su lista de materiales, su reparto de tareas y su tiempo, y a implementarlo con seguridad. Sirve para terminar a tiempo, sin desperdiciar recursos y sin accidentes.",
    prior=["Sé calcular materiales con un dibujo técnico.", "Sé que debo prever los riesgos.", "Sé sumar tiempos en minutos."],
    explain=[
        "Un plan de trabajo reúne cuatro cosas: el plano con las medidas, la lista de materiales con cantidades, el orden de las tareas y el tiempo de cada una. Las tareas se anotan en el orden en que se hacen, porque algunas dependen de otras: no se puede pegar antes de cortar. El tiempo total se calcula sumando los tiempos de las tareas que se hacen una tras otra.",
        "Repartir tareas hace más eficiente el uso del tiempo: si dos personas trabajan a la vez en tareas que no dependen entre sí, se ahorra tiempo. Por ejemplo, mientras una persona corta las tiras, otra prepara el lugar o dibuja las marcas. En cambio, las tareas que dependen de una anterior, como armar después de cortar, deben esperar.",
        "Al implementar, sigue el plan y revisa cada paso. Reglas básicas de seguridad: mesa despejada y buena luz, tijeras de punta roma con la punta hacia abajo al caminar, pelo recogido, materiales fuera del suelo para no tropezar y manos lavadas al final. Si un paso es riesgoso, se cambia por otro más seguro y se anota el cambio. Las herramientas con filo o con motor las usa solo una persona adulta.",
    ],
    vocab=[("plan de trabajo", "documento con plano, materiales, tareas y tiempos"), ("tarea dependiente", "tarea que solo puede empezar cuando termina otra"), ("tareas en paralelo", "tareas que se hacen a la vez entre personas distintas"), ("implementar", "construir o poner en práctica una solución"), ("prevención", "medida que evita un accidente antes de que ocurra")],
    worked=[
        ("Sumar el tiempo de tareas seguidas", "Tareas seguidas: medir 10 minutos, cortar 15 minutos, armar 20 minutos y revisar 5 minutos. ¿Cuánto tiempo toma todo?", ["Las tareas dependen una de otra y se hacen en orden.", "Sumo 10 + 15 + 20 + 5."], "50 minutos"),
        ("Ahorrar tiempo con tareas en paralelo", "Dos estudiantes arman un soporte. Ana corta las tiras (15 minutos) y Luis dibuja la base (10 minutos), sin depender uno del otro. Después arman juntos (20 minutos). ¿Cuánto tarda el trabajo?", ["Ana y Luis trabajan a la vez: la parte inicial dura lo del más lento, 15 minutos.", "Luego arman juntos 20 minutos: 15 + 20."], "35 minutos"),
    ],
    mistakes=[
        ("Planificar las tareas sin mirar cuáles dependen de otras.", "Se puede intentar armar antes de cortar y se pierde tiempo.", "Ordena las tareas y marca cuáles esperan a otra."),
        ("Cambiar un paso por otro sin anotarlo.", "Después nadie sabe cómo se hizo ni por qué.", "Anota el cambio y el motivo en el plan."),
    ],
    R=[
        ("Armar un soporte, ¿puede hacerse antes de cortar las piezas?", "No", "Primero hay que tener las piezas cortadas."),
        ("Dos tareas que se hacen a la vez por personas distintas, ¿están en paralelo o dependen una de otra?", "Están en paralelo", "No necesitan esperarse."),
        ("¿Para qué se marcan los riesgos antes de empezar?", "Para evitar accidentes", "Es la prevención de la clase."),
    ],
    C=[
        ("¿Qué tarea depende de otra? A secar el pegamento después de pegar, B limpiar la mesa mientras otra persona corta.", "A", "Secar solo puede ocurrir después de pegar."),
        ("En una mesa hay cordeles tirados en el suelo. ¿Cuál es el riesgo y cómo se evita?", "Tropiezo; se guardan los cordeles", "Despejar el piso evita caídas."),
        ("Un compañero dice: «Si trabajamos en paralelo, el trabajo termina más rápido». ¿Es verdad cuando las tareas no dependen entre sí?", "Sí", "Se hacen a la vez y se ahorra tiempo."),
    ],
    A=[
        arith("Tareas seguidas: marcar 12 minutos, cortar 18 minutos y pegar 15 minutos. ¿Cuántos minutos toma todo?", "12+18+15", "Se suman los tiempos de las tareas seguidas.", " minutos"),
        arith("Dos estudiantes trabajan a la vez: uno corta en 20 minutos y otra prepara las marcas en 14 minutos. Después arman juntos en 25 minutos. ¿Cuántos minutos tarda todo?", "20+25", "La primera parte dura lo que tarda la más lenta y luego se suma el armado.", " minutos"),
        ("Pasos de un portalápices, desordenados: (a) pegar, (b) dibujar las medidas, (c) cortar, (d) probar. ¿Cuál es el orden correcto?", "b, c, a, d", "Se mide, se corta, se pega y por último se prueba."),
    ],
    Z=[
        ("Un grupo tiene 60 minutos. Sus tareas seguidas son 15, 20 y 30 minutos. Marta dice que alcanza. ¿Tiene razón?", "No", "Suman 65 minutos, 5 más de lo que hay."),
        ("Dos estudiantes pueden cortar y armar solos, pero les falta una persona adulta para cortar cartón grueso con un cortador. ¿Cómo cambian el plan sin romper la seguridad?", "Usar cartón delgado y tijeras de punta roma", "Se reemplaza el paso riesgoso por otro más seguro."),
    ],
    D=[
        arith("Un trabajo tiene 4 tareas seguidas de 15 minutos cada una. Con dos personas se logra trabajar a la vez en 2 de ellas, lo que ahorra 15 minutos. ¿Cuántos minutos tarda el trabajo?", "4*15-15", "Se calcula el tiempo total seguido y se resta lo ahorrado.", " minutos"),
        ("Tres tareas: A (10 minutos), B (25 minutos) y C (15 minutos). B y C dependen de A; B y C no dependen entre sí. Si dos personas hacen B y C a la vez después de A, ¿cuántos minutos tarda todo?", "35", "A toma 10 y luego B y C se hacen a la vez, lo que dura 25; 10 + 25 = 35."),
    ],
    ctx=("Vas a armar con una amiga un estante de cartón. Tareas: dibujar y medir (10 minutos), cortar (20 minutos), pegar (15 minutos) y probar (5 minutos). Calcula el tiempo seguido y di qué riesgo cuidarías al cortar.", "50 minutos. Riesgo: cortarse con la tijera, que se evita con tijera de punta roma y las manos lejos del borde", "Se suma 10 + 20 + 15 + 5 y se nombra un riesgo con prevención."),
    sc=[
        ("¿Qué incluye un plan de trabajo?", "Plano, materiales, tareas y tiempos", "Son las cuatro partes de la clase."),
        ("¿Qué es una tarea dependiente?", "La que solo puede empezar cuando termina otra", "Su orden importa."),
        ("¿Qué haces si un paso es riesgoso?", "Lo cambio por otro más seguro y lo anoto", "Se previene el accidente."),
    ],
    open_task=(
        "Escoge un trabajo. Trabajo 1: un organizador de escritorio con 5 tareas: medir (10 minutos), cortar (20), pegar (15), decorar (10) y probar (5). Trabajo 2: un cartel de cartón con 4 tareas: diseñar el texto (15 minutos), dibujar las letras (25), colorear (20) y pegar a la pared (5). Escribe el orden, el tiempo total, qué tareas pasarías en paralelo con otra persona, cuántos minutos ahorrarías y dos riesgos con su prevención.",
        "Trabajo 1: orden medir, cortar, pegar, decorar, probar = 60 minutos. En paralelo: una persona decora piezas mientras otra pega; ahorro de unos 10 minutos. Riesgos: cortarse con la tijera y tropiezo con material en el suelo",
        ["orden correcto con dependencias", "calcula el tiempo total", "propone tareas en paralelo con ahorro", "dos riesgos con prevención segura"],
        ["hoja con plan, tiempos y riesgos"],
        ["poner en paralelo tareas que dependen entre sí", "no prever riesgos"],
        "Pregunta: «¿esta tarea necesita que otra termine antes?». Si sí, pídele sacarla del paralelo.",
    ),
    reinforce="Anota las tareas y los tiempos para ordenar tu pieza en casa y calcula cuánto demoras en total.",
    extend="Explica por qué dos personas trabajando en paralelo no siempre terminan en la mitad del tiempo.",
)

# ------------------------------------------------------------------ OA 02, clase 5
reg(
    OA2, 5,
    materials="Hoja, lápiz y los datos de pruebas escritos en este cuaderno. Si quieres practicar, hojas de papel y monedas de $10 o libros livianos.",
    use="Aprenderé a probar una solución con evidencia, a calcular su eficiencia comparando lo que logra con lo que gasta, y a decidir si funciona. Sirve para mostrar con datos que tu solución es eficiente.",
    prior=["Sé hacer pruebas repetidas y calcular un promedio.", "Sé comparar un resultado con un criterio.", "Sé que cambiar una sola variable es una prueba justa."],
    explain=[
        "Probar una solución es comprobar que cumple los criterios con datos. Una prueba justa repite lo mismo varias veces, cambia una sola variable y mide con la misma forma. Se hacen al menos tres pruebas y se calcula el promedio. Si un dato es muy distinto de los otros, se revisa qué pasó.",
        "La eficiencia relaciona lo que logra la solución con lo que gasta. Por ejemplo, si una estructura de cartón de 100 g sostiene 600 g, logra 600 ÷ 100 = 6 g sostenidos por cada gramo de cartón. Entre dos diseños, es más eficiente el que logra más con los mismos recursos, o el que logra lo mismo con menos recursos.",
        "Para comparar un antes y un después se calcula la diferencia entre ambos resultados. Si la versión 1 sostenía 400 g y la versión 2 sostiene 600 g con el mismo cartón, la mejora es 200 g. Tu conclusión debe decir si cumple el criterio, qué dato lo muestra y qué cambiarías para mejorar.",
    ],
    vocab=[("eficiencia", "lo que logra una solución en relación con lo que gasta"), ("prueba justa", "prueba repetida igual, cambiando una sola variable"), ("promedio", "suma de los datos dividida entre la cantidad de datos"), ("variable", "lo que se puede cambiar en una prueba"), ("evidencia", "datos que apoyan una decisión")],
    worked=[
        ("Calcular la eficiencia", "Una estructura de cartón de 50 g sostiene 400 g. ¿Cuántos gramos sostiene por cada gramo de cartón?", ["La eficiencia es lo sostenido dividido entre el cartón usado.", "Divido 400 ÷ 50."], "8 g por cada gramo de cartón"),
        ("Decidir con las pruebas", "Criterio: sostiene al menos 300 g en cada prueba. Resultados de un puente: 320 g, 300 g y 280 g. ¿Cumple?", ["Comparo cada prueba con 300 g.", "La tercera, 280 g, no llega."], "No cumple, porque en la tercera prueba sostuvo solo 280 g"),
    ],
    mistakes=[
        ("Decir que funciona después de una sola prueba.", "Una prueba puede salir bien por casualidad.", "Haz al menos tres pruebas iguales y calcula el promedio."),
        ("Comparar dos diseños que usan cantidades distintas de material como si fueran iguales.", "No se sabe cuál es más eficiente sin relacionar el resultado con el gasto.", "Calcula cuánto logra cada uno por unidad de material."),
    ],
    R=[
        ("¿Cuántas pruebas se hacen como mínimo?", "Tres", "Con tres datos se calcula un promedio."),
        ("Una prueba justa, ¿cambia una sola variable o varias a la vez?", "Una sola", "Así se sabe qué produjo el resultado."),
        ("Si un dato es muy distinto de los otros dos, ¿se ignora o se revisa qué pasó?", "Se revisa qué pasó", "Puede ser un error o una falla del diseño."),
    ],
    C=[
        ("Diseño 1 sostiene 600 g con 100 g de cartón. Diseño 2 sostiene 600 g con 150 g de cartón. ¿Cuál es más eficiente?", "El diseño 1", "Logra lo mismo con menos cartón."),
        ("¿Qué debe decir la conclusión de una prueba? A si cumple el criterio y qué dato lo muestra, B que el diseño le gustó a mi grupo.", "A", "La conclusión se apoya en evidencia."),
        ("Lía probó dos puentes cambiando el papel y también la distancia entre los apoyos. ¿Puede saber qué produjo la diferencia?", "No", "Cambió más de una variable."),
    ],
    A=[
        arith("Tres pruebas de un puente dieron 400 g, 500 g y 600 g sostenidos. ¿Cuál es el promedio?", "(400+500+600)//3", "Se suman los datos y se divide entre 3.", " g"),
        arith("Una estructura de 80 g sostiene 640 g. ¿Cuántos gramos sostiene por cada gramo de cartón?", "640//80", "Se divide lo sostenido entre el cartón.", " g"),
        arith("La versión 1 sostenía 350 g y la versión 2 sostiene 500 g con el mismo cartón. ¿Cuántos gramos mejoró?", "500-350", "Se resta el resultado antes del resultado después.", " g"),
    ],
    Z=[
        ("Criterio: sostiene al menos 250 g en cada prueba. Resultados: 250 g, 260 g y 240 g. Ana dice que cumple porque el promedio es 250 g. Beto dice que no cumple. ¿Quién tiene razón?", "Beto", "Aunque el promedio es 250 g, la tercera prueba no llega a 250 g."),
        ("Un grupo dice: «Sostuvo 400 g una vez, así que es el mejor diseño». ¿Qué falta para afirmarlo?", "Repetir la prueba y comparar con otros diseños", "Una sola prueba no es evidencia suficiente."),
    ],
    D=[
        arith("Diseño A: 60 g de cartón, sostiene 480 g. Diseño B: 90 g de cartón, sostiene 540 g. ¿Cuántos gramos más por gramo de cartón sostiene A que B?", "480//60-540//90", "A sostiene 8 g por gramo y B sostiene 6 g por gramo.", " g"),
        ("Un puente de papel sostuvo 150 g, 200 g, 100 g y 150 g en cuatro pruebas. El criterio dice «sostiene en promedio al menos 150 g». ¿Cumple?", "Sí", "El promedio es (150 + 200 + 100 + 150) ÷ 4 = 150 g."),
    ],
    ctx=("Probaste una repisa de cartón con monedas de $10. Soportó 40, 40 y 34 monedas en tres intentos. El criterio pide «soporta al menos 36 monedas en cada prueba». Calcula el promedio y di si cumple.", "Promedio: 38 monedas, pero no cumple en todas porque en una prueba soportó 34", "Se calcula (40 + 40 + 34) ÷ 3 y se revisa cada prueba."),
    sc=[
        ("¿Cómo se calcula la eficiencia de una estructura?", "Lo que sostiene dividido entre el material usado", "Relaciona el resultado con el gasto."),
        ("¿Cuántas variables cambias en una prueba justa?", "Una", "Así se sabe qué produjo el cambio."),
        ("En Tecnología: ¿Qué debe tener una conclusión?", "El criterio, el dato y qué cambiarías", "Debe apoyarse en evidencia."),
    ],
    open_task=(
        "Escoge un registro. Registro 1: un puente de papel de 50 g sostuvo 300 g, 320 g y 280 g; el criterio es «sostiene al menos 300 g en promedio». Registro 2: una repisa de cartón de 150 g sostuvo 900 g, 960 g y 840 g; el criterio es «sostiene en cada prueba al menos 900 g». Calcula el promedio, la eficiencia (gramos sostenidos por gramo de material usando el promedio), di si cumple y propone una mejora que cambie una sola variable.",
        "Registro 1: promedio 300 g, cumple en promedio. Eficiencia: 300 ÷ 50 = 6 g sostenidos por cada gramo de papel. Mejora: aumentar el doblez del papel sin cambiar el largo",
        ["calcula bien el promedio", "calcula la eficiencia", "decide con el criterio del registro", "mejora con una sola variable"],
        ["hoja con cálculos, decisión y mejora"],
        ["revisar solo el promedio y olvidar cada prueba", "cambiar varias variables a la vez"],
        "Pregunta: «¿qué número de las pruebas apoya tu decisión?». Si no cita ninguno, pídele volver a los datos.",
    ),
    reinforce="Repite tres veces cuántas monedas de $10 sostiene una hoja doblada como puente entre dos libros y anota el promedio.",
    extend="Explica con un ejemplo por qué un diseño que sostiene más puede no ser el más eficiente.",
)
