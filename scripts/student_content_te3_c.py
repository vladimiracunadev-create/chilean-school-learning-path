"""Cuaderno del estudiante, 3.º básico Tecnología: OA 05 (software de presentación), OA 06 (procesador de textos) y OA 07 (internet y buscadores).

Las pantallas se describen con texto y son EJEMPLOS FICTICIOS: cada programa real se ve distinto y aquí no se nombra ninguna marca.
Todas las clases tienen alternativa en papel (hojas dibujadas como pantallas).
Simplificación declarada: juzgar si una fuente es confiable es más complejo que las señales de este cuaderno.
No se usan datos personales ni direcciones reales: las direcciones web de ejemplo son inventadas.
"""
from __future__ import annotations

from student_content_te3_a import reg
from student_lessons import arith

OA5, OA6, OA7 = "TE03 OA 05", "TE03 OA 06", "TE03 OA 07"

# ------------------------------------------------------------------ OA 05, clase 1
reg(
    OA5, 1,
    materials="Hoja y lápiz. Las pantallas son un ejemplo ficticio descrito con palabras; si no hay computador, se dibujan en papel.",
    use="Aprenderé a decidir para qué y para quién será mi presentación antes de abrir el programa. Sirve para que mi mensaje llegue claro.",
    prior=["Sé ordenar ideas en una lista.", "Sé que un software es un programa del computador."],
    explain=[
        "Un software de presentación es un programa para mostrar ideas en pantallas llamadas diapositivas. En el ejemplo ficticio de esta clase, a la izquierda hay una columna con las diapositivas pequeñas y en el centro la diapositiva grande. Cada programa real se ve un poco distinto.",
        "Antes de abrirlo, define el propósito, que es para qué presentas: informar, explicar cómo se hace algo o convencer. También define la audiencia, que son las personas que te van a ver, por ejemplo tu curso o tu familia. El propósito y la audiencia cambian cómo hablas y cuántas palabras usas.",
        "Para niños de primero, usa pocas palabras y dibujos grandes. Para tu curso, puedes usar datos con números. Escribe una frase: «Quiero (propósito) a (audiencia) sobre (tema)». Después recién decide cuántas diapositivas hacer. Presentar sin pensar el propósito es como armar un objeto sin saber para qué sirve.",
    ],
    vocab=[("diapositiva", "pantalla de una presentación"), ("propósito", "para qué presentas"), ("audiencia", "personas que ven la presentación"), ("software de presentación", "programa para mostrar ideas en diapositivas")],
    worked=[
        ("Escribir la frase", "Quieres explicar a tu curso cómo cuidar una planta. Escribe la frase de propósito y audiencia.", ["Propósito: explicar.", "Audiencia: tu curso.", "Tema: cuidar una planta."], "Quiero explicar a mi curso cómo cuidar una planta"),
        ("Adaptar a la audiencia", "Presentas a niños de primero. ¿Pones párrafos largos o dibujos grandes con pocas palabras?", ["Los pequeños leen poco.", "Los dibujos ayudan."], "Dibujos grandes y pocas palabras"),
    ],
    mistakes=[
        ("Abrir el programa y empezar a poner texto.", "No se sabe qué mensaje quieres dar.", "Escribe primero el propósito y la audiencia."),
        ("Hacer la misma presentación para cualquier audiencia.", "Cada audiencia entiende de distinta forma.", "Adapta palabras y ejemplos."),
    ],
    R=[
        ("Una pantalla de una presentación ¿se llama diapositiva o archivo?", "Diapositiva", "Es cada pantalla."),
        ("Las personas que ven la presentación ¿son la audiencia o el propósito?", "La audiencia", "Son quienes miran."),
        ("Presentar para explicar cómo se hace algo ¿es un propósito o una audiencia?", "Un propósito", "Dice para qué presentas."),
    ],
    C=[
        ("¿Por qué se define el propósito antes de abrir el programa?", "Para saber qué mensaje dar", "Guía todo lo que harás."),
        ("¿Cambia la presentación si la audiencia son niños de primero o adultos?", "Sí", "Cambian palabras y ejemplos."),
        ("¿Todos los programas de presentación se ven iguales?", "No", "Cada uno se ve algo distinto."),
    ],
    A=[
        ("Quieres informar a tu familia sobre el reciclaje del cartón. Escribe la frase de propósito, audiencia y tema.", "Quiero informar a mi familia sobre el reciclaje del cartón", "Lleva los tres datos."),
        ("Presentarás a niños de primero. ¿Eliges 10 líneas de texto por diapositiva o una imagen grande con una palabra?", "Una imagen grande con una palabra", "A los más pequeños les sirve poco texto."),
        arith("Tu presentación tendrá 1 portada, 4 diapositivas de contenido y 1 de cierre. ¿Cuántas diapositivas son?", "1+4+1", "Se suman las tres partes."),
    ],
    Z=[
        ("Tomás dice: «Haré 20 diapositivas, mientras más mejor». ¿Qué le falta pensar primero? Responde con una frase.", "Su propósito y su audiencia", "El mensaje decide cuántas diapositivas."),
        ("Dos frases: A «Quiero explicar a mi curso cómo hacer un soporte de cartón» y B «Quiero hacer diapositivas». ¿Cuál tiene propósito y audiencia?", "A", "B no dice para qué ni para quién."),
    ],
    D=[
        ("Reto: la misma idea, cuidar una planta, para dos audiencias: niños de primero y tu curso. Escribe cómo cambia la presentación.", "Primero: dibujos grandes y pocas palabras; curso: pasos con números y datos", "Se adapta a cada audiencia."),
        arith("Presentas a 24 compañeros divididos en 4 grupos iguales. ¿Cuántos hay por grupo?", "24//4", "Se reparte en grupos iguales."),
    ],
    ctx=("Camila presentará a su curso cómo hacer un portalápices de cartón. Tendrá 5 minutos. Escribe la frase de propósito y audiencia, y qué hará distinto si la audiencia fueran niños de primero.", "Quiero explicar a mi curso cómo hacer un portalápices de cartón. Con niños de primero usaría más dibujos y menos palabras", "Propósito, audiencia y adaptación."),
    sc=[
        ("¿El propósito es para qué presentas?", "Sí", "Es el objetivo."),
        ("¿La audiencia es quien ve la presentación?", "Sí", "Son quienes miran."),
        ("¿Se piensa el propósito antes de abrir el programa?", "Sí", "Guía toda la presentación."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: cómo cuidar una planta. Tema 2: cómo reciclar cartón. Escribe la frase «Quiero (propósito) a (audiencia) sobre (tema)» para dos audiencias distintas y di cuántas diapositivas harías para cada una. Si tienes computador, usa un programa de presentación; si no, dibuja las diapositivas en hojas.",
        "Tema 1: Quiero explicar a mi curso cómo cuidar una planta (5 diapositivas). Quiero informar a mi familia sobre el riego (3 diapositivas).",
        ["escribe dos frases con propósito, audiencia y tema", "las audiencias son distintas", "indica el número de diapositivas"],
        ["dos frases y número de diapositivas"],
        ["no definir audiencia", "mismo mensaje para todos"],
        "Pregunta: «¿para quién es y qué quieres lograr?». Si no sabe, ayúdale con la frase.",
    ),
    reinforce="Piensa para quién y para qué le contarías a un amigo cómo se hace un objeto.",
    extend="Escribe la frase de propósito y audiencia para una presentación sobre seguridad con tijeras.",
)

# ------------------------------------------------------------------ OA 05, clase 2
reg(
    OA5, 2,
    materials="Hojas de papel para dibujar diapositivas, lápiz. Con computador es opcional: la pantalla es un ejemplo ficticio.",
    use="Aprenderé a organizar las diapositivas en una secuencia: portada, contenido y cierre. Sirve para que la presentación tenga un orden claro.",
    prior=["Sé definir propósito y audiencia.", "Sé que una diapositiva es una pantalla de la presentación."],
    explain=[
        "Una presentación tiene una secuencia, que es el orden de las diapositivas. La primera es la portada: tiene el título y tu nombre de pila si tu profesor lo pide. Después vienen las diapositivas de contenido y la última es el cierre, con la idea principal o un agradecimiento.",
        "Cada diapositiva de contenido tiene una sola idea. Si tienes dos ideas, usa dos diapositivas. Escribe un título corto arriba. En el ejemplo ficticio de esta clase, el título va arriba de la pantalla y el cuerpo va al medio. Para ordenar, mira la columna de diapositivas pequeñas y arrastra la que quieras mover; con un botón de deshacer vuelves atrás.",
        "Para decidir el orden, piensa en una historia: primero qué es, luego cómo se hace y al final para qué sirve. Si es un proceso, ordena por pasos: primero, segundo, tercero. Un buen orden ayuda a que la audiencia siga la idea sin perderse.",
    ],
    vocab=[("secuencia", "orden de las diapositivas"), ("portada", "primera diapositiva con el título"), ("cierre", "última diapositiva con la idea principal"), ("título", "texto corto que dice de qué trata la diapositiva")],
    worked=[
        ("Ordenar diapositivas", "Tienes: A «Cierre: gracias», B «Portada: Cómo cuidar una planta», C «Paso 1: regar». ¿Cuál es el orden?", ["La portada va primero.", "Luego el contenido.", "El cierre va al final."], "B, C, A"),
        ("Una idea por diapositiva", "Una diapositiva dice «Riego y luz». Tiene dos ideas. ¿Qué haces?", ["Separo las ideas.", "Hago una para riego y otra para luz."], "Dividirla en dos diapositivas"),
    ],
    mistakes=[
        ("Poner todo en una sola diapositiva.", "Se llena de texto y nadie lee.", "Una idea por diapositiva."),
        ("Poner el cierre al medio.", "Confunde a la audiencia.", "El cierre va al final."),
    ],
    R=[
        ("La diapositiva con el título de todo va al principio. ¿Es la portada o el cierre?", "La portada", "Presenta el tema."),
        ("La última diapositiva con la idea principal ¿es el cierre o la portada?", "El cierre", "Termina la presentación."),
        ("¿Cuántas ideas lleva cada diapositiva de contenido?", "Una", "Una idea por diapositiva."),
    ],
    C=[
        ("¿Por qué conviene una sola idea por diapositiva?", "Para que se lea y se entienda mejor", "Menos texto, más claridad."),
        ("¿Qué sirve para ordenar un proceso: pasos primero, segundo, tercero o letras al azar?", "Pasos primero, segundo, tercero", "Dan un orden claro."),
        ("Si te equivocas al mover una diapositiva, ¿qué botón usas?", "Deshacer", "Vuelve un paso atrás."),
    ],
    A=[
        ("Ordena: «Paso 2: sacar la bolsa», «Portada: Cómo reciclar cartón», «Cierre: gracias», «Paso 1: aplastar la caja». Escribe el orden correcto.", "Portada, Paso 1, Paso 2, Cierre", "La portada va primero y el cierre al final."),
        ("Una diapositiva dice «Qué es el cartón y cómo se recicla». ¿Cuántas diapositivas necesitas: 1 o 2?", "2", "Son dos ideas."),
        arith("Tu presentación tiene 1 portada, 3 de contenido y 1 de cierre. ¿Cuántas diapositivas tiene?", "1+3+1", "Se suman todas."),
    ],
    Z=[
        ("Rita puso el cierre en la diapositiva 2 de 5. ¿Qué problema habrá? Responde con una frase.", "La audiencia se confunde porque termina antes", "El cierre va al final."),
        ("Dos presentaciones sobre una planta: A con un solo cuadro lleno de texto y B con cinco diapositivas de una idea. ¿Cuál es más clara?", "B", "Cada idea tiene su lugar."),
    ],
    D=[
        ("Reto: diseña la secuencia de 5 diapositivas para «cómo hacer un portalápices» con portada, tres pasos y cierre.", "Portada; 1 medir; 2 cortar; 3 pegar; cierre", "Cinco diapositivas ordenadas."),
        arith("Tienes 6 diapositivas y borras 2. ¿Cuántas quedan?", "6-2", "Se restan las borradas."),
    ],
    ctx=("Mateo presentará «cómo cuidar una planta» a su curso. Debe tener portada, 3 ideas (riego, luz, tierra) y cierre. Escribe la secuencia con el título de cada diapositiva.", "1 Portada: Cómo cuidar una planta; 2 Riego; 3 Luz; 4 Tierra; 5 Cierre: gracias", "Portada, tres ideas y cierre."),
    sc=[
        ("¿El cierre va al principio o al final?", "Al final", "Termina la presentación."),
        ("¿Cada diapositiva lleva una idea?", "Sí", "Así se entiende."),
        ("¿La portada es la primera diapositiva?", "Sí", "Presenta el tema."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: cómo cuidar una planta (riego, luz, tierra). Tema 2: cómo reciclar cartón (aplastar, guardar, llevar). Escribe la secuencia de 5 diapositivas con el título de cada una. Si tienes computador, hazlas en un programa de presentación; si no, en hojas.",
        "Tema 1: 1 Portada; 2 Riego; 3 Luz; 4 Tierra; 5 Cierre.",
        ["incluye portada y cierre", "una idea por diapositiva", "títulos cortos", "orden lógico"],
        ["lista o diapositivas con títulos"],
        ["dos ideas en una diapositiva", "cierre antes del final"],
        "Pregunta: «¿qué idea tiene esta diapositiva?». Si tiene dos, pídele dividirla.",
    ),
    reinforce="Ordena en una hoja las partes de la historia de tu día: mañana, tarde y noche.",
    extend="Haz la secuencia de una presentación de seis diapositivas sobre seguridad en la sala.",
)

# ------------------------------------------------------------------ OA 05, clase 3
reg(
    OA5, 3,
    materials="Hojas, lápiz, dibujos propios o fotografías hechas por ti. Pantallas descritas con texto como ejemplo ficticio.",
    use="Aprenderé a combinar texto con una imagen mía o autorizada. Sirve para que mi presentación se entienda y respete a quien creó cada imagen.",
    prior=["Sé ordenar diapositivas con una idea cada una.", "Sé que una imagen puede ser dibujo o fotografía."],
    explain=[
        "Una diapositiva combina texto e imagen. El texto dice la idea en pocas palabras; la imagen la muestra. Una buena imagen ayuda a entender y no es solo decoración. En el ejemplo ficticio, el botón de insertar imagen está arriba; eliges el archivo y aparece en la diapositiva.",
        "Las imágenes que uses deben ser tuyas o autorizadas. Una imagen propia es un dibujo que hiciste tú o una fotografía que tomaste, sin personas que no lo quieran. Una imagen autorizada es una que su autor permite usar, y debes anotar quién es el autor. No uses imágenes de otras personas sin permiso, porque cada una tiene un autor.",
        "Cuida los datos personales: no pongas direcciones, teléfonos ni fotos de compañeros sin permiso de ellos y de sus familias. Pon la imagen al lado del texto, no encima. Anota al pie de la diapositiva: «Imagen: dibujo mío» o «Imagen: de (autor)».",
    ],
    vocab=[("imagen propia", "dibujo o foto que hiciste tú"), ("imagen autorizada", "imagen cuyo autor permite usarla"), ("autor", "persona que creó una imagen o un texto"), ("insertar", "poner un archivo dentro de la diapositiva"), ("dato personal", "información que identifica a una persona")],
    worked=[
        ("Elegir la imagen", "Para una diapositiva sobre regar una planta tienes: A tu dibujo de una regadera, B foto de un amigo sin permiso. ¿Cuál usas?", ["Tu dibujo es propio.", "La foto del amigo no tiene permiso."], "A, tu dibujo"),
        ("Dar crédito", "Usas un dibujo tuyo. Escribe el crédito al pie.", ["Digo quién lo hizo.", "Escribo: «Imagen: dibujo mío»."], "Imagen: dibujo mío"),
    ],
    mistakes=[
        ("Copiar una imagen de internet sin saber quién es el autor.", "No sabes si puedes usarla y no das crédito.", "Usa imágenes propias o autorizadas y anota el autor."),
        ("Tapar el texto con la imagen.", "No se lee el mensaje.", "Pon la imagen al lado del texto."),
    ],
    R=[
        ("Un dibujo que hiciste tú ¿es una imagen propia o autorizada?", "Propia", "Lo creaste tú."),
        ("Persona que creó una imagen ¿se llama autor o usuario?", "Autor", "Creó la imagen."),
        ("¿Se ponen teléfonos y direcciones en una diapositiva?", "No", "Son datos personales."),
    ],
    C=[
        ("¿Por qué se anota el autor de una imagen autorizada?", "Para reconocer a quien la creó", "Respeta su trabajo."),
        ("¿La imagen debe ayudar a entender o solo decorar?", "Ayudar a entender", "Debe mostrar la idea."),
        ("¿Se puede usar una foto de un compañero sin pedir permiso?", "No", "Hay que pedir permiso a él y a su familia."),
    ],
    A=[
        ("Tu diapositiva «Luz» tiene el dibujo de un sol que hiciste tú. Escribe el crédito.", "Imagen: dibujo mío", "Indica el autor."),
        ("Quieres una imagen de un riego. ¿Usas tu dibujo o una imagen cuyo autor no conoces?", "Tu dibujo", "Es una imagen propia y segura."),
        arith("Tienes dos diapositivas con dibujo propio y tres sin imagen. ¿Cuántas diapositivas tienes?", "2+3", "Se suman las que llevan imagen y las que no."),
    ],
    Z=[
        ("Lía copió una imagen sin saber de quién era. ¿Qué dos problemas hay? Responde con una frase.", "No sabe si puede usarla y no da crédito al autor", "Falta permiso y crédito."),
        ("Dos diapositivas: A con la imagen encima del texto y B con la imagen al lado. ¿Cuál se lee mejor?", "B", "El texto queda visible."),
    ],
    D=[
        ("Reto: para tu diapositiva «Tierra», escribe el texto (una frase corta), la imagen que usarías y el crédito.", "Texto: La planta necesita tierra suave. Imagen: dibujo mío de una maceta. Crédito: dibujo mío", "Texto, imagen y crédito."),
        arith("Una presentación tiene 8 diapositivas y 5 llevan imagen propia. ¿Cuántas no llevan imagen propia?", "8-5", "Se resta."),
    ],
    ctx=("Valeria presenta «cómo reciclar cartón». Tiene su dibujo de una caja aplastada y una foto de su compañero Ben sin permiso. Escribe cuál usa y cómo da el crédito.", "Usa su dibujo de la caja aplastada y escribe: Imagen: dibujo mío", "Elige la propia y da crédito."),
    sc=[
        ("¿Se usa una imagen propia o autorizada?", "Propia o autorizada", "Respeta al autor."),
        ("¿Se anota el autor?", "Sí", "Es una buena práctica."),
        ("¿La imagen debe tapar el texto?", "No", "No se leería."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: «Luz» para una presentación de cuidar una planta. Tema 2: «Aplastar la caja» para reciclar cartón. Dibuja una imagen tuya para la diapositiva, escribe una frase corta de texto y el crédito, y di dónde pones la imagen respecto del texto.",
        "Tema 1: dibujo de un sol; texto: La planta necesita luz; crédito: dibujo mío; imagen al lado del texto.",
        ["usa imagen propia o autorizada", "escribe una frase corta", "da el crédito", "pone la imagen al lado del texto"],
        ["dibujo, frase y crédito"],
        ["usar imágenes sin permiso", "imagen sobre el texto"],
        "Pregunta: «¿de quién es esta imagen?». Si no lo sabe, no la uses.",
    ),
    reinforce="Haz un dibujo de una idea de ciencias y escribe su crédito.",
    extend="Escribe cómo pedirías permiso a un compañero para usar su dibujo en tu presentación.",
)

# ------------------------------------------------------------------ OA 05, clase 4
reg(
    OA5, 4,
    materials="Hoja, lápiz. Las diapositivas de ejemplo están descritas en el cuaderno. Pantallas ficticias.",
    use="Aprenderé a presentar y a revisar que mi presentación se lea bien. Sirve para que la audiencia vea y entienda sin esfuerzo.",
    prior=["Sé organizar una secuencia de diapositivas.", "Sé usar imágenes propias con crédito."],
    explain=[
        "Una presentación legible se lee fácilmente desde lejos. Para eso, usa letras grandes, un color de letra que contraste con el fondo (por ejemplo letras oscuras sobre fondo claro) y pocas palabras. Mira la diapositiva a un paso de distancia: si no se lee, hay que agrandar.",
        "Una regla simple es un máximo de seis líneas por diapositiva y pocas palabras por línea. No pongas un párrafo entero. Las palabras que dices en voz alta son las que explican; la pantalla solo ayuda. En el ejemplo ficticio, cambias el tamaño con una caja que muestra un número: más número, letra más grande.",
        "Al presentar: habla fuerte, mira a la audiencia, no leas todo y muestra con la mano la parte de la imagen que explicas. Practica antes y mide el tiempo. Pide a alguien que te diga qué no se vio bien y cámbialo. Revisa la ortografía y que los datos coincidan con la información.",
    ],
    vocab=[("legible", "que se lee fácilmente"), ("contraste", "diferencia clara entre el color de la letra y el fondo"), ("tamaño de letra", "qué tan grande se ve la letra"), ("practicar", "ensayar antes de presentar")],
    worked=[
        ("Revisar contraste", "Una diapositiva tiene letras amarillo claro sobre fondo blanco. ¿Se lee bien?", ["Los dos colores son muy claros.", "Casi no hay diferencia."], "No, falta contraste; usa letras oscuras"),
        ("Menos texto", "Una diapositiva tiene 12 líneas. La regla es máximo 6. ¿Cuántas debes sacar?", ["12 menos 6.", "Salen 6."], "6 líneas"),
    ],
    mistakes=[
        ("Poner letra pequeña para que quepa todo.", "No se lee desde lejos.", "Saca palabras y agranda la letra."),
        ("Leer toda la diapositiva en voz alta.", "La audiencia se aburre.", "Explica con tus palabras."),
    ],
    R=[
        ("Letras oscuras sobre fondo claro ¿tienen buen contraste o mal contraste?", "Buen contraste", "Se ven bien."),
        ("Una diapositiva con muchas palabras pequeñas ¿es legible o no?", "No", "Cuesta leerla desde lejos."),
        ("Ensayar antes de presentar ¿se llama practicar o cerrar?", "Practicar", "Practicar es ensayar antes."),
    ],
    C=[
        ("¿Por qué conviene mirar la diapositiva a un paso de distancia?", "Para ver si se lee de lejos", "La audiencia está lejos."),
        ("¿Qué explica la presentación: la pantalla sola o tus palabras con la pantalla?", "Tus palabras con la pantalla", "La pantalla ayuda."),
        ("Si la letra de tu diapositiva es pequeña, ¿qué haces?", "La agrandas", "Mejora la lectura."),
    ],
    A=[
        arith("Una diapositiva tiene 10 líneas y el máximo es 6. ¿Cuántas líneas sobran?", "10-6", "Se resta el máximo."),
        ("Letras blancas sobre fondo amarillo claro. ¿Las cambias a letras oscuras o las dejas?", "Las cambias a oscuras", "Mejora el contraste."),
        ("Practicas tu presentación y dura 3 minutos. El límite son 4 minutos. ¿Te sobra tiempo? Responde sí o no.", "Sí", "3 es menor que 4."),
    ],
    Z=[
        ("Ema agrandó la letra pero ahora no cabe. ¿Qué haces con el texto? Responde con una frase.", "Saco palabras o separo en otra diapositiva", "Lo importante es que se lea."),
        ("Dos diapositivas: A con 4 líneas cortas y B con un párrafo largo. ¿Cuál es legible?", "A", "Tiene pocas palabras."),
    ],
    D=[
        ("Reto: escribe una lista de 4 puntos para revisar la legibilidad de una diapositiva.", "Letra grande, buen contraste, pocas líneas, imagen al lado del texto", "Cuatro revisiones útiles."),
        arith("Tu presentación tiene 6 diapositivas y dedicas 30 segundos a cada una. ¿Cuántos segundos dura?", "6*30", "Se multiplica por 30.", " segundos"),
    ],
    ctx=("Pablo revisa su diapositiva «Riego»: tiene 9 líneas con letra pequeña y letras grises sobre fondo gris claro. El máximo son 6 líneas. Escribe tres cambios.", "Sacar 3 líneas, agrandar la letra y usar letras oscuras", "Cambia cantidad, tamaño y contraste."),
    sc=[
        ("¿Una diapositiva legible se lee de lejos?", "Sí", "Es su objetivo."),
        ("¿Se lee todo en voz alta?", "No", "Se explica con tus palabras."),
        ("¿Se practica antes?", "Sí", "Mejora la presentación."),
    ],
    open_task=(
        "Usa este caso: una diapositiva de «Cómo cuidar una planta» tiene 10 líneas, letra pequeña y letras amarillo claro sobre fondo blanco. Escribe qué tres cosas cambiarías, redacta la diapositiva mejorada con máximo 6 líneas y practica una vez en voz alta.",
        "Cambios: sacar 4 líneas, agrandar la letra y usar letras oscuras. Nueva: Riego: poca agua; Luz: cerca de la ventana; Tierra: suave.",
        ["identifica tres problemas", "redacta con máximo 6 líneas", "usa letras oscuras o buen contraste", "practica en voz alta"],
        ["diapositiva mejorada y nota de práctica"],
        ["mantener mucho texto", "no revisar contraste"],
        "Pregunta: «¿se lee desde un paso de distancia?». Si no, agranda o saca texto.",
    ),
    reinforce="Mira un cartel de tu casa o calle y di si se lee desde lejos.",
    extend="Haz una lista de verificación de cinco puntos para revisar una presentación.",
)

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja y lápiz. La pantalla del procesador de textos es un ejemplo ficticio descrito con palabras; sin computador, se escribe a mano en una hoja dividida en párrafos.",
    use="Aprenderé a escribir un texto en un procesador de textos y a organizarlo en un título y párrafos. Sirve para que se lea ordenado.",
    prior=["Sé escribir oraciones con mayúscula y punto.", "Sé que un software es un programa del computador."],
    explain=[
        "Un procesador de textos es un programa para escribir, cambiar y guardar textos. En el ejemplo ficticio de esta clase, arriba hay una barra de botones y debajo una página blanca donde aparece lo que escribes. Cada programa real se ve algo distinto.",
        "Un texto se organiza en párrafos. Un párrafo es un grupo de oraciones que habla de una misma idea. Para empezar otro párrafo, presionas la tecla Enter, que baja una línea. El texto tiene un título corto arriba. Cada oración empieza con mayúscula y termina con punto. Deja un espacio, no dos, después del punto.",
        "Escribe de a poco y mira la pantalla mientras tecleas, para ver errores. Si ves una palabra subrayada, puede estar mal escrita; revísala. En esta clase solo usa datos de ejemplo: no escribas tus datos personales como dirección o teléfono. Practica con las frases del cuaderno.",
    ],
    vocab=[("procesador de textos", "programa para escribir, cambiar y guardar textos"), ("párrafo", "grupo de oraciones sobre una misma idea"), ("Enter", "tecla que baja una línea y empieza otro párrafo"), ("título", "texto corto arriba que dice de qué trata"), ("barra de botones", "fila de botones con acciones del programa")],
    worked=[
        ("Separar en párrafos", "Texto: «Mi planta necesita luz. Está junto a la ventana. Riego mi planta los lunes. Uso una taza de agua». ¿Cuántas ideas hay y cuántos párrafos conviene?", ["Una idea es la luz.", "Otra idea es el riego.", "Dos ideas, dos párrafos."], "Dos párrafos"),
        ("Usar Enter", "Terminaste un párrafo sobre la luz y quieres empezar otro sobre el riego. ¿Qué tecla usas?", ["Necesito bajar y empezar otro.", "La tecla Enter baja una línea."], "Enter"),
    ],
    mistakes=[
        ("Escribir todo seguido en un solo bloque.", "Es difícil de leer.", "Separa las ideas con Enter."),
        ("Empezar una oración sin mayúscula.", "No se entiende dónde empieza.", "Empieza con mayúscula y termina con punto."),
    ],
    R=[
        ("Un grupo de oraciones sobre una misma idea ¿es un párrafo o un título?", "Un párrafo", "Habla de una sola idea."),
        ("Para bajar una línea, ¿presionas Enter o la barra espaciadora?", "Enter", "Baja una línea."),
        ("¿El título va arriba del texto o al final?", "Arriba", "Dice de qué trata."),
    ],
    C=[
        ("¿Por qué conviene separar el texto en párrafos?", "Para que se lea ordenado", "Cada idea queda separada."),
        ("¿Con qué letra empieza cada oración?", "Con mayúscula", "Marca el inicio."),
        ("Si una palabra está subrayada, ¿qué haces?", "La revisas", "Puede estar mal escrita."),
    ],
    A=[
        ("Texto: «Cuidar una planta es fácil. Necesita agua. Necesita luz». ¿Cuántas oraciones tiene?", "3", "Cada punto cierra una oración."),
        ("Quieres escribir dos ideas, plantas y reciclaje. ¿Haces un párrafo o dos?", "Dos", "Una idea por párrafo."),
        arith("Escribiste 3 párrafos de 4 oraciones cada uno. ¿Cuántas oraciones son?", "3*4", "Se multiplican párrafos por oraciones."),
    ],
    Z=[
        ("Rita escribió 8 oraciones de dos ideas en un solo bloque. ¿Qué mejora le sugieres? Responde con una frase.", "Separar en dos párrafos con Enter", "Cada idea va aparte."),
        ("Dos textos: A con título y dos párrafos, B todo seguido. ¿Cuál se lee mejor?", "A", "Está ordenado y se entiende."),
    ],
    D=[
        ("Reto: escribe un título y dos párrafos de dos oraciones cada uno sobre cuidar el medioambiente.", "Título: Cuidemos el medioambiente. P1: Reciclo el cartón. Lo llevo al punto limpio. P2: Cierro la llave. Ahorro agua.", "Título y dos párrafos."),
        arith("Un texto tiene 5 párrafos y borras 2. ¿Cuántos párrafos quedan?", "5-2", "Se restan."),
    ],
    ctx=("Elena escribe sobre su portalápices: dice cómo lo hizo (3 oraciones) y para qué sirve (2 oraciones). Escribe cuántos párrafos hace, qué título pone y qué tecla usa entre ellos.", "Dos párrafos; título «Mi portalápices»; tecla Enter", "Organiza el texto."),
    sc=[
        ("¿Un párrafo trata de una idea?", "Sí", "Es su definición."),
        ("¿Se usa Enter para separar párrafos?", "Sí", "Baja una línea."),
        ("¿Las oraciones empiezan con mayúscula?", "Sí", "Marca el inicio."),
    ],
    open_task=(
        "Escoge un tema. Tema 1: cómo cuidas una planta. Tema 2: cómo reciclas cartón. Escribe un título y dos párrafos de dos oraciones cada uno. Si tienes computador, usa un procesador de textos; si no, escribe en una hoja. No pongas datos personales.",
        "Tema 1: Cuido mi planta. (Párrafo 1) Mi planta necesita luz. La dejo junto a la ventana. (Párrafo 2) La riego cuando la tierra está seca. Uso poca agua.",
        ["escribe un título", "hace dos párrafos", "oraciones con mayúscula y punto", "sin datos personales"],
        ["texto con título y dos párrafos"],
        ["un solo bloque", "faltan mayúsculas o puntos"],
        "Pregunta: «¿cuántas ideas hay en este párrafo?». Si hay dos, separa.",
    ),
    reinforce="Escribe dos frases sobre tu día y sepáralas en dos párrafos.",
    extend="Escribe un texto de tres párrafos sobre cómo cuidar el medioambiente.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja y lápiz. Los textos de práctica están escritos en el cuaderno. Pantallas descritas como ejemplo ficticio.",
    use="Aprenderé a editar un texto: seleccionar, copiar, cortar, pegar, mover y deshacer. Sirve para corregir sin escribir todo de nuevo.",
    prior=["Sé escribir párrafos con título.", "Sé que un botón del programa hace una acción."],
    explain=[
        "Editar es cambiar un texto que ya escribiste. Primero seleccionas: pasas el puntero (la flechita del ratón) sobre las palabras manteniendo apretado el botón y quedan marcadas. Lo marcado es lo que cambiará. Selecciona solo lo necesario.",
        "Con lo seleccionado puedes hacer cuatro cosas. Copiar hace una copia y deja el original. Cortar saca el texto de su lugar. Pegar pone lo copiado o cortado donde está el cursor. Para mover una frase, la cortas y la pegas en otro lugar. En el ejemplo ficticio, los botones dicen copiar, cortar y pegar, y hay una flecha que dice deshacer.",
        "Si te equivocas, usa deshacer, que vuelve atrás un paso. También puedes borrar con la tecla de borrar. Antes de borrar, revisa qué está seleccionado. Después de editar, lee otra vez el texto completo para ver si tiene sentido.",
    ],
    vocab=[("seleccionar", "marcar una parte del texto para cambiarla"), ("copiar", "hacer una copia sin sacar el original"), ("cortar", "sacar el texto de su lugar"), ("pegar", "poner lo copiado o cortado en otro lugar"), ("cursor", "línea que parpadea y muestra dónde escribirás")],
    worked=[
        ("Mover una frase", "Texto: «Riego la planta. Mi planta necesita luz.» Quieres que «Mi planta necesita luz.» vaya primero. ¿Qué haces?", ["Selecciono la frase de la luz.", "La corto.", "Pongo el cursor al inicio y pego."], "Seleccionar, cortar y pegar al inicio"),
        ("Copiar o cortar", "Quieres repetir el título en otra parte sin sacarlo de arriba. ¿Copiar o cortar?", ["Copiar deja el original.", "Cortar lo saca."], "Copiar"),
    ],
    mistakes=[
        ("Seleccionar todo el texto para cambiar una palabra.", "Si escribes encima, borras todo.", "Selecciona solo la palabra."),
        ("Cortar cuando querías copiar.", "El texto desaparece de su lugar.", "Usa copiar para dejar el original."),
    ],
    R=[
        ("Marcar una parte del texto ¿es seleccionar o pegar?", "Seleccionar", "Se marca lo que cambiarás."),
        ("Hacer una copia sin sacar el original ¿es copiar o cortar?", "Copiar", "El original queda."),
        ("Volver un paso atrás ¿es deshacer o pegar?", "Deshacer", "Devuelve el último cambio."),
    ],
    C=[
        ("¿Por qué conviene seleccionar solo lo necesario?", "Para no borrar o cambiar de más", "Se cambia lo marcado."),
        ("Para mover una frase, ¿qué dos acciones haces?", "Cortar y pegar", "Se saca y se pone en otro lugar."),
        ("¿Qué haces si te equivocas al borrar?", "Usas deshacer", "Vuelve el paso."),
    ],
    A=[
        ("Texto: «Mi planta es linda. Necesita agua.» Quieres repetir «Necesita agua.» al final sin sacarla. ¿Copiar o cortar?", "Copiar", "Se repite sin sacar."),
        ("Quieres cambiar la palabra «linda» por «verde». ¿Qué seleccionas primero?", "La palabra linda", "Solo la palabra que cambiarás."),
        arith("Tu texto tiene 5 frases. Copias 1 frase y la pegas en otro lugar. ¿Cuántas frases tiene ahora?", "5+1", "Copiar deja el original y agrega una más."),
    ],
    Z=[
        ("Mía seleccionó un párrafo y escribió una letra encima. El párrafo desapareció. ¿Qué botón la salva? Responde con una frase.", "Deshacer", "Vuelve el texto anterior."),
        ("Dos formas de poner una frase en otro lugar: A cortar y pegar, B copiar y pegar. ¿Cuál deja la frase repetida?", "B", "Copiar deja el original."),
    ],
    D=[
        ("Reto: ordena estos pasos para mover un párrafo: pegar, cortar, seleccionar, poner el cursor.", "Seleccionar, cortar, poner el cursor, pegar", "Ese es el orden correcto."),
        arith("Un texto tiene 7 frases. Cortas 2 y no pegas. ¿Cuántas frases quedan?", "7-2", "Se restan las cortadas."),
    ],
    ctx=("Sofía escribió: «Cierro la llave. Ahorro agua. Reciclo el cartón.» Quiere que «Reciclo el cartón.» vaya primero. Escribe los pasos y qué botón usa si se equivoca.", "Seleccionar la frase, cortar, poner el cursor al inicio, pegar; deshacer si se equivoca", "Pasos ordenados con deshacer."),
    sc=[
        ("¿Se selecciona antes de copiar?", "Sí", "Se necesita lo marcado."),
        ("¿Cortar saca el texto?", "Sí", "Lo quita de su lugar."),
        ("¿Se lee el texto después de editar?", "Sí", "Para ver si tiene sentido."),
    ],
    open_task=(
        "Usa este texto: «Cierro la llave. Reciclo el cartón. Ahorro agua. Apago la luz.» Reordena las frases para que las dos de agua queden juntas, usando seleccionar, cortar y pegar. Escribe los pasos y el texto final. Si no tienes computador, escribe cada frase en un papelito y muévelos.",
        "Texto final: Cierro la llave. Ahorro agua. Reciclo el cartón. Apago la luz.",
        ["escribe los pasos", "las frases de agua quedan juntas", "usa seleccionar, cortar y pegar", "lee el texto final"],
        ["pasos y texto final"],
        ["cortar sin seleccionar", "no leer el resultado"],
        "Pregunta: «¿qué marcaste antes de cortar?». Si no seleccionó, repite desde el principio.",
    ),
    reinforce="Mueve frases de lugar con papelitos y lee si tienen sentido.",
    extend="Escribe una lista de 6 acciones y reordénala por el orden en que se hacen.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja y lápiz. Los textos de ejemplo están en el cuaderno. Pantalla ficticia descrita con texto.",
    use="Aprenderé a dar formato que ayude a leer: título más grande, negrita en palabras clave, listas y alineación. Sirve para que el texto sea claro.",
    prior=["Sé editar con seleccionar, copiar, cortar y pegar.", "Sé organizar un texto en párrafos."],
    explain=[
        "El formato es cómo se ve el texto. Se aplica seleccionando y luego eligiendo un botón. En el ejemplo ficticio, la barra tiene botones para negrita, tamaño de letra, lista y alineación. El formato sirve cuando ayuda a leer, no para decorar demasiado.",
        "Reglas simples: el título más grande que el resto; la negrita solo en palabras clave; una letra de tamaño legible, por ejemplo 12 o más; y pocas fuentes distintas, máximo dos. Una lista con puntos ordena ideas cortas, como los pasos de una tarea. Alinear a la izquierda es lo más cómodo para leer.",
        "Si usas muchos colores, tamaños y tipos de letra, el texto cansa. Un buen texto tiene un formato parejo. Después de dar formato, léelo otra vez y pregúntate: ¿se entiende más rápido? Si no, quita lo que sobra.",
    ],
    vocab=[("formato", "cómo se ve el texto"), ("negrita", "letra más gruesa para destacar"), ("lista con puntos", "ideas cortas una bajo otra con un punto adelante"), ("alineación", "lado hacia el que se acomoda el texto"), ("tamaño de letra", "qué tan grande es la letra")],
    worked=[
        ("Dar formato a un título", "Texto: «Cómo cuidar una planta». Quieres que se note como título. ¿Qué haces?", ["Selecciono el título.", "Lo agrando y lo pongo en negrita."], "Seleccionarlo, agrandarlo y ponerlo en negrita"),
        ("Cuándo usar una lista", "Tienes los pasos: medir, cortar, pegar. ¿Los escribes en un párrafo largo o en lista con puntos?", ["Son ideas cortas en orden.", "La lista las ordena."], "Lista con puntos"),
    ],
    mistakes=[
        ("Poner todo el texto en negrita.", "Nada se destaca.", "Usa negrita solo en palabras clave."),
        ("Usar cinco tipos de letra distintos.", "El texto cansa y se ve desordenado.", "Usa máximo dos."),
    ],
    R=[
        ("Letra más gruesa para destacar ¿es negrita o lista?", "Negrita", "Es el formato más grueso."),
        ("Ideas cortas una bajo otra con puntos ¿son una lista o un título?", "Una lista", "Se ordenan con puntos."),
        ("¿El título debe ser más grande o más pequeño que el resto?", "Más grande", "Así se distingue."),
    ],
    C=[
        ("¿Para qué sirve el formato?", "Para ayudar a leer", "Hace el texto más claro."),
        ("¿Por qué no conviene poner todo en negrita?", "Porque nada se destaca", "Todo parece igual."),
        ("¿Cuántos tipos de letra conviene usar como máximo?", "Dos", "Menos mezcla, más orden."),
    ],
    A=[
        ("Tienes los pasos «lavar el pincel», «secar el pincel», «guardar el pincel». ¿Los pones en lista o en párrafo?", "En lista", "Son pasos cortos en orden."),
        ("En la frase «La planta necesita luz», quieres destacar la palabra clave. ¿Cuál pones en negrita: «La» o «luz»?", "luz", "Es la palabra que lleva la idea importante."),
        ("Un párrafo largo del cuerpo del texto, ¿lo alineas a la izquierda o lo centras para leerlo cómodo?", "A la izquierda", "Es la alineación más cómoda para leer."),
    ],
    Z=[
        ("Lía usó tres colores, cuatro tamaños y tres tipos de letra en un texto corto. ¿Qué le recomiendas? Responde con una frase.", "Quitar lo que sobra y dejar un formato parejo", "Demasiado formato cansa."),
        ("Dos textos: A con título grande y lista, B con todo grande y de colores. ¿Cuál se lee mejor?", "A", "Tiene jerarquía clara."),
    ],
    D=[
        ("Reto: da formato a este texto: título «Cuidar una planta» y los pasos regar, dar luz, revisar la tierra. Escribe cómo queda.", "Título grande y en negrita; lista con regar, dar luz, revisar la tierra", "Título destacado y lista."),
        arith("Un texto tiene 10 palabras en negrita y quitas 6. ¿Cuántas quedan en negrita?", "10-6", "Se restan."),
    ],
    ctx=("Camila escribió las instrucciones de su portalápices: título, 4 pasos y una advertencia de seguridad. Escribe cómo darías formato: título, pasos y advertencia.", "Título grande en negrita; pasos en lista; advertencia en negrita", "Cada parte con su formato."),
    sc=[
        ("¿El formato debe ayudar a leer?", "Sí", "Es su función."),
        ("¿La negrita se usa en todo el texto?", "No", "Solo en palabras clave."),
        ("¿Las listas ordenan ideas cortas?", "Sí", "Dan orden a las ideas."),
    ],
    open_task=(
        "Usa este texto: Cuidar una planta. Dar luz. Regar con poca agua. Revisar la tierra. Cuidado: no dejar agua acumulada en el plato. Dale formato: título más grande, lista con los tres pasos y negrita solo en «Cuidado». Escribe cómo queda. Si no hay computador, hazlo en papel con tamaños distintos de letra.",
        "Título grande; lista con tres pasos; «Cuidado» en negrita.",
        ["título más grande", "pasos en lista", "negrita solo en la advertencia", "formato parejo"],
        ["texto con formato"],
        ["negrita en todo", "demasiados colores y letras"],
        "Pregunta: «¿esto ayuda a leer o solo decora?». Si decora, quítalo.",
    ),
    reinforce="Revisa un afiche de tu casa o calle y di qué formato ayuda a leer.",
    extend="Da formato a una lista de cinco materiales con título y negrita solo en el más importante.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja y lápiz. Imágenes: dibujos propios o descritos. Pantalla ficticia descrita con texto.",
    use="Aprenderé a insertar una imagen en un documento y a anotar su autor. Sirve para ilustrar mi texto respetando a quien la creó.",
    prior=["Sé dar formato a un texto.", "Sé que una imagen propia es la que hice yo."],
    explain=[
        "Insertar es poner una imagen dentro del documento. En el ejemplo ficticio, el botón «insertar imagen» está arriba. Eliges el archivo y la imagen aparece donde está el cursor. Puedes cambiar su tamaño con las esquinas, sin deformarla, y ponerla junto a un párrafo.",
        "Toda imagen tiene un autor. Si la hiciste tú, es propia. Si es de otra persona, debes tener su permiso o una autorización, y anotar su nombre. Esto se llama atribuir. Debajo de la imagen escribe una línea corta: «Imagen: dibujo mío» o «Imagen: de (nombre del autor)». No uses imágenes sin saber quién es el autor.",
        "Elige imágenes que ayuden a entender el texto. Una imagen de una regadera sirve en un texto sobre regar; una que no tiene relación solo distrae. Cuida el tamaño del archivo y los datos personales: no incluyas fotos de otras personas sin permiso.",
    ],
    vocab=[("insertar imagen", "poner una imagen dentro del documento"), ("atribuir", "anotar quién es el autor"), ("pie de imagen", "línea bajo la imagen con su crédito"), ("deformar", "estirar una imagen de modo que se vea torcida")],
    worked=[
        ("Escribir el pie", "Insertaste un dibujo que hiciste tú de una regadera. Escribe el pie de imagen.", ["Digo qué es.", "Digo quién lo hizo.", "Escribo: «Imagen: dibujo mío»."], "Imagen: dibujo mío"),
        ("Elegir la imagen que ayuda", "Tu texto trata de regar plantas. ¿Insertas un dibujo de una regadera o uno de una pelota?", ["La regadera tiene relación.", "La pelota no ayuda."], "El de la regadera"),
    ],
    mistakes=[
        ("Insertar una imagen sin anotar el autor.", "No se respeta a quien la hizo.", "Escribe el crédito en el pie."),
        ("Estirar la imagen de las orillas.", "Se deforma.", "Cambia el tamaño desde la esquina."),
    ],
    R=[
        ("Poner una imagen dentro del documento ¿es insertar o copiar?", "Insertar", "Se ubica en el cursor."),
        ("Anotar el autor de una imagen ¿es atribuir o seleccionar?", "Atribuir", "Se da el crédito."),
        ("La línea bajo la imagen con su crédito ¿es el pie de imagen o el título?", "El pie de imagen", "Va debajo de la imagen."),
    ],
    C=[
        ("¿Por qué se anota el autor de una imagen?", "Para reconocer a quien la creó", "Respeta su trabajo."),
        ("¿Qué imagen es mejor para un texto sobre reciclar cartón: una caja aplastada o un auto?", "Una caja aplastada", "Se relaciona con el tema."),
        ("¿Se cambia el tamaño de la imagen desde las orillas o desde las esquinas?", "Desde las esquinas", "Así no se deforma."),
    ],
    A=[
        ("Insertaste un dibujo de un sol hecho por ti. Escribe el pie de imagen.", "Imagen: dibujo mío", "Indica que es propio."),
        ("Una compañera te autoriza usar su dibujo de un árbol. Se llama Ana. Escribe el pie.", "Imagen: dibujo de Ana", "Da crédito a la autora."),
        arith("Un documento tiene 3 imágenes propias y 2 autorizadas. ¿Cuántas imágenes tiene?", "3+2", "Se suman."),
    ],
    Z=[
        ("Rita insertó una imagen de una persona sin permiso. ¿Qué debió hacer? Responde con una frase.", "Pedir permiso o usar una imagen propia", "Debe haber autorización."),
        ("Dos documentos: A con una imagen sobre el tema y B con una imagen que no tiene que ver. ¿Cuál es mejor?", "A", "Ayuda a entender el texto."),
    ],
    D=[
        ("Reto: describe cómo insertarías un dibujo tuyo de una caja aplastada en un texto sobre reciclar y cómo lo rotulas.", "Poner el cursor, insertar imagen, elegir el archivo, ajustar desde la esquina y escribir: Imagen: dibujo mío", "Pasos y crédito."),
        arith("Tu documento tiene 4 imágenes y quitas 1. ¿Cuántas quedan?", "4-1", "Se resta."),
    ],
    ctx=("Tomás escribe sobre cómo cuidar una planta y quiere insertar su dibujo de una maceta. Escribe qué pasos hace y cuál es el pie de imagen.", "Pone el cursor junto al párrafo, inserta el dibujo, lo ajusta desde la esquina y escribe: Imagen: dibujo mío", "Pasos y pie de imagen."),
    sc=[
        ("¿Se anota el autor de la imagen?", "Sí", "Eso es dar crédito."),
        ("¿La imagen debe tener relación con el texto?", "Sí", "Ayuda a entender."),
        ("¿Se estira la imagen de las orillas?", "No", "La imagen se ve torcida."),
    ],
    open_task=(
        "Escribe un párrafo de dos oraciones sobre cuidar una planta y agrega una imagen: dibuja una regadera o una maceta. Describe cómo la insertarías y escribe el pie de imagen. Si no tienes computador, pégala en una hoja con su pie.",
        "Párrafo: Mi planta necesita agua. La riego con poca agua. Imagen: dibujo de una regadera. Pie: Imagen: dibujo mío.",
        ["escribe el párrafo", "agrega una imagen relacionada", "escribe el pie con el autor", "no usa datos personales"],
        ["párrafo con imagen y pie"],
        ["imagen sin crédito", "imagen sin relación con el texto"],
        "Pregunta: «¿quién hizo esta imagen?». Si no lo sabe, no la uses.",
    ),
    reinforce="Haz un dibujo y escribe su pie con tu crédito.",
    extend="Escribe cómo pedirías permiso para usar el dibujo de otra persona.",
)

# ------------------------------------------------------------------ OA 06, clase 5
reg(
    OA6, 5,
    materials="Hoja y lápiz. Pantalla ficticia descrita con texto; sin computador, usa carpetas de papel con nombres.",
    use="Aprenderé a guardar, cerrar y recuperar un documento con un nombre claro y en una carpeta. Sirve para no perder mi trabajo.",
    prior=["Sé escribir, editar y dar formato a un texto.", "Sé que un archivo es un trabajo guardado con nombre."],
    explain=[
        "Guardar es conservar el trabajo en el dispositivo. Si cierras sin guardar, puedes perderlo. Al guardar por primera vez, eliges tres cosas: un nombre claro, una carpeta y el lugar. Un nombre claro dice de qué trata, por ejemplo «cuidar_planta_texto». Evita nombres como «documento1».",
        "Una carpeta es un lugar para ordenar archivos, como un cajón. En el ejemplo ficticio, el botón «guardar como» abre una ventana: escribes el nombre abajo y eliges la carpeta a la izquierda. Guardar de nuevo mantiene el mismo nombre; guardar como crea una copia con otro nombre. Guarda cada pocos minutos mientras trabajas.",
        "Cerrar es salir del documento. Después se puede abrir: buscas la carpeta, ves el nombre y lo abres de nuevo. Recuperar es volver a encontrar tu trabajo. Si no lo encuentras, mira en las carpetas que usaste. No pongas datos personales en el nombre del archivo.",
    ],
    vocab=[("guardar", "conservar el trabajo en el dispositivo"), ("guardar como", "guardar una copia con otro nombre o lugar"), ("carpeta", "lugar para ordenar archivos"), ("abrir", "traer un archivo guardado a la pantalla"), ("recuperar", "volver a encontrar un trabajo guardado")],
    worked=[
        ("Elegir un nombre claro", "Escribiste un texto sobre cuidar una planta. ¿Qué nombre eliges: «cuidar_planta_texto» o «documento1»?", ["El primero dice de qué trata.", "El segundo no dice nada."], "cuidar_planta_texto"),
        ("Recuperar un archivo", "Guardaste «cuidar_planta_texto» en la carpeta «tecnologia». Mañana quieres abrirlo. ¿Qué haces?", ["Busco la carpeta tecnologia.", "Veo el nombre.", "Lo abro."], "Buscar la carpeta tecnologia y abrir el archivo"),
    ],
    mistakes=[
        ("Cerrar el documento sin guardar.", "Se pierde lo escrito.", "Guarda antes de cerrar."),
        ("Poner el nombre completo de una persona en el archivo.", "Es un dato personal.", "Usa un nombre sobre el tema."),
    ],
    R=[
        ("Conservar el trabajo en el dispositivo ¿es guardar o cerrar?", "Guardar", "Se mantiene el trabajo."),
        ("Un lugar para ordenar archivos ¿es una carpeta o una imagen?", "Una carpeta", "Como un cajón."),
        ("Volver a encontrar un trabajo guardado ¿es recuperar o borrar?", "Recuperar", "Se vuelve a ver."),
    ],
    C=[
        ("¿Por qué se guarda cada pocos minutos?", "Para no perder lo escrito si algo falla", "Se conserva el avance."),
        ("¿Qué nombre es más claro: «reciclaje_carton_texto» o «cosa»?", "reciclaje_carton_texto", "Dice de qué trata."),
        ("¿Guardar como crea una copia con otro nombre?", "Sí", "Es su función."),
    ],
    A=[
        ("Escribiste sobre reciclar cartón. Escribe un nombre de archivo claro.", "reciclaje_carton_texto", "Dice el tema."),
        ("Quieres guardar el archivo en la carpeta «tecnologia». ¿Qué eliges en la ventana de guardar?", "La carpeta tecnologia", "Se elige el lugar."),
        arith("Tienes 3 archivos en una carpeta y guardas 2 más. ¿Cuántos archivos hay?", "3+2", "Se suman."),
    ],
    Z=[
        ("Eli cerró sin guardar y perdió su texto. ¿Qué debió hacer? Responde con una frase.", "Guardar antes de cerrar", "Así se conserva el trabajo."),
        ("Dos nombres: A «Maria_Gonzalez_direccion» y B «cuidar_planta_texto». ¿Cuál es mejor para proteger los datos?", "B", "No lleva datos personales."),
    ],
    D=[
        ("Reto: escribe los pasos para guardar un texto por primera vez: guardar como, nombre, carpeta, guardar.", "Guardar como; escribir el nombre; elegir la carpeta; guardar", "Pasos en orden."),
        arith("Tienes 8 archivos y borras 3 que no sirven. ¿Cuántos archivos quedan?", "8-3", "Se resta."),
    ],
    ctx=("Valentina escribió un texto sobre su portalápices. Debe guardarlo, cerrarlo y abrirlo mañana. Escribe un nombre claro, la carpeta y cómo lo recuperará.", "Nombre: portalapices_texto; carpeta: tecnologia; mañana abre la carpeta y el archivo", "Nombre, carpeta y recuperación."),
    sc=[
        ("¿Se guarda antes de cerrar?", "Sí", "Para no perder el trabajo."),
        ("¿El nombre debe decir de qué trata?", "Sí", "Así se encuentra."),
        ("¿Se usan datos personales en el nombre?", "No", "Hay que protegerlos."),
    ],
    open_task=(
        "Usa este caso: escribiste un texto sobre cuidar una planta. Escribe el nombre del archivo, la carpeta donde lo guardas, los pasos para guardar y cerrar, y los pasos para abrirlo mañana. Si no tienes computador, usa una carpeta de papel y una hoja.",
        "Nombre: cuidar_planta_texto; carpeta: tecnologia. Pasos: guardar como, nombre, carpeta, guardar, cerrar. Mañana: abrir la carpeta y el archivo.",
        ["nombre claro sin datos personales", "elige una carpeta", "describe cómo guardar", "describe cómo recuperar"],
        ["nombre, carpeta y pasos"],
        ["nombres vagos", "cerrar sin guardar"],
        "Pregunta: «¿cómo lo encontrarás mañana?». Si no sabe, ayúdale con la carpeta y el nombre.",
    ),
    reinforce="Pon nombres claros a tres papeles de tu mochila y guárdalos en una carpeta.",
    extend="Escribe una regla de tres frases para nombrar archivos.",
)

# ------------------------------------------------------------------ OA 07, clase 1
reg(
    OA7, 1,
    materials="Hoja y lápiz. Las pantallas de buscador son un ejemplo ficticio descrito con palabras; no se usa ninguna dirección real. Sin computador, se simula en papel.",
    use="Aprenderé a escribir una búsqueda específica con palabras clave. Sirve para encontrar información útil rápido.",
    prior=["Sé qué es un tema.", "Sé escribir palabras sin errores."],
    explain=[
        "Internet es una red que conecta computadores de todo el mundo. Un buscador es un programa de internet que busca páginas según las palabras que escribes en una caja. Esas palabras son las palabras clave. Una buena búsqueda usa pocas palabras, las más importantes del tema. En el ejemplo ficticio, la caja está arriba y debajo aparece la lista de resultados.",
        "Una búsqueda vaga como «plantas» da miles de resultados. Una específica como «cuánta agua necesita una planta de interior» da resultados más útiles. Para hacerla específica, piensa en qué quieres saber: qué, quién, cuánto o cómo. Quita palabras que no ayudan, como «por favor» o «quiero saber».",
        "Cuida tu seguridad: nunca escribas en la caja tus datos personales, como tu nombre completo, tu dirección o tu teléfono. Busca siempre con ayuda de una persona adulta cercana. Si no tienes internet, simula la búsqueda en papel con los resultados del cuaderno.",
    ],
    vocab=[("buscador", "programa de internet que busca páginas según las palabras que escribes"), ("palabra clave", "palabra importante del tema"), ("búsqueda específica", "búsqueda con palabras que dicen exactamente lo que quieres saber"), ("resultado", "página que aparece como respuesta a la búsqueda")],
    worked=[
        ("Elegir palabras clave", "Quieres saber cuánta agua necesita una planta. ¿Qué palabras clave eliges?", ["Lo importante es planta y agua.", "También cuánta."], "cuánta agua necesita una planta"),
        ("Hacer específica una búsqueda", "La búsqueda «plantas» es muy vaga. Mejórala para saber cómo regar una planta de interior.", ["Digo qué quiero saber: cómo regar.", "Agrego planta de interior."], "cómo regar una planta de interior"),
    ],
    mistakes=[
        ("Escribir una sola palabra como «plantas».", "Da demasiados resultados.", "Agrega lo que quieres saber."),
        ("Escribir datos personales en la caja.", "No es seguro.", "Usa solo palabras del tema."),
    ],
    R=[
        ("El programa de internet que busca páginas ¿es un buscador o un procesador de textos?", "Un buscador", "Busca por palabras."),
        ("Una palabra importante del tema ¿es una palabra clave o un resultado?", "Una palabra clave", "Resume el tema."),
        ("¿Se escribe la dirección de tu casa en el buscador?", "No", "Es un dato personal."),
    ],
    C=[
        ("¿Por qué «plantas» es una búsqueda vaga?", "Porque no dice qué quieres saber", "Da demasiados resultados."),
        ("¿Es mejor una búsqueda con pocas palabras importantes o con una frase muy larga?", "Pocas palabras importantes", "Es más claro."),
        ("¿Con quién buscas en internet a tu edad?", "Con una persona adulta cerca", "Es más seguro."),
    ],
    A=[
        ("Quieres saber cómo reciclar cartón. Escribe una búsqueda específica.", "cómo reciclar cartón en casa", "Dice el tema y lo que quieres."),
        ("Escribes «por favor quiero saber cuántas horas de luz necesita una planta». ¿Qué palabras sobran?", "Por favor quiero saber", "No ayudan a buscar."),
        arith("Una búsqueda vaga da 1000 resultados y una específica da 50. ¿Cuántos resultados menos da la específica?", "1000-50", "Se resta."),
    ],
    Z=[
        ("Pablo busca «tijeras». Quiere saber cómo cortar cartón con seguridad. ¿Qué le falta? Responde con una frase.", "Agregar lo que quiere saber: cómo cortar cartón con seguridad", "La búsqueda es vaga."),
        ("Dos búsquedas: A «ayuda» y B «cómo plegar papel». ¿Cuál es más específica?", "B", "Dice qué quiere hacer."),
    ],
    D=[
        ("Reto: quieres saber qué materiales se pueden reutilizar para un portalápices. Escribe una búsqueda y dos palabras clave.", "materiales reutilizables para un portalápices; palabras clave: materiales, portalápices", "Búsqueda con palabras importantes."),
        arith("Haces 3 búsquedas y cada una da 20 resultados. ¿Cuántos resultados son en total?", "3*20", "Se multiplica."),
    ],
    ctx=("Rafa quiere saber cuántas veces regar un cactus. Puede buscar «cactus» o «cada cuánto regar un cactus». Elige la mejor búsqueda y di por qué.", "Cada cuánto regar un cactus, porque dice lo que quiere saber", "Es una búsqueda específica."),
    sc=[
        ("¿Se usan palabras clave?", "Sí", "Resumen del tema."),
        ("¿La búsqueda específica da resultados más útiles?", "Sí", "Dice lo que quieres."),
        ("¿Se buscan datos personales?", "No", "Hay que protegerlos."),
    ],
    open_task=(
        "Escoge una pregunta. Pregunta 1: ¿cada cuánto se riega una planta de interior? Pregunta 2: ¿cómo se recicla el cartón? Escribe una búsqueda vaga, una específica y las palabras clave que usarías. Si no tienes internet, simula la búsqueda en papel.",
        "Pregunta 1: vaga: plantas. Específica: cada cuánto regar una planta de interior. Palabras clave: regar, planta, interior.",
        ["escribe una búsqueda vaga y una específica", "elige palabras clave", "no usa datos personales"],
        ["búsquedas y palabras clave"],
        ["una sola palabra", "datos personales"],
        "Pregunta: «¿qué quieres saber exactamente?». Úsalo para armar la búsqueda.",
    ),
    reinforce="Escribe tres búsquedas específicas sobre un tema que te guste.",
    extend="Reescribe cinco búsquedas vagas para que sean específicas.",
)

# ------------------------------------------------------------------ OA 07, clase 2
reg(
    OA7, 2,
    materials="Hoja y lápiz. La lista de resultados está escrita en el cuaderno como ejemplo ficticio con direcciones inventadas.",
    use="Aprenderé a leer los resultados antes de abrirlos: título, dirección y resumen. Sirve para elegir bien y evitar páginas que no sirven o no son seguras.",
    prior=["Sé escribir una búsqueda específica.", "Sé que un resultado es una página que aparece en la lista."],
    explain=[
        "Un buscador muestra una lista de resultados. Cada resultado tiene tres partes: el título, la dirección y un resumen corto. Antes de abrir uno, léelas. El título dice de qué trata. La dirección es el nombre de la página en internet. El resumen cuenta un poco de lo que hay.",
        "Compara el título y el resumen con lo que buscas. Si dicen cosas distintas, no lo abras. Mira también si la dirección parece de una escuela, un museo o una institución conocida, o si está llena de números y símbolos raros. Desconfía de resultados que prometen premios, regalos o que piden datos.",
        "Los resultados marcados como anuncios sirven para vender cosas; no son la respuesta. No abras un resultado solo porque está primero. Elige el que mejor responde a tu pregunta. En esta clase todos los resultados son un ejemplo ficticio y las direcciones están inventadas.",
    ],
    vocab=[("título", "nombre del resultado que dice de qué trata"), ("dirección", "nombre de la página en internet"), ("resumen", "texto corto que cuenta qué hay en la página"), ("anuncio", "resultado hecho para vender algo")],
    worked=[
        ("Elegir un resultado", "Buscas «cada cuánto regar una planta de interior». Resultado A: «Regar plantas de interior: guía de cuidados» (dirección: plantas-cuidado.ejemplo). Resultado B: «¡Gana un premio ahora!» (dirección: premios-123.ejemplo). ¿Cuál abres?", ["A coincide con lo que busco.", "B habla de premios, no de plantas."], "El A"),
        ("Detectar un anuncio", "Un resultado dice «Anuncio: compra macetas ahora». ¿Es una respuesta o es para vender?", ["Dice Anuncio.", "Su fin es vender."], "Es para vender"),
    ],
    mistakes=[
        ("Abrir el primer resultado sin leer.", "Puede no responder tu pregunta.", "Lee el título, la dirección y el resumen."),
        ("Abrir un resultado que promete premios.", "Puede ser engañoso o peligroso.", "No lo abras y avisa a una persona adulta."),
    ],
    R=[
        ("El nombre de la página en internet ¿es la dirección o el resumen?", "La dirección", "Identifica la página."),
        ("Un resultado hecho para vender ¿es un anuncio o un título?", "Un anuncio", "Sirve para vender."),
        ("¿Se lee el resumen antes o después de abrir?", "Antes", "Así eliges mejor."),
    ],
    C=[
        ("¿Por qué no se abre un resultado solo por estar primero?", "Porque puede no responder lo que buscas", "El orden no asegura que sirva."),
        ("¿Qué haces si un resultado promete un premio gratis?", "No lo abres y avisas a un adulto", "Puede ser engañoso."),
        ("Si el título y el resumen no coinciden con tu pregunta, ¿lo abres?", "No", "No responde lo que buscas."),
    ],
    A=[
        ("Buscas cómo reciclar cartón. Resultado A: «Cómo reciclar cartón en casa» (reciclaje-casa.ejemplo). Resultado B: «Juegos gratis sin límite» (juegos-gratis.ejemplo). ¿Cuál abres?", "El A", "Su título coincide con lo que buscas."),
        ("Un resultado dice «Anuncio». ¿Lo tomas como respuesta o como venta?", "Como venta", "Los anuncios venden."),
        arith("La lista tiene 10 resultados y 3 son anuncios. ¿Cuántos no son anuncios?", "10-3", "Se resta."),
    ],
    Z=[
        ("Dani abrió un resultado que decía «Gana un regalo» y le pidió su dirección. ¿Qué debe hacer ahora? Responde con una frase.", "Cerrar la página y avisar a un adulto", "Pide datos y puede ser engañoso."),
        ("Dos resultados sobre un tema de ciencias: A tiene título claro y resumen que responde; B tiene muchas mayúsculas y signos. ¿Cuál es mejor?", "A", "Parece más claro y serio."),
    ],
    D=[
        ("Reto: lee estos dos resultados sobre «cuidar un cactus»: A «Cuidados del cactus» y B «Compra ya, descuento». Explica cuál abres y por qué.", "A, porque responde a la búsqueda y B vende", "Elige con razón."),
        arith("Revisas 6 resultados y abres 2. ¿Cuántos no abres?", "6-2", "Se resta."),
    ],
    ctx=("Mía buscó «cómo cortar cartón con seguridad». Ve tres resultados: A «Consejos para cortar cartón con seguridad» (cortar-carton.ejemplo), B «Tijeras en oferta» (anuncio) y C «Gana un premio» (premios.ejemplo). Elige uno y di por qué.", "A, porque el título responde a su pregunta y B y C son venta o engaño", "Elige con razón."),
    sc=[
        ("¿Se lee antes de abrir?", "Sí", "Para elegir bien."),
        ("¿Un anuncio es una respuesta?", "No", "Su fin es vender."),
        ("¿Se abren resultados que prometen premios?", "No", "Pueden ser engañosos."),
    ],
    open_task=(
        "Usa esta lista para la búsqueda «cada cuánto regar un cactus». A: «Regar un cactus: guía» (cactus-guia.ejemplo, resumen: explica cada cuánto regar). B: «Anuncio: compra tu cactus» (cactus-tienda.ejemplo). C: «Gana un premio gratis ya» (premio-rapido.ejemplo). Elige cuál abres, di por qué, y explica qué haces con los demás.",
        "Abro A porque coincide con mi pregunta. B es anuncio; C promete un premio, no lo abro.",
        ["elige el resultado correcto", "da una razón", "explica qué hace con los otros"],
        ["elección con razones"],
        ["abrir el primero", "abrir el que promete un premio"],
        "Pregunta: «¿qué dice el título y qué buscabas?». Si no coinciden, no lo abre.",
    ),
    reinforce="Mira una lista de resultados con una persona adulta y señala cuál responde mejor.",
    extend="Escribe tres señales de que un resultado puede no ser seguro.",
)

# ------------------------------------------------------------------ OA 07, clase 3
reg(
    OA7, 3,
    materials="Hoja y lápiz. Las páginas de ejemplo están descritas en el cuaderno con datos inventados.",
    use="Aprenderé a evaluar si una fuente es confiable y segura con señales simples. Sirve para no creer cualquier cosa ni dar datos a quien no corresponde.",
    prior=["Sé leer los resultados antes de abrir.", "Sé que no se dan datos personales en internet."],
    explain=[
        "Una fuente es el lugar de donde viene la información, como una página, un libro o una persona. Una fuente confiable es la que podemos creer con buenas razones. Aquí usamos señales simples; es una simplificación, porque juzgar una fuente en la vida real es más complejo y a veces necesita la ayuda de una persona adulta.",
        "Señales de una fuente confiable: dice quién la escribió o qué institución la publica; tiene una fecha actual; los datos coinciden con otras fuentes; no te pide datos personales; tiene pocos anuncios y no promete premios. Señales de alerta: promete regalos, usa muchas mayúsculas y signos, te pide dirección o contraseña, o abre ventanas sin que las pidas.",
        "Para estar más seguro, compara dos o tres fuentes. Si dicen lo mismo, la información es más confiable. Si una página te pide datos o hace sentir miedo, ciérrala y avisa a una persona adulta. Nunca des contraseñas ni datos personales.",
    ],
    vocab=[("fuente", "lugar de donde viene la información"), ("fuente confiable", "fuente que podemos creer con buenas razones"), ("señal de alerta", "rasgo que avisa un posible peligro o engaño"), ("contraseña", "clave secreta que no se comparte"), ("comparar fuentes", "mirar si varias fuentes dicen lo mismo")],
    worked=[
        ("Revisar una fuente", "Una página dice: autor: Museo de Ciencias del Barrio (ficticio), fecha: este año, sin anuncios, explica cómo regar plantas. ¿Es confiable según las señales?", ["Dice quién la escribe.", "Tiene fecha actual.", "No tiene anuncios."], "Sí, cumple las señales"),
        ("Detectar alerta", "Una página dice: «¡Gana un regalo! Escribe tu dirección». ¿Qué haces?", ["Pide datos y promete un regalo.", "Son señales de alerta."], "Cierro la página y aviso a un adulto"),
    ],
    mistakes=[
        ("Creer una página solo porque se ve bonita.", "Lo bonito no asegura que sea verdad.", "Revisa autor, fecha y datos."),
        ("Dar datos personales a una página que los pide.", "Puede ser engañosa.", "No des datos; avisa a un adulto."),
    ],
    R=[
        ("Lugar de donde viene la información ¿es una fuente o una carpeta?", "Una fuente", "Es de donde sale el dato."),
        ("«Gana un regalo» ¿es una señal de alerta o de confianza?", "Señal de alerta", "Es un posible engaño."),
        ("¿Se comparte una contraseña con una página?", "No", "Es una clave secreta."),
    ],
    C=[
        ("¿Por qué conviene comparar dos o tres fuentes?", "Para ver si dicen lo mismo", "Si coinciden, es más confiable."),
        ("¿Qué dato de una página ayuda a confiar: que diga quién la escribió o que use muchos colores?", "Que diga quién la escribió", "Se sabe a quién creer."),
        ("Esto es una simplificación: ¿juzgar fuentes en la vida real es más fácil o más complejo?", "Más complejo", "Requiere más cuidado."),
    ],
    A=[
        ("Página A: autor claro, fecha actual, sin anuncios. Página B: sin autor, con anuncios y premios. ¿Cuál es más confiable?", "A", "Cumple más señales."),
        ("Una página pide tu contraseña para mostrarte un dibujo. ¿La das?", "No", "Nunca se da."),
        arith("Una fuente cumple 4 de 5 señales de confianza. ¿Cuántas no cumple?", "5-4", "Se resta."),
    ],
    Z=[
        ("Dos páginas dicen cosas distintas sobre cuánto regar un cactus. ¿Qué haces? Responde con una frase.", "Comparo con otra fuente y pido ayuda a un adulto", "Se necesita otra fuente para decidir."),
        ("Lía confió en una página con muchas imágenes y sin autor. ¿Qué señal le faltó mirar?", "Quién la escribió", "El autor da respaldo."),
    ],
    D=[
        ("Reto: escribe tres señales de una fuente confiable y dos de alerta.", "Confiable: autor claro, fecha actual, sin pedir datos. Alerta: promete regalos, pide contraseña", "Son cinco señales distintas."),
        arith("Tres fuentes dicen lo mismo y una dice otra cosa. ¿Cuántas fuentes comparaste?", "3+1", "Se suman."),
    ],
    ctx=("Camilo busca cuántas horas de luz necesita una planta. Página A: la escribe un colegio, tiene fecha de este año y no pide datos. Página B: dice «¡Premios!» y pide su dirección. Elige y explica con dos señales.", "Página A, porque dice quién la escribe, tiene fecha y no pide datos; B promete premios y pide dirección", "Elige con señales."),
    sc=[
        ("¿Una página que pide contraseña es de fiar?", "No", "Nunca se da."),
        ("¿Se comparan fuentes?", "Sí", "Si coinciden, es mejor."),
        ("¿Esto es una simplificación?", "Sí", "La realidad es más compleja."),
    ],
    open_task=(
        "Usa este caso: buscas «cómo cuidar un cactus». Página A: autor un colegio, fecha de este año, sin anuncios, explica cuidados. Página B: sin autor, muchos anuncios, promete premios y pide tu dirección. Haz una tabla con las señales de cada una y decide cuál usar. Escribe qué harías con la otra.",
        "A: autor sí, fecha sí, sin anuncios. B: sin autor, anuncios, premios. Uso A; cierro B y aviso a un adulto.",
        ["revisa autor, fecha, anuncios y datos", "decide con razones", "dice qué hace con la otra"],
        ["tabla de señales y decisión"],
        ["dar datos personales", "elegir por apariencia"],
        "Pregunta: «¿quién la escribió y qué te pide?». Si no se sabe, pide ayuda.",
    ),
    reinforce="Con un adulto, mira una página y busca quién la escribió y la fecha.",
    extend="Escribe una lista de cinco reglas para navegar con seguridad.",
)

# ------------------------------------------------------------------ OA 07, clase 4
reg(
    OA7, 4,
    materials="Hoja y lápiz. El texto de ejemplo está en el cuaderno, con datos inventados.",
    use="Aprenderé a sacar información, anotar de dónde viene y guardarla en una carpeta. Sirve para usarla después sin copiar y respetando al autor.",
    prior=["Sé buscar y evaluar una fuente.", "Sé guardar un archivo con nombre en una carpeta."],
    explain=[
        "El texto «Guía del cactus» de esta clase es un insumo ficticio, inventado para practicar: no es un consejo real de riego, porque cada planta y cada estación piden cuidados distintos. Extraer es sacar de un texto las ideas que sirven. No copies todo: lee, entiende y escribe con tus palabras. Una nota breve tiene la idea principal y un dato. Por ejemplo: «Un portalápices de cartón se arma con tres piezas». Si necesitas la frase exacta, ponla entre comillas.",
        "Atribuir es anotar de dónde viene la información: el nombre de la página o de quien la escribió, y la fecha. Así otras personas pueden revisar y respetas al autor. Una ficha de fuente dice: tema, nota, fuente y fecha. Esto se llama citar la fuente.",
        "Almacenar es guardar la información. Puedes escribir las notas en un documento y guardarlo en una carpeta con nombre claro, como «cactus_notas». También puedes anotar en una hoja. Guarda solo lo que sirve, sin datos personales. Revisa que lo guardado tenga la fuente anotada.",
    ],
    vocab=[("extraer", "sacar las ideas que sirven de un texto"), ("con tus palabras", "explicar la idea sin copiarla"), ("atribuir", "anotar de dónde viene la información"), ("almacenar", "guardar la información"), ("cita", "frase exacta copiada y puesta entre comillas")],
    worked=[
        ("Escribir una nota", "Texto ficticio: «El cactus guarda agua en su tallo y por eso necesita regarse poco, más o menos cada dos semanas». Escribe una nota con tus palabras.", ["Saco la idea principal.", "La digo corta."], "El cactus guarda agua y se riega poco, cada dos semanas"),
        ("Anotar la fuente", "La nota viene de la página ficticia «Guía del cactus», publicada este año. Escribe la fuente.", ["Digo el nombre de la página.", "Agrego la fecha."], "Fuente: Guía del cactus, este año"),
    ],
    mistakes=[
        ("Copiar el texto entero.", "No muestra que entendiste y es copiar el trabajo de otro.", "Escribe la idea con tus palabras."),
        ("Guardar la nota sin la fuente.", "No se sabe de dónde vino.", "Anota siempre la fuente."),
    ],
    R=[
        ("Sacar las ideas que sirven de un texto ¿es extraer o borrar?", "Extraer", "Es sacar lo importante."),
        ("Anotar de dónde viene la información ¿es atribuir o seleccionar?", "Atribuir", "Se da el crédito."),
        ("Guardar la información ¿es almacenar o buscar?", "Almacenar", "Así se conserva el trabajo."),
    ],
    C=[
        ("¿Por qué se escribe la idea con tus palabras?", "Para mostrar que la entendiste", "Copiar no prueba que entiendes."),
        ("¿Qué dos datos lleva la fuente?", "El nombre de la página o autor y la fecha", "Así otros pueden revisarla."),
        ("¿Dónde guardas tus notas: en una carpeta con nombre claro o suelta?", "En una carpeta con nombre claro", "Así las encuentras."),
    ],
    A=[
        ("Texto ficticio: «Las plantas necesitan luz para crecer; las de interior se ubican cerca de una ventana». Escribe una nota con tus palabras.", "Las plantas necesitan luz, así que se ponen cerca de la ventana", "Resume la idea."),
        ("La nota viene de la página «Cuidados de plantas», publicada este año. Escribe la ficha de fuente.", "Fuente: Cuidados de plantas, este año", "Nombre y fecha."),
        arith("Tienes 3 notas con fuente y escribes 2 más. ¿Cuántas notas tienes?", "3+2", "Se suman."),
    ],
    Z=[
        ("Rita copió un párrafo entero y no anotó la fuente. ¿Qué dos errores cometió? Responde con una frase.", "Copió todo y no dio crédito", "Falta resumir y atribuir."),
        ("Dos notas: A «Cactus: se riega cada dos semanas» (Fuente: Guía del cactus, página ficticia) y B «Cactus: poca agua». ¿Cuál es mejor?", "A", "Tiene dato y fuente."),
    ],
    D=[
        ("Reto: lee este texto ficticio: «El cartón se puede reciclar varias veces y debe estar limpio y seco». Escribe una nota con tus palabras y su fuente: página «Reciclaje en casa», este año.", "El cartón limpio y seco se recicla varias veces. Fuente: Reciclaje en casa, este año", "Nota con fuente."),
        arith("Guardas 4 notas en una carpeta y 3 en otra. ¿Cuántas notas guardaste?", "4+3", "Se suman."),
    ],
    ctx=("Mateo investigó sobre el cactus y encontró «El cactus necesita mucha luz y poca agua». La fuente es la página ficticia «Guía del cactus», este año (todo es un ejemplo inventado). Escribe su nota, la fuente y el nombre del archivo donde la guarda.", "Nota: el cactus necesita luz y poca agua. Fuente: Guía del cactus, este año. Archivo: cactus_notas", "Nota, fuente y archivo."),
    sc=[
        ("¿Se copia todo el texto?", "No", "Se escribe con tus palabras."),
        ("¿Se anota la fuente?", "Sí", "Eso es dar crédito."),
        ("¿Se guarda con nombre claro?", "Sí", "Así la puedes encontrar."),
    ],
    open_task=(
        "Usa este texto, un insumo ficticio inventado para practicar (no es un consejo real de riego), de una página ficticia llamada «Guía del cactus», de este año: «El cactus guarda agua en su tallo. Por eso se riega cada dos semanas y necesita mucha luz». Escribe dos notas con tus palabras, la ficha de fuente y el nombre del archivo y la carpeta donde guardarías las notas. Si no tienes computador, usa una hoja y una carpeta de papel.",
        "Notas: se riega cada dos semanas; necesita mucha luz. Fuente: Guía del cactus, este año. Archivo: cactus_notas. Carpeta: tecnologia.",
        ["escribe dos notas con sus palabras", "anota la fuente con fecha", "elige nombre de archivo y carpeta", "no copia todo"],
        ["notas, fuente y archivo"],
        ["copiar todo", "no anotar la fuente"],
        "Pregunta: «¿dónde lo leíste y cuándo?». Si no lo sabe, falta la fuente.",
    ),
    reinforce="Lee un párrafo de un libro y escríbelo en una línea con tus palabras.",
    extend="Crea una ficha con tema, nota, fuente y fecha para tres datos sobre una planta.",
)
