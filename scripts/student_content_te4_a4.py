"""Cuaderno del estudiante, 4.º básico Tecnología: OA 06 (procesador de textos), clases 1 a 5, y OA 07 (internet y buscadores), clases 1 a 5.

Las pantallas se describen con texto y son EJEMPLOS FICTICIOS: cada programa real se ve distinto y aquí no se nombra ninguna marca.
Todas las clases tienen alternativa en papel. Las direcciones web de los ejemplos son inventadas y no existen.
Simplificación declarada: juzgar si una fuente es confiable es más complejo que las señales de este cuaderno (autor, fecha, propósito, dirección).
No se usan datos personales. Los atajos de teclado (copiar, pegar, cortar y deshacer) son los más habituales, pero pueden variar según el programa.
"""
from __future__ import annotations

from student_content_te4_a import reg
from student_lessons import arith

OA6, OA7 = "TE04 OA 06", "TE04 OA 07"

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja y lápiz. La pantalla del procesador de textos es un ejemplo ficticio descrito con palabras; si no hay computador, se escribe en papel.",
    use="Aprenderé a escribir un texto en un procesador de textos y a organizarlo en párrafos con título. Sirve para que otras personas lo lean con facilidad.",
    prior=["Sé escribir oraciones con letra mayúscula y punto.", "Sé que un software es un programa del computador."],
    explain=[
        "Un procesador de textos es un programa para escribir, corregir y guardar documentos. En el ejemplo ficticio de esta clase, hay una hoja en blanco al centro y una barra de botones arriba. El cursor es una rayita que parpadea e indica dónde aparecerá la próxima letra. Se mueve con las flechas del teclado o haciendo clic en otro lugar.",
        "Un párrafo es un grupo de oraciones sobre una misma idea. Para empezar un párrafo nuevo, se presiona la tecla Enter (o Intro), que baja el cursor a una línea nueva. No se presiona Enter al final de cada línea, porque el programa baja solo cuando llega al borde. El título es una línea corta arriba que nombra el tema.",
        "Para organizar bien un texto, escribe primero el título. Luego escribe un párrafo por idea: uno para qué es, otro para cómo se hace y otro para el cierre. Revisa que cada párrafo tenga una idea y que haya una separación clara entre ellos. Un texto en párrafos ordenados se lee más rápido y se entiende mejor que un bloque sin cortes.",
    ],
    vocab=[("procesador de textos", "programa para escribir, corregir y guardar documentos"), ("cursor", "rayita que parpadea e indica dónde se escribe"), ("párrafo", "grupo de oraciones sobre una misma idea"), ("Enter", "tecla que baja a una línea nueva"), ("título", "línea corta que nombra el tema del texto")],
    worked=[
        ("Decidir cuándo usar Enter", "Escribes: «Las plantas necesitan luz. También necesitan agua.» y quieres empezar otra idea sobre la tierra. ¿Presionas Enter?", ["Terminó la idea sobre luz y agua.", "La idea de la tierra es nueva.", "Para un párrafo nuevo, presiono Enter."], "Sí, para empezar un párrafo nuevo"),
        ("Contar los párrafos", "Un texto tiene el título «Cuidar una planta» y tres bloques de oraciones separados por Enter: luz, agua y tierra. ¿Cuántos párrafos tiene?", ["El título no cuenta como párrafo de idea.", "Hay tres bloques."], "3 párrafos"),
    ],
    mistakes=[
        ("Presionar Enter al final de cada línea.", "El programa baja solo y el texto queda cortado de forma rara.", "Presiona Enter solo para empezar un párrafo nuevo."),
        ("Escribir todo en un solo bloque sin título.", "Cuesta saber de qué trata y dónde cambia la idea.", "Pon un título y separa en párrafos."),
    ],
    R=[
        ("La rayita que parpadea e indica dónde se escribe, ¿es el cursor o el título?", "El cursor", "Marca el lugar de la próxima letra."),
        ("Un grupo de oraciones sobre una misma idea, ¿es un párrafo o un título?", "Un párrafo", "Esa es su definición."),
        ("La tecla para empezar un párrafo nuevo, ¿es Enter o la flecha?", "Enter", "Baja el cursor a una línea nueva."),
    ],
    C=[
        ("¿Por qué no se presiona Enter al final de cada línea?", "Porque el programa baja solo al llegar al borde", "Enter es para empezar un párrafo."),
        ("En Tecnología: ¿Para qué sirve el título?", "Para nombrar el tema del texto", "Se lee primero."),
        ("¿Cómo cambias el lugar donde se escribe sin borrar nada?", "Haciendo clic en otro lugar o con las flechas", "El cursor se mueve así."),
    ],
    A=[
        arith("Un texto tiene 3 párrafos y cada uno tiene 4 oraciones. ¿Cuántas oraciones hay en total?", "3*4", "Se multiplican los párrafos por las oraciones de cada uno."),
        ("Escribes sobre dos ideas: cómo regar y cómo poner luz. ¿Cuántos párrafos necesitas?", "2", "Un párrafo por idea."),
        ("Escribes «Riego la planta con poca agua cada» y llegas al borde derecho de la hoja con la oración sin terminar. ¿Presionas Enter para seguir escribiendo?", "No", "El programa baja solo al llegar al borde; Enter es para empezar un párrafo nuevo."),
    ],
    Z=[
        ("Lía escribió tres ideas en un solo bloque largo. ¿Qué problema tiene el lector?", "No sabe dónde cambia la idea", "Falta separar en párrafos."),
        ("Entre «Cuidar una planta» y «cuidar», ¿cuál es mejor título para un texto sobre cómo cuidar una planta?", "Cuidar una planta", "Nombra el tema completo."),
    ],
    D=[
        arith("Un texto tiene 5 párrafos. Cada uno ocupa 3 líneas. ¿Cuántas líneas hay en total sin contar el título?", "5*3", "Se multiplican los párrafos por las líneas de cada uno."),
        ("Ordena los pasos: A escribir los párrafos, B escribir el título, C revisar la separación. ¿En qué orden?", "B, A, C", "Primero el título, luego los párrafos y al final la revisión."),
    ],
    ctx=("Debes escribir un texto sobre «Cómo cuidar una planta» con título y tres párrafos: luz, agua y tierra. Escribe el título y la primera oración de cada párrafo.", "Título: Cómo cuidar una planta. Luz: La planta necesita luz. Agua: La planta necesita poca agua cada día. Tierra: La tierra debe estar suelta", "Título y tres párrafos con una idea cada uno."),
    sc=[
        ("En Tecnología: ¿Qué es un párrafo?", "Un grupo de oraciones sobre una misma idea", "Cada párrafo trata una sola idea."),
        ("¿Cuándo se presiona Enter?", "Para empezar un párrafo nuevo", "No al final de cada línea."),
        ("¿Qué indica el cursor?", "Dónde se va a escribir", "Es la rayita que parpadea."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: cómo cuidar una planta. Tema 2: cómo ordenar la mochila. Escribe, en el procesador de textos o en papel como si lo fuera, un texto con título y tres párrafos de dos oraciones cada uno, separados con Enter.",
        "Tema 2: título «Cómo ordenar la mochila». Párrafo 1: Saca todo. Mira qué necesitas. Párrafo 2: Pon los libros atrás. Los cuadernos van al frente. Párrafo 3: Cierra la mochila. Revisa que no falte nada.",
        ["tiene título", "tiene tres párrafos", "una idea por párrafo", "usa Enter para separar"],
        ["documento o hoja con título y tres párrafos"],
        ["Enter al final de cada línea", "todo en un bloque"],
        "Pregunta: «¿cuál es la idea de este párrafo?». Si hay dos ideas, pídele separar.",
    ),
    reinforce="Escribe en un cuaderno un título y dos párrafos cortos sobre tu día.",
    extend="Escribe un texto de cuatro párrafos sobre un tema que te guste y revisa que cada párrafo tenga una idea.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja y lápiz. Las acciones se describen con palabras; si no hay computador, se simulan con lápiz y papel marcando con colores.",
    use="Aprenderé a editar un texto seleccionando, copiando, cortando, pegando y deshaciendo. Sirve para corregir y mover partes sin escribir todo de nuevo.",
    prior=["Sé escribir un texto en párrafos.", "Sé mover el cursor."],
    explain=[
        "Editar es corregir o cambiar un texto ya escrito. Para cambiar una parte, primero hay que seleccionarla, que es marcarla arrastrando el puntero o con las teclas, y queda con un color de fondo. Todo lo que se hace después afecta solo lo seleccionado. Si no seleccionas, el programa no sabe en qué parte actuar.",
        "Hay tres acciones básicas con lo seleccionado. Copiar guarda una copia para ponerla en otro lugar y el texto original se queda donde estaba. Cortar quita el texto de su lugar y lo guarda. Pegar pone en el cursor lo último copiado o cortado. Los atajos más usados son Ctrl + C para copiar, Ctrl + X para cortar y Ctrl + V para pegar; en algunos programas son distintos.",
        "Si te equivocas, puedes deshacer con Ctrl + Z, que anula la última acción. Con Borrar puedes quitar una letra a la vez. Mover un párrafo es cortar y pegar; repetir una frase es copiar y pegar. Después de editar, lee de nuevo el texto para comprobar que el cambio quedó bien y que no se perdió nada importante.",
    ],
    vocab=[("seleccionar", "marcar una parte del texto para actuar sobre ella"), ("copiar", "guardar una copia para ponerla en otro lugar"), ("cortar", "quitar el texto de su lugar y guardarlo"), ("pegar", "poner en el cursor lo último copiado o cortado"), ("deshacer", "anular la última acción")],
    worked=[
        ("Mover un párrafo", "Los párrafos están en el orden tierra, luz, agua y quieres dejar el de tierra al final. ¿Qué acciones usas?", ["Selecciono el párrafo de tierra.", "Lo corto.", "Pongo el cursor al final del párrafo de agua y pego."], "Seleccionar, cortar y pegar"),
        ("Corregir un error", "Pegaste una frase en un lugar equivocado. ¿Qué haces?", ["La última acción fue pegar.", "Puedo deshacerla con Ctrl + Z."], "Deshacer con Ctrl + Z"),
    ],
    mistakes=[
        ("Cortar cuando querías copiar.", "El texto desaparece de su lugar original.", "Usa copiar si el texto debe quedar en los dos lugares."),
        ("Escribir sobre un texto seleccionado sin querer.", "Se reemplaza todo lo seleccionado.", "Deshaz con Ctrl + Z y selecciona con cuidado."),
    ],
    R=[
        ("Marcar una parte del texto para actuar sobre ella, ¿es seleccionar o pegar?", "Seleccionar", "Es el primer paso para editar."),
        ("Anular la última acción, ¿es deshacer o copiar?", "Deshacer", "Con Ctrl + Z."),
        ("Quitar el texto de su lugar y guardarlo, ¿es cortar o copiar?", "Cortar", "El original ya no queda donde estaba."),
    ],
    C=[
        ("¿Qué diferencia hay entre copiar y cortar?", "Copiar deja el original y cortar lo quita", "Cortar lo mueve de lugar."),
        ("¿Para qué hay que seleccionar antes de copiar?", "Para que el programa sepa qué parte copiar", "Sin selección no sabe qué usar."),
        ("¿Qué acciones usas para repetir una frase en otro lugar?", "Copiar y pegar", "Se deja el original y se crea otra."),
    ],
    A=[
        ("Quieres mover el último párrafo al inicio del texto. ¿Qué haces: copiar y pegar, o cortar y pegar?", "Cortar y pegar", "Cortar quita el original; así no queda repetido."),
        arith("Tu texto tiene 5 párrafos. Cortas 1 y lo pegas en otro lugar. ¿Cuántos párrafos tiene ahora?", "5", "Cortar y pegar mueve el párrafo y no cambia la cantidad."),
        arith("Tu texto tiene 5 párrafos. Copias 1 y lo pegas en otro lugar. ¿Cuántos párrafos tiene ahora?", "5+1", "Copiar deja el original y pegar agrega uno más."),
    ],
    Z=[
        ("Tim seleccionó una frase y tecleó una letra, y la frase desapareció. ¿Qué pasó y cómo lo arregla?", "Se reemplazó la selección; deshace con Ctrl + Z", "Escribir sobre algo seleccionado lo reemplaza."),
        ("Un compañero dice: «Cortar y borrar son lo mismo». ¿Qué diferencia hay?", "Cortar guarda el texto para pegarlo; borrar lo quita sin guardarlo", "Lo cortado se puede pegar después."),
    ],
    D=[
        arith("Escribes un texto de 8 líneas. Cortas 2 líneas y las pegas más abajo. ¿Cuántas líneas tiene el texto?", "8", "Cortar y pegar mueve las líneas sin cambiar el total."),
        arith("Copias 2 líneas de un texto de 8 líneas y las pegas más abajo. ¿Cuántas líneas tiene ahora?", "8+2", "Copiar agrega las líneas pegadas al total."),
    ],
    ctx=("Tu texto tiene tres párrafos en este orden: agua, tierra, luz. Debe quedar en el orden luz, agua, tierra. Mueve solo el párrafo de luz y escribe cómo lo harías con seleccionar, cortar y pegar.", "Selecciono el párrafo de luz, lo corto, pongo el cursor al inicio del texto y pego", "Mueve un solo párrafo con tres acciones."),
    sc=[
        ("¿Qué se hace antes de copiar o cortar?", "Seleccionar", "El programa necesita saber qué parte."),
        ("¿Qué atajo deshace la última acción?", "Ctrl + Z", "Es el atajo habitual para deshacer."),
        ("¿Qué acción pone el texto en el cursor?", "Pegar", "Usa lo último copiado o cortado."),
    ],
    open_task=(
        "Escoge un texto. Texto 1: «Pon la planta cerca de la ventana. Riega con poca agua. Revisa la tierra cada día.» Texto 2: «Saca los libros. Ordena los cuadernos. Cierra la mochila.» Escribe qué acciones usarías (seleccionar, copiar, cortar, pegar, deshacer) para: 1) mover la última frase al inicio, 2) repetir la primera frase al final, 3) arreglar un error.",
        "Texto 1: 1) selecciono «Revisa la tierra cada día», corto y pego al inicio; 2) selecciono «Pon la planta...», copio y pego al final; 3) deshago con Ctrl + Z.",
        ["usa cortar y pegar para mover", "usa copiar y pegar para repetir", "usa deshacer para el error", "selecciona antes de actuar"],
        ["lista de tres acciones aplicadas al texto"],
        ["cortar cuando debía copiar", "no seleccionar"],
        "Pregunta: «¿quieres que el original quede donde estaba?». Si sí, es copiar; si no, cortar.",
    ),
    reinforce="Con lápiz, marca una frase de un texto de tu cuaderno y dibuja una flecha hacia donde la moverías.",
    extend="Explica con tus palabras cuándo conviene copiar y cuándo cortar.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja y lápiz. Las pantallas son ejemplos ficticios descritos con palabras; en papel se pueden simular con distintos subrayados.",
    use="Aprenderé a dar formato a un texto para que se lea mejor: tamaño, negrita, alineación y espacio entre líneas. Sirve para destacar lo importante sin recargar.",
    prior=["Sé seleccionar texto.", "Sé que el título nombra el tema."],
    explain=[
        "El formato es la forma en que se ve el texto sin cambiar lo que dice. Para dar formato, primero se selecciona el texto y luego se elige la opción en la barra de botones. Algunas opciones son el tamaño de la letra, el tipo de letra, la negrita (letra más gruesa), la cursiva (letra inclinada) y la alineación.",
        "La alineación puede ser a la izquierda, centrada o a la derecha. Los textos largos se leen mejor alineados a la izquierda. Los títulos suelen ir más grandes y centrados o con negrita. El interlineado es el espacio entre líneas: un poco más de espacio hace el texto más fácil de leer. Usa pocos tipos de letra, dos como máximo.",
        "El formato debe ayudar a leer. Usa la negrita solo para las palabras clave, no para frases enteras. Si todo está destacado, nada destaca. Un título grande, el texto de tamaño medio y una o dos palabras en negrita bastan. Después de aplicar formato, lee el documento completo para ver si se entiende mejor que antes.",
    ],
    vocab=[("formato", "forma en que se ve el texto sin cambiar lo que dice"), ("negrita", "letra más gruesa para destacar"), ("cursiva", "letra inclinada"), ("alineación", "lado hacia el que se acomoda el texto"), ("interlineado", "espacio entre las líneas")],
    worked=[
        ("Elegir el formato adecuado", "Quieres destacar la palabra clave «luz» dentro de una oración. ¿Usas negrita en la palabra o en toda la oración?", ["Solo la palabra clave debe destacar.", "Si destaco todo, nada destaca."], "Negrita solo en la palabra «luz»"),
        ("Elegir la alineación", "Tienes un texto largo de tres párrafos. ¿Lo alineas a la izquierda o centrado?", ["Mi texto tiene tres párrafos y es largo.", "Los textos largos se leen mejor alineados a la izquierda."], "A la izquierda"),
    ],
    mistakes=[
        ("Poner todo el texto en negrita.", "Cuando todo destaca, nada destaca.", "Usa negrita solo en palabras clave."),
        ("Usar cinco tipos de letra distintos.", "El documento se ve desordenado y cuesta leerlo.", "Usa dos tipos de letra como máximo."),
    ],
    R=[
        ("Letra más gruesa para destacar, ¿es negrita o cursiva?", "Negrita", "La negrita engrosa la letra."),
        ("Letra inclinada, ¿es cursiva o negrita?", "Cursiva", "La cursiva inclina la letra."),
        ("¿Se da formato a un texto antes de seleccionarlo o después?", "Después", "Primero se selecciona."),
    ],
    C=[
        ("¿Por qué no conviene poner todo en negrita?", "Porque si todo destaca, nada destaca", "La negrita sirve para palabras clave."),
        ("¿Qué alineación se lee mejor en textos largos?", "A la izquierda", "El ojo encuentra el inicio de cada línea."),
        ("¿Qué cambia el formato: lo que dice el texto o cómo se ve?", "Cómo se ve", "El contenido es el mismo."),
    ],
    A=[
        ("Quieres que el título se vea más importante. ¿Qué haces: letra más grande o letra más pequeña?", "Letra más grande", "El título debe verse más que el resto."),
        arith("Tu texto tiene 12 palabras y destacas 3 en negrita. ¿Cuántas palabras quedan sin destacar?", "12-3", "Se restan las destacadas del total."),
        ("El texto tiene tres tipos de letra distintos. ¿Cuántos deberías usar como máximo?", "Dos", "La regla es dos tipos como máximo."),
    ],
    Z=[
        ("Rita puso todo en cursiva, con tres colores y cuatro tipos de letra. ¿Qué problema tiene su documento?", "Se ve desordenado y cuesta leerlo", "Demasiado formato distrae."),
        ("Entre un poema de cuatro versos corto y un informe largo, ¿cuál se lee mejor alineado a la izquierda?", "El informe largo", "En textos largos, esa alineación ayuda a leer."),
    ],
    D=[
        arith("Un documento tiene 4 párrafos con 5 líneas cada uno. Con interlineado doble, cada línea ocupa 2 espacios. ¿Cuántos espacios ocupa todo?", "4*5*2", "Se multiplican párrafos, líneas y espacios por línea."),
        ("Escribe qué formato usarías para un título, para una palabra clave y para el texto general.", "Título grande, palabra clave en negrita y texto en tamaño medio", "Cada elemento tiene un formato distinto."),
    ],
    ctx=("Tu texto «Cómo cuidar una planta» tiene título y tres párrafos. Decide el formato de: el título, una palabra clave por párrafo y la alineación del texto.", "Título más grande y con negrita; una palabra clave en negrita por párrafo; texto alineado a la izquierda", "Tres decisiones coherentes con la clase."),
    sc=[
        ("¿Qué es el formato?", "La forma en que se ve el texto", "No cambia lo que dice."),
        ("¿Para qué sirve la negrita?", "Para destacar palabras clave", "Se usa poco."),
        ("¿Cuántos tipos de letra se usan como máximo?", "Dos", "Así el documento se ve ordenado."),
    ],
    open_task=(
        "Escoge un texto. Texto 1: «Cómo cuidar una planta» con tres párrafos. Texto 2: «Cómo ordenar la mochila» con tres párrafos. Escribe o simula el formato con una lista: tamaño del título, palabras en negrita (una por párrafo), alineación del texto y número de tipos de letra. Explica por qué ese formato ayuda a leer.",
        "Texto 2: título grande en negrita; negrita en «libros», «cuadernos» y «cerrar»; alineado a la izquierda; dos tipos de letra. Ayuda a leer porque destaca lo clave sin recargar.",
        ["título más grande", "una palabra clave por párrafo", "alineación adecuada", "máximo dos tipos de letra", "explica por qué ayuda"],
        ["lista de decisiones de formato con explicación"],
        ["todo en negrita", "muchos tipos de letra"],
        "Pregunta: «¿qué dejaría de verse si quitas este formato?». Si nada, probablemente sobra.",
    ),
    reinforce="Mira la portada de un libro de tu casa y di qué formato tiene el título.",
    extend="Escribe tres reglas para usar el formato sin recargar un documento.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja y lápiz. Las imágenes se describen con palabras; en papel se simulan con un dibujo. Los datos de autoría son ficticios.",
    use="Aprenderé a insertar una imagen en un documento, ajustarla y anotar quién la hizo. Sirve para ilustrar el texto respetando a los autores.",
    prior=["Sé dar formato al texto.", "Sé qué es una imagen propia o autorizada."],
    explain=[
        "Un documento puede llevar imágenes además de texto. Para insertar una imagen, se pone el cursor donde irá, se elige la opción de insertar imagen en la barra de botones y se escoge el archivo. Después, se puede cambiar su tamaño arrastrando una esquina, para no deformarla, y se puede mover cerca del párrafo que ilustra.",
        "La imagen debe tener relación con el texto y ayudar a entenderlo. Además, debe ser tuya o estar autorizada. Una imagen tiene autoría, que es la persona que la creó. Debajo de la imagen se escribe un pie de foto: una frase corta que dice qué muestra y quién la hizo. Por ejemplo: «Una planta en una ventana. Dibujo de Matías».",
        "Si usas una imagen de otra persona con permiso, escribe su nombre y de dónde la sacaste. Si no tienes permiso o no sabes si se puede usar, no la insertes. No uses fotos con rostros de otras personas sin su permiso ni con datos personales a la vista. Revisa también que la imagen no tape el texto y que se vea bien al imprimir.",
    ],
    vocab=[("insertar", "agregar un elemento al documento"), ("pie de foto", "frase corta bajo la imagen que dice qué muestra y quién la hizo"), ("autoría", "nombre de la persona que creó algo"), ("deformar", "cambiar la forma de una imagen al estirarla mal"), ("esquina", "punto de la imagen desde donde se cambia su tamaño")],
    worked=[
        ("Cambiar el tamaño sin deformar", "Una imagen sale muy grande. ¿La estiras desde un lado o desde una esquina?", ["Desde un lado se deforma.", "Desde una esquina conserva su forma."], "Desde una esquina"),
        ("Escribir un pie de foto", "Insertaste el dibujo de una planta que hizo Sofía. Escribe el pie de foto.", ["Digo qué muestra.", "Digo quién lo hizo."], "Una planta en una ventana. Dibujo de Sofía"),
    ],
    mistakes=[
        ("Estirar la imagen desde un lado.", "Se deforma y se ve mal.", "Arrastra desde una esquina."),
        ("Insertar una imagen sin anotar quién la hizo.", "No se reconoce el trabajo del autor.", "Escribe la autoría en un pie de foto."),
    ],
    R=[
        ("Agregar una imagen al documento, ¿es insertar o seleccionar?", "Insertar", "Es agregar un elemento."),
        ("La frase bajo la imagen con qué muestra y quién la hizo, ¿es el pie de foto o el título?", "El pie de foto", "Explica la imagen."),
        ("Quien creó una imagen, ¿es el autor o el cursor?", "El autor", "Es la persona que la creó."),
    ],
    C=[
        ("¿Por qué se cambia el tamaño desde una esquina?", "Para no deformar la imagen", "Se mantiene la proporción."),
        ("¿Qué haces si no sabes si puedes usar una imagen?", "No la insertas", "Mejor usar una propia o autorizada."),
        ("¿Para qué sirve el pie de foto?", "Para explicar la imagen y dar la autoría", "Dice qué muestra y quién la hizo."),
    ],
    A=[
        ("Quieres ilustrar el párrafo sobre el agua. ¿Dónde pones la imagen: cerca de ese párrafo o al final del documento?", "Cerca de ese párrafo", "La imagen ayuda a entender lo que está cerca."),
        arith("Tu documento tiene 4 párrafos y pones 1 imagen cada 2 párrafos. ¿Cuántas imágenes insertas?", "4//2", "Se divide el número de párrafos por 2."),
        ("Escribe un pie de foto para un dibujo de un vaso de agua hecho por un niño llamado Pedro.", "Un vaso con agua. Dibujo de Pedro", "Dice qué muestra y quién lo hizo."),
    ],
    Z=[
        ("Ana insertó una foto de una compañera con su nombre y su dirección visibles, sin pedirle permiso. ¿Qué cuidados olvidó?", "Pedir permiso y no mostrar datos personales", "La privacidad se cuida."),
        ("Una imagen de un gato aparece en un texto sobre cómo cuidar plantas. ¿Ayuda a entender?", "No", "No tiene relación con el texto."),
    ],
    D=[
        arith("Un documento tiene 3 imágenes y cada una lleva un pie de foto de 8 palabras. ¿Cuántas palabras hay en total en los pies de foto?", "3*8", "Se multiplican las imágenes por las palabras de cada pie."),
        ("Una imagen tapa dos líneas del texto. ¿Qué haces?", "La muevo o la hago más pequeña", "El texto debe verse completo."),
    ],
    ctx=("En tu texto «Cómo cuidar una planta» quieres insertar un dibujo tuyo cerca del párrafo de la luz. Escribe los pasos para insertarlo, ajustarlo sin deformarlo y escribir el pie de foto.", "Pongo el cursor junto al párrafo de la luz; inserto el dibujo; lo ajusto desde una esquina; escribo debajo: Una planta con luz. Dibujo de (mi nombre)", "Pasos de inserción, tamaño y pie de foto."),
    sc=[
        ("¿Cómo se cambia el tamaño sin deformar?", "Arrastrando desde una esquina", "Mantiene la forma."),
        ("¿Qué lleva el pie de foto?", "Qué muestra la imagen y quién la hizo", "Es una frase corta."),
        ("¿Puedes insertar una imagen sin saber si se puede usar?", "No", "Debe ser propia o autorizada."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: «Cómo cuidar una planta», con un dibujo propio cerca del párrafo del agua. Documento 2: «Cómo ordenar la mochila», con un dibujo propio cerca del párrafo de los libros. Describe los pasos para insertar la imagen, cómo ajustarías el tamaño y escribe el pie de foto con autoría.",
        "Documento 1: cursor bajo el párrafo del agua; inserto el dibujo; ajusto desde una esquina; pie: «Un vaso regando una planta. Dibujo de Lucía».",
        ["pasos de inserción", "ajuste desde una esquina", "pie de foto con autoría", "imagen cerca del párrafo relacionado"],
        ["pasos escritos y pie de foto"],
        ["imagen deformada", "sin autoría"],
        "Pregunta: «¿quién hizo esa imagen y dónde lo dice?». Si no está escrito, pídele agregar el pie de foto.",
    ),
    reinforce="Dibuja una imagen para ilustrar un párrafo de tu cuaderno y escribe su pie de foto.",
    extend="Explica por qué es importante escribir quién hizo una imagen.",
)

# ------------------------------------------------------------------ OA 06, clase 5
reg(
    OA6, 5,
    materials="Hoja y lápiz. Las pantallas son ejemplos ficticios descritos con palabras. En papel, se simulan carpetas con hojas rotuladas.",
    use="Aprenderé a guardar un documento con un buen nombre, cerrarlo y volver a abrirlo para recuperarlo. Sirve para no perder mi trabajo.",
    prior=["Sé escribir, editar y dar formato a un texto.", "Sé qué es una carpeta."],
    explain=[
        "Guardar es copiar el documento al almacenamiento del computador, para que no se pierda al apagarlo. Mientras no guardes, el trabajo existe solo en la pantalla y se puede perder. La primera vez, el programa pide un nombre y una carpeta. El nombre debe decir de qué trata el documento y, si hay varias versiones, cuál es.",
        "Un buen nombre es corto, claro y sin símbolos raros: «cuidado_planta_v2». Un mal nombre es «documento1» o «asdf». La carpeta es el lugar donde queda. Elige una carpeta con un nombre claro y sin símbolos raros, como «tecnologia_4», para encontrarlo después. Guarda de nuevo cada cierto tiempo mientras trabajas, para no perder los últimos cambios.",
        "Cerrar el documento libera el programa, pero el archivo queda guardado. Para recuperarlo, se abre el procesador de textos, se elige abrir, se busca la carpeta y se escoge el archivo por su nombre. Si no recuerdas el nombre, el programa muestra los documentos recientes. Por eso es útil poner nombres con sentido: encontrar el archivo es mucho más fácil.",
    ],
    vocab=[("guardar", "copiar el documento al almacenamiento para no perderlo"), ("nombre de archivo", "nombre que identifica un documento"), ("carpeta", "lugar donde se ordenan los archivos"), ("abrir", "mostrar en pantalla un documento guardado"), ("versión", "copia del documento en un momento del trabajo")],
    worked=[
        ("Elegir un buen nombre", "Documento sobre cómo cuidar una planta, segunda versión. Opciones: A «documento1», B «cuidado_planta_v2». ¿Cuál es mejor?", ["A no dice de qué trata.", "B dice el tema y la versión."], "B"),
        ("Recuperar un archivo", "Guardaste «ordenar_mochila» en la carpeta «tecnologia_4» y cerraste el programa. ¿Cómo lo abres de nuevo?", ["Abro el procesador de textos.", "Elijo abrir.", "Busco la carpeta y el nombre."], "Abrir el programa, elegir abrir y buscar la carpeta y el nombre"),
    ],
    mistakes=[
        ("Cerrar el documento sin guardar.", "Se pierden los cambios.", "Guarda antes de cerrar y cada cierto tiempo."),
        ("Poner nombres como «documento1».", "No se sabe qué contiene.", "Usa un nombre que diga el tema."),
    ],
    R=[
        ("Copiar el documento al almacenamiento para no perderlo, ¿es guardar o cerrar?", "Guardar", "Guardar conserva el trabajo."),
        ("El lugar donde se ordenan los archivos, ¿es una carpeta o un párrafo?", "Una carpeta", "Agrupa y ordena archivos."),
        ("Mostrar en pantalla un documento guardado, ¿es abrir o pegar?", "Abrir", "Es recuperar el documento."),
    ],
    C=[
        ("¿Por qué conviene guardar cada cierto tiempo?", "Para no perder los últimos cambios", "Si falla el computador, no se pierde todo."),
        ("¿Por qué «cuidado_planta_v2» es un buen nombre?", "Dice el tema y la versión", "Es corto y claro."),
        ("¿Se pierde el archivo al cerrar el documento si ya lo guardaste?", "No", "El archivo queda guardado."),
    ],
    A=[
        ("Elige el mejor nombre: A «asdf», B «ordenar_mochila_v1», C «trabajo».", "B", "Dice el tema y la versión."),
        arith("Guardas tu documento cada 10 minutos durante 40 minutos de trabajo. ¿Cuántas veces lo guardas?", "40//10", "Se divide el tiempo total por el intervalo."),
        ("Cerraste todo ayer y hoy quieres seguir tu texto. ¿Qué haces primero: abrir el procesador de textos o buscar la carpeta en la pantalla vacía?", "Abrir el procesador de textos", "Desde el programa eliges abrir y recién ahí buscas la carpeta y el archivo."),
    ],
    Z=[
        ("Dani trabajó 30 minutos sin guardar y se apagó el computador. ¿Qué pasó con su trabajo?", "Se perdió", "Lo que no está guardado no sobrevive."),
        ("Tienes tres versiones de un texto. ¿Cómo las distingues en el nombre?", "Agregando v1, v2 y v3", "Las versiones se numeran en el nombre."),
    ],
    D=[
        arith("Tienes 12 archivos y los ordenas en 3 carpetas con la misma cantidad. ¿Cuántos archivos hay en cada carpeta?", "12//3", "Se reparten en partes iguales."),
        ("Un archivo se llama «cuidado_planta_v1» y otro «cuidado_planta_v2». ¿Cuál es la versión más reciente?", "cuidado_planta_v2", "El número mayor indica la versión más nueva."),
    ],
    ctx=("Terminaste el texto «Cómo cuidar una planta», segunda versión. Escribe el nombre de archivo, la carpeta donde lo guardarías y los pasos para abrirlo mañana.", "Nombre: cuidado_planta_v2. Carpeta: tecnologia_4. Mañana: abro el procesador de textos, elijo abrir, busco la carpeta y el nombre", "Nombre claro, carpeta y pasos."),
    sc=[
        ("¿Qué hace guardar?", "Conserva el documento para no perderlo", "Lo copia al almacenamiento."),
        ("¿Cómo debe ser un buen nombre de archivo?", "Corto y claro", "Dice el tema y la versión."),
        ("¿Cómo recuperas un documento cerrado?", "Abriéndolo desde su carpeta", "Se busca por carpeta y nombre."),
    ],
    open_task=(
        "Escoge un documento. Documento 1: «Cómo cuidar una planta», versión 2. Documento 2: «Cómo ordenar la mochila», versión 1. Escribe el nombre del archivo, la carpeta, cuándo guardarías (al menos dos momentos) y los pasos para recuperarlo después de cerrarlo.",
        "Documento 2: nombre: ordenar_mochila_v1; carpeta: tecnologia_4; guardo al terminar cada párrafo y antes de cerrar; recupero: abrir el programa, abrir, buscar la carpeta y el nombre.",
        ["nombre claro", "carpeta ordenada", "dos momentos de guardado", "pasos para recuperar"],
        ["ficha de guardado y recuperación"],
        ["nombres sin sentido", "no guardar antes de cerrar"],
        "Pregunta: «¿cómo lo encontrarías en una semana?». Si no sabe, pídele mejorar nombre o carpeta.",
    ),
    reinforce="Inventa tres nombres de archivo claros para trabajos de tus asignaturas.",
    extend="Explica con tus palabras por qué guardar no es lo mismo que cerrar.",
)

# ------------------------------------------------------------------ OA 07, clase 1
reg(
    OA7, 1,
    materials="Hoja y lápiz. Las páginas y los buscadores se describen con texto y son ejemplos ficticios; las direcciones web inventadas no existen.",
    use="Aprenderé a construir una búsqueda específica con palabras clave. Sirve para encontrar rápido la información que necesito en internet.",
    prior=["Sé que internet permite buscar información.", "Sé escribir palabras en un teclado."],
    explain=[
        "Un buscador es un programa de internet donde escribes palabras y te muestra una lista de páginas relacionadas. Lo que escribes se llama búsqueda. Si la búsqueda es muy general, aparecen muchas páginas que no sirven. Una búsqueda específica usa las palabras clave, que son las más importantes de lo que necesitas.",
        "Para construir una búsqueda específica, piensa en tres preguntas: ¿sobre qué tema?, ¿qué quiero saber exactamente? y ¿para quién o para dónde? Por ejemplo, «plantas» es general. «cuidados de una planta de interior con poca luz» es más específica. No escribas una pregunta larga con palabras de relleno como «por favor» o «dime». Usa entre 3 y 6 palabras clave; palabras como «de», «un» o «una» no cuentan.",
        "Si los resultados no sirven, cambia las palabras: usa un sinónimo, agrega un detalle o quita lo que sobra. Nunca escribas datos personales en un buscador, como tu nombre completo, tu dirección o tu colegio. Si el tema es delicado o dudas, pide ayuda a una persona adulta. Una buena búsqueda ahorra tiempo y reduce el riesgo de abrir páginas peligrosas.",
    ],
    vocab=[("buscador", "programa de internet que busca páginas según las palabras que escribes"), ("palabra clave", "palabra importante de lo que quieres encontrar"), ("búsqueda específica", "búsqueda con palabras clave que delimitan el tema"), ("sinónimo", "palabra con significado parecido"), ("resultado", "página que el buscador muestra")],
    worked=[
        ("Mejorar una búsqueda", "Quieres saber cómo regar un cactus. Escribiste «plantas». ¿Qué búsqueda es mejor: A «plantas» o B «cómo regar un cactus»?", ["A es muy general.", "B tiene el tema y lo que quiero saber."], "B"),
        ("Cambiar las palabras", "La búsqueda «regar cactus» no dio buenos resultados. ¿Qué puedes probar?", ["Puedo usar un sinónimo.", "O agregar un detalle."], "Probar «cuánta agua necesita un cactus» o agregar un detalle como «en invierno»"),
    ],
    mistakes=[
        ("Escribir una búsqueda muy general, como «plantas».", "Aparecen demasiadas páginas que no sirven.", "Agrega el tema exacto y lo que quieres saber."),
        ("Escribir datos personales en el buscador.", "Se expone información privada.", "Nunca escribas tu nombre completo, dirección ni colegio."),
    ],
    R=[
        ("Una palabra importante de lo que quieres encontrar, ¿es una palabra clave o un resultado?", "Una palabra clave", "Resume lo central de la búsqueda."),
        ("Una palabra con significado parecido, ¿es un sinónimo o un buscador?", "Un sinónimo", "Es otra palabra para decir lo mismo."),
        ("¿Se escribe el nombre completo en un buscador?", "No", "Son datos personales."),
    ],
    C=[
        ("¿Por qué «plantas» es una búsqueda muy general?", "Porque no dice qué quieres saber", "Muestra muchísimas páginas distintas."),
        ("¿Cuántas palabras clave conviene usar?", "De 3 a 6", "Así la búsqueda es clara y breve."),
        ("Si los resultados no sirven, ¿qué se hace?", "Se cambian las palabras", "Con un sinónimo o un detalle."),
    ],
    A=[
        ("Quieres saber qué come un conejo mascota. Elige la mejor búsqueda: A «conejos», B «qué come un conejo mascota».", "B", "B tiene el tema y lo que quieres saber."),
        ("Quieres aprender a plegar un avión de papel. Escribe una búsqueda de 3 a 6 palabras clave.", "cómo plegar un avión de papel", "Incluye tema y lo que quieres saber."),
        arith("Tu búsqueda tiene 4 palabras clave y agregas 2 palabras clave más. ¿Cuántas palabras clave tiene ahora?", "4+2", "Se suman las palabras nuevas."),
    ],
    Z=[
        ("Sol escribió «Por favor dime todo sobre los animales del mundo». ¿Qué problema tiene su búsqueda?", "Es muy larga y muy general", "Tiene relleno y no delimita el tema."),
        ("Dos búsquedas: A «volcanes», B «cómo se forma un volcán para niños». ¿Cuál ayuda más a un trabajo de 4.º?", "B", "Es específica y dice para quién."),
    ],
    D=[
        arith("Una búsqueda general da 5.000 resultados y una específica da 500. ¿Cuántos resultados menos da la específica?", "5000-500", "Se resta el menor del mayor."),
        ("Quieres saber la altura de un edificio famoso, pero escribiste «edificio». ¿Qué agregas?", "El nombre del edificio y la palabra altura", "Delimita el tema y lo que quieres saber."),
    ],
    ctx=("Tienes que investigar cómo cuidar una planta de interior con poca luz para tu clase. Escribe una búsqueda general, otra específica y di por qué la específica es mejor.", "General: plantas. Específica: cómo cuidar una planta de interior con poca luz. Es mejor porque dice el tema exacto y lo que quiero saber", "Compara una búsqueda general con una específica."),
    sc=[
        ("En Tecnología: ¿Qué es una palabra clave?", "Una palabra importante de lo que buscas", "Resume el tema."),
        ("¿Qué hace una búsqueda específica?", "Delimita el tema con palabras clave", "Así aparecen mejores resultados."),
        ("¿Se escriben datos personales en un buscador?", "No", "Se protege la privacidad."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: cómo cuidar una planta de interior. Tema 2: cómo se hace un avión de papel. Escribe una búsqueda general y tres búsquedas específicas con 3 a 6 palabras clave cada una. Marca las palabras clave y explica cuál usarías primero.",
        "Tema 2: general: aviones. Específicas: cómo hacer un avión de papel; pasos para plegar un avión de papel; avión de papel que vuele lejos. Uso la segunda porque pide los pasos.",
        ["una búsqueda general", "tres búsquedas específicas", "3 a 6 palabras clave cada una", "elige una y explica"],
        ["lista de búsquedas con la elegida"],
        ["búsquedas largas o con relleno", "datos personales"],
        "Pregunta: «¿esta búsqueda dice el tema y lo que quieres saber?». Si no, pídele agregar un detalle.",
    ),
    reinforce="Escribe tres búsquedas específicas sobre un tema de otra asignatura.",
    extend="Explica con tus palabras por qué cambiar las palabras puede mejorar los resultados.",
)

# ------------------------------------------------------------------ OA 07, clase 2
reg(
    OA7, 2,
    materials="Hoja y lápiz. La lista de resultados está escrita en el cuaderno como ejemplo ficticio; las direcciones inventadas no existen.",
    use="Aprenderé a leer la lista de resultados antes de abrir una página. Sirve para elegir las páginas útiles y evitar las que no sirven o son peligrosas.",
    prior=["Sé construir una búsqueda específica.", "Sé qué es una palabra clave."],
    explain=[
        "Un buscador muestra cada resultado con tres datos: el título de la página, la dirección web (por ejemplo, www.plantas-ejemplo.example) y un resumen de dos líneas. Léelos antes de abrir. El título dice el tema. La dirección web muestra de dónde viene la página. El resumen te adelanta si responde lo que buscas.",
        "Para elegir, pregúntate: ¿el título tiene mis palabras clave?, ¿el resumen responde mi pregunta?, ¿la dirección parece de un sitio que conozco o de uno educativo? Algunos resultados dicen «anuncio» o «publicidad»: no son las mejores respuestas, sino avisos pagados. Evita los resultados con direcciones raras, llenas de números o con promesas como «gana premios gratis».",
        "No abras el primer resultado solo porque está primero. El orden no asegura que sea el mejor ni el más seguro. Elige dos o tres resultados que parezcan útiles y confiables, y ábrelos uno por uno. Si una página pide datos personales o descargar algo, ciérrala y avisa a una persona adulta. Leer antes de abrir ahorra tiempo y protege.",
    ],
    vocab=[("título", "nombre de la página en la lista de resultados"), ("dirección web", "texto que identifica dónde está una página"), ("resumen", "dos líneas que adelantan el contenido de la página"), ("anuncio", "resultado pagado que no siempre responde la búsqueda"), ("sitio educativo", "página hecha para enseñar")],
    worked=[
        ("Elegir entre dos resultados", "Búsqueda: «cuánta agua necesita un cactus». Resultado A: «Riego del cactus: cuánta agua necesita» (www.cuidado-plantas-ejemplo.example). Resultado B: «Gana premios gratis ahora» (www.premios123.example). ¿Cuál abres?", ["A tiene mis palabras clave.", "B promete premios y no tiene relación."], "A"),
        ("Reconocer un anuncio", "Un resultado tiene la palabra «anuncio» arriba. ¿Es la mejor respuesta del buscador?", ["Un anuncio es un aviso pagado.", "Puede no responder la búsqueda."], "No necesariamente; es un aviso pagado"),
    ],
    mistakes=[
        ("Abrir siempre el primer resultado.", "Estar primero no asegura que sea el mejor ni el más seguro.", "Lee título, dirección y resumen de varios resultados."),
        ("Abrir un resultado que promete premios gratis.", "Puede ser engañoso o peligroso.", "Ignóralo y avisa a una persona adulta si insiste."),
    ],
    R=[
        ("El nombre de la página en la lista de resultados, ¿es el título o el resumen?", "El título", "Es la primera línea del resultado."),
        ("Un resultado pagado marcado como «anuncio», ¿es un aviso o una respuesta confiable?", "Un aviso", "Se paga por mostrarlo."),
        ("Las dos líneas que adelantan el contenido, ¿son el título o el resumen?", "El resumen", "Adelanta lo que dirá la página."),
    ],
    C=[
        ("¿Por qué se lee el resumen antes de abrir una página?", "Para saber si responde lo que busco", "Ahorra tiempo y evita páginas inútiles."),
        ("¿Qué indica una dirección con números raros y promesas de premios?", "Que conviene no abrirla", "Puede ser engañosa."),
        ("¿Por qué no se abre solo el primer resultado?", "Porque el orden no asegura que sea el mejor", "Hay que comparar varios."),
    ],
    A=[
        ("Búsqueda: «cómo plegar un avión de papel». Resultado A: «Avión de papel paso a paso» (www.papel-ejemplo.example). Resultado B: «Todo sobre aviones comerciales y vuelos» (www.vuelos-ejemplo.example). ¿Cuál se parece más a lo que buscas?", "A", "Su título tiene las palabras clave de la búsqueda."),
        arith("Tienes 6 resultados y descartas 2 por promesas engañosas. ¿Cuántos quedan para revisar?", "6-2", "Se restan los descartados del total."),
        ("Un resultado dice «anuncio». ¿Lo abres primero porque sale arriba?", "No", "Un anuncio es un aviso pagado."),
    ],
    Z=[
        ("Eli dice: «El primer resultado es el mejor porque está primero». ¿Qué le responderías?", "Que el orden no asegura calidad ni seguridad", "Hay anuncios y páginas con direcciones dudosas."),
        ("Una página abre y pide tu nombre y dirección para mostrarte la información. ¿Qué haces?", "La cierras y avisas a una persona adulta", "Pide datos personales sin necesidad."),
    ],
    D=[
        arith("Revisas 3 resultados en 2 minutos cada uno. ¿Cuántos minutos te toma revisarlos?", "3*2", "Se multiplican los resultados por los minutos de cada uno."),
        ("De tres resultados, uno es anuncio, uno tiene dirección rara y uno es un sitio educativo con tus palabras clave. ¿Cuál abres primero?", "El sitio educativo", "Es el más relevante y confiable de los tres."),
    ],
    ctx=("Buscaste «cómo cuidar una planta de interior». Resultado 1: «Anuncio: compra plantas hoy» (www.tienda-ejemplo.example). Resultado 2: «Cuidado de plantas de interior: luz y riego» (www.jardin-escuela-ejemplo.example). Resultado 3: «Gana un viaje gratis» (www.viaje777.example). Elige cuál abres y explica por qué.", "Abro el 2, porque su título tiene mis palabras clave y parece un sitio educativo. El 1 es un anuncio y el 3 promete un premio", "Elige el pertinente y descarta con razón."),
    sc=[
        ("¿Qué tres datos tiene un resultado?", "Título, dirección web y resumen", "Se leen antes de abrir."),
        ("¿Qué es un anuncio?", "Un resultado pagado", "No es necesariamente la mejor respuesta."),
        ("¿Se abre una página que pide datos personales?", "No", "Se cierra y se avisa a un adulto."),
    ],
    open_task=(
        "Escoge una búsqueda. Búsqueda 1: «cuánta agua necesita un cactus». Búsqueda 2: «cómo plegar un avión de papel». Para tu búsqueda, escribe cuatro resultados ficticios con título, dirección inventada y resumen, uno de ellos engañoso. Marca cuáles abrirías y explica con las palabras clave.",
        "Búsqueda 2: A «Avión de papel paso a paso» (www.papel-ejemplo.example); B «Anuncio: compra aviones»; C «Gana premios gratis»; D «Historia del vuelo». Abro A porque tiene mis palabras clave.",
        ["cuatro resultados con tres datos", "uno engañoso", "elige con razón", "usa palabras clave"],
        ["tabla de resultados y elección"],
        ["abrir el primero sin leer", "elegir el engañoso"],
        "Pregunta: «¿qué dato del resultado te hizo elegirlo?». Si no hay, pídele leer título y resumen.",
    ),
    reinforce="Busca con una persona de tu casa una cosa simple y lean juntos los títulos antes de abrir.",
    extend="Escribe una lista de tres señales de un resultado que no conviene abrir.",
)

# ------------------------------------------------------------------ OA 07, clase 3
reg(
    OA7, 3,
    materials="Hoja y lápiz. Las páginas se describen con texto; son ejemplos ficticios y las direcciones inventadas no existen.",
    use="Aprenderé a evaluar si una fuente es confiable y segura con señales sencillas. Sirve para elegir información verdadera y cuidar mis datos.",
    prior=["Sé leer los resultados antes de abrir.", "Sé que no se escriben datos personales en internet."],
    explain=[
        "Una fuente es el lugar de donde viene la información. No toda la información de internet es verdadera. Para evaluar una fuente, revisa cuatro señales: ¿quién la escribió? (autor o institución conocida), ¿cuándo se publicó? (fecha), ¿para qué se hizo? (enseñar, vender o entretener) y ¿cómo es la dirección? (clara y sin símbolos raros). Una página educativa, con autor y fecha, es mejor que una sin ellos.",
        "También conviene contrastar: buscar el mismo dato en dos o tres fuentes distintas. Si coinciden, es más confiable; si se contradicen, hay que seguir buscando o preguntar a un adulto. Esta clase es una simplificación: juzgar fuentes es complejo, y las señales ayudan pero no son una garantía.",
        "La seguridad también se revisa. Una página segura no pide datos personales, no te obliga a descargar nada, no llena la pantalla de ventanas emergentes y no te promete premios. La dirección que empieza con «https» usa una conexión protegida, pero no prueba que la página sea buena. Si algo te incomoda, cierra la página y avisa a una persona adulta.",
    ],
    vocab=[("fuente", "lugar de donde viene la información"), ("autor", "persona o institución que escribió la información"), ("fecha", "día en que se publicó la información"), ("contrastar", "comparar un dato en varias fuentes"), ("ventana emergente", "ventana que aparece sola sobre la página")],
    worked=[
        ("Evaluar con las cuatro señales", "Página A: «Plantas de interior», autora Ana Soto del Jardín Escuela (ficticio), fecha 2024, para enseñar. Página B: sin autor, sin fecha, que vende y promete premios. ¿Cuál es más confiable?", ["A tiene autor, fecha y propósito educativo.", "B no tiene autor ni fecha y quiere vender."], "A"),
        ("Contrastar fuentes", "Dos fuentes dicen que un cactus necesita poca agua y una tercera dice que necesita agua todos los días. ¿Qué haces?", ["Dos coinciden y una contradice.", "Busco una cuarta fuente o pregunto a un adulto."], "Seguir buscando o preguntar a un adulto"),
    ],
    mistakes=[
        ("Creer que toda la información de internet es verdadera.", "Cualquiera puede publicar cualquier cosa.", "Revisa autor, fecha, propósito y dirección, y contrasta."),
        ("Pensar que «https» garantiza que la información es buena.", "Solo indica una conexión protegida.", "Revisa además las otras señales."),
    ],
    R=[
        ("El lugar de donde viene la información, ¿es la fuente o el resumen?", "La fuente", "Es el origen de la información."),
        ("Comparar un dato en varias fuentes se llama...", "Contrastar", "Así se ve si coinciden."),
        ("Una ventana que aparece sola sobre la página, ¿es una ventana emergente o un autor?", "Una ventana emergente", "Es una señal de poca seguridad."),
    ],
    C=[
        ("¿Por qué se revisa la fecha de una fuente?", "Porque la información puede estar vieja", "Algunos datos cambian con el tiempo."),
        ("¿Por qué conviene contrastar con dos o tres fuentes?", "Para ver si coinciden", "Si coinciden, es más confiable."),
        ("¿Qué dato muestra el propósito de una página?", "Para qué fue hecha: enseñar, vender o entretener", "Cambia cuánto confiar."),
    ],
    A=[
        ("Página con autor, fecha y propósito educativo. ¿Es más confiable que una sin autor ni fecha?", "Sí", "Tiene más señales de confianza."),
        arith("Revisas 4 señales en una página y cumple 3. ¿Cuántas no cumple?", "4-3", "Se restan las cumplidas del total."),
        ("Una página te pide el nombre completo y la dirección de tu casa para mostrarte un dato. ¿Qué haces?", "La cierras y avisas a un adulto", "Pide datos personales sin necesidad."),
    ],
    Z=[
        ("Mía dice: «La página es buena porque empieza con https». ¿Qué le falta revisar?", "Autor, fecha, propósito y contraste", "Https solo indica conexión protegida."),
        ("Dos fuentes dicen cosas distintas sobre la misma fecha. ¿Debes confiar en la que tú prefieras?", "No", "Debes seguir buscando o preguntar a un adulto."),
    ],
    D=[
        arith("De 5 fuentes que revisaste, 3 coinciden en un dato y 2 no. ¿Cuántas más coinciden que no coinciden?", "3-2", "Se resta las que no coinciden de las que coinciden."),
        ("Una página vende un producto y dice que «es el mejor del mundo». ¿Cuál es su propósito: enseñar o vender?", "Vender", "Quiere que lo compres."),
    ],
    ctx=("Buscas cuánta luz necesita una planta de interior. Página 1: autora Ana Soto, sitio educativo, fecha 2024. Página 2: sin autor, llena de ventanas emergentes y pide tu dirección. Evalúa cuál usarías, con al menos dos señales.", "Usaría la página 1: tiene autor y fecha y es educativa. La página 2 no tiene autor, abre ventanas emergentes y pide mi dirección", "Compara con señales concretas."),
    sc=[
        ("¿Cuáles son las cuatro señales de una fuente?", "Autor, fecha, propósito y dirección", "Ayudan a evaluar."),
        ("En Tecnología: ¿Qué es contrastar?", "Comparar un dato en varias fuentes", "Si coinciden, es más confiable."),
        ("¿Qué haces si una página te incomoda o pide datos?", "Cerrarla y avisar a un adulto", "Se cuida la seguridad."),
    ],
    open_task=(
        "Escoge un par de páginas ficticias. Par 1: página A con autor, fecha y propósito educativo; página B sin autor y que vende con promesas. Par 2: página C con autor pero fecha de hace 10 años; página D con autor y fecha de este año. Evalúa con las cuatro señales, decide cuál usarías y qué contrastarías.",
        "Par 2: D, porque tiene autor y fecha actual; C tiene autor pero fecha vieja. Contrastaría el dato con una tercera fuente.",
        ["revisa las cuatro señales", "decide con razón", "propone contrastar", "menciona un cuidado de seguridad"],
        ["tabla de señales y decisión"],
        ["decidir solo por https", "no contrastar"],
        "Pregunta: «¿qué señales tiene esta página que la otra no?». Si no sabe, pídele volver a la lista.",
    ),
    reinforce="Pregunta a una persona de tu casa cómo sabe si una noticia es confiable.",
    extend="Escribe una lista de cinco señales de peligro en una página de internet.",
)

# ------------------------------------------------------------------ OA 07, clase 4
reg(
    OA7, 4,
    materials="Hoja y lápiz. El texto de ejemplo está escrito en el cuaderno. Si quieres, un procesador de textos o un cuaderno para guardar la ficha.",
    use="Aprenderé a extraer ideas de una página, escribirlas con mis palabras, anotar la fuente y almacenarlas en una carpeta. Sirve para usar la información sin copiarla.",
    prior=["Sé evaluar una fuente.", "Sé guardar un archivo con un buen nombre."],
    explain=[
        "Extraer información es sacar de una página las ideas que sirven para tu pregunta. No se copia todo. Se lee, se subrayan las ideas clave y se reescribe con tus propias palabras. A esto se le llama parafrasear. Copiar tal cual un texto ajeno sin decirlo no es honesto, porque parece que lo escribiste tú.",
        "También anotas la fuente: el título de la página, el autor y la fecha, y la dirección web. Así otras personas pueden comprobar el dato. Una ficha de información tiene cuatro partes: la pregunta, la idea con tus palabras, la fuente y la fecha en que la consultaste. Si usas una frase exacta, la pones entre comillas y dices de dónde es.",
        "Por último, almacenas la información en un lugar ordenado: una carpeta con un nombre claro, y un archivo con un nombre que diga el tema. Puede ser una ficha en el procesador de textos. Guarda de nuevo si agregas datos. Descargar archivos desconocidos no es seguro, por eso solo guarda texto que tú escribiste o archivos que una persona adulta revisó.",
    ],
    vocab=[("extraer", "sacar de una página las ideas que sirven"), ("parafrasear", "decir una idea con palabras propias"), ("atribuir", "decir de dónde viene una información"), ("ficha de información", "hoja con pregunta, idea propia, fuente y fecha"), ("almacenar", "guardar información en un lugar ordenado")],
    worked=[
        ("Parafrasear una idea", "Texto: «Los cactus guardan agua en su tallo y por eso pueden pasar días sin riego.» Escribe la idea con tus palabras.", ["Las ideas clave: guardan agua, tallo, días sin riego.", "Las digo de otra manera."], "El cactus acumula agua en su tallo, así que puede estar varios días sin que lo rieguen"),
        ("Anotar la fuente", "Tomaste la idea de la página «Cuidado del cactus», de Ana Soto, sitio ficticio www.jardin-escuela-ejemplo.example, consultada el 5 de marzo. Escribe la fuente.", ["Escribo título, autora y dirección.", "Agrego la fecha de consulta."], "Cuidado del cactus, Ana Soto, www.jardin-escuela-ejemplo.example, consultada el 5 de marzo"),
    ],
    mistakes=[
        ("Copiar el texto completo sin decir de dónde es.", "Parece que lo escribiste tú y no se reconoce al autor.", "Parafrasea y anota la fuente."),
        ("Guardar el dato sin la fuente.", "Nadie puede comprobar de dónde salió.", "Anota título, autor, dirección y fecha."),
    ],
    R=[
        ("Decir una idea con tus propias palabras se llama...", "Parafrasear", "Es reescribir sin copiar."),
        ("Decir de dónde viene la información se llama...", "Atribuir", "Se anota la fuente."),
        ("¿La ficha de información incluye la pregunta, la idea propia, la fuente y la fecha?", "Sí", "Son las cuatro partes de la ficha."),
    ],
    C=[
        ("¿Por qué no se copia el texto tal cual?", "Porque parecería que lo escribiste tú y no se reconoce al autor", "Es deshonesto sin citar."),
        ("¿Qué se hace con una frase exacta que quieres usar?", "Se pone entre comillas y se dice de dónde es", "Así se muestra que es de otra persona."),
        ("¿Por qué se anota la fecha de consulta?", "Porque la página puede cambiar", "Muestra cuándo se leyó."),
    ],
    A=[
        ("Texto: «Los girasoles jóvenes giran su flor siguiendo al Sol.» Elige la idea con tus palabras: A «Los girasoles jóvenes giran su flor siguiendo al Sol», B «La flor de un girasol joven se mueve hacia donde está el Sol».", "B", "A copia la frase; B la dice de otra manera."),
        arith("Tienes 4 fichas de información y cada una tiene 4 partes. ¿Cuántas partes escribiste en total?", "4*4", "Se multiplican las fichas por las partes de cada una."),
        ("Tomaste un dato de una página. ¿Qué cuatro datos de la fuente anotas: título, autor, dirección y qué más?", "La fecha", "La fecha de consulta completa la fuente."),
    ],
    Z=[
        ("Ema copió tres párrafos de una página y los entregó como suyos. ¿Qué debió hacer?", "Parafrasear y anotar la fuente", "Debe usar sus palabras y reconocer al autor."),
        ("Un archivo desconocido te pide descargarlo para ver el dato. ¿Qué haces?", "No lo descargas y avisas a un adulto", "Descargar archivos desconocidos no es seguro."),
    ],
    D=[
        arith("Guardas 3 fichas por tema y trabajas 4 temas. ¿Cuántas fichas almacenas?", "3*4", "Se multiplican las fichas por los temas."),
        ("Escribe el nombre de una carpeta y de un archivo para guardar la ficha sobre cuidados del cactus.", "Carpeta: tecnologia_4; archivo: ficha_cactus_v1", "Nombres claros que dicen el tema."),
    ],
    ctx=("Leíste: «La suculenta almacena agua en sus hojas gruesas, por eso soporta poco riego». La página se llama «Riego de suculentas», de Ana Soto, www.jardin-escuela-ejemplo.example, consultada el 12 de abril. Escribe tu ficha: pregunta, idea con tus palabras, fuente y fecha.", "Pregunta: ¿cuánta agua necesita una suculenta? Idea: guarda agua en las hojas gruesas, así que se riega poco. Fuente: Riego de suculentas, Ana Soto, www.jardin-escuela-ejemplo.example. Consultada el 12 de abril", "Cuatro partes y parafraseo."),
    sc=[
        ("En Tecnología: ¿Qué es parafrasear?", "Decir una idea con palabras propias", "Es no copiar tal cual."),
        ("¿Qué datos tiene la fuente?", "Título, autor, dirección y fecha", "Permiten comprobar el dato."),
        ("¿Se descargan archivos desconocidos?", "No", "No son seguros."),
    ],
    open_task=(
        "Escoge un texto breve. Texto 1: «Las abejas visitan las flores para tomar néctar y, sin querer, llevan polen de una flor a otra.» Texto 2: «El agua del mar es salada porque contiene sales disueltas que llegan desde las rocas.» Imagina la fuente (título, autor ficticio, dirección inventada y fecha). Escribe tu ficha: pregunta, idea con tus palabras, fuente completa, y el nombre de carpeta y archivo donde la guardarías.",
        "Texto 1: Pregunta: ¿cómo ayudan las abejas a las flores? Idea: pasan polen de una flor a otra mientras buscan néctar. Fuente: Las abejas, Pedro Díaz, www.naturaleza-ejemplo.example, 3 de mayo. Carpeta: ciencias_4; archivo: ficha_abejas_v1.",
        ["la idea está con palabras propias", "fuente con los cuatro datos", "nombre de carpeta y archivo claros", "pregunta que se responde"],
        ["ficha y nombre de almacenamiento"],
        ["copiar el texto tal cual", "olvidar la fuente"],
        "Pregunta: «¿cómo se dice esto con otras palabras?». Si copia, pídele explicarlo como a un amigo.",
    ),
    reinforce="Lee un párrafo de un libro y explícalo con tus palabras a una persona de tu casa.",
    extend="Prepara dos fichas de información sobre un mismo tema con fuentes distintas.",
)

# ------------------------------------------------------------------ OA 07, clase 5
reg(
    OA7, 5,
    materials="Hoja y lápiz. Las situaciones están escritas en el cuaderno. Si no hay internet, se resuelve en papel.",
    use="Aprenderé a usar lo que sé de búsqueda, fuentes y almacenamiento cuando cambia la condición: otra audiencia, fuentes que se contradicen o sin conexión. Sirve para resolver búsquedas reales.",
    prior=["Sé construir una búsqueda específica y leer resultados.", "Sé evaluar fuentes y anotar la fuente."],
    explain=[
        "Transferir es usar lo aprendido en una situación nueva. En una búsqueda real, las condiciones cambian: hay otra audiencia, fuentes que dicen cosas distintas o no hay conexión a internet. El proceso sigue siendo el mismo: buscar con palabras clave, leer resultados, evaluar la fuente, extraer con tus palabras, anotar la fuente y almacenar.",
        "Si cambia la audiencia, cambia la búsqueda y la elección de fuentes. Para niños de primero busca palabras simples y páginas con dibujos; para tu curso, páginas con datos. Si las fuentes se contradicen, busca una tercera y una cuarta, y fíjate en cuál tiene autor, fecha y propósito claros. Si no puedes decidir, pregunta a una persona adulta.",
        "Si no hay conexión, usa lo que ya almacenaste en tus fichas o busca la información en libros de la biblioteca de aula o de la casa, que también son fuentes y se citan con título y autor. Revisa siempre la seguridad: no compartas datos personales, no descargues archivos desconocidos y avisa si algo te incomoda.",
    ],
    vocab=[("transferir", "usar lo aprendido en una situación nueva"), ("condición", "dato que puede cambiar, como la audiencia o la conexión"), ("contradecirse", "decir cosas distintas sobre lo mismo"), ("fuente impresa", "libro o revista en papel"), ("proceso", "pasos que se repiten para lograr algo")],
    worked=[
        ("Cambia la audiencia", "Debes buscar información sobre el ciclo del agua para niños de primero, no para tu curso. ¿Qué cambia en la búsqueda?", ["Los niños pequeños entienden palabras simples.", "Agrego «para niños» y busco dibujos."], "Agrego «para niños» y busco páginas con dibujos y palabras simples"),
        ("Dos fuentes se contradicen", "Fuente A dice que el cactus se riega una vez por semana y fuente B dice que cada tres meses. ¿Qué haces?", ["Hay una contradicción.", "Busco más fuentes y reviso autor y fecha."], "Busco más fuentes y comparo autor, fecha y propósito"),
    ],
    mistakes=[
        ("Usar la misma búsqueda para cualquier audiencia.", "No siempre sirve igual a todos.", "Adapta palabras clave y fuentes a quien va a leer."),
        ("Quedarse con la primera fuente cuando hay una contradicción.", "No se sabe cuál es la correcta.", "Busca más fuentes y revisa sus señales."),
    ],
    R=[
        ("Usar lo aprendido en una situación nueva, ¿es transferir o almacenar?", "Transferir", "Esa es la definición."),
        ("Decir cosas distintas sobre lo mismo, ¿es contradecirse o parafrasear?", "Contradecirse", "Las fuentes no coinciden."),
        ("Un libro en papel, ¿puede ser una fuente?", "Sí", "También se cita con título y autor."),
    ],
    C=[
        ("¿Qué haces si no hay conexión a internet?", "Usas tus fichas o libros", "Las fuentes impresas también sirven."),
        ("¿Por qué cambia la búsqueda si cambia la audiencia?", "Porque cada audiencia entiende cosas distintas", "Se adaptan palabras y fuentes."),
        ("Si dos fuentes se contradicen, ¿qué conviene buscar?", "Una tercera y cuarta fuente", "Para ver cuál coincide con más."),
    ],
    A=[
        ("Debes buscar cómo se hace un avión de papel para niños de primero. Escribe una búsqueda de 3 a 6 palabras que agregue la audiencia.", "cómo hacer un avión de papel para niños", "Incluye tema y audiencia."),
        arith("Revisas 5 fuentes: 3 dicen una cosa y 2 otra. ¿Cuántas fuentes más apoyan la primera idea?", "3-2", "Se resta las que apoyan la segunda de las que apoyan la primera."),
        ("No hay internet y necesitas un dato sobre cactus. ¿Dónde lo buscas primero: en tus fichas o en una página que no abre?", "En tus fichas", "Ya está almacenado y no depende de conexión."),
    ],
    Z=[
        ("Julia encontró dos fuentes distintas y eligió la que le gustó más. ¿Qué debió hacer?", "Revisar autor, fecha y propósito, y buscar más fuentes", "La preferencia no decide la verdad de un dato."),
        ("Entre una página de internet sin autor y un libro de la biblioteca con autor y fecha, ¿cuál tiene más señales de confianza?", "El libro", "Tiene autor y fecha."),
    ],
    D=[
        arith("Para tu trabajo guardaste 6 fichas y necesitas 10. ¿Cuántas fichas te faltan?", "10-6", "Se resta lo que tienes de lo que necesitas."),
        ("Para el trabajo del ejercicio anterior, ¿qué haces primero con las 4 fichas que faltan: buscar con palabras clave específicas o abrir cualquier página?", "Buscar con palabras clave específicas", "Una búsqueda específica ahorra tiempo y mejora los resultados."),
    ],
    ctx=("Te piden explicar a niños de primero por qué las plantas necesitan luz, y no hay internet en tu casa. Dispones de tus fichas sobre plantas y de un libro de ciencias con autor y año. Escribe qué fuente usas, cómo adaptas la explicación y cómo anotas la fuente.", "Uso mis fichas y el libro; explico con palabras simples y dibujos grandes; anoto título, autor y año del libro", "Adapta audiencia, fuente y atribución."),
    sc=[
        ("¿Qué es transferir?", "Usar lo aprendido en una situación nueva", "Permite resolver búsquedas reales."),
        ("¿Qué haces si dos fuentes se contradicen?", "Buscas más fuentes", "Y revisas autor, fecha y propósito."),
        ("¿Un libro también se cita como fuente?", "Sí", "Con título y autor."),
    ],
    open_task=(
        "Escoge un cambio. Cambio 1: debes buscar información sobre el ciclo del agua para niños de primero. Cambio 2: no hay internet y necesitas un dato sobre plantas; tienes dos fichas y un libro. Escribe cómo cambia tu búsqueda o tu fuente, qué señales revisarías, cómo anotarías la fuente y qué cuidado de seguridad mantendrías.",
        "Cambio 1: busco «ciclo del agua para niños»; reviso autor y fecha; anoto título, autor y dirección de la página; no escribo datos personales.",
        ["adapta la búsqueda o la fuente al cambio", "revisa señales de la fuente", "anota la fuente", "menciona un cuidado de seguridad"],
        ["texto de adaptación del proceso"],
        ["usar la misma búsqueda para todos", "olvidar la fuente"],
        "Pregunta: «¿qué cambió y qué parte de tu proceso se adapta?». Si no sabe, pídele nombrar el cambio.",
    ),
    reinforce="Piensa cómo buscarías el mismo dato en un libro y en internet, y cuál es más rápido.",
    extend="Escribe un proceso de seis pasos para investigar un tema desde la búsqueda hasta guardar la ficha.",
)
