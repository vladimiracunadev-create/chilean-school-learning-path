"""Cuaderno del estudiante, 3.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 10 (arte y técnicas ancestrales en diálogo con la naturaleza) y OA 11 (normas en eventos
socioculturales y espirituales).

Criterio de autoría: las comunidades, las personas, los eventos, las técnicas y las normas de práctica son
INVENTADOS y se rotulan así. No se asocia ningún arte, técnica, diseño, rol, norma ni evento a un pueblo
concreto. Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc3_a import L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA10, OA11 = "LC03 OA 10", "LC03 OA 11"

FICHA_TELAR = ("Ficha de práctica (inventada): Comunidad: Valle Alto. Técnica: tejido de lana en un telar sencillo. "
               "Portadora: doña Marta, que aprendió de su abuela y hoy enseña a los jóvenes. Permiso: doña Marta autorizó usar esta ficha. "
               "Límite: los diseños de su familia no se copian.")

# ============================================================ OA 10 · Arte y técnicas ancestrales en diálogo con la naturaleza
L(
    OA10, 1,
    materials="Lápiz y hojas. La ficha está escrita aquí. La comunidad, la técnica y las personas son inventadas.",
    use="Aprenderé a reconocer de dónde viene un arte o una técnica y quiénes la conocen y la enseñan. Sirve para valorarla con respeto y dar crédito.",
    prior=["Sé que una ficha tiene comunidad, fuente y permiso.", "Sé que una cultura viva comparte saberes con permiso."],
    explain=[
        "Un arte o técnica ancestral es un saber que se hace con las manos y se enseña de generación en generación. Puede ser tejer, trabajar la arcilla o preparar tintes. La palabra «ancestral» quiere decir que viene de los antepasados y continúa hoy.",
        "Las personas que conocen y enseñan una técnica se llaman portadores o portadoras. Pueden ser abuelas, abuelos, maestras, maestros o jóvenes. La técnica tiene origen en una comunidad concreta. Por eso decimos de dónde viene y quién la enseña.",
        "Transmitir es pasar un saber de una persona a otra. Se transmite mirando, practicando y conversando. Un portador decide cómo y a quién enseña y qué parte no se comparte. En esta clase usamos una ficha inventada para practicar.",
    ],
    vocab=[("técnica", "manera de hacer algo siguiendo pasos"), ("ancestral", "que viene de los antepasados y continúa hoy"), ("portador", "persona que conoce, practica y enseña un saber"), ("transmitir", "pasar un saber de una persona a otra"), ("origen", "lugar o comunidad de donde viene algo")],
    worked=[
        W("Leer la ficha de práctica", "Lee: «" + FICHA_TELAR + "» ¿Quién es la portadora y de quién aprendió?", ["Busco Portadora: doña Marta.", "Leo que aprendió de su abuela.", "Junto los dos datos."], "La portadora es doña Marta; aprendió de su abuela."),
        W("Reconocer el límite", "En la ficha, ¿qué parte no se puede copiar?", ["Busco el Límite.", "Dice que los diseños de su familia no se copian.", "Eso es lo que se respeta."], "Los diseños de su familia."),
    ],
    mistakes=[
        M("Pensar que una técnica «no tiene dueño» porque es antigua.", "Tiene origen en una comunidad y personas que la enseñan.", "Pregunta de dónde viene y quién la enseña."),
        M("Decir que un arte es de un pueblo sin que lo diga una fuente.", "Puede ser falso y faltar al respeto.", "Escribe solo lo que dice la ficha."),
    ],
    R=[
        ex("En la ficha de práctica de Valle Alto, ¿quién es la portadora de la técnica?", "Doña Marta", "La ficha la nombra."),
        ex("¿Qué técnica trata la ficha? A) tejido de lana en un telar sencillo B) construir puentes", "A", "Lo dice la ficha."),
        ex("¿De quién aprendió doña Marta?", "De su abuela", "La ficha lo dice."),
    ],
    C=[
        ex("¿Qué significa «ancestral»? A) que viene de los antepasados y continúa hoy B) que ya no existe", "A", "Se mantiene hoy."),
        ex("Verdadero o falso: un portador es solo una persona que ya murió.", "Falso", "Es una persona que practica y enseña hoy."),
        ex("Verdadero o falso: transmitir un saber es pasarlo de una persona a otra.", "Verdadero", "Se aprende mirando, practicando y conversando."),
    ],
    A=[
        ex("Une cada pregunta con su dato de la ficha. 1) ¿Qué técnica? 2) ¿Quién la enseña? 3) ¿Qué no se copia? a) los diseños de su familia b) tejido de lana c) doña Marta", "1-b, 2-c, 3-a", "Cada dato está en la ficha."),
        ex("Una frase dice: «Doña Marta aprendió el tejido en una escuela de arte». ¿Está en la ficha? Responde Sí o No.", "No", "La ficha dice que aprendió de su abuela."),
        ex("Una frase dice: «Doña Marta enseña a los jóvenes». ¿Está en la ficha? Responde Sí o No.", "Sí", "La ficha dice que hoy enseña a los jóvenes."),
    ],
    Z=[
        ex("Tomás dice: «Esa técnica es de todos los pueblos porque es antigua». ¿Qué error comete?", "Generaliza una técnica a todos los pueblos", "La ficha habla de una comunidad."),
        ex("Ema quiere copiar un diseño familiar de doña Marta para su cuaderno. ¿Debe hacerlo? Responde Sí o No.", "No", "La ficha dice que esos diseños no se copian."),
    ],
    D=[
        ex("Dos niños leen la ficha. Uno escribe «según doña Marta, aprendió de su abuela». Otro escribe «aprendió en un curso». ¿Quién se queda en lo que dice la ficha?", "El primero", "El segundo agrega un dato que no está."),
        ex("Si quieres aprender la técnica real de tu zona, ¿a quién pides que te enseñe? A) a un portador o educador tradicional B) a un video al azar", "A", "Ellos pueden enseñar con permiso."),
    ],
    context=[ex("La escuela invita a doña Marta (inventada) a mostrar su telar. Antes de empezar, ¿qué se le debe preguntar? A) qué se puede compartir y qué no B) cuánto vale su telar", "A", "Se respetan los límites del portador.")],
    selfcheck=[
        ex("Escribe qué es un portador.", "Una persona que conoce, practica y enseña un saber", "Es la definición de la lección."),
        ex("Verdadero o falso: una técnica ancestral ya no se practica hoy.", "Falso", "Se practica hoy."),
        ex("¿Qué dos datos dices para dar crédito a una técnica?", "De qué comunidad viene y quién la enseña", "Así se reconoce su origen."),
    ],
    task=T("Con la ficha inventada del telar de Valle Alto, haz una tarjeta de crédito con cuatro líneas: técnica, comunidad, portadora y lo que no se copia. Dibuja un telar sencillo de madera sin copiar ningún diseño. Debajo escribe una frase de agradecimiento a doña Marta.",
           "Técnica: tejido de lana en un telar sencillo. Comunidad: Valle Alto. Portadora: doña Marta. No se copia: los diseños de su familia. Gracias, doña Marta, por enseñar a los jóvenes.",
           ["completa las cuatro líneas con datos de la ficha", "no copia diseños", "agradece a la portadora"], ["tarjeta de crédito", "dibujo", "agradecimiento"], ["copiar un diseño de un libro y decir que es de doña Marta", "no nombrar a la portadora"],
           "Preguntar de dónde sacó cada línea; valorar el agradecimiento y el dibujo sin diseños copiados."),
    reinforce="Subraya en la ficha lo que se enseña y lo que no se copia.",
    extend="Escribe dos preguntas para un portador de tu zona sobre cómo aprendió su técnica.",
)

L(
    OA10, 2,
    materials="Lápiz y hojas. El proceso inventado está escrito aquí.",
    use="Aprenderé a relacionar el material, la técnica y la naturaleza en un arte ancestral. Sirve para entender cómo se puede trabajar con la naturaleza sin dañarla.",
    prior=["Sé que una técnica tiene portadores y origen.", "Sé que los materiales vienen de la naturaleza."],
    explain=[
        "Muchos artes se hacen con materiales de la naturaleza: lana, fibras vegetales, arcilla, hojas, piedras. Para usarlos bien hay que conocerlos y saber cuándo y cómo tomarlos. Tomar más de lo necesario puede dañarlos.",
        "La técnica es el camino de pasos para transformar un material. Si la persona conoce bien la naturaleza, sabe cuándo recoger y cuánto. Así el trabajo dialoga con la naturaleza: recibe de ella y la cuida para que siga dando.",
        "En esta clase usamos un proceso inventado de Valle Alto con lana y tintes de hojas. No describe la técnica real de ningún pueblo. Las técnicas reales y sus cuidados los enseñan los portadores y el educador tradicional.",
    ],
    vocab=[("material", "cosa con la que se hace algo"), ("fibra", "hilo que sale de una planta o de un animal"), ("tinte", "color que se saca de una planta u otro material"), ("recoger", "tomar lo que da la naturaleza"), ("cuidar", "tomar solo lo necesario para que siga existiendo")],
    worked=[
        W("Del material al objeto", "Proceso inventado de doña Marta: 1) lana de oveja, 2) hilado, 3) teñido con hojas, 4) tejido. ¿Qué viene después de hilar?", ["Leo el orden.", "Después de hilado viene el teñido.", "Respondo."], "El teñido con hojas."),
        W("Cuidar al recoger", "Doña Marta recoge hojas para teñir. Dice: «Tomo unas pocas de cada planta, no arranco la planta entera». ¿Por qué?", ["Si arranca la planta, no vuelve a dar hojas.", "Si toma pocas, la planta sigue viva.", "Así la naturaleza sigue dando."], "Porque la planta sigue viva y puede dar más hojas."),
    ],
    mistakes=[
        M("Tomar todo el material porque «hay mucho».", "Se puede acabar o dañar.", "Toma solo lo necesario y deja que se renueve."),
        M("Creer que la técnica es solo hacer el objeto, sin conocer la naturaleza.", "La técnica incluye saber cuándo y cómo recoger.", "Aprende también cómo cuidar el material."),
    ],
    R=[
        ex("En el proceso inventado de doña Marta, ¿qué material animal se usa: lana de oveja o madera?", "Lana de oveja", "El proceso empieza con lana."),
        ex("¿Con qué se tiñe? A) con hojas B) con pintura de tienda", "A", "Lo dice el proceso."),
        ex("¿Cuál es el último paso del proceso: hilar o tejer?", "Tejer", "El tejido es el paso final."),
    ],
    C=[
        ex("Verdadero o falso: para cuidar la naturaleza, se toma todo el material de una vez.", "Falso", "Se toma solo lo necesario."),
        ex("¿Qué es una fibra? A) un hilo que sale de una planta o de un animal B) una piedra", "A", "La lana es una fibra."),
        ex("Verdadero o falso: la técnica incluye saber cuándo y cómo recoger el material.", "Verdadero", "Es parte de conocer la naturaleza."),
    ],
    A=[
        ex("Ordena el proceso: a) tejer b) teñir con hojas c) lana de oveja d) hilar. Escribe las letras.", "c, d, b, a", "Lana, hilar, teñir y tejer."),
        arith("Doña Marta recoge 3 hojas de cada planta y visita 4 plantas. ¿Cuántas hojas recoge en total?", "3+3+3+3", "Se suman 3 hojas cuatro veces."),
        ex("Une cada material con su origen. 1) lana 2) hojas de tinte a) planta b) oveja", "1-b, 2-a", "La lana viene de la oveja y las hojas de una planta."),
    ],
    Z=[
        ex("Pedro arrancó una planta entera para sacar muchas hojas. ¿Qué problema hay?", "La planta ya no podrá dar más hojas", "Dañó la fuente del material."),
        ex("Ema dice que si recoge solo lo necesario, la naturaleza sigue dando. ¿Tiene razón? Responde Sí o No.", "Sí", "Así el material se renueva."),
    ],
    D=[
        ex("Dos niñas: una recoge unas pocas hojas de cada planta; otra arranca una planta entera. ¿Cuál dialoga mejor con la naturaleza?", "La primera", "Recibe sin dañar."),
        ex("Quieres teñir lana con hojas que no conoces. ¿Qué debes hacer primero? A) preguntar a un portador o adulto que conozca B) probarlo sin saber", "A", "Así se evita dañar o hacerse daño."),
    ],
    context=[ex("En el patio de la escuela hay un arbusto con hojas. Alguien quiere sacarlas todas para un trabajo. ¿Qué es mejor? A) sacar pocas y dejar que siga creciendo B) sacarlas todas", "A", "Se cuida la planta.")],
    selfcheck=[
        ex("Escribe una forma de cuidar un material de la naturaleza.", "Tomar solo lo necesario o no arrancar la planta entera", "Así el material sigue existiendo."),
        ex("Verdadero o falso: la lana viene de una planta.", "Falso", "La lana viene de la oveja."),
        ex("¿Qué es un tinte?", "Un color que se saca de una planta u otro material", "Es lo que da color al hilo."),
    ],
    task=T("Dibuja en cuatro cuadros el proceso inventado de doña Marta: lana de oveja, hilado, teñido con hojas y tejido. Debajo de cada cuadro escribe cómo se cuida la naturaleza en ese paso (por ejemplo, tomar pocas hojas). Termina con una pregunta para un portador de tu zona sobre cómo cuida los materiales.",
           "Cuadro 1: lana de oveja, se usa solo la necesaria. Cuadro 2: hilado, sin desperdiciar lana. Cuadro 3: teñido con hojas, se toman pocas de cada planta. Cuadro 4: tejido, se aprovecha el hilo. Pregunta: ¿cómo cuida usted los materiales que usa?",
           ["dibuja los cuatro pasos en orden", "explica un cuidado de la naturaleza", "plantea una pregunta respetuosa"], ["cuatro cuadros", "frases de cuidado", "pregunta"], ["cambiar el orden", "inventar una técnica real de un pueblo"],
           "Preguntar por qué cada paso necesita cuidar el material; valorar la pregunta."),
    reinforce="Escribe dos materiales de la naturaleza y de dónde vienen.",
    extend="Piensa en un material que uses en la escuela. Escribe de dónde viene y una forma de usarlo con cuidado.",
)

L(
    OA10, 3,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a analizar decisiones y resguardos en el uso de un arte ancestral: qué se comparte, qué se pide y qué se cuida. Sirve para participar con respeto.",
    prior=["Sé que una técnica tiene portadores y origen.", "Sé qué es apropiarse y qué es valorar."],
    explain=[
        "Un resguardo es un cuidado para proteger algo importante. En un arte ancestral hay resguardos: ciertos diseños son de una familia o de la comunidad y no se copian. Una comunidad puede decidir que algunos saberes se enseñen solo a ciertas personas.",
        "Una decisión es una elección. El portador decide qué enseña, a quién y cuándo. Nosotros decidimos si pedimos permiso, damos crédito y respetamos los límites. Pedir permiso es el primer paso para participar.",
        "Cuando una persona vende o copia un diseño sin permiso, puede dañar a la comunidad. Si quieres usar algo, preguntas: ¿de quién es?, ¿me autorizan?, ¿cómo lo puedo mencionar? Si la respuesta es no, respetas el no.",
    ],
    vocab=[("resguardo", "cuidado para proteger algo importante"), ("decisión", "elección que hace una persona o grupo"), ("autorizar", "dar permiso para usar algo"), ("copiar", "hacer igual a otro sin permiso"), ("crédito", "reconocimiento a quien hizo o enseñó algo")],
    worked=[
        W("Analizar un caso", "Caso inventado: una escuela quiere imprimir en poleras el diseño de la familia de doña Marta. Doña Marta no fue consultada. ¿Qué falta?", ["Es un diseño de su familia.", "No pidieron permiso.", "Falta la autorización."], "Falta pedir permiso a doña Marta."),
        W("Respetar un no", "Doña Marta responde: «Ese diseño no se puede usar». ¿Qué hace el curso?", ["Escucha la respuesta.", "No usa el diseño.", "Busca otra forma de valorar, como invitarla a contar su técnica."], "No usa el diseño y respeta su decisión."),
    ],
    mistakes=[
        M("Pensar que si algo se ve en internet, ya se puede usar.", "Verlo no significa tener permiso.", "Pregunta a la comunidad o al portador."),
        M("Insistir cuando la respuesta es no.", "El portador decide qué se comparte.", "Acepta el no y busca otra manera de valorar."),
    ],
    R=[
        ex("Un diseño familiar de doña Marta, ¿se copia o se pide permiso?", "Se pide permiso", "Es de una familia."),
        ex("Si el portador dice que no, ¿insistes o respetas?", "Respeto", "El portador decide."),
        ex("¿Qué es un resguardo? A) un cuidado para proteger algo importante B) un tipo de lana", "A", "Es un cuidado protector."),
    ],
    C=[
        ex("Verdadero o falso: si algo está en internet, ya tengo permiso para usarlo.", "Falso", "Verlo no es tener permiso."),
        ex("¿Quién decide qué enseña un portador? A) el portador B) cualquier visitante", "A", "Él o ella decide."),
        ex("Verdadero o falso: dar crédito es reconocer quién enseñó o hizo algo.", "Verdadero", "Es parte del respeto."),
    ],
    A=[
        ex("Ordena los pasos para usar un diseño: a) usarlo si lo autorizan b) preguntar de quién es c) pedir permiso d) dar crédito. Escribe las letras.", "b, c, a, d", "Primero preguntar, luego pedir permiso, usar y dar crédito."),
        ex("Clasifica en RESPETA o NO RESPETA: a) pedir permiso b) copiar un diseño familiar c) agradecer a la portadora.", "a respeta, b no respeta, c respeta", "Copiar sin permiso no respeta."),
        ex("Cuenta cuántas acciones respetuosas hay en la lista: 1) pedir permiso 2) copiar sin avisar 3) dar crédito 4) insistir después de un no.", "2", "Solo pedir permiso y dar crédito."),
    ],
    Z=[
        ex("Lía dice: «Si doña Marta no estaba, no importa que imprimamos el diseño». ¿Qué error comete?", "Falta el permiso", "El permiso es necesario aunque no esté."),
        ex("Pedro dice: «Si usamos el diseño y ponemos su nombre, ya no hace falta permiso». ¿Tiene razón? Responde Sí o No.", "No", "El crédito no reemplaza al permiso."),
    ],
    D=[
        ex("Dos cursos quieren valorar el telar de Valle Alto. Uno copia un diseño. El otro invita a doña Marta a contar cómo enseña. ¿Cuál respeta los límites?", "El segundo", "Escucha y no copia."),
        ex("Si la comunidad dice que un diseño es solo suyo, ¿puedes dibujarlo en un cartel? Responde Sí o No.", "No", "Es un límite que se respeta."),
    ],
    context=[ex("Un negocio quiere vender recuerdos con un diseño de una comunidad inventada, sin consultar. ¿Qué debe hacer primero? A) pedir permiso a la comunidad B) cambiar el nombre", "A", "Sin permiso se daña a la comunidad.")],
    selfcheck=[
        ex("Escribe qué es un resguardo.", "Un cuidado para proteger algo importante", "Es la definición de la lección."),
        ex("Verdadero o falso: se puede insistir si el portador dice que no.", "Falso", "Se respeta el no."),
        ex("¿Cuál es el primer paso para usar el diseño de otra persona?", "Pedir permiso", "Es lo primero."),
    ],
    task=T("Lee este caso inventado: «Un curso quiere hacer un mural con un diseño familiar de doña Marta, de Valle Alto. No han hablado con ella.» Escribe cuatro pasos para actuar con respeto: qué preguntan, a quién, qué hacen si dice sí y qué hacen si dice no. Añade una frase de agradecimiento.",
           "1 Preguntan si el diseño se puede usar. 2 A doña Marta o a su familia. 3 Si dice sí, lo usan y dan crédito. 4 Si dice no, lo respetan y buscan otra forma, como invitarla a contar su técnica. Gracias, doña Marta.",
           ["escribe los cuatro pasos", "incluye qué hacen si dice no", "agradece"], ["cuatro pasos", "agradecimiento"], ["usar el diseño sin permiso", "no decir qué se hace si dice no"],
           "Preguntar qué pasa si la respuesta es no; valorar los pasos en orden."),
    reinforce="Colorea de verde las acciones que respetan y de rojo las que no en la lista de la clase.",
    extend="Escribe una regla de tu curso para usar el trabajo de otras personas con permiso.",
)

L(
    OA10, 4,
    materials="Hojas, lápiz y colores. Si lo deseas, tiras de papel; puedes rasgarlas con las manos o usar tijera de punta roma con ayuda de una persona adulta.",
    use="Aprenderé a responder de forma creativa a lo que observo de la naturaleza, sin copiar los diseños de nadie. Sirve para crear algo propio con respeto.",
    prior=["Sé que hay diseños que no se copian.", "Sé que la naturaleza entrega materiales y formas."],
    explain=[
        "Responder creativamente significa crear algo propio a partir de lo que observamos y sentimos. Puedes mirar una hoja, una piedra o una nube y crear un dibujo o un trenzado de papel con tus ideas.",
        "No es lo mismo inspirarse que copiar. Inspirarse es observar algo de la naturaleza y hacer tu propia versión. Copiar es repetir el diseño de otra persona sin permiso. Si te inspiras en un arte, lo dices y agradeces.",
        "En esta clase observarás una hoja de tu casa o patio, sin arrancar plantas de lugares protegidos. Pide ayuda a una persona adulta para elegirla y lávate las manos después. Crearás tu propio diseño con líneas y formas simples. Los diseños tradicionales los enseñan los portadores y el educador tradicional.",
    ],
    vocab=[("crear", "hacer algo nuevo con tus ideas"), ("inspirarse", "mirar algo y hacer tu propia versión"), ("copiar", "repetir lo que hizo otra persona"), ("observar", "mirar con atención"), ("forma", "contorno o figura de algo")],
    worked=[
        W("Observar una hoja", "Observas una hoja ovalada con una línea al centro y líneas pequeñas a los lados. ¿Qué formas puedes anotar?", ["Veo un óvalo.", "Veo una línea central.", "Veo líneas pequeñas a los lados."], "Un óvalo, una línea central y líneas pequeñas a los lados."),
        W("Inspirarse sin copiar", "Con esas formas dibujas una franja: óvalos repetidos con una línea al centro de cada uno. ¿Copiaste el diseño de alguien?", ["Las formas salen de tu hoja.", "No miraste el diseño de nadie.", "Es tu propia versión."], "No, es un diseño propio inspirado en tu hoja."),
    ],
    mistakes=[
        M("Copiar un diseño de un libro y decir que es tuyo.", "Es apropiarse y falta el crédito.", "Observa la naturaleza y crea tu versión."),
        M("Dibujar símbolos que no entiendes y decir que son de un pueblo.", "Puedes inventar algo que no es verdad.", "Di solo que es tu diseño."),
    ],
    R=[
        ex("Observas una hoja con forma de óvalo. ¿Qué forma anotas: óvalo o cuadrado?", "Óvalo", "Esa es la forma que ves."),
        ex("Inspirarse, ¿es hacer tu propia versión o copiar lo de otro?", "Hacer tu propia versión", "Copiar es otra cosa."),
        ex("¿Qué haces antes de crear: observar o copiar de un libro?", "Observar", "Primero se mira la naturaleza."),
    ],
    C=[
        ex("Verdadero o falso: copiar un diseño de otra persona sin permiso es crear.", "Falso", "Copiar no es crear."),
        ex("¿Qué es inspirarse? A) mirar algo y hacer tu propia versión B) repetir sin cambiar", "A", "Es crear algo propio."),
        ex("Verdadero o falso: si te inspiras en un arte, puedes decirlo y agradecer.", "Verdadero", "Es una forma de dar crédito."),
    ],
    A=[
        arith("Una hoja tiene 1 línea central y 6 líneas pequeñas a los lados. ¿Cuántas líneas hay en total?", "1+6", "Se suma la línea central y las pequeñas."),
        ex("Clasifica en INSPIRARSE o COPIAR: a) dibujar tu hoja con tus formas b) calcar un diseño de un libro.", "a inspirarse, b copiar", "Calcar es copiar."),
        ex("Escribe una frase de crédito para tu diseño: «Me inspiré en ___ ». Completa con lo que observaste (una hoja).", "una hoja", "Dice de dónde viene la idea."),
    ],
    Z=[
        ex("Mateo dibuja símbolos que vio en una foto y dice «son de un pueblo, aunque no sé cuál». ¿Qué error comete?", "Atribuye algo sin fuente", "No sabe de dónde vienen."),
        ex("Ema dibuja su hoja y dice «es mi diseño, me inspiré en esta hoja». ¿Actuó con respeto? Responde Sí o No.", "Sí", "Creó algo propio y dijo su inspiración."),
    ],
    D=[
        ex("Dos trabajos: A) óvalos y líneas inspirados en una hoja; B) un símbolo calcado de un libro. ¿Cuál es creación propia?", "A", "B es copia."),
        ex("Quieres incluir un diseño tradicional en tu trabajo. ¿Qué haces? A) pedir permiso al educador tradicional o a la comunidad B) calcarlo", "A", "Así evitas apropiarte."),
    ],
    context=[ex("Julia observa una piedra lisa y crea un diseño con círculos. Lo muestra en el curso como propio. ¿Qué dato debería agregar? A) «Me inspiré en una piedra» B) «Es de un pueblo»", "A", "Dice su inspiración real.")],
    selfcheck=[
        ex("Escribe la diferencia entre inspirarse y copiar.", "Inspirarse es hacer tu versión; copiar es repetir lo de otro", "Es la idea central."),
        ex("Verdadero o falso: puedo decir que un símbolo es de un pueblo si lo vi en una foto.", "Falso", "Sin fuente no se atribuye."),
        ex("¿Qué haces primero para crear un diseño propio?", "Observar la naturaleza", "De ahí salen las formas."),
    ],
    task=T("Observa una hoja de tu casa o de la escuela (pide ayuda a una persona adulta para elegirla, no arranques plantas de lugares protegidos y lávate las manos después) o usa esta descripción: «hoja ovalada con una línea al centro y seis líneas pequeñas a los lados». Anota tres formas que ves. Crea una franja de diseño propio con esas formas, dibujada o hecha con tiras de papel trenzadas. Escribe debajo: «Me inspiré en…» y una frase de lo que aprendiste.",
           "Formas: óvalo, línea central, líneas pequeñas. Franja con óvalos repetidos. Me inspiré en una hoja ovalada. Aprendí que puedo crear sin copiar.",
           ["anota tres formas observadas", "crea un diseño propio", "dice en qué se inspiró"], ["lista de formas", "diseño", "frase de inspiración"], ["calcar un diseño ajeno", "decir que es de un pueblo"],
           "Preguntar de qué forma salió cada parte del diseño; valorar la frase de inspiración."),
    reinforce="Observa otra hoja y anota dos formas distintas de la anterior.",
    extend="Escribe dos preguntas para un portador sobre cómo se inspira en la naturaleza al crear.",
)

# ============================================================ OA 11 · Normas en eventos socioculturales y espirituales
L(
    OA11, 1,
    materials="Lápiz y hojas. La ficha del evento está escrita aquí y es inventada.",
    use="Aprenderé a situar un evento y a reconocer que su significado lo cuenta la comunidad. Sirve para llegar a un encuentro con respeto y sin adivinar.",
    prior=["Sé que cada comunidad tiene su manera de vivir.", "Sé que hay cosas que se comparten y otras que se resguardan."],
    explain=[
        "Un evento es una reunión que la comunidad organiza con un sentido. Puede ser sociocultural, como un encuentro para compartir, conversar o celebrar. O puede ser espiritual, ligado a lo que la comunidad considera sagrado.",
        "Cada evento tiene un significado, es decir, la razón por la que se hace y lo que representa. Ese significado lo cuenta la comunidad. Si el evento es espiritual, su significado puede unirse a cómo la comunidad ve el mundo; eso también lo explica solo la comunidad. Desde afuera no lo adivinamos viendo una foto o un video.",
        "Para situar un evento preguntamos: ¿qué evento es?, ¿de qué comunidad?, ¿quién lo cuenta?, ¿quién puede participar? y ¿qué se puede compartir? En esta clase usamos un evento inventado de Valle Alto. No es de ningún pueblo real.",
    ],
    vocab=[("evento", "reunión que la comunidad organiza con un sentido"), ("sociocultural", "que tiene que ver con la vida de la comunidad y su cultura"), ("espiritual", "que tiene que ver con lo sagrado"), ("significado", "razón y sentido de algo"), ("participar", "tomar parte en una actividad")],
    worked=[
        W("Situar un evento", "Ficha inventada: «Evento: Encuentro de Valle Alto. Es una reunión en la plaza para conversar y compartir comida. Lo cuenta doña Rosa. Pueden venir todas las personas invitadas.» ¿Es sociocultural o espiritual?", ["Es una reunión para conversar y compartir.", "No dice que sea sagrado.", "Es sociocultural."], "Sociocultural."),
        W("No adivinar el significado", "Un niño dice: «Seguro el encuentro tiene un significado secreto». ¿Se puede afirmar?", ["La ficha no lo dice.", "No hay fuente.", "No se puede afirmar."], "No, porque la ficha no lo dice."),
    ],
    mistakes=[
        M("Decir qué significa un evento mirando una foto.", "Solo la comunidad conoce su significado.", "Pregunta a la fuente."),
        M("Creer que todos los eventos pueden verse por cualquiera.", "Algunos eventos son solo para invitados o la comunidad.", "Pregunta quién puede participar."),
    ],
    R=[
        ex("En la ficha inventada, ¿qué evento es? A) un Encuentro de Valle Alto B) una carrera", "A", "Lo dice la ficha."),
        ex("¿Dónde ocurre el encuentro? A) en la plaza B) en la playa", "A", "La ficha dice «en la plaza»."),
        ex("¿Quién lo cuenta en la ficha?", "Doña Rosa", "Es la fuente."),
    ],
    C=[
        ex("¿Qué es un evento sociocultural? A) una reunión de la comunidad para compartir B) un viaje", "A", "Es un encuentro de vida comunitaria."),
        ex("Verdadero o falso: puedo saber el significado de un evento viendo una foto.", "Falso", "Lo cuenta la comunidad."),
        ex("Verdadero o falso: todos los eventos son para cualquier persona.", "Falso", "Algunos son solo para invitados o la comunidad."),
    ],
    A=[
        ex("Clasifica en SOCIOCULTURAL o ESPIRITUAL según la ficha: a) un encuentro para compartir comida b) una actividad ligada a lo sagrado.", "a sociocultural, b espiritual", "Compartir comida es sociocultural; lo sagrado es espiritual."),
        arith("Para situar un evento se hacen 5 preguntas. Si ya respondiste 3, ¿cuántas faltan?", "5-3", "Se restan las respondidas."),
        ex("Une cada pregunta con su dato. 1) ¿Qué evento? 2) ¿Dónde? 3) ¿Quién lo cuenta? a) doña Rosa b) en la plaza c) Encuentro de Valle Alto", "1-c, 2-b, 3-a", "Cada dato está en la ficha."),
    ],
    Z=[
        ex("Tomás dice: «Ese evento debe ser espiritual porque se ve importante». ¿Qué error comete?", "Adivina sin fuente", "La ficha dice que es una reunión para conversar."),
        ex("Ema dice: «Todos los eventos de los pueblos son iguales al Encuentro de Valle Alto». ¿Qué error comete?", "Generaliza un ejemplo inventado", "Cada comunidad es distinta."),
    ],
    D=[
        ex("Una niña quiere saber el significado de un evento real de su zona. ¿A quién le pregunta? A) al educador tradicional o a la comunidad B) a un buscador al azar", "A", "La comunidad cuenta el significado."),
        ex("Una ficha dice «solo para invitados». ¿Puedes ir sin invitación? Responde Sí o No.", "No", "Se respeta quién puede participar."),
    ],
    context=[ex("Tu curso fue invitado al Encuentro de Valle Alto (inventado). ¿Qué haces antes? A) leer la ficha y preguntar lo que no sabes B) llegar sin saber nada", "A", "Prepararse es una forma de respeto.")],
    selfcheck=[
        ex("Escribe qué es un evento sociocultural.", "Una reunión de la comunidad para compartir o celebrar", "Es la definición de la lección."),
        ex("Verdadero o falso: el significado de un evento lo cuenta la comunidad.", "Verdadero", "Solo ella lo conoce."),
        ex("¿Qué preguntas haces para situar un evento?", "Qué evento, qué comunidad, quién lo cuenta, quién participa y qué se comparte", "Son las preguntas de la lección."),
    ],
    task=T("Lee la ficha inventada: «Evento: Encuentro de Valle Alto. Es una reunión en la plaza para conversar y compartir comida. Lo cuenta doña Rosa. Pueden venir las personas invitadas. No se sacan fotos.» Completa una ficha con cinco líneas: evento, comunidad, quién lo cuenta, quién puede participar y qué no se hace. Añade una pregunta para el educador tradicional sobre un evento de tu comunidad que sea público.",
           "Evento: Encuentro de Valle Alto. Comunidad: Valle Alto. Cuenta: doña Rosa. Participan: las personas invitadas. No se hace: sacar fotos. Pregunta: ¿qué eventos de nuestra comunidad están abiertos a todas las personas?",
           ["completa las cinco líneas con datos de la ficha", "incluye lo que no se hace", "formula una pregunta respetuosa"], ["ficha de cinco líneas", "pregunta"], ["inventar el significado del evento", "olvidar que no se sacan fotos"],
           "Preguntar qué dice la ficha de quién participa; valorar que respete la norma de no sacar fotos."),
    reinforce="Subraya en la ficha el nombre del evento y a quién se invita.",
    extend="Escribe dos diferencias entre un evento sociocultural y uno espiritual, usando solo lo que dice la clase.",
)

L(
    OA11, 2,
    materials="Lápiz y hojas. Las normas están escritas aquí y son inventadas.",
    use="Aprenderé a reconocer los roles y las normas de un evento y a respetarlos. Sirve para participar sin interrumpir ni faltar el respeto.",
    prior=["Sé situar un evento.", "Sé que el significado lo cuenta la comunidad."],
    explain=[
        "En un evento cada persona puede tener un rol, que es la tarea o el lugar que le corresponde. Hay personas que organizan, personas que guían, personas que invitan y personas invitadas. Quién tiene cada rol lo define la comunidad.",
        "Una norma es una regla que indica cómo comportarse. Las normas ayudan a que todos se sientan respetados. Hay normas generales de respeto, como saludar, escuchar y esperar turno. Las normas especiales de cada evento las explica la comunidad.",
        "En esta clase usamos un evento inventado con roles y normas inventadas: doña Rosa organiza, las personas invitadas llegan a la hora, escuchan sin interrumpir y no usan el teléfono. No son normas de ningún pueblo real.",
    ],
    vocab=[("rol", "tarea o lugar que le corresponde a una persona en un evento"), ("norma", "regla que indica cómo comportarse"), ("organizar", "preparar un evento para que ocurra"), ("invitado", "persona a quien se avisa que puede participar"), ("interrumpir", "cortar a alguien mientras habla")],
    worked=[
        W("Asignar roles", "Ficha inventada: «Doña Rosa organiza el Encuentro de Valle Alto. Don Luis guía la conversación. Las personas invitadas escuchan y comparten.» ¿Quién guía?", ["Busco el verbo guía.", "Dice don Pedro.", "Respondo."], "Don Luis."),
        W("Aplicar una norma", "Norma inventada: «Se escucha sin interrumpir». Alguien habla mientras don Pedro conversa. ¿Qué norma se rompe?", ["Busco la norma sobre hablar.", "Dice escuchar sin interrumpir.", "Se rompió esa norma."], "Escuchar sin interrumpir."),
    ],
    mistakes=[
        M("Pensar que las normas de un evento valen para todos los pueblos.", "Las normas especiales las define cada comunidad.", "Pregunta qué norma rige en ese evento."),
        M("Tomar un rol que no te corresponde, como guiar la conversación.", "Cada rol lo define la comunidad.", "Pregunta cuál es tu rol."),
    ],
    R=[
        ex("En la ficha inventada, ¿quién organiza el encuentro?", "Doña Rosa", "La ficha lo dice."),
        ex("¿Qué hacen las personas invitadas? A) escuchan y comparten B) guían la conversación", "A", "Guía don Pedro."),
        ex("¿Qué es una norma? A) una regla que indica cómo comportarse B) un tipo de comida", "A", "Es una regla."),
    ],
    C=[
        ex("Verdadero o falso: las normas de un evento las define la comunidad.", "Verdadero", "Cada comunidad las explica."),
        ex("Verdadero o falso: escuchar sin interrumpir es una norma de respeto.", "Verdadero", "Ayuda a que todos se sientan respetados."),
        ex("¿Qué es un rol? A) la tarea o lugar de una persona en el evento B) una norma", "A", "Define qué le corresponde a cada uno."),
    ],
    A=[
        ex("Une cada persona con su rol. 1) doña Rosa 2) don Pedro 3) las personas invitadas a) guía la conversación b) organiza c) escuchan y comparten", "1-b, 2-a, 3-c", "Cada rol está en la ficha."),
        ex("Clasifica en CUMPLE o ROMPE la norma «se escucha sin interrumpir»: a) esperar el turno b) hablar encima de otra persona.", "a cumple, b rompe", "Esperar el turno es escuchar."),
        arith("Hay 3 normas inventadas: llegar a la hora, escuchar sin interrumpir y apagar el teléfono. Si cumples 2, ¿cuántas te faltan?", "3-2", "Se restan las cumplidas."),
    ],
    Z=[
        ex("Pedro llega a la mitad del encuentro y se pone a conversar fuerte. ¿Qué dos normas inventadas rompe?", "Llegar a la hora y escuchar sin interrumpir", "Llegó tarde e interrumpió."),
        ex("Ana dice: «Yo quiero guiar la conversación porque sé mucho». ¿Qué debe considerar? A) el rol lo define la comunidad B) el que sabe más manda", "A", "No decide ella."),
    ],
    D=[
        ex("Dos niñas llegan a un evento real de su zona. Una pregunta «¿cómo debo comportarme?», la otra supone que es igual al Encuentro de Valle Alto. ¿Cuál actúa mejor?", "La primera", "Pregunta lo que no sabe."),
        ex("Las normas del Encuentro de Valle Alto son inventadas. ¿Sirven para saber las normas de un evento real? Responde Sí o No.", "No", "Las reales las cuenta la comunidad."),
    ],
    context=[ex("Tu curso visitará un encuentro abierto de la comunidad. ¿Qué haces antes? A) preguntar al educador tradicional qué normas hay B) suponer que son las del recreo", "A", "Cada evento tiene sus normas.")],
    selfcheck=[
        ex("Escribe qué es un rol.", "La tarea o lugar que le corresponde a una persona en un evento", "Es la definición."),
        ex("Verdadero o falso: puedo suponer las normas de un evento real.", "Falso", "Siempre se pregunta antes."),
        ex("Escribe una norma general de respeto.", "Saludar, escuchar o esperar turno", "Son normas generales."),
    ],
    task=T("Con el Encuentro inventado de Valle Alto: doña Rosa organiza, don Pedro guía la conversación y las personas invitadas llegan a la hora, escuchan sin interrumpir y no usan el teléfono. Haz dos cuadros: «Roles» (tres filas) y «Normas» (tres filas). Escribe cómo te comportarías tú como persona invitada. Añade una pregunta para el educador tradicional sobre las normas de un evento abierto de tu comunidad.",
           "Roles: doña Rosa organiza; don Pedro guía; las personas invitadas escuchan y comparten. Normas: llegar a la hora; escuchar sin interrumpir; no usar el teléfono. Yo llegaría a la hora y escucharía. Pregunta: ¿qué normas hay en los eventos abiertos de nuestra comunidad?",
           ["completa los dos cuadros con datos de la ficha", "describe su comportamiento", "formula una pregunta"], ["dos cuadros", "frase de comportamiento"], ["inventar normas reales de un pueblo", "asignarse el rol de guía"],
           "Revisar que cada rol y norma estén en la ficha; valorar la pregunta final."),
    reinforce="Escribe tres normas de respeto que usas en tu sala.",
    extend="Compara las normas de la sala con las del Encuentro inventado: escribe una igual y una distinta.",
)

L(
    OA11, 3,
    materials="Lápiz y hojas. Los casos están escritos aquí y son inventados.",
    use="Aprenderé a analizar quién puede participar en un evento y qué cuidados hay que tener, como pedir consentimiento. Sirve para respetar a las personas y a la comunidad.",
    prior=["Sé que cada evento tiene roles y normas.", "Sé que hay cosas que se resguardan."],
    explain=[
        "Participar es tomar parte en una actividad. En algunos eventos pueden participar muchas personas. En otros, solo las invitadas o las de la comunidad. Es importante preguntar antes de llegar y aceptar la respuesta.",
        "El consentimiento es el permiso que se pide y se recibe antes de hacer algo, como sacar una foto, grabar o preguntar. Si la persona dice que no, respetamos su no. Esto vale para las personas y para los eventos.",
        "Algunas partes de un evento se resguardan. Esto significa que la comunidad decide no mostrarlas ni publicarlas. Si hay resguardo, no se graba, no se fotografía y no se cuenta a otras personas. Respetar esa decisión es parte de participar bien.",
    ],
    vocab=[("consentimiento", "permiso que se pide y se recibe antes de hacer algo"), ("participar", "tomar parte en una actividad"), ("resguardo", "cuidado para proteger algo importante"), ("grabar", "guardar sonido o imagen con un aparato"), ("aceptar", "recibir una respuesta sin insistir")],
    worked=[
        W("Pedir consentimiento", "En el Encuentro inventado de Valle Alto, Mía quiere sacar una foto a don Pedro. ¿Qué debe hacer primero?", ["Pregunta a don Pedro.", "Espera su respuesta.", "Si dice no, no saca la foto."], "Pedir permiso a don Pedro y aceptar su respuesta."),
        W("Un resguardo", "La ficha dice: «La parte final del encuentro es solo para la comunidad». Un invitado quiere quedarse. ¿Qué hace?", ["La ficha dice que es solo de la comunidad.", "Es un resguardo.", "Se retira con respeto."], "Se retira, porque esa parte es solo de la comunidad."),
    ],
    mistakes=[
        M("Sacar fotos de un evento sin preguntar.", "Se pasa por encima del consentimiento y del resguardo.", "Pregunta antes de sacar fotos o grabar."),
        M("Insistir cuando la respuesta es no.", "El no se respeta siempre.", "Acepta el no y agradece."),
    ],
    R=[
        ex("Antes de sacar una foto a una persona, ¿pides permiso o sacas la foto primero?", "Pido permiso", "Eso es el consentimiento."),
        ex("Si la persona dice que no, ¿insistes o aceptas?", "Aceptas", "El no se respeta."),
        ex("La parte final del encuentro es solo para la comunidad. ¿Puedes grabarla? Responde Sí o No.", "No", "Es un resguardo."),
    ],
    C=[
        ex("¿Qué es el consentimiento? A) el permiso que se pide y se recibe antes de hacer algo B) un tipo de evento", "A", "Se pide antes."),
        ex("Verdadero o falso: todos los eventos son para cualquier persona.", "Falso", "Algunos son solo para invitados o la comunidad."),
        ex("Verdadero o falso: si sacas una foto sin permiso, igual puedes subirla a internet.", "Falso", "Falta el consentimiento."),
    ],
    A=[
        ex("Ordena: a) sacar la foto si te dicen que sí b) preguntar si puedes sacar una foto. ¿Cuál letra va primero?", "b", "Primero se pide el permiso y después se actúa."),
        ex("Clasifica en PIDE CONSENTIMIENTO o NO LO PIDE: a) pregunta antes de grabar b) saca fotos sin avisar.", "a pide consentimiento, b no lo pide", "Preguntar antes es pedirlo."),
        arith("Un encuentro tiene 4 partes. La parte 4 es solo de la comunidad. ¿En cuántas partes puede participar una persona invitada?", "4-1", "Se resta la parte reservada."),
    ],
    Z=[
        ex("Tomás dice: «Si es un evento público, puedo grabar todo». ¿Qué error comete?", "No pide consentimiento", "Aun en eventos públicos se pide permiso."),
        ex("Ema se quedó en la parte final aunque era solo de la comunidad. ¿Qué hizo mal?", "No respetó el resguardo", "La ficha dice que esa parte es solo de la comunidad."),
    ],
    D=[
        ex("Dos niños: uno pregunta «¿puedo sacar una foto?» y otro la saca y pregunta después. ¿Quién respeta el consentimiento?", "El primero", "Pidió permiso antes."),
        ex("Una comunidad dice que no quiere fotos de su evento. ¿Aceptas, aunque quisieras mostrarlas a tu curso? A) sí, acepto B) no, las saco", "A", "El no se respeta."),
    ],
    context=[ex("Tu curso fue a un encuentro abierto. Un compañero quiere grabar un canto sin preguntar. ¿Qué le dices? A) «Pregunta primero si se puede» B) «Grábalo rápido»", "A", "Se pide consentimiento.")],
    selfcheck=[
        ex("Escribe qué es el consentimiento.", "El permiso que se pide y se recibe antes de hacer algo", "Es la definición."),
        ex("Verdadero o falso: se puede grabar una parte resguardada si nadie mira.", "Falso", "El resguardo se respeta siempre."),
        ex("¿Qué haces si te dicen que no?", "Acepto el no", "El no se respeta."),
    ],
    task=T("Lee este caso inventado: «En el Encuentro de Valle Alto hay una parte pública y una parte final solo para la comunidad. Tomás quiere sacar fotos de todo el encuentro y subirlas a internet.» Escribe tres consejos para Tomás: qué debe preguntar, qué no debe hacer en la parte final y qué haría si le dicen que no. Añade una pregunta para el educador tradicional sobre cómo participar bien en eventos de tu comunidad.",
           "1 Preguntar si puede sacar fotos. 2 No sacar fotos ni quedarse en la parte final. 3 Si le dicen que no, aceptar y agradecer. Pregunta: ¿cómo podemos participar bien en los eventos de nuestra comunidad?",
           ["da los tres consejos", "menciona el consentimiento y el resguardo", "formula una pregunta"], ["tres consejos", "pregunta"], ["decir que en un evento público se puede grabar todo", "no mencionar el no"],
           "Preguntar por qué la parte final es distinta; valorar el consejo sobre aceptar un no."),
    reinforce="Subraya en el caso las palabras que indican cuidado y permiso.",
    extend="Escribe una regla de tres frases para tu curso sobre fotos y grabaciones.",
)

L(
    OA11, 4,
    materials="Lápiz y hojas. El cuaderno de visita inventado está escrito aquí.",
    use="Aprenderé a contar lo que viví en un evento sin mostrar ni repetir lo que la comunidad resguarda. Sirve para agradecer y compartir con respeto.",
    prior=["Sé qué es el consentimiento y el resguardo.", "Sé que los eventos tienen roles y normas."],
    explain=[
        "Comunicar es contar lo vivido a otras personas. Después de visitar un evento, podemos escribir un relato o hacer un dibujo. Pero antes de escribir, nos preguntamos qué se puede compartir y qué no.",
        "Lo restringido es lo que la comunidad pide no mostrar, no grabar ni repetir. Eso no lo escribimos, no lo dibujamos y no lo imitamos. Podemos decir que existe una parte que se resguarda, sin contar qué pasó en ella.",
        "Un buen relato dice quién nos invitó, qué evento fue, qué aprendimos y qué normas respetamos. Termina con un agradecimiento. Si no estamos seguros de que algo se puede contar, le preguntamos al educador tradicional antes de publicarlo.",
    ],
    vocab=[("comunicar", "contar lo vivido a otras personas"), ("restringido", "que no se puede mostrar ni repetir"), ("relato", "texto que cuenta algo que pasó"), ("agradecer", "reconocer lo que otra persona nos dio"), ("publicar", "mostrar algo a muchas personas")],
    worked=[
        W("Qué se puede escribir", "Cuaderno de visita inventado: «Fuimos al Encuentro de Valle Alto. Doña Rosa nos recibió. Conversamos y compartimos comida. En la parte final, que es solo de la comunidad, nos retiramos.» ¿Qué dato es restringido?", ["Revisa qué se pidió resguardar.", "La parte final es de la comunidad.", "Lo que pasó allí no se cuenta."], "Lo que pasó en la parte final."),
        W("Escribir con respeto", "Escribe una frase que diga que hubo una parte resguardada sin contarla.", ["Digo que existe esa parte.", "No cuento qué pasó.", "Agrego que la respetamos."], "Hubo una parte solo para la comunidad y la respetamos."),
    ],
    mistakes=[
        M("Contar lo que ocurrió en la parte restringida «para completar el relato».", "Rompe el resguardo.", "Cuenta solo lo que se puede compartir."),
        M("Publicar el relato sin consultar.", "La comunidad podría no estar de acuerdo.", "Pregunta al educador tradicional antes."),
    ],
    R=[
        ex("En el cuaderno de visita, ¿quién recibió al curso?", "Doña Rosa", "El cuaderno lo dice."),
        ex("¿Qué se hizo en la parte final que es solo de la comunidad? A) el curso se retiró B) el curso grabó", "A", "El cuaderno dice que se retiraron."),
        ex("Lo que pasó en la parte restringida, ¿se cuenta o no se cuenta?", "No se cuenta", "Eso es algo restringido."),
    ],
    C=[
        ex("¿Qué es lo restringido? A) lo que la comunidad pide no mostrar ni repetir B) lo que ya se publicó", "A", "El no se respeta."),
        ex("Verdadero o falso: un buen relato termina agradeciendo.", "Verdadero", "Reconoce lo recibido."),
        ex("Verdadero o falso: si no estás seguro de que algo se puede contar, lo publicas igual.", "Falso", "Se pregunta antes."),
    ],
    A=[
        ex("Del cuaderno de visita, escribe dos datos que sí se pueden compartir.", "Doña Rosa nos recibió; conversamos y compartimos comida", "Son datos abiertos del evento."),
        ex("Clasifica en SE PUEDE o NO SE PUEDE contar: a) quién nos recibió b) lo que pasó en la parte reservada.", "a se puede, b no se puede", "La parte reservada no se cuenta."),
        ex("En un buen relato de visita, ¿qué va al final: el agradecimiento o decir quién invitó?", "El agradecimiento", "El relato termina agradeciendo."),
    ],
    Z=[
        ex("Ema dibuja lo que supone que pasó en la parte reservada. ¿Qué error comete?", "Inventa y rompe el resguardo", "Esa parte no se cuenta ni se imagina."),
        ex("Pedro publica el relato del curso sin preguntar. ¿Qué debió hacer?", "Preguntar al educador tradicional antes", "La comunidad puede no estar de acuerdo."),
    ],
    D=[
        ex("Dos relatos: 1) «Fuimos, conversamos y respetamos la parte reservada. Gracias.» 2) «Fuimos y contamos lo que pasó en la parte reservada.» ¿Cuál respeta mejor?", "El 1", "No cuenta lo restringido."),
        ex("Quieres mostrar tu relato en la feria de la escuela. ¿Qué haces antes? A) consultar si se puede compartir B) mostrarlo sin avisar", "A", "Se pide consentimiento."),
    ],
    context=[ex("Tu curso hará un diario mural sobre su visita al Encuentro inventado de Valle Alto. ¿Qué incluye? A) lo que se puede compartir y un agradecimiento B) fotos de la parte reservada", "A", "Respeta el resguardo.")],
    selfcheck=[
        ex("Escribe qué es lo restringido.", "Lo que la comunidad pide no mostrar ni repetir", "Es la definición."),
        ex("Verdadero o falso: puedo contar una parte reservada si la cambio un poco.", "Falso", "Sigue siendo reservada."),
        ex("¿Cómo terminas un buen relato?", "Con un agradecimiento", "Reconoce lo recibido."),
    ],
    task=T("Escribe un relato de seis a ocho líneas sobre la visita inventada al Encuentro de Valle Alto, usando este cuaderno de visita: «Doña Rosa nos recibió. Conversamos y compartimos comida. Escuchamos a don Pedro sin interrumpir. La parte final es solo de la comunidad y nos retiramos.» Tu relato debe decir quién invitó, qué hicieron, qué norma respetaron y terminar con un agradecimiento. No cuentes ni dibujes la parte final. Pregunta al educador tradicional si puedes publicarlo.",
           "Fuimos al Encuentro de Valle Alto. Doña Rosa nos recibió. Conversamos, compartimos comida y escuchamos a don Pedro sin interrumpir. Hubo una parte solo para la comunidad y la respetamos. Gracias, doña Rosa, por invitarnos.",
           ["dice quién invitó y qué hicieron", "menciona una norma respetada", "no cuenta lo restringido", "agradece"], ["relato de seis a ocho líneas"], ["inventar lo que pasó en la parte final", "publicar sin preguntar"],
           "Preguntar qué parte no contó y por qué; valorar el agradecimiento."),
    reinforce="Subraya en tu relato la frase que respeta el resguardo.",
    extend="Escribe una regla de cuatro frases sobre cómo contar lo vivido en un evento sin mostrar lo restringido.",
)
