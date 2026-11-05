"""Cuaderno del estudiante, 2.º medio Orientación: OA 05 (relaciones constructivas e inclusión en redes) y OA 06 (resolución de conflictos en un marco de derechos)."""
from __future__ import annotations

from or_m2_common import M, T, W, lesson
from student_lessons import arith, ex

OA5, OA6 = "OR2M OA 05", "OR2M OA 06"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. El caso del grupo de mensajes de Ema y sus compañeros, personajes inventados, está escrito en la clase y en los ejercicios.",
    "Aprenderé a examinar un caso ficticio de convivencia, presencial o en redes sociales, con cuatro principios: igualdad, dignidad, inclusión y no discriminación. Sirve para reconocer cuándo una relación es constructiva.",
    ["Sé que todas las personas tienen derechos (1.º medio).", "Sé que puedo pedir ayuda a una persona adulta de confianza."],
    [
        "Una relación constructiva es aquella en la que las personas se tratan con respeto y se ayudan a crecer, tanto cara a cara como en redes sociales. Se apoya en cuatro principios. La igualdad es que todas las personas tienen los mismos derechos. La dignidad es que cada persona vale por ser persona. La inclusión es que nadie queda fuera por ser distinto. La no discriminación es que nadie recibe un trato peor por su origen, género, apariencia, creencias u otra característica.",
        "En una red social lo que se escribe queda visible y puede circular rápido. Por eso un comentario o un chiste puede afectar la dignidad de alguien aunque no se diga a la cara. También hay conductas constructivas en línea: felicitar, invitar a un grupo, aclarar un malentendido con respeto o apoyar a quien lo necesita.",
        "Para examinar un caso se separan los hechos, se identifica qué principio se respeta o se vulnera y se piensa quién puede ayudar. Si una situación daña a alguien, la acción siguiente es avisar a una persona adulta de confianza. El análisis se hace con casos inventados, sin nombrar a nadie real.",
    ],
    [("igualdad", "todas las personas tienen los mismos derechos"), ("dignidad", "valor que tiene cada persona por ser persona"), ("inclusión", "que nadie quede fuera por ser distinto"), ("discriminación", "trato peor a alguien por una característica suya"), ("constructivo", "que ayuda a mejorar o a crecer")],
    [
        W("Identificar el principio", "En el grupo de mensajes del curso de Ema nadie responde cuando Bruno, un compañero nuevo, saluda. ¿Qué principio se vulnera?", ["Bruno queda fuera del grupo.", "Nadie lo incluye."], "La inclusión"),
        W("Distinguir lo constructivo", "Dominga escribe: «Bruno, si quieres, te sumamos al equipo de la feria». ¿Es una conducta constructiva?", ["Invita a participar.", "Respeta su dignidad."], "Sí, es constructiva"),
    ],
    [
        M("Pensar que un chiste en línea no daña porque «es broma».", "Se mide solo la intención de quien escribe.", "Mira cómo afecta a la persona: si daña su dignidad, no es una broma válida."),
        M("Creer que discriminar es solo insultar a la cara.", "Se reduce a una forma visible.", "También es excluir, ignorar o tratar peor a alguien por una característica."),
    ],
    R=[
        ex("Todas las personas tienen los mismos derechos. ¿A qué principio corresponde? A) Igualdad B) Inclusión", "A", "La igualdad dice que los derechos son iguales para todos."),
        ex("Ignorar a un compañero nuevo en un grupo de mensajes, ¿vulnera la inclusión? Responde sí o no.", "Sí", "Lo deja fuera del grupo."),
        ex("Invitar a un compañero a sumarse a un equipo, ¿es una conducta constructiva? Responde sí o no.", "Sí", "Lo incluye y lo respeta."),
    ],
    U=[
        ex("Un comentario burlón sobre el cuerpo de una compañera en un chat, ¿qué afecta? A) Su dignidad B) Su horario", "A", "La burla le resta valor como persona."),
        ex("¿Por qué lo escrito en redes puede dañar más rápido? A) Porque queda visible y circula con rapidez B) Porque nadie lo lee", "A", "Más personas pueden verlo."),
        ex("¿Qué es la no discriminación? A) Que nadie reciba un trato peor por una característica suya B) Que todos piensen igual", "A", "Respeta las diferencias sin trato desigual."),
    ],
    A=[
        ex("Clasifica con C (constructiva) o V (vulnera): 1) Felicitar a un compañero por su logro. 2) Excluir a alguien del grupo por su acento. 3) Aclarar con respeto un malentendido. Escribe las letras en orden.", "C, V, C", "La 1 y la 3 cuidan la relación; la 2 discrimina."),
        ex("En un chat de 30 integrantes, 4 se burlan de un compañero y el resto no responde. ¿Cuántos integrantes no se burlan?", "26", "A los 30 se les restan los 4 que se burlan."),
        ex("Si un compañero es tratado peor por su origen, ¿qué principio se vulnera? A) La no discriminación B) El horario", "A", "Se trata distinto por una característica suya."),
    ],
    Z=[
        ex("¿Por qué quedarse callado ante una burla colectiva puede aumentar el daño?", "Porque la víctima siente que nadie la apoya y se refuerza la exclusión", "El silencio colectivo parece aprobar la conducta."),
        ex("Un compañero dice: «Si no se lo digo a la cara, no es discriminar». ¿Qué respondes? A) También se discrimina en redes B) Tienes razón", "A", "El daño existe aunque no sea presencial."),
    ],
    D=[
        arith("En una encuesta anónima de ejemplo, 60 estudiantes responden y 15 dicen haber visto exclusión en un chat. ¿Cuántos no la vieron?", "60-15", "Al total se le restan quienes la vieron."),
        ex("Eres parte del grupo de ejemplo y ves que excluyen a Bruno. ¿Qué acción es más constructiva? A) Invitarlo a una actividad y contarlo a una persona adulta B) Reírte para no quedar fuera", "A", "Incluye a Bruno y busca ayuda adulta."),
    ],
    context=[ex("En una asamblea de curso, una estudiante dice que algunos memes del chat se burlan de la forma de hablar de un compañero. ¿Qué principio debe recordarse? A) Dignidad y no discriminación B) Solo el humor", "A", "El humor no justifica dañar la dignidad.")],
    selfcheck=[ex("En Orientación: ¿la inclusión es que nadie quede fuera por ser distinto?", "Sí", "Es su definición."), ex("¿Una burla en línea puede afectar la dignidad?", "Sí", "Daña a la persona aunque no sea presencial."), ex("¿Hay que avisar a una persona adulta si una situación daña a alguien?", "Sí", "Así se busca ayuda competente.")],
    task=T("Lee el caso inventado: En el chat de un curso, Trinidad publica una foto de una compañera con una frase burlesca por su peso. Varios ponen risas y otros no responden. La compañera deja de ir a clases dos días. Escribe: (1) dos hechos del caso, (2) dos principios vulnerados, (3) una acción constructiva de quienes no se burlaron y (4) a qué persona adulta avisarías.", "Hechos: se publicó una foto con burla; varios rieron y otros callaron. Principios: dignidad y no discriminación. Acción: no reírse, apoyar a la compañera y avisar. Persona adulta: la orientadora o el profesor jefe.", ["escribe dos hechos distintos", "nombra dos principios", "propone una acción constructiva", "indica una persona adulta"], ["texto escrito", "tabla"], ["culpar a la compañera", "no nombrar a una persona adulta"], "Reconoce los hechos separados y pregunta qué haría la persona que calló."),
    reinforce="Escribe tres conductas constructivas en un chat de curso inventado.",
    extend="Explica por qué la igualdad no significa que todos sean iguales, sino que tengan los mismos derechos.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los mensajes y casos de ejemplo están escritos en los ejercicios; los personajes son inventados.",
    "Aprenderé a distinguir hechos, derechos y límites en la convivencia en redes: qué es una opinión, qué es una burla, qué es acoso y qué hacer con una imagen íntima. Sirve para actuar con claridad y protegerme.",
    ["Sé reconocer la igualdad, la dignidad y la inclusión.", "Sé qué es un hecho y qué es un mito."],
    [
        "Una opinión es lo que alguien piensa y se puede debatir con respeto. Una burla repetida o un insulto que busca humillar ya no es opinión: es acoso, que es una conducta repetida que daña a otra persona. Cuando ocurre por internet, se llama ciberacoso. No es necesario que haya golpes para que haya daño, porque la humillación también afecta la salud emocional.",
        "Hay límites que cuidan a todas las personas. Nadie puede publicar fotos tuyas sin permiso, ni pedirte imágenes íntimas, ni amenazarte con difundirlas. Si alguien te manda o te muestra una imagen íntima de otra persona, no la guardes, no la reenvíes y avisa a una persona adulta de confianza. Compartir imágenes íntimas de otra persona es un daño grave a su intimidad.",
        "Si sufres o ves acoso en línea, el protocolo es: no responder con insultos, guardar una captura de pantalla de los mensajes que no sean imágenes íntimas, bloquear a la persona, no borrar el chat y contarlo a una persona adulta de confianza. Todas las personas tienen derecho a una convivencia sin humillación, dentro y fuera de internet.",
    ],
    [("acoso", "conducta repetida que daña a otra persona"), ("ciberacoso", "acoso que ocurre por internet o por redes"), ("opinión", "lo que alguien piensa y se puede debatir"), ("captura de pantalla", "imagen guardada de lo que se ve en una pantalla"), ("imagen íntima", "foto o video privado del cuerpo de una persona")],
    [
        W("Opinión o acoso", "Un estudiante inventado escribe cada día un insulto sobre otra persona en el chat. ¿Es una opinión o acoso?", ["Se repite cada día.", "Busca humillar."], "Es acoso"),
        W("Ordenar el protocolo", "Dominga recibe amenazas por mensaje. ¿Cuál de estas acciones corresponde: responder con insultos, guardar las capturas y avisar a una persona adulta, o borrar todo?", ["Responder con insultos aumenta el conflicto.", "Borrar elimina la prueba.", "Guardar y avisar protege."], "Guardar las capturas y avisar a una persona adulta"),
    ],
    [
        M("Borrar el chat para evitar problemas.", "Se piensa que sin el mensaje desaparece el daño.", "No borres el chat: sirve como evidencia para que una persona adulta ayude."),
        M("Reenviar una imagen íntima para «avisar a otros».", "Se cree que difundirla ayuda.", "No la guardes ni la reenvíes; avisa a una persona adulta de confianza."),
    ],
    R=[
        ex("Un insulto diario para humillar a alguien, ¿es una opinión o acoso?", "Acoso", "Es repetido y busca dañar."),
        ex("Si te llega una imagen íntima de otra persona, ¿la reenvías? Responde sí o no.", "No", "Compartirla daña gravemente su intimidad."),
        ex("¿Se debe borrar el chat donde hay amenazas? Responde sí o no.", "No", "Sirve como evidencia para que adultos ayuden."),
    ],
    U=[
        ex("¿Qué es el ciberacoso? A) Acoso que ocurre por internet B) Una discusión de una vez", "A", "Se repite y daña a través de redes."),
        ex("¿Qué haces con los mensajes de amenaza? A) Guardas una captura y avisas a una persona adulta B) Respondes con amenazas", "A", "Conservas la evidencia y buscas ayuda."),
        ex("¿Por qué la humillación sin golpes también daña? A) Afecta la salud emocional B) No daña", "A", "Las emociones y el ánimo se ven afectados."),
    ],
    A=[
        ex("Clasifica con O (opinión) o A (acoso): 1) «No me gustó la propuesta del curso.» 2) Un meme diario burlándose de un compañero. 3) «Prefiero otra fecha para la feria.» Escribe las letras en orden.", "O, A, O", "La 1 y la 3 son opiniones; la 2 se repite y humilla."),
        ex("Dominga recibe una captura de una conversación donde se burlan de ella. ¿Cuál de estas acciones respeta el protocolo? A) Guardar la captura, bloquear y avisar a una persona adulta B) Reenviar la captura a todo el curso", "A", "Conserva la evidencia sin exponer a nadie y pide ayuda."),
        ex("Un compañero amenaza con difundir una imagen privada de otra persona si no le da dinero. ¿Qué haces? A) Aviso a una persona adulta de confianza B) Lo enfrento por chat", "A", "Es un daño grave y requiere ayuda adulta."),
    ],
    Z=[
        ex("¿Por qué es importante no responder con insultos al ciberacoso?", "Porque responder con insultos puede aumentar el conflicto y dañar la evidencia de quién agrede", "Mantener la calma protege más."),
        ex("Un compañero dice: «Si ya la vieron muchos, da lo mismo reenviarla». ¿Qué respondes? A) Cada reenvío aumenta el daño B) Tienes razón", "A", "Cada difusión suma daño a la persona."),
    ],
    D=[
        arith("En un chat de ejemplo hubo 12 mensajes de burla el lunes, 9 el martes y 14 el miércoles. ¿Cuántos mensajes de burla hubo en total?", "12+9+14", "Se suman los mensajes de los tres días."),
        arith("De 48 estudiantes de un curso inventado, 8 dicen haber visto ciberacoso en el último mes. ¿Cuántos no lo vieron?", "48-8", "Al total se le restan quienes lo vieron."),
    ],
    context=[ex("En un taller de convivencia leen un caso inventado: alguien manda a una compañera un mensaje que dice «si no haces lo que quiero, muestro tu foto». ¿Qué conviene hacer? A) Guardar una captura del mensaje, bloquear y contarlo a una persona adulta B) Hacer lo que pide", "A", "No se cede al chantaje y se pide ayuda adulta.")],
    selfcheck=[ex("En Orientación: ¿acoso es una conducta repetida que daña?", "Sí", "Se repite y busca humillar."), ex("¿Se debe borrar el chat de amenazas?", "No", "Sirve como evidencia de lo ocurrido."), ex("¿Hay que avisar a una persona adulta ante una imagen íntima ajena?", "Sí", "Así se protege a la persona.")],
    task=T("Lee los casos inventados: (a) un estudiante critica con respeto la idea de otro en el chat; (b) un grupo publica cada día un apodo ofensivo de una compañera; (c) alguien recibe una imagen íntima de una persona de otro curso. Para cada uno escribe si es opinión, acoso o riesgo de imagen íntima y qué haría la persona que lo ve, incluyendo avisar a una persona adulta.", "(a) Opinión: se puede debatir con respeto. (b) Acoso: se repite y humilla; guardar capturas, no responder con insultos, bloquear y contarlo a una persona adulta. (c) Imagen íntima: no guardarla ni reenviarla y avisar a una persona adulta de confianza.", ["clasifica los tres casos", "indica qué hacer en (b) y (c)", "incluye a una persona adulta", "no usa nombres reales"], ["tabla escrita", "texto breve"], ["reenviar la imagen", "borrar el chat"], "Reconoce el protocolo y pregunta qué persona adulta sería más cercana."),
    reinforce="Escribe tres pasos del protocolo de ciberacoso con tus palabras.",
    extend="Explica por qué guardar una captura no es lo mismo que difundir una imagen.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. Las tres respuestas posibles a cada caso están escritas en los ejercicios.",
    "Aprenderé a comparar respuestas a una situación de exclusión o de burla, presencial o en línea, y a prever sus consecuencias. Sirve para elegir la que cuida a todas las personas.",
    ["Sé distinguir opinión, acoso y límites.", "Sé el protocolo de ciberacoso."],
    [
        "Quien presencia una situación de exclusión o de burla puede responder de varias maneras. Puede unirse a la burla, mirar sin hacer nada o actuar a favor de la persona afectada. A estas tres posturas se les llama agresor que se suma, espectador y aliado. Cada una tiene consecuencias distintas para la persona afectada, para el grupo y para quien la elige.",
        "Para comparar se usan tres preguntas: ¿protege la dignidad de la persona afectada?, ¿evita que la situación crezca? y ¿conecta con ayuda adulta? Cada sí vale 1 punto. Una respuesta de aliado, como acompañar a la persona, no reírse del comentario y avisar a un adulto, suele sumar los tres puntos.",
        "Ser aliado no significa enfrentarse a golpes ni exponer a nadie. Significa apoyar a la persona afectada, negarse a compartir el contenido dañino y pedir ayuda. Y si ser aliado implica un riesgo para ti, la manera segura es avisar a una persona adulta de confianza.",
    ],
    [("espectador", "persona que ve una situación de burla y no hace nada"), ("aliado", "persona que apoya a quien está siendo dañado"), ("agresor", "persona que daña a otra"), ("negarse a compartir", "no difundir contenido que daña a alguien"), ("consecuencia", "lo que ocurre después de una acción")],
    [
        W("Clasificar la postura", "Colomba ve un meme ofensivo sobre un compañero y no hace nada. ¿Qué postura tiene?", ["Ve la situación.", "No actúa a favor ni en contra."], "Espectadora"),
        W("Puntuar una respuesta", "Colomba decide no compartir el meme, escribirle a su compañero para acompañarlo y contarlo a su profesora. Protege dignidad: sí. Evita que crezca: sí. Conecta con ayuda: sí. ¿Cuántos puntos suma?", ["Hay tres respuestas afirmativas.", "Cada una vale 1 punto."], "3 puntos"),
    ],
    [
        M("Pensar que ser espectador no tiene consecuencias.", "Se cree que no hacer nada es neutral.", "El silencio puede dejar a la persona sin apoyo; elige una acción segura."),
        M("Creer que un aliado debe enfrentarse a quien agrede.", "Se confunde apoyar con pelear.", "Apoya a la persona afectada y avisa a una persona adulta."),
    ],
    R=[
        ex("Quien apoya a la persona afectada es A) un aliado B) un espectador", "A", "El aliado actúa a favor de quien está siendo dañado."),
        ex("Quien ve la burla y no hace nada es un A) espectador B) aliado", "A", "No actúa, solo observa."),
        ex("Una respuesta que sí protege dignidad, sí evita que crezca y sí conecta con ayuda, ¿cuántos puntos suma?", "3", "Hay tres síes."),
    ],
    U=[
        ex("¿Qué puede hacer un aliado sin exponerse? A) Apoyar a la persona y avisar a una persona adulta B) Insultar a quien agrede", "A", "Es una acción segura y respetuosa."),
        ex("¿Por qué compartir el meme ofensivo es una mala opción? A) Porque aumenta el daño a la persona B) Porque gasta datos", "A", "Cada difusión hace crecer la humillación."),
        ex("Un espectador que decide avisar a un adulto, ¿sigue siendo espectador? A) No, pasa a ser aliado B) Sí, igual", "A", "Ya actúa a favor de la persona."),
    ],
    A=[
        ex("Dominga evalúa dos respuestas. (1) Reírse y compartir: dignidad no, crece no, ayuda no. (2) Acompañar y avisar: sí, sí, sí. ¿Cuál tiene más puntos?", "La 2", "La 2 suma 3 y la 1 suma 0."),
        ex("Felipe ve que excluyen a una compañera de un trabajo grupal. ¿Qué respuesta suma más? A) Invitarla a su equipo y contarlo a su profesor B) Mirar y esperar", "A", "Protege su dignidad y conecta con ayuda."),
        ex("En un curso de ejemplo de 32 estudiantes, 5 se burlaron, 3 apoyaron a la persona afectada y el resto miró. ¿Cuántos fueron espectadores?", "24", "A los 32 se les restan los 5 y los 3: 32 − 5 − 3 = 24."),
    ],
    Z=[
        ex("¿Por qué el silencio de muchos puede reforzar la burla?", "Porque quien agrede interpreta el silencio como aprobación y la víctima se siente sola", "La falta de reacción envía un mensaje."),
        ex("Un compañero dice: «Si no me meto, no tengo responsabilidad». ¿Qué respondes? A) Hay acciones seguras para ayudar sin exponerse B) Tienes razón, no tienes ninguna", "A", "Ayudar puede ser tan simple como avisar."),
    ],
    D=[
        arith("De un grupo de ejemplo, 3 respuestas obtienen 3, 1 y 2 puntos. ¿Cuántos puntos suman en total?", "3+1+2", "Se suman los puntos de las tres respuestas."),
        ex("Un aliado en riesgo de ser agredido por apoyar a alguien, ¿qué hace? A) Avisa a una persona adulta de confianza B) Lo enfrenta solo", "A", "Así se protege él también."),
    ],
    context=[ex("En el patio, un grupo se ríe de una estudiante. Una compañera se acerca y le dice «ven con nosotras» y después le cuenta a la inspectora. ¿Qué postura tiene? A) Aliada B) Espectadora", "A", "Apoya y conecta con ayuda adulta.")],
    selfcheck=[ex("En Orientación: ¿un aliado apoya a quien está siendo dañado?", "Sí", "Es su definición."), ex("¿No hacer nada es neutral?", "No", "Puede dejar sola a la persona."), ex("¿Avisar a una persona adulta es una acción segura del aliado?", "Sí", "Protege a todos.")],
    task=T("Lee el caso inventado: En el chat de un curso, Mauricio publica una foto de Sergio con una frase para burlarse de su ropa. Tres estudiantes ríen, cuatro miran y una estudiante, Isabel, no sabe qué hacer. Compara tres respuestas de Isabel con las preguntas de dignidad, crecimiento y ayuda: (1) reírse; (2) mirar; (3) escribirle a Sergio, no compartir la foto y avisar al profesor jefe. Suma los puntos y justifica cuál elige.", "(1) dignidad no, crece no, ayuda no = 0. (2) dignidad no, crece no, ayuda no = 0. (3) sí, sí, sí = 3. Elige la 3 porque protege a Sergio y conecta con una persona adulta.", ["responde las tres preguntas por opción", "suma bien los puntos", "justifica la elección", "incluye a una persona adulta"], ["tabla escrita", "explicación oral"], ["sumar mal", "elegir enfrentar a golpes"], "Reconoce la tabla y pregunta qué haría si el profesor jefe no está."),
    reinforce="Compara dos respuestas posibles a una exclusión inventada con las tres preguntas.",
    extend="Explica la diferencia entre espectador y aliado con un ejemplo inventado.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Los casos de ejemplo de exclusión y de ciberacoso están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura ante discriminación, exclusión o ciberacoso, y a promover relaciones constructivas con acciones concretas. Sirve para actuar sin exponerme ni exponer a nadie.",
    ["Sé comparar respuestas con tres preguntas.", "Sé el protocolo de ciberacoso."],
    [
        "Una acción segura ante una situación de discriminación o ciberacoso protege a la persona afectada, no la expone y conecta con ayuda adulta. Se puede resumir en cinco pasos: no responder con insultos, guardar capturas de los mensajes que no sean imágenes íntimas, bloquear a quien agrede, no borrar el chat y contarlo a una persona adulta de confianza.",
        "Promover relaciones constructivas va más allá de reaccionar. Se puede invitar a un compañero nuevo, usar un lenguaje respetuoso, corregir con calma un comentario discriminatorio y proponer acuerdos de convivencia en el chat del curso, como no compartir fotos de otros sin permiso. Estas acciones previenen problemas antes de que ocurran.",
        "Si el conflicto sube de tono o hay amenazas, se detiene la conversación y se avisa a un adulto. No se necesita ganar una discusión en línea. Cuidar la dignidad de todos importa más que tener la razón. Y si alguien dice sentirse mal por lo que sucede, se le acompaña y se le sugiere hablar con una persona adulta de confianza.",
    ],
    [("acuerdo de convivencia", "regla compartida para tratarse con respeto"), ("prevenir", "actuar antes de que ocurra un problema"), ("bloquear", "impedir que una persona te escriba o te vea en una red"), ("evidencia", "registro que muestra lo que ocurrió"), ("corregir con calma", "señalar un error sin agredir")],
    [
        W("Elegir los pasos", "Isabel recibe mensajes de burla repetidos. ¿Cuál es un orden seguro: guardar captura, bloquear y avisar a un adulto; o responder con insultos y borrar el chat?", ["Responder con insultos aumenta el conflicto.", "Borrar el chat elimina la evidencia.", "El primer orden protege."], "Guardar captura, bloquear y avisar a una persona adulta"),
        W("Prevenir con un acuerdo", "El curso de Isabel acuerda no compartir fotos de otras personas sin permiso. ¿Qué tipo de acción es?", ["Se hace antes de que haya un problema.", "Cuida la dignidad de todos."], "Una acción de prevención"),
    ],
    [
        M("Pensar que hay que ganar la discusión en línea.", "Se cree que quien responde último gana.", "Detén la conversación y avisa a una persona adulta."),
        M("Compartir capturas de acoso con todo el curso.", "Se cree que exponer a quien agrede soluciona.", "Muestra la evidencia solo a una persona adulta de confianza."),
    ],
    R=[
        ex("Bloquear a quien envía mensajes de burla repetidos, ¿es una acción segura? Responde sí o no.", "Sí", "Evita seguir recibiendo el daño."),
        ex("Una captura de pantalla de una amenaza debe mostrarse a A) una persona adulta de confianza B) todo el curso", "A", "Sirve para pedir ayuda sin exponer a nadie más."),
        ex("Proponer no compartir fotos ajenas sin permiso, ¿es prevenir? Responde sí o no.", "Sí", "Actúa antes de que haya daño."),
    ],
    U=[
        ex("¿Qué hace una persona que corrige con calma un comentario discriminatorio? A) Señala el error sin agredir B) Responde con otro insulto", "A", "Cuida la relación mientras defiende un principio."),
        ex("Si la conversación en línea sube de tono con amenazas, ¿qué corresponde? A) Detenerla y avisar a un adulto B) Seguir discutiendo", "A", "Hay riesgo y se necesita ayuda."),
        ex("¿Por qué no se debe difundir la evidencia de acoso? A) Porque expone a las personas y no la protege B) Porque es aburrido", "A", "La evidencia es para quien ayuda, no para el público."),
    ],
    A=[
        ex("Clasifica con S (segura) o N (no segura): 1) Bloquear a quien agrede. 2) Publicar la captura en el chat del curso. 3) Contarlo a una persona adulta de confianza. Escribe las letras en orden.", "S, N, S", "La 1 y la 3 protegen; la 2 expone."),
        ex("Un compañero nuevo, Hugo, almuerza solo. ¿Qué acción promueve relaciones constructivas? A) Invitarlo a tu mesa B) Comentar que es raro", "A", "Incluye y respeta su dignidad."),
        ex("Un grupo de 36 estudiantes forma equipos de 4 para practicar el protocolo. ¿Cuántos equipos hay?", "9", "36 dividido en 4 es 9."),
    ],
    Z=[
        ex("¿Por qué prevenir con acuerdos de convivencia sirve más que solo castigar?", "Porque define cómo tratarse antes del problema y todos saben qué se espera", "La prevención evita el daño."),
        ex("Un compañero dice: «Si corrijo un comentario discriminatorio, me van a excluir». ¿Qué respuesta ayuda? A) Corregir con calma y avisar a un adulto si hay riesgo B) Callarse siempre", "A", "Se puede defender un principio con cuidado."),
    ],
    D=[
        arith("En un chat de ejemplo, 3 de cada 10 mensajes eran burlas. En 50 mensajes, ¿cuántas burlas hubo?", "3*5", "50 mensajes son 5 grupos de 10 y hay 3 burlas en cada grupo."),
        ex("Una compañera de ejemplo te cuenta que sufre ciberacoso y pide guardar el secreto. ¿Qué haces? A) Le explicas que lo cuentas a una persona adulta porque te importa B) Le prometes callar", "A", "Cuidas su seguridad sin dejarla sola."),
    ],
    context=[ex("En una reunión de apoderados y estudiantes, se propone hacer una guía para el chat del curso. ¿Qué regla es constructiva? A) Pedir permiso antes de subir fotos de otras personas B) Que cada uno publique lo que quiera", "A", "Protege la privacidad y la dignidad.")],
    selfcheck=[ex("En Orientación: ¿bloquear a quien agrede es una acción segura?", "Sí", "Frena el daño."), ex("¿Se debe mostrar la evidencia solo a una persona adulta de confianza?", "Sí", "Así se pide ayuda sin exponer."), ex("¿Prevenir es actuar antes del problema?", "Sí", "Evita el daño.")],
    task=T("Escribe una propuesta de tres acuerdos de convivencia para el chat de un curso inventado y un plan de acción segura si alguien recibe burlas. Los acuerdos deben incluir respeto a la dignidad, inclusión y no discriminación. El plan debe tener al menos cuatro pasos y nombrar a una persona adulta.", "Acuerdos: (1) no subir fotos de otros sin permiso; (2) invitar a los compañeros nuevos a los grupos; (3) no usar apodos ofensivos. Plan: no responder con insultos, guardar capturas, bloquear, no borrar el chat y contarlo a la orientadora.", ["escribe tres acuerdos distintos", "incluye dignidad, inclusión y no discriminación", "plan con al menos cuatro pasos", "nombra a una persona adulta"], ["lista escrita", "afiche"], ["acuerdos vagos", "olvidar a la persona adulta"], "Reconoce acuerdos concretos y pregunta cómo los revisarían en un mes."),
    reinforce="Escribe dos acuerdos de convivencia para un chat de grupo de amigos inventado.",
    extend="Explica por qué un acuerdo de convivencia vale si todos lo conocen.",
)

lesson(
    OA5, 5,
    "Una hoja y un lápiz. Los mensajes de ejemplo están escritos en los ejercicios; los personajes son inventados.",
    "Aprenderé a comunicar con respeto un desacuerdo o un malestar, en persona y en un chat, y a pedir ayuda cuando no es suficiente. Sirve para defender mis derechos sin agredir.",
    ["Sé elegir una acción segura.", "Sé armar un mensaje con hecho, emoción y petición."],
    [
        "Una comunicación asertiva dice lo que uno piensa o siente sin agredir y sin quedarse callado. Una forma simple usa tres partes: describir el hecho, expresar cómo me siento con un mensaje en primera persona y pedir un cambio concreto. Por ejemplo: «Cuando subes mi foto sin avisar, me siento incómodo; te pido que primero me preguntes».",
        "En un chat conviene escribir con calma, sin mayúsculas ni insultos, y releer antes de enviar. Si sientes rabia, puedes esperar un rato. Escribir mensajes largos e hirientes casi siempre empeora el conflicto. Un mensaje respetuoso tiene más posibilidades de ser escuchado.",
        "Si el otro no escucha, o si hay amenazas o humillación repetida, el diálogo no basta y se pide ayuda a una persona adulta de confianza. Es una decisión responsable y no una derrota. El Fono Niños 147 puede orientar a adolescentes, siempre junto con el aviso a una persona adulta.",
    ],
    [("asertivo", "que expresa lo que piensa con respeto y sin agredir"), ("mensaje en primera persona", "frase que parte de lo que yo siento, como «me siento…»"), ("petición concreta", "pedido claro de un cambio específico"), ("releer", "volver a leer antes de enviar"), ("agredir", "dañar con palabras o acciones")],
    [
        W("Reescribir con asertividad", "Un mensaje dice: «Eres un pesado, deja de subir mis fotos». ¿Cómo se reescribe en primera persona?", ["Describe el hecho: subió fotos sin avisar.", "Dice lo que siente.", "Pide un cambio."], "«Cuando subes mis fotos sin avisar me siento incómodo; te pido que me preguntes antes»"),
        W("Decidir cuándo pedir ayuda", "Tras tres mensajes respetuosos, el compañero sigue amenazando. ¿Qué corresponde?", ["El diálogo no cambió la situación.", "Hay amenazas."], "Avisar a una persona adulta de confianza"),
    ],
    [
        M("Responder con mayúsculas y gritos escritos.", "Se cree que así se muestra seriedad.", "Escribe con calma y pide un cambio concreto."),
        M("Insistir con el diálogo cuando hay amenazas.", "Se piensa que pedir ayuda es rendirse.", "Si hay amenazas, avisa a una persona adulta de confianza."),
    ],
    R=[
        ex("¿Cuál frase está en primera persona? A) «Me siento incómodo cuando subes mi foto.» B) «Eres un pesado.»", "A", "Parte de lo que yo siento, no de un insulto."),
        ex("Esperar un rato antes de responder cuando sientes rabia, ¿ayuda a escribir con calma? Responde sí o no.", "Sí", "Permite pensar antes de enviar."),
        ex("¿Una petición concreta pide un cambio específico? Responde sí o no.", "Sí", "Dice exactamente lo que se espera."),
    ],
    U=[
        ex("¿Qué incluye una comunicación asertiva? A) Hecho, sentimiento y petición B) Insultos y amenazas", "A", "Expresa sin agredir."),
        ex("¿Por qué conviene releer antes de enviar? A) Para evitar palabras hirientes sin querer B) Para tardar más", "A", "Un mensaje claro y respetuoso se entiende mejor."),
        ex("Ante amenazas repetidas, ¿qué conviene? A) Pedir ayuda a una persona adulta de confianza B) Seguir discutiendo en el chat", "A", "El diálogo no basta si hay amenazas."),
    ],
    A=[
        ex("Ordena con letras las partes: (a) «Te pido que me preguntes antes.» (b) «Subiste mi foto sin avisar.» (c) «Me siento incómodo.» ¿Cuál es el orden hecho, sentimiento, petición?", "b, c, a", "La b es el hecho, la c el sentimiento y la a la petición."),
        ex("Clasifica con A (asertivo) o N (no asertivo): 1) «Me molesta que hables de mí en el chat; prefiero que no lo hagas.» 2) «ERES UN IDIOTA.» 3) «Cuando me interrumpes me siento ignorado; te pido que esperes.» Escribe las letras en orden.", "A, N, A", "La 1 y la 3 expresan sin agredir; la 2 agrede."),
        ex("Un estudiante de ejemplo escribe 5 mensajes respetuosos y recibe 2 respuestas. ¿Cuántos mensajes quedaron sin respuesta?", "3", "A los 5 mensajes se les restan las 2 respuestas."),
    ],
    Z=[
        ex("¿Por qué un mensaje en primera persona tiene más posibilidades de ser escuchado?", "Porque habla de lo que uno siente y no acusa, así la otra persona se defiende menos", "Reduce la reacción defensiva."),
        ex("Un compañero dice: «Ser asertivo es lo mismo que ser agresivo». ¿Qué respondes? A) Asertivo expresa con respeto; agresivo daña B) Son iguales", "A", "La diferencia es el respeto."),
    ],
    D=[
        arith("En un taller de ejemplo, 24 estudiantes ensayan en parejas un mensaje asertivo, 3 veces cada pareja. ¿Cuántos ensayos hay en total?", "12*3", "24 estudiantes forman 12 parejas y cada una ensaya 3 veces."),
        ex("Eres Isabel y un compañero responde a tu mensaje respetuoso con insultos y amenazas. ¿Qué haces? A) Guardo la captura, bloqueo y aviso a una persona adulta B) Respondo con amenazas", "A", "Es una acción segura y no aumenta el conflicto."),
    ],
    context=[ex("Un estudiante de ejemplo quiere decirle a un amigo que le molesta que lo llame con un apodo. ¿Qué frase es más asertiva? A) «Cuando me llamas así me siento mal; prefiero que me digas por mi nombre.» B) «Eres un grosero.»", "A", "Incluye sentimiento y petición sin agredir.")],
    selfcheck=[ex("En Orientación: ¿un mensaje asertivo expresa sin agredir?", "Sí", "Es su característica."), ex("¿Releer antes de enviar ayuda a evitar palabras hirientes?", "Sí", "Permite corregir antes de enviar."), ex("¿Ante amenazas hay que avisar a una persona adulta?", "Sí", "El diálogo no basta.")],
    task=T("Escribe dos mensajes para un chat inventado: (1) un mensaje asertivo con hecho, sentimiento y petición para un compañero que sube fotos de otros sin permiso; (2) un mensaje breve de aviso a una persona adulta de confianza, por si el compañero no cambia y empieza a amenazar. Revisa que no tengan insultos ni mayúsculas y que el segundo incluya hecho, emoción y petición.", "(1) «Cuando subes fotos de otros sin permiso me siento incómodo; te pido que les preguntes antes.» (2) «Necesito hablar contigo. Un compañero sigue subiendo fotos y ahora amenaza. Me siento asustado. Quiero que me ayudes a avisar al colegio.»", ["mensaje 1 con tres partes", "mensaje 2 con hecho, emoción y petición", "sin insultos ni mayúsculas", "nombra a una persona adulta"], ["texto escrito", "ensayo oral"], ["incluir insultos", "olvidar la petición"], "Reconoce los dos mensajes completos y pregunta cómo los diría en persona."),
    reinforce="Reescribe en primera persona la frase inventada «Siempre llegas tarde y me molesta».",
    extend="Explica cuándo el diálogo asertivo deja de ser suficiente y qué se hace entonces.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. El caso de Rosario y Cristóbal, estudiantes inventados, está escrito en la clase y en los ejercicios.",
    "Aprenderé a examinar un conflicto ficticio y a separar las posiciones, los intereses y los derechos de cada parte. Sirve para buscar acuerdos en lugar de ganar una discusión.",
    ["Sé comunicar con respeto un desacuerdo (OA 5).", "Sé que las personas tienen derechos."],
    [
        "Un conflicto es una diferencia entre personas que tienen intereses o necesidades que parecen opuestos. Un conflicto no es lo mismo que violencia: se puede resolver con diálogo. Violencia es cuando alguien daña a otro con golpes, amenazas o humillación. Resolver un conflicto en un marco de derechos significa que ninguna solución puede dañar la dignidad ni la seguridad de nadie.",
        "En todo conflicto hay posiciones, que es lo que cada parte dice que quiere, e intereses, que es la necesidad que hay detrás. Por ejemplo, Rosario dice «quiero la sala de música hoy», y su interés es ensayar para una presentación. Cristóbal también la pide para estudiar. Al mirar los intereses se descubren soluciones que no aparecen si solo se miran las posiciones.",
        "Para examinar un caso conviene anotar los hechos, la posición y el interés de cada parte, y el derecho que protege a cada una. Un acuerdo bueno beneficia a las dos partes y exige un compromiso recíproco, es decir, que cada parte se comprometa a algo. Si hay violencia, no se busca acuerdo entre pares: se avisa a una persona adulta.",
    ],
    [("conflicto", "diferencia entre personas con intereses que parecen opuestos"), ("posición", "lo que una parte dice que quiere"), ("interés", "necesidad que hay detrás de lo que se pide"), ("compromiso recíproco", "cada parte se compromete a algo"), ("marco de derechos", "ninguna solución puede dañar la dignidad ni la seguridad de nadie")],
    [
        W("Posición e interés", "Rosario dice: «Quiero la sala de música hoy». Necesita ensayar para una presentación de mañana. ¿Cuál es su posición y cuál su interés?", ["Lo que pide es la sala.", "Lo que necesita es ensayar."], "Posición: la sala hoy; interés: ensayar para la presentación"),
        W("Conflicto o violencia", "Cristóbal grita y golpea una mesa cuando Rosario habla. ¿Es solo un conflicto?", ["Hay gritos y golpes.", "Hay un riesgo para la seguridad."], "No, hay violencia y se avisa a una persona adulta"),
    ],
    [
        M("Pensar que todo conflicto es violencia.", "Se confunde diferencia con daño.", "Un conflicto se puede resolver con diálogo; la violencia exige avisar a un adulto."),
        M("Buscar solo ganar la discusión.", "Se mira la posición y no el interés.", "Pregunta qué necesita cada parte para buscar un acuerdo."),
    ],
    R=[
        ex("Lo que una parte dice que quiere es su A) posición B) interés", "A", "La posición es lo que se pide en voz alta."),
        ex("La necesidad que hay detrás de lo que se pide es el A) interés B) golpe", "A", "El interés es la razón de fondo."),
        ex("¿Un conflicto es lo mismo que violencia? Responde sí o no.", "No", "El conflicto se puede resolver dialogando."),
    ],
    U=[
        ex("Rosario y Cristóbal quieren la misma sala. ¿Cuál es una solución que mira los intereses? A) Turnarse la sala por horas B) Que gane quien grite más", "A", "Cubre las necesidades de ambos."),
        ex("¿Qué significa un compromiso recíproco? A) Cada parte se compromete a algo B) Solo una cede", "A", "Ambas participan del acuerdo."),
        ex("Si en el conflicto hay amenazas, ¿qué corresponde? A) Avisar a una persona adulta B) Negociar solos", "A", "Hay un riesgo para la seguridad."),
    ],
    A=[
        ex("Clasifica con P (posición) o I (interés): 1) «Quiero la sala de música.» 2) «Necesito ensayar para una presentación.» 3) «Necesito estudiar en un lugar tranquilo.» Escribe las letras en orden.", "P, I, I", "La 1 es lo que piden; la 2 y la 3 son sus necesidades."),
        ex("La sala tiene 4 horas libres: de 15:00 a 19:00. Si Rosario y Cristóbal se reparten el tiempo en partes iguales, ¿cuántas horas tiene cada uno?", "2", "4 horas entre 2 personas son 2 horas cada una."),
        ex("¿Cuál acuerdo respeta los derechos de ambos? A) Turnarse sin insultos ni gritos B) Que uno amenace al otro para decidir", "A", "El acuerdo no daña la dignidad de nadie."),
    ],
    Z=[
        ex("¿Por qué mirar los intereses ayuda a encontrar acuerdos que las posiciones no muestran?", "Porque detrás de posiciones opuestas puede haber necesidades que se pueden cubrir de maneras distintas", "El interés abre más soluciones."),
        ex("Un compañero dice: «En un conflicto siempre hay un ganador». ¿Qué respondes? A) Se puede buscar un acuerdo que beneficie a ambas partes B) Tienes razón", "A", "No siempre es ganar-perder."),
    ],
    D=[
        arith("Un curso de ejemplo tuvo 28 conflictos por turnos en un mes de 4 semanas, repartidos en partes iguales. ¿Cuántos conflictos hubo por semana?", "28//4", "Se divide el total entre las semanas."),
        ex("Cristóbal acepta turnarse, pero quiere que Rosario no le hable mal. ¿Qué compromiso recíproco aparece? A) Respeto mutuo B) Silencio total", "A", "Ambos se comprometen a un trato respetuoso."),
    ],
    context=[ex("En el liceo, dos cursos quieren la misma cancha el viernes. ¿Cuál es el interés más probable de cada curso? A) Jugar o hacer una actividad B) Pelear", "A", "Detrás de pedir la cancha hay una necesidad de actividad.")],
    selfcheck=[ex("En Orientación: ¿un interés es la necesidad detrás de lo que se pide?", "Sí", "Explica por qué se pide."), ex("¿Un conflicto puede resolverse dialogando?", "Sí", "Con respeto y acuerdos."), ex("¿Hay que avisar a un adulto si hay violencia?", "Sí", "Se protege la seguridad.")],
    task=T("Lee el caso inventado: Valentina y Nicolás deben presentar un trabajo juntos. Valentina quiere hacerlo por videollamada porque vive lejos; Nicolás quiere juntarse en la biblioteca porque no tiene buena conexión. Cada uno cree que el otro «no colabora». Escribe: (1) la posición de cada uno, (2) su interés, (3) un derecho que protege a cada uno y (4) un acuerdo posible con un compromiso de cada parte.", "Posiciones: videollamada / biblioteca. Intereses: cumplir sin viajar mucho / trabajar con buena conexión. Derechos: ser escuchada y ser tratado con respeto. Acuerdo: dos reuniones en biblioteca cerca de la casa de Valentina y una por videollamada; ambos aceptan hablarse con respeto.", ["escribe las dos posiciones", "escribe los dos intereses", "nombra un derecho por parte", "propone un acuerdo con compromiso de ambos"], ["tabla escrita", "texto breve"], ["confundir posición con interés", "acuerdo donde solo cede uno"], "Reconoce la tabla clara y pregunta cómo comprobarían si el acuerdo funciona."),
    reinforce="Escribe la posición y el interés de dos personajes inventados que quieren el mismo computador.",
    extend="Explica por qué un acuerdo en que solo una parte cede puede no ser duradero.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. Las frases de ejemplo están escritas en los ejercicios; los personajes son inventados.",
    "Aprenderé a distinguir hechos, derechos y límites en un conflicto: qué se puede discutir, qué no es negociable y qué siempre se respeta. Sirve para conversar sin ceder en lo esencial.",
    ["Sé separar posición e interés.", "Sé que violencia no es conflicto."],
    [
        "En un conflicto hay cosas que se pueden negociar, como los turnos, los horarios o el reparto de tareas. Y hay cosas que no se negocian porque son derechos: la integridad física y emocional, la dignidad, la seguridad y la no discriminación. Nadie puede aceptar un acuerdo a cambio de que lo humillen, lo amenacen o lo discriminen, y nadie puede exigirlo.",
        "Un hecho es lo que se puede comprobar, como «el trabajo estaba a medias el jueves». Una interpretación es lo que alguien supone, como «lo hizo por flojo». Al conversar, conviene hablar de hechos y evitar las etiquetas, porque las etiquetas hieren y cierran el diálogo.",
        "Algunos límites ayudan a cuidar el diálogo: no interrumpir, no gritar, no usar apodos, no hablar de lo privado de otros. Si alguien rompe un límite, se le avisa con calma. Si lo sigue rompiendo y hay riesgo, se pide a una persona adulta que ayude a mediar, que es acompañar el diálogo de forma imparcial.",
    ],
    [("negociable", "que se puede acordar o cambiar"), ("no negociable", "que no se puede ceder porque es un derecho"), ("etiqueta", "palabra que reduce a una persona a un defecto"), ("imparcial", "que no favorece a ninguna parte"), ("mediar", "ayudar a dos partes a dialogar y acordar")],
    [
        W("Negociable o no", "En un conflicto de ejemplo, uno propone que el otro haga más tareas a cambio de no humillarlo. ¿Es negociable?", ["La humillación vulnera la dignidad.", "Un derecho no se negocia."], "No, la dignidad no es negociable"),
        W("Hecho o interpretación", "«Lo entregó el lunes y no el viernes» y «lo hizo por mala voluntad». ¿Cuál es el hecho?", ["La fecha de entrega se comprueba.", "La mala voluntad es una suposición."], "Lo entregó el lunes y no el viernes"),
    ],
    [
        M("Aceptar un trato injusto para evitar la pelea.", "Se piensa que ceder en todo acaba el conflicto.", "Un derecho no se cede; busca otro acuerdo o pide ayuda."),
        M("Usar etiquetas como «flojo» o «mentiroso».", "Se cree que describe un hecho.", "Describe lo que pasó, sin etiquetar a la persona."),
    ],
    R=[
        ex("Los turnos de uso de un espacio, ¿son negociables? Responde sí o no.", "Sí", "Se pueden acordar entre las partes."),
        ex("La dignidad, ¿es negociable? Responde sí o no.", "No", "Es un derecho que no se cede."),
        ex("Un hecho se puede A) comprobar B) solo suponer", "A", "Los hechos se verifican."),
    ],
    U=[
        ex("«Es un flojo» es A) una etiqueta B) un hecho", "A", "Reduce a la persona a un defecto."),
        ex("¿Qué es mediar? A) Ayudar a las partes a dialogar de forma imparcial B) Decidir quién gana", "A", "Quien media no favorece a nadie."),
        ex("Si alguien rompe una regla del diálogo, ¿qué conviene primero? A) Avisarle con calma B) Gritarle", "A", "Se cuida la conversación."),
    ],
    A=[
        ex("Clasifica con N (negociable) o D (derecho): 1) Cambiar el horario de la reunión. 2) Que no te amenacen. 3) Repartir las tareas del trabajo. Escribe las letras en orden.", "N, D, N", "La 1 y la 3 se acuerdan; la 2 es un derecho."),
        ex("Clasifica con H (hecho) o I (interpretación): 1) «El archivo se subió a las 22:00.» 2) «Lo hizo para fastidiar.» 3) «Faltaron dos páginas.» Escribe las letras en orden.", "H, I, H", "La 2 supone una intención."),
        ex("En una reunión, 3 compañeros hablan 2 minutos cada uno sin interrumpirse. ¿Cuántos minutos dura la ronda?", "6", "3 personas por 2 minutos son 6 minutos."),
    ],
    Z=[
        ex("¿Por qué conviene hablar de hechos y no de etiquetas?", "Porque los hechos se pueden comprobar y las etiquetas hieren y cierran el diálogo", "Mantienen el respeto."),
        ex("Un compañero dice: «Si cedo en todo, se acaba el problema». ¿Qué respondes? A) Hay cosas, como los derechos, que no se ceden B) Tienes razón", "A", "No se negocia la dignidad."),
    ],
    D=[
        arith("Un grupo de 5 estudiantes revisa 4 frases de ejemplo cada uno para clasificar hechos e interpretaciones. ¿Cuántas frases revisan en total?", "5*4", "Se multiplica el número de estudiantes por las frases."),
        ex("Una parte pide que un adulto medie porque la otra insulta. ¿Es una decisión adecuada? A) Sí, porque hay un límite roto y riesgo B) No, debe aguantar", "A", "Un adulto puede cuidar el diálogo."),
    ],
    context=[ex("En un trabajo en grupo, un integrante insulta a otro. ¿Qué límite se rompió? A) El respeto a la dignidad B) El horario", "A", "El insulto afecta a la persona.")],
    selfcheck=[ex("En Orientación: ¿los derechos son negociables?", "No", "No se ceden."), ex("¿Una etiqueta describe un hecho?", "No", "Reduce a la persona."), ex("¿Mediar es ayudar de forma imparcial?", "Sí", "No favorece a ninguna parte.")],
    task=T("Lee las frases inventadas: (a) «Me prometiste el borrador el jueves y llegó el sábado»; (b) «Eres un irresponsable»; (c) «Cambiemos el horario de ensayo a las 16:00»; (d) «Si no haces lo que digo, te dejo fuera y subo tu foto». Clasifica cada una como hecho, etiqueta, propuesta negociable o amenaza que vulnera un derecho, y escribe qué harías con la (d).", "(a) Hecho. (b) Etiqueta. (c) Propuesta negociable. (d) Amenaza que vulnera derechos: no se acepta, se guarda la evidencia y se avisa a una persona adulta de confianza.", ["clasifica las cuatro frases", "justifica cada una", "indica qué hacer con la amenaza", "nombra a una persona adulta"], ["tabla escrita", "explicación oral"], ["llamar hecho a una etiqueta", "no actuar ante la amenaza"], "Reconoce la clasificación y pregunta cómo reformularía la etiqueta."),
    reinforce="Reescribe sin etiquetas la frase inventada «Eres un desordenado».",
    extend="Explica por qué ceder en un derecho nunca es parte de un buen acuerdo.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. Las cuatro alternativas y el conflicto de Emilia y Gonzalo, estudiantes inventados, están escritos en los ejercicios.",
    "Aprenderé a comparar alternativas de resolución, como evitar, imponer, ceder, negociar y mediar, según su resultado y su respeto a los derechos. Sirve para elegir una que beneficie a ambas partes.",
    ["Sé separar posición e interés.", "Sé qué es negociable y qué no."],
    [
        "Hay varias formas de responder a un conflicto. Evitar es no hablar del tema. Imponer es lograr lo que uno quiere presionando al otro. Ceder es aceptar todo lo que pide el otro. Negociar es dialogar para llegar a un acuerdo con cesiones de ambas partes. Mediar es pedir a una persona imparcial que ayude a dialogar. La negociación y la mediación son las más recomendables cuando ambas partes buscan un acuerdo.",
        "Para comparar alternativas se usan tres preguntas: ¿respeta los derechos de ambos?, ¿beneficia a las dos partes? y ¿exige un compromiso recíproco? Cada sí vale 1 punto. Imponer casi siempre suma 0 porque pasa por sobre el otro. Ceder en todo puede sumar poco, porque no beneficia a quien cede.",
        "Un acuerdo bueno es específico, posible y se puede evaluar. Dice quién hace qué y cuándo, y cómo se revisará. Si el acuerdo no se cumple, no hay que pelear: se vuelve a conversar, con una persona adulta que medie si hace falta.",
    ],
    [("evitar", "no hablar del conflicto"), ("imponer", "lograr lo que uno quiere presionando al otro"), ("ceder", "aceptar todo lo que pide el otro"), ("negociar", "dialogar para acordar con cesiones de ambas partes"), ("acuerdo específico", "acuerdo que dice quién hace qué y cuándo")],
    [
        W("Reconocer la alternativa", "Emilia y Gonzalo discuten por el uso del proyector. Emilia dice: «Hoy lo uso yo; mañana tú». ¿Qué alternativa propone?", ["Propone un reparto con cesión de ambos.", "Dialoga para acordar."], "Negociar"),
        W("Puntuar", "Imponer: respeta derechos no, beneficia a ambos no, compromiso no. Negociar: sí, sí, sí. ¿Cuál tiene más puntos?", ["Imponer suma 0.", "Negociar suma 3."], "Negociar, con 3 puntos"),
    ],
    [
        M("Creer que evitar el conflicto lo resuelve.", "Se confunde calma con solución.", "El conflicto sigue; conversa para acordar."),
        M("Pensar que ceder en todo es ser buena persona.", "Se confunde amabilidad con renuncia.", "Un buen acuerdo exige compromiso de ambos."),
    ],
    R=[
        ex("Lograr lo que uno quiere presionando al otro es A) imponer B) negociar", "A", "Pasa por sobre el otro."),
        ex("Pedir a una persona imparcial que ayude a dialogar es A) mediar B) evitar", "A", "Esa persona acompaña el diálogo."),
        ex("Un acuerdo de verdad debe beneficiar a las dos partes. Responde sí o no.", "Sí", "Es parte de los criterios."),
    ],
    U=[
        ex("¿Qué tiene de bueno un acuerdo específico? A) Dice quién hace qué y cuándo B) Es largo", "A", "Se puede cumplir y evaluar."),
        ex("Emilia cede todo y se queda sin proyector. ¿Qué criterio falla? A) Beneficia a ambas partes B) Respeta los derechos", "A", "Solo gana una parte."),
        ex("Si el acuerdo no se cumple, ¿qué conviene? A) Volver a conversar, con un adulto si hace falta B) Pelear", "A", "Se revisa sin aumentar el conflicto."),
    ],
    A=[
        ex("Puntúa Mediar: respeta derechos sí, beneficia a ambos sí, compromiso recíproco sí. Evitar: no, no, no. ¿Cuántos puntos más tiene Mediar que Evitar?", "3", "Mediar suma 3 y evitar suma 0."),
        ex("Gonzalo y Emilia acuerdan: «Emilia usa el proyector los lunes y miércoles; Gonzalo martes y jueves; lo revisan el viernes». ¿Es un acuerdo específico? A) Sí, dice quién hace qué y cuándo B) No", "A", "Incluye días, personas y revisión."),
        ex("Clasifica con E (evitar), I (imponer), C (ceder) o N (negociar): 1) «Haz lo que digo o no te hablo.» 2) «Está bien, quédate tú con el proyector siempre y yo no lo uso.» 3) «Probemos turnos y vemos.» Escribe las letras en orden.", "I, C, N", "La 1 presiona, la 2 renuncia y la 3 dialoga para acordar."),
    ],
    Z=[
        ex("¿Por qué evitar puede empeorar un conflicto?", "Porque el problema sigue sin resolver y crece el malestar", "Callar no soluciona las diferencias."),
        ex("Un compañero dice: «Mediar es que otro decida por mí». ¿Qué respondes? A) Quien media ayuda a dialogar, no impone la decisión B) Tienes razón", "A", "Las partes toman sus acuerdos."),
    ],
    D=[
        arith("Un acuerdo de ejemplo reparte 5 días de uso de un espacio: Emilia usa 2 y Gonzalo usa 3. ¿Cuántos días usan entre los dos?", "2+3", "Se suman los días de cada uno."),
        arith("Un grupo de ejemplo prueba 4 alternativas en 3 conflictos distintos. ¿Cuántas comparaciones hacen?", "4*3", "Se multiplican alternativas por conflictos."),
    ],
    context=[ex("Dos amigos de ejemplo discuten por turnos del computador del curso. ¿Qué alternativa conviene? A) Negociar turnos y revisarlos en una semana B) Que uno se lo quede", "A", "Es específica y exige compromiso de ambos.")],
    selfcheck=[ex("En Orientación: ¿negociar exige cesiones de ambas partes?", "Sí", "Es parte de la definición."), ex("¿Imponer respeta los derechos del otro?", "No", "Pasa por sobre el otro."), ex("¿Un acuerdo bueno es específico?", "Sí", "Se puede evaluar.")],
    task=T("Lee el caso inventado: Vicente y Antonia comparten el único día libre de la sala de ensayo del liceo. Vicente quiere el lunes; Antonia también. Compara cuatro alternativas con las tres preguntas (respeta derechos, beneficia a ambos, compromiso recíproco): (1) evitar; (2) imponer; (3) ceder; (4) negociar turnos y revisarlo. Suma los puntos, elige una y escribe el acuerdo con quién, qué y cuándo.", "(1) 0; (2) 0; (3) 1 (respeta derechos, no beneficia a ambos, no compromiso); (4) 3. Elige negociar. Acuerdo: Vicente el lunes y Antonia el miércoles; lo revisan el viernes.", ["responde las preguntas por alternativa", "suma bien los puntos", "elige y justifica", "escribe un acuerdo específico"], ["tabla escrita", "texto breve"], ["sumar mal", "acuerdo sin fechas"], "Reconoce la tabla y pregunta cómo revisarían el acuerdo."),
    reinforce="Escribe un acuerdo específico para repartir el uso de una pelota entre dos amigos inventados.",
    extend="Explica por qué un acuerdo sin compromiso de ambas partes se rompe fácilmente.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. Los conflictos de ejemplo, con y sin amenazas, están escritos en los ejercicios.",
    "Aprenderé a elegir la acción segura según el tipo de conflicto: dialogar si es de intereses, y avisar a una persona adulta si hay violencia, amenazas o riesgo. Sirve para no resolver solo lo que no se puede resolver solo.",
    ["Sé comparar alternativas de resolución.", "Sé que las amenazas no se negocian."],
    [
        "Los conflictos entre pares se pueden resolver con diálogo cuando las partes se respetan y tienen intereses distintos. Si ambas están dispuestas, se negocia o se pide mediación. Los pasos son: calmarse, describir hechos, escuchar los intereses del otro, proponer opciones, escoger una y revisarla después.",
        "Cuando hay violencia, amenazas, humillación repetida o una diferencia de poder grande, el diálogo entre pares no es suficiente y no se debe obligar a las personas a negociar. La acción segura es alejarse, proteger a quien está en riesgo y avisar a una persona adulta de confianza, para que adultos del establecimiento intervengan según sus protocolos.",
        "Nadie debe sentirse culpable por pedir ayuda. Pedirla también protege a quien agrede, porque permite detener la situación antes de que empeore. Y si el conflicto es en línea, se guardan capturas, se bloquea y no se borra el chat. Con estos criterios se decide en cada caso si se dialoga o se acude a un adulto.",
    ],
    [("diferencia de poder", "situación en que una persona tiene más fuerza o influencia que otra"), ("protocolo", "pasos que sigue una institución ante un problema"), ("intervenir", "actuar para detener o resolver una situación"), ("mediación", "diálogo acompañado por una persona imparcial"), ("calmarse", "bajar la rabia antes de hablar")],
    [
        W("Elegir entre dialogar y avisar", "Dos amigos de ejemplo discuten por turnos de la cancha y se hablan con respeto. ¿Dialogan o avisan a un adulto?", ["Hay respeto y solo diferencia de intereses.", "No hay amenazas."], "Pueden dialogar y negociar"),
        W("Reconocer el riesgo", "Un estudiante mayor amenaza a otro más pequeño para quitarle el turno. ¿Qué corresponde?", ["Hay amenazas y diferencia de poder.", "El diálogo entre pares no basta."], "Avisar a una persona adulta"),
    ],
    [
        M("Obligar a negociar a quien es amenazado.", "Se cree que todo conflicto se arregla conversando.", "Si hay amenazas, se protege a la persona y se avisa a un adulto."),
        M("Pensar que pedir ayuda es traicionar al grupo.", "Se confunde lealtad con silencio.", "Pedir ayuda cuida a todos."),
    ],
    R=[
        ex("Un conflicto con respeto y solo intereses distintos, ¿se puede dialogar? Responde sí o no.", "Sí", "No hay violencia ni amenazas."),
        ex("Si hay amenazas, ¿se obliga a negociar? Responde sí o no.", "No", "Se protege a la persona y se avisa a un adulto."),
        ex("¿Qué es una diferencia de poder? A) Que uno tiene más fuerza o influencia que el otro B) Que ambos son amigos", "A", "Esa diferencia puede impedir un diálogo parejo."),
    ],
    U=[
        ex("¿Cuál es el primer paso del diálogo? A) Calmarse B) Gritar", "A", "Bajar la rabia permite escuchar."),
        ex("¿Por qué avisar a un adulto puede proteger también a quien agrede? A) Porque se detiene la situación antes de que empeore B) Porque lo castigan más", "A", "Se frena un daño mayor."),
        ex("Si el conflicto es en línea y con amenazas, ¿qué se hace? A) Guardar capturas, bloquear y contarlo a un adulto B) Borrar el chat", "A", "Se conserva la evidencia y se pide ayuda."),
    ],
    A=[
        ex("Clasifica con D (dialogar) o A (avisar a un adulto): 1) Diferencia sobre turnos con respeto. 2) Un compañero amenaza con golpear. 3) Dos estudiantes pelean por un tema del trabajo en grupo, sin insultos. Escribe las letras en orden.", "D, A, D", "La 2 incluye amenazas; las otras son diferencias de intereses."),
        ex("Ordena los pasos del diálogo: (a) proponer opciones, (b) calmarse, (c) escuchar intereses. ¿Cuál va primero?", "b", "Calmarse permite escuchar y proponer."),
        ex("En una semana de ejemplo, un curso tuvo 9 conflictos: 7 de intereses y el resto con amenazas. ¿Cuántos tenían amenazas?", "2", "A los 9 se les restan los 7 de intereses."),
    ],
    Z=[
        ex("¿Por qué no se debe obligar a dialogar cuando hay una diferencia de poder grande?", "Porque la parte con menos poder no puede hablar con libertad y puede sufrir más daño", "El diálogo parejo requiere igualdad de condiciones."),
        ex("Un compañero dice: «Avisar es de cobardes». ¿Qué respondes? A) Avisar es una decisión responsable que protege B) Tienes razón", "A", "Cuidar a alguien exige a veces ayuda adulta."),
    ],
    D=[
        arith("Un liceo de ejemplo registra 15 conflictos en el semestre. Si 12 se resolvieron con diálogo, ¿cuántos requirieron intervención adulta?", "15-12", "Al total se le restan los resueltos con diálogo."),
        ex("Una estudiante dice que tiene miedo de enfrentarse a un compañero que la amenaza. ¿Qué acción segura sugieres? A) Que lo cuente a una persona adulta de confianza B) Que lo enfrente sola", "A", "Se protege su seguridad."),
    ],
    context=[ex("En el patio, un estudiante le dice a otro «si no me das tu turno, te espero afuera». ¿Qué clase de conflicto es? A) Uno con amenazas, que requiere un adulto B) Uno de simple diferencia de turnos", "A", "La frase incluye una amenaza.")],
    selfcheck=[ex("En Orientación: ¿las amenazas se negocian?", "No", "Vulneran la seguridad."), ex("¿Calmarse es un paso del diálogo?", "Sí", "Ayuda a escuchar."), ex("¿Pedir ayuda cuida a todos?", "Sí", "Frena el daño.")],
    task=T("Lee los dos casos inventados: (A) Paula y Joaquín discuten por quién presenta primero en un trabajo; se hablan con respeto. (B) Iván amenaza a un compañero para que le entregue su tarea y le dice que no cuente. Para cada caso escribe si corresponde dialogar o avisar a un adulto, qué pasos seguirías y a qué persona adulta avisarías en el caso (B).", "(A) Dialogar: calmarse, describir hechos, escuchar intereses, proponer turnos y revisar. (B) Avisar: hay amenaza y silencio impuesto; guardar capturas si es en línea y contarlo a la inspectora, orientadora o profesor jefe.", ["distingue los dos casos", "da pasos para (A)", "elige avisar en (B)", "nombra a una persona adulta"], ["texto escrito", "tabla"], ["obligar a negociar en (B)", "guardar el secreto"], "Reconoce la diferencia entre ambos casos y pregunta por qué no se negocia en (B)."),
    reinforce="Escribe tres señales de que un conflicto necesita a una persona adulta.",
    extend="Explica por qué avisar a una persona adulta no es lo mismo que acusar sin pruebas.",
)
