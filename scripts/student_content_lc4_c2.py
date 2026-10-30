"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR06 (registro con recursos tecnológicos de experiencias cotidianas, con expresiones culturalmente significativas) y
OA LS01 (relatos orales y palabras culturalmente significativas, contexto de sensibilización lingüística).

Criterio de autoría: los relatos son inventados para practicar y no son de ningún pueblo; no se adapta ni se reproduce
ningún relato fundacional o cosmogónico real (eso lo cuenta el portador/a de la tradición). Todas las fichas, escuelas,
listas y personas son inventadas solo para practicar y están rotuladas como tales. Las únicas expresiones en lengua
indígena son saludos y palabras muy atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke); no se
inventa gramática, pronunciación ni significados rituales. Las frases completas en lengua indígena las enseña el
educador/a tradicional. Los recursos digitales se describen sin marcas ni enlaces y siempre con un adulto. Cada tarea
abierta remite al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR6, LS1 = "LC04 OA LR06", "LC04 OA LS01"

CONSULT = " Recuerda: la forma tradicional de escribir, decir y usar estas palabras la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de escritura, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad."

FICHA_SAL = "Ficha: «mari mari» es un saludo y «chaltumay» quiere decir «gracias», ambas en mapuzugun."
FICHA_PAL = "Ficha de palabras en mapuzugun (de práctica): «ko» es agua, «antü» es sol, «kuyen» es luna, «ruka» es la casa mapuche, «mapu» es tierra, «ñuke» es madre."


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


# =================================================================== LR06 clase 1 · propósito, fuente y autorización
FICHA_REG = "Ficha de registro A (inventada para practicar): Qué se registra: la bienvenida a una visita en la Escuela Ejemplo. Para qué: recordar la actividad y agradecer. Palabras en lengua indígena: «mari mari» y «chaltumay», enseñadas por la educadora tradicional de la escuela. Autorización de las personas que aparecen: sí, firmada por sus familias. Autorización de la educadora: sí, solo para guardar en la sala."

L(
    LR6, 1,
    materials="Lápiz y hoja. Las fichas y los casos están escritos aquí; son inventados para practicar. Si usas un dispositivo, hazlo siempre con una persona adulta.",
    use="Aprenderé a decidir, antes de registrar una experiencia con un medio tecnológico, para qué la registro, de quién vienen las palabras y quién da la autorización. Sirve para contar experiencias de mi vida familiar y comunitaria con respeto.",
    prior=["Sé que cada recurso tiene un propósito y unos límites.", "Sé que las palabras de la lengua indígena las enseña el educador o la educadora tradicional."],
    explain=[
        "Registrar es dejar guardada una experiencia para recordarla o compartirla. Puedo registrar con las TIC, que son las tecnologías de la información y la comunicación: un texto en el computador, una foto, una grabación de audio o un video. Pero registrar no es solo apretar un botón: primero decido para qué lo hago.",
        "Antes de registrar contesto cuatro preguntas. ¿Qué experiencia voy a registrar? ¿Para qué: recordar, contar, agradecer o enseñar? ¿De quién son las palabras en lengua indígena que aparecerán y quién me las enseñó? ¿Quién autoriza: las personas que aparecen y la fuente de las palabras? Las respuestas las anoto en una ficha de registro.",
        "La autorización es el sí de las personas que aparecen o cuyo saber uso. Si una persona no quiere aparecer, no la registro. Si la fuente solo autorizó guardar en la sala, no lo muestro afuera. Y no registro experiencias privadas de una familia, a menos que esa familia lo pida. Si falta una respuesta de la ficha, me detengo y pregunto.",
    ],
    vocab=[("registrar", "dejar guardada una experiencia para recordarla o contarla"), ("TIC", "tecnologías que sirven para comunicarse, como el computador o una grabadora"), ("autorización", "el sí de las personas para registrar o usar algo"), ("propósito", "para qué hago el registro"), ("ficha de registro", "papel donde anoto lo que decido antes de registrar")],
    worked=[
        W("Leer una ficha de registro", FICHA_REG + " ¿Quién autorizó que se guarde el registro solo en la sala?", ["Busco la línea de la educadora.", "Dice: autorización de la educadora, solo para guardar en la sala.", "Fue la educadora tradicional."], "la educadora tradicional"),
        W("Detenerse si falta un dato", "Ficha B (inventada): Qué se registra: una conversación en el recreo. Para qué: no se indica. Palabras en lengua indígena: «kuyen», sin fuente. Autorización: no se indica. ¿Se puede empezar a registrar?", ["Reviso los datos de la ficha.", "Faltan el propósito, la fuente y la autorización.", "Me detengo y pregunto antes de registrar."], "no: faltan el propósito, la fuente y la autorización"),
    ],
    mistakes=[
        M("Grabar a un compañero en el recreo sin preguntarle porque «es solo un rato».", "Nadie debe ser registrado sin su autorización.", "Pregunto si quiere aparecer y, si dice que no, no lo registro."),
        M("Empezar a registrar antes de saber para qué.", "Sin propósito no sé qué guardar ni a quién mostrarlo.", "Anoto primero el propósito en la ficha."),
    ],
    R=[
        ex(FICHA_REG + " ¿Para qué se registra la bienvenida?", "para recordar la actividad y agradecer", "Lo dice la línea «Para qué»."),
        ex("Una foto, una grabación de audio y un video, ¿son medios de las TIC o de la alfarería?", "de las TIC", "Son tecnologías para registrar y comunicar."),
        ex("Si una persona no quiere aparecer en mi registro, ¿la registro igual o respeto su decisión?", "respeto su decisión", "Sin su autorización no se registra."),
    ],
    C=[
        ex("Verdadero o falso: puedo registrar una experiencia sin saber para qué la hago.", "Falso", "El propósito se decide antes de registrar."),
        ex(FICHA_REG + " ¿Quién enseñó las palabras «mari mari» y «chaltumay»?", "la educadora tradicional de la escuela", "Es la fuente que anota la ficha."),
        ex("En la ficha B del caso trabajado (conversación en el recreo), la línea «Para qué» dice «no se indica». ¿Qué dato falta: el propósito o el color?", "el propósito", "«Para qué» es la línea del propósito."),
    ],
    A=[
        ex("Cuatro preguntas antes de registrar: qué, para qué, de quién son las palabras y quién autoriza. Si una ficha responde solo la primera y la segunda, ¿cuántas preguntas le faltan?", "2", "4 − 2 = 2."),
        ex("Un curso quiere guardar el registro de la ficha A en un lugar abierto de internet. La educadora autorizó «solo para guardar en la sala». ¿Puede? Sí o No.", "No", "El permiso limita dónde se guarda."),
        ex("Tres propósitos posibles: A) agradecer a una visita. B) burlarse de cómo habla alguien. C) recordar una actividad. ¿Cuáles son respetuosos? Escribe las letras.", "A y C", "La burla daña a las personas."),
    ],
    Z=[
        ex("Una niña dice: «Si muchas personas aparecen en el registro, con que una autorice basta». ¿Tiene razón? Sí o No.", "No", "Cada persona que aparece debe autorizar."),
        ex("Un niño quiere registrar con un teléfono una experiencia privada de una familia sin preguntarle. ¿Qué es mejor: A) registrar y pedir permiso después. B) preguntar antes y registrar solo si la familia lo pide?", "B", "Primero se pregunta."),
    ],
    D=[
        ex("Ordena los pasos antes de registrar: A) escribo el propósito. B) pido autorización. C) anoto la fuente de las palabras. D) registro. Escribe las letras en orden.", "A, C, B, D", "Primero propósito y fuente, luego autorización y al final registro."),
        arith("En un registro aparecen 12 estudiantes y solo 9 tienen autorización de su familia. ¿Cuántos estudiantes no deberían aparecer?", "12-9", "Se restan los autorizados de los que aparecen."),
    ],
    context=[ex("Quieres grabar el audio de una visita que saluda al curso con «mari mari». Ella no ha dicho si acepta. ¿Le preguntas primero o grabas para después contarle?", "le pregunto primero", "La autorización va antes del registro.")],
    selfcheck=[
        ex("¿Qué dato anoto primero en la ficha de registro: el propósito o el almacenamiento?", "el propósito", "Primero decido para qué registro."),
        ex("Si falta la fuente de una palabra en lengua indígena, ¿sigo adelante o me detengo y pregunto?", "me detengo y pregunto", "Sin fuente no sé si la palabra está bien."),
        ex("¿Deben autorizar tanto las personas que aparecen como la fuente de las palabras? Sí o No.", "Sí", "Ambas deben dar su sí."),
    ],
    task=T(
        "Lee esta situación inventada para practicar: «Un curso quiere registrar con un computador, y con un adulto, un texto breve que cuente cómo recibieron a una visita en la escuela. En el texto aparecerán las palabras «mari mari» y «chaltumay».» " + FICHA_SAL + " En tu cuaderno completa una ficha de registro con estas cuatro líneas: qué se registra, para qué, quién enseñó las palabras y quién autoriza. Si no sabes un dato, escribe «por preguntar». Termina con una pregunta para el educador o la educadora tradicional.",
        "Qué: cómo recibimos a una visita. Para qué: recordar y agradecer. Palabras: «mari mari» y «chaltumay», enseñadas por la educadora tradicional. Autoriza: la educadora y las familias. Pregunta: ¿cuánto tiempo podemos guardar este registro?",
        ["completa las cuatro líneas de la ficha", "nombra la fuente de las palabras", "escribe «por preguntar» donde no sabe", "formula una pregunta para el educador/a tradicional"],
        ["ficha de registro de cuatro líneas", "pregunta escrita o dicha en voz alta"],
        ["registrar sin autorización", "no anotar el propósito"],
        "Comprueba que las cuatro líneas tengan información real; si inventó una autorización, pídele que escriba «por preguntar».",
    ),
    reinforce="Vuelve a leer la ficha A y señala con el dedo la línea del propósito, la de la fuente y la de la autorización.",
    extend="Escribe una ficha de registro de cuatro líneas para algo que quisieras registrar de la vida de tu sala.",
)

# =================================================================== LR06 clase 2 · medio accesible y seguro
OPCIONES = "Medios de práctica: A) un texto escrito a mano. B) un dibujo con rótulos. C) un audio grabado con un dispositivo del colegio. D) un video con rostros de estudiantes."

L(
    LR6, 2,
    materials="Lápiz y hoja. Las opciones y los casos están escritos aquí. No necesitas ningún dispositivo para esta clase; puedes responder por escrito o con dibujos.",
    use="Aprenderé a elegir el medio para registrar una experiencia según lo que tengo, lo que es seguro y quién podrá usarlo. Sirve para registrar sin gastar de más, sin exponerme y para que todos puedan participar.",
    prior=["Sé que antes de registrar defino propósito, fuente y autorización.", "Sé que no puedo registrar a nadie sin su permiso."],
    explain=[
        "Un medio es la forma en que registro una experiencia: un texto, un dibujo, una foto, un audio o un video. Cada medio tiene ventajas y riesgos. El texto es simple y no muestra rostros. El audio guarda la voz de quien habla. La foto y el video muestran la cara y el lugar de las personas.",
        "Un medio accesible es el que todos pueden usar. Si no tengo internet, escribo o dibujo a mano. Si alguien no puede escribir, puede contar su experiencia en voz alta y otra persona la anota con su permiso. Un medio seguro no muestra rostros ni lugares privados sin permiso y no se sube a sitios abiertos. También elijo el que no necesita crear una cuenta ni dar datos.",
        "Para elegir hago tres preguntas: ¿puedo hacerlo con lo que tengo? ¿protege a las personas que aparecen? ¿sirve al propósito? Siempre hay una alternativa analógica, es decir, sin tecnología: un dibujo, un texto escrito o una conversación. Usar un dispositivo no es obligatorio para registrar bien.",
    ],
    vocab=[("medio", "forma de registrar, como texto, dibujo, audio o video"), ("accesible", "que todas las personas pueden usar"), ("seguro", "que no expone a las personas ni sus datos"), ("analógico", "sin tecnología digital, como un dibujo en papel"), ("cuenta", "registro con nombre y contraseña en un sitio de internet")],
    worked=[
        W("Elegir un medio seguro", OPCIONES + " Propósito: contar una actividad del curso sin mostrar rostros. ¿Qué medio no sirve?", ["Reviso qué medios muestran rostros.", "El video D muestra los rostros de estudiantes.", "No sirve D."], "D"),
        W("Medio sin internet", "En una casa no hay internet ni computador. Quieren registrar una experiencia para llevar al colegio. ¿Qué medio analógico pueden usar?", ["Busco un medio que no necesite tecnología.", "Un texto escrito a mano o un dibujo con rótulos sirve.", "Elijo escribir o dibujar."], "un texto escrito a mano o un dibujo"),
    ],
    mistakes=[
        M("Pensar que un registro solo es válido si es un video.", "Un texto o un dibujo también registran bien una experiencia.", "Elijo el medio que sirve al propósito y que todos puedan usar."),
        M("Crear una cuenta con mi nombre y mis datos para guardar un trabajo del curso.", "Entrego datos personales sin necesidad.", "Uso una herramienta sin cuenta y con un adulto, o un medio en papel."),
    ],
    R=[
        ex(OPCIONES + " ¿Qué medio no necesita ningún dispositivo: A o C?", "A", "El texto escrito a mano no necesita tecnología."),
        ex("Un video con rostros, ¿muestra a las personas o no las muestra?", "las muestra", "El video enseña la cara de quienes aparecen."),
        ex("Un medio analógico, ¿necesita internet? Sí o No.", "No", "Analógico quiere decir sin tecnología digital."),
    ],
    C=[
        ex("Verdadero o falso: un dibujo con rótulos puede ser un registro válido de una experiencia.", "Verdadero", "El dibujo también guarda la experiencia."),
        ex(OPCIONES + " ¿Cuál guarda solo la voz, sin mostrar rostros: C o D?", "C", "El audio guarda la voz sin imagen; el video, además, muestra las caras."),
        ex("Un medio accesible es A) el que todos pueden usar. B) el más caro. ¿Cuál es?", "A", "Accesible significa que todos pueden usarlo."),
    ],
    A=[
        ex("Un curso no tiene internet y quiere registrar una actividad con la educadora. De las opciones A, B, C y D, ¿cuáles son las dos que no necesitan ningún dispositivo? Escribe las letras.", "A y B", "El texto y el dibujo en papel no necesitan tecnología; C y D usan un dispositivo."),
        ex("Un estudiante no puede escribir por una lesión en la mano. Quiere registrar una experiencia. ¿Qué alternativa le propones: A) contar en voz alta y que alguien la anote con su permiso. B) no registrar?", "A", "La experiencia se puede registrar de otra manera."),
        ex("Una herramienta pide crear una cuenta con nombre completo y dirección. Otra funciona sin cuenta. ¿Cuál eliges para un trabajo del curso?", "la que funciona sin cuenta", "No se entregan datos personales sin necesidad."),
    ],
    Z=[
        ex("Una niña dice: «Si grabo un video, el registro es mejor que un texto». ¿Es siempre cierto? Sí o No.", "No", "Depende del propósito y del cuidado de las personas."),
        ex("Propósito: guardar la opinión de varios estudiantes sin mostrar sus rostros. Opciones: A) video. B) texto escrito con sus iniciales y permiso. ¿Cuál cuida mejor?", "B", "El texto no muestra rostros."),
    ],
    D=[
        arith("Cinco medios: texto, dibujo, foto, audio y video. Tres de ellos (foto, audio y video) pueden guardar la imagen o la voz de una persona. ¿Cuántos medios no lo hacen?", "5-3", "Se restan los tres medios que guardan imagen o voz."),
        ex("Ordena las tres preguntas como aparecen en la explicación de esta clase: A) pregunto si protege a las personas. B) pregunto si lo puedo hacer con lo que tengo. C) pregunto si sirve al propósito. Escribe las letras.", "B, A, C", "Primero lo posible, luego lo seguro y al final el propósito."),
    ],
    context=[ex("Tu curso quiere agradecer a una visita y varias familias no quieren que sus hijos salgan en fotos. ¿Proponen una tarjeta dibujada por el curso o una foto del curso?", "una tarjeta dibujada por el curso", "El dibujo no muestra rostros y todos pueden participar.")],
    selfcheck=[
        ex("¿Qué es un medio de registro?", "la forma en que registro una experiencia", "Es texto, dibujo, audio o video."),
        ex("Si no hay internet, ¿qué alternativa uso: una analógica o ninguna?", "una analógica", "Siempre hay una alternativa sin tecnología."),
        ex("¿Debo crear una cuenta con mis datos para registrar un trabajo del curso? Sí o No.", "No", "Se elige una herramienta sin cuenta o un medio en papel."),
    ],
    task=T(
        "Lee este caso inventado para practicar: «Un curso quiere registrar cómo recibe a una visita con el saludo «mari mari». Hay una sala sin internet y una familia pidió que su hijo no salga en fotos.» " + FICHA_SAL + " " + OPCIONES + " En tu cuaderno haz una tabla con tres columnas: medio, ventaja y riesgo, para los medios A, B, C y D. Después escribe cuál elegirías y por qué. Termina con una pregunta para la educadora tradicional.",
        "Elijo B, el dibujo con rótulos, porque no necesita internet, no muestra rostros y todos pueden participar. Riesgo: que se copie algún símbolo tradicional. Pregunta: ¿qué palabras puedo rotular en el dibujo?",
        ["completa la tabla con ventaja y riesgo", "elige un medio que no exponga a la familia", "justifica su elección", "formula una pregunta para el educador/a tradicional"],
        ["tabla de cuatro medios", "elección justificada y pregunta escritas"],
        ["elegir un video con rostros", "no considerar que no hay internet"],
        "Comprueba que la elección cuide a la familia y que sea posible sin internet; si eligió video con rostros, conversa por qué se pidió no mostrar al estudiante.",
    ),
    reinforce="Escribe tres medios para registrar una experiencia y marca con una cruz los que muestran la cara de las personas.",
    extend="Explica a una persona de tu casa por qué un dibujo puede ser un buen registro.",
)

# =================================================================== LR06 clase 3 · registrar sin exponer datos ni saberes restringidos
LISTA_DAT = "Lista de datos de práctica: 1) nombre de pila, 2) apellido completo, 3) dirección de la casa, 4) teléfono, 5) el saludo «mari mari», 6) la agenda de una familia."

L(
    LR6, 3,
    materials="Lápiz y hoja. Los casos están escritos aquí. Todo es de práctica y puedes hacerlo en papel.",
    use="Aprenderé a reconocer los datos personales y los saberes restringidos para no ponerlos en un registro. Sirve para proteger a las personas y respetar lo que una comunidad cuida.",
    prior=["Sé elegir un medio accesible y seguro.", "Sé que cada persona decide qué cuenta de su vida."],
    explain=[
        "Un dato personal es un dato que identifica a una persona: su nombre completo, su dirección, su teléfono, su colegio o su rostro. Si lo pongo en un registro, cualquiera podría saber quién es y dónde encontrarla. Por eso no lo incluyo. Uso solo lo que ella autoriza, por ejemplo su nombre de pila.",
        "Un saber restringido es un conocimiento que una familia o una comunidad comparte solo en ciertos momentos, con ciertas personas o de cierta forma. No sé siempre cuáles son. Por eso, si no estoy seguro de que algo se pueda registrar, no lo registro y pregunto al educador tradicional o a quien lo cuida.",
        "Hay cosas que sí puedo registrar: una actividad de la sala, un saludo que la educadora nos autorizó a usar, un dibujo hecho por el curso. Al registrar una experiencia de mi casa, hablo de ella sin dar nombres, direcciones ni detalles que no quiero que se sepan. Registrar bien es contar lo justo.",
    ],
    vocab=[("dato personal", "dato que identifica a una persona"), ("saber restringido", "conocimiento que se comparte solo en ciertos casos o con ciertas personas"), ("exponer", "dejar a la vista algo que debía cuidarse"), ("autorizado", "con permiso de quien corresponde"), ("identificar", "reconocer quién es una persona")],
    worked=[
        W("Separar los datos", LISTA_DAT + " ¿Cuáles de los seis son datos personales que no pongo en un registro?", ["Pienso cuáles identifican a una persona.", "Apellido completo, dirección, teléfono y la agenda de una familia identifican.", "El nombre de pila lo usaré solo si lo autoriza; el saludo ya fue autorizado."], "2, 3, 4 y 6"),
        W("Qué hacer ante la duda", "Un niño quiere registrar un canto que escuchó en una reunión de la comunidad, pero no sabe si se puede compartir. ¿Qué hace?", ["Un canto puede ser un saber restringido.", "No sé si está autorizado.", "No lo registra y pregunta al educador tradicional."], "no lo registra y pregunta al educador tradicional"),
    ],
    mistakes=[
        M("Poner el apellido y la dirección de mis compañeros para que el registro sea «más completo».", "Esos datos permiten ubicar a personas.", "Pongo solo «estudiantes del curso» o el nombre de pila con permiso."),
        M("Registrar algo de la comunidad porque lo escuché, aunque nadie me dijo que podía.", "Puede ser un saber que se comparte solo de cierta forma.", "Pregunto antes y no lo registro si no hay permiso."),
    ],
    R=[
        ex(LISTA_DAT + " ¿El teléfono es un dato personal? Sí o No.", "Sí", "Con el teléfono se puede ubicar a una persona."),
        ex("Si no estoy seguro de que algo se pueda registrar, ¿lo registro o pregunto?", "pregunto", "Ante la duda se pregunta."),
        ex("Un nombre de pila es solo el primer nombre, como «Ana». ¿Es lo mismo que un nombre completo con apellidos? Sí o No.", "No", "El nombre completo tiene más datos."),
    ],
    C=[
        ex("Verdadero o falso: una dirección es un dato personal que no pongo en un registro.", "Verdadero", "Permite ubicar la casa de una persona."),
        ex("Un saber restringido es un conocimiento que se comparte A) con cualquiera, en cualquier momento. B) solo en ciertos momentos o con ciertas personas. ¿Cuál es?", "B", "Esa es la idea de «restringido»."),
        ex("Dos cosas: el saludo «mari mari» autorizado por la educadora y el apellido de una compañera. ¿Cuál puede ir en un registro con permiso de la fuente?", "el saludo «mari mari»", "El saludo fue autorizado; el apellido es un dato personal."),
    ],
    A=[
        ex(LISTA_DAT + " Si de esa lista solo se puede usar el nombre de pila con permiso y el saludo ya autorizado, ¿cuántos datos de la lista se pueden usar?", "2", "Son el 1 y el 5."),
        ex("Quieres contar que ayudaste en tu casa. ¿Cuál frase cuida mejor la privacidad: A) «Ayudé a ordenar la mesa». B) «Ayudé en Calle Roble 123 a ordenar la mesa»?", "A", "La B incluye una dirección."),
        ex("Un compañero propone grabar en audio una conversación que escuchó entre adultos de la comunidad sobre su manera de celebrar. ¿Qué haces: A) lo grabas. B) preguntas a la educadora tradicional si se puede?", "B", "No sabemos si es un saber restringido."),
    ],
    Z=[
        ex("Una niña dice: «Si un dato es verdadero, puedo ponerlo en el registro». ¿Tiene razón? Sí o No.", "No", "Aunque sea verdadero, puede ser personal o restringido."),
        ex("Dos registros: 1) «Hoy saludamos a la visita con «mari mari»». 2) «Hoy la familia de Pedro Soto, que vive en la esquina de la plaza, saludó a la visita». ¿Cuál protege mejor la privacidad?", "1", "El 2 da un apellido y un lugar."),
    ],
    D=[
        arith("De los 6 datos de la lista, 4 no se pueden poner en un registro. ¿Cuántos sí se pueden considerar para el registro?", "6-4", "Se restan los datos que no se pueden usar."),
        ex("Ordena para decidir qué registrar: A) pregunto a la fuente si tengo dudas. B) separo datos personales. C) reviso si hay saberes restringidos. Escribe las letras.", "B, C, A", "Separo lo personal, reviso lo restringido y pregunto lo que no sé."),
    ],
    context=[ex("Una persona mayor de tu familia te cuenta cómo se hace una celebración y tú quieres escribirla en el cuaderno del curso. ¿La escribes con nombres y detalles o le preguntas qué parte se puede contar?", "le preguntas qué parte se puede contar", "Cada familia decide qué comparte.")],
    selfcheck=[
        ex("¿Qué dato identifica a una persona: su dirección o el color de su mochila?", "su dirección", "Permite saber dónde vive."),
        ex("Si algo puede ser un saber restringido, ¿lo registro o pregunto?", "pregunto", "Sin permiso no lo registro."),
        ex("¿Decide cada persona qué cosas de su vida se registran? Sí o No.", "Sí", "Cada persona decide qué comparte."),
    ],
    task=T(
        "Lee este caso inventado para practicar: «Un curso quiere escribir en el computador, con un adulto, un texto breve que cuente una actividad de la sala. Cada estudiante tiene sus datos en una ficha: nombre completo, dirección, teléfono y nombre de pila. La educadora tradicional autorizó usar el saludo «mari mari».» " + FICHA_SAL + " En tu cuaderno escribe: 1) qué datos de la ficha pondrías en el texto y cuáles no, 2) una frase corta que cuente la actividad con el saludo autorizado, 3) una pregunta para la educadora sobre qué más se puede registrar.",
        "Pondría solo el nombre de pila con permiso. No pondría nombre completo, dirección ni teléfono. Frase: «Saludamos a la visita con «mari mari»». Pregunta: ¿qué otras palabras puedo registrar?",
        ["separa los datos que sí y los que no", "no escribe datos personales", "escribe una frase con el saludo autorizado", "formula una pregunta para el educador/a tradicional"],
        ["lista de datos separada", "frase y pregunta escritas"],
        ["incluir la dirección o el teléfono", "usar palabras sin autorización"],
        "Comprueba que no aparezcan datos personales; si incluyó uno, conversa por qué ese dato permitiría ubicar a una persona.",
    ),
    reinforce="Haz dos listas en tu cuaderno: datos que no pongo en un registro y datos que sí puedo poner con permiso.",
    extend="Escribe una frase que cuente algo de tu casa sin dar ningún dato personal.",
)

# =================================================================== LR06 clase 4 · revisar lengua, contexto, autoría y almacenamiento
BORRADOR = "Borrador de práctica (inventado): «Hoy vino una visita. Dijimos mari marí y después chaltumay. Pedro Soto y Ana Rojas hicieron un dibujo. Lo guardamos en un sitio abierto de internet.»"

L(
    LR6, 4,
    materials="Lápiz y un lápiz de otro color para marcar. El borrador y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a revisar un registro con cuatro preguntas: la lengua, el contexto, la autoría y el almacenamiento. Sirve para entregar un trabajo cuidadoso y respetuoso.",
    prior=["Sé decidir propósito, fuente y autorización.", "Sé elegir un medio seguro y no exponer datos personales."],
    explain=[
        "Revisar un registro es leerlo de nuevo con cuatro preguntas. La lengua: ¿las palabras en lengua indígena están escritas igual que en la ficha de la fuente? El contexto: ¿cuenta cuándo, dónde y para qué se dijo o hizo? La autoría: ¿dice quién enseñó las palabras y quiénes hicieron el registro? El almacenamiento: ¿dónde queda guardado y quién puede verlo?",
        "Para la lengua comparo letra por letra con la ficha: «mari mari» y «chaltumay» no cambian. Para el contexto agrego, por ejemplo, «Hoy, en la sala, cuando llegó una visita». Para la autoría escribo «Palabras enseñadas por la educadora tradicional. Registro hecho por el curso». No pongo apellidos ni datos personales.",
        "El almacenamiento es el lugar donde guardo el registro, como una carpeta del colegio, una hoja en la sala o un cuaderno. Lo guardo donde la fuente autorizó y no en sitios abiertos. Si una de las cuatro respuestas falla, corrijo antes de terminar; y si no puedo decidir algo, se lo pregunto a la educadora tradicional.",
    ],
    vocab=[("revisar", "leer de nuevo con preguntas para mejorar"), ("contexto", "cuándo, dónde y para qué ocurrió algo"), ("autoría", "quién hizo o enseñó algo"), ("almacenamiento", "lugar donde se guarda un registro"), ("sitio abierto", "lugar de internet que cualquier persona puede ver")],
    worked=[
        W("Revisar la lengua", BORRADOR + " " + FICHA_SAL + " ¿Cuántas expresiones en lengua indígena están mal escritas?", ["Comparo con la ficha: «mari mari» y «chaltumay».", "«Chaltumay» coincide.", "En el borrador dice «marí» con tilde; la ficha no la tiene."], "1 (marí debe ser mari)"),
        W("Revisar el almacenamiento", BORRADOR + " ¿Qué problema tiene el almacenamiento?", ["Busco dónde se guardó: en un sitio abierto de internet.", "Un sitio abierto lo ve cualquier persona.", "La fuente solo autorizó guardar en la sala."], "se guardó en un sitio abierto; debe guardarse en la sala"),
    ],
    mistakes=[
        M("Revisar solo la ortografía y no la autoría ni el almacenamiento.", "Un registro bien escrito puede igual exponer a personas.", "Reviso las cuatro preguntas: lengua, contexto, autoría y almacenamiento."),
        M("Dejar los apellidos de mis compañeros porque ya estaban escritos.", "Son datos personales.", "Los reemplazo por «el curso» o por el nombre de pila con permiso."),
    ],
    R=[
        ex("Las cuatro preguntas de la revisión son lengua, contexto, autoría y almacenamiento. ¿Cuántas son?", "4", "Se nombran cuatro preguntas distintas."),
        ex("El almacenamiento, ¿es dónde se guarda el registro o quién lo escribió?", "dónde se guarda el registro", "Quién lo hizo es la autoría."),
        ex("La autoría, ¿dice quién hizo o enseñó algo, o dónde se guarda?", "quién hizo o enseñó algo", "Dónde se guarda es el almacenamiento."),
    ],
    C=[
        ex("Verdadero o falso: un registro puede guardarse en un sitio abierto si quedó muy bien escrito.", "Falso", "El lugar debe respetar el permiso de la fuente."),
        ex("En el borrador de práctica, ¿qué dato personal aparece: los nombres completos de dos estudiantes o el saludo?", "los nombres completos de dos estudiantes", "Pedro Soto y Ana Rojas se identifican con nombre y apellido."),
        ex("El contexto de un registro responde A) cuándo, dónde y para qué. B) con qué color se escribió. ¿Cuál es?", "A", "Contexto es lo que rodea lo ocurrido."),
    ],
    A=[
        ex(BORRADOR + " Cuenta los problemas: 1) «marí» mal escrito, 2) apellidos, 3) almacenamiento abierto, 4) falta la autoría de la educadora. ¿Cuántos problemas hay en total?", "4", "Son cuatro, uno por cada pregunta de revisión."),
        ex("¿Cómo queda mejor la parte «Pedro Soto y Ana Rojas hicieron un dibujo» sin datos personales? A) «El curso hizo un dibujo». B) «Pedro y Ana Rojas hicieron un dibujo».", "A", "La B deja un apellido; «el curso» no identifica a nadie."),
        ex("Completa la autoría: «Palabras enseñadas por ____. Registro hecho por el curso». Elige: la educadora tradicional o un sitio de internet.", "la educadora tradicional", "Ella es la fuente de las palabras."),
    ],
    Z=[
        ex("Un niño dice: «Si las palabras están bien escritas, el registro ya está listo». ¿Tiene razón? Sí o No.", "No", "Faltan contexto, autoría y almacenamiento."),
        ex("Dos formas de guardar: A) en una carpeta del colegio autorizada. B) en un sitio abierto porque «así lo ven más personas». ¿Cuál respeta el permiso de «solo para guardar en la sala»?", "A", "La carpeta del colegio respeta el permiso."),
    ],
    D=[
        arith("Un registro tiene 4 preguntas de revisión y falló en 1. ¿Cuántas están bien?", "4-1", "Se restan las preguntas que fallaron."),
        ex("Ordena la revisión: A) compruebo dónde se guardará. B) comparo las palabras con la ficha. C) reviso que diga quién enseñó. D) agrego cuándo y dónde ocurrió. Escribe las letras en el orden de las preguntas (lengua, contexto, autoría, almacenamiento).", "B, D, C, A", "Lengua, contexto, autoría y almacenamiento."),
    ],
    context=[ex("Tu curso terminó un texto y un compañero dice: «Súbanlo a internet para que lo vea todo el mundo». La educadora autorizó guardarlo solo en la sala. ¿Qué respondes: «Respetemos el permiso» o «Hagámoslo igual»?", "«Respetemos el permiso»", "El almacenamiento debe respetar la autorización.")],
    selfcheck=[
        ex("¿Qué comparo para revisar la lengua: mi texto con la ficha de la fuente o con mi memoria?", "con la ficha de la fuente", "La ficha es la referencia válida."),
        ex("Si falta decir quién enseñó las palabras, ¿qué pregunta de revisión falla?", "la de la autoría", "La autoría dice quién enseñó."),
        ex("¿Dejo apellidos en un registro del curso? Sí o No.", "No", "Son datos personales."),
    ],
    task=T(
        "Revisa este borrador inventado para practicar. " + BORRADOR + " " + FICHA_SAL + " En tu cuaderno haz una tabla de cuatro filas (lengua, contexto, autoría, almacenamiento). En cada fila escribe qué encontraste y cómo lo corregirías. Termina con una pregunta para el educador o la educadora tradicional.",
        "Lengua: «marí» debe ser «mari» como en la ficha. Contexto: agrego «en la sala, cuando llegó la visita». Autoría: «Palabras enseñadas por la educadora tradicional; registro hecho por el curso». Almacenamiento: se guarda en la sala, no en un sitio abierto. Pregunta: ¿puedo guardar una copia en papel?",
        ["completa las cuatro filas", "elimina los apellidos", "corrige el almacenamiento según el permiso", "formula una pregunta para el educador/a tradicional"],
        ["tabla de revisión de cuatro filas", "pregunta escrita o dicha en voz alta"],
        ["revisar solo la ortografía", "dejar el sitio abierto"],
        "Verifica que revisó las cuatro preguntas; si dejó el sitio abierto o los apellidos, conversa por qué eso expone a las personas.",
    ),
    reinforce="Escribe en una tarjeta las cuatro preguntas de revisión: lengua, contexto, autoría y almacenamiento.",
    extend="Revisa un texto breve de tu cuaderno con las cuatro preguntas y anota qué cambiarías.",
)

# =================================================================== LS01 clase 1 · acercarse sin apropiarse
L(
    LS1, 1,
    materials="Lápiz y hoja. Las situaciones están escritas aquí; son inventadas para practicar. Nadie tiene que repetir sonidos ni contar datos de su familia.",
    use="Aprenderé a escuchar con respeto relatos orales de otro pueblo, a distinguir aprender, reproducir, recrear y apropiarse, y a cuidar lo que una comunidad guarda. Sirve para valorar relatos que cuentan cómo un pueblo entiende el mundo.",
    prior=["Sé escuchar sin interrumpir.", "Sé que el educador o la educadora tradicional enseña la lengua y la cultura de su pueblo."],
    explain=[
        "Un relato oral es una historia que se cuenta en voz alta y se transmite de unas personas a otras. Un relato fundacional o cosmogónico cuenta cómo un pueblo entiende su origen y el del mundo. Por eso es muy importante para esa comunidad. Lo cuentan quienes tienen la tradición de contarlo, en ciertos momentos y de cierta forma.",
        "Para acercarme con respeto escucho con atención, sin interrumpir ni burlarme. Distingo cuatro actitudes. Aprender es escuchar y entender con quien sabe. Reproducir es repetir tal cual algo que me dieron permiso de repetir. Recrear es hacer algo nuevo inspirado en lo escuchado, avisando y con permiso. Apropiarse es tomar como mío lo de otros, y eso no se hace.",
        "No cambio los relatos de otro pueblo ni los transformo en cuentos graciosos. No los dramatizo con disfraces sin que su comunidad lo permita. Si quiero compartir lo que aprendí, digo quién lo contó y a qué pueblo pertenece. Y si no sé, lo pregunto. Un relato tradicional no se inventa ni se completa con mi imaginación.",
    ],
    vocab=[("relato oral", "historia que se cuenta en voz alta"), ("cosmogónico", "que cuenta cómo un pueblo entiende el origen del mundo"), ("aprender", "escuchar y entender con quien sabe"), ("reproducir", "repetir tal cual con permiso"), ("apropiarse", "tomar como propio lo de otros sin permiso ni crédito")],
    worked=[
        W("Clasificar una acción", "Una niña escucha un relato que cuenta una visita y después dice a sus amigos que ella lo inventó. ¿Aprende o se apropia?", ["Escuchó el relato, eso está bien.", "Pero después dice que es suyo.", "Toma como propio lo de otra persona."], "se apropia"),
        W("Elegir una respuesta respetuosa", "Un compañero quiere disfrazarse y actuar un relato de un pueblo para hacer reír. ¿Qué le dices: A) «Preguntemos al educador tradicional si se puede». B) «Dale, hazlo más gracioso»?", ["La burla o el disfraz pueden dañar un relato importante.", "La A propone consultar a quien lo cuida.", "Elijo A."], "A"),
    ],
    mistakes=[
        M("Agregarle un final inventado a un relato de otro pueblo.", "Cambia una historia que no me pertenece.", "Escucho el relato como lo cuenta quien lo conoce."),
        M("Disfrazarme para dramatizar un relato sin preguntar.", "Puedo faltar el respeto a su comunidad.", "Pregunto al educador tradicional qué se puede hacer."),
    ],
    R=[
        ex("Un relato oral, ¿se cuenta en voz alta o se dibuja?", "se cuenta en voz alta", "Oral quiere decir que se dice con la voz."),
        ex("Al escuchar a una visita, ¿qué hago primero: escuchar con atención o interrumpir?", "escuchar con atención", "La atención muestra respeto."),
        ex("Apropiarse de un relato, ¿es tomarlo como mío o aprenderlo con quien sabe?", "tomarlo como mío", "Aprender es lo contrario."),
    ],
    C=[
        ex("Une: 1) repetir tal cual con permiso. 2) hacer algo nuevo inspirado, avisando y con permiso. Escribe la palabra de cada una.", "reproducir, recrear", "La 1 es reproducir y la 2, recrear."),
        ex("Verdadero o falso: puedo cambiar el final de un relato tradicional porque me parece más bonito.", "Falso", "El relato pertenece a su comunidad."),
        ex("Un relato fundacional cuenta cómo un pueblo entiende su origen. ¿Es importante para esa comunidad? Sí o No.", "Sí", "Habla de su origen y su forma de ver el mundo."),
    ],
    A=[
        ex("Acciones: A) escuchar sin interrumpir. B) disfrazarme para burlarme. C) preguntar con respeto quién lo cuenta. D) decir que el relato es mío. ¿Cuáles son respetuosas? Escribe las letras.", "A y C", "B y D no respetan a quien lo cuenta."),
        ex("Después de escuchar un relato, un niño propone contarlo en la reunión de apoderados diciendo quién se lo contó y a qué pueblo pertenece, con permiso de la educadora. ¿Qué actitud es: aprender, reproducir o apropiarse?", "reproducir", "Lo repite tal cual y con permiso."),
        ex("La visita no pidió que el curso repitiera sus palabras. ¿Puede el curso participar escuchando y preguntando? Sí o No.", "Sí", "Escuchar y preguntar es participar."),
    ],
    Z=[
        ex("Un niño dice: «Si cuento un relato igual que la visita, ya es mío». ¿Qué falta para que sea respetuoso: decir quién lo contó o contarlo más fuerte?", "decir quién lo contó", "Dar crédito evita la apropiación."),
        ex("Un grupo quiere hacer una obra de teatro basada en un relato de otro pueblo, cambiando partes para hacerla divertida. ¿Es respetuoso? Sí o No.", "No", "Cambia un relato que no es suyo y puede ofender."),
    ],
    D=[
        ex("Tres acciones: 1) copiar un relato diciendo que es tuyo. 2) escucharlo y preguntar de qué pueblo viene. 3) contarlo con permiso nombrando a quien te lo contó. ¿Cuál es una apropiación? Escribe el número.", "1", "Es la que lo presenta como propio."),
        ex("Ordena: A) pregunto si puedo compartirlo. B) escucho con atención. C) lo comparto diciendo quién lo contó. Escribe las letras.", "B, A, C", "Escucho, pido permiso y recién comparto."),
    ],
    context=[ex("Una visita termina de contar un relato y un compañero susurra que lo repetirá en otro curso «como si fuera suyo». ¿Qué le dices: «Mejor preguntémosle a la visita» o «Hazlo»?", "«Mejor preguntémosle a la visita»", "Pedir permiso y dar crédito es lo respetuoso.")],
    selfcheck=[
        ex("¿Qué es apropiarse de un relato?", "tomarlo como mío sin permiso ni crédito", "Es lo contrario de aprender con respeto."),
        ex("Si no quiero repetir una palabra, ¿cómo participo?", "escuchando y preguntando", "Escuchar es participar."),
        ex("¿A quién le pregunto si puedo compartir un relato de una comunidad?", "al educador tradicional o a la comunidad", "Ellos lo cuidan."),
    ],
    task=T(
        "Lee esta situación inventada para practicar: «Una visita contó un relato de su comunidad. Dos estudiantes dijeron cosas diferentes. Una: «Escuchemos y preguntemos de dónde viene». Otro: «Contémoslo en otro curso diciendo que lo inventamos nosotros».» En tu cuaderno escribe: 1) cuál estudiante aprende y cuál se apropia, 2) una pregunta respetuosa para la visita, 3) qué haces tú si no quieres repetir una palabra de la lengua. Nota para el docente: el relato real lo cuenta el portador o la portadora de la tradición, no el cuaderno.",
        "Aprende la primera estudiante. Se apropia el segundo. Pregunta: ¿de qué pueblo es este relato y podemos contarlo? Si no quiero repetir una palabra, escucho con atención.",
        ["distingue aprender y apropiarse", "escribe una pregunta respetuosa", "explica cómo participar escuchando", "no inventa partes del relato"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["confundir aprender con apropiarse", "inventar partes de un relato tradicional"],
        "Valora que reconoce la apropiación y propone escuchar; si inventó o cambió partes de un relato real, conversa sobre por qué pertenece a su comunidad.",
    ),
    reinforce="Dibuja una escena donde alguien escucha con atención a una visita y escribe una frase que diga cómo participa.",
    extend="Explica con tus palabras la diferencia entre reproducir y recrear con un ejemplo de tu curso.",
)

# =================================================================== LS01 clase 2 · situar relato y fuente
FICHA_REL = "Ficha oral A (inventada para practicar): Relato: «El árbol de la plaza». Lo cuenta: el profesor del curso, que lo inventó para practicar. Pueblo: no corresponde, no es un relato de ningún pueblo. Territorio: no corresponde. Permiso: es del curso. Para qué: practicar la escucha."
FICHA_REL_B = "Ficha oral B (inventada): Relato: «Una historia sin datos». Lo cuenta: no se indica. Pueblo: no se indica. Territorio: no se indica. Permiso: no se indica."

L(
    LS1, 2,
    materials="Lápiz y hoja. Las fichas están escritas aquí; son inventadas para practicar y ningún relato de este cuaderno es de un pueblo real.",
    use="Aprenderé a situar un relato: decir quién lo cuenta, de qué pueblo y territorio viene y si hay permiso. Sirve para no mezclar relatos ni atribuirlos al pueblo equivocado.",
    prior=["Sé distinguir aprender y apropiarse.", "Sé que una ficha de procedencia dice fuente y permiso."],
    explain=[
        "Situar un relato es decir de dónde viene: quién lo cuenta, a qué pueblo pertenece, en qué territorio y con qué permiso se comparte. Cada pueblo tiene sus propios relatos y no todos los pueblos originarios cuentan lo mismo. Por eso no digo «los indígenas cuentan» sino «el pueblo tal, según el educador tradicional, cuenta».",
        "El portador o portadora es la persona que conoce y cuida un relato y puede contarlo. No es lo mismo que un libro o una pantalla. Si no hay portador identificado ni permiso, el relato no se puede usar en el cuaderno. En esta clase usamos relatos inventados para practicar, que dicen claramente que no son de ningún pueblo.",
        "Una ficha oral reúne los datos: el relato, quién lo cuenta, el pueblo, el territorio, el permiso y para qué se cuenta. Si un dato dice «no se indica», no lo adivino: me detengo y pregunto. Así evito atribuir un relato al pueblo equivocado y cuido la confianza de quienes lo comparten.",
    ],
    vocab=[("portador o portadora", "persona que conoce y cuida un relato y puede contarlo"), ("situar", "decir de dónde viene algo y con qué permiso"), ("territorio", "lugar donde vive y se cuida una comunidad"), ("ficha oral", "papel con los datos de un relato"), ("atribuir", "decir a quién pertenece algo")],
    worked=[
        W("Leer una ficha oral", FICHA_REL + " ¿De qué pueblo es el relato?", ["Busco la línea «Pueblo».", "Dice: no corresponde, no es un relato de ningún pueblo.", "Es un relato de práctica."], "de ninguno: es un relato inventado de práctica"),
        W("Detenerse ante datos que faltan", FICHA_REL_B + " ¿Puedo usar este relato?", ["Reviso los datos de la ficha.", "Todos dicen «no se indica».", "Me detengo y pregunto."], "no: faltan todos los datos"),
    ],
    mistakes=[
        M("Decir «los pueblos originarios cuentan que…» para un relato de un solo pueblo.", "Cada pueblo tiene sus propios relatos.", "Digo qué pueblo, según qué fuente."),
        M("Usar un relato de una pantalla sin saber quién lo cuenta.", "No hay portador ni permiso identificados.", "Pregunto al educador tradicional si hay un relato autorizado."),
    ],
    R=[
        ex(FICHA_REL + " ¿Quién cuenta el relato?", "el profesor del curso", "La ficha lo dice en la línea «Lo cuenta»."),
        ex("Un portador o portadora, ¿es quien conoce y cuida un relato o quien lo escucha por primera vez?", "quien conoce y cuida un relato", "Es quien puede contarlo."),
        ex("En la ficha B, la línea «Permiso» dice «no se indica». ¿Sé si hay permiso? Sí o No.", "No", "Ese dato falta."),
    ],
    C=[
        ex("Verdadero o falso: todos los pueblos originarios cuentan los mismos relatos.", "Falso", "Cada pueblo tiene sus propios relatos."),
        ex(FICHA_REL + " ¿Para qué se cuenta el relato?", "para practicar la escucha", "La última línea de la ficha lo dice."),
        ex("En la ficha A, ¿el relato es de un pueblo real? Sí o No.", "No", "La ficha dice que no es de ningún pueblo."),
    ],
    A=[
        ex("Dos fichas: A trae relato, quién lo cuenta, pueblo, territorio y permiso. B dice «no se indica» en todas las líneas. ¿Cuál puedo usar para practicar?", "A", "Solo A tiene datos completos."),
        ex("Una niña dice «los indígenas cuentan este relato», pero no dice de qué pueblo es. ¿Qué línea de la ficha oral responde eso: «Pueblo» o «Permiso»?", "Pueblo", "Esa línea dice a qué pueblo pertenece el relato."),
        ex(FICHA_REL_B + " ¿Cuántas líneas dicen «no se indica»?", "4", "Lo cuenta, pueblo, territorio y permiso."),
    ],
    Z=[
        ex("Un niño dice: «Si encontré un relato en una pantalla, ya no necesito saber quién lo cuenta». ¿Tiene razón? Sí o No.", "No", "Sin portador ni permiso no se usa."),
        ex("Un cartel dice: «Relato de un pueblo, contado por un portador de la comunidad, con permiso para el curso». Otro dice: «Relato de por ahí». ¿Cuál situó mejor el relato?", "el primero", "Tiene portador, pueblo y permiso."),
    ],
    D=[
        ex("Ordena para situar un relato: A) leo el permiso. B) leo quién lo cuenta. C) leo de qué pueblo y territorio es. Escribe las letras en el orden de la ficha oral A (lo cuenta, pueblo y territorio, permiso).", "B, C, A", "La ficha va en ese orden."),
        arith("Cada ficha oral tiene 6 líneas. Un curso llenó 4 líneas de una ficha. ¿Cuántas le faltan?", "6-4", "Se restan las líneas llenas de las que tiene la ficha."),
    ],
    context=[ex("En tu escuela alguien trae un libro con un relato y quiere leerlo en voz alta, pero nadie sabe quién lo contó. ¿Pides que lo revise la educadora tradicional o lo lees igual?", "pides que lo revise la educadora tradicional", "Sin fuente conocida no se usa un relato.")],
    selfcheck=[
        ex("¿Qué dato dice de qué pueblo es un relato?", "el pueblo", "Es una línea de la ficha oral."),
        ex("Si un dato dice «no se indica», ¿lo adivino o pregunto?", "pregunto", "No se adivinan datos."),
        ex("¿Todos los pueblos cuentan los mismos relatos? Sí o No.", "No", "Cada pueblo tiene los suyos."),
    ],
    task=T(
        "Lee estas dos fichas inventadas para practicar. " + FICHA_REL + " " + FICHA_REL_B + " En tu cuaderno escribe: 1) cuál ficha permite practicar y por qué, 2) qué datos faltan en la otra, 3) una frase que diga «El relato… lo cuenta… según…» para la ficha A. Termina con una pregunta para el educador o la educadora tradicional sobre cómo se comparte un relato de su pueblo. Nota: los relatos reales los cuenta el portador o portadora, no el cuaderno.",
        "La ficha A, porque trae quién cuenta, pueblo, territorio y permiso. En la B faltan todos. Frase: El relato «El árbol de la plaza» lo cuenta el profesor del curso, según la ficha. Pregunta: ¿cómo se comparte un relato de su pueblo?",
        ["elige la ficha completa y justifica", "nombra los datos que faltan", "escribe una frase con relato, quien cuenta y fuente", "formula una pregunta para el educador/a tradicional"],
        ["tres respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["generalizar a todos los pueblos", "adivinar datos que faltan"],
        "Verifica que no adivinó datos; si generalizó a todos los pueblos, vuelve a leer con él la línea del pueblo.",
    ),
    reinforce="Con la ficha A, señala con el dedo cada línea y di en voz alta qué dato entrega.",
    extend="Inventa una ficha oral de seis líneas para un cuento de tu propia invención y escribe «por preguntar» en lo que no sabes.",
)

# =================================================================== LS01 clase 3 · reconocer palabras significativas
REL_ARBOL = "Relato de práctica «El árbol de la plaza» (inventado, de ningún pueblo): «Había una plaza sin sombra. Los niños de la Escuela Ejemplo plantaron un arbolito. Cada mañana, cuando salía el antü, lo regaban con ko. Con los años, el árbol dio sombra a todo el barrio, y los vecinos dijeron chaltumay a los niños.»"

L(
    LS1, 3,
    materials="Lápiz y hoja. El relato y las fichas están escritos aquí; son inventados para practicar.",
    use="Aprenderé a encontrar en un relato las palabras en lengua indígena o en castellano que tienen valor cultural, a entender su significado con una ficha y a decir por qué importan. Sirve para entender un relato sin quedarme solo con las palabras raras.",
    prior=["Sé situar un relato con su ficha.", "Sé usar una ficha de palabras para saber un significado."],
    explain=[
        "Una palabra significativa es una palabra que tiene un valor especial en el relato o para la cultura que lo cuenta. Puede estar en lengua indígena, como «ko» o «antü», o en castellano, como «sombra», «vecinos» o «cuidar». Para reconocerla pregunto: ¿qué idea importante del relato carga esta palabra?",
        "Para entender su significado sigo tres pasos. Busco la palabra en la ficha. Leo la oración completa para ver cómo se usa. Y me pregunto qué enseña el relato con ella. En el relato de práctica, «ko» es agua según la ficha, y regar el árbol con agua todos los días muestra el cuidado. El significado cultural profundo de las palabras reales lo explica el educador tradicional.",
        "No me quedo solo con las palabras en lengua indígena. A veces una palabra en castellano, como «cuidar» o «compartir», lleva el valor principal. Y no afirmo para qué sirve una palabra en una ceremonia o un rito real: eso lo explican quienes lo practican. Yo explico lo que el relato dice y lo que dice la ficha.",
    ],
    vocab=[("palabra significativa", "palabra con valor especial en un relato o cultura"), ("ficha", "papel que da el significado de una palabra"), ("oración", "grupo de palabras que dice una idea completa"), ("valor", "idea importante, como el cuidado o el respeto"), ("cuidar", "atender algo para que esté bien")],
    worked=[
        W("Encontrar y entender una palabra", REL_ARBOL + " " + FICHA_PAL + " ¿Qué significa «ko» según la ficha y qué hacían los niños con ella?", ["Busco «ko» en la ficha: agua.", "Leo la oración: lo regaban con ko cada mañana.", "Regaban el árbol con agua."], "ko es agua; los niños regaban el árbol con ella"),
        W("Una palabra en castellano con valor", REL_ARBOL + " ¿Qué palabra de castellano describe mejor lo que hacían los niños con el árbol: «cuidar» o «vender»?", ["Leo qué hacían: plantaron el árbol y lo regaban cada mañana.", "Eso muestra que se preocupaban de que el árbol estuviera bien.", "La palabra que lo dice es cuidar."], "cuidar"),
    ],
    mistakes=[
        M("Decir qué significa una palabra sin mirar la ficha.", "Puedo equivocarme.", "Primero busco la palabra en la ficha y después leo la oración."),
        M("Explicar para qué se usa una palabra en una ceremonia real.", "Eso lo explican quienes practican la ceremonia.", "Explico lo que dice el relato y la ficha y pregunto al educador tradicional."),
    ],
    R=[
        ex(REL_ARBOL + " ¿Qué palabra en lengua indígena aparece junto al verbo «salía»?", "antü", "El relato dice «cuando salía el antü»."),
        ex(FICHA_PAL + " Según la ficha, ¿«antü» es sol o luna?", "sol", "La ficha dice que «antü» es sol."),
        ex("En el relato de práctica, ¿con qué regaban el árbol: con ko o con kuyen?", "con ko", "El relato dice «lo regaban con ko»."),
    ],
    C=[
        ex("Verdadero o falso: una palabra significativa solo puede estar en lengua indígena.", "Falso", "También puede estar en castellano."),
        ex(REL_ARBOL + " ¿Qué dijeron los vecinos a los niños al final?", "chaltumay", "Es la palabra que usan al final."),
        ex(FICHA_SAL + " Según la ficha, ¿«chaltumay» es una forma de agradecer o de saludar?", "agradecer", "Quiere decir «gracias»."),
    ],
    A=[
        ex(REL_ARBOL + " Escribe las tres palabras en lengua indígena que aparecen, en el orden del relato.", "antü, ko, chaltumay", "Aparecen en ese orden."),
        ex(REL_ARBOL + " ¿Cuándo regaban el árbol los niños: cada mañana o una sola vez?", "cada mañana", "Lo dice el texto."),
        ex("De las palabras «cuidar», «sombra» y «ruka», ¿cuáles están en castellano? Escribe dos.", "cuidar y sombra", "«Ruka» es una palabra en lengua indígena."),
    ],
    Z=[
        ex("Una niña dice: ««Antü» solo importa si sé para qué sirve en una ceremonia». ¿Es necesario eso para entender el relato de práctica? Sí o No.", "No", "En el relato basta la ficha y la oración."),
        ex("Un niño afirma: «El relato enseña que el árbol cuidado da sombra». ¿Qué parte del relato lo apoya: «Con los años, el árbol dio sombra a todo el barrio» o «Había una plaza sin sombra»?", "«Con los años, el árbol dio sombra a todo el barrio»", "Muestra el resultado del cuidado."),
    ],
    D=[
        ex("En el relato de práctica del árbol, ¿cuántas palabras distintas en lengua indígena aparecen?", "3", "Son antü, ko y chaltumay."),
        ex("Ordena los pasos para entender una palabra: A) leo la oración. B) busco la palabra en la ficha. C) me pregunto qué valor muestra. Escribe las letras.", "B, A, C", "Ficha, oración y valor."),
    ],
    context=[ex("En una reunión escuchas la palabra «mapu» y no sabes qué significa. La ficha de la profesora dice que es tierra. ¿Qué haces: miras la ficha o adivinas con lo que parece?", "miro la ficha", "La ficha es la referencia.")],
    selfcheck=[
        ex("¿Dónde busco el significado de una palabra en lengua indígena: en la ficha o en mi imaginación?", "en la ficha", "La ficha la entrega."),
        ex("¿Una palabra en castellano puede ser significativa? Sí o No.", "Sí", "Puede cargar un valor."),
        ex("¿Quién explica para qué sirve una palabra en una ceremonia real?", "el educador tradicional o la comunidad", "Quien la practica."),
    ],
    task=T(
        "Lee este relato inventado para practicar: " + REL_ARBOL + " " + FICHA_PAL + " En tu cuaderno haz una tabla de tres columnas: palabra, significado según la ficha y qué muestra en el relato. Escribe las tres palabras en lengua indígena y una palabra en castellano con valor, como «cuidar». Termina con una pregunta para el educador o la educadora tradicional.",
        "antü, sol, el momento en que se regaba el árbol. ko, agua, con lo que se cuidó el árbol. chaltumay, gracias, el agradecimiento de los vecinos. cuidar, atender algo, lo que hicieron los niños. Pregunta: ¿qué palabras de su pueblo hablan del cuidado del agua?",
        ["completa la tabla con las tres palabras", "usa la ficha para el significado", "explica qué muestra cada palabra en el relato", "formula una pregunta para el educador/a tradicional"],
        ["tabla de tres columnas", "pregunta escrita o dicha en voz alta"],
        ["inventar significados", "explicar ceremonias reales"],
        "Verifica que cada significado salga de la ficha; si inventó un significado ritual, pide que lo cambie por una pregunta.",
    ),
    reinforce="Lee el relato de práctica en voz alta y levanta la mano cada vez que oigas una palabra en lengua indígena.",
    extend="Escribe un relato inventado de tres oraciones que use dos palabras de la ficha y una palabra en castellano con valor.",
)

# =================================================================== LS01 clase 4 · relacionar saberes sin generalizar
L(
    LS1, 4,
    materials="Lápiz y hoja. Las afirmaciones y los relatos están escritos aquí; son inventados para practicar. Nadie tiene que contar datos de su familia.",
    use="Aprenderé a relacionar un relato con lo que sé y con otros saberes sin decir que todos los pueblos piensan igual. Sirve para valorar la cosmovisión de un pueblo sin hacer generalizaciones.",
    prior=["Sé situar un relato por su fuente.", "Sé reconocer palabras significativas en un relato."],
    explain=[
        "La cosmovisión es la manera en que un pueblo entiende el mundo: la tierra, el agua, el tiempo, las personas y la naturaleza. Cada pueblo tiene la suya, y puede ser distinta aunque comparta ideas con otros. Un relato muestra una parte de esa cosmovisión, pero no toda.",
        "Generalizar es decir que algo vale para todos sin saberlo. Por ejemplo, «todos los pueblos originarios creen lo mismo» es una generalización. Para no generalizar uso frases con límites: «en este relato…», «según el educador tradicional de este pueblo…», «en mi sala, según lo que aprendimos…». Esas frases dicen de dónde sale mi afirmación.",
        "Puedo relacionar el relato con mis saberes. Por ejemplo, el relato de práctica del árbol me recuerda que cuidar algo toma tiempo. Eso lo digo desde mi experiencia, sin atribuirlo a ningún pueblo. Si quiero saber qué piensa un pueblo sobre el agua o la tierra, le pregunto al educador tradicional, que representa esa tradición.",
    ],
    vocab=[("cosmovisión", "manera en que un pueblo entiende el mundo"), ("generalizar", "decir que algo vale para todos sin saberlo"), ("afirmación", "frase que dice que algo es cierto"), ("límite", "frase que dice hasta dónde vale algo"), ("saber", "lo que una persona o comunidad conoce")],
    worked=[
        W("Detectar una generalización", "Afirmaciones: A) «Todos los pueblos originarios cuentan lo mismo del agua». B) «En el relato de práctica del árbol, el agua sirve para cuidar». ¿Cuál generaliza?", ["Busco una frase que valga para todos.", "La A dice «todos los pueblos» y no tiene fuente.", "La B se limita al relato de práctica."], "A"),
        W("Poner un límite", FICHA_SAL + " Afirmación: «Los indígenas dicen chaltumay para agradecer». Reescríbela con un límite usando «según la ficha de la educadora tradicional de la escuela».", ["Mantengo la idea.", "Agrego de dónde sale: la ficha de la educadora tradicional.", "Digo la lengua y quito «los indígenas», que no tiene límite."], "Según la ficha de la educadora tradicional de la escuela, en mapuzugun «chaltumay» quiere decir «gracias»"),
    ],
    mistakes=[
        M("Decir «todos los pueblos creen…» después de escuchar un solo relato.", "Un relato muestra una parte de la cosmovisión de un solo pueblo.", "Uso frases con límites: «en este relato…», «según…»."),
        M("Atribuir a un pueblo una idea que yo asocié desde mi experiencia.", "Estaría hablando por ese pueblo.", "Digo «desde mi experiencia…» y pregunto al educador tradicional."),
    ],
    R=[
        ex("La cosmovisión, ¿es la manera en que un pueblo entiende el mundo o un tipo de comida?", "la manera en que un pueblo entiende el mundo", "Esa es la definición."),
        ex("Generalizar, ¿es decir que algo vale para todos sin saberlo o decir de qué fuente viene?", "decir que algo vale para todos sin saberlo", "Eso es generalizar."),
        ex("«Según el educador tradicional de la escuela…», ¿pone un límite o es una generalización?", "pone un límite", "Dice de dónde sale la afirmación."),
    ],
    C=[
        ex("Verdadero o falso: todos los pueblos originarios entienden el mundo exactamente igual.", "Falso", "Cada pueblo tiene su cosmovisión."),
        ex("¿Cuál frase se limita a un relato? A) «En este relato, el árbol dio sombra». B) «Todos los pueblos cuidan los árboles».", "A", "La A dice «en este relato»."),
        ex("Al decir «desde mi experiencia, cuidar toma tiempo», ¿hablo por un pueblo o por mí?", "por mí", "La frase dice que es mi experiencia."),
    ],
    A=[
        ex("Cuatro frases: 1) «En el relato de práctica, el árbol se cuida cada mañana». 2) «Todos los pueblos nunca pelean». 3) «Según el educador tradicional, su pueblo saluda con «mari mari»». 4) «Los indígenas piensan igual». ¿Cuántas frases generalizan?", "2", "Son la 2 y la 4."),
        ex("Reescribe con límite: «Los indígenas dicen ko al agua». Elige la mejor: A) «Según la ficha de la educadora de mi escuela, en mapuzugun «ko» es agua». B) «Todos los indígenas dicen «ko» al agua».", "A", "La A dice de dónde sale y de qué lengua habla."),
        ex("Un niño escuchó un relato de un pueblo y dice: «Así es todo el mundo indígena». ¿Qué falta: un límite o más volumen?", "un límite", "Debe decir a qué pueblo y relato se refiere."),
    ],
    Z=[
        ex("Una niña dice: «Si escuché un relato bonito, ya conozco la cosmovisión del pueblo». ¿Tiene razón? Sí o No.", "No", "Un relato muestra solo una parte."),
        ex("Dos formas de compartir: A) «En el relato del árbol, el cuidado da sombra al barrio». B) «Para los pueblos originarios, el árbol siempre es sagrado». ¿Cuál tiene fuente clara?", "A", "La A se apoya en el relato de práctica."),
    ],
    D=[
        arith("De 6 afirmaciones que escribió un curso, 2 generalizan y el resto tiene un límite. ¿Cuántas tienen límite?", "6-2", "Se restan las que generalizan."),
        ex("Ordena para evitar generalizar: A) agrego un límite a mi frase. B) pienso de dónde sale mi idea. C) pregunto al educador tradicional si dudo. Escribe las letras.", "B, A, C", "Pienso, pongo un límite y pregunto."),
    ],
    context=[ex("Un compañero dice en clase: «Los indígenas no usan tecnología». Tú sabes que no puedes afirmar eso de todos. ¿Qué respondes: «Esa afirmación generaliza; mejor preguntemos al educador tradicional» o «Tienes razón»?", "«Esa afirmación generaliza; mejor preguntemos al educador tradicional»", "No se habla por todos los pueblos.")],
    selfcheck=[
        ex("En Lengua y Cultura: ¿Qué es generalizar?", "decir que algo vale para todos sin saberlo", "Es afirmar sin límite."),
        ex("¿Qué frase pone un límite: «según el educador tradicional» o «todos los pueblos»?", "«según el educador tradicional»", "Dice la fuente."),
        ex("¿Cada pueblo tiene su propia cosmovisión? Sí o No.", "Sí", "Aunque compartan ideas, son distintas."),
    ],
    task=T(
        "Lee este relato inventado: " + REL_ARBOL + " En tu cuaderno escribe: 1) una idea del relato con límite («En este relato…»), 2) una idea de tu experiencia sobre cuidar algo («Desde mi experiencia…»), 3) una generalización que NO escribirías, con la razón, 4) una pregunta para el educador o la educadora tradicional sobre cómo su pueblo se relaciona con la tierra o el agua. No atribuyas a ningún pueblo lo que escribiste en 1) ni en 2): son de práctica.",
        "En este relato, cuidar el árbol dio sombra al barrio. Desde mi experiencia, cuidar una planta toma tiempo. No escribiría «todos los pueblos cuidan los árboles», porque no lo sé. Pregunta: ¿cómo cuida su pueblo el agua?",
        ["escribe una idea con límite", "separa su experiencia de lo que dice el relato", "reconoce una generalización", "formula una pregunta para el educador/a tradicional"],
        ["cuatro respuestas escritas", "pregunta escrita o dicha en voz alta"],
        ["atribuir ideas a todos los pueblos", "hablar por un pueblo"],
        "Revisa que cada afirmación tenga un límite; si generalizó, ayúdalo a agregar «en este relato» o «según».",
    ),
    reinforce="Escribe dos frases con límite sobre el relato del árbol y subraya la parte que pone el límite.",
    extend="Busca una generalización que hayas oído sobre algún pueblo y escríbela de nuevo con un límite y una pregunta.",
)
