"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR06 (usar recursos tecnológicos disponibles para registrar y narrar situaciones personales o acontecimientos de la
vida comunitaria y describir prácticas culturales, incorporando frases y oraciones en lengua indígena o en castellano,
culturalmente significativas).

Criterio de autoría: todas las fichas, planes, escuelas y personas son inventados solo para practicar y están rotulados
como tales. Las frases son sobre todo en castellano. Las únicas expresiones en lengua indígena son «mari mari» y
«chaltumay» (saludo y gracias en mapuzugun) y los nombres mapuzugun / mapudungun, dos escrituras del nombre de la lengua
mapuche. La palabra «minga» se usa como palabra del castellano de Chile para un trabajo en que varias personas ayudan
juntas; su uso y tradición en cada lugar los enseña la comunidad. No se inventa gramática ni oraciones en lengua
indígena: las oraciones completas las enseña el educador/a tradicional. Los recursos tecnológicos se describen sin marcas
ni enlaces y siempre con una persona adulta; toda actividad tiene alternativa en papel. No se piden datos personales.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LR6 = "LC05 OA LR06"

CONSULT = " Recuerda: la forma tradicional de decir y escribir las palabras y frases de la lengua la enseñan el educador o la educadora tradicional y tu comunidad. Pregúntales antes de dar tu trabajo por terminado. Si usas un aparato, hazlo con una persona adulta; puedes hacerlo todo en papel."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No exigir fotos, voces ni datos de la familia."


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


# ============================================================ LR06 clase 1 · situar: qué voy a registrar y con qué permiso
PLAN = "Plan de registro P (inventado para practicar): Quién registra: el 5.º básico de la Escuela Ejemplo. Qué cuenta: una minga para limpiar la plaza del barrio. Tipo: acontecimiento de la vida comunitaria. Medio: texto escrito en un computador, con una persona adulta. Frase en castellano que se incluye: «Entre todos, mejor» (frase inventada por el curso). Autorización: las personas que ayudaron aceptaron que se cuente la minga, sin nombres ni rostros."

L(
    LR6, 1,
    materials="Lápiz y hoja. Los planes están escritos aquí y son inventados para practicar. Si usas un computador o un teléfono, hazlo con una persona adulta; también puedes hacer todo en papel.",
    use="Aprenderé a decidir, antes de usar un recurso tecnológico, qué situación voy a registrar, de qué tipo es, con qué medio y con qué permiso. Sirve para contar mi vida y la de mi comunidad con cuidado.",
    prior=["Sé ubicar pueblo, territorio y fuente.", "Sé que un dato necesita su fuente y su autorización."],
    explain=[
        "Un recurso tecnológico es un aparato o programa que me ayuda a guardar o a contar algo: un computador con un procesador de texto, una grabadora de voz, una cámara. Antes de usarlo, decido qué voy a registrar. Puede ser una situación personal, lo que me pasó a mí; un acontecimiento de la vida comunitaria, algo que vivió o hizo un grupo; o una práctica cultural, una costumbre que se repite y se transmite.",
        "También decido el medio y las frases. Puedo escribir en castellano e incluir una frase culturalmente significativa, es decir, que tiene valor para mi comunidad o mi familia. Si la frase es de una lengua indígena, la copio tal como me la enseñó mi educador o educadora tradicional. «Minga» es una palabra del castellano de Chile que nombra un trabajo en que varias personas ayudan juntas.",
        "El último paso es la autorización. Cuento solo lo que me corresponde y lo que las personas aceptan que se cuente. No pongo nombres, rostros ni asuntos privados sin permiso. Un buen plan de registro responde: ¿qué cuento?, ¿de qué tipo es?, ¿con qué medio?, ¿qué frase incluyo y de quién es?, ¿quién autoriza?",
    ],
    vocab=[("recurso tecnológico", "aparato o programa que ayuda a guardar o contar algo"), ("situación personal", "algo que me ocurrió a mí"), ("acontecimiento comunitario", "algo que vivió o hizo un grupo o la comunidad"), ("práctica cultural", "costumbre que se repite y se transmite"), ("culturalmente significativa", "que tiene valor para una comunidad o familia")],
    worked=[
        W("Clasificar un registro", PLAN + " ¿De qué tipo es el registro del plan P?", ["Busco la línea «Tipo».", "Dice: acontecimiento de la vida comunitaria.", "Una minga es algo que hizo un grupo."], "es un acontecimiento de la vida comunitaria"),
        W("Completar el permiso", "Plan Q (inventado): Qué cuenta: el primer día de una niña en una escuela nueva. Tipo: situación personal. Medio: dibujo con textos. Autorización: no se indica. ¿Qué falta antes de registrar?", ["Reviso las líneas del plan Q.", "La línea de autorización no dice nada.", "Se debe preguntar a la persona si acepta que se cuente."], "falta la autorización de la persona"),
    ],
    mistakes=[
        M("Contar un problema privado de otra familia porque «es un acontecimiento».", "Un asunto privado no me corresponde y puede dañar a las personas.", "Cuento solo lo que viví y lo que las personas aceptan que se cuente."),
        M("Usar una frase de la comunidad sin decir de dónde la saqué.", "No se sabe quién la enseñó ni si se puede usar.", "Anoto quién me la enseñó y la copio tal cual."),
    ],
    R=[
        ex(PLAN + " ¿Qué cuenta el plan P?", "una minga para limpiar la plaza del barrio", "La línea «Qué cuenta» lo dice."),
        ex(PLAN + " ¿Qué medio usa el plan P?", "texto escrito en un computador, con una persona adulta", "Está en la línea «Medio»."),
        ex("Una situación personal, ¿es algo que me ocurrió a mí o algo que vivió toda la comunidad?", "algo que me ocurrió a mí", "Así se definió situación personal."),
    ],
    C=[
        ex("Clasifica con P (situación personal), C (acontecimiento comunitario) o K (práctica cultural): 1) lo que sentí el primer día en una escuela nueva. 2) la inauguración de la sede de una comunidad. 3) la costumbre de recibir a las visitas con un saludo. Escribe las tres letras.", "1 P, 2 C, 3 K", "La 1 le ocurre a una persona, la 2 la vive un grupo y la 3 es una costumbre que se repite."),
        ex(PLAN + " Verdadero o falso: el plan P incluye nombres y rostros de las personas que ayudaron.", "Falso", "Dice que se cuenta sin nombres ni rostros."),
        ex("«Minga» es una palabra del castellano de Chile. ¿Nombra un trabajo en que varias personas ayudan juntas o un aparato para grabar?", "un trabajo en que varias personas ayudan juntas", "Así se explicó en la clase."),
    ],
    A=[
        ex("Un plan de registro responde cinco preguntas: qué cuento, de qué tipo es, con qué medio, qué frase incluyo y quién autoriza. El curso ya respondió tres. ¿Cuántas faltan por responder?", "2", "Cinco menos tres.", "5-3"),
        ex("Ordena los pasos del plan: A) pedir autorización. B) decidir qué situación contar. C) elegir el medio. D) registrar. Escribe las letras en orden.", "B, C, A, D", "Primero se decide qué contar y con qué medio; luego se pide permiso y al final se registra."),
        ex("Plan R (inventado): Qué cuenta: una reunión vecinal. Tipo: no se indica. Medio: audio. Autorización: sí, sin nombres. ¿Qué dato falta?", "el tipo", "La línea «Tipo» no está completa."),
    ],
    Z=[
        ex("Una niña dice: «Si la frase es en castellano, no necesito decir quién me la enseñó». Si la frase es significativa para mi comunidad, ¿necesita fuente? Sí o No.", "Sí", "La frase significativa viene de personas que se pueden nombrar."),
        ex("Un niño quiere contar el enojo de una persona vecina. ¿Qué es mejor: A) contarlo porque pasó, o B) elegir otra situación que viva él sin exponer a nadie?", "B", "No corresponde contar asuntos privados de otras personas."),
    ],
    D=[
        ex("Dos planes. Plan 1: cuenta una situación personal, sin rostros, con permiso. Plan 2: cuenta la discusión de una familia, con nombres, sin permiso. ¿Cuál puede registrarse: 1 o 2?", "1", "El plan 2 expone a personas sin permiso."),
        arith("En un curso de 28 estudiantes, 9 eligen contar una situación personal y 11 un acontecimiento comunitario. ¿Cuántos eligen contar una práctica cultural?", "28-9-11", "Se restan los otros dos grupos del total."),
    ],
    context=[ex("Quieres registrar con una grabadora, con ayuda de un adulto, cómo se prepara la sala para una visita. Antes de grabar, ¿decides qué cuentas, de qué tipo es y quién autoriza, o grabas y ves después?", "decides qué cuentas, de qué tipo es y quién autoriza", "El plan va antes del registro.")],
    selfcheck=[
        ex("Lo que vivió una comunidad entera, ¿es una situación personal o un acontecimiento comunitario?", "un acontecimiento comunitario", "Lo vivió un grupo."),
        ex("¿Puedo poner el rostro de alguien en mi registro sin su permiso? Sí o No.", "No", "Sin permiso no se expone a nadie."),
        ex("Una costumbre que se repite y se transmite, ¿es una práctica cultural o una situación personal?", "una práctica cultural", "Así se definió."),
    ],
    task=T(
        "Lee estas tres opciones inventadas: A) el día que ayudé a ordenar la sala del curso (situación personal); B) la feria que organizó el barrio (acontecimiento comunitario); C) la costumbre de saludar a la persona que llega a la sala (práctica cultural). Elige una y escribe en tu cuaderno su plan de registro con cinco líneas: qué cuentas, tipo, medio, frase que incluirás con su fuente y quién autoriza. Si no sabes un dato, escribe «por preguntar». Termina con una pregunta para el educador o educadora tradicional.",
        "Qué cuento: la costumbre de saludar a quien llega. Tipo: práctica cultural. Medio: texto en papel. Frase: «mari mari», enseñada por el educador tradicional. Autoriza: por preguntar. Pregunta: ¿cómo se saluda en nuestra comunidad cuando llega una visita?",
        ["completa las cinco líneas", "elige el tipo correcto", "nombra la fuente de la frase", "usa «por preguntar» donde no sabe", "formula una pregunta"],
        ["plan de registro de cinco líneas", "pregunta escrita o dicha en voz alta"],
        ["inventar una autorización", "usar una frase sin fuente"],
        "Comprueba que el tipo coincida con la opción elegida y que ningún dato esté inventado.",
    ),
    reinforce="Relee el plan P y subraya con un color el tipo y con otro la autorización.",
    extend="Escribe un plan de registro para una práctica cultural de tu escuela, con las cinco líneas, y marca como «inventado» lo que no sea real.",
)

# ============================================================ LR06 clase 2 · leer/escuchar con límites declarados: el guion
GUION = "Guion de práctica (inventado): «Soy una estudiante de la Escuela Ejemplo. Voy a contar lo que hicimos en la minga de la plaza. Llegamos a las diez de la mañana y trajimos guantes y bolsas. Entre todos recogimos hojas. Una vecina nos dijo «chaltumay» al despedirnos, que en mapuzugun quiere decir gracias, según nos enseñó la educadora tradicional. No grabé a nadie sin permiso. No sé cómo se hace una minga en otros lugares.»"

L(
    LR6, 2,
    materials="Lápiz y hoja. El guion está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta en voz alta.",
    use="Aprenderé a leer o escuchar un registro y a reconocer lo que cuenta, qué frases usa, de dónde vienen y qué límites declara. Sirve para entender un registro sin agregarle cosas.",
    prior=["Sé separar tipos de registro: personal, comunitario y práctica cultural.", "Sé que una frase de la lengua lleva su fuente."],
    explain=[
        "Un registro narrado tiene una voz que cuenta. Al leerlo o escucharlo busco cuatro cosas: qué situación cuenta, qué datos entrega, qué frases significativas incluye y qué límites declara. Los datos son lo que ocurrió: cuándo, dónde y quiénes. Las frases significativas son las palabras o expresiones que tienen valor para la comunidad.",
        "Cuando una frase viene de una lengua indígena, el registro bien hecho dice quién la enseñó y la traduce solo si la fuente lo hizo. En el guion, «chaltumay» aparece con su fuente: la educadora tradicional. Yo no puedo agregar otros significados ni usos que el guion no dice. Si me interesa saber más, pregunto a quien enseñó la palabra.",
        "Los límites declarados avisan lo que el registro no cubre: «no grabé a nadie sin permiso» y «no sé cómo se hace una minga en otros lugares». Al resumir un registro, copio esos límites. Así quien me escuche sabrá hasta dónde vale lo que cuento y no confundirá una minga de una plaza con todas las mingas del país.",
    ],
    vocab=[("narrar", "contar una situación en orden"), ("dato", "información concreta: cuándo, dónde, quiénes"), ("frase significativa", "expresión que tiene valor para una comunidad"), ("límite declarado", "aviso de lo que el registro no cubre"), ("resumir", "decir lo principal con menos palabras")],
    worked=[
        W("Encontrar una frase con fuente", GUION + " ¿Qué frase significativa aparece y quién la enseñó?", ["Busco una palabra marcada entre comillas.", "Aparece «chaltumay».", "El guion dice que la enseñó la educadora tradicional."], "«chaltumay», enseñada por la educadora tradicional"),
        W("Encontrar los límites", GUION + " ¿Qué límites declara la estudiante?", ["Busco frases que digan lo que no hizo o no sabe.", "Dice que no grabó a nadie sin permiso.", "También dice que no sabe cómo se hace una minga en otros lugares."], "no grabó sin permiso y no sabe cómo es una minga en otros lugares"),
    ],
    mistakes=[
        M("Decir que «chaltumay» es una oración sagrada.", "El guion solo dice que quiere decir gracias.", "Repito solo lo que dice la fuente."),
        M("Resumir el guion sin los límites.", "Parece que la minga de la plaza vale para todas.", "Incluyo los límites en el resumen."),
    ],
    R=[
        ex(GUION + " ¿A qué hora llegaron a la plaza?", "a las diez de la mañana", "El guion lo dice."),
        ex(GUION + " ¿Qué trajeron para la minga?", "guantes y bolsas", "El guion nombra lo que llevaron."),
        ex(GUION + " ¿Qué quiere decir «chaltumay» según el guion?", "gracias", "El guion lo explica."),
    ],
    C=[
        ex(GUION + " ¿Qué hicieron entre todos en la plaza?", "recogieron hojas", "El guion lo cuenta."),
        ex(GUION + " ¿Quién enseñó el significado de «chaltumay» según el guion?", "la educadora tradicional", "El guion cita esa fuente."),
        ex(GUION + " Verdadero o falso: la estudiante grabó a personas sin su permiso.", "Falso", "Dice que no grabó a nadie sin permiso."),
    ],
    A=[
        ex(GUION + " ¿Cuál de estas frases da el dato de cuándo ocurrió algo? A) «Llegamos a las diez de la mañana». B) «Trajimos guantes y bolsas». C) «Entre todos recogimos hojas». Escribe la letra.", "A", "Solo A dice la hora, es decir, cuándo."),
        ex(GUION + " Elige el mejor resumen: A) «En una minga de la plaza, una estudiante contó que recogieron hojas y que no grabó sin permiso; no sabe cómo es en otros lugares». B) «Las mingas del país se hacen con guantes». Escribe la letra.", "A", "A mantiene los límites y los datos."),
        arith("Llegaron 24 personas a la minga y 9 se fueron antes del final. ¿Cuántas personas quedaron hasta el final?", "24-9", "Se restan las que se fueron."),
    ],
    Z=[
        ex(GUION + " Un niño dice que «chaltumay» se usa solo en la plaza. ¿Eso lo dice el guion? Sí o No.", "No", "El guion no dice dónde más se usa."),
        ex(GUION + " Si quieres saber cómo se dice «gracias» en otra lengua indígena, ¿qué haces: A) preguntas al educador o educadora tradicional o B) lo inventas?", "A", "Las palabras de una lengua las enseña quien las conoce."),
    ],
    D=[
        ex(GUION + " ¿Cuál de estas ideas es una interpretación y no un dato del guion? A) recogieron hojas. B) la minga es la mejor forma de cuidar una plaza. C) llegaron a las diez. Escribe la letra.", "B", "El guion no emite esa opinión."),
        ex("Un registro dice: «Fuimos a una minga. Un vecino dijo una palabra en su lengua y la usamos en el video». Para usar esa palabra con cuidado faltan dos cosas. Escríbelas.", "la fuente de la palabra y el permiso para usarla", "No se sabe quién la enseñó ni si autorizó usarla."),
    ],
    context=[ex("Escuchas el registro de un compañero sobre una costumbre de su familia. Al resumirlo, ¿incluyes también los límites que él declaró o los dejas fuera?", "incluyes también los límites", "Los límites dicen hasta dónde vale su relato.")],
    selfcheck=[
        ex("Un dato dice cuándo, dónde o quiénes. ¿Es un dato o una opinión?", "un dato", "Es información concreta."),
        ex("Si una frase indígena no trae fuente en el registro, ¿qué falta?", "la fuente", "Debe decir quién la enseñó."),
        ex("Al resumir, ¿copio los límites declarados? Sí o No.", "Sí", "Avisan hasta dónde vale el registro."),
    ],
    task=T(
        "Lee este guion inventado: «Soy un estudiante de la Escuela Muestra. Cuento cómo recibimos a una visita en la sala. Todos nos pusimos de pie. Dijimos «mari mari», un saludo en mapuzugun que nos enseñó el educador tradicional. No sé cómo se recibe a una visita en otros lugares.» En tu cuaderno escribe: dos datos del guion, la frase con su fuente y los límites. Luego escribe un resumen de dos oraciones que incluya los límites.",
        "Datos: se pusieron de pie; recibieron a una visita en la sala. Frase: «mari mari», enseñada por el educador tradicional. Límite: no sabe cómo se recibe a una visita en otros lugares. Resumen: En la Escuela Muestra recibieron a una visita de pie y con «mari mari», según el educador tradicional. El estudiante no sabe cómo es en otros lugares.",
        ["extrae dos datos", "nombra la frase y su fuente", "copia los límites", "el resumen no agrega ideas"],
        ["lista de datos, frase y límites", "resumen de dos oraciones"],
        ["agregar significados que no están", "resumir sin límites"],
        "Si el resumen agrega ideas nuevas, pídele que señale en el guion dónde aparecen.",
    ),
    reinforce="Relee el guion de la minga y subraya con tres colores: datos, frase con fuente y límites.",
    extend="Escribe un guion inventado de cinco oraciones sobre una situación de tu curso, con una frase en castellano significativa y un límite declarado.",
)

# ============================================================ LR06 clase 3 · relaciones culturales: medio, propósito y oralidad
MEDIOS = "Tabla de medios (inventada para practicar). Texto escrito: sirve para explicar los pasos de una práctica con orden. Audio: sirve para guardar una voz que cuenta de forma oral, si la persona lo autoriza. Fotografía de objetos o manos: sirve para mostrar un objeto o un gesto sin mostrar rostros. Dibujo con rótulos: sirve para explicar un lugar o un proceso y no necesita internet."

L(
    LR6, 3,
    materials="Lápiz y hoja. La tabla está escrita aquí y es inventada para practicar. No necesitas dispositivos.",
    use="Aprenderé a relacionar el medio tecnológico con lo que quiero contar y con el valor de la oralidad y de la comunidad. Sirve para elegir bien cómo registrar y devolver algo a quienes me enseñaron.",
    prior=["Sé armar un plan de registro y reconocer los límites de un guion.", "Sé que la lengua se aprende de quienes la conocen."],
    explain=[
        "No todos los medios sirven para lo mismo. Si quiero explicar los pasos de una práctica, un texto escrito o un dibujo con rótulos los muestra en orden. Si quiero conservar una voz que cuenta de forma oral, un audio sirve, pero solo si la persona acepta. Si quiero mostrar un objeto o un gesto, una fotografía de objetos o de manos evita mostrar rostros.",
        "La oralidad es la forma de transmitir saberes hablando, de persona a persona. Cuando registro una voz, estoy guardando un saber oral que es de quien lo cuenta. Por eso pido su permiso, nombro a la fuente y no cambio sus palabras. El registro no reemplaza a la persona: es una ayuda para recordar y compartir con cuidado.",
        "La reciprocidad aparece al devolver. Si alguien de mi comunidad me contó algo, puedo agradecerle y, si él o ella lo desea, entregarle una copia de lo que escribí. Así el registro vuelve a la comunidad y no queda solo en mis manos. Al elegir un medio pienso en tres cosas: qué quiero contar, a quién protege y qué devuelvo.",
    ],
    vocab=[("oralidad", "forma de transmitir saberes hablando, de persona a persona"), ("medio", "forma de registrar: texto, audio, foto, dibujo"), ("propósito", "para qué hago el registro"), ("devolver", "entregar a la comunidad algo de lo que aprendí"), ("proteger", "cuidar que nadie quede expuesto")],
    worked=[
        W("Elegir un medio según el propósito", MEDIOS + " Quiero mostrar un gesto de tejer con las manos sin mostrar el rostro de nadie. ¿Qué medio uso?", ["Leo qué medio muestra gestos sin rostros.", "La fotografía de objetos o manos lo hace.", "Pido permiso a la persona antes de fotografiar."], "fotografía de manos, con permiso"),
        W("Relacionar oralidad y permiso", "Una persona mayor cuenta una historia de su familia. Una niña quiere grabarla. ¿Qué debe hacer primero?", ["Recuerdo que la voz es parte del saber de quien cuenta.", "Debe pedirle permiso antes de grabar.", "Después nombra la fuente al usar lo grabado."], "pedir permiso a la persona antes de grabar"),
    ],
    mistakes=[
        M("Grabar una voz porque «es más moderno» sin preguntar.", "La voz es de quien la dice.", "Pido permiso y explico para qué la usaré."),
        M("Pensar que el registro reemplaza a la persona que enseña.", "El saber sigue en quien lo transmite.", "Uso el registro como ayuda y vuelvo a consultar a la persona."),
    ],
    R=[
        ex(MEDIOS + " ¿Qué medio sirve para explicar pasos con orden?", "texto escrito", "La tabla lo dice."),
        ex(MEDIOS + " ¿Qué medio no necesita internet y explica un lugar o un proceso?", "dibujo con rótulos", "La tabla lo dice."),
        ex("La oralidad, ¿es transmitir saberes hablando o solo escribirlos?", "transmitir saberes hablando", "Así se definió oralidad."),
    ],
    C=[
        ex(MEDIOS + " ¿Qué medio permite mostrar un objeto sin mostrar rostros?", "fotografía de objetos o manos", "La tabla lo explica."),
        ex(MEDIOS + " Verdadero o falso: el audio se usa sin necesidad de pedir permiso a la persona que habla.", "Falso", "La tabla dice que el audio sirve si la persona lo autoriza."),
        ex("Cuando devuelvo a la comunidad una copia de lo que escribí, ¿practico reciprocidad o competencia?", "reciprocidad", "Devolver con cuidado es reciprocidad."),
    ],
    A=[
        ex("Une cada propósito con un medio: A) guardar una voz que cuenta oralmente, B) mostrar los pasos de una práctica, C) mostrar un gesto sin rostros. Medios: 1) texto escrito, 2) audio con permiso, 3) fotografía de manos. Escribe los tres pares.", "A-2, B-1, C-3", "El audio guarda voz, el texto ordena pasos y la foto de manos evita rostros."),
        arith("Un curso de 30 estudiantes elige medios: 12 eligen texto, 8 eligen dibujo y el resto elige audio. ¿Cuántos eligen audio?", "30-12-8", "Se restan los otros dos medios del total."),
        ex("Una niña quiere explicar cómo llegar a la sede de su comunidad sin usar internet. ¿Qué medio le conviene según la tabla: texto escrito o dibujo con rótulos?", "dibujo con rótulos", "La tabla dice que sirve para explicar un lugar."),
    ],
    Z=[
        ex("Un niño dice: «Si grabo la historia de una persona mayor, ya no necesito volver a preguntarle». ¿Tiene razón? Sí o No.", "No", "El registro no reemplaza a quien enseña."),
        ex("Una vecina cuenta una historia y acepta que se escriba. ¿Qué te parece mejor para devolver: A) preguntarle si quiere una copia o B) quedarte con el texto sin avisar?", "A", "Devolver respeta su saber."),
    ],
    D=[
        ex("Hay que elegir un medio para mostrar cómo se hace una minga con tres pasos, sin exponer rostros y sin internet. ¿Cuál sirve mejor: A) video en un sitio abierto, B) dibujo con rótulos, C) audio que identifica a todos por su nombre? Escribe la letra.", "B", "El dibujo con rótulos ordena los pasos sin rostros ni internet."),
        ex("Tres ideas para devolver: A) agradecer a la persona, B) entregarle una copia si la quiere, C) publicar su voz sin avisar. ¿Cuáles son reciprocidad? Escribe las letras.", "A y B", "C no pide permiso y no cuida."),
    ],
    context=[ex("Vas a registrar cómo una persona de tu comunidad explica un saludo. Antes de elegir el medio, ¿le preguntas qué prefiere compartir o decides tú todo?", "le preguntas qué prefiere compartir", "La persona decide qué se comparte de su saber.")],
    selfcheck=[
        ex("¿Qué medio uso para guardar una voz que cuenta oralmente: audio con permiso o dibujo?", "audio con permiso", "El audio guarda la voz si la persona lo autoriza."),
        ex("¿Devolver una copia a quien me enseñó es reciprocidad? Sí o No.", "Sí", "Es una forma de devolver."),
        ex("¿Una fotografía de manos muestra rostros? Sí o No.", "No", "La foto de manos evita los rostros."),
    ],
    task=T(
        "Lee estos tres propósitos inventados: A) conservar la voz de una persona que cuenta cómo se organizó una minga; B) enseñar los pasos de una costumbre de saludo; C) mostrar un objeto de uso cotidiano sin rostros. Para cada uno, en tu cuaderno escribe qué medio elegirías (texto, audio, fotografía de objetos o manos, o dibujo con rótulos), qué permiso necesitas y qué devolverías a la comunidad. Termina con una pregunta para el educador o educadora tradicional.",
        "A: audio, con permiso de quien cuenta; devolvería una copia si la desea. B: texto escrito con pasos, con fuente del saludo; devolvería una copia al educador. C: fotografía del objeto, con permiso de su dueño; devolvería la foto. Pregunta: ¿qué saberes de nuestra comunidad conviene registrar y cuáles no?",
        ["elige un medio coherente para cada propósito", "nombra el permiso necesario", "propone una forma de devolver", "formula una pregunta"],
        ["tabla de tres propósitos", "pregunta escrita o dicha en voz alta"],
        ["elegir medios que exponen rostros", "olvidar el permiso"],
        "Pide que justifique cada medio con una razón de la tabla.",
    ),
    reinforce="Relee la tabla de medios y pinta cada medio con un color distinto según su propósito.",
    extend="Escribe un párrafo de cuatro oraciones que explique por qué grabar una voz exige permiso y qué puedes devolver a quien te enseñó.",
)

# ============================================================ LR06 clase 4 · construir un registro atribuido
CRED = "Ficha de créditos (inventada para practicar): Título: «Nuestra minga en la plaza». Narra: el 5.º básico de la Escuela Ejemplo. Fecha: un sábado de octubre. Fuente de la frase «chaltumay»: la educadora tradicional de la escuela. Medio: texto escrito con una persona adulta. Autorización: sin nombres ni rostros. Límite: cuenta solo esta minga."

L(
    LR6, 4,
    materials="Lápiz y hoja. La ficha está escrita aquí y es inventada para practicar. Si usas un aparato, hazlo con una persona adulta.",
    use="Aprenderé a escribir un registro narrado con sus créditos: quién cuenta, de dónde vienen las frases, con qué permiso y hasta dónde vale. Sirve para que mi registro sea claro y respetuoso.",
    prior=["Sé elegir un medio según el propósito.", "Sé reconocer fuente y límites en un guion."],
    explain=[
        "Un registro narrado tiene dos partes: la narración y los créditos. La narración cuenta la situación en orden: qué pasó, cuándo y dónde. Para eso uso oraciones claras y en el orden en que ocurrió. Puedo incluir una frase significativa en castellano o una palabra de una lengua indígena que me enseñaron.",
        "Los créditos son una ficha corta que va junto a la narración. Dice el título, quién narra, la fecha, la fuente de cada frase significativa, el medio, la autorización y el límite. Los créditos permiten comprobar de dónde salió cada dato y proteger a las personas. Sin créditos, un registro queda incompleto aunque esté bien escrito.",
        "Al escribir una frase de una lengua indígena, la copio tal cual me la enseñaron y no cambio su significado. Si quiero explicarla, solo uso la explicación que dio mi fuente. Y si el registro incluye mis ideas, las marco como «yo pienso». Al final reviso: ¿están los siete datos de los créditos?",
    ],
    vocab=[("narración", "la parte que cuenta lo que pasó en orden"), ("créditos", "ficha con título, quién narra, fuentes y permisos"), ("fecha", "día en que ocurrió o se registró"), ("fuente de la frase", "persona que enseñó la frase o palabra"), ("revisar", "mirar de nuevo para corregir")],
    worked=[
        W("Leer los créditos", CRED + " ¿Quién narra y de quién es la fuente de «chaltumay»?", ["Busco «Narra»: el 5.º básico de la Escuela Ejemplo.", "Busco la fuente de la frase: la educadora tradicional.", "Uno ambos datos."], "narra el 5.º básico de la Escuela Ejemplo y la fuente de «chaltumay» es la educadora tradicional"),
        W("Completar los créditos", "Créditos incompletos (inventados): Título: «Mi primer día». Narra: una estudiante. Medio: dibujo con textos. Autorización: sin rostros. El registro incluye una frase significativa. ¿Qué tres datos faltan de los siete?", ["Los siete datos son título, narra, fecha, fuente de la frase, medio, autorización y límite.", "Aparecen cuatro: título, narra, medio y autorización.", "Faltan los otros tres: fecha, fuente de la frase y límite."], "faltan la fecha, la fuente de la frase y el límite"),
    ],
    mistakes=[
        M("Escribir la narración y olvidar los créditos.", "Nadie sabe quién narra ni con qué permiso.", "Agrego una ficha de créditos con los siete datos."),
        M("Cambiar una palabra de la lengua para que «se vea mejor».", "Cambia cómo se escribe o se dice lo que enseñó la fuente.", "Copio la palabra tal cual me la enseñaron."),
    ],
    R=[
        ex(CRED + " ¿Cuál es el título del registro?", "Nuestra minga en la plaza", "Está en la línea «Título»."),
        ex(CRED + " ¿Qué medio se usó?", "texto escrito con una persona adulta", "Está en la línea «Medio»."),
        ex("Los créditos, ¿son una ficha con título, quién narra y fuentes o son la parte que cuenta lo que pasó?", "una ficha con título, quién narra y fuentes", "La parte que cuenta es la narración."),
    ],
    C=[
        ex(CRED + " ¿Qué límite declara la ficha?", "cuenta solo esta minga", "Está en la línea «Límite»."),
        ex(CRED + " Verdadero o falso: los créditos indican que aparecen rostros.", "Falso", "Dicen sin nombres ni rostros."),
        ex("La narración de un registro, ¿cuenta lo que pasó en orden o enumera las fuentes?", "cuenta lo que pasó en orden", "La narración relata la situación."),
    ],
    A=[
        ex("Los créditos tienen siete datos: título, narra, fecha, fuente de la frase, medio, autorización y límite. Un registro tiene cuatro. ¿Cuántos faltan?", "3", "Siete menos cuatro.", "7-4"),
        ex("Ordena la narración de una minga: A) recogimos hojas entre todos. B) llegamos a la plaza. C) nos despedimos con un «gracias». Escribe las letras en orden.", "B, A, C", "Primero se llega, luego se trabaja y al final se despide."),
        ex(CRED + " Si el curso quiere incluir además la palabra «mari mari», ¿qué dato de los créditos debe agregar: la fuente de esa palabra o la fecha?", "la fuente de esa palabra", "Cada frase significativa lleva su fuente."),
    ],
    Z=[
        ex("La educadora tradicional escribió «chaltumay». Un niño quiere escribirlo a su manera porque cree que así se ve mejor. ¿Es correcto cambiarlo? Sí o No.", "No", "Se copia tal cual la enseñó la fuente."),
        ex("Una niña escribe en su registro: «Esa costumbre sirve para que todos sean felices». ¿Cómo debe marcar esa idea: con «yo pienso» o como si la hubiera dicho la fuente?", "con «yo pienso»", "Es una idea propia."),
    ],
    D=[
        ex("Dos registros cuentan la misma minga. El registro 1 tiene créditos con fuente y límite. El registro 2 no tiene créditos. ¿Cuál es más claro sobre su procedencia: 1 o 2?", "1", "Los créditos permiten comprobar de dónde sale cada dato."),
        ex("Un registro tiene estos créditos: «Narra: una estudiante. Fecha: un sábado. Medio: texto. Fuente de la frase: una vecina». De estos tres datos, ¿cuáles faltan: título, autorización, límite?", "los tres", "No aparece ninguno de los tres en los créditos."),
    ],
    context=[ex("Terminaste de escribir un registro sobre una costumbre de tu curso. Antes de mostrarlo, ¿revisas que estén todos los créditos o lo muestras así?", "revisas que estén todos los créditos", "Los créditos completan el registro.")],
    selfcheck=[
        ex("¿Cuántos datos tienen los créditos de esta clase: 5 o 7?", "7", "Título, narra, fecha, fuente, medio, autorización y límite."),
        ex("Si una frase indígena no tiene fuente en los créditos, ¿el registro está completo? Sí o No.", "No", "Falta la fuente de la frase."),
        ex("Mis ideas propias en un registro, ¿las marco con «yo pienso»? Sí o No.", "Sí", "Así no se confunden con lo que dijo la fuente."),
    ],
    task=T(
        "Lee esta situación inventada: «En la Escuela Muestra, el curso ayudó a ordenar la biblioteca el viernes. Cada estudiante llevó una caja de libros. Al final, una profesora dijo «gracias» y el educador tradicional enseñó que se puede decir «chaltumay» en mapuzugun.» En tu cuaderno escribe un registro de cuatro oraciones en orden y debajo la ficha de créditos con los siete datos. Si no sabes uno, escribe «por preguntar».",
        "Narración: El viernes el curso ayudó a ordenar la biblioteca. Cada estudiante llevó una caja de libros. Al final, una profesora dijo «gracias». El educador tradicional enseñó que también se dice «chaltumay» en mapuzugun. Créditos: Título: Ordenamos la biblioteca. Narra: el curso. Fecha: un viernes. Fuente de la frase: el educador tradicional. Medio: texto. Autorización: por preguntar. Límite: cuenta solo esta actividad.",
        ["narración en orden", "siete datos de créditos", "fuente de la frase", "usa «por preguntar» donde no sabe"],
        ["registro de cuatro oraciones", "ficha de créditos"],
        ["omitir créditos", "cambiar cómo se escribe la palabra"],
        "Revisa dato por dato los siete créditos y pide que corrija solo lo que falte.",
    ),
    reinforce="Copia los créditos de la ficha y numera cada uno de los siete datos.",
    extend="Escribe créditos para un registro sobre otra actividad de tu curso, incluyendo una frase en castellano significativa con su fuente.",
)

# ============================================================ LR06 clase 5 · contrastar sin jerarquizar
DOS = "Dos registros inventados sobre la misma costumbre de recibir a una visita. Registro 1 (Comunidad Ejemplo): se recibe a la visita en la puerta de la sala y se ofrece un lugar para sentarse; luego se la saluda con «mari mari». Registro 2 (Comunidad Muestra): se recibe a la visita en la sala ya sentados, y una persona del curso la saluda en nombre de todos. Ambos declaran que cuentan solo lo que hace su comunidad."

L(
    LR6, 5,
    materials="Lápiz y hoja. Los registros están escritos aquí y son inventados para practicar. No necesitas dispositivos.",
    use="Aprenderé a comparar dos registros de una misma práctica cultural, de comunidades o medios distintos, sin decir que uno es mejor o más verdadero. Sirve para respetar la diversidad de las comunidades.",
    prior=["Sé armar un registro con créditos.", "Sé que cada comunidad cuenta solo lo suyo."],
    explain=[
        "Dos comunidades pueden hacer una misma práctica de manera distinta. Eso se llama variante: es una forma distinta de hacer o decir lo mismo. Las variantes no se ordenan en mejores y peores. Cada una responde a su territorio, a su historia y a las personas que la viven. Por eso, al contrastar, comparo sin jerarquizar.",
        "Para comparar uso una tabla con tres columnas: lo que es igual, lo que es distinto y qué fuente respalda cada cosa. Por ejemplo, ambos registros cuentan que se saluda a la visita, pero uno la recibe en la puerta y el otro sentados. No digo «el registro 1 es correcto». Digo «en la Comunidad Ejemplo se hace así y en la Comunidad Muestra se hace así».",
        "También hay variantes en la escritura de una lengua. El nombre de la lengua mapuche se escribe de dos maneras muy usadas: mapuzugun y mapudungun. Ninguna es una falta de ortografía de la otra. Cuando no sé cuál usa mi comunidad, pregunto al educador o educadora tradicional y respeto la forma que ellos indiquen.",
    ],
    vocab=[("variante", "forma distinta de hacer o decir lo mismo"), ("contrastar", "comparar para ver parecidos y diferencias"), ("jerarquizar", "ordenar en mejor y peor"), ("mapuzugun / mapudungun", "dos escrituras usadas para el nombre de la lengua mapuche"), ("respaldar", "apoyar un dato con su fuente")],
    worked=[
        W("Buscar lo igual y lo distinto", DOS + " ¿Qué tienen igual los dos registros?", ["Leo qué hace cada comunidad.", "Ambos saludan a la visita.", "Ambos declaran que cuentan solo lo suyo."], "ambos saludan a la visita y declaran que cuentan solo lo suyo"),
        W("Comparar sin jerarquizar", DOS + " Un niño dice: «El registro 2 está mal porque no usa mari mari». ¿Cómo lo corriges?", ["El registro 2 no dice que use esa palabra, pero tampoco dice que esté mal.", "Es otra variante de una comunidad distinta.", "Digo que en la Comunidad Muestra se saluda de otra manera."], "es otra variante; no se juzga como mala, solo se describe"),
    ],
    mistakes=[
        M("Decir que una comunidad lo hace bien y la otra mal.", "Cada comunidad tiene su forma y su razón.", "Describo cada forma sin ordenarlas en mejor o peor."),
        M("Pensar que mapudungun es una falta de ortografía de mapuzugun.", "Son dos escrituras usadas del nombre de la lengua.", "Uso la que indique mi educador o educadora tradicional."),
    ],
    R=[
        ex(DOS + " ¿Qué comunidad recibe a la visita en la puerta de la sala?", "la Comunidad Ejemplo", "Lo dice el registro 1."),
        ex(DOS + " ¿Qué comunidad saluda a la visita en nombre de todos con una persona del curso?", "la Comunidad Muestra", "Lo dice el registro 2."),
        ex("Una variante, ¿es una forma distinta de hacer o decir lo mismo o un error de escritura?", "una forma distinta de hacer o decir lo mismo", "Así se definió variante."),
    ],
    C=[
        ex(DOS + " Verdadero o falso: según los registros, las dos comunidades reciben a la visita exactamente igual.", "Falso", "Una la recibe en la puerta y la otra en la sala sentados."),
        ex("¿Cuáles son dos escrituras usadas del nombre de la lengua mapuche: mapuzugun y mapudungun, o mapuzugun y castellano?", "mapuzugun y mapudungun", "Son las dos formas vistas en la clase."),
        ex(DOS + " ¿Qué palabra de saludo menciona el registro 1?", "mari mari", "Se nombra en el registro 1."),
    ],
    A=[
        ex(DOS + " Haz una tabla mental: en la columna «igual» pones que saludan a la visita. ¿En qué columna pones que una la recibe en la puerta y otra sentados: igual o distinto?", "distinto", "Es una diferencia entre ellas."),
        ex("Clasifica con I (igual) o D (distinto): 1) ambos registros declaran que cuentan solo lo suyo. 2) uno recibe en la puerta y el otro sentados. 3) ambos tienen un saludo. Escribe las tres letras.", "1 I, 2 D, 3 I", "Las 1 y 3 coinciden y la 2 difiere."),
        arith("En una tabla de comparación hay 9 filas. 4 filas son «igual». ¿Cuántas filas son «distinto»?", "9-4", "Se restan las iguales del total."),
    ],
    Z=[
        ex("Una niña dice: «El registro 1 es el verdadero porque es el más largo». ¿Es un buen argumento? Sí o No.", "No", "El largo no mide cuál es verdadero."),
        ex("Dos estudiantes escriben mapuzugun y mapudungun. ¿Qué es mejor: A) decirles que uno se equivoca o B) preguntar al educador tradicional qué forma usa la comunidad?", "B", "Ambas formas existen y la comunidad decide."),
    ],
    D=[
        ex(DOS + " ¿Cuál de estas frases compara sin jerarquizar? A) «En la Comunidad Ejemplo se recibe en la puerta y en la Comunidad Muestra se recibe sentados». B) «La Comunidad Ejemplo recibe mejor». Escribe la letra.", "A", "A solo describe cada forma."),
        ex("Un curso compara un registro en audio y uno en texto de la misma costumbre. ¿Qué es lo que no se puede decir: A) «el audio guarda la voz y el texto ordena pasos» o B) «el audio es mejor que el texto siempre»?", "B", "No se jerarquizan los medios en forma general."),
    ],
    context=[ex("Tu curso recibe dos relatos distintos de una misma costumbre contados por dos familias de una comunidad. ¿Los guardas ambos con su fuente o eliges uno y borras el otro?", "los guardas ambos con su fuente", "Cada versión tiene valor y fuente.")],
    selfcheck=[
        ex("Al comparar, ¿digo cuál es mejor o describo lo igual y lo distinto?", "describo lo igual y lo distinto", "Se compara sin jerarquizar."),
        ex("¿Mapudungun es una falta de ortografía de mapuzugun? Sí o No.", "No", "Son dos escrituras usadas."),
        ex("Una variante, ¿es una forma distinta de hacer lo mismo? Sí o No.", "Sí", "Eso significa variante."),
    ],
    task=T(
        "Lee estos dos registros inventados sobre despedir a una visita. Registro A: la Comunidad Ejemplo despide a la visita en la puerta con un «chaltumay». Registro B: la Comunidad Muestra despide a la visita con un «gracias por venir» dicho por todo el curso. En tu cuaderno haz una tabla con tres columnas: igual, distinto y qué fuente respalda cada cosa. Después escribe dos frases que comparen sin decir cuál es mejor. Termina con una pregunta para el educador o educadora tradicional.",
        "Igual: ambas comunidades despiden a la visita y agradecen. Distinto: A usa «chaltumay» y B usa «gracias por venir»; A despide en la puerta y B lo hace todo el curso. Fuente: cada registro. Frases: En la Comunidad Ejemplo se despide en la puerta con «chaltumay». En la Comunidad Muestra se despide con «gracias por venir» dicho por todo el curso. Pregunta: ¿cómo se despide a una visita en nuestra comunidad?",
        ["identifica lo igual y lo distinto", "nombra la fuente", "compara sin jerarquizar", "formula una pregunta"],
        ["tabla de tres columnas", "dos frases comparativas"],
        ["decir cuál comunidad lo hace mejor", "mezclar las fuentes"],
        "Si aparece un juicio de valor, pide que lo reemplace por una descripción de cada forma.",
    ),
    reinforce="Relee los dos registros y subraya con un color lo igual y con otro lo distinto.",
    extend="Escribe una frase que explique por qué dos comunidades pueden hacer lo mismo de maneras distintas y por qué eso no es un error.",
)

# ============================================================ LR06 clase 6 · comunicar y revisar con validación pertinente
LISTA = "Lista de revisión (inventada para practicar): 1) ¿Dice quién narra? 2) ¿Cada frase de la lengua tiene su fuente y está copiada tal cual? 3) ¿Hay autorización de las personas? 4) ¿No aparecen rostros ni nombres sin permiso? 5) ¿Declara su límite? 6) ¿Lo vio el educador o educadora tradicional?"

L(
    LR6, 6,
    materials="Lápiz y hoja. La lista y los registros están escritos aquí y son inventados para practicar. No necesitas dispositivos.",
    use="Aprenderé a revisar mi registro con una lista y a pedir la validación del educador o educadora tradicional antes de comunicarlo a otras personas. Sirve para compartir con respeto y corregir a tiempo.",
    prior=["Sé armar un registro con créditos.", "Sé comparar variantes sin jerarquizar."],
    explain=[
        "Comunicar es mostrar mi registro a otras personas, como el curso o las familias. Antes de comunicarlo, lo reviso con una lista de preguntas: quién narra, si cada frase tiene fuente, si hay autorización, si no aparecen rostros ni nombres sin permiso, si declara su límite y si lo vio quien debe validarlo. Una respuesta «no» significa que todavía no está listo.",
        "La validación pertinente es la revisión que hace la persona que corresponde. Para un saludo, una palabra o una costumbre de la lengua, esa persona es el educador o la educadora tradicional o alguien de la comunidad. Yo no puedo validar mi propio trabajo en lo cultural. Si esa persona dice «esto no se comparte» o «cámbialo», lo cambio o no lo comparto, aunque yo piense distinto.",
        "Revisar también es mejorar. Si falta una fuente, la agrego. Si hay un rostro, lo saco. Si hay una frase mal copiada, la corrijo con el modelo original. Cuando todo está en orden, comunico mi registro y agradezco a quienes me enseñaron. Así mi trabajo es útil, claro y respetuoso.",
    ],
    vocab=[("comunicar", "mostrar mi trabajo a otras personas"), ("validación", "revisión de la persona que corresponde"), ("pertinente", "que es adecuado para el caso"), ("lista de revisión", "preguntas para comprobar que el registro está completo"), ("corregir", "cambiar lo que está mal")],
    worked=[
        W("Usar la lista", LISTA + " Un registro cumple 1, 2, 3, 4 y 5, pero nadie lo vio. ¿Está listo para comunicar?", ["Reviso la pregunta 6: ¿lo vio el educador o la educadora tradicional?", "La respuesta es no.", "Todavía no está listo."], "no: falta la validación del educador o educadora tradicional"),
        W("Responder a una validación", "El educador tradicional dice que una frase del registro no se debe compartir. La autora cree que sí se puede. ¿Qué hace?", ["La validación pertinente es la del educador.", "La autora no valida su propio trabajo en lo cultural.", "Retira o cambia la frase."], "retira o cambia la frase y no la comparte"),
    ],
    mistakes=[
        M("Comunicar el registro sin que lo vea el educador o educadora tradicional.", "Podría contener errores o cosas que no se comparten.", "Pido la validación antes de comunicar."),
        M("Pensar que una respuesta «no» en la lista no importa.", "Cada «no» muestra algo por corregir.", "Corrijo cada punto y reviso de nuevo."),
    ],
    R=[
        ex(LISTA + " ¿Cuántas preguntas tiene la lista?", "6", "Se cuentan seis preguntas.", "3+3"),
        ex(LISTA + " ¿Cuál es la pregunta 6?", "¿Lo vio el educador o educadora tradicional?", "Está en la lista."),
        ex("Comunicar, ¿es mostrar mi trabajo a otras personas o guardarlo para siempre?", "mostrar mi trabajo a otras personas", "Así se definió comunicar."),
    ],
    C=[
        ex(LISTA + " ¿Qué pregunta de la lista revisa los créditos de las frases de la lengua?", "la 2", "La 2 habla de la fuente de cada frase."),
        ex("Verdadero o falso: yo puedo validar solo mi trabajo cuando trata de una costumbre de la lengua.", "Falso", "La validación la hace quien corresponde."),
        ex("La validación pertinente de un saludo de la lengua indígena, ¿la hace el educador o educadora tradicional o un buscador de internet?", "el educador o educadora tradicional", "Es la persona que conoce la lengua."),
    ],
    A=[
        ex("Un registro responde «sí» a 4 de las 6 preguntas de la lista. ¿Cuántas faltan por cumplir?", "2", "Seis menos cuatro.", "6-4"),
        ex("Ordena los pasos finales: A) comunico y agradezco. B) corrijo lo que falta. C) reviso con la lista. D) pido la validación de la versión ya corregida. Escribe las letras en orden.", "C, B, D, A", "Reviso, corrijo, valido y comunico."),
        ex(LISTA + " Un registro muestra el rostro de una persona sin permiso. ¿Qué pregunta de la lista no se cumple: la 4 o la 5?", "la 4", "La 4 pregunta por rostros o nombres sin permiso."),
    ],
    Z=[
        ex("Una niña dice: «Como mi registro quedó lindo, no necesito mostrárselo al educador». ¿Tiene razón? Sí o No.", "No", "La validación no depende de que quede lindo."),
        ex("El educador dice que cambies una frase. ¿Qué es mejor: A) discutirlo y compartirla igual o B) cambiarla o retirarla?", "B", "Se respeta la validación pertinente."),
    ],
    D=[
        ex("Dos registros. Registro 1: cumple las seis preguntas. Registro 2: cumple cinco, pero nadie lo validó. ¿Cuál puede comunicarse: 1 o 2?", "1", "El 2 no cumple la pregunta 6."),
        ex(LISTA + " Un registro olvidó el límite y la fuente de una frase. ¿Qué preguntas no se cumplen? Escribe los dos números.", "2 y 5", "La 2 pide fuente y la 5 pide límite."),
    ],
    context=[ex("Terminaste un registro sobre una costumbre y estás por mostrarlo en la reunión de familias. ¿Primero lo muestras o primero lo revisas con la lista y lo ve el educador o educadora tradicional?", "primero lo revisas con la lista y lo ve el educador o educadora tradicional", "La revisión y validación van antes de comunicar.")],
    selfcheck=[
        ex("Si una pregunta de la lista dice «no», ¿el registro está listo? Sí o No.", "No", "Hay algo por corregir."),
        ex("¿Quién valida un saludo en lengua indígena: el educador tradicional o un compañero?", "el educador tradicional", "Es quien corresponde."),
        ex("Después de comunicar, ¿agradezco a quienes me enseñaron? Sí o No.", "Sí", "Es parte de la reciprocidad."),
    ],
    task=T(
        "Lee este registro inventado y revísalo con la lista: «Narra: un curso de la Escuela Muestra. Cuenta una minga en la plaza. Incluye «mari mari», sin decir quién lo enseñó. Aparece el rostro de un niño sin que su familia lo haya autorizado. No declara límite. Ni el educador ni la educadora tradicional lo vieron.» En tu cuaderno escribe qué preguntas de la lista no se cumplen y qué cambiarías en cada caso. Termina con una pregunta para el educador o educadora tradicional.",
        "No se cumplen: 2 (falta la fuente de «mari mari»), 3 y 4 (rostro sin autorización), 5 (falta el límite) y 6 (no lo vio el educador). Cambios: agregar la fuente, sacar el rostro o pedir el permiso, agregar el límite y pedir la validación. Pregunta: ¿puede revisar este registro antes de que lo compartamos?",
        ["detecta las preguntas no cumplidas", "propone un cambio para cada una", "incluye la validación", "formula una pregunta"],
        ["lista de problemas y cambios", "pregunta escrita o dicha en voz alta"],
        ["dejar pasar el rostro", "no pedir validación"],
        "Pide que numere cada problema con el número de la pregunta de la lista.",
    ),
    reinforce="Copia la lista de revisión y marca con un visto bueno cada pregunta que ya cumple tu último trabajo.",
    extend="Escribe una lista de revisión propia con cinco preguntas para un registro de tu curso, y explica por qué la última pregunta es sobre la validación.",
)
