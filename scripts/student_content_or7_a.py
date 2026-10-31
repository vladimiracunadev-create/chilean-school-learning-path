"""Cuaderno del estudiante, 7.º básico Orientación: OA 01 (autoconcepto positivo) y OA 02 (sexualidad integral, cuidado y respeto)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR07 OA 01", "OR07 OA 02"


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


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Una hoja y un lápiz. El caso de Valentina, una estudiante inventada, y todos sus datos están escritos en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé qué es el autoconcepto y sus partes: características, motivaciones, intereses y capacidades. Sirve para describirme con justicia mientras mi cuerpo y mis ideas cambian en la adolescencia.",
    ["Sé separar un hecho de una opinión o etiqueta.", "Sé que valorarme es reconocer lo que hago bien y lo que quiero mejorar."],
    [
        "El autoconcepto es la imagen que tienes de ti mismo o misma. Se construye con cuatro partes. Las características son rasgos de cómo eres, por ejemplo «soy curiosa» o «me cuesta esperar». Las motivaciones son lo que te mueve a actuar, como querer ayudar o querer aprender. Los intereses son lo que te gusta y te llama la atención, como el fútbol o el dibujo. Las capacidades son cosas que puedes hacer, o aprender a hacer, con práctica.",
        "Un autoconcepto positivo no significa creerse perfecto. Significa describirse con justicia: ver lo que haces bien, lo que te cuesta y lo que puedes cambiar, apoyándote en hechos. «Preparé la exposición y la entregué a tiempo» es un hecho. «Soy un desastre» es una etiqueta que no mira los hechos.",
        "Entre los 10 y los 14 años empieza la pubertad: el cuerpo crece, cambia la voz o la piel, y también cambian los intereses y las emociones. Estos cambios son normales, ocurren en distinto momento en cada persona y no son una competencia. Tu autoconcepto se actualiza con ellos. Lo que eras a los 9 años no es toda tu historia: puedes sumar nuevos intereses y capacidades.",
    ],
    [("autoconcepto", "imagen que una persona tiene de sí misma"), ("característica", "rasgo de cómo es una persona"), ("motivación", "razón que mueve a una persona a actuar"), ("interés", "cosa que a una persona le gusta o le llama la atención"), ("capacidad", "cosa que una persona puede hacer o aprender a hacer"), ("pubertad", "etapa en que el cuerpo cambia al pasar de niño o niña a adolescente")],
    [
        W("Clasificar una frase", "Valentina escribe: «Me gusta armar y reparar bicicletas». ¿Es una característica, un interés o una capacidad?", ["Pregunta: ¿habla de lo que le gusta o llama la atención? Sí.", "No dice cómo es ni qué logra hacer, sino qué disfruta.", "Entonces es un interés."], "Un interés"),
        W("Describir con justicia", "Valentina creció 6 cm este año y su voz cambió. Dice: «Ya no soy yo». ¿Qué es más justo decir: «Mi cuerpo está cambiando y sigo siendo yo» o «Ya no soy la misma de antes»?", ["La pubertad cambia el cuerpo, pero no borra tus intereses ni tus valores.", "La segunda frase exagera: dice que todo cambió.", "La primera reconoce el cambio y mantiene la identidad."], "«Mi cuerpo está cambiando y sigo siendo yo»"),
    ],
    [
        M("Creer que tener un autoconcepto positivo es no reconocer nada malo de uno.", "Se confunde sentirse bien con ser perfecto.", "Reconoce lo que haces bien y lo que quieres mejorar, usando hechos."),
        M("Pensar que si mi cuerpo cambia más tarde que el de mis compañeros, algo anda mal.", "Se compara el ritmo propio con el de otros.", "La pubertad empieza en edades distintas y todas son normales."),
    ],
    R=[
        ex("«Soy curiosa y pregunto cuando no entiendo». ¿Es una característica o un interés?", "Una característica", "Describe cómo es la persona, no algo que le guste hacer."),
        ex("«Quiero ayudar a mi curso a ordenar la sala». ¿Es una motivación o una capacidad?", "Una motivación", "Dice lo que la mueve a actuar."),
        ex("«Puedo armar un mapa con bastantes detalles». ¿Es una capacidad o un interés?", "Una capacidad", "Habla de algo que puede hacer."),
    ],
    U=[
        ex("Si dos compañeros tienen 12 años y uno ya cambió la voz y el otro no, ¿es normal?", "Sí", "La pubertad empieza en edades distintas y todas son normales."),
        ex("¿Qué parte del autoconcepto aparece en «Me encanta la astronomía»: motivaciones, intereses o capacidades?", "Intereses", "Dice lo que le gusta y le llama la atención."),
        ex("¿Es un hecho o una etiqueta: «Entregué las 5 tareas de la semana»?", "Un hecho", "Se puede comprobar contando las tareas entregadas."),
    ],
    A=[
        ex("Ordena según el tipo de parte: 1) «soy paciente»; 2) «me gusta cantar»; 3) «sé armar un circuito simple»; 4) «quiero aprender inglés». ¿Cuál es la motivación?", "4", "«Quiero aprender» dice lo que la mueve; las otras son rasgo, interés y capacidad."),
        ex("Valentina escribe: «Soy buena para el deporte porque ayer jugué 40 minutos sin cansarme». ¿Qué parte del autoconcepto es? A) Característica. B) Capacidad apoyada en un hecho.", "B", "Dice lo que puede hacer y lo apoya con un hecho."),
        ex("Una persona escribe «soy un desastre» sin dar ningún ejemplo. ¿Qué le falta a esa frase para ser justa?", "Un hecho que la apoye", "Una etiqueta sin hechos no describe con justicia."),
    ],
    Z=[
        ex("Rodrigo dice: «Si mi voz cambió más tarde que la de mis amigos, soy raro». ¿Qué error comete?", "Compara su ritmo con el de otros y concluye algo falso", "Cada cuerpo cambia a su ritmo y todos los ritmos son normales."),
        ex("¿Por qué conviene incluir los intereses nuevos en el autoconcepto, aunque eran distintos a los de hace dos años?", "Porque el autoconcepto se actualiza con los cambios", "En la adolescencia aparecen nuevos intereses y capacidades que forman parte de ti."),
    ],
    D=[
        arith("Valentina anotó 14 frases sobre sí misma: 5 características, 4 intereses y 3 capacidades. El resto son motivaciones. ¿Cuántas son motivaciones?", "14-5-4-3", "Al total se le restan las frases de los otros tres grupos."),
        arith("En un cuadro de 4 partes, Valentina escribió 3 frases por parte. ¿Cuántas frases escribió en total?", "4*3", "Se multiplican las partes por las frases de cada una."),
    ],
    context=[ex("En el Consejo de Curso, la profesora pide: «Completa: Soy… porque…». Lucas escribe: «Soy simpático porque todos me quieren». ¿Se apoya en un hecho que él haya hecho?", "No", "«Todos me quieren» no cuenta lo que él hizo ni se puede comprobar.")],
    selfcheck=[ex("En Orientación: ¿el autoconcepto incluye características, motivaciones, intereses y capacidades?", "Sí", "Son sus cuatro partes."), ex("¿Los cambios de la pubertad ocurren al mismo tiempo en todas las personas?", "No", "Cada persona cambia a su ritmo."), ex("¿Un autoconcepto positivo exige creerse perfecto?", "No", "Exige describirse con justicia, con hechos.")],
    task=T("Lee el perfil de Bruno, un estudiante inventado: toca la guitarra desde hace un año; ayudó a un compañero a entender una resta de fracciones; se pone nervioso al hablar en público; este año creció mucho y dice que se siente raro. Arma un cuadro con cuatro frases sobre Bruno: una característica, una motivación, un interés y una capacidad, cada una con su hecho.", "Característica: se pone nervioso al hablar en público, aunque ayuda a otros. Motivación: quiere que sus compañeros entiendan. Interés: la guitarra. Capacidad: explicar fracciones, porque ayudó a un compañero.", ["escribe las cuatro partes del autoconcepto", "cada parte tiene un hecho del perfil", "no usa etiquetas como «raro»", "no cuenta algo íntimo propio"], ["cuadro escrito", "texto oral"], ["usar una etiqueta sin hecho", "confundir interés con capacidad"], "Reconoce las partes bien clasificadas y pregunta qué hecho apoya la frase menos clara."),
    reinforce="Escribe cuatro frases sobre un personaje de cuento: una característica, una motivación, un interés y una capacidad.",
    extend="Explica por qué el autoconcepto de una persona puede cambiar entre los 10 y los 14 años.",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. El caso de Matías, un estudiante inventado, está escrito en los ejercicios.",
    "Aprenderé a separar hechos, emociones y comentarios sobre el cuerpo, y a reconocer mi derecho a ser respetado y a poner límites. Sirve para que burlas o comparaciones no definan cómo me veo.",
    ["Sé que el autoconcepto tiene características, motivaciones, intereses y capacidades.", "Sé que los cambios de la pubertad ocurren a distinto ritmo."],
    [
        "Durante la pubertad aparecen comentarios sobre el cuerpo: «qué alto», «qué flaco», «tu voz suena rara». Para pensar con claridad conviene separar cuatro cosas. El hecho es lo que se puede observar: «Matías mide 8 cm más que hace un año». La emoción es lo que él siente: vergüenza, enojo o tristeza. La opinión es lo que otros dicen y no es un hecho: «te ves ridículo». El derecho es lo que le corresponde: que lo traten con respeto y sin burlas.",
        "Las burlas sobre el cuerpo, la voz o la apariencia no son bromas inofensivas cuando la persona se siente mal. Afectan el autoconcepto y pueden repetirse. Todas las personas tienen derecho a un trato digno, es decir, respetuoso, y a que su cuerpo no sea tema de humillación. También puedes poner un límite: decir con calma «no me gusta que hables de mi cuerpo; para, por favor».",
        "Compararte con otros tampoco es justo. Lo que ves en redes sociales suele ser una imagen elegida y retocada: no muestra cómo es la vida real. Tu cuerpo cambia a su propio ritmo. Si un comentario te hace sentir mal varios días, es una buena razón para hablar con una persona adulta de confianza.",
    ],
    [("hecho", "lo que pasó y se puede observar"), ("emoción", "lo que siente una persona"), ("opinión", "lo que alguien piensa o dice, sin que sea un hecho"), ("trato digno", "trato respetuoso que reconoce el valor de toda persona"), ("límite", "lo que acepto y lo que no que me hagan o me digan")],
    [
        W("Separar hecho y opinión", "En el patio le dicen a Matías: «Tu voz suena rara». Su voz cambió hace un mes. ¿Cuál es el hecho y cuál la opinión?", ["Que su voz cambió hace un mes se puede observar: es un hecho.", "«Rara» es un juicio de quien habla.", "Entonces el hecho es el cambio; la opinión es «rara»."], "Hecho: su voz cambió hace un mes. Opinión: «rara»"),
        W("Poner un límite", "Un compañero se burla del cuerpo de Matías todos los recreos. ¿Qué puede decir para poner un límite respetuoso?", ["Debe nombrar lo que le molesta y pedir que pare.", "Debe hacerlo con calma, sin insultar.", "Puede agregar que, si sigue, avisará a un adulto."], "«No me gusta que hables de mi cuerpo; para, por favor»"),
    ],
    [
        M("Pensar que si es una broma, no debo sentirme mal.", "Se cree que la intención de reírse cambia el efecto sobre la otra persona.", "Si algo me duele, puedo decirlo; una broma que humilla no es respeto."),
        M("Creer que lo que opinan los demás de mi cuerpo es la verdad sobre mí.", "Se confunde la opinión de otros con un hecho.", "Una opinión no es un hecho: yo decido cómo describirme."),
    ],
    R=[
        ex("«Matías mide 8 cm más que hace un año». ¿Es un hecho o una opinión?", "Un hecho", "Se puede medir y comprobar."),
        ex("«Te ves ridículo». ¿Es un hecho o una opinión?", "Una opinión", "Es un juicio de quien habla; no se puede medir."),
        ex("¿Todas las personas tienen derecho a un trato digno, sí o no?", "Sí", "El trato respetuoso es un derecho de toda persona."),
    ],
    U=[
        ex("¿Por qué una burla sobre el cuerpo no es «solo una broma» si la persona se siente mal?", "Porque daña y puede repetirse", "El efecto sobre quien la recibe importa más que la intención de reírse."),
        ex("¿Qué frase es una forma respetuosa de poner un límite: «No me gusta que opines de mi cuerpo; para, por favor» o «Cállate, feo»?", "«No me gusta que opines de mi cuerpo; para, por favor»", "Nombra lo que molesta y pide parar, sin insultar."),
        ex("Una foto de redes sociales muestra a una persona con el cuerpo muy retocado. ¿Muestra cómo es de verdad?", "No", "Las imágenes pueden estar elegidas y retocadas."),
    ],
    A=[
        ex("Frases: 1) «Tomás creció 5 cm este año»; 2) «Qué ridículo se ve»; 3) «Tomás se siente avergonzado»; 4) «Tomás mide 1,60 m». ¿Cuántas son hechos?", "2", "Las frases 1 y 4 se pueden comprobar; la 2 es opinión y la 3 es una emoción."),
        ex("A Tomás le gritan un apodo por su cuerpo y se siente triste. ¿Qué derecho no se está respetando?", "El derecho a un trato digno", "Las burlas humillan y no respetan su dignidad."),
        ex("Tomás lleva 4 días con ganas de no ir al colegio por los comentarios. ¿Qué acción segura corresponde? A) Contárselo a una persona adulta de confianza. B) Guardar silencio hasta que pase.", "A", "Un malestar de varios días necesita apoyo; callar no lo resuelve."),
    ],
    Z=[
        ex("Ana dice: «Si me comparo con las fotos de esa influencer, me veo mal». ¿Qué error hay en esa comparación?", "Compara su vida real con una imagen elegida o retocada", "Las imágenes de redes no muestran la realidad completa."),
        ex("¿Por qué conviene separar la emoción del hecho cuando alguien se burla?", "Para no creer que lo que siento prueba lo que dicen", "Sentir vergüenza no demuestra que la burla sea verdad."),
    ],
    D=[
        arith("Tomás medía 148 cm hace un año y ahora mide 156 cm. ¿Cuántos centímetros creció?", "156-148", "Se resta la estatura anterior a la actual."),
        arith("En 5 días de la semana, un compañero le dijo apodos a Tomás 3 veces por día. ¿Cuántas veces ocurrió en la semana?", "5*3", "Se multiplican los días por las veces diarias."),
    ],
    context=[ex("En un grupo de mensajes del curso aparece una foto de un compañero con el texto «mírenle el pelo». Varios ponen risas. El compañero escribe: «no me gusta». ¿Qué corresponde hacer a quienes pusieron risas?", "Dejar de reírse, borrar su reacción y respetar el límite", "Él dijo que le molesta; seguir riendo no respeta su derecho a un trato digno.")],
    selfcheck=[ex("En Orientación: ¿una opinión sobre mi cuerpo es un hecho?", "No", "Es un juicio de otra persona."), ex("¿Puedo poner un límite si me molestan los comentarios sobre mi cuerpo?", "Sí", "Es un derecho y puede hacerse con respeto."), ex("¿Sentir vergüenza prueba que lo que dicen es verdad?", "No", "Una emoción no demuestra un hecho.")],
    task=T("Lee el caso de Daniela, una estudiante inventada: este año le salieron granos en la cara y un compañero le dice «cara de pizza» frente al curso. Ella se siente humillada. Escribe el hecho, la emoción, la opinión de quien se burla, el derecho que no se respeta y una frase para poner un límite con respeto.", "Hecho: tiene granos en la cara. Emoción: humillación. Opinión: «cara de pizza». Derecho: a un trato digno. Límite: «No me gusta que hables de mi cara; para, por favor».", ["separa hecho, emoción y opinión", "nombra el derecho", "escribe un límite respetuoso", "no cuenta nada íntimo propio"], ["texto escrito o dicho"], ["escribir la opinión como si fuera el hecho", "poner un límite con insultos"], "Reconoce cada parte y pregunta a quién podría contarle Daniela si las burlas siguen."),
    reinforce="Escribe un hecho, una emoción y una opinión para una situación de burla de un personaje de cuento.",
    extend="Explica por qué mirar muchas fotos retocadas puede afectar el autoconcepto de una persona.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. El caso de Renata y las tarjetas de opciones están escritos en los ejercicios.",
    "Aprenderé a comparar opciones ante un comentario o una comparación y a construir una descripción positiva de mí con aportes de otros. Sirve para elegir respuestas que cuidan mi autoconcepto y el de mi curso.",
    ["Sé separar hechos, emociones y opiniones.", "Sé poner un límite respetuoso."],
    [
        "Cuando alguien te compara o te dice algo que te duele, tienes varias opciones, y cada una tiene consecuencias. Esconderte evita el momento incómodo, pero el comentario puede repetirse. Responder con otra burla puede parar a la persona un rato, pero genera más conflicto. Reírse para encajar te aleja de lo que sientes. Decir con calma que no te gusta y pedir ayuda a un adulto puede detenerlo y cuidar a todos.",
        "Un autoconcepto positivo también se construye en grupo. Los compañeros pueden aportar evidencia: «Renata siempre explica con paciencia», «Renata organizó el equipo». Eso se llama retroalimentación: dar a otra persona un dato sobre lo que hizo. La buena retroalimentación es específica, verdadera y respetuosa. «Eres lo mejor» no ayuda, porque no dice qué hizo. «Ordenaste los turnos y todos hablamos» sí ayuda.",
        "Puedes armar un mural del curso con aportes de cada estudiante: un hecho positivo y verdadero de cada persona, escrito con su acuerdo. Así se construyen representaciones positivas de manera individual y colectiva. Nadie debe aparecer si no quiere, y no se escribe nada que humille o que sea íntimo.",
    ],
    [("opción", "una de las cosas que puedo elegir hacer"), ("consecuencia", "lo que ocurre después de una decisión"), ("retroalimentación", "dato que se da a otra persona sobre lo que hizo"), ("específico", "que dice con claridad qué se hizo, no solo una impresión"), ("mural", "cartel del curso con aportes de cada integrante")],
    [
        W("Anticipar consecuencias", "Un compañero compara a Renata con su hermana: «Ella es mucho mejor que tú». Renata puede (a) responder con otra comparación, (b) decir que le molesta y pedir que pare. ¿Qué consecuencia es más probable en (a)?", ["Una comparación responde con otra.", "Eso suele subir el enojo.", "Entonces el conflicto aumenta."], "El conflicto aumenta"),
        W("Retroalimentación específica", "¿Cuál es mejor retroalimentación para Renata: «Eres genial» o «Cuando te tocó explicar, usaste un ejemplo y todos entendimos»?", ["«Eres genial» no dice qué hizo.", "La segunda frase cuenta una acción concreta y sus resultados.", "Por eso es específica."], "«Cuando te tocó explicar, usaste un ejemplo y todos entendimos»"),
    ],
    [
        M("Pensar que reírme con los demás de una burla me evita problemas.", "Se busca encajar aunque duela o dañe a otra persona.", "Puedes no participar y apoyar a quien recibe la burla."),
        M("Creer que un halago general como «eres lo mejor» ayuda a construir autoconcepto.", "No dice qué hizo la persona, así que no sirve de evidencia.", "Menciona una acción concreta y verdadera."),
    ],
    R=[
        ex("¿Qué opción ayuda más ante una burla: decir con calma «no me gusta, para» o esconderse?", "Decir con calma «no me gusta, para»", "Nombra el problema y puede detenerlo sin agredir."),
        ex("¿Una consecuencia es lo que ocurre antes o después de una decisión?", "Después", "Es el resultado de lo que se decide."),
        ex("¿Es específica la frase «Hiciste el cartel con colores claros y letras grandes»?", "Sí", "Dice qué hizo la persona."),
    ],
    U=[
        ex("¿Por qué responder a una burla con otra burla suele aumentar el conflicto?", "Porque cada uno devuelve el golpe", "La respuesta agresiva invita a otra respuesta agresiva."),
        ex("¿Qué es mejor retroalimentación: «Eres buena en todo» o «Tus ejemplos en la exposición fueron claros»?", "«Tus ejemplos en la exposición fueron claros»", "Menciona una acción concreta y comprobable."),
        ex("Para un mural del curso con aportes positivos, ¿hace falta el acuerdo de la persona que aparece, sí o no?", "Sí", "Nadie debe aparecer si no quiere."),
    ],
    A=[
        ex("Opciones ante una comparación: 1) esconderse; 2) responder con otra comparación; 3) decir que le molesta y pedir ayuda a un adulto si sigue. ¿Cuál cuida mejor el autoconcepto y no aumenta el conflicto?", "3", "Pone un límite sin agredir y suma apoyo."),
        ex("En un mural se escribirán aportes de 6 compañeros. Hay una frase que dice «Sofía es la más fea del curso». ¿Debe ir al mural?", "No", "Humilla; el mural es para aportes verdaderos y respetuosos."),
        ex("Renata debe elegir entre reírse de un chiste sobre el pelo de un compañero o no reírse y acercarse a él. ¿Qué elección protege su autoconcepto y el del compañero? A) No reírse y acercarse a él. B) Reírse para encajar.", "A", "No participa de la burla y apoya a quien la recibe."),
    ],
    Z=[
        ex("Camilo dice: «Si me quedo callado, el comentario se acaba solo». ¿Qué podría pasar?", "Podría repetirse", "Callar no siempre detiene el comentario; puede seguir si nadie lo frena."),
        ex("¿Por qué una retroalimentación debe ser verdadera además de amable?", "Porque solo una evidencia real sirve para construir autoconcepto", "Un elogio falso no se puede comprobar y no ayuda a conocerse."),
    ],
    D=[
        arith("Un curso de 32 estudiantes arma un mural con un aporte por persona. Ya hay 21 aportes. ¿Cuántos faltan?", "32-21", "Al total de estudiantes se le restan los aportes ya escritos."),
        arith("Renata recibió 3 aportes de cada uno de 4 compañeros. ¿Cuántos aportes recibió en total?", "3*4", "Se multiplican los aportes por los compañeros."),
    ],
    context=[ex("En el grupo del curso alguien publica: «Hagamos un mural con una cualidad real de cada persona». Mateo propone escribir «es chistoso» sin permiso de nadie. ¿Qué falta para respetar a todos?", "Preguntar a cada persona si quiere aparecer", "El mural debe hacerse con el acuerdo de quien aparece.")],
    selfcheck=[ex("En Orientación: ¿cada opción ante una burla tiene consecuencias?", "Sí", "Lo que decides produce resultados distintos."), ex("¿Una retroalimentación específica nombra una acción concreta?", "Sí", "Por eso sirve como evidencia."), ex("¿Un mural del curso debe incluir a quien no quiere aparecer?", "No", "Se respeta su decisión.")],
    task=T("Lee el caso de Ignacio, un estudiante inventado: sus compañeros se ríen cuando habla porque se le traba la voz al exponer. Compara dos opciones de Ignacio: reírse con ellos o decir con calma «prefiero que no se rían, estoy practicando». Escribe la consecuencia más probable de cada una. Luego redacta una retroalimentación específica y verdadera que le darías, inventando un hecho, por ejemplo qué parte de su exposición estuvo bien.", "Reírse: puede parar hoy, pero legitima la burla. Pedir respeto: puede incomodar, pero cuida su dignidad. Retroalimentación: «Tu ejemplo sobre el reciclaje fue claro y usaste una imagen; sigue así».", ["escribe una consecuencia por cada opción", "elige la opción que cuida su dignidad", "la retroalimentación nombra una acción concreta", "no humilla a nadie"], ["texto escrito o dicho"], ["dar un elogio general", "no anticipar consecuencias"], "Reconoce la consecuencia bien explicada y pregunta qué otro dato concreto podría sumar."),
    reinforce="Escribe dos opciones y su consecuencia para un personaje al que le dicen un apodo molesto.",
    extend="Redacta tres reglas para que el mural de tu curso sea respetuoso con todos.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. El caso de Paula y la lista de recursos de ayuda están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura para cuidar mi autoconcepto y a reconocer cuándo pedir ayuda a una persona adulta. Sirve cuando los cambios de la adolescencia o los comentarios me hacen sentir mal por muchos días.",
    ["Sé comparar opciones y sus consecuencias.", "Sé dar y pedir retroalimentación específica."],
    [
        "Una acción segura para tu autoconcepto es una que te ayuda a avanzar sin dañarte ni dañar a otros. Algunas son: anotar cada semana tres cosas que hiciste bien, pedir una retroalimentación concreta a alguien de confianza, practicar una capacidad nueva y limitar el tiempo que pasas viendo comparaciones en redes sociales. Todas ayudan a construir una imagen apoyada en hechos.",
        "También existen señales de que necesitas más apoyo: sentirte muy triste o sin ganas durante varias semanas, dejar de hacer lo que te gustaba, no querer ir al colegio o pensar con frecuencia que no vales. En esos casos no tienes que resolverlo solo o sola. Cuéntalo a una persona adulta de confianza: alguien de tu casa, tu profesor o profesora jefe, el orientador o la orientadora o el equipo de convivencia escolar. Si no te escuchan, insiste con otra persona.",
        "Pedir ayuda no es una debilidad. Es una forma de cuidarte, igual que cuando pides ayuda por un dolor físico. Si alguna vez piensas en hacerte daño, avísale a un adulto de inmediato. En Chile también puedes llamar gratis al Fono Niños 147 de Carabineros.",
    ],
    [("acción segura", "decisión que me ayuda sin dañarme ni dañar a otros"), ("señal de alerta", "cambio que indica que necesito apoyo"), ("persona adulta de confianza", "adulto con quien me siento seguro de hablar"), ("registro", "hoja donde anoto lo que hago y logro"), ("insistir", "volver a pedir ayuda si la primera persona no me escuchó")],
    [
        W("Usar un registro", "Paula anota cada semana tres logros. La semana 1 anotó «terminé el afiche», «ayudé a Eva» y «corregí mi tarea». ¿Para qué sirve ese registro si un día piensa «no sirvo para nada»?", ["El registro guarda hechos.", "Los hechos se pueden mirar cuando la voz crítica exagera.", "Muestra que sí hizo cosas."], "Para contrastar la voz crítica con hechos"),
        W("Decidir cuándo pedir ayuda", "Paula lleva tres semanas muy triste, no quiere ir a clases y dejó de dibujar, que le encantaba. ¿Qué acción segura elige?", ["Son señales de que necesita apoyo.", "Aguantar sola no resuelve la tristeza.", "Debe contárselo a una persona adulta de confianza."], "Contárselo a una persona adulta de confianza"),
    ],
    [
        M("Pensar que pedir ayuda me hace ver débil.", "Se cree que los problemas emocionales se deben resolver solo.", "Pedir ayuda a tiempo es una decisión valiente y cuida tu bienestar."),
        M("Contarlo una vez y rendirme si no me escuchan.", "Se cree que no hay más adultos a quienes acudir.", "Insiste con otra persona de confianza hasta que te escuchen."),
    ],
    R=[
        ex("¿Anotar tres logros por semana es una acción segura para tu autoconcepto, sí o no?", "Sí", "Reúne hechos que contrastan con la voz crítica."),
        ex("¿Sentirte muy triste durante semanas es una señal de que puede ser útil pedir ayuda, sí o no?", "Sí", "Una emoción intensa y prolongada necesita apoyo."),
        ex("¿Una persona adulta de confianza puede ser alguien de tu casa, un profesor o el orientador?", "Sí", "Son personas a quienes se puede acudir."),
    ],
    U=[
        ex("¿Por qué limitar el tiempo viendo comparaciones en redes sociales puede cuidar el autoconcepto?", "Porque disminuye comparaciones injustas", "Muchas imágenes en redes están elegidas o retocadas."),
        ex("Si el primer adulto al que le cuentas no te escucha, ¿qué haces: te quedas callado o insistes con otra persona?", "Insistes con otra persona", "Hay más adultos de confianza que pueden ayudar."),
        ex("¿Qué número gratuito de Carabineros puedes llamar en Chile si necesitas ayuda siendo niño o niña?", "147", "Es el Fono Niños de Carabineros, mencionado en la explicación."),
    ],
    A=[
        ex("Señales: 1) hace semanas dejó de hacer lo que le gustaba; 2) estuvo triste un día por una nota; 3) no quiere ir al colegio hace tres semanas; 4) pelea con su hermano por una polera. ¿Cuántas muestran una señal de que necesita apoyo?", "2", "La 1 y la 3 son cambios que se mantienen en el tiempo; la 2 y la 4 son situaciones pasajeras."),
        ex("Paula escribe en su registro: «Hoy no hice nada bien». ¿Qué corrección la hace más justa? A) «Hoy terminé la tarea de Lenguaje y se me quedó el cuaderno». B) «Nunca hago nada bien».", "A", "Cuenta hechos concretos, buenos y malos, en vez de generalizar."),
        ex("Paula se lo cuenta a su profesor jefe y él dice que no tiene tiempo. ¿Qué debe hacer ella?", "Contárselo a otra persona adulta de confianza", "Si no la escuchan, debe insistir con otro adulto."),
    ],
    Z=[
        ex("Gabriel dice: «Si le cuento a alguien, van a pensar que soy débil». ¿Qué argumento le darías?", "Pedir ayuda es cuidarse, no ser débil", "Es una decisión responsable, como pedir ayuda por un dolor físico."),
        ex("¿Por qué un registro de logros es más útil que recordar solo lo que salió mal?", "Porque muestra la realidad completa", "Recordar solo los errores deforma el autoconcepto."),
    ],
    D=[
        arith("Paula anotó 3 logros por semana durante 6 semanas. ¿Cuántos logros anotó en total?", "3*6", "Se multiplican los logros por las semanas."),
        arith("De sus 18 logros anotados, 11 fueron de estudio y el resto de ayuda a otros. ¿Cuántos fueron de ayuda a otros?", "18-11", "Al total se le restan los de estudio."),
    ],
    context=[ex("Una compañera de tu curso lleva semanas sin hablar con nadie y te cuenta que piensa «no valgo». Te pide que no se lo cuentes a nadie. ¿Qué es lo más seguro que puedes hacer?", "Avisar a un adulto de confianza", "Está en riesgo de sentirse peor; guardar el secreto no la protege.")],
    selfcheck=[ex("En Orientación: ¿conviene pedir ayuda cuando me siento muy mal por mucho tiempo?", "Sí", "Un malestar prolongado necesita apoyo."), ex("¿Pedir ayuda muestra que soy débil?", "No", "Es una forma de cuidarse."), ex("¿Puedo insistir con otro adulto si el primero no me escucha?", "Sí", "Debo seguir hasta recibir ayuda.")],
    task=T("Lee el caso de Matilde, una estudiante inventada: hace tres semanas que no quiere ir a clases, dejó de jugar básquetbol y piensa «no valgo» casi todos los días. Escribe tres señales que indican que necesita apoyo, a qué dos personas adultas de confianza podría contarle y qué podría decir como primera frase.", "Señales: no quiere ir a clases, dejó de jugar, piensa «no valgo». Personas: alguien de su casa y la orientadora. Primera frase: «Hace unas semanas me siento muy mal y necesito ayuda».", ["identifica tres señales", "nombra dos personas adultas de confianza", "escribe una primera frase respetuosa", "no cuenta nada íntimo propio"], ["texto escrito o dicho"], ["decir que debe aguantar sola", "no nombrar a una persona adulta"], "Reconoce las señales y pregunta qué haría Matilde si la primera persona no la escucha."),
    reinforce="Escribe tres señales de que un personaje de cuento necesita ayuda y dos personas a quienes podría acudir.",
    extend="Explica por qué guardar el secreto de un amigo que se siente muy mal no es una forma de cuidarlo.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. El caso de Camila y las frases de cada dimensión están escritos en los ejercicios. No necesitas contar nada personal.",
    "Aprenderé que la sexualidad tiene varias dimensiones y que cuidar el cuerpo y la intimidad es parte de ella. Sirve para entender los cambios de la adolescencia con respeto y sin vergüenza.",
    ["Sé que la pubertad es una etapa de cambios normales.", "Sé que tengo derecho a un trato digno."],
    [
        "La sexualidad es una parte de la vida de toda persona y no se reduce a las relaciones sexuales. Tiene varias dimensiones que se influyen entre sí. La dimensión biológica es el cuerpo: cómo crece, qué cambios trae la pubertad y cómo se cuida. La dimensión afectiva son las emociones y los sentimientos: el cariño, el enamoramiento, la vergüenza. La dimensión social son las relaciones con otros: la amistad, la familia y el pololeo, y lo que la sociedad espera. La dimensión ética son los valores: el respeto, la responsabilidad y el cuidado de uno mismo y de los demás.",
        "Integrar las dimensiones es tenerlas en cuenta juntas. Por ejemplo, si te gusta alguien (afectiva), piensas en cómo tratarla con respeto (ética), en cómo es la relación con tu grupo (social) y en cómo te sientes con los cambios de tu cuerpo (biológica). Decidir con una sola dimensión, como solo lo que sientes en el momento, puede llevarte a lo que después lamentas.",
        "Cuidar el cuerpo y la intimidad es parte de la sexualidad. La intimidad es lo que corresponde a tu mundo privado: tus partes íntimas, tus sentimientos y tus mensajes personales. Tienes derecho a decidir quién se entera de qué y quién te toca. Hablar de estos temas con respeto, con una persona adulta de confianza o un profesional de salud, es una forma de cuidarte.",
    ],
    [("sexualidad", "parte de la vida de toda persona que incluye cuerpo, afectos, relaciones y valores"), ("dimensión", "una de las partes que forman un tema"), ("intimidad", "mundo privado de una persona: cuerpo, sentimientos y mensajes personales"), ("afectivo", "relacionado con emociones y sentimientos"), ("ético", "relacionado con valores como el respeto y la responsabilidad")],
    [
        W("Clasificar por dimensión", "Camila, una estudiante inventada, piensa: «Me siento nerviosa porque me gusta un compañero». ¿Qué dimensión nombra?", ["Habla de lo que siente: nerviosismo y gusto por alguien.", "Esas son emociones y sentimientos.", "Entonces es la dimensión afectiva."], "La dimensión afectiva"),
        W("Integrar dimensiones", "Camila quiere invitar a un compañero a conversar. Piensa en tratarlo con respeto y en no presionarlo. ¿Qué dimensión usa al pensar así?", ["Respeto y no presionar son valores.", "Los valores forman la dimensión ética.", "Además usa la social porque piensa en su relación con otra persona."], "La ética, junto con la social"),
    ],
    [
        M("Creer que sexualidad solo significa relaciones sexuales.", "Se reduce un tema amplio a una sola parte.", "La sexualidad incluye cuerpo, afectos, relaciones y valores."),
        M("Pensar que hablar de intimidad y de cambios del cuerpo es de mal gusto.", "Se confunde cuidar la información con tener vergüenza.", "Se puede hablar con respeto con un adulto de confianza o un profesional de salud."),
    ],
    R=[
        ex("«Mi voz cambió y estoy creciendo». ¿Qué dimensión nombra: biológica o ética?", "Biológica", "Habla del cuerpo y sus cambios."),
        ex("«Quiero tratar con respeto a mi amigo». ¿Qué dimensión nombra: ética o biológica?", "Ética", "El respeto es un valor."),
        ex("¿La sexualidad incluye solo las relaciones sexuales, sí o no?", "No", "Incluye cuerpo, afectos, relaciones sociales y valores."),
    ],
    U=[
        ex("¿Por qué la dimensión afectiva incluye la vergüenza además del cariño?", "Porque ambas son emociones y sentimientos", "La dimensión afectiva abarca todo lo que se siente."),
        ex("«En mi grupo de amigos se comenta quién pololea con quién». ¿Qué dimensión nombra: social o biológica?", "Social", "Habla de relaciones y de lo que ocurre en el grupo."),
        ex("¿Qué es la intimidad: tu mundo privado o todo lo que haces en el colegio?", "Tu mundo privado", "Incluye tu cuerpo, sentimientos y mensajes personales."),
    ],
    A=[
        ex("Camila anotó cuatro frases: 1) «me crecieron las piernas»; 2) «me da vergüenza que me miren»; 3) «mis amigos hablan de pololeo»; 4) «quiero cuidar a los demás». ¿Cuál es la dimensión ética?", "4", "Cuidar a los demás es un valor; las otras son biológica, afectiva y social."),
        ex("Un joven decide solo por lo que siente en el momento y no piensa en respeto ni consecuencias. ¿Qué dimensión deja fuera? A) La ética. B) La biológica.", "A", "Dejó de lado los valores como el respeto y la responsabilidad."),
        ex("Camila escribe un diario privado sobre sus sentimientos. ¿Quién decide si alguien lo lee?", "Ella", "La intimidad es suya y decide quién se entera."),
    ],
    Z=[
        ex("¿Por qué decidir mirando una sola dimensión puede llevar a equivocarse?", "Porque deja fuera cosas importantes", "Las dimensiones se influyen entre sí y deben considerarse juntas."),
        ex("Un compañero dice que hablar de los cambios del cuerpo es «cochino». ¿Qué respuesta respetuosa le darías?", "Que es normal hablar con respeto para cuidarse", "Entender los cambios ayuda a cuidar el cuerpo y la salud."),
    ],
    D=[
        arith("En una lista de 20 frases, 6 son de la dimensión biológica, 5 de la afectiva y 4 de la social. El resto son éticas. ¿Cuántas son éticas?", "20-6-5-4", "Al total se le restan las frases de las otras tres dimensiones."),
        arith("Un cuadro tiene 4 dimensiones y Camila escribe 3 ideas en cada una. ¿Cuántas ideas escribió?", "4*3", "Se multiplican las dimensiones por las ideas de cada una."),
    ],
    context=[ex("En la clase de Orientación, la profesora pregunta: «¿Qué dimensiones intervienen cuando alguien decide qué subir a una red social sobre su relación de pololeo?». Marcos responde: «Solo la tecnológica». ¿Cuál es la respuesta más completa según lo aprendido?", "Afectiva, social y ética, porque hay sentimientos, relaciones y respeto", "Se involucran sentimientos, vínculos con otros y valores como la privacidad.")],
    selfcheck=[ex("En Orientación: ¿la sexualidad tiene dimensiones biológica, afectiva, social y ética?", "Sí", "Son cuatro partes que se influyen."), ex("¿La intimidad incluye tus sentimientos y mensajes personales?", "Sí", "Es tu mundo privado."), ex("¿Decidir solo por lo que siento en el momento integra las dimensiones?", "No", "Deja fuera otras dimensiones.")],
    task=T("Lee el caso de Elías, un estudiante inventado: a los 13 años le cambió la voz, le gusta una compañera, sus amigos le preguntan si pololea y él quiere tratarla con respeto. Escribe una frase de Elías para cada dimensión: biológica, afectiva, social y ética. No cuentes nada personal tuyo.", "Biológica: mi voz cambió. Afectiva: me gusta una compañera y me da nervios. Social: mis amigos me preguntan si pololeo. Ética: quiero tratarla con respeto y sin presionar.", ["escribe una frase por cada dimensión", "usa los datos de Elías", "no cuenta nada personal", "usa un lenguaje respetuoso"], ["cuadro de cuatro columnas"], ["confundir afectiva con social", "reducir la sexualidad a relaciones sexuales"], "Reconoce las frases bien ubicadas y pregunta qué cambiaría si Elías olvidara la dimensión ética."),
    reinforce="Escribe una frase por dimensión sobre un personaje de cuento que está entrando a la adolescencia.",
    extend="Explica con tus palabras por qué las cuatro dimensiones deben pensarse juntas.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. El caso de Andrés y las situaciones de contacto están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos, emociones y derechos sobre mi cuerpo y mi intimidad, y a poner límites claros. Sirve para cuidar mi cuerpo y respetar el de los demás.",
    ["Sé que la sexualidad tiene cuatro dimensiones.", "Sé que la intimidad es mi mundo privado."],
    [
        "Tu cuerpo es tuyo. Eso significa que tienes derecho a decidir quién te toca y de qué manera. Las partes íntimas son las que cubre la ropa interior o el traje de baño. Nadie debe tocarlas ni mirarlas sin que sea necesario, por ejemplo en un examen médico con una persona de confianza presente, y nadie debe pedirte que las muestres ni que toques las de otra persona.",
        "El consentimiento es aceptar algo de forma libre, sin presión, engaño ni miedo. Un «sí» dicho por miedo o por presión no es un consentimiento verdadero. Y puede cambiar: lo que aceptaste ayer, hoy puedes no querer. Esto también aplica a los demás: si alguien dice «no», se aleja o parece incómodo, debes detenerte, aunque sea tu amigo o pololo. Respetar un «no» es respetar a la persona.",
        "Para decidir cómo actuar, separa los hechos de lo que sientes y de lo que otros dicen. Si alguien te hace sentir incómodo con un contacto, tu emoción es una señal importante y tienes derecho a poner un límite. Si la persona insiste, es mayor o te pide guardar un secreto, avisa a una persona adulta de confianza. Si te da miedo hablar con esa persona, no tienes que hacerlo: puedes alejarte y avisar directamente a un adulto. La responsabilidad nunca es de quien fue tocado sin su consentimiento.",
    ],
    [("partes íntimas", "partes del cuerpo que cubre la ropa interior o el traje de baño"), ("consentimiento", "aceptar algo de forma libre, sin presión, engaño ni miedo"), ("límite", "lo que acepto y lo que no respecto de mi cuerpo y mis cosas"), ("presión", "insistir para que alguien acepte algo que no quiere"), ("respeto", "aceptar que otra persona decida sobre su cuerpo y su vida")],
    [
        W("Reconocer una falta de consentimiento", "Andrés, un estudiante inventado, abraza a una compañera que baja la cabeza y se aleja. ¿Hubo consentimiento?", ["Ella se alejó y bajó la cabeza.", "Esas son señales de que no quiere.", "No hubo consentimiento."], "No hubo consentimiento: debió parar y respetar su señal"),
        W("Poner un límite", "Un compañero de otro curso le pone la mano en la espalda a Andrés y a él le incomoda. ¿Qué puede decir?", ["Debe nombrar lo que le incomoda con claridad.", "Debe pedir que pare.", "Si sigue, debe avisar a un adulto."], "Decir «No me gusta, saca tu mano» o alejarse, y avisar a un adulto de confianza si sigue"),
    ],
    [
        M("Pensar que si alguien no dijo «no» en voz alta, aceptó.", "Se ignoran las señales como alejarse, callar o bajar la mirada.", "Detente ante cualquier señal de incomodidad y pregunta con respeto."),
        M("Creer que un «sí» dicho por miedo o por presión sirve como consentimiento.", "Se confunde decir «sí» con aceptar libremente.", "El consentimiento debe ser libre, sin miedo ni presión."),
    ],
    R=[
        ex("¿Las partes íntimas son las que cubre la ropa interior o el traje de baño, sí o no?", "Sí", "Esa es la definición de partes íntimas."),
        ex("¿Se debe respetar un «no» de un amigo, sí o no?", "Sí", "Respetar un «no» es respetar a la persona."),
        ex("Si alguien se aleja cuando le quieres dar un abrazo, ¿debes insistir o detenerte?", "Detenerte", "Alejarse es una señal de que no quiere."),
    ],
    U=[
        ex("¿Por qué un «sí» dicho por miedo no es un consentimiento verdadero?", "Porque no es libre", "El consentimiento exige que no haya presión ni miedo."),
        ex("Ayer Lucía aceptó que le tomaran una foto, y hoy dice que no quiere. ¿Se respeta lo de ayer o lo de hoy?", "Lo de hoy", "El consentimiento puede cambiar en cualquier momento."),
        ex("Si te tocan de una manera que te incomoda, ¿tu emoción es una señal importante, sí o no?", "Sí", "Indica que debes poner un límite o pedir ayuda."),
    ],
    A=[
        ex("Situaciones: 1) «¿Puedo darte un abrazo?» y la otra dice sí contenta; 2) «Si no me dejas, no eres mi amigo»; 3) la otra baja la cabeza y calla; 4) «Cuando quieras, avísame». ¿Cuántas respetan el consentimiento?", "2", "Las situaciones 1 y 4 no presionan; la 2 chantajea y en la 3 hay señal de incomodidad ignorada."),
        ex("Un adulto le pide a Andrés guardar el secreto de un contacto que lo incomoda. ¿Qué debe hacer? A) Contárselo a una persona adulta de confianza. B) Guardar el secreto para no meterse en problemas.", "A", "Un secreto que incomoda debe contarse; la responsabilidad es del adulto."),
        ex("Andrés dice «no me gusta» y su compañero responde «era broma». ¿El límite sigue valiendo?", "Sí", "Aunque sea broma, quien se incomodó tiene derecho a que se respete su límite."),
    ],
    Z=[
        ex("Pía dice: «Como somos amigos, no necesito preguntarle si quiere que le dé un abrazo». ¿Qué error comete?", "Piensa que la amistad reemplaza el consentimiento", "Aun con amigos hay que respetar si la otra persona quiere o no."),
        ex("¿Por qué la responsabilidad nunca es de quien fue tocado sin su consentimiento?", "Porque la responsabilidad es de quien cruzó el límite", "Quien tocó sin permiso decidió hacerlo; no es culpa de la otra persona."),
    ],
    D=[
        arith("En una encuesta ficticia de 30 estudiantes, 24 saben qué es el consentimiento y el resto no. ¿Cuántos no lo saben?", "30-24", "Al total se le restan los que sí lo saben."),
        ex("Dos amigos, Nico y Pía, juegan a hacerse cosquillas. Pía dice «ya no» entre risas, y Nico sigue porque «se estaba riendo». ¿Qué debió hacer Nico y por qué?", "Parar de inmediato, porque ella dijo «ya no»", "Reírse no equivale a aceptar; un «no» claro se respeta aunque haya risa."),
    ],
    context=[ex("En una fiesta de cumpleaños ficticia, un grupo juega a retar a alguien a tocar a otro compañero. Rafaela no quiere y se lo dice. ¿Qué corresponde hacer al grupo?", "Parar el juego y respetar su «no»", "Un reto no reemplaza el consentimiento; nadie debe ser forzado.")],
    selfcheck=[ex("En Orientación: ¿mi cuerpo es mío y decido quién me toca?", "Sí", "Es un derecho de toda persona."), ex("¿Se puede cambiar de opinión después de haber aceptado algo?", "Sí", "El consentimiento puede retirarse en cualquier momento."), ex("¿La culpa es de quien fue tocado sin consentimiento?", "No", "La responsabilidad es de quien tocó.")],
    task=T("Lee los tres casos de personajes inventados: (1) Lucas le pide un abrazo a Emma y ella dice «hoy no»; él responde «está bien»; (2) Tomás insiste en tomarle una foto a Julia mientras ella tapa su cara; (3) Valeria ofrece un saludo con la mano y Marcos acepta. Para cada caso, escribe si se respeta el consentimiento y qué haría una persona respetuosa.", "(1) Sí, respeta el «hoy no». (2) No, Julia mostró que no quiere; debe parar y pedir permiso. (3) Sí, Valeria ofrece y Marcos acepta libremente.", ["clasifica los tres casos", "explica qué haría una persona respetuosa", "usa lenguaje respetuoso", "no cuenta una vivencia propia"], ["tabla escrita"], ["no respetar el «no»", "ignorar señales como taparse la cara"], "Reconoce la clasificación y pregunta qué otra manera de saludar habría sin contacto."),
    reinforce="Escribe una frase para decir «no» con respeto y otra para aceptar un «no» que te dicen.",
    extend="Explica por qué un secreto que te hace sentir incómodo debe contarse a un adulto de confianza.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. Las cuatro fuentes de información del cuadro están escritas en los ejercicios.",
    "Aprenderé a comparar fuentes de información sobre sexualidad y cambios del cuerpo y a elegir las apropiadas para mi edad. Sirve para resolver dudas sin caer en rumores ni contenido que no corresponde.",
    ["Sé que tengo derecho a cuidar mi intimidad.", "Sé que la sexualidad tiene dimensiones biológica, afectiva, social y ética."],
    [
        "Cuando tienes una duda sobre tu cuerpo o sobre las relaciones, necesitas una fuente de información apropiada. Una fuente es de donde sale un dato: una persona, un libro o un sitio. Es apropiada cuando es confiable, está pensada para tu edad y respeta tu dignidad. Algunas fuentes apropiadas son una persona adulta de confianza de tu familia, el profesor o la orientadora, el personal de salud del consultorio y los materiales de salud del Ministerio de Salud o del colegio.",
        "Hay fuentes que no son apropiadas. Los rumores del recreo suelen traer errores. Las páginas y videos con contenido sexual para adultos no son educación: muestran ideas falsas, no respetan a las personas y no son para menores. Los consejos de desconocidos en línea pueden ser engañosos o peligrosos. Un video de un influencer puede ser popular y aun así no ser confiable.",
        "Para evaluar una fuente hazte cuatro preguntas. ¿Quién lo dice y es una persona o institución con conocimiento? ¿Está pensado para mi edad? ¿Se puede comprobar con otra fuente? ¿Trata con respeto a las personas? Si la respuesta es no a alguna, busca otra fuente. Y si encuentras algo que te asusta o te incomoda, cuéntaselo a un adulto de confianza.",
    ],
    [("fuente", "lugar o persona de donde sale un dato"), ("confiable", "que tiene conocimiento y se puede comprobar"), ("rumor", "cosa que se dice sin comprobar"), ("apropiado", "adecuado para la edad y respetuoso"), ("comprobar", "revisar un dato en otra fuente")],
    [
        W("Evaluar una fuente", "Una duda: «¿Por qué cambia mi voz?». Una compañera dice «lo vi en un grupo». El personal de salud del consultorio explica los cambios de la pubertad. ¿Cuál fuente es más confiable?", ["El personal de salud tiene conocimiento y puede comprobarse.", "«Lo vi en un grupo» no dice quién lo afirma.", "Entonces es más confiable el personal de salud."], "El personal de salud del consultorio"),
        W("Aplicar las cuatro preguntas", "Un video popular de un desconocido dice «lo normal es que todos cambien a los 11 años». ¿Pasa las cuatro preguntas?", ["No se sabe quién lo dice ni si tiene conocimiento.", "Es falso: cada cuerpo cambia a distinto ritmo.", "Tampoco se puede comprobar."], "No pasa; es mejor consultar una fuente confiable"),
    ],
    [
        M("Creer que si algo tiene muchos «me gusta», es confiable.", "Se confunde popularidad con conocimiento.", "Verifica quién lo dice y compáralo con otra fuente."),
        M("Preguntarle solo a un amigo porque da vergüenza preguntar a un adulto.", "Se prefiere evitar la vergüenza aunque la información sea incorrecta.", "Elige una fuente apropiada: un adulto de confianza, profesional de salud o material oficial."),
    ],
    R=[
        ex("¿Una fuente apropiada puede ser el personal de salud del consultorio, sí o no?", "Sí", "Tiene conocimiento y atiende a adolescentes."),
        ex("¿Un rumor del recreo es una fuente confiable, sí o no?", "No", "No se comprueba y suele traer errores."),
        ex("¿Qué debes hacer si algo en internet te asusta o incomoda: ocultarlo o contárselo a un adulto de confianza?", "Contárselo a un adulto de confianza", "Un adulto puede ayudarte y protegerte."),
    ],
    U=[
        ex("¿Por qué el contenido sexual para adultos no es una fuente apropiada para aprender sobre sexualidad?", "Porque no es para menores y muestra ideas falsas", "No respeta a las personas ni está pensado para tu edad."),
        ex("¿Cuál de estas preguntas ayuda a evaluar una fuente: «¿Quién lo dice y tiene conocimiento?» o «¿Cuántos amigos lo vieron?»?", "«¿Quién lo dice y tiene conocimiento?»", "La cantidad de personas que lo vieron no prueba que sea cierto."),
        ex("Una fuente dice cosas que contradicen lo que explican tres profesionales de salud. ¿Cuál debes creer?", "Lo que explican los profesionales de salud", "Tienen conocimiento y sus datos pueden comprobarse."),
    ],
    A=[
        ex("Duda: «¿Es normal que mi amigo ya mida más que yo?». Fuentes: 1) un rumor; 2) la orientadora; 3) un desconocido en un chat; 4) un folleto del consultorio. ¿Cuántas son apropiadas?", "2", "La orientadora y el folleto del consultorio son fuentes confiables."),
        ex("Un chat de desconocidos te ofrece «consejos privados» sobre tu cuerpo. ¿Qué haces? A) Salgo del chat y se lo cuento a un adulto. B) Pregunto todo lo que quiera saber.", "A", "Los desconocidos en línea pueden engañar o ser peligrosos."),
        ex("Un video afirma que «la pubertad empieza igual en todas las personas». ¿Es verdadera la afirmación?", "No", "La pubertad empieza en edades distintas y todas son normales."),
    ],
    Z=[
        ex("Joaquín dice: «Prefiero preguntar en internet porque a un adulto me da vergüenza». ¿Qué riesgo corre?", "Encontrar información falsa o inapropiada", "En internet hay fuentes no confiables y contenido que no es para su edad."),
        ex("¿Por qué conviene comprobar un dato con otra fuente?", "Porque una sola fuente puede equivocarse", "Si dos fuentes confiables coinciden, el dato es más seguro."),
    ],
    D=[
        arith("En un cuestionario de 10 fuentes, Noelia marcó 6 como apropiadas, pero 2 estaban mal marcadas. ¿Cuántas marcó bien como apropiadas?", "6-2", "A las marcadas como apropiadas se le restan las mal marcadas."),
        arith("El curso evaluó 5 fuentes con 4 preguntas cada una. ¿Cuántas respuestas dieron?", "5*4", "Se multiplican las fuentes por las preguntas."),
    ],
    context=[ex("En el curso, un compañero dice que se enteró «de todo» por un video que le mandó un desconocido. Otro propone preguntarle a la orientadora y mirar el folleto del consultorio. ¿Quién propone una fuente apropiada?", "El que propone preguntarle a la orientadora y mirar el folleto", "Son personas e instituciones con conocimiento y pensadas para su edad.")],
    selfcheck=[ex("En Orientación: ¿una fuente apropiada es confiable y pensada para mi edad?", "Sí", "Además respeta la dignidad de las personas."), ex("¿Los rumores son buenas fuentes?", "No", "No se comprueban."), ex("¿Puedo contar a un adulto de confianza algo que me asustó en línea?", "Sí", "Es una acción segura.")],
    task=T("Lee las cuatro fuentes para una duda inventada («¿Por qué me salen granos?»): (1) una amiga que dice «es por lavarte poco»; (2) un video de un desconocido que vende una crema; (3) el personal de salud del consultorio que explica los cambios de la pubertad; (4) un folleto del colegio. Ordena de la más a la menos confiable y explica con dos de las cuatro preguntas por qué descartas una.", "Más confiables: 3 y 4. Menos: 1 y 2. Descarto el video: no se sabe si quien habla tiene conocimiento y busca vender.", ["ordena las fuentes", "usa al menos dos de las cuatro preguntas", "explica por qué descarta una", "no cuenta nada íntimo propio"], ["lista ordenada y texto breve"], ["creer lo más popular", "no justificar el orden"], "Reconoce el orden y pregunta qué otra fuente confiable agregaría."),
    reinforce="Escribe tres preguntas que sirvan para evaluar una fuente de información sobre salud.",
    extend="Explica por qué un influencer popular puede no ser una fuente confiable sobre el cuerpo.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. El caso de Sofía y Tomás, estudiantes inventados, y las frases de cada opción están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura y respetuosa en las relaciones de pololeo, amistad y mensajes en línea. Sirve para cuidar mi intimidad, respetar a los demás y evitar riesgos.",
    ["Sé reconocer el consentimiento.", "Sé evaluar fuentes de información."],
    [
        "Las relaciones pueden ser de amistad o de pololeo. En todas, el respeto es la base: no presionar, no insultar, no controlar ni humillar. Un signo de respeto es aceptar un «no». Un signo de falta de respeto es el chantaje, como «si me quieres, lo haces». También es una señal de alerta que te pidan la contraseña de tus cuentas, que revisen tu teléfono o que te digan con quién puedes hablar.",
        "En línea, la intimidad corre más riesgo. Las fotos o videos íntimos, es decir, aquellos en que se ve el cuerpo en ropa interior o sin ropa, no deben pedirse ni enviarse. Lo que se envía puede reenviarse y quedar para siempre. Si recibes una imagen íntima de alguien, no la reenvíes ni la guardes: avisa a un adulto de confianza. Compartir imágenes íntimas de otra persona la daña mucho y, si es menor de edad, puede ser un delito.",
        "Una acción segura es la que cuida tu cuerpo, tu intimidad y la de los demás. Si alguien te pide una foto íntima, dices «no», dejas de responder y se lo cuentas a un adulto. No es tu culpa si te lo piden. Si una persona adulta te escribe pidiendo fotos o encuentros a solas, también es una señal de peligro: no respondas, no borres el chat y avisa a un adulto.",
    ],
    [("pololeo", "relación afectiva entre dos personas basada en el cariño y el respeto"), ("chantaje", "presionar a alguien amenazándolo o haciéndolo sentir culpable"), ("control", "intentar decidir con quién habla o qué hace otra persona"), ("imagen íntima", "foto o video del cuerpo en ropa interior o sin ropa"), ("acción segura", "decisión que cuida mi cuerpo y mi intimidad")],
    [
        W("Detectar una señal de alerta", "Tomás, un estudiante inventado, le dice a Sofía: «Si de verdad me quieres, me pasas tu contraseña». ¿Qué señal es?", ["Pedir la contraseña es control.", "La frase condiciona el cariño a hacerlo.", "Es chantaje y control."], "Chantaje y control"),
        W("Elegir una acción segura", "Un chat le pide a Sofía una foto íntima y dice que «nadie se va a enterar». ¿Qué acción segura elige?", ["No debe enviar imágenes íntimas.", "Lo enviado puede reenviarse.", "Debe responder que no, dejar de contestar y avisar a un adulto."], "Decir que no, dejar de responder y avisar a un adulto"),
    ],
    [
        M("Pensar que si confío en la persona, puedo enviarle una foto íntima.", "Se cree que la confianza evita que la imagen se reenvíe.", "Nunca envíes imágenes íntimas: no puedes controlar lo que pasa después."),
        M("Creer que revisar el teléfono de mi pareja es una prueba de cariño.", "Se confunde control con cuidado.", "El respeto incluye la privacidad: nadie debe revisar tus mensajes sin permiso."),
    ],
    R=[
        ex("¿Aceptar un «no» es una señal de respeto, sí o no?", "Sí", "Respetar la decisión del otro es la base de la relación."),
        ex("¿Se debe reenviar una imagen íntima que recibiste, sí o no?", "No", "Reenviarla daña a la persona y puede ser delito."),
        ex("Si alguien dice «si me quieres, me mandas una foto íntima», ¿es chantaje o muestra de cariño?", "Chantaje", "Presiona haciendo sentir culpa."),
    ],
    U=[
        ex("¿Por qué no es buena idea enviar una foto íntima aunque confíes en la persona?", "Porque puede reenviarse y quedar para siempre", "No puedes controlar lo que ocurre con una imagen enviada."),
        ex("Si te piden una foto íntima, ¿es tu culpa que te lo hayan pedido?", "No", "La responsabilidad es de quien pide."),
        ex("Un adulto desconocido te escribe y pide verte a solas. ¿Es una señal de alerta o algo normal?", "Una señal de alerta", "Los adultos no deben pedir encuentros a solas a menores."),
    ],
    A=[
        ex("Frases de una pareja: 1) «Avísame si llegas bien»; 2) «Dame tu contraseña»; 3) «Con quién hablas, no me gusta»; 4) «Me gustó pasar tiempo contigo». ¿Cuántas muestran control?", "2", "Las frases 2 y 3 buscan controlar; las otras son cariño y respeto."),
        ex("Sofía recibe una imagen íntima de un compañero. ¿Qué hace? A) La reenvía a una amiga. B) No la reenvía y avisa a un adulto de confianza.", "B", "Reenviarla lo daña y puede ser delito."),
        ex("Un adulto que no conoces escribe a Sofía: «Mándame una foto sin ropa». ¿Qué pasos corresponden? 1) Responder; 2) No responder, no borrar el chat y avisar a un adulto.", "2", "Es una señal de peligro; se avisa y el chat queda como prueba."),
    ],
    Z=[
        ex("Valentina dice: «Mi pololo me pidió una foto íntima y me dijo que me quería; entonces está bien». ¿Qué error hay en su razonamiento?", "El cariño no justifica pedir imágenes íntimas", "Pedir ese tipo de fotos no es una muestra de respeto."),
        ex("¿Por qué avisar a un adulto cuando recibes una imagen íntima ayuda a proteger a la persona que aparece?", "Porque evita que se siga difundiendo", "Un adulto puede detener el reenvío y apoyar."),
    ],
    D=[
        arith("En una votación ficticia del curso sobre 20 frases de relaciones respetuosas, 14 se marcaron como respetuosas. ¿Cuántas se marcaron como no respetuosas?", "20-14", "Al total se le restan las respetuosas."),
        arith("Un grupo ficticio tenía 36 mensajes, y 9 eran de una persona. Ella no escribió el resto. ¿Cuántos mensajes escribieron los demás?", "36-9", "Al total se le restan los de esa persona."),
    ],
    context=[ex("En un grupo del curso circula una foto íntima de una compañera de otro colegio. Varios dicen que la reenviarán «porque ya todos la tienen». ¿Qué corresponde hacer?", "No reenviarla y avisar a un adulto", "Reenviarla amplía el daño y puede ser delito; un adulto puede ayudar.")],
    selfcheck=[ex("En Orientación: ¿el chantaje es una forma de cariño?", "No", "Es una forma de presión."), ex("¿Una foto íntima enviada puede reenviarse?", "Sí", "No se puede controlar."), ex("¿Si me piden una foto íntima, debo avisar a un adulto?", "Sí", "Es una acción segura.")],
    task=T("Lee el caso de Isidora, una estudiante inventada: un compañero que le gusta le escribe «mándame una foto sin polera, es solo para mí». Escribe qué le respondería con una frase corta, qué haría después y a qué persona adulta se lo contaría. Escribe además una señal de que esa petición no es respetuosa.", "Respuesta: «No, no envío eso». Después: dejar de contestar, no borrar el chat y no reenviar. Persona: su profesora jefe. Señal: pide una imagen íntima que puede reenviarse.", ["escribe una respuesta clara", "decide qué hace después", "nombra una persona adulta de confianza", "identifica una señal de falta de respeto"], ["texto escrito o dicho"], ["aceptar por confianza", "culparse por la petición"], "Reconoce la respuesta firme y pregunta qué haría si el compañero insiste."),
    reinforce="Escribe tres frases que muestren respeto en una relación y tres que muestren control.",
    extend="Explica por qué compartir la imagen íntima de otra persona la daña aunque se haga «de broma».",
)

lesson(
    OA2, 5,
    "Una hoja y un lápiz. Las frases del ensayo de comunicación y la lista de personas de ayuda están escritas en los ejercicios.",
    "Aprenderé a comunicar un límite con firmeza y a buscar ayuda cuando algo me incomoda. Sirve para cuidar mi cuerpo y mi intimidad, y para apoyar a otros.",
    ["Sé elegir acciones seguras ante petición de imágenes íntimas.", "Sé que el consentimiento debe ser libre."],
    [
        "Comunicar un límite con firmeza significa decir lo que quieres o no quieres, con voz clara y sin agresión. Una fórmula sencilla tiene tres partes: nombras lo que ocurre («me estás insistiendo»), dices cómo te sientes («me incomoda») y pides algo concreto («para, por favor»). Si la persona no respeta, puedes irte del lugar, bloquear el chat y avisar a un adulto. Si te da miedo decirlo, no estás obligado u obligada: puedes alejarte y avisar a un adulto sin hablar con esa persona. Si no sabes a quién acudir, puedes llamar gratis al Fono Niños 147.",
        "Existe una regla de oro: ningún secreto que te haga sentir incómodo, asustado o confundido debe guardarse. Los secretos que te piden mantener sobre contactos o fotos no deben guardarse. Cuéntalo a una persona adulta de confianza, aunque te hayan dicho que no lo hagas. Si el primero no te escucha, cuéntaselo a otro. La responsabilidad nunca es tuya.",
        "Las personas de ayuda pueden estar en tu casa o en el colegio: tu profesor o profesora jefe, el orientador o la orientadora, el equipo de convivencia escolar. Fuera del colegio, el personal de salud del consultorio. También puedes apoyar a un compañero que te cuenta algo difícil: escúchalo sin juzgar, dile que no es su culpa y ayúdalo a hablar con un adulto. No prometas guardar un secreto que lo ponga en riesgo.",
    ],
    [("límite firme", "decir con claridad lo que no acepto, sin agredir"), ("secreto que incomoda", "secreto que me hace sentir asustado, confundido o triste"), ("red de ayuda", "personas e instituciones a las que puedo acudir"), ("escuchar sin juzgar", "escuchar sin retar ni culpar"), ("bloquear", "impedir que alguien me escriba")],
    [
        W("Armar un mensaje de límite", "Un compañero le insiste a Paz, una estudiante inventada, para que le mande una foto. Usa la fórmula de tres partes.", ["Nombra lo que ocurre: «me estás insistiendo».", "Dice cómo se siente: «me incomoda».", "Pide algo concreto: «no vuelvas a pedírmelo»."], "«Me estás insistiendo y me incomoda; no vuelvas a pedírmelo»"),
        W("Apoyar a quien confía", "Un amigo cuenta a Paz que un adulto le pidió guardar un secreto sobre fotos. Le pide que no cuente. ¿Qué hace?", ["El secreto lo pone en riesgo.", "No debe prometer guardarlo.", "Debe ayudarlo a hablar con un adulto de confianza."], "No prometer guardarlo y ayudarlo a hablar con un adulto de confianza"),
    ],
    [
        M("Pensar que contar un secreto que incomoda es una traición.", "Se confunde lealtad con proteger a quien causa el daño.", "Proteger a la persona en riesgo es lo más leal."),
        M("Creer que gritar es la única forma de que me respeten.", "Se cree que sin gritos no hay firmeza.", "La firmeza es voz clara y mensaje directo, sin agredir."),
    ],
    R=[
        ex("¿La fórmula del límite firme tiene tres partes: nombrar lo que ocurre, decir cómo me siento y pedir algo concreto?", "Sí", "Son las tres partes explicadas."),
        ex("¿Un secreto que me incomoda se debe guardar, sí o no?", "No", "Debe contarse a un adulto de confianza."),
        ex("¿El orientador del colegio puede ser una persona de ayuda, sí o no?", "Sí", "Es una persona del colegio que apoya a estudiantes."),
    ],
    U=[
        ex("¿Por qué no debes prometer guardar un secreto que pone en riesgo a un amigo?", "Porque necesita ayuda de un adulto", "Guardarlo lo deja sin protección."),
        ex("¿Cuál frase es un límite firme: «Me incomoda, para por favor» o «Haz lo que quieras»?", "«Me incomoda, para por favor»", "Dice lo que siente y pide algo claro."),
        ex("Si un adulto de confianza no te escucha, ¿qué debes hacer?", "Contárselo a otra persona adulta de confianza", "Debes insistir hasta recibir ayuda."),
    ],
    A=[
        ex("Paz le dice a un compañero: «Me estás insistiendo y me incomoda; para, por favor». ¿Cuál es la parte que pide algo concreto?", "«para, por favor»", "Pide una acción clara; las otras partes nombran lo que ocurre y lo que siente."),
        ex("Un compañero te cuenta que alguien le pidió fotos. ¿Qué respuesta ayuda más? A) «No es tu culpa; hablemos con la orientadora». B) «Ya no lo comentes, no importa».", "A", "Lo apoya sin culparlo y lo conecta con ayuda."),
        ex("Paz quiere avisar a un adulto y duda a quién. ¿Cuál de estas personas sirve: su profesora jefe, un desconocido en línea o un compañero que no sabe qué hacer?", "Su profesora jefe", "Es una persona adulta de confianza del colegio."),
    ],
    Z=[
        ex("Camilo dice: «Si cuento lo que me pidió ese adulto, nadie me va a creer». ¿Qué respuesta le darías?", "Que insista con otro adulto de confianza hasta ser escuchado", "Hay más adultos y es importante que alguien lo sepa."),
        ex("¿Por qué un límite firme no necesita gritos?", "Porque la claridad hace que se entienda", "La voz clara y el mensaje directo bastan."),
    ],
    D=[
        ex("Una compañera cuenta que su pololo la insulta y le pidió no contárselo a nadie. ¿Debes guardar ese secreto o ayudarla a hablar con un adulto de confianza?", "Ayudarla a hablar con un adulto de confianza", "Un secreto que pone en riesgo a alguien no se guarda."),
        arith("De 25 estudiantes, 19 saben a quién avisar si algo los incomoda. ¿Cuántos no lo saben?", "25-19", "Al total se le restan los que sí lo saben."),
    ],
    context=[ex("Durante un juego en línea, un jugador mayor le pide a Catalina que pase a otro chat privado y que no le cuente a nadie. ¿Qué es lo más seguro?", "No pasar, no borrar el chat y avisar a un adulto", "Es una señal de peligro; un secreto así no se guarda.")],
    selfcheck=[ex("En Orientación: ¿puedo contar un secreto que me incomoda?", "Sí", "Debe contarse a un adulto de confianza."), ex("¿Un límite firme puede ser claro y respetuoso a la vez?", "Sí", "Se dice sin agredir."), ex("¿La responsabilidad es mía si alguien me pide algo indebido?", "No", "Es de quien lo pide.")],
    task=T("Escribe un guion corto con tres líneas para un personaje inventado, Dani, a quien un compañero le insiste en mostrarle un video que no quiere ver. Línea 1: lo que dice usando la fórmula de tres partes. Línea 2: lo que hace si no lo respeta. Línea 3: a qué persona adulta se lo cuenta y qué le dice.", "1) «Me estás insistiendo y me incomoda; no me lo muestres». 2) Se va del lugar. 3) A la orientadora: «Un compañero me insiste en mostrarme un video que no quiero ver».", ["usa la fórmula de tres partes", "decide qué hacer si no lo respetan", "nombra a una persona adulta de confianza", "no cuenta nada íntimo propio"], ["guion escrito"], ["usar insultos", "no avisar a un adulto"], "Reconoce la firmeza del guion y pregunta qué cambiaría si el compañero fuera un adulto."),
    reinforce="Practica la fórmula de tres partes con una situación inventada distinta.",
    extend="Explica cómo apoyarías a un compañero que te cuenta que alguien le pide fotos.",
)

lesson(
    OA2, 6,
    "Una hoja y un lápiz. Los tres casos nuevos y las dudas de ejemplo están escritos en los ejercicios. No cuentes experiencias personales.",
    "Aprenderé a usar lo que sé sobre sexualidad, cuidado del cuerpo, respeto y fuentes en situaciones nuevas, sin exponerme. Sirve para decidir con criterio cuando aparezca un caso distinto.",
    ["Sé evaluar fuentes de información.", "Sé comunicar un límite y pedir ayuda."],
    [
        "Transferir significa usar lo aprendido en un caso nuevo. Para eso sigue cuatro pasos. Primero, identifica qué dimensión de la sexualidad está en juego: biológica, afectiva, social o ética. Segundo, revisa si hay respeto, consentimiento y cuidado de la intimidad. Tercero, evalúa si la información viene de una fuente apropiada. Cuarto, decide qué acción segura tomar y a quién pedir ayuda.",
        "Un caso nuevo puede ser un rumor sobre el cuerpo de una compañera, un video con ideas falsas, un chat de pololeo con presión o una duda sobre un cambio del cuerpo. En todos, la dignidad de las personas se mantiene: no se humilla, no se reenvían imágenes ni se presiona. Y tú no tienes que contar tu vida para participar: puedes usar siempre un personaje inventado.",
        "Cuando una duda sea personal, puedes preguntar de forma privada a una persona adulta de confianza o al personal de salud. Hacer una pregunta no es de mal gusto: es una forma de cuidarte. Si ves que a otra persona la perjudican, avisa a un adulto de confianza y no participes del daño.",
    ],
    [("transferir", "usar lo aprendido en un caso nuevo"), ("dignidad", "valor que tiene toda persona y exige respeto"), ("rumor", "cosa que se dice sin comprobar"), ("difundir", "pasar información a muchas personas"), ("pregunta privada", "pregunta que hago a un adulto de confianza sin exponerme ante el curso")],
    [
        W("Aplicar los cuatro pasos", "Un rumor dice que una compañera «hizo cosas» con un chico. Nadie lo comprobó. ¿Qué haces primero según los pasos?", ["El rumor no se comprueba: no es una fuente apropiada.", "Difundirlo daña su dignidad.", "No lo reenvío y lo detengo si puedo."], "No difundir el rumor porque no es una fuente apropiada y daña su dignidad"),
        W("Elegir una acción", "Un compañero tiene una duda sobre un cambio de su cuerpo y le da vergüenza. ¿Qué acción segura le propones?", ["Una duda personal puede resolverse en privado.", "Una persona adulta de confianza o el personal de salud puede orientarlo.", "Eso evita fuentes dudosas."], "Preguntar en privado a un adulto de confianza o al personal de salud"),
    ],
    [
        M("Pensar que si un rumor es entretenido, da lo mismo difundirlo.", "Se ignora que el rumor puede dañar a una persona real.", "No difundas lo que no comprobaste ni lo que puede humillar."),
        M("Creer que para participar en la clase hay que contar mi propia experiencia.", "Se piensa que el tema obliga a exponerse.", "Puedes usar casos inventados y reservar lo personal."),
    ],
    R=[
        ex("¿Se debe reenviar un rumor sin comprobar, sí o no?", "No", "Puede dañar la dignidad de una persona."),
        ex("¿Se puede hacer una pregunta personal de forma privada a un adulto de confianza, sí o no?", "Sí", "Es una forma de cuidarse sin exponerse."),
        ex("Un video dice que la pubertad empieza igual en todos. ¿Es una fuente confiable o debe comprobarse?", "Debe comprobarse", "Cada cuerpo cambia a distinto ritmo."),
    ],
    U=[
        ex("¿Por qué el paso 2 pide revisar si hay respeto y consentimiento?", "Porque ahí se ve si alguien puede ser dañado", "Sin respeto ni consentimiento se afecta la dignidad."),
        ex("¿Qué es mejor en clase: contar una vivencia personal o analizar un personaje inventado?", "Analizar un personaje inventado", "Permite aprender sin exponerse."),
        ex("Quien recibe una imagen íntima de un tercero, ¿debe reenviarla o avisar a un adulto?", "Avisar a un adulto", "Reenviarla amplía el daño."),
    ],
    A=[
        ex("Caso: un chat del curso se burla del cuerpo de una compañera con una foto editada. Pasos: 1) no reenviar; 2) reírse; 3) avisar a un adulto. ¿Cuántos pasos son acciones seguras?", "2", "No reenviar y avisar a un adulto protegen a la compañera."),
        ex("Caso: Gaspar tiene una duda sobre su cuerpo y busca en un sitio desconocido. ¿Qué haces tú como compañero? A) Le sugiero preguntar en el consultorio o a un adulto de confianza. B) Le digo que mire todos los videos que encuentre.", "A", "Un adulto o un profesional de salud es una fuente apropiada."),
        ex("Caso: una compañera te dice que alguien en un videojuego le pide fotos. ¿Cuál es el mejor primer paso?", "Ayudarla a contárselo a un adulto de confianza", "La situación es riesgosa y necesita acompañamiento adulto."),
    ],
    Z=[
        ex("Un amigo dice: «Si no es mi problema, no hago nada». ¿Por qué avisar a un adulto sí puede ser tu responsabilidad?", "Porque puedes evitar que alguien siga siendo dañado", "Avisar es una acción segura que ayuda a quien está en riesgo."),
        ex("¿Por qué una persona puede usar un personaje inventado y aun así aprender para su vida?", "Porque las decisiones del personaje se parecen a las que enfrentará", "Analizar un caso permite practicar sin exponerse."),
    ],
    D=[
        ex("Un compañero afirma: «Si lo vi en tres videos distintos, es verdad». ¿Por qué eso no prueba que sea cierto?", "Porque los tres videos pueden repetir el mismo error", "Repetir una información no la vuelve verdadera; hay que comprobarla en una fuente confiable."),
        arith("De 32 estudiantes, 27 saben a quién acudir con una duda. ¿Cuántos no lo saben?", "32-27", "Al total se le restan los que sí lo saben."),
    ],
    context=[ex("Una influencer publica que «la verdadera confianza es mandar fotos» a quien te gusta. Un estudiante del curso lo comparte con su grupo. ¿Qué corresponde hacer al grupo?", "No difundirlo y recordar que las fotos íntimas no se envían", "El mensaje es riesgoso: lo enviado puede reenviarse y dañar a las personas.")],
    selfcheck=[ex("En Orientación: ¿puedo aplicar lo aprendido en un caso nuevo?", "Sí", "Eso es transferir."), ex("¿Hacer una pregunta personal a un adulto de confianza es una forma de cuidarse?", "Sí", "Permite resolver dudas con información apropiada."), ex("¿Debo contar experiencias personales para participar?", "No", "Puedo usar personajes inventados.")],
    task=T("Lee el caso inventado de Jaime: en el grupo del curso circula una foto de Marta con la palabra «mírenla» y varios la reenvían. Jaime sabe que a Marta no le gusta. Aplica los cuatro pasos: qué dimensión está en juego, si hay respeto y consentimiento, si la fuente es apropiada y qué acción segura tomaría Jaime.", "Dimensión: ética y social. No hay respeto ni consentimiento. La foto no informa nada: solo expone a Marta. Jaime no la reenvía ni reacciona, y avisa a un adulto de confianza.", ["aplica los cuatro pasos", "elige una acción segura", "nombra una persona adulta", "no cuenta nada personal"], ["texto escrito"], ["reenviar la foto", "culpar a Marta"], "Reconoce los cuatro pasos y pregunta qué diría Jaime a quienes reenvían."),
    reinforce="Aplica los cuatro pasos a un caso inventado nuevo.",
    extend="Explica por qué cuidar la dignidad de otros también es parte de la sexualidad integral.",
)
