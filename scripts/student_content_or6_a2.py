"""Cuaderno del estudiante, 6.º básico Orientación: OA 03 (desarrollo afectivo y sexual en la pubertad) y OA 04 (conductas protectoras y de autocuidado)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or6_a import M, T, W, lesson

OA3, OA4 = "OR06 OA 03", "OR06 OA 04"

# ================================================================ OA 03
lesson(
    OA3, 1,
    "Una hoja y un lápiz. Las listas de cambios y los casos de personajes inventados están escritos en los ejercicios. Nadie debe mostrar su cuerpo ni contar cosas privadas.",
    "Aprenderé qué es la pubertad y qué cambios físicos trae en niñas y en niños. Sirve para entender mi cuerpo y el de otras personas y cuidarlo con respeto.",
    ["Sé que mi cuerpo es mío y merece respeto.", "Sé que cada persona crece a su propio ritmo."],
    [
        "La pubertad es la etapa en que el cuerpo cambia para pasar de la niñez a la adolescencia. Suele empezar entre los 8 y los 14 años, pero puede empezar antes o después y sigue siendo normal. Los cambios los provocan las hormonas, que son sustancias que produce el cuerpo y que le indican cómo crecer y madurar.",
        "Algunos cambios son comunes a todas las personas: un crecimiento rápido en estatura (el estirón), vello en axilas y en otras zonas del cuerpo, más sudor y olor corporal, y piel con más grasa, por lo que pueden salir granos. Otros cambios son distintos. En las niñas crecen los pechos, se ensanchan las caderas y llega la menstruación, un sangrado normal que ocurre cada cierto tiempo. En los niños cambia la voz, sale vello en la cara y aumentan los músculos. En ambos maduran los órganos reproductores, y los niños pueden tener salidas involuntarias de semen durante el sueño, que son normales.",
        "Cada cuerpo cambia a su propio ritmo. Que un compañero cambie antes o después que tú no significa que algo esté mal. Para cuidar tu cuerpo durante la pubertad, adopta hábitos de higiene: ducharte con agua y jabón, lavar las axilas, cambiar tu ropa interior y usar ropa limpia cada día. Si algo te preocupa de tu cuerpo, puedes preguntarle a un adulto de confianza o a un profesional de la salud.",
    ],
    [("pubertad", "etapa en que el cuerpo cambia al pasar de la niñez a la adolescencia"), ("hormonas", "sustancias del cuerpo que le indican cómo crecer y cambiar"), ("menstruación", "sangrado normal y periódico que ocurre en las niñas durante la pubertad"), ("estirón", "crecimiento rápido en estatura"), ("higiene", "hábitos de limpieza para cuidar el cuerpo")],
    [
        W("Reconocer un cambio común", "Teo nota que ahora suda más y que su cuerpo huele más fuerte que antes. ¿Es un cambio de la pubertad?", ["La pubertad trae más sudor y olor corporal.", "Ocurre en niñas y en niños.", "Se cuida con higiene diaria."], "Sí, es un cambio de la pubertad"),
        W("Cada cuerpo tiene su ritmo", "Sam empezó a crecer antes que su amigo Luis y Luis se preocupa porque aún no cambia. ¿Qué frase es justa: «Cada persona cambia a su ritmo; es normal» o «Algo anda mal contigo»?", ["La pubertad empieza a edades distintas.", "Cambiar antes o después es normal.", "Hay que respetar el ritmo de cada uno."], "«Cada persona cambia a su ritmo; es normal»"),
    ],
    [
        M("Pensar que si mi cuerpo cambia más tarde, algo está mal.", "Se compara con otros sin saber que el ritmo es distinto.", "Recuerda que la pubertad empieza a edades diferentes."),
        M("Comentar el cambio del cuerpo de otro para reírse.", "Se confunde curiosidad con burla.", "Respeta el cuerpo de los demás y no hagas comentarios que hieran."),
    ],
    R=[
        ex("Las hormonas son sustancias que produce el cuerpo. ¿Qué hacen durante la pubertad: indican al cuerpo cómo crecer y cambiar o solo sirven para dormir?", "Indican al cuerpo cómo crecer y cambiar", "Son las responsables de los cambios físicos y afectivos de esta etapa."),
        ex("«Sudar más y tener más olor corporal». ¿Es un cambio físico de la pubertad?", "Sí", "Aparece en niñas y niños durante la pubertad."),
        ex("¿Qué significa «dar un estirón»?", "Crecer rápido en estatura", "Es un aumento rápido de la altura del cuerpo."),
    ],
    U=[
        ex("Dos amigos de 11 años: uno ya dio el estirón y la otra todavía no. ¿Alguno de los dos tiene un problema?", "No", "La pubertad empieza a edades distintas y ambos están dentro de lo normal."),
        ex("¿La menstruación es un sangrado normal y periódico de la pubertad o una herida que hay que ocultar?", "Un sangrado normal y periódico", "Es parte del desarrollo de las niñas y no hay que esconderla con vergüenza."),
        ex("¿Para qué sirve la higiene diaria durante la pubertad?", "Para cuidar el cuerpo y evitar el mal olor", "El sudor aumenta y se debe limpiar el cuerpo."),
    ],
    A=[
        ex("Lista: 1) estirón; 2) cambio de voz; 3) mochila nueva; 4) más vello en el cuerpo; 5) perder un diente de leche. ¿Cuántos son cambios de la pubertad?", "3", "Los números 1, 2 y 4 son cambios de la pubertad; la mochila y el diente de leche no lo son."),
        ex("Noa se ducha con jabón y cambia su ropa interior todos los días. ¿Qué hábito practica: higiene o descanso?", "Higiene", "Limpiar el cuerpo y cambiar la ropa es higiene."),
        ex("Una compañera inventada nota que le salieron granos en la cara. ¿Cuál es una respuesta respetuosa: «Es común en la pubertad» o «Qué asco»?", "«Es común en la pubertad»", "Reconoce el cambio sin burlarse."),
    ],
    Z=[
        ex("Un grupo dice: «Si alguien no ha cambiado todavía, no es normal». ¿Tienen razón?", "No", "La pubertad puede empezar más temprano o más tarde."),
        ex("¿Por qué es mejor preguntar a un adulto de confianza o a un profesional de la salud que a un compañero cuando algo del cuerpo preocupa?", "Porque pueden dar información segura", "Un compañero puede equivocarse o inventar."),
    ],
    D=[
        arith("En un curso de 36 estudiantes, 9 ya notaron el estirón. ¿Cuántos todavía no lo notan?", "36-9", "Se restan los que ya lo notaron al total."),
        arith("Una estudiante inventada medía 141 cm y creció 7 cm en un año. ¿Cuánto mide ahora?", "141+7", "Se suma lo que creció a su estatura anterior."),
    ],
    context=[ex("En clase, la profesora dice: «Los cambios del cuerpo se notan primero en unos y después en otros». Leo responde: «Entonces mi ritmo no es mejor ni peor que el de mis compañeros». ¿Entendió bien?", "Sí", "Reconoció que cada persona cambia a su ritmo.")],
    selfcheck=[ex("En Orientación: ¿los cambios de la pubertad ocurren solo en las niñas?", "No", "Ocurren en niñas y en niños, aunque no son idénticos."), ex("¿Se deben hacer burlas sobre los cambios del cuerpo de otros?", "No", "Hay que respetar a las personas."), ex("¿La higiene ayuda a cuidar el cuerpo en la pubertad?", "Sí", "Limpiarse bien es un hábito de autocuidado.")],
    task=T("Clasifica en «cambio de la pubertad» o «no es de la pubertad»: crecer rápido, mojarse por la lluvia, sudar más, tener sueño por la noche, que cambie la voz. Después escribe una frase respetuosa que le dirías a un amigo inventado que se preocupa porque su cuerpo todavía no ha cambiado.", "Pubertad: crecer rápido, sudar más, que cambie la voz. No: mojarse por la lluvia, tener sueño por la noche. Frase: «Cada uno cambia a su ritmo; es normal».", ["clasifica las cinco frases", "escribe una frase respetuosa", "no habla de su propio cuerpo"], ["lista escrita o dicha"], ["decir una edad exacta igual para todos", "burlarse de un cambio"], "Reconoce la clasificación y pregunta qué hábito de higiene ayuda con el cambio de sudor."),
    reinforce="Escribe tres cambios físicos de la pubertad y un hábito de higiene para cuidarse.",
    extend="Explica con tus palabras por qué el ritmo de cambio es distinto en cada persona.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. Los casos de Maite y de Ian, personajes inventados, y las frases están escritos en los ejercicios.",
    "Aprenderé qué cambios afectivos trae la pubertad: emociones más intensas, cambios de ánimo y necesidad de privacidad. Sirve para entender lo que siento y tratar con respeto lo que sienten otros.",
    ["Sé nombrar emociones y medir su intensidad.", "Sé que la pubertad trae cambios físicos."],
    [
        "En la pubertad no cambia solo el cuerpo; también cambian los afectos, es decir, la forma de sentir. Las emociones se pueden sentir más fuertes que antes. Es común pasar rápido de la alegría al enojo o a la tristeza sin una razón clara. Esto se debe en parte a las hormonas, y es normal. No significa que estés enfermo ni que seas «dramático».",
        "Aparecen también nuevas necesidades. Muchas personas quieren más privacidad: tener su espacio, que no revisen su cuaderno o sus mensajes sin permiso y decidir qué cuentan. Esa privacidad tiene un límite: si algo pone en riesgo tu seguridad, los adultos que te cuidan deben saberlo. También crece la sensibilidad a lo que opinan los demás, y puede surgir interés o enamoramiento por otras personas. Todo eso es parte del desarrollo y no hay que sentir vergüenza por ello.",
        "Para cuidar tus afectos, nombra lo que sientes y su intensidad, pide un momento si estás alterado y habla con un adulto de confianza si una emoción pesa mucho o dura muchos días. Con los demás, recuerda que un cambio de ánimo no justifica tratar mal a otro: puedes explicar lo que te pasa y pedir comprensión. Y respeta cuando alguien necesita estar solo un rato.",
    ],
    [("afecto", "forma de sentir y de querer a otros"), ("cambio de ánimo", "paso rápido de una emoción a otra"), ("privacidad", "derecho a tener un espacio y cosas propias que otros no revisan sin permiso"), ("enamoramiento", "sentir una atracción y cariño especial por otra persona"), ("comprensión", "intentar entender lo que le pasa al otro")],
    [
        W("Reconocer un cambio afectivo", "Maite estaba feliz en el recreo y diez minutos después se siente muy triste sin saber por qué. ¿Es algo que puede ocurrir en la pubertad?", ["Las hormonas pueden provocar cambios rápidos de ánimo.", "Maite no está enferma ni exagerando.", "Es común en esta etapa."], "Sí, puede ocurrir en la pubertad"),
        W("Respetar la privacidad", "Ian pide que no lean su cuaderno de dibujos sin permiso. ¿Qué respuesta respeta su privacidad: «Claro, lo respeto» o «Si no me dejas, algo ocultas»?", ["La privacidad es un derecho.", "Pedir un espacio propio no significa ocultar algo malo.", "La respuesta respetuosa acepta el límite."], "«Claro, lo respeto»"),
    ],
    [
        M("Pensar que cambiar de ánimo rápido significa estar mal de la cabeza.", "Se desconoce que los afectos cambian en la pubertad.", "Nombra lo que sientes y pide ayuda solo si dura mucho o pesa demasiado."),
        M("Burlarse de alguien porque le gusta otra persona.", "Se confunde intimidad con tema de chiste.", "Respeta lo que sienten los demás y no lo cuentes sin permiso."),
    ],
    R=[
        ex("¿Los cambios rápidos de ánimo pueden ser normales en la pubertad? Responde sí o no.", "Sí", "Las hormonas pueden hacer que las emociones cambien rápido."),
        ex("Querer más espacio propio y que no revisen mis cosas sin permiso, ¿es privacidad o es hacer algo malo?", "Es privacidad", "Tener un espacio propio es un derecho."),
        ex("Sentir una atracción y cariño especial por otra persona, ¿es enamoramiento o enojo?", "Enamoramiento", "Así se llama ese sentimiento especial por otra persona."),
    ],
    U=[
        ex("¿Por qué sentir emociones más intensas en la pubertad no es una enfermedad?", "Porque es parte del desarrollo", "Se debe en parte a las hormonas y le pasa a muchas personas."),
        ex("¿Un mal día de ánimo justifica tratar mal a otro? Responde sí o no.", "No", "Se puede explicar lo que pasa y pedir comprensión sin herir."),
        ex("Si una tristeza fuerte dura muchos días, ¿qué conviene hacer: hablar con un adulto de confianza o guardarlo?", "Hablar con un adulto de confianza", "Un adulto puede ayudar a manejarla."),
    ],
    A=[
        ex("Frases: 1) «Quiero más tiempo a solas»; 2) «Me sorprendo llorando por cosas pequeñas»; 3) «Me da vergüenza que me miren»; 4) «Me encanta el helado de chocolate». ¿Cuántas pueden ser cambios afectivos de la pubertad?", "3", "Las frases 1, 2 y 3 hablan de privacidad, emociones intensas y sensibilidad a la opinión de otros."),
        ex("Maite se siente muy enojada y contesta mal a su hermana. ¿Qué es mejor después: pedir disculpas y explicar que estaba alterada, o decir que su hermana tuvo la culpa?", "Pedir disculpas y explicar que estaba alterada", "Reconoce su error y cuida la relación."),
        ex("Un compañero quiere estar solo en el recreo. ¿Cuál es una respuesta respetuosa? A) «Déjame acompañarte aunque no quieras». B) «Está bien; si quieres hablar, aquí estoy». C) «Qué raro eres».", "B", "Respeta su necesidad y ofrece apoyo."),
    ],
    Z=[
        ex("¿Por qué contar a otros el secreto de enamoramiento de un compañero sin su permiso es una falta de respeto?", "Porque es algo privado que le pertenece", "Cada persona decide qué comparte y con quién."),
        ex("Una amiga dice: «Ya no soy la misma, cambió mi humor». ¿Qué respuesta ayuda más: «Te escucho» o «Estás exagerando»?", "«Te escucho»", "Acompaña sin juzgar."),
    ],
    D=[
        arith("En una encuesta anónima de un curso de 30 estudiantes, 12 dijeron que a veces necesitan más tiempo a solas y 7 que a veces cambian de ánimo rápido, sin que nadie esté en ambos grupos. ¿Cuántos estudiantes no marcaron ninguna de las dos?", "30-12-7", "Al total se le restan los dos grupos distintos."),
        arith("Ian anotó su ánimo en una escala de 1 a 5: lunes 4, martes 2, miércoles 5. ¿Cuántos puntos de diferencia hay entre su día más bajo y el más alto?", "5-2", "Se restan el valor más bajo al más alto."),
    ],
    context=[ex("En el curso, Tomás se enoja con facilidad esta semana. Sofi le pregunta: «¿Te pasa algo? Si quieres hablar, aquí estoy». Tomás responde: «Hoy me siento raro, mejor más tarde». ¿Respetaron ambos los afectos del otro?", "Sí", "Sofi ofreció escuchar sin presionar y Tomás dijo lo que necesitaba.")],
    selfcheck=[ex("En Orientación: ¿tener más privacidad es parte de los cambios afectivos de la pubertad?", "Sí", "Muchas personas necesitan más espacio propio."), ex("¿Cambiar de ánimo rápido significa estar enfermo?", "No", "Es común en esta etapa."), ex("¿Se debe contar un enamoramiento ajeno sin permiso?", "No", "Es algo privado.")],
    task=T("Lee el caso de Rocío, una estudiante inventada: esta semana pasó de la risa al llanto varias veces, quiere cerrar la puerta de su pieza y le da vergüenza que sus compañeros sepan que le gusta alguien. Escribe tres cosas que le están pasando (cambio de ánimo, privacidad, vergüenza) y una frase que Rocío podría decirle a su familia para pedir comprensión.", "Le pasan: cambios rápidos de ánimo, necesidad de privacidad y sensibilidad a lo que piensan otros. Frase: «Estoy sintiendo cosas nuevas y a veces necesito estar sola; ¿puedes tener paciencia y preguntarme con cariño?»", ["identifica los tres cambios afectivos", "escribe una frase respetuosa para pedir comprensión", "no cuenta un enamoramiento propio ni ajeno"], ["texto escrito o dicho"], ["decir que algo anda mal con ella", "contar secretos de otros"], "Reconoce lo identificado y pregunta cómo podría la familia responder con cuidado."),
    reinforce="Escribe tres cambios afectivos de la pubertad y una forma de respetar a quien los vive.",
    extend="Explica por qué la privacidad ayuda a sentirse seguro y no significa ocultar algo malo.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. El caso del grupo de amigos y la tabla están escritos en los ejercicios.",
    "Aprenderé qué cambios sociales trae la pubertad: más peso de los amigos, presión de grupo y deseo de más autonomía. Sirve para tomar decisiones propias sin perder el respeto por los demás.",
    ["Sé que la pubertad trae cambios físicos y afectivos.", "Sé poner un límite con respeto."],
    [
        "Con la pubertad también cambian las relaciones sociales. Los amigos y el grupo empiezan a pesar más: se quiere ser aceptado, compartir gustos y pasar más tiempo con pares. Al mismo tiempo, muchas personas quieren más autonomía, es decir, tomar más decisiones por sí mismas, y a veces eso genera discusiones con la familia sobre horarios, permisos o salidas. Es una etapa de aprendizaje, no una pelea para ganar.",
        "Una consecuencia de estos cambios es la presión de grupo: sentir que debes hacer lo que hace el grupo para ser aceptado, aunque no quieras. La presión puede ser buena, como estudiar juntos, o dañina, como burlarse de alguien. Para resistirla, conviene detenerte y preguntar: ¿yo quiero hacerlo?, ¿daña a alguien?, ¿cumple las normas de mi casa y del colegio? Si la respuesta es no, puedes decir «no, gracias» sin dar mil explicaciones.",
        "También cambian las comparaciones: se mira más cómo se ve y cómo se comporta cada uno. Compararse mucho puede doler. Recuerda que todos cambian a su ritmo y que una buena amistad respeta tus decisiones. Si te cuesta decir que no o sientes que te excluyen, habla con un adulto de confianza.",
    ],
    [("autonomía", "capacidad de tomar decisiones por uno mismo"), ("presión de grupo", "sentir que debo hacer lo que hace el grupo para ser aceptado"), ("par", "persona de mi edad"), ("pertenecer", "sentirse parte de un grupo"), ("excluir", "dejar fuera a alguien de un grupo")],
    [
        W("Reconocer presión de grupo", "El grupo de Tomás se burla de un compañero y le dicen: «Ríete tú también o quedas fuera». ¿Es presión de grupo?", ["Le piden hacer algo para ser aceptado.", "La acción hiere a otra persona.", "Es presión de grupo dañina."], "Sí, es presión de grupo dañina"),
        W("Responder con firmeza", "Tomás no quiere reírse. ¿Qué respuesta le sirve: «No quiero burlarme de nadie» o «Ya, lo hago para que no me dejen solo»?", ["La primera dice lo que quiere sin atacar.", "La segunda cede a una acción que hiere.", "La firmeza sin ofensas protege sus valores."], "«No quiero burlarme de nadie»"),
    ],
    [
        M("Creer que si no hago lo que hace el grupo me quedaré solo siempre.", "Se piensa que ser aceptado vale más que decidir por uno mismo.", "Busca amistades que respeten tus decisiones."),
        M("Pensar que querer más autonomía significa no respetar las normas de la casa.", "Se confunde decidir con hacer lo que sea.", "Pide más libertad con acuerdos claros y responsabilidad."),
    ],
    R=[
        ex("Sentir que debes hacer lo que hace el grupo para ser aceptado, ¿es presión de grupo o autonomía?", "Presión de grupo", "La persona actúa por la aceptación y no por decisión propia."),
        ex("Tomar más decisiones por uno mismo, ¿es autonomía o exclusión?", "Autonomía", "Significa decidir con más independencia."),
        ex("¿Dejar fuera a alguien del grupo a propósito es excluir? Responde sí o no.", "Sí", "Excluir es apartar a una persona de un grupo."),
    ],
    U=[
        ex("¿Toda presión de grupo es mala? Responde sí o no.", "No", "Puede ser buena, como animarse a estudiar juntos."),
        ex("¿Qué pregunta ayuda a decidir ante presión: «¿qué hacen todos?» o «¿yo quiero hacerlo y daña a alguien?»?", "«¿Yo quiero hacerlo y daña a alguien?»", "Pensar en mi decisión y en el daño protege mis valores."),
        ex("¿Por qué una buena amistad no te exige hacer algo que te incomoda?", "Porque respeta tus decisiones", "Una amistad cuida a la otra persona."),
    ],
    A=[
        ex("Situaciones: 1) estudiar juntos para una prueba; 2) esconder el cuaderno de alguien por diversión; 3) acompañar a un compañero que está solo; 4) rayar la mesa porque «todos lo hacen». ¿Cuántas son presión de grupo dañina o acciones dañinas?", "2", "Las situaciones 2 y 4 hieren o dañan; las otras dos son positivas."),
        ex("Sofi quiere que la dejen ir a una plaza con amigas. ¿Qué propuesta muestra autonomía con responsabilidad? A) «Voy y listo». B) «Les aviso a qué hora vuelvo, con quién voy y les mando un mensaje al llegar». C) «No hablaré del tema».", "B", "Pide libertad con acuerdos claros."),
        ex("Un amigo te presiona a no hablar con un compañero nuevo. ¿Qué respuesta firme sirve: «Yo hablo con quien quiero» o «Tienes razón, no le hablo»?", "«Yo hablo con quien quiero»", "Defiende su decisión sin ofender."),
    ],
    Z=[
        ex("¿Por qué ceder siempre para ser aceptado puede dañar la valoración de uno mismo?", "Porque deja de decidir por sí mismo", "Cuando siempre se cede, se pierde la propia voz."),
        ex("¿Por qué pedir más autonomía con acuerdos es más probable que funcione que exigirla gritando?", "Porque da confianza a la familia", "Los acuerdos muestran responsabilidad."),
    ],
    D=[
        arith("En un curso de 32 estudiantes, 5 se sintieron presionados a hacer algo que no querían. ¿Cuántos no se sintieron presionados?", "32-5", "Se restan los presionados al total."),
        arith("Sofi pasa 3 tardes por semana con su grupo de amigas y 2 tardes con su familia. ¿Cuántas tardes de la semana dedica en total a su grupo de amigas y a su familia?", "3+2", "Se suman las tardes con cada grupo."),
    ],
    context=[ex("Un grupo le dice a Valentina que si no publica una burla de una compañera, la dejarán fuera. Ella responde: «No voy a publicar nada que hiera a alguien». ¿Resistió la presión de grupo?", "Sí", "Dijo que no a una acción dañina sin atacar al grupo.")],
    selfcheck=[ex("En Orientación: ¿los amigos suelen importar más en la pubertad?", "Sí", "Se busca pertenecer y compartir con pares."), ex("¿Se puede decir «no, gracias» a una presión dañina?", "Sí", "Es una forma de cuidar los propios valores."), ex("¿Pedir autonomía con acuerdos ayuda a tener confianza?", "Sí", "Muestra responsabilidad y genera confianza.")],
    task=T("Lee la situación de Gabo, un estudiante inventado: su grupo quiere que escriba una burla sobre un compañero en el chat del curso. Gabo no quiere y teme que lo dejen solo. Escribe: qué presión siente, una frase firme para decir que no sin atacar, y a quién podría pedir apoyo si el grupo lo excluye.", "Presión: hacer una burla para ser aceptado. Frase: «No voy a escribir eso, pero sí puedo escribir algo bueno». Apoyo: la profesora jefe o la orientadora.", ["nombra la presión", "escribe una frase firme y respetuosa", "nombra un apoyo adulto", "no cuenta una vivencia propia"], ["texto escrito o dicho"], ["ceder a la presión", "responder con insultos"], "Reconoce la frase y pregunta qué haría si el grupo insistiera."),
    reinforce="Escribe una frase firme para decir que no a tres presiones distintas sin insultar.",
    extend="Explica la diferencia entre ser aceptado y ser respetado.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. Los casos de personajes inventados están escritos en los ejercicios.",
    "Aprenderé a expresar afecto con respeto y a reconocer que el consentimiento y el «no» deben respetarse. Sirve para relacionarme con cuidado con amigos, familia y otras personas.",
    ["Sé que mi cuerpo es mío.", "Sé que la pubertad cambia lo que siento por otros."],
    [
        "Expresar afecto es mostrar cariño a otra persona. Se puede hacer de muchas formas: con palabras amables, con un gesto, ayudando o con un abrazo. Cada persona siente cómodo el afecto de una forma distinta. Lo importante es que el afecto sea respetuoso: que la otra persona quiera recibirlo y que no la incomode ni la presione.",
        "El consentimiento es que la persona acepte algo de forma libre, es decir, sin presión, engaño ni miedo. Si alguien dice «no», o se aleja, o parece incómodo, hay que detenerse y respetar. Eso vale para un abrazo, para una broma de contacto o para una foto. Un «sí» dicho por miedo o por presión no es un sí verdadero. Y tú también tienes derecho a decir «no» a un contacto que no quieres, aunque sea de alguien conocido.",
        "En la pubertad pueden aparecer nuevas motivaciones, como querer gustarle a alguien o querer estar con una persona especial. Una forma respetuosa de acercarse es conversar, preguntar qué le gusta al otro y aceptar su respuesta, sea cual sea. Si alguien te obliga, te chantajea o te hace sentir mal, no es afecto: avisa a un adulto de confianza.",
    ],
    [("afecto", "cariño que muestro a otra persona"), ("consentimiento", "aceptar algo de forma libre, sin presión, engaño ni miedo"), ("límite personal", "lo que acepto y lo que no en mi cuerpo y mis cosas"), ("chantaje", "presionar a alguien amenazándolo o haciéndolo sentir culpable"), ("respeto", "aceptar que el otro decida por sí mismo")],
    [
        W("Reconocer el consentimiento", "Ema le pregunta a su amiga: «¿Quieres un abrazo?». La amiga dice: «No, hoy no». ¿Qué debe hacer Ema?", ["La amiga dijo «no».", "Un «no» se respeta.", "Ema puede mostrar su cariño de otra manera, como con palabras."], "Respetar el «no» y mostrar su cariño de otra forma"),
        W("Detectar el chantaje", "Un niño dice: «Si de verdad me quisieras, me mandarías esa foto». ¿Es afecto o chantaje?", ["Presiona con la culpa.", "Pide algo que la otra persona no quiere hacer.", "Eso no es cariño."], "Chantaje"),
    ],
    [
        M("Pensar que si alguien no dice «no» en voz alta, entonces dijo «sí».", "Se confunde el silencio con aceptar.", "Pregunta y solo sigue si la persona acepta de forma clara y libre."),
        M("Creer que un «no» a un abrazo significa que no me quieren.", "Se toma personal una decisión sobre el cuerpo.", "Respeta el «no» y busca otras formas de expresar cariño."),
    ],
    R=[
        ex("Si alguien dice «no» a un abrazo, ¿se respeta o se insiste?", "Se respeta", "El cuerpo de cada uno es suyo y un «no» debe respetarse."),
        ex("Presionar a alguien diciéndole «si me quisieras lo harías», ¿es afecto o chantaje?", "Chantaje", "Usa la culpa para forzar."),
        ex("¿Se puede mostrar afecto con palabras amables? Responde sí o no.", "Sí", "El afecto no solo se muestra con contacto físico."),
    ],
    U=[
        ex("¿Por qué un «sí» dicho por miedo no es un sí verdadero?", "Porque no fue libre", "El consentimiento debe darse sin presión ni miedo."),
        ex("¿Cuál es una forma respetuosa de acercarse a alguien que te gusta: conversar y aceptar su respuesta o insistir hasta que diga que sí?", "Conversar y aceptar su respuesta", "Respetar su decisión es parte del afecto."),
        ex("Si alguien te obliga a algo y te dice que es un secreto, ¿qué haces?", "Aviso a un adulto de confianza", "Un secreto que obliga a hacer algo incómodo no debe guardarse."),
    ],
    A=[
        ex("Frases: 1) «¿Te parece si te doy un abrazo?»; 2) «Si no me abrazas, me enojo contigo»; 3) «Te regalo este dibujo para que sepas que te quiero»; 4) «Si de verdad eres mi amigo, hazlo». ¿Cuántas respetan el consentimiento?", "2", "Las frases 1 y 3 no presionan; la 2 y la 4 sí."),
        ex("Rocío no quiere que su primo le dé besos aunque la familia diga que «es cariño». ¿Tiene derecho a decir no? Responde sí o no.", "Sí", "Su cuerpo es suyo, aunque sea alguien conocido."),
        ex("Un compañero dice que no quiere participar en un juego de contacto. ¿Qué respuesta respeta su límite? A) «No pasa nada, juega otra cosa». B) «No seas aburrido». C) «Solo un rato más».", "A", "Acepta su decisión sin presionar."),
    ],
    Z=[
        ex("¿Por qué es mejor preguntar «¿quieres?» antes de un contacto físico que suponer que sí?", "Porque solo la otra persona sabe lo que quiere", "Preguntar evita incomodar o dañar."),
        ex("¿Por qué el afecto verdadero no necesita presiones ni chantajes?", "Porque cuida y respeta a la otra persona", "Si hay presión, no hay respeto."),
    ],
    D=[
        arith("En un curso de 28 estudiantes, 24 dicen que un «no» siempre debe respetarse. ¿Cuántos no lo dicen o dudaron?", "28-24", "Se restan los que están de acuerdo al total."),
        arith("Una niña inventada ofreció 3 formas de mostrar cariño el lunes y 2 el martes. ¿Cuántas ofreció en total?", "3+2", "Se suman las formas de cada día."),
    ],
    context=[ex("Bruno le dice a un compañero: «Me caes muy bien. ¿Quieres que juguemos juntos en el recreo?». El compañero responde: «Hoy prefiero estar solo». Bruno dice: «Está bien, otro día». ¿Expresó afecto de forma respetuosa?", "Sí", "Preguntó, escuchó el «no» y lo aceptó.")],
    selfcheck=[ex("En Orientación: ¿un «no» debe respetarse?", "Sí", "Cada persona decide sobre su cuerpo."), ex("¿El chantaje es una forma de afecto?", "No", "Usa la culpa o el miedo."), ex("¿Puedo mostrar cariño sin contacto físico?", "Sí", "Con palabras, gestos o ayuda.")],
    task=T("Lee los tres casos de personajes inventados: (1) Ema abraza a su amiga aunque ella baja la cabeza y se aleja; (2) Teo escribe «si me quisieras, contestarías ya»; (3) Luz le agradece a su compañero con un dibujo. Para cada caso, escribe si respeta el consentimiento o no, y qué haría una persona respetuosa.", "(1) No; debería parar, preguntar «¿quieres un abrazo?» y aceptar el «no». (2) No, es chantaje; debería decir «cuando puedas, avísame». (3) Sí, regala sin presionar.", ["clasifica los tres casos", "explica qué haría una persona respetuosa", "no cuenta una vivencia propia"], ["tabla escrita"], ["aceptar el chantaje como cariño", "no respetar el «no»"], "Reconoce la clasificación y pregunta qué otra forma de mostrar cariño sin contacto elegiría."),
    reinforce="Escribe tres frases para ofrecer afecto de forma respetuosa y una para decir «no» con calma.",
    extend="Explica por qué el consentimiento puede cambiar: lo que hoy acepto, mañana puedo no querer.",
)

lesson(
    OA3, 5,
    "Una hoja y un lápiz. Las preguntas, las fuentes y las frases están escritas en los ejercicios.",
    "Aprenderé a pedir ayuda y a buscar información confiable sobre los cambios de la pubertad. Sirve para resolver dudas sin pasar vergüenza ni informarme mal.",
    ["Sé que mi cuerpo y mi intimidad tienen límites.", "Sé que puedo contar con un adulto de confianza."],
    [
        "Es normal tener dudas sobre la pubertad: ¿por qué cambia mi voz?, ¿qué es la menstruación?, ¿por qué me da tanta vergüenza? Preguntar es una forma de cuidarte. Elige a una persona adulta de confianza: alguien de tu casa, tu profesor o profesora, el orientador o un profesional de la salud. Puedes empezar con: «Tengo una duda y me da vergüenza preguntar. ¿Podemos hablar?».",
        "No toda la información sirve. Una fuente confiable tiene autor o institución que se puede identificar, como un centro de salud, un hospital, un ministerio o un libro de la biblioteca del colegio. Usa un lenguaje claro y respetuoso, es actual y no pide datos personales. Una fuente poco confiable promete «secretos», no dice quién escribe o pide datos como tu nombre completo o tu dirección.",
        "Si un compañero te cuenta algo sobre los cambios del cuerpo, puede estar equivocado. Antes de creerlo, compáralo con una fuente confiable o pregunta a un adulto. Si alguien te da información que te incomoda o te pide guardar un secreto sobre tu cuerpo, avisa a un adulto de confianza. Tener una duda no es algo malo, y hay personas preparadas para ayudarte.",
    ],
    [("duda", "pregunta que aún no tiene respuesta"), ("fuente confiable", "lugar de información con autor o institución identificable y datos correctos"), ("adulto de confianza", "persona adulta con la que me siento seguro de hablar"), ("profesional de la salud", "persona formada para cuidar la salud"), ("comparar fuentes", "revisar si dos fuentes dicen lo mismo")],
    [
        W("Elegir a quién preguntar", "Una niña inventada tiene una duda sobre la menstruación. Puede preguntar a (a) un compañero que dice saber todo o (b) una profesional de la salud del consultorio. ¿Quién dará información más confiable?", ["Un compañero puede equivocarse.", "Una profesional de la salud estudió el tema.", "La información debe ser clara y segura."], "(b), la profesional de la salud"),
        W("Evaluar una fuente", "Una página dice: «Secretos que tus padres no te cuentan. Escribe tu nombre completo y tu dirección». ¿Es confiable?", ["Promete «secretos».", "Pide datos personales.", "No dice quién escribe."], "No es confiable"),
    ],
    [
        M("Creer todo lo que dice el compañero que habla con más seguridad.", "Se confunde seguridad al hablar con información correcta.", "Compara con una fuente confiable o pregunta a un adulto."),
        M("Quedarme con la duda porque me da vergüenza.", "Se piensa que preguntar es mostrar debilidad.", "Prepara una frase para pedir hablar con calma."),
    ],
    R=[
        ex("Si tienes una duda sobre la pubertad, ¿es bueno preguntarla a un adulto de confianza?", "Sí", "Preguntar es una forma de cuidarte."),
        ex("Una fuente confiable, ¿tiene autor o institución identificable o no se sabe quién escribe?", "Tiene autor o institución identificable", "Eso permite confiar en los datos."),
        ex("Una página que pide tu nombre completo y tu dirección para dar información, ¿es confiable?", "No", "Una fuente confiable no pide datos personales."),
    ],
    U=[
        ex("¿Por qué conviene revisar en una fuente confiable lo que escuchaste en el patio sobre la pubertad?", "Porque puede ser un rumor equivocado", "Los rumores se comprueban con información segura."),
        ex("¿Qué frase sirve para pedir ayuda: «Quiero preguntarte algo sobre mi cuerpo y me cuesta; ¿tienes un momento?» o «Da lo mismo, nada importa»?", "«Quiero preguntarte algo sobre mi cuerpo y me cuesta; ¿tienes un momento?»", "Dice lo que necesitas y pide un momento al adulto."),
        ex("Alguien te toca o te pide mostrar partes privadas de tu cuerpo y dice que es un secreto. ¿Qué haces?", "Digo no, me alejo y se lo cuento a un adulto de confianza", "Un secreto que daña no se guarda y un adulto puede protegerte."),
    ],
    A=[
        ex("Fuentes: 1) libro de la biblioteca del colegio con autor; 2) página sin autor que promete «trucos»; 3) sitio de un hospital público; 4) mensaje que pide tu dirección. ¿Cuántas son confiables?", "2", "El libro y el hospital tienen institución identificable; las otras no."),
        ex("Antes de hablar con un adulto, ¿qué ayuda más: anotar tres preguntas en una hoja o decidir no preguntar?", "Anotar tres preguntas en una hoja", "Escribir prepara lo que se quiere decir y baja la vergüenza."),
        ex("Un amigo dice: «Dicen que durante la pubertad no hay que bañarse». ¿Qué haces: compararlo con una fuente confiable o creerle?", "Compararlo con una fuente confiable", "La higiene es importante en la pubertad y hay que revisar."),
    ],
    Z=[
        ex("¿Por qué un adulto de confianza puede ser mejor para responder que una búsqueda sin criterio?", "Porque puede explicar con cuidado y conocerte", "Evita información equivocada o demasiado fuerte."),
        ex("¿Qué señal muestra que una fuente de información no es segura?", "Pide datos personales o promete secretos", "Una fuente segura informa sin pedir datos privados."),
    ],
    D=[
        arith("De 24 fuentes revisadas por un curso, 16 eran confiables. ¿Cuántas no lo eran?", "24-16", "Se restan las confiables al total."),
        arith("Rocío preparó 4 preguntas y le respondieron 3. ¿Cuántas quedan por preguntar?", "4-3", "Se resta lo respondido a lo preparado."),
    ],
    context=[ex("Un niño inventado ve en una página: «Hospital Regional: ¿Qué es la pubertad?». Tiene autor, fecha y no pide datos personales. ¿Es una fuente confiable?", "Sí", "Tiene institución, fecha y no pide datos personales.")],
    selfcheck=[ex("En Orientación: ¿es mejor informarme con una fuente confiable que con rumores?", "Sí", "Una fuente confiable da datos correctos."), ex("¿Una página que dice quién la escribe y no pide datos personales es una señal de confianza?", "Sí", "Una fuente identificable que respeta tu privacidad es más segura."), ex("¿Puedo pedir hablar con un adulto de confianza?", "Sí", "Es una forma de pedir ayuda.")],
    task=T("Escribe tres preguntas que podrías hacer sobre la pubertad (por ejemplo, sobre higiene, ánimo o cambios del cuerpo). Para cada una escribe a quién la harías y por qué. Después escribe una frase para empezar a conversar si sientes vergüenza.", "Pregunta: ¿cómo cuido mi cuerpo cuando sudo más? A: la orientadora, porque conoce hábitos de higiene. Frase: «Tengo una duda y me da vergüenza preguntar; ¿podemos hablar?»", ["tres preguntas con destinatario", "razón de por qué", "una frase para comenzar", "no incluye datos personales"], ["lista escrita o dicha"], ["elegir a quien no tiene información", "frase que ofende"], "Reconoce la preparación y pregunta cómo comprobaría la respuesta."),
    reinforce="Haz una lista de dos adultos de confianza a quienes podrías preguntar y una frase para cada uno.",
    extend="Explica por qué una fuente confiable no pide tu nombre completo ni tu dirección.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. Los casos de Ema y de Ian, personajes inventados, y las frases de ejemplo están escritos en los ejercicios.",
    "Aprenderé a comunicarme bien con mi familia o con un adulto de confianza: elegir el momento, decir lo esencial y escuchar. Sirve para contar lo que me preocupa y recibir ayuda a tiempo.",
    ["Sé que puedo pedir ayuda a un adulto de confianza.", "Sé armar un mensaje «yo»."],
    [
        "Una comunicación efectiva es aquella en que el mensaje llega y se entiende. Con tu familia o con un adulto de confianza ayuda a proteger tu bienestar, porque si ellos saben dónde estás, con quién y qué te pasa, te pueden cuidar mejor. Las personas de confianza no son siempre las mismas para todos: pueden ser alguien de tu casa, un profesor o profesora, el orientador o un familiar cercano.",
        "Para comunicarte bien, sigue cuatro pasos. Primero, elige el momento: cuando la persona pueda escucharte y no esté apurada. Segundo, di lo esencial de forma clara: qué pasó, cómo te sientes y qué necesitas. Tercero, escucha la respuesta sin interrumpir y pregunta si no entiendes. Cuarto, acuerden qué hacer y cuándo volver a conversar. Usa un mensaje «yo» y evita acusar.",
        "A veces es difícil decir algo que da vergüenza o miedo. Puedes empezar con «Necesito contarte algo importante» o escribirlo en una nota si te cuesta hablar. Si el primer adulto no te escucha o no te cree, no te rindas: busca a otro adulto de confianza. Contar algo a tiempo no es acusar; es cuidarte.",
    ],
    [("comunicación efectiva", "mensaje que llega claro y se entiende"), ("adulto de confianza", "persona adulta con la que me siento seguro de hablar"), ("lo esencial", "lo más importante que necesito decir"), ("escuchar", "prestar atención a la respuesta sin interrumpir"), ("acuerdo", "decisión que toman entre dos o más sobre qué hacer")],
    [
        W("Elegir el momento", "Ema quiere contarle algo importante a un adulto de su casa. Está cocinando con prisa y atendiendo una llamada. ¿Es buen momento para hablar?", ["La persona está ocupada.", "No podrá escuchar con atención.", "Es mejor esperar o pedir un momento."], "No, mejor pedir un momento después"),
        W("Decir lo esencial", "Ian recibió un mensaje que lo incomodó. ¿Qué frase dice lo esencial: «Pasó algo» o «Me llegó un mensaje de un desconocido que me incomodó y quiero mostrártelo»?", ["La primera es muy vaga.", "La segunda dice qué pasó, cómo se siente y qué necesita.", "Es la que permite recibir ayuda."], "«Me llegó un mensaje de un desconocido que me incomodó y quiero mostrártelo»"),
    ],
    [
        M("Callar algo importante porque creo que me van a retar.", "Se teme el enojo y se pierde la ayuda.", "Empieza diciendo «Necesito contarte algo importante y me da miedo» y pide calma."),
        M("Contar todo a la vez y rápido, sin elegir el momento.", "Se piensa que decir de inmediato basta.", "Elige un momento tranquilo y di lo esencial en pocas frases."),
    ],
    R=[
        ex("¿Los cuatro pasos de una comunicación efectiva incluyen elegir el momento? Responde sí o no.", "Sí", "El primer paso es elegir cuándo hablar."),
        ex("«Necesito contarte algo importante». ¿Sirve para empezar una conversación difícil? Responde sí o no.", "Sí", "Avisa que es importante y pide atención."),
        ex("Si el primer adulto no te escucha, ¿qué haces: buscar a otro adulto de confianza o quedarte callado?", "Buscar a otro adulto de confianza", "Insistir en pedir ayuda es parte de cuidarte."),
    ],
    U=[
        ex("¿Por qué conviene decir qué pasó, cómo te sientes y qué necesitas?", "Porque el otro entiende y puede ayudar", "Esos tres datos hacen el mensaje claro."),
        ex("¿Por qué conviene escuchar la respuesta sin interrumpir?", "Porque así se entiende el consejo o la ayuda", "Interrumpir impide comprender lo que el adulto quiere decir."),
        ex("Si te da vergüenza hablar, ¿puedes escribir una nota? Responde sí o no.", "Sí", "Escribir es una forma válida de empezar a contar."),
    ],
    A=[
        ex("Los pasos de una comunicación efectiva son: elegir el momento, decir lo esencial, escuchar la respuesta y acordar qué hacer. ¿Qué paso va justo antes de acordar qué hacer?", "Escuchar la respuesta", "Primero se escucha lo que responde el adulto y después se acuerda qué hacer."),
        ex("Ema debe avisar que irá a casa de una compañera. ¿Qué mensaje comunica mejor? A) «Voy a salir». B) «Voy a la casa de Valentina, una compañera del curso; vuelvo a las 18:00; te aviso cuando llegue». C) «Después te cuento».", "B", "Dice dónde, con quién y a qué hora, y promete avisar."),
        ex("Ian prepara lo que dirá: 1) qué pasó; 2) cómo se siente; 3) qué necesita. ¿Cuántas partes tiene su mensaje?", "3", "Son tres partes: hecho, emoción y petición."),
    ],
    Z=[
        ex("Un amigo piensa: «Si cuento, me van a quitar el celular». ¿Qué argumento puede ayudarle a decidir contar?", "Que contar a tiempo evita que el problema crezca", "El apoyo adulto evita que el problema empeore."),
        ex("¿Por qué contar algo a tiempo no es lo mismo que «acusar»?", "Porque busca cuidarse y no culpar", "El propósito es pedir ayuda y proteger a alguien."),
    ],
    D=[
        arith("Ema conversó con un adulto 2 veces la semana pasada y 3 veces esta semana. ¿Cuántas veces conversó entre las dos semanas?", "2+3", "Se suman las conversaciones de cada semana."),
        arith("Ian tiene 25 minutos para contar algo importante antes de que llegue una visita. Usa 5 minutos para preparar lo que dirá y 10 para conversar. ¿Cuántos minutos le quedan para acordar qué hacer?", "25-5-10", "Se restan los dos tiempos ya usados al total."),
    ],
    context=[ex("Valentina volvió preocupada porque un compañero le pidió su contraseña. Un adulto de su casa está viendo un partido. Ella le dice: «Cuando termine el partido, ¿puedes escucharme? Es importante». ¿Eligió bien el momento?", "Sí", "Avisó que es importante y esperó a que ese adulto pudiera escucharla.")],
    selfcheck=[ex("En Orientación: ¿decir lo esencial incluye qué pasó, cómo me siento y qué necesito?", "Sí", "Esas tres ideas hacen el mensaje claro."), ex("¿Contar a un adulto de confianza es cuidarse?", "Sí", "Permite recibir ayuda."), ex("¿Es buen momento para hablar cuando el adulto está muy apurado?", "No", "No podrá escuchar bien.")],
    task=T("Escribe un diálogo corto de 4 líneas entre Teo, un estudiante inventado, y un adulto de confianza. Teo quiere contar que un compañero mayor le pidió sus contraseñas de una red social. El diálogo debe tener: cómo pide el momento, lo esencial (qué pasó, cómo se siente, qué necesita) y un acuerdo final.", "Teo: «¿Tienes un momento? Necesito contarte algo importante». Adulto: «Claro, dime». Teo: «Un compañero mayor me pidió mis contraseñas. Me sentí presionado y necesito ayuda». Adulto: «Gracias por contarme; no las compartas y mañana hablamos con la orientadora».", ["pide el momento", "dice qué pasó, cómo se siente y qué necesita", "incluye un acuerdo final", "no cuenta una vivencia propia"], ["diálogo escrito o dramatizado"], ["no decir qué necesita", "no llegar a un acuerdo"], "Reconoce el diálogo y pregunta qué otro adulto de confianza podría elegir Teo."),
    reinforce="Escribe una frase para empezar a contar algo difícil y otra para pedir un momento tranquilo.",
    extend="Explica por qué a veces conviene contarle lo mismo a un segundo adulto de confianza.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. Las listas de información y los casos de personajes inventados están escritos en los ejercicios.",
    "Aprenderé a resguardar mi intimidad: qué información no se comparte y por qué no se envían fotos íntimas. Sirve para cuidar mi privacidad en la vida diaria y en internet.",
    ["Sé que mi cuerpo es mío.", "Sé que puedo decir «no»."],
    [
        "La intimidad es lo que pertenece a tu vida privada y tú decides con quién compartirla. Incluye tu cuerpo, tus pensamientos, tus mensajes y tus datos personales. La información personal que no debes dar a desconocidos incluye: tu nombre completo, tu dirección, el nombre de tu colegio, tus horarios, tus contraseñas y cualquier foto que te muestre en una situación privada. Con eso alguien podría encontrarte, engañarte o dañarte.",
        "Las fotos o videos íntimos, es decir, aquellos en que se ve el cuerpo en ropa interior o sin ropa, nunca deben enviarse ni pedirse. Nadie tiene derecho a pedírtelos, ni siquiera un amigo, una pareja o alguien que te dice que te quiere. Aunque confíes, lo que se envía puede reenviarse y quedar para siempre en internet. Si recibes una foto íntima de alguien, no la reenvíes ni la guardes: muestra el chat a un adulto de confianza. Compartir estas imágenes de otra persona la daña y puede tener consecuencias legales para quien las comparte.",
        "Si alguien te pide una foto íntima o información privada, di «no», no respondas más, guarda una captura de pantalla como prueba y cuéntaselo a un adulto de confianza. No es tu culpa y no es una vergüenza. Si ya enviaste algo, también puedes pedir ayuda: lo importante es que un adulto sepa y pueda ayudar a detener el daño.",
    ],
    [("intimidad", "lo que pertenece a mi vida privada y yo decido a quién mostrarlo"), ("dato personal", "información que permite identificar o ubicar a una persona"), ("foto íntima", "imagen que muestra el cuerpo en una situación privada"), ("captura de pantalla", "foto de lo que se ve en el celular o computador"), ("reenviar", "mandar a otras personas algo que recibí")],
    [
        W("Clasificar información", "Teo dice su nombre completo, su dirección y su colegio a un desconocido en un videojuego. ¿Fue una decisión segura?", ["Esos datos permiten ubicarlo.", "Un desconocido no debe saberlos.", "Hubo riesgo para su seguridad."], "No, fue riesgoso"),
        W("Responder a una petición", "Alguien le escribe a Luz: «Mándame una foto tuya sin ropa; será nuestro secreto». ¿Qué debe hacer Luz?", ["Nadie puede pedir una foto así.", "Debe decir no, no responder y guardar prueba.", "Luego debe contárselo a un adulto de confianza."], "Decir no, guardar una captura y contárselo a un adulto de confianza"),
    ],
    [
        M("Creer que si confío en la persona, puedo enviarle una foto íntima.", "Se piensa que la confianza evita que se reenvíe.", "Nunca envíes fotos íntimas: lo enviado puede reenviarse."),
        M("Pensar que, si ya la envié, no puedo pedir ayuda.", "Se siente culpa y vergüenza.", "Cuenta a un adulto de confianza: lo importante es detener el daño."),
    ],
    R=[
        ex("¿La dirección de tu casa es un dato personal que no debes dar a desconocidos? Responde sí o no.", "Sí", "Con la dirección pueden encontrarte."),
        ex("¿Alguien tiene derecho a pedirte una foto íntima? Responde sí o no.", "No", "Nadie tiene derecho, aunque diga que te quiere."),
        ex("Si te piden una foto íntima, ¿qué respondes: «No» o «Sí, pero que no se sepa»?", "«No»", "Es la respuesta que te protege."),
    ],
    U=[
        ex("¿Por qué una foto enviada a alguien de confianza igual puede quedar expuesta?", "Porque puede reenviarse", "Una vez enviada, ya no la controlas."),
        ex("¿Por qué guardar una captura de pantalla de la petición ayuda?", "Porque sirve de prueba para un adulto", "Le permite ver lo ocurrido."),
        ex("Si ya enviaste algo y te da vergüenza, ¿qué conviene hacer: contarle a un adulto de confianza o esconderlo?", "Contarle a un adulto de confianza", "Un adulto puede ayudar a detener el daño."),
    ],
    A=[
        ex("Lista: 1) tu color favorito; 2) tu dirección; 3) tu contraseña; 4) el nombre de tu colegio y tu horario de salida; 5) tu comida preferida. ¿Cuántos son datos que no debes dar a desconocidos?", "3", "La dirección, la contraseña y el colegio con horario permiten ubicarte o entrar a tus cuentas."),
        ex("Un desconocido en un chat pregunta «¿a qué colegio vas y a qué hora sales?». ¿Qué respondes: «No doy esa información» o «Voy a tal colegio y salgo a las 5»?", "«No doy esa información»", "Evita que alguien pueda encontrarte."),
        ex("Luz recibe una foto íntima de una compañera. ¿Qué debe hacer? A) Reenviarla al curso. B) No reenviarla y contárselo a un adulto de confianza. C) Guardarla y mirarla.", "B", "No dañar a la compañera y pedir ayuda adulta."),
    ],
    Z=[
        ex("Alguien dice: «Si me mandas la foto, te doy un regalo». ¿Por qué la oferta no cambia la respuesta?", "Porque ninguna oferta justifica enviar una foto íntima", "Es una forma de presión y de engaño."),
        ex("¿Por qué compartir la foto íntima de otra persona también es dañino aunque «solo fue una broma»?", "Porque expone a la persona y la humilla", "El daño es real aunque quien la reenvía diga que era un juego."),
    ],
    D=[
        arith("Un curso de 30 estudiantes revisó cuántos conocían las reglas de privacidad: 22 las conocían. ¿Cuántos no las conocían?", "30-22", "Se restan los que las conocían al total."),
        arith("Ema revisó 6 ajustes de privacidad de su cuenta y cambió 4. ¿Cuántos le faltan por cambiar?", "6-4", "Se restan los cambiados al total revisado."),
    ],
    context=[ex("Un perfil nuevo escribe a Camila: «Hola, soy de tu colegio. ¿Me mandas tu dirección y una foto con el uniforme?». Camila no responde, guarda una captura y se la muestra a una persona adulta de su casa. ¿Actuó de forma segura?", "Sí", "No dio datos, guardó prueba y avisó a un adulto de confianza.")],
    selfcheck=[ex("En Orientación: ¿la contraseña es información que debo cuidar?", "Sí", "Permite entrar a mis cuentas."), ex("¿Se deben enviar fotos íntimas aunque confíe en la persona?", "No", "Lo enviado puede reenviarse."), ex("¿Es mi culpa si alguien me pide una foto íntima?", "No", "La responsabilidad es de quien la pide.")],
    task=T("Lee las situaciones inventadas: (1) un desconocido pregunta tu dirección en un juego; (2) un compañero te pide tu contraseña «para jugar»; (3) alguien te pide una foto sin ropa. Para cada una, escribe qué dirías y qué harías después.", "(1) «No doy esa información»; bloqueo y aviso a un adulto. (2) «No comparto mi contraseña»; se lo cuento a un adulto. (3) «No»; no respondo más, guardo una captura y se la muestro a un adulto de confianza.", ["responde con un «no» claro", "indica una acción posterior segura", "incluye avisar a un adulto en la que lo requiere", "no cuenta una vivencia propia"], ["tabla escrita"], ["dar datos para evitar conflicto", "no avisar a un adulto"], "Reconoce las respuestas y pregunta quién sería su adulto de confianza."),
    reinforce="Escribe cinco datos personales que no darías a desconocidos y una frase para decir que no.",
    extend="Explica por qué lo que se envía por internet puede quedar mucho tiempo y llegar a muchas personas.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. Las situaciones y el semáforo de señales están escritos en los ejercicios. Todos los casos son inventados.",
    "Aprenderé a reconocer manifestaciones sexuales inapropiadas, a decir «no» y a pedir ayuda. Sirve para protegerme y proteger a otros, sin sentir culpa.",
    ["Sé que mi cuerpo es mío.", "Sé que puedo decir «no» y pedir ayuda."],
    [
        "Una manifestación sexual inapropiada es cualquier gesto, mensaje, foto, broma o contacto de tipo sexual que no corresponde, que no quieres o que viene de un adulto hacia un niño o niña. Puede ocurrir en persona o en línea, y puede venir de un desconocido o de alguien conocido. Algunas señales de alerta son que te pidan guardar un secreto sobre el contacto, que te ofrezcan regalos a cambio de algo, que te pidan fotos del cuerpo o te hablen de temas sexuales, que quieran encontrarse a solas contigo o que te hagan sentir incómodo.",
        "Si algo te hace sentir incómodo, confía en esa sensación. Tienes derecho a protegerte. Puedes seguir cuatro pasos. Primero, di «no» con voz firme o detén la conversación. Segundo, guarda pruebas, como una captura de pantalla, sin responder más. Tercero, aléjate del lugar o bloquea a la persona. Cuarto, cuéntaselo a un adulto de confianza, y si el primero no te cree, cuéntaselo a otro. Existen líneas telefónicas gratuitas de ayuda para niños y niñas, como el Fono Niños 147 de Carabineros en Chile.",
        "Nunca es culpa de la persona que recibe esa conducta. Quien actúa de forma inapropiada es el único responsable. Tampoco es «acusar»: avisar protege a ti y a otros. Si alguien amenaza con hacerte daño si cuentas, ese es un motivo más para pedir ayuda cuanto antes.",
    ],
    [("manifestación sexual inapropiada", "gesto, mensaje, imagen o contacto sexual que no corresponde ni se quiere"), ("señal de alerta", "algo que indica que puede haber riesgo"), ("bloquear", "impedir que alguien me contacte"), ("prueba", "captura o registro que muestra lo ocurrido"), ("denunciar", "contar a una autoridad o adulto responsable para que actúe")],
    [
        W("Reconocer señales de alerta", "Un adulto que conoce en línea a Ian le dice: «No le cuentes a nadie que hablamos; te daré regalos». ¿Hay señales de alerta?", ["Le pide guardar un secreto.", "Le ofrece regalos.", "Ambas son señales de alerta."], "Sí, hay dos señales: el secreto y los regalos"),
        W("Aplicar los cuatro pasos", "Una compañera inventada recibe mensajes sexuales de un desconocido. ¿Qué paso va después de «bloquear»?", ["Los pasos son: decir no, guardar pruebas, alejarse o bloquear y contar a un adulto.", "Bloquear es el tercero.", "Solo falta contárselo a un adulto."], "Contárselo a un adulto de confianza"),
    ],
    [
        M("Creer que debo aguantar para no causar problemas.", "Se teme lo que pase si se cuenta.", "Avisar a un adulto de confianza protege a ti y a otros."),
        M("Pensar que si conozco a la persona, no puede haber nada inapropiado.", "Se cree que solo los desconocidos pueden dañar.", "Cualquier persona puede portarse de forma inapropiada; confía en tu sensación de incomodidad."),
    ],
    R=[
        ex("Pedir guardar un secreto sobre el contacto con un niño, ¿es una señal de alerta? Responde sí o no.", "Sí", "Los secretos impiden pedir ayuda."),
        ex("Si una conversación te incomoda, ¿puedes detenerla y bloquear a la persona? Responde sí o no.", "Sí", "Tienes derecho a protegerte."),
        ex("¿Es culpa de la persona que recibe la conducta inapropiada? Responde sí o no.", "No", "La responsabilidad es de quien actúa mal."),
    ],
    U=[
        ex("¿Por qué conviene guardar una captura de pantalla antes de bloquear?", "Porque sirve de prueba para un adulto", "Muestra lo ocurrido."),
        ex("¿Por qué avisar a un adulto no es lo mismo que acusar sin razón?", "Porque protege y busca ayuda", "Busca detener un riesgo, no hacer daño."),
        ex("Si el primer adulto no te cree, ¿qué haces: te rindes o se lo cuentas a otro adulto de confianza?", "Se lo cuento a otro adulto de confianza", "Debes seguir pidiendo ayuda hasta que te escuchen."),
    ],
    A=[
        ex("Señales: 1) pide un secreto; 2) te saluda con un «hola» amable; 3) ofrece regalos por una foto; 4) quiere encontrarse a solas contigo; 5) te agradece una tarea. ¿Cuántas son señales de alerta?", "3", "Las señales 1, 3 y 4 son de alerta; las otras dos son comunes."),
        ex("Un desconocido en un chat te dice cosas sexuales. ¿Cuál es el mejor primer paso? A) Responder con un chiste. B) Dejar de responder y no seguir la conversación. C) Pedirle que pare por varias horas.", "B", "Detener el contacto es una acción segura."),
        ex("Ordena los pasos: guardar prueba (P), decir no (N), contar a un adulto (C), alejarse o bloquear (B). ¿Cuál es el último?", "C", "El orden es N, P, B, C: contar a un adulto cierra los pasos."),
    ],
    Z=[
        ex("Alguien te dice «si cuentas, te irá peor». ¿Qué debes hacer?", "Pedir ayuda a un adulto de confianza", "Una amenaza es otro motivo para avisar."),
        ex("¿Por qué una persona conocida también puede portarse de forma inapropiada?", "Porque el riesgo no depende de ser desconocido", "Lo que cuenta es la conducta, no cuánto se conoce a la persona."),
    ],
    D=[
        arith("Un colegio recibió 18 consultas de ayuda sobre seguridad en línea. Atendió 12 el mismo día. ¿Cuántas quedaron para el día siguiente?", "18-12", "Se restan las atendidas al total."),
        arith("Una estudiante inventada guardó 3 capturas el lunes y 4 el martes de mensajes inapropiados. ¿Cuántas capturas guardó entre ambos días?", "3+4", "Se suman las capturas de cada día."),
    ],
    context=[ex("Un adulto desconocido le escribe a Mati por un juego: «Eres muy madura, hablemos de temas privados; si cuentas, ya no te hablo». Mati deja de responder, bloquea y se lo cuenta a una persona adulta de su casa. ¿Actuó de forma segura?", "Sí", "Detuvo el contacto, bloqueó y avisó a un adulto.")],
    selfcheck=[ex("En Orientación: ¿puedo detener un contacto que me incomoda?", "Sí", "Tengo derecho a protegerme."), ex("¿Un secreto que obliga a ocultar un contacto incómodo es una señal de alerta?", "Sí", "Impide pedir ayuda."), ex("¿Es mi culpa si alguien me trata de forma inapropiada?", "No", "La responsabilidad es de quien actúa mal.")],
    task=T("Escribe un plan de cuatro pasos para este caso de Luz, una estudiante inventada: un adulto desconocido le escribe por un juego en línea, le pide guardar un secreto y que se junten a solas. Debe incluir: qué diría o haría primero, cómo se alejaría, qué pruebas guardaría y a qué adulto se lo contaría.", "1) No respondo más y escribo «no». 2) Guardo capturas de la conversación. 3) Bloqueo a la persona. 4) Se lo cuento a un adulto de confianza, como una persona adulta de mi casa o la orientadora, y si no me cree, se lo cuento a otro.", ["incluye los cuatro pasos", "nombra a un adulto de confianza", "no culpa a Luz", "no cuenta una vivencia propia"], ["plan escrito"], ["responder o aceptar el encuentro", "no avisar a un adulto"], "Reconoce el plan y pregunta qué señales de alerta identificó en el caso."),
    reinforce="Escribe tres señales de alerta y los cuatro pasos para protegerte.",
    extend="Explica por qué avisar a un adulto puede proteger también a otros niños o niñas.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Las fuentes y los casos están escritos en los ejercicios.",
    "Aprenderé a elegir fuentes de información confiables: personas significativas, libros y páginas especializadas. Sirve para resolver dudas sobre salud, cuerpo y seguridad sin confundirme.",
    ["Sé que preguntar es una forma de cuidarme.", "Sé que no todo lo que dicen los compañeros es correcto."],
    [
        "Cuando necesitas información sobre tu cuerpo, tu salud o tu seguridad, importa de dónde la sacas. Hay tres tipos de fuentes confiables. Las personas significativas son adultos que te cuidan y saben del tema, como alguien de tu casa, tu profesor o profesora, el orientador, una enfermera o un médico. Los libros especializados son los de la biblioteca o recomendados por el colegio. Y las páginas de internet especializadas son las de instituciones de salud, ministerios u organizaciones reconocidas.",
        "Para revisar una fuente de internet, hazte cinco preguntas. ¿Se sabe quién escribe: una persona o una institución? ¿Tiene fecha reciente? ¿Explica con lenguaje claro y sin prometer milagros? ¿Pide datos personales o dinero? ¿Otra fuente confiable dice lo mismo? Si falla en varias, no la uses. Un video o una publicación con muchos «me gusta» no es automáticamente confiable.",
        "Compara siempre dos fuentes. Si coinciden, es más probable que la información sea correcta. Si no coinciden, pregunta a un adulto de confianza o a un profesional. Y recuerda que ninguna fuente reemplaza la ayuda de una persona cuando algo te preocupa de verdad: si tu duda es urgente o te afecta, habla con un adulto.",
    ],
    [("fuente", "lugar o persona de donde viene la información"), ("fuente confiable", "fuente con autor identificable y datos correctos"), ("persona significativa", "adulto cercano que me cuida y puedo consultar"), ("institución", "organización reconocida, como un hospital o un ministerio"), ("contrastar", "comparar lo que dicen dos o más fuentes")],
    [
        W("Evaluar una fuente", "Una página dice: «El Ministerio de Salud explica cómo lavarse las manos», trae fecha de este año, usa lenguaje claro y no pide datos. ¿Es confiable?", ["Dice quién escribe: una institución.", "Tiene fecha reciente.", "No pide datos y es clara."], "Sí, es confiable"),
        W("Contrastar", "Un video dice «los jugos detox curan todo». ¿Qué debe hacer Luz antes de creerle?", ["Una promesa de curarlo todo es sospechosa.", "Debe buscar si una fuente confiable dice lo mismo.", "Y preguntar a un adulto o profesional de la salud."], "Contrastar con una fuente confiable y preguntar a un adulto"),
    ],
    [
        M("Creer que un video con muchos «me gusta» es siempre cierto.", "Se confunde popularidad con exactitud.", "Revisa quién lo escribe y compara con otra fuente."),
        M("Usar una sola fuente para decidir algo importante.", "Se piensa que una respuesta basta.", "Compara al menos dos fuentes confiables."),
    ],
    R=[
        ex("Un médico o una enfermera, ¿son personas significativas para consultar sobre salud? Responde sí o no.", "Sí", "Son profesionales formados para cuidar la salud."),
        ex("Una página de un hospital con autor y fecha, ¿es una fuente confiable? Responde sí o no.", "Sí", "Tiene institución y datos claros."),
        ex("Una página que pide dinero por revelar «el secreto del cuerpo», ¿es confiable? Responde sí o no.", "No", "Promete secretos y pide dinero."),
    ],
    U=[
        ex("¿Por qué conviene comparar dos fuentes?", "Porque si coinciden es más probable que sea correcto", "Contrastar reduce el riesgo de error."),
        ex("¿Los «me gusta» de una publicación prueban que es verdadera? Responde sí o no.", "No", "La popularidad no prueba exactitud."),
        ex("Si la información no coincide entre dos fuentes confiables, ¿qué haces: la inventas tú o preguntas a un adulto o profesional?", "Pregunto a un adulto o profesional", "Ellos pueden aclarar la diferencia."),
    ],
    A=[
        ex("Revisa cada fuente: 1) libro de biblioteca con autor; 2) video sin autor que promete milagros; 3) página de un centro de salud con fecha reciente; 4) mensaje que pide tu número de teléfono para «darte el secreto». ¿Cuántas son confiables?", "2", "El libro y el centro de salud tienen autor o institución y no piden datos."),
        ex("Tienes una duda sobre alimentación. ¿Cuál es mejor fuente? A) Un compañero que dice saber. B) Una nutricionista o el sitio de una institución de salud. C) Un video anónimo con muchos «me gusta».", "B", "Tiene formación y responde por la información."),
        ex("Una página dice quién la escribe, tiene fecha reciente y usa lenguaje claro, pero pide tu número de teléfono y ninguna otra fuente confiable dice lo mismo. ¿Es confiable?", "No", "Falla en dos preguntas clave: pide datos personales y no coincide con otras fuentes."),
    ],
    Z=[
        ex("¿Por qué una buena fuente de internet no debería pedirte datos personales para darte información básica de salud?", "Porque no los necesita y podrían usarse mal", "Una fuente seria informa sin pedir datos privados."),
        ex("Dos fuentes confiables dicen lo mismo y una tercera, anónima, dice lo contrario. ¿A cuál creer más?", "A las dos confiables", "Coinciden y se pueden identificar."),
    ],
    D=[
        arith("Un curso revisó 20 páginas. 13 eran confiables. ¿Cuántas no lo eran?", "20-13", "Se restan las confiables al total."),
        arith("Luz usó 2 libros y 3 páginas de instituciones para un trabajo. ¿Cuántas fuentes usó?", "2+3", "Se suman los libros y las páginas."),
    ],
    context=[ex("Para un trabajo sobre sueño, Matías usó un artículo con autor del sitio de un hospital, fechado este año, y un libro de la biblioteca. Ambos coinciden. ¿Eligió bien sus fuentes?", "Sí", "Ambas son identificables, recientes y coinciden.")],
    selfcheck=[ex("En Orientación: ¿un adulto cercano que sabe del tema puede ser una fuente confiable?", "Sí", "Es una persona significativa."), ex("¿Una fuente que promete milagros es confiable?", "No", "Promete cosas que no puede cumplir."), ex("¿Conviene comparar dos fuentes?", "Sí", "Se detectan errores.")],
    task=T("Lee estas tres fuentes inventadas sobre cómo dormir mejor: A) «Hospital Infantil: dormir entre 9 y 11 horas ayuda a los niños y niñas. Fecha: este año. Autora: Dra. Pérez»; B) «Video anónimo: duerme 3 horas y serás genio»; C) «Un compañero dice que no hay que dormir». Evalúa cada fuente con las cinco preguntas y decide cuál usarías y por qué.", "A: tiene institución y autora, fecha reciente y lenguaje claro; la usaría. B: sin autor y promete un milagro; no. C: es una opinión sin fuente; no. Elijo A porque cumple las preguntas de revisión.", ["evalúa las tres fuentes", "usa al menos tres de las cinco preguntas", "elige una y justifica", "no cuenta una vivencia propia"], ["tabla escrita"], ["elegir por popularidad", "no justificar la elección"], "Reconoce la evaluación y pregunta qué segunda fuente usaría para contrastar."),
    reinforce="Escribe las cinco preguntas para revisar una fuente de internet y aplícalas a un ejemplo.",
    extend="Explica por qué una fuente puede ser confiable en un tema y no serlo en otro.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. Los casos y las listas de ajustes están escritos en los ejercicios. Trabajas con personajes inventados.",
    "Aprenderé a usar las redes sociales de forma segura: cuidar la privacidad, los contactos y lo que publico. Sirve para protegerme y proteger a otras personas en internet.",
    ["Sé qué datos personales no debo dar.", "Sé cuándo pedir ayuda a un adulto de confianza."],
    [
        "Las redes sociales sirven para conversar y compartir, pero tienen riesgos. Muchas redes tienen una edad mínima para abrir una cuenta; esa regla existe para proteger. Si usas una, hazlo con el conocimiento de un adulto de tu familia. Lo que publicas deja una huella digital: es el rastro que queda en internet y que puede verse mucho tiempo después, incluso si lo borras.",
        "Para usarlas con seguridad, sigue estas ideas. Configura tu cuenta como privada para que solo vean tu contenido las personas que conoces. Acepta solo a personas que conoces en la vida real. No publiques tu ubicación en tiempo real, tu dirección, tu colegio ni tus horarios. Nunca te juntes en persona con alguien que conociste solo en línea. Usa contraseñas largas y distintas, y no las compartas con amigos. Antes de publicar una foto, pregúntate si te sentirías cómodo si la viera tu familia, tu profesora o un desconocido.",
        "Cuida también a los demás. No reenvíes fotos o mensajes que humillen a alguien. Si ves ciberacoso, es decir, burlas o amenazas repetidas en línea, no participes, guarda pruebas y avisa a un adulto. Y recuerda que no todo lo que ves es verdad: fotos y mensajes pueden estar falsificados. Si algo te incomoda, sal de la conversación, bloquea y cuéntalo.",
    ],
    [("huella digital", "rastro que dejo en internet con lo que publico"), ("perfil privado", "cuenta que solo ven las personas que acepto"), ("ubicación en tiempo real", "lugar exacto donde estoy en este momento"), ("ciberacoso", "burlas o amenazas repetidas en línea"), ("contraseña segura", "clave larga, distinta en cada cuenta y que no se comparte")],
    [
        W("Evaluar una publicación", "Camila quiere publicar una foto con el uniforme de su colegio y la ubicación exacta en tiempo real. ¿Es seguro?", ["Muestra su colegio y su ubicación actual.", "Cualquiera podría encontrarla.", "Es riesgoso."], "No, es riesgoso"),
        W("Ajustar la privacidad", "Ian tiene su cuenta pública y recibe solicitudes de personas que no conoce. ¿Qué debería hacer?", ["Dejar la cuenta privada.", "Aceptar solo a quienes conoce en la vida real.", "Avisar a un adulto si algún desconocido insiste."], "Poner la cuenta privada y aceptar solo a quienes conoce"),
    ],
    [
        M("Aceptar a cualquiera para tener más seguidores.", "Se valora más la cantidad que la seguridad.", "Acepta solo a personas que conoces en la vida real."),
        M("Creer que lo que borro desaparece para siempre.", "Se desconoce que otros pueden guardar o reenviar.", "Piensa antes de publicar: puede quedar como huella digital."),
    ],
    R=[
        ex("¿Una cuenta privada permite que solo vean tu contenido las personas que aceptas? Responde sí o no.", "Sí", "Ese es el efecto del perfil privado."),
        ex("¿Debes compartir tu contraseña con amigos? Responde sí o no.", "No", "Es un dato privado que protege tu cuenta."),
        ex("La huella digital, ¿es el rastro que dejas en internet o una foto de perfil?", "El rastro que dejas en internet", "Incluye lo que publicas y lo que otros guardan."),
    ],
    U=[
        ex("¿Por qué es riesgoso publicar tu ubicación en tiempo real?", "Porque alguien puede saber dónde estás", "Revela tu lugar exacto en ese momento."),
        ex("¿Por qué existe una edad mínima para abrir cuentas en muchas redes?", "Para proteger a niños y niñas", "Hay riesgos que requieren más madurez y apoyo."),
        ex("Si ves burlas repetidas hacia un compañero en un chat, ¿qué haces: participar o guardar pruebas y avisar a un adulto?", "Guardar pruebas y avisar a un adulto", "Participar sería ciberacoso."),
    ],
    A=[
        ex("Lista: 1) cuenta privada; 2) aceptar a desconocidos; 3) contraseña larga y distinta; 4) publicar el horario de salida del colegio; 5) pedir permiso a alguien antes de subir su foto. ¿Cuántas son hábitos seguros?", "3", "Los hábitos 1, 3 y 5 son seguros; los números 2 y 4 son riesgosos."),
        ex("Un perfil que no conoces te pide ser tu amigo y te escribe «soy de tu curso». ¿Qué haces? A) Aceptarlo. B) Preguntar a compañeros si lo conocen o preguntar a un adulto antes de aceptar. C) Darle tu número.", "B", "Verificar antes de aceptar reduce el riesgo de engaño."),
        ex("Una amiga te manda una foto humillante de una compañera para que la reenvíes. ¿Qué haces: reenviar o no reenviar y avisar a un adulto?", "No reenviar y avisar a un adulto", "Reenviar sería participar del daño."),
    ],
    Z=[
        ex("¿Por qué pensar «¿me sentiría cómodo si la viera mi familia?» ayuda a decidir si publicar una foto?", "Porque revisa si es adecuada y segura", "Ayuda a prever cómo se verá lo publicado."),
        ex("¿Por qué una foto puede estar falsificada aunque parezca real?", "Porque se puede editar", "No todo lo que se ve en línea es verdadero."),
    ],
    D=[
        arith("Camila tiene 50 contactos. Revisó y 38 los conoce en la vida real. ¿Cuántos no conoce?", "50-38", "Se restan los conocidos al total."),
        arith("Ian pasa 90 minutos al día en redes y su familia acordó que sean 60. ¿Cuántos minutos debe reducir?", "90-60", "Se resta el tiempo acordado al tiempo actual."),
    ],
    context=[ex("Sofi abrió una cuenta con ayuda de una persona adulta de su casa, la dejó privada, aceptó solo a familiares y compañeros que conoce, y no publica dónde está. ¿Está usando la red de forma segura?", "Sí", "Cumple privacidad, contactos conocidos y cuidado de la ubicación.")],
    selfcheck=[ex("En Orientación: ¿conviene aceptar solo a personas que conoces en la vida real?", "Sí", "Reduce el riesgo de engaño."), ex("¿Una contraseña se comparte con amigos?", "No", "Debe mantenerse privada."), ex("¿El ciberacoso se enfrenta guardando pruebas y avisando a un adulto?", "Sí", "Permite detener el daño.")],
    task=T("Escribe cinco reglas para usar redes sociales de forma segura. Incluye: privacidad de la cuenta, a quién aceptar, qué no publicar, qué hacer con las contraseñas y qué hacer ante ciberacoso.", "1) Cuenta privada. 2) Acepto solo a quienes conozco. 3) No publico ubicación, colegio ni horarios. 4) No comparto mi contraseña. 5) Si veo ciberacoso, no participo, guardo pruebas y aviso a un adulto.", ["incluye las cinco reglas pedidas", "cada regla es clara y posible", "no cuenta una vivencia propia"], ["lista escrita"], ["reglas vagas", "olvidar el ciberacoso"], "Reconoce la lista y pregunta cuál sería la regla más difícil de cumplir y cómo ayudar."),
    reinforce="Haz un dibujo o lista con cuatro ajustes de privacidad para una cuenta inventada.",
    extend="Explica por qué la huella digital puede afectar en el futuro y cómo cuidarla desde ahora.",
)
