"""Cuaderno del estudiante, 1.º medio Orientación: OA 05 (relaciones constructivas presenciales y digitales) y OA 06 (resolución de conflictos en un marco de derechos)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA5, OA6 = "OR1M OA 05", "OR1M OA 06"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. La conversación del grupo «Curso 1.º A», escrita en los ejercicios, es inventada y no tiene cuentas ni datos reales.",
    "Aprenderé a examinar una conversación digital y a reconocer cuándo una relación en línea es constructiva y cuándo daña. Sirve para cuidar la dignidad de todos en el curso, también en las redes.",
    ["Sé que la dignidad y el respeto valen igual en persona y en línea (8.º básico).", "Sé que un mensaje puede leerse de formas distintas."],
    [
        "Una relación constructiva es aquella en que las personas se tratan con respeto, se escuchan y se apoyan. Lo mismo vale cuando se conversa en persona o en redes sociales. Se basa en cuatro principios: igualdad (todos valen lo mismo), dignidad (nadie merece humillación), inclusión (todos caben en el grupo) y no discriminación (nadie es tratado peor por su género, origen, apariencia, creencias u otra característica).",
        "En línea hay rasgos especiales. Los mensajes quedan escritos, se pueden copiar y reenviar, llegan a muchas personas rápido y no muestran el tono de voz ni la cara. Por eso un chiste puede doler más de lo que se piensa. Para examinar una conversación, separa los hechos (qué se escribió, quién, cuántas veces), las emociones posibles de las personas y los derechos que se afectan.",
        "Algunas conductas construyen: pedir permiso antes de publicar una foto, felicitar un logro, invitar a quien está solo, corregir con respeto. Otras dañan: burlas repetidas, memes sobre alguien, excluir de un grupo, difundir rumores o capturas privadas. Esas conductas, cuando se repiten para hacer daño, forman el ciberacoso.",
    ],
    [("relación constructiva", "relación en que las personas se respetan, se escuchan y se apoyan"), ("inclusión", "que todas las personas puedan participar en el grupo"), ("no discriminación", "no tratar peor a alguien por una característica personal"), ("red social", "sitio o aplicación para comunicarse y compartir contenido"), ("ciberacoso", "daño repetido hacia alguien por medios digitales")],
    [
        W("Conducta que construye o daña", "En el chat, Julia escribe: «Mañana hay prueba de historia, ¿estudiamos juntas a las 17:00 en la biblioteca?». ¿Construye o daña?", ["Invita a estudiar.", "No humilla a nadie."], "Construye"),
        W("Hecho y emoción", "En el chat se publicó 3 veces un meme sobre Bruno. Bruno dejó de escribir. ¿Cuál es el hecho y cuál es la emoción posible?", ["El meme publicado 3 veces se puede contar: hecho.", "Bruno puede sentirse humillado: emoción."], "Hecho: 3 memes; emoción: humillación"),
    ],
    [
        M("Pensar que, como es un chat, no tiene consecuencias.", "Se cree que lo digital no es real.", "Los mensajes dañan igual y quedan escritos."),
        M("Creer que un chiste es inocente si el grupo se ríe.", "Se mide por las risas y no por cómo se siente la persona.", "Pregúntate cómo lo vive la persona de la que hablas."),
    ],
    R=[
        ex("Invitar a todo el curso a un trabajo grupal, ¿es una conducta de inclusión o de exclusión?", "De inclusión", "Todos pueden participar."),
        ex("Burlarse de la apariencia de alguien, ¿es respeto o discriminación?", "Discriminación", "Trata peor a alguien por una característica."),
        ex("Escribes un comentario burlón en un chat y lo borras a los dos minutos. ¿Qué puede haber pasado en ese tiempo? A) Otras personas pudieron copiarlo o reenviarlo B) Dejó de existir para todos", "A", "Los mensajes en línea se copian y reenvían rápido."),
    ],
    U=[
        ex("¿Cuál es una conducta constructiva? A) Pedir permiso antes de publicar una foto de alguien B) Reenviar un meme sobre un compañero.", "A", "Respeta la dignidad y la privacidad."),
        ex("¿Qué principio violan las burlas por el origen de una persona? A) La no discriminación B) La puntualidad.", "A", "Trata peor a alguien por su origen."),
        ex("¿Por qué un chiste puede doler más en un chat? A) Porque queda escrito y no se ve la cara de quien lo lee B) Porque se escribe más rápido.", "A", "Falta el tono de voz y los mensajes se difunden."),
    ],
    A=[
        ex("Clasifica con C (construye) o D (daña): 1) felicitar a una compañera por su logro; 2) crear un sticker burlesco de otro; 3) invitar a quien está solo a un grupo. Escribe las letras en orden.", "C, D, C", "La 1 y la 3 incluyen y valoran; la 2 humilla."),
        arith("En un grupo, 24 mensajes son sobre el trabajo, 9 son bromas inofensivas y 6 son burlas a una compañera. ¿Cuántos mensajes hay en total?", "24+9+6", "Se suman los mensajes de los tres tipos."),
        ex("Un chat excluye a Lucas porque «no tiene el último celular». ¿Qué principio se afecta? A) La inclusión y la no discriminación B) La velocidad de internet.", "A", "Lo excluyen por una característica personal."),
    ],
    Z=[
        ex("¿Por qué el ciberacoso suele dañar más que una burla aislada?", "Porque se repite, llega a muchos y queda escrito", "La repetición y la difusión aumentan el daño."),
        ex("Un compañero dice: «Es solo un meme». ¿Qué falta considerar? A) Cómo lo vive la persona de la que se habla B) Cuántos likes tiene.", "A", "El efecto en la persona importa más que la intención."),
    ],
    D=[
        arith("En un chat inventado de 32 personas, 8 reaccionan con burlas a un mensaje ofensivo y 3 piden respeto. ¿Cuántas personas no reaccionan?", "32-8-3", "Al total se le restan quienes reaccionan con burlas y quienes piden respeto."),
        arith("Una compañera recibió 5 mensajes ofensivos por día durante 4 días. ¿Cuántos mensajes recibió?", "5*4", "Se multiplican mensajes por días."),
    ],
    context=[ex("En el curso circulan memes sobre cómo habla Nicolás. Una compañera propone un chat de apoyo para quien lo necesite. ¿Qué efecto tiene? A) Construye una relación más inclusiva B) Evita que Nicolás se entere de los memes.", "A", "Ofrece apoyo en vez de burla.")],
    selfcheck=[ex("En Orientación: ¿la dignidad vale también en las redes sociales?", "Sí", "Los derechos no desaparecen en línea."), ex("¿Excluir a alguien por su apariencia es discriminación?", "Sí", "Trata peor por una característica."), ex("¿Un mensaje en línea puede difundirse rápido?", "Sí", "Se copia y reenvía.")],
    task=T("Lee este chat inventado: Mati: «¿Alguien me pasa los apuntes de ayer?». Cata: «Yo, te los mando». Beto: «Jaja, Mati siempre faltando, qué flojo». Dani: «Uf, no sean así». Fran: sube un sticker burlesco con la cara de Mati. Escribe una tabla con dos mensajes constructivos, dos que dañan, la emoción posible de Mati y una acción que podría hacer Dani.", "Constructivos: el de Cata y el de Dani. Dañan: el de Beto y el sticker de Fran. Emoción: vergüenza o rabia. Acción de Dani: pedir que borren el sticker y apoyar a Mati.", ["identifica dos mensajes constructivos", "identifica dos que dañan", "nombra una emoción posible", "propone una acción respetuosa"], ["tabla escrita", "texto oral"], ["culpar a Mati", "confundir broma con burla"], "Reconoce los mensajes bien clasificados y pregunta qué principio se vulnera en cada uno."),
    reinforce="Escribe dos mensajes de un chat que construyan una relación respetuosa.",
    extend="Explica por qué la inclusión es parte de una buena relación en línea.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los casos de Amelia y de Rodrigo, personas inventadas, y las reglas de privacidad están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos, derechos y límites en la vida digital: privacidad, consentimiento, datos personales y ciberacoso. Sirve para saber qué se puede compartir y qué no.",
    ["Sé reconocer conductas que construyen y que dañan en línea.", "Sé qué es el consentimiento."],
    [
        "La privacidad es tu derecho a decidir quién ve tu información. Los datos personales son los que te identifican: nombre completo, dirección, teléfono, colegio, clave, fotos y ubicación. Compartirlos sin cuidado puede poner en riesgo tu seguridad. Hay datos que nunca debes entregar a desconocidos: tu dirección, tus claves y tus imágenes íntimas.",
        "El consentimiento digital significa que antes de publicar una foto, un audio o una captura de otra persona, le pides permiso. Si la persona dice que no, no se publica. Compartir sin permiso una conversación privada o una imagen íntima vulnera su intimidad y puede causar mucho daño. Un hecho importante es que lo que se publica se puede copiar y reenviar, aunque luego se borre.",
        "Tienes derechos y límites: puedes bloquear a quien te molesta, no responder, ajustar tu privacidad y pedir que borren algo tuyo. El ciberacoso es un daño repetido por medios digitales y no es una broma. Si te pasa, o ves que le pasa a otro, guardas capturas y avisas a un adulto de confianza.",
    ],
    [("privacidad", "derecho a decidir quién ve tu información"), ("datos personales", "información que te identifica, como tu dirección o tus claves"), ("consentimiento digital", "permiso de una persona antes de publicar algo suyo"), ("bloquear", "impedir que alguien te escriba o te vea"), ("captura de pantalla", "imagen de lo que se ve en la pantalla, útil como evidencia")],
    [
        W("Pedir consentimiento", "Rodrigo quiere publicar una foto del paseo en que sale Amelia. ¿Qué debe hacer antes?", ["La foto muestra a otra persona.", "Debe pedirle permiso.", "Si dice que no, no la publica."], "Pedirle permiso a Amelia"),
        W("Datos personales", "Un desconocido de un juego le pide a Amelia su dirección y el nombre de su colegio. ¿Qué debe hacer?", ["Son datos personales.", "No debe entregarlos.", "Debe avisar a un adulto de confianza."], "No entregarlos y avisar a un adulto"),
    ],
    [
        M("Creer que si borras un mensaje ya no existe.", "Se piensa que borrar es definitivo.", "Otros pudieron copiarlo; piensa antes de publicar."),
        M("Compartir una captura de una conversación privada «porque es graciosa».", "Se olvida que la conversación era privada.", "Pide permiso o no la compartas."),
    ],
    R=[
        ex("¿Cuál es un dato personal? A) Tu nombre completo junto con el nombre de tu colegio B) El nombre de tu equipo de fútbol favorito", "A", "Identifica a la persona y dónde encontrarla."),
        ex("¿Cómo se llama el permiso que se pide antes de publicar una foto o un audio de otra persona? A) Consentimiento digital B) Configuración de privacidad", "A", "Es el permiso de la persona que aparece."),
        ex("Alguien te molesta por chat. ¿Cuál de estas acciones puedes decidir tú? A) Bloquearlo y ajustar tu privacidad B) Obligarlo a borrar su cuenta", "A", "Son decisiones sobre tus propias cuentas."),
    ],
    U=[
        ex("¿Cuál es un dato que nunca debes entregar a un desconocido? A) Tu dirección B) Tu color favorito.", "A", "Pone en riesgo tu seguridad."),
        ex("Si una persona dice que no quiere que subas su foto, ¿qué haces? A) No la subes B) La subes pero sin etiquetarla.", "A", "El «no» se respeta."),
        ex("Borraste un mensaje hace un minuto. ¿Qué es cierto? A) Alguien pudo haberlo copiado antes B) Ya no existe en ninguna parte", "A", "Alguien pudo guardarlo."),
    ],
    A=[
        ex("Clasifica con P (dato personal) o N (no personal): 1) tu clave; 2) tu comida favorita; 3) el nombre de tu colegio con tu nombre completo. Escribe las letras en orden.", "P, N, P", "La clave y el nombre con el colegio identifican a la persona."),
        ex("Un compañero comparte una captura de un chat privado de Amelia para reírse. ¿Qué derecho vulnera? A) La privacidad B) La puntualidad.", "A", "Difundió algo privado sin permiso."),
        ex("Amelia recibe 6 mensajes ofensivos de un perfil falso durante 3 días seguidos. ¿Cuál es la acción segura? A) Guardar capturas, bloquear y avisar a un adulto B) Responder con insultos.", "A", "Es el protocolo ante el ciberacoso."),
    ],
    Z=[
        ex("¿Por qué conviene configurar la privacidad de tus perfiles?", "Porque permite decidir quién ve tu información", "Reduce el riesgo de que desconocidos accedan a tus datos."),
        ex("Un amigo dice: «Es mi captura, la comparto cuando quiera». ¿Qué falta considerar? A) Que la conversación incluía a otra persona con derecho a privacidad B) Que la pantalla es suya.", "A", "Los datos de otros no se publican sin permiso."),
    ],
    D=[
        arith("De 40 estudiantes de un curso inventado, 26 tienen perfil público. ¿Cuántos tienen perfil privado?", "40-26", "Al total se le restan los de perfil público."),
        arith("En un taller, 6 grupos de 5 estudiantes revisan reglas de privacidad. ¿Cuántos estudiantes participan?", "6*5", "Se multiplican grupos por integrantes."),
    ],
    context=[ex("Camila quiere subir al grupo del curso un video del recreo. En el video se ve Pablo, que antes dijo no querer salir en redes. ¿Qué debe hacer? A) No subirlo, o editar para que no aparezca B) Subirlo porque es corto.", "A", "Se respeta su «no».")],
    selfcheck=[ex("En Orientación: ¿los datos personales incluyen tu dirección y tus claves?", "Sí", "Identifican a una persona."), ex("¿Se necesita permiso para publicar una foto de otra persona?", "Sí", "Es consentimiento digital."), ex("¿Bloquear es una forma de protegerse?", "Sí", "Impide el contacto no deseado.")],
    task=T("Lee las cuatro situaciones inventadas: (a) un desconocido pide tu dirección en un juego; (b) un compañero publica una foto tuya sin permiso; (c) alguien te insulta por chat todos los días de esta semana; (d) tú quieres compartir una captura de un chat privado. Para cada una escribe qué derecho está en juego y qué haces.", "(a) Privacidad: no entrego datos y aviso a un adulto. (b) Consentimiento: pido que la borren y aviso si no. (c) Ciberacoso: guardo capturas, bloqueo y aviso a un adulto. (d) Privacidad de otros: no la comparto sin permiso.", ["responde las cuatro situaciones", "nombra un derecho por situación", "indica una acción concreta", "no usa datos personales reales"], ["tabla escrita", "texto oral"], ["ignorar el derecho en juego", "proponer responder con insultos"], "Reconoce los derechos bien identificados y pregunta qué acción es la primera en cada caso."),
    reinforce="Escribe tres datos personales que no se comparten con desconocidos.",
    extend="Explica por qué borrar un mensaje no garantiza que desaparezca.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. El caso del meme sobre Ignacio, un estudiante inventado, está escrito en los ejercicios.",
    "Aprenderé a comparar opciones y consecuencias frente a una conducta dañina en línea: reírse, reenviar, ignorar, pedir que lo borren o reportar y avisar. Sirve para elegir la respuesta que protege a la persona y a la convivencia.",
    ["Sé distinguir hechos, derechos y límites digitales.", "Sé qué es la inclusión."],
    [
        "Cuando alguien publica algo que daña a otra persona, quienes lo ven tienen distintos papeles: quien lo publicó, la persona afectada y quienes observan. Los observadores pueden reírse, reenviar, ignorar, defender a la persona, pedir que lo borren o avisar a un adulto. Cada opción tiene consecuencias: reírse y reenviar aumentan el daño; ignorar deja sola a la persona; defender y avisar protegen.",
        "Para comparar, usa tres preguntas: ¿cómo queda la persona afectada?, ¿cómo queda la convivencia del grupo? y ¿qué riesgo corro yo? Una respuesta constructiva ayuda a la persona sin agredir a quien publicó. Por ejemplo, escribir en privado «ese meme no está bien, bórralo» es mejor que insultar en público.",
        "También existe la reparación: pedir disculpas sinceras, borrar el contenido, reconocer el daño y comprometerse a no repetirlo. Una disculpa que dice «perdón si te ofendiste» no repara; una que dice «hice mal y borré el meme» sí. Y si el daño es grave o se repite, el paso seguro es avisar a un adulto del colegio.",
    ],
    [("observador", "persona que ve una conducta dañina sin ser quien la hace ni quien la sufre"), ("reparación", "acción para corregir el daño causado"), ("disculpa sincera", "reconocer el daño causado sin excusas"), ("reportar", "avisar a la plataforma que un contenido daña"), ("convivencia", "forma en que un grupo vive y trabaja junto")],
    [
        W("Comparar opciones", "Alguien publica un meme sobre Ignacio en el chat del curso. Opción A: reírse. Opción B: escribir al autor en privado pidiendo que lo borre y avisar a un profesor si no lo hace. Compara.", ["A aumenta el daño y deja a Ignacio solo.", "B protege a Ignacio sin agredir.", "B tiene un paso de ayuda adulta."], "B es mejor"),
        W("Distinguir una disculpa", "¿Cuál repara más: «perdón si te ofendiste» o «hice mal, borré el meme y no lo repetiré»?", ["La primera culpa a quien se ofendió.", "La segunda reconoce el daño y se compromete."], "La segunda"),
    ],
    [
        M("Pensar que ignorar siempre protege.", "Se cree que no hacer nada no tiene efecto.", "Ignorar puede dejar sola a la persona; apóyala o avisa."),
        M("Responder al ofensor con otro insulto público.", "Se cree que así se defiende a la persona.", "Escribe en privado o avisa a un adulto; no agravar el conflicto."),
    ],
    R=[
        ex("Ante un meme ofensivo, Tomás lo reenvía y Vale pide en privado que lo borren. ¿Quién aumenta el daño? A) Tomás B) Vale", "A", "Reenviar difunde la burla."),
        ex("¿Cuál es una respuesta constructiva a un meme ofensivo? A) Pedir en privado que lo borren B) Responder con otro meme sobre el autor", "A", "Busca reparar sin agravar el conflicto."),
        ex("¿Qué es una reparación después de dañar a alguien en línea? A) Corregir el daño, por ejemplo borrando el contenido y reconociendo el error B) Dejar pasar el tiempo hasta que se olvide", "A", "Repara con acciones concretas."),
    ],
    U=[
        ex("¿Qué opción protege más a la persona afectada? A) Defenderla y avisar a un adulto B) Ignorarla.", "A", "La acompaña y consigue ayuda."),
        ex("¿Qué disculpa repara el daño? A) «Hice mal, borré el meme y no lo repetiré.» B) «Perdón si te ofendiste.»", "A", "Reconoce el daño y se compromete."),
        ex("¿Cuál de estas es una pregunta para comparar opciones? A) ¿Cómo queda la persona afectada? B) ¿Qué meme tiene más likes?", "A", "Es una de las tres preguntas de la clase."),
    ],
    A=[
        ex("Clasifica con A (aumenta el daño) o P (protege): 1) reenviar; 2) pedir en privado que lo borren; 3) avisar a la persona orientadora. Escribe las letras en orden.", "A, P, P", "Reenviar difunde; pedir borrar y avisar protegen."),
        arith("Un meme sobre Ignacio lo vieron 30 personas distintas: 12 lo reenviaron y 5 pidieron borrarlo. ¿Cuántas lo vieron y no hicieron ninguna de las dos cosas?", "30-12-5", "Al total se le restan quienes reenviaron y quienes pidieron borrarlo."),
        ex("Fernanda quiere ayudar a Ignacio. ¿Cuál es mejor? A) Escribirle en privado «cuenta conmigo» y acompañarlo a hablar con un adulto B) Subir otro meme sobre quien lo publicó.", "A", "Lo apoya sin agravar el conflicto."),
    ],
    Z=[
        ex("¿Por qué responder con otra burla pública no resuelve el problema?", "Porque aumenta el conflicto y el daño", "Se suma otra agresión y no repara."),
        ex("Un compañero dice: «Yo solo miré». ¿Qué le falta considerar? A) Que mirar sin hacer nada deja sola a la persona B) Que mirar sin participar nunca tiene efecto.", "A", "Los observadores pueden ayudar."),
    ],
    D=[
        arith("De 30 integrantes de un chat inventado, 18 no reaccionan al meme, 7 se ríen y el resto defiende a Ignacio. ¿Cuántos lo defienden?", "30-18-7", "Al total se le restan quienes no reaccionan y quienes se ríen."),
        arith("Un meme se reenvió 4 veces por cada una de 6 personas. ¿Cuántos reenvíos hubo en total?", "4*6", "Se multiplican reenvíos por personas."),
    ],
    context=[ex("Al abrir el chat ves que dos compañeros se burlan de Bastián con un audio. ¿Cuál es la respuesta más segura? A) No participar, apoyar a Bastián y avisar a un adulto B) Grabar el audio para reírte después.", "A", "Protege a Bastián y no agrava el daño.")],
    selfcheck=[ex("En Orientación: ¿un observador puede ayudar a la persona afectada?", "Sí", "Puede defenderla o avisar."), ex("¿Una disculpa sincera reconoce el daño?", "Sí", "Por eso repara."), ex("¿Ignorar siempre protege a la persona?", "No", "Puede dejarla sola.")],
    task=T("Lee el caso inventado: Pía publica en el chat un sticker burlesco con la foto de Mauro. Hay tres reacciones: Sofía se ríe, Tomás lo reenvía y Vale le escribe a Pía en privado pidiéndole que lo borre y avisa a la profesora jefe. Compara las tres reacciones con las preguntas de la clase y escribe una frase de reparación que Pía podría decirle a Mauro.", "Sofía y Tomás aumentan el daño; Vale cuida a Mauro y a la convivencia. Frase de reparación: «Hice mal, borré el sticker y no lo repetiré».", ["compara las tres reacciones", "usa las preguntas de la clase", "escribe una frase de reparación", "no insulta a nadie"], ["tabla escrita", "texto oral"], ["justificar la burla", "disculpa sin compromiso"], "Reconoce las comparaciones y pregunta qué pregunta de las tres es más importante."),
    reinforce="Escribe una frase para pedir en privado que borren un meme ofensivo.",
    extend="Explica por qué una disculpa debe incluir reparar el daño.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Los mensajes del chat de un juego, de Isidora (inventada) y de un perfil adulto, están escritos en los ejercicios.",
    "Aprenderé a actuar de forma segura ante el engaño en línea, la presión para enviar imágenes íntimas y el contacto de adultos desconocidos. Sirve para protegerme y para ayudar a otros sin exponerlos.",
    ["Sé que los datos personales no se entregan.", "Sé bloquear y guardar capturas."],
    [
        "El grooming es el engaño de una persona adulta para ganar la confianza de un menor y luego hacerle daño, generalmente de tipo sexual. Suele comenzar con halagos, regalos, secretos y preguntas personales, y pide pasar a otro chat privado. Señales de alerta: una persona adulta desconocida que pide un secreto, que pide fotos, que te aísla de tu familia o que te amenaza si lo cuentas. Una persona adulta que hace esto actúa de forma grave, y la ley puede sancionarla. La víctima nunca es culpable.",
        "La presión para enviar imágenes íntimas también se da entre pares. Nadie está obligado a enviar fotos íntimas y nadie debe guardar ni reenviar las de otros: reenviarlas o publicarlas hace daño grave a la persona y puede tener consecuencias legales. El protocolo seguro es: 1) decir no o no responder, 2) guardar capturas, 3) bloquear al perfil, 4) avisar a un adulto de confianza, y 5) no borrar el chat hasta que el adulto lo vea.",
        "Si te llega una imagen íntima de otra persona, no la reenvíes ni la guardes y avisa a un adulto. Si una amiga te cuenta que le pasa, escúchala, dile que no tiene la culpa y acompáñala a pedir ayuda. Si necesitas orientación, puedes llamar al Fono Niños 147.",
    ],
    [("grooming", "engaño de un adulto para ganar la confianza de un menor y dañarlo"), ("imagen íntima", "foto o video que muestra el cuerpo sin ropa o una situación íntima"), ("protocolo", "conjunto de pasos acordados para actuar"), ("evidencia", "prueba de lo ocurrido, como una captura"), ("perfil falso", "cuenta que oculta la identidad real de quien la usa")],
    [
        W("Detectar señales", "En un juego, un perfil adulto le dice a Isidora: «Eres muy madura, no se lo cuentes a nadie; mándame una foto». ¿Qué señales hay?", ["Le pide secreto.", "Le pide una foto.", "Es un adulto desconocido."], "Secreto, pedido de foto y adulto desconocido"),
        W("Aplicar el protocolo", "Isidora recibe presión para enviar una foto íntima. Ordena los pasos.", ["No responder.", "Guardar capturas.", "Bloquear.", "Avisar a un adulto de confianza y no borrar el chat."], "No responder, capturas, bloquear y avisar"),
    ],
    [
        M("Pensar que ceder una vez evitará que insistan.", "Se cree que enviar una foto termina el problema.", "Enviar da más poder al chantaje; sigue el protocolo."),
        M("Borrar el chat por vergüenza antes de mostrarlo.", "Se cree que así desaparece el problema.", "No lo borres: es la evidencia que ayuda al adulto."),
    ],
    R=[
        ex("Un perfil adulto desconocido le dice a un adolescente: «no se lo cuentes a nadie». ¿Qué señal es? A) Un pedido de secreto, señal de grooming B) Una muestra normal de cortesía", "A", "El secreto protege al adulto y no al menor."),
        ex("¿Cuál es un ejemplo de imagen íntima? A) Una foto que muestra el cuerpo sin ropa B) Una foto de un paseo con amigos con ropa normal", "A", "Muestra el cuerpo sin ropa o una situación íntima."),
        ex("Una adolescente fue engañada por un adulto en un chat y piensa: «fue mi culpa por contestarle». ¿Qué debe recordar? A) La responsabilidad es de quien engaña B) Debió desconfiar desde el principio", "A", "La víctima nunca es culpable."),
    ],
    U=[
        ex("¿Cuál es una señal de grooming? A) Un adulto desconocido pide un secreto y fotos B) Un compañero pide la tarea.", "A", "El secreto y las fotos son señales de alerta."),
        ex("¿Qué se hace con las capturas del chat? A) Guardarlas y mostrarlas a un adulto B) Borrarlas.", "A", "Son la evidencia."),
        ex("Si te llega una imagen íntima de otra persona, ¿qué haces? A) No la reenvías ni la guardas y avisas a un adulto B) La guardas por si acaso.", "A", "Guardarla o reenviarla agrava el daño."),
    ],
    A=[
        ex("Ordena los pasos del protocolo: 1) bloquear; 2) no responder; 3) avisar a un adulto; 4) guardar capturas. ¿Cuál es el primero?", "No responder", "Se corta la conversación antes de actuar."),
        ex("Un compañero amenaza a Rocío: «Si no me mandas una foto, difundo tu chat». ¿Qué debe hacer? A) Guardar la captura, bloquearlo y avisar a un adulto B) Enviar la foto para que no difunda.", "A", "Ceder aumenta el chantaje."),
        ex("Una amiga te cuenta que un adulto de un juego le pide secreto y fotos. ¿Qué respuesta ayuda? A) «No tienes la culpa; vamos a contárselo a un adulto.» B) «Ya se le pasará.»", "A", "La apoya y la acerca a la ayuda."),
    ],
    Z=[
        ex("¿Por qué un adulto que pide un secreto a un menor es una señal de alerta?", "Porque quiere ocultar el daño y evitar que lo cuenten", "El secreto protege al adulto, no al menor."),
        ex("¿Por qué no se debe borrar el chat antes de mostrarlo a un adulto? A) Porque es evidencia que ayuda a protegerte B) Porque ocupa memoria.", "A", "El adulto necesita ver lo que pasó."),
    ],
    D=[
        arith("En un grupo de ejemplo de 45 estudiantes, 30 saben el protocolo completo. ¿Cuántos no lo saben?", "45-30", "Al total se le restan los que sí lo saben."),
        arith("El protocolo tiene 5 pasos. Un curso de 35 estudiantes se divide en grupos de 7 para practicarlo. ¿Cuántos grupos hay?", "35//7", "Se divide el total entre los integrantes de cada grupo."),
    ],
    context=[ex("Tu compañera Inés recibe mensajes de un perfil que dice ser un joven famoso y le pide fotos. ¿Qué es lo más seguro? A) Bloquear, guardar capturas y avisar a un adulto B) Seguir la conversación para saber quién es.", "A", "No debe seguir el contacto con un perfil dudoso.")],
    selfcheck=[ex("En Orientación: ¿el grooming es un engaño de un adulto a un menor?", "Sí", "Es su definición."), ex("¿Se debe reenviar una imagen íntima de otra persona?", "No", "Daña gravemente a la persona."), ex("¿Es correcto avisar a un adulto de confianza?", "Sí", "Es el paso final del protocolo.")],
    task=T("Lee los cinco mensajes inventados de un perfil desconocido a Joaquín: «Hola, vi tu partida»; «Eres muy bueno, mejor que todos»; «Te regalo unos juegos si me das tu número»; «No se lo cuentes a tu familia, es un secreto»; «Mándame una foto tuya». Subraya dos señales de alerta, escribe los cinco pasos del protocolo en orden y una frase que usarías con un adulto.", "Señales: el pedido de secreto y la foto. Pasos: no responder, guardar capturas, bloquear, avisar a un adulto, no borrar el chat. Frase: «Un perfil desconocido me pidió un secreto y una foto; quiero que veas los mensajes».", ["identifica dos señales", "ordena los pasos del protocolo", "escribe una frase para el adulto", "no reproduce datos personales"], ["lista escrita", "texto oral"], ["omitir avisar al adulto", "borrar el chat"], "Reconoce las señales y pregunta qué paso sigue después de guardar capturas."),
    reinforce="Escribe los cinco pasos del protocolo con tus palabras.",
    extend="Explica por qué la víctima de un engaño en línea nunca es culpable.",
)

lesson(
    OA5, 5,
    "Una hoja y un lápiz. Los mensajes de ejemplo están escritos en los ejercicios; usa personas inventadas.",
    "Aprenderé a comunicar con respeto en línea, a pedir reparación o ayuda y a escribir mensajes que no dañan. Sirve para construir relaciones sanas, también en las redes.",
    ["Sé comparar opciones ante una conducta dañina en línea.", "Sé aplicar el protocolo de seguridad."],
    [
        "Comunicarse con respeto en línea tiene reglas simples. Antes de enviar, pregúntate si lo dirías cara a cara, si podría herir a alguien y si lo escribirías si lo viera una persona adulta de tu familia. Evita escribir con mayúsculas todo, que parece un grito; evita ironías que pueden entenderse mal; y no uses el humor a costa de alguien.",
        "Para pedir reparación, usa mensajes en primera persona, calmados y concretos: «Me incomodó que subieras mi foto. Por favor, bórrala». Si la persona no responde, reporta el contenido a la plataforma y avisa a un adulto. Si fuiste tú quien se equivocó, di: «Me equivoqué, borré el mensaje y lamento el daño».",
        "Hablar de un conflicto es mejor en persona o con una llamada que a punta de mensajes, porque se evitan malentendidos. Y si algo te supera, pide ayuda: a una persona adulta de confianza, a la persona orientadora, o llama al Fono Niños 147.",
    ],
    [("primera persona", "frase que parte con «yo» y dice lo que uno siente o pide"), ("malentendido", "interpretación equivocada de lo que otro quiso decir"), ("reparación", "acción para corregir el daño"), ("reportar", "avisar a la plataforma que un contenido daña"), ("ironía", "decir lo contrario de lo que se piensa, que puede malinterpretarse")],
    [
        W("Reescribir un mensaje", "Matías escribe: «ERES TONTO, BORRA ESA FOTO». Reescríbelo en primera persona.", ["Dice lo que siente.", "Pide con calma."], "«Me incomodó la foto. Por favor, bórrala.»"),
        W("Reparar", "Fer subió un chiste hiriente. ¿Qué mensaje repara?", ["Reconoce el daño.", "Borra y se compromete."], "«Me equivoqué, lo borré y lamento el daño.»"),
    ],
    [
        M("Escribir con rabia y enviar de inmediato.", "Se reacciona antes de pensar.", "Respira, espera y reescribe en primera persona."),
        M("Resolver un conflicto largo solo por mensajes.", "Se cree que es más rápido.", "Habla en persona o por llamada si el tema es delicado."),
    ],
    R=[
        ex("Un chat dice: «ESTOY HARTA DE TI». ¿Cómo suele leerse? A) Como un grito, aunque no se oiga B) Como un mensaje calmado", "A", "Las mayúsculas parecen un grito."),
        ex("¿Cuál mensaje está en primera persona? A) «Me incomodó que subieras mi audio.» B) «Tú siempre subes cosas sin avisar.»", "A", "Dice lo que yo siento y no acusa."),
        ex("Un contenido que te daña sigue publicado. ¿Qué significa reportarlo? A) Avisar a la plataforma que daña B) Compartirlo para que más gente lo vea", "A", "Pide a la plataforma que lo retire."),
    ],
    U=[
        ex("¿Qué mensaje respeta más? A) «Me molestó que subieras mi audio; por favor, bórralo.» B) «Eres un pesado, bórralo ya.»", "A", "Pide con calma y sin insultar."),
        ex("Antes de enviar un mensaje delicado, ¿qué pregunta ayuda? A) ¿Lo diría cara a cara? B) ¿Cuántos emoticones tiene?", "A", "Evita herir por impulso."),
        ex("Si la persona no borra un contenido que te daña, ¿qué haces? A) Reportar y avisar a un adulto B) Vengarte publicando algo suyo.", "A", "Es una respuesta segura y respetuosa."),
    ],
    A=[
        ex("Clasifica con R (respeta) o H (hiere): 1) «Me gustaría que no compartieras mi audio.» 2) «JAJA qué ridícula saliste.» 3) «Gracias por avisarme, lo borro.» Escribe las letras en orden.", "R, H, R", "La 1 y la 3 son respetuosas; la 2 se burla."),
        ex("Un conflicto entre dos amigas por mensajes ya lleva 12 mensajes y cada vez se entienden menos. ¿Qué conviene? A) Hablar en persona con apoyo de un adulto si es necesario B) Seguir escribiendo más rápido.", "A", "En persona se aclaran tono e intención."),
        ex("Marcela escribe: «Qué gracioso tu corte de pelo, jaja». ¿Qué problema tiene el mensaje? A) Puede entenderse como una burla B) Es demasiado largo.", "A", "La ironía puede herir."),
    ],
    Z=[
        ex("¿Por qué esperar unos minutos antes de responder con enojo ayuda?", "Porque evita decir algo que luego dañe", "La calma permite escribir con respeto."),
        ex("Un compañero dice: «Si me disculpo, muestro debilidad». ¿Qué le responderías? A) Que reconocer un error repara la relación B) Que tiene razón.", "A", "Disculparse repara y fortalece."),
    ],
    D=[
        arith("Un grupo de 28 estudiantes escribe 3 mensajes respetuosos cada uno para un cartel. ¿Cuántos mensajes hay?", "28*3", "Se multiplican estudiantes por mensajes."),
        arith("De 20 mensajes del chat, 6 tienen todo en mayúsculas. ¿Cuántos no?", "20-6", "Al total se le restan los que tienen mayúsculas."),
    ],
    context=[ex("Tu amiga Javiera sube sin avisar una foto tuya con una frase burlesca. ¿Qué mensaje inicial es mejor? A) «Me molestó la foto con esa frase; por favor, bórrala.» B) «Te voy a denunciar a todos.»", "A", "Es claro, calmado y concreto.")],
    selfcheck=[ex("En Orientación: ¿un mensaje en primera persona dice lo que tú sientes?", "Sí", "Empieza con «yo» o con lo que te pasó."), ex("¿Se debe hablar en persona un conflicto delicado?", "Sí", "Se evitan malentendidos."), ex("¿Reportar es avisar a la plataforma?", "Sí", "Ayuda a quitar el daño.")],
    task=T("Lee las tres situaciones inventadas: (a) un compañero subió tu foto sin permiso; (b) escribiste un comentario burlón y alguien se molestó; (c) un chat del curso se llena de insultos. Escribe un mensaje para cada una: en (a) una petición en primera persona, en (b) una reparación y en (c) una propuesta al grupo y a quién avisarías.", "(a) «Me incomodó que subieras mi foto; por favor, bórrala.» (b) «Me equivoqué, borré el comentario y lamento el daño.» (c) «Propongo un acuerdo de respeto en el chat; si sigue, aviso a la profesora jefe.»", ["escribe los tres mensajes", "usa primera persona y tono calmado", "incluye reparación en (b)", "nombra a quién avisar en (c)"], ["mensajes escritos", "juego de roles"], ["mensajes con insultos", "olvidar avisar a un adulto"], "Reconoce los mensajes respetuosos y pregunta qué cambiaría en el menos claro."),
    reinforce="Reescribe en tono respetuoso: «Eres tonto, devuélveme mi cuaderno».",
    extend="Explica por qué la ironía puede herir en un chat.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. El conflicto de Rocío y Gabriel por un trabajo en grupo, personas inventadas, está escrito en los ejercicios.",
    "Aprenderé a examinar un conflicto distinguiendo las posiciones de cada parte, sus intereses y sus emociones. Sirve para buscar acuerdos que beneficien a todos.",
    ["Sé que un conflicto es una diferencia entre personas (8.º básico).", "Sé que la violencia no resuelve conflictos."],
    [
        "Un conflicto es una situación en que dos o más personas tienen intereses, necesidades o ideas que parecen incompatibles. Es normal y no siempre es malo: puede ayudar a aclarar cosas. Lo importante es cómo se enfrenta, con respeto a los derechos de todos y sin violencia.",
        "Para examinar un conflicto, distingue tres cosas. La posición es lo que cada persona dice que quiere: «yo hago la presentación». El interés es la razón detrás de esa posición: «quiero que mi nota sea buena». Las emociones son lo que siente: rabia, miedo, frustración. Muchas veces las posiciones chocan, pero los intereses se pueden compatibilizar.",
        "También se separan los hechos de las interpretaciones. «Gabriel no contestó el mensaje» es un hecho. «Gabriel me ignora» es una interpretación. Confundirlos aumenta el conflicto. Un buen análisis habla de lo que ocurrió, de lo que cada parte necesita y de qué derechos están en juego, como ser escuchado y tratado con respeto.",
    ],
    [("conflicto", "diferencia de intereses, necesidades o ideas entre personas"), ("posición", "lo que cada persona dice que quiere"), ("interés", "razón o necesidad detrás de la posición"), ("interpretación", "explicación que una persona da a un hecho, que puede no ser cierta"), ("parte", "persona o grupo involucrado en un conflicto")],
    [
        W("Posición e interés", "Rocío dice: «Yo hago la presentación». Quiere asegurar su nota. ¿Cuál es la posición y cuál el interés?", ["Lo que dice querer es hacer la presentación: posición.", "Lo que necesita es una buena nota: interés."], "Posición: hacer la presentación; interés: la nota"),
        W("Hecho o interpretación", "«Gabriel no contestó el mensaje en dos días» y «Gabriel me ignora a propósito». ¿Cuál es hecho?", ["No contestó se puede comprobar.", "A propósito es una interpretación."], "La primera es hecho"),
    ],
    [
        M("Creer que si hay conflicto, alguien tiene la culpa.", "Se busca un culpable en vez de entender intereses.", "Distingue posiciones, intereses y hechos."),
        M("Tomar una interpretación como si fuera un hecho.", "Se supone la intención del otro.", "Pregunta y contrasta con lo que pasó."),
    ],
    R=[
        ex("Dos hermanos discuten por la tele. Ana dice: «Yo veo mi serie ahora». ¿Qué es esa frase? A) Una posición B) Un interés", "A", "Es lo que ella declara querer."),
        ex("Ana quiere ver su serie ahora porque hoy es el último capítulo y no quiere enterarse del final por las redes. ¿Qué es eso? A) Su interés B) Su posición", "A", "Es la razón detrás de lo que pide."),
        ex("Un conflicto enfrentado con respeto a los derechos de todos, ¿qué puede lograr? A) Aclarar cosas y mejorar el trabajo B) Terminar siempre la amistad", "A", "Un conflicto no siempre es malo."),
    ],
    U=[
        ex("¿Cuál es un hecho? A) «Gabriel no entregó su parte el lunes.» B) «Gabriel es un irresponsable.»", "A", "Se puede comprobar; la otra es un juicio."),
        ex("Gabriel dice: «No quiero hacer las diapositivas» porque no se siente bueno en eso. ¿Cuál es su interés? A) No sentirse expuesto en algo que no domina B) No hacer las diapositivas.", "A", "La razón detrás de su posición."),
        ex("¿Qué derecho está en juego cuando se escucha a cada parte? A) Ser escuchado y respetado B) Ganar siempre.", "A", "Es un derecho de todos."),
    ],
    A=[
        ex("Clasifica con P (posición) o I (interés): 1) «Quiero la cancha a las 12:00»; 2) «Necesito practicar para el campeonato»; 3) «No acepto jugar a otra hora.» Escribe las letras en orden.", "P, I, P", "La 1 y la 3 son lo que piden; la 2 es la razón."),
        ex("Un mensaje dice: «Siempre me ignoras». ¿Qué parte es interpretación? A) «Siempre me ignoras» B) «No contestaste el mensaje de las 17:00»", "A", "Supone una intención y una repetición no comprobada."),
        ex("Rocío cree que «Gabriel me ignora a propósito». Después se sabe que Gabriel estuvo sin datos móviles dos días. ¿Qué muestra eso sobre su frase? A) Era una interpretación equivocada B) Era un hecho comprobado.", "A", "Suponía una intención que no existía."),
    ],
    Z=[
        ex("¿Por qué conviene mirar los intereses y no solo las posiciones?", "Porque permite encontrar soluciones que sirvan a las dos partes", "Detrás de posiciones opuestas suele haber intereses compatibles."),
        ex("Un compañero dice: «Se ve que Gabriel lo hace a propósito». ¿Qué le falta? A) Un hecho que lo compruebe B) Más enojo.", "A", "Es una interpretación sin pruebas."),
    ],
    D=[
        arith("En un conflicto de ejemplo, 3 compañeros dicen 2 posiciones cada uno. ¿Cuántas posiciones se dijeron?", "3*2", "Se multiplican personas por posiciones."),
        arith("Un grupo de 5 tiene que repartir 20 tareas en partes iguales. ¿Cuántas tareas le tocan a cada persona?", "20//5", "Se divide el total entre los integrantes."),
    ],
    context=[ex("En el Consejo de Curso discuten por el lugar de la fiesta: unos quieren el gimnasio y otros el patio. Los primeros quieren estar bajo techo; los segundos, más espacio. ¿Cuáles son los intereses? A) Estar bajo techo y tener espacio B) El gimnasio y el patio.", "A", "Son las razones; gimnasio y patio son las posiciones.")],
    selfcheck=[ex("En Orientación: ¿un conflicto es una diferencia de intereses o ideas?", "Sí", "Es su definición."), ex("¿Una interpretación es lo mismo que un hecho?", "No", "La interpretación supone una intención."), ex("¿El interés es la razón detrás de la posición?", "Sí", "Explica por qué se pide algo.")],
    task=T("Lee el conflicto inventado: Vero y Sebastián deben entregar un afiche el viernes. Vero quiere dividir en partes y que cada uno trabaje en casa; Sebastián quiere juntarse el jueves a trabajar. Vero no tiene tiempo el jueves por su entrenamiento; Sebastián teme que el afiche no quede parejo. Escribe las posiciones, los intereses, un hecho y una interpretación.", "Posiciones: Vero, trabajar en casa; Sebastián, juntarse el jueves. Intereses: Vero, tener tiempo para entrenar; Sebastián, que el afiche quede parejo. Hecho: Vero tiene entrenamiento el jueves. Interpretación: «Sebastián no confía en mí».", ["identifica las dos posiciones", "identifica los dos intereses", "da un hecho y una interpretación", "no culpa a nadie"], ["tabla escrita", "texto oral"], ["confundir posición con interés", "dar una opinión como hecho"], "Reconoce lo bien identificado y pregunta qué interés se podría compatibilizar."),
    reinforce="Escribe la posición y el interés de un personaje que quiere el último pan.",
    extend="Explica por qué un conflicto no siempre es malo.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. Los derechos de la tarjeta y los casos de Matías y Javiera, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a distinguir los derechos y los límites en un conflicto. Sirve para saber cuándo se puede negociar y cuándo no, y qué conductas no son aceptables.",
    ["Sé distinguir posición, interés y hechos.", "Sé que la dignidad se respeta."],
    [
        "En un conflicto hay derechos que todas las partes tienen: ser escuchadas, ser tratadas con respeto, expresar su opinión, no sufrir violencia ni humillación y que se resguarde su privacidad. Estos derechos no se negocian: el acuerdo se construye sobre ellos. Si uno pide que no lo traten con respeto, no hay negociación posible.",
        "Los límites son lo que no se permite en un conflicto: golpear, amenazar, insultar, difundir fotos, aislar o chantajear. Cuando hay violencia, no se negocia entre las partes: se detiene la situación y se avisa a un adulto del colegio. La violencia no resuelve conflictos, solo los agrava.",
        "Los derechos también se equilibran. Mi libertad de opinar termina donde empieza a dañar tu dignidad. Por ejemplo, puedes decir «no estoy de acuerdo con tu propuesta», pero no «eres un inútil». En un buen análisis se identifican qué derechos están en juego y qué límites se cruzaron.",
    ],
    [("derecho", "lo que corresponde a toda persona y los demás deben respetar"), ("límite", "lo que no se permite hacer a otros"), ("dignidad", "valor que tiene toda persona y que no debe ser humillada"), ("negociar", "buscar un acuerdo hablando"), ("violencia", "daño intencional físico, psicológico o digital")],
    [
        W("Derechos y límites", "En una discusión, Matías le grita «eres un inútil» a Javiera. ¿Qué límite se cruzó?", ["El insulto humilla.", "La dignidad no se negocia."], "Se cruzó el límite del respeto"),
        W("Cuándo no negociar", "En el patio, un estudiante empuja a otro durante un desacuerdo. ¿Se negocia entre ellos?", ["Hay violencia física.", "Se detiene y se avisa a un adulto."], "No: se avisa a un adulto"),
    ],
    [
        M("Pensar que todo se puede negociar.", "Se olvida que algunos derechos no se negocian.", "Primero se detiene la violencia; luego se busca acuerdo."),
        M("Creer que expresar una opinión da derecho a insultar.", "Se confunde libertad de expresión con agresión.", "La opinión se dice sin dañar la dignidad."),
    ],
    R=[
        ex("Javiera quiere explicar su idea y los demás la interrumpen sin dejarla terminar. ¿Qué derecho se afecta? A) Ser escuchada B) Ganar la discusión", "A", "Todas las partes tienen derecho a ser escuchadas."),
        ex("Alguien dice: «Te voy a publicar en el grupo si no cedes». ¿Qué es eso? A) Una amenaza, que cruza un límite B) Una opinión respetuosa", "A", "Amenazar quita la libertad de la otra parte."),
        ex("¿Cuál de estas conductas nunca se permite en un conflicto? A) Aislar a alguien del grupo para presionarlo B) Pedir un turno para hablar", "A", "Aislar es una forma de violencia psicológica."),
    ],
    U=[
        ex("¿Cuál frase respeta los derechos? A) «No estoy de acuerdo con tu propuesta.» B) «Eres un inútil.»", "A", "Expresa una opinión sin humillar."),
        ex("¿Qué derecho se vulnera si difunden una foto de Javiera sin permiso? A) La privacidad B) El recreo.", "A", "Se expuso su imagen."),
        ex("¿Qué se hace cuando hay amenazas en un conflicto? A) Avisar a un adulto del colegio B) Negociar a solas con quien amenaza.", "A", "No es seguro negociar bajo amenaza."),
    ],
    A=[
        ex("Clasifica con D (derecho) o L (límite cruzado): 1) Javiera pide ser escuchada; 2) Matías amenaza con publicar una foto; 3) Javiera propone buscar un acuerdo. Escribe las letras en orden.", "D, L, D", "La 1 y la 3 ejercen derechos; la 2 cruza un límite."),
        ex("Dos estudiantes discuten por turnos de la cancha. Uno dice «tengo derecho a jugar tanto como tú». ¿Qué principio usa? A) Que ambos tienen el mismo derecho B) Que la privacidad se protege.", "A", "Pide el mismo trato para ambos."),
        ex("Marta quiere decir lo que piensa de la propuesta de un compañero. ¿Cuál es respetuoso? A) «No creo que alcance el tiempo; propongo otra opción.» B) «Tu idea es una porquería.»", "A", "Critica la idea sin humillar a la persona."),
    ],
    Z=[
        ex("¿Por qué no se negocia bajo amenaza?", "Porque no hay igualdad ni libertad para decidir", "La amenaza quita la libertad de una de las partes."),
        ex("Un compañero dice: «Mi libertad de opinar me permite todo». ¿Qué falta? A) Que mi libertad termina donde daña la dignidad de otro B) Que no hay límites.", "A", "Los derechos se equilibran."),
    ],
    D=[
        arith("Un curso lista 12 derechos y 8 límites para un cartel. ¿Cuántos ítems hay en total?", "12+8", "Se suman derechos y límites."),
        arith("De 36 estudiantes, 27 saben que no se negocia bajo amenaza. ¿Cuántos no lo saben?", "36-27", "Al total se le restan los que sí lo saben."),
    ],
    context=[ex("En un recreo, un estudiante quita la pelota a otro y lo empuja. ¿Qué corresponde? A) Detener el empujón y avisar a un inspector B) Que los dos se ajusten solos.", "A", "Hay violencia física.")],
    selfcheck=[ex("En Orientación: ¿insultar es un límite que no se debe cruzar?", "Sí", "Humilla a otra persona."), ex("¿Se negocia bajo amenaza?", "No", "No hay libertad para decidir."), ex("¿Ser escuchado es un derecho?", "Sí", "Todas las partes lo tienen.")],
    task=T("Lee el caso inventado: Dante y Pía discuten por la propuesta de un baile del curso. Dante le dice «tu idea es ridícula» y Pía le responde que lo publicará en el grupo. Escribe: dos derechos en juego, dos límites cruzados y qué haría una persona que mira para ayudar.", "Derechos: ser escuchados y ser tratados con respeto. Límites cruzados: el insulto y la amenaza de publicar. Ayuda: separar la discusión y avisar a la profesora jefe.", ["nombra dos derechos", "nombra dos límites cruzados", "propone una ayuda segura", "no justifica la violencia"], ["tabla escrita", "texto oral"], ["justificar el insulto", "negociar bajo amenaza"], "Reconoce los derechos y límites y pregunta qué acción es la primera."),
    reinforce="Escribe una frase respetuosa para decir que no estás de acuerdo.",
    extend="Explica por qué la libertad de opinar tiene límites.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. El caso del uso de la cancha, con personajes inventados, está escrito en los ejercicios.",
    "Aprenderé a comparar cinco formas de enfrentar un conflicto (evitar, imponer, ceder, negociar y pedir mediación) y sus consecuencias. Sirve para elegir la que busca acuerdos que beneficien a todos.",
    ["Sé distinguir derechos y límites.", "Sé reconocer posiciones e intereses."],
    [
        "Hay varias maneras de enfrentar un conflicto. Evitar es no hablar del tema; imponer es obligar al otro a aceptar lo que uno quiere; ceder es aceptar lo que el otro quiere dejando lo propio; negociar es dialogar para encontrar un acuerdo en que ambas partes ganan algo; y la mediación es pedir a una tercera persona neutral que ayude a conversar, sin decidir por ellas.",
        "Cada forma tiene consecuencias. Evitar deja el problema sin resolver. Imponer genera rabia y rompe la relación. Ceder siempre deja a una parte con la necesidad sin atender. Negociar suele producir acuerdos más duraderos, porque ambas partes se comprometen. Y la mediación ayuda cuando la conversación está muy tensa. Lo mejor es la que busca un beneficio mutuo y compromiso recíproco, sin violencia.",
        "Para comparar, pregunta: ¿se atienden los intereses de las dos partes?, ¿se respetan los derechos?, ¿se puede cumplir el acuerdo?, ¿cómo queda la relación? Un acuerdo «ganar-ganar» no significa que todos obtengan todo, sino que todos obtengan algo importante.",
    ],
    [("evitar", "no hablar del conflicto"), ("imponer", "obligar a otro a aceptar lo que uno quiere"), ("ceder", "aceptar lo que el otro quiere dejando lo propio"), ("negociar", "dialogar para llegar a un acuerdo en que ambas partes ganan algo"), ("mediación", "ayuda de una tercera persona neutral para conversar")],
    [
        W("Clasificar la forma", "Dos cursos quieren la cancha a la misma hora. Uno dice «es nuestra y punto». ¿Qué forma de enfrentar el conflicto es?", ["Obliga al otro a aceptar.", "No escucha lo que el otro necesita."], "Imponer"),
        W("Buscar ganar-ganar", "La cancha se usa a la misma hora. Propuesta: cada curso la usa 30 minutos de los 60 del recreo. ¿Es un acuerdo ganar-ganar?", ["Ambos obtienen tiempo.", "Se respeta a las dos partes."], "Sí"),
    ],
    [
        M("Creer que ceder siempre es ser amable.", "Se olvida que una necesidad queda sin atender.", "Ceder a veces sirve, pero conviene buscar un acuerdo para ambos."),
        M("Pensar que mediación es que otro decida quién gana.", "Se confunde con un juicio.", "La persona mediadora ayuda a conversar y las partes deciden."),
    ],
    R=[
        ex("No hablar del conflicto, ¿es evitar o negociar?", "Evitar", "No se enfrenta el problema."),
        ex("Obligar al otro a aceptar lo que uno quiere, ¿es imponer o ceder?", "Imponer", "Usa la fuerza o la autoridad."),
        ex("Un curso le cede siempre la cancha a otro para evitar peleas. ¿Qué forma usa? A) Ceder B) Negociar", "A", "Acepta lo que el otro quiere y deja lo propio."),
    ],
    U=[
        ex("¿Qué forma busca un acuerdo con beneficio para las dos partes? A) Negociar B) Imponer.", "A", "Las dos ganan algo importante."),
        ex("¿Qué consecuencia suele tener imponer? A) Rabia y ruptura de la relación B) Acuerdos duraderos.", "A", "Una parte siente que no la escucharon."),
        ex("¿Quién decide en una mediación? A) Las partes, con ayuda de una persona neutral B) La persona mediadora sola.", "A", "La mediación facilita; no impone."),
    ],
    A=[
        ex("Clasifica: 1) no hablar del tema por semanas; 2) pedir ayuda a una persona neutral; 3) proponer turnos para usar la cancha. Escribe E (evitar), M (mediación) o N (negociar) en orden.", "E, M, N", "La 1 evita, la 2 pide mediación y la 3 busca un acuerdo."),
        ex("Dos cursos tienen 80 minutos de recreo y acuerdan repartirlos en partes iguales. ¿Cuántos minutos le tocan a cada curso?", "40", "80 dividido en 2 partes da 40 minutos."),
        ex("Un curso cede siempre su turno para evitar problemas. ¿Qué consecuencia tiene? A) Su necesidad queda sin atender B) Se resuelve el conflicto de fondo.", "A", "Una parte siempre pierde."),
    ],
    Z=[
        ex("¿Por qué un acuerdo ganar-ganar suele durar más?", "Porque las dos partes se sienten escuchadas y se comprometen", "Cada parte obtiene algo importante y por eso lo cumple."),
        ex("Un curso dice: «Imponer es más rápido, así que es mejor». ¿Qué falta considerar? A) La relación y el cumplimiento después B) Nada, es lo mejor.", "A", "Lo impuesto suele generar rabia y no se cumple."),
    ],
    D=[
        arith("Tres cursos se turnan una cancha durante 90 minutos, en partes iguales. ¿Cuántos minutos usa cada curso?", "90//3", "Se divide el tiempo total entre los cursos.", " minutos"),
        arith("En una votación de 40 estudiantes, 24 prefieren negociar, 9 prefieren evitar y el resto prefiere pedir mediación. ¿Cuántos prefieren mediación?", "40-24-9", "Al total se le restan las otras preferencias."),
    ],
    context=[ex("Dos amigos pelean por quién usa el computador del taller. Un profesor les propone conversar con él presente para ayudar. ¿Qué forma de resolución es? A) Mediación B) Imposición.", "A", "Una persona neutral facilita el diálogo.")],
    selfcheck=[ex("En Orientación: ¿negociar busca un acuerdo para ambas partes?", "Sí", "Ambas ganan algo."), ex("¿Imponer genera rabia en el otro?", "Sí", "No se siente escuchado."), ex("¿La mediación la hace una tercera persona neutral?", "Sí", "Ayuda a conversar.")],
    task=T("Lee el conflicto inventado: dos cursos quieren la cancha a la misma hora. El A dice «nos tocaba a nosotros»; el B dice «llegamos primero». Escribe las cinco formas de enfrentar un conflicto aplicadas a este caso (una frase por cada una), clasifica con el semáforo cuál conviene más y explica por qué.", "Evitar: no usan la cancha. Imponer: ocupar sin hablar. Ceder: A le deja la cancha a B. Negociar: turnos de 30 minutos. Mediación: la profesora ayuda a decidir turnos. Verde: negociar o mediación.", ["escribe las cinco formas aplicadas", "usa el semáforo", "explica por qué conviene negociar o mediar", "no justifica imponer"], ["tabla escrita", "texto oral"], ["confundir ceder con negociar", "olvidar la mediación"], "Reconoce las formas bien aplicadas y pregunta cuál daría un acuerdo más duradero."),
    reinforce="Aplica evitar, imponer y negociar a un conflicto por el último asiento del bus escolar.",
    extend="Explica por qué ceder siempre no resuelve el conflicto de fondo.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. La plantilla de acuerdo y el caso de Lucas y Elisa, personas inventadas, están escritos en los ejercicios.",
    "Aprenderé a elegir una solución segura para un conflicto y a escribir un acuerdo con compromiso recíproco. Sirve para que lo acordado se cumpla y para saber cuándo pedir ayuda a un adulto.",
    ["Sé comparar formas de enfrentar un conflicto.", "Sé que la violencia se detiene y se avisa."],
    [
        "Un acuerdo bien hecho dice qué hará cada parte, cuándo y cómo se revisará. Se escribe con conductas observables, no con buenas intenciones: «Lucas entrega su parte el miércoles a las 18:00» y «Elisa revisa el trabajo el jueves». Un acuerdo con compromiso recíproco incluye tareas para las dos partes, porque si solo una se compromete, no es un acuerdo parejo.",
        "Un buen acuerdo tiene cuatro partes: una conducta que se pueda ver, una persona responsable, un plazo y una revisión. Por ejemplo: «Lucas sube su parte al documento (conducta) hasta el miércoles (plazo); Elisa la revisa (conducta) el jueves (plazo); el viernes conversan 5 minutos para ver si funcionó (revisión)».",
        "Elegir una acción segura también es saber cuándo escalar. Si hay golpes, amenazas, acoso o humillaciones, no se acuerda a solas: se avisa a un adulto del colegio. Y si el acuerdo no se cumple, no se castiga ni se humilla; se vuelve a conversar con el adulto o con una persona mediadora.",
    ],
    [("acuerdo", "decisión conjunta de las partes sobre qué hará cada una"), ("compromiso recíproco", "compromiso de ambas partes"), ("conducta observable", "acción que se puede ver y comprobar"), ("plazo", "fecha o momento en que se cumplirá"), ("revisión", "momento para comprobar si el acuerdo funciona")],
    [
        W("Mejorar un acuerdo", "Lucas y Elisa escriben: «Vamos a esforzarnos». ¿Qué le falta?", ["No dice qué hará cada uno.", "No tiene plazo ni revisión."], "Una conducta observable, un responsable, un plazo y una revisión"),
        W("Acuerdo completo", "Redacta un acuerdo para entregar el trabajo el viernes.", ["Lucas sube su parte el miércoles.", "Elisa la revisa el jueves.", "El viernes conversan 5 minutos."], "Acuerdo con conducta, responsable, plazo y revisión"),
    ],
    [
        M("Escribir acuerdos con buenas intenciones pero sin fechas.", "Se piensa que la confianza basta.", "Usa conducta observable, plazo y revisión."),
        M("Acordar a solas cuando hay golpes o amenazas.", "Se cree que se pueden arreglar entre las partes.", "Cuando hay violencia, avisa a un adulto."),
    ],
    R=[
        ex("En un acuerdo se escribe: «el viernes conversan 5 minutos para ver si funcionó». ¿Qué parte es? A) La revisión B) El plazo", "A", "Es el momento para comprobar si el acuerdo funciona."),
        ex("En un acuerdo se escribe: «hasta el miércoles a las 18:00». ¿Qué parte es? A) El plazo B) La revisión", "A", "Indica cuándo se cumple la conducta."),
        ex("Un acuerdo dice: «Mía hará todo el trabajo». ¿Qué le falta? A) El compromiso de ambas partes B) Que Mía lo firme dos veces", "A", "Un acuerdo recíproco compromete a las dos partes."),
    ],
    U=[
        ex("¿Cuál es un compromiso recíproco? A) Lucas sube su parte y Elisa la revisa B) Solo Lucas se compromete.", "A", "Ambos tienen tareas."),
        ex("¿Qué es una revisión? A) Un momento para comprobar si el acuerdo funciona B) Un castigo si falla.", "A", "Sirve para ajustar."),
        ex("Si el acuerdo no se cumple, ¿qué se hace? A) Volver a conversar con apoyo B) Humillar a quien no cumplió.", "A", "Se busca mejorar y no dañar."),
    ],
    A=[
        ex("¿Cuál acuerdo es observable? A) «Elisa sube sus diapositivas hasta el jueves a las 17:00.» B) «Elisa se esforzará.»", "A", "Tiene conducta, responsable y plazo."),
        ex("Un buen acuerdo tiene cuatro partes: conducta, responsable, plazo y revisión. El acuerdo «Mía envía el resumen el jueves» tiene tres. ¿Cuál parte le falta?", "La revisión", "Tiene responsable (Mía), conducta (envía el resumen) y plazo (el jueves), pero no dice cómo se comprobará que funcionó."),
        ex("Un estudiante amenaza a otro en medio de un acuerdo. ¿Qué se hace? A) Detener y avisar a un adulto del colegio B) Seguir negociando a solas.", "A", "Con amenazas no hay condiciones para acordar."),
    ],
    Z=[
        ex("¿Por qué un acuerdo necesita plazo y revisión?", "Porque permite comprobar si se cumple y corregir a tiempo", "Sin fecha ni control, las intenciones se pierden."),
        ex("Un curso quiere que solo una parte se comprometa. ¿Qué problema tiene? A) No es recíproco ni parejo B) Ninguno.", "A", "Un acuerdo recíproco compromete a ambas partes."),
    ],
    D=[
        arith("Un acuerdo del curso tiene 3 conductas por persona y participan 4 personas. ¿Cuántas conductas observables se acuerdan?", "3*4", "Se multiplican conductas por personas."),
        arith("Un acuerdo se revisa cada 5 días durante 20 días. ¿Cuántas revisiones hay?", "20//5", "Se divide el tiempo total entre los días entre revisiones."),
    ],
    context=[ex("Dos amigas se pelearon por un rumor. Aceptan reunirse con la persona orientadora para acordar qué harán. ¿Qué acuerdo sirve? A) Cada una dejará de decir cosas de la otra y se reunirán el lunes para revisar B) Serán amigas para siempre.", "A", "Tiene conductas, responsables y revisión.")],
    selfcheck=[ex("En Orientación: ¿un acuerdo observable dice qué se hace y cuándo?", "Sí", "Así se puede comprobar."), ex("¿La violencia se arregla entre las partes a solas?", "No", "Hay que avisar a un adulto."), ex("¿Un compromiso recíproco incluye a ambas partes?", "Sí", "Las dos se comprometen.")],
    task=T("Lee el conflicto inventado: Bruno y Mía comparten un trabajo para el jueves. Bruno no ha enviado su parte y Mía le dijo que era un irresponsable. Redacta un acuerdo de cuatro partes (conducta, responsable, plazo, revisión) para cada uno, y una frase para avisar a un adulto si vuelven los insultos.", "Bruno envía su parte el martes a las 18:00; Mía revisa el miércoles; ambos conversan el jueves 5 minutos para ver si funcionó; si hay insultos, se avisa al profesor jefe. Frase: «Volvieron los insultos; necesitamos ayuda para acordar».", ["escribe conductas para ambas partes", "incluye plazo y revisión", "incluye qué se hace si falla", "no humilla a nadie"], ["acuerdo escrito", "texto oral"], ["acuerdos sin plazo", "compromiso de una sola parte"], "Reconoce los acuerdos observables y pregunta cómo se revisaría el cumplimiento."),
    reinforce="Convierte «vamos a colaborar» en un acuerdo con conducta y plazo.",
    extend="Explica por qué un acuerdo recíproco es más justo que uno de una sola parte.",
)
