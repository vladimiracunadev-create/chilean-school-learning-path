"""Gráfica TP 3.º y 4.º medio: OAE-01 (diagramar y editar imágenes y textos originales), OAE-02 (prueba de color, película, matriz e impreso digital) y OAE-03 (materias primas e insumos). Todo en papel: trabajos, archivos, medidas y precios inventados, sin software, imágenes ni máquinas; los procesos de impresión solo como conceptos."""
from __future__ import annotations

from tp_graf_common import build

O1 = "TP-GRAF-3y4-OAE-01"
O2 = "TP-GRAF-3y4-OAE-02"
O3 = "TP-GRAF-3y4-OAE-03"
LIM = " Este cuaderno trabaja en papel, sin software de diseño ni taller real: lo que haces aquí no reemplaza la práctica con un instructor."
MAQ = " Esto es aprendizaje conceptual en papel: practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar."

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (orden de trabajo de ejemplo, inventada). Cliente ficticio: «Panadería Ejemplo». Producto: 500 volantes de tamaño A5 (148 × 210 mm), impresos por las 2 caras, a todo color. "
     "El cliente entrega un logotipo y 3 fotografías de un banco de imágenes cuya licencia permite uso comercial. Fases del trabajo: preimpresión (preparar los archivos), impresión y postimpresión (cortar y terminar). "
     "Responsables: una diseñadora, un operador de preimpresión y un jefe de taller. Entrega: viernes.")
build(
    O1, 1, F,
    use="Aprenderé qué es una orden de trabajo gráfica, qué fases tiene el proceso y qué reglas de derechos de autor, privacidad y ergonomía debo respetar al diagramar y editar.",
    prior=["Sé leer una tabla o una ficha.", "Sé sumar, restar y multiplicar.", "Sé qué es una imagen y un texto."],
    explain=[
        "En Gráfica, todo trabajo parte de una orden de trabajo (OT): un documento que dice qué producto se hará, de qué tamaño, cuántas unidades, con qué colores y papel, y para qué fecha. El proceso tiene tres fases: la preimpresión prepara los archivos (diagramar es ordenar textos e imágenes en la página, y editar es corregirlos o ajustarlos), la impresión pasa el diseño al papel y la postimpresión corta, dobla o termina el producto.",
        "Los textos, las imágenes y las tipografías (los diseños de letra) tienen autor. Una licencia es el documento que dice qué usos permite el autor: usar algo sin revisar su licencia puede infringir los derechos de autor. También se cuida la privacidad: una foto donde aparece una persona exige su autorización, o la de su apoderado si es menor, y los datos personales de un original no se difunden.",
        "El trabajo con pantalla exige ergonomía: pantalla a la altura de los ojos, espalda apoyada y pausas breves y regulares. Como pauta de ejemplo de este cuaderno, se hace una pausa de 5 minutos por cada hora frente a la pantalla. Cada decisión se registra y tiene un responsable." + LIM,
    ],
    vocab=[("orden de trabajo (OT)", "documento que detalla qué producto se hará, sus medidas, cantidades, colores y plazo"), ("preimpresión", "fase en que se preparan y revisan los archivos antes de imprimir"), ("postimpresión", "fase en que el impreso se corta, dobla o termina"), ("diagramar", "ordenar textos e imágenes dentro de la página"), ("licencia", "documento que indica qué usos permite el autor de una obra"), ("derechos de autor", "derechos de quien crea un texto, imagen o letra sobre su obra"), ("tipografía", "diseño de letra")],
    worked=[
        ("Contar cajas de entrega", "Un taller de ejemplo entrega 300 tarjetas en cajas de 25 tarjetas. ¿Cuántas cajas necesita?", ["Se divide el total de tarjetas por las que caben en una caja.", "300 ÷ 25 = 12."], "12 cajas"),
        ("Revisar una licencia", "Una imagen de ejemplo trae una licencia que dice «uso personal, no comercial». El cliente quiere ponerla en un volante para vender productos. ¿Se puede usar?", ["Un volante para vender es un uso comercial.", "La licencia solo permite uso personal, así que no cubre ese uso."], "No: hay que pedir otra licencia o elegir otra imagen"),
    ],
    mistakes=[("Bajar una fotografía de un buscador de internet y ponerla en el trabajo «porque estaba a la vista».", "Estar a la vista no significa que sea libre: la imagen tiene autor y una licencia que puede no permitir el uso comercial.", "Pide al cliente la imagen con su licencia o usa una cuya licencia permita ese uso."),
              ("Cambiar un dato de la OT, como la cantidad, «porque me pareció poco», sin avisar.", "La OT es el documento que respalda el trabajo; cambiarlo sin registro hace que cada persona trabaje con datos distintos.", "Consulta a la jefatura y deja constancia escrita de quién aprobó el cambio.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una orden de trabajo?", "Un documento que detalla qué producto se hará, sus medidas, cantidades y plazo", "Un permiso para usar cualquier imagen de internet", "El diseño final ya impreso", "La orden de trabajo es el documento base que indica qué producir, cuánto y para cuándo."),
        ("abc", "¿Cuáles son las tres fases del proceso gráfico?", "Preimpresión, impresión y postimpresión", "Cobro, entrega y reclamo", "Corte, plegado y encuadernación", "Preparar archivos, imprimir y terminar son las tres fases; corte y plegado pertenecen solo a la última."),
        ("abc", "{F} ¿Cuántas caras se imprimen en cada volante?", "2 caras", "1 cara", "4 caras", "La ficha indica que los volantes se imprimen por las dos caras."),
        ("abc", "{F} ¿Qué tamaño tienen los volantes según la orden?", "A5, de 148 × 210 mm", "A4, de 210 × 297 mm", "A3, de 297 × 420 mm", "La ficha fija el tamaño A5; A4 y A3 son formatos mayores."),
        ("abc", "¿Qué es una licencia de una imagen o de una tipografía?", "El documento que indica qué usos permite su autor", "El precio de la impresión", "El tamaño en píxeles del archivo", "La licencia fija los usos permitidos y es lo que se revisa antes de usar una obra ajena."),
        ("=", "{F} Cada caja de entrega lleva 50 volantes terminados. ¿Cuántas cajas se necesitan para entregar todo el pedido?", "500//50", "Se divide el total de volantes por los que caben en cada caja.", " cajas"),
        ("abc", "Una diseñadora de ejemplo encontró en un buscador una fotografía sin autor ni licencia visibles y quiere usarla en un afiche de venta. ¿Cuál es el problema principal?", "No sabe si el uso comercial está permitido y puede infringir derechos de autor", "Ninguno, porque cualquier imagen de internet es libre", "La imagen cambiará de color al imprimirse", "Sin licencia conocida no hay permiso comprobado; que esté en internet no la hace libre."),
        ("abc", "El cliente entrega una fotografía de un grupo de estudiantes y quiere publicarla en un volante. ¿Qué corresponde hacer antes de usarla?", "Confirmar que las personas, o sus apoderados si son menores, autorizaron el uso de su imagen", "Imprimirla y pedir permiso si alguien reclama", "Recortar los rostros para ahorrar tinta", "Publicar la imagen de una persona exige su autorización, y la de su apoderado si es menor."),
        ("=", "{F} Cada fase empieza cuando termina la anterior. La preimpresión demora 2 días, la impresión 1 día y la postimpresión 1 día. Si el trabajo parte el lunes (día 1) y se entrega el viernes (día 5), ¿cuántos días de margen quedan?", "5-(2+1+1)", "Al plazo total de 5 días se le restan los días que ocupan las tres fases.", " día"),
        ("abc", "Una compañera dice: «si la tipografía ya viene en el computador, puedo usarla en cualquier trabajo comercial sin revisar nada». ¿Qué le respondes?", "Que su licencia también fija los usos permitidos y hay que revisarla", "Que tiene razón, porque lo instalado siempre es libre", "Que las tipografías no tienen autor", "Una tipografía es una obra con autor y su licencia puede limitar el uso comercial."),
        ("abc", "La OT de ejemplo dice «volante A5», pero una nota del cliente dice «A4». ¿Qué hace el operador de preimpresión?", "Consulta a la jefatura y deja constancia antes de seguir", "Elige el tamaño que le parece mejor", "Prepara ambos y entrega solo uno sin avisar", "Los datos contradictorios se aclaran por escrito con quien responde antes de trabajar."),
        ("abc", "En una OT de ejemplo no figura quién aprueba el archivo final. ¿Qué riesgo produce?", "Nadie responde por verificar y pueden imprimirse errores sin que se note", "Ninguno, porque el archivo se corrige solo", "El papel cambia de tamaño", "Sin responsable, las revisiones se dan por hechas y los errores llegan a la impresión."),
        ("=", "Un operador de preimpresión de ejemplo trabaja 6 horas frente a la pantalla y sigue la pauta de este cuaderno de una pausa de 5 minutos por hora. ¿Cuántos minutos de pausa suma en la jornada?", "6*5", "Se multiplica el número de horas por los minutos de pausa de cada hora.", " minutos"),
    ],
    ctx=("abc", "Un cliente de ejemplo te pide copiar «igual» el diseño completo de la tarjeta de otra tienda. ¿Qué corresponde responder?", "Que copiar el trabajo ajeno puede infringir derechos de autor y que puedes proponer un diseño original", "Que se copia sin problema si se cambia un poco el color", "Que se copia solo si el cliente lo pide en voz alta", "El diseño de otra persona tiene autor; lo correcto es crear una propuesta propia."),
    sc=[
        ("En Gráfica: ¿qué fase prepara y revisa los archivos?", "La preimpresión", "En ella se diagrama, se edita y se revisan los archivos antes de imprimir."),
        ("¿Qué revisas antes de usar una imagen ajena en un trabajo comercial?", "Su licencia", "La licencia dice si el uso comercial está permitido."),
        ("¿Qué haces si la OT y otra nota del cliente se contradicen?", "Consulto a quien responde y dejo constancia", "Los datos contradictorios se aclaran antes de trabajar y se registran."),
    ],
    op=("Un taller de ejemplo recibe esta OT: 200 marcapáginas de 60 × 180 mm, 1 cara a color, con una fotografía de una niña que el cliente sacó en un paseo del curso, y una tipografía descargada de una página sin licencia visible. Entrega en 3 días. "
        "Escribe: las tres fases con una tarea de cada una, dos riesgos de derechos o privacidad que detectas y lo que harías con cada uno, y cuántas cajas de 20 marcapáginas necesitas.",
        "Fases: preimpresión (revisar archivos), impresión (imprimir los 200), postimpresión (cortar a 60 × 180 mm). Riesgos: la foto muestra a una menor, así que pido la autorización de su apoderado; la tipografía no tiene licencia visible, así que pido la licencia o uso otra. Cajas: 200 ÷ 20 = 10.",
        ["nombra las tres fases con una tarea de cada una", "detecta el riesgo de privacidad y el de licencia", "calcula bien las cajas y escribe qué haría"],
        ["hoja con fases, riesgos con su acción y el cálculo"],
        ["decir que la foto se puede usar porque la sacó el cliente", "no mencionar la licencia de la tipografía", "olvidar la autorización del apoderado"],
        "Pregunta: «¿qué documento prueba que puedes usar esa letra?». Si no lo nombra, repasa el concepto de licencia con el ejemplo del marcapáginas."),
    reinforce="Dibuja una línea con las tres fases del proceso gráfico y escribe bajo cada una una tarea que se hace en ella.",
    extend="Explica con un ejemplo inventado por qué una OT con un responsable de aprobación evita errores.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (especificaciones de ejemplo, inventadas). Afiche A3 de 297 × 420 mm. Sangrado: 3 mm por cada lado. Margen de seguridad: 10 mm dentro del formato final. "
     "Modo de color: CMYK. Resolución mínima de las fotografías a tamaño final: 300 ppp. Texto del cuerpo: 12 pt con interlineado de 15 pt. Archivo final: PDF.")
build(
    O1, 2, F,
    use="Aprenderé los conceptos técnicos de un archivo gráfico: formato, sangrado, márgenes, resolución, modo de color, tipo de imagen y medidas de tipografía.",
    prior=["Conozco la orden de trabajo y las fases del proceso.", "Sé multiplicar y dividir.", "Sé medir en milímetros."],
    explain=[
        "El formato es el tamaño final del producto, por ejemplo 297 × 420 mm. El sangrado es una zona extra de color o imagen que se extiende más allá del borde final: así, si el corte se corre un poco, no queda un filo blanco. El margen de seguridad es una zona dentro del borde donde no deben ir textos importantes, porque podrían cortarse o quedar pegados al borde.",
        "Una imagen de mapa de bits se compone de píxeles (puntitos de color); su resolución se mide en ppp, píxeles por pulgada. Los píxeles que necesita una imagen se calculan multiplicando su ancho en pulgadas por los ppp. Al revés, los ppp efectivos son los píxeles divididos por las pulgadas. Una imagen vectorial, como un logotipo, se define con formas matemáticas y se agranda sin perder nitidez.",
        "Para imprimir, los archivos se preparan en CMYK, las cuatro tintas: cian, magenta, amarillo y negro. El modo RGB es el de las pantallas y puede cambiar de aspecto al imprimir. La tipografía se mide en puntos (pt): el cuerpo es el tamaño de la letra y el interlineado es la distancia entre una línea y la siguiente; el alto de un bloque es el número de líneas por el interlineado." + LIM,
    ],
    vocab=[("formato", "tamaño final del producto"), ("sangrado", "zona extra de color o imagen que sobrepasa el borde final"), ("margen de seguridad", "zona interior donde no se ponen textos importantes"), ("ppp", "píxeles por pulgada; mide la resolución"), ("vectorial", "imagen definida por formas que se agranda sin perder nitidez"), ("CMYK", "modo de color de impresión: cian, magenta, amarillo y negro"), ("interlineado", "distancia entre una línea de texto y la siguiente")],
    worked=[
        ("Píxeles necesarios", "Una imagen de ejemplo se usará a 4 pulgadas de ancho con 300 ppp. ¿Cuántos píxeles de ancho necesita?", ["Píxeles = pulgadas × ppp.", "4 × 300 = 1.200."], "1.200 píxeles"),
        ("Tamaño con sangrado", "Una tarjeta de ejemplo mide 90 × 50 mm y lleva 2 mm de sangrado por lado. ¿Qué ancho tiene el archivo?", ["El sangrado se agrega a la izquierda y a la derecha.", "90 + 2 + 2 = 94."], "94 mm"),
    ],
    mistakes=[("Poner el nombre del evento a 3 mm del borde final del afiche.", "Esa zona puede cortarse o verse pegada al borde: es parte del margen de seguridad.", "Mueve los textos importantes hacia el interior, respetando el margen de seguridad."),
              ("Creer que una imagen sirve para imprimir porque «tiene muchos píxeles», sin mirar a qué tamaño se usa.", "Lo que importa es la resolución efectiva: los píxeles divididos por las pulgadas de la impresión.", "Calcula los ppp efectivos y compáralos con el mínimo pedido.")],
    T=[
        ("abc", "En Gráfica: ¿qué es el sangrado?", "Una zona extra de color o imagen que sobrepasa el borde final para que el corte no deje un filo blanco", "El margen interior donde van los textos importantes", "El espacio en blanco entre dos columnas de texto", "El sangrado se extiende más allá del borde final; el margen de seguridad es el que queda hacia adentro."),
        ("abc", "¿Qué significa ppp en una imagen?", "Píxeles por pulgada", "Páginas por pliego", "Puntos por párrafo", "ppp mide cuántos píxeles caben en una pulgada y define la resolución."),
        ("abc", "¿Para qué se prepara un archivo en modo CMYK?", "Para imprimirlo con tintas cian, magenta, amarilla y negra", "Para verlo más brillante en una pantalla", "Para que el archivo pese menos", "CMYK es el modo de las tintas de impresión; el modo de las pantallas es RGB."),
        ("abc", "{F} ¿Qué tamaño final tiene el afiche?", "297 × 420 mm", "303 × 426 mm", "210 × 297 mm", "El formato final es el de la ficha; 303 × 426 mm sería el archivo con sangrado."),
        ("=", "{F} ¿Cuántos mm de ancho tiene el archivo del afiche con su sangrado?", "297+3+3", "Al ancho final se le suma el sangrado de ambos lados.", " mm"),
        ("abc", "Un logotipo debe poder ampliarse a un letrero grande sin verse borroso. ¿Qué tipo de imagen conviene?", "Una vectorial", "Un mapa de bits de baja resolución", "Una fotografía pequeña ampliada", "Las formas matemáticas de una imagen vectorial se agrandan sin perder nitidez."),
        ("=", "Una fotografía de ejemplo se usará a 6 pulgadas de ancho y debe tener 250 ppp. ¿Cuántos píxeles de ancho necesita?", "6*250", "Los píxeles son las pulgadas por los ppp pedidos.", " píxeles"),
        ("abc", "{F} Un texto importante queda a 4 mm del borde final del afiche. ¿Qué problema puede tener?", "Está dentro del margen de seguridad de 10 mm y podría cortarse o verse pegado al borde", "Ninguno, porque el sangrado es de 3 mm", "Su resolución bajará a 150 ppp", "El margen de seguridad pide dejar 10 mm libres de textos importantes; el sangrado es otra cosa."),
        ("=", "{F} Un bloque del afiche tiene 9 líneas de texto con el interlineado de la ficha. ¿Cuántos pt de alto ocupa?", "9*15", "El alto de un bloque es el número de líneas por el interlineado.", " pt"),
        ("abc", "{F} El cliente entrega una imagen de 1.500 píxeles de ancho que se imprimirá a 6 pulgadas de ancho. ¿Cumple la resolución mínima?", "No: 1.500 ÷ 6 = 250 ppp, menos de 300", "Sí, porque 1.500 es mayor que 300", "Sí, porque el afiche es A3", "Los ppp efectivos se calculan dividiendo píxeles por pulgadas; 1.500 píxeles no son 1.500 ppp."),
        ("abc", "{F} Un compañero propone entregar el archivo en RGB «porque se ve más vivo en la pantalla». ¿Qué le respondes?", "La especificación pide CMYK y en RGB los colores pueden cambiar al imprimir", "Tiene razón: RGB siempre imprime mejor", "El modo de color no influye en el resultado impreso", "RGB es el modo de las pantallas; la ficha exige CMYK para la impresión."),
        ("abc", "{F} El cliente entrega un archivo de exactamente 297 × 420 mm, sin sangrado, con una fotografía de fondo hasta el borde. ¿Cuál es el problema?", "Al cortar, una pequeña desviación puede dejar un filo blanco en el borde", "La fotografía pasará a ser vectorial", "El formato A3 no se puede imprimir", "Sin sangrado, cualquier desvío del corte deja a la vista el papel blanco."),
        ("=", "{F} Se respeta el margen de seguridad en ambos lados del ancho final. ¿Cuántos mm de ancho útil quedan para los textos importantes?", "297-10-10", "Al ancho final se le restan los márgenes izquierdo y derecho.", " mm"),
    ],
    ctx=("abc", "Una imprenta de ejemplo recibe de un cliente una fotografía de 600 píxeles de ancho para un afiche A3 de 297 mm de ancho, bajada de una página sin datos de autor. ¿Qué corresponde?", "Avisar que la resolución es baja y que falta la licencia, y pedir el original con su permiso", "Ampliarla hasta cubrir el ancho y seguir", "Buscar otra imagen cualquiera en internet y reemplazarla sin avisar", "Una imagen pequeña ampliada se ve borrosa y sin licencia no hay permiso comprobado de uso."),
    sc=[
        ("En Gráfica: ¿cómo se calculan los píxeles que necesita una imagen?", "Pulgadas de ancho por ppp", "Los ppp son píxeles por cada pulgada, así que se multiplican por las pulgadas."),
        ("¿Qué zona se mantiene libre de textos importantes?", "El margen de seguridad", "Esa zona interior evita que el texto se corte o quede pegado al borde."),
        ("¿Qué modo de color se usa para preparar un archivo de impresión?", "CMYK", "Es el modo de las cuatro tintas de impresión."),
    ],
    op=("Especificaciones de ejemplo para una tarjeta de presentación: 90 × 50 mm, sangrado de 2 mm por lado, margen de seguridad de 5 mm, CMYK, y una fotografía que irá a 2 pulgadas de ancho con 300 ppp mínimo. "
        "Calcula: el tamaño del archivo con sangrado, el ancho útil para textos importantes y los píxeles de ancho que necesita la fotografía; luego explica en una frase qué pasaría si no hubiera sangrado.",
        "Archivo: 94 × 54 mm (90 + 2 + 2 y 50 + 2 + 2). Ancho útil: 90 − 5 − 5 = 80 mm. Fotografía: 2 × 300 = 600 píxeles. Sin sangrado, un corte levemente corrido podría dejar un filo blanco en el borde.",
        ["calcula bien el tamaño con sangrado", "calcula ancho útil y píxeles", "explica la función del sangrado"],
        ["hoja con los tres cálculos y la explicación"],
        ["sumar el sangrado una sola vez", "restar solo un margen", "confundir sangrado con margen de seguridad"],
        "Pregunta: «¿el sangrado va hacia afuera o hacia adentro del borde?». Si responde 'adentro', vuelve a la diferencia con el margen de seguridad."),
    reinforce="Dibuja un rectángulo de 90 × 50 mm y marca con colores distintos el sangrado hacia afuera y el margen de seguridad hacia adentro.",
    extend="Explica por qué una imagen de pantalla de 72 ppp puede verse bien en el computador y mal en el afiche impreso.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (OT y archivo recibido, de ejemplo). OT: volante A5 de 148 × 210 mm; sangrado de 3 mm por lado; modo CMYK; fotografías con 300 ppp o más a tamaño final; tipografías incrustadas; logotipo vectorial. "
     "Archivo recibido: tamaño 148 × 210 mm, sin sangrado; modo RGB; una fotografía de 800 píxeles de ancho impresa a 4 pulgadas de ancho; una tipografía sin incrustar; logotipo en mapa de bits de 150 ppp.")
build(
    O1, 3, F,
    use="Aprenderé a revisar un archivo contra la orden de trabajo, detectar incumplimientos con una revisión previa y registrar lo que hay que corregir.",
    prior=["Conozco sangrado, ppp, CMYK y vectorial.", "Sé calcular píxeles y ppp efectivos.", "Sé comparar una lista de requisitos con un archivo."],
    explain=[
        "La revisión previa, o preflight, es una lista de comprobaciones que se hace al archivo antes de mandarlo a impresión: tamaño, sangrado, modo de color, resolución de las imágenes, tipografías y tipo de logotipo. Cada punto se compara con la OT y se anota si cumple o no cumple. Una revisión sin registro no sirve, porque nadie sabe qué se comprobó.",
        "Incrustar una tipografía es guardarla dentro del archivo para que se vea igual en otro computador; si no está incrustada, el sistema puede reemplazarla por otra letra y cambiar el aspecto y los saltos de línea. Los ppp efectivos de una imagen se obtienen dividiendo sus píxeles por las pulgadas con que se imprimirá. Un logotipo en mapa de bits de baja resolución se verá borroso si se agranda.",
        "Si el archivo no cumple, el operador no corrige a escondidas: registra cada incumplimiento, avisa a la jefatura o al cliente y espera la corrección o una autorización escrita. Cambiar colores o imágenes sin avisar puede alterar lo que el cliente aprobó." + LIM,
    ],
    vocab=[("revisión previa (preflight)", "lista de comprobaciones del archivo antes de imprimir"), ("incrustar", "guardar la tipografía dentro del archivo"), ("ppp efectivos", "píxeles de la imagen divididos por las pulgadas de impresión"), ("incumplimiento", "punto que no cumple lo pedido en la OT"), ("registro", "anotación escrita de lo comprobado y decidido")],
    worked=[
        ("Calcular ppp efectivos", "Una imagen de ejemplo tiene 1.800 píxeles de ancho y se imprimirá a 6 pulgadas de ancho. ¿Cuántos ppp efectivos tiene?", ["ppp efectivos = píxeles ÷ pulgadas.", "1.800 ÷ 6 = 300."], "300 ppp"),
        ("Detectar un incumplimiento", "La OT de un trabajo de ejemplo pide CMYK y el archivo viene en RGB. ¿Cumple?", ["Se compara el modo pedido con el modo recibido.", "RGB es distinto de CMYK."], "No cumple el modo de color"),
    ],
    mistakes=[("Aprobar un archivo porque «el formato está bien», sin mirar los demás puntos.", "Cada requisito de la OT se comprueba por separado; un punto correcto no compensa los incumplidos.", "Revisa todos los puntos de la lista y anota cuáles cumplen y cuáles no."),
              ("Cambiar el modo de color del archivo sin avisar a nadie.", "El cliente aprobó un aspecto; un cambio de modo puede variar los colores y no queda registro.", "Registra el incumplimiento, avisa y espera la autorización antes de modificar.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una revisión previa (preflight) de un archivo?", "Una lista de comprobaciones que se hace antes de imprimir, comparando el archivo con la OT", "La impresión de una prueba en papel", "El corte final del impreso", "La revisión previa verifica el archivo contra la OT antes de gastar papel y tinta."),
        ("abc", "{F} ¿Qué modo de color pide la OT?", "CMYK", "RGB", "Escala de grises", "La OT exige CMYK; RGB es el modo del archivo recibido, no el pedido."),
        ("abc", "En Gráfica: ¿qué significa incrustar una tipografía?", "Guardarla dentro del archivo para que se vea igual en otro computador", "Hacerla más grande en la página", "Cambiarla por otra más liviana", "Una tipografía incrustada viaja con el archivo y no se reemplaza por otra."),
        ("abc", "{F} ¿Qué sangrado pide la OT?", "3 mm por cada lado", "Ninguno", "10 mm por cada lado", "La OT pide 3 mm de sangrado y el archivo recibido no trae ninguno."),
        ("=", "{F} ¿Cuántos mm de ancho debería tener el archivo con el sangrado pedido?", "148+3+3", "Al ancho final se le suma el sangrado de ambos lados.", " mm"),
        ("abc", "{F} El logotipo llegó como mapa de bits de 150 ppp y la OT lo pide vectorial. ¿Qué se hace?", "Pedir al cliente el logotipo vectorial original antes de seguir", "Ampliarlo hasta que quepa", "Reemplazarlo por texto sin avisar", "Un mapa de bits de baja resolución no puede reemplazar a un logotipo vectorial sin perder calidad."),
        ("=", "{F} Para que la fotografía llegue a 300 ppp con el mismo tamaño de impresión, ¿cuántos píxeles de ancho necesitaría?", "4*300", "Los píxeles necesarios son las pulgadas de impresión por los ppp pedidos.", " píxeles"),
        ("abc", "{F} ¿Qué puede pasar al imprimir el volante con la tipografía sin incrustar?", "Que el sistema la reemplace por otra letra y cambien el aspecto y los saltos de línea", "Que la fotografía suba a 300 ppp", "Que el sangrado se agrande solo", "Sin incrustar, la letra puede sustituirse y el texto se acomoda distinto."),
        ("=", "{F} La lista de la OT tiene 6 condiciones: formato, sangrado, modo de color, resolución, tipografías y logotipo. El archivo cumple solo el formato. ¿Cuántas condiciones no cumple?", "6-1", "A las seis condiciones se les resta la que sí cumple.", " condiciones"),
        ("abc", "{F} Una compañera dice: «como el formato está bien, el archivo se puede aprobar». ¿Qué le respondes?", "Que incumple otros cinco puntos y debe devolverse con un registro de correcciones", "Que tiene razón: el formato es lo único que importa", "Que se aprueba si se imprime rápido", "Cada condición de la OT se revisa; con cinco incumplimientos el archivo no se aprueba."),
        ("abc", "Un operador de ejemplo cambia por su cuenta el modo de color de un archivo y no avisa. ¿Qué riesgo tiene?", "Los colores pueden variar frente a lo aprobado y no queda registro del cambio", "Ninguno, porque el cambio es automático y perfecto", "El papel cambiará de formato", "Cambiar sin aviso altera lo aprobado y deja el trabajo sin respaldo."),
        ("abc", "{F} El cliente no responde y la entrega es en 3 días. ¿Qué decisión responsable es la mejor?", "Registrar los incumplimientos, avisar a la jefatura y no imprimir hasta tener el archivo corregido o una autorización escrita", "Imprimir igual y no decir nada", "Corregir todo en silencio y decir que el archivo venía bien", "Avisar y registrar protege al taller y al cliente; ocultar el problema no lo resuelve."),
        ("=", "{F} El cliente corrige y envía una fotografía de 1.400 píxeles de ancho para los mismos 4 pulgadas de ancho. ¿Cuántos ppp efectivos tiene?", "1400/4", "Los ppp efectivos son los píxeles divididos por las pulgadas de impresión.", " ppp"),
    ],
    ctx=("abc", "En la revisión previa de un afiche de ejemplo aparece: «imagen de 72 ppp a tamaño final». El cliente dice: «en mi pantalla se ve perfecto». ¿Qué respondes?", "Que la pantalla disimula la baja resolución y en papel se verá borrosa, así que se necesita una imagen de más ppp", "Que entonces se imprime igual porque se ve bien en pantalla", "Que se agranda la imagen para que se note menos", "Las pantallas toleran baja resolución; en el impreso los puntos se notan."),
    sc=[
        ("En Gráfica: ¿cómo se calculan los ppp efectivos de una imagen?", "Dividiendo sus píxeles por las pulgadas de impresión", "Los ppp efectivos relacionan el tamaño de la imagen con el de la impresión."),
        ("¿Qué haces si encuentras un incumplimiento en el archivo?", "Lo registro y aviso antes de corregir", "El registro y el aviso dejan constancia y evitan cambios no aprobados."),
        ("¿Qué riesgo tiene una tipografía sin incrustar?", "Que se reemplace por otra letra", "El sistema sustituye la letra y cambia el aspecto del texto."),
    ],
    op=("Ficha de ejemplo. OT: marcapáginas de 60 × 180 mm, sangrado de 3 mm, CMYK, fotografías con 300 ppp o más. Archivo recibido: 60 × 180 mm, CMYK, sin sangrado, una fotografía de 900 píxeles de ancho que irá a 2 pulgadas de ancho. "
        "Escribe un informe de revisión previa con una fila por requisito (formato, sangrado, modo, resolución), indicando si cumple o no, y qué harías con los incumplimientos.",
        "Formato: cumple. Sangrado: no cumple, falta 3 mm por lado (archivo de 66 × 186 mm). Modo: cumple, CMYK. Resolución: cumple, 900 ÷ 2 = 450 ppp. Acción: registrar que falta el sangrado, avisar a la jefatura y pedir el archivo corregido antes de imprimir.",
        ["compara cada requisito con la OT", "calcula bien los ppp efectivos y el tamaño con sangrado", "propone registrar y avisar"],
        ["tabla de cuatro filas con cumple o no cumple y la acción"],
        ["decir que la resolución no cumple sin calcularla", "olvidar el sangrado", "corregir sin avisar"],
        "Pregunta: «¿cómo sabes que la resolución cumple?». Si solo dice 'tiene muchos píxeles', pídele que divida píxeles por pulgadas."),
    reinforce="Escribe una lista de cinco comprobaciones para revisar un archivo de un afiche y márcalas con «cumple» o «no cumple» según una ficha que inventes.",
    extend="Explica por qué la revisión previa se hace antes de imprimir y no después.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (alternativas de composición, de ejemplo, para un afiche A3 de una feria escolar). Alternativa 1: título 48 pt, texto 12 pt, 3 familias tipográficas, texto claro sobre fondo oscuro. "
     "Alternativa 2: título 60 pt, texto 14 pt, 2 familias tipográficas, texto negro sobre fondo blanco. Alternativa 3: título 60 pt, texto 8 pt, 2 familias tipográficas, texto gris claro sobre fondo blanco. "
     "Criterios del cliente: título de 54 pt o más, texto de 11 pt o más, máximo 2 familias tipográficas y buen contraste.")
build(
    O1, 4, F,
    use="Aprenderé a elegir entre alternativas de composición con criterios técnicos verificables (jerarquía, contraste, legibilidad) y a revisar los textos antes de aprobar.",
    prior=["Conozco el cuerpo y el interlineado en puntos.", "Sé comparar medidas con un mínimo.", "Sé revisar un archivo contra una lista."],
    explain=[
        "Un criterio técnico es una regla que se puede comprobar con un dato, como «el texto mide 11 pt o más». Es distinto del gusto personal: decir «me gusta más» no justifica una decisión. La jerarquía visual es el orden de importancia que se da a los elementos con el tamaño y el peso de las letras: el título debe verse primero. El contraste es la diferencia de claridad entre el texto y el fondo; con poco contraste, el texto cuesta leer.",
        "Una familia tipográfica es un diseño de letra con sus variantes (normal, cursiva, negrita). Usar muchas familias distintas en una página la vuelve desordenada; para variar conviene usar las variantes de una misma familia. Legibilidad es la facilidad para leer un texto, y depende del tamaño, el contraste y el interlineado.",
        "Antes de aprobar, se corrigen la ortografía y los datos (fechas, horas, nombres) del texto original, y se cita al autor de lo que no es propio. Para decidir, se comprueba cada alternativa contra cada criterio y se descartan las que fallan; la respuesta se escribe con los datos que la respaldan." + LIM,
    ],
    vocab=[("criterio técnico", "regla que se puede comprobar con un dato"), ("jerarquía visual", "orden de importancia dado con tamaño y peso de las letras"), ("contraste", "diferencia de claridad entre texto y fondo"), ("familia tipográfica", "diseño de letra con sus variantes: normal, cursiva y negrita"), ("legibilidad", "facilidad para leer un texto"), ("interlineado", "distancia entre una línea de texto y la siguiente")],
    worked=[
        ("Comprobar un mínimo", "Un cartel de ejemplo exige un título de 40 pt o más y el título mide 36 pt. ¿Cumple y cuánto le falta?", ["Se compara 36 pt con el mínimo de 40 pt.", "40 − 36 = 4."], "No cumple: le faltan 4 pt"),
        ("Distinguir criterio y gusto", "Un compañero dice «elijo la opción azul porque me gusta». ¿Es un criterio técnico?", ["Un criterio técnico se puede comprobar con un dato.", "«Me gusta» no se comprueba con ningún dato."], "No: es una preferencia"),
    ],
    mistakes=[("Elegir una alternativa «porque se ve más moderna» sin comprobar los criterios del cliente.", "Una preferencia no reemplaza criterios que se pueden medir; la alternativa elegida podría incumplirlos.", "Comprueba cada criterio con su dato y recién ahí compara el aspecto."),
              ("Usar el texto de otra persona sin decir quién lo escribió.", "Un texto tiene autor y sus derechos; omitirlo es una falta ética y puede ser una infracción.", "Cita a la autora o al autor y pide autorización si corresponde.")],
    T=[
        ("abc", "En Gráfica: ¿qué es la jerarquía visual?", "El orden de importancia que se da a los elementos con tamaño y peso de letra", "El número de páginas de un libro", "El tipo de papel que se usa", "La jerarquía visual guía la lectura: lo más importante se ve primero."),
        ("abc", "En Gráfica: ¿qué es el contraste entre texto y fondo?", "La diferencia de claridad entre ambos", "El tamaño del archivo", "La cantidad de tipografías usadas", "Con buen contraste, como negro sobre blanco, el texto se lee con facilidad."),
        ("abc", "¿Qué es una familia tipográfica?", "Un diseño de letra con sus variantes, como normal, cursiva y negrita", "Un conjunto de imágenes del mismo autor", "Un grupo de personas que diseñan juntas", "Las variantes de un mismo diseño forman una familia tipográfica."),
        ("abc", "{F} ¿Qué alternativa cumple todos los criterios del cliente?", "La alternativa 2", "La alternativa 1", "La alternativa 3", "La 2 tiene título de 60 pt, texto de 14 pt, dos familias y buen contraste; la 1 y la 3 fallan en algún criterio."),
        ("=", "{F} ¿Cuántos pt le faltan al título de la alternativa 1 para llegar al mínimo?", "54-48", "Al mínimo exigido se le resta el tamaño del título de esa alternativa.", " pt"),
        ("abc", "{F} ¿Por qué falla la alternativa 3 en contraste?", "Porque el texto gris claro sobre fondo blanco casi no se distingue", "Porque usa dos familias tipográficas", "Porque su título mide 60 pt", "Gris claro sobre blanco tiene poca diferencia de claridad; las otras características sí cumplen."),
        ("=", "{F} En la alternativa 2, un bloque de 7 líneas de texto tiene interlineado de 18 pt. ¿Cuántos pt de alto ocupa el bloque?", "7*18", "El alto es el número de líneas por el interlineado.", " pt"),
        ("abc", "{F} El cliente pide agregar una tercera familia tipográfica «para que se vea más variado». ¿Qué corresponde según los criterios?", "Explicar que el máximo es de 2 familias y proponer variar con negrita o cursiva de la misma familia", "Agregar la familia y no decir nada", "Quitar todo el texto del afiche", "El criterio limita a dos familias; las variantes de una familia permiten variar sin incumplirlo."),
        ("=", "{F} El afiche mide 420 mm de alto. El título ocupa 60 mm, la imagen 240 mm y el bloque de texto 70 mm. ¿Cuántos mm quedan para márgenes y espacios en blanco?", "420-60-240-70", "Al alto total se le restan los alturas de los tres elementos.", " mm"),
        ("abc", "{F} Una compañera elige la alternativa 1 «porque el fondo oscuro se ve moderno». ¿Cuál es el error de su razonamiento?", "Decide por gusto, no por los criterios, y esa alternativa incumple dos de ellos", "Ninguno, porque el fondo oscuro siempre cumple los criterios", "Eligió la alternativa con el título más grande", "La alternativa 1 tiene título de 48 pt y tres familias, así que no cumple todos los criterios."),
        ("abc", "Un diseñador de ejemplo compone un poema escrito por otra persona y no pone su nombre. ¿Qué falta en el trabajo?", "El crédito de la autora o el autor y, si corresponde, su autorización", "Un título más grande", "Más contraste en el fondo", "Un texto ajeno se usa con crédito y permiso, porque tiene derechos de autor."),
        ("abc", "{F} El cliente cambia el criterio del texto a 13 pt o más. ¿Qué pasa con la decisión?", "No cambia: la alternativa 2 sigue cumpliendo, con 14 pt", "Ahora ninguna alternativa cumple", "Pasa a ganar la alternativa 1", "Con 14 pt la alternativa 2 supera el nuevo mínimo; las otras siguen incumpliendo otros criterios."),
        ("Un texto de ejemplo dice «Feria de cienscias el sabado 14». ¿Cuántos errores de ortografía hay que corregir?", "2 errores: «ciencias» y «sábado»", "«cienscias» está mal escrita y «sábado» lleva tilde, así que son dos correcciones."),
    ],
    ctx=("abc", "Faltan 2 horas para enviar un afiche de ejemplo a impresión y notas que el horario escrito en el texto no coincide con el que dice el correo del cliente. ¿Qué haces?", "Preguntar al cliente cuál es el horario correcto y dejar el dato confirmado por escrito", "Elegir el horario que te parece más probable", "Quitar el horario del afiche para evitar el problema", "Los datos del texto original se confirman con quien los aporta, porque un error se imprime en toda la tirada."),
    sc=[
        ("En Gráfica: ¿qué es un criterio técnico?", "Una regla que se puede comprobar con un dato", "A diferencia del gusto, un criterio técnico permite verificar si se cumple."),
        ("¿Qué compruebas antes de aprobar un texto?", "Ortografía y datos como fechas y horas", "Un error de texto se repite en todos los ejemplares impresos."),
        ("¿Cómo varías el texto sin pasar el límite de familias?", "Con negrita o cursiva de la misma familia", "Las variantes de una familia no suman familias nuevas."),
    ],
    op=("Un cliente de ejemplo pide un cartel A3 con estos criterios: título de 50 pt o más, texto de 12 pt o más, máximo 2 familias y buen contraste. Opciones: P) título 54 pt, texto 12 pt, 2 familias, negro sobre blanco; Q) título 72 pt, texto 10 pt, 2 familias, negro sobre blanco; R) título 60 pt, texto 14 pt, 3 familias, negro sobre blanco. "
        "Evalúa cada opción contra cada criterio, elige una y escribe en tres líneas la recomendación con sus datos y una condición bajo la cual cambiarías la decisión.",
        "P cumple los cuatro criterios. Q falla en el texto (10 pt es menos de 12). R falla en las familias (3 es más de 2). Recomiendo P porque es la única que cumple todo. Cambiaría la decisión si el cliente subiera el mínimo del título sobre 54 pt, porque P dejaría de cumplir.",
        ["evalúa cada opción contra cada criterio", "elige una opción con datos y no con gusto", "indica una condición que cambiaría la decisión"],
        ["tabla de opciones por criterios y recomendación escrita"],
        ["elegir por gusto", "no revisar todos los criterios", "no dar ninguna condición de cambio"],
        "Pregunta: «¿qué dato descarta a Q?». Si no lo dice, pídele que marque en la tabla cada incumplimiento con su cifra."),
    reinforce="Elige un cartel que hayas visto y anota, sin copiarlo, si su título, su texto y su contraste cumplirían los criterios de esta clase.",
    extend="Explica por qué un criterio técnico ayuda a que dos personas lleguen a la misma decisión.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (trabajo de ejemplo, inventado). Un taller de ejemplo recibe la OT de 1.000 cajas de cartulina impresas a cuatro colores. Antes de imprimir la tirada completa, el cliente exige una prueba de color firmada. "
     "Tipos de prueba disponibles: prueba en pantalla (solo se ve en un monitor), prueba impresa (hoja impresa por un equipo digital calibrado) y prueba de máquina (hoja impresa en la máquina real). "
     "Costos de ejemplo: repetir una prueba impresa, $8.000; imprimir mal la tirada completa y rehacerla, $400.000. Participan el ejecutivo de ventas, el operador de preimpresión y el cliente.")
build(
    O2, 1, F,
    use="Aprenderé para qué sirve una prueba de color, qué tipos hay, quién la aprueba y qué riesgos tiene aprobar sin registro.",
    prior=["Conozco la orden de trabajo y las fases del proceso gráfico.", "Sé que la impresión usa tintas CMYK.", "Sé multiplicar y dividir."],
    explain=[
        "Una prueba de color es una muestra que anticipa cómo quedarán los colores del impreso, para que el cliente la revise y la apruebe antes de imprimir toda la tirada. La prueba en pantalla sirve para trabajar, pero no basta para aprobar: cada monitor muestra los colores algo distinto. La prueba impresa se hace con un equipo calibrado, es decir, ajustado para que dé resultados constantes, y la prueba de máquina se imprime en la máquina real.",
        "Una prueba aprobada solo sirve de respaldo si queda registrada: lleva el nombre de quien aprueba, la firma y la fecha. Aprobar «de palabra» o por mensaje sin constancia deja a todos sin respaldo si después hay un reclamo. Los colores se comparan con luz adecuada y siempre la misma, y se cuida la vista con pausas.",
        "Los controles de calidad de una prueba se hacen según la norma vigente y los estándares del taller. Si el cliente cambia un color después de firmar, se registra el cambio y se hace una nueva prueba." + LIM,
    ],
    vocab=[("prueba de color", "muestra que anticipa los colores del impreso para que el cliente la apruebe"), ("prueba en pantalla", "vista del color en un monitor; no basta para aprobar"), ("prueba de máquina", "hoja impresa en la máquina real"), ("calibrar", "ajustar un equipo para que dé resultados constantes"), ("tirada", "cantidad total de ejemplares que se imprimen"), ("registro de aprobación", "constancia escrita con nombre, firma y fecha de quien aprueba")],
    worked=[
        ("Costo de repetir pruebas", "En un trabajo de ejemplo cada prueba impresa cuesta $5.000 y se repite 2 veces. ¿Cuánto cuestan las repeticiones?", ["Se multiplica el costo de una prueba por las repeticiones.", "5.000 × 2 = 10.000."], "$10.000"),
        ("Elegir la prueba", "El cliente de un cartel de ejemplo quiere aprobar el color exacto del fondo. ¿Le sirve una prueba en pantalla?", ["Cada monitor muestra los colores algo distinto.", "Para aprobar un color se necesita una prueba impresa."], "No basta; conviene una prueba impresa"),
    ],
    mistakes=[("Imprimir la tirada porque «el cliente dijo por teléfono que estaba bien».", "Sin constancia escrita, nadie puede demostrar qué se aprobó si después hay un reclamo.", "Pide la prueba firmada o una aprobación escrita con fecha antes de imprimir."),
              ("Dar por aprobado un color visto solo en la pantalla del cliente.", "Los monitores no coinciden entre sí ni con el papel impreso.", "Haz una prueba impresa con equipo calibrado y apruébala por escrito.")],
    T=[
        ("abc", "En Gráfica: ¿para qué sirve una prueba de color?", "Para anticipar los colores del impreso y que el cliente los apruebe antes de imprimir la tirada", "Para cortar el papel al tamaño final", "Para calcular el precio del papel", "La prueba permite corregir antes de gastar papel y tinta en toda la tirada."),
        ("abc", "{F} ¿Qué tipo de prueba se imprime en la máquina real?", "La prueba de máquina", "La prueba en pantalla", "La prueba firmada", "Solo la prueba de máquina se imprime en la máquina real; la de pantalla se ve en un monitor."),
        ("abc", "En Gráfica: ¿qué significa calibrar un equipo?", "Ajustarlo para que dé resultados constantes", "Cambiarle las tintas por otras", "Apagarlo al terminar el día", "Un equipo calibrado entrega siempre los mismos colores para una misma orden."),
        ("abc", "{F} ¿Por qué una prueba en pantalla no basta para que el cliente apruebe los colores?", "Porque cada monitor muestra los colores algo distinto y no equivale al papel impreso", "Porque la pantalla no muestra el color negro", "Porque las pantallas están prohibidas en el taller", "Los monitores varían entre sí y el papel no se comporta como una pantalla."),
        ("=", "{F} ¿Cuántas pruebas impresas repetidas cuestan lo mismo que rehacer una tirada completa mal impresa?", "400000//8000", "Se divide el costo de rehacer la tirada por el costo de una prueba.", " pruebas"),
        ("abc", "¿Qué datos hacen que una prueba aprobada sirva de respaldo?", "Nombre, firma y fecha de quien aprueba", "Solo el nombre del operador", "El tamaño del papel usado", "El registro de aprobación identifica quién aprobó y cuándo."),
        ("=", "{F} Para ajustar el color del cliente se necesitan 3 pruebas impresas repetidas. ¿Cuánto cuestan esas repeticiones?", "3*8000", "Se multiplican las repeticiones por el costo de cada prueba.", " pesos"),
        ("abc", "El ejecutivo de ventas dice: «el cliente aprobó por teléfono, imprimamos». ¿Qué falta antes de imprimir?", "Una constancia escrita de la aprobación, con fecha", "Cambiar el papel por uno más caro", "Hacer la prueba en pantalla otra vez", "Una aprobación oral no deja respaldo si hay un reclamo."),
        ("abc", "¿Qué condición ayuda a comparar bien dos colores en una prueba?", "Mirarlos con una luz adecuada y siempre la misma", "Mirarlos con la luz que haya en cada momento", "Mirarlos por separado en días distintos", "Con la luz cambiando, el mismo color parece distinto y la comparación pierde valor."),
        ("abc", "{F} Un compañero dice: «la prueba cuesta $8.000, conviene saltársela para ahorrar». ¿Qué respuesta es correcta?", "Un error en la tirada cuesta $400.000, mucho más que la prueba", "Tiene razón: $8.000 siempre es más que el ahorro", "Las pruebas no evitan errores", "Comparar los costos muestra que la prueba reduce el riesgo de perder la tirada."),
        ("abc", "El cliente cambia un color de fondo después de firmar la prueba. ¿Qué corresponde?", "Registrar el cambio, hacer una nueva prueba y obtener una nueva aprobación", "Imprimir con el color nuevo sin avisar", "Ignorar el cambio porque ya firmó", "Un cambio posterior anula lo aprobado y exige nueva prueba y registro."),
        ("abc", "La prueba impresa salió más oscura que el archivo. Antes de culpar al cliente, ¿qué conviene revisar?", "La calibración del equipo y el papel usado", "El nombre del archivo", "La fecha de entrega", "Un equipo mal calibrado o un papel distinto puede cambiar el color."),
        ("=", "{F} Cada ronda de prueba demora 45 minutos en prepararse y 15 minutos en revisarse. Si se hacen 2 rondas completas, ¿cuántos minutos se usan?", "(45+15)*2", "Se suma el tiempo de preparar y revisar y se multiplica por las rondas.", " minutos"),
    ],
    ctx=("abc", "Un cliente de ejemplo te manda por mensaje una foto de su teléfono con la frase «así quiero el rojo» y te pide aprobar con eso. ¿Qué respondes?", "Que se hará una prueba impresa y que su aprobación debe quedar firmada y con fecha", "Que imprimes de inmediato porque ya lo dijo", "Que la foto reemplaza a la prueba de color", "La pantalla de un teléfono no muestra el color impreso y el mensaje no es un registro firmado."),
    sc=[
        ("En Gráfica: ¿qué es una prueba de color?", "Una muestra que anticipa los colores del impreso", "Sirve para que el cliente apruebe antes de imprimir toda la tirada."),
        ("¿Qué debe llevar una aprobación para servir de respaldo?", "Nombre, firma y fecha", "Sin esos tres datos no se sabe quién aprobó ni cuándo."),
        ("¿Qué haces si el cliente cambia un color después de aprobar?", "Registro el cambio y hago una nueva prueba", "El cambio posterior anula la aprobación anterior y exige otra."),
    ],
    op=("Un taller de ejemplo debe imprimir 5.000 bolsas de papel con un verde de marca. Cada prueba impresa cuesta $6.000 y rehacer toda la tirada mal impresa cuesta $350.000. El cliente solo envió una foto del verde desde su teléfono. "
        "Escribe: qué tipo de prueba pedirías y por qué, cuántas pruebas completas de $6.000 se podrían pagar con el costo de rehacer la tirada (división entera) y tres datos que debe llevar la aprobación.",
        "Pediría una prueba impresa con equipo calibrado, porque la foto de un teléfono no muestra el color impreso. Con $350.000 se pagan 58 pruebas de $6.000 (58 × 6.000 = 348.000). La aprobación lleva nombre de quien aprueba, firma y fecha.",
        ["elige una prueba impresa y explica por qué la foto no basta", "calcula la división entera con su comprobación", "nombra tres datos de la aprobación"],
        ["hoja con la elección, el cálculo y los tres datos"],
        ["aceptar la foto como prueba", "olvidar la fecha o la firma", "calcular mal la división"],
        "Pregunta: «¿por qué la foto de un teléfono no es una prueba?». Si responde 'es pequeña', vuelve a la idea de que cada pantalla muestra el color distinto."),
    reinforce="Escribe una lista de cuatro datos que debe tener una hoja de aprobación de prueba de color, e inventa un ejemplo completo.",
    extend="Explica con un ejemplo inventado cuándo conviene una prueba de máquina en vez de una prueba impresa digital.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (glosario y costos de ejemplo, inventados). Película (o fotolito): lámina transparente con el diseño de una tinta, usada en algunos procesos para pasar la imagen a la matriz. "
     "Matriz de impresión: pieza que lleva la imagen que se transfiere al papel; en offset es una plancha y en serigrafía una malla; muchas matrices de offset hoy se hacen directamente del archivo, sin película. "
     "Impreso digital: impresión directa del archivo, sin matriz, útil para tiradas cortas. Tira de control: franja de parches de color impresa en el borde para medir. Tolerancia: diferencia máxima aceptada. "
     "Costos de ejemplo: offset, 4 matrices de $25.000 cada una más $20 por ejemplar; digital, $120 por ejemplar y ninguna matriz.")
build(
    O2, 2, F,
    use="Aprenderé qué son la prueba de color, la película, la matriz de impresión y el impreso digital, en qué se diferencian y cómo se compara su costo.",
    prior=["Sé para qué sirve una prueba de color.", "Conozco las cuatro tintas CMYK.", "Sé calcular costos con multiplicaciones."],
    explain=[
        "La matriz de impresión es la pieza que lleva la imagen para pasarla al papel. En offset es una plancha y hay una por cada tinta; en una impresión a cuatro colores se necesitan cuatro matrices. La película o fotolito es una lámina transparente con el diseño de una tinta que, en algunos procesos, se usa para pasar la imagen a la matriz; muchas matrices de offset hoy se hacen directamente del archivo y no usan película.",
        "El impreso digital imprime el archivo directamente, sin matriz. Por eso no tiene el costo inicial de fabricar matrices y conviene en tiradas cortas, aunque cada ejemplar sale más caro. En una tirada larga, el costo inicial de las matrices se reparte entre muchos ejemplares y el offset resulta más barato por unidad. Para comparar se calcula el costo total de cada opción para la misma cantidad.",
        "Cada pieza se controla: se mide la tira de control y se compara con la tolerancia, que es la diferencia máxima aceptada. Estos son conceptos para leer una orden de trabajo, no instrucciones para operar equipos." + LIM,
    ],
    vocab=[("matriz de impresión", "pieza que lleva la imagen que se transfiere al papel"), ("película (fotolito)", "lámina transparente con el diseño de una tinta"), ("impreso digital", "impresión directa del archivo, sin matriz"), ("tira de control", "franja de parches de color impresa para medir"), ("tolerancia", "diferencia máxima aceptada"), ("costo inicial", "gasto que se paga una vez antes de imprimir, como las matrices")],
    worked=[
        ("Matrices de un trabajo", "Un trabajo de ejemplo se imprime en offset con 3 tintas. ¿Cuántas matrices se necesitan?", ["Hay una matriz por cada tinta.", "3 tintas → 3 matrices."], "3 matrices"),
        ("Costo en offset", "Un trabajo de ejemplo usa matrices por $60.000 y cuesta $10 por ejemplar. ¿Cuánto cuestan 2.000 ejemplares?", ["Costo = matrices + ejemplares × costo unitario.", "60.000 + 2.000 × 10 = 80.000."], "$80.000"),
    ],
    mistakes=[("Elegir siempre impreso digital «porque no usa matrices», sin mirar la cantidad.", "En tiradas largas el costo por ejemplar del digital puede superar al offset con matrices repartidas.", "Calcula el costo total de cada opción para la cantidad pedida."),
              ("Creer que la película y la matriz son lo mismo.", "La película es una lámina con el diseño de una tinta; la matriz es la pieza que lleva la imagen al papel.", "Recuerda: la película puede ayudar a hacer la matriz, pero no la reemplaza.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una matriz de impresión?", "La pieza que lleva la imagen que se transfiere al papel", "La hoja de prueba que firma el cliente", "La tira de control de color", "La matriz lleva la imagen al papel; la prueba la firma el cliente."),
        ("abc", "En Gráfica: ¿qué es el impreso digital?", "Una impresión directa del archivo, sin matriz", "Una impresión con una matriz por cada tinta", "Una prueba hecha en pantalla", "El impreso digital va del archivo al papel y por eso no tiene el costo de matrices."),
        ("abc", "¿Qué es la tolerancia en el control de calidad?", "La diferencia máxima que se acepta respecto del valor pedido", "El precio de la prueba", "El tamaño del papel", "La tolerancia fija hasta dónde se acepta una desviación."),
        ("=", "{F} Un trabajo de offset se imprime a cuatro colores. ¿Cuánto cuestan sus matrices?", "4*25000", "Se multiplican las cuatro matrices por el costo de cada una.", " pesos"),
        ("abc", "{F} ¿Qué ventaja tiene el impreso digital para una tirada muy corta?", "No exige fabricar matrices", "Siempre cuesta menos por ejemplar", "Usa una matriz por cada tinta", "Sin matriz no hay costo inicial de matrices, lo que favorece tiradas cortas."),
        ("abc", "{F} ¿Para qué sirve la tira de control?", "Para medir parches de color y comparar con la tolerancia", "Para cortar el papel", "Para guardar la firma del cliente", "La tira de control lleva parches medibles en el borde del impreso."),
        ("=", "{F} Se pide una tirada de 500 ejemplares. ¿Cuánto cuesta en total con impreso digital?", "500*120", "Se multiplica la cantidad de ejemplares por el costo de cada uno.", " pesos"),
        ("=", "{F} Se pide la misma tirada de 500 ejemplares. ¿Cuánto cuesta en total con offset?", "4*25000+500*20", "Se suman las matrices y el costo de los ejemplares.", " pesos"),
        ("abc", "{F} Para 500 ejemplares, ¿qué opción tiene menor costo total?", "El impreso digital, con $60.000 frente a $110.000", "El offset, con $110.000 frente a $60.000", "Cuestan lo mismo", "Digital cuesta 500 × 120 = 60.000 y offset 100.000 + 10.000 = 110.000."),
        ("abc", "{F} Un compañero dice: «la película y la matriz son lo mismo». ¿Qué le respondes?", "La película es una lámina con el diseño de una tinta y la matriz es la pieza que lleva la imagen al papel", "Tiene razón, son lo mismo", "La película es la tinta líquida y la matriz es el papel", "Son piezas distintas: la película puede ayudar a obtener la matriz, pero no es la matriz."),
        ("abc", "Un cliente de ejemplo dice que prefiere offset porque «las matrices no cuestan nada». ¿Qué error tiene?", "Las matrices tienen un costo inicial que debe sumarse al total", "Ninguno, porque las matrices son gratis", "El offset no usa tintas", "Las matrices se fabrican y su costo inicial forma parte del total."),
        ("abc", "{F} En una tirada muy larga, ¿por qué el offset suele resultar más barato por ejemplar?", "Porque el costo de las matrices se reparte entre muchos ejemplares", "Porque no necesita papel", "Porque el costo por ejemplar es el mismo que el del digital", "Al repartir el costo inicial en muchos ejemplares, el costo por unidad baja."),
        ("=", "{F} Se pide una tirada de 2.000 ejemplares. ¿Cuántos pesos más cuesta el digital que el offset?", "2000*120-(4*25000+2000*20)", "Se calcula el costo total de cada opción y se restan.", " pesos"),
    ],
    ctx=("abc", "Una escuela de ejemplo pide 100 invitaciones para el lunes y otra escuela pide 20.000 volantes para el mes. ¿Cómo conviene asignar los procesos según la ficha?", "Digital para las 100 invitaciones y offset para los 20.000 volantes", "Offset para las 100 invitaciones y digital para los 20.000 volantes", "Digital para ambos, porque no usa matrices", "En tiradas cortas pesa el costo inicial de las matrices; en tiradas largas se reparte entre muchos ejemplares."),
    sc=[
        ("En Gráfica: ¿cuántas matrices usa un offset a cuatro colores en esta ficha?", "Cuatro", "En offset se fabrica una matriz distinta por cada tinta usada."),
        ("¿Qué proceso no usa matriz?", "El impreso digital", "El archivo se imprime directamente, sin fabricar ninguna matriz antes."),
        ("¿Qué compara la tolerancia?", "Una medida con el valor pedido", "Muestra cuánta diferencia entre lo medido y lo pedido se acepta."),
    ],
    op=("Un taller de ejemplo cotiza 300 afiches de ejemplo a cuatro colores. Offset: 4 matrices de $25.000 cada una más $20 por ejemplar. Digital: $120 por ejemplar, sin matrices. "
        "Calcula el costo total de cada proceso para 300 afiches, indica cuál conviene y escribe una frase que explique por qué el resultado cambiaría con una tirada de 5.000.",
        "Offset: 4 × 25.000 + 300 × 20 = 106.000. Digital: 300 × 120 = 36.000. Conviene el digital. Con 5.000 afiches el costo inicial de las matrices se reparte entre muchos ejemplares y el offset se vuelve más barato por unidad.",
        ["calcula bien ambos costos", "elige la opción más barata para 300", "explica el efecto de la cantidad"],
        ["hoja con ambos cálculos, la elección y la frase"],
        ["olvidar sumar las matrices", "no multiplicar por la cantidad", "no explicar por qué cambia con la tirada"],
        "Pregunta: «¿qué costo se paga una sola vez?». Si no nombra las matrices, vuelve al concepto de costo inicial."),
    reinforce="Haz una tabla de dos columnas, offset y digital, con una ventaja y una limitación de cada uno según esta ficha.",
    extend="Explica por qué el costo inicial hace que la cantidad pedida sea un dato clave para elegir proceso.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (mediciones de ejemplo, inventadas). Tira de control de una prueba de color. Valores objetivo de densidad, en unidades arbitrarias de ejemplo: cian 140, magenta 135, amarillo 100, negro 170. Tolerancia: ± 5 unidades. "
     "Valores medidos en la prueba: cian 143, magenta 128, amarillo 102, negro 168. La densidad es una medida de cuánta tinta tiene un parche; cada valor se compara con su objetivo.")
build(
    O2, 3, F,
    use="Aprenderé a analizar una tira de control: comparar lo medido con el valor objetivo y la tolerancia, decidir si cumple y registrar la decisión.",
    prior=["Conozco la prueba de color y la tolerancia.", "Sé restar y comparar números.", "Sé leer una tabla."],
    explain=[
        "Una tira de control es una franja de parches que se imprime junto al trabajo. Cada parche se mide y el valor obtenido se compara con el valor objetivo que fija el estándar o la orden de trabajo. La densidad es una medida de cuánta tinta tiene el parche. La diferencia se calcula restando el valor menor al mayor, es decir, tomando el resultado sin signo.",
        "La tolerancia es la diferencia máxima aceptada. Si la diferencia es igual o menor que la tolerancia, el parche cumple; si es mayor, no cumple, aunque se vea parecido. Una prueba se aprueba solo si cumple todos sus parches; un solo parche fuera de tolerancia obliga a revisar antes de aprobar.",
        "Lo medido se anota en un registro con la fecha y el nombre de quien midió. El operador no corrige sin avisar: informa al responsable y deja constancia. Los valores de esta ficha son de ejemplo; en un trabajo real los fija el estándar vigente." + LIM,
    ],
    vocab=[("tira de control", "franja de parches de color que se mide"), ("valor objetivo", "valor que debería tener el parche"), ("densidad", "medida de cuánta tinta tiene un parche"), ("diferencia", "distancia entre el valor medido y el objetivo, sin signo"), ("tolerancia", "diferencia máxima aceptada"), ("registro", "anotación escrita de lo medido y decidido")],
    worked=[
        ("Parche dentro de tolerancia", "Un parche de ejemplo debe medir 120, la tolerancia es ± 4 y mide 123. ¿Cumple?", ["Diferencia: 123 − 120 = 3.", "3 es menor que 4."], "Sí, cumple"),
        ("Parche fuera de tolerancia", "Otro parche de ejemplo debe medir 90, la tolerancia es ± 4 y mide 83. ¿Cumple?", ["Diferencia sin signo: 90 − 83 = 7.", "7 es mayor que 4."], "No cumple"),
    ],
    mistakes=[("Aprobar la prueba porque «se ve parecida» aunque un parche supera la tolerancia.", "La decisión se toma con la medición, no con la impresión visual.", "Compara cada parche con su tolerancia y anota el resultado."),
              ("Restar al revés y concluir que la diferencia es negativa y por eso cumple.", "La diferencia se toma sin signo: importa cuánto se aleja, no hacia dónde.", "Usa la diferencia sin signo para compararla con la tolerancia.")],
    T=[
        ("abc", "En Gráfica: ¿qué es la densidad de un parche?", "Una medida de cuánta tinta tiene el parche", "El tamaño del papel", "El nombre de la tinta", "La densidad se mide en el parche y se compara con el valor objetivo."),
        ("abc", "{F} ¿Cuál es el valor objetivo del negro?", "170", "168", "135", "El objetivo del negro es 170; 168 es lo que se midió."),
        ("abc", "{F} ¿Cuál es la tolerancia de la ficha?", "± 5 unidades", "± 10 unidades", "± 1 unidad", "La ficha fija una tolerancia de más o menos 5."),
        ("=", "{F} ¿Cuál es la diferencia sin signo del cian entre lo medido y el objetivo?", "143-140", "Se resta el valor menor al mayor.", " unidades"),
        ("=", "{F} ¿Cuál es la diferencia sin signo del magenta entre lo medido y el objetivo?", "135-128", "Se resta el valor menor al mayor para obtener un número sin signo.", " unidades"),
        ("abc", "{F} ¿Qué parche está fuera de tolerancia?", "El magenta", "El cian", "El negro", "La diferencia del magenta es 7, mayor que 5; las del cian, amarillo y negro son 3, 2 y 2."),
        ("=", "{F} ¿Cuántos parches de los cuatro cumplen la tolerancia?", "4-1", "A los cuatro parches se les resta el que no cumple.", " parches"),
        ("abc", "{F} ¿Se puede aprobar la prueba tal como está?", "No, porque un parche supera la tolerancia", "Sí, porque tres de cuatro cumplen", "Sí, si se ve parecida", "La prueba se aprueba solo si todos los parches cumplen."),
        ("abc", "{F} Si el amarillo midiera 106, ¿cumpliría?", "No: la diferencia sería 6, mayor que 5", "Sí: la diferencia sería 5", "Sí: 106 es mayor que 100", "El valor 106 se aleja 6 unidades del objetivo, más que la tolerancia."),
        ("abc", "{F} Una compañera dice: «el magenta está solo 7 bajo el objetivo, a simple vista se ve igual». ¿Qué respondes?", "La decisión se toma con la medición y 7 supera la tolerancia de 5", "Tiene razón: si se ve igual se aprueba", "Que el magenta no se mide", "La tolerancia mide el límite aceptable y no la impresión visual."),
        ("abc", "El operador de ejemplo midió un parche fuera de tolerancia. ¿Qué hace de forma responsable?", "Lo anota, avisa al responsable y espera una decisión", "Cambia el valor anotado para que cumpla", "Imprime la tirada completa igual", "Alterar un registro o ignorar el problema dañan la confianza y la calidad."),
        ("abc", "{F} Una medición nueva da: cian 139, magenta 133, amarillo 104, negro 172. ¿Cumple la prueba?", "Sí: las diferencias son 1, 2, 4 y 2", "No: el magenta bajó", "No: el negro supera su objetivo", "Todas las diferencias son iguales o menores que 5, así que cada parche cumple."),
        ("=", "{F} En otra medición el magenta mide 138. ¿A cuántas unidades del objetivo queda?", "138-135", "Se resta el valor menor al mayor.", " unidades"),
    ],
    ctx=("abc", "El cliente de ejemplo ve la prueba de la ficha y dice: «yo la veo bien, aprobada». Tu medición muestra el magenta fuera de tolerancia. ¿Qué haces?", "Muestro la medición, aviso al responsable y propongo corregir y repetir la prueba antes de aprobar", "Imprimo la tirada porque el cliente ya aprobó", "Anoto que el magenta cumple para evitar problemas", "La medición objetiva y el registro respaldan la decisión; ocultar el dato no resuelve el problema."),
    sc=[
        ("En Gráfica: ¿cuándo cumple un parche?", "Cuando su diferencia es igual o menor que la tolerancia", "La tolerancia es la diferencia máxima aceptada para cada parche."),
        ("¿Cuántos parches deben cumplir para aprobar una prueba?", "Todos", "Un solo parche fuera de tolerancia obliga a revisar antes de aprobar."),
        ("¿Qué haces con una medición fuera de tolerancia?", "La anoto y aviso al responsable", "El registro honesto de lo medido permite decidir y corregir después."),
    ],
    op=("Tira de ejemplo: valores objetivo cian 150, magenta 120, amarillo 95, negro 180; tolerancia ± 6. Valores medidos: cian 155, magenta 112, amarillo 97, negro 186. "
        "Calcula la diferencia de cada parche, indica cuáles cumplen y cuáles no, y escribe lo que anotarías en el registro y a quién avisarías.",
        "Cian: 5, cumple. Magenta: 8, no cumple. Amarillo: 2, cumple. Negro: 6, cumple porque es igual a la tolerancia. Registro: «magenta fuera de tolerancia, diferencia 8 con tolerancia 6; no se aprueba; se avisa al responsable de preimpresión y se repite la prueba».",
        ["calcula bien las cuatro diferencias", "aplica el criterio igual o menor para el negro", "escribe un registro con aviso"],
        ["tabla con valores, diferencias y resultado, más el registro"],
        ["restar mal o con signo", "considerar que el negro no cumple por igual a la tolerancia", "no avisar al responsable"],
        "Pregunta: «¿por qué el negro cumple si midió 6?». Si dice que no, repasa que la tolerancia incluye el valor límite."),
    reinforce="Inventa una tira con cuatro valores objetivo, una tolerancia y mediciones; calcula las diferencias y marca cuáles cumplen.",
    extend="Explica por qué la medición es más confiable que la mirada para decidir si una prueba cumple.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (decisión de ejemplo). Trabajo: 50 muestras impresas con equipo digital para un catálogo. Criterio del taller: se acepta el lote si al menos 90 de cada 100 muestras están conformes. "
     "Resultado de la revisión: 4 muestras con manchas, todas las demás conformes. Costos de ejemplo: repetir las 4 muestras defectuosas, $12.000; repetir las 50 muestras, $150.000; entregar sin repetir, con probable reclamo del cliente. "
     "La matriz de una tirada posterior se compara con la prueba aprobada antes de imprimir.")
build(
    O2, 4, F,
    use="Aprenderé a aplicar un criterio de aceptación con porcentajes y costos, a decidir si un lote se acepta y a dejar la decisión registrada.",
    prior=["Sé calcular diferencias y tolerancias.", "Conozco la prueba de color, la matriz y el impreso digital.", "Sé calcular porcentajes simples."],
    explain=[
        "Un criterio de aceptación es la regla que fija cuándo un lote o una prueba se da por buena. Un ejemplo es aceptar un lote si al menos el 90 % de las muestras están conformes. Un porcentaje se calcula multiplicando la parte por 100 y dividiéndola por el total: si de 50 muestras 46 son conformes, el porcentaje es 46 × 100 ÷ 50 = 92 %.",
        "Si el lote cumple el criterio, se acepta, y las muestras defectuosas se separan y se registran. Si no lo cumple, se decide entre alternativas con datos: costo de repetir, plazo y riesgo de reclamo. También se compara la matriz de una tirada posterior con la prueba aprobada, para asegurar que lo que se imprimirá coincide con lo que el cliente firmó.",
        "La decisión se escribe con los datos que la respaldan (porcentaje, costos y plazo) y con quién la aprobó. Una decisión sin registro puede repetir el problema más adelante." + LIM,
    ],
    vocab=[("criterio de aceptación", "regla que fija cuándo un lote se da por bueno"), ("lote", "grupo de muestras o ejemplares revisados juntos"), ("conforme", "que cumple lo pedido"), ("defectuoso", "que no cumple lo pedido"), ("porcentaje", "parte por cada 100 del total")],
    worked=[
        ("Calcular un porcentaje", "En un lote de ejemplo de 40 hojas, 36 están conformes. ¿Qué porcentaje es conforme?", ["Porcentaje = conformes × 100 ÷ total.", "36 × 100 ÷ 40 = 90."], "90 %"),
        ("Aplicar el criterio", "Un lote de ejemplo tiene 85 % conforme y el criterio exige 90 % o más. ¿Se acepta?", ["Se compara 85 con 90.", "85 es menor que 90."], "No se acepta"),
    ],
    mistakes=[("Aceptar el lote porque «solo hay unas pocas manchas» sin calcular el porcentaje.", "El criterio se aplica con un dato: «pocas» no es una cifra y cada persona la interpreta distinto.", "Calcula el porcentaje conforme y compáralo con el mínimo."),
              ("Entregar en silencio las muestras defectuosas «para que no se note».", "Ocultar defectos afecta al cliente y a la confianza; además no queda registro.", "Sepáralas, regístralas y decide con la jefatura qué hacer.")],
    T=[
        ("abc", "En Gráfica: ¿qué es un criterio de aceptación?", "La regla que fija cuándo un lote se da por bueno", "El nombre de la máquina de impresión", "El color más usado en el trabajo", "El criterio de aceptación convierte la calidad en una regla comprobable."),
        ("abc", "{F} ¿Qué porcentaje mínimo de muestras conformes exige el taller?", "90 de cada 100", "50 de cada 100", "100 de cada 100", "El criterio de la ficha es de al menos 90 conformes por cada 100."),
        ("=", "{F} ¿Cuántas muestras conformes hay?", "50-4", "Al total de muestras se le restan las defectuosas.", " muestras"),
        ("=", "{F} ¿Qué porcentaje de las 50 muestras está conforme?", "46*100//50", "Se multiplica la parte conforme por 100 y se divide por el total.", " %"),
        ("abc", "{F} ¿Se acepta el lote según el criterio?", "Sí, porque 92 % supera el mínimo de 90 %", "No, porque hay muestras con manchas", "No, porque 92 es menor que 90", "El criterio no exige cero defectos, sino al menos 90 % conforme."),
        ("abc", "Para un lote de ejemplo de 20 muestras, el criterio pide 90 % y hay 17 conformes. ¿Qué porcentaje es?", "85 %", "90 %", "17 %", "17 × 100 ÷ 20 = 85, menor que el 90 % exigido."),
        ("=", "{F} Si el lote fuera de 200 muestras con 12 defectuosas, ¿qué porcentaje estaría conforme?", "(200-12)*100//200", "Se resta lo defectuoso, se multiplica por 100 y se divide por el total.", " %"),
        ("abc", "{F} ¿Qué diferencia de costo hay entre repetir las 4 muestras defectuosas y repetir las 50 muestras?", "Repetir solo las defectuosas ahorra $138.000", "Repetir las 50 ahorra $138.000", "No hay diferencia", "150.000 − 12.000 = 138.000 de ahorro al repetir solo las defectuosas."),
        ("abc", "{F} Si el lote cumple el criterio, ¿qué se hace con las 4 muestras defectuosas?", "Separarlas, registrarlas y decidir con la jefatura si se reponen", "Mezclarlas con las demás para entregar todo junto", "Botarlas sin dejar registro", "Los defectos se separan y registran, aunque el lote se acepte."),
        ("abc", "{F} Un compañero dice: «con una mancha ya hay que repetir todo el lote». ¿Qué le respondes?", "El criterio del taller acepta el lote con al menos 90 % conforme, y aquí hay 92 %", "Tiene razón, todo lote con una mancha se descarta", "Que las manchas no importan nunca", "La decisión sigue el criterio acordado y no la impresión de una sola muestra."),
        ("abc", "El cliente pide que el lote tenga 100 % conforme sin cambiar el plazo ni el costo. ¿Qué corresponde?", "Explicar que cambiar el criterio implica costo y plazo, y acordarlo por escrito", "Aceptar sin decir nada y arreglarlo después", "Rechazar toda conversación", "Cambiar un criterio afecta recursos y debe acordarse con registro."),
        ("abc", "Antes de imprimir una tirada posterior, ¿qué conviene comparar con la prueba aprobada?", "La matriz o el archivo que se usará", "El precio del papel", "El nombre del cliente", "Se verifica que lo que se imprimirá coincide con lo aprobado."),
        ("=", "{F} Si se acepta el lote y se repiten solo las 4 muestras defectuosas, ¿cuánto cuesta cada muestra repetida?", "12000//4", "Se divide el costo total de repetir por el número de muestras.", " pesos"),
    ],
    ctx=("abc", "Tu lote de ejemplo tiene 80 % conforme, el criterio pide 90 % y el cliente retira el pedido en 2 horas. ¿Qué haces?", "Informar a la jefatura con los datos y proponer repetir lo defectuoso, dejando registrada la decisión", "Entregar el lote sin avisar", "Cambiar el porcentaje en el informe a 90 %", "Con el criterio incumplido se informa, se propone una solución y se registra; alterar datos es una falta."),
    sc=[
        ("En Gráfica: ¿cómo se calcula el porcentaje conforme?", "Conformes por 100 dividido por el total", "Es la parte que corresponde a cada 100 del total revisado."),
        ("¿Qué haces con el lote si cumple el criterio?", "Lo acepto y registro los defectos", "Aceptar el lote no implica olvidar ni ocultar las muestras defectuosas."),
        ("¿Qué pasa si cambias el criterio a petición del cliente?", "Se acuerda por escrito, con su costo y plazo", "Cambiar el criterio modifica el trabajo y debe quedar registrado."),
    ],
    op=("Un taller de ejemplo revisa 60 invitaciones impresas con equipo digital. El criterio pide 90 % conforme o más. Hay 6 invitaciones defectuosas. Repetir las 6 cuesta $9.000 y repetir las 60 cuesta $72.000. "
        "Calcula el porcentaje conforme, decide si se acepta el lote, calcula el ahorro de repetir solo las defectuosas y escribe qué anotarías en el registro.",
        "Conformes: 60 − 6 = 54; 54 × 100 ÷ 60 = 90 %, que es igual al mínimo: se acepta. Ahorro de repetir solo las 6: 72.000 − 9.000 = 63.000. Registro: «lote aceptado con 90 % conforme; 6 invitaciones defectuosas separadas y repuestas; aprobó la jefatura».",
        ["calcula el porcentaje con el criterio correcto", "calcula el ahorro con claridad", "escribe un registro con datos y responsable"],
        ["hoja con los cálculos, la decisión y el registro"],
        ["olvidar restar las defectuosas", "decidir sin calcular", "registrar sin datos ni responsable"],
        "Pregunta: «¿qué dato respalda tu decisión?». Si dice 'se ve bien', pídele que muestre el porcentaje."),
    reinforce="Inventa un lote de 25 muestras con algunas defectuosas, calcula el porcentaje conforme y decide si se acepta con el criterio de 90 %.",
    extend="Explica por qué un criterio de aceptación escrito evita discusiones entre el taller y el cliente.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (OT de ejemplo, inventada). Trabajo: 2.000 etiquetas adhesivas de 100 × 60 mm para frascos de un producto de ejemplo, impresas por una cara. Insumos pedidos: papel adhesivo de 80 g/m², tinta indicada en la ficha técnica del fabricante y un barniz de protección. "
     "Documentos: la OT, la ficha técnica de cada insumo y la hoja de datos de seguridad (HDS) de tintas y barniz. Bodega: los insumos se guardan rotulados con nombre y fecha de recepción; los residuos de tinta y los trapos con restos van a un contenedor rotulado, no al desagüe ni a la basura común. "
     "Cada hoja trae 20 etiquetas; el taller pide un 5 % de hojas extra por merma.")
build(
    O3, 1, F,
    use="Aprenderé qué son las materias primas e insumos de un trabajo gráfico, qué documentos los respaldan y qué cuidados de seguridad, registro y ambiente exigen.",
    prior=["Conozco la orden de trabajo y sus datos.", "Sé calcular porcentajes simples.", "Sé leer una ficha de datos."],
    explain=[
        "Las materias primas y los insumos son todo lo que se consume para producir: el sustrato (el material sobre el que se imprime, como papel o cartulina), las tintas, los barnices y los productos de limpieza. Seleccionar es elegir el que pide la orden de trabajo (OT) y acondicionar es dejarlo en condiciones de usarse: identificado, vigente y bien guardado. La ficha técnica del fabricante dice para qué sirve cada insumo y cómo se usa; la hoja de datos de seguridad (HDS) informa sus riesgos, cómo guardarlo y qué hacer en una emergencia.",
        "Todo insumo se rotula con su nombre y su fecha de recepción, y no se usa si está vencido o sin identificar. La merma es la cantidad extra que se pide porque parte del material se pierde en pruebas y ajustes; en esta ficha es el 5 % de las hojas. Los residuos de tinta o solventes no se vierten al desagüe: se guardan en contenedores rotulados según la norma vigente y las indicaciones de la empresa.",
        "Nunca se reemplaza un insumo de la OT por otro «parecido» sin consultar a quien responde, porque cambia la calidad, el costo y la seguridad. No se guardan productos químicos en envases de alimentos o bebidas." + MAQ,
    ],
    vocab=[("sustrato", "material sobre el que se imprime"), ("insumo", "material que se consume para producir, como tinta o barniz"), ("acondicionar", "dejar un material identificado, vigente y listo para usarse"), ("ficha técnica", "documento del fabricante que explica para qué sirve y cómo se usa un insumo"), ("hoja de datos de seguridad (HDS)", "documento con los riesgos de un producto y cómo guardarlo y actuar en una emergencia"), ("merma", "cantidad de material que se pierde en pruebas y ajustes"), ("rotular", "poner nombre y fecha a un envase")],
    worked=[
        ("Calcular la merma", "Un trabajo de ejemplo necesita 200 hojas y se pide un 10 % extra por merma. ¿Cuántas hojas se piden?", ["El 10 % de 200 es 20.", "200 + 20 = 220."], "220 hojas"),
        ("Qué documento consultar", "Quieres saber cómo guardar un barniz de ejemplo y qué hacer si se derrama. ¿Qué documento consultas?", ["Los riesgos, el almacenamiento y la emergencia aparecen en la hoja de datos de seguridad.", "La ficha técnica trata sobre el uso del producto."], "La hoja de datos de seguridad"),
    ],
    mistakes=[("Verter el resto de una tinta por el desagüe «porque es poco».", "Los residuos de tinta contaminan el agua y deben ir a un contenedor rotulado según la norma vigente.", "Guarda los residuos en el contenedor indicado y avisa al responsable."),
              ("Usar un envase sin rótulo porque «creo que es la tinta que necesitamos».", "Sin rótulo no se sabe qué contiene ni si está vigente, y puede ser peligroso.", "No lo uses: apártalo rotulado como «sin identificar» y avisa.")],
    T=[
        ("abc", "En Gráfica: ¿qué es una ficha técnica de un insumo?", "El documento del fabricante que explica para qué sirve y cómo se usa", "La factura de compra del insumo", "El plano de la bodega", "La ficha técnica orienta el uso correcto; la factura solo respalda el pago."),
        ("abc", "En Gráfica: ¿qué informa la hoja de datos de seguridad (HDS) de un producto?", "Sus riesgos, cómo guardarlo y qué hacer en una emergencia", "Su precio de venta", "El diseño del envase", "La HDS reúne la información de seguridad que se debe conocer antes de manipular el producto."),
        ("abc", "{F} ¿Dónde se ponen los residuos de tinta?", "En un contenedor rotulado, no en el desagüe ni en la basura común", "En el desagüe, si son pocos", "En un envase de bebida para guardarlos", "Los residuos de tinta se separan y se guardan según la norma vigente."),
        ("abc", "¿Por qué se rotula cada insumo con su nombre y fecha de recepción?", "Para identificarlo y saber si sigue vigente", "Para que se vea más ordenado únicamente", "Para aumentar su precio", "El rótulo evita confundir insumos y permite controlar la vigencia."),
        ("=", "{F} Cada hoja trae 20 etiquetas. ¿Cuántas hojas se necesitan para las 2.000 etiquetas, sin considerar la merma?", "2000//20", "Se divide el total de etiquetas por las que trae cada hoja.", " hojas"),
        ("abc", "{F} ¿Qué documento dice si la tinta es adecuada para el papel adhesivo del trabajo?", "La ficha técnica del fabricante", "La factura del papel", "El rótulo de la bodega", "La ficha técnica indica para qué materiales sirve cada tinta."),
        ("=", "{F} Con la merma de la ficha, ¿cuántas hojas se piden en total?", "100+100*5//100", "A las hojas netas se les suma el 5 % de merma.", " hojas"),
        ("abc", "Un frasco de tinta de ejemplo no tiene rótulo y nadie sabe qué contiene. ¿Qué corresponde?", "No usarlo, apartarlo rotulado como sin identificar y avisar al responsable", "Probarlo en una hoja para ver qué color da", "Mezclarlo con otra tinta para aprovecharlo", "Sin rótulo no se conoce el contenido ni el riesgo, así que no se usa."),
        ("abc", "La fecha de vencimiento de un barniz de ejemplo ya pasó. ¿Qué corresponde?", "No usarlo y consultar al responsable qué hacer con él", "Usarlo igual si se ve bien", "Pintar encima la fecha con otra", "Un insumo vencido puede dar mala calidad o ser inseguro, y la decisión es del responsable."),
        ("abc", "{F} Un compañero dice: «si una tinta de otro tipo se ve igual, se usa igual». ¿Qué le respondes?", "Manda lo que dice la OT y la ficha técnica, no la apariencia", "Tiene razón: lo único importante es el color", "Las fichas técnicas no sirven para elegir", "Dos tintas parecidas pueden secar o reaccionar distinto; el criterio es la especificación."),
        ("abc", "Una persona nueva quiere guardar un solvente en una botella de bebida «para ahorrar espacio». ¿Por qué es peligroso?", "Alguien podría confundirla y tomarla, y no tendría el rótulo de riesgo", "Porque la botella pesa más", "Porque el solvente cambia de nombre", "Los químicos se guardan en envases propios y rotulados para evitar accidentes."),
        ("abc", "{F} La OT pide papel adhesivo de 80 g/m² y en bodega solo hay de 90 g/m². ¿Qué corresponde?", "Consultar a la persona responsable antes de reemplazarlo", "Usar el de 90 g/m² sin avisar porque es mejor", "Cambiar la OT por su cuenta para que diga 90 g/m²", "Un cambio de insumo afecta calidad y costo, y se autoriza por escrito."),
        ("=", "{F} Cada hoja de papel adhesivo cuesta $150 (valor de ejemplo). ¿Cuánto cuestan las hojas pedidas con merma?", "(100+100*5//100)*150", "Se multiplica el total de hojas pedidas por el precio de cada una.", " pesos"),
    ],
    ctx=("abc", "El bodeguero de ejemplo te pide guardar rápido unos trapos con restos de tinta en la basura común «porque son solo trapos». ¿Qué respondes?", "Que deben ir al contenedor rotulado de residuos y que lo consultarás con el responsable", "Que se botan con la basura normal", "Que se guardan junto a los alimentos", "Los restos de tinta son residuos que se manejan según la norma vigente y no van a la basura común."),
    sc=[
        ("En Gráfica: ¿qué es el sustrato?", "El material sobre el que se imprime", "Puede ser papel, cartulina o un film, según la OT."),
        ("¿Qué documento informa los riesgos de una tinta?", "La hoja de datos de seguridad", "Reúne los riesgos y qué hacer en una emergencia."),
        ("¿Qué haces con un insumo sin rótulo?", "No lo uso y aviso al responsable", "Sin rótulo no se conoce su contenido ni su vigencia."),
    ],
    op=("Un taller de ejemplo debe imprimir 1.200 stickers; cada hoja trae 24 stickers y se pide un 10 % de hojas extra por merma. Además, en la bodega hay un frasco de tinta sin rótulo y un envase de solvente guardado en una botella de bebida. "
        "Calcula cuántas hojas netas y cuántas con merma se piden, y escribe qué harías con el frasco sin rótulo y con la botella de solvente.",
        "Hojas netas: 1.200 ÷ 24 = 50. Merma: 10 % de 50 = 5; total 55 hojas. El frasco sin rótulo no se usa: se aparta rotulado como sin identificar y se avisa al responsable. La botella de solvente no es un envase seguro: se avisa para que se pase a un envase propio rotulado según la norma vigente.",
        ["calcula las hojas netas y con merma", "decide no usar el frasco sin rótulo y avisar", "explica el riesgo de guardar solvente en una botella de bebida"],
        ["hoja con los cálculos y las dos acciones"],
        ["calcular la merma sobre el total de stickers", "usar el frasco para comprobar qué es", "no avisar al responsable"],
        "Pregunta: «¿sobre qué número se calcula el 10 %?». Si responde 'sobre 1.200', repasa que la merma se aplica a las hojas, no a los stickers."),
    reinforce="Haz una lista con cinco insumos de un taller gráfico (de ejemplo) y escribe, para cada uno, el documento donde buscarías cómo usarlo y cómo guardarlo.",
    extend="Explica con un ejemplo inventado por qué un envase sin rótulo es un riesgo para las personas y para el ambiente.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (catálogo de ejemplo, inventado). Gramaje: masa del papel por cada metro cuadrado; se mide en g/m². Papel bond: 75 g/m², escritura y fotocopia. Cartulina lisa: 250 g/m², rígida, para tarjetas. Papel couché: 130 g/m², liso y brillante, para fotografías. "
     "Papel kraft: 90 g/m², café y resistente, para bolsas. Film adhesivo plástico: no absorbente. Tintas: las que secan absorbiéndose en el papel sirven para materiales absorbentes; las tintas UV secan con luz ultravioleta y sirven también para materiales no absorbentes. "
     "Tinta directa (o plana): un color mezclado para un tono especial. Sentido de fibra: dirección en que se alinean las fibras del papel.")
build(
    O3, 2, F,
    use="Aprenderé a leer un catálogo de sustratos y tintas: gramaje, tipos de papel, tintas según el material y datos que se declaran en una orden de trabajo.",
    prior=["Sé qué son un sustrato y un insumo.", "Sé multiplicar y dividir.", "Sé leer una ficha técnica."],
    explain=[
        "El gramaje es la masa de un papel por cada metro cuadrado, y se mide en g/m². A mayor gramaje, el papel es más pesado y, por lo general, más grueso y rígido, pero un gramaje alto no significa «mejor»: el sustrato se elige según el uso. El peso de una lámina se calcula multiplicando su gramaje por su área en metros cuadrados.",
        "Los sustratos pueden ser absorbentes, como el papel, o no absorbentes, como un film plástico. Una tinta que seca absorbiéndose en el papel no sirve para un film, donde se necesita otra, como una tinta UV, que seca con luz ultravioleta. La cuatricromía obtiene los colores mezclando cian, magenta, amarillo y negro; una tinta directa o plana es un color mezclado de antemano para un tono especial.",
        "El sentido de fibra es la dirección en que se alinean las fibras del papel, y conviene declararlo en la OT porque afecta cómo se dobla. La OT debe indicar el tipo de sustrato, el gramaje, el tamaño y las tintas, y el manual del fabricante manda sobre la costumbre." + MAQ,
    ],
    vocab=[("gramaje", "masa del papel por metro cuadrado, en g/m²"), ("absorbente", "que deja que la tinta penetre, como el papel"), ("no absorbente", "que no deja penetrar la tinta, como un film plástico"), ("tinta UV", "tinta que seca con luz ultravioleta"), ("tinta directa", "color mezclado de antemano para un tono especial"), ("sentido de fibra", "dirección en que se alinean las fibras del papel")],
    worked=[
        ("Peso de una lámina", "Una lámina de ejemplo de 3 m² tiene 100 g/m². ¿Cuánto pesa?", ["Peso = gramaje × área.", "100 × 3 = 300."], "300 g"),
        ("Tinta para un film", "Un trabajo de ejemplo se imprime sobre film plástico. ¿Sirve una tinta que seca absorbiéndose?", ["El film no es absorbente.", "La tinta que seca absorbiéndose no tiene dónde penetrar."], "No: conviene una tinta como la UV"),
    ],
    mistakes=[("Pensar que un papel de más gramaje siempre es de mejor calidad.", "El gramaje solo indica masa por m²; el uso decide qué papel conviene.", "Elige el gramaje y el tipo de papel que pide la OT para ese uso."),
              ("Doblar una cartulina sin tener en cuenta el sentido de fibra y quejarse de que se agrieta.", "El sentido de fibra influye en cómo se dobla; debe declararse en la OT.", "Declara el sentido de fibra al pedir el papel.")],
    T=[
        ("abc", "En Gráfica: ¿qué mide el gramaje de un papel?", "La masa por cada metro cuadrado", "El largo de la hoja", "El brillo de la superficie", "Se expresa en g/m² y relaciona el peso con el área."),
        ("abc", "En Gráfica: ¿qué es un sustrato no absorbente?", "Un material sobre el que la tinta no penetra, como un film plástico", "Un papel muy delgado", "Una tinta de secado lento", "En un material no absorbente la tinta queda en la superficie."),
        ("abc", "¿Qué tinta de la ficha seca con luz ultravioleta?", "La tinta UV", "La tinta directa", "La tinta de cuatricromía", "La tinta UV debe su nombre a la luz ultravioleta que la seca."),
        ("abc", "{F} ¿Cuál es el papel de mayor gramaje del catálogo?", "La cartulina lisa", "El papel bond", "El papel kraft", "Con 250 g/m², la cartulina supera a los demás papeles de la ficha."),
        ("=", "{F} Una lámina de cartulina de 2 m² ¿cuántos gramos pesa?", "250*2", "El peso es el gramaje por el área en metros cuadrados.", " g"),
        ("abc", "{F} ¿Qué es una tinta directa?", "Un color mezclado de antemano para un tono especial", "La tinta que seca con luz UV", "Una tinta que solo sirve en el papel bond", "La tinta directa o plana se prepara para obtener un tono especial."),
        ("=", "{F} Diez láminas de papel couché de 2 m² cada una. ¿Cuántos gramos pesan en total?", "130*2*10", "Se multiplica el gramaje por el área de cada lámina y por las diez láminas.", " g"),
        ("abc", "{F} Una OT pide tarjetas rígidas para invitaciones. ¿Qué sustrato del catálogo conviene?", "La cartulina lisa de 250 g/m²", "El papel bond de 75 g/m²", "El film adhesivo plástico", "Una tarjeta necesita rigidez, que da el gramaje alto de la cartulina."),
        ("abc", "{F} Un cliente quiere un papel liso y brillante para las fotografías de un catálogo. ¿Qué papel de la ficha conviene?", "El papel couché de 130 g/m²", "El papel kraft de 90 g/m²", "El papel bond de 75 g/m²", "El couché es el liso y brillante que describe la ficha."),
        ("abc", "{F} Un compañero dice: «a mayor gramaje, mejor calidad, siempre». ¿Qué respondes?", "El gramaje mide masa por m²; el papel adecuado depende del uso", "Tiene razón: más gramaje siempre es mejor", "El gramaje mide el color del papel", "Una bolsa de papel kraft de 90 g/m² cumple su uso aunque pese menos que una cartulina."),
        ("abc", "{F} La cartulina del trabajo se agrieta al doblarse en un sentido y no en el otro. ¿Qué dato conviene declarar en la OT?", "El sentido de fibra", "El color del logotipo", "El nombre del cliente", "El sentido de fibra influye en cómo se dobla un papel."),
        ("abc", "{F} Se imprimirán 5.000 etiquetas sobre un film plástico con secado inmediato. ¿Qué tinta de la ficha corresponde?", "Una tinta UV", "Una tinta que seca absorbiéndose", "No se necesita tinta", "El film no absorbe y la UV seca con luz sin depender del material."),
        ("=", "{F} El papel couché cuesta $300 por cada 100 g (valor de ejemplo). ¿Cuánto cuestan 5 láminas de 2 m²?", "130*2*5//100*300", "Se calcula el peso total, se divide por 100 g y se multiplica por el precio.", " pesos"),
    ],
    ctx=("abc", "Un cliente de ejemplo quiere bolsas resistentes de color café para una tienda de productos naturales. ¿Qué sustrato del catálogo propones y por qué?", "Papel kraft, porque es café y resistente según la ficha", "Papel couché, porque es brillante", "Film adhesivo, porque es plástico", "El kraft es el papel resistente y de color café que describe el catálogo para bolsas."),
    sc=[
        ("En Gráfica: ¿cómo se calcula el peso de una lámina de papel?", "Gramaje por área en metros cuadrados", "El gramaje es la masa por cada metro cuadrado."),
        ("¿Qué tinta seca con luz ultravioleta?", "La tinta UV", "Por eso puede usarse en materiales no absorbentes."),
        ("¿Qué dato de la fibra conviene declarar en la OT?", "El sentido de fibra", "Afecta cómo se dobla el papel."),
    ],
    op=("Un cliente de ejemplo pide 1.000 invitaciones rígidas y 500 bolsas café resistentes. Catálogo de la ficha. Para cada pedido elige un sustrato del catálogo, justifica con un dato de la ficha y calcula el peso de una lámina de 4 m² del sustrato elegido para las invitaciones.",
        "Invitaciones: cartulina lisa de 250 g/m², porque es rígida y para tarjetas; peso de una lámina de 4 m²: 250 × 4 = 1.000 g. Bolsas: papel kraft de 90 g/m², porque es café y resistente.",
        ["elige el sustrato correcto para cada pedido", "justifica con un dato de la ficha", "calcula el peso con gramaje por área"],
        ["hoja con las dos elecciones, las razones y el cálculo"],
        ["elegir por el precio sin justificar", "usar couché porque es brillante", "no multiplicar por los 4 m²"],
        "Pregunta: «¿qué dato de la ficha apoya tu elección?». Si no lo cita, pídele que subraye la descripción de cada papel."),
    reinforce="Elige tres papeles del catálogo y escribe, para cada uno, un trabajo de ejemplo para el que servirían.",
    extend="Explica por qué el manual del fabricante manda sobre la costumbre al elegir una tinta para un sustrato.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (pedido de ejemplo, inventado). 3.000 volantes A5, impresos por una cara. En cada hoja grande de papel couché caben 4 volantes. Merma de ejemplo: 40 hojas. Cada paquete trae 250 hojas y cuesta $12.000. "
     "Consumo de ejemplo: 3 g de tinta por hoja en total. Stock de bodega: 600 hojas de papel couché y 5.000 g de tinta. Los recortes y hojas con error se separan para reciclaje.")
build(
    O3, 3, F,
    use="Aprenderé a calcular cantidades de papel y tinta para un pedido, a comparar con el stock de bodega y a registrar qué falta y qué sobra.",
    prior=["Sé qué es la merma.", "Sé multiplicar, dividir y restar.", "Sé leer un stock de bodega."],
    explain=[
        "Para saber cuánto material pedir se parte de la cantidad de productos y de cuántos caben en cada hoja. Las hojas netas son los productos divididos por los que caben en una hoja. A las hojas netas se les suma la merma para obtener las hojas totales. Luego se compara con el stock, que es lo que ya hay en bodega: lo que falta se compra y lo que sobra queda registrado.",
        "El papel se compra por paquetes completos. Si se necesitan 790 hojas y cada paquete trae 250, se comprarán 4 paquetes (1.000 hojas) y sobrarán hojas, que se guardan para otro trabajo. El consumo de tinta se estima multiplicando las hojas totales por el consumo por hoja; esos datos vienen de la ficha técnica y son de ejemplo.",
        "Pedir de menos atrasa el trabajo y pedir de más genera costo y residuos. Los recortes y las hojas con error se separan para reciclaje según las indicaciones de la empresa. Todo cálculo se anota en un registro con responsable." + MAQ,
    ],
    vocab=[("hojas netas", "hojas necesarias sin contar la merma"), ("hojas totales", "hojas netas más la merma"), ("stock", "cantidad de material que ya hay en bodega"), ("paquete", "cantidad fija de hojas con que se vende el papel"), ("consumo", "cantidad de insumo que se gasta por hoja o por trabajo")],
    worked=[
        ("Hojas netas", "Un pedido de ejemplo de 600 tarjetas, con 6 tarjetas por hoja. ¿Cuántas hojas netas necesita?", ["Se dividen las tarjetas por las que caben en una hoja.", "600 ÷ 6 = 100."], "100 hojas"),
        ("Lo que falta", "Un trabajo de ejemplo necesita 120 hojas y hay 80 en bodega. ¿Cuántas faltan?", ["Se resta el stock a lo necesario.", "120 − 80 = 40."], "40 hojas"),
    ],
    mistakes=[("Pedir solo las hojas netas, sin merma.", "Parte del papel se pierde en pruebas y ajustes, y las hojas netas no alcanzan.", "Suma la merma antes de comparar con el stock."),
              ("Botar el sobrante del paquete sin anotarlo ni guardarlo.", "Un sobrante se puede usar en otro trabajo y debe quedar en el stock registrado.", "Anota el sobrante y guárdalo rotulado.")],
    T=[
        ("abc", "En Gráfica: ¿qué son las hojas netas?", "Las hojas necesarias sin contar la merma", "Las hojas que se botan", "Las hojas de otro color", "Las netas son las que el pedido necesita sin la pérdida prevista."),
        ("abc", "En Gráfica: ¿qué es el stock?", "La cantidad de material que ya hay en bodega", "El precio de un paquete", "El tamaño de una hoja", "El stock se compara con lo necesario para saber qué falta."),
        ("=", "{F} ¿Cuántas hojas netas necesita el pedido?", "3000//4", "Se dividen los volantes por los que caben en cada hoja.", " hojas"),
        ("=", "{F} ¿Cuántas hojas totales se necesitan sumando la merma?", "3000//4+40", "A las hojas netas se les suma la merma.", " hojas"),
        ("abc", "{F} ¿Qué es la merma en este pedido?", "Las 40 hojas extra que se pierden en pruebas y ajustes", "Los 3.000 volantes del pedido", "Los 5.000 g de tinta", "La ficha fija una merma de 40 hojas."),
        ("=", "{F} Con el stock de bodega, ¿cuántas hojas faltan comprar?", "(3000//4+40)-600", "Se restan las hojas del stock a las hojas totales.", " hojas"),
        ("=", "{F} Si se compran 4 paquetes, ¿cuántas hojas quedarán sobrando después de cubrir las 790 hojas totales sin usar el stock?", "4*250-(3000//4+40)", "Se restan las hojas totales a las hojas compradas.", " hojas"),
        ("=", "{F} ¿Cuánto cuestan los 4 paquetes?", "4*12000", "Se multiplican los paquetes por el precio de cada uno.", " pesos"),
        ("=", "{F} ¿Cuántos gramos de tinta se estima que consume el trabajo con las hojas totales?", "(3000//4+40)*3", "Las hojas totales se multiplican por el consumo por hoja.", " g"),
        ("abc", "{F} ¿Alcanza la tinta que hay en bodega?", "Sí: se necesitan 2.370 g y hay 5.000 g", "No: se necesitan 5.000 g y hay 2.370 g", "No se puede saber", "El consumo estimado es menor que el stock de 5.000 g."),
        ("abc", "{F} Un compañero propone comprar solo las hojas netas «porque la merma se arregla sola». ¿Qué respondes?", "La merma es una pérdida real; sin ella no alcanzarán las hojas para el pedido", "Tiene razón: la merma nunca ocurre", "Comprar de más es siempre lo mejor", "Las pruebas y los ajustes gastan hojas que deben estar previstas."),
        ("abc", "Un operador de ejemplo bota 30 hojas con error en la basura común. ¿Qué debió hacer?", "Separarlas para reciclaje según las indicaciones de la empresa", "Guardarlas para pegarlas en el pedido final", "Venderlas como nuevas", "El papel con error se recicla y no se mezcla con otros residuos."),
        ("=", "{F} Si el stock fuera de 800 hojas y el trabajo de ejemplo usara 790, ¿cuántas hojas quedarían en bodega?", "800-(3000//4+40)", "Al stock se le restan las hojas que se usan.", " hojas"),
    ],
    ctx=("abc", "La jefa de taller de ejemplo ve que tu cálculo da 750 hojas y te pregunta si incluiste la merma. ¿Qué haces?", "Reviso el cálculo, sumo la merma de 40 hojas y dejo el nuevo total anotado", "Le digo que la merma es opcional", "Borro el cálculo y pido 1.000 hojas sin explicar", "La merma forma parte de lo que se pide y el cálculo queda registrado."),
    sc=[
        ("En Gráfica: ¿cómo se obtienen las hojas totales?", "Sumando la merma a las hojas netas", "Las netas no cubren las pérdidas de pruebas y ajustes."),
        ("¿Cómo se estima el consumo de tinta?", "Multiplicando las hojas totales por el consumo por hoja", "Cada hoja gasta una cantidad de tinta según la ficha técnica."),
        ("¿Qué haces con las hojas con error?", "Las separo para reciclaje", "El papel con error no se mezcla con los residuos comunes."),
    ],
    op=("Pedido de ejemplo: 1.800 tarjetas, con 6 tarjetas por hoja, merma de 30 hojas, paquetes de 100 hojas a $9.000 y consumo de 2 g de tinta por hoja. Stock: 200 hojas y 900 g de tinta. "
        "Calcula las hojas netas y totales, cuántas hojas faltan, cuántos paquetes comprarías, cuánto costarían y si alcanza la tinta.",
        "Netas: 1.800 ÷ 6 = 300. Totales: 300 + 30 = 330. Faltan 330 − 200 = 130 hojas, por lo que se compran 2 paquetes (200 hojas) por 2 × 9.000 = 18.000 pesos. Tinta: 330 × 2 = 660 g, y hay 900 g, así que alcanza.",
        ["calcula hojas netas y totales", "resta el stock y compra paquetes completos", "calcula el costo y el consumo de tinta"],
        ["hoja con los seis cálculos y la conclusión"],
        ["olvidar la merma", "comprar menos hojas de las que faltan", "calcular la tinta con las hojas netas"],
        "Pregunta: «¿por qué compras 2 paquetes y no 1,3?». Si no lo explica, recuerda que el papel se compra por paquetes completos."),
    reinforce="Inventa un pedido de 900 sobres con 3 por hoja y calcula hojas netas, merma de 20 hojas y hojas totales.",
    extend="Explica cómo cambiaría tu cálculo si cada hoja pudiera llevar 5 productos en vez de 4.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (opciones de sustrato y lotes de tinta, de ejemplo). Trabajo: 1.000 tarjetas de invitación. Requisitos de la OT: gramaje de 250 g/m² o más, superficie lisa y gasto en papel de $90.000 o menos. "
     "Opción A: cartulina lisa de 250 g/m², $70 por tarjeta. Opción B: cartulina rugosa de 300 g/m², $85 por tarjeta. Opción C: papel couché de 130 g/m², $40 por tarjeta. "
     "Lotes de tinta en bodega: lote 1 recibido en enero, vence en junio; lote 2 recibido en marzo, vence en diciembre. Regla de la bodega: se usa primero lo que vence antes, si está vigente.")
build(
    O3, 4, F,
    use="Aprenderé a elegir un sustrato con criterios verificables de la OT y a decidir qué lote de insumo usar primero, dejando la decisión registrada.",
    prior=["Conozco el gramaje y los tipos de sustrato.", "Sé calcular costos y stocks.", "Sé qué es una ficha técnica."],
    explain=[
        "Elegir un insumo es comparar cada opción con los requisitos de la OT: si falla uno, la opción se descarta aunque sea la más barata o la más bonita. Un requisito se verifica con un dato: el gramaje, la superficie y el costo máximo. Entre las opciones que cumplen todo, se puede considerar el costo, el plazo y el ambiente.",
        "Para controlar los lotes de insumos se aplica una regla simple: se usa primero el lote que vence antes, siempre que siga vigente, para no desperdiciar material. Cada decisión se anota en un registro con la fecha y quien la tomó. Si ninguna opción cumple la OT, no se improvisa: se informa y se pide autorización para cambiar el requisito.",
        "Los recortes y sobrantes se separan para reciclaje o reutilización según la norma vigente y las indicaciones de la empresa." + MAQ,
    ],
    vocab=[("requisito", "condición que debe cumplir una opción según la OT"), ("lote", "grupo de insumos recibido junto, con la misma fecha de recepción y vencimiento"), ("vigente", "que todavía no ha vencido"), ("descartar", "dejar fuera una opción porque no cumple un requisito"), ("vencimiento", "fecha a partir de la cual un insumo ya no debe usarse")],
    worked=[
        ("Costo de una opción", "Una opción de ejemplo cuesta $50 por tarjeta y se necesitan 800 tarjetas. ¿Cuánto cuesta?", ["Se multiplica el precio por la cantidad.", "50 × 800 = 40.000."], "$40.000"),
        ("Qué lote usar", "Un lote de tinta de ejemplo vence en mayo y otro en septiembre; ambos están vigentes. ¿Cuál se usa primero?", ["La regla dice que se usa primero el que vence antes.", "Mayo es antes que septiembre."], "El que vence en mayo"),
    ],
    mistakes=[("Elegir la opción más barata aunque no cumple un requisito de la OT.", "Una opción que falla un requisito no sirve, por barata que sea.", "Descarta las que no cumplen y compara el costo solo entre las que cumplen."),
              ("Usar el lote nuevo para «dejar el viejo para después» y que venza sin usarse.", "Eso desperdicia material y dinero.", "Usa primero el lote que vence antes mientras esté vigente.")],
    T=[
        ("abc", "En Gráfica: ¿qué es un requisito de la OT?", "Una condición que la opción elegida debe cumplir", "El precio de venta del trabajo", "Un color favorito del cliente", "Un requisito se verifica con un dato y si falla se descarta la opción."),
        ("abc", "{F} ¿Qué opción cumple todos los requisitos de la OT?", "La opción A", "La opción B", "La opción C", "A es lisa, tiene 250 g/m² y cuesta 70.000 en total; B es rugosa y C tiene menos gramaje."),
        ("=", "{F} ¿Cuánto costaría el papel de la opción A para las 1.000 tarjetas?", "70*1000", "Se multiplica el precio por tarjeta por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuánto costaría el papel de la opción B para las 1.000 tarjetas?", "85*1000", "Se multiplica el precio por tarjeta por la cantidad.", " pesos"),
        ("abc", "{F} ¿Por qué se descarta la opción B si está dentro del gasto máximo?", "Porque su superficie es rugosa y la OT pide superficie lisa", "Porque su gramaje es menor que 250 g/m²", "Porque es la más cara de todas", "El gasto de B cumple, pero falla el requisito de superficie."),
        ("abc", "{F} ¿Por qué se descarta la opción C aunque es la más barata?", "Porque su gramaje de 130 g/m² es menor que el mínimo de 250 g/m²", "Porque es lisa", "Porque cuesta $40 por tarjeta", "Un requisito incumplido descarta la opción, por barata que sea."),
        ("=", "{F} ¿Cuánto margen queda bajo el gasto máximo si se elige la opción A?", "90000-70*1000", "Al gasto máximo se le resta el costo de la opción elegida.", " pesos"),
        ("abc", "{F} ¿Qué lote de tinta se usa primero?", "El lote 1, que vence en junio, si está vigente", "El lote 2, porque llegó después", "Cualquiera, da lo mismo", "La regla manda usar primero lo que vence antes si sigue vigente."),
        ("abc", "{F} Un compañero dice: «usemos el lote 2 y dejemos el 1 para el final». ¿Qué le respondes?", "El lote 1 vence antes y podría perderse si no se usa primero", "Tiene razón, siempre se usa lo más nuevo", "Los lotes nunca vencen", "Usar primero el que vence antes evita desperdicio."),
        ("abc", "{F} Pasa junio y el lote 1 ya está vencido. ¿Qué corresponde con ese lote?", "No usarlo y consultar al responsable qué hacer con él", "Usarlo igual con cuidado", "Cambiarle la fecha del rótulo", "Un insumo vencido no se usa y su destino lo decide el responsable."),
        ("abc", "{F} El cliente pide cambiar a 1.200 tarjetas con la opción A. ¿Sigue cumpliendo el gasto máximo?", "Sí: 1.200 × 70 = 84.000, que no supera los 90.000", "No: 1.200 × 70 = 84.000, que supera los 90.000", "No se puede saber sin otra ficha", "El gasto sería 84.000 y el máximo es 90.000, así que sigue cumpliendo."),
        ("abc", "El cliente quiere cambiar el requisito a «superficie rugosa» porque le gustó la opción B. ¿Qué corresponde?", "Pedir el cambio por escrito, recalcular el costo y registrarlo antes de comprar", "Comprar B sin avisar y cambiar el papel después", "Ignorar el pedido del cliente", "Un cambio de requisito se acuerda por escrito y se recalcula antes de comprar."),
        ("=", "{F} Si el cliente pide 1.200 tarjetas con la opción B, ¿cuánto pasa del gasto máximo?", "85*1200-90000", "Se calcula el costo con 1.200 tarjetas y se resta el máximo.", " pesos"),
    ],
    ctx=("abc", "Un cliente de ejemplo necesita las tarjetas para el viernes y la opción A tarda 5 días en llegar, mientras que la C llega mañana. ¿Qué haces?", "Informar el problema de plazo, mostrar que C no cumple el gramaje y pedir una decisión al responsable", "Usar C sin avisar para cumplir el plazo", "Cambiar la fecha de la OT por tu cuenta", "Un conflicto entre plazo y requisitos se informa con datos y lo decide quien responde."),
    sc=[
        ("En Gráfica: ¿qué pasa con una opción que falla un requisito?", "Se descarta", "Por barata que sea, no cumple la OT."),
        ("¿Qué lote se usa primero?", "El que vence antes y sigue vigente", "Así se evita desperdiciar material que podría vencer sin usarse."),
        ("¿Qué haces si el cliente cambia un requisito?", "Lo pido por escrito y recalculo", "El cambio afecta el costo y debe quedar registrado."),
    ],
    op=("OT de ejemplo: 500 afiches con papel de 150 g/m² o más, superficie brillante y gasto de papel máximo de $60.000. Opción X: couché brillante de 170 g/m², $110 por afiche. Opción Y: couché brillante de 130 g/m², $80 por afiche. Opción Z: papel opaco de 200 g/m², $95 por afiche. "
        "Calcula el costo de cada opción, descarta las que no cumplen con la razón y recomienda una; si ninguna cumple, escribe qué harías.",
        "X: 500 × 110 = 55.000, cumple todo. Y: 500 × 80 = 40.000, se descarta porque 130 g/m² es menor que 150. Z: 500 × 95 = 47.500, se descarta porque no es brillante. Recomiendo X.",
        ["calcula los tres costos", "descarta con la razón correcta", "recomienda la única opción que cumple"],
        ["tabla de opciones con requisitos y recomendación"],
        ["elegir por precio", "no verificar el gasto máximo", "descartar sin dar la razón"],
        "Pregunta: «¿qué requisito descarta a Z?». Si responde 'es cara', pídele que compare con la superficie pedida."),
    reinforce="Inventa tres opciones de sustrato para un trabajo y marca cuáles cumplen los requisitos que fijes tú.",
    extend="Explica por qué usar primero el lote que vence antes también ayuda a cuidar el ambiente.",
)
