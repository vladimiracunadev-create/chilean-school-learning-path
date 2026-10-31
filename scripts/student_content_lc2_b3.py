"""Cuaderno del estudiante, 2.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF03 (interacción con textos escritos en lengua indígena) y OA LF04 (escritura inicial).

Los textos de práctica están en castellano, son inventados y no pertenecen a ningún pueblo. Solo
se usan las palabras de mapuzugun muy conocidas «mari mari», «mapu», «ko», «antü» y «kuyen», con la
indicación de que la escritura, la pronunciación y el uso los confirma el educador/a tradicional o
la comunidad. No se inventa ortografía, gramática ni vocabulario de ninguna lengua indígena.
"""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


LF03 = "LC02 OA LF03"
LF04 = "LC02 OA LF04"

CARTEL = "«Mari mari. Bienvenidos a la biblioteca. Aquí puedes leer cuentos. Cuida los libros y habla en voz baja.»"
CUENTO = ("Título: «La niña y el río». Imagen: una niña sentada junto a un río, con un cerro verde al fondo. "
          "Texto: «Rosa llega al río cada tarde. Escucha el agua y mira el cerro. Después vuelve a casa contenta.»")

# ================================================================ LF03
register(
    LF03, 1,
    materials="Este cuaderno y lápiz. Los textos de práctica están escritos aquí en castellano. Los textos de un pueblo los entrega su educador/a tradicional o su comunidad.",
    use="Aprenderé a reconocer quién escribió un texto, para qué y dónde se usa. Sirve para leer con respeto los textos escritos en lenguas indígenas o sobre ellas.",
    prior=["Sé leer frases cortas.", "Sé qué es una fuente."],
    explain=[
        "Un texto escrito puede ser un cartel, una etiqueta de museo, un cuento, un afiche o una invitación. Cada texto tiene una voz, que es quien lo escribe; un propósito, que es para qué se escribe; y un contexto, que es dónde se lee. Por ejemplo, un cartel de biblioteca se escribe para dar un aviso y se lee en la entrada.",
        "Algunos textos están escritos en una lengua indígena o en dos lenguas a la vez. Un texto en dos lenguas se llama bilingüe. Por ejemplo, un cartel puede decir «Mari mari» y debajo «Bienvenidos». «Mari mari» es un saludo en mapuzugun. Aunque no sepas leer todo, puedes fijarte en las imágenes y en las palabras que conoces.",
        "Para saber si un texto es confiable, mira quién lo hizo. Un texto con autoría clara hecho por la comunidad o con su permiso es una fuente validada. Un texto sin autor ni lugar no sirve para aprender, porque no sabes si dice la verdad. Si tienes dudas, pregunta al educador o educadora tradicional.",
    ],
    vocab=[("texto bilingüe", "texto escrito en dos lenguas"), ("voz", "quien escribe un texto"), ("propósito", "para qué se escribe"), ("contexto", "dónde se lee un texto"), ("autoría", "quién creó un texto")],
    worked=[
        {"title": "Voz, propósito y contexto", "problem": f"Lees este cartel de práctica: {CARTEL} Está pegado en la puerta de la biblioteca. ¿Cuál es el propósito y el contexto?", "steps": ["Dice bienvenida y pide cuidar los libros.", "Su propósito es dar la bienvenida y avisar cómo cuidar.", "Se lee en la puerta de la biblioteca."], "answer": "Propósito: dar la bienvenida y pedir cuidado; contexto: la puerta de la biblioteca"},
        {"title": "Fuente validada", "problem": "Encuentras dos textos: A) un afiche sin autor ni fecha y B) un folleto hecho por una comunidad con su nombre y su permiso. ¿Cuál es mejor fuente?", "steps": ["El A no dice quién lo hizo.", "El B dice quién lo hizo y tiene permiso.", "El B es una fuente validada."], "answer": "El folleto B"},
    ],
    mistakes=[
        {"wrong": "Creer que todo texto con una palabra indígena es una buena fuente.", "why": "Hay textos sin autoría o hechos sin permiso.", "fix": "Revisa quién lo hizo y si tiene permiso de la comunidad."},
        {"wrong": "No leer el contexto y pensar que un cartel dice lo mismo en cualquier lugar.", "why": "El lugar cambia el sentido de un aviso.", "fix": "Pregunta dónde se usa antes de interpretarlo."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál de estos es un texto escrito: un cartel, un silbido o un baile?", "Un cartel", "El cartel se lee escrito."),
            ex("Un texto bilingüe está escrito en dos lenguas. Si un cartel dice «Mari mari» y «Bienvenidos», ¿es bilingüe?", "Sí", "Tiene dos lenguas: mapuzugun y castellano."),
            ex("La voz de un texto es quien lo escribe. Si lo escribió una profesora, ¿quién es la voz?", "La profesora", "Ella lo escribió."),
        ],
        "understand": [
            ex("Un cartel dice «Cuida los libros». ¿Cuál es su propósito: avisar cómo cuidar o contar un cuento?", "Avisar cómo cuidar", "Es un aviso."),
            ex("Un cartel se lee en la entrada de una escuela. ¿Eso es el contexto o la voz?", "El contexto", "Dice dónde se lee."),
            ex("¿Qué es mejor fuente: un texto sin autor ni lugar, o un texto hecho por una comunidad con su nombre?", "Un texto hecho por una comunidad con su nombre", "Dice quién lo hizo y se puede confiar."),
        ],
        "apply": [
            ex(f"Lee: {CARTEL} ¿Cuál es el saludo del cartel?", "Mari mari", "Es lo primero que dice."),
            ex(f"En el cartel de la biblioteca, ¿cuántas cosas pide? Lee: {CARTEL}", "2", "Pide cuidar los libros y hablar en voz baja."),
            ex("Tres textos: A) una receta, B) una invitación a una feria con la firma de una comunidad, C) un afiche sin autor. ¿Cuál tiene autoría clara de una comunidad?", "B", "Tiene la firma de una comunidad."),
        ],
        "reason": [
            ex("Un niño dice que un afiche sin autor es buena fuente porque es bonito. ¿Por qué se equivoca?", "Porque no dice quién lo hizo", "Sin autoría no se sabe si dice la verdad."),
            ex("Un cartel que dice «Silencio» es igual en una biblioteca y en un estadio. ¿Su sentido cambia por el contexto?", "Sí", "En la biblioteca es habitual; en un estadio no."),
        ],
        "challenge": [
            ex("Mira esta ficha de un libro inventado: «Título: Cuentos del río. Autoría: no hay. Lugar: no hay. Año: no hay». ¿Es una fuente validada? Explica en pocas palabras.", "No, porque no tiene autoría, lugar ni año", "Faltan los datos que muestran de dónde viene."),
            ex("Un museo escribe: «Mari mari. Esta sala muestra textiles». Escribe la voz, el propósito y el contexto.", "Voz: el museo; propósito: dar la bienvenida y presentar la sala; contexto: la sala de textiles", "Dice quién escribe, para qué y dónde."),
        ],
    },
    context=[ex("En un negocio ves un cartel con una palabra en lengua indígena y no sabes quién lo hizo. ¿Qué haces antes de aprender de él?", "Pregunto quién lo hizo", "Hay que ver si tiene autoría.")],
    selfcheck=[
        ex("¿Qué es un texto bilingüe?", "Un texto en dos lenguas", "Tiene dos lenguas."),
        ex("¿Qué es el contexto de un texto?", "Dónde se lee", "Es el lugar."),
        ex("¿Qué haces si un texto no tiene autoría?", "No lo uso como fuente", "No se sabe de dónde viene."),
    ],
    open_task=task(
        f"Lee este cartel de práctica: {CARTEL}. Escribe tres líneas: 1) Voz (quién podría haberlo escrito), 2) Propósito (para qué se escribió) y 3) Contexto (dónde estaría pegado). Después anota una pregunta que le harías a un educador tradicional sobre cómo se pronuncia «Mari mari».",
        "1) Voz: el personal de la biblioteca. 2) Propósito: dar la bienvenida y pedir cuidado. 3) Contexto: la entrada de la biblioteca. Pregunta: ¿cómo se pronuncia «mari mari»?",
        ["escribe voz, propósito y contexto", "las respuestas coinciden con el cartel", "escribe una pregunta sobre la pronunciación"],
        ["tres líneas", "pregunta"],
        ["inventar una traducción del saludo", "decir que el cartel es de un pueblo"],
        "Reconoce que usó solo el cartel para responder. Recuérdale que la pronunciación la enseña el educador tradicional.",
    ),
    reinforce="Mira un cartel de tu barrio y anota quién lo hizo y para qué.",
    extend="Busca en casa un texto con dos lenguas, como una etiqueta, y compara qué dice en cada una.",
)

register(
    LF03, 2,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a sacar información de un texto escrito usando el título, la imagen y el texto. Sirve para comprender lo que dice un texto sin necesidad de traducir palabra por palabra.",
    prior=["Sé reconocer voz, propósito y contexto.", "Sé leer frases cortas."],
    explain=[
        "Los textos escritos suelen tener un título, una imagen y un texto. El título dice de qué trata. La imagen muestra lo que sucede. El texto cuenta los detalles. Si juntas las tres cosas, comprendes mejor aunque haya palabras que no conoces. A esto se le llama usar pistas.",
        "El tema es de qué trata un texto. La información son los datos que el texto da, como quién, dónde y qué pasa. Para hallarlos, hazte preguntas: ¿quién aparece?, ¿dónde está?, ¿qué hace? Responde con lo que ves en el texto y en la imagen, no con lo que imaginas.",
        "En un texto en dos lenguas, no es necesario traducir palabra por palabra. Si una parte está en una lengua indígena y otra en castellano, usa la parte en castellano y la imagen como apoyo. Para saber el significado exacto de la palabra indígena, pregunta al educador o educadora tradicional.",
    ],
    vocab=[("título", "nombre del texto"), ("imagen", "dibujo o foto que acompaña un texto"), ("tema", "de qué trata un texto"), ("información", "datos que da un texto"), ("pista", "algo que ayuda a comprender")],
    worked=[
        {"title": "Título, imagen y texto", "problem": f"Mira este texto: {CUENTO} ¿Cuál es el tema y qué hace Rosa?", "steps": ["El título dice «La niña y el río».", "La imagen muestra una niña junto a un río.", "El texto dice que Rosa escucha el agua, mira el cerro y vuelve a casa."], "answer": "Tema: una niña y el río; Rosa escucha el agua, mira el cerro y vuelve a casa"},
        {"title": "Usar pistas", "problem": "Un cartel dice «Cuidemos el agua» y tiene una imagen de una llave cerrada. ¿Qué te pide?", "steps": ["El título habla de cuidar el agua.", "La imagen muestra una llave cerrada.", "Me pide cerrar la llave para no gastar agua."], "answer": "Cerrar la llave para cuidar el agua"},
    ],
    mistakes=[
        {"wrong": "Responder con lo que imaginas y no con lo que dice el texto.", "why": "Se pierde la información del texto.", "fix": "Busca la respuesta en el título, la imagen o el texto."},
        {"wrong": "Querer traducir cada palabra antes de comprender el tema.", "why": "Las lenguas dicen las ideas de maneras distintas.", "fix": "Primero mira el título y la imagen, luego lee el texto."},
    ],
    tiers={
        "recovery": [
            ex(f"En el cuento cuyo título es «La niña y el río», ¿de quién trata?", "De una niña", "El título nombra a la niña y al río."),
            ex("La imagen muestra una niña junto a un río. ¿Qué lugar aparece?", "Un río", "La imagen lo muestra."),
            ex("El título es el nombre del texto. ¿«La niña y el río» es el título o el tema?", "El título", "Es el nombre del texto."),
        ],
        "understand": [
            ex(f"Lee: {CUENTO} ¿Qué hace Rosa en el río?", "Escucha el agua y mira el cerro", "El texto lo dice."),
            ex("El tema es de qué trata un texto. En un texto con título «Cuidemos el agua», ¿cuál es el tema?", "Cuidar el agua", "El título lo dice."),
            ex("¿Por qué ayuda la imagen a comprender un texto?", "Porque muestra lo que sucede", "Da pistas visuales."),
        ],
        "apply": [
            ex(f"Según el texto de Rosa, ¿cuándo llega al río: por la mañana o cada tarde? Lee: {CUENTO}", "Cada tarde", "El texto dice «cada tarde»."),
            ex("Lee: «Mari mari. Hoy la feria abre a las 10 de la mañana. Habrá tejidos y cerámica». ¿A qué hora abre la feria?", "A las 10 de la mañana", "El texto da la hora."),
            ex("Con el texto anterior de la feria, ¿qué dos cosas habrá?", "Tejidos y cerámica", "El texto las nombra."),
        ],
        "reason": [
            ex("Un niño dice que Rosa está triste. El texto dice que vuelve «contenta». ¿Quién tiene razón?", "El texto", "El texto dice «contenta»."),
            ex("Una palabra del cartel está en lengua indígena y no la conoces. ¿Es mejor inventar su significado o preguntar al educador?", "Preguntar al educador", "Inventar puede cambiar el sentido."),
        ],
        "challenge": [
            ex("Lee: «Título: El camino del cerro. Imagen: tres niños con mochilas subiendo. Texto: Los niños suben despacio y descansan dos veces». ¿Cuántas veces descansan?", "2", "El texto dice dos veces."),
            ex("En el texto anterior, ¿qué dato viene de la imagen y no del texto: las mochilas, o que descansan dos veces?", "Las mochilas", "Las mochilas están en la imagen."),
        ],
    },
    context=[ex("En una exposición ves un cartel con una imagen de un telar y un título en dos lenguas. ¿Qué miras primero para comprender: el título y la imagen o solo una palabra?", "El título y la imagen", "Dan pistas del tema.")],
    selfcheck=[
        ex("¿Qué es el tema?", "De qué trata el texto", "Es de lo que habla."),
        ex("¿Qué ayuda a comprender además del texto?", "El título y la imagen", "Son pistas que ayudan."),
        ex("¿Qué haces con una palabra que no conoces en lengua indígena?", "Pregunto al educador", "Él conoce el significado."),
    ],
    open_task=task(
        "Lee este texto inventado: «Título: La feria del sábado. Imagen: puestos con telas y frutas. Texto: Mari mari. El sábado hay feria en la plaza. Habrá música y comida». Escribe tres respuestas: 1) tema, 2) qué día es la feria, 3) dos cosas que habrá. Agrega una pregunta al educador sobre «Mari mari».",
        "1) La feria del sábado. 2) El sábado. 3) Música y comida. Pregunta: ¿cuándo se usa «mari mari»?",
        ["responde el tema", "responde el día", "nombra dos cosas", "agrega pregunta"],
        ["tres respuestas", "pregunta"],
        ["usar datos que no están en el texto", "traducir el saludo por su cuenta"],
        "Reconoce que usó datos del texto y la imagen. Refuerza que el texto es inventado.",
    ),
    reinforce="Elige un libro de tu casa y di cuál es el título, qué muestra la imagen de la portada y de qué crees que trata.",
    extend="Haz un afiche de una feria con título, imagen y tres líneas de texto.",
)

register(
    LF03, 3,
    materials="Este cuaderno y lápiz. Escribe con letra clara.",
    use="Aprenderé a copiar con cuidado palabras escritas en una lengua indígena, respetando sus letras y signos. Sirve para no cambiar una palabra al escribirla.",
    prior=["Sé que cada lengua tiene sus letras.", "Sé contar letras."],
    explain=[
        "Cuando copias una palabra de una lengua indígena, cada letra importa. Algunas lenguas usan letras o signos que no usamos en castellano. Por ejemplo, algunas formas de escribir el mapuzugun usan la letra «ü», como en «antü» (sol). Si cambias una letra, la palabra puede cambiar de sentido o dejar de existir.",
        "También hay distintas formas de escribir una lengua, que se llaman grafías. Una comunidad decide cuál usa. Por eso, copia la palabra tal como te la muestra tu educador o educadora tradicional. No la «arregles» con las reglas del castellano, como ponerle tilde o cambiar la «k» por «c».",
        "Para copiar bien: mira la palabra letra por letra, cópiala despacio y compárala con el modelo. Cuenta las letras: si tienen la misma cantidad y son iguales, está bien. Y usa la palabra solo donde corresponda: por ejemplo, un cartel de la sala con su significado al lado.",
    ],
    vocab=[("grafía", "forma de escribir una lengua"), ("modelo", "palabra que copias"), ("letra", "signo que representa un sonido"), ("copiar", "escribir igual que el modelo"), ("comparar", "mirar dos cosas para ver si son iguales")],
    worked=[
        {"title": "Copiar con cuidado", "problem": "Copia la palabra «antü» (sol) y cuenta sus letras.", "steps": ["Escribo a, n, t, ü sin cambiar nada.", "Dejo los dos puntos sobre la u.", "Cuento: a, n, t, ü son 4 letras."], "answer": "antü, 4 letras"},
        {"title": "Detectar un error", "problem": "El modelo es «kuyen». Un niño copió «cuyen». ¿Qué cambió?", "steps": ["Comparo letra por letra.", "En el modelo la primera letra es k.", "El niño puso c: cambió una letra."], "answer": "Cambió la k por una c"},
    ],
    mistakes=[
        {"wrong": "Quitar los dos puntos de la ü porque «no se ven».", "why": "La ü es una letra de esa grafía y cambia la palabra.", "fix": "Copia exactamente, con sus dos puntos."},
        {"wrong": "Ponerle tilde a una palabra indígena como en castellano.", "why": "Cada lengua tiene sus propias reglas.", "fix": "Copia sin agregar signos que el modelo no tiene."},
    ],
    tiers={
        "recovery": [
            ex("Copiar es escribir igual que el modelo. Si el modelo es «mapu», ¿cómo lo copias?", "mapu", "Se escribe igual que el modelo."),
            ex("¿La palabra «antü» lleva dos puntos sobre la u?", "Sí", "Así se muestra el modelo."),
            ex("«Ko» tiene 2 letras. ¿Cuántas letras tiene «ko»?", "2", "Son la k y la o."),
        ],
        "understand": [
            ex("«Antü» significa sol. ¿Qué significa «antü»?", "Sol", "Así lo dice el modelo."),
            ex("¿Por qué no se cambia una letra de la palabra?", "Porque la palabra puede cambiar de sentido", "Cada letra importa."),
            ex("Una grafía es una forma de escribir una lengua. ¿Quién decide cuál usa la comunidad: la comunidad o un compañero?", "La comunidad", "Ella decide cómo escribe su lengua."),
        ],
        "apply": [
            arith("«Antü» tiene 4 letras y «kuyen» tiene 5 letras. ¿Cuántas letras tienen las dos palabras juntas?", "4+5", "Se suman las letras de cada palabra."),
            ex("Modelo: «mapu». Copias: A) «mapu», B) «mapo», C) «mapu». ¿Cuáles copias son iguales al modelo?", "A y C", "La B cambió la u por una o."),
            ex("Cuenta las letras de «kuyen»: k, u, y, e, n. ¿Cuántas son?", "5", "Se cuentan cinco letras."),
        ],
        "reason": [
            ex("Teo copió «kuyen» como «cuyen» «porque suena igual». ¿Qué le dices?", "Que copie la k como en el modelo", "La grafía del modelo es con k."),
            ex("Una compañera puso una tilde en «antü» «para que suene fuerte». ¿Fue correcto?", "No", "No se agregan signos que el modelo no tiene."),
        ],
        "challenge": [
            ex("Modelo: «antü». Copia 1: «antu». Copia 2: «antü». Copia 3: «anta». ¿Cuál copia es correcta y por qué?", "La copia 2, porque tiene todas las letras y los dos puntos", "Es igual al modelo."),
            ex("Tres compañeros copian «ko». Sol: «ko». Beto: «co». Lía: «ko». ¿Quiénes copiaron bien?", "Sol y Lía", "Beto cambió la k por una c."),
        ],
    },
    context=[ex("Tu curso hará un cartel con la palabra «antü» y su significado «sol». ¿Qué revisas antes de pegarlo?", "Que tenga todas las letras y los dos puntos", "Se compara con el modelo.")],
    selfcheck=[
        ex("¿Qué es una grafía?", "Una forma de escribir una lengua", "Cada lengua puede tener grafías."),
        ex("¿Se puede cambiar una letra para que se vea más fácil?", "No", "Cambia la palabra."),
        ex("¿Quién confirma la escritura?", "El educador o educadora tradicional", "Es la fuente."),
    ],
    open_task=task(
        "Copia en tu cuaderno estas cuatro palabras exactamente como están: «mapu» (tierra), «ko» (agua), «antü» (sol) y «kuyen» (luna). Escribe al lado cuántas letras tiene cada una. Luego compara tu copia con el modelo letra por letra y marca con una cruz las que estén iguales. Cuando venga el educador tradicional, pregúntale si la escritura es la que usa su comunidad.",
        "mapu (4), ko (2), antü (4), kuyen (5). Las cuatro están iguales al modelo. Preguntaré al educador si es la escritura de su comunidad.",
        ["copia las cuatro palabras sin cambiar letras", "cuenta bien las letras: 4, 2, 4, 5", "compara con el modelo", "agrega una pregunta"],
        ["cuatro palabras copiadas", "conteo de letras"],
        ["cambiar la k por c", "quitar los dos puntos de la ü"],
        "Reconoce que copió con cuidado y que verificó. Refuerza que la escritura la confirma el educador.",
    ),
    reinforce="Copia «mapu» y «ko» tres veces cada una y compara con el modelo.",
    extend="Cuenta las vocales de cada palabra: mapu, ko, antü y kuyen.",
)

register(
    LF03, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a compartir lo que comprendí de un texto, citando de dónde viene y diciendo qué no sé. Sirve para devolver a la comunidad lo aprendido sin inventar.",
    prior=["Sé comprender un texto con título, imagen y texto.", "Sé qué es una fuente."],
    explain=[
        "Cuando cuentas lo que leíste, cita el texto: di el título, quién lo escribió y de qué pueblo o lugar viene, si lo dice. Por ejemplo: «El cuento “La niña y el río” fue escrito para este cuaderno; no pertenece a ningún pueblo». Citar es decir de dónde viene la información.",
        "También di tus límites. Si no entendiste una palabra o no sabes cómo se pronuncia, dilo. Eso muestra respeto y evita inventar. Puedes decir: «No sé qué significa esa palabra y se lo voy a preguntar al educador».",
        "Después puedes devolver: mostrar a la comunidad o a quien enseñó lo que hiciste, por ejemplo un resumen o un dibujo. Pregúntale si está bien y corrige lo que haga falta. Así la comunidad cuida su lengua y tú aprendes con cuidado.",
    ],
    vocab=[("citar", "decir de dónde viene la información"), ("resumen", "texto breve con lo más importante"), ("límite", "lo que no sé"), ("devolver", "mostrar a quien enseñó lo que hice"), ("corregir", "cambiar lo que está mal")],
    worked=[
        {"title": "Citar el texto", "problem": "Leíste el cuento «La niña y el río», escrito para este cuaderno. Escribe una frase que lo cite y resuma.", "steps": ["Digo el título: «La niña y el río».", "Digo de dónde viene: escrito para este cuaderno.", "Resumo: Rosa escucha el agua y mira el cerro."], "answer": "En el cuento «La niña y el río», escrito para este cuaderno, Rosa escucha el agua y mira el cerro"},
        {"title": "Decir un límite", "problem": "El cartel tiene una palabra en lengua indígena que no entiendes. ¿Cómo lo dices al compartirlo?", "steps": ["No invento su significado.", "Digo: «No sé qué significa».", "La anoto para preguntar al educador."], "answer": "Digo que no sé qué significa y que lo preguntaré al educador"},
    ],
    mistakes=[
        {"wrong": "Contar lo que leíste sin decir de dónde viene.", "why": "No se sabe quién escribió ni si es confiable.", "fix": "Empieza citando el título y la fuente."},
        {"wrong": "Esconder las palabras que no entiendes.", "why": "Puedes dar información falsa.", "fix": "Di cuáles no entiendes y pregunta."},
    ],
    tiers={
        "recovery": [
            ex("Citar es decir de dónde viene la información. Si lees «El camino del cerro», ¿qué citas primero: el título o el color del papel?", "El título", "El título identifica el texto."),
            ex("Si no entendiste una palabra, ¿la inventas o la anotas para preguntar?", "La anoto para preguntar", "No se inventa."),
            ex("Devolver es mostrar a quien enseñó lo que hiciste. ¿A quién le muestras tu resumen?", "A quien enseñó", "Para que lo revise."),
        ],
        "understand": [
            ex("¿Qué dos datos citas de un texto: título y quién lo escribió, o el color y el tamaño?", "Título y quién lo escribió", "Son datos de la fuente."),
            ex("¿Para qué sirve decir un límite?", "Para no inventar y respetar", "Muestra lo que falta saber."),
            ex("Un resumen es un texto breve con lo más importante. ¿Es más largo o más corto que el texto original?", "Más corto", "Resume lo importante."),
        ],
        "apply": [
            ex("Elige la mejor cita: a) «El cuento “La niña y el río”, escrito para este cuaderno» o b) «Un cuento que leí». Letra:", "a", "Dice el título y la fuente."),
            arith("Un curso resume 4 textos y cada resumen tiene 2 frases. ¿Cuántas frases hay en total?", "4*2", "Se suman 2 frases cuatro veces."),
            ex("Resume en una frase: «Rosa llega al río cada tarde. Escucha el agua y mira el cerro. Vuelve contenta». Elige: a) «Rosa va al río y vuelve contenta» o b) «Rosa nunca va al río». Letra:", "a", "Es fiel al texto."),
        ],
        "reason": [
            ex("Pablo contó un cartel como si lo hubiera inventado. ¿Qué dato debió decir?", "Quién lo escribió", "Se cita la fuente."),
            ex("Una niña mostró su dibujo de un cuento a la educadora y ella le corrigió una palabra. ¿Qué hizo bien la niña?", "Devolvió su trabajo para corregirlo", "Así mejora su trabajo."),
        ],
        "challenge": [
            ex("Lee: «Mi cartel usa la palabra “ko”, que según el educador Luis significa agua. No sé cómo se pronuncia». Escribe la fuente, el dato y el límite.", "Fuente: el educador Luis; dato: ko significa agua; límite: no sé cómo se pronuncia", "Separa quién, qué y lo que no sabe."),
            ex("Dos compañeros presentan: Ema dice «ko significa agua, según el educador Luis». Beto dice «ko significa agua». ¿Quién cuidó mejor la fuente?", "Ema", "Cita al educador."),
        ],
    },
    context=[ex("Vas a presentar un cartel con palabras de la lengua del pueblo de tu comunidad. ¿Qué agregas para respetar a quien te enseñó?", "Su nombre como fuente", "Se reconoce a quien enseñó.")],
    selfcheck=[
        ex("¿Qué es citar?", "Decir de dónde viene la información", "Es dar la fuente."),
        ex("En Lengua y Cultura: ¿Qué es un límite?", "Lo que no sé", "Es lo que falta."),
        ex("¿Qué haces con un resumen después de hacerlo?", "Lo muestro a quien enseñó", "Para que lo revise."),
    ],
    open_task=task(
        "Lee este cuento inventado: «Título: El viento del patio. Texto: Sol siente el viento en el patio. Mueve las hojas y apaga la vela del cumpleaños. Sol sonríe y pide otro deseo». Escribe: 1) una cita (título y que fue inventado para este cuaderno), 2) un resumen de una frase y 3) un límite (algo que te gustaría preguntar a un educador tradicional sobre el viento).",
        "1) «El viento del patio», inventado para este cuaderno. 2) Sol siente el viento, que apaga la vela, y pide otro deseo. 3) Me gustaría preguntar cómo se dice «viento» en la lengua de su pueblo.",
        ["cita el título y la fuente", "resume en una frase", "escribe un límite o pregunta"],
        ["cita", "resumen", "límite"],
        ["no citar la fuente", "inventar una palabra en lengua indígena"],
        "Reconoce que citó y que dejó una pregunta honesta. Refuerza que no inventó la palabra.",
    ),
    reinforce="Cuéntale a un adulto un cuento que leíste hoy diciendo el título.",
    extend="Haz un resumen de dos frases de un cuento y muéstralo a alguien.",
)

register(
    LF03, 5,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a comparar dos formas de escribir una palabra o dos textos sin decir que una es mejor. Sirve para respetar que las lenguas y las comunidades pueden escribir de distintas maneras.",
    prior=["Sé copiar una palabra.", "Sé que hay grafías distintas."],
    explain=[
        "Una misma lengua puede escribirse de más de una manera. Por ejemplo, el nombre de la lengua mapuche se encuentra escrito como «mapudungun» y también como «mapuzugun». Son dos formas de escribir que usan comunidades, libros y personas distintas. Ninguna es la «correcta» y la otra «incorrecta».",
        "Otro ejemplo: el pueblo y la isla llamados Rapa Nui se escriben a veces «Rapa Nui» y a veces «Rapanui». Cuando compares, usa palabras como «es distinta» o «cambia». No digas «es mejor». Mejor pregunta: ¿quién la usa?, ¿en qué texto?, ¿para qué?",
        "Comparar es buscar qué se parece y qué cambia. Primero mira cada ejemplo y su fuente. Luego anota las semejanzas y las diferencias. Al final di qué contexto hace útil a cada uno. Si no lo sabes, pregunta a la comunidad.",
    ],
    vocab=[("comparar", "ver qué se parece y qué cambia"), ("variante", "otra forma de decir o escribir lo mismo"), ("semejanza", "lo que se parece"), ("diferencia", "lo que cambia"), ("autorizado", "con permiso de quien corresponde")],
    worked=[
        {"title": "Comparar dos escrituras", "problem": "Comparas «mapudungun» y «mapuzugun», dos formas de escribir el nombre de la lengua mapuche. ¿Qué se parece y qué cambia?", "steps": ["Se parecen en que empiezan con «mapu».", "Cambia la segunda parte: «dungun» y «zugun».", "Ninguna es mejor: las usan comunidades y libros distintos."], "answer": "Empiezan igual y cambia «dungun» por «zugun»; ninguna es mejor"},
        {"title": "No decir que una es superior", "problem": "Un compañero dice que «Rapa Nui» está bien y «Rapanui» está mal. ¿Qué le respondes?", "steps": ["Las dos formas se encuentran escritas.", "No son un error: son variantes.", "Pregunto en qué texto o comunidad se usa cada una."], "answer": "Que son variantes y que ninguna es mala"},
    ],
    mistakes=[
        {"wrong": "Decir que una variante es la correcta y la otra está mal.", "why": "Distintas comunidades y textos usan formas distintas.", "fix": "Di cuál usa cada fuente y pregunta por qué."},
        {"wrong": "Mezclar las dos variantes en un mismo texto.", "why": "Cada texto debe seguir una grafía.", "fix": "Elige la que usa tu fuente y úsala igual en todo el texto."},
    ],
    tiers={
        "recovery": [
            ex("Dos formas de escribir lo mismo se llaman variantes. «Mapudungun» y «mapuzugun» son variantes. ¿Es una de las dos un error?", "No", "Son dos formas válidas."),
            ex("Comparar es ver qué se parece y qué cambia. De «Rapa Nui» y «Rapanui», ¿cuál de las dos lleva un espacio?", "Rapa Nui", "La otra va escrita junta."),
            ex("¿Es mejor decir «ésta es mejor» o «es distinta» al comparar variantes?", "Es distinta", "No se jerarquiza."),
        ],
        "understand": [
            ex("¿Por qué existen distintas formas de escribir una lengua?", "Porque distintas comunidades y libros usan grafías distintas", "No hay una sola forma obligatoria."),
            ex("Beto dice que «Rapanui» está mal. ¿Qué le dices?", "Que es una variante", "También se encuentra escrita así."),
            ex("Si un texto usa «mapuzugun», ¿qué grafía mantienes en tu copia del texto?", "mapuzugun", "Copias lo que usa tu fuente."),
        ],
        "apply": [
            ex("Palabras: «mapudungun» y «mapuzugun». ¿En qué parte cambian: al comienzo o en la segunda parte?", "En la segunda parte", "Ambas empiezan con «mapu»."),
            ex("Compara «Rapa Nui» y «Rapanui». ¿Cuántas letras tiene «Rapanui»?", "7", "R, a, p, a, n, u, i son siete letras."),
            ex("Tabla: texto A usa «mapudungun» y texto B usa «mapuzugun». ¿Cuántas formas distintas aparecen?", "2", "Son dos formas distintas."),
        ],
        "reason": [
            ex("Un profesor dice que solo se puede usar una variante en el curso. ¿Qué pregunta le haces para decidir?", "¿Qué variante usa nuestra fuente o comunidad?", "La fuente define qué usar."),
            ex("Una niña usó «mapudungun» en el título y «mapuzugun» en el texto. ¿Qué mejora debe hacer?", "Usar la misma variante en todo el texto", "Cada texto sigue una grafía."),
        ],
        "challenge": [
            ex("Dos cartas hechas por comunidades distintas escriben el nombre de la lengua de manera diferente. Ana dice «una está mal». Luis dice «las dos son válidas». ¿Quién tiene razón y por qué?", "Luis, porque existen variantes", "Ninguna se descarta."),
            ex("Escribe una semejanza y una diferencia entre «mapudungun» y «mapuzugun».", "Semejanza: empiezan con «mapu»; diferencia: cambia «dungun» por «zugun»", "Sirve para comparar sin jerarquizar."),
        ],
    },
    context=[ex("En la feria ves dos carteles con una palabra escrita de manera distinta. ¿Qué pregunta haces: cuál es el correcto o quién lo escribió y para qué?", "Quién lo escribió y para qué", "Esa pregunta respeta a ambos.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es una variante?", "Otra forma de escribir o decir lo mismo", "Dos formas válidas."),
        ex("¿Se dice que una variante es mejor?", "No", "No se jerarquiza."),
        ex("¿Qué comparas?", "Qué se parece y qué cambia", "Semejanzas y diferencias."),
    ],
    open_task=task(
        "Compara estas dos escrituras reales del nombre de la lengua mapuche: «mapudungun» y «mapuzugun». Completa una tabla de tres filas: 1) una semejanza, 2) una diferencia y 3) una pregunta que le harías a un educador tradicional para saber cuál usa su comunidad. No escribas que una es mejor.",
        "1) Las dos empiezan con «mapu». 2) Cambia «dungun» por «zugun». 3) ¿Cuál de las dos escrituras usa su comunidad y por qué?",
        ["escribe una semejanza", "escribe una diferencia", "escribe una pregunta", "no dice que una es mejor"],
        ["tabla de tres filas"],
        ["decir que una está mal", "mezclar las dos escrituras"],
        "Reconoce que comparó sin jerarquizar. Refuerza que cada comunidad decide su grafía y que se pregunta al educador.",
    ),
    reinforce="Escribe tu nombre en letra imprenta y en letra cursiva y di qué se parece y qué cambia, sin decir que una está mal.",
    extend="Busca en tu casa dos etiquetas del mismo producto con escritura distinta y compara qué cambia.",
)

# ================================================================ LF04
register(
    LF04, 1,
    materials="Este cuaderno y lápiz con punta fina. Los modelos de palabras son pocos y muy conocidos; el educador/a tradicional los confirma.",
    use="Aprenderé a escuchar y mirar una palabra modelo antes de escribirla, para no inventar su escritura. Sirve para empezar a escribir una lengua indígena con cuidado.",
    prior=["Sé copiar palabras en castellano.", "Sé que cada lengua tiene sus letras."],
    explain=[
        "Escribir en una lengua indígena es una forma de cuidarla. Pero no se escribe adivinando. Primero se escucha la palabra de una persona que la hable y se mira cómo la escribe el educador o educadora tradicional. Ese ejemplo es el modelo. Un modelo es lo que copias para estar seguro.",
        "Cada letra representa un sonido. Algunas lenguas indígenas tienen sonidos que no existen en castellano y por eso usan letras o signos distintos. Si no conoces cómo se escribe un sonido, no lo inventes. Pregunta cómo lo escribe la comunidad.",
        "Palabras modelo muy conocidas en mapuzugun: «mari mari» (saludo), «mapu» (tierra), «ko» (agua), «antü» (sol) y «kuyen» (luna). Úsalas como práctica de copia, no para crear palabras nuevas. El educador tradicional te dirá cómo se dicen y cuándo se usan.",
    ],
    vocab=[("modelo", "palabra que copias para escribir bien"), ("sonido", "lo que oyes al decir una palabra"), ("letra", "signo que representa un sonido"), ("escritura", "forma de escribir una lengua"), ("confirmar", "comprobar con la persona que sabe")],
    worked=[
        {"title": "Mirar el modelo", "problem": "El educador muestra la palabra «mapu» (tierra) en la pizarra. ¿Qué haces antes de escribirla?", "steps": ["Miro las cuatro letras: m, a, p, u.", "Escucho cómo la dice el educador.", "La copio despacio sin cambiar nada."], "answer": "Miro y escucho el modelo, y la copio sin cambiar nada"},
        {"title": "Cuando no conoces un sonido", "problem": "Escuchas un sonido que no conoces y no sabes qué letra usar. ¿Qué haces?", "steps": ["No invento una letra.", "Anoto que no sé cómo se escribe.", "Pregunto al educador tradicional."], "answer": "Pregunto al educador y no invento la letra"},
    ],
    mistakes=[
        {"wrong": "Escribir una palabra indígena como suena en castellano.", "why": "Puede cambiar letras o signos y la palabra deja de ser correcta.", "fix": "Copia del modelo que muestra el educador."},
        {"wrong": "Inventar una palabra nueva mezclando sílabas de otras.", "why": "Las lenguas tienen sus propias formas y no se crean palabras al azar.", "fix": "Practica solo con palabras confirmadas."},
    ],
    tiers={
        "recovery": [
            ex("Un modelo es lo que copias para estar seguro. Si copias «ko», ¿cuál es el modelo?", "ko", "La palabra que copias."),
            ex("Cada letra representa un sonido. ¿Una letra representa un color o un sonido?", "Un sonido", "Así lo dice la explicación."),
            ex("Antes de escribir una palabra indígena, ¿qué haces: escucharla y mirarla, o adivinarla?", "Escucharla y mirarla", "Se aprende del modelo."),
        ],
        "understand": [
            ex("«Mapu» significa tierra. ¿Qué significa «mapu»?", "Tierra", "Es el significado del modelo."),
            ex("«Kuyen» significa luna. ¿Qué significa «kuyen»?", "Luna", "Es el significado del modelo."),
            ex("¿Por qué no se inventa la letra de un sonido que no conoces?", "Porque puede ser incorrecta", "Hay que preguntar a la comunidad."),
        ],
        "apply": [
            ex("De estas palabras muestra el modelo correcto del saludo: a) «mari mari», b) «marimari». Letra:", "a", "El modelo tiene dos palabras."),
            arith("«Mapu» tiene 4 letras y «ko» tiene 2 letras. ¿Cuántas letras tienen las dos palabras juntas?", "4+2", "Se suman las letras."),
            ex("Empareja: antü, ko, mapu. ¿Cuál es «agua»?", "ko", "Ko significa agua."),
        ],
        "reason": [
            ex("Sofía escribió «mari mari» como «mary mary». ¿Qué debió hacer antes de escribir?", "Mirar el modelo del educador", "Debe copiar el modelo."),
            ex("Un niño inventó la palabra «mapuko» juntando «mapu» y «ko». ¿Por qué no es buena idea?", "Porque inventó una palabra que no está confirmada", "No se crean palabras sin la comunidad."),
        ],
        "challenge": [
            ex("Tres modelos: «mari mari», «mapu», «ko». ¿Cuántas palabras hay en total si cuentas «mari mari» como dos palabras?", "4", "mari, mari, mapu y ko."),
            ex("Tienes los modelos «antü» y «kuyen». ¿Cuál tiene más letras y cuántas más?", "Kuyen, una letra más", "Kuyen tiene 5 y antü tiene 4."),
        ],
    },
    context=[ex("El educador tradicional escribe una palabra en la pizarra. Tu compañero la copia sin mirar bien. ¿Qué le sugieres?", "Mirar el modelo letra por letra", "Así evita errores.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es un modelo?", "Lo que copio para estar seguro", "Es la palabra confirmada."),
        ex("¿Qué haces si no conoces un sonido?", "Pregunto", "No se inventa."),
        ex("¿Qué significa «ko»?", "Agua", "Es el significado del modelo."),
    ],
    open_task=task(
        "Copia con letra clara estos cinco modelos: «mari mari», «mapu», «ko», «antü» y «kuyen». Al lado de cada uno escribe su significado: saludo, tierra, agua, sol y luna. Cuenta las letras de cada uno (sin el espacio en «mari mari»). Cuando venga el educador tradicional, pregúntale cómo se dicen y si escribe igual.",
        "mari mari (saludo, 8 letras), mapu (tierra, 4), ko (agua, 2), antü (sol, 4), kuyen (luna, 5). Le preguntaré cómo se dicen.",
        ["copia los cinco modelos", "escribe el significado de cada uno", "cuenta bien las letras", "agrega una pregunta"],
        ["lista de cinco palabras", "significados y conteo"],
        ["cambiar la ü", "inventar significados"],
        "Reconoce que copió con cuidado. Insiste en que el educador confirma la escritura y la pronunciación.",
    ),
    reinforce="Copia «mari mari» tres veces y revisa letra por letra.",
    extend="Cuenta cuántas letras suman en total los cinco modelos juntos.",
)

register(
    LF04, 2,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé la diferencia entre palabra, frase y oración, y cómo un significado se une a una palabra. Sirve para escribir con sentido, en castellano y con palabras confirmadas de una lengua indígena.",
    prior=["Sé copiar un modelo.", "Sé qué significan mapu, ko, antü y kuyen."],
    explain=[
        "Una palabra es una unidad con significado, como «sol» o «agua». Una frase es un grupo de palabras que dice algo, como «el sol de la mañana». Una oración es una idea completa, con quien hace algo y qué hace, como «El sol sale temprano». Cada una tiene su lugar al escribir.",
        "En este curso solo practicamos con palabras sueltas de mapuzugun que son muy conocidas. No inventamos frases ni oraciones en esa lengua, porque la gramática de una lengua la conocen sus hablantes. Para formar una oración en mapuzugun, hay que pedir ayuda a quien la habla.",
        "Lo que sí podemos hacer es escribir oraciones en castellano y poner al lado la palabra confirmada. Por ejemplo: «El sol (antü) sale temprano». Así unes el significado en castellano con la palabra de la lengua, sin cambiar nada.",
    ],
    vocab=[("palabra", "unidad con significado"), ("frase", "grupo de palabras que dice algo"), ("oración", "idea completa"), ("significado", "lo que quiere decir una palabra"), ("revisión", "leer de nuevo para corregir")],
    worked=[
        {"title": "Palabra, frase u oración", "problem": "Clasifica: A) «ko», B) «el agua fría», C) «El agua corre». ¿Cuál es palabra, frase y oración?", "steps": ["A es una sola palabra.", "B es un grupo de palabras sin idea completa: es frase.", "C dice quién hace algo: es oración."], "answer": "A palabra, B frase, C oración"},
        {"title": "Unir significado y palabra", "problem": "Escribe una oración en castellano sobre el sol e incluye la palabra confirmada «antü».", "steps": ["Pienso una idea completa en castellano.", "Escribo: El sol sale temprano.", "Pongo la palabra confirmada entre paréntesis: El sol (antü) sale temprano."], "answer": "El sol (antü) sale temprano"},
    ],
    mistakes=[
        {"wrong": "Armar una oración en mapuzugun juntando palabras sueltas.", "why": "La gramática de una lengua no es juntar palabras en el orden del castellano.", "fix": "Escribe la oración en castellano y pide ayuda a un hablante para la lengua."},
        {"wrong": "Confundir una frase con una oración.", "why": "La oración dice una idea completa.", "fix": "Pregunta: ¿quién hace qué?"},
    ],
    tiers={
        "recovery": [
            ex("¿«Sol» es una palabra, una frase o una oración?", "Una palabra", "Es una sola unidad con significado."),
            ex("«Los niños juegan» dice quién hace algo. ¿Es una frase o una oración?", "Una oración", "Tiene idea completa."),
            ex("«Mapu» significa tierra. ¿Qué es «mapu»: una palabra o una oración?", "Una palabra", "Es una sola unidad."),
        ],
        "understand": [
            ex("Clasifica «el agua clara»: ¿frase u oración?", "Frase", "No dice qué hace el agua."),
            ex("¿Por qué no armamos oraciones en mapuzugun en el cuaderno?", "Porque la gramática la conocen sus hablantes", "No se inventa."),
            ex("¿Qué es la revisión?", "Leer de nuevo para corregir", "Se mira otra vez lo escrito."),
        ],
        "apply": [
            ex("Completa con una palabra de la lista (mapu, ko, antü, kuyen): «La __ brilla de noche (luna)». ¿Qué palabra va?", "kuyen", "Kuyen es luna."),
            ex("Escribe la oración: «El agua (___) está fría». ¿Qué palabra confirmada va entre paréntesis?", "ko", "Ko es agua."),
            ex("En «Los niños juegan en la tierra (mapu)», ¿cuántas palabras hay sin contar el paréntesis?", "6", "Los, niños, juegan, en, la y tierra son seis palabras."),
        ],
        "reason": [
            ex("Un niño escribió «ko mapu antü» para decir «el agua de la tierra bajo el sol». ¿Qué error cometió?", "Inventó una oración en mapuzugun", "Juntó palabras sin saber la gramática."),
            ex("Una niña escribió «El sol (antü) sale temprano». ¿Qué hizo bien?", "Escribió en castellano y puso la palabra confirmada", "Unió significado y palabra sin inventar."),
        ],
        "challenge": [
            ex("Mira estas tres líneas: A) «luna», B) «la luna blanca», C) «La luna sale de noche». Escribe cuál es palabra, frase y oración.", "A palabra; B frase; C oración", "Solo C tiene idea completa."),
            ex("Escribe una oración sobre la tierra con la palabra «mapu» entre paréntesis. Elige: a) «La tierra (mapu) está seca» o b) «Mapu tierra seca». Letra:", "a", "Es una oración clara en castellano con la palabra confirmada."),
        ],
    },
    context=[ex("Quieres hacer un cartel que diga «El agua es vida» y usar la palabra «ko». ¿Cómo lo haces sin inventar?", "Escribo la oración en castellano y pongo «ko» entre paréntesis", "Así no se inventa la gramática.")],
    selfcheck=[
        ex("¿Qué es una oración?", "Una idea completa", "Dice quién hace qué."),
        ex("¿Qué es una frase?", "Un grupo de palabras que dice algo", "No siempre es una idea completa."),
        ex("¿Se inventan oraciones en mapuzugun en este cuaderno?", "No", "Solo se usan palabras confirmadas."),
    ],
    open_task=task(
        "Escribe tres oraciones en castellano, una por cada tema de esta lista: el sol, el agua y la luna. Después pon al lado de cada una, entre paréntesis, la palabra confirmada correspondiente: antü, ko o kuyen. Marca con un subrayado la palabra confirmada. Cuando venga el educador tradicional, pregúntale si puede decir la oración completa en su lengua.",
        "El sol (antü) sale temprano. El agua (ko) está fría. La luna (kuyen) brilla de noche. Preguntaré al educador cómo se dicen las oraciones en su lengua.",
        ["escribe tres oraciones en castellano", "usa antü, ko y kuyen con su significado correcto", "subraya la palabra", "agrega una pregunta"],
        ["tres oraciones", "palabras subrayadas"],
        ["juntar palabras en mapuzugun para formar oraciones", "cambiar el significado de las palabras"],
        "Reconoce que escribió en castellano y puso las palabras confirmadas. Refuerza que la oración en la lengua la dice un hablante.",
    ),
    reinforce="Escribe una oración sobre algo que ves hoy y subraya la palabra principal.",
    extend="Escribe tres frases y tres oraciones sobre tu patio y clasifícalas.",
)

register(
    LF04, 3,
    materials="Este cuaderno, lápiz y lápices de colores.",
    use="Aprenderé a usar palabras confirmadas en una tarjeta ilustrada, respetando su escritura y su contexto. Sirve para practicar la escritura inicial sin inventar nada.",
    prior=["Sé qué es una oración.", "Sé copiar un modelo."],
    explain=[
        "Una tarjeta de palabra tiene tres partes: la palabra confirmada, su significado en castellano y un dibujo. Por ejemplo: «antü / sol» con un dibujo del sol. Es una manera de aprender sin inventar. Se escribe la palabra tal como está en el modelo.",
        "Usa la palabra solo donde es pertinente, es decir, adecuada. Una tarjeta de saludo, como «mari mari», se usa para recibir a una visita. Una tarjeta de naturaleza, como «ko», sirve para nombrar el agua. No uses una palabra como burla ni en un lugar donde la comunidad no lo desea.",
        "Cuando hagas tu tarjeta, escribe tu nombre como autor o autora y pon abajo: «Palabra confirmada por el educador tradicional» cuando él te lo diga. Si aún no la confirma, pon: «Palabra pendiente de confirmar».",
    ],
    vocab=[("tarjeta de palabra", "tarjeta con palabra, significado y dibujo"), ("pertinente", "adecuado para la situación"), ("autoría", "quién hizo la tarjeta"), ("confirmada", "revisada por quien sabe"), ("pendiente", "que falta hacerse")],
    worked=[
        {"title": "Armar una tarjeta", "problem": "Arma una tarjeta con la palabra «ko» (agua).", "steps": ["Escribo «ko» como en el modelo.", "Escribo al lado: agua.", "Dibujo una gota o un río.", "Escribo mi nombre como autor."], "answer": "Tarjeta: «ko / agua», dibujo de agua y mi nombre como autor"},
        {"title": "Palabra pendiente", "problem": "Hiciste la tarjeta «mapu» pero el educador aún no la ha revisado. ¿Qué escribes abajo?", "steps": ["No digo que está confirmada.", "Escribo que está pendiente.", "La muestro cuando el educador pueda revisarla."], "answer": "Palabra pendiente de confirmar"},
    ],
    mistakes=[
        {"wrong": "Escribir en la tarjeta «confirmada» sin que nadie la haya revisado.", "why": "Es decir algo que no es verdad.", "fix": "Escribe «pendiente de confirmar»."},
        {"wrong": "Usar una tarjeta de saludo para hacer una broma.", "why": "El saludo es de una lengua viva y se usa con respeto.", "fix": "Úsala para recibir a una visita."},
    ],
    tiers={
        "recovery": [
            ex("Una tarjeta tiene palabra, significado y dibujo. ¿Cuántas partes son?", "3", "Se cuentan tres."),
            ex("En la tarjeta «antü / sol», ¿qué dibujo va: un sol o una luna?", "Un sol", "Antü significa sol."),
            ex("Si el educador no revisó la tarjeta, ¿qué escribes: «confirmada» o «pendiente de confirmar»?", "Pendiente de confirmar", "No se afirma algo no revisado."),
        ],
        "understand": [
            ex("Una tarjeta «mari mari» sirve para..., ¿saludar a una visita o hacer una broma?", "Saludar a una visita", "Es un saludo."),
            ex("¿Por qué pones tu nombre en la tarjeta?", "Para mostrar quién la hizo", "Es la autoría."),
            ex("¿Qué palabra va en una tarjeta con el dibujo de una luna: «kuyen» o «ko»?", "Kuyen", "Kuyen es luna."),
        ],
        "apply": [
            ex("Arma la tarjeta de «ko»: escribe la palabra, el significado y el dibujo. Escribe: «ko / ___ / dibujo de ___».", "ko / agua / dibujo de agua", "Ko significa agua."),
            arith("Tienes 5 tarjetas de palabras y haces 3 más. ¿Cuántas tarjetas tienes?", "5+3", "Se suman las tarjetas."),
            ex("De estas dos tarjetas, ¿cuál está bien hecha? A) «mapu / sol» con un dibujo de tierra. B) «mapu / tierra» con un dibujo de tierra. Letra:", "B", "Mapu significa tierra."),
        ],
        "reason": [
            ex("Tomás hizo una tarjeta con «antü / luna». ¿Qué error tiene?", "Cambió el significado: antü es sol", "Antü significa sol."),
            ex("Una niña pegó una tarjeta en la sala y escribió «confirmada» sin mostrarla al educador. ¿Qué debió escribir?", "Pendiente de confirmar", "No se afirma algo no revisado."),
        ],
        "challenge": [
            ex("Dos tarjetas: 1) «kuyen / luna» con dibujo de luna y firma. 2) «kuyen / luna» sin firma ni dibujo. ¿Cuál es más completa?", "La 1", "Tiene todas las partes y la autoría."),
            ex("Tienes tres tarjetas: «ko / agua», «antü / sol», «mapu / tierra». ¿Cuál palabra tiene menos letras y cuántas?", "ko, 2 letras", "Ko tiene 2 letras; antü y mapu tienen 4 cada una."),
        ],
    },
    context=[ex("El curso decora la sala con tarjetas para recibir al educador. ¿Cuál tarjeta de la lista usas: «mari mari», «ko» o «antü»?", "mari mari", "Es el saludo para recibir.")],
    selfcheck=[
        ex("¿Qué partes tiene una tarjeta de palabra?", "Palabra, significado y dibujo", "Son tres partes."),
        ex("¿Cuándo escribes «pendiente de confirmar»?", "Cuando el educador no la ha revisado", "No se afirma sin revisión."),
        ex("¿Se usa la palabra para burlarse?", "No", "Se usa con respeto."),
    ],
    open_task=task(
        "Haz una tarjeta de palabra con una de estas opciones: «mari mari» (saludo), «mapu» (tierra), «ko» (agua), «antü» (sol) o «kuyen» (luna). Escribe la palabra, su significado, un dibujo y tu nombre como autor. Abajo escribe: «Palabra pendiente de confirmar por el educador tradicional». Muéstrala al educador cuando venga.",
        "Tarjeta: «antü / sol», con un dibujo del sol y mi nombre. Abajo: «Palabra pendiente de confirmar por el educador tradicional».",
        ["escribe la palabra sin cambiar letras", "escribe el significado correcto", "dibuja", "escribe pendiente de confirmar"],
        ["tarjeta terminada"],
        ["cambiar el significado", "escribir confirmada sin revisión"],
        "Reconoce la tarjeta y que escribió «pendiente». Refuerza que el educador confirma la escritura.",
    ),
    reinforce="Haz otra tarjeta con otra palabra de la lista.",
    extend="Haz un cartel con las cinco tarjetas y escribe abajo quién las hizo.",
)

register(
    LF04, 4,
    materials="Este cuaderno y lápiz.",
    use="Aprenderé a revisar mi escritura comparándola con el modelo y a mostrarla a quien me enseñó para que la corrija. Sirve para mejorar y devolver mi trabajo con respeto.",
    prior=["Sé armar una tarjeta de palabra.", "Sé citar la fuente."],
    explain=[
        "Revisar es leer de nuevo lo que escribiste para corregir. Para revisar una palabra indígena, ponla al lado del modelo y compara letra por letra. Mira la cantidad de letras, las letras especiales como «ü» y los espacios. Si algo cambia, corrige.",
        "Una lista de revisión ayuda: 1) ¿tiene las mismas letras que el modelo?, 2) ¿lleva sus signos, como los dos puntos de la «ü»?, 3) ¿está bien su significado?, 4) ¿puse mi nombre y la fuente? Si respondes sí a las cuatro, tu escritura está lista para mostrarla.",
        "Después viene devolver: muestra tu trabajo al educador o educadora tradicional o a quien te enseñó. Pregunta si está bien y escucha. Si te corrige, agradece y cambia. Corregir no es un castigo: es parte de aprender una lengua que se cuida entre todos.",
    ],
    vocab=[("revisar", "leer de nuevo para corregir"), ("lista de revisión", "lista de preguntas para comprobar el trabajo"), ("comparar", "ver qué se parece y qué cambia"), ("corregir", "cambiar lo que está mal"), ("devolver", "mostrar a quien enseñó lo que hice")],
    worked=[
        {"title": "Revisar con el modelo", "problem": "Modelo: «antü». Tu copia: «antu». Revisa y corrige.", "steps": ["Comparo letra por letra.", "Falta el signo de la ü: puse u.", "Corrijo: antü."], "answer": "Corrijo «antu» por «antü»"},
        {"title": "Usar la lista de revisión", "problem": "Hiciste una tarjeta «ko / agua» con tu nombre pero sin dibujo. ¿Está lista?", "steps": ["Las letras están bien.", "El significado está bien.", "Falta el dibujo de la tarjeta."], "answer": "Todavía no: falta el dibujo"},
    ],
    mistakes=[
        {"wrong": "Creer que no hace falta revisar porque «ya la copié».", "why": "Se pueden olvidar letras o signos.", "fix": "Compara siempre con el modelo."},
        {"wrong": "Enojarse cuando el educador corrige.", "why": "La corrección ayuda a escribir bien.", "fix": "Agradece, escucha y cambia."},
    ],
    tiers={
        "recovery": [
            ex("Para revisar una palabra indígena, ¿qué pones al lado: el modelo o un dibujo?", "El modelo", "Comparas con el modelo."),
            ex("Modelo: «mapu». Copia: «mapu». ¿Está igual?", "Sí", "Tiene las mismas letras."),
            ex("Si el educador te corrige, ¿qué haces: te enojas o agradeces y cambias?", "Agradezco y cambio", "Corregir ayuda a mejorar."),
        ],
        "understand": [
            ex("¿Cuántas preguntas tiene la lista de revisión: 1) letras, 2) signos, 3) significado, 4) nombre y fuente?", "4", "Se cuentan cuatro."),
            ex("En «antü», ¿qué signo especial hay que revisar?", "Los dos puntos de la ü", "Es la letra especial."),
            ex("Revisar sirve para..., ¿corregir errores o cambiar el modelo?", "Corregir errores", "Se compara con el modelo."),
        ],
        "apply": [
            ex("Modelo: «kuyen». Copia: «kuyem». ¿Qué letra cambió?", "La n por m", "La última letra es distinta."),
            ex("Modelo: «mari mari». Copia: «marimari». ¿Qué falta?", "El espacio entre las palabras", "Son dos palabras."),
            arith("Tienes 6 palabras para revisar y ya revisaste 4. ¿Cuántas te quedan?", "6-4", "Se resta lo revisado."),
        ],
        "reason": [
            ex("Beto dice que no necesita revisar porque copió despacio. ¿Qué le dices?", "Que igual puede haber errores y conviene comparar", "Siempre se compara."),
            ex("Una niña mostró su cartel al educador y él le corrigió una letra. ¿Qué hizo bien ella?", "Devolvió su trabajo para que lo revisaran", "Así mejoró su escritura."),
        ],
        "challenge": [
            ex("Mira estas tres copias del modelo «antü»: 1) «antu», 2) «antü», 3) «anto». ¿Cuál no necesita corrección?", "La 2", "Solo la 2 es igual al modelo."),
            ex("Revisa esta tarjeta: «ko / sol» con un dibujo de agua. ¿Qué dato es incorrecto?", "El significado: ko es agua", "El dibujo muestra agua pero el significado dice sol."),
        ],
    },
    context=[ex("Terminaste una tarjeta para tu sala. Antes de pegarla, ¿qué paso falta: revisarla con la lista o dejarla así?", "Revisarla con la lista", "Se revisa antes de mostrar.")],
    selfcheck=[
        ex("¿Con qué comparas tu copia?", "Con el modelo", "Letra por letra."),
        ex("¿Qué haces si te corrigen?", "Agradezco y cambio", "Es parte de aprender."),
        ex("¿Qué es devolver?", "Mostrar a quien enseñó lo que hice", "Para que lo revise."),
    ],
    open_task=task(
        "Revisa esta copia inventada de un estudiante: el modelo es «antü / sol» y el estudiante escribió «antu / luna». Escribe qué dos cosas debes corregir y cómo quedaría bien. Después revisa tu propia tarjeta de la clase anterior con la lista de cuatro preguntas y escribe sí o no a cada una.",
        "Corregir: 1) falta la ü (antü). 2) el significado es sol, no luna. Bien: «antü / sol». Mi tarjeta: letras sí, signos sí, significado sí, nombre y fuente sí.",
        ["encuentra los dos errores", "escribe la versión corregida", "usa la lista de cuatro preguntas"],
        ["dos correcciones", "lista de revisión"],
        ["no ver el error del significado", "olvidar la ü"],
        "Reconoce que revisó con el modelo y la lista. Refuerza que mostrar el trabajo al educador es parte de aprender.",
    ),
    reinforce="Pide a alguien de tu casa que compare tu copia de «mapu» con el modelo y te diga si es igual.",
    extend="Crea una lista de revisión con tus propias cuatro preguntas para revisar tu tarea de escritura.",
)
