"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS06 (utilizar recursos tecnológicos disponibles para registrar y narrar situaciones personales o acontecimientos de
la vida comunitaria y describir prácticas culturales, incorporando algunas palabras o expresiones en lengua indígena o
en castellano, culturalmente significativas).

Criterio de autoría: este módulo se centra en los LÍMITES comunitarios del registro (privacidad, consentimiento,
almacenamiento, retiro, devolución) para distinguirlo del OA LR06 del mismo nivel, que se centra en planificar, narrar y
revisar. Todos los acuerdos, comunidades, escuelas y personas son inventados solo para practicar y están rotulados como
tales. Las únicas palabras en lengua indígena son «mari mari» y «chaltumay» (mapuzugun); «minga» y «once» son palabras
del castellano de Chile, explicadas en la ficha. No se inventa gramática ni oraciones en lengua indígena. Los recursos
tecnológicos se describen sin marcas ni enlaces y siempre con una persona adulta; toda actividad tiene alternativa en
papel. No se piden datos personales ni de la familia. Nada de lo practicado se publica en internet.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LS6 = "LC05 OA LS06"

CONSULT = " Recuerda: los límites reales los define tu comunidad y la forma de decir y escribir las palabras de la lengua las enseñan el educador o la educadora tradicional. Pregúntales antes de dar tu trabajo por terminado. Si usas un aparato, hazlo con una persona adulta; puedes hacerlo todo en papel y no publiques nada en internet."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No exigir fotos, voces ni datos de la familia."

ACU = "Acuerdo de práctica de la Comunidad Brisa (inventado; no es de ningún pueblo real). Se puede registrar: el trabajo del curso en la minga, con permiso, sin rostros de niños. Se puede registrar la voz de una persona solo si lo autoriza y solo para uso del curso. No se registran las reuniones internas de la comunidad. Las palabras de la lengua se escriben solo después de que el educador tradicional las revise. No se publica nada en internet. Si la comunidad pide retirar un registro, se entrega y se borra la copia del curso."
GLO = "Glosario de práctica: «mari mari» es un saludo en mapuzugun. «Chaltumay» quiere decir gracias en mapuzugun. «Minga» es, en el castellano de Chile, un trabajo en que varias personas ayudan juntas. «Once» es la comida liviana de la tarde."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ============================================================ LS06 clase 1 · situar: qué se puede registrar y qué no
L(
    LS6, 1,
    materials="Lápiz y hoja. El acuerdo está escrito aquí y es inventado para practicar. Si usas un aparato, hazlo con una persona adulta; también puedes hacer todo en papel.",
    use="Aprenderé a ubicar los límites que una comunidad pone al registro de su vida y sus prácticas con recursos tecnológicos: qué se puede registrar, qué no y quién decide. Sirve para registrar sin faltar el respeto a nadie.",
    prior=["Sé que registrar es dejar guardada una experiencia.", "Sé que antes de registrar pido permiso y nombro la fuente."],
    explain=[
        "Registrar con un recurso tecnológico es dejar guardado algo con un aparato o programa: una grabadora, una cámara o un procesador de texto. Pero no todo se puede registrar. Cada comunidad tiene límites sobre lo que se graba, se fotografía, se escribe o se comparte. Esos límites son parte del respeto a la comunidad y no un obstáculo.",
        "En el acuerdo de práctica de la Comunidad Brisa, inventado, se puede registrar el trabajo del curso en la minga con permiso y sin rostros de niños; se puede registrar la voz de una persona solo si lo autoriza; no se registran las reuniones internas; las palabras de la lengua se escriben solo después de que el educador tradicional las revise; y no se publica nada en internet. Si la comunidad pide retirar un registro, se entrega y se borra la copia.",
        "Antes de registrar, pregunto: ¿hay un acuerdo?, ¿qué dice?, ¿quién decide si no hay acuerdo? Si no hay uno o no lo entiendo, no registro y pregunto al educador tradicional o a una persona de la comunidad. Un límite también protege mi propio trabajo, porque evita que tenga que retirarlo después.",
    ],
    vocab=[("límite", "regla que dice hasta dónde se puede llegar"), ("acuerdo", "reglas que una comunidad o grupo decide juntos"), ("retirar", "sacar un registro cuando la comunidad lo pide"), ("compartir", "mostrar algo a otras personas"), ("rostro", "cara de una persona")],
    worked=[
        W("Leer un límite", ACU + " ¿Se pueden registrar las reuniones internas de la comunidad?", ["Busco la regla sobre reuniones internas.", "Dice: no se registran las reuniones internas.", "La respuesta es no."], "no: las reuniones internas no se registran"),
        W("Aplicar un límite", ACU + " Un grupo quiere grabar la voz de una vecina para el curso. ¿Qué debe cumplir según el acuerdo?", ["Busco la regla sobre la voz.", "Dice: solo si lo autoriza y solo para uso del curso.", "Entonces debe tener su autorización y limitar el uso al curso."], "tener su autorización y usarla solo para el curso"),
    ],
    mistakes=[
        M("Grabar una reunión interna porque «solo es para guardarla».", "El acuerdo dice que no se registran.", "Reviso el acuerdo antes de registrar."),
        M("Subir un registro a internet porque se ve bien.", "El acuerdo dice que no se publica nada en internet.", "Lo guardo solo para el curso."),
    ],
    R=[
        ex(ACU + " ¿Se puede publicar un registro en internet?", "No", "El acuerdo dice que no se publica nada en internet."),
        ex(ACU + " ¿Qué se puede registrar con permiso y sin rostros de niños?", "el trabajo del curso en la minga", "El acuerdo lo dice."),
        ex("Un límite, ¿es una regla que dice hasta dónde se puede llegar o una invitación sin reglas?", "una regla que dice hasta dónde se puede llegar", "Así se definió límite."),
    ],
    C=[
        ex(ACU + " ¿Quién debe revisar las palabras de la lengua antes de escribirlas?", "el educador tradicional", "El acuerdo lo dice."),
        ex(ACU + " Verdadero o falso: según el acuerdo, la voz de una persona se puede registrar sin su autorización.", "Falso", "Solo si lo autoriza."),
        ex(ACU + " Si la comunidad pide retirar un registro, ¿qué se hace?", "se entrega y se borra la copia del curso", "El acuerdo lo dice."),
    ],
    A=[
        ex("Clasifica con P (permitido) o N (no permitido) según el acuerdo: 1) registrar la minga con permiso y sin rostros de niños. 2) grabar una reunión interna. 3) escribir palabras de la lengua sin revisión. Escribe las tres letras.", "1 P, 2 N, 3 N", "Solo la 1 cumple el acuerdo."),
        arith("El curso hizo 12 registros del trabajo en la minga. La comunidad pidió retirar 3. ¿Cuántos registros quedan?", "12-3", "Se restan los retirados del total."),
        ex("Ordena antes de registrar: A) registro dentro de los límites. B) leo el acuerdo. C) pido autorización a las personas. Escribe las letras en orden.", "B, C, A", "Primero leo el acuerdo, luego pido permiso y después registro."),
    ],
    Z=[
        ex("No existe un acuerdo escrito para la actividad de tu curso. ¿Qué es mejor: A) registrar igual B) preguntar al educador tradicional o a una persona de la comunidad qué límites hay?", "B", "Sin acuerdo se pregunta antes de registrar."),
        ex("Un niño dice: «Si no hay rostros de niños, ya puedo grabar cualquier cosa». Según el acuerdo, ¿tiene razón? Sí o No.", "No", "También hay límites sobre reuniones, voz, palabras e internet."),
    ],
    D=[
        ex(ACU + " Una niña quiere sacar una foto de la minga con rostros de niños para su casa. ¿El acuerdo lo permite? Sí o No.", "No", "El acuerdo pide sin rostros de niños."),
        ex(ACU + " Un grupo escribió «chaltumay» en su registro sin que el educador lo revisara. ¿Qué debe hacer: A) pedir la revisión antes de usarlo o B) dejarlo porque ya lo escribió?", "A", "El acuerdo pide revisión del educador."),
    ],
    context=[ex("Tu curso quiere grabar una actividad de la comunidad, pero no hay un acuerdo. ¿Preguntas qué límites hay antes de grabar o grabas y ves después?", "preguntas qué límites hay antes de grabar", "Los límites se conocen antes de registrar.")],
    selfcheck=[
        ex("¿Los límites de una comunidad son parte del respeto? Sí o No.", "Sí", "Cuidan a las personas y a la cultura."),
        ex("¿Puedo registrar una reunión interna si el acuerdo lo prohíbe? Sí o No.", "No", "Se respeta el acuerdo."),
        ex("Si no entiendo un límite, ¿lo ignoro o pregunto?", "pregunto", "Se pregunta a quien corresponde."),
    ],
    task=T(
        "Lee este acuerdo inventado de la Comunidad Aurora: «Se puede escribir un texto sobre la feria del sábado sin nombres. No se graba el interior de la sede. Las fotos solo de manos u objetos. Las palabras de la lengua las revisa la educadora. Nada se sube a internet.» Imagina que tu curso quiere registrar la feria. En tu cuaderno haz una tabla de dos columnas: lo que sí puede hacer según el acuerdo y lo que no puede hacer. Después escribe una pregunta para el educador o educadora tradicional sobre los límites de tu comunidad.",
        "Sí: escribir un texto sobre la feria sin nombres; fotos de manos u objetos; pedir la revisión de las palabras de la lengua. No: grabar el interior de la sede; subir algo a internet; escribir palabras de la lengua sin revisión. Pregunta: ¿qué límites tiene nuestra comunidad para registrar sus actividades?",
        ["clasifica correctamente lo permitido y lo no permitido", "no inventa reglas", "incluye la revisión de las palabras", "formula una pregunta"],
        ["tabla de dos columnas", "pregunta escrita o dicha en voz alta"],
        ["inventar reglas que no están", "olvidar un límite"],
        "Verifica que cada fila de la tabla salga de una frase del acuerdo.",
    ),
    reinforce="Relee el acuerdo de la Comunidad Brisa y subraya con un color lo que se puede y con otro lo que no se puede.",
    extend="Escribe un acuerdo inventado de cinco reglas para registrar una actividad de tu curso, marcado como inventado.",
)

# ============================================================ LS06 clase 2 · leer límites y reconocer datos sensibles
DAT = "Ficha de datos (de práctica). Datos que identifican a una persona: rostro, voz, nombre completo, dirección, teléfono, nombre del colegio y curso junto con el nombre. Datos de la comunidad que merecen cuidado: el lugar exacto de un sitio importante, las reuniones internas, las palabras o frases de la lengua sin revisión. Datos que se pueden registrar con cuidado: el trabajo del curso, objetos, manos, paisajes sin personas."

L(
    LS6, 2,
    materials="Lápiz y hoja. La ficha está escrita aquí y es de práctica. No necesitas dispositivos.",
    use="Aprenderé a reconocer qué datos de un registro identifican a las personas o merecen cuidado y a leer los límites que esto implica. Sirve para decidir qué dejar fuera de un registro.",
    prior=["Sé ubicar los límites de un acuerdo.", "Sé que no se ponen datos personales."],
    explain=[
        "Algunos datos identifican a una persona: su rostro, su voz, su nombre completo, su dirección o su teléfono. Si un registro los incluye, esa persona puede ser reconocida. Por eso pido permiso o, mejor, evito incluirlos. Otros datos son de la comunidad y merecen cuidado: el lugar exacto de un sitio importante, las reuniones internas y las palabras de la lengua que no han sido revisadas.",
        "Hay datos que se pueden registrar con más tranquilidad: el trabajo del curso, los objetos, las manos y los paisajes sin personas. Aun así, siempre pregunto por los límites de mi comunidad. Si dudo de un dato, lo dejo fuera y consulto. Dejar algo fuera no empobrece mi registro: lo hace más seguro.",
        "Al leer un registro ajeno, fijo la atención en lo que dice y en lo que declara que dejó fuera. Un registro bien hecho puede decir «no incluí nombres ni rostros» o «no incluí el lugar exacto». Esos límites muestran cuidado. Y yo, al leerlo, no intento averiguar los datos que se dejaron fuera.",
    ],
    vocab=[("dato", "información concreta sobre algo o alguien"), ("identificar", "reconocer quién es una persona"), ("dato sensible", "dato que merece cuidado especial"), ("dejar fuera", "no incluir un dato en el registro"), ("lugar exacto", "dirección o ubicación precisa de un sitio")],
    worked=[
        W("Clasificar un dato", DAT + " ¿La voz de una persona identifica o no identifica?", ["Busco la lista de datos que identifican.", "La voz está en esa lista.", "Entonces identifica a la persona."], "identifica a la persona"),
        W("Decidir qué dejar fuera", DAT + " Un registro dice: «Fotografié las manos de dos estudiantes tejiendo y anoté el nombre completo de cada uno». ¿Qué dato debe quedar fuera?", ["Las manos se pueden registrar con cuidado.", "El nombre completo identifica.", "Debe quedar fuera el nombre completo."], "el nombre completo"),
    ],
    mistakes=[
        M("Incluir la dirección de un sitio importante porque «ayuda a encontrarlo».", "El lugar exacto merece cuidado.", "Digo el nombre general de la zona o lo dejo fuera."),
        M("Creer que si el rostro no se ve, ya no hay datos que identifiquen.", "La voz y el nombre también identifican.", "Reviso toda la lista de datos."),
    ],
    R=[
        ex(DAT + " ¿El rostro identifica a una persona? Sí o No.", "Sí", "Está en la lista de datos que identifican."),
        ex(DAT + " ¿Las manos se pueden registrar con cuidado? Sí o No.", "Sí", "Están en la lista de datos que se pueden registrar con cuidado."),
        ex("Un dato, ¿es información concreta sobre algo o alguien o una opinión?", "información concreta sobre algo o alguien", "Así se definió dato."),
    ],
    C=[
        ex(DAT + " ¿Cuál de estos datos identifica a una persona: la dirección o un paisaje sin personas?", "la dirección", "La dirección está en la lista que identifica."),
        ex(DAT + " Verdadero o falso: las reuniones internas son un dato de la comunidad que merece cuidado.", "Verdadero", "Está en la lista de datos de la comunidad."),
        ex(DAT + " ¿Qué merece cuidado: el lugar exacto de un sitio importante o el trabajo del curso?", "el lugar exacto de un sitio importante", "Está en la lista de datos de la comunidad."),
    ],
    A=[
        ex(DAT + " Clasifica con I (identifica), C (cuidado de la comunidad) o S (se puede registrar con cuidado): 1) un teléfono. 2) un paisaje sin personas. 3) una reunión interna. Escribe las tres letras.", "1 I, 2 S, 3 C", "Cada dato está en una lista distinta."),
        arith("Una ficha tiene 6 datos que identifican y 3 datos de la comunidad que merecen cuidado. ¿Cuántos datos en total requieren atención?", "6+3", "Se suman las dos listas."),
        ex("Un registro dice: «No incluí nombres ni rostros, y no dije el lugar exacto del sitio». ¿Muestra cuidado? Sí o No.", "Sí", "Declara lo que dejó fuera para proteger."),
    ],
    Z=[
        ex("Una niña dice: «Si cambio solo el nombre por un apodo, ya no identifico a nadie». ¿Es siempre cierto? Sí o No.", "No", "La voz, el rostro o la combinación de datos pueden identificar."),
        ex("Lees un registro que dejó fuera la dirección de un sitio. ¿Qué haces: A) respetar que no la incluyó o B) tratar de averiguarla?", "A", "El límite muestra cuidado y se respeta."),
    ],
    D=[
        ex(DAT + " Un registro dice: «Entrevisté a una vecina; su voz está en el audio; su nombre completo aparece en el título; escribí que vive en la calle Los Aromos 123». ¿Cuántos datos de la ficha que identifican a una persona aparecen en ese registro?", "3", "Aparecen la voz, el nombre completo y la dirección.", "1+1+1"),
        ex("Debes elegir qué registrar de una minga con poco permiso: A) fotos de las bolsas llenas y las herramientas, o B) fotos de los rostros de los niños. ¿Cuál es más seguro: A o B?", "A", "Los objetos no identifican a personas."),
    ],
    context=[ex("Quieres contar en un registro un sitio importante de tu comunidad. ¿Dices su dirección exacta o lo describes de forma general y preguntas qué se puede decir?", "lo describes de forma general y preguntas qué se puede decir", "El lugar exacto merece cuidado.")],
    selfcheck=[
        ex("¿La voz identifica a una persona? Sí o No.", "Sí", "Está en la lista."),
        ex("¿Debo incluir la dirección exacta de un sitio importante? Sí o No.", "No", "Merece cuidado especial en la comunidad."),
        ex("Si dudo de un dato, ¿lo dejo fuera y consulto? Sí o No.", "Sí", "Es más seguro."),
    ],
    task=T(
        "Lee este borrador inventado de registro: «El sábado fuimos a la minga en la plaza de la calle Los Aromos 123. Grabé a Andrea Pérez diciendo «mari mari» y fotografié el rostro de dos niños. También anoté lo que se habló en la reunión interna de la sede.» En tu cuaderno haz una tabla de dos columnas: dato y qué hacer (dejar fuera, pedir permiso o registrar con cuidado). Escribe luego cómo quedaría el borrador corregido en tres oraciones, sin datos que identifiquen. Termina con una pregunta para el educador o educadora tradicional.",
        "Calle Los Aromos 123 / dejar fuera. Nombre Andrea Pérez y su voz / dejar fuera o pedir permiso. Rostros de dos niños / dejar fuera. Reunión interna / dejar fuera. «Mari mari» / pedir revisión del educador. Texto corregido: El sábado el curso fue a una minga en una plaza. Se trabajó entre todos y se saludó con «mari mari» (la fuente está por preguntar). No se incluyeron nombres, rostros ni lugares exactos. Pregunta: ¿puede revisar cómo escribí el saludo?",
        ["identifica los datos que identifican o merecen cuidado", "propone qué hacer con cada uno", "reescribe sin datos sensibles", "formula una pregunta"],
        ["tabla de dos columnas", "borrador corregido de tres oraciones"],
        ["dejar un dato que identifica", "inventar permisos"],
        "Comprueba que el texto corregido no incluya nombre, dirección ni rostro.",
    ),
    reinforce="Copia la ficha de datos y subraya con un color los que identifican y con otro los de la comunidad.",
    extend="Escribe una frase que explique por qué dejar algo fuera de un registro no lo empobrece.",
)

# ============================================================ LS06 clase 3 · relaciones culturales: consentimiento, retiro y reciprocidad
CON = "Situación de práctica (inventada): Una vecina de la Comunidad Brisa aceptó que el curso grabara su voz contando cómo se organiza una minga. Dijo: «Pueden usar el audio en la sala del curso hasta fin de año. Después, por favor, me lo devuelven». El curso guardó el audio en un aparato del colegio, lo escuchó en la sala y, al final del año, le entregó una copia y borró el audio del aparato."

L(
    LS6, 3,
    materials="Lápiz y hoja. La situación está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a relacionar el consentimiento, el plazo, la devolución y el retiro de un registro con el respeto a la comunidad. Sirve para registrar de modo que las personas puedan confiar en mí.",
    prior=["Sé qué datos identifican y cuáles merecen cuidado.", "Sé que debo pedir permiso antes de registrar."],
    explain=[
        "El consentimiento es el sí informado de una persona: sabe qué se registrará, para qué, dónde se guardará y por cuánto tiempo, y acepta. Un consentimiento tiene un plazo y un uso: «en la sala del curso hasta fin de año». No sirve para otro uso. Si quiero hacer algo distinto, pido otro permiso.",
        "Una persona puede pedir que se retire su registro, es decir, que se saque de donde está y se borre. También puede pedir que se le devuelva. Devolver es parte de la reciprocidad: dar algo a cambio de lo que recibí. En la situación de la vecina, el curso cumplió: guardó el audio en un aparato del colegio, lo usó solo en la sala, entregó una copia y borró el audio.",
        "Estas acciones relacionan el registro con la confianza. Si cumplo lo que prometí, las personas y la comunidad confían en mí. Si no lo cumplo, pierdo esa confianza y perjudico a otras personas que quizá querían compartir su saber. Por eso conviene anotar lo que se acordó, para no olvidarlo.",
    ],
    vocab=[("consentimiento", "el sí informado de una persona"), ("plazo", "tiempo durante el cual vale un permiso"), ("devolver", "entregar algo a quien lo dio o aportó"), ("retirar", "sacar un registro cuando se pide"), ("confianza", "seguridad de que se cumplirá lo prometido")],
    worked=[
        W("Reconocer el plazo", CON + " ¿Hasta cuándo puede usar el curso el audio?", ["Busco el plazo.", "La vecina dijo: hasta fin de año.", "Ese es el plazo."], "hasta fin de año"),
        W("Reconocer la devolución", CON + " ¿Qué hizo el curso al terminar el año?", ["Busco lo que hizo el curso al final.", "Le entregó una copia a la vecina.", "Y borró el audio del aparato."], "le entregó una copia y borró el audio del aparato"),
    ],
    mistakes=[
        M("Usar el audio de la vecina en otro lugar porque «ya lo tenía».", "El permiso era para la sala del curso.", "Pido otro permiso para otro uso."),
        M("Olvidar devolver o borrar el registro al terminar el plazo.", "No cumplo lo que prometí.", "Anoto el plazo y cumplo."),
    ],
    R=[
        ex(CON + " ¿Qué grabó el curso?", "la voz de una vecina contando cómo se organiza una minga", "La situación lo dice."),
        ex(CON + " ¿Dónde guardó el curso el audio?", "en un aparato del colegio", "La situación lo dice."),
        ex("Un plazo, ¿es el tiempo durante el cual vale un permiso o un lugar para guardar?", "el tiempo durante el cual vale un permiso", "Así se definió plazo."),
    ],
    C=[
        ex(CON + " Verdadero o falso: la vecina permitió usar el audio en cualquier lugar.", "Falso", "Solo en la sala del curso."),
        ex(CON + " ¿Qué pidió la vecina para después de fin de año?", "que le devolvieran el audio", "Lo dice la situación."),
        ex("En Lengua y Cultura: Cumplir lo prometido, ¿genera confianza o desconfianza?", "confianza", "Las personas confían en quien cumple."),
    ],
    A=[
        ex("Une cada elemento con su significado: A) consentimiento, B) plazo, C) devolución. Significados: 1) tiempo de validez del permiso, 2) entregar lo registrado a quien lo aportó, 3) el sí informado de la persona. Escribe los tres pares.", "A-3, B-1, C-2", "Cada palabra tiene su sentido visto en la clase."),
        arith("El curso guarda 9 audios autorizados. A mitad de año la comunidad pidió retirar 4. ¿Cuántos audios pueden seguir usándose?", "9-4", "Se restan los retirados."),
        ex("Ordena el cumplimiento de un permiso: A) devuelvo y borro al llegar el plazo. B) uso solo como se acordó. C) anoto el plazo y el uso. Escribe las letras en orden.", "C, B, A", "Anoto, uso lo acordado y devuelvo al final."),
    ],
    Z=[
        ex("Un niño quiere usar el audio de la vecina en una reunión de otro colegio. ¿Qué debe hacer: A) pedirle otro permiso o B) usarlo porque ya está grabado?", "A", "El permiso es solo para la sala del curso."),
        ex("La vecina pide el retiro del audio antes de fin de año. ¿Qué es lo correcto: A) cumplir su pedido o B) esperar a fin de año?", "A", "La persona puede pedir el retiro cuando quiera."),
    ],
    D=[
        ex(CON + " Si el curso hubiera guardado el audio en un lugar abierto a todos, ¿habría respetado lo acordado? Sí o No.", "No", "El uso era solo en la sala del curso."),
        ex("Dos cursos. El curso 1 anota plazo y uso y los cumple. El curso 2 no anota nada y olvida devolver. ¿Cuál genera más confianza: 1 o 2?", "1", "El curso 1 cumple lo acordado."),
    ],
    context=[ex("Una persona mayor te permite fotografiar sus manos tejiendo, para tu curso. ¿Anotas el uso y el plazo del permiso o confías en tu memoria?", "anotas el uso y el plazo del permiso", "Lo acordado se anota para cumplirlo.")],
    selfcheck=[
        ex("¿Un permiso puede tener un plazo? Sí o No.", "Sí", "Por ejemplo, hasta fin de año."),
        ex("¿Devolver a quien aportó es reciprocidad? Sí o No.", "Sí", "Es dar algo a cambio de lo recibido."),
        ex("Si una persona pide retirar su registro, ¿lo cumplo? Sí o No.", "Sí", "Puede pedirlo cuando quiera."),
    ],
    task=T(
        "Imagina esta situación inventada: una persona mayor de la Comunidad Aurora acepta que tu curso fotografíe sus manos preparando algo para la once, para un cuaderno del curso. En tu cuaderno escribe una ficha de permiso con cinco líneas: qué se registra, para qué, dónde se guarda, hasta cuándo y qué se hará al final (devolver o borrar). Si no sabes un dato, escribe «por preguntar». Agrega una frase que explique por qué anotar el permiso genera confianza. Termina con una pregunta para el educador o educadora tradicional.",
        "Qué: fotos de sus manos. Para qué: un cuaderno del curso. Dónde: en una carpeta del colegio. Hasta cuándo: fin de año. Al final: se le entrega una copia y se borra. Frase: Anotar el permiso ayuda a cumplirlo, y cumplir genera confianza. Pregunta: ¿cómo se agradece a quien nos deja registrar su saber?",
        ["completa las cinco líneas", "incluye plazo y cierre", "explica la confianza", "formula una pregunta"],
        ["ficha de permiso de cinco líneas", "pregunta"],
        ["inventar permisos", "no incluir plazo"],
        "Verifica que el plazo y el cierre estén escritos o marcados como por preguntar.",
    ),
    reinforce="Relee la situación de la vecina y numera los pasos que cumplió el curso.",
    extend="Escribe un párrafo de cuatro oraciones sobre qué pasaría si el curso no cumpliera lo acordado con una persona.",
)

# ============================================================ LS06 clase 4 · registro narrado con sus límites declarados
RN = "Registro de práctica (inventado): «El sábado, el 5.º básico de la Escuela Ejemplo participó en una minga para limpiar una plaza. Trajimos guantes y bolsas. Entre todos recogimos hojas. Una vecina nos dijo «chaltumay» al despedirse; la educadora tradicional nos enseñó que quiere decir gracias. No incluimos nombres, rostros ni el lugar exacto de la plaza. Este registro es solo para el curso y la comunidad que lo autorizó.»"

L(
    LS6, 4,
    materials="Lápiz y hoja. El registro está escrito aquí y es inventado para practicar. Puedes escribir todo en papel.",
    use="Aprenderé a escribir un registro narrado de una situación o práctica y a declarar en él los límites: qué no incluí, para quién es y quién lo autorizó. Sirve para contar sin exponer a nadie.",
    prior=["Sé qué datos dejar fuera.", "Sé anotar permisos con su plazo."],
    explain=[
        "Un registro narrado con límites tiene tres partes. La narración cuenta lo que pasó, en orden y con datos concretos. La fuente nombra de dónde vienen las palabras significativas. Y los límites declarados dicen qué no incluí, para quién es el registro y quién lo autorizó. Esa tercera parte hace honesto y seguro el registro.",
        "En el registro de práctica, la narración cuenta una minga, la fuente es la educadora tradicional por la palabra «chaltumay», y los límites son: no se incluyeron nombres, rostros ni el lugar exacto, y es solo para el curso y la comunidad que lo autorizó. Al leerlo, sé hasta dónde puedo usarlo.",
        "Puedo escribir un registro sobre una situación personal, un acontecimiento de la comunidad o una práctica cultural. Si es una práctica cultural, la describo con mis palabras y no explico significados profundos que no conozco. Si dudo, pregunto al educador tradicional. Y antes de mostrar el registro, pido la revisión de las palabras de la lengua y de los límites.",
    ],
    vocab=[("narración", "parte que cuenta lo que pasó en orden"), ("límite declarado", "aviso de qué no incluí y para quién es"), ("práctica cultural", "costumbre que se repite y se transmite"), ("autorizó", "dio permiso"), ("honesto", "que dice la verdad sobre lo que hizo")],
    worked=[
        W("Reconocer los límites", RN + " ¿Qué dos cosas dejaron fuera en el registro?", ["Busco la frase que dice qué no incluyeron.", "Dice: nombres, rostros y el lugar exacto de la plaza.", "Esas son las que dejaron fuera."], "nombres, rostros y el lugar exacto"),
        W("Reconocer para quién es", RN + " ¿Para quién es este registro?", ["Busco la frase final.", "Dice: solo para el curso y la comunidad que lo autorizó.", "Ese es el destinatario permitido."], "solo para el curso y la comunidad que lo autorizó"),
    ],
    mistakes=[
        M("Escribir el registro sin decir para quién es.", "Otros podrían usarlo donde no se permite.", "Declaro para quién es y quién lo autorizó."),
        M("Explicar significados profundos de una costumbre que no conozco.", "Podría decir algo falso.", "Describo lo que vi y pregunto por el sentido."),
    ],
    R=[
        ex(RN + " ¿Qué día fue la minga?", "el sábado", "El registro lo dice."),
        ex(RN + " ¿Qué trajeron para la minga?", "guantes y bolsas", "El registro lo dice."),
        ex(RN + " ¿Qué quiere decir «chaltumay», según el registro?", "gracias", "El registro lo dice."),
    ],
    C=[
        ex(RN + " ¿Quién enseñó el significado de «chaltumay»?", "la educadora tradicional", "El registro lo dice."),
        ex(RN + " Verdadero o falso: el registro incluye el lugar exacto de la plaza.", "Falso", "Dice que no lo incluyó."),
        ex("¿Qué parte del registro dice de dónde vienen las palabras significativas: la narración, la fuente o los límites declarados?", "la fuente", "La fuente nombra de dónde vienen las palabras."),
    ],
    A=[
        ex("Ordena las partes del registro: A) límites declarados. B) narración. C) fuente de las palabras. Escribe las letras en orden.", "B, C, A", "Cuento, nombro la fuente y declaro los límites."),
        ex(RN + " Elige la mejor frase de límites: A) «No incluimos nombres, rostros ni el lugar exacto; es solo para el curso y la comunidad que lo autorizó». B) «Aquí está todo lo que pasó». Escribe la letra.", "A", "A declara lo que dejó fuera y para quién es."),
        arith("El registro de práctica tiene 6 oraciones. 2 son de límites. ¿Cuántas oraciones son de narración y fuente?", "6-2", "Se restan las de límites del total."),
    ],
    Z=[
        ex(RN + " Un niño agrega: «La palabra chaltumay se usa solo los sábados». ¿Lo dice el registro? Sí o No.", "No", "El registro solo dice que quiere decir gracias."),
        ex("Una niña quiere describir una práctica cultural que ve en su vecindario pero no conoce su sentido. ¿Qué es mejor: A) describir lo que ve y preguntar el sentido o B) inventar el sentido?", "A", "No se inventan significados."),
    ],
    D=[
        ex("Dos registros. El 1 declara límites y quién autorizó. El 2 incluye el lugar exacto, nombres y no dice quién autorizó. ¿Cuál puede mostrarse: 1 o 2?", "1", "El 2 no cumple los límites."),
        ex(RN + " ¿Qué dato de los límites falta si quieres usar el registro en otro colegio: el permiso para ese uso o el nombre de la plaza?", "el permiso para ese uso", "El registro vale solo para el curso y la comunidad."),
    ],
    context=[ex("Escribes un registro sobre una actividad de tu curso. Antes de mostrarlo, ¿agregas qué dejaste fuera y para quién es o lo muestras sin ese aviso?", "agregas qué dejaste fuera y para quién es", "Los límites declarados completan el registro.")],
    selfcheck=[
        ex("¿Qué parte del registro dice qué no incluí: la narración o los límites declarados?", "los límites declarados", "Ahí se dice qué no se incluyó."),
        ex("¿Debo inventar el sentido de una costumbre que no conozco? Sí o No.", "No", "Se pregunta a quien enseña."),
        ex("¿Es honesto decir para quién es el registro? Sí o No.", "Sí", "Dice la verdad sobre su uso."),
    ],
    task=T(
        "Escribe un registro narrado de práctica sobre esta situación inventada: el 5.º básico de la Escuela Muestra ordenó la biblioteca el viernes, trajo cajas para los libros y compartió una once; el educador tradicional enseñó que se dice «chaltumay» para agradecer. En tu cuaderno escribe: 1) una narración de cuatro oraciones en orden, 2) la fuente de «chaltumay», 3) los límites declarados (qué dejaste fuera, para quién es y quién lo autorizó; si no lo sabes, escribe «por preguntar»). Termina con una pregunta para el educador o educadora tradicional.",
        "El viernes el 5.º básico ordenó la biblioteca. Trajimos cajas para los libros. Al terminar compartimos una once. Dijimos «chaltumay» para agradecernos. Fuente: el educador tradicional. Límites: no incluimos nombres ni rostros; es solo para el curso; quién lo autorizó: por preguntar. Pregunta: ¿puede revisar si escribí bien la palabra?",
        ["narración en orden", "fuente de la palabra", "límites declarados", "usa «por preguntar» donde no sabe", "formula una pregunta"],
        ["registro narrado", "pregunta"],
        ["olvidar los límites", "inventar permisos"],
        "Comprueba que el registro no tenga nombres, rostros ni dirección.",
    ),
    reinforce="Copia el registro de práctica y subraya con tres colores la narración, la fuente y los límites.",
    extend="Escribe otro registro de cuatro oraciones sobre otra actividad de tu curso, con sus límites declarados.",
)

# ============================================================ LS06 clase 5 · contrastar acuerdos sin jerarquizar
AC2 = "Dos acuerdos de práctica (inventados; no son de ningún pueblo real). Acuerdo de la Comunidad Brisa: se puede grabar la voz de una persona con su permiso, solo para el curso; no se publica nada en internet. Acuerdo de la Comunidad Aurora: no se graban voces; se aceptan textos escritos y fotos de objetos; nada se publica en internet."

L(
    LS6, 5,
    materials="Lápiz y hoja. Los acuerdos están escritos aquí y son inventados para practicar. No necesitas dispositivos.",
    use="Aprenderé a comparar los límites de dos comunidades para registrar, sin decir que una es más correcta. Sirve para entender que cada comunidad decide qué comparte y cómo.",
    prior=["Sé leer un acuerdo de registro.", "Sé comparar sin jerarquizar."],
    explain=[
        "Cada comunidad decide qué se puede registrar de su vida y cómo. Por eso dos comunidades pueden tener límites distintos. En los acuerdos de práctica, la Comunidad Brisa permite grabar voces con permiso y solo para el curso; la Comunidad Aurora no permite grabar voces, pero acepta textos escritos y fotos de objetos. Las dos coinciden en algo: nada se publica en internet.",
        "Para comparar uso una tabla de tres columnas: igual, distinto y qué cuida cada límite. La Comunidad Brisa cuida que la voz solo se use con permiso y en el curso; la Comunidad Aurora cuida las voces dejándolas fuera. No digo que una cuide mejor. Cada una decide según su historia, sus personas y su experiencia, y todas esas decisiones se respetan.",
        "Cuando trabajo con una comunidad, cumplo su acuerdo y no el de otra. Si mi curso trabaja con las dos, hago registros distintos para cada una. No copio los permisos de una a la otra. Y si no hay un acuerdo escrito, pregunto. Contrastar sirve para comprender la diversidad, no para elegir un acuerdo «mejor».",
    ],
    vocab=[("acuerdo", "reglas que una comunidad decide juntos"), ("contrastar", "comparar para ver parecidos y diferencias"), ("jerarquizar", "ordenar en mejor y peor"), ("diversidad", "variedad de formas de decidir y vivir"), ("coincidir", "estar de acuerdo en algo")],
    worked=[
        W("Buscar lo que coincide", AC2 + " ¿En qué coinciden los dos acuerdos?", ["Leo cada acuerdo.", "Brisa dice: no se publica nada en internet.", "Aurora dice lo mismo."], "en que nada se publica en internet"),
        W("Buscar la diferencia", AC2 + " ¿Qué diferencia hay sobre la voz?", ["En Brisa se puede grabar la voz con permiso.", "En Aurora no se graban voces.", "Esa es la diferencia."], "Brisa permite grabar voces con permiso y Aurora no permite grabarlas"),
    ],
    mistakes=[
        M("Decir que el acuerdo de Brisa es mejor porque permite más.", "Cada comunidad decide qué comparte.", "Describo qué permite y qué cuida cada una."),
        M("Aplicar el permiso de Brisa en la Comunidad Aurora.", "Cada comunidad tiene su acuerdo.", "Cumplo el acuerdo de la comunidad con la que trabajo."),
    ],
    R=[
        ex(AC2 + " ¿Qué comunidad permite grabar voces con permiso?", "la Comunidad Brisa", "Lo dice su acuerdo."),
        ex(AC2 + " ¿Qué comunidad no permite grabar voces?", "la Comunidad Aurora", "Lo dice su acuerdo."),
        ex(AC2 + " ¿Se publica algo en internet en alguna de las dos comunidades? Sí o No.", "No", "Ambos acuerdos lo prohíben."),
    ],
    C=[
        ex(AC2 + " ¿Qué acepta la Comunidad Aurora además de textos escritos?", "fotos de objetos", "Lo dice su acuerdo."),
        ex(AC2 + " Verdadero o falso: los dos acuerdos son exactamente iguales.", "Falso", "Difieren en la voz y en lo que aceptan."),
        ex("Contrastar, ¿es comparar para ver parecidos y diferencias o elegir el mejor?", "comparar para ver parecidos y diferencias", "Así se definió contrastar."),
    ],
    A=[
        ex(AC2 + " Clasifica con I (igual) o D (distinto): 1) ninguna publica en internet. 2) una permite grabar voces con permiso y la otra no. 3) las dos cuidan a las personas. Escribe las tres letras.", "1 I, 2 D, 3 I", "La 2 es la diferencia."),
        arith("En una tabla de comparación hay 7 filas. 4 son «igual». ¿Cuántas son «distinto»?", "7-4", "Se restan las iguales del total."),
        ex(AC2 + " Elige la frase que compara sin jerarquizar: A) «Brisa permite grabar voces con permiso y Aurora decide no grabarlas; ambas cuidan a las personas». B) «El acuerdo de Aurora es mejor». Escribe la letra.", "A", "A solo describe."),
    ],
    Z=[
        ex("Un curso trabajará con la Comunidad Aurora. Un niño propone grabar una voz porque en Brisa se puede. ¿Es correcto? Sí o No.", "No", "Cada comunidad tiene su acuerdo."),
        ex("Una niña dice: «Los acuerdos más estrictos son más respetuosos». ¿Se puede decir eso según la clase? Sí o No.", "No", "No se ordenan los acuerdos en mejores y peores."),
    ],
    D=[
        ex(AC2 + " Un curso quiere un registro de la minga para las dos comunidades. ¿Qué tipo de registro sirve a ambas: un texto escrito sin nombres o un audio de una vecina?", "un texto escrito sin nombres", "Aurora no permite voces."),
        ex("Un curso compara un acuerdo real con permiso con otro de práctica. ¿Qué debe hacer: A) citar la fuente y describir sin ordenar en mejor y peor o B) decir cuál es más completo?", "A", "Se compara con fuente y sin jerarquizar."),
    ],
    context=[ex("Tu curso trabaja con dos comunidades que tienen límites distintos. ¿Cumples el acuerdo de cada una para su registro o usas el mismo para ambas?", "cumples el acuerdo de cada una para su registro", "Cada comunidad decide sus límites.")],
    selfcheck=[
        ex("¿Una comunidad puede tener límites distintos a otra? Sí o No.", "Sí", "Cada comunidad decide."),
        ex("Al comparar acuerdos, ¿digo cuál es mejor? Sí o No.", "No", "Se describen sin jerarquizar."),
        ex("Si trabajo con una comunidad, ¿cumplo su acuerdo? Sí o No.", "Sí", "Es su decisión."),
    ],
    task=T(
        "Lee estos dos acuerdos inventados. Acuerdo A (Comunidad Costa): se aceptan fotos de objetos y textos escritos; no se registran personas; nada se publica en internet. Acuerdo B (Comunidad Cumbre): se acepta grabar la voz con permiso y plazo de un año; no se registran las reuniones internas; nada se publica en internet. En tu cuaderno haz una tabla de tres columnas (igual, distinto, qué cuida cada límite) con al menos dos filas por columna. Escribe dos frases que comparen sin decir cuál es mejor. Termina con una pregunta para el educador o educadora tradicional.",
        "Igual: en ninguna se publica nada en internet. Distinto: A acepta fotos de objetos y textos, y no registra personas; B acepta la voz con permiso y plazo de un año. Qué cuida: A cuida a las personas dejándolas fuera; B las cuida con permiso y plazo. Frases: La Comunidad Costa acepta fotos de objetos y textos; la Comunidad Cumbre acepta la voz con permiso por un año. Ambas cuidan a las personas. Pregunta: ¿cómo puedo conocer los límites de nuestra comunidad?",
        ["identifica lo igual y lo distinto", "dice qué cuida cada límite", "compara sin jerarquizar", "formula una pregunta"],
        ["tabla de tres columnas", "dos frases comparativas"],
        ["decir cuál es mejor", "aplicar un acuerdo a la otra comunidad"],
        "Si aparece un juicio de valor, pide que lo reemplace por una descripción.",
    ),
    reinforce="Relee los dos acuerdos y subraya con un color lo que coincide y con otro lo que difiere.",
    extend="Escribe un párrafo de cuatro oraciones que explique por qué es bueno que cada comunidad decida sus límites.",
)

# ============================================================ LS06 clase 6 · comunicar y revisar con validación
LIST6 = "Lista de revisión final (de práctica): 1) ¿Hay un acuerdo o permiso por escrito? 2) ¿Dejé fuera nombres, rostros y lugares exactos? 3) ¿Las palabras de la lengua tienen fuente y las revisó el educador? 4) ¿Declaro para quién es el registro? 5) ¿Anoté el plazo y qué haré al final? 6) ¿La comunidad o el educador validó lo que voy a mostrar?"

L(
    LS6, 6,
    materials="Lápiz y hoja. La lista y los registros están escritos aquí y son inventados para practicar. No necesitas dispositivos.",
    use="Aprenderé a revisar un registro con una lista final y a pedir la validación de la comunidad o del educador tradicional antes de comunicarlo. Sirve para compartir solo lo que está listo y con permiso.",
    prior=["Sé declarar límites en un registro.", "Sé que cada comunidad decide sus límites."],
    explain=[
        "Comunicar un registro es mostrarlo a otras personas. Antes de comunicarlo uso una lista final con seis preguntas: si hay un acuerdo o permiso, si dejé fuera nombres, rostros y lugares exactos, si las palabras de la lengua tienen fuente y fueron revisadas, si declaro para quién es, si anoté el plazo y el cierre, y si la comunidad o el educador validó lo que mostraré.",
        "La validación es la revisión de la persona que corresponde. Si ella dice que algo no se muestra, no se muestra. Si pide un cambio, lo hago. Si pide retirar el registro, lo retiro y devuelvo. Yo no decido sobre los saberes de la comunidad. Mi trabajo es hacer un registro cuidadoso y respetar la decisión.",
        "Cuando todas las respuestas son sí, comunico el registro en el espacio acordado, por ejemplo la sala del curso, y agradezco a quienes participaron. Si alguna respuesta es no, no lo comunico todavía: corrijo, pregunto y reviso otra vez. Esperar un poco es mejor que dañar la confianza de una comunidad.",
    ],
    vocab=[("validación", "revisión de la persona que corresponde"), ("comunicar", "mostrar el registro a otras personas"), ("lista final", "preguntas para revisar antes de mostrar"), ("cierre", "lo que se hará con el registro al terminar el plazo"), ("agradecer", "dar las gracias a quienes participaron")],
    worked=[
        W("Usar la lista", LIST6 + " Un registro cumple las preguntas 1 a 5, pero nadie de la comunidad lo validó. ¿Se puede comunicar?", ["Reviso la pregunta 6.", "La respuesta es no.", "Todavía no se puede comunicar."], "no: falta la validación"),
        W("Responder a una decisión", "El educador tradicional dice que una frase no se debe mostrar. El curso cree que sí se puede. ¿Qué hace?", ["La validación es del educador.", "El curso respeta su decisión.", "Retira la frase."], "retira la frase y no la muestra"),
    ],
    mistakes=[
        M("Mostrar un registro porque ya está terminado, sin pedir validación.", "Puede tener errores o límites que no cumplí.", "Pido la validación antes de comunicar."),
        M("Discutir con el educador cuando pide cambiar algo.", "La decisión sobre los saberes es suya.", "Cambio lo que me pide y agradezco."),
    ],
    R=[
        ex(LIST6 + " ¿Cuántas preguntas tiene la lista final?", "6", "Se cuentan seis preguntas.", "3*2"),
        ex(LIST6 + " ¿Cuál es la pregunta 6?", "¿La comunidad o el educador validó lo que voy a mostrar?", "Está en la lista."),
        ex("Comunicar, ¿es mostrar el registro a otras personas o borrarlo?", "mostrar el registro a otras personas", "Así se definió comunicar."),
    ],
    C=[
        ex(LIST6 + " ¿Qué pregunta revisa que se dejen fuera nombres, rostros y lugares exactos?", "la 2", "La 2 habla de eso."),
        ex("Verdadero o falso: si el educador dice que algo no se muestra, igual puedo mostrarlo si quedó bonito.", "Falso", "Se respeta la decisión."),
        ex(LIST6 + " ¿Qué pregunta se refiere al plazo y al cierre?", "la 5", "La 5 pregunta por el plazo y lo que se hará al final."),
    ],
    A=[
        ex("Un registro responde sí a 4 de las 6 preguntas. ¿Cuántas faltan por cumplir?", "2", "Seis menos cuatro.", "6-4"),
        ex("Ordena los pasos finales: A) comunico en el espacio acordado. B) corrijo lo que falta. C) reviso con la lista. D) pido la validación de la versión ya corregida. Escribe las letras en orden.", "C, B, D, A", "Reviso, corrijo, valido y comunico."),
        ex(LIST6 + " Un registro tiene un rostro y no declara para quién es. ¿Qué preguntas no se cumplen? Escribe los dos números.", "2 y 4", "La 2 pide dejar fuera rostros y la 4 pide declarar para quién es."),
    ],
    Z=[
        ex("Una niña dice: «Como mi registro cumple cinco preguntas, ya está listo». ¿Tiene razón? Sí o No.", "No", "Debe cumplir las seis."),
        ex("La comunidad pide retirar el registro después de que se mostró. ¿Qué es lo correcto: A) cumplir y devolver o B) negarse porque ya se mostró?", "A", "La comunidad puede pedir el retiro."),
    ],
    D=[
        ex("Dos registros. El 1 cumple las seis preguntas y fue validado. El 2 cumple cinco y no se validó. ¿Cuál puede comunicarse: 1 o 2?", "1", "El 2 no cumple la pregunta 6."),
        ex(LIST6 + " Un registro no tiene plazo ni fuente de las palabras. ¿Qué preguntas no se cumplen? Escribe los dos números.", "3 y 5", "La 3 pide la fuente y la 5 pide el plazo."),
    ],
    context=[ex("Terminaste un registro y quieres mostrarlo en la reunión del curso. ¿Primero lo revisas con la lista y pides la validación o lo muestras de inmediato?", "primero lo revisas con la lista y pides la validación", "La revisión y validación van antes de comunicar.")],
    selfcheck=[
        ex("Si una pregunta de la lista dice «no», ¿puedo comunicar el registro? Sí o No.", "No", "Hay algo por corregir."),
        ex("¿Son la comunidad o el educador tradicional quienes validan lo que se refiere a la lengua y la cultura? Sí o No.", "Sí", "Son las personas que corresponden."),
        ex("Después de comunicar, ¿agradezco a quienes participaron? Sí o No.", "Sí", "Es parte de la reciprocidad."),
    ],
    task=T(
        "Lee este registro inventado y revísalo con la lista final: «El 5.º básico de la Escuela Muestra hizo una minga en una plaza que queda en la calle Los Aromos. Grabamos a un vecino y escribimos su nombre completo. Dijimos «mari mari» pero no sabemos quién lo enseñó. Pensamos mostrarlo en otro colegio. Nadie de la comunidad lo ha visto.» En tu cuaderno escribe qué preguntas de la lista no se cumplen y qué harías para corregir cada una. Termina con una pregunta para el educador o educadora tradicional.",
        "No se cumplen: 1 (no hay permiso por escrito), 2 (hay nombre completo y lugar exacto), 3 (falta la fuente de «mari mari»), 4 (se quiere mostrar en otro colegio sin permiso), 5 (no hay plazo ni cierre), 6 (nadie lo validó). Correcciones: pedir permiso, sacar nombre y calle, anotar la fuente, mostrarlo solo donde se autorice, anotar el plazo y pedir la validación. Pregunta: ¿puede revisar el registro antes de que lo mostremos?",
        ["detecta las preguntas no cumplidas", "propone un cambio para cada una", "incluye la validación", "formula una pregunta"],
        ["lista de problemas y cambios", "pregunta"],
        ["dejar pasar el nombre o la calle", "no pedir validación"],
        "Pide que numere cada problema con el número de la pregunta de la lista.",
    ),
    reinforce="Copia la lista final y marca con un visto cada pregunta que ya cumple tu último registro.",
    extend="Escribe una lista final propia de cinco preguntas para un registro de tu curso y explica por qué la última es sobre la validación.",
)
