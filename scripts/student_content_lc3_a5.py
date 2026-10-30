"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 14 (patrimonio cultural de comunidad, territorio y pueblo) y OA 15 (ciencia indígena en relación con
naturaleza y cosmos).

Criterio de autoría: las comunidades, las personas, los lugares, los relatos y los saberes de práctica son
INVENTADOS y se rotulan así. No se afirma nada de lengua, ritos, fechas, arte, cosmovisión ni conocimientos
astronómicos o de otro tipo de un pueblo concreto. Los datos de "ciencia escolar" son hechos generales y
seguros (estaciones, día y noche, fases de la Luna). Lo tradicional lo enseñan el educador o la educadora
tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc3_a import L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA14, OA15 = "LC03 OA 14", "LC03 OA 15"

# ============================================================ OA 14 · Patrimonio cultural de comunidad, territorio y pueblo
L(
    OA14, 1,
    materials="Lápiz y hojas. La lista de ejemplos está escrita aquí y es inventada.",
    use="Aprenderé a reconocer distintas manifestaciones del patrimonio cultural y a distinguir un objeto de una práctica viva. Sirve para valorar lo que la comunidad hereda y cuida.",
    prior=["Sé que las culturas indígenas están vivas hoy.", "Sé que hay cosas que se comparten y otras que se resguardan."],
    explain=[
        "El patrimonio cultural es lo que una comunidad hereda de sus antepasados, valora y quiere cuidar. Hay patrimonio de distintos tipos: comidas, ceremonias, espacios naturales, sitios arqueológicos, relatos, oficios y otras manifestaciones.",
        "Hay que distinguir un objeto de una práctica viva. Un objeto es una cosa, como una olla antigua guardada en un museo. Una práctica viva es algo que las personas hacen hoy, como preparar una comida o enseñar un relato. El patrimonio incluye ambos.",
        "Un sitio arqueológico es un lugar donde hay restos de personas que vivieron hace mucho tiempo. Un espacio natural es un lugar de la naturaleza importante para la comunidad. En esta clase usamos una lista inventada para practicar. El patrimonio real lo cuenta la comunidad.",
    ],
    vocab=[("patrimonio cultural", "lo que una comunidad hereda, valora y quiere cuidar"), ("práctica viva", "algo que las personas hacen hoy y se sigue transmitiendo"), ("objeto", "cosa que se puede guardar o mostrar"), ("sitio arqueológico", "lugar con restos de personas que vivieron hace mucho"), ("espacio natural", "lugar de la naturaleza importante para la comunidad")],
    worked=[
        W("Clasificar una manifestación", "Lista inventada de Valle Alto: 1) una sopa que se prepara en la fiesta de la cosecha, 2) una olla antigua guardada en la escuela, 3) la vertiente. ¿Cuál es un espacio natural?", ["La sopa es una comida.", "La olla es un objeto.", "La vertiente es un lugar de la naturaleza."], "La 3, la vertiente."),
        W("Objeto o práctica viva", "¿La sopa que se prepara cada año es un objeto o una práctica viva?", ["Las personas la preparan hoy.", "Se repite cada año.", "Es una práctica viva."], "Una práctica viva."),
    ],
    mistakes=[
        M("Pensar que el patrimonio son solo cosas antiguas guardadas.", "También hay prácticas vivas que se hacen hoy.", "Pregunta si la gente lo sigue haciendo."),
        M("Llamar «patrimonio de un pueblo» a algo sin que la fuente lo diga.", "Puede ser falso.", "Atribuye con una fuente."),
    ],
    R=[
        ex("Una olla antigua guardada en una escuela, ¿es un objeto o una práctica viva?", "Un objeto", "Es una cosa guardada."),
        ex("Preparar una comida que se repite cada año, ¿es un objeto o una práctica viva?", "Una práctica viva", "Las personas lo hacen hoy."),
        ex("¿La vertiente es un espacio natural o un objeto? Responde.", "Un espacio natural", "Es un lugar de la naturaleza."),
    ],
    C=[
        ex("¿Qué es el patrimonio cultural? A) lo que una comunidad hereda, valora y quiere cuidar B) una compra", "A", "Es lo que se hereda y se cuida."),
        ex("Verdadero o falso: el patrimonio son solo cosas antiguas guardadas.", "Falso", "También hay prácticas vivas."),
        ex("Verdadero o falso: un sitio arqueológico tiene restos de personas que vivieron hace mucho.", "Verdadero", "Esa es su definición."),
    ],
    A=[
        ex("Clasifica en COMIDA, ESPACIO NATURAL u OBJETO: a) una sopa de la fiesta b) la vertiente c) una olla antigua.", "a comida, b espacio natural, c objeto", "Cada ejemplo corresponde a su tipo."),
        ex("Una abuela de Valle Alto (inventada) enseña cada año a las niñas y niños cómo preparar una sopa de la cosecha. ¿Eso es un objeto o una práctica viva?", "Una práctica viva", "Se hace hoy y se sigue transmitiendo."),
        ex("Une cada ejemplo inventado con su tipo. 1) un relato que cuenta una abuela 2) un cerro importante 3) restos de un lugar muy antiguo a) espacio natural b) sitio arqueológico c) práctica viva", "1-c, 2-a, 3-b", "Cada uno corresponde a su tipo."),
    ],
    Z=[
        ex("Tomás dice: «Solo es patrimonio lo que está en un museo». ¿Qué error comete?", "Olvida las prácticas vivas", "El patrimonio incluye lo que se hace hoy."),
        ex("Ema dice que una lista inventada muestra el patrimonio de todos los pueblos. ¿Qué error comete?", "Generaliza una lista inventada", "Cada comunidad tiene el suyo."),
    ],
    D=[
        ex("Una escuela guarda un objeto antiguo y también invita a una abuela a enseñar un relato. ¿Qué tipos de patrimonio hay? A) un objeto y una práctica viva B) solo un objeto", "A", "El relato es una práctica viva."),
        ex("Para saber cuál es el patrimonio de tu comunidad, ¿a quién consultas? A) al educador tradicional o a la comunidad B) a nadie", "A", "Ellos son la fuente."),
    ],
    context=[ex("Tu curso hace una lista inventada de patrimonio de Valle Alto con una sopa, una olla antigua y la vertiente. ¿Cuántos son prácticas vivas? Escribe el número.", "1", "Solo la sopa que se prepara cada año.")],
    selfcheck=[
        ex("Escribe qué es el patrimonio cultural.", "Lo que una comunidad hereda, valora y quiere cuidar", "Es la definición."),
        ex("Verdadero o falso: una práctica viva es algo que las personas hacen hoy.", "Verdadero", "Se transmite hoy."),
        ex("Nombra dos tipos de patrimonio de la clase.", "Dos de estos: comidas, ceremonias, espacios naturales, sitios arqueológicos", "Son los tipos vistos."),
    ],
    task=T("Con esta lista inventada de Valle Alto: una sopa de la fiesta de la cosecha, una olla antigua guardada en la escuela, la vertiente y un relato que cuenta doña Rosa, haz una tabla con dos columnas: «Objeto» y «Práctica viva o espacio». Escribe al lado cuál es cada tipo. Añade una pregunta para el educador tradicional sobre un patrimonio de tu zona que se pueda compartir.",
           "Objeto: la olla antigua. Práctica viva: la sopa de la fiesta y el relato de doña Rosa. Espacio natural: la vertiente. Pregunta: ¿qué patrimonio de nuestra zona se puede conocer y cuidar con respeto?",
           ["clasifica los cuatro ejemplos", "distingue objeto y práctica viva", "formula una pregunta"], ["tabla", "pregunta"], ["decir que todo es objeto", "inventar patrimonio real"],
           "Preguntar por qué el relato es práctica viva; valorar la pregunta."),
    reinforce="Escribe tres ejemplos inventados de patrimonio y su tipo.",
    extend="Escribe una frase que explique por qué una práctica viva también necesita cuidado.",
)

L(
    OA14, 2,
    materials="Lápiz y hojas. La ficha está escrita aquí y es inventada.",
    use="Aprenderé a investigar la procedencia y el significado de una manifestación del patrimonio preguntando a la fuente adecuada. Sirve para conocerla sin inventar.",
    prior=["Sé qué es el patrimonio cultural.", "Sé que una ficha tiene fuente y permiso."],
    explain=[
        "Investigar la procedencia es descubrir de dónde viene algo y quién lo cuida. Investigar el significado es saber por qué es importante para la comunidad. Ambas cosas las cuenta la propia comunidad, no se adivinan.",
        "Podemos preparar una entrevista, que es una conversación con preguntas. Las preguntas piden datos: ¿De dónde viene? ¿Quién lo cuida? ¿Para qué se hace? ¿Qué se puede compartir? Así recogemos información de una fuente.",
        "Anotamos lo que dice la fuente con sus palabras y agradecemos. Si algo no se cuenta, lo dejamos escrito como límite. En esta clase usamos una ficha inventada de la sopa de Valle Alto. Los significados reales los enseñan el educador tradicional y la comunidad.",
    ],
    vocab=[("procedencia", "lugar o comunidad de donde viene algo"), ("significado", "razón y sentido de algo"), ("entrevista", "conversación en que se hacen preguntas a una persona"), ("fuente", "persona que entrega la información"), ("compartir", "dar a otros una parte de lo que uno tiene o sabe")],
    worked=[
        W("Leer la ficha", "Ficha inventada: «Comida: sopa de la fiesta de la cosecha de Valle Alto. La cuenta doña Rosa. Se prepara con lo que da la huerta. Significado: agradecer la cosecha. Límite: la receta exacta la guarda la familia.» ¿Cuál es el significado?", ["Busco la línea Significado.", "Dice agradecer la cosecha.", "Respondo."], "Agradecer la cosecha."),
        W("Elegir una buena pregunta", "Para saber de dónde viene la sopa, ¿qué pregunta haces a doña Rosa? A) ¿De dónde viene esta comida? B) ¿Es rica?", ["Busco un dato.", "A pide la procedencia.", "B pide una opinión."], "A."),
    ],
    mistakes=[
        M("Pedir la receta exacta aunque la familia la guarda.", "Es un límite que se respeta.", "Pregunta qué se puede compartir."),
        M("Inventar el significado de una comida.", "Solo la comunidad lo cuenta.", "Anota lo que dice la fuente."),
    ],
    R=[
        ex("En la ficha, ¿quién cuenta?", "Doña Rosa", "La ficha la nombra."),
        ex("¿Cuál es el significado de la sopa en la ficha? A) agradecer la cosecha B) ganar un premio", "A", "La ficha lo dice."),
        ex("La receta exacta, ¿se comparte o la guarda la familia?", "La guarda la familia", "Es el límite de la ficha."),
    ],
    C=[
        ex("¿Qué es la procedencia? A) de dónde viene algo B) cuánto cuesta", "A", "Dice su origen."),
        ex("Verdadero o falso: puedo inventar el significado de una comida si no lo sé.", "Falso", "Lo cuenta la comunidad."),
        ex("Verdadero o falso: una entrevista usa preguntas que piden datos.", "Verdadero", "Así se obtiene información."),
    ],
    A=[
        ex("Clasifica en PROCEDENCIA, SIGNIFICADO o LÍMITE: a) viene de la huerta de Valle Alto b) agradecer la cosecha c) la receta exacta no se comparte.", "a procedencia, b significado, c límite", "Cada dato responde una pregunta distinta."),
        ex("¿Qué pregunta pide el significado de la sopa? A) ¿Para qué se prepara la sopa? B) ¿Cuánto cuesta la sopa?", "A", "«¿Para qué?» pide la razón y el sentido."),
        ex("Ordena para investigar: a) agradecer b) preparar preguntas c) entrevistar d) anotar. ¿Cuál va primero?", "b", "Primero se preparan las preguntas."),
    ],
    Z=[
        ex("Ema dice que sabe el significado de una comida de un pueblo real porque lo vio en un video. ¿Qué error comete?", "No consultó a la comunidad", "El significado lo cuenta la comunidad."),
        ex("Pedro entrevistó a doña Rosa y escribió la receta exacta, que ella dijo que no podía contar. ¿Qué hizo mal?", "No respetó el límite", "La receta es de la familia."),
    ],
    D=[
        ex("Dos preguntas: 1) ¿Es la sopa más rica que otra? 2) ¿De dónde viene la sopa y quién la cuida? ¿Cuál sirve para investigar procedencia?", "La 2", "Pide datos concretos."),
        ex("Quieres entrevistar a una persona mayor de tu comunidad. ¿Qué haces antes? A) pedir permiso y avisar el tema B) llegar sin avisar", "A", "Se pide consentimiento."),
    ],
    context=[ex("Tu curso prepara una entrevista a doña Rosa. ¿Qué incluye al final? A) un agradecimiento B) nada", "A", "Se reconoce lo recibido.")],
    selfcheck=[
        ex("Escribe qué es la procedencia.", "De dónde viene algo", "Es la definición."),
        ex("Verdadero o falso: puedo pedir todo lo que quiera en una entrevista.", "Falso", "Siempre hay límites."),
        ex("¿Qué haces con lo que la fuente no cuenta?", "Lo anoto como límite", "No se inventa."),
    ],
    task=T("Lee la ficha inventada: «Comida: sopa de la fiesta de la cosecha de Valle Alto. La cuenta doña Rosa. Se prepara con lo que da la huerta. Significado: agradecer la cosecha. Límite: la receta exacta la guarda la familia.» Escribe tres preguntas de entrevista para doña Rosa: una sobre procedencia, una sobre significado y una sobre lo que se puede compartir. Escribe un agradecimiento. Añade una pregunta para el educador tradicional sobre una comida de tu zona.",
           "1 ¿De dónde viene la sopa? 2 ¿Para qué se prepara? 3 ¿Qué podemos conocer de ella? Gracias, doña Rosa. Pregunta: ¿qué comidas de nuestra zona se pueden conocer y cuidar con respeto?",
           ["escribe tres preguntas distintas", "agradece", "respeta el límite"], ["tres preguntas", "agradecimiento"], ["pedir la receta exacta", "preguntas de opinión"],
           "Revisar que cada pregunta pida un dato distinto; valorar que respete el límite."),
    reinforce="Cambia una pregunta de opinión por una que pida un dato.",
    extend="Escribe cómo registrarías las respuestas de una entrevista sin cambiar lo que dijo la persona.",
)

L(
    OA14, 3,
    materials="Lápiz y hojas. La lista de lugares está escrita aquí y es inventada.",
    use="Aprenderé a distinguir el patrimonio de acceso público y el restringido y cómo comportarme con cada uno. Sirve para visitar y cuidar sin dañar.",
    prior=["Sé que hay cosas que se resguardan.", "Sé qué es el consentimiento."],
    explain=[
        "Algunos lugares y prácticas son de acceso público: cualquier persona puede visitarlos o conocerlos, como una plaza o una feria. Otros son restringidos: solo ciertas personas pueden entrar o participar, porque son delicados o muy importantes.",
        "Los sitios arqueológicos están protegidos por una ley. No se excava, no se llevan objetos y no se escribe en ellos. Si encuentras una pieza antigua, no la tomes: avisa a una persona adulta o a la escuela. Una pieza fuera de su lugar pierde su historia.",
        "Algunas ceremonias y espacios sagrados son restringidos porque la comunidad decide resguardarlos. Aunque tengamos curiosidad, no entramos, no grabamos y no publicamos sin permiso. En esta clase usamos una lista inventada.",
    ],
    vocab=[("acceso público", "que cualquier persona puede visitar o conocer"), ("acceso restringido", "que solo ciertas personas pueden visitar o conocer"), ("protegido", "cuidado por una ley o por una comunidad"), ("pieza", "objeto antiguo encontrado en un lugar"), ("sitio arqueológico", "lugar con restos de personas que vivieron hace mucho")],
    worked=[
        W("Clasificar el acceso", "Lista inventada: 1) la plaza de Valle Alto, abierta a todos, 2) un sitio arqueológico, 3) un lugar de ceremonias solo para la comunidad. ¿Cuál es de acceso público?", ["La plaza está abierta a todos.", "El sitio arqueológico está protegido.", "El lugar de ceremonias es solo de la comunidad."], "La 1, la plaza."),
        W("Qué hacer con una pieza", "Un niño encuentra una piedra con marcas muy antigua en un cerro. ¿Qué hace?", ["No la toma.", "Avisa a una persona adulta.", "La deja donde está."], "No la toma y avisa a una persona adulta."),
    ],
    mistakes=[
        M("Llevarse una pieza antigua de recuerdo.", "Pierde su historia y está protegida.", "Déjala donde está y avisa a un adulto."),
        M("Pensar que todo lugar se puede visitar.", "Algunos son restringidos.", "Pregunta si se puede."),
    ],
    R=[
        ex("Una plaza abierta a todos, ¿es de acceso público o restringido?", "Público", "Cualquiera puede ir."),
        ex("Si encuentras una piedra muy antigua en el campo, ¿la tomas o avisas a un adulto?", "Avisas a un adulto", "Las piezas están protegidas."),
        ex("Un lugar de ceremonias solo para la comunidad, ¿es público o restringido?", "Restringido", "Solo entra la comunidad."),
    ],
    C=[
        ex("¿Qué es un sitio arqueológico? A) un lugar con restos de personas que vivieron hace mucho B) un parque nuevo", "A", "Es un lugar con restos antiguos."),
        ex("Verdadero o falso: puedes llevarte una pieza de un sitio arqueológico de recuerdo.", "Falso", "Están protegidos por ley."),
        ex("Verdadero o falso: una comunidad puede decidir que un lugar sea restringido.", "Verdadero", "Es parte de su resguardo."),
    ],
    A=[
        ex("Clasifica en PÚBLICO o RESTRINGIDO: a) una feria abierta b) un lugar de ceremonias solo para la comunidad c) una plaza.", "a público, b restringido, c público", "La feria y la plaza son abiertas."),
        arith("En una lista de 5 lugares, 2 son restringidos. ¿Cuántos son de acceso público?", "5-2", "Se restan los restringidos."),
        ex("Une cada acción con su comportamiento correcto. 1) pieza antigua 2) lugar restringido 3) plaza pública a) avisar a un adulto b) no entrar c) visitar con respeto", "1-a, 2-b, 3-c", "Cada lugar tiene su comportamiento."),
    ],
    Z=[
        ex("Tomás dice: «Si nadie me ve, puedo llevarme la pieza». ¿Qué error comete?", "Las piezas están protegidas", "Se pierde su historia aunque nadie vea."),
        ex("Ema dice que puede subir al lugar restringido si lo hace en silencio. ¿Es correcto? Responde Sí o No.", "No", "El acceso restringido se respeta siempre."),
    ],
    D=[
        ex("Dos niñas: una visita la plaza pública y otra quiere entrar a un lugar restringido «solo a mirar». ¿Cuál respeta el acceso?", "La primera", "La segunda no respeta la restricción."),
        ex("Quieres saber qué lugares de tu zona son públicos y cuáles restringidos. ¿A quién consultas? A) al educador tradicional B) a nadie", "A", "Él o ella orienta."),
    ],
    context=[ex("En una excursión, tu curso ve un cartel que dice que un sitio está protegido. ¿Qué haces? A) obedecer el cartel B) entrar para ver", "A", "Se respeta la protección.")],
    selfcheck=[
        ex("Escribe la diferencia entre público y restringido.", "Público lo puede visitar cualquiera; restringido, solo ciertas personas", "Es la idea central."),
        ex("Verdadero o falso: puedo tomar una pieza antigua si es pequeña.", "Falso", "Está protegida por ley."),
        ex("¿Qué haces si encuentras una pieza antigua?", "No la tomo y aviso a un adulto", "Así se protege."),
    ],
    task=T("Con la lista inventada de Valle Alto: la plaza abierta, un sitio arqueológico cerrado con un cartel que dice «No pasar», un lugar de ceremonias solo para la comunidad y una feria abierta, haz una tabla con dos columnas: «Público» y «Restringido». Escribe una regla de comportamiento para cada lugar. Añade una pregunta para el educador tradicional sobre cómo visitar con respeto los lugares de tu zona.",
           "Público: la plaza y la feria (visitar con respeto). Restringido: el sitio arqueológico cerrado (no entrar ni llevarse piezas) y el lugar de ceremonias (no entrar). Pregunta: ¿cómo debemos visitar los lugares importantes de nuestra zona?",
           ["clasifica los cuatro lugares", "escribe una regla por lugar", "formula una pregunta"], ["tabla", "reglas", "pregunta"], ["decir que se puede entrar a lo restringido", "llevarse piezas"],
           "Preguntar por qué cada lugar está en su columna; valorar las reglas."),
    reinforce="Escribe tres reglas de respeto para una visita a un sitio protegido.",
    extend="Diseña un cartel breve para un sitio protegido inventado que explique qué no hacer.",
)

L(
    OA14, 4,
    materials="Hojas, lápiz y colores. La ficha de permiso está escrita aquí y es inventada.",
    use="Aprenderé a recrear solo lo que está autorizado, dando crédito y sin copiar lo restringido. Sirve para valorar sin apropiarme.",
    prior=["Sé distinguir lo público de lo restringido.", "Sé qué es apropiarse."],
    explain=[
        "Recrear es volver a crear algo con tus manos a partir de lo que aprendiste. Puedes hacer un dibujo, una maqueta o un libro. Pero no todo se puede recrear: solo lo que la fuente autoriza.",
        "Antes de recrear nos hacemos cuatro preguntas: ¿hay permiso?, ¿es público o restringido?, ¿quién es la fuente? y ¿cómo doy crédito? Si falta una respuesta, nos detenemos y preguntamos.",
        "Recrear no es imitar una ceremonia ni copiar un diseño familiar. Podemos recrear un espacio público, como una plaza, o hacer un libro con lo que la fuente contó y autorizó. En esta clase usamos una ficha inventada con permiso.",
    ],
    vocab=[("recrear", "volver a crear algo con tus manos a partir de lo que aprendiste"), ("autorizado", "que tiene permiso"), ("crédito", "reconocimiento a quien enseñó"), ("maqueta", "modelo pequeño de un lugar o cosa"), ("copiar", "repetir sin permiso lo que hizo otra persona")],
    worked=[
        W("Revisar los cuatro pasos", "Ficha inventada: «La plaza de Valle Alto puede dibujarse y mostrarse. Lo autoriza doña Rosa. Los lugares de ceremonias no se dibujan.» ¿Qué puedes recrear?", ["Busco qué está autorizado.", "La plaza.", "Los lugares de ceremonias no."], "La plaza."),
        W("Dar crédito", "Escribe una frase de crédito para tu dibujo de la plaza.", ["Digo qué es.", "Digo quién lo autorizó.", "Agradezco."], "Dibujo de la plaza de Valle Alto, autorizado por doña Rosa. Gracias."),
    ],
    mistakes=[
        M("Dibujar una ceremonia para «completar» un trabajo.", "Es restringido y puede ser falso.", "Recrea solo lo autorizado."),
        M("No poner de dónde viene lo que recreas.", "Falta el crédito.", "Escribe la fuente y la comunidad."),
    ],
    R=[
        ex("Según la ficha, ¿puedes dibujar la plaza? Responde Sí o No.", "Sí", "La ficha lo autoriza."),
        ex("Según la ficha, ¿puedes dibujar los lugares de ceremonias? Responde Sí o No.", "No", "La ficha lo prohíbe."),
        ex("¿Quién autoriza el dibujo de la plaza?", "Doña Rosa", "Es la fuente."),
    ],
    C=[
        ex("¿Qué es recrear? A) volver a crear algo a partir de lo que aprendiste B) tomar sin permiso", "A", "Es crear con tus manos."),
        ex("Verdadero o falso: se puede recrear todo lo que se ve en una foto.", "Falso", "Solo lo autorizado."),
        ex("Verdadero o falso: al recrear se debe dar crédito.", "Verdadero", "Se reconoce la fuente."),
    ],
    A=[
        ex("Clasifica en SE PUEDE o NO SE PUEDE recrear según la ficha: a) la plaza b) un lugar de ceremonias c) la plaza dibujada para mostrarla en la escuela.", "a se puede, b no se puede, c se puede", "Solo lo autorizado se recrea: la plaza sí, el lugar de ceremonias no."),
        ex("Completa la frase de crédito: «Dibujo de la plaza de Valle Alto, autorizado por ___ ». Escribe el nombre.", "Doña Rosa", "La ficha dice quién autoriza."),
        arith("Un libro del curso tiene 6 páginas con temas autorizados y 2 páginas con temas que no se pueden incluir. Si el curso decide quitar las 2 que no se pueden incluir, ¿cuántas páginas quedan en el libro?", "6", "Quedan las 6 páginas autorizadas."),
    ],
    Z=[
        ex("Pedro dibuja una ceremonia porque «se ve bonita». ¿Qué error comete?", "Recrea algo restringido", "No está autorizado."),
        ex("Ema hace una maqueta de la plaza y escribe de dónde sacó el dato. ¿Actúa bien? Responde Sí o No.", "Sí", "Recrea lo autorizado y da crédito."),
    ],
    D=[
        ex("Dos trabajos: 1) un dibujo de la plaza autorizado y con crédito; 2) un dibujo de una ceremonia sin permiso. ¿Cuál valora sin apropiarse?", "El 1", "El 2 no tiene permiso."),
        ex("Quieres recrear algo de tu comunidad real. ¿Qué haces primero? A) preguntar si está autorizado B) dibujarlo sin avisar", "A", "El permiso es lo primero."),
    ],
    context=[ex("Tu curso hará una exposición con dibujos de la plaza de Valle Alto (inventada). ¿Qué incluye cada dibujo? A) un crédito con la fuente B) nada", "A", "Reconoce quién autorizó.")],
    selfcheck=[
        ex("Escribe las cuatro preguntas antes de recrear.", "¿Hay permiso?, ¿es público o restringido?, ¿quién es la fuente? y ¿cómo doy crédito?", "Son las cuatro de la clase."),
        ex("Verdadero o falso: puedo imitar una ceremonia si me interesa.", "Falso", "Eso es restringido."),
        ex("¿Qué escribes en un dibujo recreado?", "La comunidad, la fuente y un agradecimiento", "Es el crédito."),
    ],
    task=T("Según la ficha inventada (se puede dibujar la plaza de Valle Alto, autorizada por doña Rosa; los lugares de ceremonias no), haz un dibujo de la plaza con un árbol, bancas y gente conversando. Escribe una tarjeta de crédito: qué es, comunidad, quién autorizó y un agradecimiento. Escribe qué NO dibujaste y por qué. Añade una pregunta para el educador tradicional sobre qué se puede recrear de tu comunidad.",
           "Dibujo de la plaza con árbol, bancas y gente. Tarjeta: plaza de Valle Alto, autorizada por doña Rosa. Gracias. No dibujé lugares de ceremonias porque son restringidos. Pregunta: ¿qué de nuestra comunidad podemos recrear con respeto?",
           ["dibuja solo lo autorizado", "escribe la tarjeta de crédito", "explica qué no dibujó"], ["dibujo", "tarjeta", "pregunta"], ["dibujar ceremonias", "omitir el crédito"],
           "Preguntar por qué no dibujó ciertos lugares; valorar el crédito."),
    reinforce="Subraya en la ficha lo que se puede recrear y lo que no.",
    extend="Haz una maqueta pequeña de un patio inventado y escribe su tarjeta de crédito.",
)

L(
    OA14, 5,
    materials="Hojas y lápiz. Las opciones de acción están escritas aquí. No se usan objetos peligrosos.",
    use="Aprenderé a diseñar una acción para valorar y cuidar el patrimonio de mi comunidad, con pasos claros y respeto. Sirve para pasar de aprender a cuidar.",
    prior=["Sé distinguir lo público de lo restringido.", "Sé recrear solo lo autorizado."],
    explain=[
        "Una acción de valoración y cuidado es algo que hacemos para que el patrimonio se conozca y se proteja. Puede ser una exposición, un cartel, una charla con el educador tradicional o una campaña para no dejar basura en un lugar público.",
        "Para diseñarla, respondemos: ¿qué patrimonio?, ¿qué haremos?, ¿quién ayuda?, ¿cuándo? y ¿qué permisos necesitamos? Así evitamos improvisar y respetamos a la comunidad.",
        "No decidimos por la comunidad. Proponemos y preguntamos. Si la comunidad dice que no, cambiamos la acción. En esta clase usamos opciones inventadas y casos de práctica. El patrimonio real lo cuenta la comunidad.",
    ],
    vocab=[("acción", "algo que se hace para lograr un objetivo"), ("campaña", "serie de acciones para lograr un objetivo"), ("exposición", "muestra de trabajos para que otros los vean"), ("plan", "lista de pasos para lograr algo"), ("proteger", "cuidar para que no se dañe")],
    worked=[
        W("Armar un plan", "Acción inventada: exposición de dibujos de la plaza de Valle Alto en la escuela. ¿Qué dato falta para que sea un plan?", ["Dice qué: exposición.", "Falta quién ayuda y cuándo.", "También el permiso."], "Quién ayuda, cuándo y el permiso."),
        W("Revisar el permiso", "Si doña Rosa autoriza solo mostrar dibujos de la plaza, ¿puedes agregar un dibujo de un lugar de ceremonias a la exposición?", ["La autorización es solo para la plaza.", "El lugar de ceremonias no está autorizado.", "No se puede."], "No."),
    ],
    mistakes=[
        M("Hacer una exposición sin preguntar a la comunidad.", "Puede mostrar cosas que no se pueden mostrar.", "Pregunta y pide permiso."),
        M("Planear sin decir cuándo y quién.", "No se puede cumplir.", "Escribe responsable y fecha."),
    ],
    R=[
        ex("¿Una exposición de dibujos autorizados es una acción de valoración? Responde Sí o No.", "Sí", "Muestra el patrimonio con respeto."),
        ex("Un plan, ¿tiene pasos o es solo una idea?", "Tiene pasos", "Es una lista de pasos."),
        ex("¿Qué necesitas antes de mostrar algo de la comunidad? A) permiso B) un premio", "A", "El permiso es primero."),
    ],
    C=[
        ex("Verdadero o falso: puedo decidir por la comunidad cómo cuidar su patrimonio.", "Falso", "Proponemos y preguntamos."),
        ex("¿Qué es una campaña? A) serie de acciones para lograr un objetivo B) una sola idea", "A", "Tiene varias acciones."),
        ex("Verdadero o falso: si la comunidad dice que no, cambio la acción.", "Verdadero", "Respetamos su decisión."),
    ],
    A=[
        ex("Un plan dice: «Qué patrimonio: la plaza. Qué haremos: un cartel. Cuándo: la próxima semana.» ¿Qué dos preguntas faltan? A) quién ayuda y qué permisos B) qué patrimonio y cuándo", "A", "Esas dos no están respondidas."),
        ex("Completa: «Acción: exposición. Cuándo: la última semana del mes. Quién ayuda: el curso. Qué falta: ___ ». Elige. A) el permiso B) un tambor", "A", "El permiso es lo que falta."),
        ex("Clasifica en CUIDA o NO CUIDA: a) pedir permiso b) dejar basura en un lugar público c) invitar a una charla al educador.", "a cuida, b no cuida, c cuida", "Dejar basura daña el lugar."),
    ],
    Z=[
        ex("Tomás organiza una exposición sin avisar a la comunidad. ¿Qué paso omite?", "Pedir permiso", "El permiso es necesario."),
        ex("Ema planea la acción pero no escribe quién será responsable. ¿Qué problema puede haber?", "Nadie se hace cargo", "Sin responsable no se cumple."),
    ],
    D=[
        ex("Dos planes: 1) una campaña para no dejar basura en la plaza, con responsables y fecha; 2) una charla improvisada sin avisar. ¿Cuál es mejor?", "El 1", "Está bien organizado."),
        ex("Si la comunidad propone cambiar tu plan, ¿lo cambias? Responde Sí o No.", "Sí", "Se respeta su decisión."),
    ],
    context=[ex("Tu curso quiere cuidar la plaza del pueblo. ¿Qué acción es segura y adecuada? A) recoger la basura con bolsa y guantes con un adulto B) pintar una pared de un sitio protegido", "A", "Cuida sin dañar.")],
    selfcheck=[
        ex("Escribe tres preguntas de un plan.", "Tres de estas: qué patrimonio, qué haremos, quién ayuda, cuándo, qué permisos", "Son las preguntas de la clase."),
        ex("Verdadero o falso: un buen plan incluye quién ayuda y cuándo.", "Verdadero", "Así se puede cumplir."),
        ex("¿Qué haces si la comunidad dice que no?", "Cambio la acción", "Se respeta su decisión."),
    ],
    task=T("Elige UNA acción: A) exposición de dibujos autorizados de la plaza de Valle Alto (inventada), B) campaña para recoger basura de una plaza pública con bolsa y guantes junto a un adulto, C) invitar al educador tradicional a conversar con el curso. Completa un plan con cinco datos: qué patrimonio, qué haremos, quién ayuda, cuándo y qué permisos. Escribe cómo cuidas la seguridad y una pregunta para el educador tradicional.",
           "Elijo B. Patrimonio: plaza pública. Haremos: recoger basura. Ayuda: el curso y un adulto. Cuándo: el viernes. Permisos: de la escuela y del adulto. Seguridad: bolsa y guantes. Pregunta: ¿cómo podemos cuidar mejor nuestros lugares públicos?",
           ["completa los cinco datos", "cuida la seguridad", "formula una pregunta"], ["plan de cinco datos", "frase de seguridad", "pregunta"], ["omitir permisos", "proponer algo peligroso"],
           "Preguntar quién hará cada tarea; valorar la seguridad."),
    reinforce="Escribe tres acciones que tu curso podría hacer para cuidar un lugar público.",
    extend="Diseña un afiche para invitar a otros cursos a la acción que elegiste.",
)

# ============================================================ OA 15 · Ciencia indígena en relación con naturaleza y cosmos
L(
    OA15, 1,
    materials="Lápiz y hojas. El relato está escrito aquí y es inventado.",
    use="Aprenderé a situar una pregunta y una perspectiva: de qué comunidad viene un saber sobre la naturaleza y cómo se construye. Sirve para respetar distintas maneras de conocer.",
    prior=["Sé que cada comunidad tiene su manera de vivir.", "Sé que la ciencia escolar se basa en observar y preguntar."],
    explain=[
        "La ciencia empieza con una pregunta sobre cómo funciona la naturaleza. Se responde observando, anotando y comparando. En la escuela aprendemos ciencia escolar. Muchas comunidades han observado la naturaleza durante generaciones y han construido conocimientos propios.",
        "Una perspectiva es una manera de mirar un tema. La perspectiva de una comunidad indígena sobre la naturaleza y el cosmos la cuenta la propia comunidad. Hay que situarla: ¿de qué comunidad es?, ¿quién la cuenta? y ¿hay permiso?",
        "En esta clase usamos un relato inventado de Valle Alto. No es ciencia de ningún pueblo real. El cosmos es todo lo que existe en el cielo y más allá: el Sol, la Luna, las estrellas y los planetas. Nunca mires el Sol directamente.",
    ],
    vocab=[("ciencia", "forma de conocer la naturaleza observando, anotando y comparando"), ("perspectiva", "manera particular de mirar un tema"), ("cosmos", "todo lo que existe en el cielo y más allá"), ("observación", "mirar con atención y anotar"), ("generación", "grupo de personas de edades parecidas")],
    worked=[
        W("Situar la pregunta", "Relato inventado: «En Valle Alto los vecinos se preguntan: ¿cuándo florece el árbol del patio? Lo cuenta doña Rosa. Permiso: sí.» ¿Cuál es la pregunta?", ["Busco el signo de pregunta.", "Dice ¿cuándo florece el árbol?", "Respondo."], "¿Cuándo florece el árbol del patio?"),
        W("Distinguir perspectivas", "La escuela explica que las estaciones cambian porque la Tierra gira alrededor del Sol. Valle Alto (inventado) dice que sabe que llega la primavera porque florece el árbol. ¿Son la misma perspectiva?", ["Una explica con lo que se aprende en la escuela.", "La otra se apoya en la observación de la comunidad.", "No son la misma."], "No: son perspectivas distintas."),
    ],
    mistakes=[
        M("Decir que el saber de una comunidad «no es ciencia» o «es más científico».", "Es jerarquizar.", "Describe cómo se conoce, sin decir cuál vale más."),
        M("Mirar el Sol directamente para observarlo.", "Daña los ojos.", "Observa solo sombras o el cielo sin mirar el Sol."),
    ],
    R=[
        ex("En el relato, ¿qué pregunta se hacen los vecinos de Valle Alto? A) ¿Cuándo florece el árbol del patio? B) ¿Cuánto cuesta el árbol?", "A", "El relato lo dice."),
        ex("¿Quién cuenta el relato?", "Doña Rosa", "Es la fuente."),
        ex("¿Se puede mirar el Sol directamente para observarlo? Responde Sí o No.", "No", "Daña los ojos."),
    ],
    C=[
        ex("¿Qué es una perspectiva? A) una manera particular de mirar un tema B) un instrumento", "A", "Es un punto de vista."),
        ex("Verdadero o falso: la ciencia empieza con una pregunta sobre la naturaleza.", "Verdadero", "Se pregunta y se observa."),
        ex("Verdadero o falso: el relato de Valle Alto es ciencia de un pueblo real.", "Falso", "Es un relato inventado."),
    ],
    A=[
        ex("Clasifica en PREGUNTA u OPINIÓN: a) ¿cuándo florece el árbol? b) el árbol es hermoso c) ¿cuánto dura el invierno?", "a pregunta, b opinión, c pregunta", "Las preguntas piden datos."),
        ex("Un relato dice: «En Valle Alto se preguntan cuándo florece el árbol. Lo cuenta doña Rosa.» ¿Qué dato de situación no está escrito: el permiso o la fuente?", "El permiso", "La comunidad y la fuente están; el permiso no."),
        ex("Une cada pregunta con su fuente posible. 1) ¿Por qué cambian las estaciones? 2) ¿Cuándo florece el árbol del patio de Valle Alto? a) ciencia escolar b) doña Rosa", "1-a, 2-b", "Cada pregunta se responde con su fuente."),
    ],
    Z=[
        ex("Pedro dice: «El saber de la comunidad no es ciencia». ¿Qué error comete?", "Jerarquiza sin describir cómo se conoce", "Cada manera tiene su forma de conocer."),
        ex("Ema dice que doña Rosa representa a todos los pueblos. ¿Qué error comete?", "Generaliza un relato inventado", "Es un personaje inventado."),
    ],
    D=[
        ex("Dos niñas: una pregunta «¿cuándo florece el árbol?» y observa; otra dice «seguro florece en septiembre» sin observar. ¿Quién actúa como la ciencia escolar?", "La primera", "Observa antes de afirmar."),
        ex("Para conocer la perspectiva de tu comunidad sobre la naturaleza, ¿a quién consultas? A) al educador tradicional B) a nadie", "A", "Él o ella es la fuente."),
    ],
    context=[ex("Tu curso quiere saber cuándo florece un árbol del patio. ¿Qué hacen? A) observar y anotar por semanas B) adivinar", "A", "Así se construye conocimiento.")],
    selfcheck=[
        ex("Escribe qué es el cosmos.", "Todo lo que existe en el cielo y más allá", "Es la definición."),
        ex("Verdadero o falso: puedo mirar el Sol directamente.", "Falso", "Daña los ojos."),
        ex("¿Qué haces para situar una perspectiva?", "Digo de qué comunidad es, quién la cuenta y si hay permiso", "Así se sitúa."),
    ],
    task=T("Lee el relato inventado: «En Valle Alto se preguntan cuándo florece el árbol del patio. Lo cuenta doña Rosa y autoriza compartirlo.» Haz una ficha con cuatro líneas: pregunta, comunidad, fuente y permiso. Escribe una pregunta de ciencia escolar sobre las estaciones. Escribe una pregunta para el educador tradicional. No mires el Sol directamente.",
           "Pregunta: ¿cuándo florece el árbol del patio? Comunidad: Valle Alto. Fuente: doña Rosa. Permiso: sí. Pregunta escolar: ¿por qué cambian las estaciones? Pregunta al educador: ¿qué observa nuestra comunidad para conocer los cambios del año?",
           ["completa la ficha", "formula dos preguntas distintas", "no mezcla fuentes"], ["ficha de cuatro líneas", "dos preguntas"], ["mezclar el relato inventado con ciencia escolar", "mirar el Sol"],
           "Preguntar de qué fuente viene cada pregunta; reforzar la seguridad con el Sol."),
    reinforce="Escribe tres preguntas sobre la naturaleza que se pueden responder observando.",
    extend="Escribe cómo registrarías tus observaciones del árbol del patio durante dos meses.",
)

L(
    OA15, 2,
    materials="Lápiz y hojas. Las tablas de observación están escritas aquí y son inventadas.",
    use="Aprenderé a examinar cómo la observación repetida produce conocimiento y a distinguir lo que veo de lo que supongo. Sirve para construir evidencia.",
    prior=["Sé situar una pregunta y una perspectiva.", "Sé leer una tabla."],
    explain=[
        "Observar es mirar con atención y anotar lo que se ve. Si observamos una vez, solo sabemos un momento. Si observamos muchas veces, podemos ver patrones, que son cosas que se repiten. Esas repeticiones forman conocimiento.",
        "La evidencia son los datos que sustentan una afirmación. Si decimos que en invierno hay más días con lluvia, la evidencia es una tabla con los días observados. Una afirmación sin evidencia es solo una suposición.",
        "Los conocimientos de las comunidades también nacen de observar muchas veces durante generaciones. Cómo lo hace una comunidad real lo cuenta ella misma. En esta clase usamos tablas inventadas para practicar.",
    ],
    vocab=[("patrón", "algo que se repite de manera ordenada"), ("evidencia", "datos que sustentan una afirmación"), ("registro", "lista o tabla donde se anotan datos"), ("suposición", "idea que no tiene datos que la apoyen"), ("transmitir", "pasar un conocimiento de una persona a otra")],
    worked=[
        W("Leer una tabla", "Tabla inventada de 7 días: lun lluvia, mar nublado, mié lluvia, jue despejado, vie despejado, sáb lluvia, dom nublado. ¿Cuántos días llovió?", ["Busco los días de lluvia.", "Lunes, miércoles y sábado.", "Son 3."], "3 días."),
        W("Evidencia o suposición", "Un niño dice: «Siempre llueve los lunes». ¿La tabla lo prueba?", ["Solo hay una semana.", "Un lunes con lluvia no basta.", "Es una suposición."], "No, es una suposición."),
    ],
    mistakes=[
        M("Afirmar un patrón con una sola observación.", "Una vez no basta.", "Observa muchas veces."),
        M("Anotar lo que debería pasar y no lo que se ve.", "El registro debe ser real.", "Anota solo lo observado."),
    ],
    R=[
        ex("En la tabla inventada, ¿qué hubo el jueves: lluvia o despejado?", "Despejado", "La tabla lo dice."),
        ex("¿Qué es un registro? A) una tabla donde se anotan datos B) un juego", "A", "Es donde se anota."),
        ex("Una suposición, ¿tiene datos que la apoyan o no?", "No", "Por eso es suposición."),
    ],
    C=[
        ex("Verdadero o falso: con una sola observación puedo afirmar un patrón.", "Falso", "Hay que observar muchas veces."),
        ex("¿Qué es la evidencia? A) datos que sustentan una afirmación B) una opinión", "A", "Es la base."),
        ex("Verdadero o falso: los conocimientos pueden nacer de observar muchas veces durante generaciones.", "Verdadero", "Así se construye el saber."),
    ],
    A=[
        ex("En la tabla de 7 días, ¿cuántos días estuvo despejado?", "2", "Jueves y viernes."),
        ex("En la tabla, ¿cuántos días hubo nubes (nublado)? Escribe el número.", "2", "Martes y domingo."),
        ex("Clasifica en EVIDENCIA o SUPOSICIÓN: a) llovió 3 días en esa semana b) siempre va a llover los lunes.", "a evidencia, b suposición", "Lo primero está en la tabla."),
    ],
    Z=[
        ex("Tomás observó un día y dice que «en esta ciudad nunca llueve». ¿Qué error comete?", "Generaliza con una sola observación", "Faltan más días."),
        ex("Ema anotó «lluvia» el martes aunque estaba nublado, porque «seguro iba a llover». ¿Qué error comete?", "Anotó lo que supuso", "El registro es lo observado."),
    ],
    D=[
        arith("En otra tabla inventada llovió 3 días la primera semana y 4 la segunda. ¿Cuántos días llovió en total?", "3+4", "Se suman las dos semanas."),
        ex("Para tener mejor evidencia, ¿qué haces? A) observar más semanas B) dejar de observar", "A", "Más datos dan más seguridad."),
    ],
    context=[ex("Tu curso observa la lluvia durante un mes. ¿Qué anotan cada día? A) lo que realmente ven B) lo que quisieran que pasara", "A", "Es el registro real.")],
    selfcheck=[
        ex("Escribe qué es un patrón.", "Algo que se repite de manera ordenada", "Es la definición."),
        ex("Verdadero o falso: una suposición es lo mismo que una evidencia.", "Falso", "La suposición no tiene datos."),
        ex("¿Qué haces para tener mejor evidencia?", "Observo muchas veces y anoto", "Más datos, más seguridad."),
    ],
    task=T("Con esta tabla inventada de 7 días: lun lluvia, mar nublado, mié lluvia, jue despejado, vie despejado, sáb lluvia, dom nublado, cuenta cuántos días hubo de cada tipo y escribe dos afirmaciones que sí tengan evidencia y una que sea suposición. Después observa el cielo de tu casa o escuela 3 días (sin mirar el Sol directamente) y registra lo que ves. Añade una pregunta para el educador tradicional sobre qué observa su comunidad del clima.",
           "Lluvia: 3. Nublado: 2. Despejado: 2. Evidencia: llovió 3 días; hubo 2 despejados. Suposición: siempre llueve los lunes. Mi registro: día 1 nublado, día 2 despejado, día 3 nublado. Pregunta: ¿qué observa nuestra comunidad para conocer el clima?",
           ["cuenta correctamente", "distingue evidencia y suposición", "registra lo que realmente ve"], ["conteo", "afirmaciones", "registro propio"], ["afirmar un patrón con una semana", "mirar el Sol"],
           "Revisar el conteo; preguntar por qué la última afirmación es suposición."),
    reinforce="Cuenta de nuevo los días de la tabla y comprueba que suman 7.",
    extend="Escribe una pregunta que podrías responder observando durante un mes.",
)

L(
    OA15, 3,
    materials="Lápiz y hojas. Si deseas, observa la Luna en la noche con una persona adulta. No mires el Sol directamente.",
    use="Aprenderé a relacionar la naturaleza con el cosmos, usando hechos de la ciencia escolar y un relato inventado. Sirve para ver cómo el cielo y la tierra se conectan.",
    prior=["Sé situar una pregunta y una perspectiva.", "Sé qué es un patrón."],
    explain=[
        "El cosmos incluye el Sol, la Luna y las estrellas. En la ciencia escolar sabemos que la Tierra gira sobre sí misma, y por eso hay día y noche. También sabemos que la Tierra se mueve alrededor del Sol durante un año, y por eso hay estaciones.",
        "Además, la inclinación de la Tierra influye en las estaciones; eso se estudia más adelante. La Luna cambia de forma en el cielo. Se ve llena, luego va menguando, después casi desaparece y vuelve a crecer. Ese ciclo dura cerca de un mes. Es un patrón que se puede observar desde la casa con un adulto, de noche.",
        "En esta clase usamos hechos de la ciencia escolar y un relato inventado de Valle Alto. El relato dice: «Cuando la Luna está llena, los vecinos conversan más tarde». Es solo una práctica. Cómo una comunidad real relaciona el cielo con la vida lo cuenta ella misma.",
    ],
    vocab=[("cosmos", "todo lo que existe en el cielo y más allá"), ("Luna", "astro que vemos de noche y cambia de forma"), ("estación", "cada una de las cuatro partes del año"), ("ciclo", "serie de pasos que se repite"), ("astro", "cuerpo del cielo, como el Sol, la Luna o una estrella")],
    worked=[
        W("Día y noche", "La Tierra gira sobre sí misma. ¿Qué ocurre por eso?", ["La Tierra gira.", "Una parte mira al Sol y otra no.", "Hay día y noche."], "Hay día y noche."),
        W("Ciclo de la Luna", "La Luna tarda cerca de un mes en volver a verse igual. ¿Es un ciclo?", ["Se repite.", "Vuelve a verse igual.", "Sí es un ciclo."], "Sí, es un ciclo."),
    ],
    mistakes=[
        M("Pensar que la Luna desaparece de verdad.", "Cambia lo que vemos de ella, pero sigue ahí.", "Observa varios días."),
        M("Mirar el Sol directamente.", "Daña los ojos.", "Nunca lo mires."),
    ],
    R=[
        ex("¿Por qué hay día y noche? A) porque la Tierra gira sobre sí misma B) porque el Sol se apaga", "A", "Así una parte recibe luz y otra no."),
        ex("¿Cuánto dura aproximadamente el ciclo de la Luna: cerca de un mes o cerca de un día?", "Cerca de un mes", "Eso dice la ciencia escolar."),
        ex("¿Se puede mirar el Sol directamente? Responde Sí o No.", "No", "Daña los ojos."),
    ],
    C=[
        ex("Verdadero o falso: las estaciones ocurren porque la Tierra se mueve alrededor del Sol durante un año.", "Verdadero", "Es el hecho de la ciencia escolar."),
        ex("¿Qué es un astro? A) un cuerpo del cielo, como el Sol o la Luna B) un animal", "A", "Son cuerpos del cielo."),
        ex("Verdadero o falso: el relato de Valle Alto sobre la Luna llena es de un pueblo real.", "Falso", "Es un relato inventado."),
    ],
    A=[
        ex("Clasifica en CIENCIA ESCOLAR o RELATO INVENTADO: a) la Tierra gira y hay día y noche b) con Luna llena los vecinos conversan más tarde.", "a ciencia escolar, b relato inventado", "Cada uno viene de su fuente."),
        ex("Ordena el ciclo de la Luna: a) vuelve a crecer b) llena c) casi desaparece d) va menguando. Escribe las letras.", "b, d, c, a", "Llena, mengua, casi desaparece y crece."),
        arith("Si el ciclo de la Luna dura cerca de 30 días y observas 2 ciclos, ¿cuántos días son aproximadamente?", "30*2", "Se repite 30 días dos veces."),
    ],
    Z=[
        ex("Pedro dice que la ciencia escolar confirma el relato de la Luna llena de Valle Alto. ¿Qué error comete?", "Mezcla dos fuentes", "El relato es inventado y no se prueba con ciencia."),
        ex("Ema observa la Luna una sola noche y dice que «siempre se ve así». ¿Qué error comete?", "Generaliza con una sola observación", "La Luna cambia."),
    ],
    D=[
        ex("Dos niños: uno anota la forma de la Luna cada noche por una semana; otro solo imagina. ¿Cuál construye evidencia?", "El primero", "Registra lo que ve."),
        ex("¿Qué debes hacer para observar la Luna de noche? A) hacerlo con una persona adulta B) salir solo a oscuras", "A", "Es más seguro."),
    ],
    context=[ex("Tu curso dibuja la forma de la Luna cada noche durante una semana con ayuda de una persona adulta. ¿Qué logran ver? A) cómo cambia de forma B) que se apaga", "A", "Es su ciclo.")],
    selfcheck=[
        ex("Escribe por qué hay día y noche.", "Porque la Tierra gira sobre sí misma", "Es el hecho de la ciencia escolar."),
        ex("Verdadero o falso: la Luna se apaga de verdad cuando casi no se ve.", "Falso", "Cambia lo que vemos de ella."),
        ex("¿Qué haces con un relato inventado y con un hecho de ciencia escolar?", "Los mantengo separados y digo de dónde viene cada uno", "No se mezclan."),
    ],
    task=T("En una tabla de dos columnas escribe «Ciencia escolar» y «Relato inventado de Valle Alto». En la primera escribe dos hechos: día y noche por el giro de la Tierra y el ciclo de la Luna de cerca de un mes. En la segunda escribe el relato de la Luna llena. Si puedes, con una persona adulta observa la Luna una noche y dibuja su forma. No mires el Sol. Añade una pregunta para el educador tradicional sobre qué observa su comunidad del cielo.",
           "Ciencia escolar: la Tierra gira y hay día y noche; la Luna tarda cerca de un mes en su ciclo. Relato inventado: con Luna llena los vecinos conversan más tarde. Dibujo de la Luna una noche. Pregunta: ¿qué observa nuestra comunidad del cielo y para qué?",
           ["separa ciencia escolar y relato inventado", "escribe dos hechos correctos", "no mira el Sol"], ["tabla de dos columnas", "pregunta"], ["mezclar las dos fuentes", "afirmar creencias de un pueblo real"],
           "Preguntar de dónde viene cada dato; reforzar la seguridad con el Sol."),
    reinforce="Dibuja cuatro formas de la Luna y ordénalas en su ciclo.",
    extend="Escribe una pregunta que podrías responder observando la Luna durante un mes.",
)

L(
    OA15, 4,
    materials="Lápiz y hojas. La tabla comparativa está escrita aquí y es inventada.",
    use="Aprenderé a comparar la ciencia escolar con un saber de una comunidad sin decir cuál es mejor ni mezclarlas. Sirve para respetar cada manera de conocer.",
    prior=["Sé distinguir ciencia escolar y relato inventado.", "Sé qué es una evidencia."],
    explain=[
        "Comparar es ver qué se parece y qué es distinto. La ciencia escolar y los saberes de una comunidad pueden hablar de la misma parte de la naturaleza, como las estaciones. Pero cada una se apoya en su propia forma de conocer.",
        "Jerarquizar es decir que una es mejor. Fusionar es mezclarlas como si fueran lo mismo. Ninguna de las dos acciones es respetuosa. Lo correcto es describir cada una por separado y señalar semejanzas y diferencias.",
        "En esta clase comparamos con un ejemplo inventado: la escuela explica que las estaciones ocurren porque la Tierra se mueve alrededor del Sol, y la comunidad inventada de Valle Alto reconoce la primavera cuando florece el árbol del patio. Son maneras distintas de conocer y ambas sirven.",
    ],
    vocab=[("comparar", "mirar dos cosas para ver semejanzas y diferencias"), ("jerarquizar", "decir que una cosa es mejor que otra"), ("fusionar", "mezclar dos cosas hasta que parezcan una sola"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas son distintas")],
    worked=[
        W("Comparar sin jerarquizar", "Tabla: Escuela: estaciones por el movimiento de la Tierra. Valle Alto (inventado): primavera cuando florece el árbol. ¿Qué tienen en común?", ["Ambas hablan de las estaciones.", "Ambas se basan en observar.", "Escribo la semejanza."], "Las dos hablan de las estaciones del año."),
        W("Evitar la fusión", "Un niño dice: «La ciencia confirma lo que dice Valle Alto». ¿Qué problema hay?", ["Son dos maneras de conocer.", "Una no confirma a la otra.", "Se están mezclando."], "Mezcla dos maneras de conocer."),
    ],
    mistakes=[
        M("Decir que una manera de conocer es mejor.", "Es jerarquizar.", "Describe cada una."),
        M("Mezclar los datos como si fueran lo mismo.", "Pierden su origen.", "Rotula de dónde viene cada dato."),
    ],
    R=[
        ex("Según la tabla, ¿cómo explica las estaciones la escuela? A) por el movimiento de la Tierra B) por el árbol del patio", "A", "Eso dice la tabla."),
        ex("Según la tabla, ¿cómo reconoce la primavera Valle Alto (inventado)?", "Cuando florece el árbol", "La tabla lo dice."),
        ex("Decir que una manera es mejor que otra, ¿es jerarquizar o comparar?", "Jerarquizar", "Comparar solo describe."),
    ],
    C=[
        ex("¿Qué es fusionar? A) mezclar como si fueran lo mismo B) separar", "A", "Pierde el origen."),
        ex("Verdadero o falso: comparar significa elegir la manera mejor.", "Falso", "Se buscan semejanzas y diferencias."),
        ex("Verdadero o falso: la ciencia escolar confirma el saber de una comunidad.", "Falso", "Son maneras distintas de conocer."),
    ],
    A=[
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas hablan de las estaciones b) una usa el movimiento de la Tierra y la otra el árbol.", "a semejanza, b diferencia", "Hablar de lo mismo es semejanza; la fuente es diferencia."),
        ex("Escribe una diferencia entre cómo conoce la escuela y cómo conoce Valle Alto (inventado).", "La escuela explica con el movimiento de la Tierra; Valle Alto reconoce con el árbol que florece", "Son las dos fuentes de la tabla."),
        ex("¿Cuál frase fusiona dos maneras de conocer? A) «La escuela y Valle Alto hablan de las estaciones» B) «El árbol que florece es la misma explicación que el movimiento de la Tierra»", "B", "La B dice que son lo mismo; la A solo las compara."),
    ],
    Z=[
        ex("Ema escribe: «La escuela es más científica que Valle Alto». ¿Qué error comete?", "Jerarquiza", "No describe, juzga."),
        ex("Tomás escribe: «El árbol que florece prueba que la Tierra se mueve alrededor del Sol». ¿Qué error comete?", "Fusiona dos maneras de conocer", "Una no prueba a la otra."),
    ],
    D=[
        ex("Dos comparaciones: 1) «La escuela y Valle Alto hablan de las estaciones de maneras distintas». 2) «Valle Alto es mejor porque usa un árbol». ¿Cuál compara bien?", "La 1", "La 2 jerarquiza."),
        ex("Una niña pregunta cómo conoce las estaciones su comunidad real. ¿A quién consulta? A) al educador tradicional B) a un buscador al azar", "A", "La comunidad es la fuente."),
    ],
    context=[ex("Tu curso hace un cartel con dos columnas: escuela y Valle Alto (inventado). ¿Qué escriben al final? A) «Son dos maneras de conocer; no hay una mejor» B) «Gana la escuela»", "A", "No dice cuál es mejor.")],
    selfcheck=[
        ex("Escribe la diferencia entre jerarquizar y fusionar.", "Jerarquizar es decir que una es mejor; fusionar es mezclarlas", "Son los dos errores."),
        ex("Verdadero o falso: puedo decir que un saber de una comunidad es mejor que la ciencia escolar.", "Falso", "Eso sería jerarquizar."),
        ex("¿Qué haces para comparar bien?", "Describo cada una y digo semejanzas y diferencias", "No juzgo ni mezclo."),
    ],
    task=T("Completa esta comparación inventada. Columna 1, escuela: las estaciones ocurren porque la Tierra se mueve alrededor del Sol. Columna 2, Valle Alto (inventado): la primavera se reconoce porque florece el árbol del patio. Escribe una semejanza, una diferencia y una frase que explique por qué no se debe decir cuál es mejor ni mezclarlas. Añade una pregunta para el educador tradicional sobre cómo su comunidad reconoce las estaciones.",
           "Semejanza: las dos hablan de las estaciones. Diferencia: una usa el movimiento de la Tierra y la otra el árbol que florece. No se dice cuál es mejor ni se mezclan porque son maneras distintas de conocer. Pregunta: ¿cómo reconoce nuestra comunidad el cambio de estaciones?",
           ["escribe una semejanza y una diferencia", "no jerarquiza ni fusiona", "formula una pregunta"], ["tabla", "frase", "pregunta"], ["decir cuál es mejor", "mezclar las dos fuentes"],
           "Preguntar por qué no se mezclan; valorar la pregunta."),
    reinforce="Marca con S las semejanzas y con D las diferencias en la tabla de la clase.",
    extend="Escribe otra comparación con la ciencia escolar: cómo explica la escuela el día y la noche y cómo podría contarlo una comunidad, rotulando la segunda como ejemplo inventado.",
)

L(
    OA15, 5,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a comunicar qué puede decir cada fuente y hasta dónde llega lo que sé. Sirve para presentar sin inventar.",
    prior=["Sé comparar sin jerarquizar ni fusionar.", "Sé distinguir ciencia escolar y relato inventado."],
    explain=[
        "Cada fuente tiene un alcance, que es hasta dónde puede responder. Un libro de ciencia escolar puede explicar por qué hay estaciones. Una persona de la comunidad puede contar cómo su comunidad vive el cambio de estación. Ninguna responde todo.",
        "Al comunicar, decimos de qué fuente viene cada dato y qué no sabemos. Usamos frases como «según el libro de ciencias…» o «según doña Rosa…». Y terminamos con un límite: «esto no lo sé» o «esto lo enseña el educador tradicional».",
        "Así evitamos inventar, generalizar o mezclar. En esta clase usamos fichas inventadas y hechos de la ciencia escolar. Los saberes reales los cuenta la propia comunidad.",
    ],
    vocab=[("alcance", "hasta dónde puede responder una fuente"), ("atribuir", "decir de quién viene un dato"), ("límite", "lo que no se sabe o no corresponde decir"), ("fuente", "persona o texto que entrega el dato"), ("generalizar", "decir que algo vale para todos sin tener pruebas")],
    worked=[
        W("Atribuir cada dato", "Datos: 1) «hay estaciones porque la Tierra se mueve alrededor del Sol», 2) «Valle Alto reconoce la primavera cuando florece el árbol, según doña Rosa». ¿Cuál es de ciencia escolar?", ["El 1 explica el movimiento de la Tierra.", "El 2 viene de doña Rosa.", "La ciencia escolar es el 1."], "El 1."),
        W("Escribir un límite", "Al terminar, ¿cómo dices lo que no sabes?", ["Digo qué no sé.", "Digo quién lo enseña.", "Lo escribo."], "«No sé cómo lo vive la comunidad real; eso lo enseña el educador tradicional.»"),
    ],
    mistakes=[
        M("No decir de dónde viene un dato.", "El oyente no sabe si es ciencia o relato.", "Usa «según…»."),
        M("Terminar sin decir un límite.", "Parece que lo sabes todo.", "Agrega lo que no sabes."),
    ],
    R=[
        ex("¿Qué es el alcance de una fuente?", "Hasta dónde puede responder", "Es su límite de respuesta."),
        ex("«Según doña Rosa…», ¿atribuye el dato o no?", "Sí, lo atribuye", "Dice de quién viene."),
        ex("Si no sabes algo, ¿lo inventas o lo dices como límite?", "Lo digo como límite", "No se inventa."),
    ],
    C=[
        ex("Verdadero o falso: una fuente puede responder todo.", "Falso", "Cada fuente tiene un alcance."),
        ex("¿Qué es generalizar? A) decir que algo vale para todos sin pruebas B) dar un dato exacto", "A", "Es afirmar sin pruebas."),
        ex("Verdadero o falso: al comunicar conviene decir de qué fuente viene cada dato.", "Verdadero", "Así no se mezclan."),
    ],
    A=[
        ex("Clasifica en CIENCIA ESCOLAR o COMUNIDAD INVENTADA: a) hay estaciones porque la Tierra se mueve alrededor del Sol b) Valle Alto reconoce la primavera por el árbol.", "a ciencia escolar, b comunidad inventada", "Cada dato viene de su fuente."),
        ex("Completa con la atribución: «___ doña Rosa, el árbol del patio florece en primavera». Escribe la palabra.", "Según", "Atribuye el dato."),
        ex("¿Cuál es un buen límite para el final de tu presentación? A) «No sé cómo lo vive la comunidad real; lo enseña el educador tradicional» B) «Ya lo sé todo»", "A", "Un límite dice lo que no se sabe."),
    ],
    Z=[
        ex("Pedro presenta un dato de ciencia escolar y uno del relato inventado sin decir de dónde viene cada uno. ¿Qué error comete?", "No atribuye las fuentes", "El oyente los mezcla."),
        ex("Ema termina diciendo «así piensan todos los pueblos». ¿Qué error comete?", "Generaliza", "Solo conoce una ficha inventada."),
    ],
    D=[
        ex("Dos cierres: 1) «Esto es lo que sé de la ficha. Lo real lo enseña el educador tradicional.» 2) «Ya sé todo sobre este tema.» ¿Cuál es más responsable?", "El 1", "Declara su límite."),
        ex("¿A quién agradeces al terminar? A) a las fuentes B) a nadie", "A", "Reconoces lo recibido."),
    ],
    context=[ex("Tu curso presenta un cartel con ciencia escolar sobre las estaciones y la ficha inventada de Valle Alto. ¿Cómo lo hacen bien? A) rotulando cada dato con su fuente B) sin rótulos", "A", "Así no se mezclan.")],
    selfcheck=[
        ex("Escribe qué es el alcance de una fuente.", "Hasta dónde puede responder", "Es la definición."),
        ex("Verdadero o falso: un buen trabajo termina con un límite.", "Verdadero", "Declara lo que no se sabe."),
        ex("¿Qué palabra usas para decir de dónde viene un dato?", "Según", "Atribuye la fuente."),
    ],
    task=T("Prepara un cartel con tres partes: 1) un dato de ciencia escolar (por ejemplo, por qué hay día y noche), con «según el libro de ciencias»; 2) un dato de la ficha inventada de Valle Alto («la primavera se reconoce cuando florece el árbol del patio»), con «según doña Rosa»; 3) un límite («no sé…»). Termina con un agradecimiento. No mires el Sol directamente. Añade una pregunta para el educador tradicional.",
           "1 Según el libro de ciencias, hay día y noche porque la Tierra gira sobre sí misma. 2 Según doña Rosa (ficha inventada), la primavera se reconoce cuando florece el árbol del patio. 3 No sé cómo lo vive la comunidad real; eso lo enseña el educador tradicional. Gracias. Pregunta: ¿qué observa nuestra comunidad para conocer la naturaleza?",
           ["incluye las tres partes", "atribuye cada dato", "declara un límite"], ["cartel de tres partes", "agradecimiento"], ["mezclar las fuentes", "olvidar el límite"],
           "Preguntar de dónde viene cada dato; valorar el límite."),
    reinforce="Subraya en tu cartel la palabra «según» cada vez que atribuyes un dato.",
    extend="Escribe dos límites distintos que pondrías a una presentación sobre ciencia y cosmos.",
)
