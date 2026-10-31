"""Cuaderno del estudiante, 7.º básico Orientación: OA 05 (relaciones basadas en derechos) y OA 06 (resolución dialogada de conflictos)."""
from __future__ import annotations

from student_content_or7_a import M, T, W, lesson
from student_lessons import arith, ex

OA5, OA6 = "OR07 OA 05", "OR07 OA 06"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. El chat del 7.º B, curso inventado, y las definiciones de los cuatro principios están escritos en los ejercicios.",
    "Aprenderé qué significan igualdad, dignidad, inclusión y no discriminación, y a usarlos para analizar relaciones presenciales y en redes. Sirve para reconocer cuándo se respetan los derechos de las personas y cuándo no.",
    ["Sé que todas las personas tienen derecho a un trato digno.", "Sé que lo que se publica en línea puede dañar."],
    [
        "Los derechos son cosas que corresponden a toda persona por el solo hecho de serlo. Para analizar una relación, presencial o por redes sociales, sirven cuatro principios. La igualdad significa que todas las personas tienen los mismos derechos, aunque sean distintas. La dignidad es el valor de toda persona, que exige un trato respetuoso. La inclusión es lograr que todos puedan participar en los espacios comunes. La no discriminación es no tratar peor a alguien por su origen, su género, su apariencia, una discapacidad, su religión u otra característica.",
        "Estos principios valen igual en el patio y en un chat. Un grupo de mensajes del curso es un espacio común: si alguien es dejado fuera a propósito, si se ríen de su acento o de su aspecto, o si se difunden fotos suyas para burlarse, se están dañando esos derechos. Un ejemplo ficticio: en el chat del 7.º B, un grupo comparte un audio burlándose de cómo habla una compañera que llegó de otro país. Ella deja de participar y se siente triste.",
        "Cuando no se actúa conforme a los derechos, hay un impacto en el bienestar: la persona puede sentirse sola, ansiosa o sin ganas de ir al colegio. También afecta a quienes miran y no dicen nada, y al clima de todo el curso. Analizar una situación con estos principios ayuda a ver con claridad qué falló y qué se puede hacer.",
    ],
    [("derecho", "cosa que corresponde a toda persona"), ("igualdad", "todas las personas tienen los mismos derechos"), ("dignidad", "valor de toda persona que exige un trato respetuoso"), ("inclusión", "lograr que todos puedan participar"), ("discriminación", "tratar peor a alguien por una característica suya")],
    [
        W("Identificar el principio", "En el chat del 7.º B dejan fuera a una compañera sin explicación. ¿Qué principio se vulnera?", ["Ella no puede participar en el espacio común.", "La inclusión busca que todos participen.", "Se vulnera la inclusión."], "La inclusión"),
        W("Reconocer el impacto", "Tras burlarse de su acento, la compañera deja de hablar en el chat. ¿Qué impacto tiene en su bienestar?", ["Se siente sola y triste.", "Deja de participar.", "Afecta su bienestar emocional y su participación."], "Se siente sola y triste, y deja de participar"),
    ],
    [
        M("Pensar que lo que ocurre en línea no tiene consecuencias reales.", "Se separa lo virtual de lo presencial.", "Los derechos valen en cualquier espacio y el daño es real."),
        M("Creer que discriminar es solo una agresión física.", "Se confunde discriminar con pegar.", "También es excluir, burlarse o tratar peor a alguien por una característica."),
    ],
    R=[
        ex("«Todas las personas tienen los mismos derechos». ¿Es igualdad o inclusión?", "Igualdad", "La igualdad dice que todos tienen los mismos derechos."),
        ex("«Lograr que todos puedan participar». ¿Es inclusión o dignidad?", "Inclusión", "Busca que nadie quede fuera de los espacios comunes."),
        ex("Burlarse del acento de una compañera, ¿es discriminación, sí o no?", "Sí", "La trata peor por una característica suya."),
    ],
    U=[
        ex("¿Por qué un chat del curso es un espacio donde también se deben respetar los derechos?", "Porque es un espacio común", "Los derechos valen en cualquier lugar donde conviven personas."),
        ex("¿Qué es la dignidad: el valor de toda persona o el éxito en las notas?", "El valor de toda persona", "Exige un trato respetuoso para todos."),
        ex("Quien mira una burla y no dice nada, ¿también puede verse afectado, sí o no?", "Sí", "El clima del curso se resiente."),
    ],
    A=[
        ex("Situaciones: 1) dejar fuera a alguien de un grupo; 2) invitar a todos al cumpleaños; 3) reírse del aspecto de una compañera; 4) reenviar una foto para humillar. ¿Cuántas vulneran derechos?", "3", "Las situaciones 1, 3 y 4 dañan; la 2 es inclusiva."),
        ex("Un compañero con muletas no puede subir la escalera del paseo del curso. Opciones: A) Cambiar el recorrido para que todos puedan ir. B) Dejarlo en casa porque «complica».", "A", "Cambiar el recorrido es inclusión; excluirlo discrimina."),
        ex("¿Qué principio se vulnera cuando se difunde una foto para burlarse de alguien?", "La dignidad", "Se trata a la persona sin respeto."),
    ],
    Z=[
        ex("Diego dice: «Era solo una burla en el chat; en la vida real no importa». ¿Qué error hay?", "El daño en línea es real", "Una burla en línea puede afectar tanto como una presencial."),
        ex("¿Por qué excluir a alguien por su apariencia viola dos principios a la vez?", "Porque no respeta su dignidad y lo discrimina", "Lo trata peor y desconoce su valor."),
    ],
    D=[
        arith("Un chat de 30 integrantes tiene a 4 personas que dejan fuera a otra. Además de la persona excluida, ¿cuántas no participan en dejarla fuera?", "30-4-1", "Se restan quienes dejan fuera y la persona excluida."),
        arith("En un análisis ficticio de 12 mensajes, 5 respetan los cuatro principios. ¿Cuántos no los respetan?", "12-5", "Al total se le restan los que sí los respetan."),
    ],
    context=[ex("En un juego en línea, algunos jugadores le dicen a una compañera «no sabes jugar, eres mujer». ¿Qué principio se está vulnerando?", "No discriminación e igualdad", "La tratan peor por su género y niegan que tenga los mismos derechos.")],
    selfcheck=[ex("En Orientación: ¿la inclusión busca que todos participen?", "Sí", "Nadie debe quedar fuera."), ex("¿La discriminación puede ocurrir en un chat?", "Sí", "También en línea."), ex("¿Los derechos valen en espacios virtuales?", "Sí", "Se respetan donde sea.")],
    task=T("Lee el caso inventado de Tomasa: en el chat del curso, un grupo hace un meme con su foto, se ríen de su ropa y la dejan fuera del grupo de trabajo. Escribe el principio que se vulnera en cada acción (meme, burlas, exclusión) y dos efectos en su bienestar.", "Meme: dignidad. Burla de ropa: no discriminación. Exclusión: inclusión. Efectos: se siente sola y no quiere ir al colegio.", ["asocia cada acción con un principio", "nombra dos efectos en el bienestar", "usa lenguaje respetuoso", "no cuenta nada personal"], ["tabla escrita"], ["confundir principios", "decir que no tiene consecuencias"], "Reconoce lo identificado y pregunta qué principio es más difícil de distinguir."),
    reinforce="Escribe un ejemplo para cada principio: igualdad, dignidad, inclusión y no discriminación.",
    extend="Explica por qué el silencio de quienes miran también afecta el clima del curso.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los mensajes de ejemplo y las tarjetas de bromas están escritos en los ejercicios.",
    "Aprenderé a distinguir una broma de una agresión, a reconocer el ciberacoso y a separar hechos, emociones, derechos y límites. Sirve para saber cuándo hay que parar y pedir ayuda.",
    ["Sé que la igualdad, la dignidad, la inclusión y la no discriminación guían las relaciones.", "Sé separar hechos de opiniones."],
    [
        "Una broma es un juego en que todos se ríen, incluida la persona de quien se habla. Una agresión es una conducta que daña a alguien: insultos, burlas que humillan, amenazas o exclusión. La diferencia está en el efecto: si la persona se siente mal y lo dice, o se nota que se aleja, no es broma, aunque haya risas. Además, si se repite y es de varios contra uno, es acoso.",
        "El ciberacoso es el acoso a través de redes o celulares: mensajes crueles repetidos, burlas en grupos, memes humillantes, difusión de fotos o suplantar a alguien con un perfil falso. Se agrava porque queda registrado, puede verlo mucha gente y puede ocurrir a cualquier hora. Para analizarlo, separa cuatro cosas: el hecho (qué se escribió o publicó y cuántas veces), la emoción (cómo se siente quien lo recibe), el derecho vulnerado (dignidad, no discriminación) y el límite (lo que se debe parar).",
        "Quien recibe mensajes crueles tiene derecho a pedir que paren, a no responder con agresión y a pedir ayuda. Quien los envía debe parar y reparar, es decir, disculparse y corregir lo que hizo. Cuando un caso se repite o hay amenazas, es un asunto del equipo de convivencia escolar y de los adultos.",
    ],
    [("broma", "juego en que todos se ríen, incluida la persona de quien se habla"), ("agresión", "conducta que daña a otra persona"), ("acoso", "agresión repetida de uno o más contra una persona"), ("ciberacoso", "acoso a través de redes sociales, mensajes o celulares"), ("reparar", "disculparse y corregir el daño que se hizo")],
    [
        W("Distinguir broma y agresión", "Un grupo ríe de Matías, que dice «no me gusta» y se aleja. ¿Es broma o agresión?", ["Él dijo que no le gusta.", "Se aleja: se siente mal.", "Es una agresión."], "Una agresión"),
        W("Analizar un caso de ciberacoso", "Durante tres días un grupo envía a Fernanda memes con su foto. Ella dice que se siente humillada. Nombra el hecho, la emoción y el derecho.", ["Hecho: memes con su foto durante tres días.", "Emoción: humillación.", "Derecho: dignidad."], "Hecho: memes por tres días. Emoción: humillación. Derecho: dignidad"),
    ],
    [
        M("Pensar que si hay risas, es broma.", "Se mide por las risas y no por el efecto.", "Una broma lo es si todos, incluida la persona, se ríen."),
        M("Creer que el ciberacoso no es grave porque no hay golpes.", "Se asocia el daño solo a lo físico.", "Los mensajes crueles dañan el bienestar y pueden repetirse."),
    ],
    R=[
        ex("Una broma, ¿la disfruta también la persona de quien se habla, sí o no?", "Sí", "Si no, deja de ser broma."),
        ex("Memes humillantes enviados varias veces, ¿son broma o ciberacoso?", "Ciberacoso", "Es una agresión repetida en línea."),
        ex("Si alguien dice «no me gusta» y sigues, ¿estás bromeando o agrediendo?", "Agrediendo", "Se debe parar cuando la persona lo pide."),
    ],
    U=[
        ex("¿Por qué el ciberacoso puede ser más grave que una burla presencial?", "Porque queda registrado y puede verlo mucha gente", "Se difunde más y puede ocurrir a cualquier hora."),
        ex("¿Qué debe hacer quien envió mensajes crueles: seguir o reparar?", "Reparar", "Debe disculparse y corregir el daño."),
        ex("¿Una amenaza en un chat se debe contar a un adulto, sí o no?", "Sí", "Es un asunto grave."),
    ],
    A=[
        ex("Mensajes: 1) «Qué buen gol»; 2) «Eres un asco, nadie te quiere»; 3) un meme humillante; 4) «¿Vamos al parque?». ¿Cuántos son agresiones?", "2", "El 2 y el 3 humillan; el 1 y el 4 son amables."),
        ex("Fernanda recibe amenazas por mensaje. Opciones: A) Guardar capturas y avisar a un adulto. B) Responder con insultos para defenderse.", "A", "Las capturas son evidencia y un adulto puede actuar; insultar escala el conflicto."),
        ex("Un grupo repite un chiste sobre el acento de un compañero. Él dice «ya basta». ¿Qué corresponde al grupo?", "Parar y disculparse", "Su límite debe respetarse."),
    ],
    Z=[
        ex("Pablo dice: «Solo era una broma, él se lo toma a mal». ¿Qué error hay en esa frase?", "Pone la culpa en quien se siente mal", "Si el otro se siente mal, el efecto de la acción es lo que importa."),
        ex("¿Por qué conviene separar hecho y emoción al analizar un caso de ciberacoso?", "Para describir lo ocurrido sin opinar y reconocer lo que siente la persona", "Así se ve con claridad qué pasó y cómo afectó."),
    ],
    D=[
        ex("Una persona recibió 20 mensajes crueles repartidos en 5 días, de las mismas 3 personas. ¿Es una burla puntual o ciberacoso?", "Ciberacoso", "Es una agresión repetida de varios contra una persona."),
        arith("De 25 mensajes de un chat, 8 fueron agresivos. ¿Cuántos no lo fueron?", "25-8", "Al total se le restan los agresivos."),
    ],
    context=[ex("En el grupo del curso, alguien crea un perfil falso con el nombre de una compañera para escribir cosas ofensivas. ¿Qué es esto?", "Suplantación, una forma de ciberacoso", "Finge ser otra persona para dañarla.")],
    selfcheck=[ex("En Orientación: ¿si hay risas ya es broma?", "No", "Importa el efecto."), ex("¿Una agresión repetida en línea es ciberacoso?", "Sí", "Se agrava por el registro."), ex("¿Quien recibe agresión debe responder con agresión?", "No", "Debe pedir ayuda.")],
    task=T("Lee el caso inventado de Tomás: durante una semana, un grupo le manda memes con su foto y apodos. Él dice que lo deje y siguen. Escribe el hecho, la emoción, el derecho vulnerado, el límite y qué debería hacer el grupo.", "Hecho: memes y apodos por una semana. Emoción: humillación. Derecho: dignidad. Límite: ya dijo basta. El grupo debe parar, disculparse y reparar.", ["separa hecho, emoción, derecho y límite", "dice qué debe hacer el grupo", "no culpa a Tomás", "no cuenta nada personal"], ["texto escrito"], ["justificar como broma", "no mencionar al grupo"], "Reconoce el análisis y pregunta qué pasaría si Tomás no pudiera decir basta."),
    reinforce="Anota tres mensajes de ejemplo y clasifica cuáles son broma y cuáles agresión.",
    extend="Explica por qué reparar es más que decir «perdón» una vez.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. Las tarjetas de opciones del grupo del 7.º C, curso inventado, están escritas en los ejercicios.",
    "Aprenderé a comparar las opciones de quienes ven una situación de discriminación o ciberacoso y a anticipar sus consecuencias. Sirve para elegir un rol que proteja a las personas.",
    ["Sé distinguir broma y agresión.", "Sé que quien mira también influye."],
    [
        "Cuando ocurre una agresión, hay varios roles. Está quien agrede, quien la recibe y quienes miran, llamados testigos. Los testigos tienen opciones: reírse y reenviar, ignorar, acompañar a la persona, pedir que paren (si te sientes seguro o segura) y avisar a un adulto. Cada opción tiene consecuencias. Reírse y reenviar anima a quien agrede y amplía el daño. Ignorar deja sola a la persona. Acompañar y avisar protege y puede detener la situación.",
        "A veces da miedo actuar porque se teme ser el siguiente blanco. Es válido sentir miedo. Por eso hay formas de ayudar que no te exponen: escribirle a la persona un mensaje privado de apoyo, no reaccionar a las publicaciones dañinas, guardar capturas y contarle a un adulto de confianza. No siempre es necesario enfrentar al grupo.",
        "También hay consecuencias para quien agrede: sanciones escolares, pérdida de confianza y, si el caso es grave, consecuencias legales. Quien comparte material humillante también participa del daño. Elegir bien como testigo es una forma de cuidar el clima del curso y de ejercer tus derechos y deberes.",
    ],
    [("testigo", "persona que ve una agresión sin ser quien agrede ni quien la recibe"), ("acompañar", "estar al lado de alguien para apoyarlo"), ("amplificar", "hacer que el daño llegue a más personas"), ("sanción", "castigo por una conducta que daña a otros"), ("clima del curso", "ambiente de convivencia entre los estudiantes")],
    [
        W("Anticipar la consecuencia", "Ante un meme humillante, Camilo lo reenvía riendo. ¿Qué consecuencia tiene?", ["Lo recibe más gente.", "La persona queda más expuesta.", "Amplía el daño."], "Amplía el daño"),
        W("Elegir un rol protector", "Valentina ve que humillan a una compañera en el chat y le da miedo enfrentar al grupo. ¿Qué puede hacer sin exponerse?", ["Escribirle a la compañera en privado.", "Guardar capturas.", "Contárselo a un adulto de confianza."], "Apoyarla en privado, guardar capturas y avisar a un adulto"),
    ],
    [
        M("Pensar que ignorar una agresión no hace daño.", "Se cree que no actuar es neutral.", "Ignorar deja sola a la persona y mantiene el problema."),
        M("Creer que avisar a un adulto es soplonear.", "Se confunde cuidar con traicionar.", "Avisar protege a la persona y puede detener la agresión."),
    ],
    R=[
        ex("Reenviar un meme humillante, ¿ayuda o amplía el daño?", "Amplía el daño", "Lo ven más personas."),
        ex("Escribirle un mensaje privado de apoyo a quien sufre acoso, ¿ayuda, sí o no?", "Sí", "La persona se siente acompañada."),
        ex("Avisar a un adulto de confianza, ¿es una opción protectora, sí o no?", "Sí", "Un adulto puede actuar para detenerlo."),
    ],
    U=[
        ex("¿Por qué dar miedo actuar es normal y no te hace cobarde?", "Porque temer ser el siguiente blanco es una emoción válida", "Hay formas de ayudar que no te exponen."),
        ex("¿Qué consecuencia puede tener quien agrede: sanciones o felicitaciones?", "Sanciones", "Dañar a otros puede traer consecuencias escolares y legales."),
        ex("Quien comparte material humillante, ¿participa del daño, sí o no?", "Sí", "Lo amplía a más personas."),
    ],
    A=[
        ex("Roles: 1) reírse y reenviar; 2) ignorar; 3) apoyar en privado y avisar a un adulto; 4) pedir ayuda a un adulto del colegio. ¿Cuántas opciones protegen?", "2", "La 3 y la 4 protegen; la 1 y la 2 no."),
        ex("Una amiga recibe burlas y te cuenta, pero te pide no decir nada. Opciones: A) Acompañarla y ayudarla a hablar con un adulto. B) Prometer silencio total.", "A", "Un secreto que mantiene el daño no ayuda."),
        ex("Lucas dice que no reaccionará a las publicaciones que humillan. ¿Es una decisión protectora, sí o no?", "Sí", "Evita amplificar el daño."),
    ],
    Z=[
        ex("Teresa dice: «Si no hago nada, no me meto en problemas». ¿Qué problema tiene ese razonamiento?", "La persona queda sola y el daño sigue", "No actuar mantiene la situación."),
        ex("¿Por qué comparar roles de testigo antes de actuar ayuda a decidir mejor?", "Porque muestra consecuencias distintas", "Permite elegir el que más protege."),
    ],
    D=[
        arith("En un chat, 24 estudiantes ven un meme humillante y 9 lo reenvían. ¿Cuántos no lo reenvían?", "24-9", "Al total se le restan los que lo reenvían."),
        ex("Ana ve un meme humillante y no lo reenvía, pero tampoco hace nada más. ¿Qué paso más podría dar para proteger a la persona?", "Apoyarla en privado o avisar a un adulto", "No reenviar evita amplificar, pero acompañar y avisar protege."),
    ],
    context=[ex("En una videollamada del curso, alguien comparte la pantalla con un meme de una compañera. Algunos ríen y otros apagan la cámara. ¿Cuál es una opción protectora?", "Avisar a un adulto y apoyar en privado a la compañera", "Un adulto puede detener la difusión y el apoyo privado no te expone.")],
    selfcheck=[ex("En Orientación: ¿ignorar una agresión es una opción protectora?", "No", "Deja sola a la persona."), ex("¿Puedo apoyar a alguien en privado?", "Sí", "Es una forma segura de ayudar."), ex("¿Avisar a un adulto es soplonear?", "No", "Es una forma de cuidar a otros.")],
    task=T("Lee el caso inventado del 7.º C: un grupo comparte un video de Ignacio tropezando en el patio con el texto «el torpe». Compara tres roles de testigo: reírse y reenviar, ignorar, y apoyar a Ignacio y avisar a un adulto. Escribe la consecuencia de cada uno y elige uno.", "Reenviar: amplía el daño. Ignorar: lo deja solo. Apoyar y avisar: protege y puede detener. Elige apoyar y avisar.", ["escribe una consecuencia por cada rol", "elige y justifica", "propone una forma segura de actuar", "no cuenta nada personal"], ["tabla escrita"], ["no ver consecuencias", "elegir reírse"], "Reconoce la tabla y pregunta cómo actuaría si tuviera miedo."),
    reinforce="Anota tres formas de ayudar a alguien que sufre acoso en línea sin exponerte.",
    extend="Explica por qué el rol de testigo es una elección y no un hecho neutral.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. El caso de Antonia y la lista de pasos de protección están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura ante discriminación, ciberacoso o contacto riesgoso en línea. Sirve para protegerme y apoyar a otros sin empeorar la situación.",
    ["Sé comparar roles de testigo.", "Sé que debo avisar a un adulto de confianza."],
    [
        "Ante un caso de ciberacoso o discriminación en línea, una acción segura tiene seis pasos. Primero, no respondas con agresión, porque puede empeorar el conflicto. Segundo, guarda evidencia: toma capturas de pantalla con fecha, nombre de usuario y mensaje. Tercero, bloquea a la persona que agrede. Cuarto, reporta el mensaje o perfil a la plataforma. Quinto, avisa a un adulto de confianza: familia, profesor jefe o equipo de convivencia escolar. Sexto, cuida tu bienestar y pide apoyo emocional si lo necesitas.",
        "No borres todo antes de mostrarlo. Las capturas ayudan a los adultos a actuar. Y no reenvíes el material dañino ni siquiera para mostrarlo a otros; muéstralo solo al adulto que ayuda. Si el material incluye imágenes íntimas de una persona menor de edad, avisa de inmediato a un adulto y no lo guardes ni lo compartas.",
        "También existe el riesgo del contacto con adultos desconocidos que fingen ser jóvenes. Si un perfil te pide fotos, datos, o encontrarse a solas, no respondas, bloquea, no borres el chat y avisa a un adulto. La responsabilidad nunca es de quien recibe esos mensajes. Pedir ayuda es una decisión valiente.",
    ],
    [("evidencia", "prueba, como una captura de pantalla"), ("bloquear", "impedir que alguien me escriba"), ("reportar", "avisar a la plataforma que algo es dañino"), ("captura de pantalla", "imagen de lo que se ve en la pantalla"), ("perfil falso", "cuenta que finge ser otra persona")],
    [
        W("Ordenar los pasos", "Antonia, una estudiante inventada, recibe insultos en un chat. ¿Qué hace primero: responder con insultos o guardar capturas?", ["Responder puede empeorar el conflicto.", "Guardar evidencia sirve para pedir ayuda.", "Primero guarda las capturas."], "Guardar capturas de pantalla"),
        W("Responder a un perfil sospechoso", "Un perfil con foto de adolescente le pide a Antonia que se encuentren a solas. ¿Qué hace?", ["Puede ser un perfil falso.", "Pide un encuentro a solas.", "Debe bloquear, no borrar el chat y avisar a un adulto."], "Bloquear, no borrar el chat y avisar a un adulto"),
    ],
    [
        M("Pensar que borrar el chat resuelve el problema.", "Se pierde la evidencia que ayuda a los adultos a actuar.", "Guarda capturas antes de bloquear."),
        M("Creer que reenviar el mensaje dañino a un amigo para mostrarlo está bien.", "Se amplifica el daño.", "Muéstralo solo al adulto que ayuda."),
    ],
    R=[
        ex("¿Se debe responder a una agresión con otra agresión, sí o no?", "No", "Empeora el conflicto."),
        ex("Una captura de pantalla, ¿sirve como evidencia, sí o no?", "Sí", "Muestra lo que se escribió."),
        ex("Un perfil desconocido que pide verse a solas, ¿es una señal de alerta, sí o no?", "Sí", "Puede ser un adulto que finge ser joven."),
    ],
    U=[
        ex("¿Por qué conviene guardar capturas antes de bloquear?", "Porque son evidencia para los adultos", "Sin ellas es más difícil comprobar lo ocurrido."),
        ex("¿Qué significa reportar un perfil: avisar a la plataforma o borrar mi cuenta?", "Avisar a la plataforma", "Permite que la plataforma revise la cuenta."),
        ex("Si recibes una imagen íntima de un menor, ¿la reenvías o avisas a un adulto?", "Avisas a un adulto", "Reenviarla es grave y daña más."),
    ],
    A=[
        ex("Pasos: 1) bloquear; 2) guardar capturas; 3) responder con insultos; 4) avisar a un adulto. ¿Cuántos son acciones seguras?", "3", "Bloquear, guardar capturas y avisar protegen; insultar no."),
        ex("Un compañero amenaza a Antonia por mensajes. Opciones: A) Mostrar las capturas a su profesora jefe. B) Borrar todo para olvidarlo.", "A", "Mostrar la evidencia permite a un adulto actuar."),
        ex("Un perfil desconocido le pide a Antonia su dirección. ¿Qué hace? A) La da porque parece amable. B) Bloquea y avisa a un adulto.", "B", "Dar datos expone a riesgos."),
    ],
    Z=[
        ex("Marcelo dice: «Si bloqueo, no hay prueba». ¿Cómo evita ese problema?", "Guardando capturas antes de bloquear", "Así conserva la evidencia."),
        ex("¿Por qué la responsabilidad nunca es de quien recibe los mensajes peligrosos?", "Porque la responsabilidad es de quien los envía", "Quien agrede o acosa decide hacerlo."),
    ],
    D=[
        ex("Antonia guardó capturas pero no anotó cuándo ocurrió cada mensaje. ¿Qué dato le falta para que la evidencia sea más útil?", "La fecha de cada mensaje", "Con la fecha, los adultos pueden ordenar lo ocurrido."),
        arith("De 20 mensajes recibidos, 7 eran agresivos. ¿Cuántos no lo eran?", "20-7", "Al total se le restan los agresivos."),
    ],
    context=[ex("Un grupo del curso crea un chat para burlarse de un compañero. Tú ves el chat. ¿Cuál es el mejor primer paso?", "Guardar capturas y avisar a un adulto", "Protege al compañero y da evidencia.")],
    selfcheck=[ex("En Orientación: ¿debo guardar evidencia antes de bloquear?", "Sí", "Ayuda a los adultos."), ex("¿Puedo avisar a un adulto si recibo mensajes riesgosos?", "Sí", "Es una acción segura."), ex("¿La responsabilidad es de quien recibe los mensajes?", "No", "Es de quien los envía.")],
    task=T("Lee el caso inventado de Joaquín: en un chat del curso le escriben «eres un asco» y lo amenazan con subir una foto suya. Escribe los seis pasos de acción segura que Joaquín puede seguir en su caso y a qué adulto se lo contaría.", "1) No responder con agresión. 2) Guardar capturas. 3) Bloquear. 4) Reportar. 5) Avisar a su profesora jefe o al equipo de convivencia. 6) Pedir apoyo emocional.", ["escribe los pasos", "nombra a un adulto", "incluye evidencia", "no cuenta nada personal"], ["lista ordenada"], ["responder con insultos", "borrar la evidencia"], "Reconoce la lista y pregunta cuál paso le costaría más."),
    reinforce="Anota los seis pasos de una acción segura en tus palabras.",
    extend="Explica por qué guardar evidencia ayuda a los adultos a proteger a una persona.",
)

lesson(
    OA5, 5,
    "Una hoja y un lápiz. Las frases de apoyo y el guion de conversación están escritos en los ejercicios.",
    "Aprenderé a decir frases que defienden los derechos de alguien y a conversar con adultos para pedir ayuda. Sirve para intervenir con respeto y buscar apoyo en el colegio.",
    ["Sé elegir acciones seguras ante el ciberacoso.", "Sé comparar roles de testigo."],
    [
        "Defender los derechos de otro no requiere pelear. Puedes usar frases breves, tranquilas y firmes. Por ejemplo: «Eso no está bien», «No me gusta que hables así de él», «Dejemos de reenviar eso» o «Vamos a hablar con la profesora». También puedes sacar a la persona de la situación: invitarla a otro grupo o a conversar. Estas frases muestran que los derechos importan y que el grupo no está de acuerdo con el daño.",
        "Si la situación es más compleja, necesitas ayuda de adultos. Dentro del colegio, el equipo de convivencia escolar, el profesor jefe, orientación o dirección tienen obligación de actuar. Cuando hables con ellos, prepara lo que dirás: qué ocurrió (hechos), desde cuándo, cómo afecta a la persona y qué evidencia tienes. Pide que se tomen medidas para proteger a la persona afectada y a quien denuncia.",
        "Después de una agresión, la reparación es importante. Quien agredió puede pedir disculpas sinceras, comprometerse a no repetirlo y reparar el daño, por ejemplo borrando lo publicado. La persona afectada decide si acepta las disculpas. Un curso que cuida a todos construye un clima donde cada uno se siente seguro.",
    ],
    [("denunciar", "avisar a una autoridad que ocurrió algo dañino"), ("convivencia escolar", "área del colegio que cuida el buen trato entre estudiantes"), ("medida de protección", "acción para evitar que el daño continúe"), ("disculpa sincera", "reconocer el daño y comprometerse a no repetirlo"), ("reparación", "acciones para corregir el daño causado")],
    [
        W("Elegir una frase de defensa", "Ante un chiste sobre el acento de Dayana, ¿cuál frase defiende sin agredir: «Eso no está bien» o «Eres un pesado»?", ["La primera señala el problema sin atacar.", "La segunda insulta.", "La primera es la correcta."], "«Eso no está bien»"),
        W("Preparar una conversación con un adulto", "Camila quiere contar a la profesora jefe que hay un chat que humilla a un compañero. ¿Qué datos lleva?", ["Qué ocurrió.", "Desde cuándo.", "Qué evidencia tiene."], "Qué ocurrió, desde cuándo y capturas como evidencia"),
    ],
    [
        M("Creer que defender a otro exige pelear.", "Se confunde defensa con violencia.", "Una frase breve y firme es suficiente; puedes buscar a un adulto."),
        M("Pensar que una disculpa rápida arregla todo.", "Se omite reparar el daño.", "Una disculpa sincera incluye reconocer, comprometerse y reparar."),
    ],
    R=[
        ex("«Eso no está bien», ¿es una frase firme y respetuosa, sí o no?", "Sí", "Señala el problema sin atacar."),
        ex("El equipo de convivencia escolar, ¿puede ayudar en casos de ciberacoso, sí o no?", "Sí", "Tiene la tarea de cuidar el buen trato."),
        ex("Una reparación, ¿puede incluir borrar lo publicado, sí o no?", "Sí", "Corrige parte del daño."),
    ],
    U=[
        ex("¿Por qué conviene llevar capturas cuando hablas con un adulto?", "Porque muestran lo ocurrido", "Son evidencia de lo que pasó."),
        ex("¿Quién decide si acepta una disculpa: la persona afectada o el grupo?", "La persona afectada", "Es quien fue dañada."),
        ex("¿Qué es mejor para defender a alguien: gritar al agresor o decir con calma «eso no está bien»?", "Decir con calma «eso no está bien»", "La calma evita escalar el conflicto."),
    ],
    A=[
        ex("Frases: 1) «Dejemos de reenviar eso»; 2) «Te lo mereces»; 3) «Vamos a hablar con la profesora»; 4) «Cállate, tonto». ¿Cuántas defienden sin agredir?", "2", "La 1 y la 3 defienden; las otras agreden."),
        ex("Un compañero que agredió dice «perdón» y sigue publicando. ¿Es una disculpa sincera, sí o no?", "No", "No cumple con dejar de hacerlo ni reparar."),
        ex("Valentina quiere contar un caso grave a un adulto. Opciones: A) Pedir una reunión con convivencia escolar y llevar capturas. B) Contárselo solo a una amiga.", "A", "Convivencia escolar puede actuar con medidas de protección."),
    ],
    Z=[
        ex("Gabriel dice: «Si hablo, me van a hacer lo mismo». ¿Qué le aconsejas?", "Pedir al adulto medidas de protección y reserva sobre quién avisó", "Un adulto puede cuidar a quien denuncia."),
        ex("¿Por qué una disculpa sin cambio de conducta no repara?", "Porque el daño continúa", "Reparar es dejar de hacerlo y corregir."),
    ],
    D=[
        arith("Convivencia escolar recibió 32 reportes en un semestre y 5 siguen abiertos. ¿Cuántos ya se cerraron?", "32-5", "Al total se le restan los que siguen abiertos."),
        ex("Un grupo se niega a borrar una publicación humillante y dice «ya pasó». ¿Qué debe hacer la persona afectada o quien la apoya?", "Pedir ayuda a convivencia escolar", "El daño continúa mientras la publicación siga disponible."),
    ],
    context=[ex("Un compañero extranjero recibe burlas por su comida. En clase, Pía dice: «Eso no está bien; todos tenemos derecho a comer lo que comemos». ¿Qué hizo Pía?", "Defendió con una frase firme y respetuosa", "No agredió y puso límite al comentario.")],
    selfcheck=[ex("En Orientación: ¿puedo defender a alguien con una frase firme?", "Sí", "Se puede defender sin pelear."), ex("¿La convivencia escolar puede tomar medidas de protección?", "Sí", "Es su labor."), ex("¿Una disculpa sincera incluye reparar?", "Sí", "Y comprometerse a no repetirlo.")],
    task=T("Escribe un guion de tres líneas para el caso inventado de Rocío, a quien un grupo humilla en un chat por su apariencia. Línea 1: una frase firme y respetuosa que diría una compañera testigo. Línea 2: lo que la testigo o Rocío diría a la profesora jefe con hechos, desde cuándo y evidencia. Línea 3: una reparación posible del grupo.", "1) «Eso no está bien; dejemos de reenviar eso». 2) «Hace una semana circulan memes de Rocío; tengo capturas». 3) Borrar los memes y pedir disculpas sinceras.", ["incluye una frase firme", "incluye hechos, fecha y evidencia", "propone una reparación", "no cuenta nada personal"], ["guion escrito"], ["usar insultos", "no mencionar evidencia"], "Reconoce el guion y pregunta qué cambiaría si el grupo se negara."),
    reinforce="Escribe dos frases firmes y respetuosas para defender a alguien.",
    extend="Explica la diferencia entre decir «perdón» y reparar.",
)

lesson(
    OA5, 6,
    "Una hoja y un lápiz. Los tres casos nuevos están escritos en los ejercicios. No cuentes experiencias personales.",
    "Aprenderé a aplicar los principios de igualdad, dignidad, inclusión y no discriminación en casos distintos sin exponerme. Sirve para decidir con criterio en situaciones nuevas, presenciales o virtuales.",
    ["Sé analizar un caso con los cuatro principios.", "Sé elegir acciones seguras y pedir ayuda."],
    [
        "Transferir es usar lo aprendido en un caso nuevo. Para analizar cualquier situación entre personas, haz cuatro preguntas. ¿Qué hecho ocurrió y dónde? ¿Se respetaron la igualdad, la dignidad, la inclusión y la no discriminación? ¿Qué impacto tuvo en el bienestar de las personas? ¿Qué acción segura puede tomarse y a quién se puede pedir ayuda? Responder estas preguntas ordena el pensamiento.",
        "Los casos nuevos pueden tener otros contextos: un equipo de fútbol que no deja jugar a una niña, un paseo donde una compañera con silla de ruedas no puede entrar a un lugar, un juego en línea con insultos por la nacionalidad, o un grupo de música que ridiculiza el gusto de otro. En todos, la pregunta es la misma: ¿quedan personas fuera o dañadas por una característica suya?",
        "También recuerda que puedes participar sin contar tu vida: usa personajes inventados o casos del texto. Y cuando un caso real te afecte, busca a un adulto de confianza. Reflexionar sobre derechos es construir un entorno donde todos puedan participar y sentirse seguros.",
    ],
    [("transferir", "usar lo aprendido en un caso nuevo"), ("acceso", "posibilidad de entrar y participar en un lugar o actividad"), ("nacionalidad", "país al que pertenece una persona"), ("estereotipo", "idea fija y simplificada sobre un grupo de personas"), ("accesibilidad", "condición que permite a todos usar un espacio")],
    [
        W("Aplicar las cuatro preguntas", "Un equipo de fútbol dice a Sofía: «las niñas no juegan aquí». ¿Qué principios se vulneran?", ["La excluyen por su género.", "No la dejan participar.", "Se vulneran la no discriminación y la inclusión."], "La no discriminación y la inclusión"),
        W("Proponer una acción", "Un paseo incluye un lugar sin acceso para una compañera con silla de ruedas. ¿Qué acción asegura inclusión?", ["El lugar excluye a una persona.", "Se puede cambiar el lugar o buscar un acceso.", "Así todos participan."], "Cambiar el lugar o buscar un acceso para que todos participen"),
    ],
    [
        M("Pensar que un estereotipo es solo una opinión sin daño.", "Se ignora que reduce a las personas a una idea fija.", "Los estereotipos pueden excluir y dañar."),
        M("Creer que la inclusión es un favor.", "Se ve como un acto de generosidad y no como un derecho.", "La inclusión es un derecho de todas las personas."),
    ],
    R=[
        ex("Dejar a una niña fuera del equipo por ser niña, ¿es discriminación, sí o no?", "Sí", "La trata peor por su género."),
        ex("Cambiar un lugar para que alguien en silla de ruedas pueda ir, ¿es inclusión, sí o no?", "Sí", "Asegura que participe."),
        ex("Un estereotipo, ¿es una idea fija sobre un grupo, sí o no?", "Sí", "Simplifica a las personas."),
    ],
    U=[
        ex("¿Por qué la inclusión es un derecho y no un favor?", "Porque todas las personas tienen derecho a participar", "No depende de la generosidad de otros."),
        ex("¿Qué pregunta ayuda a analizar un caso: «¿Quedan personas fuera o dañadas por una característica suya?» o «¿Quién ganó?»?", "«¿Quedan personas fuera o dañadas por una característica suya?»", "Identifica discriminación o exclusión."),
        ex("Insultar a alguien por su nacionalidad en un juego en línea, ¿vulnera la dignidad, sí o no?", "Sí", "No respeta su valor como persona."),
    ],
    A=[
        ex("Casos: 1) un niño no es invitado a un cumpleaños por su acento; 2) todos votan juegos; 3) se ríen de un compañero por su religión; 4) alguien traduce a un compañero nuevo. ¿Cuántos vulneran derechos?", "2", "El 1 y el 3 discriminan; el 2 y el 4 incluyen."),
        ex("Una compañera con discapacidad auditiva no entiende un video sin subtítulos. Opciones: A) Poner subtítulos. B) Decir que no importa si no entiende.", "A", "Los subtítulos permiten su participación."),
        ex("Un grupo dice «los de otro barrio son flojos». ¿Qué es esa frase?", "Un estereotipo", "Generaliza a un grupo con una idea fija."),
    ],
    Z=[
        ex("Antonio dice: «Yo no discrimino, solo no lo invito porque es distinto». ¿Qué error hay?", "Excluir por ser distinto es discriminar", "Se trata peor a alguien por una característica."),
        ex("¿Por qué lo virtual y lo presencial deben respetar los mismos principios?", "Porque los derechos valen en cualquier espacio", "El daño es real en ambos."),
    ],
    D=[
        arith("En un curso de 35 estudiantes, 28 firman un acuerdo de buen trato. ¿Cuántos faltan por firmar?", "35-28", "Al total se le restan los que firmaron."),
        ex("Un compañero dice que un chiste sobre los hinchas de otro equipo «no discrimina a nadie». ¿Cuándo se vuelve discriminación?", "Cuando trata peor a personas por su identidad o grupo", "Una broma que humilla a un grupo por quién es, es discriminación."),
    ],
    context=[ex("En un videojuego en línea, un grupo expulsa a una jugadora por ser extranjera. ¿Qué principio se vulnera principalmente?", "La no discriminación", "La tratan peor por su origen.")],
    selfcheck=[ex("En Orientación: ¿puedo aplicar los cuatro principios a casos nuevos?", "Sí", "Eso es transferir."), ex("¿La inclusión es un derecho?", "Sí", "Todos deben poder participar."), ex("¿Debo contar mi vida para participar?", "No", "Puedo usar casos inventados.")],
    task=T("Lee el caso inventado de Bastián: en el 7.º D se organiza un paseo a un parque con escaleras y se decide no llevar a Julia, que usa silla de ruedas, «porque es complicado». Responde las cuatro preguntas: hecho, principios vulnerados, impacto en el bienestar y acción segura con a quién pedir ayuda.", "Hecho: no la llevan por usar silla de ruedas. Principios: inclusión, igualdad y no discriminación. Impacto: se siente excluida. Acción: proponer cambiar el lugar y pedir apoyo al profesor jefe.", ["responde las cuatro preguntas", "nombra los principios", "propone una acción", "no cuenta nada personal"], ["texto escrito"], ["justificar la exclusión", "no proponer solución"], "Reconoce el análisis y pregunta qué pasaría si el lugar no puede cambiarse."),
    reinforce="Aplica las cuatro preguntas a un caso inventado nuevo sobre un grupo de música.",
    extend="Explica cómo la accesibilidad es una forma de inclusión.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. El conflicto de Ema y Gaspar, estudiantes inventados, y las situaciones de ejemplo están escritos en los ejercicios.",
    "Aprenderé qué es un conflicto, en qué se diferencia de la violencia y qué partes lo forman. Sirve para ver el conflicto como una oportunidad de aprender en lugar de algo que hay que esconder.",
    ["Sé reconocer mis emociones.", "Sé que debo respetar a los demás."],
    [
        "Un conflicto es un desacuerdo entre personas que tienen intereses, ideas o necesidades distintas. Es normal que aparezca en cualquier relación, porque las personas son diferentes. No es lo mismo que la violencia. En un conflicto se puede conversar y buscar soluciones. La violencia es dañar a otra persona con golpes, insultos, amenazas o humillaciones, y nunca es una forma aceptable de resolverlo.",
        "Todo conflicto tiene partes: las personas involucradas, el problema, los intereses (lo que cada uno quiere o necesita) y las emociones. Por ejemplo, Ema y Gaspar deben hacer un trabajo en pareja. Ema quiere entregarlo el jueves para estudiar para otra prueba; Gaspar prefiere el viernes porque tiene entrenamiento. El problema es la fecha. Sus intereses son tener tiempo para estudiar y tiempo para entrenar. Hay molestia, pero no hay violencia.",
        "Un conflicto bien manejado es una oportunidad. Permite conocer otras ideas, mejorar la comunicación y fortalecer la relación. Un conflicto mal manejado, en cambio, se vuelve más grande, genera enojo y puede terminar en violencia. Aprender a resolverlo con diálogo es una habilidad que se practica.",
    ],
    [("conflicto", "desacuerdo entre personas con intereses o ideas distintas"), ("violencia", "daño a otra persona con golpes, insultos, amenazas o humillaciones"), ("interés", "lo que una persona quiere o necesita"), ("oportunidad", "ocasión para aprender o mejorar"), ("diálogo", "conversación respetuosa en que se escuchan ambos")],
    [
        W("Distinguir conflicto y violencia", "Ema y Gaspar discuten por la fecha de entrega, sin insultarse. ¿Es conflicto o violencia?", ["Hay un desacuerdo.", "No hay daño ni insultos.", "Es un conflicto."], "Un conflicto"),
        W("Identificar los intereses", "Ema quiere entregar el jueves para estudiar; Gaspar prefiere el viernes por su entrenamiento. ¿Cuáles son los intereses?", ["Ema necesita tiempo para estudiar.", "Gaspar necesita tiempo para entrenar.", "La fecha es el problema; los intereses son lo que necesitan."], "Ema: tiempo para estudiar. Gaspar: tiempo para entrenar"),
    ],
    [
        M("Pensar que tener un conflicto significa que la relación está mal.", "Se cree que los desacuerdos no deberían ocurrir.", "Los conflictos son normales; lo importante es cómo se resuelven."),
        M("Confundir conflicto con violencia.", "Se cree que todo desacuerdo termina en agresión.", "En un conflicto se puede conversar; la violencia daña."),
    ],
    R=[
        ex("Un desacuerdo entre dos personas, ¿es un conflicto, sí o no?", "Sí", "Es una diferencia de intereses o ideas."),
        ex("Un insulto o un golpe, ¿es violencia o conflicto?", "Violencia", "Daña a la otra persona."),
        ex("¿Es normal que existan conflictos entre las personas, sí o no?", "Sí", "Las personas son distintas."),
    ],
    U=[
        ex("¿Por qué un conflicto puede ser una oportunidad?", "Porque permite aprender y mejorar la relación", "Se conocen ideas distintas y se practica el diálogo."),
        ex("¿Qué diferencia hay entre el problema y los intereses?", "El problema es el desacuerdo y los intereses son lo que cada uno necesita", "Los intereses explican por qué cada persona piensa distinto."),
        ex("¿Se puede resolver un conflicto con diálogo, sí o no?", "Sí", "Es una forma respetuosa de buscar soluciones."),
    ],
    A=[
        ex("Situaciones: 1) dos amigos discuten por quién usa la cancha; 2) uno empuja al otro; 3) conversan sobre un horario; 4) uno insulta al otro. ¿Cuántas son violencia?", "2", "El empujón y el insulto dañan; las otras son diálogo o conflicto."),
        ex("Dos grupos quieren la sala al mismo tiempo: uno para ensayar y otro para estudiar. ¿Cuál es el problema? A) La sala está ocupada. B) Un grupo es más importante.", "A", "El problema es el uso simultáneo de la sala."),
        ex("En el conflicto de la sala, ¿cuál es un interés de un grupo: ensayar tranquilos o ser el primero?", "Ensayar tranquilos", "Es lo que necesitan; ser el primero es solo querer ganar."),
    ],
    Z=[
        ex("Rafael dice: «Si peleo con mi compañero, nunca más seremos amigos». ¿Qué puede responder?", "Que un conflicto bien manejado puede fortalecer la relación", "El diálogo ayuda a resolverlo y aprender."),
        ex("¿Por qué la violencia nunca es una forma aceptable de resolver un conflicto?", "Porque daña a las personas", "El conflicto se resuelve con respeto."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 22 prefieren resolver los conflictos conversando. ¿Cuántos no lo prefieren?", "30-22", "Al total se le restan los que prefieren conversar."),
        ex("Dos hermanos discuten porque ambos quieren el computador a las 17 h: uno para jugar y otro para una tarea. ¿Qué solución ganar-ganar propones?", "Turnos de uso del computador", "Con turnos ambos logran lo que necesitan sin que nadie pierda."),
    ],
    context=[ex("En un trabajo grupal, Lucas quiere un tema de deportes y Valeria uno de arte. Empiezan a discutir. ¿Qué es esto?", "Un conflicto", "Tienen ideas distintas y deben decidir.")],
    selfcheck=[ex("En Orientación: ¿un conflicto es lo mismo que violencia?", "No", "Se puede resolver con diálogo."), ex("¿Los conflictos pueden ser una oportunidad?", "Sí", "Permiten aprender y mejorar la relación."), ex("¿Todo conflicto tiene intereses?", "Sí", "Lo que cada uno quiere o necesita.")],
    task=T("Lee el conflicto inventado entre Camila y Diego: ambos quieren usar la cancha en el recreo, ella para jugar básquetbol y él para jugar fútbol. Escribe las partes: las personas, el problema y el interés de cada uno. Indica además si hay violencia o no, y por qué.", "Personas: Camila y Diego. Problema: ambos quieren la cancha. Intereses: jugar básquetbol y jugar fútbol. No hay violencia: solo un desacuerdo.", ["identifica las partes", "distingue conflicto y violencia", "explica por qué", "no cuenta nada personal"], ["tabla escrita"], ["confundir problema con interés", "decir que hay violencia"], "Reconoce las partes y pregunta cómo se podría resolver."),
    reinforce="Escribe un conflicto inventado y sus partes: personas, problema e intereses.",
    extend="Explica una forma de convertir un conflicto en una oportunidad de aprendizaje.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. El diálogo de Andrea y Nicolás, estudiantes inventados, está escrito en los ejercicios.",
    "Aprenderé a escuchar con empatía, a separar hechos, emociones e interpretaciones y a usar mensajes en primera persona. Sirve para dialogar sin acusar ni gritar.",
    ["Sé identificar las partes de un conflicto.", "Sé distinguir conflicto y violencia."],
    [
        "La escucha empática es escuchar para comprender lo que el otro siente y necesita, no para preparar mi respuesta. Se logra mirando a la persona, sin interrumpir, y devolviendo lo que dijo con tus palabras: «Entiendo que te molestó que llegara tarde». Esto se llama parafrasear. También implica reconocer la emoción: «Parece que te sentiste ignorado».",
        "En un conflicto, conviene separar tres cosas. El hecho es lo que ocurrió y se puede observar: «Llegaste 20 minutos tarde». La emoción es lo que sientes: molestia o tristeza. La interpretación es lo que supones: «No te importa mi tiempo». La interpretación no es un hecho y suele empeorar la discusión. Habla de los hechos y de tu emoción, no de supuestas intenciones.",
        "Los mensajes en primera persona o «mensajes yo» ayudan a decir lo que sientes sin acusar. Tienen tres partes: «Yo me siento… cuando… porque necesito…». Por ejemplo: «Me siento molesto cuando llegas tarde porque necesito aprovechar el tiempo». Comparado con «Eres un irresponsable», el mensaje yo invita a conversar. Escuchar y hablar así ayuda a que ambos se sientan respetados.",
    ],
    [("escucha empática", "escuchar para comprender lo que el otro siente y necesita"), ("parafrasear", "repetir con mis palabras lo que dijo el otro"), ("interpretación", "lo que supongo sobre las intenciones del otro"), ("mensaje yo", "frase que dice lo que siento sin acusar"), ("acusar", "culpar a alguien con un juicio sobre su persona")],
    [
        W("Parafrasear", "Nicolás dice: «Me molestó que cambiaras el plan sin avisarme». ¿Cómo parafrasea Andrea?", ["Debe repetir con sus palabras.", "Debe reconocer la emoción.", "No debe defenderse todavía."], "«Entiendo que te molestó que cambiara el plan sin avisarte»"),
        W("Armar un mensaje yo", "Andrea quiere decir que le molesta que Nicolás llegue tarde. Usa «Yo me siento… cuando… porque necesito…».", ["Emoción: molesta.", "Hecho: llegas tarde.", "Necesidad: aprovechar el tiempo."], "«Me siento molesta cuando llegas tarde porque necesito aprovechar el tiempo»"),
    ],
    [
        M("Escuchar pensando en cómo contestar.", "Se prepara la respuesta en vez de comprender.", "Escucha hasta el final y parafrasea."),
        M("Usar frases como «tú siempre…» o «nunca…».", "Generalizan y acusan.", "Habla de un hecho concreto y de tu emoción."),
    ],
    R=[
        ex("«Eres un irresponsable». ¿Es un mensaje yo o una acusación?", "Una acusación", "Juzga a la persona sin hablar de lo que siento."),
        ex("Repetir con tus palabras lo que dijo el otro, ¿se llama parafrasear, sí o no?", "Sí", "Muestra que escuchaste."),
        ex("«Llegaste 20 minutos tarde», ¿es un hecho o una interpretación?", "Un hecho", "Se puede observar."),
    ],
    U=[
        ex("¿Por qué «no te importa mi tiempo» es una interpretación?", "Porque supone la intención del otro", "No se puede comprobar."),
        ex("¿Qué tres partes tiene un mensaje yo?", "Lo que siento, cuándo ocurre y lo que necesito", "Dice emoción, hecho y necesidad."),
        ex("¿Por qué conviene no interrumpir en un diálogo?", "Porque la otra persona se siente escuchada", "Permite entender su punto de vista."),
    ],
    A=[
        ex("Frases: 1) «Me siento molesto cuando no me avisas porque necesito organizarme»; 2) «Siempre me ignoras»; 3) «Entiendo que estás cansado»; 4) «Eres el peor». ¿Cuántas ayudan a dialogar?", "2", "La 1 y la 3 expresan emoción y comprensión."),
        ex("Valentina dice: «Me dolió que no me invitaras». Daniel responde: A) «Entiendo que te dolió que no te invitara». B) «No es para tanto».", "A", "Parafrasea y reconoce su emoción."),
        ex("Separa: «Faltaste a nuestro ensayo; seguro no te importa el grupo». ¿Cuál es la interpretación?", "«seguro no te importa el grupo»", "Supone una intención; el hecho es que faltó al ensayo."),
    ],
    Z=[
        ex("Camila dice: «Si le explico todo con enojo, me va a entender mejor». ¿Qué error hay?", "El enojo puede cerrar el diálogo", "Hablar con calma ayuda a que escuchen."),
        ex("¿Por qué evitar «siempre» y «nunca» en una discusión?", "Porque generalizan y no son verdad", "Un hecho concreto es más justo."),
    ],
    D=[
        arith("En un taller de 24 estudiantes se forman parejas para practicar mensajes yo. ¿Cuántas parejas hay?", "24//2", "Se divide el total en grupos de dos."),
        ex("Dani quiere decir que le molesta que le interrumpan. ¿Cuál es el mensaje yo correcto? A) «Me siento molesto cuando me interrumpen porque necesito terminar mi idea». B) «Eres un maleducado que interrumpe siempre».", "A", "Dice emoción, hecho y necesidad sin acusar."),
    ],
    context=[ex("Dos compañeros discuten porque uno usó los materiales del otro sin pedirlos. ¿Cuál es un mensaje yo adecuado?", "«Me siento molesto cuando usas mis cosas sin pedirlas, porque necesito cuidarlas»", "Dice emoción, hecho y necesidad sin acusar.")],
    selfcheck=[ex("En Orientación: ¿parafrasear muestra que escuché?", "Sí", "Repito con mis palabras."), ex("¿Una interpretación es un hecho?", "No", "Es una suposición."), ex("¿Un mensaje yo acusa a la otra persona?", "No", "Habla de mí.")],
    task=T("Lee el conflicto inventado: Pía le dice a Joaquín «Siempre llegas tarde y no te importa el equipo». Él responde «Tú eres una mandona». Reescribe lo que cada uno podría decir con escucha empática: Pía con un mensaje yo y Joaquín parafraseando.", "Pía: «Me siento molesta cuando llegas tarde porque necesito empezar a tiempo». Joaquín: «Entiendo que te molesta que llegue tarde y que necesitas empezar a tiempo».", ["Pía usa un mensaje yo", "Joaquín parafrasea", "no usa acusaciones", "no cuenta nada personal"], ["texto escrito"], ["generalizar con siempre", "defenderse sin escuchar"], "Reconoce los mensajes y pregunta qué emoción reconocería Joaquín."),
    reinforce="Convierte tres acusaciones en mensajes yo.",
    extend="Explica por qué la escucha empática no significa estar de acuerdo.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. El conflicto de la sala de computación y las cinco formas de enfrentarlo están escritos en los ejercicios.",
    "Aprenderé a comparar las formas de enfrentar un conflicto y a reconocer cuál busca soluciones que sirvan a ambas partes. Sirve para elegir caminos respetuosos y sin violencia.",
    ["Sé escuchar con empatía.", "Sé hablar con mensajes yo."],
    [
        "Hay varias formas de enfrentar un conflicto, y cada una tiene consecuencias. Evitar es hacer como que no pasa nada; baja la tensión hoy, pero el problema sigue. Imponer es obligar al otro a aceptar lo que yo quiero; puedo ganar, pero la otra persona se resiente. Ceder es aceptar todo lo del otro; evita la pelea, pero mis necesidades quedan sin atender. Negociar es conversar para encontrar una solución que ambos puedan aceptar. Pedir mediación es buscar a una tercera persona neutral que ayude a conversar.",
        "Negociar es lo que más favorece soluciones respetuosas. Se parte de los intereses, no de las posiciones. Una posición es lo que digo que quiero («quiero la sala hoy»). Un interés es por qué lo quiero («necesito practicar para una exposición»). Con los intereses claros se pueden inventar opciones: turnos, horarios compartidos, otra sala. Se llama solución «ganar-ganar» cuando ambas partes obtienen algo importante.",
        "La mediación ayuda cuando es difícil dialogar solos: una persona neutral, como un profesor o un compañero capacitado, ordena la conversación sin imponer una solución. Si hay amenazas o golpes, no es un conflicto que se resuelva entre pares: se debe pedir ayuda adulta.",
    ],
    [("evitar", "hacer como que el conflicto no existe"), ("imponer", "obligar a otro a aceptar lo que yo quiero"), ("ceder", "aceptar todo lo que el otro quiere"), ("negociar", "conversar para llegar a una solución aceptable para ambos"), ("mediación", "ayuda de una tercera persona neutral para dialogar")],
    [
        W("Identificar la estrategia", "Camila dice: «Yo uso la sala y punto». ¿Evita, impone, cede o negocia?", ["Obliga a los demás.", "No pregunta qué necesitan.", "Impone."], "Impone"),
        W("Pasar de posiciones a intereses", "Un grupo dice «queremos la sala hoy» porque debe ensayar para una exposición mañana. Otro grupo dice «también la queremos» para terminar un afiche. ¿Qué opción ganar-ganar hay?", ["Ambos necesitan tiempo.", "Pueden dividir la sala en turnos.", "Así los dos logran lo importante."], "Dividir el uso de la sala en turnos"),
    ],
    [
        M("Pensar que ceder siempre es la mejor forma de evitar problemas.", "Se descuidan las propias necesidades.", "Negocia para que ambos logren algo."),
        M("Creer que si no hablo del conflicto, desaparece.", "Se confunde evitar con resolver.", "Si el problema sigue, conviene hablarlo."),
    ],
    R=[
        ex("Obligar al otro a aceptar lo que quiero, ¿es imponer o negociar?", "Imponer", "No considera las necesidades del otro."),
        ex("Hacer como que nada pasó, ¿es evitar o ceder?", "Evitar", "El problema sigue."),
        ex("Conversar para encontrar una solución aceptable para ambos, ¿es negociar, sí o no?", "Sí", "Esa es la definición."),
    ],
    U=[
        ex("¿Qué diferencia hay entre una posición y un interés?", "La posición es lo que digo que quiero y el interés es por qué lo quiero", "El interés explica la necesidad detrás de lo que se pide."),
        ex("¿Qué es una solución ganar-ganar?", "Una en que ambas partes obtienen algo importante", "Satisface a los dos."),
        ex("¿Para qué sirve una mediación?", "Para que una persona neutral ayude a dialogar", "No impone la solución."),
    ],
    A=[
        ex("Formas: 1) evitar; 2) imponer; 3) negociar; 4) pedir mediación. ¿Cuál parte conversando entre los involucrados para llegar a un acuerdo?", "3", "Negociar es dialogar directamente."),
        ex("Dos grupos quieren la misma cancha. Opciones: A) Dividir el horario en turnos de 15 minutos. B) Que gane el grupo más numeroso.", "A", "Los turnos satisfacen a ambos; imponer por número no."),
        ex("Un conflicto incluye amenazas y empujones. ¿Se resuelve entre compañeros o se pide ayuda adulta?", "Se pide ayuda adulta", "Hay violencia y riesgo."),
    ],
    Z=[
        ex("Pedro dice: «Si cedo, evito la pelea y no pierdo nada». ¿Qué pierde en realidad?", "Sus propias necesidades", "Ceder siempre deja sus intereses sin atender."),
        ex("¿Por qué negociar desde los intereses abre más opciones que desde las posiciones?", "Porque permite inventar soluciones distintas", "Se busca qué necesita cada uno."),
    ],
    D=[
        arith("Dos grupos comparten la sala 60 minutos en turnos iguales. ¿Cuántos minutos usa cada uno?", "60//2", "Se divide el tiempo entre dos grupos."),
        ex("Dos grupos pelean por una sala y proponen, uno, que decida la profesora, y otro, que se sorteen turnos. ¿Cuál es una negociación entre las partes?", "El sorteo de turnos", "Las partes acuerdan una regla entre ellas."),
    ],
    context=[ex("Dos amigas discuten por quién usará el computador. La profesora les propone turnos de 20 minutos. ¿Qué forma de enfrentar el conflicto es esa?", "Negociar con turnos", "Ambas obtienen tiempo de uso.")],
    selfcheck=[ex("En Orientación: ¿negociar busca una solución para ambos?", "Sí", "Busca una solución ganar-ganar."), ex("¿Imponer considera las necesidades del otro?", "No", "Solo las mías."), ex("¿La mediación ayuda a dialogar?", "Sí", "Con una persona neutral.")],
    task=T("Lee el conflicto inventado: Tomás quiere usar el único balón en el recreo para fútbol y Sofía para vóleibol. Escribe la consecuencia de cinco formas de enfrentarlo (evitar, imponer, ceder, negociar, mediación) y elige la más adecuada, con una solución ganar-ganar.", "Evitar: sigue; imponer: resentimiento; ceder: sin necesidades; negociar: turnos; mediación: ayuda. Elige negociar: 10 minutos para cada uno.", ["escribe las cinco consecuencias", "elige la más adecuada", "propone una solución ganar-ganar", "no cuenta nada personal"], ["tabla escrita"], ["no ver consecuencias", "elegir imponer"], "Reconoce la tabla y pregunta qué hacer si no hay acuerdo."),
    reinforce="Escribe una posición y el interés que hay detrás en un conflicto de tu curso inventado.",
    extend="Explica cuándo conviene pedir mediación y cuándo ayuda adulta.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. El caso del trabajo en equipo del 7.º A y los pasos de resolución están escritos en los ejercicios.",
    "Aprenderé una secuencia de pasos para resolver un conflicto de forma segura y a reconocer cuándo debo pedir ayuda a un adulto. Sirve para actuar con calma y sin violencia.",
    ["Sé negociar desde los intereses.", "Sé hablar con mensajes yo."],
    [
        "Una secuencia segura para resolver un conflicto tiene cinco pasos. Primero, calma: si estás muy enojado, respira profundo, cuenta hasta diez o aléjate unos minutos antes de hablar. Segundo, escucha: deja que el otro explique y parafrasea. Tercero, di lo tuyo con un mensaje yo. Cuarto, busquen juntos opciones que sirvan a ambos y elijan una. Quinto, acuerden cómo la revisarán: quién hace qué y cuándo.",
        "Hay conflictos que no se resuelven solos. Si hay golpes, amenazas, humillaciones repetidas o una persona tiene miedo de la otra, no es un conflicto entre iguales sino violencia. En ese caso no enfrentes sola o solo a la otra persona: avisa a un adulto de confianza, como un profesor jefe, el orientador o el equipo de convivencia escolar. Pedir ayuda no es fracasar, es protegerte.",
        "Después de resolver, revisen cómo les fue. Si el acuerdo no funciona, pueden ajustarlo. El conflicto bien resuelto fortalece la relación y la confianza. Y recuerda que la calma ayuda, pero tu seguridad es lo primero: si sientes peligro, alejarte y buscar ayuda es lo correcto.",
    ],
    [("calma", "estado de tranquilidad antes de hablar"), ("acuerdo", "decisión que aceptan las dos partes"), ("seguimiento", "revisar después si el acuerdo funciona"), ("amenaza", "anuncio de que se hará daño"), ("ayuda adulta", "apoyo de un adulto de confianza o del colegio")],
    [
        W("Aplicar los cinco pasos", "Bruno y Elisa discuten por quién presenta el trabajo. Bruno está muy enojado. ¿Qué paso va primero?", ["Estar enojado dificulta escuchar.", "Primero hay que calmarse.", "Después viene escuchar."], "Calma: respirar o alejarse unos minutos"),
        W("Reconocer cuándo pedir ayuda", "Elisa recibe amenazas de Bruno por mensaje y tiene miedo. ¿Es un conflicto que resuelven solos?", ["Hay amenazas y miedo.", "Eso es violencia.", "Debe avisar a un adulto."], "No: debe avisar a un adulto"),
    ],
    [
        M("Pensar que debo resolver todo sola o solo.", "Se cree que pedir ayuda es fracasar.", "En casos de amenazas o golpes, avisa a un adulto."),
        M("Hablar de inmediato cuando estoy muy enojado.", "El enojo dificulta escuchar.", "Primero calma, después diálogo."),
    ],
    R=[
        ex("¿El primer paso es la calma, sí o no?", "Sí", "Con calma se puede escuchar."),
        ex("Si hay amenazas, ¿se resuelve entre compañeros o se pide ayuda adulta?", "Se pide ayuda adulta", "Las amenazas son violencia."),
        ex("Un acuerdo, ¿es una decisión que aceptan las dos partes, sí o no?", "Sí", "Esa es la definición."),
    ],
    U=[
        ex("¿Por qué conviene revisar el acuerdo después?", "Porque se ve si funcionó", "Así se puede ajustar."),
        ex("¿Por qué no se debe enfrentar solo a alguien que amenaza?", "Porque hay riesgo", "Un adulto puede proteger."),
        ex("¿Qué se hace antes de hablar si estás muy enojado: respirar o gritar?", "Respirar", "Ayuda a calmarse."),
    ],
    A=[
        ex("Pasos: 1) calma; 2) escuchar; 3) mensaje yo; 4) buscar opciones; 5) acordar. ¿Cuál va después de escuchar?", "3", "Se dice lo propio con un mensaje yo."),
        ex("Dos compañeros acuerdan alternar quién presenta cada semana. Después de dos semanas, uno dice que no funciona. Opciones: A) Ajustar el acuerdo conversando. B) Abandonar el trabajo.", "A", "El seguimiento permite ajustar."),
        ex("Una compañera le dice a otra que «la va a pillar a la salida». ¿Qué debe hacer la afectada? A) Contárselo a un adulto de confianza. B) Esperar y ver qué pasa.", "A", "Una amenaza es un riesgo."),
    ],
    Z=[
        ex("Lucas dice: «Si pido ayuda, parezco débil». ¿Qué respuesta le darías?", "Pedir ayuda protege y es una decisión inteligente", "Cuidarse no es debilidad."),
        ex("¿Por qué la calma es el primer paso y no el último?", "Porque sin calma no se puede escuchar", "Es la base del diálogo."),
    ],
    D=[
        arith("Un grupo de 28 estudiantes practica los cinco pasos en 4 grupos iguales. ¿Cuántos estudiantes hay por grupo?", "28//4", "Se divide el total entre 4."),
        ex("Dos estudiantes gritan en medio de una discusión. ¿Qué conviene hacer primero según la secuencia segura?", "Calmarse antes de seguir", "Con enojo no se puede escuchar."),
    ],
    context=[ex("En un trabajo grupal, dos integrantes discuten por la nota. Uno dice «lo dejamos para mañana, estoy muy enojado». ¿Qué paso aplicó?", "Calma", "Se alejó para poder hablar tranquilo.")],
    selfcheck=[ex("En Orientación: ¿conviene calmarme antes de hablar?", "Sí", "Es el primer paso."), ex("¿Debo enfrentar solo una amenaza?", "No", "Debo avisar a un adulto."), ex("¿Se puede revisar un acuerdo después?", "Sí", "Sirve para ajustarlo si falla.")],
    task=T("Lee el caso inventado del 7.º A: Valentina y Matías discuten porque él copió parte de su trabajo; ella está muy molesta. Escribe los cinco pasos de resolución aplicados a su caso, con una frase para cada uno, y una situación en que deberían pedir ayuda a un adulto.", "1) Calma: «Hablamos mañana». 2) Escuchar: «Entiendo que quisiste ayudar». 3) Mensaje yo: «Me siento molesta porque copiaste mi trabajo». 4) Opciones: rehacer. 5) Acordar: entregar el viernes. Pedir ayuda si hay amenazas.", ["escribe los cinco pasos", "usa un mensaje yo", "nombra cuándo pedir ayuda", "no cuenta nada personal"], ["texto escrito"], ["saltar la calma", "no nombrar cuándo pedir ayuda"], "Reconoce los pasos y pregunta cuál paso le cuesta más."),
    reinforce="Anota los cinco pasos de resolución en tus palabras.",
    extend="Explica por qué cuidar tu seguridad es parte de resolver un conflicto.",
)
