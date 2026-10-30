"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA 15 (patrimonio cultural: comida, música, ceremonia, sitios, medicina, historia; recrear solo lo autorizado)
y OA 16 (ciencia indígena en relación con naturaleza y cosmos).

Criterio de autoría: las comunidades, las personas, las fichas y los saberes de práctica son INVENTADOS y se
rotulan así. No se describe ninguna receta, canción, ceremonia, remedio, sitio, cosmovisión ni conocimiento
astronómico de un pueblo concreto. Los saberes de salud y de ceremonia quedan para las personas que los
guardan. Lo tradicional lo enseñan el educador o la educadora tradicional y la comunidad.
"""
from __future__ import annotations

from student_content_lc4_a import FC4, FV4, L, M, T, W  # noqa: F401
from student_lessons import arith, ex  # noqa: F401

OA15, OA16 = "LC04 OA 15", "LC04 OA 16"

PAT = ("Lista de práctica (inventada) de Valle Alto: 1) un guiso que se prepara con lo que da la huerta comunitaria; 2) una canción de saludo que se canta al recibir visitas; "
       "3) el cerro Pelado, que la comunidad cuida; 4) un sitio con restos antiguos, que se visita solo con guía y sin tocar nada; "
       "5) una ceremonia de la comunidad que no se cuenta; 6) saberes de salud que guardan algunas personas de la comunidad; 7) relatos de las abuelas y los abuelos sobre cómo era antes el valle.")

# ============================================================ OA 15 · Patrimonio cultural de comunidad, territorio y pueblo
L(
    OA15, 1,
    materials="Lápiz y hojas. La lista está escrita aquí y es inventada.",
    use="Aprenderé a reconocer diferentes manifestaciones del patrimonio cultural de una comunidad: comidas, música, ceremonias, lugares naturales, sitios antiguos, saberes de salud e historias. Sirve para valorar que el patrimonio es vivo y variado.",
    prior=["Sé que las culturas indígenas están vivas hoy.", "Sé que algunos saberes se comparten y otros se resguardan."],
    explain=[
        "El patrimonio cultural es lo que una comunidad recibe de sus antepasados, mantiene hoy y quiere transmitir a las generaciones futuras. Incluye cosas que se pueden tocar, como un sitio o un objeto, y cosas que se viven, como una comida, una canción, una ceremonia, un relato o un saber de salud.",
        "Cada comunidad tiene su propio patrimonio. Hay comidas, música, ceremonias, espacios naturales, sitios arqueológicos, historias y saberes de salud, entre otras manifestaciones. Un sitio arqueológico es un lugar con restos de personas del pasado. En Chile, estos sitios están protegidos por la ley: no se excavan ni se llevan objetos.",
        "Distinguir los tipos de patrimonio ayuda a cuidarlo. Algunas manifestaciones se comparten con todos y otras se resguardan. Que algo sea patrimonio no significa que sea de todos: pertenece a la comunidad que lo mantiene. Para conocer el patrimonio de un pueblo real, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("patrimonio cultural", "lo que una comunidad recibe de sus antepasados, mantiene hoy y quiere transmitir"), ("manifestación", "forma en que se expresa el patrimonio, como una comida o una canción"), ("sitio arqueológico", "lugar con restos de personas del pasado, protegido por la ley"), ("espacio natural", "lugar de la naturaleza importante para la comunidad"), ("transmitir", "pasar un saber a otras personas")],
    worked=[
        W("Clasificar manifestaciones", "Con la lista de Valle Alto: «" + PAT + "» ¿Cuáles son vivas (se practican) y cuáles son lugares?", ["Se practican: el guiso, la canción, la ceremonia, los saberes de salud y los relatos.", "Son lugares: el cerro Pelado y el sitio con restos antiguos.", "Los separo."], "Vivas: 1, 2, 5, 6 y 7. Lugares: 3 y 4."),
        W("Cuidar el patrimonio", "¿Qué se hace con el sitio con restos antiguos?", ["La lista dice que se visita solo con guía.", "No se toca nada.", "La ley también lo protege."], "Se visita con guía, sin tocar nada, y la ley lo protege."),
    ],
    mistakes=[
        M("Pensar que el patrimonio son solo objetos antiguos.", "También incluye comidas, canciones, saberes y relatos que se viven hoy.", "Busca prácticas vivas y lugares."),
        M("Llevarse un objeto de un sitio antiguo como recuerdo.", "Está protegido por la ley y su cuidado nos corresponde a todos.", "No se toca ni se saca nada."),
    ],
    R=[
        ex("Según la lista, ¿cuál es un espacio natural que cuida la comunidad: el cerro Pelado o la canción de saludo?", "El cerro Pelado", "Es un lugar de la naturaleza."),
        ex("¿Qué manifestación se canta al recibir visitas en la lista de Valle Alto?", "La canción de saludo", "La lista lo dice."),
        ex("¿Se puede llevar un objeto de un sitio arqueológico? Responde Sí o No.", "No", "Está protegido por la ley."),
    ],
    C=[
        ex("¿Qué es el patrimonio cultural? A) lo que una comunidad recibe, mantiene y quiere transmitir B) un objeto comprado en una tienda", "A", "Es la herencia viva de una comunidad."),
        ex("Verdadero o falso: una comida puede ser patrimonio cultural.", "Verdadero", "Es una manifestación viva."),
        ex("Verdadero o falso: el patrimonio de una comunidad pertenece a cualquiera que lo quiera usar.", "Falso", "Pertenece a la comunidad que lo mantiene."),
    ],
    A=[
        ex("Clasifica en LUGAR o PRÁCTICA VIVA: a) el cerro Pelado b) la canción de saludo c) el sitio con restos antiguos.", "a lugar, b práctica viva, c lugar", "El cerro y el sitio son lugares; la canción se practica."),
        ex("Une cada manifestación con su tipo. 1) guiso de la huerta 2) relatos de los abuelos a) comida b) historia oral", "1-a, 2-b", "El guiso es comida; los relatos son historia."),
        ex("Cuenta cuántas manifestaciones tiene la lista de práctica de Valle Alto. Escribe el número.", "7", "La lista numera siete manifestaciones."),
    ],
    Z=[
        ex("Tomás dice: «La música no es patrimonio porque no se puede tocar». ¿Qué error comete?", "Piensa que el patrimonio solo son objetos", "También incluye prácticas vivas como la música."),
        ex("¿Por qué se visita el sitio antiguo solo con guía? A) para cuidarlo y no dañarlo B) para cobrar entrada", "A", "El guía ayuda a protegerlo."),
    ],
    D=[
        ex("Dos frases: 1) «El patrimonio de Valle Alto incluye comida, música y lugares» 2) «El patrimonio de todos los pueblos es igual». ¿Cuál se apoya en la lista?", "La primera", "La segunda generaliza."),
        ex("Si quieres conocer el patrimonio de un pueblo real, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a quien lo vio en una foto", "A", "Ellos lo explican."),
    ],
    context=[ex("En una excursión encuentras una piedra con forma extraña cerca de un sitio antiguo. ¿Qué haces? A) aviso al guía o al adulto y no la toco B) me la llevo", "A", "Los sitios y sus objetos se protegen.")],
    selfcheck=[
        ex("Escribe dos tipos de manifestación del patrimonio cultural.", "Dos entre: comida, música, ceremonia, espacio natural, sitio arqueológico, saber de salud, historia", "Están en la explicación."),
        ex("Verdadero o falso: el patrimonio solo son cosas del pasado.", "Falso", "También se vive hoy."),
        ex("¿Qué haces con un sitio arqueológico? A) lo cuido sin tocar nada B) me llevo un recuerdo", "A", "La ley lo protege."),
    ],
    task=T("Lee la lista de práctica de Costa Clara (inventada): «1) un caldo de pescado de la caleta; 2) una canción de trabajo que se canta al arreglar redes; 3) las rocas planas de la caleta; 4) un lugar con restos antiguos, que se visita con guía; 5) una ceremonia que no se cuenta; 6) historias de los pescadores mayores.» Clasifica cada elemento en comida, música, espacio natural, sitio arqueológico, ceremonia o historia. Marca con una estrella los que se resguardan y escribe una pregunta al educador tradicional sobre el patrimonio de tu zona.",
           "1 comida; 2 música; 3 espacio natural; 4 sitio arqueológico; 5 ceremonia (se resguarda); 6 historia. Pregunta: ¿qué patrimonio de nuestra zona se puede conocer y cuál se resguarda?",
           ["clasifica bien los seis elementos", "marca lo resguardado", "formula una pregunta respetuosa"], ["tabla de clasificación", "pregunta"], ["confundir práctica con lugar", "describir la ceremonia"],
           "Pedir que justifique cada clasificación; valorar que no describa lo resguardado."),
    reinforce="Haz una lista con tres manifestaciones del patrimonio de tu zona que ya conozcas, sin datos personales.",
    extend="Explica con tus palabras por qué un sitio arqueológico lo protege la ley y por qué se visita con guía.",
)

L(
    OA15, 2,
    materials="Lápiz y hojas. Las tarjetas de fuentes están escritas aquí y son inventadas.",
    use="Aprenderé a investigar la procedencia y el significado de una manifestación del patrimonio. Sirve para distinguir fuentes confiables de otras que no lo son.",
    prior=["Sé reconocer manifestaciones del patrimonio.", "Sé preguntar quién cuenta y con qué permiso."],
    explain=[
        "La procedencia es el origen de algo: de qué comunidad viene, quién lo guarda y cómo llegó hasta nosotros. El significado es lo que representa para la comunidad. Ambos los explica la comunidad; desde fuera solo podemos recoger lo que ella autoriza compartir.",
        "Una fuente es más confiable cuando es de la comunidad o está validada por ella, nombra a quien cuenta, dice cuándo y con qué permiso se compartió y reconoce sus límites. Una fuente es menos confiable cuando es anónima, no dice de dónde sacó los datos o mezcla comunidades sin distinguirlas.",
        "Al investigar una manifestación, completamos una ficha con cuatro datos: comunidad, quién cuenta, qué dice sobre su origen y significado, y qué límite declara. Si falta alguno, buscamos otra fuente o preguntamos al educador o educadora tradicional. No completamos con suposiciones.",
    ],
    vocab=[("procedencia", "origen de algo: de qué comunidad viene y quién lo guarda"), ("significado", "lo que algo representa para la comunidad"), ("fuente confiable", "fuente que nombra a quien cuenta, dice de dónde viene y respeta los límites"), ("anónimo", "sin nombre de autor"), ("validar", "reconocer que algo es correcto según la comunidad")],
    worked=[
        W("Evaluar dos fuentes", "Tarjeta A (inventada): «Según doña Rosa, de Valle Alto, el guiso se prepara con lo que da la huerta y se comparte en la explanada. Ella autorizó contarlo.» Tarjeta B: «Un sitio de internet sin nombre dice que todos los pueblos preparan el mismo guiso.» ¿Cuál es más confiable?", ["A nombra a doña Rosa y la comunidad.", "A dice que hay autorización.", "B es anónima y generaliza."], "La tarjeta A."),
        W("Completar la ficha", "Con la tarjeta A, completa comunidad, quién cuenta, origen y significado.", ["Comunidad: Valle Alto.", "Cuenta: doña Rosa.", "Origen y significado: se prepara con lo que da la huerta y se comparte en la explanada."], "Valle Alto; doña Rosa; se prepara con la huerta y se comparte."),
    ],
    mistakes=[
        M("Confiar en una fuente solo porque suena segura.", "Puede no nombrar a quien cuenta ni respetar límites.", "Revisa los cuatro datos de la ficha."),
        M("Completar el significado con lo que parece lógico.", "El significado lo da la comunidad.", "Deja en blanco lo que no dice la fuente."),
    ],
    R=[
        ex("En la tarjeta A, ¿quién cuenta cómo se prepara el guiso?", "Doña Rosa", "La tarjeta la nombra."),
        ex("¿Dónde se comparte el guiso según la tarjeta A: en la explanada o en la playa?", "En la explanada", "La tarjeta lo dice."),
        ex("¿La tarjeta B nombra a quien cuenta? Responde Sí o No.", "No", "La tarjeta B es anónima."),
    ],
    C=[
        ex("¿Qué es la procedencia? A) el origen de algo y quién lo guarda B) un tipo de comida", "A", "Es el origen."),
        ex("Verdadero o falso: una fuente anónima es igual de confiable que una que nombra a la comunidad.", "Falso", "Una fuente anónima no dice de dónde viene."),
        ex("Verdadero o falso: el significado de una manifestación lo explica la comunidad.", "Verdadero", "Ella lo conoce."),
    ],
    A=[
        ex("Tarjeta C (inventada): «Don Luis, de Costa Clara, cuenta que el caldo de pescado se comparte después de una buena pesca. Autorizó contarlo.» Escribe comunidad y quién cuenta.", "Costa Clara y don Luis", "Están en la tarjeta."),
        ex("Clasifica cada fuente en CONFIABLE o MENOS CONFIABLE: a) una persona de la comunidad que autoriza b) un texto anónimo que mezcla comunidades.", "a confiable, b menos confiable", "La primera nombra y tiene permiso; la segunda no."),
        ex("Una tarjeta no dice de qué comunidad viene. ¿Qué haces? A) busco otra fuente o pregunto al educador tradicional B) la uso igual", "A", "Falta un dato clave."),
    ],
    Z=[
        ex("Lucía dice: «El significado del guiso es que simboliza la unidad de todos los pueblos». ¿Qué error comete?", "Inventa un significado que la fuente no da", "El significado lo da la comunidad."),
        ex("¿Por qué conviene que la fuente declare sus límites? A) para saber qué no se debe agregar B) para ser más larga", "A", "El límite protege lo reservado."),
    ],
    D=[
        ex("Dos fichas completas: A) nombra comunidad, fuente, origen y límite; B) solo tiene el origen. ¿Cuál es mejor para un trabajo?", "A", "Tiene los cuatro datos."),
        ex("¿Qué ficha de datos debes completar para investigar una manifestación? Escribe dos de los cuatro datos.", "Dos entre: comunidad, quién cuenta, origen y significado, límite", "Son los cuatro datos de la clase."),
    ],
    context=[ex("Para tu exposición encuentras dos textos sobre una canción de una comunidad. Uno nombra al autor y a la comunidad y el otro no. ¿Cuál usas? A) el que nombra B) el anónimo", "A", "Es más confiable.")],
    selfcheck=[
        ex("Nombra dos señales de una fuente confiable.", "Dos entre: nombra a quien cuenta, dice de dónde viene, tiene permiso, declara límites", "Están en la explicación."),
        ex("Verdadero o falso: puedo completar el significado con lo que me parece lógico.", "Falso", "Lo da la comunidad."),
        ex("¿Qué haces si falta un dato de la ficha? A) busco otra fuente o pregunto B) lo supongo", "A", "No se suponen datos."),
    ],
    task=T("Lee dos tarjetas inventadas. Tarjeta 1: «Doña Rosa, de Valle Alto, cuenta que la canción de saludo se canta al recibir visitas. Autorizó contarlo. No se cuenta su letra completa.» Tarjeta 2: «En un video sin nombre dicen que todas las comunidades saludan igual». Completa una ficha de cuatro datos para la tarjeta 1 (comunidad, quién cuenta, origen y significado, límite) y explica en dos frases por qué la tarjeta 2 es menos confiable.",
           "Comunidad: Valle Alto. Cuenta: doña Rosa. Origen y significado: se canta al recibir visitas (el resto del significado no se cuenta). Límite: no se cuenta la letra completa. La tarjeta 2 es anónima y generaliza a todas las comunidades.",
           ["completa los cuatro datos con la tarjeta 1", "explica por qué la tarjeta 2 es menos confiable", "no inventa significados"], ["ficha de cuatro datos", "dos frases"], ["inventar el significado", "generalizar"],
           "Pedir que muestre en la tarjeta cada dato; valorar que declare el límite."),
    reinforce="Rodea en una tarjeta el nombre de quien cuenta y la comunidad.",
    extend="Escribe una pregunta que le harías a una persona mayor de tu comunidad sobre el origen de una comida de tu zona.",
)

L(
    OA15, 3,
    materials="Lápiz y hojas. La lista está escrita aquí y es inventada.",
    use="Aprenderé a distinguir qué parte del patrimonio es de acceso público y qué parte es restringida, y a actuar con respeto en cada caso. Sirve para visitar, aprender y compartir sin dañar.",
    prior=["Sé reconocer manifestaciones del patrimonio y su procedencia.", "Sé que algunos saberes se resguardan."],
    explain=[
        "Acceso público significa que la comunidad permite que cualquier persona conozca o participe, por ejemplo en una feria o en un museo comunitario. Acceso restringido significa que la comunidad limita quién puede ver, saber o participar, por ejemplo en una ceremonia o en saberes de salud que guardan ciertas personas.",
        "La comunidad es quien decide qué es público y qué es restringido, y sus razones merecen respeto aunque no las conozcamos. Cuando algo es restringido, no se graba, no se fotografía, no se busca otra manera de verlo y no se publica en internet. Tampoco se dan indicaciones de salud o de ceremonia: eso lo hacen las personas que los guardan.",
        "Los sitios arqueológicos son un caso especial: se pueden visitar con autorización y guía, pero no se tocan ni se sacan objetos, porque la ley los protege. Si no sabemos si algo es público o restringido, preguntamos al educador o educadora tradicional antes de actuar.",
    ],
    vocab=[("acceso público", "permiso para que cualquiera conozca o participe"), ("acceso restringido", "permiso solo para ciertas personas"), ("saber de salud", "conocimiento sobre cuidar el cuerpo que guardan ciertas personas"), ("publicar", "mostrar algo para que muchas personas lo vean"), ("autorización", "permiso para visitar o compartir")],
    worked=[
        W("Clasificar", "Ficha inventada de Valle Alto: «La feria de la comunidad y la canción de saludo ante visitas son públicas. La ceremonia y los saberes de salud son restringidos.» ¿Qué es público y qué restringido?", ["La feria y la canción de saludo se comparten con visitas.", "La ceremonia y los saberes de salud están limitados.", "Los separo."], "Público: feria y canción de saludo. Restringido: ceremonia y saberes de salud."),
        W("Actuar con respeto", "Quieres filmar la ceremonia. ¿Qué haces?", ["Es restringida.", "No se graba ni se fotografía.", "Respeto el límite."], "No filmo; respeto la decisión de la comunidad."),
    ],
    mistakes=[
        M("Pensar que si algo se puede ver, se puede grabar.", "Puede ser restringido.", "Pregunta antes."),
        M("Dar consejos de salud basados en un saber tradicional.", "Eso corresponde a quienes lo guardan.", "Remite a la persona que lo guarda."),
    ],
    R=[
        ex("¿La ceremonia de Valle Alto (inventada) es de acceso público o restringido?", "Restringido", "La lista dice que no se cuenta."),
        ex("¿La canción de saludo ante visitas es pública o restringida?", "Pública", "Se canta ante visitas."),
        ex("¿Se puede tocar un objeto de un sitio arqueológico? Responde Sí o No.", "No", "El sitio está protegido por la ley."),
    ],
    C=[
        ex("¿Qué es el acceso restringido? A) permiso solo para ciertas personas B) permiso para cualquiera", "A", "Limita quién puede ver o participar."),
        ex("Verdadero o falso: la comunidad decide qué es público y qué es restringido.", "Verdadero", "Es su decisión."),
        ex("Verdadero o falso: puedo dar consejos de salud basados en un saber tradicional.", "Falso", "Eso corresponde a quienes lo guardan."),
    ],
    A=[
        ex("Ficha inventada de Costa Clara: «La feria es pública; los saberes de salud son restringidos». Clasifica: a) la feria b) los saberes de salud.", "a público, b restringido", "Lo dice la ficha."),
        ex("Quieres sacar fotos de un lugar restringido. ¿Qué haces? A) no las saco B) las saco rápido", "A", "El límite se respeta."),
        ex("Un sitio arqueológico se visita con guía. ¿Qué haces ahí? A) miro sin tocar nada B) me llevo una piedra", "A", "La ley lo protege."),
    ],
    Z=[
        ex("Camilo dice: «Si lo puedo ver, lo puedo publicar». ¿Qué error comete?", "Confunde ver con tener permiso para publicar", "Ver no es autorización."),
        ex("¿Por qué los saberes de salud no se enseñan en la sala? A) porque los guardan ciertas personas que saben cuidarlos B) porque son aburridos", "A", "Su manejo requiere a quienes los guardan."),
    ],
    D=[
        ex("Dos conductas ante un sitio antiguo: 1) mirar con guía sin tocar 2) llevarse un recuerdo. ¿Cuál es respetuosa?", "La primera", "La segunda daña el sitio."),
        ex("Si no sabes si una manifestación es pública o restringida, ¿qué haces? A) pregunto al educador tradicional B) la publico", "A", "Se pregunta antes de actuar."),
    ],
    context=[ex("Visitas una muestra pública de una comunidad y alguien te ofrece mostrar «un secreto» de una ceremonia. ¿Qué respondes? A) gracias, prefiero lo que la comunidad autorizó B) sí, cuéntamelo", "A", "Se respeta el límite.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es el acceso público.", "Permiso para que cualquiera conozca o participe", "Es la definición de la clase."),
        ex("Verdadero o falso: lo restringido se puede buscar por otro lado.", "Falso", "Se respeta el límite."),
        ex("¿Quién decide qué es restringido? A) la comunidad B) quien lo ve", "A", "Es su patrimonio."),
    ],
    task=T("Lee la lista inventada de Costa Clara: «Feria de la caleta (pública); caldo de pescado compartido en la feria (público); canción de trabajo (pública, sin letra completa); ceremonia de la comunidad (restringida); saberes de salud (restringidos); sitio con restos antiguos (visita con guía).» Haz una tabla de tres columnas: público, restringido y con condiciones. Escribe una regla de tres puntos para tu curso al visitar la caleta.",
           "Público: feria, caldo, canción de trabajo. Restringido: ceremonia, saberes de salud. Con condiciones: sitio con restos antiguos (con guía). Regla: 1) preguntar antes de fotografiar, 2) no tocar el sitio, 3) respetar lo restringido.",
           ["clasifica bien los elementos", "escribe una regla coherente", "respeta lo restringido"], ["tabla de tres columnas", "regla de tres puntos"], ["describir lo restringido", "ignorar las condiciones del sitio"],
           "Pedir que justifique cada columna; valorar la regla respetuosa."),
    reinforce="Colorea de verde lo público, de rojo lo restringido y de amarillo lo que tiene condiciones.",
    extend="Escribe cómo explicarías a un compañero por qué no basta con que algo sea visible para poder publicarlo.",
)

L(
    OA15, 4,
    materials="Lápiz, hojas o cartulina, lápices de colores. Se trabaja con ayuda de una persona de tu casa si se usan tijeras de punta redondeada.",
    use="Aprenderé a recrear un aspecto autorizado del patrimonio de forma respetuosa, aplicando un valor de la comunidad en una producción artística propia. Sirve para valorar el patrimonio sin copiar lo que no corresponde.",
    prior=["Sé distinguir lo público de lo restringido.", "Sé que inspirarse es distinto de copiar."],
    explain=[
        "Recrear significa crear algo nuevo a partir de algo que ya existe. Podemos recrear solo lo que la comunidad autoriza: por ejemplo, el paisaje de la huerta o un valor como «devolver al río lo que nos da», que aparece en la ficha de Valle Alto. No recreamos ceremonias, saberes de salud ni objetos con significado reservado.",
        "Una producción artística significativa y contextualizada tiene un propósito claro (qué valor expresa), está pensada para un lugar o un público (por ejemplo, el patio de la escuela) y reconoce de dónde viene la inspiración. Escribimos una nota como «Inspirado en el valor de devolver al río lo que nos da, que cuenta la ficha de práctica de Valle Alto».",
        "Para aplicar un aspecto de la cosmovisión en un trabajo propio, usamos solo lo que la ficha autoriza y lo presentamos como una interpretación nuestra, no como la voz de la comunidad. Si queremos acercarnos a una cosmovisión real, es el educador o educadora tradicional quien guía.",
    ],
    vocab=[("recrear", "crear algo nuevo a partir de algo que ya existe"), ("cosmovisión", "manera en que un pueblo entiende el mundo y la vida"), ("significativo", "que tiene sentido y propósito"), ("contextualizado", "pensado para un lugar y un público concretos"), ("interpretación propia", "mi manera de entender y expresar algo")],
    worked=[
        W("Elegir lo autorizado", "La ficha de Valle Alto autoriza usar el valor «devolver al río lo que nos da». ¿Qué puedes recrear: ese valor o una ceremonia?", ["La ficha autoriza el valor.", "La ceremonia es restringida.", "Recreo el valor."], "El valor «devolver al río lo que nos da»."),
        W("Planificar un afiche", "Planifica un afiche para el patio de la escuela que exprese ese valor.", ["Propósito: invitar a cuidar el agua del patio.", "Imagen: un río, una huerta y manos que riegan sin desperdiciar.", "Nota: inspirado en el valor que cuenta la ficha de Valle Alto."], "Afiche con río, huerta y manos, más la nota de inspiración."),
    ],
    mistakes=[
        M("Dibujar una ceremonia «para mostrarla».", "Es restringida y no corresponde recrearla.", "Elige un valor o un paisaje autorizado."),
        M("Presentar mi afiche como si hablara por la comunidad.", "Es mi interpretación.", "Escribe «inspirado en…»."),
    ],
    R=[
        ex("¿Qué valor autoriza recrear la ficha de Valle Alto: devolver al río lo que nos da o copiar un diseño reservado?", "Devolver al río lo que nos da", "La ficha lo autoriza."),
        ex("¿Se recrea una ceremonia restringida? Responde Sí o No.", "No", "Esa ceremonia no corresponde recrearla."),
        ex("¿Qué debe llevar la obra para reconocer su origen: una nota de inspiración o ninguna nota?", "Una nota de inspiración", "Reconoce de dónde viene la idea."),
    ],
    C=[
        ex("¿Qué significa contextualizado? A) pensado para un lugar y un público concretos B) copiado sin pensar", "A", "Tiene en cuenta dónde se muestra."),
        ex("Verdadero o falso: mi obra es la voz de la comunidad.", "Falso", "Es mi interpretación."),
        ex("Verdadero o falso: recrear es crear algo nuevo a partir de algo existente.", "Verdadero", "Es la definición de la clase."),
    ],
    A=[
        ex("Escribe una nota de inspiración para un afiche sobre devolver al río lo que nos da (ficha de Valle Alto).", "Inspirado en el valor de devolver al río lo que nos da, que cuenta la ficha de práctica de Valle Alto", "Nombra el valor y la ficha."),
        ex("Clasifica en AUTORIZADO o NO AUTORIZADO según la ficha: a) dibujar el paisaje de la huerta b) dibujar la ceremonia.", "a autorizado, b no autorizado", "La ceremonia se resguarda."),
        arith("Tu afiche tiene 4 filas con 5 gotas de agua dibujadas en cada una. ¿Cuántas gotas dibujaste en total?", "4*5", "Se repiten 5 gotas cuatro veces."),
    ],
    Z=[
        ex("Lucas dice: «Mi afiche es el arte tradicional de Valle Alto». ¿Qué error comete?", "Presenta su obra como si fuera la de la comunidad", "Es una obra inspirada, no la voz de la comunidad."),
        ex("¿Por qué ayuda pensar en dónde se mostrará la obra? A) porque la hace contextualizada B) porque es más grande", "A", "Piensa en el público."),
    ],
    D=[
        ex("Dos afiches: 1) un valor de la ficha con nota de inspiración 2) una copia de un símbolo reservado. ¿Cuál valora el patrimonio?", "El primero", "Recrea lo autorizado y reconoce su origen."),
        ex("Si una persona de la comunidad real te dice que tu obra no es adecuada, ¿qué haces? A) escucho y la cambio B) la mantengo igual", "A", "La comunidad orienta."),
    ],
    context=[ex("Tu curso hará un afiche para el patio sobre cuidar el agua, inspirado en la ficha de Valle Alto. ¿Qué agregan al final? A) una nota que diga en qué se inspiran B) nada", "A", "Reconoce el origen.")],
    selfcheck=[
        ex("Nombra dos rasgos de una producción significativa y contextualizada.", "Dos entre: propósito claro, pensada para un lugar o público, nota de inspiración", "Están en la explicación."),
        ex("Verdadero o falso: puedo recrear cualquier cosa de una comunidad si lo hago con cariño.", "Falso", "Solo lo autorizado."),
        ex("¿Cómo presentas tu obra? A) como interpretación propia B) como voz de la comunidad", "A", "No hablo por la comunidad."),
    ],
    task=T("Crea un afiche para el patio de tu escuela que exprese el valor «devolver al río lo que nos da» (de la ficha de práctica de Valle Alto). Incluye un título, un dibujo (por ejemplo, un río, una huerta y manos que riegan sin desperdiciar) y una nota de inspiración. Cuenta cuántos elementos dibujaste y escribe una frase que diga a quién va dirigido el afiche. No dibujes ceremonias ni símbolos reservados.",
           "Título: Devolvamos al río. Dibujo: un río, una huerta y 3 manos. Elementos: 5. Va dirigido a los estudiantes del patio. Nota: inspirado en el valor que cuenta la ficha de práctica de Valle Alto.",
           ["expresa el valor autorizado", "incluye nota de inspiración", "indica a quién va dirigido"], ["afiche", "frase de destinatario", "conteo de elementos"], ["recrear lo restringido", "presentarlo como obra de la comunidad"],
           "Pedir que explique el valor y el destinatario; valorar que no copie símbolos reservados."),
    reinforce="Reescribe tu nota de inspiración en una oración clara.",
    extend="Muestra tu afiche a un compañero y anota una sugerencia que recibiste.",
)

# ============================================================ OA 16 · Ciencia indígena en relación con naturaleza y cosmos
L(
    OA16, 1,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a situar una pregunta sobre la naturaleza y a reconocer la perspectiva de quien la responde. Sirve para entender que los saberes de las comunidades también responden preguntas sobre el mundo.",
    prior=["Sé situar una fuente con permiso y límite.", "Sé que los saberes se construyen y validan en la comunidad."],
    explain=[
        "Las comunidades han observado la naturaleza durante muchas generaciones y han construido conocimientos para responder preguntas: ¿cuándo termina la lluvia?, ¿cuándo está tranquilo el mar?, ¿cómo cuidar el suelo? Esos conocimientos se transmiten, se ponen a prueba con la experiencia y se validan en la comunidad.",
        "Una perspectiva es la manera de mirar una pregunta según quién la hace, desde dónde la mira y con qué experiencia. Una familia agricultora y una de pescadores miran distinto el clima, porque necesitan cosas distintas. La ciencia escolar también tiene su perspectiva: usa mediciones y registros que otros pueden repetir.",
        "Para situar una pregunta decimos: ¿quién la hace?, ¿qué quiere saber?, ¿de qué comunidad o fuente viene? y ¿qué parte no se cuenta? En esta unidad usamos fichas inventadas. Los conocimientos reales de un pueblo los explica el educador o educadora tradicional, y no se mezclan con lo que dice otra fuente sin avisar.",
    ],
    vocab=[("pregunta", "lo que se quiere saber sobre algo"), ("perspectiva", "manera de mirar algo según quién lo mira"), ("observación", "mirar con atención y anotar lo que se ve"), ("conocimiento", "saber que se ha comprobado y se transmite"), ("validar", "reconocer que algo es correcto según quien corresponde")],
    worked=[
        W("Situar la pregunta", "Ficha inventada: «Don Luis, de Costa Clara, se pregunta cuándo es seguro salir a pescar. Para responder observa cómo está el mar desde la playa.» ¿Cuál es la pregunta y cuál es la perspectiva?", ["Pregunta: ¿cuándo es seguro salir a pescar?", "Quien pregunta: don Luis, pescador.", "Perspectiva: la de quien necesita pescar con seguridad."], "Pregunta: cuándo salir a pescar; perspectiva: la de un pescador."),
        W("Comparar perspectivas", "Doña Rosa, de Valle Alto, se pregunta cuándo sembrar. ¿Es la misma perspectiva que la de don Luis?", ["Doña Rosa mira la tierra y el clima para sembrar.", "Don Luis mira el mar para pescar.", "Son distintas."], "No: cada uno mira según lo que necesita."),
    ],
    mistakes=[
        M("Pensar que hay una sola manera de hacer preguntas sobre la naturaleza.", "Las preguntas dependen de quién las hace y para qué.", "Pregunta quién pregunta y qué necesita."),
        M("Decir que el saber de una comunidad es solo una creencia sin base.", "Se construye con observación durante muchas generaciones.", "Busca qué observa y cómo lo comprueba."),
    ],
    R=[
        ex("¿Qué se pregunta don Luis en la ficha: cuándo es seguro salir a pescar o cuándo sembrar?", "Cuándo es seguro salir a pescar", "La ficha lo dice."),
        ex("¿Cómo responde don Luis su pregunta: observa el mar desde la playa o mira televisión?", "Observa el mar desde la playa", "La ficha lo dice."),
        ex("¿Qué es una perspectiva: la manera de mirar algo según quién lo mira o un tipo de pescado?", "La manera de mirar algo según quién lo mira", "Es la definición."),
    ],
    C=[
        ex("¿Qué es una observación? A) mirar con atención y anotar lo que se ve B) adivinar", "A", "Es la base del conocimiento."),
        ex("Verdadero o falso: los conocimientos de las comunidades se construyen observando durante generaciones.", "Verdadero", "Se transmiten y se validan."),
        ex("Verdadero o falso: todas las preguntas sobre la naturaleza son iguales para todos.", "Falso", "Dependen de quién las hace y para qué."),
    ],
    A=[
        ex("Ficha inventada de Valle Alto: «Doña Rosa se pregunta cuándo sembrar. Observa si terminaron las lluvias.» ¿Qué observa?", "Si terminaron las lluvias", "La ficha lo dice."),
        ex("Une cada persona con su pregunta. 1) don Luis 2) doña Rosa a) ¿cuándo sembrar? b) ¿cuándo salir a pescar?", "1-b, 2-a", "Cada uno pregunta según su trabajo."),
        ex("Una ficha trae una pregunta pero no dice quién la hace ni de qué comunidad es. ¿Puedes usarla? Responde Sí o No.", "No", "Faltan datos para situarla."),
    ],
    Z=[
        ex("Pedro dice: «Como don Luis observa el mar, su saber no es serio». ¿Qué error comete?", "Descalifica un saber construido con observación", "La observación es una base de conocimiento."),
        ex("¿Por qué la perspectiva de un pescador y la de un agricultor pueden ser distintas? A) porque necesitan cosas distintas B) porque uno sabe más", "A", "Cada uno responde a sus necesidades."),
    ],
    D=[
        ex("Dos frases: 1) «Doña Rosa observa si terminaron las lluvias para sembrar» 2) «Todas las comunidades siembran cuando terminan las lluvias». ¿Cuál se apoya en la ficha?", "La primera", "La segunda generaliza."),
        ex("Si quieres conocer qué observa un pueblo real para decidir cuándo sembrar, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a una página al azar", "A", "Ellos lo explican."),
    ],
    context=[ex("En tu curso quieren saber cuándo regar mejor las plantas del patio. ¿Cuál es una buena pregunta con perspectiva clara? A) ¿en qué momento del día se secan más las plantas del patio? B) ¿qué es una planta?", "A", "Es concreta y situada.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es una perspectiva.", "La manera de mirar algo según quién lo mira", "Es la definición de la clase."),
        ex("Verdadero o falso: el saber de una comunidad se construye con observación.", "Verdadero", "Es parte de la explicación."),
        ex("¿A quién preguntas por los conocimientos de un pueblo real? A) al educador tradicional B) a nadie", "A", "Es la fuente."),
    ],
    task=T("Lee estas dos fichas inventadas. Ficha 1: «Don Luis, de Costa Clara, se pregunta cuándo es seguro salir a pescar. Observa cómo está el mar.» Ficha 2: «Doña Rosa, de Valle Alto, se pregunta cuándo sembrar. Observa si terminaron las lluvias.» Completa una tabla con cuatro filas: quién pregunta, la pregunta, qué observa y perspectiva. Escribe una pregunta propia sobre la naturaleza de tu zona y qué observarías para responderla.",
           "Quién pregunta: don Luis / doña Rosa. Pregunta: cuándo salir a pescar / cuándo sembrar. Observa: el mar / si terminaron las lluvias. Perspectiva: de un pescador / de una agricultora. Mi pregunta: ¿cuándo florecen las plantas del patio? Observaría las plantas cada semana.",
           ["completa la tabla con datos de las fichas", "distingue las perspectivas", "formula una pregunta propia con su observación"], ["tabla de cuatro filas", "pregunta propia"], ["generalizar a todas las comunidades", "mezclar las fichas"],
           "Pedir que muestre en cada ficha el dato; valorar que distinga perspectivas."),
    reinforce="Subraya en cada ficha la pregunta y lo que se observa con dos colores.",
    extend="Escribe cómo cambiaría la pregunta de doña Rosa si viviera junto al mar.",
)

L(
    OA16, 2,
    materials="Lápiz y hojas. Los datos están escritos aquí y son inventados.",
    use="Aprenderé a examinar cómo una observación repetida durante años se convierte en conocimiento, usando un registro de datos. Sirve para valorar la evidencia que sostiene un saber.",
    prior=["Sé situar una pregunta y su perspectiva.", "Sé contar y comparar números."],
    explain=[
        "Un conocimiento nace cuando alguien observa algo muchas veces y reconoce un patrón: algo que se repite. Si el árbol del patio florece casi en la misma semana todos los años, se puede usar esa señal para decidir cuándo hacer una tarea. Cuantos más años de observación hay, más sólida es la evidencia.",
        "La evidencia son los datos que sostienen lo que decimos. Registrarla permite compararla. Por ejemplo, anotamos en una tabla la semana en que floreció el árbol en cinco años. Si en la mayoría de los años fue la misma semana, vemos un patrón; si cambia mucho, no podemos asegurarlo.",
        "Los saberes de las comunidades se construyen así durante generaciones y se transmiten. En esta clase usamos una tabla inventada de Valle Alto. No es un dato real de ningún pueblo. Para conocer qué señales observa una comunidad real, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("patrón", "algo que se repite de manera parecida"), ("evidencia", "datos que sostienen lo que se afirma"), ("registro", "anotación ordenada de lo que se observa"), ("señal", "cambio en la naturaleza que indica que algo ocurrirá"), ("generación", "grupo de personas de edades parecidas")],
    worked=[
        W("Leer un registro", "Registro inventado de Valle Alto (semana en que floreció el árbol del patio): año 1: 12, año 2: 11, año 3: 12, año 4: 13, año 5: 12. ¿En cuántos años floreció en la semana 12?", ["Reviso cada año.", "Semana 12: años 1, 3 y 5.", "Cuento: 3."], "3 años."),
        W("Reconocer el patrón", "Con el mismo registro, ¿hay un patrón?", ["En 3 de 5 años fue la semana 12.", "Los otros años fueron 11 y 13, cerca de la 12.", "Hay un patrón."], "Sí: la floración ocurre cerca de la semana 12."),
    ],
    mistakes=[
        M("Decidir con un solo año de observación.", "Un solo dato no muestra un patrón.", "Usa varios años."),
        M("Creer que si un año cambia, el saber está mal.", "Puede haber variación y aun así hay un patrón.", "Compara todos los años."),
    ],
    R=[
        ex("En el registro de Valle Alto, ¿en qué semana floreció el árbol el año 2? Escribe el número.", "11", "La tabla dice 11."),
        ex("¿Qué es un patrón: algo que se repite de manera parecida o algo que ocurre una sola vez?", "Algo que se repite de manera parecida", "Es la definición."),
        ex("¿Cuántos años tiene el registro? Escribe el número.", "5", "La tabla tiene cinco años."),
    ],
    C=[
        ex("¿Qué es la evidencia? A) datos que sostienen lo que se afirma B) una opinión sin base", "A", "Son los datos."),
        ex("Verdadero o falso: más años de observación dan evidencia más sólida.", "Verdadero", "Se ven mejor los patrones."),
        ex("Verdadero o falso: el registro de Valle Alto es un dato real de un pueblo.", "Falso", "Es un ejemplo inventado."),
    ],
    A=[
        ex("En el registro, ¿cuál fue la semana más tardía de floración? Escribe el número.", "13", "El año 4 fue 13."),
        ex("Cuenta en cuántos años la floración fue en la semana 12 o antes: año 1: 12, año 2: 11, año 3: 12, año 4: 13, año 5: 12.", "4", "Años 1, 2, 3 y 5."),
        ex("En el registro, ¿en cuántos años la floración fue en la semana 11 o en la 13? Escribe el número.", "2", "Fue en la semana 11 el año 2 y en la 13 el año 4."),
    ],
    Z=[
        ex("Lucía dice: «Floreció en la semana 13 el año 4, así que el saber de la comunidad no sirve». ¿Qué responde el registro?", "Hay variación pero la floración se mantiene cerca de la semana 12", "Un año no anula el patrón."),
        ex("¿Por qué conviene registrar los datos en una tabla? A) para compararlos con orden B) para decorar", "A", "El registro ordena la evidencia."),
    ],
    D=[
        ex("Dos conclusiones: 1) «En los 5 años, la floración fue entre la semana 11 y la 13» 2) «La floración siempre es en la semana 12». ¿Cuál se apoya en el registro?", "La primera", "La segunda no se cumple todos los años."),
        ex("Si una comunidad real te cuenta una señal de la naturaleza, ¿qué haces con esa información? A) la atribuyo a la comunidad y no la generalizo B) la presento como una ley para todos", "A", "Se nombra la fuente."),
    ],
    context=[ex("Quieres saber cuándo florecen las plantas del patio. ¿Qué haces durante 5 semanas? A) las observo cada semana y anoto B) las observo una sola vez", "A", "Un registro necesita varias observaciones.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es un patrón.", "Algo que se repite de manera parecida", "Es la definición de la clase."),
        ex("Verdadero o falso: un solo dato basta para afirmar un patrón.", "Falso", "Se necesitan varios datos."),
        ex("¿Para qué sirve registrar datos? A) para comparar la evidencia B) para guardarlos sin usar", "A", "Permite reconocer patrones."),
    ],
    task=T("Observa una planta del patio o de tu casa durante 5 días (con ayuda de una persona de tu casa si sales). Anota cada día si hay flores, hojas nuevas o cambios, en una tabla con dos columnas: día y qué observé. Si no puedes observar, usa estos datos de práctica (inventados) de una planta: día 1: sin hojas nuevas; día 2: sin hojas nuevas; día 3: una hoja nueva; día 4: dos hojas nuevas; día 5: dos hojas nuevas. Escribe una frase que describa el patrón que ves y otra que diga qué no puedes asegurar.",
           "Día 1: sin hojas nuevas. Día 2: sin hojas nuevas. Día 3: una hoja nueva. Día 4: dos hojas nuevas. Día 5: dos hojas nuevas. Patrón: la planta empezó a tener hojas nuevas desde el día 3. No puedo asegurar qué pasará después con solo 5 días.",
           ["registra datos de varios días", "describe un patrón", "declara lo que no puede asegurar"], ["tabla de 5 días", "dos frases"], ["afirmar con un solo dato", "inventar datos como reales"],
           "Pedir que muestre sus datos; valorar que declare el alcance de su evidencia."),
    reinforce="Marca con un color los días en que viste un cambio en tu planta.",
    extend="Explica cómo mejorarías tu registro si observaras durante 10 días.",
)

L(
    OA16, 3,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a relacionar la naturaleza (suelo, agua, plantas, mar) con el cosmos (sol, luna, estrellas) en lo que cuentan las comunidades, y también con lo que explica la ciencia escolar. Sirve para ver cómo se conectan las observaciones sin mezclarlas.",
    prior=["Sé reconocer observación, evidencia y patrón.", "Sé que cada fuente tiene su perspectiva."],
    explain=[
        "El cosmos es todo lo que hay en el cielo y más allá: el Sol, la Luna, las estrellas y los planetas. La naturaleza es lo que hay en la Tierra: el agua, el suelo, las plantas y los animales. Muchas comunidades observan el cielo y la Tierra juntos, porque lo que pasa arriba se relaciona con lo que pasa abajo.",
        "La ciencia escolar también relaciona el cosmos con la naturaleza. Por ejemplo, explica que el mar sube y baja con las mareas, y que la Luna influye en ellas. Es una explicación basada en mediciones que otros pueden repetir.",
        "En una ficha inventada, una comunidad (Costa Clara) puede decir que sus pescadores observan la Luna y el mar para decidir cuándo salir. Eso es lo que esa comunidad cuenta. No decimos que la ciencia escolar y el saber de la comunidad sean lo mismo: cada uno tiene su origen, su manera de comprobar y su alcance. Para conocer relaciones reales de un pueblo, preguntamos al educador o educadora tradicional.",
    ],
    vocab=[("cosmos", "todo lo que hay en el cielo y más allá, como el Sol y la Luna"), ("naturaleza", "lo que hay en la Tierra, como el agua, el suelo y las plantas"), ("marea", "subida y bajada del mar"), ("cielo despejado", "cielo sin nubes"), ("relación", "vínculo entre dos cosas")],
    worked=[
        W("Relacionar con la ficha", "Ficha inventada de Costa Clara: «Los pescadores miran la Luna y el mar desde la playa antes de decidir si salen.» ¿Qué relación hay entre cosmos y naturaleza?", ["Cosmos: la Luna.", "Naturaleza: el mar.", "La comunidad los observa juntos para decidir."], "Observan la Luna y el mar juntos para decidir si salen."),
        W("Distinguir fuentes", "La ciencia escolar dice que la Luna influye en las mareas. La ficha dice que los pescadores miran la Luna y el mar. ¿Son la misma fuente?", ["La ciencia escolar usa mediciones.", "La ficha cuenta el saber de una comunidad.", "Son fuentes distintas."], "No: son fuentes distintas con relaciones parecidas."),
    ],
    mistakes=[
        M("Decir que la ficha de Costa Clara explica científicamente las mareas.", "Cuenta lo que observa una comunidad, no una explicación científica.", "Atribuye cada afirmación a su fuente."),
        M("Mezclar la explicación científica y el saber de la comunidad como si fueran lo mismo.", "Tienen distinto origen y alcance.", "Escribe qué dice cada fuente."),
    ],
    R=[
        ex("Según la ficha, ¿qué miran los pescadores desde la playa: la Luna y el mar o solo el cerro?", "La Luna y el mar", "La ficha lo dice."),
        ex("¿Qué es el cosmos: todo lo que hay en el cielo y más allá o solo el mar?", "Todo lo que hay en el cielo y más allá", "Es la definición."),
        ex("¿Qué sube y baja con las mareas: el mar o el cerro?", "El mar", "Las mareas son subidas y bajadas del mar."),
    ],
    C=[
        ex("¿Qué corresponde al cosmos? A) la Luna B) el suelo", "A", "La Luna está en el cielo."),
        ex("Verdadero o falso: la ciencia escolar explica que la Luna influye en las mareas.", "Verdadero", "Es una explicación científica escolar."),
        ex("Verdadero o falso: la ficha de Costa Clara y la ciencia escolar son la misma fuente.", "Falso", "Tienen distinto origen."),
    ],
    A=[
        ex("Clasifica en COSMOS o NATURALEZA: a) la Luna b) el mar c) el suelo d) las estrellas.", "a cosmos, b naturaleza, c naturaleza, d cosmos", "La Luna y las estrellas están en el cielo; el mar y el suelo están en la Tierra."),
        ex("Une cada afirmación con su fuente. 1) «Los pescadores miran la Luna y el mar» 2) «La Luna influye en las mareas» a) ficha de la comunidad b) ciencia escolar", "1-a, 2-b", "Cada una viene de una fuente distinta."),
        ex("Ficha inventada de Valle Alto: «Doña Rosa observa el cielo despejado después de las lluvias para decidir cuándo sembrar». Escribe un elemento del cosmos y uno de la naturaleza.", "Cosmos: el cielo; naturaleza: las lluvias o la tierra", "La ficha nombra ambos."),
    ],
    Z=[
        ex("Tomás escribe: «Según la ciencia, los pescadores de Costa Clara usan las mareas». ¿Qué error comete?", "Mezcla la ciencia escolar con lo que cuenta la comunidad", "Cada afirmación debe atribuirse a su fuente."),
        ex("¿Por qué conviene decir «según la ficha» o «según la ciencia escolar»? A) para que se sepa de dónde sale cada dato B) para alargar", "A", "Se distingue la fuente."),
    ],
    D=[
        ex("Dos frases: 1) «La ficha cuenta que los pescadores miran la Luna y el mar; la ciencia escolar explica la influencia de la Luna en las mareas» 2) «La ciencia y la ficha dicen exactamente lo mismo». ¿Cuál es más precisa?", "La primera", "Distingue las fuentes."),
        ex("Si quieres conocer las relaciones que un pueblo real ve entre naturaleza y cosmos, ¿a quién preguntas? A) al educador tradicional o a la comunidad B) a una página al azar", "A", "Ellos explican esas relaciones."),
    ],
    context=[ex("Tu curso observa el cielo despejado desde el patio por la tarde, con una persona adulta. ¿Qué puedes registrar sin mirar el Sol directamente? A) si hay nubes y cómo está el cielo B) la forma del Sol con los ojos", "A", "Mirar el Sol directamente daña la vista.")],
    selfcheck=[
        ex("Escribe un ejemplo de cosmos y uno de naturaleza.", "Cosmos: la Luna; naturaleza: el mar", "Ejemplo posible de la clase."),
        ex("Verdadero o falso: puedo mirar el Sol directamente para observarlo.", "Falso", "Daña la vista."),
        ex("¿Qué haces para no mezclar fuentes? A) atribuyo cada dato a su fuente B) uso todo junto", "A", "Se distingue el origen."),
    ],
    task=T("Lee esta ficha inventada de Costa Clara: «Los pescadores miran la Luna y el mar antes de decidir si salen a pescar.» y esta frase de la ciencia escolar: «La Luna influye en las mareas». Completa una tabla con tres columnas: naturaleza, cosmos y fuente de cada dato. Escribe dos frases que atribuyan bien cada dato y una pregunta al educador tradicional. No mires el Sol directamente en ningún momento.",
           "Naturaleza: el mar (ficha) / las mareas (ciencia escolar). Cosmos: la Luna (ambas). Frases: Según la ficha de Costa Clara, los pescadores miran la Luna y el mar. Según la ciencia escolar, la Luna influye en las mareas. Pregunta: ¿qué señales de la naturaleza y del cielo observa nuestra comunidad?",
           ["clasifica naturaleza y cosmos", "atribuye cada dato a su fuente", "no mezcla las fuentes"], ["tabla de tres columnas", "dos frases", "pregunta"], ["mezclar las fuentes", "decir que son lo mismo"],
           "Pedir que señale la fuente de cada frase; valorar la precisión."),
    reinforce="Colorea con azul lo que corresponde a la naturaleza y con amarillo lo que corresponde al cosmos.",
    extend="Escribe cómo explicarías a un compañero por qué es importante decir de qué fuente viene cada dato.",
)

L(
    OA16, 4,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a comparar el saber de una comunidad y la ciencia escolar sin decir que una es mejor y sin fusionarlas. Sirve para respetar cada fuente por lo que es.",
    prior=["Sé relacionar naturaleza y cosmos.", "Sé atribuir cada dato a su fuente."],
    explain=[
        "Comparar no es competir. Cuando comparamos el saber de una comunidad con la ciencia escolar miramos qué observa cada una, cómo lo comprueba, quién lo transmite y para qué sirve. Esto ayuda a comprender sin jerarquizar, es decir, sin decir que una es mejor o más verdadera que la otra.",
        "Tampoco se fusionan, es decir, no se mezclan como si fueran una sola cosa. Cada fuente tiene su origen y su alcance. La ciencia escolar usa mediciones y experimentos que otros pueden repetir. El saber de una comunidad se construye con observaciones de generaciones y se valida en la comunidad. Ambos pueden dar información valiosa, y a veces coinciden en una relación.",
        "Una comparación respetuosa se hace con una tabla de cuatro filas: qué observa, cómo lo comprueba, quién lo transmite y para qué sirve. Debajo se escriben una semejanza, una diferencia y un límite. Para un pueblo real, el educador o educadora tradicional guía qué se puede compartir y cómo.",
    ],
    vocab=[("jerarquizar", "decir que algo es mejor o más verdadero que otra cosa"), ("fusionar", "mezclar dos cosas como si fueran una sola"), ("método", "manera de comprobar algo"), ("alcance", "hasta dónde llega lo que una fuente puede afirmar"), ("transmitir", "pasar un saber a otras personas")],
    worked=[
        W("Armar la tabla", "Compara: Ficha de Costa Clara (inventada): «Los pescadores miran la Luna y el mar para decidir si salen; lo aprenden de los mayores». Ciencia escolar: «La Luna influye en las mareas; se mide con instrumentos y registros». ¿Qué observa, cómo comprueba y quién transmite cada una?", ["Ficha: observa Luna y mar; comprueba con la experiencia; transmite el mayor.", "Ciencia escolar: observa la Luna y las mareas; comprueba con instrumentos; transmite la escuela.", "Hago la tabla."], "Ambas observan Luna y mar; comprueban y transmiten de maneras distintas."),
        W("Escribir un límite", "¿Qué límite tiene decir «las dos fuentes explican lo mismo»?", ["La ficha cuenta una práctica.", "La ciencia explica una causa.", "No explican lo mismo."], "Que la ficha no explica la causa de las mareas y la ciencia escolar no cuenta la práctica de la comunidad."),
    ],
    mistakes=[
        M("Decir que la ciencia escolar es más verdadera que el saber de la comunidad.", "Es jerarquizar.", "Compara por origen, método y alcance."),
        M("Decir que la ficha y la ciencia escolar son lo mismo.", "Es fusionar.", "Mantén cada fuente separada."),
    ],
    R=[
        ex("¿Qué significa jerarquizar: decir que algo es mejor que otra cosa o comparar sin ordenar?", "Decir que algo es mejor que otra cosa", "Es lo que no se hace al comparar."),
        ex("¿Cómo aprenden los pescadores de la ficha a decidir si salen: de los mayores o de un libro?", "De los mayores", "La ficha lo dice."),
        ex("¿Cómo comprueba la ciencia escolar lo de las mareas: con instrumentos y registros o con suposiciones?", "Con instrumentos y registros", "Es su método."),
    ],
    C=[
        ex("¿Qué significa fusionar? A) mezclar como si fueran una sola cosa B) separar con cuidado", "A", "Es mezclar sin distinguir."),
        ex("Verdadero o falso: comparar es decir cuál saber es mejor.", "Falso", "Es comprender sin jerarquizar."),
        ex("Verdadero o falso: cada fuente tiene su origen y su alcance.", "Verdadero", "Es la idea de la clase."),
    ],
    A=[
        ex("Escribe una semejanza entre la ficha de Costa Clara y la ciencia escolar.", "Ambas observan la Luna y el mar", "Es lo que comparten."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas observan la Luna y el mar b) una se valida en la comunidad y otra con instrumentos y registros.", "a semejanza, b diferencia", "La primera es común; la segunda distingue métodos."),
        ex("Completa: la ficha se aprende de los ___; la ciencia escolar se aprende en la ___. Escribe las dos palabras.", "mayores y escuela", "Cada fuente tiene su transmisión."),
    ],
    Z=[
        ex("Camila dice: «La ficha de Costa Clara no vale porque no usa instrumentos». ¿Qué error comete?", "Jerarquiza juzgando por un método distinto", "Cada fuente se valora por su origen y alcance."),
        ex("¿Qué límite tiene comparar solo una ficha y una frase de ciencia escolar? A) no se puede decir cómo son todos los saberes B) se puede decir todo", "A", "Solo hay dos fuentes."),
    ],
    D=[
        ex("Dos conclusiones: 1) «Las dos fuentes observan la Luna y el mar, y las comprueban de maneras distintas» 2) «La ficha y la ciencia escolar son exactamente lo mismo». ¿Cuál es válida?", "La primera", "La segunda fusiona."),
        ex("Si una comunidad real te cuenta un saber, ¿qué haces para respetarlo? A) lo atribuyo a la comunidad y no lo mezclo con otras fuentes sin avisar B) lo corrijo con lo que sé de la escuela", "A", "Se respeta su origen."),
    ],
    context=[ex("En una exposición, un compañero dice que el saber de una comunidad «es solo una creencia». ¿Qué respondes? A) que se construye con observación y se valida en la comunidad B) que tiene razón", "A", "No se jerarquiza ni se descalifica.")],
    selfcheck=[
        ex("Escribe con tus palabras qué es fusionar.", "Mezclar dos cosas como si fueran una sola", "Es la definición de la clase."),
        ex("Verdadero o falso: puedo decir que una fuente es más verdadera si me gusta más.", "Falso", "No se jerarquiza."),
        ex("¿Qué incluye una buena comparación? A) semejanza, diferencia y límite B) solo la opinión", "A", "Es la estructura de la clase."),
    ],
    task=T("Compara la ficha de Costa Clara («Los pescadores miran la Luna y el mar; lo aprenden de los mayores») con la frase de la ciencia escolar («La Luna influye en las mareas; se mide con instrumentos y registros»). Haz una tabla con cuatro filas: qué observa, cómo lo comprueba, quién lo transmite y para qué sirve. Escribe una semejanza, una diferencia y un límite. No digas cuál es mejor ni las presentes como si fueran lo mismo.",
           "Qué observa: la Luna y el mar (ambas). Cómo lo comprueba: con la experiencia de la comunidad / con instrumentos y registros. Quién lo transmite: los mayores / la escuela. Para qué sirve: decidir si salir a pescar / explicar la causa de las mareas. Semejanza: ambas observan la Luna y el mar. Diferencia: distintos métodos y transmisión. Límite: son solo dos fuentes.",
           ["completa la tabla con datos de las fuentes", "escribe semejanza, diferencia y límite", "no jerarquiza ni fusiona"], ["tabla de cuatro filas", "tres frases"], ["decir cuál es mejor", "mezclar las fuentes"],
           "Pedir que muestre en cada fuente el dato; valorar que no jerarquice."),
    reinforce="Rodea con un color las semejanzas y con otro las diferencias de tu tabla.",
    extend="Escribe qué otro tipo de fuente te gustaría sumar a la comparación y a quién le pedirías permiso.",
)

L(
    OA16, 5,
    materials="Lápiz y hojas. Las fichas están escritas aquí y son inventadas.",
    use="Aprenderé a comunicar qué puede afirmar cada fuente y hasta dónde llega, en un texto breve y respetuoso. Sirve para presentar ciencia y saberes de comunidades sin confundirlos.",
    prior=["Sé comparar sin jerarquizar ni fusionar.", "Sé atribuir cada dato a su fuente."],
    explain=[
        "Comunicar los alcances de cada fuente significa decir qué puede afirmar y qué no. La ficha de una comunidad cuenta lo que esa comunidad observa y valida. La ciencia escolar explica causas con mediciones que otros pueden repetir. Ninguna de las dos responde todas las preguntas.",
        "Un texto respetuoso nombra las fuentes («según la ficha de Costa Clara», «según la ciencia escolar»), separa lo que dice cada una, declara sus límites («no sabemos cómo se transmite todo el saber») y evita palabras que juzguen, como «mejor», «más verdadero» o «solo una creencia».",
        "En esta clase también valoramos y recreamos una expresión simple y autorizada: un cuaderno de observaciones del cielo y la naturaleza hecho por ti, con tu propio registro. Es tu producción, inspirada en lo que aprendimos, y reconoce a las fuentes. Para temas de un pueblo real, el educador o educadora tradicional es quien guía.",
    ],
    vocab=[("alcance", "hasta dónde llega lo que una fuente puede afirmar"), ("atribuir", "decir de quién viene un dato"), ("límite", "lo que una fuente no puede afirmar"), ("cuaderno de observaciones", "cuaderno donde se anota lo que se ve, con fecha"), ("respetuoso", "que no juzga ni descalifica")],
    worked=[
        W("Escribir con alcances", "Escribe un párrafo que comunique los alcances de la ficha de Costa Clara y de la ciencia escolar sobre la Luna y el mar.", ["Nombro la ficha: los pescadores miran la Luna y el mar.", "Nombro la ciencia: la Luna influye en las mareas.", "Declaro que son fuentes distintas y que no sabemos más de la comunidad."], "«Según la ficha de Costa Clara, los pescadores miran la Luna y el mar. Según la ciencia escolar, la Luna influye en las mareas. Son fuentes distintas y no sabemos más detalles de la comunidad.»"),
        W("Revisar un texto", "Un texto dice: «La ciencia explica mejor las mareas que los pescadores». ¿Qué corriges?", ["La palabra «mejor» jerarquiza.", "Las fuentes responden cosas distintas.", "Reescribo sin juicio."], "«La ciencia escolar explica la causa de las mareas; los pescadores usan lo que observan para decidir si salen.»"),
    ],
    mistakes=[
        M("Usar palabras como «solo una creencia» o «más verdadero».", "Descalifican una fuente.", "Describe lo que cada fuente aporta."),
        M("No decir qué no sabemos.", "El texto parece completo y no lo es.", "Escribe un límite."),
    ],
    R=[
        ex("¿Qué palabra debe evitar un texto respetuoso: «mejor» o «según la ficha»?", "Mejor", "Esa palabra jerarquiza las fuentes."),
        ex("¿Qué debe nombrar un buen texto: las fuentes o ninguna?", "Las fuentes", "Así se sabe de dónde salen los datos."),
        ex("¿Qué es un cuaderno de observaciones: un cuaderno donde se anota lo que se ve, con fecha, o un cuaderno de dibujos sin datos?", "Un cuaderno donde se anota lo que se ve, con fecha", "Es la definición."),
    ],
    C=[
        ex("¿Qué es el alcance de una fuente? A) hasta dónde llega lo que puede afirmar B) lo lejos que está", "A", "Es lo que puede afirmar y lo que no."),
        ex("Verdadero o falso: un texto respetuoso puede decir que una fuente es solo una creencia.", "Falso", "Eso descalifica una fuente."),
        ex("Verdadero o falso: declarar un límite mejora un texto.", "Verdadero", "Muestra honestidad y respeto."),
    ],
    A=[
        ex("Completa con la fuente: «___ la ficha de Costa Clara, los pescadores miran la Luna y el mar». Escribe la palabra que falta.", "Según", "Es la manera de atribuir."),
        ex("Clasifica en ATRIBUCIÓN, LÍMITE o JUICIO: a) según la ficha b) no sabemos más detalles de la comunidad c) es más verdadero lo científico.", "a atribución, b límite, c juicio", "Solo la última juzga."),
        ex("Reescribe sin juicio: «El saber de la comunidad es solo una creencia». Escribe una versión posible.", "El saber de la comunidad se construye con observación y se valida en ella", "Describe en vez de juzgar."),
    ],
    Z=[
        ex("Marcos escribe: «Los pescadores y la ciencia dicen lo mismo». ¿Qué error comete?", "Fusiona fuentes distintas", "Cada una tiene su origen y alcance."),
        ex("¿Por qué es mejor mostrar el texto a la comunidad o al educador antes de compartirlo? A) para que corrijan lo que quedó mal B) para terminar antes", "A", "Ellos conocen su saber."),
    ],
    D=[
        ex("Dos párrafos: 1) «Según la ficha, miran la Luna y el mar; según la ciencia escolar, la Luna influye en las mareas; no sabemos más» 2) «Los pescadores tienen razón y la ciencia también». ¿Cuál comunica mejor los alcances?", "El primero", "Nombra fuentes y límites."),
        ex("¿Cuál es una producción propia respetuosa? A) un cuaderno de observaciones con mi propio registro B) copiar un diseño reservado", "A", "Es tu producción y reconoce las fuentes."),
    ],
    context=[ex("Presentas tu trabajo y alguien pregunta «¿cuál es más cierto?». ¿Qué respondes? A) responden preguntas distintas y tienen distinto alcance B) el científico", "A", "No se jerarquiza.")],
    selfcheck=[
        ex("Nombra dos rasgos de un texto respetuoso.", "Dos entre: nombra fuentes, separa lo que dice cada una, declara límites, evita juicios", "Están en la explicación."),
        ex("Verdadero o falso: puedo escribir «mejor» para comparar fuentes.", "Falso", "Esa palabra jerarquiza las fuentes."),
        ex("¿Qué incluye tu cuaderno de observaciones? A) fecha y lo que observé B) solo dibujos sin datos", "A", "Un registro necesita datos."),
    ],
    task=T("Escribe un párrafo de cuatro oraciones que comunique los alcances de la ficha de Costa Clara (los pescadores miran la Luna y el mar) y de la ciencia escolar (la Luna influye en las mareas). Debe nombrar las fuentes, separarlas, declarar un límite y no usar palabras que jerarquicen. Después comienza un cuaderno de observaciones del cielo y la naturaleza de tu patio: anota durante tres días la fecha, cómo está el cielo (despejado o con nubes) y una observación de una planta. No mires el Sol directamente. Reconoce con una nota que tu cuaderno está inspirado en lo que aprendiste.",
           "Según la ficha de Costa Clara, los pescadores miran la Luna y el mar. Según la ciencia escolar, la Luna influye en las mareas. Son fuentes distintas con alcances distintos. No sabemos más detalles de la comunidad. Cuaderno: Día 1, cielo despejado, la planta tiene 3 hojas. Día 2, nublado, 3 hojas. Día 3, despejado, 4 hojas. Nota: inspirado en lo que aprendí de la ficha de Costa Clara y la ciencia escolar.",
           ["nombra y separa las fuentes", "declara un límite y no jerarquiza", "registra tres días en el cuaderno con una nota de inspiración"], ["párrafo de cuatro oraciones", "cuaderno de tres días"], ["usar palabras que jerarquicen", "mirar el Sol directamente"],
           "Pedir que señale en el párrafo cada fuente y el límite; valorar el registro honesto."),
    reinforce="Subraya en tu párrafo las atribuciones y rodea el límite.",
    extend="Explica en dos oraciones cómo cambiaría tu párrafo si pudieras conversar con un educador tradicional sobre el tema.",
)
