"""Cuaderno del estudiante, 8.º básico Orientación: OA 05 (derechos y bienestar en relaciones presenciales y virtuales) y OA 06 (resolución dialogada de conflictos)."""
from __future__ import annotations

from student_content_or8_a import M, T, W, lesson
from student_lessons import arith, ex

OA5, OA6 = "OR08 OA 05", "OR08 OA 06"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. El caso del chat «Los del fondo» y todas las frases están escritos en los ejercicios. Los personajes son inventados.",
    "Aprenderé cuatro principios que protegen a las personas en sus relaciones, presenciales o virtuales: igualdad, dignidad, inclusión y no discriminación. Sirve para reconocer cuándo se respetan y cuándo no.",
    ["Sé que todas las personas tienen derecho a un trato digno.", "Sé que lo que se escribe en línea también afecta a las personas."],
    [
        "Los derechos de las personas se apoyan en cuatro principios. La igualdad dice que todas las personas valen lo mismo y tienen los mismos derechos, sin importar si son mujeres u hombres, de dónde vienen o cómo son. La dignidad es el valor de cada persona y exige que no se la humille. La inclusión es hacer lugar a todos en las actividades y en los grupos. La no discriminación es no tratar peor a alguien por una característica suya, como su apariencia, su origen, su género, su forma de hablar o una discapacidad.",
        "Estos principios valen en la sala, en el patio y también en las redes sociales. Un chat de curso que deja fuera a un compañero por cómo habla no incluye. Un meme que humilla a una compañera por su cuerpo no respeta su dignidad. Una regla como «las niñas no juegan fútbol» rompe la igualdad entre mujeres y hombres.",
        "Para analizar una relación, mira a quiénes involucra, qué derecho está en juego y qué impacto tiene en su bienestar: cómo se sienten, si se aíslan, si cambian su conducta. Identificar una circunstancia en que no se respetan los derechos es el primer paso para cambiarla. Siempre se hace pensando en los hechos y en las personas, sin ridiculizar a nadie.",
    ],
    [("igualdad", "principio que dice que todas las personas valen lo mismo y tienen los mismos derechos"), ("dignidad", "valor de toda persona, que exige no humillarla"), ("inclusión", "hacer lugar a todas las personas en las actividades y grupos"), ("discriminación", "tratar peor a alguien por una característica suya"), ("bienestar", "sentirse bien física y emocionalmente")],
    [
        W("Identificar un principio", "En el chat «Los del fondo», dejan fuera a Nicolás porque tartamudea. ¿Qué principio no se respeta?", ["Lo excluyen por una característica suya.", "No lo tratan igual que a los demás.", "Se rompen la inclusión y la no discriminación."], "La inclusión y la no discriminación"),
        W("Analizar el impacto", "Nicolás deja de hablar en clase desde que lo excluyen. ¿Qué impacto tiene en su bienestar?", ["Cambió su conducta.", "Se aísla.", "Es una señal de que se siente mal."], "Se aísla y se siente mal"),
    ],
    [
        M("Pensar que si es un chat, no cuentan los derechos.", "Se cree que lo virtual no es real.", "Los derechos valen igual en lo presencial y en lo virtual."),
        M("Creer que discriminar es solo insultar.", "Se olvida que dejar fuera también discrimina.", "La exclusión por una característica también es discriminación."),
    ],
    R=[
        ex("Dejar fuera a un compañero de un chat por su forma de hablar, ¿es inclusión o discriminación?", "Discriminación", "Lo trata peor por una característica suya."),
        ex("La dignidad ¿exige no humillar a nadie, sí o no?", "Sí", "Es el valor de cada persona."),
        ex("Decir que «las niñas no juegan fútbol», ¿respeta la igualdad entre mujeres y hombres?", "No", "Les niega un derecho por ser mujeres."),
    ],
    U=[
        ex("¿Qué principio busca hacer lugar a todas las personas en un grupo? A) La inclusión. B) La competencia.", "A", "Incluir es dar un lugar a todos."),
        ex("Un meme humilla a una compañera por su cuerpo. ¿Qué principio rompe: la dignidad o la inclusión?", "La dignidad", "La humillación no respeta el valor de la persona."),
        ex("¿Cambiar la conducta y aislarse son señales de impacto en el bienestar, sí o no?", "Sí", "Muestran que la persona se siente mal."),
    ],
    A=[
        ex("Cuatro situaciones: 1) se burlan del acento de un compañero; 2) se turnan la cancha entre niñas y niños; 3) no invitan a una compañera a un trabajo por usar silla de ruedas; 4) se ayuda a un compañero nuevo. ¿Cuántas rompen derechos?", "2", "La 1 y la 3 discriminan; la 2 y la 4 los respetan."),
        ex("El curso decide que en el chat «todos escriben y todos son escuchados». ¿Qué principio aplica? A) La inclusión. B) La exclusión.", "A", "Da lugar a todos."),
        ex("Una profesora da la palabra solo a los hombres porque «hablan más fuerte». ¿Qué principio no se respeta?", "La igualdad", "Trata distinto a mujeres y hombres sin razón."),
    ],
    Z=[
        ex("¿Por qué excluir de un grupo a alguien también es una forma de discriminación?", "Porque lo trata peor por una característica suya", "La exclusión niega su lugar y le causa daño."),
        ex("Un compañero dice que «es solo un chat». ¿Qué respuesta le darías?", "Que lo virtual también afecta a las personas", "Las burlas en línea dañan igual que en persona."),
    ],
    D=[
        arith("En un chat de 30 integrantes, 18 escribieron mensajes de apoyo a un compañero excluido y 4 siguieron burlándose. El resto no participó. ¿Cuántos no participaron?", "30-18-4", "Al total se le restan los que apoyaron y los que se burlaron."),
        arith("Un curso identifica 3 situaciones de exclusión por semana durante 6 semanas. ¿Cuántas situaciones identifica en total?", "3*6", "Se multiplican las situaciones por las semanas."),
    ],
    context=[ex("En el recreo, un grupo no deja jugar a Matilda al fútbol porque «las niñas no saben». ¿Qué dos principios no se respetan?", "La igualdad y la inclusión", "La tratan distinto por ser mujer y la dejan fuera.")],
    selfcheck=[ex("En Orientación: ¿la dignidad significa no humillar?", "Sí", "Es el valor de toda persona."), ex("¿Los derechos valen en lo virtual y lo presencial?", "Sí", "Valen en ambos."), ex("¿Dejar fuera por una característica es inclusión?", "No", "Eso es discriminación.")],
    task=T("Lee el caso inventado: en el chat del curso, un grupo hace un meme con la foto de Rosario, a quien le cuesta leer en voz alta, y la deja afuera de la actividad de la semana. Escribe una tabla con tres columnas: hecho, principio que no se respeta y posible impacto en el bienestar de Rosario.", "Hecho: hacen un meme y la dejan fuera. Principios: dignidad e inclusión. Impacto: puede sentir vergüenza, aislarse y no querer participar.", ["distingue el hecho", "nombra al menos dos principios", "describe un impacto posible", "no humilla a nadie en su respuesta"], ["tabla de tres columnas"], ["culpar a Rosario", "decir que es solo una broma"], "Reconoce los principios y pregunta qué haría un compañero para apoyar a Rosario."),
    reinforce="Escribe una situación de inclusión y otra de discriminación en el patio.",
    extend="Explica con un ejemplo cómo la igualdad entre mujeres y hombres se aplica en una actividad deportiva.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Los mensajes del grupo y la lista de características están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a distinguir un desacuerdo de una discriminación o ciberacoso, y a nombrar hechos, emociones, derechos y límites. Sirve para reconocer cuándo una relación afecta el bienestar de alguien.",
    ["Conozco los principios de igualdad, dignidad, inclusión y no discriminación.", "Sé que lo virtual también tiene efectos reales."],
    [
        "No todo desacuerdo es discriminación. Pensar distinto sobre una película o un equipo de fútbol es legítimo y se puede conversar con respeto. Hay discriminación cuando se trata peor a alguien por una característica suya. El ciberacoso es el maltrato repetido por medios digitales y tiene cuatro rasgos: se repite, hay un desequilibrio entre quien agrede y quien recibe, causa daño y a veces se difunde ante muchos.",
        "Para analizar un caso, separa cuatro cosas. El hecho: lo que ocurrió. La emoción: lo que puede sentir quien lo vive, como tristeza, rabia, miedo o vergüenza. El derecho: lo que la persona merece, como trato digno y a no ser excluida. El límite: lo que no se debe hacer, como insultar, humillar o difundir sin permiso. La libertad de expresar una opinión termina donde empieza la humillación de otra persona.",
        "El impacto en el bienestar puede verse en cambios: no querer ir al colegio, dejar actividades que antes gustaban, aislarse o tener cambios de ánimo. Si notas estos cambios en alguien, o en ti, conviene hablar con una persona adulta de confianza. Reconocer el impacto no es exagerar: es cuidar.",
    ],
    [("desacuerdo", "diferencia de opinión que puede conversarse"), ("ciberacoso", "maltrato repetido por medios digitales"), ("desequilibrio", "diferencia de poder entre quien agrede y quien recibe"), ("difundir", "enviar algo a muchas personas"), ("libertad de expresión", "derecho a opinar sin humillar a otros")],
    [
        W("Desacuerdo o discriminación", "Dos estudiantes discuten si el mejor postre es el helado o la torta. Otro grupo se burla de un compañero por su acento. ¿Cuál es discriminación?", ["La discusión sobre postres es una diferencia de gustos.", "La burla por el acento trata peor a alguien por una característica.", "Es discriminación."], "La burla por el acento"),
        W("Reconocer ciberacoso", "Cada día, durante dos semanas, tres compañeros envían a Julia mensajes burlones y los comparten en un chat de 25 personas. ¿Es ciberacoso?", ["Se repite durante dos semanas.", "Hay tres contra una y se difunde.", "Causa daño."], "Sí, tiene los rasgos del ciberacoso"),
    ],
    [
        M("Llamar «ciberacoso» a cualquier discusión en línea.", "Se mezcla un desacuerdo con maltrato repetido.", "Revisa si se repite, hay desequilibrio, daño y difusión."),
        M("Creer que la libertad de expresión permite decir cualquier cosa.", "Se olvida el derecho de los demás.", "Termina donde empieza la humillación."),
    ],
    R=[
        ex("Discutir si es mejor una película u otra, ¿es discriminación, sí o no?", "No", "Es una diferencia de gustos."),
        ex("Un maltrato repetido por medios digitales, ¿es ciberacoso o conversación?", "Ciberacoso", "Es su definición."),
        ex("¿Aislarse es un posible impacto del acoso en el bienestar, sí o no?", "Sí", "Es un cambio frecuente en quien lo vive."),
    ],
    U=[
        ex("¿Qué diferencia una burla ocasional del ciberacoso? A) Que el ciberacoso se repite y causa daño. B) Que se hace en una app.", "A", "La repetición y el daño lo caracterizan."),
        ex("¿Qué derecho está en juego si difunden una foto de alguien sin permiso: la dignidad o el descanso?", "La dignidad", "La difusión sin permiso daña su imagen."),
        ex("¿La libertad de expresión autoriza humillar a otro, sí o no?", "No", "Termina donde empieza la humillación."),
    ],
    A=[
        ex("Cuatro situaciones: 1) un debate respetuoso sobre un tema; 2) tres alumnos humillan cada día a un compañero en un chat; 3) un mensaje equivocado enviado una vez; 4) un meme sobre el cuerpo de una compañera compartido por 20 personas. ¿Cuántas son ciberacoso o discriminación?", "2", "La 2 y la 4 humillan y se difunden; la 1 es un desacuerdo y la 3 un error aislado."),
        ex("Pía se aísla y deja de ir a la banda del colegio tras recibir burlas en línea. ¿Qué indica? A) Un impacto en su bienestar. B) Un cambio de gustos sin relación.", "A", "El cambio coincide con las burlas."),
        ex("Un compañero dice: «Es mi opinión que ella es fea». ¿Es libertad de expresión o humillación?", "Humillación", "Ataca su dignidad."),
    ],
    Z=[
        ex("¿Por qué una burla difundida a 100 personas puede doler más que una burla dicha en privado?", "Porque más personas la ven y no se puede controlar", "La difusión amplifica el daño."),
        ex("Un amigo dice que si ella no responde, no le afecta. ¿Qué error comete?", "Cree que callar significa no sentir daño", "Muchas personas callan por vergüenza o miedo."),
    ],
    D=[
        arith("En un chat de 40 personas, 6 escriben burlas, 22 miran sin hacer nada y el resto apoya a la persona afectada. ¿Cuántos la apoyan?", "40-6-22", "Al total se le restan los que se burlan y los que solo miran."),
        arith("Una persona recibe 8 mensajes burlones por día durante 7 días. ¿Cuántos mensajes recibió en la semana?", "8*7", "Se multiplican los mensajes diarios por los días."),
    ],
    context=[ex("Un grupo de estudiantes ficticios comparte cada día en un chat un video editado de Mateo cayéndose. Él ya no quiere ir al colegio. Nombra el hecho y la emoción probable.", "Hecho: difunden un video suyo cada día. Emoción: vergüenza o miedo", "El video se repite y se difunde, y él cambia su conducta.")],
    selfcheck=[ex("En Orientación: ¿el ciberacoso se repite?", "Sí", "La repetición es un rasgo."), ex("¿Un desacuerdo respetuoso es discriminación?", "No", "Es una diferencia de opinión."), ex("¿El acoso puede afectar el bienestar?", "Sí", "Puede causar aislamiento y malestar.")],
    task=T("Lee los cuatro casos inventados: (a) discusión amable sobre qué serie ver; (b) un grupo crea un chat para burlarse del peso de una compañera; (c) alguien se equivoca de chat y envía un mensaje; (d) un video de un estudiante sordo imitado por un grupo. Clasifica cada caso como desacuerdo, error aislado, discriminación o ciberacoso y escribe el derecho afectado en los dos más graves.", "(a) Desacuerdo. (b) Ciberacoso y discriminación; dignidad. (c) Error aislado. (d) Discriminación, quizá ciberacoso si se repite; dignidad e igualdad.", ["clasifica los cuatro casos", "justifica con rasgos", "nombra derechos afectados", "no humilla a nadie"], ["tabla de clasificación"], ["llamar acoso a todo", "no ver la discriminación"], "Reconoce las clasificaciones y pregunta cómo comprobar si un caso se repite."),
    reinforce="Escribe una diferencia entre un desacuerdo y un acoso.",
    extend="Explica los cuatro rasgos del ciberacoso con tus palabras.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. El caso del meme y las alternativas del público están escritos en los ejercicios. Los personajes son inventados.",
    "Aprenderé a comparar las opciones de quienes ven una situación de discriminación o acoso y a prever sus consecuencias. Sirve para decidir cómo actuar como espectador.",
    ["Distingo hechos, emociones, derechos y límites.", "Reconozco los rasgos del ciberacoso."],
    [
        "Quien ve una situación de acoso, en persona o en línea, se llama espectador. Su decisión importa. Puede reenviar o reírse, y así ayuda al acoso; puede ignorar, y la persona queda sola; puede defender con respeto, apoyar en privado o avisar a una persona adulta. Cada opción tiene consecuencias para quien sufre, para quien agrede y para el espectador.",
        "Reírse o reenviar aumenta el daño y hace sentir a la víctima más sola. Ignorar parece neutral, pero deja que el acoso continúe. Apoyar a la persona con un mensaje privado, no sumarse y avisar a una persona adulta suele ayudar más. Defender públicamente puede ser valioso si es seguro, y no hay que insultar a quien agrede: se puede decir «eso no está bien».",
        "Pensar en las consecuencias también incluye lo legal y escolar: reenviar un contenido que humilla puede traer sanciones según el reglamento del colegio. Una buena decisión protege a la persona afectada, evita nuevos daños y se apoya en adultos cuando es necesario.",
    ],
    [("espectador", "persona que ve una situación sin ser quien agrede ni quien la sufre"), ("reenviar", "mandar a otros un mensaje o imagen recibida"), ("apoyar", "ayudar a una persona mostrando que está acompañada"), ("sanción", "consecuencia por romper una norma"), ("reglamento", "conjunto de normas del colegio")],
    [
        W("Comparar acciones de espectadores", "Un meme humilla a Pía. Ana lo reenvía, Beto lo ignora y Cata le escribe a Pía en privado y avisa a la orientadora. ¿Quién ayuda más?", ["Ana aumenta el daño.", "Beto deja que continúe.", "Cata apoya y busca ayuda."], "Cata"),
        W("Prever consecuencias", "Si Beto sigue ignorando, ¿qué ocurre probablemente?", ["El acoso continúa.", "Pía sigue sola.", "Ignorar tiene un costo."], "El acoso continúa y Pía queda sola"),
    ],
    [
        M("Pensar que reírse de un meme no es hacer daño.", "Se cree que solo daña quien lo crea.", "Reír y reenviar también aumentan el daño."),
        M("Creer que defender implica insultar a quien agrede.", "Se piensa que hay que responder con violencia.", "Puedes decir «eso no está bien» sin insultar."),
    ],
    R=[
        ex("Reenviar un meme que humilla, ¿ayuda o aumenta el daño?", "Aumenta el daño", "Más personas lo ven."),
        ex("Escribirle en privado a quien fue humillado para apoyarlo, ¿es una buena opción, sí o no?", "Sí", "Le muestra que no está solo."),
        ex("Avisar a una persona adulta, ¿es una opción que ayuda, sí o no?", "Sí", "Un adulto puede intervenir."),
    ],
    U=[
        ex("¿Por qué ignorar no es una opción neutral? A) Porque el acoso sigue. B) Porque cansa.", "A", "Si nadie actúa, el acoso continúa."),
        ex("Cata dice a un grupo: «Eso no está bien, dejen de compartir el meme». ¿Defendió con respeto o insultó?", "Defendió con respeto", "Usó una frase firme sin agredir."),
        ex("Un espectador que ríe y reenvía, ¿participa en el acoso, sí o no?", "Sí", "Sus acciones refuerzan el daño."),
    ],
    A=[
        ex("Opciones ante un chat que humilla a Lucas: 1) reír; 2) reenviar; 3) escribirle en privado y avisar a un adulto; 4) ignorar. ¿Cuál ayuda más?", "La 3", "Apoya a Lucas y busca ayuda."),
        ex("Rodrigo quiere defender a una compañera en el chat, pero teme represalias. ¿Qué alternativa segura tiene? A) Apoyarla en privado y avisar a un adulto. B) Gritarle al grupo.", "A", "Es segura y efectiva."),
        ex("Un curso decide que quien reenvíe un meme humillante recibirá una conversación con convivencia escolar. ¿Es una consecuencia del reglamento, sí o no?", "Sí", "Aplica una norma del colegio."),
    ],
    Z=[
        ex("Explica por qué reenviar «solo para avisar» a otros puede aumentar el daño.", "Porque más personas ven el contenido", "El meme circula más y la víctima sufre más."),
        ex("Un joven dice: «Si me meto, me molestarán a mí». ¿Qué opción le recomendarías?", "Apoyar en privado y avisar a un adulto", "Ayuda sin exponerse en público."),
    ],
    D=[
        arith("Un meme humillante llegó a 4 grupos de 22 personas. ¿Cuántas personas lo recibieron si ninguna estaba en dos grupos?", "4*22", "Se multiplican los grupos por las personas de cada uno."),
        arith("De 35 estudiantes de una encuesta de ejemplo, 12 reenviarían, 9 ignorarían y el resto apoyaría. ¿Cuántos apoyarían?", "35-12-9", "Al total se le restan los otros dos grupos."),
    ],
    context=[ex("En el recreo, Camila ve que un grupo graba a una niña de primero para burlarse. ¿Qué dos acciones puede hacer para actuar de forma segura?", "Apoyar a la niña y avisar a una persona adulta", "Evita enfrentar al grupo y activa la ayuda.")],
    selfcheck=[ex("En Orientación: ¿ignorar un acoso lo detiene?", "No", "Si nadie actúa, continúa."), ex("¿Apoyar en privado ayuda a la persona afectada?", "Sí", "Le muestra que no está sola."), ex("¿Reenviar un meme humillante aumenta el daño?", "Sí", "Más personas lo ven.")],
    task=T("Lee el caso inventado: circula en el chat del curso un audio de Marcela cantando fuera de tono, con risas de fondo. Marcela se siente avergonzada. Haz una tabla con cuatro opciones de un espectador (reír, reenviar, ignorar, apoyar y avisar), la consecuencia para Marcela y la consecuencia para el espectador. Cierra eligiendo una y explicando por qué.", "Reír: más burla; el espectador participa. Reenviar: más difusión; puede tener sanción. Ignorar: el audio sigue; el espectador no ayuda. Apoyar y avisar: Marcela se siente acompañada; el espectador actúa bien. Elijo la última.", ["compara cuatro opciones", "describe consecuencias para ambos", "elige una opción y justifica", "no se burla de nadie"], ["tabla de cuatro filas"], ["decir que ignorar es neutral", "defender insultando"], "Valora la comparación y pregunta qué frase usaría para apoyar a Marcela."),
    reinforce="Escribe una frase de apoyo en privado para alguien que fue humillado en un chat.",
    extend="Explica por qué las decisiones del espectador cambian lo que ocurre con el acoso.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Los mensajes del caso están escritos en los ejercicios. Todo ocurre con personajes inventados.",
    "Aprenderé a elegir una acción segura cuando alguien sufre discriminación o ciberacoso: apoyar, guardar evidencia, reportar y avisar. Sirve para ayudar sin ponerme en riesgo.",
    ["Sé comparar las opciones de un espectador.", "Conozco los rasgos del ciberacoso."],
    [
        "Una acción segura protege a la persona afectada, detiene el daño y evita nuevos riesgos. Tiene cuatro pasos. Primero, no participes ni respondas con agresión: no reenvíes ni insultes. Segundo, guarda evidencia: capturas de pantalla con fecha, nombres de cuentas y mensajes. Tercero, apoya a la persona afectada con un mensaje respetuoso. Cuarto, avisa a una persona adulta de confianza y usa las herramientas de la plataforma para reportar y bloquear.",
        "La evidencia debe ser clara: qué se dijo, quién lo dijo y cuándo. No la compartas con otros: solo se muestra a la persona adulta que ayudará. Si lo que circula es una imagen íntima de alguien, no la guardes ni la reenvíes: no borres el chat y avisa de inmediato a una persona adulta. Reportar en la plataforma es avisar al servicio que ofrece la aplicación para que revise y retire contenidos que dañan. Bloquear impide que esa cuenta te siga escribiendo.",
        "En el colegio puedes recurrir al profesor jefe, al orientador o al equipo de convivencia escolar, que tienen protocolos para estos casos. Si te cuesta hablar, puedes acompañar a la persona afectada a contarlo. Y si la situación te abruma o necesitas hablar con alguien, existe el Fono Niños 147.",
    ],
    [("evidencia", "prueba de lo ocurrido, como capturas con fecha y nombres"), ("reportar", "avisar a la plataforma para que revise y retire contenido"), ("bloquear", "impedir que una cuenta nos escriba"), ("protocolo", "pasos que sigue el colegio ante un caso"), ("plataforma", "aplicación o sitio donde se publica")],
    [
        W("Armar los pasos", "Un chat comparte una foto de Sofía editada para burlarse de ella (no es una imagen íntima). Ordena las acciones seguras de Ema: reportar, apoyar a Sofía, no reenviar, avisar a un adulto.", ["Primero no participa: no reenvía.", "Luego apoya a Sofía.", "Después avisa a una persona adulta y reporta en la plataforma."], "No reenviar, apoyar a Sofía, avisar a un adulto y reportar"),
        W("Qué guardar como evidencia", "Ema decide guardar capturas. ¿Qué datos debe incluir?", ["Qué se dijo.", "Quién lo dijo.", "Cuándo se dijo."], "Mensaje, cuenta y fecha"),
    ],
    [
        M("Contestar con insultos para defender a alguien.", "Se cree que la agresión detiene la agresión.", "Responder con insultos genera más conflicto."),
        M("Borrar los mensajes para que no los vean.", "Se quiere evitar el problema.", "Guarda capturas antes de bloquear."),
    ],
    R=[
        ex("Antes de bloquear, ¿conviene guardar capturas como evidencia, sí o no?", "Sí", "Sirve para mostrar lo que ocurrió."),
        ex("Reportar en la plataforma, ¿es avisar para que revisen un contenido, sí o no?", "Sí", "Es su función."),
        ex("¿Respondes con insultos o con un mensaje respetuoso de apoyo?", "Con un mensaje respetuoso de apoyo", "Los insultos aumentan el conflicto."),
    ],
    U=[
        ex("¿Qué datos deben aparecer en la evidencia? A) Qué se dijo, quién y cuándo. B) Solo la hora.", "A", "Con esos datos se entiende el caso."),
        ex("¿Se comparte la evidencia con todo el curso o solo con la persona adulta que ayudará?", "Solo con la persona adulta", "Difundirla sería otro daño."),
        ex("¿El profesor jefe puede ser una persona de ayuda en el colegio, sí o no?", "Sí", "Conoce al curso y tiene apoyo de convivencia."),
    ],
    A=[
        ex("Pasos: 1) compartir la foto para denunciar; 2) guardar capturas; 3) apoyar a la víctima; 4) bloquear y reportar. ¿Cuáles son seguros?", "2, 3 y 4", "Compartir la foto aumenta el daño."),
        ex("Sofía no quiere hablar con nadie. Ema puede: A) Acompañarla a contarlo a una persona adulta. B) Esperar que se le pase.", "A", "Acompañar ayuda a pedir ayuda."),
        ex("Un compañero amenaza a quien reportó el contenido. ¿Qué debe hacer la persona? A) Avisar a una persona adulta. B) Amenazarlo de vuelta.", "A", "Un adulto puede protegerla."),
    ],
    Z=[
        ex("¿Por qué conviene guardar evidencia antes de bloquear?", "Porque el bloqueo puede impedir ver los mensajes", "Con evidencia, los adultos pueden entender y actuar."),
        ex("¿Por qué reportar en la plataforma además de avisar a un adulto?", "Porque la plataforma puede retirar el contenido", "Ayuda a que el daño no siga circulando."),
    ],
    D=[
        arith("Una captura muestra 7 mensajes por día durante 4 días. ¿Cuántos mensajes de evidencia hay?", "7*4", "Se multiplican los mensajes por los días."),
        arith("De 28 estudiantes de una encuesta de ejemplo, 17 saben cómo reportar y el resto no. ¿Cuántos no saben?", "28-17", "Al total se le restan los que sí saben."),
    ],
    context=[ex("En el chat del curso, Joaquín recibe un mensaje con una foto editada de una compañera para burlarse de ella (no es una imagen íntima). Quiere ayudar. Ordena brevemente lo que haría primero y por qué.", "No reenviarla, guardar evidencia y avisar a un adulto", "Evita el daño y consigue ayuda.")],
    selfcheck=[ex("En Orientación: ¿guardar capturas ayuda a un adulto a entender el caso?", "Sí", "Son evidencia de lo ocurrido."), ex("¿Se debe responder con insultos?", "No", "Aumenta el conflicto."), ex("¿Se puede reportar en la plataforma?", "Sí", "Es una herramienta de seguridad.")],
    task=T("Lee el caso inventado de Daniela: en un grupo, tres compañeros publican cada día un meme sobre su cuerpo y el resto lo comparte. Escribe un plan de acción segura con cinco pasos para un compañero que quiere ayudarla: qué no hace, qué evidencia guarda, cómo la apoya, a quién avisa y cómo usa la plataforma.", "1) No comparte ni insulta. 2) Guarda capturas con fecha, nombres y mensaje. 3) Le escribe a Daniela: «Estoy contigo». 4) Avisa al profesor jefe y a convivencia. 5) Reporta y bloquea las cuentas.", ["cinco pasos claros", "incluye evidencia y apoyo", "nombra personas adultas", "no humilla a nadie"], ["lista de pasos"], ["publicar la evidencia", "responder con agresión"], "Reconoce los pasos y pregunta qué hará si el adulto no responde."),
    reinforce="Escribe tres pasos de acción segura ante un meme que humilla a alguien.",
    extend="Explica por qué reportar y avisar a un adulto se complementan.",
)

lesson(
    OA5, 5,
    "Una hoja y un lápiz. Los mensajes y la ficha de reporte están escritos en los ejercicios. Todo ocurre con personajes inventados.",
    "Aprenderé a escribir un mensaje de apoyo, un reporte claro a una persona adulta y frases de límite. Sirve para ayudar a quien sufre discriminación y para cuidar relaciones respetuosas.",
    ["Sé qué evidencia guardar.", "Sé a quién acudir en el colegio."],
    [
        "Comunicar bien es parte de actuar bien. Un mensaje de apoyo es breve, cálido y sin juicio: «Vi lo que pasó, no me parece justo. Estoy contigo. ¿Quieres que lo conversemos?». No dice «no es para tanto» ni «ignóralo»: respeta lo que la persona siente.",
        "Un reporte claro a una persona adulta cuenta cuatro cosas: qué pasó, quiénes participan, desde cuándo ocurre y qué evidencia hay. Por ejemplo: «Desde hace una semana, un grupo publica memes de Daniela en el chat del curso. Tengo capturas con fecha. Necesito ayuda». Es mejor ser concreto que decir «hay problemas en el curso».",
        "Para poner un límite a quien agrede, usa frases firmes y sin insultos: «Eso es una burla, para ya», «No lo comparto» o «No quiero estar en este chat». Y recuerda que los derechos de las personas son de todos: igualdad, dignidad, inclusión y no discriminación. Defenderlos, con respeto y ayuda adulta, mejora el bienestar del curso.",
    ],
    [("mensaje de apoyo", "mensaje breve y cálido para acompañar a alguien"), ("reporte", "relato claro de lo ocurrido para pedir ayuda"), ("concreto", "con datos precisos y comprobables"), ("límite", "frase que dice lo que no se acepta"), ("juicio", "opinión que culpa o critica a alguien")],
    [
        W("Revisar un mensaje de apoyo", "Compara: (a) «No es para tanto, ignóralos». (b) «Vi lo que pasó, no me parece justo. Estoy contigo». ¿Cuál apoya mejor?", ["La opción (a) minimiza lo que siente.", "La (b) reconoce su situación y ofrece compañía.", "El apoyo respeta lo que la persona siente."], "La (b)"),
        W("Armar un reporte", "Datos: un grupo publica memes de Daniela en el chat del curso desde hace una semana; hay capturas con fecha. ¿Cómo lo dice a la orientadora?", ["Dice qué pasa: memes de Daniela.", "Dice quiénes y dónde: grupo en el chat.", "Dice desde cuándo y qué evidencia hay."], "«Desde hace una semana, un grupo publica memes de Daniela en el chat del curso. Tengo capturas con fecha»"),
    ],
    [
        M("Decir «no te lo tomes tan en serio» a quien sufre acoso.", "Se quiere calmar rápido.", "Reconoce lo que siente y ofrece apoyo."),
        M("Hacer un reporte vago: «hay problemas en el curso».", "Se omite lo concreto.", "Cuenta qué pasó, quiénes, desde cuándo y qué evidencia hay."),
    ],
    R=[
        ex("Un buen mensaje de apoyo, ¿es cálido y sin juicio o frío y crítico?", "Cálido y sin juicio", "Acompaña sin culpar."),
        ex("Un reporte claro dice qué pasó y desde cuándo, ¿verdadero o falso?", "Verdadero", "Esos datos ayudan a actuar."),
        ex("«No quiero estar en este chat» ¿es una frase de límite, sí o no?", "Sí", "Dice lo que no acepta."),
    ],
    U=[
        ex("¿Qué mensaje respeta lo que la persona siente? A) «Lamento lo que te pasó, estoy contigo». B) «No es para tanto».", "A", "Reconoce su situación."),
        ex("¿Cuál de estos datos NO es necesario en un reporte: qué pasó o la marca del celular?", "La marca del celular", "No ayuda a entender el caso."),
        ex("Una frase de límite firme, ¿insulta o dice lo que no se acepta?", "Dice lo que no se acepta", "Es firme y respetuosa."),
    ],
    A=[
        ex("Marcela escribe este reporte: «Un grupo publica memes de Ana en el chat del curso; tengo capturas». ¿Qué dato importante le falta?", "Desde cuándo ocurre", "Le faltan las fechas: el reporte debe decir desde cuándo pasa."),
        ex("Marcela quiere decir un límite al chat. ¿Qué frase sirve? A) «Eso es una burla, para ya». B) «Son lo peor».", "A", "Es firme sin insultar."),
        ex("Un amigo recibe burlas por su acento. ¿Qué mensaje de apoyo le servirá más?", "«Estoy contigo, ¿quieres que lo contemos a la orientadora?»", "Acompaña y ofrece ayuda concreta."),
    ],
    Z=[
        ex("¿Por qué un reporte concreto ayuda más a un adulto que uno vago?", "Porque permite entender y actuar rápido", "Los datos precisos guían la ayuda."),
        ex("Un joven dice: «Mejor no digo nada, es mi amigo». ¿Qué le responderías si el amigo es quien agrede?", "Que avisar protege a todos, incluso a su amigo", "Un adulto puede ayudar a que cambie su conducta."),
    ],
    D=[
        arith("Un reporte tiene 4 partes y el curso escribió 7 reportes de ejemplo. ¿Cuántas partes escribieron en total?", "4*7", "Se multiplican las partes por los reportes."),
        arith("De 32 estudiantes, 20 escribieron un reporte completo y el resto uno incompleto. ¿Cuántos incompletos hubo?", "32-20", "Al total se le restan los reportes completos."),
    ],
    context=[ex("En un chat de curso, Pablo comenta que se burlan de Ana por su ropa. Él quiere apoyarla. ¿Qué mensaje puede escribirle?", "«Vi lo que pasó, no me parece justo. Estoy contigo»", "Es breve, cálido y respeta lo que ella siente.")],
    selfcheck=[ex("En Orientación: ¿un reporte debe ser concreto?", "Sí", "Los datos ayudan a actuar."), ex("¿Un mensaje de apoyo minimiza lo que siente la persona?", "No", "Debe reconocer lo que siente."), ex("¿Se puede poner un límite sin insultar?", "Sí", "Una frase firme es suficiente.")],
    task=T("Lee el caso inventado: desde el lunes, Gabriel recibe burlas en el chat del curso por su ropa de segunda mano; hay capturas del martes y jueves. Escribe tres textos: un mensaje de apoyo para Gabriel, un reporte de cuatro datos para la orientadora y una frase de límite para el chat.", "Apoyo: «Vi lo que pasó, no me parece justo. Estoy contigo». Reporte: «Desde el lunes, varios compañeros se burlan de la ropa de Gabriel en el chat del curso. Tengo capturas del martes y jueves. Necesito ayuda». Límite: «Eso es una burla, para ya».", ["escribe los tres textos", "el reporte tiene qué, quiénes, desde cuándo y evidencia", "el límite no insulta", "no humilla a nadie"], ["tres textos breves"], ["mensaje que minimiza", "reporte vago"], "Reconoce los textos claros y pregunta cómo seguirá apoyando a Gabriel."),
    reinforce="Escribe un mensaje de apoyo para un personaje de cuento que fue excluido de un juego.",
    extend="Explica por qué un reporte vago ayuda menos que uno concreto.",
)

lesson(
    OA5, 6,
    "Una hoja y un lápiz. Los cuatro casos nuevos están escritos en los ejercicios; ocurren entre personajes inventados. No hace falta contar nada propio.",
    "Aprenderé a aplicar los derechos de igualdad, dignidad, inclusión y no discriminación a casos nuevos de mi entorno inmediato. Sirve para proponer cambios concretos en el curso y en el colegio.",
    ["Conozco los cuatro principios.", "Sé actuar con seguridad ante una situación de discriminación."],
    [
        "Transferir es llevar lo aprendido a situaciones nuevas. Los mismos cuatro principios sirven para casos distintos: una niña a la que no dejan participar en un taller de robótica por ser mujer rompe la igualdad; un compañero con silla de ruedas que no puede entrar a la sala de computación pide inclusión; un estudiante que llegó de otro país y recibe burlas por su acento requiere no discriminación; una compañera de la que se burlan por su cuerpo merece dignidad.",
        "Para analizar un caso nuevo, haz tres preguntas. ¿Qué derecho está en juego? ¿Cómo afecta el bienestar de la persona? ¿Qué acción segura y respetuosa corresponde? A veces la respuesta es una conversación; otras, un cambio de reglas, como turnos justos en la cancha o rampas de acceso; y otras, la ayuda de una persona adulta.",
        "También conviene proponer mejoras para el curso: un acuerdo de convivencia que prohíba burlas, un buzón de ayuda o un grupo de apoyo entre compañeros. Un buen acuerdo se escribe con todos, incluye a mujeres y hombres por igual, y se revisa cada cierto tiempo.",
    ],
    [("transferir", "aplicar lo aprendido a una situación nueva"), ("acceso", "posibilidad de entrar o participar"), ("acuerdo de convivencia", "norma que el curso acuerda para vivir bien juntos"), ("rampa", "plano inclinado que permite subir sin escalones"), ("buzón", "caja o espacio donde se dejan mensajes o ideas")],
    [
        W("Analizar un caso nuevo", "A una niña no la dejan inscribirse en un taller de robótica «porque es de hombres». Aplica las tres preguntas.", ["Derecho: igualdad entre mujeres y hombres.", "Bienestar: se siente excluida y desmotivada.", "Acción: pedir al taller que la acepte y avisar a la dirección."], "Se rompe la igualdad; corresponde inscribirla y avisar a la dirección"),
        W("Proponer un cambio concreto", "Un estudiante con silla de ruedas no puede entrar al laboratorio por la escalera. ¿Qué cambio propones?", ["El derecho en juego es la inclusión.", "Hace falta un acceso sin escalones.", "Se pide a la dirección una rampa o cambiar la clase de lugar."], "Pedir una rampa o trasladar la clase a un lugar accesible"),
    ],
    [
        M("Pensar que hay actividades «de hombres» o «de mujeres».", "Se repiten estereotipos.", "Todas las personas pueden participar en todas las actividades."),
        M("Creer que la inclusión es solo ser amable.", "Se olvida que a veces hay que cambiar condiciones.", "Incluir a veces exige ajustes como rampas o turnos."),
    ],
    R=[
        ex("Impedir a una niña entrar a un taller por ser mujer, ¿rompe la igualdad, sí o no?", "Sí", "La trata distinto por su género."),
        ex("Una rampa para una silla de ruedas, ¿es un ajuste de inclusión, sí o no?", "Sí", "Permite acceder sin escalones."),
        ex("Burlarse de un acento extranjero, ¿es discriminación, sí o no?", "Sí", "Trata peor por una característica."),
    ],
    U=[
        ex("¿Qué pregunta ayuda a analizar un caso nuevo? A) ¿Qué derecho está en juego? B) ¿Quién ganó?", "A", "Permite identificar el principio afectado."),
        ex("Un acuerdo de convivencia, ¿se escribe con todos o lo decide solo el profesor?", "Con todos", "Un buen acuerdo incluye a todo el curso."),
        ex("Turnos justos en la cancha entre niñas y niños, ¿aplican la igualdad, sí o no?", "Sí", "Dan las mismas oportunidades."),
    ],
    A=[
        ex("Cuatro casos: 1) a una niña no la dejan jugar fútbol; 2) un compañero no puede subir al segundo piso; 3) se burlan del acento de un estudiante nuevo; 4) se felicita a un equipo. ¿Cuántos requieren cambios?", "3", "Los casos 1, 2 y 3 vulneran derechos."),
        ex("El curso propone un buzón de ayuda. ¿Qué cumple? A) Un medio para pedir ayuda con respeto. B) Un lugar para difundir burlas.", "A", "Sirve para comunicar problemas de forma segura."),
        ex("En un acuerdo del curso, ¿qué frase respeta la igualdad? A) «Mujeres y hombres tienen la misma palabra». B) «Los hombres hablan primero».", "A", "Da las mismas oportunidades."),
    ],
    Z=[
        ex("Explica por qué una rampa beneficia no solo a quien usa silla de ruedas.", "Porque también ayuda a quien lleva peso o tiene dificultad para subir", "Una mejora de acceso beneficia a toda la comunidad."),
        ex("Un compañero dice: «Es una tradición que solo juegan los niños». ¿Qué le responderías?", "Que una tradición no justifica negar derechos", "La igualdad vale más que una costumbre."),
    ],
    D=[
        arith("En un colegio de 360 estudiantes, 24 usan apoyos de accesibilidad. ¿Cuántos no los usan?", "360-24", "Al total se le restan quienes los usan."),
        arith("El curso propone 3 mejoras de inclusión por cada una de sus 5 comisiones. ¿Cuántas mejoras reúnen?", "3*5", "Se multiplican las mejoras por las comisiones."),
    ],
    context=[ex("En una feria ficticia del colegio, los puestos de ciencia son dirigidos solo por hombres y los de cocina por mujeres, «como siempre». ¿Qué principio conviene revisar y qué cambio propones?", "La igualdad; mezclar a mujeres y hombres en ambos puestos", "Evita estereotipos y da las mismas oportunidades.")],
    selfcheck=[ex("En Orientación: ¿los mismos principios sirven para casos nuevos?", "Sí", "Se aplican a distintas situaciones."), ex("¿La inclusión puede exigir ajustes como rampas?", "Sí", "A veces hay que cambiar condiciones."), ex("¿Hay actividades solo para hombres?", "No", "Todas las personas pueden participar.")],
    task=T("Lee los cuatro casos inventados: (a) a Camila no la eligen para el equipo de ajedrez por ser mujer; (b) Ismael usa audífonos auditivos y no entiende las instrucciones cuando todos gritan; (c) un grupo se burla de una estudiante recién llegada de otro país por su acento; (d) Tamara recibe memes sobre su cuerpo. Para cada caso escribe: principio afectado, impacto en el bienestar y una acción segura o un cambio concreto.", "(a) Igualdad; se desmotiva; pedir un proceso justo y avisar. (b) Inclusión; no participa; acordar señales visuales. (c) No discriminación; se aísla; apoyarla y avisar. (d) Dignidad; vergüenza; guardar evidencia y avisar.", ["completa los cuatro casos", "nombra el principio", "describe el impacto", "propone acción o cambio"], ["tabla de cuatro filas"], ["culpar a la persona afectada", "dar soluciones vagas"], "Valora las acciones concretas y pregunta cuál cambio es más urgente."),
    reinforce="Escribe una norma de convivencia para tu curso inventado que proteja la dignidad de todos.",
    extend="Explica por qué la igualdad entre mujeres y hombres es un derecho de todas las personas.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. El caso del trabajo grupal de Camila y Mateo y todas las frases están escritos en los ejercicios. Los personajes son inventados.",
    "Aprenderé qué es un conflicto, en qué se diferencia de la violencia y por qué puede ser una oportunidad de aprendizaje. Sirve para enfrentar los desacuerdos sin agredir.",
    ["Sé que las personas pueden pensar distinto.", "Sé que la violencia daña a las personas."],
    [
        "Un conflicto es un desacuerdo entre personas porque quieren cosas distintas, tienen intereses opuestos o piensan diferente. Es normal: ocurre en todas las relaciones humanas. El conflicto no es lo mismo que la violencia. La violencia es dañar a otro con golpes, insultos, amenazas o humillaciones. El conflicto se puede resolver con diálogo; la violencia no es una forma válida de resolverlo.",
        "Todo conflicto tiene partes (las personas), intereses (lo que cada una necesita) y emociones (lo que sienten). Camila y Mateo tienen que entregar un trabajo y discuten porque ella quiere dividirlo en partes y él quiere hacerlo junto. Cada uno tiene una necesidad: ella, avanzar rápido; él, que quede coherente. Entender los intereses ayuda a buscar soluciones.",
        "Un conflicto bien resuelto es una oportunidad de aprendizaje. Aprendes a escuchar, a expresar lo que necesitas, a negociar y a conocer mejor a los demás. Evitarlo o resolverlo con violencia no enseña nada y daña la relación. Por eso la meta es resolverlo con diálogo, escucha empática y soluciones respetuosas.",
    ],
    [("conflicto", "desacuerdo entre personas por intereses, necesidades u opiniones distintas"), ("violencia", "daño a otra persona con golpes, insultos, amenazas o humillaciones"), ("interés", "lo que cada persona necesita o quiere lograr"), ("diálogo", "conversación en que se habla y se escucha"), ("oportunidad de aprendizaje", "situación en que se aprende algo nuevo")],
    [
        W("Conflicto o violencia", "Camila y Mateo discuten con calma cómo dividir el trabajo. Otro grupo se insulta y se empuja. ¿Cuál es violencia?", ["La discusión con calma es un conflicto.", "Insultar y empujar daña.", "Eso es violencia."], "El grupo que se insulta y se empuja"),
        W("Intereses de cada parte", "Camila quiere dividir el trabajo para avanzar rápido; Mateo prefiere hacerlo junto para que quede coherente. ¿Cuáles son los intereses?", ["Camila: avanzar rápido.", "Mateo: que el trabajo sea coherente.", "Son necesidades distintas."], "Camila: rapidez. Mateo: coherencia"),
    ],
    [
        M("Creer que todo conflicto es malo y hay que evitarlo.", "Se confunde conflicto con violencia.", "El conflicto es normal y puede enseñar."),
        M("Pensar que gana quien más grita.", "Se confunde imponer con resolver.", "Resolver es buscar una solución respetuosa."),
    ],
    R=[
        ex("Un desacuerdo sobre cómo organizar un trabajo, ¿es un conflicto, sí o no?", "Sí", "Hay intereses distintos."),
        ex("Golpear a alguien porque no piensa igual, ¿es violencia o conflicto?", "Violencia", "Daña a otra persona."),
        ex("¿Se puede resolver un conflicto con diálogo, sí o no?", "Sí", "El diálogo permite buscar soluciones."),
    ],
    U=[
        ex("¿Qué diferencia un conflicto de la violencia? A) El conflicto es un desacuerdo; la violencia daña. B) No hay diferencia.", "A", "Un conflicto puede conversarse; la violencia daña."),
        ex("Si Camila sabe qué necesita Mateo, ¿tendrá más ideas de solución, sí o no?", "Sí", "Entender los intereses ayuda a buscar soluciones."),
        ex("¿Qué se aprende de un conflicto bien resuelto: a escuchar o a gritar?", "A escuchar", "Resolverlo con diálogo enseña habilidades."),
    ],
    A=[
        ex("Situaciones: 1) dos amigos discuten por un lugar en la cancha y conversan; 2) alguien amenaza a otro; 3) un grupo se pone de acuerdo sobre un horario; 4) un estudiante rompe los útiles de otro. ¿Cuántas son violencia?", "2", "La amenaza y romper los útiles dañan; las otras son conflicto bien llevado."),
        ex("Rodrigo quiere salir al patio y Julia quiere terminar el trabajo. ¿Qué intereses tienen? A) Descanso y avance. B) Los dos quieren lo mismo.", "A", "Cada uno quiere algo distinto."),
        ex("Un compañero dice «gano yo porque tengo más fuerza». ¿Resuelve el conflicto o lo impone?", "Lo impone", "Quien impone no escucha ni busca una solución común."),
    ],
    Z=[
        ex("¿Por qué evitar siempre los conflictos puede dañar las relaciones?", "Porque los problemas no se resuelven y crecen", "Callar deja el desacuerdo sin atender."),
        ex("Explica con tus palabras cómo un conflicto puede ser una oportunidad de aprendizaje.", "Porque se aprende a escuchar y a negociar", "Resolverlo con diálogo enseña habilidades útiles."),
    ],
    D=[
        arith("En una encuesta de ejemplo de 40 estudiantes, 25 dicen resolver conflictos conversando, 8 evitándolos y el resto con gritos. ¿Cuántos usan gritos?", "40-25-8", "Al total se le restan los otros grupos."),
        arith("Un curso registra 3 conflictos por semana durante 8 semanas. ¿Cuántos conflictos registra?", "3*8", "Se multiplican los conflictos por las semanas."),
    ],
    context=[ex("En la clase de Orientación, Daniela y Pía discuten porque ambas quieren usar la sala para ensayar. Una dice «yo llegué primero» y la otra «yo la reservé». ¿Es conflicto o violencia?", "Conflicto", "Hay intereses distintos y no hay daño.")],
    selfcheck=[ex("En Orientación: ¿el conflicto es normal en las relaciones?", "Sí", "Ocurre en todas."), ex("¿La violencia es una forma válida de resolverlo?", "No", "Daña a las personas."), ex("¿Un conflicto puede enseñar algo?", "Sí", "Es una oportunidad de aprendizaje.")],
    task=T("Lee el caso inventado: Tomás y Elena deben preparar una exposición. Tomás quiere usar solo imágenes; Elena quiere usar solo texto. Se enojan y dejan de hablarse. Haz un cuadro con las partes, los intereses de cada uno, las emociones probables y una forma de convertir el conflicto en aprendizaje.", "Partes: Tomás y Elena. Intereses: Tomás, que sea atractiva; Elena, que explique bien. Emociones: enojo y frustración. Aprendizaje: combinar imágenes y texto y practicar a escuchar.", ["identifica partes e intereses", "nombra emociones", "propone un aprendizaje", "no culpa a nadie"], ["cuadro escrito"], ["culpar a una parte", "proponer evitar el problema"], "Reconoce los intereses y pregunta qué solución combinada propondrían."),
    reinforce="Escribe dos ejemplos de conflicto y dos de violencia sin nombres reales.",
    extend="Explica por qué entender los intereses de ambos ayuda a resolver un conflicto.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. El diálogo de Isidora y Benjamín y los mensajes están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé a separar hechos de interpretaciones, a usar mensajes en primera persona y a practicar la escucha empática. Sirve para hablar de un conflicto sin atacar y para entender al otro.",
    ["Sé que un conflicto no es violencia.", "Sé que cada parte tiene intereses."],
    [
        "En un conflicto conviene separar el hecho de la interpretación. El hecho es lo que se puede comprobar: «llegaste 15 minutos tarde». La interpretación es lo que pienso sobre ello: «no te importa el grupo». Atacar con interpretaciones genera defensa; hablar de hechos facilita el diálogo. También conviene nombrar la emoción: «me enojé», «me dio pena».",
        "Un mensaje en primera persona, o mensaje «yo», habla de lo que yo siento sin acusar. Tiene tres partes: cuando pasa tal hecho, yo me siento así, y necesito esto. Por ejemplo: «Cuando llegas tarde, me siento preocupada porque no avanzamos; necesito que avises si te retrasas». Es distinto de «tú siempre llegas tarde y no te importa».",
        "La escucha empática es escuchar para comprender, no para responder. Se hace mirando a la persona, sin interrumpir, y repitiendo con tus palabras lo que entendiste: «Entonces te sentiste molesto porque nadie te preguntó, ¿es así?». Escuchar no significa estar de acuerdo, sino reconocer lo que el otro siente y necesita. Todos tenemos derecho a ser escuchados y a hablar sin gritos ni insultos.",
    ],
    [("hecho", "algo que ocurrió y se puede comprobar"), ("interpretación", "lo que alguien piensa o supone sobre un hecho"), ("mensaje «yo»", "forma de hablar de lo que yo siento sin acusar"), ("escucha empática", "escuchar para comprender lo que el otro siente"), ("parafrasear", "decir con otras palabras lo que escuchamos")],
    [
        W("Separar hecho e interpretación", "Isidora le dice a Benjamín: «Llegaste 15 minutos tarde, y no te importa el grupo». ¿Cuál es el hecho y cuál la interpretación?", ["«Llegaste 15 minutos tarde» se puede comprobar.", "«No te importa el grupo» es lo que ella supone.", "El hecho es lo primero."], "Hecho: llegó 15 minutos tarde. Interpretación: no le importa el grupo"),
        W("Armar un mensaje «yo»", "Isidora quiere decirle a Benjamín lo que le pasó. Arma el mensaje en tres partes.", ["Hecho: cuando llegas 15 minutos tarde.", "Sentimiento: me siento preocupada.", "Necesidad: necesito que avises si te retrasas."], "«Cuando llegas 15 minutos tarde me siento preocupada; necesito que avises si te retrasas»"),
    ],
    [
        M("Empezar con «tú siempre…» o «tú nunca…».", "Se acusa a la persona y se generaliza.", "Habla de un hecho concreto y de lo que sientes."),
        M("Escuchar solo para pensar qué responder.", "Se prepara la defensa en vez de entender.", "Escucha, parafrasea y recién responde."),
    ],
    R=[
        ex("«Llegaste a las 8:20» ¿es un hecho o una interpretación?", "Un hecho", "Se puede comprobar con un reloj."),
        ex("«No te importa nadie» ¿es un hecho o una interpretación?", "Una interpretación", "Es una suposición sobre lo que piensa."),
        ex("Un mensaje «yo» ¿acusa o habla de lo que yo siento?", "Habla de lo que yo siento", "Evita acusar al otro."),
    ],
    U=[
        ex("¿Qué tres partes tiene un mensaje «yo»? A) Hecho, sentimiento y necesidad. B) Insulto, grito y excusa.", "A", "Esa es su estructura."),
        ex("Parafrasear es: ¿repetir con otras palabras lo que entendiste o contradecir al otro?", "Repetir con otras palabras lo que entendiste", "Ayuda a comprobar que se comprendió."),
        ex("Escuchar de forma empática ¿exige estar de acuerdo, sí o no?", "No", "Exige comprender lo que el otro siente."),
    ],
    A=[
        ex("Cuatro frases: 1) «Tú nunca escuchas»; 2) «Cuando me interrumpes me siento molesta; necesito terminar mi idea»; 3) «Eres insoportable»; 4) «Siempre arruinas todo». ¿Cuál es un mensaje «yo»?", "La 2", "Tiene hecho, sentimiento y necesidad."),
        ex("Benjamín dice: «Entonces te preocupa que no avancemos, ¿es así?». ¿Qué hace? A) Parafrasea. B) Interrumpe.", "A", "Repite lo que entendió."),
        ex("Rodrigo dice «tú me arruinaste el día». Cambia a mensaje «yo»: ¿qué parte falta si solo dice «me enojé»?", "El hecho y la necesidad", "El mensaje debe incluir qué pasó y qué necesita."),
    ],
    Z=[
        ex("¿Por qué «tú siempre» provoca defensa en el otro?", "Porque acusa y generaliza", "La persona se siente atacada y no escucha."),
        ex("Explica por qué escuchar sin interrumpir ayuda a bajar la tensión.", "Porque la persona se siente respetada", "Sentirse escuchado reduce la rabia."),
    ],
    D=[
        arith("En un taller, 30 estudiantes practican mensajes «yo» en parejas. ¿Cuántas parejas se forman?", "30//2", "Se divide el total entre 2."),
        arith("Cada pareja escribe 3 mensajes «yo» y hay 15 parejas. ¿Cuántos mensajes escriben?", "15*3", "Se multiplican las parejas por los mensajes."),
    ],
    context=[ex("Valentina y Lucas pelean porque él usó su cuaderno sin pedirlo. Ella dice: «Eres un irrespetuoso». ¿Cómo cambia a un mensaje «yo»?", "«Cuando usas mi cuaderno sin pedirlo me enojo; necesito que me preguntes»", "Incluye hecho, sentimiento y necesidad.")],
    selfcheck=[ex("En Orientación: ¿un hecho se puede comprobar?", "Sí", "Una interpretación no."), ex("¿Un mensaje «yo» acusa?", "No", "Habla de lo que uno siente."), ex("¿Parafrasear ayuda a comprender?", "Sí", "Comprueba que se entendió.")],
    task=T("Lee el diálogo inventado: Sol dice: «Tú nunca me ayudas con el afiche, eres un flojo». Cristóbal responde: «No tengo por qué ayudarte». Reescribe lo que dice Sol como mensaje «yo» de tres partes y escribe una frase de Cristóbal que parafrasee lo que Sol siente.", "Sol: «Cuando hago el afiche sola me siento cansada; necesito que me ayudes con los dibujos». Cristóbal: «Entonces te sientes cansada porque haces todo sola, ¿es así?».", ["mensaje «yo» con tres partes", "frase que parafrasea", "sin insultos", "no culpa a nadie"], ["dos frases escritas"], ["acusar con «tú siempre»", "parafrasear con ironía"], "Reconoce los mensajes y pregunta cómo seguiría el diálogo."),
    reinforce="Escribe un mensaje «yo» para una situación de tu elección con un personaje de cuento.",
    extend="Explica la diferencia entre hecho e interpretación con un ejemplo inventado.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. El caso del proyecto de Ana y Pablo y las cuatro formas de enfrentar el conflicto están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé cuatro formas de enfrentar un conflicto: evitar, imponer, ceder y colaborar, y a comparar sus consecuencias. Sirve para elegir la que permite una solución respetuosa y justa.",
    ["Sé usar mensajes «yo».", "Sé escuchar de manera empática."],
    [
        "Hay cuatro formas de enfrentar un conflicto. Evitar es hacer como si no existiera: no se resuelve y suele crecer. Imponer es lograr lo que uno quiere sin escuchar al otro: puede ganar uno, pero se daña la relación. Ceder es aceptar todo lo que quiere el otro para evitar el problema: se pierde lo que uno necesita. Colaborar es buscar entre ambos una solución que atienda los intereses de los dos.",
        "Colaborar es la forma que mejor permite resolver sin violencia. Sus pasos son: calmarse, escuchar los intereses de ambos, pensar varias soluciones, elegir la que sirve a los dos y acordar cómo se revisará. Una solución en que ambos ganan algo se llama «ganar-ganar». No siempre se logra, pero la intención de buscarla cambia el tono.",
        "Cada forma puede servir en una ocasión: evitar puede ser sensato si hay peligro o hay que calmarse; ceder, si el tema no importa mucho. Pero si el tema es importante y la relación también, conviene colaborar. Siempre se descarta la violencia. Si el conflicto incluye amenazas o golpes, hay que pedir ayuda a una persona adulta.",
    ],
    [("evitar", "no enfrentar el conflicto"), ("imponer", "conseguir lo que uno quiere sin escuchar al otro"), ("ceder", "aceptar lo que el otro quiere dejando lo propio de lado"), ("colaborar", "buscar entre ambos una solución que sirva a los dos"), ("ganar-ganar", "solución en que ambas partes logran algo")],
    [
        W("Clasificar la forma", "Ana y Pablo quieren presentar su proyecto de formas distintas. Ana dice: «Se hace como yo digo». ¿Evita, impone, cede o colabora?", ["Ana quiere lo suyo sin escuchar.", "No negocia.", "Impone."], "Impone"),
        W("Buscar un ganar-ganar", "Ana quiere hacer un afiche y Pablo un video. Proponen un afiche con un código para ver un video corto. ¿Qué forma usan?", ["Buscan algo que sirva a ambos.", "Los dos logran algo.", "Colaboran."], "Colaboran: es un ganar-ganar"),
    ],
    [
        M("Creer que ceder siempre es ser buena persona.", "Se confunde amabilidad con dejar de lado lo propio.", "Ceder sirve en temas menores; en lo importante, colabora."),
        M("Pensar que colaborar significa que ambos obtienen todo.", "Se ignora que hay que negociar.", "Colaborar es buscar una solución que sirva a los dos."),
    ],
    R=[
        ex("Hacer como si el problema no existiera, ¿es evitar o colaborar?", "Evitar", "No enfrenta el conflicto."),
        ex("Buscar una solución que sirva a ambos, ¿es colaborar o imponer?", "Colaborar", "Atiende los intereses de los dos."),
        ex("Aceptar todo lo que quiere el otro para no discutir, ¿es ceder o colaborar?", "Ceder", "Deja de lado lo propio."),
    ],
    U=[
        ex("¿Qué forma suele dañar más la relación? A) Imponer. B) Colaborar.", "A", "Ignora lo que necesita el otro."),
        ex("¿Una solución ganar-ganar atiende los intereses de uno o de ambos?", "De ambos", "Esa es su definición."),
        ex("Si hay amenazas o golpes en un conflicto, ¿se resuelve solo o se pide ayuda a una persona adulta?", "Se pide ayuda a una persona adulta", "Hay riesgo y se necesita apoyo."),
    ],
    A=[
        ex("Cuatro respuestas en un grupo: 1) «Hagamos lo mío»; 2) «Lo que quieran»; 3) «No hablemos de eso»; 4) «Cada uno diga qué necesita y busquemos una opción que sirva a todos». ¿Cuál colabora?", "La 4", "Escucha los intereses y busca una solución común."),
        ex("Pía y Tomás quieren usar la sala al mismo tiempo. Ella propone dividir el tiempo en dos mitades. ¿Qué forma usa? A) Colaborar. B) Imponer.", "A", "Busca una solución que atienda a ambos."),
        ex("Un joven decide ceder en un tema que no le importa para ahorrar tiempo. ¿Es una buena decisión, sí o no?", "Sí", "Ceder en temas menores puede ser sensato."),
    ],
    Z=[
        ex("¿Por qué imponer puede parecer ganar, pero no resolver?", "Porque el conflicto sigue y se daña la relación", "El otro no queda conforme y puede responder después."),
        ex("Explica una situación en que evitar un conflicto sea sensato.", "Cuando hay peligro o hay que calmarse antes de hablar", "Evitar por un momento puede proteger y permitir pensar."),
    ],
    D=[
        arith("En un curso de 36 estudiantes, 16 eligieron colaborar, 9 ceder, 6 evitar y el resto imponer. ¿Cuántos eligieron imponer?", "36-16-9-6", "Al total se le restan los otros grupos."),
        arith("Cada grupo de 4 propone 3 soluciones y hay 8 grupos. ¿Cuántas soluciones se reúnen?", "8*3", "Se multiplican los grupos por las soluciones de cada uno."),
    ],
    context=[ex("Dos grupos de 8.º quieren la cancha a la misma hora. Uno dice «es nuestra», el otro «también». ¿Qué solución colaborativa pueden proponer?", "Dividir el tiempo o alternar los días", "Atiende los intereses de ambos grupos.")],
    selfcheck=[ex("En Orientación: ¿colaborar busca una solución para ambos?", "Sí", "Atiende a los dos."), ex("¿Imponer escucha al otro?", "No", "No lo toma en cuenta."), ex("¿Se descarta la violencia?", "Sí", "Nunca es una solución.")],
    task=T("Lee el caso inventado: Sebastián y Valeria quieren elegir el tema de la exposición. Sebastián prefiere el mar y Valeria el espacio. Escribe una tabla con las cuatro formas (evitar, imponer, ceder, colaborar): qué dirían y qué consecuencia tendría. Después propone una solución ganar-ganar.", "Evitar: no deciden y se atrasan. Imponer: gana uno y el otro se molesta. Ceder: uno se queda sin lo que quería. Colaborar: eligen «planetas con océanos» o combinan los temas. Solución: comparar el océano de la Tierra con los de otros planetas.", ["describe las cuatro formas", "anota consecuencias", "propone un ganar-ganar", "no culpa a nadie"], ["tabla de cuatro filas"], ["decir que ceder siempre es mejor", "no prever consecuencias"], "Reconoce la tabla y pregunta qué paso seguiría para acordar la solución."),
    reinforce="Escribe un ejemplo de cada forma de enfrentar un conflicto con personajes de cuento.",
    extend="Explica cuándo conviene colaborar y cuándo ceder.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. El conflicto del recreo y los pasos de resolución están escritos en los ejercicios. Todo es inventado.",
    "Aprenderé una secuencia de pasos para resolver un conflicto con respeto y a reconocer cuándo debo pedir ayuda. Sirve para actuar de forma segura ante desacuerdos reales.",
    ["Sé separar hechos de interpretaciones.", "Sé las cuatro formas de enfrentar un conflicto."],
    [
        "Una acción segura ante un conflicto sigue pasos. Primero, calmarse: respirar, alejarse un momento y esperar a poder hablar sin gritar. Segundo, hablar con un mensaje «yo». Tercero, escuchar con empatía y parafrasear. Cuarto, pensar varias soluciones juntos. Quinto, elegir una y acordar cómo se revisará. Si ambos están de acuerdo, se agradece y se cumple.",
        "A veces el diálogo no basta: si hay amenazas, golpes, burlas repetidas o miedo, ya no es solo un conflicto, es violencia. En ese caso, no hay que enfrentarlo solo ni intentar convencer a quien agrede. Se debe pedir ayuda a una persona adulta, como el profesor jefe, el orientador o el equipo de convivencia escolar, que pueden mediar.",
        "Mediar es ayudar a dos partes a conversar con orden y respeto, sin tomar partido. La mediación la hace una persona neutral que cuida que cada uno hable y escuche. Si el conflicto se resuelve, se escribe un acuerdo. Si no, se pide ayuda a una persona adulta. Pedir ayuda a tiempo es una señal de madurez.",
    ],
    [("calmarse", "bajar la rabia o la tensión antes de hablar"), ("mediar", "ayudar a dos partes a conversar sin tomar partido"), ("neutral", "que no toma partido por ninguna parte"), ("acuerdo", "decisión que ambos aceptan"), ("convivencia escolar", "equipo y forma de relacionarse en el colegio")],
    [
        W("Ordenar los pasos", "Ordena: elegir una solución, calmarse, escuchar y parafrasear, hablar con mensaje «yo».", ["Primero se calma.", "Luego habla con mensaje «yo».", "Después escucha y parafrasea; al final elige una solución."], "Calmarse, hablar con mensaje «yo», escuchar y parafrasear, elegir una solución"),
        W("Cuándo pedir ayuda", "Un compañero amenaza a Ema después de un desacuerdo y ella tiene miedo. ¿Qué hace?", ["Hay amenaza y miedo.", "No es solo un conflicto.", "Avisa a una persona adulta."], "Avisar a una persona adulta, como el profesor jefe o convivencia escolar"),
    ],
    [
        M("Hablar apenas se siente rabia.", "Se piensa que hay que reaccionar rápido.", "Primero calma, luego conversa."),
        M("Creer que pedir ayuda a un adulto es rendirse.", "Se quiere resolver todo solo.", "Hay situaciones en que la ayuda es necesaria."),
    ],
    R=[
        ex("El primer paso para resolver un conflicto, ¿es calmarse o gritar?", "Calmarse", "Permite hablar sin agredir."),
        ex("Si hay amenazas, ¿lo resuelves solo o pides ayuda a un adulto?", "Pides ayuda a un adulto", "Hay un riesgo real."),
        ex("Una persona que media, ¿toma partido o es neutral?", "Es neutral", "No favorece a ninguna parte."),
    ],
    U=[
        ex("¿Qué paso va después de hablar con mensaje «yo»? A) Escuchar con empatía. B) Imponer.", "A", "Es el siguiente paso."),
        ex("¿Qué se escribe al final de una mediación exitosa?", "Un acuerdo", "Registra lo que ambos aceptan."),
        ex("Si el diálogo no resuelve y hay burlas repetidas, ¿es solo un conflicto o ya hay violencia?", "Ya hay violencia", "Las burlas repetidas dañan."),
    ],
    A=[
        ex("Pasos desordenados: 1) elegir una solución; 2) calmarse; 3) escuchar; 4) mensaje «yo»; 5) revisar. ¿Cuál es el primero?", "El 2", "Calmarse permite hablar sin gritar."),
        ex("Dos amigas se gritan sin escucharse. Un compañero se ofrece a mediar sin favorecer a ninguna. ¿Qué rol cumple? A) Persona neutral. B) Juez.", "A", "No toma partido."),
        ex("Tomás acuerda con Julia turnos para usar el computador de la sala. ¿Qué paso cumplió?", "Elegir una solución y acordar", "Llegaron a un acuerdo."),
    ],
    Z=[
        ex("¿Por qué conviene calmarse antes de hablar?", "Porque con rabia se dicen cosas que dañan", "Calmarse permite escuchar y expresarse sin agredir."),
        ex("Un joven dice: «Si pido ayuda, parezco débil». ¿Qué le responderías?", "Que pedir ayuda a tiempo es una señal de madurez", "Cuidar la seguridad es responsable."),
    ],
    D=[
        arith("Un curso medió 12 conflictos en el año y logró acuerdos en 9. ¿En cuántos no hubo acuerdo?", "12-9", "Al total se le restan los que sí tuvieron acuerdo."),
        arith("Un taller ensaya 5 pasos con 4 conflictos distintos. ¿Cuántos pasos ensaya en total?", "5*4", "Se multiplican los pasos por los conflictos."),
    ],
    context=[ex("En el recreo, Camila y Rafael discuten porque ella dice que él rompió su lápiz. Ella está muy enojada. ¿Qué debe hacer primero?", "Calmarse antes de hablar", "Es el primer paso para dialogar sin agresión.")],
    selfcheck=[ex("En Orientación: ¿el primer paso es calmarse?", "Sí", "Permite hablar sin agredir."), ex("¿Una persona neutral toma partido?", "No", "Debe ser neutral."), ex("¿Se debe pedir ayuda cuando hay amenazas?", "Sí", "Es una situación de riesgo.")],
    task=T("Lee el conflicto inventado: Ámbar y Nico discuten porque él compartió una foto del grupo sin avisarle y ella se enojó. Escribe el diálogo de cinco pasos: cómo se calman, un mensaje «yo» de Ámbar, una frase de Nico que parafrasee, dos soluciones posibles y un acuerdo final. Incluye qué harían si hubiera amenazas.", "Calma: se alejan un momento. Ámbar: «Cuando subes fotos sin avisarme me enojo; necesito que me preguntes». Nico: «Entonces te enojaste porque no te avisé, ¿es así?». Soluciones: preguntar antes o subir solo fotos aprobadas. Acuerdo: preguntar siempre. Amenazas: pedir ayuda a un adulto.", ["incluye los cinco pasos", "usa mensaje «yo» y parafraseo", "propone dos soluciones y un acuerdo", "dice qué hacer ante amenazas"], ["diálogo escrito"], ["saltarse la calma", "no pedir ayuda ante amenazas"], "Reconoce los pasos y pregunta cómo revisarán el acuerdo."),
    reinforce="Escribe los cinco pasos de resolución de un conflicto con tus palabras.",
    extend="Explica por qué ciertos conflictos requieren ayuda de una persona adulta.",
)
